# PROTOCOL — wrap_account

> A protocol = an ordered composition of L1 blocks. **Order is owned by this file** — L1 units are
> independent and do not know their sequence. L1s are **referenced only** (content lives in each L1 file).
> Purpose: run the paper book as a **wrap account / discretionary mandate** instead of one undifferentiated
> pile — sector target weights are declared, and the book is managed against them: drift bands, single-name
> and correlated-theme caps, and a portfolio beta band. **Paper only: no real order is ever sent.**
> Output root `llm_outputs/{YYYY-MM-DD}/wrap_account/`. Runtime `--market us|kr|all` (P3 auto-detects by ticker).

## What this desk is (and is NOT)
- **IS:** the *mandate* layer above paper_desk. Where paper_desk asks "is this name worth owning today",
  this desk asks "**does the book still look like what it promised to look like**" — and rebalances toward the
  mandate when a sector, the cash weight, or the beta leaves its band.
- **IS NOT:** a stock picker, and not a live trader. It never invents a name to fill an underweight sector; the
  candidates come from the research desks' `REPORT/` via INTAKE. Fills are simulated; `--commit` writes only the
  *paper* ledger (`data/paper_book.db`). No `--execute`, no broker call, no scheduler auto-fire (P5).
- **Division of labor (P4):** `module_paper_book._allocate` supplies everything with exactly one right answer —
  drift in pp, the amount to move, which **held** name absorbs it (weakest-first on trims, strongest-first on
  adds), the caps. **The judgment — whether a breach is worth trading today, and which new name enters an
  underweight sector — is THIS protocol's DECIDE stage.** The module returns `NEEDS_CANDIDATE` and stops.

## File-output rules
- Run outputs → `llm_outputs/{date}/wrap_account/`: `BOOK_STATE.md` · `MANDATE.md` · `DRIFT_REPORT.md` ·
  `INTAKE_LEDGER.md` · `DECISIONS.md` · `REBALANCE_PLAN.md` · `FILLS.md` · `PAPER_JOURNAL.md`.
  The machine-readable plan also lands in `out/paper_book/WRAP_REBALANCE_{date}.json`.
- The book and the mandate share one store: `data/paper_book.db` (`PAPER_BOOK_DB_PATH` to relocate).
- No secrets in any output. Every weight, beta and amount is module-computed (no eyeballed figures).

## Composition (L1 order)

| # | L1 block | Output |
|---|---|---|
| 1 | [MARK](../L1_stages/mark.md) | `BOOK_STATE.md` (equity · cash sleeves · per-position P&L · stop-hits) |
| 2 | [MANDATE_SET](../L1_stages/mandate_set.md) | `MANDATE.md` (sector targets · band · cash target · beta target) |
| 3 | [DRIFT_CHECK](../L1_stages/drift_check.md) | `DRIFT_REPORT.md` (target vs current pp · breaches · book beta) |
| 4 | [INTAKE](../L1_stages/intake.md) | `INTAKE_LEDGER.md` (candidates per underweight sector, with freshness) |
| 5 | [DECIDE](../L1_stages/decide.md) | `DECISIONS.md` (trade the breach or carry it; which name fills each gap) |
| 6 | [REBALANCE_PLAN](../L1_stages/rebalance_plan.md) | `REBALANCE_PLAN.md` (trims/adds · weights before→after · unfilled) |
| 7 | [SIMULATE](../L1_stages/simulate.md) | `FILLS.md` + updated `paper_book.db` (DRY-RUN unless `--commit`) |
| 8 | [REVIEW](../L1_stages/review.md) | `PAPER_JOURNAL.md` (decision journal + track record + mandate compliance) |

Note the ordering difference from paper_desk: intake comes **after** the drift measurement, not before. The
gaps decide which reports matter — the desk reads the research for the sectors it is actually short of, instead
of shopping the whole ledger and then discovering the book had no room.

## Runtime deltas
- **`--market`**: `us` (yfinance marks, GICS sectors, SPY beta), `kr` (`module_KIS` marks, KRX sectors, `^KS11`
  beta), `all` (both sleeves; the book beta is then a cross-market approximation — say so when quoting it).
- **Bands are the anti-churn device.** Inside the band the book is left alone. `--to target` restores fully;
  `--to band` restores to the edge and accepts residual drift.
- **Discipline carried from the research desks:** a 🔴RESOLVED name may not be used to fill an underweight
  sector — the mandate never overrides the freshness veto. A correlated basket flagged "one risk unit" by the
  premortem is capped as ONE position by `MAX_THEME_PCT`, even when two different sector targets would allow more.
- **The cash sleeve is real.** KRW cash cannot buy a US name; an unfundable add is reported, not assumed.

**Start → read [MARK](../L1_stages/mark.md) and execute.** Advance only after each L1's EXIT CHECK passes.
Finish with [handoff](../handoff.md) to fold the mandate-compliance note into the tag ledger.
