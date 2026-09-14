# PREFLIGHT — 2026-08-15 · industry_us (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This document is not a report — it is a rights table.** A FAIL is not "read with care"; it is
> **"what this run may not claim today."**
> Run clock **KST 2026-08-15 22:10–22:35 = ET 2026-08-15 09:10–09:35, SATURDAY — US cash closed.**
> Sweep data **asof 2026-08-14** — last settled US close (Friday). No session is open behind this run.
>
> ⚠ **Filename deviation, logged (6th consecutive run, same reason):** the composition table names this
> `preflight/PREFLIGHT.md`, but the `industry_kr` desk already wrote its rights table to that path this
> morning (10:17 KST). Overwriting a sibling desk's output is not a correction, so the US table is
> written as `PREFLIGHT_US.md` in the same folder — the documented practice on 08-10 · 08-12 · 08-13 · 08-14.
> Human decision on permanent market-suffixing is still pending (PROMPT_MAP §6).

## Verdict summary

| Gate | Verdict | One line |
|---|---|---|
| **G0** bar completeness · date alignment *(bonus gate, carried from the KR desk)* | 🟢 **PASS** | Last bar **2026-08-14**, **settled by construction** (weekend run). Benchmark **SPY carries the 08-14 bar** (776.34), **85/85** valid bars → matched RS endpoints. **Third consecutive clean US clock** |
| **G1** news axis alive | 🔴 **FAIL** *(but the diagnosis inverted — read it)* | Sweep coverage **17.1% (51/299)**, third run at the same number. ★ **n=40 re-probe of the "silent" names: 34 valid (85.0%) · 6 pipe-fail (15.0%) · ZERO genuinely no-news.** The 83% is **entirely instrument**, and the library path is **alive** — it is the **sweep's burst** and the **CLI path** that fail |
| **G2** scoring-scale continuity | 🟢 **PASS** | **3-axis (`nonews`) vs 3-axis (`nonews`)**, baseline **2026-08-13**, **299/300** names carry Δ. Δ spans **exactly one settled session** (08-13 → 08-14) |
| **G3** who owns the sector sign | 🟢 **PASS** | Flipper list printed in full — **3 of 11** (IT/`NVDA` · Industrials/`CAT` · Materials/`LIN`). Health Care exited, Industrials re-entered |
| **G4** risk-unit stability | 🔴 **FAIL** | 250d **11 units** · 500d **10** · 750d **10** — 500 and 750 agree, **250 does not** (**6th consecutive run, identical numbers**) |
| **G5** does the universe cover the book | 🔴 **FAIL** | **11/11 US holdings inside `us_top300` AND scored ✅**. But `us_top300.csv` is **31 days old** (limit ≤8) and **`EA` returned a null last bar for the 3rd consecutive run** |
| **G6** estimate-snapshot accrual | 🔴 **FAIL** | Measured ETA **≈72 days** vs ideal 30 = **2.4×** (limit 1.5×). 10 files / 24 calendar days |
| **G7** tool liveness | 🔴 **FAIL** | **46 entry points** probed, **2** non-zero `--help` (`scripts/margin_history.py` · `module_chart`) — **6th consecutive run unrepaired**. Both pass a functional probe ⇒ citation rights retained **for those command lines only** |

**PASS 3 / FAIL 5** (of the seven official gates: PASS 2 / FAIL 5; G0 is the bonus gate).
Headline count identical to 08-14 — **but the content of G1 changed materially and in the desk's favour.**
Today this desk **cannot** speak with the sweep's news-velocity axis, theme freshness, "it went quiet",
a single concentration number, or an `--ic`-derived size. It **can** speak with settled prices through
the **08-14** close, fine-grain RS, OBV, breadth, `vol_surge` both ways, FINRA short pressure, CFTC COT
positioning, FRED series, primary filings — **and, newly measured today, hand-cited per-name news
velocity at 85% success, provided the number is quoted with its own probe on the same line.**

---

## G0 · Bar completeness · date alignment — 🟢 PASS *(bonus gate)*

Not one of the seven. Carried because the KR desk measured it into existence on 08-12 and it has failed
repeatedly there — intraday stubs and benchmark bar gaps that silently re-date a whole run.

**Command** direct measurement of `llm_outputs/sector_flow/prices_2026-08-15.pkl`
(85 rows × 1806 columns = 301 tickers × 6 fields, MultiIndex `Ticker`×`Price`) + `SECTOR_FLOW_US.json §asof`.

| Item | Value |
|---|---|
| Run clock | **09:10 ET Sat 08-15 — MARKET CLOSED** (no session open behind the run) |
| Last index in the price frame | **2026-08-14** (Friday) |
| Last-bar volume / prior-20d average — median | **0.649** (q25 **0.543** · q75 **0.822**, n=300) |
| Benchmark `SPY` last three bars | 08-12 **772.49** · 08-13 **777.88** · **08-14 776.34 — present** |
| `SPY` valid bars vs frame rows | **85 / 85** — no benchmark gap |
| `SECTOR_FLOW_US.json §asof` | **2026-08-14** — matches the data's own last index |
| Non-null closes on the last row | **300 / 301** (one hole → G5) |

⇒ Because the run is on a **non-session day**, an incomplete last bar is **impossible in principle** —
this is the strongest form this gate can pass in. The benchmark carries the same terminal date as the
names, so `rs20 = ret(name,20) − ret(bench,20)` has **matched endpoints**.

⚠ **Read the 0.649 correctly.** It is **not** an incomplete bar; it is a genuinely **light-volume
session**. 08-14 was a full Friday in which SPY *fell* 777.88 → 776.34 (**−0.20%**) on volume running
about **two-thirds** of the trailing 20-day norm, and the ratio is *lower* than 08-13's 0.732. Two
consecutive sub-0.75 sessions is a **finding for later stages** (a tape thinning out, not a tape
selling off), not an instrument defect. It is also **not** an opex artifact — August monthly expiry is
08-21.

**✅ Rights available for this run:**
1. **RS20/RS60 may be compared at fine grain** — no contamination band.
2. **`vol_surge` may be read in both directions** — the last bar is complete, so a low reading is a
   low reading and not a clock artifact. ★ This matters unusually today: the whole tape reads light,
   and this gate is what licenses the desk to call that real.
3. `asof 2026-08-14` may be written plainly as "data through the 08-14 close". No date caveat.

---

## G1 · News axis alive — 🔴 FAIL *(3rd run at the same number — with a materially different cause)*

**Commands**
- `SECTOR_FLOW_US.json §scoring` → `{"vel_axis": false, "vel_coverage": 0.1706, "n_axes": 3, "scored": 299, "dropped_missing_axis": 0}`
- Sweep's own health line: `[axis] velocity 측정 51/299 = 17.1% → 속도축 제외(전원 3축) · 기준 80%` + the 🚨 line
- Falsification probe A (CLI path), actually run: `python -X utf8 -m module_news_data fts search <name> --days 7 --count --scope foreign`
- Falsification probe B (library path, **the exact call the sweep makes**), actually run:
  `flow_read.news_velocity(flow_read._news_query(tk, name), 7, 30, kr=False)`

### (a) Probe A — the CLI path is dead, 5/5

| Probe (22:14 KST) | Result |
|---|---|
| Nvidia · Broadcom · Marathon Petroleum · Eaton · Nucor | ❌ all five: `뉴스 API 접속 실패(https://…ngrok-free.dev/exec): URLError(FileNotFoundError(2))` |

Local fallback probed separately with `DEGAJA_NEWS_API=` → **`색인 없음 — 먼저 fts build 실행`**.

| Bridge | State |
|---|---|
| Remote **via the CLI** (`…ngrok-free.dev/exec`) | **unreachable** — `URLError`, same as 08-13 and 08-14 |
| Local `data/news_fts.db` | **0 bytes** (mtime 2026-08-12 10:51) — unchanged for 3 days |
| Local `data/news_fts_kr.db` | **0 bytes** (mtime 2026-07-30) |
| `data/news_alert.db` | **absent from this repo's `data/`** — no local raw store to rebuild the index from |

### (b) ★ Probe B — the library path is ALIVE, and it overturns yesterday's conclusion

Yesterday this gate concluded *"both bridges are down."* That was measured **through the CLI only**.
Today the **library** entry point — the one `sector_flow` itself calls, same function, same query
builder, same arguments — was re-probed against **names the sweep had recorded as `velocity: None`**:

| Re-probe (n=40 random draw from the 248 "silent" names, 80 requests, **17.2 s**) | Count | Share |
|---|---|---|
| **Valid velocity returned** — i.e. the sweep simply failed to count it | **34** | **85.0%** |
| **Pipe failure** (`뉴스 API 응답 실패 + 로컬 FTS 색인 없음`) | **6** | 15.0% |
| **Genuinely zero articles in the window** | **0** | **0.0%** |

Worked examples, all from the sweep's *dead* list, all `"source": "api"`:
`NDAQ` 7d **3,895** / 30d 12,810 → **1.30** · `BLK` 370/990 → **1.60** · `BA` 363/1,374 → **1.13** ·
`LITE` 194/424 → **1.96** · `HPE` 48/137 → **1.50** · `PANW` 79/223 → **1.52** · `ANET` 52/155 → **1.44** ·
`GD` 27/119 → **0.97** · `PNC` 3/23 → **0.56** · `CCL` 3/17 → **0.76**.

⇒ **Not one name in 40 was actually quiet.** The sweep's 83% silence is **100% instrument, 0% world.**
The failure is **rate-dependent**: the sweep fires ~600 sequential remote calls and most fail; a probe
firing 80 calls in 17 seconds succeeds 85%. Two separate transports are involved and they disagree —
the **CLI** endpoint fails 5/5 while the **library** endpoint answers 85%.

⚠ **The one thing that did not resolve.** The 51 survivors are **the same 51 tickers as on 08-14**
(set identity verified: today-only 0, yesterday-only 0) while **48 of 51 carry different values**. A
purely random rate failure would not reproduce an identical survivor set two days running. So the
selection mechanism is **not yet measured** — it is not article volume (`NDAQ` returns 3,895 articles
and is a non-survivor), and it is not caching (the values move). **Recorded as unexplained.** Repair
and root-cause are not this stage's job (rule 1).

### (c) The independent witness went stale — new this run

`data/news_vectors.db` (**1.045 GB**) is the client-owned derivative store used yesterday as an
independent witness. Its **sync cursor is frozen at `2026-08-14T07:59:45`** — byte-identical to
yesterday's reading — and every title count is unchanged (`Nvidia` **439**, `Fed` **442**, `CPI` **304**,
`PPI` **198**, `tariff` **102**). Max `market_day` = **2026-08-14** with only **487** rows against
8,000–9,000 on normal days. The file's mtime moved (08-15 10:56) while its contents did not.

⇒ **The entire Friday 08-14 US session — the very session this run prices off — is unwitnessed in the
local store** (07:59 KST = 18:59 ET on 08-13). The store may be used for the window **through 08-13**
and **not beyond**. The remote corpus itself is fresh (`NVDA` returns 1,407 articles over 7 days), so
this is a **local sync stall**, not a collection failure.

**🚫 Rights revoked today**
1. **No citation of the sweep's news-velocity axis, and no citation of the 51 survivors.** They remain
   a **non-random survivor sample** selected by an unexplained mechanism (§b) — worse than a random
   sample, not better.
2. **No "this theme is fresh / this theme has cooled" verdict from `theme_age`, `chain_hop` or
   `drift_watch`** — they ride the CLI transport, which is 5/5 dead.
   ⚠ **This binds stage 11 (DRIFT) directly**: DRIFT must state that its instrument was dead rather
   than report an empty burst list as "no drift".
3. **"It has gone quiet" is forbidden as evidence.** Measured: **0 of 40** silent names were quiet.
4. `flow_score` is a **3-axis score** — that fact goes on the **same line** as any conclusion drawn
   from it, every time.
5. **No use of `news_vectors.db` for anything after 2026-08-13.** The 08-14 session is not in it.
6. ⚠ **The inverse is equally forbidden** — "the news axis is dead, therefore there is no news."

**✅ Right RESTORED today, with conditions.** Per-name news velocity **may** be cited when the desk
runs `flow_read.news_velocity` for that specific name and writes **the returned 7d/30d counts on the
same line as the claim**. Measured warrant: **85% success at probe rate, 0% false silence.** Two limits
travel with it: (i) it is an **article-count ratio, not content** — it says attention moved, never why;
(ii) a name that fails the probe is **unmeasured, not quiet**, and must be written that way.

---

## G2 · Scoring-scale continuity — 🟢 PASS

**Command** `§scoring.n_axes` vs `llm_outputs/sector_flow/history.json` previous snapshot `_mode`

| Snapshot key | `_mode` | n | Note |
|---|---|---|---|
| 2026-08-06 | news (4-axis) | 300 | last 4-axis run |
| 2026-08-07 | nonews (3-axis) | 299 | |
| 2026-08-11 | nonews (3-axis) | 300 | |
| 2026-08-12 | nonews (3-axis) | 300 | |
| 2026-08-13 | nonews (3-axis) | 300 | ← **today's Δ baseline** |
| **2026-08-14** | **nonews (3-axis)** | **299** | ← **this run's saved key** (run date 08-15, asof 08-14) |

Axis count matches (3 = 3) ⇒ **PASS**. The baseline is **2026-08-13**, so Δ spans **exactly one settled
trading session** (08-13 close → 08-14 close) — "Δ vs prior session" is literally true this run.
**299 of 300** names carry a Δ; the missing one is `EA` (G5).

⚠ **Standing caveat, unchanged**: this is a **3-axis** Δ on both sides. It measures price/OBV/RS
rotation only. A name whose entire change is narrative is **invisible in this Δ by construction** —
and with the sweep's news axis down, the only compensating instrument is the per-name hand probe
licensed in G1, which no Δ uses.

---

## G3 · Who owns the sector sign — 🟢 PASS

**Command** `§sector_rotation[].top1_flips_sign` — the list must be printed (zero entries still PASS)

**3 of 11** sectors flip sign when their single largest name is removed. Printed in full:

| Sector | wflow | ex-top1 | top1 | top1_w | n | eqflow | breadth |
|---|---|---|---|---|---|---|---|
| Information Technology | **+0.023** | **−0.082** | `NVDA` Nvidia | 19.4% | 56 | +0.044 | 0.09 |
| Industrials | **−0.047** | **+0.006** | `CAT` Caterpillar | 8.7% | 50 | −0.007 | 0.00 |
| Materials | **−0.169** | **+0.033** | `LIN` Linde plc | 24.7% | 12 | −0.114 | 0.00 |

Count unchanged at **3**, membership rotated: **Health Care exited** (wflow −0.115, ex-top1 −0.031 —
`LLY` no longer decides the sign), **Industrials re-entered** (it was the one that dropped out on 08-14).

★ **The one that matters, for the second straight run.** Information Technology is the desk's largest
sector (n=56) and, after Energy, its **only non-negative `wflow`** — and that non-negativity is
**entirely one name**. Strip `NVDA` and IT reads **−0.082**. A sign flip only appears when weighted flow
is sitting on zero: IT at **+0.023** is not a bullish sector, it is a sector with **no aggregate signal**
in which one 19.4%-weighted name decides the sign. Note `eqflow +0.044` and `breadth 0.09` (5 green vs
6 red of 56) point the same faint way — IT is *flat*, not strong.
⚠ Industrials is the mirror image: `wflow −0.047` vs `ex-top1 +0.006` on a top1 weight of only **8.7%**,
with `breadth 0.00` (**0 green, 10 red**). The flip is real but the sector is uniformly weak either way.
⚠ Every `top1_w` here is computed from a **31-day-old market-cap file** (G5).

**Binding**: **Information Technology, Industrials and Materials may not be promoted or demoted on
`wflow`** (ROTATION §2). Use `eqflow` / `breadth`, or hold the call.

---

## G4 · Risk-unit stability — 🔴 FAIL (6th consecutive run)

**Command** `python -X utf8 scripts/risk_units.py --book --days {250,500,750}` — **all three actually run**

| `--days` | Units | Window | In-group resid. corr | Max resid. corr | ARI (1st half vs 2nd) |
|---|---|---|---|---|---|
| 250 | **11** | 2025-07-29 → 2026-08-14 (249 sessions) | +0.6058 | +0.8524 | 0.4902 |
| 500 | **10** | 2024-07-02 → 2026-08-14 (499 sessions) | +0.5248 | +0.8467 | 0.3743 |
| 750 | **10** | 2023-06-12 → 2026-08-14 (749 sessions) | +0.5135 | +0.8217 | 0.3810 |

**500 and 750 agree; 250 does not.** The book is 13 names; the disagreement is three pairs:

| Pair | 250d | 500d | 750d |
|---|---|---|---|
| `AVGO` · `NVDA` | **separate** (U3·U9) | **merged** (U1) | **merged** (U1) |
| `ANET` · `ETN` | **separate** (U2·U4) | **merged** (U0) | **merged** (U0) |
| `028050` · `316140` (KR) | **merged** (U0) | separate (U3·U4) | separate (U3·U4) |

`MPC`·`PSX` merge in all three windows — the only unit the instrument agrees on.
The tool flags the `ANET·ETN` merge itself at 500d/750d: *"two different theme labels inside one
measured unit — `MAX_THEME_PCT` is counting this as two"* (`AI-compute-EPICENTER` vs
`AI-power/electrical`). At 250d the KR pair draws the same warning.
Standing tool warnings, re-logged: **ARI 0.37–0.49 moves opposite to fit (S5)** in all three windows;
**249 < 250 sessions** at the short window ("short samples invent structure"); **KR returns are KRW and
US returns are USD** so a common FX factor can be injected; intersection holes up to **8 days**
(2 at 250d · 5 at 500d · 8 at 750d).
※ **Numbers identical to 08-14** (11/10/10) — sixth run in the same place.

**🚫 Rights revoked today**
1. **No single-number concentration guard** in BET/SIZE.
2. Any concentration statement must carry **the `--days` window on the same line as the conclusion**.
3. **No verdict today on whether `AVGO`+`NVDA` are one unit or two** — the window picks the answer,
   and 2 of 3 windows say one. Same for `ANET`+`ETN` (2 of 3 say one) and the KR pair (1 of 3).

---

## G5 · Does the universe cover the book — 🔴 FAIL *(on staleness only; coverage is clean)*

**Command** `data/us_universe/us_top300.csv` × `module_paper_book status` holdings × the scored-name set

| Item | Value |
|---|---|
| Book holdings | **13** (US 11 · KR 2) · total **17,859,402 KRW** · cash KRW 4,938,207 + USD 1,904 |
| US holdings inside `us_top300` | **11 / 11 ✅** — ANET · AVGO · ETN · HPE · MET · MPC · NDAQ · NUE · NVDA · PSX · RTX |
| US holdings actually **scored** by the sweep | **11 / 11 ✅** (verified against `§names`, not just the CSV) |
| ★ `LNG` · `TSM` outside-universe hole | **still closed** — neither is held (was logged 12 consecutive runs) |
| `us_top300.csv` age | **31 days** (mtime 2026-07-15, limit **≤8**) → 🔴 |
| Universe size | 300 requested / **299 scored** |
| ⚠ **Null last bar** | **`EA`** — 300 of 301 columns carry an 08-14 close; `EA` has none (**3rd consecutive run**) |
| Rebuild candidate | `data/us_universe/us_all_v2_candidate.csv` (mtime 08-10) **exists, unpromoted** — promotion is a human decision (P5) |

Sweep log line 1: `[warn] 유니버스 us_top300.csv 31일 경과 — 시총 stale.`

**🚫 Rights revoked today**
1. **`wflow` may not be described as "current market-cap weighted"** — the weights are **31 days old**.
   Every `top1_w` in G3 inherits this, including the 19.4% that decides IT's sign.
2. **No flow / RS / OBV / short verdict on `EA`** — it was not measured. Absence of a bar is not
   absence of a move. Third run running; it has now dropped out of the Δ set as well (G2).
3. ✅ **Positive, fourth consecutive run**: every name the book holds can be tagged by every instrument
   the desk uses. There are **zero** "held but unmeasurable" names.

---

## G6 · Estimate-snapshot accrual — 🔴 FAIL

**Command** `python -X utf8 scripts/snapshot_estimates.py --status`

| Item | Value |
|---|---|
| Accumulated | **10 files / 24 calendar days** (2026-07-22 → 2026-08-14) |
| Measured rate | **0.42 files/day** (ideal 1.0) |
| To the 40-day target | ideal **30 days** vs measured **≈72 days** = **2.4×** (limit 1.5×) |
| Gaps (days) | [3, 4, 6, 3, 1, 2, 1, 1] · median 2 · max 6 |
| Since last save | **1 day** (08-14) — **today (Saturday) accrues nothing** |

Unchanged from 08-14. Not recoverable retroactively: days not captured are gone. The tool re-logs its
own trap: *"counting files makes this look healthy"* (D16).

**🚫 Rights revoked today**
1. **No reporting of `kelly_size --ic` output as an evidence-backed size.**
2. Any size written today is labelled **"mechanical ¼"**.

---

## G7 · Tool liveness — 🔴 FAIL (2 of 46 · 6th consecutive run, same two)

**Command** `--help` on every entry point this run will use; exit code recorded. **exit 0 = 44 / 46.**

**exit 0 — 44**: `sector_flow` · `us_live_shortlist` · `us_flow` · `flow_read` · `exposure_rule` ·
`missed_ledger` · `reject_ledger` · `kelly_size` · `catalyst_calendar` · `report_lint` · `risk_units` ·
`axis_window_flow` · `snapshot_estimates` · `ic_ledger` · `leak_scan` · `axis_inflection` ·
`cycle_exposure` · `drift_watch` · `us_setup_screener` · `action_bracket` · `handoff_id_audit` ·
`handoff_compact` · `yf_snapshot` · `brief_recall` · `measure_ic` · `module_news_data` · `module_KIS` ·
`module_valuation` · `module_report_tags` · `module_disclosure_us` · `module_disclosure` ·
`module_fundamentals_us` · `module_fundamentals_kr` · `module_business_us` · `module_business` ·
`module_paper_book` · `module_macro_us` · `module_industry_map` · `module_flow` · `module_watchlist` ·
`module_epistemics` · `module_inflection` · `module_math_check` · `module_publish`

**exit 1 — 2** (identical to 08-10 · 08-12 · 08-13 · 08-14 and this morning's KR run)

| Tool | `--help` failure | Functional probe (rule 3), actually run |
|---|---|---|
| `scripts/margin_history.py` | exit 1 — `%`-format bug in the help string (argparse `_expand_help`) | `margin_history.py NVDA` → **exit 0**: gross margin FY2009–FY2026, high **FY2025 75.0%** · low **FY2009 34.3%** · **median 56.9%** · FY2026 **71.1%** on **$215.9B** revenue |
| `module_chart` | exit 1 — CLI does not implement `--help` (prints usage, exits 1) | `module_chart NVDA --read` → **exit 0**: OBV **neutral** (20d slope **+10%**) · no divergence · bull stack 5>20>60>120, price above 4/4 MA · Bollinger expansion 20.8%, mid-band · **RSI 75.4** · momentum20d **+10.8%** · turn verdict **NEUTRAL/CHOP** · swing-low stop **190.01** |

⇒ Under rule 3 both were **actually run and produced correct output** ⇒ **citation rights retained**,
but the warrant is the **probe output above**, not `--help`, and only for **those two command lines**.
⚠ A broken `--help` means a human cannot discover the tool. **Logged unrepaired for the 6th run.**

---

## What this table binds today (handed to HANDOVER)

| Stage | Cannot use today |
|---|---|
| SWEEP | the sweep's news-velocity axis · the 51 survivors · theme freshness · "quiet" · stale mcap described as current · any verdict on `EA` |
| EVENT_ALPHA | "theme is fresh/cooled" from `theme_age` / `chain_hop` · `news_vectors.db` content after **2026-08-13** |
| ROTATION | **`wflow` promotion/demotion for Information Technology, Industrials and Materials** (G3 flippers) · news-axis tie-breaks |
| PREMORTEM | "the tape has gone quiet on this risk" — measured, 0 of 40 silent names were quiet |
| DEEP | the velocity axis as an axis · "no news flow" as evidence of anything |
| BET / SIZE | single-number concentration · `--ic`-backed size (→ **"mechanical ¼"**) · `AVGO/NVDA` and `ANET/ETN` unit counts |
| DRIFT | **must report that `drift_watch`'s instrument was dead** — an empty burst list today is not "no drift" |

**What this desk CAN speak with today (stated positively).**
① **Settled prices through 2026-08-14** — with **RS at fine grain** (G0 clean, third run running).
② **OBV level and state** — last bar complete by construction (weekend run).
③ **eqflow · breadth** — unweighted, so the 31-day-stale caps barely touch them; with the news axis
   down these carry more load, not less.
④ **`vol_surge` in both directions** — and today that licenses a real reading: **two consecutive
   light-volume sessions** (0.732 then 0.649 of the 20-day norm).
⑤ **FINRA short pressure · CFTC COT percentile positioning** — the US substitute for the
   investor-type feed. Context, never a trigger.
⑥ **FRED macro series** (`module_macro_us`, cite `[FRED]`).
⑦ **Primary filings** (`module_disclosure_us` / `module_fundamentals_us`) and **margin history**.
⑧ ★ **Per-name news velocity by hand probe** — *restored today*, 85% measured success, 0% false
   silence, provided the 7d/30d counts are written on the same line as the claim.

**Speak with settled prices, breadth, positioning, primary documents — and with per-name news counts
you fetched yourself. Do not speak with the sweep's news axis, theme age, or a single concentration
number.**

*Instrument state is not a market view — this document is not written into `handoff/` (HANDOVER only reads it).*
