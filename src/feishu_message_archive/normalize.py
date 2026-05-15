"""Normalize lark-cli search payloads into deduplicated, classified records."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class NormalizedMessage:
    message_id: str
    create_time: str
    chat_id: str
    chat_name: str | None
    chat_type: str | None
    msg_type: str | None
    sender_id: str | None
    sender_name: str | None
    content: str
    deleted: bool
    updated: bool
    thread_id: str | None
    mentions: list[dict[str, Any]] = field(default_factory=list)
    is_self: bool = False
    mentions_me: bool = False
    mentions_all: bool = False
    priority: str = "normal"  # high | normal


def extract_messages(payload: Any) -> list[dict[str, Any]]:
    """Extract message list from lark-cli +messages-search JSON root."""
    if payload is None:
        return []
    if isinstance(payload, list):
        return [x for x in payload if isinstance(x, dict)]
    if not isinstance(payload, dict):
        return []
    for key in ("messages", "items", "records", "list"):
        val = payload.get(key)
        if isinstance(val, list):
            return [x for x in val if isinstance(x, dict)]
    data = payload.get("data")
    if isinstance(data, dict):
        return extract_messages(data)
    return []


def _sender_ids(sender: Any) -> tuple[str | None, str | None]:
    if not isinstance(sender, dict):
        return None, None
    sid = sender.get("id") or sender.get("open_id") or sender.get("openId")
    name = sender.get("name") or sender.get("display_name")
    if isinstance(sid, str):
        return sid, str(name) if name is not None else None
    return None, str(name) if name is not None else None


def _parse_mentions(raw: Any) -> list[dict[str, Any]]:
    if raw is None:
        return []
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except json.JSONDecodeError:
            return []
    if not isinstance(raw, list):
        return []
    out: list[dict[str, Any]] = []
    for item in raw:
        if isinstance(item, dict):
            out.append(item)
    return out


def _mentions_flags(
    mentions: list[dict[str, Any]],
    self_open_id: str,
) -> tuple[bool, bool]:
    mentions_me = False
    mentions_all = False
    for m in mentions:
        mid = m.get("id")
        key = m.get("key")
        if key == "all" or mid == "all":
            mentions_all = True
        if isinstance(mid, str) and mid == self_open_id:
            mentions_me = True
    return mentions_me, mentions_all


def normalize_one(raw: dict[str, Any], self_open_id: str) -> NormalizedMessage:
    """Map one search result dict to NormalizedMessage."""
    message_id = str(raw.get("message_id") or raw.get("messageId") or "")
    sender_id, sender_name = _sender_ids(raw.get("sender"))
    mentions = _parse_mentions(raw.get("mentions"))
    mentions_me, mentions_all = _mentions_flags(mentions, self_open_id)
    if raw.get("is_at_me") is True or raw.get("at_me") is True:
        mentions_me = True
    is_self = bool(sender_id and sender_id == self_open_id)

    priority = "normal"
    if is_self or mentions_me or mentions_all:
        priority = "high"

    return NormalizedMessage(
        message_id=message_id,
        create_time=str(raw.get("create_time") or raw.get("createTime") or ""),
        chat_id=str(raw.get("chat_id") or raw.get("chatId") or ""),
        chat_name=_optional_str(raw.get("chat_name") or raw.get("chatName")),
        chat_type=_optional_str(raw.get("chat_type") or raw.get("chatType")),
        msg_type=_optional_str(raw.get("msg_type") or raw.get("msgType")),
        sender_id=sender_id,
        sender_name=sender_name,
        content=str(raw.get("content") or ""),
        deleted=bool(raw.get("deleted")),
        updated=bool(raw.get("updated")),
        thread_id=_optional_str(raw.get("thread_id") or raw.get("threadId")),
        mentions=mentions,
        is_self=is_self,
        mentions_me=mentions_me,
        mentions_all=mentions_all,
        priority=priority,
    )


def _optional_str(val: Any) -> str | None:
    if val is None:
        return None
    s = str(val).strip()
    return s if s else None


def merge_and_normalize(
    payloads: list[Any],
    self_open_id: str,
) -> list[NormalizedMessage]:
    """Merge multiple search payloads, dedupe by message_id, sort by create_time."""
    by_id: dict[str, NormalizedMessage] = {}
    for payload in payloads:
        for row in extract_messages(payload):
            nm = normalize_one(row, self_open_id)
            if not nm.message_id:
                continue
            by_id[nm.message_id] = nm
    messages = list(by_id.values())
    messages.sort(key=lambda m: m.create_time or "")
    return messages


def to_jsonl_line(msg: NormalizedMessage) -> str:
    return json.dumps(asdict(msg), ensure_ascii=False)
