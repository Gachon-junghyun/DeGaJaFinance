import sys, warnings, pandas as pd, numpy as np, yfinance as yf
warnings.filterwarnings("ignore"); sys.stdout.reconfigure(encoding="utf-8")
H = pd.Timestamp("2026-08-28")
d = pd.read_pickle(r"C:/Users/fivep/DeGaJaFinance/llm_outputs/sector_flow/prices_2026-09-03.pkl")
cl = d.xs("Close", axis=1, level=1); vo = d.xs("Volume", axis=1, level=1)
official = [t for t in cl.columns if pd.notna(cl.at[H, t])]
d5 = yf.download(official, start="2026-08-28", end="2026-08-29", interval="5m",
                 auto_adjust=False, group_by="ticker", progress=False, threads=True)
proxy = {}
for t in official:
    try: df = d5[t].dropna(how="all")
    except Exception: continue
    df = df[df.index.date == H.date()]
    if df.empty: continue
    proxy[t] = (float(df["Close"].iloc[-1]), float(df["Volume"].sum()))

def obv_norm(c, v):
    obv = (np.sign(c.diff()).fillna(0) * v).cumsum()
    return (obv.iloc[-1] - obv.iloc[-21]) / v.tail(20).sum()
def state(x): return "acc" if x > 0.05 else ("dist" if x < -0.05 else "neu")

rows = []
for t in official:
    if t not in proxy: continue
    pc, pv = proxy[t]
    oc, ov = float(cl.at[H, t]), float(vo.at[H, t])
    c, v = cl[t].dropna(), vo[t].dropna(); c, v = c.align(v, join="inner")
    if len(c) < 25: continue
    true = obv_norm(c, v)
    ch, vh = c.copy(), v.copy(); ch.loc[H] = np.nan; vh.loc[H] = 0.0
    holed = obv_norm(ch, vh)
    cr, vr = c.copy(), v.copy(); cr.loc[H] = pc; vr.loc[H] = pv
    rep = obv_norm(cr, vr)
    rows.append((t, abs(pc-oc)/oc*100, (pv-ov)/ov*100 if ov else np.nan, true, holed, rep))
r = pd.DataFrame(rows, columns=["t","cerr","verr","true","holed","rep"])
for lab, sub in (("ALL n=%d" % len(r), r), ("EX-APH n=%d" % len(r[r.t!="APH"]), r[r.t != "APH"])):
    print("== %s ==" % lab)
    print("  close  mean|err| %.4f pct  max %.4f pct  gt0.05pct: %d"
          % (sub.cerr.mean(), sub.cerr.max(), (sub.cerr > 0.05).sum()))
    print("  volume mean %.2f pct  median %.2f pct  min %.2f pct  max %.2f pct"
          % (sub.verr.mean(), sub.verr.median(), sub.verr.min(), sub.verr.max()))
    for nm, col in (("hole", "holed"), ("repair", "rep")):
        dd = (sub[col] - sub["true"]).abs()
        fl = sum(state(a) != state(b) for a, b in zip(sub[col], sub["true"]))
        sf = sum(np.sign(a) != np.sign(b) for a, b in zip(sub[col], sub["true"]))
        print("  obv-%-6s mean|d| %.4f  median %.4f  max %.4f  label-flips %d/%d  sign-flips %d/%d"
              % (nm, dd.mean(), dd.median(), dd.max(), fl, len(sub), sf, len(sub)))
e = r[r.t != "APH"].assign(dd=(r.rep - r.true))
print("\nrepair worst (ex-APH):", " · ".join("%s %+.3f" % (x.t, x.dd) for x in e.reindex(e.dd.abs().sort_values(ascending=False).index).head(5).itertuples()))
h = r.assign(dd=(r.holed - r.true))
print("hole worst:", " · ".join("%s %+.3f->%+.3f" % (x.t, x.true, x.holed) for x in h.reindex(h.dd.abs().sort_values(ascending=False).index).head(6).itertuples()))
lf = [x.t for x in r.itertuples() if state(x.holed) != state(x.true)]
print("hole label-flip names:", lf)
lf2 = [x.t for x in r.itertuples() if state(x.rep) != state(x.true)]
print("repair label-flip names:", lf2)
