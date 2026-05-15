@echo off
REM One-click launcher for the Streamlit UI (Feishu message archive).
REM Prefer project venv, then python on PATH, then Windows py launcher.

chcp 65001 >nul
setlocal
cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" -m feishu_message_archive.ui_run %*
  goto :done
)

where python >nul 2>&1
if %errorlevel%==0 (
  python -m feishu_message_archive.ui_run %*
  goto :done
)

where py >nul 2>&1
if %errorlevel%==0 (
  py -3 -m feishu_message_archive.ui_run %*
  goto :done
)

echo.
echo [错误] 未找到 Python。请安装 Python 3 并勾选「Add python.exe to PATH」，
echo 或在项目目录创建虚拟环境: python -m venv .venv
echo.
pause
exit /b 1

:done
if errorlevel 1 (
  echo.
  echo 若提示缺少 streamlit 等模块，请在项目根目录执行:
  echo   pip install -e ".[ui]"
  echo.
  pause
)
exit /b %errorlevel%
