"""Prompt helper smoke test."""

from feishu_message_archive.analysis_prompt import render_user_prompt, user_message_body


def test_user_message_body_with_context() -> None:
    body = user_message_body("archive text", "focus on deadlines")
    assert "archive text" in body
    assert "deadlines" in body


def test_user_message_body_no_context() -> None:
    body = user_message_body("only archive", None)
    assert "only archive" in body
    assert "用户补充" not in body


def test_render_user_prompt_template() -> None:
    body = render_user_prompt(
        archive_bundle="BUNDLE",
        extra_context="CTX",
        template="A:{archive_bundle}\nE:{extra_context_block}\n",
    )
    assert "A:BUNDLE" in body
    assert "CTX" in body


def test_render_user_prompt_bad_template_fallback() -> None:
    body = render_user_prompt(
        archive_bundle="BUNDLE",
        extra_context=None,
        template="A:{unknown_key}",
    )
    assert "BUNDLE" in body
