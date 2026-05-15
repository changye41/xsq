"""Shared archive run logic for CLI and UI."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from pathlib import Path
from typing import Literal
from zoneinfo import ZoneInfo

from feishu_message_archive.lark_cli import (
    LarkCliError,
    get_self_open_id,
    messages_search,
    resolve_lark_cli,
)
from feishu_message_archive.filter_chats import filter_messages_by_chat_name
from feishu_message_archive.normalize import merge_and_normalize, to_jsonl_line
from feishu_message_archive.render import render_digest


def day_bounds_iso(dstr: str, tz_name: str) -> tuple[str, str]:
    """Return ISO8601 start/end for a calendar day in the given IANA timezone."""
    d = date.fromisoformat(dstr)
    tz = ZoneInfo(tz_name)
    start = datetime(d.year, d.month, d.day, 0, 0, 0, tzinfo=tz)
    end = start + timedelta(days=1) - timedelta(seconds=1)
    return start.isoformat(timespec="seconds"), end.isoformat(timespec="seconds")


def combine_date_time_to_iso(
    d: date,
    t: time,
    tz_name: str,
) -> str:
    """Combine date + time with timezone into ISO8601 string with offset."""
    tz = ZoneInfo(tz_name)
    dt = datetime(d.year, d.month, d.day, t.hour, t.minute, t.second, tzinfo=tz)
    return dt.isoformat(timespec="seconds")


@dataclass
class ArchiveParams:
    """Parameters for one archive run."""

    mode: Literal["date", "range"]
    timezone: str
    output_dir: Path
    lark_cli: str | None = None
    page_limit: int | None = None
    chat_id: str | None = None
    skip_at_me_pass: bool = False
    # Exclude chats by display name (applied after fetch; substring or exact match, case-insensitive)
    exclude_chat_names: tuple[str, ...] = ()
    exclude_chat_match: Literal["substring", "exact"] = "substring"
    # mode date
    calendar_date: str | None = None  # YYYY-MM-DD
    # mode range
    start_iso: str | None = None
    end_iso: str | None = None


@dataclass
class ArchiveResult:
    outcome: Literal["ok", "error"]
    message_count: int = 0
    high_priority_count: int = 0
    jsonl_path: Path | None = None
    digest_path: Path | None = None
    digest_text: str | None = None
    title_label: str = ""
    error_message: str | None = None
    fetched_count: int = 0
    excluded_by_chat_name: int = 0
    archive_dir: Path | None = None


def resolve_time_window(params: ArchiveParams) -> tuple[str, str, str]:
    """
    Return (start_iso, end_iso, title_label).

    Raises ValueError on invalid parameter combinations.
    """
    if params.mode == "date":
        if not params.calendar_date:
            raise ValueError("calendar_date is required for mode=date")
        start, end = day_bounds_iso(params.calendar_date, params.timezone)
        return start, end, params.calendar_date
    if params.mode == "range":
        if not params.start_iso or not params.end_iso:
            raise ValueError("start_iso and end_iso are required for mode=range")
        return params.start_iso, params.end_iso, f"{params.start_iso} — {params.end_iso}"
    raise ValueError(f"unknown mode: {params.mode}")


_SAFE_NAME_RE = re.compile(r"[^0-9A-Za-z._-]+")


def _safe_name(text: str, *, default: str = "window") -> str:
    """Filesystem-safe token for directory names."""
    cleaned = _SAFE_NAME_RE.sub("_", text).strip("._-")
    if not cleaned:
        return default
    return cleaned[:80]


def build_export_dir(output_root: Path, title_label: str) -> Path:
    """
    Build unique export directory path containing:
    - chat record time window token (title_label)
    - export timestamp
    """
    window = _safe_name(title_label, default="window")
    export_ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    return output_root / f"{window}__export_{export_ts}"


def run_archive(
    params: ArchiveParams,
    *,
    logger: logging.Logger | None = None,
) -> ArchiveResult:
    """Execute search, normalize, write JSONL + digest. Returns ArchiveResult."""
    log = logger or logging.getLogger(__name__)
    try:
        start, end, title_label = resolve_time_window(params)
    except ValueError as e:
        return ArchiveResult(outcome="error", error_message=str(e))

    out_dir = params.output_dir
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        return ArchiveResult(
            outcome="error",
            error_message=f"无法创建输出目录 {out_dir}: {e}",
        )

    try:
        exe = resolve_lark_cli(params.lark_cli)
        self_id = get_self_open_id(exe)
        log.info("current user open_id: %s", self_id)

        payloads: list[object] = []
        log.info("searching messages (broad pass): %s .. %s", start, end)
        payloads.append(
            messages_search(
                exe,
                query="",
                start=start,
                end=end,
                page_all=True,
                page_limit=params.page_limit,
                is_at_me=False,
                chat_id=params.chat_id,
            )
        )
        if not params.skip_at_me_pass:
            log.info("searching messages (@me pass): %s .. %s", start, end)
            payloads.append(
                messages_search(
                    exe,
                    query="",
                    start=start,
                    end=end,
                    page_all=True,
                    page_limit=params.page_limit,
                    is_at_me=True,
                    chat_id=params.chat_id,
                )
            )

        merged = merge_and_normalize(payloads, self_id)
        fetched_n = len(merged)
        patterns = list(params.exclude_chat_names)
        excluded_n = 0
        if patterns:
            merged, excluded_n = filter_messages_by_chat_name(
                merged,
                patterns,
                match=params.exclude_chat_match,
            )
            log.info(
                "excluded %s messages by chat name (%s match, %s patterns)",
                excluded_n,
                params.exclude_chat_match,
                len(patterns),
            )
        high_n = sum(1 for m in merged if m.priority == "high")

        archive_dir = build_export_dir(out_dir, title_label)
        archive_dir.mkdir(parents=True, exist_ok=True)

        jsonl_path = archive_dir / "messages.jsonl"
        with jsonl_path.open("w", encoding="utf-8") as f:
            for m in merged:
                f.write(to_jsonl_line(m) + "\n")

        digest_path = archive_dir / "digest.md"
        digest_body = render_digest(merged, title=f"飞书消息归档 {title_label}")
        if patterns:
            preview = "、".join(patterns[:8])
            if len(patterns) > 8:
                preview += f" 等共 {len(patterns)} 项"
            digest_body += (
                "\n\n---\n\n"
                f"_已启用「不统计群聊」过滤：**{params.exclude_chat_match}** 匹配；"
                f"模式：{preview}。拉取 **{fetched_n}** 条，排除 **{excluded_n}** 条，保留 **{len(merged)}** 条。_\n"
            )
        digest_path.write_text(digest_body, encoding="utf-8")

        log.info("wrote %s (%s messages)", jsonl_path, len(merged))
        return ArchiveResult(
            outcome="ok",
            message_count=len(merged),
            high_priority_count=high_n,
            jsonl_path=jsonl_path,
            digest_path=digest_path,
            digest_text=digest_body,
            title_label=title_label,
            fetched_count=fetched_n,
            excluded_by_chat_name=excluded_n,
            archive_dir=archive_dir,
        )
    except LarkCliError as e:
        log.error("%s", e)
        return ArchiveResult(outcome="error", error_message=str(e))
