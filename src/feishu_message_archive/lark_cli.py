"""Subprocess helpers for lark-cli (user identity)."""

from __future__ import annotations

import json
import logging
import shutil
import subprocess
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class LarkCliError(RuntimeError):
    """lark-cli exited with failure or returned invalid JSON."""


_SCOPE_SEARCH_MESSAGE_HINT = (
    "【处理方式】当前操作需要「搜索消息」权限（search:message）。请在终端执行以下命令，"
    "按提示在浏览器中完成授权（命令会阻塞直至完成）：\n"
    '  lark-cli auth login --scope "search:message"\n'
    "完成后重新运行归档或刷新可视化界面。"
)


def _scope_hint_from_stderr(stderr: str) -> str:
    """If stderr looks like lark-cli JSON missing_scope, return a short Chinese hint."""
    text = (stderr or "").strip()
    if not text:
        return ""
    if "missing_scope" not in text and "search:message" not in text:
        return ""
    obj: Any = None
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        if "search:message" in text:
            return _SCOPE_SEARCH_MESSAGE_HINT
        return ""

    if isinstance(obj, dict) and obj.get("ok") is False:
        err = obj.get("error")
        if isinstance(err, dict) and err.get("type") == "missing_scope":
            msg = str(err.get("message") or "")
            if "search:message" in msg:
                return _SCOPE_SEARCH_MESSAGE_HINT
            return (
                "【处理方式】缺少 OAuth 权限。请按终端中的 hint 使用 "
                '`lark-cli auth login --scope "..."` 重新登录并勾选所需 scope。'
            )
    return ""


def _format_cli_failure(
    exe: str,
    exit_code: int,
    stderr: str,
    stdout: str,
) -> str:
    err = (stderr or "").strip() or "(no stderr)"
    out = (stdout or "").strip()
    base = f"lark-cli failed (exit {exit_code}): {exe}\nstderr:\n{err}\nstdout:\n{out}"
    hint = _scope_hint_from_stderr(stderr)
    if hint:
        base = base + "\n\n" + hint
    return base


def resolve_lark_cli(override: str | None) -> str:
    """Return executable name or path for lark-cli."""
    if override:
        return override
    found = shutil.which("lark-cli")
    if not found:
        raise LarkCliError(
            "lark-cli not found in PATH. Install Lark CLI and ensure it is on PATH, "
            "or pass --lark-cli."
        )
    return found


def run_lark_json(
    argv: list[str],
    *,
    cwd: Path | None = None,
    timeout_s: float | None = 600.0,
) -> Any:
    """Run lark-cli, parse stdout as JSON, raise on failure with stderr context."""
    exe = argv[0]
    logger.debug("running: %s", " ".join(argv))
    try:
        proc = subprocess.run(
            argv,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout_s,
            check=False,
        )
    except subprocess.TimeoutExpired as e:
        raise LarkCliError(f"lark-cli timed out after {timeout_s}s: {exe}") from e
    if proc.returncode != 0:
        raise LarkCliError(
            _format_cli_failure(exe, proc.returncode, proc.stderr or "", proc.stdout or "")
        )
    raw = proc.stdout.strip()
    if not raw:
        raise LarkCliError(f"lark-cli returned empty stdout: {exe}")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        snippet = raw[:500]
        raise LarkCliError(f"lark-cli stdout is not JSON: {exe}\n{snippet}") from e


def get_self_open_id(lark_cli: str, cwd: Path | None = None) -> str:
    """Return current user's open_id via `contact +get-user`."""
    data = run_lark_json(
        [
            lark_cli,
            "contact",
            "+get-user",
            "--as",
            "user",
            "--format",
            "json",
        ],
        cwd=cwd,
        timeout_s=60.0,
    )
    oid = _extract_open_id(data)
    if not oid:
        raise LarkCliError(
            "could not parse open_id from contact +get-user output; keys at root may differ."
        )
    return oid


def _extract_open_id(data: Any) -> str | None:
    if isinstance(data, dict):
        for key in ("open_id", "openId"):
            v = data.get(key)
            if isinstance(v, str) and v.startswith("ou_"):
                return v
        user = data.get("user")
        if isinstance(user, dict):
            for key in ("open_id", "openId"):
                v = user.get(key)
                if isinstance(v, str) and v.startswith("ou_"):
                    return v
        data_obj = data.get("data")
        if isinstance(data_obj, dict):
            return _extract_open_id(data_obj)
    return None


def messages_search(
    lark_cli: str,
    *,
    query: str,
    start: str,
    end: str,
    page_all: bool = True,
    page_limit: int | None = None,
    is_at_me: bool = False,
    chat_id: str | None = None,
    cwd: Path | None = None,
) -> Any:
    """Call `im +messages-search` and return parsed JSON."""
    cmd: list[str] = [
        lark_cli,
        "im",
        "+messages-search",
        "--query",
        query,
        "--start",
        start,
        "--end",
        end,
        "--as",
        "user",
        "--format",
        "json",
    ]
    if page_all:
        cmd.append("--page-all")
    if page_limit is not None:
        cmd.extend(["--page-limit", str(page_limit)])
    if is_at_me:
        cmd.append("--is-at-me")
    if chat_id:
        cmd.extend(["--chat-id", chat_id])
    return run_lark_json(cmd, cwd=cwd)
