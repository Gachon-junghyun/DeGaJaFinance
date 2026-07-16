# L1 · SIMULATE — simulate the fills (stage)

> Phase 4. Book the sized orders into the **paper** ledger. DRY-RUN by default; a human adds `--commit` to
> persist the simulation (there is no real order — `--commit` writes only `paper_book.db`). Calls L2.
> Output: `FILLS.md` + updated `paper_book.db`.

## L2 called
- [bookkeeping](../L2_modules/bookkeeping.md) — `module_paper_book fill --ticker … --side … --qty … --price …
  [--stop --theme --rationale --source] [--commit]`: preview without `--commit`, persist with it (cash sleeve,
  weighted-avg cost, realized P&L on sells, transaction ledger, decision journal all update atomically).

## What this stage does
- Simulate each order at the **current mark** (not the report's stale price) — the fill price is today's quote.
- **Default DRY-RUN:** print the preview (side, qty, notional, resulting cash) and log the intent to the journal
  as un-committed. Persist to the book **only** when a human passes `--commit` (the paper analogue of the
  `--execute` human gate — the desk never auto-fires).
- EXITs (sells) realize P&L against the weighted-avg cost; ENTER/ADD update the average. Carry the DECIDE
  rationale + source report into each fill so the journal stays auditable.
- ⚠ This is a simulation for learning/track-record. It is NOT a live order and must never be described as one.

## ✅ EXIT CHECK
- [ ] Each order simulated at the current mark; previews shown.
- [ ] Book mutated ONLY under `--commit`; otherwise dry-run intents journaled un-committed.
- [ ] Sells realized P&L vs avg cost; each fill carries rationale + source report.
