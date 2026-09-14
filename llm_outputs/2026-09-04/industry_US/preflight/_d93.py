"""D93: trailing-252 distributions computed BEFORE the thresholds are frozen."""
import warnings, numpy as np, pandas as pd, yfinance as yf
warnings.filterwarnings("ignore")
def pct(s, ps=(5,15,50,85,95)):
    a=np.asarray(s,dtype=float); a=a[~np.isnan(a)]
    return dict(n=len(a), mean=round(float(a.mean()),4), sd=round(float(a.std(ddof=1)),4),
                **{f"p{p:02d}": round(float(np.percentile(a,p)),4) for p in ps})

print("=== P136: (^FVX - ^TYX) 3-session CHANGE, in bp ===")
d=yf.download(["^FVX","^TYX"],start="2024-06-01",end="2026-09-04",auto_adjust=False,group_by="column",progress=False,threads=True)["Close"].loc[:"2026-09-03"].dropna()
sp=(d["^FVX"]-d["^TYX"])*100          # bp
ch=sp.diff(3).dropna()
print("  full n",len(ch)); print("  trailing252:",pct(ch.tail(252)))
print(f"  STATE @09-03: spread {sp.iloc[-1]:.1f}bp · 3-session change {ch.iloc[-1]:+.1f}bp")
print(f"    (09-01 change {ch.loc['2026-09-01']:+.1f} · 09-02 {ch.loc['2026-09-02']:+.1f})")
r=np.asarray(ch.tail(252)); print(f"  state percentile: {(r<ch.iloc[-1]).mean()*100:.1f}")

print("\n=== P137: EW{Comm-ex-Alphabet} minus EW{GOOGL,GOOG}, 5-session return spread, pp ===")
EX=["META","NFLX","TMUS","VZ","DIS","T","CMCSA","WBD","TTWO","LYV"]; AL=["GOOGL","GOOG"]
d=yf.download(EX+AL,start="2024-06-01",end="2026-09-04",auto_adjust=False,group_by="column",progress=False,threads=True)["Close"].loc[:"2026-09-03"].dropna()
r5=d.pct_change(5)*100
spread=r5[EX].mean(axis=1)-r5[AL].mean(axis=1)
spread=spread.dropna()
print("  full n",len(spread)); print("  trailing252:",pct(spread.tail(252)))
print(f"  STATE @09-03: {spread.iloc[-1]:+.4f}pp")
r=np.asarray(spread.tail(252)); print(f"  state percentile: {(r<spread.iloc[-1]).mean()*100:.1f}")
print("  members priced 09-03:", {t: round(float(d[t].iloc[-1]),2) for t in EX+AL})

print("\n=== P138: USDJPY 5-session % change ===")
d=yf.download(["JPY=X","^TYX"],start="2024-06-01",end="2026-09-04",auto_adjust=False,group_by="column",progress=False,threads=True)["Close"].loc[:"2026-09-03"].dropna()
ch=(d["JPY=X"].pct_change(5)*100).dropna()
print("  full n",len(ch)); print("  trailing252:",pct(ch.tail(252)))
print(f"  STATE @09-03: USDJPY {d['JPY=X'].iloc[-1]:.3f} · 5-session change {ch.iloc[-1]:+.4f}%")
r=np.asarray(ch.tail(252)); print(f"  state percentile: {(r<ch.iloc[-1]).mean()*100:.1f}")
t3=(d["^TYX"].diff(5)*100).iloc[-1]; print(f"  KPI ^TYX 5-session change: {t3:+.1f}bp · level {d['^TYX'].iloc[-1]:.3f}")
