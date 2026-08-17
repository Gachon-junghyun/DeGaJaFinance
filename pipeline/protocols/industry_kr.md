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
| −1 | [INSTRUMENT_CHECK](../L1_stages/instrument_check.md) ★preflight | `preflight/PREFLIGHT.md` — 7 gates; **a FAIL removes a citation right for this run** (protocol [preflight](preflight.md)) |
| 0 | [HANDOVER](../L1_stages/handover.md) | `HANDOVER.md` (inherited standing view + scenarios scored + dig list) |
| 1 | [MACRO](../L1_stages/macro.md) | `MACRO_REPORT.md` |
| 2 | [SWEEP](../L1_stages/sweep.md) | `SECTOR_FLOW.json` · `KR_LIVE_SHORTLIST.json` |
| 3 | [EVENT_ALPHA](../L1_stages/event_alpha.md) | `EVENT_ALPHA.md` (forward cards: building threads × money flow) |
| 4 | [ROTATION](../L1_stages/rotation.md) | `SECTOR_ROTATION.md` |
| 5 | [DEEP](../L1_stages/deep.md) | `SECTOR_DEEP_{code}.md` **×2** |
| 6 | [BET](../L1_stages/bet.md) | `BET_SHEET.md` |
| 7 | [ALPHA](../L1_stages/alpha.md) | `BET_SHEET §B` tags |

## DEEP budget — **N = 2** (1 continuous-track + 1 rotating)

ROTATION reads this line to size its selection rule (the L1 owns the *rule*, this protocol owns *N*;
`industry_us` keeps N=4). Cut from 4 to 2 on **2026-07-31**, on measurement, not taste:

- The 07-31 run spent roughly **710k sub-agent tokens** producing sector theses — the part of this
  desk's output that **cannot be verified at the rate it is produced.** Stock selection yields
  ~10–20 independent observations *per year*, so significance on it is arithmetically out of reach
  (rule C4). Exposure yields one observation *per session*.
- The desk's own decomposition the same week: of a **+16.86pp** lead, **~14pp was cash weight** and
  selection contributed **+2.54pp carried by a single name** — i.e. indistinguishable from zero.
- And the main sweep instrument had **already been graded negative**: M224 measured all four sweep
  axes (`flow_score`·`obv_norm`·`vol_surge`·`rs20/60`) against next-session residuals at
  **ρ −0.21~+0.19, n=22** against a p=0.05 threshold of **|ρ|=0.43** — every axis inside the noise
  band, and the desk kept using them anyway.

⇒ **The budget moves to the layer that can be scored** (`scripts/exposure_rule.py` ledger +
`scripts/missed_ledger.py`). This is deliberately *not* an attempt to predict better; it is a
decision to stop paying for predictions no one can grade.
⚠ **What this gives up, stated plainly**: two fewer sectors get a value-chain map each run. The
guard is that ROTATION must **name the un-slotted OW sectors in DEEP_LOG** — coverage that shrinks
must shrink *visibly* — otherwise "we never looked" and "we looked and passed" leave identical
evidence, which is the asymmetry `missed_ledger` exists to close.
⚠ **This guard originally cited a measured leak ordering ("retention, not discovery"). That citation
is withdrawn (2026-07-31)** — re-scoring the same window over a longer horizon inverted it
(`B.커버리지소실` went from **+1.93pp worst** to **−4.68pp best**). The guard stands on its own logic;
it does not stand on that number, and it should not be re-argued with a fresh single-window mean.

## KR runtime deltas (vs industry_us)
- **No PREMORTEM·DRIFT blocks** (7 stages). No CYCLE_EXPOSURE / ACTION_TICKETS.
- MACRO primary data: no FRED module for KR → cross-read the same-day US `MACRO_REPORT §A`,
  cited `[FRED via US-desk]`.
- News `--scope domestic` + `news_fts --kr` (trigram index — ⚠ 2-char Korean terms return 0
  (not absence); use 3+ char synonyms). The event axis (`brief`/`thread`) is also
  `--scope domestic` — market/non-market classification only works there anyway. Universe `kr_all`
  (KRX sectors).
- **KR's edge axis**: SWEEP·DEEP·BET use `module_KIS` per-investor net-buy actuals
  (✅ real-hands / ❌ weak-hands) — the measured "who is buying" the US desk lacks.
- **The valuation axis stands on one leg here, and the file must say which** (D70/D120, measured
  2026-08-03). DEEP's EXIT CHECK asks every "cheap on forward multiple" claim for **two** legs:
  (i) where margin sits in that name's own history, (ii) the estimate-revision trend.
  - **(i) now exists for KR** — `python -X utf8 scripts/margin_history.py <6자리>`
    (`--quarterly` for the 3-month series). DART 전체재무제표; measured on 042700 and 005930 as
    **11/11 fiscal years FY2015–FY2025, zero gaps**, and 042700 quarterly at **42/48 periods
    2015Q1–2026Q1**. ⚠ It is **undefined, not broken, for financials and cost-by-nature filers** —
    measured: 105560·086790 carry no revenue account at all, 035420 carries revenue but no 매출원가.
    Those names return a blank series with the reason, and a margin percentile is simply unavailable.
  - **(ii) does not exist for KR.** `module_fundamentals_us §추정치 모멘텀` and
    `scripts/snapshot_estimates.py` are both yfinance/us_top300 — there is no KR consensus-revision
    history in this repo, and none is being built. ⚠ **Naver's 컨센 목표주가 상승여력 is not a
    substitute** — it is someone else's estimate of price, not our measurement of the denominator.
  ⇒ A KR "cheap" verdict is written **with the margin percentile and an explicit
  `[revision leg: unavailable — KR]` tag**. Without that tag the claim reads as if both legs passed,
  which is the silent-pass this delta exists to stop. Strategy consequence, stated plainly:
  **KR value claims are half-powered by construction; momentum and flow carry the rest of the load.**

**Start → read HANDOVER (stage 0) first, then MACRO, and execute.** Pass each EXIT CHECK, finish with
[handoff](../handoff.md) for the tag ledger — and write the analytical carry back to `handoff/*.md`
per the HANDOVER stage. The two are different objects: the ledger records *what was covered*, the
carry records *what we believe, what we pre-committed to, and what we retracted*.
