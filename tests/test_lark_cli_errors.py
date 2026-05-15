"""Tests for lark-cli failure message enrichment."""

from feishu_message_archive.lark_cli import _format_cli_failure


def test_format_cli_failure_adds_search_message_hint() -> None:
    stderr = """{ "ok": false, "identity": "user", "error": { "type": "missing_scope", "message": "missing required scope(s): search:message" } }"""
    msg = _format_cli_failure("lark-cli", 3, stderr, "")
    assert "search:message" in msg
    assert "处理方式" in msg
    assert "auth login" in msg
