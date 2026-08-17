# L1 · PREMORTEM — blind-spot pre-mortem (stage) ★US-only

> Phase 1.5. Four adversarial subagents argue **AGAINST our own tilt** BEFORE the deep budget is
> committed. No rubber-stamping. Anti-tunnel (born from the 2026-07-14 postmortem: GS bank leg
> missed, cool-CPI semi rip missed, "already ran" names avoided wrongly, zero #1-cycle exposure).
> Output: `BLINDSPOT_PREMORTEM.md`.

## Calls
- Not a module — an **Agent fan-out, 4 lenses in ONE message (parallel)**. Each agent gets the draft
  tilt + 4 DEEP picks + flow sweep + dated catalysts, and MUST return named tickers + dated catalysts:
  1. **UNDER-COMPUTED LEGS** — strongest bull case for a sector/sub-leg we did NOT deep-dive that has
     a catalyst ≤~5 trading days. Verdict per leg: PROMOTE-TO-DEEP or WITHIN-RUN-WATCH.
  2. **REGIME-FLIP / BOTH-SIDES** — for each known binary (from CATALYST_WATCH), the against-us
     branch: what rips, which of our OWs gets hit, a starter list + trigger + invalidation.
  3. **MOMENTUM-CONTINUATION** — "already ran +100%" ≠ avoid. Re-tag each runner
     EXTENDED-BUT-LIVE (cycle KPI still accelerating → add-on-dip) vs EXHAUSTED, with the flip condition.
  4. **CYCLE-EXPOSURE** — dominant-cycle registry vs our coverage AND the real book. Epicenter vs
     one-layer-off audit; flag ZERO epicenter exposure; name the cleanest epicenter expressions.
     Rule: a crowded/🔴 tape gates ADD timing — it never justifies 0% core in a multi-year cycle.

## What this stage does — inject, don't just note
- Synthesize the 4 verdicts into `BLINDSPOT_PREMORTEM.md`:
  under-computed legs (each PROMOTED to a 5th DEEP or logged as within-run watch — never silently
  dropped) · both-sides brackets per binary (→ ALPHA's action bracket) · momentum re-tags ·
  cycle-GAP flag with core expressions (→ BET's epicenter-starter module).
- If all 4 lenses agree with the draft (rare), say so explicitly — the default expectation is that
  at least one leg surfaces something the deterministic desk missed.
- ⚠ Field note (2026-07-15): watch for the **correlated-UW pattern** — two UW sectors that are one
  bet in disguise (RE+DISC both = "core-sticky wins"); the lens-2 bracket is what catches it.

### Carry rules from `handoff/RESEARCH.md` (loaded by HANDOVER; binding here)
- ⚠ **Grade each branch by information content before the event, not after** (lens B4). Branches are
  not symmetric: one outcome may only be able to *confirm*, while the other can *falsify*. Measured
  framing — a hyperscaler capex **cut** breaks both the volume and the price leg of a memory thesis,
  while a **raise** confirms volume only and cannot un-measure the contract-price series, because
  the same buyers signed the price caps. **If neither branch would change the conclusion, the event
  is not worth bracketing** — say so and spend the bracket elsewhere.
- ⚠ **Freeze the observable and its threshold at registration** and write them into
  `handoff/SCENARIOS_{US|KR}.md` (this desk's half — split 2026-07-29; the ID must ALSO be added to
  the MASTER INDEX in the `handoff/SCENARIOS.md` spine, and IDs are still allocated against EVERY
  existing row in BOTH files — the D76 collision class).
  A bracket whose threshold moves after the print is a description wearing a
  forecast's clothes. Scoring is L3 [scenario_score](../L3_functions/scenario_score.md), against the
  frozen threshold only.
- ★ **Take the magnitude threshold from the options market, not from your judgement.**
  `module_flow <TKR> --positioning` now prints `예상변동 ±x%` — the nearest-expiry ATM straddle, i.e.
  what is **already priced**. A bracket that fires inside the implied move is not a surprise; a
  bracket needs a threshold *outside* it to carry information. *Measured 2026-07-22*: GOOGL **±7.1%**
  into that night's print. ⚠ Read `D±n` with it — the straddle covers the whole path to expiry, not
  the event alone.
- ⚠ **Score the observable, not the price reaction.** A capex raise the tape sells off still scored
  as a raise. Conflating the two lets the next day's candle rewrite the hypothesis.
- ⚠ **Date-clustered moves are one observation** (lens B3). N names moving together on one day is
  **n≈1**, not n=N — measured 2026-07-21: 18/18 US semis green (median +5.0%), next session 4/4 KR
  semis green (median +7.1%). Normalize by each name's own 20-day volatility before calling a move
  exceptional: **+14.3% on a 9.7% daily sigma is a 1.48 z**, inside the regime, not an outlier.

## ✅ EXIT CHECK
- [ ] 4 lenses fanned out in parallel; each returned named tickers + dated catalysts.
- [ ] **Every bracket names its observable + frozen threshold + date, and is registered in
      `handoff/SCENARIOS_{US|KR}.md` with BOTH branches, and indexed in the `SCENARIOS.md` spine.**
      One-way brackets are protocol violations.
- [ ] **Every magnitude threshold is stated against the implied move** (`module_flow --positioning`
      → `예상변동 ±x%`, with its `D±n`). A threshold inside the implied move is pre-declared as
      **no-information** rather than presented as a trigger.
- [ ] **Each branch graded by information content**; any binary where no branch would change the
      conclusion is dropped with that reason stated.
- [ ] BLINDSPOT_PREMORTEM.md written (legs · brackets · re-tags · cycle GAP).
- [ ] Every catalyst-bearing leg promoted or logged; brackets handed to ALPHA; GAP handed to BET.
- [ ] DEEP set updated if a leg was promoted (state the final set).
