# PREFLIGHT — industry_US · 2026-08-25 (Phase −1, INSTRUMENT_CHECK)

> Measures whether today's instruments **work**, not whether they return an answer.
> No market view, no tickers-as-picks, no sizing (P4).
> ★ A FAIL is not a warning — it removes a **citation right** for this entire run.

Baseline snapshot read (PREFLIGHT runs before today's SWEEP): `llm_outputs/2026-08-24/industry_US/SECTOR_FLOW_US.json` (asof 2026-08-21).

---

## Gate table

| # | Gate | Measured | Verdict |
|---|---|---|---|
| G1 | News axis alive | sweep `vel_coverage` **0.0%** (0/299) vs 80% bar; live probes **alive** (Nvidia 4137 / Nucor 27 / Marathon Petroleum 25 / Nasdaq Inc 6, `--days 7 --scope foreign`) | **FAIL** |
| G2 | Scoring-scale continuity | `n_axes` = **3** on 08-20, 08-21, 08-22, 08-23, 08-24 — unchanged | **PASS** |
| G3 | Who owns the sector sign | flipper list printed: **1 of 11** — Consumer Staples (top1 `WMT`, wflow −0.013, n=19) | **PASS** (list emitted) |
| G4 | Risk-unit stability | 250d → **11 units**; 500d → **10 units**; 750d → **10 units**. Groupings differ | **FAIL** |
| G5 | Universe covers holdings | 11 US book names, **0 outside** `us_top300`; universe file age **41 days** (bar ≤8) | **FAIL** (staleness leg) |
| G6 | Measurement accrual rate | `snapshot_estimates --status`: 17 files / 35 calendar days = **0.49/day**, **2.1× slower** than ideal (bar ≤1.5×) | **FAIL** |
| G7 | Tool liveness | 13 modules + 14 scripts probed; **26 exit 0**, 1 non-standard (`module_chart`) verified live by real invocation | **PASS** |

---

## G1 — News axis alive · **FAIL**
- **Command / source**: `SECTOR_FLOW_US.json §scoring` → `{vel_axis: false, vel_coverage: 0.0, n_axes: 3, scored: 299, dropped_missing_axis: 0}`.
  Sweep log (`_sweep2.log`): velocity measured 0/299 = 0.0% → velocity axis excluded (all names scored on 3 axes).
- **Falsification probe actually run** (this is the gate's whole point — pipe vs silence):
  `module_news_data fts search "<name>" --days 7 --count --scope foreign`
  → Nvidia **4137**, Nucor **27**, Marathon Petroleum **25**, Nasdaq Inc **6**. Routed via the NEWS API tunnel.
- **Reading**: the news pipe is **alive right now and discriminating** (three orders of magnitude between
  a loud name and a quiet one). Therefore the sweep's 0.0% is **NOT "there is no news"** — it is
  "the sweep could not count". The 300-query burst is the differing variable versus these single queries.
- **Trend, not a one-off**: vel_coverage 16.4% (08-20) → 16.7% (08-21) → **0.0%** (08-22, 08-23, 08-24) → 0.0% baseline today.
  The axis has been below the 80% bar on **every** recent run; it has been fully dead for four.
- 🚫 **Rights removed for this run**: cannot cite **theme freshness** or **news velocity** in any stage
  (MACRO, SWEEP, EVENT_ALPHA, ROTATION, DEEP, BET, ALPHA). Cannot rule any name or sector **"quiet"** —
  we did not measure quiet, we failed to measure. Any freshness tag in BET_SHEET §B must be written as
  `UNMEASURED (G1 FAIL)`, never as `stale` or `cold`.
- ↳ Note: single-name news lookups done **by hand** in later stages remain legal (they are the probe that
  passed). What is banned is the **sweep-derived velocity axis** and any cross-sectional freshness ranking built on it.

## G2 — Scoring-scale continuity · **PASS**
- `n_axes` = 3 on 2026-08-20, 08-21, 08-22, 08-23, 08-24. `dropped_missing_axis` = 0 on every snapshot.
- Same axis count on both sides of every subtraction ⇒ Δflow arithmetic is scale-legal this run.
- ⚠ Conditional: it is legal **because the axis has been consistently absent**, not because it is healthy.
  If today's SWEEP recovers velocity coverage ≥80%, `n_axes` becomes 4 and **Δflow against the 3-axis
  history becomes illegal** — SWEEP must re-check this line before differencing.

## G3 — Who owns the sector sign · **PASS**
- Source: `§sector_rotation[].top1_flips_sign`, 11 sectors evaluated.
- **Full flipper list (1 of 11)**:
  - **Consumer Staples** — top1 `WMT`, sector wflow −0.013, `wflow_ex_top1` flips sign, n=19.
- Ten sectors carry `top1_flips_sign: false` (Health Care, Info Tech, Comm Svcs, Energy, Financials,
  Industrials, Cons Disc, Materials, Utilities, Real Estate).
- 🚫 **Right removed**: Consumer Staples may **not** be promoted or demoted on the weighted-flow bucket —
  its sign belongs to one company. If STPL is ranked at all in ROTATION §2 it must be ranked on `eqflow`
  and `breadth`, with the substitution stated inline.

## G4 — Risk-unit stability · **FAIL**
- Ran all three windows (`risk_units.py --book --days 250 / 500 / 750`). Not one window.
- **250d → 11 units.** `{028050, 316140}` merged into one unit; `ANET`, `ETN`, `AVGO`, `NVDA` each standalone.
- **500d → 10 units.** `{ANET, ETN}` merged; `{AVGO, NVDA}` merged; `028050` and `316140` split apart.
- **750d → 10 units.** Identical grouping to 500d.
- **The disagreement is structural, not cosmetic**: at 250d the book reads as *four* independent
  AI-complex risks; at 500/750d it reads as *two*. The concentration answer changes with the lookback.
- 🚫 **Right removed**: no concentration guard may be quoted as a single number. Every unit-count or
  concentration statement in this run must carry its `--days` **on the same line**
  (e.g. "10 units @750d"). A bare "the book holds N independent risks" fails EXIT.
- ↳ Also logged by the tool itself: one measured unit spans **two book theme labels**
  (250d: KR-E&C/plant + KR-bank-holding; 500/750d: AI-compute-EPICENTER + AI-power/electrical),
  i.e. `MAX_THEME_PCT` counts as 2 what correlation measures as 1. Instrument note only; no repair here.

## G5 — Universe covers holdings · **FAIL** (staleness leg)
- **Coverage leg — clean**: 11 US book names (`ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX`)
  checked against `data/us_universe/us_top300.csv` → **0 outside the universe**.
  (The 2 KR book names `028050`, `316140` are out of scope for the US universe by construction, not by defect.)
- **Freshness leg — fails**: `us_top300.csv` mtime **2026-07-15 = 41 days old**, bar is ≤8 days.
  The sweep logs the same warning: market caps are stale ⇒ **the weights are stale**, and `wflow` is a
  cap-weighted number. Membership may also be stale (a name that entered or left the top 300 in 41 days is mis-listed).
- 🚫 **Right removed**: cap-weighted sector flow (`wflow`) may not be cited as a **current** weighting —
  it is weighted as of 2026-07-15. Where `wflow` and `eqflow` disagree this run, **`eqflow` is the citable
  one**; `wflow` may be reported only with the 41-day tag attached.
- ↳ Not removed: per-name flow/RS/OBV/short judgments on the 11 holdings remain legal — all 11 are covered.

## G6 — Measurement accrual rate · **FAIL**
- `snapshot_estimates.py --status`: **17 files across 35 calendar days** (2026-07-22 → 2026-08-25)
  ⇒ measured **0.49/day** vs ideal 1.0/day = **2.1× slower** (bar 1.5×).
- Gaps (days): `[1, 5, 1, 1, 1, 1, 1, 1]`, median 1, max 6. The 40-dated-sample target is
  **~47 days away at measured rate**, not the 23 days a file-count reading implies (D16's trap verbatim).
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
  (positional-arg CLI; it prints usage). Probed for real instead: `module_chart NVDA --read` → **exit 0**,
  full structural read returned (OBV slope, divergence, MA stack, Bollinger, RSI, turn verdict, trigger/stop).
  Treated as **live**; this gate measures liveness, not flag conformance. No right removed.

---

## What this run may NOT claim (consolidated)
1. **No news-velocity or theme-freshness citation anywhere**, and **no "quiet"/"no news" verdict** on any name or sector. (G1)
2. **No bare concentration number** — every unit count carries its `--days` on the same line. (G4)
3. **`wflow` is not a current weighting** — 41-day-old caps; prefer `eqflow` on disagreement, tag `wflow` when used. (G5)
4. **Consumer Staples may not be promoted/demoted on the weighted-flow bucket** — substitute `eqflow`/`breadth` and say so. (G3)
5. **No IC-backed sizing language** — any fraction is "mechanical 1/4", explicitly unmeasured. (G6)

## Instrument notes (no repair attempted — rule 1)
- G1 is the run-defining failure and it is **chronic** (≥5 runs below bar, 4 at zero). The discriminating
  fact recorded today: single queries answer with correct magnitude ordering while the 300-query sweep
  measures zero — the failure tracks **burst load**, not source silence.
- G4's cross-window disagreement and G5's 41-day universe are both **weighting-layer** defects: they move
  the same numbers (cap weights, correlation grouping) that concentration and rotation rest on.
- Repairs are a human-approval item or `idle_probe`'s job, not this stage's.

## EXIT CHECK
- [x] All 7 gates carry PASS/FAIL/UNKNOWN **plus real numbers**. Zero blanks. Zero UNKNOWNs.
- [x] Every FAIL states the removed right as "cannot cite X today", not "be careful".
- [x] G1 ran the falsification probe (4 probes, 3 orders of magnitude apart) and did **not** write low coverage as "no news".
- [x] G3's flipper list is written out in full — 1 named, 10 explicitly false.
- [x] G4 ran all three windows (250/500/750) and reports three separate groupings.
- [x] `PREFLIGHT.md` exists before HANDOVER starts.
