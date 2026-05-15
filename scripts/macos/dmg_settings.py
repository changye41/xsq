import os
from pathlib import Path


ROOT = Path(os.environ.get("FEISHU_ARCHIVE_ROOT", os.getcwd())).resolve()
DIST = ROOT / "dist"
APP_NAME = "Feishu Message Archive.app"
VOLUME_NAME = "Feishu Message Archive Installer"

application = DIST / APP_NAME

filename = str(DIST / "Feishu-Message-Archive.dmg")
volume_name = VOLUME_NAME
format = "UDZO"
size = "500M"
files = [str(application)]
symlinks = {"Applications": "/Applications"}
badge_icon = None
icon_locations = {
    APP_NAME: (150, 160),
    "Applications": (420, 160),
}
window_rect = ((100, 100), (600, 360))
text_size = 12
show_status_bar = False
show_toolbar = False
show_pathbar = False
show_sidebar = False
