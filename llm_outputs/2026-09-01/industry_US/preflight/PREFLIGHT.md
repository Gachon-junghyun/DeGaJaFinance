# PREFLIGHT — 2026-09-01 (Tue) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is not a report, it is a permissions table** — a FAIL is not "be careful", it is
> **"what this run may not cite today"**.
> Execution KST 2026-09-01 **22:09 clock/weekday · 22:10 bar probe (daily endpoint, 16 tickers)
> · 22:11 news probe pre-sweep (6/6) · 22:12 tool `--help` x37 + chart live x3 · 22:13 universe/book/accrual
> · 22:13–22:16 risk units x3 windows · 22:11–22:18 sweep (`--json --refresh`) · 22:18 OBV-hole
> quantification · 22:19–22:27 5m-proxy repair + rescore · 22:28 OBV repair-error validation
> · 22:29 news probe post-sweep (4/4) · 22:30 falsification probe (10/10).**
> **Tuesday 09:09 ET — NYSE has NOT opened yet** (opens 09:30 ET). Last completed US session
> **Mon 2026-08-31**. ⇒ Every price statement below is about **Monday 08-31 or earlier**.

★ **Three-line summary**
> ① ✅ **The ghost bar healed at the head of the series.** The 2026-08-31 daily row is complete —
>    **1 of 301** Close NaN across the sweep cache (that 1 is **EA**, delisted-type response, not the
>    ghost). Four days ago this was 301/301. Two consequences follow immediately: the sweep
>    **scored 299 of 299 again** (`dropped_missing_axis=0`, after two consecutive zero-score runs),
>    and `module_chart` **renders 3/3** (it was 0/3 yesterday, downstream of the NaN).
> ② 🔴 **But 08-28 did not heal — it is a permanent partial hole, and it is not cosmetic.**
>    **259 of 301** names still carry a NaN Close/Volume at 08-28 (T+4). Measured on the **42** names
>    the vendor *did* backfill: leaving that hole in place shifts `obv_norm` by **0.065 mean / 0.404 max**
>    and **flips the accumulation/distribution label on 12 of 42 (29%)** and the OBV **sign on 7 of 42 (17%)**.
>    The mechanism is exact: `np.sign(close.diff())` is NaN on both 08-28 *and* 08-31 when the prior
>    close is missing, so **the two most recent sessions contribute zero** to a 20-session OBV window.
>    ⇒ The primary `SECTOR_FLOW_US.json` OBV axis is corrupted for 259 of 299 scored names.
> ③ ★ **Yesterday's 5m proxy is now independently confirmed by official prints — and one of its
>    warrants is now shown to have been too generous.** Seven names the vendor backfilled overnight let
>    the 08-28 proxy tape be checked against the real settle: **all 7 within 0.04pp** (NVDA proxy −4.58%
>    vs official **−4.57%**; SPY −0.22% vs **−0.23%**; HPE −3.90% vs **−3.86%**). But re-validating on
>    42 official closes gives max error **0.0937%** (4 names over 0.05%), **looser than yesterday's
>    stated 0.0448% max**, and — not measured at all yesterday — the **5m *volume* sum is biased
>    −18.15% mean / −54.6% worst** because it misses off-exchange and closing-auction prints.
>    That volume bias was then measured through to the axis it feeds: it moves `obv_norm` by
>    **0.009 mean / 0.026 max with 0/42 label flips** — i.e. **~7x smaller than the error it removes.**
>    ⇒ The repair is the better instrument, **and it is now the only one whose error is bounded in
>    both legs.** `SECTOR_FLOW_US_REPAIRED.json` is today's citable flow object.

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | 🟡 **head HEALED · 08-28 permanently holed** · ✅ proxy-recovered | 08-31 Close NaN **1/301** (EA only) · 08-28 **259/301** at T+4 · direct 16-ticker probe 08-31 **0/16**, 08-28 **10/16**. Unpatched OBV distortion **0.065 mean / 0.404 max, 12/42 label flips**; after repair **0.009 / 0.026, 0/42** |
| **G1** | News-axis liveness | 🔴 **FAIL** (sweep axis) · ✅ **direct path LIVE** | `vel_coverage` **16.05%** (48/299, bar 80%) — up from 15.72%, still far below bar. Probe **6/6 pre-sweep · 4/4 post-sweep**, every count **above** yesterday. ★ Falsification **10/10**, incl. universe-bottom PCAR **1.29** · JCI **1.07** · AON **3.07** |
| **G2** | Scoring-scale continuity | ⚠ **PASS on scale · Δ UNDEFINED on the primary** | `n_axes=3` = yesterday's `3`, `mode=nonews`, `scored=299`. But primary Δ is **null on 299/299 names and 11/11 sectors** — the previous history key (08-28) holds **1 key**. Repaired run recovers Δ against the **08-27** snapshot (299/299 common, same mode) = **2 sessions**, not one |
| **G3** | Who owns the sector sign | ✅ **PASS** (list printed) · ⚠ instrument-dependent | **Repaired: 1 of 11 flips** — Cons. Disc./**AMZN** (40.2%), −0.282 → **+0.081**. **Primary: 2 of 11** — adds Financials/BRK-B. The two instruments disagree on Financials ⇒ that sign is not established either way |
| **G4** | Risk-unit stability | 🔴 **FAIL** | 250d **12 units** · 500d **10** · 750d **10**; membership differs. ARI **0.3188 / 0.2328 / 0.3810** vs within-group fit **+0.8509 / +0.5275 / +0.5174**. All three windows end **2026-08-31** |
| **G5** | Does the universe cover the book | 🔴 **FAIL** (freshness leg) | Cover ✅ **11/11** US holdings in `us_top300.csv` (300 rows), missing **0**. Freshness ❌ **48 days** (mtime 2026-07-15; bar ≤8) |
| **G6** | Instrumentation accrual rate | 🔴 **FAIL** | **22 files / 42 calendar days = 0.52/day** ⇒ ETA **~34 days** vs ideal 18 = **1.9x** (threshold 1.5x). Gap median 1, max 6 |
| **G7** | Tool liveness | 🟡 **PASS with 2 named exceptions** (was FAIL) | 35 of 37 `--help` exit 0. `module_chart --help` **exit=1** *but* **live render 3/3 exit 0** (NVDA·ANET·SPY) ⇒ **chart citation restored**. `scripts/margin_history.py` **exit=1** (KR-only, unused here) |

---

## Gate detail

### G0 — Bar completeness 🟡 head healed · 🔴 08-28 permanently holed · ✅ proxy-recovered ★today's principal finding

#### (a) The head of the series is clean again
Direct `yfinance` probe, `auto_adjust=False`, 16 US tickers (11 book holdings + SPY + 4 sector ETFs):

| Session | Close NaN |
|---|---:|
| 2026-08-24 … 08-27 | **0** / 16 each |
| **2026-08-28 (Fri)** | **10 / 16** ← was 16/16 yesterday |
| **2026-08-31 (Mon, last session)** | **0 / 16** |

Widened to the sweep's own fresh cache (`prices_2026-09-01.pkl`, 301 columns, downloaded today):
08-31 is **1/301** NaN — and that one name is **EA**, which the 5m endpoint also refuses
("possibly delisted"), i.e. a name-specific vendor problem, not the ghost.

★ **This is a change of state, not a repetition.** For three runs the desk logged a head-of-series
hole; today the head is complete and the two tools that were dead because of it — the sweep's scorer
and `module_chart` — came back on their own. **The correct update is not "the bug is back", it is
"the bug moved": it is now a *fixed* hole at 08-28 rather than a *rolling* hole at T-1.**

#### (b) 08-28 is a standing hole, and it is load-bearing
**259 of 301** names still have Close **and** Volume NaN at 08-28, four calendar days on. Only 42
were backfilled. This is not cosmetic, because of how the OBV axis is computed
(`module_flow/_price_flow.py:29–31`):

    obv = (np.sign(close.diff()).fillna(0) * vol).cumsum()
    obv_chg = obv.iloc[-1] - obv.iloc[-21]
    obv_norm = obv_chg / vol.tail(20).sum()

With 08-28's close missing, `close.diff()` is NaN at **08-28** *and* at **08-31** (its predecessor is
NaN). `.fillna(0)` then silently assigns **direction zero to the two most recent sessions** — 10% of
a 20-session window, and the 10% that matters most. `vol.tail(20).sum()` likewise sums 19 days into a
20-day denominator. **Nothing in the output says so.** `dropped_missing_axis=0`; every name reports a
number.

★ **Measured, not reasoned.** Taking the **42** names that *do* have an official 08-28 bar and
re-computing `obv_norm` with that bar blanked — i.e. simulating exactly what the other 259 suffer:

| | value |
|---|---:|
| mean abs Δ `obv_norm` | **0.0652** |
| median | 0.0310 |
| max | **0.4040** (PCG: −0.243 → +0.161) |
| `obv_state` (accumulation/neutral/distribution) label flips | **12 / 42 (29%)** |
| OBV **sign** flips | **7 / 42 (17%)** |
| implied mean `flow_score` shift (OBV axis = clip(obv/0.16)/3) | **≈ 0.136** |

Names whose accumulation/distribution reading is created by the hole rather than by the tape include
**PCG · PYPL · MRVL · HPE · SNDK · DELL · SPY**.

#### (c) The repair, and the correction it forces to yesterday's warrant
The 5m endpoint returns the full 08-28 session (**78/78 bars, median = min = max = 78**) for
**300 of 301** names (EA excepted). Patch applied to a **working copy only** — `history.json` was not
written (preflight rule 1). Validation against the **42 official** 08-28 bars:

| leg | result |
|---|---|
| **close** | mean abs err **0.0203%** · max **0.0937%** · names >0.05%: **4 / 42** |
| **volume** | mean **−18.15%** · median **−14.52%** · range **−4.74% … −54.58%** |

★ **Two honest corrections to yesterday's entry.**
1. Yesterday claimed close-proxy **max 0.0448%, 0 names over 0.05%**. Checked today against *official
   prints* rather than a prior-session backtest, the true max is **0.0937%** with **4** names over.
   The proxy is still good; **the stated bound was tighter than the instrument earns.**
2. Yesterday validated the **close** leg only, then used the proxy to rebuild an axis that also eats
   **volume**. The volume leg is biased **−18%** — 5m bars miss off-exchange and closing-auction
   prints. That was an unmeasured assumption carried into a cited number.

So the volume bias was measured **through to the axis it feeds**, on the same 42 names — repaired
`obv_norm` vs the official bar:

| | unpatched hole | **5m repair** |
|---|---:|---:|
| mean abs Δ `obv_norm` | 0.0652 | **0.0090** |
| max | 0.4040 | **0.0262** |
| `obv_state` label flips | **12 / 42** | **0 / 42** |
| sign flips | **7 / 42** | **0 / 42** |

⇒ The repair removes **~7x** more error than it injects, and injects **zero** label flips. Worst
residuals: MCHP +0.026 · GOOG −0.025 · GOOGL −0.021.

#### (d) Yesterday's proxy tape, now checkable against the settle
Seven of the names in yesterday's published 08-28 proxy tape were backfilled overnight:

| Ticker | proxy (published 08-31) | **official 08-28** | err |
|---|---:|---:|---:|
| NVDA | −4.58% | **−4.57%** | +0.01pp |
| HPE | −3.90% | **−3.86%** | +0.04pp |
| AVGO | −0.77% | **−0.74%** | +0.03pp |
| QQQ | −0.65% | **−0.65%** | +0.00pp |
| SPY | −0.22% | **−0.23%** | −0.01pp |
| XLE | +0.59% | **+0.63%** | +0.04pp |
| XLF | +0.36% | **+0.38%** | +0.02pp |

★ **7/7 within 0.04pp against the real settle.** Yesterday's 08-28 statements stand.

#### (e) The 08-31 session (official, complete — no proxy label needed)

| Risk-off | | Risk-on | |
|---|---:|---|---:|
| XLU | **−2.20%** | PSX | **+2.82%** |
| XLI · RTX | **−2.05%** | MPC | **+2.69%** |
| XLK | **−1.12%** | XLE | **+2.04%** |
| XLB | **−1.01%** | NVDA | **+1.48%** |
| XLRE | **−0.83%** | XLY | **+0.61%** |
| XLF | **−0.67%** | AVGO | **+0.42%** |
| SPY | **−0.30%** | QQQ | **+0.05%** |

*(ANET −2.69% · ETN −3.40% · NUE −1.08% · MET −1.12% span 08-27→08-31, two sessions, because their
08-28 bar is in the hole — labeled `vs27` in the probe log.)*

- ✅ **Live authority**: **the 08-31 session may be cited plainly** from the daily endpoint,
  `module_paper_book status`, and `pulse` — re-verified: `status` prints ANET **195.69**, which *is*
  the 08-31 close (yesterday it printed a stale 08-27 value under a current label). **That revocation
  is lifted.**
- ✅ **08-28 may be cited from `SECTOR_FLOW_US_REPAIRED.json` or the 5m tape**, with
  **"5m-proxy (close err ≤0.094%, volume −18%)"** on the same line.
- 🚫 **Today's revocations**:
  1. **Do not cite `obv_norm` / `obv_state` / any OBV-derived flow score from the primary
     `SECTOR_FLOW_US.json`** — 259 of 299 scored names have the two most recent sessions zeroed out
     of the OBV window (§b). Use the repaired file.
  2. **Do not cite an 08-28 close from the daily endpoint for any name outside the 42 backfilled** —
     it is NaN, and any tool that quietly skips it returns an 08-27 number under an 08-28 label.
  3. **Do not cite raw 08-28 volume, or any volume-magnitude claim ("volume surge", "heavy tape") for
     08-28**, from either instrument — official is missing for 259, and the proxy is **−18% biased**.
  4. **Do not cite anything about Tuesday 09-01's tape** — the market had not opened at run time.

#### (f) The sweep recovered

| Run | asof | vel_cov | scored | n_axes |
|---|---|---:|---:|---:|
| 08-27 | 08-27 | 16.72% | 299 | 3 |
| 08-28 | 08-28 | 16.72% | 299 | 3 |
| 08-29 | 08-27 | 0.0% | 299 | 3 |
| 08-30 | 08-28 | 17.06% | **0** | 3 |
| 08-31 | 08-28 | 15.72% | **0** | 3 |
| **09-01** | **08-31** | **16.05%** | **299** | 3 |

### G1 — News-axis liveness 🔴 FAIL on the sweep axis · ✅ direct path LIVE

| Window | KST | `fts search --days 7 --count --scope foreign` |
|---|---|---|
| **pre-sweep** | 22:11 | **6/6** — Federal Reserve **1485** · Nvidia **5318** · tariff **2025** · jobs report **110** · oil prices **1294** · data center **2691** |
| **post-sweep** | 22:29 | **4/4** — identical (1485 / 5318 / 2025 / 110) |

**All six counts are above yesterday's** (1365 / 5292 / 1993 / 82 / 1143 / 2551) — the pool grew on
every query, `jobs report` by 34%. Yet the sweep measured **16.05%**.

★ **The decisive probe.** Direct `news_velocity` on ten names, weighted toward the universe's
flow-ranking floor:

| Ticker | velocity | recent / base (7d / 30d) |
|---|---:|---|
| **PCAR** (universe bottom) | **1.29** | 6 / 20 |
| **JCI** (bottom-2) | **1.07** | 6 / 24 |
| **AON** | **3.07** | 68 / 95 |
| **UAL** | **1.47** | 65 / 189 |
| SLB | **2.42** | 74 / 131 |
| CRM | **2.21** | 500 / 968 |
| WDC | 0.66 | 88 / 569 |
| APP | 0.62 | 48 / 334 |
| SYY | 0.49 | 6 / 53 |
| AMAT | 0.43 | 54 / 544 |

⇒ **10/10 alive.** The ~84% the sweep could not measure are **not quiet** — the sweep's own 300-query
burst rate-limits itself, and `news_velocity` cannot distinguish "server refused" from "no articles"
(`module_flow/_news_velocity.py:126–136`). **AON is the sharpest case**: the sweep ranks it near the
universe floor on price axes while its news velocity is **3.07** — accelerating, not silent.

- 🚫 **Today's revocations**: **no theme-freshness / news-velocity citation sourced from the sweep**;
  **no "sector X is quiet" verdict from sweep coverage** — 251 of 299 were never counted. The 78 red
  names (84 in the repaired run) may **not** be described as having "no news flow".
- ✅ **Live authority**: **direct queries** (`fts search` · `brief` · `thread` · `chain-hop` · `burst`
  · `flow_read.news_velocity`). ★ Fire **≤11 consecutively, ~90s pause if refused**, and write
  **"direct query, outside the sweep window"** on the same line as the number.
  **The sweep is not run again in this run.**

### G2 — Scoring-scale continuity ⚠ PASS on scale · Δ UNDEFINED on the primary
Scale: `n_axes=3`, `vel_axis=false`, `mode=nonews`, `scored=299` — identical to the previous
same-mode snapshot ⇒ **no mixed-scale subtraction risk.** PASS by the gate's wording.

But the operand is missing. `history.json`'s key immediately before 08-31 is **08-28, which holds
1 key** (yesterday's zero-score run). The engine therefore returned **`delta: null` on 299/299 names
and 11/11 sectors** in the primary file. The repaired run reaches past it to the **08-27** snapshot
(300 keys, `nonews`), giving **299/299 common names**.

- ✅ **Live authority**: **Δflow may be cited today**, on condition it is labeled
  **"repaired sweep (5m-proxy), 08-27 → 08-31, two sessions, 3-axis nonews"** on the same line.
  Measured sector Δ: **Energy +0.353** · Real Estate +0.168 · Materials +0.120 · Cons. Staples +0.107
  · Health Care +0.095 · Utilities +0.076 · IT +0.040 · Financials −0.047 · Cons. Disc. −0.146 ·
  **Industrials −0.225** · **Comm. Services −0.287**.
  Name movers: **up** CTVA +0.98 · AAPL +0.83 · ABBV +0.64 · AZO +0.63 · ADM +0.58 · XOM +0.47 ·
  WMB +0.46 · OKE +0.46 · APD +0.46; **down** COHR −0.81 · VRT −0.69 · PYPL −0.68 · ETN −0.67 ·
  TT −0.65 · HCA −0.54 · GLW −0.54 · PCG −0.53.
- 🚫 **Revoked**: **no Δ from the primary `SECTOR_FLOW_US.json`** (null throughout). **No Δ described
  as a one-day move** — the baseline is two sessions back. **No Δ spanning the 08-28/08-29/08-30
  snapshots** — they are 0-name or 0-score and cannot be an operand.
- ⚠ The repair did **not** write `history.json`; the stored 08-31 entry is the **primary**
  (corrupted-OBV) one. Tomorrow's Δ will therefore be against a baseline whose OBV axis is holed.
  **Logged, not fixed — file/state repair is a human item.**

### G3 — Who owns the sector sign ✅ PASS (list printed) · ⚠ instrument-dependent
**Repaired file (citable): 1 of 11 sectors flips sign when its top-1 name is removed.**

| Sector | wflow | ex-top1 | top-1 | top-1 weight | n |
|---|---:|---:|---|---:|---:|
| **Consumer Discretionary** | −0.282 | **+0.081** | AMZN | **40.2%** | 28 |

Non-flippers, in full: Energy (XOM 30.5%, +0.302→+0.471) · Materials (LIN 24.7%, +0.148→+0.115) ·
Health Care (LLY 19.4%, +0.069→+0.115) · IT (NVDA 19.4%, +0.048→+0.001) · Financials (BRK-B 13.9%,
−0.191→−0.142) · Cons. Staples (WMT 28.9%, −0.237→−0.115) · Real Estate (WELL 16.9%, −0.248→−0.334) ·
Industrials (CAT 8.7%, −0.413→−0.380) · Utilities (NEE 17.7%, −0.448→−0.489) · Comm. Services
(GOOGL 38.3%, −0.547→−0.404).

⚠ **The primary file lists 2 flippers** — it adds **Financials/BRK-B** (−0.040 → +0.004, a sign flip
on a margin of 0.004). The repaired file puts Financials at **−0.191 → −0.142**, no flip. **The two
instruments disagree about Financials**, so its sign is not established by either.

★ Note also **Comm. Services**: `wflow` **−0.547** but `eqflow` **+0.054** — the whole negative sign
is GOOGL's 38.3% weight, without technically flipping on removal. Cap-weight and equal-weight tell
opposite stories there.

- 🚫 **Today's revocations**: **no promotion or demotion of Consumer Discretionary on `wflow`**
  (ROTATION §2) — one company owns the sign. **No `wflow`-based claim about Financials at all** —
  the two instruments disagree. **No "Comm. Services is the worst sector" claim from `wflow` alone**
  — equal-weight is positive.
  Substitutes available today: `eqflow`, `breadth`, the official 08-31 tape, FRED transmission,
  short/COT positioning, direct news — each named **on the same line** as the conclusion it supports.

### G4 — Risk-unit stability 🔴 FAIL
All three windows actually run (`risk_units.py --book --days {250,500,750}`, bench SPY, 1-factor
residual; logs `preflight/_ru{250,500,750}.log`). ✅ All three now end **2026-08-31** — the real last
session, not a truncation artifact.

| `--days` | trading days | units @0.65 | within-group resid. corr | ARI (1st vs 2nd half) |
|---:|---:|---:|---:|---:|
| 250 | 249 | **12** | +0.8509 | 0.3188 |
| 500 | 499 | **10** | +0.5275 | 0.2328 |
| 750 | 749 | **10** | +0.5174 | 0.3810 |

- 250d membership: `U0 {MPC, PSX}` and then **ten singletons** — ANET, AVGO, ETN, HPE, MET, NDAQ,
  NUE, NVDA, RTX, plus the 2 KR names each alone. The 500/750d windows instead merge **ANET+ETN**
  and **AVGO+NVDA**. ⇒ **Whether the four AI names are one bet or four is still unmeasured; the
  answer flips with the window.** The 500/750 runs raise the tool's own label warning (ANET+ETN carry
  *two* book theme labels inside one measured unit, so `MAX_THEME_PCT` counts them as two).
- Threshold sensitivity: at dist **0.40–0.60 all three windows converge on 12 units**; they diverge
  only at the chosen **0.65** ⇒ the unit count tracks an arbitrary threshold as much as the window.
- ARI (0.23–0.38) moves **opposite** to fit (+0.52–0.85) in all three — the tool's own warning not to
  trust membership. The 250d run raises its S5 short-sample flag (249 < 250) and is also the window
  with the *highest* fit, which is exactly the S5 trap.
- 🚫 **Today's revocations**: **no single-number concentration/diversification claim.** Any
  concentration statement must carry the `--days` used **on the same line**.

### G5 — Does the universe cover the book 🔴 FAIL (freshness leg)
- **Cover leg ✅**: `data/us_universe/us_top300.csv` **300 rows**; all 11 US holdings
  (ANET·AVGO·ETN·HPE·MET·MPC·NDAQ·NUE·NVDA·PSX·RTX) present. **Missing 0.**
- **Freshness leg ❌**: mtime **2026-07-15** ⇒ **48 days** (bar ≤8; the sweep prints its own warning).
  `us_all_v2_candidate.csv` (2026-08-10) sits beside it but is **a candidate, not the wired source** —
  not switching today (file replacement is a human-approval item).
- 🚫 **Today's revocations**: **do not cite market-cap rank or cap-weighting (`wflow`) as "current
  size"** — it is a 48-day-old weighting. This compounds G3: Consumer Discretionary's sign rests on
  AMZN's 40.2% weight, and that weight is itself seven weeks stale.
- ⚠ The 2 KR names in the book (`028050`, `316140`) are outside the US universe by construction and
  are covered by the KR desk — not a US coverage miss.

### G6 — Instrumentation accrual rate 🔴 FAIL
`snapshot_estimates.py --status`: **22 files / 42 calendar days** (2026-07-22 → 2026-09-01) ⇒
**0.52/day**. 18 more needed for the 40-day target ⇒ ideal 18 days vs **measured ~34** = **1.9x**
(threshold 1.5x). Gap median **1**, max **6**. Today's snapshot stored (120 names).
- 🚫 **Today's revocations**: **do not report `kelly_size --ic` as an evidenced size.** If used, write
  **"mechanical 1/4"** explicitly.
- ⚠ Not recoverable retroactively — a day not accrued is gone (valid sample = number of **dates**, S1).

### G7 — Tool liveness 🟡 PASS with 2 named exceptions (was FAIL)
`--help` exit codes: **35 of 37 are 0** — the same two exceptions as yesterday.

| Group | exit 0 |
|---|---|
| `module_KIS`·`module_news_data`·`module_flow`·`module_watchlist`·`module_paper_book`·`module_valuation`·`module_business`·`module_business_us`·`module_disclosure`·`module_disclosure_us`·`module_fundamentals_us`·`module_industry_map`·`module_report_tags`·`module_inflection`·`module_macro_us`·`module_evidence` | ✅ 16/16 |
| `sector_flow`·`us_live_shortlist`·`us_setup_screener`·`us_flow`·`flow_read`·`risk_units`·`snapshot_estimates`·`exposure_rule`·`missed_ledger`·`kelly_size`·`catalyst_calendar`·`report_lint`·`reject_ledger`·`drift_watch`·`cycle_exposure`·`action_bracket`·`company_score`·`axis_inflection`·`axis_window_flow` | ✅ 19/19 |
| `python -m module_chart --help` | 🟡 **1** — prints a usage stub, not argparse (it is `module_text_chart`, positional ticker) |
| `scripts/margin_history.py --help` | 🔴 **1** — argparse `ValueError: unsupported format character`; KR-only tool, unused by this run |

★ **The chart tool was re-probed live rather than judged on `--help`, and it now works:**

| Invocation | exit |
|---|---:|
| `python -m module_chart NVDA` · `ANET` · `SPY` | **0 / 0 / 0** (3/3 render, file written) |

Yesterday all three exited 1 on `cannot convert float NaN to integer` — that was **downstream of G0's
head-of-series NaN**, and it cleared when the 08-31 bar landed. The `--help` stub is a CLI-shape
quirk, not a dead tool.
- ✅ **Live authority restored**: **US chart shape/pattern may be cited again today**, on data ending
  **08-31**. ⚠ Any chart window that spans 08-28 inherits the hole for the 259 names — say so if the
  read depends on that bar.
- 🚫 `scripts/margin_history.py` output may not be cited (unused here regardless).

---

## 🧾 Everything this run **may not claim** — collected

1. **OBV / accumulation-distribution / flow score taken from the primary `SECTOR_FLOW_US.json`** —
   259 of 299 scored names have their two most recent sessions zeroed out of the OBV window; measured
   label-flip rate **29%** (G0b). Use `SECTOR_FLOW_US_REPAIRED.json`, labeled.
2. **Any Δflow from the primary file** (null on 299/299) · **any Δ called a one-day move** — the only
   valid baseline is **08-27**, two sessions back (G2).
3. **`wflow` promotion/demotion of Consumer Discretionary** (AMZN owns the sign, 40.2% weight) ·
   **any `wflow` claim about Financials** (the two instruments disagree on its sign) ·
   **"Comm. Services is worst" from `wflow` alone** (eqflow is +0.054) (G3).
4. **News velocity / theme freshness / "it is quiet"** *when sourced from the sweep* (G1) — 251 of 299
   names were never counted, and 10/10 re-probed answered normally, including the bottom two.
5. **08-28 closes from the daily endpoint for the 259 unbackfilled names** · **any 08-28 volume or
   volume-magnitude claim from either instrument** (official missing; proxy −18% biased) ·
   **anything about Tuesday 09-01's tape** — the market had not opened at run time (G0).
6. **Concentration/diversification as a single number** (G4) · **market-cap-weighted "current size"**
   (G5, 48 days stale) · **`kelly_size --ic` as evidenced** (G6) · **`margin_history` output** (G7).

## ✅ What is **live** today
- ★ **The 08-31 session, officially and without a proxy label** — 1/301 NaN (EA only). `status` and
  `pulse` are current again; **yesterday's staleness revocation is lifted.**
- ★ **`SECTOR_FLOW_US_REPAIRED.json`** (299 scored, 3-axis nonews, asof 08-31, 258 names patched at
  08-28), **including Δ vs the 08-27 snapshot** — always labeled "repaired, 5m-proxy, two-session Δ".
  Its residual error is bounded on both legs: close ≤0.094%, OBV 0.009 mean / 0.026 max,
  **0/42 label flips**.
- ★ **The 08-28 proxy tape published yesterday** — now confirmed against **7 official backfills, all
  within 0.04pp**.
- **Direct news queries** at every entry point: **6/6 pre-sweep · 4/4 post-sweep · 10/10 falsification**,
  every headline count above yesterday. ★ ≤11 consecutive, ~90s pause if refused.
- **`module_chart`** — live 3/3 today (restored).
- **`module_macro_us` (FRED)** · **`module_disclosure_us` / `module_business_us` /
  `module_fundamentals_us`** · **`us_flow` (FINRA short-vol / CFTC COT)** — `--help` clean, none of
  them touch the 08-28 hole.
- **Book positions and cost basis**, and now the price column too (08-31 marks are real).

---
> Output: `preflight/PREFLIGHT.md` · logs `preflight/_ru{250,500,750}.log` · `../_sweep.log` ·
> `../_repair.log` · primary `../SECTOR_FLOW_US.json` · repaired `../SECTOR_FLOW_US_REPAIRED.json`
