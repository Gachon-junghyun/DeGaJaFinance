# -*- coding: utf-8 -*-
"""시뮬레이션 6회차 — 단어 파급력: «이 단어가 나오면 가격이 (방향 상관없이) 얼마나 크게 움직이나».

사람 물음(2026-10-31): 방향이 아니라 크기. «금리는 보통 위아래로 커지고, 실적도 클 테고, '입니다'는 0 에 가깝다 —
얼마나 중요한지를 보고 싶다». 이 값이 증거 장부(매일 조사의 «이 증거로 이 선택을, 몇 %로»)의 사전값이 된다.

두 층
  ① 종목 층 — (종목, 세션) 이벤트의 **장 시작 전** 기사 제목 단어 → 그날·이후 3일 |초과수익| ÷ 그 종목 평소 변동성
     파급력 = 그 단어가 든 이벤트의 평균 |z| ÷ 모든 뉴스 이벤트의 평균 |z|   (1.0 = 아무 일 없음)
  ② 시장 층 — 세션마다 장 전 제목 전체의 단어 → 그날 |시장 수익| ÷ 평소 |시장 수익|
     단어가 그 세션 점유율 상위 20% 인 날의 평균 |시장| ÷ 전체 평균
  장 전만 쓰는 이유: 장중 기사의 «급등»·«특징주»는 이미 움직인 가격을 묘사한다(5회차 E1c 실측 — 순환).
  작은 표본은 줄여 잡는다: (Σ|z| + K·기준) ÷ (n + K), K=20 (경험적 베이즈) — 3번 나온 단어가 1등이 되지 않게.
  안정성: 기간을 반으로 갈라 두 반쪽 파급력의 순위상관 — 낮으면 «사전값»으로 못 쓴다.
  🔴 2026-09-08 세션까지(holdout 선).

재현: `python -X utf8 lab/sim_wordimpact_20261031.py` → out/news3d/wordimpact_20261031.json
"""
from __future__ import annotations

import json
import pathlib
import sqlite3
import sys
from collections import defaultdict
from zoneinfo import ZoneInfo
from datetime import time

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from module_lens import _data                                   # noqa: E402
from module_lens._config import NEWS_START, VEC_DB              # noqa: E402
from module_news_data._timeaxis import parse_published          # noqa: E402
from module_news_data._tokenize import tokens                   # noqa: E402

OUT = ROOT / "out" / "news3d"
LAST = "2026-09-08"
K = 20
MIN_EV, MIN_SESS = 30, 15
OPEN = {"KR": ("Asia/Seoul", time(9, 0)), "US": ("America/New_York", time(9, 30))}


def preopen(pub, s, mk) -> bool:
    dt = parse_published(pub)
    if dt is None:
        return False
    loc = dt.astimezone(ZoneInfo(OPEN[mk][0]))
    d = loc.strftime("%Y-%m-%d")
    return d < s or (d == s and loc.time() < OPEN[mk][1])


def shrink(vals: list[float], base: float) -> float:
    return (sum(vals) + K * base) / (len(vals) + K)


def rank_corr(a: dict, b: dict) -> float | None:
    ks = [k for k in a if k in b]
    if len(ks) < 20:
        return None
    x, y = pd.Series([a[k] for k in ks]).rank(), pd.Series([b[k] for k in ks]).rank()
    return float(np.corrcoef(x, y)[0, 1])


def stock_layer(con, mk, P, pubs):
    exc = P.pct_change(fill_method=None)
    exc = exc.sub(exc.mean(axis=1), axis=0)
    sd = exc.shift(1).rolling(60, min_periods=30).std()          # 그날 제외 평소 변동성
    art = _data.article_frame(con, mk)
    art = art[(art.s <= LAST)]
    art = art[[preopen(pubs.get(h), s, mk) for h, s in zip(art.h, art.s)]]
    ev = []
    for (tk, s), g in art.groupby(["ticker", "s"]):
        if s not in sd.index or tk not in sd.columns:
            continue
        v = sd.at[s, tk]
        r = g.iloc[0]
        if pd.isna(v) or v == 0 or pd.isna(r.react) or pd.isna(r.fwd3):
            continue
        toks = set().union(*(tokens(t) for t in g.title))
        ev.append((s, abs(r.react) / v, abs(r.fwd3) / v, toks))
    base0 = float(np.mean([e[1] for e in ev]))
    base3 = float(np.mean([e[2] for e in ev]))
    mid = sorted({e[0] for e in ev})[len({e[0] for e in ev}) // 2]
    by = defaultdict(lambda: {"d0": [], "d3": [], "h1": [], "h2": []})
    for s, z0, z3, toks in ev:
        for w in toks:
            b = by[w]
            b["d0"].append(z0)
            b["d3"].append(z3)
            (b["h1"] if s < mid else b["h2"]).append(z0)
    rows = {}
    for w, b in by.items():
        if len(b["d0"]) < MIN_EV:
            continue
        rows[w] = {"n": len(b["d0"]), "day0": shrink(b["d0"], base0) / base0, "fwd3": shrink(b["d3"], base3) / base3,
                   "h1": shrink(b["h1"], base0) / base0, "h2": shrink(b["h2"], base0) / base0}
    stab = rank_corr({w: r["h1"] for w, r in rows.items()}, {w: r["h2"] for w, r in rows.items()})
    stab3 = None
    return {"events": len(ev), "words": len(rows), "split_half_rank_corr_day0": stab, "rows": rows}


def market_layer(mk, P, titles):
    r = P.pct_change(fill_method=None).mean(axis=1)                 # 동일가중 시장
    absr = r.abs()
    days = list(P.index)
    per = defaultdict(set)
    cnt = defaultdict(int)
    for pub, title in titles:
        s = _data._session(pub, mk, days)
        if s is None or s > LAST or not preopen(pub, s, mk):
            continue
        cnt[s] += 1
        per[s] |= {(w) for w in tokens(title)}
    # 세션별 단어 기사 수가 필요해 한 번 더 — 점유율
    wc = defaultdict(lambda: defaultdict(int))
    for pub, title in titles:
        s = _data._session(pub, mk, days)
        if s is None or s > LAST or not preopen(pub, s, mk):
            continue
        for w in tokens(title):
            wc[w][s] += 1
    sess = [d for d in days if cnt.get(d) and d in absr.index and not pd.isna(absr[d])]
    base = float(absr[sess].mean())
    rows = {}
    for w, c in wc.items():
        present = [d for d in sess if c.get(d)]
        if len(present) < MIN_SESS:
            continue
        sh = pd.Series({d: c.get(d, 0) / cnt[d] for d in sess})
        top = sh[sh >= sh.quantile(0.8)].index
        top = [d for d in top if c.get(d)]
        if len(top) < 5:
            continue
        rows[w] = {"sessions": len(present), "top_days": len(top),
                   "impact": shrink([absr[d] for d in top], base) / base}
    return {"sessions": len(sess), "base_abs_pct": base * 100, "words": len(rows), "rows": rows}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    con = _data.connect()
    P = {mk: p.ffill(limit=2) for mk, p in _data.panels(con).items()}
    src = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    titles = src.execute("SELECT published_at, title FROM articles WHERE market_day >= ? AND title IS NOT NULL",
                         (NEWS_START,)).fetchall()
    pubs = dict(src.execute("SELECT url_hash, published_at FROM articles WHERE market_day >= ?", (NEWS_START,)))
    src.close()
    res = {"last": LAST, "K": K, "markets": {}}
    for mk in ("KR", "US"):
        st = stock_layer(con, mk, P[mk], pubs)
        mt = market_layer(mk, P[mk], titles)
        res["markets"][mk] = {"stock": st, "market": mt}
        rows = st["rows"]
        print(f"\n[{mk}] 종목 층: 장 전 이벤트 {st['events']:,} · 단어 {st['words']} · 반쪽 안정성(순위상관) {st['split_half_rank_corr_day0']}")
        srt = sorted(rows.items(), key=lambda kv: -kv[1]["day0"])
        print("  파급력 큰 단어 (그날 |z| 배수 · 이후3일 배수 · 건수):")
        print("   ", " · ".join(f"{w} {r['day0']:.2f}/{r['fwd3']:.2f}({r['n']})" for w, r in srt[:30]))
        print("  파급력 작은 단어:")
        print("   ", " · ".join(f"{w} {r['day0']:.2f}({r['n']})" for w, r in srt[-15:]))
        for w in ["금리", "실적", "영업이익", "수주", "계약", "목표가", "유상증자", "자사주", "배당", "소송", "입니다",
                  "EARNINGS", "GUIDANCE", "DOWNGRADE", "UPGRADE", "FDA", "LAWSUIT", "ACQUIRE", "THE", "AND"]:
            if w in rows:
                print(f"    {w}: 그날 {rows[w]['day0']:.2f} · 3일 {rows[w]['fwd3']:.2f} · n {rows[w]['n']}")
        mr = sorted(mt["rows"].items(), key=lambda kv: -kv[1]["impact"])
        print(f"  시장 층: 세션 {mt['sessions']} · 평소 |시장| {mt['base_abs_pct']:.2f}% · 단어 {mt['words']}")
        print("   큰:", " · ".join(f"{w} {r['impact']:.2f}" for w, r in mr[:25]))
        for w in ["금리", "환율", "유가", "관세", "FED", "RATE", "INFLATION", "TARIFF", "입니다", "THE"]:
            if w in mt["rows"]:
                print(f"    {w}: {mt['rows'][w]['impact']:.2f} (세션 {mt['rows'][w]['sessions']})")
    (OUT / "wordimpact_20261031.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
