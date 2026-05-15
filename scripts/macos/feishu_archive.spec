from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"

datas = collect_data_files("feishu_message_archive", include_py_files=False)

a = Analysis(
    [str(SRC / "feishu_message_archive" / "ui_run.py")],
    pathex=[str(ROOT), str(SRC)],
    binaries=[],
    datas=datas,
    hiddenimports=[
        "streamlit.web.bootstrap",
        "streamlit.runtime.scriptrunner",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="feishu-message-archive-ui",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(
    exe,
    name="Feishu Message Archive.app",
    icon=None,
    bundle_identifier="ai.neolix.feishu-message-archive",
    info_plist={
        "CFBundleDisplayName": "Feishu Message Archive",
        "CFBundleShortVersionString": "0.1.0",
        "CFBundleVersion": "0.1.0",
        "NSHighResolutionCapable": True,
    },
)
