#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
us_flow.py — US 수급/포지셔닝 파이프라인 (free public feeds, no auth)

두 축을 붙인다 (US는 KR처럼 투자자별(외국인/기관) 일별 데이터가 없어서,
아래 프록시를 겹쳐 '수급'을 재구성한다):

  ① 선물 포지셔닝 (CFTC Commitments of Traders, 주간)
     - Socrata legacy futures-only: publicreporting.cftc.gov/resource/6dca-aqww.json
     - 투기자(non-commercial) 순포지션 + 주간증감 + %OI + 1년 백분위(포지셔닝 극단)
     - index(S&P/Nasdaq/Russell)·rates(UST)·dollar(DXY)·energy(WTI/gas)·metals(gold/copper/silver)
       => 매크로/섹터 버킷에 매핑 (산업런 Phase0/Phase2 수급 보강)

  ② 개별종목 일별 공매도 압력 (FINRA Reg SHO daily short-sale volume)
     - cdn.finra.org/equity/regsho/daily/CNMSshvol{YYYYMMDD}.txt  (파이프구분)
     - short-vol ratio = ShortVolume/TotalVolume, 20일 베이스라인 대비 z-score + 5일 추세
     - 주의: 40~45%는 정상(마켓메이커 헤지 포함). 신호는 '자기 베이스라인 대비 극단/추세'.

사용:
  python -X utf8 scripts/us_flow.py --cot                      # 선물 포지셔닝 스냅
  python -X utf8 scripts/us_flow.py MU NVDA CEG LMT CVX        # 종목 공매도 압력 스냅
  python -X utf8 scripts/us_flow.py --cot MU NVDA --json       # 둘 다 + JSON

의존성: 표준 라이브러리만 (urllib, json). pandas/requests 불필요.
"""
import sys, os, json, argparse, urllib.request, urllib.parse, gzip, io
from datetime import date, timedelta

UA = "Mozilla/5.0 (us_flow research; +local)"
CACHE = os.path.join(os.path.dirname(__file__), ".cache", "finra")
COT_URL = "https://publicreporting.cftc.gov/resource/6dca-aqww.json"
FINRA_URL = "https://cdn.finra.org/equity/regsho/daily/CNMSshvol{d}.txt"

# label -> (market_and_exchange_names substring, bucket)  [멀티매치 시 최대 OI 자동선택]
COT_MARKETS = {
    "S&P500 (E-mini)": ("E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE", "equity/concentration"),
    "Nasdaq-100":      ("NASDAQ-100 Consolidated - CHICAGO MERCANTILE EXCHANGE", "equity/tech"),
    "Russell 2000":    ("MICRO E-MINI RUSSELL 2000 INDX - CHICAGO MERCANTILE EXCHANGE", "equity/smallcap"),
    "UST 10Y":         ("UST 10Y NOTE - CHICAGO BOARD OF TRADE", "rates"),
    "UST 2Y":          ("UST 2Y NOTE - CHICAGO BOARD OF TRADE", "rates"),
    "USD Index":       ("USD INDEX - ICE FUTURES U.S.", "dollar"),
    "WTI Crude":       ("WTI FINANCIAL CRUDE OIL - NEW YORK MERCANTILE EXCHANGE", "energy(ENRG)"),
    "Nat Gas":         ("NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE", "energy(ENRG)"),
    "Gold":            ("GOLD - COMMODITY EXCHANGE INC.", "metals(MATR)"),
    "Copper":          ("COPPER- #1 - COMMODITY EXCHANGE INC.", "metals(MATR)"),
    "Silver":          ("SILVER - COMMODITY EXCHANGE INC.", "metals(MATR)"),
}


def _get(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.GzipFile(fileobj=io.BytesIO(raw)).read()
    return raw.decode("utf-8", "replace")


# ─────────────────────────────── COT (futures positioning) ───────────────────────────────
def _cot_pull(market_substr, weeks=60):
    """market 이름 substring으로 최근 weeks주 뽑고, 멀티매치면 최대 OI 시장만 남김."""
    sel = ",".join(["market_and_exchange_names", "report_date_as_yyyy_mm_dd",
                    "noncomm_positions_long_all", "noncomm_positions_short_all",
                    "comm_positions_long_all", "comm_positions_short_all",
                    "open_interest_all",
                    "change_in_noncomm_long_all", "change_in_noncomm_short_all"])
    params = {
        "$where": "market_and_exchange_names like '%{}%'".format(market_substr.replace("'", "''")),
        "$select": sel,
        "$order": "report_date_as_yyyy_mm_dd DESC",
        "$limit": weeks * 4,
    }
    q = COT_URL + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    try:
        rows = json.loads(_get(q))
    except Exception as e:
        return None, str(e)
    if not rows:
        return None, "no rows"
    # 멀티매치: 최신주에서 최대 OI 시장 선택
    latest_date = rows[0]["report_date_as_yyyy_mm_dd"]
    cands = [r for r in rows if r["report_date_as_yyyy_mm_dd"] == latest_date]
    pick = max(cands, key=lambda r: float(r.get("open_interest_all") or 0))["market_and_exchange_names"]
    series = [r for r in rows if r["market_and_exchange_names"] == pick]
    return series, pick


def _f(r, k):
    try:
        return float(r.get(k) or 0)
    except Exception:
        return 0.0


def cot_snapshot(weeks=60, verbose=True):
    out = []
    for label, (substr, bucket) in COT_MARKETS.items():
        series, pick = _cot_pull(substr, weeks)
        if not series:
            out.append({"label": label, "bucket": bucket, "error": pick})
            continue
        nets = []
        for r in series:
            nets.append(_f(r, "noncomm_positions_long_all") - _f(r, "noncomm_positions_short_all"))
        cur = nets[0]
        prev = nets[1] if len(nets) > 1 else cur
        oi = _f(series[0], "open_interest_all")
        wk_chg = (_f(series[0], "change_in_noncomm_long_all")
                  - _f(series[0], "change_in_noncomm_short_all"))
        # 1년 백분위 (현재 net-spec가 지난 weeks 중 어디)
        srt = sorted(nets)
        pct = 100.0 * (sum(1 for x in srt if x <= cur) - 1) / max(1, (len(srt) - 1))
        pct = max(0.0, min(100.0, pct))
        # 판정
        if pct >= 80:   tag = "🟢 크라우디드-롱(과열주의)"
        elif pct <= 20: tag = "🔴 크라우디드-숏(반등탄약)"
        else:           tag = "🟡 중립"
        arrow = "▲" if wk_chg > 0 else ("▼" if wk_chg < 0 else "·")
        out.append({
            "label": label, "bucket": bucket, "market": pick,
            "report_date": series[0]["report_date_as_yyyy_mm_dd"][:10],
            "net_spec": int(cur), "net_spec_prev": int(prev),
            "wk_change": int(wk_chg), "wk_arrow": arrow,
            "pct_of_oi": round(100.0 * cur / oi, 1) if oi else None,
            "pctile_1y": round(pct, 0), "tag": tag, "n_weeks": len(nets),
        })
    return out


# ─────────────────────────────── FINRA daily short volume ───────────────────────────────
def _finra_day(d):
    """하루치 파일 -> {symbol: (short, total)}. 캐시. 없으면 None."""
    os.makedirs(CACHE, exist_ok=True)
    ds = d.strftime("%Y%m%d")
    fp = os.path.join(CACHE, ds + ".txt")
    if os.path.exists(fp):
        txt = open(fp, encoding="utf-8", errors="replace").read()
    else:
        try:
            txt = _get(FINRA_URL.format(d=ds))
        except Exception:
            return None
        if not txt.startswith("Date|"):     # 주말/휴일/미발행 => HTML
            return None
        open(fp, "w", encoding="utf-8").write(txt)
    m = {}
    for line in txt.splitlines()[1:]:
        p = line.split("|")
        if len(p) < 5:
            continue
        try:
            m[p[1].upper()] = (float(p[2]), float(p[4]))
        except Exception:
            continue
    return m


def _finra_series(tickers, ndays=20):
    """최근 거래일 ndays치 수집(주말/휴일 스킵). {ticker: [(date, ratio), ...] 최신순}."""
    want = set(t.upper() for t in tickers)
    res = {t: [] for t in want}
    got, back = 0, 0
    d = date.today()
    while got < ndays and back < ndays * 2 + 12:
        day = _finra_day(d)
        d -= timedelta(days=1)
        back += 1
        if day is None:
            continue
        got += 1
        for t in want:
            if t in day:
                short, total = day[t]
                if total > 0:
                    res[t].append((d + timedelta(days=1), 100.0 * short / total))
    return res


def _mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


def _std(xs):
    if len(xs) < 2:
        return 0.0
    mu = _mean(xs)
    return (sum((x - mu) ** 2 for x in xs) / (len(xs) - 1)) ** 0.5


def short_snapshot(tickers, ndays=20):
    ser = _finra_series(tickers, ndays)
    out = []
    for t in [x.upper() for x in tickers]:
        pts = ser.get(t, [])
        if not pts:
            out.append({"ticker": t, "error": "no data"})
            continue
        ratios = [r for _, r in pts]           # 최신순
        cur = ratios[0]
        base = ratios[1:] if len(ratios) > 1 else ratios
        mu, sd = _mean(base), _std(base)
        z = (cur - mu) / sd if sd else 0.0
        recent5 = _mean(ratios[:5]) if len(ratios) >= 2 else cur
        older5 = _mean(ratios[5:10]) if len(ratios) >= 6 else recent5
        slope = recent5 - older5               # +면 공매도압력 증가
        if z >= 1.5:    tag = "🔴 공매도급증(자기베이스대비 극단)"
        elif z <= -1.5: tag = "🟢 공매도급감(숏커버/압력이탈)"
        else:           tag = "🟡 정상범위"
        arrow = "▲" if slope > 0.3 else ("▼" if slope < -0.3 else "·")
        out.append({
            "ticker": t, "date": pts[0][0].strftime("%Y-%m-%d"),
            "short_ratio": round(cur, 1), "base20_mean": round(mu, 1),
            "z_score": round(z, 2), "slope5v5": round(slope, 1),
            "trend_arrow": arrow, "n_days": len(ratios), "tag": tag,
        })
    return out


# ─────────────────────────────── render ───────────────────────────────
def render_cot(rows):
    print("# 선물 포지셔닝 — CFTC COT (투기자 net, 주간)  [1yr 백분위]")
    print("  {:<17s} {:<16s} {:>12s} {:>8s} {:>7s}  {:<8s} {}".format(
        "INSTRUMENT", "BUCKET", "NET_SPEC", "WK_Δ", "%OI", "1Y_%ILE", "판정"))
    print("  " + "─" * 92)
    for r in rows:
        if r.get("error"):
            print("  {:<17s} {:<16s}  ! {}".format(r["label"], r["bucket"], r["error"]))
            continue
        print("  {:<17s} {:<16s} {:>12,d} {:>6,d}{} {:>6s} {:>6.0f}%ile  {}".format(
            r["label"], r["bucket"], r["net_spec"], r["wk_change"], r["wk_arrow"],
            (str(r["pct_of_oi"]) + "%") if r["pct_of_oi"] is not None else "n/a",
            r["pctile_1y"], r["tag"]))
    print("  net_spec>0=투기자 순매수 · WK_Δ=주간증감 · 1Y_%ile≥80=크라우디드롱 ≤20=크라우디드숏")
    print("  ⚠️ COT는 화요일 마감·금요일 발표 → 3~4일 지연. 극단 백분위=역발상 탄약, 방향 확정 아님.")


def render_short(rows):
    print("\n# 개별종목 공매도 압력 — FINRA Reg SHO daily (short-vol ratio)")
    print("  {:<6s} {:>10s} {:>9s} {:>7s} {:>8s}  {:<6s} {}".format(
        "TICKER", "SHORT%", "BASE20", "Z", "5v5추세", "date", "판정"))
    print("  " + "─" * 82)
    for r in rows:
        if r.get("error"):
            print("  {:<6s}  ! {}".format(r["ticker"], r["error"]))
            continue
        print("  {:<6s} {:>9.1f}% {:>8.1f}% {:>7.2f} {:>+7.1f}{} {:<10s} {}".format(
            r["ticker"], r["short_ratio"], r["base20_mean"], r["z_score"],
            r["slope5v5"], r["trend_arrow"], r["date"], r["tag"]))
    print("  short%=일별 공매도체결/총체결(40~45%는 정상; MM헤지 포함) · Z=자기 20일 베이스대비 · 추세+면 압력↑")


def main():
    ap = argparse.ArgumentParser(description="US 수급/포지셔닝 (CFTC COT + FINRA 공매도)")
    ap.add_argument("tickers", nargs="*", help="공매도 압력 볼 US 티커들")
    ap.add_argument("--cot", action="store_true", help="선물 포지셔닝(COT) 스냅 포함")
    ap.add_argument("--weeks", type=int, default=60, help="COT 백분위 룩백(주)")
    ap.add_argument("--ndays", type=int, default=20, help="공매도 베이스라인 일수")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if not a.cot and not a.tickers:
        a.cot = True  # 인자 없으면 COT 스냅

    result = {}
    if a.cot:
        result["cot"] = cot_snapshot(a.weeks)
    if a.tickers:
        result["short"] = short_snapshot(a.tickers, a.ndays)

    if a.json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return
    if "cot" in result:
        render_cot(result["cot"])
    if "short" in result:
        render_short(result["short"])


if __name__ == "__main__":
    main()
