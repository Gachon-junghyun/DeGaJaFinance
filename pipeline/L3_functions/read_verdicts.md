# L3 · read_verdicts — one report → its tags (function)

> Single deterministic job: parse ONE report file into its surface signals. No judgment (P4) — tags are data.

## Run
- `python -X utf8 -m module_paper_book intake --dir <path>` (whole dir) — or, programmatically,
  `from module_paper_book import read_actionable` for one directory.
- Per file it extracts: **tickers** (validated against the US/KR universe via `module_report_tags`) ·
  **freshness** (🟢LIVE / 🟡PARTIAL / 🔴RESOLVED) · **hard-stop** (`stop`/`스탑 <num>`) · **section/theme** ·
  **★core** (lines under an EPICENTER / CORE-STARTER block).

## Output
A list of `Candidate(ticker, market, freshness, theme, stop, is_core, source_report)`.
**The caller (report_read → INTAKE) merges across reports; the strongest freshness per source wins, conflicts kept.**
