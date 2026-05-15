#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
DIST_DIR="$ROOT_DIR/dist"
BUILD_DIR="$ROOT_DIR/build"
SPEC_PATH="$ROOT_DIR/scripts/macos/feishu_archive.spec"
DMG_SETTINGS="$ROOT_DIR/scripts/macos/dmg_settings.py"
export FEISHU_ARCHIVE_ROOT="$ROOT_DIR"

cd "$ROOT_DIR"

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "This script must run on macOS (Darwin)." >&2
  exit 1
fi

if ! command -v lark-cli >/dev/null 2>&1; then
  echo "lark-cli is required on target machines. Install and login first." >&2
  echo "Install: npm i -g @larksuiteoapi/lark-cli" >&2
fi

python3 -m pip install --upgrade pip
python3 -m pip install -e ".[ui,analyze]"
python3 -m pip install pyinstaller dmgbuild

rm -rf "$DIST_DIR" "$BUILD_DIR"

pyinstaller --noconfirm "$SPEC_PATH"

if [[ ! -d "$DIST_DIR/Feishu Message Archive.app" ]]; then
  echo "App bundle not found after PyInstaller build." >&2
  exit 1
fi

dmgbuild -s "$DMG_SETTINGS" "Feishu Message Archive" "$DIST_DIR/Feishu-Message-Archive.dmg"

echo "Build complete:"
echo "  APP: $DIST_DIR/Feishu Message Archive.app"
echo "  DMG: $DIST_DIR/Feishu-Message-Archive.dmg"
