# L1 · MACRO — the macro axis (stage)

> Big stage. The entry stage **shared** by industry_us and industry_kr. Calls L2.
> Runtime: `--market us|kr`. Output: `MACRO_REPORT.md` under the protocol's output root
> (`llm_outputs/{date}/industry_{US|KR}/` — drift_watch's default read path expects exactly this).

## L2 called
- [schedule](../L2_modules/schedule.md) — **run-start catalyst injection**: `catalyst_calendar --days 5`.
  Any 🔀binary ≤48h (CPI/PPI/FOMC/NFP/major earnings) is recorded NOW — downstream PREMORTEM must
  bracket it both ways. ⚠ saves `CATALYST_WATCH.json` under the day folder root, not the desk subfolder.
- [indicators](../L2_modules/indicators.md) — US: FRED primaries via `module_macro_us --json`
  (⚠ always `--json`: the markdown view has KR headers; cite values `[FRED]`; monthly series
  (CPI/M2) lag ~1 month — say so instead of pretending freshness) + `us_flow --cot` positioning
  percentiles (≥80 crowded-long / ≤20 crowded-short; Tue-close data, 3–4d lag = context, not trigger).
  KR: cross-read same-day US MACRO_REPORT §A.
- [news](../L2_modules/news.md) — **event pass first, then the term sweep** (that L2 explains why they
  are different axes):
  1. **Events** (`brief`, run `embed sync` first) — the day's events with their denominator. Do this
     BEFORE the bucket sweep: the buckets can only find what you already thought to name, and a
     regime-moving event can sit at 1.3× term-share while 8 outlets scream it (measured: the
     KOSPI −8% circuit-breaker day ranked **nowhere** by term velocity). Read the head, and read the
     tail *count* — if a proposition claims "quiet", that number must support it.
  2. 7-bucket narrative sweep (FTS `--syn`, OR-mode per bucket, body-inclusive) — now targeted at the
     buckets, knowing what the day actually held.
  3. **blind-spot pass** (read `sample[]` rows RAW; a rank-jump of a single name is itself a signal →
     body-read before classifying; append confirmed new macro terms to the protocol's term table —
     the term set is living, never frozen).

- **Continuity anchor (DeGaJa-native — replaces the old mvp `insight_corpus` daily anchor):**
  read the PREVIOUS run's `llm_outputs/{prev date}/industry_{US|KR}/MACRO_REPORT.md` (propositions +
  addendums) and query the handoff ledger (`module_report_tags show`) for inherited coverage.
  The mvp daily-card corpus is NOT a dependency of this repo — if a prompt mentions a "daily anchor",
  this is what it means here.

## What this stage does
- Build falsifiable macro propositions (1–2 per bucket): anchor `[FRED]` > `[news]`, direction/prob
  both ways, **mandatory anti-signal**, track KPI, dated catalyst.
- → **★sector transmission matrix** (OW[…]/UW[…] per all 11 GICS + driving proposition ID) —
  THE deliverable; it is ROTATION's input. Do NOT analyze 11 sectors equally — set wind direction only.
- Self-backtest: score past +7/+14/+30d MACRO_REPORT propositions hit/half/miss and append a running
  hit-rate. ⚠ Recurring failure class to watch: banking a one-sided read of an *oscillating* regime
  variable (oil war-premium, headline-CPI wedge) — such propositions must carry BOTH branches.

## ✅ EXIT CHECK
- [ ] Catalysts injected; narrative (**events + 7-bucket + blindspot**) and indicators (primaries + positioning) read; daily anchor read.
- [ ] Every "nothing happened in bucket X" claim carries the event denominator that backs it (P4).
- [ ] Transmission matrix produced (all 11 sectors, one line each) — the downstream input.
- [ ] MACRO_REPORT.md written with primary numbers explicit; self-backtest hit-rate appended; new blind-spot terms folded back into the term table.
