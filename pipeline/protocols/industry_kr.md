# PROTOCOL — industry_kr

> A protocol = an ordered composition of L1 blocks (references only). **Order is owned by this file**
> (L1 units are independent). Shares the **same L1s** as industry_us — only the composition differs.
> Purpose: identical funnel (macro → OW sectors → value chain).
> Output root `llm_outputs/{YYYY-MM-DD}/industry_KR/` — same file-output rules as industry_us
> (scripts' hardcoded paths are the single source: `kr_live_shortlist` reads `SECTOR_FLOW_KR.json`
> there; previous date folders read-only; filenames load-bearing; module scratch → `out/`).
> Runtime = `--market kr`.

## Composition (L1 order)

| # | L1 block | Output |
|---|---|---|
| 1 | [MACRO](../L1_stages/macro.md) | `MACRO_REPORT.md` |
| 2 | [SWEEP](../L1_stages/sweep.md) | `SECTOR_FLOW.json` · `KR_LIVE_SHORTLIST.json` |
| 3 | [ROTATION](../L1_stages/rotation.md) | `SECTOR_ROTATION.md` |
| 4 | [DEEP](../L1_stages/deep.md) | `SECTOR_DEEP_{code}.md` ×4 |
| 5 | [BET](../L1_stages/bet.md) | `BET_SHEET.md` |
| 6 | [ALPHA](../L1_stages/alpha.md) | `BET_SHEET §B` tags |

## KR runtime deltas (vs industry_us)
- **No PREMORTEM·DRIFT blocks** (6 stages). No CYCLE_EXPOSURE / ACTION_TICKETS.
- MACRO primary data: no FRED module for KR → cross-read the same-day US `MACRO_REPORT §A`,
  cited `[FRED via US-desk]`.
- News `--scope domestic` + `news_fts --kr` (trigram index — ⚠ 2-char Korean terms return 0
  (not absence); use 3+ char synonyms). Universe `kr_all` (KRX sectors).
- **KR's edge axis**: SWEEP·DEEP·BET use `module_KIS` per-investor net-buy actuals
  (✅ real-hands / ❌ weak-hands) — the measured "who is buying" the US desk lacks.

**Start → read [MACRO](../L1_stages/macro.md) and execute.** Pass each EXIT CHECK, finish with [handoff](../handoff.md).
