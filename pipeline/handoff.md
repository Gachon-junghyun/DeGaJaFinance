# handoff — REPORT handoff ledger (prevents re-searching)

> Every layer's output reports accumulate in `REPORT/`. This step **extracts tags only and
> incrementally updates the ledger**; the next desk reads the ledger first instead of re-searching
> and re-reporting. (Engine: [`module_report_tags`](../MODULE_MAP.md#module_report_tags))

## When
- **Right after a protocol finishes writing its reports to `REPORT/`** — fold the tags into the ledger.
- **At the start of a MACRO stage** — query the ledger first to inherit "already covered"
  (decides what needs fresh digging vs inheritance).

## Run
```bash
python -X utf8 -m module_report_tags update          # incremental REPORT/ scan → HANDOFF.md + _tags.json
python -X utf8 -m module_report_tags show            # print the ledger (who covered what, which verdict)
python -X utf8 -m module_report_tags ticker 005930   # reverse-lookup reports covering a ticker
```

## What the ledger holds
- **Per ticker** — which reports covered it, how often, with what verdict (🟢LIVE/🔴RESOLVED/GO/REAL…).
- **Per sector · per desk** — report list + representative themes.
- **Incremental** — file-mtime tracking → only new/changed reports re-extracted.

## Rules
- Downstream desks **query the ledger first**. If it's already there, inherit the report instead of re-searching.
- Dig fresh through L1–L3 only when the ledger has nothing or is stale.
- The 🔴RESOLVED log matters as much as 🟢 — it stops "it's cheap" theses resurfacing every run.

**→ loop: when a new judgment is needed, start from the protocol's MACRO block again.**
