"""Export analysis markdown to Feishu Doc with deduplicated title."""

from __future__ import annotations

import re
from datetime import datetime
from dataclasses import dataclass
from html import escape
from pathlib import Path
from uuid import uuid4
from typing import Any

from feishu_message_archive.lark_cli import LarkCliError, resolve_lark_cli, run_lark_json

_TITLE_PREFIX_RE = re.compile(r"^#\s*飞书消息归档\s+(.+?)\s*$")
_NUMBERED_TITLE_RE = re.compile(r"^(?P<base>.+?)（(?P<n>\d+)）$")
_MAX_SEARCH_QUERY_LEN = 30
_OUTER_FENCE_RE = re.compile(
    r"^\s*```(?:markdown|md)?\s*\n(?P<body>[\s\S]*?)\n```\s*$",
    re.IGNORECASE,
)


@dataclass
class FeishuDocResult:
    ok: bool
    title: str = ""
    url: str | None = None
    doc_id: str | None = None
    error: str | None = None


def archive_label_from_dir(input_dir: Path) -> str:
    """Try extracting the archive date/window label from digest or directory name."""
    digest = input_dir / "digest.md"
    if digest.is_file():
        first = digest.read_text(encoding="utf-8").splitlines()
        if first:
            m = _TITLE_PREFIX_RE.match(first[0].strip())
            if m:
                return m.group(1).strip()
    # fallback: "<window>__export_yyyymmdd-hhmmss"
    stem = input_dir.name.split("__export_", 1)[0]
    return stem.replace("_", " ").strip() or "未知日期"


def format_archive_title_label(raw_label: str) -> str:
    """
    Convert ISO-range label to compact title style.

    Example:
      2026-05-12T08:00:00+08:00 — 2026-05-12T22:00:00+08:00
      -> 5.12 8-22
    """
    parts = [p.strip() for p in raw_label.split("—")]
    if len(parts) == 2:
        try:
            s = datetime.fromisoformat(parts[0])
            e = datetime.fromisoformat(parts[1])
            if s.date() == e.date():
                return f"{s.month}.{s.day} {s.hour}-{e.hour}"
            return f"{s.month}.{s.day} {s.hour}-{e.month}.{e.day} {e.hour}"
        except ValueError:
            pass
    return raw_label


def _collect_titles(node: Any) -> list[str]:
    titles: list[str] = []
    if isinstance(node, dict):
        for k in ("title", "name"):
            v = node.get(k)
            if isinstance(v, str) and v.strip():
                titles.append(v.strip())
        for v in node.values():
            titles.extend(_collect_titles(v))
    elif isinstance(node, list):
        for item in node:
            titles.extend(_collect_titles(item))
    return titles


def pick_next_title(existing_titles: list[str], base_title: str) -> str:
    """If base title exists, append full-width numbered suffix."""
    nums: set[int] = set()
    base_exists = False
    for t in existing_titles:
        if t == base_title:
            base_exists = True
            nums.add(1)
            continue
        m = _NUMBERED_TITLE_RE.match(t)
        if m and m.group("base") == base_title:
            nums.add(int(m.group("n")))
    if not base_exists and not nums:
        return base_title
    n = 1
    while n in nums:
        n += 1
    return f"{base_title}（{n}）"


def _existing_similar_titles(lark_cli: str, base_title: str) -> list[str]:
    # Lark drive +search currently validates query max length=30.
    query = base_title[:_MAX_SEARCH_QUERY_LEN]
    data = run_lark_json(
        [
            lark_cli,
            "drive",
            "+search",
            "--as",
            "user",
            "--query",
            query,
            "--only-title",
            "--doc-types",
            "doc,docx",
            "--format",
            "json",
        ],
        timeout_s=60.0,
    )
    titles = _collect_titles(data)
    # keep only same base or numbered variants to avoid fuzzy noise
    out: list[str] = []
    for t in titles:
        if t == base_title:
            out.append(t)
            continue
        m = _NUMBERED_TITLE_RE.match(t)
        if m and m.group("base") == base_title:
            out.append(t)
    return out


def _build_doc_markdown(title: str, analysis_markdown: str) -> str:
    """Build final markdown body with required lark-cli source annotation."""
    body = normalize_analysis_markdown(analysis_markdown)
    # Title is created explicitly via XML `<title>` in step 1.
    # Here we only keep analysis body content.
    return (
        f"{body}\n\n"
        "---\n"
        "本[文档]由飞书工具 Lark-Cli 创建\n"
    )


def normalize_analysis_markdown(text: str) -> str:
    """
    Normalize model markdown so doc import keeps semantic formatting.

    If the whole response is wrapped by a single fenced code block
    (```markdown ... ```), unwrap it to plain markdown content.
    """
    s = (text or "").strip()
    m = _OUTER_FENCE_RE.match(s)
    if m:
        return m.group("body").strip()
    return s


def create_feishu_doc_from_analysis(
    *,
    input_dir: Path,
    analysis_markdown: str,
    lark_cli_path: str | None = None,
) -> FeishuDocResult:
    """Create a Feishu Doc (docs +create v2 markdown), handling title collisions."""
    try:
        lark_cli = resolve_lark_cli(lark_cli_path)
        label = format_archive_title_label(archive_label_from_dir(input_dir))
        base_title = f"{label}飞书信息归档"
        existing = _existing_similar_titles(lark_cli, base_title)
        title = pick_next_title(existing, base_title)

        content_md = _build_doc_markdown(title, analysis_markdown)
        # lark-cli validates --content @file as a relative path in current directory.
        temp_md_name = f".feishu_doc_upload_{uuid4().hex}.md"
        temp_md = input_dir / temp_md_name
        temp_md.write_text(content_md, encoding="utf-8")
        temp_xml_name = f".feishu_doc_create_{uuid4().hex}.xml"
        temp_xml = input_dir / temp_xml_name
        temp_xml.write_text(
            f"<title>{escape(title)}</title><p>AI分析结果</p>",
            encoding="utf-8",
        )
        try:
            # Step 1: create doc with explicit XML title to avoid "Untitled".
            create_res = run_lark_json(
                [
                    lark_cli,
                    "docs",
                    "+create",
                    "--api-version",
                    "v2",
                    "--as",
                    "user",
                    "--doc-format",
                    "xml",
                    "--content",
                    f"@{temp_xml_name}",
                ],
                cwd=input_dir,
                timeout_s=90.0,
            )
            doc = (
                (create_res.get("data") or {}).get("document")
                if isinstance(create_res, dict)
                else None
            )
            if not isinstance(doc, dict):
                return FeishuDocResult(ok=False, error=f"创建文档成功响应异常: {create_res!r}"[:500])
            doc_id = doc.get("document_id")
            if not isinstance(doc_id, str) or not doc_id:
                return FeishuDocResult(ok=False, error=f"创建文档缺少 document_id: {create_res!r}"[:500])

            # Step 2: append markdown analysis body.
            run_lark_json(
                [
                    lark_cli,
                    "docs",
                    "+update",
                    "--api-version",
                    "v2",
                    "--as",
                    "user",
                    "--doc",
                    doc_id,
                    "--command",
                    "append",
                    "--doc-format",
                    "markdown",
                    "--content",
                    f"@{temp_md_name}",
                ],
                cwd=input_dir,
                timeout_s=120.0,
            )
        finally:
            try:
                temp_md.unlink(missing_ok=True)
            except OSError:
                pass
            try:
                temp_xml.unlink(missing_ok=True)
            except OSError:
                pass
        return FeishuDocResult(
            ok=True,
            title=title,
            url=doc.get("url"),
            doc_id=doc.get("document_id"),
        )
    except LarkCliError as e:
        return FeishuDocResult(ok=False, error=str(e))
