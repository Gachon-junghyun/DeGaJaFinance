"""watchlist.db 스키마 + CRUD.

3 테이블:
    watchlist          — 현재 상태 (UNIQUE(thesis, item))
    watchlist_history  — field-level 변경 로그
    thesis_updates     — §6-6 "Thesis 업데이트 변경 전/후" 표
"""
from __future__ import annotations

import json
import os
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable, Iterator, Optional

STATUS_VALUES = ("open", "partial", "resolved", "split", "rejected")
IMPORTANCE_VALUES = ("high", "mid", "low")
THESIS_IMPACT_VALUES = ("강화", "부분", "부정", "정보공백")

DB_FILENAME = "watchlist.db"


def default_db_path() -> Path:
    """`WATCHLIST_DB_PATH` env 우선, 없으면 프로젝트 루트(research_Mvp/) 기준."""
    env = os.environ.get("WATCHLIST_DB_PATH")
    if env:
        return Path(env).expanduser().resolve()
    here = Path(__file__).resolve().parent
    return here.parent / "data" / DB_FILENAME


SCHEMA = """
CREATE TABLE IF NOT EXISTS watchlist (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    thesis           TEXT NOT NULL,
    item             TEXT NOT NULL,
    trigger_criteria TEXT,
    importance       TEXT,
    status           TEXT NOT NULL DEFAULT 'open',
    tickers          TEXT,
    resolution_note  TEXT,
    thesis_impact    TEXT,
    created_at       TEXT NOT NULL,
    last_updated     TEXT NOT NULL,
    UNIQUE(thesis, item)
);

CREATE INDEX IF NOT EXISTS idx_watchlist_thesis ON watchlist(thesis);
CREATE INDEX IF NOT EXISTS idx_watchlist_status ON watchlist(status);

CREATE TABLE IF NOT EXISTS watchlist_history (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    watchlist_id INTEGER NOT NULL REFERENCES watchlist(id) ON DELETE CASCADE,
    field        TEXT NOT NULL,
    old_value    TEXT,
    new_value    TEXT,
    changed_at   TEXT NOT NULL,
    note         TEXT
);

CREATE INDEX IF NOT EXISTS idx_history_watchlist ON watchlist_history(watchlist_id);

CREATE TABLE IF NOT EXISTS thesis_updates (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    thesis      TEXT NOT NULL,
    item        TEXT,
    before_text TEXT,
    after_text  TEXT,
    source      TEXT,
    changed_at  TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_thesis_updates_thesis ON thesis_updates(thesis);
"""


@dataclass
class WatchlistItem:
    id: Optional[int] = None
    thesis: str = ""
    item: str = ""
    trigger_criteria: Optional[str] = None
    importance: Optional[str] = None
    status: str = "open"
    tickers: list[str] = field(default_factory=list)
    resolution_note: Optional[str] = None
    thesis_impact: Optional[str] = None
    created_at: Optional[str] = None
    last_updated: Optional[str] = None

    def to_row(self) -> dict:
        return {
            "thesis": self.thesis,
            "item": self.item,
            "trigger_criteria": self.trigger_criteria,
            "importance": self.importance,
            "status": self.status,
            "tickers": json.dumps(self.tickers, ensure_ascii=False) if self.tickers else None,
            "resolution_note": self.resolution_note,
            "thesis_impact": self.thesis_impact,
        }

    def to_dict(self) -> dict:
        d = asdict(self)
        return d


@dataclass
class HistoryRow:
    id: int
    watchlist_id: int
    field: str
    old_value: Optional[str]
    new_value: Optional[str]
    changed_at: str
    note: Optional[str]


@dataclass
class ThesisUpdate:
    id: Optional[int] = None
    thesis: str = ""
    item: Optional[str] = None
    before_text: Optional[str] = None
    after_text: Optional[str] = None
    source: Optional[str] = None
    changed_at: Optional[str] = None


def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _row_to_item(row: sqlite3.Row) -> WatchlistItem:
    tickers_raw = row["tickers"]
    tickers: list[str] = []
    if tickers_raw:
        try:
            parsed = json.loads(tickers_raw)
            if isinstance(parsed, list):
                tickers = [str(x) for x in parsed]
        except json.JSONDecodeError:
            tickers = [t.strip() for t in tickers_raw.split(",") if t.strip()]
    return WatchlistItem(
        id=row["id"],
        thesis=row["thesis"],
        item=row["item"],
        trigger_criteria=row["trigger_criteria"],
        importance=row["importance"],
        status=row["status"],
        tickers=tickers,
        resolution_note=row["resolution_note"],
        thesis_impact=row["thesis_impact"],
        created_at=row["created_at"],
        last_updated=row["last_updated"],
    )


@contextmanager
def connect(db_path: Optional[Path] = None) -> Iterator[sqlite3.Connection]:
    path = db_path or default_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db(db_path: Optional[Path] = None) -> Path:
    path = db_path or default_db_path()
    with connect(path) as conn:
        conn.executescript(SCHEMA)
    return path


def _validate_enum(name: str, value: Optional[str], allowed: tuple[str, ...]) -> None:
    if value is None:
        return
    if value not in allowed:
        raise ValueError(f"{name} must be one of {allowed}, got {value!r}")


def _validate_item(item: WatchlistItem) -> None:
    if not item.thesis or not item.thesis.strip():
        raise ValueError("thesis is required")
    if not item.item or not item.item.strip():
        raise ValueError("item is required")
    _validate_enum("status", item.status, STATUS_VALUES)
    _validate_enum("importance", item.importance, IMPORTANCE_VALUES)
    _validate_enum("thesis_impact", item.thesis_impact, THESIS_IMPACT_VALUES)


def get_by_id(conn: sqlite3.Connection, wid: int) -> Optional[WatchlistItem]:
    row = conn.execute("SELECT * FROM watchlist WHERE id=?", (wid,)).fetchone()
    return _row_to_item(row) if row else None


def get_by_key(conn: sqlite3.Connection, thesis: str, item: str) -> Optional[WatchlistItem]:
    row = conn.execute(
        "SELECT * FROM watchlist WHERE thesis=? AND item=?", (thesis, item)
    ).fetchone()
    return _row_to_item(row) if row else None


def find(
    conn: sqlite3.Connection,
    thesis: Optional[str] = None,
    status: Optional[str] = None,
    importance: Optional[str] = None,
    ticker: Optional[str] = None,
    text: Optional[str] = None,
    limit: int = 200,
) -> list[WatchlistItem]:
    where: list[str] = []
    params: list = []
    if thesis:
        where.append("thesis = ?")
        params.append(thesis)
    if status:
        where.append("status = ?")
        params.append(status)
    if importance:
        where.append("importance = ?")
        params.append(importance)
    if ticker:
        where.append("(tickers LIKE ? OR tickers LIKE ?)")
        params.extend([f'%"{ticker}"%', f"%{ticker}%"])
    if text:
        like = f"%{text}%"
        where.append(
            "(item LIKE ? OR trigger_criteria LIKE ? OR resolution_note LIKE ? OR thesis LIKE ?)"
        )
        params.extend([like, like, like, like])
    sql = "SELECT * FROM watchlist"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY CASE status WHEN 'open' THEN 0 WHEN 'partial' THEN 1 ELSE 2 END,"
    sql += " CASE importance WHEN 'high' THEN 0 WHEN 'mid' THEN 1 WHEN 'low' THEN 2 ELSE 3 END,"
    sql += " last_updated DESC LIMIT ?"
    params.append(limit)
    rows = conn.execute(sql, params).fetchall()
    return [_row_to_item(r) for r in rows]


def add(conn: sqlite3.Connection, item: WatchlistItem, *, source: Optional[str] = None) -> int:
    """신규 등록. 같은 (thesis, item)이 있으면 IntegrityError — 호출측이 upsert 사용."""
    _validate_item(item)
    now = _now()
    item.created_at = item.created_at or now
    item.last_updated = now
    row = item.to_row()
    cur = conn.execute(
        """
        INSERT INTO watchlist
            (thesis, item, trigger_criteria, importance, status, tickers,
             resolution_note, thesis_impact, created_at, last_updated)
        VALUES
            (:thesis, :item, :trigger_criteria, :importance, :status, :tickers,
             :resolution_note, :thesis_impact, :created_at, :last_updated)
        """,
        {**row, "created_at": item.created_at, "last_updated": item.last_updated},
    )
    wid = cur.lastrowid
    conn.execute(
        """
        INSERT INTO watchlist_history (watchlist_id, field, old_value, new_value, changed_at, note)
        VALUES (?, 'created', NULL, ?, ?, ?)
        """,
        (wid, item.status, now, source),
    )
    return wid


def update(
    conn: sqlite3.Connection,
    wid: int,
    *,
    thesis: Optional[str] = None,
    item: Optional[str] = None,
    trigger_criteria: Optional[str] = None,
    importance: Optional[str] = None,
    status: Optional[str] = None,
    tickers: Optional[list[str]] = None,
    resolution_note: Optional[str] = None,
    thesis_impact: Optional[str] = None,
    source: Optional[str] = None,
) -> WatchlistItem:
    """변경된 필드만 UPDATE + watchlist_history 기록."""
    current = get_by_id(conn, wid)
    if not current:
        raise KeyError(f"watchlist id {wid} not found")
    _validate_enum("status", status, STATUS_VALUES)
    _validate_enum("importance", importance, IMPORTANCE_VALUES)
    _validate_enum("thesis_impact", thesis_impact, THESIS_IMPACT_VALUES)

    changes: list[tuple[str, Optional[str], Optional[str]]] = []
    new_values: dict = {}

    def _diff(field_name: str, new_value, old_value, *, serialize=False):
        if new_value is None:
            return
        if serialize:
            old_repr = json.dumps(old_value, ensure_ascii=False) if old_value else None
            new_repr = json.dumps(new_value, ensure_ascii=False) if new_value else None
            db_value = new_repr
        else:
            old_repr = None if old_value is None else str(old_value)
            new_repr = None if new_value is None else str(new_value)
            db_value = new_value
        if old_repr == new_repr:
            return
        changes.append((field_name, old_repr, new_repr))
        new_values[field_name] = db_value

    _diff("thesis", thesis, current.thesis)
    _diff("item", item, current.item)
    _diff("trigger_criteria", trigger_criteria, current.trigger_criteria)
    _diff("importance", importance, current.importance)
    _diff("status", status, current.status)
    _diff("tickers", tickers, current.tickers, serialize=True)
    _diff("resolution_note", resolution_note, current.resolution_note)
    _diff("thesis_impact", thesis_impact, current.thesis_impact)

    if not changes:
        return current

    now = _now()
    set_clause = ", ".join(f"{k}=:{k}" for k in new_values)
    set_clause += ", last_updated=:last_updated"
    params = {**new_values, "last_updated": now, "id": wid}
    conn.execute(f"UPDATE watchlist SET {set_clause} WHERE id=:id", params)
    for fname, old_v, new_v in changes:
        conn.execute(
            """
            INSERT INTO watchlist_history (watchlist_id, field, old_value, new_value, changed_at, note)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (wid, fname, old_v, new_v, now, source),
        )
    refreshed = get_by_id(conn, wid)
    assert refreshed is not None
    return refreshed


def upsert(
    conn: sqlite3.Connection, spec: WatchlistItem, *, source: Optional[str] = None
) -> tuple[int, str]:
    """(thesis, item) 기준 upsert. 반환: (id, "created" | "updated" | "noop")."""
    existing = get_by_key(conn, spec.thesis, spec.item)
    if not existing:
        wid = add(conn, spec, source=source)
        return wid, "created"
    refreshed = update(
        conn,
        existing.id,  # type: ignore[arg-type]
        trigger_criteria=spec.trigger_criteria,
        importance=spec.importance,
        status=spec.status if spec.status != "open" or existing.status == "open" else spec.status,
        tickers=spec.tickers if spec.tickers else None,
        resolution_note=spec.resolution_note,
        thesis_impact=spec.thesis_impact,
        source=source,
    )
    action = "updated" if refreshed.last_updated != existing.last_updated else "noop"
    return existing.id, action  # type: ignore[return-value]


def remove(conn: sqlite3.Connection, wid: int) -> bool:
    cur = conn.execute("DELETE FROM watchlist WHERE id=?", (wid,))
    return cur.rowcount > 0


def history(conn: sqlite3.Connection, wid: int) -> list[HistoryRow]:
    rows = conn.execute(
        "SELECT * FROM watchlist_history WHERE watchlist_id=? ORDER BY id ASC", (wid,)
    ).fetchall()
    return [
        HistoryRow(
            id=r["id"],
            watchlist_id=r["watchlist_id"],
            field=r["field"],
            old_value=r["old_value"],
            new_value=r["new_value"],
            changed_at=r["changed_at"],
            note=r["note"],
        )
        for r in rows
    ]


def add_thesis_update(
    conn: sqlite3.Connection,
    thesis: str,
    *,
    item: Optional[str] = None,
    before_text: Optional[str] = None,
    after_text: Optional[str] = None,
    source: Optional[str] = None,
) -> int:
    if not thesis:
        raise ValueError("thesis is required")
    if before_text is None and after_text is None:
        raise ValueError("before_text or after_text required")
    now = _now()
    cur = conn.execute(
        """
        INSERT INTO thesis_updates (thesis, item, before_text, after_text, source, changed_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (thesis, item, before_text, after_text, source, now),
    )
    return cur.lastrowid


def list_thesis_updates(
    conn: sqlite3.Connection,
    thesis: Optional[str] = None,
    item: Optional[str] = None,
    limit: int = 200,
) -> list[ThesisUpdate]:
    where: list[str] = []
    params: list = []
    if thesis:
        where.append("thesis=?")
        params.append(thesis)
    if item:
        where.append("item=?")
        params.append(item)
    sql = "SELECT * FROM thesis_updates"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY changed_at DESC, id DESC LIMIT ?"
    params.append(limit)
    rows = conn.execute(sql, params).fetchall()
    return [
        ThesisUpdate(
            id=r["id"],
            thesis=r["thesis"],
            item=r["item"],
            before_text=r["before_text"],
            after_text=r["after_text"],
            source=r["source"],
            changed_at=r["changed_at"],
        )
        for r in rows
    ]
