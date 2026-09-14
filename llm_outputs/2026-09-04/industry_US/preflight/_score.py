import warnings, pandas as pd, numpy as np, yfinance as yf
warnings.filterwarnings("ignore")
tk = ["SPY","MRVL","AVGO","MSFT","T","VZ","HPE","DELL","NUE","STLD","FRO","SMH","XLF","XLU","XLRE","XLP"]
d = yf.download(tk, start="2026-06-01", end="2026-09-04", auto_adjust=False, group_by="column", progress=False, threads=True)
cl = d["Close"].loc[:"2026-09-03"].dropna(how="all")
print("last row:", cl.index[-1].date(), " NaN:", int(cl.iloc[-1].isna().sum()))
idx = list(cl.index)
def pos(ds): return idx.index(pd.Timestamp(ds))
def exc(t, end, n):
    e = pos(end); b = e - n
    r = (cl[t].iloc[e]/cl[t].iloc[b]-1)*100
    s = (cl["SPY"].iloc[e]/cl["SPY"].iloc[b]-1)*100
    return r - s, cl.index[b].date(), cl[t].iloc[b], cl[t].iloc[e]
def excwin(t, start, end):
    b, e = pos(start), pos(end)
    r = (cl[t].iloc[e]/cl[t].iloc[b]-1)*100
    s = (cl["SPY"].iloc[e]/cl["SPY"].iloc[b]-1)*100
    return r - s
def verdict(v, a, b, aop, bop):
    ha = (v >= a) if aop == ">=" else (v <= a)
    hb = (v >= b) if bop == ">=" else (v <= b)
    return "A" if ha else ("B" if hb else "C")

print("\n=== S109  FRO exc5, 08-26 -> 09-02 close · A>=+8.043 · B<=-4.620 ===")
v = excwin("FRO","2026-08-26","2026-09-02")
print(f"  FRO {cl['FRO'].loc['2026-08-26']:.2f} -> {cl['FRO'].loc['2026-09-02']:.2f} | SPY {cl['SPY'].loc['2026-08-26']:.2f} -> {cl['SPY'].loc['2026-09-02']:.2f}")
print(f"  exc5 = {v:+.4f}pp  => FIRED-{verdict(v,8.043,-4.620,'>=','<=')}")

print("\n=== S105  [MRVL exc10] - [AVGO exc10] @09-03 · A<=-10.836 · B>=+30.484 ===")
m,bd,p0,p1 = exc("MRVL","2026-09-03",10); a,_,q0,q1 = exc("AVGO","2026-09-03",10)
print(f"  base {bd} | MRVL {p0:.2f}->{p1:.2f} exc10 {m:+.4f} | AVGO {q0:.2f}->{q1:.2f} exc10 {a:+.4f}")
v=m-a; print(f"  spread = {v:+.4f}pp  => FIRED-{verdict(v,-10.836,30.484,'<=','>=')}")

print("\n=== S106  MSFT exc10 @09-03 · A>=+7.969 · B<=-9.184 ===")
v,bd,p0,p1 = exc("MSFT","2026-09-03",10)
print(f"  base {bd} MSFT {p0:.2f}->{p1:.2f}  exc10 = {v:+.4f}pp  => FIRED-{verdict(v,7.969,-9.184,'>=','<=')}")

print("\n=== S107  EW{T,VZ} exc10 @09-03 · A>=+12.244 · B<=-9.533 ===")
t_,_,t0,t1 = exc("T","2026-09-03",10); z_,_,z0,z1 = exc("VZ","2026-09-03",10)
v=(t_+z_)/2
print(f"  T {t0:.2f}->{t1:.2f} exc10 {t_:+.4f} | VZ {z0:.2f}->{z1:.2f} exc10 {z_:+.4f}")
print(f"  EW = {v:+.4f}pp  => FIRED-{verdict(v,12.244,-9.533,'>=','<=')}")

print("\n=== S110  [HPE exc5] - [DELL exc5] @09-03 · A>=+6.022 · B<=-6.141 ===")
h,bd,h0,h1 = exc("HPE","2026-09-03",5); dd,_,d0,d1 = exc("DELL","2026-09-03",5)
print(f"  base {bd} | HPE {h0:.2f}->{h1:.2f} exc5 {h:+.4f} | DELL {d0:.2f}->{d1:.2f} exc5 {dd:+.4f}")
v=h-dd; print(f"  spread = {v:+.4f}pp  => FIRED-{verdict(v,6.022,-6.141,'>=','<=')}")

print("\n=== S114  EW{NUE,STLD} exc5, 08-26 -> 09-03 close · A<=-6.219 · B>=+0.826 ===")
n_=excwin("NUE","2026-08-26","2026-09-03"); s_=excwin("STLD","2026-08-26","2026-09-03")
v=(n_+s_)/2
print(f"  NUE {cl['NUE'].loc['2026-08-26']:.2f}->{cl['NUE'].loc['2026-09-03']:.2f} exc {n_:+.4f} | STLD {cl['STLD'].loc['2026-08-26']:.2f}->{cl['STLD'].loc['2026-09-03']:.2f} exc {s_:+.4f}")
print(f"  EW = {v:+.4f}pp  => FIRED-{verdict(v,-6.219,0.826,'<=','>=')}")

print("\n=== AVGO exc1 09-02 -> 09-03 (S132 A>=+9 B<=-9 · S138 A>=+11 B<=-11) ===")
v,bd,p0,p1 = exc("AVGO","2026-09-03",1)
print(f"  AVGO {p0:.2f}->{p1:.2f} = {(p1/p0-1)*100:+.3f}% | SPY {cl['SPY'].iloc[-2]:.2f}->{cl['SPY'].iloc[-1]:.2f} = {(cl['SPY'].iloc[-1]/cl['SPY'].iloc[-2]-1)*100:+.3f}%")
print(f"  exc1 = {v:+.4f}pp  => S132 FIRED-{verdict(v,9.0,-9.0,'>=','<=')} · S138 FIRED-{verdict(v,11.0,-11.0,'>=','<=')}")

print("\n=== S141  SMH exc1 09-02 -> 09-03 · A>=+1.802 · B<=-1.732 ===")
v,bd,p0,p1 = exc("SMH","2026-09-03",1)
print(f"  SMH {p0:.2f}->{p1:.2f}  exc1 = {v:+.4f}pp  => FIRED-{verdict(v,1.802,-1.732,'>=','<=')}")

print("\n=== NOT SETTLED (need the 09-04 close) — reference states only, NOT scores ===")
v=excwin("XLF","2026-08-28","2026-09-03"); print(f"  S134 XLF exc(08-28->09-03, 4 of 5 sessions) = {v:+.4f}pp   [A>=+2.00 B<=-2.00 at the 09-04 close]")
u=excwin("XLU","2026-09-01","2026-09-03"); r=excwin("XLRE","2026-09-01","2026-09-03"); p=excwin("XLP","2026-09-01","2026-09-03")
print(f"  S139 EW{{XLU {u:+.3f}, XLRE {r:+.3f}, XLP {p:+.3f}}} = {(u+r+p)/3:+.4f}pp over 2 of 3 sessions  [A>=+1.653 B<=-1.757 at the 09-04 close]")
