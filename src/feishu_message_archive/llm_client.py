"""OpenAI-compatible Chat Completions client (uses httpx)."""

from __future__ import annotations

import json
import logging
from typing import Any

logger = logging.getLogger(__name__)


class LLMClientError(RuntimeError):
    """HTTP or API-level failure from the LLM endpoint."""


def _llm_http_error_detail(status_code: int, body: str) -> str:
    """Build user-visible error string with optional Chinese hint for quota/billing."""
    snippet = (body or "")[:1200]
    base = f"LLM API error HTTP {status_code}: {snippet}"
    low = snippet.lower()
    if status_code == 402:
        return (
            base
            + "\n\n【处理方式】HTTP 402 通常与 **付费/配额** 有关：请到模型服务商控制台检查套餐、账单或充值。"
        )
    if status_code == 429:
        if any(
            kw in low
            for kw in (
                "balance",
                "quota",
                "billing",
                "recharge",
                "suspended",
                "insufficient",
                "exceeded_current_quota",
                "payment",
            )
        ):
            return (
                base
                + "\n\n【处理方式】当前返回与 **账户余额不足 / 套餐配额用尽 / 账号暂停** 等相关。"
                "请到该 API 所属平台 **充值、升级套餐或核对账单**；确认后可更换其它可用的 API Key 或兼容网关（在侧栏修改 Base URL 与 Key）。"
                "\n该错误由 **模型服务商** 返回，与飞书归档程序本身无关。"
            )
        return (
            base
            + "\n\n【提示】HTTP 429 也可能是 **请求过于频繁**，请稍后重试或降低调用频率。"
        )
    return base


def _require_httpx():
    try:
        import httpx
    except ImportError as e:
        raise LLMClientError(
            'Missing dependency httpx. Install with: pip install -e ".[analyze]"'
        ) from e
    return httpx


def chat_completion(
    *,
    messages: list[dict[str, str]],
    model: str,
    api_key: str,
    base_url: str,
    timeout_s: float = 180.0,
) -> str:
    """
    POST /chat/completions (OpenAI-compatible).
    base_url should be like https://api.openai.com/v1 (no trailing slash required).
    """
    httpx = _require_httpx()
    url = base_url.rstrip("/") + "/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": 0.35,
    }
    try:
        with httpx.Client(timeout=timeout_s) as client:
            resp = client.post(url, headers=headers, json=payload)
    except httpx.HTTPError as e:
        logger.exception("LLM HTTP error")
        raise LLMClientError(f"LLM request failed: {e}") from e

    if resp.status_code >= 400:
        log_snip = (resp.text or "")[:800]
        logger.error("LLM error status=%s body=%s", resp.status_code, log_snip)
        raise LLMClientError(
            _llm_http_error_detail(resp.status_code, resp.text or "")
        )

    try:
        data = resp.json()
    except json.JSONDecodeError as e:
        raise LLMClientError("LLM response is not JSON") from e

    choices = data.get("choices")
    if not choices or not isinstance(choices, list):
        raise LLMClientError(
            "Unexpected LLM response shape: " + repr(data)[:500]
        )

    msg = choices[0].get("message") or {}
    content = msg.get("content")
    if not isinstance(content, str) or not content.strip():
        raise LLMClientError("LLM returned empty content")
    return content.strip()
