# L1 · REVIEW — journal + track record (stage)

> Phase 5. Close the loop: record *why* each action was taken, snapshot the equity curve, and write a portfolio
> review the next run inherits. Calls L2. Output: `PAPER_JOURNAL.md`.

## L2 called
- [bookkeeping](../L2_modules/bookkeeping.md) — `module_paper_book snapshot` (equity snapshot → track-record curve)
  · `module_paper_book journal` / `track` (decision log + return/MDD/win-rate).

## What this stage does
- Write `PAPER_JOURNAL.md`: for each action this run, the **thesis, freshness, conviction, and the flip-condition**
  (what would reverse it) — append-only, so a wrong call stays visible next to its outcome (the self-backtest's food,
  same discipline as the research desks' §5).
- **Snapshot equity** (`snapshot`) so the track record (return %, max drawdown, win-rate on closed trades) advances
  one point. State the current book as a short review: top exposures, the live "one risk unit," what the book is
  waiting on (which catalysts from the reports), and what would force a de-risk.
- **Handoff:** run [handoff](../handoff.md) so the paper journal folds into the tag ledger — the research desks can
  see "the paper book already acted on GEV/RTX with verdict X," closing the read→act→review loop.

## ✅ EXIT CHECK
- [ ] `PAPER_JOURNAL.md` written (append-only): each action's thesis + conviction + flip-condition.
- [ ] Equity snapshot taken; track record (return/MDD/win-rate) updated.
- [ ] Portfolio review stated (exposures · one-risk-unit · what it's waiting on); handoff ledger updated.
