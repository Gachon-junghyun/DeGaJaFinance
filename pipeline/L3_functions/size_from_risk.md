# L3 · size_from_risk — one position's share count (function)

> Single deterministic job: given price, stop, and equity, return the risk-allowed share count. No judgment (P4).

## Run
- Programmatic: `from module_paper_book import size_position, RiskParams`.
  `size_position(equity, price, stop, is_core, params)` →
  `risk_amount = equity × risk% ÷ 100` (core-risk% if `is_core`); `per_share_risk = price − stop`
  (or `price × stop%` if no stop); `qty = floor(risk_amount ÷ per_share_risk)`, capped by max-position %.
- CLI: `python -X utf8 -m module_paper_book size <ticker> --price P [--stop S] [--core]`.

## Output
`{qty, stop, per_share_risk, risk_amount, notional, binding_constraint}` for one name.
**SIZE (via risk_model) uses it per ENTER/ADD; the binding_constraint says whether risk or the position-cap set the size.**
