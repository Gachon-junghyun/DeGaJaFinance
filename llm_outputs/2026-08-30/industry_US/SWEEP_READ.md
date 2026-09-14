# SWEEP_READ — industry_US · 2026-08-30 (Stage 4 / L1·SWEEP)

> The reading, not a second copy of the data. Sector rows live in `SECTOR_FLOW_US_REPAIRED.json
> §sector_rotation`; per-name rows in `US_LIVE_SHORTLIST.json`. Neither is reprinted here.

## 0 · 🚨 Instrument health line — read before any number below

**The native sweep produced nothing.** `SECTOR_FLOW_US.json §scoring`:
**`n_axes` 3 · `vel_coverage` 17.06% · `scored` 0 · `dropped_missing_axis` 299 ·
`sector_rotation` `[]` · `names` `[]`.**

- **News axis: DEAD this run** (17.06% « 80%). **Cause probed, not assumed** — 5 of 5 names the sweep
  recorded as `velocity: null` (QCOM · DIS · ADBE · PFE · T) returned normal velocities on a direct
  query two minutes later, and the pre/post-sweep probes ran 6/6 and 4/4. ⇒ **pipe, not silence.**
  🚫 No theme-freshness or news-velocity claim anywhere downstream.
- **Price axis: DEAD in the native run, and REPAIRABLE.** All 301 cached tickers (bench SPY included)
  carried a 2026-08-28 row with **Close = NaN and Open/High/Low/Volume present**, which nulls
  `rs20`/`rs60` for every name and drops all 299. **Isolated by experiment**: trimming the bench alone
  does **not** repair it (unlike the KR case) — both sides must be repaired.

## 0b · What I did about it, and where the line is

**`SECTOR_FLOW_US.json` is left exactly as the tool wrote it** — empty — because it is the honest
record of what the instrument produced. A **separately named** reconstruction was built beside it:

**`SECTOR_FLOW_US_REPAIRED.json`**, carrying a `provenance` block. What was changed and what was not:
- **Changed**: the 08-28 `Close` only, replaced by the **5m-proxy close** (validated on 08-27 against
  official closes: **0.018% mean / 0.045% max error, n=24**; universe-wide n=324, mean 0.022%, 319 of
  324 inside 0.1%, worst `MU` 0.60%). **300 patched · 1 trimmed · 0 missing.**
- **Not changed**: Open/High/Low/Volume are the provider's originals; the scoring engine is
  `scripts/sector_flow.py`'s own `price_axes`/`flow_score`/`score_all`/`aggregate_sectors`,
  **unmodified**; the news axis was **not re-queried** (G1 discipline — the sweep is not re-run in
  this run), so `use_vel_axis=False`, **3 axes, the identical scale the native run would have used.**
- **Result: 299 of 299 scored, 0 dropped.** The repair is complete, not partial.
- 🚫 **This does not make the repaired file a settled reading.** It is a labelled reconstruction; every
  downstream citation says so, and `US_LIVE_SHORTLIST.json` records that it was built from it.

⚠ **Open decision resolved for this unattended run**: a repaired reconstruction gets a **new filename**
rather than overwriting a load-bearing one. Rationale — the protocol's file rule protects the *name*
for downstream globs, but a downstream reader that globs `SECTOR_FLOW_US.json` is entitled to the
tool's output, not to mine. Logged in the run summary.

## 1 · Universe headline — three numbers

**n = 299 · wflow = −0.136 · 🟢 4 / 🔴 73.**
⚠ Repaired basis, `asof` **2026-08-28**. **No Δflow is computed and none may be cited**: G2 has no
operand (the native run scored 0), and the previous comparable snapshot (the 08-28 run) carries
`D401` — its terminal bar was a **live intraday print wearing a settled date**. Two reasons, either
sufficient.

## 2 · Cross-checks against the MACRO matrix — confirm / contradict

| MACRO §D said | the repaired flow says | verdict |
|---|---|---|
| **`UTIL` UW** (worst `exc20`, −6.69) | **worst sector on the board**, `wflow` −0.548, **10 red of 15, 0 green**, and it does **not** flip on its top-1 (`NEE`, 17.7%) | ✅ **CONFIRMED, and independently** — the ETF read is price, this is OBV/RS/volume, and neither depends on the other |
| **`IT` cut to N**, two-sided (best `exc20`, worst `exc1`, `SMH` −15.31 exc60) | `wflow` **+0.034** — 2nd of 11 — but `eqflow` **−0.033**, i.e. **negative on breadth**, **3 green of 56 (breadth 0.05) against 13 red**, and it **FLIPS SIGN on `NVDA`** (19.4% ⇒ +0.034 → −0.015) | ✅ **CONFIRMED and sharpened.** The N call was made on a price sign-flip; the flow adds that the sector's positive cap-weighted number **is one name**. **All three of IT's greens are software (CRM · INTU · MSTR), none is a semiconductor** |
| **`MATR` N** with a Copper-COT-100th-%ile caution | **best sector, `wflow` +0.225**, and it does **not** flip on `LIN` | ⚠ **CONTRADICTED on direction, and I am not moving.** The money says MATR is the board's strongest; the positioning says its key input sits at the **100th percentile** of speculative length. **Flow and positioning point opposite ways and ROTATION gets both**, not a reconciled number |
| **`COMM` N with an OW-lean** (best `exc1` +1.63 and `exc5` +0.94) | **`wflow` −0.424 (10th of 11) against `eqflow` +0.079** — **a 0.503 gap, the widest on the board** — `GOOGL` is 38.3% of the bucket and `wflow_ex_top1` is **−0.341** | ★ **CONFIRMS the lean and relocates it.** Breadth is positive while the cap-weighted read is deeply negative ⇒ **the ETF's strength is not `GOOGL`-led.** ⚠ But the bucket does **not** flip sign, so the sign is not a one-name artifact either — the *magnitude* is |
| **`ENRG` N**, held there for instrument reasons (`R89`/`P83`) | `wflow` −0.097 but `eqflow` **+0.005** and `wflow_ex_top1` **+0.074** — **`XOM` (30.5%) alone makes Energy negative. FLIPPER** | ✅ **CONFIRMED as N.** And the flip is why: **the sector's negative sign is one name**, so neither a promotion nor a demotion is available on this axis |
| **`FIN` OW** (best `exc60` +12.19, up on the hawkish day) | `wflow` **−0.072**, `eqflow` −0.090, **0 green of 47**, no flip | ⚠ **CONTRADICTED, and this is the run's sharpest disagreement.** Price momentum says leadership; OBV/RS/volume say **zero accelerating names in a 47-name sector**. **Both are handed to ROTATION with the conflict named** — see §4 |
| **`INDU` UW** (`exc5` −2.23, `exc20` −4.52) | `wflow` −0.317, **17 red of 50 — the most reds of any sector**, no flip | ✅ **CONFIRMED** |
| **`HLTH` OW** (best `exc60` +13.99) | `wflow` +0.021 (3rd), **`eqflow` +0.135 — the best breadth number on the board**, no flip | ✅ **CONFIRMED, and on the stronger of the two axes** (breadth, not cap weight) |

## 3 · Flipper list — handed to ROTATION in full (3 of 11)

**ROTATION may not promote or demote these three on `wflow`.**

| sector | top1 | top1 weight | `wflow` | `wflow_ex_top1` |
|---|---|---:|---:|---:|
| Information Technology | `NVDA` | 19.4% | +0.034 | **−0.015** |
| Energy | `XOM` | 30.5% | −0.097 | **+0.074** |
| Consumer Discretionary | `AMZN` | 40.2% | −0.262 | **+0.056** |

⚠ **`AMZN` at 40.2% of Consumer Discretionary is the largest single-name share on the board** — the
sector's `wflow` is −0.262 and without it the remainder is **+0.056**. ⇒ **"Consumer Discretionary is
weak" is, on this axis, a statement about one company.**
⚠ **The other eight are listed as non-flippers, which is an observation and not a clean bill** —
`R108` (retracted 08-29) removed the right to cite a non-flipper as evidence that a bucket is clean.

## 4 · Shortlist composition — read the ABSENCES

`US_LIVE_SHORTLIST.json`: **4 names pass** (mcap ≥ $10B ∧ tag 🟢가속). Names are in the artifact.

**Absences, each diagnosed before being cited:**
- **9 of 11 sectors produced zero shortlist names.** ⚠ **Diagnosed as real, not as a filter artifact**:
  the universe has **only 4 greens in 299** — the filter is not the binding constraint, the tape is.
  🔴 outnumbers 🟢 **73 to 4**, an 18:1 ratio.
- **Zero semiconductors.** IT supplies 3 of the 4 greens and **all three are software.** ⇒ the sector
  the book is most concentrated in has **no accelerating name on this axis**, which is the flow-side
  restatement of `SMH`'s `exc60` **−15.31**.
- **Zero Financials, from 47 names.** This is the absence that carries the §2 contradiction: a sector
  leading by 12.19pp over 60 sessions with **not one accelerating name**. ⚠ **Diagnosed**: `XLF`'s
  60-day leadership is a **price** fact and this axis is an **OBV/RS/volume** fact; they are not the
  same measurement and the desk does not have a rule that says which wins. **Named as an open
  contradiction for ROTATION, not reconciled here.**
- **Zero Energy**, despite `MPC` **+0.650** and `PSX` **+0.388** being the book's two strongest flow
  scores — **both tagged 🟡중립, so the 🟢-only filter excludes them.** ⚠ **This is a filter artifact
  and it is the exact one logged on 2026-07-21** (an ENRG shortlist of 0 that turned out to be
  OBV-accumulating names wearing a 🟡 tag). **Recorded as reproduced, not rediscovered.**

## 5 · Held-but-not-in-universe — the desk can tag everything it owns

**11 of 11 US holdings are in `us_top300.csv` (300 rows); missing 0.** ⚠ The builder was **not** re-run
(`build_us_universe.py` would rebuild a 46-day-old file mid-run, which is a human-approval item); the
check was made directly against the wired CSV. **No 🚨 on this invariant this run.**
⚠ The two KR holdings (`028050`, `316140`) are outside the US universe **by construction** and are
covered by the KR desk's own file — not a US coverage miss.

## 6 · Cycle exposure — GAP check

`cycle_exposure.py` → `llm_outputs/2026-08-30/CYCLE_EXPOSURE.md`. **No GAP**: rank-1 AI-compute
epicenter **16.93%** (need ≥12.0%) via `NVDA`/`ANET`; rank-2 Energy/refining **9.97%** (need ≥8.0%)
via `MPC`/`PSX`; rank-3 missile-defense 3.83% via `RTX`, **threshold unset**.
🚨 **`D250`, 14th run**: the registry still carries **no optical row**, so `LITE`/`COHR` exposure is
**unmeasurable, not zero** — and a cycle with no row cannot produce a GAP flag by construction.
**Nothing handed to ALPHA's action bracket on this axis.**

## 7 · The one line ROTATION most needs

**On price the board is led by what worked over 60 sessions (`XLV` +13.99, `XLF` +12.19); on money it
is led by breadth in Materials and Health Care, dragged by Utilities, and its single positive
mega-cap sector (IT) is one name wide.** **The two axes disagree hardest on Financials — and the
disagreement, not either number, is what ROTATION is being handed.**
