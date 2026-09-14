# PREFLIGHT — 2026-09-14 (Mon) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is a permissions table, not a report** — a FAIL is "what this run may not cite today".
> Execution KST 2026-09-14 **13:16 news probe pre-sweep (3/3 alive — first live response since 09-05)
> · 13:16–13:19 sweep #1 (`--json --refresh`, 301 names, news axis ON) · 13:19 post-sweep probe
> (0/3, `URLError` tunnel-drop) · 13:19–13:24 sweep #2 (`--json --no-news`, same price cache → the
> load-bearing `SECTOR_FLOW_US.json`) · 13:2x risk units × 3 windows · accrual status · universe/book
> cover · 35 tool `--help` + chart live render · 13:20–13:24 remote re-probe 8× at 30 s (all dead)
> · 13:25 local-fallback base-window probe · 13:25 catalyst calendar.**
> **Time-of-run note: Monday 13:16 KST = Monday 00:16 ET — NYSE not yet open.** The sweep `asof` is
> **Fri 2026-09-11 = a settled close**, the *same close the 09-12 run measured*. No new US bar
> exists since the last US desk run → **today's price tape is a reprint of 09-12's** (verified:
> `flow_score` diff **0/299**, `tag` diff **0/299**, `delta` identical). What is new today is the
> news instrument's state (below) and whatever the desk does *outside* the sweep.
> ⚠ An `industry_kr` run is in flight in the same date folder (`industry_KR/_sweep_start.txt` 13:24,
> KR sweep ran 13:18–13:24 — **concurrently with sweep #1**). This desk touches only `industry_US/`
> and re-reads `handoff/*.md` before writing at HANDOVER.

**Three-line summary**
> (1) 🚨 **G1 FAIL — a new, worse failure mode: the news axis came back *half-alive* and silently
>    contaminated the tags.** The remote API answered pre-sweep (NVIDIA 1,453 / Apple 505 / Tesla 340
>    in 7d) and **died mid-sweep** (`URLError`, the tunnel-drop signature — two sweeps, US + KR, hit it
>    in parallel; cf. the self-DoS memory). `sector_flow` then fell back to the **local DB restored
>    09-13 14:27** — a one-shot 4,613-article pull whose entire pool sits inside the last 7 days, so
>    `velocity ≡ 30/7 = 4.29` for **139 names** (r == b, "acceleration" = "exists"). Coverage
>    **62.9% (188/299)** < 80% ⇒ `flow_score` correctly dropped the axis (3-axis, no inflation), **but
>    `flow_tag` still consumed `vel ≥ 1.2` as conviction: 33 names 🟡→🟢, 12 🟡→🔴, 11 🔴→🟡;
>    `new_green` 4 → 36.** That file is quarantined as `_SECTOR_FLOW_US.mixed_news_1317.json`; the
>    load-bearing `SECTOR_FLOW_US.json` is the `--no-news` re-run (tags/scores = 09-12's, byte-equal).
> (2) **G2 PASS on scale, ⚠ zero novelty:** `asof` 09-11 = 09-12's snapshot; `history.json` last key
>    09-11 (no new key written — same asof overwrites). `delta` is still the **09-04 → 09-11 (5
>    sessions)** change, exactly as on 09-12. Nothing in the sweep can be called "new since Saturday".
> (3) **Structural FAILs unchanged:** risk units **11 / 11 / 10** (G4, identical membership to 09-12);
>    universe file **61 days** stale (G5); accrual **0.61/day = 1.6× slower than ideal** (G6).
>    **Catalyst injection: FOMC 2026-09-16 14:00 ET (≈62 h out, D-2 by date) + S&P quarterly
>    rebalance/quad witching 09-18 (D-4) + undated Hormuz binary** → PREMORTEM must bracket FOMC
>    both ways (the calendar tool itself prints "both-sides bracket REQUIRED").

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | **PASS** | `prices_2026-09-14.pkl` 301 tickers × 85 sessions (2026-05-12 → 09-11). NaN Close on last row **1/301** (`EA` only, structurally absent; partial-NaN names **0**; always-NaN **0** after the 2-level frame is read correctly). `dropped_missing_axis=0`, scored **299**. `SPY` last valid bar **2026-09-11** = frame end |
| **G1** | News-axis liveness | **FAIL — mixed-source contamination** (worse than dead) | Pre-sweep probe **3/3 alive** (13:16). Sweep #1 `vel_coverage` **62.9% (188/299)**; of the 188, **139 = 4.29 exactly** (local-fallback artifact, 7d count == 30d count), **~49 = real remote ratios** (0.32–0.62). Post-sweep probe **0/3**, 8 retries over 4 min **0/8** (`URLError`). Local `news_alert.db` **16.9 MB / 4,613 rows, all `fetched_at` 2026-09-13T14:27** (one pull), published 09-08…09-13 |
| **G2** | Scoring-scale continuity | **PASS (scale) · ⚠ no novelty** | Load-bearing file: `n_axes=3`, `mode=nonews`, `scored=299` — identical to 09-11/09-04 snapshots. `asof` **2026-09-11 = 09-12 run's asof** ⇒ **reprint**. `delta` = **09-04 → 09-11 (5 sessions)** — same window as 09-12 |
| **G3** | Who owns the sector sign | **PASS** (full 11-row list) · Alphabet blind spot persists | Built-in flag: **1 of 11 flips — Consumer Staples / WMT** (28.9%): wflow −0.186 → ex-top1 **+0.023**. Issuer-level rescan: **Comm. Services / Alphabet (2 classes, 76.6%)** −0.148 → ex-issuer **+0.400**, flag prints `False`. Unchanged from 09-12 (same close) |
| **G4** | Risk-unit stability | **FAIL** | 250d **11 units** · 500d **11** · 750d **10** — **different membership**: 250d merges `028050+316140`; 500d merges `ANET+ETN`; 750d merges `ANET+ETN` + `AVGO+NVDA`; `MPC+PSX` merged in all three. ARI **0.381 / 0.233 / 0.794**. All windows end 2026-09-11. Identical to 09-12 |
| **G5** | Does the universe cover the book | **FAIL** (freshness leg) | Cover: **11/11** US holdings (ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX) in `us_top300.csv` (300 rows), all scored; missing **0**. Freshness **61 days** (mtime 2026-07-15; bar ≤8) |
| **G6** | Instrumentation accrual | **FAIL** | **33 files / 54 days = 0.61/day**; 7 more needed → ideal 7d, measured **~11d = 1.6×** (bar 1.5×). Last save 09-13 (120 names); gaps [2,1,1,1,1,1,1,1], max 6 |
| **G7** | Tool liveness | **PASS with 1 named exception** | **34/35** `--help` exit 0 (15 `-m module_*` + 20 `scripts/*.py`). `module_chart --help` exit 1 (no handler) **but live render `NVDA` populated** (candles/RSI/OBV20d blocks written to `module_chart/output/NVDA_chart.txt`) → citable |

⇒ **8 gates: PASS 4 (G0, G2-scale, G3, G7-with-exception) · FAIL 4 (G1, G4, G5, G6).**

---

## Gate detail

### G0 — PASS
Fresh `--refresh` pull at 13:16, **301 × 85**, 2-level `(ticker, field)` frame. Last row NaN Close =
`EA` only. `SPY` last bar 2026-09-11 = frame end ⇒ the positional `rs20/rs60` misalignment class
cannot fire. Sweep #2 (`--no-news`) reused this cache (no second download) — same frame.
- GRANTED: `obv_norm` / `obv_state` / `flow_score` / `rs20` / `rs60` from `SECTOR_FLOW_US.json`.
- REVOKED: **`EA` receives no flow/OBV/RS judgment** — unmeasured, not neutral.

### G1 — FAIL: mixed-source velocity, tag contamination (new failure class, D48-logged in-run)

**(a) Timeline, measured**

| KST | probe / event | result |
|---|---|---|
| 13:16:22 | `fts search NVIDIA / Apple / Tesla --scope foreign --days 7 --count` | **1,453 / 505 / 340** — remote alive (first since 09-05) |
| 13:16:3x | `fts search Samsung Electronics (KR probe term) --days 7 --count` (KR scope) | **775** alive |
| 13:16–13:19 | sweep #1, news axis ON; KR desk's sweep starts 13:18 on the same endpoint | velocity measured **188/299** |
| 13:19:5x | post-sweep `fts search NVIDIA / Boeing / Archer-Daniels` | `URLError(FileNotFoundError)` ×3 — **tunnel drop** (not the 09-12 `HTTPError 404`) |
| 13:20:44 → 13:24:27 | 8 retries at 30 s | **0/8** |
| 13:25 | local fallback (`DEGAJA_NEWS_API=` unset) `NVIDIA / Boeing / Exxon / Walmart / Valero` **7d vs 30d** | **254/254 · 37/37 · 14/14 · 21/21 · 4/4** — every 30-day count equals its 7-day count |

**(b) What the artifact is.** `news_velocity = (r/7)/(b/30)`. When the pool holds only the last
week, `r == b` and `velocity ≡ 30/7 = 4.2857 → 4.29` regardless of the name. The local DB
(`data/news_alert.db`, 16.9 MB) is a **single pull at 2026-09-13T14:27** (4,613 rows; `published_at`
09-08…09-13, plus 482 unparseable). It is a *presence* detector, not an *acceleration* meter.
Distribution in sweep #1: `4.29 × 139`, then a real-looking tail (0.62, 0.54, 0.52, 0.51, 0.45,
0.37, 0.32 …) for ~49 names measured **before** the tunnel dropped — so the axis was **two
instruments in one column** (remote ratio → local presence) with no per-row source tag.

**(c) What it did downstream — measured, not inferred.** `flow_score` dropped the axis (62.9% <
80%; `n_axes=3`; no +0.305 inflation — the D225 guard worked). **`flow_tag` did not**: it reads
`vel ≥ 1.2` as a green vote *and* as `has_conviction`. Sweep #1 vs the clean 3-axis set:

| transition | n | examples |
|---|--:|---|
| 🟡 → 🟢 | **33** | VLO DVN PSX MPC MSTR CRM COP LITE KR COIN COR NEM T HUM VZ FANG CMG VST … |
| 🟡 → 🔴 | 12 | (remote-measured `vel < 0.7` names) |
| 🔴 → 🟡 | 11 | |
| `new_green` | **4 → 36** | clean: QCOM META HPE AIG |

**This is the sentence the stage exists for:** the instrument returned numbers, the numbers were
plausible, and a tag column 299 rows long moved on a value that means "has an article since
Tuesday". The 09-12 desk could not measure news; today's desk **measured its own fallback DB**.

**(d) Disposition (no code fixed — P4/P5; recorded, permissions cut):**
- Sweep #1 file quarantined → `_SECTOR_FLOW_US.mixed_news_1317.json` (+ `_sweep_mixed_1317.log`).
  It is evidence of the defect, not an input to any stage.
- `SECTOR_FLOW_US.json` = sweep #2 `--no-news` (13:19–13:24, same price cache): `vel_coverage 0.0`,
  `n_axes=3`, tags **0/299 diff vs 09-12**, `new_green` = QCOM META HPE AIG. This is the same
  instrument mode every run since 08-09 has used; it is *not* a repair, it is the measurable mode.
- ⚠ Defect to carry as a dig item (human/idle_probe): **`flow_tag` consumes velocity even when
  `score_all` has excluded the axis** — the two guards disagree. Also: **velocity has no
  source-provenance field**, so a mid-sweep fallback is invisible in the output.

**Permissions revoked (all stages):**
- **No news velocity / theme-freshness / "quiet" claim of any kind.** The remote pipe is dead again
  after ~3 minutes of life; the local pool is a 6-day presence set with no base window.
- **No `tag` / `new_green` / 🟢-count citation from sweep #1.** Only the `--no-news` file's tags exist.
- **No `fts/search/theme-age/chain-hop/drift` citation** — remote dead post-13:19; **local fallback
  counts may be cited only as "n articles 09-08…09-13 in the 09-13 local pull"**, never as a rate
  or a change. `drift_watch` (DRIFT) will be unable to measure a kill-switch burst — record that.
- GRANTED, narrowly: (i) the **pre-sweep 7-day counts** NVIDIA 1,453 · Apple 505 · Tesla 340 (remote,
  13:16) as `[measured, remote, 7d, asof 13:16]` — counts, not velocity; (ii) `brief`/`thread` from
  `news_vectors.db` (titles) — cursor still **2026-09-09T08:44** per the 09-13 KR preflight; the
  local pull did **not** advance it (sync source = the same dead endpoint), so market_day ≤ 09-08 full
  + 09-09 partial only; (iii) the local pool's **titles** for 09-08…09-13 as `[local pull 09-13,
  titles+summary, no bodies]` — these are the only same-week headlines the desk has.

### G2 — PASS (scale) · ⚠ no novelty
`scoring = {vel_axis:false, vel_coverage:0.0, n_axes:3, scored:299, dropped_missing_axis:0}`.
`history.json` keys … `09-02, 09-03, 09-04, 09-11`, all `_mode=nonews`; today's run wrote no new key
(same asof). Δ 09-04→09-11 is legal and is **the identical number 09-12 already carried**.
- GRANTED: Δflow as the **09-04 → 09-11 one-week change**, labelled with both dates.
- REVOKED: any "since Saturday / since the last run" attribution to the sweep — there is none.
  Any novelty today must come from **outside the sweep** (macro releases, FINRA/CFTC prints if
  updated, scenario settlements, ledger `due` rows, the FOMC bracket).

### G3 — PASS (list printed), Alphabet blind spot persists
Full flag list (11/11): Energy F · Materials F · IT F · Comm.Svcs F · Health Care F · **Cons.
Staples T** · Cons. Disc. F · Utilities F · Financials F · Real Estate F · Industrials F.
Issuer-level rescan (share classes merged, recomputed today on the same close):

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
| 500d (2024-07-29→) | **11** | 0.6148 | 0.233 | `ANET+ETN` · `MPC+PSX` | 5 |
| 750d (2023-07-10→) | **10** | 0.5187 | 0.794 | `ANET+ETN` · `AVGO+NVDA` · `MPC+PSX` | 8 |

Threshold sweep at 250d: 12/12/12/12/**11**/10/7/7/5 (thr 0.40→0.85). Identical to 09-12 (same
window end). `ANET+ETN` spans two book theme labels (`AI-compute-EPICENTER` + `AI-power/electrical`).
- REVOKED: no concentration guard as a single number; any claim carries `--days` on the same line
  and notes **11 / 11 / 10**.
- REVOKED: treating `AI-compute-EPICENTER` and `AI-power/electrical` as independent without noting
  the 500/750d merge.

### G5 — FAIL (freshness leg only)
Coverage PASS: 11/11 US holdings in `us_top300.csv` and all 11 scored (KR names `028050`, `316140`
are the KR desk's). Freshness FAIL: **61 days** (2026-07-15). `sector_flow` itself warns
"61 days elapsed — market caps stale".
- GRANTED: per-name flow/RS/OBV/short on the 11 holdings.
- REVOKED: cap weights / sector cap shares / `top1_w` / issuer shares as *current*; where weighted
  and equal-weighted disagree, **equal-weighted is the citable one**.

### G6 — FAIL
`snapshot_estimates --status`: 33 files / 54 calendar days = **0.61/day**; 7 more to the 40-day
target → **~11 days measured vs 7 ideal = 1.6×** (bar 1.5×). Daemon alive (09-13 saved; 9-day
streak), cumulative rate fails.
- REVOKED: `kelly_size --ic` as an evidence-backed size — must be labelled **"mechanical 1/4"**.

### G7 — PASS with 1 exception
34/35 exit 0. `module_chart --help` exit 1 but `python -m module_chart NVDA` rendered the full
block (candles + MA/BB, RSI, OBV20d) → **citable**. `module_macro_us --help` exit 0 (FRED path
available; the fetch itself is checked at MACRO). `scripts/margin_history.py` not in this run's
entry-point set (not probed, not citable).

---

## Consolidated permissions table for 2026-09-14

| # | Revoked | Gate |
|---|---|---|
| 1 | **Any news-velocity / theme-freshness / "quiet" claim**; any `fts`/`search`/`theme-age`/`chain-hop`/`drift` citation as a rate or change — remote dead post-13:19, local pool = 6-day presence set | **G1** |
| 2 | **Any `tag` / `new_green` / 🟢-count from sweep #1** (`_SECTOR_FLOW_US.mixed_news_1317.json`) — 33 spurious promotions | **G1** |
| 3 | Any measured narrative for the **09-09 → 09-11 sessions** beyond local-pull *titles*; tag `[local pull 09-13, titles]` / `[inferred]` / `[WebSearch]` | **G1** |
| 4 | Calling Δflow "new since the last run" — `asof` 09-11 is a **reprint of 09-12**; Δ = **09-04 → 09-11** | G2 |
| 5 | Promote/demote **Consumer Staples** or **Communication Services** on `wflow` — use `eqflow`/breadth, say which | G3 |
| 6 | Concentration guard as one number — carry `--days`, note **11/11/10** | G4 |
| 7 | `AI-compute-EPICENTER` and `AI-power/electrical` as independent themes without the 500/750d merge note | G4 |
| 8 | Cap weights / `top1_w` / issuer shares as current — **61-day-old** cap vector | G5 |
| 9 | `kelly_size --ic` as evidence-backed — "mechanical 1/4" | G6 |
| 10 | `EA` any flow/OBV/RS verdict | G0 |
| 11 | Differencing against any snapshot ≤ 2026-09-02 without clean-baseline recomputation | G2 |

**Granted:** primary-file OBV/flow/RS on the `--no-news` file (G0) · Δflow 09-04→09-11 on the
continuous 3-axis scale (G2) · 9/11 sector `wflow` signs (G3) · per-name measurement on all 11
holdings (G5) · `module_chart` (G7) · pre-sweep remote 7-day **counts** (NVIDIA 1,453 · Apple 505 ·
Tesla 340, 13:16) as counts only · local-pull titles 09-08…09-13 as titles only · `brief`/`thread`
titles for market_day ≤ 09-08 (+09-09 partial) · FRED via `module_macro_us` (subject to MACRO's own
fetch check) · FINRA/CFTC via `us_flow` (subject to fetch).

**Catalyst injection (run-start):** `CATALYST_WATCH.json` (13:25) — **FOMC 2026-09-16 14:00 ET**
(SEP/dot plot; ≈62 h from run start, so *not* inside the 48 h rule by clock, but D-2 by calendar and
the tool prints "both-sides bracket REQUIRED") · **S&P quarterly rebalance / quad witching 09-18**
(D-4, volume multiple) · **undated Hormuz "strait open" binary** (watch). PREMORTEM must produce the
FOMC bracket; a one-way tilt into it is a protocol violation.

**Standing implication:** the price tape is **not new** (reprint of 09-12's Friday close), and the
news instrument went from *dead* to *lying* for three minutes and back to *dead*. The honest output
today is a **settlement-and-bracket run**: score what came due, carry the 09-12 tape read forward
without re-deriving it, bracket FOMC, and treat every "why" as inference or web-sourced.

> P4 compliance: no market call, no name-level verdict, no sizing. Tickers appear only as instrument
> identifiers. Nothing here is written to `handoff/`.
