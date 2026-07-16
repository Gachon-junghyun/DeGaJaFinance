# L2 · discovery — discovery/sweep (orchestration)

> Called by L1s. Sweeps the universe wide so candidates surface from data breadth,
> not from the names you already knew.

## Calls
- Sector-rotation quant sweep — `python -X utf8 scripts/sector_flow.py --market us|kr --json`
  (mcap-weighted GICS flow_score across the universe; read **wflow vs eqflow** — high wflow with
  weak eqflow = mega-cap-narrow concentration tell — and **new-🟢** day-over-day ignitions;
  stdout=data, stderr=logs; rebuild the universe CSV weekly if the sweep warns >8d stale).
- LIVE shortlist — `python -X utf8 scripts/us_live_shortlist.py --floor-b 10 --top 15` /
  `kr_live_shortlist.py` (KR = foreign/institution actuals; US = FINRA short-z proxy).
  ⚠ **SERIAL dependency: the shortlist reads TODAY's SECTOR_FLOW json by default path — run the
  sweep to completion first** (parallel launch feeds it an empty file → JSONDecodeError).
- (US) setup screener — `python -X utf8 scripts/us_setup_screener.py --sector <GICS>`.
- (US) cycle-exposure GAP — `python -X utf8 scripts/cycle_exposure.py --json`
  (registry vs REAL book; 🚨 GAP when a rank≤2 cycle's epicenter < min%).
- Emergent-theme discovery — L3 [random_news](../L3_functions/random_news.md).

## Output
Candidate list (+ LIVE real-hands/short-pressure tags) + any cycle GAP.
**The calling L1 hands them to DEEP/BET; GAP goes to the action bracket.**
