"""list / show / history / thesis_updates 출력용 markdown / 텍스트 렌더러."""
from __future__ import annotations

from typing import Iterable

from ._db import HistoryRow, ThesisUpdate, WatchlistItem


def _short(text: str | None, n: int = 60) -> str:
    if not text:
        return ""
    text = text.replace("\n", " ").strip()
    return text if len(text) <= n else text[: n - 1] + "…"


def render_list_table(items: Iterable[WatchlistItem]) -> str:
    items = list(items)
    if not items:
        return "(no watchlist items)"
    header = (
        "| ID | Thesis | Item | Importance | Status | Impact | Tickers | Updated |\n"
        "|---:|---|---|---|---|---|---|---|"
    )
    rows = [header]
    for it in items:
        rows.append(
            "| {id} | {thesis} | {item} | {imp} | {status} | {impact} | {tickers} | {updated} |".format(
                id=it.id,
                thesis=_short(it.thesis, 16),
                item=_short(it.item, 38),
                imp=it.importance or "",
                status=it.status,
                impact=it.thesis_impact or "",
                tickers=",".join(it.tickers) if it.tickers else "",
                updated=(it.last_updated or "")[:16],
            )
        )
    return "\n".join(rows)


def render_show(item: WatchlistItem) -> str:
    lines = [
        f"# [{item.id}] {item.item}",
        "",
        f"- **Thesis**: {item.thesis}",
        f"- **Importance**: {item.importance or '-'}",
        f"- **Status**: {item.status}",
        f"- **Thesis Impact**: {item.thesis_impact or '-'}",
        f"- **Tickers**: {', '.join(item.tickers) if item.tickers else '-'}",
        f"- **Created**: {item.created_at}",
        f"- **Last updated**: {item.last_updated}",
        "",
        "## Trigger",
        item.trigger_criteria or "_(none)_",
        "",
        "## Resolution",
        item.resolution_note or "_(none)_",
    ]
    return "\n".join(lines)


def render_history(item: WatchlistItem, rows: Iterable[HistoryRow]) -> str:
    rows = list(rows)
    out = [f"# History — [{item.id}] {item.item}", "", f"Thesis: {item.thesis}", ""]
    if not rows:
        out.append("_(no history)_")
        return "\n".join(out)
    out.append("| When | Field | Old | New | Source |")
    out.append("|---|---|---|---|---|")
    for r in rows:
        out.append(
            "| {when} | {field} | {old} | {new} | {src} |".format(
                when=r.changed_at[:16],
                field=r.field,
                old=_short(r.old_value, 30) or "_∅_",
                new=_short(r.new_value, 30) or "_∅_",
                src=_short(r.note, 28),
            )
        )
    return "\n".join(out)


def render_thesis_updates(updates: Iterable[ThesisUpdate]) -> str:
    updates = list(updates)
    if not updates:
        return "(no thesis updates)"
    header = (
        "| When | Thesis | Item | Before | After | Source |\n"
        "|---|---|---|---|---|---|"
    )
    rows = [header]
    for u in updates:
        rows.append(
            "| {when} | {thesis} | {item} | {before} | {after} | {src} |".format(
                when=(u.changed_at or "")[:16],
                thesis=_short(u.thesis, 16),
                item=_short(u.item, 28),
                before=_short(u.before_text, 36),
                after=_short(u.after_text, 36),
                src=_short(u.source, 24),
            )
        )
    return "\n".join(rows)
