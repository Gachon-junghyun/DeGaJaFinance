# SECTOR_DEEP_FIN — Financials · industry_US · 2026-08-03 · **CONTINUOUS track → DELTA ONLY**

> Structure carried by reference to `llm_outputs/2026-08-02/industry_US/SECTOR_DEEP_FIN.md`.
> ⚠ Lenses executed in-context, not by an agent fan-out (see PREMORTEM §0).

## 0 · The question this DEEP owes an answer to

**M317 recorded that the FIN OW−'s stated carrier has changed in three consecutive runs** —
*"breadth-led"* (retracted, **R32**) → *"the bear steepener"* (**W3-constrained** by M138) →
*"the insurance node"* — and **flagged it as an instability, not sold it as a discovery.**
**A fourth change would make the tilt unfalsifiable.** So: **does the insurance carrier survive a
run in which the flow instrument itself was proven unstable?**

**Answer: YES, and it is the only FIN claim that does.** Uniquely among this run's flow evidence, the
insurance node's greens survive the D126 filter — because they cleared on **volume**, not on the
velocity path that was null two days ago.

---

## 1 · ★★★ Delta 1 — of Financials' 5 greens, THREE are manufactured and one of the survivors is on the reject ledger

`SWEEP_READ §2` isolated **10 greens manufactured** by the velocity join on identical prices.
**Three of them are Financials: BAC · JPM · MA.** Filtering them out:

| Ticker | flow | tag | `vol_surge` | Green path | Status |
|---|---|---|---|---|---|
| **MET** | **+0.80** | 🟢 | **1.36** | ✅ **VOLUME — real** | ✅ clean |
| **ICE** | +0.79 | 🟢 | **1.22** | ✅ volume — real | ⛔ **on the reject ledger (08-02), 🔴RESOLVED at ALPHA** |
| BAC | +0.60 | 🟢 | **0.85** | ⚠ velocity — **manufactured** | not citable |
| MA | +0.57 | 🟢 | **1.03** | ⚠ velocity — **manufactured** | not citable |
| JPM | +0.55 | 🟢 | **0.76** | ⚠ velocity — **manufactured** | not citable |

⇒ ★★ **Financials has exactly ONE clean, non-rejected, volume-path green on the board: MET.**
Stated positively rather than as a complaint: **when the instrument is filtered to what reproduces,
the sector's evidence collapses onto the insurance node — which is exactly what M317's third carrier
predicted.** That is a carrier surviving a filter it was not designed for.

---

## 2 · ★★★ Delta 2 — the insurance/life node has BOTH the flow and the base, and nothing else in the sector does

Top non-exchange flow scores, settled 07-31, **benchmark SPY inline**:

| Ticker | node | flow | RS20 | RS60 | **days 21-60** | `vol_surge` | OBV |
|---|---|---|---|---|---|---|---|
| **MET** | Life & Health | **+0.80** | +6.4 | **+17.1** | **+10.7** | **1.36** | 매집 |
| **PRU** | Life & Health | +0.76 | +7.8 | **+18.5** | **+10.7** | 1.18 | 매집 |
| **TRV** | P&C | +0.72 | +9.1 | **+21.0** | **+11.9** | 1.16 | 매집 |
| **STT** | Custody | +0.54 | +7.6 | **+20.6** | **+13.0** | 0.80 | 매집 |
| *(contrast)* BAC | Bank | +0.60 | +5.2 | +13.4 | +8.2 | 0.85 | 매집 |
| *(contrast)* JPM | Bank | +0.55 | +4.9 | +10.5 | +5.6 | 0.76 | 매집 |
| *(contrast)* ICE | Exchange | +0.79 | +14.4 | **−5.0** | **−19.4** | 1.22 | 매집 |

★★ **The insurance/custody cluster is the only group in the sector positive on flow, RS20, RS60 AND
days 21-60 simultaneously.** Its bases (**+10.7 to +13.0**) are roughly **2× the banks'** and stand
against **ICE's −19.4**, which is the shape that got ICE resolved.

★ **M317's stated mechanism is consistent with the curve this run measured**: a **30y-led**
steepening — **DGS30 +12bp to 5.21 with 30y−10y 0.48 → 0.53** `[FRED]` — transmits to insurers
through **reinvestment yield on long liabilities**, not through deposit-funded NIM. ⚠ **W2 binds: the
desk has NO lag table for "long-end steepening → insurer reinvestment yield."** The claim is
**`[inferred]` and is not admissible as evidence** — it is stated as the mechanism the carrier
*asserts*, with the test named below.

⚠ **W5 — dispersion inside the label**: **PYPL +25.5 RS20 vs ICE −5.0 RS60**; M317 measured 12
sub-industry groups spanning mean flow **+0.618 to −0.236 = 0.854**, ~7× the sector's own eqflow.
**"Financials" remains the wrong unit of analysis; the tilt is carried by a node, not a sector.**

---

## 3 · Delta 3 — the curve leg, and where its falsifier sits

`[FRED]`, derived `DGS10 − DGS2` (derivation stated, **C5**): **2s10s +0.45 on two consecutive
settled prints (07-29, 07-30)**, against **S23's ≤ +0.20 line ⇒ 25bp away and receding.**
⚠ **The 07-31 nominal prints are UNPUBLISHED** (**D139** — FRED publishes T10YIE a business day ahead
of the nominals, observed twice now), so this is **n = 2 dates (S1)**, not two independent weeks.

⚠⚠ **W3 binds and is not softened**: **M138 measured the NII leg migrating to markets/financing** —
**WFC held FY26 NII ~flat and MISSED; JPM RAISED on markets NII** ⇒ **a steepener does not reach
every bank**, and **BAC and JPM both slipped 🟢 → 🟡 with negative deltas on 07-31.**
⇒ **the curve leg supports the INSURANCE carrier better than it supports the bank carrier**, which is
the same conclusion §2 reaches from the price side, by an independent route.

**S51 (NFP 08-07) is the live falsifier**: 2s10s **≤ +0.20** breaks the mechanism.

---

## 4 · R32 held to, not quietly rebuilt

**R32 killed *"Financials is the board's only breadth-led sector"*.** M316 re-tested it on fresh data:
**all-47 gap +0.0370; ex-BRK-B +0.0095**, with **BRK-B = $1,055.7bn = 13.94% of a $7,573.9bn sector**.
⇒ **74% of the statistic is one row.** **"Breadth-led" is not rebuilt here as a reason**, and this
run adds nothing that would let it be — **the sector's own flow numbers moved on D126 this run**, so
any recomputation of the gap would be a recomputation of the artifact.

---

## 5 · Track KPIs · anti-signals · dates

| KPI | State | Anti-signal | Date |
|---|---|---|---|
| **S23** — derived 2s10s | **+0.45** | **≤ +0.20** | **08-05** |
| **S51** — NFP → flattener | armed | 2s10s ≤ +0.20 post-print | **08-07** |
| Insurance carrier (this run's claim) | MET/PRU/TRV/STT all 4-way positive | **any of the four losing its days-21-60 base**, or MET's `vol_surge` falling below 1.20 (it would become a D126 name) | 08-12 |
| **S14 / S14-num** — MA | armed | any move inside ±3.9% is pre-declared no-information | **08-06** |
| Exchanges replacement observable | venue-minus-ratings flow spread | M135's registered RS60 test **remains BROKEN — on frozen prices it can only report CONFIRM** | 08-07 |
| **MET valuation** | fwd **8.77×** vs trailing 18.63, PEG 0.51, **−14% to a $97.75 mean target** | ⚠ **estimate momentum is NEGATIVE — current-quarter 1↑:2↓ at both 7d and 30d** | — |
| ⚠ margin percentile | **unobtainable for every insurer (C3)** | — | **no cheapness claim is made on MET** |

**Verdict: OW− HELD, carrier NAMED as the insurance/custody node and flagged as a FOURTH carrier
statement.** ⚠⚠ **M317's instability warning is not resolved by this run — it is sharpened**: the
carrier now survives an instrument filter, which is more than the previous three did, **but "the
carrier changed again" is exactly what M317 warned about, and one clean green (MET) with a negative
revision book is thin evidence.** **Stated as thin rather than sold as a discovery (P4).**
