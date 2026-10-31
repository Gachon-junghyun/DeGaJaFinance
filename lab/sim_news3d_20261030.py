# -*- coding: utf-8 -*-
"""시뮬레이션 1회 — 뉴스 임베딩 × 이후 3일 평균 초과수익 → «무엇을 몇 % 보고 고를까».

실험 노트(참고용, 매매 지시 아님). 재현: `python -X utf8 lab/sim_news3d_20261030.py`
산출: out/news3d/sim_20261030.json · out/news3d/sim_20261030.md

재료는 전부 이미 있는 파생물을 **읽기만** 한다(새 벡터 0, 네트워크 0):
  data/inflection.db  px(종가) · mention_link(종목↔기사) · universe
  data/news_vectors.db 제목·발행시각·768차원 벡터(ko-sroberta)

라벨
  세션 s  = 발행시각(KST)이 거래일 15:30 전이면 그날, 아니면 다음 거래일.
  반응     = s 당일 수익 − 같은 날 유니버스 평균 (사람들이 그날 어떻게 받았나)
  앞3일    = s 종가에 샀다 치고 s+1·s+2·s+3 누적수익의 평균 − 같은 날 유니버스 평균
           (사람이 말한 «그 이후 3일 동안 평균 높낮이»)

렌즈(볼 것) — 전부 s 종가에 알 수 있는 정보만
  emb_react  임베딩 → «반응» 릿지. 가격이 가르친 긍정·부정(뉴스 말투)
  emb_fwd    임베딩 → «앞3일» 릿지
  analog     학습 구간에서 가장 닮은 기사 20건의 앞3일 평균
  lexicon    제목 유형(module_inflection._lexicon)의 호재 +1 / 악재 −1
  react      실제 그날 반응(가격이 낸 판정) — 이어지나 되돌리나
  diverge    emb_react 예측 − 실제 반응 (말은 좋은데 가격이 안 받았나)
  attention  그날 기사 수(log)
  prior5     직전 5일 초과수익

검증 — walk-forward
  앞 25거래일로 처음 학습, 10거래일마다 다시 학습해 바로 다음 10일을 표본 밖으로 잰다.
  학습 라벨이 시험 구간과 겹치지 않게 3거래일 띄운다(embargo).
  하루 = 한 표본(날짜 묶음, lab/INFLECTION_NEWS_KR.md §2-③). 일별 횡단면 스피어만 IC.

자동 비중 — 각 재학습 시점에 그때까지의 «표본 밖» IC 의 t 값만 보고 비중을 정한다
  w_i = max(t_i, 0) / Σ max(t_j, 0)  (전부 0 이하면 동일비중)
  그 비중으로 섞은 합성 점수를 다음 10일에 표본 밖으로 잰다 → 비중 자체도 표본 밖 검증.
"""
from __future__ import annotations

import json
import math
import pathlib
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, time, timedelta, timezone

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from module_inflection import _analog, _lexicon               # noqa: E402
from module_news_data._timeaxis import parse_published         # noqa: E402

KST = timezone(timedelta(hours=9))
DATA = ROOT / "data"
OUT = ROOT / "out" / "news3d"
INIT_DAYS, STEP, EMBARGO, H = 25, 10, 3, 3
RIDGE = 30.0
K_ANALOG = 20
GOOD = {"수주_계약", "실적_호", "주주환원", "설비_투자", "제품_기술", "협약_MOU", "지분_MA"}
BAD = {"실적_악", "규제_법률", "자본조달_희석", "사후보도_급락"}
LENSES = ["emb_react", "emb_fwd", "analog", "lexicon", "react", "diverge", "attention", "prior5"]


def load():
    con = sqlite3.connect(f"file:{DATA / 'inflection.db'}?mode=ro", uri=True)
    px = pd.read_sql_query("SELECT ticker,date,close FROM px", con)
    close = px.pivot(index="date", columns="ticker", values="close").sort_index()
    links = pd.read_sql_query("SELECT ticker,url_hash FROM mention_link", con)
    names = dict(con.execute("SELECT ticker,name FROM universe").fetchall())
    con.close()
    v = sqlite3.connect(f"file:{DATA / 'news_vectors.db'}?mode=ro", uri=True)
    hashes = sorted(set(links.url_hash))
    meta = {}
    for i in range(0, len(hashes), 900):
        part = hashes[i:i + 900]
        q = f"SELECT url_hash,published_at,source,title FROM articles WHERE url_hash IN ({','.join('?' * len(part))})"
        for h, p, s, t in v.execute(q, part):
            meta[h] = (p, s, t)
        q = f"SELECT url_hash,vec FROM vectors WHERE url_hash IN ({','.join('?' * len(part))})"
        for h, b in v.execute(q, part):
            meta[h] = meta.get(h, (None, None, None)) + (np.frombuffer(b, dtype=np.float16).astype(np.float32),)
    v.close()
    return close, links, names, meta


def session_of(pub, days, day_idx):
    dt = parse_published(pub)
    if dt is None:
        return None
    k = dt.astimezone(KST)
    d = k.strftime("%Y-%m-%d")
    # 그날이 거래일이고 장 마감 전이면 그날, 아니면 다음 거래일
    if d in day_idx and k.time() < time(15, 30):
        return d
    for x in days[np.searchsorted(days, d, side="right"):][:1]:
        return x
    return None


def ridge_fit(X, y, lam=RIDGE):
    mu = X.mean(0)
    Xc = X - mu
    ym = y.mean()
    w = np.linalg.solve(Xc.T @ Xc + lam * np.eye(X.shape[1]), Xc.T @ (y - ym))
    return lambda Z: (Z - mu) @ w + ym


def spearman(a, b):
    if len(a) < 5:
        return None
    ra = pd.Series(a).rank().values
    rb = pd.Series(b).rank().values
    if ra.std() == 0 or rb.std() == 0:
        return None
    return float(np.corrcoef(ra, rb)[0, 1])


def tstat(xs):
    xs = [x for x in xs if x is not None and not math.isnan(x)]
    if len(xs) < 3:
        return None, None, len(xs)
    m = float(np.mean(xs))
    se = float(np.std(xs, ddof=1) / math.sqrt(len(xs)))
    return m, (m / se if se > 0 else None), len(xs)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    close, links, names, meta = load()
    days = np.array(close.index.tolist())
    day_idx = {d: i for i, d in enumerate(days)}
    ret = close.pct_change()
    exc = ret.sub(ret.mean(axis=1), axis=0)                         # 그날 횡단면 초과
    cum = {h: close.shift(-h) / close - 1 for h in range(1, H + 1)}
    fwd = sum(cum[h] for h in cum) / H                               # 앞 1·2·3일 누적의 평균
    fwd_exc = fwd.sub(fwd.mean(axis=1), axis=0)
    prior5 = (close / close.shift(5) - 1)
    prior5 = prior5.sub(prior5.mean(axis=1), axis=0)
    cmean = _analog.corpus_mean()

    # 기사 단위 행
    rows = []
    for tic, h in links.itertuples(index=False):
        m = meta.get(h)
        if not m or len(m) < 4 or tic not in close.columns:
            continue
        s = session_of(m[0], days, day_idx)
        if s is None:
            continue
        rows.append((tic, h, s, m[2] or "", m[3]))
    art = pd.DataFrame(rows, columns=["ticker", "h", "s", "title", "vec"])
    art["react"] = [exc.at[s, t] if s in exc.index else np.nan for t, s in zip(art.ticker, art.s)]
    art["fwd"] = [fwd_exc.at[s, t] for t, s in zip(art.ticker, art.s)]
    art = art.dropna(subset=["react", "fwd"]).reset_index(drop=True)
    V = np.vstack(art.vec.values) - cmean
    V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
    art["lex"] = [(1 if c in GOOD else -1 if c in BAD else 0) if (c := _lexicon.classify_title(t)) else 0
                  for t in art.title]
    art["type"] = [_lexicon.classify_title(t) or "일반" for t in art.title]
    sdays = sorted(art.s.unique())
    print(f"기사 {len(art):,} · 세션일 {len(sdays)} ({sdays[0]}~{sdays[-1]}) · 종목 {art.ticker.nunique()}")

    # walk-forward
    oos = []                 # (ticker, s) 단위 표본 밖 점수
    weights_log = []
    ic_hist = defaultdict(list)   # 렌즈 → 표본 밖 일별 IC (과거만 누적)
    combo_ic, equal_ic = [], []
    start = INIT_DAYS
    while start < len(sdays):
        test_days = sdays[start:start + STEP]
        train_cut = sdays[max(0, start - EMBARGO)]                  # 이 날 전까지만 학습
        tr = art.s < train_cut
        te = art.s.isin(test_days)
        if tr.sum() < 500 or te.sum() == 0:
            start += STEP
            continue
        f_react = ridge_fit(V[tr], art.react[tr].values)
        f_fwd = ridge_fit(V[tr], art.fwd[tr].values)
        Vtr, ytr = V[tr], art.fwd[tr].values
        sub = art[te].copy()
        Vte = V[te.values]
        sub["emb_react"] = f_react(Vte)
        sub["emb_fwd"] = f_fwd(Vte)
        sim = Vte @ Vtr.T
        top = np.argpartition(-sim, K_ANALOG, axis=1)[:, :K_ANALOG]
        sub["analog"] = ytr[top].mean(1)
        g = sub.groupby(["ticker", "s"]).agg(
            emb_react=("emb_react", "mean"), emb_fwd=("emb_fwd", "mean"), analog=("analog", "mean"),
            lexicon=("lex", "mean"), react=("react", "first"), fwd=("fwd", "first"), n=("h", "count")).reset_index()
        g["diverge"] = g.emb_react - g.react
        g["attention"] = np.log1p(g.n)
        g["prior5"] = [prior5.at[s, t] for t, s in zip(g.ticker, g.s)]

        # 이 블록 들어가기 전의 표본 밖 기록만으로 비중
        ts = {L: (tstat(ic_hist[L])[1] or 0.0) for L in LENSES}
        pos = {L: max(t, 0.0) for L, t in ts.items()}
        tot = sum(pos.values())
        w = {L: (pos[L] / tot if tot > 0 else 1 / len(LENSES)) for L in LENSES}
        weights_log.append({"from": test_days[0], "n_hist_days": len(ic_hist["emb_react"]),
                            "t": {k: round(v, 2) for k, v in ts.items()},
                            "w": {k: round(v, 3) for k, v in w.items()}})

        for d, gd in g.groupby("s"):
            if len(gd) < 5:
                continue
            z = {L: (gd[L] - gd[L].mean()) / (gd[L].std() or 1) for L in LENSES}
            combo = sum(w[L] * z[L].fillna(0) for L in LENSES)
            eq = sum(z[L].fillna(0) for L in LENSES) / len(LENSES)
            combo_ic.append((d, spearman(combo.values, gd.fwd.values)))
            equal_ic.append((d, spearman(eq.values, gd.fwd.values)))
            for L in LENSES:
                ic_hist[L].append(spearman(gd[L].values, gd.fwd.values))
        oos.append(g)
        start += STEP

    G = pd.concat(oos, ignore_index=True)
    res = {"window": [sdays[0], sdays[-1]], "articles": int(len(art)), "oos_rows": int(len(G)),
           "oos_days": int(G.s.nunique()), "lenses": {}}
    for L in LENSES:
        m, t, n = tstat(ic_hist[L])
        # 상·하위 3분위 앞3일 차 (날짜 묶음)
        spr = []
        for d, gd in G.groupby("s"):
            if len(gd) < 6:
                continue
            q = gd[L].rank(pct=True)
            spr.append(gd.fwd[q > 2 / 3].mean() - gd.fwd[q <= 1 / 3].mean())
        sm, stt, _ = tstat(spr)
        res["lenses"][L] = {"ic_mean": m, "ic_t": t, "days": n,
                            "top_minus_bottom_3d_pct": sm * 100 if sm is not None else None,
                            "spread_t": stt}
    for name, arr in (("combo_auto", combo_ic), ("combo_equal", equal_ic)):
        m, t, n = tstat([x for _, x in arr])
        res[name] = {"ic_mean": m, "ic_t": t, "days": n}
    res["weights_log"] = weights_log
    res["final_weights"] = weights_log[-1]["w"] if weights_log else {}

    # 제목 유형별 — 가격이 가르친 긍정·부정(emb_react)과 실제 앞3일
    T = art.groupby("type").agg(n=("h", "count"), react=("react", "mean"), fwd=("fwd", "mean"))
    T = T[T.n >= 40].sort_values("fwd", ascending=False)
    res["by_type"] = {k: {"n": int(r.n), "react_pct": r.react * 100, "fwd3_pct": r.fwd * 100} for k, r in T.iterrows()}
    # 반응 부호 × 앞3일 — 이어지나 되돌리나 (날짜 묶음)
    cont = []
    for d, gd in G.groupby("s"):
        if len(gd) < 6:
            continue
        cont.append(gd.fwd[gd.react > 0].mean() - gd.fwd[gd.react <= 0].mean())
    m, t, n = tstat([c for c in cont if not math.isnan(c)])
    res["react_up_minus_down_fwd3_pct"] = {"mean": m * 100 if m is not None else None, "t": t, "days": n}

    (OUT / "sim_20261030.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if k not in ("weights_log", "by_type")}, ensure_ascii=False, indent=1))
    print("weights_log:")
    for wl in weights_log:
        print(" ", wl["from"], wl["n_hist_days"], wl["w"])
    print("by_type:")
    for k, v in res["by_type"].items():
        print(f"  {k:10s} n={v['n']:5d} 반응 {v['react_pct']:+.2f}% 앞3일 {v['fwd3_pct']:+.2f}%")


if __name__ == "__main__":
    main()
