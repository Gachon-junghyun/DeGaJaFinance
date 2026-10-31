# -*- coding: utf-8 -*-
"""Replay the ledger in settle order to test self-upgrade policies before adopting them.

At each settled question only questions settled earlier are visible (no look-ahead).
A policy rewrites the stated branch probabilities; the Brier difference against the
stated ones is bootstrapped (90% interval). The upgrade routine adopts a policy only when
the whole interval is below zero. Read-only on the ledger; deterministic (fixed seed).
"""
from __future__ import annotations

import json
import random
from collections import Counter

from module_lens._score import _rows, brier

WARM = 20


def _br(q):
    try:
        return [b for b in json.loads(q["branches"] or "[]") if b.get("p") is not None]
    except (TypeError, ValueError):
        return []


def _renorm(bs):
    t = sum(b["p"] for b in bs) or 1.0
    return [dict(b, p=b["p"] * 100.0 / t) for b in bs]


def _calib(past, k):
    bk = {}
    for q in past:
        for b in _br(q):
            s = bk.setdefault(min(int(b["p"] // 20), 4), [0.0, 0, 0])
            s[0] += b["p"] / 100.0
            s[1] += b["k"] == q["fired"]
            s[2] += 1

    def f(p):
        s = bk.get(min(int(p // 20), 4))
        if not s or s[2] < 5:
            return p
        pred, obs, n = s[0] / s[2], s[1] / s[2], s[2]
        return max(1.0, p + (obs - pred) * 100.0 * n / (n + k))
    return f


def _base_rate(past, bs, x):
    keys = [b["k"] for b in bs]
    seen = {k: sum(1 for p in past if k in [b["k"] for b in _br(p)]) for k in keys}
    hit = {k: sum(1 for p in past if p["fired"] == k) for k in keys}
    rate = {k: (1 + hit[k]) / (len(keys) + seen[k]) for k in keys}
    t = sum(rate.values())
    return [dict(b, p=(1 - x) * b["p"] + x * rate[b["k"]] / t * 100.0) for b in bs]


def _vol(prices, q):
    """종목 60일 일간 수익 표준편차(settle 전까지). 없으면 None."""
    days = sorted(prices.prices.get(q.get("subject") or "", {}))
    px = prices.prices.get(q.get("subject") or "", {})
    before = [d for d in days if d < str(q["settle"])[:10]][-61:]
    if len(before) < 30:
        return None
    r = [px[b] / px[a] - 1 for a, b in zip(before, before[1:]) if px[a] and px[b]]
    if len(r) < 20:
        return None
    m = sum(r) / len(r)
    return (sum((x - m) ** 2 for x in r) / (len(r) - 1)) ** 0.5


def _vol_rate(past, bs, q, vols, x):
    """같은 변동성 오분위의 지난 갈래 기준률로 x 만큼 당긴다 (2026-10-31 sim inflection: t +7~9)."""
    v = vols.get(q["id"])
    pv = sorted(vols[p["id"]] for p in past if vols.get(p["id"]) is not None)
    if v is None or len(pv) < 25:
        return bs
    edges = [pv[int(len(pv) * k / 5)] for k in (1, 2, 3, 4)]
    band = lambda y: sum(y >= e for e in edges)
    peers = [p for p in past if vols.get(p["id"]) is not None and band(vols[p["id"]]) == band(v)]
    return _base_rate(peers, bs, x) if len(peers) >= 5 else bs


POLICIES = {
    "calib_k5": lambda past, bs: _renorm([dict(b, p=_calib(past, 5)(b["p"])) for b in bs]),
    "calib_k20": lambda past, bs: _renorm([dict(b, p=_calib(past, 20)(b["p"])) for b in bs]),
    "base_rate_20": lambda past, bs: _base_rate(past, bs, 0.2),
    "base_rate_40": lambda past, bs: _base_rate(past, bs, 0.4),
}


def _boot(d, n=2000):
    rnd = random.Random(1)
    m = sorted(sum(rnd.choice(d) for _ in d) / len(d) for _ in range(n))
    return m[int(0.05 * n)], m[int(0.95 * n)]


def replay(con) -> dict:
    qs = _rows(con, """SELECT q.id,q.settle,q.subject,q.branches,o.fired FROM questions q JOIN outcomes o ON o.question=q.id
                       WHERE o.fired NOT IN ('VOID','AMBIGUOUS') ORDER BY q.settle,q.id""")
    qs = [q for q in qs if len(_br(q)) >= 2 and q["fired"] in [b["k"] for b in _br(q)]]
    ev = _rows(con, "SELECT question,method,supports FROM evidence WHERE dead IS NULL AND weight>0 AND supports!=''")
    fired = {q["id"]: q["fired"] for q in qs}
    support = Counter(e["supports"] for e in ev if e["question"] in fired)
    out = {"usable": len(qs), "evaluated": max(0, len(qs) - WARM),
           "fired_share": dict(Counter(q["fired"] for q in qs)), "evidence_support_share": dict(support),
           "methods_settled_5plus": sum(1 for v in Counter(e["method"] for e in ev if e["question"] in fired).values() if v >= 5),
           "policies": {}}
    if len(qs) <= WARM:
        out["note"] = f"정산 표본 {len(qs)} ≤ {WARM}: 겨룰 수 없다"
        return out
    base = [brier(_br(q), q["fired"]) for q in qs[WARM:]]
    out["stated_brier"] = sum(base) / len(base)
    from module_lens._score import _open_px, _Prices
    con_px = _open_px()
    prices = _Prices(con_px)
    if con_px is not None:
        con_px.close()
    vols = {q["id"]: _vol(prices, q) for q in qs}
    out["with_vol"] = sum(1 for v in vols.values() if v is not None)
    pols = dict(POLICIES)
    pols["vol_rate_40"] = lambda past, bs, q=None: _vol_rate(past, bs, q, vols, 0.4)
    pols["vol_rate_70"] = lambda past, bs, q=None: _vol_rate(past, bs, q, vols, 0.7)
    for name, pol in pols.items():
        if name.startswith("vol_"):
            v = [brier(pol(qs[:i], _br(q), q), q["fired"]) for i, q in enumerate(qs) if i >= WARM]
        else:
            v = [brier(pol(qs[:i], _br(q)), q["fired"]) for i, q in enumerate(qs) if i >= WARM]
        d = [a - b for a, b in zip(v, base)]
        lo, hi = _boot(d)
        out["policies"][name] = {"brier": sum(v) / len(v), "diff": sum(d) / len(d), "lo90": lo, "hi90": hi,
                                 "adopt": hi < 0}
    return out


def vol_table(con, h=5) -> dict:
    """채택된 vol_rate 정책을 사람이 쓰게 펼친 표: 60일 일간 변동성 오분위 경계와 구간별 갈래 빈도.

    정산된 물음 중 관측 기간이 h 인 것만 센다(h 마다 칸 폭이 다르다). 갈래 키는 A(위)·C(가운데)·B(아래).
    """
    from module_lens._score import _open_px, _Prices, parse_observable
    qs = _rows(con, """SELECT q.id,q.settle,q.subject,q.observable,q.branches,o.fired FROM questions q
                       JOIN outcomes o ON o.question=q.id WHERE o.fired IN ('A','B','C')""")
    qs = [q for q in qs if (parse_observable(q["observable"]).get("h") == h)]
    con_px = _open_px()
    prices = _Prices(con_px)
    if con_px is not None:
        con_px.close()
    rows = [(v, q["fired"]) for q in qs for v in [_vol(prices, q)] if v is not None]
    if len(rows) < 50:
        return {"h": h, "n": len(rows)}
    vs = sorted(v for v, _ in rows)
    edges = [vs[int(len(vs) * k / 5)] for k in (1, 2, 3, 4)]
    bands = []
    for i in range(5):
        lo = edges[i - 1] if i else 0.0
        hi = edges[i] if i < 4 else None
        f = [k for v, k in rows if v >= lo and (hi is None or v < hi)]
        n = len(f)
        bands.append({"vol_lo": lo, "vol_hi": hi, "n": n,
                      **{k: (1 + f.count(k)) / (3 + n) for k in "ACB"}})
    return {"h": h, "n": len(rows), "bands": bands}


def method_skill(con) -> dict:
    """방법마다 «변동성 기준률보다 브라이어를 얼마나 낮췄나»(+면 실력). 적중률이 아니라 확률의 질로 잰다.

    2026-10-31: 세 갈래에서 «지지한 갈래가 일어났나» 적중률은 표본 고르기(신호가 켜진 날만)와
    supports 정하는 법에 휘둘려, 시뮬 보고서가 «반대로 작동»이라 한 방법을 «먼저 쓸 방법»으로 올렸다.
    기준률 칸은 전체 정산에서 센다(순위용 — 약간의 표본 안 적합을 안고 간다).
    """
    from module_lens._score import _open_px, _Prices
    qs = _rows(con, """SELECT q.id,q.settle,q.subject,q.branches,o.fired FROM questions q JOIN outcomes o ON o.question=q.id
                       WHERE o.fired NOT IN ('VOID','AMBIGUOUS') ORDER BY q.settle,q.id""")
    qs = [q for q in qs if len(_br(q)) >= 2 and q["fired"] in [b["k"] for b in _br(q)]]
    con_px = _open_px()
    prices = _Prices(con_px)
    if con_px is not None:
        con_px.close()
    vols = {q["id"]: _vol(prices, q) for q in qs}
    skill = {}
    for q in qs:
        base = _vol_rate(qs, _br(q), q, vols, 1.0) if vols.get(q["id"]) is not None else _base_rate(qs, _br(q), 1.0)
        skill[q["id"]] = brier(base, q["fired"]) - brier(_br(q), q["fired"])
    out = {}
    for e in _rows(con, "SELECT DISTINCT question, method FROM evidence WHERE dead IS NULL AND weight>0"):
        if e["question"] in skill:
            out.setdefault(e["method"], []).append(skill[e["question"]])
    res = {}
    for m, v in out.items():
        n = len(v)
        mean = sum(v) / n
        sd = (sum((x - mean) ** 2 for x in v) / (n - 1)) ** 0.5 if n > 1 else None
        se = sd / n ** 0.5 if sd else None
        res[m] = {"n": n, "skill": mean, "lo90": None if se is None else mean - 1.645 * se,
                  "hi90": None if se is None else mean + 1.645 * se}
    return res

