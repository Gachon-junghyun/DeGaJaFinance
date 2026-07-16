# L1 · MARK — mark the book to market (stage)

> Phase 1. Before deciding anything, know exactly where the book stands. Calls L2.
> Output: `BOOK_STATE.md`.

## L2 called
- [bookkeeping](../L2_modules/bookkeeping.md) — `module_paper_book status` / `mark`: value every open position
  (`module_KIS` for KR, yfinance for US), compute equity, cash sleeves, per-position P&L, stop-distance.

## What this stage does
- Mark every open position to the current price → **unrealized P&L %, stop-distance %, ⛔ stop-hit flags.**
  A stop-hit is a hard fact handed to DECIDE (it forces an EXIT verdict, not a discretionary one).
- Report the **cash sleeves** (KRW + USD) and **total equity** (KRW-translated at `--fx`) — this equity is the
  denominator SIZE will use, so it must be current.
- Compute **theme (correlation-unit) exposure** and run the **concentration check** (single-name > max-pos%,
  theme > max-theme%) — the premortem "one risk unit" guard surfaces here as a live number, not a memory.
- ⚠ Marks can be stale/NaN if a data source hiccups (see the yfinance bulk-fetch RS-NaN lesson) — state any
  missing mark as a blank, never a guess; a missing mark ≠ a zero position.

## ✅ EXIT CHECK
- [ ] `BOOK_STATE.md` written: equity, cash sleeves, per-position P&L, stop-distances.
- [ ] Stop-hits flagged (→ DECIDE must EXIT them); concentration flags surfaced.
- [ ] Any missing/failed mark stated as blank (not zero, not guessed).
