# PREFLIGHT — industry_US · 2026-08-28 (Phase −1, INSTRUMENT_CHECK)

> Measures whether today's instruments **work**, not whether they return an answer.
> No market view, no tickers-as-picks, no sizing (P4).
> ★ A FAIL is not a warning — it removes a **citation right** for this entire run.

Baseline snapshot read (PREFLIGHT runs before today's SWEEP):
`llm_outputs/2026-08-27/industry_US/SECTOR_FLOW_US.json` (asof 2026-08-27, 1 day old).

---

## Gate table

| # | Gate | Measured | Verdict |
|---|---|---|---|
| G1 | News axis alive | baseline `vel_coverage` **16.72%** (50/299) vs 80% bar; live probes **alive and discriminating** (Nvidia 5161 / Eli Lilly 180 / Nucor 26 / Marathon Petroleum 23, `--days 7 --scope foreign`). Covered set = universe ranks **1–50 contiguous, zero gaps** — 4th consecutive reproduction | **FAIL** |
| G2 | Scoring-scale continuity | `n_axes` = **3** on all 7 snapshots 08-21→08-27; `dropped_missing_axis` = 0 on all | **PASS** |
| G3 | Who owns the sector sign | flipper list printed: **2 of 11** — Health Care (`LLY`), Energy (`XOM`) | **PASS** (list emitted) |
| G4 | Risk-unit stability | 250d → **11 units**; 500d → **10 units**; 750d → **10 units**. Groupings differ between 250d and 500/750d | **FAIL** |
| G5 | Universe covers holdings | 11 US book names, **0 outside** `us_top300` (n=300); universe file age **44 days** (bar ≤8) | **FAIL** (staleness leg) |
| G6 | Measurement accrual rate | `snapshot_estimates --status`: 19 files / 38 calendar days = **0.50/day**, **2.0× slower** than ideal (bar ≤1.5×) | **FAIL** |
| G7 | Tool liveness | 13 modules + 14 scripts probed; **26 exit 0**, 1 non-standard (`module_chart`) verified live by real invocation | **PASS** |

---

## G1 — News axis alive · **FAIL** (8th consecutive run below bar)

- **Command / source**: baseline `SECTOR_FLOW_US.json §scoring` →
  `{vel_axis: false, vel_coverage: 0.1672, n_axes: 3, scored: 299, dropped_missing_axis: 0}`. Bar 80%.

- **Falsification probe actually run** (pipe vs silence — the gate's whole point):
  `module_news_data fts search "<name>" --days 7 --count --scope foreign`, via the NEWS API tunnel →
  **Nvidia 5161 · Eli Lilly 180 · Nucor 26 · Marathon Petroleum 23**. Two orders of magnitude between
  loudest and quietest ⇒ the pipe is alive **and discriminating** right now. Low coverage is therefore
  **not** "no news" — it is "not counted".

- **Rank-prefix structure re-measured** (mapping the non-null-`velocity` tickers onto `us_top300` rank):

  | snapshot | covered | rank range | contiguous prefix? | gaps |
  |---|---|---|---|---|
  | 08-25 | 51 | 1–51 | **yes** | none |
  | 08-26 | 51 | 1–51 | **yes** | none |
  | 08-27 | 50 | 1–50 | **yes** | none |

  Overlap 08-27 ∩ 08-26 = **50/50**; 08-27 ∩ 08-25 = **50/50**. The sweep iterates names in
  market-cap-descending order, so the pipe answers the first ~50 calls of a run and then stops. This is
  a **hard stop at a call count**, not random thinning — random thinning cannot produce a gap-free
  rank prefix four days running with an identical name set.

  ⚠ **Priority note, carried forward per the 08-27 HANDOVER correction**: this is a **reproduction, not
  a discovery.** `R103` ("the 300-query SWEEP overloads the tunnel") was retracted on **2026-08-26** by
  `M947`, which measured the same contiguity. Today's measurement is the **4th** independent
  confirmation of settled desk doctrine. It is written here as a live re-measurement (rule 2: instrument
  state is measured every run, never copied), **not** as a new finding.

- **Trend**: 16.7% (08-20) → 16.7% (08-21) → **0.0% × 3** (08-22/23/24, snapshots frozen at asof 08-21) →
  17.1% (08-25) → 17.1% (08-26) → **16.7% (08-27)**. Eight consecutive runs below bar, three at zero.

- 🚫 **Rights removed for this run**: cannot cite **theme freshness** or **news velocity** in any stage
  (MACRO, SWEEP, EVENT_ALPHA, ROTATION, PREMORTEM, DEEP, BET, ALPHA). Cannot rule any name or sector
  **"quiet"** — quiet was not measured. Any freshness tag in `BET_SHEET §B` must read
  `UNMEASURED (G1 FAIL)`, never `stale` / `cold` / `quiet`.
- 🚫 **Second right removed** (from the prefix structure): the partial velocity subset may **not** be used
  as a **cross-sectional** comparison. Coverage is rank-ordered, so the 50 measured names are the 50
  largest caps and the 249 unmeasured are systematically smaller. A ranking built on the covered subset
  is a mega-cap-only ranking wearing a universe label.
- ↳ **Not removed**: single-name news lookups done **by hand** in later stages stay legal — that is
  exactly the probe that passed, and it passed for low-rank names (NUE #217, MPC #177 in the same file).

## G2 — Scoring-scale continuity · **PASS**
- `n_axes` = 3 on 2026-08-21, 08-22, 08-23, 08-24, 08-25, 08-26, 08-27. `dropped_missing_axis` = 0 on all seven.
- Same axis count on both sides of every subtraction ⇒ Δflow arithmetic is scale-legal against this history.
- ⚠ **Separate hazard measured in the same read, and it is not a scale problem**: the 08-22, 08-23 and
  08-24 snapshot files all carry `asof: 2026-08-21`. Three consecutive run-days wrote a **stale** snapshot.
  A Δflow computed across that band would difference a file against **itself** and return ~0, which reads
  as "nothing moved". SWEEP must check `§asof`, not just the filename date, before differencing.
- ⚠ Conditional stands: the axis switches on at `vel_coverage ≥ VEL_COVERAGE_MIN` (80%). Given G1's
  call-count cutoff at ~50, a mid-run flip to `n_axes = 4` requires the cutoff to disappear entirely,
  not merely to improve. SWEEP re-reads `§scoring.n_axes` before differencing anything.

## G3 — Who owns the sector sign · **PASS**
- Source: baseline `§sector_rotation[].top1_flips_sign`, 11 sectors evaluated.
- **Full flipper list (2 of 11)** — written out in full, per EXIT rule:
  - **Health Care** — top1 `LLY`; `wflow` **−0.033**, `wflow_ex_top1` **+0.038**, `eqflow` **+0.086**,
    n=32, breadth 0.06. One company drags the whole sector's weighted sign negative while both
    unweighted reads are **positive**.
  - **Energy** — top1 `XOM`; `wflow` **−0.091**, `wflow_ex_top1` **+0.140**, `eqflow` **+0.042**,
    n=16, breadth 0.00. Same shape, larger gap (0.231 between weighted and ex-top1).
- Nine sectors carry `top1_flips_sign: false`: Materials (LIN), Financials (BRK-B),
  Consumer Discretionary (AMZN), Info Tech (NVDA), Industrials (CAT), Comm Svcs (GOOGL),
  Consumer Staples (WMT), Real Estate (WELL), Utilities (NEE).
- 🚫 **Rights removed**: **Health Care and Energy may not be promoted or demoted on the weighted-flow
  bucket** (ROTATION §2). Each must be ranked on `eqflow` and `breadth` instead, with the substitution
  stated inline at the point of use.
- 🚨 Note the asymmetry this creates: **Health Care and Energy hold the only two positive `eqflow`
  readings in the entire 11-sector table** (+0.086, +0.042) while both print negative `wflow`. A naive
  weighted read would rank them mid-table-negative; they are the two sectors where the instrument is
  known to be wrong about the sign. This is the largest available instrument error today.
- ↳ Flipper identity is **not stable run-to-run** and must never be carried from memory:
  08-24 flagged Consumer Staples/`WMT`; 08-25 flagged Health Care/`LLY`; 08-26 flagged Consumer
  Discretionary + Materials + Energy; today flags Health Care + Energy. **Fourth consecutive change.**

## G4 — Risk-unit stability · **FAIL**
- Ran all three windows (`risk_units.py --book --days 250 / 500 / 750`). Not one window.
- **250d → 11 units** (249 aligned days; ARI 0.3188; within-group resid corr +0.6039; max resid corr +0.8501).
  `{028050, 316140}` merged; `{MPC, PSX}` merged; `ANET`, `ETN`, `AVGO`, `NVDA` each **standalone**.
- **500d → 10 units** (499 days; ARI 0.1899; within +0.5274; max +0.8468). `{ANET, ETN}` merged;
  `{AVGO, NVDA}` merged; `{MPC, PSX}` merged; `028050` and `316140` **split apart**.
- **750d → 10 units** (749 days; ARI 0.3810; within +0.5171; max +0.8235). Grouping **identical to 500d**.
- **The disagreement is structural**: at 250d the book reads as *four* independent AI-complex risks
  (ANET / ETN / AVGO / NVDA); at 500/750d it reads as *two* (`{ANET,ETN}`, `{AVGO,NVDA}`). The
  concentration answer is a function of the lookback, not of the book.
- Threshold sensitivity severe at all three windows: dist 0.40–0.60 → **12 units everywhere**;
  0.85 → 5 (250d) / 4 (500d) / 5 (750d). The chosen 0.65 sits on a slope, not a plateau.
- 🚫 **Right removed**: no concentration guard may be quoted as a single number. Every unit-count or
  concentration statement this run carries its `--days` **on the same line** (e.g. "10 units @750d").
  A bare "the book holds N independent risks" fails EXIT.
- ↳ Tool's own logs, carried as instrument notes (no repair here): one measured unit spans **two book
  theme labels** in every window (250d: KR-E&C/plant + KR-bank-holding; 500/750d: AI-compute-EPICENTER
  + AI-power/electrical) — `MAX_THEME_PCT` counts as 2 what correlation measures as 1. S5 warning stands:
  ARI (0.19–0.38) moves **opposite** to within-group fit at all three windows. Calendar-intersection loss
  is 22 days on each of the six US names at 250d, and KRW/USD local returns are mixed in the same matrix
  (common-FX factor injection possible). 250d also warns sample < 250 (short samples invent structure).

## G5 — Universe covers holdings · **FAIL** (staleness leg)
- **Coverage leg — clean**: 11 US book names (`ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX`)
  checked against `data/us_universe/us_top300.csv` (n=300) → **0 outside the universe**.
  (The 2 KR book names `028050`, `316140` are out of US-universe scope by construction, not by defect.)
- **Freshness leg — fails**: `us_top300.csv` mtime **2026-07-15 = 44 days old**, bar ≤8 days.
  Market caps are stale ⇒ **the weights are stale**, and `wflow` is a cap-weighted number. Membership may
  also be stale (a name that entered or left the top 300 in 44 days is mis-listed).
- 🚫 **Right removed**: cap-weighted sector flow (`wflow`) may not be cited as a **current** weighting —
  it is weighted as of 2026-07-15. Where `wflow` and `eqflow` disagree this run, **`eqflow` is the citable
  one**; `wflow` may be reported only with the 44-day tag attached.
- ★ **Compounding note (G5 × G1)**: the rank column of this same stale file is what determines which 50
  names the news axis reaches before the cutoff. The staleness corrupts *two* instruments, not one —
  the weights **and** the coverage frontier.
- ↳ Not removed: per-name flow/RS/OBV/short judgments on the 11 holdings remain legal — all 11 are covered.

## G6 — Measurement accrual rate · **FAIL**
- `snapshot_estimates.py --status`: **19 files across 38 calendar days** (2026-07-22 → 2026-08-28)
  ⇒ measured **0.50/day** vs ideal 1.0/day = **2.0× slower** (bar 1.5×).
- Gaps (days): `[1, 1, 1, 1, 1, 1, 1, 2]`, median 1, max 6. The 40-dated-sample target needs 21 more
  files: **~42 days away at measured rate**, not the 21 days a file-count reading implies (D16's trap).
- ✅ One thing did move: **today's file (2026-08-28) has already accrued** at PREFLIGHT time — unlike
  08-27, when the run read a window with nothing added since. The ratio is nonetheless **byte-identical
  at 2.0×**, because one file over one more calendar day is exactly the measured rate.
- 🚫 **Right removed**: `kelly_size --ic` output may **not** be reported as an evidence-backed size.
  Wherever a fraction appears this run it must be labelled **"mechanical 1/4 — IC not yet estimable (G6 FAIL)"**.
- ↳ Not repaired here (rule 1). Retroactive recovery is impossible; missed days are gone permanently.

## G7 — Tool liveness · **PASS**
- **Modules, `--help`, exit 0 (12/13)**: `module_macro_us` `module_news_data` `module_flow`
  `module_valuation` `module_business_us` `module_disclosure_us` `module_fundamentals_us`
  `module_industry_map` `module_watchlist` `module_report_tags` `module_paper_book` `module_epistemics`.
- **Scripts, `--help`, exit 0 (14/14)**: `sector_flow` `us_live_shortlist` `us_flow` `us_setup_screener`
  `catalyst_calendar` `cycle_exposure` `drift_watch` `risk_units` `kelly_size` `exposure_rule`
  `reject_ledger` `missed_ledger` `action_bracket` `report_lint`.
- **One non-standard entry point**: `module_chart --help` exits **1** — no `--help` flag by design
  (positional-arg CLI). Probed for real instead: `module_chart NVDA --read` → **exit 0**. Treated as
  **live**; this gate measures liveness, not flag conformance. No right removed.
- ⚠ Liveness ≠ correctness. G1 is the standing proof: `module_news_data --help` exits 0 and the module
  answers single queries, yet the axis it feeds is 16.7% covered. G7 passing removes no other gate's FAIL.

---

## What this run may NOT claim (consolidated)
1. **No news-velocity or theme-freshness citation anywhere**, and **no "quiet"/"no news" verdict** on any name or sector. (G1)
2. **No cross-sectional use of the partial velocity subset** — its coverage is a market-cap rank prefix (1–50), so it is a mega-cap-only sample. (G1)
3. **No bare concentration number** — every unit count carries its `--days` on the same line. (G4)
4. **`wflow` is not a current weighting** — 44-day-old caps; prefer `eqflow` on disagreement, tag `wflow` when used. (G5)
5. **Health Care and Energy may not be promoted/demoted on the weighted-flow bucket** — substitute `eqflow`/`breadth` and say so inline. (G3)
6. **No IC-backed sizing language** — any fraction is "mechanical 1/4", explicitly unmeasured. (G6)
7. **SWEEP must re-read `§scoring.n_axes` AND `§asof` before any Δflow subtraction** — three snapshots in the last week (08-22/23/24) carry a stale `asof`. (G2, conditional)

## Instrument notes (no repair attempted — rule 1)
- **G1's mechanism is settled, not new.** The ~50-call cutoff was established 2026-08-26 (`M947`, retiring
  `R103`) and has now reproduced four days running. What is worth recording is that it has **not moved**:
  no drift toward the bar, no widening, no recovery. Filed for `idle_probe` / human approval.
- **New this run (G2 side-finding)**: three consecutive snapshot files (08-22/23/24) carry `asof: 2026-08-21`.
  This is a *different* defect class from G1 — the file was written, dated by filename, and contained
  **yesterday's measurements**. A Δflow across it returns ~0 and reads as calm. Not a gate FAIL (n_axes
  is continuous, which is what G2 measures) but it belongs to the same family the preflight exists for:
  **a plausible number from a source that did not re-measure.**
- G3's flipper identity changed for the **fourth consecutive run** (STPL/WMT → HLTH/LLY → CD+MATR+ENRG →
  HLTH+ENRG). Copying it forward is a fabricated instrument reading. Note Health Care has now been a
  flipper in 2 of the last 4 runs and Energy in 2 of 4 — frequency, not stability.
- G4's cross-window disagreement and G5's 44-day universe are both **weighting-layer** defects: they move
  the same numbers (cap weights, correlation grouping) that concentration and rotation rest on.
- G6 accrued today's file but the rate is unchanged at 2.0×.

## EXIT CHECK
- [x] All 7 gates carry PASS/FAIL/UNKNOWN **plus real numbers**. Zero blanks. Zero UNKNOWNs.
- [x] Every FAIL states the removed right as "cannot cite X today", not "be careful".
- [x] G1 ran the falsification probe — 4 live CLI probes spanning two orders of magnitude, plus the
      rank-prefix mapping across three snapshots. Low coverage is **not** written as "no news".
- [x] G3's flipper list is written out in full — 2 named with numbers, 9 explicitly false.
- [x] G4 ran all three windows (250/500/750) and reports three separate groupings.
- [x] `PREFLIGHT.md` exists before HANDOVER starts.

---

## ADDENDUM — `vs-yesterday` DIFF column (`D358-KR`, third run under the rule)

| # | 08-27 verdict | 08-28 verdict | Verdict changed? | **Number / content changed?** |
|---|---|---|---|---|
| G1 | FAIL | FAIL | no | coverage 17.06% → **16.72%** (51 → 50 names). Prefix structure **identical in shape**, 4th reproduction. ⚠ Yesterday's file claimed the prefix finding was "★ New this run" and was corrected mid-run by HANDOVER; **this run does not repeat that claim** |
| G2 | PASS | PASS | no | n_axes 3 on both sides; history 7 snapshots. 🚨 **NEW side-finding**: 08-22/23/24 snapshots carry a **stale `asof` (2026-08-21)** — a Δflow across that band silently returns ~0 |
| G3 | PASS | PASS | no | 🚨 **YES — the flipper list changed again, and shrank 3 → 2.** 08-27 named **CD (`AMZN`) + Materials (`LIN`) + Energy (`XOM`)**; today names **Health Care (`LLY`) + Energy (`XOM`)**. CD and Materials restrictions **LIFTED**; Health Care **RE-ATTACHED** |
| G4 | FAIL | FAIL | no | counts identical (11/10/10) and groupings identical to 08-27. Third straight day of the same structural split |
| G5 | FAIL | FAIL | no | universe age **43d → 44d** (one day worse; same defect) |
| G6 | FAIL | FAIL | no | 18 files/36d → **19 files/38d**. Today's file **did** accrue (it had not on 08-27), but the ratio is **still exactly 2.0×** |
| G7 | PASS | PASS | no | same 26 exit-0, same one non-standard entry point (`module_chart`, verified live by real invocation) |

### Removed-rights list, rendered as a DIFF against 2026-08-27
- **UNCHANGED (6)**: no news-velocity/theme-freshness citation · no cross-sectional use of the partial
  velocity subset · no bare concentration number · `wflow` not a current weighting · no IC-backed
  sizing language · G2 conditional on Δflow.
- **🔴 REMOVED from yesterday's list (2)**: *"Consumer Discretionary may not be promoted/demoted on the
  weighted-flow bucket"* and the same for *"Materials"*. Both carry `top1_flips_sign: false` today
  (CD: `wflow` −0.153 / ex-top1 −0.020, same sign; Materials: `wflow` +0.012 / ex-top1 +0.080, same sign).
- **🟢 ADDED to today's list (1)**: **Health Care** may not be promoted/demoted on the weighted-flow
  bucket — and it matters more than usual today, because HLTH holds the table's **largest positive
  `eqflow` (+0.086)** while printing a negative `wflow`.
- **🟢 STRENGTHENED (1)**: the G2 conditional now names a *measured* failure mode (stale `asof`), not a
  hypothetical one. SWEEP must check `§asof`, not the filename.
- ⚠ **What a copy-forward would have produced today**: *"the flippers are CD, Materials and Energy"*
  (true 08-27, half-false today — and it would have left Health Care's sign error uncaught while
  needlessly restricting two clean sectors), and *"today's snapshot has not accrued yet"* (true 08-27,
  false today). `D358-KR`'s failure mode caught by the column for the third run running.
