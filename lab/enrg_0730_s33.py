# -*- coding: utf-8 -*-
"""ENRG DEEP 2026-07-30 : S33 재측정(07-28 동결일 + 07-29 정착봉) + 베타 창 민감도"""
import yfinance as yf, pandas as pd, numpy as np

TK = ["069500.KS", "096770.KS", "010950.KS", "078930.KS", "011200.KS",
      "475150.KS", "009830.KS", "322000.KS", "018670.KS", "017940.KS"]

px = yf.download(TK, start="2025-08-01", end="2026-08-01",
                 auto_adjust=False, progress=False)["Close"]
px = px.dropna(how="all")
print("=== 마지막 6봉(종가) ===")
print(px[["069500.KS","096770.KS","010950.KS","078930.KS"]].tail(6).to_string())

r = px.pct_change()
BE = "069500.KS"

def beta(t, win, end):
    s = r.loc[:end, [t, BE]].dropna().tail(win)
    if len(s) < 20: return np.nan, len(s)
    b = np.cov(s[t], s[BE])[0,1] / np.var(s[BE], ddof=1)
    return b, len(s)

for asof in ["2026-07-28", "2026-07-29"]:
    if pd.Timestamp(asof) not in px.index:
        print(f"\n!!! {asof} 봉 결측 (069500 시리즈)"); continue
    rb = r.loc[asof, BE]
    print(f"\n########## asof {asof} · 벤치 {BE} {rb*100:+.3f}% ##########")
    rows = []
    for t in ["096770.KS","010950.KS","078930.KS","011200.KS","475150.KS",
              "009830.KS","322000.KS","018670.KS","017940.KS"]:
        rt = r.loc[asof, t]
        if pd.isna(rt): continue
        b60, n60 = beta(t, 60, asof)
        b_all, nA = beta(t, 10**6, asof)
        b120, n120 = beta(t, 120, asof)
        rows.append(dict(tk=t, abs_pct=rt*100, raw_ex=(rt-rb)*100,
                         b60=b60, res60=(rt-b60*rb)*100,
                         b120=b120, res120=(rt-b120*rb)*100,
                         b_all=b_all, nAll=nA, res_all=(rt-b_all*rb)*100))
    df = pd.DataFrame(rows).set_index("tk")
    print(df.round(3).to_string())
    duo = df.loc[["096770.KS","010950.KS"]]
    print(f"  S33 raw median      = {duo.raw_ex.median():+.3f} pp")
    print(f"  S33 res(b60) median = {duo.res60.median():+.3f} pp")
    print(f"  S33 res(b120) median= {duo.res120.median():+.3f} pp")
    print(f"  S33 res(ball) median= {duo.res_all.median():+.3f} pp")

# 잔차 상관 (R22 재확인)
print("\n=== 잔차 ρ (069500 베타 제거, asof 07-29) ===")
end = "2026-07-29"
def resid(t, win):
    s = r.loc[:end, [t, BE]].dropna().tail(win)
    b = np.cov(s[t], s[BE])[0,1] / np.var(s[BE], ddof=1)
    return s[t] - b*s[BE]
for win in [20, 60, 240]:
    a = resid("096770.KS", win); b = resid("010950.KS", win); g = resid("078930.KS", win)
    idx = a.index.intersection(b.index).intersection(g.index)
    print(f" win={win:3d} n={len(idx):3d}  096770~010950 {np.corrcoef(a[idx],b[idx])[0,1]:+.3f}"
          f" | GS~096770 {np.corrcoef(g[idx],a[idx])[0,1]:+.3f}"
          f" | GS~010950 {np.corrcoef(g[idx],b[idx])[0,1]:+.3f}")

# 베타 시계열 안정성 (010950 음수 β = 창 아티팩트 D82 검증)
print("\n=== 010950 / 096770 베타 창 민감도 (asof 07-29) ===")
for t in ["010950.KS","096770.KS"]:
    out=[]
    for w in [20,40,60,90,120,180,240]:
        b,n = beta(t,w,end); out.append(f"w{w}={b:+.3f}(n{n})")
    print(f" {t}: " + "  ".join(out))
