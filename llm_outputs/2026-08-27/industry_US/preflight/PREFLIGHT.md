# PREFLIGHT — industry_US · 2026-08-27 (Phase −1, INSTRUMENT_CHECK)

> Measures whether today's instruments **work**, not whether they return an answer.
> No market view, no tickers-as-picks, no sizing (P4).
> ★ A FAIL is not a warning — it removes a **citation right** for this entire run.

Baseline snapshot read (PREFLIGHT runs before today's SWEEP):
`llm_outputs/2026-08-26/industry_US/SECTOR_FLOW_US.json` (asof 2026-08-26, 1 day old).

---

## Gate table

| # | Gate | Measured | Verdict |
|---|---|---|---|
| G1 | News axis alive | baseline `vel_coverage` **17.06%** (51/299) vs 80% bar; live probes **alive** (Nvidia 4756 / Nasdaq Inc 6 / Nucor 31 / Marathon Petroleum 22, `--days 7 --scope foreign`). ★ New this run: the covered 51 are **exactly universe ranks 1–51**, a contiguous mcap prefix | **FAIL** |
| G2 | Scoring-scale continuity | `n_axes` = **3** on 08-20 → 08-26 (7 consecutive snapshots); `dropped_missing_axis` = 0 on all | **PASS** |
| G3 | Who owns the sector sign | flipper list printed: **3 of 11** — Consumer Discretionary (`AMZN`), Materials (`LIN`), Energy (`XOM`) | **PASS** (list emitted) |
| G4 | Risk-unit stability | 250d → **11 units**; 500d → **10 units**; 750d → **10 units**. Groupings differ | **FAIL** |
| G5 | Universe covers holdings | 11 US book names, **0 outside** `us_top300` (n=300); universe file age **43 days** (bar ≤8) | **FAIL** (staleness leg) |
| G6 | Measurement accrual rate | `snapshot_estimates --status`: 18 files / 36 calendar days = **0.50/day**, **2.0× slower** than ideal (bar ≤1.5×) | **FAIL** |
| G7 | Tool liveness | 13 modules + 14 scripts probed; **26 exit 0**, 1 non-standard (`module_chart`) verified live by real invocation | **PASS** |

---

## G1 — News axis alive · **FAIL**  ★ the diagnosis changed today

- **Command / source**: baseline `SECTOR_FLOW_US.json §scoring` →
  `{vel_axis: false, vel_coverage: 0.1706, n_axes: 3, scored: 299, dropped_missing_axis: 0}`.
  Bar is 80%. The sweep log confirms it: `[axis] velocity 측정 51/299 = 17.1% → 속도축 제외`.

- **Falsification probe actually run** (pipe vs silence — the gate's whole point):
  `module_news_data fts search "<name>" --days 7 --count --scope foreign`, via the NEWS API tunnel →
  **Nvidia 4756 · Nasdaq Inc 6 · Nucor 31 · Marathon Petroleum 22**. Three orders of magnitude
  between loudest and quietest ⇒ the pipe is alive **and discriminating** right now.

- ★ **New measurement — the missing 248 are not random.** Extracted the ticker set with non-null
  `velocity` from three snapshots and mapped it onto `us_top300.csv` rank:
  - 08-26: 51 names — **ranks 1,2,3,…,51. A contiguous prefix, no gaps.**
  - 08-25: 51 names — **identical set** (overlap 51/51, zero difference).
  - 08-21: 50 names — overlap 50/51 with today's set.

  The sweep iterates names in market-cap-descending order (`scripts/sector_flow.py:499`). So the news
  pipe answers for the **first ~51 calls of the run and then stops answering for the remaining ~248**,
  and never recovers inside that run. The 16.4 / 16.7 / 17.1% band seen across every recent run is that
  same cutoff wobbling by ±2 names.
  ⇒ **Yesterday's phrasing "the failure tracks burst load" was directionally right but the wrong shape.
  It is a hard stop at a call count, not a random thinning.** Random thinning cannot reproduce a
  gap-free rank prefix twice, nor an identical 51-name set on consecutive days.

- **Second falsification — called one at a time, the "missing" names all answer.** Ran
  `flow_read.news_velocity(_news_query(tk,name), 7, 30, kr=False)` in-process for four names the
  sweep recorded as `velocity: null`:

  | ticker | universe rank | query | recent / base | velocity |
  |---|---|---|---|---|
  | NUE | 217 | `Nucor` | 31 / 95 | **1.40** |
  | MPC | 177 | `Marathon Petroleum` | 22 / 127 | **0.74** |
  | NEE | 68 | `NextEra Energy` | 16 / 102 | **0.67** |
  | WELL | 84 | `WELL\|Welltower` | 6999 / 30225 | **0.99** |

  All four returned `source: "api"` and a finite velocity. **`null` in the sweep therefore means
  "not counted", never "no articles"** — measured, not assumed.

- **Trend**: vel_coverage 16.4% (08-20) → 16.7% (08-21) → **0.0%** (08-22, 08-23, 08-24) →
  17.1% (08-25) → 17.1% (08-26). **Seven consecutive runs below bar**, three of them at zero.

- 🚫 **Rights removed for this run**: cannot cite **theme freshness** or **news velocity** in any stage
  (MACRO, SWEEP, EVENT_ALPHA, ROTATION, PREMORTEM, DEEP, BET, ALPHA). Cannot rule any name or sector
  **"quiet"** — quiet was not measured. Any freshness tag in BET_SHEET §B must read
  `UNMEASURED (G1 FAIL)`, never `stale` / `cold` / `quiet`.
- 🚫 **Additional right removed today, from the prefix finding**: even a *partial* velocity reading may
  not be used as a **cross-sectional** comparison, because coverage is **rank-ordered**. The 51 measured
  names are the 51 largest caps; the 248 unmeasured are systematically smaller. A ranking built on the
  covered subset is a mega-cap-only ranking wearing a universe label.
- ↳ **Not removed**: single-name news lookups done **by hand** in later stages stay legal — that is
  exactly the probe that passed, and it passed for low-rank names too (NUE #217, MPC #177).

## G2 — Scoring-scale continuity · **PASS**
- `n_axes` = 3 on 2026-08-20, 08-21, 08-22, 08-23, 08-24, 08-25, 08-26. `dropped_missing_axis` = 0 on all seven.
- Same axis count on both sides of every subtraction ⇒ Δflow arithmetic is scale-legal against this history.
- ⚠ Conditional stands: the axis switches on at `vel_coverage ≥ VEL_COVERAGE_MIN` (80%). Given G1's
  finding that coverage is pinned by a **call-count cutoff at ~51**, a mid-run flip to `n_axes = 4` is
  *less* likely than yesterday's reading implied — it would require the cutoff to disappear entirely,
  not merely to improve. SWEEP must still re-read `§scoring.n_axes` before differencing anything.

## G3 — Who owns the sector sign · **PASS**
- Source: baseline `§sector_rotation[].top1_flips_sign`, 11 sectors evaluated.
- **Full flipper list (3 of 11)** — written out in full, per EXIT rule:
  - **Consumer Discretionary** — top1 `AMZN`; `wflow` **+0.035**, `wflow_ex_top1` **−0.003**,
    `eqflow` **−0.270**, n=28, breadth 0.00. The *only* positive `wflow` in the whole table is one company's.
  - **Materials** — top1 `LIN`; `wflow` **−0.059**, `wflow_ex_top1` **+0.053**, `eqflow` **−0.106**, n=12, breadth 0.00.
  - **Energy** — top1 `XOM`; `wflow` **−0.111**, `wflow_ex_top1` **+0.098**, `eqflow` **−0.011**, n=16, breadth 0.00.
- Eight sectors carry `top1_flips_sign: false`: Info Tech (NVDA), Financials (BRK-B), Health Care (LLY),
  Industrials (CAT), Consumer Staples (WMT), Comm Svcs (GOOGL), Real Estate (WELL), Utilities (NEE).
- 🚫 **Rights removed**: **Consumer Discretionary, Materials and Energy may not be promoted or demoted
  on the weighted-flow bucket** (ROTATION §2). Each must be ranked on `eqflow` and `breadth` instead,
  with the substitution stated inline at the point of use.
- 🚨 Note the asymmetry this creates: Consumer Discretionary is the sector a naive `wflow` read would
  rank **#1 (and the only green)**, and it is a flipper — `wflow_ex_top1` is negative and `eqflow` is the
  **second-worst** number in the table (−0.270). Ranking it on `wflow` today would be the single largest
  available instrument error.
- ↳ Flipper identity is **not stable run-to-run** and must never be carried from memory: the 08-24
  baseline flagged Consumer Staples/`WMT`, the 08-25 baseline flagged Health Care/`LLY`, today's flags
  three different sectors. Third consecutive change of identity.

## G4 — Risk-unit stability · **FAIL**
- Ran all three windows (`risk_units.py --book --days 250 / 500 / 750`). Not one window.
- **250d → 11 units** (249 aligned days; ARI 0.3188; within-group resid corr +0.6047; max resid corr +0.8509).
  `{028050, 316140}` merged; `ANET`, `ETN`, `AVGO`, `NVDA` each **standalone**.
- **500d → 10 units** (ARI 0.1899; within +0.5260; max +0.8471). `{ANET, ETN}` merged; `{AVGO, NVDA}`
  merged; `028050` and `316140` **split apart**.
- **750d → 10 units** (ARI 0.3810; within +0.5160; max +0.8232). Grouping **identical to 500d**.
- **The disagreement is structural**: at 250d the book reads as *four* independent AI-complex risks;
  at 500/750d it reads as *two*. The concentration answer is a function of the lookback.
- Threshold sensitivity severe at all three windows: dist 0.40–0.60 → 12 units everywhere;
  0.85 → 6 units (250d) / 4 (500d) / 5 (750d). The chosen 0.65 sits on a slope, not a plateau.
- 🚫 **Right removed**: no concentration guard may be quoted as a single number. Every unit-count or
  concentration statement this run carries its `--days` **on the same line** (e.g. "10 units @750d").
  A bare "the book holds N independent risks" fails EXIT.
- ↳ Tool's own logs, carried as instrument notes (no repair here): one measured unit spans **two book
  theme labels** in every window (250d: KR-E&C/plant + KR-bank-holding; 500/750d: AI-compute-EPICENTER
  + AI-power/electrical) — `MAX_THEME_PCT` counts as 2 what correlation measures as 1. S5 warning stands:
  ARI (0.19–0.38) moves **opposite** to within-group fit at all three windows. Calendar-intersection loss
  is 22 / 48 / 66 days on the six US names, and KRW/USD local returns are mixed in the same matrix
  (common-FX factor injection possible).

## G5 — Universe covers holdings · **FAIL** (staleness leg)
- **Coverage leg — clean**: 11 US book names (`ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX`)
  checked against `data/us_universe/us_top300.csv` (n=300) → **0 outside the universe**.
  (The 2 KR book names `028050`, `316140` are out of US-universe scope by construction, not by defect.)
- **Freshness leg — fails**: `us_top300.csv` mtime **2026-07-15 = 43 days old**, bar ≤8 days.
  Market caps are stale ⇒ **the weights are stale**, and `wflow` is a cap-weighted number. Membership may
  also be stale (a name that entered or left the top 300 in 43 days is mis-listed). The sweep raises it
  itself: `[warn] 유니버스 us_top300.csv 42일 경과 — 시총 stale`.
- 🚫 **Right removed**: cap-weighted sector flow (`wflow`) may not be cited as a **current** weighting —
  it is weighted as of 2026-07-15. Where `wflow` and `eqflow` disagree this run, **`eqflow` is the citable
  one**; `wflow` may be reported only with the 43-day tag attached.
- ★ **Compounding note (G5 × G1)**: the rank column of this same stale file is what determines which 51
  names the news axis reaches before the cutoff. The staleness corrupts *two* instruments, not one —
  the weights **and** the coverage frontier.
- ↳ Not removed: per-name flow/RS/OBV/short judgments on the 11 holdings remain legal — all 11 are covered.

## G6 — Measurement accrual rate · **FAIL**
- `snapshot_estimates.py --status`: **18 files across 36 calendar days** (2026-07-22 → 2026-08-26)
  ⇒ measured **0.50/day** vs ideal 1.0/day = **2.0× slower** (bar 1.5×).
- Gaps (days): `[5, 1, 1, 1, 1, 1, 1, 1]`, median 1, max 6. The 40-dated-sample target needs 22 more
  files: **~44 days away at measured rate**, not the 22 days a file-count reading implies (D16's trap).
- ⚠ **Today's file has not accrued yet** at PREFLIGHT time (tool reports "마지막 저장 이후 1일"). The
  window is identical to yesterday's reading because nothing was added in between; the ratio worsens
  arithmetically if today's snapshot is missed.
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
  (positional-arg CLI). Probed for real instead: `module_chart NVDA --read` → **exit 0**, full structural
  read returned (OBV slope, divergence, MA stack, Bollinger, RSI, turn verdict, trigger/stop).
  Treated as **live**; this gate measures liveness, not flag conformance. No right removed.
- ⚠ Liveness ≠ correctness. G1 is the standing proof: `module_news_data --help` exits 0 and the module
  answers single queries, yet the axis it feeds is 17% covered. G7 passing removes no other gate's FAIL.

---

## What this run may NOT claim (consolidated)
1. **No news-velocity or theme-freshness citation anywhere**, and **no "quiet"/"no news" verdict** on any name or sector. (G1)
2. **No cross-sectional use of the partial velocity subset** — its coverage is a market-cap rank prefix (1–51), so it is a mega-cap-only sample. (G1, new today)
3. **No bare concentration number** — every unit count carries its `--days` on the same line. (G4)
4. **`wflow` is not a current weighting** — 43-day-old caps; prefer `eqflow` on disagreement, tag `wflow` when used. (G5)
5. **Consumer Discretionary, Materials and Energy may not be promoted/demoted on the weighted-flow bucket** — substitute `eqflow`/`breadth` and say so inline. (G3)
6. **No IC-backed sizing language** — any fraction is "mechanical 1/4", explicitly unmeasured. (G6)
7. **SWEEP must re-read `§scoring.n_axes` before any Δflow subtraction.** (G2, conditional)

## Instrument notes (no repair attempted — rule 1)
- **G1's mechanism is now localised**: not "the tunnel is flaky", but "the run gets ~51 answered news
  calls and then zero". That is a bounded, testable claim, and it is the first time this gate has
  produced one. Filed for `idle_probe` / human approval; **not fixed here.**
- **Latent query contamination found while probing G1** (not itself a gate verdict):
  `news_query('WELL','Welltower')` returns `WELL|Welltower` because `WELL` is absent from
  `STOPWORD_TICKERS` (`module_flow/_config.py:26`). It counts **6999 hits / 7d** — the English word
  "well", not the company. `WELL` is Real Estate's top1, so if the news axis were ever repaired, that
  sector's velocity would be garbage **and would look healthy**. Recorded because it is exactly the
  D-class defect this stage exists to catch: a plausible number from a broken source.
- G3's flipper identity changed for the **third consecutive run** (STPL/WMT → HLTH/LLY → CD+MATR+ENRG).
  Flipper status is a per-run measurement; copying it forward is a fabricated instrument reading.
- G4's cross-window disagreement and G5's 43-day universe are both **weighting-layer** defects: they move
  the same numbers (cap weights, correlation grouping) that concentration and rotation rest on.
- G6 has stopped improving — 18 files / 36 days is byte-identical to yesterday's reading.

## EXIT CHECK
- [x] All 7 gates carry PASS/FAIL/UNKNOWN **plus real numbers**. Zero blanks. Zero UNKNOWNs.
- [x] Every FAIL states the removed right as "cannot cite X today", not "be careful".
- [x] G1 ran the falsification probe — twice: 4 CLI probes (3 orders of magnitude apart) **and** 4
      in-process `news_velocity` calls on names the sweep recorded as null, all of which returned finite
      velocities. Low coverage is **not** written as "no news".
- [x] G3's flipper list is written out in full — 3 named with numbers, 8 explicitly false.
- [x] G4 ran all three windows (250/500/750) and reports three separate groupings.
- [x] `PREFLIGHT.md` exists before HANDOVER starts.

---

## ADDENDUM — `vs-yesterday` DIFF column (`D358-KR`, second run under the rule)

| # | 08-26 verdict | 08-27 verdict | Verdict changed? | **Number / content changed?** |
|---|---|---|---|---|
| G1 | FAIL | FAIL | no | ⚠ **YES — the diagnosis changed, not the number.** `vel_coverage` identical (17.06%), but the covered set is now measured as **ranks 1–51 contiguous** and **identical name-for-name to 08-25**. Yesterday's written mechanism ("tracks burst load") is superseded by "hard stop at ~51 calls", and a **new** right is removed as a result |
| G2 | PASS | PASS | no | n_axes 3 on both sides; history extends 6 → 7 snapshots. ⚠ The conditional is **weaker** than yesterday claimed — a call-count cutoff will not drift up to 80% |
| G3 | PASS | PASS | no | 🚨 **YES — the flipper list changed again, and grew 1 → 3.** 08-26 named **Health Care (`LLY`)**; today names **Consumer Discretionary (`AMZN`) + Materials (`LIN`) + Energy (`XOM`)**. The HLTH restriction is **LIFTED**; three new ones are **ATTACHED** |
| G4 | FAIL | FAIL | no | no — identical counts (11/10/10) and identical groupings to 08-26 |
| G5 | FAIL | FAIL | no | universe age **42d → 43d** (one day worse; same defect) |
| G6 | FAIL | FAIL | no | **unchanged at 2.0× slower** — 18 files/36d on both days. Yesterday it was "trending toward pass"; today it did not move at all |
| G7 | PASS | PASS | no | no — same 26 exit-0, same one non-standard entry point |

### Removed-rights list, rendered as a DIFF against 2026-08-26
- **UNCHANGED (5)**: no news-velocity/theme-freshness citation · no bare concentration number ·
  `wflow` not a current weighting · no IC-backed sizing language · G2 conditional on Δflow.
- **🔴 REMOVED from yesterday's list (1)**: *"Health Care may not be promoted/demoted on the weighted-flow
  bucket."* **HLTH is not a flipper today** (`top1_flips_sign: false`; `wflow` −0.132 and `wflow_ex_top1`
  −0.029 carry the same sign) — the restriction does not apply this run.
- **🟢 ADDED to today's list (4)**: **Consumer Discretionary**, **Materials**, **Energy** may not be
  promoted/demoted on the weighted-flow bucket · **plus** the new G1 right: the partial velocity subset
  may not be used cross-sectionally, because its coverage is a market-cap rank prefix.
- ⚠ **What a copy-forward would have produced today**: *"the flipper is Health Care / `LLY`"* (true on
  08-26, false today), *"the failure tracks burst load"* (true but now known to be the wrong shape), and
  *"G6 is trending toward pass"* (true on 08-26, false today — it did not move). Three copyable
  sentences, three wrong. `D358-KR`'s failure mode caught by the column again.

---

## ⚠ CORRECTION appended by HANDOVER (same run, one stage later) — G1's "new this run" claim is WRONG ON PRIORITY

> Written per `§4c` / `D48`: **verification that arrives after the assertion is a finding, and it gets
> written down.** The G1 block above is **left standing exactly as written**; this is appended, not edited.

**What G1 asserted above**: that the contiguous rank-prefix measurement was **"★ New this run"**, and
that *"yesterday's phrasing 'the failure tracks burst load' was directionally right but the wrong shape."*

**What the next stage's read of `handoff/STANDING_VIEW.md` refuted**: the finding is **one run old and
already retracted by this desk**. On **2026-08-26** the `industry_US` run filed:
- **`R103`** — *"The news axis fails because the 300-query SWEEP overloads the tunnel"* → **RETRACTED**,
  killed by **`M947`**: the 51 velocity-measured names are `us_top300` **ranks 1–51, contiguous, and
  byte-identical to 08-25's set**. The retraction even records that the **08-25** run's own `M856` had
  already measured the contiguity while that same run's PREFLIGHT wrote the burst-load diagnosis.
- **`D371-KR`** (2026-08-27 `industry_kr`, this morning) cites `R103` by name as settled US doctrine and
  proposes porting the same test to KR.

⇒ **The measurement above is a 3rd independent reproduction, not a discovery.** Its *content* stands —
ranks 1–51 contiguous, 51/51 identical to 08-25, four in-process probes returning finite velocities on
names the sweep called null — and the **removed right it produced is unchanged and still binds**. What
is withdrawn is the **priority claim** and the implication that yesterday's diagnosis was still live:
**it was not; it had been killed 24 hours earlier.**

**Why this stage could not see it, and it is not carelessness** — PREFLIGHT's `vs-yesterday` DIFF column
(`D358-KR`) compares **this file against yesterday's PREFLIGHT.md**. Yesterday's `PREFLIGHT.md` is
**frozen at the moment it was written** and therefore still carries the burst-load sentence; the
retraction lives in `handoff/STANDING_VIEW.md`, which PREFLIGHT does not read (by design — the stage runs
before HANDOVER). **So a diagnosis retracted late in run N is invisible to the DIFF column in run N+1,
which is reading the pre-retraction text as if it were the standing view.** Registered as a dig by this
run's HANDOVER (**`D379`**), with the positive-form remedy stated there.

**Gate verdicts are unaffected**: G1 remains **FAIL**; all seven verdicts and all seven removed rights
stand exactly as tabled above.
