# L2 · carryover — read and reconcile the standing view (orchestration)

> Called by L1·HANDOVER. Turns `handoff/` (the analytical carry) plus the mechanical tag ledger into
> one reconciled inheritance packet. Reuses `module_report_tags` — never re-implements it. Composes L3.

## Calls (all `python -X utf8`)

**1. Read the carry** — plain file reads, no module needed:
```
handoff/STANDING_VIEW.md    regime call · measured chain · per-name theses · retracted ledger · open contradictions
handoff/SCENARIOS.md        pre-registered branches + scoring log
handoff/RESEARCH.md         Part A rules · Part B lenses · Part C dig list
```

**2. Reconcile against the mechanical ledger** — what we *believe* vs what we *covered*:
```bash
python -X utf8 -m module_report_tags show            # who covered what, with which verdict
python -X utf8 -m module_report_tags ticker <TKR>    # per-name report history
```
The two are different objects and must be cross-read, not merged:
- A name in STANDING_VIEW with **no** ledger coverage = a belief no report supports → demote or dig.
- A name with heavy ledger coverage and **no** standing thesis = an unowned coverage gap → candidate
  DEEP (this is exactly how 009150 surfaced as C2).
- A ledger 🔴RESOLVED that still has a live thesis = staleness → re-justify or retract.

**3. Score matured scenarios** — L3 [scenario_score](../L3_functions/scenario_score.md), one call per
`ARMED` row whose event date has passed. Atomic: one scenario → one branch verdict.

**3b. Audit the rejection ledger for anything due — do not rely on `score` alone for this.**
L3 [reject_ledger](../L3_functions/reject_ledger.md). Rejections are the one desk action that used
to leave no score. Run **both**:
```bash
python -X utf8 scripts/reject_ledger.py due     # ★ run this one first, every HANDOVER, no exceptions
python -X utf8 scripts/reject_ledger.py score   # per-class / per-type excess return (context, not a gate)
```
`score` benchmarks against the **equal-weight 1조+ universe**, never the index (measured 2026-07-23,
equal-weight −2.6% vs cap-weight −15.7% — an index benchmark flatters every rejection). It tells you
which reason classes are earning their keep. It does **not** by itself surface a revived name — that
is `due`'s job, and until 2026-07-23 nothing called it: 24 of the ledger's 25 rows were entered with
no `revives_if`/`recheck_date` at all, so "any row whose condition has now come true" was silently
unstatable for almost the whole ledger. That gap cost **+41.2pp and +26.9pp on SK이터닉스 alone** —
the ledger's two most expensive rows, both narrative-class, both never re-examined until a user
prompted a manual re-audit.

⚠ **A HANDOVER that skips `due` is not a lighter HANDOVER — it is the same failure mode as an
unscored SCENARIOS.md row, just on the candidate side instead of the macro side.** `due` output has
two sections and neither may be waved through silently:
- **재확인일 도래/경과** (recheck date has passed) — re-pull flow/news for each name named here
  (same re-pull commands as §4 below) and either `resolve --outcome revived` (back into §A/§B with
  its original evidence, per the 2026-07-23 SK이터닉스 precedent) or `resolve --outcome reaffirmed`
  (stays out, but now on fresh evidence, not a stale one).
- **부활조건 없는 레거시** (no revival condition was ever set) — these cannot be re-checked on a
  schedule because there is no schedule; HANDOVER may not carry them forward unexamined a second
  time. Either audit one now with a fresh pull, or explicitly note it as still-pending audit in
  `HANDOVER.md` so the gap is visible, not silent.
- A `due` row that surfaces two HANDOVERs in a row without a `resolve` call against it is a process
  failure to name in `HANDOVER.md`, the same way an `EXPIRED` scenario is named, never dropped quietly.

**4. Re-measure anything the carry marked suspended-until-a-date.** When a suspension's clearing date
has passed, the carry does not tell you the answer — it tells you to go get it. This includes any
**watch condition an earlier stage armed** ("enter on the breakout", "revisit after the 2Q NIM print"):
an armed condition that nobody re-reads is an idea the desk paid for and never collected. Typical re-pulls:
```bash
python -X utf8 -m module_flow <TKR>.KS --bench ^KS11              # KR flow + short balance
python -X utf8 -m module_KIS <6-digit> --investor 20              # KR investor actuals
python -X utf8 -m module_fundamentals_us <TKR>                    # valuation vs its own history
```
⚠ **KR tickers need the `.KS` suffix in `module_flow`.** A bare 6-digit code returns empty rows
**without erroring** — measured, and it silently reads as "no flow signal" on a day flow reversed.

## Output

An inheritance packet for HANDOVER, in four parts:
1. **Carried theses**, tags (`[measured]`/`[inferred]`) intact, each with `asof` and a stale flag.
2. **Retracted ledger**, surfaced verbatim so today's view is checked against it before it forms.
3. **Scenario status** — scored this run / still armed with dates / expired-unscored (a logged failure).
4. **Reconciliation deltas** — beliefs without coverage, coverage without beliefs, resolved-but-live.

**HANDOVER folds this into `HANDOVER.md`. This L2 adds no new views and no names — it transports and
reconciles what already exists, and says plainly where the two ledgers disagree.**
