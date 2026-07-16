# L3 · drill_detail — drill into bodies

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing.

- **Role**: drill a given theme/emergent term down to article BODIES and confirm or refute the
  narrative (title+summary-only search is ~49% body-blind).
- **Input**: theme term · qualifier term(s) · `--scope` · `--days`.
- **CLI**:
  ```bash
  python -X utf8 -m module_news_data search "<theme>" "<qualifier>" --field any --match-mode and --days 30
  python -X utf8 -m module_news_data fts search "<theme>" --days 14 --scope foreign --syn --full
  ```
  ⚠ `--field any` REQUIRES and-mode pairing for common words (a bare "dollar"/"oil" floods).
- **Output**: body evidence (supports/refutes verdict). If coverage is in doubt, quantify with
  `coverage <terms>` ("what % of the pool do I see", with denominator).
