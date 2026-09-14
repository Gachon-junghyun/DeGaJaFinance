# ACTION_TICKETS — 2026-07-31  (conditional DRY-RUN tickets · a human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + SCENARIOS_US both-sides brackets (binary→both branches) + the
> risk model + live prices. **Book total ≈ $10,641 (₩14,684,894) · fx 1450 · per-trade risk 1.5% of
> book ($151.9) · core risk 0.8% ($81.0) · stop 7.0%.** Share counts are **DRY-RUN illustrations of
> influence only** — a human executes separately via `module_kis --order … --execute`; **the desk sends
> no order under any branch, and `TIMEFOLIO_EXECUTE=1` being ARMED changes nothing here (P4/P5).**
>
> ⚠ **This window has NO US-owned binary inside 48h.** Nearest cluster: **MPC 08-04 (S49) · AMD/ANET
> 08-04 (S50) · PSX 08-05 · CEG 08-06 (S49 window close) · NFP 08-07 (S51).** Tickets are pre-committed
> against those settlements. Share math: shares = floor(risk_budget / (price × 0.07)).

---

## CORE-STARTER (tape-independent) — refiner core, to close the Energy epicenter GAP

- **condition:** establish the CORE NOW regardless of tape — closes the rank-2 **Energy/oil-refining
  epicenter GAP (6.87% < 8.0% floor, −1.135pp ≈ $121 to floor)**; the tape is 🟢 accumulating so the
  gate is open for the core (PREMORTEM Lens 4: **add refiners, not integrateds**).
- **instrument (illustration):** **MPC** — the one refiner whose straddle (**±8.5%, expiry 08-21, D21**)
  COVERS its 08-04 print, and which holds a positive days-21-60 base. **3 sh @ ~$313.37** (≈$940
  notional, risk $65.8 = 0.6%, inside the 0.8% core budget) · stop **$291.43 (−7.0%)** · NYSE.
  Alt clean-base expression: **VLO 3 sh @ ~$309.74** (RS60 +19.5 vs SPY, the deepest positive base).
- **⛔ CAVEAT STAMPED (the delta of this run):** the epicenter's own engine — the settled distillate
  crack — **rolled over −5.879 on the 07-30 bar (first negative since 07-24) while crude also fell**, the
  demand-destruction anti-signal. **So the CORE exists (gap real, tape 🟢) but the ADD beyond core is
  DEFERRED** until the 5-session settled crack change re-crosses > 0 (S49 → 08-06). The crack is **+3.0
  with the daily increment already past the −5.0 branch-B magnitude** — one further settled roll kills it.
- **⚠ `core_pick` note (D19, 6th run):** the registry's human-locked `core_pick` is **PSX**, whose
  straddle (±2.4%, expiry 07-31) **expires BEFORE its 08-05 print (not event-priced)** and whose
  days-21-60 base is the weakest of the three refiners. The desk does not choose the instrument (locked
  field); it records that the locked pick is the run's weakest refiner on the measured base.

---

## BRACKET S49 — the distillate-crack margin thesis · MPC 08-04 / PSX 08-05 → 08-06

- **A_with (crack change stays > 0 through 08-06):** refining margin intact, P4 survives the Russia-ban
  expiry ⇒ **ADD refiner. MPC +3 sh @ ~$313.37** (risk $65.8) on the confirming settled close.
- **B_against (crack change ≤ −5.0 by 08-06):** the bottleneck is releasing — hits **ENRG OW− AND INDU
  OW− on the same tick** (M91 fuel-surcharge). ⇒ **TRIM / no-add the refiner core; do not average down.**
  (No buy ticket on this branch — the informative branch is a stand-down.)
- **live state:** +3.0, daily increment −5.879 ⇒ **B is one settled session away.** This is the binary
  the CORE-STARTER caveat rests on.

## BRACKET S31 — is XOM the business or the war premium? → 08-05

- **A_against-us (XOM RS20 vs SPY holds > +10% through 08-05 with crude ≥5% below range):** the
  integrated leg decouples from the crack ⇒ the OW is pointed at the wrong sub-segment ⇒ **rotate the
  refiner CORE toward the crack-pure names (VLO/MPC), away from any integrated beta.** (Read-through, not
  an XOM buy — XOM is the control, RS60 −3.6 vs SPY.)
- **B_with-us (XOM RS20 vs SPY reverts ≤ 0 by 08-05):** the last 20 days were war premium ⇒ the
  refining-margin thesis is the only surviving Energy leg ⇒ the refiner CORE is the right expression.
- **live:** XOM RS20 +12.1 / RS60 −3.6 vs SPY; XOM **missed** Q2 07-31 ⇒ branch A tracking, softening.

## BRACKET S50 — AMD/ANET AI-capex-guidance read · 08-04 → 08-06

- **A_confirm (AMD datacenter guide ≥ prior-Q y/y AND ANET reaffirms cloud-titan revenue):** hyperscaler
  build intact (low-info, confirms volume only) ⇒ **ADD the un-crowded networking pick-and-shovel. ANET
  +12 sh @ ~$177.08** (≈$2,125 notional, risk $150.2 = 1.5%) · stop **$164.68** · NYSE.
- **B_against (AMD datacenter guide cut y/y OR ANET guides down):** capex decelerating at the silicon
  layer ⇒ reads through to the AI-power node (CEG/VST) + IT N(split), and **NVDA's EXTENDED-BUT-LIVE tag
  flips toward EXHAUSTED** ⇒ **no-add / trim AI-compute; do not initiate ANET.** (Informative branch =
  stand-down. Score the GUIDE, not the 1-day price — a cut the tape buys still scores as a cut.)
- **positioning:** AMD P/C 0.99 skew +22.3 (hedging downside) · ANET P/C 0.46 (complacent). n≈1 same-day.

## BRACKET S51 — NFP flattener risk to the FIN OW · 08-07 → 08-10

- **A_with-OW (derived 2s10s ≥ +0.35 at the settled 08-07 close):** bear steepener persists, NIM thesis
  intact, FIN OW− confirmed on its fresh mechanism ⇒ **ADD money-center bank. BAC +35 sh @ ~$62.07**
  (≈$2,172 notional, risk $151.8 = 1.5%) · stop **$57.72** · NYSE. Alt: **JPM +6 sh @ ~$353.70**
  (≈$2,122, risk $148.5) · stop $328.94.
- **B_against (derived 2s10s ≤ +0.20 at the settled 08-07 close):** hot print reprices cuts out → front
  end sells harder → **bear FLATTENER trips the S23 line ⇒ the NIM mechanism breaks and FIN OW− loses its
  only non-retracted leg (R32 killed breadth)** ⇒ **exit / no-add banks.** (Both branches change the FIN
  conclusion — symmetric, information-bearing.)
- **overlay:** if HY OAS breaks > 2.90% on the same print, read it as the credit-fear override separately
  (banks de-rate regardless of NIM). Positioning: KRE P/C 1.87, JPM skew +27.1 (already hedged).

---

## Share-math ledger (DRY-RUN, illustration only)

| Ticket | Price | Stop (−7%) | risk/sh | Budget | **Shares** | Notional |
|---|---|---|---|---|---|---|
| CORE MPC | $313.37 | $291.43 | $21.94 | $81.0 (core 0.8%) | **3** | $940 |
| CORE alt VLO | $309.74 | $287.96 | $21.68 | $81.0 | **3** | $929 |
| S49-A MPC add | $313.37 | $291.43 | $21.94 | $81.0 | **3** | $940 |
| S50-A ANET | $177.08 | $164.68 | $12.40 | $151.9 (1.5%) | **12** | $2,125 |
| S51-A BAC | $62.07 | $57.72 | $4.34 | $151.9 | **35** | $2,172 |
| S51-A alt JPM | $353.70 | $328.94 | $24.76 | $151.9 | **6** | $2,122 |

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order
is sent by this desk under any branch, `--execute` never invoked. A human pulls every trigger (P5).*
