# PREFLIGHT — 2026-08-16 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-16 20:05–20:35 = ET 2026-08-16 07:05–07:35, SUNDAY — US cash closed.**
> Sweep data **asof 2026-08-14** — last settled US close (Friday). No session is open behind this run.
>
> ★ **The headline of this preflight is a negative one and it is stated up front: this run inherits
> ZERO new price sessions.** Yesterday's US run (08-15, Saturday) also priced off the **08-14** close.
> 08-15 was Saturday, 08-16 is Sunday. Every price-derived number below is **byte-comparable to
> yesterday's**, and where it is identical that is **evidence of identical input, not of a stable
> signal.** The KR desk reached the same conclusion at 08:39 this morning for the same calendar reason.
>
> ⚠ **Filename deviation, logged (7th consecutive run, same reason):** the composition table names this
> `preflight/PREFLIGHT.md`, but the `industry_kr` desk already wrote its rights table to that path this
> morning (08:56 KST). Overwriting a sibling desk's output is not a correction, so the US table is
> written as `PREFLIGHT_US.md` in the same folder — the documented practice on 08-10 · 08-12 · 08-13 ·
> 08-14 · 08-15. Human decision on permanent market-suffixing still pending (PROMPT_MAP §6).

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** | Last bar **2026-08-14**, **settled by construction** (weekend run). **SPY 85/85** valid bars, carries the 08-14 bar (**776.34**) → matched RS endpoints. **Fourth consecutive clean US clock** |
| **G1** news axis alive | 🔴 **FAIL** *(4th run — and the diagnosis inverted for the second time)* | Sweep coverage **16.7% (50/299)**, down from 17.1%. ★ The 50 survivors are a **strict subset** of yesterday's 51 (today-only **0**, RTX dropped out) — three runs, a nested set. Re-probe of the "silent" names: **24/40 valid (60.0%) · 16 pipe-fail (40.0%) · ZERO genuinely quiet.** ★ **The CLI path, 5/5 dead yesterday, is 5/5 ALIVE today** |
| **G2** scoring-scale continuity | 🟢 **PASS** *(literally)* | **3-axis (`nonews`) vs 3-axis (`nonews`)** ⇒ no apples-to-oranges subtraction. ★ **But the Δ carries no new information** — `asof` is **the same 2026-08-14** as yesterday's saved key, baseline is again **08-13**. Today's Δ is **a replay of yesterday's Δ** |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **3 of 11** (IT/`NVDA` · Industrials/`CAT` · Materials/`LIN`). **Identical set and identical numbers to yesterday** — same input file, not a confirmed structure |
| **G4** risk-unit stability | 🔴 **FAIL** | 250d **11 units** · 500d **10** · 750d **10** — 500 and 750 agree, **250 does not** (**7th consecutive run, identical numbers**) |
| **G5** does the universe cover the book | 🔴 **FAIL** *(on staleness only)* | **11/11 US holdings inside `us_top300` AND scored ✅** (verified against `§names`). But `us_top300.csv` is **32 days old** (limit ≤8) and **`EA` returns a null last bar for the 4th consecutive run** |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** | Measured ETA **≈72 days** vs ideal 30 = **2.4×** (limit 1.5×). 10 files / 24 calendar days; last save **08-14**, and a Sunday accrues nothing |
| **G7** tool liveness | 🔴 **FAIL** | **46 entry points** probed, **2** non-zero `--help` (`scripts/margin_history.py` · `module_chart`) — **7th consecutive run unrepaired**. Both pass a functional probe ⇒ citation rights retained **for those command lines only** |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate).
Headline count identical to 08-15 — **and this time the identity is itself the finding.** Two of the
three PASSes (G2, G3) pass on numbers that are *literally the same bytes* as yesterday's, because the
input file is the same 08-14 close.

Today this desk **cannot** speak with the sweep's news-velocity axis, theme freshness, "it went quiet",
a single concentration number, an `--ic`-derived size, or **any Δ described as "today's change"**. It
**can** speak with settled prices through the **08-14** close, fine-grain RS, OBV, breadth, `vol_surge`
both ways, FINRA short pressure, CFTC COT positioning, FRED series, primary filings, hand-probed
per-name news velocity — and, **restored today**, `news_vectors.db` (its sync cursor un-stalled).

---

## G0 · Bar completeness · date alignment — 🟢 PASS *(bonus gate)*

Not one of the seven. Carried because the KR desk measured it into existence on 08-12 and it has failed
repeatedly there — intraday stubs and benchmark bar gaps that silently re-date a whole run.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-16.pkl`
(85 rows × 1806 columns = 301 tickers × 6 fields, MultiIndex `Ticker`×`Price`) + `SECTOR_FLOW_US.json §asof`.

| Item | Value | vs 08-15 run |
|---|---|---|
| Run clock | **07:05 ET Sun 08-16 — MARKET CLOSED** | closed then too |
| Last index in the price frame | **2026-08-14** (Friday) | **same** |
| Last-bar volume / prior-20d average — median | **0.649** (q25 **0.543** · q75 **0.822**, n=300) | **identical** |
| Benchmark `SPY` last three bars | 08-12 **772.49** · 08-13 **777.88** · **08-14 776.34** | **identical** |
| `SPY` valid bars vs frame rows | **85 / 85** — no benchmark gap | same |
| `SPY` own last-bar volume / 20d | **0.646** | — |
| `SECTOR_FLOW_US.json §asof` | **2026-08-14** — matches the data's own last index | same |
| Non-null closes on the last row | **300 / 301** (one hole → G5) | same |

⇒ Because the run is on a **non-session day**, an incomplete last bar is **impossible in principle** —
the strongest form this gate can pass in. Benchmark and names share the same terminal date, so
`rs20 = ret(name,20) − ret(bench,20)` has **matched endpoints**.

⚠ **The 0.649 is a real light-volume reading, not a clock artifact** — 08-14 was a full Friday in which
SPY fell 777.88 → 776.34 (**−0.20%**) on about two-thirds of the trailing 20-day volume norm, itself
below 08-13's 0.732. **But it is not a new observation.** It is the same Friday bar yesterday's run
already read. **[measured 08-14, re-read 08-15 and 08-16 — one observation, three readings.]**
Not an opex artifact either: August monthly expiry is 08-21.

**✅ Rights available for this run:**
1. **RS20/RS60 may be compared at fine grain** — no contamination band.
2. **`vol_surge` may be read in both directions** — the last bar is complete, so a low reading is a
   low reading.
3. `asof 2026-08-14` may be written plainly as "data through the 08-14 close".
4. 🚫 **But**: any sentence of the form "volume thinned *today*" is forbidden. The correct form is
   "through the 08-14 close, and unchanged since this desk last looked."

---

## G1 · News axis alive — 🔴 FAIL *(4th consecutive run — diagnosis inverted for the second time)*

**Commands**
- `SECTOR_FLOW_US.json §scoring` → `{"vel_axis": false, "vel_coverage": 0.1672, "n_axes": 3, "scored": 299, "dropped_missing_axis": 0}`
- Sweep's own health line: `[axis] velocity 측정 50/299 = 16.7% → 속도축 제외(전원 3축) · 기준 80%` + the 🚨 line
- Falsification probe A (CLI path), actually run at **20:26 KST**:
  `python -X utf8 -m module_news_data fts search <name> --days 7 --count --scope foreign`
- Falsification probe B (library path, **the exact call the sweep makes**), actually run at **20:24 KST**:
  `flow_read.news_velocity(flow_read._news_query(tk, name), 7, 30, kr=False)` on a seeded n=40 draw
  from the 249 names the sweep recorded as `velocity: None`

### (a) ★ Probe A — the CLI path is ALIVE today, 5/5. Yesterday it was 5/5 dead.

| Probe (20:26 KST) | Result |
|---|---|
| Nvidia | ✅ **3,639** articles / 7d · `(via NEWS API @ …ngrok-free.dev)` |
| Broadcom | ✅ **359** |
| Eaton | ✅ **49** |
| Nucor | ✅ **17** |
| Raytheon | ✅ **9** |

Yesterday this exact command failed 5/5 with `URLError(FileNotFoundError(2))`, and yesterday's table
concluded *"the CLI endpoint fails 5/5 while the library endpoint answers 85%."* **Today the two have
swapped rank.** This is the second inversion in three runs, and it matches what the KR desk measured
independently this morning: at 08:41 the CLI answered 5/5, at 08:44–08:50 it failed 51/51, at 08:54 it
answered again. ⇒ **The bridge is not dead and it is not alive. It flickers on a timescale of minutes,
and which transport happens to be up when you look is close to a coin flip.** **[measured, n=3 sessions]**

### (b) Probe B — library path down to 60%, but still ZERO genuine silence

| Re-probe (n=40 seeded draw from the 249 "silent" names, 80 requests, **14.4 s**) | Count | Share | 08-15 |
|---|---|---|---|
| **Valid velocity returned** — the sweep simply failed to count it | **24** | **60.0%** | 85.0% |
| **Pipe failure** | **16** | 40.0% | 15.0% |
| **Genuinely zero articles in the window** | **0** | **0.0%** | **0.0%** |

Worked examples, all from the sweep's *dead* list, all `"source": "api"`:
`C` 7d **201** / 30d 1,053 → **0.82** · `MSTR` 91/365 → **1.07** · `PEP` 46/221 → **0.89** ·
`PSX` 36/124 → **1.24** · `MDT` 29/97 → **1.28** · `XYZ` 25/69 → **1.55** · `DVN` 22/90 → **1.05** ·
`BNY` 12/49 → **1.05** · `GRMN` 12/106 → **0.49** · `CI` 8/67 → **0.51** · `SLB` 1/12 → **0.36**.

⇒ **Cumulative over two runs: 0 of 80 "silent" names were actually quiet.** The sweep's ~83% silence
remains **100% instrument, 0% world**. The success *rate* is unstable (85% → 60%); the *false-silence
rate* is stable at zero.

### (c) ★ The survivor set is NESTED, not resampled — new evidence on the unexplained mechanism

Yesterday logged as unexplained: the 51 survivors were the *same 51 tickers* as on 08-14 while 48 of
51 carried different values. Today extends the series:

| | 08-14 | 08-15 | 08-16 |
|---|---|---|---|
| Survivors | 51 | 51 | **50** |
| Today-only (new entrants) | — | **0** | **0** |
| Prior-only (dropouts) | — | **0** | **1 — `RTX`** |
| Shared names whose value moved | — | 48/51 | **48/50** |

**Three runs, zero new entrants, one dropout.** A rate-dependent random failure would resample the
survivor set every run; this set only ever **shrinks**. That is a different mechanism from the one the
85%/60% probe measures, and it is still **not identified** — it is not article volume (`C` returns 201
articles over 7 days and is a non-survivor), and it is not caching (48 of 50 values moved).
⇒ **Recorded as unexplained, now with a shape: monotone nesting.** Repair and root-cause are not this
stage's job (rule 1); this is handed up as a dig item.

### (d) ✅ The independent witness un-stalled — a right RESTORED

`data/news_vectors.db` (**1.076 GB**, 428,716 articles) was flagged yesterday with its sync cursor
**frozen at `2026-08-14T07:59:45`**, which put the entire Friday 08-14 session outside the local store.

| Reading | 08-15 run | **08-16 run** |
|---|---|---|
| Sync cursor | `2026-08-14T07:59:45` (frozen) | **`2026-08-16T09:01:55`** ✅ |
| Rows on `market_day` 2026-08-14 | **487** | **7,992** ✅ |
| Rows on 08-15 · 08-16 | 0 · 0 | **2,938 · 363** |

⇒ **The 08-14 session is now witnessed.** The store may be used through **2026-08-15**. ⚠ **08-16 is
partial (363 rows, run still in progress)** — do not read a low count on 08-16 as a quiet Sunday.

### (e) Local fallback — still none

| Bridge | State |
|---|---|
| Remote `…ngrok-free.dev/exec` | **flickering** (see a/b) |
| `data/news_fts.db` (foreign index) | **0 bytes**, mtime 2026-08-12 10:51 — unchanged 4 days |
| `data/news_fts_kr.db` | **0 bytes**, mtime 2026-07-30 |
| `data/news_alert.db` | **0 bytes** — present as an empty file, no raw store to rebuild an index from |

**🚫 Rights revoked today**
1. **No citation of the sweep's news-velocity axis, and no citation of the 50 survivors.** They are a
   **non-random, monotonically nesting** sample selected by an unmeasured mechanism (§c) — worse than
   a random sample, not better.
2. **"It has gone quiet" is forbidden as evidence.** Measured **0 of 80** across two runs.
3. `flow_score` is a **3-axis score** — that fact goes on the **same line** as any conclusion drawn
   from it, every time.
4. ⚠ **The inverse is equally forbidden** — "the news axis is dead, therefore there is no news."
5. ⚠ **No claim that a transport is dead.** Yesterday's table said the CLI was dead; today it answers
   5/5. Both statements were true at the minute they were measured and false four minutes either side.
   A transport may only be described **with the clock time of the probe on the same line.**

**✅ Rights available, with conditions**
- **Per-name news velocity may be cited** when the desk runs the probe for that specific name and
  writes **the returned 7d/30d counts and the probe time on the same line as the claim.** Measured
  warrant today: **60% success at probe rate, 0% false silence.** Two limits travel with it: (i) it is
  an **article-count ratio, not content** — attention moved, never why; (ii) a name that fails the
  probe is **unmeasured, not quiet**.
- **`theme_age` / `chain_hop` / `drift_watch` are conditionally permitted** — only where a value
  actually returned, quoted with its probe time. An **empty** result may never be read as "cooled".
  ⚠ This binds stage 11 (DRIFT): DRIFT must state whether its instrument answered, and an empty burst
  list is not "no drift".
- **`news_vectors.db` through 2026-08-15** (restored today, §d).

---

## G2 · Scoring-scale continuity — 🟢 PASS *(literally — and the Δ is worth nothing)*

**Command** `§scoring.n_axes` vs `llm_outputs/sector_flow/history.json` previous snapshot `_mode`

| Snapshot key | `_mode` | n | Note |
|---|---|---|---|
| 2026-08-06 | news (4-axis) | 300 | last 4-axis run |
| 2026-08-07 | nonews (3-axis) | 299 | |
| 2026-08-11 | nonews (3-axis) | 300 | |
| 2026-08-12 | nonews (3-axis) | 300 | |
| **2026-08-13** | **nonews (3-axis)** | 300 | ← **today's Δ baseline (and yesterday's)** |
| **2026-08-14** | **nonews (3-axis)** | **299** | ← **this run's saved key — overwriting yesterday's identical entry** |

Axis count matches (3 = 3) ⇒ **PASS on the gate's own condition.** No apples-to-oranges subtraction.

**★ But the Δ is not new information, and this is written explicitly.**
Today is Sunday; 08-15 was Saturday. The last settled US close is **2026-08-14**, which is exactly what
yesterday's run priced off. So this run **wrote the same key `2026-08-14`** with the same content and
**re-picked the same baseline `2026-08-13`**.
⇒ **Today's Δ = 08-13 close → 08-14 close = the identical interval yesterday's run reported. Newly
observed sessions: ZERO.**

The corroboration is direct: the 11-sector `wflow` / `eqflow` / `breadth` table is identical to
yesterday's to three decimals, and all three G3 flippers carry identical `top1_w`. **Agreement between
two runs here is evidence of one input read twice, not of a signal holding.**

**🚫 Rights revoked today**
1. **No Δ may be described as "today's change", "the latest session", or "accelerating".** The required
   form is **"08-13 → 08-14, one settled session, the same interval as the prior run."**
2. **Agreement with yesterday's report may not be cited as confirmation, persistence, or stability.**
   It is the same file read twice.
3. **The `history.json` date keys may not be trusted as observation dates** in any key-indexed time
   series (`ic_ledger`, `axis_inflection`, `reject_ledger`). This run created **no new key** — it
   overwrote `2026-08-14`.

---

## G3 · Who owns the sector sign — 🟢 PASS

**Command** `§sector_rotation[].top1_flips_sign` — the list must be printed (zero entries still PASS)

**3 of 11** sectors flip sign when their single largest name is removed. Printed in full:

| Sector | wflow | ex-top1 | top1 | top1_w | n | eqflow | breadth |
|---|---|---|---|---|---|---|---|
| Information Technology | **+0.023** | **−0.082** | `NVDA` Nvidia | 19.4% | 56 | +0.044 | 0.05 |
| Industrials | **−0.047** | **+0.006** | `CAT` Caterpillar | 8.7% | 50 | −0.007 | 0.00 |
| Materials | **−0.169** | **+0.033** | `LIN` Linde plc | 24.7% | 12 | −0.114 | 0.00 |

⚠ **Identical set, identical numbers to the 08-15 run** — for the reason G2 gives (same input file).
Do **not** read "the same three flippers two runs running" as a structural fact. It is one observation.

★ **The one that matters.** Information Technology is the desk's largest sector (n=56) and, after
Energy, its **only non-negative `wflow`** — and that non-negativity is **entirely one name**. Strip
`NVDA` and IT reads **−0.082**. A sign flip only appears when weighted flow is sitting on zero: IT at
**+0.023** is not a strong sector, it is a sector with **no aggregate signal** in which one
19.4%-weighted name decides the sign. `eqflow +0.044` and `breadth 0.05` point the same faint way.
⚠ Industrials is the mirror image: `wflow −0.047` vs `ex-top1 +0.006` on a top1 weight of only **8.7%**,
with `breadth 0.00`. The flip is real but the sector is uniformly weak either way.
⚠ Every `top1_w` here is computed from a **32-day-old market-cap file** (G5).

**Binding**: **Information Technology, Industrials and Materials may not be promoted or demoted on
`wflow`** (ROTATION §2). Use `eqflow` / `breadth`, or hold the call.

---

## G4 · Risk-unit stability — 🔴 FAIL (7th consecutive run)

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
The tool flags the `ANET·ETN` merge itself at 500d/750d: *"two different theme labels inside one
measured unit — `MAX_THEME_PCT` is counting this as two"* (`AI-compute-EPICENTER` vs
`AI-power/electrical`). At 250d the KR pair draws the same warning.
Threshold sensitivity, re-measured: at `dist` 0.40–0.60 **all three windows converge on 12 units**; the
disagreement appears only at the selected 0.65. **The instability is attached to the threshold choice**
(C5 — an arbitrary choice that changes the answer).
Standing tool warnings, re-logged: **ARI 0.37–0.49 moves opposite to fit (S5)**; **249 < 250 sessions**
at the short window; **KR returns are KRW and US returns are USD** so a common FX factor can be
injected; intersection holes up to **8 days**.
※ **Numbers identical to 08-14 and 08-15** (11/10/10) — seventh run in the same place.

**🚫 Rights revoked today**
1. **No single-number concentration guard** in BET/SIZE.
2. Any concentration statement must carry **the `--days` window on the same line as the conclusion**.
3. **No verdict today on whether `AVGO`+`NVDA` are one unit or two** — the window picks the answer,
   and 2 of 3 windows say one. Same for `ANET`+`ETN` (2 of 3 say one) and the KR pair (1 of 3).

---

## G5 · Does the universe cover the book — 🔴 FAIL *(on staleness only; coverage is clean)*

**Command** `data/us_universe/us_top300.csv` × `module_paper_book status` holdings × the scored-name set

| Item | Value |
|---|---|
| Book holdings | **13** (US 11 · KR 2) · total **17,859,402 KRW** · cash KRW 4,938,207 + USD 1,904 |
| US holdings inside `us_top300` | **11 / 11 ✅** — ANET · AVGO · ETN · HPE · MET · MPC · NDAQ · NUE · NVDA · PSX · RTX |
| US holdings actually **scored** by the sweep | **11 / 11 ✅** (verified against `§names`, not just the CSV) |
| ★ `LNG` · `TSM` outside-universe hole | **still closed** — neither is held (was logged 12 consecutive runs) |
| `us_top300.csv` age | **32 days** (mtime 2026-07-15, limit **≤8**) → 🔴 |
| Universe size | 300 requested / **299 scored** |
| ⚠ **Null last bar** | **`EA`** — 300 of 301 columns carry an 08-14 close; `EA` has none (**4th consecutive run**) |
| Rebuild candidate | `data/us_universe/us_all_v2_candidate.csv` (mtime 08-10, 129 KB) **exists, unpromoted** — promotion is a human decision (P5) |

Sweep log line 1: `[warn] 유니버스 us_top300.csv 32일 경과 — 시총 stale.`
Universe aggregate this run: **n=299 · wflow −0.132 · 9 green / 60 red.**

**🚫 Rights revoked today**
1. **`wflow` may not be described as "current market-cap weighted"** — the weights are **32 days old**.
   Every `top1_w` in G3 inherits this, including the 19.4% that decides IT's sign.
2. **No flow / RS / OBV / short verdict on `EA`** — it was not measured. Absence of a bar is not
   absence of a move. Fourth run running; it is also absent from the Δ set (G2).
3. ✅ **Positive, fifth consecutive run**: every name the book holds can be tagged by every instrument
   the desk uses. There are **zero** "held but unmeasurable" names.

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL

**Command** `python -X utf8 scripts/snapshot_estimates.py --status`

| Item | Value |
|---|---|
| Accumulated | **10 files / 24 calendar days** (2026-07-22 → 2026-08-14), 120 names each |
| Measured rate | **0.42 files/day** (ideal 1.0) |
| To the 40-day target | ideal **30 days** vs measured **≈72 days** = **2.4×** (limit 1.5×) |
| Gaps (days) | [3, 4, 6, 3, 1, 2, 1, 1] · median 2 · max 6 |
| Since last save | **2 days** (08-14) — the weekend accrues nothing |

Unchanged from 08-14/08-15. Not recoverable retroactively: days not captured are gone. The tool
re-logs its own trap: *"counting files makes this look healthy"* (D16).

**🚫 Rights revoked today**
1. **No reporting of `kelly_size --ic` output as an evidence-backed size.**
2. Any size written today is labelled **"mechanical ¼"**.

---

## G7 · Tool liveness — 🔴 FAIL (2 of 46 · 7th consecutive run, same two)

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

**exit 1 — 2** (identical to 08-10 · 08-12 · 08-13 · 08-14 · 08-15 and this morning's KR run)

| Tool | `--help` failure | Functional probe (rule 3), actually run |
|---|---|---|
| `scripts/margin_history.py` | exit 1 — `%`-format bug in the help string (argparse `_expand_help`) | `margin_history.py NVDA` → **exit 0**: gross margin FY2008–FY2026 (19 years, 0 gaps), high **FY2025 75.0%** · low **FY2009 34.3%** · **median 56.9%** · FY2026 **71.1%** on **$215.9B** revenue |
| `module_chart` | exit 1 — CLI does not implement `--help` (prints usage, exits 1) | `module_chart NVDA --read` → **exit 0**: OBV **neutral** (20d slope **+10%**) · no divergence · bull stack 5>20>60>120, price above 4/4 MA · Bollinger expansion 20.8%, mid-band · **RSI 75.4** · momentum20d **+10.8%** · turn verdict **NEUTRAL/CHOP** · swing-low stop **190.01** |

⇒ Under rule 3 both were **actually run and produced correct output** ⇒ **citation rights retained**,
but the warrant is the **probe output above**, not `--help`, and only for **those two command lines**.
⚠ Both probes returned **byte-identical output to yesterday's** — same 08-14 close, same SEC filings.
⚠ A broken `--help` means a human cannot discover the tool. **Logged unrepaired for the 7th run.**

---

## What this table binds today (handed to HANDOVER)

| Stage | Cannot use today |
|---|---|
| **ALL** | ★ **any Δ or comparison described as "today", "the latest session", "now accelerating"** — zero new sessions since the prior run · **agreement with yesterday's report as confirmation** |
| SWEEP | the sweep's news-velocity axis · the 50 survivors (monotone-nesting sample) · theme freshness · "quiet" · stale mcap described as current · any verdict on `EA` |
| EVENT_ALPHA | "theme is fresh/cooled" from an **empty** `theme_age` / `chain_hop` result · `news_vectors.db` **after 2026-08-15** (08-16 is a partial 363-row day) |
| ROTATION | **`wflow` promotion/demotion for Information Technology, Industrials and Materials** (G3 flippers) · news-axis tie-breaks · "the third run running" as a persistence argument |
| PREMORTEM | "the tape has gone quiet on this risk" — measured, **0 of 80** silent names were quiet |
| DEEP | the velocity axis as an axis · "no news flow" as evidence of anything |
| BET / SIZE | single-number concentration · `--ic`-backed size (→ **"mechanical ¼"**) · `AVGO/NVDA` and `ANET/ETN` unit counts |
| DRIFT | **must state whether `drift_watch`'s instrument answered, with the probe clock time.** An empty burst list today is not "no drift" |

**What this desk CAN speak with today (stated positively).**
① **Settled prices through 2026-08-14** — with **RS at fine grain** (G0 clean, fourth run running).
② **OBV level and state** — last bar complete by construction (weekend run).
③ **eqflow · breadth** — unweighted, so the 32-day-stale caps barely touch them; with the news axis
   down these carry more load, not less.
④ **`vol_surge` in both directions** — licensing the reading that 08-13 and 08-14 were both
   light-volume sessions (0.732 then 0.649 of the 20-day norm).
⑤ **FINRA short pressure · CFTC COT percentile positioning** — the US substitute for the
   investor-type feed. Context, never a trigger.
⑥ **FRED macro series** (`module_macro_us`, cite `[FRED]`) — **the only axis on this desk that can
   have moved since the prior run**, because it is not keyed to the equity session.
⑦ **Primary filings** (`module_disclosure_us` / `module_fundamentals_us`) and **margin history**.
⑧ **Per-name news velocity by hand probe** — 60% measured success, 0% false silence, provided the
   7d/30d counts **and the probe clock time** are on the same line as the claim.
⑨ ★ **`news_vectors.db` through 2026-08-15** — *restored today*, cursor un-stalled to 08-16T09:01.

**Speak with settled 08-14 prices, breadth, positioning, primary documents, FRED, and news counts you
fetched yourself with the clock time attached. Do not speak with the sweep's news axis, a single
concentration number, or the word "today" attached to any price-derived change.**

*Instrument state is not a market view — this document is not written into `handoff/` (HANDOVER only reads it).*
