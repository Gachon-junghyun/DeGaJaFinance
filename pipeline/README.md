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
  `wrap_account.md` (8 blocks) · `미러링.md` (7 blocks) · `real_alpha_kr.md` (8 blocks) — complete,
  compile-verified. Only US adds premortem·drift.
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
  falsify · verdict** (real_alpha_kr) + **mandate_set · drift_check · rebalance_plan** (wrap_account).
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
- **Language rule**: every unit here is written in **English** — the US desk runs English-pure
  (Korean in context skews the frame), and the KR desk reads English instructions while emitting
  KR-market outputs. Field-tested run notes are embedded per unit as ⚠ notes.
