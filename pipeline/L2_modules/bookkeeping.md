# L2 · bookkeeping — the paper ledger (orchestration)

> Called by L1·MARK, SIMULATE, REVIEW. All book state: mark-to-market, fills, snapshots, journal. Single source
> of book truth = `data/paper_book.db` (`module_paper_book._book`). Marks reuse `module_KIS`/yfinance. Composes L3.

## Calls (all `python -X utf8`)
- Mark / status — `python -X utf8 -m module_paper_book status --fx <rate>` (per-position P&L, stop-distance,
  equity) and `mark --fx <rate>` (stop-hits + `concentration_check` theme/single-name caps + equity snapshot).
- Value one position — L3 [mark_position](../L3_functions/mark_position.md) (atomic: quote + unrealized/stop-dist).
- Simulate a fill — `python -X utf8 -m module_paper_book fill --ticker … --side buy|sell --qty … --price …
  [--stop --theme --rationale --source] [--commit]` — **DRY-RUN unless `--commit`** (no real order ever).
- Track record — `python -X utf8 -m module_paper_book snapshot --fx <rate>` (equity-curve point) and
  `track` (return % · max drawdown · win-rate on closed trades) and `journal` (decision log).
- KR cross-read (optional) — `python -X utf8 -m module_KIS --balance` / `fetch_overseas_balance` to sanity-check
  the simulated book against the real KIS book shape (read-only; the paper book is independent).

## Output
Current equity + cash sleeves + per-position P&L + stop-hits + concentration flags; committed/dry-run fills;
equity snapshots + track record. **The calling L1 renders `BOOK_STATE.md` / `FILLS.md` / `PAPER_JOURNAL.md` from it.**
