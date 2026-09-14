import warnings, pandas as pd, yfinance as yf
warnings.filterwarnings("ignore")
tk = ["ANET","AVGO","ETN","HPE","MET","MPC","NDAQ","NUE","NVDA","PSX","RTX",
      "SPY","XLK","XLE","XLF","XLV"]
d = yf.download(tk, start="2026-08-18", end="2026-09-05", auto_adjust=False,
                group_by="column", progress=False, threads=True)
cl = d["Close"]
print("rows:", len(cl), " last idx:", cl.index[-1].date())
for ts, row in cl.iterrows():
    n = int(row.isna().sum())
    bad = [c for c in cl.columns if pd.isna(row[c])]
    print(f"{ts.date()}  NaN {n}/{len(cl.columns)}  {bad if bad else ''}")
print("\n-- last-session % change (prev close -> last close) --")
pct = (cl.iloc[-1]/cl.iloc[-2]-1)*100
for t in pct.sort_values(ascending=False).index:
    print(f"  {t:6} {pct[t]:+.2f}%")
