# L2 · report_read — read finished reports (orchestration)

> Called by L1·INTAKE. Turns the desk's own `REPORT/` output into a validated, freshness-tagged candidate
> ledger. Reuses `module_report_tags` (ticker universe + tag extraction) — never re-implements it. Composes L3.

## Calls (all `python -X utf8`)
- Candidate ledger — `python -X utf8 -m module_paper_book intake [--dir REPORT]`
  (scans `REPORT/**.md`, prioritizing `BET_SHEET.md` + `ACTION_TICKETS.md`; validates tickers against
  `data/us_universe` / `data/kr_universe` via `module_report_tags._config`; parses freshness 🟢/🟡/🔴,
  hard-stops, section/theme, ★core).
- Per-report verdict parse — L3 [read_verdicts](../L3_functions/read_verdicts.md) (atomic: one report → its
  freshness/verdict/stop tags).
- Cross-reference "who already covered this" — `python -X utf8 -m module_report_tags ticker <TKR>` (the handoff
  ledger reverse-lookup) so a name's full report history is visible before acting.

## Output
A freshness-bucketed candidate list (🟢LIVE / 🟡PARTIAL / 🔴RESOLVED · ★core · stop · theme · source report).
**INTAKE folds it into `INTAKE_LEDGER.md`; it adds no names the reports never raised.**
