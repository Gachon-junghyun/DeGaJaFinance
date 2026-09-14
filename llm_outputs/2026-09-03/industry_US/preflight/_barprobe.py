import yfinance as yf, pandas as pd, sys
sys.stdout.reconfigure(encoding='utf-8')
tk = ["ANET","AVGO","ETN","HPE","MET","MPC","NDAQ","NUE","NVDA","PSX","RTX","SPY","XLE","XLU","XLK","SMH"]
d = yf.download(tk, start="2026-08-18", end="2026-09-04", auto_adjust=False, progress=False, group_by="column")
cl = d["Close"]
print("rows:", list(cl.index.strftime("%Y-%m-%d")))
for ix, row in cl.iterrows():
    n = int(row.isna().sum())
    print(ix.strftime("%Y-%m-%d"), "NaN", n, "/", len(tk), ("  -> "+",".join(row[row.isna()].index)) if n else "")
