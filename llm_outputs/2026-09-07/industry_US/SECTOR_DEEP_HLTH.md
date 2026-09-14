# SECTOR_DEEP_HLTH — Health Care · industry_US · 2026-09-07 (Mon, US Labor Day)
### CONTINUOUS TRACK (deep-dived 09-06, 09-05, 09-02, 09-01 …) ⇒ **leads with the DELTA**

> Structure carried by reference to `llm_outputs/2026-09-06/industry_US/SECTOR_DEEP_HLTH.md`.
> ⚠ **No new price session** (`asof` 2026-09-04, third run). **P4: no sizing, no buy/sell language.**

---

## 0 · THE DELTA — the sector's headline breadth number is **wrong by a factor of ~23**, and this run measured it

Every prior run has read Health Care through `breadth = 0.03` (**1 🟢 of 32**) and treated it as a
sector carried by one name. **That number is a `vol_surge` gate artifact, and the gate's cut-point is
now known** (`D561`).

| breadth measure | value | what it counts |
|---|--:|---|
| **🟢-tag breadth** (the carried number) | **1 / 32 = 3%** | names clearing `vol_surge` ≈1.2 |
| ★ **OBV-accumulation breadth** | **23 / 32 = 72%** | `obv_state == 매집` |
| **positive `flow_score`** | **24 / 32 = 75%** | the composite, velocity-free |
| **positive `rs60`** | **21 / 32 = 66%** | 60-session relative strength vs `SPY` |

★★ **Only ONE name in the entire sector has `vol_surge` ≥ 1.2: `MDT` at 1.47.** The next highest are
`A` 1.16, `ALNY` 1.03, `UNH` 0.96 — **every other name in a 32-name sector trades below the gate.**
⇒ The 🟢 count is not measuring participation; it is measuring **whether Health Care is a
high-turnover sector**, which it is not. **Nine names clear flow > +0.5 **and** OBV > +0.15 **and**
`rs20` > 0 and are excluded from 🟢 by `vol_surge` alone**: `ALNY` `MRK` `GILD` `PFE` `A` `AMGN`
`JNJ` `REGN` `VRTX`.

⇒ **This is the third sector this run has found mis-measured by the same gate** (Utilities, Staples,
Health Care) and it is the cleanest case, because here the gate excludes **nine** merit-passing names
rather than two. **Handed to ROTATION and BET: Health Care's "one-name breadth" reading is retired.**

---

## 1 · Flow — node decomposition (sector row by reference to `SECTOR_FLOW_US.json`)

| node | n | eqflow | OBV mean | accumulating | rs20 | rs60 | names (flow desc) |
|---|--:|--:|--:|--:|--:|--:|---|
| ★ **Biotechnology** | 6 | **+0.519** | **+0.261** | ★ **6/6** | **+10.6** | **+14.2** | `ALNY` `GILD` `AMGN` `REGN` `VRTX` `ABBV` |
| Pharmaceuticals | 5 | +0.302 | +0.179 | 4/5 | +6.3 | +8.7 | `MRK` `PFE` `JNJ` `BMY` `LLY` |
| Health Care Distributors | 3 | +0.257 | +0.111 | 2/3 | +4.5 | +9.4 | `COR` `CAH` `MCK` |
| Life Sciences Tools | 4 | +0.226 | +0.113 | **0/4** | +2.6 | +10.8 | `A` `TMO` `DHR` `WAT` |
| Managed Health Care | 3 | +0.128 | +0.069 | 1/3 | +2.2 | −3.4 | `HUM` `ELV` `UNH` |
| Health Care Services | 2 | +0.110 | +0.069 | 0/2 | +0.9 | −9.1 | `CVS` `CI` |
| **Health Care Equipment** | 8 | **−0.044** | +0.021 | 2/8 | −1.1 | +0.2 | `MDT` `BDX` `BSX` `EW` `ABT` `ISRG` `IDXX` `SYK` |
| Health Care Facilities | 1 | **−0.472** | −0.223 | 0/1 | −1.6 | +2.3 | `HCA` |

**Sub-node dispersion (excluding the n=1 node): +0.519 − (−0.044) = 0.563**, against the sector's own
`eqflow` of **+0.190** ⇒ **the spread is 3.0× the sector move.** ⚠ **Per lens B5 the sector label is
the wrong unit of analysis here**, and this file says so: *"Health Care is N+"* averages a
**6-of-6-accumulating biotech node** with an **8-name equipment node that is negative on flow and
`rs20`**.

🚨 **And the sector's only 🟢 sits in its WEAKEST node.** `MDT` (flow **+0.928**, `rs20` **+8.4**, `rs60` **+11.2**, `vol_surge` **1.47**, with OBV +0.327 quoted as one of four axes — **RULE D6 exempt: the claim rests on the composite `flow_score` and the two RS axes; OBV is never alone**)
is **Health Care Equipment**, `eqflow` **−0.044**, 2/8 accumulating. **The one name the tag surfaces
is the one name whose node the flow does not support** — carried unchanged from 09-06 and now
explained by §0 (it is the only name that clears the turnover gate, not the only name that is strong).

---

## 2 · Players — large-cap ∪ thematic, bounded

All 32 universe names are ≥$10B and appear in the sector's news window. **The thematic small-cap
union cannot be built**: mid-cap biotech (the node with 6/6 accumulation) is almost entirely below
the universe's cap floor, so the alpha layer this stage is told to reach is **structurally absent**
(`D563`, third instance). **Named as a gap, not narrowed silently.**

**Chain-hop**: not run for this sector this run — the direct news axis is live but the sector produced
**no BUILDING or REIGNITED thread** in `thread --days 7 --scope foreign`. ⚠ **That is NOT a "quiet
sector" claim** (barred: 247 of 299 names unmeasured, and Health Care had 5 of 32 measured). It is
recorded as *"no thread surfaced in the 99 alive"*, which is a statement about the selection, not the
sector.

---

## 3 · IR / primary — the valuation check, and it is the MIRROR of Energy's

`module_fundamentals_us ALNY` (the biotech node's top flow, OBV **+0.359 매집**, `rs20` **+21.8**):

| | |
|---|---|
| price / mcap | **$266.11** · $36B (52w **$197.81 – $495.55** ⇒ price is **46% below its 52-week high**) |
| **forward P/E** | **21.14** (trailing 46.28) · PEG 0.34 · P/S 7.41 · P/B 26.28 · beta **0.30** |
| **estimate momentum, 90-day change** | current quarter **2.46 → 2.32 = −5.9%** · next quarter **−3.8%** · current year **9.51 → 8.92 = −6.3%** · **next year 13.90 → 12.59 = −9.4%** |
| **revision breadth (30d)** | current quarter **2↑ / 11↓** |
| analyst target | mean **$370.20** ⇒ **+39.1% vs price**; median $350; 6 Strong Buy / 16 Buy / 7 Hold / 0 Sell |

★★ **The cross-sector finding, and it is the reason this file was worth writing on a frozen tape.**
This desk holds **two OW sectors and they are in opposite estimate regimes:**

| | Energy (`MPC`) | Health Care (`ALNY`) |
|---|---|---|
| forward P/E | **12.24** | **21.14** |
| 90-day estimate change (next year) | **+33.6%** | **−9.4%** |
| revision breadth (30d) | **15↑ / 0↓** | **2↑ / 11↓** |
| price vs 52w high | **within 2.4% of the high** | **46% below the high** |
| price vs mean target | **−14.3% (above consensus)** | **+39.1% (below consensus)** |
| OBV | accumulating | accumulating |

⇒ **"OW" means two different things.** Energy is **accumulation into a rising denominator at a cycle
high** — the peak-margin/low-multiple trap. Health Care/biotech is **accumulation into a falling
denominator well below the highs** — the opposite risk, where the multiple is *not* low and the
estimates are *not* helping. **Neither is "cheap"; they fail the test from opposite directions**, and
no prior run has put them side by side.
⚠ The revision table is used **only as a description of the denominator's direction** (`measure_ic`
2026-08-09: opposite signs across two windows, and the effect is an **IT loading** — ex-IT Q5−Q1
**−1.1pp**). **On a non-IT name that caveat cuts the other way**: the confound the measurement found
lives in IT, so a Health Care revision reading is *less* contaminated — but it still carries **no
leading claim**, only direction.

**Contract-terms / mean-reversion check.** No mean-reversion claim is made about this sector's
margins in this file, so the rule's trigger does not fire. ⚠ Stated explicitly rather than skipped:
**the biotech node's denominator risk is patent-cliff and trial binary, not contracted price** — a
different structure from Energy's and from memory's, and the take-or-pay frame **does not apply**
(this is the "checked, does not apply" pass the frame-transfer rule allows).

---

## 4 · Value chain — 6 nodes, and the binding constraint is **not** demand

| # | node | state (`asof 09-04`) | binding? |
|---|---|---|:--:|
| 1 | **Discovery / biotech pipeline** | `eqflow` **+0.519**, **6/6 accumulating**, `rs60` +14.2 — the chain's strongest node | — |
| 2 | Large-cap pharma | +0.302, 4/5 accumulating, `rs60` +8.7 | — |
| 3 | **Tools & instruments** (the capex node) | +0.226, **0/4 accumulating**, `rs20` +2.6 — **positive flow with ZERO accumulation** | ★ **the leading indicator that is NOT confirming** |
| 4 | Distribution | +0.257, 2/3 | — |
| 5 | **Payors / managed care** | +0.128, `rs60` **−3.4**; `UNH` **−0.378, OBV −0.131 분산** | ★★ **THE BINDING CONSTRAINT — reimbursement, not demand** |
| 6 | Providers / facilities | **−0.472** (`HCA`), OBV −0.223 분산 | the payor squeeze's other side |

⚠ **Strong demand ≠ bottleneck.** The chain's money is at the **front** (discovery) and its weakness
is at the **payment** end (nodes 5–6 are the only two negative-`rs60` nodes). **A pipeline that cannot
be reimbursed is not a revenue node**, and the binding constraint is therefore policy/pricing.
**Cross-sector chain**: node 5 → federal budget → the same fiscal thread `EVENT_ALPHA` Card 6 tracks
($40tn debt, $1.25tn annual interest). **No row on this desk measures that link.**

---

## 5 · The node's CUSTOMERS, named, with their disclosed spend

The biotech node's customers are **large-cap pharma (in-licensing / M&A)** and **payors**.
- **Pharma's capacity to pay is measurable and it is positive**: node 2 `eqflow` +0.302 with 4/5
  accumulating and `rs60` +8.7 — the buyer is not distressed.
- **The payor's willingness is the constraint and it is negative**: node 5 `rs60` −3.4, `UNH` OBV
  **분산**, node 6 `HCA` **−0.472**.
- ⚠ **No Health Care name has a dated print inside this window.** `catalyst_calendar --days 10`
  returns **"(none in window / yfinance unavailable)"** for EARNINGS — which this run has shown is an
  **unavailability rendered as an absence** (`D560`), so the correct statement is *"the calendar
  cannot tell us"*, not *"there are none"*.

---

## 6 · Lead/lag claims — tested or tagged

| claim | status |
|---|---|
| *"Tools & instruments leads pharma capex"* | **`[unverified]`** — not measured this run. ⚠ It is the exact claim class `RESEARCH.md` A5 warns about (the EDA→semis case: same-month **+0.63** vs lag-12 **+0.05**, i.e. coincident, not leading). **Not asserted.** ★ But the *cross-sectional* fact stands on its own without any lead claim: node 3 has **positive flow and 0/4 accumulation**, which is a disagreement inside one node at one time |
| *"biotech leads the sector"* | **`[unverified]`**, and deliberately not inferred from the 6/6 accumulation |

---

## 7 · Track KPIs and anti-signals

| KPI | current | what breaks the thesis |
|---|---|---|
| Biotech node OBV breadth | **6/6 accumulating** | **any name losing accumulation** — this is the node's whole case |
| Tools node accumulation | **0/4** | it turns positive ⇒ the capex node confirms; it stays 0/4 through another run ⇒ the front of the chain is unfunded |
| `ALNY` revision breadth | **2↑ / 11↓** (30d) | a flip to net-up ⇒ the denominator has stopped falling |
| Payor node `rs60` | **−3.4** | deepening past −10 ⇒ the binding constraint is tightening |
| `MDT` (the sector's only 🟢) | flow +0.928 in a **−0.044** node | its node turning positive ⇒ the tag stops being a lone signal |
| Sector `eqflow` | **+0.190**, rank 2 on the board | turning negative ⇒ the N+/OW verdict loses its only positive aggregate |

**Anti-signals:** a **US drug-pricing action** (executive or legislative) — the binding-constraint node
is policy · **a failed late-stage trial** in the biotech node (idiosyncratic, but the node is 6 names)
· **`hy_oas` ≥ 3.10%** (a credit event re-prices unprofitable biotech first).
⚠ **None of these is dated.** The sector has **no binary in `catalyst_calendar`'s 10-day window**, and
per `D560` that absence is not verified.

---

## 8 · ROTATION's divergence — resolved

**ROTATION attempted `HLTH OW → OW+` and declined**, citing *"Δ −0.043 negative and unchanged"* and
noting that the promoting argument (the `vol_surge` critique) was *"an INSTRUMENT critique, not a flow
number."*

**Resolution: the instrument critique is now a MEASUREMENT, and it still does not justify a promotion.**
§0 converts *"8 names look blocked"* into *"9 named names clear three merit conditions and are
excluded by the gate alone, and only one name in 32 clears the gate at all."* That is a number.
**But it is a number about the tag, not about the sector's direction** — `eqflow` is still +0.190
(unchanged) and Δ is still **−0.043** (negative, unchanged). ⇒ **The verdict stays `OW`**, and what
changes is that **the sector may no longer be described as one-name breadth.** The corrected
description goes to BET; the notch does not move.

---

## ✅ EXIT CHECK — DEEP-HLTH

- [x] Continuous-track file **leads with the delta** (a measured correction to the sector's own headline breadth number); structure carried by reference.
- [x] flow → players (with the small-cap union's **structural absence** stated) → IR (primary fundamentals, XBRL-crosschecked) → chain map (6 nodes, binding constraint named as reimbursement) → KPI/anti-signals.
- [x] **Commodity/price-cycle rule**: not applicable — Health Care has no commodity node. **Stated rather than skipped.**
- [x] **The valuation claim states where the denominator sits AND its revision trend** — `ALNY` fwd P/E 21.14 with estimates **−9.4% / 2↑:11↓**, and the cross-sector table places it against Energy's opposite regime. The `measure_ic` caveat is quoted **and its direction for a non-IT name is stated.**
- [x] 🚨 **Mean-reversion / contract-terms rule**: no margin mean-reversion claim is made; the **frame-transfer question is answered as "checked, does not apply"** with the reason (patent-cliff and trial risk, not contracted price).
- [x] **Customers named and their disclosed capacity checked** (pharma node positive, payor node negative), with the calendar's silence flagged as `D560` rather than read as absence.
- [x] **Lead/lag claims tagged `[unverified]`, none inherited as fact** — and the A5 precedent quoted.
- [x] **Sub-node dispersion stated: 0.563 vs a sector move of 0.190 = 3.0×** ⇒ **the file states that the sector label is the wrong unit.**
- [x] **ROTATION's divergence has an explicit verdict** — critique upgraded to a measurement, notch still declined, description corrected.
- [x] Linter run — see run log.

---

> P4 — analytical only. No sizing, no buy/sell language.
