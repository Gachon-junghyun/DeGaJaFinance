"""One-run repair: patch the frozen 2026-08-28 vendor hole with 5m-aggregated bars,
then rescore the sweep with sector_flow's own functions. History is NOT written."""
import sys, json, pickle, warnings
from pathlib import Path
import numpy as np, pandas as pd, yfinance as yf
warnings.filterwarnings("ignore")
ROOT = Path(r"C:/Users/fivep/DeGaJaFinance")
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "scripts"))
import sector_flow as SF

HOLE = pd.Timestamp("2026-08-28")
CACHE = ROOT / "llm_outputs/sector_flow/prices_2026-09-02.pkl"
OUTD = ROOT / "llm_outputs/2026-09-02/industry_US"

def log(*a): print(*a, file=sys.stderr, flush=True)

data = pickle.load(open(CACHE, "rb"))
tickers = sorted(set(data.columns.get_level_values(0)))
close = data.xs("Close", level="Price", axis=1)
official = [t for t in tickers if pd.notna(close.at[HOLE, t])]
missing  = [t for t in tickers if t not in official]
log(f"[repair] tickers={len(tickers)}  official 08-28={len(official)}  missing={len(missing)}")

# ── 5m fetch for every ticker (official ones too, so the proxy can be validated) ──
proxy = {}
bars = {}
B = 40
for i in range(0, len(tickers), B):
    chunk = tickers[i:i+B]
    d5 = yf.download(chunk, start="2026-08-28", end="2026-08-29", interval="5m",
                     auto_adjust=False, group_by="ticker", progress=False, threads=True)
    for t in chunk:
        try:
            df = d5[t].dropna(how="all") if isinstance(d5.columns, pd.MultiIndex) else d5.dropna(how="all")
        except Exception:
            continue
        if df is None or df.empty: continue
        df = df[df.index.date == HOLE.date()]
        if df.empty: continue
        proxy[t] = dict(Open=float(df["Open"].iloc[0]), High=float(df["High"].max()),
                        Low=float(df["Low"].min()), Close=float(df["Close"].iloc[-1]),
                        Volume=float(df["Volume"].sum()))
        bars[t] = len(df)
    log(f"  … 5m {min(i+B,len(tickers))}/{len(tickers)}  got={len(proxy)}")

bl = pd.Series(bars)
log(f"[validate] 5m bars per name: median {bl.median():.0f}  min {bl.min()}  max {bl.max()}  n={len(bl)}")

# ── validate against the 42 official bars ──
vol = data.xs("Volume", level="Price", axis=1)
ce, ve = [], []
for t in official:
    if t not in proxy: continue
    o_c, o_v = float(close.at[HOLE, t]), float(vol.at[HOLE, t])
    ce.append(abs(proxy[t]["Close"] - o_c) / o_c * 100)
    if o_v: ve.append((proxy[t]["Volume"] - o_v) / o_v * 100)
ce, ve = np.array(ce), np.array(ve)
log(f"[validate] n={len(ce)}  close  mean|err| {ce.mean():.4f}%  max {ce.max():.4f}%  >0.05%: {(ce>0.05).sum()}")
log(f"[validate] volume  mean err {ve.mean():.2f}%  median {np.median(ve):.2f}%  min {ve.min():.2f}%  max {ve.max():.2f}%  n={len(ve)}")

# ── measure what the hole does to obv_norm, on the 42 names that have the official bar ──
def obv_norm(c, v):
    obv = (np.sign(c.diff()).fillna(0) * v).cumsum()
    return (obv.iloc[-1] - obv.iloc[-21]) / v.tail(20).sum()
def state(x):
    return "accumulation" if x > 0.05 else ("distribution" if x < -0.05 else "neutral")

rows = []
for t in official:
    if t not in proxy: continue
    c, v = close[t].dropna(), vol[t].dropna()
    c, v = c.align(v, join="inner")
    if len(c) < 25: continue
    true = obv_norm(c, v)
    ch, vh = c.copy(), v.copy(); ch.loc[HOLE] = np.nan; vh.loc[HOLE] = np.nan
    holed = obv_norm(ch.fillna(np.nan), vh.fillna(0))
    cr, vr = c.copy(), v.copy(); cr.loc[HOLE] = proxy[t]["Close"]; vr.loc[HOLE] = proxy[t]["Volume"]
    rep = obv_norm(cr, vr)
    rows.append((t, true, holed, rep))
df = pd.DataFrame(rows, columns=["t", "true", "holed", "rep"]).dropna()
for lab, col in (("unpatched hole", "holed"), ("5m repair", "rep")):
    d = (df[col] - df["true"]).abs()
    flips = sum(state(a) != state(b) for a, b in zip(df[col], df["true"]))
    sflips = sum(np.sign(a) != np.sign(b) for a, b in zip(df[col], df["true"]))
    log(f"[obv-{lab}] n={len(df)} mean|d| {d.mean():.4f}  median {d.median():.4f}  max {d.max():.4f}"
        f"  label-flips {flips}/{len(df)}  sign-flips {sflips}/{len(df)}")
worst = df.assign(e=(df["rep"]-df["true"])).reindex(df.assign(e=(df["rep"]-df["true"]).abs())["e"].sort_values(ascending=False).index).head(5)
log("[obv-repair worst] " + " · ".join(f"{r.t} {r.rep-r.true:+.3f}" for r in worst.itertuples()))
worst2 = df.assign(e=(df["holed"]-df["true"])).reindex(df.assign(e=(df["holed"]-df["true"]).abs())["e"].sort_values(ascending=False).index).head(6)
log("[obv-hole worst] " + " · ".join(f"{r.t} {r.true:+.3f}->{r.holed:+.3f}" for r in worst2.itertuples()))

# ── patch a working copy ──
patched = data.copy()
n = 0
for t in missing:
    if t not in proxy: continue
    for f, v in proxy[t].items():
        try: patched.loc[HOLE, (t, f)] = v
        except Exception: pass
    n += 1
left = [t for t in missing if t not in proxy]
log(f"[repair] patched={n}  no-5m(left NaN)={len(left)} {left}")

# ── rescore with sector_flow's own functions, --no-news, history read-only ──
SF.MKT, SF.UNIVERSE, SF.BENCH, SF.COLS = "us", SF.MARKETS["us"]["universe"], SF.MARKETS["us"]["bench"], SF.MARKETS["us"]
SF.HISTORY = SF.OUT_DIR / "history.json"
rows_u = SF.load_universe(None, None)
bslice = SF.slice_frame(patched, SF.BENCH)
bclose = bslice["Close"].astype(float)
res = []
for i, r in enumerate(rows_u, 1):
    res.append(SF.one_name(r, bclose, patched, False, False))
    if i % 100 == 0: log(f"  … rescore {i}/{len(rows_u)}")
meta = SF.score_all(res, False)
asof = str(bslice.index[-1].date())
hist = SF.load_history()
prev = SF.prev_snapshot(hist, asof, "nonews")
log(f"[hist] prev keys available: {sorted(hist)[-6:]}  prev_n={len(prev)}")
sectors = SF.aggregate_sectors(res, prev)
out = SF.build_json(asof, res, sectors, prev, meta)
(OUTD / "SECTOR_FLOW_US_REPAIRED.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
log("[repair] wrote SECTOR_FLOW_US_REPAIRED.json")
log("scoring: " + json.dumps(meta) + "\nuniverse: " + json.dumps(out["universe"]))
