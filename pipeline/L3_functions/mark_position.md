# L3 · mark_position — value one position (function)

> Single deterministic job: quote one name and value the holding. No judgment (P4).

## Run
- Programmatic: `from module_paper_book import get_price, position_pnl`.
  `get_price(ticker)` → current price in native currency (KR 6-digit via `module_KIS.fetch_quote`, US via
  yfinance; failure returns **None** — a blank is a blank, never a guessed price).
- `position_pnl(position, price)` → unrealized (abs + %), stop-distance %, and the ⛔ **stop-hit** boolean.

## Output
`{price, unrealized, unrealized_pct, stop_dist_pct, stop_hit}` for one position.
**bookkeeping aggregates these into the book mark; a None price is surfaced as blank, not zero.**
