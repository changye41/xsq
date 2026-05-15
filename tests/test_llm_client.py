"""Tests for LLM client with mocked HTTP."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from feishu_message_archive.llm_client import LLMClientError, chat_completion


def test_chat_completion_success() -> None:
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "choices": [{"message": {"content": "# Hello\nanalysis"}}],
    }
    mock_client = MagicMock()
    mock_client.__enter__.return_value.post.return_value = mock_resp

    with patch("feishu_message_archive.llm_client._require_httpx") as rq:
        httpx_mod = MagicMock()
        httpx_mod.Client.return_value = mock_client
        rq.return_value = httpx_mod

        out = chat_completion(
            messages=[{"role": "user", "content": "x"}],
            model="gpt-4o-mini",
            api_key="sk-test",
            base_url="https://api.openai.com/v1",
        )
    assert "Hello" in out


def test_chat_completion_http_error() -> None:
    mock_resp = MagicMock()
    mock_resp.status_code = 401
    mock_resp.text = "unauthorized"
    mock_client = MagicMock()
    mock_client.__enter__.return_value.post.return_value = mock_resp

    with patch("feishu_message_archive.llm_client._require_httpx") as rq:
        httpx_mod = MagicMock()
        httpx_mod.Client.return_value = mock_client
        rq.return_value = httpx_mod

        with pytest.raises(LLMClientError):
            chat_completion(
                messages=[{"role": "user", "content": "x"}],
                model="m",
                api_key="k",
                base_url="https://api.openai.com/v1",
            )


def test_429_insufficient_balance_shows_hint() -> None:
    mock_resp = MagicMock()
    mock_resp.status_code = 429
    mock_resp.text = (
        '{"error":{"message":"exceeded_current_quota insufficient balance recharge"}}'
    )
    mock_client = MagicMock()
    mock_client.__enter__.return_value.post.return_value = mock_resp

    with patch("feishu_message_archive.llm_client._require_httpx") as rq:
        httpx_mod = MagicMock()
        httpx_mod.Client.return_value = mock_client
        rq.return_value = httpx_mod

        with pytest.raises(LLMClientError) as exc_info:
            chat_completion(
                messages=[{"role": "user", "content": "x"}],
                model="m",
                api_key="k",
                base_url="https://api.example.com/v1",
            )
    assert "处理方式" in str(exc_info.value)
