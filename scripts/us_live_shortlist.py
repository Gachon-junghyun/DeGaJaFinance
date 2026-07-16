# -*- coding: utf-8 -*-
"""us_live_shortlist — sector_flow wide sweep → LIVE shortlist → us_flow FINRA short/COT enrich.

Back half of the 2-stage US discovery pipe (mirror of kr_live_shortlist, US-adapted):
  ① (front) sector_flow.py --json  : whole-universe yfinance flow sweep → 🟢/🔴 tags
  ② (this)  filter(liquidity+🟢) → shortlist(~15) → **us_flow FINRA short z-score** on shortlist only

Why: the wide sweep's OBV is a price×volume inference. A liquidity floor kills thin +1.000
     spikes. Then us_flow adds the order-flow tell the sweep can't see — but note **the US has
     NO investor-type (foreign/institution) feed** (unlike KR/KIS), so the enrichment here is
     FINRA daily short-vol z-score (short pressure easing/building), a positioning proxy, not
     a smart-money net-buy. Crowded-short is turn-conditional (squeeze fuel IF a turn), not a
     standalone buy. Keep expectations honest.

Input : llm_outputs/{today}/industry_US/SECTOR_FLOW_US.json (sector_flow --json)
Output: stdout report + llm_outputs/{today}/industry_US/US_LIVE_SHORTLIST.json

Usage:
  python -X utf8 scripts/us_live_shortlist.py
  python -X utf8 scripts/us_live_shortlist.py --floor-b 10 --top 15
"""
from __future__ import annotations
import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser()
    today = datetime.now().strftime("%Y-%m-%d")
    ap.add_argument("--in", dest="inp", default=None,
                    help="sector_flow --json output (default today's SECTOR_FLOW_US.json)")
    ap.add_argument("--floor-b", type=float, default=10.0, help="market-cap floor in $B (default 10)")
    ap.add_argument("--top", type=int, default=15, help="max shortlist size")
    ap.add_argument("--tags", default="🟢가속", help="include tags (comma)")
    a = ap.parse_args()

    inp = Path(a.inp) if a.inp else ROOT / "llm_outputs" / today / "industry_US" / "SECTOR_FLOW_US.json"
    if not inp.exists():
        print(f"[err] input missing: {inp} — run sector_flow.py --json first", file=sys.stderr)
        return 1
    d = json.loads(inp.read_text(encoding="utf-8"))
    names = d.get("names", [])
    asof = d.get("asof", today)

    uni = ROOT / "data" / "us_universe" / "us_top300.csv"
    nm = {r["ticker"]: r["name"] for r in csv.DictReader(open(uni, encoding="utf-8"))}

    floor = a.floor_b * 1e9
    want = set(a.tags.split(","))
    cand = [n for n in names if n.get("flow_score") is not None
            and n.get("mcap", 0) >= floor and n.get("tag") in want]
    cand.sort(key=lambda x: x["flow_score"], reverse=True)
    cand = cand[:a.top]
    if not cand:
        print(f"[info] 0 names pass floor ${a.floor_b}B + tag {want}. total 🟢="
              f"{sum(1 for n in names if n.get('tag')=='🟢가속')}", file=sys.stderr)
        return 0

    tickers = [c["ticker"] for c in cand]
    print(f"[info] shortlist {len(tickers)} — us_flow FINRA short z-score …", file=sys.stderr)
    # us_flow enrichment (한 번에 여러 티커)
    short_by = {}
    try:
        r = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts" / "us_flow.py"),
                            *tickers, "--json"], capture_output=True, text=True, timeout=180)
        js = json.loads(r.stdout or "{}")
        for s in js.get("short", []):
            short_by[s.get("ticker")] = s
    except Exception as e:  # noqa
        print(f"[warn] us_flow 실패: {str(e)[:60]}", file=sys.stderr)

    def verdict(sh):
        if not sh or sh.get("z_score") is None:
            return "숏 n/a"
        z = sh["z_score"]
        if z >= 1.5:
            return "⚡crowded-short (스퀴즈연료·턴조건)"
        if z <= -0.5:
            return "✅저숏/숏커버 (청정 상승)"
        return "△정상숏"

    L = []
    L.append(f"# US LIVE SHORTLIST — wide sweep→filter→us_flow FINRA short  (asof {asof})")
    L.append(f"filter: mcap≥${a.floor_b}B · tag {'/'.join(want)} · flow desc top{a.top} → {len(cand)} names")
    L.append("⚠️ US엔 투자자별(외국인/기관) 피드 없음 → 숏압력(FINRA z) proxy. crowded-short=턴조건 스퀴즈연료(단독 매수 아님).")
    L.append("")
    L.append(f"{'TICKER':<7}{'name':<20}{'flow':>6}{'news':>6}{'OBV':>6}{'RS20':>6}{'shortZ':>7}  verdict")
    out_rows = []
    for c in cand:
        tk = c["ticker"]; sh = short_by.get(tk)
        vel = f"{c['velocity']:.2f}" if c.get("velocity") is not None else "n/a"
        z = f"{sh['z_score']:+.2f}" if sh and sh.get("z_score") is not None else "n/a"
        L.append(f"{tk:<7}{nm.get(tk,'')[:19]:<20}{c['flow_score']:>+6.2f}{vel:>6}"
                 f"{c.get('obv_norm',0):>+6.2f}{str(c.get('rs20','')):>6}{z:>7}  {verdict(sh)}")
        out_rows.append({**c, "name": nm.get(tk, tk), "short": sh, "verdict": verdict(sh)})

    live = [r for r in out_rows if "청정" in r["verdict"]]
    L.append("")
    L.append("★ 청정 상승 (🟢 AND 저숏/숏커버): " +
             (", ".join(f"{r['name']}({r['ticker']})" for r in live) if live else "none"))
    squeeze = [r for r in out_rows if "crowded-short" in r["verdict"]]
    if squeeze:
        L.append("⚡ crowded-short 스퀴즈연료(턴조건): " +
                 ", ".join(f"{r['ticker']}" for r in squeeze))
    L.append("\n해석: 저숏/숏커버=상방 청정 · crowded-short=턴 확인 시 스퀴즈연료(단독 매수 X) · US는 '누가 사나' 실측 부재(KR KIS 대비 약점).")
    print("\n".join(L))

    outp = inp.parent / "US_LIVE_SHORTLIST.json"
    outp.write_text(json.dumps({"asof": asof, "filter": {"floor_b": a.floor_b, "top": a.top},
                    "shortlist": out_rows, "clean": [r["ticker"] for r in live],
                    "squeeze": [r["ticker"] for r in squeeze]}, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    print(f"\n[saved] {outp}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
