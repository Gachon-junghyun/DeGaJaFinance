# SWEEP_READ — industry_US · 2026-08-16 · Stage 4/11 (L1·SWEEP)

> **The reading, not a second copy of the data.** Numbers live in `SECTOR_FLOW_US.json` ·
> `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.json`. No table the JSON already holds is reprinted here.
> Benchmark **`SPY`** named inline on every relative number (C1).

## 1 · Universe headline — three numbers

**n = 299 scored (300 requested) · `wflow` −0.132 · 9 🟢 / 60 🔴.** `asof` **2026-08-14**.

## 2 · 🚨 Instrument health, read BEFORE the numbers (the `scoring` block)

`§scoring` = `{"vel_axis": false, "vel_coverage": 0.1672, "n_axes": 3, "scored": 299, "dropped_missing_axis": 0}`
plus the sweep's own 🚨 line: `[axis] velocity 측정 50/299 = 16.7% → 속도축 제외(전원 3축) · 기준 80%`.

**The news axis is dead in this run, and the cause is the PIPE, not silence — probed, not assumed.**
A seeded n=40 re-probe of the 249 names the sweep recorded as `velocity: None` returned **24 valid
(60.0%) · 16 pipe-fail (40.0%) · ZERO genuinely quiet** (probe 20:24 KST). Cumulative over two runs:
**0 of 80 silent names were actually quiet.** Worked examples from the sweep's own dead list:
`C` 7d 201 / 30d 1,053 → 0.82 · `MSTR` 91/365 → 1.07 · `PSX` 36/124 → 1.24 · `SLB` 1/12 → 0.36.
⇒ **`flow_score` is a 3-axis score, and that fact travels on the same line as every conclusion below.**

### 2a · ★★★ The run's natural experiment — the 🟢 set moved with ZERO price change

This is `D261` demonstrated instead of argued, and the weekend supplied the control:

| | 08-15 run | **08-16 run** |
|---|---|---|
| Names with an identical `last` price | — | **299 / 299** |
| Names whose `flow_score` changed | — | **0 / 299** |
| **🟢 count** | **11** | **9** |
| Dropped | — | **`NVDA` · `MRVL`** |
| Added | — | **none** |

The cause is exact: `NVDA` velocity **1.20 → 1.16**, `MRVL` **1.20 → 1.10** — both crossed the 1.2 gate.
Every other input is identical to the digit (`NVDA` flow 0.458, RS20 +6.6, `vol_surge` **0.73**;
`MRVL` flow 0.378, RS20 +13.2, `vol_surge` **0.48**).

★ **Read what that means.** `NVDA` is the **G3 flipper that owns Information Technology's entire
`wflow` sign** (19.4% weight; ex-`NVDA` the sector reads −0.082). It lost its 🟢 to a **4-basis-point
move in an article-count ratio**, produced by a bridge measured to flicker on a **minute** timescale,
**on a day when no market was open.** And with `vol_surge` at 0.73 it could **never** have been green on
the 3-axis path — it was a **velocity-only** green the whole time.
⇒ **A green count is not a demand measurement. It is 2 parts price and 1 part transport uptime.**

### 2b · `D261` decomposition of today's 9 greens (ROTATION may not count a green before reading this)

**5 of 9 are producible from `OBV 매집 ∧ RS20>0 ∧ vol_surge≥1.2`** — `COHR` · `KKR` · `ABNB` · `LITE` ·
`MPC`. **4 of 9 are not** — `NFLX` · `CVX` · `CSCO` · `BAC` — and **all four carry a velocity value**.
Velocity coverage is **16.7%** of the universe but **44.4%** of the greens ⇒ a **2.66× over-representation**
of a survivor sample the PREFLIGHT forbids citing (08-15 was 3.19×, 08-13 2.6× — **third replication**).
⇒ **The admissible green count is 5, not 9.** ⚠ `CSCO` is 🟢 on **RS20 −4.7 — negative — for a third
consecutive run**.

### 2c · `M144` replicates a **SEVENTH** time, at the same record size

**110 names pass `OBV 매집 ∧ RS20>0`. 102 are not 🟢. 100.0% of those 102 are blocked by `vol_surge`
alone.** Two markets, seven dates ⇒ **code structure, not market structure**.
★ **And `D270`'s explanation holds on re-measurement**: the whole tape is thin (median last-bar volume
**0.649×** the 20-day average, after 0.732×), so the ratio's denominator carries a busier past and the
gate closes **board-wide at once**. ⇒ **"breadth 0.00" this week is a statement about VOLUME, not
about demand.** Any sector read that leans on breadth being zero is leaning on a volume artifact.

## 3 · G3 flippers handed to ROTATION (binding — no promotion or demotion on their `wflow`)

**3 of 11**: Information Technology (`NVDA`, **19.4%**) · Industrials (`CAT`, **8.7%**) ·
Materials (`LIN`, **24.7%**). Rows are in `SECTOR_FLOW_US.json §sector_rotation`.
⚠ Identical set and identical numbers to the 08-15 run — **that is one observation read twice**, not a
structure confirmed. ⚠ Every `top1_w` is computed from a **32-day-old** market-cap file.

## 4 · Cross-checks against the MACRO matrix — what the money CONFIRMS and what it CONTRADICTS

**✅ CONFIRMS · Energy (matrix rank 1, `P66`).** The only sector where flow and narrative agree and
where the narrative moved this run. `eqflow +0.102` and `breadth 0.12` are **both the highest of
eleven**, and Energy is **not a flipper** (ex-`XOM` `wflow` +0.205 at a 30.5% weight), so the OW does
not depend on a revoked axis. `MPC` is the sector's **only admissible 🟢** and carries a FINRA
**clean-rise** reading (short z **−0.71**) with RS20 +9.3 / RS60 +29.3 vs **`SPY`**.

**⚠ CONTRADICTS · Industrials (matrix rank 3, `D249`).** **Industrials has the board's HIGHEST
accumulation count — 25 of 50 pass `OBV 매집 ∧ RS20>0`, more than IT's 22 of 56 — and produced ZERO
shortlist names.** Its `eqflow` is −0.007 and `breadth` 0.00. **A sector cannot be simultaneously the
board's broadest accumulation and its emptiest shortlist unless the filter is the thing being measured**
— and §2c says it is: 100% of the block is `vol_surge`. ⇒ The matrix's "OW-side wind on an unverified
object" and the flow data are **not in conflict about direction; they are in conflict about the
instrument**. `D249` is now **5 runs old** and this is the number that should end it.

**⚠ CONTRADICTS · Health Care (matrix rank 4, Neutral).** **15 of 32 accumulating** — the third-highest
share on the board (46.9%) — against `breadth 0.00` and Δ −0.103, the worst of eleven. Same diagnosis,
same instrument. **The 0.00 is not evidence of absence.**

**⚠ CONTRADICTS · Real Estate (matrix rank 11, UW).** Every aggregate axis agrees with the UW, yet
**4 of 12 accumulate — `EQIX` `DLR` `CBRE` `IRM`**, which is exactly `M131`'s measured **data-centre
unit**, not the tower/duration unit the UW was written about. ★ `P67` supplies the variable that should
adjudicate it (cost of capital, via the $70bn shadow-credit story), and `HY OAS` at the **10.3rd
percentile** currently argues **against** the UW's premise.

**✅ CONFIRMS · Utilities (matrix rank 10, UW).** **0 of 15 accumulate.** ★ **This is the only zero on
the board that is real rather than a `vol_surge` artifact** — it survives the §2c correction, because
the block is at the OBV/RS stage, not the volume stage. Utilities is the one sector where "the money is
not there" is a measurement.

**⚠ CONTRADICTS the shortlist's own tag filter · Consumer Staples.** **3 of 19 accumulate** — the
board's lowest share (15.8%) — which agrees with UW−. No contradiction, recorded for completeness.

## 5 · Shortlist composition — the ABSENCES, each diagnosed

9 names cleared `mcap ≥ $10bn ∧ 🟢`. Rows are in `US_LIVE_SHORTLIST.json`.

| Sector | Shortlist names | Accumulating (`OBV 매집 ∧ RS20>0`) | Diagnosis of the absence |
|---|---|---|---|
| **Industrials** | **0** | **25 / 50 — board's highest** | 🚨 **Filter artifact, 100% `vol_surge`.** The largest absence on the board is the least informative one |
| **Health Care** | **0** | 15 / 32 | 🚨 **Filter artifact**, same mechanism |
| **Materials** | 0 | 6 / 12 | ⚠ **Mixed** — 50% accumulating but `eqflow −0.114`; the flipper (`LIN`) blocks the only cap-weighted read. `unknown` (C3) |
| **Real Estate** | 0 | 4 / 12 | ⚠ **Partial artifact** — the 4 are one measured unit (`M131` data-centre), so the absence hides a sub-sector, not a sector |
| **Utilities** | **0** | **0 / 15** | ✅ **Evidence, not artifact.** The only absence on this board that means what it looks like |
| **Consumer Staples** | 0 | 3 / 19 | ✅ **Evidence** — lowest accumulation share on the board |
| IT | 3 (`COHR` `LITE` `CSCO`) | 22 / 56 | ⚠ Only `COHR`/`LITE` are admissible; `CSCO` is a velocity green on **negative RS20** |
| Energy | 2 (`MPC` `CVX`) | 6 / 16 | `MPC` admissible; `CVX` is a velocity green (`vol_surge` 0.95) |
| Financials | 2 (`KKR` `BAC`) | 15 / 47 | `KKR` admissible and is `M669`'s relocated breadth node; `BAC` is a velocity green (`vol_surge` 0.73) |
| Consumer Disc. | 1 (`ABNB`) | 8 / 28 | Admissible; **RS60 +34.5 vs `SPY`, the best in the exposure set**, inside a sector the matrix reads UW-side |
| Comm. Services | 1 (`NFLX`) | 6 / 12 | Velocity green (`vol_surge` 0.63) and the run's **only** `new_green` (Δ +0.48) — ⚠ a `new_green` produced by the revoked axis is **not** an ignition |

**Short-pressure verdicts read** (`us_flow` FINRA z, the US substitute for an investor-type feed —
context, never a trigger): ✅ clean-rise **`ABNB` (−0.94)** and **`MPC` (−0.71)** · ⚡ crowded-short
**`KKR` (+1.62)** and **`NFLX` (+1.69)** — squeeze fuel conditional on a turn, never a standalone read.

## 6 · Held-but-not-in-universe check — ✅ clean, fifth consecutive run

**11 / 11 US holdings are inside `us_top300` AND actually scored** (verified against `§names`, not just
the CSV): `ANET · AVGO · ETN · HPE · MET · MPC · NDAQ · NUE · NVDA · PSX · RTX`. **Zero "held but
unmeasurable" names.** `LNG`/`TSM` remain closed (neither held).
⚠ Two universe holes are still open and both were named by earlier stages, not this one: the **tankers**
(`STNG·FRO·INSW·DHT·TNK`) and **`HII`**, the pure-play US Navy shipbuilder — outside `us_top300`, so no
flow/RS/OBV/short axis exists for them. ⚠ `us_top300.csv` is **32 days old** (limit ≤8) and
`us_all_v2_candidate.csv` sits unpromoted (human decision, P5).

## 7 · CYCLE_EXPOSURE GAP → handed to ALPHA

🚨 **`Energy / oil-refining (Hormuz + Russia crack)`, rank 2: epicenter exposure 7.1% vs a required
8.0% ⇒ margin −0.898pp.** Book touches the cycle only through the refining pair (`MPC`, `PSX`); there is
beta to the *consequence* and none to the *engine*.
⚠ **The number is identical to the 08-15 run to three decimals** — the book did not trade and prices did
not move, so this is **the same GAP measured twice, not a widening one**.
★ **The tension worth handing on**: this GAP sits on the **rank-2 cycle whose narrative strengthened
most this run** (`P66`: five dated Russian refining strikes in six days), while the same cycle's
positioning is **`WTI` spec at the 18th percentile SHORT**, dated 08-11 — *before* the escalation.
✅ Rank 1 (AI-compute) clears at **16.54%** vs a 12.0% floor. Rank 3 (missile-defense) has **no floor
set** ⇒ `⚪ n/a`, which is `D250` — the registry is **29 days stale** and still has **no entry for
either cycle this desk actually found** (optical/interconnect, custom AI silicon).

## ✅ EXIT CHECK

- [x] 🚨 **`scoring` block read and quoted** — `n_axes` 3 · `vel_coverage` **16.7%** · `dropped_missing_axis` 0.
      Coverage < 80% ⇒ this file states **"news axis dead this run"** and names the cause as **pipe, not
      silence**, having **actually probed it** (24/40 valid, 0/40 genuinely quiet).
- [x] **Every `top1_flips_sign` sector listed with its `top1` and `top1_w`** (§3), handed to ROTATION as
      binding.
- [x] **Held-but-not-in-universe check run** (§6) — 11/11 inside and scored; the two open universe holes
      (tankers, `HII`) named as 🚨 rather than left for a later stage.
- [x] **Sweep done → `SECTOR_FLOW_US.json`**; sector ranking and the run's only `new_green` (`NFLX`)
      read — **and the `new_green` is disclosed as velocity-produced, i.e. not an ignition**.
- [x] **`US_LIVE_SHORTLIST.json` written**; FINRA short-pressure verdicts read (§5).
- [x] **`CYCLE_EXPOSURE` GAP read** (§7) and the 🚨 handed to ALPHA's action bracket.
- [x] **No table in this file exists in the JSONs** — the 11-sector rows and the per-name shortlist rows
      are cited by artifact. The tables here are **derived cross-cuts** (accumulation counts, the
      green-set diff, absence diagnoses) that no JSON contains.
- [x] **At least one cross-check that confirms or contradicts the MACRO matrix** — §4 gives **two
      confirmations** (Energy, Utilities) and **three contradictions** (Industrials, Health Care, Real
      Estate), each with the side the money is on.
- [x] **Shortlist absences read and each diagnosed as evidence vs filter artifact** (§5) — **2 real
      absences** (Utilities, Staples), **2 artifacts** (Industrials, Health Care), **2 partial/unknown**
      (Materials, Real Estate).
