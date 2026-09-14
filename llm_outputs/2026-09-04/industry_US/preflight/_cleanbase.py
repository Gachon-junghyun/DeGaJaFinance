"""G2 upgrade: the stored 09-02 baseline was scored on the HOLED cache (08-28 missing for 258
names). Today's cache is healed. Recompute a CLEAN 09-02 baseline from the healed cache truncated
to <=09-02, so today's delta is healed-minus-healed. History is NOT written."""
import sys, json, pickle, warnings
from pathlib import Path
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
ROOT = Path(r"C:/Users/fivep/DeGaJaFinance")
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "scripts"))
import sector_flow as SF
def log(*a): print(*a, file=sys.stderr, flush=True)

CUT = pd.Timestamp("2026-09-02")
data = pickle.load(open(ROOT / "llm_outputs/sector_flow/prices_2026-09-04.pkl", "rb"))
trunc = data.loc[:CUT]
log(f"[clean] healed cache rows {len(data)} -> truncated {len(trunc)}  last {trunc.index[-1].date()}")

SF.MKT, SF.UNIVERSE, SF.BENCH, SF.COLS = "us", SF.MARKETS["us"]["universe"], SF.MARKETS["us"]["bench"], SF.MARKETS["us"]
rows_u = SF.load_universe(None, None)
bclose = SF.slice_frame(trunc, SF.BENCH)["Close"].astype(float)
res = [SF.one_name(r, bclose, trunc, False, False) for r in rows_u]
meta = SF.score_all(res, False)
clean = {r["ticker"]: r["flow_score"] for r in res if r.get("flow_score") is not None}
log(f"[clean] rescored 09-02 on healed data: {json.dumps(meta)}")

hist = json.load(open(ROOT / "llm_outputs/sector_flow/history.json", encoding="utf-8"))
holed = {k: v[0] for k, v in hist["2026-09-02"].items() if k != "_mode" and isinstance(v, list)}
both = sorted(set(clean) & set(holed))
d = np.array([clean[t] - holed[t] for t in both])
log(f"[baseline contamination] n={len(both)}  mean|d| {np.abs(d).mean():.4f}  median {np.median(np.abs(d)):.4f}"
    f"  max {np.abs(d).max():.4f}  sign-flips {int(sum(np.sign(clean[t])!=np.sign(holed[t]) for t in both))}/{len(both)}")
w = sorted(both, key=lambda t: -abs(clean[t]-holed[t]))[:8]
log("[baseline worst] " + " · ".join(f"{t} {holed[t]:+.3f}->{clean[t]:+.3f}" for t in w))

# today's healed snapshot
today = json.load(open(ROOT / "llm_outputs/2026-09-04/industry_US/SECTOR_FLOW_US.json", encoding="utf-8"))
cur = {n["ticker"]: n for n in today["names"] if n.get("flow_score") is not None}

# clean one-session delta, per name and per sector (cap-weighted + equal-weighted)
recs = []
for t, n in cur.items():
    if t in clean:
        recs.append(dict(ticker=t, sector=n["sector"], mcap=n.get("mcap") or 0.0,
                         cur=n["flow_score"], base=clean[t],
                         d_clean=n["flow_score"] - clean[t],
                         d_stored=n.get("delta")))
df = pd.DataFrame(recs)
log(f"[delta] names with clean delta: {len(df)}")
out = {}
for sec, g in df.groupby("sector"):
    wsum = g["mcap"].sum()
    out[sec] = dict(n=len(g),
                    d_clean_w=float((g["d_clean"] * g["mcap"]).sum() / wsum) if wsum else None,
                    d_clean_eq=float(g["d_clean"].mean()),
                    d_stored_w=float((g["d_stored"].fillna(0) * g["mcap"]).sum() / wsum) if wsum else None)
print(json.dumps(dict(sectors=out,
                      names={r.ticker: dict(cur=r.cur, base=r.base, d=r.d_clean) for r in df.itertuples()}),
                 ensure_ascii=False))
log("\n[sector clean delta, cap-weighted]")
for sec, v in sorted(out.items(), key=lambda kv: -(kv[1]["d_clean_w"] or 0)):
    log(f"  {sec:24} clean {v['d_clean_w']:+.3f}   (stored {v['d_stored_w']:+.3f})   eq {v['d_clean_eq']:+.3f}  n={v['n']}")
top = df.sort_values("d_clean", ascending=False)
log("\n[name movers up]   " + " · ".join(f"{r.ticker} {r.d_clean:+.2f}" for r in top.head(10).itertuples()))
log("[name movers down] " + " · ".join(f"{r.ticker} {r.d_clean:+.2f}" for r in top.tail(10).itertuples()))
