# SWEEP_READ — industry_US · 2026-08-15 · Stage 4/11 (L1·SWEEP)

> The reading, not a second copy of the data. Sector rows live in `SECTOR_FLOW_US.json §sector_rotation`;
> per-name rows in `§names` and `US_LIVE_SHORTLIST.json`. **Nothing that exists there is reprinted here.**

## 0 · The instrument's health line, read BEFORE its numbers

`§scoring` = `{"vel_axis": false, "vel_coverage": 0.1706, "n_axes": 3, "scored": 299,
"dropped_missing_axis": 0}`

**News axis DEAD this run (17.1%, 51/299) — third consecutive run at the same number.**
**Cause: the pipe, and this run measured it rather than assuming it.** An n=40 re-probe of names the
sweep recorded as `velocity: None`, using the sweep's own function and query builder, returned
**34 valid (85.0%) · 6 pipe-fail (15.0%) · ZERO genuinely no-news (0.0%)** (PREFLIGHT G1). ⇒ the 83%
silence is **100% instrument, 0% world**. ✅ `dropped_missing_axis: 0` — the 2026-08-09 per-name
axis-dropping defect (+0.305 board-wide inflation) **did not recur**; all 299 are scored on the same
3 axes.

🚨 **`D261` REPLICATED AND WORSE — the tag is 4-axis while the score is 3-axis.**
**6 of 11 🟢 cannot be produced by `OBV 매집 ∧ RS20>0 ∧ vol_surge ≥ 1.2`: `NFLX` `NVDA` `CVX` `MRVL`
`CSCO` `BAC`** — their `vol_surge` reads 0.63 / 0.73 / 0.95 / 0.48 / 1.37 / 0.73, and **`CSCO`'s RS20
is −4.7, negative** (the same name, the same defect, as 08-13). **All six carry a velocity value**, so
only the **revoked** axis can be lighting them. Velocity exists on 17.1% of the board ⇒ **1.9 greens
expected from the survivor sample, 6 observed = 3.2× over-representation** (08-13 was 5 of 11 = 2.6×).

⇒ **The admissible green count is 5, not 11**: `COHR` `KKR` `ABNB` `LITE` `MPC`.
**Every downstream stage uses 5/59, and this file states it once so no stage has to re-derive it.**

## 1 · Universe headline — three numbers

**n = 299 scored (300 requested; `EA` finally dropped out) · `wflow` −0.132 · 🟢 11 raw / **5
admissible** / 🔴 59.**

## 2 · 🚨 THE FINDING — the 🟢 gate did not measure demand this week, it measured volume

| | |
|---|---|
| Names passing `OBV 매집 ∧ RS20 > 0` | **110 of 299** |
| Of those, tagged 🟢 | **11** |
| **Blocked** | **100** |
| **Blocked by `vol_surge` < 1.2 ALONE** | **100 — 100.0%** |

★★ **`M144` replicates a SIXTH time, at the largest count yet** (US 07-22 **99** · US 07-23 68 ·
KR 07-24 191 · US 07-24 71 · US 08-13 74 · **US today 100**).

★★★ **And this run can say WHY it is this large, which prior runs could not.** `vol_surge` is a ratio
of the last bar's volume to its own trailing 20-day average. **The whole tape is running thin**: median
last-bar volume ÷ 20-day average was **0.732 on 08-13 and 0.649 on 08-14** (PREFLIGHT G0, licensed as
real because this is a weekend run on settled bars). In a thinning tape the denominator carries a
busier past, so **the leg fails board-wide at once** — the gate closes on everyone regardless of
accumulation. ⇒ **"breadth 0.00" this week is a statement about volume, not about demand.**

⚠ **This compounds with the desk's own scoreboard.** `vol_surge` is the only axis in `ic_ledger` with
a consistent sign across two horizons and it now **clears Bonferroni on both** — with a **NEGATIVE**
IC (h=1 t −3.20 · h=5 t −2.90). **W1: that ledger is KR and does not transfer**; the honest US
statement is that the gate's third leg is **unmeasured here** and is, on the only market where it has
been measured, **backwards**. Registered as **`D270`**. **No gate is flipped this run** (P4).

## 3 · Cross-checks against the MACRO transmission matrix

**CONFIRM ①  Energy's expression is the refiner, not the integrated.** The matrix put Energy first on
`P62` (distillate-led crack). The sweep locates it precisely: **`MPC` is Energy's only admissible 🟢
and it is one of the board's two ✅clean-rise names** (FINRA short z **−0.71**). **`CVX`'s 🟢 is
velocity-lit and inadmissible.** ⇒ money is in the crack, not the barrel — the same split `P62`
argued from futures, reached independently from flow.

**CONFIRM ②  Information Technology's OW-side wind is BREADTH, and the sweep names the node.**
The matrix rested IT on `RSPT` beating `XLK` on all three windows. The sweep's **two admissible IT
greens are `COHR` (flow +0.990, the highest score on the 299-name board) and `LITE` (+0.817)** — the
**optical/interconnect layer**. **`NVDA`, `MRVL` and `CSCO` are all velocity-lit and inadmissible.**
⇒ **IT's strength is not the megacaps and is not even the AI-compute epicenter; it is optics.**
🚨 **And `cycle_registry.json` has NO ENTRY for that cycle** (28 days stale, `D250`) — **the two
highest-scoring names on the entire board sit in a cycle the desk's registry does not know exists.**

**CONFIRM ③  `M669` reproduces on a second date.** Financials' only admissible green is **`KKR`** —
alternatives/asset-management, exactly the node `M669` said the breadth **relocated** to when `R69`
withdrew *"the board's only breadth-led sector."* The sector's headline is still negative
(`eqflow −0.126` below `wflow −0.031`); the life is in the node, not the label.

**CONTRADICT ①  Industrials' "breadth 0.00, 0🟢/10🔴" is a filter artifact, and it is the largest
one on the board.** **25 of 50 Industrials names pass `OBV 매집 ∧ RS20 > 0`** — including
**`LMT` (RS20 +15.2, surge 0.78) · `AXON` (+15.7, 0.98) · `EMR` (+12.5, 0.93) · `RTX` (+10.8, 0.64) ·
`WAB` (+9.6, 1.00) · `NOC` (+7.9, 0.58) · `ETN` (+8.4, 0.66) · `GD` (+2.9, 0.52)** — **every one
blocked on `vol_surge` alone.** ⇒ **half of a sector the desk calls breadth-dead is quietly
accumulating**, and the accumulating half is **aero/defense + electricals**, which is `M667`'s node
and the object `D249` says the INDU OW− is actually on. **ROTATION must not read Industrials' 0.00
breadth as evidence.**

**CONTRADICT ②  Health Care's 0.00 breadth is the same artifact** — **15 of 32** pass
`OBV 매집 ∧ RS20>0`. The 08-14 demotion rested on Δ, not on the green count, so it is unaffected; but
any stage tempted to re-cite "0🟢/32" as demand evidence is citing volume.

**CONFIRM ④ — and this is the one absence that is REAL.** **Utilities: 0 of 15** pass
`OBV 매집 ∧ RS20 > 0`. **Not a filter artifact — nothing is accumulating.** That is the only sector on
the board where the flow axis and the tag agree from the bottom up. ⚠ It sits against `XLU` exc5
**+1.207 vs `SPY`** (2nd best of 11) in the two sessions hike odds fell — so **price turned while flow
did not**, which is exactly the disagreement `P61` predicts if the driver is changing.

## 4 · Shortlist composition — read as absences

11 names cleared `mcap ≥ $10B ∧ 🟢`; **5 survive the `D261` adjustment**. By sector the survivors are
IT 2 · FIN 1 · DISC 1 · ENRG 1.

**Zero shortlist names from: Industrials · Health Care · Materials · Utilities · Real Estate ·
Consumer Staples.** Diagnosed, one line each:
- **Industrials — FILTER ARTIFACT** (25/50 accumulating, all blocked on volume). Strongest absence on
  the board and it is **not evidence**.
- **Health Care — FILTER ARTIFACT** (15/32 accumulating).
- **Materials — PARTIAL ARTIFACT** (6/12 accumulating, incl. `NEM` `NUE` `FCX`). ⚠ But `P59`'s price
  evidence stands independently: ex-`NEM` EW exc5 **−2.097 vs `SPY`, 1 of 11 positive**. **Flow and
  price disagree here; the price axis is the A-grade one (D6).**
- **Real Estate — PARTIAL ARTIFACT** (4/12: `EQIX` `DLR` `CBRE` `IRM` — the data-centre node `M131`
  identified, accumulating while `XLRE` is the only duration leg that did NOT turn up on 5 days).
- **Consumer Staples — mostly real** (3/19).
- **Utilities — REAL** (0/15), as above.

⚠ **The general rule this run establishes: on a thin tape, a zero-shortlist sector is a volume
statement until someone checks `OBV 매집 ∧ RS20>0` underneath it.** Six sectors produced zero names
and **four of the six were artifacts.**

## 5 · Held-but-not-in-universe check — ✅ clean, 4th consecutive run

**11 of 11 US holdings are inside `us_top300` AND scored** (`ANET` `AVGO` `ETN` `HPE` `MET` `MPC`
`NDAQ` `NUE` `NVDA` `PSX` `RTX`). The `LNG`/`TSM` hole (12 consecutive runs) stays closed — neither is
held. ⚠ Caps are **31 days stale**, so `wflow` and every `top1_w` are **not** current-market-cap
weights.
⚠ **`EA` (`R56`) changed shape rather than being fixed**: after 8 runs of being scored while delisted,
it has now **dropped out of the scored set** (299 of 300) — so the Communication Services numbers moved
by **composition**, not by demand. Still in the universe file at day 31.

## 6 · 🚨 CYCLE_EXPOSURE GAP — handed to ALPHA

| Cycle | rank | epicenter | need | GAP |
|---|---|---|---|---|
| AI-compute / semiconductors | 1 | 16.54% | 12.0% | ✅ |
| **Energy / oil-refining (Hormuz + Russia crack)** | **2** | **7.10%** | **8.0%** | 🚨 **GAP, margin −0.898pp** |
| Missile-defense / rearmament | 3 | 5.77% | — | ⚪ no floor set |

★ **The GAP is on the cycle the tape just paid**: `XLE` exc5 **+7.271 vs `SPY`** (best of 11), crack at
the **95.2nd percentile of 250 days**, and Energy's only admissible 🟢 (`MPC`) is a **held** name.
⚠ **This is not `M146`'s mark-to-market drift** — that finding was about a ✅ clearing by 1.1bp with
nothing bought. This is a **GAP**, on a **−0.898pp** margin, in the **direction the flow is moving**.
**Handed to ALPHA's action bracket.**
⚠ **The registry is 28 days stale and rank-3 has no floor** (`D250`), so "rank 3, no GAP" for
missile-defense means *unmeasured*, not *fine* — and §3 CONTRADICT-① just found defense to be the
board's largest accumulating-but-blocked node.

## ✅ EXIT CHECK
- [x] `scoring` block read and quoted; **coverage 17.1% < 80% ⇒ "news axis dead this run" stated**,
      with the cause **probed, not assumed** (n=40: 85% valid / 0% genuinely quiet ⇒ **pipe**).
- [x] **Every `top1_flips_sign` sector listed with `top1` and `top1_w`** — **Information Technology
      /`NVDA`/19.4% · Industrials/`CAT`/8.7% · Materials/`LIN`/24.7%** (3 of 11; Health Care **exited**
      — `LLY` no longer flips the sign, so `wflow` is admissible for HLTH again). **Handed to ROTATION,
      which may not promote or demote those three on `wflow`.**
- [x] **Held-but-not-in-universe check run** — 11/11 inside and scored, no 🚨.
- [x] sweep done → `SECTOR_FLOW_US.json`; ranking read; **new 🟢 = `MRVL` `NFLX` (both velocity-lit,
      both inadmissible); lost 🟢 = `ALL` `DELL`** ⇒ **the day-over-day ignition signal is entirely
      inside the revoked axis and carries no information this run.**
- [x] `US_LIVE_SHORTLIST.json` written; FINRA short verdicts read (✅clean-rise `ABNB` `MPC` ·
      ⚡crowded-short `KKR` `NFLX` `NVDA`).
- [x] **CYCLE_EXPOSURE GAP read; the 🚨 is handed to ALPHA** (§6).
- [x] **No table here exists in the JSONs** — sector rows and per-name rows are cited by artifact.
      The only tables printed are the gate decomposition, the absence diagnosis and the GAP, none of
      which the JSON contains.
- [x] **Cross-checks stated with the side the money is on** — 4 confirms, 2 contradicts (§3), and
      **every absence diagnosed as artifact vs evidence** (§4).
