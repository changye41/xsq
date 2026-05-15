"""CLI: LLM analysis over feishu-archive output folder."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from feishu_message_archive import __version__
from feishu_message_archive.analysis_run import AnalyzeParams, run_analysis


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="feishu-archive-analyze",
        description=(
            "Analyze feishu-archive output (digest.md + messages.jsonl) with an "
            "OpenAI-compatible Chat Completions API."
        ),
    )
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    p.add_argument(
        "--input-dir",
        type=Path,
        required=True,
        help="Directory containing digest.md and/or messages.jsonl",
    )
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Write analysis markdown here (default: <input-dir>/analysis.md)",
    )
    p.add_argument(
        "--max-chars",
        type=int,
        default=120_000,
        metavar="N",
        help="Max characters sent to the model (default 120000)",
    )
    p.add_argument(
        "--context",
        default=None,
        help="Extra user context appended to the prompt",
    )
    p.add_argument("-v", "--verbose", action="store_true")
    ns = p.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if ns.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )

    params = AnalyzeParams(
        input_dir=ns.input_dir,
        output_path=ns.output,
        extra_context=ns.context,
        max_bundle_chars=ns.max_chars,
    )
    result = run_analysis(params)
    if result.outcome != "ok":
        logging.error("%s", result.error_message)
        return 1
    logging.info(
        "analysis ok (%s chars bundle) -> %s",
        result.bundle_chars,
        result.output_path,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
