# L2 · deepdive — dig deep (orchestration)

> Called by L1s. Dissects narrowed candidates: value chain, business, filings, valuation, chart.

## Calls
- Value chain / competitors — `python -X utf8 -m module_industry_map "<sector thesis terms>"`
  (nodes 5–8, surfaces sub-suppliers). L3 [related_companies](../L3_functions/related_companies.md) ·
  [competitors](../L3_functions/competitors.md).
- Business model — `python -X utf8 -m module_business 005930` / `python -X utf8 -m module_business_us AAPL --full --json`
  ⚠ US: always `--json` — the default markdown carries KR scaffolding; extract the English SEC body
  (10-K Item 1 business / **Item 1A = a ready-made anti-signal source** / Item 7 MD&A).
- Filings catalyst — `python -X utf8 -m module_disclosure 034020 --days 60` / `module_disclosure_us AAPL` (8-K list).
- Valuation / fundamentals — `python -X utf8 -m module_valuation 005930 --peers …` /
  `python -X utf8 -m module_fundamentals_us AAPL --json` (XBRL primary; cross-check vs yfinance).
- Chart structure — `python -X utf8 -m module_chart <ticker> --read` (embed the CHART_READ block
  verbatim in the brief — don't summarize it away into metadata).
- Arithmetic check — `python -X utf8 -m module_math_check` on any derived figure.

## Output
Per-candidate business + numbers + chart dissection. **The calling L1 (DEEP/BET) assembles the report;
blanks stay blanks — no guessed numbers.**
