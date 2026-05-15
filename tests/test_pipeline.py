"""Tests for archive pipeline time windows."""

from __future__ import annotations

from datetime import date, time

import pytest

from feishu_message_archive.pipeline import (
    ArchiveParams,
    build_export_dir,
    combine_date_time_to_iso,
    day_bounds_iso,
    resolve_time_window,
)


def test_day_bounds_iso() -> None:
    start, end = day_bounds_iso("2026-05-11", "Asia/Shanghai")
    assert "+08:00" in start and "+08:00" in end
    assert start < end


def test_resolve_time_window_date() -> None:
    p = ArchiveParams(
        mode="date",
        timezone="Asia/Shanghai",
        calendar_date="2026-05-11",
        output_dir=__import__("pathlib").Path("."),
    )
    s, e, title = resolve_time_window(p)
    assert title == "2026-05-11"
    assert s < e


def test_resolve_time_window_range() -> None:
    p = ArchiveParams(
        mode="range",
        timezone="UTC",
        start_iso="2026-05-11T00:00:00+00:00",
        end_iso="2026-05-11T23:59:59+00:00",
        output_dir=__import__("pathlib").Path("."),
    )
    s, e, title = resolve_time_window(p)
    assert "—" in title
    assert s == p.start_iso


def test_combine_date_time_to_iso() -> None:
    iso = combine_date_time_to_iso(date(2026, 5, 11), time(14, 30, 0), "Asia/Shanghai")
    assert "2026-05-11" in iso
    assert "+08:00" in iso


def test_resolve_invalid() -> None:
    p = ArchiveParams(mode="date", timezone="Asia/Shanghai", calendar_date=None, output_dir=__import__("pathlib").Path("."))
    with pytest.raises(ValueError):
        resolve_time_window(p)


def test_build_export_dir_contains_window_and_export_time() -> None:
    out = build_export_dir(__import__("pathlib").Path("base"), "2026-05-11 — 2026-05-12")
    s = str(out)
    assert "base" in s
    assert "__export_" in s
