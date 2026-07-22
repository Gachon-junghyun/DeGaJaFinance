# SCENARIOS — pre-registered branches, scored after the fact

> Read at HANDOVER (run start) and at PREMORTEM. A scenario is only valid if it was written
> **before** its event, carries **both** branches, and names a **date** and an **observable with a
> threshold**. Registered-after-the-fact entries are worthless — they are hindsight wearing a table.
> Scoring is done by L3 [`scenario_score`](../pipeline/L3_functions/scenario_score.md). Not advice.

**asof 2026-07-22 12:12 KST** (US Eastern 2026-07-21 23:12 — the US 07-22 session had **not opened**)

## Status legend
`ARMED` registered, event pending · `FIRED-A/B/C` branch that occurred · `EXPIRED` date passed unscored
(a scoring failure, log it) · `VOID` premise invalidated before the event

---

## S1 — Alphabet Q2 print · ARMED · 2026-07-22 after US close (≈2026-07-23 05:00 KST)

**Why it matters here**: first of four hyperscaler prints; the only one inside a 24h horizon.
**The observable is capex, not EPS.** Consensus EPS $2.86–2.95, revenue $116.8–120.2B — neither
is the variable that touches the memory thesis.

**Derived threshold (own arithmetic, not a cited figure)**: FY guide midpoint $185B minus Q1 actual
$35.7B leaves $149.3B over three quarters = **~$49.8B/quarter run-rate**. Q2 capex materially below
~$40B under-runs the guide; materially above ~$50B implies another raise.
⚠ Capex normally ramps into year-end, so a Q2 below the flat average is not by itself a shortfall.

### Pre-print state — measured 2026-07-22 with the three axes added today

| Axis | Reading | What it means before the print |
|---|---|---|
| **Implied move** (`module_flow --positioning`) | **±7.1%**, 0DTE (expiry 2026-07-22) | The market has already priced a ~7% move. **A reaction inside ±7.1% is not information** — thresholds must sit outside it to carry any. |
| **Estimate revisions** (`module_fundamentals_us`) | Current quarter **1↑ : 4↓ over 30 days**; next quarter 2↑ : 3↓; current year 3↑ : 4↓ | ★ **Near-term estimates have been drifting DOWN into the print** — the bar was quietly lowered. This is the exact opposite of MU (**30↑ : 0↓**). |
| Estimate level | +1y EPS 13.38 → **14.69** over 90 days (+9.7%); current year +23.1% | Longer-dated estimates still rising, near-term cut. A classic "push the good news out" pattern. |
| Valuation | fwd P/E **23.66**, PEG 1.37, consensus target **$433.51 (+24.9%)** vs price $347.15 | Sell-side target is 25% above the tape while it trims the near quarter — read the two together. |
| **Credit backdrop** (`module_macro_us hy_oas`) | HY OAS **2.69%**, 6bp off its 365-day low, **16bp tighter over 90 days** | No risk-off backdrop. A disappointment lands into a *complacent* credit market, which is why the second-order test below matters. |

★ **Two pre-commitments from this state, binding:**
1. **A move inside ±7.1% scores as branch B (no information)** regardless of the headline. Do not
   convert an in-line reaction into a thesis change.
2. **A "beat" against estimates that were cut 4:1 into the print is not a beat** — it is a lowered
   bar being cleared. Score against the **capex line and the revision trend**, not against consensus EPS.

| Branch | Observable | Meaning for the standing view | Information content |
|---|---|---|---|
| **A · raise** | FY guide lifted above $190B, or 2027 quantified upward | Volume leg extends; margin-peak timing **pushed later**. M1 unaffected. | **Low** |
| **B · hold** | $180–190B reaffirmed, no change | No information. Thesis unchanged. | ~None |
| **C · cut or ROI defensiveness** | Guide lowered, or management hedges on returns, or Cloud margin disappoints | **Rewrite required** — breaks the volume leg *and* the price leg together. Extends beyond memory to NVDA/AVGO. | **High** |

**Second-order test (new, from the credit axis)** — if branch C fires, watch **HY OAS** the following
session. A capex cut that widens high-yield spreads is a *regime* event (the AI-capex complex is a
credit story too); one that leaves HY at ~2.7% is a single-name repricing. This distinction was
unavailable before 2026-07-22 and is the reason the credit series were added.

**Prior**: A or B far more likely than C — Alphabet raised in each recent quarter, Q1 capex was
+107% YoY, the 2027 increase is already publicly stated, Cloud backlog >$460B. `[inferred]`
⚠ **But the revision trend cuts against that prior** — near-term estimates fell 4:1 over 30 days,
which is not what a desk expecting an unambiguous raise usually looks like. Hold both and let the
capex line settle it.
**Transmission path**: print ≈05:00 KST 07-23 → US after-hours → **KR semis open 09:00 KST 07-23**
(~4h later) → US regular session 22:30 KST. Same day: TSLA. Next day: INTC (foundry read-through).

**Pre-commitment (binding)**: a beat on EPS/revenue with capex merely reaffirmed is **branch B, not A**.
Do not upgrade the thesis on the wrong line item.

---

## S2 — The 2026-07-29 cluster · ARMED · four events, one day

The single most loaded date on the calendar. Two of them resolve currently-unreadable state.

| Event | Resolves |
|---|---|
| **Microsoft earnings** | Second half of hyperscaler capex (with META) |
| **Meta earnings** | ditto |
| **FOMC decision** | The duration/real-rate gate the US desk carries (`real 10Y > 2.50~2.55%` kill line; 2.31% asof 07-17) |
| **SK hynix ADR ↔ ordinary two-way conversion opens** | **Un-suspends the 000660 flow read** (STANDING_VIEW §3) and collapses the ~25% premium |

| Branch | Observable | Meaning |
|---|---|---|
| **A** | MSFT+META both raise capex | Volume leg confirmed across 3 of 4 hyperscalers; margin-peak timing pushed out |
| **B** | Mixed / reaffirmed | Partial; wait for AMZN + AAPL (07-30) |
| **C** | Either cuts, or real 10Y closes >2.55% | Thesis rewrite (C) or duration-book invalidation (rate) — **two independent triggers stacked on one day** |

⚠ **Stacked-tail warning**: a hawkish FOMC and a capex disappointment hit the same book from
different directions on the same date. The US desk's own PREMORTEM flagged this class of
concentration on 07-21 for Energy; it applies here.

**On the ADR leg**: whichever way convergence runs, the *mechanical* distortion ends. From 07-30 the
000660 foreign-flow series is readable again — but the pre-07-29 series is **not retroactively
clean**. Do not backfill a directional read onto it.

---

## S3 — 4Q26 DRAM contract guidance · ARMED · ~2026-09/10

**The only frontal falsifier of the standing regime call.**

| Branch | Observable | Meaning |
|---|---|---|
| **A** | 4Q26 QoQ guide **>18%** (re-acceleration) | **The deceleration read (M1) is wrong.** Retract §1 of STANDING_VIEW. |
| **B** | 4Q26 in the 5–18% band | Deceleration continues as read |
| **C** | 4Q26 <5% or negative | Deceleration is steeper than read; margin peak arrives sooner |

---

## S4 — Micron FQ4 print + FQ1'27 guide · ARMED · ~2026-09 late

**The actual test of the margin-peak hypothesis**, because FQ4 (Jun–Aug) still carries decent
pricing; the 3Q26 calendar price deceleration lands in **FQ1'27 (Sep–Nov)**. `[inferred]` on timing.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | FQ4 GM ≈86% delivered **and** FQ1'27 GM guided flat/up | LTA floors (C1) are real; margin-peak call weakens materially |
| **B** | FQ4 in line, FQ1'27 GM guided down | Margin-peak hypothesis confirmed on schedule |
| **C** | FQ4 GM misses 86% | Peak already passed; earlier than read |

---

## S5 — KR semiconductor exports, 1–10 August · ARMED · ~2026-08-11

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Semis up MoM on a like-for-like window | M12's MoM decline was a one-month artifact |
| **B** | **Second consecutive MoM decline** | Deceleration confirmed on an independent series (customs, not TrendForce) |

⚠ **Comparison discipline**: compare 1–10th to 1–10th, or 1–20th to 1–20th. Mixing a partial window
against a full month is how M12 got mis-cited the first time (R2).

---

## Scoring log

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| S1 | 2026-07-22 | 2026-07-22 AMC | — | — | ARMED |
| S2 | 2026-07-22 | 2026-07-29 | — | — | ARMED |
| S3 | 2026-07-22 | ~2026-09/10 | — | — | ARMED |
| S4 | 2026-07-22 | ~2026-09 | — | — | ARMED |
| S5 | 2026-07-22 | ~2026-08-11 | — | — | ARMED |

**Scoring rule**: a scenario is scored at its next HANDOVER after the event date, whether or not
anyone remembers to look. An `EXPIRED` row is a process failure and is logged as one — an unscored
scenario is how a desk keeps its wins and forgets its losses.
