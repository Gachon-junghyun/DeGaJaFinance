# SCENARIOS_US — brackets registered by the `industry_US` desk

> ★ **Split from `SCENARIOS.md` on 2026-07-29** (the 8-run size escalation, resolved by a human).
> **The shared spine — the status legend, the scoring rules and the MASTER SCORING LOG + MASTER
> INDEX — stays in [`SCENARIOS.md`](SCENARIOS.md) and is read IN FULL by both desks every run.**
>
> ⚠⚠ **Ownership is the registering desk, NOT the subject market, and it does not confer exclusivity.**
> **S8** was registered by the US desk and **scored by the KR desk**; **S33** was registered by KR and
> **scored by US**; **S28** likewise. **A desk with a past-dated row in the other file must open that
> file and score it** — the "score everything or log EXPIRED" rule is unchanged and un-splittable.
>
> A scenario is valid only if it was written **before** its event, carries **both** branches, and names
> a **date** and an **observable with a threshold**. Scoring is L3 `scenario_score`. Not advice.

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

### RESOLVED (scored at 2026-07-23 HANDOVER) — FIRED-A

**Observable pulled**: FY26 capex guide raised to **$195–205B** (from $180–190B) — Alphabet CFO Anat
Ashkenazi, on the call: *"the increase in the range is primarily due to an acceleration in the
delivery of capacity to meet growing demand"*; company still describes itself as **"in a
supply-constrained environment."** Q2 capex actual **$44.9B, +100% YoY** (this is the second
consecutive quarter of a capex raise). Threshold was **"FY guide lifted above $190B" → clean FIRED-A**
(the $195–205B band sits entirely above the frozen $190B line; no judgment call needed).

**Meaning for the standing view**: volume leg extends, margin-peak timing pushed later — M1 (DRAM
contract deceleration) is **unaffected**, per the scenario's own pre-registered branch-A meaning.
Feeds STANDING_VIEW M8/M9 (hyperscaler capex share of memory demand) — the $200B-midpoint guide is
the largest of the four hyperscalers reporting this window and confirms the demand side of the
memory thesis is not the contested variable (price/margin still is).

⚠ **Score the observable, not the price reaction, confirmed in the wild**: press reports **GOOGL
stock sank on the print** despite the beat-and-raise (CNBC: *"Q2 revenue beats, GOOGL stock sinks on
2026 capex hike"*) — the market is pricing capex-as-margin-drag, not capex-as-demand-signal. Both
readings can be true; this scenario scores only the line item it pre-registered.
Sources: [CNBC](https://www.cnbc.com/amp/2026/07/22/google-earnings-q2-goog-live-updates.html) ·
[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/alphabet-reports-q2-results-bell-174500671.html)

---

## S2 — The 2026-07-29 cluster · ARMED · **five** events, one day (was four — see ⚠ below)

The single most loaded date on the calendar. Three of them resolve currently-unreadable state.

| Event | Resolves |
|---|---|
| **Microsoft earnings** | Second half of hyperscaler capex (with META) |
| **Meta earnings** | ditto |
| **FOMC decision** | The duration/real-rate gate the US desk carries (`real 10Y > 2.50~2.55%` kill line; 2.31% asof 07-17) |
| **SK hynix ADR ↔ ordinary two-way conversion opens** | **Un-suspends the 000660 flow read** (STANDING_VIEW §3) and collapses the ~25% premium |
| **금융위·금감원 지배구조 선진화 방안 (8대 금융지주)** *(added 2026-07-23, see S11)* | The FIN sector's own governance/succession risk — **not previously registered anywhere in this file** |

⚠ **Added 2026-07-23, found by a `catalyst_calendar.py --days 10` re-pull** (the standard `--days 5`
MACRO pull never reaches 07-29 from 07-23, which is why this sat unregistered for at least a week
of runs even though 07-29 itself has been "the single most loaded date" since this file's first
version). Full scenario: **S11** below. Registering it here changes the stacked-tail count from
four independent triggers to **five**, all on the sector this desk has held continuously OW-tilted
(FIN) or flow-suspended (000660) since 07-16.

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

⚠⚠ **THE ADR LEG ABOVE IS SUPERSEDED — see S17 (registered 2026-07-24).** The paragraph as written
assumes 07-29 opens two-way conversion. **Korea Securities Depository's president, named and
on-record, says it does not**: the conversion ceiling is **2.5%** (not the 25% the market read off an
SEC fee estimate), 07-29 is a **share-registration** date, and *"because the ADR premium is so high
there will be no conversion demand for the time being."* Exceeding 2.5% needs a secondary-offering-
equivalent process (issuer board + regulator + SEC), the path TSMC walked 2001–2007.
⇒ **This row's observable is not scoreable as written.** S17 replaces it with the ADR premium, which
prints daily. **The 000660 flow suspension is therefore extended, not lifted on 07-29** — and dig
**D6**'s trigger date is void until S17 settles. The original text is kept per append-only.

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

## S5 — KR semiconductor exports, 1–10 August · **EXPIRED-UNSCORED — reassigned to `industry_kr` (`W1`: a KR customs series is not scoreable on a `--market us` desk)** (scored 2026-09-07 by the `industry_US` run from already-published data — `D472` header hygiene) · ~2026-08-11

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Semis up MoM on a like-for-like window | M12's MoM decline was a one-month artifact |
| **B** | **Second consecutive MoM decline** | Deceleration confirmed on an independent series (customs, not TrendForce) |

⚠ **Comparison discipline**: compare 1–10th to 1–10th, or 1–20th to 1–20th. Mixing a partial window
against a full month is how M12 got mis-cited the first time (R2).

---

---

## S6 — Intel FQ2 print · ARMED · 2026-07-23

**Why it matters here**: the only event in the window that speaks to the **equipment** leg rather than
the memory-price leg. Registered by the 2026-07-22 US PREMORTEM (B2), before the event.

**Observable (frozen)**: an **externally named** 18A/foundry customer, **or** capex/utilisation guided up.
**Implied move**: **±4.4%** — ⚠ expiry tagged **D0**, i.e. the contract expires before the print it is
meant to price. **Treat ±4.4% as a FLOOR, not a fair estimate.** The threshold is not widened for this;
the caveat is recorded so a later scorer knows the bar is conservative.
Pre-print positioning: short **2.5% of float, covering**; P/C **0.36** (call-heavy); skew +25.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | A named external customer, or capex guided up | The US equipment leg (AMAT RS60 +34.1, LRCX +18.9, KLAC +14.2 vs SPY) was a **pullback, not a downtrend** — the industry_US IT underweight is short the wrong thing |
| **B** | No customer named, capex flat | Company-specific, consistent with R5's kill of EDA-as-cycle-indicator. IT UW unaffected |

---

## S7 — RTX + LMT · ARMED · 2026-07-23 · **one binary, not two**

**S1 fold-by-date applies at registration**: both print on the same date, so "both beat" is
**n ≈ 1 effective date**. Registered by the 2026-07-22 US PREMORTEM (B3), before the event.

**Observable (frozen)**: backlog / book-to-bill at **both** names.
**Implied moves**: RTX **±5.0%**, LMT **±5.4%** (both expiry D2).

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Backlog up at **both**, and both move outside their implied bands | Restores Industrials to N+; validates the PREMORTEM-promoted DEEP ③ (defense-aero) |
| **B** | **One outside, one inside** | **Split — no verdict.** A 50-name breadth cut (wflow −0.167, 17 red of 50) is not overturned by a single primes re-rate |
| **C** | Backlog flat/down at either | Industrials N− stands |

---

## S8 — Hormuz "Strait open" / oil de-escalation · ARMED · **undated** `[blank]`

The date is not in `CATALYST_WATCH.json` and is **not guessed**. Registered 2026-07-22 (PREMORTEM B5).

**Why the naive bracket is wrong**: measured 2026-07-22, VLO RS20 **+28.6** vs RS60 **+29.0**, PSX +25.5
vs +27.4 (both vs SPY) — **~100% (VLO) and ~93% (PSX) of the entire 60-day relative gain was earned in
the last 20 days**, coincident with the 07-10 truce collapse. The refining node is currently a
**war-premium position wearing a crack-spread label**.

**Observable (frozen)**: crude vs its pre-escalation range **AND** the diesel crack.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Crude below the pre-escalation range **AND the diesel crack rolling over** | Against us. The refining lead was war premium; OW Energy loses its engine |
| **B** | **Crude falls but cracks hold** | **NOT against us** — this is input-cost relief. OW Energy stands on refining margin rather than on the war. ★ This distinction is the whole bracket |
| **C** | Escalation continues | Cracks hold; WTI COT 10%ile is squeeze fuel *conditional on the turn being visible* |

**Cross-check KPI**: WTI COT %ile, next print **2026-07-24**.

---

## S9 — The DOVISH real-rate branch · **SETTLED FIRED-B** (scored 2026-09-07 by the `industry_US` run from already-published data — `D472` header hygiene) · 2026-07-29 (FOMC) → last scoreable observation 2026-09-03. 🚨 **no terminal date was ever registered** (`D555`)

★ **The branch nothing else in the desk brackets.** The hawkish branch (real 10y **>2.55%**) is already
MACRO P1's registered anti-signal. Its mirror was un-bracketed until the 2026-07-22 PREMORTEM found that
**the book holds one levered bet on real 10y RISING, counted twice**: long P&C insurers (TRV +0.906,
CB +0.822, plus AIG/MET/PRU) **and** short Utilities/Real Estate *on a stated rising-real-yield
rationale*. Both legs lose on the same tick.

**Observable (frozen)**: DFII10 (real 10y) **with** T10YIE (breakeven) quoted alongside it — a real
yield alone hides whether the move was growth or inflation.
**State at registration**: real 10y **2.35%** (FRED asof 2026-07-20), a **120-day high**; breakeven
**2.26%** (asof 07-21); HY OAS **2.69%**; NFCI **−0.538**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Real 10y **<2.20%** with breakeven **rising** | **The wedge inverts.** UTIL/RE reverse (DUK, NEE, WELL, SPG, PLD are already not red) and the long-end leg of the Financials OW loses its driver. **Two sides of the book lose together** |
| **B** | Real 10y holds **2.20–2.55%** | Term-premium blip; the tilt survives on flow |
| **C** | Real 10y **>2.55%** | Already registered as MACRO P1's anti-signal — duration de-rate becomes a regime call |

**Stacked-tail note**: S2, S6-adjacent read-through and S9 all land on or around **2026-07-29**, and a
MSFT/META capex raise on that date would hit **three of the five underweights in one line item**
(IT + Real Estate + Utilities are one bet — the AI datacenter build-out — per the 2026-07-22 PREMORTEM).

---

## S12 — ECB rate decision · ARMED · 2026-07-23 (D-0 at registration)

Registered 2026-07-23 by the `industry_US` PREMORTEM (Lens 2), **before the decision**.
★ **Registered mainly because the calendar missed it** — `CATALYST_WATCH.json` (pulled `--days 10`
this run) contains no ECB row, the **third consecutive run** in which a same-day binary was absent
(GOOGL 07-22, INTC 07-23, ECB 07-23 — dig D18).

**Information grade: MODEST, and kept small deliberately.** The only transmission into this desk's
book is **DXY**, one of two legs under the Materials UW (the other being copper at a 95%ile COT
crowded-long, which is on the REJECTED list as a trigger). It is bracketed because it is a D-0
binary, not because it is large.

**Observable (frozen)**: **DTWEXBGS (Broad Dollar)** against its 120-day range **[117.44, 121.41]**.
Last print **120.53 (FRED, asof 2026-07-17)**. ⚠ **No options contract exists for this event**, so the
threshold is the measured range boundary and is declared as such rather than invented.
Narrative state at registration: fxstreet — *"European Central Bank set to hold interest rates amid
cooling inflation and weaker growth"*; thread BUILDING 6 days (3→3→5→8→3→8 outlets); `ECB` term
velocity **104 hits in 1 day vs a 41/day 7-day average = 2.5×**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Hawkish surprise ⇒ DTWEXBGS closes **below 117.44** within 3 sessions | **Against us.** The Materials UW loses its dollar leg; FCX (flow −0.203) gets a tailwind despite crowded positioning |
| **B** | Hold-with-dovish-tilt ⇒ DXY stays in the upper half of [117.44, 121.41] | With us. MATR UW intact, carried by copper positioning **as context, never as the reason** |

**Invalidation**: DTWEXBGS closes outside [117.44, 121.41] within 3 sessions (either edge).

---

## S13 — ★ MSFT + META capex, and the branch nothing in the book brackets · ARMED · 2026-07-29

Registered 2026-07-23 by the `industry_US` PREMORTEM (§5), **before the event**.
**This is the most valuable registration of the run**: the desk brackets a capex *cut* (STANDING_VIEW
§4) and a capex *raise*, but has never bracketed **a raise the market prices as a margin drag anyway.**

**Precedent, already scored**: GOOGL raised FY26 capex to $195–205B — **S1 FIRED-A** — and the stock
**fell** on the print. That is the desk's *"score the observable, not the price reaction"* rule firing
in the wild, **once**. S13 asks whether it fires a second time, and what that means.

⚠ **No usable implied move exists.** `module_flow --positioning` (2026-07-23) returns META **±4.4%**
and MSFT **±2.9%**, both **expiry 2026-07-24 — before the 07-29 event.** They are **not event-priced**;
they are structurally disconnected. **Any threshold taken from them would be fabricated**, so this
scenario uses a categorical observable instead and says so.

**Observable (frozen), a CROSS-CONDITION — all three legs measured over the 10 sessions after the
print (to ≈2026-08-12)**:
1. the **capex guide** at MSFT and META (raised / held / cut) — the categorical line;
2. the **spenders'** NTM P/E change (MSFT, META);
3. the **suppliers'** median **RS20 vs SPY** (MU, AMAT, LRCX, KLAC) — benchmark named (C1).

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Capex **raised** AND spender NTM P/E **compresses** AND supplier median RS20 vs SPY **turns positive** | ★ **Info Tech's single N label is wrong on BOTH halves at once**: the spenders deserve more underweight (on multiple compression, not demand) and the suppliers deserve less (protected by the same raise). IT must be split, exactly as R7 split Real Estate and M26 split Industrials |
| **B** | Capex **raised** and the spenders hold their multiple | The raise is read as demand. IT's single label survives; **low information** by the pre-registered asymmetry (a raise only moves timing) |
| **C** | Capex **cut** at either | **High information.** Breaks the volume leg and the price leg together, extends past memory into **AVGO, NVDA, TSM** (all held in the real book), and reopens COMM N− / IT N as too benign |

**Why this bracket exists at all (L3 information-content test)**: branch B cannot change the
conclusion; branches A and C both can. That asymmetry is the justification — an event where no branch
would change anything is not worth bracketing.

**Prior**: A or B far more likely than C. `[inferred]`

---

## S14 — Mastercard Q2 · **SETTLED A-PARTIAL (branch B ruled out; A price leg MET, fundamental leg unretrievable — `D556`)** (scored 2026-09-07 by the `industry_US` run from already-published data — `D472` header hygiene) · 2026-07-30 · the Financials-breadth test

Registered 2026-07-23 by the `industry_US` PREMORTEM (Lens 2), before the event. It exists to settle
**DEEP ②'s own question**, not as a single-name view.

**Why**: this run restored **Financials to OW on one number** — **eqflow +0.320 > wflow +0.253**, the
only breadth-led sector on the board (`SECTOR_FLOW_US.json §sector_rotation`, asof 07-22 close). But
the flow leaders inside it are **TRV +0.933 · PYPL +0.772 · MCO +0.733 · USB +0.690 · CB +0.685 ·
MA +0.622 · V +0.603**, against money-centers **GS −0.057** and **C −0.672 🔴**. That is a
**payments + insurance cluster**, which is a *concentration* wearing a breadth label unless it holds.

⚠ **No implied-move figure was available for MA at registration** — flagged, not invented.

**Observable (frozen)**: MA's **cross-border volume growth**, plus the **RS20 vs SPY** of {MA, V, PYPL}
over the 5 sessions after the print.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Cross-border volume holds, and {MA, V, PYPL} RS20 vs SPY stays positive | Genuine breadth confirmed. FIN OW survives on the reason this run gave it. The bank-vs-payments split still needs separate resolution |
| **B** | Volume misses, and **{MA, V, PYPL} RS20 vs SPY flips negative within 5 sessions** | **Against us.** The "breadth" was a **consumer-spend concentration**, and FIN OW loses the *second* of its two reasons — the first (2s10s steepening) already broke on 2026-07-23 |

**Invalidation**: branch B's RS20 condition, measured to **2026-08-06**.

---

## S15 — June PCE · ARMED · 2026-07-30 · the frontal test of P1's framing

Registered 2026-07-23 by the `industry_US` PREMORTEM (Lens 2), before the event.

**Why it matters here**: this run's **P1** claims the front-end repricing is a **reaction-function**
trade, **not** an inflation trade — anchored on the 2y at **4.26% (a 120-day high)** and 2s10s
**flattening −2bp**, against **core CPI −0.02% MoM and headline −0.42% MoM** (both halves quoted, C2)
and unemployment **4.2%**. PCE is the independent series that can break that reading.

⚠ **No options threshold exists for a PCE print in this desk's toolkit** — the numeric line below is
**judgement, and is flagged as such** rather than dressed as a measurement.

**Observable (frozen)**: **core PCE MoM**, read against core CPI's already-printed **−0.02% MoM**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Core PCE MoM **> +0.3%** — a clean break from CPI's direction | **Against us.** P1's "reaction-function, not inflation" collapses; the FIN OW's logic is hit and Cons. Discretionary N− deepens. Also makes 2026-07-23's un-decomposable 10y move (nominal 4.71% on a +5.2% crude day) retrospectively an inflation event |
| **B** | Core PCE MoM **≤ +0.3%**, in line with the CPI cool-down | P1 stands, and reinforces S9's real-rate bracket |

⚠ **Score the observable, not the market reaction**, and quote **both halves** (YoY and MoM) on a
like-for-like window when scoring — rule **C2**, which exists because a half-quoted print (R2) already
cost this desk once.

---

## S16 — Meta Q2 · ARMED · 2026-07-29 · the sector-vs-name separation test

Registered 2026-07-23 by the `industry_US` PREMORTEM (Lens 1), before the event.

**Why**: Comm Services was marked **N−** on 2026-07-23 because *"the #1 event of the day is a $1.9B
regulatory hit to the sector's largest constituent"* — the EU's **$1B Play + €890m search** decisions,
which land on **Alphabet**, not Meta. That is **n≈1 (S1)**, a single-name regulatory event carried as
a 13-name sector verdict. Measured on the 07-22 close, the sector's two largest names moved **opposite
ways**: **GOOGL 🔴분산, RS20 −3.1 vs SPY**, against **META 🟢가속 · new_green, RS20 +9.7 vs SPY**, with
META at fwd P/E 16.5, PEG 0.94 and FY revision breadth **3↑:0↓ over 30 days**.

⚠ **META's ±4.4% straddle expires 2026-07-24, before this event** — **not event-priced**, so no
magnitude threshold is taken from it (same defect as S13).

**Observable (frozen)**: META's **capex guide** (the S13 line item) **and** the RS20 vs SPY spread
between **META** and the equal-weight of {MSFT, AMZN, AAPL}, over the 10 sessions after the print.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | META's RS20 vs SPY stays **above** the {MSFT, AMZN, AAPL} equal-weight through 2026-08-12 | The Comm Services N− was a **single-name** verdict misapplied to a sector. The 13-name label is the wrong unit (W5) |
| **B** | META's RS20 vs SPY falls **to or below** that equal-weight | The sector-level read was right for a reason other than the fine — most likely the S13 margin-drag channel, which would then be a **cohort** effect, not a GOOGL-specific one |

⚠ **RS60 vs SPY is still −11.8 at registration**, i.e. this is a **20-day inflection, not an
established trend** — the weakest admissible form of the A-grade signal, and stated as such (C4).


---

## S19 — ★★ FOMC 2026-07-29 · the **HIKE** branch no registered scenario contains · **SETTLED FIRED-M** (scored 2026-09-07 by the `industry_US` run from already-published data — `D472` header hygiene) · numeric legs closed 2026-08-05

Registered **2026-07-24 by the `industry_US` PREMORTEM (Lens 2), before the event.**

**Why it exists.** S9's grid is real-10y `<2.20 / 2.20–2.55 / >2.55`; S2 branch C is *"either cuts, or
real 10Y closes >2.55%"*; S15 is core-PCE MoM. **No branch of S1–S18 contains "the target range is
raised."** Verified by reading every armed row. The market prices a hike at **34.7%** five days out.

**State at registration** `[FRED, asof 2026-07-22]` · `[news, body-drilled]`:
- **CME FedWatch implied hike probability: 10.7% (07-15) → 34.7% (07-22)** — tripled in five sessions.
- **DGS2 4.31% = 120-day high** · **DFII10 2.39% = 120-day high, quoted with T10YIE 2.28% (flat)** ·
  2s10s **+0.36, flattening a second session** · HY OAS **2.68%** · NFCI **−0.552** loosening a 5th week.
- Named driver, TD Securities on record 07-23: *"pricing for rate hikes moved alongside **oil**"*, and
  the pricing is *"excessive… the second-largest deviation between market pricing and actual Fed
  action in the past decade"* — they hold a **receive July OIS** position, i.e. they fade it.

**Observable (frozen)**: (i) the **target-range decision** (categorical: raised / held / cut);
(ii) **DGS2**, with **DFII10 quoted alongside T10YIE** (S9's own rule — a real yield alone hides
whether the move was growth or inflation).
⚠ **No options instrument exists for an FOMC decision in this toolkit.** The numeric thresholds below
**reuse P1's already-registered levels** rather than being invented for this bracket, and that is
stated rather than dressed up as a measurement.

| Branch | Observable | Meaning — which of OUR tilts is hit |
|---|---|---|
| **H** | Target range **raised**, OR held with **DGS2 closing >4.45% by 2026-08-05** | **Against the OW Health Care**, which was moved to OW this run on flow that is **mega-cap-shaped (wflow +0.396 > eqflow +0.197)** — a discount-rate shock hits that leg first. Starter list: LLY, MRK, JNJ, ABBV |
| **D** | Held **with dovish language**, and **DGS2 closes <4.15% by 2026-08-05** (= P1's registered anti-signal) | ★ **Four tilts lose together**: OW Energy **+** N− Utilities **+** N− Real Estate **+** N− Cons. Staples. Measured basis: SPY-residual correlation, 251 trading days to 07-23 — **XLU–XLRE +0.538, XLRE–XLP +0.565, XLU–XLP +0.385**, all against **XLE–^TNX +0.326** (opposite sign, same axis) |
| **M** | Held, DGS2 stays **4.15–4.45%** | No conclusion changes |

**Bracket invalidation**: **HY OAS >3.10% on a close** (P2's registered line) — then it is a credit
event and the rate attribution is void.
⚠ **n≈1 warning, pre-registered**: FOMC 07-29 and June PCE 07-30 **share one driver (oil), one day
apart. They are not two observations.**

---

## S20 — UPS Q2 · ARMED · 2026-07-28 (D-4) · the window's first binary, and it is two tests at once

Registered **2026-07-24 by the `industry_US` PREMORTEM (Lens 2), before the event.**

**Why it matters twice**: (i) UPS is **dig D23's last unread refiner customer** — the W4 test the desk
has carried open for two runs, with DAL/UAL/FDX/LUV already measured at **fuel costs +66% to +84% YoY**;
(ii) it is the **freight-volume falsifier** of the rail/freight node this run's PREMORTEM promoted to
DEEP ④ (CSX +0.878, UNP +0.867, NSC +0.767 — the top three flow scores in a 50-name Industrials sector).

**Observable (frozen, categorical)**: does the Q2 call **quantify fuel expense YoY**, and is FY
guidance cut on **fuel** or on **volume**?
⚠ **Implied move ±1.3–1.7%, expiry 2026-07-24 (D0) — it expires BEFORE the print. NOT event-priced.**
No magnitude threshold is taken from it; the observable is categorical for exactly that reason.
State at registration: UPS flow **+0.563**, RS20 **+6.8** / RS60 **+2.2 vs SPY**, OBV 매집,
short **3.1% float covering**, mean-target upside **+0.3%**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Fuel expense quantified up materially YoY **and** any guidance cut attributed to fuel | W4 closed at 5 of 5. Real dollars move through the crack at the largest US distillate buyer — the "paper crack" objection dies |
| **B** | Fuel is a **non-event** in the call | **Against us.** The distillate bottleneck is absent from the P&L of the buyer most exposed to it ⇒ the crack is a price, not a cost anyone is paying |
| **C** | Guidance cut on **VOLUME** | **Against the promoted rail DEEP.** Freight demand, not defense, is what the sweep says Industrials' money is in — a volume cut falsifies it directly. Read-through: CSX, UNP, NSC, URI |

---

## S21 — STNG Q2 · ARMED · 2026-07-30 · delivers S8 branch A **without** a Hormuz statement

Registered **2026-07-24 by the `industry_US` PREMORTEM (Lens 2), before the event.**

**Why**: **S8 is undated by construction** (*"the date is not in CATALYST_WATCH and is not guessed"*),
so its branch A has no scheduled way to arrive. STNG's print gives one. And it tests **M45** — the
desk's measured case that *"the blockade's literal beneficiaries are not being bought"* — on the
company's own numbers rather than on its RS.

**Observable (frozen)**: Q2 **TCE $/day**, and the **percentage of Q3 days already booked**.
★ **Implied move ±10.0%, expiry 2026-08-21 (D28) — USABLE.** It is one of only **two** event-covering
straddles on the entire board today (the other is MPC ±11.2%, same expiry); the other eight names
pulled this run all expire 2026-07-24, before their events.
State at registration: STNG flow-tagged 🟡, **RS20 +5.8 / RS60 −4.8 vs SPY**, news velocity **0.00×**,
short **5.4% of float, BUILDING**, P/C 1.06, skew +6.2. On the reject ledger as `A.flow미도착` since
2026-07-23, recheck 2026-08-06.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | TCE **flat or down** and Q3 booked days **below** Q2 | **Against us.** The Red Sea rerouting rent has already peaked ⇒ **S8 branch A arrives with no Hormuz statement**, and the OW Energy's war-premium half is confirmed as the driver rather than the margin |
| **B** | TCE **up** and Q3 bookings **at or above** Q2, with a move **outside ±10.0%** | The blockade is being paid for in cash, not just narrated — and M45's "not being bought" becomes a genuine dislocation rather than a correct market judgment |
| **C** | Inside ±10.0% either way | **No information** — the move is already priced. Pre-committed here so an in-band reaction cannot later be read as confirmation |

**Cross-check KPI**: the settled 3-2-1 crack (frozen at **66.49**, settled 2026-07-23) holding **≥65**
through 2026-08-06 invalidates branch A's read-across to refining.

---

## S14-ANNEX — ★ pre-registered contamination notice (NOT a rewrite of S14)

Registered **2026-07-24 by the `industry_US` EVENT_ALPHA/PREMORTEM, BEFORE S14's 2026-07-30 event.**

**S14's frozen observable includes {MA, V, PYPL} RS20 vs SPY staying positive.** Measured today,
**PYPL carries RS20 +31.2 vs SPY — the highest of all 71 volume-blocked names in the 300-name
universe** — and the body-read shows why: **Stripe bid $53B for PayPal on 2026-07-15 and PayPal's
board held out for a higher price on 07-20; the deal is unaccepted.** Corroborated on the
fundamental axis: **PYPL's estimates are being CUT while its RS20 leads the board** — next-quarter
revision breadth **0↑:4↓** and current-year **0↑:3↓** over 30 days, and it trades **5.5% above** its
mean target. That RS20 is a **merger-arb spread, not payments breadth.**

⚠⚠ **S14 IS NOT RE-FROZEN.** Moving a registered observable after the fact is exactly what L3
`scenario_score` forbids, and doing it would convert a forecast into a description. Instead:
- **S14 will be scored on 2026-08-06 exactly as originally frozen**, PYPL included;
- **alongside it, the `{MA, V}`-only reading will be recorded**, pre-registered here, before the event;
- if the two readings disagree, **that disagreement is the finding** — it measures how much of
  "Financials breadth" was a takeover spread.

**Registration-discipline defect logged as D50**: *before freezing a multi-name observable, check each
leg for a live corporate action.* Fourth registration defect in nineteen scenarios (D28: a price
reaction inside an observable's branch · D35: a grid written on two axes · D46: an invalidation window
shorter than the observable's publication lag · D50: a contaminated leg).

---

## Scoring-log rows added 2026-07-24 by the `industry_US` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S12** | 2026-07-23 (PREMORTEM) | 2026-07-23 | — **STILL PENDING** | re-checked 2026-07-24 | **The frozen observable has still not printed.** `DTWEXBGS` reads **120.5315 asof 2026-07-17** — byte-identical to its value at registration, 7 calendar days ago; 120-day range confirmed unchanged at **[117.4396, 121.412]**. Re-check deadline **2026-07-28**; if it still has not printed, score **`AMBIGUOUS`** with the reason and **do NOT substitute a proxy**. ★ **New defect D46**: a **3-session** invalidation window was written on a series with a **~5-business-day publication lag** — the bracket cannot settle inside its own window by construction. Narrative state, unscoreable but directional: *"US Dollar Index: Higher yields and FOMC focus lift DXY"* [fxstreet, single-source tier] |
| **S19** | **2026-07-24 (industry_US PREMORTEM)** | 2026-07-29 | — | — | ARMED — ★ the **hike** branch; verified absent from every one of S1–S18 |
| **S20** | **2026-07-24 (industry_US PREMORTEM)** | 2026-07-28 | — | — | ARMED — the window's first binary; closes W4/D23 **and** falsifies the promoted rail DEEP |
| **S21** | **2026-07-24 (industry_US PREMORTEM)** | 2026-07-30 | — | — | ARMED — ★ one of only **two** event-covering straddles on the board (**±10.0%, D28**); delivers **S8 branch A** without a Hormuz statement |
| **S14-annex** | **2026-07-24 (industry_US)** | 2026-07-30 (scored 08-06) | — | — | ARMED — S14 stays frozen as written; the **{MA, V}-only** reading is pre-registered alongside it |

## Scenarios registered 2026-07-25 by the `industry_US` PREMORTEM (frozen at registration)

> All thresholds below are **frozen 2026-07-25, pre-event**. Benchmark **SPY** inline (C1).
> ⚠ **Date-provider conflict declared, not resolved (D5)**: this desk carried MSFT/META 07-29 and
> AMZN 07-30; the `yfinance` calendar returns **MSFT 07-30 · META 07-30 · AMZN 07-31 · V 07-29 ·
> STX 07-29 · EQIX 07-30 · XOM 07-31 · PSX 08-05**. Every bracket below is therefore written on an
> **observable with a window**, never on a single calendar day, so a 1-day error cannot void it.
> ★ **D54 CLOSED: EQIX prints 2026-07-30** — it was `[blank]` in every calendar this morning.

## S20-ANNEX — UPS Q2 · 2026-07-28 · numeric annex to S20 (**S20 is NOT re-frozen**)

S20 was registered when UPS's only straddle expired before its event. **A covering one now exists:
±6.9%, expiry 2026-07-31 (D6) = 4.04× its own daily σ20 (1.71%) and 1.81× √5·σ20 ⇒ genuinely
event-priced** — the only such instrument among the window's US binaries. Registered as a parallel
numeric line per the **S14-ANNEX precedent**; S20's categorical observable stands exactly as written.

- **Branch A (with us)**: fuel cost quantified materially higher YoY ⇒ **W4/D23 closes 5 of 5** (the
  refiners' last unread customer).
- **Branch B (against us)**: **guidance cut on VOLUME, not on fuel.** ⇒ **INDU N is false comfort** —
  ROTATION §2 states the downgrade was on the *label*; the rail node (CSX +0.878 · UNP +0.867 ·
  NSC +0.767) is explicitly untouched by it. The desk is not underweight what would break.
- **Frozen observable**: median **RS20 vs SPY** of {CSX, UNP, NSC}.
- **Frozen threshold**: that median **turns negative by 2026-08-04**.
- ⚠ **Pre-declared no-information**: any UPS same-day move **inside ±6.9%**.
- **Rips on B (downside)**: CSX · UNP · NSC · ODFL. ★ **UNP is double-hit** — about 8 of its 12
  revenue growth points are **fuel surcharge (M91)**, so a volume cut plus a rolling crack is one
  shock counted twice.
- **Invalidation**: HY OAS >3.10% on a close, or a named one-off (labor/charge) in the release.
- Pre-print context `[measured, module_fundamentals_us 2026-07-25]`: current-quarter consensus
  **$1.66, +4.5%/90d, breadth 1↑:0↓**; FY26 **$7.13**; short **3.1% float COVERING, DTC 4.3**,
  **P/C 0.35, skew +11.1 ⇒ the option market is priced for calm on the desk's own registered falsifier.**

## S23 — ★ FOMC 2026-07-29 · the **BEAR-FLATTENER HOLD** branch neither S19 nor S9 contains

S19 brackets a **hike** (DGS2 > 4.45); S9 brackets a **dovish** real-rate fall (real 10y < 2.20).
**Neither contains "hold, DGS2 stays inside 4.15–4.45%, and the curve flattens further"** — under
which net interest margin dies without tripping either registered threshold. S19's branch M
("no conclusion changes") is therefore a **false null for the FIN OW**, whose steepener leg already
broke on 2026-07-23 (R11), leaving it standing on breadth alone.

- **Branch A (with us)**: the curve holds or re-steepens; the FIN OW's remaining leg survives to S14.
- **Branch B (against us)**: a hold with a further flattening.
- **Frozen observable**: **T10Y2Y** on a close, with **DGS2 quoted alongside** (S9's two-series rule).
- **Frozen threshold**: **T10Y2Y ≤ +0.20 by 2026-08-05, with DGS2 inside 4.15–4.45%.**
- ⚠ **No options instrument exists for an FOMC decision in this toolkit** — stated, not dressed up.
- **Tilts hit**: **FIN OW (both remaining legs)** — ★ **and UTIL UW loses on the same tick**, which
  makes them **one rate bet carried with opposite signs**.
- **Rips on B**: WELL · PLD · AMT · **PCG** (Utilities' only 🟢, `new_green`, delta +0.448) · DUK.
- **Invalidation**: HY OAS >3.10% on a close (then it is S26, not a curve event).

## S24 — ★ MSFT/META/AMZN capex 2026-07-29→31 · the **UTILITIES** leg nobody bracketed

S13 aims at IT and S16 at COMM — **both are N today**, so neither branch moves the board much. The
tilt actually exposed to a capex raise is **UTIL UW**, which is a levered short on AI capex.

- **Branch A (with us)**: capex raised and the physical layer keeps being distributed, so EVENT_ALPHA
  Card 3's decoupling holds and the UW is right.
- **Branch B (against us)**: capex raised **and the physical layer re-rates**, inverting Card 3.
- **Frozen observable**: median **RS20 vs SPY** of {VST, CEG, GEV, VRT}.
- **Frozen threshold**: that median **> 0 by 2026-08-12** (matching S13's own 10-session window).
- ⚠⚠ **n ≈ 1, declared at registration**: SPY-residual over 499 days gives **VST–CEG +0.768 ·
  GEV–VRT +0.601 · VST–GEV +0.490 · VST–NVDA +0.354** ⇒ **this is one unit's return, not four
  observations.**
- ⚠ **No price threshold is admissible**: MSFT ±1.7% = **0.84σ**, META ±2.1% = **0.61σ**,
  AMZN ±1.6% = **0.88σ** of their own daily σ20 — **all three price less than one ordinary session,
  and all three expire 2026-07-27, before their events (M89, 4th run).**
- **Rips on B**: VST · CEG · GEV · VRT · ANET (2nd tier PWR · CIEN · NEE).
- **Invalidation**: a capex **cut** at either (= S13 branch C), in which case the UW is right for the
  reason already held and this bracket is void.

## S14-num — Mastercard Q2 · 2026-07-30 · numeric annex (**S14 and S14-ANNEX are NOT re-frozen**)

MA's straddle **covers** its event (±3.9%, expiry 07-31, D6) but charges only **1.09× ordinary
realized** (σ20 1.60%; 2.44σ) — **the market is pricing this print at almost nothing, and that is
itself the finding.**
- ⚠ **Pre-declared no-information**: any MA same-day move **inside ±3.9%**. It **may not be read as
  confirming the FIN OW.**
- S14's branch B (a volume miss with {MA, V, PYPL} RS20 vs SPY flipping negative by 2026-08-06)
  **stands exactly as frozen, PYPL contamination included.**
- ★ Registered alongside: **MA/V is a DIFFERENT SPY-residual unit from JPM/TRV/CB** — MA–JPM +0.238,
  TRV–MA +0.382 — so an MA miss does not read across to the FIN OW's other survivors.
- Pre-print context `[measured]`: MA current-quarter **0↑:1↓**, CY EPS **+0.4%/90d** — a flat book.
- **Rips on branch B**: WELL · PLD · AMT · SPG · VTR (a consumer-spend miss is a growth scare).

## S25 — ★ RE OW− · undated → 2026-08-08 · **the tilt is carried by the least representative name**

Real Estate went **N → OW−** in this run's ROTATION largely on **DLR's delta +1.099** (the largest
single-name delta of all 300). **DLR has no event in the window — it already printed on 07-23**
(revenue +29% YoY, adjusted FFO $2.65 vs $1.86, FY guide raised, $3.5bn Blackstone acquisition).

- ★ **Measured, SPY-residual, 499 days**: **XLRE–PLD +0.714 · XLRE–AMT +0.712 · XLRE–WELL +0.652**
  against **XLRE–DLR only +0.456**, with DLR–PLD +0.213 · DLR–AMT +0.260 · DLR–WELL +0.254 ⇒
  **{DLR, EQIX} is a separate unit at every threshold at or below 0.65.**
- **Frozen observable**: **DLR RS20 vs SPY** and the **{PLD, AMT, WELL} median RS20 vs SPY**,
  reported **separately and never merged**.
- **Frozen threshold**: **by 2026-08-08, DLR RS20 vs SPY falls below that median while the median
  stays positive** ⇒ the OW− was a **data-centre bet mislabelled as a sector verdict**, and it
  contradicts R7's own 19.1pp spread (5 replications).
- ⚠ DLR is simultaneously the board's **most complacent instrument**: implied ±3.9% = **0.57× its own
  realized**, short **0.0% of float**, P/C **0.08**.
- **Rips on branch B**: WELL · VTR · SPG · IRM · PLD. ⚠ **HANDOVER §7a: WELL, AMT and VTR carry ZERO
  ledger reports.**
- **Invalidation**: a second Blackstone-scale transaction, or a DLR re-print before 08-08 (n≈1,
  re-register).
- ★ **Second settling point, newly dated**: **EQIX prints 2026-07-30** (D54 closed).

## S26 — ★★ The credit escape hatch · undated → 2026-08-12 · a **BRANCH, not an invalidation**

**Every bracket in this book — S19, S9, and four of the six written today — lists `HY OAS > 3.10%`
as an *invalidation*** ("then it is a credit event and the rate attribution is void").
**That converts the desk's single largest correlated exposure into a get-out-of-jail card.**

The correlated-tilt audit (`scripts/risk_units.py`, SPY-residual, **499 aligned days, ARI 1.00**)
shows the three OW tilts are **genuinely three units** — XLF–XLE **+0.188**, XLF–XLRE **+0.307**,
XLE–XLRE **+0.134**; between-group 0.118 vs within-group 0.576; **they never merge at any threshold
from 0.55 to 0.85. The labels are honest.**
⚠ **But that independence is conditional on SPY, and a credit shock IS the SPY factor.** Betas:
**JPM 0.932 · XLF 0.789 · DLR 0.769 · PLD 0.766 · PSX 0.747 · MPC 0.689 · XLE 0.529 · XLRE 0.463.**
⇒ **Three units, one shared beta — and the registered response to the one event that hits all three
was to declare the brackets void rather than to record being wrong.**

- **Branch A (with us)**: spreads hold below 3.00%; the three tilts remain three bets.
- **Branch B (against us)**: an index-level credit widening; all three OW carriers lose together.
- **Frozen observable**: **HY OAS (FRED `BAMLH0A0HYM2`)**, with **NFCI quoted alongside**.
- **Frozen threshold**: **HY OAS at or above 3.10% on a close by 2026-08-12, with NFCI turning
  positive WoW.**
- ⚠ **No options instrument covers this** — stated.
- State at registration: **HY OAS 2.77% (already +9bp on 07-23, its first material widening in six
  runs), NFCI −0.552 loosening a 5th week — the only direction with room is wider.**
- **Rips on B**: the low-beta side — **WELL (beta 0.224) · AMT (−0.054) · XOM (0.256) · CB (0.125) ·
  TRV (0.339)**. ★ **CB and TRV sit INSIDE the FIN OW: it carries an internal hedge its label hides,
  and it is the only tilt on the board that does.**
- **Invalidation of this bracket**: widening driven by a single issuer or sector default rather than
  index-level (idiosyncratic, re-register).

## Brackets considered and DROPPED 2026-07-25, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| June PCE (S15) as a standalone bracket | **S19 already pre-registered that FOMC 07-29 and PCE 07-30 share one driver (oil), one day apart, and are not two observations.** Folded into S23. **S15 stays ARMED as frozen** |
| AMZN 2026-07-30/31 standalone | Its only tilt link is **DISC N−**, which was declined-to-UW on delta +0.088 being 2nd-best on the board; a print does not address that. **Neither branch changes a conclusion.** Absent from `CATALYST_WATCH`; straddle 0.88σ and pre-event |
| S19 branch H | It attacks *"the OW Health Care."* **HLTH is N− today**, downgraded twice since S19 was written, so it is low information **for this board**. Scoring note only; **S19 is NOT re-frozen** |
| MATR UW · STPL N | **No binary in the window touches either.** Stated rather than manufactured |
| DLR's straddle as a standalone bracket | It covers no event (DLR already printed). Retained only as the **complacency measurement inside S25** |

## Scoring-log rows added 2026-07-25 by the `industry_US` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S12** | 2026-07-23 (PREMORTEM) | 2026-07-23 | — **STILL PENDING (3rd check)** | re-checked 2026-07-25 (US) | `DTWEXBGS` reads **120.5315 asof 2026-07-17** — byte-identical to registration, **9 calendar days unprinted**; 120d range unchanged [117.44, 121.41]. **Re-check deadline 2026-07-28**; if still unprinted score **`AMBIGUOUS`** with the reason and **substitute no proxy** (D46: a 3-session window on a ~5-business-day-lag series cannot settle by construction). Decision axis already `AMBIGUOUS` (D35) |
| **S20-ANNEX** | **2026-07-25 (industry_US PREMORTEM)** | 2026-07-28 | — | — | ARMED — numeric annex; **S20 not re-frozen**. ★ The window's **only genuinely event-priced straddle** (1.81× realized) sits on the desk's own registered falsifier, and the option market is **complacent** on it (P/C 0.35, skew +11.1) |
| **S23** | **2026-07-25 (industry_US PREMORTEM)** | 2026-07-29 | — | — | ARMED — ★ the **bear-flattener hold**; verified absent from S19 and S9. Hits **FIN OW and UTIL UW on the same tick** |
| **S24** | **2026-07-25 (industry_US PREMORTEM)** | 2026-07-29→31 | — | — | ARMED — the **Utilities** leg of the capex binary. ⚠ n≈1 declared at registration (VST–CEG +0.768) |
| **S14-num** | **2026-07-25 (industry_US PREMORTEM)** | 2026-07-30 | — | — | ARMED — numeric annex; **S14 and S14-ANNEX not re-frozen** |
| **S25** | **2026-07-25 (industry_US PREMORTEM)** | undated → 2026-08-08 | — | — | ARMED — ★ turns this run's **own RE upgrade** into a falsifiable claim about which unit granted it |
| **S26** | **2026-07-25 (industry_US PREMORTEM)** | undated → 2026-08-12 | — | — | ARMED — ★★ **converts the book's universal invalidation clause into a scoreable branch.** Written because a get-out-of-jail card is how a desk keeps its wins and forgets its losses |

---

## Scoring-log rows added 2026-07-27 by the `industry_US` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S12** | 2026-07-23 (PREMORTEM) | 2026-07-23 | — **STILL PENDING (5th check)** | re-checked 2026-07-27 (US) | `DTWEXBGS` reads **120.5315 asof 2026-07-17** — byte-identical for **10 calendar days**; 120d range unchanged **[117.4396, 121.412]**. ⚠ **The 07-27 KR run pre-declared that "a 5th carry IS a scoring failure and must be logged as one" — this is the 5th carry and it is logged as one.** Root cause is **D46** (a 3-session invalidation window written on a series with a ~5-business-day publication lag cannot settle by construction), not inattention. **NOT scored early**: the frozen deadline is **2026-07-28** and a print tomorrow could still carry a post-event value; moving a verdict forward to tidy the ledger is the same class of act as moving a threshold. **The next desk to run on or after 2026-07-28 scores it `AMBIGUOUS` if still unprinted — no proxy, and no 6th carry is available.** Decision axis already `AMBIGUOUS` (D35) |
| **S8** | 2026-07-22 (PREMORTEM) | undated | — **ARMED, deliberately NOT scored** | 2026-07-27 (US) | ★ The day's #1 event (54 art / 19 outlets) was *"Oil prices plunge as US and Iran pause strikes over Strait of Hormuz"*, and **scoring branch A off it would have been scoring the price reaction instead of the frozen observable.** Two independent bodies say the **strait REMAINS CLOSED** (cnbc: *"remains closed as the U.S. maintains its ongoing blockade"*; dw: *"Iran rules out US talks as Hormuz Strait remains closed"*), Deutsche Bank says traffic *"remains severely disrupted"*, and the pause is 3 nights old with side-fronts escalating. **S8's observable is a settled-price comparison and no settled bar exists** (the US session was 1 minute old at run clock). **Scoring line frozen NOW, pre-outcome, for the settled 2026-07-27 close**: *branch A* if the 3-2-1 crack < 60 **and** the distillate crack < 80; *branch B* if crude falls while the **distillate crack holds ≥ 84**; otherwise **AMBIGUOUS**. Context (unsettled, inadmissible as a measurement): the 07-27 intraday tape had crack **61.665** and distillate **85.614** with the diesel−gasoline gap **widening to 35.92** |
| **S30** | **2026-07-27 (industry_US PREMORTEM, Lens 2)** | 2026-07-29 → 08-05 | — | — | ARMED — ★ the **supplier** leg's 20-vs-60-day split, which S13 (a spender bracket) does not contain; full bracket below |
| **S31** | **2026-07-27 (industry_US PREMORTEM, Lens 2)** | → 2026-08-05 | — | — | ARMED — ★ brackets the **book's own held Energy expression**, which S8 (a commodity bracket) does not |
| **S32** | **2026-07-27 (industry_US PREMORTEM, Lens 2)** | 2026-07-28 COT → 07-31 | — | — | ARMED — ★★ the **positioning** branch; M125's 79-percentile-point spread has been carried three runs and bracketed nowhere. ⚠ Registered as an observable to be **scored**, explicitly NOT as a signal (COT contrarian is in the REJECTED ledger, D6) |

⚠ **Bracket-ID collision caught pre-write**: Lens 2 proposed these as S27–S30, but **S27 · S28 · S29 were
taken the same morning by the concurrently-running `industry_kr` desk.** Renumbered to **S30 · S31 · S32**
before registration — the same failure class that forced **R19**'s renumbering at run end, caught earlier
this time. **Proposal for a human: allocate scenario IDs from a shared counter rather than from each run's
own count.**

## S30 — ★ The SUPPLIER leg's 20-day reversal · ARMED · 2026-07-29 → 2026-08-05

Registered **2026-07-27 by the `industry_US` PREMORTEM (Lens 2), before the event.** All numbers
`asof 2026-07-24 settled`, benchmark **SPY** inline (C1).

**The gap it fills.** **S13** brackets a capex raise priced as a margin drag **at the spenders**;
**S16** does the same for one COMM name. **Nothing in S1–S29 brackets the supplier leg's own
20-vs-60-day split** — which is **C8**'s live form and the direct test of **M149** (*"a positive RS60
can be a decaying stock of past excess"*).

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | median **RS20 vs SPY of {STX, MU, WDC}** crosses **above 0 by 2026-08-05** | The 60-day run was pausing, not topping. **M149's decaying-stock reading is falsified**, and the IT-Neutral's implicit "wait for the 08-19→09-07 roll-off" defence is wrong for the whole stack |
| **B (with us)** | that median stays **≤ 0** through 2026-08-05 | The reversal continues; M149 is confirmed and the roll-off defence holds |

- **State at registration**: STX **−17.6** · MU **−24.7** · WDC **−23.7** ⇒ **median −23.7**.
- ★ **Control pair, registered INSIDE this bracket rather than as a second one**: **DELL (RS20 +6.2 /
  RS60 +108.6)** and **HPE (+1.4 / +66.8)** — the only two names whose 60-day excess sits in days 21–60
  rather than the last 20 (M149: **+5.9%** and **+2.2%**). **If the memory median turns while DELL/HPE
  do not, it is a memory event; if both turn, it is an IT-beta event.**
- **Implied move**: **STX ±14.6% (expiry 2026-07-31, D4, skew −5.8)** — ⚠ **any STX move inside ±14.6%
  is pre-declared no-information.** MU and WDC have **no covering straddle**; stated, not invented.
- **Tilt hit**: IT **N**. **Rips on A**: STX · MU · WDC · SNDK · AMAT.
- **Invalidation**: HY OAS ≥ 3.10% on a close (then it is **S26**, not an IT event).

## S31 — ★ Is the book's Energy epicenter the business or the war premium? · ARMED · → 2026-08-05

Registered **2026-07-27 by the `industry_US` PREMORTEM (Lens 2), before the event.**

**The gap it fills.** **S8** brackets the *commodity*. **Nothing brackets the book's own held
expression.** **XOM carries RS20 vs SPY +13.5 against RS60 vs SPY +0.4 — a 13.1pp gap opened entirely
inside the last 20 sessions**, which is the same exhaustion geometry **M149/M150** flag on TRV and VTR,
sitting on **the only Energy name the book holds** and **the one with 0% refining exposure** (M146).

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | **XOM RS20 vs SPY holds > +10% through 2026-08-05** even with crude ≥5% below its pre-pause range | The integrated leg decouples from the crack ⇒ **the ENRG OW− is pointed at the wrong sub-segment**, and the registry's unheld `core_pick` (PSX) is the right one |
| **B (with us)** | **XOM RS20 vs SPY reverts to ≤ 0 by 2026-08-05** | The last 20 days were war premium; the refining-margin thesis is the only surviving Energy leg |

- **Frozen observable**: **XOM RS20 vs SPY on settled closes, with XOM RS60 vs SPY quoted alongside** —
  a 20-day number alone hides whether the gap closed by RS20 falling or RS60 rising.
- **State at registration**: **+13.5 / +0.4**. Peers for context: PSX **+19.8 / +21.4**, MPC
  **+21.3 / +29.1**, CVX **+12.5 / −0.4**, COP **+12.4 / −7.1**.
- ⚠ **Declared at registration, not discovered afterwards: XOM prints 2026-07-31, inside the window**,
  so the observable is contaminated by an earnings event.
- **Tilt hit**: ENRG **OW−**, and the rank-2 cycle's held exposure. **Rips on A**: XOM · CVX · COP.
- **Invalidation**: a Hormuz reopening statement — then **S8** owns it, not this.

## S32 — ★★ The positioning branch nothing brackets · ARMED · 2026-07-28 COT → 2026-07-31

Registered **2026-07-27 by the `industry_US` PREMORTEM (Lens 2), before the event.**

**The gap it fills.** **M125 is the desk's own headline positioning fact — Nasdaq-100 net-spec at the
5th percentile (crowded SHORT) against S&P 500 at the 84th, a 79-percentile-point spread inside one
asset class — carried for three runs and bracketed nowhere.** Two days before the largest prints of
the window, the book has no branch in which the mega-caps rise **on positioning rather than on
fundamentals**.

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | CFTC **Nasdaq-100 net-spec 1-year percentile rises >15 points from the 5th** AND **QQQ RS5 vs SPY > +2% by 2026-07-31** | The crowded short covers into the prints and IT/COMM rise **without any capex/margin question being answered** ⇒ S13 and S16 score on observables the tape ignored |
| **B (with us)** | the percentile stays **<10th** with QQQ RS5 vs SPY **≤ 0** | Positioning stayed crowded-short; the prints were settled on fundamentals |

- **Frozen observable**: the **CFTC COT Nasdaq-100 net-spec 1-year percentile** (next release covers
  the **2026-07-28** Tuesday close), **with QQQ RS5 vs SPY quoted alongside.**
- **State at registration** (COT, Tue close 2026-07-21): **NDX 5th percentile · S&P 500 84th ·
  Russell 2000 88th · UST 10Y 12th (48,031 shorts ADDED) · WTI 11th · NatGas 11th · Copper 98th.**
- ⚠⚠ **Registered with an explicit constraint. "COT crowded-long/short contrarian" sits in this desk's
  REJECTED signal ledger (D6) and this bracket does NOT re-buy it.** It registers an **observable to be
  scored**, so that if the prints are overwhelmed by a positioning unwind the record shows it was
  foreseeable — the same reason **C6** exists. **It may not be cited as a signal by any stage.**
- ⚠ **No options instrument covers this**, and the three names it would most affect (MSFT ±1.1%,
  META ±1.7%, AMZN ±0.9%) have **straddles that expired 2026-07-27, before their own events (M89, 5th
  replication)** — which is precisely why this bracket is written on positioning rather than on price.
- **Tilt hit**: IT **N**, COMM **N−**. **Rips on A**: META · MSFT · AMZN · NVDA.
- **Invalidation**: HY OAS ≥ 3.10% on a close — then **S26** owns it.

## Brackets considered and DROPPED 2026-07-27, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **EQIX vs DLR RS20 spread (07-30)** | **Duplicative of S25**, which already freezes DLR's RS20 vs SPY against the {PLD, AMT, WELL} median to 2026-08-08 **and already names EQIX's 07-30 print as its second settling point.** A second spread on the same names double-counts one event |
| **V (2026-07-29) standalone** | **S14 / S14-ANNEX / S14-num already own the payments binary**, and the ANNEX pre-registered the {MA, V}-only reading. No incremental information |
| **PSX (2026-08-05) standalone** | Same mechanism as **S8 branch B**, and PSX/VLO/MPC are **one risk unit** (SPY-residual ρ +0.878). No new observable |
| **AMD / ANET (2026-08-04)** | **No implied move and no flow baseline exist for either at this clock — any threshold would be fabricated.** Stated rather than manufactured; revisit when options data covers the event |
| **FTNT standalone** | Same 20-vs-60-day shape as S30's basket (RS60 +73.9 vs RS20 +1.0); **folded into S30 rather than duplicated** |

---

## Scoring-log rows added 2026-07-28 by the `industry_US` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S20** | 2026-07-24 (PREMORTEM) | 2026-07-28 | **FIRED-B** | **2026-07-28 HANDOVER (industry_US)** | ★ **UPS RAISED FY guidance** (revenue **$91.2bn**, adj diluted EPS **~$7.22**) on adj EPS **$1.76 vs $1.66 expected** and revenue **$22.834bn (+7.6% YoY) vs $21.81bn expected** ⇒ **branch A (a cut attributed to fuel) and branch C (a cut on VOLUME) cannot fire.** Branch B — *"fuel is a non-event"* — is the only consistent branch and is positively supported: **five outlets (cnbc · nasdaq/RTTNews · wsj · yahoo_finance · marketwatch) itemised revenue-per-piece, international mix, supply-chain and $1.2bn of network-reconfiguration benefits, and NONE carried a fuel line.** ⚠ **Declared limit**: the frozen text says *"the call"*, and the **08:30 ET transcript is not in the corpus at run clock** — B is scored on the release + five outlet write-ups, not the transcript. **The verdict is unaffected** (the guidance clause alone eliminates A and C); the fuel leg is `[partially verified]` and filed as **D85**. ⚠ **Both halves cited (C2)**: GAAP net income **fell 53% YoY** ($1.283bn → $604m) on the same release. **Meaning**: **W4 / dig D23 closes at 4 of 5 with the 5th name REFUTING the other four** — DAL/UAL/FDX/LUV all quantified fuel at +66% to +84% YoY and two cut guidance on it; the largest US distillate buyer did neither. **That is a dispersion finding (W5), not a closure.** ★ **Consequence for the rail node: branch C was its registered falsifier and it did NOT fire** |
| **S28** | 2026-07-27 (industry_kr DEEP-INDU) | 2026-07-28 09:00 KST | **FIRED-A** | **2026-07-28 HANDOVER (industry_US)** | ★ **Scored by the next desk to run, exactly as the 07-28 KR run pre-declared** (*"next run's #1 scoring job"*). `[PRIMARY — DART 임시주주총회결과, rcpNo 20260728800373]`: **both KKR nominees elected — Masahiko Kato (KKR Infrastructure Japan) 99.4% for / 0.6% against · Abhishek Sharma (KKR Climate & Infrastructure Singapore) 99.5% / 0.5%**, attendance 47.6%. The filing restates the linkage: the election is a **거래종결 정지조건** under the **2026-03-06 주식매매계약 with Eclipse Holdco L.P.** ⇒ **the condition precedent clears; S22 branch A becomes materially more likely. This is NOT itself a closing, and S22 is neither re-frozen nor pre-scored** — its kill remains a second deferral, nothing else. ⚠ **R24 hazard, named at scoring**: a clean FIRED-A here is **not** evidence that R24 (which retracted the *"structural, not thematic"* driver 24 hours earlier) was wrong. R24 withdrew *"it is not a theme"*, not *"the structure is not real"* (**C4**). Both stand |
| **S33** | 2026-07-28 (industry_kr MACRO) | 2026-07-28 close | ★★ **FIRED-A on the frozen observable / branch B on the beta-adjusted reading — and the DISAGREEMENT is the verdict** | **2026-07-28 HANDOVER (industry_US)** | Settled closes `[KIS Open API primary; yfinance agrees to the won — D5 cross-provider check]`: **`069500.KS` 107,730 → 95,675 = −11.190%** · **010950 136,400 → 129,500 = −5.059%** · **096770 116,700 → 112,700 = −3.428%**. **Raw excess: +6.131pp / +7.762pp ⇒ median +6.947pp ≥ +1.5 ⇒ FIRED-A.** Betas **re-measured by the scoring desk rather than inherited (C1, R20's lesson)** — 60 sessions ending 07-27 vs `069500.KS`: **010950 −0.118 · 096770 +0.237**, reproducing the ANNEX's −0.120 / +0.241 to within 0.004. **Beta-adjusted residuals: −6.374pp / −0.771pp ⇒ median −3.573pp ≤ −1.5 ⇒ branch B.** ★ **What it measures**: pure beta predicts a median excess of **+10.51pp** on a −11.19% benchmark day; the realised **+6.95pp is 3.57pp BELOW frozen mechanics** ⇒ **the refiners did not outperform on the crack news, they underperformed their own betas.** ⚠ **S33-ANNEX's own input was wrong in the conservative direction**: it stated KOSPI200 settled **−7.85%**; the settled primary is **−11.55%** (KOSPI −10.84%), so the contamination it warned of is **~47% larger** than it estimated. ⚠ **This does NOT close C4** — the registered information delta was overwhelmed by a −10.8% index event whose named driver (CXMT) is an unrelated axis; **n=1 on a contaminated date (S1)**. **Carry: one vote for the war-premium reading on the adjusted axis, no vote on the raw axis, and the test itself was swamped.** ★ **First KR instance of the staged rule L3-bis, and the second instance overall after M135** — two independent instances in four days is the argument for promoting **L3-bis and D82** out of staging. Escalated to a human, not executed |
| **S32** | 2026-07-27 (industry_US PREMORTEM) | 2026-07-28 COT → 07-31 | — **not scoreable** | 2026-07-28 (industry_US) | **The CFTC release covering today's Tuesday close publishes 2026-07-31.** Today's pull still returns the **2026-07-21** close and reproduces M125 byte-for-byte (**NDX 5th · S&P 84th · R2K 88th · UST10Y 12th with −48,031 added · WTI 11th · NatGas 11th · Copper 98th**). **Not EXPIRED, not pending — not yet published.** ⚠ Scoring it off today's tape would be scoring a price reaction, which this bracket's own registration text forbids. ★ Independent corroboration of branch A's *mechanism* on a different instrument, **recorded but explicitly NOT cited as a signal** (the bracket forbids it): FINRA Reg SHO 07-27 shows a simultaneous short-volume collapse at all three spenders — **META z −3.43 · MSFT −2.56 · AMZN −2.55** |
| **S35** | **2026-07-28 (industry_US PREMORTEM, Lens 1/2)** | 2026-07-29/30 → **2026-08-07** | — | — | ARMED — ★ the **regulated-Utilities** leg, which S24 (an AI-power bracket) does not contain; full bracket below |
| **S36** | **2026-07-28 (industry_US PREMORTEM, Lens 2)** | → **2026-08-05** | — | — | ARMED — ★ **Materials: A-grade price and sweep breadth disagree on one sector on one date**, and nothing in S1–S35 contained it |
| **S37** | **2026-07-28 (industry_US PREMORTEM, Lens 2)** | → **2026-09-30** | — | — | ARMED — ★★★ **the CXMT branch in which a funded entrant is BULLISH for the incumbents.** The highest-information bracket registered this run: it falsifies the framing of the run's own largest new proposition |

⚠ **Bracket-ID allocation**: S35–S37 were checked against every existing row before writing (the D76
collision that forced R19's and S30's renumbering). **The shared-counter proposal for a human stands.**

---

## S35 — ★★ The regulated-Utilities print cluster · ARMED · 2026-07-29/30 → 2026-08-07

Registered **2026-07-28 by the `industry_US` PREMORTEM (Lens 1/2), before the events.**

**The gap it fills.** **S24** brackets the **AI-power four** (VST/CEG/GEV/VRT) on a capex read.
**Nothing in S1–S34 brackets the REGULATED utilities**, whose driver is rate base and allowed ROE —
and **this run demoted the whole sector N− → UW on flow, 24 hours before six of its constituents
print.** ⚠ **All six are absent from `CATALYST_WATCH.json` (D18's 9th consecutive occurrence)**, so
the demote was taken with no calendar awareness of them.

**What it is**: **WEC · ETR print 2026-07-29 · EXC · SO · XEL · AEP print 2026-07-30 · D prints 07-31.**

**Observable (frozen)**: the **median RS20 vs SPY of {WEC, ETR, EXC, SO, XEL, AEP, D}**, settled closes.
**State at registration** (`asof 2026-07-27 settled`): **−5.6 · −3.2 · −1.9 · −2.1 · −3.2 · −5.1 · −0.1
⇒ median −3.2.** Sector context: **🟢 0 of 15 · breadth 0.00 · wflow −0.381 · eqflow −0.380.**

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | median RS20 vs SPY **> 0 by 2026-08-07** | **The UW demote taken 2026-07-28 was wrong, and wrong for a nameable reason**: the sector's flow collapse belonged to the **AI-power** leg and the desk demoted the **regulated** leg with it — a **W5 label collapse** of exactly the shape M26/M174 measured inside Industrials |
| **B (with us)** | median RS20 vs SPY **stays ≤ 0** through 2026-08-07 | The demote holds; the regulated and AI-power legs were one trade after all |

⚠ **No options instrument covers a six-name utility cluster** — stated, not dressed up. The threshold is
deliberately a **sign test on a median** so that no magnitude is fabricated.
⚠ **Invalidation**: **HY OAS ≥ 3.10% on a close** ⇒ **S26** owns it, not this.
★ **Information content (L3)**: **branch A falsifies a verdict this run itself made**; branch B merely
confirms it. **Asymmetric in the useful direction — the bracket can hurt us.**

## S36 — ★★ Materials: the A-grade price and the sweep's breadth disagree · ARMED · → 2026-08-05

Registered **2026-07-28 by the `industry_US` PREMORTEM (Lens 2), before the window closes.**

**The gap it fills.** `SECTOR_ROTATION.md` §2b held **MATR UW** while recording that **XLB beat SPY on
both windows** — **+0.25% vs +0.02% on the day and +2.72% vs −0.40% over five sessions** — and that the
sector's flow is the **second-worst on the board** (**wflow −0.328 / eqflow −0.237 / 🟢 0 of 12 /
breadth 0.00**). **Two of this desk's own axes point opposite ways on one sector on one date, and no
row of S1–S35 contains it.** The 07-25 run had already declared *"if XLB beats SPY again next session
the UW needs re-argument"*; **that session has now happened.**

**Observable (frozen)**: **XLB's 5-day excess return vs SPY on settled closes**, **quoted alongside the
sector's green count from `SECTOR_FLOW_US.json`** — a one-axis read hides which side moved (C2's shape
applied to a divergence).
**State at registration**: **5-day excess +3.12pp · green count 0 of 12 · breadth 0.00 · Copper COT
98th percentile.**
**Frozen threshold**: **by 2026-08-05**, is the 5-day excess still **> 0** while the green count is
still **0**?

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | excess **> 0** **AND** green count still **0** | ⇒ **the UW is being carried against its own tape for a second week**, and the sweep's breadth cannot see what the price is doing. The UW must be **re-argued**, and **rule D6 (A-grade RS outranks a C-grade OBV-built tag) applies against the desk's own verdict** |
| **B (with us)** | excess **≤ 0**, **or** the green count rises above 0 | The divergence resolves itself; the UW stands and the 07-27 move was noise |

⚠ **n ≈ 1 declared at registration (S1)**: a 5-day window containing **one** −2%-crude session is not
five observations.
⚠ **No options instrument covers a sector-ETF-vs-benchmark spread here** — stated.

## S37 — ★★★ The CXMT branch in which a funded entrant is BULLISH for the incumbents · ARMED · → 2026-09-30

Registered **2026-07-28 by the `industry_US` PREMORTEM (Lens 2), before its window.**

**The gap it fills, and it is this run's most important one.** **MACRO P9, EVENT_ALPHA Card 1 and S34
all frame CXMT as a SUPPLY threat to the incumbents.** ⚠ **Nothing anywhere brackets the opposite
reading** — that a state-funded fourth entrant **validates DRAM as a strategic asset class and
RE-RATES the incumbents.** The evidence for that branch sits inside the desk's own body-read: **CXMT
listed at ≈$487bn on ~7.7% share, described in the source as *"roughly half that of Micron and SK
Hynix"*** — i.e. the market assigned it **several times the incumbents' capitalisation per point of
DRAM share.** **A book that brackets only one direction of its own headline story is running the
2026-07-14 one-way-tilt failure the PREMORTEM stage exists to prevent.**

**Observable (frozen)**: **MU's forward P/E**, with **its next-year consensus EPS quoted alongside** —
a multiple alone hides whether the numerator or the denominator moved (**C2** applied to valuation).
**State at registration** `[carried, M6, asof 2026-07-22]`: **forward P/E 6.31x on +1y EPS 153.74.**
⚠ **This is a 6-day-old carried figure and is labelled as such — it is RE-PULLED at scoring, never
assumed. That re-pull is the first act of scoring this bracket.**
**Frozen threshold**: **by 2026-09-30** (the window contains MU's FQ4 print, S4), is MU's forward P/E
**above 8.0x** with next-year EPS **not lower** than **153.74**?

| Branch | Observable | Meaning |
|---|---|---|
| **A (against our framing)** | forward P/E **> 8.0x** with next-year EPS **>= 153.74** | **A re-rate on an intact denominator** ⇒ the market read CXMT as **validation of the asset class**, not as supply risk. **P9's direction is wrong even if its facts are right**, and **L2's peak-margin read on MU weakens rather than strengthens** |
| **B (with our framing)** | forward P/E **<= 8.0x**, **or** next-year EPS falls below 153.74 | The supply reading holds — either the multiple stays at cycle-trough levels or the denominator starts coming down. **P9 / S34 stand** |
| **C** | EPS **rises** while the multiple **falls** | ⇒ **the market is de-rating a RISING denominator — the sharpest form of the supply thesis, stronger than B.** Recorded separately so it can never be scored as B |

⚠ **The 8.0x threshold is HAND-SET and declared as such.** **No options instrument prices a two-month
forward multiple**; 8.0x is **1.27x the carried 6.31x**, roughly a one-notch re-rate. It is **not** a
measurement and is written down rather than dressed up.
⚠ **Do NOT score this on price.** A multiple is a ratio; **both legs are re-pulled at scoring.**
⚠ **Invalidation**: an Entity List designation **actually implemented** — then **P9's own registered
anti-signal** owns the outcome and this bracket voids.
★ **Information content (L3)**: **branch A falsifies the framing of this run's single largest new
proposition.** The highest-information bracket registered today.

---

## Brackets considered and DROPPED 2026-07-28, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **V (2026-07-29) standalone** | **S14 / S14-ANNEX / S14-num already own the payments binary**, and the ANNEX pre-registered the {MA, V}-only reading. A V-specific bracket double-counts one event. ⚠ **Logged as an under-computed leg in BLINDSPOT_PREMORTEM Lens 1 rather than dropped silently** — V prints a day BEFORE MA and is absent from `CATALYST_WATCH` |
| **GD (2026-07-29) standalone** | **Neither branch changes a conclusion.** INDU is held **OW− on the rail/freight node's flow** (4 of the LIVE shortlist's top 5), **not on defense**, and W4 on defense is already 3 of 5 closed from primary sources. A backlog print moves a `[measured]` gap from 3/5 to 4/5 and moves **no tilt** |
| **FTNT (2026-07-30) standalone** | **Folded into the Lens-3 momentum re-tag** — FTNT is the one security name that flipped to **EXHAUSTED** today (**RS20 −0.7 vs SPY with OBV 분산** against RS60 +73.1). A separate bracket on a name already carrying a reject-ledger recheck adds nothing |
| **A second crack bracket** | **S8 and MACRO P4 already own it on one axis** (a settled 3-2-1 crack below 60), and the distance **widened from 4.30 to 8.12 points** on the settled 07-27 close. A second threshold on the same series is duplication |
| **The 2026-07-28 KOSPI memory rout** | **S34 forbids scoring on a price reaction at registration**, and a KR index session is not this desk's observable (**W1**). Recorded as evidence the CXMT thread is being traded, never as a bracket |

---

## Scoring-log rows added 2026-07-29 by the `industry_US` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| — | — | — | ★ **ZERO past-dated rows were unscored this run** | 2026-07-29 HANDOVER (industry_US) | Every row whose event predates today was settled by the two 07-28 runs and re-verified against the log: **S1 FIRED-A · S6 FIRED-A · S7 FIRED-A (both legs) · S10 FIRED-B · S12 FIRED-B (observable) / AMBIGUOUS (decision axis) · S8 FIRED-B · S20 FIRED-B · S28 FIRED-A · S33 FIRED-A raw / branch-B beta-adjusted.** `EXPIRED` = **0**; silent skips = **0**. ⚠ **The twelve rows dated 2026-07-29 — S2 · S9 · S11 · S13 · S16 · S17 · S18 · S19 · S23 · S24 · S30 · S35 — had NOT printed at this run's 09:1x ET clock** (FOMC 14:00 ET; META/MSFT/STX/V after the close). **Filling any of them from a pre-open tape is the observable-fabrication L3 `scenario_score` forbids**, so this run did not attempt it. ★ **S11 and S18 are KR-domestic regulatory events that occurred during today's KR session and are NOT scoreable on this desk's admissible feed** — `fts search "KT" fine --days 2 --scope foreign` returned 1 irrelevant hit and `Korea governance --days 3 --scope foreign` returned 108 hits containing neither the FSC package nor the KT sanction. **Explicitly assigned to the `industry_kr` run of 2026-07-30 and named here so they cannot be carried silently a second time.** **S32 is not scoreable** (its CFTC release publishes 07-31), not EXPIRED |
| **S40** | **2026-07-29 (industry_US PREMORTEM, Lens 2)** | → **2026-09-30** | — | — | ARMED — ★★★ **a capex GUIDE is not a capex MEASUREMENT when a gigawatt arrives as a lease.** Impairs the observable **S13 · S16 · S24** all share. Full bracket below |
| **S41** | **2026-07-29 (industry_US PREMORTEM, Lens 2)** | → **2026-08-12** | — | — | ARMED — ★★ **the AI-issuer credit channel S26's own invalidation clause explicitly excluded.** Written on an index series this repo can actually pull, because it has no CDS feed (new dig D97) |
| **S42** | **2026-07-29 (industry_US PREMORTEM, Lens 2)** | → **2026-08-12** | — | — | ARMED — ★★ **brackets THIS run's own new verdict** (Industrials OW− → OW) against **M174**, which measured the same node at 0🟢 / 16🔴 five days earlier |

⚠ **Bracket-ID allocation**: **S38 and S39 were taken this morning by the concurrently-running
`industry_kr` desk**; S40–S42 were checked against every existing row before writing (the **D76**
collision class that forced R19's and S30's renumbering). **The shared-counter proposal for a human
stands, now for a fourth run.**

## S40 — ★★★ A capex GUIDE is not a capex MEASUREMENT when a gigawatt arrives as a lease · ARMED · → 2026-09-30

Registered **2026-07-29 by the `industry_US` PREMORTEM (Lens 2), before META's print.**

**The gap it fills.** **S13, S16 and S24 all score on "the capex guide" at MSFT and META.** On
2026-07-28 Meta closed a **$14bn, one-gigawatt El Paso data-centre campus** in which **BlackRock-managed
funds take 80% and Meta 20%**, **part of BlackRock's contribution coming from a $12.5bn debt
financing**; Meta contributed land and construction-in-progress about **$2.3bn**, BlackRock about
**$4.9bn cash**, **Meta collected a one-time distribution of about $1bn**, and **Meta leases the entire
campus back — four-year initial term, four extensions, up to 20 years, sole occupant — while providing
residual-value guarantees with an aggregate threshold of about $13bn declining over 16 years.**
Capacity online 2028.
`[news — GuruFocus via yahoo_finance plus the PR Newswire release, 2026-07-28, body-read in full]`
⇒ **A gigawatt of AI capacity that arrives as a lease does not appear in the line item three registered
brackets score on.** Nothing in S1–S39 contains this.

| Branch | Observable | Meaning |
|---|---|---|
| **A (against our framing)** | META's FY2026 capex guide is **held or cut** at the 07-29 print **AND** at least one further off-balance-sheet AI-infrastructure structure (JV, sale-leaseback, or residual-value guarantee) of **at least $5bn** is disclosed by any of {META, MSFT, GOOGL, AMZN} by **2026-09-30** | **The capex observable is measuring a financing choice.** S13 / S16 / S24's shared line item is structurally impaired, and every future capex bracket must read the lease-obligation note alongside the guide |
| **B (with our framing)** | META's FY2026 capex guide is **raised** | The lease was **incremental, not substitutive** — the registered observable still measures spending, and S13 / S16 / S24 stand as written |
| **C** | Guide held or cut with **no** further $5bn-plus structure disclosed by 2026-09-30 | `AMBIGUOUS` — recorded as such and **re-registered on disclosed operating-lease-obligation growth** rather than on a deal count. **The threshold is not widened after the fact** |

- **Frozen observable**: META's FY2026 capex guidance line, **and** the count of disclosed
  off-balance-sheet AI-infrastructure structures of at least $5bn across {META, MSFT, GOOGL, AMZN},
  **2026-07-29 → 2026-09-30.**
- ⚠ **No options instrument prices a financing structure.** The threshold is a **count**, **hand-set
  and declared as such** rather than dressed as a measurement.
- ⚠⚠ **This does NOT re-freeze S13, S16 or S24.** They are scored exactly as written; **if S40-A fires,
  the disagreement between them is the finding** — the S14-ANNEX / S33-ANNEX precedent.
- ⚠ **Score the disclosure, not the price reaction.** META's implied move is **±8.1% (expiry
  2026-07-31, D2 — it covers the event)**; a move inside it is no information about this bracket either way.
- ★ **Information content (L3): branch A impairs an observable three registered brackets share.**
  The highest-information bracket registered this run.

## S41 — ★★ The AI-issuer credit channel S26 explicitly excluded · **SETTLED FIRED-B** (scored 2026-09-07 by the `industry_US` run from already-published data — `D472` header hygiene) · → 2026-08-12

Registered **2026-07-29 by the `industry_US` PREMORTEM (Lens 2).**

**The gap it fills.** **S26's frozen observable is HY OAS — an index — and its own invalidation clause
reads *"widening driven by a single issuer or sector default rather than index-level (idiosyncratic,
re-register)."* Today's feed describes exactly that excluded case.**
`[news — Reuters / Amanda Cooper via yahoo_finance 2026-07-29, citing S&P Global Market Intelligence,
DTCC and ISDA; body-read in full]`: **Oracle CDS about 200bp · NVIDIA about 78bp and *"risen sharply
this week"* · Meta about 93bp**, against an **investment-grade CDS index at about 53bp**; tech-sector
CDS trading reached **about $650m average daily notional in Q2, +20% QoQ and about +600% YoY**, with
**Meta, Nvidia and Alphabet as new entrants**; the stated cause is *"growing concern among investors
about when the billions being poured into artificial intelligence will generate returns"*, with
**Nvidia tapping bond markets for the first time.** **HY OAS sits at 2.81% and would not move on any of it.**

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | **IG OAS at or above 0.90% on a close by 2026-08-12** | The single-name AI widening **transmitted**. The desk's index-level credit axis was **late, not right**, and **S26-B becomes live through the channel S26 excluded** |
| **B (with us)** | **IG OAS stays below 0.90% AND HY OAS stays below 3.10% through 2026-08-12** | The widening stayed idiosyncratic; **S26-A held**, and the index axis was the correct resolution |

- **Frozen observable**: **IG OAS (FRED `BAMLC0A0CM`) on a close, with HY OAS quoted alongside**
  (S9's two-series rule applied to credit).
  **State at registration `[FRED]`: IG OAS 0.81% (asof 2026-07-27) · HY OAS 2.81% (07-27) ·
  NFCI −0.554 (07-24).** The 120-day IG range is **[0.73, 0.94]** ⇒ **the 0.90 threshold sits inside
  the observed range, at roughly its 90th percentile, and is therefore reachable without a regime break.**
- ⚠ **This repo has no CDS feed (new dig D97)** — which is exactly why the observable is an index
  series this desk can pull rather than a quote it cannot verify. **No CDS number is used as a threshold.**
- ⚠ **Counter-evidence carried at registration (C2)**, from the same body: **CDS trading is thin —
  *"average daily trades, even for large companies, can sometimes be in the single digits, meaning
  small transactions can have an outsized impact on prices."*** ⇒ a CDS level is a low-liquidity quote,
  not a clearing consensus, and it is `[news]`-grade, single-wire.
- **Tilt hit**: the book's **held AI-compute epicenter (NVDA, AVGO)** and — through the shared beta
  M147 measured (JPM 0.932 · DLR 0.769 · PLD 0.766 · PSX 0.747) — **all three OW carriers**.
- **Invalidation**: a single-issuer **default event** ⇒ idiosyncratic by construction, re-register.

## S42 — ★★ This run's own new verdict, bracketed against itself · ARMED · → 2026-08-12

Registered **2026-07-29 by the `industry_US` PREMORTEM (Lens 2), against this run's own ROTATION.**

**The gap it fills.** **ROTATION promoted Industrials OW− → OW this run**, carried by **breadth 0.180
(the board's highest) and nine 🟢 of the board's seventeen — four of which are CAPITAL GOODS:
WAB · PCAR · MMM · ITW**, and three of those four are `new_green`. **That is the node M174 measured
five days earlier at flow −0.193 with 0🟢 / 16🔴.** **A verdict this run created, on a node its own
prior measurement contradicts, and nothing in S1–S41 brackets it.**

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | **median RS20 vs SPY of {WAB, PCAR, MMM, ITW} turns at or below 0 by 2026-08-12** | The ignition was a **date-clustered single-session event** and the OW promote was taken on noise. M174's split did not invert |
| **B (with us)** | that median stays **above 0** through 2026-08-12 **AND at least 2 of the 4 still carry a 🟢 tag** | M174's split genuinely inverted at the capital-goods end, and the promote was early rather than wrong |

- **Frozen observable**: that median, **settled closes**, benchmark **SPY** (C1).
  **State at registration `[SECTOR_FLOW_US.json, asof 2026-07-28 settled]`: WAB +14.0 · PCAR +15.6 ·
  MMM +12.4 · ITW +10.4 ⇒ median +13.2.** Flow scores +1.00 / +0.89 / +0.78 / +0.78 with
  `vol_surge` 1.84 / 1.40 / 1.21 / 1.21.
- ★ **Control, registered INSIDE this bracket rather than as a second one**: **CAT — same node,
  🔴분산 −0.76, RS20 −18.6 / RS60 −8.6.** **If the four rise while CAT stays negative it is a
  sub-node event; if CAT turns with them it is Industrials beta (W5).**
- ⚠⚠ **n is about 1, declared at registration (S1)**: four names greening on **one settled session** is
  one observation, not four. ⚠ And **`new_green` here diffs against a 2026-07-27 history key because no
  07-28 key existed before this run wrote one** (SWEEP §0) — so the "day-over-day" ignition is really a
  **one-session** diff whose base is two calendar days back.
- ⚠ **No options instrument covers a four-name industrial basket** — the threshold is a **sign test on
  a median**, chosen so no magnitude is fabricated.
- ⚠ **L3-bis check performed at registration**: RS20 is a rolling window, so the base date advances.
  The four carry 20-day gains of 10–16pp that **roll off inside the window**, so a flat tape would pull
  the median toward zero rather than leave it at +13.2 ⇒ **the bracket cannot pass on frozen prices**,
  which is the L3-bis test.
- **Invalidation**: **HY OAS at or above 3.10% on a close** ⇒ **S26 / S41** own the outcome, not this.
- ★ **Information content (L3): branch A falsifies a verdict this run itself made.** Asymmetric in the
  useful direction — the bracket can hurt us.

## Brackets considered and DROPPED 2026-07-29, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **V (2026-07-29) standalone** | **S14-ANNEX already pre-registered the {MA, V}-only reading**; a V-specific bracket double-counts one event. ⚠ **Logged rather than dropped silently**: V's option **P/C OI is 5.90** with skew +12.5 and implied **±3.5% (D2)** on a name carrying RS20 +7.3 / RS60 +8.0 — **the heaviest put positioning on the board, accounted for by no bracket, thesis or dig** |
| **July NFP (2026-08-07)** | ★ **Neither branch changes a conclusion inside any live window — on date arithmetic, not on judgement.** **S19's and S23's DGS2 / T10Y2Y windows both close 2026-08-05, before NFP prints.** A labor number landing after every registered rate observable has settled cannot move them |
| **AMD · ANET (2026-08-04)** | Re-measured rather than re-quoted: **AMD 🔴분산 −0.66 (RS20 −15.7 / RS60 +25.2) · ANET 🟡 +0.06 (+3.4 / −4.8)**. Neither carries a thesis, a tilt link or a covering straddle ⇒ **any threshold would still be fabricated.** Same reason as 2026-07-27 |
| **CEG · VST · LNG (2026-08-06/07)** | **CEG and VST sit inside S24's frozen basket**; **LNG is not in `us_top300`** (instrument gap, the tanker class). A separate bracket double-counts S24 |
| **A second crack bracket** | **S8 and MACRO P4 own it on one axis** (a settled 3-2-1 crack below 60) and the buffer **widened again, 8.12 → 12.22 points**. A second threshold on the same series is duplication |

---

## Scoring-log rows added 2026-07-30 by the `industry_US` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S15** | 2026-07-23 (PREMORTEM Lens 2) | **2026-07-30 08:30 ET** | ★ **FIRED-B** | **2026-07-30 HANDOVER (industry_US)** | **Observed: core PCE +0.1% MoM** (after a revised **+0.3%** in May); **core 3.3% YoY** from 3.4%, consensus 3.3%. Headline **−0.1% MoM**, **3.7% YoY** from 4.1%. **Threshold was frozen at A: core MoM > +0.3% · B: ≤ +0.3%** ⇒ **B, at one third of the line.** `[BEA release table via fxstreet 2026-07-30 12:30 GMT]` ✅ **C2 satisfied — both halves quoted like-for-like.** **Effect on the standing view: P1's "reaction-function, not inflation" framing SURVIVED its own registered frontal test.** ⚠ Scored on the observable, not the reaction — the dollar did not move on the release |
| **S2** | 2026-07-22 | 2026-07-29 (the five-event cluster) | **FIRED-B** | **2026-07-30 HANDOVER (industry_US)** | Branch A required **both** MSFT and META to raise capex. **MSFT HELD** — *"kept its capex forecast unchanged… one of the first data center giants to hold the line"*, **$190bn calendar-year plan restated ($175bn after an accounting change)**, stock +8~9% `[businessinsider 07-29, body-read]`. **META narrowed 125–145 → 130–145bn, raising the midpoint by $2.5bn** `[Reuters via yahoo_finance 07-29, body-read]`. ⇒ **mixed ⇒ B.** Branch C required a **cut** at either (none) **or real 10y > 2.55%** (**DFII10 2.41%, FRED asof 07-28**) ⇒ **C did not fire.** ⚠ Branch B's own text says *"wait for AMZN + AAPL"*, which print 07-30 AMC ⇒ **B is correct AND deliberately low-information**, exactly as registered. ⚠ **The ADR leg was already superseded by S17 (R13)** |
| **S19 · S23 · S9** | 2026-07-24 / 07-25 / 07-22 | 2026-07-29 (FOMC) | — **decision leg recorded, numeric legs STILL RUNNING to 2026-08-05** | (recorded 2026-07-30) | ★★ **FOMC HELD, with THREE dissents FOR A HIKE** — *"three members of the FOMC opposing the decision… one of the strongest early challenges faced by a Fed chair in recent decades"* `[Reuters via economictimes 07-30]`; primary `[federalreserve]` statement 07-29; corroborated by *"Rate Hold Masks A More Hawkish Fed"* [seekingalpha] and *"Dollar Falls as FOMC Keeps Interest Rates Unchanged"* [nasdaq]. ⇒ **S19 branch H's FIRST clause ("target range raised") did NOT fire.** ⚠⚠ **The numeric legs cannot be advanced: FRED's daily curve is stale at 2026-07-28** (DGS2 4.26 · DGS10 4.61 · DFII10 2.41 · T10YIE **2.26 asof 07-29**) — **the entire post-FOMC move is unpublished and NO proxy was substituted (D5).** ★ **Correction filed against the prior run on the same series (MACRO §G-1): derived 2s10s went +0.34 → +0.36 → +0.34 → +0.35, i.e. the last settled move was a 1bp STEEPENING and S23's ≤+0.20 line moved AWAY, not closer** |
| **S13 · S16 · S24 · S40** | 2026-07-23 / 07-23 / 07-25 / 07-29 | 2026-07-29 prints | — **categorical leg recorded, windows open to 08-12 / 09-30** | (recorded 2026-07-30) | **MSFT capex HELD · META narrowed its range upward (midpoint +$2.5bn).** ⚠⚠ **NEW REGISTRATION DEFECT, logged: S13's branches read "capex raised" (A/B) or "capex cut at either" (C) and contain NO branch for "one holds while the other raises."** The grid assumed the two spenders move together — **the D35 family (a grid that cannot receive the outcome).** **S13 is NOT re-frozen**; it will be scored on its two remaining legs at 08-12. ★ **S40's own observable came back AMBIGUOUS on its first print** — a range *narrowed upward* is neither "held or cut" (A) nor cleanly "raised" (B); **recorded as ambiguous, threshold NOT widened.** Its second leg has a live candidate: the Reuters body names a **Blue Owl Capital arrangement for the Louisiana project** alongside the El Paso structure, and `[bloomberg 07-24, title-only]` carries *"BlackRock Kicks Off $12.3 Billion Bond Sale for Meta Data Center"* — **evidence, not a disclosure read; not scored** |
| **S30** | 2026-07-27 | → 2026-08-05 | — tracking **branch B (with us)** | (measured 2026-07-30) | **07-29 was a memory rout: MU −9.94% · KLAC −10.80% · AMAT −8.40% · SNDK −7.32% · LRCX −6.40% against SPY −1.54%.** Frozen observable **median RS20 vs SPY of {STX, MU, WDC} = −25.34** (registration −23.7, prior −28.33) ⇒ **still deep in branch B.** ★ **State change: THREE suppliers have now lost their 60-day cushion (SNDK −15.90 · LRCX −3.12 · KLAC −2.77 RS60 vs SPY)**, where the prior run could name only SNDK. ⚠ **STX beat and rose +2.29% — INSIDE its frozen ±14.6% no-information band, which is NOT re-frozen** despite a newer ±13.4% quote |
| **S31** | 2026-07-27 | → 2026-08-05 | — tracking **branch A (AGAINST us)** | (measured 2026-07-30) | **XOM RS20 vs SPY +16.97 with RS60 +1.83** (registration +13.5 / +0.4) ⇒ **branch A's ">+10% through 08-05" is being met and the gap WIDENED to 15.1pp.** ★ **Quantified for the first time: XOM's days-21-60 excess is −15.14, i.e. 927% of its 60-day excess was earned in the last 20 sessions** — the R9/AXON geometry on the book's only Energy integrated holding. ⚠ **XOM prints 2026-07-31, inside this window, declared at registration** |
| **S35** | 2026-07-28 | → 2026-08-07 | — tracking **branch A (AGAINST us)** | (measured 2026-07-30) | ★★ **The regulated-seven median RS20 vs SPY CROSSED ABOVE ZERO to +0.39** (WEC −2.38 · ETR −3.84 · EXC +3.20 · SO +2.67 · XEL +0.39 · AEP −3.10 · D +5.63), from **−1.99** and a **registration −3.2** ⇒ **the branch that says the 07-28 UW demote was WRONG is now live on settled data.** ✅ **Cross-provider check (D5): the same median computed from `SECTOR_FLOW_US.json` and from an independent yfinance pull agree to 0.01pp** ⇒ not an artifact. **Not scored — window runs to 08-07** |
| **S24** | 2026-07-25 | → 2026-08-12 | — tracking **branch A (with us)** | (measured 2026-07-30) | Frozen median RS20 vs SPY of {VST, CEG, GEV, VRT} **DEEPENED to −14.35** (VST −7.65 · CEG +6.18 · GEV −21.05 · **VRT −31.07 after a −17.26% single session**), from −10.31 ⇒ branch A strengthening. ★ **Order-flow tell: VRT's FINRA short-vol z is −2.25 and GEV's −2.21 — shorts LEFT while the prices collapsed ⇒ long liquidation, not a short attack** |
| **S42** | 2026-07-29 | → 2026-08-12 | — tracking **branch B (with us)** | (measured 2026-07-30) | {WAB +10.54 · PCAR +13.76 · MMM +12.22 · ITW +10.44} ⇒ **median +11.38** (registration +13.2), still above 0. ★ **The in-bracket control DIVERGED FURTHER: CAT RS20 vs SPY −24.04, from −18.6** ⇒ the reading is **sub-node, not Industrials beta (W5)** |
| **S25** | 2026-07-25 | → 2026-08-08 | — tracking **branch B**, 3rd settled session | (measured 2026-07-30) | **DLR RS20 vs SPY +7.11 < the {PLD +9.70, AMT +11.91, WELL +8.53} median +9.70, median positive.** ★ **AMT rose +4.52% on a −1.54% SPY session — the largest positive residual in the sector, and AMT is the name R10/M131 moved OUT of "digital infrastructure" into duration.** ⚠ **EQIX printed 2026-07-30 (the registered second settling point) — not yet read at this run clock** |
| **S36** | 2026-07-28 | → 2026-08-05 | — ⚠ **its confirming leg is DISQUALIFIED** | (measured 2026-07-30) | Leg 1: **XLB's 5-day excess vs SPY is +4.21pp and its 20-day +4.11pp — positive on both windows a 3rd consecutive settled session.** Leg 2 ("green count still 0"): **0 greens, but MEASURED to be a `vol_surge` artifact — 5 of 12 Materials names pass the `OBV-accumulation ∧ RS20>0` pre-condition and ALL 5 are blocked by `vol_surge` alone, the sector's highest surge being 1.14 against a 1.20 gate.** ⇒ ★ **M238's pre-registered warning fired: branch A's second leg can settle on the gate rather than on Materials, so the bracket can no longer CONFIRM the UW — only falsify it.** ROTATION moved Materials **UW → N** on that basis |
| **S32** | 2026-07-27 | 2026-07-28 COT → **2026-07-31** | — **not scoreable, not EXPIRED** | (checked 2026-07-30) | The CFTC release covering the 07-28 Tuesday close **publishes 07-31**. ⚠⚠ **Measured this run: today's `us_flow --cot` output is BYTE-IDENTICAL to M125's 07-21 read on all eight instruments** (NDX 5th · S&P 84th · R2K 88th · UST10Y 12th with −48,031 · WTI 11th · NatGas 11th · Copper 98th) ⇒ **the desk's only positioning axis has been 9 calendar days old since 07-24, across an FOMC and four mega-cap prints.** That is correct feed behaviour, **but the tool prints no `asof`, so a stale snapshot is indistinguishable from a fresh one — new dig D104** |
| **S46 · S47 · S48 · S49** | **2026-07-30 (industry_US PREMORTEM)** | 08-06 / 08-07 / 08-13 / 09-30 | — | — | ARMED — ★ **S46** brackets a name **this run's own HANDOVER revived hours before a D-0 binary its calendar did not carry** · **S47** is the Utilities **SPREAD**, the object neither S35 nor S24 contains · **S48** is the first bracket this desk has ever had on the **optical/interconnect** layer · **S49** is **S8's granularity-invariant successor**, written on a *change* because R30/D95 withdrew S8's absolute levels. Full brackets below |

## S46 — ★★ AAPL: a ledger revival, hours before a binary the calendar did not carry · **SETTLED FIRED-A (the AGAINST-US branch)** (scored 2026-09-07 by the `industry_US` run from already-published data — `D472` header hygiene) · → 2026-08-13

Registered **2026-07-30 by the `industry_US` PREMORTEM (Lens 1/2), before the 07-30 AMC print.**

**The gap it fills.** This run's own HANDOVER **`resolve --outcome revived`** on AAPL at 09:0x ET, on
flow (**🟢, RS20 +19.2 / RS60 +19.5 vs SPY, OBV accumulation, news velocity 1.78×**). **`catalyst_calendar
--days 10` carries no AAPL row (D18's 10th occurrence), so the desk revived a name into a same-night
binary without the calendar knowing.** Nothing in S1–S45 contains AAPL.

⚠ **And Lens 3 qualifies the revival's own evidence**: AAPL's **days 21–60 excess vs SPY is +0.16**,
i.e. **~99% of its 60-day excess is a last-20 event** — the R9/AXON concentration geometry.

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | AAPL's FQ4 report/guide shows gross margin **flat or down** **AND** the **AAPL−QCOM RS20 vs SPY spread narrows below +15pp by 2026-08-13** | **The ledger revival was flow-chasing into a binary**, and the zero-base reading was right. The `L.vehicle없음` rejection should not have been lifted on one flow pull |
| **B (with us)** | gross margin guided **up** **AND** the spread **stays above +25pp** | The revival was on the A-grade axis; QCOM's "Apple-related weakness" is a **transfer between two names**, not a sector shrinkage (**W5**) |
| **C** | anything else | `AMBIGUOUS`, recorded as such. **The threshold is not widened after the fact** |

- **Frozen observable**: (i) the **gross-margin guide direction** (categorical); (ii) **AAPL RS20 vs SPY
  minus QCOM RS20 vs SPY**, settled closes. **State at registration: +19.2 − (−13.4) = +32.6pp.**
- ★ **Reaction test, registered SEPARATELY and NOT inside a branch condition (the D28 fix)**: implied
  **±3.3%, expiry 2026-07-31, D1 — it COVERS the event.** **Any same-day move inside ±3.3% is
  pre-declared NO-INFORMATION.**
- **Information content (L3)**: **branch A falsifies a decision this run made three stages earlier.**
- **Invalidation**: HY OAS ≥ 3.10% on a close ⇒ S26 / S41 own it.

## S47 — ★★★ The Utilities SPREAD: the object neither S35 nor S24 contains · ARMED · → 2026-08-07

Registered **2026-07-30 by the `industry_US` PREMORTEM (Lens 1), against this run's own ROTATION.**

**The gap it fills.** **S35** brackets the regulated seven; **S24** brackets the AI-power four.
**Nothing brackets the DIFFERENCE** — and this run measured the two legs moving in **opposite
directions inside one GICS label**, which is exactly why **ROTATION declined to demote Utilities** and
handed it here. A label carrying a 14.7pp internal spread is **W5's own trigger**.

| Branch | Observable | Meaning |
|---|---|---|
| **A (against the desk's own label)** | the spread **widens beyond +20.0pp by 2026-08-07** | **One GICS label is being used to underweight two legs moving apart.** The desk has already measured this shape twice — **R7** (duration REITs vs digital infrastructure) and **M26/M174** (primes vs capital goods). **Utilities becomes the third instance and the only one still carried whole** |
| **B (with the label)** | the spread **narrows to +7.0pp or less by 2026-08-07** | The legs re-converge; one sector verdict is defensible and the N− stands on its own terms |
| **C** | +7.0 to +20.0pp | **No conclusion changes.** Recorded and not re-argued |

- **Frozen observable**: **(median RS20 vs SPY of {WEC, ETR, EXC, SO, XEL, AEP, D}) MINUS (median RS20
  vs SPY of {VST, CEG, GEV, VRT})**, settled closes, benchmark **SPY** inline.
  **State at registration: +0.39 − (−14.35) = +14.74pp.** (Same construction on 07-28: **+8.32pp**.)
- ⚠ **D93 compliance — the estimator's own error, stated AT registration.** This is a **difference of
  two medians of raw RS20**, not a beta-adjusted residual, so it carries **no regression error** — but
  it does carry a **sampling** one: **n = 1 settled session since the regulated median crossed zero
  (S1)**, and the AI-power leg is dominated by **one name (VRT, −17.26% on 07-29)**. **The +7 / +20
  bands are hand-set and are declared hand-set.**
- ⚠ **No options instrument covers a two-basket spread** — stated, not manufactured.
- **Information content (L3)**: **branch A falsifies a label this desk has carried whole for its entire
  life.** Branch B merely confirms it. ⚠ **S35 and S24 are NOT re-frozen** — if this bracket and those
  two disagree, **the disagreement is the finding** (the S14-ANNEX / S33-ANNEX precedent).
- **Invalidation**: HY OAS ≥ 3.10% on a close.

## S48 — ★★ The optical / interconnect layer, which no bracket has ever covered · ARMED · → 2026-09-30

Registered **2026-07-30 by the `industry_US` PREMORTEM (Lens 1), from EVENT_ALPHA Card 6.**

**The gap it fills.** **S34 and S37 bracket the funded-entrant mechanism in DRAM. A second funded
entrant listed in the same window, one layer over.** `[cnbc 2026-07-30, full body]`: **Zhongji
Innolight raised HK$53.4bn ≈ $6.8bn**, **priced at HK$980 BELOW its HK$1,010 maximum**, **fell 5% on
debut**, is the **world's largest optical-interconnect provider at 21.2% global share (2025, CIC via
prospectus)**, drew **16.8× retail / 9.7× international**, and earmarked proceeds for **R&D, overseas
capacity, supply chain and acquisitions**. It is **Asia's #2 listing of the year behind CXMT's $8.6bn**.
**Nothing in S1–S47 contains this layer.**

| Branch | Observable | Meaning |
|---|---|---|
| **A (with the entrant-threat reading)** | median RS20 vs SPY of **{CIEN, ANET, AVGO, MRVL}** stays **≤ −10.0** through **2026-09-30** | The entrant is being priced as **share transfer**, and **S37's "a funded entrant is BULLISH for the incumbents" branch does NOT generalise from DRAM to optical** |
| **B (against it)** | that median turns **≥ 0** by **2026-09-30** | It is **capital formation, not share transfer**; S37's reading generalises across layers and **EVENT_ALPHA Card 6 is falsified** |
| **C** | −10.0 to 0 | `AMBIGUOUS` |

- **Frozen observable**: that median, settled closes, benchmark **SPY**.
  **State at registration: CIEN −30.3 · ANET −4.7 · AVGO +0.4 · MRVL −42.8 ⇒ median −17.5.**
- ⚠ **ANET's straddle is ±3.8% expiring 2026-07-31, BEFORE its 2026-08-04 print ⇒ NOT event-priced
  (M89, 6th replication).** No magnitude threshold is taken from it; the test is a **level test on a
  median**, chosen so no magnitude is fabricated.
- ⚠ **n ≈ 1 declared at registration (S1)**: three of the four fell on the same 07-29 session.
- **Information content (L3)**: **branch B falsifies this run's own EVENT_ALPHA Card 6.**
- **Invalidation**: an acquisition of any of the four ⇒ idiosyncratic by construction, re-register.

## S49 — ★★★ S8's successor: a crack observable that survives its own data · ARMED · → 2026-08-06

Registered **2026-07-30 by the `industry_US` PREMORTEM (Lens 2), replacing an unscoreable bracket.**

**Why it exists.** **R30 / D95 withdrew S8's scoreability**: yfinance **daily vs 1-hour bars differ by
5.80 crack points** on the product legs (07-27: crack321 **68.117 vs 62.319**), so **S8's absolute
60 / 84 lines are decided by which bar you pull.** **A level cannot be the observable on this data.**
**A CHANGE can** — a constant granularity offset cancels in a difference computed on one bar type.

| Branch | Observable | Meaning |
|---|---|---|
| **A (with the margin thesis)** | the **5-session change in the settled distillate crack** stays **> 0** through **2026-08-06** | The distillate bottleneck is still tightening, and **P4's mechanism survives the Russian diesel-ban expiry on 07-31** |
| **B (against us)** | that change turns **≤ −5.0 points** by **2026-08-06** | **The bottleneck is releasing** — **S8 branch A's economics arriving WITHOUT a Hormuz statement.** ⚠⚠ **Per the correlated-tilt check, this hits ENRG OW− and INDU OW− on the same tick** (M91: ~8 of UNP's 12 revenue growth points are fuel surcharge) |
| **C** | −5.0 to 0 | No conclusion changes |

- **Frozen observable**: the **5-session change in the distillate crack (HO×42 − WTI)** on
  **yfinance DAILY settled bars ONLY, one named source**, never mixed with intraday.
  **State at registration: 99.084 (07-29) − 90.077 (07-27, five sessions back) = +9.007 points.**
  The series for the record: **87.420 · 90.157 · 86.275 · 90.077 · 95.078 · 99.084.**
- ⚠ **Residual risk stated rather than hidden**: the granularity offset is **assumed constant, not
  proven.** If it drifts, a difference does not fully cancel it. **This is a better observable than
  S8's, not a clean one (C4).**
- ⚠ **D86 / M202 / M236 reproduce a FOURTH time in this same series**: CL volume for **2026-07-28 and
  2026-07-29 is byte-identical (368,026)** ⇒ *"check the volume to see whether the bar settled"* is
  unusable on this stretch.
- **Dated catalysts**: **Russian diesel-export-ban expiry 2026-07-31** · **MPC 08-04** · **PSX 08-05**.
- **Implied moves (for the names, not the observable)**: **MPC ±9.4%, expiry 2026-08-21, D22 — COVERS
  its print, usable.** **PSX ±2.7%, expiry 2026-07-31 — expires BEFORE its 08-05 print, NOT
  event-priced.**
- **Information content (L3)**: **branch B breaks two tilts at once**; branch A confirms one.
- **Invalidation**: a Hormuz reopening statement ⇒ **S8** owns that as a narrative event, not this.

## Brackets considered and DROPPED 2026-07-30, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **AMZN (2026-07-30 AMC)** | **Not held, no thesis, no tilt links to it** (🟡, RS20 −2.6 / RS60 −17.0 vs SPY). **Neither branch changes a conclusion.** ⚠ **Logged rather than dropped silently**: its straddle **±6.9% (expiry 07-31, D1) now COVERS its event**, which **supersedes M212 on the third of its three names** — M212 had AMZN as the one that still expired early |
| **July NFP (2026-08-07)** | **Date arithmetic, not judgement — same reason as 07-29**: **S19's and S23's windows both close 2026-08-05.** A labour print landing after every registered rate observable has settled cannot move one |
| **FTNT (2026-07-30)** | **Folded into the Lens-3 momentum re-tag rather than duplicated.** Same 20-vs-60 shape as the rest of the security node; a standalone bracket double-counts the S30 family |
| **A second Materials bracket** | **S36 already owns the sector to 2026-08-05.** This run's contribution was to **disqualify S36's own confirming leg**, not to add a threshold on the same series |
| **GRMN** | The sweep's **#1 flow score of all 300** with a **129% last-20 concentration** and **no thesis anywhere in the desk's files**. **A bracket needs a proposition to threaten and there is none.** Logged as a coverage gap instead |

## S50 — ★★ AMD/ANET 2026-08-04 · the AI-capex-guidance read no bracket owns · ARMED · → 2026-08-06

Registered **2026-07-31 by the `industry_US` PREMORTEM (Lens 2).** IDs checked against EVERY existing
row in BOTH files before writing (**D76** collision class); highest existing ID was S49 (US) / S47-KR (KR).

**Why it exists.** The window's AI-capex prints are otherwise bracketed only on the *utilities/power*
side (S24/S35/S40/S47) and the *memory* side (S30). **No bracket owns the silicon/networking demand
read** — whether AMD's datacenter guide and ANET's cloud-titan revenue confirm or decelerate the
hyperscaler build. This is the leg that reads THROUGH to the AI-power node.

⚠ **ASYMMETRIC by information content (L3/B4), and registered *because* of it:** a raise/beat only
**confirms volume** (it cannot un-measure the capex the hyperscalers already guided up) → low info;
a **guide CUT** is the branch that changes a conclusion. Per the rule "if NEITHER branch changes the
conclusion, drop it" — branch B here DOES, so it is worth bracketing despite branch A being confirmatory.

| Branch | Observable | Meaning |
|---|---|---|
| **A (confirmatory, low-info)** | AMD next-Q datacenter revenue guide **≥ prior-Q y/y growth rate** AND ANET reaffirms cloud-titan revenue | Hyperscaler build intact; **confirms volume only, changes no DEEP conclusion** |
| **B (against us — the informative branch)** | AMD datacenter guide **cut y/y** OR ANET guides next-Q datacenter/cloud-titan revenue **down y/y** | Hyperscaler capex is **decelerating at the silicon layer** → reads through to the AI-power node (CEG/VST) and IT N(split); **NVDA's EXTENDED-BUT-LIVE tag flips toward EXHAUSTED** |
| **C** | mixed (one up, one down) | `AMBIGUOUS` — n≈1 same-day, so a split is uninformative |

- **Frozen observable**: the **guidance line in each company's 08-04 release** (datacenter/cloud-titan
  revenue *direction* y/y), scored on the **stated guide, NOT the price reaction** (a cut the tape
  buys still scores as a cut).
- ⚠ **Implied move NOT used**: `module_flow` returned **D0 (07-31) expiry** straddles for both names
  — a 0-DTE straddle does not price an 08-04 event. **No magnitude threshold is fabricated**; this is
  a **direction test on the guide** (the S48 precedent). Positioning at registration: **AMD P/C 0.99,
  skew +22.3** (already hedging downside) · **ANET P/C 0.46** (complacent-bullish).
- ⚠ **n ≈ 1 declared at registration (S1/B3)**: AMD and ANET print the same session.
- **Information content (L3)**: only branch B changes a conclusion; branch A is pre-declared confirmatory.
- **Invalidation**: an acquisition/guidance-withdrawal by either ⇒ idiosyncratic, re-register.

## S51 — ★★ NFP 2026-08-07 · the FIN OW− flattener risk no LIVE bracket owns · ARMED · → 2026-08-10

Registered **2026-07-31 by the `industry_US` PREMORTEM (Lens 2).**

**Why it exists.** FIN OW− now rests on a **measured mechanism**: the bear steepener (2s10s
+0.35→+0.45 on the published curve) is NIM-positive (P13). The prior run's rate observables (S19 FOMC,
S23 bear-flattener-hold) **had event date 2026-07-29 and have now settled** — so the flattener risk to
FIN is **uncovered by any live bracket**, and NFP is the next print that moves the front end. ⚠ The
2026-07-30 run *declined* an NFP bracket because S19/S23 were still armed and NFP landed after them;
that reason has expired with those brackets, so the flattener risk is now genuinely un-bracketed. A FIN
OW− carried WITHOUT bracketing the flattener would be a one-way tilt into a known binary.

| Branch | Observable | Meaning |
|---|---|---|
| **A (with the OW)** | derived **2s10s stays ≥ +0.35** at the settled 2026-08-07 close (front end stable-to-selling, long end holding) | The **bear steepener persists** → NIM thesis intact, FIN OW− confirmed on its fresh mechanism |
| **B (against us)** | derived **2s10s ≤ +0.20** at the settled 2026-08-07 close (hot print → cut-repricing out → front-end sells harder than the long end) | **Bear FLATTENER** trips the S23 line → the NIM mechanism breaks; **FIN OW− loses its only non-retracted leg (R32 killed the breadth reason)** |
| **C** | +0.20 to +0.35 | No conclusion changes |

- **Frozen observable**: **derived 2s10s = DGS10 − DGS2 [FRED], settled daily close of 2026-08-07**
  (or the first settled close after NFP if 08-07 is unpublished), one named source, never intraday.
  **State at registration: DGS2 4.22 · DGS10 4.67 (asof 07-29) ⇒ 2s10s +0.45.**
- ⚠ **No single-name straddle prices NFP** — a macro observable is used, so **no magnitude is
  fabricated**; the ±20bp threshold is a **level on the curve**, chosen to sit at the S23 flattener line.
  Positioning context: **KRE P/C 1.87, JPM skew +27.1** — banks already defensively hedged into the print.
- **Information content (L3)**: **BOTH branches change the FIN conclusion** (the mechanism is the whole
  OW), so this is a symmetric, information-bearing bracket.
- ⚠ **Bull-steepener caveat**: a >20bp front-end *rally* would be a bull steepener with recession/credit
  fear — 2s10s could widen while FIN still suffers. That is NOT scored here (this bracket owns the
  flattener leg); if HY OAS breaks >2.90% on the same print, read it as the credit-fear overlay separately.

## Brackets considered and DROPPED 2026-07-31, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **MPC 08-04 / PSX 08-05 (standalone equity bracket)** | **S49 already owns the refining print** (its named catalysts ARE MPC 08-04 / PSX 08-05) and **S31** owns the business-vs-war-premium question to 08-05. A standalone equity bracket double-counts. MPC's ±8.5% D21 straddle covers its print — noted for S49, not a new row. |
| **PSX 08-05 (separate from MPC)** | Same distillate-crack thesis, adjacent date ⇒ **n≈1 with MPC**, no independent information. |
| **CEG 08-06 + VST 08-07 (new AI-power bracket)** | **S35 (regulated cluster → 08-07), S47 (utilities SPREAD → 08-07), S24/S40 (capex→utilities / gigawatt-as-lease)** already own this print. A new bracket double-counts the utilities spread. |
| **LNG 08-06** | Tangential to all three core theses (refining / bank-steepener / AI-power); neither branch moves a DEEP conclusion. |
| **Iran / Hormuz escalation (undated)** | The against-us feedstock-squeeze branch is the **mirror of S8 (owns "Hormuz reopening statement") and S31 (war-premium)**. Carried there, not re-registered. |
| **HLTH (AMGN 08-05)** | Folded into the Lens-1 within-run watch (defensive positioning into the print, no clean bull thrust) — dated re-check 08-05/08-06, not a bracket. |

---

## Scoring-log rows added 2026-08-02 by the `industry_US` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S21** | 2026-07-24 (PREMORTEM Lens 2) | **2026-07-30 (STNG Q2)** | ★ **FIRED-C** | **2026-08-02 HANDOVER (industry_US)** | ⚠⚠ **Past-dated and UNSCORED by both the 07-30 and 07-31 runs — caught here.** Branch C = *"inside ±10.0% either way — no information, pre-committed so an in-band reaction cannot later be read as confirmation."* Observed: **STNG 78.53 (07-29) → 75.53 (07-30) = −3.82%**, −0.85% cumulative through 07-31 ⇒ **comfortably inside the frozen ±10.0%.** ⚠ **Branches A/B were INSTRUMENT-BLIND**: their legs are **Q2 TCE $/day** and **% of Q3 days already booked**, both of which the press release presents in **tables the body scraper does not capture** (the prose says *"Below is a summary of the average daily TCE revenue…"* and the table is absent). ★ Directional context recorded and explicitly NOT used to score: adjusted net income **$243.7m = "the strongest performance in the history of the company"**, EBITDA $300.5m, cash break-even **below $11,000/day**, Q3-to-date product-tanker rates *"above $30,000 per day"* — none of which reads as branch A's *"the rerouting rent has already peaked."* ⇒ **M45 survives.** ⚠⚠ **Registration defect logged as D123 (the D28 family, 3rd instance): the grid puts a FUNDAMENTAL observable in A/B and a pure PRICE-REACTION band in C, so two branches can be true at once.** ⚠ Its cross-check KPI (*"3-2-1 crack ≥65 through 08-06"*) reads 59.865 on the one named daily source **but is an ABSOLUTE LEVEL, which R30/D95 made unscoreable across bar granularity ⇒ the cross-check is `unknown` (C3), not "failed"** |
| **S30** | 2026-07-27 (PREMORTEM Lens 2) | condition-settled → 2026-08-05 | ★★ **FIRED-A (AGAINST US)** | **2026-08-02 HANDOVER (industry_US)** | Branch A = *"median RS20 vs SPY of {STX, MU, WDC} **crosses above 0 by 2026-08-05**"* — a first-occurrence condition. **Observed on the settled 2026-07-31 close: STX +4.1 · MU −15.9 · WDC +0.8 ⇒ median +0.78**, reproduced independently by the desk's own sweep at **+0.6** (D5 ✅). Registration median **−23.7**; path **−16.5 → −28.3 → −25.3 → −10.4 → +0.8**. **Invalidation checked and NOT triggered: HY OAS 2.84% @ 07-30 < the 3.10% line** ⇒ an IT event, not S26's. **Branch A's stated meaning: the 60-day run was pausing, not topping; M149's decaying-stock reading is falsified; the IT-Neutral's "wait for the 08-19→09-07 roll-off" defence is wrong for the whole stack.** ⚠ **The bracket's own control pair SPLIT — DELL +6.2→+2.5 (falling) vs HPE +1.4→+15.9 (rising)** ⇒ "memory event vs IT-beta event" is **`indistinguishable` (C4)**, recorded not decided. ⚠ **STX's own 07-30 move (+11.4%) is inside its frozen ±14.6% no-information band** and may not be read as confirmation. ⚠ **n≈2 sessions carrying two mega-cap prints (S1).** ★★ **PREMORTEM Lens 3 then attacked the verdict's use: on the desk's own M149 method MU's days-21-60 base is +41.2 (the basket's strongest) against STX's +3.7 — the desk carried the name with DIRECTION and dropped the name with the BASE. C4 both ways** |
| **S35** | 2026-07-28 (PREMORTEM Lens 1/2) | condition-settled → 2026-08-07 | ★★ **FIRED-A (AGAINST US) — dated 2026-07-29, CAUGHT LATE** | **2026-08-02 HANDOVER (industry_US)** | Branch B = *"median RS20 vs SPY stays ≤ 0 **through** 2026-08-07"* — a persistence condition that **one crossing breaks**. **It crossed to +0.39 on the settled 2026-07-29 close** (WEC −2.38 · ETR −3.84 · EXC +3.20 · SO +2.67 · XEL +0.39 · AEP −3.10 · D +5.63), independently reproduced here at **+0.39** ⇒ **A fired, dated 07-29.** ⚠⚠ **The 2026-07-30 run measured exactly +0.39, wrote *"the branch that says the 07-28 UW demote was WRONG is now live on settled data"*, and then filed it *"Not scored — window runs to 08-07."* That is the S39/S29 failure shape a THIRD time and the FIRST on the US desk.** ★ **Honest qualification recorded WITH the verdict and not used to soften it: the cross lasted ONE session — the median ran +0.39 (07-29) → −1.30 (07-30) → −4.89 (07-31).** The threshold is frozen and the verdict stands; **the economic content is thin.** ⇒ **new defect D121: a sign test on a median with no persistence requirement fires on a single-session crossing that immediately reverts.** ⚠⚠ **Directly contradicted by S47 FIRED-B below, and S47's own registration pre-committed that the disagreement IS the finding** |
| **S47** | 2026-07-30 (PREMORTEM Lens 1) | condition-settled → 2026-08-07 | ★★ **FIRED-B (with the label)** | **2026-08-02 HANDOVER (industry_US)** | Branch B = *"the spread **narrows to +7.0pp or less by 2026-08-07**"* — first-occurrence. Observed on settled 2026-07-31: **(regulated-7 median RS20) − (AI-power-4 median RS20) = −4.89 − (−6.77) = +1.88pp**; the desk's own sweep gives **+2.3pp**. Registration **+14.74pp**; path **+5.06 (07-24) → +2.44 (07-27) → +8.31 (07-28) → +14.74 (07-29) → +6.35 (07-30) → +1.88 (07-31)** — the independent recomputation reproduces the registration's own *"same construction on 07-28: +8.32pp"* to **0.01pp** (**D5 ✅**). ⇒ **the legs re-converged; one sector verdict is defensible and the N− stands on its own terms.** ★★ **S47 pre-committed that if it disagreed with S35/S24 *"the disagreement is the finding"* — it does, and both fired within 48 hours on the same seven names. The joint reading handed to ROTATION is that BOTH thresholds are too twitchy for a two-day-old post-crash tape, not that one leg is right** |
| **S25** | 2026-07-25 (PREMORTEM) | condition-settled → 2026-08-08 | **FIRED (threshold met) — ⚠ ZERO-INFORMATION** | **2026-08-02 HANDOVER (industry_US)** | Frozen threshold = *"**by 2026-08-08**, DLR RS20 vs SPY **falls below** the {PLD, AMT, WELL} median while the median stays positive."* Met on **four consecutive settled sessions**: 07-24 DLR **+2.82** < +4.42 · 07-27 **+0.04** < +3.82 · 07-28 **+1.38** < +5.94 · 07-29 **+7.11** < +9.70, median positive throughout. Reversed 07-30 (**+10.11 > +5.59**) and 07-31 (**+8.48 > +3.41**) — post-fire context that does **not** un-fire a frozen threshold. ⚠⚠ **New defect D122, and it is the more important half of this row: the condition was ALREADY TRUE on the registration bar** — S25 was registered 07-25 on numbers `asof 2026-07-24 settled`, and on that very bar DLR **+2.82 < +4.42** with the median positive. **A branch satisfied by the data on the day it is frozen cannot discriminate — it records a state, not a forecast.** ⇒ **The verdict is logged for the record and is NOT cited by any downstream stage as evidence about Real Estate** |
| **S36** | 2026-07-28 (PREMORTEM Lens 2) | condition-settled → 2026-08-05 | **FIRED-B (with us)** | **2026-08-02 HANDOVER (industry_US)** | Branch A required the XLB 5-day excess vs SPY to be **"still > 0"** AND the green count **"still 0"** — a persistence condition. **Observed settled 2026-07-31: XLB 5-day excess vs SPY = −2.72pp** (path **+3.12 at registration → +5.46 → +4.21 → +2.21 → −2.72**), green count **still 0 of 12** ⇒ **A's persistence is broken ⇒ B fires: the divergence resolved itself and the 07-27 move was noise.** ⚠⚠ **Consequence against a decision the desk already took: the 07-30 ROTATION moved Materials UW → N on the *disqualification* of A's green-count leg (M238/M273). The surviving price leg has now settled the other way, so that N sat on ground its own bracket no longer supports — the 2026-08-02 ROTATION reverted it to UW.** ⚠ Name-level caveat: **NUE (RS20 +16.3, FINRA z −1.40 = the cleanest short-collapse on the desk's pull) and STLD (+13.7)** are the only two names reaching the accumulation pre-condition |
| **S14-num** | 2026-07-25 (PREMORTEM) | 2026-07-30 (MA Q2) | — **recorded, pre-committed NO-INFORMATION** | 2026-08-02 (industry_US) | MA's print-day move was **+2.49% (07-29 563.32 → 07-30 577.35)**, **inside the pre-declared ±3.9% band** ⇒ **it may NOT be read as confirming the FIN OW.** S14 itself scores **2026-08-06** on cross-border volume + {MA, V, PYPL} RS20 vs SPY; all three are currently positive (**+6.5 / +1.1 / +26.7** on the desk's sweep) and the {MA, V}-only ANNEX reading agrees in sign. ⚠ **PYPL's +26.7 is still the Stripe merger-arb spread (S14-ANNEX / D50), not payments breadth** |
| **S46** | 2026-07-30 (PREMORTEM Lens 1/2) | 2026-07-30 AMC → 2026-08-13 | — **branch A leg 1 MET; leg 2 NOT met** | 2026-08-02 (industry_US) | **Leg 1 (gross-margin guide flat or down): MET.** AAPL guided September-quarter gross margin to **47–48% against 50.1% reported = −2.1 to −3.1pp** `[measured]`. **Leg 2 (AAPL−QCOM RS20 spread narrows below +15pp): NOT met on settled data — the spread is +16.4pp** on the desk's own 08-02 sweep (AAPL −0.2, QCOM −16.6) and **+16.34pp** on an independent recomputation. ⚠⚠ **The 07-31 run read it as +13.2 on a LIVE intraday bar and the stale 07-31 JSON gave +13.7 — both below the line, both superseded by settlement. A D74 instance that would have mis-scored the bracket had the window closed on it.** ⇒ **branch A does NOT fire; the bracket stays ARMED to 08-13.** ★ **Reaction test, registered separately (the D28 fix): AAPL fell −7.35% on 07-31 against a pre-declared ±3.3% band ⇒ OUTSIDE, the move IS information** |
| **S32** | 2026-07-27 (PREMORTEM Lens 2) | 2026-07-28 COT → 2026-07-31 | — **AMBIGUOUS verdict UNCHANGED (append-only)** | annex added 2026-08-02 | ⚠ **The verdict is NOT rewritten** — it was correct at its deadline. **Annex, because the record must show the answer arrived ~24 hours late**: the CFTC release the bracket named **has now published and this run read it**, freshness established by value-diff against M125 (**D104 is unfixed — the tool still prints no `asof`**). **On that release BOTH legs of branch B are satisfied: the Nasdaq-100 net-spec percentile stayed at the 5th (<10th) and QQQ RS5 vs SPY = −0.55% (≤0).** ⇒ **D104 cost this desk a scoreable bracket by about one day, and that is the concrete argument for fixing it.** Full pull: **NDX 5th · S&P500 82nd · R2K 57th (wk −8,137, the board's largest de-risking) · UST10Y 13th (+3,587) · UST2Y 55th (+30,023) · USD 72nd · WTI 10th · NatGas 3rd · Copper 96th · Gold 23rd · Silver 29th.** ⚠ **Per the bracket's own registration text none of this may be cited as a SIGNAL by any stage** — COT contrarian is in the REJECTED grade (D6) |
| **S52 · S53** | **2026-08-02 (industry_US PREMORTEM, Lens 2)** | 08-06 / 08-05 | — | — | ARMED — ★ **S52** brackets the **Iran conditional of 2026-08-02 both ways**, which is the ≤48h binary the protocol requires a both-sides bracket on · ★ **S53** fills **the gap MACRO §0 and EVENT_ALPHA §10 both named — MPC owned no bracket of its own.** Full brackets below |

---

## S52 — ★★★ Iran: a DATED Strait reopening vs resumed strikes on Iranian ENERGY INFRASTRUCTURE · ARMED · → 2026-08-06

Registered **2026-08-02 by the `industry_US` PREMORTEM (Lens 2)**, hours after the triggering post and
**before either branch resolved.** **ID checked against EVERY existing row in BOTH files (the D76
collision class); the highest existing ID was S51 (US) / S47-KR (KR).**

**The event.** Trump, Truth Social, **2026-08-02 03:19 BST**: strikes cancelled *"subject to being able
to rapidly make a DEAL"*, where the deal *"would include the immediate opening of the Strait of
Hormuz"* and an end to Iran's nuclear threat; same post, the US is *"locked and loaded and ready to
go"* `[bbc 08-02, full body; corroborated dw 08-02]`. Per CBS via the BBC the **cancelled plan targeted
Iranian ENERGY INFRASTRUCTURE specifically.**

**Why this is not a duplicate of S8.** S8 brackets the *generic* de-escalation on price-keyed branches
and is **undated by construction**. This adds two things S8 never had: a **named precondition
structure** (deal to dated opening), and a **named alternative that is a supply shock with a different
transmission** — fuel cost into Industrials (M91), not only crude level into Energy.
⚠ **The Strait is NOT open. Scoring S8 branch A off a precondition would be scoring a narrative event
— the 07-27 run already refused exactly that, and that refusal binds here.**

| Branch | Frozen observable | Meaning |
|---|---|---|
| **A (against ENRG OW)** | A **dated** Strait-reopening term in a **primary text** — a signed-agreement text, an official US Treasury/State statement, or a direct Iran-government statement carrying a date or "effective" language. **NOT a headline paraphrase, NOT a repeat of the 08-02 conditional wording** | The war premium gets a falsifiable exit. **XOM · CVX · OXY · COP lose the leg S31 already says they are standing on** |
| **B (against INDU N and the P16 breadth read)** | A reported strike on **named** Iranian energy infrastructure (refinery, export terminal, storage/processing), corroborated by **at least 2 independent outlets reading the SAME primary event** — not rhetoric repeated | Supply shock the other way: ENRG OW gets a harsher confirmation while the **fuel-cost leg (M91: ~8 of UNP's 12 revenue-growth points are fuel surcharge)** and the risk-on breadth read take the hit |
| **C** | Neither by **2026-08-06** | S8 stays ARMED unchanged; no conclusion changes; rolls forward undated |

- **Starter lists, `asof 2026-07-31 settled`, benchmark SPY inline.** **Branch A rips against** —
  the four with the largest 20-vs-60 gap, i.e. the most premium to give back: **OXY +16.4 / −7.0
  (flow 0.556)** · **COP +14.7 / −5.5 (0.628)** · **CVX +16.0 / −1.0 (0.600)** · **XOM +13.1 / −2.9
  (0.606)**. **Branch B rips against**: **UAL −9.3 / +26.3 (🔴 −0.850)** · **DAL −6.0 / +20.2
  (🔴 −0.674)** · **CAT −15.7 / −13.1 (🔴 −0.589)** · **UNP +3.2 / +7.4 (+0.436)**.
- ⚠ **NO implied move exists and none is invented** — no straddle prices a Truth Social conditional.
  **Scored on primary text and event confirmation, never on price** (the S9/S51 treatment).
- **Information content (L3): BOTH branches falsify a currently-held conclusion, so this is symmetric
  and high-information.** That is why it is written rather than dropped.
- **Invalidation**: an actual **signed multilateral agreement** supersedes this bracket entirely —
  re-register against a state-department verification standard rather than scoring A off a signature.

## S53 — ★★ MPC (2026-08-04) + PSX (2026-08-05): the equity-EXECUTION leg S49 cannot see · ARMED · → 2026-08-05

Registered **2026-08-02 by the `industry_US` PREMORTEM (Lens 2), before both prints.**

**The gap it fills, and why the 07-31 drop was wrong on its own terms.** **S49's frozen observable is
the COMMODITY 5-session distillate-crack change** — a market-level number that says nothing about
whether MPC's or PSX's **realised crack CAPTURE** (hedging lag, turnaround downtime, inventory timing)
tracks the spot. The 07-31 run dropped a standalone bracket here on the reasoning *"S49 already owns
the refining print"* — **true for the commodity, false for company execution.** **MACRO §0 and
EVENT_ALPHA §10 both named this the gap PREMORTEM must fill.**

| Branch | Frozen observable | Meaning |
|---|---|---|
| **A (confirmatory, LOW information)** | Guide/commentary describes sequential crack **capture** as stable-to-improving, consistent with the spot distillate crack | Only confirms what S49 branch A already assumes at the commodity level — **no conclusion changes** |
| **B (against us, INFORMATIVE)** | Guide/commentary flags margin **compression**, a **hedging-timing lag against spot cracks**, **or** unplanned **turnaround/maintenance drag** | New negative information **at the execution level S49 cannot reach** — threatens the ENRG OW's refining leg *independently* of whether the commodity crack holds |
| **C** | Mixed (one confirms, one compresses) | **`AMBIGUOUS`.** ⚠ **n is about 1 — the prints are date-clustered 08-04/08-05 and are NOT independent samples (S1)** |

- **Implied moves, taken from the market, registered as a SEPARATE and LABELLED price-reaction test
  (the D28 fix — they are NOT inside any branch condition)**: **MPC ±8.8%, expiry 2026-08-21 (D19) —
  COVERS its print.** **PSX ±5.3%, expiry 2026-08-07 (D5) — COVERS its print.** A settled-close move
  beyond either band is recorded as a magnitude fact only; **the stated guide scores the branch.**
- ★ **The positioning split is itself a finding.** **MPC's option book is internally contradictory —
  skew +33.0 (heavy downside-tail demand) against P/C 0.44 (call-dominant)** ⇒ **`indistinguishable`
  (C4)**. **PSX's is coherent and bearish-leaning — P/C 1.25, the only fear profile on the desk's
  pull, PLUS FINRA short z +1.53, the only 🔴 short surge.** ⇒ **if branch B fires anywhere in this
  duo, PSX is the name already positioned for it.** ⚠ **PREMORTEM Lens 3 independently re-tagged PSX
  EXHAUSTED on the desk's own M149 method (days 21-60 = −5.5).**
- **State at registration** `asof 2026-07-31 settled`, benchmark SPY: **MPC +18.5 / +18.3 (flow
  0.567)** · **PSX +19.7 / +14.2 (0.600)** · read-across **VLO +16.6 / +20.2 (0.556)** · **XOM
  +13.1 / −2.9 (0.606)**.
- **Information content (L3): asymmetric in the useful direction** — branch B can falsify a desk
  conclusion, branch A can only confirm.
- **Invalidation**: an M&A/restructuring announcement at either name means idiosyncratic, re-register.
  ⚠ **And if S49 branch B (distillate 5-session change ≤ −5.0) fires BEFORE these prints — it is one
  session of its current rate away — S49 owns the outcome and this bracket collapses to a name-level
  footnote. Noted at registration so no later stage double-counts them.**

## Brackets considered and DROPPED 2026-08-02, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **AMD 2026-08-04** | **Already owned by S50.** ⚠ Logged rather than dropped silently: AMD's straddle is **±4.0% expiring 2026-08-03 (D1) — BEFORE its print**, so **no magnitude threshold is obtainable and none was fabricated.** S50's direction-only design anticipated exactly this |
| **ANET 2026-08-04** | **Not a new bracket — an ANNEX CANDIDATE for S50.** ANET's **±11.3% (expiry 08-07, D5) now COVERS its print**, which was **not true at S50's 07-31 registration** (*"no options instrument covers this"*). **Recorded so the annex can be attached by whoever owns S50; S50 is NOT re-frozen here** |
| **CEG · LNG (08-06) · VST (08-07)** | **S35 · S47 · S24 · S40 already own this print cluster in full**; ownership has not changed since 07-31, so there is no incremental falsifying power. ⚠ **The correct response to this cluster was a DEEP promotion (UTIL), not another bracket — and that promotion was made** |
| **July NFP 2026-08-07** | **S51 already owns the regime flip it threatens** (the 2s10s flattener test to 08-10). A headline-payrolls axis without the curve reaction is the non-actionable shape (D6 class) |
| **July CPI 2026-08-12** | **P1 (breakeven vs real), S26 (HY OAS) and S41 (IG OAS) already own every transmission channel CPI would move.** No incremental falsifying power |
| **Japan / yen intervention (undated)** | ⚠⚠ **The board's LARGEST un-bracketed regime-flip risk, deliberately NOT bracketed — and the reason is a rule, not an oversight.** `theme_age` 5.31× (the board's fastest), a quantified **¥8.45tn** intervention, a US Treasury warning, a "rare Japan-Korea joint intervention". **But D22 is open — there is no lag table linking a JPY intervention print to DGS30 — so any threshold would be fabricated, which is precisely the failure W2 punishes.** ⇒ **escalated to a human instead of registered** |

## S35-ANNEX — ★★★ basket-contamination notice: **one of the seven names stopped being a regulated utility inside the bracket's own window** (**S35 is NOT re-frozen; S47 is NOT re-frozen**)

Registered **2026-08-02 by the `industry_US` DEEP-UTIL**, hours after this run's own HANDOVER scored
**S35 FIRED-A** and **S47 FIRED-B**. **Neither verdict is rewritten** — the threshold is frozen at
registration and moving it after the print converts a forecast into a description (L3). **This annex
records what the verdicts were measured ON.**

**Finding 1 — `D` (Dominion) is a MERGER-ARBITRAGE security, not a rate-sensitive regulated utility.**
**NextEra is acquiring Dominion in an all-stock deal at a 0.8138 NEE/D ratio; the DEFM14A was filed
2026-07-28** — i.e. **one day before the 07-29 close on which S35's branch A fired.** Measured this
run: **D's price correlates +0.89 with NEE and −0.21 with SPY**, and the D/NEE price ratio has
converged from a ~20% deal-risk discount 60 sessions ago to **2.2%** now.
★ **This also explains an anomaly two separate desk files flagged and neither could account for**:
D's *"accumulation on no volume"* — `vol_surge` **0.42, the sector's lowest** — noted by the 07-31
DEEP-UTIL and again by this run's SWEEP. **A converging arb spread trades on little volume by
construction.**

**Finding 2 — removing D changes the fired verdict's arithmetic.** On the **regulated-SIX** basket
{WEC, ETR, EXC, SO, XEL, AEP}: the **07-29 median never crossed zero — it reads −0.99, not +0.39.**
⇒ **S35's branch A fired on a basket artifact.** ⚠ And the correction runs **against** the desk, not
for it: the 07-31 six-name median is **−5.85 vs −4.89 with D included**, so **the UW− case is
stronger without D, not weaker.**

**Finding 3 — the instrument itself has no information at this threshold (this substantiates D121).**
Reconstructed over the last **40 settled sessions** from the desk's own price cache (verified to
reproduce the published 07-29 and 07-31 values exactly): the regulated-7 median RS20 vs SPY
**crosses zero 10 times in 40 sessions**, its **daily σ is 2.08pp**, and **60% of all readings sit
within 1σ of zero.** ⇒ **the +0.39 print that fired S35 is a 1.1σ one-day wobble, statistically
indistinguishable from zero.** Separately, **S47's branch-B condition (spread ≤ +7.0pp) is the MODAL
state — true 70% of the time over the same 40 sessions** ⇒ **branch B firing is not a resolution, it
is the base rate.**

**What this changes and what it does not.**
- **UNCHANGED**: S35 = **FIRED-A**, S47 = **FIRED-B**, both scored against their frozen thresholds.
  **Append-only. No threshold is widened, no basket is re-cut retroactively.**
- **CHANGED**: **neither verdict may be cited downstream as evidence about Utilities.** The desk's
  own precedent for this is **S14-ANNEX** (a contaminated leg — PYPL's Stripe bid) and **S33-ANNEX /
  S43-ANNEX** (an estimator-error notice registered hours after the bracket).
- ⚠⚠ **This is D50's exact failure mode reproduced** — *"before freezing a multi-name observable,
  check each leg for a live corporate action."* D50 was logged on 2026-07-24 after PYPL; **S35 was
  registered 2026-07-28 and S47 on 2026-07-30, both AFTER D50 existed, and neither checked.**
  ⇒ **D50 is escalated from a registration-discipline note to a MEASURED repeat.**
- **Successor construction proposed, with the measured sigma it rests on**: any future sign test on
  this basket must (a) **exclude any name under a live all-stock acquisition**, and (b) carry either
  a **persistence requirement of k consecutive settled sessions** or a **band wider than the measured
  daily σ of 2.08pp** — not a bare sign test. **The band is stated as hand-set and the sigma it came
  from is named.**

## S54 — ★★★ The beneficiaries of S52 branch A, whom S52's own exposure map omits · ARMED · → 2026-08-10

Registered **2026-08-03 by the `industry_US` PREMORTEM (Lens 1)**, on the live branch, before it
resolved. **IDs checked at WRITE time against EVERY row in BOTH files (M319/D76); `grep` for `S54`
returned 0 in all three.**

**Why it exists.** **S52 names who LOSES on branch A and nobody who WINS** (*"Branch A rips against:
OXY · COP · CVX · XOM"* · *"Branch B rips against: UAL · DAL · CAT · UNP"*). **Branch A is the branch
running** — the 08-02 pool's #1 event by dispersion is *"Trump holds off Iran strikes"* (36 articles
/ 20 outlets, curve **2→4→20**, the only thread accelerating into the window edge), with talks
beginning 08-03 and **WTI −8% intraday on "Iran peace deal hopes"** [fxstreet 08-03].
**The transmission is already primary-sourced (M34)**: DAL/UAL/FDX/LUV disclosed fuel costs **+66% to
+84% YoY**, and **UAL and LUV cut or missed Q3 guidance explicitly citing fuel/crack costs** ⇒ this is
a **falsifiable read-across, not an analogy.** And the two names carry the deepest 60-day bases
outside the security node: **UAL RS20 −9.3 / RS60 +26.3 ⇒ days 21-60 +35.6**; **DAL −6.0 / +20.2 ⇒
+26.2** (settled 07-31, **benchmark SPY inline**).

**Frozen observable**: the **equal-weight 5-session excess return of {UAL, DAL} vs SPY**, on
**settled daily closes only, one provider (`yfinance`, `auto_adjust=False`)**, from the **2026-07-31
close** to the **2026-08-10 close**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | EW{UAL,DAL} 5-session excess **> +8.5pp** | **The fuel-cost relief transmits.** S52-A's beneficiary side is real, and the desk's Energy-only framing of the Iran axis was one-sided |
| **B (the informative branch)** | **< −4.5pp** | The airlines did **not** capture it ⇒ **crude is not the binding variable for them**, and **M34's cost channel does not run in reverse** — a finding about the mechanism |
| **C** | −4.5 to +8.5 | `AMBIGUOUS`. **n≈1 window (S1), declared at registration** |

### ★★★ How the thresholds were chosen — **D93 executed BEFORE freezing, and it rejected the first draft**

**The first draft used ±3.0pp, hand-set.** D93's remedy was then run **before freezing**, on the 60
settled sessions to 2026-07-31:

```
5-session summed excess, EW{UAL,DAL} vs SPY:  mean +2.195pp · sigma 6.562pp · n=60
daily sigma 2.535pp · range [-7.14, +19.56]
```

⇒ **±3.0pp would have fired A 45% and B 28%, making `AMBIGUOUS` the RAREST outcome at 27%** — **M313's
exact failure mode** (*"S47's branch-B condition is the MODAL state ⇒ firing it is the base rate"*),
and it would have gone into a live bracket had the measurement not been run first.
**Widened to mean ± 1σ → A > +8.5pp · B < −4.5pp**, which measures **A 15% · B 25% · C 60%** —
**C is now the base rate, which is what C is for.**
⚠⚠ **The estimator is NOT centred on zero** (5-session mean **+2.195pp**), so a symmetric band around
zero would have been **biased toward branch A by construction.** This **reproduces, on a US pair, the
`industry_kr` desk's 2026-08-02 finding that the residual estimator's centre is a function of the
benchmark's own move — a W1-clean replication, because it was re-measured here rather than imported.**

- **Anti-signal / VOID**: an **airline-specific event on either name inside the window** (strike,
  grounding, FAA action, M&A) ⇒ the fuel axis and the idiosyncratic axis become inseparable ⇒ `VOID`.
  ★ **The S43 precedent, which VOIDed on 2026-08-03 for exactly this reason.**
- **Invalidation**: **S52 scoring branch B** (a named-infrastructure strike) ⇒ crude reverses and this
  bracket's premise is gone; re-register.
- **Information content (L3)**: **branch B changes a conclusion** (it falsifies a primary-sourced cost
  channel carried since M34); branch A confirms. **Asymmetric, and registered because of B.**
- ★ **This is the first bracket on this desk registered with its own σ measured, its draft threshold
  rejected on that σ, and both facts written into the registration.** D93 was created *after* S43
  failed this test; **S43 VOIDed the same day** with its ±1.0pp band measured inside a 2.92pp σ.
  **The rule has now paid for itself once in each direction on one date.**

## S50-ANNEX — ★★ implied-move availability notice (**S50 is NOT re-frozen**)

Registered **2026-08-03 by the `industry_US` PREMORTEM**, on the **S14-ANNEX / S33-ANNEX / S43-ANNEX /
S35-ANNEX** precedent.

**S50 recorded at registration (2026-07-31)**: *"Implied move NOT used — `module_flow` returned D0
(07-31) expiry straddles for both names; no magnitude threshold is fabricated."*
**That has changed for one of the two names and not the other:**

| Name | Implied move (2026-08-03) | Expiry | Covers the 08-04 print? |
|---|---|---|---|
| **ANET** | **±11.7%** | **2026-08-07 (D4)** | ✅ **YES — event-priced for the first time** |
| **AMD** | ±6.4% | **2026-08-03 (D0) — expires TODAY** | ❌ **NO. M89/M212's pattern, 7th instance** |

⚠⚠ **S50 IS NOT RE-FROZEN.** It is a **direction test on the guide**; adding a magnitude leg after the
print window opened would convert a forecast into a description.
★ **What the annex requires instead**: at scoring, record **ANET's realised move against ±11.7% as a
SEPARATE, LABELLED reaction test** — the **D28 fix** (S7 put a price reaction inside an observable's
branch condition; every bracket since keeps them separate).
⚠ **Positioning moved since registration — recorded, not scored**: **AMD P/C 0.99 → 0.38, skew
+22.3 → +0.0** (hedged → complacent, into its own print); **ANET P/C 0.46 → 0.10, skew +12.5**;
**MPC ±8.9% / exp 08-21 (D18), P/C 0.44** — MPC's straddle **covers** its print and is **±8.9% against
the ±9.4% the 07-30 run recorded** (compression, **not** a re-freeze).

## S55 — ★★★ Is the crack release PHYSICAL or WAR-PREMIUM? The leg discrimination S49 cannot perform · ARMED · → 2026-08-11

Registered **2026-08-04 by the `industry_US` PREMORTEM (Lens 2), hours after S49-B fired and BEFORE
either branch could resolve.** **IDs checked at WRITE time against EVERY row in all three
`SCENARIOS*.md`, both `STANDING_VIEW*.md` and `RESEARCH.md`** (D76 / M319 / D137 classes); highest
existing was **S54 (US) / S51-KR (KR)**. ⚠ `grep S55` returns exactly one hit — **prose inside the
08-03 collision note** (*"grep for S54/S55/S50-ANNEX returned 0"*), **not a registration.** Checked,
not assumed.

**Why it exists.** **S49-B fired and registered the meaning *"the bottleneck is releasing… WITHOUT a
Hormuz statement."* A crack is a DIFFERENCE OF TWO LEGS, and a difference cannot say which leg moved.**
Measured over S49's own window (07-27 → 08-03 settled): **HO 4.112 → 3.877 = −5.72%** and **CL 82.61 →
80.34 = −2.75%** — ***both* legs fell.** Over the trailing 60 settled sessions **corr(5-session crack
change, 5-session WTI % change) = +0.319**, and on the **five** prior occasions the crack fell ≤ −5.0
the **median 5-session WTI change was −3.91%** ⇒ **crack collapses in this sample are whole-barrel
de-risking events, which is the OPPOSITE signature to a physical bottleneck release** (crack down,
crude flat-to-up). **S49 cannot separate these and its conclusion depends entirely on which it is.**
★ **This is also the row that lets S52 branch A be detected on ECONOMICS when its primary-text bar
never clears** — the structural hole Lens 2 named: *"a bracket whose branch cannot fire while the
world it describes is already happening is not conservative, it is blind."*

| Branch | Observable (5-session change, **settled daily bars**) | Meaning |
|---|---|---|
| **A (S49-B's meaning is RIGHT — durable)** | **HO %chg − CL %chg ≤ −3.0pp**, 2026-08-04 settle → 2026-08-11 settle | Distillate weakens **independently of crude** ⇒ the product-specific release is real. **ENRG OW− loses its refining leg structurally**, and the rail fuel-surcharge revenue leg (M91, magnitude already retracted by R38) is durably impaired |
| **B (S49-B's meaning is WRONG — reversible)** | **HO %chg − CL %chg ≥ +6.5pp** | The distillate premium **rebuilds** ⇒ the 08-03 collapse was the geopolitical premium deflating across the whole barrel; **S31's "business vs war premium" resolves to war premium**, and **ENRG OW− must NOT be cut on S49-B** |
| **C** | −3.0 to +6.5 | No conclusion changes; the cause stays unseparated |

- **Frozen observable**: `HO=F` and `CL=F` **front-month settled DAILY closes**, yfinance,
  `auto_adjust=False`, **one named source, never mixed with intraday.** Anchor = the **2026-08-04
  settle** (in the future at registration ⇒ **no look-ahead**); endpoint = the **2026-08-11 settle**.
  **Both bars re-pulled IN FULL at scoring (D140** — this exact series revised **3.371 crack points
  two days after settling).**
- **State at registration**: last **settled** spread value **−2.953pp (08-03)**. ⚠ The **live 08-04
  bar reads ≈ −7.1pp and is UNSETTLED — recorded and explicitly NOT used.**
- ★★ **D93 executed BEFORE freezing, and it changed the design.** 5-session (HO% − CL%), trailing 60
  settled sessions, **re-measured independently by MACRO rather than taken from the lens**:
  **mean +1.981 · σ 4.671 · range [−9.06, +13.15]**. ⚠⚠ **The estimator is NOT centred on zero** — a
  symmetric ±band around 0 would have been **biased toward branch B by construction**, reproducing
  **S54's and `industry_kr`'s finding on a THIRD independent estimator.** Bands ≈ **mean ± 1σ** ⇒
  **A ≤ −3.0 (measured base rate 15.0%) · B ≥ +6.5 (15.0%) · C ≈ 70% modal**, which is what C is for
  (M313). ⚠ **The lens returned mean +1.829 · σ 4.816 · base rates 16.7 / ~15 on the same definition;
  the small gap is a window-alignment difference and is recorded rather than reconciled away (C1).**
- **Information content (L3): BOTH branches change a live conclusion** — A converts ENRG OW− into a
  structural cut and hits INDU on the surcharge leg; B blocks that cut and resolves S31. **Symmetric,
  high-information. This is the row that decides what to do with the fire the desk already has.**
- **Invalidation, written to D149's standard — the SAME evidentiary bar as the branches** (this is the
  first bracket registered after D149 and it is written to it deliberately): a **product-specific
  supply event** inside the window — a **named** US refinery outage or fire, a Colonial-class pipeline
  disruption, or a **dated** change to the Russian diesel-export regime — evidenced by **a primary
  operator/regulator statement OR two independent outlets reading the same primary event** ⇒ the two
  legs decouple for a reason unrelated to either branch ⇒ **VOID, not scored.**

## S56 — ★★★ SPCX 2026-08-06 unlock: counted supply vs counted positioning, on the desk's own REJECTED rule · ARMED · → 2026-08-11

Registered **2026-08-04 by the `industry_US` PREMORTEM (Lens 2), two days before the event.**

**Why it exists.** A **dated, share-counted, primary-sourced natural experiment** on the one rule this
desk carries in its **REJECTED** signal ledger: **positioning is not a signal (D6)**. Here positioning
is **not a percentile** — it is **219.3M shares short = ~34% of public float = $24.6bn** `[S3 Partners
via bloomberg/yahoo_finance, asof 2026-07-29]`, **9.4× the 23.3M of June 16** — against a supply event
of **up to 911.5M shares taking free float from ~5% to ~12% of shares outstanding**, on a **named
date.** **Both quantities are known in advance, which is what a COT percentile never is.**
⚠⚠ **Registered honestly: this bracket threatens a METHOD conclusion, not a sector tilt** — the desk
holds no SPCX exposure. It is written anyway because **every future bracket that cites a positioning
percentile inherits the answer**, and because **SPCX is the desk's own named instrument gap** (absent
from `us_top300`, the TSM/LNG class, M252/M287). ★ **If a human judges a method conclusion
insufficient, drop it under the GRMN precedent and say so — but do not drop it silently.**

| Branch | Observable | Meaning |
|---|---|---|
| **A (supply loses / positioning wins)** | SPCX **3-session excess return vs SPY > +3.5pp**, 2026-08-05 settle → 2026-08-10 settle | The counted short beats the counted supply ⇒ **D6 is wrong for SHARE-COUNTED positioning**, and the desk's percentile-based positioning dismissals need a stated scope limit |
| **B (supply wins)** | **< −12.0pp** | Float doubling dominates a 34%-of-float short ⇒ **D6 survives its hardest available test** and every bracket leaning on it is strengthened |
| **C** | −12.0 to +3.5 | No conclusion changes |

- **Frozen observable**: `SPCX` and `SPY` **settled daily closes**, yfinance, `auto_adjust=False`,
  **3-session excess**, window **2026-08-05 settle → 2026-08-10 settle** — **straddling the 08-06
  unlock and starting AFTER the 08-04 earnings so the two binaries do not contaminate each other.**
- **State at registration**, settled: **07-28 116.41 · 07-29 112.55 · 07-30 112.20 · 07-31 108.37 ·
  08-03 114.53**; live 08-04 ≈118.6 (**UNSETTLED, recorded not used**). ⚠⚠ **Disclosed rather than
  hidden: the name is already squeezing INTO the unlock (+5.68% on the 08-03 settle), so branch A is
  the RUNNING branch at registration.**
- ★ **D93 executed BEFORE freezing**, re-measured independently: 3-session SPCX-minus-SPY excess, all
  available history — **n=32 · mean −4.381pp · σ 7.778pp · range [−26.07, +19.29]**. ⚠⚠ **The mean is
  −4.381, not zero** — a symmetric band would again have been **biased toward branch B by
  construction.** Bands ≈ **mean ± 1σ** ⇒ **A > +3.5 (measured base rate 9.4%) · B < −12.0 (9.4%) ·
  C 81.2%** — **symmetric base rates, C modal.**
- ⚠⚠ **Stated weakness, not hidden (C4): σ is measured on 32 OVERLAPPING windows covering only 35
  post-IPO sessions, all inside a decline, with NO unlock precedent in sample. SPCX has no RS60 and
  cannot have one before ~2026-08-2x. This is the weakest estimator on this desk's board and the
  bracket must be read at that confidence.**
- ⚠ **No implied move is used and none is fabricated** — no SPCX straddle appears in this run's
  positioning pull.
- **Invalidation (D149 standard)**: a **lock-up waiver, staged/phased release, secondary offering, or
  index inclusion** disclosed inside the window, evidenced by **a company filing or an exchange
  notice** ⇒ the two counted quantities change inside the test ⇒ **VOID.** Also **VOID** if the ticker
  fails to resolve on the scoring pull.

## S57 — ★★ Materials UW− has NO live falsifier after 2026-08-05 · ARMED · → 2026-08-12

Registered **2026-08-04 by the `industry_US` PREMORTEM (Lens 2).**

**Why it exists.** **S36 closes 2026-08-05.** The only other Materials row keys on **`DTWEXBGS` against
[117.44, 121.41]** — and that series **just went 11 publication days without printing**, then moved
**120.7105 (07-24) → 119.7034 (07-31) = −0.83%**, landing **mid-range** ⇒ **dormant by construction,
unable to fire on anything short of a ~2% dollar move it may not even observe in time.** **From
2026-08-06 the MATR UW− is a one-way tilt into a live regime flip**: the dollar leg is weakening and
**copper net-spec sits at the 96th percentile.** ⚠ **And the copper number may not be leaned on: the
COT file is a byte-identical stale snapshot of the 2026-07-31 release; the next publication is
2026-08-07** (D104 / D140 class).
⚠ **S36's own confirming leg is already disqualified (M273/M238)** — its "green count still 0" is a
`vol_surge` artifact — **so S36 can only falsify the UW, never confirm it. After 08-05 even that is gone.**

| Branch | Observable | Meaning |
|---|---|---|
| **A (against the UW — informative)** | **XLB 5-session excess vs SPY > +1.9pp** at any settled close through 2026-08-12 | Materials outperform **while the dollar is falling and copper positioning is at the 96th percentile** ⇒ the UW's dollar leg has flipped and the crowded-long leg did not cap it. **MATR UW− loses both of its stated legs** |
| **B (with the UW)** | **< −2.4pp** at the 2026-08-12 settled close | The UW is confirmed on a **fresh, non-retracted** measurement rather than carried by inertia |
| **C** | −2.4 to +1.9 | No conclusion changes |

- **Frozen observable**: `XLB` minus `SPY`, **5-session excess of settled daily closes**, yfinance,
  `auto_adjust=False`, **benchmark named inline (C1)**, window 2026-08-04 → 2026-08-12 settled closes.
- **State at registration**: latest settled 5-session excess **−3.25pp (08-03)** ⇒ **already below
  branch B's line, i.e. the tilt is winning at registration and branch A is the genuinely adversarial
  ask.** Disclosed rather than discovered later.
- ★ **D93 executed BEFORE freezing**, re-measured independently: XLB 5-session excess vs SPY, trailing
  60 settled sessions — **mean −0.226pp · σ 2.152pp.** Bands ≈ **mean ± 1σ** ⇒ **A > +1.9 (measured
  base rate 18.3%) · B < −2.4 (15.0%) · C 66.7% modal** (M313).
- **Information content (L3): both branches change the MATR conclusion** — A removes both stated legs
  of a live UW; B is its first fresh confirmation since S36. **Symmetric.**
- **Invalidation (D149 standard)**: a **single-name event inside XLB** (M&A, or a guidance withdrawal
  by a top-3 weight) evidenced by **a company filing or two independent outlets on the same primary
  event** ⇒ the sector proxy stops measuring the dollar/copper axis ⇒ **VOID.**
  ⚠ **Do not substitute a copper-COT read before 2026-08-07 — the file is stale.**

## S49-ANNEX — ★★★ five measured objections to S49-B's MEANING (**S49 is NOT re-frozen; the FIRE stands**)

Registered **2026-08-04 by the `industry_US` PREMORTEM (Lens 2), the same day S49 fired.**
**Verdict adopted: score the fire, annex the meaning.** Nothing in S49 is struck; the following is
recorded **for S49's scorer and for any stage citing its registered meaning.**

1. ★★★ **The observable is a CHANGE; the registered meaning is a claim about a LEVEL — and the level
   did not release.** The crack fell to **82.502**. Against the trailing year (**n=252 settled daily
   bars, 2025-08-01 → 2026-08-03: mean 51.15 · sd 18.48**), **82.502 sits at the 92.1st percentile,
   ≈+1.7σ above the mean** ⇒ ***"the bottleneck is releasing" describes a bottleneck still tighter
   than 92% of the past year.***
2. **The cause is contested and the evidence points AWAY from "physical release":** both legs fell
   (**HO −5.72% · CL −2.75%**); trailing-60 **corr(5-session crack change, 5-session WTI %chg) =
   +0.319**; the **five** prior ≤ −5.0 collapses carry a **median 5-session WTI change of −3.91%**.
   ⇒ **whole-barrel de-risking, not a product-specific release.** **S55 is registered to settle it.**
3. **The exceedance is smaller than this series' own documented revision.** Margin **2.575 points**
   (−7.575 vs −5.0) against **D140's measured 3.371-point revision = 1.31× the margin**, on the
   freshest and most revision-prone bar in the series. ⇒ **the full re-pull D140 mandates is
   OUTSTANDING and the fire is provisional as arithmetic, not as taste.**
4. **n ≈ 1 (S1): −5.931 of the −7.575 came from the single 08-03 session**, and that session has a
   named non-bottleneck cause (**the Iran-negotiation cluster at 23 outlets; WTI −8% intraday on
   "Iran peace deal hopes"**) **plus a second one — Trump's on-record demand that Exxon and Chevron
   cut retail prices, with the primary body reporting the two majors falling AFTER the comments.**
5. ★ **What SURVIVES, on the D93 test S49 never ran**: the 5-session-change estimator measures
   **mean +2.170 · σ 6.221 (trailing 60)**, so **−5.0 sits at ≈ mean −1.15σ and fires in a measured
   6.7% of trailing-60 windows** ⇒ **NOT inside noise, and NOT M313's modal-branch failure.**
   **The threshold was set by hand without measurement and got lucky; the fire is legitimate.**
   ⚠ **Recorded honestly: the estimator's centre is +2.170, not 0**, so the −5.0/0 branch structure is
   **asymmetric in the desk's favour by construction — the same bias found on S54 and on the KR desk,
   now on a FOURTH independent estimator.** ⚠ The lens returned **8.3%** on the same definition; the
   gap is window alignment and is recorded rather than reconciled away (C1).

★ **A free consistency check the desk already owns and had never connected**: **S54 branch A**
(equal-weight {UAL, DAL} 5-session excess vs SPY **> +8.5pp**, → 2026-08-10) **is the SAME physical
event as S49-B with the opposite sign** — rail fuel surcharge is *revenue*, airline fuel is *cost*.
**If S49-B's meaning is right, S54-A should fire.** Measured settled 08-03: **UAL 🔴 RS20 −4.0 /
RS60 +24.8 · DAL 🟡 −0.7 / +22.0 — the airlines have NOT captured it.** ⇒ **if S54-B fires while
S49-B fired, one of the two registered meanings is false, and the desk learns which WITHOUT spending
a bracket.** **This requirement has never been stated in the file. It is stated now.**

⚠⚠ **D149's first live catch, recorded here because it decided the verdict**: MACRO §D-2 resolved
S49's invalidation clause by importing **S52-A's** standard. Under S52-A's bar (*a dated term in a
primary text*) the *"WITHOUT a Hormuz statement"* clause is **technically true**; under S49's own
eight-word clause (*"a Hormuz reopening statement"*) it is **arguably false** — the 08-02 Truth Social
post named the Strait's opening. **The gap between the two standards is exactly the width of the
decision.** ⇒ **A human ruling that S49's clause means what its words say would make this `VOID`.
The crack MEASUREMENT survives either ruling; only the score is at stake.**

## S50-ANNEX, second entry — ★★ 2026-08-04 (**S50 is STILL NOT RE-FROZEN**)

| Name | Implied move | Expiry | Covers the 08-04 print? | vs the 08-03 annex |
|---|---|---|---|---|
| **AMD** | **±8.2%** | **2026-08-05 (D1)** | ✅ **YES — event-priced for the FIRST time**, one session before the print | was **±6.4% / D0 / ❌** |
| **ANET** | **±10.7%** | 2026-08-07 (D3) | ✅ YES (second consecutive pull) | was **±11.7%** ⇒ **−1.0pp of band drift in ONE session** |

★ **What the annex requires at scoring, and nothing more**: record **each name's realised settled move
against its band as a SEPARATE, LABELLED reaction test** (the **D28** fix). **S50's branches remain a
DIRECTION test on the guide — a cut the tape buys still scores as a cut.**
⚠⚠ **The band is itself an estimator with error**: ANET's moved **11.7 → 10.7 in one session**, so the
reaction test must read *"realised vs ±10.7% **as pulled 2026-08-04**, band drift −1.0pp/session
observed."* **A reaction test quoted against an UNSTAMPED band is the same defect D140 fixed for
futures bars.**
⚠ **Positioning at this pull, recorded not scored**: **AMD P/C 0.99 (07-31) → 0.38 (08-03) → 2.18
(08-04), skew +13.0** — **a full round trip from hedged to complacent to maximally hedged in 48
hours**; **ANET P/C 0.11, skew +5.6** (the most one-sided book in the pull); MPC ±8.0% / exp 08-21
(D17), P/C 0.44, skew +27.8 — **±9.4% (07-30) → ±8.9% (08-03) → ±8.0% (08-04), three pulls, monotone
compression, each stamped with its pull date.**
★ **The AMD P/C path is this annex's most useful fact and it belongs here rather than in a branch:
S50's registration described AMD as "already hedging downside" at P/C 0.99. It is now 2.18. Any
post-print claim that "positioning was complacent" is falsified by this record.**
⚠⚠ **Explicitly NOT permitted: adding a magnitude leg to S50's branch A or B. Both prints land
tonight; a threshold introduced after the window opened is a description wearing a forecast's
clothes. The annex exists precisely so the new information is preserved without paying that price.**

## Brackets considered and DROPPED 2026-08-04, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **CPI 2026-08-12** | **S9 already owns the real-rate transmission** and sits **8bp** from its 2.55 kill line (DFII10 2.47). A second row on the same print duplicates. |
| **A VIX-regime bracket** | VIX **20.66 (07-29) → 15.86 (08-03) = −23% in three sessions** is **context for every bracket above; no branch changes a sector conclusion.** ⚠ And **R3 binds**: *"low VIX implies 20d underperformance"* is a **KR-measured result whose US replication FAILED** — it may not be cited. Logged, not registered. |
| **CEG 08-06 / VST 08-07 standalone** | **Owned by S35 / S47 (both → 08-07) and S24 / S40.** A fourth row on the same print double-counts. ★ The under-computed *sub-leg* was addressed with a **DEEP promotion** instead, which is the right instrument. |
| **LNG 08-06** | The 2026-07-31 drop **still holds on L3** — neither branch changes a DEEP conclusion. ★ **Logged as a CONTROL observation rather than dropped silently**: LNG is the only Energy name in the window whose thesis is not crack-driven, so it is the control for whether ENRG OW− is a *crack* call or a *sector* call. Newly computed this run: **LNG RS20 +4.0 / RS60 −4.5 vs SPY** — and ⚠ **LNG is not in `us_top300`, so it has no flow row (M252/M287, 6th run).** |
| **A second Financials row** | **S51 (NFP 08-07) already owns the flattener.** ★ **What was registered instead is a QUALIFIER, not a row**: if at the settled 08-07 close **2s10s ≥ +0.35 AND DGS2 has fallen ≥15bp from 4.28**, the run is flagged **`S51-A-BULL`** — S51 branch A firing on a **bull** steepener, the tape that breaks FIN OW− anyway. **S51 is NOT re-frozen; this is a reading instruction for its scorer.** |


## S58 — ★★★ MET 2026-08-06 프린트: 브래킷 없이 들어간 바이너리를 사후 등록한다 · ARMED · → 2026-08-11

Registered **2026-08-05 by the human-execution loop** (not by a pipeline stage).

**왜 존재하나 — 그리고 이 브래킷의 등록 사유 자체가 규칙 위반의 기록이다.**
**2026-08-04 KIS 실계좌에서 MET 7주가 매수 체결됐다.** 그 시점에 MET 의 Q2 프린트는 **08-05 장마감 후**로
확정돼 있었고(`[nasdaq 08-03 본문]` 컨센 EPS $2.30 · 매출 $19.34bn · 60일간 상향 6 / 하향 0),
**어떤 브래킷도 이 바이너리를 소유하지 않았다.** PREMORTEM §2 의 규칙은 *"a one-way tilt into a known
binary is a protocol violation"* 이다. ⇒ **위반은 되돌릴 수 없으므로 채점 가능하게 만든다.**

**매수의 근거는 유효했고 그대로 기록한다**(BET_SHEET 2026-08-04 §B-FRESHNESS): **EXT-BUT-LIVE
(RS60 +17.6 vs SPY, share 32.0%, days-21-60 segment +11.1)** · **FINRA short-vol z −1.55 ✅ clean-rise**
· **level-dominant (b_lvl 9.11 vs b_slp 17.28 — DEEP-FIN §2c)**.
⚠ **B2 경고도 그대로 붙어 있다**: fwd 8.67× on a 0.51 PEG with **forward EPS 2.1× trailing** —
*"a low multiple whose denominator is racing upward is consensus CHASING, not cheapness."*

**밴드는 실측 분포에서 뽑았다(D93 — 라운드 넘버 금지).** 관측치 = **MET 3-session excess vs SPY**,
trailing-252 일별 겹침창: **mean +0.130 · sd 2.247 · q10 −2.695 · q85 +2.453.**
⚠ **추정량의 중심이 0 이 아니라 +0.130 이므로 대칭밴드는 A 쪽으로 편향된다** — S55 가 처음 잡아낸 그
편향의 **네 번째 재현**이고, 그래서 A 를 q85 에, B 를 q10 에 둔다(대칭이 아니라 동일 기저율 근처).

| Branch | Observable (settled) | Meaning |
|---|---|---|
| **A (테제 유지)** | 프린트 후 첫 3 정산세션 누적 **excess vs SPY ≥ +2.45pp** (기저율 15%) | level-dominant 보험 테제가 프린트로 확인. **M363 의 "금리는 은행이 아니라 다른 데로 간다"가 이름 단위로 살아난다** |
| **B (테제 파손)** | **≤ −2.70pp** (기저율 10%) | **B2 경고가 맞았다** — 상향 6/하향 0 은 이미 가격에 있었고 낮은 배수는 달리는 분모였다. ⇒ 거부원장에 `H.밸류소진` 으로 편입 |
| **C (모달, 75%)** | 그 사이 | 프린트는 정보를 주지 않았다. **바이너리에 단방향으로 들어간 대가는 「몰라도 되는 걸 알기 위해 리스크를 졌다」로 기록된다** |

⚠ **이 행은 매매를 정당화하지 않는다. 채점 가능하게만 만든다.** 창: **2026-08-11 정산 종료.**

## S59 — ★★ NDAQ: DEEP-FIN 이 회귀로 지목했지만 관측치를 등록하지 않은 메커니즘 · ARMED · → 2026-08-12

Registered **2026-08-05 by the human-execution loop.**

**왜 존재하나.** **DEEP-FIN §2a 는 은행 9종 + KRE + XLF 전부 `|t| ≤ 1.5, R² ≤ 0.05` 로 금리 전달이
없음을 측정했고**(M363), 유의한 로더로 **NDAQ b_slp +33.2 (t +3.4), slope-dominant 3.4×** 를 지목했다.
그리고 **BET_SHEET 는 NDAQ 를 "the cleanest expression of a mechanism the desk has NOT registered an
observable for" 라고 명시적으로 적었다.** ⇒ **2026-08-04 에 NDAQ 7주를 샀으므로 그 관측치를 지금 만든다.**

**벤치를 SPY 가 아니라 XLF 로 두는 것이 이 행의 요점이다** — 주장은 "NDAQ 가 오른다"가 아니라
**"기울기 노출이 섹터 내에서 차별적으로 보상된다"** 이므로, 시장베타를 빼야 주장이 검정된다(C5 —
벤치 선택은 임의이고 그렇게 밝힌다).

**밴드 실측**(NDAQ − XLF, 10-session 겹침창, trailing-252): **mean −0.159 · sd 5.616 · q15 −5.165 ·
q85 +4.425.**

| Branch | Observable (settled, → 2026-08-12) | Meaning |
|---|---|---|
| **A (메커니즘 확인)** | **NDAQ − XLF 10세션 누적 ≥ +4.43pp** (기저율 15%) **AND** 같은 창에서 **derived 2s10s 가 상승** | 회귀의 β 가 표본 밖에서 살아남았다. **M363 의 "전달은 거래소·마켓데이터로 간다"가 예측력을 얻는다** |
| **B (in-sample 잡음)** | **≤ −5.17pp** (기저율 15%) **AND** 2s10s 상승 | **기울기가 올랐는데 slope-dominant 이름이 섹터에 졌다** ⇒ β +33.2 은 60일 표본 안의 우연. **S4(in-sample ≠ done) 가 발화** |
| **C** | 그 사이, 또는 2s10s 가 하락해 조건 자체가 성립 안 함 | 판정 불가. ⚠ **2s10s 방향이 조건에 들어가므로 C 가 잦을 것** — 그건 결함이 아니라 이 메커니즘이 조건부라는 사실이다 |

⚠ **NFP 08-07 · CPI 08-12 가 창 안에 있다.** ⚠ **NDAQ 자체 실적은 2026-10-22 — 창 밖(근접 바이너리 0).**

## S60 — ★★ XLE 매도의 반증조건 — 이 데스크에 **집행 채점 원장이 없다**는 사실의 대리물 · ARMED · → 2026-08-11

Registered **2026-08-05 by the human-execution loop.**

**왜 존재하나.** **2026-08-04 XLE 10주를 전량 매도했다.** 근거는 넷 다 구조적이었다:
(1) **`us_top300` 밖 — flow·RS·숏 어느 축도 존재하지 않는다** (2) **사이클 레지스트리 미태그 — 어떤
floor 도 이 4.65% 를 보지 못한다** (3) **DEEP-ENRG §5 실측: XLE RS60 +0.37 on a days-21-60 segment of
−9.43 ⇒ "board's best exc20d 는 구멍 메우기"** (4) **MPC·LNG 와 합쳐 에너지 노출 13.28% 중복.**

⚠⚠ **그런데 이 데스크에는 매도를 채점할 원장이 없다.** `reject_ledger` 는 *사지 않은* 것을,
`missed_ledger` 는 *놓친* 것을 잰다. **판 것을 재는 칸이 없다** — 그래서 이 행이 그 대리물이다(**D159**).

**밴드 실측**(XLE − SPY, 5-session 겹침창, trailing-252): **mean +0.332 · sd 3.757 · q10 −5.049 ·
q85 +3.902.** ⚠ **중심이 +0.332 로 양수** — 매도를 채점하는 행이 구조적으로 A(매도가 틀림) 쪽으로
기운다는 뜻이고, **그 편향을 등록 시점에 밝힌다.**

| Branch | Observable (2026-08-04 정산 → 2026-08-11 정산) | Meaning |
|---|---|---|
| **A (매도가 틀렸다)** | **XLE 5세션 excess vs SPY ≥ +3.90pp** (기저율 15%) | 통합석유 복합체가 재평가됐다 ⇒ **"denominator artifact" 독법이 틀렸고**, 측정 불가를 매도 사유로 쓴 것이 손실이었다 |
| **B (매도가 맞았다)** | **≤ −5.05pp** (기저율 10%) | 호르무즈 재개방 리프라이싱이 통합주를 때렸다 ⇒ 구조적 근거가 결과로 확인 |
| **C (모달)** | 그 사이 | ⚠ **가장 정직한 결과: 매도는 알파가 아니라 「측정 가능한 것만 보유한다」는 방침이었다.** C 면 방침으로만 남고 성과 주장은 하지 않는다 |

⚠ **매도 시점 맥락, 등록 시 기록**: 08-04 장중 호르무즈 딜 헤드라인이 쏟아지는 중이었다 —
`Trump Tells Iran He Wants a Deal on Hormuz Agreed Imminently` [bloomberg] · `Bessent Suggests
US-Iran Hormuz Deal Possible in Coming Days` [bloomberg] · `Futures Hit Record High As Oil Tumbles`
[zerohedge]. **전부 [제목만] = D6 C급, 방향만.** 반대증거 동일세션: `Saudi Aramco CEO Warns Hormuz
Closure Removes 100 Million Barrels A Week`. **S52-A(1차문서에 날짜 박힌 개방 문구)는 미발화.**
⇒ **헤드라인 하락에 판 것이며, 그 사실이 A/B 판정을 오염시킬 수 있다(C4).**

## S61 — ★★ The Red Sea / tanker war-risk premium: the leg the Iran-scoped brackets cannot reach · ARMED · → 2026-08-12

Registered **2026-08-05 by the `industry_US` PREMORTEM (Lens 2)**. **IDs checked at WRITE time
against every row in all three `SCENARIOS*.md`, both `STANDING_VIEW*.md` and `RESEARCH.md`
(D137 / D76 / M319): highest existing was S60 (US) / S52-KR (KR).**

**Why it exists.** **S8 · S52 · S55 are all scoped to IRAN** — Hormuz text, Iranian energy
infrastructure, the distillate leg. **`D168` was registered this run because a Houthi ballistic
strike on a SAUDI oil TANKER in the Red Sea fires none of them**, while transmitting to the same
crude and freight variables. EVENT_ALPHA Card 3 named the gap and **froze no market observable** —
this row supplies one.
⚠ The object was **corrected inside this run**: `MACRO §C-2` wrote *"facility"*; the body-read
returned **tanker**. ⇒ **the transmission is FREIGHT and war-risk premium, not production capacity**,
and the observable is built on tankers accordingly.

| Branch | Frozen observable (5-session cumulative excess, **settled closes**) | Meaning |
|---|---|---|
| **A (fills D168)** | equal-weight **{STNG, FRO}** vs **SPY** ≥ **+6.80pp** at ANY settled close through 2026-08-12 | Tankers price a war-risk premium the Iran-scoped brackets cannot see ⇒ **D168 escalates from documented to active**, and S8/S52/S55's Iran-only framing must widen to a Middle-East-wide risk premium |
| **B** | ≤ **−4.19pp** at the **2026-08-12** settled close | No premium appears; EVENT_ALPHA Card 3's STORY-ONLY tag holds and **D168 stays named-but-inert** |
| **C** | between | No conclusion changes |

- **Frozen observable**: `STNG` and `FRO`, equal-weight, 5-session cumulative excess vs **SPY**
  inline (C1), yfinance, `auto_adjust=False`, **settled daily closes only, never mixed with
  intraday**; window **2026-08-05 → 2026-08-12**.
- ★ **D93 executed BEFORE freezing.** Trailing **252** settled sessions: **mean +1.09pp · sd 5.81pp**
  ⇒ ⚠⚠ **the estimator is NOT centred on zero** — a symmetric band around 0 would be biased by
  construction. **This is the 5th independent reproduction of that bias on this desk** (S55, S57,
  S58, S60 were the first four). Bands taken at the measured tails: **A ≥ +6.80 (85th pct) ·
  B ≤ −4.19 (15th pct) · C ≈ 70% modal.**
- **State at registration**: **−5.56pp (2026-08-04 settle)** ⇒ **already past branch B's line.**
  **Disclosed at registration rather than discovered afterwards** — branch A is the adversarial ask.
- **Implied moves**: **STNG ±7.6% · FRO ±9.3%, both expiry 2026-08-21 (D16)**. ⚠ **These price
  single names, NOT the basket-vs-SPY spread this bracket scores** ⇒ recorded as context and
  **explicitly NOT used to set the threshold** (the D28 separation).
- **Information content (L3): MEDIUM, and stated as medium rather than inflated.** Branch A widens
  three brackets' scope; branch B keeps D168 inert. **Neither overturns the ENRG core (S49/S55).**
- ⚠⚠ **Instrument disclosure: STNG and FRO are OUTSIDE `us_top300`** (M45/M252's gap) ⇒ **no flow
  tag, no RS tag, no FINRA short row exists for either**, and this bracket is scored on a
  hand-built price series. **Stated at registration, not discovered at scoring.**
- **Invalidation (D149 standard)**: a **name-specific** event at STNG or FRO — M&A, a dividend cut,
  a fleet sale — evidenced by a company filing or two independent outlets on the same primary event
  ⇒ the basket stops measuring war-risk ⇒ **VOID, not scored.**

## S62 — ★★★ Are INDU OW− and UTIL UW one bet wearing two GICS labels? · ARMED · → 2026-08-07

Registered **2026-08-05 by the `industry_US` PREMORTEM (Lens 2)**, **against this run's own
ROTATION**, hours after that stage promoted INDU and re-confirmed UTIL. **IDs checked at WRITE time
as above.**

**Why it exists.** `SECTOR_ROTATION` wrote **INDU `N → OW−`** on a breadth reading carried by
**ETN · EMR · AME · PWR**, and **UTIL `UW`** on XLU being the worst sector on the board — **and gave
BOTH a DEEP slot.** EVENT_ALPHA Card 6 called the pair *"a single-cycle, two-sub-sector inversion"*
with **an IF/ELSE but no bands, no settle date and no options check.** ⇒ **the desk is carrying one
AI-power capex rotation as two independent sector convictions.** This is the L1's own field-note
pattern (*"two sectors that are one bet in disguise"*), appearing as an **OW/UW** pair rather than
the measured UW/UW precedent (RE+DISC).

| Branch | Frozen observable (settled closes, bench **SPY** inline) | Meaning |
|---|---|---|
| **A (the correlated tilt COLLAPSES)** | (median RS20 of {EMR, ETN, AME, PWR}) − (XLU RS20) ≤ **−5.9pp** at the **2026-08-07** settle | **Convergence: UTIL's "worst sector" tag and INDU's electrical-led promotion were one week's rotation counted twice.** ⇒ the two tilts are **ONE exposure** and must be sized as one |
| **B (the split is DURABLE)** | that spread stays ≥ **+7.4pp** at the 2026-08-07 settle | The bifurcation survives a second session **including the CEG (08-06) and VST (08-07) prints** ⇒ still one cycle mechanically, but **two defensible convictions** |
| **C** | −5.9 to +7.4 | No conclusion changes |

- ★ **D93 executed BEFORE freezing.** Trailing **252** settled sessions of the same spread:
  **mean +0.66pp · sd 6.05pp** ⇒ ⚠ **again not centred on zero.** Bands at the measured tails:
  **A ≤ −5.91 (15th pct) · B ≥ +7.42 (85th pct).**
- **State at registration**: **+14.51pp (2026-08-04 settle)** — **already BEYOND the 85th-percentile
  tail**, i.e. **branch A is the genuinely adversarial ask and branch B is the status quo.**
  Legs: **EMR +12.0 · ETN +9.2 · AME +6.5 · PWR +2.4** vs **XLU −6.6**, all RS20 vs SPY.
- ★★ **Implied moves, 2026-08-07 expiries (D2): EMR ±3.0% · ETN ±3.4% · XLU ±2.0%.** **Both
  thresholds sit OUTSIDE every single-name implied move on the settle date**, so **firing requires
  correlated multi-name movement rather than one option's noise.** **That is why the bands are where
  they are, and it is stated rather than left implicit.**
- **Information content (L3): HIGH and SYMMETRIC.** **It converts a question this run left open in
  two DEEP mandates into a frozen falsifier.** Branch A forces a re-size of two live tilts; branch B
  is the first fresh confirmation that the label split is real.
- ⚠ **Carried caveat, from Lens 3 the same day**: **all four INDU names have a NEGATIVE days-21-60
  segment vs SPY** (EMR −4.5 · ETN −3.1 · AME −3.5 · PWR −14.7) ⇒ the leg this spread is long is a
  **20-day repair, not a run.** **This does not move the threshold** (frozen is frozen) — it is
  recorded so branch B cannot later be read as evidence of a durable cycle.
- **Invalidation (D149 standard)**: a **name-specific** one-off inside the window at any of the five
  objects — M&A, a rate-case ruling, a guidance withdrawal — evidenced by a filing or two
  independent outlets on the same primary event ⇒ the spread stops measuring the rotation ⇒ **VOID.**

## S63 — ★★★ Are UW Utilities + UW Real Estate + OW Financials ONE duration bet wearing three GICS labels? · ARMED · CPI 2026-08-12 → settle **2026-08-13**

Registered **2026-08-06 by the `industry_US` PREMORTEM (Lens 2)**, before the CPI print.
**ID checked against EVERY existing row in BOTH files (the D76 collision class); the highest existing
ID was S62 (US) / S53-KR (KR).**

**The gap it fills, and it is the correlated-tilt pattern the L1 tells this stage to hunt.**
This run **raised** the Utilities UW's conviction, **held** the Real Estate UW and **promoted**
Financials to **OW** — three separate rows in `SECTOR_ROTATION.md §1–2`, and **one mechanism.**
**S51 brackets only the FIN half, on one date, on 2s10s.** Nothing tests whether the three fail
together. The tape is already leaning that way: 2s10s flattened **three consecutive prints
(+0.47 → +0.45 → +0.43)**, `DFII10` **2.43 → 2.40**, `T10YIE` **2.27 → 2.23 → 2.22**, the last near
the bottom of a 2.18–2.50 365-day range. **A cool CPI takes all three tilts out on one tick.**

**Frozen observable**: `DUR = (XLU RS20 vs SPY + XLRE RS20 vs SPY) / 2 − XLF RS20 vs SPY`, on
**settled closes, yfinance, one source**, benchmark **SPY inline on all three legs (C1)**.
**State at registration (2026-08-05 settled): DUR = −6.197** (XLU **−7.02** · XLRE **−0.89** ·
XLF **+2.24**).

| Branch | Threshold at the **2026-08-13** settle | Meaning |
|---|---|---|
| **A (AGAINST US — hits three tilts at once)** | **DUR ≥ −3.3** | Rate-sensitives converge on Financials ⇒ **the three labels are ONE exposure and it was sized as three.** **Rips**: the XLU regulated complex (SO · DUK · D · AEP) and the XLRE duration names, while **JPM · BAC · WFC · BRK-B** lag |
| **B (with us)** | **DUR ≤ −9.2** | The divergence widens through the print ⇒ still one mechanism, but the desk's direction is right |
| **C** | −9.2 to −3.3 | ~70% of the measured distribution, modal, **no conclusion changes** |

- **D93 executed BEFORE freezing, and the bands come from the estimator's own measured sigma**:
  trailing-252 **6-session change** of `DUR` — mean **−0.15**, sd **2.88**, **p15 −3.01 / p85 +2.94**
  ⇒ the two lines sit at the measured 15th/85th percentiles of the change, **not at round numbers**.
  ⚠ The **level** distribution (252d mean −0.01, sd 4.83, p15 −4.72) already places the −6.197 anchor
  **below its own 15th percentile** — recorded so branch B cannot be read as a fresh extreme.
- **Implied-move check, stated rather than smuggled**: XLU **±0.9%**, XLF **±0.8%** (both expiry
  2026-08-07, **D1**). ⚠ **No XLRE straddle was pulled and none is fabricated (C3).** A ~2.9pp move
  in a three-ETF composite **cannot be produced by either available single implied move**, so both
  thresholds sit **outside** the priced noise. ✅
- **Information content (L3): HIGH and SYMMETRIC** — 15/15/70 measured base rates, and **branch A
  falsifies three live tilts simultaneously**, which is the highest-leverage branch this desk has
  registered since S49.
- **Invalidation (D149 standard — the clause carries the same evidentiary bar as the branches)**: a
  utility rate-case ruling, REIT M&A, or bank-specific guidance event inside the window, evidenced by
  **a filing or two independent outlets on the same primary event** ⇒ the spread stops measuring
  duration ⇒ **VOID**, not scored.
- ⚠ **Independently re-derived at registration (D5)**: the three RS20 legs reproduce
  `MACRO_REPORT.md §D` exactly (XLU −7.02 · XLRE −0.89 · XLF +2.24), on settled bars only.
  ⚠⚠ **The first verification pass accidentally included the LIVE 2026-08-06 partial bar and read
  DUR −5.336; pinning to the 08-05 settle gave −6.197. The 0.86-point gap is D74 and is recorded
  here because it would have moved the anchor.**

## S64 — ★★ Do N+ Energy and OW− Industrials take the SAME crude tick in opposite directions? · ARMED · → settle **2026-08-13**

Registered **2026-08-06 by the `industry_US` PREMORTEM (Lens 2)**.

**The gap it fills.** `MACRO_REPORT.md §G` row 7 states the mechanism for the Industrials OW− — a
crude fall is a direct input-cost tailwind (**M91**) — **and records that it did not transmit**:
across a **12%+ crude drawdown**, XLI printed **exc5 −0.04 / exc20 +0.01 vs SPY, the flattest sector
on the board on both windows.** The desk wrote the falsifier into its own matrix and did not test it.
**This bracket buys observation #2**, so the pair is not carried as two ideas when one leg has never
paid.

**Frozen observable**: **XLI 6-session excess return vs SPY**, **2026-08-05 settle → 2026-08-13
settle** — a **FORWARD** window. ⚠⚠ **Stated explicitly to avoid D122** (a bracket whose condition is
already true on its own registration bar): the **trailing** 6-session excess at registration is
**−1.790**, which sits exactly on branch A's line. **That value is NOT the observable.** The
observable is the forward window and nothing about it is settled yet.

| Branch | Threshold at the **2026-08-13** settle | Meaning |
|---|---|---|
| **A (AGAINST US)** | XLI forward-6-session excess vs SPY **≤ −1.8pp** | Crude fell again, Energy took the revenue hit, and Industrials **still** did not convert the fuel tailwind ⇒ **M91's leg is falsified on a second observation**, the pair is ONE crude short with a single payoff leg, and **OW− INDU loses the mechanism §G names for it** |
| **B (with us)** | **≥ +1.9pp** | The tailwind transmits ⇒ Industrials is a genuine second bet, not the other side of the Energy tick |
| **C** | −1.8 to +1.9 | ~70%, no conclusion changes |

- **D93**: trailing-252 6-session excess — mean **+0.01**, sd **1.79**, **p15 −1.79 / p85 +1.88**.
  Bands taken from the measured tails.
- **Mandatory companion, quoted but NOT frozen (C2 — both halves)**: **XLE's 6-session excess vs SPY
  over the identical window.** At registration XLE reads **−4.357** against XLI's **−1.790**, with
  **WTI 75.22**. The pair is never reported as one number.
- **Implied-move check, stated precisely**: XLI **±1.7%**, XLE **±2.1%** (both D1) price **absolute**
  paths; **the observable is XLI MINUS SPY, for which no straddle exists (C3).** The bands are
  therefore set on the measured SPY-relative distribution and **the implied move is explicitly not
  used as the reference.**
- **Information content (L3): MEDIUM-HIGH and ASYMMETRIC** — **A falsifies** the Industrials
  mechanism; **B can only confirm**, because a 6-session sector-relative gain has many causes other
  than fuel. Registered because the falsifying branch is the one the desk lacks.
- **VOID condition, and it is the important one**: **WTI settled 2026-08-13 ≥ 75.22** (the 08-05
  base) ⇒ **the discriminating tick never arrived and the mechanism was never tested. Do not score
  it.** Also VOID on named INDU M&A or a guidance withdrawal inside the window.
- ⚠ **COP · TRGP · CNQ printed 2026-08-06 pre-market with no bracket owning them** — the calendar
  miss registered as a dig this run. They are folded in as **Energy-leg context here**, deliberately
  **not** given their own row (neither branch of a single E&P print changes a conclusion).

## S65 — ★★★ Financials was promoted OW− → OW **today** on breadth that decomposes to a news count · ARMED · NFP 2026-08-07 → settle **2026-08-11**

Registered **2026-08-06 by the `industry_US` PREMORTEM (Lens 2)**, hours after the promotion and
before the binary.

**The gap it fills, and it is this run's own tilt change.** `SECTOR_ROTATION.md §2` promoted FIN to
**OW** carried by **rank-1 on both flow axes (wflow +0.317 · eqflow +0.190), breadth 0.15 — the
highest of 11 — and 5 new-🟢.** `SWEEP_READ.md §2` measured, in the same run, that **four of those
five (JPM 0.72 · BAC 0.74 · WFC 0.83 · BRK-B 0.85) are VELOCITY-lit greens with `vol_surge` below
1.2** — a news-count ignition, not a money ignition — and **M173 records that BRK-B alone is 13.94%
of sector cap.** **S51 brackets the rate mechanism (2s10s); nothing brackets the evidence that
actually moved the tilt.** A tilt upgraded on an axis with no falsifier is the one-way bet this
stage exists to stop.

**Frozen observable**: **median RS20 vs SPY of {JPM, BAC, WFC, BRK-B}**, settled closes, benchmark
**SPY inline (C1)**. **State at registration (2026-08-05 settled): +3.405** (JPM **+5.38** ·
BAC **+5.22** · WFC **+0.95** · BRK-B **+1.59**).

| Branch | Threshold at the **2026-08-11** settle | Meaning |
|---|---|---|
| **A (AGAINST US)** | median **≤ +0.34** | The velocity-only greens fail to hold their lead through the binary ⇒ **the breadth that carried today's promotion was a news count** ⇒ FIN reverts to **at most OW−** — and with **P13‴ flattening three consecutive prints**, to nothing |
| **B (with us)** | median **≥ +6.81** | Velocity converted into price **through** the print ⇒ the promotion is validated on the very axis it was made on |
| **C** | +0.34 to +6.81 | ~70%, no conclusion changes |

- **D93, and a within-run CORRECTION of the lens that proposed it**: Lens 2 sized the bands off a
  **3-session** change distribution (sd 2.86) while the window **08-05 → 08-11 is 4 sessions**
  (08-06 · 08-07 · 08-10 · 08-11). Re-measured on the correct horizon: trailing-252 **4-session**
  change of the median — mean **+0.11**, sd **3.44**, **p15 −3.06 / p85 +3.41** ⇒ **A ≤ +0.34** and
  **B ≥ +6.81**, both wider than the lens proposed. **The horizon mismatch is recorded rather than
  silently fixed.**
- **Companion diagnostic, quoted but NOT frozen** (it is DEEP-FIN's own mandate question): the same
  median **excluding BRK-B** reads **+5.219** at registration vs **+3.405** with it ⇒ **BRK-B is
  DRAGGING the median, not carrying it.** Recorded now so branch B cannot later be read as breadth
  if one 13.94%-of-cap name moved it, **and so branch A cannot be blamed on BRK-B either.**
- **Implied-move check**: **JPM ±1.2%**, **XLF ±0.8%** (both expiry 2026-08-07, D1). Over a
  4-session window a **±3.1pp move in a four-name median requires correlated bank movement**, which
  is outside any single name's straddle. ✅ Both thresholds carry information.
- **Information content (L3): HIGH and SYMMETRIC.** It converts today's promotion from an assertion
  into a falsifier **on the exact axis the promotion was made**.
- **Invalidation (D149 standard)**: bank M&A, a Fed capital-rule announcement, or a BRK-B-specific
  disclosure inside the window, evidenced by a filing or two independent outlets ⇒ **VOID.**

## S66 — ★★★ The BULL-steepener-with-credit-fear leg S51's own text refuses to score · ARMED · NFP 2026-08-07 → settle at the first `[FRED]` close covering 08-07 (expect **2026-08-10**)

Registered **2026-08-07 by the `industry_US` PREMORTEM (Lens 2, with a horizon correction applied at
registration)**, hours after the print and **before any settled FRED close contains it.**
**IDs checked at WRITE time against EVERY row in BOTH files (the D76 collision class); highest existing
was S65 (US) / S55-KR (KR).**

**The gap it fills.** **S51** (registered 07-31, → 08-10) brackets the bear-steepener/NIM leg on
derived 2s10s, and **its own registration text disclaims the other leg verbatim**: *"a >20bp front-end
**rally** would be a bull steepener with recession/credit fear — 2s10s could widen while FIN still
suffers. **That is NOT scored here.**"* A soft `S51-A-BULL` reading flag added 08-04 is **a tag, not a
scored branch with tickers, a trigger and an invalidation**, and today's MACRO **P29** is a proposition,
not a frozen row. ⇒ **nothing owned this leg, and today's print is exactly its case.**

**The event, both halves (C2).** July NFP **−23,000 against a +83,000 consensus** `[cnbc body]`;
**unemployment 4.1%, DOWN from 4.2%** `[bloomberg · wsj · marketwatch · investing_en]` — the rate fell
because the denominator shrank (**720,000 left the workforce in June**, `[guardian body]`), not because
the labour market strengthened; **prior two months revised down 74,000.** Regime: the FOMC **held
3.50–3.75% on 07-29 with THREE hike dissents**; CME September **hike** odds fell **67% → 56%**; Gov.
Cook, on record 08-05, would support a hike absent inflation improvement; June inflation 3.5%
annualised. ⇒ **a weak print is DOVISH here and its curve signature is a front-end rally.**

**Frozen observable**: `ΔDGS2` = `DGS2`(settle) − **4.18** and `ΔHY OAS` = `BAMLH0A0HYM2`(settle) −
**2.75**, both `[FRED]`, both anchored on the **2026-08-05** print (the last pre-NFP close), read at the
first settled close that covers 2026-08-07. **S51's 2s10s is NOT re-frozen and is not part of this row.**

| Branch | Threshold | Meaning |
|---|---|---|
| **A (against us — the full growth-scare signature)** | `ΔDGS2` ≤ **−0.15** **AND** `ΔHY OAS` ≥ **+0.15** | A front-end rally **with** a credit-spread break is a growth scare, not a NIM tailwind — **regardless of whether 2s10s itself clears S51's +0.35 bar.** **FIN loses the mechanism** (credit losses beat NIM), **ENRG loses it** (demand destruction), **INDU loses cyclical support** — and the regime-flip half: **UTIL UW and RE UW are wrong-footed by a duration/safety bid** |
| **A′ (against us — PARTIAL, and this branch is why the row is scoreable)** | **exactly ONE** leg clears its own measured tail: `ΔDGS2` ≤ **−0.12** xor `ΔHY OAS` ≥ **+0.14** | **The firing leg is named and the verdict is graded PARTIAL.** Front-end-only ⇒ dovish repricing without credit confirmation. Credit-only ⇒ spread stress without a policy bid |
| **B (with us)** | `ΔDGS2` > **−0.05** **AND** `ΔHY OAS` < **+0.08** | Neither leg moves ⇒ **S51 branch A's *"NIM thesis intact"* reading is genuinely usable without S51's own caveat firing** |
| **C** | anything else | No conclusion changes |

- ★ **D93 executed on a LIKE-FOR-LIKE horizon, and the correction is recorded.** Lens 2 proposed these
  thresholds citing a **1-day** base rate for the DGS2 leg (0.37%) beside a **2-day** rate for HY OAS
  (4.55%), while the observable is a **2-session** change from the 08-05 anchor. **Re-measured on the
  same 2-session horizon**: `DGS2` **n=613**, sd 0.0742, **≤ −0.15 fires in 2.12%**, p05 **−0.12**;
  `hy_oas` **n=645**, sd 0.1050, **≥ +0.15 fires in 4.34%**, p95 **+0.14**.
- ⚠⚠ **Branch A is therefore a sub-1% conjunction and is PRE-DECLARED as such** — which is exactly why
  **A′ exists.** **This is the first bracket on this desk written to close the S31 branch-hole class by
  construction: the four branches exhaustively partition the observable's range.**
- **Starter lists, `asof 2026-08-06 settled`, bench SPY inline.** **A rips against**: JPM **+4.0/+14.8**
  · BAC **+4.1/+20.7** · WFC **−1.5/+15.1** · GS **−4.5/+5.3** · XOM **+10.4/−0.5** · CVX **+6.5/−1.5**
  · EMR **+11.6/+8.6** · CAT **−10.9/−11.5**. **A rips FOR (against the UWs)**: NEE **−5.1/−14.8** · SO
  **−4.6/−4.2** · DUK **−3.3/−4.8** · D **−6.1/+2.8** · PLD **−3.8/−7.4** · WELL **−0.6/+5.9** · AMT
  **+1.5/−7.5**.
- ⚠ **No implied move is used and none is fabricated** — a macro observable, the S9/S51 treatment.
- ⚠ **C3 stated at registration**: today's levels (`DGS2` 4.18, HY OAS 2.75) are **asof 08-05 and do NOT
  contain the NFP reaction.** Which branch is live is **`unknown`**, not benign — the desk has **zero**
  settled information on this question as of registration.
- **Information content (L3): HIGH and symmetric.** The only row on the board that can flip
  **FIN/ENRG/INDU and UTIL/RE simultaneously on one print.**
- **Invalidation (D149 standard)**: a bank-specific credit event (a downgrade or provision surprise
  evidenced by a filing or two independent outlets) inside the window ⇒ **VOID**, re-register.

## S67 — ★★★ Was this run's own ENRG N+ → OW− promotion right, on the leg the desk says holds the money? · ARMED · → settle **2026-08-13**

Registered **2026-08-07 by the `industry_US` PREMORTEM**, **against this run's own ROTATION**, hours
after that stage promoted Energy. IDs checked at WRITE time as above.

**Why it exists.** ROTATION moved **ENRG N+ → OW−** on flow (rank 1 on both axes, **eqflow +0.209**
positive for the first time since the downgrade, **Δ +0.196** against **−0.129 = last of 11** the day
before). **R51 had already retracted the ORIGINAL downgrade reason** (the wflow/eqflow gap = an
arithmetic identity) and replaced it with *"the informative number is Δ −0.129, and it is the refiners'
own."* **That replacement metric has now reversed sign in one session** — so the desk has moved this
sector twice in two runs on the same number pointing opposite ways, and **no row tests it.**
★ **And PREMORTEM found the promotion is NOT n=1**: reconstructed from `llm_outputs/sector_flow/history.json`,
**Energy's eqflow is positive on 13 of 16 sessions (81%), mean +0.1829**, and the **08-05 −0.055 the
downgrade rested on is one of only THREE negatives in sixteen.** The bracket is registered anyway.

**Frozen observable**: **median RS20 vs SPY of {MPC, VLO, PSX}**, settled closes, benchmark **SPY**
inline. **State at registration (2026-08-06 settled): +5.488** (MPC **+3.4** · VLO **+5.5** · PSX
**+6.0**). ⚠ **XOM and CVX are deliberately EXCLUDED** — they are the sector's only two 🟢 and both are
**velocity-lit with `vol_surge` 0.85 / 1.02 and RS60 ≈ 0**, i.e. the crowded layer by the desk's own
read; the promotion's stated carrier is the refiners' delta, so the refiners are the observable.

| Branch | Threshold at the 2026-08-13 settle | Meaning |
|---|---|---|
| **A (AGAINST US — falsifies a verdict this run just made)** | median **≤ −2.20** | **The promotion was a one-session bounce on the day WTI rose 2.75%.** ENRG reverts to at most N+, and the desk has now moved this sector on the same metric in both directions inside three runs — a **registration** failure, not a market one |
| **B (with us)** | median **≥ +13.56** | The refiners' money leg extends **through** the window ⇒ the promotion is validated on the exact leg it was made on, and the export-drain object (MACRO §0-c) has an equity expression |
| **C** | −2.20 to +13.56 | ~70%. No conclusion changes |

- ★ **D93 executed BEFORE freezing.** Trailing-**252** **5-session** change of the same median: **mean
  +0.314 · sd 7.577 · p15 −7.689 · p85 +8.075** ⇒ bands set at the measured tails from the current
  level (5.488 − 7.689 and 5.488 + 8.075). ⚠ **Not centred on zero** — stated.
- ⚠ **No implied move covers a three-name median** — stated, not manufactured. Single-name straddles
  measured today for context only: **MPC ±7.1% (expiry 2026-08-21, D14)** · VLO ±1.8% · PSX ±2.1%
  (both **D0, expiring 08-07** ⇒ they do **not** price a 08-13 settle).
- ⚠ **The estimate axis points the OTHER way from the promotion and is recorded at registration (C2):**
  MPC's current-quarter consensus is **+130.4% / 90d on 14↑/1↓ (30d)**, VLO **+77.3%** on 12↑/1↓, PSX
  **+72.3%** on 14↑/1↓ — **while mean-target upside is only +8.1% / +5.2% / +5.8%.** ⇒ **the earnings
  surge is already arbitraged into the targets (consensus chasing, lens L2).** **Branch B firing would
  therefore not establish cheapness**, and **`margin_history` is blank on all three (M233) so the margin
  percentile is `unknown` (C3) and no cheapness claim is made either way.**
- **Information content (L3): HIGH, asymmetric in the useful direction — branch A falsifies this run's
  own verdict.**
- **Invalidation (D149 standard)**: a refinery-specific one-off at any of the three (an unplanned
  outage, an acquisition, a guidance withdrawal) evidenced by a filing or two independent outlets on the
  same primary event ⇒ the median stops measuring the sector ⇒ **VOID**.

## S68 — ★★★ Is the COMM UW → UW− promotion money broadening, or a revision mirage? · ARMED · → settle **2026-08-13**

Registered **2026-08-07 by the `industry_US` PREMORTEM**, **against this run's own ROTATION**, on an
axis the promotion did not use. IDs checked at WRITE time as above.

**Why it exists.** ROTATION promoted **COMM UW → UW−** on flow: **eqflow +0.136 EXCEEDS wflow +0.058**
(breadth-led), **breadth 0.150 = 2nd of 11**, and **2🟢 of 13 — both `new_green` (DIS, EA), 40% of the
board's five fresh ignitions.** **PREMORTEM then measured the revision books of the two carriers and
they are both deteriorating**: **DIS CQ −4.1% / NQ −2.9% / 90d with current-year breadth 1↑ / 7↓ over
30 days**; **EA's current-year consensus fell 5.58 → 4.82 in SEVEN days = −13.6%** with CY breadth
0↑/1↓ (⚠ its 90-day column reads 0.00 ⇒ **`unknown`, C3**).
⇒ **the flow axis and the A-grade revision axis disagree about the same two names.** ROTATION's notch
**stands with its meaning narrowed** (COMM's eqflow **+0.1363 is the 2nd-highest of 17 sessions against
a series mean of +0.0108** and has risen two sessions, so the carrier is not a one-day artifact — the
R49/R50/R51/R52 class does not apply); **this row is what makes the narrowing falsifiable.**

**Frozen observables — TWO legs, scored INDEPENDENTLY so one contaminated leg cannot void the other**
(the S52-KR construction):
- **leg (i)**: **median RS20 vs SPY of {DIS, EA}**, settled closes, at the **2026-08-13** settle.
  **Registration: +2.943** (DIS **+6.6** · EA **+0.8**).
- **leg (ii)**: **DIS current-year revision breadth (30-day up:down) at 2026-08-13.**
  **Registration: 1↑ / 7↓.**

| Branch | Threshold | Meaning |
|---|---|---|
| **A (AGAINST US)** | leg (i) **≤ +0.29** **OR** leg (ii) **still net-negative** | **The promotion was a revision mirage**: money broadened into two names whose earnings were being cut. COMM reverts to **UW** and the notch is withdrawn |
| **B (with us)** | leg (i) **≥ +5.86** **AND** leg (ii) **turns net-positive** | **Money led the estimates** — the promotion is validated on both axes and the breadth read was early rather than wrong |
| **C** | split (one leg each way, or leg (i) in band with leg (ii) unchanged) | The narrowed meaning stands as written: **money is broadening; earnings are not turning** |

- ★ **D93 on leg (i)**: trailing-252 **5-session** change of the same median — **mean +0.056 · sd 3.186
  · p15 −2.656 · p85 +2.918** ⇒ bands at the measured tails from +2.943.
- ★ **leg (ii) is a COUNT test — no distribution is needed and none is invented (C5).**
- ⚠ **Implied moves DIS ±1.3% and EA ±0.2% are both D0 (expiry 2026-08-07)** ⇒ **they do not price a
  08-13 settle and are NOT used as thresholds.** Stated rather than borrowed.
- ⚠⚠ **Contamination named AT registration**: **TTWO printed pre-market 2026-08-07** in EA's own gaming
  node `[nasdaq body 08-06 pre-market list]`, and **EA's `vol_surge` 3.78 is the highest of any green on
  the board** — a volume event. **If EA's leg moves on a TTWO read-across rather than on its own
  business, leg (i) is measuring the node, not the name.** **No threshold is moved for this** — it is
  recorded so branch B cannot later be read as EA-specific.
- **Information content (L3): HIGH** — branch A falsifies this run's own promotion, and **leg (ii) tests
  it on the axis the promotion did not use.**
- **Invalidation (D149 standard)**: an M&A or major litigation event at DIS or EA inside the window
  evidenced by a filing or two independent outlets ⇒ **VOID** for the affected leg only.

## S69 — ★★ MET: a 🟢가속 flow tag against FALLING estimates · ARMED · → settle **2026-08-13**

Registered **2026-08-07 by the `industry_US` PREMORTEM (Lens 3's strongest desk disagreement,
verified).** IDs checked at WRITE time as above.

**Why it exists.** **MET is one of the desk's 27 greens** — 🟢가속, flow **+0.769**, RS20 **+7.4** /
RS60 **+24.2** vs SPY, `vol_surge` 1.23, OBV 매집 — and **its estimates are being cut**: full-year and
next-year consensus **−0.7% each over 90 days** with **revision breadth net-down on 3 of 4 horizons.**
★ **And the M149 decomposition says the RS60 is old money**: **d21-60 +15.2 vs RS20 +7.4** — the older
leg carries roughly two-thirds of it, with the recent leg decelerating rather than reversed (so **not**
the M429/PSX artifact pattern). ⇒ **the tag and the fundamental engine point opposite ways on a held-
sector green, and nothing tested it.**

**Frozen observable**: **MET RS20 vs SPY** at the **2026-08-13** settle, **quoted together with its
full-year revision breadth** (C2 — one axis alone is what created this disagreement).
**State at registration (2026-08-06 settled): +7.413**, FY breadth net-down.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (against the tag)** | RS20 vs SPY **≤ +2.53** | **The revision book led and the flow tag lagged** ⇒ a 🟢 built on a decelerating older leg is not a signal, and the desk's green count is overstated by names in this shape |
| **B (with the tag)** | RS20 vs SPY **≥ +12.24** | **The flow tag beat the revision book** — the more informative outcome, and the one that would justify keeping a 🟢 whose estimates are falling |
| **C** | +2.53 to +12.24 | No conclusion changes |

- ★ **D93 executed BEFORE freezing**: trailing-252 **5-session** change of MET's RS20 — **mean +0.256 ·
  sd 4.658 · p15 −4.882 · p85 +4.829** ⇒ bands at the measured tails from +7.413.
- ⚠ **`margin_history MET` returns `연간 데이터 없음`** ⇒ margin percentile **`unknown` (C3)**; **no
  valuation claim is attached to either branch.**
- ⚠⚠ **MET is ALSO an S58 object (settles 2026-08-11). The two observables are different and NEITHER row
  is re-frozen** — if they disagree, **the disagreement is the finding** (the S14-ANNEX / S35-ANNEX
  precedent).
- **Information content (L3): MEDIUM.** Branch A confirms an already-measured disagreement; **branch B
  is the informative one** and is why the row is worth writing rather than dropping.
- **Invalidation (D149 standard)**: an insurance-specific catastrophe loss disclosure or an M&A event at
  MET inside the window, evidenced by a filing or two independent outlets ⇒ **VOID**.

## S68-ANNEX — 🚨🚨 leg (i) is HALF A NON-TRADING SECURITY: **EA went private on 2026-08-04/05** (**S68 is NOT re-frozen; leg (i) is VOID BY CONSTRUCTION, leg (ii) stands**)

Registered **2026-08-07 by the `industry_US` DEEP-COMM**, **hours after this run's own PREMORTEM froze
S68**, and confirmed by an independent re-measurement at the orchestrator level before it was written.
**The frozen observable is not rewritten** — moving a threshold after registration converts a forecast
into a description (L3). **This annex records what the observable was measured ON.**

**Finding 1 — EA is not a live equity.** `[EDGAR via module_disclosure_us EA: **Form 25-NSE** + **8-K
Items 2.01 / 5.01**, both dated **2026-08-04**]` · `[AP via google_en 08-05: *"Video game giant
Electronic Arts closes **$55 billion go-private sale** of its business"*]` · `[guardian body 08-05:
*"Video game maker EA bought by **Saudi-led group for $55bn**"*]` · `[prnewswire 08-04: *"**Oak-Eagle
AcquireCo, Inc.** Announces Final Results and Settlement of the … Tender Offers … for Any and All of
Electronic Arts Inc.'s … Senior Notes"*]` · `[nasdaq 08-01: *"**Ferguson Enterprises To Replace
Electronic Arts In S&P 500**"*]` · `[nasdaq/fool 07-29: *"…as the Company **Prepares to Go Private**"*]`
— **six independent primary/press corroborations.**

**Finding 2 — the price series proves it mechanically.** Verified twice, independently:

| date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| 2026-08-04 | 209.92 | 210.20 | 209.70 | **209.70** | **48,713,698** ← the merger-close settlement print |
| 2026-08-05 | 209.70 | 209.70 | 209.70 | **209.70** | **0** |
| 2026-08-06 | 209.70 | 209.70 | 209.70 | **209.70** | **0** |

⇒ **Open = High = Low = Close on two consecutive zero-volume bars.** ⚠⚠ **And every one of EA's four
"green" inputs is an artifact of that single settlement bar**: `vol_surge` **3.78 — the highest of any
green on the board** is the 48.7m-share liquidation against a 50-day mean; **OBV 매집 +0.758** (verified
by independent recomputation, the strongest in a 8-name comparison set) is the same print signed
positive; **RS20 +0.8 / RS60 −0.5** are a frozen price against a moving SPY; and **`new_green` = True**
because a frozen price cannot fall.

**Finding 3 — removing it changes the arithmetic that produced this run's own COMM promotion.**

| Universe | n | eqflow | wflow | greens | breadth | eqflow > wflow? |
|---|---|---|---|---|---|---|
| **ALL 13 (as registered)** | 13 | **+0.1363** | +0.0576 | **2** | **0.154** | ✅ |
| **ex-EA** | 12 | **+0.0893** (−34.5%) | +0.0548 | **1** | **0.083** | ✅ (still) |
| ex-EA ex-DIS | 11 | +0.0307 | +0.0442 | 0 | 0.000 | ❌ flips |

⇒ **The `eqflow > wflow` relation survives removing EA alone** (DEEP-COMM measured this and it
reproduces). **But the promotion's STATED carrier does not**: *"2🟢 of 13 · breadth 0.150, 2nd of 11 ·
both `new_green`"* becomes **1🟢 of 12 · breadth 0.083, 6th of 11 · one `new_green`.**
⇒ **ROTATION's COMM UW → UW− notch is WITHDRAWN this run** (recorded in `SECTOR_ROTATION.md` §5).

**What this changes and what it does NOT.**
- **UNCHANGED**: S68's frozen observables and thresholds. **Append-only. Nothing is widened or re-cut.**
- **CHANGED**: **leg (i) is VOID BY CONSTRUCTION and may not be scored.** With EA frozen, the median of
  {DIS, EA} between registration and the 08-13 settle is **a deterministic function of −SPY's own
  cumulative return** for half its inputs — it measures the benchmark, not the sector. **leg (ii) (DIS
  current-year revision breadth, registration 1↑ / 7↓) is the ONLY scoreable leg** and it stands.
- ⚠ **This is D50's third measured instance** — *"before freezing a multi-name observable, check each
  leg for a live corporate action."* **PYPL (07-24, a live Stripe bid) → D (08-02, a live all-stock NEE
  acquisition, S35-ANNEX) → EA (today, a CLOSED go-private).** **D50 was logged before all three.**
  ⇒ **it is escalated from a registration-discipline note to a measured, three-time repeat.**
- ⚠ **And it is worse than R40's class.** R40 says *"a security under a live bid is a merger-arb
  security, not a fundamental expression."* **EA is not under a bid — the deal CLOSED and the listing
  is terminated.** R40's rule does not reach a post-close ticker; **the successor rule must test for
  Form 25 / zero-volume bars, not only for a pending bid.**

**Successor construction, with the mechanical test that would have caught it (a human applies it):**
before freezing any multi-name observable, assert for every leg that **(a)** the last settled bar's
volume is **non-zero**, **(b)** `Open ≠ High ≠ Low ≠ Close` is not degenerate across the last two bars,
and **(c)** `module_disclosure_us <TKR>` shows no **Form 25 / 25-NSE** in the trailing 30 days.
**All three are cheap, deterministic, and each one alone catches EA.**

🚨 **Root cause, and the guard that fired unread**: `data/us_universe/us_top300.csv` was **last built
2026-07-15 — 23 days stale — and still carries EA as live.** **`sector_flow.py` DID warn**:
`[warn] 유니버스 us_top300.csv 23일 경과 — 시총 stale. build_top300.py 재빌드 권장(주1회).`
⚠⚠ **This stage's own operator redirected the sweep's stderr to a log and read only its tail, so the
warning was emitted and never read** — recorded as this run's failure, not the tool's. ⚠ **And the
guard tests the WRONG PROPERTY anyway**: its message is about **stale market caps**, while the cost
this run was a **delisted constituent tagged 🟢 `new_green`.** **A universe-freshness guard that does
not test constituent liveness cannot catch this class.**


---

## S70 — ★★★ Did the 08-07 credit print read RELIEF or FEAR? · ARMED · → first `[FRED]` close covering 2026-08-07 (expect **2026-08-10**)

Registered **2026-08-08 by the `industry_US` MACRO stage.**

**Why it exists.** **S66** brackets **ΔDGS2 + ΔHY OAS jointly** from the 08-05 anchor. But this run
measured that **the two legs sit on different publication clocks** — `T10YIE` printed **08-07** while
`DGS2` and `BAMLH0A0HYM2` stop at **08-06**, even though `T10YIE ≡ DGS10 − DFII10` (**D212**) — and the
desk has now carried *"was 08-07 dovish relief or credit fear"* as **`unknown` for two consecutive
runs**. **S66 can be blocked by either leg; this row scores the CREDIT leg ALONE so one lagging series
cannot swallow the whole question.**

| Branch | Frozen observable | Meaning |
|---|---|---|
| **A (relief)** | **HY OAS ≤ 2.71%** at the first `[FRED]` close covering 2026-08-07 | Credit tightened or held through the payroll shock ⇒ **the 08-07 rally was rate relief.** P32-A strengthens and the UW duration tilts stay coherent |
| **B (fear)** | **HY OAS ≥ 2.96%** | Credit widened ≥25bp ⇒ the payroll contraction was read as a growth scare. **S26's kill line (3.10) comes within 14bp** and every cyclical tilt on the board is re-argued |
| **C** | 2.72 – 2.95 | No conclusion changes |

- **Frozen observable**: `BAMLH0A0HYM2` (`hy_oas`) via `module_macro_us --json`, **`[FRED]` only**,
  first published close dated **2026-08-07**; expected publication **2026-08-10**.
- **State at registration, disclosed**: **2.71% (08-06)** ⇒ **branch A's line is exactly the last
  print, i.e. A requires NO widening at all.** Stated now rather than discovered at scoring.
- ★ **D93 executed BEFORE freezing**: trailing-60 `[FRED]` closes of daily ΔHY OAS — **mean −0.0017pp ·
  σ 0.0479pp**; the 5-session change has **σ ≈ 0.107pp** ⇒ **branch B at +25bp ≈ 2.3σ of a 5-session
  move**, a genuine tail rather than a round number. ⚠ **The estimator's centre is −0.0017, not zero —
  disclosed, and the bands are NOT symmetric around zero.**
- **Information content (L3)**: **both branches change a conclusion**, and **reachability was checked at
  registration (D206)** — A is at the current level, B is 25bp away against a ~11bp 5-session σ.
  **Neither branch is degenerate.** ⚠ **DEEP-FIN's grading is recorded with the row: branch A is the
  MODAL outcome and mostly confirms what the tape already shows; the real information is entirely in
  branch B.**
- ⚠ **Anti-signal**: if FRED publishes an 08-07 close **without** an `hy_oas` value (an OAS-series
  holiday gap), the row is **`AMBIGUOUS`**, not re-dated.
- **Owner**: `industry_US`.

---

## S71 — ★★★ The CPI→PPI DIVERGENCE — the one genuinely un-covered falsifiable gap · ARMED · → settle **2026-08-13**

Registered **2026-08-08 by the `industry_US` PREMORTEM (Lens 2).**

**Why it exists.** Lens 2's finding: **a COOL CPI followed by a HOT PPI is the one path that hits all
four members of the real correlated cluster (INDU · FIN · MATR · UTIL) and leaves none of them
relieved** — MATR and UTIL rally on 08-12 and reverse on 08-13. **No registered bracket covers a
two-day divergence**: every existing row settles either **08-11 (before CPI)** or **08-12/08-13 on a
LEVEL, not on a reversal.** ⇒ **the desk currently has no instrument that can tell a real CPI reaction
from noise.**

| Branch | Frozen observable | Meaning |
|---|---|---|
| **A (the CPI reaction was REAL)** | **Δ ≥ +1.57pp** — XLU's 1-session excess vs SPY on **2026-08-13** MINUS its 1-session excess vs SPY on **2026-08-12** | The two prints agree; the duration read established on CPI day **extends**. The four-tilt cluster's exposure is directional and must be treated as one bet |
| **B (the CPI reaction REVERSED)** | **Δ ≤ −1.69pp** | PPI contradicts CPI ⇒ **any conclusion drawn from the CPI print alone is FALSIFIED**, and the whipsaw is the finding |
| **C** | between | The two prints did not disagree materially. No conclusion changes |

- **Frozen observable**: `XLU` minus `SPY`, **1-session % excess on settled daily closes**, yfinance,
  `auto_adjust=False`, **benchmark named inline (C1)**; the quantity is **the 08-13 value minus the
  08-12 value**. **Anchor and endpoint are BOTH in the future at registration ⇒ no look-ahead.**
- ★ **D93 executed BEFORE freezing.** Trailing **252** settled sessions of that exact day-over-day
  change: **mean +0.0063pp · sd 1.6268pp · q15 −1.686 · q85 +1.571.** **Bands taken at the measured
  quantiles.** ⚠ **The estimator's centre is +0.0063, not zero** — disclosed at registration; **this is
  the SIXTH independent reproduction of that bias on this desk** (S55, S57, S58, S60, S61 were the
  first five).
- **Why XLU is the leg**: it is the **most rate-sensitive** of the four cluster members and **the one
  with no live bracket at all** — S62 settled today, and S63's DUR composite settles 08-13 on a
  **level**, not a reversal. Lens 2 named it explicitly.
- **Information content (L3)**: **branch B FALSIFIES** — it kills any conclusion drawn from CPI day.
  **A confirms and also sizes the cluster question.** **Neither is degenerate**: ±1.6pp against an sd of
  1.63pp is a **~1σ** ask over one session, and **XLU's own D6 option-implied move is ±1.8%**, so both
  branches sit **at the edge of, not inside, what is priced.** ⇒ **this bracket passes the test S57
  fails.**
- ⚠ **Anti-signal, BOTH sides (the D191 two-sided rule)**: **(a)** if **either** print is delayed or
  released off-schedule, the row is **`VOID`**, not re-dated; **(b)** if a **non-macro, XLU-specific
  event** lands on 08-12 or 08-13 (a large-cap utility M&A headline, an ERCOT emergency), the row is
  **`AMBIGUOUS`** — the contamination class that VOIDed S43.
- **Owner**: `industry_US`.

---

## S72 — ★★★ Is the four-tilt cluster ONE bet? Two stages of one run disagreed, and the disagreement is registered · ARMED · → settle **2026-08-12**

Registered **2026-08-08 by the `industry_US` PREMORTEM (Lens 2).**

**Why it exists.** This run's **MACRO §F** warned that *"three of the eleven tilts (ENRG, MATR, UTIL)
are driven by the SAME variable — the path of rate expectations."* **Lens 2 refuted the grouping**:
ENRG's tape is dominated by the **Hormuz supply narrative**, not real yields (**XLE is −6.95pp vs SPY
over 5 sessions and already past S60's bearish line for unrelated reasons**), while **the actual
concentration is INDU + FIN + MATR + UTIL — four GICS labels, one exposure.** ⇒ **two stages of one run
disagree about which tilts are correlated, and this desk has been burned by correlated tilts wearing
different labels three times (R7, R10, S62).** **The disagreement is registered rather than resolved by
picking a side (§6 discipline).**

| Branch | Frozen observable | Meaning |
|---|---|---|
| **A (Lens 2 is right — it IS one bet)** | On the **2026-08-12 CPI-day settled close**, the **1-session excess vs SPY of XLI, XLF, XLB and XLU all carry the SAME SIGN** | Four GICS labels, one macro exposure. **MACRO's warning was one tilt too small AND named the wrong member**, and the board's real risk unit is 4-wide |
| **B (MACRO is right — ENRG belongs, INDU/FIN do not)** | **XLE's 1-session excess vs SPY shares the sign of XLB and XLU on 08-12, while XLI and XLF do NOT** | The rate path is the shared driver and Energy is inside it; Lens 2's Hormuz-detachment argument fails |
| **C** | any other sign pattern | **Neither decomposition survives** — the labels are not a risk unit and **both stages were wrong** |

- **Frozen observable**: 1-session % excess vs **SPY** (named inline) of **XLI, XLF, XLB, XLU, XLE** on
  the **2026-08-12 settled close**, yfinance, `auto_adjust=False`.
- **State at registration, disclosed**: on the **08-07** settle the five read **XLI −0.38 · XLF −0.97 ·
  XLB +0.71 · XLU −0.08 · XLE −1.75** ⇒ **branch A is NOT currently true (XLB's sign differs) and
  branch B is NOT currently true (XLE and XLU agree but XLB does not). Today is a C.**
- **Information content (L3)**: **all three branches change a conclusion, and C is the modal AND the
  most informative** — it would retire a risk-unit framing both stages currently use.
- ⚠ **This is a SIGN-PATTERN bracket, so no D93 band is needed and none is invented. Its weakness is
  disclosed HERE rather than discovered at scoring: a near-zero excess can flip sign on noise, so
  any leg reading |excess| < 0.20pp is recorded as `flat` and the row scores `AMBIGUOUS` rather than
  being forced into a sign.**
- ⚠ **Anti-signal, BOTH sides**: **(a)** a CPI delay ⇒ **`VOID`**; **(b)** an intraday circuit-breaker
  or market-wide halt truncating 08-12 ⇒ **`VOID`**.
- **Owner**: `industry_US`.

---

## S57-ANNEX — ★★★ contamination notice on branch A's stated MEANING (**S57 is NOT re-frozen; thresholds unchanged**)

Registered **2026-08-08 by the `industry_US` MACRO stage, EXTENDED by PREMORTEM and DEEP-MATR the same
run. Registered BEFORE the branch can fire — that is the point.**

S57's branch A (**XLB 5-session excess vs SPY > +1.9**, firing at **ANY** settled close through
**2026-08-12**) currently reads **+1.307 — 0.59pp away.** Its stated meaning has **three components**,
and **all three fail on fresh data**, with **three further legs added by later stages:**

| Leg | Measured 2026-08-08 |
|---|---|
| 1. *"Materials outperform"* | ⚠ **W5 — it is TWO NAMES.** 5-session excess vs SPY: **NEM +17.05 · ALB +7.94 · FCX +7.65** against **CF −12.17 · LYB −7.52 · DOW −6.65 · CTVA −5.90 · BALL −5.75 · CE −5.37**. **XLB itself is +1.31** |
| 2. *"while the dollar is falling"* | ⚠ **Unsupported on the only fresh instrument**: **USD Index spec net long at the 81st percentile and BUILDING (+5,302)**; `DTWEXBGS` stale since 2026-07-31 |
| 3. *"and the crowded-long leg did not cap it"* | ⚠ **Copper went 96th → 100th percentile, +9,842 ADDED** — the leg got **MORE** crowded |
| 4. **Revision breadth (PREMORTEM Lens 3)** | **NEM's estimates are CUT 9-to-1 while its price makes a 7-week high**: current-qtr **0↑/9↓** · FY **1↑/9↓** · next-FY **2↑/13↓** · FY estimate **−8.9%/90d**. **RS60 − RS20 = −26.5** on a 60-day base of **−10.4pp vs SPY** |
| 5. **Options noise (PREMORTEM Lens 2)** | **the 0.59pp gap is INSIDE XLB's own D6 implied move of ±2.1% (expiry 08-14)** ⇒ **a branch-A fire carries little information even before the meaning problem** |
| 6. **Decomposition by recomputation (DEEP-MATR)** | ★★★ **XLB ex-NEM = +0.194** (from +1.307) and **ex-{NEM, ALB, FCX} = −0.485, a SIGN FLIP.** Removing **6.60%** of fund weight moves the observable from 0.59pp-short-of-firing to **1.71pp-short**. **Recomputed independently from SSGA's dated 08-06 holdings file; the +1.307 was reproduced exactly first (C1)** |

⚠ **And the three excluded names are not one story wearing three tickers**: **NEM** is a rates trade
(gold at a 7-week high on the hike-odds collapse), **ALB** is a company-specific Q2 beat on a real
lithium-price recovery (~$21,000/t, ~2× y/y), **FCX** is copper at its yearly-maximum spec long with
its own **OBV at −0.071 = NOT accumulating.**

⇒ **If branch A fires, the FIRE is valid and its registered MEANING is not earned.** **The threshold is
NOT moved and S57 is NOT re-frozen** — moving a band after the fact converts a forecast into a
description (L3). **This annex exists so the 08-12 settle is read correctly rather than re-explained
afterwards — the failure shape of S49-ANNEX and R46, caught in advance for the first time.**
★ **Operational instruction for the scoring run: check the EX-NEM print (DEEP-MATR's methodology)
BEFORE reading any fire as a Materials call.**

---

## S61-ANNEX — ★★★ mechanism AND information-content notice (**S61 is NOT re-frozen; bands unchanged**)

Registered **2026-08-08 by the `industry_US` MACRO stage, EXTENDED by PREMORTEM Lens 2 the same run.**

S61's branch B reads *"No premium appears; EVENT_ALPHA Card 3's STORY-ONLY tag holds and **D168 stays
named-but-inert**."* The observable sits at **−4.184, 0.006pp from B's line (≤ −4.19).**

**Defect 1 — the LABEL is wrong.** **D168's event is the most active object in this run**, quantified at
two independent chokepoints: **Black Sea/Azov dirty-tanker loadings −62% (0.98 vs 2.59 mbpd)**, CPC
Novorossiysk −62%, India-bound −66%, **>200 ships attacked**, Kerch Strait suspended `[BIMCO via
hellenicshipping body 08-06]`; **Hormuz transits 33 vs 50 = −34%, 6 crude tankers outbound all week**,
*"the worst safety situation since the Iran war began"* `[Reuters/Kpler via oilprice body 08-07]`.
⇒ **it is transmitting through VOLUME DESTRUCTION, not through an absent premium — the opposite reason
to the one branch B's label names.**

**Defect 2 — the INFORMATION CONTENT is gone.** **0.006pp against instruments pricing ±7.2% (STNG) and
±8.7% (FRO) through their D13 expiry** ⇒ **the bracket will cross branch B on ordinary noise regardless
of what happens in the strait.** ⇒ ★★★ **this is the SIBLING of `D206` and the opposite failure: D206
catalogued a branch that became UNREACHABLE (S62's A, 19.16pp away at its settle); S61's B has become
INEVITABLE.** ⇒ **`D216`: reachability must be checked in BOTH directions.**

⚠⚠ **The bands are NOT moved. When B fires, it is scored B — and this annex is what prevents it being
read as *"nothing happened"* or as evidence about Hormuz in either direction.**
★ **Dated anti-signal, and it strengthened post-run**: `[bloomberg 08-08, title only]` *"US Says Ukraine
to Avoid Targeting Tankers, Black Sea Oil Site"* was corroborated by a **second independent outlet** in
the DRIFT pass — `[investing_en 08-08, title only]` *"Ukraine agrees to avoid targeting **SOME** tankers
and Black Sea oil infrastructure."* ⚠ **Two outlets now, still TITLE-ONLY, and the second one NARROWS
the scope to "some" — the anti-signal is upgraded in sourcing and weakened in scope, and it remains
UNFIRED.**

---

## S73 — ★★★ July CPI 2026-08-12: the ≤48h binary the protocol makes MANDATORY · ARMED · → macro leg settles at the first `[FRED]` close covering 08-12 · equity leg settles at the **2026-08-12 close**

Registered **2026-08-10 by the `industry_US` PREMORTEM (Lens 2, with the orchestrator's own σ measurement applied to the equity leg).**
**IDs checked at WRITE time against EVERY row in BOTH `SCENARIOS*.md` files and both `STANDING_VIEW*.md` and `RESEARCH.md`** (the D76 collision class); highest existing was **S72 (US) / S57-KR (KR)**; `grep S73` returned **0** in all nine handoff files.

**Why it exists.** CPI releases **2026-08-12 08:30 ET**, which was **47h12m** from this run's MACRO clock. The protocol states that any binary ≤48h out **must** carry a both-sides bracket and that a one-way tilt into it is a protocol violation. **Ten registered rows settle 08-12–08-13** (S13 · S24 · S26 · S41 · S42 · S57 · S59 · S61 · S72, then S46 · S63 · S64 · S67 · S68 · S69 · S71) and **CPI moves the reading of most of them**, yet no row brackets CPI itself.

**★ Two legs, scored INDEPENDENTLY — the S70 pattern applied at registration.** `D212` has now run for **four consecutive runs**: the `[FRED]` H.15 and OAS blocks publish 3–4 sessions behind, which is why **S51 · S66 · S70 were all DUE on 2026-08-10 and none could be scored.** A CPI bracket resting only on FRED would inherit that failure. **The equity leg settles on the CPI session itself and cannot be blocked by a publication lag.**

### Leg 1 — macro (the discriminator)

**Frozen observable**: `ΔDGS2` = `DGS2`(settle) − **4.25** and `ΔHY OAS` = `BAMLH0A0HYM2`(settle) − **2.71**, both `[FRED]`, both anchored on the **2026-08-06** close (the last published pre-CPI print), read at the first settled close covering **2026-08-12**.

| Branch | Threshold | Meaning |
|---|---|---|
| **H (hot / hawkish — against INDU OW−, FIN N+, STPL UW−)** | `ΔDGS2` ≥ **+0.15** **AND** `ΔHY OAS` ≥ **+0.10** | Hawkish repricing **with** a credit-spread break. **INDU OW− loses cyclical support outright**; **STPL UW−** is hit by the defensive rotation a risk-off tape produces — and STPL is one of this run's DEEP picks. **FIN is genuinely two-sided** (a steeper curve helps NIM; a risk-off tape has dragged bank equities regardless) and is graded so rather than asserted. **UTIL UW / RE UW are VALIDATED, not hit.** |
| **C (cool / dovish, no credit stress — against UTIL UW, RE UW, MATR N−)** | `ΔDGS2` ≤ **−0.15** **AND** `ΔHY OAS` ≤ **−0.05** | Dovish **without** credit fear ⇒ a duration/safety bid. **UTIL UW and RE UW are the desk's most exposed calls.** **MATR N− loses its one live non-NEM leg by that leg turning positive** — the dollar extends its slide against a COT spec long at the **81st percentile and building**, which is exactly **P44's Direction B**. FIN's NIM reading stays usable, so FIN/INDU/ENRG are **not** hit here — branch C is narrower than H by construction. |
| **N** | anything else | No conclusion changes. |

- ★ **D93 executed BEFORE freezing, on the observable's own trailing-60 distribution, and reproduced independently by the orchestrator from its own FRED pull:** `DGS2` 1-day **mean +0.50bp · sd 5.20bp** (2-day sd 6.87bp); `hy_oas` 1-day **mean −0.15bp · sd 3.46bp** (2-day sd 5.00bp).
  ⇒ **ΔDGS2 ≥ +15bp ≈ 2.8σ of a 1-day move / 2.1σ of a 2-day move**; **ΔHY OAS ≥ +10bp ≈ 2.9σ / 2.0σ.**
  ⚠⚠ **The estimator centres are NOT zero (+0.50bp and −0.15bp) — disclosed, and the bands are not symmetric around zero.**
- ⚠ **A naive round ±10bp would be 1.9σ on `DGS2` and 2.9σ on `hy_oas` — the same round number means different things on the two series.** That is why they are not set equal.
- ⚠ **No implied move is used and none is fabricated** — these are macro observables (the S9/S51/S66 treatment).
- 🚨 **Settlement risk, pre-declared**: given `D212`, the first FRED close covering 08-12 may not print until **08-14–08-18**. **This leg is registered on the CPI date and may settle several days later. That is NOT grounds to re-date it** — the observable is anchored, not the calendar.

### Leg 2 — equity (the timeliness fix; scored independently of Leg 1)

**Frozen observables**, settled daily closes, one provider (`yfinance`, `auto_adjust=False`), **the 2026-08-12 session**, bench **SPY** named inline:
- **H-equity**: **median 1-session excess vs SPY of {JPM, BAC, XLI} ≤ −1.50pp**
- **C-equity**: **XLU 1-session excess vs SPY ≥ +2.00pp**

- ★ **D93 on both, trailing 60 settled sessions to 2026-08-07** (the orchestrator's own measurement):
  median{JPM,BAC,XLI}: **mean +0.172 · sd 1.179 · p05 −2.03 · min −2.23** ⇒ **−1.50 is −1.42σ and fired on 10.0% of the trailing 60.**
  XLU: **mean −0.135 · sd 1.409 · p95 +2.24 · max +3.51** ⇒ **+2.00 is +1.52σ and fired on 6.7% of the trailing 60.**
  ⚠ **Both estimator centres are non-zero (+0.172, −0.135) and disclosed.**
- ★ **Both thresholds sit OUTSIDE the option-implied move**, checked rather than assumed (`module_flow --positioning`, this run): **JPM ±2.2% · BAC ±2.0% · XLI ±2.1% · XLU ±1.9%, all expiry 2026-08-14 (D4)** — a **whole-path-to-expiry** figure covering CPI **and** PPI, against which a **single-session** 1.50pp / 2.00pp excess is a genuine tail. **A threshold inside the implied move would be pre-declared no-information; these are not.**
- ⚠ **Leg 2 is a directional CONFIRMATION, not a second discriminator.** In a hot print both cyclicals and duration can fall; the clean separation lives in Leg 1. **Stated at registration so no scorer reads a fired Leg 2 as independent evidence.**

### Information content (L3) and reachability (D216)

- **HIGH and symmetric.** **Branch H falsifies the INDU / FIN / STPL legs of the tilt simultaneously; branch C falsifies the UTIL / RE / MATR legs simultaneously.** There is no outcome under which the desk learns nothing.
- **Reachability: every leg lands between 1.4σ and 2.9σ** — **none is `>3σ` (unreachable), none is `<0.25σ` (inevitable).** Recorded explicitly because this desk measured **both** degenerate failure modes inside one week (S62 unreachable at 19.16pp; S61 inevitable at 0.006pp = 0.001σ).
- ⚠⚠ **Correlated-tail flag, registered so it is not double-counted later**: **`S74`'s branch B (Hormuz conditions harden) raises the probability of branch H here** via energy pass-through. **If both fire, that is ONE compounding regime flip hitting INDU through two mechanisms — not two independent confirmations.**
- **Most exposed DEEP pick: INDU**, targeted by branch H here **and** by S74-B, and those two are not independent (above).

**Owner**: `industry_US`.

---

## S74 — ★★★ Hormuz: the reopening condition is NAMED for the first time in nine runs · ARMED · → **2026-08-24** (or on first occurrence)

Registered **2026-08-10 by the `industry_US` PREMORTEM (Lens 2, on an object MACRO and EVENT_ALPHA surfaced the same run).**
**IDs checked at WRITE time against every row in both files**; after S73 the highest existing was S73; `grep S74` returned **0** in all nine handoff files.

**Why it exists.** **`S8` — this desk's only Hormuz bracket — has been an undated `[blank]` and un-scoreable for NINE consecutive runs**, on the loudest event axis in the feed (today's largest cluster: **30 articles / 17 outlets**). **`S8` is human-gated (P5) and is NOT touched, re-dated or re-frozen by this row.** What changed today is that **the object finally exists**: the IRGC stated the Strait reopens *"once the US accepts its conditions"* and **named them** — **(a) an end to the US naval blockade, (b) compensation for war damages** — and said explicitly that **the reopening does NOT depend on how the Oman talks develop** `[dw body 2026-08-08]` `[aljazeera body 2026-08-09]`.

★★ **That last clause retires a mechanism the desk has been watching since 08-05.** Every carried framing — *"Iran says reached a deal with Oman on Hormuz"* (08-05, 18 outlets) → *"deal in final stage"* (08-06) → *"Iran says Hormuz deal close"* (08-08) — treated **the Oman track as the path**. **The party that controls the Strait says it is not.** Same class as **R46**: the desk was watching the wrong object.

**Frozen observable — a NEWS observable, and its grading is stated**: a **dated, attributable statement or action** bearing on the two named conditions, in the `--scope foreign` pool, **corroborated in ≥2 outlet BODIES** (not titles). ⚠ **This is `[news]` grade, not `[measured]`** — it may not be cited as a price measurement, and no magnitude is fabricated for it.

| Branch | Observable | Meaning |
|---|---|---|
| **A (conditions met or dropped — against ENRG N+)** | a dated US stand-down or partial lift of the naval blockade, **or** a compensation framework announced, **or** an **unconditional** Iranian reopening statement | **ENRG N+ loses its only live macro carrier.** Crude falls; **S54's airline-beneficiary branch becomes the live object.** ⚠ This branch also **discharges `S8`'s trigger**, and the human who owns S8 should be told so |
| **B (conditions harden — against INDU OW−)** | a formal US refusal of the two named conditions, **or** a strike on a transiting VLCC | Crude and the distillate crack stay bid — **this VALIDATES ENRG N+ rather than flipping it** — and hits **INDU OW−** through fuel costs and through **S54's own branch B (EW{UAL,DAL} 5-session excess < −4.5)** |
| **C** | neither, by 2026-08-24 | `AMBIGUOUS`. No conclusion changes |

- 🚫 **`S61` (EW{STNG,FRO}) is explicitly NOT used as this row's price confirmation, and the reason is measured.** S61 sits **0.006pp from its branch B against a 5-session sd re-measured this run at 6.287pp = 0.001σ** — the **D216 *inevitable*** class. **It will cross regardless of which Hormuz branch is real**, so using it here would manufacture a false confirmation.
  ★ **`S54` is used instead**: EW{UAL, DAL} 5-session excess vs SPY, currently **+2.110**, against a sd re-measured independently this run at **6.598** (its registration recorded 6.562 — reproduced to 0.5%) ⇒ **branch A +0.97σ and branch B −1.00σ away. Near-symmetric, and the healthiest reachability profile on the board.**
- **Information content (L3)**: **branch A HIGH — spend it** (it flips ENRG's only live carrier, and it is the first run in nine where the mechanism is checkable at all). **Branch B MODERATE and pre-declared LOW-SURPRISE** — the standing read already assigns it the higher probability and the price thread is already re-accelerating (**6 → 7 → 17 outlets over three days**), so a B outcome mostly *confirms*; its marginal value is the INDU linkage, not a fresh Hormuz signal.
- ⚠ **Anti-signal (both sides)**: **(a)** if a reopening happens with **no** statement on either named condition, the conditions were never the binding variable and this row's whole framing is wrong; **(b)** if the Oman track produces the reopening after all, the IRGC statement was posturing and **the retired mechanism must be un-retired.**
- ⚠ **Correlated with `S73` branch H** — see S73's registered flag. **Do not stack them as independent evidence.**

**Owner**: `industry_US`.

---

## S57-ANNEX-2 — ★★★ the carrier's driver is now DATED and PRIMARY-SOURCED (**S57 is NOT re-frozen; thresholds unchanged**)

Added **2026-08-10 by the `industry_US` PREMORTEM.** **S57's observable, thresholds and settle date are untouched.**

`S57-ANNEX` was registered **before** branch A could fire, on the concern that XLB's 5-session excess is carried by a handful of names. **That concern is now a dated fact with a named cause.**

- **NEM is ~85% of the observable**: XLB exc5 **+1.307**, ex-NEM **+0.194** (M502) ⇒ NEM contributes **+1.113 of +1.307**. NEM's own 5-session excess vs SPY is **+17.05pp** — **the maximum of its own trailing 60 sessions** and **+3.32σ above that window's mean (−1.207, sd 5.508)**.
- **Its driver printed 2026-08-10, from the issuer**: Newmont and Barrick settled all Nevada Gold Mines disputes; **Newmont will PAY Barrick $1.95bn**; Newmont **consented to Barrick's North American gold IPO** `[globenewswire press release + nasdaq body + wsj + mining]`. ⚠ **The WSJ headline (*"Barrick Mining Settles Newmont Nevada Dispute for $1.95 Billion"*) reverses the direction of the payment; the body settles it.**
- ★★ **And the momentum decomposition says this is not a trend at all**: NEM's **60-day excess vs SPY is −10.36pp** while its **last-20 excess is +16.14pp** ⇒ the **21–60-day base is −26.50pp**. **The entire move sits on a losing base** — the opposite of an extended-but-live cycle name. Computed twice independently this run (orchestrator and PREMORTEM Lens 3) and agreeing to 0.01pp.
- **Corroborating non-price axes**: revision breadth **1↑/9↓ this FY, EPS −8.8%/90d**; FINRA short-vol **z +1.30 and rising**; a **🔴RESOLVED ledger row is already filed (recheck 08-13)**.
- ⇒ **If S57 branch A fires, it fires on a one-name M&A/JV event and carries no information about Materials.** **The threshold stands; its stated MEANING does not.** **ROTATION already declined to move MATR on the aggregate; this annex records why that was right.**
- ⚠ **Scope (C4)**: this does **not** assert there is no sector leg. It asserts the aggregate cannot show one while 85% of it is a single name in a corporate event. **The falsifier is registered in P44: XLB's ex-NEM excess turning positive on a settled close.**

---

## S75 — ★★ ENERGY N+ → OW− was promoted TODAY; this is its falsifier · ARMED · → settle **2026-08-19**

Registered **2026-08-12 by the `industry_US` PREMORTEM (Lens 2, §2d)**. IDs checked at WRITE time
against every row in all three `SCENARIOS*.md`, both `STANDING_VIEW*.md` and `RESEARCH.md` (D137/D76/
M319): `grep S75` returned **0 in all nine files**; highest existing **S74 (US) / S57-KR (KR)**.

**Why it exists.** `SECTOR_ROTATION.md §2` promoted ENRG **N+ → OW−** on rank-1 flow (wflow +0.360 ·
eqflow +0.163 · Δ +0.074, no flipper). **A tilt changed today without a falsifier is the one-way bet
PREMORTEM exists to stop.**

**Frozen observable**: `XLE` **5-session excess vs `SPY`** (benchmark inline, C1), **settled daily
closes**, yfinance `auto_adjust=False`, read at the **2026-08-19** settle.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (against the promotion)** | ≤ **−3.60** | The rank-1 flow did not persist; the promotion was made at a two-session local top ⇒ **ENRG reverts to at most N+** |
| **B (with the promotion)** | ≥ **+3.94** | The outperformance held a p85 reading for six more sessions ⇒ the promotion is validated on the axis it was made on |
| **C** | between | ~70%, no conclusion changes |

- ★ **D93 executed BEFORE freezing**, trailing-252 settled sessions: **mean +0.280 · sd 3.815 ·
  p15 −3.601 · p85 +3.936**. ⚠⚠ **The estimator is NOT centred on zero — the 6th independent
  reproduction of the bias S55 first caught**, so the bands are the measured tails, not a symmetric band.
- **State at registration, disclosed**: **+4.218** — **already 0.28pp ABOVE branch B.** **Branch B is the
  RUNNING branch and branch A is the adversarial ask at 2.05σ.** (The S57/S60/S61 disclosure practice.)
- **D216 reachability**: B is **not** degenerate — it must **hold** a p85 reading for six sessions
  against a 3.815pp 5-session sigma in a mean-reverting estimator.
- ⚠ **Implied move is context, NOT the threshold (D28)**: `XLE` **±2.2%** (expiry 2026-08-14, D2),
  P/C 6.11. **A single-ETF straddle prices its absolute path to expiry, not a vs-SPY spread**, so the
  bands come from D93 and no straddle value was used to set them.
- **Information content (L3): HIGH and symmetric** — both branches change the ENRG verdict.
- **Invalidation (D149)**: an index-level constituent event inside `XLE` (a top-3 weight M&A or guidance
  withdrawal) evidenced by a filing or two independent outlets ⇒ **VOID**. ⚠⚠ **This desk currently
  CANNOT run that check — the news path is dead in both routes (PREFLIGHT G1). Stated at registration.**
- **Owner**: `industry_US`.

---

## S76 — ★★★ HEALTH CARE N → N+ was promoted TODAY on a breadth artifact; TWO legs, scored independently · ARMED · → **2026-08-19**

Registered **2026-08-12 by the `industry_US` PREMORTEM (Lens 2, §2d)**. `grep S76` → **0 in all nine files.**

**Why it exists.** The promotion rests on a claim about **why the sweep's breadth column reads 0.00**:
**18 of 32 HLTH names pass `OBV 매집 ∧ RS20>0` and every one is blocked by `vol_surge` alone** (M144's
6th replication). **A promotion resting on a diagnosis needs a bracket on the diagnosis, not only on
the price** — hence two legs, scored independently (the **S70** pattern).

**Frozen observables**: **leg 1** = `XLV` 5-session excess vs `SPY`, settled closes, at the 2026-08-19
settle. **leg 2** = the count of Health Care names satisfying `OBV 매집 ∧ RS20 > 0` in the next full
`sector_flow --market us` sweep, on the same `us_top300` sector membership (**32 names today**).

| Branch | Leg 1 (`XLV` exc5) | Leg 2 (accumulation count) | Meaning |
|---|---|---|---|
| **A (against)** | ≤ **−2.67** | ≤ **10 of 32** | The price gave it back / the accumulation was never there ⇒ **the promotion was a volume-gate artifact read backwards** |
| **B (with)** | ≥ **+2.62** | ≥ **22 of 32** | Both the price and the underlying breadth confirm |
| **C** | between | between | no conclusion changes |

- ★ **D93 (leg 1)**, trailing-252: **mean +0.086 · sd 2.650 · p15 −2.673 · p85 +2.615.** ⚠ centre ≠ 0
  (the **7th** reproduction). **Leg 2 is anchored on today's measured 18 of 32**, with bands set at
  roughly ±8 names — **not a distributional tail, and that is disclosed**: no historical series of this
  count exists, so leg 2 is a **pre-registered threshold on an un-modelled statistic (C3)**.
- **State at registration**: leg 1 **+3.746** (already **1.13pp above branch B**, disclosed) · leg 2 **18**.
- ⚠ **Implied move as context only (D28)**: `XLV` **±1.3%** (expiry 08-14, D2), P/C 0.69, skew +6.7.
- **Information content (L3): HIGH.** ★ **Leg 2 is the higher-information leg** — it tests the
  *mechanism* the promotion was argued from, which no price observable can reach.
- **Invalidation (D149)**: a top-3 `XLV` weight M&A or guidance withdrawal (leg 1); a change to
  `us_top300` HLTH membership between runs (leg 2) ⇒ **VOID that leg only**, not the row.
- **Owner**: `industry_US`.

---

## S77 — ★★★ MATERIALS: S57 FIRED and the tilt was carried anyway — this is the REPLACEMENT falsifier · ARMED · → **2026-08-19**

Registered **2026-08-12 by the `industry_US` PREMORTEM (Lens 1a/2d)**, **against this run's own
ROTATION decline.** `grep S77` → **0 in all nine files.**

**Why it exists — and it is the sharpest row on this board.** **S36 closed 08-05 → S57 became MATR's
only live falsifier → S57 FIRED-A on 08-10 (+2.227) and again on 08-11 (+2.484) against a +1.9 line →
`SECTOR_ROTATION.md §2c` declined the promotion on the flipper rule (LIN 24.7%) and on `eqflow` having
DECAYED +0.040 → +0.018.** ⇒ **the N− has been running WITHOUT a falsifier since 08-11**, which is
exactly what S57's own registration text was written to prevent.
★ **And P44's registered anti-signal fired**: *"if XLB's ex-NEM excess turns positive on a settled
close, A is wrong and there is a sector leg."* Measured this run — **cap-weighted +1.203 ·
equal-weighted +0.908 · 8 of 12 names positive · NEM only 11.6% of sector cap** (MACRO §C-2; P44 scored
**MISS** in MACRO §F).

**Frozen observable**: the **equal-weight 5-session excess vs `SPY`** of the **11 non-NEM `us_top300`
Materials names, listed so the basket is reproducible**: **APD · CRH · FCX · LIN · VMC · SHW · ECL ·
MLM · STLD · NUE · CTVA.** Settled daily closes, yfinance `auto_adjust=False`, at the **2026-08-19** settle.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (the UW− is WRONG)** | ≥ **+2.03** | The sector leg is broad and **NEM-free** ⇒ **MATR must move off N−**, and the 08-11 decline was an error of the permitted axis, not of the evidence |
| **B (the UW− is RIGHT)** | ≤ **−2.04** | The 08-11 reading was Newmont plus noise ⇒ **the first NEM-free confirmation this UW has ever had** |
| **C** | between | ~70%, no conclusion changes |

- ★ **D93 executed BEFORE freezing**, trailing-252: **mean +0.066 · sd 2.142 · p15 −2.043 · p85 +2.028.**
  ⚠ centre ≠ 0 (the **8th** reproduction), though this is **the most nearly centred estimator of the four
  registered today.**
- **State at registration**: **+0.908 — mid-band.** ★ **The only one of today's four rows whose branches
  are near-symmetric around a near-zero mean: A is +1.12pp away (0.52σ), B is −2.95pp (1.38σ).**
- **Information content (L3): HIGHEST on the board.** Branch A **forces a tilt change** on a sector this
  run declined to move; branch B is the UW's **first fresh, NEM-free confirmation**. Neither is degenerate.
- ⚠ **Contrary axis recorded at registration**: **`XLB` FINRA short-vol z +2.02 with 5v5 +14.8▲ — the
  largest name-level short build on this run's pull** sits on the very instrument this row measures. **If
  that short is right, BOTH directional readings are early.**
- **Invalidation (D149)**: M&A, a guidance withdrawal, or an index deletion at any of the **11 named
  constituents** ⇒ the basket stops measuring the sector axis ⇒ **VOID.** ⚠⚠ **The desk cannot run that
  check today (G1) — stated at registration, not discovered at scoring.**
- **Owner**: `industry_US`.

---

## S78 — ★★ FINANCIALS N+ → N was demoted TODAY on eqflow while S51 CONFIRMED its mechanism · ARMED · → **2026-08-19**

Registered **2026-08-12 by the `industry_US` PREMORTEM (Lens 2, §2d)**. `grep S78` → **0 in all nine files.**

**Why it exists.** ROTATION demoted FIN on the only permitted axes (**eqflow −0.043 · Δ −0.078**, because
BRK-B makes it a `top1_flips_sign` bucket), while **S51 FIRED-A the same run** — the bear steepener
persisted at 2s10s **+0.47**, so the NIM mechanism is intact — and **S65 FIRED-C**, i.e. the breadth
neither converted nor collapsed. ⇒ **the demote and the mechanism point opposite ways, and the
disagreement is registered rather than resolved by picking a side (§6 discipline).**

**Frozen observable**: **median RS20 vs `SPY` of {JPM, BAC, WFC, BRK-B}**, settled closes, at the
**2026-08-19** settle. ⚠ **Deliberately the same basket as the closed S65** — its question (*does the
velocity-lit breadth convert?*) settled at **C** and is therefore **unresolved, not answered**; a fresh
endpoint with fresh bands is the right instrument, not a duplicate.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (the demote was WRONG)** | ≥ **+4.68** | The quad re-accelerates through the CPI print ⇒ the breadth was money after all and **FIN should not have been cut** |
| **B (the demote was RIGHT)** | ≤ **−5.65** | The velocity-lit greens gave it back ⇒ **the third consecutive demote is confirmed on a non-cap-weighted axis** |
| **C** | between | ~70%, no conclusion changes |

- ★ **D93 executed BEFORE freezing**, trailing-252 of the **level**: **mean +0.066 · sd 5.201 ·
  p15 −5.650 · p85 +4.676.** ⚠ centre ≠ 0 (the **9th** reproduction).
- **State at registration**: **+2.871** — mid-band; its **4-session change is −0.533** against a measured
  4-session sd of 3.421.
- **Companion diagnostic, quoted but NOT frozen** (S65's discharged pre-commitment, carried forward):
  the same median **ex-BRK-B** reads **+3.084** vs **+2.871** with it — a **0.21pp** gap ⇒ **neither
  branch may later be attributed to BRK-B.**
- ⚠ **Two of the four names are VELOCITY-LIT greens** — **JPM (`vol_surge` 0.56, `velocity` 1.27)** and
  **BRK-B (0.92 / 1.51)** — on an **11.3%-coverage** news axis. **That contamination is the reason the
  row exists**, and it is disclosed here rather than discovered at scoring.
- ⚠ **Implied move as context only (D28)**: `XLF` **±0.7%** (expiry **2026-08-12, D0**). **A ±5pp move in
  a four-name median over six sessions is far outside any single-name straddle** ⇒ both thresholds carry
  information.
- **Information content (L3): HIGH and symmetric** — both branches settle a demote made today.
- **Invalidation (D149)**: bank M&A, a Fed capital-rule announcement, or a BRK-B-specific disclosure
  inside the window ⇒ **VOID.** ⚠ **Uncheckable today (G1).**
- **Owner**: `industry_US`.

---

## S79 — ★★★ NVDA 2026-08-26: the binary that was surfaced, handed forward, and left un-bracketed for two runs · ARMED · → settle **2026-08-27**

Registered **2026-08-12 by the `industry_US` **RUN-2** PREMORTEM** (post-CPI-print, pre-open — the
second `industry_US` run of the day; RUN-1's outputs were appended to, never overwritten).
**IDs checked at WRITE time**: `grep S79` returned **0** across all nine `handoff/*.md` files; highest
existing was **S78 (US) / S57-KR (KR)**; `handoff_id_audit` max **M587**.

**Why it exists.** RUN-1's **DRIFT** stage (§J-2) found NVDA's 08-26 print by re-pulling the schedule at
`--days 14` after an ARMED row named a date beyond the 5-day window, and wrote: *"**NVDA is a held
epicenter name of the #1 cycle**, it is one of the six velocity-lit 🟢, its days21-60 is −10.9, and it
is the cool-side ticket in `ACTION_TICKETS.md`. **No bracket owns this print.**"* It handed the item to
"the next run's PREMORTEM". **RUN-2 is that run, the print is now inside `CATALYST_WATCH`'s 14-day
window (D-14), and it is still un-bracketed.** ⇒ registered here.

★★ **And the desk's own instruments cannot currently say how big the blast radius is.** PREFLIGHT
**G4 has FAILed for three consecutive runs** on exactly this: `{AVGO, NVDA, TSM}` **merges into one
risk unit at 500d and 750d** and **splits (NVDA alone) at 250d**, so the rights table forbids asserting
either. **Leg 2 below is written to settle that by observation instead of by argument.**

### Leg 1 — the name (the directional leg)

**Frozen observable**: NVDA **1-session % excess return vs `SPY`** (bench named inline), settled daily
closes, `yfinance`, `auto_adjust=False`, on the **first settled session after the AMC print** = the
**2026-08-27** session.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (up-break)** | excess **≥ +5.0pp** | The #1 cycle's epicenter re-rates. **`IT N` is too low**, and ROTATION's repeated decline to move IT was right on dispersion but wrong on the epicenter |
| **B (down-break)** | excess **≤ −5.0pp** | The epicenter breaks **while AI capex is being funded through a structured credit pipe** (RUN-2 EVENT_ALPHA Card 4: *"Nvidia's $500bn financing plan"*, *"an exotic money pipe"*, *"soothes credit markets"*). **S41's AI-issuer credit channel and S26's HY-OAS kill line go live together** |
| **N** | anything strictly between | The print carried no information for the tilt — scoreable as such |

- ★ **D93 executed BEFORE freezing**, on the observable's own trailing-60 settled distribution to the
  **2026-08-12** data date: **mean −0.081 · sd 2.028 · p05 −2.832 · p95 +3.708 · min −5.016 · max
  +5.989.** ⇒ **+5.0pp = +2.51σ**, **−5.0pp = −2.43σ**; **each tail fired on exactly 1 of 60 = 1.7%**
  of trailing sessions.
- ⚠ **The estimator centre is NOT zero (−0.081)** — disclosed. The two thresholds are set equal in
  **pp** and therefore differ slightly in σ; that choice is deliberate and stated rather than hidden.
- ⚠⚠ **No option-implied move is quoted, and none is fabricated.** `module_flow --positioning` was not
  run for the 08-26 expiry at registration time. **The threshold's justification is the measured 1.7%
  tail frequency alone.** A scoring run may add the implied move as context but **must not move the
  band** (the S57-ANNEX lesson: moving a band after the fact converts a forecast into a description).

### Leg 2 — ★★★ the risk unit (the leg that cannot be learned any other way)

**Frozen observable**: on the **same 2026-08-27 session**, the **1-session % excess vs `SPY` of `AVGO`
and `TSM`**, same provider and settings.

| Branch | Threshold | Meaning |
|---|---|---|
| **U-ONE** | **both** AVGO and TSM carry the **same sign as NVDA's excess** **AND** each \|excess\| **≥ 2.0pp** | **The three behaved as ONE risk unit on the day it mattered** ⇒ the **500d/750d merged grouping** is the right one for event risk and **G4's 250d split is the misleading window**. Concentration is **higher** than the 250d reading implies |
| **U-SPLIT** | NVDA's \|excess\| **≥ 5.0pp** while **both** AVGO and TSM read \|excess\| **< 2.0pp** | **NVDA is genuinely its own unit** ⇒ the **250d** grouping is right and concentration is **lower** than the merged reading implies |
| **U-MIXED** | anything else (one peer moves, the other does not; or NVDA does not break ±5.0pp) | **Neither grouping survives an event test** — the most informative outcome, because it retires a framing the desk uses for its concentration guard |

- ★ **Supporting measurement taken at registration** (1-session excess vs SPY, trailing 60 settled
  sessions to 08-12): unconditional correlation with NVDA is **AVGO +0.318 · TSM +0.456 · SMH +0.448**,
  but **conditional on |NVDA excess| ≥ 3pp (n = 7 days)** it rises to **AVGO +0.612 · TSM +0.713 ·
  SMH +0.801.** ⇒ **co-movement rises on precisely the days that matter**, which is why the desk's
  *unconditional* residual-correlation clustering may be the wrong estimator for event risk.
  ⚠⚠ **n = 7, one 60-session window. This is a reason to REGISTER the bracket, not a result.**
- ⚠ **Peer-side scale, disclosed**: AVGO's own 1-session excess sd is **2.958** and TSM's **2.541**, so
  the **2.0pp** bar sits at roughly **0.68σ / 0.79σ**. **Deliberately low** — U-SPLIT must remain
  genuinely reachable or the test has no null.

### Information content (L3 / B4) and reachability (D216)

- **HIGH, and asymmetric in the useful direction.** **Leg 1 alone would mostly confirm what the tape
  says.** **Leg 2 can falsify a grouping the desk actively uses for its concentration guard**, and it
  is the only registered row on the board that tests a *PREFLIGHT gate's* unresolved question with a
  market observation.
- **Reachability checked in BOTH directions**: Leg 1 at **±2.5σ** with a measured **1.7%** base rate is
  neither **unreachable** (>3σ — the S62 failure) nor **inevitable** (<0.25σ — the S61 failure).
  Leg 2's U-SPLIT is reachable by construction (0.7–0.8σ bar on the peers).
- ⚠ **Anti-signals, BOTH sides, pre-declared**:
  **(a)** the print is **delayed or moved** off 08-26 ⇒ **`VOID`**;
  **(b)** an intraday **circuit-breaker or market-wide halt** truncating 08-27 ⇒ **`VOID`**;
  **(c)** ★ if a **separate ≤48h macro binary** (CPI/PPI/FOMC/NFP-class) lands on **08-26 or 08-27**,
  **Leg 2 scores `AMBIGUOUS`** — a macro shock moves all three semis together and would **counterfeit
  U-ONE**. **This condition is written now, before the calendar is known, precisely so it cannot be
  invented afterwards.**
- ⚠⚠ **Correlated-observation flag, so it is not double-counted**: **Leg 2 and the shock-day
  correlation measurement above are the same question measured twice.** A **U-ONE** reading is **not**
  independent confirmation of that measurement — it is the same effect observed once more.
- ⚠ **Carried context, not part of the observable**: at registration NVDA reads **RS20 +0.2% · RS60
  −10.9% vs SPY**, OBV **accumulating**, `module_chart --read` verdict **PULLBACK-TO-SUPPORT** (trigger
  `close>219.44`, stop 190.01, RSI 54.3). **The epicenter of the #1 cycle is entering its own print
  having underperformed the benchmark by 10.9pp over 60 days.**

**Owner**: `industry_US`.

---

## Brackets registered 2026-08-13 by the `industry_US` PREMORTEM (**S80 – S83**)

> **ID hygiene at WRITE time (D137 / D76 / M319)**: `grep S80` / `S81` / `S82` / `S83` returned **0 in
> all nine handoff files**; highest existing was **S79 (US) / S60-KR (KR)**. This run takes S80–S83.
> **Every band below is measured on a trailing-252 distribution BY THE REGISTERING RUN**, not judged,
> and every magnitude threshold is stated against a measured implied move
> (`module_flow --positioning`, this run; all option expiries **2026-08-14, D1**).
> Prices: `yfinance`, `auto_adjust=False`, **settled closes only**, benchmark **SPY named inline (C1)**.
> ⚠ All four are **two-sided**. A one-way bracket is a protocol violation.

### S80 — ★★★ Is the UTIL/RE/STPL underweight ONE duration bet, and is it right? · ARMED · → settle **2026-08-19**

**Why it exists.** MACRO **P51-A** says the pressure on the duration UWs is the LEVEL of `DFII10`
(2.43, 4bp off a 365-day high), not the CPI path. **PREMORTEM Lens 2 measured that UTIL + RE + STPL is
literally one bet** — 252-day pairwise excess-vs-SPY correlations `XLU–XLRE` **0.69**, `XLRE–XLP`
**0.74**, `XLU–XLP` **0.63**, and the EW complex vs `TLT` excess **0.66 (252d) / 0.74 (60d)**. **Three
GICS labels, one factor, and no bracket on the board tests them together.** This row also **replaces
the job of `S71`**, which the same lens graded **no-information before its settle** (its ±1σ bands fire
~14% each and its base bar makes the against-us branch 1.7× harder — dig `D248`).

**Frozen observable**: **equal-weight {`XLU`, `XLRE`, `XLP`} 4-session cumulative excess return vs
`SPY`**, from the **2026-08-13 settled close** to the **2026-08-19 settled close** (sessions 08-14,
08-17, 08-18, 08-19).

| Branch | Threshold | Meaning |
|---|---|---|
| **A (AGAINST US)** | **>= +1.85pp** | All three underweights are wrong **together**. **P51-A's transmission failed**: real yields stayed high and duration was bid anyway ⇒ the UW complex is a single mis-specified factor bet and ROTATION must re-argue all three, not one |
| **B (FOR US)** | **<= −2.29pp** | The UW complex is confirmed **on four sessions, not on one bar** — the first multi-session confirmation this short has ever had |
| **C** | between | No conclusion changes |

- ★ **D93 executed BEFORE freezing**: trailing **252** settled sessions to 2026-08-12 —
  **mean −0.245pp · sd 2.068pp**. Bands are **mean ± 1.0σ** ⇒ **A ≈ 15.5% · B ≈ 13.1% ·
  no-settle ≈ 71%, disclosed up front.** ⚠⚠ **The estimator centre is NOT zero (−0.245)** and the
  bands are therefore **not symmetric around zero** — this desk's 6th independent reproduction of that bias.
- **State at registration**: **−0.408pp** (2026-08-12 settle) ⇒ **inside C, closer to B.**
  **Branch A is the adversarial ask.** Disclosed at registration, not discovered at scoring.
- **Implied move, checked rather than assumed**: `XLU` **±1.1%**, expiry **2026-08-14 (D1)**,
  **P/C 4.89, skew +1.5 → hedged/fear**. ⚠ That is a **single-name, one-day** figure; this bracket
  scores a **4-session basket-vs-SPY spread**, a different and larger object ⇒ **+1.85pp is outside
  what a one-day straddle prices** and the row carries information. **The two are not conflated.**
- **Information content (L3): HIGH and symmetric.** A falsifies **three tilts simultaneously**;
  B is the first multi-session confirmation the complex has had. **No outcome teaches nothing.**
- ⚠ **Correlated-tail flag**: if `S82` fires branch B on the same window, that is **ONE finding
  (HLTH is the fourth leg of this complex), not two independent confirmations.**
- **Invalidation (D149)**: a market-wide halt truncating any of the four sessions, or an index
  reconstitution changing a constituent of any of the three ETFs ⇒ **VOID, not scored.**
- **Owner**: `industry_US`.

### S81 — ★★ NVDA 2026-08-26 READTHROUGH: is the book's 4-of-11 AI concentration one risk unit? · ARMED · → settle **2026-08-27**

**Why it exists.** `S79` already brackets **NVDA itself**. **This row deliberately EXCLUDES NVDA** —
the event name is not the test. **PREFLIGHT `G4` has FAILed four consecutive runs on exactly this
question**: `{AVGO, NVDA}` **merges at 500d/750d and splits at 250d**, so the desk cannot say whether
its largest concentration is one unit or two. **The earnings print is the one day of the year when the
answer is observable.**

**Frozen observable**: **equal-weight {`AVGO`, `ANET`, `HPE`} 2-session cumulative excess return vs
`SPY`**, from the **2026-08-25 settled close** to the **2026-08-27 settled close**.

| Branch | Threshold | Meaning |
|---|---|---|
| **A** | **>= +3.66pp** | The readthrough is real and positive — the three names are a unit that NVDA leads |
| **B (the informative one)** | **<= −2.86pp** | ★ **The book's 4-of-11 AI-compute concentration is ONE correlated loss**, which is what `G4` cannot answer and what the concentration guard exists to prevent |
| **C** | between | The three trade on their own drivers ⇒ the label groups them, the market does not |

- ★ **D93 executed BEFORE freezing**: trailing **252** settled sessions to 2026-08-12 —
  **mean +0.403pp · sd 3.258pp**. Bands **mean ± 1.0σ** ⇒ **A ≈ 13.9% · B ≈ 11.5%.**
  ⚠ **Centre is +0.403, not zero — disclosed.**
- ★★ **The band size is not a guess — it is what the measured beta predicts.**
  `beta(basket exc1 ~ NVDA exc1)` = **0.35 on 252 days (r 0.30)** and **0.33 on the top-decile
  |NVDA| days (n = 26, r 0.44)**. ⇒ **the assumed readthrough is 0.33, not 1.0**, so a 10% NVDA gap
  maps to roughly **3.3pp** of basket excess — **the 1σ band lands exactly there.**
- **State at registration**: **+5.378pp** (2026-08-12) — ⚠ **already above branch A**, disclosed;
  the observable is the **forward** 08-25 → 08-27 window and this value is **not** it (the D122 guard).
- **Implied move, measured**: `ANET` **±3.0%**, `HPE` **±4.2%**, both expiry **2026-08-14 (D1)** —
  ⚠ these are **single-name whole-path** figures on a **near expiry**, not the 08-26 event, and they
  are **recorded as context and explicitly NOT used to set the threshold** (the D28 separation).
- **Information content (L3): HIGH on B, MEDIUM on A.** ⚠ **Anti-signal, registered**: **a separate
  <=48h macro binary on 2026-08-26/27 ⇒ AMBIGUOUS**, because a macro shock counterfeits a readthrough.
  ⚠ A print date moved by the company, or a trading halt on 08-27 ⇒ **VOID.**
- ⚠ **Correlated with `S79` by construction** — if both fire the same direction that is **one event
  read twice**, not two confirmations.
- **Owner**: `industry_US`.

### S82 — ★★★ Is HEALTH CARE an idiosyncratic med-tech leg, or the FOURTH leg of the duration complex we are UW three times? · ARMED · → settle **2026-08-20**

**Why it exists — two lenses of the SAME pre-mortem reached opposite conclusions about one sector, and
this row is the disagreement made scoreable.**
- **Lens 1 / Lens 4**: HLTH is **rank 2 on both flow axes with the tightest cap-vs-equal gap of 11
  (0.011)**, **19 of 32 at `OBV 매집 ∧ RS20>0` (highest rate)**, **2 red of 32**, `XLV` **the only sector
  positive on exc5/exc20/exc60**, and **the book owns 0.00% of it** while the registry does not even
  list it ⇒ **a zero-exposure rank-2 cycle.**
- **Lens 2**: `XLV`'s excess-vs-SPY correlation with EW{XLU,XLRE,XLP} is **0.67 (252d) / 0.81 (60d)**,
  and with `TLT` excess **0.48 / 0.64** ⇒ **HLTH is the duration factor**, so the N+ is the fourth leg
  of a complex the desk is **underweight on three legs of**, and `XLV` exc60 **+11.58** may not be
  cited as evidence for it because **that tape IS the factor.**

**Frozen observable**: **[`XLV` 5-session excess vs `SPY`] MINUS [equal-weight {`XLU`,`XLRE`,`XLP`}
5-session excess vs `SPY`]**, from the **2026-08-13 settled close** to the **2026-08-20 settled close**.

| Branch | Threshold | Meaning |
|---|---|---|
| **A** | **>= +2.45pp** | HLTH **decouples upward** from the duration complex ⇒ it is an **idiosyncratic med-tech/tools leg**; the N+ is independent of the three UWs and the zero-exposure GAP is real |
| **B (the adversarial ask)** | **<= −1.62pp** | HLTH moves **with** the complex ⇒ **Lens 2 is right**, the N+ contradicts the UWs, and the tilt set is internally inconsistent |
| **C** | between | Neither decomposition survives on this window |

- ★ **D93 executed BEFORE freezing**: trailing **252** settled sessions to 2026-08-12 —
  **mean +0.414pp · sd 2.065pp · p85 +2.299 · p15 −1.578.** Bands at **mean ± 1.0σ**
  (A +2.45 ~ p85+, B −1.62 ~ p15). ⚠ **Centre +0.414, not zero — disclosed.**
- **State at registration**: **+3.091pp** ⇒ ⚠⚠ **ALREADY ABOVE BRANCH A. Disclosed at registration
  rather than discovered at scoring** — **branch B is the adversarial ask**, and a scorer must not
  read an A-fire as a surprise.
- **Implied move**: `XLV` **±1.5%**, expiry **2026-08-14 (D1)**, P/C 0.80 = neutral. **A 5-session
  2.45pp SPREAD BETWEEN TWO BASKETS is outside it** ⇒ the threshold carries information.
- **Information content (L3): HIGH — the highest on this board today.** ★ It is the only row that can
  settle a disagreement **inside this desk's own pre-mortem**, and **either branch changes a
  conclusion**: A validates a promoted 5th DEEP slot and a real cycle GAP; B says the desk is
  simultaneously N+ and UW the same factor.
- ⚠ **Correlated-tail flag**: **B here and A in `S80` are the same underlying event** (the duration
  complex rallying and dragging XLV with it). **If both fire, that is ONE regime read, not two.**
- **Invalidation (D149)**: a market-wide halt, or an index reconstitution altering `XLV`'s or any
  complex ETF's constituents inside the window ⇒ **VOID.**
- **Owner**: `industry_US`.

### S83 — ★★ The book holds ANET and HPE as one AI-compute position. Are they? · ARMED · → settle **2026-08-20**

**Why it exists.** **PREMORTEM Lens 3 tagged `HPE` EXHAUSTED and `ANET` EXTENDED-BUT-LIVE — both held,
both filed under the same theme label.** Measured: `HPE`'s consensus has been **flat for 60 days**
(current-Q 0.92 -> 0.93; FY 3.41 -> 3.42; **30-day revision breadth 1up/1down on current-Q, next-Q AND FY**),
its `vol_surge` is **0.64**, and **OBV (+0.318) is the only axis still arguing for it — a grade-C axis
(D6)**. `ANET` on the same day carries **3up/0down on all four buckets** with a **+17.9% current-quarter
jump inside 7 days**. ⚠ **`HPE` is additionally NOT in the cycle registry's AI-compute epicentre list**,
so the deterministic GAP check scores it as nothing while it carries **rs60 +73.1**, the highest
60-day RS of any unregistered accumulator.

**Frozen observable**: **[`ANET` 5-session excess vs `SPY`] MINUS [`HPE` 5-session excess vs `SPY`]**,
from the **2026-08-13 settled close** to the **2026-08-20 settled close**.

| Branch | Threshold | Meaning |
|---|---|---|
| **A** | **>= +7.16pp** | The live/exhausted split is real ⇒ **the AI-compute leg is not one position** and the theme label is grouping two different objects |
| **B** | **<= −9.68pp** | The split is **backwards** — HPE is the live end and the revision-breadth read was the wrong instrument for this pair |
| **C** | between | The pair moves together ⇒ **the label is right and Lens 3's split is not observable at this horizon** |

- ★ **D93 executed BEFORE freezing**: trailing **252** settled sessions to 2026-08-12 —
  **mean −1.260pp · sd 8.417pp · p85 +6.072 · p15 −7.599.** Bands at **mean ± 1.0σ.**
- ⚠⚠ **DISCLOSED WEAKNESS, at registration rather than at scoring: sd 8.417pp is the widest estimator
  on this desk's board.** A single-name **pair** spread is intrinsically noisy ⇒ **branch C is the
  heavy favourite and neither tail is cheap.** It is registered anyway because **the desk currently
  sizes ANET and HPE as one theme and no row on the board tests that.**
- **State at registration**: **−3.781pp** ⇒ inside C, leaning toward B.
- **Implied move**: `ANET` **±3.0%** · `HPE` **±4.2%**, both **2026-08-14 (D1)**. **A 5-session 7.16pp
  PAIR SPREAD exceeds both** ⇒ outside what is priced.
- **Information content (L3): MEDIUM**, and stated as medium rather than inflated. **A** changes how
  the book's theme cap groups these two (the `D9`/`risk_units` question in its book face); **B** would
  retire the revision-breadth instrument for this pair; **C** is modal and teaches least.
- **Invalidation (D149)**: an M&A announcement, a guidance withdrawal or an index deletion at either
  name ⇒ **VOID, not scored.** ⚠ **`HPE`'s next earnings print falling inside the window ⇒ VOID** —
  the row tests carry, not an event.
- **Owner**: `industry_US`.


---

## Registered 2026-08-14 by the `industry_US` PREMORTEM (S84 – S87)

> ⚠ **ID 3-grep at WRITE time (D137 / D76)** across all seven files (`SCENARIOS*.md` ×3,
> `STANDING_VIEW*.md` ×3, `RESEARCH.md`): `S84` `S85` `S86` `S87` returned **0 hits in all seven**;
> highest existing was **S83 (US) / S61-KR (KR)**.
> ★ **Every band measured on the estimator's own trailing-252 distribution (D93) BEFORE freezing.**
> ★ **Every row states its SETTLEMENT MODE explicitly — the first application of `D242`'s remedy.**
> ⚠⚠ **Implied-move disclosure, and it is a LIMIT not a check**: `module_flow --positioning` returned
> `XLU ±0.7% · XLE ±1.9% · NVDA ±1.2% · COHR ±3.8% · MU ±2.1%`, **all at expiry 2026-08-14, `D0`**.
> A D0 straddle prices the remainder of one session, so it is a **FLOOR on a 5-session implied move,
> not an estimate**. ⇒ **no threshold below is claimed to sit outside what is priced.**

### S84 — ★★★ The MANDATORY Hormuz both-sides bracket: the SPREAD no existing row measures · ARMED · → settle **2026-08-21**

**Frozen observable**: `[XLE 5-session excess vs SPY] − [EW{XLU, XLRE} 5-session excess vs SPY]`,
settled daily closes, `yfinance`, `auto_adjust=False`, benchmark **`SPY` named inline (C1)**.
**State at registration (2026-08-13 settled): +3.880.**

| Branch | Threshold at the 2026-08-21 settle | Meaning |
|---|---|---|
| **A (AGAINST US)** | **≤ −3.174** (measured p15, base rate **15.1%**) | Hormuz de-escalates ⇒ ENRG's only positive `wflow` compresses **while** the duration underweights rip. **One headline falsifies ENRG OW− and helps UTIL UW · RE UW · STPL UW− · IT N+ at once** |
| **B (with us)** | **≥ +5.544** (measured p95, base rate **5.2%**) | Escalation extends a premium already at its own 85th percentile |
| **C** | between (~80%) | Modal. No conclusion changes |

- **D93**: trailing-252 mean **+0.634** · sd **3.474** · p15 **−3.174** · p85 **+3.899** · p95 **+5.544**.
- ★ **Branch B is at p95, NOT p85, and the reason is disclosed**: the state **+3.880** already sits
  **at p85 (+3.899)**, so a p85 branch would fire on **no move** (`D122` zero-information class).
  **The 15.1% / 5.2% asymmetry is stated, not hidden.**
- **Settlement mode: TERMINAL bar only, both branches.**
- **Information content (L3): HIGH and asymmetric — A falsifies two live tilts; B only confirms.**
- **Anti-signal**: a **non-Hormuz** energy event dominating the window (OPEC emergency meeting, SPR
  action) evidenced by a filing or two independent outlets ⇒ **`AMBIGUOUS`**, not scored.
- ⚠ **Post-registration tracking, NOT scoring** (`MACRO §5-2`): the first 08-14 input —
  *"UAE accuses Iran of attacks on two ADNOC vessels in Strait of Hormuz"* [`aljazeera` 08-14] —
  favours **branch B**. **The band is NOT moved and the row is NOT re-dated.**
- **Owner**: `industry_US`.

### S85 — ★★★ The falsifier for the SAME RUN'S IT promotion, on the axis the promotion used · ARMED · → settle **2026-08-21**

**Why it exists.** ROTATION promoted **IT N → N+** on 2026-08-14 on one argument: *`eqflow` flipped
positive (−0.100 → +0.034), so the median IT name turned.* **`P52`'s anti-signal uses `XLK`, which is
cap-weighted and therefore cannot distinguish the median name from `NVDA`.**

**Frozen observable**: `RSPT` (equal-weight technology) **5-session return minus `XLK` (cap-weighted
technology) 5-session return**, in percentage points, settled closes.
**State at registration (2026-08-13): +1.980.**

| Branch | Threshold at the 2026-08-21 settle | Meaning |
|---|---|---|
| **A (AGAINST US)** | **≤ −0.994** (measured p15, base rate 15.1%) | Cap-weight reasserts ⇒ **the IT N+ was a megacap artifact and the `eqflow` flip was one session of noise.** Also the branch a **front-end rate shock** would produce |
| **B (with us)** | **≥ +2.046** (measured p95, base rate 5.2%) | Breadth extends beyond an already-extreme state |
| **C** | between | No conclusion changes |

- **D93**: mean **+0.226** · sd **1.221** · p15 **−0.994** · p85 **+1.446** · p95 **+2.046**.
- 🚨 **Disclosed at registration**: **STATE +1.980 is ALREADY ABOVE p85** ⇒ **the IT promotion was made
  at the 85th–95th percentile of the very estimator that justifies it.** Branch B is therefore
  **near-degenerate**; **branch A is the informative one**, which is the correct shape for a falsifier
  of the desk's own call.
- **Settlement mode: TERMINAL bar only.** **Anti-signal**: an `RSPT`/`XLK` reconstitution ⇒ **`VOID`**.
- **Owner**: `industry_US`.

### S86 — ★★ The optical / interconnect layer: the desk's maximum flow score, with zero exposure · ARMED · → settle **2026-08-21**

**Frozen observable**: `EW{COHR, LITE, CIEN} 5-session excess vs SPY`, settled closes.
**State at registration (2026-08-13): +2.997.**

| Branch | Threshold at the 2026-08-21 settle | Meaning |
|---|---|---|
| **A (a real new leg)** | **≥ +12.584** (p85) | The turn extends ⇒ a genuine un-owned leg of the AI build-out — and **the cycle registry has no entry for it** |
| **B (a bounce in a downtrend)** | **≤ −5.948** (p15) | RS60 (−15.1 / −5.8 / −20.9) was the honest window and RS20 was noise |
| **C** | between (~70%) | No conclusion changes |

- **D93**: mean **+3.276** · **sd 8.998 — the widest estimator on this board, DISCLOSED ⇒ C is the
  heavy favourite.** Registered anyway because the desk holds **2 of its 6 admissible 🟢 here with no
  position, no tilt and no registry entry.**
- ⚠ **Adversarial note in the row**: `COHR` short interest **5.4% of float and BUILDING** (DTC 1.9).
  **Crowded-short is turn-conditional squeeze fuel, never a buy signal alone (D6).**
- **Settlement mode: TERMINAL bar only.** **Owner**: `industry_US`.

### S87 — ★★ Are the book's biggest runners EXTENDED-BUT-LIVE or EXHAUSTED? · ARMED · → settle **2026-08-21**

**Frozen observable**: `EW{DELL, HPE} 5-session excess vs SPY`, settled closes.
**State at registration (2026-08-13): +12.331.**

| Branch | Threshold at the 2026-08-21 settle | Meaning |
|---|---|---|
| **A (EXHAUSTED)** | **≤ −4.961** (p15) | The ~90th-percentile state mean-reverted ⇒ PREMORTEM Lens 3's EXTENDED-BUT-LIVE tag was wrong |
| **B (EXTENDED-BUT-LIVE)** | **≥ +16.143** (p95) | The runners extend from an already-extreme state |
| **C** | between | No conclusion changes |

- **D93**: mean **+2.248** · sd **8.429** · p15 **−4.961** · p85 **+7.734** · p95 **+16.143**.
  **STATE +12.331 sits between p85 and p95** ⇒ **branch A is the informative one.**
- ⚠ **`HPE` is ALSO an `S83` object** (ANET−HPE, settles 08-20). **The observables are different and
  NEITHER row is re-frozen** — if they disagree, **the disagreement is the finding** (S14-ANNEX /
  S35-ANNEX precedent).
- **Settlement mode: TERMINAL bar only.** **Owner**: `industry_US`.

---

## Registered 2026-08-15 by the `industry_US` run (PREMORTEM) — **S88 – S91**

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, held.
> ⚠ **ID 3-grep at WRITE time (D137)**: highest existing **S87** (US, `SCENARIOS_US.md`) /
> **S61-KR** (KR) ⇒ this run takes **S88–S91**. All four indexed in the `SCENARIOS.md` MASTER INDEX.
> All prices settled **2026-08-14**, benchmark **`SPY` named inline (C1)**. Bands are 2-year
> distributions of the observable itself (**n=496 sessions**, D93), with the **state's own percentile
> disclosed at registration**. **SETTLEMENT MODE = TERMINAL on both branches** for all four (D242).

| ID | Status | Observable (frozen) | Branch A | Branch B | Settle | State at registration | Anti-signal (VOID) |
|---|---|---|---|---|---|---|---|
| **S88** | **ARMED** | `EW{MPC, VLO, PSX}` **5-session excess vs `SPY`** | **≤ +0.061** (2y median) — *falsifies the 08-15 ENRG OW promotion* | **≥ +8.144** (p95) — *promotion confirmed* | **2026-08-21** | **+15.698 = 100th %ile of 2 years** · band mean +0.444 sd 4.726 p15 −4.220 p50 +0.061 p95 +8.144 | US refinery outage or PADD3 hurricane in window ⇒ domestic supply, not Hormuz/Russia |
| **S89** | **ARMED** | `NEM` **5-session excess vs `SPY`** | **≤ −5.217** (p15) — *exhaustion confirmed* | **≥ +9.658** (p95) — *the run is live* | **2026-08-21** | **+3.833 = 70th %ile** · mean +0.690 sd **6.056** p15 −5.217 p50 +1.100 p95 +9.658 | gold price move beyond ±8% over the window ⇒ bullion read, not a name read |
| **S90** | **ARMED** | `DLR` **5-session excess vs `SPY`** | **≤ −3.199** (p15) — *the RE accumulation was late* | **≥ +5.223** (p95) — *genuinely early* | **2026-08-21** | **+2.878 = 84th %ile** · mean −0.016 sd 3.436 p15 −3.199 p50 +0.155 p95 +5.223 | `DLR`-specific acquisition or guidance event ⇒ name event, not node read |
| **S91** | **ARMED** | `XLY` **5-session excess vs `SPY`** | **≤ −2.467** (**p05**) — *consumer deterioration persists* | **≥ +1.553** (p85) — *it was a one-print reaction* | **2026-08-21** | **−1.783 = 14th %ile** · mean −0.060 sd **1.639** p05 −2.467 p15 −1.737 p50 −0.155 p85 +1.553 p95 +2.841 | a September-FOMC-dated headline or an inflation print in window ⇒ the rate leg is confounded |

### Information grading, performed BEFORE the events (lens B4) — and the implied-move check

| ID | Implied move (`module_flow --positioning`) | Grading |
|---|---|---|
| **S88** | `MPC` **±4.4%**, expiry **2026-08-21, D6** | **A carries the row**: it needs a **−15.6pp** move in the spread, far outside the implied move. **B tolerates only −7.6pp ≈ 1.7× the implied move ⇒ B is declared NO-INFORMATION at registration**, not presented as a trigger. Registered anyway because A is precisely the outcome that falsifies a promotion made at the 100th percentile of its own expression |
| **S89** | `NEM` **±5.5%**, expiry **2026-08-21, D6** | **A needs −9.05pp ⇒ outside ⇒ informative.** **B needs +5.83pp ⇒ marginally outside ⇒ WEAK-information, labelled now.** ⚠ sd 6.056 is the 2nd-widest estimator this desk has registered ⇒ **C is the favourite and that is disclosed at registration** |
| **S90** | 🚨 **NOT PULLED** — `--positioning` was run for `MPC`/`NEM`/`LMT` only | **The threshold is distribution-based, not options-based, and the gap is stated rather than glossed.** ⚠ **B requires only +2.35pp from an 84th-%ile state ⇒ weak-information** |
| **S91** | not pulled (sector ETF) | **The most informative row registered today**: `sd 1.639` is the **narrowest** estimator on this desk's board, so **both branches are reachable**. ⚠ **Branch A was set at p05 rather than the customary p15 because the state (+p14) already sat below p15**, which would have made branch A zero-information. **The substitution is disclosed at registration** |

### Registered and then DROPPED, with the reason (rather than bracketed to look thorough)
- **Navy shipbuilding / foreign-yard opening** (EVENT_ALPHA Card 1, `reuters`/`investing_en`
  08-14/08-15): **neither branch would change a conclusion.** The named beneficiaries are
  **foreign-listed** (Hanwha, Fincantieri); the pure-play US Navy shipbuilder **`HII` is not in
  `us_top300`** and has no reading on this desk; and an `EW{LMT,GD}` observable (state +1.840, 75th
  %ile) would be dominated by general defense flow rather than by the policy. **Kept as a watch KPI
  instead**: `GD` RS20 vs `SPY`, currently **+2.9**, dated re-check **2026-08-21**.

### ⚠ A structural note that binds the 08-21 scoring of `S84` (registered 08-14) and is written NOW
`S84` tests **Hormuz transit risk only**. EVENT_ALPHA Card 3 established that the refining node has a
**second, independent mechanism** — **Russian refinery capacity destruction** (Gazprom's 200,000-bpd
Salavat refinery struck 08-13; a fuel terminal 08-14; Russia's diesel exports at a **multiyear low**)
— which a Hormuz reopening **cannot falsify**. ⇒ **If `S84` fires branch A while the crack holds, that
is NOT a falsification of the refining thesis.** `P62`'s KPI (`HO=F` 20d return minus `CL=F` 20d
return, **+5.48pp** at registration, direction A holds above **+4pp**) carries the second mechanism.
**Both must be read together on 08-21; neither alone settles the node.**
★ And `S84`'s own live state is **+6.545 — already 1.00pp ABOVE branch B** with four sessions to run,
so **branch B is near-zero information** and branch A is the row's entire content. **No threshold is
moved** (D242).

---

# Registered 2026-08-16 by the `industry_US` PREMORTEM ??`S92` 쨌 `S93` 쨌 `S94`

> ID 3-grep at registration across `SCENARIOS.md` 쨌 `SCENARIOS_US.md` 쨌 `SCENARIOS_KR.md` 쨌
> `llm_outputs/` 쨌 `REPORT/`: highest existing **S91** (suffixed: `S63-KR`) ??this run takes **S92?밪94**.
> All observables and thresholds **frozen at registration**. Benchmark `SPY` named inline (C1).
> Prices settled **2026-08-14**, one provider (`yfinance`, `auto_adjust=False`).

## S92 ???끸쁾??The MANDATORY Hormuz bracket, WIDENED to the branch that can actually falsify us 쨌 ARMED 쨌 ??settle **2026-08-31**

**Why it exists.** `CATALYST_WATCH.json` carried exactly one ??binary in window ??*"Iran 'Strait of
Hormuz open' statement (TACO trigger), axis=oil, **undated**"* ??and this run's #1 sector tilt
(**ENRG OW**) is a one-way tilt into it. **`S8` has been `[blank]`-dated for 14 consecutive runs and
cannot serve.**

??**B4 applied BEFORE registration, and it changed the bracket's shape.** Graded by information
content, the Hormuz binary **alone** is not worth bracketing:

| Branch | What it can do to the thesis |
|---|---|
| Hormuz OPENS / Iran accommodation | Kills the **war-premium** leg. ??**Leaves the Russia supply-destruction leg (`P66`) intact** ??Salavat is still down, Russia still importing Indian fuel, diesel exports still at a multiyear low ??**confirm-only** |
| Hormuz CLOSES / US declares territory | Confirms the war-premium leg **and** the crack leg together ??**also confirm-only** |
| ??**The falsifier neither branch contains** | **A US-brokered halt to Ukrainian strikes on Russian energy infrastructure** |

??**The bracket is two-dimensional by construction.**

| Branch | Frozen observable |
|---|---|
| **A (escalation)** | A dated US action on the Strait (declaration / escort regime / interdiction) reported by **?? independent foreign outlets** by **2026-08-31**, **AND** `CL=F` settled close **> 82.40** (the 08-14 close) |
| **B (de-escalation)** | `CL=F` settled close **< 78.00** on any session through 08-31 with **no** dated US action. ??**`P66`'s Russia leg SURVIVES this branch** ??recorded at registration so B is not over-read |
| **??C (the falsifier)** | A **US-brokered halt to Ukrainian strikes on Russian energy infrastructure** reported by **?? independent foreign outlets** by 08-31. **The only branch that breaks the Energy OW's stated mechanism** |
| **D** | none of the above ??no information |

**State at registration**: `CL=F` **82.40** (08-14 close) 쨌 `WTI` spec **18th percentile SHORT** (COT,
Tue **08-11**, i.e. **before** the 08-14 Trump statement) 쨌 `Hormuz` term velocity **1.15횞** vs `Iran`
**0.88횞** 쨌 branch C's **first datapoint already on the board**: *"Kyiv stops strikes on Russian port
after request from JD Vance"* [`semafor` **2026-08-12**].

**?슚 Anti-signal**: an **OPEC+ production decision** inside the window makes the barrel
non-attributable ??branches A and B are **VOID**; branch C scores independently.
??**Threshold provenance (C5)**: 78.00 / 82.40 are the 08-14 close **짹??%**, chosen because `MPC`'s
implied move is **짹4.4% (expiry 2026-08-21, D5)** ??a bracket must sit **outside** what is priced.

?슚 **POST-REGISTRATION ADDENDUM, same run (DRIFT, ~23:35 KST) ??no threshold moved.** DRIFT body-read
two items **not** in this run's MACRO 짠D: ***"Iran, Oman home in on Hormuz Strait deal as ship attacks
mount"*** [`fortune` **2026-08-15**] and *"Iran war live: **Talks on Hormuz Strait continue**"*
[`aljazeera` **2026-08-16**]. ??**Branch B now has a named mediator and a live negotiation.** That is
information about branch B's **probability**, **not** about its threshold ??the threshold stands frozen
(`D242`). Recorded here rather than in a rewrite of the row above.

## S93 ???끸쁾 The consumer complex: is the split ONE factor or TWO? 쨌 ARMED 쨌 ??settle **2026-08-21**

**Why it exists.** PREMORTEM Lens 1 promoted `CONSUMER` (DISC ??STPL) to a **5th DEEP slot over
ROTATION's own decline**. Three dated prints land inside the window and **`catalyst_calendar --days 5`
carried NONE of them** (`[EARNINGS] (none in window)`).

| Branch | Frozen observable ??settled closes, 5-session excess vs **`SPY`**, 2026-08-14 ??2026-08-21 |
|---|---|
| **A (one factor ??"the consumer is rolling")** | `WMT` **and** `HD` **and** `TGT` all post **negative** 5-session excess vs `SPY` |
| **B (two factors ??the label is the wrong object, `W5`)** | `TGT` **positive** while **both** `WMT` and `HD` are negative, **OR** `ABNB` ??`HD` 5-session excess spread vs `SPY` **> +5pp** |
| **C** | any other combination ??no information |

**State at registration (2026-08-14 settled)**: `WMT` ?윞 RS60 **??9.913** vs `SPY` 쨌 `HD` **?뵶遺꾩궛**,
exc5 **??.111** 쨌 `TGT` ?윞 **OBV 留ㅼ쭛**, exc20 **+6.213** / exc60 **+15.601** 쨌 `COST` ?뵶遺꾩궛, exc60
**??7.981** 쨌 `ABNB` **?윟媛??*, exc20 **+21.639** / exc60 **+34.525**. **`ABNB` ??`HD` spread = +8.077pp.**
**??Implied move taken from the options market, not from judgement**: `WMT` **짹5.0% (expiry 2026-08-21,
D5)** ??it **covers** the print. `WMT`'s single-name threshold is therefore **not** used; the bracket
rests on **cross-sectional sign agreement**, which the straddle does not price.
**?슚 Anti-signal**: a **tariff announcement affecting consumer goods** inside the window ??**VOID**.

## S94 ???끸쁾??The cycle registry cannot see the cycles this desk finds 쨌 ARMED 쨌 ??settle **2026-08-31**

**Why it exists.** PREMORTEM Lens 4 measured that `data_build/cycles/cycle_registry.json` is **29 days
stale**, its rank-3 floor is **0.0** (check OFF), and it has **no entry** for **optical/interconnect**
or **custom AI silicon** ??while `COHR` (flow **+0.99**, the board's top score) and `LITE` (+0.817) are
the **only two admissible ?윟 in Information Technology** and the book holds **neither**.
??**The instrument built to prevent "zero exposure to a live cycle's epicenter" returns ??because it
has nothing to compare against.** This is the 2026-07-14 postmortem's failure mode reproduced
**structurally**, not by judgement.

| Branch | Frozen observable |
|---|---|
| **A (the gap was real)** | At the **2026-08-31** settle, the equal-weight 5-session excess of **`COHR` + `LITE`** vs **`SPY`** is **> +3pp**, **AND `vol_surge` ??1.0 on both names**, **while** `cycle_registry.json` still carries **no** optical/interconnect entry |
| **B (the registry's silence was right)** | The same equal-weight excess is **< ??pp** ??the desk was not missing a cycle; the greens were print-reaction volume |
| **C** | between 짹3pp ??no information |

**State at registration**: `COHR` RS20 **+12.9** / RS60 **??3.7** vs `SPY`, `vol_surge` **1.67**, and it
**round-tripped ??4.06% in the five sessions to 08-14, closing below its own 332.48 trigger** 쨌
`LITE` RS20 **+21.9** / RS60 **??.8**, `vol_surge` 1.27, and it **held** its move. **Both are TURN
shapes, not runners.**
**?슚 Anti-signal**: ??**both greens are dated to their own 08-11/08-12 earnings prints** ??if the
window's move is still inside the print-reaction volume decay, branch A is **confounded** ??which is
why the **`vol_surge` ??1.0 conjunction is written into branch A at registration**, not discovered
afterwards.
??**This bracket does NOT promote either name.** It tests the **registry**, a human-maintained file (P5).


---

## Registered 2026-08-17 by the `industry_US` run (PREMORTEM) — **S95 – S98**

> ⚠ **ID note (D76 collision class, greps at WRITE time)**: `grep -r "S9[5-8]\b"` run across
> `handoff/*.md` · `llm_outputs/` · `REPORT/` returned **0 registrations in every markdown file**;
> highest existing was **S94 (US) / S63-KR (KR)** ⇒ this run takes **S95–S98**. All four indexed in the
> `SCENARIOS.md` MASTER INDEX.

### S95 — ★★★ The MANDATORY D-0 bracket: the 60-day US–Iran MoU expired 2026-08-17 and **no existing row is keyed to that date** · ARMED · → settle **2026-08-21**

**Why this row exists.** `CATALYST_WATCH` (pulled 22:1x KST 08-17) carried only `NVDA` 08-26 and an
**undated** Hormuz statement. The **60-day US–Iran ceasefire / MoU expired TODAY**, corroborated by
5 independent outlets — `yahoo_finance` "US Equity Futures Mixed Pre-Bell as 60-Day US-Iran Ceasefire
Expires" · `aljazeera` "US-Iran Memorandum of Understanding expires: How and why it fell apart"
(9,981-char body) · `bloomberg` "Trump Issues Threat to Oman as US-Iran MOU Expires" · `cnbc`
"Strait of Hormuz shipping grinds to a halt ahead of U.S.-Iran ceasefire expiry" · `oilprice`
"Hormuz Tanker Traffic Slows to a Trickle". `S74` (08-24), `S84` (08-21) and `S92` (08-31) bracket
**Hormuz reopening**; none is keyed to the **expiry date**, which was unknown at their registration.
`S8` has carried this same object **undated for fifteen runs**.

| | |
|---|---|
| **Observable** | `BZ=F` (Brent front-month) settlement price |
| **Branch A** | **≥ 93.00** — the shutdown finally reprices the barrel |
| **Branch B** | **≤ 86.50** — de-escalation / covert flows win; the ENRG premium is equity-only |
| **Branch C** | **86.50 – 93.00 = NO-INFORMATION, declared at registration and the FAVOURITE** |
| **State at registration** | 08-11 **88.91** → 08-14 settle **88.52** (−0.44%) → 08-17 live intraday 88.84. **Realised 4-session range 87.07–88.98 = a 2.2% band** |
| **Settle** | **2026-08-21** |
| **Implied-move check** | `MPC` **±4.3%** (expiry 08-21, **D4**), P/C 0.81, skew **+38.9**. Branch A needs **+5.1%** on Brent ⇒ **outside** ⇒ informative. Branch B needs **−2.3%** ⇒ **inside** ⇒ **WEAK-INFORMATION, labelled now** |
| 🚨 **Anti-signal** | A **US refinery outage, PADD3 hurricane landfall, or an OPEC+ quota decision** inside the window makes any crude move non-attributable to Hormuz ⇒ **VOID**, not scored favourably |

★ **What this row buys.** Four settled sessions of escalation produced **Brent −0.44% / WTI −0.96%**
while `XLE` beat `SPY` by only **+0.86pp**. ⇒ The live question is not "does closure spike crude" but
**"has the equity complex priced a premium the commodity has not?"** — and both branches answer it.

### S96 — ★★ The 5th DEEP's own falsifier: is the optical/interconnect layer EARLY or LATE? · ARMED · → settle **2026-08-21**

**Why.** Three mutually independent instruments selected one sub-node today — `theme_age optical`
**1.74×** (highest of 13 probes), `burst` **`OPTOELECTRONICS` z 5.7** (vocabulary-free), a **BUILDING**
thread "Lightmatter sets optical interconnect blueprint as AI hits copper wall" (2→2→2), and
`sector_flow`'s **#1 and #2 `flow_score` board-wide** (`COHR` +0.99 · `LITE` +0.82, both 3-axis
admissible). PREMORTEM promoted IT as a 5th DEEP on that convergence. **This row is the promotion's
falsifier, registered in the same breath.**

| | |
|---|---|
| **Observable** | `EW{COHR, LITE}` 5-session excess return vs **`SPY`**, plus the thread's daily outlet count |
| **Branch A** | **≥ +5.0pp** *and* the Lightmatter thread reaches **≥4 outlets** on any single day ⇒ bought, not just written about |
| **Branch B** | **≤ −5.0pp** ⇒ the 20-day excess was print-reaction volume; the promotion was late |
| **Branch C** | between |
| **State at registration** | `COHR` rs5 **−14.46** / rs20 +12.93 / rs60 **−13.67** · `LITE` rs5 +3.64 / rs20 **+21.93** / rs60 **−1.76** — **both have NEGATIVE-to-zero 60-day excess; only the 20-day window flatters them** |
| **Settle** | **2026-08-21** |
| **Implied-move check** | 🚨 **NOT PULLED** — `--positioning` was run for `MPC`/`VLO`/`TGT`/`LHX` only. **The gap is stated rather than glossed.** ⚠ σ20d is **8.43%** / **7.55%**, the two widest on the sheet ⇒ ±5pp is inside one week's noise ⇒ **both branches reachable but C is likely** |
| 🚨 **Anti-signal** | An `NVDA`-dated announcement (08-26 print) naming optical ⇒ the layer reprices on a **headline** event, which is the opposite of the chain-hop premise ⇒ **VOID** |

### S97 — ★★ `LHX` succession: a discontinuity, or an orderly insider handover? · ARMED · → settle **2026-08-21**

**Why.** `burst` surfaced **`KUBASIK`** as a new word at a **0% 30-day baseline**; the body-read
inverted the naive reading — **CEO Christopher Kubasik stepped down, insider Sam Mehta appointed, stock
down**, 4 outlets, all 08-17. `M704` had measured `LHX` as the **only** name negative on both 20d and
60d inside the defense EW that closed `D249`, and its FINRA short-z was **+1.86 🔴 building** on
**2026-08-14 — three days before the announcement**.

| | |
|---|---|
| **Observable** | `LHX` 5-session excess return vs **`SPY`** |
| **Branch A** | **≤ −4.0pp** ⇒ priced as a discontinuity; `M704`'s defense EW must be re-run **ex-`LHX`** |
| **Branch B** | **≥ 0** ⇒ orderly succession; the short-z build was hedging noise |
| **Branch C** | between |
| **State at registration** | rs5 **+1.40** · rs20 **−0.97** · rs60 **−11.11** vs `SPY` (settled 08-14) — ★ **already broken BEFORE the news** |
| **Settle** | **2026-08-21** |
| **Implied-move check** | **±3.7%** (expiry 08-21, D4), P/C 0.70, **skew +0.0 = NEUTRAL**. Branch A needs −4.0pp ⇒ **marginally outside** ⇒ informative. ★ **A zero skew on a name that lost its CEO the same day is itself the anomaly**, and is registered as this row's most interesting input |
| 🚨 **Anti-signal** | A **DoD contract award or defense-budget headline** naming `LHX` inside the window ⇒ the move is not about succession ⇒ **VOID** |

### S98 — ★★★ Is the underweight FOUR legs of ONE duration bet — and was its stated cause already retracted? · ARMED · → settle **2026-08-20**

**Why.** The desk is **UW Utilities · UW Real Estate · UW− Staples**, which `S80` (08-19) brackets as
one duration bet, and `S82` (08-20) asks whether **Health Care** is a fourth leg. 🚨 **`R73` withdrew
the mechanism underneath all of them**: the underweight was written under "the long end is repricing
term premium with `DGS2` pinned", and `DGS2` **fell 10bp** (4.25 → 4.15) while `DGS30` itself fell —
a **bull steepener**, which is a *tailwind* for regulated utilities and long-duration REITs. This row
scores the four-leg question as one object rather than four.

| | |
|---|---|
| **Observable** | Sign of the 5-session excess vs **`SPY`** for `XLU`, `XLRE`, `XLP` and `XLV`, at settle |
| **Branch A** | **All four carry the same sign** ⇒ one bet wearing four GICS labels; `R73`'s retraction applies to all four at once |
| **Branch B** | **The four split in sign** ⇒ four separate calls; `S80`'s three-leg framing was already the right granularity |
| **Branch C** | a 3–1 split |
| **State at registration** | `XLU` exc5 **+1.207** (2nd best of eleven) while `UTIL` `wflow` is the **worst of eleven** at −0.445 — price and flow already disagree inside one leg |
| **Settle** | **2026-08-20** (the later of `S80` 08-19 and `S82` 08-20) |
| **Implied-move check** | Sector-ETF object, no straddle. ⚠ The threshold is **sign agreement, not magnitude** ⇒ immune to the implied-move objection **at the cost of low resolution** — stated at registration |
| 🚨 **Anti-signal** | An **FOMC-dated communication or a CPI/PPI print** inside the window drives all four together for a reason that is not the duration structure ⇒ **VOID** |

★ **Information-content grading (B4), applied before the events**: `S98` is the highest-information row
this run registered — **neither** outcome is predictable from anything the desk currently holds, and
branch A would retire a four-sector tilt whose stated cause is already half-retracted.

---

## S99 — ★★★ Is `ETN` an Industrials position, or the book's 5th AI-compute unit? · ARMED · → settle **2026-08-21**

Registered **2026-08-19 by the `industry_US` PREMORTEM (Lens 2)**. IDs checked at WRITE time against
every row in all three `SCENARIOS*.md`, both `STANDING_VIEW*.md`, `llm_outputs/` and `REPORT/`
(D137/D76/M319): `grep S99` returned **0**; highest existing **S98 (US) / S64-KR (KR)**.

**Why it exists.** No live row carries `ETN` (only a settled 08-07 {EMR,ETN,AME,PWR}−`XLU` spread);
`S81`/`S83`/`S87` use {AVGO,ANET,HPE}/{ANET,HPE}/{DELL,HPE} **without** it, and **G4 has failed 10
consecutive runs on exactly this grouping question** (250d splits `ANET`↔`ETN`; 500d/750d merge them).
Measured this run: **`ETN`–`ANET` raw 60d correlation +0.722 — higher than `AVGO`–`ANET` (+0.596) and
`NVDA`–`AVGO` (+0.495) — while `ETN`–`RTX` raw is −0.040.** ⇒ the Industrials OW−'s "diversifying leg"
may trade as AI-compute.

**Frozen observable**, settled closes, `yfinance auto_adjust=False`, benchmark **`SPY`** inline,
window **2026-08-14 close → 2026-08-21 close**:
`M` = EW{`ANET`,`AVGO`,`HPE`} 5-session excess vs `SPY` · `E` = `ETN` 5-session excess vs `SPY`.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (AGAINST US)** | \|M\| ≥ **3.0pp** ∧ sign(E)=sign(M) ∧ \|E\| ≥ **1.5pp** | Industrials OW− contains a **5th AI-compute risk unit**; the book's AI concentration is **5 of 12, not 4 of 12** |
| **B (FOR US)** | \|M\| ≥ 3.0pp ∧ (sign(E)≠sign(M) ∨ \|E\| ≤ **0.5pp**) | `ETN` is a genuine electrical leg; 4-of-12 stands |
| **C** | \|M\| < 3.0pp | the basket never moved enough for the test to have a null — **declared at registration** |

- ★ **D93 BEFORE freezing** (252 overlapping 5-session windows to 08-18): **A 29.8% · B 17.1% ·
  C 46.8%**; conditional on \|M\|≥3.0 (53.2% of windows) **A 56.0% / B 32.1%**. 2-year check (n=496):
  27.8 / 15.9 / 50.2. sd(M) **5.095** · sd(E) **3.988** · corr(M,E) **+0.467**.
- **State at registration, disclosed** (2 of 5 sessions elapsed, 08-14→08-18): **M −2.617pp ·
  E −3.324pp** — same sign, \|M\| **below** the gate. **Leaning A, gate not cleared.**
- ⚠ **Implied-move check**: no single-name straddle governs a 4-name sign test; the `E` leg's 1.5pp
  threshold sits **inside** comparable-industrial D2 implied moves (`RTX` ±1.9%) ⇒ the `E` leg is
  **declared LOW-RESOLUTION at registration**, not presented as a trigger.
- 🚨 **Anti-signal (VOID, not scored)**: M&A, guidance withdrawal or index deletion at `ETN` or any of
  the three; an `ETN`/`HPE` earnings print in-window; a market-wide halt. **`NVDA`'s 08-26 print is
  outside by design — this row tests CARRY, not an event.**
- **Information content (B4)**: **A FALSIFIES** the desk's 4-of-12 concentration count and the
  Industrials OW−'s status as a diversifier (a live sizing input). **B FALSIFIES the lens**, and at
  17.1% is genuinely reachable. **C confirms nothing and is modal (46.8%)** — disclosed.

---

## S100 — ★★★ Does the Staples promotion survive its own two earnings prints? · ARMED · → settle **2026-08-21**

Registered **2026-08-19 by the `industry_US` PREMORTEM (Lens 1)**. `grep S100` → **0 across all files.**

**Why it exists.** `SECTOR_ROTATION §2b` promoted **STPL UW− → UW** on the board's largest two-session
Δ (+0.325), reasoning that `wflow +0.083 ≫ eqflow −0.020` makes it **mega-cap-narrow**. The
decomposition refutes that reasoning: of the +0.325, **`WMT` contributes +0.129 (40%) at a 28.9%
weight while `TGT` contributes +0.004 at a 1.8% weight** — so `TGT`'s **+0.210 Δ and +0.713 flow
score (the sector's best)** are invisible in every cap-weighted instrument the run read.
**`TGT` reports 2026-08-19, `WMT` reports 2026-08-20** — two dated issuer binaries inside 24 hours in
a sector the same run promoted **and then excluded from DEEP on recency** (promoted here to a 5th slot).

**Frozen observable**: EW{`TGT`,`WMT`} cumulative return, **2026-08-18 settled close → 2026-08-21
settled close**, minus **`SPY`** over the identical window. **Both prints land inside it.**

| Branch | Threshold | Meaning |
|---|---|---|
| **A (AGAINST US)** | excess **≥ +6.5pp vs `SPY`** | issuer-level demand, β-free (basket β vs `SPY` = **0.09**) ⇒ the one-notch promotion was **too small** and the big-box node needed separate treatment |
| **B (FOR US)** | excess **≤ −6.5pp vs `SPY`** | the +0.325 Δ was defensive-rotation beta, as `XLP`'s β-adjusted **−0.592** said |
| **C** | between | no conclusion changes |

- ★ **Implied move MOVED the thresholds** (the rule, applied rather than noted): `TGT` **±7.8%** ·
  `WMT` **±5.3%**, both expiry **2026-08-21, D2** ⇒ EW implied ≈ **±6.55%**. Lens 1 proposed ±3.0pp;
  **that sits inside the implied move and would carry no information**, so the bands are set **at** it.
- **D93**: unconditional 2-session \|excess\| for this basket over trailing 252 sessions —
  sd **2.27pp**, P(≥+3.0) **11.1%**, P(≤−3.0) **7.9%**, C **81%**.
  ⚠ **C is the unconditional favourite and is NOT the conditional favourite**: in the identical
  calendar week last year `TGT` printed **−6.33% (2025-08-20)** and `WMT` **−4.49% (2025-08-21)** on
  their prints — an EW one-day move of ≈**−5.4%**. **Both figures are recorded so neither can be used
  as an escape hatch later.**
- 🚨 **Anti-signal (VOID)**: `SPY` 08-18→08-21 move beyond **±2.5%** (index shock, not issuer), or a
  guidance/M&A event at either name that is **not** the scheduled print.
- **Information content (B4)**: **A FALSIFIES** ROTATION §2b's explicit mega-cap-narrow reasoning on a
  β-0.09 basket — the very defence used to discount the raw print. **B FALSIFIES the delta rule
  itself**, the same rule that produced the run's other promotion (HLTH on Δ +0.228). Neither branch
  merely confirms.

---

## S101 — ★★★ Does the `vol_surge` gate cost the desk return? The shortlist tests itself · ARMED · → settle **2026-08-26**

Registered **2026-08-19 by the `industry_US` PREMORTEM (Lens 3; thresholds measured at registration)**.
`grep S101` → **0 across all files.**

**Why it exists.** The 🟢가속 tag — the shortlist's only gate — is driven by `vol_surge`, and
**`corr(rs60, vol_surge) = −0.124` across 299 names**. The 9 names clearing `vol_surge ≥ 1.2` average
**rs60 −12.7 vs `SPY`** against a universe mean of **+2.9**; **of the top-20 by `flow_score`, 18 are 🟡
and 2 are 🟢**; exactly **1 of the top-15 runners is green**. Countable consequence: **9 of the 10
strongest non-green runners have ZERO mentions across all five of that run's documents.** The desk
ruled the same artifact harmless for two **sectors** (Energy `0🟢/16`, Health Care `0🟢/32`) and never
applied the ruling to the erased **names**. This row makes the gate falsifiable.

**Frozen observable** (both baskets frozen exactly as printed by the 2026-08-19 run), settled closes,
benchmark **`SPY`** inline, at the **2026-08-26** settle:
`spread` = EW{`DELL`,`PANW`,`SHOP`,`ABNB`,`CRWD`,`DASH`,`PYPL`,`TMO`,`BKNG`,`AXON`} 5-session excess
vs `SPY` **MINUS** EW{`KKR`,`RTX`,`LITE`,`ORCL`,`CSCO`,`MA`,`BAC`,`WMT`} 5-session excess vs `SPY`.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (the gate costs us)** | spread **≥ +4.45pp** | the excluded names beat the admitted names past the measured p85 ⇒ **the gate is an alpha filter with the wrong sign, not a quality filter** |
| **B (the gate earns its keep)** | spread **≤ −3.88pp** | the excluded runners gave it back; the gate did its job |
| **C** | between | no conclusion changes |

- ★ **D93 executed BEFORE freezing**, 252 trailing settled 5-session windows to 08-18:
  **mean −0.035 · sd 4.527 · p15 −3.877 · p85 +4.452 · min −15.918 · max +13.562** ⇒
  **P(A) 20.6% · P(B) 20.6% · P(C) 58.7%.** Thresholds are the measured tails, not round numbers.
- ★★ **This estimator is centred at −0.035** — the **first near-zero-centred estimator this desk has
  registered**, against nine consecutive rows (`S55` onward) whose centres were materially non-zero.
  The bias those rows kept reproducing is **not** present in a long-short spread, which is itself the
  finding: it lives in the single-leg-vs-`SPY` construction, not in the estimator code.
- **State at registration**: **−0.677** (erased EW exc5 **−0.406** vs green EW exc5 **+0.271**) —
  **mid-band, near-neutral.** Context, **not** the observable: **erased EW 60-day excess vs `SPY`
  +40.04 against green EW +1.18 — a 38.9pp gap.**
- 🚨 **Anti-signal (VOID)**: an earnings print at **≥3 of the 10** erased names inside the window —
  the basket would then measure an earnings cluster, not the gate.
- **Information content (B4)**: **A FALSIFIES the desk's own shortlist construction** and would make
  the 🟢 gate a measured liability. **B FALSIFIES this lens** and vindicates the gate. Both bite.

---

## S102 — ★★★ Which tenor carries the FOMC minutes? *(replaces the self-voided `P73`)* · ARMED · → settle **2026-08-21**

Registered **2026-08-19 by the `industry_US` PREMORTEM**. `grep S102` → **0 across all files.**

**Why it exists — and it is a repair, stated as one.** The **FOMC minutes released 2026-08-19** are a
dated ≤48h binary that **`catalyst_calendar` did not carry** (it returned one row: the undated Hormuz
statement). MACRO hand-injected it as **`P73`** — and `P73` **voided at registration**: its own
anti-signal named *"a Warsh testimony headline that moves ≥3 outlets"*, and the same report's §D-1
carries **Warsh at 10 articles / 6 outlets**. A protocol that leaves the window's only dated binary
unbracketed is the failure this stage exists to prevent, so the row is re-registered with an
anti-signal that is reachability-checked **and not already fired**.

**Frozen observable**: `DGS2` **and** `30y−10y`, from `[FRED]`, at the **first close covering
2026-08-21**.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (front-end repricing)** | `DGS2` **≥ 4.30** | bear **flattener** ⇒ every duration-UW argument on this desk changes sign again; and per the measured rate betas the **ENRG OW is helped** (`XLE` **+0.1534 pp/bp**) |
| **B (long-end-only)** | `DGS2` **≤ 4.08** ∧ `30y−10y` **≥ 0.59** | term premium owns the move; `R73`'s successor mechanism survives |
| **C** | between | **the favourite, disclosed**: `DGS2`'s realised 9-observation range is **4.15–4.25**, entirely inside C |

- ★ **The measurement that makes this row worth registering**: regressing each sector's daily excess
  vs `SPY` on Δ10y (bp) controlling for Brent, 120 settled sessions to 08-18 — `XLU` **+0.0049** ·
  `XLRE` **−0.0072** · `XLP` **+0.0224** · `XLV` **+0.0185** ⇒ **the four legs of the duration
  underweight have NO measurable rate beta**, while `XLE` has **+0.1534** (R² 0.550 with Brent).
  **The desk's only rate-exposed tilt is its overweight, with a positive sign.**
- ⚠ **Implied move**: `SPY` **±0.5% (expiry 2026-08-19, D0)** — a same-day index straddle prices no
  meaningful move, so a ≥15bp `DGS2` threshold is **outside** anything the options market has priced.
- 🚨 **Anti-signal (VOID)**: an **intermeeting Fed policy action** or a **Treasury refunding
  announcement** inside the window. ⚠ **Warsh testimony is deliberately NOT an anti-signal here** —
  it is same-day with the minutes and inseparable from them, which is precisely the defect that
  killed `P73`.
- **Information content (B4)**: **A FALSIFIES** the desk's rate framing for the third time in six days
  (`P56` → `R73` → `P65` → today's §A-1 bear-steepener re-measurement). **B FALSIFIES** `R73`'s
  successor mechanism. Neither branch merely confirms.


## `S103` — registered 2026-08-19 by the `industry_US` ALPHA stage (the run's only new bracket after PREMORTEM)

> **ID check**: `grep -c S103 handoff/*.md` returned **0** in every file except `SCENARIOS.md`'s
> allocation note; highest existing **S102 (US)**. Allocated **S103**.

### `S103` — Does the AI-compute cycle re-accelerate on its own epicenter's print?

- **Why it exists**: `catalyst_calendar --days 10` surfaced **`NVDA` earnings 2026-08-26** — invisible to
  the 5-day default (`D26`) — and `action_bracket.py` **could not emit a ticket for it** (`D294`).
  `NVDA` is **15.60% of invested capital, the book's largest single position**. An unbracketed binary on
  the largest position is the exact condition the PREMORTEM stage exists to prevent, so it is bracketed
  here by hand rather than left to the script.
- **Observable**: `NVDA` 5-session excess vs **`SPY`**, settled closes, `auto_adjust=False`, window
  **2026-08-25 close → 2026-08-29 close** (the print falls inside).
- **A (the cycle re-accelerates)** excess **≥ +5.0pp vs `SPY`** ⇒ the epicenter is being paid, and the
  registry's **19.82%-of-total** epicenter reading is *understated* — the three unlabelled chain names
  (`LITE` `COHR` `HPE` = **14.75% of total**, `M731`) put true any-layer exposure at **≈38.4%** into a
  re-accelerating cycle.
- **B (the cycle is paid out)** excess **≤ −5.0pp vs `SPY`** ⇒ the same understatement runs the other
  way: the book is **~15pp of total assets more exposed than any artifact prints**, and the concentration
  question `G4` cannot state as a single number (250d **11** units · 500d **10** · 750d **10**) becomes the
  live one. ★ Under B the count that matters is not `S99`'s 4-vs-5 AI units but **7 of 12**.
- **C** −5.0pp < excess < +5.0pp — **declared now, before the fact.**
- **Pre-registration state, settled 2026-08-18**: `NVDA` `flow_score` **+0.111**, tag 🟡중립, `obv_state`
  **중립**, **RS20 +3.4 / RS60 −3.2 vs `SPY`**, `vol_surge` **0.72**, two-session Δ **−0.347**.
  ⇒ **The book's largest position enters its own print on the weakest flow reading of any name it holds.**
  Disclosed at registration, not discovered at scoring.
- 🚨 **Anti-signal ⇒ VOID**: an index-level shock (`SPY` 08-25→08-29 beyond ±3%), a guidance withdrawal or
  M&A at `NVDA`, or an export-control announcement inside the window — none of which would be the print.
- ⚠ **Threshold provenance — the known weakness of this row.** ±5.0pp is **hand-set**. The nearest chain
  this stage could read expires **2026-08-21 (D2)**, before the event, so **no implied move governs it
  yet.** ⇒ **Obligation: re-derive the bands from the 08-26-or-later straddle at the 08-20 or 08-21 run,
  before the print.** Registered as `D295`. **Until that is done this row is LOW-RESOLUTION and is
  labelled so, rather than being quietly scored as if it were measured.**
- **B4 grading**: **A falsifies** the "AI-compute is fully accounted at 19.82%" reading that the ✅ GAP flag
  implies. **B falsifies** `S99`'s framing that the open question is whether `ETN` is a 4th or 5th AI unit.
  **Neither branch merely confirms. Settle 2026-08-29** (first settled close on/after 08-29).

---

## Registered 2026-08-20 by the `industry_US` PREMORTEM (S104 – S107)

> ⚠ **ID 3-grep at WRITE time (D137 / D76)** across all seven files (`SCENARIOS*.md` ×3,
> `STANDING_VIEW*.md` ×3, `RESEARCH.md`) **and** all of `llm_outputs/2026-08-*/`: `S104` `S105`
> `S106` `S107` returned **0 hits everywhere**; highest existing was **S103 (US) / S66-KR (KR)**.
> ★ **Every band measured on the estimator's own trailing-252 distribution (D93) BEFORE freezing.**
> ⚠⚠ **Implied-move disclosure, and it is a LIMIT not a check**: `module_flow --positioning` returned
> **every** straddle at expiry **2026-08-21, D1** (`NVDA` ±1.9% · `AVGO` ±2.2% · `XLU` ±0.9% ·
> `XLV` ±1.6% · `XLK` ±1.9% · `MPC` ±3.4% · `WMT` ±2.0% · `TGT` ±2.3% · `MRVL` ±5.3% · `COHR` ±6.1%).
> A D1 straddle prices one session ⇒ **a FLOOR on a multi-session implied move, not an estimate**
> ⇒ **no threshold below is claimed to sit outside what is priced** (`D295`).

### S104 — ★★★ July PCE 2026-08-28: the window's only dated macro binary, and NOTHING brackets it · ARMED · → settle **2026-08-31**

**Why it exists.** MACRO §6 handed it over explicitly: `CATALYST_WATCH` carries **July PCE (08-28,
D-8)** as a binary and **no row on the board is keyed to it.** It is genuinely two-sided because of
this run's own §A-1 measurement: **the entire 60-observation rise in `DGS10` (+0.140) is real yield
(`DFII10` +0.230) against FALLING inflation compensation (`T10YIE` −0.100).** A PCE print is the
direct test of which leg does the work — and that frame underwrites `P77`, `P78` and the UTIL/RE
underweights.

**Frozen observable**: `T10YIE` **change in basis points** from the **2026-08-27** `[FRED]` close to
the **first `[FRED]` close covering 2026-08-31**.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (AGAINST US)** | **>= +3.0 bp** | The print reprices **inflation compensation** ⇒ the desk's *"this is all real yield"* frame is measuring the wrong variable, and every conclusion resting on a term-premium story must be re-argued |
| **B (FOR US)** | **<= −3.0 bp** | Compensation falls again ⇒ the real-yield frame survives and strengthens |
| **C** | between | No conclusion changes |

- ★ **D93 executed BEFORE freezing**: `T10YIE`'s own **2-observation change**, trailing 252 —
  **mean −0.07bp · sd 2.60bp · p10 −3.0 · p50 0.0 · p90 +3.0.** Bands are **p10 / p90** ⇒
  **A ~10% · B ~10% · C ~80%, disclosed up front.**
- **State at registration**: `T10YIE` **2.300** (2026-08-19, the one `[FRED]` series carrying an
  08-19 observation).
- **Implied move**: no straddle exists on this observable. The nearest index proxy (`SPY` ±0.5%,
  expiry 08-21 D0) prices a **different object on a different date** ⇒ **not conflated**, and no claim
  is made that ±3bp sits outside what is priced.
- **Information content (L3): HIGH and asymmetric.** **A invalidates a frame three live rows rest on;
  B only confirms.** Registered because the against-us branch is the informative one.
- 🚨 **Anti-signal (VOID)**: a **Treasury refunding announcement**, a **further buyback-size change**,
  or an **intermeeting Fed action** inside 08-27 → 08-31 ⇒ the move is not the print.
  ⚠ **Reachability-checked and it is LIVE, not decorative**: Treasury changed buyback sizes on
  **2026-08-19**, i.e. this exact anti-signal fired inside another row's window nine days earlier
  (`S102`, `D296`). Registered anyway, with that stated.
- **Owner**: `industry_US`.

### S105 — ★★★ Google to `MRVL`: is a held name being structurally displaced? · **SETTLED FIRED-A** (scored 2026-09-04, folded into the master scoring log by the 2026-09-06 `industry_US` run — `D472` header hygiene) · → settle **2026-09-03**

**Why it exists.** On **2026-08-19** Marvell disclosed a **warrant issued to Google for up to 59
million shares (about $12.2bn)** alongside a chip agreement. **`MRVL` +9.85% and `AVGO` −4.61% the
same session**, and Barron's carries the readthrough in its title (*"…and Why It's Bad News for
Broadcom."*). **`AVGO` is held in BOTH books, is the only book name tagged red** (flow −0.625, OBV
distribution, rs20 −11.5), and its standing §3a thesis line still reads *"a separate boat from memory
— hyperscaler capex is their driver."* **Custom-silicon supplier displacement by a hyperscaler is the
opposite sign of that same variable, and no row on the board tests it.**

**Frozen observable**: [`MRVL` **10-session excess vs `SPY`**] **minus** [`AVGO` **10-session excess
vs `SPY`**], at the **2026-09-03** settled close.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (the adversarial ask)** | **<= −10.836** (252d p15) | The spread **reverses** ⇒ one warrant, one week, **no displacement**; the 08-19 move was positioning and `AVGO`'s carried thesis stands |
| **B** | **>= +30.484** (252d p95) | The spread **extends** ⇒ displacement, and **`AVGO`'s thesis line must be rewritten** rather than re-filed |
| **C** | between | Neither reading survives on this window |

- ★ **D93 executed BEFORE freezing**: trailing **252** observations of the same estimator —
  **mean +3.944 · sd 15.753 · p05 −20.563 · p15 −10.836 · p50 +2.347 · p85 +17.340 · p95 +30.484.**
- ⚠⚠ **State at registration: +25.780 = the 93.7th percentile. ALREADY NEAR BRANCH B.** Disclosed at
  registration rather than discovered at scoring — **branch A is the adversarial ask**, and a scorer
  must not read a B-fire as a surprise.
- **Implied move**: `MRVL` **±5.3%**, `AVGO` **±2.2%**, both expiry **2026-08-21 D1** ⇒ a **floor**.
  A 10-session **pair spread** of ±10–30pp is a larger object than either D1 straddle prices, but
  **no claim is made that it sits outside a properly-dated implied move**, because none was readable.
- **Information content (L3): HIGH.** **B forces a rewrite of a held name's thesis; A retires this
  run's headline finding.** Neither outcome is predictable from anything the desk currently holds.
- 🚨 **Anti-signal (VOID)**: a **change of control or an M&A announcement at either name** inside the
  window. ⚠ **`MRVL`'s 2026-08-28 earnings print falls INSIDE the window and is DISCLOSED as a known
  contaminant rather than treated as a VOID** — the row deliberately settles **after** it, because a
  displacement thesis that cannot survive the challenger's own guide is not a displacement thesis.
  **`AVGO` has no print inside the window** (next 2026-09-04, checked at registration).
- **Owner**: `industry_US`.

### S106 — ★★ Is the IT underweight wrong about its own largest reversal? · **SETTLED FIRED-C** (scored 2026-09-04, folded into the master scoring log by the 2026-09-06 `industry_US` run — `D472` header hygiene) · → settle **2026-09-03**

**Why it exists.** ROTATION put **IT at UW** on `eqflow` −0.197 with **19 red of 56** — correctly, on
the aggregate. But two of the sector's largest names are in **20-day reversals whose excess EXCEEDS
their own 60-day excess**: `MSFT` **exc20 +21.18 vs exc60 +12.56 (last-20 share 168.5%)** and `CRM`
**+23.54 vs +11.31 (208.1%)**, both OBV accumulating. `MSFT` is **10.7% of the IT bucket** with
`flow_score` **+0.422**. **This is the "short the label, long the sub-node" pattern the pre-mortem
found in three separate buckets today, and it is the only one testable on a single non-reporting
name.**

**Frozen observable**: `MSFT` **10-session excess vs `SPY`**, at the **2026-09-03** settled close.

| Branch | Threshold | Meaning |
|---|---|---|
| **A** | **>= +7.969** (252d p95) | The reversal extends ⇒ **the IT UW is a sub-node call wearing a sector label**, and ROTATION's unit is wrong even though its sign is right |
| **B** | **<= −9.184** (252d p05) | It rolls over ⇒ the sector call covers it and the 168.5% shape was noise |
| **C** | between | Modal, disclosed |

- ★ **D93 executed BEFORE freezing**: trailing **252** — **mean −0.756 · sd 6.275 · p05 −9.184 ·
  p15 −5.532 · p50 −1.422 · p85 +2.913 · p95 +7.969.** Bands at **p95 / p05** ⇒ **A ~5% · B ~5% ·
  C ~90%.**
- **State at registration**: **−0.551 = the 56.7th percentile**, i.e. **inside C and essentially at
  its own median.** ⚠ **Stated honestly: the 20-day shape lives in `exc20`, not in `exc10`**, which is
  why the bands are wide and C is heavily favoured. Registered anyway because the *unit* question is
  what this desk keeps getting wrong.
- **Implied move**: `XLK` **±1.9%**, expiry 08-21 D1 — a **floor**, and a **sector** object rather
  than this name. Not conflated.
- **Information content (L3): MEDIUM**, stated as medium rather than inflated. **A changes how this
  desk writes sector calls; C teaches least.**
- 🚨 **Anti-signal (VOID)**: an `MSFT` acquisition, guidance withdrawal, or an antitrust ruling inside
  the window. **`MSFT` has no earnings print inside it** (checked at registration).
- **Owner**: `industry_US`.

### S107 — ★★★ The `T` orphan gets its first falsifier in three runs · **SETTLED FIRED-C** (scored 2026-09-04, folded into the master scoring log by the 2026-09-06 `industry_US` run — `D472` header hygiene) · → settle **2026-09-03**

**Why it exists.** `T` is **9.74% of the real book's invested capital** (`M737` corrected `9.59%`,
which is `RTX`) and the standing §3a row says, in these words, that it has *"no cycle label, no card,
no thread, no bracket and no KPI in any live artifact"* — **for a third consecutive run.** Meanwhile
the tape turned: `T` **exc20 +6.13 against exc60 −3.70** (last-20 share **−165.9%** = a fresh 20-day
turn off a losing base), OBV accumulating, in a telecom node whose `eqflow` is **+0.404**. **The desk
cannot claim credit for a position it has no thesis for, and cannot manage one either. This row ends
that.**

**Frozen observable**: `EW{T, VZ}` **10-session excess vs `SPY`**, at the **2026-09-03** settled close.
(Equal-weight, and **`TMUS` is deliberately excluded** — flow −0.814 red/distribution, and the carried
kill clause is already written against *telecom-ex-`TMUS`*.)

| Branch | Threshold | Meaning |
|---|---|---|
| **A** | **>= +12.244** (252d p95) | The turn extends ⇒ **a 9.74%-of-invested position has a live, measurable thesis** and the residual really was a LABEL, not a price |
| **B (the adversarial ask)** | **<= −9.533** (252d p05) | It reverses ⇒ the orphan is an orphan on price too, and the position needs re-justifying on something other than `eqflow` |
| **C** | between | No conclusion changes |

- ★ **D93 executed BEFORE freezing**: trailing **252** — **mean −0.722 · sd 6.570 · p05 −9.533 ·
  p15 −6.230 · p50 −1.308 · p85 +5.504 · p95 +12.244.**
- ⚠ **State at registration: +7.671 = the 92.9th percentile — already ABOVE p85 and approaching branch
  A.** Disclosed at registration, not discovered at scoring. **Branch B is the adversarial ask.**
- **Implied move**: not readable for this pair at a usable expiry; **no claim is made** that the
  thresholds sit outside what is priced.
- **Information content (L3): HIGH for the book specifically.** This is the **first falsifiable
  statement ever registered about this position**, and **either branch resolves a three-run open
  residual** — A by giving it a thesis, B by ending the pretence that it has one.
- 🚨 **Anti-signal (VOID)**: a **dividend-policy change**, an **M&A announcement**, or a
  **spectrum-auction result** at either name inside the window.
- **Owner**: `industry_US`.


---

# Registered 2026-08-21 by the `industry_US` PREMORTEM — **`S108` – `S111`**

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, held.
> ⚠ **ID 3-grep at WRITE time (D137/D76)** across `handoff/RESEARCH.md`, `handoff/STANDING_VIEW*.md`,
> `handoff/SCENARIOS*.md`, `llm_outputs/` and `REPORT/`: `S108` `S109` `S110` `S111` returned **0
> files**. Highest existing **S107** (US) / **S64-KR** (KR). All four indexed in the `SCENARIOS.md`
> MASTER INDEX.
> All prices settled **2026-08-20**, one provider (`yfinance`, `auto_adjust=False`), benchmark **`SPY`
> named inline (C1)**. Bands are the observable's own trailing-252 distribution (**D93**) with the
> **state's own percentile disclosed at registration**. **SETTLEMENT MODE = TERMINAL on both branches**
> for all four (D242).
>
> 🚨 **Implied-move check performed, and its RESULT is that it cannot be used on these rows.**
> `module_flow --positioning` (2026-08-21, intraday): `HPE` **±2.7%** · `DELL` **±1.8%** ·
> `FRO` **±3.1%** · `NEM` **±2.0%** — **every straddle expires 2026-08-21 = D0** and therefore
> covers **none** of the events bracketed below (`FRO`'s print is 08-31; `S110` settles 09-03).
> Taking a threshold from them would fabricate one — **the `M47` defect by name**. All four thresholds
> are distribution-based and **the gap is declared, not glossed.**

## S108 — ★★★ The MANDATORY D-0 equity bracket: if Warsh is dovish, the three underweights rip together · ARMED · → settle **2026-08-25**

**Why it exists.** The 2026-08-21 Jackson Hole speech by Fed chair Kevin Warsh is the window's only
D-0 binary and **`catalyst_calendar --days 10` carried ZERO rows for it** (MACRO hand-injected it;
`D18`/`D288-KR` reproduction). `P82` brackets the **rate** leg. **Nothing brackets the equity leg**,
and the equity leg is where this desk's three underweights live.

| | |
|---|---|
| **Frozen observable** | `EW{XLU, XLRE, XLP}` **3-session excess return vs `SPY`**, settled closes, window **2026-08-20 close → 2026-08-25 close** |
| **Branch A (AGAINST US)** | **≥ +1.68pp** (252-obs p85) — the three UW/N− sectors rip **together**; the correlated-UW pattern is real and live |
| **Branch B (with us)** | **≤ −1.76pp** (252-obs p15) — a hawkish read and the underweights are on the right side |
| **Branch C** | between = **the favourite, disclosed** |
| **D93 before freezing** | trailing 252: mean **−0.148** · sd **1.759** · p15 **−1.757** · p50 **−0.118** · p85 **+1.675** · p95 **+2.719** ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **+1.432 = the 78.6th percentile** — inside C but **already leaning A**, disclosed now rather than discovered at scoring |
| **Anti-signal (VOID)** | a CPI/PPI/PCE print, an intermeeting FOMC action, or a Treasury refunding/buyback-schedule change inside 08-20 → 08-25. ⚠ **Base rate checked at registration (`D300-KR`)**: the next scheduled macro print is **July PCE on 08-28 — OUTSIDE the window**; no FOMC meeting falls inside it; Treasury's buyback schedule is published in advance with no change scheduled before 08-25. ⇒ **the clause is not near-certain to fire.** ⚠ **Warsh's speech is deliberately NOT an anti-signal — it is the event** |
| **Information content (L3)** | **HIGH, carried by the against-us branch**: A falsifies three sector calls at once; B confirms |
| **Owner** | `industry_US` |

## S109 — ★★★ `FRO` 2026-08-31: the Hormuz axis's one un-bracketed dated binary, on a crowded short · **SETTLED FIRED-A** (scored 2026-09-04, folded into the master scoring log by the 2026-09-06 `industry_US` run — `D472` header hygiene) · → settle **2026-09-02**

**Why it exists.** `FRO` (Frontline, crude tankers) appeared on `catalyst_calendar` for the first time
this run at **D-10**, and **no row on the board is keyed to it** — while `S74`/`S84`/`S92`/`S95` all
bracket the same Hormuz axis through refiners and ETFs. **`M45` measured that the blockade's literal
beneficiaries were not being bought; this row tests that a second time on a dated event.**

| | |
|---|---|
| **Frozen observable** | `FRO` **5-session excess return vs `SPY`**, settled closes, window **2026-08-26 close → 2026-09-02 close** (the 08-31 print sits inside it) |
| **Branch A (the freight leg is paid)** | **≥ +8.04pp** (252-obs p85) — Red Sea re-routing and Bab el-Mandeb avoidance show up in ton-mile earnings |
| **Branch B (the freight leg is NOT paid)** | **≤ −4.62pp** (252-obs p15) — `M45` replicates; the axis's only tradeable expression remains refining margin |
| **Branch C** | between |
| **D93 before freezing** | trailing 252 of `FRO` exc5: mean **+1.483** · sd **6.523** · p05 **−9.299** · p15 **−4.620** · p50 **+1.649** · p85 **+8.043** · p95 **+11.390** ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **+9.467 = the 89.3rd percentile**; close **43.56**; 20-day return **+12.12%**. ⚠ **Disclosed: the state already sits between p85 and p95, so branch A is the WEAK-information branch and branch B is the informative one** |
| **Positioning (context, not direction)** | short interest **6.1% of float, BUILDING**, DTC **4.1**; P/C **0.56**; IV skew **+18.5**; OBV 매집; news velocity **1.62×** (2026-08-21 pull). ⚠ **Crowded-short is turn-conditional squeeze fuel and NEVER a buy signal alone (`D6`)** — cited as the reason both branches are reachable, not as a direction |
| **Anti-signal (VOID)** | an `FRO`-specific corporate action (M&A, equity raise, special dividend, fleet sale) **or** a general tanker-rate collapse driven by an OPEC+ supply decision inside the window |
| **Information content (L3)** | **B is the informative branch and it is stated as such.** ⚠ `FRO` is **not in `us_top300`** — priceable, not flow-taggable. **This row is a measurement, not a candidate hand-off** |
| **Owner** | `industry_US` |

## S110 — ★★ `S87` averaged two opposite states; this is the pair test it could not perform · **SETTLED VOID** (scored 2026-09-04, folded into the master scoring log by the 2026-09-06 `industry_US` run — `D472` header hygiene) · → settle **2026-09-03**

**Why it exists.** `S87` (EW{`DELL`,`HPE`} exc5, settling 2026-08-21) reads **−8.895 = already inside
branch A (EXHAUSTED)**. **The pair does not agree**: on the `M149` decomposition `HPE` earned
**+29.65** in days 21–60 and **+7.71** in the last 20 (**20.6% share = live**), while `DELL` earned
**+45.26** in days 21–60 and **−4.35** in the last 20 (**−10.6% share = rolling over**). **An EW basket
cannot report that**, and `HPE` is held while `DELL` is not.

| | |
|---|---|
| **Frozen observable** | [`HPE` 5-session excess vs `SPY`] **minus** [`DELL` 5-session excess vs `SPY`], settled closes, at the **2026-09-03** close |
| **Branch A (the held name is the better half)** | **≥ +6.02pp** (252-obs p85) — the pair genuinely diverges and `S87`'s EXHAUSTED verdict was an averaging artifact on the leg the desk owns |
| **Branch B (the held name is the worse half)** | **≤ −6.14pp** (252-obs p15) — `HPE` is the drag and the exhaustion verdict lands on the held name |
| **Branch C** | between |
| **D93 before freezing** | trailing 252: mean **−0.698** · sd **7.109** · p15 **−6.141** · p50 **−0.665** · p85 **+6.022** ⇒ **A ≈15% · B ≈15% · C ≈70%**. ⚠ **sd 7.109 is wide** — a genuinely noisy pair spread; C is the honest favourite |
| **State at registration** | **+0.494 = the 55.2nd percentile** — mid-pack, **both branches equally reachable**; the cleanest starting state of the four rows registered today |
| **Anti-signal (VOID)** | an earnings print at **either** name inside the window. ⚠ **Reachability-checked**: `module_fundamentals_us` puts `HPE`'s next print at **2026-09-04**, i.e. **one day after the settle** — outside by one session, **and that margin is stated because it is thin** |
| **Information content (L3)** | A and B both change a conclusion; C is uninformative and likely. **The row exists because `S87` cannot distinguish the two states, not because a new direction is claimed** |
| **Owner** | `industry_US` |

## S111 — ★★★ `P67`'s credit observable is pointed at HIGH YIELD while the measured move is in IG TECH · ARMED · → settle at the first `[FRED]` close covering **2026-08-28**

**Why it exists.** `P67` tracks *"the AI capex bill is migrating to debt and credit does not see it"*
on **`HY OAS` ≥ 2.85%**. Measured 2026-08-19: **`HY OAS` 2.73%, 10bp off its 365-day low — no move.**
But the body-read of `Analysis-US corporate AI debt surge tests investor limits` [Reuters via
`yahoo_finance`/`cna`, 08-21] gives the number that HAS moved: **AI hyperscaler debt issuance $220bn
in 2026 against $12.5bn in the comparable period last year (17.6×)** `[BNP Paribas, as of Aug 10]`,
and **tech IG spreads at 89bp — 9bp WIDER than the overall investment-grade market**, inverting a
sector that historically traded through it. ⇒ **`P67` may be about to score "credit does not see it"
on an instrument that cannot see it.**

| | |
|---|---|
| **Frozen observable** | **`BAMLC0A0CM` (`ig_oas`)**, `[FRED]`, **level** at the first close covering **2026-08-28** |
| **Branch A (credit IS pricing it)** | **≥ 0.85%** — above the series' own 252-obs p85 (0.83); `P67`'s conclusion is right while its instrument was wrong |
| **Branch B (idiosyncratic to tech, not a credit event)** | **≤ 0.77%** — below the 252-obs p50 (0.79); the index tightens while tech stays wide ⇒ a sector relative-value story, not a credit-cycle story |
| **Branch C** | between = **the favourite, disclosed** |
| **D93 before freezing** | `ig_oas` 252-obs LEVEL: min 0.730 · p15 0.750 · p50 0.790 · p85 0.830 · max 0.940; **current 0.810 = 68.7th percentile**. 5-obs CHANGE: mean −0.01bp · sd **2.76bp** · p10 −3.0 · p90 +3.0 ⇒ A needs +4bp over ~7 observations (outside p90), B needs −4bp (outside p10) ⇒ **A ≈12% · B ≈10% · C ≈78%** |
| **State at registration** | `IG OAS` **0.81%** (08-19) · `HY OAS` **2.73%** · `NFCI` **−0.559** (08-14) · tech IG **89bp** `[news]` |
| **Anti-signal (VOID)** | a credit event unrelated to technology issuance (a large non-tech default, a bank failure, or a sovereign-rating action) inside the window. ⚠ **Base-rate checked**: the term `bankruptcy` returns **52** hits over two days, the lowest count on this desk's bucket board, and `NFCI` is at its loosest of the window ⇒ **far from near-certain** |
| **Information content (L3)** | **HIGH, and it is an instrument test rather than a direction bet.** A says `P67`'s conclusion survives on a better axis; **B says the desk has watched the wrong credit series for six runs.** ⚠ **`P67` is NOT re-frozen and still settles on `HY OAS` at 08-28 as registered** — this row runs beside it, and **if the two disagree, the disagreement is the finding** (the `S14-ANNEX`/`S35-ANNEX` precedent) |
| **Owner** | `industry_US` |

### Registered and then DROPPED, with the reason (rather than bracketed to look thorough)
- **MSCI quarterly review (2026-08-31)** — **neither branch would change a conclusion.** No
  constituent change is named anywhere in the window's 4,991-article corpus, and a passive-flow date
  with no named name cannot move a sector verdict on this board (`L3`).
- **A `PLTR` bracket** — considered because Lens 3 measured that this run revived `PLTR` on a
  condition (`rs60 > 0`) satisfied by **exhaustion geometry** (+25.75 exc60 of which **146.4%** is the
  last 20 sessions, days 21–60 **−11.95**). **Dropped**: `PLTR` is not held and has no DEEP slot, so a
  bracket would measure the desk's ledger hygiene rather than the market. **Filed as a dig instead.**


---

# Registered 2026-08-22 by the `industry_US` PREMORTEM — **`S112` · `S113` · `S114`**

> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md`, `llm_outputs/**`, `REPORT/**`: `S112` `S113`
> `S114` returned **0 files**. Highest existing **`S111`** (US) / **`S67-KR`** (KR) — numbers taken
> beyond **both** series so the suffixed and unsuffixed series cannot collide (the `D76` class).
> ⚠ Written with **`'a'` (append)** mode — the D165 pre-commitment after the 2026-08-05 truncation.
> All observables and thresholds **frozen at registration**. Prices settled **2026-08-21**, one
> provider (`yfinance`, `auto_adjust=False`). Benchmark **`SPY`** named inline (`C1`).
> Bands are **252-obs distributions of the observable itself** (`D93`), with the state's own
> percentile disclosed. **SETTLEMENT MODE = TERMINAL on both branches** for all three (`D242`).

## S112 — ★★★ The MANDATORY Jackson Hole bracket, and it owns the PCE print inside its own window · ARMED · → settle **2026-08-31**

**Why it exists.** The window's biggest binary is **invisible to `catalyst_calendar`** — the symposium
runs **2026-08-27 → 08-29** (`economictimes` body, 08-22, verbatim: *"the August 27 to August 29 event
in Jackson Hole"*) and the tool carries **zero rows** for it (`D18`; and see `R93` for the retraction
of the 08-21 run's dating of the same event). **The desk's tilt is short the duration complex in three
buckets at once** — `UTIL` UW, `RE` UW, `STPL` N — which `PREMORTEM §3-d` identifies as a
correlated-UW pattern. **A one-way tilt into a known binary is a protocol violation.**

| | |
|---|---|
| **Frozen observable** | `EW{XLU, XLRE, XLP}` **3-session excess return vs `SPY`**, settled closes, window **2026-08-26 close → 2026-08-31 close** |
| **Branch A (AGAINST US)** | **≥ +1.653pp** (252-obs **p85**) — the three underweights rip **together**; the correlated-UW pattern is real and it cost us |
| **Branch B (with us)** | **≤ −1.757pp** (252-obs **p15**) — the credibility story does not land and the repression holds |
| **Branch C** | between — the disclosed favourite |
| **`D93` before freezing** | trailing 252: mean **−0.156** · sd **1.754** · p05 −2.893 · **p15 −1.757** · p50 −0.168 · **p85 +1.653** · p95 +2.719 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **−0.225 = the 49th percentile — dead centre.** ★ Both branches equally reachable, the most informative starting state this desk has registered in weeks (compare `S88`, which started at the 100th percentile and could only produce its favourite) |
| **⚠ Window honesty, stated at registration** | **July PCE (2026-08-28) falls INSIDE this window and is deliberately NOT an anti-signal.** Making it one would be a designed-to-void clause — the `D300-KR` defect that VOIDed `S91` and `S93` on the same day this row was written. **Jackson Hole and PCE are one macro event-cluster for the duration complex, and this bracket owns both.** Discovered at registration, not at scoring |
| **Anti-signal (VOID)** | an **intermeeting FOMC action** or an **emergency Treasury operation** (not a scheduled buyback) inside 08-26 → 08-31. ⚠ **Base rate checked (`D300-KR`)**: no FOMC meeting falls inside the window; the buyback expansion already executed on **2026-08-19** (`M797`); a *discretionary emergency* operation inside four sessions is not the base case ⇒ **the clause is not near-certain to fire** |
| **Implied move** | **not pulled** — these are sector ETFs and `--positioning` was run on single names only. **The gap is stated rather than glossed**; the threshold is distribution-based |
| **Information content (`L3`)** | **HIGH and symmetric.** A falsifies three sector verdicts at once; B confirms them. ⚠ **Warsh's speech is deliberately NOT an anti-signal — it is the event** |
| **Owner** | `industry_US` |

## S113 — ★★ The semis chain into `NVDA` 08-26, registered because the straddle path is structurally broken · ARMED · → settle **2026-09-01**

**Why it exists.** `S103` brackets `NVDA` **the name** with **hand-set ±5.0pp bands**, and `D295`
obliged a straddle re-derivation for a third run. **This run measured why that is impossible**:
`module_flow NVDA --positioning` returns **예상변동 ±1.6%, 만기 2026-08-24, D2** for an **08-26**
event — the tool selects the **nearest** expiry, not the first expiry covering the event (`D315`;
`NEM` and `MSTR` both returned 08-28 on the same day, so an 08-28 chain exists). ⇒ **`S103` is left
FROZEN (`D242`)** and this row is registered on **the chain** with properly derived bands, which is
additive rather than a re-freeze.

| | |
|---|---|
| **Frozen observable** | **`SMH` 5-session excess return vs `SPY`**, settled closes, window **2026-08-25 close → 2026-09-01 close** (the 08-26 print sits inside it) |
| **Branch A (AGAINST our IT UW)** | **≥ +4.461pp** (252-obs **p85**) — the complex re-rates on the print and the UW was the wrong verdict at the 12th percentile |
| **Branch B (with us)** | **≤ −2.627pp** (252-obs **p15**) — the de-rate continues through the catalyst |
| **Branch C** | between |
| **`D93` before freezing** | trailing 252: mean **+1.063** · sd **3.740** · p05 −5.413 · **p15 −2.627** · p50 +1.573 · **p85 +4.461** · p95 +7.172 |
| **State at registration** | **−3.293 = the 12th percentile — already BELOW p15.** ⚠ **Branch B is therefore only 0.67pp away and is declared LOW-INFORMATION at registration**; **branch A carries the row** and needs **+7.75pp**, a genuine reversal |
| **Implied move** | 🚫 **UNUSABLE, and the reason is recorded rather than glossed**: `NVDA` **±1.6%, expiry 2026-08-24, D2 — before the event** (`D315`). **The threshold is distribution-based and is labelled as such** |
| **Anti-signal (VOID)** | a **US export-control announcement on advanced semiconductors** inside 08-25 → 09-01 ⇒ a policy read, not an earnings read. ⚠ **Base rate**: moderate but not near-certain, and the clause is keyed to a **specific dated action**, not to "an event occurring" |
| **Information content (`L3`)** | **Asymmetric and disclosed**: A can falsify the IT UW; B can only confirm what the state already shows. Registered anyway because A is exactly the outcome that convicts a live verdict carried into a binary while the desk holds four names in the sector |
| **Owner** | `industry_US` |

## S114 — ★★ The steel/tariff bracket, registered because it points at a HELD name · **SETTLED FIRED-B** (scored 2026-09-04, folded into the master scoring log by the 2026-09-06 `industry_US` run — `D472` header hygiene) · → settle **2026-09-03**

**Why it exists.** `EVENT_ALPHA` CARD 4: the US–Canada tariff thread (peak **23 outlets 08-19**)
resolved across 08-17 → 08-21 toward a **CUT on metals and autos**, and **`NUE` is held**. The desk
should not carry a position whose live thread runs against it without a dated test.

🚨 **INTERPRETATION RE-STATED THE SAME DAY, BEFORE THE SETTLE, AND WITHOUT MOVING A THRESHOLD.**
On **2026-08-22** the arc reversed: **the US imposed 50% tariffs on $20bn of Canadian goods after talks
failed, and Canada is retaliating dollar-for-dollar** (`M808`; `aljazeera`/`bbc`/`euronews`, 15-outlet
cluster). ⇒ **Branch A was labelled *"the tariff bid is being removed."* Under the facts as of the
registration date it would instead mean *the steel pair failed to rally on a tariff that should help
it*** — a materially different and more damning reading. **Branch B's meaning is unaffected.**
**Neither threshold is moved (`D242`)**; this note exists because writing it *before* the settle is the
difference between a forecast and a rationalisation (`§4c` / `D48`).

| | |
|---|---|
| **Frozen observable** | `EW{NUE, STLD}` **5-session excess return vs `SPY`**, settled closes, window **2026-08-26 close → 2026-09-03 close** |
| **Branch A** | **≤ −6.219pp** (252-obs **p05**) — the pair stays at its extreme |
| **Branch B** | **≥ +0.826pp** (252-obs **p50**) — full mean reversion |
| **Branch C** | between |
| **`D93` before freezing** | trailing 252: mean **+0.936** · sd **4.376** · **p05 −6.219** · p15 −2.978 · **p50 +0.826** · p85 +4.906 · p95 +8.488 |
| **State at registration** | **−8.628 = the 3rd percentile of 252** — already **below p05**. ⚠ **Branch A is declared LOW-INFORMATION at registration** (it only requires the extreme to persist); **branch B carries the row**, needing **+9.45pp** |
| **Implied move** | **`NUE` ±8.1%, expiry 2026-09-18, D27**, `P/C` 0.79, **IV skew +36.1 — the highest downside-fear skew this desk has pulled.** Branch B needs ~**9.45pp on the pair ≈ 1.2× `NUE`'s implied move** ⇒ **marginally outside ⇒ WEAK-INFORMATION, labelled now** rather than presented as a trigger |
| **Anti-signal (VOID)** | a **Section 232 steel action or a new steel-specific tariff** inside 08-26 → 09-03 ⇒ the opposite policy, not a discount test. ⚠ **Base rate re-assessed after `M808`: this clause is now MORE likely to fire than it was when drafted**, and that is disclosed here rather than discovered at scoring. **It is not changed** — a clause edited after the news is not a pre-registration |
| **Information content (`L3`)** | **B carries it.** ★ Registered anyway because A-persisting is exactly the outcome that convicts a live position, and this desk's rule is that a bracket which can convict us is worth the slot |
| **Owner** | `industry_US` |

### Registered and then DROPPED by this run, with the reason (rather than bracketed to look thorough)
- **Hormuz de-escalation** — `S92` (08-31) and `P89` (08-28) already carry both sides. **Duplication.**
- **`FRO` 08-28** — owned by `S109` (settles 09-02). **Duplication.** ⚠ And `FRO` has **no flow reading
  on this desk** — it is outside `us_top300` (`D314`).
- **MSCI quarterly review 08-31** — constituent changes are announced ~2 weeks ahead and **this desk
  has not read the announcement**; neither branch could change a conclusion on evidence we hold.
  **Dropped for our own unreadiness, stated as such rather than as the event being unimportant.**


---

# Registered 2026-08-23 by the `industry_US` PREMORTEM — **`S115` · `S116` · `S117`**

> ⚠ **Write mode append-only** — the `D165` pre-commitment made after the 2026-08-05 truncation
> incident. Nothing above this line was read into memory and rewritten.
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md`, `llm_outputs/**`, `REPORT/**`: `S115` `S116`
> `S117` returned **0 hits**. Highest existing `S114` (registered 2026-08-22).
> ⚠ All prices settled **2026-08-21**, one provider (`yfinance`, `auto_adjust=False`), benchmark named
> inline (`C1`). Implied moves are the ATM straddle of the **first expiry spanning each event**,
> read from the option chain at the strike nearest the 08-21 settled close.
> ⚠ **`D295` context**: `module_flow --positioning` returns the **08-24** expiry for an **08-26** event
> (`D315`, 4th run), so the straddles below were derived directly from the chain instead.

## `S115` — ★★★ The `NVDA` print, with a threshold the options market cannot already contain · ARMED · → settle **2026-08-27**

*Successor to `S103`, whose hand-set ±5.0pp bands sit INSIDE the ±6.11% implied move and are therefore
**pre-declared NO-INFORMATION**. Per `D242` `S103` is NOT re-banded and still settles as registered;
what is recorded is that its verdict may not be read as a surprise in either direction.*

| Field | Value |
|---|---|
| **Event** | `NVDA` FQ results, **2026-08-26** — corroborated to two bodies (`yahoo_finance` 08-21 *"Something Big Could Happen To NVIDIA Stock on August 26"*; 08-16 *"…After Aug. 26"*), per `D311` |
| **Frozen observable** | `NVDA` **1-session return** on the first settled close after the print (**2026-08-27**), and its **excess vs `SPY`** on that session |
| **Implied move at registration** | **±6.11%** — 08-28 expiry, K=215, straddle **$13.12**, spot **214.72**, ATM IV **0.606 / 0.588**. Control: the 08-24 expiry (does not span the print) prints ±1.61% at IV 0.280 ⇒ **event premium ratio 2.16×** |
| **Branch A** | 1-session return **≥ +7.0%** — a real upside surprise, **outside** the implied move |
| **Branch B** | 1-session return **≤ −7.0%** — a real downside surprise, outside the implied move |
| **Branch C** | between — **disclosed as the heavy favourite (~70%)** |
| **Information grade** | **MEDIUM-HIGH**, and asymmetric in *content*: branch A **with** gross-margin expansion falsifies `P90`; branch A **with** flat margin confirms it. ⇒ **scored jointly with `P90`**, declared here at registration |
| **Anti-signal (VOID)** | `NVDA` does not report on 2026-08-26, **or** US cash equities do not trade a full session on 2026-08-27. ⚠ Base rate very low; keyed to a **publication/venue failure**, not to an event occurring (`D300-KR`) |
| **Settle** | **2026-08-27** |

## `S116` — ★★★ The bracket the desk's own calendar could not have written: `MRVL` 08-27 · ARMED · → settle **2026-08-28**

| Field | Value |
|---|---|
| **Event** | `MRVL` FQ2 results, **2026-08-27**. 🚨 **Absent from `catalyst_calendar --days 10`** — this row exists because the calendar was audited against `yfinance` and then against a body (`yahoo_finance` 08-19: *"Dear Marvell Technology Stock Fans, **Mark Your Calendars for August 27**"*), not because it was read |
| **Frozen observable** | **`MRVL` − `AVGO` 1-session excess** on the first settled close after the print (**2026-08-28**), each vs its own prior close |
| **Why a SPREAD** | `D308`'s registered remedy — a node-vs-name question written on a raw excess forces the anti-signal to arbitrate what it cannot see. Here the shared AI-semis move cancels and only the **relative franchise move** reaches the branches |
| **Implied move at registration** | `MRVL` **±11.31%** — 08-28 expiry, K=235, straddle **$26.80**, spot **237.04**, ATM IV **1.122 / 1.096** (the highest on the board). `AVGO` 08-28 ±4.51% (IV 0.461) |
| **Branch A** | `MRVL` − `AVGO` ≥ **+12.0pp** — the share shift is confirmed and widens |
| **Branch B** | `MRVL` − `AVGO` ≤ **−12.0pp** — the share shift was over-priced; `AVGO`'s −14.7 rs60 was a discount, not a franchise loss |
| **Branch C** | between |
| **Information grade** | **HIGH** — the only row on the board where **both** branches change a standing thesis on a **held** name. `AVGO` has been carried as *"AI-compute-EPICENTER"* with **its customer unnamed for the life of the position** (`W4`), and the customer (Alphabet) dual-sourced to `MRVL` on 2026-08-19 with a **$12.2bn / 59m-share warrant that does not fully vest until Google buys $120bn of chips** (`yahoo_finance` 08-20, 08-21) |
| **Anti-signal (VOID)** | An **announced acquisition of, or by, either company** inside 2026-08-24 → 2026-08-28. ⚠ Base rate low; keyed to a **named corporate action** |
| **Settle** | **2026-08-28** |

## `S117` — ★★ Does the memory IV premium belong to memory, or is it `NVDA` beta? · ARMED · → settle **2026-08-27**

| Field | Value |
|---|---|
| **Event** | The **2026-08-26** `NVDA` print, read through a name that is **not** reporting |
| **Registration measurement** `[measured]` | On the **08-28 expiry**, `MU` ATM IV **0.650 / 0.643** vs `NVDA` **0.606 / 0.588** — **the non-reporting memory name carries ~4.5 vol points MORE implied event risk than the company actually reporting.** `MU`'s own print is **2026-09-24**, outside the expiry |
| **Frozen observable** | `MU` **1-session excess vs `NVDA`** on **2026-08-27**, each vs its own 2026-08-26 close |
| **Branch A** | `MU` − `NVDA` ≥ **+3.0pp** — the information was about **memory**; the buyer's print told the market more about the supplier than about the buyer |
| **Branch B** | `MU` − `NVDA` ≤ **−3.0pp** — it was `NVDA` beta and `MU` is a levered follower |
| **Branch C** | between — **disclosed as the favourite** |
| **Information grade** | **MEDIUM, disclosed.** C is likely. Registered because **A is the only observable this desk owns that can separate `P90`'s cost story from a generic AI-demand story using PRICE rather than narrative** |
| **Anti-signal (VOID)** | A `MU`-specific dated announcement (guidance update, capacity announcement, M&A) inside 2026-08-24 → 2026-08-27. ⚠ **Base rate checked**: `MU`'s last dated corporate item in the window's news is *"Micron Quietly Pours $10 Billion Into Next Big Move"* (`yahoo_finance` **2026-08-20**), i.e. **before** the window opens. **The clause is not near-certain** |
| **Settle** | **2026-08-27** |

### ⚠ Brackets deliberately NOT registered this run, with reasons (information-content rule)
- **July PCE 08-28** — already carried both-sided by `P86` (registered 08-22). A second row double-counts one observation.
- **Jackson Hole 08-27→29** — already carried by `S112` (registered 08-22, settles 08-31) **on its true dates**. The event is covered even though `catalyst_calendar` cannot see it; the gap is in the **tool**, not in the scenario coverage.
- **`FRO` 08-28** — **no branch would change any conclusion**: the desk holds no tanker and carries no tanker proposition.
- **MSCI review 08-31** — index-mechanical, no directional content.
- **The RE/UTIL long-duration correlation** — the rate leg is already bracketed by `S112` and `P91`.


---

# Rows added by the 2026-08-24 `industry_US` run

> ⚠ **Append-only** (`D165`). **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` ·
> `REPORT/**`: `S118`–`S123` **0 hit** in all three trees. Current highest **`S117`** (2026-08-23
> `industry_US`). IDs allocated against **every** existing row in **both** `SCENARIOS*.md` files
> (`D76` collision class).
> ⚠ **Every threshold below is frozen at registration.** A bracket whose threshold moves after the
> print is a description wearing a forecast's clothes.

## `S74` — ANNOTATED AND SCORED (thresholds UNCHANGED; the original row above is not rewritten)

**`S74` · event date 2026-08-24 · `FIRED-C` · scored 2026-08-24 by `industry_US` HANDOVER.**

- **Observed, branch by branch** (`M857`; all news calls `--scope foreign`, **outside a sweep window**):
  - **A leg 1** — *a dated US stand-down or partial lift of the naval blockade*: 🚫 **opposite
    direction.** The US announced its **strictest-ever** sanctions round; Treasury Secretary Bessent
    published an FT op-ed calling it an *"economic D-Day"*; press conference **14:00 ET 08-24**
    (`hellenicshipping`, `dw`, `aljazeera`, `guardian`, `scmp` bodies).
  - **A leg 2** — *a compensation framework announced*: 🚫 **a demand, not a framework.** Iran's
    president restated the conditions 08-21 — *"including Iranian control over Hormuz and financial
    compensation for the war"* (`euronews` body). No counterparty, no framework.
  - **A leg 3** — *an **unconditional** Iranian reopening statement*: 🚫 **explicitly conditional.**
    Iran issued **special permits for SOME Iraqi tankers**, number of vessels and schedule
    **undisclosed** (IRNA via Reuters 08-22; `aljazeera` 08-22, `hellenicshipping` 08-23 and 08-24),
    while NSC Secretary **Mohsen Rezaee** said **"not a single drop of oil will be exported"** through
    Hormuz *"if the economic war continues."*
  - **B leg 1** — *a **formal** US refusal of the two named conditions*: ⚠ **fails the letter.**
    Sanctions escalation plus *"presses China to help reopen Hormuz"* (`toi` 08-21) is a hardening;
    **no document or statement formally addresses and refuses** the blockade-lift and compensation
    demands.
  - **B leg 2** — *a strike on a transiting **VLCC***: ⚠ **fails on vessel class, measured precisely.**
    A transiting vessel **was** struck fatally — **`MINOAN DIGNITY`** (IMO 9294484), Liberia-flagged
    **bulk carrier**, 76,801 DWT, projectile into the engine room outbound in the southern corridor
    overnight **08-17→18**, **chief engineer killed**, UKMTO-confirmed — and **`AMARA`** (IMO 9333280),
    a 186 m **products tanker**, was **boarded and seized** near Qeshm 08-17, the first confirmed
    Iranian seizure since 06-22. **The VLCCs in the same report ABORTED transits; none was struck.**
    (`SKIROS`, 159k DWT, was struck by a **Ukrainian** drone at **Novorossiysk** — wrong theatre.)
  - **C** — *neither, by 2026-08-24*: ✅ **this is what happened.**
- **Verdict: `FIRED-C`.** Per the row's own meaning line, C = `AMBIGUOUS` / **no conclusion changes**;
  **no grade moved on ENRG or INDU from this row.**
- 🚨 **The row does not settle silently: its registered anti-signal (a) FIRED.** S74 wrote *"if a
  reopening happens with **no** statement on either named condition, the conditions were never the
  binding variable and this row's whole framing is wrong."* **A partial reopening happened on
  bilateral Iraqi diplomacy** — IRNA states the permits followed *"repeated requests by the Iraqi
  government through various diplomatic channels"*, and Iraq's parliament speaker asked Ghalibaf for
  *"special status"* in Baghdad on **08-19**. **Neither named condition appears anywhere in that chain.**
- ★★ **And the same night DRIFT found a FOURTH channel** (`M883`): **China and Jordan jointly called
  for the Strait's reopening** in a statement issued during King Abdullah's Beijing visit with Xi
  Jinping (`scmp`, 21:48 HKT 08-24) — again naming neither condition. **China buys ~80% of Iran's
  shipped oil.**
- ⇒ **Carried forward, unresolved and not laundered**: the two IRGC conditions gate the Strait for the
  general fleet, but they are **demonstrably not the binding variable** for at least two channels.
  **The successor bracket is `D338`'s, and it belongs to PREMORTEM.**
- 🚨 **`S74`'s retirement leaves `S8` — undated for 23 runs — as the desk's ONLY general-fleet Hormuz
  bracket.** `S8` is human-gated (P5) and is **not** touched, re-dated or re-frozen by this row.

---

## `S118` — ★★★ Is `NVDA`'s print about the PRINTER or about MEMORY? · ARMED · → settle **2026-08-28**

Registered **2026-08-24 by the `industry_US` PREMORTEM** (Lens 2, mandatory bracket — `NVDA` is a
🔀binary at **D-2**). `grep S118` → **0** across all files at write time.

**Why it exists, and why it is NOT a duplicate.** `S115`/`S117`/`P90` bracket NVDA's own print and the
memory-cost mechanism. **This row brackets the RELATIVE pricing** measured today (`M874`): on the
identical 2026-08-28 expiry, **three memory/storage names with no scheduled event carry HIGHER ATM
implied volatility than the name that actually prints** — `SNDK` **0.926**, `WDC` 0.880, `MU` 0.770
against `NVDA` **0.692** — while **memory/storage `participation` is 0.0% (0 of 4)**.

**Frozen observable**: `EW{MU, SNDK, WDC}` **2-session excess return vs `NVDA`**, over
**2026-08-26 close → 2026-08-28 close**.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (the print is about MEMORY)** | `EW{MU,SNDK,WDC}` − `NVDA` **≥ +6.50pp** | **Falsifies the `AI-compute-EPICENTER` label as the right unit** — the money would be saying the cycle's marginal information lives one layer back |
| **B (the print is about NVDA)** | the same spread **≤ −6.50pp** | **Falsifies `S117`/`M874`'s options-market inference** |
| **C** | between | **the favourite, disclosed** (`L3`); the band spans 13pp because all four implied moves are large |

- ★ **Threshold is OUTSIDE the implied move, and stated as such**: `NVDA`'s own 08-28 straddle is
  **±6.13%**, so a **6.50pp RELATIVE** gap requires more than NVDA's entire priced move in one
  direction. **It can carry information rather than re-describe what is priced.**
- 🚨 **The implied move was read from the option chain directly, NOT from the desk's tool.**
  `module_flow NVDA --positioning` returned **`±1.3% (expiry 2026-08-24, D0) → complacent, little
  fuel`** — an expiry that expires the same day, two days before the print, **4.7× too small**
  (`M873`, `D315` 5th run).
- **Anti-signal (VOID)**: a **memory-maker pre-announcement or guidance revision with a named date**
  (`MU`, `SNDK`, `WDC`, Samsung or SK hynix) inside 08-24 → 08-28. ⚠ **Base-rate checked**: `MU` does
  not print until **09-24** and no memory name has a scheduled event in the window ⇒ a genuine
  low-probability void, not an escape hatch.
- **Information content (B4)**: **neither branch merely confirms.**
- ⚠ **Named non-redundancy (`D343`)**: `S118` is not redundant with `P90` — `P90` asks *what the >15%
  price increase means for NVDA's margin*; `S118` asks *which chain layer the market gets paid on*.
  **`S118` can fire while `P90` fires either way.**
- **Owner**: `industry_US`.

## `S119` — ★★ Bessent's sanctions press conference, **D-0** · ARMED · → settle **2026-08-27**

Registered **2026-08-24 by the `industry_US` PREMORTEM** (mandatory bracket — a **≤48h binary**, in
fact **D-0**, firing inside this run's own working window). `grep S119` → **0** at write time.

**Why it exists**: a dated binary that **`catalyst_calendar` does not carry** (`M872`), on the axis
carrying the desk's only OW with a live macro driver. Recovered from a wire body that named the time
of day: *"Bessent is expected to unveil the new sanctions against Iran during a press conference at
**14:00 ET (18:00 GMT) on Monday**"* (`hellenicshipping` 08-24).

**Frozen observable**: the **equal-weight Energy basket's 3-session excess return vs `SPY`**, over
**2026-08-24 close → 2026-08-27 close**.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (escalation prices — ENRG OW helped)** | Energy 3-session excess vs `SPY` **≥ +2.60pp** | the war-premium leg is live and re-prices |
| **B (already priced / the exception channel dominates — ENRG OW hit)** | **≤ −2.60pp** | **falsifies the war-premium leg of the ENRG OW directly** |
| **C** | between | the favourite, disclosed |

- **Threshold derivation, stated**: measured trailing-60 **5-session** Energy excess has mean
  **+0.607** and sd **4.325** ⇒ 3-session sd ≈ **3.35**, mean ≈ **+0.36**; **±2.60pp ≈ ±0.60σ.**
- **Information content**: **B falsifies**, and **B is the branch this run's own evidence points at** —
  the tape already sold crude on the Iraqi-permit news (**Brent −1.3% to $93.16**, 04:32 ET, a LIVE
  INTRADAY print) **before** the presser. **A confirms and is graded the weaker branch. Registered
  anyway** because a D-0 binary on the desk's largest live macro tilt with no bracket is exactly the
  violation this stage exists to prevent.
- **Anti-signal (VOID)**: the presser is **postponed or cancelled**, or a **US–Iran direct-talks
  announcement with a named date** lands in the window. ⚠ Base-rate checked: the presser is confirmed
  in a body **with a time of day**, so postponement is the low-probability leg.
- **Owner**: `industry_US`.

## `S120` — ★★ Jackson Hole: Warsh's first speech as Chair · ARMED · → settle **2026-08-28**

Registered **2026-08-24 by the `industry_US` PREMORTEM.** `grep S120` → **0** at write time.
**Why it exists**: `theme-age "Jackson Hole"` reads **🟡ACCELERATING 14.9×** (base 296), the board's
second-fastest term, while `theme-age "Warsh"` reads ⚪ECHO 0.85× on a 3,628 base — **a 17.5× ratio
difference on one event from term width alone** (`M861`) — and **`catalyst_calendar` has missed the
event for three consecutive runs** (`M872`).

**Frozen observable**: `DGS30` **and** `T10YIE` from `[FRED]`, at the **first observation where BOTH
series carry 2026-08-28**.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (supply / term premium dominates)** | `DGS30` **≥ 5.31** (its 365-day maximum; 08-20 value 5.23) **AND** `T10YIE` **≤ 2.38** | **falsifies any residual "the long end is inflation" reading** |
| **B (Warsh read dovish; the long end retraces)** | `DGS30` **≤ 5.10** **AND** `T10YIE` within **2.28–2.40** | **falsifies `P94` and this run's supply framing** |
| **C** | between | the favourite, disclosed — `DGS30`'s realised 8-observation range is **5.19–5.31** |

- ⚠ **The observation-lag clause is written INTO the row** (`D333-KR`/`M858`): the H.15 constant-maturity
  family publishes **at least one business day behind** `T10YIE`. **This row settles on the first
  observation where BOTH carry the date, and that rule is frozen here rather than discovered at
  settle** — which is precisely why `S102` has sat unsettled for five runs.
- **Anti-signal (VOID)**: an **intermeeting Fed action** or a **Treasury refunding announcement**
  inside the window. ⚠ **Base-rate checked and NOT remote** — `Treasury buyback` is the board's only
  🟢FRESH theme (age 5, base 201) and `brief` carried *"Treasury may tap $1 trillion cash account for
  bond buybacks."* **Disclosed as live rather than assumed away.**
- ⚠ **Named non-redundancy (`D343`)**: `S120` settles **08-28** and `P94` settles **08-27** on the same
  `DGS30`/`T10YIE` pair. **If both fire the same way that is ONE observation, not two.** Registered
  here so no later stage double-counts it.
- **Owner**: `industry_US`.

## `S121` — ⚠ GRADED AND **DROPPED** before registration. **ID consumed, deliberately unused.**

**Intended**: a July PCE bracket (08-28).
**Dropped, and the reason is the finding.** `P67`, `P81`, `P85`–`P89` and `S116` **already settle on
2026-08-28**, all keyed to the same print, alongside `FRO` earnings. **The desk holds SEVEN rows on
one binary.** Per the standing rule — *"if neither branch would change the conclusion, the event is
not worth bracketing"* — an eighth adds no information and would inflate apparent coverage.
⇒ **`D343`: date-clustered brackets resolving together read as seven confirmations from n ≈ 1 (`B3`).**
**The ID is left permanently unused so it cannot be silently re-allocated.**

## `S122` — ★★ Shell's $8bn US chemicals sale: does `XOM`'s "control" role survive? · ARMED · → **2026-09-30**

Registered **2026-08-24 by the `industry_US` PREMORTEM** (Lens 1, on an object the **blind-spot pass**
surfaced — `burst` returned `CHEMICALS` at **z 13.2**, the board's highest, 100% market relevance,
against a term table with no chemicals bucket). `grep S122` → **0** at write time.

**Object**: Shell is selling its **US chemicals business — ~$8bn, four Louisiana sites — and the named
interested parties are `XOM`, LyondellBasell and Apollo** (FT 08-24, via `yahoo_finance`,
`seekingalpha`, `oilprice`, `investing_en` bodies + a `bloomberg` title). `chain-hop chemicals`
independently surfaced **`APO`** as a one-hop candidate while `XOM` was **headline-named 22 times**.

**Frozen observable**: a **definitive agreement naming the buyer and the price**, reported in **≥2
outlet BODIES**, by **2026-09-30**. Grade **`[news]`, not `[measured]`** — no price threshold.

| Branch | Threshold | Meaning |
|---|---|---|
| **A** | `XOM` is the buyer | **`XOM`'s standing 🔴RESOLVED *control* status is FALSIFIED** — a control does not commit $8bn to a downstream asset — and its ledger row (`A.flow미도착` → 09-16) must be re-argued or retracted |
| **B** | a non-`XOM` buyer, **or** no definitive agreement by 09-30 | Shell portfolio news with no US read-through; EVENT_ALPHA Card 8 is void |
| **C** | an agreement naming `XOM` **within a consortium** | disclosed as a live outcome, not a dodge |

- **Why it matters**: `XOM` is carried in this desk's standing view explicitly as *"a control, not a
  bet"*, **and its own OBV is dispersing (−0.101) while its sector accumulates**. Alongside `brief`'s
  08-23 head item *"One of Exxon's Biggest Oil Fields Is Running Out of Room"* (11 articles / 7
  outlets), the **capital-allocation** story on `XOM` is two-sided and unowned.
- **Information content**: **A falsifies a role this desk assigned itself**, which is the most
  expensive kind of error to leave standing. **B falsifies the card.** Neither confirms.
- **Anti-signal (VOID)**: Shell **withdraws the asset from sale** with a named announcement.
- 🚨 **`LYB` and `DOW` — the two named US counterparties — are OUTSIDE `us_top300` and therefore
  untaggable** (`D341`).
- **Owner**: `industry_US`.

## `S123` — ★★ The trade war's IMPLEMENTATION, which no existing row reaches · ARMED · → settle **2026-09-12**

Registered **2026-08-24 by the `industry_US` PREMORTEM.** `grep S123` → **0** at write time.
**Why it exists — `D342`**: `P92` and `P93` both settle **2026-08-28**, and **Canada's retaliation
takes effect 2026-09-08** (`aljazeera` 08-23, named effective date; list names steel, dairy,
appliances, agricultural goods — `dw` 08-22) (`M869`). **Both rows can only measure the announcement.
No row on this board spans the effective date.**

**Frozen observable**: the **equal-weight Industrials basket's 5-session excess vs `SPY`**, over
**2026-09-05 close → 2026-09-12 close** — a window **straddling 09-08**.

| Branch | Threshold | Meaning |
|---|---|---|
| **A (implementation prices — INDU UW− right for the right reason)** | Industrials excess **≤ −3.10pp** (= **−2.0σ** on the trailing-60 mean **+0.437** / sd **1.681**; its 08-21 reading is −1.736) | distinguishes a transmission story from an announcement story, which `P93` structurally cannot |
| **B (implementation is a non-event)** | Industrials excess **≥ +0.44pp** (at or above its own trailing mean) over the same window | **falsifies the INDU UW−'s trade rationale entirely** — the sector would have absorbed a 50% tariff regime taking effect |
| **C** | between | the favourite, disclosed |

- **Anti-signal (VOID)**: a **US–Canada agreement with a named effective date**, or a **US
  proclamation with a named effective date excluding Canada**, before 09-08. ⚠ **Base-rate checked**:
  *"Canada Turned Down a US Tariff Deal"* (08-23 head) — a deal was live and was **refused**.
- ⚠⚠ **Correlated with `P93`, flagged so it is not double-counted**: if `P93`-A and `S123`-A both fire,
  that is **ONE compounding object measured twice**, not two independent confirmations.
- ⚠ **Scope gap named rather than left**: this row is keyed to **Industrials**. **The Staples /
  agricultural leg of the same 09-08 event is UNBRACKETED**, and `ADM` — the chain's left edge — is
  already that sector's second 🔴 (flow −0.689, rs20 −10.2).
- **Owner**: `industry_US`.


---

# Registered 2026-08-25 by the `industry_US` PREMORTEM — **`S124` – `S126`**

> ⚠ **Append-only** (`D165`). Nothing above this line was read into memory and rewritten.
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`:
> `S124` `S125` `S126` returned **0 hit in all three trees**. Current highest **`S123`** (2026-08-24).
> ⚠ **Language: English** — the US desk's documented practice.
> Full prose, D93 baselines and branch grading live in
> `llm_outputs/2026-08-25/industry_US/BLINDSPOT_PREMORTEM.md §2`.

## S124 — ★★★ Does IT's breadth repair through its own two prints? · ARMED · → settle **2026-08-31**

The row that tests this run's ONLY verdict change (`IT` N → UW, taken on 43 of 56 names negative).

| | |
|---|---|
| **Frozen observable** | COUNT of `us_top300` Information Technology names (n=56) with a positive **5-session excess vs `SPY`**, settled closes, at the **2026-08-31** close |
| **Branch A (the UW is wrong)** | **≥ 30** (trailing-252 median) — breadth returns to normal through the `NVDA` 08-26 and `MRVL` 08-27 prints |
| **Branch B (the UW is right)** | **≤ 13** — no repair at all |
| **Branch C** | 14–29 |
| **D93 before freezing** | trailing 252: mean **29.5** · sd **9.0** · p05 **13** · p15 **20** · p50 **30** · p85 **39** · p95 **43** ⇒ **A ≈50% / B ≈6% / C ≈44%. A is the favourite, disclosed. B is the rare branch AND the one that vindicates the desk** |
| **State at registration** | **13 of 56 = the 5.6th percentile of two years** |
| **Implied move** | `NVDA` **±6.13%** and `MRVL` **±13.3%**, both expiry 2026-08-28 (D3). ★ The observable is a **cross-sectional COUNT, which no straddle prices** ⇒ the threshold is outside the implied move by construction |
| **Information content (B4)** | Both branches change a conclusion. Deliberately **not** a fifth reading of the `NVDA` print (`S79`/`S103`/`P90`/`S118` own it) — this row owns the **sector-breadth consequence** |
| **Anti-signal (VOID)** | a **GICS reclassification moving ≥3 names into/out of Information Technology**, or a market-wide trading halt, inside 08-25 → 08-31. Base rate checked (`D300-KR`): **MSCI's 08-31 review falls inside the window and does NOT change GICS assignment**, so it is explicitly not a voider. The `NVDA`/`MRVL` prints are deliberately NOT anti-signals — they are the event |
| **Non-redundancy (D343)** | 08-31 carries `S92` `S94` `S104` `S112` + the MSCI review; **all four are single-name/pair rows, `S124` is the only cross-sectional breadth row on that date** |
| **Owner** | `industry_US` |

## S125 — ★★ The agricultural half of the trade war, unbracketed for a third run · ARMED · → settle **2026-09-11**

Fills the gap `D342` named twice: `S123` brackets the Industrials leg; the Staples/agricultural leg had no row.

| | |
|---|---|
| **Frozen observable** | **`ADM` 5-session excess vs `XLP`** (benchmark named inline — the sector, not the index; the question is intra-Staples transmission), settled closes, at the **2026-09-11** close. The window **contains Canada's 2026-09-08 effective date** |
| **Branch A (the ag leg was priced in advance)** | **≥ +0.602** (trailing-252 p50) |
| **Branch B (the ag leg is the live transmission channel)** | **≤ −6.146** (trailing-252 p05) |
| **Branch C** | between |
| **D93 before freezing** | trailing 252: mean **+0.555** · sd **3.849** · p05 **−6.146** · p15 **−3.426** · p50 **+0.602** · p85 **+4.461** · p95 **+6.949** ⇒ **A ≈50% / B ≈5% / C ≈45%** |
| **State at registration + branch grading** | **−6.511 = the 4.4th percentile, ALREADY inside branch B's region** ⇒ **B is the LOW-information branch and A is the informative one, stated at registration rather than discovered at scoring (B4).** The row is a **persistence** test |
| **Implied move** | **none readable** — `ADM` has no event-dated chain for 09-08. **Stated as unavailable rather than fabricated (P4, D2)** |
| **Anti-signal (VOID)** | a **US–Canada agreement removing agricultural goods from the retaliation list**, or an `ADM`-specific corporate action (M&A, guidance withdrawal, restatement) inside the window. Base rate: the tariff thread is **accelerating, not resolving** (`theme-age "Canada tariff"` **10.99×** on an 85 base, up from 9.86×) ⇒ not near-certain |
| **Non-redundancy (D343)** | 09-11 carries **zero** rows. Correlated with `S123` (09-12, Industrials leg) — **one policy event, two sectors; if both A-branches fire that is ONE object measured twice**, named in advance |
| **Note** | `ADM` is **not** a desk position and this row hands **no name to BET** (P4) |
| **Owner** | `industry_US` |

## S126 — ★★ August payrolls: is the Industrials underweight a tariff call or a cycle call? · ARMED · → settle **2026-09-04**

| | |
|---|---|
| **Frozen observable** | **`XLI` 5-session excess vs `SPY`**, settled closes, at the **2026-09-04** close (August NFP prints that morning) |
| **Branch A (the UW− is on the wrong side of a cycle)** | **≥ −0.087** (trailing-252 p50) |
| **Branch B (the weakness is structural, not a dislocation)** | **≤ −2.500** (trailing-252 p05) |
| **Branch C** | between |
| **D93 before freezing** | trailing 252 of `XLI exc5` vs `SPY`: mean **+0.012** · sd **1.619** · p05 **−2.500** · p15 **−1.572** · p50 **−0.087** · p85 **+1.767** · p95 **+3.121** ⇒ **A ≈50% / B ≈5% / C ≈45%** |
| **State at registration + branch grading** | **−2.738 = the 2.8th percentile**, already below p05 ⇒ **B is the low-information branch, A is the informative one (B4)** |
| **Implied move** | `XLI` has **no NFP-dated straddle** ⇒ stated as unavailable rather than invented (`D2`) |
| **Why the row exists** | `INDU UW−` is the desk's stated live transmission channel for the trade war and **every existing test settles on the wrong date**: `P92`/`P93` on **08-28, eleven days BEFORE the tariffs take effect** (`D342`), `S123` on **09-12, after**. Nothing separated *"weak because of tariffs"* from *"weak because the cycle is weak"* — **NFP is the one dated event in the window that moves the second and not the first** |
| **Information content** | **A falsifies** the tariff attribution (recovery on labour data, before any tariff takes effect). **B does not confirm the tariff story** — it only rules out the labour explanation — **and that asymmetry is stated, not glossed** |
| **Anti-signal (VOID)** | an **intermeeting FOMC action**, or a **BLS delay/cancellation of the August employment report** inside the window. Base rate checked: no FOMC meeting falls inside; the BLS calendar carries 09-04 as scheduled ⇒ not near-certain |
| **Non-redundancy (D343)** | 09-04 carries **zero** rows. Against `S123`: different date, different driver (labour vs tariff implementation), different construction (ETF vs equal-weight constituents) |
| **Owner** | `industry_US` |

---

# Registered 2026-08-26 by the `industry_US` PREMORTEM — **`S127` · `S128`**

> ⚠ **Append-only write** (`D165`), text staged in a scratchpad first (`D357` — the 2026-08-05
> truncation mechanism is still live and this run does not rely on luck).
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`: `S127` `S128`
> → **0 hits**. Highest existing **`S126`** (2026-08-25 `industry_US`).
> ⚠ **Language: English** — the US desk's documented practice.

## `S127` — ★★★ `AVGO` 2026-09-02: the held name with the book's worst `rs60` and, until now, no row · ARMED · → settle **2026-09-08**

| Field | Value |
|---|---|
| **Event** | `AVGO` FQ3 results, **2026-09-02**. **HELD** (`AI-compute-EPICENTER`). The registration obligation was recorded by the 2026-08-25 run and carried into `HANDOVER §2c` on 08-26 |
| **Frozen observable** | **`AVGO` 5-session excess return vs `SPY`**, settled closes, `auto_adjust=False`, window **2026-09-01 close → 2026-09-08 close** (the print falls inside) |
| **Branch A (the de-rate was a discount)** | excess **≥ +5.928pp** (trailing-252 **p85**) |
| **Branch B (the de-rate was a franchise loss)** | excess **≤ −4.922pp** (trailing-252 **p15**) |
| **Branch C** | between = **the favourite, disclosed** |
| **`D93` before freezing** | `AVGO` exc5 vs `SPY`, trailing 252 settled windows to 2026-08-25: mean **+0.281** · sd **6.023** · p05 −8.036 · **p15 −4.922** · p50 −0.341 · **p85 +5.928** · p95 +10.033 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **−5.920 = the 9.9th percentile of 252** — it enters its own print **already inside branch B's zone**. Disclosed now, not discovered at scoring |
| 🚨 **Threshold provenance — NOT from the options market, and why** | `module_flow AVGO --positioning` returns **`예상변동 ±1.3% (만기 2026-08-26, D0)`** for a **2026-09-02** event — the straddle expires **seven days before the print** (`D353` reproducing, `M948`). **No implied move for this event is readable today.** Thresholds are the measured 252-day tails, labelled as such. ⚠ **Obligation: re-derive from the 09-04-or-later straddle at the 08-28 or 08-31 run, before the print.** Until then this row is **MEDIUM-RESOLUTION** and is labelled so |
| **Positioning at registration** | Short **1.2% float, covering**, DTC 3.0 · **P/C 2.75** (put-heavy) · skew **−5.3** · FINRA **z −2.17, 5v5 −10.4▼ = the board's largest short exit** · sweep: flow −0.487, 🟡중립, OBV 중립, `rs20 −9.4`, **`rs60 −24.1` = worst of the 11 holdings**. ⚠ **The option book and the daily short tape disagree in tone** and that is recorded, not averaged |
| **Information content (`B4`)** | **A** falsifies the `IT UW` on the desk's own held epicenter name and says the −24.1 `rs60` was a discount. **B** falsifies the `AI-compute-EPICENTER` label on a held name and turns `S116`'s Alphabet dual-sourcing story from a relative-share question into an absolute one. ⚠ **C at ~70% is genuinely likely and is NOT informative** — the row earns its slot only because A and B are both thesis-breaking |
| **Anti-signal (VOID)** | an **announced acquisition of or by `AVGO`**, or a **trading halt ≥1 full session**, inside 2026-09-01 → 2026-09-08. ⚠ **Base rate checked (`D300-KR`)**: none scheduled. **The print is deliberately NOT an anti-signal — it is the event** |
| **Non-redundancy (`D343`)** | 09-08 carries the Canada tariff effective date, `MSTR` revive and six ledger rechecks — **no other price bracket settles there.** `S116` (08-28) is a **relative** `MRVL − AVGO` spread settling **before** this print; `S127` is `AVGO` **absolute**, **after** it |
| **Owner** | `industry_US` |

## `S128` — ★★★ The out-of-sample test of this desk's own strongest measured cell · ARMED · → settle **2026-09-09**

| Field | Value |
|---|---|
| **Why it exists** | `rs60` h=5 is the US desk's strongest IC cell — **mean IC −0.1310, `t(NW) −5.46`, `n_eff 5.4`, positive in 7% of 27 run-dates, Bonferroni-passing NEGATIVE** — and it has **never been tested out of sample**. Sorting the 299 names on the 2026-08-26 sweep gives **35 reversal** (`rs20 > 0 ∧ rs60 < 0`) vs **117 decay** (`rs20 < 0 ∧ rs60 > 0`): **39.1% of the board is a decaying stock of past excess** (`M949`), and **4 of 11 holdings sit in decay** (`MET`, `NDAQ`, `RTX`, `XOM`) against **1 in reversal** (`NVDA`) |
| **Frozen observable** | `EW{35 reversal names}` **minus** `EW{117 decay names}`, **5-session returns**, settled closes, **both baskets frozen as printed by the 2026-08-26 sweep** (membership rule `rs20 > 0 ∧ rs60 < 0` vs `rs20 < 0 ∧ rs60 > 0`; full lists in `llm_outputs/2026-08-26/industry_US/SECTOR_FLOW_US.json`), at the **2026-09-09** close |
| **Branch A (the ledger's sign is real out of sample)** | spread **≥ +5.433pp** (trailing-252 **p85**) |
| **Branch B (the ledger's sign is a regime artifact)** | spread **≤ −3.158pp** (trailing-252 **p15**) |
| **Branch C** | between |
| **`D93` before freezing** | trailing 252 of the same spread to 2026-08-25: mean **+1.268** · sd **4.552** · p05 −6.833 · **p15 −3.158** · p50 +2.131 · **p85 +5.433** · p95 +7.154 ⇒ **A ≈15% · B ≈15% · C ≈70%.** ⚠ **The estimator's centre is +1.268, NOT zero** — reversal has beaten decay on average over the window, so branch A is not the "surprising" side and the row says so before the fact |
| **State at registration** | **−0.556 = the 31.7th percentile** — currently mildly favouring decay, i.e. **against** the ledger's sign |
| **⚠ `S6` / `D4`, written INTO the row** | the IC ledger's window contains the 2026-08-24 rotation, i.e. **a reversal regime**, so a reversal IC measured inside it may not generalise. **This row is the out-of-sample test and it can fail. That is the point** |
| **Information content (`L3`/`B4`)** | **A** says the measured axis holds prospectively and the book's 4 decay names are on the wrong side of it. **B** kills a Bonferroni-passing cell **before it becomes doctrine**, which is the more valuable outcome. Neither branch merely confirms |
| **Anti-signal (VOID)** | an index-level shock (`SPY` 2026-09-01 → 2026-09-09 beyond **±5%**), or a **GICS/index reconstitution removing ≥5 names from either basket** inside the window. ⚠ **MSCI's 08-31 quarterly review is checked and is explicitly NOT a voider** — it falls before the window opens and does not change GICS assignment |
| **Non-redundancy (`D343`)** | 09-09 carries `P102` (a two-name Materials spread) and `S58-KR`. **`S128` is the board's only cross-sectional factor row**, orthogonal to `P101`'s sector-internal software−hardware cut |
| **Owner** | `industry_US` |


---

# Rows added by the 2026-08-27 `industry_US` run (PREMORTEM registrations)

> ⚠ **Append-only** (`D165`); text staged in a scratchpad first (`D357`).
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`, excluding this
> run's own files: `S129` `S130` → **0 hits**. Highest existing **`S128`** (2026-08-26 `industry_US`).
> IDs allocated against **every** existing row in **BOTH** `SCENARIOS*.md` files (`D76` collision class,
> 5th consecutive day the class was checked and prevented).
> ⚠ **Every threshold below is frozen at registration.** The full registration tables (including each
> row's `D93` baseline, anti-signal base-rate check and non-redundancy statement) are reproduced here
> verbatim from `llm_outputs/2026-08-27/industry_US/BLINDSPOT_PREMORTEM.md §4b`.

## `S129` — ★★★ The Canadian retaliation's agricultural leg · ARMED · → settle **2026-09-09**

## `S130` — ★★ `NVDA` / Hugging Face $12.9bn · ARMED · → settle **2026-09-10**

#### `S129` — ★★★ The Canadian retaliation's **agricultural** leg, which three runs have left unbracketed

| Field | Value |
|---|---|
| **Event** | **Canadian retaliatory tariffs take effect 2026-09-08.** Corroborated to bodies: *"U.S. and Canada Are Bracing for Prolonged Trade Dispute"* [14 outlets, 08-26] · *"'We got attacked': Canadians unite in fury against Trump's latest tariff salvo"* [5 outlets] |
| **Frozen observable** | **`ADM` 5-session excess return vs `SPY`**, settled closes, `auto_adjust=False`, window **2026-09-02 close → 2026-09-09 close** (the 09-08 effective date falls inside) |
| **Branch A (the agricultural leg prices)** | `ADM` 5-session excess **≤ −4.00pp** — the retaliation list's named US casualty is repriced, and `STPL N−` is a *tariff* call, not a *defensive-rotation* call |
| **Branch B (it was already in the price)** | `ADM` 5-session excess **≥ +2.50pp** — the selling already happened (`ADM` is 🔴분산 with OBV −0.154 **before** the effective date), and the desk's STPL demotion rests on something else entirely |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | `ADM`'s own current readings, from this run's sweep (asof 08-27): `RS20` **−4.8**, `RS60` **−4.6**, OBV **−0.154 분산**, `flow_score` **−0.643**. Bands are set **asymmetrically and deliberately**: the state is already negative on all four axes, so **A asks the move to extend and B asks it to reverse** — a symmetric band from a negative state would make B nearly unreachable and the row would be one-sided in disguise. **A ≈25% · B ≈20% · C ≈55% — disclosed** |
| **Information content (`B4`)** | **Both branches change a conclusion, and they change DIFFERENT ones.** **A** makes `STPL N−` a tariff call and puts the 09-08 date on the desk's defensive underweight. **B** falsifies the tariff channel on the one name the retaliation list actually names, which would mean `S123`'s 09-12 settle is measuring an event that already cleared. **Neither merely confirms.** |
| **Anti-signal (VOID)** | a **negotiated carve-out for agricultural goods announced before 09-08**, confirmed in **≥2 outlet bodies**, **or** an `ADM`-specific dated corporate action (guidance update, M&A) inside the window. ⚠ **Base rate checked**: the 08-26 tape carries no carve-out story; the durability thread is climbing, not resolving. **The clause is keyed to a named event, not to commentary** — the tariff itself is deliberately **not** a voider, because it is the event |
| **Non-redundancy (`D343`)** | **09-09 currently carries `P102`, `S128` and `P105`** — a materials two-name spread, a cross-sector reversal basket, and a single-sector aggregate. **`S129` is the only single-name trade-policy row on that date**, and it deliberately avoids **08-28 (nine rows)**. `S123` (09-12) brackets the trade war's *implementation* at index level; **this row brackets one named casualty**, which `S123` cannot reach |
| **⚠ `W3`** | this measures whether the tariff channel prices, **not** whether any position was right. No sizing (P4) |
| **Owner** | `industry_US` |

#### `S130` — ★★ `NVDA` buys **Hugging Face** for $12.9bn: is it confirmed, and does the tape read it as strength?

| Field | Value |
|---|---|
| **Event** | *"Nvidia agrees to buy Hugging Face for $12.9 billion"*, **2026-08-27**, carried by `cnbc`, `techcrunch`, `fortune`, `yahoo_finance`. 🚨 **Every one says "report says" / "reports" — there is NO company announcement**, and the row says so at registration rather than discovering it at scoring. Precursor: `yahoo_finance` 08-23 *"Hugging Face exploring sale valuing it at $13 billion"* [2 outlets] |
| **Frozen observable** | **Two legs, both read at the 2026-09-10 close.** **Leg 1 (confirmation)**: whether an **`NVDA` company statement or an SEC filing** naming the acquisition exists by 09-10. **Leg 2 (tape)**: `NVDA` **10-session excess return vs `SPY`**, settled closes, window **2026-08-27 close → 2026-09-10 close** |
| **Branch A (confirmed AND the tape rewards it)** | Leg 1 **confirmed** **AND** leg 2 **≥ +2.00pp** — the market prices the adjacency as strategic |
| **Branch B (the informative one)** | Leg 2 **≤ −4.00pp**, *regardless of leg 1* — ★ **a $12.9bn acquisition announced the day after a 100bp gross-margin guide-down** (`P90` → `FIRED-A`, this run) **being sold is the peak-margin trap (`L2`) arriving on the epicenter of the #1 cycle**, which is the single most consequential thing that could happen to this book |
| **Branch C** | between, or leg 1 unconfirmed with leg 2 inside the bands |
| **`D93` executed BEFORE freezing** | `NVDA` current state (asof 08-27 sweep): `RS20` **+11.4**, `RS60` **−0.8**, OBV **−0.069 중립**, `delta` **−0.114**. Implied move **±3.0%** at the **08-28 (D1)** expiry with skew **+16.3** and P/C **0.59** ⇒ the tool reads positioning as **"complacent, little fuel."** ⚠ **The ±3.0% is a D1 figure and cannot price a 10-session window** (`D353`'s class) — **so the bands are NOT taken from the options market**, and that is stated, not hidden. They are set at roughly ±0.5σ of `NVDA`'s own 10-session excess dispersion. **A ≈30% · B ≈20% · C ≈50% — disclosed** |
| **Information content (`B4`)** | **Asymmetric, and the asymmetry is declared**: **A can only confirm** (a strategic acquisition being rewarded tells us little we do not already believe). **B falsifies** — it says the epicenter is buying adjacency because its core is getting more expensive, which is the thesis this run's own `P90` verdict opened. **The row is registered FOR branch B**, and A is included because a one-way tilt into a live corporate event is a protocol violation |
| **Anti-signal (VOID)** | the deal is **formally denied** by `NVDA` or Hugging Face in a **company statement** inside the window (a *report* being contradicted by another *report* does **not** void it), **or** `NVDA` announces a separate transaction ≥ $10bn inside the window. ⚠ Base rate low; keyed to a **company statement**, not to press disagreement |
| **Non-redundancy (`D343`)** | 09-10 carries **no other registered row**. `S115`/`S79` settle tonight on the **print**; `S103` settles 08-29 on the print's **5-session window**. **`S130` is the only row on the acquisition**, which is a different object from the earnings event |
| **Owner** | `industry_US` |


---

# Registered 2026-08-29 by the `industry_US` PREMORTEM — **`S131` – `S134`**

> ⚠ **Append-only write** (`D165`); text staged in
> `llm_outputs/2026-08-29/industry_US/_scenarios_us_block.md` first (`D357`), and both
> `SCENARIOS_US.md` and `SCENARIOS.md` backed up to `*.bak_0829us_premortem` before the write.
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**` (excluding this
> run's own files): `S131` `S132` `S134` → **0 hits**. `S133` returned **1 apparent hit which was
> inspected and is a false positive** — the substring sits inside the FRED series id `MTSDS133FMS` in
> a 2026-08-28 KR company report. **Inspected rather than assumed** (`D94`). IDs issued by
> `module_evidence next-id S` (highest existing **`S130`**), not hand-grepped (`D76`).
> ⚠ **Language: English** — the US desk's documented practice.
> ⚠ **All spot prices settled 2026-08-28**, read via `fast_info.last_price` because `yf.download`
> returns `Close = NaN` on 300 of 301 US names for that session (`M1040`/`M1059`, `D402`).
> ⚠ **Implied moves read DIRECTLY from the option chain**, at the strike nearest the settled 08-28
> close on the first expiry **spanning** each event — because `module_flow --positioning` returned
> **`예상변동 ±nan%` on every ticker probed** (`M1065`) and, when it works, picks a **non-spanning**
> expiry (`D315`, 6th run). **No threshold was invented** (`M47`).
> ⚠ **SETTLEMENT MODE = TERMINAL on both branches** for all four (`D242`).
> ⚠ **`D388-KR` honoured**: the one basket row (`S133`) **enumerates its membership** inline.

## `S131` — ★★★ MSCI 08-31: does the passive print concentrate or broaden? · ARMED · → settle **2026-08-31**

**The mandatory ≤48h bracket.** `catalyst_calendar` puts the MSCI quarterly review at **D-2**, and
**six rows already settle 2026-08-31** (`S92` `S94` `S104` `S112` `S124` `S103`) — **not one observes
the rebalance itself.** A one-way tilt into a known binary is a protocol violation, so this row exists.

| Field | Value |
|---|---|
| **Event** | MSCI quarterly review, **2026-08-31** (passive print concentrates at that close) |
| **Frozen observable** | **`RSP` − `SPY` 1-session excess return**, settled closes, **2026-08-28 → 2026-08-31** |
| **Implied move at registration** | `RSP` **±1.06%** (2026-09-04 expiry, ATM K=220.00, straddle 2.34, IV 0.374/0.216) · `SPY` **±0.45%** (08-31 expiry, K=769.00, straddle 3.47). **Both branches sit outside `RSP`'s own priced move** |
| **Branch A (broadening)** | `RSP` − `SPY` **≥ +1.30pp** — the passive print favours the median stock ⇒ `M1051`'s sector-breadth-vs-stock-breadth split narrows and `P106`'s narrowing claim weakens |
| **Branch B (concentration)** | `RSP` − `SPY` **≤ −1.30pp** — the rebalance pushes further into the mega-caps ⇒ **`M1051` gets a mechanical explanation instead of a behavioural one**, and every `eqflow`-carried delta this run made stands on a number the index is actively working against |
| **Branch C** | between — **disclosed favourite** |
| **State at registration** | `RSP` 220.69 · `SPY` 769.35 (both settled 08-28). `RSP` `exc1` on 08-28 = **−0.116pp**; `exc5` = **−0.916pp** |
| **Information grade (B4)** | **HIGH on both, and asymmetric in a way worth stating**: this run made **four** verdict deltas entirely on `eqflow`, and **B is the branch that says the market is paying for the other number** |
| **Anti-signal (VOID)** | a market-wide trading halt, **or** MSCI postponing/withdrawing the review, inside 08-28 → 08-31. ⚠ Base rate low; the review date is calendar-confirmed |
| **Non-redundancy (`D343`)** | 08-31 carries six rows; all six are single-name, cross-sectional-count, or macro-print rows. **`S131` is the only one whose observable is the cap-weight-vs-equal-weight axis the rebalance actually moves** |
| **Owner** | `industry_US` |

## `S132` — ★★★ `AVGO` 09-02: a threshold that can carry information, four runs after `D295` asked for one · **SETTLED FIRED-C** (scored 2026-09-04, folded into the master scoring log by the 2026-09-06 `industry_US` run — `D472` header hygiene) · → settle **2026-09-03**

| Field | Value |
|---|---|
| **Event** | `AVGO` FQ3 earnings, **2026-09-02 (D-4)**. **Held.** `rs60` **−24.4 = the worst on the book** |
| **Frozen observable** | **`AVGO` 1-session excess vs `SPY`** on the first settled close after the print (**2026-09-03**), each vs its own 2026-09-02 close |
| **Implied move at registration** | **±8.11%** — ATM straddle **K=370.00 = 29.91** on the **2026-09-04** expiry, the first that spans the print (IV 0.736/0.731). **Cross-checked** on the 09-02 expiry (K=380.00, straddle 29.94) → **±8.12%, agreeing to 0.01pp** |
| **Branch A (the discount was wrong)** | excess **≥ +9.00pp** — outside the implied move ⇒ the −24.4 `rs60` was a discount, not a franchise loss, and `S116`'s B-leaning read (that `MRVL` took the socket) is falsified |
| **Branch B (the discount was right)** | excess **≤ −9.00pp** ⇒ the franchise loss is real and **the AI-compute epicenter is narrower than the book's three names assume** |
| **Branch C** | between — **disclosed favourite, and disclosed as LARGE**: the band spans 18pp against an 8.11% priced move. Stated rather than tightened |
| **Relationship to `S127`** | 🚫 **`S127` is NOT re-frozen** (`D242`) and stays ARMED on its own bands (**A ≥ +5.928 / B ≤ −4.922**, settle 09-08). ★ **Those bands sit INSIDE ±8.11% ⇒ pre-declared NO-INFORMATION** — exactly what `D295` predicted when it flagged them as hand-set, unmet for four runs. **This row is `D295`'s prescription executed.** If the two rows disagree, **the disagreement is the finding** (`S14-ANNEX` precedent) |
| **Anti-signal (VOID)** | `AVGO` postpones the print, **or** an announced acquisition of/by `AVGO` inside 2026-08-31 → 2026-09-03 |
| **Information grade** | **HIGH on both** — each branch changes a standing thesis on a **held** name |
| **Owner** | `industry_US` |

## `S133` — ★★★ Health Care: is the sector its constituents or its ETF? · ARMED · → settle **2026-09-14**

**This row brackets a verdict change this run made today**, which is the point of it.
`SECTOR_ROTATION §2` promoted `HLTH` `N`→`OW` on **`eqflow` +0.102 (the board's highest)** *against*
**`XLV` `exc5` −2.456pp vs `SPY` (the board's worst)**.

| Field | Value |
|---|---|
| **Frozen observable** | **`EW{REGN, AMGN, TMO, BDX, MRK, VRTX}` 10-session excess return vs `XLV`**, settled closes, **2026-08-28 → 2026-09-14** |
| **Membership, enumerated** (`D388-KR`) | Exactly those six tickers — the six `us_top300` Health Care names with the highest `rs60` on the **2026-08-27 settled** sweep (`REGN` +32.4 · `AMGN` +31.6 · `TMO` +29.3 · `BDX` +28.7 · `MRK` +27.8 · `VRTX` +27.3), **all six `OBV 매집`, all six `rs20` positive**. Equal-weighted, no rebalancing inside the window |
| **Benchmark, named inline (`C1`)** | **`XLV`, not `SPY`** — the question is constituents-versus-cap-weighted, so the sector ETF *is* the correct counterparty. Using `SPY` here would measure the sector, not the split |
| **Implied move at registration** | `XLV` **±2.20%** (2026-09-11 expiry, ATM K=171.00, straddle 3.77, IV 0.368/0.219). Both thresholds outside it |
| **Branch A (the constituents are the sector — the promotion was right)** | EW6 − `XLV` **≥ +3.00pp** ⇒ `XLV` is reporting on `LLY` (its `top1` **flipper**), `eqflow` was the better instrument, and G5's "prefer `eqflow` on a 45-day-stale universe" rule earned its keep |
| **Branch B (the ETF is the sector — the promotion was wrong)** | EW6 − `XLV` **≤ −3.00pp** ⇒ **`SECTOR_ROTATION §2`'s promotion was wrong**, and a 60-day relative-strength screen selected six names that were about to mean-revert together |
| **Branch C** | between — disclosed favourite |
| **State at registration** | `eqflow` +0.102 vs `wflow` −0.027 (🚨1名 `LLY`), breadth 0.03, n=32. `XLV` settled 08-28 **171.16**; `exc1` −0.018pp, `exc5` **−2.456pp** vs `SPY` |
| **Information grade (B4)** | **HIGH on B, MEDIUM on A.** A largely confirms a direction this run already took; **B falsifies a verdict change made today**, which is rarer and more useful. **Stated at registration, not discovered at scoring** |
| **Anti-signal (VOID)** | an **FDA action or trial readout with a named date** at **≥2 of the six** inside 2026-08-28 → 2026-09-14. ⚠ **Base rate checked and NOT remote** — `LLY` took an FDA Mounjaro CV-risk approval on **08-28** (7 outlets) and the same day's head layer carried three other FDA items (`Revolution Medicines`, ivermectin EUA, `Pfizer`/`BioNTech` XFG vaccine). **Disclosed as live rather than assumed away** |
| **`L2` (peak-margin) not waived** | `MRK` **trades ABOVE its mean target** (upside −4.4%) on the carried §3a row. The basket is live **and** its one prior 🟢 is the expensive member — both stated |
| **Owner** | `industry_US` |

## `S134` — ★★ Financials: the contradiction with no instrument defect to blame · ARMED · → settle **2026-09-04**

| Field | Value |
|---|---|
| **Why it exists** | The **only** sector where both flow reads agree (`wflow` −0.144, `eqflow` −0.144), **neither is a `top1_flips_sign` bucket**, and the settled tape is **positive** (`XLF` `exc5` **+0.605pp vs `SPY`**, 2nd-best on the board). Every other contradiction this run found has an instrument defect available; **this one does not**, and `SECTOR_ROTATION §4` handed it here unresolved |
| **Frozen observable** | **`XLF` 5-session excess vs `SPY`**, settled closes, **2026-08-28 → 2026-09-04** |
| **Implied move at registration** | `XLF` **±1.36%** (2026-09-04 expiry, ATM K=58.00, straddle 0.79, IV 0.158/0.134). Both thresholds outside it |
| **Branch A (the tape was right, the flow axes were late)** | `XLF` exc5 **≥ +2.00pp** ⇒ ROTATION's `OW−`→`N` demotion was wrong, **and it would be the first evidence this desk has that `eqflow` can be wrong for a full week on a non-flipper bucket** |
| **Branch B (the flow was right)** | `XLF` exc5 **≤ −2.00pp** ⇒ the demotion was early and correct |
| **Branch C** | between — disclosed favourite |
| **State at registration** | `XLF` settled 08-28 **58.10**; `exc1` +0.607pp, `exc5` **+0.605pp** vs `SPY`; `wflow` −0.144 / `eqflow` −0.144 / breadth 0.02 / n=47, `top1` `BRK-B`, **not** a flipper |
| **Anti-signal (VOID)** | **Aug NFP prints 2026-09-04, the window's last day.** The window deliberately ends **ON** the print so the observable is the five sessions **before** it; **if the print is moved earlier, the row VOIDs** |
| **Hypothesis recorded, NOT adopted** | `EVENT_ALPHA` Card 8 — a take-private premium unwinding inside the sector (`PYPL` `rs60` **+36.5**, built on an Advent/Stripe offer **withdrawn 2026-08-28**, `OBV 중립`). **Named so a later run can test it; this row does not depend on it** |
| **Information grade (B4)** | **HIGH on A** (falsifies a demotion made today, and a rule the desk leans on), confirm-only on B |
| **Non-redundancy (`D343`)** | 09-04 carries `S126` (`XLI` exc5 vs `SPY` **into** NFP) and, from 09-04, `P114` (`XLI` exc5 **out of** NFP). **`S134` is a different sector on the same date**, and it is registered as sharing that date deliberately: if `S134`-B and `S126`-B both fire, that is **one macro observation**, not two sector verdicts |
| **Owner** | `industry_US` |


# Registered 2026-08-30 by the `industry_US` PREMORTEM — **`S135`** (one row)

> ⚠ Append-only (`D165`). **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` ·
> `REPORT/**` (excluding this run's own files): `S135` → **0 hits**. Highest existing **`S134`**
> (2026-08-29 US). IDs issued by `module_evidence next-id`, not hand-grepped.
>
> ★ **This stage drafted FOUR brackets and registered ONE.** Three were withdrawn after reading this
> file *before* writing: the MSCI 08-31 bracket is already owned by **`S131`**, the `AVGO` 09-02
> bracket by **`S132`** (+ `S127`), and the `HPE` 09-03 bracket was **deferred to the `IT` DEEP** by
> the 08-29 run's own written precedent, which applies again because `IT` is a DEEP this run too.
> Recorded so the *absence* of three rows is legible rather than looking like an omission.

## `S135` — ★★ Are `UTIL`, `RE` and `STPL` three UW verdicts or one? · ARMED · → settle **2026-09-11**

**Why it exists.** The PREMORTEM L1 tells Lens 2 to hunt the **correlated-UW pattern**. This desk
currently books **three separate UW verdicts** (`UTIL`, `RE`, `STPL`) and the last row that tested
that family settled **2026-08-13**; nothing has replaced it. ★ **There is a fresh prior AGAINST the
one-bet reading**, which is why the row is worth running rather than assumed: on **2026-08-28** the
three duration legs printed **1.11pp apart** (`XLK` −1.33 · `XLU` −0.87 · `XLRE` −0.22 vs `SPY`).

| Field | Value |
|---|---|
| **Frozen observable** | **max pairwise spread among `XLU`, `XLRE`, `XLP` 5-session excess returns vs `SPY`**, settled closes, **2026-09-04 → 2026-09-11**, `yfinance`, `auto_adjust=False` |
| **Benchmark, named inline (`C1`)** | **`SPY`**, on all three legs |
| **Branch A (they are ONE bet)** | max pairwise spread **≤ 1.50pp** ⇒ the desk's three UW verdicts are one position booked as three, and `G4`'s unresolved grouping question gets its first market answer |
| **Branch B (they decouple)** | max pairwise spread **≥ 4.00pp** ⇒ each UW needs its own cause, and `EVENT_ALPHA` Card 4's *capex* explanation for `XLU` becomes separable from the *rate* explanation |
| **Branch C** | between — disclosed favourite |
| **Band derivation (`C5`, stated, not round numbers)** | 5-session realised sigma measured on the repaired series: `XLU` **1.89%** · `XLRE` **1.59%** · `XLP` **2.04%**. **4.00pp ≈ 2σ of the widest leg; 1.50pp is below 1σ of any leg** ⇒ both bands sit outside the noise, in opposite directions |
| **Implied-move check, stated not smuggled** | `XLU` **±2.88%** (2026-09-11 expiry, K=42.50, **put OI 3,594 vs call OI 22**). ⚠ **No `XLRE` or `XLP` straddle was pulled and none is fabricated (`C3`)** — a 4.00pp *dispersion* among three ETFs cannot be produced by any single implied move, so the implied is context, not the band's source |
| **State at registration** | `XLU` `exc5` **−0.62pp** · `XLRE` **−1.85pp** · `XLP` **−1.14pp** vs `SPY` (settled 08-28; that close is a 5m-proxy validated to **0.0225% mean / 0.038% max** against the KIS broker feed, n=9) ⇒ **current max pairwise spread 1.23pp, i.e. ALREADY inside branch A's line.** Disclosed so A cannot later be read as a discovery |
| **Anti-signal (VOID)** | a **utility-specific regulatory or single-issuer event** (rate-case decision, major outage, or an announced merger) at **≥2** `XLU` constituents inside the window ⇒ `XLU` moves for a non-duration reason. ⚠ **Base rate checked and NOT remote** — `XLU` is the board's worst sector (`eqflow` −0.524, 10 reds of 15) and distressed sectors are where corporate actions cluster |
| **Information grade (`B4`)** | **HIGH on A.** A says three of the desk's eleven verdicts are one decision — a claim about its own book structure, the class `G4` has failed to settle for 11 consecutive runs. **B is modal-adjacent and only confirms that the current bookkeeping is not wrong**, which is worth less. **Stated at registration, not at scoring** |
| **Non-redundancy (`D343`)** | 09-04 carries `S126` and `S134`; 09-11 carries `P108`/`P116`. **`S135` observes a SPREAD among three UW sectors, not a level on any one of them**, and its window sits **between** those two dates rather than on either |
| **Owner** | `industry_US` |

---

# ═══ Registered 2026-08-31 by the `industry_US` PREMORTEM (frozen at registration) ═══

> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `REPORT/` · `llm_outputs/2026-08-2*/`:
> `S136` · `S137` → **0 hits**. Highest existing **`S135`** (2026-08-30 US). IDs issued by
> `module_evidence next-id`, not hand-grepped.
> ⚠ Both rows use **spread** observables so that neither the 2026-08-28 daily-close ghost bar nor the
> 2026-08-31 `BZ=F` front-month roll (`M1136`) can make them unscoreable.

## `S136` — ★★★ Is the Energy escalation a BARREL event or a CHAIN-POSITION event? · ARMED · → settle **2026-09-09**

| field | value |
|---|---|
| **Object** | `EW{SLB, MPC, PSX, VLO, COP}` **minus** `EW{XOM, EOG, FANG}` — **5-session sum of daily returns**, from the first settled close after **2026-09-01** through **2026-09-08** |
| **Why it exists** | This run's **principal flow claim** is that money left E&P and sat in services/refining **before** the 08-30/31 strikes (`SECTOR_ROTATION §2`: accumulating `SLB` +0.661 · `MPC` +0.650 · `PSX` +0.388 · `VLO` +0.349 · `COP` +0.324 vs distributing `XOM` −0.486 🔴 · `FANG` −0.622 🔴 · `EOG` −0.694 🔴, `repaired sweep asof 08-28`). **Nothing brackets it** — `P107`/`P112`/`P117`/`P118` all observe the barrel |
| **A** | **≥ +3.90pp** ⇒ the chain-position split is real and widening; the **sector label is the wrong unit** and Energy should be booked as two legs |
| **B** | **≤ −3.90pp** ⇒ the escalation lifts the barrel and E&P catches up; the split was a pre-event artifact and **this run's headline flow finding is wrong** |
| **C** | between ⇒ disclosed as the modal outcome |
| **Band derivation (`C5`)** | Measured 5-session-sum sigma of this exact spread over 60 sessions = **2.598pp**; realised range **−4.39 to +7.29**. **±3.90pp = ±1.50σ**, reachable in **both** directions inside the realised range (`D216`). **Symmetric, because the realised distribution straddles zero** — no asymmetry claimed |
| **Anti-signal (AMBIGUOUS)** | An **M&A event on any of the eight names** inside the window. ⚠ **Base rate NOT remote — `SLB` closed one TODAY** (Kelvion, $3.4bn). Second anti-signal: an **OPEC+ quota decision** |
| **Information grade (`B4`)** | **HIGH on B** — B kills this run's own headline reading. A confirms a direction already visible in the 08-28 tape and is worth less |
| **Non-redundancy (`D343`)** | `P107` (BZ=F ≥96.00 → 09-08) · `P112` (→ 09-11) · `P117` (BZ=F ≤85/≥95 → 09-18) · `P118` (`DCOILWTICO` spot → 09-11) **all observe the barrel**. This observes **relative position within the sector** and can disagree with all four; **if it does, the disagreement is the finding** |
| **Owner** | `industry_US` |

## `S137` — ★★ Is optical a SEPARATE leg from semis, or `SMH` beta? *(`D250`'s 16th run, finally bracketed)* · ARMED · → settle **2026-09-09**

| field | value |
|---|---|
| **Object** | `EW{LITE, COHR}` **minus `SMH`** (benchmark named inline, `C1`) — **5-session sum of daily returns**, from the first settled close after **2026-09-01** through **2026-09-08** |
| **Why it exists** | `D250` has asked for an optical row in `cycle_registry.json` for **16 runs** and never got one, so the desk's standing sentence is *"exposure is unmeasurable, not zero."* **A bracket does not need the registry** — it measures the question directly. Live context: *"AI Chips Update — Optical Transceivers Propel AI Data Center Growth"* [4 outlets, 2026-08-31]; `theme_age` optical **accel 1.35×**, the highest on the board after Warsh (3.27×); `LITE` **+0.550, OBV +0.287 매집, `rs20` +22.3 vs `SPY` — the strongest 20-day in the whole candidate set — against `rs60` −6.6** |
| **A** | **≥ +9.00pp** ⇒ optical is **its own leg**; `SMH`'s `exc60` −15.31pp vs `SPY` does not describe it, and the registry gap is a **real exposure gap** |
| **B** | **≤ −9.00pp** ⇒ optical is **high-beta semis**; the registry is right to fold it in and **`D250` should be CLOSED as not-a-gap** |
| **C** | between ⇒ contested |
| **Band derivation (`C5`)** | Measured 5-session-sum sigma of this spread over 60 sessions = **8.639pp**; realised range **−16.69 to +24.69**. **±9.00pp ≈ ±1.04σ**, reachable both ways. ⚠ **The band is wide because the spread is wide** — a tighter band would fire on noise (the `S61` failure) |
| **Anti-signal (AMBIGUOUS)** | An **earnings print by `LITE` or `COHR`** inside the window (a single-name event, not a leg verdict). ⚠ **Second, and it is CERTAIN not remote: `AVGO` prints 09-02 or 09-03 and sits inside `SMH`**, moving the denominator for a reason unrelated to optical. **Disclosed at registration; the row is registered anyway, because a leg that cannot survive its own index's largest print is not a leg** |
| **Information grade (`B4`)** | **HIGH on B** — B lets the desk **close** a 16-run open dig, which is worth more than confirming it |
| **Non-redundancy (`D343`)** | No existing row observes optical. `S130` observes `NVDA`/Hugging Face; `S132`/`S127` observe `AVGO`. **None reaches the interconnect layer** |
| **Owner** | `industry_US` |


---

# Registered 2026-09-01 by the `industry_US` run — **`P121`–`P124` (MACRO)** · **`S138`–`S140` (PREMORTEM)**

> ⚠ **Append-only** (`D165`). Nothing above this line is rewritten.
> ⚠ **IDs issued by `module_evidence next-id`, not hand-grepped** (`D76` collision class): highest
> existing **`P120`** / **`S137`** at write time, live scan across `handoff/*.md` · `llm_outputs/**` ·
> `REPORT/**`. Allocated against **every** existing row in **both** `SCENARIOS*.md` files.
> ⚠ **Every threshold below is frozen at registration.** A bracket whose threshold moves after the
> print is a description wearing a forecast's clothes.
> 🚨 **Instrument state at registration**: the 08-28 daily bar is a **permanent partial hole**
> (259 of 301 names still NaN at T+4); the primary sweep's OBV axis is **revoked**; every flow number
> quoted below comes from `SECTOR_FLOW_US_REPAIRED.json` (3-axis `nonews`, 299 scored, **asof 08-31**).

## `P121` — ★★★ The repricing is the POLICY PATH, not inflation, and not term premium · ARMED · → settle **2026-09-04+**

- **Claim.** `[FRED]` 08-28: `DGS2` **+14 bp** (4.20 → 4.34) · `DFII10` **+8 bp** · `T10YIE` **−2 bp** ·
  2s10s **47 → 39 bp**. `[news]` Warsh's Jackson Hole debut read hawkish across 10 outlets; Barclays
  sees **two 2026 hikes**; the "odds of a September rate hike have nearly doubled" thread is
  **BUILDING 2→5**; `theme-age Warsh` **3.22× ACCELERATING** on a 5,102 base.
- **A (the path repricing extends).** `DGS2` **≥ 4.50** at the first `[FRED]` close covering
  **2026-09-04** **AND** `T10YIE` **≤ 2.36**.
- **B (a two-session Jackson-Hole artifact).** `DGS2` **≤ 4.18** at the same close.
- **C** between — the disclosed favourite.
- **`D93` before freezing.** `DGS2` 5-observation change, trailing 252: sd ≈ **6.5 bp**; 30-day
  realised range **4.17 – 4.34**. A needs +16 bp and B needs −16 bp over ~4 observations ⇒ both
  ≈ **±2.5σ** ⇒ **A ≈10% · B ≈10% · C ≈80%, disclosed up front.**
- **Anti-signal (VOID).** An **intermeeting Fed action**, or a **BLS delay / restatement of the
  August payroll release**. ⚠ Base rate low — both are publication-failure clauses.
- **KPI.** `T10YIE` **2.31** — under A it should stay ≤ 2.36. **If A fires WITH `T10YIE` above 2.42
  the claim is right about direction and wrong about mechanism**, which is exactly the split `P86`
  produced today (`M1166`).
- **Owner** `industry_US`.

## `P122` — ★★★ The oil bid is a supply event that positioning has not chased · ARMED · → settle **2026-09-08**

- **Claim.** `CL=F` **83.40 → 85.76** (08-31 settled); `BZ=F` **89.31 → 90.49**. `[COT 08-25]` WTI spec
  net **+31,099 = 43rd percentile of its year**, +1,935 WoW. Cause dated and multi-sourced: **US
  strikes on Larak Island, inside the Strait of Hormuz**, and **Iranian retaliation on US bases in
  Jordan and on the UAE** (22-outlet head cluster; 12-outlet live thread). `theme-age Larak`
  **58.21×**, the fastest term on the board.
- **A (supply premium extends AND positioning follows).** At `[COT]` for **2026-09-08**, WTI spec
  1-year percentile **≥ 65** **AND** `CL=F` settled close **≥ 88.00** on that date.
- **B (a headline spike into an oversupplied market).** `CL=F` settled close **≤ 80.00** on or before
  2026-09-08.
- **C** between — the disclosed favourite.
- **`D93` before freezing.** `CL=F` 30-day realised range **81.25 – 87.83**; 5-session sd ≈ **2.6**.
  Both thresholds sit **outside** the 30-day range ⇒ **A ≈15% · B ≈10% · C ≈75%.**
- **Anti-signal (VOID).** A **front-month contract roll inside the window.** ★ **Base rate RAISED, not
  decorative** — `R116` was retracted one run ago on exactly this. ✅ Resolved on settled closes:
  `BZ=F` 89.31 → **90.49 = +1.32%** (Brent **rose**) and the Brent−WTI spread **5.91 → 4.73**, inside
  its 60-day 2.40–8.50 range ⇒ the artifact was intraday only.
- **KPI.** `theme-age Larak` **58.21×** — a fall below ~5× with `CL=F` still bid would say the market
  stopped attributing the bid to the Strait.
- **⚠ Counter-evidence stated at registration.** The **Venezuela** oil-deal cluster is **15 outlets**
  and **ACCELERATING 2.74×**; its own bodies read "Trump's 'Historic Deal' Isn't Fooling Oil Traders"
  and "65 Billion-Barrel Oil Deal Won't Fix Supply Anytime Soon".
- **Replaces** the bracket `S92` consumed when it scored `FIRED-A` this run. **Owner** `industry_US`.

## `P123` — ★★ The AI trade's marginal dollar moved from COMPUTE to POWER · ARMED · → settle **2026-09-08**

- **Claim.** Same-day, ≥5 outlets each: "AI Power Demand Is Exploding, But How Much Actually Gets
  Built" (13 outlets) · "SLB Makes $3.4 Billion Bet on AI Data Center Boom" · Anthropic's **$35bn**
  Lambda contract (BUILDING) with **"Sundar Pichai Says Alphabet Can't Build AI Capacity Fast Enough,
  and Anthropic Has Secured 5 Gigawatts of It"** — while `theme-age data center` is **⚪ECHO 1.01×** on
  an 18,656 base. `SLB` is the repaired sweep's **#3** name (+0.822 🟢, OBV +0.498, `rs20` +20.6 vs
  `SPY`) and sits in **Energy**, not IT.
- **A (the power leg is where the delivery is).** `EW{SLB, ETN, NEE, VRT}` **minus `SMH`**, 5-session
  sum of daily returns, first settled close after 2026-09-01 → **2026-09-08**: **≥ +5.00pp**.
- **B (one week of oil beta).** **≤ −5.00pp**.
- **C** between — disclosed as the modal outcome.
- **Band derivation (`C5`).** Measured 5-session-sum sd of this spread over 60 sessions ≈ **3.3pp**;
  **±5.00pp ≈ ±1.5σ**, the same construction `S136` uses — chosen for consistency, not tuned.
- **Anti-signal (VOID).** `AVGO`'s 09-02/09-03 print moving `SMH` by **>±5%** in a single session.
  ⚠ **Base rate HIGH and disclosed now, not at settle** — `AVGO`'s measured implied move is **±9.6%**.
- **KPI.** `NEE` `[FINRA]` short-volume **z +1.76 🔴** — under A that pressure should ease.
- **⚠ Post-registration evidence, disclosed and NOT used to re-band (`D242`).** EVENT_ALPHA Card 5
  measured, later in the same run, that **every AI-power name is 🟡 or 🔴 and none is 🟢**
  (`ETN` −0.339 Δ −0.687 · `VRT` −0.215 Δ −0.687 · `NEE` −0.254 · `CEG` −0.396 · `VST` −0.767🔴 ·
  `PWR` −0.597🔴 · `FIX` −0.783🔴 · `DUK` −0.672🔴 · `SO` −0.597🔴), and that **Texas has halted new
  data-center power interconnects over "ghost demand"** [reuters via yahoo_finance + cna, 09-01].
  ⇒ **the basket is one strong leg and three weak ones and the evidence points to B or C.**
  **Recorded as a disclosed pre-settle state, explicitly NOT a score** — this desk's pre-settle reads
  are **0 for 4**.
- **⚠ `D416` open**: `cycle_registry.json` has no ranked AI-power row, so "the book holds 0% of this
  layer" is **unstatable**. This row measures the question the registry cannot. **Owner** `industry_US`.

## `P124` — ★★ Credit and the dollar both say this is a policy event, not a risk event · ARMED · → settle **2026-09-18**

- **Claim.** `[FRED 08-28]` `hy_oas` **2.60**, tighter on **seven consecutive observations** (2.73 →
  2.60); `ig_oas` **0.79** unmoved; `NFCI` **−0.566**, looser. `[yfinance 08-31]` `GC=F` 4,609.7 →
  **4,431.1** over three sessions **while `DTWEXBGS` rose** (118.36 → 118.75) and `VIXCLS` sat at
  **14.43**. A war escalation, a hawkish central-bank debut and a new one-year high in the 10y
  produced **no credit widening, no vol bid, and a falling gold price**.
- **A (the market is under-pricing it).** `hy_oas` **≥ 2.85** (`P67`'s standing line) at the first
  `[FRED]` close covering **2026-09-18**.
- **B (orderly repricing).** `hy_oas` **≤ 2.50** at the same close **AND** `VIXCLS` **≤ 15.5**.
- **C** between — disclosed favourite.
- **`D93`.** `hy_oas` 14-observation change sd ≈ **8 bp**; current 2.60 sits near the low end of its
  year ⇒ A needs +25 bp (≈3σ), B needs −10 bp (≈1.2σ) ⇒ **A ≈5% · B ≈25% · C ≈70%.**
  ⚠ **The bands are asymmetric because the distribution is** — stated, not hidden.
- **Anti-signal (VOID).** A **single-issuer default or a bank resolution** inside the window.
- **KPI.** `GC=F` — under A gold should stop falling.
- **Non-redundancy (`D343`).** `P67` is a **level** claim about AI-capex debt; `S111` scored `C` on
  `ig_oas`. This row is a **joint** claim about credit ∧ vol ∧ gold through a geopolitical event.
  If it and `P67` fire the same way that is two observations of one regime, named in advance.
- **Owner** `industry_US`.

## `S138` — ★★★ `AVGO`: a threshold that is actually OUTSIDE the priced move · **SETTLED FIRED-C** (scored 2026-09-04, folded into the master scoring log by the 2026-09-06 `industry_US` run — `D472` header hygiene) · → settle **first settled close after the print (2026-09-03 or 09-04)**

| field | value |
|---|---|
| **Event** | `AVGO` FQ3 earnings, **2026-09-02** per `catalyst_calendar` ⚠ **`D420` unresolved** — the issuer calendar says **09-03**. **The row settles on the observable, not the date.** |
| **Frozen observable** | **`AVGO` 1-session excess vs `SPY`**, settled closes, the first settled session after the print, each vs its own prior close |
| **Implied move at registration** | **±9.6%** — `module_flow AVGO --positioning`, expiry **2026-09-02 (D1)**. ⚠ Read with its `D±n`: the straddle covers the path to expiry, not the event alone |
| **A (the discount was wrong)** | excess **≥ +11.00pp** — outside the priced move ⇒ `rs60` **−12.9 vs `SPY`** was a discount, not a franchise loss, and the deepest-discounted half of IT (`MRVL` `rs60` −34.4 with `rs20` **+8.0** already turning · `AMAT` · `NXPI` · `ARM` · `ON`) re-rates with it — **none of which the book owns** |
| **B (the discount was right)** | excess **≤ −11.00pp** ⇒ the franchise loss is real and the **AI-compute epicenter is narrower than the book's three names assume** |
| **C** | between — **disclosed favourite, and disclosed as LARGE**: the band spans 22pp against a 9.6% priced move. Stated rather than tightened |
| **Information grade (`B4`)** | **HIGH on both.** A falsifies ROTATION's `IT N` hold and `S116`'s B-leaning read that `MRVL` took the socket; B falsifies the epicenter's breadth. ⚠ C is likely and that is the honest cost of a threshold outside the priced move |
| **Relationship to `S132` / `S127`** (`D343`) | 🚫 **`S132` is NOT re-banded and NOT voided.** It settles on its own ±9.00pp and is **pre-declared NO-INFORMATION** because that now sits **inside** the ±9.6% straddle (`M1197`). `S127` (09-08) observes a different window. This row exists **solely** because it is the only one of the three with a threshold outside the priced move — the `S103` → `S115` precedent |
| **Anti-signal (VOID)** | a **guidance withdrawal, M&A announcement, or export-control action** at `AVGO` inside the window — none of which would be the print. ⚠ Base rate low but **not remote** given the export-control tape |
| **Positioning disclosed at registration** | options **P/C 1.73**, IV skew **−3.3**, short **1.2% of float, covering, DTC 3.0**, news velocity **1.33× accelerating** ⚠ **live partial bar (NYSE open at read time)**; settled flow 08-31 **−0.616 🔴분산**, OBV −0.133 |
| **Owner** | `industry_US` |

## `S139` — ★★ Re-arming the correlated-underweight bracket across the NFP · ARMED · → settle **2026-09-04**

| field | value |
|---|---|
| **Why it exists** | `S112` **FIRED-B today** on exactly this basket (**−2.331pp vs `SPY`** against a −1.757 threshold) ⇒ the correlated-UW pattern is **measured, not hypothetical** — and scoring **disarmed** it, leaving three of the desk's underweights unbracketed across a dated macro binary |
| **Frozen observable** | **`EW{XLU, XLRE, XLP}` 3-session excess vs `SPY`**, settled closes, **2026-09-01 close → 2026-09-04 close** (August NFP prints that morning) |
| **A (AGAINST US)** | **≥ +1.653pp** (trailing-252 **p85**) — the three rip **together** on a cold payroll and give back the `S112` gain in one window |
| **B (with us)** | **≤ −1.757pp** (trailing-252 **p15**) — a hot payroll extends the duration repricing and the basket pays twice |
| **C** | between — disclosed favourite |
| **`D93` before freezing** | **Identical distribution to `S112`, reused deliberately rather than re-derived**: trailing 252 mean −0.156 · sd 1.754 · p05 −2.893 · **p15 −1.757** · p50 −0.168 · **p85 +1.653** · p95 +2.719 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | the basket **just delivered −2.331pp**, i.e. it starts **below p05** ⇒ ⚠ **B is the low-information branch here** (mean reversion alone could produce a C) **and A is the informative one** — the reverse of `S112`'s balanced start, disclosed |
| **Implied move** | ⚠ **No straddle prices an equal-weight three-ETF basket** ⇒ stated as unavailable rather than invented (`D2`) |
| **Anti-signal (VOID)** | a **BLS delay or methodology restatement** of the August payroll release |
| **Non-redundancy (`D343`)** | `S135` (09-11) asks whether these three are **one verdict or three**; this row asks how the **one bet** behaves across a dated binary. Different objects; the correlation is named in advance |
| **Owner** | `industry_US` |

## `S140` — ★★★ Does IT's repaired breadth HOLD, or was 41-of-56 one week? · ARMED · → settle **2026-09-08**

| field | value |
|---|---|
| **Why it exists** | `S124` **FIRED-A at 41 of 56** today — above the trailing-252 **p85 (39)** — from a registration state of **13 of 56 (5.6th percentile)**. ROTATION declined to promote `IT` because the pro-case is a **return** measurement while `eqflow` reads **−0.014**. ★ **The desk therefore holds a verdict its own settled bracket just argued against, and nothing re-tests it** |
| **Frozen observable** | **COUNT of `us_top300` Information Technology names (n=56) with a positive 5-session excess vs `SPY`**, settled closes, at the **2026-09-08** close — the identical construction `S124` used |
| **A (the repair is structural)** | **≥ 39** (trailing-252 p85) ⇒ `IT N` is wrong, and ROTATION's `eqflow`-based decline was measuring participation while the money measured price |
| **B (it was one week)** | **≤ 20** (trailing-252 p15) ⇒ the 41 was a post-print bounce and the sweep's `eqflow` −0.014 / 3🟢-vs-9🔴 was the better instrument |
| **C** | 21–38 — disclosed favourite |
| **`D93` before freezing** | trailing 252 of the same count: mean **29.5** · sd **9.0** · p05 13 · **p15 20** · p50 30 · **p85 39** · p95 43 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **41 of 56 = above p85.** ⚠ Starting at an extreme means **mean reversion alone produces C**, disclosed |
| **Implied move** | ★ the observable is a **cross-sectional COUNT, which no straddle prices** ⇒ the threshold is outside the implied move **by construction**, stated rather than claimed as a virtue |
| **Information content (`B4`)** | **Both branches change a conclusion**: A kills `IT N`; B settles the `M1184` price-vs-participation contradiction in favour of the flow instrument. Deliberately **not** a fifth reading of the `AVGO` print — `S138`/`S132`/`S127` own that; this row owns the **sector-breadth consequence** |
| **Anti-signal (VOID)** | a **GICS reclassification moving ≥3 names into/out of Information Technology**, or a market-wide trading halt, inside 09-02 → 09-08 |
| **Owner** | `industry_US` |


# ═══ Registered 2026-09-02 by the `industry_US` PREMORTEM — **`S141`** · **`S142`** ═══

> IDs from `module_evidence next-id` (live scan of `handoff/*.md` · `llm_outputs/**` · `REPORT/**`),
> highest existing `S140` at write time. Both indexed in the `SCENARIOS.md` MASTER INDEX.
> ⚠ Registered under the run's declared constraint: the four PREMORTEM lenses ran **serially and
> in-context**, not as a parallel adversarial agent fan-out (8th consecutive run).

## `S141` — ★★★ Does the `AVGO` print move the SECTOR? · **SETTLED FIRED-C** (scored 2026-09-04, folded into the master scoring log by the 2026-09-06 `industry_US` run — `D472` header hygiene) · → settle **2026-09-03**

**Why it exists.** `S138` (±11.00pp), `S127` (09-08) and `S132` (±9.00pp, pre-declared
NO-INFORMATION) all bracket the **name**. **Nothing on the board measures whether the print moves
`SMH`**, and the against-us branch of this run's tilt is a sector event: if `AVGO` beats and raises,
`S124`'s 41-of-56 breadth repair extends, this run's declined `IT N → UW` was wrong, and
EVENT_ALPHA Card 6's "late money" tag on `NVDA`/`ANET` breaks — three readings at once.

| | |
|---|---|
| **Frozen observable** | `SMH` **1-session excess return vs `SPY`**, settled closes, `auto_adjust=False`, **2026-09-02 close → 2026-09-03 close** |
| **Branch A (the print re-rates semis)** | **>= +1.802pp** (trailing-252 **p85**) |
| **Branch B (the print de-rates semis)** | **<= -1.732pp** (trailing-252 **p15**) |
| **Branch C** | between |
| **`D93` before freezing** | trailing 252 of `SMH` exc1 vs `SPY`: mean **+0.212** · sd **1.911** · p05 -3.249 · **p15 -1.732** · p50 +0.367 · **p85 +1.802** · p95 +3.418 ⇒ **A ~15% · B ~15% · C ~70%** |
| **State at registration** | **-1.363 = the 17.9th percentile** (2026-09-01 settled) — **just outside branch B**; B is nearer, A is farther. Disclosed at registration, not discovered at scoring |
| ★ **Implied-move check — UNCHECKED, and the reason is recorded** | `module_flow AVGO --positioning` reads **예상변동 ±9.5% (expiry 2026-09-02, D0)**, which confirms `S138`'s ±11.00pp is **outside** and `S132`'s ±9.00pp is **inside** the priced move. **`SMH`'s only straddle reads ±0.9% at a D0 expiry that lapses BEFORE this row's window opens**, so it bounds today's residual move, not the print reaction. ⇒ **this row is labelled `implied-move UNCHECKED`, not "outside the implied move"** (`C3` — the column is unknown, not zero). First row this desk has had to label this way |
| **Anti-signal (VOID)** | a market-wide trading halt, **or** a dated US export-control announcement on advanced semiconductors, inside 09-02 -> 09-03. ⚠ **Base rate pre-stated so no void is improvised at scoring**: the 09-01/09-02 window already contained a *near-miss* of this class — an export action on **tungsten / battery black mass** (a different product class) and a **draft** rule reported as "could be shared with industry as soon as September". **Neither would void this row.** |
| **Information content (L3)** | A and B both change a conclusion; C does not and is the disclosed favourite. **A is the informative branch** because the registration state already sits near B |
| **Non-redundancy (`D343`)** | `S138`/`S127`/`S132` are all **name**-level rows on `AVGO`. This is the only **sector**-level row on the same event, and it can disagree with all three |
| **Owner** | `industry_US` |

## `S142` — ★★ The against-us branch of the `FIN UW` issued today, priced on the CPI print · ARMED · → settle **2026-09-11**

**Why it exists.** ROTATION demoted **`FIN N -> UW`** today on `eqflow` -0.220, Δ -0.220 and 0 greens
of 47. The strongest fact on the board points the other way: **`hy_oas` 2.63 = the 0.4th percentile of
its trailing 252**, `ig_oas` flat, `NFCI` easing. **Demoting a sector into a one-year credit tight is
the shape of an error**, and the run's own spine (`P125`: is the repricing the policy path or
inflation?) settles at the NFP and leaves the **CPI print unbracketed on the equity side**.

| | |
|---|---|
| **Frozen observable** | `XLF` **3-session excess return vs `SPY`**, settled closes, `auto_adjust=False`, at the **2026-09-11** close (August CPI) |
| **Branch A (banks rip — today's demotion was wrong)** | **>= +1.315pp** (trailing-252 **p85**) |
| **Branch B (banks lag — the demotion holds)** | **<= -1.516pp** (trailing-252 **p15**) |
| **Branch C** | between |
| **`D93` before freezing** | trailing 252 of `XLF` exc3 vs `SPY`: mean **-0.118** · sd **1.397** · p05 -2.329 · **p15 -1.516** · p50 -0.175 · **p85 +1.315** · p95 +2.071 ⇒ **A ~15% · B ~15% · C ~70%** |
| **State at registration** | **+0.034 = the 56.7th percentile** — ★ **dead centre, the most balanced starting state this desk has registered in weeks**, which makes this the more informative of the two rows written today |
| **Implied-move check** | `XLF` reads **예상변동 ±0.4% (expiry 2026-09-02, D0)** — a straddle that lapses before the window opens ⇒ **labelled `implied-move UNCHECKED`**. ⚠ The qualitative reading it does carry: P/C **0.04** = *"안일 (연료 적음)"*, i.e. almost no put protection in the bucket the desk just demoted |
| **Anti-signal (VOID)** | an unscheduled Federal Reserve action, a US bank failure or emergency facility, or a change to the CPI release date, inside 09-08 -> 09-11 |
| **Track KPI** | if **A** fires, `hy_oas` should be flat-to-tighter (a growth/curve read); if **A** fires while `hy_oas` **widens**, the move is a rate move and not a credit-quality move — **stated now so the two are not conflated at scoring** |
| **Information content (L3)** | **A falsifies a verdict this run just made; B defends it against the single strongest counter-argument on the board.** Both change a conclusion. ⚠ An `XLE`-vs-`SPY` bracket was considered and **DROPPED** because with `XLE` board-best on exc1/exc5/exc20 and `eqflow` +0.551, **neither of its branches would have changed `ENRG OW`** (B4) |
| **Non-redundancy (`D343`)** | `S134` settles **09-04** on the NFP; `P128` settles **09-08** on `hy_oas` itself. **Neither reaches the CPI print, and neither measures the equity bucket** |
| **Owner** | `industry_US` |


---

# ═══ APPEND — `industry_US` PREMORTEM registrations, 2026-09-05 (Sat) ═══

> IDs allocated by `module_evidence next-id S` against a LIVE scan of BOTH scenario files plus
> `REPORT/**` and `llm_outputs/**` (the `D76` collision class) — highest existing was `S144`.
> All thresholds from `D93` measured trailing-252 dispersion, executed BEFORE freezing.
> 🚫 **`implied-move UNCHECKED` does NOT apply**: the check was RUN and its result is that **no
> straddle covers either binary** — `SPY` ±0.5% and `SMH` ±1.8% expire 2026-09-08, `XLE` ±1.6%
> expires 09-09, against PPI 09-10 and CPI 09-11 (`M1305`). Thresholds therefore come from `D93`,
> and each row says so.
> Windows are counted in **settled sessions** because **2026-09-07 is Labor Day** and
> `catalyst_calendar` does not carry it (`D507`).

# §Registrations — three brackets + one annex

> All thresholds from **`D93` measured trailing-252 dispersion**, executed BEFORE freezing.
> 🚫 **None is stated against an implied move, because no straddle covers the binaries** (`M1305`).
> All windows in **settled sessions** (Labor Day 09-07, `D507`).

### `S145` — ★★★ Does the LOW-`vol_surge` sub-node lead its own sector? (the desk's first US-market read on the axis `C29` is about)

**Why it exists.** The board's three largest Δflows — `STX` **+0.728**, `WDC` **+0.718**,
`AMD` **+0.566** — all print **`vol_surge` 0.59–0.68** and are therefore **structurally excluded from
the 🟢 tag**, while the node's one 🟢 (`DELL`) passed on **surge 2.48** with a Δ of exactly **0.000**.
The KR `ic_ledger` scores `vol_surge` h=1 at **IC −0.0414 · t(NW) −3.61 · n_eff 45**, clearing
Bonferroni for a third run with a **NEGATIVE** sign, while `sector_flow`'s gate weights it
**positively**. `W1` bars importing that verdict; **it does not bar running the measurement here**,
and `D395`/`D428` have asked for a US-market read for weeks.

| | |
|---|---|
| **Frozen observable** | `EW{STX, WDC, AMD}` **minus `SMH`**, **4 settled-session** returns, `auto_adjust=False`, 2026-09-04 close → **2026-09-11** close |
| **Branch A** (the low-surge/high-Δ sub-node leads ⇒ the surge gate cost information) | **≥ +6.825** (p85) |
| **Branch B** (it lags its own sector ⇒ the gate filtered correctly) | **≤ −3.406** (p15) |
| **Branch C** | between |
| **`D93` BEFORE freezing** | trailing 252: mean **+1.567** · sd 5.051 · p05 −5.887 · **p15 −3.406** · p50 +1.647 · **p85 +6.825** · p95 +10.300 ⇒ A ≈15% · B ≈15% · C ≈70%. ★ **centre POSITIVE (+1.567)** — these three beating `SMH` is the *normal* state, so B is the harder branch and the row is written knowing it |
| **State at registration** | **+0.712 = the 44.8th percentile** — dead middle, slightly **below** its own mean. **No edge in either direction at the start** |
| **Anti-signal (VOID)** | an **earnings print at `STX`, `WDC` or `AMD`** inside 09-05 → 09-11 (checked via `Ticker.earnings_dates`, **not** the forward-calendar field — `D488`), or a semiconductor-specific US export-control **action** (a published rule, not a draft) |
| **Information content (`B4`)** | **A** says a whole node was invisible to this desk's own green gate for the wrong reason and the tag should not gate candidates. **B** says the gate earned its keep on US data and `C29` is a KR-only finding that does not transfer. **Neither merely confirms**, and either way the US desk finally has one own-market observation on the axis |
| **Non-redundancy (`D343`)** | `P137` asks whether **`SMH` itself** extends vs `SPY`; **`S145` asks whether the sub-node beats `SMH`** — the two can fire in opposite directions and the pair is more informative than either. `S140` (09-08) is a **breadth** row |
| **Owner** | `industry_US` |

### `S146` — ★★★ Is the AI-power lane one object, or is the book holding its worst name?

**Why it exists.** Lens 4 finding `M1308` + EVENT_ALPHA Card 6's **book flag**. `ETN` is **held**,
**🔴분산 −0.662**, rs20 **−8.0**, while `VST` (Δ +0.491), `CEG` (+0.644, OBV 매집) and `VRT`
(Δ +0.444, OBV 매집) all accumulate — **and the four sit in two different GICS sectors**, so no
sector verdict can express the split (`D416`).

| | |
|---|---|
| **Frozen observable** | `EW{VST, CEG, VRT}` **minus `ETN`**, **5 settled-session** returns, `auto_adjust=False`, 2026-09-04 close → **2026-09-14** close (09-07 is Labor Day) |
| **Branch A** (the split widens — generation/thermal is the lane and components are not) | **≥ +7.651** (**p95, not p85**) |
| **Branch B** (`ETN` catches up ⇒ the split was noise and the book's placement is fine) | **≤ −5.037** (p15) |
| **Branch C** | between |
| **`D93` BEFORE freezing** | trailing 252: mean **+0.103** · sd 4.967 · p05 −7.534 · **p15 −5.037** · p50 +0.394 · p85 +4.956 · **p95 +7.651** ⇒ A ≈5% · B ≈15% · C ≈80% |
| **⚠ Asymmetric branch design, declared** | **A is set at p95, not p85, because the state is ALREADY at the 92.9th percentile.** Using p85 (+4.956) would make A near-certain and therefore uninformative (`B4`) — the same construction `P102` used from a 98.8th-percentile state |
| **State at registration** | **+6.681 = the 92.9th percentile.** ⚠ **DISCLOSED: mean reversion is the base case from here, so B is the harder-to-reach but higher-information branch, and C is the favourite** |
| **Anti-signal (VOID)** | an **announced acquisition or merger involving any of the four**, or a **PJM/ERCOT capacity-auction result or emergency order** inside 09-05 → 09-14. ⚠ **Base rate checked**: no scheduled capacity auction falls in the window; the desk's own carried `M367` notes PJM cleared at the price cap in a prior auction, which is a *past* event and not a voider |
| **Information content (`L3`)** | **A** says the desk's one AI-power holding is the wrong expression of a live cycle and the registry's missing row (`D416`) has a measurable cost. **B** says the 09-04 flow split was a one-session artifact and the lane is one object. **Neither merely confirms** |
| **Non-redundancy (`D343`)** | `P123` (09-08) asks whether the AI marginal dollar moved **to power at all** — a cross-cycle question. **`S146` asks WHICH NAMES inside the lane**, which `P123` cannot answer. `S127`–`S130` are name-level AI-compute rows |
| **⚠ `W3`** | this measures a spread, not whether any position was right, and it sizes nothing (P4) |
| **Owner** | `industry_US` |

### `S147` — ★★ The refiner sub-node: EXTENDED-BUT-LIVE, or is `L2`'s peak-margin trap loaded?

**Why it exists.** Lens 3 tagged `MPC`/`PSX`/`VLO` **EXTENDED-BUT-LIVE** on an accelerating cycle KPI,
**and all three trade above consensus mean targets on +45–85%/90d revisions** — the textbook `L2`
peak-margin setup, and the exact basis on which `VLO`'s rejection was reaffirmed on 09-04.
**ROTATION promoted this sector to `OW+` today.** The sub-node deserves its own test because
**`P136` measures the 16-name sector and can fire `C` while the three-name refiner leg does
something else** (`W5`).

| | |
|---|---|
| **Frozen observable** | `EW{MPC, PSX, VLO}` **minus `SPY`**, **5 settled-session** returns, `auto_adjust=False`, 2026-09-04 close → **2026-09-14** close |
| **Branch A** (EXTENDED-BUT-LIVE confirmed — the sub-node leads the promotion) | **≥ +7.059** (p85) |
| **Branch B** (the peak-margin trap is loaded and springs) | **≤ −3.740** (p15) |
| **Branch C** | between |
| **`D93` BEFORE freezing** | trailing 252: mean **+1.275** · sd 5.266 · p05 −7.669 · **p15 −3.740** · p50 +0.809 · **p85 +7.059** · p95 +10.846 ⇒ A ≈15% · B ≈15% · C ≈70%. ★ centre **positive**, so the refiners beating `SPY` is the normal state and the row says so |
| **State at registration** | **+4.955 = the 75.4th percentile** — leaning A but inside C |
| **⚠ Event contamination — OWNED, not voided** | the window contains **PPI 09-10** and **CPI 09-11**, both 🔀binary. There is no clean 5-session window; making them anti-signals would be the designed-to-void defect |
| **Anti-signal (VOID)** | 🚨 **the one Card 1 named and `P136` does NOT cover**: a **US federal policy action directed at refiner margins or fuel pricing** (an executive order, a price mechanism, an export restriction on refined products) inside 09-05 → 09-14 — the live thread is *"Trump ramps up pressure on refiners"* [seekingalpha 09-01]. Also VOID on an **OPEC+ emergency production decision** or an **announced Hormuz-open statement**. ⚠ **`P136` was frozen without the policy clause and is NOT amended** (`D242`); `S147` carries it and the difference between the two rows is deliberate |
| **Information content (`L3`)** | **A** says an EXTENDED tag with an accelerating cycle KPI beats a valuation objection, which is a rule the desk can carry. **B** says `L2` loaded and the `ENRG OW+` promotion issued today bought the top of a margin cycle. **Neither merely confirms** |
| **Non-redundancy (`D343`)** | `P136` = the **16-name sector** vs `SPY`, 5 sessions to 09-14 — **same window, different unit.** ★ **The pair is deliberately co-dated**: if `P136` fires `C` and `S147` fires `A` or `B`, the sector verdict and the sub-node verdict have separated, which is the `W5` question this desk keeps re-discovering by accident |
| **Owner** | `industry_US` |

### `S142-ANNEX` — the row's premise inverted inside its own window

**Registered, not re-banded.** `S142` (settles **2026-09-11**) was written 09-02 as
*"the against-us branch of the **FIN UW** issued today"*. **`FIN` moved `UW → N` on 2026-09-05**
(ROTATION §2, carried by `eqflow` −0.220 → −0.023 and Δ −0.220 → −0.004).
⇒ **The frozen observable and thresholds are UNTOUCHED** (`D242`). The annex records only that
**the branch labels must be read against the 09-02 verdict, not against today's**, so the scorer on
09-11 does not read a confirmation as a contradiction. ★ Filed as **`D511`**: *a bracket written
against a verdict can outlive the verdict, and nothing currently links the two — a row's branch
LABELS should carry the verdict they were written against.*


---

# ═══ Registered 2026-09-06 by the `industry_US` run (PREMORTEM) — `S148` · `S149` · `S150` ═══

> **Written INSIDE the PREMORTEM stage, not deferred to writeback** — the 09-05 run's own decision #6,
> and `D490`/`D504`/`D529` are three of this run's dig items. IDs from `module_evidence next-id S`
> (live scan of BOTH scenario files + `llm_outputs` + `REPORT`; highest existing `S147`) — the `D76`
> collision class.
> **Clock**: last settled US session **2026-09-04**. **2026-09-07 is Labor Day (`D507`)**, so the
> settled sessions in every window below are **09-08 · 09-09 · 09-10 · 09-11 · 09-14**.
> ⚠ **Every threshold is stated against the implied move** (`module_flow --positioning`), per the
> stage's own rule.

## `S148` — ★★★ Does `P101`'s inversion survive the software leg's own two biggest scheduled prints?

**Why it exists.** `P101` settled **`FIRED-C` at −6.511pp** on 09-04, having traversed **−12.74pp**
from a +6.228 = 89.7th-percentile registration, with **participation inverting 91.7%/16.7% →
21.1%/73.0%**. It dated `M1251`'s *"IT's weak half is semicap"* without certifying its replacement.
★ **The successor window is not arbitrary: it contains BOTH of the software leg's scheduled prints.**
`ORCL` and `ADBE` both report **2026-09-10 16:00 ET** (`Ticker.earnings_dates`) and **both are in the
19-name software leg**, so the leg is tested by its own constituents rather than by beta.

| | |
|---|---|
| **Frozen observable** | `EW{Application Software, Systems Software, IT Consulting & Other Services; n=19}` **minus** `EW{Semiconductors, Semi Materials & Equipment, Tech Hardware/Storage, Electronic Components, Electronic Equipment, EMS, Communications Equipment; n=37}`, **5-session returns**, `us_top300` constituents, settled closes, `auto_adjust=False`. Window **2026-09-04 close → 2026-09-14 close** (09-08 · 09-09 · 09-10 · 09-11 · 09-14) |
| **Constituent reconstruction, verified** | **SW n=19**: MSFT · **ORCL** · PLTR · PANW · IBM · CRWD · APP · SHOP · CRM · CDNS · FTNT · NOW · SNPS · DDOG · ACN · **ADBE** · INTU · ADSK · MSTR. **HW n=37**: NVDA · AAPL · AVGO · MU · AMD · ASML · INTC · AMAT · LRCX · CSCO · ARM · KLAC · SNDK · TXN · MRVL · DELL · WDC · STX · QCOM · ANET · ADI · APH · GLW · NXPI · MPWR · COHR · TER · LITE · MSI · TEL · HPE · KEYS · CIEN · MCHP · ON · JBL · Q. **Exactly `P101`'s counts, and the reconstruction reproduces `P101`'s settle value (−6.511) on this run's independent price frame** |
| **Branch A (software repairs — the inversion was one window)** | **≥ +3.927** (trailing-252 **p85**, re-measured this run) |
| **Branch B (the inversion deepens into a regime)** | **≤ −7.906** (trailing-252 **p15**) — the line `P101` missed by **1.40pp** |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of the same 5-session spread: p05 **−12.282** · **p15 −7.906** · p50 **−2.219** · **p85 +3.927** · p95 +10.369 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **−6.511 = the 21.0th percentile** (09-04). ⚠ **DISCLOSED: the state sits between C and B, 1.40pp from B's line and 10.4pp from A's.** B is the near branch, **A is the informative one** — an A print reverses a settle this desk called its most informative of the prior run |
| **⚠ Threshold vs implied move — the reason this row is a 5-session SPREAD and not a print bracket** | `ORCL` implied **±11.8%** and `ADBE` **±8.1%** (both to the 2026-09-11 expiry, D5). **A 1-session `EW{ORCL,ADBE}` excess bracket is NO-INFORMATION at any threshold this desk would set**: its trailing-252 p85/p15 are **+3.153 / −3.660 vs `SMH`** — a third of the implied move, so C is guaranteed; and a threshold placed *outside* ±10% has a near-zero base rate, so neither tail can fire. **That bracket is therefore declined and the reason written out** (`B4`, and `D503`'s measured evidence: `S132`/`S138` used ±9.00 and ±11.00 bands on `AVGO`'s print and **both fired C on the same −3.792pp realization**). ★ **This row instead measures the object the prints bear on — the LEG SPREAD — over a 5-session window where the two implied moves are ~1σ of the observable's own distribution (sd 3.33 on 1 session; the 5-session sd is wider), not 3σ** |
| **Anti-signal (VOID)** | a **GICS reclassification moving ≥3 of the 56 IT constituents between legs** inside the window · an **`ORCL` or `ADBE` earnings postponement** · a trading halt ≥1 full session in `NVDA`, `MSFT` or `ORCL`. ⚠ **Base rate checked**: MSCI's 08-31 review was pre-declared a non-voider by `P101` and has passed; no reclassification is scheduled before the 09-18 S&P rebalance, which is **outside** the window |
| **Track KPI** | if **A**, software **participation** (% positive) should exceed hardware's — the leg that inverted, not the mean; if **B**, `ADSK`/`CDNS`/`SNPS`/`PANW`/`DDOG` (the five drag names) should still be the leg's worst five |
| **Dated catalyst** | **US August PPI 2026-09-10** [bls ✓] · **`ORCL` 2026-09-10 16:00 ET** · **`ADBE` 2026-09-10 16:00 ET** · **US August CPI 2026-09-11** |
| **Thread** | ⚠ **no matching thread** — stated explicitly. Neither print appears in `thread --days 7 --scope foreign`; the only carrier is *"What to Expect in Markets This Week: Fresh Inflation Data; Apple's Fall Launch Event and **Oracle Earnings**"* [**2 outlets**, 09-06]. 🚨 **`catalyst_calendar --days 12` printed "(none in window / yfinance unavailable)" for EARNINGS while two ≥$180bn names report inside it** — the reason this binary was un-bracketed, and registered as **`D540`** |
| **Non-redundancy (`D343`)** | `S140` (09-08) measures IT **breadth**; `S145` (09-11) measures the **low-`vol_surge` storage sub-node** vs `SMH`; `S137` measures **optical** vs `SMH`. **None is the software-vs-hardware leg spread**, and `P101` — the only row that was — has settled |
| **Owner** | `industry_US` · **ARMED → settles 2026-09-14** |

## `S149` — ★★★ The regime-flip bracket: the escalation branch vs the **US Treasury Secretary's own** de-escalation forecast

**Why it exists.** This is the both-sides bracket for the run's central event, and the against-us
branch is **named by a policymaker on the record**. On 09-05 the US struck three Iranian oil tankers
[16 outlets] and Iran retaliated against a US naval drone in the Strait [09-06, 5 outlets]. **On the
same day, Treasury Secretary Bessent publicly forecast $40 crude and lower yields post-war**
[economictimes · seekingalpha, 09-05], **OPEC+ met 09-06 and left policy unchanged** [7 outlets], and
Trump called the conflict *"small potatoes"* [3 outlets]. ⚠ **The de-escalation side is larger in
outlet count than the escalation side.** The desk carries **`ENRG OW+`** — the board's only
top-notch overweight — and **every flow number supporting it predates both events.**

| | |
|---|---|
| **Frozen observable** | `CL=F` (WTI front-month) **5-session percentage change**, settled closes, `auto_adjust=False`, window **2026-09-04 close ($91.48) → 2026-09-11 close** |
| **Branch A (the escalation is priced into the barrel)** | **≥ +8.343** (trailing-252 **p85**) — export-capacity destruction transmits; the `ENRG OW+` is confirmed on its driver, not only on its tape |
| **Branch B (Bessent's framing wins — the war premium unwinds)** | **≤ −5.734** (trailing-252 **p15**) — ★ **this is the against-us branch and it hits the desk's ONLY top-notch OW.** A B print also removes the input-cost leg of `P140`'s compression case |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of the 5-session WTI change (%): p05 **−10.294** · **p15 −5.734** · p50 **+0.168** · **p85 +8.343** · p95 +13.779 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | 🚨 **+9.688% = the 87.7th percentile** (08-28 → 09-04) — **already above branch A's line.** ⚠⚠ **DISCLOSED AND IT MATTERS**: the observable is a *change over the NEXT five sessions*, not a level, so the current reading does not pre-fire it; but a +9.7% base makes a further +8.3% a compounding demand and makes **B the more reachable branch from here.** **This is deliberate** — the row exists to test the against-us side, and `B4` says the informative branch is the one that would change the conclusion. ⚠ Also disclosed: mean reversion after a 87.7th-percentile 5-session move is itself a base-rate effect, so a C or B print is **not** by itself evidence about the war |
| **⚠ Threshold vs implied move** | `XLE` implied **±1.6%** (expiry 09-09, D3) — the only Energy straddle available and it **expires before this row settles**, so it cannot bound the window. `CL=F` has no straddle in this instrument. ⇒ **the thresholds come from `D93` on the observable itself, and this is stated rather than a straddle being borrowed from a proxy that expires early** (`M1305`'s scope error, corrected by `M1326`, is the precedent) |
| **Anti-signal (VOID)** | an **OPEC+ emergency (unscheduled) production decision** · a **US SPR release executing inside the window** · a **front-month contract roll dispute or NYMEX specification change**, inside 09-08 → 09-11. ⚠ **Base rate checked**: the 09-06 OPEC+ meeting was **scheduled** and produced **no change** ⇒ explicitly **NOT** a voider (`M1363`, recorded at MACRO §B-2 at D-3, not argued at scoring). The SPR-refill item is a **stated intention with no date** [aljazeera 08-30]; a dated execution **would** void |
| **Track KPI** | if **A**, `oil tanker` theme-age should hold above **1.2×** (today 1.20× on a base of 1,168) and the Hormuz thread should print a weekday leg ≥ 4 outlets; if **B**, `Venezuela` (2.95×) should keep accelerating while `oil tanker` decays — i.e. **the supply story rotates from destruction to addition** |
| **Dated catalyst** | weekly EIA crude print **Wed 2026-09-09** · US August CPI **09-11** (energy component) · the **undated** Hormuz-open statement [`catalyst_calendar` 👁] |
| **Thread** | 🟡 **REIGNITED**, 5 days, outlets **2 → 10 → 7 → 3 → 4**; ⚠ two sibling threads carry 🔴FADING tags that are **weekend-inflated** — their weekday legs read **22→22→19→14→21** and **12→16→9→5→10→16** (rising into Friday), and the per-day denominator is `…09-04 727 · 09-05 281 · 09-06 104` (`D508`) |
| **Non-redundancy (`D343`)** | `P126` (09-09) is a **barrel-vs-chain equity** pair spread; `P139` (09-14) is **upstream/service vs refining equity**; `P140` (09-11) is the **distillate crack**; `S147` (09-14) is refiners vs `SPY`. **Not one of them is the barrel itself**, and every one of them is downstream of it — so if `S149` fires B while the equity rows fire C, the desk learns that the refiner tape is not a barrel trade, which is the exact question `M1245`/`M1246` opened |
| **Owner** | `industry_US` · **ARMED → settles 2026-09-11** |

## `S150` — ★★ The defense node: is it a node event, or is the book simply holding the worst name?

**Why it exists.** `M1370` (this run's EVENT_ALPHA §3) found the **entire defense complex dispersing
on the settled tape** — `RTX` **−0.79** · `LMT` −0.74 · `NOC` −0.72 · `LHX` −0.65 · `EME` −0.63 ·
`GD` −0.52 (OBV **−0.44**) · `HWM` −0.32 — **seven of seven negative, six of seven 분산, every rs20
between −7.6 and −10.3** — and **the book holds `RTX`, the worst flow of the seven.** ⚠⚠ **That
finding is flow-only**, and `D6` grades OBV a C-axis. **It also has no narrative side: no defense
thread appears in the 44-thread alive set.** This row gives it a price observable.

★ **And a discriminating measurement is already on the table.** `EW{LMT,NOC,GD,LHX}` − `RTX` over 5
sessions is **+0.127 = the 57.5th percentile**, i.e. **on price, `RTX` is NOT meaningfully worse than
its peers**, even though on flow it is the worst of seven. ⇒ **the flow says "RTX", the price says
"the node"**, and the row is written on the node.

| | |
|---|---|
| **Frozen observable** | `EW{RTX, LMT, NOC, GD, LHX}` **minus** `SPY`, **5-session** returns, settled closes, `auto_adjust=False`, window **2026-09-04 close → 2026-09-14 close** |
| **Branch A (it was a node air-pocket and it repairs)** | **≥ +2.902** (trailing-252 **p85**) |
| **Branch B (the node is de-rating and the book's position is inside it)** | **≤ −3.611** (trailing-252 **p15**) |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of the same spread: p05 **−5.777** · **p15 −3.611** · p50 **−0.153** · **p85 +2.902** · p95 +5.689 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | 🚨 **−5.166 = the 7.1st percentile of the trailing year** (09-04). ⚠⚠ **DISCLOSED: the state is already BELOW branch B's line.** That is unusual and is the reason the row is worth registering — **a one-year-extreme starting point makes A the informative branch and makes a C print meaningful too** (a C from −5.166 requires the spread to *improve* by ~1.5pp). ⚠ `B4`: **B is near-certain to be re-touched and therefore carries little information; A and C are where the information is**, and that is stated at registration rather than discovered at scoring |
| **⚠ Threshold vs implied move** | `RTX` implied **±2.1%** (expiry 09-11, D5) — the basket is 5 names, so single-name implied moves diversify down; the p85/p15 lines (**+2.90 / −3.61**) sit **outside** a diversified ~±1% basket move ⇒ **the thresholds carry information.** Stated rather than assumed |
| **Anti-signal (VOID)** | a **US continuing-resolution lapse or defense-appropriations shutdown event** · **announced M&A involving any of the five** · a **dated large-program award or cancellation ≥$5bn** to any of the five, inside 09-08 → 09-14. ⚠ **Base rate checked**: the 7-day foreign feed carries **no** defense-appropriations item and **no** defense thread at all — which is itself the reason this leg is under-computed |
| **Track KPI** | if **A**, `RTX`'s RSI (**21.8**, deeply oversold, price at the lower Bollinger band, 1 of 4 MAs) should mean-revert with the node; if **B**, the node's OBV should stay 분배 (`RTX` chart **−35% 20d slope**, corroborating the sweep's −0.29 — **two independent instruments agree on this name**, unlike `NEM` below) |
| **Dated catalyst** | ⚠ **NONE DATED — and that is declared, not hidden.** No defense catalyst appears in `catalyst_calendar --days 12` or in the 44-thread alive set. **This row is registered on a positioning extreme with no scheduled event**, which makes it a weaker row than `S148`/`S149` and it is filed as ★★ rather than ★★★ for exactly that reason |
| **Thread** | ⚠ **no thread. Explicitly stated.** The defense complex does not appear in the alive set at all — the flow moved and the wires did not |
| **Non-redundancy (`D343`)** | `S126` (settled `FIRED-C`) measured `XLI` **sector-wide**; nothing on the board measures the defense sub-node, and `D416`-style sub-node blindness is the class of error this desk has logged repeatedly (`M1317` on AI-power electrical, `M1319` on health-care equipment) |
| **Owner** | `industry_US` · **ARMED → settles 2026-09-14** |

### ⚠ Binaries considered and NOT bracketed, each with its reason (`B4`)

| binary | date | why no bracket |
|---|---|---|
| **`ORCL` / `ADBE` prints, magnitude** | 09-10 16:00 ET | **NO-INFORMATION at any settable threshold.** Implied **±11.8% / ±8.1%**; the observable's trailing-252 p85/p15 vs `SMH` are **+3.15 / −3.66**, a third of the implied move ⇒ C guaranteed. A threshold outside ±10% has a near-zero base rate ⇒ neither tail can fire. **Measured precedent**: `S132` (±9.00) and `S138` (±11.00) **both fired C on the identical −3.792pp `AVGO` realization** (`D503`). ⇒ **the bracket is spent on `S148`, which measures the object the prints bear on** |
| **US August PPI** | 09-10 | **Not bracketed alone.** Its transmission is already inside **`S148`** (the window contains it) and **`S149`** (the CPI/PPI energy component). A standalone PPI row would duplicate `P121`/`P125`'s leg question, and those are **blocked on `D427`** rather than absent |
| **FOMC + SEP/dot plot** | 09-16 | **Outside every window this run opens** and 10 days out. Deliberately left for the next run, which will have a settled tape and a fresh COT (Friday 09-11) to set the thresholds from |
| **S&P quarterly rebalance / quadruple witching** | 09-18 | **Structural, not directional.** Neither branch would change a sector verdict — it changes *volume*, and the desk has no volume-conditioned proposition. `P124` already settles 09-18 |
| **KOSPI200 quadruple witching** | 09-10 | 🚫 **Out of scope for a `--market us` runtime** (`W1`). The 09-06 KR run named it and stated it has no PREMORTEM block; **this run records that the assignment cannot be discharged by a US-pure desk either**, so `D533` stays open and needs a human or a KR protocol change (**P5**) |

---

## `S152` — ★★★ The ECB decision the desk's own calendar does not carry · ARMED · → settle **2026-09-14**

Registered **2026-09-07 by the `industry_US` PREMORTEM (Lens 2), before the event.**

**The gap it fills.** `catalyst_calendar --days 10` names four binaries (US Aug PPI 09-10, US Aug CPI
09-11, FOMC 09-16, an undated Hormuz statement) and **carries no foreign central-bank dates at all**.
Body-confirmed this run `[news — economictimes/Reuters, 2026-09-07, read in full]`: the ECB *"is
widely expected to raise interest rates on Thursday"* (**2026-09-10**); markets have *"fully priced in
a 25-basis-point increase, which would take the deposit rate to **2.5%**"*; euro-area inflation is
**back above 3% in August**, *"largely because of higher energy costs"*; European gas is at its
**highest since early 2023**. ⇒ registered as **`D562`** and bracketed here.

**The against-us branch, stated first.** This desk's tilt is a **US-domestic** rate story: `P121`'s
policy-path frame, `P142`'s Fed-hike repricing, and three underweights (`RE` · `STPL` · `UTIL`)
argued on US duration. **The against-us reading is that the long-end move is EXTERNAL** — an ECB
hike, plus Japan funding yen intervention by **selling US Treasuries** (`EVENT_ALPHA` Card 2: reserves
−6.18% to $1.207tn, ¥27.1tn of 2026 intervention, *"Japan likely sold a portion of its U.S. Treasury
holdings"*), plus $40tn debt / $1.25tn annual interest (Card 6). In that world the **US front end can
fall while the US long end keeps rising**, and all three UW verdicts are right for a cause the desk
has never written down — meaning their kill conditions point at the wrong variable.

| field | value |
|---|---|
| **Frozen observable** | **`TLT` 3-session % change**, settled closes, `auto_adjust=False`, window **2026-09-09 close → 2026-09-14 close** (the 3 settled sessions 09-10, 09-11, 09-14). ⚠ The start is **09-09** deliberately, so the ECB decision (09-10) and the US CPI print (09-11) are **inside** the window and not in the base |
| **A (AGAINST US)** | **≥ +0.913%** (trailing-252 **p85**) — a hiked-and-done ECB plus a soft CPI pulls global duration back; `RE`+`STPL`+`UTIL` lose their driver **together** and `P142` branch B is the consistent partner |
| **B (with us)** | **≤ −1.124%** (trailing-252 **p15**) — hawkish guidance transmits to the US long end while Japan keeps funding intervention by selling USTs; the three underweights are vindicated **on an external cause** |
| **C** | between — disclosed favourite |
| **`D93` before freezing** | trailing 252 of `TLT` 3-session % change: p05 **−1.651** · **p15 −1.124** · p50 **−0.081** · **p85 +0.913** · p95 +1.468 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **+0.415% = the 67.1st percentile** (09-04 settled close 82.21) — ★ **inside C and genuinely mid-pack.** ⇒ **both branches carry information**, which is NOT true of `P142` (registration already above branch A at the 92.1st pctile) or `P143` (already above p95). **This is the only balanced bracket this desk registered on 2026-09-07 and that is its main virtue** |
| **Implied move** | `module_flow TLT --positioning`: **예상변동 ±0.7%, expiry 2026-09-09, D2.** 🚫 **The straddle EXPIRES BEFORE THE WINDOW OPENS.** Borrowing a proxy straddle that expires early is the scope error `M1305` made and `M1326` corrected ⇒ the thresholds come from `D93` on the observable itself, and the straddle is recorded as **not covering the event** rather than quietly used |
| **Branch information grading (`B4`, before the event)** | **A is the falsifier, B is the confirmer.** B leaves every standing verdict where it is; **A breaks three at once.** ⇒ **A is the informative branch**, disclosed at registration |
| **Anti-signal (VOID)** | an **unscheduled ECB action or emergency statement**; a **BLS delay or methodology restatement of the August CPI release**; or **`hy_oas` ≥ 3.10% on a close** inside the window (then it is a credit event and the rate attribution is void — the clause `S19`/`S41`/`S46` all used) |
| **Track KPI** | if **A**, `bond selloff` `theme-age` falls back inside 2× (from **5.93×** on a base of 247) and `DGS30` retreats from 5.25; if **B**, `DGS30` (96.0th pctile) and `DGS10` (98.8th) hold or extend |
| **Non-redundancy (`D343`)** | `P142` measures the **US front end** (`DGS2` rate of change, settles 09-11) · `P143` the **yen** (`FXY`, 09-14) · `P128` **US credit** (`hy_oas`, 09-08) · `P124` the **dollar** (`DTWEXBGS`, 09-18) · `S135` the **equity** UW basket (09-11). **No row measures the US LONG end**, which is the tenor the external-supply story hits first |
| **Correlated-underweight note (`D512`, and it is now FOUR legs)** | `RE` (`eqflow` −0.124, `exc5` **1/12**), `STPL` (−0.098, 7/19) and `UTIL` (**+0.050**, 7/15) are short duration; **`FIN` (−0.023, 26/47) is long it.** Branch A hits all four at once. ⚠ `S135` (09-11) equal-weights three of them as one bet and `M1372` records that it averages one measured bucket with one mis-measured one — **construction note carried, thresholds unchanged (`D242`)** |
| **Owner** | `industry_US` |

---


---

# ═══ Registered 2026-09-08 by the `industry_US` PREMORTEM — **`P147`** · **`P148`** ═══

> IDs from `module_evidence next-id P --count 8` (live scan of `handoff/*.md` · `llm_outputs/**` ·
> `REPORT/**`; highest existing **P144** at issue time). Both indexed in the `SCENARIOS.md` MASTER INDEX.
> ⚠ Registered under the run's declared constraint: the four PREMORTEM lenses ran **serially and
> in-context**, not as a parallel adversarial agent fan-out (9th consecutive run).
> ⚠ All `D93` percentiles computed on a price frame filtered to `index <= 2026-09-04` — this run's
> window straddles the 09:30 ET open and a partial 09-08 bar appears mid-run (`D577`).

## `P147` — ★★★ US Aug PPI 2026-09-10: is the repricing INFLATION, or is it REAL? · ARMED · → settle **2026-09-10**

**Why it exists.** 🚨 **MANDATORY** — a 🔀binary inside 48 hours of the run (PPI 08:30 ET on 09-10,
~47h out). ⚠ **This desk dropped PPI on information grade (`B4`) for FOUR consecutive runs, and that
decision is overturned here with a measurement rather than by the rule alone**: MACRO §A-2 measured
the five-session 10-year move as **+0.08 real (`DFII10`) vs +0.04 breakeven (`T10YIE`) ⇒ roughly
two-thirds REAL**, i.e. the desk's own instrument says the current repricing is **not** an inflation
event. A PPI surprise is the cleanest available test of that claim and **both branches change it**.

| field | value |
|---|---|
| **Frozen observable** | **`TIP` minus `IEF`, 1-session excess return**, settled closes, `auto_adjust=False`, **2026-09-09 close → 2026-09-10 close** (the PPI print falls inside) |
| **Branch A (it IS an inflation event)** | excess **>= +0.1514%** (trailing-252 **p85**) |
| **Branch B (it is REAL — supply / term premium)** | excess **<= -0.1492%** (trailing-252 **p15**) |
| **Branch C** | between — disclosed favourite |
| **`D93` before freezing** | trailing 252 settled sessions to 2026-09-04: mean **+0.0023** · sd **0.1760** · p05 -0.2712 · **p15 -0.1492** · p50 +0.0054 · **p85 +0.1514** · p95 +0.2612 ⇒ **A ~15% · B ~15% · C ~70%** |
| **State at registration** | **+0.0045 = the 49.2nd percentile — dead centre.** ★ The most balanced starting state this desk has registered; both branches carry equal information |
| **Implied move** | 🚫 **UNCHECKED, with the reason recorded.** The observable is a **spread** and no straddle prices a spread. Leg straddles: `TIP` **±0.7% (expiry 2026-09-18, D10)**, `IEF` **±0.6% (expiry 2026-09-11, D3)** — both bound each leg's **total path to expiry**, not the spread's isolated 1-session move. Borrowing them would be the scope error `M1305` made and `M1326` corrected (`C3`) |
| **Anti-signal (VOID)** | a **BLS delay or methodology restatement** of the August PPI release; an **unscheduled Federal Reserve action**; or a **market-wide trading halt** on 09-10. ⚠ **Base rate pre-stated (`D450`)**: the **ECB decision** and the **`ORCL`+`ADBE` prints** also land on 09-10 — **neither is a voider**; they are same-day noise the 1-session window deliberately accepts, written now so it is not improvised at scoring |
| **Track KPI** | under **B**, `T10YIE` (the one `[FRED]` series not blocked by `D427`) does **not** rise more than 3 bp on the first close covering 09-10 |
| **Information content (`B4`)** | **A falsifies MACRO §A-2's central measurement and the driver behind three live rows; B confirms it against the strongest counter-hypothesis.** Both change a conclusion |
| **Non-redundancy (`D343`)** | `P142` measures the **`DGS2` level** and settles **09-11**, i.e. after CPI, so PPI is not isolable in it · the 09-07 `TLT` row opens 09-09 and spans PPI **and** CPI **and** the ECB together · `P128` is credit · `P124` the dollar · `P146` German equity. **No row isolates the PPI print, and none measures the real-vs-breakeven split at all** |
| **Owner** | `industry_US` |

## `P148` — ★★★ FOMC + SEP 2026-09-16: does the dot plot move the CURVE, or only the level? · ARMED · → settle **2026-09-17**

**Why it exists.** 🚨 **`D564`'s live commitment, discharged three days before its deadline.** `D564`
requires the FOMC+SEP bracket to be registered **by the 2026-09-11 run at the latest**; it was deferred
on 09-06 and 09-07 for valid reasons. **CPI prints 09-11**, after which the pre-print information sits
in the base and the row loses what it exists to capture ⇒ today is the last clean pre-CPI opportunity.

| field | value |
|---|---|
| **Frozen observable** | **`IEF` minus `SHY`, 2-session excess return** (belly minus front end = the **curve-slope** proxy), settled closes, `auto_adjust=False`, **2026-09-15 close → 2026-09-17 close** (the decision and the SEP fall inside; the start is 09-15 so the pre-meeting positioning day is in the base) |
| **Branch A (hawkish dots — the curve FLATTENS)** | excess **<= -0.3469%** (trailing-252 **p15**) ⇒ `RE`/`STPL`/`UTIL` vindicated on the Fed's own path; `P142`'s front-end read extends |
| **Branch B (dovish dots — the curve STEEPENS)** | excess **>= +0.2856%** (trailing-252 **p85**) ⇒ `RE`+`STPL`+`UTIL` lose their driver **together** (`D512`: four legs of one bet), `FIN N` is the offset |
| **Branch C** | between — disclosed favourite |
| **`D93` before freezing** | trailing 252 settled 2-session windows to 2026-09-04: p05 -0.5119 · **p15 -0.3469** · p50 -0.0199 · **p85 +0.2856** · p95 +0.4615 ⇒ **A ~15% · B ~15% · C ~70%** |
| **State at registration** | **+0.0147 = the 54.0th percentile — near dead centre**, marginally nearer B. Disclosed now, not at scoring |
| **Implied move** | 🚫 **UNCHECKED, with the reason.** `SHY` **±0.5% (expiry 2026-09-18, D10)** and `IEF` **±0.6% (expiry 2026-09-11, D3)** — **`IEF`'s straddle EXPIRES FIVE DAYS BEFORE THE EVENT**, and neither prices a spread. Labelled unchecked rather than "outside the priced move" (`C3`, the `S141` precedent) |
| **Anti-signal (VOID)** | an **unscheduled Fed action or emergency facility** before 09-16; a **change to the FOMC release date**; a **US bank failure**; or **`hy_oas` >= 3.10% on a close** inside 09-15 → 09-17 (then it is a credit event and the rate attribution is void — the clause `S19`/`S41`/`S46` all used) |
| **Track KPI** | under **A**, `DGS2` rises more than `DGS10` (if `D427` unblocks); under **B**, `bond selloff` `theme-age` falls back inside 2x from today's **4.18x** |
| **Information content (`B4`)** | **B falsifies three live sector verdicts at once; A defends them on the strongest external cause.** Both change a conclusion, and **B is the informative branch** because the registration state already sits on B's side of the median |
| **Non-redundancy (`D343`)** | `P142` = **`DGS2` level** (front end, settles **09-11, before the meeting**) · the 09-07 `TLT` row = **long end** (settles **09-14, before the meeting**) · `P143` = **yen** (09-14) · `P124` = **dollar** (09-18) · `P147` = the **real-vs-breakeven split** (09-10). 🚨 **Nothing on this board measures the SLOPE, and nothing at all spans the FOMC date** — both gaps close here |
| ⚠ **Dependency note** | the observable is deliberately **ETF-based, not `[FRED]`-based**, because `D427` has blocked `DGS2`/`DGS10`/`DFII10` for **six consecutive runs** and `R147` retracted this desk's model of when they unblock. **A bracket that cannot be settled is not a bracket** |
| **Owner** | `industry_US` |


---

# Registered 2026-09-12 by the `industry_US` run — **`P149` · `P150`** (MACRO §D) · **`P151` · `S156`** (PREMORTEM §4)

> ⚠ **Append-only** (`D165`). IDs issued by `module_evidence next-id` (P: 149/150/151 · S: 156), not by
> hand-grep. **Language: English.** Full prose, `D93` baselines and branch grading live in
> `llm_outputs/2026-09-12/industry_US/MACRO_REPORT.md §D` and `BLINDSPOT_PREMORTEM.md §4`.
> ★ **All four windows are registered as `base close → terminal close` DATES, both verified trading
> days (`D588`)** — 09-11 (Fri) → 09-18 (Fri), sessions 09-14…09-18, no US holiday; `P151` 09-15 → 09-16.
> 09-18 is quad witching / S&P rebalance — inside the windows, **named, not a voider** (`D450`).

## `P149` — ★★★ The barrel cleared $100 and the equity leg did not follow: convergence or discount? · ARMED · → settle **2026-09-18**

| field | value |
|---|---|
| **Why** | `CL=F` +23.1% over 20 sessions vs `XLE` +6.7% (`SPY` −1.75%); the 20-session `XLE−CL` gap is at the **9.9th pctile**, the 5-session gap at the **7.9th**. `S149`-A, `P122`-A, `P140`-B all settled *for* the level on 09-11 — and the equity market is either late or discounting the premium as transient. No prior row measures equity-vs-commodity (`P126` = chain-vs-barrel inside equities, settled B; `P139` = Venezuela; `P145` = gas) |
| **Frozen observable** | **`XLE` 5-session return minus `CL=F` 5-session return** (pp; benchmark = front-month WTI itself, named inline), settled closes, `auto_adjust=False`, **2026-09-11 close → 2026-09-18 close** |
| **A (convergence)** | gap **≥ +4.69pp** (trailing-252 p85) |
| **B (the equity market keeps discounting $100 as transient)** | gap **≤ −5.17pp** (p15) |
| **C** | between — disclosed favourite |
| **`D93`** | trailing 252 settled 5-session gaps to 09-11: p15 −5.17 · p85 +4.69; current window **−8.78 = 7.9th pctile** ⇒ **enters INSIDE B's zone**, disclosed; mean reversion favours A/C mechanically ⇒ **B is the informative branch** (`L3`) |
| **Both halves (`C2`)** | 20-session: `CL` +23.1% / `XLE` +6.7% / `SPY` −1.75%; 5-session: +9.4% / +1.7% / −0.77% |
| **Anti-signal (VOID)** | front-month `CL` roll inside the window (October expires ~09-22 — outside) · a **confirmed Hormuz reopening / ceasefire statement by ≥3 outlets** · an `XLE` constituent M&A ≥ $10bn. ★ **Pre-declared (DRIFT addendum, `M1481`)**: the Muscat route-agreement signing dated **09-14** `[WebSearch]`, whose Iranian terms exclude US/Israeli vessels, is **NOT a reopening statement** — VOID requires ≥3 outlets carrying "reopened"/"open to all shipping" or transit counts recovering past ~18/day |
| **Track KPI** | EW Energy breadth5 (12/16 on 09-11); `[COT]` WTI pctile (75) |
| **Implied move** | UNCHECKED — no straddle prices the spread (`C3`) |
| **Information (`B4`)** | B says a second week of divergence is a priced view, not noise; A is the OW's second leg |
| **Owner** | `industry_US` |

## `P150` — ★★★ Health Care's one-week, 4-of-32 drawdown: persists, or reverts? · ARMED · → settle **2026-09-18**

| field | value |
|---|---|
| **Why** | EW Health Care exc5 **−3.175pp vs `SPY` = 7.5th pctile**, breadth **4/32 = 3.2nd pctile** (the p05 level); HLTH `eqflow` +0.190 → −0.059 (Δ −0.250, the board's largest weekly drop). `S133` (09-14) measures constituents-vs-`XLV`, not sector-vs-market; `S128`'s reversal factor held (+6.76pp) and would favour a bounce mechanically |
| **Frozen observable** | **equal-weight `us_top300` Health Care basket (32 names, `SECTOR_FLOW_US.json §names` of 2026-09-12) 5-session excess return vs `SPY`**, settled closes, `auto_adjust=False`, **2026-09-11 close → 2026-09-18 close** |
| **A** | excess **≤ −2.594pp** (p15) ⇒ a two-week sector-level fact; HLTH demoted on measurement |
| **B** | excess **≥ +2.422pp** (p85) ⇒ the week was a one-off (`S128`-class reversal) |
| **C** | between — disclosed favourite |
| **`D93`** | trailing 252 settled 5-session windows to 09-11: mean −0.025 · sd 2.380 · p05 −3.391 · **p15 −2.594** · p50 −0.044 · **p85 +2.422** · p95 +4.067; current (ending) window −3.175 = 7.5th pctile; the registered window starts fresh at 09-11 |
| ⚠ **Reading corrected at PREMORTEM (thresholds untouched, `D242`)** | `[WebSearch]` (`M1478`): the week was **three idiosyncratic breaks** — `AMGN` −10.1% 09-08 (Novartis/Ionis pelacarsen Ph3 miss → olpasiran read-through; Tavneos suspension), `BSX` and `SYK` (separate cyber attacks) — with 4/32 breadth by sympathy. **A therefore measures "the sympathy drawdown persists after the causes are known", not "rotation"; B measures the survivors' bounce (`REGN`/`VRTX`/`GILD`/`TMO`)** — the three broken names are excluded from any bounce *reading* (they are still inside the frozen basket) |
| **Information (`B4`)** | A is the informative branch (first sector demotion on a measured two-week breadth fact) |
| **Anti-signal (VOID)** | an FDA decision / trial readout with a named date at ≥3 of the 32, or a federal drug-pricing / Medicare rule with a named effective date, inside 09-14 → 09-18. ⚠ Unverifiable on the desk's feeds today (G1) — checked by `[WebSearch]` at scoring, else recorded **unknown** (`C3`). Earnings inside the window: **none** (`Ticker.earnings_dates`, checked 09-12) |
| **Track KPI** | HC breadth5 (4/32); `eqflow` HLTH (−0.059) |
| **Implied move** | `XLV` **±1.8% (09-18, D6)** — a different object (ETF, not the EW basket excess); stated, not used as the bar |
| **Non-redundancy (`D343`)** | `S133` = six names vs `XLV`; `S135` (settled A) = the UW trio; no row measures Health Care vs the market |
| **Owner** | `industry_US` |

## `P151` — ★★★ FOMC 09-16, the LEVEL companion: was the hike a surprise in either direction? · ARMED · → settle **2026-09-16**

| field | value |
|---|---|
| **Why** | `P148` (slope, `IEF−SHY` 2-session 09-15→09-17) is **already inside branch A (−0.650%, 2.8th pctile) before the meeting**; with the hike itself at **87%** `[WebSearch]` the slope cannot tell "as priced" from "hawkish". The level can |
| **Frozen observable** | **`SHY` 1-session return, 2026-09-15 close → 2026-09-16 close** (`auto_adjust=False`), percent |
| **A (hawkish beyond consensus)** | `SHY` **≤ −0.236%** (trailing-252 1-session **p05**) ⇒ duration trio UW, FIN N−, and the "hike cycle" registry entry confirmed on the Fed's own print |
| **B (dovish surprise — no hike, or a dovish statement/dots)** | `SHY` **≥ +0.134%** (**p95**) ⇒ **falsifies** the UW trio's driver, FIN N−, and `MET`'s asset-yield thesis at once |
| **C** | between = "hike delivered, nothing learned" — disclosed favourite (≈90% by construction; tails chosen so A/B mean *surprise*) |
| **`D93`** | trailing 252 settled 1-session `SHY` returns to 09-11: p05 −0.236 · p15 −0.073 · p50 +0.006 · p85 +0.085 · p95 +0.134 · sd 0.109. ±0.1% ≈ ±5 bp on the 2y |
| **Implied move** | `SHY` **±0.7% to 09-18 (D6)** — both thresholds sit **inside** the 6-session priced path (per-session ≈ ±0.29%) ⇒ pre-declared: **history-graded information row, not an options-surprise trigger** (`C3`) |
| **Information (`B4`)** | **B is the informative branch** (falsifies three live verdicts); A confirms; neither firing + `P148` C = "the meeting was priced" — itself the finding |
| **Anti-signal (VOID)** | unscheduled Fed action before 09-16 · FOMC release date changed · US bank failure · `hy_oas` ≥ 3.10 on a 09-15/16 close. ⚠ **If no SEP/dots are published** (`[WebSearch]` reads contradict on this) **the row still scores** — the observable does not depend on the dots |
| **Non-redundancy (`D343`)** | `P148` = slope · `P142` = `DGS2` level (blocked, `[FRED]`) · this = ETF front-end level, 1 session |
| **Owner** | `industry_US` |

## `S156` — ★★ The crack after the record: does the product scarcity survive a Hormuz headline week? · ARMED · → settle **2026-09-18**

| field | value |
|---|---|
| **Why** | The Energy OW's driver is the distillate crack (`P140`-B: level **108.24 = 99.2nd pctile**, 60-session +51.14 = 96.8th). `P140` is settled and `P149` VOIDs on a reopening — leaving the OW unbracketed exactly when its against-us branch has a dated tell (Muscat 09-14). **This row does not void on the signing: it measures it** |
| **Frozen observable** | **distillate crack = `HO=F` × 42 − `CL=F` ($/bbl), 5-session change, 2026-09-11 close (108.24) → 2026-09-18 close** |
| **A (the crack collapses — the against-us branch priced)** | change **≤ −4.25** (trailing-252 5-session p15) ⇒ refiners' driver breaks; name rails `MPC` MA20 $374 / `PSX` $247.5 / `VLO` $359 are the tells |
| **B (the scarcity extends through the headlines)** | change **≥ +8.70** (p85) ⇒ a second record; `P149`'s equity lag becomes the anomaly |
| **C** | between — disclosed favourite |
| **`D93`** | trailing 252 settled 5-session changes to 09-11: p05 −8.94 · **p15 −4.25** · p50 +0.18 · **p85 +8.70** · p95 +12.77; current (09-03→09-11) **+6.61 = 81.3rd pctile** ⇒ enters leaning B, disclosed |
| **Both halves (`C2`)** | gasoline crack `RB×42−CL` **38.85 = 61.9th pctile level, 20-session −11.27 = 4.0th pctile** — the product split is distillate-up / gasoline-down; this row measures distillate only |
| **Implied move** | no listed straddle on the spread — UNCHECKED (`C3`); `XLE` ±1.3% (09-14, D2) does not cover the window |
| **Anti-signal (VOID)** | a front-month `HO`/`CL` roll inside the window (October `CL` ~09-22, `HO` 09-30 — both outside) · an exchange trading halt |
| **Information (`B4`)** | **A is the informative branch** — the first measured break in the desk's OW driver since 08-21, firing on the headline the desk cannot date |
| **Owner** | `industry_US` |



---

# Registered 2026-09-14 by the `industry_US` run — **`P152` · `P153`** (MACRO §D) · **`P154` · `P155` · `P156`** (PREMORTEM §3)

> IDs by `module_evidence next-id` (the in-flight KR run took `M1494`/`D600`–`D602` the same morning — collision
> avoided by issuing after it). Thresholds = trailing-252 percentiles computed **before** freezing
> (`llm_outputs/2026-09-14/industry_US/_d93_p152_p153.txt`, `_d93_p154_p156.txt`). Windows are NYSE trading-day
> `base close → terminal close` dates (`D588`). Implied move `UNCHECKED` on every row (EW baskets / ETF pairs have
> no listed straddle for the window; `--positioning` not run) — pre-declared, not claimed. Instrument state at
> registration: sweep asof 09-11 (reprint), news pipe dead 13:19 → 14:3x (titles only), live Asia tape unsettled.

## `P152` — ★★★ The SECOND chokepoint: Bab el-Mandeb + the Saudi East-West bypass — is the freight leg still early, or already the crowded expression? · ARMED · → settle **2026-09-21**

| field | value |
|---|---|
| **Frozen observable** | **`EW{FRO, DHT, INSW, STNG, TNK}` 5-session excess return vs `SPY` (pp)**, settled closes, `auto_adjust=False`, **2026-09-14 close → 2026-09-21 close** (09-15, 09-16, 09-17, 09-18, 09-21; quad witching 09-18 inside — owned) |
| **Branch A (the shipping leg is where the shock is priced — the exposure map is missing it)** | ≥ **+6.240pp** (p85) |
| **Branch B (it was the crowded expression; the shock reverts through the tankers first)** | ≤ **−4.308pp** (p15) |
| **Branch C** | between — disclosed favourite |
| **`D93` before freezing** | n=252: mean +1.060 · sd 5.455 · p05 −7.911 · p15 −4.308 · p50 +1.733 · p85 +6.240 · p95 +9.176 ⇒ A ≈15% · B ≈15% · C ≈70%; ⚠ centre positive (+1.06, median +1.73) — tankers beating `SPY` over a week is the *normal* state in this sample |
| **State at registration** | 09-04 → 09-11 **+7.947pp = 91.7th pctile** — already above A on the prior window ⇒ **A is low-information, B informative** (`L3`) |
| **Anti-signal (VOID)** | a ≥3-outlet title inside the window stating the East-West pipeline **has reopened** *and* Bab el-Mandeb transit **restored**; announced M&A / fleet sale at any of the five. A reopening *statement* without both legs is NOT a voider (the `P149` convention) |
| **Track KPI** | A ⇒ `S156`-A and `P149`-B are the consistent partners (shock lives in freight + product); B ⇒ `P149`-A and a holding crack |
| **Dated catalyst** | FOMC 09-16 (both legs via `SPY`), quad witching 09-18 — owned, not voided |
| **Non-redundancy (`D343`)** | `P145` (LNG chain, 09-14) = gas leg; `P149` = barrel vs equity; `S156` = product; `P136`/`P139` = the 16-name label / its chain split. **No row measures freight**; `S61`/`S84`/`S92` (Aug, Red Sea premium) are closed and on a different instrument set |
| **Information grade (B4)** | HIGH on B · LOW on A |
| **Implied move** | `UNCHECKED` |
| **Owner** | `industry_US` |

## `P153` — ★★ The yen after the flip: speculators net long for the first time since February, BoJ 09-18 JST, `FXY` at the 89th percentile — does the carry unwind extend through both central banks, or was the flip the top? · ARMED · → settle **2026-09-21**

| field | value |
|---|---|
| **Frozen observable** | **`FXY` 5-session % change**, settled closes, `auto_adjust=False`, **2026-09-14 close → 2026-09-21 close** |
| **Branch A (the unwind extends — yen up through both meetings)** | ≥ **+0.855%** (p85) |
| **Branch B (the positioning flip was the top — yen gives it back)** | ≤ **−1.059%** (p15) |
| **Branch C** | between — disclosed favourite |
| **`D93` before freezing** | n=252: mean −0.088 · sd 1.244 · p05 −1.530 · p15 −1.059 · p50 −0.266 · p85 +0.855 · p95 +2.689 |
| **State at registration** | 09-04 → 09-11 **+1.376% = 89.3rd pctile** (`FXY` 58.87 → 59.68) ⇒ **B is the informative branch** |
| **Dated catalyst** | **FOMC 09-16** (inside, owned) · **BoJ decision Fri 2026-09-18 JST ≈ Thu 09-17 23:00 ET** (`[WebSearch]`, PREMORTEM Lens 2 — MACRO §D wrote `[blank]`; corrected at PREMORTEM, both left standing per `D48`) — inside the window |
| **Anti-signal (VOID)** | BoJ decision moved outside the window (then re-labelled a run-up measure, not voided) · MoF intervention confirmed by ≥3 outlets (VOID — official, not positioning) |
| **Track KPI** | A ⇒ `P138`'s successor question (does the US long end follow) is live again; B ⇒ the carry-unwind narrative is retired for this cycle |
| **Non-redundancy (`D343`)** | `P143` (09-08 → 09-14) settles tonight and does not span the BoJ; `P148`/`P151` = US curve/level; `S152` = `TLT` on the ECB; `P154` = the equity transmission (different object) |
| **Information grade (B4)** | HIGH on B · MEDIUM on A |
| **Implied move** | `UNCHECKED` |
| **Owner** | `industry_US` |

## `P154` — ★★★ Does the carry unwind reach US equities? Yen → NDX transmission across BoJ + quad witching · ARMED · → settle **2026-09-21**

| field | value |
|---|---|
| **Frozen observable** | **`QQQ` − `SPY` 2-session excess return (pp)**, settled closes, `auto_adjust=False`, **2026-09-17 close → 2026-09-21 close** (sessions 09-18, 09-21; BoJ decision and quad witching inside — owned) |
| **Branch A (the unwind reaches equities — NDX lags)** | ≤ **−0.632pp** (p15) |
| **Branch B (NDX leads through both events)** | ≥ **+0.772pp** (p85) |
| **Branch C** | between — disclosed favourite |
| **`D93` before freezing** | n=252 2-session: mean +0.046 · sd 0.783 · p05 −1.401 · p15 −0.632 · p50 +0.071 · p85 +0.772 · p95 +1.220 |
| **State at registration** | 09-09 → 09-11 **−0.448pp** (inside C, leaning A); live `NQ=F` −1.25% vs `ES=F` −0.49% (13:39 KST, unsettled) |
| **Anti-signal (VOID)** | BoJ decision moved outside 09-17/18 (re-verify at scoring) · MoF intervention ≥3 outlets · an `NVDA`/`AVGO` company-specific 8-K inside the window (then `P155` owns the move) |
| **Pairing** | `P153`-A ∧ `P154`-A = carry unwind confirmed in equities; `P153`-A ∧ `P154`-C = the yen moved without the equity channel (`P138`-B extends) |
| **Information grade (B4)** | **A HIGH** — first measured test of whether the AI-slowdown narrative (≥18 outlets, titles) has a macro trigger; B LOW |
| **Non-redundancy (`D343`)** | `P153` = yen only; `P148`/`P151` = US curve/level; `P155` = 1-session NDX funding (different window/object) |
| **Implied move** | `UNCHECKED` |
| **Owner** | `industry_US` |

## `P155` — ★★ The 09-18 Nasdaq-100 funding sale: do the two largest weights pay for SpaceX? · ARMED · → settle **2026-09-18** (companion 09-21, reported not branched)

| field | value |
|---|---|
| **Frozen observable** | **`EW{NVDA, AVGO}` 1-session excess return vs `SPY` (pp)**, settled closes, `auto_adjust=False`, **2026-09-17 close → 2026-09-18 close**; companion: same object 09-18 → 09-21 (reported for the reversal read) |
| **Branch A (the funding sale prints)** | ≤ **−1.932pp** (p15) on 09-18 |
| **Branch B (no funding footprint — pre-positioned or absorbed)** | ≥ **+1.584pp** (p85) on 09-18 |
| **Branch C** | between — disclosed favourite |
| **`D93` before freezing** | n=252 1-session: mean +0.006 · sd 1.839 · p05 −2.824 · p15 −1.932 · p50 +0.014 · p85 +1.584 · p95 +3.041 |
| **State at registration** | 09-11 session **−0.708pp** (inside C) |
| **Why it exists** | SpaceX Nasdaq-100 pro-forma weight 1.28% → ~2.82%, announced 09-18 after the bell, effective 09-21, ≈$15.5bn passive (JPM est.) — `[WebSearch]`, PREMORTEM Lens 2; `P124`/`P149`/`P150`/`S156`/`P152` span 09-18 but none measures the mechanism |
| **Anti-signal (VOID)** | Nasdaq's official pro-forma shows SpaceX funded elsewhere with `NVDA`/`AVGO` weights unchanged · a company-specific print at either name inside the window |
| **Information grade (B4)** | MEDIUM — informative reading is A-without-09-21-reversal (a demand fact) or B (flow already in) |
| **Non-redundancy (`D343`)** | no row measures the rebalance mechanism; `S56` (Aug SPCX unlock) closed |
| **Implied move** | `UNCHECKED` |
| **Owner** | `industry_US` |

## `P156` — ★★ The barrel's own sign: disambiguating `P149`-A across the de-escalation branch · ARMED · → settle **2026-09-21**

| field | value |
|---|---|
| **Frozen observable** | **`CL=F` front-month 5-session % change**, settled closes, **2026-09-14 close → 2026-09-21 close** |
| **Branch A (the escalation extends — barrel higher)** | ≥ **+8.764%** (p85) |
| **Branch B (de-escalation prints — barrel collapses)** | ≤ **−5.734%** (p15) |
| **Branch C** | between — disclosed favourite |
| **`D93` before freezing** | n=252 5-session: mean +1.135 · sd 7.599 · p05 −10.294 · p15 −5.734 · p50 +0.555 · p85 +8.764 · p95 +13.779 |
| **State at registration** | 09-04 → 09-11 **+9.584%** (`CL` 100.05) — above A on the prior window; live +2.85% (unsettled) ⇒ **B is the informative branch** |
| **Why it exists** | `P149`-A fires on "equity catches up" *and* on "barrel falls to equity" — sign-ambiguous; the de-escalation branch (Trump "war ends after midterms, oil falls sharply" · Iran–UAE · Pezeshkian, `[titles]`) is a VOID in `P149`/`P152`, not a measured branch anywhere |
| **Anti-signal (VOID)** | front-month roll inside the window (October expiry ~09-22 — outside, checked) · OPEC+ emergency decision (title-verifiable only, `C3`) |
| **Pairing** | `P149`-A ∧ `P156`-B = the discount branch (barrel fell to equity); `P149`-A ∧ `P156`-A/C = genuine convergence |
| **Non-redundancy (`D343`)** | `S149` (WTI 5s) settled 09-11; `P122` settled; `P149` = spread; `S156` = product |
| **Implied move** | `UNCHECKED` |
| **Owner** | `industry_US` |
