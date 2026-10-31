# L1 · PREMORTEM — blind-spot pre-mortem (stage) ★US-only

> Runs right after MACRO (US only). Four adversarial subagents argue **AGAINST our own tilt** BEFORE the
> earnings and competition budget is committed. No rubber-stamping. Anti-tunnel (born from the 2026-07-14
> postmortem: GS bank leg missed, cool-CPI semi rip missed, "already ran" names avoided wrongly, zero #1-cycle exposure).
> **Reads**: MACRO_REPORT §2–§4, the focus sectors, CATALYST_WATCH, the real book.
> Output: `BLINDSPOT_PREMORTEM.md` — **cap 10 KB**. **Next**: promoted legs join EARNINGS/COMPETITION scope;
> brackets go to ALPHA's tickets; the cycle GAP goes to BET.

## Calls
- [lens](../L2_modules/lens.md) — before registering any bracket, run `python -X utf8 -m module_lens find "<question>"`; then register the question, evidence, branches, and actual weights with `ask` → `ev` → `think` (see lens for exact commands).
- Not a module — an **Agent fan-out, 4 lenses in ONE message (parallel)**. Each agent gets the draft
  tilt + the focus sectors + MACRO's transmission lines + dated catalysts, and MUST return named tickers +
  dated catalysts; prefer earnings observables (guide, order, margin) over tape observables:
  1. **UNDER-COMPUTED LEGS** — strongest bull case for a sector/sub-leg we did NOT deep-dive that has
     a catalyst ≤~5 trading days. Verdict per leg: PROMOTE-TO-FOCUS or WITHIN-RUN-WATCH.
  2. **REGIME-FLIP / BOTH-SIDES** — for each known binary (from CATALYST_WATCH), the against-us
     branch: what rips, which of our OWs gets hit, a starter list + trigger + invalidation.
  3. **MOMENTUM-CONTINUATION** — "already ran +100%" ≠ avoid. Re-tag each runner
     EXTENDED-BUT-LIVE (cycle KPI still accelerating → add-on-dip) vs EXHAUSTED, with the flip condition.
  4. **CYCLE-EXPOSURE** — dominant-cycle registry vs our coverage AND the real book. Epicenter vs
     one-layer-off audit; flag ZERO epicenter exposure; name the cleanest epicenter expressions.
     Rule: a crowded/🔴 tape gates ADD timing — it never justifies 0% core in a multi-year cycle.

## What this stage does — inject, don't just note
- Synthesize the 4 verdicts into `BLINDSPOT_PREMORTEM.md`:
  under-computed legs (each PROMOTED to a 5th focus sector or logged as within-run watch — never silently
  dropped) · both-sides brackets per binary (→ ALPHA's action bracket) · momentum re-tags ·
  cycle-GAP flag with core expressions (→ BET's epicenter-starter module).
- If all 4 lenses agree with the draft (rare), say so explicitly.
- ⚠ Field note (2026-07-15): watch for the **correlated-UW pattern** — two UW sectors that are one
  bet in disguise (RE+DISC both = "core-sticky wins"); the lens-2 bracket is what catches it.

### Carry rules from `handoff/RESEARCH.md` (loaded by HANDOVER; binding here)
- ⚠ **Grade each branch by information content before the event** (lens L3): one outcome may only confirm,
  the other falsify (a hyperscaler capex **cut** breaks volume and price legs of a memory thesis; a **raise**
  confirms volume only). **If neither branch would change the conclusion, do not bracket it** — say so.
- ⚠ **Freeze the observable and its threshold at registration** in the lens ledger (`ask` → `think`); the ledger
  allocates the Q ID, so the old hand-allocated ID collisions (D76, `S##-KR`) cannot recur. A bracket whose threshold moves after the print is a description wearing a
  forecast's clothes. Scoring is the lens `resolve` at HANDOVER (the old L3 scenario_score), against the
  frozen threshold only.
- ★ **Take the magnitude threshold from the options market**: `module_flow <TKR> --positioning` prints
  `예상변동 ±x%` (nearest-expiry ATM straddle = already priced; GOOGL ±7.1% into its 2026-07-22 print). A
  threshold inside it carries no information. Read `D±n` with it — the straddle covers the whole path to expiry.
- ⚠ **Score the observable, not the price reaction.** A capex raise the tape sells off still scored
  as a raise. Conflating the two lets the next day's candle rewrite the hypothesis.
- ⚠ **Date-clustered moves are one observation** (rule U6): 18/18 US semis green on 2026-07-21 is n≈1. Normalize
  by each name's 20-day volatility: **+14.3% on a 9.7% daily sigma is a 1.48 z**, not an outlier.

## ✅ EXIT CHECK
- [ ] 4 lenses fanned out in parallel; each returned named tickers + dated catalysts.
- [ ] **Every bracket names its observable + frozen threshold + date, and is registered in
      the lens ledger with BOTH branches (Q ID cited in the file).**
      One-way brackets are protocol violations.
- [ ] **Every magnitude threshold is stated against the implied move** (`module_flow --positioning`
      → `예상변동 ±x%`, with its `D±n`). A threshold inside the implied move is pre-declared as
      **no-information** rather than presented as a trigger.
- [ ] **Each branch graded by information content**; any binary where no branch would change the
      conclusion is dropped with that reason stated.
- [ ] BLINDSPOT_PREMORTEM.md written (legs · brackets · re-tags · cycle GAP).
- [ ] Every catalyst-bearing leg promoted or logged; brackets handed to ALPHA; GAP handed to BET.
- [ ] Focus set updated if a leg was promoted (state the final set).
