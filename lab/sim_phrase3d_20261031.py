# -*- coding: utf-8 -*-
"""시뮬레이션 3회차 — «이 문장(단어 묶음)이 뉴스에 튄 뒤 3일, 시장·업종에 무슨 일이 일어났나».

1·2회차는 «종목 이름이 든 기사의 말투»를 봤다. 사람이 궁금한 건 그게 아니라 «금리가 올랐다» 같은
**특정 문장 뒤에 일어난 일**이다(2026-10-31). 거시 문장은 제목에 회사 이름이 없어 종목 링크로는 안 잡히므로
단위를 «세션 × 단어»로 바꾼다.

재현: `python -X utf8 lab/sim_phrase3d_20261031.py` (module_lens build 뒤) → out/news3d/phrase_20261031.json

정의
  문장 = 단어 묶음의 AND. 묶음 안은 OR. 예: [["금리"],["인상","상승","올라","오른","오름"]] — 한 제목에 둘 다.
         단어는 `module_news_data._tokenize.tokens` (조사 절단, 단일 원본) 결과와 **앞부분 일치**로 맞춘다.
  세션   = 기사 발행시각 → 그 시장의 장 마감 전이면 그날, 아니면 다음 거래일 (`module_lens._data._session`).
  튄 날  = 그 문장 기사 수 ÷ 그 세션 전체 기사 수(점유율)의 z ≥ 2, 기준은 직전 30세션(최소 10) — `_burst` 와 같은 자.
           연달아 튄 날은 한 사건으로 접고 첫날만 쓴다(겹치는 3일 창을 두 번 세지 않게).
  일어난 일 = 그 세션 종가 기준 +1·+2·+3일 누적의 평균
           · 시장 = 유니버스 동일가중 평균 (KR 832 · US 300) — 지수가 아니다
           · 업종 = 업종 동일가중 − 시장
           · 이어서 뜬 단어 = +1~+3세션 점유율 − 직전 3세션 점유율
  기준선 = 같은 기간 모든 세션의 같은 값. 사건 평균 − 기준선, t 는 사건 단위.
  🔴 holdout: 2026-09-08 세션까지만 (sim_news3d_20261031 과 같은 선).
"""
from __future__ import annotations

import json
import math
import pathlib
import sqlite3
import sys
from collections import Counter, defaultdict

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from module_lens import _data                                  # noqa: E402
from module_lens._config import NEWS_START, VEC_DB            # noqa: E402
from module_news_data._tokenize import tokens                 # noqa: E402

OUT = ROOT / "out" / "news3d"
LAST = "2026-09-08"
Z, WIN, MIN_OBS = 2.0, 30, 10
MIN_DF = 300            # 발굴 단계: 이보다 드문 단어는 안 본다
MIN_EVENTS = 4

UP = ["인상", "상승", "올라", "올랐", "오른", "오름", "급등", "치솟", "뛰"]
DOWN = ["인하", "하락", "내려", "내렸", "내린", "급락", "떨어"]
PHRASES = {
    "금리 오름": [["금리"], UP], "금리 내림": [["금리"], DOWN],
    "국채금리 오름": [["국채"], UP], "환율 오름": [["환율"], UP], "환율 내림": [["환율"], DOWN],
    "유가 오름": [["유가"], UP], "유가 내림": [["유가"], DOWN],
    "관세": [["관세"]], "물가 오름": [["물가", "인플레"], UP],
    "반도체 수출": [["반도체"], ["수출"]], "외국인 매도": [["외국인"], ["매도", "순매도", "팔"]],
    "외국인 매수": [["외국인"], ["매수", "순매수", "사들"]],
    # 영어는 `tokens` 가 대문자로 바꾼다 — 앞부분 일치라 RATE 가 RATES 도 잡는다
    "rate hike": [["HIKE", "RAISE"], ["RATE"]],
    "rate cut": [["CUT"], ["RATE"]],
    "yields rise": [["YIELD", "TREASUR"], ["RISE", "JUMP", "CLIMB", "SURGE", "SOAR"]],
    "oil rise": [["OIL", "CRUDE"], ["RISE", "JUMP", "SURGE", "CLIMB", "SOAR"]],
    "tariff": [["TARIFF"]],
    "inflation": [["INFLATION", "CPI"]],
    "layoffs": [["LAYOFF"]],
}


def match(toks: set[str], groups) -> bool:
    return all(any(t.startswith(w) for t in toks for w in g) for g in groups)


def load_titles():
    src = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    rows = src.execute("SELECT published_at, title FROM articles WHERE market_day >= ? "
                       "AND title IS NOT NULL", (NEWS_START,)).fetchall()
    src.close()
    return rows


def market_frames(con):
    P = _data.panels(con)
    uni = pd.read_sql_query("SELECT ticker, market, sector FROM universe", con)
    out = {}
    for mk, C in P.items():
        C = C.ffill(limit=2)
        r = C.pct_change(fill_method=None)
        cum = {h: C.shift(-h) / C - 1 for h in (1, 2, 3)}
        f3 = sum(cum.values()) / 3                                   # 종목별 앞3일 평균
        mkt = f3.mean(axis=1)
        sec_of = uni[uni.market == mk].set_index("ticker").sector
        sec = {}
        for s, cols in sec_of.groupby(sec_of).groups.items():
            cols = [c for c in cols if c in f3.columns]
            if len(cols) >= 5:
                sec[s] = f3[cols].mean(axis=1) - mkt
        out[mk] = {"days": list(C.index), "mkt": mkt, "sec": pd.DataFrame(sec), "r": r}
    return out


def events(share: pd.Series) -> list[str]:
    prev = share.shift(1)
    mu = prev.rolling(WIN, min_periods=MIN_OBS).mean()
    sd = prev.rolling(WIN, min_periods=MIN_OBS).std()
    z = (share - mu) / sd.where(sd > 0)
    hot = (z >= Z).fillna(False)
    first = hot & ~hot.shift(1, fill_value=False)
    return [d for d in share.index[first] if d <= LAST]


def effect(days: list[str], s: pd.Series) -> dict | None:
    s = s.dropna()
    s = s[s.index <= LAST]
    ev = s.reindex([d for d in days if d in s.index]).dropna()
    if len(ev) < MIN_EVENTS:
        return None
    base = float(s.mean())
    diff = ev.values - base
    se = float(np.std(diff, ddof=1) / math.sqrt(len(diff))) if len(diff) > 1 else float("nan")
    return {"n": int(len(ev)), "pct": float(diff.mean() * 100), "t": float(diff.mean() / se) if se > 0 else None,
            "hit": float((ev.values > base).mean())}


def bh(ps: list[float], q=0.1) -> float:
    """Benjamini–Hochberg 문턱 p. 통과하는 게 없으면 0."""
    ps = sorted(ps)
    m = len(ps)
    thr = 0.0
    for i, p in enumerate(ps, 1):
        if p <= q * i / m:
            thr = p
    return thr


def p_of(t: float | None, n: int) -> float:
    if t is None or n < 3:
        return 1.0
    return math.erfc(abs(t) / math.sqrt(2))      # 정규 근사(양측) — 표본이 작아 낙관적이다


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    con = _data.connect()
    F = market_frames(con)
    rows = load_titles()
    print(f"제목 {len(rows):,}건 토큰화…", flush=True)

    res = {"holdout_last": LAST, "markets": {}}
    for mk, fr in F.items():
        days = fr["days"]
        tot = Counter()
        ph_cnt = {k: Counter() for k in PHRASES}
        df_cnt: dict[str, Counter] = defaultdict(Counter)
        for pub, title in rows:
            s = _data._session(pub, mk, days)
            if s is None:
                continue
            tot[s] += 1
            tk = tokens(title)
            for k, g in PHRASES.items():
                if match(tk, g):
                    ph_cnt[k][s] += 1
            for t in tk:
                df_cnt[t][s] += 1
        sess = [d for d in days if tot[d] > 0]
        T = pd.Series({d: tot[d] for d in sess})

        def share(c: Counter) -> pd.Series:
            return pd.Series({d: c.get(d, 0) for d in sess}) / T

        def after_words(evd: list[str], top=8):
            """사건 뒤 +1~+3세션에 점유율이 오른 단어 (사건 전 3세션 대비)."""
            idx = {d: i for i, d in enumerate(sess)}
            gain = Counter()
            for w, c in big.items():
                sh = shares[w]
                v = []
                for d in evd:
                    i = idx.get(d)
                    if i is None or i < 3 or i + 3 >= len(sess):
                        continue
                    v.append(sh.iloc[i + 1:i + 4].mean() - sh.iloc[i - 3:i].mean())
                if len(v) >= MIN_EVENTS:
                    gain[w] = float(np.mean(v))
            return [(w, round(g * 100, 3)) for w, g in gain.most_common(top)]

        big = {w: c for w, c in df_cnt.items() if sum(c.values()) >= MIN_DF}
        shares = {w: share(c) for w, c in big.items()}
        R = {"sessions": len(sess), "first": sess[0], "last": sess[-1], "vocab": len(big),
             "baseline_mkt3_pct": float(fr["mkt"][fr["mkt"].index <= LAST].mean() * 100), "phrases": {}}

        for k in PHRASES:
            sh = share(ph_cnt[k])
            evd = events(sh)
            e = effect(evd, fr["mkt"])
            secs = {}
            for s in fr["sec"].columns:
                x = effect(evd, fr["sec"][s])
                if x:
                    secs[s] = x
            top_sec = sorted(secs.items(), key=lambda kv: -abs(kv[1]["t"] or 0))[:4]
            R["phrases"][k] = {"articles": int(sum(ph_cnt[k].values())), "event_days": evd, "market": e,
                               "sectors_top": top_sec, "words_after": after_words(evd) if len(evd) >= MIN_EVENTS else []}
            print(f"[{mk}] {k:12s} 기사 {R['phrases'][k]['articles']:6d} 사건 {len(evd):2d} 시장 {e}", flush=True)

        # 발굴: 모든 단어를 같은 자로
        disc = []
        for w, sh in shares.items():
            evd = events(sh)
            e = effect(evd, fr["mkt"])
            if e:
                disc.append((w, e))
        thr = bh([p_of(e["t"], e["n"]) for _, e in disc])
        disc.sort(key=lambda x: -abs(x[1]["t"] or 0))
        R["discovery"] = {"words_tested": len(disc), "bh_q10_p_threshold": thr,
                          "passed_bh": [w for w, e in disc if p_of(e["t"], e["n"]) <= thr and thr > 0],
                          "top": [(w, e) for w, e in disc[:25]]}
        res["markets"][mk] = R
        print(f"[{mk}] 발굴 {len(disc)}단어 · BH 통과 {len(R['discovery']['passed_bh'])}", flush=True)
        for w, e in disc[:15]:
            print(f"    {w:12s} 사건 {e['n']:2d} 시장 {e['pct']:+.2f}%p t {e['t']:+.2f} 적중 {e['hit']:.0%}")

    (OUT / "phrase_20261031.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
