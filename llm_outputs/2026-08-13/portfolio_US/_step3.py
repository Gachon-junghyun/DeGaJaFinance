# -*- coding: utf-8 -*-
"""STEP 3 의 5개 열린 질문을 숫자로 답하기 위한 계기.

전부 **08-12 정착 종가**에 고정한다(08-13 은 아직 장중이다).
창 길이와 양끝 날짜를 같은 칸에 적는다(D253 / R65 재발 방지).
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import pandas as pd
import numpy as np
import yfinance as yf

ASOF = pd.Timestamp("2026-08-12")
TK = ["SPY", "XLV", "XLU", "XLRE", "XLP", "XLB", "ANET", "HPE", "NUE", "NEM", "NDAQ", "MET", "IHI", "XBI"]
raw = yf.download(TK, period="3y", progress=False, auto_adjust=False, group_by="ticker")
cl = {}
for t in TK:
    try:
        s = raw[t]["Close"].dropna().astype(float)
        if len(s):
            cl[t] = s
    except Exception:
        pass
px = pd.DataFrame(cl).dropna()
px = px[px.index <= ASOF]
print(f"[asof] 마지막 봉 {px.index[-1].date()} · n={len(px)}\n")


def exc_series(t, w):
    """t 의 w세션 초과수익 vs SPY 시계열(%)"""
    a = px[t] / px[t].shift(w) - 1
    b = px["SPY"] / px["SPY"].shift(w) - 1
    return ((a - b) * 100).dropna()


def win(t, w):
    s = exc_series(t, w)
    d0 = px.index[-1 - w].date()
    d1 = px.index[-1].date()
    return round(float(s.iloc[-1]), 3), f"{d0}→{d1}"


print("=== ② HLTH — 지금 살까, S82(08-20)까지 기다릴까 ===")
for w in (5, 20, 60):
    v, dr = win("XLV", w)
    print(f"  XLV exc{w:<3} = {v:>7}pp   [{dr}]")
ew = (exc_series("XLU", 5) + exc_series("XLRE", 5) + exc_series("XLP", 5)) / 3
s82 = exc_series("XLV", 5) - ew
print(f"\n  S82 관측값 = XLV exc5 − EW{{XLU,XLRE,XLP}} exc5")
print(f"    현재값 {round(float(s82.iloc[-1]),3)}pp  [{px.index[-6].date()}→{px.index[-1].date()}]  (등록 상태 +3.091)")
print(f"    밴드 A ≥ +2.45(독립 med-tech) / B ≤ −1.62(듀레이션 4번째 다리)")
t252 = s82.tail(252)
print(f"    D93 자체분포(252): mean {round(float(t252.mean()),3)} · sd {round(float(t252.std()),3)}"
      f" · A발화 {round(float((t252>=2.45).mean())*100,1)}% · B발화 {round(float((t252<=-1.62).mean())*100,1)}%")

x5 = exc_series("XLV", 5).tail(252)
print(f"\n  ★ 기다림의 기회비용 = XLV 5세션 초과수익의 분포(252일)")
print(f"    mean {round(float(x5.mean()),3)}pp · sd {round(float(x5.std()),3)}pp"
      f" · p15 {round(float(x5.quantile(.15)),3)} · p85 {round(float(x5.quantile(.85)),3)}")
print(f"    ⇒ 5세션(08-13→08-20) 기다리는 기대비용 = {round(float(x5.mean()),3)}pp ± {round(float(x5.std()),3)}pp")

print("\n  ★ 듀레이션 팩터 중복 리스크 — XLV 와 3개 UW 다리의 상관(일간 초과수익, 252일)")
r = {}
for t in ("XLU", "XLRE", "XLP"):
    a = exc_series("XLV", 1).tail(252)
    b = exc_series(t, 1).tail(252)
    j = pd.concat([a, b], axis=1).dropna()
    r[t] = round(float(np.corrcoef(j.iloc[:, 0], j.iloc[:, 1])[0, 1]), 3)
print(f"    corr(XLV, XLU) {r['XLU']} · corr(XLV, XLRE) {r['XLRE']} · corr(XLV, XLP) {r['XLP']}")
ewd = (exc_series("XLU", 1) + exc_series("XLRE", 1) + exc_series("XLP", 1)) / 3
j = pd.concat([exc_series("XLV", 1).tail(252), ewd.tail(252)], axis=1).dropna()
print(f"    corr(XLV, EW{{3 UW다리}}) = {round(float(np.corrcoef(j.iloc[:,0], j.iloc[:,1])[0,1]),3)}")

print("\n=== ① HPE — S83 관측값 = ANET exc5 − HPE exc5 (08-20 정산) ===")
s83 = exc_series("ANET", 5) - exc_series("HPE", 5)
print(f"  현재값 {round(float(s83.iloc[-1]),3)}pp  [{px.index[-6].date()}→{px.index[-1].date()}]")
print(f"  밴드 A ≥ +7.16 / B ≤ −9.68 · 등록 sd 8.417")
t = s83.tail(252)
print(f"  자체분포(252): mean {round(float(t.mean()),3)} · sd {round(float(t.std()),3)}"
      f" · A발화 {round(float((t>=7.16).mean())*100,1)}% · B발화 {round(float((t<=-9.68).mean())*100,1)}%"
      f" · C {round(float(((t>-9.68)&(t<7.16)).mean())*100,1)}%")
print(f"  ⇒ 장중 6pp 이동 = {round(6/8.417,2)}σ")

print("\n=== ④ MATR — 책이 든 것은 NEM 이 아니라 NUE 다 ===")
for t in ("NEM", "NUE", "XLB"):
    for w in (5, 20, 60):
        v, dr = win(t, w)
        print(f"  {t:<4} exc{w:<3} = {v:>8}pp  [{dr}]")
    print()
a = exc_series("NUE", 1).tail(252)
b = exc_series("NEM", 1).tail(252)
jj = pd.concat([a, b], axis=1).dropna()
print(f"  corr(NUE, NEM) 일간초과 252일 = {round(float(np.corrcoef(jj.iloc[:,0], jj.iloc[:,1])[0,1]),3)}")

print("\n=== ⑤ 미매핑 4종 — 계기 커버리지 ===")
for t in ("HPE", "MET", "NDAQ", "NUE"):
    for w in (5, 20):
        v, dr = win(t, w)
        print(f"  {t:<5} exc{w:<3} = {v:>8}pp  [{dr}]")
