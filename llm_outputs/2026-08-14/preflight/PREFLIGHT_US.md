# PREFLIGHT — 2026-08-14 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-14 22:10–22:40 = ET 2026-08-14 09:10–09:40, Friday PRE-OPEN**
> (US cash opens 09:30 ET). Sweep data **asof 2026-08-13** — last settled US close (Thursday).
>
> ⚠ **Filename deviation, logged (5th consecutive run, same reason):** the composition table names this
> `preflight/PREFLIGHT.md`, but the `industry_kr` desk already wrote its rights table to that path this
> morning (08:34 KST). Overwriting a sibling desk's output is not a correction, so the US table is
> written as `PREFLIGHT_US.md` in the same folder — the documented practice on 08-10 · 08-12 · 08-13.
> Human decision on permanent market-suffixing is still pending (PROMPT_MAP §6).

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** | Last bar **2026-08-13**, **settled** (last-bar volume / prior-20d avg, median **0.732**). Benchmark **SPY carries the 08-13 bar** (777.88) → no re-dating, no split-endpoint RS. **Second consecutive clean US clock** |
| **G1** news axis alive | 🔴 **FAIL** | Coverage **17.0% (51/300)** — **identical to yesterday**. Falsification probe **5/5 failed** (remote `URLError`, local FTS **0 bytes**), while the client-side store holds **42,192** articles for market-days 08-08→08-14 including **439 `Nvidia` title hits**. **The pipe, not silence** |
| **G2** scoring-scale continuity | 🟢 **PASS** | **3-axis (`nonews`) vs 3-axis (`nonews`)**, baseline **2026-08-12**, **300/300** names carry Δ. Δ spans **exactly one settled session** (08-12→08-13) |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **3 of 11** sectors (IT/`NVDA` · Health Care/`LLY` · Materials/`LIN`). **Up from 2**, and the new entrant is the desk's largest sector |
| **G4** risk-unit stability | 🔴 **FAIL** | 250d **11 units** · 500d **10** · 750d **10** — 500 and 750 agree, **250 does not** (**5th consecutive run**) |
| **G5** does the universe cover the book | 🔴 **FAIL** | **11/11 US holdings inside `us_top300` AND scored ✅**. But `us_top300.csv` is **30 days old** (limit ≤8) and **`EA` again returned a null last bar** |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** | Measured ETA **72 days** vs ideal 30 = **2.4×** (limit 1.5×) |
| **G7** tool liveness | 🔴 **FAIL** | **46 entry points** probed, **2** non-zero `--help` (`scripts/margin_history.py` · `module_chart`) — **5th consecutive run unrepaired**. Both pass a functional probe ⇒ citation rights retained **for those command lines only** |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate).
**Today this desk cannot speak with news velocity, theme freshness, "it went quiet", a single
concentration number, or an `--ic`-derived size.** It *can* speak with settled prices through the
08-13 close, RS at fine grain, OBV, breadth, `vol_surge` in both directions, FINRA short pressure,
CFTC COT positioning, FRED series and primary filings.

---

## G0 · Bar completeness · date alignment — 🟢 PASS *(bonus gate)*

Not one of the seven. Carried because the KR desk measured it into existence on 08-12 and it has
now **failed on five KR runs** — intraday stubs and benchmark bar gaps that silently re-date a whole
run. Measured here so the absence is a measurement, not an assumption.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-14.pkl`
(85 rows × 1806 columns = 301 tickers × 6 fields, MultiIndex `Ticker`×`Price`) + `SECTOR_FLOW_US.json §asof`.

| Item | Value |
|---|---|
| Run clock | **09:10 ET Fri 08-14 — PRE-OPEN** (cash opens 09:30 ET) |
| Last index in the price frame | **2026-08-13** (Thursday) |
| Last-bar volume / prior-20d average — median | **0.732** (q25 **0.613** · q75 **0.892**, n=300) |
| Benchmark `SPY` last three bars | 08-11 **770.56** · 08-12 **772.49** · **08-13 777.88 — present** |
| `SPY` valid bars vs frame rows | **85 / 85** — no benchmark gap |
| `SECTOR_FLOW_US.json §asof` | **2026-08-13** — matches the data's own last index |
| Non-null closes on the last row | **300 / 301** (one hole → G5) |

⇒ The last bar is a **full settled session**, not an intraday stub (the KR failure mode measured
**0.223**). The benchmark carries the same terminal date as the names, so
`rs20 = ret(name,20) − ret(bench,20)` has **matched endpoints** — the split-endpoint contamination
that revoked fine-grain RS on five KR runs **does not exist in this run**.

⚠ Read the 0.732 correctly: it is **not** an incomplete bar. 08-13 was a real full session in which
SPY rose **+0.70%** (772.49 → 777.88); the sub-1.0 ratio is a genuinely lighter-volume up-session,
which is itself a *finding* for later stages, not an instrument defect.

**✅ Rights available for this run:**
1. **RS20/RS60 may be compared at fine grain** — no contamination band.
2. **`vol_surge` may be read in both directions** — the last bar is complete, so a low reading is a
   low reading and not a clock artifact.
3. `asof 2026-08-13` may be written plainly as "data through the 08-13 close". No two-line date caveat.

---

## G1 · News axis alive — 🔴 FAIL *(second consecutive run, same number, same cause)*

**Commands**
- `SECTOR_FLOW_US.json §scoring` → `{"vel_axis": false, "vel_coverage": 0.17, "n_axes": 3, "scored": 300, "dropped_missing_axis": 0}`
- Sweep's own health line: `[axis] velocity 측정 51/300 = 17.0% → 속도축 제외(전원 3축) · 기준 80%` + the 🚨 line
- Falsification probe, actually run: `python -X utf8 -m module_news_data fts search <name> --days 7 --count --scope foreign`

| Probe (22:15 KST) | Result |
|---|---|
| Nvidia | ❌ `뉴스 API 접속 실패(https://…ngrok-free.dev/exec): URLError(FileNotFoundError(2))` |
| Broadcom | ❌ same |
| Marathon Petroleum | ❌ same |
| Eaton | ❌ same |
| Nucor | ❌ same |

**5/5 failed on the remote bridge.** Local fallback probed separately with `DEGAJA_NEWS_API=` →
**`색인 없음 — 먼저 fts build 실행`**. Both bridges are down:

| Bridge | State |
|---|---|
| Remote (`…ngrok-free.dev/exec`) | **unreachable** — `URLError`. Same failure as the 08-13 US run |
| Local `data/news_fts.db` | **0 bytes** (mtime 2026-08-12 10:51) — unchanged for 2 days |
| Local `data/news_fts_kr.db` | **0 bytes** (mtime 2026-07-30) |
| `data/news_alert.db` | **absent from this repo's `data/`** — the desk has no local raw store to rebuild the index from |

### ★ The decisive measurement: is it silence, or is it the pipe?

The client-owned derivative store `data/news_vectors.db` (**1.045 GB**, mtime **2026-08-14 08:55**)
was queried directly. It does not go through the FTS index or the remote API, so it is an
independent witness to whether articles exist at all.

⚠ **Method correction made during this gate, logged deliberately.** A first pass filtered on
`published_at`, which is stored as an **RFC-2822 string** (`"Wed, 8 Jul 2026 23:55:00 +0900"`), not
ISO — a string comparison against `'2026-08-07'` returned **393,493 rows** and a "max date" of
**8 July**. Both are artifacts of comparing prose to a date. The correct column is `market_day`.
This is the exact defect class the gate exists for, caught inside the gate itself; the numbers below
are the `market_day` numbers.

| `market_day` | Articles in client store |
|---|---|
| 2026-08-08 | 3,426 |
| 2026-08-09 | 3,631 |
| 2026-08-10 | 8,350 |
| 2026-08-11 | 8,836 |
| 2026-08-12 | 8,989 |
| 2026-08-13 | 8,473 |
| 2026-08-14 (partial, pre-open) | 487 |
| **7-day total** | **42,192** |

Title-string hits in that same window: **`Nvidia` 439** · **`Fed` 442** · **`CPI` 304** ·
**`PPI` 198** · **`tariff` 102** · **`Broadcom` 45** · **`Eaton` 12** · `Phillips 66` 9 ·
`Nucor` 4 · `Marathon Petroleum` 2 · `rate cut` 2 · `Powell` 1.

⇒ **The corpus is alive and large. The desk's ability to read it is dead.** `Nvidia` returns
**439 titles** from the store and **an error** from the desk's own search path. The number that
would have been reported (17% coverage) describes **the tunnel**, not the world.

⚠ Note what the sweep did **right**: it scored all 300 names on **3 axes uniformly** and printed the
🚨 line. The 2026-08-09 defect (per-name axis dropping worth up to **+0.5**, inflating 799 of 827
names by an average **+0.305**) **did not recur** — `dropped_missing_axis: 0`.

**🚫 Rights revoked today**
1. **No citation of news velocity** in any stage (SWEEP · EVENT_ALPHA · ROTATION · DEEP · BET).
   The **51** names that *did* return are a **non-random survivor sample** (they survived a failing
   tunnel) — they are not usable either.
2. **No "this theme is fresh / this theme has cooled" verdict.** `theme_age`, `chain_hop` and
   `drift_watch` outputs are **not citable** — they ride the same transport.
   ⚠ **This binds stage 11 (DRIFT) directly**: DRIFT must state that its instrument was dead rather
   than report an empty burst list as "no drift".
3. **"It has gone quiet" is forbidden as evidence.** Measured: 42,192 articles exist in the window
   the desk reads as 83% empty.
4. `flow_score` is a **3-axis score** — that fact goes on the **same line** as any conclusion drawn
   from it, every time.
5. ⚠ **The inverse is equally forbidden** — "the news axis is dead, therefore there is no news" is
   the same error with the sign flipped. If a stage needs a news fact today it must come from a
   **named primary source with a URL/date on that line** (filing, FRED release, exchange notice),
   not from the desk's search layer.

---

## G2 · Scoring-scale continuity — 🟢 PASS

**Command** `§scoring.n_axes` vs `llm_outputs/sector_flow/history.json` previous snapshot `_mode`

| Snapshot key | `_mode` | n | Note |
|---|---|---|---|
| 2026-08-06 | news (4-axis) | 300 | last 4-axis run |
| 2026-08-07 | nonews (3-axis) | 299 | |
| 2026-08-11 | nonews (3-axis) | 300 | |
| 2026-08-12 | nonews (3-axis) | 300 | ← **today's Δ baseline** |
| **2026-08-13** | **nonews (3-axis)** | **300** | ← **this run's saved key** (run date 08-14, asof 08-13) |

Axis count matches (3 = 3) ⇒ **PASS**, and **300/300 names carry a Δ**. No apples-to-oranges
subtraction. The baseline is **2026-08-12**, i.e. Δ spans **exactly one settled trading session** —
"Δ vs prior session" is literally true this run, as it was on 08-13.

⚠ **Standing caveat, unchanged**: this is a **3-axis** Δ on both sides. It measures price/OBV/RS
rotation only. A name whose entire change is narrative is **invisible in this Δ by construction** —
and with G1 down, that blindness has no compensating instrument today.

---

## G3 · Who owns the sector sign — 🟢 PASS *(gate passes; the content is worse than yesterday)*

**Command** `§sector_rotation[].top1_flips_sign` — the list must be printed (zero entries still PASS)

**3 of 11** sectors flip sign when their single largest name is removed. Printed in full:

| Sector | wflow | ex-top1 | top1 | top1_w | n | eqflow | breadth |
|---|---|---|---|---|---|---|---|
| Information Technology | **+0.016** | **−0.078** | `NVDA` Nvidia | 19.4% | 56 | +0.034 | 0.09 |
| Health Care | **−0.012** | **+0.002** | `LLY` Lilly (Eli) | 19.4% | 32 | +0.019 | 0.00 |
| Materials | **−0.179** | **+0.016** | `LIN` Linde plc | 24.7% | 12 | −0.130 | 0.00 |

Up from **2** on 08-13 (Industrials/`CAT` dropped out at −0.046; **IT and Health Care entered**).

★ **The one that matters.** Information Technology is the desk's largest sector (n=56) and its
**only non-negative `wflow` outside Energy** — and that non-negativity is **entirely one name**.
Strip `NVDA` and IT reads **−0.078**, i.e. sixth of eleven rather than second. A sign flip only
appears when a sector's weighted flow is sitting on zero: IT at **+0.016** is not a bullish sector,
it is a sector with **no aggregate signal**, where one 19.4%-weighted name decides the sign.
⚠ Fewer/more flippers is **not** a concentration trend; it is a measure of how many sectors are
pinned near zero.
⚠ Every `top1_w` here is computed from a **30-day-old market-cap file** (G5).

**Binding**: **Information Technology, Health Care and Materials may not be promoted or demoted on
`wflow`** (ROTATION §2). Use `eqflow` / `breadth` — note that in IT and Health Care these point the
**opposite way** from `wflow`'s implied story (IT breadth 0.09 with 5 green vs 10 red; Health Care
breadth 0.00) — or hold the call.

---

## G4 · Risk-unit stability — 🔴 FAIL (5th consecutive run)

**Command** `python -X utf8 scripts/risk_units.py --book --days {250,500,750}` — **all three actually run**

| `--days` | Units | In-group resid. corr | Chosen dist |
|---|---|---|---|
| 250 | **11** | +0.6018 | 0.65 (corr ≥ 0.35) |
| 500 | **10** | +0.5254 | 0.65 |
| 750 | **10** | +0.5141 | 0.65 |

**500 and 750 agree; 250 does not.** The book is 13 names; the disagreement is three pairs:

| Pair | 250d | 500d | 750d |
|---|---|---|---|
| `AVGO` · `NVDA` | **separate** | **merged** | **merged** |
| `ANET` · `ETN` | **separate** | **merged** | **merged** |
| `028050` · `316140` (KR) | **merged** | separate | separate |

`MPC`·`PSX` merge in all three windows — the only unit the instrument agrees on.

The tool flags the `ANET·ETN` merge itself at 500d/750d: *"two different theme labels inside one
measured unit — `MAX_THEME_PCT` is counting this as two."* i.e. the book's label taxonomy
(`AI-compute-EPICENTER` vs `AI-power/electrical`) and the **measured** co-movement structure
disagree on the two longer windows. At 250d the KR pair (`KR-E&C/plant` + `KR-bank-holding`) draws
the same warning — two labels, one measured unit.

⚠ Slightly better than 08-13 (which had all three windows disagreeing: 12/10/11). Still FAIL: the
gate is *identical grouping across three windows*, and two of three is not three.

**🚫 Rights revoked today**
1. **No single-number concentration guard** in BET/SIZE.
2. Any concentration statement must carry **the `--days` window on the same line as the conclusion**.
3. **No verdict today on whether `AVGO`+`NVDA` are one unit or two** — the window picks the answer,
   and 2 of 3 windows say one. Same for `ANET`+`ETN` (2 of 3 say one) and the KR pair (1 of 3).

---

## G5 · Does the universe cover the book — 🔴 FAIL *(on staleness only; coverage is clean)*

**Command** `data/us_universe/us_top300.csv` × `module_paper_book status` holdings × scored-name set

| Item | Value |
|---|---|
| Book holdings | **13** (US 11 · KR 2) |
| US holdings inside `us_top300` | **11 / 11 ✅** — ANET · AVGO · ETN · HPE · MET · MPC · NDAQ · NUE · NVDA · PSX · RTX |
| US holdings actually **scored** by the sweep | **11 / 11 ✅** (verified against `§names`, not just the CSV) |
| ★ `LNG` · `TSM` outside-universe hole | **still closed** — neither is held (was logged 12 consecutive runs) |
| `us_top300.csv` age | **30 days** (mtime 2026-07-15, limit **≤8**) → 🔴 |
| Universe size | 300 requested / **300 scored** |
| ⚠ **Null last bar** | **`EA`** — 300 of 301 columns carry an 08-13 close; `EA` has none (**2nd consecutive run**) |
| Rebuild candidate | `data/us_universe/us_all_v2_candidate.csv` **exists, unpromoted** — promotion is a human decision (P5) |

Sweep log line 1: `[warn] 유니버스 us_top300.csv 30일 경과 — 시총 stale.`

**🚫 Rights revoked today**
1. **`wflow` may not be described as "current market-cap weighted"** — the weights are **30 days
   old**. Every `top1_w` in G3 inherits this, including the 19.4% that decides IT's sign.
2. **No flow / RS / OBV / short verdict on `EA`** — it was not measured. Absence of a bar is not
   absence of a move.
3. ✅ **Positive, third consecutive run**: every name the book holds can be tagged by every
   instrument the desk uses. There are **zero** "held but unmeasurable" names.

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL

**Command** `python -X utf8 scripts/snapshot_estimates.py --status`

| Item | Value |
|---|---|
| Accumulated | **10 files / 24 calendar days** (2026-07-22 → 2026-08-14, today's included) |
| Measured rate | **0.42 files/day** (ideal 1.0) |
| To the 40-day target | ideal **30 days** vs measured **≈72 days** = **2.4×** (limit 1.5×) |
| Gaps (days) | [3, 4, 6, 3, 1, 2, 1, 1] · median 2 · max 6 |

Today's file landed, and the recent gap sequence (1, 2, 1, 1) is the best stretch since inception —
but the cumulative rate is what sizes the sample, and it is 2.4× slow. Not recoverable
retroactively: days not captured are gone.

**🚫 Rights revoked today**
1. **No reporting of `kelly_size --ic` output as an evidence-backed size.**
2. Any size written today is labelled **"mechanical ¼"**.

---

## G7 · Tool liveness — 🔴 FAIL (2 of 46 · 5th consecutive run, same two)

**Command** `--help` on every entry point this run will use; exit code recorded.

**exit 0 — 44**: `sector_flow` · `us_live_shortlist` · `us_flow` · `flow_read` · `exposure_rule` ·
`missed_ledger` · `reject_ledger` · `kelly_size` · `catalyst_calendar` · `report_lint` · `risk_units` ·
`axis_window_flow` · `snapshot_estimates` · `ic_ledger` · `leak_scan` · `axis_inflection` ·
`cycle_exposure` · `drift_watch` · `us_setup_screener` · `action_bracket` · `handoff_id_audit` ·
`handoff_compact` · `yf_snapshot` · `brief_recall` · `measure_ic` · `module_news_data` · `module_KIS` ·
`module_valuation` · `module_report_tags` · `module_disclosure_us` · `module_disclosure` ·
`module_fundamentals_us` · `module_fundamentals_kr` · `module_business_us` · `module_business` ·
`module_paper_book` · `module_macro_us` · `module_industry_map` · `module_flow` · `module_watchlist` ·
`module_epistemics` · `module_inflection` · `module_math_check` · `module_publish`

**exit 1 — 2** (identical to 08-10 · 08-12 · 08-13 · this morning's KR run)

| Tool | `--help` failure | Functional probe (rule 3), actually run |
|---|---|---|
| `scripts/margin_history.py` | exit 1 — `%`-format bug in the help string (argparse `_expand_help`) | `margin_history.py NVDA` → **exit 0**: gross margin FY2009–FY2026, high **FY2025 75.0%** · low **FY2009 34.3%** · **median 56.9%** · FY2026 **71.1%** on **$215.9B** |
| `module_chart` | exit 1 — CLI does not implement `--help` (prints usage, exits 1) | `module_chart NVDA --read` → **exit 0**: OBV **neutral** (20d slope +0%) · no divergence · bull stack 5>20>60>120, price above 4/4 MA · Bollinger expansion 20.1%, **mid-band** · RSI 63.9 · momentum20d +11.1% · turn verdict **NEUTRAL/CHOP** · swing-low stop 190.01 |

⇒ Under rule 3 both were **actually run and produced correct output** ⇒ **citation rights retained**,
but the warrant is the **probe output above**, not `--help`, and only for **those two command lines**.
⚠ A broken `--help` means a human cannot discover the tool. **Logged unrepaired for the 5th run.**

---

## What this table binds today (handed to HANDOVER)

| Stage | Cannot use today |
|---|---|
| SWEEP | news velocity · theme freshness · "quiet" · stale mcap described as current · any verdict on `EA` |
| EVENT_ALPHA | "theme is fresh/cooled" · `theme_age` / `chain_hop` outputs · any velocity-derived forward card |
| ROTATION | **`wflow` promotion/demotion for Information Technology, Health Care and Materials** (G3 flippers) · news-axis tie-breaks |
| PREMORTEM | "the tape has gone quiet on this risk" — the tape is unreadable, not quiet |
| DEEP | news velocity · "no news flow" as evidence of anything |
| BET / SIZE | single-number concentration · `--ic`-backed size (→ **"mechanical ¼"**) · `AVGO/NVDA` and `ANET/ETN` unit counts |
| DRIFT | **must report that `drift_watch`'s instrument was dead** — an empty burst list today is not "no drift" |

**What this desk CAN speak with today (stated positively).**
① **Settled prices through 2026-08-13** — with **RS at fine grain** (G0 clean, second run running).
② **OBV level and state** — last bar complete.
③ **eqflow · breadth** — unweighted, so the 30-day-stale caps barely touch them; with news dead
   these carry more load, not less.
④ **`vol_surge` in both directions** (G0 clean).
⑤ **FINRA short pressure · CFTC COT percentile positioning** — the US substitute for the
   investor-type feed. Context, never a trigger.
⑥ **FRED macro series** (`module_macro_us`, cite `[FRED]`).
⑦ **Primary filings** (`module_disclosure_us` / `module_fundamentals_us`) and **margin history**.
⑧ **Hand-cited individual news facts with a named source and date on the line** — the search layer is
   dead, the world is not (42,192 articles exist in the 7-day window).

**Speak with settled prices, breadth, positioning and primary documents. Do not speak with the
news axis, theme age, or a single concentration number.**

*Instrument state is not a market view — this document is not written into `handoff/` (HANDOVER only reads it).*
