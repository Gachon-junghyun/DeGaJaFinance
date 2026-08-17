# -*- coding: utf-8 -*-
"""D83/D86 감사: 크랙 구성 4계열의 정착 여부 · 볼륨 지문 · 런 간 재작성 검증"""
import yfinance as yf, pandas as pd

pd.set_option("display.width", 200)
for t in ["CL=F","BZ=F","RB=F","HO=F"]:
    h = yf.Ticker(t).history(start="2026-07-15", end="2026-08-01", interval="1d")
    print(f"\n===== {t} 일봉 =====")
    print(h[["Open","High","Low","Close","Volume"]].round(4).to_string())

print("\n\n===== CL=F 1시간봉 (마지막 30) — 07-29/07-30 경계 확인 =====")
h1 = yf.Ticker("CL=F").history(start="2026-07-27", end="2026-08-01", interval="1h")
print(h1[["Close","Volume"]].tail(30).to_string())
