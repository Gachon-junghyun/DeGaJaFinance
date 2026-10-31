# -*- coding: utf-8 -*-
"""시뮬레이션 2회차(E1) — 기간 최대(2026-05-01~), 미장 추가. 1회차(sim_news3d_20261030.py)와 같은 자.

재현: `python -X utf8 -m module_lens build` 다음 `python -X utf8 lab/sim_news3d_20261031.py`
산출: out/news3d/sim_20261031.json

1회차와 다른 점
  · 재료가 `module_lens`(data/lens.db) — KR 828종목 · US 300종목, 시장별로 따로 학습·채점
  · 라벨 셋(fwd1·fwd3·fwd5)을 같이 잰다 — 결론이 라벨에 흔들리나(E2 맛보기)
  · 🔴 2026-09-15 이후는 **안 본다(holdout)**. 표본 밖 시험일은 09-08 이전 세션까지만 —
    앞5일 라벨이 holdout 으로 넘어가지 않게. holdout 은 E4·E5 가 끝나고 단 한 번 연다.
  · analog 는 메모리 때문에 시험 기사를 1,000건씩 나눠 잰다
"""
from __future__ import annotations

import json
import math
import pathlib
import sys
from collections import defaultdict

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from module_inflection import _analog, _lexicon      # noqa: E402
from module_lens import _data                        # noqa: E402

OUT = ROOT / "out" / "news3d"
HOLDOUT = "2026-09-15"
LAST_TEST = "2026-09-08"
INIT_DAYS, STEP, EMBARGO = 25, 10, 5
RIDGE, K_ANALOG = 30.0, 20
GOOD = {"수주_계약", "실적_호", "주주환원", "설비_투자", "제품_기술", "협약_MOU", "지분_MA"}
BAD = {"실적_악", "규제_법률", "자본조달_희석", "사후보도_급락"}
LENSES = ["emb_react", "emb_fwd", "analog", "lexicon", "react", "diverge", "attention", "prior5"]
LABELS = ["fwd1", "fwd3", "fwd5"]


def ridge_fit(X, y, lam=RIDGE):
    mu, ym = X.mean(0), y.mean()
    Xc = X - mu
    w = np.linalg.solve(Xc.T @ Xc + lam * np.eye(X.shape[1]), Xc.T @ (y - ym))
    return lambda Z: (Z - mu) @ w + ym


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


def run_market(con, mk, cmean):
    art = _data.article_frame(con, mk)
    art = art[art.s < HOLDOUT].dropna(subset=["react", "fwd3"]).reset_index(drop=True)
    vec = _data.vectors(sorted(set(art.h)))
    art = art[art.h.isin(vec)].reset_index(drop=True)
    V = np.vstack([vec[h] for h in art.h]) - cmean
    V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
    del vec
    typ = [_lexicon.classify_title(t) for t in art.title]
    art["lex"] = [1 if c in GOOD else -1 if c in BAD else 0 for c in typ]
    art["type"] = [c or "일반" for c in typ]
    sdays = sorted(art.s.unique())
    print(f"[{mk}] 기사 {len(art):,} · 세션일 {len(sdays)} ({sdays[0]}~{sdays[-1]}) · 종목 {art.ticker.nunique()}", flush=True)

    ic = {lab: defaultdict(list) for lab in LABELS}
    combo_ic, equal_ic, weights_log, blocks = [], [], [], []
    start = INIT_DAYS
    while start < len(sdays):
        test_days = [d for d in sdays[start:start + STEP] if d <= LAST_TEST]
        if not test_days:
            break
        cut = sdays[max(0, start - EMBARGO)]
        tr, te = (art.s < cut).values, art.s.isin(test_days).values
        f_react = ridge_fit(V[tr], art.react.values[tr])
        f_fwd = ridge_fit(V[tr], art.fwd3.values[tr])
        Vtr, ytr = V[tr], art.fwd3.values[tr]
        sub = art[te].copy()
        Vte = V[te]
        sub["emb_react"], sub["emb_fwd"] = f_react(Vte), f_fwd(Vte)
        an = np.empty(len(Vte), dtype=np.float32)
        for i in range(0, len(Vte), 1000):
            sim = Vte[i:i + 1000] @ Vtr.T
            top = np.argpartition(-sim, K_ANALOG, axis=1)[:, :K_ANALOG]
            an[i:i + 1000] = ytr[top].mean(1)
        sub["analog"] = an
        g = sub.groupby(["ticker", "s"]).agg(
            emb_react=("emb_react", "mean"), emb_fwd=("emb_fwd", "mean"), analog=("analog", "mean"),
            lexicon=("lex", "mean"), react=("react", "first"), prior5=("prior5", "first"),
            fwd1=("fwd1", "first"), fwd3=("fwd3", "first"), fwd5=("fwd5", "first"),
            n=("n_arts", "first")).reset_index()
        g["diverge"] = g.emb_react - g.react
        g["attention"] = np.log1p(g.n)

        ts = {L: (tstat(ic["fwd3"][L])[1] or 0.0) for L in LENSES}
        pos = {L: max(t, 0.0) for L, t in ts.items()}
        tot = sum(pos.values())
        w = {L: (pos[L] / tot if tot > 0 else 1 / len(LENSES)) for L in LENSES}
        weights_log.append({"from": test_days[0], "hist_days": len(ic["fwd3"]["emb_react"]),
                            "w": {k: round(v, 3) for k, v in w.items()}})
        for d, gd in g.groupby("s"):
            if len(gd) < 5:
                continue
            z = {L: ((gd[L] - gd[L].mean()) / (gd[L].std() or 1)).fillna(0) for L in LENSES}
            combo_ic.append(spearman(sum(w[L] * z[L] for L in LENSES), gd.fwd3))
            equal_ic.append(spearman(sum(z[L] for L in LENSES) / len(LENSES), gd.fwd3))
            for lab in LABELS:
                for L in LENSES:
                    ic[lab][L].append(spearman(gd[L], gd[lab]))
        blocks.append(g)
        start += STEP

    G = pd.concat(blocks, ignore_index=True)
    res = {"articles": int(len(art)), "session_days": len(sdays), "window": [sdays[0], sdays[-1]],
           "oos_days": int(G.s.nunique()), "oos_rows": int(len(G)), "lenses": {}}
    for L in LENSES:
        spr = []
        for d, gd in G.groupby("s"):
            if len(gd) < 6:
                continue
            q = gd[L].rank(pct=True)
            spr.append(gd.fwd3[q > 2 / 3].mean() - gd.fwd3[q <= 1 / 3].mean())
        sm, st, _ = tstat(spr)
        row = {"spread3_pct": None if sm is None else sm * 100, "spread_t": st}
        for lab in LABELS:
            m, t, n = tstat(ic[lab][L])
            row[f"ic_{lab}"], row[f"t_{lab}"] = m, t
        row["days"] = n
        res["lenses"][L] = row
    # 전반부·후반부로 갈라 부호가 유지되나 (국면 안정성)
    half = sorted(G.s.unique())
    mid = half[len(half) // 2]
    for L in LENSES:
        a = [spearman(gd[L], gd.fwd3) for d, gd in G[G.s < mid].groupby("s") if len(gd) >= 5]
        b = [spearman(gd[L], gd.fwd3) for d, gd in G[G.s >= mid].groupby("s") if len(gd) >= 5]
        res["lenses"][L]["ic_first_half"] = tstat(a)[0]
        res["lenses"][L]["ic_second_half"] = tstat(b)[0]
    for name, arr in (("combo_auto", combo_ic), ("combo_equal", equal_ic)):
        m, t, n = tstat(arr)
        res[name] = {"ic": m, "t": t, "days": n}
    res["weights_log"] = weights_log
    T = art.groupby("type").agg(n=("h", "count"), react=("react", "mean"), fwd3=("fwd3", "mean"))
    T = T[T.n >= 40].sort_values("fwd3", ascending=False)
    res["by_type_in_sample"] = {k: {"n": int(r.n), "react_pct": r.react * 100, "fwd3_pct": r.fwd3 * 100}
                                for k, r in T.iterrows()}
    res["links_by_how"] = art.how.value_counts().to_dict()
    return res


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    con = _data.connect()
    cmean = _analog.corpus_mean()
    res = {"holdout_from": HOLDOUT, "last_test_session": LAST_TEST, "markets": {}}
    for mk in ("KR", "US"):
        res["markets"][mk] = run_market(con, mk, cmean)
        (OUT / "sim_20261031.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    for mk, r in res["markets"].items():
        print(f"\n[{mk}] 표본 밖 {r['oos_days']}일 · {r['oos_rows']}행 · 자동 {r['combo_auto']} · 동일 {r['combo_equal']}")
        for L, v in r["lenses"].items():
            f = lambda x: "  ·  " if x is None else f"{x:+.3f}"
            print(f"  {L:10s} IC1 {f(v['ic_fwd1'])} IC3 {f(v['ic_fwd3'])}(t {f(v['t_fwd3'])}) IC5 {f(v['ic_fwd5'])}"
                  f" | 3분위차 {f(v['spread3_pct'])}% | 전반 {f(v['ic_first_half'])} 후반 {f(v['ic_second_half'])}")
        print("  비중:", [(w["from"], w["hist_days"], {k: v for k, v in w["w"].items() if v >= 0.1}) for w in r["weights_log"]])


if __name__ == "__main__":
    main()
