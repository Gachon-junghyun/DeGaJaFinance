# -*- coding: utf-8 -*-
"""정정 재채점 D — 벤치 09-04 를 **실측**으로 채운다.

PREFLIGHT G0 은 "^KS11 09-04 종가는 존재하지 않는다"고 적었다. **틀렸다.**
yfinance 에 없을 뿐이고 `module_KIS --futopt A05609` 의 기초지수 필드가
**종합 6,687.21 (+1.64%)** 를 준다(교차확인: brief 머리층 "[스팟]코스피 107.73포인트(1.64%) 오른 6687.21 마감").
=> 변종 C(069500 프록시 임퓨트 6,713.47, [inferred])를 **D(6,687.21, [measured])** 로 대체한다.
"""
import sys, json, importlib.util, statistics as st
from pathlib import Path
import pandas as pd

ROOT = Path("C:/Users/fivep/DeGaJaFinance"); sys.path.insert(0, str(ROOT/"scripts"))
spec = importlib.util.spec_from_file_location("sf", ROOT/"scripts"/"sector_flow.py")
sf = importlib.util.module_from_spec(spec); spec.loader.exec_module(sf)
mk = sf.MARKETS["kr"]
sf.MKT, sf.UNIVERSE, sf.BENCH, sf.COLS = "kr", mk["universe"], mk["bench"], mk
sf.HISTORY = sf.OUT_DIR / "history_kr.json"

rows = sf.load_universe(None, None)
d = pd.read_pickle(ROOT/"llm_outputs"/"sector_flow"/"prices_kr_2026-09-05.pkl")
bA = sf.slice_frame(d, "^KS11")["Close"].astype(float).dropna()      # 끝 09-03 6,579.48
KIS_0904 = 6687.21                                                    # [measured] module_KIS --futopt
bD = pd.concat([bA, pd.Series({pd.Timestamp('2026-09-04'): KIS_0904})])
IMP_C = float(bA.iloc[-1]) * (105720/103610)                          # 앞 런의 [inferred] 값

def run(bench):
    res = []
    for r in rows:
        df = sf.slice_frame(d, r["ticker"])
        if df is None:
            res.append({**r, "error": "empty", "flow_score": None, "tag": "?", "velocity": None}); continue
        p = sf.flow_read.price_flow(r["ticker"], bench, df=df)
        o = {**r, "flow_score": None, "velocity": None,
             "tag": sf.flow_read.flow_tag(p, None) if "error" not in p else "?"}
        if "error" in p: o["error"] = p["error"]
        else: o.update({k: p[k] for k in ("last","obv_norm","obv_state","rs20","rs60","vol_surge")})
        res.append(o)
    return res, sf.score_all(res, use_news=False)

A, mA = run(bA); C, mC = run(pd.concat([bA, pd.Series({pd.Timestamp('2026-09-04'): IMP_C})])); D, mD = run(bD)
hist = sf.load_history(); prev = sf.prev_snapshot(hist, "2026-09-04", "nonews")
prev_key = max((k for k in hist if k < "2026-09-04" and sum(1 for x in hist[k] if not x.startswith("_"))>0), default=None)
secD = sf.aggregate_sectors(D, prev)
da, dc, dd = ({r["ticker"]: r for r in X} for X in (A, C, D))

print(f"[bench] 09-03 {bA.iloc[-1]:,.2f} [measured yf] · 09-04 {KIS_0904:,.2f} [measured KIS] "
      f"(직전 임퓨트 {IMP_C:,.2f} [inferred] ⇒ 오차 {IMP_C-KIS_0904:+.2f} = {(IMP_C/KIS_0904-1)*100:+.3f}%)")
print(f"[prev] key={prev_key} n={len(prev)}")
def summ(res, l):
    v=[r for r in res if r.get("flow_score") is not None]; W=sum(r["mcap"] for r in v) or 1
    print(f"{l}: n={len(v)} mean={sum(r['flow_score'] for r in v)/len(v):+.4f} "
          f"wflow={sum(r['flow_score']*r['mcap'] for r in v)/W:+.4f} "
          f"ge+0.5={sum(1 for r in v if r['flow_score']>=.5)} le-0.5={sum(1 for r in v if r['flow_score']<=-.5)} "
          f"G={sum(1 for r in v if r['tag']=='🟢가속')} Y={sum(1 for r in v if r['tag']=='🟡중립')} R={sum(1 for r in v if r['tag']=='🔴분산')}")
summ(A,"A 정렬(벤치09-03)"); summ(C,"C 임퓨트(inferred)"); summ(D,"★D 실측(measured)")
for lbl, x in (("A−D 정렬편의", da), ("C−D 임퓨트오차", dc)):
    for ax in ("rs20","rs60","flow_score"):
        v=[(x[t][ax]-dd[t][ax]) for t in dd if x[t].get(ax) is not None and dd[t].get(ax) is not None]
        print(f"  {lbl} Δ({ax}): 중앙 {st.median(v):+.3f} 평균 {sum(v)/len(v):+.3f} 양(+) {sum(1 for y in v if y>0)/len(v):.1%} n={len(v)}")
same=sum(1 for t in dc if dc[t].get("flow_score") is not None and dc[t]["flow_score"]==dd[t].get("flow_score"))
print("  C 와 D 의 점수 동일:", same, "/", mD["scored"])
flip=[s for s in secD if s.get("top1_flips_sign")]
print(f"[G3·D] 섹터 {len(secD)} · 플리퍼 {len(flip)}")
for s in flip:
    print(f"   {s['sector']:9s} n={s['n']:3d} wflow={s['wflow']:+.3f} eqflow={s['eqflow']:+.3f} br={s['breadth']:.2f} Δ={s['delta']} top1={s.get('top1_name')}({s.get('top1_w')}%) ex={s.get('wflow_ex_top1'):+.3f}")
print("[전 섹터 · D]")
for s in secD:
    print(f"   {s['sector']:10s} n={s['n']:3d} wflow={s['wflow']:+.3f} eq={s['eqflow']:+.3f} br={s['breadth']:.2f} G={s['green']} R={s['red']} Δ={s['delta']} flip={s.get('top1_flips_sign')} top1={s.get('top1_name')}({s.get('top1_w')}%)")
Path(__file__).parent.joinpath("_realign_D.json").write_text(json.dumps(
    {"bench_0903": float(bA.iloc[-1]), "bench_0904_measured": KIS_0904, "bench_0904_inferred_prev": IMP_C,
     "source": "module_KIS --futopt A05609 기초지수 종합 · 교차확인 brief 09-04 머리층",
     "prev_snapshot_key": prev_key, "prev_n": len(prev),
     "meta_D": mD, "meta_C": mC, "meta_A": mA, "sectors_D": secD, "names_D": D},
    ensure_ascii=False, default=str), encoding="utf-8")
print("[saved] _realign_D.json")
