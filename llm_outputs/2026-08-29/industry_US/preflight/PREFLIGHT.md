# PREFLIGHT — industry_US · 2026-08-29 (Phase −1, INSTRUMENT_CHECK)

> Measures whether today's instruments **work**, not whether they return an answer.
> No market view, no tickers-as-picks, no sizing (P4).
> ★ A FAIL is not a warning — it removes a **citation right** for this entire run.

Baseline snapshot read (PREFLIGHT runs before today's SWEEP):
`llm_outputs/2026-08-28/industry_US/SECTOR_FLOW_US.json` — `asof: 2026-08-28`, **1 day old, asof matches
its filename date** (the 08-22/23/24 stale-`asof` defect is not present in this baseline).

---

## Gate table

| # | Gate | Measured | Verdict |
|---|---|---|---|
| G1 | News axis alive | baseline `vel_coverage` **16.72%** (50/299) vs 80% bar; live probes **alive and discriminating** (Nvidia 5353 / Eli Lilly 191 / Nucor 23 / Marathon Petroleum 19, `--days 7 --scope foreign`). Covered set = universe ranks **1–50 contiguous, zero gaps** — 5th consecutive reproduction | **FAIL** |
| G2 | Scoring-scale continuity | `n_axes` = **3** on all 10 snapshots 08-19→08-28; `dropped_missing_axis` = 0 on all | **PASS** |
| G3 | Who owns the sector sign | flipper list printed: **2 of 11** — Information Technology (`NVDA`), Health Care (`LLY`) | **PASS** (list emitted) |
| G4 | Risk-unit stability | 250d → **11 units**; 500d → **10 units**; 750d → **10 units**. Groupings differ between 250d and 500/750d | **FAIL** |
| G5 | Universe covers holdings | 11 US book names, **0 outside** `us_top300` (n=300); universe file age **45 days** (bar ≤8) | **FAIL** (staleness leg) |
| G6 | Measurement accrual rate | `snapshot_estimates --status`: 19 files / 38 calendar days = **0.50/day**, **2.0× slower** than ideal (bar ≤1.5×); **no file accrued for 2026-08-29 at PREFLIGHT time** | **FAIL** |
| G7 | Tool liveness | 13 modules + 14 scripts probed; **26 exit 0**, 1 non-standard (`module_chart`) verified live by real invocation | **PASS** |

---

## G1 — News axis alive · **FAIL** (9th consecutive run below bar)

- **Command / source**: baseline `SECTOR_FLOW_US.json §scoring` →
  `{vel_axis: false, vel_coverage: 0.1672, n_axes: 3, scored: 299, dropped_missing_axis: 0}`. Bar 80%.

- **Falsification probe actually run** (pipe vs silence — the gate's whole point):
  `module_news_data fts search "<name>" --days 7 --count --scope foreign`, routed through the NEWS API
  tunnel → **Nvidia 5353 · Eli Lilly 191 · Nucor 23 · Marathon Petroleum 19**. Two orders of magnitude
  between loudest and quietest ⇒ the pipe is alive **and discriminating right now**. Low coverage is
  therefore **not** "no news" — it is "not counted". Two of the four probes (NUE rank #217, MPC #177)
  sit far below the coverage frontier and still answered.

- **Rank-prefix structure re-measured** (mapping non-null-`velocity` tickers onto `us_top300` rank):

  | snapshot | covered | rank range | contiguous prefix? | gaps | overlap w/ prev |
  |---|---|---|---|---|---|
  | 08-25 | 51 | 1–51 | **yes** | 0 | — |
  | 08-26 | 51 | 1–51 | **yes** | 0 | 51/51 |
  | 08-27 | 50 | 1–50 | **yes** | 0 | 50/50 |
  | 08-28 | 50 | 1–50 | **yes** | 0 | 50/50 |

  The sweep iterates names in market-cap-descending order, answers the first ~50 calls of a run, then
  stops. A **hard stop at a call count**, not random thinning — random thinning cannot produce a
  gap-free rank prefix five days running with an identical name set.

- ⚠ **Priority note (carried per the 08-27 HANDOVER correction)**: this is a **reproduction, not a
  discovery.** `R103` ("the 300-query SWEEP overloads the tunnel") was retracted 2026-08-26 by `M947`,
  which measured the same contiguity. Today is the **5th** independent confirmation of settled desk
  doctrine, re-measured because rule 2 forbids copying instrument state — **not** a new finding.

- **Trend**: 17.06% (08-19) → 16.39% (08-20) → 16.72% (08-21) → **0.0% × 3** (08-22/23/24, snapshots
  frozen at `asof 2026-08-21`) → 17.06% (08-25) → 17.06% (08-26) → 16.72% (08-27) → **16.72% (08-28)**.
  Nine consecutive runs below bar, three at zero. **No drift toward the bar in either direction.**

- 🚫 **Rights removed for this run**: cannot cite **theme freshness** or **news velocity** in any stage
  (MACRO, SWEEP, EVENT_ALPHA, ROTATION, PREMORTEM, DEEP, BET, ALPHA). Cannot rule any name or sector
  **"quiet"** — quiet was not measured. Any freshness tag in `BET_SHEET §B` must read
  `UNMEASURED (G1 FAIL)`, never `stale` / `cold` / `quiet`.
- 🚫 **Second right removed** (from the prefix structure): the partial velocity subset may **not** be
  used as a **cross-sectional** comparison. Coverage is rank-ordered, so the 50 measured names are the
  50 largest caps and the 249 unmeasured are systematically smaller. A ranking built on the covered
  subset is a mega-cap-only ranking wearing a universe label.
- ↳ **Not removed**: single-name news lookups done **by hand** in later stages stay legal — that is
  exactly the probe that passed, and it passed for two low-rank names in the same file.

## G2 — Scoring-scale continuity · **PASS**
- `n_axes` = 3 on 2026-08-19, 08-20, 08-21, 08-22, 08-23, 08-24, 08-25, 08-26, 08-27, 08-28 (ten
  snapshots). `dropped_missing_axis` = 0 on all ten.
- Same axis count on both sides of every subtraction ⇒ Δflow arithmetic is scale-legal against this history.
- ✅ **The stale-`asof` hazard logged on 08-28 does not affect today's baseline**: 08-25 → 08-28 each
  carry an `asof` equal to their own filename date. The defective band is 08-22/23/24 only (all three
  `asof: 2026-08-21`). A Δflow crossing that band would difference a file against **itself** and return
  ~0, which reads as "nothing moved". **SWEEP must check `§asof`, not the filename**, if it reaches back
  more than four snapshots.
- ⚠ Conditional stands: the axis switches on at `vel_coverage ≥ VEL_COVERAGE_MIN` (80%). Given G1's
  call-count cutoff at ~50, a mid-run flip to `n_axes = 4` requires the cutoff to disappear entirely,
  not merely to improve. SWEEP re-reads `§scoring.n_axes` before differencing anything.

## G3 — Who owns the sector sign · **PASS**
- Source: baseline `§sector_rotation[].top1_flips_sign`, 11 sectors evaluated.
- **Full flipper list (2 of 11)** — written out in full, per EXIT rule:
  - **Information Technology** — top1 `NVDA`; `wflow` **+0.035**, `wflow_ex_top1` **−0.042**,
    `eqflow` **−0.029**, n=56, breadth 0.04. One company is the **only reason the sector's weighted
    sign is positive**; both unweighted reads are negative.
  - **Health Care** — top1 `LLY`; `wflow` **−0.046**, `wflow_ex_top1` **+0.023**, `eqflow` **+0.057**,
    n=32, breadth 0.06. Opposite shape: one company drags the weighted sign negative while both
    unweighted reads are positive.
- Nine sectors carry `top1_flips_sign: false`: Materials (LIN), Financials (BRK-B), Energy (XOM),
  Industrials (CAT), Real Estate (WELL), Consumer Staples (WMT), Consumer Discretionary (AMZN),
  Utilities (NEE), Communication Services (GOOGL).
- 🚫 **Rights removed**: **Information Technology and Health Care may not be promoted or demoted on the
  weighted-flow bucket** (ROTATION §2). Each must be ranked on `eqflow` and `breadth` instead, with the
  substitution stated inline at the point of use.
- 🚨 **This is today's largest available instrument error, and it points at the desk's own epicentre.**
  IT is the **only sector with a positive `wflow` besides Materials**, and that positivity is `NVDA`
  alone — ex-top1 it is negative, and equal-weighted it is negative. Health Care holds the table's
  **largest positive `eqflow` (+0.057)** while printing a negative `wflow`. A naive weighted read would
  rank IT top-half-positive and Health Care mid-table-negative; those are the two sectors where the
  instrument is known to be wrong about the sign.
- ↳ Flipper identity is **not stable run-to-run** and must never be carried from memory:
  08-24 STPL/`WMT` → 08-25 HLTH/`LLY` → 08-26 CD+MATR+ENRG → 08-27 CD+MATR+ENRG → 08-28 HLTH+ENRG →
  **today IT+HLTH**. Health Care is now a flipper in **3 of the last 6** runs; IT is a flipper for the
  **first time in this window**.

## G4 — Risk-unit stability · **FAIL**
- Ran all three windows (`risk_units.py --book --days 250 / 500 / 750`). Not one window.
- **250d → 11 units** (max resid corr **+0.8501**; within-group +0.6039 vs between +0.0071; ARI **0.3188**).
  `{028050, 316140}` merged; `{MPC, PSX}` merged; `ANET`, `ETN`, `AVGO`, `NVDA` each **standalone**.
- **500d → 10 units** (max **+0.8468**; within +0.5274 vs between +0.0175; ARI **0.1899**).
  `{ANET, ETN}` merged; `{AVGO, NVDA}` merged; `{MPC, PSX}` merged; `028050` and `316140` **split apart**.
- **750d → 10 units** (max **+0.8235**; within +0.5171 vs between +0.0194; ARI **0.3810**).
  Grouping **identical to 500d**.
- **The disagreement is structural, and it is about the book's own concentration**: at 250d the book
  reads as *four* independent AI-complex risks (ANET / ETN / AVGO / NVDA); at 500/750d it reads as
  *two* (`{ANET,ETN}`, `{AVGO,NVDA}`). The concentration answer is a function of the lookback, not of
  the book. **Fourth consecutive run with this identical split.**
- Threshold sensitivity severe at all three windows: dist 0.40–0.60 → **12 units everywhere**;
  0.85 → 5 (250d) / 4 (500d) / 5 (750d). The chosen 0.65 sits on a slope, not a plateau.
- 🚫 **Right removed**: no concentration guard may be quoted as a single number. Every unit-count or
  concentration statement this run carries its `--days` **on the same line** (e.g. "10 units @750d").
  A bare "the book holds N independent risks" fails EXIT.
- ↳ Tool's own logs, carried as instrument notes (no repair here): one measured unit spans **two book
  theme labels** in every window (250d: KR-E&C/plant + KR-bank-holding; 500/750d: AI-compute-EPICENTER
  + AI-power/electrical) — `MAX_THEME_PCT` counts as 2 what correlation measures as 1. S5 warning
  stands: ARI (0.19–0.38) moves **opposite** to within-group fit at all three windows.
  Calendar-intersection loss is **21 days** on each of the six long-history names at 250d (48d at 500d,
  66d at 750d), and KRW/USD local returns share one matrix (common-FX factor injection possible).
  Intersection holes >4 days: 2 @250d, 5 @500d, 8 @750d (max 8 days each).

## G5 — Universe covers holdings · **FAIL** (staleness leg)
- **Coverage leg — clean**: 11 US book names (`ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX`)
  checked against `data/us_universe/us_top300.csv` (n=300) → **0 outside the universe**.
  (The 2 KR book names `028050`, `316140` are out of US-universe scope by construction, not by defect.)
- **Freshness leg — fails**: `us_top300.csv` mtime **2026-07-15 18:04 = 45 days old**, bar ≤8 days.
  Market caps are stale ⇒ **the weights are stale**, and `wflow` is a cap-weighted number. Membership
  may also be stale (a name that entered or left the top 300 in 45 days is mis-listed).
- 🚫 **Right removed**: cap-weighted sector flow (`wflow`) may not be cited as a **current** weighting —
  it is weighted as of 2026-07-15. Where `wflow` and `eqflow` disagree this run, **`eqflow` is the
  citable one**; `wflow` may be reported only with the 45-day tag attached.
- ★ **Compounding note (G5 × G1 × G3)**: the rank column of this same stale file determines which 50
  names the news axis reaches before the cutoff **and** which name is each sector's `top1`. The
  staleness corrupts *three* readings, not one — the weights, the coverage frontier, and the identity
  of the company that owns each sector's sign.
- ↳ Not removed: per-name flow/RS/OBV/short judgments on the 11 holdings remain legal — all 11 covered.
- ↳ A candidate replacement exists on disk (`us_all_v2_candidate.csv`, mtime 2026-08-10, 19 days) but
  is **not** what the scripts read. Swapping it is a human-approval item, not this stage's job (rule 1).

## G6 — Measurement accrual rate · **FAIL**
- `snapshot_estimates.py --status`: **19 files across 38 calendar days** (2026-07-22 → 2026-08-28)
  ⇒ measured **0.50/day** vs ideal 1.0/day = **2.0× slower** (bar 1.5×).
- Gaps (days): `[1, 1, 1, 1, 1, 1, 1, 2]`, median 1, max 6. The 40-dated-sample target needs 21 more
  files: **~42 days away at measured rate**, not the 21 days a file-count reading implies (D16's trap).
- ⚠ **Regression vs 08-28**: yesterday's run could record "today's file has already accrued at PREFLIGHT
  time". **Today's has not** — the newest file is dated 2026-08-28, one day behind. The headline ratio
  is byte-identical at 2.0× because the window grew by one day and one file simultaneously *yesterday*;
  today it has grown by one day and **zero** files. The next status read will show the ratio worsen
  unless a file lands.
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
  (positional-arg CLI). Probed for real instead: `module_chart NVDA --read` → **exit 0**, four
  indicator lines returned. Treated as **live**; this gate measures liveness, not flag conformance.
  No right removed.
- ⚠ Liveness ≠ correctness. G1 is the standing proof: `module_news_data --help` exits 0 and the module
  answers single queries, yet the axis it feeds is 16.7% covered. G7 passing removes no other gate's FAIL.
- ⚠ Second liveness-≠-correctness instance found in the same probe: `module_chart NVDA --read` returned
  exit 0 with **`nan` in three of its five fields** (Bollinger width, RSI, 20d momentum). The tool is
  live; part of its output is not a number. Any later stage quoting `module_chart` must read the
  actual field, not assume a number arrived because the command succeeded.

---

## What this run may NOT claim (consolidated)
1. **No news-velocity or theme-freshness citation anywhere**, and **no "quiet"/"no news" verdict** on any name or sector. (G1)
2. **No cross-sectional use of the partial velocity subset** — its coverage is a market-cap rank prefix (1–50), so it is a mega-cap-only sample. (G1)
3. **No bare concentration number** — every unit count carries its `--days` on the same line. (G4)
4. **`wflow` is not a current weighting** — 45-day-old caps; prefer `eqflow` on disagreement, tag `wflow` when used. (G5)
5. **Information Technology and Health Care may not be promoted/demoted on the weighted-flow bucket** — substitute `eqflow`/`breadth` and say so inline. (G3)
6. **No IC-backed sizing language** — any fraction is "mechanical 1/4", explicitly unmeasured. (G6)
7. **A `module_chart` field is not a number because the command exited 0** — read the field. (G7 note)
8. **SWEEP checks `§scoring.n_axes` AND `§asof` before any Δflow subtraction** — the 08-22/23/24 band carries a stale `asof`. Today's baseline is clean. (G2, conditional)

## Instrument notes (no repair attempted — rule 1)
- **G1's mechanism is settled, not new.** The ~50-call cutoff was established 2026-08-26 (`M947`,
  retiring `R103`) and has now reproduced five days running. What is worth recording is that it has
  **not moved**: no drift toward the bar, no widening, no recovery. Filed for `idle_probe` / human approval.
- **G3's flipper set moved onto the desk's epicentre for the first time in this window.** IT/`NVDA` has
  never appeared as a flipper in the 08-24→08-28 band; it does today, and the direction matters — it is
  the flip that would make IT *look positive*. Copying yesterday's list (HLTH+ENRG) would have left this
  uncaught while needlessly restricting Energy.
- **G4's cross-window disagreement and G5's 45-day universe are the same defect family**: both move the
  weighting layer (cap weights, correlation grouping) that concentration and rotation rest on. G5 now
  also feeds G3 — the stale rank column decides which company is each sector's `top1`.
- **G6 did not accrue today.** The 2.0× headline is unchanged only by coincidence of arithmetic.

## EXIT CHECK
- [x] All 7 gates carry PASS/FAIL/UNKNOWN **plus real numbers**. Zero blanks. Zero UNKNOWNs.
- [x] Every FAIL states the removed right as "cannot cite X today", not "be careful".
- [x] G1 ran the falsification probe — 4 live CLI probes spanning >2 orders of magnitude (5353 → 19),
      two of them below the coverage frontier, plus the rank-prefix mapping across four snapshots.
      Low coverage is **not** written as "no news".
- [x] G3's flipper list is written out in full — 2 named with numbers, 9 explicitly false and named.
- [x] G4 ran all three windows (250/500/750) and reports three separate groupings.
- [x] `PREFLIGHT.md` exists before HANDOVER starts.

---

## ADDENDUM — `vs-yesterday` DIFF column (`D358-KR`, fourth run under the rule)

| # | 08-28 verdict | 08-29 verdict | Verdict changed? | **Number / content changed?** |
|---|---|---|---|---|
| G1 | FAIL | FAIL | no | coverage **16.72% → 16.72%** (50/299, identical). Prefix structure identical in shape, **5th** reproduction. Probe counts moved (Nvidia 5161→**5353**, LLY 180→**191**, NUE 26→**23**, MPC 23→**19**) — the pipe is live and its counts change, which is itself the evidence it is not frozen |
| G2 | PASS | PASS | no | n_axes 3 on both sides; history extended to **10** snapshots (08-19→08-28). ✅ The stale-`asof` band flagged yesterday is **behind** today's baseline — 08-25→08-28 all carry self-consistent `asof` |
| G3 | PASS | PASS | no | 🚨 **YES — flipper list changed for the 5th consecutive run.** 08-28 named **HLTH (`LLY`) + Energy (`XOM`)**; today names **IT (`NVDA`) + HLTH (`LLY`)**. Energy restriction **LIFTED**; **IT restriction NEWLY ATTACHED** |
| G4 | FAIL | FAIL | no | counts identical (11/10/10), groupings identical to 08-27 and 08-28. **Fourth** straight day of the same structural split. Calendar-loss figure re-measured: 21d @250d (was reported 22d on 08-28) |
| G5 | FAIL | FAIL | no | universe age **44d → 45d** (one day worse; same defect). Coverage leg still clean (0 outside) |
| G6 | FAIL | FAIL | no | 19 files/38d on **both** days — but yesterday that included a same-day accrual and today it does **not**. Ratio flat at 2.0× by arithmetic coincidence, not by health |
| G7 | PASS | PASS | no | same 26 exit-0, same one non-standard entry point. 🚨 **NEW**: the `module_chart` real invocation returned exit 0 with **`nan` in 3 of 5 fields** — logged as a liveness-≠-correctness instance, no right removed |

### Removed-rights list, rendered as a DIFF against 2026-08-28
- **UNCHANGED (6)**: no news-velocity/theme-freshness citation · no cross-sectional use of the partial
  velocity subset · no bare concentration number · `wflow` not a current weighting · no IC-backed
  sizing language · G2 conditional on Δflow.
- **🔴 REMOVED from yesterday's list (1)**: *"Energy may not be promoted/demoted on the weighted-flow
  bucket"* — `XOM` carries `top1_flips_sign: false` today (`wflow` −0.205 / ex-top1 −0.045 / eqflow
  −0.093, all negative, same sign).
- **🟢 ADDED to today's list (1)**: **Information Technology** may not be promoted/demoted on the
  weighted-flow bucket — and it is the highest-consequence addition of the window, because IT's
  `wflow` (+0.035) is the **only** positive weighted reading outside Materials, it is positive
  **solely because of `NVDA`**, and both unweighted reads are negative (ex-top1 −0.042, eqflow −0.029).
- **🟢 STRENGTHENED (1)**: the G5 compounding note now covers **three** downstream readings (weights,
  news-coverage frontier, and — new today — the identity of each sector's `top1`, which is what G3 tests).
- **🟡 SOFTENED (1)**: the G2 conditional. Yesterday it named a live hazard in the differencing window;
  today the defective band (08-22/23/24) sits outside the four most recent snapshots, so the conditional
  applies only to reach-backs of five snapshots or more.
- ⚠ **What a copy-forward would have produced today**: *"the flippers are Health Care and Energy"*
  (half-false — it would have **missed that NVDA alone owns IT's positive sign** while needlessly
  restricting Energy), and *"today's snapshot has already accrued"* (true 08-28, **false** today).
  `D358-KR`'s failure mode caught by the column for the fourth run running.
