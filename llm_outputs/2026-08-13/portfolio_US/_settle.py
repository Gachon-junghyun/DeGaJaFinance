# -*- coding: utf-8 -*-
"""STEP 0 정산 계기 — S63/S64/S67/S68/S69/S71 을 동결된 관측값 정의 그대로 재잰다.

RS20 정의는 module_flow._price_flow 와 동일: ret(close,20) - ret(bench,20), auto_adjust=False.
임계값은 SCENARIOS_US.md 등록본 그대로. 밴드를 옮기지 않는다.
가장 중요한 출력: **마지막 정착 봉의 날짜** — 08-13 이 없으면 전부 미정산이다.
"""
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import pandas as pd
import yfinance as yf

TK = ["SPY", "XLU", "XLRE", "XLF", "XLI", "XLE", "MPC", "VLO", "PSX", "MET",
      "DIS", "XLB", "JPM", "BAC", "WFC", "BRK-B", "ANET", "HPE", "XLV", "NEM"]

raw = yf.download(TK, period="8mo", progress=False, auto_adjust=False, group_by="ticker")
cl = {}
for t in TK:
    try:
        s = raw[t]["Close"].dropna()
    except Exception:
        s = None
    if s is not None and len(s):
        cl[t] = s.astype(float)
px = pd.DataFrame(cl)

print("=== 마지막 5 봉 (정착 여부 판정용) ===")
print(px[["SPY", "XLU", "XLF", "XLI"]].tail(5).to_string())
last = px.index[-1].date()
print(f"\n[LAST SETTLED BAR] {last}")
print(f"[bars present]  08-12={'YES' if any(str(i.date())=='2026-08-12' for i in px.index) else 'NO'}"
      f"  08-13={'YES' if any(str(i.date())=='2026-08-13' for i in px.index) else 'NO'}")


def ret(s, d):
    return float(s.iloc[-1] / s.iloc[-1 - d] - 1.0) * 100.0


def rs20_at(t, idx=-1):
    """idx 위치 봉 기준 RS20 vs SPY."""
    s = px[t].dropna()
    b = px["SPY"].dropna()
    s = s.iloc[: len(s) + idx + 1] if idx != -1 else s
    b = b.iloc[: len(b) + idx + 1] if idx != -1 else b
    return round((float(s.iloc[-1] / s.iloc[-21] - 1) - float(b.iloc[-1] / b.iloc[-21] - 1)) * 100, 3)


print("\n=== S63 · DUR = (XLU RS20 + XLRE RS20)/2 − XLF RS20 ===")
u, r, f = rs20_at("XLU"), rs20_at("XLRE"), rs20_at("XLF")
dur = round((u + r) / 2 - f, 3)
print(f"  XLU {u} · XLRE {r} · XLF {f}  ⇒ DUR = {dur}")
print(f"  등록 앵커(08-05 정착) −6.197 · A: DUR ≥ −3.3 · B: DUR ≤ −9.2 · C: 사이")

print("\n=== S64 · XLI 전방 6세션 초과수익 vs SPY (08-05 정착 → 정산일) ===")
base = pd.Timestamp("2026-08-05")
try:
    i0 = px.index.get_loc(base)
    xli0, spy0 = float(px["XLI"].iloc[i0]), float(px["SPY"].iloc[i0])
    xli1, spy1 = float(px["XLI"].iloc[-1]), float(px["SPY"].iloc[-1])
    exc = round((xli1 / xli0 - 1) * 100 - (spy1 / spy0 - 1) * 100, 3)
    sess = len(px.index) - 1 - i0
    xle0, xle1 = float(px["XLE"].iloc[i0]), float(px["XLE"].iloc[-1])
    exce = round((xle1 / xle0 - 1) * 100 - (spy1 / spy0 - 1) * 100, 3)
    print(f"  08-05 XLI {xli0:.2f} SPY {spy0:.2f} → {px.index[-1].date()} XLI {xli1:.2f} SPY {spy1:.2f}")
    print(f"  경과 세션 = {sess} (동결 정의는 6세션)")
    print(f"  XLI 초과 = {exc}pp   [동반 비동결 C2] XLE 초과 = {exce}pp")
    print(f"  A: ≤ −1.8 · B: ≥ +1.9 · C: 사이 / VOID: WTI 정산 ≥ 75.22")
except KeyError:
    print("  08-05 봉 없음")

print("\n=== S67 · median RS20 vs SPY of {MPC,VLO,PSX} ===")
trio = {t: rs20_at(t) for t in ("MPC", "VLO", "PSX")}
med = round(sorted(trio.values())[1], 3)
print(f"  {trio}  ⇒ median = {med}")
print(f"  등록 앵커(08-06 정착) +5.488 · A: ≤ −2.20 · B: ≥ +13.56")

print("\n=== S69 · MET RS20 vs SPY ===")
print(f"  MET RS20 = {rs20_at('MET')}   등록 앵커(08-06 정착) +7.413 · A: ≤ +2.53 · B: ≥ +12.24")

print("\n=== S71 · XLU 1세션 초과(08-13) − XLU 1세션 초과(08-12) ===")


def exc1(t, ts):
    i = px.index.get_loc(pd.Timestamp(ts))
    a = float(px[t].iloc[i] / px[t].iloc[i - 1] - 1) * 100
    b = float(px["SPY"].iloc[i] / px["SPY"].iloc[i - 1] - 1) * 100
    return round(a - b, 3)


for d in ("2026-08-11", "2026-08-12", "2026-08-13"):
    try:
        print(f"  XLU 1세션 초과 {d} = {exc1('XLU', d)}")
    except KeyError:
        print(f"  XLU 1세션 초과 {d} = 봉 없음 (미정산)")
print("  A: Δ ≥ +1.57 · B: Δ ≤ −1.69 · C: 사이")

print("\n=== STEP3 ① S83 · HPE vs ANET (등록 sd 8.417pp) ===")
for t in ("HPE", "ANET"):
    try:
        print(f"  {t}: RS20 {rs20_at(t)} · 마지막 종가 {float(px[t].iloc[-1]):.2f} ({px.index[-1].date()})")
    except Exception as e:
        print(f"  {t}: {e}")

print("\n=== 참고 · 섹터 ETF exc5 / exc20 vs SPY (정착 기준) ===")
rows = []
for t in ("XLU", "XLRE", "XLF", "XLI", "XLE", "XLB", "XLV"):
    s, b = px[t].dropna(), px["SPY"].dropna()
    e5 = round((float(s.iloc[-1] / s.iloc[-6] - 1) - float(b.iloc[-1] / b.iloc[-6] - 1)) * 100, 2)
    e20 = round((float(s.iloc[-1] / s.iloc[-21] - 1) - float(b.iloc[-1] / b.iloc[-21] - 1)) * 100, 2)
    rows.append((t, e5, e20))
for t, e5, e20 in rows:
    print(f"  {t:<5} exc5 {e5:>7} · exc20 {e20:>7}")
print(f"\n[모든 수치의 창 끝 날짜] {px.index[-1].date()} / 창 시작은 각 창 길이만큼 앞")
