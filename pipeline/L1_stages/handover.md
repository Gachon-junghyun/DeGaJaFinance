# L1 · HANDOVER — inherit the standing view before anything else (stage)

> Big stage. **Runs first, before MACRO**, in every desk protocol. Calls L2.
> Reads `handoff/` (the analytical carry) and, at run end, writes back what changed.
> Runtime: `--market us|kr` (the carry is market-tagged; read both, cite the one you are running).
> Output: `HANDOVER.md` under the protocol's output root, plus in-place updates to `handoff/*.md`.

**Why this stage exists.** `REPORT/` + [handoff ledger](../handoff.md) answer *what was covered*.
They do not answer *what we currently believe, what we already pre-committed to, and what we already
got wrong*. Without that, a run re-derives a view it already had and re-makes errors it already paid
for — measured 2026-07-22: **six judgments reversed inside a single session**, every one of them
re-discoverable from a prior run's material. This stage is the inheritance step.

## L2 called
- [carryover](../L2_modules/carryover.md) — reads `handoff/STANDING_VIEW.md`, `SCENARIOS.md`,
  `RESEARCH.md`; cross-queries the mechanical ledger (`module_report_tags show`) so *what we believe*
  and *what we covered* are reconciled rather than duplicated; scores any scenario whose date passed.
- [report_read](../L2_modules/report_read.md) — only when the protocol also runs an intake-style
  stage. HANDOVER does not build candidate lists; it inherits **views**, not names.

## What this stage does

### 1. Inherit — read before deciding anything
- **STANDING_VIEW** — the regime call, the measured chain, per-name theses.
  ⚠ Every claim is tagged `[measured]` or `[inferred]`. **An `[inferred]` claim may be carried but
  may not be cited as evidence** for a new proposition. Carry the tag forward; do not launder it.
- **Retracted ledger (§5)** — read it *before* forming today's view, not after. It is append-only
  precisely so a killed thesis cannot resurface as a fresh idea.
- **Open contradictions (§6)** — carried deliberately. Do not resolve one by picking a side; if you
  resolve it, resolve it with a measurement and move it out.

### 2. Score — settle every scenario whose date has passed
- For each `ARMED` row in `SCENARIOS.md` whose event date is now in the past, call L3
  [scenario_score](../L3_functions/scenario_score.md) and write the branch that fired.
- ⚠ **An unscored past-dated scenario is a process failure**, not a neutral. Mark it `EXPIRED` and
  log why. A desk that only scores its hits has no track record.
- Scoring is against the **pre-registered observable and threshold only**. If the observable was
  ambiguous, that is a finding about the scenario's construction — record it; do not improvise a
  new threshold to make the call scoreable.

### 2b. Audit the rejection ledger — do not let a due row cross a second HANDOVER unexamined
- Run L3 [reject_ledger](../L3_functions/reject_ledger.md) `due` — never `score` alone; `score`
  tells you which reason classes are earning their keep, it does not surface a revived name.
- ⚠ **A `due` row that carries into a second HANDOVER without a `resolve` call is a process
  failure**, the same class as an unscored `EXPIRED` scenario — name it in `HANDOVER.md`, do not
  drop it silently.
- For every row `due` surfaces (recheck date passed, or a legacy row with no `revives_if` ever set),
  re-pull the name's flow/news (§4 re-pull commands below) and either `resolve --outcome revived`
  (back into the candidate pool with its original evidence, not laundered) or
  `resolve --outcome reaffirmed` (stays out, on fresh evidence). Do not skip a legacy row twice in
  a row just because it has no scheduled date — it has no schedule precisely because it was never
  given one, which is the defect, not a reason to keep deferring it.
- ⚠ **Do not treat a clean `due` run (nothing due) as proof the ledger is healthy.** Cross-check the
  legacy-count line — a shrinking legacy count across runs is the only real evidence this practice is
  taking hold, not a quiet pass this run.

### 3. Stale-check — every carry has an expiry
- Flag any STANDING_VIEW row whose `asof` is older than this run's horizon, and any suspension whose
  clearing date has passed (e.g. a blocked cross-listing conversion window). A suspension that has
  cleared is a **dig instruction**, not a silent trust.
- ⚠ Do **not** retroactively clean a contaminated data stretch once the contamination ends. The old
  window stays unreadable.

### 4. Load the method rules
`handoff/RESEARCH.md` is the **single source** for research rules — 21 triggers + 3 lenses,
consolidated from four previously-scattered locations. `lab/` is now the evidence archive only
(it records how a finding was derived; RESEARCH.md records what to do about it) and is **not read
during a run**.

Rules are grouped **by the moment they fire**, so a stage can load the ones that apply to it:

| Group | Fires when | IDs | Binds |
|---|---|---|---|
| **C** | you cite a number | C1 baseline·C2 both halves·C3 unknown column·C4 "indistinguishable"·C5 arbitrary choice | MACRO · every stage |
| **S** | you make a statistical claim | S1 date-fold·S2 diagnose the null·S3 power first·S4 in-sample≠done·S5 short samples·S6 future labels | any stage citing a test |
| **D** | you read data | D1 second listing venue·D2 proxy sign·D3 signed vs unsigned·D4 regime contamination·D5 cross-provider·**D6 signal grade (A/B/C/rejected — OBV is C)** | SWEEP · ALPHA · L2 indicators · L2 money_trail |
| **W** | you write a conclusion | W1 cross-market transfer·W2 inherited lead/lag·W3 real≠profitable·W4 name the customers·W5 sub-sector dispersion | DEEP · BET · ROTATION |
| **L** | (lenses, not triggers) | L1 second derivative·L2 peak-margin trap·L3 branch information content | DEEP · PREMORTEM |

- ⚠ **Load them as binding constraints, not as a summary.** Measured 2026-07-22: three of that
  session's six reversals broke rules that already existed — written as prose, in a folder
  `pipeline/` referenced **zero** times. A rule that is read but not carried into the working
  constraints is the failure mode this stage exists to close.
- Surface Part C (the dig list) — the top open digs are candidate DEEP assignments for this run.
  ⚠ **D9 and D10 are open code defects** the lab found, documented, and never fixed (holdco
  concentration; news-body boilerplate). Both need human approval to change code — carry them
  forward rather than silently re-discovering them.

### 5. Emit
- `HANDOVER.md` — inherited regime call + per-name carry + scenarios scored this run + still-armed
  scenarios with their dates + stale flags + the dig list ranked for today.
- Write back to `handoff/*.md` at run end: new/updated theses, newly registered scenarios, any claim
  retracted **this** run (append to §5 with the measurement that killed it), and new dig items.

## ✅ EXIT CHECK
- [ ] `handoff/STANDING_VIEW.md`, `SCENARIOS.md`, `RESEARCH.md` all read; mechanical ledger
      (`module_report_tags show`) cross-queried so belief and coverage are reconciled.
- [ ] **Retracted ledger read BEFORE forming today's view.** Any claim in this run that matches a
      retracted entry is either dropped or re-argued with a *new* measurement that names the old one.
- [ ] **Every past-dated scenario scored or explicitly marked `EXPIRED` with a reason.** Zero silent
      skips — this is the check the stage exists for.
- [ ] **`reject_ledger.py due` run this HANDOVER — not skipped, not substituted with `score` alone.**
      Every row it surfaces is either `resolve`d this run or explicitly named as still-pending in
      `HANDOVER.md` (never silently carried a second time). The legacy (no-`revives_if`) count is
      reported and, run over run, does not sit flat forever.
- [ ] Stale rows flagged with their `asof`; every cleared suspension converted into a dig item.
- [ ] `[measured]` / `[inferred]` tags preserved on every carried claim. No `[inferred]` claim is
      passed downstream as evidence.
- [ ] **RESEARCH triggers loaded as binding constraints**, grouped C/S/D/W + lenses L — not summarized.
      State which groups bind which downstream stages in `HANDOVER.md`.
- [ ] `HANDOVER.md` written; `handoff/*.md` updated at run end (append-only for retractions).
- [ ] No position sizing, no buy/sell language anywhere in the carry (P4 — this stage transports
      analysis, never a recommendation).
