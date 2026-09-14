# L2 · deepdive — dig deep (orchestration)

> Called by L1s. Dissects narrowed candidates: value chain, business, filings, valuation, chart.

## Calls
- Value chain / competitors — `python -X utf8 -m module_industry_map "<sector thesis terms>"`
  (nodes 5–8, surfaces sub-suppliers). L3 [related_companies](../L3_functions/related_companies.md) ·
  [competitors](../L3_functions/competitors.md).
- Business model — `python -X utf8 -m module_business_us AAPL --full --json` (US) /
  **`python -X utf8 -m module_disclosure 005930 --business-report`** (KR).
  ⚠ US: always `--json` — the default markdown carries KR scaffolding; extract the English SEC body
  (10-K Item 1 business / **Item 1A = a ready-made anti-signal source** / Item 7 MD&A).
  🚨 **KR: do NOT use `module_business --include-dart`.** That flag reaches
  `module_business/_dart_fetch.py`, which scrapes `dsaf001/main.do` — the DART **frameset shell**, i.e.
  the table-of-contents/nav page, not the filing — and can return UI strings ("잠시만 기다려주세요",
  "전체문서") as 본문. `module_disclosure._business_report` is the single source (P1): it parses the
  JS TOC for each section's viewer coordinates and reads `report/viewer.do` (fixed 2026-07-20).
  `module_business` itself is still correct for the **corp_embeddings** business model + IR 발췌 — use it
  **without** `--include-dart`.
- **Segment P&L — L3 [segment_pnl](../L3_functions/segment_pnl.md)**. The business text names the segments;
  it does **not** carry their earnings. Pull the segment table before any single-driver thesis, and read the
  Basis of Presentation with it (a consolidation-scope change is invisible in the number and fatal to a YoY).
- **What moves each segment — L3 [driver_link](../L3_functions/driver_link.md)** (roll-guarded) and
  **what the tape prices it as — L3 [peer_pricing](../L3_functions/peer_pricing.md)**. Called by L1 DRIVER_TEST;
  listed here so any L1 doing a deep dive can reach them.
- Filings catalyst — `python -X utf8 -m module_disclosure 034020 --days 60` / `module_disclosure_us AAPL` (8-K list).
- Valuation / fundamentals — `python -X utf8 -m module_valuation 005930 --peers …` /
  `python -X utf8 -m module_fundamentals_us AAPL --json` (XBRL primary; cross-check vs yfinance).
- Chart structure — `python -X utf8 -m module_chart <ticker> --read` (embed the CHART_READ block
  verbatim in the brief — don't summarize it away into metadata).
- Arithmetic check — `python -X utf8 -m module_math_check` on any derived figure.

## Output
Per-candidate business + numbers + chart dissection. **The calling L1 (DEEP/BET) assembles the report;
blanks stay blanks — no guessed numbers.**
