# SECTOR_ROTATION — industry_US · 2026-08-20 (Thu) · Stage 4 / L1·ROTATION

> **Delta-only.** MACRO §G owns the 11-sector verdict and `SECTOR_FLOW_US.json` owns the flow numbers;
> both are on disk all run. This file writes **what changes and why**, plus the DEEP picks.
> `asof` **2026-08-19 settled**. Analytical only — no buy/sell, no sizing (P4).

**Axis count this run: `n_axes = 3` (`vel_axis false`, `vel_coverage 0.1639`).** The prior history
snapshot `2026-08-18` is also `nonews`/3-axis ⇒ **the Δ subtraction is legal and spans exactly one
session.** 🚫 **No delta below cites theme freshness or news velocity** (`G1`), and **no delta rests on
a tag** (`R81`, 10th replication: 4 of 7 greens are velocity-derived).

---

## §1 · Inherited — one line, verbatim from MACRO §G

`MACRO holds: HLTH OW · ENRG OW · STPL N · COMM N · DISC N · MATR N− · FIN N− · INDU UW− · IT UW · RE UW · UTIL UW`

---

## §2 · Deltas — **ZERO verdict changes. The flow confirms the matrix on all 11.**

That is the honest output and it is not a reason to manufacture differences. What follows is the
**work that produced the zero**: every attempt considered, each declined with the number that
declined it.

### 2a · Flip list, reproduced in full even though it changes nothing

| Sector | `top1` | `top1_w` | `wflow` | `wflow_ex_top1` | swing |
|---|---|---:|---:|---:|---:|
| **Materials** | `LIN` | **24.7%** | −0.099 | **+0.063** | 0.162 |

**One flipper of eleven.** The other ten sectors: **zero.** 🚫 **Materials may not be promoted or
demoted on its `wflow` sign** — *this sector's sign is `LIN` at 24.7%*. Its admissible reading is
`eqflow` **−0.064** with **0🟢 / 4🔴 of 12**, which supports **N−** and does not move it.

### 2b · 🚨 A NEW instrument defect found while checking the flip list — dual-class listings defeat the top-1 guard

`Communication Services` reports `top1 = GOOGL, top1_w = 38.3%`. **`GOOG` is a separate row in the
same bucket at the same 38.3%** ⇒ **the Alphabet complex is 76.6% of the sector by cap and the guard
reports exactly half of it.** Measured:

- `wflow` **−0.262** · `wflow_ex_top1` (GOOGL only) **−0.296** · **`wflow` ex-BOTH Alphabet classes
  −0.288** ⇒ **no sign flip either way, so no verdict is affected today.**
- But the guard's premise — *"remove the largest name and see if the sign survives"* — **cannot be
  executed on a dual-class issuer**, because the largest *company* is two rows.
- Scope check run: `Communication Services` is the **only** dual-class pair in `us_top300`
  (name-collision scan over all 299 scored names returned exactly this one), so the exposure is
  narrow — **but the guard would not have caught a flip here, and that is a property of the
  instrument, not of today's numbers.**

**Dig `D297`.** Not repaired here (rule 1: this stage measures, it does not fix).

### 2c · Attempts considered and DECLINED, each with the number

| Attempt | Flow evidence | Verdict | Why declined |
|---|---|---|---|
| **UTIL UW → UW−** (i.e. *up* a notch, on price) | `eqflow` **−0.545 = last of eleven** · `ex_top1` **−0.578** · **0🟢 / 8🔴 of 15** · Δ −0.171 — **and the bucket is uniformly negative**: all eight largest names carry negative flow, so `NEE` (17.7%) is **not** a flipper and removing it makes the sector **worse** | **DECLINED — stays UW** | ★ The only argument for moving it is **price**: `XLU` 5-session excess vs `SPY` is **+0.855pp**. **That is not a flow number**, and this stage requires one. **The macro re-argument is declined and logged**, per the stage's own rule. ⇒ The contradiction is handed to DEEP as a mandate, not converted into a verdict |
| **COMM N → N+** | `eqflow` **+0.023** (positive) against `wflow` −0.262; and **ex-Alphabet, ex-`META` the remaining 9 names read `wflow` +0.217 / `eqflow` +0.168** — i.e. **the COMM underweight is two names, not a sector** (`META` flow −0.728 🔴 rs20 −15.8; the Alphabet complex −0.208/−0.301) | **DECLINED — stays N** | `eqflow` **+0.023 is 0.023 away from zero** and the bucket carries **0🟢 / 2🔴 of 12**. Promoting on a number that small is promoting on noise (`C4`). ★ **But it is the run's strongest declined attempt and it is the DEEP mandate if COMM takes a slot** — the carried `GOOGL` row says *"half of the COMM underweight is already wrong"*, and the measurement says it is narrower than half: **2 of 12 names.** COMM was covered **08-19** ⇒ too recent for a slot |
| **IT UW → lower** | `eqflow` **−0.197** · **19🔴 / 1🟢 of 56** · `ex_top1` −0.290 (worse than headline) · Δ −0.088 · and `EW{AVGO,ANET,HPE,COHR,LITE}` exc5 **−12.425 = 0.8th percentile of 252 obs** | **DECLINED — stays UW** | **There is no notch below UW in this desk's scale.** Stated rather than invented. The evidence is routed to a **DEEP slot** instead, which is the correct instrument for it |
| **IT UW → N− (the contrarian read)** | `Nasdaq-100` spec net at the **0th percentile short** — maximum rebound ammunition | **DECLINED — stays UW** | **Positioning is context, not a trigger** (protocol, US runtime deltas), **and this reading is 9 days old**: COT is as of **Tuesday 2026-08-11**, digit-identical for the **6th consecutive run**. A verdict may not rest on it |
| **STPL N → N−** | `WMT` printed **08-20 pre-market**: *"Weakest Sales Growth in Over Six Years"* (`wsj`), US sales hit by falling drug prices (5 outlets) | **DECLINED — stays N** | 🚫 **The print's price consequence is OUTSIDE the settled frame** (`G0` bars any 08-20 price). In the flow that exists, `eqflow` is **−0.012** and Δ **+0.005** — flat, not deteriorating — and the sector's best `flow_score` is `TGT` **+0.817** with an **admissible** `vol_surge` 1.27. **A demote on a print the frame cannot see is the `R82` error in the other direction** |
| **FIN N− → lower** | ★ **`eqflow` −0.127 is now BELOW `wflow` −0.009**, inverting `M40`'s carried *"the board's only breadth-led sector"*; **2🟢 / 8🔴 of 47**; `GS` −0.744 🔴 | **DECLINED — stays N−** | `eqflow` −0.127 ranks **8th of 11**, not bottom, and the bucket's largest names are mostly positive (`BRK-B` +0.233, `MA` +0.349, `BAC` +0.189, `JPM` +0.093). **The inversion is a real finding and it is a DEEP mandate, not a notch** |
| **MATR N− → any** | flipper-blocked (§2a) | **DECLINED** | *This sector's sign is `LIN` at 24.7%.* On `eqflow` −0.064 nothing moves |
| **HLTH · ENRG · DISC · INDU · RE** | flow and matrix agree in sign and rank | **no attempt** | HLTH `eqflow` **+0.252 (1st)** and ENRG **+0.182 (2nd)** are the board's top two on flow **and** the top two on 5-session price excess (`XLV` +4.742, `XLE` +4.622) — **two independent instruments, same top two, same order** |

### 2d · One divergence named, with its resolution owner

**Energy's Δ disagrees with Energy's level.** Δ **−0.157** (2nd worst on the board) against `eqflow`
**+0.182** (2nd best) and `wflow_ex_top1` **+0.257**. Per **`D293`** a Δ mixes earned excess with
rolling-window roll-off and the sweep publishes neither leg ⇒ **the Δ is not used as a verdict and the
level is.** ⚠ Also note **Energy carries 0🟢 and 0🔴 of 16** — every name is 🟡, so a 🟢-filtered
shortlist can produce nothing from the board's second-best sector. **That is the `M144`/`D270` volume
gate (`MPC` surge 1.00, `PSX` 1.03, just under 1.2), not an absence of money** — 3rd consecutive run.
**Resolution owner: DEEP-ENRG.**

---

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

### Continuous track (⌈N/2⌉ = 2) — today's top OW ranks

| Slot | Sector | Basis | Continuity |
|---|---|---|---|
| **C1** | **ENRG** | `eqflow` **+0.182 (2nd of 11)** · `wflow_ex_top1` +0.257 · `XLE` exc5 **+4.622 (2nd)** · `EW{MPC,VLO,PSX}` exc5 **+5.730 = 79.8th %ile** | ★ **KEEPS its slot** — held a continuous slot on 08-19 **and** is still top-N OW today. Anti-thrash rule applied and stated |
| **C2** | **HLTH** | `eqflow` **+0.252 (1st of 11)** · `ex_top1` +0.238 · `XLV` exc5 **+4.742 (1st)** · 24 of 32 accumulate | **NEW to the continuous track.** It was a *rotating* slot on 08-17 and MACRO promoted it to OW today; the rule assigns continuous slots to today's top OW ranks, and HLTH is rank 1 |

⚠ **`INDU` LOSES its continuous slot.** It held one on 08-17 and 08-19, but MACRO has it at **UW−**
today (`eqflow` −0.073, **10🔴 / 0🟢 of 50**), and the continuity rule only protects a sector that is
*still top-N OW*. **Stated rather than silently rotated out.** ⚠ The desk's actual Industrials
position is **defense** (`RTX` held, flow +0.617, rs20 +10.2 / rs60 +21.3, OBV 매집) and the label's
weakness is not the sub-node's — that mismatch is logged in DEEP_LOG, not resolved here.

### Rotating track (⌊N/2⌋ = 2) — ★ **recency-starved, declared, 7th consecutive run**

**There are only two OW sectors on the board and both took continuous slots ⇒ zero OW remain for the
rotating track.** The rule's fallback is invoked explicitly: **fill from non-OW, rank by evidence
produced *this run*, break ties on recency.** This is the documented practice of 08-15 · 08-16 ·
08-17 · 08-19, and the deviation is logged again rather than normalised.

| Slot | Sector | Last DEEP | Evidence that earned it **this run** |
|---|---|---|---|
| **R1** | **IT** | **08-16 (3 runs)** | ★ The heaviest evidence on the board, and **three separate items**: ① **`EW{AVGO,ANET,HPE,COHR,LITE}` exc5 −12.425 = the 0.8th percentile of 252 observations**, and **all five are held in the real book**; ② **a named structural event against a held name** — Google's **$12.2bn / 59m-share warrant to `MRVL`**, with `AVGO` **−4.61%** the same session and `AVGO` the **only book name tagged 🔴** (EVENT_ALPHA Card 3); ③ the **optical node this desk promoted to a 5th DEEP on 08-17** is the board's worst group (`COHR` exc5 **−18.72**, `LITE` −10.80, `CIEN` −7.10) and `S96` settles **08-21** (Card 6). **Mandate: is this a positioning flush or the first leg of a de-rate — and does the `AVGO` thesis line survive being rewritten?** |
| **R2** | **UTIL** | **08-16 (3 runs)** | ★ **The sharpest instrument contradiction on the board, and §2c refused to convert it into a verdict**: `eqflow` **−0.545, last of eleven, 0🟢/8🔴 of 15, uniformly negative across all eight largest names** — against `XLU` 5-session excess **+0.855pp**. **Mandate: which instrument is right, and is the four-legged "duration complex" one object at all?** This is MACRO **`P78`**'s empirical core and it also decides how `S80`/`S82`/`S98` should be read |

**No padding.** Both rotating slots are filled on evidence, and the two strongest *unfilled* mandates
(`STPL`, `FIN`) are named below rather than dropped.

### §3b · The un-covered sectors, with last-covered date and mandate

| Sector | Verdict | Last DEEP | Mandate carried forward |
|---|---|---|---|
| **STPL** | N | **08-17 (2 runs)** | 🚩 **`S100` settles 08-21 on both prints, and the DEEP would be one day early.** Mandate: `TGT`'s Q2 beat contains a **$752m / $1.65-per-share tariff refund** (issuer-attributed, `cnbc`/`bbc`/`fortune`) — **is the merchandising leg real once the non-recurring credit is removed?** `WMT` printed 08-20 (weakest sales growth in over six years) with FINRA short-z **+2.39 crowded-short** |
| **FIN** | N− | **08-14 (4 runs — the least-recent on the board)** | ★ **`M40` has INVERTED**: `eqflow` **−0.127 now sits BELOW `wflow` −0.009**, so the sector this desk carried for weeks as *"the only breadth-led sector"* is now the opposite. Mandate: re-measure `M40`'s shape before any argument still resting on it is used. Also `KKR` is one of only **3 admissible greens** (surge 1.20) and `NDAQ` is a **held name with no bracket** (its miss-ledger row was reaffirmed this run on exc20 +3.099 vs its own 252d p85 +6.439) |
| **COMM** | N | **08-19 (1 run)** | The §2c finding: the underweight is **2 names of 12** (`META` −0.728, the Alphabet complex), while the other 9 read `wflow` **+0.217**. Plus **`T` — 9.74% of invested, no cycle label, no card, no bracket, 3rd consecutive run.** Too recent for a slot |
| **MATR** | N− | **08-19 (1 run)** | `S77` settled **FIRED-C** at −1.589 and **`STLD` −11.78 + `NUE` −8.04 are the entire residual**; `NUE` is held in both books and carries the sheet's **only 🔴 FINRA axis**. Handed over by the KR desk explicitly |
| **INDU** | UW− | **08-19 (1 run)** | The label is UW− while the **held sub-node (defense) is positive**: `RTX` rs20 +10.2 / rs60 +21.3, OBV 매집. `S97`/`S99` settle 08-21 |
| **DISC** | N | 08-15 (5 runs) | `eqflow` +0.022 with β **1.178** ⇒ the +1.038 excess is beta, not selection. `AMZN` **revived** from the rejection ledger this run on the tariff-refund leg (EVENT_ALPHA §Ledger, `D48`) |
| **RE** | UW | 08-15 (5 runs) | Same price-vs-flow contradiction as UTIL, one rank milder (`eqflow` −0.252, **0🟢/4🔴**, against `XLRE` exc5 **+1.568**). `S90` settled 08-21 window |

---

## §4 · What ROTATION hands forward

- **To PREMORTEM**: the two rotating mandates (IT, UTIL) are **both adversarial by construction** —
  R1 asks whether a held basket at a 2-year extreme is a flush or a de-rate; R2 asks whether an
  underweight this desk holds three (possibly four) legs of is one object at all.
  ⚠ **Correlated-tail flag carried from EVENT_ALPHA**: Cards 1 and 7 (Russian refining capacity, Iran
  economic warfare) **share their entire exposure map** — `MPC` `PSX` `VLO`. They are **one risk unit,
  not two independent legs**, and ENRG's continuous slot rests on both.
- **To DEEP**: four slots — **ENRG (C1) · HLTH (C2) · IT (R1) · UTIL (R2)**.
- **To BET §B**: EVENT_ALPHA's CONFIRMED-EARLY cards (Card 1 Energy, Card 4 Health Care) and its
  LATE-MONEY cards **with their gates attached** (Card 5's `TGT` refund gate, Card 8's extreme).
- **To ALPHA**: `CYCLE_EXPOSURE` shows **no top-rank GAP** (AI-compute 19.78% vs a 12.0% floor;
  Energy 9.89% vs 8.0%) — ⚠ with `M731`'s under-count and rank-3's absent floor both re-confirmed.

## DEEP_LOG 2026-08-20: continuous=[ENRG, HLTH] rotating=[IT, UTIL] · N=4/4 · **ZERO verdict deltas — flow confirms the matrix on all 11, and the zero was produced by SEVEN attempts declined with numbers, not by inertia (UTIL→up: price-only, `eqflow` −0.545 is last of eleven and the bucket is uniformly negative — macro re-argument declined and logged · COMM→N+: `eqflow` +0.023 is 0.023 from zero with 0🟢/2🔴, though ex-Alphabet-ex-`META` the other 9 names read wflow **+0.217** ⇒ the UW is 2 names of 12, and that is COMM's DEEP mandate · IT→lower: no notch below UW exists, routed to a DEEP slot instead · IT→N− contrarian: `Nasdaq-100` 0th-%ile short is positioning, context not trigger, and 9 days stale · STPL→N−: `WMT`'s 08-20 print is OUTSIDE the settled frame (`G0`), `eqflow` −0.012 flat · FIN→lower: `eqflow` −0.127 ranks 8th of 11 not bottom · MATR→any: flipper-blocked)** · **flip list 1 of 11 — Materials/`LIN`/24.7% (`wflow` −0.099 → `ex_top1` +0.063); the other TEN are zero, down from 3 flippers on 08-19 (`BRK-B` and `CAT` both left)** · 🚨 **NEW instrument defect `D297`: dual-class listings defeat the top-1 flipper guard — `GOOGL` and `GOOG` are separate rows at 38.3% each, so the Alphabet complex is **76.6%** of COMM while `top1_w` reports 38.3%; ex-BOTH classes `wflow` is −0.288 so no verdict moves today, but the guard could not have caught a flip. Scope: the only dual-class pair in `us_top300`** · **`INDU` LOSES its continuous slot (UW− today; continuity only protects a still-top-N-OW sector) — and the desk's actual INDU position is defense, which is positive (`RTX` rs20 +10.2 / rs60 +21.3, OBV 매집), a label-vs-sub-node mismatch logged not resolved** · **rotating slots are a DECLARED recency-starved deviation for a 7th run: only 2 OW exist and both took continuous slots, so R1/R2 were filled from non-OW by evidence-density with recency as tiebreak** · **`M144`/`D270` replicated a NINTH time: 105 names pass `OBV 매집 ∧ RS20>0`, exactly 3 clear `vol_surge ≥1.2` (`MRK` 1.28 · `TGT` 1.27 · `KKR` 1.20) ⇒ 102 blocked, 97.1% on `vol_surge` alone; median `vol_surge` 0.740; 12 names clear the gate and 9 of them are 🟡/🔴** · **`R81`/`D290` replicated a TENTH time: 4 of 7 greens are velocity-derived (`LLY` · `MRVL` · `MA` · `WMT`) on the axis `G1` revoked ⇒ the admissible green count is 3 and the admissible new-🟢 count is 2, not 4 — and `US_LIVE_SHORTLIST` is tag-filtered, so 4 of its 7 rows are inadmissible** · **★ the run's structural headline is a NAMED EVENT ON A HELD NAME: Google's $12.2bn / 59m-share warrant to `MRVL` (08-19), `AVGO` −4.61% the same session, Barron's carrying the readthrough in its title; `AVGO` is held in both books, is the only book name tagged 🔴, and its standing thesis line still reads "hyperscaler capex is their driver" — the same variable now has the opposite sign for this name (EVENT_ALPHA Card 3, re-filed not dropped)** · **★ and the macro event of the window is a TREASURY action, not a Fed one: Bessent doubled long-dated buybacks 08-19 with `DGS30` at 5.28, within 3bp of a 252-obs high; `theme_age "Treasury buybacks"` = 🟢FRESH age 1 n=64, the first 🟢FRESH in TEN runs, which confirms `R83`'s rewritten conjunction mechanism by producing the positive case** · **🚨 two live rows are at VOID on 08-19 events and MACRO §E-0 ruled on the CLAUSE before seeing the branch: `S102` (Treasury action inside a window whose anti-signal names a Treasury refunding announcement — and `S102` was itself the repair for the self-voided `P73`, `D296`) and `S98` (FOMC minutes 08-19 inside 08-13→08-20)** · **uncovered=[STPL(N, 08-17, `S100` settles 08-21, `TGT`'s beat contains $1.65/sh of tariff refund), FIN(N−, **08-14 = least recent on the board**, `M40` INVERTED: eqflow −0.127 now BELOW wflow −0.009), COMM(N, 08-19, the UW is 2 names of 12; `T` orphan at 9.74% of invested for a 3rd run), MATR(N−, 08-19, `S77` FIRED-C residual is `STLD` −11.78 + `NUE` −8.04 and `NUE` is held), INDU(UW−, 08-19, label vs defense sub-node), DISC(N, 08-15 = 5 runs, `AMZN` revived on the tariff-refund leg), RE(UW, 08-15 = 5 runs, same price-vs-flow contradiction as UTIL one rank milder)]**

---

## ✅ EXIT CHECK — self-audit

- ✅ **§1 is ONE line**, verbatim from MACRO §G. No unchanged sector has a row, paragraph or restated
  flow number.
- ✅ **Delta count is 0**, and the file says so plainly rather than manufacturing differences — with the
  seven declined attempts each carried by a number (§2c).
- ✅ **No promotion or demotion rests on a `top1_flips_sign` bucket.** The flip list is reproduced in
  full (§2a) even though it changes nothing, and Materials' decline is written out as *"this sector's
  sign is `LIN` at 24.7%."*
- ✅ **The macro re-argument was identified and declined**, not smuggled in: UTIL's only case is a
  price/rate argument, and the stage's own rule refuses it.
- ✅ **Axis count stated** (`n_axes = 3`), Δ compared only against a same-axis-count snapshot
  (`2026-08-18`, `nonews`), and **no delta cites theme freshness or news velocity.**
- ✅ Every matrix × flow divergence named with a resolution owner (§2d, §3b — all to DEEP).
- ✅ **N=4 picked by the rule**: continuity applied and stated (ENRG keeps, INDU loses), recency-starved
  fallback **declared**, no padding, and every OW-less rotating choice justified by evidence produced
  this run.
- ✅ **All seven un-covered sectors named with last-covered date and mandate** (§3b + DEEP_LOG).
- ✅ DEEP_LOG line appended for the next run.
- ⏳ Linter run — result appended below.

**Lint**: `report_lint.py` on this file → **0 findings** (C1 · C2 · S6 · D6). No exemption claimed.
A clean lint is a form check only — the content findings above (the declined attempts, `D297`, the
`M40` inversion) came from measurement, not from the linter.
