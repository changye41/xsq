# feishu-message-archive

通过本机已登录的 `lark-cli`（**用户身份**）拉取飞书消息，输出 JSONL 与 Markdown，便于后续交给大模型做每日摘要与待办抽取。

## 前置条件

- 已安装 `lark-cli` 并完成用户登录。
- **必须**具备「搜索消息」OAuth scope（`search:message`），否则消息检索会失败。首次使用或提示 `missing_scope` 时，在终端执行（按提示在浏览器完成授权）：

```bash
lark-cli auth login --scope "search:message"
```

- 飞书开放平台里该应用也需勾选对应权限后再授权。

## 可视化界面（Streamlit）

安装 UI；若需 **AI 整理与分析** 标签页，一并安装 analyze（含 httpx）：

```bash
pip install -e ".[ui,analyze]"
```

**一键启动（Windows，推荐）：** 在仓库根目录双击 **`一键启动可视化.bat`**，或运行 **`start_visual_ui.bat`**（同一逻辑）。脚本会优先使用项目下的 **`.venv`**（若存在），否则使用系统的 `python` / `py`。

**命令行（不依赖 Python Scripts 是否在 PATH）：**

```bash
python -m feishu_message_archive.ui_run
```

或在仓库根目录运行 **`run-ui.bat`** / **`run-ui.ps1`**（与上一键脚本等价）。

可选：若已将 Python 的 `Scripts` 目录加入系统 PATH，也可直接运行 `feishu-archive-ui`。

等价方式：

```bash
streamlit run src/feishu_message_archive/streamlit_app.py
```

浏览器中会打开本地页面：**「消息归档」** 中拉取与下载；**「AI 整理与分析」** 中基于归档目录生成待办/要点报告（需环境变量中的 API Key 与 `.[analyze]` 依赖）。

> 说明：侧栏里的 **AI 模型配置**（Key / Base URL / 模型名）会自动保存并继承上次输入。
> 同一处新增开关 **“导出后自动执行 AI 分析”**，默认开启；关闭后需手动触发分析。
> 导出时段设置（时区、按日历日日期、自定义时段起止）也会自动保存并继承上次输入。
> 侧栏已提供 **“浏览文件夹选择输出目录”** 按钮，并将 `lark-cli路径 / 分页上限 / 群名匹配方式 / 时区` 收纳在 **“其他设置”** 折叠区。

## macOS 一键安装包（.app + DMG）

如果希望 macOS 用户无需手动安装 Python，可在 macOS 构建机上制作分发包（应用内已打包 Python 运行时与项目依赖）：

```bash
chmod +x scripts/macos/build_macos.sh
./scripts/macos/build_macos.sh
```

构建产物：

- `dist/Feishu Message Archive.app`
- `dist/Feishu-Message-Archive.dmg`

说明：

- `.app` 可直接双击启动（初次可能需在系统设置中允许打开）。
- `.dmg` 适合发给其他 macOS 用户安装。
- **目标用户仍需安装并登录 `lark-cli`**（这是唯一外部依赖）：

```bash
npm i -g @larksuiteoapi/lark-cli
lark-cli auth login --scope "search:message,search:docs:read"
```

## 用法（命令行）

```bash
pip install -e ".[dev]"
# 按本地日历日归档（默认上海时区）
feishu-archive --date 2026-05-11 --output-dir ./out
# 自定义时间范围（须带时区偏移）
feishu-archive --start "2026-05-11T00:00:00+08:00" --end "2026-05-11T23:59:59+08:00" --output-dir ./out
```

输出目录中会生成：

- 每次导出都会创建单独目录：`<时间窗口>__export_<导出时间>/`
- 子目录内固定产物：
  - `messages.jsonl`：去重后的结构化消息（一行一条 JSON）。
  - `digest.md`：按「我发送 / @我 / 其他」分组的可读摘要。

## 排除指定群聊（按会话展示名称）

飞书搜索接口无法直接「按名称排除」，因此工具会先拉取再在本地过滤：凡 **会话展示名称**（群名或私聊对方昵称）匹配你配置的条目，其下消息 **不会写入** `messages.jsonl` / `digest.md`。

- **可视化**：侧栏「不统计的群聊名称」文本框，每行一个，或逗号分隔；可选「子串」或「完全相等」（均忽略大小写）。**输入会自动保存**到本机 `~/.feishu-message-archive/exclude_ui_prefs.json`，下次打开界面自动恢复，可直接增删改。
- **命令行**：

```bash
# 群名包含「灌水」的会话全部不写入结果（可重复传参）
feishu-archive --date 2026-05-11 --output-dir ./out --exclude-chat-name "灌水"
# 完全等于「全员群」才排除
feishu-archive --date 2026-05-11 --output-dir ./out --exclude-chat-name "全员群" --exclude-chat-match exact
```

## AI 整理与分析（OpenAI 兼容接口）

安装分析依赖（含 `httpx`）：

```bash
pip install -e ".[analyze]"
```

在系统环境变量中配置（**勿**将 Key 写进代码或提交仓库）：

| 变量 | 说明 |
|------|------|
| `OPENAI_API_KEY` 或 `LLM_API_KEY` | 必填 |
| `LLM_BASE_URL` | 可选，默认 `https://api.openai.com/v1`（国内兼容网关、Azure OpenAI 等可改） |
| `LLM_MODEL` | 可选，默认 `gpt-4o-mini` |

对某次归档目录生成 `analysis.md`（含待办、关注点、时间线、风险与建议）：

```bash
feishu-archive-analyze --input-dir ./feishu_archive_out
# 或指定输出路径
feishu-archive-analyze --input-dir ./out --output ./out/my_analysis.md
```

**Streamlit** 中打开 **「AI 整理与分析」** 标签页，可基于同一归档目录一键生成并预览/下载报告。

### 提示词自定义（可视化）

- 在侧栏展开 **「🧠 提示词配置（可编辑并自动保存）」**：
  - `系统提示词（System Prompt）`
  - `用户提示词模板（User Template）`
- 用户模板支持两个占位变量：
  - `{archive_bundle}`：归档文本内容
  - `{extra_context_block}`：你在“补充说明”输入的文本块（可为空）
- 配置会自动保存到本机：
  - `~/.feishu-message-archive/prompt_ui_prefs.json`
- 留空时会回退到项目默认提示词。

### 分析后生成飞书文档（可选确认）

- AI 分析完成后，界面会出现 **“是否生成飞书文档？”** 选项。
- 选择 **否**：不做任何后续操作。
- 选择 **是** 并确认：自动新建飞书文档并写入完整分析结果。
- 文档标题规则：
  - 基础：`聊天记录日期 + 飞书信息归档`
  - 若同名已存在：自动追加编号，如 `（2）`、`（3）` … 进行区分。

## 说明
