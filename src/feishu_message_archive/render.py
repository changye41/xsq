"""Render Markdown digests for human + LLM follow-up."""

from __future__ import annotations

from collections.abc import Iterable

from feishu_message_archive.normalize import NormalizedMessage


def render_digest(
    messages: Iterable[NormalizedMessage],
    *,
    title: str,
) -> str:
    lines: list[str] = [
        f"# {title}",
        "",
        "以下为同一时间窗口内的飞书会话摘录，已按优先级分组。"
        "可直接粘贴到大模型，并要求提取待办、决策与风险点。",
        "",
    ]
    msgs = list(messages)
    high = [m for m in msgs if m.priority == "high"]
    normal = [m for m in msgs if m.priority != "high"]

    lines.append("## 重点（我发送 / @我 / @所有人）")
    lines.append("")
    if high:
        for m in high:
            lines.extend(_format_message_block(m))
            lines.append("")
    else:
        lines.append("_（本时段无高优先级消息）_")
        lines.append("")

    lines.append("## 其他消息")
    lines.append("")
    if normal:
        for m in normal:
            lines.extend(_format_message_block(m))
            lines.append("")
    else:
        lines.append("_（无）_")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "_生成说明：`priority=high` 当消息为我方发送、包含对我的 @，或包含 @所有人。"
        "可按需调整分类规则。_"
    )
    return "\n".join(lines).rstrip() + "\n"


def _format_message_block(m: NormalizedMessage) -> list[str]:
    chat = m.chat_name or m.chat_id or "unknown_chat"
    who = m.sender_name or m.sender_id or "unknown"
    tags: list[str] = []
    if m.is_self:
        tags.append("我发送")
    if m.mentions_me:
        tags.append("@我")
    if m.mentions_all:
        tags.append("@所有人")
    tag_str = f"（{' · '.join(tags)}）" if tags else ""
    head = f"- **{m.create_time}** · `{chat}` · {who} {tag_str}"
    body_lines = [head]
    mt = m.msg_type or "?"
    body_lines.append(f"  - 类型: {mt}；message_id: `{m.message_id}`")
    content = m.content.replace("\r\n", "\n").strip()
    if content:
        for part in content.split("\n"):
            body_lines.append(f"  {part}")
    else:
        body_lines.append("  _(无文本内容或仅资源类消息)_")
    if m.deleted:
        body_lines.append("  _(消息已撤回)_")
    if m.updated:
        body_lines.append("  _(消息已编辑)_")
    return body_lines
