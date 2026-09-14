# -*- coding: utf-8 -*-
"""근거 색인 저장·조회 (SQLite). **파생물** — 지우고 `build` 하면 md 에서 그대로 복원된다.

FTS5 를 쓰지 않는 이유는 `_config` 상단에 적혀 있다(2자 한글 0건 + 코퍼스가 작다).
조회는 `instr()` 부분일치 — 「수주」·「실적」 같은 2자 한글이 그대로 걸린다.
"""
from __future__ import annotations

import sqlite3
import time
from pathlib import Path

from ._config import (EVIDENCE_DB, HANDOFF_DIR, REPORT_DIR, RUNS_DIR, iter_md)
from ._harvest import harvest_ledger, harvest_refs_and_ids, harvest_report

COLS = ("cid", "family", "market", "claim", "evidence", "source", "asof", "run",
        "tag", "link", "tickers", "file", "line", "kind", "scope", "section", "raw")

SCHEMA = f"""
CREATE TABLE IF NOT EXISTS claims (
  rowid_key INTEGER PRIMARY KEY AUTOINCREMENT,
  {', '.join(c + ' TEXT' for c in COLS if c != 'line')},
  line INTEGER,
  search_text TEXT
);
CREATE INDEX IF NOT EXISTS ix_claims_cid  ON claims(cid);
CREATE INDEX IF NOT EXISTS ix_claims_kind ON claims(kind);
CREATE INDEX IF NOT EXISTS ix_claims_file ON claims(file);

CREATE TABLE IF NOT EXISTS refs (
  cid TEXT, file TEXT, line INTEGER, context TEXT
);
CREATE INDEX IF NOT EXISTS ix_refs_cid ON refs(cid);

CREATE TABLE IF NOT EXISTS occupancy (
  cid TEXT, family TEXT, num INTEGER, file TEXT, line INTEGER
);
CREATE INDEX IF NOT EXISTS ix_occ_family ON occupancy(family);

CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, v TEXT);
"""

_DECOR_CHARS = "*`_~"


def _search_text(rec: dict) -> str:
    blob = " ".join(str(rec.get(c) or "") for c in
                    ("cid", "claim", "evidence", "source", "tickers", "section"))
    return "".join(ch for ch in blob if ch not in _DECOR_CHARS).lower()


def connect(db: Path = EVIDENCE_DB) -> sqlite3.Connection:
    db.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


def build(db: Path = EVIDENCE_DB, include_runs: bool = False) -> dict:
    """md 전량 재수확 → DB 재작성. 증분 아님(전체가 2초대) — 상태를 안 들고 있으면 안 틀린다.

    `include_runs=True` 면 `llm_outputs/` 의 런 사본까지 **주장으로** 넣는다. 기본은 끔 —
    런 사본은 `handoff/` 행의 복제라 인용 카운트를 부풀린다. **ID 점유 스캔은 항상 켠다**
    (런 사본에만 있는 번호를 못 보면 next-id 가 남의 번호를 발급한다).
    """
    from module_report_tags._config import load_kr_names, load_us_tickers
    kr, us = load_kr_names(), load_us_tickers()

    t0 = time.time()
    claims: list[dict] = []
    refs: list[dict] = []
    ids: list[dict] = []
    stats = {"handoff": 0, "report": 0, "runs": 0}

    for p in iter_md(HANDOFF_DIR):
        claims += harvest_ledger(p, kr, us)
        r, i = harvest_refs_and_ids(p)
        refs += r
        ids += i
        stats["handoff"] += 1

    for p in iter_md(REPORT_DIR):
        claims += harvest_report(p, kr, us)
        r, i = harvest_refs_and_ids(p)
        refs += r
        ids += i
        stats["report"] += 1

    for p in iter_md(RUNS_DIR):
        stats["runs"] += 1
        r, i = harvest_refs_and_ids(p)
        refs += r
        ids += i
        if include_runs:
            claims += harvest_report(p, kr, us)

    con = connect(db)
    with con:
        con.execute("DELETE FROM claims")
        con.execute("DELETE FROM refs")
        con.execute("DELETE FROM occupancy")
        con.executemany(
            f"INSERT INTO claims ({', '.join(COLS)}, search_text) "
            f"VALUES ({', '.join('?' * (len(COLS) + 1))})",
            [tuple(rec.get(c, "") for c in COLS) + (_search_text(rec),) for rec in claims],
        )
        con.executemany("INSERT INTO refs (cid, file, line, context) VALUES (?,?,?,?)",
                        [(r["cid"], r["file"], r["line"], r["context"]) for r in refs])
        con.executemany("INSERT INTO occupancy (cid, family, num, file, line) VALUES (?,?,?,?,?)",
                        [(i["cid"], i["family"], i["num"], i["file"], i["line"]) for i in ids])
        con.executemany("INSERT OR REPLACE INTO meta (k, v) VALUES (?,?)", [
            ("built_at", time.strftime("%Y-%m-%dT%H:%M:%S")),
            ("include_runs", "1" if include_runs else "0"),
        ])
    out = {"claims": len(claims), "refs": len(refs), "ids": len(set(i["cid"] for i in ids)),
           "files": stats, "secs": round(time.time() - t0, 2)}
    con.close()
    return out


# ── 조회 ────────────────────────────────────────────────────────────────────
def _rows(con, sql: str, args: tuple, limit: int) -> list[sqlite3.Row]:
    return list(con.execute(sql + " LIMIT ?", args + (limit,)))


def cite(term: str, db: Path = EVIDENCE_DB, limit: int = 20, kind: str = "",
         market: str = "", tag: str = "", since: str = "") -> list[sqlite3.Row]:
    """한 단어 → 근거 행. 부분일치(2자 한글 OK). ID 를 넣으면 그 ID 를 먼저 돌려준다."""
    con = connect(db)
    q = term.strip()
    where = ["instr(search_text, ?) > 0"]
    args: list = [q.lower().strip("`*")]
    if kind:
        where.append("kind = ?")
        args.append(kind)
    if market:
        where.append("market = ?")
        args.append(market)
    if tag:
        where.append("tag = ?")
        args.append(tag)
    if since:
        where.append("asof >= ?")
        args.append(since)
    sql = ("SELECT * FROM claims WHERE " + " AND ".join(where) +
           " ORDER BY (cid = ?) DESC, (kind='ledger') DESC, asof DESC, cid DESC")
    args.append(q.upper())
    rows = _rows(con, sql, tuple(args), limit)
    con.close()
    return rows


def where_ticker(token: str, db: Path = EVIDENCE_DB, limit: int = 30) -> list[sqlite3.Row]:
    con = connect(db)
    rows = _rows(con,
                 "SELECT * FROM claims WHERE instr(',' || tickers || ',', ?) > 0 "
                 "ORDER BY (kind='ledger') DESC, asof DESC",
                 (f",{token.strip().upper() if not token.isdigit() else token.strip()},",), limit)
    con.close()
    return rows


def show(cid: str, db: Path = EVIDENCE_DB) -> tuple[list[sqlite3.Row], list[sqlite3.Row]]:
    """(정의 행, 인용 백링크). 정의가 여러 개면 전부 준다 — 중복 등록 자체가 발견이다."""
    con = connect(db)
    cid = cid.strip().upper().strip("`*")
    defs = list(con.execute("SELECT * FROM claims WHERE upper(cid) = ? ORDER BY asof", (cid,)))
    refs = list(con.execute(
        "SELECT * FROM refs WHERE upper(cid) = ? ORDER BY file, line", (cid,)))
    con.close()
    return defs, refs


def stats(db: Path = EVIDENCE_DB) -> dict:
    con = connect(db)
    g = lambda sql, a=(): con.execute(sql, a).fetchone()[0]          # noqa: E731
    out = {
        "built_at": (con.execute("SELECT v FROM meta WHERE k='built_at'").fetchone() or [""])[0],
        "claims": g("SELECT count(*) FROM claims"),
        "ledger": g("SELECT count(*) FROM claims WHERE kind='ledger'"),
        "registry": g("SELECT count(*) FROM claims WHERE kind='registry'"),
        "report": g("SELECT count(*) FROM claims WHERE kind='report'"),
        "report_line_scope": g("SELECT count(*) FROM claims WHERE kind='report' AND scope='line'"),
        "report_sec_scope": g("SELECT count(*) FROM claims WHERE kind='report' AND scope='section'"),
        "with_link": g("SELECT count(*) FROM claims WHERE link <> ''"),
        "unique_ids": g("SELECT count(DISTINCT cid) FROM occupancy"),
        "refs": g("SELECT count(*) FROM refs"),
        "families": {r[0]: r[1] for r in con.execute(
            "SELECT family, count(DISTINCT cid) FROM occupancy GROUP BY family ORDER BY family")},
    }
    con.close()
    return out
