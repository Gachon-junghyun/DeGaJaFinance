# L1 · MACRO — the financial environment, its transmission to earnings, and the focus sectors (stage)

> Big stage, shared by industry_us and industry_kr (`--market us|kr`). First analytical stage after HANDOVER.
> Absorbs ROTATION (2026-10-31): the sector verdicts and the focus-sector pick are made here, once.
> **Reads (primary sources)**: FRED series (`module_macro_us --json`), Treasury/oil/FX/credit levels, the catalyst
> calendar, the day's event list. News explains a move; it does not measure one.
> **Output**: `MACRO_REPORT.md` (filename load-bearing — `drift_watch` reads it) — **cap 14 KB**.
> **Next stages use**: §2 transmission lines (EARNINGS asks the named companies for the exposure number),
> §3 sector verdicts + focus sectors (EARNINGS and COMPETITION scope), §4 dated catalysts (PREMORTEM, ALPHA).

## Why the order is data-change first (measured)
On days when the US 10-year moved **±10bp** the S&P's absolute day return was **1.98×** normal (**±15bp: 3.02×**),
WTI **±5%: 2.08×**, the dollar **±0.7%: 2.21×** (`lab/NEWS3D_20261030.md` E2). Macro read as **the size of a data
change** moves prices; macro read as a narrative bucket scored 0.38 in the lens ledger. And the old desk used
macro only as a *sector price factor* (e.g. «10y up ⇒ FIN/UTIL/RE/STPL UW») and never sent it down to a
company's earnings — bank NIM, exporter FX, refiner/airline fuel (K1 §3, question ⑤: 0 of 6 runs).

## L2 called
- [schedule](../L2_modules/schedule.md) — catalyst injection: `catalyst_calendar --days 5`, widen to `--days 10`
  when a lens question settles beyond the window. Any binary ≤48h is recorded now (PREMORTEM brackets it).
  KR: front-month futures expiry from `module_KIS --futboard` (`days_left` ≤ ~5 ⇒ register as a binary).
- [indicators](../L2_modules/indicators.md) — US: `module_macro_us --series … --days 120 --json` (always
  `--json`; cite `[FRED]`; monthly series lag ~1 month, say so) + `us_flow --cot` (context, Tue close, 3–4d lag).
  KR: cross-read the same-day US `MACRO_REPORT.md §1` cited `[FRED via US desk]`, plus KRW and KTB 3y/10y
  (no owning module — yfinance `KRW=X` or the print in `brief`'s `single_source`, source stated) and
  `module_KIS --futboard` basis/OI (positioning context, not a trigger, not directional).

## What this stage does

### §1 The change table — measure before you narrate
One row per series: `level · 1-day Δ · 5-day Δ · 20-day Δ · percentile of |Δ| in its own 1-year history · asof`.
Series: US 2y/10y, `real_10y` **with** `breakeven_10y`, fed funds path, DXY (KR: KRW/USD), WTI/Brent, `hy_oas`
(+ `ig_oas`, `nfci` when a proposition touches financial conditions), VIX. Flag every row whose move clears the
measured thresholds above (10y ±10bp, oil ±5%, dollar ±0.7%) — those are the regime-relevant days.
- ⚠ Credit stress / risk-off claims cite `hy_oas` or `nfci` or are labelled **narrative-only**. Measured
  2026-07-21: a «credit surprise stack» was built from narrative while HY OAS sat 6bp off its 1-year low.
- ⚠ Cite both halves of every print (C2), on like-for-like windows. Measured: KR chip exports +180.6% YoY while
  the 1–20th window was −11.3% MoM.
- ⚠ Name the benchmark inline on every relative-performance number (C1): 005930 was −12.1% vs SPY and +10.1% vs
  `^KS11` over the same 20 days. No statistical result crosses markets without its own replication (W1).

### §2 Transmission to earnings — not to sector multiples
Write 3–6 propositions, each: `data change (§1 row) → mechanism → which line of which companies' P&L → sign and
rough size → the exposure number EARNINGS must fetch (e.g. NIM sensitivity, % USD revenue, fuel share of cost,
floating-rate debt share) → dated observable that falsifies it → the opposite branch`.
A proposition with no company exposure number named is labelled **«price-factor only»** and may not drive a
sector verdict alone. Oscillating variables (oil war premium, headline-CPI wedge) always carry both branches.

### §3 Sector verdicts and the focus sectors (was ROTATION)
- One line per GICS sector (KR: KRX sector): `OW | N | UW · driving proposition ID · earnings direction if known`.
  Do not analyse 11 sectors equally — set the wind; prose only for sectors that changed since the prior report.
- **A verdict change must carry an earnings, competition or macro-transmission reason.** Flow may confirm it
  later (FLOW_CHECK); a flow number alone does not move a verdict. (The old rule «a delta must be carried by a
  flow number» is retired — it made earnings and guidance changes formally unable to move a verdict.)
- **Focus-sector rule — never by gut.** N is owned by the protocol (US 4, KR 2; default 4 if absent).
  ① continuous ⌈N/2⌉ = top OW ranks; a sector that held a continuous slot last run and is still top-N OW keeps it.
  ② rotating ⌊N/2⌋ = next-highest OW not focused in the last ~3 runs (read prior `DEEP_LOG` lines — in
  `MACRO_REPORT.md` from 2026-10-31, in `SECTOR_ROTATION.md` before); if all recently covered, say «recency-starved».
  Never pad with N/UW. Name the OW sectors left without a slot.
- Append `## DEEP_LOG {date}: continuous=[…] rotating=[…] unslotted_OW=[…]`.

### §4 Events, briefly — the «why» behind §1, and the dated calendar
- `python -X utf8 -m module_news_data embed sync` then `brief --body 2` and `thread --days 7`, scope market-locked
  (KR `--scope domestic`, US `--scope foreign`, every call; measured 787 rate hits : 0 US-bank hits when the KR
  feed ranked the US frame). Read the three recovery sections — `single_source` (FX and rate prints live there),
  `excluded_nonmarket` boundary band, `subevents` — and quote their counts; measured 2026-07-23: with tail = 0,
  45.6% of the day was still unseen. Quote the denominator after `excluded_not_news`.
- `brief` has no prices: pair an event with the day's index move before ranking it. FTS terms are separate argv
  (a quoted bucket silently returns ~0); KR trigram needs 3+ chars. «Quiet» claims cite what was still withheld.

### §5 Self-backtest and continuity
Read the previous run's `MACRO_REPORT.md` (and its drift addendum if any). Score past +7/+14/+30d propositions
hit/half/miss and append the running hit rate. Lens questions this report registers are cited by Q ID.

## ✅ EXIT CHECK
- [ ] §1 change table present with 1/5/20-day Δ and own-history percentile; threshold-clearing rows flagged.
- [ ] `hy_oas` read (credit claims cite it or are narrative-only); `real_10y` quoted with `breakeven_10y`.
- [ ] **Every §2 proposition names a P&L line and the company exposure number EARNINGS must fetch**, a dated
      falsifier and the opposite branch — or is labelled «price-factor only».
- [ ] §3 one line per sector; every changed verdict states its earnings/competition/transmission reason.
- [ ] Focus sectors picked by the rule at the protocol's N; unslotted OW named; DEEP_LOG appended.
- [ ] Events read with `--body 2`, recovery-section counts and corrected denominator quoted; scope market-locked.
- [ ] Both halves of every print; benchmark named on every relative number; no cross-market transfer.
- [ ] Self-backtest hit rate appended; `MACRO_REPORT.md` ≤ 14 KB.
- [ ] Linter run: `python -X utf8 scripts/report_lint.py <file>` (form only — C1 · C2 · S6 · D6).
