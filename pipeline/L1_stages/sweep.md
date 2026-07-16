# L1 · SWEEP — opening sweep (stage)

> Phase 0.5. BEFORE rotation, quantify "where the money actually flows" across the whole universe
> (anti-tunnel — orient from flow, then name things). Calls L2.
> Output: `SECTOR_FLOW.json` · `{US|KR}_LIVE_SHORTLIST.json` · (US) `CYCLE_EXPOSURE.md`.

## L2 called
- [discovery](../L2_modules/discovery.md) — `sector_flow --market us|kr --json`, then
  `{us|kr}_live_shortlist`, (US) `cycle_exposure --json`.

## What this stage does
- Universe-wide flow quantification (us_top300 / kr_all) → per-sector **wflow** (mega-cap-led) vs
  **eqflow** (breadth) + **new-🟢** ignitions (day-over-day flow ignition = early-cycle tell).
- LIVE shortlist: mcap floor + 🟢 tag filter → per-name enrichment.
  KR: real-hands tagging (foreign/institution actuals via KIS). US: FINRA short-z proxy —
  ✅ low-short/short-cover (clean rise) · ⚡ crowded-short (turn-conditional squeeze fuel, NOT a buy) · △ normal.
- (US) cycle-exposure GAP: dominant-cycle registry vs the REAL book → 🚨 GAP when a rank≤2 cycle's
  epicenter exposure < min%. A 🔴 tape gates ADD *timing* — it never justifies zero core in a top cycle.

## ⚠ Field notes (2026-07-15 run)
- **S1→S2 is SERIAL**: `{us}_live_shortlist` reads *today's* `SECTOR_FLOW.json` by default path —
  running them in parallel feeds it an empty file (JSONDecodeError). Sweep first, then shortlist.
- The sweep is asof the *previous close* — a same-day catalyst (e.g. an overnight oil shock) is NOT
  in the flow numbers yet; note the asof date when cross-checking against the matrix.
- The sweep **cross-checks** macro rotation; it never replaces it (flow = money now, matrix = why).

## ✅ EXIT CHECK
- [ ] sector_flow sweep done → SECTOR_FLOW.json; sector ranking + new-🟢 read.
- [ ] LIVE_SHORTLIST written (real-hands / short-pressure verdicts read).
- [ ] (US) CYCLE_EXPOSURE GAP read; any 🚨 handed to ALPHA's action bracket.
