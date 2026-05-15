import json
from pathlib import Path

import pytest

from feishu_message_archive.normalize import merge_and_normalize, normalize_one
from feishu_message_archive.render import render_digest

_FIX = Path(__file__).resolve().parent / "fixtures"


def _load(name: str) -> object:
    return json.loads((_FIX / name).read_text(encoding="utf-8"))


def test_merge_dedupes_and_classifies() -> None:
    broad = _load("search_broad.json")
    at_me = _load("search_at_me.json")
    merged = merge_and_normalize([broad, at_me], "ou_self")
    assert len(merged) == 3
    by_id = {m.message_id: m for m in merged}
    assert by_id["om_100"].is_self and by_id["om_100"].priority == "high"
    assert not by_id["om_101"].is_self and by_id["om_101"].priority == "normal"
    assert by_id["om_200"].mentions_me and by_id["om_200"].priority == "high"


def test_mentions_all_is_high_priority() -> None:
    raw = {
        "message_id": "om_x",
        "create_time": "0",
        "chat_id": "oc_1",
        "msg_type": "text",
        "sender": {"id": "ou_peer", "name": "X"},
        "content": "大家看一下",
        "mentions": [{"key": "all"}],
    }
    m = normalize_one(raw, "ou_self")
    assert m.mentions_all
    assert m.priority == "high"


def test_is_at_me_flag() -> None:
    raw = {
        "message_id": "om_y",
        "create_time": "0",
        "chat_id": "oc_1",
        "msg_type": "text",
        "sender": {"id": "ou_peer", "name": "X"},
        "content": "hi",
        "is_at_me": True,
    }
    m = normalize_one(raw, "ou_self")
    assert m.mentions_me
    assert m.priority == "high"


def test_render_digest_non_empty() -> None:
    broad = _load("search_broad.json")
    at_me = _load("search_at_me.json")
    merged = merge_and_normalize([broad, at_me], "ou_self")
    text = render_digest(merged, title="测试")
    assert "项目A" in text
    assert "重点" in text
