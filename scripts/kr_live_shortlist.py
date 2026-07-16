# -*- coding: utf-8 -*-
"""kr_live_shortlist — sector_flow 와이드 스윕 → LIVE shortlist → KIS 외국인/기관 순매수 실측.

2단계 발굴 파이프의 뒷단:
  ① (앞단) sector_flow --market kr : 전 유니버스 yfinance flow 스윕(KIS 0콜) → 🟢/🔴 태그
  ② (이 스크립트) 필터(유동성+🟢) → shortlist(~15) → **KIS 투자자별 순매수 실측**(shortlist에만)

왜: 와이드 스윕의 OBV는 '가격×거래량' 추론이라 외국인 매집인지 개인이 물량 받는지 못 가린다.
    무필터 wide 스윕은 뉴스 없는 얇은 소형주 +1.000 스파이크가 올라옴(아티팩트).
    → 유동성 플로어로 컷 + shortlist에만 KIS 실측(외국인/기관=스마트머니)을 붙여
      '진짜손(외국인/기관 순매수)' vs '약한손(개인 흡수)'을 최종 판정. KIS 부하 ~15콜뿐.

입력: llm_outputs/{today}/industry_KR/SECTOR_FLOW_KR.json (sector_flow --market kr --json 산출)
출력: stdout 리포트 + llm_outputs/{today}/industry_KR/KR_LIVE_SHORTLIST.json

사용:
  python -X utf8 scripts/kr_live_shortlist.py                       # 오늘 스윕 → shortlist
  python -X utf8 scripts/kr_live_shortlist.py --floor-jo 1.0 --top 15
  python -X utf8 scripts/kr_live_shortlist.py --in <sector_flow.json>
"""
from __future__ import annotations
import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import flow_read  # 엔진 재사용 — investor_flow(KIS 외국인/기관/개인)


def _man(qty) -> str:
    """주 → 만주 표기(부호 유지)."""
    if qty is None:
        return "n/a"
    return f"{qty/1e4:+.0f}만"


def main() -> int:
    ap = argparse.ArgumentParser()
    today = datetime.now().strftime("%Y-%m-%d")
    ap.add_argument("--in", dest="inp", default=None,
                    help="sector_flow --market kr --json 산출 경로(기본 오늘 SECTOR_FLOW_KR.json)")
    ap.add_argument("--floor-jo", type=float, default=1.0, help="시총 플로어(조원, 기본 1.0)")
    ap.add_argument("--top", type=int, default=15, help="shortlist 최대 종수")
    ap.add_argument("--tags", default="🟢가속", help="포함 태그(콤마, 기본 🟢가속)")
    ap.add_argument("--days", type=int, default=20, help="KIS 투자자 누적 일수")
    a = ap.parse_args()

    inp = Path(a.inp) if a.inp else ROOT / "llm_outputs" / today / "industry_KR" / "SECTOR_FLOW_KR.json"
    if not inp.exists():
        print(f"[err] 입력 없음: {inp} — sector_flow --market kr --json 먼저", file=sys.stderr)
        return 1
    d = json.loads(inp.read_text(encoding="utf-8"))
    names = d.get("names", [])
    asof = d.get("asof", today)

    # 이름 조인
    uni = ROOT / "data" / "kr_universe" / "kr_all.csv"
    nm = {r["ticker"]: r["name"] for r in csv.DictReader(open(uni, encoding="utf-8"))}

    floor = a.floor_jo * 1e12
    want_tags = set(a.tags.split(","))
    # 필터: 유동성 플로어 + 태그, flow_score desc
    cand = [n for n in names
            if n.get("flow_score") is not None
            and n.get("mcap", 0) >= floor
            and n.get("tag") in want_tags]
    cand.sort(key=lambda x: x["flow_score"], reverse=True)
    cand = cand[:a.top]

    if not cand:
        print(f"[info] 플로어 {a.floor_jo}조 · 태그 {want_tags} 통과 종목 0 "
              f"(플로어 낮추거나 태그 확장). 전체 🟢={sum(1 for n in names if n.get('tag')=='🟢가속')}",
              file=sys.stderr)
        return 0

    print(f"[info] shortlist {len(cand)}종 — KIS 투자자별 순매수 조회({a.days}일) …", file=sys.stderr)

    out_rows = []
    for n in cand:
        tk = n["ticker"]
        inv = flow_read.investor_flow(tk, days=a.days)  # KIS 실측(외국인/기관/개인)
        row = {
            "ticker": tk, "name": nm.get(tk, tk),
            "sector": n.get("sector", ""), "mcap_h": None,
            "flow_score": n.get("flow_score"), "tag": n.get("tag"),
            "velocity": n.get("velocity"), "obv_norm": n.get("obv_norm"),
            "rs20": n.get("rs20"), "rs60": n.get("rs60"), "vol_surge": n.get("vol_surge"),
            "investor": inv,
        }
        out_rows.append(row)

    # verdict: 🟢 AND 외국인/기관 순매수 = 진짜 LIVE
    def verdict(r):
        inv = r["investor"] or {}
        if not inv or "error" in inv:
            return "투자자 n/a"
        st = inv.get("state", "")
        if "순매수" in st:
            return "✅진짜손(외국인/기관 순매수)"
        if "개인 흡수" in st:
            return "❌약한손(개인 흡수·외국인 이탈)"
        return "△혼조"

    # 리포트
    L = []
    L.append(f"# KR LIVE SHORTLIST — 와이드스윕→필터→KIS 실측  (asof {asof})")
    L.append(f"필터: 시총≥{a.floor_jo}조 · 태그 {'/'.join(want_tags)} · flow_score desc top{a.top} "
             f"→ {len(cand)}종 · KIS 투자자 {a.days}일 누적")
    L.append("")
    L.append(f"{'TICKER':<11}{'종목':<10}{'flow':>6}{'뉴스':>6}{'OBV':>6}{'RS20':>6}"
             f"{'외국인':>8}{'기관':>8}{'개인':>8}  판정")
    for r in out_rows:
        inv = r["investor"] or {}
        vel = f"{r['velocity']:.2f}" if r.get("velocity") is not None else "n/a"
        fg = _man(inv.get("foreign_20")) if inv and "error" not in inv else "n/a"
        ig = _man(inv.get("inst_20")) if inv and "error" not in inv else "n/a"
        pg = _man(inv.get("indiv_20")) if inv and "error" not in inv else "n/a"
        L.append(f"{r['ticker']:<11}{r['name'][:9]:<10}{r['flow_score']:>+6.2f}{vel:>6}"
                 f"{r.get('obv_norm',0):>+6.2f}{str(r.get('rs20','')):>6}"
                 f"{fg:>8}{ig:>8}{pg:>8}  {verdict(r)}")
    # 진짜 LIVE
    live = [r for r in out_rows if "진짜손" in verdict(r)]
    L.append("")
    if live:
        L.append("★ 진짜 LIVE (🟢 AND 외국인/기관 순매수): "
                 + ", ".join(f"{r['name']}({r['ticker']})" for r in live))
    else:
        L.append("★ 진짜 LIVE 없음 — 🟢가속이나 외국인/기관 실측 미확인(약한손/혼조).")
    L.append("\n해석: 외국인+기관 순매수(진짜손) = OBV '매집'을 실측 확증 · 개인 흡수(약한손) = 🟢를 무효화(꼭지위험).")
    report = "\n".join(L)
    print(report)

    outp = inp.parent / "KR_LIVE_SHORTLIST.json"
    outp.write_text(json.dumps({"asof": asof, "filter": {"floor_jo": a.floor_jo, "tags": list(want_tags),
                    "top": a.top, "days": a.days}, "shortlist": out_rows,
                    "live": [r["ticker"] for r in live]}, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    print(f"\n[saved] {outp}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
