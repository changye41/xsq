"""Tests for chat name exclusion helpers."""

from feishu_message_archive.filter_chats import (
    filter_messages_by_chat_name,
    is_chat_excluded,
    parse_exclude_chat_names,
)
from feishu_message_archive.normalize import NormalizedMessage


def test_parse_exclude_chat_names_multiline_and_commas() -> None:
    raw = "群A\n群B，群C、群A"
    got = parse_exclude_chat_names(raw)
    assert got == ["群A", "群B", "群C"]


def test_is_chat_excluded_substring() -> None:
    assert is_chat_excluded("产品讨论群-日常", ["讨论"], match="substring")
    assert not is_chat_excluded("产品讨论群-日常", ["闲聊"], match="substring")


def test_is_chat_excluded_exact() -> None:
    assert is_chat_excluded("  全员群  ", ["全员群"], match="exact")
    assert not is_chat_excluded("全员群备份", ["全员群"], match="exact")


def test_is_chat_excluded_empty_name() -> None:
    assert not is_chat_excluded(None, ["x"], match="substring")


def test_filter_messages_by_chat_name() -> None:
    m1 = NormalizedMessage(
        message_id="1",
        create_time="1",
        chat_id="c1",
        chat_name="项目Alpha",
        chat_type="group",
        msg_type="text",
        sender_id="ou_1",
        sender_name="u",
        content="hi",
        deleted=False,
        updated=False,
        thread_id=None,
    )
    m2 = NormalizedMessage(
        message_id="2",
        create_time="2",
        chat_id="c2",
        chat_name="闲聊灌水",
        chat_type="group",
        msg_type="text",
        sender_id="ou_2",
        sender_name="v",
        content="yo",
        deleted=False,
        updated=False,
        thread_id=None,
    )
    kept, n_ex = filter_messages_by_chat_name([m1, m2], ["闲聊"], match="substring")
    assert n_ex == 1
    assert len(kept) == 1
    assert kept[0].message_id == "1"
