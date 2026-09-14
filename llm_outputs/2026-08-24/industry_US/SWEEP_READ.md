# SWEEP_READ — industry_US · 2026-08-24 (Mon) · Stage 4 / L1·SWEEP

> **A reading, not a report.** Numbers live in `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` ·
> `CYCLE_EXPOSURE.json`; no table from those files is reprinted here. This file exists to feed
> ROTATION §2 with what the JSON cannot say.

## 0 · 🚨 Instrument health line — read BEFORE the numbers

`SECTOR_FLOW_US.json §scoring`: `vel_axis=false` · **`vel_coverage = 0.0`** · `n_axes = 3` ·
`scored = 299` · `dropped_missing_axis = 0` · `asof = 2026-08-21`.

**The news axis is DEAD this run — and the cause is the pipe, not silence.** Probed, not assumed:
`fts search Nvidia --days 7 --count --scope foreign` returned **3704 · 3704 · 3704** minutes before
the sweep (08-23 read 3475 ⇒ **+229 new foreign articles**), and a 40-name falsification probe on the
sweep's own silent set returned **40/40 valid, 0 false silences** minutes after (**400/400 cumulative
over ten runs**). Run 1 measured **16.4%**, run 2 on the identical price frame measured **0.0%**.
★ **New this run, from PREFLIGHT §1: the 49 names that DO get counted are universe ranks 0–48 —
contiguous from rank 1, identical to yesterday's 49, 16.4% of names but 69.0% of universe market cap.**
⇒ Any name outside the top 49 is **guaranteed** velocity-free. This is not sampling noise.

🚫 **Because coverage is exactly 0.0, all 299 names are scored on the identical 3 axes** — the tag
layer is provably velocity-free and is citable as *3-axis unanimity*, never as *news-confirmed*, and
**never compared to a pre-08-22 run's breadth**.

**Flippers handed to ROTATION (§2 may not promote or demote on these):** **1 of 11** —
**Consumer Staples**, `top1 = WMT`, `top1_w = 28.9%`, `wflow −0.013` → **ex-top1 +0.116**.
The other ten print `top1_flips_sign = False` and carry no flipper restriction.

**Held-but-not-in-universe:** ✅ **0.** All 11 US paper-book holdings are inside `us_top300.csv` **and**
carry a score (checked by direct set comparison in PREFLIGHT G5). The real KIS book's five US names
(`NVDA` `ANET` `MPC` `PSX` `RTX`) are a subset. ⚠ **`EA` is in the universe but absent from the price
frame for a 12th run** — 299 scored of 300 — so `EA` is **unmeasured, not quiet**.
⚠ `us_top300.csv` is **40 days old**; no cap-weighted claim rests on its weights.

## 1 · Universe headline

**n = 299 · wflow −0.076 · 🟢 6 / 🔴 71** — **identical to the last two runs, element for element**
(`asof` 2026-08-21 for a third run; `n_new_sessions_since_prior_run = 0`). **Nothing in this section
is new information, and saying so is the point.**

## 2 · ★★★ The cross-check that matters: `breadth` is not breadth, and on the US board the gap is +29.4pp

`D325` established that `SECTOR_FLOW.json`'s `breadth` field is `greens / n` — the **🟢 rate**, gated on
`vol_surge ≥ 1.2`. Recomputed here against true participation (`OBV 매집` **∧** `rs20 > 0`), all 299
names (`M865`):

**Universe: green_rate 2.01% vs participation 31.44% ⇒ gap +29.4pp** — **larger than the KR desk's
measured +26.4pp** (`D332-KR`). Rank inversions, and they are not marginal:

- ★★ **Communication Services: green_rate 0.0% (joint LAST) → participation 66.7% (FIRST on the board).**
  8 of 12 names accumulating with positive rs20 — and **the highest `vol_surge` among all eight is 0.83**.
  The entire sector is accumulating on *below-average* volume, so not one name can reach the 🟢 gate.
- **Health Care 3.1% → 59.4% (2nd)** · **Consumer Discretionary 0.0% → 39.3%** · **Energy 0.0% → 37.5%**
- **Utilities 0.0% → 0.0%** — the **only** sector where the two instruments agree, exactly as the KR
  run found (one agreeing cell there too).
- **Industrials 16.0%** — 2nd worst participation, and it agrees with its `wflow` rank.

**Confirms the MACRO matrix:** **UTIL UW−** (0/0 on both instruments; the board's only unambiguous
zero) · **INDU UW−** (16.0% participation, 2nd worst, and `exc5 −1.736 = −1.29σ`) · **HLTH OW**
(59.4%, 2nd best participation, best `exc5 +3.889`, best `wflow +0.196` — three instruments agreeing).

**Contradicts the MACRO matrix — one line, and it is the file's main output:**
🚨 **COMM is graded `N` and the money says it is the board's most-participated sector.** The matrix's
own note compounds it: `D297` means `GOOGL` 38.3% + `GOOG` 38.3% = **76.6%** of COMM, so its flipper
test is structurally halved and its aggregate is two rows of one company. **ROTATION should treat
COMM's `N` as unproven in either direction rather than as a settled grade.**

## 3 · Shortlist absences — diagnosed, not cited

Six names cleared the filter (`mcap ≥ $10B` ∧ 🟢 ∧ flow-desc top-15): **Financials 1 · IT 2 ·
Health Care 1 · Staples 1 · Materials 1.**
**Absent: Energy · Industrials · Utilities · Real Estate · Communication Services ·
Consumer Discretionary — six of eleven sectors produced nothing.**

★ **Diagnosis, and the answer is the same for five of the six: it is a `vol_surge` filter artifact,
not an absence of money** (`M866`).
- **Energy** — six names are accumulating with positive rs20: `PSX` **+0.728** (surge **1.11**) ·
  `MPC` **+0.700** (**1.06**) · `COP` +0.694 (1.05) · `VLO` +0.506 (0.71) · `CVX` +0.369 (0.93) ·
  `BKR` +0.365 (0.66). **Not one fails on OBV or on RS. All six fail on `vol_surge` alone**, two of
  them by less than 0.15. **This is the exact case measured 2026-07-15 — refiners OBV-accumulating,
  tagged 🟡, read as an absence.** It is not an absence.
- **Communication Services** — 8 of 12 participating, max surge **0.83**. Structurally unable to green.
- **Consumer Discretionary** (39.3% participation) and **Real Estate** (16.7%) — same shape, smaller.
- **Utilities** — ★ the one absence that IS evidence: participation **0.0%**, `wflow −0.648`,
  `exc20 −11.469`. **Both instruments agree there is nothing there.**
- **Industrials** — 16.0% participation with `exc5 −1.29σ`: a genuine absence, and `P93` is armed on it.

★★ **The whole board's 🟢 count is a volume filter.** All six greens have `vol_surge` **1.25–1.68**
(`COIN` 1.68 · `MSTR` 1.61 · `MRK` 1.56 · `TGT` 1.51 · `ECL` 1.40 · `MSI` 1.25). **Every accumulating
name on quiet volume is invisible to the tag layer**, and there are ~94 of them.

**New-🟢 ignitions: 2 of 299** — `MSI` (IT, surge 1.25) and `ECL` (Materials, surge 1.40). Both are
also the two lowest-surge greens, i.e. the ignitions are marginal passes of the gate, not step changes.

## 4 · The gate's own scoreboard — and it cuts both ways (`M867`)

HANDOVER §6 measured the US IC ledger for the first time (405 rows, 33 run-dates). Two cells bear
directly on §3 above, and they disagree with each other:

- ✅ **`vol_surge` h=1: `IC +0.0398`, `t(NW) +3.40`, 67% positive — Bonferroni pass, POSITIVE.**
  On US data the gate that excluded `PSX`/`MPC`/`COP` is selecting **for** 1-day forward returns.
  🚫 **The KR desk's argument for distrusting this gate (`t −3.86`, negative) does NOT transfer** —
  that is the `W1` line and it holds in both directions.
- 🚨 **`rs60` h=5: `IC −0.1310`, `t(NW) −5.46`, 7% positive — Bonferroni pass, NEGATIVE**, and h=1
  carries the same sign. **The six greens all sit on high rs20 (14.2 · 26.5 · 12.8 · 17.3 · 11.4 ·
  1.2).**
⇒ **Horizon decides.** A 🟢 read at **h=1** is supported by the ledger; the same 🟢 read as a
multi-session lean runs into the board's strongest measured negative cell. **ROTATION and BET should
carry the horizon on the same line as any 🟢 citation.**
⚠ Regime label required: the 33 US run-dates span **2026-07-13 → 2026-08-20**, a window containing the
mid-August drawdown. `rs60`'s −5.46 is the shape a drawdown produces and does not generalise to a
trending tape. ⚠ `n_eff 5.4` clears the bar but only just; the h=10 rows are **unquotable** (`n_eff 2.1`).

## 5 · Shortlist read + cycle exposure

**Short-pressure (FINRA z, proxy — the US has no investor-type feed):** one clean-rise name —
**`MSTR` z −1.23 (low-short / covering)**. `COIN` +0.81, `TGT` +1.22, `MSI` +0.77 are 🟡 normal;
`MRK` −0.25, `ECL` −0.07 neutral. **No crowded-short in the shortlist**, so there is no squeeze-fuel
name this run. ⚠ Crowded-short is turn-conditional fuel and never a stand-alone reason (P4).

**`CYCLE_EXPOSURE` — ✅ no GAP.** Real KIS book ≈ **$10,986** total / **$5,097** invested.
AI-compute rank 1: epicenter **16.4%** vs need ≥12.0% (`NVDA`, `ANET`) ✅ · Energy/refining rank 2:
**10.0%** vs need ≥8.0% (`MPC`, `PSX`) ✅ · Missile-defense rank 3: 3.83% (`RTX`), **no threshold set**
⚪. **Nothing is handed to ALPHA's action bracket from this leg.**
⚠ Standing, unchanged for a 4th run: **`cycle_registry.json` still has no optical/interconnect row**
(`D250`/`M731`), so `LITE`/`COHR`/`CIEN` exposure is **unmeasurable, not zero** — and `D329` records
that the single `AI-compute-EPICENTER` label spans **2–3 measured risk units**.

---
*Reading only. No grade, no name recommendation, no sizing (P4).*
