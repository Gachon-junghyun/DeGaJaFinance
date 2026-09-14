# PREFLIGHT — 2026-08-30 (Sun) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is not a report, it is a permissions table** — a FAIL is not "be careful", it is
> **"what this run may not cite today"**.
> Execution KST 2026-08-30 **22:09 clock/weekday · 22:10 tool `--help` ×37 · 22:11 US bar probe ·
> 22:11–22:12 intraday-proxy validation (24 names) · 22:12 news probe pre-sweep (6/6) ·
> 22:12–22:13 universe/book/accrual · 22:12–22:14 risk units ×3 windows ·
> 22:13–22:19 sweep (`--json`, ~6 min) · 22:19 cause isolation · 22:20 news probe post-sweep (4/4) ·
> 22:21 sweep-failed-name re-probe (5/5).**
> **Sunday · NYSE closed.** Last US session **Fri 2026-08-28**.

★ **Two-line summary**
> ① 🚨 **The ghost bar crossed the ocean and got worse. Yesterday KR was ghosted and US was clean;
>    today the US daily endpoint is ghosted on `2026-08-28` for `301/301` tickers — bench SPY included.**
>    Consequence: the sweep scored **0 of 299** names. ★ But unlike the KR case, **trimming the bench
>    alone does NOT repair it** — every ticker's own Close is NaN too, so the repair needs both sides
>    trimmed (measured: NVDA `rs20 nan→+12.9 · rs60 nan→+0.8`). **Same symptom, different locus. Do not
>    file this as "the KR bug again."**
> ② ★★ **The Friday session is recoverable, and I measured the recovery error before using it.**
>    The **5-minute intraday endpoint has all 78 bars of 08-28** while the daily endpoint has a NaN
>    Close. Validated against the last known-good session (08-27, 24 names): the proxy reproduces the
>    official close with **mean abs error 0.018% · max 0.045%**. ⇒ The 08-28 tape is citable **as a
>    labeled proxy**, and it is not a quiet tape: **NVDA −4.58% · HPE −3.90% · ETN −3.21% · ANET −2.87%
>    · XLK −1.55%** against **PSX +1.76% · MPC +1.47% · XLC +1.40% · XLY +1.15%**, with SPY only −0.22%.
>    ⇒ **A run that had accepted the instrument failure would have recorded "no data" on the single
>    most informative session for this book's largest cluster.**

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | 🔴 **FAIL** — ✅ **proxy-recovered** | Daily endpoint 08-28 Close NaN **301/301** (08-27: **0/16**). O/H/L/Volume present ⇒ Close-only NaN. **5m endpoint: 78/78 bars present**, proxy err vs 08-27 official **0.018% mean / 0.045% max (n=24)** |
| **G1** | News-axis liveness | 🔴 **FAIL** (sweep axis) · ✅ **direct path LIVE** | `vel_coverage` **17.06%** (51/299, vs 80% bar). Falsification probe **6/6 pre-sweep · 4/4 post-sweep**. ★ **5/5 names the sweep recorded as "no velocity" answer normally when asked directly** (QCOM 0.98 · DIS 0.70 · ADBE 1.03 · PFE 0.74 · T 0.75) ⇒ burst rate-limit, **not** absence of news |
| **G2** | Scoring-scale continuity | ⚠ **PASS (idling)** | Today `n_axes=3` = yesterday `n_axes=3`. **But `scored=0` — there is no operand to subtract** |
| **G3** | Who owns the sector sign | 🔴 **FAIL** | `§sector_rotation` = **`[]`** · `§names` = **`[]`**. `top1_flips_sign` list **absent** (empty array ≠ "zero flippers") |
| **G4** | Risk-unit stability | 🔴 **FAIL** | 250d **11 units** vs 500d **10** vs 750d **10**, and the *membership* differs, not just the count. All three windows end **2026-08-27** (the 08-28 ghost row is truncated) |
| **G5** | Does the universe cover the book | 🔴 **FAIL** (freshness leg) | Cover ✅ **11/11** US holdings in `us_top300.csv` (300 rows) · missing 0. Freshness ❌ **46 days old** (bar ≤8) |
| **G6** | Instrumentation accrual rate | 🔴 **FAIL** | 20 files / 40 calendar days = **0.50/day** ⇒ ETA **~40 days** vs ideal 20 = **2.0×** (threshold 1.5×) |
| **G7** | Tool liveness | 🔴 **FAIL** (2/37) | 35 of 37 entry points exit 0. `module_chart --help` **exit=1** *and* **renders 0/3 US tickers** (NVDA·ANET·SPY all exit 1) · `margin_history.py --help` **exit=1** (KR-only tool, unused this run) |

---

## Gate detail

### G0 — Bar completeness 🔴 FAIL, ✅ proxy-recovered ★today's principal finding

#### (a) The defect — Close-only NaN, now on the US side
Direct `yfinance` probe, `auto_adjust=False`, 16 US tickers (11 book holdings + SPY + 4 sector ETFs):

| Session | Close NaN |
|---|---:|
| 2026-08-26 | **0** / 16 |
| 2026-08-27 | **0** / 16 |
| **2026-08-28 (Fri, last session)** | **16 / 16** |

Widened to the sweep's own price cache (`prices_2026-08-30.pkl`, 301 columns): **301/301 have a
trailing 08-28 Close NaN.** SPY row 08-28: `O 771.76 · H 775.29 · L 768.31 · V 36,342,284 · C NaN`.
⇒ **Row count normal · Volume normal · O/H/L normal — exactly one column empty, and that column is
the input to every downstream calculation.** This is the same silent class the KR desk characterised
on 08-30 KST 08:18; today it is the US side that is empty.

#### (b) ★ The locus is NOT the same as KR's — measured, not assumed
The KR run isolated its failure to **one bench cell** (`^KS11`) and proved it by swapping the bench.
I ran the identical experiment on US and it **falsified the transfer**:

| Input | NVDA result |
|---|---|
| bench SPY raw (ghost row in) | `obv −0.020 · vsurge 1.38 · **rs20 nan · rs60 nan**` |
| bench SPY **ghost row trimmed**, ticker untouched | `obv −0.020 · vsurge 1.38 · **rs20 nan · rs60 nan**` ← **no repair** |
| **both** bench and ticker trimmed | `obv **+0.036** · vsurge 1.25 · **rs20 +12.9 · rs60 +0.8**` ← repaired |

Reproduced on XOM (`rs20 −4.3 · rs60 +3.1`), LLY (`−2.1 · +9.0`), GOOGL (`−1.9 · −7.4`), JPM (`−3.0 · +16.2`).
⇒ **On US the ghost is in the bench *and* in all 300 constituents**, so a bench-only fix is a
no-op here. ⚠ Note the second-order effect: `obv_norm` also moves (NVDA −0.020 → +0.036) because the
ghost row carries **real volume with a missing close** — the OBV path ingests the volume and mis-signs it.
⚠ Repair is **not this stage's job** (preflight rule 1); this is a measurement, and it is left as a
human-approval item.

#### (c) ★ The recovery, and its measured error
The **5-minute** endpoint returns the full 08-28 session (**78 bars**, last at 15:55 ET) for every
ticker tested. Validation on the last known-good session (08-27), 24 names:

| | value |
|---|---:|
| mean abs error vs official close | **0.018%** |
| max abs error | **0.045%** (XLRE) |
| names with error > 0.05% | **0** |

08-28 proxy tape (last 5m bar close, % vs 08-27 official close):

| Risk-off | | Risk-on | |
|---|---:|---|---:|
| NVDA | **−4.58%** | PSX | **+1.76%** |
| HPE | **−3.90%** | MPC | **+1.47%** |
| ETN | **−3.21%** | XLC | **+1.40%** |
| ANET | **−2.87%** | XLY | **+1.15%** |
| XLK | **−1.55%** | XLE | **+0.59%** |
| XLU | **−1.09%** | XLF | **+0.36%** |
| XLI | **−0.95%** | MET | **+0.26%** |
| AVGO | **−0.77%** | | |
| QQQ | **−0.65%** | SPY | **−0.22%** |

- ✅ **Live authority**: **the 08-28 US session may be cited**, on the condition that the words
  **"5m-proxy close (err ≤0.05%)"** appear on the same line as the number. It is not an official settle
  (no closing-auction print).
- 🚫 **Today's revocations**:
  1. **Do not cite an 08-28 close taken from the daily endpoint, the book, or `pulse`** — those tables
     show **08-27** while labelling it current (verified: `module_paper_book status` prints ANET 201.09,
     which is the **08-27** close; the 08-28 proxy is **195.31**).
  2. **Do not cite `SECTOR_FLOW_US.json`** — any number in it (§(d), the file is empty).
  3. **Do not cite US chart shape/pattern** (`module_chart` renders 0/3, G7).

#### (d) The sweep's failure, quantified
`scored=0 / dropped_missing_axis=299`, `universe.n=0`, `sector_rotation=[]`, `names=[]`, `asof 2026-08-28`.
⚠ **This is the first US `scored=0` in the visible history** — the previous five runs all scored 299:

| Run | asof | vel_cov | scored | n_axes |
|---|---|---:|---:|---:|
| 08-25 | 08-25 | 17.06% | 299 | 3 |
| 08-26 | 08-26 | 17.06% | 299 | 3 |
| 08-27 | 08-27 | 16.72% | 299 | 3 |
| 08-28 | 08-28 | 16.72% | 299 | 3 |
| 08-29 | 08-27 | **0.0%** | 299 | 3 |
| **08-30** | **08-28** | **17.06%** | **0** | 3 |

⇒ The news axis and the price axis fail **independently**: 08-29 lost news and kept price; today
kept news-at-17% and lost price.

### G1 — News-axis liveness 🔴 FAIL on the sweep axis · ✅ direct path LIVE

| Window | KST | `fts search --days 7 --count --scope foreign` |
|---|---|---|
| **pre-sweep** | 22:12 | **6/6** — Federal Reserve **1237** · Nvidia **5251** · tariff **2022** · jobs report **55** · oil prices **1044** · data center **2467** |
| **post-sweep** | 22:20 | **4/4** — identical values (1237 / 5251 / 2022 / 55) |

★ **The decisive probe.** I took five names the sweep had just recorded as *no velocity* and asked
for them directly, ~2 minutes later:

| Ticker | sweep | direct probe (recent/base, 7d/30d) |
|---|---|---|
| QCOM | `velocity: null` | **0.98** (99 / 434) |
| DIS | `velocity: null` | **0.70** (34 / 209) |
| ADBE | `velocity: null` | **1.03** (145 / 605) |
| PFE | `velocity: null` | **0.74** (55 / 317) |
| T | `velocity: null` | **0.75** (64 / 365) |

⇒ **5/5 alive.** The 83% of names the sweep could not measure are **not** quiet — the sweep's own
300-query burst rate-limits itself, and `news_velocity` cannot distinguish "server refused" from
"no articles" (`module_flow/_news_velocity.py:126–136`). ⚠ I also checked the alternative hypothesis —
that the successes were the first N before a ban — and **falsified it**: on the 08-28 run the 50
successes sit at index 8…298, scattered, not a prefix. The survivors are the mega-caps and the semis
(MSFT·AAPL·NVDA·GOOGL·AMZN·META·JPM·V·MA·XOM·LLY·WMT·UNH + MU·MRVL·LRCX·KLAC·AMAT·ASML·INTC·WDC·ARM·AMD),
i.e. the highest-article-count names win the race for the few slots the limiter grants.
- 🚫 **Today's revocations**: **no theme-freshness / news-velocity citation sourced from the sweep**;
  **no "sector X is quiet" verdict from sweep coverage** — 248 of 299 were never counted.
- ✅ **Live authority**: **direct queries** (`fts search` · `brief` · `thread` · `chain-hop` · `burst`).
  ★ Fire **≤11 consecutively and wait ~90s if refused**, and write **"direct query, outside the sweep
  window"** on the same line as the number.

### G2 — Scoring-scale continuity ⚠ PASS (idling)
Today `n_axes=3` (`vel_axis=false`) = yesterday `n_axes=3`. Same axis count, so PASS by the gate's
wording. **But `scored=0`, so there is nothing to subtract.**
- 🚫 **Today's revocations**: **no Δflow · no "newly green" · no "flow rose/fell" lists.**
- ✅ Live: citing the series **through the 08-28 run (asof 08-28)** as "the flow picture as of Friday's
  own run", provided the vintage is on the same line. The last valid US sweep observation is the
  **08-28 run**; 08-29's had a dead news axis and today's has no scores at all.

### G3 — Who owns the sector sign 🔴 FAIL
`§sector_rotation` = **empty array** · `§names` = **empty array**. The `top1_flips_sign` list does not
exist — which is **different from "zero flippers"** (zero is an observation, empty is a non-observation).
- 🚫 **Today's revocations**: **no `wflow`-based promotion/demotion in ROTATION §2.** The substitutes
  (`eqflow`, `breadth`) live in the same empty file, so they are gone too. Any sector call today must
  come from **axes outside the sweep** (FRED transmission matrix, the 08-28 proxy tape, short/COT
  positioning, direct news), and must say so **on the same line as the conclusion**.
- ⚠ For reference, the last measured flipper list is the **08-29 run** (4 of 11 sectors flip sign when
  their top-1 name is removed: **IT/NVDA · Health Care/LLY · Energy/XOM · Cons. Disc./AMZN**). That is
  **a stale observation carried for context, not today's measurement.**

### G4 — Risk-unit stability 🔴 FAIL
All three windows actually run (`risk_units.py --book --days {250,500,750}`, bench SPY, 1-factor
residual; logs `preflight/_ru{250,500,750}.log`). ⚠ All three end at **2026-08-27** — the 08-28 ghost
row is truncated, which is the one place the defect helped.

| `--days` | trading days | units | within-group resid. corr | ARI (1st vs 2nd half) | AI cluster placement |
|---:|---:|---:|---:|---:|---|
| 250 | 249 | **11** | +0.6039 | 0.3188 | ANET·AVGO·ETN·NVDA **all separate** |
| 500 | 499 | **10** | +0.5274 | 0.1899 | **ANET+ETN** one unit · **AVGO+NVDA** one unit |
| 750 | 749 | **10** | +0.5171 | 0.3810 | identical to 500d |

- Threshold sensitivity: at dist 0.40–0.60 **all three windows converge on 12 units**; they split only
  at the chosen 0.65 ⇒ the unit count moves with the arbitrary threshold, not only with the window.
- ARI (0.19–0.38) moves **opposite** to fit (+0.52–0.60) in all three — the tool's own warning not to
  trust membership.
- The 250d run flagged its own sample warning (S5: 249 < 250 days); calendar intersection loses 21 days
  on every non-US name, and KRW/USD axes are mixed.
- 🚫 **Today's revocations**: **no single-number concentration/diversification claim.** If cited, the
  `--days` used must sit **on the same line** as the conclusion. **Whether ANET·ETN·AVGO·NVDA are one
  bet or four is unmeasured today** — the answer flips with the window.

### G5 — Does the universe cover the book 🔴 FAIL (freshness leg)
- **Cover leg ✅**: `data/us_universe/us_top300.csv` **300 rows**; all 11 US holdings
  (ANET·AVGO·ETN·HPE·MET·MPC·NDAQ·NUE·NVDA·PSX·RTX) present. **Missing 0.**
- **Freshness leg ❌**: the sweep warns on itself — **`us_top300.csv` 46 days old**, market caps stale
  (bar ≤8 days, weekly rebuild recommended). File mtime **2026-07-15**. ⚠ `us_all_v2_candidate.csv`
  (2026-08-10) sits beside it but is **a candidate, not the wired source** — not switching today
  (file replacement is a human-approval item).
- 🚫 **Today's revocations**: **do not cite market-cap rank or cap-weighting (`wflow`) as "current size"**
  — it is a 46-day-old weighting. The substitute is equal-weight/breadth, which is unavailable today
  anyway (G3), so the G3 prohibition dominates.
- ⚠ Note the 2 KR names in the book (`028050`, `316140`) are outside the US universe by construction;
  they are covered by the KR desk's own universe and are **not** a US coverage miss.

### G6 — Instrumentation accrual rate 🔴 FAIL
`snapshot_estimates.py --status`: **20 files / 40 calendar days** (2026-07-22 → 2026-08-30) ⇒
**0.50/day**. 20 more needed to reach the 40-day target ⇒ ideal 20 days vs **measured ~40** = **2.0×**
(threshold 1.5×). Gap median **1 day**, max **6**. Today's snapshot stored (120 names).
- 🚫 **Today's revocations**: **do not report `kelly_size --ic` as an evidenced size.** If used, write
  **"mechanical 1/4"** explicitly.
- ⚠ Not recoverable retroactively — a day not accrued is gone (valid sample = number of **dates**, rule S1).

### G7 — Tool liveness 🔴 FAIL (2/37)
`--help` exit codes: **35 of 37 are 0**.

| Group | exit 0 |
|---|---|
| `module_KIS`·`module_news_data`·`module_flow`·`module_watchlist`·`module_paper_book`·`module_valuation`·`module_business`·`module_business_us`·`module_disclosure`·`module_disclosure_us`·`module_fundamentals_us`·`module_industry_map`·`module_report_tags`·`module_inflection`·`module_macro_us`·`module_evidence` | ✅ 16/16 |
| `sector_flow`·`us_live_shortlist`·`us_setup_screener`·`us_flow`·`flow_read`·`risk_units`·`snapshot_estimates`·`exposure_rule`·`missed_ledger`·`kelly_size`·`catalyst_calendar`·`report_lint`·`reject_ledger`·`drift_watch`·`cycle_exposure`·`action_bracket`·`company_score`·`axis_inflection`·`axis_window_flow` | ✅ 19/19 |
| `python -m module_chart --help` | 🔴 **1** (usage stub exits 1 — not argparse) |
| `scripts/margin_history.py --help` | 🔴 **1** (argparse `ValueError: unsupported format character`; KR-only tool, unused by this run) |

★ **The chart tool is not merely a broken `--help` — it fails on live tickers**:

| Ticker | exit |
|---|---:|
| `NVDA` · `ANET` · `SPY` | **1 / 1 / 1** |

⇒ 0/3. Downstream of G0 (the render hits `cannot convert float NaN to integer` on the ghost row).
- 🚫 **Today's revocations**: **no US chart shape/pattern verdict** — the render does not complete, so
  any "the chart shows…" sentence today would be unsourced. Structural levels must be computed from the
  price series directly and labelled as such.

---

## 🧾 Everything this run **may not claim** — collected

1. **Any number in `SECTOR_FLOW_US.json`** (empty) · **any flow-based sector promotion/demotion** (G3) ·
   **any Δflow** (G2).
2. **News velocity / theme freshness / "it is quiet"** *when sourced from the sweep* (G1) — 248 of 299
   names were never counted, and 5/5 re-probed answered normally.
3. **08-28 closes taken from the daily endpoint, the book, `status`, or `pulse`** (G0) — those are
   **08-27** wearing a current-day label. **US chart shape** (G7).
4. **Concentration/diversification as a single number** (G4) · **market-cap-weighted "size"** (G5) ·
   **`kelly_size --ic` as evidenced** (G6).

## ✅ What is **live** today
- ★ **The 08-28 US session via the 5m proxy** — validated at **0.018% mean / 0.045% max** error against
  the 08-27 official closes (n=24). Cite with the proxy label on the same line.
- **08-27 official closes** (0/16 missing) — the last unambiguous settle.
- **Direct news queries** at every entry point (`fts search`·`brief`·`thread`·`chain-hop`·`burst`),
  **6/6 pre-sweep and 4/4 post-sweep, plus 5/5 on names the sweep had failed.** ★ ≤11 consecutive,
  ~90s pause if refused. **The sweep is not run again in this run.**
- **`module_macro_us` (FRED)** · **`module_disclosure_us` / `module_business_us` / `module_fundamentals_us`**
  · **`us_flow` (FINRA short-vol / CFTC COT)** — all `--help` clean, none of them touch the ghost bar.
- **Book positions and cost basis** (quantities and averages are not price-dated); only the *price*
  column is stale.

---
> Output: `preflight/PREFLIGHT.md` · logs `preflight/_ru{250,500,750}.log` · `../_sweep.log`
