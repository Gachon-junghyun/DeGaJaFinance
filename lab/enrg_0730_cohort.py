# -*- coding: utf-8 -*-
"""C1 준수: 절대 RS 금지 → 코호트 차감. + 시총 + 07-29 정착 잔차 코호트 순위"""
import json, numpy as np, pandas as pd, yfinance as yf

j = json.load(open('llm_outputs/2026-07-30/industry_KR/SECTOR_FLOW_KR.json', encoding='utf-8'))
N = pd.DataFrame(j['names'])
N["code"] = N.ticker.str.split(".").str[0]

ENRG = {"096770":"SK이노베이션","010950":"S-Oil","078930":"GS","011200":"HMM",
        "018670":"SK가스","017940":"E1","002960":"한국쉘석유","014530":"극동유화",
        "006650":"대한유화","001740":"SK네트웍스","017390":"서울도시가스"}
RENEW = {"475150":"SK이터닉스","009830":"한화솔루션","322000":"HD현대에너지솔루션",
         "112610":"씨에스윈드","267260":"HD현대일렉트릭"}

print("=== 코호트 베이스라인 (C1: 절대 RS 금지) ===")
print(f" all-827  rs20 중앙값 = {N.rs20.median():.1f} · rs60 중앙값 = {N.rs60.median():.1f}")
top30 = N.nlargest(30, "mcap")
print(f" top30    rs20 중앙값 = {top30.rs20.median():.1f} · rs60 중앙값 = {top30.rs60.median():.1f}")
sub = N[N.code.isin(ENRG)]
print(f" ENRG-11  rs20 중앙값 = {sub.rs20.median():.1f} · rs60 중앙값 = {sub.rs60.median():.1f}")
sub2 = N[N.code.isin(RENEW)]
print(f" 신재생-5  rs20 중앙값 = {sub2.rs20.median():.1f} · rs60 중앙값 = {sub2.rs60.median():.1f}")
print(f" all-827  rs60>0 비중 = {(N.rs60>0).mean()*100:.1f}%")

print("\n=== 플레이어: 시총 + 코호트 차감 RS (⚠ RS는 07-30 장중 미완성 봉) ===")
rows=[]
for code, nm in list(ENRG.items())+list(RENEW.items()):
    r = N[N.code==code]
    if len(r)==0: continue
    r = r.iloc[0]
    rows.append(dict(code=code, name=nm, leg=("정유·가스" if code in ENRG else "신재생·전력"),
                     mcap_jo=r.mcap/1e12 if pd.notna(r.mcap) else np.nan,
                     tag=r.tag, obv=r.obv_state, surge=r.vol_surge,
                     rs20_abs=r.rs20, rs20_vs_all=r.rs20-N.rs20.median(),
                     rs60_abs=r.rs60, rs60_vs_all=r.rs60-N.rs60.median(),
                     last=r.last))
df = pd.DataFrame(rows).sort_values("mcap_jo", ascending=False)
print(df.round(2).to_string(index=False))
print(f"\n 시총 ≥3조 = {(df.mcap_jo>=3).sum()}종 / 전체 {len(df)}종")

# 07-29 정착 잔차의 코호트 내 위치
print("\n=== 07-29 정착 잔차(β60d) 코호트 순위 — all-827 대비가 아니라 ENRG 내부 ===")
tks = [c+".KS" for c in list(ENRG)+list(RENEW)] + ["069500.KS"]
px = yf.download(tks, start="2025-08-01", end="2026-07-30", auto_adjust=False, progress=False)["Close"]
r = px.pct_change(fill_method=None)
BE="069500.KS"; asof="2026-07-29"; rb=r.loc[asof,BE]
out=[]
for c,nm in list(ENRG.items())+list(RENEW.items()):
    t=c+".KS"
    if t not in r.columns or pd.isna(r.loc[asof,t]): continue
    s=r[[t,BE]].dropna().tail(60)
    b=np.cov(s[t],s[BE])[0,1]/np.var(s[BE],ddof=1)
    out.append(dict(code=c,name=nm,abs_pct=r.loc[asof,t]*100,
                    raw_ex=(r.loc[asof,t]-rb)*100,b60=b,res60=(r.loc[asof,t]-b*rb)*100))
o=pd.DataFrame(out).sort_values("res60",ascending=False)
print(f" 벤치 {BE} 07-29 = {rb*100:+.3f}%")
print(o.round(3).to_string(index=False))
print(f"\n 정유·가스 레그 잔차 중앙값 = {o[o.code.isin(ENRG)].res60.median():+.3f}")
print(f" 신재생·전력 레그 잔차 중앙값 = {o[o.code.isin(RENEW)].res60.median():+.3f}")
print(f" ⇒ 레그 간 스프레드 = {o[o.code.isin(ENRG)].res60.median()-o[o.code.isin(RENEW)].res60.median():+.3f} pp")
print(f" ENRG 레그 내부 스프레드(max-min) = {o[o.code.isin(ENRG)].res60.max()-o[o.code.isin(ENRG)].res60.min():+.3f} pp")
