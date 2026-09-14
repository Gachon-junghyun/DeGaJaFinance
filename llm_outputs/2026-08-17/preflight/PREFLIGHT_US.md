# PREFLIGHT — 2026-08-17 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-17 22:10–22:15 = ET 2026-08-17 09:10–09:15, MONDAY — US cash PRE-MARKET.**
> Sweep download 22:11 · scoring complete 22:13 · sweep `asof` **2026-08-14** (Friday close).
> ★ **The regular session opens at 09:30 ET = 22:30 KST — twenty minutes AFTER this sweep finished,
> and therefore DURING the later stages of this run.**
>
> ★ **Two headlines, and the second one revokes a right this desk granted itself yesterday.**
> ① **The clean clock is luck, not construction.** The previous four US runs were weekend runs, where an
> incomplete last bar is impossible *in principle*. Today is a session day and the sweep merely finished
> before the bell. The bar is settled; the *reason* it is settled is a 20-minute margin.
> ② **`breadth` is not a news-axis-independent statistic.** Measured today: with **all 299 flow_scores
> byte-identical to yesterday's**, two names changed tag (`NFLX` 🟢→🟡, `MA` 🟡→🟢) purely because their
> *news velocity* moved, and two sector `breadth` values moved with them. Yesterday's table told the
> desk that breadth "carries more load, not less" when the news axis is down. **That is now measured to
> be wrong** — `tag` is computed as `flow_tag(price, velocity)` and never passes through the axis-drop
> guard that protects `flow_score`.
>
> ⚠ **Filename deviation, logged (8th consecutive run, same reason):** the composition table names this
> `preflight/PREFLIGHT.md`, but the `industry_kr` desk already wrote its rights table to that path this
> morning (09:33 KST). Overwriting a sibling desk's output is not a correction, so the US table is
> written as `PREFLIGHT_US.md` in the same folder — documented practice on 08-10 · 08-12 · 08-13 ·
> 08-14 · 08-15 · 08-16. Human decision on permanent market-suffixing still pending (PROMPT_MAP §6).

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** *(5th consecutive)* — **but for a different reason than the last four** | Last bar **2026-08-14**, **zero 08-17 bars in the frame**. SPY **85/85** valid bars, carries 08-14 (**776.34**) → matched RS endpoints. ★ First session-day US run in five: the margin was **20 minutes to the bell**, not the weekend |
| **G1** news axis alive | 🔴 **FAIL** *(5th run — and the "monotone nesting" shape from yesterday is falsified)* | Sweep coverage **17.06% (51/299)**. Re-probe of 40 names the sweep called silent: **40/40 valid · 0 pipe-fail · ZERO genuinely quiet, in 18.5 s.** Cumulative **0 of 120** false-silence across three runs. ★ `RTX` **re-entered** the survivor set (yesterday's dropout) ⇒ the set is not monotone. ★★ **`breadth` measured to be news-contaminated** |
| **G2** scoring-scale continuity | 🟢 **PASS** *(literally)* | **3-axis (`nonews`) vs 3-axis (`nonews`)** ⇒ no apples-to-oranges subtraction. ★ **All 299 `flow_score` values are identical to yesterday's** — `asof` is the same **2026-08-14**, baseline again **08-13**. Today's Δ is the **4th replay** of one interval |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **3 of 11** (IT/`NVDA` 19.4% · Industrials/`CAT` 8.7% · Materials/`LIN` 24.7%). Same set, same numbers as 08-15 and 08-16 — same input file, **not** a confirmed structure |
| **G4** risk-unit stability | 🔴 **FAIL** *(8th consecutive run, identical numbers)* | 250d **11 units** · 500d **10** · 750d **10** — 500 and 750 agree, **250 does not** |
| **G5** does the universe cover the book | 🔴 **FAIL** *(on staleness only)* | **11/11 US holdings inside `us_top300` AND scored ✅**. But `us_top300.csv` is **33 days old** (limit ≤8) and **`EA` returns a null last bar for the 5th consecutive run** |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** | Measured ETA **≈72 days** vs ideal 30 = **2.4×** (limit 1.5×). 10 files / 24 calendar days; last save **08-14**, **3 days ago** |
| **G7** tool liveness | 🔴 **FAIL** | **46 entry points** probed, **2** non-zero `--help` (`scripts/margin_history.py` · `module_chart`) — **8th consecutive run unrepaired**. Both pass a functional probe ⇒ citation rights retained **for those command lines only** |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate).
Headline count identical to 08-15 and 08-16 for the third run running — **and the desk is by now on record
that an identical headline is not an identical state.** Today two things changed underneath it: the
falsification probe hit **100%** (its best reading in five runs), and one instrument the desk had been
treating as safe (`breadth`) turned out to be carrying the broken axis.

Today this desk **cannot** speak with the sweep's news-velocity axis, the 51 survivors, theme freshness,
"it went quiet", **`breadth` as a news-independent reading**, a single concentration number, an
`--ic`-derived size, or **any Δ described as "today's change"**. It **can** speak with settled prices
through the **08-14** close, fine-grain RS, OBV, `eqflow`, `vol_surge` both ways, FINRA short pressure,
CFTC COT positioning, FRED series, primary filings, `news_vectors.db` through 08-16, and hand-probed
per-name news velocity — the last of which measured **40/40** today.

---

## G0 · Bar completeness · date alignment — 🟢 PASS *(bonus gate — and today the PASS has a different warrant)*

Not one of the seven. Carried because the KR desk measured it into existence on 08-12 and it has failed
repeatedly there — intraday stubs and benchmark bar gaps that silently re-date a whole run.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-17.pkl`
(85 rows × 1806 columns = 301 tickers × 6 fields, MultiIndex `Ticker`×`Price`) + `SECTOR_FLOW_US.json §asof`.

| Item | Value | vs 08-16 run |
|---|---|---|
| Run clock | **09:10–09:15 ET Mon 08-17 — PRE-MARKET, bell at 09:30 ET** | 07:05 ET Sunday, closed |
| Last index in the price frame | **2026-08-14** (Friday) | same |
| **Rows dated 2026-08-17** | **ZERO** | (n/a — weekend) |
| Last-bar volume / prior-20d average — median | **0.649** (q25 **0.543** · q75 **0.822**, n=300) | **identical** |
| Benchmark `SPY` last three bars | 08-12 **772.49** · 08-13 **777.88** · **08-14 776.34** | **identical** |
| `SPY` valid bars vs frame rows | **85 / 85** — no benchmark gap | same |
| `SPY` own last-bar volume / 20d | **0.646** | identical |
| `SECTOR_FLOW_US.json §asof` | **2026-08-14** — matches the data's own last index | same |
| Non-null closes on the last row | **300 / 301** (one hole → G5) | same |
| Per-name last close date | **08-14 = 300 names**, 08-10 = 1 (`EA`) | same |

⇒ Benchmark and names share the same terminal date, so `rs20 = ret(name,20) − ret(bench,20)` has
**matched endpoints**. The gate passes on its own condition.

★ **But read the warrant, not just the verdict.** The last four US runs passed this gate because they ran
on **non-session days**, where a stub bar is impossible in principle — the strongest form the gate can
pass in. Today's run is the **first session-day US run in five**, and it passed because yfinance had not
yet minted an 08-17 bar at 09:10 ET, twenty minutes before the bell. **[measured]**
⚠ Therefore: **this PASS does not license "session-day runs are safe."** The KR desk reached exactly this
conclusion at 09:22 KST this morning about its own clean clock, independently, on the same calendar day.
⚠ **Binding on later stages of THIS run:** the bell rings at **22:30 KST**, i.e. *during* this run. Any
stage that re-pulls prices after that point will be pulling a **live partial bar**. No stage may re-run
`sector_flow` or `yf_snapshot` for fresh prices and treat the result as comparable to this sweep.

⚠ **The 0.649 is a real light-volume reading, not a clock artifact** — 08-14 was a full Friday in which
SPY fell 777.88 → 776.34 (**−0.20%**) on about two-thirds of the trailing 20-day volume norm, itself
below 08-13's 0.732. **But it is not a new observation.** It is the same Friday bar the 08-15 and 08-16
runs already read. **[measured 08-14, re-read on 08-15, 08-16 and 08-17 — one observation, four readings.]**
Not an opex artifact either: August monthly expiry is 08-21 (this Friday).

**✅ Rights available for this run:**
1. **RS20/RS60 may be compared at fine grain** — no contamination band.
2. **`vol_surge` may be read in both directions** — the last bar is complete, so a low reading is a low reading.
3. `asof 2026-08-14` may be written plainly as "data through the 08-14 close".
4. 🚫 **But**: any sentence of the form "volume thinned *today*" is forbidden. The correct form is
   "through the 08-14 close, and unchanged since this desk last looked."
5. 🚫 **And**: no stage may describe anything in this run as reflecting **Monday 08-17 trading**. This run
   contains **zero** cells of 08-17 price data, and it was assembled before the market opened.

---

## G1 · News axis alive — 🔴 FAIL *(5th consecutive run — best probe reading yet, and one new contamination found)*

**Commands**
- `SECTOR_FLOW_US.json §scoring` → `{"vel_axis": false, "vel_coverage": 0.1706, "n_axes": 3, "scored": 299, "dropped_missing_axis": 0}`
- Sweep's own health line: `[axis] velocity 측정 51/299 = 17.1% → 속도축 제외(전원 3축) · 기준 80%` + the 🚨 line
- Falsification probe A (CLI path), actually run at **22:13:55–22:14:02 KST**:
  `python -X utf8 -m module_news_data fts search <name> --days 7 --count --scope foreign`
- Falsification probe B (library path, **the exact call the sweep makes**), actually run at
  **22:14:12–22:14:30 KST**: `flow_read.news_velocity(flow_read._news_query(tk, name), 7, 30, kr=False)`
  on a seeded (`seed=817`) n=40 draw from the **248** names the sweep recorded as `velocity: None`

### (a) Probe A — CLI path alive, 5/5, at 22:13:55 KST

| Probe | 7-day count | 08-16 run |
|---|---|---|
| Nvidia | ✅ **3,624** · `(via NEWS API @ …ngrok-free.dev)` | 3,639 |
| Broadcom | ✅ **396** | 359 |
| Eaton | ✅ **47** | 49 |
| Nucor | ✅ **19** | 17 |
| Raytheon | ✅ **14** | 9 |

All five answered in **7 seconds total**. Counts moved on all five — this is a live query, not a cache.

### (b) ★ Probe B — 40/40. Zero pipe failures. Zero genuine silence.

| Re-probe (n=40 seeded draw from the 248 "silent" names, 80 requests, **18.5 s**) | Count | Share | 08-16 | 08-15 |
|---|---|---|---|---|
| **Valid velocity returned** — the sweep simply failed to count it | **40** | **100.0%** | 60.0% | 85.0% |
| **Pipe failure** | **0** | **0.0%** | 40.0% | 15.0% |
| **Genuinely zero articles in the window** | **0** | **0.0%** | **0.0%** | **0.0%** |

Worked examples, all from the sweep's *dead* list, all `"source": "api"`, all fetched 22:14:12–22:14:30:
`C` 7d **201** / 30d 1,052 → **0.82** · `CEG` 47/136 → **1.48** · `ADBE` 147/623 → **1.01** ·
`VLO` 27/123 → **0.94** · `ROST` → 1.29 · `SCHW` → 0.93 · `ALNY` → 0.95 · `IBKR` → 0.92 ·
`SYK` → 0.80 · `CMCSA` → 0.73 · `SRE` → 0.71 · `KDP` → 0.40 · `ECL` → 0.27 · `MRSH` → 0.16.

⇒ **Cumulative over three runs: 0 of 120 "silent" names were actually quiet.** The sweep's ~83% silence
is **100% instrument, 0% world** — measured three times, on three different draws, at three different
success rates (85% → 60% → 100%). The success *rate* is unstable; the *false-silence rate* is stably zero.

★ **The rate series now says something the single readings did not.** Standalone probing returned
**100%** today while the same library call inside the full sweep returned **17%** twenty minutes earlier.
That is not "the bridge is down" — the bridge answered 80 requests in 18.5 seconds with a perfect record
*after* the sweep had already recorded those exact names as silent. **The failure attaches to the
full-universe sweep as a usage pattern, not to the transport.** The KR desk measured the identical split
this morning on its own corpus (5.9% swept vs 100% standalone, successes spread evenly across the whole
processing order). Two desks, two universes, one shape. **[measured, n=2 desks × 1 session]** Repair
direction (retry / backoff / concurrency reduction) is a human-approval item — this stage does not fix
(rule 1).

### (c) ★ The "monotone nesting" shape from yesterday is FALSIFIED

Yesterday's table recorded, as a new finding, that the survivor set **only ever shrinks** — three runs,
zero new entrants, one dropout (`RTX`). Today extends and breaks that series:

| | 08-14 | 08-15 | 08-16 | **08-17** |
|---|---|---|---|---|
| Survivors | 51 | 51 | 50 | **51** |
| Today-only (new entrants) | — | 0 | 0 | **1 — `RTX` (re-entered)** |
| Prior-only (dropouts) | — | 0 | 1 (`RTX`) | **0** |
| Shared names whose value moved | — | 48/51 | 48/50 | **41/50** |

⇒ **The name that left yesterday came back today.** The set is a stable ~50-name core plus a flickering
edge, not a monotone nest. Yesterday's shape was a two-point artifact and is retracted here rather than
quietly dropped. What survives from it: the core **is** unusually stable across four runs, the mechanism
selecting it is **still unidentified**, and it is **not** article volume (`C` returns 201 articles over
7 days and has never been a survivor). Handed up as a dig item, unexplained.

### (d) ★★ NEW — `breadth` carries the broken axis. A right granted yesterday is revoked.

**Measurement.** Today's 299 `flow_score` values are **identical to yesterday's — every one of them**
(0 differing names). Prices are the same 08-14 close, and the news axis is dropped in both runs. Yet the
sector table is **not** identical: `Financials` breadth **0.04 → 0.06**, `Communication Services` breadth
**0.08 → 0.00**.

Cause, traced in the code: `sector_flow.py:224` computes `tag = flow_read.flow_tag(p, vel)` — the
synthesized 🟢/🟡/🔴 label consumes **raw velocity**, and it does so **outside** the axis-drop guard that
protects `flow_score`. `breadth` is then defined at `sector_flow.py:342` as `greens / len(names)` over
that tag. So when the news bridge answers for a name in one run and not the next, its tag can move with
no price change at all. Two names did exactly that today:

| Name | 08-16 tag | 08-17 tag | 08-16 velocity | 08-17 velocity | flow_score |
|---|---|---|---|---|---|
| `NFLX` | 🟢가속 | **🟡중립** | 1.23 | **1.17** | **unchanged** |
| `MA` | 🟡중립 | **🟢가속** | 1.17 | **1.29** | **unchanged** |

⇒ **Two sector breadth readings moved on zero new price information.** The universe totals happen to
cancel (9 green / 60 red both runs), which is precisely why this went unnoticed for four runs — the
aggregate is stable while the *per-sector* numbers are not.

★ **This directly contradicts what yesterday's rights table told the desk**: *"eqflow · breadth —
unweighted, so the 32-day-stale caps barely touch them; with the news axis down these carry more load,
not less."* The staleness half was right; the news-independence half is now measured to be wrong.
**`eqflow` survives** (it averages `flow_score`, which the guard protects). **`breadth` does not.**

### (e) Local fallback and the independent witness

| Bridge | State |
|---|---|
| Remote `…ngrok-free.dev/exec` | **answering** — 5/5 CLI at 22:13, 80/80 library at 22:14; **17% inside the sweep** at 22:11 |
| `data/news_vectors.db` (client-owned derivative, **1.084 GB**, 432,170 articles) | ✅ cursor **`2026-08-17T09:23:10`**. Rows: 08-12 **9,216** · 08-13 **9,114** · 08-14 **8,102** · 08-15 **3,034** · 08-16 **2,909** · **08-17 567 (partial)** |
| `data/news_fts.db` (foreign index) | **0 bytes**, mtime 2026-08-12 — unchanged 5 days |
| `data/news_fts_kr.db` | **0 bytes**, mtime 2026-07-30 |
| `data/news_alert.db` | **0 bytes** — present as an empty file, no raw store to rebuild an index from |

**🚫 Rights revoked today**
1. **No citation of the sweep's news-velocity axis, and no citation of the 51 survivors.** They are a
   non-random sample selected by an unmeasured mechanism (§c) — worse than a random sample, not better.
2. **"It has gone quiet" is forbidden as evidence.** Measured **0 of 120** across three runs.
3. `flow_score` is a **3-axis score** — that fact goes on the **same line** as any conclusion drawn from
   it, every time.
4. ⚠ **The inverse is equally forbidden** — "the news axis is dead, therefore there is no news." Today's
   probe answered 40/40; the world is loud and the sweep did not hear it.
5. ★ **NEW — `breadth` may not be cited as a news-independent reading, and no sector may be promoted,
   demoted, or ranked on a `breadth` change versus a prior run.** Measured today: two sectors moved on
   zero new prices. Where a stage wants an unweighted cross-section, **use `eqflow`**, which is protected
   by the axis-drop guard. A *level* reading of breadth within this single run is permitted **only** with
   the note that its tag input is 17%-covered.
6. ⚠ **No claim that a transport is dead** without the probe clock time on the same line. Across five
   runs this desk has recorded the CLI path at 5/5 dead and 5/5 alive on consecutive days.

**✅ Rights available, with conditions**
- **Per-name news velocity may be cited** when the desk runs the probe for that specific name and writes
  **the returned 7d/30d counts and the probe clock time on the same line as the claim.** Measured warrant
  today: **100% success at probe rate (40/40), 0% false silence**. Two limits travel with it: (i) it is an
  **article-count ratio, not content** — attention moved, never why; (ii) a name that fails the probe is
  **unmeasured, not quiet**.
- **`theme_age` / `chain_hop` / `drift_watch` are conditionally permitted** — only where a value actually
  returned, quoted with its probe time. An **empty** result may never be read as "cooled". ⚠ This binds
  stage 11 (DRIFT): DRIFT must state whether its instrument answered, and an empty burst list is not
  "no drift".
- **`news_vectors.db` through 2026-08-16.** ⚠ **08-17 is partial (567 rows, cursor 09:23 KST)** — do not
  read a low 08-17 count as a quiet Monday.

⚠ **The sweep is not re-run for the news axis (unattended rule, practice carried since 08-07).**
① the prior snapshot is **3-axis**, so switching to 4-axis makes G2 fail immediately and kills the Δ
outright; ② it would overwrite `history.json` key `2026-08-14` on a different scale and break the *next*
run's baseline; ③ today's own measurement says a full-universe re-run would land in **partial** coverage
again, which is the exact entrance to the defect this gate exists to catch (an axis dropping per-name and
inflating scores). ⇒ **The 3-axis `nonews` output stands as this run's official instrument.**

---

## G2 · Scoring-scale continuity — 🟢 PASS *(literally — and the Δ is the fourth reading of one session)*

**Command** `§scoring.n_axes` vs `llm_outputs/sector_flow/history.json` previous snapshot `_mode`

| Snapshot key | `_mode` | n | Note |
|---|---|---|---|
| 2026-08-05 | news (4-axis) | 300 | |
| 2026-08-06 | news (4-axis) | 300 | last 4-axis run |
| 2026-08-07 | nonews (3-axis) | 299 | |
| 2026-08-11 | nonews (3-axis) | 300 | |
| 2026-08-12 | nonews (3-axis) | 300 | |
| **2026-08-13** | **nonews (3-axis)** | 300 | ← **today's Δ baseline (and 08-15's, and 08-16's)** |
| **2026-08-14** | **nonews (3-axis)** | **299** | ← **this run's saved key — overwritten for the third time** |

Axis count matches (3 = 3) ⇒ **PASS on the gate's own condition.** No apples-to-oranges subtraction.

**★ The Δ is not new information, stated explicitly for the third run running.**
The last settled US close is **2026-08-14**; 08-15 and 08-16 were the weekend, and 08-17's session had
not opened when this sweep ran (G0). So this run **wrote the same key `2026-08-14`** and **re-picked the
same baseline `2026-08-13`**.
⇒ **Today's Δ = 08-13 close → 08-14 close = the identical interval the 08-15 and 08-16 runs reported.
Newly observed sessions: ZERO. This is the fourth reading of one Friday.**

Direct corroboration, and it is stronger than yesterday's: **all 299 `flow_score` values are identical to
the 08-16 run** — not "to three decimals", but zero differing names. Universe aggregate identical
(`n=299 · wflow −0.132 · 9 green / 60 red`).
⚠ **The two exceptions prove the point rather than weakening it**: `Financials` and `Communication
Services` `breadth` moved, and §G1(d) shows that movement came from the **news bridge**, not from the
market. A stage that read those two numbers as a change would be reading instrument flicker as tape.

**🚫 Rights revoked today**
1. **No Δ may be described as "today's change", "the latest session", or "accelerating".** The required
   form is **"08-13 → 08-14, one settled session, the same interval as the three prior runs."**
2. **Agreement with the 08-15/08-16 reports may not be cited as confirmation, persistence, or
   stability.** It is the same file read four times.
3. **The `history.json` date keys may not be trusted as observation dates** in any key-indexed time
   series (`ic_ledger`, `axis_inflection`, `reject_ledger`). This run created **no new key** — it
   overwrote `2026-08-14` for the third time.

---

## G3 · Who owns the sector sign — 🟢 PASS

**Command** `§sector_rotation[].top1_flips_sign` — the list must be printed (zero entries still PASS)

**3 of 11** sectors flip sign when their single largest name is removed. Printed in full:

| Sector | wflow | ex-top1 | top1 | top1_w | n | eqflow | breadth |
|---|---|---|---|---|---|---|---|
| Information Technology | **+0.023** | **−0.082** | `NVDA` Nvidia | 19.4% | 56 | +0.044 | 0.05 |
| Industrials | **−0.047** | **+0.006** | `CAT` Caterpillar | 8.7% | 50 | −0.007 | 0.00 |
| Materials | **−0.169** | **+0.033** | `LIN` Linde plc | 24.7% | 12 | −0.114 | 0.00 |

Full 11-sector `wflow` ordering this run (unchanged from 08-16 in every value):
Energy **+0.217** · IT **+0.023** · Financials −0.031 · Industrials −0.047 · Health Care −0.115 ·
Materials −0.169 · Consumer Staples −0.242 · Real Estate −0.280 · Consumer Discretionary −0.378 ·
Communication Services −0.436 · Utilities −0.445.

⚠ **Identical set, identical numbers to the 08-15 and 08-16 runs** — for the reason G2 gives (same input
file). Do **not** read "the same three flippers three runs running" as a structural fact. It is one
observation read four times.

★ **The one that matters.** Information Technology is the desk's largest sector (n=56) and, after Energy,
its **only non-negative `wflow`** — and that non-negativity is **entirely one name**. Strip `NVDA` and IT
reads **−0.082**. A sign flip only appears when weighted flow is sitting on zero: IT at **+0.023** is not
a strong sector, it is a sector with **no aggregate signal** in which one 19.4%-weighted name decides the
sign. `eqflow +0.044` points the same faint way; the `breadth 0.05` that used to be quoted alongside is
now a **news-contaminated statistic** (§G1(d)) and is not quotable as corroboration.
⚠ Industrials is the mirror image: `wflow −0.047` vs `ex-top1 +0.006` on a top1 weight of only **8.7%**.
The flip is real but the sector is uniformly weak either way (`eqflow −0.007`).
⚠ Every `top1_w` here is computed from a **33-day-old market-cap file** (G5).

**Binding**: **Information Technology, Industrials and Materials may not be promoted or demoted on
`wflow`** (ROTATION §2). Use `eqflow`, or hold the call. **`breadth` is no longer an available
substitute** — that is new today.

---

## G4 · Risk-unit stability — 🔴 FAIL (8th consecutive run)

**Command** `python -X utf8 scripts/risk_units.py --book --days {250,500,750}` — **all three actually run**

| `--days` | Units | Window | In-group resid. corr | Max resid. corr | ARI (1st half vs 2nd) |
|---|---|---|---|---|---|
| 250 | **11** | 2025-07-29 → 2026-08-14 (249 sessions) | +0.6058 | +0.8524 | 0.4902 |
| 500 | **10** | 2024-07-02 → 2026-08-14 (499 sessions) | +0.5248 | +0.8467 | 0.3743 |
| 750 | **10** | 2023-06-12 → 2026-08-14 (749 sessions) | +0.5135 | +0.8217 | 0.3810 |

**500 and 750 agree; 250 does not.** The book is 13 names; the disagreement is three pairs:

| Pair | 250d | 500d | 750d |
|---|---|---|---|
| `AVGO` · `NVDA` | **separate** (U3·U9) | **merged** (U1) | **merged** (U1) |
| `ANET` · `ETN` | **separate** (U2·U4) | **merged** (U0) | **merged** (U0) |
| `028050` · `316140` (KR) | **merged** (U0) | separate (U3·U4) | separate (U3·U4) |

`MPC`·`PSX` merge in all three windows — the only unit the instrument agrees on.
The tool flags the `ANET·ETN` merge itself at 500d/750d: *"two different theme labels inside one measured
unit — `MAX_THEME_PCT` is counting this as two"* (`AI-compute-EPICENTER` vs `AI-power/electrical`). At
250d the KR pair draws the same warning.
Threshold sensitivity, re-measured: at `dist` 0.40–0.60 **all three windows converge on 12 units**; the
disagreement appears only at the selected 0.65. **The instability is attached to the threshold choice**
(C5 — an arbitrary choice that changes the answer).
Standing tool warnings, re-logged: **ARI 0.37–0.49 moves opposite to fit (S5)**; **249 < 250 sessions** at
the short window; **KR returns are KRW and US returns are USD** so a common FX factor can be injected;
intersection holes up to **8 days**.
※ **Numbers identical to 08-14, 08-15 and 08-16** (11/10/10) — eighth run in the same place, and the
window end is 2026-08-14 in all three, so this too is a re-reading.

**🚫 Rights revoked today**
1. **No single-number concentration guard** in BET/SIZE.
2. Any concentration statement must carry **the `--days` window on the same line as the conclusion**.
3. **No verdict today on whether `AVGO`+`NVDA` are one unit or two** — the window picks the answer, and
   2 of 3 windows say one. Same for `ANET`+`ETN` (2 of 3 say one) and the KR pair (1 of 3).

---

## G5 · Does the universe cover the book — 🔴 FAIL *(on staleness only; coverage is clean)*

**Command** `data/us_universe/us_top300.csv` × `module_paper_book status` holdings × the scored-name set

| Item | Value |
|---|---|
| Book holdings | **13** (US 11 · KR 2) · total **17,859,402 KRW** · cash KRW 4,938,207 + USD 1,904 |
| US holdings inside `us_top300` | **11 / 11 ✅** — ANET · AVGO · ETN · HPE · MET · MPC · NDAQ · NUE · NVDA · PSX · RTX |
| US holdings actually **scored** by the sweep | **11 / 11 ✅** (verified against `§names`, not just the CSV) |
| ★ `LNG` · `TSM` outside-universe hole | **still closed** — neither is held (was logged 12 consecutive runs) |
| `us_top300.csv` age | **33 days** (mtime 2026-07-15, limit **≤8**) → 🔴 |
| Universe size | 300 requested / **299 scored** |
| ⚠ **Null last bar** | **`EA`** — 300 of 301 columns carry an 08-14 close; `EA`'s last close is **08-10** (**5th consecutive run**) |
| Rebuild candidate | `data/us_universe/us_all_v2_candidate.csv` (mtime 08-10, 129 KB) **exists, unpromoted** — promotion is a human decision (P5) |

Sweep log line 1: `[warn] 유니버스 us_top300.csv 33일 경과 — 시총 stale.`
Universe aggregate this run: **n=299 · wflow −0.132 · 9 green / 60 red** (identical to 08-16).
⚠ KR holdings show `PRICE n/a` again (no KIS mark) — irrelevant to this desk, logged for the ledger.

**🚫 Rights revoked today**
1. **`wflow` may not be described as "current market-cap weighted"** — the weights are **33 days old**.
   Every `top1_w` in G3 inherits this, including the 19.4% that decides IT's sign.
2. **No flow / RS / OBV / short verdict on `EA`** — it was not measured. Absence of a bar is not absence
   of a move. Fifth run running; it is also absent from the Δ set (G2).
3. ✅ **Positive, sixth consecutive run**: every name the book holds can be tagged by every instrument the
   desk uses. There are **zero** "held but unmeasurable" names.

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL

**Command** `python -X utf8 scripts/snapshot_estimates.py --status`

| Item | Value |
|---|---|
| Accumulated | **10 files / 24 calendar days** (2026-07-22 → 2026-08-14), 120 names each |
| Measured rate | **0.42 files/day** (ideal 1.0) |
| To the 40-day target | ideal **30 days** vs measured **≈72 days** = **2.4×** (limit 1.5×) |
| Gaps (days) | [3, 4, 6, 3, 1, 2, 1, 1] · median 2 · max 6 |
| Since last save | **3 days** (08-14) — the weekend accrues nothing, and 08-17 is not yet captured |

Unchanged from 08-14/08-15/08-16 except the "days since" counter. Not recoverable retroactively: days not
captured are gone. The tool re-logs its own trap: *"counting files makes this look healthy"* (D16).

**🚫 Rights revoked today**
1. **No reporting of `kelly_size --ic` output as an evidence-backed size.**
2. Any size written today is labelled **"mechanical ¼"**.

---

## G7 · Tool liveness — 🔴 FAIL (2 of 46 · 8th consecutive run, same two)

**Command** `--help` on every entry point this run will use; exit code recorded. **exit 0 = 44 / 46.**

**exit 0 — 44**: `sector_flow` · `us_live_shortlist` · `us_flow` · `flow_read` · `exposure_rule` ·
`missed_ledger` · `reject_ledger` · `kelly_size` · `catalyst_calendar` · `report_lint` · `risk_units` ·
`axis_window_flow` · `snapshot_estimates` · `ic_ledger` · `leak_scan` · `axis_inflection` ·
`cycle_exposure` · `drift_watch` · `us_setup_screener` · `action_bracket` · `handoff_id_audit` ·
`handoff_compact` · `yf_snapshot` · `brief_recall` · `measure_ic` · `module_news_data` · `module_KIS` ·
`module_valuation` · `module_report_tags` · `module_disclosure_us` · `module_disclosure` ·
`module_fundamentals_us` · `module_fundamentals_kr` · `module_business_us` · `module_business` ·
`module_paper_book` · `module_macro_us` · `module_industry_map` · `module_flow` · `module_watchlist` ·
`module_epistemics` · `module_inflection` · `module_math_check` · `module_publish`

**exit 1 — 2** (identical to 08-10 · 08-12 · 08-13 · 08-14 · 08-15 · 08-16 and this morning's KR run)

| Tool | `--help` failure | Functional probe (rule 3), actually run |
|---|---|---|
| `scripts/margin_history.py` | exit 1 — `%`-format bug in the help string (argparse `_expand_help`) | `margin_history.py NVDA` → **exit 0**: gross margin FY2008–FY2026 (19 years, 0 gaps), high **FY2025 75.0%** · low **FY2009 34.3%** · **median 56.9%** · FY2026 **71.1%** on **$215.9B** revenue |
| `module_chart` | exit 1 — CLI does not implement `--help` (prints usage, exits 1) | `module_chart NVDA --read` → **exit 0**: OBV **neutral** (20d slope **+10%**) · no divergence · bull stack 5>20>60>120, price above 4/4 MA · Bollinger expansion 20.8%, mid-band · **RSI 75.4** · momentum20d **+10.8%** · turn verdict **NEUTRAL/CHOP** · swing-low stop **190.01** |

⇒ Under rule 3 both were **actually run and produced correct output** ⇒ **citation rights retained**, but
the warrant is the **probe output above**, not `--help`, and only for **those two command lines**.
⚠ Both probes returned **byte-identical output to the 08-16 run's** — same 08-14 close, same SEC filings.
⚠ A broken `--help` means a human cannot discover the tool. **Logged unrepaired for the 8th run.**

---

## What this table binds today (handed to HANDOVER)

| Stage | Cannot use today |
|---|---|
| **ALL** | ★ **any Δ or comparison described as "today", "the latest session", "now accelerating"** — zero new sessions since the prior three runs · **agreement with the 08-15/08-16 reports as confirmation** · ★ **any statement that this run reflects Monday 08-17 trading** (the bell rang after the sweep) |
| SWEEP | the sweep's news-velocity axis · the 51 survivors (non-random, mechanism unidentified) · theme freshness · "quiet" · stale (33-day) mcap described as current · any verdict on `EA` · ★ **`breadth` as a news-independent reading** |
| EVENT_ALPHA | "theme is fresh/cooled" from an **empty** `theme_age` / `chain_hop` result · `news_vectors.db` **after 2026-08-16** (08-17 is a partial 567-row day) |
| ROTATION | **`wflow` promotion/demotion for Information Technology, Industrials and Materials** (G3 flippers) · news-axis tie-breaks · ★ **`breadth`-change tie-breaks — use `eqflow`** · "the fourth run running" as a persistence argument |
| PREMORTEM | "the tape has gone quiet on this risk" — measured, **0 of 120** silent names were quiet |
| DEEP | the velocity axis as an axis · "no news flow" as evidence of anything |
| BET / SIZE | single-number concentration · `--ic`-backed size (→ **"mechanical ¼"**) · `AVGO/NVDA` and `ANET/ETN` unit counts |
| DRIFT | **must state whether `drift_watch`'s instrument answered, with the probe clock time.** An empty burst list today is not "no drift" |

**What this desk CAN speak with today (stated positively).**
① **Settled prices through 2026-08-14** — with **RS at fine grain** (G0 clean, fifth run running).
② **OBV level and state** — last bar complete, verified by a zero count of 08-17 rows.
③ **`eqflow`** — unweighted **and** protected by the axis-drop guard, so it is the cross-section
   statistic that survived today's `breadth` finding. It carries more load than yesterday, not less.
④ **`vol_surge` in both directions** — licensing the reading that 08-13 and 08-14 were both light-volume
   sessions (0.732 then 0.649 of the 20-day norm).
⑤ **FINRA short pressure · CFTC COT percentile positioning** — the US substitute for the investor-type
   feed. Context, never a trigger.
⑥ **FRED macro series** (`module_macro_us`, cite `[FRED]`) — **the only axis on this desk that can have
   moved since the prior run**, because it is not keyed to the equity session.
⑦ **Primary filings** (`module_disclosure_us` / `module_fundamentals_us`) and **margin history**.
⑧ **Per-name news velocity by hand probe** — **100% measured success today (40/40), 0% false silence**,
   provided the 7d/30d counts **and the probe clock time** are on the same line as the claim. This is the
   strongest this right has been in five runs.
⑨ **`news_vectors.db` through 2026-08-16** (cursor 08-17T09:23).

**Speak with settled 08-14 prices, `eqflow`, positioning, primary documents, FRED, and news counts you
fetched yourself with the clock time attached. Do not speak with the sweep's news axis, a `breadth`
change, a single concentration number, or the word "today" attached to any price-derived reading.**

*Instrument state is not a market view — this document is not written into `handoff/` (HANDOVER only reads it).*
