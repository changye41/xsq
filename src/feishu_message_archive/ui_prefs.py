"""Persist Streamlit UI preferences (e.g. excluded chat names) across sessions."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

_PREFS_VERSION = 1


def prefs_dir() -> Path:
    """Directory for JSON prefs; override with FEISHU_ARCHIVE_PREFS_DIR for tests."""
    override = os.environ.get("FEISHU_ARCHIVE_PREFS_DIR", "").strip()
    if override:
        return Path(override).expanduser()
    return Path.home() / ".feishu-message-archive"


def exclude_ui_prefs_path() -> Path:
    return prefs_dir() / "exclude_ui_prefs.json"


def load_exclude_ui_prefs() -> dict[str, Any]:
    """Return saved exclude-chat UI fields; missing file -> empty defaults."""
    path = exclude_ui_prefs_path()
    if not path.is_file():
        return {
            "version": _PREFS_VERSION,
            "exclude_chat_raw": "",
            "exclude_chat_match": "substring",
        }
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {
            "version": _PREFS_VERSION,
            "exclude_chat_raw": "",
            "exclude_chat_match": "substring",
        }
    if not isinstance(data, dict):
        return {
            "version": _PREFS_VERSION,
            "exclude_chat_raw": "",
            "exclude_chat_match": "substring",
        }
    raw = data.get("exclude_chat_raw")
    match = data.get("exclude_chat_match", "substring")
    if match not in ("substring", "exact"):
        match = "substring"
    return {
        "version": _PREFS_VERSION,
        "exclude_chat_raw": raw if isinstance(raw, str) else "",
        "exclude_chat_match": match,
    }


def save_exclude_ui_prefs(*, exclude_chat_raw: str, exclude_chat_match: str) -> None:
    """Write prefs to disk; failures are logged but not raised (UI should stay usable)."""
    if exclude_chat_match not in ("substring", "exact"):
        exclude_chat_match = "substring"
    payload = {
        "version": _PREFS_VERSION,
        "exclude_chat_raw": exclude_chat_raw,
        "exclude_chat_match": exclude_chat_match,
    }
    path = exclude_ui_prefs_path()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        import logging

        logging.getLogger(__name__).warning("could not write UI prefs to %s", path, exc_info=True)


def prompt_ui_prefs_path() -> Path:
    return prefs_dir() / "prompt_ui_prefs.json"


def load_prompt_ui_prefs() -> dict[str, Any]:
    """Return saved prompt editor fields; missing/invalid file -> safe defaults."""
    path = prompt_ui_prefs_path()
    defaults = {
        "version": _PREFS_VERSION,
        "system_prompt": "",
        "user_prompt_template": "",
    }
    if not path.is_file():
        return defaults
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return defaults
    if not isinstance(data, dict):
        return defaults
    sp = data.get("system_prompt")
    up = data.get("user_prompt_template")
    return {
        "version": _PREFS_VERSION,
        "system_prompt": sp if isinstance(sp, str) else "",
        "user_prompt_template": up if isinstance(up, str) else "",
    }


def save_prompt_ui_prefs(*, system_prompt: str, user_prompt_template: str) -> None:
    """Persist prompt editor fields locally; fail-open for UI usage."""
    payload = {
        "version": _PREFS_VERSION,
        "system_prompt": system_prompt,
        "user_prompt_template": user_prompt_template,
    }
    path = prompt_ui_prefs_path()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        import logging

        logging.getLogger(__name__).warning("could not write prompt prefs to %s", path, exc_info=True)


def ai_model_ui_prefs_path() -> Path:
    return prefs_dir() / "ai_model_ui_prefs.json"


def load_ai_model_ui_prefs() -> dict[str, Any]:
    """Return saved AI model fields (api_key/base_url/model)."""
    path = ai_model_ui_prefs_path()
    defaults = {
        "version": _PREFS_VERSION,
        "api_key": "",
        "base_url": "",
        "model": "",
        "auto_analyze_after_export": True,
    }
    if not path.is_file():
        return defaults
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return defaults
    if not isinstance(data, dict):
        return defaults
    return {
        "version": _PREFS_VERSION,
        "api_key": data.get("api_key") if isinstance(data.get("api_key"), str) else "",
        "base_url": data.get("base_url") if isinstance(data.get("base_url"), str) else "",
        "model": data.get("model") if isinstance(data.get("model"), str) else "",
        "auto_analyze_after_export": (
            data.get("auto_analyze_after_export")
            if isinstance(data.get("auto_analyze_after_export"), bool)
            else True
        ),
    }


def save_ai_model_ui_prefs(
    *,
    api_key: str,
    base_url: str,
    model: str,
    auto_analyze_after_export: bool,
) -> None:
    """Persist AI model fields locally; fail-open for UI usage."""
    payload = {
        "version": _PREFS_VERSION,
        "api_key": api_key,
        "base_url": base_url,
        "model": model,
        "auto_analyze_after_export": auto_analyze_after_export,
    }
    path = ai_model_ui_prefs_path()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        import logging

        logging.getLogger(__name__).warning("could not write AI model prefs to %s", path, exc_info=True)


def export_window_ui_prefs_path() -> Path:
    return prefs_dir() / "export_window_ui_prefs.json"


def load_export_window_ui_prefs() -> dict[str, Any]:
    """Return saved export time-window fields."""
    path = export_window_ui_prefs_path()
    defaults = {
        "version": _PREFS_VERSION,
        "timezone": "Asia/Shanghai",
        "cal_day": "",
        "rng_sd": "",
        "rng_st": "",
        "rng_ed": "",
        "rng_et": "",
    }
    if not path.is_file():
        return defaults
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return defaults
    if not isinstance(data, dict):
        return defaults
    out = dict(defaults)
    for k in ("timezone", "cal_day", "rng_sd", "rng_st", "rng_ed", "rng_et"):
        v = data.get(k)
        if isinstance(v, str):
            out[k] = v
    return out


def save_export_window_ui_prefs(
    *,
    timezone: str,
    cal_day: str,
    rng_sd: str,
    rng_st: str,
    rng_ed: str,
    rng_et: str,
) -> None:
    """Persist export time-window fields locally; fail-open for UI usage."""
    payload = {
        "version": _PREFS_VERSION,
        "timezone": timezone,
        "cal_day": cal_day,
        "rng_sd": rng_sd,
        "rng_st": rng_st,
        "rng_ed": rng_ed,
        "rng_et": rng_et,
    }
    path = export_window_ui_prefs_path()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        import logging

        logging.getLogger(__name__).warning("could not write export window prefs to %s", path, exc_info=True)
