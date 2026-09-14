# SWEEP_READ — industry_US · 2026-08-21 · Stage 4 / L1·SWEEP

> **The reading, not a second copy of the data.** Numbers live in `SECTOR_FLOW_US.json` ·
> `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.json`. This file holds only what those cannot say.
> Settled bar **2026-08-20** · sweep `asof` **2026-08-20** · Δ spans **one session (08-19 → 08-20)**.

## 0 · Instrument health line, read BEFORE the numbers

`§scoring`: **`vel_axis` false · `vel_coverage` 0.1672 (50/299) · `n_axes` 3 · `dropped_missing_axis`
0.** All 299 names scored on the **same three axes** ⇒ the D225 per-name scale defect is not present,
and Δ is legal (`G2`). **The low coverage is evidence about the pipe, not about the news** — the
falsification probe returned **40/40 valid** and the CLI **3523 ×3** while the sweep ran
(`PREFLIGHT_US §G1`).

**Book-coverage invariant: 11/11 US paper-book names are in the universe AND scored; 6/6 real-book US
names likewise.** The `TSM`/`LNG` failure of 2026-08-10 does not recur. **`EA` remains the one
universe row the sweep cannot measure — 9th run.**

## 1 · Universe headline — three numbers

**n = 299 · `wflow` −0.105 · 7 🟢 : 68 🔴.**

## 2 · Cross-checks against the MACRO transmission matrix

**CONFIRMS ×2, CONTRADICTS ×2, and the contradictions are the two promotions MACRO made today.**

| Matrix call | Sweep says | Verdict |
|---|---|---|
| **ENRG OW** | `wflow` +0.169 **and** `eqflow` +0.160 — **rank 1 on both**, the only sector where the cap-weighted and the breadth reading agree at the top | ✅ **CONFIRMED on both axes.** ⚠ But **breadth is 0.06 and green:red is 1:1** — the agreement is between two aggregates, not a broad advance |
| **HLTH OW** | `eqflow` +0.159 > `wflow` +0.150 ⇒ **breadth-led, not mega-cap-narrow** | ✅ **CONFIRMED, and on the better half.** ⚠ 1🟢/3🔴, breadth 0.03 — thin under the price |
| **MATR N (promoted today from N−)** | `eqflow` **−0.010** · **0🟢 / 2🔴** · breadth **0.00** · Δ +0.107 | 🚨 **CONTRADICTED. The money is not there.** MACRO promoted on exc5 rank 3 (+2.175) and a FINRA short-covering reversal (`NUE` z +1.99 → −2.33, `STLD` −4.40). **Short covering is not accumulation, and the sweep's breadth axis says so.** The notch survives only because it rests on a B-grade axis MACRO named; **ROTATION must not add a second notch on flow** |
| **RE N− (promoted today from UW)** | `eqflow` **−0.231** (rank 10 of 11) · **0🟢 / 4🔴** · breadth **0.00** | 🚨 **CONTRADICTED, harder than Materials.** exc5 is +1.876 (rank 4). **Price up, flow last-but-one — the same contradiction MACRO already flagged**, and the sweep is the side that says the money is against it |
| **UTIL UW** | `eqflow` **−0.606**, `ex_top1` −0.648, **0🟢 / 12🔴** — worst on the board by a distance | ✅ **CONFIRMED for a second run.** This is `P78`'s strongest single row |
| **IT UW** | `eqflow` −0.208, **21 red of 56** — worst breadth in absolute count | ✅ CONFIRMED |
| **COMM N** | `eqflow` **+0.151** (rank 3) against **breadth 0.00 — zero green of 12** | ⚠ **The two admissible axes disagree with each other.** `wflow` is flipper-owned (`G3`) and unusable. **Neither number promotes anything; the disagreement is the finding** |

★ **The board-level caution MACRO raised is measured here**: **6 of 11 sectors print a positive
`eqflow`** on a session the benchmark fell. **An absolute-`eqflow` rule would promote most of the
board** (`D302-KR` in form). Both of today's promotions were made on rank and on non-flow legs, and
both are contradicted by the flow axis — **that is stated, not averaged.**

## 3 · Shortlist composition — the ABSENCES are the finding

**7 names of 299 clear `mcap ≥ $10B ∧ 🟢`. Six of the eleven sectors produce ZERO**: Industrials,
Utilities, Real Estate, Materials, Communication Services, Consumer Discretionary.

⚠ **But the filter is the revoked axis, so the absences must be diagnosed before they are cited**
(`R81` / `D290`). Measured on this board:

- **3 of the 7 greens are velocity-derived and therefore inadmissible as tags**: `MRVL`
  (`vol_surge` 0.77, velocity 1.62) · `MA` (0.87, 1.25) · `CVX` (0.94, 1.21). **Their 🟢 rests on the
  axis `G1` revoked.** The other four (`MSTR` 1.42 · `MRK` 1.41 · `TGT` 1.40 · `COIN` 1.36) clear the
  volume bar on their own.
- **`M144` replicates for at least a tenth measurement**: **92 names pass `OBV 매집 ∧ rs20 > 0`; 7 are
  🟢; 85 are blocked and 100% of them by `vol_surge` < 1.2 alone.**
- ⇒ **The six empty sectors are mostly a volume-gate artifact, not an absence of money.** The clean
  statement is: *no name in those six sectors combined accumulation, positive 20-day relative strength
  **and** a 1.2× volume surge.* It is **not**: *no money went there.*

★ **The 2026-07-21 refiner artifact recurs exactly, on the desk's own overweight.** **`MPC` +0.700,
`PSX` +0.733, `VLO` +0.506 are all OBV 매집 with positive `rs20` — and all three are 🟡**, because
`vol_surge` reads **1.06 / 1.12 / 0.71** against a 1.2 bar. **The rank-1 sector's core names cannot
appear on their own desk's shortlist.** Energy's single entry is **`CVX`**, and `CVX`'s 🟢 is one of
the three velocity-derived ones. ⇒ **Energy's shortlist presence is one inadmissible tag; its real
evidence is `eqflow`, `rs60` and the crack, none of which the shortlist reads.**

**Short-pressure enrichment (the US substitute for KR's investor actuals, `[FINRA 08-20]`)**:
✅ clean-rise **`MSTR` (z −1.87) · `CVX` (−0.54)** · ⚡ crowded-short **`COIN` (z +2.20)** — squeeze
fuel, turn-conditional, **never a buy signal alone (`D6`)** · △ normal for the rest.

## 4 · New-🟢 ignitions — three, and two are the same trade

**`MSTR` (Δ +0.601) · `COIN` (Δ +0.873) · `CVX` (Δ −0.011).**
⚠ **`MSTR` and `COIN` are one object wearing two GICS labels** (Information Technology and
Financials) — both are crypto-beta, and the day's #6 event is *"Bitcoin rockets past $71,000"*
(43 articles / 11 outlets). **Counting them as two ignitions in two sectors would be the
`W5`/diversification-by-label error.** `COIN` carries the board's largest single-session Δ (+0.873)
**and** a crowded-short z of +2.20 — a squeeze shape, which is exactly what the enrichment axis is for.
⚠ **`CVX`'s "ignition" has a NEGATIVE Δ (−0.011)** — it crossed the tag boundary without improving.
A new-🟢 with a negative delta is a gate artifact and is recorded as one.

## 5 · Cycle exposure — no GAP, and the registry is why that is not reassuring

`CYCLE_EXPOSURE.md`: **AI-compute epicenter 19.8% (need ≥12.0) ✅ · Energy/refining 9.78% (need ≥8.0)
✅ · Missile-defense 5.73% (no floor set) ⚪.** Real book total ≈ **$11,143**, invested **$6,735**.

🚨 **`D250`/`M731` stands and bears directly on this ✅**: `cycle_registry.json` carries **no row for
the optical/interconnect cycle**, which this desk holds (`LITE`, `COHR` in the real book) and which
`S86`/`S96` bracket. **The reported "any-layer 23.57%" is a floor, not a measurement** — the GAP check
**cannot fire** on a cycle it cannot see. Registry maintenance is a human item (P5).

## 6 · Hand-off to ROTATION

1. **Both of MACRO's promotions are contradicted by the flow axis.** Materials and Real Estate went up
   one notch each on price and on FINRA; `eqflow` is negative and breadth is **0.00** in both.
   **No second notch on flow.**
2. **The two OW sectors are confirmed on both axes**, and both are thin underneath (breadth 0.06 /
   0.03).
3. **The shortlist is not a quality signal today** — 3 of 7 tags are velocity-derived and 85 names are
   blocked by the volume gate alone. **Absences may not be read as "no money".**
4. **The refiner trio cannot reach its own desk's shortlist**, on the sector the desk ranks first.
5. **`MSTR` + `COIN` are one risk unit**, not two sector ignitions.
