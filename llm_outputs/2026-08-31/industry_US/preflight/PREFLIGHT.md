# PREFLIGHT — 2026-08-31 (Mon) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is not a report, it is a permissions table** — a FAIL is not "be careful", it is
> **"what this run may not cite today"**.
> Execution KST 2026-08-31 **22:09 clock/weekday · 22:10 bar probe · 22:11 news probe pre-sweep (6/6)
> · 22:11 tool `--help` x37 · 22:12 universe/book/accrual · 22:12–22:14 risk units x3 windows ·
> 22:10–22:16 sweep (`--json`) · 22:17–22:24 ghost-bar repair (5m proxy patch + rescore) ·
> 22:25 news probe post-sweep (4/4) · 22:25 falsification probe (8/8) · 22:26 chart-tool live probe.**
> **Monday 09:09 ET — NYSE has NOT opened yet** (opens 09:30 ET). Last completed US session
> **Fri 2026-08-28**. ⇒ Nothing from Monday's tape exists for this run; every price statement
> below is about **Friday**.

★ **Two-line summary**
> ① 🚨 **The ghost bar did not heal. It is now T+3.** The daily endpoint still returns
>    `2026-08-28` with **O/H/L/Volume present and Close = NaN**, for **301/301** tickers including
>    SPY — the same symptom as yesterday, three calendar days after the session closed.
>    That reclassifies it: yesterday it was reasonable to call this a **transient**; today the
>    vendor has had a full weekend to backfill and has not, so it is a **standing hole in the
>    daily series**, and the desk must assume it will still be there tomorrow.
>    Second consecutive `scored=0` sweep (**0 of 299** names scored, `sector_rotation=[]`).
> ② ★★ **The repair reproduced, independently, to the third decimal — which is itself the
>    strongest evidence the proxy is sound.** I rebuilt the 5m-proxy patch from scratch today
>    (validated **mean abs err 0.0181% · max 0.0448% · 0 names >0.05%**, n=24) and the repaired
>    sector table matches yesterday's separate reconstruction on every one of 11 sectors
>    (Materials `+0.225`, IT `+0.033`, Utilities `−0.549`; largest divergence anywhere **0.002**).
>    Two independent reconstructions of the same session agreeing is a much better warrant than one.
>    ⇒ The Friday tape is citable **as a labeled proxy**, and it is risk-off and narrow:
>    universe wflow **−0.136**, **4 green / 73 red of 299**, only **Materials · IT · Health Care**
>    above zero, Utilities and Comm. Services worst.

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | 🔴 **FAIL — T+3, not transient** · ✅ **proxy-recovered** | 08-28 Close NaN **16/16** direct probe (08-24/25/26/27: **0/16** each) · sweep cache **301/301**. SPY 08-28 `O 771.76 H 775.29 L 768.31 V 36,342,284 C NaN`. 5m endpoint **78/78 bars**; proxy err **0.0181% mean / 0.0448% max, n=24, 0 over 0.05%** |
| **G1** | News-axis liveness | 🔴 **FAIL** (sweep axis) · ✅ **direct path LIVE** | `vel_coverage` **15.72%** (47/299, bar 80%) — *lower* than yesterday's 17.06%. Probe **6/6 pre-sweep · 4/4 post-sweep**. ★ Falsification **8/8**, incl. the two most-negative names in the whole universe (GWW `0.69` · PCAR `1.12`) |
| **G2** | Scoring-scale continuity | ⚠ **PASS (primary idling)** · ✅ **repaired series is scale-legal** | Primary `n_axes=3` = yesterday `3`, but `scored=0` ⇒ no operand. Repaired run: `n_axes=3`, `mode=nonews`, `scored=299`, prev snapshot **08-27 `nonews` n=299** ⇒ same scale, Δ defined on **299/299 common names** |
| **G3** | Who owns the sector sign | 🔴 **FAIL** (primary) · ✅ **recovered via repair** | Primary `§sector_rotation` = **`[]`**, `§names` = **`[]`**. Repaired: **3 of 11 sectors flip sign** on removal of top-1 — **IT/NVDA (19.4%) · Energy/XOM (30.5%) · Cons. Disc./AMZN (40.2%)** |
| **G4** | Risk-unit stability | 🔴 **FAIL** | 250d **11 units** · 500d **10** · 750d **10**, membership differs. ARI **0.3188 / 0.1899 / 0.3810** vs within-group fit **+0.6039 / +0.5274 / +0.5171**. All three windows end **2026-08-27** |
| **G5** | Does the universe cover the book | 🔴 **FAIL** (freshness leg) | Cover ✅ **11/11** US holdings in `us_top300.csv` (300 rows), missing **0**. Freshness ❌ **47 days** (mtime 2026-07-15; bar ≤8) |
| **G6** | Instrumentation accrual rate | 🔴 **FAIL** | **21 files / 41 calendar days = 0.51/day** ⇒ ETA **~37 days** vs ideal 19 = **2.0x** (threshold 1.5x). Gap median 1, max 6 |
| **G7** | Tool liveness | 🔴 **FAIL** (2/37) | 35 of 37 `--help` exit 0. `module_chart` **exit=1** *and* **0/3 live tickers** (NVDA·ANET·SPY all exit 1) · `scripts/margin_history.py` **exit=1** (KR-only, unused here) |

---

## Gate detail

### G0 — Bar completeness 🔴 FAIL (T+3) · ✅ proxy-recovered ★today's principal finding

#### (a) The defect persisted through a full weekend
Direct `yfinance` probe, `auto_adjust=False`, 16 US tickers (11 book holdings + SPY + 4 sector ETFs):

| Session | Close NaN |
|---|---:|
| 2026-08-24 | **0** / 16 |
| 2026-08-25 | **0** / 16 |
| 2026-08-26 | **0** / 16 |
| 2026-08-27 | **0** / 16 |
| **2026-08-28 (Fri, last session)** | **16 / 16** |

Widened to the sweep's own fresh cache (`prices_2026-08-31.pkl`, downloaded today, 301 columns):
**301/301** carry the 08-28 Close NaN. Row present · Volume present · O/H/L present · **Close empty**.

★ **What is new today is the elapsed time, not the symptom.** On 2026-08-30 this was one day old and
could honestly be logged as a transient vendor gap. It is now **three calendar days** past the
session, across a weekend when backfills normally land, and the row is unchanged. **Filing this a
second time as "yesterday's bug again" would be the mistake** — the correct update is that the
daily-endpoint series has a **standing hole at 08-28**, and any downstream tool that reads daily
closes will keep producing NaN until it is patched at the reader, not waited out.

#### (b) The locus — re-confirmed, still both sides
Yesterday's measurement (a bench-only trim does **not** repair; both bench and ticker must be handled)
is consistent with today's repair statistics: the patch had to touch **300 of 301** tickers to produce
any score at all. A bench-only fix would have left 299 names unscored.
⚠ Repair of the *tool* is **not this stage's job** (preflight rule 1). What is patched here is this
run's working copy of the price frame, in a scratch script, labeled on every number it produces.

#### (c) ★ The recovery, its measured error, and its independent reproduction
The **5-minute** endpoint returns the full 08-28 session for every ticker tested. Validation on the
last known-good session (08-27), 24 names:

| | value |
|---|---:|
| mean abs error vs official close | **0.0181%** |
| max abs error | **0.0448%** (XLRE) |
| names with error > 0.05% | **0** |
| bars per name on 08-27 | **78 / 78** |

Repair statistics over the full 301-ticker cache: **patched 300 · trimmed 1 · proxy-covered 300 ·
names with <78 bars 9**. The single trim is **EA** (the 5m endpoint returns "possibly delisted, no
price data" for the 5d window); EA is therefore scored on data ending 08-27, one day short of the rest.

★ **Cross-run agreement.** The repaired sector table was rebuilt today from a freshly downloaded
cache by a freshly written script, without reference to yesterday's output, and lands on the same
numbers:

| Sector | 2026-08-30 repaired | **2026-08-31 repaired** | diff |
|---|---:|---:|---:|
| Materials | +0.225 | **+0.225** | 0.000 |
| Information Technology | +0.034 | **+0.033** | 0.001 |
| Health Care | +0.021 | **+0.021** | 0.000 |
| Financials | −0.072 | **−0.072** | 0.000 |
| Energy | −0.097 | **−0.097** | 0.000 |
| Consumer Discretionary | −0.262 | **−0.262** | 0.000 |
| Consumer Staples | −0.264 | **−0.264** | 0.000 |
| Industrials | −0.317 | **−0.317** | 0.000 |
| Real Estate | −0.338 | **−0.338** | 0.000 |
| Communication Services | −0.424 | **−0.422** | 0.002 |
| Utilities | −0.548 | **−0.549** | 0.001 |

⇒ Two independent reconstructions of the same session agree to ≤0.002 on 11/11 sectors. That is a
stronger warrant for the proxy than a single run's internal error estimate.

#### (d) The 08-28 proxy tape (last 5m bar close vs 08-27 official close)

| Risk-off | | Risk-on | |
|---|---:|---|---:|
| NVDA | **−4.58%** | PSX | **+1.76%** |
| HPE | **−3.90%** | MPC | **+1.47%** |
| ETN | **−3.21%** | XLC | **+1.41%** |
| ANET | **−2.87%** | XLY | **+1.15%** |
| XLK | **−1.55%** | XLE | **+0.59%** |
| XLU | **−1.09%** | XLP | **+0.41%** |
| XLI | **−0.95%** | XLF | **+0.36%** |
| AVGO | **−0.77%** | MET | **+0.26%** |
| NUE | **−0.74%** | | |
| QQQ | **−0.65%** | SPY | **−0.22%** |

- ✅ **Live authority**: **the 08-28 US session may be cited**, on condition that the words
  **"5m-proxy close (err ≤0.05%)"** appear **on the same line** as the number. It is not an official
  settle — there is no closing-auction print in it.
- 🚫 **Today's revocations**:
  1. **Do not cite an 08-28 close taken from the daily endpoint, `module_paper_book status`, or
     `pulse`.** Verified again today: `status` prints ANET **201.09**, which is the **08-27** close;
     the 08-28 proxy is **195.31**. Those tables are one session stale while labeled current.
  2. **Do not cite the primary `SECTOR_FLOW_US.json`** — it is empty (§e).
     `SECTOR_FLOW_US_REPAIRED.json` is the citable object, with its label.
  3. **Do not cite US chart shape/pattern** (`module_chart` renders 0/3 — G7).
  4. **Do not cite anything about Monday 08-31's tape** — the market had not opened at run time.

#### (e) The primary sweep's failure, quantified
`scored=0 / dropped_missing_axis=299`, `universe.n=0`, `sector_rotation=[]`, `names=[]`, `asof 08-28`.

| Run | asof | vel_cov | scored | n_axes |
|---|---|---:|---:|---:|
| 08-25 | 08-25 | 17.06% | 299 | 3 |
| 08-26 | 08-26 | 17.06% | 299 | 3 |
| 08-27 | 08-27 | 16.72% | 299 | 3 |
| 08-28 | 08-28 | 16.72% | 299 | 3 |
| 08-29 | 08-27 | **0.0%** | 299 | 3 |
| 08-30 | 08-28 | 17.06% | **0** | 3 |
| **08-31** | **08-28** | **15.72%** | **0** | 3 |

⇒ Two consecutive zero-score sweeps. The news axis and the price axis keep failing **independently**.

### G1 — News-axis liveness 🔴 FAIL on the sweep axis · ✅ direct path LIVE

| Window | KST | `fts search --days 7 --count --scope foreign` |
|---|---|---|
| **pre-sweep** | 22:11 | **6/6** — Federal Reserve **1365** · Nvidia **5292** · tariff **1993** · jobs report **82** · oil prices **1143** · data center **2551** |
| **post-sweep** | 22:25 | **4/4** — identical (1365 / 5292 / 1993 / 82) |

Five of six counts are **above** yesterday's (1237 / 5251 / 2022 / 55 / 1044 / 2467; only `tariff` is
lower) — the pool is growing, not drying up. Yet the sweep measured **15.72%**, *lower* than
yesterday's 17.06%.

★ **The decisive probe.** Direct `news_velocity` on eight names, including the two the flow ranking
put at the very bottom of the universe:

| Ticker | velocity | recent / base (7d / 30d) |
|---|---:|---|
| QCOM | **1.10** | 100 / 390 |
| DIS | **0.79** | 128 / 696 |
| ADBE | **1.12** | 150 / 575 |
| PFE | **0.77** | 56 / 313 |
| T | **0.75** | 62 / 355 |
| CSCO | **0.82** | 112 / 583 |
| **GWW** (universe rank 299) | **0.69** | 5 / 31 |
| **PCAR** (universe rank 298) | **1.12** | 6 / 23 |

⇒ **8/8 alive.** The ~84% the sweep could not measure are **not quiet** — the sweep's own 300-query
burst rate-limits itself, and `news_velocity` cannot distinguish "server refused" from "no articles"
(`module_flow/_news_velocity.py:126–136`). Note GWW and PCAR specifically: even the thinnest-covered
names in the universe return counts on a direct ask.

- 🚫 **Today's revocations**: **no theme-freshness / news-velocity citation sourced from the sweep**;
  **no "sector X is quiet" verdict from sweep coverage** — 252 of 299 were never counted. In
  particular, the 73 red names may not be described as "no news flow".
- ✅ **Live authority**: **direct queries** (`fts search` · `brief` · `thread` · `chain-hop` · `burst`
  · `flow_read.news_velocity`). ★ Fire **≤11 consecutively, ~90s pause if refused**, and write
  **"direct query, outside the sweep window"** on the same line as the number.
  **The sweep is not run again in this run.**

### G2 — Scoring-scale continuity ⚠ PASS (primary idling) · ✅ repaired series is scale-legal
Primary: `n_axes=3` (`vel_axis=false`) = yesterday's `3` ⇒ PASS by the gate's wording, but `scored=0`
so there is nothing to subtract.

Repaired run: `n_axes=3`, `mode=nonews`, `scored=299`. The previous same-mode snapshot in
`llm_outputs/sector_flow/history.json` is **08-27 `nonews`, n=299**, and **299/299 names are common**
⇒ the Δ is a like-for-like subtraction over one calendar step (08-27 → 08-28), not a mixed-scale one.

- ✅ **Live authority**: **Δflow may be cited today**, on condition that it is labeled
  **"repaired sweep (5m-proxy), 08-27 → 08-28, 3-axis nonews"** on the same line. Measured movers:
  **up** CTVA +0.77 · AAPL +0.69 · LYV +0.63 · CBRE +0.52 · SYK +0.47 · MLM +0.47 · ADM +0.47;
  **down** FTNT −0.59 · PYPL −0.55 · MPWR −0.48 · KLAC −0.45 · CIEN −0.42 · JBL −0.40 · ETN −0.39.
- 🚫 **Revoked**: **no Δ against the primary `SECTOR_FLOW_US.json`** (it has no scores), and **no Δ
  spanning the 08-29/08-30 snapshots** — those are 0-name or 0-score and cannot be an operand.
- ⚠ `history.json` was **not written** by the repair (read-only use). The stored 08-28 snapshot
  remains the empty one the primary sweep wrote; tomorrow's Δ will therefore again have to reach back
  to 08-27 unless the ghost is fixed. **Logged, not fixed — file/state repair is a human item.**

### G3 — Who owns the sector sign 🔴 FAIL (primary) · ✅ recovered via repair
Primary `§sector_rotation` = **empty array**, `§names` = **empty array**. An empty array is a
**non-observation**, not "zero flippers".

The repaired file supplies the list. **3 of 11 sectors flip sign when their top-1 name is removed:**

| Sector | wflow | ex-top1 | top-1 | top-1 weight | n |
|---|---:|---:|---|---:|---:|
| **Consumer Discretionary** | −0.262 | **+0.056** | AMZN | **40.2%** | 28 |
| **Energy** | −0.097 | **+0.074** | XOM | **30.5%** | 16 |
| **Information Technology** | +0.033 | **−0.016** | NVDA | **19.4%** | 56 |

Non-flippers, for completeness: Materials (LIN 24.7%, +0.225→+0.233) · Health Care (LLY 19.4%,
+0.021→+0.095) · Financials (BRK-B 13.9%, −0.072→−0.020) · Cons. Staples (WMT 28.9%, −0.264→−0.130) ·
Industrials (CAT 8.7%, −0.317→−0.291) · Real Estate (WELL 16.9%, −0.338→−0.415) · Comm. Services
(GOOGL 38.3%, −0.422→−0.338) · Utilities (NEE 17.7%, −0.549→−0.525).

- 🚫 **Today's revocations**: **no promotion or demotion of IT, Energy, or Consumer Discretionary
  on `wflow`** in ROTATION §2. For those three the sign belongs to one company. Substitutes available
  today: `eqflow` and `breadth` from the repaired file, the 08-28 proxy tape, FRED transmission,
  short/COT positioning, direct news — each must be named **on the same line** as the conclusion it
  supports.
- ⚠ The flipper set **changed** from the 08-29 measurement (IT/NVDA · Health Care/LLY · Energy/XOM ·
  Cons. Disc./AMZN → today Health Care no longer flips). Health Care's ex-top1 is **+0.095 vs +0.021
  headline**, i.e. LLY is now *dragging* a sector that is broader-positive underneath it.

### G4 — Risk-unit stability 🔴 FAIL
All three windows actually run (`risk_units.py --book --days {250,500,750}`, bench SPY, 1-factor
residual; logs `preflight/_ru{250,500,750}.log`). ⚠ All three end **2026-08-27** — the truncation of
the 08-28 ghost row is the one place the defect helps.

| `--days` | trading days | units @0.65 | within-group resid. corr | ARI (1st vs 2nd half) |
|---:|---:|---:|---:|---:|
| 250 | 249 | **11** | +0.6039 | 0.3188 |
| 500 | 499 | **10** | +0.5274 | 0.1899 |
| 750 | 749 | **10** | +0.5171 | 0.3810 |

- 250d membership: `U0 {028050, 316140}` · `U1 {MPC, PSX}` · then **nine singletons** — ANET, AVGO,
  ETN, HPE, MET, NDAQ, NUE, NVDA, RTX each alone. The 500/750d windows instead merge **ANET+ETN** and
  **AVGO+NVDA**. ⇒ **Whether the four AI names are one bet or four is unmeasured today; the answer
  flips with the window.**
- Threshold sensitivity: at dist 0.40–0.60 **all three windows converge on 12 units**; they diverge
  only at the chosen 0.65 ⇒ the unit count tracks an arbitrary threshold as much as it tracks the window.
- ARI (0.19–0.38) moves **opposite** to fit (+0.52–0.60) in all three — the tool's own warning not to
  trust membership. The 250d run raises its own S5 short-sample flag (249 < 250).
- 🚫 **Today's revocations**: **no single-number concentration/diversification claim.** Any
  concentration statement must carry the `--days` used **on the same line**.

### G5 — Does the universe cover the book 🔴 FAIL (freshness leg)
- **Cover leg ✅**: `data/us_universe/us_top300.csv` **300 rows**; all 11 US holdings
  (ANET·AVGO·ETN·HPE·MET·MPC·NDAQ·NUE·NVDA·PSX·RTX) present. **Missing 0.**
- **Freshness leg ❌**: mtime **2026-07-15** ⇒ **47 days** (bar ≤8; the sweep prints its own warning).
  `us_all_v2_candidate.csv` (2026-08-10) sits beside it but is **a candidate, not the wired source** —
  not switching today (file replacement is a human-approval item).
- 🚫 **Today's revocations**: **do not cite market-cap rank or cap-weighting (`wflow`) as "current
  size"** — it is a 47-day-old weighting. This compounds G3: for the three flipper sectors the sign
  rests on one name's weight, and that weight is itself seven weeks stale.
- ⚠ The 2 KR names in the book (`028050`, `316140`) are outside the US universe by construction and
  are covered by the KR desk — not a US coverage miss.

### G6 — Instrumentation accrual rate 🔴 FAIL
`snapshot_estimates.py --status`: **21 files / 41 calendar days** (2026-07-22 → 2026-08-31) ⇒
**0.51/day**. 19 more needed for the 40-day target ⇒ ideal 19 days vs **measured ~37** = **2.0x**
(threshold 1.5x). Gap median **1**, max **6**. Today's snapshot stored (120 names).
- 🚫 **Today's revocations**: **do not report `kelly_size --ic` as an evidenced size.** If used, write
  **"mechanical 1/4"** explicitly.
- ⚠ Not recoverable retroactively — a day not accrued is gone (valid sample = number of **dates**, S1).

### G7 — Tool liveness 🔴 FAIL (2/37)
`--help` exit codes: **35 of 37 are 0**.

| Group | exit 0 |
|---|---|
| `module_KIS`·`module_news_data`·`module_flow`·`module_watchlist`·`module_paper_book`·`module_valuation`·`module_business`·`module_business_us`·`module_disclosure`·`module_disclosure_us`·`module_fundamentals_us`·`module_industry_map`·`module_report_tags`·`module_inflection`·`module_macro_us`·`module_evidence` | ✅ 16/16 |
| `sector_flow`·`us_live_shortlist`·`us_setup_screener`·`us_flow`·`flow_read`·`risk_units`·`snapshot_estimates`·`exposure_rule`·`missed_ledger`·`kelly_size`·`catalyst_calendar`·`report_lint`·`reject_ledger`·`drift_watch`·`cycle_exposure`·`action_bracket`·`company_score`·`axis_inflection`·`axis_window_flow` | ✅ 19/19 |
| `python -m module_chart --help` | 🔴 **1** (prints a usage stub, not argparse — it is `module_text_chart`, positional ticker) |
| `scripts/margin_history.py --help` | 🔴 **1** (argparse `ValueError: unsupported format character`; KR-only tool, unused by this run) |

★ **The chart tool fails on live tickers with the correct positional syntax too** — this was
re-tested today rather than inherited:

| Invocation | exit |
|---|---:|
| `python -m module_chart NVDA` · `ANET` · `SPY` | **1 / 1 / 1** (traceback) |

⇒ 0/3, downstream of G0 (the render hits `cannot convert float NaN to integer` on the ghost row).
- 🚫 **Today's revocations**: **no US chart shape/pattern verdict** — the render does not complete, so
  any "the chart shows…" sentence today would be unsourced. Structural levels must be computed from
  the price series directly and labeled as such.

---

## 🧾 Everything this run **may not claim** — collected

1. **Any number in the primary `SECTOR_FLOW_US.json`** (empty). **Any `wflow`-based promotion or
   demotion of IT, Energy, or Consumer Discretionary** — one name owns each sign (G3). **Any Δ against
   the primary file or the 08-29/08-30 snapshots** (G2).
2. **News velocity / theme freshness / "it is quiet"** *when sourced from the sweep* (G1) — 252 of 299
   names were never counted, and 8/8 re-probed answered normally, including the bottom two.
3. **08-28 closes taken from the daily endpoint, the book, `status`, or `pulse`** (G0) — those are
   **08-27** wearing a current-day label. **US chart shape** (G7). **Anything about Monday 08-31's
   tape** — the market had not opened at run time.
4. **Concentration/diversification as a single number** (G4) · **market-cap-weighted "current size"**
   (G5, 47 days stale) · **`kelly_size --ic` as evidenced** (G6).

## ✅ What is **live** today
- ★ **The 08-28 US session via the 5m proxy** — validated **0.0181% mean / 0.0448% max** (n=24), and
  **independently reproduced to ≤0.002 on 11/11 sectors** against yesterday's separate reconstruction.
  Cite with the proxy label on the same line.
- ★ **The repaired sweep** `SECTOR_FLOW_US_REPAIRED.json` (299 scored, 3-axis nonews, asof 08-28),
  **including Δ vs the 08-27 snapshot** (299/299 common names, same mode) — always labeled "repaired".
- **08-27 official closes** (0/16 missing) — the last unambiguous settle.
- **Direct news queries** at every entry point, **6/6 pre-sweep · 4/4 post-sweep · 8/8 falsification**.
  ★ ≤11 consecutive, ~90s pause if refused.
- **`module_macro_us` (FRED)** · **`module_disclosure_us` / `module_business_us` /
  `module_fundamentals_us`** · **`us_flow` (FINRA short-vol / CFTC COT)** — `--help` clean, none of
  them touch the ghost bar.
- **Book positions and cost basis** (quantities and averages are not price-dated); only the *price*
  column is stale.

---
> Output: `preflight/PREFLIGHT.md` · logs `preflight/_ru{250,500,750}.log` · `../_sweep.log` ·
> `../_repair.log` · repaired sweep `../SECTOR_FLOW_US_REPAIRED.json`
