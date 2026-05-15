"""run_analysis error paths without calling LLM."""

from pathlib import Path

import pytest

from feishu_message_archive.analysis_run import AnalyzeParams, run_analysis


def test_run_analysis_missing_api_key(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    (tmp_path / "digest.md").write_text("# x", encoding="utf-8")
    r = run_analysis(AnalyzeParams(input_dir=tmp_path))
    assert r.outcome == "error"
    assert r.error_message and "API Key" in r.error_message


def test_run_analysis_missing_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-fake-not-used")
    r = run_analysis(AnalyzeParams(input_dir=tmp_path))
    assert r.outcome == "error"
    assert "未找到" in (r.error_message or "")
