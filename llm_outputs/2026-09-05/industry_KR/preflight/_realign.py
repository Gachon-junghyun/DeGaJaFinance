# -*- coding: utf-8 -*-
"""PREFLIGHT G0/G2/G3 측정 — as-run 스윕이 scored=0 으로 죽었을 때의 정렬 재채점.

수식 이식 0: scripts/sector_flow.py 함수를 그대로 호출한다.
  A 정렬  : 벤치 = ^KS11 Close 결측제거(끝 2026-09-03) · 종목 끝 09-04  → [measured] 만
  C 임퓨트: 벤치 09-04 = A마지막 × (1+069500.KS 09-03→09-04 수익률)     → [inferred] 1칸
as-run 은 벤치 Close 09-04 = NaN 이라 rs 전량 NaN → 825종 전량 점수 미부여(scored=0).
"""
import sys, json, importlib.util, statistics as st
from pathlib import Path
import pandas as pd

ROOT = Path("C:/Users/fivep/DeGaJaFinance"); sys.path.insert(0, str(ROOT/"scripts"))
spec = importlib.util.spec_from_file_location("sf", ROOT/"scripts"/"sector_flow.py")
sf = importlib.util.module_from_spec(spec); spec.loader.exec_module(sf)
mk = sf.MARKETS["kr"]
sf.MKT, sf.UNIVERSE, sf.BENCH, sf.COLS = "kr", mk["universe"], mk["bench"], mk
sf.HISTORY = sf.OUT_DIR / "history_kr.json"          # ★ 시장 네임스페이스(main() 과 동일)

rows = sf.load_universe(None, None)
d = pd.read_pickle(ROOT/"llm_outputs"/"sector_flow"/"prices_kr_2026-09-05.pkl")
bA = sf.slice_frame(d, "^KS11")["Close"].astype(float).dropna()
PROXY = (103610.0, 105720.0)                          # 069500.KS 09-03 → 09-04 (G0 실측)
r1 = PROXY[1]/PROXY[0] - 1
imp = float(bA.iloc[-1]) * (1 + r1)
bC = pd.concat([bA, pd.Series({pd.Timestamp('2026-09-04'): imp})])

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

A, mA = run(bA); C, mC = run(bC)
hist = sf.load_history()
prev = sf.prev_snapshot(hist, "2026-09-04", "nonews")
prev_key = max((k for k in hist if k < "2026-09-04" and sum(1 for x in hist[k] if not x.startswith("_"))>0), default=None)
secC = sf.aggregate_sectors(C, prev); secA = sf.aggregate_sectors(A, prev)
da = {r["ticker"]: r for r in A}; dc = {r["ticker"]: r for r in C}

rep = {"note":"as-run scored=0 (벤치 Close 09-04 NaN) → 이 파일이 대체 채점",
       "bench_last_measured":"2026-09-03", "bench_0904_imputed": round(imp,2),
       "proxy":"069500.KS 103,610→105,720 (+2.036%) [inferred]",
       "prev_snapshot_key": prev_key, "prev_n": len(prev),
       "meta_A": mA, "meta_C": mC, "sectors_C": secC, "sectors_A": secA, "names_C": C, "names_A": A}
Path(__file__).parent.joinpath("_realign.json").write_text(
    json.dumps(rep, ensure_ascii=False, default=str), encoding="utf-8")

def summ(res, l):
    v=[r for r in res if r.get("flow_score") is not None]; W=sum(r["mcap"] for r in v) or 1
    print(f"{l}: n={len(v)} mean={sum(r['flow_score'] for r in v)/len(v):+.4f} "
          f"wflow={sum(r['flow_score']*r['mcap'] for r in v)/W:+.4f} "
          f"ge+0.5={sum(1 for r in v if r['flow_score']>=.5)} le-0.5={sum(1 for r in v if r['flow_score']<=-.5)} "
          f"G={sum(1 for r in v if r['tag']=='🟢가속')} R={sum(1 for r in v if r['tag']=='🔴분산')}")
print(f"[prev] key={prev_key} n={len(prev)}  (Δ 기준선 — 1세션이 아니다)")
summ(A,"A 정렬"); summ(C,"C 임퓨트")
for ax in ("rs20","rs60","flow_score"):
    v=[(da[t][ax]-dc[t][ax]) for t in da if da[t].get(ax) is not None and dc[t].get(ax) is not None]
    print(f"  정렬편의 Δ({ax}) A−C: 중앙 {st.median(v):+.3f} 평균 {sum(v)/len(v):+.3f} 양(+) {sum(1 for x in v if x>0)/len(v):.1%} n={len(v)}")
flip=[s for s in secC if s.get("top1_flips_sign")]
print(f"[G3·C] 섹터 {len(secC)} · 플리퍼 {len(flip)}")
for s in flip:
    print(f"   {s['sector']:9s} n={s['n']:3d} wflow={s['wflow']:+.3f} eqflow={s['eqflow']:+.3f} breadth={s['breadth']:.2f} "
          f"Δ={s['delta']} top1={s.get('top1_name')}({s.get('top1_w')}%) ex={s.get('wflow_ex_top1'):+.3f}")
print("[top8 wflow·C]")
for s in secC[:8]: print(f"   {s['sector']:9s} n={s['n']:3d} wflow={s['wflow']:+.3f} eq={s['eqflow']:+.3f} br={s['breadth']:.2f} Δ={s['delta']}")
print("[bottom6 wflow·C]")
for s in secC[-6:]: print(f"   {s['sector']:9s} n={s['n']:3d} wflow={s['wflow']:+.3f} eq={s['eqflow']:+.3f} br={s['breadth']:.2f} Δ={s['delta']}")
