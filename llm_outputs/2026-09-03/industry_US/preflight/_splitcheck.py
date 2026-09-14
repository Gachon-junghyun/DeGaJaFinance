import sys, warnings, pandas as pd, numpy as np, yfinance as yf
warnings.filterwarnings("ignore"); sys.stdout.reconfigure(encoding="utf-8")
H = pd.Timestamp("2026-08-28")
d = pd.read_pickle(r"C:/Users/fivep/DeGaJaFinance/llm_outputs/sector_flow/prices_2026-09-03.pkl")
cl = d.xs("Close", axis=1, level=1)
tickers = sorted(set(d.columns.get_level_values(0)))
missing = [t for t in tickers if pd.isna(cl.at[H, t])]
print("missing n =", len(missing))
# neighbour reference: 08-27 and 08-31 official closes
prev, nxt = pd.Timestamp("2026-08-27"), pd.Timestamp("2026-08-31")
out = []
B = 40
for i in range(0, len(missing), B):
    ch = missing[i:i+B]
    d5 = yf.download(ch, start="2026-08-28", end="2026-08-29", interval="5m",
                     auto_adjust=False, group_by="ticker", progress=False, threads=True)
    for t in ch:
        try: df = d5[t].dropna(how="all")
        except Exception: continue
        df = df[df.index.date == H.date()]
        if df.empty: continue
        pc = float(df["Close"].iloc[-1])
        a, b = cl.at[prev, t], cl.at[nxt, t]
        if pd.isna(a) or pd.isna(b): continue
        ref = (float(a) + float(b)) / 2
        out.append((t, ref, pc, pc/ref))
r = pd.DataFrame(out, columns=["t","neighbour_avg","proxy_close","ratio"])
print("n compared =", len(r))
bad = r[(r["ratio"] > 1.25) | (r["ratio"] < 0.8)]
print("names whose 5m proxy is >25pct off its 08-27/08-31 neighbours:", len(bad))
print(bad.sort_values("ratio").to_string(index=False) if len(bad) else "  (none)")
print("\nratio distribution: min %.4f  p1 %.4f  median %.4f  p99 %.4f  max %.4f"
      % (r.ratio.min(), r.ratio.quantile(.01), r.ratio.median(), r.ratio.quantile(.99), r.ratio.max()))
