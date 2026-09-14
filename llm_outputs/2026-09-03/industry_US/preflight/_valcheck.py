import sys, warnings, pandas as pd, numpy as np, yfinance as yf
warnings.filterwarnings("ignore"); sys.stdout.reconfigure(encoding="utf-8")
H = pd.Timestamp("2026-08-28")
d = pd.read_pickle(r"C:/Users/fivep/DeGaJaFinance/llm_outputs/sector_flow/prices_2026-09-03.pkl")
cl = d.xs("Close", axis=1, level=1); vo = d.xs("Volume", axis=1, level=1)
official = [t for t in cl.columns if pd.notna(cl.at[H, t])]
print("official n =", len(official))
d5 = yf.download(official, start="2026-08-28", end="2026-08-29", interval="5m",
                 auto_adjust=False, group_by="ticker", progress=False, threads=True)
rows = []
for t in official:
    try: df = d5[t].dropna(how="all")
    except Exception: continue
    df = df[df.index.date == H.date()]
    if df.empty: continue
    pc = float(df["Close"].iloc[-1]); po = float(df["Open"].iloc[0])
    pv = float(df["Volume"].sum())
    oc = float(cl.at[H, t]); ov = float(vo.at[H, t])
    rows.append((t, oc, pc, abs(pc-oc)/oc*100, ov, pv, (pv-ov)/ov*100 if ov else np.nan,
                 float(d[(t,"Open")].loc[H]) if (t,"Open") in d.columns else np.nan, po))
r = pd.DataFrame(rows, columns=["t","off_close","proxy_close","close_err%","off_vol","proxy_vol","vol_err%","off_open","proxy_open"])
r = r.sort_values("close_err%", ascending=False)
print(r.head(8).to_string(index=False))
sub = r[r["close_err%"] < 50]
print("\n-- excluding outliers >50% err (n=%d) --" % len(sub))
print("close mean|err| %.4f%%  max %.4f%%  >0.05%%: %d" % (sub["close_err%"].mean(), sub["close_err%"].max(), (sub["close_err%"]>0.05).sum()))
print("volume mean %.2f%%  median %.2f%%  min %.2f%%  max %.2f%%" % (sub["vol_err%"].mean(), sub["vol_err%"].median(), sub["vol_err%"].min(), sub["vol_err%"].max()))
print("\nvol worst:"); print(r.nsmallest(4,"vol_err%")[["t","off_vol","proxy_vol","vol_err%"]].to_string(index=False))
