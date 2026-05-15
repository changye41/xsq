"""Filter messages by excluded chat display names (post-fetch)."""

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import Literal

from feishu_message_archive.normalize import NormalizedMessage

# Split user input on newlines, commas, or Chinese comma /顿号
_SPLIT_RE = re.compile(r"[\n\r,，、;；]+")


def parse_exclude_chat_names(raw: str | None) -> list[str]:
    """
    Parse a user-provided block into non-empty unique patterns (order preserved).

    Accepts multiple lines, or comma / Chinese comma / semicolon separated values.
    """
    if not raw:
        return []
    parts = _SPLIT_RE.split(raw.strip())
    out: list[str] = []
    seen: set[str] = set()
    for p in parts:
        s = p.strip()
        if not s:
            continue
        key = s.casefold()
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
    return out


def _fold(s: str | None) -> str:
    if not s:
        return ""
    return s.strip().casefold()


def is_chat_excluded(
    chat_name: str | None,
    patterns: list[str],
    *,
    match: Literal["substring", "exact"] = "substring",
) -> bool:
    """
    Return True if this message's chat should be dropped.

    - ``substring`` (default): excluded when any pattern is a case-insensitive substring of chat_name.
    - ``exact``: excluded when chat_name equals any pattern (after strip, case-insensitive).

    If ``chat_name`` is missing/empty, never matches (cannot reliably apply name rules).
    """
    if not patterns:
        return False
    name_fold = _fold(chat_name)
    if not name_fold:
        return False
    for pat in patterns:
        p_fold = _fold(pat)
        if not p_fold:
            continue
        if match == "exact":
            if name_fold == p_fold:
                return True
        else:
            if p_fold in name_fold:
                return True
    return False


def filter_messages_by_chat_name(
    messages: Iterable[NormalizedMessage],
    patterns: list[str],
    *,
    match: Literal["substring", "exact"],
) -> tuple[list[NormalizedMessage], int]:
    """Return (kept_list, excluded_count)."""
    if not patterns:
        return list(messages), 0
    kept: list[NormalizedMessage] = []
    excluded = 0
    for m in messages:
        if is_chat_excluded(m.chat_name, patterns, match=match):
            excluded += 1
        else:
            kept.append(m)
    return kept, excluded
