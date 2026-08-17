# pipeline — call hierarchy + protocol composition

> **Call direction**: `protocol` = an ordered composition of L1 blocks. `L1` (big stage) → `L2`
> (module orchestration) → `L3` (single-role function) — each layer **calls downward only**.
> The full prompt-inventory map is [`PROMPT_MAP.md`](PROMPT_MAP.md); modules live in [`../MODULE_MAP.md`](../MODULE_MAP.md).

```
protocols/     protocol = ordered combination of L1 blocks (industry_us = MACRO→SWEEP→…→DRIFT)
    │  calls (composes)
    ▼
L1_stages/     big stages = reusable stage blocks (MACRO·SWEEP·DEEP·BET…). Each calls L2.
    │  calls
    ▼
L2_modules/    module orchestration (indicators·schedule·discovery·deepdive·news). Composes L3/modules.
    │  calls
    ▼
L3_functions/  single-role functions (atomic steps: random news sample·body drill·related companies·competitors). One deterministic job each.
```

## Core properties
- **Only the protocol owns ORDER.** L1/L2/L3 units are all **independent** — no unit knows what
  comes after it (no chaining inside units). Which units run, and in what order, is decided solely
  by `protocols/`. Units are reused; order is composed.
- **L1s are Lego blocks.** One MACRO stage is **shared** by industry_us and industry_kr. A protocol
  is defined by *which blocks in which order* (reference, never copy-paste).
- **Calls go one way (top→down).** protocol→L1→L2→L3. Never up, never sideways.
- **Runtime deltas are absorbed inside L1.** The same MACRO L1 splits KR/US via `--market kr|us`.
  Protocols differ only in which L1s they include (e.g., only US adds PREMORTEM·DRIFT).
- ★ **Cite upstream artifacts; never re-print them.** Every prior stage's output stays on disk for the
  whole run. A stage writes **only what it adds** — the delta, the reading, the resolution. Restating
  an upstream table is P1 duplication that costs tokens twice (writing it, then re-reading it) and
  hides the stage's real yield.
  **Measured 2026-07-21 (industry_US)**: `SECTOR_ROTATION.md` reproduced MACRO's transmission matrix
  on **8 of 9 comparable sectors** — 14KB whose true output was 2 verdict changes. `SWEEP_READ.md`
  restated **100% of its tickers and 97% of its numbers** from `SECTOR_FLOW_US.json`, in a file
  **nothing downstream reads**. Both are now delta/interpretation-only by spec.
  **Self-test for any stage**: if you removed every sentence whose content exists upstream, what
  remains? That remainder is the stage's yield — and it should be most of the file.
  ⚠ Not every high-overlap stage is waste: PREMORTEM re-covers the same names **on purpose**, in the
  opposite direction (it reversed three of its own desk's calls on 2026-07-21), and DEEP's chain-hop
  surfaced 10 names the sweep universe structurally cannot see. Overlap is a **prompt to check
  yield**, not a verdict.

## Folder per layer
| Layer | Folder | What | Example |
|---|---|---|---|
| protocol | `protocols/` | L1 composition = a desk flow | `industry_us.md` = [MACRO,SWEEP,ROTATION,PREMORTEM,DEEP,BET,ALPHA,DRIFT] |
| L1 | `L1_stages/` | big stages | `macro.md`·`sweep.md`·`deep.md`·`bet.md`… |
| L2 | `L2_modules/` | module orchestration | `indicators.md`·`schedule.md`·`discovery.md`·`deepdive.md`·`news.md` |
| L3 | `L3_functions/` | single-role functions | `daily_events.md`·`random_news.md`·`drill_detail.md`·`related_companies.md`·`competitors.md` |
| — | `handoff.md` | REPORT handoff ledger (prevents re-searching; crosses layers) | `module_report_tags` |
| — | [`../handoff/`](../handoff/README.md) | **the analytical carry** — standing view · pre-registered scenarios · research rules. Read/written by L1·HANDOVER | `STANDING_VIEW.md`·`SCENARIOS.md`·`RESEARCH.md` |

⚠ **`pipeline/handoff.md` and `../handoff/` are different objects.** The first is the *mechanical*
ledger (which report covered which ticker). The second is the *analytical* carry (what we believe,
what we pre-committed to, what we retracted). A run needs both: coverage without belief re-derives
yesterday's view; belief without coverage re-searches what is already on disk.

## Compiling a composition
`build_protocol.py` follows a protocol's L1 links in order and **merges L1→L2→L3 into one file**.
```bash
python pipeline/build_protocol.py industry_us industry_kr   # → protocols/_compiled/{name}.md
python pipeline/build_protocol.py --all
```
- Output `protocols/_compiled/{name}.md` = the complete executable protocol (composition recipe + ordered L1 blocks + L2/L3 appendix).
- Each L1 is defined ONCE → protocols reuse it with different orderings (DRY). Never edit compiled output; fix the source and recompile.
- ⚠ **Ordering rule**: the compiler orders L1 by *first link appearance*. Keep stage links **only in the
  composition table** — name stages as plain text in prose, or the run order scrambles.

## Running a composition stage-by-stage (context-loss guard)
`run_protocol.py` feeds **one L1 stage at a time** (that L1 + only the L2/L3 it calls) instead of the
whole monolith — so a long protocol's early context (datapack) isn't diluted by the time you reach the verdict.
```bash
python pipeline/run_protocol.py real_alpha_kr --start --target 009150   # print stage 1 only
python pipeline/run_protocol.py real_alpha_kr --next     # pass current EXIT CHECK → print next stage
python pipeline/run_protocol.py real_alpha_kr --status   # progress table (✅passed / ▶current / ·pending)
python pipeline/run_protocol.py real_alpha_kr --goto 4   # jump
```
Checkpoint at `out/pipeline_runs/{name}.json` (stage · passed · target). Do a stage → pass its EXIT CHECK →
`--next`. Prior stages' outputs live on disk — reread the run dir, not memory.

## Current contents
- **HANDOVER (stage 0)**: every desk protocol now opens with [HANDOVER](L1_stages/handover.md), which
  inherits [`../handoff/`](../handoff/README.md) before MACRO runs — standing view, retracted ledger,
  armed scenarios, and the binding research rules. It also **scores every past-dated scenario** (L3
  `scenario_score`); an unscored matured scenario is logged as a process failure, not skipped. Born
  from a measured 2026-07-22 session in which **six judgments were reversed inside one session**, each
  re-discoverable from material a prior run already had — the failures were carry failures, not data
  failures. The rules it loads are enforced downstream (MACRO citation discipline · DEEP cyclical
  lens + peak-margin check · PREMORTEM branch grading · L2 indicators venue-contamination check).
- **protocols/**: `industry_us.md` (10 blocks) · `industry_kr.md` (8 blocks) · `paper_desk.md` (6 blocks) ·
  `wrap_account.md` (8 blocks) · `미러링.md` (7 blocks) · `real_alpha_kr.md` (8 blocks) ·
  `idle_probe.md` (7 blocks) · **`preflight.md` (2 blocks)** — complete, compile-verified.
  Only US adds premortem·drift.
  ★ **`preflight` runs BEFORE HANDOVER in any desk run.** It is a few-minute mechanical gate check
  whose output is not a report but a **claim-permission table**: a failed gate removes a citation
  right for that run (dead news axis ⇒ no theme-freshness claim; a sign-flipping sector bucket ⇒ no
  promotion off it). Born from 2026-08-09/10, where **12 instrument defects were found in one day and
  none of them threw** — every one returned a plausible number, and one silently inflated **every**
  flow score by **+0.305**. `idle_probe` *finds* such defects (slow, exploratory); `preflight`
  *prevents their return* (fast, boring). Keeping them separate is deliberate — a heavy daily check
  stops being run, which is the exact failure `measure_ic` demonstrated (0 invocations in 3 weeks).
  `paper_desk` is the *downstream* desk — it consumes the research desks' `REPORT/` output and runs a simulated book
  (engine = `module_paper_book`; paper only, no real order). `미러링` mirrors the **real KIS account** into that book,
  applies judgment, and stages recommendations onto the real KIS order desk stack as **human-fireable intent cards**
  (no execution; not advice). `real_alpha_kr` is the **forensic desk** — one company, "is it REAL?" → 4-tier verdict
  (REAL / REAL-but-PRICED / INFLATED / BROKEN) + dated observation points + ledger; **참고-only, READ-ONLY, not advice**
  (port of the mvp `REAL_ALPHA_COMPANY_RESEARCH_KR.md`, reusing our modules). The remaining desks (company·strategy)
  have their L1 decomposition in [PROMPT_MAP](PROMPT_MAP.md) — build the L1 blocks and compose.
  `wrap_account` is the **mandate layer above paper_desk**: sector target weights are declared and the same book
  is managed against them (drift bands · single-name/theme caps · portfolio beta band). It reuses 5 of
  paper_desk's L1s (mark·intake·decide·simulate·review) and reorders them — drift is measured *before* intake,
  so the desk reads research only for the sectors it is short of. Engine = `module_paper_book._allocate`;
  the module returns `NEEDS_CANDIDATE` instead of ever picking a name (P4). Paper only, `--commit` human-gated.
- **L1_stages/**: **handover** (stage 0, all desks) + the 9 industry blocks
  (macro·sweep·event_alpha·rotation·premortem·deep·bet·alpha·drift) + pulse ·
  mirror_ingest · stage_orders (미러링) + **forensic_pack · self_score · chain_alpha · money_forensic · set_diff ·
  falsify · verdict** (real_alpha_kr) + **mandate_set · drift_check · rebalance_plan** (wrap_account)
  + **census · pair · probe · control · adjudicate** (idle_probe)
  + **instrument_check** (preflight; reuses census).
- **L3 `reject_ledger`** (2026-07-23) — the desk's rejections become a scored asset. Every
  DROP/PASS/강등 is appended with a reason class and a **`--revives-if`** condition, then scored by
  class and by **type** (`measured` / `structural` / `narrative`) against the equal-weight 1조+
  universe. Called by L2 [carryover](L2_modules/carryover.md); written by L1 bet · alpha · decide ·
  event_alpha. First observation (n=24): **67% of rejections changed nothing** and the loss tail ran
  **2.2×** the gain tail — the unit exists to make that ratio visible and improvable, not to rule.
- **protocol `morning_brief`** (2026-07-23) — the second *publication* desk (paper_desk consumes the
  research to trade; this one consumes it to **publish**). Three blocks — gather → rank → render —
  emitting one phone-readable `MORNING_BRIEF.md` at 08:30 KST, pre-open. Two rules carry it, both
  born from a measured draft failure the same day: **(a)** an 08:30 brief cannot quote a mid-session
  number (the draft cited a 10:20 KST flow pull that did not exist at 08:30), and **(b)** our
  filenames are not sources — four of the draft's eight `출처:` lines pointed at `MACRO_REPORT §1`,
  `EVENT_ALPHA Card 1`, `module_flow`, `SCENARIOS S8-C`, each of which had a real public origin
  (한국은행 · USTR · 거래소 · 외신) the draft walked past. An unresolvable citation is worse than
  none: it still reads as authority. New L3 [public_source](L3_functions/public_source.md) holds the
  substitution table and the ban list; **zero new L2** — it reuses report_read · news · schedule ·
  bookkeeping as they are.
- **Scoreboard, third leg — `exposure_rule` + `missed_ledger`** (2026-07-31). The desk could already
  score what it *rejected* (L3 reject_ledger). It could not score **what it did not buy**, and it had
  never scored **its own cash weight** — which turned out to be the variable that actually moves the
  number. Measured that day: of a **+16.86pp** lead over the benchmark, roughly **14pp was cash
  weight**, and stock selection contributed **+2.54pp with one name (삼성물산 +0.89pp) carrying it** —
  n=11 over one window, i.e. indistinguishable from zero (C4). The next session the same cash weight
  gave back **−12.5pp in a day**. Same variable, opposite sign, no gate in between: the desk had
  "reduce risk" triggers and **no "restore risk" trigger** (F1 — the 🟢LIVE tag fired 0 times in 8
  consecutive runs because it required a FRESH theme age that the board structurally could not have).
  ⇒ `scripts/exposure_rule.py` makes the exposure decision an **explicit, dated, scored** one: four
  states (정상/방어/**복귀**/과열) against `069500.KS`, one ledger row per day, and a daily attribution
  that closes as an identity (`총초과 = (w−1)×벤치 + 잔차`). **The load-bearing half is 복귀** — it does
  not predict the bottom, it fires only on *evidence of a turn*, so a missed rebound becomes a lag of
  a few pp instead of a total loss. Its thresholds are **human-set** (`data/exposure_bands.json`);
  absent that file the tool refuses to render a verdict and logs `밴드미설정 🚨`. `scripts/missed_ledger.py`
  is reject_ledger's mirror with the sign flipped. **Why this layer and not more prediction**: exposure
  yields one independent observation per session (n≈20 in a month), while stock selection yields
  10–20 per *year* — it is the only place in this repo where significance is arithmetically reachable.
  **Wiring** (the tools are not the point; being *called without anyone remembering* is): new L3
  [missed_ledger](L3_functions/missed_ledger.md) + L3 [exposure_state](L3_functions/exposure_state.md),
  both invoked by L2 [carryover](L2_modules/carryover.md) §3c/§3d, so **every desk's HANDOVER** runs
  `missed_ledger due` beside `reject_ledger due` and carries the exposure verdict as size context.
  L1 bet · alpha · event_alpha now write missed entries the way they already wrote rejections; L1
  leak_audit is the ledger's **supply line** (its B/C/D buckets become rows — previously `leak_scan`
  recomputed the same leak every audit and accumulated nothing). ⚠ Zero new L2 — carryover absorbed
  both, which is the test that these were functions and not stages.
- **L1 `leak_audit`** (2026-07-23) — the counterpart to §5 self-backtest: it scores what the desk did **not** do. Runs against a *past* run (≥3 sessions later), pairs `scripts/leak_scan.py` with L3 reject_ledger, and classifies every mover into A.런에있었음 / B.커버리지소실 / C.스쳐감 / D.발굴부재. Two guards are load-bearing: **forward-test only** (OBV is price×volume, so trailing scoring is tautological — measured: trailing said 매집 +42.2%, forward said it lost) and **label the window's regime** (measured: in the 07-20 bounce 🔴분산 +8.22% beat 🟢가속 +7.77%; in the 07-16 window 🟢 beat the universe 11×). First result: **B.커버리지소실 was the worst leak (+1.93pp, n=26) while D.발굴부재 UNDERPERFORMED (−0.70pp, n=89)** — discovery is not the leak, retention is.
  ⚠ **RETRACTED 2026-07-31 — that ordering does not reproduce, and it was quoted as settled for a week.**
  Re-scoring **the same 07-20 window** today (i.e. only the measurement horizon extended, through the
  07-28~30 crash and the 07-31 rebound) inverts it completely: **D.발굴부재 +2.58pp · C.스쳐감 +2.56 ·
  A.런에있었음 −0.31 · B.커버리지소실 −4.68pp** — B goes from *worst* to *best*. The 07-24 window scores
  the same way (D +3.57 · C +2.35 · A −0.73 · B −4.90), so the ordering is stable **across windows** and
  unstable **across horizons**. ⚠ The n's also disagree (26 vs 51, 89 vs 48), so the two runs were not
  like-for-like to begin with — which is the second half of the defect: the original figure was recorded
  without the parameters needed to reproduce it. ⇒ **"retention, not discovery" is withdrawn as a
  standing claim.** A single-window, single-horizon class mean is an observation, not a finding, and
  must not be cited as a reason to change the protocol (it was — see `industry_kr.md` DEEP budget,
  now corrected).
- **L2/L3**: orchestration + atomic functions, reused across L1s. handover added L2 `carryover`
  (reads the carry + reconciles it against the mechanical ledger — a belief with no coverage gets
  demoted, coverage with no belief becomes a DEEP candidate) + L3 `scenario_score` (one scenario →
  one branch verdict, against the **frozen** threshold; `EXPIRED` is logged, never dropped).
  wrap_account added L2 `mandate` + L3
  `portfolio_beta` (regression beta vs `^KS11`/`SPY`) — everything else it needs (bookkeeping · risk_model ·
  report_read · mark_position · size_from_risk) was already there. real_alpha added L2 `money_trail` +
  L3 `accruals_check · filing_diff · set_difference · contract_alpha`. event_alpha added L2
  `narrative_money` (trajectory × money-flow cross; **all its L3s are reused** — event_threads ·
  drill_detail · related_companies · competitors — zero new atoms, which is the point).
- **News has two axes** (L2 `news`): the **term** axis (`blindspot`·`fts`·`chain-hop` — "is my theme
  hot?") and the **event** axis — which itself has two time-shapes: the **snapshot** (L3
  `daily_events` → `brief`, "what happened today, all of it") and the **trajectory** (L3
  `event_threads` → `thread --days 7`, "how is each event moving across the week" —
  BUILDING/FADING/REIGNITED/ENDED with per-day outlet curves). Term vs event are not substitutes:
  on the measured KOSPI −8% circuit-breaker day the term `코스피` ran at 1.3× normal and ranked
  nowhere, while the event view had it at [39 articles/8 outlets]. A term spikes when it is *new*;
  an event ranks when it is *big*. Snapshot vs trajectory are not substitutes either: the BOK
  rate-hike saga was a 2-outlet tail item 5 days before the hike — invisible in any one day's
  brief, obvious as a climbing curve (`2→7→6→7→5→8`). ⚠ The event axis is **client-only**
  (GPU embeddings, CLAUDE.md P6) — the collection server cannot run it.
  ⚠ **The snapshot's coverage is now a measured number, not a claim** (2026-07-23). 20% of a day's
  articles drawn at random and traced back into the brief: **45.6% appeared nowhere**, with the tail
  already emptied by `--body 2`. The leak was never the tail — it was 1-outlet clusters (35% of the
  day, holding that day's FX/rates prints), the non-market bucket's unshown remainder (a `[:5]` cut
  that structurally showed the *most certain* non-market items and hid every borderline one — the
  Iran strike-planning event went that way while the head carried the oil move it caused), and topic
  blobs (a 44-article US-tariff event had swallowed a domestic anti-dumping ruling). Now three
  reported sections — `single_source` · `excluded_nonmarket.band` · `subevents` — at **64.6% recall
  for +6.2k tokens**, with everything still withheld carried as a count. Re-measure any day with
  `scripts/brief_recall.py`; the L1 EXIT CHECK now requires quoting those counts, because
  `tail = 0` was never the coverage claim it looked like.
- **Language rule**: every unit here is written in **English** — the US desk runs English-pure
  (Korean in context skews the frame), and the KR desk reads English instructions while emitting
  KR-market outputs. Field-tested run notes are embedded per unit as ⚠ notes.
