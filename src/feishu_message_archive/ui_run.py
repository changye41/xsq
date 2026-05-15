"""Launch Streamlit UI without relying on PATH wrapper scripts.

Preferred on Windows when `feishu-archive-ui` is not on PATH::

    pip install -e ".[ui]"
    python -m feishu_message_archive.ui_run

Or from repository root run ``run-ui.ps1`` / ``run-ui.bat``.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    app = Path(__file__).resolve().parent / "streamlit_app.py"
    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(app),
        "--browser.gatherUsageStats",
        "false",
    ]
    # Allow passing extra streamlit flags, e.g. --server.port 8502
    cmd.extend(sys.argv[1:])
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
