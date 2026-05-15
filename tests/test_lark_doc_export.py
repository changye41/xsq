"""Tests for Feishu doc title numbering logic."""

from pathlib import Path

from feishu_message_archive.lark_doc_export import (
    _MAX_SEARCH_QUERY_LEN,
    _build_doc_markdown,
    archive_label_from_dir,
    format_archive_title_label,
    normalize_analysis_markdown,
    pick_next_title,
)


def test_pick_next_title_no_collision() -> None:
    assert pick_next_title([], "2026-05-12飞书信息归档") == "2026-05-12飞书信息归档"


def test_pick_next_title_with_collisions() -> None:
    existing = [
        "2026-05-12飞书信息归档",
        "2026-05-12飞书信息归档（2）",
        "2026-05-12飞书信息归档（3）",
    ]
    assert pick_next_title(existing, "2026-05-12飞书信息归档") == "2026-05-12飞书信息归档（4）"


def test_archive_label_from_dir_fallback(tmp_path: Path) -> None:
    d = tmp_path / "2026-05-12__export_20260512-120000"
    d.mkdir()
    assert "2026-05-12" in archive_label_from_dir(d)


def test_build_doc_markdown_has_source_annotation() -> None:
    md = _build_doc_markdown("T", "analysis body")
    assert "analysis body" in md
    assert "本[文档]由飞书工具 Lark-Cli 创建" in md


def test_search_query_max_len_constant() -> None:
    assert _MAX_SEARCH_QUERY_LEN == 30


def test_format_archive_title_label_iso_range() -> None:
    raw = "2026-05-12T08:00:00+08:00 — 2026-05-12T22:00:00+08:00"
    assert format_archive_title_label(raw) == "5.12 8-22"


def test_normalize_analysis_markdown_unwraps_outer_fence() -> None:
    raw = "```markdown\n## A\n- item\n```"
    out = normalize_analysis_markdown(raw)
    assert out.startswith("## A")
    assert "```" not in out


def test_build_doc_markdown_uses_normalized_body() -> None:
    md = _build_doc_markdown("T", "```md\n## X\n正文\n```")
    assert "## X" in md
    assert "```md" not in md
