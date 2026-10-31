# -*- coding: utf-8 -*-
"""Bounded FTS candidates, Python lexical scoring, and a fail-open prompt hook."""
from __future__ import annotations

import json
import math
import re

from ._config import LEDGER_DB, utf8_stdout
from . import _ledger

FTS_CANDIDATES = 300
# Calibrated by _selftest_ledger: near duplicates pass, incidental single terms
# and unrelated prompts fail. Use absolute coverage, never best-hit scaling.
HOOK_MIN = 0.5      # 실제 장부(백필 165건)에 맞춘 값 — 0.65 는 «Alphabet capex guidance»(0.53)를 놓쳤다(2026-10-31)
_WORD = re.compile(r"\w+", re.UNICODE)


def _grams(text):
    out = set()
    for word in _WORD.findall((text or "").lower()):
        if word.isascii() or len(word) == 1:
            out.add(word)
        else:
            out.update(word[i:i + 2] for i in range(len(word) - 1))
    return out


def _cover(want, have):
    return len(want & have) / len(want) if want else 0.0


def _candidates(con, text):
    words = list(dict.fromkeys(_WORD.findall(text.lower())))[:64]
    # Korean suffix changes still enter the candidate set; final bigram scoring
    # distinguishes actual matches. Parameters/quoted tokens escape FTS syntax.
    keys = list(dict.fromkeys(words + [w[:2] for w in words if not w.isascii() and len(w) > 2]))
    if not keys:
        return []
    expr = " OR ".join('"' + w.replace('"', '""') + '"*' for w in keys)
    return [r[0] for r in con.execute(
        "SELECT qid FROM q_fts WHERE q_fts MATCH ? ORDER BY bm25(q_fts),qid LIMIT ?",
        (expr, FTS_CANDIDATES))]


def method_summary(con, hits):
    ids = list(dict.fromkeys(h["id"] if isinstance(h, dict) else h for h in hits))
    if not ids:
        return {"methods": [], "best": [], "worst": [], "single_method_questions": 0}
    methods, alive = {}, {}
    for qid in ids:
        q = _ledger.get(con, qid)
        keys = {b["k"] for b in _ledger._branches(q)}
        outcome = con.execute("SELECT fired FROM outcomes WHERE question=?", (qid,)).fetchone()
        fired = outcome[0] if outcome else None
        for e in con.execute("SELECT * FROM evidence WHERE question=? ORDER BY id", (qid,)):
            m = methods.setdefault(e["method"], {"method": e["method"], "uses": 0, "hits": 0, "misses": 0})
            m["uses"] += 1
            if e["dead"] is None:
                alive.setdefault(qid, set()).add(e["method"])
            if fired in keys and e["dead"] is None and e["weight"] > 0 and e["supports"]:
                m["hits" if e["supports"] == fired else "misses"] += 1
    rows = sorted(methods.values(), key=lambda r: (-r["uses"], r["method"]))
    best = sorted((m for m in rows if m["hits"] > m["misses"]),
                  key=lambda m: (-m["hits"] / (m["hits"] + m["misses"]), -m["hits"], m["method"]))
    worst = sorted((m for m in rows if m["misses"] > m["hits"]),
                   key=lambda m: (-m["misses"] / (m["hits"] + m["misses"]), -m["misses"], m["method"]))
    return {"methods": rows, "best": best, "worst": worst,
            "single_method_questions": sum(len(ms) == 1 for ms in alive.values())}


def find(con, text, limit=8, vec_scores=None):
    """Return {hits, method_summary}; lexical scores are absolute values in [0,1].

    Optional precomputed cosine scores supply up to 300 additional candidates.
    No embedding or third-party import takes place here (including in hooks).
    """
    limit = max(0, min(int(limit), 300))
    if not limit:
        return {"hits": [], "method_summary": method_summary(con, [])}
    want = _grams(text)
    candidates = _candidates(con, text)
    if vec_scores is not None:
        semantic_ids = sorted(vec_scores, key=lambda k: (-float(vec_scores[k]), k))[:300]
        candidates = list(dict.fromkeys(candidates + semantic_ids))
    hits = []
    for qid in candidates:
        row = con.execute("""SELECT q.*,o.fired,f.words FROM questions q
            LEFT JOIN outcomes o ON o.question=q.id LEFT JOIN q_fts f ON f.qid=q.id
            WHERE q.id=? LIMIT 1""", (qid,)).fetchone()
        if row is None:
            continue
        head = _grams(row["title"])
        body = _grams(row["words"] or "")
        lexical = max(0.85 * _cover(want, head) + 0.15 * _cover(head, want),
                      0.8 * _cover(want, body)) if want else 0.0
        semantic = 0.0
        if vec_scores is not None:
            semantic = float(vec_scores.get(qid, 0.0))
            semantic = max(-1.0, min(1.0, semantic)) if math.isfinite(semantic) else 0.0
        score = 0.5 * lexical + 0.5 * semantic if vec_scores is not None else lexical
        if score <= 0:
            continue
        hits.append({"id": qid, "legacy": row["legacy"], "title": row["title"],
                     "status": row["status"], "fired": row["fired"], "score": score,
                     "lexical": lexical, "semantic": semantic})
    hits.sort(key=lambda h: (-h["score"], int(h["id"][1:]), h["id"]))
    hits = hits[:limit]
    return {"hits": hits, "method_summary": method_summary(con, hits)}


def _short(text, n=90):
    text = " ".join(str(text or "").split())
    return text if len(text) <= n else text[:n - 1] + "…"


def _method_line(rows):
    return " · ".join(f"{_short(m['method'], 45)} ({m['hits']}/{m['hits'] + m['misses']} 맞음)"
                      for m in rows[:2]) or "없음"


def summary_lines(summary):
    return ["잘 맞던 방법: " + _method_line(summary["best"]),
            "잘 틀리던 방법: " + _method_line(summary["worst"]),
            f"🎲 방법이 하나뿐인 물음 {summary['single_method_questions']}건"]


def format_find(result):
    lines = [f"비슷한 지난 물음 {len(result['hits'])}건"]
    for h in result["hits"]:
        lines.append(f"{h['id']} legacy={h['legacy'] or '-'} | {h['title']} | {h['status']} | fired={h['fired'] or '-'}")
    lines.append("METHOD SUMMARY (uses / hits / misses)")
    for m in result["method_summary"]["methods"]:
        lines.append(f"{m['method']} | {m['uses']} / {m['hits']} / {m['misses']}")
    return "\n".join(lines + summary_lines(result["method_summary"]))


def hook_prompt(stdin_text):
    """Read-only and fail-open: any malformed input/DB/output error returns 0."""
    try:
        utf8_stdout()
        event = json.loads(stdin_text)
        prompt = event.get("prompt") if isinstance(event, dict) else None
        if not isinstance(prompt, str) or len(prompt.strip()) < 8:
            return 0
        # Refuse creation and writes; a busy ledger cannot hold the hook for 5 s.
        con = _ledger.connect(LEDGER_DB, readonly=True)
        try:
            con.execute("PRAGMA busy_timeout=100")
            result = find(con, prompt[:8000], limit=2)
            hits = [h for h in result["hits"] if h["score"] >= HOOK_MIN]
            summary = method_summary(con, hits)
        finally:
            con.close()
        if not hits:
            return 0
        lines = ["비슷한 물음과 방법 — show <Q번호>로 근거 확인"]
        lines += [f"{h['id']} {_short(h['title'])} [{h['status']}; fired={h['fired'] or '-'}]" for h in hits]
        lines += summary_lines(summary)
        print("\n".join("📒 module_lens — " + line for line in lines[:6]))
    except Exception:
        pass
    return 0
