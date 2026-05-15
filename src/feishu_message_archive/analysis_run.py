"""Load archive artifacts and run LLM analysis."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from feishu_message_archive.analysis_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT_TEMPLATE,
    render_user_prompt,
)
from feishu_message_archive.llm_client import LLMClientError, chat_completion

logger = logging.getLogger(__name__)


def default_llm_settings() -> tuple[str, str, str]:
    """Return (api_key, base_url, model) from environment."""
    api_key = (
        os.environ.get("OPENAI_API_KEY", "").strip()
        or os.environ.get("LLM_API_KEY", "").strip()
    )
    base_url = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1").strip()
    model = os.environ.get("LLM_MODEL", "gpt-4o-mini").strip()
    return api_key, base_url, model


@dataclass
class AnalyzeParams:
    input_dir: Path
    output_path: Path | None = None
    extra_context: str | None = None
    max_bundle_chars: int = 120_000
    api_key: str | None = None
    base_url: str | None = None
    model: str | None = None
    system_prompt: str | None = None
    user_prompt_template: str | None = None


@dataclass
class AnalyzeResult:
    outcome: Literal["ok", "error"]
    markdown: str | None = None
    output_path: Path | None = None
    error_message: str | None = None
    bundle_chars: int = 0


def load_archive_bundle(input_dir: Path, *, max_chars: int) -> tuple[int, str]:
    """
    Load digest.md and messages.jsonl from input_dir into one prompt-sized string.

    Returns (approx_char_count, text).
    """
    digest_path = input_dir / "digest.md"
    jsonl_path = input_dir / "messages.jsonl"
    chunks: list[str] = []

    if digest_path.is_file():
        chunks.append("# digest.md\n" + digest_path.read_text(encoding="utf-8"))
    if jsonl_path.is_file():
        raw = jsonl_path.read_text(encoding="utf-8")
        half = max(max_chars // 2, 10_000)
        if len(raw) > half:
            raw = (
                raw[:half]
                + "\n\n...[messages.jsonl 已截断：内容过长，仅保留前段；如需更多上下文可调大 max_bundle_chars 或分段归档]...\n"
            )
        chunks.append("# messages.jsonl\n" + raw)

    if not chunks:
        raise FileNotFoundError(
            f"未找到 digest.md 或 messages.jsonl：{input_dir}"
        )

    combined = "\n\n".join(chunks)
    if len(combined) > max_chars:
        combined = (
            combined[:max_chars]
            + "\n\n...[总长度超过限制已截断；可在调用侧增大 max_bundle_chars]...\n"
        )
    return len(combined), combined


def run_analysis(params: AnalyzeParams) -> AnalyzeResult:
    """Read archive folder, call LLM, optionally write analysis markdown file."""
    dk, bu, mm = default_llm_settings()
    api_key = (params.api_key or dk).strip()
    base_url = (params.base_url or bu).strip()
    model = (params.model or mm).strip()

    if not api_key:
        return AnalyzeResult(
            outcome="error",
            error_message=(
                "未配置 API Key。请在环境变量中设置 OPENAI_API_KEY 或 LLM_API_KEY；"
                "可选 LLM_BASE_URL（默认 OpenAI）、LLM_MODEL（默认 gpt-4o-mini）。"
            ),
        )

    try:
        bundle_chars, bundle = load_archive_bundle(
            params.input_dir,
            max_chars=params.max_bundle_chars,
        )
    except FileNotFoundError as e:
        return AnalyzeResult(outcome="error", error_message=str(e))
    except OSError as e:
        return AnalyzeResult(outcome="error", error_message=f"读取归档失败: {e}")

    system_prompt = (params.system_prompt or SYSTEM_PROMPT).strip() or SYSTEM_PROMPT
    user_template = (
        params.user_prompt_template or USER_PROMPT_TEMPLATE
    ).strip() or USER_PROMPT_TEMPLATE
    user_body = render_user_prompt(
        archive_bundle=bundle,
        extra_context=params.extra_context,
        template=user_template,
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_body},
    ]

    try:
        md = chat_completion(
            messages=messages,
            model=model,
            api_key=api_key,
            base_url=base_url,
        )
    except LLMClientError as e:
        logger.error("%s", e)
        return AnalyzeResult(
            outcome="error",
            bundle_chars=bundle_chars,
            error_message=str(e),
        )

    out = params.output_path
    if out is None:
        out = params.input_dir / "analysis.md"

    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md, encoding="utf-8")
        logger.info("wrote analysis to %s", out)
    except OSError as e:
        return AnalyzeResult(
            outcome="error",
            markdown=md,
            bundle_chars=bundle_chars,
            error_message=f"分析已完成但写入文件失败: {e}",
        )

    return AnalyzeResult(
        outcome="ok",
        markdown=md,
        output_path=out,
        bundle_chars=bundle_chars,
    )
