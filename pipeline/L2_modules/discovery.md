# L2 · discovery — discovery/sweep (orchestration)

> Called by L1s. Sweeps the universe wide so candidates surface from data breadth,
> not from the names you already knew.

## Calls
- Sector-rotation quant sweep — `python -X utf8 scripts/sector_flow.py --market us|kr --json`
  (mcap-weighted GICS flow_score across the universe; read **wflow vs eqflow** — high wflow with
  weak eqflow = mega-cap-narrow concentration tell — and **new-🟢** day-over-day ignitions;
  stdout=data, stderr=logs; rebuild the universe CSV weekly if the sweep warns >8d stale).
  🚨 **Read `json.scoring` before `json.sector_rotation`** (added 2026-08-10):
  `n_axes` · `vel_coverage` · `dropped_missing_axis`. **Scores from different `n_axes` are not the
  same scale and must not be compared or differenced** — the snapshot `_mode` guard now derives from
  the *realized* axis count rather than the `--no-news` flag, because the news axis dies on its own.
  ⚠ `vel_coverage` low ⇒ **the pipe, not the news**. Probe it (`fts search … --count`) before saying
  "quiet". The four defects behind this block are documented in L1 [sweep](../L1_stages/sweep.md).
  🚨 **And read `sector_rotation[].top1_flips_sign`** — 10 of 26 KR sectors flip sign when their
  largest name is removed. ROTATION may not promote/demote on those.
- LIVE shortlist — `python -X utf8 scripts/us_live_shortlist.py --floor-b 10 --top 15` /
  `kr_live_shortlist.py` (KR = foreign/institution actuals; US = FINRA short-z proxy).
  ⚠ **SERIAL dependency: the shortlist reads TODAY's SECTOR_FLOW json by default path — run the
  sweep to completion first** (parallel launch feeds it an empty file → JSONDecodeError).
- (US) setup screener — `python -X utf8 scripts/us_setup_screener.py --sector <GICS>`.
- (US) cycle-exposure GAP — `python -X utf8 scripts/cycle_exposure.py --json`
  (registry vs REAL book; 🚨 GAP when a rank≤2 cycle's epicenter < min%).
- Emergent-theme discovery — L3 [random_news](../L3_functions/random_news.md).
- Universe rebuild (weekly, **not a desk run**) — `python -X utf8 data/us_universe/build_us_universe.py`
  / `data/kr_universe/build_kr_universe.py`. Both write a **candidate** file; promotion is a human step
  because the universe is the **denominator of every sweep, sector aggregate and ledger benchmark**.
  ⚠ **An index list is not a universe** — S&P excludes foreign domiciles (ASML·ARM·TSM·PDD·SHOP) and
  non-members regardless of size (LNG, tankers). The US builder therefore takes the **union** of
  index ∪ current ∪ **book holdings** ∪ `--include`, and reports any held name missing from it.
  ⚠ Widening the universe does **not** widen text detection: `module_news_data._config.US_TEXT_TOP_N`
  caps the ticker-detection view (measured — S&P 1500 adds 1,201 short tickers, ≥26 of them spelled
  like ordinary English words: CASH·FORM·POST·TECH·UNIT·WAY…).

## Output
Candidate list (+ LIVE real-hands/short-pressure tags) + any cycle GAP.
**The calling L1 hands them to DEEP/BET; GAP goes to the action bracket.**
