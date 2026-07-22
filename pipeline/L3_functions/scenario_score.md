# L3 · scenario_score — settle one pre-registered scenario

> Atomic, single-role. Called by L2·carryover. **One scenario row in → one branch verdict out.**
> Deterministic: it compares a pre-registered observable against its pre-registered threshold and
> reports which branch fired. It does not interpret, re-weight, or explain away.

## Input
One `ARMED` row from `handoff/SCENARIOS.md` whose event date has passed, carrying:
`id · event · date · branches[A,B,C] · observable · threshold`

## Procedure
1. **Pull the observable only.** Whatever the row named — a capex guide figure, a QoQ contract-price
   band, a MoM export print, a gross-margin guide. Nothing else from that day's news is admissible.
2. **Compare to the pre-registered threshold.** Not to a threshold that seems more reasonable now.
3. **Emit one verdict**:

| Verdict | Meaning |
|---|---|
| `FIRED-A` / `FIRED-B` / `FIRED-C` | The observable met that branch's condition |
| `AMBIGUOUS` | The observable printed but does not cleanly map to any branch |
| `EXPIRED` | The date passed and the observable was never pulled — **a process failure** |
| `VOID` | The premise was invalidated before the event (event cancelled, company delisted, …) |

## Rules
- **The threshold is frozen at registration.** If today's number sits just outside it, that is
  `FIRED` on the other branch — not a reason to widen the band. Moving a threshold after the fact
  converts a forecast into a description.
- **`AMBIGUOUS` is a finding about the scenario, not about the market.** Record what made it
  unscoreable so the next registration is written sharper. It is a legitimate output, not a failure.
- **`EXPIRED` is always logged, never dropped.** An unscored past-dated scenario is precisely how a
  desk keeps its wins and forgets its losses.
- **Score the observable, not the price reaction.** A capex raise that the tape sells off is still
  `FIRED-A`. Conflating the two is how a hypothesis gets rewritten by the next day's candle.
- **The named line item only.** Measured pre-commitment: for a hyperscaler print the observable is
  *capex guidance*; an EPS/revenue beat with capex merely reaffirmed scores as the reaffirm branch.
- Emit the verdict plus the raw observed value, so a later reader can re-check the call without
  re-running the pull.

## Output
```
{id} · {event date} · {verdict} · observed: {raw value} · threshold was: {frozen threshold}
{one line: what this does to the standing view, or "no change"}
```
Appends to the scoring log in `handoff/SCENARIOS.md`. Zero buy/sell language.
