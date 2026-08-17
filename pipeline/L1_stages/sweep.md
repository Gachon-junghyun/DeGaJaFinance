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

## 🚨 Read the instrument's own health line BEFORE reading its numbers (added 2026-08-10)

`SECTOR_FLOW.json` now opens with a `scoring` block — `n_axes` · `vel_coverage` · `scored` ·
`dropped_missing_axis` — and the sweep logs a 🚨 line when the news axis dies. **Read it first.**

**Why this block exists — four defects measured 2026-08-09/10, all silent:**
1. **The 4th axis was dropped per NAME, not per run.** A name with no news velocity got a 3-axis
   mean; one with velocity got a 4-axis mean — **different scales, then averaged into `wflow`**.
   General form: `3축평균 − 4축평균 = (s₃+3)/12 ∈ [0, +0.5]`, i.e. **dropping is never a penalty and
   is worth up to +0.5**. Measured: **799 of 827 names (96.6%)** carried an average **+0.305** bonus.
2. **`clip(nan)` returned `+1.0`** — `min(1.0, nan)` is `1.0` in Python — so a **missing** axis scored
   the **maximum positive** value. All 20 NaN names printed exactly `flow_score +0.667`.
3. **The KR sweep queried the FOREIGN news pool** — `news_velocity(..., kr=)` was never passed, so
   Korean company names were counted against English wires: 삼성바이오로직스 base **5 articles**,
   LG에너지솔루션 **2** ⇒ velocity `0.00` ⇒ `clip(−2.5) = −1.0` **maximum penalty**, cap-weighted,
   on the largest companies in Korea. **That axis never once fired as a reward.**
4. **The news search rides a tunnel that drops.** Velocity `None` is returned identically for
   *"no articles"* and *"could not reach the index"* — and defect ① turned the second case into a
   **universe-wide score inflation** with nothing in the output saying so.

⇒ **A low `vel_coverage` is not evidence about the news. It is evidence about the pipe.**
Verify before concluding: `python -X utf8 -m module_news_data fts search 삼성전자 --days 7 --count`.

## ★ Invariant: the desk must be able to tag what it holds
Measured 2026-08-10 — the book held **`TSM` and `LNG`**, and **neither was in the sweep universe**.
Both were invisible to every flow/RS/OBV/short axis while being owned; the desk had logged
*"LNG: 어느 축도 데스크 계기로는 존재하지 않는다"* for **9 consecutive runs** without connecting it
to the universe file. ⚠ **Index membership is not a universe** — S&P lists exclude foreign domiciles
(ASML·ARM·TSM·PDD·SHOP) and non-members regardless of size (LNG, the tankers).
`data/us_universe/build_us_universe.py` now builds the union (지수 ∪ 현행 ∪ **보유** ∪ `--include`)
and reports held-but-missing names; this stage reads that report rather than assuming.

## ⚠ Field notes (2026-07-15 run)
- **S1→S2 is SERIAL**: `{us}_live_shortlist` reads *today's* `SECTOR_FLOW.json` by default path —
  running them in parallel feeds it an empty file (JSONDecodeError). Sweep first, then shortlist.
- The sweep is asof the *previous close* — a same-day catalyst (e.g. an overnight oil shock) is NOT
  in the flow numbers yet; note the asof date when cross-checking against the matrix.
- The sweep **cross-checks** macro rotation; it never replaces it (flow = money now, matrix = why).

## ✅ EXIT CHECK
- [ ] 🚨 **`scoring` block read and quoted in `SWEEP_READ.md`** — `n_axes` · `vel_coverage` ·
      `dropped_missing_axis`. If coverage < 80% the file states **"news axis dead this run"** and
      names the likely cause (pipe vs genuinely quiet), having actually probed it — not assumed.
- [ ] **Every sector with `top1_flips_sign` is listed with its `top1` and `top1_w`.** This list is
      handed to ROTATION, which may not promote/demote on those buckets.
- [ ] **Held-but-not-in-universe check run.** If any owned name is outside the universe, that is
      reported as a 🚨 (the desk cannot tag what it owns), not left for a later stage to trip over.
- [ ] sector_flow sweep done → SECTOR_FLOW.json; sector ranking + new-🟢 read.
- [ ] LIVE_SHORTLIST written (real-hands / short-pressure verdicts read).
- [ ] (US) CYCLE_EXPOSURE GAP read; any 🚨 handed to ALPHA's action bracket.
- [ ] **`SWEEP_READ.md` contains no table that exists in the JSONs.** Sector rows and per-name rows
      are cited by artifact, not reprinted.
- [ ] It states at least one cross-check that **confirms or contradicts** the MACRO matrix, and reads
      the shortlist's **absences** (with each absence diagnosed as evidence vs filter artifact).
