# PREFLIGHT — 2026-09-12 (Sat) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is a permissions table, not a report** — a FAIL is "what this run may not cite today".
> Execution KST 2026-09-12 **14:52 news probe pre-sweep (0/6, retried +20s: 0/1) · 14:55–15:00 sweep
> (`--json --refresh`, 300 names, completed) · 15:01 bar-completeness scan · 15:02 sweep-history
> `_mode` check · 15:03–15:08 risk units × 3 windows · 15:09 universe/book coverage · 15:09 accrual
> status · 15:10–15:14 tool `--help` × 53 · 15:15 chart live render · 15:15 news probe post-sweep (0/1)
> · 15:16 local `brief` fallback probe (3 dates).**
> **Time-of-run note: Saturday, NYSE closed.** The sweep's `asof` is **Fri 2026-09-11 = a settled
> close**, so no partial intraday bar entered any calculation. Last US desk run was **Tue 09-08**
> (pre-open, asof 09-04) — **five sessions (09-08 … 09-11) are new to this desk today.**
> ⚠ An `industry_kr` run is in flight in the same date folder (`industry_KR/_sweep_start.txt` present);
> this desk touches only `industry_US/` and, at HANDOVER, re-reads `handoff/*.md` before writing.

**Three-line summary**
> (1) **FAIL, and worse than the standing FAIL: the news pipe is entirely dead, not just inside the
>    sweep.** The remote endpoint returns **HTTP 404 (ngrok offline page)** on **every** probe,
>    before and after the sweep, retried once; `vel_coverage` **0.00% (0/299)**, wall at rank **0**
>    (prior runs: 49→50→52→52). The local DB fallback is **0 bytes** (`data/news_alert.db`). The only
>    news instrument alive is the **client-owned title derivative** `data/news_vectors.db`
>    (`brief`/`thread`), which stops at **market_day 2026-09-08** (4,811 foreign titles; 09-09/-10/-11
>    = 0 rows). ⇒ **No news of any kind exists on this desk for the 09-09 → 09-11 sessions.**
> (2) **PASS on price novelty for the first time in five runs.** `asof` **2026-09-11**; the sweep
>    history now holds 09-04 → 09-11 on the **same 3-axis `nonews` scale**, so `delta` is legal and is
>    the **one-week (09-04→09-11, 5 sessions) change**, not a daily one — it must be labelled so.
> (3) **Structural FAILs persist, one moved:** risk units **11 / 11 / 10** (G4; the 250d window now
>    merges the two KR names, which it did not on 09-08 — membership changed, still unstable);
>    universe file **59 days** stale (G5 freshness); accrual **0.60/day = 1.7× slower than ideal** (G6).

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | **PASS** | `prices_2026-09-12.pkl` 301 tickers × 85 sessions. NaN Close **1/301 on all last 14 sessions** (`EA` only, always-NaN; partial-NaN names **0**). `dropped_missing_axis=0`, scored **299**. Last index **2026-09-11** = `SPY` last valid bar → no benchmark/name misalignment |
| **G1** | News-axis liveness | **FAIL — total** (sweep axis AND direct path) | `vel_coverage` **0.0% (0/299)**. Probe **0/6 pre-sweep, 0/1 retry (+20s), 0/1 post-sweep** — all `HTTPError 404` from the ngrok host (offline page, not a tunnel-drop `URLError` as on 09-05…09-08). Local `news_alert.db` **0 bytes**. Local `news_vectors.db` (titles only): 09-08 **4,811** foreign articles / 760 events; **09-09, 09-11: 0** |
| **G2** | Scoring-scale continuity | **PASS (scale) · PASS (novelty)** | `n_axes=3`, `mode=nonews`, `scored=299` — identical to the 09-04 snapshot (`nonews`). `asof` **2026-09-11 ≠ 09-04** ⇒ new information. `delta` = **09-04 → 09-11 (5 sessions)**; no 09-09/09-10 snapshot exists |
| **G3** | Who owns the sector sign | **PASS** (full 11-row list) · guard still blind to Alphabet | Built-in flag: **1 of 11 flips — Consumer Staples / WMT** (28.9%): wflow −0.186 → ex-top1 **+0.023**. Issuer-level rescan: **Comm. Services / Alphabet (2 classes, 76.6%)** −0.148 → ex-issuer **+0.400**, flag prints `False`. 09-08's AMZN flip is gone (−0.240 → −0.037, same sign) |
| **G4** | Risk-unit stability | **FAIL** | 250d **11 units** · 500d **11** · 750d **10** — same count at 250/500 but **different membership**: 250d merges `028050+316140`, separates ANET/ETN; 500d merges `ANET+ETN`, separates the KR pair; 750d adds `AVGO+NVDA`. ARI **0.381 / 0.233 / 0.794**. All windows end 2026-09-11 |
| **G5** | Does the universe cover the book | **FAIL** (freshness leg) | Cover: **11/11** US holdings in `us_top300.csv` and all 11 scored; missing **0**. Freshness **59 days** (mtime 2026-07-15; bar ≤8) |
| **G6** | Instrumentation accrual | **FAIL** | **32 files / 53 days = 0.60/day**; 8 more needed → ideal 8d, measured **~13d = 1.7×** (bar 1.5×). Last save today 09-12 (120 names); gaps median 1, max 6 |
| **G7** | Tool liveness | **PASS with 2 named exceptions** | **51/53** `--help` exit 0. `module_chart --help` exit 1 (no handler) **but live render NVDA populated** (OBV/trigger/stop lines present) → citable. `scripts/margin_history.py` exit 1 (help-string bug; unused here) |

⇒ **8 gates: PASS 4 (G0, G2, G3, G7-with-exceptions) · FAIL 4 (G1, G4, G5, G6).**

---

## Gate detail

### G0 — PASS
Fresh `--refresh` pull, **301 × 85**. Last 14 sessions (08-24 → 09-11) each carry exactly **1** NaN
Close = `EA` (structurally absent every session; partial-NaN names = **none**). `SPY` last bar
2026-09-11 = frame end ⇒ the positional `rs20/rs60` misalignment class cannot fire.
- GRANTED: `obv_norm` / `obv_state` / `flow_score` may be cited from the primary `SECTOR_FLOW_US.json`.
- REVOKED: **`EA` receives no flow/OBV/RS judgment** — unmeasured, not neutral.

### G1 — FAIL, total outage (new failure mode)
**(a)** `sector_flow` dropped the velocity axis and scored all 299 on 3 axes (`mode=nonews`) —
correct behaviour, no inflation.
**(b) Falsification probe — every path dead:**

| probe | result |
|---|---|
| `fts search NVIDIA/Apple/Tesla --scope foreign --days 7 --count` (pre-sweep) | `HTTPError 404` ×3 |
| `fts search NVIDIA/Apple/삼성전자 --days 7 --count` (no scope, pre-sweep) | `HTTPError 404` ×3 |
| retry after 20 s | `HTTPError 404` |
| post-sweep | `HTTPError 404` |
| `curl <endpoint>/exec` · `/` | **404** · ngrok "endpoint offline" HTML page |
| local fallback `data/news_alert.db` | **0 bytes** |
| local `news_vectors.db` `brief --scope foreign` | 09-08: **4,811 articles → 760 events** · 09-09: **0** · 09-11: **0** |

**This is not the idle-timer tunnel drop of 09-05…09-08** (that returned `URLError(FileNotFoundError)`
and recovered after ~5 min of idleness). A **404 from the ngrok host itself** means the tunnel
process on the server PC is not registered — the server-side collector/API is **down or the ngrok
session expired**. Nothing this desk does can recover it (P4/P5: repair is a human item).
**Collector liveness cannot be shown today** — no count can move because no count returns.

**Permissions revoked (all stages):**
- **No news velocity / theme freshness citation** of any kind. No "quiet"/"no news on X" judgment
  anywhere — for **all 299 names and all 11 sectors** the desk measured its own outage, not silence.
- **No `module_news_data fts/search/theme-age/chain-hop/drift` output may be cited** (all remote).
  `drift_watch` (DRIFT stage) will therefore be **unable to measure** — it must record that, not
  "no drift found".
- GRANTED, narrowly: **`brief` / `thread` from the local title derivative for market_day ≤ 2026-09-08**,
  cited as `[news_vectors.db, titles only, asof 09-08]`. Titles, not bodies; 3–4 days stale; **zero
  coverage of the 09-09 → 09-11 sessions**, which are exactly the sessions whose price moves are new
  today. Any narrative attached to those three sessions' tape must be tagged **[inferred]** or
  `[WebSearch]` and cannot be cited as measured.

### G2 — PASS (scale) · PASS (novelty)
`scoring = {vel_axis:false, vel_coverage:0.0, n_axes:3, scored:299, dropped_missing_axis:0}`.
`history.json` keys … `09-03, 09-04, 09-11`, all `_mode=nonews`. Subtraction 09-04→09-11 is legal.
- GRANTED: Δflow may be cited **as the 09-04 → 09-11 one-week change**, labelled with both dates.
- REVOKED: calling it "today's move" / "yesterday's rotation"; no daily attribution exists — the
  09-08, 09-09, 09-10 closes were never snapshotted individually.

### G3 — PASS (list printed), Alphabet blind spot persists
Full flag list (11/11): Energy F · Materials F · IT F · Comm.Svcs F · Health Care F · **Cons.
Staples T** · Cons. Disc. F · Utilities F · Financials F · Real Estate F · Industrials F.
Issuer-level rescan (share classes merged, recomputed today):

| sector | issuer | classes | share | wflow | ex-issuer | flip |
|---|---|--:|--:|--:|--:|:--:|
| **Communication Services** | **Alphabet** | 2 | 76.6% | −0.148 | **+0.400** | **YES** |
| **Consumer Staples** | Walmart | 1 | 28.9% | −0.186 | **+0.023** | **YES** |
| Consumer Discretionary | Amazon | 1 | 40.2% | −0.240 | −0.037 | no |
| Energy | ExxonMobil | 1 | 30.5% | +0.470 | +0.486 | no |
| Materials | Linde | 1 | 24.7% | −0.085 | −0.158 | no |
| Information Technology | Nvidia | 1 | 19.4% | −0.102 | −0.012 | no |
| Health Care | Lilly | 1 | 19.4% | −0.152 | −0.025 | no |
| Utilities | NextEra | 1 | 17.7% | −0.268 | −0.259 | no |
| Real Estate | Welltower | 1 | 16.9% | −0.319 | −0.407 | no |
| Financials | Berkshire | 1 | 13.9% | −0.288 | −0.291 | no |
| Industrials | Caterpillar | 1 | 8.7% | −0.505 | −0.510 | no |

- REVOKED: **Consumer Staples and Communication Services may not be promoted/demoted on `wflow`**;
  use `eqflow` (−0.059 / −0.054) or breadth and say which on the same line.
- GRANTED: the other 9 sectors' signs survive top-issuer removal.

### G4 — FAIL
| window | units | within-corr | ARI | merged pairs | holes >4d |
|---|--:|--:|--:|---|--:|
| 250d (2025-08-25→2026-09-11, n=249) | **11** | 0.6005 | 0.381 | `028050+316140` · `MPC+PSX` | 2 |
| 500d | **11** | 0.6148 | 0.233 | `ANET+ETN` · `MPC+PSX` | 5 |
| 750d | **10** | 0.5187 | 0.794 | `ANET+ETN` · `AVGO+NVDA` · `MPC+PSX` | 8 |

Change vs 09-08: 250d went 12 → 11 because the **two KR names now cluster** (residual corr 0.35);
that pair does not cluster at 500/750. `ANET+ETN` still spans two book theme labels
(`AI-compute-EPICENTER` + `AI-power/electrical`) at 500/750d. Threshold sweep: 250d 12/12/12/12/**11**/10/7.
- REVOKED: no concentration guard as a single number; any claim carries `--days` on the same line
  and notes **11 / 11 / 10**.
- REVOKED: treating `AI-compute-EPICENTER` and `AI-power/electrical` as independent without noting
  the 500/750d merge.

### G5 — FAIL (freshness leg only)
Coverage PASS: ANET, AVGO, ETN, HPE, MET, MPC, NDAQ, NUE, NVDA, PSX, RTX all in `us_top300.csv`
(300 rows) and all scored. Freshness FAIL: **59 days** (2026-07-15).
- GRANTED: per-name flow/RS/OBV/short on the 11 holdings.
- REVOKED: cap weights / sector cap shares / `top1_w` / issuer shares as *current*; where weighted
  and equal-weighted disagree, **equal-weighted is the citable one**.

### G6 — FAIL
`snapshot_estimates --status`: 32 files / 53 calendar days = **0.60/day**; 8 more to the 40-day
target → **~13 days measured vs 8 ideal = 1.7×** (bar 1.5×). Daemon alive (saved today), rate fails.
- REVOKED: `kelly_size --ic` as an evidence-backed size — must be labelled **"mechanical 1/4"**.

### G7 — PASS with 2 exceptions
51/53 exit 0 (20 `-m module_*` + 32 `scripts/*.py` + universe builder). `module_chart --help` exit 1
but `python -m module_chart NVDA` rendered a full block (OBV 20d slope −60% distribution, trigger,
swing-low stop) → **citable**. `margin_history.py --help` exit 1 → not citable, not needed.
`module_macro_us --help` exit 0 (FRED path available; liveness of the FRED fetch itself is
established at MACRO, not here).

---

## Consolidated permissions table for 2026-09-12

| # | Revoked | Gate |
|---|---|---|
| 1 | **Any news-velocity / theme-freshness / "quiet" claim**, any `fts`/`search`/`theme-age`/`chain-hop`/`drift` citation — the remote news pipe is 404-dead, local fallback is empty | **G1** |
| 2 | Any measured narrative for the **09-09, 09-10, 09-11 sessions** — the only live title source ends at 09-08. Tag `[inferred]`/`[WebSearch]` | **G1** |
| 3 | Calling Δflow "today's" — it is the **09-04 → 09-11** one-week change | G2 |
| 4 | Promote/demote **Consumer Staples** or **Communication Services** on `wflow` — use `eqflow`/breadth, say which | G3 |
| 5 | Concentration guard as one number — carry `--days`, note **11/11/10** | G4 |
| 6 | `AI-compute-EPICENTER` and `AI-power/electrical` as independent themes without the 500/750d merge note | G4 |
| 7 | Cap weights / `top1_w` / issuer shares as current — **59-day-old** cap vector | G5 |
| 8 | `kelly_size --ic` as evidence-backed — "mechanical 1/4" | G6 |
| 9 | `scripts/margin_history.py` output | G7 |
| 10 | `EA` any flow/OBV/RS verdict | G0 |
| 11 | Differencing against any snapshot ≤ 2026-09-02 without clean-baseline recomputation | G2 |

**Granted:** primary-file OBV/flow/RS (G0) · Δflow 09-04→09-11 on the continuous 3-axis scale (G2) ·
9/11 sector `wflow` signs (G3) · per-name measurement on all 11 holdings (G5) · `module_chart` (G7) ·
local `brief`/`thread` titles for market_day ≤ 09-08 (G1, narrow) · FRED via `module_macro_us`
(subject to MACRO's own fetch check) · FINRA/CFTC via `us_flow` (subject to fetch).

**Standing implication:** for the first time in five runs the **price tape is new** (five sessions),
but the **news instrument is gone entirely** — the desk can see *what* moved 09-08→09-11 and cannot
measure *why* from its own feeds. Every "why" this run attaches to those sessions is inference or
web-sourced and must be tagged as such; the honest output today is a **tape-first, narrative-light** run.

> P4 compliance: no market call, no name-level verdict, no sizing. Tickers appear only as instrument
> identifiers. Nothing here is written to `handoff/`.

---

## ADDENDUM — 22:10 KST re-run (same date, second scheduled invocation)

The 14:52–15:16 run stopped after HANDOVER (last write 15:16; no MACRO_REPORT/ROTATION/DEEP/BET
files exist). This invocation **continues from the on-disk outputs** (PREFLIGHT · HANDOVER ·
`SECTOR_FLOW_US.json` asof 09-11 · `_fred.json` · `_usflow.json` · `_risk_*.json`) rather than
re-running them: Saturday, NYSE closed ⇒ no new bar since the 15:00 sweep, and same-date files are
append-only per repo practice (no clobber).

**G1 re-probe at 22:10 (+7h):** `fts search NVIDIA / Apple --scope foreign --count` → `HTTPError 404`
×2; retry after 20 s (`Tesla`) → `HTTPError 404`. Local `news_alert.db` still **0 bytes**;
`news_vectors.db` last touched 15:00 (no new sync — the sync source is the same dead endpoint).
⇒ **G1 verdict unchanged: FAIL — total outage, 7 hours and counting.** Every revocation in the
consolidated table above stands for the remainder of this run. All other gates: no re-measurement
needed (no new bars, no universe/accrual change possible on a Saturday evening).
