# -*- coding: utf-8 -*-
"""--asof 날짜 이후 봉을 전부 버리고 그 정착일 기준으로 6개 브래킷의 '현재 서 있는 위치'를 잰다.

이것은 채점이 아니다. 정산일(08-13)의 정착 종가가 아직 없으므로, 마지막 진짜 정착일(08-12)에서
각 브래킷이 어느 밴드에 서 있고 임계선까지 몇 pp 남았는지만 보고한다. 밴드는 옮기지 않는다.
"""
import sys, io, argparse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import pandas as pd
import yfinance as yf

ap = argparse.ArgumentParser()
ap.add_argument("--asof", default="2026-08-12")
a = ap.parse_args()
ASOF = pd.Timestamp(a.asof)

TK = ["SPY", "XLU", "XLRE", "XLF", "XLI", "XLE", "MPC", "VLO", "PSX", "MET", "DIS",
      "XLB", "XLV", "ANET", "HPE", "NEM", "MET", "NDAQ", "NUE", "AVGO", "NVDA", "ETN"]
raw = yf.download(sorted(set(TK)), period="10mo", progress=False, auto_adjust=False, group_by="ticker")
cl = {}
for t in sorted(set(TK)):
    try:
        s = raw[t]["Close"].dropna().astype(float)
        if len(s):
            cl[t] = s
    except Exception:
        pass
px = pd.DataFrame(cl)
px = px[px.index <= ASOF]
print(f"[asof 고정] 마지막 봉 = {px.index[-1].date()}  (그 이후 봉 전부 폐기)\n")


def rs20(t):
    s, b = px[t], px["SPY"]
    return round((float(s.iloc[-1] / s.iloc[-21] - 1) - float(b.iloc[-1] / b.iloc[-21] - 1)) * 100, 3)


def exc1(t, ts):
    i = px.index.get_loc(pd.Timestamp(ts))
    return round((float(px[t].iloc[i] / px[t].iloc[i - 1] - 1)
                  - float(px["SPY"].iloc[i] / px["SPY"].iloc[i - 1] - 1)) * 100, 3)


u, r, f = rs20("XLU"), rs20("XLRE"), rs20("XLF")
dur = round((u + r) / 2 - f, 3)
print(f"S63  DUR = {dur}   (XLU {u} · XLRE {r} · XLF {f})")
print(f"     밴드 A ≥ −3.3 / B ≤ −9.2 · 앵커 −6.197 ⇒ 현재 C밴드, A선까지 {round(dur-(-3.3),3)}pp, B선까지 {round(dur-(-9.2),3)}pp")

i0 = px.index.get_loc(pd.Timestamp("2026-08-05"))
xe = round((float(px['XLI'].iloc[-1] / px['XLI'].iloc[i0] - 1)
            - float(px['SPY'].iloc[-1] / px['SPY'].iloc[i0] - 1)) * 100, 3)
ee = round((float(px['XLE'].iloc[-1] / px['XLE'].iloc[i0] - 1)
            - float(px['SPY'].iloc[-1] / px['SPY'].iloc[i0] - 1)) * 100, 3)
print(f"\nS64  XLI 08-05→{px.index[-1].date()} 초과 = {xe}pp  ({len(px.index)-1-i0}세션 경과 / 동결정의 6세션)")
print(f"     [C2 동반] XLE 같은 창 = {ee}pp · 밴드 A ≤ −1.8 / B ≥ +1.9")

trio = {t: rs20(t) for t in ("MPC", "VLO", "PSX")}
med = sorted(trio.values())[1]
print(f"\nS67  median{{MPC,VLO,PSX}} RS20 = {med}   {trio}")
print(f"     밴드 A ≤ −2.20 / B ≥ +13.56 · 앵커 +5.488")

print(f"\nS69  MET RS20 = {rs20('MET')}   밴드 A ≤ +2.53 / B ≥ +12.24 · 앵커 +7.413")

print(f"\nS71  XLU 1세션 초과: 08-11 {exc1('XLU','2026-08-11')} · 08-12 {exc1('XLU','2026-08-12')}")
print(f"     Δ = (08-13) − (08-12={exc1('XLU','2026-08-12')}) · 밴드 A ≥ +1.57 / B ≤ −1.69")
print(f"     ⇒ A 가 뜨려면 08-13 초과 ≥ {round(exc1('XLU','2026-08-12')+1.57,3)}, B 는 ≤ {round(exc1('XLU','2026-08-12')-1.69,3)}")

print(f"\nS83  HPE RS20 {rs20('HPE')} · ANET RS20 {rs20('ANET')} · 스프레드 {round(rs20('HPE')-rs20('ANET'),3)}pp (등록 sd 8.417)")

print("\n=== 미매핑 보유 4종 + 최대단위 RS20 (정착 기준) ===")
for t in ("HPE", "MET", "NDAQ", "NUE", "AVGO", "NVDA", "ANET", "ETN", "NEM"):
    try:
        print(f"  {t:<5} RS20 {rs20(t):>8}  종가 {float(px[t].iloc[-1]):>9.2f}")
    except Exception as e:
        print(f"  {t:<5} {e}")
