"""Streamlit UI for Feishu message archive."""

from __future__ import annotations

import logging
from datetime import date, time
from pathlib import Path

import streamlit as st

from feishu_message_archive.analysis_prompt import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from feishu_message_archive.filter_chats import parse_exclude_chat_names
from feishu_message_archive.pipeline import ArchiveParams, combine_date_time_to_iso, run_archive
from feishu_message_archive.ui_prefs import (
    ai_model_ui_prefs_path,
    exclude_ui_prefs_path,
    export_window_ui_prefs_path,
    load_ai_model_ui_prefs,
    load_exclude_ui_prefs,
    load_export_window_ui_prefs,
    load_prompt_ui_prefs,
    prompt_ui_prefs_path,
    save_ai_model_ui_prefs,
    save_exclude_ui_prefs,
    save_export_window_ui_prefs,
    save_prompt_ui_prefs,
)

TIMEZONES = [
    "Asia/Shanghai",
    "Asia/Chongqing",
    "UTC",
    "America/New_York",
    "Europe/London",
]

_PAGE_HELP = (
    "依赖本机已登录的 `lark-cli`（用户身份），且需 **search:message** 权限。"
    "若报错 missing_scope，请在终端执行：`lark-cli auth login --scope \"search:message\"`"
)

_SCOPE_BOX = r"""**权限说明**

消息归档使用「消息搜索」接口，必须授权 scope：`search:message`。

若界面或终端出现 `missing required scope(s): search:message`，请在**单独开一个终端**执行：

```
lark-cli auth login --scope "search:message"
```

按提示用浏览器完成授权后，再回到本页点击「拉取并生成」。"""

_AI_DEPS_HINT = (
    "依赖：`pip install -e \".[analyze]\"`。凭证可在 **侧栏 → AI 模型配置** 填写，"
    "或使用环境变量 **OPENAI_API_KEY** / **LLM_API_KEY**。"
)


def _page_limit_value(raw: int) -> int | None:
    if raw <= 0:
        return None
    return min(raw, 40)


def _persist_exclude_prefs() -> None:
    save_exclude_ui_prefs(
        exclude_chat_raw=st.session_state.get("exclude_chat_names_area", ""),
        exclude_chat_match=st.session_state.get("exclude_chat_match_sel", "substring"),
    )


def _persist_prompt_prefs() -> None:
    save_prompt_ui_prefs(
        system_prompt=st.session_state.get("prompt_system_text", ""),
        user_prompt_template=st.session_state.get("prompt_user_template_text", ""),
    )


def _persist_ai_model_prefs() -> None:
    save_ai_model_ui_prefs(
        api_key=st.session_state.get("ai_cfg_api_key", ""),
        base_url=st.session_state.get("ai_cfg_base_url", ""),
        model=st.session_state.get("ai_cfg_model", ""),
        auto_analyze_after_export=bool(
            st.session_state.get("ai_auto_analyze_after_export", True)
        ),
    )


def _persist_export_window_prefs() -> None:
    save_export_window_ui_prefs(
        timezone=str(st.session_state.get("export_tz_sel", "Asia/Shanghai")),
        cal_day=str(st.session_state.get("cal_day", "")),
        rng_sd=str(st.session_state.get("rng_sd", "")),
        rng_st=str(st.session_state.get("rng_st", "")),
        rng_ed=str(st.session_state.get("rng_ed", "")),
        rng_et=str(st.session_state.get("rng_et", "")),
    )


def _safe_date(s: str, fallback: date) -> date:
    try:
        return date.fromisoformat(s)
    except ValueError:
        return fallback


def _safe_time(s: str, fallback: time) -> time:
    try:
        return time.fromisoformat(s)
    except ValueError:
        return fallback


def _browse_directory_dialog(initial_dir: str) -> str | None:
    """Open native folder picker (best-effort). Returns selected path or None."""
    try:
        import tkinter as tk
        from tkinter import filedialog
    except Exception:
        return None
    try:
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        path = filedialog.askdirectory(
            initialdir=initial_dir or str(Path.cwd()),
            title="选择输出目录",
        )
        root.destroy()
        if path:
            return path
        return None
    except Exception:
        return None


def _llm_overrides_from_sidebar() -> dict[str, str | None]:
    """Optional API settings from sidebar (None => fall back to env in analysis_run)."""
    key = (st.session_state.get("ai_cfg_api_key") or "").strip()
    bu = (st.session_state.get("ai_cfg_base_url") or "").strip()
    mo = (st.session_state.get("ai_cfg_model") or "").strip()
    return {
        "api_key": key or None,
        "base_url": bu or None,
        "model": mo or None,
    }


def _show_ai_analysis_result(ar, *, download_key: str, archive_dir: Path) -> None:
    if ar.outcome != "ok":
        st.error(ar.error_message or "分析失败")
        return
    # Persist latest analysis so follow-up actions survive Streamlit reruns.
    if ar.markdown:
        st.session_state["latest_analysis_markdown"] = ar.markdown
        st.session_state["latest_analysis_archive_dir"] = str(archive_dir)
        st.session_state["latest_analysis_output_path"] = str(ar.output_path or "")

    st.success(
        f"已写入 `{ar.output_path}`（归档材料约 **{ar.bundle_chars}** 字符）"
    )
    if ar.markdown:
        with st.expander("报告预览", expanded=True):
            st.markdown(ar.markdown)
        st.download_button(
            "下载 analysis.md",
            ar.markdown.encode("utf-8"),
            file_name="analysis.md",
            mime="text/markdown",
            key=download_key,
        )


def _render_feishu_doc_export_panel(*, prefix: str) -> None:
    """Render persistent one-click panel for exporting latest analysis to Feishu Doc."""
    md = st.session_state.get("latest_analysis_markdown")
    ad = st.session_state.get("latest_analysis_archive_dir")
    if not isinstance(md, str) or not md.strip():
        return
    if not isinstance(ad, str) or not ad.strip():
        return

    st.markdown("### 生成飞书文档")

    if st.button(
        "生成飞书文档",
        type="primary",
        key=f"{prefix}_feishu_confirm",
    ):
        from feishu_message_archive.lark_doc_export import create_feishu_doc_from_analysis

        with st.spinner("正在创建飞书文档…"):
            doc_res = create_feishu_doc_from_analysis(
                input_dir=Path(ad),
                analysis_markdown=md,
            )
        if not doc_res.ok:
            st.error(doc_res.error or "创建飞书文档失败")
        else:
            st.success(f"飞书文档创建成功：`{doc_res.title}`")
            if doc_res.url:
                st.markdown(f"[打开飞书文档]({doc_res.url})")


def _run_ai_analysis_dispatch(prefix: str) -> None:
    from feishu_message_archive.analysis_run import AnalyzeParams, run_analysis

    oo = _llm_overrides_from_sidebar()
    key_dir = f"ai_{prefix}_archive_dir"
    key_ctx = f"ai_{prefix}_extra_ctx"
    key_max = f"ai_{prefix}_max_chars"

    ap = AnalyzeParams(
        input_dir=Path(st.session_state.get(key_dir, "").strip()).expanduser(),
        extra_context=(st.session_state.get(key_ctx) or "").strip() or None,
        max_bundle_chars=int(st.session_state.get(key_max, 120000)),
        api_key=oo["api_key"],
        base_url=oo["base_url"],
        model=oo["model"],
        system_prompt=(st.session_state.get("prompt_system_text") or "").strip() or None,
        user_prompt_template=(st.session_state.get("prompt_user_template_text") or "").strip() or None,
    )
    with st.spinner("正在调用大模型…"):
        ar = run_analysis(ap)
    st.session_state["last_ai_analyzed_archive_dir"] = str(ap.input_dir)
    _show_ai_analysis_result(
        ar,
        download_key=f"dl_analysis_md_{prefix}",
        archive_dir=ap.input_dir,
    )


def _render_ai_analysis_form(
    prefix: str,
    default_archive_dir: Path,
    *,
    show_heading: bool,
) -> None:
    """Shared AI form. Use prefix ``tab`` or ``inline`` for unique widget keys."""
    key_dir = f"ai_{prefix}_archive_dir"
    key_ctx = f"ai_{prefix}_extra_ctx"
    key_max = f"ai_{prefix}_max_chars"
    key_btn = f"ai_{prefix}_generate_btn"
    key_show_adv = f"ai_{prefix}_show_adv"

    if key_dir not in st.session_state:
        st.session_state[key_dir] = str(default_archive_dir)
    if key_show_adv not in st.session_state:
        st.session_state[key_show_adv] = False

    if show_heading:
        st.subheader("AI 整理与分析")
        st.caption(
            "读取 **digest.md** 与 **messages.jsonl**，生成 **analysis.md**（要点、待办、时间线、风险与建议）。"
            + _AI_DEPS_HINT
        )
    else:
        st.caption(_AI_DEPS_HINT)

    st.text_input(
        "归档目录（须含 digest.md 或 messages.jsonl）",
        key=key_dir,
        help="通常与侧栏「输出目录」一致；也可指向其它已归档文件夹。",
    )
    st.checkbox(
        "显示高级参数（补充说明 / 最大字符数）",
        key=key_show_adv,
    )
    if st.session_state.get(key_show_adv, False):
        st.text_area(
            "补充说明（可选，会一并交给模型）",
            height=90,
            key=key_ctx,
        )
        st.number_input(
            "送入模型的最大字符数",
            min_value=5000,
            max_value=500000,
            value=120000,
            step=5000,
            key=key_max,
        )
        btn_label = "重新生成分析报告" if prefix == "inline" else "生成分析报告"
        if st.button(btn_label, type="primary", key=key_btn, use_container_width=True):
            _run_ai_analysis_dispatch(prefix)
    else:
        # Ensure defaults remain available even when hidden.
        if key_ctx not in st.session_state:
            st.session_state[key_ctx] = ""
        if key_max not in st.session_state:
            st.session_state[key_max] = 120000
        if prefix != "inline":
            if st.button("生成分析报告", type="primary", key=key_btn, use_container_width=True):
                _run_ai_analysis_dispatch(prefix)

    _render_feishu_doc_export_panel(prefix=f"{prefix}_panel")


def main() -> None:
    st.set_page_config(
        page_title="飞书消息归档",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("飞书消息归档")
    st.caption(_PAGE_HELP)

    _prefs = load_exclude_ui_prefs()
    _prompt_prefs = load_prompt_ui_prefs()
    _ai_model_prefs = load_ai_model_ui_prefs()
    _window_prefs = load_export_window_ui_prefs()
    if "exclude_chat_names_area" not in st.session_state:
        st.session_state["exclude_chat_names_area"] = _prefs.get("exclude_chat_raw", "")
    if "exclude_chat_match_sel" not in st.session_state:
        st.session_state["exclude_chat_match_sel"] = _prefs.get("exclude_chat_match", "substring")
    if "prompt_system_text" not in st.session_state:
        st.session_state["prompt_system_text"] = (
            _prompt_prefs.get("system_prompt") or SYSTEM_PROMPT
        )
    if "prompt_user_template_text" not in st.session_state:
        st.session_state["prompt_user_template_text"] = (
            _prompt_prefs.get("user_prompt_template") or USER_PROMPT_TEMPLATE
        )
    if "ai_cfg_api_key" not in st.session_state:
        st.session_state["ai_cfg_api_key"] = _ai_model_prefs.get("api_key", "")
    if "ai_cfg_base_url" not in st.session_state:
        st.session_state["ai_cfg_base_url"] = _ai_model_prefs.get("base_url", "")
    if "ai_cfg_model" not in st.session_state:
        st.session_state["ai_cfg_model"] = _ai_model_prefs.get("model", "")
    if "ai_auto_analyze_after_export" not in st.session_state:
        st.session_state["ai_auto_analyze_after_export"] = _ai_model_prefs.get(
            "auto_analyze_after_export",
            True,
        )
    today = date.today()
    if "export_tz_sel" not in st.session_state:
        st.session_state["export_tz_sel"] = _window_prefs.get("timezone") or "Asia/Shanghai"
    if "cal_day" not in st.session_state:
        st.session_state["cal_day"] = _safe_date(_window_prefs.get("cal_day", ""), today)
    if "rng_sd" not in st.session_state:
        st.session_state["rng_sd"] = _safe_date(_window_prefs.get("rng_sd", ""), today)
    if "rng_st" not in st.session_state:
        st.session_state["rng_st"] = _safe_time(_window_prefs.get("rng_st", ""), time(9, 0))
    if "rng_ed" not in st.session_state:
        st.session_state["rng_ed"] = _safe_date(_window_prefs.get("rng_ed", ""), today)
    if "rng_et" not in st.session_state:
        st.session_state["rng_et"] = _safe_time(_window_prefs.get("rng_et", ""), time(18, 0))

    default_out = Path.cwd() / "feishu_archive_out"
    if "output_dir_input" not in st.session_state:
        st.session_state["output_dir_input"] = str(default_out)

    try:
        with st.sidebar:
            with st.expander("首次使用 / 提示缺少 search:message？"):
                st.markdown(_SCOPE_BOX)
            st.header("输出与高级选项")
            st.text_input(
                "输出目录",
                key="output_dir_input",
                disabled=True,
                help="通过下方“浏览文件夹选择输出目录”按钮选择路径。",
            )
            if st.button("浏览文件夹选择输出目录", key="btn_browse_output_dir", use_container_width=True):
                selected = _browse_directory_dialog(st.session_state.get("output_dir_input", ""))
                if selected:
                    st.session_state["output_dir_input"] = selected
                else:
                    st.info("未选择目录，保持当前输出目录。")

            chat_id_raw = st.text_input(
                "限定会话 chat_id",
                value="",
                placeholder="可选 oc_xxx",
            )
            skip_at_me = st.checkbox(
                "跳过「@我」第二次检索",
                value=False,
                help="仅执行宽泛检索一遍，略慢场景或调试时可勾选",
            )
            st.text_area(
                "不统计的群聊名称",
                height=96,
                key="exclude_chat_names_area",
                placeholder="每行一个；也可用英文逗号、中文逗号分隔。默认「子串」：群名包含该文字即整群排除。",
                help=(
                    "拉取后过滤：匹配到的会话内消息不会写入 JSONL / 摘要。"
                    "上次输入会自动恢复；每次页面刷新会写回本地配置。"
                    f" 文件：`{exclude_ui_prefs_path()}`"
                ),
            )
            with st.expander("其他设置"):
                lark_cli_raw = st.text_input(
                    "lark-cli 路径",
                    value="",
                    placeholder="留空则使用 PATH 中的 lark-cli",
                )
                page_limit_raw = st.number_input(
                    "page-limit（分页上限）",
                    min_value=0,
                    max_value=40,
                    value=0,
                    help="0 表示交给 CLI 默认值；最大 40（与飞书搜索分页一致）",
                )
                st.selectbox(
                    "群名匹配方式",
                    options=("substring", "exact"),
                    format_func=lambda m: "子串（名称包含即排除）" if m == "substring" else "完全相等（忽略大小写）",
                    key="exclude_chat_match_sel",
                )
                st.selectbox(
                    "时区",
                    TIMEZONES,
                    key="export_tz_sel",
                    help=f"导出时段会自动保存并继承（本地文件：`{export_window_ui_prefs_path()}`）",
                )

            with st.expander("🤖 AI 模型配置（可选）"):
                st.caption(
                    "此处填写优先生效；全部留空则使用环境变量 "
                    "**OPENAI_API_KEY** 或 **LLM_API_KEY**，以及 **LLM_BASE_URL**、**LLM_MODEL**。"
                    f" 本地保存：`{ai_model_ui_prefs_path()}`"
                )
                st.text_input(
                    "API Key",
                    type="password",
                    key="ai_cfg_api_key",
                    placeholder="留空则用环境变量",
                )
                st.text_input(
                    "API Base URL",
                    key="ai_cfg_base_url",
                    placeholder="默认 https://api.openai.com/v1",
                )
                st.text_input(
                    "模型名称",
                    key="ai_cfg_model",
                    placeholder="默认 gpt-4o-mini",
                )
                st.checkbox(
                    "导出后自动执行 AI 分析",
                    key="ai_auto_analyze_after_export",
                    value=True,
                    help="默认开启。关闭后需手动点击“生成分析报告”。",
                )

            with st.expander("🧠 提示词配置（可编辑并自动保存）"):
                st.caption(
                    "支持变量：`{archive_bundle}`、`{extra_context_block}`。"
                    f" 本地保存：`{prompt_ui_prefs_path()}`"
                )
                st.text_area(
                    "系统提示词（System Prompt）",
                    key="prompt_system_text",
                    height=220,
                )
                st.text_area(
                    "用户提示词模板（User Template）",
                    key="prompt_user_template_text",
                    height=180,
                )

        out_dir_raw = st.session_state.get("output_dir_input", "")
        out_dir = Path((out_dir_raw or str(default_out)).strip()).expanduser()

        tab_archive, tab_ai = st.tabs(["📥 消息归档", "🤖 AI 整理与分析"])

        with tab_archive:
            st.markdown("### 1) 拉取飞书消息")
            col_left, col_right = st.columns([1, 1], gap="large")

            with col_left:
                st.subheader("方式一：按日历日")
                day = st.date_input("日期", key="cal_day")
                run_cal = st.button(
                    "拉取并生成",
                    type="primary",
                    key="btn_cal",
                    use_container_width=True,
                )

            with col_right:
                st.subheader("方式二：自定义时间段")
                r1, r2 = st.columns(2)
                with r1:
                    sd = st.date_input("开始日期", key="rng_sd")
                    st_time = st.time_input("开始时间", key="rng_st")
                with r2:
                    ed = st.date_input("结束日期", key="rng_ed")
                    et_time = st.time_input("结束时间", key="rng_et")
                run_rng = st.button(
                    "拉取并生成",
                    type="primary",
                    key="btn_rng",
                    use_container_width=True,
                )

            lark_cli = lark_cli_raw.strip() or None
            chat_id = chat_id_raw.strip() or None
            plim = _page_limit_value(int(page_limit_raw))
            exclude_raw = st.session_state.get("exclude_chat_names_area", "")
            exclude_match = st.session_state.get("exclude_chat_match_sel", "substring")
            exclude_patterns = tuple(parse_exclude_chat_names(exclude_raw))

            tz = str(st.session_state.get("export_tz_sel", "Asia/Shanghai"))

            if run_cal:
                ds = day.isoformat()
                params = ArchiveParams(
                    mode="date",
                    timezone=tz,
                    calendar_date=ds,
                    output_dir=out_dir,
                    lark_cli=lark_cli,
                    page_limit=plim,
                    chat_id=chat_id,
                    skip_at_me_pass=skip_at_me,
                    exclude_chat_names=exclude_patterns,
                    exclude_chat_match=exclude_match,
                )
                _run_and_display(params)

            if run_rng:
                try:
                    start_iso = combine_date_time_to_iso(sd, st_time, tz)
                    end_iso = combine_date_time_to_iso(ed, et_time, tz)
                except Exception as e:
                    st.error(f"时间组合失败: {e}")
                    return
                if start_iso > end_iso:
                    st.error("开始时间不能晚于结束时间")
                    return
                params = ArchiveParams(
                    mode="range",
                    timezone=tz,
                    start_iso=start_iso,
                    end_iso=end_iso,
                    output_dir=out_dir,
                    lark_cli=lark_cli,
                    page_limit=plim,
                    chat_id=chat_id,
                    skip_at_me_pass=skip_at_me,
                    exclude_chat_names=exclude_patterns,
                    exclude_chat_match=exclude_match,
                )
                _run_and_display(params)
            st.markdown("### 2) 拉取结果")
            with st.container(border=True):
                _render_last_archive_result_panel()

        with tab_ai:
            _render_ai_analysis_form("tab", out_dir, show_heading=True)
    finally:
        _persist_exclude_prefs()
        _persist_prompt_prefs()
        _persist_ai_model_prefs()
        _persist_export_window_prefs()


def _run_and_display(params: ArchiveParams) -> None:
    log = logging.getLogger("feishu_message_archive.run")
    if not log.handlers:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    with st.status("正在调用 lark-cli 拉取消息…", expanded=True) as status:
        result = run_archive(params, logger=log)
        if result.outcome == "ok":
            status.update(label="完成", state="complete")
        else:
            status.update(label="失败", state="error")

    st.session_state["last_archive_result"] = result
    st.session_state["last_archive_output_dir"] = str(params.output_dir)


def _render_last_archive_result_panel() -> None:
    result = st.session_state.get("last_archive_result")
    output_dir = st.session_state.get("last_archive_output_dir")
    if result is None:
        return
    if getattr(result, "outcome", None) == "error":
        st.error(result.error_message or "未知错误")
        return

    params_output_dir = Path(output_dir) if isinstance(output_dir, str) and output_dir else Path.cwd()
    ok_parts = [
        f"已写入 **{result.message_count}** 条消息（其中高优先级 **{result.high_priority_count}** 条）"
    ]
    if result.excluded_by_chat_name > 0:
        ok_parts.append(
            f"从拉取的 **{result.fetched_count}** 条中按群名排除了 **{result.excluded_by_chat_name}** 条。"
        )
    st.success("".join(ok_parts))

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("保留条数", result.message_count)
    c2.metric("高优先级", result.high_priority_count)
    c3.metric("拉取条数", result.fetched_count)
    c4.metric("按群名排除", result.excluded_by_chat_name)
    archive_dir = result.archive_dir or params_output_dir
    st.caption(f"本次导出目录：`{archive_dir}`")
    with st.expander("查看详细信息（摘要预览 / 下载）", expanded=False):
        if result.digest_text:
            st.markdown("#### 摘要预览")
            st.markdown(result.digest_text)

        dl_col1, dl_col2 = st.columns(2)
        if result.digest_text:
            dl_col1.download_button(
                label="下载 digest.md",
                data=result.digest_text.encode("utf-8"),
                file_name="digest.md",
                mime="text/markdown",
                use_container_width=True,
            )
        if result.jsonl_path and result.jsonl_path.is_file():
            data_bytes = result.jsonl_path.read_bytes()
            dl_col2.download_button(
                label="下载 messages.jsonl",
                data=data_bytes,
                file_name="messages.jsonl",
                mime="application/jsonl",
                use_container_width=True,
            )

    st.markdown("### 3) 快捷 AI 分析")
    with st.container(border=True):
        st.session_state["ai_inline_archive_dir"] = str(archive_dir)
        st.markdown(
            "归档已完成。可直接在本页生成 **analysis.md**，无需切换标签页；"
            "API Key 可在侧栏 **「AI 模型配置」** 填写。"
        )
        if st.session_state.get("ai_auto_analyze_after_export", True):
            last_auto_for = st.session_state.get("last_ai_analyzed_archive_dir", "")
            current_archive = str(archive_dir)
            if last_auto_for != current_archive:
                st.info("已启用自动分析：正在基于本次导出结果调用大模型。")
                _run_ai_analysis_dispatch("inline")
                st.divider()
        _render_ai_analysis_form(
            "inline",
            Path(archive_dir),
            show_heading=False,
        )


if __name__ == "__main__":
    main()
