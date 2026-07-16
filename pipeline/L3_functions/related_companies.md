# L3 · related_companies — extract related companies

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing.

- **Role**: from a theme, extract beneficiary companies that are NEVER named in titles but appear
  body-proximate (one hop down the chain = where the un-crowded alpha leaks).
- **Input**: theme terms · `--scope` · `--days` (KR: sector thesis terms).
- **CLI**:
  ```bash
  python -X utf8 -m module_news_data chain-hop "<theme1>" "<theme2>" --days 14 --scope foreign   # US
  python -X utf8 -m module_industry_map "<sector thesis terms>" --top-n 30                        # KR
  ```
- **Output**: CHAIN-HOP candidates (0 title mentions + ≥N body-proximity). ⚠ A co-mention alone is
  NOT a candidate — the flow unit must cross-check each before it may enter a bet stage.
