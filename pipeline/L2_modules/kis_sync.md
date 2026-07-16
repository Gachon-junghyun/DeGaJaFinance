# L2 · kis_sync — real KIS book ↔ paper ↔ order stack (orchestration)

> Called by L1·MIRROR_INGEST and STAGE_ORDERS. Three-way sync between the **real KIS account**, the
> **paper book**, and the **KIS order desk stack** — plus the epistemics feedback. Reuses
> `module_order_desk.stack` (order intents) and `module_epistemics` (learned sensitivities); never re-implements them.

## Calls (all `python -X utf8`)
- **Ingest real → paper** — `python -X utf8 -m module_paper_book mirror --from-json <holdings.json> --fx <r>`
  (holdings from live `module_KIS.fetch_overseas_balance`/`fetch_balance`, or, if KIS creds are absent, from the
  account screenshot — derive share counts as `market_value ÷ fx ÷ price`, avg-cost as `price ÷ (1+pnl%)`).
  Seeds positions as **already-held** (no cash effect) and sets the real cash sleeves. US-limited by default.
- **Stage paper → order desk** — `python -X utf8 -m module_paper_book stage --from-json <intents.json> [--clear]`
  → writes `out/order_desk/kis_stack.json` (`module_order_desk.stack` intents `{market,side,code,qty,price,note}`).
  **Intents only — the desk shows dry-run cards; a human fires each with [체결]. No order is ever sent here (P5).**
- **Epistemics feedback** — `learned_sensitivity(ticker)` reads `epistemics/sensitivity/{ticker}.json` (learned
  factor elasticities/confidence) as a DECIDE prior; `record_sensitivity(ticker, factor, dir, event, conf)` writes
  today's judgment basis back (`python -X utf8 -m module_epistemics sensitivity <tkr> --add <factor> --dir +강 --conf 0.8`).
  The vault accumulates at `epistemics/sensitivity/` — consult it before deciding, feed it after a catalyst fires.

## Output
A paper book synced to the real holdings; an order-desk stack loaded with human-fireable intent cards; an
epistemics ledger richer by today's factors. **MIRROR_INGEST/STAGE_ORDERS render their reports from it.**
