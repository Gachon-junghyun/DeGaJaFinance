# pipeline — call hierarchy + protocol composition

> **Call direction**: `protocol` = an ordered composition of L1 blocks. `L1` (big stage) → `L2`
> (module orchestration) → `L3` (single-role function) — each layer **calls downward only**.
> The full prompt-inventory map is [`PROMPT_MAP.md`](PROMPT_MAP.md); modules live in [`../MODULE_MAP.md`](../MODULE_MAP.md).

```
protocols/     protocol = ordered combination of L1 blocks (industry_us = HANDOVER→MACRO→…→BET→ALPHA)
    │  calls (composes)
    ▼
L1_stages/     big stages = reusable stage blocks (MACRO·EARNINGS·COMPETITION·BET…). Each calls L2.
    │  calls
    ▼
L2_modules/    module orchestration (indicators·schedule·discovery·deepdive·news·web_errand). Composes L3/modules.
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
  Protocols differ only in which L1s they include (e.g., only US adds PREMORTEM).
- ★ **Cite upstream artifacts; never re-print them.** Every prior stage's output stays on disk for the
  whole run. A stage writes **only what it adds** — the delta, the reading, the resolution. Restating
  an upstream table is P1 duplication that costs tokens twice (writing it, then re-reading it) and
  hides the stage's real yield.
  **Measured 2026-07-21 (industry_US)**: `SECTOR_ROTATION.md` reproduced MACRO's transmission matrix
  on **8 of 9 comparable sectors** — 14KB whose true output was 2 verdict changes. `SWEEP_READ.md`
  restated **100% of its tickers and 97% of its numbers** from `SECTOR_FLOW_US.json`, in a file
  **nothing downstream reads**. Both stages were archived 2026-10-31 (their surviving rules live in MACRO §3 and
  FLOW_CHECK).
  **Self-test for any stage**: if you removed every sentence whose content exists upstream, what
  remains? That remainder is the stage's yield — and it should be most of the file.
  ⚠ Not every high-overlap stage is waste: PREMORTEM re-covers the same names **on purpose**, in the
  opposite direction (it reversed three of its own desk's calls on 2026-07-21), and DEEP's chain-hop
  surfaced 10 names the sweep universe structurally cannot see. Overlap is a **prompt to check
  yield**, not a verdict.

## Folder per layer
| Layer | Folder | What | Example |
|---|---|---|---|
| protocol | `protocols/` | L1 composition = a desk flow | `industry_us.md` = [HANDOVER,MACRO,PREMORTEM,EARNINGS,COMPETITION,FLOW_CHECK,BET,ALPHA] |
| L1 | `L1_stages/` | big stages | `macro.md`·`earnings.md`·`competition.md`·`bet.md`… |
| L2 | `L2_modules/` | module orchestration | `indicators.md`·`schedule.md`·`discovery.md`·`deepdive.md`·`news.md`·[`web_errand.md`](L2_modules/web_errand.md)·[`lens.md`](L2_modules/lens.md) |
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
python pipeline/run_protocol.py company --start --target 009150   # print stage 1 only (mode goes on CARRY.md line 1)
python pipeline/run_protocol.py company --next     # pass current EXIT CHECK → print next stage
python pipeline/run_protocol.py company --status   # progress table (✅passed / ▶current / ·pending)
python pipeline/run_protocol.py company --goto 4   # jump
```
Checkpoint at `out/pipeline_runs/{name}.json` (stage · passed · target). Do a stage → pass its EXIT CHECK →
`--next`. Prior stages' outputs live on disk — reread the run dir, not memory.

## Current contents
- ★ **Industry desk rebuilt 2026-10-31** (`industry_us` · `industry_kr`). New spine: HANDOVER → MACRO (financial
  environment read as the **size of data changes**, transmitted to company earnings; sector verdicts and the focus
  pick, absorbing ROTATION) → (US) PREMORTEM → **EARNINGS** (operating margin, guidance vs prior guide, estimate
  direction — from the filing; absorbs EVENT_ALPHA) → **COMPETITION** (share · price · capacity · customers · contract
  terms; replaces DEEP) → **FLOW_CHECK** (one short confirmation pass; replaces SWEEP) → BET (every conclusion
  registered in `module_lens` with evidence weights by kind) → ALPHA → HANDOVER close-out (absorbs DRIFT).
  Why: hours-long runs ended with flow tables and no operating-income, guidance or competition reading; the lens
  ledger's first learning scored filings evidence 6/8 and flow 5/32; the gates that let flow carry a conclusion
  (candidate entrance, rotation delta currency, removal veto, KR confirmation gate) were removed. Compiled size
  194/188 KB → under 100 KB each. Archive and restore: `_archive/2026-10-31/README.md` §industry.
- **HANDOVER (stage 1 of the industry desks)** inherits [`../handoff/`](../handoff/README.md) — now thin files
  (≈100 KB together, 2026-10-31) with the numbers in the lens ledger — settles `module_lens due` and both decision
  ledgers, copies the preflight permission table, and at close-out writes back append-only. Born from a measured
  2026-07-22 session in which **six judgments were reversed inside one session**, each re-discoverable from material
  a prior run already had.
- **protocols/**: `industry_us.md` (8 blocks) · `industry_kr.md` (7 blocks) · **`company.md` (9 blocks, modes
  research · report · forensic — merged 2026-10-31)** · `company_batch.md` (3 blocks) · `paper_desk.md` (6 blocks) ·
  `wrap_account.md` (8 blocks) · `미러링.md` (7 blocks) · **`preflight.md` (2 blocks)** — complete, compile-verified.
  Archived 2026-10-31: `idle_probe` (1 run since 07-10), `morning_brief` (3 runs), `company_research` · `기업분석` ·
  `real_alpha_kr` (merged into `company`).
  ★ **`preflight` runs BEFORE HANDOVER in any desk run.** It is a few-minute mechanical gate check
  whose output is not a report but a **claim-permission table**: a failed gate removes a citation
  right for that run (dead news axis ⇒ no theme-freshness claim; a sign-flipping sector bucket ⇒ no
  verdict off it). Born from 2026-08-09/10, where **12 instrument defects were found in one day and
  none of them threw** — every one returned a plausible number, and one silently inflated **every**
  flow score by **+0.305**. Finding new defects was `idle_probe`'s job (archived; restore from the archive when a
  human asks); `preflight` *prevents their return* (fast, boring) — a heavy daily check stops being run, which is
  the exact failure `measure_ic` demonstrated (0 invocations in 3 weeks).
  ★ **`company`** — one name, three questions as modes on one spine: filings (earnings · margin · guidance) →
  structure and competition → financial-environment transmission → money (flow only confirms) → value → refutation
  → verdict with weights in module_lens. research = bet (ledger row), report = own target + Word/PDF, forensic =
  REAL / PRICED / INFLATED / BROKEN. Merged 2026-10-31 because runs ended in flow tables: module_lens scored filings
  evidence 6/8, flow 5/32. Archive and restore: `_archive/2026-10-31/README.md`.
  `paper_desk` is the *downstream* desk — it consumes the research desks' `REPORT/` output and runs a simulated book
  (engine = `module_paper_book`; paper only, no real order). `미러링` mirrors the **real KIS account** into that book,
  applies judgment, and stages recommendations onto the real KIS order desk stack as **human-fireable intent cards**
  (no execution; not advice). The forensic «is it REAL?» question is now `company --mode forensic`. The strategy
  desk has its L1 decomposition in [PROMPT_MAP](PROMPT_MAP.md) — build the L1 blocks and compose.
  `wrap_account` is the **mandate layer above paper_desk**: sector target weights are declared and the same book
  is managed against them (drift bands · single-name/theme caps · portfolio beta band). It reuses 5 of
  paper_desk's L1s (mark·intake·decide·simulate·review) and reorders them — drift is measured *before* intake,
  so the desk reads research only for the sectors it is short of. Engine = `module_paper_book._allocate`;
  the module returns `NEEDS_CANDIDATE` instead of ever picking a name (P4). Paper only, `--commit` human-gated.
- **L1_stages/**: the 8 industry blocks **handover · macro · premortem · earnings · competition · flow_check · bet ·
  alpha** (2026-10-31) + **co_carry · co_filings · co_structure · co_macro · co_money · co_value · falsify ·
  co_verdict · publish_report** (company) + batch_select · batch_fanout · batch_score (company_batch) + pulse ·
  mirror_ingest · stage_orders (미러링) + **mandate_set · drift_check · rebalance_plan** (wrap_account) + the
  paper_desk blocks + **instrument_check · census** (preflight). Archived 2026-10-31: sweep · event_alpha · rotation ·
  deep · drift · leak_audit and the idle_probe/morning_brief-only blocks.
- **L3 `reject_ledger`** (2026-07-23) — the desk's rejections become a scored asset. Every
  DROP/PASS/강등 is appended with a reason class and a **`--revives-if`** condition, then scored by
  class and by **type** (`measured` / `structural` / `narrative`) against the equal-weight 1조+
  universe. Called by L2 [carryover](L2_modules/carryover.md); written by L1 bet · alpha · decide.
  First observation (n=24): **67% of rejections changed nothing** and the loss tail ran
  **2.2×** the gain tail — the unit exists to make that ratio visible and improvable, not to rule.
- **protocol `morning_brief`** (2026-07-23) — the pre-open *publication* desk (gather → rank → render, one
  phone-readable file at 08:30 KST). **Archived 2026-10-31** (3 runs since 07-10) with its L1s and L3 `public_source`
  (rule: cite where a fact entered the world, not our filename). Restore from `_archive/2026-10-31/`.
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
  L1 bet · alpha now write missed entries the way they already wrote rejections (the industry HANDOVER runs both
  `due` calls directly since 2026-10-31). The old supply line L1 leak_audit was archived 2026-10-31 (no protocol
  called it). ⚠ Zero new L2 — carryover absorbed both, which is the test that these were functions and not stages.
- **L1 `leak_audit`** (2026-07-23; **archived 2026-10-31**, no protocol called it) — the counterpart to §5 self-backtest: it scores what the desk did **not** do. Runs against a *past* run (≥3 sessions later), pairs `scripts/leak_scan.py` with L3 reject_ledger, and classifies every mover into A.런에있었음 / B.커버리지소실 / C.스쳐감 / D.발굴부재. Two guards are load-bearing: **forward-test only** (OBV is price×volume, so trailing scoring is tautological — measured: trailing said 매집 +42.2%, forward said it lost) and **label the window's regime** (measured: in the 07-20 bounce 🔴분산 +8.22% beat 🟢가속 +7.77%; in the 07-16 window 🟢 beat the universe 11×). First result: **B.커버리지소실 was the worst leak (+1.93pp, n=26) while D.발굴부재 UNDERPERFORMED (−0.70pp, n=89)** — discovery is not the leak, retention is.
  ⚠ **RETRACTED 2026-07-31 — that ordering does not reproduce, and it was quoted as settled for a week.**
  Re-scoring **the same 07-20 window** today (i.e. only the measurement horizon extended, through the
  07-28~30 crash and the 07-31 rebound) inverts it completely: **D.발굴부재 +2.58pp · C.스쳐감 +2.56 ·
  A.런에있었음 −0.31 · B.커버리지소실 −4.68pp** — B goes from *worst* to *best*. The 07-24 window scores
  the same way (D +3.57 · C +2.35 · A −0.73 · B −4.90), so the ordering is stable **across windows** and
  unstable **across horizons**. ⚠ The n's also disagree (26 vs 51, 89 vs 48), so the two runs were not
  like-for-like to begin with — which is the second half of the defect: the original figure was recorded
  without the parameters needed to reproduce it. ⇒ **"retention, not discovery" is withdrawn as a
  standing claim.** A single-window, single-horizon class mean is an observation, not a finding, and
  must not be cited as a reason to change the protocol (it was — see `industry_kr.md` FOCUS budget,
  now corrected).
- **L2/L3**: orchestration + atomic functions, reused across L1s. handover added L2 `carryover`
  (reads the carry + reconciles it against the mechanical ledger — a belief with no coverage gets
  demoted, coverage with no belief becomes a focus candidate) + L3 `scenario_score` (one scenario →
  one branch verdict, against the **frozen** threshold; `EXPIRED` is logged, never dropped).
  Since 2026-10-31 the industry HANDOVER calls the two ledgers directly and settles questions with `module_lens`;
  carryover and scenario_score stay for company_batch and the not-migrated brackets.
  wrap_account added L2 `mandate` + L3
  `portfolio_beta` (regression beta vs `^KS11`/`SPY`) — everything else it needs (bookkeeping · risk_model ·
  report_read · mark_position · size_from_risk) was already there. company merged its single-use units into co_*
  stages and one L3 valuation_math (2026-10-31). The industry rebuild added **zero** L2/L3: EARNINGS and COMPETITION
  call module_disclosure(_us) · module_fundamentals_us/kr · margin_history · module_industry_map · module_business_us
  directly plus the existing L2 web_errand · lens and L3 segment_pnl · competitors; L2 narrative_money (the 2×2 that
  let flow veto a story) was archived with EVENT_ALPHA.
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
- **protocol `company_research`** (2026-08-21; **merged into `company --mode research` 2026-10-31**) — the single-name **"do we bet"** desk (`PROMPT_MAP §2`,
  specified since the port and unbuilt until now). 10 L1 blocks, 8 of them reused; the two new ones are
  **DRIVER_TEST** and **BET_VERDICT**, plus three new L3 (`segment_pnl` · `driver_link` · `peer_pricing`).
  Its whole design comes from one measured failure mode: **starting at the sector label**. On a full
  module pass over PSX the desk modeled a five-segment company off one spread (Refining = 61.6% of
  pre-tax income), read a 4.6σ one-day driver drop as a margin collapse when it was an **RBOB Sep→Oct
  spec roll** (roll-adjusted −1.0% at the 92.8th percentile, not −12.5%), and wrote a +18.8%/20d move as
  name alpha when the whole peer set did the same (corr +0.90/+0.87/+0.77). ⇒ the new stage runs
  **before** money/valuation/falsify, because each inherits the denominator it produces.
  ★ It also found the desk **holding** PSX at +21.3% while an **unresolved rejection** sat in the ledger
  whose own `--revives-if` had not fired — no protocol had ever put those two files side by side, which
  is now gate **G8**.
  ⚠ **Compiler fix shipped with it**: `build_protocol.py` collected L3s from **L2 text only**, so every
  L3 an L1 calls *directly* was dropped from the compiled executable. `real_alpha_kr` named
  `filing_diff · contract_alpha · set_difference` in its stages and shipped a file containing **none** of
  them (L3 8 → 14 after the fix). Same class as PROMPT_MAP §7's dead references: **an instruction that
  cannot execute does not fail loudly, it just stops happening.** Recompile all after any L1 edit.
- **protocol `company_batch`** (2026-08-21) — the orchestrator above company (mode research): **N companies
  (default 10) as parallel subagents → one comparable scoreboard → the top-down run's input.** Three
  L1s (`batch_select` · `batch_fanout` · `batch_score`), **zero new L2** — select reuses carryover ·
  report_read · bookkeeping, fanout is the PREMORTEM Agent idiom, score is `scripts/company_score.py`
  plus the existing `ic_ledger` axis plumbing. That zero is the test that these were stages, not
  orchestration.
  ★ **Why it exists**: `industry_us` L1 BET was re-deriving company numbers *inside* a context already
  carrying nine stages. BET now has a **thesis-confirmation gate** — a candidate with a scoreboard row
  is confirmed by citation and only the delta is written; it re-digs only when one of five tests fails
  (age >10 settled sessions · a dated observation point matured · an earnings/8-K landed · the
  roll-adjusted driver percentile crossed a band · this run's earnings/competition evidence contradicts the row;
  since 2026-10-31 a flow-only disagreement is stated, not acted on).
  ⚠ **The score is unvalidated and says so in every artifact it writes.** Weights are hand-chosen and
  their relation to return has never been measured — which is why `company_score.py axes` emits it as
  `company_score` into `out/ic/axes/`, so the IC ledger grades it over months (`n_eff < 4` ⇒ no verdict,
  by design) instead of it being trusted now. Until then it is a **reading order**, not an expected
  return, and it may not size anything.
  ⚠ **Score and verdict are different objects** — the score is *research quality*, the verdict is the
  *action*. A high-scoring `PASS` is a success. Sorting by score and reading the top row as a buy
  collapses two axes both `batch_score` and `bet` keep apart on purpose.
  ⚠ Selection's yield is the names it **removed**; the skip list is published with counts, and the
  roster is never padded to reach N.
- **Language rule**: every unit here is written in **English** — the US desk runs English-pure
  (Korean in context skews the frame), and the KR desk reads English instructions while emitting
  KR-market outputs. Field-tested run notes are embedded per unit as ⚠ notes.
