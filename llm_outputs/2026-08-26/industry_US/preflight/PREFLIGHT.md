# PREFLIGHT — industry_US · 2026-08-26 (Phase −1, INSTRUMENT_CHECK)

> Measures whether today's instruments **work**, not whether they return an answer.
> No market view, no tickers-as-picks, no sizing (P4).
> ★ A FAIL is not a warning — it removes a **citation right** for this entire run.

Baseline snapshot read (PREFLIGHT runs before today's SWEEP):
`llm_outputs/2026-08-25/industry_US/SECTOR_FLOW_US.json` (asof 2026-08-25).

---

## Gate table

| # | Gate | Measured | Verdict |
|---|---|---|---|
| G1 | News axis alive | baseline `vel_coverage` **17.06%** (≈51/299) vs 80% bar; live probes **alive** (Nvidia 4483 / Nucor 34 / Marathon Petroleum 24 / Nasdaq Inc 6, `--days 7 --scope foreign`) | **FAIL** |
| G2 | Scoring-scale continuity | `n_axes` = **3** on 08-20, 08-21, 08-22, 08-23, 08-24, 08-25 — unchanged; `dropped_missing_axis` = 0 on all six | **PASS** |
| G3 | Who owns the sector sign | flipper list printed: **1 of 11** — Health Care (top1 `LLY`, wflow −0.035, eqflow +0.004, n=32) | **PASS** (list emitted) |
| G4 | Risk-unit stability | 250d → **11 units**; 500d → **10 units**; 750d → **10 units**. Groupings differ | **FAIL** |
| G5 | Universe covers holdings | 11 US book names, **0 outside** `us_top300` (n=300); universe file age **42 days** (bar ≤8) | **FAIL** (staleness leg) |
| G6 | Measurement accrual rate | `snapshot_estimates --status`: 18 files / 36 calendar days = **0.50/day**, **2.0× slower** than ideal (bar ≤1.5×) | **FAIL** |
| G7 | Tool liveness | 13 modules + 14 scripts probed; **26 exit 0**, 1 non-standard (`module_chart`) verified live by real invocation | **PASS** |

---

## G1 — News axis alive · **FAIL**
- **Command / source**: baseline `SECTOR_FLOW_US.json §scoring` →
  `{vel_axis: false, vel_coverage: 0.1706, n_axes: 3, scored: 299, dropped_missing_axis: 0}`.
  17.06% of the 299 scored names got a velocity reading; the axis was therefore excluded and every
  name was scored on 3 axes. Bar is 80%.
- **Falsification probe actually run** (this is the gate's whole point — pipe vs silence):
  `module_news_data fts search "<name>" --days 7 --count --scope foreign`, routed via the NEWS API tunnel
  → Nvidia **4483**, Nucor **34**, Marathon Petroleum **24**, Nasdaq Inc **6**.
- **Reading**: the news pipe is **alive right now and discriminating** — three orders of magnitude between
  the loudest and quietest probe. The baseline's 17.06% is therefore **NOT "there is no news"**; it is
  "the sweep could not count". The differing variable versus these single queries is the ~300-query burst.
- **Trend, not a one-off**: vel_coverage 16.4% (08-20) → 16.7% (08-21) → **0.0%** (08-22, 08-23, 08-24)
  → **17.1%** (08-25). Partial recovery off the zero floor, still **far** below the 80% bar on every
  recent run. Six consecutive runs below bar.
- 🚫 **Rights removed for this run**: cannot cite **theme freshness** or **news velocity** in any stage
  (MACRO, SWEEP, EVENT_ALPHA, ROTATION, PREMORTEM, DEEP, BET, ALPHA). Cannot rule any name or sector
  **"quiet"** — quiet was not measured, measurement failed. Any freshness tag in BET_SHEET §B must read
  `UNMEASURED (G1 FAIL)`, never `stale` or `cold`.
- ↳ Not removed: single-name news lookups done **by hand** in later stages stay legal — they are exactly
  the probe that passed. What is banned is the **sweep-derived velocity axis** and any cross-sectional
  freshness ranking built on it.

## G2 — Scoring-scale continuity · **PASS**
- `n_axes` = 3 on 2026-08-20, 08-21, 08-22, 08-23, 08-24, 08-25. `dropped_missing_axis` = 0 on every snapshot.
- Same axis count on both sides of every subtraction ⇒ Δflow arithmetic is scale-legal this run.
- ⚠ Conditional, and today it is a live risk: 08-25 recovered to 17.1% coverage from a 0.0% floor.
  If **today's** SWEEP crosses the internal velocity-axis threshold, `n_axes` becomes 4 and **Δflow against
  the 3-axis history becomes illegal**. SWEEP must re-read `§scoring.n_axes` before differencing anything.

## G3 — Who owns the sector sign · **PASS**
- Source: baseline `§sector_rotation[].top1_flips_sign`, 11 sectors evaluated.
- **Full flipper list (1 of 11)**:
  - **Health Care** — top1 `LLY`, sector wflow **−0.035**, eqflow **+0.004**, `wflow_ex_top1` flips sign, n=32.
    The cap-weighted sign of the whole sector is one company's; equal-weighted it is flat-to-positive.
- Ten sectors carry `top1_flips_sign: false`: Energy (XOM), Cons Disc (AMZN), Materials (LIN),
  Comm Svcs (GOOGL), Financials (BRK-B), Info Tech (NVDA), Cons Staples (WMT), Industrials (CAT),
  Real Estate (WELL), Utilities (NEE).
- 🚫 **Right removed**: Health Care may **not** be promoted or demoted on the weighted-flow bucket —
  its sign belongs to `LLY`. If HLTH is ranked in ROTATION §2 it must be ranked on `eqflow` and `breadth`,
  with the substitution stated inline.
- ↳ Note vs yesterday: the flipper **moved** (08-25 baseline flagged Consumer Staples/WMT; today's
  baseline flags Health Care/LLY). Flipper identity is not stable run-to-run — do not carry it from memory.

## G4 — Risk-unit stability · **FAIL**
- Ran all three windows (`risk_units.py --book --days 250 / 500 / 750`). Not one window.
- **250d → 11 units** (249 aligned trading days; ARI 0.3188; within-group resid corr +0.6038).
  `{028050, 316140}` merged into one unit; `ANET`, `ETN`, `AVGO`, `NVDA` each standalone.
- **500d → 10 units** (499 days; ARI 0.1899; within +0.5246). `{ANET, ETN}` merged; `{AVGO, NVDA}` merged;
  `028050` and `316140` split apart.
- **750d → 10 units** (749 days; ARI 0.3810; within +0.5149). Identical grouping to 500d.
- **The disagreement is structural, not cosmetic**: at 250d the book reads as *four* independent
  AI-complex risks; at 500/750d it reads as *two*. The concentration answer changes with the lookback.
- Threshold sensitivity is also severe at every window: dist 0.40–0.60 → 12 units; 0.85 → 6 units (250d).
  The chosen 0.65 sits on a slope, not a plateau.
- 🚫 **Right removed**: no concentration guard may be quoted as a single number. Every unit-count or
  concentration statement this run must carry its `--days` **on the same line** (e.g. "10 units @750d").
  A bare "the book holds N independent risks" fails EXIT.
- ↳ Also logged by the tool itself: one measured unit spans **two book theme labels** in every window
  (250d: KR-E&C/plant + KR-bank-holding; 500/750d: AI-compute-EPICENTER + AI-power/electrical),
  i.e. `MAX_THEME_PCT` counts as 2 what correlation measures as 1. Instrument note only; no repair here.
- ↳ Tool's own S5 warning stands: ARI (0.19–0.38) moves **opposite** to within-group fit at all three
  windows — membership is not to be trusted at face value even inside a single window.

## G5 — Universe covers holdings · **FAIL** (staleness leg)
- **Coverage leg — clean**: 11 US book names (`ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX`)
  checked against `data/us_universe/us_top300.csv` (n=300) → **0 outside the universe**.
  (The 2 KR book names `028050`, `316140` are out of US-universe scope by construction, not by defect.)
- **Freshness leg — fails**: `us_top300.csv` mtime **2026-07-15 = 42 days old**, bar ≤8 days.
  Market caps are stale ⇒ **the weights are stale**, and `wflow` is a cap-weighted number. Membership may
  also be stale (a name that entered or left the top 300 in 42 days is mis-listed).
- 🚫 **Right removed**: cap-weighted sector flow (`wflow`) may not be cited as a **current** weighting —
  it is weighted as of 2026-07-15. Where `wflow` and `eqflow` disagree this run, **`eqflow` is the citable
  one**; `wflow` may be reported only with the 42-day tag attached.
- ↳ Not removed: per-name flow/RS/OBV/short judgments on the 11 holdings remain legal — all 11 are covered.

## G6 — Measurement accrual rate · **FAIL**
- `snapshot_estimates.py --status`: **18 files across 36 calendar days** (2026-07-22 → 2026-08-26)
  ⇒ measured **0.50/day** vs ideal 1.0/day = **2.0× slower** (bar 1.5×).
- Gaps (days): `[5, 1, 1, 1, 1, 1, 1, 1]`, median 1, max 6. The 40-dated-sample target needs 22 more files:
  **~44 days away at measured rate**, not the 22 days a file-count reading implies (D16's trap verbatim).
- ↳ Improving but not passing: the last 8 accruals are daily (gap=1). The deficit is the July/early-August
  holes, which are permanent.
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
- **One non-standard entry point**: `module_chart --help` exits **1** — it has no `--help` flag by design
  (positional-arg CLI). Probed for real instead: `module_chart NVDA --read` → **exit 0**, full structural
  read returned (OBV slope, divergence, MA stack, Bollinger, RSI, turn verdict, trigger/stop).
  Treated as **live**; this gate measures liveness, not flag conformance. No right removed.

---

## What this run may NOT claim (consolidated)
1. **No news-velocity or theme-freshness citation anywhere**, and **no "quiet"/"no news" verdict** on any name or sector. (G1)
2. **No bare concentration number** — every unit count carries its `--days` on the same line. (G4)
3. **`wflow` is not a current weighting** — 42-day-old caps; prefer `eqflow` on disagreement, tag `wflow` when used. (G5)
4. **Health Care may not be promoted/demoted on the weighted-flow bucket** — substitute `eqflow`/`breadth` and say so. (G3)
5. **No IC-backed sizing language** — any fraction is "mechanical 1/4", explicitly unmeasured. (G6)
6. **SWEEP must re-read `§scoring.n_axes` before any Δflow subtraction** — a velocity-axis recovery today
   would silently make the 3-axis history non-comparable. (G2, conditional)

## Instrument notes (no repair attempted — rule 1)
- G1 remains the run-defining failure and it is **chronic** (6 consecutive runs below bar, 3 of them at zero).
  Today's discriminating fact repeats yesterday's: single queries answer with correct magnitude ordering
  while the ~300-query sweep measures 17% — the failure tracks **burst load**, not source silence.
- G3's flipper identity changed between consecutive baselines (STPL/WMT → HLTH/LLY). Flipper status is a
  per-run measurement; carrying it forward from memory would be a fabricated instrument reading.
- G4's cross-window disagreement and G5's 42-day universe are both **weighting-layer** defects: they move
  the same numbers (cap weights, correlation grouping) that concentration and rotation rest on.
- G6 is the only gate trending toward pass (8 straight daily accruals); the failure is now historical debt.
- Repairs are a human-approval item or `idle_probe`'s job, not this stage's.

## EXIT CHECK
- [x] All 7 gates carry PASS/FAIL/UNKNOWN **plus real numbers**. Zero blanks. Zero UNKNOWNs.
- [x] Every FAIL states the removed right as "cannot cite X today", not "be careful".
- [x] G1 ran the falsification probe (4 probes, 3 orders of magnitude apart) and did **not** write low coverage as "no news".
- [x] G3's flipper list is written out in full — 1 named, 10 explicitly false.
- [x] G4 ran all three windows (250/500/750) and reports three separate groupings.
- [x] `PREFLIGHT.md` exists before HANDOVER starts.

---

## ADDENDUM — `vs-yesterday` DIFF column (implements `D358-KR`, registered this morning)

> `D358-KR` (2026-08-26 `industry_kr`): *"PREFLIGHT re-measures every gate daily and writes a fresh
> authority table, but downstream prose is written by copying yesterday's phrasing, and an authority
> table has no field that says **this cell reversed**."* Prescription: carry a `vs-yesterday` column
> and render the removed-rights list as a DIFF. Executed here, same day it was registered.

| # | 08-25 verdict | 08-26 verdict | Verdict changed? | **Number / content changed?** |
|---|---|---|---|---|
| G1 | FAIL | FAIL | no | ⚠ **YES — the number inverted**: `vel_coverage` **0.0% → 17.06%**. Still far below bar, so the right stays removed, but *"the axis is fully dead"* is **no longer true** |
| G2 | PASS | PASS | no | no (n_axes 3 on both sides). ⚠ The conditional is now **live** rather than theoretical: a 0.0%→17.1% move means a further recovery could flip `n_axes` to 4 mid-run |
| G3 | PASS | PASS | no | 🚨 **YES — the FLIPPER MOVED.** 08-25 named **Consumer Staples (`WMT`)**; today names **Health Care (`LLY`)**. The STPL restriction is **LIFTED**; an equivalent HLTH restriction is **ATTACHED**. This is the second consecutive run in which the flipper changed identity |
| G4 | FAIL | FAIL | no | no — identical counts (11/10/10) and identical groupings to 08-25 |
| G5 | FAIL | FAIL | no | universe age **41d → 42d** (one day worse; same defect) |
| G6 | FAIL | FAIL | no | **2.1× → 2.0× slower** (improving); 17 files/35d → 18 files/36d |
| G7 | PASS | PASS | no | no — same 26 exit-0, same one non-standard entry point |

### Removed-rights list, rendered as a DIFF against 2026-08-25
- **UNCHANGED (5)**: no news-velocity/theme-freshness citation · no bare concentration number ·
  `wflow` not a current weighting · no IC-backed sizing language · G2 conditional on Δflow.
- **🔴 REMOVED from yesterday's list (1)**: *"Consumer Staples may not be promoted/demoted on the
  weighted-flow bucket."* **STPL is no longer a flipper — the restriction does not apply today.**
  ⚠ Yesterday's `STPL N+ → N` demotion was admissible *because* the flipper had moved off STPL; the
  same logic now runs the other way and STPL is a normally-rankable sector this run.
- **🟢 ADDED to today's list (1)**: **Health Care may not be promoted/demoted on the weighted-flow
  bucket** — substitute `eqflow`/`breadth` and say so inline.
- ⚠ **What a copy-forward would have produced**: the sentence *"the axis has been fully dead for
  four runs"* (true on 08-25, false today) and the sentence *"STPL's sign belongs to `WMT`"*
  (true on 08-25, false today). Both were available to be copied; both are wrong. That is exactly
  `D358-KR`'s failure mode, caught by the column rather than by a reader.
