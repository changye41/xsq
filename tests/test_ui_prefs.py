"""Tests for UI prefs persistence."""

import json
import os
from pathlib import Path

import pytest

from feishu_message_archive.ui_prefs import (
    ai_model_ui_prefs_path,
    exclude_ui_prefs_path,
    export_window_ui_prefs_path,
    load_ai_model_ui_prefs,
    load_exclude_ui_prefs,
    load_export_window_ui_prefs,
    load_prompt_ui_prefs,
    prompt_ui_prefs_path,
    save_ai_model_ui_prefs,
    save_exclude_ui_prefs,
    save_export_window_ui_prefs,
    save_prompt_ui_prefs,
)


def test_load_save_roundtrip(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FEISHU_ARCHIVE_PREFS_DIR", str(tmp_path))
    assert load_exclude_ui_prefs()["exclude_chat_raw"] == ""

    save_exclude_ui_prefs(exclude_chat_raw="群A\n群B", exclude_chat_match="exact")
    path = exclude_ui_prefs_path()
    assert path.is_file()
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["exclude_chat_raw"] == "群A\n群B"
    assert data["exclude_chat_match"] == "exact"

    loaded = load_exclude_ui_prefs()
    assert loaded["exclude_chat_raw"] == "群A\n群B"
    assert loaded["exclude_chat_match"] == "exact"


def test_invalid_match_in_file_defaults(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FEISHU_ARCHIVE_PREFS_DIR", str(tmp_path))
    p = tmp_path / "exclude_ui_prefs.json"
    p.write_text(
        json.dumps({"exclude_chat_raw": "x", "exclude_chat_match": "bogus"}),
        encoding="utf-8",
    )
    loaded = load_exclude_ui_prefs()
    assert loaded["exclude_chat_match"] == "substring"


def test_prompt_prefs_roundtrip(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FEISHU_ARCHIVE_PREFS_DIR", str(tmp_path))
    assert load_prompt_ui_prefs()["system_prompt"] == ""
    save_prompt_ui_prefs(
        system_prompt="sys",
        user_prompt_template="bundle={archive_bundle}",
    )
    p = prompt_ui_prefs_path()
    assert p.is_file()
    loaded = load_prompt_ui_prefs()
    assert loaded["system_prompt"] == "sys"
    assert loaded["user_prompt_template"] == "bundle={archive_bundle}"


def test_ai_model_prefs_roundtrip(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FEISHU_ARCHIVE_PREFS_DIR", str(tmp_path))
    assert load_ai_model_ui_prefs()["base_url"] == ""
    assert load_ai_model_ui_prefs()["auto_analyze_after_export"] is True
    save_ai_model_ui_prefs(
        api_key="k1",
        base_url="https://api.example.com/v1",
        model="x-model",
        auto_analyze_after_export=False,
    )
    p = ai_model_ui_prefs_path()
    assert p.is_file()
    loaded = load_ai_model_ui_prefs()
    assert loaded["api_key"] == "k1"
    assert loaded["base_url"] == "https://api.example.com/v1"
    assert loaded["model"] == "x-model"
    assert loaded["auto_analyze_after_export"] is False


def test_export_window_prefs_roundtrip(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FEISHU_ARCHIVE_PREFS_DIR", str(tmp_path))
    assert load_export_window_ui_prefs()["timezone"] == "Asia/Shanghai"
    save_export_window_ui_prefs(
        timezone="UTC",
        cal_day="2026-05-12",
        rng_sd="2026-05-11",
        rng_st="09:30:00",
        rng_ed="2026-05-12",
        rng_et="18:15:00",
    )
    p = export_window_ui_prefs_path()
    assert p.is_file()
    loaded = load_export_window_ui_prefs()
    assert loaded["timezone"] == "UTC"
    assert loaded["cal_day"] == "2026-05-12"
    assert loaded["rng_st"] == "09:30:00"
