# PREFLIGHT — 2026-09-02 (Wed) · industry_US (`--market us`)

> Instrument check. No market call · no name call · no sizing (P4).
> **This is not a report, it is a permissions table** — a FAIL is not "be careful", it is
> **"what this run may not cite today"**.
> Execution KST 2026-09-02 **22:09 clock/weekday · 22:10 bar probe (daily endpoint, 16 tickers)
> · 22:10 news probe pre-sweep (6/6) · 22:10 tool `--help` ×37 + chart live ×3 · 22:10–22:11
> universe/book/accrual · 22:10–22:11 risk units ×3 windows · 22:11–22:22 sweep (`--json --refresh`)
> · 22:22 hole quantification · 22:23–22:30 5m-proxy repair + rescore · 22:31 news probe
> post-sweep (4/4) · 22:31–22:36 falsification probe (two cadences).**
> **Wednesday 09:09 ET — NYSE has NOT opened yet** (opens 09:30 ET). Last completed US session
> **Tue 2026-09-01**. ⇒ Every price statement below is about **Tuesday 09-01 or earlier**.

★ **Three-line summary**
> ① ✅ **The head of the series stayed healed for a second run.** The 2026-09-01 daily row is
>    complete — **2 of 301** Close NaN across the sweep cache (**EA**, delisted-type response, and
>    **APH**), and the direct 16-ticker probe is **0/16**. The sweep scored **298 of 298**
>    (`dropped_missing_axis=0`) and `module_chart` renders **3/3**.
> ② 🔴 **The 08-28 hole did NOT move in 24 hours — it is frozen, not lagging.** **259 of 301**
>    names carried a NaN Close/Volume at 08-28 yesterday (T+4) and **the identical 259** carry it
>    today (T+5); the backfilled set is still **42**. ★ **This is the state change worth recording:**
>    yesterday the desk could still call it "a hole that may fill". A vendor that backfilled 42 names
>    in one night and then **zero** in the next 24 hours is not lagging — **08-28 is a permanent
>    partial session for this instrument**, and every 20-session window that spans it will carry the
>    defect until it rolls out around 2026-09-25. Measured on the 42 names that *do* have the
>    official bar: leaving the hole in place shifts `obv_norm` by **0.0625 mean / 0.3702 max** and
>    flips the accumulation/distribution label on **7 of 42 (17%)** and the OBV sign on **5 of 42
>    (12%)**.
> ③ ★ **The news axis's death was falsified directly this run, on the same names, by changing only
>    the request cadence.** Ten names probed at **1.5s spacing** returned `velocity=None` on **7 of
>    10**; the **same seven**, re-probed at **9s spacing** minutes later, all returned real numbers
>    (`TER` 0.34 · `APP` 0.63 · `CRM` 2.07 · `WMB` 1.86 · `MDT` 1.87 · `NEM` 0.81 · `AVGO` 1.35).
>    ⇒ The sweep's **17.11%** coverage is **a rate-limit artifact of its own 300-query burst**, not
>    an absence of articles — and this is the first run to demonstrate it by **flipping one variable
>    on a fixed name set** rather than by probing a different sample.

---

## Gate summary

| # | Gate | Verdict | Numbers |
|---|---|---|---|
| **G0** | Bar completeness (US extension) | 🟡 **head clean 2nd run · 08-28 FROZEN** · ✅ proxy-recovered | 09-01 Close NaN **2/301** (EA, APH) · 08-28 **259/301** at T+5, **identical set to T+4** · direct 16-ticker probe 09-01 **0/16**, 08-28 **10/16**. Unpatched OBV distortion **0.0625 mean / 0.3702 max, 7/42 label flips**; after repair **0.0087 / 0.0272, 1/42** |
| **G1** | News-axis liveness | 🔴 **FAIL** (sweep axis) · ✅ **direct path LIVE** | `vel_coverage` **17.11%** (51/298, bar 80%) — up from 16.05%, still far below bar. Probe **6/6 pre-sweep · 4/4 post-sweep**. ★ Falsification **10/10 at 9s cadence**, of which **7 had returned `None` at 1.5s cadence on the same names minutes earlier** |
| **G2** | Scoring-scale continuity | ✅ **PASS on scale · Δ is a TRUE one-session Δ** · ⚠ baseline is holed | `n_axes=3`, `mode=nonews`, `scored=298` (was 299 — `APH` joined `EA`). `prev_snapshot` resolves to **2026-08-31**, one session back, same mode, **299 names** ⇒ Δ defined on 298. ⚠ That 08-31 baseline is **yesterday's PRIMARY (holed-OBV) snapshot** — the repair does not write history |
| **G3** | Who owns the sector sign | ✅ **PASS** (list printed) · ⚠ the guard misses the largest case | **Repaired: 1 of 11 flips** — Cons. Disc./**AMZN** (40.2%), −0.286 → **+0.033**. **Primary: 2 of 11** — adds Cons. Staples/**WMT** (28.9%). ★ Alphabet is **76.6%** of Comm. Services under **two** tickers, `top1_flips_sign` prints **False**, and ex-both-classes `wflow` goes **−0.506 → +0.257** (swing **0.763**) |
| **G4** | Risk-unit stability | 🔴 **FAIL** | 250d **12 units** · 500d **10** · 750d **10**; membership differs. ARI **0.3874 / 0.2328 / 0.3810** vs within-group fit **+0.8512 / +0.5278 / +0.5179**. All three windows end **2026-09-01** |
| **G5** | Does the universe cover the book | 🔴 **FAIL** (freshness leg) | Cover ✅ **11/11** US holdings in `us_top300.csv` (300 rows), missing **0**. Freshness ❌ **49 days** (mtime 2026-07-15; bar ≤8) |
| **G6** | Instrumentation accrual rate | 🔴 **FAIL** | **23 files / 43 calendar days = 0.53/day** ⇒ ETA **~32 days** vs ideal 17 = **1.9×** (threshold 1.5×). Gap median 1, max 6 |
| **G7** | Tool liveness | 🟡 **PASS with 2 named exceptions** | 35 of 37 `--help` exit 0. `module_chart --help` **exit=1** *but* **live render 3/3 exit 0** (NVDA·ANET·SPY) ⇒ **chart citation stands**. `scripts/margin_history.py` **exit=1** (KR-only, unused here) |

---

## Gate detail

### G0 — Bar completeness 🟡 head clean · 🔴 08-28 frozen · ✅ proxy-recovered ★today's principal finding

#### (a) The head of the series held
Direct `yfinance` probe, `auto_adjust=False`, 16 US tickers (11 book holdings + SPY + 4 sector ETFs):

| Session | Close NaN |
|---|---:|
| 2026-08-21 … 08-27 | **0** / 16 each |
| **2026-08-28 (Fri)** | **10 / 16** |
| **2026-08-31 (Mon)** | **0 / 16** |
| **2026-09-01 (Tue, last session)** | **0 / 16** |

In the sweep's own fresh cache (`prices_2026-09-02.pkl`, 301 columns, downloaded today) the
09-01 row is **2/301** NaN: **EA** (the 5m endpoint also refuses it — "possibly delisted") and
**APH**. Neither is a book holding. ⇒ **`asof` = 2026-09-01, no proxy label needed at the head.**

#### (b) 08-28 is now demonstrably permanent, not late ★

| | 2026-09-01 run (T+4) | **2026-09-02 run (T+5)** |
|---|---:|---:|
| names with NaN Close **and** Volume at 08-28 | **259 / 301** | **259 / 301** |
| names backfilled | 42 | **42** |
| change in 24h | (42 backfilled overnight) | **0** |

★ **The correct update is a change of category, not of number.** The vendor backfilled 42 names
between the 08-31 and 09-01 runs and then **nothing** in the following 24 hours. The desk should
stop treating this as a lag that will resolve and start treating it as **a partial session that will
sit inside every 20-session window until it rolls out**.

The mechanism is unchanged (`module_flow/_price_flow.py:29–31`):

    obv = (np.sign(close.diff()).fillna(0) * vol).cumsum()
    obv_chg = obv.iloc[-1] - obv.iloc[-21]
    obv_norm = obv_chg / vol.tail(20).sum()

With 08-28 missing, `close.diff()` is NaN at **08-28** *and* at **08-31** (its predecessor is NaN),
so `.fillna(0)` assigns direction **zero** to two of the twenty sessions. `vol.tail(20).sum()` sums
19 days into a 20-day denominator. Nothing in the output says so — `dropped_missing_axis=0`.

★ **Measured, not reasoned.** Taking the **42** names that *do* have an official 08-28 bar and
re-computing `obv_norm` with that bar blanked — simulating exactly what the other 259 suffer:

| | value |
|---|---:|
| mean abs Δ `obv_norm` | **0.0625** |
| median | 0.0335 |
| max | **0.3702** |
| `obv_state` label flips | **7 / 42 (17%)** |
| OBV **sign** flips | **5 / 42 (12%)** |

Worst cases, true → holed: **PCG** −0.086 → **+0.285** · **PYPL** −0.264 → −0.028 ·
**CRM** +0.340 → +0.183 · **MRVL** −0.129 → **+0.022** · **HPE** −0.201 → −0.062 ·
**NOW** +0.299 → +0.161.
⚠ **`CRM` is this run's rank-1 name by flow and `HPE` is a book holding** — both sit in the
distorted set.

⚠ **Honest delta vs yesterday's numbers** (0.0652 / 0.4040 / 12 label flips / 7 sign flips): the
sample is the same 42 names but the window has rolled one session, so the two are **not** directly
comparable and neither is evidence that "the hole is getting better". The label-flip rate fell from
29% to 17% because one more clean session entered the window, not because the instrument improved.

#### (c) The repair, and its residual
The 5m endpoint returns the 08-28 session for **300 of 301** names (EA excepted): bars per name
**median 78 · min 76 · max 78**. Patch applied to a **working copy only** — `history.json` was not
written (preflight rule 1). Validation against the **42 official** 08-28 bars:

| leg | result |
|---|---|
| **close** | mean abs err **0.0203%** · max **0.0937%** · names >0.05%: **4 / 42** |
| **volume** | mean **−18.15%** · median **−14.52%** · range **−4.74% … −54.58%** |

(Identical to yesterday's figures, as it must be — same 42 official bars, same 08-28 session. This
is a **reproduction**, not a new measurement, and is labelled as one.)

Carried through to the axis it feeds, on the same 42 names:

| | unpatched hole | **5m repair** |
|---|---:|---:|
| mean abs Δ `obv_norm` | 0.0625 | **0.0087** |
| max | 0.3702 | **0.0272** |
| `obv_state` label flips | **7 / 42** | **1 / 42** |
| sign flips | **5 / 42** | **1 / 42** |

⇒ The repair removes **~7×** more error than it injects. ⚠ **But it is not zero-flip this run** —
yesterday's entry recorded **0/42** label flips and today's records **1/42**. **That is written down
rather than smoothed** (`D48`): "zero label flips" was a property of one window, not of the
instrument. Worst residuals: **GOOG −0.027 · GOOGL −0.024 · MCHP +0.022 · NFLX −0.022 ·
AMZN −0.017.**

#### (d) The 09-01 session (official, complete — no proxy label needed)

| Risk-off | | Risk-on | |
|---|---:|---|---:|
| SMH | **−2.05%** | XLE | **+1.27%** |
| XLY | **−1.72%** | XLU | **+0.78%** |
| XLK | **−1.53%** | XLV | **+0.66%** |
| XLI | **−1.37%** | XLP | **+0.32%** |
| QQQ | **−1.27%** | XLRE | −0.16% |
| XLB | **−1.18%** | XLC | −0.52% |
| XLF | **−0.88%** | SPY | **−0.69%** |
| RSP | −0.82% | | |

Book holdings, 08-31 → 09-01: **MPC +2.59% · PSX +2.21% · NUE +0.91%** ·
AVGO −0.18% · MET −0.79% · NDAQ −1.09% · RTX −1.24% · NVDA −1.51% · **HPE −2.62% · ETN −2.78% ·
ANET −3.29%**.

- ✅ **Live authority**: **the 09-01 session may be cited plainly** from the daily endpoint.
- ✅ **08-28 may be cited from `SECTOR_FLOW_US_REPAIRED.json` or the 5m tape**, with
  **"5m-proxy (close err ≤0.094%, volume −18%)"** on the same line.
- 🚫 **Today's revocations**:
  1. **Do not cite `obv_norm` / `obv_state` / any OBV-derived flow score from the primary
     `SECTOR_FLOW_US.json`** — 259 of 298 scored names have two sessions zeroed out of the OBV
     window; measured label-flip rate **17%**. Use the repaired file.
  2. **Do not cite an 08-28 close from the daily endpoint for any name outside the 42 backfilled.**
  3. **Do not cite raw 08-28 volume, or any volume-magnitude claim for 08-28**, from either
     instrument — official is missing for 259, the proxy is **−18% biased**.
  4. **Do not cite anything about Wednesday 09-02's tape** — the market had not opened at run time.
  5. **Do not cite `EA` or `APH` flow/OBV/RS at all** — they are unscored (`n=298`, not 300).

### G1 — News-axis liveness 🔴 FAIL on the sweep axis · ✅ direct path LIVE

| Window | KST | `fts search --days 7 --count --scope foreign` |
|---|---|---|
| **pre-sweep** | 22:10 | **6/6** — Federal Reserve **1530** · Nvidia **5094** · tariff **1966** · jobs report **140** · oil prices **1456** · data center **2730** |
| **post-sweep** | 22:31 | **4/4** — identical (1530 / 5094 / 1966 / 140) |

Yet the sweep measured **17.11%** (51 of 298).

★ **The decisive probe — one variable changed, same names.** `flow_read.news_velocity`, run twice:

| Ticker | **1.5s cadence** | **9s cadence** | recent / base (7d / 30d) |
|---|---:|---:|---|
| TER | **None** | **0.34** | 10 / 127 |
| APP | **None** | **0.63** | 50 / 340 |
| CRM | **None** | **2.07** | 485 / 1005 |
| WMB | **None** | **1.86** | 33 / 76 |
| MDT | **None** | **1.87** | 69 / 158 |
| NEM | **None** | **0.81** | 47 / 248 |
| AVGO | **None** | **1.35** | 622 / 1971 |
| JCI (universe bottom-2) | — | **0.99** | 6 / 26 |
| PCAR (universe bottom) | — | **1.29** | 6 / 20 |
| CSCO | — | **0.83** | 120 / 621 |

⇒ **7 of 7 `None` values were refusals, not silence**, and the refusal is caused by request spacing
alone. `news_velocity` cannot distinguish "server refused" from "no articles"
(`module_flow/_news_velocity.py:126–136`), which is why the sweep's own 300-query burst reports 83%
of the universe as unmeasured. ★ Note **`CRM`**: the sweep's **rank-1 name by flow** was one of the
seven the sweep could not count, and its true velocity is **2.07 — accelerating**.

- 🚫 **Today's revocations**: **no theme-freshness / news-velocity citation sourced from the sweep**;
  **no "sector X is quiet" verdict from sweep coverage** — 247 of 298 were never counted. The 99 red
  names may **not** be described as having "no news flow".
- ✅ **Live authority**: **direct queries** (`fts search` · `brief` · `thread` · `chain-hop` · `burst`
  · `flow_read.news_velocity`). ★ Fire with **≥9s spacing**; **≤11 consecutive, ~90s pause if
  refused**, and write **"direct query, outside the sweep window"** on the same line as the number.
  **The sweep is not run again in this run.**

### G2 — Scoring-scale continuity ✅ PASS · Δ is a genuine one-session Δ
Scale: `n_axes=3`, `vel_axis=false`, `mode=nonews` — identical to the previous same-mode snapshot ⇒
**no mixed-scale subtraction risk.**

`scored` moved **299 → 298**: `APH` joined `EA` in the unscored set. The Δ baseline resolves to
**2026-08-31** (299 names, `nonews`), i.e. **one session**, not two as yesterday.

- ✅ **Live authority**: **Δflow may be cited today**, labelled **"repaired sweep (5m-proxy),
  08-31 → 09-01, ONE session, 3-axis nonews"** on the same line.
  Measured sector Δ: **Energy +0.295** · Utilities +0.267 · Health Care +0.214 · Real Estate +0.178
  · Cons. Staples +0.060 · Comm. Services +0.029 · Cons. Disc. −0.004 · IT −0.173 · Materials −0.208
  · Financials −0.220 · **Industrials −0.222**.
  Name movers: **up** FANG +0.84 · SYY +0.70 · EOG +0.69 · ABBV +0.66 · LLY +0.56 · PLD +0.54 ·
  XOM +0.54 · MPWR +0.50; **down** GLW **−1.11** · LRCX −0.90 · AXON −0.81 · EMR −0.79 · VRT −0.75 ·
  IDXX −0.73 · VMC −0.68 · MRVL −0.66.
- 🚫 **Revoked**: **no Δ from the primary `SECTOR_FLOW_US.json`** (its OBV axis is holed) ·
  **no Δ for `APH`** (it left the scored set between the two snapshots).
- ⚠ **The baseline is contaminated in a known direction.** The repair does **not** write
  `history.json`, so the stored 08-31 entry is yesterday's **primary** (holed-OBV) snapshot. Today's
  Δ is therefore **repaired-minus-holed**, biased by roughly the hole's own magnitude (0.06 on
  `obv_norm`, ≈0.13 on `flow_score`) in whatever direction the hole pushed each name.
  ⇒ **Δ may be cited as a direction, not as a magnitude.** **Logged, not fixed** — writing a repaired
  snapshot into shared history is a human-approval item (P5).

### G3 — Who owns the sector sign ✅ PASS (list printed) · ⚠ the guard misses the largest case
**Repaired file (citable): 1 of 11 sectors flips sign when its top-1 name is removed.**

| Sector | wflow | ex-top1 | top-1 | top-1 weight | n |
|---|---:|---:|---|---:|---:|
| **Consumer Discretionary** | −0.286 | **+0.033** | AMZN | **40.2%** | 28 |

Non-flippers, in full: Energy (XOM 30.5%, +0.505→+0.600) · Health Care (LLY 19.4%, +0.279→+0.279) ·
Materials (LIN 24.7%, +0.061→+0.016) · Real Estate (WELL 16.9%, −0.112→−0.244) · IT (NVDA 19.5%,
−0.117→−0.154) · Cons. Staples (WMT 28.9%, −0.143→−0.019) · Utilities (NEE 17.7%, −0.225→−0.248) ·
Financials (BRK-B 13.9%, −0.260→−0.240) · Industrials (CAT 8.7%, −0.502→−0.470) · Comm. Services
(GOOGL 38.3%, −0.506→−0.350).

⚠ **The primary file lists 2 flippers** — it adds **Consumer Staples/WMT** (−0.109 → +0.019). The
repaired file puts Staples at −0.143 → −0.019, no flip. **The two instruments disagree about
Consumer Staples**, so its sign is not established by either.

★ **`D459` reproduces, and larger than when it was registered.** Alphabet occupies **76.6%** of
Communication Services under **two tickers** (GOOGL 38.3% + GOOG 38.3%, flows −0.756 / −0.722). The
one-name guard removes only one class, so it prints `top1_flips_sign: False` while the true
ex-Alphabet reading is **wflow −0.506 → +0.257, a swing of 0.763** (yesterday: 0.691). `eqflow` is
**−0.013**, i.e. flat. **The negative sign on this sector is one company held twice.**

- 🚫 **Today's revocations**: **no promotion or demotion of Consumer Discretionary on `wflow`**
  (AMZN owns the sign) · **no `wflow` claim about Consumer Staples** (the two instruments disagree)
  · **no `wflow`-based claim about Communication Services in either direction** — the sign is
  Alphabet's two share classes, and the instrument's own guard cannot see it.
  Substitutes available today: `eqflow`, `breadth`, the official 09-01 tape, FRED transmission,
  short/COT positioning, direct news — each named **on the same line** as the conclusion it supports.

### G4 — Risk-unit stability 🔴 FAIL
All three windows actually run (`risk_units.py --book --days {250,500,750}`, bench SPY, 1-factor
residual; logs `preflight/_ru{250,500,750}.log`). All three end **2026-09-01**.

| `--days` | trading days | units @0.65 | within-group resid. corr | ARI (1st vs 2nd half) |
|---:|---:|---:|---:|---:|
| 250 | 249 | **12** | +0.8512 | 0.3874 |
| 500 | 499 | **10** | +0.5278 | 0.2328 |
| 750 | 749 | **10** | +0.5179 | 0.3810 |

- 250d membership: `U0 {MPC, PSX}` then **ten singletons** — ANET, AVGO, ETN, HPE, MET, NDAQ, NUE,
  NVDA, RTX, plus the 2 KR names each alone. The 500/750d windows instead merge **ANET+ETN** and
  **AVGO+NVDA**. ⇒ **Whether the four AI names are one bet or four still flips with the window.**
  The 500/750 runs raise the tool's own label warning (ANET+ETN carry two book theme labels inside
  one measured unit, so `MAX_THEME_PCT` counts them as two).
- Threshold sensitivity: at dist **0.40–0.60 all three windows converge on 12 units**; they diverge
  only at the chosen **0.65**.
- ARI (0.23–0.39) moves **opposite** to fit (+0.52–0.85) in all three. The 250d run raises its S5
  short-sample flag (249 < 250) and is also the window with the *highest* fit — the S5 trap exactly.
- 🚫 **Today's revocations**: **no single-number concentration/diversification claim.** Any
  concentration statement must carry the `--days` used **on the same line**.

### G5 — Does the universe cover the book 🔴 FAIL (freshness leg)
- **Cover leg ✅**: `data/us_universe/us_top300.csv` **300 rows**; all 11 US holdings
  (ANET·AVGO·ETN·HPE·MET·MPC·NDAQ·NUE·NVDA·PSX·RTX) present. **Missing 0.**
- **Freshness leg ❌**: mtime **2026-07-15** ⇒ **49 days** (bar ≤8; the sweep prints its own warning).
  `us_all_v2_candidate.csv` (2026-08-10) sits beside it but is **a candidate, not the wired source** —
  not switching today (file replacement is a human-approval item).
- 🚫 **Today's revocations**: **do not cite market-cap rank or cap-weighting (`wflow`) as "current
  size"** — it is a 49-day-old weighting. This compounds G3 twice over: Consumer Discretionary's sign
  rests on AMZN's 40.2% weight and Communication Services' on Alphabet's 76.6%, and **both weights
  are seven weeks stale**.
- ⚠ The 2 KR names in the book (`028050`, `316140`) are outside the US universe by construction and
  are covered by the KR desk — not a US coverage miss.

### G6 — Instrumentation accrual rate 🔴 FAIL
`snapshot_estimates.py --status`: **23 files / 43 calendar days** (2026-07-22 → 2026-09-02) ⇒
**0.53/day**. 17 more needed for the 40-day target ⇒ ideal 17 days vs **measured ~32** = **1.9×**
(threshold 1.5×). Gap median **1**, max **6**. Today's snapshot stored (120 names).
- 🚫 **Today's revocations**: **do not report `kelly_size --ic` as an evidenced size.** If used, write
  **"mechanical 1/4"** explicitly.
- ⚠ Not recoverable retroactively — a day not accrued is gone (valid sample = number of **dates**, S1).

### G7 — Tool liveness 🟡 PASS with 2 named exceptions
`--help` exit codes: **35 of 37 are 0** — the same two exceptions as the last two runs.

| Group | exit 0 |
|---|---|
| `module_KIS`·`module_news_data`·`module_flow`·`module_watchlist`·`module_paper_book`·`module_valuation`·`module_business`·`module_business_us`·`module_disclosure`·`module_disclosure_us`·`module_fundamentals_us`·`module_industry_map`·`module_report_tags`·`module_inflection`·`module_macro_us`·`module_evidence` | ✅ 16/16 |
| `sector_flow`·`us_live_shortlist`·`us_setup_screener`·`us_flow`·`flow_read`·`risk_units`·`snapshot_estimates`·`exposure_rule`·`missed_ledger`·`kelly_size`·`catalyst_calendar`·`report_lint`·`reject_ledger`·`drift_watch`·`cycle_exposure`·`action_bracket`·`company_score`·`axis_inflection`·`axis_window_flow` | ✅ 19/19 |
| `python -m module_chart --help` | 🟡 **1** — prints a usage stub, not argparse (it is `module_text_chart`, positional ticker) |
| `scripts/margin_history.py --help` | 🔴 **1** — argparse `ValueError: unsupported format character`; KR-only tool, unused by this run |

★ **The chart tool was re-probed live rather than judged on `--help`:** `python -m module_chart
NVDA` · `ANET` · `SPY` → **0 / 0 / 0**, 3/3 render.
- ✅ **Live authority**: **US chart shape/pattern may be cited**, on data ending **09-01**.
  ⚠ Any chart window spanning 08-28 inherits the hole for the 259 names — say so if the read depends
  on that bar.
- 🚫 `scripts/margin_history.py` output may not be cited (unused here regardless).

---

## 🧾 Everything this run **may not claim** — collected

1. **OBV / accumulation-distribution / flow score taken from the primary `SECTOR_FLOW_US.json`** —
   259 of 298 scored names have two sessions zeroed out of the OBV window; measured label-flip rate
   **17%** (G0b). Use `SECTOR_FLOW_US_REPAIRED.json`, labelled.
2. **Any Δflow from the primary file** · **Δ cited as a MAGNITUDE** — the baseline is yesterday's
   holed primary snapshot, so today's Δ is repaired-minus-holed (G2). Direction only.
3. **`wflow` promotion/demotion of Consumer Discretionary** (AMZN 40.2% owns the sign) · **any
   `wflow` claim about Consumer Staples** (the two instruments disagree) · **any `wflow` claim about
   Communication Services** (Alphabet is 76.6% under two tickers and the guard cannot see it) (G3).
4. **News velocity / theme freshness / "it is quiet"** *when sourced from the sweep* (G1) — 247 of
   298 names were never counted, and the `None`s are demonstrably refusals: 7/7 flipped to real
   numbers on cadence alone.
5. **08-28 closes from the daily endpoint for the 259 unbackfilled names** · **any 08-28 volume or
   volume-magnitude claim from either instrument** · **anything about Wednesday 09-02's tape** — the
   market had not opened at run time · **`EA` and `APH`** — unscored (G0).
6. **Concentration/diversification as a single number** (G4) · **market-cap-weighted "current size"**
   (G5, 49 days stale) · **`kelly_size --ic` as evidenced** (G6) · **`margin_history` output** (G7).

## ✅ What is **live** today
- ★ **The 09-01 session, officially and without a proxy label** — 2/301 NaN (EA, APH), 0/16 on the
  direct book probe.
- ★ **`SECTOR_FLOW_US_REPAIRED.json`** (298 scored, 3-axis nonews, asof 09-01, 258 names patched at
  08-28), **including a genuine one-session Δ vs the 08-31 snapshot** — always labelled "repaired,
  5m-proxy, one-session Δ, holed baseline". Residual error bounded on both legs: close ≤0.094%,
  OBV 0.0087 mean / 0.0272 max, **1/42 label flips** (not 0 — see G0c).
- **Direct news queries** at every entry point: **6/6 pre-sweep · 4/4 post-sweep · 10/10
  falsification at 9s cadence**. ★ ≥9s spacing, ≤11 consecutive, ~90s pause if refused.
- **`module_chart`** — live 3/3.
- **`module_macro_us` (FRED)** · **`module_disclosure_us` / `module_business_us` /
  `module_fundamentals_us`** · **`us_flow` (FINRA short-vol / CFTC COT)** — `--help` clean, none of
  them touch the 08-28 hole.
- **Book positions and cost basis**, and the price column (09-01 marks are real).

---
> Output: `preflight/PREFLIGHT.md` · logs `preflight/_ru{250,500,750}.log` · `../_sweep.log` ·
> `../_repair.log` (+ `../_repair.py`, the working-copy patcher) · primary `../SECTOR_FLOW_US.json`
> · repaired `../SECTOR_FLOW_US_REPAIRED.json`
