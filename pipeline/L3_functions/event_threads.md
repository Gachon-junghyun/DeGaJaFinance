# L3 · event_threads — the week's event TRAJECTORIES (not snapshots)

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing.

- **Role**: answer the question the daily view cannot: **is this event new, building, fading, or
  re-igniting?** [daily_events](daily_events.md) collapses one day's articles into events; this unit
  re-links those events **across days** (raw-space centroids, window-population centering) into
  threads, each with a per-day outlet curve (`2→7→6→7→5→8→5`) and a shape tag.
- **Input**: `--date` (window end, market day) · `--days` (default 7) · `--scope domestic|foreign|all`.
- **CLI** (client-only — GPU vector store; run `embed sync` first):
  ```bash
  python -X utf8 -m module_news_data thread --days 7 --scope domestic --top 25
  ```
  Read the **text view** (≈12k tokens at `--top 25`). ⚠ The `--json` file is 374KB / ~262k tokens —
  a machine artifact under `out/news_threads/`, NOT something to load into context.
- **Output**: per-day denominators, then **alive market threads** (BUILDING → REIGNITED → FADING;
  full timeline for the top N, one line each for the rest), ENDED top-10 + count, nonmarket +
  one-day counts. Tags are **count-curve shapes**, deterministic and reproducible.

⚠ **The alpha is the tail→head precursor.** Measured 2026-07-11→17 (domestic, 7d): the BOK
  rate-hike saga ran **07-11 [14 art/2 src] "금리인상 초읽기" → 07-16 [101 art/8 src] the hike** —
  five days of runway visible in the thread, invisible in any single day's brief (day 1 was tail).
  Twelve threads in that one window started at 2 outlets and peaked at 5+. When a thread's curve
  starts at 2 and climbs, the market is still pricing discovery — that is where early positioning
  lives. Conversely a thread already at its 5th day and peak outlets is **crowded**: you are late.
⚠ **Tags are curve shapes, not importance or direction** (P4). BUILDING says outlets grew; it does
  not say good/bad/tradeable. 최태원's "don't sell SK hynix" re-ignited 3→7 — whether that is support
  or distribution needs the tape + body reads ([drill_detail](drill_detail.md)).
⚠ **A holiday/low-volume window end mechanically inflates FADING.** Measured: 07-17 (제헌절) had
  185 articles vs 450+ weekday — last-day outlet counts sag with volume. Read the per-day
  denominator line before interpreting tags.
⚠ **ENDED is signal too**: it is the attention-rotation ledger. The KOSPI-crash saga (7→8→8) and the
  SK hynix US-debut saga (8→7→7→4→7) both ENDED mid-window — the market moved on. A position whose
  thesis rides a thread that just ENDED is holding yesterday's story.
⚠ One-day threads (incl. today's NEW events) are **the daily brief's job** — this unit only counts
  them. Run [daily_events](daily_events.md) for today's full coverage; run this for motion.
⚠ `--link-distance` 0.40 is a measured compromise (0.30 chops sagas into fragments; 0.50 absorbs
  recurring formats — a horoscope column threaded 7 days — and topic blobs). Same tradeoff family
  as the intra-day threshold in `_cluster`.
⚠ **Threads mix true sagas with theme bundles** — `_cluster`'s event-vs-topic limit, amplified
  across a week. Measured: the BOK saga is a real one-story arc; a 6-day "AI" BUILDING thread was
  government-AI + three unrelated corporate AI items. Still valid as theme momentum, but check the
  timeline titles share a subject before reading it as "one event ran 6 days".
