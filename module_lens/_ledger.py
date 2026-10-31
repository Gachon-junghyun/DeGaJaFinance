# -*- coding: utf-8 -*-
"""SQLite source of record for questions, evidence, and outcomes (stdlib only)."""
from __future__ import annotations

from contextlib import contextmanager
from datetime import date, datetime
import json
import math
from pathlib import Path
import re
import sqlite3

from ._config import EXPORT_DIR, FLOW_CAP, FLOW_KINDS, LEDGER_DB

KINDS = ("flow", "estimates", "options", "macro", "filing", "news", "report",
         "price", "positioning", "other")
STATUSES = ("open", "scored", "void", "ambiguous", "expired")
_WORD = re.compile(r"\w+", re.UNICODE)
_DDL = """
CREATE TABLE IF NOT EXISTS questions (
 id TEXT PRIMARY KEY, legacy TEXT, asked_at TEXT NOT NULL, desk TEXT, market TEXT,
 subject TEXT, title TEXT NOT NULL, settle TEXT, observable TEXT, branches TEXT,
 status TEXT NOT NULL DEFAULT 'open', note TEXT, link TEXT,
 backfilled INTEGER NOT NULL DEFAULT 0, created TEXT NOT NULL, updated TEXT NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS questions_legacy ON questions(legacy) WHERE legacy IS NOT NULL;
CREATE TABLE IF NOT EXISTS evidence (
 id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT NOT NULL, method TEXT NOT NULL,
 kind TEXT NOT NULL, key TEXT, reading TEXT, supports TEXT,
 weight REAL NOT NULL DEFAULT 0, impact REAL, dead TEXT, note TEXT, link TEXT,
 backfilled INTEGER NOT NULL DEFAULT 0, at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS evidence_q ON evidence(question);
CREATE TABLE IF NOT EXISTS outcomes (
 question TEXT PRIMARY KEY, fired TEXT NOT NULL, value TEXT, scored_at TEXT NOT NULL,
 scorer TEXT NOT NULL, price_1d REAL, price_3d REAL, price_5d REAL, price_20d REAL,
 brier REAL, note TEXT, link TEXT
);
CREATE VIRTUAL TABLE IF NOT EXISTS q_fts USING fts5(qid UNINDEXED, words, tokenize='unicode61');
CREATE TABLE IF NOT EXISTS q_vec (qid TEXT PRIMARY KEY, vec BLOB, model TEXT);
CREATE TABLE IF NOT EXISTS credit (
 level TEXT, name TEXT, n INTEGER, hits INTEGER, misses INTEGER, wsum REAL,
 cred REAL, beta_mean REAL, lo80 REAL, hi80 REAL, updated TEXT, PRIMARY KEY(level, name)
);
CREATE TABLE IF NOT EXISTS impact (
 kind TEXT, key TEXT, mult REAL, n INTEGER, src TEXT, PRIMARY KEY(kind, key)
);
"""


class LedgerError(ValueError):
    """Invalid ledger operation, reported by the CLI as one line and exit 2."""


def connect(path=None, *, readonly=False):
    """Open a ledger (default LEDGER_DB), with a five-second busy timeout."""
    path = LEDGER_DB if path is None else path
    if readonly:
        uri = Path(path).resolve().as_uri() + "?mode=ro"
        con = sqlite3.connect(uri, uri=True, timeout=5)
    else:
        if str(path) != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        con = sqlite3.connect(path, timeout=5)
    con.row_factory = sqlite3.Row
    if not readonly:
        try:
            con.executescript(_DDL)
        except BaseException:
            con.close()
            raise
    return con


@contextmanager
def _atomic(con):
    """Serialize id allocation and validation; compose with caller transactions."""
    nested = con.in_transaction
    con.execute("SAVEPOINT lens_write" if nested else "BEGIN IMMEDIATE")
    try:
        yield
    except BaseException:
        if nested:
            con.execute("ROLLBACK TO lens_write")
            con.execute("RELEASE lens_write")
        else:
            con.rollback()
        raise
    else:
        if nested:
            con.execute("RELEASE lens_write")
        else:
            con.commit()


def _now():
    return datetime.now().astimezone().isoformat(timespec="microseconds")


@contextmanager
def _snapshot(con):
    """A read snapshot must not commit an enclosing caller's transaction."""
    owned = not con.in_transaction
    if owned:
        con.execute("BEGIN")
    try:
        yield
    finally:
        if owned:
            con.rollback()


def _json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def get(con, qid):
    row = con.execute("SELECT * FROM questions WHERE id=?", (qid,)).fetchone()
    if row is None:
        raise LedgerError(f"question not found: {qid}")
    return dict(row)


def _next_id(con):
    nums = [int(r[0][1:]) for r in con.execute("SELECT id FROM questions")
            if re.fullmatch(r"Q[0-9]+", r[0])]
    return "Q" + str(max(nums, default=0) + 1)


def _day(value):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except ValueError as exc:
        raise LedgerError("date must be YYYY-MM-DD") from exc


def _settle(value):
    if value is None:
        return
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}(?: (?:AMC|BMO|[0-2]\d:[0-5]\d))?", value):
        raise LedgerError("settle must be YYYY-MM-DD [AMC|BMO|HH:MM]")
    _day(value[:10])
    if len(value) > 11 and ":" in value[11:] and int(value[11:13]) > 23:
        raise LedgerError("settle hour must be 00..23")


def _observable(value):
    if value is None:
        return
    if value.startswith("text:") and value[5:].strip():
        return
    if re.fullmatch(r"(?:px|pxx|fred):[^:\s]+:[1-9][0-9]*", value):
        return
    raise LedgerError("observable must be px:TICKER:h, pxx:TICKER:h, fred:SERIES:h or text:description")


def _number(value, label, *, percent=False):
    try:
        n = float(value)
    except (ValueError, TypeError) as exc:
        raise LedgerError(f"{label} must be numeric") from exc
    if not math.isfinite(n) or (percent and not 0 <= n <= 100):
        raise LedgerError(f"{label} must be finite" + (" and 0..100" if percent else ""))
    return n


def _optional_number(value):
    return None if value is None or str(value).lower() in ("", "null", "none", "?") else _number(value, "branch bound")


def parse_branch(text):
    """Parse k:p:condition[:lo:hi]; numeric trailing bounds are optional."""
    parts = text.split(":", 2)
    if len(parts) != 3:
        raise LedgerError("branch must be K:P:condition[:lo:hi]")
    k, p, cond = parts
    lo = hi = None
    tail = cond.rsplit(":", 2)
    if len(tail) == 3:
        try:
            lo, hi = _optional_number(tail[1]), _optional_number(tail[2])
        except LedgerError:
            lo = hi = None  # literal condition unless both trailing bounds parse
        else:
            cond = tail[0]
    return {"k": k, "p": _optional_number(p), "cond": cond, "lo": lo, "hi": hi}


def validate_branches(branches):
    if not isinstance(branches, list) or not branches:
        raise LedgerError("at least one branch is required")
    out, keys = [], set()
    for raw in branches:
        b = parse_branch(raw) if isinstance(raw, str) else dict(raw)
        k = b.get("k", "")
        if not re.fullmatch(r"[A-Z]+", k) or k in keys or k in ("VOID", "AMBIGUOUS"):
            raise LedgerError("branch keys must be unique uppercase letters (reserved outcomes excluded)")
        keys.add(k)
        p = b.get("p")
        p = None if p is None else _number(p, "branch p", percent=True)
        lo, hi = _optional_number(b.get("lo")), _optional_number(b.get("hi"))
        if lo is not None and hi is not None and lo >= hi:
            raise LedgerError("branch lo must be less than hi")
        out.append({"k": k, "cond": b.get("cond", ""), "p": p, "lo": lo, "hi": hi})
    if all(b["p"] is not None for b in out) and abs(sum(b["p"] for b in out) - 100) > 0.5:
        raise LedgerError("branch p sum must be 100 (+/-0.5)")
    return out


def _branches(q):
    return json.loads(q["branches"]) if q["branches"] else []


def _index(con, qid):
    q = get(con, qid)
    fields = [q["title"], q["subject"], q["legacy"], (q["note"] or "")[:2000]]
    for row in con.execute("SELECT method,key,reading FROM evidence WHERE question=? ORDER BY id", (qid,)):
        fields.extend(row)
    words = " ".join(_WORD.findall(" ".join(str(x) for x in fields if x is not None).lower()))
    con.execute("DELETE FROM q_fts WHERE qid=?", (qid,))
    con.execute("INSERT INTO q_fts(qid,words) VALUES(?,?)", (qid, words))


def reindex(con):
    """Rebuild the lexical index. Vectors remain owned by the integrator."""
    with _atomic(con):
        con.execute("DELETE FROM q_fts")
        ids = [r[0] for r in con.execute("SELECT id FROM questions")]
        for qid in ids:
            _index(con, qid)
    return len(ids)


def ask(con, title, *, subject=None, market=None, desk=None, settle=None,
        observable=None, note=None, legacy=None, asked_at=None, link=None, backfilled=0):
    if not title.strip():
        raise LedgerError("title must not be empty")
    _settle(settle)
    _observable(observable)
    now = _now()
    asked_at = asked_at or now
    try:
        stamp = datetime.fromisoformat(asked_at)
        if stamp.utcoffset() is None:
            raise ValueError("offset missing")
    except ValueError as exc:
        raise LedgerError("asked_at must be ISO-8601 with an offset") from exc
    with _atomic(con):
        if legacy is not None and con.execute("SELECT 1 FROM questions WHERE legacy=?", (legacy,)).fetchone():
            raise LedgerError(f"legacy already exists: {legacy}")
        qid = _next_id(con)
        con.execute("""INSERT INTO questions
            (id,legacy,asked_at,desk,market,subject,title,settle,observable,note,link,backfilled,created,updated)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (qid, legacy, asked_at, desk, market, subject, title, settle, observable, note, link,
             int(bool(backfilled)), now, now))
        _index(con, qid)
    return get(con, qid)


def ev(con, qid, method, reading, *, kind, key=None, supports="", weight=0,
       link=None, note=None, dead=None, backfilled=0, at=None, impact=None):
    if kind not in KINDS:
        raise LedgerError("kind must be one of " + ", ".join(KINDS))
    if not method.strip():
        raise LedgerError("method must not be empty")
    if key and not re.fullmatch(r"[a-z][a-z0-9_]*", key):
        raise LedgerError("key must be snake_case")
    weight = _number(weight, "weight", percent=True)
    if dead is not None and weight > 0:
        raise LedgerError("dead evidence must have weight 0")
    with _atomic(con):
        get(con, qid)
        if con.execute("SELECT 1 FROM outcomes WHERE question=?", (qid,)).fetchone():
            raise LedgerError("ev rejected: question already has an outcome")
        eid = con.execute("""INSERT INTO evidence
            (question,method,kind,key,reading,supports,weight,impact,dead,note,link,backfilled,at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (qid, method, kind, key, reading, supports or "", weight, impact, dead, note, link,
             int(bool(backfilled)), at or _now())).lastrowid
        con.execute("UPDATE questions SET updated=? WHERE id=?", (_now(), qid))
        _index(con, qid)
    return dict(con.execute("SELECT * FROM evidence WHERE id=?", (eid,)).fetchone())


def parse_weights(weights):
    if isinstance(weights, str):
        out = {}
        for part in weights.split(","):
            pair = part.strip().split("=")
            if len(pair) != 2 or not re.fullmatch(r"e?[1-9][0-9]*", pair[0]):
                raise LedgerError("weights must be e3=30,e4=70")
            eid = int(pair[0].lstrip("e"))
            if eid in out:
                raise LedgerError("duplicate evidence id in weights")
            out[eid] = _number(pair[1], "weight", percent=True)
        return out
    return {int(str(k).lstrip("e")): _number(v, "weight", percent=True) for k, v in weights.items()}


def think(con, qid, branches, *, weights=None, today=None):
    branches = validate_branches(branches)
    with _atomic(con):
        q = get(con, qid)
        if con.execute("SELECT 1 FROM outcomes WHERE question=?", (qid,)).fetchone():
            # 판정 뒤에 확률·비중을 고치면 역전파가 사후에 맞춘 비중으로 배운다(검토 R, 2026-10-31)
            raise LedgerError("think rejected: question already has an outcome")
        if q["settle"] and not q["backfilled"] and _day(today or date.today()) >= _day(q["settle"][:10]):
            raise LedgerError("think rejected: now >= settle date")
        rows = [dict(r) for r in con.execute("SELECT * FROM evidence WHERE question=? ORDER BY id", (qid,))]
        alive = [r for r in rows if r["dead"] is None]
        if not alive:
            raise LedgerError("think requires at least one alive evidence row")
        byid = {r["id"]: r for r in rows}
        if weights is not None:
            updates = parse_weights(weights)
            for eid, weight in updates.items():
                if eid not in byid:
                    raise LedgerError(f"weights evidence e{eid} is not from {qid}")
                byid[eid]["weight"] = weight
        elif abs(sum(r["weight"] for r in alive) - 100) > 0.5:
            for r in alive:
                r["weight"] = 100 / len(alive)
        if any(r["dead"] is not None and r["weight"] > 0 for r in rows):
            raise LedgerError("dead evidence must have weight 0")
        if abs(sum(r["weight"] for r in alive) - 100) > 0.5:
            raise LedgerError("alive weights must sum to 100 (+/-0.5)")
        flow = sum(r["weight"] for r in alive if r["kind"] in FLOW_KINDS)
        if not q["backfilled"] and flow > FLOW_CAP + 0.5:
            raise LedgerError(f"flow+positioning weights {flow:g} exceed cap {FLOW_CAP:g}")
        keys = {b["k"] for b in branches}
        if any(r["supports"] and r["supports"] not in keys for r in alive):
            raise LedgerError("evidence supports must name a branch")
        con.executemany("UPDATE evidence SET weight=? WHERE id=?", [(r["weight"], r["id"]) for r in rows])
        con.execute("UPDATE questions SET branches=?,updated=? WHERE id=?", (_json(branches), _now(), qid))
    return get(con, qid)


def resolve(con, qid, fired, *, value=None, scorer=None, note=None, link=None):
    with _atomic(con):
        q = get(con, qid)
        if fired not in {b["k"] for b in _branches(q)} | {"VOID", "AMBIGUOUS"}:
            raise LedgerError("fired must be a branch key, VOID or AMBIGUOUS")
        status = {"VOID": "void", "AMBIGUOUS": "ambiguous"}.get(fired, "scored")
        con.execute("""INSERT INTO outcomes(question,fired,value,scored_at,scorer,note,link)
            VALUES(?,?,?,?,?,?,?) ON CONFLICT(question) DO UPDATE SET
            fired=excluded.fired,value=excluded.value,scored_at=excluded.scored_at,scorer=excluded.scorer,
            note=excluded.note,link=excluded.link,price_1d=NULL,price_3d=NULL,price_5d=NULL,price_20d=NULL,brier=NULL""",
            (qid, fired, value, _now(), scorer or q["desk"] or "human", note, link))
        con.execute("UPDATE questions SET status=?,updated=? WHERE id=?", (status, _now(), qid))
        try:
            from ._score import fill_outcome
        except ImportError:
            pass
        else:
            fill_outcome(con, qid)
    return dict(con.execute("SELECT * FROM outcomes WHERE question=?", (qid,)).fetchone())


def due(con, today=None):
    today = _day(today or date.today()).isoformat()
    out = []
    for row in con.execute("""SELECT * FROM questions WHERE status='open' AND settle IS NOT NULL
            AND substr(settle,1,10)<=? ORDER BY settle,asked_at,CAST(substr(id,2) AS INTEGER)""", (today,)):
        q = dict(row)
        q["form"] = "auto" if (q["observable"] or "").split(":", 1)[0] in ("px", "pxx", "fred") else "text"
        out.append(q)
    return out


def show(con, qid):
    q = get(con, qid)
    q["branches"] = _branches(q)
    rows = [dict(r) for r in con.execute("SELECT * FROM evidence WHERE question=? ORDER BY id", (qid,))]
    learned = bool(con.execute("SELECT 1 FROM credit LIMIT 1").fetchone())
    for row in rows:
        if learned:
            c = con.execute("SELECT cred,beta_mean FROM credit WHERE level='method' AND name=?", (row["method"],)).fetchone()
            row.update(cred=c[0] if c else None, beta_mean=c[1] if c else None)
    outcome = con.execute("SELECT * FROM outcomes WHERE question=?", (qid,)).fetchone()
    return {"question": q, "evidence": rows, "outcome": dict(outcome) if outcome else None, "has_credit": learned}


def export_jsonl(con, directory=None):
    """Export only source tables, preserving ids/timestamps and canonical bytes."""
    dest = Path(EXPORT_DIR if directory is None else directory)
    dest.mkdir(parents=True, exist_ok=True)
    specs = (("questions", "question", "CAST(substr(id,2) AS INTEGER),id"),
             ("evidence", "evidence", "id"),
             ("outcomes", "outcome", "CAST(substr(question,2) AS INTEGER),question"))
    counts = {}
    with _snapshot(con):  # one read snapshot for all three files
        legacy = {r["id"]: r["legacy"] for r in con.execute("SELECT id,legacy FROM questions")}
        for table, kind, order in specs:
            count = 0
            with (dest / (table + ".jsonl")).open("w", encoding="utf-8", newline="\n") as stream:
                for row in con.execute(f"SELECT * FROM {table} ORDER BY {order}"):
                    record = dict(row)
                    record["type"] = kind
                    if kind == "question":
                        branches = _branches(record)
                        record["branches"] = validate_branches(branches) if branches else None
                    else:
                        record["legacy"] = legacy[record["question"]]
                    stream.write(_json(record) + "\n")
                    count += 1
            counts[table] = count
    return counts


def _insert_record(con, table, record):
    columns = [r[1] for r in con.execute(f"PRAGMA table_info({table})")]
    data = {k: v for k, v in record.items() if k in columns}
    primary = "question" if table == "outcomes" else "id"
    if primary in data:
        old = con.execute(f"SELECT * FROM {table} WHERE {primary}=?", (data[primary],)).fetchone()
        if old:
            if all(old[k] == v for k, v in data.items()):
                return
            raise LedgerError(f"import conflicts with {table} {data[primary]}")
    con.execute(f"INSERT INTO {table}({','.join(data)}) VALUES({','.join('?' for _ in data)})", tuple(data.values()))


def import_jsonl(con, files):
    """Import exported or legacy-keyed records in dependency order, atomically."""
    if isinstance(files, (str, Path)):
        files = [files]
    records = []
    for filename in files:
        with Path(filename).open(encoding="utf-8") as stream:
            for n, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                except ValueError as exc:
                    raise LedgerError(f"invalid JSON at {filename}:{n}") from exc
                if not isinstance(record, dict) or record.get("type") not in ("question", "evidence", "outcome"):
                    raise LedgerError(f"invalid record type at {filename}:{n}")
                records.append(record)
    counts = {"questions": 0, "evidence": 0, "outcomes": 0}
    explicit_status = set()
    now = _now()
    with _atomic(con):
        for original in records:
            if original["type"] != "question":
                continue
            r = dict(original)
            old = con.execute("SELECT id FROM questions WHERE legacy=?", (r.get("legacy"),)).fetchone()
            qid = r.get("id") or (old[0] if old else _next_id(con))
            if not re.fullmatch(r"Q[1-9][0-9]*", qid):
                raise LedgerError("import question id must be Q<number>")
            if old and old[0] != qid:
                raise LedgerError("legacy maps to another question id")
            r["id"] = qid
            if "status" in r:
                explicit_status.add(qid)
            if not str(r.get("title") or "").strip():
                raise LedgerError("import question needs a title")
            _settle(r.get("settle"))
            _observable(r.get("observable"))
            b = r.get("branches")
            if isinstance(b, str):
                b = json.loads(b)
            r["branches"] = _json(validate_branches(b)) if b else None
            r.setdefault("asked_at", now)
            stamp = datetime.fromisoformat(r["asked_at"])
            if stamp.utcoffset() is None:
                raise LedgerError("asked_at must be ISO-8601 with an offset")
            r.setdefault("created", r["asked_at"])
            r.setdefault("updated", r["created"])
            r.setdefault("backfilled", 0)
            if r.get("status", "open") not in STATUSES:
                raise LedgerError("invalid question status")
            _insert_record(con, "questions", r)
            counts["questions"] += 1
        for kind, table in (("evidence", "evidence"), ("outcome", "outcomes")):
            for original in records:
                if original["type"] != kind:
                    continue
                r = dict(original)
                old = con.execute("SELECT id FROM questions WHERE legacy=?", (r.get("legacy"),)).fetchone()
                qid = r.get("question") or (old[0] if old else None)
                q = get(con, qid)
                if r.get("legacy") is not None and r["legacy"] != q["legacy"]:
                    raise LedgerError("record legacy and question disagree")
                r["question"] = qid
                if kind == "evidence":
                    if r.get("kind") not in KINDS or not str(r.get("method") or "").strip():
                        raise LedgerError("import evidence needs a valid kind and method")
                    r["weight"] = _number(r.get("weight", 0), "weight", percent=True)
                    if r.get("dead") is not None and r["weight"] > 0:
                        raise LedgerError("dead evidence must have weight 0")
                    r.setdefault("supports", "")
                    r.setdefault("at", q["asked_at"])
                    r.setdefault("backfilled", q["backfilled"])
                else:
                    if r.get("fired") not in {b["k"] for b in _branches(q)} | {"VOID", "AMBIGUOUS"}:
                        raise LedgerError("fired must be a branch key, VOID or AMBIGUOUS")
                    r.setdefault("scored_at", now)
                    r.setdefault("scorer", "backfill" if q["backfilled"] else "human")
                _insert_record(con, table, r)
                if kind == "outcome" and qid not in explicit_status:
                    status = {"VOID": "void", "AMBIGUOUS": "ambiguous"}.get(r["fired"], "scored")
                    con.execute("UPDATE questions SET status=? WHERE id=?", (status, qid))
                counts[table] += 1
        for row in con.execute("SELECT id FROM questions").fetchall():
            _index(con, row[0])
    return counts
