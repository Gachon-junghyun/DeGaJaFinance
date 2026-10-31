# -*- coding: utf-8 -*-
"""시뮬레이션 5회차 — 종목 → 종목 이벤트 → 이벤트 벡터 → «이런 이벤트 뒤에 무슨 일이».

사람 물음(2026-10-31): «각 종목 - 종목 이벤트 - 벡터화 이렇게는 못하나».
2회차 analog 는 **기사 한 건** 단위라 같은 사건 기사 수십 건이 이웃을 채웠다. 여기선 단위를 이벤트로 올린다.

  이벤트     = (종목, 세션)에 붙은 기사 묶음 (module_lens links). 기사 수 = 그 이벤트의 크기.
  이벤트 벡터 = 기사 벡터(코퍼스 평균 중심화)의 평균 → L2 정규화 (`module_inflection._analog.fingerprint` 와 같은 식)
  유형       = 학습 구간 이벤트 벡터를 KMeans(k=K) 로 묶은 것 — 사람이 정한 사전이 아니라 데이터가 정한 유형
  일어난 일   = react(그날 초과) · fwd3(+1~+3일 누적 평균 초과) · resid3(fwd3 에서 그날 반응·직전5일 되돌림을 날마다 뺀 나머지)

  학습 = 세션 < SPLIT, 시험 = SPLIT ≤ 세션 ≤ 2026-09-08 (holdout 선). 유형은 학습 구간에서만 정하고 시험 이벤트는 가장 가까운 유형에 붙인다.
  재는 것
    ① 유형표: 유형마다 대표 제목 · 학습/시험 각각의 react·fwd3·resid3 평균 → 부호가 시험에서도 유지되나
    ② 예측력: «유형의 학습 평균» 과 «닮은 과거 이벤트 20개 평균» 을 시험 이벤트의 값으로 쓸 때 일별 IC (날짜 묶음)
       — react 도 잰다: 장중에 뉴스를 보고 «오늘 어느 쪽인가»를 아는 데 쓸 수 있나

재현: `python -X utf8 lab/sim_stockevent_20261031.py` → out/news3d/stockevent_20261031.json
"""
from __future__ import annotations

import json
import math
import os
import pathlib
import sqlite3
import sys
from datetime import time
from zoneinfo import ZoneInfo
from collections import Counter

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from module_inflection import _analog          # noqa: E402
from module_lens import _data                  # noqa: E402

OUT = ROOT / "out" / "news3d"
SPLIT, LAST = "2026-07-15", "2026-09-08"
K, KNN = 30, 20
TARGETS = ["react", "fwd3", "resid3"]
# PREOPEN=1 이면 «장 시작 전» 기사만으로 이벤트를 만든다 — 장중 기사([특징주] 급등)는 이미 움직인 가격을 보도해
# react 예측이 순환이 된다. 장 전 기사만 남기면 그날 반응은 정말 뉴스 «뒤»의 일이다.
PREOPEN = os.environ.get("PREOPEN") == "1"
OPEN = {"KR": ("Asia/Seoul", time(9, 0)), "US": ("America/New_York", time(9, 30))}


def preopen_mask(art: pd.DataFrame, mk: str) -> pd.Series:
    from module_lens._config import VEC_DB
    from module_news_data._timeaxis import parse_published
    src = sqlite3.connect(f"file:{VEC_DB}?mode=ro", uri=True)
    pub = {}
    hs = sorted(set(art.h))
    for i in range(0, len(hs), 900):
        part = hs[i:i + 900]
        pub.update(src.execute(f"SELECT url_hash,published_at FROM articles WHERE url_hash IN ({','.join('?' * len(part))})", part))
    src.close()
    tz, op = ZoneInfo(OPEN[mk][0]), OPEN[mk][1]
    def ok(h, s):
        dt = parse_published(pub.get(h))
        if dt is None:
            return False
        loc = dt.astimezone(tz)
        d = loc.strftime("%Y-%m-%d")
        return d < s or (d == s and loc.time() < op)      # 세션 날짜 이전이거나 그날 개장 전
    return pd.Series([ok(h, s) for h, s in zip(art.h, art.s)], index=art.index)


def spearman(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    ok = ~(np.isnan(a) | np.isnan(b))
    if ok.sum() < 5:
        return None
    ra, rb = pd.Series(a[ok]).rank().values, pd.Series(b[ok]).rank().values
    if ra.std() == 0 or rb.std() == 0:
        return None
    return float(np.corrcoef(ra, rb)[0, 1])


def tstat(xs):
    xs = [x for x in xs if x is not None and not math.isnan(x)]
    if len(xs) < 3:
        return None, None, len(xs)
    m, se = float(np.mean(xs)), float(np.std(xs, ddof=1) / math.sqrt(len(xs)))
    return m, (m / se if se > 0 else None), len(xs)


def day_mean_t(df, col):
    """날짜 묶음 평균과 t — 같은 날 이벤트 여럿을 한 표본으로."""
    return tstat(df.groupby("s")[col].mean().tolist())


def residualize(ev: pd.DataFrame) -> pd.Series:
    """fwd3 를 날마다 react·prior5 에 회귀한 나머지 — E1 의 되돌림을 빼고 이벤트 몫만."""
    out = pd.Series(np.nan, index=ev.index)
    for d, g in ev.groupby("s"):
        g = g.dropna(subset=["fwd3", "react", "prior5"])
        if len(g) < 6:
            continue
        X = np.column_stack([np.ones(len(g)), g.react, g.prior5])
        b, *_ = np.linalg.lstsq(X, g.fwd3.values, rcond=None)
        out[g.index] = g.fwd3.values - X @ b
    return out


def run(con, mk, cmean):
    from sklearn.cluster import KMeans                     # 승인된 예외 — 뉴스 사건 클러스터링 전용(lazy)
    art = _data.article_frame(con, mk)
    art = art[art.s <= LAST].dropna(subset=["react", "fwd3"])
    vec = _data.vectors(sorted(set(art.h)))
    art = art[art.h.isin(vec)]
    if PREOPEN:
        art = art[preopen_mask(art, mk)]
    rows, V = [], []
    for (tk, s), g in art.groupby(["ticker", "s"]):
        M = np.vstack([vec[h] for h in g.h]) - cmean
        v = M.mean(0)
        n = np.linalg.norm(v)
        if n == 0:
            continue
        V.append(v / n)
        r = g.iloc[0]
        rows.append({"ticker": tk, "s": s, "n": len(g), "react": r.react, "fwd3": r.fwd3, "prior5": r.prior5,
                     "titles": list(dict.fromkeys(g.title))[:3]})
    ev = pd.DataFrame(rows)
    V = np.vstack(V).astype(np.float32)
    ev["resid3"] = residualize(ev)
    tr, te = (ev.s < SPLIT).values, (ev.s >= SPLIT).values
    print(f"[{mk}] 이벤트 {len(ev):,} (학습 {tr.sum():,} · 시험 {te.sum():,}) · 종목 {ev.ticker.nunique()}", flush=True)

    km = KMeans(n_clusters=K, n_init=5, random_state=0).fit(V[tr])
    ev["type"] = km.predict(V)
    cen = km.cluster_centers_ / np.linalg.norm(km.cluster_centers_, axis=1, keepdims=True)

    # ① 유형표
    types = []
    trm = ev[tr].groupby("type")[TARGETS].mean()
    for c in range(K):
        a, b = ev[tr & (ev.type == c).values], ev[te & (ev.type == c).values]
        # 대표 제목 = 중심에 가장 가까운 학습 이벤트들의 첫 제목
        idx = np.where(tr & (ev.type == c).values)[0]
        near = idx[np.argsort(-(V[idx] @ cen[c]))[:4]]
        row = {"type": c, "n_train": len(a), "n_test": len(b), "tickers": a.ticker.nunique(),
               "examples": [f"{ev.ticker[i]} {ev.s[i]} {ev.titles[i][0][:60]}" for i in near]}
        for col in TARGETS:
            row[f"{col}_train"] = day_mean_t(a, col)[0]
            m, t, n = day_mean_t(b, col)
            row[f"{col}_test"], row[f"{col}_test_t"] = m, t
        types.append(row)

    # ② 예측력 — 유형 평균 · 닮은 이벤트 평균
    pred = {}
    Vtr = V[tr]
    for col in TARGETS:
        ytr = ev[col].values[tr]
        ok = ~np.isnan(ytr)
        Vk, yk = Vtr[ok], ytr[ok]
        sim = V[te] @ Vk.T
        top = np.argpartition(-sim, KNN, axis=1)[:, :KNN]
        pred[f"knn_{col}"] = yk[top].mean(1)
        pred[f"type_{col}"] = ev.type[te].map(trm[col]).values
    T = ev[te].copy()
    for k, v in pred.items():
        T[k] = v
    ics = {}
    for col in TARGETS:
        for how in ("type", "knn"):
            xs = [spearman(g[f"{how}_{col}"], g[col]) for d, g in T.groupby("s") if len(g) >= 5]
            m, t, n = tstat(xs)
            ics[f"{how}→{col}"] = {"ic": m, "t": t, "days": n}
    return {"events": int(len(ev)), "train": int(tr.sum()), "test": int(te.sum()), "types": types, "ic": ics,
            "size_dist": Counter(min(int(x), 10) for x in ev.n)}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    con = _data.connect()
    cmean = _analog.corpus_mean()
    res = {"split": SPLIT, "last": LAST, "K": K, "markets": {}}
    for mk in ("KR", "US"):
        r = run(con, mk, cmean)
        res["markets"][mk] = r
        f = lambda x: "  ·  " if x is None else f"{x * 100:+.2f}"
        print(f"[{mk}] 예측력(일별 IC):", {k: (round(v['ic'], 3) if v['ic'] is not None else None,
                                            round(v['t'], 1) if v['t'] is not None else None) for k, v in r["ic"].items()})
        print(f"  유형 (학습→시험, %) — 시험에서 같은 부호인지")
        for t in sorted(r["types"], key=lambda x: -(x["n_train"])):
            print(f"  #{t['type']:2d} 학습 {t['n_train']:4d} 시험 {t['n_test']:4d} 종목 {t['tickers']:3d} | 반응 {f(t['react_train'])}→{f(t['react_test'])}"
                  f" | 앞3 {f(t['fwd3_train'])}→{f(t['fwd3_test'])} | 잔차 {f(t['resid3_train'])}→{f(t['resid3_test'])} | {t['examples'][0]}")
        (OUT / f"stockevent_20261031{'_preopen' if PREOPEN else ''}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
