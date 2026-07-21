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
  are different axes). ⚠ **Scope is market-locked**: KR desk = `--scope domestic`, US desk =
  `--scope foreign`, on EVERY news call here (`brief`·`thread`·fts·blindspot). Never let the KR
  feed rank the US frame — measured 787 rate hits : 0 US-bank hits in a US bank-earnings week.
  1. **Events** (`brief --body 2`, run `embed sync` first) — the day's events with their denominator.
     ⚠ **`--body 2` is mandatory here**: at the default the tail emits a random 10 and drops the rest.
     Measured 2026-07-17 — TSMC's ₩148tn fab expansion, 환율 1480원 + the 24h FX-market opening, and
     CXMT's HBM-moat bypass **all sat at 2 outlets = all invisible**, and all three are transmission-
     matrix input. Cost of seeing every event: +2.3k tokens.
     ⚠ **But do not read the head as noise, and do not rank events before you read the tape.** That
     same day's top item (최태원 "just hold SK hynix", 7 outlets) looks like a platitude and was in
     fact damage control after SK하이닉스 −11.53% the prior session — `brief` carries no prices, so it
     cannot tell you that. Pair this pass with the tape (PULSE / `module_flow`) before ranking.
     Do this BEFORE the bucket sweep: the buckets can only find what you already
     thought to name, and a regime-moving event can sit at 1.3× term-share while 8 outlets scream it
     (measured: the KOSPI −8% circuit-breaker day ranked **nowhere** by term velocity). Read **every**
     event line, not the head — if a proposition claims "quiet", the denominator must support it.
  1b. **Trajectories** (`thread --days 7`, same scope) — the day's events re-linked across the past
     week: BUILDING / FADING / REIGNITED / ENDED with per-day outlet curves. This is what makes
     propositions *dated*: a proposition built on a thread at day 5 of its peak is chasing a crowded
     story; one built on a 2-outlet climbing thread is early (measured: the BOK rate-hike saga ran
     `2→7→6→7→5→8` — five days of runway before the hike printed, invisible in any single brief).
     Use it three ways: (a) every macro proposition names its thread's tag + curve — "quiet" or
     "accelerating" claims must cite a trajectory, not a feeling; (b) an ENDED thread under a
     still-open proposition is a staleness flag — attention rotated, re-justify or drop it;
     (c) BUILDING threads with no matching bucket are candidate new terms for the living table.
     ⚠ Curve shapes are not importance (P4) — direction still needs body reads. ⚠ A holiday
     window-end inflates FADING; read the per-day denominator line first.
  2. 7-bucket narrative sweep (FTS `--syn`, OR-mode per bucket, body-inclusive) — now targeted at the
     buckets, knowing what the day actually held **and which way it is moving**.
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
- [ ] Catalysts injected; narrative (**events + trajectories + 7-bucket + blindspot**) and indicators (primaries + positioning) read; daily anchor read.
- [ ] Events read via `--body 2` (tail count = 0). A head-only read is a failed stage — the day's
      macro prints hide at 2 outlets.
- [ ] Trajectories read (`thread --days 7`): every proposition carries its thread's tag+curve (or
      states "no thread" explicitly); any ENDED thread under an inherited proposition is flagged.
- [ ] Every "nothing happened in bucket X" claim carries the event denominator that backs it (P4).
- [ ] **No bucket's 0/near-0 hit count is trusted until its terms were passed as separate argv.**
      A quoted multi-word bucket returns ~0 silently, and `coverage` calls that 🟢 양호 — "quiet" that
      came from a mis-passed CLI is a fabricated proposition, not an observation.
- [ ] Transmission matrix produced (all 11 sectors, one line each) — the downstream input.
- [ ] MACRO_REPORT.md written with primary numbers explicit; self-backtest hit-rate appended; new blind-spot terms folded back into the term table.
