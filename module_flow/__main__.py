# -*- coding: utf-8 -*-
"""module_flow CLI — 티커들 → 흐름태그 테이블(+선택 포지셔닝).

    python -m module_flow NVDA GEV VRT MU ANET --bench SPY --json
    python -m module_flow NOW CCI CME --names "ServiceNow,Crown Castle,CME Group"
    python -m module_flow 005930.KS --names "삼성전자"    # KR = ⑦수급·⑧공매도 자동 조회
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime

import pandas as pd
import yfinance as yf

from ._config import OUT_DIR, utf8_stdout
from ._investor import investor_flow
from ._news_velocity import news_query, news_velocity
from ._price_flow import price_flow
from ._short import positioning, short_flow
from ._synthesize import flow_tag


def main() -> None:
    ap = argparse.ArgumentParser(prog="module_flow")
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--bench", default="SPY")
    ap.add_argument("--names", default=None, help="티커별 회사명 콤마구분(뉴스속도 매칭 보강; 'A|B' 동의어 가능)")
    ap.add_argument("--recent", type=int, default=7)
    ap.add_argument("--base", type=int, default=30)
    ap.add_argument("--positioning", action="store_true",
                    help="⑤공매도+⑥옵션(P/C·IV스큐) 추가 — 느림, 최종 후보(≤20)에만. 공매도는 캐싱.")
    ap.add_argument("--no-investor", action="store_true",
                    help="⑦투자자별 순매수(외국인/기관, KR·KIS) 비활성. 기본 ON(KR 티커만 자동, US 무영향).")
    ap.add_argument("--no-short", action="store_true",
                    help="⑧공매도잔고 비중(KR·KRX/pykrx, KRX_ID/PW 필요) 비활성. 기본 ON(KR만, 느림).")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    names = {}
    if a.names:
        for t, nm in zip(a.tickers, a.names.split(",")):
            names[t] = nm.strip()

    bdf = yf.download(a.bench, period="4mo", progress=False, auto_adjust=False)
    if isinstance(bdf.columns, pd.MultiIndex):
        bdf.columns = bdf.columns.get_level_values(0)
    bdf.columns = [str(c).lower() for c in bdf.columns]
    bench_close = bdf["close"].astype(float)

    rows = []
    for t in a.tickers:
        q = news_query(t, names.get(t))
        vel = news_velocity(q, a.recent, a.base)
        pf = price_flow(t, bench_close)
        inv = None if a.no_investor else investor_flow(t)
        sh = None if a.no_short else short_flow(t)
        tag = flow_tag(pf, vel.get("velocity"), inv, sh)
        pos = positioning(t, pf.get("last")) if (a.positioning and "error" not in pf) else None
        rows.append({"ticker": t, "tag": tag, "news": vel, "price": pf,
                     "investor": inv, "short_kr": sh, "positioning": pos})

    if a.json:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        fp = OUT_DIR / f"{datetime.now():%Y-%m-%d}.json"
        fp.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n# 수급·기대감 흐름 — {datetime.now():%Y-%m-%d}  (벤치 {a.bench}, 뉴스 {a.recent}d/{a.base}d)")
    print(f"  {'TICKER':<7}{'흐름':<8}{'뉴스속도':>8}{'OBV':>8}{'RS20':>7}{'RS60':>7}{'거래량서지':>9}")
    print("  " + "─" * 70)
    for r in rows:
        p, nv = r["price"], r["news"]
        if "error" in p:
            print(f"  {r['ticker']:<7}{'?':<8}  ({p['error']})")
            continue
        vel = nv.get("velocity")
        vels = "n/a" if vel is None else f"{vel:.2f}x"
        print(f"  {r['ticker']:<7}{r['tag']:<8}{vels:>8}{p['obv_state']:>8}{p['rs20']:>+6.1f}%{p['rs60']:>+6.1f}%{p['vol_surge']:>8.2f}x")
        iv = r.get("investor")
        if iv is not None:
            if "error" in iv:
                print(f"         ⑦ 수급(외/기/개): n/a ({iv['error']})")
            else:
                def _m(q):  # 주 → 만주
                    return f"{q/10000:+.1f}만"
                turn = " · 외국인5일 매수전환↑" if iv.get("foreign_turning") else ""
                print(f"         ⑦ 수급 {iv['days']}d(외/기/개): 외국인 {_m(iv['foreign_20'])} · "
                      f"기관 {_m(iv['inst_20'])} · 개인 {_m(iv['indiv_20'])} → {iv['state']}{turn}")
        sh = r.get("short_kr")
        if sh is not None:
            if "error" in sh:
                print(f"         ⑧ 공매도잔고: n/a ({sh['error']})")
            else:
                cw = " 🔥크라우디드" if sh.get("crowded") else (" ⚠주목" if sh.get("notable") else "")
                print(f"         ⑧ 공매도잔고: {sh['si_pct']}%float · {sh['trend']}({sh['chg']:+}){cw}")
        if r.get("positioning"):
            po = r["positioning"]; si = po["short"]; op = po["options"]
            dtc = si.get("days_to_cover")
            sf = "n/a" if si.get("pct_float") is None else f"{si['pct_float']}%float {si.get('trend','')}" + (f" DTC{dtc:.1f}" if dtc else "")
            pc = "n/a" if op.get("pc_oi") is None else f"P/C {op['pc_oi']}"
            sk = "n/a" if op.get("iv_skew") is None else f"스큐 {op['iv_skew']:+}"
            im = "" if op.get("implied_move_pct") is None else \
                f" · 예상변동 ±{op['implied_move_pct']}%(만기 {op.get('im_expiry','?')}, D{op.get('im_dte','?')})"
            print(f"         ⑤⑥ 포지셔닝: 숏 {sf}{' 🔥크라우디드' if si.get('crowded') else ''} · 옵션 {pc} {sk}{im} → {po['read']}")
    print("\n  뉴스속도>1=관심가속 · OBV 매집/분산 · RS=벤치대비(+면 이김) · 서지>1.3=돈유입")
    if any(r.get("investor") and "error" not in r["investor"] for r in rows):
        print("  ⑦수급=KIS 실측 외국인/기관/개인 순매수(만주,국내). 외국인 이탈+개인 흡수=OBV'매집'이 약한손→🟢 차단")
    if any(r.get("short_kr") and "error" not in r["short_kr"] for r in rows):
        print("  ⑧공매도잔고=KRX 실측 공매도잔고/상장주식수%(국내). building+주목(≥0.5%)=하락압력 · 크라우디드(≥2%) covering=스퀴즈연료")
    if any(r.get("positioning") for r in rows):
        print("  ⑤숏 %float·building/covering(크라우디드숏=스퀴즈연료) · ⑥옵션 P/C OI(>1.2 풋과다=공포)·IV스큐(+면 하방공포)")
    print("  ⚠️ 🟢가속이라도 진입은 하드스탑 필수(기대감=꼭지위험). 4Phase '바닥'과 교차해서 봐라.")
    if a.json:
        print(f"\n  JSON → {OUT_DIR / f'{datetime.now():%Y-%m-%d}.json'}")


if __name__ == "__main__":
    utf8_stdout()
    main()
