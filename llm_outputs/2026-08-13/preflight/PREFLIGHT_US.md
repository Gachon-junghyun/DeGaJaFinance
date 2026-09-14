# PREFLIGHT — 2026-08-13 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-13 22:10–22:30 = ET 2026-08-13 09:10–09:30, Thursday PRE-OPEN**
> (US cash opens 09:30 ET). Sweep data **asof 2026-08-12** — last settled US close (Wednesday).
>
> ⚠ **Filename deviation, logged (4th consecutive run, same reason):** the composition table names this
> `preflight/PREFLIGHT.md`, but the `industry_kr` desk already wrote its rights table to that path this
> morning (08:32 KST). Overwriting a sibling desk's output is not a correction, so the US table is
> written as `PREFLIGHT_US.md` in the same folder. Human decision on permanent market-suffixing is
> still pending (PROMPT_MAP §6).

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** | Last bar **2026-08-12**, **settled** (last-bar volume / prior-20d avg, median **0.740**). Benchmark **SPY carries the 08-12 bar** → no re-dating, no split-endpoint RS. **This is the first US run in three where the clock is clean** |
| **G1** news axis alive | 🔴 **FAIL** | Coverage **17.0%** (51/300). **Not silence — the pipe.** Falsification probe **5/5 failed** (remote API `URLError`, local FTS **0 bytes**), while the client-side store holds **51,718** articles for 08-06→08-13 **including 476 `Nvidia` title hits** |
| **G2** scoring-scale continuity | 🟢 **PASS** | **3-axis (`nonews`) vs 3-axis (`nonews`)**, baseline **2026-08-11**, **300/300 names carry Δ**. Δ spans **exactly one settled session** (08-11→08-12) — the cleanest Δ this desk has had in a week |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **2 of 11** sectors (Industrials/`CAT` · Materials/`LIN`). Down from 3 on 08-12 |
| **G4** risk-unit stability | 🔴 **FAIL** | 250d **12 units** · 500d **10** · 750d **11** — all three windows disagree (**4th consecutive run**) |
| **G5** does the universe cover the book | 🔴 **FAIL** | **11/11 US holdings inside `us_top300` AND scored ✅** (`LNG`/`TSM` hole stays closed). But `us_top300.csv` is **29 days old** (limit ≤8) and **`EA` returned a null last bar** |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** | Measured ETA **79 days** vs ideal 31 = **2.6×** (limit 1.5×) |
| **G7** tool liveness | 🔴 **FAIL** | **41 entry points** probed, **2** non-zero `--help` (`scripts/margin_history.py` · `module_chart`) — **4th consecutive run unrepaired**. Both pass a functional probe ⇒ citation rights retained **for those command lines only** |

**PASS 3 / FAIL 5.** Best gate score this desk has posted (08-10: 1/6 · 08-12: 2/5).
**Today this desk cannot speak with news velocity, theme freshness, "it went quiet", a single
concentration number, or an `--ic`-derived size.** It *can* speak with settled prices, OBV, breadth,
RS (clean this run), short pressure, COT positioning, FRED series and primary filings.

---

## G0 · Bar completeness · date alignment — 🟢 PASS *(bonus gate)*

Not one of the seven. It is carried because the KR desk measured it into existence on 08-12 and it
**failed on both of the last two KR runs** — once as an intraday stub, once as a benchmark bar gap
that silently re-dated the whole run. Measured here so the absence is a measurement, not an assumption.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-13.pkl` (n=301 columns,
MultiIndex `Ticker`×`Price`) + `SECTOR_FLOW_US.json §asof`.

| Item | Value |
|---|---|
| Run clock | **09:10 ET Thu 08-13 — PRE-OPEN** (cash opens 09:30 ET) |
| Last index in the price frame | **2026-08-12** (Wednesday) |
| Last-bar volume / prior-20d average — median | **0.740** (q25 **0.614** · q75 **0.905**) |
| Benchmark `SPY` last three bars | 08-10 **773.03** · 08-11 **770.56** · **08-12 772.49 — present** |
| `SECTOR_FLOW_US.json §asof` | **2026-08-12** — matches the data's own last index |
| Non-null closes on the last row | **300 / 301** (one hole → G5) |

⇒ The last bar is a **full settled session**, not an intraday stub (the KR failure mode measured
**0.223**). The benchmark carries the same terminal date as the names, so `rs20 = ret(name,20) −
ret(bench,20)` has **matched endpoints** — the 08-13 KR failure (unhedged single-session return
riding into RS) **does not exist in this run**.

**✅ Rights RESTORED for this run** (both were revoked on the last KR run and on the 08-12 US run):
1. **RS20/RS60 may be compared at fine grain** — no split-endpoint contamination band.
2. **`vol_surge` may be read in both directions** — the last bar is complete, so a low reading is a
   low reading and not a clock artifact.
3. `asof 2026-08-12` may be written plainly as "data through the 08-12 close". No two-line date caveat.

---

## G1 · News axis alive — 🔴 FAIL *(the pipe, and it is now measurable how badly)*

**Commands**
- `SECTOR_FLOW_US.json §scoring` → `{"vel_axis": false, "vel_coverage": 0.17, "n_axes": 3, "scored": 300, "dropped_missing_axis": 0}`
- Sweep's own health line: `[axis] velocity 측정 51/300 = 17.0% → 속도축 제외(전원 3축) · 기준 80%` + the 🚨 line
- Falsification probe, actually run: `python -X utf8 -m module_news_data fts search <name> --days 7 --count --scope foreign`

| Probe (22:14 KST) | Result |
|---|---|
| Nvidia | ❌ `뉴스 API 접속 실패 … URLError(FileNotFoundError(2))` |
| Broadcom | ❌ same |
| Marathon Petroleum | ❌ same |
| Eaton | ❌ same |
| Nucor | ❌ same |

**5/5 failed on the remote bridge.** Local fallback probed separately with `DEGAJA_NEWS_API=` →
**5/5 `색인 없음 — 먼저 fts build 실행`**. Both bridges are down:

| Bridge | State |
|---|---|
| Remote (`…ngrok-free.dev/exec`) | **unreachable** — `URLError`. ⚠ It was **alive at 08:40 KST this morning** (KR desk logged 5/5 successes via this exact tunnel). It died during the trading day |
| Local `data/news_fts.db` | **0 bytes** (mtime 2026-08-12 10:51) |
| Local `data/news_fts_kr.db` | **0 bytes** (mtime 2026-07-30) |

### ★ The decisive measurement: is it silence, or is it the pipe?

The client-owned derivative store `data/news_vectors.db` (1.02 GB, mtime **2026-08-13 09:15**) was
queried directly — it does not go through the FTS index or the remote API, so it is an independent
witness to whether articles exist at all:

| Date | Articles in client store |
|---|---|
| 2026-08-06 | 9,248 |
| 2026-08-07 | 8,330 |
| 2026-08-08 | 3,341 |
| 2026-08-09 | 3,887 |
| 2026-08-10 | 8,696 |
| 2026-08-11 | 9,095 |
| 2026-08-12 | 8,757 |
| 2026-08-13 (partial) | 364 |
| **7-day total** | **51,718** |

Title-string hits in that same 7-day window: **`Nvidia` 476** · **`Fed` 592** · **`CPI` 292** ·
**`PPI` 207** · **`tariff` 150** · **`Broadcom` 56** · **`Eaton` 20** · `Marathon Petroleum` 2 · `Nucor` 1.

⇒ **The corpus is alive and large. The desk's ability to read it is dead.** `Nvidia` returns
**476 titles** from the store and **an error** from the desk's own search path. This is the exact
class the preflight protocol exists for: the number that would have been reported (17% coverage)
describes **the tunnel**, not the world.

⚠ Note what the sweep did **right**: it scored all 300 names on **3 axes uniformly** and printed the
🚨 line. The 2026-08-09 defect (per-name axis dropping worth up to **+0.5**, inflating 799 of 827
names by an average **+0.305**) **did not recur** — `dropped_missing_axis: 0`.

**🚫 Rights revoked today**
1. **No citation of news velocity** in any stage (SWEEP · EVENT_ALPHA · ROTATION · DEEP · BET).
   The 51 names that *did* return are a **non-random survivor sample** (they survived a failing
   tunnel) — they are not usable either.
2. **No "this theme is fresh / this theme has cooled" verdict.** `theme_age`, `chain_hop` and
   `drift_watch` outputs are **not citable** — they ride the same transport.
   ⚠ **This binds stage 11 (DRIFT) directly**: DRIFT must state that its instrument was dead rather
   than report an empty burst list as "no drift".
3. **"It has gone quiet" is forbidden as evidence.** Measured: 51,718 articles exist in the window
   the desk reads as 83% empty.
4. `flow_score` is a **3-axis score** — that fact goes on the **same line** as any conclusion drawn
   from it, every time.
5. ⚠ **The inverse is equally forbidden** — "the news axis is dead, therefore there is no news" is
   the same error with the sign flipped. If a stage needs a news fact today it must come from a
   **named primary source with a URL/date on that line** (filing, FRED release, exchange notice),
   not from the desk's search layer.

---

## G2 · Scoring-scale continuity — 🟢 PASS *(and the baseline is finally adjacent)*

**Command** `§scoring.n_axes` vs `llm_outputs/sector_flow/history.json` previous snapshot `_mode`

| Snapshot key | `_mode` | Note |
|---|---|---|
| 2026-08-05 | news (4-axis) | |
| 2026-08-06 | news (4-axis) | last 4-axis run |
| 2026-08-07 | nonews (3-axis) | |
| 2026-08-11 | nonews (3-axis) | ← **today's Δ baseline** |
| **2026-08-12** | **nonews (3-axis)** | ← **this run's saved key** (run date 08-13, asof 08-12) |

Axis count matches (3 = 3) ⇒ **PASS**, and **300/300 names carry a Δ**. No apples-to-oranges subtraction.

★ **What is better than the last two runs**: the baseline is **2026-08-11**, i.e. Δ spans **exactly one
settled trading session**. The 08-12 US run compared across **two** sessions; this morning's KR run
compared across **four calendar days** because a benchmark gap re-dated its key backwards. Today
"Δ vs prior session" is literally true.

⚠ **Standing caveat, unchanged**: this is a **3-axis** Δ on both sides. It measures price/OBV/RS
rotation only. A name whose entire change is narrative is **invisible in this Δ by construction**.

---

## G3 · Who owns the sector sign — 🟢 PASS

**Command** `§sector_rotation[].top1_flips_sign` — the list must be printed (zero entries still PASS)

**2 of 11** sectors flip sign when their single largest name is removed. Printed in full:

| Sector | wflow | ex-top1 | top1 | top1_w | n |
|---|---|---|---|---|---|
| Industrials | **−0.002** | **+0.055** | `CAT` Caterpillar | 8.7% | 50 |
| Materials | **−0.106** | **+0.115** | `LIN` Linde | 24.7% | 12 |

Down from **3** on 08-12 (Financials/`BRK-B` dropped out).

⚠ Read this correctly: a sign flip only appears when the sector's weighted flow is **sitting on
zero**. Industrials at **−0.002** is not a bearish sector — it is a sector with **no aggregate signal
at all**, where one name's rounding decides the sign. Fewer flippers is **not** "improved
concentration."
⚠ `top1_w` weights come from a **29-day-old market-cap file** (G5).

**Binding**: **Industrials and Materials may not be promoted or demoted on `wflow`** (ROTATION §2).
Use `eqflow` / `breadth` — both of which, note, point the **opposite way** from `wflow` in both
buckets — or hold the call.

---

## G4 · Risk-unit stability — 🔴 FAIL (4th consecutive run)

**Command** `python -X utf8 scripts/risk_units.py --book --days {250,500,750}` — **all three actually run**

| `--days` | Units | Window | In-group resid. corr | ARI (1st half vs 2nd) | Max resid. corr |
|---|---|---|---|---|---|
| 250 | **12** | 2025-07-25 → 2026-08-12 (249 bars) | +0.8525 | 0.3874 | +0.8525 |
| 500 | **10** | 2024-06-28 → 2026-08-12 (499 bars) | +0.5244 | **0.2041** | +0.8464 |
| 750 | **11** | 2023-06-08 → 2026-08-12 (749 bars) | +0.5944 | 0.3810 | +0.8217 |

**No two windows agree.** The book is 13 names; the disagreement is entirely about two pairs:

| Pair | 250d | 500d | 750d |
|---|---|---|---|
| `AVGO` · `NVDA` | **separate** | **merged** | **merged** |
| `ANET` · `ETN` | separate | **merged** | separate |

The tool flags the `ANET·ETN` merge itself: *"two different theme labels inside one measured unit —
`MAX_THEME_PCT` is counting this as two."* i.e. the book's label taxonomy (`AI-compute-EPICENTER`
vs `AI-power/electrical`) and the **measured** co-movement structure disagree at the 500d window.
The tool also warns at all three windows that stability moves **opposite** to fit (S5), and that
mixing KRW- and USD-denominated returns can inject a common FX factor.

**🚫 Rights revoked today**
1. **No single-number concentration guard** in BET/SIZE.
2. Any concentration statement must carry **the `--days` window on the same line as the conclusion**.
3. **No verdict today on whether `AVGO`+`NVDA` are one unit or two** — the window picks the answer,
   and 2 of 3 windows say one. Same for `ANET`+`ETN` (1 of 3 says one).

---

## G5 · Does the universe cover the book — 🔴 FAIL *(on staleness only; coverage is clean)*

**Command** `data/us_universe/us_top300.csv` × `module_paper_book status` holdings × scored-name set

| Item | Value |
|---|---|
| Book holdings | **13** (US 11 · KR 2) |
| US holdings inside `us_top300` | **11 / 11 ✅** — ANET · AVGO · ETN · HPE · MET · MPC · NDAQ · NUE · NVDA · PSX · RTX |
| US holdings actually **scored** by the sweep | **11 / 11 ✅** (verified against `§names`, not just the CSV) |
| ★ `LNG` · `TSM` outside-universe hole | **still closed** — neither is held (was logged 12 consecutive runs) |
| `us_top300.csv` age | **29 days** (mtime 2026-07-15, limit **≤8**) → 🔴 |
| Universe size | 300 requested / **300 scored** |
| ⚠ **Null last bar** | **`EA`** — 300 of 301 columns have an 08-12 close; `EA` has none |
| Rebuild candidate | `data/us_universe/us_all_v2_candidate.csv` (2026-08-10) **exists, unpromoted** — promotion is a human decision (P5) |

Sweep log line 1: `[warn] 유니버스 us_top300.csv 29일 경과 — 시총 stale.`

**🚫 Rights revoked today**
1. **`wflow` may not be described as "current market-cap weighted"** — the weights are **29 days
   old**. Every `top1_w` in G3 inherits this.
2. **No flow / RS / OBV / short verdict on `EA`** — it was not measured. Absence of a bar is not
   absence of a move.
3. ✅ **Positive update, second run running**: every name the book holds can be tagged by every
   instrument the desk uses. There are **zero** "held but unmeasurable" names.

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL

**Command** `python -X utf8 scripts/snapshot_estimates.py --status`

| Item | Value |
|---|---|
| Accumulated | **9 files / 23 calendar days** (2026-07-22 → 2026-08-13, today's included) |
| Measured rate | **0.39 files/day** (ideal 1.0) |
| To the 40-day target | ideal **31 days** vs measured **≈79 days** = **2.6×** (limit 1.5×) |
| Gaps (days) | [2, 3, 4, 6, 3, 1, 2, 1] · median 3 · max 6 |

Unchanged from this morning's KR reading (2.6×, down from 2.75× on 08-12). Today's file did land.
Not recoverable retroactively — days not captured are gone.

**🚫 Rights revoked today**
1. **No reporting of `kelly_size --ic` output as an evidence-backed size.**
2. Any size written today is labelled **"mechanical ¼"**.

---

## G7 · Tool liveness — 🔴 FAIL (2 of 41 · 4th consecutive run, same two)

**Command** `--help` on every entry point this run will use; exit code recorded.

**exit 0 — 39**: `sector_flow` · `us_live_shortlist` · `us_flow` · `flow_read` · `exposure_rule` ·
`missed_ledger` · `reject_ledger` · `kelly_size` · `catalyst_calendar` · `report_lint` · `risk_units` ·
`axis_window_flow` · `snapshot_estimates` · `ic_ledger` · `leak_scan` · `axis_inflection` ·
`cycle_exposure` · `drift_watch` · `us_setup_screener` · `action_bracket` · `handoff_id_audit` ·
`handoff_compact` · `yf_snapshot` · `brief_recall` · `module_news_data` · `module_KIS` ·
`module_valuation` · `module_report_tags` · `module_disclosure_us` · `module_fundamentals_us` ·
`module_business_us` · `module_paper_book` · `module_macro_us` · `module_industry_map` ·
`module_flow` · `module_watchlist` · `module_epistemics` · `module_inflection` · `module_math_check`
*(+`module_publish` exit 0 — 41 probed in total)*

**exit 1 — 2** (identical to 08-10 · 08-12 · this morning's KR run)

| Tool | `--help` failure | Functional probe (rule 3) |
|---|---|---|
| `scripts/margin_history.py` | exit 1 — `%`-format bug in the help string (argparse `_expand_help`) | `margin_history.py NVDA` → **exit 0**: gross margin FY2009–FY2026, **18 periods**, high **FY2025 75.0%** · low **FY2009 34.3%** · **median 56.9%** · FY2026 **71.1%** on **$215.9B** |
| `module_chart` | exit 1 — CLI does not implement `--help` (prints usage, exits 1) | `module_chart NVDA --read` → **exit 0**: OBV neutral (20d slope +12%) · no divergence · bull stack 5>20>60>120, price above 4/4 MA · Bollinger expansion 18.8%, upper band · RSI 61.4 · turn verdict **BREAKOUT** |

⇒ Under rule 3 both were **actually run and produced correct output** ⇒ **citation rights retained**,
but the warrant is the **probe output above**, not `--help`, and only for **those two command lines**.
⚠ A broken `--help` means a human cannot discover the tool. **Logged unrepaired for the 4th run.**

---

## What this table binds today (handed to HANDOVER)

| Stage | Cannot use today |
|---|---|
| SWEEP | news velocity · theme freshness · "quiet" · stale mcap described as current · any verdict on `EA` |
| EVENT_ALPHA | "theme is fresh/cooled" · `theme_age` / `chain_hop` outputs · any velocity-derived forward card |
| ROTATION | **`wflow` promotion/demotion for Industrials and Materials** (G3 flippers) · news-axis tie-breaks |
| PREMORTEM | "the tape has gone quiet on this risk" — the tape is unreadable, not quiet |
| DEEP | news velocity · "no news flow" as evidence of anything |
| BET / SIZE | single-number concentration · `--ic`-backed size (→ **"mechanical ¼"**) · `AVGO/NVDA` unit count |
| DRIFT | **must report that `drift_watch`'s instrument was dead** — an empty burst list today is not "no drift" |

**What this desk CAN speak with today (stated positively).**
① **Settled prices through 2026-08-12** — and, uniquely this run, **RS at fine grain** (G0 restored it).
② **OBV level and state** — last bar complete.
③ **eqflow · breadth** — unweighted, so 29-day-stale caps barely touch them; with news dead these
   carry more load, not less.
④ **`vol_surge` in both directions** (restored by G0).
⑤ **FINRA short pressure · CFTC COT percentile positioning** — the US substitute for the investor-type
   feed. Context, never a trigger.
⑥ **FRED macro series** (`module_macro_us`, cite `[FRED]`).
⑦ **Primary filings** (`module_disclosure_us` / `module_fundamentals_us`) and **margin history**.
⑧ **Hand-cited individual news facts with a named source and date on the line** — the search layer is
   dead, the world is not (51,718 articles exist in the 7-day window).

**Speak with settled prices, breadth, positioning and primary documents. Do not speak with the
news axis, theme age, or a single concentration number.**

*Instrument state is not a market view — this document is not written into `handoff/` (HANDOVER only reads it).*
