"""Prompt override behavior in run_analysis."""

from pathlib import Path

from feishu_message_archive.analysis_run import AnalyzeParams, run_analysis


def test_run_analysis_uses_prompt_overrides(
    tmp_path: Path,
    monkeypatch,
) -> None:
    (tmp_path / "digest.md").write_text("# d", encoding="utf-8")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-fake")

    captured: dict[str, object] = {}

    def fake_chat_completion(*, messages, model, api_key, base_url, timeout_s=180.0):
        captured["messages"] = messages
        return "ok"

    monkeypatch.setattr(
        "feishu_message_archive.analysis_run.chat_completion",
        fake_chat_completion,
    )

    out = tmp_path / "analysis.md"
    r = run_analysis(
        AnalyzeParams(
            input_dir=tmp_path,
            output_path=out,
            system_prompt="SYSX",
            user_prompt_template="B:{archive_bundle}\nE:{extra_context_block}",
            extra_context="CTX",
        )
    )
    assert r.outcome == "ok"
    msgs = captured["messages"]
    assert isinstance(msgs, list)
    assert msgs[0]["content"] == "SYSX"
    assert "B:" in msgs[1]["content"]
    assert "CTX" in msgs[1]["content"]
