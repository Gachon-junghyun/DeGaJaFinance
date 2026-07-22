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

**4. Re-measure anything the carry marked suspended-until-a-date.** When a suspension's clearing date
has passed, the carry does not tell you the answer — it tells you to go get it. Typical re-pulls:
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
