# L1 · BATCH_SCORE — N verdicts → one comparable scoreboard the top-down run can read

> Phase 3 (terminal) of the company batch. Converts N heterogeneous reports into **one ranked table on
> one scale**, publishes it where the industry desk will look, and registers the score itself as an
> IC axis so it gets graded over time instead of being trusted. Calls a script + L3. Output:
> `REPORT/COMPANY_SCOREBOARD.md` + `out/company_batch/scoreboard.json`.

## Belief
Ten reports written by ten agents are ten opinions until something puts them on one axis. The
conversion must be **arithmetic performed on fields already recorded**, never a re-read of the prose —
otherwise the ranking is an eleventh opinion, and the least accountable one.

## Calls
```bash
python -X utf8 scripts/company_score.py rank --run {date}          # the table
python -X utf8 scripts/company_score.py rank --run {date} --json   # machine copy
python -X utf8 scripts/company_score.py axes --run {date}          # → out/ic/axes/{market}_{run}.json
```
- L3 [ic_ledger](../L3_functions/ic_ledger.md) — the axis file above is picked up by the next
  `ic_ledger log`, exactly like [axis_inflection](../L3_functions/axis_inflection.md) and
  `axis_window_flow` (same plumbing, zero ledger changes — P1).

## The scale (weights are in the script, not here — one source)
`gate_integrity 30 · evidence_grade 25 · driver_quality 20 · frame_integrity 10 · reward_risk 15`,
renormalised over the axes that were **actually measured**. A missing axis leaves the denominator, it
does not score zero — writing zero for *unmeasured* is how `flow_score` inflated every name by +0.305
(2026-08-10) and the same mistake is available here.

## 🚨 The score is UNVALIDATED — say so every time it is published
The weights are hand-chosen and their relationship to return has **never been measured**. That is
precisely why `axes` exists: the composite is emitted as `company_score` and the IC ledger will take
months to give it a sign (`n_eff < 4` ⇒ no verdict, by design). Until then it is a **triage order** —
which report to read first — and it may not be cited as an expected return or used to size. Sizing is
`kelly_size` + the SIZE stage against the live book.

⚠ **Score and verdict are different objects.** The score measures **research quality**; the verdict is
the **action**. A high-scoring `PASS` means *we investigated it well and are not buying* — that is a
success of the desk, and any presentation that sorts by score and reads the top row as a buy has
collapsed two axes that this stage deliberately keeps apart.

## What gets published, and where the top-down run finds it
| artifact | path | read by |
|---|---|---|
| ranked table + per-name thesis line | `REPORT/COMPANY_SCOREBOARD.md` | L1 BET (thesis-confirmation gate) · `module_report_tags` (auto-indexed into `HANDOFF.md`) |
| machine copy | `out/company_batch/scoreboard.json` | any stage that wants the fields without parsing markdown |
| per-name detail | `llm_outputs/{date}/company_batch/{ticker}/REPORT.md` | BET, only when confirmation fails and it must re-dig |
| IC axis | `out/ic/axes/{market}_{run}.json` | `ic_ledger log` |

★ `COMPANY_SCOREBOARD.md` carries, per name: **thesis (one line) · verdict · stop · score · axes
measured · the dated observation points · the report path**. Those six fields are exactly what BET
needs to *confirm* rather than re-derive — anything less and the top-down run re-digs by necessity.

## ✅ EXIT CHECK
- [ ] `rank` run and its table pasted into `COMPANY_SCOREBOARD.md`; `axes` run and its path printed.
- [ ] Every row carries the **thesis line, the stop, and the observation points** — not just a number.
- [ ] The unvalidated-score warning is in the published file, not only in this stage.
- [ ] Names with `axes_measured < 4` are flagged in the file — their score is on a different scale and is **not** rank-comparable.
- [ ] completed / failed / skipped counts from BATCH_FANOUT reproduced at the top of the scoreboard.
- [ ] `python -X utf8 -m module_report_tags update` run, so the handoff ledger indexes the new reports this run.
