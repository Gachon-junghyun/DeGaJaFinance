# ACTION_BRACKET — 2026-07-25  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 11,399,250원 · fx 1469 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** FOMC decision (Warsh, no SEP) (D-4, axis=rates) — both-sides armed below.

### BRACKET::A_cool  ★asym-hedge — NVDA  (BUY)
- **condition:** IF FOMC decision (Warsh, no SEP) (D-4) prints toward cool
- **size:** 4 sh @ ~$206.84 (≈$827.36 notional, risk $62.06 = 0.8% )
- **stop:** $192.36 (−7.0%) · exch NASD

### BRACKET::B_hot — XLE  (BUY)
- **condition:** IF FOMC decision (Warsh, no SEP) (D-4) prints toward hot
- **size:** 27 sh @ ~$59.62 (≈$1,609.74 notional, risk $116.37 = 1.5% )
- **stop:** $55.45 (−7.0%) · exch AMEX

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ADDENDUM — industry_US ALPHA (stage 9), 2026-07-25 · the pre-mortem's both-sides brackets

> Appended by the `industry_US` desk after `action_bracket.py` ran. **The script wired ONE binary
> (FOMC, D-4) and produced two tickets. The pre-mortem registered SEVEN brackets** — the six below
> plus the FOMC one the script already covers. They are recorded here as **conditions and frozen
> observables**, so that a bracket the script cannot see is not silently lost.
> ⚠ **Deviation logged, deliberately**: **no share counts or sizing are attached to the brackets
> below.** This run is analytical-output-only; the script's own DRY-RUN sizes above are its
> deterministic artifact and are left exactly as it emitted them. **Zero buy/sell advice (P4).**
> Full text of every bracket: `handoff/SCENARIOS.md` (registered 2026-07-25, frozen pre-event).

⚠ **The script's "nearest binary" is wrong by one event.** It reports **FOMC (D-4, 2026-07-29)** as
nearest, because `CATALYST_WATCH.json` contains no 2026-07-28 row at all. **The window's first binary
is UPS on 2026-07-28 (D-3)** — scenario S20, and the desk's own registered falsifier for the rail
node. This is **D18's 6th consecutive occurrence** and the first in which the calendar misses the
*next* event on the board.

| ID | Binary · date | Branch A (with the tilt) | Branch B (AGAINST the tilt) | Frozen observable · threshold | Names that move on B |
|---|---|---|---|---|---|
| **S20-ANNEX** | **UPS Q2 · 2026-07-28 (D-3)** | fuel quantified materially higher YoY ⇒ W4/D23 closes 5 of 5 | **guidance cut on VOLUME, not fuel** | median **RS20 vs SPY** of {CSX, UNP, NSC} **turns negative by 2026-08-04**. ⚠ **Any UPS same-day move inside ±6.9% is pre-declared no-information** (the straddle is 4.04σ of its own σ20 = **1.81× realized** — the only genuinely event-priced instrument in the window, and the option market is **complacent** on it: P/C 0.35, skew +11.1) | CSX · UNP · NSC · ODFL — *downside*. **UNP double-hit**: ~8 of its 12 revenue growth points are fuel surcharge |
| **S23** | **FOMC · 2026-07-29 (D-4)** | curve holds or re-steepens | **hold + BEAR-FLATTENER** — kills NIM without tripping any previously registered threshold | **T10Y2Y ≤ +0.20 on a close by 2026-08-05**, with **DGS2 quoted alongside** and inside 4.15–4.45%. **No options instrument exists for an FOMC decision** — stated | WELL · PLD · AMT · **PCG** · DUK. ★ **FIN OW and UTIL UW lose on the same tick** ⇒ one rate bet carried with opposite signs |
| **S24** | **MSFT/META/AMZN capex · 07-29→31** | capex raised **and** the physical layer keeps being distributed | capex raised **and the physical layer RE-RATES**, inverting EVENT_ALPHA Card 3 | median **RS20 vs SPY** of {VST, CEG, GEV, VRT} **> 0 by 2026-08-12**. ⚠ **n≈1 declared at registration** (VST–CEG +0.768 SPY-residual ⇒ one unit, not four). **No price threshold admissible** — the three straddles price **0.61–0.88σ** and expire 07-27, before their events | VST · CEG · GEV · VRT · ANET (2nd tier PWR · CIEN · NEE) |
| **S14-num** | **MA Q2 · 2026-07-30** | volume holds | volume miss ⇒ {MA, V, PYPL} RS20 vs SPY flips negative by 2026-08-06 | ⚠ **Any MA same-day move inside ±3.9% carries no information** (1.09× ordinary realized) **and may not be read as confirming the FIN OW.** S14 itself is **NOT re-frozen** | WELL · PLD · AMT · SPG · VTR. ★ MA/V is a **different** residual unit from JPM/TRV/CB |
| **S21 / S8** | **VLO + STNG · 2026-07-30** | cracks stabilise ≥65 and the diesel gap re-widens | crude falls **AND** the diesel crack rolls with it | VLO same-day **outside ±6.6%** *and* settled 3-2-1 crack **< 65 by 2026-08-06**. ⚠ **Crude falling while cracks HOLD is S8 branch B — explicitly NOT against us** | DAL · UAL · LUV · FDX · UPS (fuel +66–84% YoY, D23) |
| **S25** | **RE OW− · by 2026-08-08** | the sector-level tilt is what was granted | the tilt was a **data-centre bet mislabelled as a sector verdict** | **DLR RS20 vs SPY** and the **{PLD, AMT, WELL} median RS20 vs SPY**, reported **separately, never merged**. Trip: DLR falls below the median while the median stays positive. ⚠⚠ **Confound found this run: AMT and WELL both print 07-28, inside the window; PLD is the only event-free control and must be reported alone** | WELL · VTR · SPG · IRM · PLD |
| **S26** | **credit · by 2026-08-12** | spreads hold < 3.00%; the three OW tilts stay three bets | **index-level credit widening — all three OW carriers lose together** | **HY OAS (FRED `BAMLH0A0HYM2`) ≥ 3.10% on a close, with NFCI turning positive WoW.** No options instrument covers it — stated. Today **2.77% (+9bp on 07-23, its first material widening in six runs)**, NFCI **−0.552 loosening a 5th week** | The low-beta side: **WELL (β 0.224) · AMT (−0.054) · XOM (0.256) · CB (0.125) · TRV (0.339)**. ★ **CB and TRV sit INSIDE the FIN OW — it carries an internal hedge its label hides** |

### Why S26 exists at all
**Every other bracket in this book — including S19, S9 and four of the six written today — lists
`HY OAS > 3.10%` as an *invalidation*** ("then it is a credit event and the rate attribution is
void"). That turns the desk's **single largest correlated exposure** into a get-out-of-jail card. The
three OW tilts are genuinely three SPY-residual units (XLF–XLE **+0.188**, XLF–XLRE **+0.307**,
XLE–XLRE **+0.134**, never merging from threshold 0.55 to 0.85) — **but that independence is
conditional on SPY, and a credit shock IS the SPY factor** (betas: JPM 0.932, XLF 0.789, DLR 0.769,
PLD 0.766, PSX 0.747). **S26 converts the escape hatch into a scoreable branch.**

### No cycle-GAP core-starter is emitted, and the ✅ is not trusted
`cycle_exposure.py` returned **no GAP**. The pre-mortem overturned it in substance: with the held set
(AVGO/NVDA/TSM) **unchanged** across five runs, the AI-compute margin over its floor ran
`−0.001 (GAP) → +0.252 → +0.254 → +0.136 → **+0.011**` — **nothing was bought; today's ✅ clears by
1.1 basis points on mark-to-market drift.** The held names are the bucket's **worst** (AVGO 10/10,
NVDA 9/10; Energy's XOM 5/6 with **0% refining**, while the registry's own human-locked `core_pick`
is **PSX**, unheld). ⚠ **`RISK_UNITS.json` lists the book WITHOUT TSM while `cycle_exposure` counts
TSM in epicenter dollars** — one of the two is wrong about a rank-1 position, and which is
`[unknown]` (D62). **No starter list is produced from a flag this run does not trust.**

*Analytical artifact. Zero buy/sell advice, zero sizing on the addendum brackets. A human executes
separately, never the desk.*
