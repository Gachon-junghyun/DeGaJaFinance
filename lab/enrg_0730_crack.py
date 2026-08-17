# -*- coding: utf-8 -*-
"""ENRG DEEP 2026-07-30 : 크랙 정착 일봉 + 변화율(L1) 시계열. US 걸프 프록시."""
import yfinance as yf, pandas as pd, numpy as np

d = yf.download(["CL=F","BZ=F","RB=F","HO=F"], start="2024-07-01", end="2026-08-01",
                auto_adjust=False, progress=False)
C = d["Close"].dropna(how="all")
V = d["Volume"]

df = pd.DataFrame(index=C.index)
df["CL"]=C["CL=F"]; df["BZ"]=C["BZ=F"]; df["RB"]=C["RB=F"]; df["HO"]=C["HO=F"]
df = df.dropna()
df["crack321"] = (2*df.RB + df.HO)*42/3 - df.CL
df["dist"]     = df.HO*42 - df.CL          # 증류유 크랙
df["gaso"]     = df.RB*42 - df.CL

print("=== 마지막 8봉 (정착 여부 확인: Volume 동일 = forward-fill 의심, D83/D86) ===")
tail = df.tail(8).copy()
tail["volCL"]=V["CL=F"].reindex(tail.index)
tail["volHO"]=V["HO=F"].reindex(tail.index)
print(tail.round(3).to_string())

print("\n=== A. 일별 Δ1d (최근 10) ===")
a = df.tail(11).copy()
for c in ["crack321","dist","gaso","CL","BZ"]:
    a["d_"+c] = a[c].pct_change()*100
print(a.tail(10)[["crack321","d_crack321","dist","d_dist","gaso","d_gaso",
                  "CL","d_CL","BZ","d_BZ"]].round(3).to_string())

print("\n=== B. ROC5 와 그 1차차분 d(ROC5) — L1 발화 문턱 2연속 ===")
df["roc5"] = df.crack321.pct_change(5)*100
df["droc5"] = df.roc5.diff()
print(df.tail(12)[["crack321","roc5","droc5"]].round(3).to_string())
df["roc5d"] = df.dist.pct_change(5)*100
df["droc5d"] = df.roc5d.diff()
print("\n  증류유 크랙 ROC5:")
print(df.tail(8)[["dist","roc5d","droc5d"]].round(3).to_string())

print("\n=== C. 주간 (금요일 종료, WoW%) ===")
w = df[["crack321","dist","gaso","CL","BZ"]].resample("W-FRI").last()
wc = w.pct_change()*100
out = pd.concat([w.round(3), wc.round(2).add_suffix("_WoW")], axis=1)
print(out.tail(8).to_string())
print(f"  ※ 마지막 주 포함 세션수 = {len(df.loc[w.index[-2]+pd.Timedelta(days=1):])}")

print("\n=== D. 분기 QoQ (평균값 기준 = 마진 프록시) ===")
q = df[["crack321","dist","gaso","CL","BZ"]].resample("QE").mean()
qc = q.pct_change()*100
o = pd.concat([q.round(2), qc.round(2).add_suffix("_QoQ")], axis=1)
print(o.tail(7).to_string())
nq = len(df.loc["2026-07-01":])
print(f"  ※ 2026Q3 포함 세션수 = {nq} (부분 분기)")

print("\n=== E. 2년 백분위 (마지막 정착봉) ===")
last = df.iloc[-1]
for c in ["crack321","dist","gaso","BZ","CL"]:
    s = df[c]
    print(f"  {c:9s} {last[c]:8.3f}  pctile(2y) = {(s<=last[c]).mean()*100:5.1f}")

print("\n=== F. 킬라인 버퍼 ===")
print(f"  crack321 {last.crack321:.3f}  → 60 까지 {last.crack321-60:+.3f}")
print(f"  dist     {last['dist']:.3f}  → 84 까지 {last['dist']-84:+.3f}")
print(f"  마지막 정착봉 날짜 = {df.index[-1].date()}")
