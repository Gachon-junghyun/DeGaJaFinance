# -*- coding: utf-8 -*-
"""시뮬레이션 4회차 — 문장을 «데이터 조건»으로 바꿔 긴 역사로 잰다.

3회차(sim_phrase3d)에서 뉴스는 2026-05 부터라 문장마다 사건이 4~8번뿐이었다. «금리가 올랐다»는
뉴스 문장이기 전에 **데이터에서 일어난 일**이므로, 같은 문장을 시계열 조건으로 옮기면 2000년부터 잴 수 있다.

  문장 → 조건 (FRED 일별, 공개 CSV)
    금리가 올랐다(급등)   DGS10 하루 변화 ≥ +10bp      금리가 내렸다(급락)  ≤ −10bp
    유가가 올랐다(급등)   DCOILWTICO 하루 변화 ≥ +5%    유가가 내렸다(급락)  ≤ −5%
    달러가 올랐다         DTWEXBGS 하루 변화 ≥ +0.7%  (2006~)
  일어난 일 = 사건일 종가 기준 +1·+2·+3거래일 누적의 평균
    · S&P500(^GSPC) · 코스피(^KS11, 미국 사건일 «다음» 한국 거래일 종가부터 — 시차)
    · 미국 업종 ETF(XL*) − S&P500
  기준선 = 같은 기간 모든 날. 연달아 일어난 날은 첫날만(겹치는 창을 두 번 세지 않게).
  기간: 2000-01-01 ~ 2026-09-08 (뉴스 실험과 같은 holdout 선).

재현: `python -X utf8 lab/sim_dataevent_20261031.py` → out/news3d/dataevent_20261031.json
"""
from __future__ import annotations

import io
import json
import math
import pathlib

import numpy as np
import pandas as pd
import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "out" / "news3d"
START, LAST = "2000-01-01", "2026-09-08"
SECTORS = ["XLK", "XLF", "XLE", "XLU", "XLRE", "XLY", "XLP", "XLV", "XLI", "XLB", "XLC"]
NAMES = {"XLK": "기술", "XLF": "금융", "XLE": "에너지", "XLU": "유틸리티", "XLRE": "부동산", "XLY": "임의소비",
         "XLP": "필수소비", "XLV": "헬스케어", "XLI": "산업재", "XLB": "소재", "XLC": "통신"}


def fred(series: str) -> pd.Series:
    r = requests.get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}", timeout=60)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))
    df.columns = ["date", "v"]
    s = pd.to_numeric(df.v, errors="coerce")
    s.index = df.date
    return s.dropna()


def closes(tickers: list[str]) -> pd.DataFrame:
    import yfinance as yf
    df = yf.download(tickers, start=START, progress=False, auto_adjust=True, group_by="column", threads=True)
    c = df["Close"]
    c.index = [str(d)[:10] for d in c.index]
    return c


def fwd3(c: pd.Series) -> pd.Series:
    c = c.dropna()
    return sum(c.shift(-h) / c - 1 for h in (1, 2, 3)) / 3


def first_of_runs(days: list[str], all_days: list[str]) -> list[str]:
    pos = {d: i for i, d in enumerate(all_days)}
    out, last = [], -10
    for d in sorted(days):
        i = pos.get(d)
        if i is None:
            continue
        if i - last > 1:
            out.append(d)
        last = i
    return out


def effect(ev_days: list[str], s: pd.Series, shift_next: bool = False) -> dict | None:
    s = s.dropna()
    s = s[(s.index >= START) & (s.index <= LAST)]
    idx = list(s.index)
    vals = []
    for d in ev_days:
        if shift_next:                                   # 미국 사건 → 그 «다음» 한국 거래일
            j = np.searchsorted(idx, d, side="right")
        else:
            j = np.searchsorted(idx, d, side="left")
            if j < len(idx) and idx[j] != d:
                continue
        if j < len(idx):
            vals.append(s.iloc[j])
    if len(vals) < 10:
        return None
    base = float(s.mean())
    diff = np.array(vals) - base
    se = float(np.std(diff, ddof=1) / math.sqrt(len(diff)))
    return {"n": len(vals), "pct": float(diff.mean() * 100), "t": float(diff.mean() / se) if se > 0 else None,
            "hit": float((np.array(vals) > base).mean()), "base_pct": base * 100}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    y10, oil, usd = fred("DGS10"), fred("DCOILWTICO"), fred("DTWEXBGS")
    px = closes(["^GSPC", "^KS11"] + SECTORS)
    days = [d for d in px["^GSPC"].dropna().index if START <= d <= LAST]
    spx3 = fwd3(px["^GSPC"])
    ks3 = fwd3(px["^KS11"])
    sec3 = {s: fwd3(px[s]) - spx3 for s in SECTORS}

    dy = y10.diff() * 100                                  # bp
    do = oil.pct_change() * 100
    du = usd.pct_change() * 100
    conds = {
        "금리 급등(10년물 +10bp↑)": dy[dy >= 10].index, "금리 급락(10년물 −10bp↓)": dy[dy <= -10].index,
        "유가 급등(WTI +5%↑)": do[(do >= 5) & (do < 100)].index, "유가 급락(WTI −5%↓)": do[(do <= -5) & (do > -100)].index,
        "달러 급등(+0.7%↑)": du[du >= 0.7].index, "달러 급락(−0.7%↓)": du[du <= -0.7].index,
    }
    res = {"window": [START, LAST], "conditions": {}}
    for k, idx in conds.items():
        ev = first_of_runs([d for d in idx if START <= d <= LAST], days)
        row = {"events": len(ev), "spx": effect(ev, spx3), "kospi_next": effect(ev, ks3, shift_next=True),
               "sectors": {}}
        for s in SECTORS:
            e = effect(ev, sec3[s])
            if e:
                row["sectors"][f"{s} {NAMES[s]}"] = e
        # 최근 10년만 따로 — 오래된 관계가 지금도 맞나
        ev10 = [d for d in ev if d >= "2016-01-01"]
        row["spx_since2016"] = effect(ev10, spx3)
        res["conditions"][k] = row
        f = lambda e: "·" if not e else f"{e['pct']:+.2f}%p(t {e['t']:+.1f}, n {e['n']})"
        top = sorted(row["sectors"].items(), key=lambda kv: -abs(kv[1]["t"] or 0))[:4]
        print(f"{k}: 사건 {len(ev)} | S&P {f(row['spx'])} | 2016~ {f(row['spx_since2016'])} | 코스피 다음날부터 {f(row['kospi_next'])}")
        print("    업종(S&P 대비):", " · ".join(f"{s} {e['pct']:+.2f}%p(t {e['t']:+.1f})" for s, e in top))
    (OUT / "dataevent_20261031.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
