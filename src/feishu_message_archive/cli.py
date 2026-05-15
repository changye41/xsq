"""CLI entry: pull Feishu messages and write JSONL + Markdown."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from feishu_message_archive import __version__
from feishu_message_archive.filter_chats import parse_exclude_chat_names
from feishu_message_archive.pipeline import ArchiveParams, day_bounds_iso, run_archive


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="feishu-archive",
        description=(
            "Export Feishu IM messages (via lark-cli, user identity) to JSONL and Markdown."
        ),
    )
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    win = p.add_mutually_exclusive_group(required=True)
    win.add_argument(
        "--date",
        metavar="YYYY-MM-DD",
        help="Calendar day in --timezone (start 00:00:00 through end of day).",
    )
    win.add_argument(
        "--start",
        metavar="ISO8601",
        help="Range start (must include timezone offset), e.g. 2026-05-11T00:00:00+08:00",
    )
    p.add_argument(
        "--end",
        metavar="ISO8601",
        help="Range end (required with --start). Example: 2026-05-11T23:59:59+08:00",
    )
    p.add_argument(
        "--timezone",
        default="Asia/Shanghai",
        help="IANA timezone for --date expansion (default: Asia/Shanghai).",
    )
    p.add_argument(
        "--output-dir",
        type=Path,
        default=Path("feishu_archive_out"),
        help="Output directory for messages.jsonl and digest.md (default: ./feishu_archive_out).",
    )
    p.add_argument(
        "--lark-cli",
        default=None,
        help="Path to lark-cli executable if not on PATH.",
    )
    p.add_argument(
        "--page-limit",
        type=int,
        default=None,
        metavar="N",
        help="Forward to lark-cli --page-limit (caps auto-pagination pages).",
    )
    p.add_argument(
        "--chat-id",
        default=None,
        help="Optional oc_ chat id to restrict search scope.",
    )
    p.add_argument(
        "--skip-at-me-pass",
        action="store_true",
        help="Do not run a second search with --is-at-me (single broad pass only).",
    )
    p.add_argument(
        "--exclude-chat-name",
        action="append",
        default=None,
        metavar="PATTERN",
        help=(
            "Exclude messages from chats whose display name matches this pattern. "
            "Repeatable; each value may contain commas. Matching is controlled by "
            "--exclude-chat-match (default: substring, case-insensitive)."
        ),
    )
    p.add_argument(
        "--exclude-chat-match",
        choices=("substring", "exact"),
        default="substring",
        help="How --exclude-chat-name is compared to the chat display name (default: substring).",
    )
    p.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging.")
    return p.parse_args(argv)


def _exclude_patterns_from_ns(ns: argparse.Namespace) -> tuple[str, ...]:
    chunks = ns.exclude_chat_name or []
    if not chunks:
        return ()
    return tuple(parse_exclude_chat_names("\n".join(chunks)))


def _validate_range_args(ns: argparse.Namespace) -> ArchiveParams:
    if ns.date:
        if ns.start or ns.end:
            raise SystemExit("error: do not combine --date with --start/--end")
        try:
            day_bounds_iso(ns.date, ns.timezone)
        except ValueError as e:
            raise SystemExit(f"error: invalid --date or --timezone: {e}") from e
        return ArchiveParams(
            mode="date",
            timezone=ns.timezone,
            calendar_date=ns.date,
            output_dir=ns.output_dir,
            lark_cli=ns.lark_cli,
            page_limit=ns.page_limit,
            chat_id=ns.chat_id,
            skip_at_me_pass=ns.skip_at_me_pass,
            exclude_chat_names=_exclude_patterns_from_ns(ns),
            exclude_chat_match=ns.exclude_chat_match,
        )
    if ns.start:
        if not ns.end:
            raise SystemExit("error: --end is required when using --start")
        return ArchiveParams(
            mode="range",
            timezone=ns.timezone,
            start_iso=ns.start,
            end_iso=ns.end,
            output_dir=ns.output_dir,
            lark_cli=ns.lark_cli,
            page_limit=ns.page_limit,
            chat_id=ns.chat_id,
            skip_at_me_pass=ns.skip_at_me_pass,
            exclude_chat_names=_exclude_patterns_from_ns(ns),
            exclude_chat_match=ns.exclude_chat_match,
        )
    raise SystemExit("error: specify either --date or both --start and --end")


def main(argv: list[str] | None = None) -> int:
    ns = _parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if ns.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )
    log = logging.getLogger(__name__)
    params = _validate_range_args(ns)

    result = run_archive(params, logger=log)
    if result.outcome == "error":
        logging.error("%s", result.error_message)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
