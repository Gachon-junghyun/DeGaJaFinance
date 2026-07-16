# L3 · random_news — random news sample

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing.

- **Role**: surface a random sample from the UNSEEN pool + token-0 emergent terms (the ~76% blind
  spot a fixed term set never queries).
- **Input**: (optional) the fixed term set · `--scope` · `--days` · `--sample-pct`.
- **CLI**:
  ```bash
  python -X utf8 -m module_news_data blindspot --sample-pct 35 --days 14 --scope foreign --json
  ```
- **Output**: `sample[]` (read the rows RAW — bucketing them through pre-named regexes re-imposes
  the blindness the sample cures) + `emergent_terms` (mostly noise alone; a **rank JUMP** of a single
  name is itself the signal → body-read once before classifying) + coverage %.
