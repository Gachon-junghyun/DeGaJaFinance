# FILE: scripts/measure_ic.py
"""
MEASURE_IC — 신호의 정보계수(IC)를 **가정이 아니라 측정**으로 만든다.

왜 (2026-07-22): `scripts/kelly_size.py` 가 `--ic` 를 사람에게서 받는다. 근거 없는 IC 는 근거 없는
크기를 낳으므로, 최소한 하나의 축은 재서 눈금을 만들어야 한다. lab 에 이미 측정된 것은 외국인 수급
(좋았던 부분표본 0.33~0.44 · 앞 18개월 ≈0.015)뿐이고, **오늘 추가한 추정치 리비전 축은 미측정**이었다.

측정 설계 — 추정치 리비전 → 선행 초과수익:
  신호   s_i = (60일전 추정치 / 90일전 추정치 − 1)      … 90→60 구간의 리비전
  타깃   r_i = 60일전 → 오늘 수익률 − 벤치마크 같은 구간 … 겹치지 않는 선행 구간
  IC     = 횡단면 스피어만 상관(s, r)

⚠ **정직한 한계 — 규칙 S3(검정력 먼저) 를 여기 그대로 적용한다.**
yfinance `eps_trend` 는 시계열이 아니라 **스냅샷**(현재/7·30·60·90일전 수준)이라, 겹치지 않는
관측 구간이 사실상 **1개**뿐이다. 즉 이 측정은 "한 시점의 횡단면 IC" 이고 유효 표본은 **날짜 1개**다.
  · 횡단면 SE ≈ 1/√(n−1)  → n=80 이면 SE ≈ 0.11, 즉 |IC|<0.22 는 구분 불가
  · lab 규칙 S1(날짜로 접어라) 상 **유효 n 은 종목 수가 아니라 날짜 수** — 여기선 1
따라서 결과는 **[측정됨, 단일시점]** 으로만 태깅하고, kelly_size 의 --ic 근거로 쓸 때
`--ic-n` 에 종목 수를 넣으면 안 된다(그건 날짜 수를 부풀리는 것). 시계열로 쌓으려면 eps_trend 를
매일 스냅샷해 저장해야 한다 → dig D16.

사용:
  python -X utf8 scripts/measure_ic.py --universe us_top300 --limit 80
  python -X utf8 scripts/measure_ic.py --tickers MU,NVDA,AMD,... --json
결정론 산출 — 판단은 하지 않는다(P4).
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _universe(name: str, limit: int) -> list[str]:
    f = ROOT / "data" / "us_universe" / f"{name}.csv"
    if not f.exists():
        return []
    out = []
    for r in csv.DictReader(f.open(encoding="utf-8")):
        t = (r.get("ticker") or "").strip().upper()
        if t:
            out.append(t)
    return out[:limit]


def collect(tickers: list[str], bench: str, verbose: bool = True) -> list[dict]:
    import warnings
    warnings.filterwarnings("ignore")
    import numpy as np
    import yfinance as yf

    # 가격은 한 번에 — 90거래일 넘게 확보
    px = yf.download(tickers + [bench], period="8mo", interval="1d",
                     auto_adjust=True, progress=False)["Close"].dropna(how="all")
    if bench not in px.columns:
        return []
    b = px[bench].dropna()
    if len(b) < 65:
        return []
    # 60거래일 전 → 오늘 벤치마크 수익
    bret = float(b.iloc[-1] / b.iloc[-61] - 1)

    rows = []
    for i, t in enumerate(tickers, 1):
        if verbose and i % 20 == 0:
            sys.stderr.write(f"  [{i}/{len(tickers)}]\n")
        try:
            tr = yf.Ticker(t).eps_trend
            if tr is None or tr.empty or "+1y" not in tr.index:
                continue
            row = tr.loc["+1y"]
            e90, e60 = row.get("90daysAgo"), row.get("60daysAgo")
            if e90 is None or e60 is None or not np.isfinite([e90, e60]).all() or e90 == 0:
                continue
            signal = float(e60) / float(e90) - 1.0          # 90→60 구간 리비전
            if t not in px.columns:
                continue
            s = px[t].dropna()
            if len(s) < 65:
                continue
            fwd = float(s.iloc[-1] / s.iloc[-61] - 1)        # 60일전 → 오늘
            rows.append({"ticker": t, "signal": signal, "fwd_excess": fwd - bret})
        except Exception:
            continue
    return rows


def quintile_concentration(group: list[dict]) -> dict | None:
    """상위분위가 한 섹터에 몰렸는지 — 독립 관측 수를 부풀리지 않기 위한 점검."""
    import collections
    f = ROOT / "data" / "us_universe" / "us_top300.csv"
    if not f.exists() or not group:
        return None
    sec = {r["ticker"].strip().upper(): r.get("gics_sector", "?")
           for r in csv.DictReader(f.open(encoding="utf-8"))}
    c = collections.Counter(sec.get(g["ticker"], "?") for g in group)
    top, cnt = c.most_common(1)[0]
    return {"top_sector": top, "top_n": cnt, "top_share": cnt / len(group),
            "breakdown": dict(c)}


def spearman(x: list[float], y: list[float]) -> float:
    import numpy as np
    def rank(v):
        o = np.argsort(np.argsort(np.asarray(v, dtype=float)))
        return o.astype(float)
    rx, ry = rank(x), rank(y)
    rx -= rx.mean(); ry -= ry.mean()
    d = math.sqrt(float((rx**2).sum()) * float((ry**2).sum()))
    return float((rx * ry).sum() / d) if d else 0.0


def main() -> int:
    ap = argparse.ArgumentParser(description="신호 IC 측정 (추정치 리비전 → 선행 초과수익)")
    ap.add_argument("--universe", default="us_top300")
    ap.add_argument("--tickers", default=None, help="쉼표구분; 주면 universe 무시")
    ap.add_argument("--limit", type=int, default=80)
    ap.add_argument("--bench", default="SPY")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    tks = [t.strip().upper() for t in a.tickers.split(",")] if a.tickers else _universe(a.universe, a.limit)
    if not tks:
        print("유니버스 비어 있음", file=sys.stderr)
        return 2

    # ── 규칙 S3: 재기 전에 검정력부터 ─────────────────────────────
    n_planned = len(tks)
    se_planned = 1 / math.sqrt(max(n_planned - 1, 1))
    # --json 일 때 전문(前文)이 stdout 을 오염시키면 파싱이 깨진다 → stderr 로 보낸다(실측 결함).
    _out = (lambda *x: print(*x, file=sys.stderr)) if a.json else print
    _out(f"# MEASURE_IC — 추정치 리비전(90→60일) → 선행 초과수익(60일→오늘), 벤치 {a.bench}\n")
    _out("■ 규칙 S3 — 재기 전에 검정력부터")
    _out(f"   계획 표본 {n_planned}종목 → 횡단면 SE ≈ {se_planned:.3f}")
    _out(f"   → **|IC| < {1.96*se_planned:.2f} 는 0 과 구분 불가**")
    _out("   ⚠ 그리고 규칙 S1(날짜로 접어라): eps_trend 는 스냅샷이라 겹치지 않는 관측 구간이")
    _out("     사실상 **1개**다. 유효 표본은 종목 수가 아니라 **날짜 1개** — 아래 SE 는 하한이다.\n")

    rows = collect(tks, a.bench)
    n = len(rows)
    if n < 10:
        print(f"수집 {n}건 — 너무 적어 측정 불가(P4: 빈칸이 거짓보다 낫다)")
        return 0

    sig = [r["signal"] for r in rows]
    fwd = [r["fwd_excess"] for r in rows]
    ic = spearman(sig, fwd)
    se = 1 / math.sqrt(n - 1)
    lo, hi = ic - 1.96 * se, ic + 1.96 * se

    # 5분위
    order = sorted(rows, key=lambda r: r["signal"])
    q = max(1, n // 5)
    q1 = sum(r["fwd_excess"] for r in order[:q]) / q * 100
    q5 = sum(r["fwd_excess"] for r in order[-q:]) / q * 100

    if a.json:
        print(json.dumps({"n": n, "ic": ic, "se": se, "ci": [lo, hi],
                          "q1_pct": q1, "q5_pct": q5, "rows": rows},
                         ensure_ascii=False, indent=2))
        return 0

    # ── 집중도 점검 — 규칙 S1 의 정신을 '날짜' 가 아니라 '상관단위' 에 적용 ──
    # 횡단면 SE 는 90종목을 **독립** 관측으로 센다. 상위분위가 한 섹터에 몰려 있으면
    # 실제 독립 관측은 종목 수가 아니라 그 테마 블록 수에 가깝다.
    conc = quintile_concentration(order[-q:])
    print(f"■ 결과  (수집 {n}/{n_planned}종목)")
    print(f"   IC(스피어만) = **{ic:+.3f}**   SE {se:.3f}   95% CI [{lo:+.3f}, {hi:+.3f}]")
    naive = "구분 불가 (CI 가 0 포함)" if lo <= 0 <= hi else ("양(+)" if lo > 0 else "음(−)")
    print(f"   횡단면 CI 만 보면: {naive}")
    if conc and conc["top_share"] >= 0.5:
        print(f"   ⚠ **그러나 Q5 의 {conc['top_share']*100:.0f}% 가 단일 섹터({conc['top_sector']})다.**")
        print("   → 90종목은 독립 관측이 아니다. 상위분위가 한 테마면 이 IC 는 '리비전이 수익을")
        print("     예측한다' 가 아니라 '그 테마가 추정치와 주가에 **동시에** 나타났다' 일 수 있다.")
        print("   → **최종 판정: 구분 불가 (단일 테마 집중).** 규칙 C4 대로 '효과 없음' 이 아니라")
        print("     '이 표본으로는 구분 못 한다' 로 적는다. 규칙 S1 의 '날짜로 접어라' 가 여기선")
        print("     '상관단위로 접어라' 로 적용된다 — 접을 날짜가 1개라 접을 수조차 없다.")
    else:
        print(f"   판정: **{naive}**")
    print(f"\n   5분위 선행 초과수익  Q1(리비전 최저) {q1:+.1f}%  ·  Q5(최고) {q5:+.1f}%  ·  Q5−Q1 {q5-q1:+.1f}%p")

    print("\n■ 이 숫자를 쓸 때의 규칙")
    if lo <= 0 <= hi:
        print("   · CI 가 0 을 포함한다 → **'효과 없음'이 아니라 '구분 불가'** 로 적는다(규칙 C4).")
    print("   · 태그 **[측정됨, 단일시점]**. kelly_size 의 --ic-n 에 **종목 수를 넣지 마라** —")
    print("     그건 날짜 수를 부풀리는 것이고, 규칙 S1 위반이다. 겹치지 않는 관측 날짜는 1개다.")
    print("   · 시계열로 쌓으려면 eps_trend 를 매일 스냅샷해 저장해야 한다 → dig D16.")
    print("   · 이 결과는 US 에서 잰 것이다. KR 로 옮기려면 자체 재현이 필요하다(규칙 W1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
