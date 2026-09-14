# MACRO_REPORT — industry_US · 2026-08-20 (Thu) · Stage 1 / L1·MACRO

> `--market us` · news `--scope foreign` on every call · settled frame ends **2026-08-19**.
> Run clock **KST 22:3x–23:4x = ET 09:3x–10:4x**. Analytical output only — no buy/sell, no sizing (P4).

---

## ★★★ The one thing this report exists to say today

**A Treasury debt-management action, not the Fed and not the rate path, was the macro event of this
window — and it landed inside the settle windows of four of this desk's own duration brackets, on the
same day the FOMC minutes printed.**

On **2026-08-19** Treasury Secretary Bessent announced a **doubling of long-dated Treasury buyback
operations**, explicitly to lean against long-end yields sitting at **`DGS30` 5.28 — within 3bp of the
252-observation high of 5.31** `[FRED, 08-18]`. Eight separate head- and body-tier clusters carry it
(`--scope foreign`), the dollar went to three-month lows, gold jumped, and `theme_age "Treasury
buybacks"` returned **🟢FRESH, age 1 day, n=64** — **the first 🟢FRESH this desk has produced in ten
consecutive runs.**

**Three consequences, and none of them is the obvious one.**

1. **The equity tape did NOT trade it as a duration event.** Over the five settled sessions
   08-12 → 08-19, `XLU` — the purest duration leg — is the **weakest** of the four legs at **+0.855pp**
   excess vs `SPY`, while `XLV` is **+4.742** and `XLE` **+4.622**. `XLK` is **−2.320**, the worst
   sector on the board. **Money went to pharma and energy and came out of AI-compute.** A yield cap
   that helped nothing rate-sensitive is not a rate story.
2. **`S98`'s and `S102`'s VOID clauses both point at 08-19, and this desk must decide that before it
   sees which branch would have fired.** `S98` voids on *"an FOMC-dated communication … inside the
   window"* — the minutes released **08-19** are inside 08-13→08-20. `S102` voids on *"a Treasury
   refunding announcement inside the window"* — and `S102` was **registered on 08-19 as the repair for
   the self-voided `P73`, which carried the identical clause.** §E-0 rules on both, on the clause.
3. **The book's largest theme is at a two-year extreme, on the wrong side.**
   `EW{AVGO, ANET, HPE, COHR, LITE}` 5-session excess vs `SPY` = **−12.425pp = the 0.8th percentile of
   two years** (252d mean +1.96, sd 5.93). All five are held in the real book. This is not in any
   proposition the desk carried into today.

---

## §0 · Instrument state — read FIRST, because it decides what this stage may do

Inherited from `preflight/PREFLIGHT_US.md` (**PASS 3 / FAIL 5**) and `HANDOVER.md §0`.

**This stage may not** cite the sweep's news-velocity axis, theme freshness as a ranked quantity,
"it went quiet" for any name or sector, `breadth` as news-independent, the **Materials `wflow` sign**
(`LIN` 24.7% owns it), a concentration number without its `--days`, any `wflow` as *current* cap
weighting (36-day-old weights), **`EA`**, or **any 08-20 price**.

**This stage may** cite settled prices through **2026-08-19**, a **one-session Δ (08-18 → 08-19)**,
`eqflow` and the ten non-flipper sector signs, FINRA/COT positioning, `[FRED]`, primary filings, and
**hand-probed news velocity**.

⚠ Two carried rules bind every number below:
- **`R81`/`D290`** — `flow_tag` does not take the run-level axis set. **Measured again today, 10th
  consecutive replication**: of **7 greens**, only **3** (`MRK` 1.28 · `TGT` 1.27 · `KKR` 1.20) clear
  `vol_surge ≥1.2`; the other **4 are velocity-derived** — `LLY` (vel 1.20, surge 0.86) · `MRVL`
  (1.35 / 0.69) · `MA` (1.28 / 0.80) · `WMT` (1.34 / 0.93) — on the axis `G1` revoked. **No tag is
  used as evidence anywhere in this report.**
- **`D293`** — `delta` mixes earned excess with rolling-window roll-off and `sector_flow` publishes
  neither leg. Today's Δ spans **one** session, so the roll-off share is 1-in-20 rather than 2-in-20 —
  **smaller, not zero.** No verdict below rests on Δ alone.

---

## §A · Primaries — `[FRED]`, and the whole 60-session move in the 10y is REAL yield

Pull: `module_macro_us --series … --days 120 --json`, 22:3x KST. **14 of 14 series returned.**
★ Unlike the 08-17 run (`M715`: a full-run identity, zero new observations in all 14), **7 of 14 series
carry a new observation versus the 08-19 pull.** The instrument moved.

| Series | Last obs | Value | Δ 5 obs | Δ 20 obs | Δ 60 obs | 120d range |
|---|---|---:|---:|---:|---:|---|
| `DFF` Fed Funds eff. | 2026-08-18 | **3.630 %** | 0.000 | 0.000 | 0.000 | 3.62 – 3.64 |
| `DGS2` 2y | 2026-08-18 | **4.190 %** | −0.030 | **−0.070** | +0.110 | 3.38 – 4.37 |
| `DGS10` 10y | 2026-08-18 | **4.710 %** | +0.010 | **+0.080** | **+0.140** | 3.97 – 4.75 |
| `DGS30` 30y | 2026-08-18 | **5.280 %** | +0.040 | **+0.150** | +0.180 | 252-obs **min 4.54 · median 4.86 · max 5.31** |
| `DFII10` 10y TIPS real | 2026-08-18 | **2.410 %** | −0.020 | +0.040 | **+0.230** | 1.72 – 2.47 |
| `T10YIE` 10y breakeven | **2026-08-19** | **2.300 %** | +0.040 | +0.020 | **−0.100** | 2.18 – 2.50 |
| `BAMLH0A0HYM2` HY OAS | 2026-08-18 | **2.750 %** | +0.030 | +0.060 | +0.040 | **2.63** – 3.46 |
| `BAMLC0A0CM` IG OAS | 2026-08-18 | **0.820 %** | +0.030 | +0.040 | +0.080 | 0.73 – 0.94 |
| `NFCI` | 2026-08-14 | **−0.559** | −0.031 | −0.099 | — | **−0.559** – −0.460 |
| `VIXCLS` | 2026-08-18 | **15.84** | +0.560 | −1.210 | −1.170 | 14.25 – 31.05 |
| `DTWEXBGS` Broad Dollar | 2026-08-14 | **118.903** | −0.162 | **−1.629** | −0.548 | 117.46 – 121.41 |
| `CPIAUCSL` CPI | 2026-07-01 | 332.813 | — | — | — | ⚠ **monthly, ~7 weeks stale** |
| `CPILFESL` Core CPI | 2026-07-01 | 336.789 | — | — | — | ⚠ same |
| `UNRATE` | 2026-07-01 | **4.100 %** | — | — | — | ⚠ same; 120d range 4.10 – 4.50 |
| `M2SL` | 2026-06-01 | 23,155.2 $bn | — | — | — | ⚠ **~11 weeks stale** |

⚠ **C1 — the `[FRED]` frame ends 2026-08-18, which is BEFORE the buyback announcement.** Every yield
number above is a **pre-event** reading. The 08-19 reaction (long yields down, dollar to three-month
lows, gold up) is `[news]`-grade in this report and becomes `[FRED]`-grade at the next pull. **Any
stage that treats the table above as the post-buyback curve is wrong.**

### A-1 · The decomposition, because the direction alone is not the finding — **[measured]**

`DGS10` is **+0.140** over 60 observations. Over the same 60 observations `DFII10` is **+0.230** and
`T10YIE` is **−0.100**. **+0.230 − 0.100 = +0.130 ≈ +0.140.**

⇒ **The entire 60-session rise in the 10-year is real yield, and inflation compensation has fallen
against it.** Stated positively: this is a **real-rate/term-premium** repricing, **not** an inflation
repricing. `real_10y` is quoted with `breakeven_10y` as the rule requires, and the two disagree by
design — that disagreement is the content.

⚠ **C2, the half that argues the other way**: `DGS2` is **−0.070 over 20 obs** while `DGS10` is
**+0.080** and `DGS30` **+0.150**. The front end is *easing* while the long end sells off. That is a
**bear steepener at the long end sitting on top of a bull move at the front** — two different stories
in one curve, and this desk has repeatedly mislabelled it as one (`R73`, `P65`).

### A-2 · The curve, in levels and in its own distribution — **[measured]**

| Spread | Now (08-18) | 252-obs p15 | p50 | p85 |
|---|---:|---:|---:|---:|
| **2s10s** (`DGS10−DGS2`) | **+0.520** | +0.420 | +0.540 | +0.650 |
| **30y−10y** | **+0.570** | +0.510 | **+0.590** | +0.650 |

★ **Both spreads sit BELOW their own one-year medians.** The 30y is near a one-year high **in level**
(5.28 vs max 5.31) while the 30y−10y **spread** is below median — i.e. **the long end is expensive
because the whole curve is high, not because the term-premium wedge is unusually wide.** This is the
distinction `P65`/`R73` kept collapsing, and it is why `P65`'s conjunction now fails on both legs
(`30y−10y` **0.570 < 0.58** ❌ and `DGS2` **4.190 > 4.15** ❌ — see §F).

### A-3 · The credit axis, cited because a risk-off claim without it is narrative-only

`HY OAS` **2.750%** — **12bp off its own 365-day low (2.63)**, and **+6bp over 20 observations**.
`IG OAS` **0.820%**, +4bp/20obs. `NFCI` **−0.559 = the loosest reading in the 120-day window.**

⇒ **Credit has widened marginally and financial conditions are at their easiest of the window.**
Any "risk-off" or "credit stress" reading of the 08-19 equity rotation is **narrative-only** and is
labelled as such wherever it appears below. The AI-compute drawdown in §C is **not** a credit event.

---

## §B · Positioning — CFTC COT, and it is a **six-run replay**, which is itself the finding

`scripts/us_flow.py --cot`, 22:2x KST.

| Instrument | Net spec | Weekly Δ | 1y %ile | Read |
|---|---:|---:|---:|---|
| **S&P 500 (E-mini)** | +11,280 | +38,538 ▲ | **88th** | 🟢 crowded long |
| **Nasdaq-100** | **−42,905** | −7,899 ▼ | **0th** | 🔴 crowded SHORT |
| Russell 2000 | −13,943 | −5,044 ▼ | 18th | 🔴 crowded short |
| **UST 10Y** | −915,053 | +64,190 ▲ | **7th** | 🔴 crowded short |
| UST 2Y | −1,021,043 | −16,815 ▼ | 63rd | 🟡 neutral |
| **USD Index** | +21,409 | −1,090 ▼ | **80th** | 🟢 crowded long |
| **WTI Crude** | +23,226 | +193 ▲ | **18th** | 🔴 crowded short |
| Nat Gas | −197,135 | +411 ▲ | **2nd** | 🔴 crowded short |
| Gold | +217,940 | +20,306 ▲ | 49th | 🟡 neutral |
| **Copper** | +80,388 | +3,265 ▲ | **100th** | 🟢 crowded long |
| Silver | +23,646 | +1,366 ▲ | 33rd | 🟡 neutral |

🚨 **Every cell above is digit-identical to the 08-15, 08-16, 08-17 and 08-19 reports. This is the
SIXTH consecutive run on one COT observation.** The cause is mechanical and is stated rather than
implied: COT is published Fridays covering the prior Tuesday. The most recent release is **Friday
2026-08-14, covering Tuesday 2026-08-11** ⇒ **the positioning axis is 9 calendar days stale**, not the
"3–4 day lag" the tool's own footer warns about. **The next refresh is Friday 2026-08-21.**

⇒ **No proposition below is anchored on COT**, and any downstream stage citing a percentile must
carry **"as of 2026-08-11"** on the same line. ★ This is `M715`'s accounting applied to a second
instrument: three of this desk's four macro instruments (COT, monthly FRED series, the news-velocity
axis) carried **zero new information** into this run; only the daily `[FRED]` series and the tape did.

⚠ Two positioning readings still bear on live rows and are recorded with their staleness:
**`Copper` at the 100th percentile** is the reading `S77`/`FCX` was resolved 🔴 against (HANDOVER §1),
and **`WTI` at the 18th percentile with Brent at 91.62** is rebound ammunition against the Energy leg's
own direction — a crowded-short in the commodity the desk is long the refining margin of.

---

## §C · The tape — settled through 2026-08-19, and it moved hard

### C-1 · Sector excess return, 5 settled sessions 08-12 → 08-19, `SPY` **−0.444%** — **[measured]**

β measured on **252 daily returns** (`C5`: the window is a choice and is on the same line as the number).

| Sector ETF | 5-sess ret | **raw exc vs `SPY`** | β(252) | **β-adj exc** |
|---|---:|---:|---:|---:|
| **`XLV` Health Care** | +4.298 | **+4.742** | 0.268 | **+4.417** |
| **`XLE` Energy** | +4.178 | **+4.622** | −0.278 | **+4.055** |
| `XLP` Staples | +1.716 | +2.160 | −0.077 | +1.682 |
| `XLRE` Real Estate | +1.124 | +1.568 | 0.273 | +1.245 |
| `XLC` Comm. Svcs | +0.952 | +1.396 | 0.678 | +1.253 |
| `XLY` Cons. Disc. | +0.594 | +1.038 | 1.178 | +1.117 |
| **`XLU` Utilities** | +0.411 | **+0.855** | 0.146 | **+0.475** |
| `XLB` Materials | −0.114 | +0.330 | 0.740 | +0.215 |
| `XLF` Financials | −0.760 | −0.316 | 0.612 | −0.488 |
| `XLI` Industrials | −2.114 | −1.670 | 0.954 | −1.691 |
| **`XLK` Info Tech** | −2.764 | **−2.320** | 1.736 | **−1.993** |

★★ **The single-session 08-19 decomposition (equal-weight, `us_top300`, `SPY` +0.21%)** confirms the
same ordering on one bar, so the 5-session read is not a window artifact:
**Health Care EW +2.42% (excess +2.22pp) · Cons. Disc. +1.72 · Comm +0.91 · Staples +0.88 · Materials
+0.85 · Real Estate +0.52 · Utilities −0.16 · Financials −0.18 · Energy −0.46 · Industrials −0.60 ·
Info Tech −1.39% (excess −1.60pp).**

### C-2 · ★ Health Care's move is idiosyncratic and it is NOT one name — **[measured]**

08-19 single session, 32 `us_top300` Health Care names:
`MRK` **+12.60%** · `ALNY` +6.12 · `DHR` +5.97 · `A` +4.70 · `VRTX` +4.52 · `LLY` +4.46 · `TMO` +4.16 ·
`AMGN` +4.02 · `BDX` +3.78 · `REGN` +3.78 · `WAT` +3.64 · `PFE` +3.63 — against **`UNH` −1.35 ·
`CVS` −1.33 · `MCK` −1.79 · `HCA` −1.14**.

- **The control (C4)**: removing `MRK` leaves EW **+2.09%**, still **+1.88pp** over `SPY`. **It is not
  one name.**
- **The cause is named and primary-ish**: `MRK`+`MRNA` melanoma cancer-vaccine trial results, carried
  by `upi` · `scmp` · `seekingalpha` · `yahoo_finance` (*"landmark moment"*), and `theme_age
  "cancer vaccine"` reads **🟡ACCELERATING 25.71×, n=103** — a denominator that clears `T24` comfortably.
  `blindspot` independently surfaced **`REGN` z 7.5** and **`REGENERON` z 4.9** at 100% market
  relevance, i.e. the breadth shows up in a vocabulary-free instrument too.
- **The ordering is business-model, not duration**: pharma/biotech/tools lead, **managed care and
  distribution lag** — exactly the `M721` split (med-tech +0.315 vs managed care −0.402) that was
  entered *before* `S82`/`S98` settle. **The prediction registered on 08-17 is being paid.**

### C-3 · ★★ The AI-compute complex is at a two-year extreme, and the desk owns all of it — **[measured]**

5-session excess vs `SPY`, settled 08-19:
**`COHR` −18.72 · `AVGO` −12.43 · `LITE` −10.80 · `ANET` −10.98 · `HPE` −9.18 · `NUE` −8.04 ·
`ETN` −7.23 · `CIEN` −7.10 · `ORCL` −5.73 · `NVDA` −2.47.**

`EW{AVGO, ANET, HPE, COHR, LITE}` exc5 = **−12.425pp = the 0.8th percentile of 252 observations**
(mean +1.959, sd 5.930, p05 −7.715). **All five are held in the real book**
(`module_KIS.fetch_overseas_balance`, 12 names — `T22`: this is the real book, not the paper book's 11).

★ **The optical/interconnect node the desk promoted to a 5th DEEP on 08-17 is the worst of it.**
`COHR` −18.72 and `LITE` −10.80 over five sessions; the third name of the node, `CIEN`, has a
**FADING** thread titled *"Why Ciena Stock Tanked by Almost 9% on Tuesday"* (3→3→7→9→9→6 outlets);
and `theme_age "optical interconnect"` has cooled to **⚪ECHO 1.35×, n=150** against the `optical`
**1.74× = highest of 19 terms** measured on 08-17. **`S96` — "is the optical layer EARLY or LATE?" —
settles 08-21 and every axis available today points at LATE.**

⚠ **The counter-evidence, stated rather than buried**: **`MRVL` +9.85% on 08-19** (+9.74 exc5) on
*"Marvell gives Google option to buy $12.2 billion stake"*, and `MRVL` is a custom-AI-silicon /
optical-DSP name. **One name in the node ripped while the rest collapsed** ⇒ the correct sentence is
*"the node dispersed violently"*, not *"the node was sold"*. `MRVL` is **not held**.

### C-4 · `M718` / `D270` replicates a **NINTH** time — **[measured]**

**105** of 299 names pass `OBV 매집 ∧ RS20>0`. **Exactly 3** also clear `vol_surge ≥1.2`
(`MRK` 1.28 · `TGT` 1.27 · `KKR` 1.20) ⇒ **102 blocked, 97.1% of them on `vol_surge` alone.**
Median `vol_surge` across the universe: **0.740**.
From the other side: **12** names clear `vol_surge ≥1.2` and **9 of them are 🟡 or 🔴**
(`MNST` 1.64 · `COHR` 1.51 · `KEYS` 1.47 🔴 · `NKE` 1.31 · `SNDK` 1.30 🔴 · `CSCO` 1.28 · `TJX` 1.23 ·
`EBAY` 1.20 · `MO` 1.20).

⚠ **And the axis is contested across markets.** `HANDOVER §7`: `vol_surge` IC clears Bonferroni in
**KR** with a **negative** sign (h=1 t −3.30, n_eff 27), while the **US** ledger reads **+0.0253,
t +1.49, n_eff 20 — indistinguishable from zero and pointing the other way**. `D290-KR`'s conclusion
**must not be imported** (`W1`). The US gate question is open.

### C-5 · Flow, 3-axis, settled 08-19 — **[measured]**

| Sector | n | `wflow` | `eqflow` | 🟢 | 🔴 | Δ (1 sess) | top1 (w%) | ex-top1 |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| **Health Care** | 32 | +0.282 | **+0.252** | 2 | 2 | +0.169 | `LLY` (19.4) | +0.238 |
| **Energy** | 16 | +0.197 | **+0.182** | **0** | **0** | −0.157 | `XOM` (30.5) | +0.257 |
| Comm. Services | 12 | −0.262 | +0.023 | 0 | 2 | +0.176 | `GOOGL` (38.3) | −0.296 |
| Cons. Discretionary | 28 | −0.233 | +0.022 | 0 | 3 | +0.145 | `AMZN` (40.2) | −0.237 |
| Cons. Staples | 19 | +0.088 | −0.012 | 2 | 3 | +0.005 | `WMT` (28.9) | +0.038 |
| Materials | 12 | −0.099 🚩 | −0.064 | 0 | 4 | +0.018 | `LIN` (24.7) | +0.063 |
| Industrials | 50 | −0.085 | −0.073 | 0 | 10 | −0.056 | `CAT` (8.7) | −0.027 |
| Financials | 47 | −0.009 | −0.127 | 2 | 8 | −0.037 | `BRK-B` (13.9) | −0.048 |
| Info Technology | 56 | −0.283 | −0.197 | 1 | **19** | −0.088 | `NVDA` (19.4) | −0.290 |
| Real Estate | 12 | −0.309 | −0.252 | 0 | 4 | −0.014 | `WELL` (16.9) | −0.217 |
| **Utilities** | 15 | **−0.568** | **−0.545** | 0 | **8** | −0.171 | `NEE` (17.7) | −0.578 |

🚩 = the run's only `top1_flips_sign` bucket (`G3`); Materials' `wflow` sign may not be used.
Universe `wflow` **−0.162**; tags 🟢7 / 🟡229 / 🔴63.

★★ **Price and flow agree at the top and DISAGREE at the bottom.** Health Care and Energy lead **both**
rankings. But **Utilities is last on flow by a wide margin (`eqflow` −0.545, 8 red of 15, zero green,
`ex_top1` −0.578) while its price excess is POSITIVE (+0.855pp)** — a sector being bid on price with
no accumulation underneath it. **That disagreement is the empirical core of §E's `P78`.**
★ **Energy carries 0 greens and 0 reds out of 16** while running the board's second-best price excess
and second-best `eqflow` — a pure `vol_surge`-gate artifact (§C-4), not an absence of money.

---

## §D · News — `--scope foreign`, coverage stated before anything is concluded

### D-0 · Coverage accounting — because `tail = 0` is not a coverage claim

`brief --date 2026-08-20 --scope foreign --body 2 --json`, after `embed sync` (6,051 new vectors,
cursor **2026-08-20T21:31:15**).

| Field | Value |
|---|---|
| `denominator.articles` | **1,953** |
| `clusters` | 700 |
| `events_2src_plus` | **338** (head 30 · body 308) |
| `subevents_recovered` | **42** |
| `single_source_clusters` | **362**, of which **15 shown ⇒ 347 withheld** |
| `tail` | **0** shown of **0** |
| `excluded_nonmarket` | **0** of **0** |
| `excluded_not_news` | **`{}` — empty** |

🚨 **Two of those zeros are instrument limits, not observations, and this report will not read them as
coverage.**
1. **`nonmarket_events = 0` and `excluded_nonmarket = 0` because the classifier is Korean-only.** The
   tool says so itself: *"해외는 점수가 없어(분류기 한글 전용) 무작위 표본"* — `single_source` reports
   `scored 0 · scorable 0 · unscored 362`. ⇒ **On foreign scope the desk has NO non-market filter and
   NO ranking inside the single-source tier**; the 15 shown are a random sample, not the top 15.
2. **`excluded_not_news` is empty ⇒ the denominator is UNCORRECTED.** The 1,953 figure has not had
   translation duplicates or bot copy removed. It is quoted as an upper bound.

⇒ **347 single-source clusters were counted and not read**, and they are the tier where FX and rates
singles live. **No "quiet" claim appears anywhere in this report**, and the `G1` revocation makes such
a claim inadmissible in any case.

### D-1 · Events — the head, with denominators

The head (≥5 outlets, 30 clusters). **One macro object dominates it and it is carried by eight
separate clusters**, which is why it is stated as a single event rather than eight:

| Outlets | Cluster |
|---:|---|
| 8 | **US debt tops $40 trillion as Treasury doubles bond buybacks to calm markets** |
| 6 | Global Market: **Treasury bond buybacks complicate Fed's path to price stability** |
| 6 | **Dollar hugs three-month lows as Treasury seeks to soothe the bond market** |
| 5 | **Asian stocks rally as US Treasury steps in to ease bond fears** |
| 4 | **Treasury Bond Fix Could Backfire, Warns JPMorgan** |
| 4 | **JPMorgan Team Sees Credibility Risk in Treasury's Bond Buybacks** |
| 3 | **To Support The U.S. Treasury Market, Bessent Sent The Greenback Reeling** |
| 3 | Stock market today: futures steady **after Treasury's bond intervention buoys markets** |

**Body-read (`fts search "long-dated" buybacks --mode and --days 2 --scope foreign --full`, 71
matches):** `[fxstreet]`, quoting MUFG — *"The US dollar weakened after US Treasury Secretary Bessent
announced a significant expansion of long-dated Treasury buyback operations, a move to ease pressure
from rising long-end yields… While buybacks alone are unlikely to alter longer-term fundamentals, they
do signal willingness by policymakers to lean against further yield increases."* `[seekingalpha]`/ING:
*"the US Treasury has decided to double the buybacks in the 10yr."* **The mechanism is named by the
actor, not inferred.**

The rest of the head, in outlet order:
**Iran — `Oil prices rise as Trump sharpens Iran rhetoric amid talks impasse` (17 outlets / 29 art)
and `Trump vows 'economic warfare' on countries helping Iran` (14 / 16)** · `Gains in AI company stakes
juice Q2 earnings for S&P 500` (11) · Ukraine strikes on Kyiv (11) · Bitcoin toward $70k (9) ·
Evergrande founder sentenced (9) · Amazon's Anthropic stake (8) · **`Walmart shares slide as U.S. sales
hit by falling drug prices` (5) + `Walmart Posts Weakest Sales Growth in Years` (4)** ·
`Big Tech Is on Pace to Spend $735 Billion on AI Data Centers in 2026` (5) · `Why Marvell Stock Surged
Today` (5) · `Gold hovers near early-June high on lower bond yields` (5).

⚠ **`Walmart` is also the day's largest single-name burst** — `blindspot` z **5.5**, **39 articles, 12
outlets, market-relevance 100%**. `WMT` reported **08-20 pre-market**, i.e. inside this run's clock and
**outside its settled frame**. Its price consequence lands on tonight's close and is `S100`'s leg.

### D-2 · Trajectories — `thread --days 7`, foreign

Per-day denominators first, because the window's last day is incomplete:
**08-14 743 · 08-15 282 · 08-16 294 · 08-17 752 · 08-18 826 · 08-19 801 · 08-20 338.**
⚠ **08-20 is running at ~42% of 08-19's volume because the day is still in progress at run time.**
**Every FADING tag in this window is therefore suspect**, and the report treats them as such.

- 🟢 **BUILDING · 4 days · outlets 4→4→6→14 · 35 articles — the Iran "economic warfare" thread.**
  `US to Roll Out 'Economic Isolation' Plan for Iran` (08-14) → `What Bessent's economic isolation of
  Iran could look like` (08-15) → `Trump announces 'most crushing economic operation ever'` (08-19) →
  `Trump vows 'economic warfare' on countries helping Iran` (08-20, 14 outlets). **The steepest
  acceleration on the board, and it is at day 4, not day 5+ of a peak.**
- ⚪ **ENDED · peak 14 outlets · `Trump Takes Hard Line on Iran as Hormuz Standoff` (08-14→08-18).**
  ⚠ **This is a re-labelling, not a death** — the same story continues under the BUILDING thread above.
  Recorded so an ENDED tag is not read as a staleness flag on a live proposition.
- 🔴 **FADING · `Oil edges up on uncertainty over exports through Hormuz` (16→5→12→16→17→19→17)** —
  ⚠ **contradicted by its own raw count**: `Hormuz` returns **576 articles over 2 days** on the CLI.
  The tag is a partial-final-day artifact. **`T24` applies and the tag is not cited.**
- 🔴 **FADING · `US treasury doubles debt buyback to steady bond market` (11→6)** and
  `Bond Yields Dive After Treasury Increases Buybacks` (4→6→2) — ★ **while `theme_age "Treasury
  buybacks"` reads 🟢FRESH, age 1, n=64.** **Two instruments, one theme, opposite tags, same day.**
  The disagreement is fully explained by the partial final day; `theme_age`'s estimator (age + volume
  vs a 30-day baseline) is the admissible one here and `thread`'s day-over-day count is not.
- 🔴 **FADING · `'Many' Fed officials think higher rates will be needed` (6→9→5→17→3)** — **the FOMC
  minutes of 08-19 read hawkish and peaked at 17 outlets.** The 3 is today's partial day.
- 🔴 **FADING · `Moderna's cancer-vaccine breakthrough drives broad bio…` (20→3)** — same artifact;
  `theme_age "cancer vaccine"` reads **25.71× on n=103**.
- 🔴 **FADING · `Why Ciena Stock Tanked by Almost 9% on Tuesday` (3→3→7→9→9→6)** — an **optical-node
  negative** with a real, seven-day denominator. Carried to §C-3.
- 🔴 **FADING · `Marvell gives Google option to buy $12.2 billion stake` (8→2)** — one-day event, and
  the price consequence (+9.85% on 08-19) is the part that matters.

### D-3 · Bucket sweep — terms passed as **separate argv**, CLI, `--mode or --days 2 --scope foreign`

| Bucket | Terms | Hits |
|---|---|---:|
| RATES/CURVE | yields · Treasury · Fed · buyback · curve | **3,083** |
| CREDIT/FIN | credit · spreads · default · bankruptcy · lending · banks | **3,253** |
| GEOPOLITICS | Iran · Hormuz · Russia · Ukraine · sanctions · tariff | **2,260** |
| GROWTH/LABOR | payrolls · unemployment · recession · GDP · consumer | 1,942 |
| AI/SEMI | semiconductor · chips · GPU · HBM · datacenter | 1,741 |
| ENERGY/OIL | oil · crude · Brent · refinery · OPEC · diesel | 1,577 |
| INFLATION | inflation · CPI · PPI · disinflation · deflation | 1,377 |

**Single-term controls, run precisely so a near-zero cannot be a mis-passed argv:**
`buyback` **557** · `Iran` **1,187** · `Hormuz` **576** · `semiconductor` **822** · `inflation` **1,350**
· `refinery` **117** · `bankruptcy` **53**.

⚠ **`bankruptcy` at 53 over two days is the lowest count on the board** and, per `T23`, is sat next to
its credit instruments rather than read alone: `HY OAS` **2.75** (12bp off the 365-day low) and `NFCI`
**−0.559** (loosest of the window). **Word count low, credit calm — consistent, and neither is a
regime claim.**

### D-4 · `theme_age` — with denominators, as `T24` requires

| Term | Tag | Age (d) | 7d avg | Accel | **n** |
|---|---|---:|---:|---:|---:|
| **`Treasury buybacks`** | 🟢 **FRESH** | **1** | 9.1 | — (no baseline) | **64** |
| `cancer vaccine` | 🟡 ACCELERATING | 80 | 11.1 | **25.71×** | **103** |
| `long-end yields` | 🟡 ACCELERATING | ≥90 | 6.7 | **11.19×** | **72** |
| `AI data center capex` | 🟡 ACCELERATING | 81 | 0.3 | 4.29× | ⚠ **10** |
| `optical interconnect` | ⚪ ECHO | ≥90 | 3.4 | 1.35× | 150 |
| `Iran sanctions` | ⚪ ECHO | ≥90 | 1.1 | 1.37× | 55 |
| `refinery outage` | ⚪ ECHO | 51 | 0.6 | 0.82× | 27 |
| `distillate crack` | 🔴 FADING | 35 | 0.0 | 0.0× | 🚨 **4** |

★★ **`Treasury buybacks` is the first 🟢FRESH this US desk has produced in TEN consecutive runs**, and
it is the positive case that **confirms `R83`'s rewritten mechanism**: 🟢FRESH was unreachable not
because the age readout is capped but because the **conjunction** (age ≤14d ∧ accel ≥2×) needs a theme
that is genuinely newborn. One was born on 08-19 and the instrument caught it on day 1.

🚫 **`distillate crack` 🔴FADING on n=4 is NOT admissible and does not contradict a price series**
(`T24`) — the distillate crack itself settled at **101.17 $/bbl = the 98.8th percentile of 250
sessions**. `M733` reproduces exactly.
⚠ **`AI data center capex` at n=10** is likewise below the `T24` floor; the 4.29× is not cited as a
reading.

### D-5 · Blind-spot pass — `blindspot --scope foreign`, sample read raw

Denominator **2,312** articles, 30-day baseline, market-relevance ≥40%, universe 665 companies,
`field=title`.

- **Real, multi-outlet surges**: `WALMART` z **5.5** (39 art / **12 outlets**) · `REGN` z 7.5 and
  `REGENERON` z 4.9 (both 100% market) · `MELLON` z 7.3 · `CONOCOPHILLIPS` z 4.0 (100% market) ·
  `HBM` z 4.3 (⚠ **1 outlet, dispersion 0.00** — not a reading).
- **Rejected as single-source artifacts** (dispersion 0.00, 1 outlet): `PURPOSE` z 15.8 · `FILERS`
  z 13.7 · `EXITED` z 8.1 · `CAD` z 4.8. These are **13F filing-season boilerplate**, and the highest
  z-scores on the board are all in this class — a standing caution about reading the z column alone.
- **Never-before-seen tokens**: `BACKFIRE` (4 outlets) — which resolves to *"Treasury Bond Fix Could
  Backfire, Warns JPMorgan"*, i.e. **the vocabulary-free instrument independently surfaced the
  counter-argument to the day's main event** · `DRUCKENMILLER` · `MASAYOSHI` · `PARABOLIC` · `SKIDS`.
- ⚠ `burst --scope foreign` **returned no rows** (exit 0, empty). Logged in §I; `blindspot` covered
  the same job.

**New terms folded into the living table:** `Treasury buybacks` · `long-end yields` · `cancer vaccine`.

---

## §E · Propositions — falsifiable, both directions, mandatory anti-signal

★ **ID check at WRITE time**: `grep -E "\bP(77|78|79|80)\b"` across `handoff/*.md`,
`llm_outputs/2026-08-*/industry_US/*.md` returned **0**; highest existing is **P76** (2026-08-19).
(The one `P99` hit in `STANDING_VIEW_US.md:330` is the string "99th percentile", not an ID.)

### E-0 · 🚨 Two live rows are at VOID and this stage rules on the CLAUSE, before seeing the branch

**`S102` — VOID, recommended.** Its anti-signal reads *"an **intermeeting Fed policy action** or a
**Treasury refunding announcement** inside the window."* On **2026-08-19**, inside the window, Treasury
announced a **doubling of long-dated buyback operations** and the tape moved on it by name
(*"Bond Yields Dive After Treasury Increases Buybacks"*, *"Treasury Yields Fall, Gold Jumps On Bessent
Buyback Plan"*).
- **The clause's LETTER is arguable**: a buyback-size increase is not the quarterly refunding
  announcement.
- **The clause's INTENT is met without ambiguity**: the clause exists so that a yield move caused by
  Treasury cannot be scored as caused by the minutes, and that is exactly what happened.
⇒ **Recommend VOID, do not improvise a replacement threshold on the existing row** (the HANDOVER rule:
an ambiguous observable is a finding about the row's construction). `P77` below is the successor.
🚨 **And the pattern is the point**: `S102` was registered on 08-19 **as the repair for `P73`, which
self-voided on the same clause**. The repair inherited the defect. **New dig `D296`.**

**`P74` — VOID risk on its OWN anti-signal, and its substantive branch is refuted anyway.**
Its anti-signal: *"if `SPY`'s own 5-session return is within ±0.5% over the settle window, the beta
channel is too small ⇒ VOID."* Measured on the settled 08-12→08-19 window: **`SPY` −0.444%, inside
±0.5%.** Separately, its **direction A is refuted on today's numbers**: raw signs are **4-0 positive**
and β-adjusted signs are **also 4-0 positive** (§C-1) — i.e. raw and adjusted **agree**, which is
`P74`'s direction B, *"the unadjusted sign test was adequate and this proposition is wrong."*
⇒ **Recorded as a pre-settle self-refutation** (§H); the formal settle remains 08-21 and the row is
not withdrawn.

**`S98` — VOID risk, flagged in HANDOVER §2(b) and repeated here so MACRO owns it.** Its clause names
*"an FOMC-dated communication … inside the window"*; the **FOMC minutes released 2026-08-19** are
inside 08-13→08-20. **MACRO's ruling: the clause fires and `S98` should be VOID, not scored** — and
this is written while its pre-settle reading (all four legs positive, §C-1) points at the branch that
would retire a four-sector tilt.

---

### P77 — ★★★ Can Treasury cap the long end? The window's actual macro binary, bracketed both ways

**Claim.** The 08-19 buyback expansion is an attempt to hold `DGS30` down from **5.28, within 3bp of a
252-observation high (5.31)**. Two named institutional voices are already on the other side
(`JPMorgan`: *"credibility risk"*, *"could backfire"* — 4 outlets each). **The proposition is that this
is testable on the long end alone within one week, and that the equity market's answer is already
visible and is NOT the duration complex** (§C-1).

- **Direction A (the cap holds):** `DGS30` at the first `[FRED]` close covering **2026-08-26** is
  **≤ 5.18** (−10bp from 5.28) ⇒ a debt-management action moved the long end, term-premium arguments
  need a policy variable in them, and any UW justified by "the long end is repricing" is on borrowed
  time.
- **Direction B (the cap fails):** `DGS30` **≥ 5.38** (+10bp) ⇒ the JPMorgan credibility-risk read is
  right, the intervention made it worse, and the real-yield repricing of §A-1 is intact and
  accelerating.
- **Between (5.18 – 5.38) = C, and C is the favourite — disclosed at registration.**
- ★ **`D93` executed BEFORE freezing**: `DGS30`'s own **5-observation change**, trailing 252
  observations — **mean +0.8bp · sd 7.4bp · p10 −8.0bp · p50 +1.0bp · p90 +10.0bp.** The ±10bp bands
  are **≈p10 / ≈p90 ⇒ A ≈10% · B ≈10% · C ≈80%.** Stated up front, not discovered at scoring.
- **State at registration:** `DGS30` **5.28** (08-18, **pre**-announcement). The 08-19 print is not yet
  in `[FRED]`.
- 🚨 **Mandatory anti-signal (VOID):** an **FOMC intermeeting action**, a **quarterly refunding
  announcement**, or a **Treasury buyback schedule change** inside the window ⇒ the observable is no
  longer measuring whether *this* action worked. ⚠ Reachability-checked: the next scheduled quarterly
  refunding is outside a one-week window, and no FOMC meeting falls inside it.
- **Thread/velocity:** `theme_age "Treasury buybacks"` **🟢FRESH, age 1, n=64**; `long-end yields`
  **🟡ACCELERATING 11.19×, n=72**. Both denominators clear `T24`.
- **Owner:** `industry_US`. **Settles 2026-08-26.**

### P78 — ★★★ The "duration complex" is a DISPERSION question, and the desk has been asking it with a sign

**Claim.** Four of this desk's brackets (`S80`, `S82`, `S98`, and `P74`) test whether
{`XLU`,`XLRE`,`XLP`,`XLV`} are one factor **by comparing signs**. Today all four share a sign — and the
magnitudes run **`XLU` +0.855 to `XLV` +4.742**, a **3.9pp spread**, with the two extremes driven by
**a pharma trial result** and **a regulated-utility flow reading that is the worst on the board**
(`eqflow` −0.545, 8 red of 15). **A 4-0 sign agreement across a 3.9pp range is not evidence of one
factor, and a test that cannot tell those two states apart is the wrong instrument.**

- **Observable:** the **cross-sectional range (max − min) of the 5-session excess vs `SPY`** across
  {`XLU`,`XLRE`,`XLP`,`XLV`}, at the **2026-08-26** settled close.
- **Direction A (four objects, not one):** range **≥ 4.71pp** ⇒ the complex disperses; sign-based rows
  are measuring `SPY`'s direction, not a factor, and `S82`'s med-tech branch is the correct reading.
- **Direction B (one object):** range **≤ 1.69pp** ⇒ the four really do move together and the sign
  tests were adequate.
- **Between = C.**
- ★ **`D93` executed BEFORE freezing**: the estimator's own trailing **252** observations —
  **mean 3.195 · sd 1.473 · p15 1.688 · p50 3.129 · p85 4.707 · p95 5.772.** Bands set at **p85 / p15**
  ⇒ **A ≈15% · B ≈15% · C ≈70%.** ⚠ **The estimator's centre is 3.195, not zero** — a range is
  non-negative by construction, so a symmetric-around-zero band would be meaningless. Disclosed.
- **State at registration:** **3.888 = the 73.4th percentile** ⇒ inside C, **leaning A**. Disclosed at
  registration rather than discovered at scoring.
- 🚨 **Mandatory anti-signal (VOID):** a **single-name event worth >2% of any one ETF** inside the
  window (an `XLV` constituent trial result of `MRK`'s size would manufacture branch A by itself) ⇒
  the range is a name event, not a factor reading. ⚠ **This anti-signal is ALREADY live in the
  registration window** — `MRK` +12.60% on 08-19 at ~5% of `XLV` — which is why the row is registered
  forward to 08-26 rather than scored on today's number.
- **Information content (L3): HIGH.** A retires the instrument four rows share; B validates it.
- **Owner:** `industry_US`. **Settles 2026-08-26.**

### P79 — ★★★ The AI-compute drawdown: mean-reversion, or the start of a de-rate?

**Claim.** `EW{AVGO, ANET, HPE, COHR, LITE}` 5-session excess vs `SPY` is **−12.425pp = the 0.8th
percentile of two years**, and **all five are held in the real book** (`T22`). Two readings are
available and the desk currently has **no** registered row that separates them: (i) a positioning
flush — `Nasdaq-100` spec net is at the **0th percentile short** `[COT, as of 2026-08-11]`, which is
rebound ammunition; (ii) the first leg of a capex de-rate — *"Big Tech on pace to spend $735bn on AI
data centers in 2026"* sits in the same head tier as `Alibaba Posts Weaker Earnings Amid Heavy AI
Investments`.

- **Direction A (flush, reverts):** at the **2026-08-26** settle the same EW basket's 5-session excess
  is **≥ +8.02pp** (its own 252d p85) ⇒ a 0.8th-percentile reading was a positioning event.
- **Direction B (de-rate begins):** the excess is **≤ −7.72pp** (its own 252d **p05**) a second time ⇒
  two consecutive p05 weeks is not noise and the theme's multiple is being reset.
- **Between = C, the disclosed favourite.**
- ★ **`D93` executed BEFORE freezing**: trailing **252** observations — **mean +1.959 · sd 5.930 ·
  p05 −7.715 · p15 −3.616 · p50 +1.790 · p85 +8.022 · p95 +11.593.** ⇒ **A ≈15% · B ≈5% · C ≈80%.**
  ⚠ **The bands are deliberately asymmetric** because the distribution is: B is the rarer event and is
  the one that would change a conclusion.
- **State at registration:** **−12.425 = 0.8th percentile.**
- 🚨 **Mandatory anti-signal (VOID):** **`NVDA`'s 2026-08-26 earnings falls inside any settle window
  that ends on or after 08-26** ⇒ the basket would be scored on an event, not on carry. **This row is
  therefore registered to settle at the 2026-08-25 close, one session BEFORE the print**, and says so
  here rather than discovering the collision at scoring. ⚠ `S79`/`S81`/`S103` already own the print
  itself; this row deliberately does not.
- ⚠ **`W3`**: this measures whether a drawdown reverts, **not** whether the position was right. No
  sizing, no recommendation (P4).
- **Owner:** `industry_US`. **Settles 2026-08-25 (pre-print, by construction).**

### P80 — ★★ The refiners' registered kill has RESET, and the carry says otherwise

**Claim.** The carried thesis line (`STANDING_VIEW_US §3a`, 08-19) reads: *"kill = a **second
consecutive** crack-rate decline (**one has fired**)."* **Measured on settled bars through 08-19, the
most recent two 5-session crack rates are BOTH POSITIVE**: `[+2.36, +7.88, −14.45, +5.00, −1.24]`
(most recent first, 3-2-1 crack in $/bbl). ⇒ **the kill condition did not advance; it reset.** The
carry's parenthetical is stale and this report corrects it rather than repeating it.

Levels, settled 08-19: **Brent 91.62 · WTI 85.83 · 3-2-1 crack 67.64 = 95.6th percentile of 250
sessions · distillate crack 101.17 = 98.8th percentile.** `EW{MPC,VLO,PSX}` exc5 **+5.730 = 79.8th
percentile** of its own 252 observations.

- **Direction A (margin, and the L2 trap is loading):** at the **2026-08-26** settle the 3-2-1 crack is
  **≥ 65** *and* `EW{MPC,VLO,PSX}` exc5 is **≥ +0.86** (its own 252d median) ⇒ the capacity thesis is
  paying and the **peak-margin lens `L2` becomes the binding constraint, not the barrel** — a crack at
  the 95.6th percentile is not yet in any reported margin series, which is precisely how that trap gets
  built one to three quarters out.
- **Direction B (it was the barrel):** the crack is **≤ 58** *and* the EW excess **≤ −3.74** (252d p15)
  ⇒ the advance was crude, and Brent at 91.62 with `WTI` spec at the **18th percentile** did the work.
- **Between = C.**
- ★ **`D93`**: `EW{MPC,VLO,PSX}` exc5 trailing 252 — **p15 −3.740 · p50 +0.861 · p85 +6.927 ·
  p95 +10.846.** Crack bands are set on the 250-session range **19.65 – 72.22** (current 67.64).
- 🚨 **Mandatory anti-signal (VOID):** an **issuer event** at any of the three (guidance, unplanned
  outage, M&A) or a **PADD3 hurricane landfall** inside the window. ⚠ Reachability-checked:
  `theme_age "refinery outage"` reads **⚪ECHO 0.82× on n=27** and `refinery` returns **117** articles
  over two days — no outage story is carrying. ⚠ **`Ukraine Says It Hit Russia's Taneco Refinery`
  (3 outlets, 08-19/20) is a NON-US refinery strike** — it supports the capacity mechanism and does
  **not** fire the anti-signal, and saying so now prevents it being used as an escape hatch later.
- **Owner:** `industry_US`. **Settles 2026-08-26.**

---

## §F · Self-backtest — one settled score, and it flipped from yesterday's pre-settle

| ID | Claim | Registered KPI | Settle | **Observed (settled 08-19)** | Verdict |
|---|---|---|---|---|---|
| **`P52`** (08-13) | The in-line print sent money to **growth**, not defensives | A is REFUTED iff `XLK` exc5 **≤0** **∧** `XLU` exc5 **>0** | **2026-08-19 — DUE** | `XLK` exc5 **−2.320** ✅ · `XLU` exc5 **+0.855** ✅ | ★ **A IS REFUTED — the conjunction holds.** Money went to **defensives, not growth**. ⚠ **This flipped**: the 08-19 run's pre-settle had `XLK` at **+0.151** ❌ and read the conjunction as failing. One session moved it by 2.47pp |
| `P65` (08-16) | Long end is a **bull** steepener; `DGS2` **not pinned** | `30y−10y` ≥0.58 **∧** `DGS2` ≤4.15 | 08-21 | `30y−10y` **0.570** ❌ · `DGS2` **4.190** ❌ | **BOTH legs now fail** (was half-broken). §A-2 shows why: the spread is **below** its own 252d median while the 30y level is near a high |
| `P66` (08-16) | The distillate bid has a **physical** driver | `HO=F−CL=F` 20d gap + a further dated strike | 08-21 | crack **101.17 = 98.8th %ile**; `Ukraine hit Russia's Taneco Refinery` (3 outlets, 08-19/20) | ★ **HIT-tracking on both legs.** The dated strike arrived |
| `P67` (08-16) | AI capex bill migrating to debt; credit does not see it | `HY OAS` ≥2.85% at first close covering 08-28 | 08-28 | `HY OAS` **2.750**, +6bp/20obs, 12bp off the 365d low | **CARRIED, branch B tracking.** Still **narrative-only** — and now with an AI drawdown at the 0.8th percentile that credit still does not price (§C-3, §A-3) |
| `P69` (08-17) | Does a Hormuz shutdown reprice crude at all? | `BZ=F` at 08-21: A ≥93.00 · B ≤86.50 | 08-21 | **`BZ=F` 91.62** (was 91.02) | **C**, still moving **toward A**. ⚠ `Trump vows 'economic warfare'` thread at 14 outlets is the live driver |
| `P70` (08-17) | Refiners pay **without** the barrel | EW exc5 ≥+2.0 **∧** `BZ=F` 5d ≤+2.0% | 08-21 | EW **+5.730** ✅ · `BZ=F` 5d **+0.66%** ✅ | ★★ **BOTH legs now pass** — the control leg that blocked it by 0.37pp on 08-18 has cleared. Not scored (settle 08-21), but the blockage is gone |
| `P75` (08-19) | The refining leg is decided by 0.37pp on its control | crack ≥95 **∧** EW exc5 ≥+2.0 (A) | 08-21 | **3-2-1 crack 67.64** ❌ · distillate **101.17** ✅ · EW **+5.730** ✅ | ⚠ **AMBIGUOUS AS WRITTEN — a construction defect, recorded not resolved.** The row says *"the crack"* and its supporting text uses the **distillate** crack (88.41→101.96). On the **3-2-1** crack the A-leg fails (67.64 < 95); on the **distillate** crack it passes (101.17 ≥ 95). **The scorer must be told which series, and the row does not say.** `P80` replaces it with both series named |
| `P73` (08-19) | Which tenor carries the FOMC minutes | — | — | — | **VOID at registration** (Warsh leg). Successor `S102` is **also VOID** — §E-0 |
| `P74` (08-19) | Beta, not the rate, decides `S80`/`S98` | raw signs agree **∧** β-adj signs split ⇒ A | 08-21 | raw **4-0 positive** · β-adj **4-0 positive** ⇒ **they AGREE** | ★ **Direction B — i.e. `P74` is WRONG on today's data.** ⚠ **And its own anti-signal fires**: `SPY` 5-session **−0.444%**, inside the ±0.5% VOID band. Recorded in §H |
| `P76` (08-19) | A new BUILDING robotics cycle the registry does not carry | ≥5 outlets on ≥3 days by 09-02 **∧** a `us_top300` supplier named | 09-02 | Unitree thread now **FADING 2→5→17→2** | **CARRIED**, tracking **toward B**. ⚠ The final `2` is on a 42%-volume partial day — **not scored on it** |

**Running hit-rate this run: 1 scored (`P52`, A REFUTED) · 0 MISS · 5 CARRIED · 2 VOID
(`P73` inherited, `P74` on its own anti-signal) · 1 construction defect (`P75`) · 1 correction issued
to the carry (`P80` / the refiners' reset kill).**
★ **The one row that settled flipped between the pre-settle and the settle**, which is the whole
argument for not scoring on an unsettled bar.

---

## §G · ★ SECTOR TRANSMISSION MATRIX — wind direction only, all 11 GICS

> ROTATION's input. **Not** a ranking of research effort, **not** a position. Driving proposition ID in
> the last column. `eqflow` is used in preference to `wflow` throughout (36-day-old cap weights, `G5`).

| # | GICS sector | Wind | Why, in one line (settled 08-19) | Driver |
|---|---|---|---|---|
| 1 | **Health Care** | **OW** | **#1 on both axes** — `eqflow` **+0.252** (rank 1) and exc5 **+4.742** (rank 1); the move is **broad ex-`MRK`** (+2.09% EW on 08-19) and **business-model ordered** (pharma/tools lead, managed care lags), i.e. idiosyncratic, not duration | `P78` · `S82` |
| 2 | **Energy** | **OW** | `eqflow` **+0.182** (rank 2), exc5 **+4.622** (rank 2), `EW{MPC,VLO,PSX}` exc5 **+5.730 = 79.8th %ile**, distillate crack at the **98.8th percentile**, and `P70`'s blocking control leg has **cleared**. ⚠ Carries the desk's only 🔴 FINRA name (`NUE` is MATR) and a **crowded-short WTI** (18th %ile) | `P80` · `P69` · `S88` |
| 3 | **Consumer Staples** | **N** | ⚠ **`R82` reverted the 08-19 promotion** and this run does not re-make it: `eqflow` **−0.012** against exc5 **+2.160** — price without flow. `WMT` printed **08-20 pre-market** (weakest sales growth in years, 12 outlets) and its price lands **outside this frame** | `S100` |
| 4 | **Communication Services** | **N** | `eqflow` **+0.023** vs `wflow` −0.262 — the gap is `GOOGL` at **38.3%** cap weight. `GOOGL` exc5 **+0.79** and is 0.08% below its own 344.48 trigger; `T` (held, 9.74% of invested) exc5 **+4.03** with **no thesis object** | HANDOVER §1 |
| 5 | **Consumer Discretionary** | **N** | `eqflow` **+0.022**, exc5 **+1.038**, β **1.178** — the excess is beta, not selection. Δ **+0.145** is the board's 2nd largest but `D293` bars a Δ-only verdict | — |
| 6 | **Materials** | **N−** | 🚩 **`wflow` sign is `LIN`-owned (`G3`) and may not be used.** On the admissible axes: `eqflow` **−0.064**, exc5 **+0.330**, **0 green / 4 red**. ★ **`S77`'s residual is two steel names** (`STLD` −11.78, `NUE` −8.04) and `NUE` is held | `S77` handoff |
| 7 | **Financials** | **N−** | `eqflow` **−0.127** (below `wflow` −0.009 ⇒ **cap-weighted is the better half**, the inverse of the breadth story this desk carried in July), exc5 **−0.316**, 2🟢/8🔴. `PRU`'s ledger leg ("FIN returns to OW") **does not fire** | HANDOVER §3 |
| 8 | **Industrials** | **UW−** | `eqflow` **−0.073**, exc5 **−1.670**, **10 red of 50**, zero green. ⚠ **The desk's position here is defense** (`RTX` held, `LMT`/`NOC`/`GD` carried), and `RTX` exc5 is **−0.64** — the label's weakness is not the sub-node's | `S97` · `S99` |
| 9 | **Information Technology** | **UW** | **Worst on both axes**: `eqflow` **−0.197**, exc5 **−2.320**, **19 red of 56**. §C-3: the AI-compute basket is at the **0.8th percentile of 2 years** and the desk holds all five names. ⚠ **`Nasdaq-100` spec is 0th-percentile short** — rebound ammunition, `[COT as of 2026-08-11]` | **`P79`** |
| 10 | **Real Estate** | **UW** | `eqflow` **−0.252**, 0🟢/4🔴, against exc5 **+1.568** — price up, flow last-but-one. The same price-vs-flow contradiction as Utilities, one rank milder | `P78` · `S98` |
| 11 | **Utilities** | **UW** | **Worst flow on the board by a distance**: `eqflow` **−0.545**, `ex_top1` **−0.578**, **8 red of 15, zero green** — against exc5 **+0.855**. ★ **This single row is the strongest evidence for `P78`**: the purest duration leg is the *weakest* of the four in a window the duration story says it should have led | **`P78`** |

**Wind summary: OW ×2 (HLTH, ENRG) · N ×3 · N− ×2 · UW− ×1 · UW ×3.**
⚠ **The two OW sectors are the two the tape and the flow agree on, and neither is a rate story** — one
is a drug trial and one is a refining margin. **The desk's four duration-labelled brackets are aimed at
the part of the board where price and flow disagree, not at where the money went.**

---

## §H · §4c — claims this stage asserted and then refuted, in this run

1. ★ **`P74`, registered by this desk 24 hours ago, is refuted by this desk's own measurement today.**
   It claimed the β-correction, not the rate, decides `S80`/`S98`, and that raw and β-adjusted signs
   would split. Measured: **raw 4-0 positive, β-adjusted 4-0 positive — they agree.** Its own
   anti-signal also fires (`SPY` −0.444%, inside ±0.5%). **Not edited away; `P78` is the successor and
   it changes the instrument from a sign to a dispersion.**
2. ★ **The carry's refiner kill-clause is corrected, not repeated.** `STANDING_VIEW_US §3a` says
   *"a second consecutive crack-rate decline (one has fired)"*. The settled series reads **+2.36,
   +7.88** as its two most recent 5-session rates ⇒ **the counter reset**. Had this report repeated the
   parenthetical it would have carried a kill that is one step from firing when it is two.
3. ★ **`P75`'s A-leg is ambiguous as written** — *"the crack ≥ 95"* passes on the distillate crack
   (101.17) and fails on the 3-2-1 crack (67.64), and the row does not name which. **Found by
   attempting to score it, not by re-reading it.** `P80` names both series explicitly.
4. **A first draft of §A read the 08-20 futures row** (Brent 93.86, 3-2-1 crack 57.93) **as a settled
   observation.** It is a **live, incomplete bar** at 09:xx ET and `G0` revokes it. Every oil number in
   this report was recomputed on `index <= 2026-08-19`. Recorded because the un-recomputed version
   would have shown the crack **collapsing 11.9 $/bbl in a session** — the opposite of §C's finding.

⚠ **Zero self-refutations would have been the suspicious outcome here**, given that three of this
run's four propositions were built by attacking rows this desk wrote yesterday.

---

## §I · Failed or empty lookups this run

| Call | Result | Handling |
|---|---|---|
| `module_news_data burst --scope foreign` | **exit 0, zero rows** (also timed out once at 120 s and was re-run in background) | `blindspot --scope foreign` covers the same job and **did** return; the vocabulary-free finding (`BACKFIRE`) came from it |
| `brief … --json` → stdout | Writes a **summary** to stdout and the payload to `out/news_brief/2026-08-20_foreign.json` | Read from the file; not an error, documented so the next run does not re-derive it |
| `module_macro_us --json` piped to a file | The first line is a **`[macro_us] fredapi not installed`** notice on **stdout**, which breaks `json.load` | Worked around by parsing the file that separates streams; **logged as an instrument defect, not repaired** (rule 1) |
| `module_KIS.fetch_overseas_balance()` | Raised `KisError` until `.env` was loaded into the process env | Loaded without printing any value; **no secret appears in any output** |
| COT refresh | **No new observation for the 6th consecutive run** — data as of **2026-08-11** | §B; no proposition anchored on it |

---

## ✅ EXIT CHECK — self-audit

- ✅ Catalysts injected (`catalyst_calendar --days 10`, HANDOVER §6): **no binary ≤48h**; nearest
  **`NVDA` 08-26 (D-6)** and **July PCE 08-28 (D-8, un-bracketed — handed to PREMORTEM)**.
  ⚠ `--days 10` was used, not the default 5, because ARMED rows sit at 08-21/08-24/08-26.
- ✅ Events read with **`--body 2`**, `tail = 0`; **and the three recovery tiers are quoted with their
  withheld counts** (`single_source` 15 shown of **362** ⇒ **347 withheld**; `excluded_nonmarket` 0 of
  0 **with the reason** — the classifier is Korean-only; `subevents_recovered` **42**).
- ✅ **The denominator is quoted as UNCORRECTED and said so** (`excluded_not_news` = `{}`).
- ✅ Trajectories read; every proposition carries a thread tag + curve or states its absence; the
  **partial-final-day artifact is applied to every FADING tag** and no FADING tag is cited as evidence.
- ✅ No "quiet"/"nothing happened" claim anywhere (barred by `G1` and unsupported by the denominators).
- ✅ Bucket terms passed as **separate argv**, with **7 single-term controls** run against a mis-passed
  CLI.
- ✅ Both halves cited on the headline print: `DGS10` **+0.140/60obs** *with* `DFII10` **+0.230** and
  `T10YIE` **−0.100**; `DGS2` **−0.070/20obs** *against* `DGS30` **+0.150/20obs**.
- ✅ Every relative-performance number names `SPY` inline; **no statistical result carried across
  markets** — §C-4 explicitly refuses `D290-KR`'s conclusion (`W1`).
- ✅ Credit axis cited (`HY OAS` 2.750, `IG OAS` 0.820, `NFCI` −0.559); the AI drawdown is labelled
  **not a credit event**.
- ✅ `real_10y` quoted with `breakeven_10y` (§A-1).
- ✅ Transmission matrix: **all 11 sectors, one line each**, with driver IDs.
- ✅ Self-backtest appended with a running hit-rate; new blind-spot terms folded into the term table.
- ⏳ `report_lint.py` run on this file — findings in the appended lint note.

> Analytical output only. No buy/sell recommendation, no position size, no order (P4).

---

## Lint note

`python -X utf8 scripts/report_lint.py llm_outputs/2026-08-20/industry_US/MACRO_REPORT.md`
→ **0 findings** across rules **C1 · C2 · S6 · D6**. No exemption was required and none is claimed.

⚠ **A clean lint run is not a correct report.** The linter checks form only — that a relative number
names its benchmark, that a headline print carries both halves, that a future label is tagged, that
OBV is not cited alone. It cannot see that `P74` was refuted (§H), that `P75` is ambiguous as written
(§F), or that the COT block is nine days old (§B). Those are content findings and they were produced
by measurement, not by the linter.

---

# §5 · ADDENDUM — DRIFT WATCH (append-only; nothing above is rewritten)

*(Stage 8 / L1·DRIFT ★US-only. Written **KST 2026-08-20 23:4x = ET 10:4x**, i.e. **+0.9h** after this
report completed at 22:50 KST and **~1.3h after the US cash open**. Nothing above this line has been
edited — the original call stays visible next to its correction, which is what the self-backtest
eats.)*

## 1 · The instrument result, and its window is SHORT

`scripts/drift_watch.py --report llm_outputs/2026-08-20/industry_US/MACRO_REPORT.md`
→ **✅ no kill-switch term burst. No report-staleness signal.**

⚠ **The monitored window is 0.7h, not the protocol's 3–6h**, because this run completed late in the
KST evening. **A 0.7-hour absence is a short-window absence and is NOT claimed as an overnight
all-clear** — the same caveat the 08-19 run had to write at 1.6h, now for a second consecutive run.
⚠ It is also **the second consecutive run whose DRIFT window is truncated by the run's own length**,
which is a scheduling fact rather than a market one and is recorded as such.

## 2 · The report's own anti-signals, checked by hand rather than by term count (`T23`)

The automatic pass counts words. Each of this report's registered VOID clauses was checked directly:

| Anti-signal | Probe | Result |
|---|---|---|
| **A Treasury refunding announcement** (`P77`, `S104`, `S102`) | `fts search refunding Treasury --mode and --days 1 --scope foreign` → **23 matches, body-read** | ❌ **NOT fired.** The day's `refunding` volume (137 hits) is **tax refunds / refundable credits**, not debt operations — `cnbc` *"Treasury, IRS move to restrict refundable tax credits"*, `bloomberg` *"Treasury Seeks to Limit Immigrants' Use of Some Tax Breaks"*. The only debt-management item is the **same 08-19 buyback expansion already in §D-1** (`fxstreet`/OCBC: *"The Treasury will increase the size of its longer-dated buyback operations"*). **No NEW Treasury action since the report** |
| **An intermeeting Fed action** (`P77`, `S104`) | `fts search intermeeting --days 1` → **1 match** | ❌ **NOT fired** |
| **A PADD3 hurricane landfall / US refiner issuer event** (`P80`) | `fts search hurricane --days 1` → **10 matches, all body-read**; `fts search Marathon Phillips Valero --mode or --days 1` | ❌ **NOT fired.** Every `hurricane` hit is real-estate or travel boilerplate referencing **Hurricane Andrew (1992)**. The refiner hits are third-party commentary (`oilprice` *"5 Energy Stocks Cashing In On The New Energy Crunch"*, `nasdaq` *"Bull of the Day: Valero"*) — **analyst opinion, not issuer events**, exactly as `P75`'s reachability note pre-declared |
| **A single-name event worth >2% of any one ETF** (`P78`) | the intraday tape, §3 | ⚠ **PARTIALLY LIVE — see §3.** `WMT` is ~1.5% of `XLP` and moved −9.25% intraday; that is ~0.14pp of `XLP`, **below** the clause's bar. The clause is **not** fired, and the arithmetic is shown rather than asserted |

⚠ **`T23` compliance**: the one term with an elevated count (`refunding`, 137) was **body-read** and
sat next to its credit instruments — `HY OAS` **2.750** (12bp off the 365-day low), `NFCI` **−0.559**
(loosest of the 120-day window). **Word count up, credit unchanged.** Same shape as 08-19's
`bankruptcy` flag, and it resolves the same way.

## 3 · ⚠ INTRADAY tape, explicitly labelled — two live brackets moved after the report closed

🚫 **`G0` bars every number below from being compared with the sweep or with any settled statistic in
this report.** These are **live, incomplete 08-20 bars at ~10:4x ET**, quoted only to answer DRIFT's
question — *does the report lie now?*

| | 08-19 settled | **live 08-20** | intraday % |
|---|---:|---:|---:|
| `SPY` | 769.06 | 766.41 | −0.34% |
| **`BZ=F` Brent** | **91.62** | **93.31** | **+1.84%** |
| `XLE` | 63.58 | 64.52 | +1.48% |
| `MPC` · `PSX` | 360.75 · 242.29 | 365.07 · 245.74 | +1.20% · +1.43% |
| **`WMT`** | 114.30 | **103.73** | **−9.25%** |
| `MRK` | 152.20 | 150.60 | −1.05% |
| `LITE` · `COHR` | 827.60 · 287.47 | 855.10 · 285.00 | **+3.32%** · −0.86% |
| `MRVL` · `AVGO` | 237.27 · 362.48 | 243.09 · 365.91 | +2.45% · +0.95% |
| `NVDA` · `XLK` · `XLU` · `XLV` | — | — | +0.06% · +0.07% · +0.16% · −0.90% |

### 3a · ★ `P69` / `S95`: Brent has touched branch A intraday

`P69`'s branch A is **`BZ=F` ≥ 93.00 at the 08-21 settle**; §F recorded it at **91.62 settled,
"moving toward A"**. **It is 93.31 intraday.** ⇒ **The report's own reading is not stale — it is
being confirmed faster than the report expected.** 🚫 **This is NOT a score**: the observable is a
**settled** close on 08-21, and an intraday touch of a threshold is not a settle. Recorded so the
D+1 scorer sees the trajectory rather than discovering it.

### 3b · ★★ `WMT` −9.25% — the decision to keep it outside the frame is vindicated, and the cost is stated

ROTATION §2c **declined a Staples demote** on the ground that *"the print's price consequence is
OUTSIDE the settled frame (`G0`)… a demote on a print the frame cannot see is the `R82` error in the
other direction."* **The print then moved the stock −9.25%.**

**Both halves, because one alone would be self-congratulation:**
- ✅ **The rule was right**: a settled-frame desk cannot price an unsettled bar, and inventing a
  verdict from a headline is exactly what `R82` punished.
- ⚠ **And the rule has a cost, now measured**: the desk's Staples verdict is **`N` on a sector whose
  28.9%-weight name fell 9.25% the same morning**, and it will stay `N` until tomorrow's run. **A
  frame that refuses unsettled data is right about evidence and slow about reality**, and that
  trade-off is a property of the design, not a defect to be argued away.
- ★ **The bracket already covers it**: **`S100` equal-weights `WMT` and `TGT` and settles 08-21**, so
  the event is scored by a pre-registered row rather than by a same-day reaction (`D28`).
  ⚠ **`TGT` is +0.12% intraday against `WMT` −9.25%**, so `S100`'s equal-weighted observable is being
  driven almost entirely by one leg — **disclosed now, before the settle.**

### 3c · The optical node's two names disagree again, intraday

`LITE` **+3.32%** against `COHR` **−0.86%** — the same split `SECTOR_DEEP_IT §3` measured on settled
data, where the separating evidence is **price and relative strength first** (`LITE` exc5 −10.80 with
rs60 −15.7 against `COHR` exc5 **−18.72** with rs60 **−27.0**, the board's worst) and the OBV reading
(`LITE` 매집 · `COHR` 중립) is the **third and weakest** corroborant. ⚠ **RULE D6 applied, not
exempted — OBV does not carry this observation alone.** **`S96` settles 08-21 and this does not
change its reading**; it is recorded because a node this desk promoted to a 5th DEEP is dispersing
rather than moving together, for a second consecutive session.

## 4 · What changes in the report above — **nothing, and that is the finding**

- **No proposition is amended.** `P77` `P78` `P79` `P80` and `S104`–`S107` all retain their frozen
  observables and thresholds. **No threshold was moved after the fact** — the rule that a bracket
  whose threshold moves after the print is a description wearing a forecast's clothes.
- **No verdict is amended.** The transmission matrix, the DEEP set and every §B tag stand.
- **Two trajectory notes are added** (§3a Brent toward `P69` A; §3b `S100`'s single-leg dominance),
  and both are stated as **trajectories, not scores.**

## 5 · Honest limits of this check

1. **0.7h, not 3–6h.** Second consecutive truncated window.
2. **The intraday tape is one snapshot at ~10:4x ET**, not a session. Nothing in §3 survives the close
   as evidence, and the D+1 run must re-read all of it from settled bars.
3. **`drift_watch` counts terms against a 30-day baseline**, so — per `M713` — **a continuing story
   cannot burst.** The Iran/Hormuz thread and the Treasury buyback thread are both *continuing*, which
   means the ✅ in §1 **cannot** be read as evidence that neither moved. §2's hand-checks exist
   precisely because the automatic pass is blind to that class.
4. **The `refunding` count (137) is dominated by an unrelated tax story**, and only the body-read
   separated them. **A term-count DRIFT pass would have flagged this run and been wrong.**
