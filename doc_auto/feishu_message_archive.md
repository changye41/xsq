# feishu_message_archive（飞书消息归档 CLI）

本模块位于仓库根目录 `src/feishu_message_archive`，通过已登录的 `lark-cli`（用户身份）调用 `im +messages-search`，在指定时间窗口内拉取可见消息，去重后输出：

- `messages.jsonl`：结构化单行 JSON，含 `is_self`、`mentions_me`、`priority` 等字段，便于下游大模型处理。
- `digest.md`：按「重点 / 其他」分组的 Markdown 摘要。

## 依赖与前置

- 本机 `PATH` 上有 `lark-cli`，且已执行用户登录。
- 必须授权 OAuth scope **`search:message`**（消息搜索）。终端执行：`lark-cli auth login --scope "search:message"`；并在飞书开放平台为该应用勾选对应权限。

## 排除群聊（按会话展示名称）

- 搜索 API 不支持按名称排除，实现为 **拉取后本地过滤**：`chat_name` 与配置匹配则丢弃该条消息。
- **Streamlit**：侧栏「不统计的群聊名称」+「群名匹配方式」；配置写入 `~/.feishu-message-archive/exclude_ui_prefs.json`，下次启动自动恢复（环境变量 `FEISHU_ARCHIVE_PREFS_DIR` 可覆盖目录）。
- **CLI**：`--exclude-chat-name` 可重复；`--exclude-chat-match substring|exact`（默认 substring）。

## AI 整理与分析

- 可选依赖：`pip install -e ".[analyze]"`（`httpx`）。
- 环境变量：`OPENAI_API_KEY` 或 `LLM_API_KEY`；可选 `LLM_BASE_URL`（默认 OpenAI v1）、`LLM_MODEL`（默认 `gpt-4o-mini`）。
- `analysis_run.run_analysis` / CLI `feishu-archive-analyze`：读取归档目录生成 `analysis.md`（结构化 Markdown：摘要、待办、时间线、风险、下一步）。
- Streamlit：**「🤖 AI 整理与分析」** 标签页、归档成功后的 **「快捷 AI 分析」** 展开区；侧栏 **「AI 模型配置」** 可选填写 API Key / Base URL / 模型（优先于环境变量）。

## 命令示例

```bash
pip install -e ".[dev]"
python -m feishu_message_archive --date 2026-05-11 --output-dir ./out
```

更多参数见 `python -m feishu_message_archive --help`。

## 可视化界面

- 可选依赖：`pip install -e ".[ui]"`（Streamlit）。
- **一键启动（Windows）：** 仓库根目录双击 **`一键启动可视化.bat`**，或运行 **`start_visual_ui.bat`**（优先 `.venv`）。
- **命令行启动（无需把 Scripts 加入 PATH）：** `python -m feishu_message_archive.ui_run`；另有 `run-ui.bat` / `run-ui.ps1`。
- 若已将 Python `Scripts` 加入 PATH，可使用控制台脚本 `feishu-archive-ui`。
- 等价：`streamlit run src/feishu_message_archive/streamlit_app.py`。

## 修改记录

- 2026-05-11：首次添加 Python 包、`pytest` 单测与文档说明。
- 2026-05-11：抽取 `pipeline.run_archive`；新增 Streamlit 界面（`streamlit_app.py`、`feishu-archive-ui`）。
- 2026-05-11：新增 `ui_run` 模块入口与 `run-ui.bat` / `run-ui.ps1`，避免 Windows 下未配置 PATH 时无法识别 `feishu-archive-ui`。
- 2026-05-11：修复 `streamlit_app.py` 对已删除函数 `_render_results_placeholder` 的调用导致的 `NameError`。
- 2026-05-11：新增根目录一键启动脚本 `start_visual_ui.bat`、`一键启动可视化.bat`，并统一 `run-ui.bat` 入口。
- 2026-05-11：`lark_cli` 对 `missing_scope` / `search:message` 追加中文处理说明；README 与 Streamlit 侧栏补充 scope 授权指引。
- 2026-05-11：支持按会话展示名称排除群聊（`filter_chats`、CLI `--exclude-chat-name`、Streamlit 文本框）；`ArchiveResult` 增加拉取/排除计数；`digest.md` 尾部记录过滤摘要。
- 2026-05-11：Streamlit 排除群聊配置持久化（`ui_prefs.py`）；`try/finally` 在每次脚本重跑结束时写回 prefs（含时间校验失败等提前 return）。
- 2026-05-11：新增 OpenAI 兼容分析链路（`analysis_prompt`、`llm_client`、`analysis_run`、`cli_analyze`）；Streamlit 增加「AI 整理与分析」标签页；可选依赖 `[analyze]`。
- 2026-05-11：Streamlit 强化 AI：侧栏「AI 模型配置」、归档页「快捷 AI 分析」展开区、标签页文案与步骤提示。
- 2026-05-12 10:55（UTC+8）：新增提示词可配置与持久化：侧栏支持编辑 System Prompt / User Template；`analysis_run` 支持覆盖提示词；配置写入 `prompt_ui_prefs.json` 并自动继承上次输入。
- 2026-05-12 11:05（UTC+8）：新增 AI 模型配置持久化（`ai_model_ui_prefs.json`，保存 Key/Base URL/模型并自动继承）；归档改为“每次独立目录”输出，目录名含记录时间窗口与导出时间。
- 2026-05-12 13:55（UTC+8）：新增“导出后自动 AI 分析”开关（默认开启、可关闭），并持久化到 `ai_model_ui_prefs.json`；归档成功后在快捷分析区自动执行模型处理。
- 2026-05-12 13:57（UTC+8）：导出时段设置持久化（`export_window_ui_prefs.json`），自动继承上次的时区、按日历日日期、自定义时段起止日期与时间。
- 2026-05-12 16:08（UTC+8）：AI 分析完成后增加“是否生成飞书文档”确认流程：选“否”不处理，选“是”则创建飞书文档并写入完整分析；标题按“聊天记录日期+飞书信息归档”，同名时自动追加编号（`（2）` 等）。
- 2026-05-15 14:20（UTC+8）：新增 macOS 可分发打包脚手架（`scripts/macos/build_macos.sh` + `feishu_archive.spec` + `dmg_settings.py`），支持在 macOS 上一键生成 `.app` 与 `.dmg`；README 同步补充终端构建与分发说明（目标机仅需外部安装 `lark-cli`）。
- 2026-05-15 14:47（UTC+8）：修复 macOS CI 打包偶发 `NameError: __file__ is not defined`：`feishu_archive.spec` / `dmg_settings.py` 改为优先读取环境变量 `FEISHU_ARCHIVE_ROOT`（回退 `cwd`），并在 `build_macos.sh` 中显式导出该变量。
