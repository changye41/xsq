"""Prompt templates for archive analysis (Chinese)."""

SYSTEM_PROMPT = """你是一名高效的职业助理，擅长从即时通讯记录中提炼可执行信息与风险。
用户提供了飞书会话归档（含摘要 digest 与结构化 messages.jsonl 节选）。
请基于这些内容输出一份 **Markdown** 报告，语言简洁、条理清晰，避免空话。

必须包含以下二级标题（按顺序）：
## 关键信息摘要
## 需要我关注的任务与待办
## 时间节点与截止时间
## 风险、阻塞与依赖
## 建议的下一步行动

在「需要我关注的任务与待办」中，请区分：
- **明确指派给我的 / @我的**：优先列出，可加粗；
- **与我相关但待确认的**：次序列出；
- 若能推断截止日期或优先级，请标注。

若材料中信息不足，请在对应小节诚实说明「原文未提及」，不要编造事实。"""

USER_PROMPT_TEMPLATE = """以下是本次归档材料（可能包含 digest.md 与 messages.jsonl 节选）：

```archive
{archive_bundle}
```
{extra_context_block}
请按要求输出 Markdown 分析报告。"""


def user_message_body(archive_bundle: str, extra_context: str | None = None) -> str:
    return render_user_prompt(
        archive_bundle=archive_bundle,
        extra_context=extra_context,
        template=USER_PROMPT_TEMPLATE,
    )


def render_user_prompt(
    *,
    archive_bundle: str,
    extra_context: str | None,
    template: str,
) -> str:
    """Render user prompt from a template with safe fallback."""
    extra_block = ""
    if extra_context and extra_context.strip():
        extra_block = f"用户补充说明：\n{extra_context.strip()}\n"
    try:
        rendered = template.format(
            archive_bundle=archive_bundle,
            extra_context_block=extra_block,
        )
    except (KeyError, ValueError):
        parts = [
            "以下是本次归档材料（可能包含 digest.md 与 messages.jsonl 节选）：\n\n",
            "```archive\n",
            archive_bundle,
            "\n```\n",
        ]
        if extra_block:
            parts.extend(["\n", extra_block])
        parts.append("\n请按要求输出 Markdown 分析报告。")
        rendered = "".join(parts)
    return rendered
