# PREFLIGHT — 2026-09-04 (Fri) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is not a report, it is a permissions table** — a FAIL is not "be careful", it is
> **"what this run may not cite today"**.
> Execution KST 2026-09-04 **22:10 clock/weekday · 22:10–22:11 news probe pre-sweep (6/6)
> · 22:11–22:13 sweep (`--json --refresh`) · 22:11–22:12 tool `--help` ×44 · 22:12 chart live ×3
> · 22:12–22:14 risk units ×3 windows · 22:13 universe/book/accrual · 22:14 direct 16-ticker bar
> probe · 22:14–22:15 hole quantification vs yesterday's cache · 22:15–22:17 clean-baseline rescore
> · 22:17–22:21 falsification probe (two cadences + 40-name burst) · 22:22 news probe post-sweep
> (4/4) · 22:22 ETF tape.**
> **Friday 09:10–09:22 ET — NYSE had NOT opened at any point during this preflight** (opens 09:30 ET).
> Last completed US session **Thu 2026-09-03**. ⇒ Every price statement below is about
> **Thursday 09-03 or earlier**. A partial 2026-09-04 row already exists at the vendor (`^VIX`
> quoted, all 21 ETFs NaN) and was **truncated out** — it must not be cited.

★ **Three-line summary**
> ① ✅ **The 08-28 vendor hole is HEALED — the single largest instrument state change in two weeks.**
>    Yesterday's cache carried **258 of 301** names with a NaN Close at 2026-08-28; today's fresh
>    cache carries **2** (`APH`, `EA`). The 42 bars that were already official are returned
>    **byte-identical** (mean |err| **0.000000%**, max 0.000000%) — the vendor filled holes, it did
>    not rewrite history. ⇒ **The 5m-proxy repair is retired for this run. No
>    `SECTOR_FLOW_US_REPAIRED.json` is produced, and none is needed** — the primary file's OBV axis
>    is clean for the first time since 2026-08-28.
> ② 🔴 **But the healing makes yesterday's stored baseline the contaminated side.** The Δ column
>    inside `SECTOR_FLOW_US.json` subtracts a **holed** 09-02 snapshot from a **healed** 09-03 one.
>    Measured directly by rescoring 09-02 off the healed cache: mean |Δ| **0.1078**, max **0.5570**,
>    **19 of 299 sign flips**, and at sector level the stored Δ is wrong by as much as **0.177**
>    (Utilities stored +0.308 vs clean **+0.131**; Health Care stored −0.207 vs clean **−0.069**).
>    ★ **Fixed inside this preflight rather than merely flagged** — a clean 09-02 baseline was
>    recomputed and the clean Δ is what this run may cite.
> ③ ★ **The news-axis diagnosis from the last run is OVERTURNED, by its own method.** The 09-02 run
>    concluded the `None`s were a *request-spacing* artifact and prescribed "≥9s spacing". Today the
>    same fixed-name-set experiment shows **8 of 10 sweep-`None` names return real velocities at
>    1.5s spacing**, the identical 10 give the **identical** answers at 9s (0 flipped on cadence),
>    and a **40-name / 80-query burst at ~0s spacing scored 40/40**. The real signature is
>    **positional**: the sweep measured universe positions **0–49 and nothing after** — a hard
>    cutoff at exactly 50 names inside its own ~600-query run. ⇒ Spacing was never the variable;
>    **burst volume within one sweep** is. The prescription changes accordingly.

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | ✅ **PASS — hole healed** | 08-28 Close NaN **258/301 → 2/301** in 24h. Direct 16-ticker probe **0/16 on all 13 sessions** 08-18→09-03. Sweep cache 301 cols, NaN ≤2 on every row (`EA` always, `APH` on 4). `dropped_missing_axis=1`, scored **298**. asof **2026-09-03** |
| **G1** | News-axis liveness | 🔴 **FAIL** (sweep axis) · ✅ **direct path LIVE** | `vel_coverage` **16.72%** (50/298, bar 80%). Probe **6/6 pre-sweep · 4/4 post-sweep**. ★ Falsification: **8/10 at 1.5s**, **8/10 at 9s** (0 cadence flips), **40/40 in an 80-query burst at ~0s**. Sweep coverage is **universe positions 0–49 exactly** |
| **G2** | Scoring-scale continuity | ✅ **PASS on scale** · ⚠ stored baseline holed · ★ **repaired here** | `n_axes=3`, `mode=nonews`, `scored=298`. `prev` resolves to **2026-09-02** (`nonews`, 299) ⇒ genuine **one-session** Δ. Stored-baseline contamination mean **0.1078** / max **0.5570** / **19/299** sign flips ⇒ clean 09-02 baseline recomputed |
| **G3** | Who owns the sector sign | ✅ **PASS** (list printed) · ⚠ guard misses the largest case | **1 of 11 flips** — Cons. Disc./**AMZN** (40.2%), −0.251 → **+0.051**. ★ Alphabet is **76.6%** of Comm. Services under **two** tickers; `top1_flips_sign` prints **False**; ex-both-classes `wflow` **−0.396 → +0.294**, swing **0.690** |
| **G4** | Risk-unit stability | 🔴 **FAIL** | 250d **12 units** · 500d **11** · 750d **10**; membership differs. ARI **0.3188 / 0.2328 / 0.7937** vs within-group fit **+0.8511 / +0.6145 / +0.5178**. All three windows end **2026-09-03** |
| **G5** | Does the universe cover the book | 🔴 **FAIL** (freshness leg) | Cover ✅ **11/11** US holdings in `us_top300.csv` (300 rows), missing **0**. Freshness ❌ **51 days** (mtime 2026-07-15; bar ≤8) |
| **G6** | Instrumentation accrual rate | 🔴 **FAIL** | **25 files / 45 calendar days = 0.56/day** ⇒ ETA **~27 days** vs ideal 15 = **1.8×** (threshold 1.5×). Gap median 1, max 6 |
| **G7** | Tool liveness | 🟡 **PASS with 2 named exceptions** | **42 of 44** `--help` exit 0. `module_chart --help` **exit=1** *but* live render **3/3** (NVDA·ANET·SPY) ⇒ **chart citation stands**. `scripts/margin_history.py` **exit=1** (KR-only, unused here) |

---

## Gate detail

### G0 — Bar completeness ✅ PASS · ★ today's principal finding: the hole healed

#### (a) The 08-28 hole is gone
The defect this desk has carried since 2026-08-28 — a partial vendor session that zeroed two of
twenty sessions inside every OBV window — **closed between yesterday's run and today's**.

| | 2026-09-03 run (T+4 cache) | **2026-09-04 run (T+5 cache)** |
|---|---:|---:|
| names with NaN Close at 2026-08-28 | **258 / 301** | **2 / 301** (`APH`, `EA`) |
| names with the official bar | 43 | **299** |
| change in 24h | 0 | **+256** |

★ **The backfill is additive, not a rewrite.** Taking the **42** names that already had an official
08-28 bar in yesterday's cache and comparing them to today's:
**mean |err| 0.000000% · max 0.000000%.** The vendor filled holes and left existing bars untouched
— which is the necessary condition for treating the new bars as official rather than as a proxy.

⇒ **Consequences, stated as permissions:**
- ✅ **`obv_norm` / `obv_state` / `flow_score` may now be cited from the PRIMARY
  `SECTOR_FLOW_US.json`.** The revocation that stood on 09-01 / 09-02 / 09-03 is **lifted**.
- ✅ **08-28 closes and volumes may be cited plainly**, with no "5m-proxy" label, for 299 of 301.
- 🚫 **`SECTOR_FLOW_US_REPAIRED.json` is NOT produced today and must not be sought by any
  downstream stage** — the repair existed only to route around this hole. Downstream readers that
  glob for it fall back to the primary file (which is what the protocol names anyway).
- ⚠ **This does not retroactively clean history.** `llm_outputs/sector_flow/history.json` entries
  for 2026-08-28 … 2026-09-02 were all written off the holed cache. That is G2's problem, below.

#### (b) The head of the series
Direct `yfinance` probe, `auto_adjust=False`, 16 US tickers (11 book holdings + SPY + 4 sector ETFs),
2026-08-18 → 2026-09-03:

| Session | Close NaN |
|---|---:|
| 08-18, 08-19, 08-20, 08-21, 08-24, 08-25, 08-26, 08-27 | **0 / 16** each |
| **2026-08-28 (Fri)** | **0 / 16** ← was 10/16 two runs ago |
| 08-31, 09-01, 09-02 | **0 / 16** each |
| **2026-09-03 (Thu, last session)** | **0 / 16** |

In the sweep's own fresh cache (`prices_2026-09-04.pkl`, 301 columns, downloaded today, 86 rows,
last row **2026-09-03**) NaN is **≤2 on every row**: `EA` on all rows (the vendor answers "possibly
delisted"), `APH` on 08-28, 09-01, 09-02, 09-03. Both fall out of the scored set —
`scored=298`, `n_requested=300`, `dropped_missing_axis=1`.

#### (c) The 09-03 session (official, complete)
Last completed session, from the daily endpoint, truncated at 09-03 (a partial 09-04 row exists and
was discarded):

| Risk-on | 1d | Risk-off | 1d |
|---|---:|---|---:|
| GLD | **+1.85%** | XLP | −0.32% |
| XLF | **+1.56%** | UUP | −0.57% |
| XLY | **+1.39%** | XLB | −0.62% |
| XLK | **+1.29%** | XLE | **−0.74%** |
| XLRE | +1.19% | ^VIX | **−5.79%** (to 14.32) |
| QQQ | +1.19% | | |
| SPY | **+1.05%** | | |

Also: XLI +1.03% · XLC +0.85% · XLU +0.84% · USO +0.67% · RSP +0.66% · IWM +0.40% · SMH +0.39% ·
XLV +0.18% · TLT +0.15% · HYG +0.13%.

Book holdings, 09-02 → 09-03: **HPE +5.04% · NDAQ +3.12% · MET +2.91% · ANET +2.87% ·
NVDA +1.80% · ETN +1.60% · RTX +0.67% · MPC +0.18%** · PSX −0.56% · NUE −0.57% · **AVGO −2.74%**.

- ✅ **Live authority**: **the 09-03 session may be cited plainly** from the daily endpoint, and so
  may every session back through 08-18 including 08-28.
- 🚫 **Today's revocations**:
  1. **Nothing about Friday 2026-09-04's tape** — NYSE had not opened during this preflight, and the
     vendor's partial 09-04 row (VIX quoted, all 21 ETFs NaN) is an incomplete bar.
  2. **`EA` and `APH`** — unscored (`n=298`, not 300); no flow / OBV / RS / Δ claim about either.

### G1 — News-axis liveness 🔴 FAIL on the sweep axis · ✅ direct path LIVE · ★ mechanism re-diagnosed

| Window | KST | `fts search --days 7 --count --scope foreign` |
|---|---|---|
| **pre-sweep** | 22:10–22:11 | **6/6** — Federal Reserve **1506** · Nvidia **4475** · tariff **1841** · jobs report **279** · oil prices **1442** · data center **2643** |
| **post-sweep** | 22:22 | **4/4** — identical (1506 / 4475 / 1841 / 279) |

Yet the sweep measured **16.72%** (50 of 298), tripping its own 80% bar and dropping the velocity
axis for the whole run (`vel_axis=false`, `n_axes=3`).

★ **What the last run concluded, and why it is wrong.** The 2026-09-02 preflight ran a fixed-name
set at 1.5s vs 9s spacing, found 7 of 7 `None`s flip to real numbers, and prescribed **"≥9s
spacing"**. Re-running that experiment today on a fresh fixed set of ten sweep-`None` names:

| Ticker | **1.5s cadence** | **9s cadence** | recent / base (7d / 30d) |
|---|---:|---:|---|
| CRM | **1.51** | 1.51 | 363 / 1030 |
| MDT | **2.15** | 2.15 | 91 / 181 |
| DE | **0.80** | 0.80 | 44 / 236 |
| CTVA | **1.25** | 1.25 | 7 / 24 |
| HPE | **2.11** | 2.11 | 114 / 232 |
| NEM | **0.86** | 0.86 | 51 / 253 |
| TER | **0.39** | 0.39 | 12 / 133 |
| JCI | **1.15** | 1.15 | 7 / 26 |
| SLB | None (0/0) | None (0/0) | ⚠ **my own probe** passed the multi-word string "SLB Schlumberger"; the sweep's actual query is `SLB`, which returns **77 / 140, vel 2.36** |
| MSTR | None (0/0) | None (0/0) | ⚠ same artifact; sweep query `MSTR\|MicroStrategy` returns **135 / 465, vel 1.24** |

⇒ **0 of 10 flipped on cadence.** Both `None`s were **my own query-string error**, reproduced
identically at both spacings, and both names return real numbers under the query the sweep actually
builds. **Spacing is not the variable.**

★ **The variable is burst position.** Two measurements:
1. A **40-name / 80-query burst at ~0s spacing** returned **40/40** real velocities — first `None`
   at *none*. If spacing mattered this should have collapsed immediately.
2. Mapping the sweep's measured names back onto universe order (market-cap desc): coverage is
   **positions 0–49, and None for 50–297.** Not a distribution — **a cutoff at exactly 50 names**
   (=100 requests) inside the sweep's own ~600-query run.

⇒ The refusal is a **quota on burst volume within a single sweep**, and `news_velocity` cannot
distinguish "server refused" from "no articles" (`module_flow/_news_velocity.py:126–136`), so the
sweep silently reports 83% of the universe as unmeasured. ★ Note **`CRM`** is the sweep's rank-3
name by flow and one of the 248 it could not count; its true velocity is **1.51 — accelerating**.

⚠ **Two ticker-token false positives were observed in passing** and are recorded, not acted on:
`AME` returns **6159** 7d hits and `HES` **6364** — three-letter tickers colliding with ordinary
English tokens. Any per-name velocity on a 2–3 letter ticker needs the company-name form.

- 🚫 **Today's revocations**: **no theme-freshness / news-velocity citation sourced from the sweep**;
  **no "sector X is quiet" verdict from sweep coverage** — 248 of 298 were never counted. The 89 red
  names may **not** be described as having "no news flow".
- ✅ **Live authority**: **direct queries** (`fts search` · `brief` · `thread` · `chain-hop` ·
  `burst` · `flow_read.news_velocity`) — **measured 40/40 at zero spacing this run**, so the ≥9s
  prescription is **retired**. The operative limit is **total queries in one burst**, so: keep any
  single fan-out under ~40 names, and write **"direct query, outside the sweep window"** on the same
  line as the number. **The sweep is not run again in this run.**

### G2 — Scoring-scale continuity ✅ PASS on scale · ★ baseline repaired inside this preflight
Scale: `n_axes=3`, `vel_axis=false`, `mode=nonews`. `prev_snapshot` resolves to **2026-09-02**
(`_mode=nonews`, 299 names) ⇒ **no mixed-scale subtraction risk**, and the Δ spans **exactly one
session** (09-02 → 09-03).

⚠ **But the stored baseline was scored on the holed cache.** Today's snapshot is healed; the 09-02
entry in `history.json` is not. Today's Δ column is therefore **healed-minus-holed**. This was
**measured, not estimated** — the 09-02 session was rescored from today's healed cache (truncated to
09-02, `sector_flow`'s own `one_name`/`score_all`, 299 scored, history not written):

| stored 09-02 vs clean 09-02 | value |
|---|---:|
| mean abs Δ `flow_score` | **0.1078** |
| median | 0.0550 |
| max | **0.5570** |
| **sign flips** | **19 / 299 (6.4%)** |

Worst: **CVS −0.615→−0.147 · TRI +0.031→+0.517 · FANG +0.151→+0.702 · LLY +0.433→−0.124 ·
CCI −0.235→+0.285 · ANET −0.284→−0.720 · APH −0.497→−0.056 · AEP −0.340→+0.112.**
⚠ **`ANET` and `LLY` are the cases that matter**: a book holding and a DEEP-relevant large cap, both
of whose stored yesterday-scores were wrong by >0.4.

**Clean one-session Δ (09-02 → 09-03, healed both sides, cap-weighted), with the stored — wrong —
column beside it:**

| Sector | **clean Δ (cite this)** | stored Δ (do not) | eq-wt Δ | n |
|---|---:|---:|---:|---:|
| Utilities | **+0.131** | +0.308 | +0.159 | 15 |
| Real Estate | **+0.091** | +0.091 | +0.109 | 12 |
| Financials | **+0.077** | +0.003 | +0.122 | 47 |
| Comm. Services | **+0.058** | +0.059 | −0.044 | 12 |
| Industrials | **+0.051** | +0.023 | +0.059 | 50 |
| Cons. Discretionary | **+0.023** | −0.022 | +0.050 | 28 |
| Information Technology | **+0.018** | +0.025 | +0.023 | 55 |
| Cons. Staples | **−0.031** | −0.074 | −0.035 | 19 |
| Materials | **−0.035** | −0.123 | −0.027 | 12 |
| Health Care | **−0.069** | −0.207 | −0.036 | 32 |
| Energy | **−0.151** | −0.075 | −0.099 | 16 |

★ **Three sectors change ordinal position between the two columns** (Financials, Cons. Disc.,
Materials) and one changes by more than its own magnitude (Health Care). A run that cited the stored
column would have called Health Care the second-worst sector on flow momentum; on clean data it is
fourth.

Name movers on the clean Δ: **up** AXON +0.84 · HPE +0.72 · IBKR +0.58 · UPS +0.52 · D +0.51 ·
EXC +0.43 · DDOG +0.42 · STT +0.42 · VRT +0.40 · F +0.40; **down** MSI −0.57 · ADSK −0.44 ·
STX −0.44 · ABT −0.44 · ASML −0.40 · LLY −0.38 · AMD −0.35 · XOM −0.35 · BKNG −0.35 · BKR −0.33.

- ✅ **Live authority**: **Δflow may be cited as a magnitude today**, labelled **"clean one-session Δ,
  09-02 → 09-03, both sides rescored on healed data, 3-axis nonews"** on the same line.
  Source file: `preflight/_cleanbase.json`.
- 🚫 **Revoked**: **the `delta` field inside `SECTOR_FLOW_US.json` may not be cited at all today** —
  it is healed-minus-holed, wrong by up to 0.557 per name and 0.177 per sector.
- ⚠ **Logged, not fixed**: writing a corrected snapshot into shared `history.json` is a
  human-approval item (P5). Tomorrow's run compares healed-to-healed and this whole clause
  disappears.

### G3 — Who owns the sector sign ✅ PASS (list printed) · ⚠ the guard misses the largest case
**1 of 11 sectors flips sign when its top-1 name is removed:**

| Sector | wflow | ex-top1 | top-1 | top-1 weight | n |
|---|---:|---:|---|---:|---:|
| **Consumer Discretionary** | −0.251 | **+0.051** | AMZN | **40.2%** | 28 |

Non-flippers, in full: Energy (XOM 30.5%, +0.386→+0.572) · Health Care (LLY 19.4%, +0.140→+0.295) ·
Utilities (NEE 17.7%, +0.108→+0.051) · Materials (LIN 24.7%, +0.013→+0.011) · IT (NVDA 19.5%,
−0.080→−0.101) · Real Estate (WELL 16.9%, −0.096→−0.200) · Financials (BRK-B 13.9%, −0.114→−0.054) ·
Cons. Staples (WMT 28.9%, −0.164→−0.053) · Comm. Services (GOOGL 38.3%, −0.396→−0.292) ·
Industrials (CAT 8.7%, −0.461→−0.435).

★ **`D459` reproduces at essentially unchanged size.** Alphabet occupies **76.6%** of Communication
Services under **two tickers** (GOOGL 38.3%, flow −0.562 + GOOG 38.3%, flow −0.651). The one-name
guard removes only one class, so it prints `top1_flips_sign: False` while the true ex-Alphabet
reading is **wflow −0.396 → +0.294, a swing of 0.690** (09-02: 0.763). `eqflow` is **+0.029**, i.e.
flat, and **+0.156** ex-Alphabet. **The negative sign on this sector is one company held twice** —
the other ten names are 7 accumulating / 3 not (META +0.399, WBD +0.521, VZ +0.474, T +0.400,
CMCSA +0.317, DIS +0.236, NFLX +0.056; TTWO −0.367, LYV −0.386, TMUS −0.091).

- 🚫 **Today's revocations**: **no promotion or demotion of Consumer Discretionary on `wflow`**
  (AMZN owns the sign) · **no `wflow`-based claim about Communication Services in either direction**
  — the sign is Alphabet's two share classes and the instrument's own guard cannot see it.
  Substitutes available today: `eqflow`, `breadth`, the official 09-03 tape, the clean Δ, FRED
  transmission, short/COT positioning, direct news — each named **on the same line** as the
  conclusion it supports.

### G4 — Risk-unit stability 🔴 FAIL
All three windows actually run (`risk_units.py --book --days {250,500,750}`, bench SPY, 1-factor
residual; logs `preflight/_ru{250,500,750}.log`). All three end **2026-09-03**.

| `--days` | window | trading days | units @0.65 | within-group resid. corr | ARI (1st vs 2nd half) |
|---:|---|---:|---:|---:|---:|
| 250 | 2025-08-18 → 2026-09-03 | **249** | **12** | +0.8511 | 0.3188 |
| 500 | 2024-07-22 → 2026-09-03 | 499 | **11** | +0.6145 | 0.2328 |
| 750 | 2023-06-30 → 2026-09-03 | 749 | **10** | +0.5178 | 0.7937 |

- 250d membership: `U0 {MPC, PSX}` then **ten singletons**. 500d additionally merges **ANET+ETN**;
  750d merges **ANET+ETN** *and* **AVGO+NVDA**. ⇒ **Whether the four AI names are one bet or four
  still flips with the window.** The 500/750 runs raise the tool's own label warning (ANET+ETN carry
  two book theme labels inside one measured unit, so `MAX_THEME_PCT` counts them as two).
- Threshold sensitivity: at dist **0.40–0.60 all three windows converge on 12 units**; they diverge
  only at the chosen **0.65** — the same C5 signature as the last three runs.
- ARI moves **opposite** to fit in the 250d and 500d runs (the S5 trap); the 750d run is the one
  window where both are decent (ARI 0.7937 at fit +0.5178), a **change from 09-02** (0.3810) that is
  recorded, not leaned on.
- 250d raises the tool's short-sample flag (249 < 250). All three carry calendar-intersection
  warnings (KRW/USD mixing from the 2 KR holdings; ≥2 gaps >4 days).
- 🚫 **Today's revocations**: **no single-number concentration/diversification claim.** Any
  concentration statement must carry the `--days` used **on the same line**.

### G5 — Does the universe cover the book 🔴 FAIL (freshness leg)
- **Cover leg ✅**: `data/us_universe/us_top300.csv` **300 rows**; all 11 US holdings
  (ANET·AVGO·ETN·HPE·MET·MPC·NDAQ·NUE·NVDA·PSX·RTX) present. **Missing 0.**
- **Freshness leg ❌**: mtime **2026-07-15** ⇒ **51 days** (bar ≤8; the sweep prints its own warning).
  `us_all_v2_candidate.csv` (2026-08-10) sits beside it but is **a candidate, not the wired source** —
  not switching today (file replacement is a human-approval item).
- 🚫 **Today's revocations**: **do not cite market-cap rank or cap-weighting (`wflow`) as "current
  size"** — it is a 51-day-old weighting. This compounds G3 twice over: Consumer Discretionary's sign
  rests on AMZN's 40.2% weight and Communication Services' on Alphabet's 76.6%, and **both weights
  are seven weeks stale**.
- ⚠ The 2 KR names in the book (`028050`, `316140`) are outside the US universe by construction and
  are covered by the KR desk — not a US coverage miss.

### G6 — Instrumentation accrual rate 🔴 FAIL
`snapshot_estimates.py --status`: **25 files / 45 calendar days** (2026-07-22 → 2026-09-04) ⇒
**0.56/day**. 15 more needed for the 40-day target ⇒ ideal 15 days vs **measured ~27** = **1.8×**
(threshold 1.5×). Gap median **1**, max **6**. Today's snapshot stored (120 names).
- 🚫 **Today's revocations**: **do not report `kelly_size --ic` as an evidenced size.** If used, write
  **"mechanical 1/4"** explicitly.
- ⚠ Not recoverable retroactively — a day not accrued is gone (valid sample = number of **dates**, S1).

### G7 — Tool liveness 🟡 PASS with 2 named exceptions
`--help` exit codes: **42 of 44 are 0** — the same two exceptions as the last three runs.

| Group | exit 0 |
|---|---|
| `module_KIS`·`module_news_data`·`module_flow`·`module_watchlist`·`module_paper_book`·`module_valuation`·`module_business`·`module_business_us`·`module_disclosure`·`module_disclosure_us`·`module_fundamentals_us`·`module_industry_map`·`module_report_tags`·`module_inflection`·`module_macro_us`·`module_evidence`·`module_epistemics`·`module_math_check` | ✅ 18/18 |
| `sector_flow`·`us_live_shortlist`·`us_setup_screener`·`us_flow`·`flow_read`·`risk_units`·`snapshot_estimates`·`exposure_rule`·`missed_ledger`·`kelly_size`·`catalyst_calendar`·`report_lint`·`reject_ledger`·`drift_watch`·`cycle_exposure`·`action_bracket`·`company_score`·`axis_inflection`·`axis_window_flow`·`ic_ledger`·`measure_ic`·`handoff_compact`·`handoff_id_audit`·`leak_scan` | ✅ 24/24 |
| `python -m module_chart --help` | 🟡 **1** — prints a usage stub, not argparse (it is `module_text_chart`, positional ticker) |
| `scripts/margin_history.py --help` | 🔴 **1** — argparse `ValueError: unsupported format character`; KR-only tool, unused by this run |

★ **The chart tool was re-probed live rather than judged on `--help`:** `python -m module_chart
NVDA` · `ANET` · `SPY` → **0 / 0 / 0**, 3/3 render.
- ✅ **Live authority**: **US chart shape/pattern may be cited**, on data ending **09-03**.
  ⚠ Any chart window spanning 08-28 is now clean for 299 of 301 names (G0) — the caveat that stood
  for the last four runs is **lifted**.
- 🚫 `scripts/margin_history.py` output may not be cited (unused here regardless).

---

## 🧾 Everything this run **may not claim** — collected

1. **The `delta` field inside `SECTOR_FLOW_US.json`, at name or sector level** — it subtracts a holed
   09-02 baseline from a healed 09-03 snapshot; measured error mean 0.1078 / max 0.5570 / 19 sign
   flips, and up to 0.177 per sector (G2). Cite the clean Δ from `preflight/_cleanbase.json` instead.
2. **News velocity / theme freshness / "it is quiet"** *when sourced from the sweep* (G1) — 248 of
   298 names were never counted, and the coverage is a positional cutoff at exactly 50, not a
   distribution.
3. **`wflow` promotion/demotion of Consumer Discretionary** (AMZN 40.2% owns the sign) · **any
   `wflow` claim about Communication Services** (Alphabet is 76.6% under two tickers and the guard
   prints False) (G3).
4. **Anything about Friday 2026-09-04's tape** — NYSE had not opened during this preflight and the
   vendor's partial 09-04 row is an incomplete bar · **`EA` and `APH`** — unscored (G0).
5. **Concentration/diversification as a single number** (G4) · **market-cap-weighted "current size"**
   (G5, 51 days stale) · **`kelly_size --ic` as evidenced** (G6) · **`margin_history` output** (G7).
6. **`SECTOR_FLOW_US_REPAIRED.json`** — it does not exist today, by design (G0a). A downstream stage
   that reaches for it must use the primary file.

## ✅ What is **live** today
- ★ **The primary `SECTOR_FLOW_US.json`, OBV axis included** — first run since 2026-08-28 where the
  hole is not in the window. 298 scored, 3-axis `nonews`, asof **2026-09-03**.
- ★ **The 09-03 session and every session back through 08-18, including 08-28**, officially and
  without a proxy label — 0/16 on the direct book probe, ≤2/301 in the sweep cache.
- ★ **A clean one-session Δ (09-02 → 09-03), citable as a magnitude**, both sides rescored on healed
  data (`preflight/_cleanbase.json`).
- **Direct news queries** at every entry point: **6/6 pre-sweep · 4/4 post-sweep · 40/40 in an
  80-query zero-spacing burst · 8/8 on well-formed names in the fixed-set falsification.** Keep any
  single fan-out under ~40 names; the ≥9s spacing rule is retired.
- **`module_chart`** — live 3/3, and its 08-28 caveat is lifted.
- **`module_macro_us` (FRED)** · **`module_disclosure_us` / `module_business_us` /
  `module_fundamentals_us`** · **`us_flow` (FINRA short-vol / CFTC COT)** — `--help` clean.
- **Book positions and cost basis**, and the price column (09-03 marks are real).

---
> Output: `preflight/PREFLIGHT.md` · logs `preflight/_ru{250,500,750}.log` · `_barprobe.log` ·
> `_news_pre.log` · `_news_post.log` · `_falsify.log`/`.json` · `_cleanbase.log`/`.json` ·
> `../_sweep.log` · primary `../SECTOR_FLOW_US.json`. **No `_REPAIRED.json` this run — the hole
> healed.**
