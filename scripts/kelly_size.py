# FILE: scripts/kelly_size.py
"""
KELLY_SIZE — 확실성을 기다리는 대신 **불확실성을 사이즈에 넣는** 계산기.

왜 (PLAY28, 2026-07-22 배선): 데스크의 기존 사이저(`module_paper_book._risk.size_position`)는
**스탑 거리**로만 크기를 정한다 — 자본의 1.5% 를 걸고 스탑이 7% 면 비중 ≈ 21%. 변동성도, 엣지의
질도, 그 엣지 추정의 오차도 들어가지 않는다. 그래서 연변동성 40% 종목과 160% 종목이 같은 크기가 된다.

이 스크립트가 채우는 빈칸 = **엣지(IC) × 신호강도(z) × 변동성(σ) × 그 IC 추정의 오차.**

PLAY28 실측이 이 계산의 근거다:
  · full Kelly 는 IC 추정오차 CI 하한으로 재계산하면 **13% 로 쪼그라든다(8배 축소)**
  · full Kelly 는 **in-sample 에서조차 손실** — 연 −5%, MDD −71%
  · 권고 **1/4 Kelly** — 이상 성장률의 ~44% 확보 + 안전마진 4배
  · 무거래 밴드 **신호 z 1.5σ** — 턴오버 1.32→0.44, 비용 드래그 7.8%→2.7%/년
    ⚠ 공짜 아님: 뒤집힘 국면에서 MDD 악화(−32%→−52%)

수학:  μ = IC · z · σ   →   f* = μ/σ² = **IC · z / σ**   (σ 는 보유기간 변동성)
       IC 표준오차 ≈ 1/√n  →  IC_lower = IC − 1.96/√n  →  f*_lower

사용:
  python -X utf8 scripts/kelly_size.py MU 005930.KS --ic 0.05 --ic-n 200 --z 1.0
  python -X utf8 scripts/kelly_size.py MU --ic 0.05 --ic-n 2000 --equity 10000000 --json

⚠ **매매 권유가 아니다.** 이 스크립트는 "이만큼 확신하면 이만한 크기가 수학적으로 정합한가"만
계산한다. IC 와 z 는 **사람이 넣는 가정**이지 측정값이 아니다 — 근거 없는 IC 를 넣으면 근거 없는
크기가 나온다. 실제 집행은 사람이 한다(P4·드라이런 원칙).
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# PLAY28 실측 상수 — 여기서만 정의한다(P1).
KELLY_FRACTION = 0.25          # 권고 1/4 Kelly
BAND_SIGMA = 1.5               # 무거래 밴드 = 신호 z 1.5σ
FULL_KELLY_INSAMPLE_CAGR = -5.0
FULL_KELLY_INSAMPLE_MDD = -71.0

# lab 참고 IC — 사람이 자기 IC 를 넣을 때 눈금이 되라고 박아둔다.
IC_REFERENCE = [
    ("외국인 순매수 (좋았던 부분표본, 전력기기 2종목)", "0.33 ~ 0.44"),
    ("외국인 순매수 (앞 18개월)", "≈ 0.015 — 사실상 0. 비정상 신호"),
    ("현실적인 좋은 팩터의 연 샤프", "0.3 ~ 1.0"),
]


def realized_vol(ticker: str, hold_days: int, lookback: str = "2y") -> dict:
    import warnings
    warnings.filterwarnings("ignore")
    import numpy as np
    import yfinance as yf

    px = yf.download(ticker, period=lookback, interval="1d", auto_adjust=True,
                     progress=False)["Close"].dropna()
    if hasattr(px, "columns"):
        px = px.iloc[:, 0]
    if len(px) < 60:
        return {"error": "가격 데이터 부족"}
    r = np.log(px).diff().dropna()
    sd = float(r.std())
    # 팻테일 — lab 법칙 4(Hill α≈3): 정규분포는 꼬리를 체계적으로 과소평가한다.
    obs2 = float((r.abs() > 2 * sd).mean()) * 100
    return {
        "last": float(px.iloc[-1]),
        "sigma_daily": sd,
        "sigma_annual": sd * math.sqrt(252),
        "sigma_hold": sd * math.sqrt(hold_days),
        "beyond_2sd_pct": obs2,          # 정규분포 기대 4.55%
        "n_days": int(len(r)),
    }


def kelly(ic: float, z: float, sigma_hold: float) -> float:
    """f* = IC·z/σ  (σ 는 보유기간 변동성). 음수는 0 으로 자른다(롱 전용 가정)."""
    if sigma_hold <= 0:
        return 0.0
    return max(0.0, ic * z / sigma_hold)


def ic_lower_bound(ic: float, n: int, conf: float = 1.96) -> float:
    """IC 자체가 추정치다. SE ≈ 1/√n."""
    if n <= 1:
        return float("-inf")
    return ic - conf / math.sqrt(n)


def n_needed(ic: float, keep: float = 0.13, conf: float = 1.96) -> float:
    """IC 하한이 IC 의 keep 배 이상으로 남으려면 관측치가 몇 개 필요한가."""
    if ic <= 0 or keep >= 1:
        return float("inf")
    return (conf / (ic * (1 - keep))) ** 2


def analyse(ticker: str, ic: float, n: int, z: float, hold_days: int,
            equity: float | None, stop_pct: float, max_pos_pct: float) -> dict:
    v = realized_vol(ticker, hold_days)
    if "error" in v:
        return {"ticker": ticker, **v}
    sh = v["sigma_hold"]
    f_full = kelly(ic, z, sh)
    ic_lo = ic_lower_bound(ic, n)
    f_lo = kelly(ic_lo, z, sh)
    f_q = f_full * KELLY_FRACTION
    shrink = (f_lo / f_full * 100) if f_full > 0 else 0.0

    out = {
        "ticker": ticker, "price": v["last"],
        "sigma_daily_pct": v["sigma_daily"] * 100,
        "sigma_annual_pct": v["sigma_annual"] * 100,
        "sigma_hold_pct": sh * 100,
        "beyond_2sd_pct": v["beyond_2sd_pct"],
        "ic": ic, "ic_lower": ic_lo, "z": z, "hold_days": hold_days,
        "f_full_pct": f_full * 100,
        "f_ic_lower_pct": f_lo * 100,
        "f_quarter_pct": f_q * 100,
        "ic_lower_shrink_pct": shrink,
        "n_obs": n, "n_needed_for_13pct": n_needed(ic),
        # 무거래 밴드 = **신호 z 가 1.5 움직여야** 재조정. 이건 신호 공간의 단위이지 가격이 아니다.
        # 가격 환산은 신호가 가격 기반(모멘텀·RS)일 때만 성립한다 — 수급·추정치 리비전 같은
        # 신호에는 그대로 쓰면 안 된다(단위 혼동). 참고치로만 내보내고 라벨에 조건을 붙인다.
        "band_signal_z": BAND_SIGMA,
        "band_price_equiv_pct": BAND_SIGMA * sh * 100,
    }
    # 상한 적용 + 자본 환산
    capped = min(f_q * 100, max_pos_pct)
    out["f_final_pct"] = capped
    out["capped_by_max_pos"] = capped < f_q * 100
    if equity:
        out["notional"] = equity * capped / 100
        out["shares"] = out["notional"] / v["last"] if v["last"] else None
        # 기존 스탑기반 사이저와 교차확인 (P1: 재구현하지 않고 그 규칙을 그대로 적용)
        stop_based = equity * 1.5 / stop_pct        # risk_pct 1.5 / stop 7 → 자본의 21%
        out["stop_based_notional"] = stop_based
        out["stop_based_pct"] = stop_based / equity * 100
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="1/4 Kelly + 무거래 밴드 사이징 (참고용, 매매 권유 아님)")
    ap.add_argument("tickers", nargs="+", help="KR 은 .KS 접미사 필수")
    ap.add_argument("--ic", type=float, required=True, help="정보계수 가정 (예 0.05)")
    ap.add_argument("--ic-n", type=int, default=200, help="그 IC 를 추정한 관측치 수")
    ap.add_argument("--z", type=float, default=1.0, help="현재 신호 강도(표준화)")
    ap.add_argument("--hold-days", type=int, default=20, help="보유기간(거래일)")
    ap.add_argument("--equity", type=float, default=None, help="자본(원/달러) — 넣으면 금액 환산")
    ap.add_argument("--stop-pct", type=float, default=7.0)
    ap.add_argument("--max-pos-pct", type=float, default=25.0)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    rows = [analyse(t, a.ic, a.ic_n, a.z, a.hold_days, a.equity, a.stop_pct, a.max_pos_pct)
            for t in a.tickers]
    if a.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2, default=str))
        return 0

    print(f"# KELLY_SIZE — IC={a.ic} (n={a.ic_n}) · z={a.z} · 보유 {a.hold_days}거래일")
    print(f"  f* = IC·z/σ · 권고 1/4 Kelly · 무거래 밴드 {BAND_SIGMA}σ   [PLAY28]\n")

    ic_lo = ic_lower_bound(a.ic, a.ic_n)
    print(f"■ 먼저 — 당신의 IC 자체가 추정치다")
    print(f"   IC {a.ic:.3f} · 관측 {a.ic_n}개 → 표준오차 ≈ {1/math.sqrt(max(a.ic_n,1)):.3f}")
    print(f"   95% 신뢰구간 하한 IC = **{ic_lo:+.3f}**", end="")
    if ic_lo <= 0:
        print("  ← 0 이하. **이 표본으로는 엣지의 부호조차 확립 못 한다.**")
        print(f"   → full Kelly 는 정당화 불가. 하한이 IC 의 13%라도 남으려면 관측치 **{n_needed(a.ic):,.0f}개** 필요.")
    else:
        print(f"  (원 IC 의 {ic_lo/a.ic*100:.0f}%)")
    print()

    for r in rows:
        if "error" in r:
            print(f"  {r['ticker']}: {r['error']}\n")
            continue
        print(f"── {r['ticker']}  (가격 {r['price']:,.2f})")
        print(f"   변동성   일 {r['sigma_daily_pct']:.2f}% · 연 {r['sigma_annual_pct']:.0f}% · "
              f"{a.hold_days}일 {r['sigma_hold_pct']:.1f}%")
        tail = r["beyond_2sd_pct"]
        flag = " ⚠ 정규분포 기대 4.55% 초과 — 팻테일(lab 법칙 4)" if tail > 5.5 else ""
        print(f"   2σ 초과일 {tail:.1f}%{flag}")
        print(f"   Kelly    full {r['f_full_pct']:6.1f}%  →  IC하한 {r['f_ic_lower_pct']:5.1f}%"
              f"  →  **1/4 Kelly {r['f_quarter_pct']:.1f}%**")
        if r["capped_by_max_pos"]:
            print(f"            ↳ 단일종목 상한 {a.max_pos_pct}% 적용 → **{r['f_final_pct']:.1f}%**")
        print(f"   무거래밴드  **신호 z 가 {BAND_SIGMA} 움직여야** 재조정 "
              f"(턴오버 1.32→0.44, 드래그 7.8→2.7%/년)")
        print(f"              ↳ 신호가 가격기반(모멘텀·RS)일 때만 가격 ±{r['band_price_equiv_pct']:.1f}% 에 해당. "
              f"수급·추정치 리비전 신호엔 그대로 쓰지 말 것(단위 다름)")
        if a.equity:
            print(f"   자본 환산  {r['notional']:,.0f}  ({r['shares']:,.2f}주)")
            if r["shares"] is not None and r["shares"] < 1:
                print(f"              ⚠ **1주 미만** — 이 자본에서 이 종목은 권고 크기로 살 수 없다. "
                      f"1주 = {r['price']:,.0f} = 자본의 {r['price']/a.equity*100:.1f}%. "
                      f"강행하면 사이징 규율이 아니라 최소단위가 크기를 정하게 된다")
            print(f"   교차확인   기존 스탑기반 사이저(위험1.5%/스탑{a.stop_pct}%) = "
                  f"{r['stop_based_pct']:.1f}% = {r['stop_based_notional']:,.0f}")
            gap = r["stop_based_pct"] - r["f_final_pct"]
            if abs(gap) > 3:
                who = "스탑기반이 더 큼" if gap > 0 else "Kelly 가 더 큼"
                print(f"              ↳ 차이 {gap:+.1f}%p — {who}. "
                      f"스탑기반은 변동성·엣지를 안 본다는 점을 기억할 것")
        print()

    print("■ 반드시 같이 읽을 것")
    print(f"   · full Kelly 는 **in-sample 에서조차 손실**이었다 — 연 {FULL_KELLY_INSAMPLE_CAGR}%, "
          f"MDD {FULL_KELLY_INSAMPLE_MDD}% (PLAY28)")
    print("   · 1/4 Kelly = 이상 성장률의 ~44% 를 안전마진 4배와 맞바꾸는 것")
    print("   · 무거래 밴드는 공짜가 아니다 — 뒤집힘 국면에서 MDD 악화(−32%→−52%)")
    print("   · 팻테일(Hill α≈3)이라 정규분포 기반 스탑은 꼬리를 과소평가한다")
    print("\n■ IC 눈금 (lab 실측 — 자기 IC 를 부풀리지 않기 위한 참고)")
    for k, v in IC_REFERENCE:
        print(f"   · {k}: {v}")
    print("\n⚠ IC·z 는 **사람이 넣는 가정**이지 측정값이 아니다. 근거 없는 IC 는 근거 없는 크기를 낳는다.")
    print("   이 스크립트는 정합성만 계산한다 — 매매 권유가 아니고, 집행은 사람이 한다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
