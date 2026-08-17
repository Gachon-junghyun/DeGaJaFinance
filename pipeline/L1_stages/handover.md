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
- [carryover](../L2_modules/carryover.md) — reads the **shared spines** `handoff/STANDING_VIEW.md`
  and `handoff/SCENARIOS.md` **plus this desk's market half** (`STANDING_VIEW_{US|KR}.md`,
  `SCENARIOS_{US|KR}.md`) and `RESEARCH.md`; ⚠ **split 2026-07-29 — the spine carries §5 (the
  retracted ledger) and the master scoring log UN-SPLIT, and a past-dated row owned by the OTHER
  market is still this run's to score: open that file rather than skipping it**; cross-queries the mechanical ledger (`module_report_tags show`) so *what we believe*
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

### 2b. Audit **both** ledgers — do not let a due row cross a second HANDOVER unexamined
> ★ 2026-07-31: this section used to name only the rejection ledger. Scoring what you *refused*
> while never scoring what you *never reached* is not discipline — it is a scoreboard with one team
> on it (F2). L3 [missed_ledger](../L3_functions/missed_ledger.md) is now run beside it, every run.
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
| **W** | you write a conclusion | W1 cross-market transfer·W2 inherited lead/lag·W3 real≠profitable·W4 name the customers·W5 sub-sector dispersion·**W6 reader's-market spine** | DEEP · BET · ROTATION · **BRIEF_GATHER · BRIEF_RANK** |
| **L** | (lenses, not triggers) | L1 second derivative·L2 peak-margin trap·L3 branch information content | DEEP · PREMORTEM |

- ⚠ **Load them as binding constraints, not as a summary.** Measured 2026-07-22: three of that
  session's six reversals broke rules that already existed — written as prose, in a folder
  `pipeline/` referenced **zero** times. A rule that is read but not carried into the working
  constraints is the failure mode this stage exists to close.
- Surface Part C (the dig list) — the top open digs are candidate DEEP assignments for this run.
  ⚠ **D10 is an open code defect** the lab found, documented, and never fixed (news-body boilerplate);
  it needs human approval and a **server console** (FTS writes are server-only, P6). Carry it forward
  rather than silently re-discovering it. **D9 is now half-closed** — the holdco problem is measured
  and surfaced (L2 [risk_model](../L2_modules/risk_model.md) · L1 [size](size.md)); what remains is
  whether a mismatch **blocks** or only **warns**, which is a human call.

### 4b. 🚨 A capability nothing invokes is a capability that does not exist — so count the calls
`handoff/README.md` opens its toolkit table with exactly that sentence, and **that table contained a
command nobody had ever run** (`scripts/measure_ic.py`, 3 weeks after registration; also
`module_disclosure_us`, `module_inflection`, `module_watchlist`, `module_publish`, and
`scripts/risk_units.py` at **zero** pipeline invocations — the tool that killed R10).
The reason nobody noticed is simple: **there was no line that counted.**
- Count **CLI invocations**, not mentions — measured 3–15× inflation (`module_flow`: 172 mentions
  vs **11** invocations; `module_inflection`: 5 vs **0**).
- Three buckets: **fully idle** (0/0/0) · **not wired** (`pipeline/` 0 but used ad hoc) · **shim**
  (0 is correct — exclude with a reason).
- ⚠ **A tool whose `--help` crashes reads as "nobody uses it."** `risk_units.py` died on a bare `%`
  in an argparse help string — one character kept the tool unreachable for three weeks.
- This is L1 [census](census.md); the `preflight` protocol runs it. Weekly is enough.

### 4c. 🚨 Verification that arrives after the assertion is a finding, and it gets written down
The desk counts this as the **D48** pattern and it has 12 KR instances. It applies to **the author of
the current run**, not only to inherited claims. Measured 2026-08-09: this desk's own operator wrote
*"the grouping is invariant under every perturbation"* and the **next command refuted it** (a `--days`
sweep dissolved the AI-compute unit at a 1-year window).
⇒ **Do not silently edit the earlier sentence.** Leave it and append what broke it, in the run's own
output. A run that only shows its surviving claims has hidden its own error rate — which is the same
failure as a desk that only scores its hits (§2).

### 5. Emit
- `HANDOVER.md` — inherited regime call + per-name carry + scenarios scored this run + still-armed
  scenarios with their dates + stale flags + the dig list ranked for today.
- Write back to `handoff/*.md` at run end: new/updated theses, newly registered scenarios, any claim
  retracted **this** run (append to §5 with the measurement that killed it), and new dig items.

## ✅ EXIT CHECK
- [ ] `handoff/STANDING_VIEW.md` + `SCENARIOS.md` (**the shared spines, in full**) + this desk's
      `STANDING_VIEW_{US|KR}.md` and `SCENARIOS_{US|KR}.md` + `RESEARCH.md` all read; **and any
      other-market file opened if it holds a past-dated row this run must score**; mechanical ledger
      (`module_report_tags show`) cross-queried so belief and coverage are reconciled.
- [ ] **Retracted ledger read BEFORE forming today's view.** Any claim in this run that matches a
      retracted entry is either dropped or re-argued with a *new* measurement that names the old one.
- [ ] **Every past-dated scenario scored or explicitly marked `EXPIRED` with a reason.** Zero silent
      skips — this is the check the stage exists for.
- [ ] **`reject_ledger.py due` run this HANDOVER — not skipped, not substituted with `score` alone.**
      Every row it surfaces is either `resolve`d this run or explicitly named as still-pending in
      `HANDOVER.md` (never silently carried a second time). The legacy (no-`revives_if`) count is
      reported and, run over run, does not sit flat forever.
- [ ] **`missed_ledger.py due` run too — the ledger is symmetric or it is not a scoreboard**
      (`carryover.md` §3c). Same treatment as the rejection rows. ⚠ Its `excess` sign is **inverted**;
      the two ledgers are never summed without aligning signs.
- [ ] **Exposure state read and carried** (`carryover.md` §3d, L3
      [exposure_state](../L3_functions/exposure_state.md)): the 4-state verdict, target vs current
      invested %, and the cumulative cash/selection split go into `HANDOVER.md` as size context for
      BET/ALPHA. ⚠ If `show` has no rows, say **cold start** and do not quote the verdict as reliable —
      measured 2026-07-31, cold start read `방어`/−1.9pp where the backfilled path read `복귀`/**−37.2pp**.
      ⚠ If the state is `밴드미설정`, that is reported as 🚨 and no number is substituted (P5).
- [ ] 🚨 **Instrument health inherited before any number is trusted** — read
      `llm_outputs/{date}/preflight/PREFLIGHT.md` (protocol [preflight](../protocols/preflight.md))
      or state that it was not run. A FAILED gate **downgrades what this run may claim**: a dead news
      axis bars every theme-freshness citation; a `top1_flips_sign` bucket bars a sector promotion.
      ⚠ An instrument that returns a number is not the same as an instrument that is working —
      measured: a dropped news axis silently inflated **every** flow score by **+0.305**.
- [ ] **Any claim this run asserted and then refuted is written down, not edited away** (§4c, D48).
      Zero self-refutations in a run that ran controls is itself worth a line — it usually means the
      controls were not adversarial.
- [ ] Stale rows flagged with their `asof`; every cleared suspension converted into a dig item.
- [ ] `[measured]` / `[inferred]` tags preserved on every carried claim. No `[inferred]` claim is
      passed downstream as evidence.
- [ ] **RESEARCH triggers loaded as binding constraints**, grouped C/S/D/W + lenses L — not summarized.
      State which groups bind which downstream stages in `HANDOVER.md`.
- [ ] `HANDOVER.md` written; `handoff/*.md` updated at run end (append-only for retractions).
- [ ] No position sizing, no buy/sell language anywhere in the carry (P4 — this stage transports
      analysis, never a recommendation).
