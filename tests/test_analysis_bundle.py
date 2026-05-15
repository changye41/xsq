"""Tests for archive bundle loading."""

from pathlib import Path

import pytest

from feishu_message_archive.analysis_run import load_archive_bundle


def test_load_bundle_combined(tmp_path: Path) -> None:
    d = tmp_path / "out"
    d.mkdir()
    (d / "digest.md").write_text("# hi\n", encoding="utf-8")
    (d / "messages.jsonl").write_text('{"x":1}\n', encoding="utf-8")
    n, text = load_archive_bundle(d, max_chars=10_000)
    assert n > 0
    assert "digest" in text and "messages.jsonl" in text


def test_load_bundle_missing_raises(tmp_path: Path) -> None:
    d = tmp_path / "empty"
    d.mkdir()
    with pytest.raises(FileNotFoundError):
        load_archive_bundle(d, max_chars=1000)


def test_load_bundle_truncates(tmp_path: Path) -> None:
    d = tmp_path / "out"
    d.mkdir()
    (d / "digest.md").write_text("a" * 5000, encoding="utf-8")
    (d / "messages.jsonl").write_text("b" * 100_000, encoding="utf-8")
    _n, text = load_archive_bundle(d, max_chars=8000)
    assert "截断" in text or len(text) <= 8500
