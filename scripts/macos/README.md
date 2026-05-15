# macOS Packaging Guide

This directory contains packaging assets for a distributable macOS GUI build:

- `build_macos.sh`: one-shot build script for `.app` and `.dmg`
- `feishu_archive.spec`: PyInstaller config for Streamlit launcher
- `dmg_settings.py`: dmgbuild layout config

## Build prerequisites (on macOS)

- Python 3.10+
- Xcode Command Line Tools (`xcode-select --install`)
- `lark-cli` available in `PATH`

## Build command

```bash
chmod +x scripts/macos/build_macos.sh
./scripts/macos/build_macos.sh
```

Artifacts:

- `dist/Feishu Message Archive.app`
- `dist/Feishu-Message-Archive.dmg`

## End-user requirements

The packaged app bundles Python runtime and project dependencies.
The only external dependency still required on target machines is `lark-cli` (and user login/authorization).
