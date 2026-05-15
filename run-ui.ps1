# Feishu archive Streamlit UI — same logic as start_visual_ui.bat
$ErrorActionPreference = "Stop"
$Root = $PSScriptRoot
if (-not $Root) {
  $Root = Split-Path -Parent $MyInvocation.MyCommand.Path
}
Set-Location $Root

$venvPy = Join-Path $Root ".venv\Scripts\python.exe"
try {
  if (Test-Path -LiteralPath $venvPy) {
    & $venvPy -m feishu_message_archive.ui_run @args
  }
  elseif (Get-Command python -ErrorAction SilentlyContinue) {
    python -m feishu_message_archive.ui_run @args
  }
  elseif (Get-Command py -ErrorAction SilentlyContinue) {
    py -3 -m feishu_message_archive.ui_run @args
  }
  else {
    Write-Host "[错误] 未找到 Python。请安装 Python 3 或将 python 加入 PATH，或创建 .venv。" -ForegroundColor Red
    exit 1
  }
}
catch {
  Write-Host $_ -ForegroundColor Red
  exit 1
}

if ($LASTEXITCODE -ne 0) {
  Write-Host ""
  Write-Host "若提示缺少模块，请先安装 UI 依赖：" -ForegroundColor Yellow
  Write-Host '  pip install -e ".[ui]"' -ForegroundColor Yellow
  exit $LASTEXITCODE
}
