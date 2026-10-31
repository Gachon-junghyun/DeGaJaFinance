# L1 · FLOW_CHECK — does the money agree? (stage, short)

> Big stage (replaces SWEEP, 2026-10-31). Runs **after** EARNINGS and COMPETITION, before BET. One pass.
> **Role: confirm or contradict a conclusion that already stands on earnings, competition or macro evidence.
> A flow reading cannot carry a conclusion by itself, cannot admit a name, and cannot veto a removal.**
> **Reads**: the sweep JSON (`SECTOR_FLOW_{US|KR}.json`), the shortlist JSON, per-name flow tags, (US) cycle exposure.
> **Output**: the JSONs (filenames load-bearing) + `FLOW_CHECK.md` — **cap 4 KB**.
> **Next stages use**: BET takes one agree/disagree line per name and per focus sector; ALPHA takes positioning
> for finalists.

## Why it is short (measured)
- The lens ledger's first learning: flow evidence right **5 of 32 (0.18)**; the worst method, «weighted vs equal
  flow against breadth/volume thresholds», **0 of 7**. M224 graded all four sweep axes inside the noise band.
- In the old order the sweep ran first and its 🟢 tag was the candidate entrance, the rotation-delta currency,
  the removal veto and the KR promotion gate (K1 §5 rows 1–4, 9–13). Each of those gates is removed.

## L2 called
- [discovery](../L2_modules/discovery.md) — `sector_flow --market us|kr --json` → then, serially (it reads today's
  JSON), `{us|kr}_live_shortlist` → (US) `cycle_exposure --json`.
- [indicators](../L2_modules/indicators.md) — `module_flow <tickers…> --bench SPY|^KS11 --json` for the BET
  candidates (KR: `.KS` suffix — a bare code returns empty rows without error; `--names` adds investor actuals).
  Grade every reading before using it (D6 table in indicators: RS20/60 A · KIS investor actuals B, confirmation only · **OBV and the 🟢 tag built on it C**).

## What this stage does
1. **Instrument health first** — quote `json.scoring` (`n_axes` · `vel_coverage` · `dropped_missing_axis`). Below
   80% coverage the file says «news axis dead this run» after probing the pipe
   (`python -X utf8 -m module_news_data fts search 삼성전자 --days 7 --count`). Measured 2026-08-10: a per-name
   dropped axis inflated 799 of 827 names by **+0.305**; `clip(nan)` scored a missing axis **+1.0**; the KR sweep
   queried the foreign pool for Korean names. Scores from different `n_axes` are never compared or differenced.
2. **One-name buckets** — list every sector with `top1_flips_sign` with `top1` and `top1_w`. Measured on KR: 10 of
   26 sectors flip sign without their largest name (전기·가스: 한국전력 79.9%). A flipper's `wflow` is one company;
   cite `eqflow`/breadth or nothing. Concentration is not a flip (삼성전자 45.6% of 전기·전자, no flip).
3. **Held-but-not-in-universe** — any owned name outside the universe is a 🚨 (measured: `TSM`, `LNG` invisible
   for 9 runs). Write «not measurable», never «no flow».
4. **Agree / disagree** — one line per focus sector and per BET candidate:
   `conclusion (from EARNINGS/COMPETITION/MACRO) · flow reading (grade, asof) · agrees | disagrees | not measurable`.
   A disagreement is a question for BET, not a verdict. A new 🟢 ignition outside the focus sectors is a question
   for the next run's EARNINGS, not a promotion.
5. **Shortlist names** are handed to the **next run's** EARNINGS as candidates tagged `flow` (this run's EARNINGS has
   already run; they reach BET only with the four numbers).
6. (US) Cycle-exposure GAP: any 🚨 goes to BET's epicenter-starter note; a 🔴 tape gates ADD timing only.
- The sweep is as of the previous close; a same-day catalyst is not in it.

## ✅ EXIT CHECK
- [ ] `scoring` block quoted; coverage <80% probed and diagnosed (pipe vs quiet).
- [ ] Flipper list written in full (0 is written as 0).
- [ ] Held-but-not-in-universe check run.
- [ ] One agree/disagree line per focus sector and candidate, each with a graded reading and asof — **no line
      states a conclusion that has no earnings, competition or macro reason beside it.**
- [ ] `FLOW_CHECK.md` ≤ 4 KB and contains no table that exists in the JSONs.
