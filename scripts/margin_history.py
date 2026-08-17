# FILE: scripts/margin_history.py
"""
MARGIN_HISTORY — 장기 총이익률 시계열 (US: SEC XBRL · KR: DART 전체재무제표).

왜 (handoff/RESEARCH.md dig D2, 2026-07-22): lens L2(peak-margin / low-multiple trap)가
"현재 84.6% vs 직전 사이클 정점 59%"에 걸려 있었는데, 그 59% 는 **언론 인용**이지 우리 데이터가
아니었다. 사이클 종목의 마진이 자기 역사에서 어디쯤인지는 밸류에이션 판단의 전제라, 한 번 만들어
재사용한다("A multiple without a margin percentile is not a valuation").

⚠ XBRL 함정: companyfacts 의 `fy` 는 **제출연도**라 10-K 한 건에 비교연도가 같이 들어온다.
그대로 쓰면 매출·원가가 다른 기간끼리 짝지어져 총이익률이 −200% 로 나온다(실측). 그래서
**기간 길이(340~400일)로 연간만 남기고**, 같은 연도가 여러 번이면 가장 최근 제출본을 쓴다.

**KR 티커(6자리 숫자)는 자동감지해 DART 경로로 넘긴다**(P3 — 시장별 파일 미러 복제 금지).
D70: 이 스크립트가 KR 에서 "CIK not found" 로 죽어 DEEP 의 마진 백분위 게이트가 KR 에서
호출조차 되지 않았다. KR 구현은 `module_fundamentals_kr/_margin_history.py` — 그 파일 상단에
받아지는 기간·결측·함정이 실측으로 적혀 있다.

사용:
  python -X utf8 scripts/margin_history.py MU
  python -X utf8 scripts/margin_history.py MU --current 84.6 --json
  python -X utf8 scripts/margin_history.py 042700               # KR — DART 자동경로
  python -X utf8 scripts/margin_history.py 042700 --quarterly --current 57.6

결정론 산출물 — 판단은 하지 않는다(P4).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

_KR_CODE = re.compile(r"^\d{6}$")


def _load_dotenv() -> None:
    """DART_API_KEY 는 리포 .env 가 단일 원본(CLAUDE.md 시크릿 규약)."""
    for c in (ROOT / ".env", ROOT.parent / ".env"):
        if not c.exists():
            continue
        try:
            for line in c.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k and v and k not in os.environ:
                    os.environ[k] = v
        except Exception:
            pass
        break

# CIK 해석과 SEC UA 는 이미 단일 원본이 있다 — 재구현하지 않는다(P1).
# ⚠ sec.gov/files/company_tickers.json 을 직접 치면 403(실측). data.sec.gov 만 열려 있다.
from module_disclosure_us._ticker_cik import USER_AGENT, ticker_to_cik  # noqa: E402

# ⚠ Accept-Encoding 을 주지 않는다 — urllib 은 gzip 을 자동 해제하지 않아 UnicodeDecodeError 가 난다(실측).
UA = {"User-Agent": USER_AGENT}

REV_TAGS = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"]
COS_TAGS = ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold"]


def _get(url: str):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))


def cik_for(ticker: str) -> int | None:
    c = ticker_to_cik(ticker)
    return int(c) if c is not None else None


def annual(facts: dict, tags: list[str]) -> dict[int, float]:
    """end 연도 → 값. 기간 340~400일 행만(= 연간), 같은 연도면 최근 제출본."""
    best: dict[int, tuple[float, str]] = {}
    for t in tags:
        node = facts.get("facts", {}).get("us-gaap", {}).get(t)
        if not node:
            continue
        for unit, rows in node.get("units", {}).items():
            if unit != "USD":
                continue
            for r in rows:
                s, e = r.get("start"), r.get("end")
                if not s or not e:
                    continue
                dur = (_dt.date.fromisoformat(e) - _dt.date.fromisoformat(s)).days
                if not (340 <= dur <= 400):
                    continue
                y, filed = int(e[:4]), r.get("filed", "")
                if y not in best or filed > best[y][1]:
                    best[y] = (float(r["val"]), filed)
    return {y: v for y, (v, _) in best.items()}


def build(ticker: str) -> dict:
    cik = cik_for(ticker)
    if cik is None:
        return {"ticker": ticker, "error": "CIK not found"}
    f = _get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")
    rev, cos = annual(f, REV_TAGS), annual(f, COS_TAGS)
    series = []
    for y in sorted(set(rev) & set(cos)):
        if rev[y] <= 0:
            continue
        series.append({"fy": y, "revenue": rev[y], "gross_margin_pct": round((1 - cos[y] / rev[y]) * 100, 1)})
    return {"ticker": ticker, "cik": cik, "source": "SEC XBRL companyfacts", "series": series}


def main() -> int:
    ap = argparse.ArgumentParser(description="장기 총이익률 시계열 (SEC XBRL)")
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--current", type=float, default=None, help="현재 분기 총이익률(%) — 백분위 비교용")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quarterly", action="store_true",
                    help="KR 전용 — 분기(3개월) 시계열. Q4 는 연간−3분기누적 유도값")
    ap.add_argument("--start-year", type=int, default=2015, help="KR 전용 — 시작 사업연도 (기본 2015)")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    out = []
    for tk in a.tickers:
        # KR 6자리 코드는 DART 경로로. SEC 는 KR 종목을 모른다(D70).
        if _KR_CODE.match(tk):
            _load_dotenv()
            from module_fundamentals_kr import build_margin_history, render_text  # noqa: PLC0415

            d = build_margin_history(tk, start_year=a.start_year, quarterly=a.quarterly)
            out.append(d)
            if not a.json:
                print(render_text(d, current=a.current))
            continue

        d = build(tk)
        out.append(d)
        if a.json:
            continue
        if d.get("error"):
            print(f"{tk}: {d['error']}")
            continue
        s = d["series"]
        if not s:
            print(f"{tk}: 연간 데이터 없음")
            continue
        gms = [x["gross_margin_pct"] for x in s]
        print(f"\n# {tk} 연간 총이익률 — SEC XBRL ({len(s)}년, FY{s[0]['fy']}~{s[-1]['fy']})\n")
        print(f"{'FY':<6}{'매출($B)':>10}{'총이익률':>10}")
        for x in s:
            g = x["gross_margin_pct"]
            bar = "█" * max(0, int(g / 3)) if g > 0 else "▁" * max(1, int(-g / 3))
            print(f"{x['fy']:<6}{x['revenue']/1e9:10.1f}{g:9.1f}%   {bar}")
        hi = max(s, key=lambda x: x["gross_margin_pct"])
        lo = min(s, key=lambda x: x["gross_margin_pct"])
        med = sorted(gms)[len(gms) // 2]
        print(f"\n  최고 FY{hi['fy']} {hi['gross_margin_pct']}%  ·  최저 FY{lo['fy']} {lo['gross_margin_pct']}%  ·  중앙값 {med}%")
        if a.current is not None:
            pct = sum(1 for g in gms if g < a.current) / len(gms) * 100
            print(f"  ★ 현재 {a.current}% → 자기 역사 **{pct:.0f} 백분위**, 표본 최고 대비 {a.current - hi['gross_margin_pct']:+.1f}%p")
            print("     (lens L2 — 멀티플은 마진 백분위와 같이 읽어야 밸류에이션이 된다)")
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
