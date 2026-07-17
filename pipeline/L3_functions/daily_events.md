# L3 · daily_events — the day's events (not articles)

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing.

- **Role**: turn a day's raw article flood into **events** — same story told 27–54 times collapses
  to one line, ranked by **how many outlets ran it** (= editors independently judging it news).
  This is the "what actually happened today, all of it" axis; term-frequency tools cannot give it.
- **Input**: `--date` (market day, published_at-based) · `--scope domestic|foreign|all`.
- **CLI** (client-only — needs the GPU vector store; run `embed sync` first, ~2s/day):
  ```bash
  python -X utf8 -m module_news_data embed sync                          # catch up (server→client)
  python -X utf8 -m module_news_data brief --date <D> --scope domestic --json
  ```
- **Output**: tiered — `head` (≥5 outlets, the day's news) · `body` (3–4 outlets, one line each) ·
  `tail` (2 outlets: **count + random sample**, NOT cut) · `denominator` (articles→clusters→events).
  Measured: 3,782 articles → 512 events → 394 market → head 61 / body 143 / tail 190 ≈ 44k tokens.

⚠ **Read the tail's count, not just the shown sample.** Outlet-count is a good proxy for importance,
  not the truth — real items hide there (a "Korea–Singapore FTA renegotiation" sat at 2 outlets).
  The sample+denominator exist so you know what you did NOT see and can drill down.
⚠ **This does not say direction.** 2026-07-07's top event [54 articles/9 outlets] was Hanwha Ocean
  **LOSING** the Canada submarine deal, not winning it. The headline alone misleads; `--lede` would
  carry the why but is **off by default** (asiae·sedaily bodies are 100% page furniture in the first
  400 chars → 22% of ledes belonged to a different article). Until the scraper is fixed, confirm
  direction with [drill_detail](drill_detail.md) before you act on any event.
⚠ Market/non-market filtering is **domestic-only** (the classifier is Korean-trained). Foreign feeds
  are 82% finance by source selection, so nothing is filtered there — `nb` comes back null, not 0.
