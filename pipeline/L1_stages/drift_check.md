# L1 · DRIFT_CHECK — measure the book against the mandate (stage)

> Phase 2 of the wrap desk. Pure measurement: where each sector actually sits versus its target, and what the
> book's beta is versus its band. No plan, no judgment yet. Calls L2. Output: `DRIFT_REPORT.md`.

## L2 called
- [mandate](../L2_modules/mandate.md) — `module_paper_book drift [--fx r] [--period 1y]`: per-sector target vs
  current weight (marked to market), drift in **pp**, band-breach flag, cash vs cash target, and — via L3
  [portfolio_beta](../L3_functions/portfolio_beta.md) — per-name and book beta against `target_beta ± band`.

## What this stage does
- Report every sector as **target% · current% · drift pp · band · 🔺OVER / 🔻UNDER / ok**, sorted by |drift|.
  A holding in a sector the mandate never named appears as target 0 → **fully overweight, flagged off-mandate**.
  Nothing is allowed to sit outside the table.
- Report the **cash weight against the cash target**. Cash drift is a mandate breach like any other: a book
  that is 39% cash against a 13% target is not "waiting", it is 26pp off its promise.
- Report **book beta vs the band**, with each position's beta and its contribution. Two books can hold the same
  sector weights at very different betas — sector compliance is not risk compliance.
- ⚠ Marks first, mandate second: if a position failed to mark it is valued at cost and flagged. Weights computed
  on stale marks are stale drift. Say which positions were valued at cost.
- ⚠ Drift is measured, not judged. A breach is a *fact*; whether to trade it belongs to DECIDE — bands exist so
  the book is not churned on every 1pp wobble, and a breach inside a live catalyst window may be worth carrying.

## ✅ EXIT CHECK
- [ ] `DRIFT_REPORT.md` written: every sector's target/current/drift/band + breach count; off-mandate sectors shown.
- [ ] Cash weight compared to the cash target; any position valued at cost (failed mark) named.
- [ ] Book beta (and invested-only beta) stated against the band; names with no beta listed as blanks, not zeros.
