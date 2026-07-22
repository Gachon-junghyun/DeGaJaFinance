# L1 · SWEEP — opening sweep (stage)

> Phase 0.5. BEFORE rotation, quantify "where the money actually flows" across the whole universe
> (anti-tunnel — orient from flow, then name things). Calls L2.
> Output: `SECTOR_FLOW.json` · `{US|KR}_LIVE_SHORTLIST.json` · (US) `CYCLE_EXPOSURE.md`
> · `SWEEP_READ.md` (**the reading — interpretation only, see the size discipline below**).

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

## ★ `SWEEP_READ.md` — the reading, not a second copy of the data

The JSONs above hold the numbers and stay on disk all run. **This file holds only what the JSON
cannot say.** It was previously an undeclared artifact and drifted into restatement — measured
2026-07-21: **100% of its tickers and 97% of its numbers already existed in
`SECTOR_FLOW_US.json`**, in a file nothing downstream reads.

**Forbidden** — reprinting any table the JSON already holds: the 11-sector ranking rows, the
per-name shortlist rows. Cite the artifact (`SECTOR_FLOW_US.json §sector_rotation`) instead.

**Required** — the three things the JSON genuinely cannot express:
1. **Universe headline, 3 numbers**: n · wflow · 🟢/🔴 count. One line.
2. **Cross-checks that CONFIRM or CONTRADICT the MACRO matrix** — this is the file's reason to exist,
   and it is ROTATION's direct input. State the contradiction and which side the money is on.
   *Good examples, measured*: "eqflow > wflow ⇒ breadth-led, not mega-cap-narrow" · "Staples inverted:
   breadth positive, mega-caps negative — first life in 5 runs" · "IT 0 green of 56 = worst breadth
   on the board".
3. **Shortlist composition — read the ABSENCES.** Which sectors produced *no* shortlist name is
   usually the finding; the names themselves are already in the JSON.
   *Measured*: an ENRG shortlist of 0 turned out to be a 🟢-tag filter artifact, not evidence — the
   refiners were OBV-accumulating but tagged 🟡. Absences must be diagnosed before they are cited.

**Size discipline** — this is a reading, not a report. If it is longer than the deltas it found,
it is restating. ⚠ It is **not** load-bearing (nothing globs it); it exists to feed ROTATION §2.

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
- [ ] **`SWEEP_READ.md` contains no table that exists in the JSONs.** Sector rows and per-name rows
      are cited by artifact, not reprinted.
- [ ] It states at least one cross-check that **confirms or contradicts** the MACRO matrix, and reads
      the shortlist's **absences** (with each absence diagnosed as evidence vs filter artifact).
