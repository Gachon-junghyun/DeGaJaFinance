# -*- coding: utf-8 -*-
"""1시간봉으로 정착(14:00~14:30 ET) 크랙 재구축 + KR 장중 시간대 역추적.
KST = ET(EDT) + 13h.  KR 09:00~15:30 KST = 전일 20:00 ~ 당일 02:30 ET."""
import yfinance as yf, pandas as pd

legs = {}
for t in ["CL=F","BZ=F","RB=F","HO=F"]:
    h = yf.Ticker(t).history(start="2026-07-22", end="2026-08-01", interval="1h")
    legs[t] = h["Close"]
df = pd.DataFrame(legs).dropna()
df.index = df.index.tz_convert("America/New_York")
df["crack321"] = (2*df["RB=F"] + df["HO=F"])*42/3 - df["CL=F"]
df["dist"]     = df["HO=F"]*42 - df["CL=F"]
df["gaso"]     = df["RB=F"]*42 - df["CL=F"]
df["KST"] = df.index.tz_convert("Asia/Seoul")

print("=== A. 정착 시간대(13:00~16:00 ET) 크랙 — 트레이드 날짜별 ===")
for d in ["2026-07-24","2026-07-27","2026-07-28","2026-07-29"]:
    s = df.loc[d]
    s = s[(s.index.hour>=13)&(s.index.hour<=16)]
    if len(s)==0: print(f"  {d}: 없음"); continue
    print(f"\n  --- {d} ---")
    print(s[["CL=F","BZ=F","RB=F","HO=F","crack321","dist","gaso"]].round(3).to_string())

print("\n\n=== B. KR 장중 시간대 역추적 (M188 재현) ===")
for kr_day, et_start, et_end in [("2026-07-29","2026-07-28 20:00","2026-07-29 02:30"),
                                 ("2026-07-30","2026-07-29 20:00","2026-07-30 02:30")]:
    s = df.loc[et_start:et_end]
    print(f"\n  --- KR {kr_day} 세션 (09:00~15:30 KST) ---")
    if len(s)==0: print("   데이터 없음"); continue
    o = s[["KST","CL=F","BZ=F","crack321","dist"]].copy()
    o["KST"] = o["KST"].dt.strftime("%m-%d %H:%M")
    print(o.round(3).to_string(index=False))
    print(f"   crack321 범위 {s.crack321.min():.3f}~{s.crack321.max():.3f}  (킬라인 60)")
    print(f"   증류유     범위 {s['dist'].min():.3f}~{s['dist'].max():.3f}  (브랜치B 하한 84)")

print("\n\n=== C. 최신 틱 (지금 KR이 보는 화면) ===")
print(df.tail(4)[["KST","CL=F","BZ=F","RB=F","HO=F","crack321","dist"]].round(3).to_string())
