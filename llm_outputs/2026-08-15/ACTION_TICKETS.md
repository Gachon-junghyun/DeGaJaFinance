# ACTION_BRACKET — 2026-08-15  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,984,877원 · fx 1415 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

### CORE-STARTER (tape-independent) — PSX  (BUY)
- **condition:** establish NOW regardless of tape — closes Energy / oil-refining (Hormuz + Russia crack) epicenter GAP (7.1% < 8.0%)
- **size:** 5 sh @ ~$233.61 (≈$1,168.05 notional, risk $90.38 = 0.8% )
- **stop:** $217.26 (−7.0%) · exch NYSE
- **why core:** cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively exiting (FINRA short-vol z -1.43, 5v5 -16.6▼) = clean structural entry, not an extended one (cf. MPC RSI 85.7). Crack-spread leverage, not crude beta. Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

## 🚨 HAND-WRITTEN ADDENDUM — the mandatory both-sides bracket the script dropped (`D263`, 2nd run)

**What happened, measured:** `CATALYST_WATCH.json` carries **one** binary in window —
*"Iran 'Strait of Hormuz open' statement (TACO trigger)"*, `🔀binary`, **`"undated": true,
"days_until": null`** — and `action_bracket` printed **no both-sides ticket for it**. The protocol makes
that bracket **MANDATORY**. `D263` recorded the cause on 08-14 (**the date filter drops undated rows**,
distinct from `D155`'s midnight-crossing false negative) and instructed the desk to hand-write the
ticket meanwhile. **This is that ticket, and this is the second consecutive run it has been needed.**

### BOTH-SIDES CONDITIONAL — Strait of Hormuz statement (UNDATED, trigger-on-occurrence)

| | Branch A — **"the Strait is open"** | Branch B — **escalation continues** |
|---|---|---|
| **Trigger (occurrence, not a date)** | An Iranian or US official statement that the Strait is **open**, corroborated by a **ship-traffic** print off its 3-month low | A **named-vessel** attack, a formal closure/territorial declaration, or traffic making a **new** 3-month low |
| **What rips** | `XLU` · `XLRE` · `XLP` · long-duration equity · `RSPT`/`XLK` — **everything this desk is underweight** | The refining node · `XLE` |
| **What gets hit** | 🚨 **The Energy OW promoted TODAY**, the held refiners (`MPC`, `PSX`), the rank-2 cycle GAP, and EVENT_ALPHA Card 3 — **one statement, four objects** | The four duration underweights simultaneously |
| **Named starter list** *(naming, not sizing — P4)* | `XLU` · `XLRE` · `NEE` · `DLR` · `EQIX` | already on the sheet: `MPC` · `PSX` · `VLO` |
| **Invalidation of the branch** | ★ **The Strait reopens while the crack HOLDS.** Card 3's mechanism is **Russian refinery capacity destruction** — killed by a **ceasefire**, not by Hormuz | The crack falls while the Strait stays shut ⇒ the transit premium was never the driver |
| **Positioning context (D6 — context, never a trigger)** | **WTI spec sits at the 18th percentile SHORT** (COT, Tue 08-11 close) ⇒ a bullish-crude unwind has **little short fuel to burn**, so branch A would be one-directional | same reading, opposite sign |

**Frozen observable (already registered, not re-minted): `S84`** — `[XLE exc5] − [EW{XLU,XLRE} exc5]`
vs **`SPY`**, settle **2026-08-21**, **A ≤ −3.174 · B ≥ +5.544**.
★ **Live state +6.545 — already 1.00pp ABOVE branch B** with four sessions to run.
🚨 **Information grading, stated BEFORE the settle (B4): branch B is now NEAR-ZERO information; branch
A is the row's entire content.** No threshold is moved (`D242`).
⚠⚠ **And `S84` alone does not settle the node** — it tests Hormuz transit only. **`P62`'s KPI
(`HO=F` 20d − `CL=F` 20d = +5.48pp, direction A holds above +4pp) carries the Russia mechanism.**
**Both must be read together on 08-21.**

*Hand-written because the generator cannot see undated rows. Analytical artifact — zero buy/sell
advice, no order is sent, no size is recommended.*
