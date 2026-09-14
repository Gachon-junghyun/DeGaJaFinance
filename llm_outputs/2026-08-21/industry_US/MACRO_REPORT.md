# MACRO_REPORT — industry_US · 2026-08-21 (Fri) · Stage 3 / L1·MACRO

> Wind direction only. **No position, no size, no buy/sell language (P4).** `--scope foreign` on every
> news call. Run clock **KST 22:2x–23:2x = ET 09:2x–10:2x, US cash pre-market** (bell 22:30 KST).
> Terminal settled equity bar **2026-08-20**. `[FRED]` yields terminate **2026-08-19** — one session
> behind the tape, and today that gap is load-bearing (§A-0).

## ★★★ The one thing this report exists to say today

🚨 **The window's largest dated macro binary is happening during this run's own session, and
`catalyst_calendar` carries zero rows for it: the new Fed chair, Kevin Warsh, makes his Jackson Hole
debut TODAY, 2026-08-21.** `scmp` 08-21 lists it as the day's item (*"Wang Yi visits South Korea,
China's economy cools, **Warsh speaks at Jackson Hole**"*); `investing_en` 08-21 frames the week as
*"**Nvidia earnings, Jackson Hole to test pillars of stock rally**"*; `Barron's` 08-20:
*"Jackson Hole Meeting Gives Fed's Kevin Warsh a Chance to Quell Market Fears."*
`theme_age "Jackson Hole"` = **🟡ACCELERATING 7.0× on n=134**; the bare term `Warsh` returns **132**
articles over two days.

⇒ **This run's own HANDOVER §6 wrote *"No binary lands ≤48h from this run"* on the strength of
`catalyst_calendar --days 10`, and this stage's news pass refutes it.** The sentence is **left in
place and corrected here, not edited** (`§4c`/`D48`). **The protocol's mandatory both-sides bracket
rule DOES trigger today**, and `P82` below is that bracket. This is **`D18`/`D288-KR`'s Nth
reproduction and the most expensive instance yet** — the calendar missed the FOMC minutes last window
(which VOIDed `S98`) and has now missed a Fed-chair speech at D-0.

**And the second thing, because it re-frames every rate sentence downstream.** The desk has carried
*"the whole 60-session move in the 10y is REAL yield"* since 07-25. **On 60 observations that is still
true — and on the last five it has inverted.** `[FRED]`, aligned dates:

| Window | Δ`DGS10` | Δ`DFII10` (real) | Δ`T10YIE` (breakeven) | Reading |
|---|---:|---:|---:|---|
| 60 obs (05-22 → 08-19) | **+9bp** | **+19bp** | **−10bp** | real-led — the carry holds |
| 20 obs (07-22 → 08-19) | −2bp | −4bp | +2bp | ≈ nil, faintly the other way |
| **5 obs (08-12 → 08-19)** | **−3bp** | **−7bp** | **+4bp** | 🚨 **inflation-expectation-led** |

**Both halves are stated because the variable oscillates**, which is the recurring failure class this
stage's own instructions name. The 08-20 `T10YIE` print (**2.34**, +4bp in one session, and one
session *ahead* of the yield series) landed on the day Brent made a 3-week high — so the near-term
composition change has a named driver.

---

## §0 · Instrument state — read FIRST, because it decides what this stage may do

`preflight/PREFLIGHT_US.md` **PASS 3 / FAIL 5**. Binding, not re-litigated.

**This stage may NOT use**: the sweep's news-velocity axis · theme freshness *from the sweep* · any
"it went quiet" claim sourced from the sweep · the 50 velocity survivors as a set · the **Communication
Services `wflow` sign** (`GOOGL` 38.3%, `G3`) · `wflow` cap-weights as current (**37 days**, `G5`) ·
any flow/RS/OBV/short call on `EA` · a concentration number without its `--days` · any 08-21 price.

**This stage MAY use**: settled prices through **2026-08-20** · a **one-session Δ (08-19 → 08-20)** ·
`eqflow` and the ten non-flipper sector signs · FINRA short-vol · CFTC COT · `[FRED]` · primary
filings · **hand-probed** per-name news velocity and `theme_age` on themes (the CLI path measured
**40/40 valid** and **3523 · 3523 · 3523** at 22:1x–22:20 KST).

⚠ **`R81` is enforced here, not merely quoted.** The board carries **3 greens** — `MSTR` +0.900
(new-🟢), `TGT` +0.889, `MRVL` +0.539 — and **not one of them is used as evidence anywhere in this
report.** Where they appear, the underlying `obv_norm` / `rs20` / `flow_score` carries the sentence.

### §A-0 · 🚨 The `[FRED]` staleness is material today, and the substitute is labelled

`[FRED]` yield series end **2026-08-19**. The 08-20 session is the one the news is about
(*"Treasury rout restarts one day after Bessent's beefed-up buyback plan"*, 3 outlets;
*"US 30-Year Bonds Erase Gains From Treasury's Buyback Surprise"*, 4 outlets).

**Cross-provider substitute, declared under `D5`**: CBOE `^TYX`/`^TNX` (yfinance). **Provenance check
before use** — on the shared date **08-19**, `^TYX` **5.194** vs `[FRED]` `DGS30` **5.19**, and `^TNX`
**4.653** vs `DGS10` **4.65** ⇒ **agreement to 0.4bp**, so the substitute is admissible **for the
08-20 session only** and is tagged `[CBOE]` wherever it appears.

| Series | 08-19 | **08-20** | 08-21 (live, **not settled**) |
|---|---:|---:|---:|
| 30y `^TYX` `[CBOE]` | 5.194 | **5.237 (+4.3bp)** | 5.258 |
| 10y `^TNX` `[CBOE]` | 4.653 | **4.696 (+4.3bp)** | 4.712 |
| `DX-Y.NYB` | 98.830 | **98.900** | 98.791 — **11.5th percentile of 3 months** |

⇒ **The buyback bought one session.** `DGS30` fell **9bp on 08-19** (5.28 → 5.19) and gave back
**4.3bp on 08-20**. Any stage citing "the long end came down" must cite the give-back in the same
sentence.

---

## §A · Primaries — `[FRED]`, asof **2026-08-19** unless stated

### A-1 · The decomposition — **[measured]**

Given in the headline. **60-obs real-led (+19bp real vs −10bp breakeven); 5-obs breakeven-led (+4bp
breakeven vs −7bp real).** `T10YIE` has an **08-20** print (**2.34**) the yield series does not.

### A-2 · The curve, in levels and in its own distribution — **[measured]**

| Series | Level (08-19) | 20 obs ago | Note |
|---|---:|---:|---|
| `DGS2` | **4.19** | 4.20 | flat. 3-obs change distribution: mean +0.56bp, sd 6.87, p10 −8.0, p90 +10.0 |
| `DGS10` | **4.65** | 4.67 | `^TNX` says **4.696** on 08-20 |
| `DGS30` | **5.19** | 5.24 | `^TYX` says **5.237** on 08-20 |
| **`30y−10y`** | **54.0bp** | — | ⚠ **below its own 252-obs median (59bp)** and near p15 (51bp). The long end is high in **level** and the spread is **not** wide |
| `real_10y` | 2.35 | 2.39 | |
| `breakeven_10y` | **2.34 (08-20)** | 2.28 | +6bp |
| `DFF` | 3.63 | 3.63 | |
| `VIX` | 14.89 (08-19) | — | `^VIX` **16.01** on 08-20, **15.51** live 08-21 — 15.2nd percentile of 3 months |

★ **The shape that matters**: `DGS2` is **pinned at 4.19** while the 30y is within ~7bp of a
252-observation high and the 30y−10y spread sits **below** its median. That is **not** a term-premium
steepening story on the desk's own numbers — it is a **level** story concentrated in the long end with
the front end anchored. `P65`'s bull-steepener claim fails on both legs for a second run (§F).

### A-3 · The credit axis — cited, because a risk-off claim without it is narrative-only

`HY OAS` **2.73%** (08-19), **10bp off its 365-day low (2.63)**, +5bp over 20 observations.
`IG OAS` **0.81%**. `NFCI` **−0.559** (08-14) — the loosest reading in the window.
⇒ **There is no credit stress on this board.** Every "bond rout", "debasement" and "debt-ceiling"
sentence in §D is **narrative-only** by this stage's own rule, and is labelled as such where used.
⚠ `T23` applied: the term `bankruptcy` returns **52** hits over two days, the lowest count on the
board, and it is sat next to those two numbers rather than read alone. **Word count low, credit calm
— consistent, and neither is a regime claim.**

### A-4 · Staleness, stated

`DTWEXBGS` last prints **2026-08-14 (118.90) — 7 days**, so **the dollar is not cited from `[FRED]`
anywhere in this report**; `DX-Y.NYB` `[CBOE/ICE]` is used and labelled. `CPI`/`core CPI` are **July**
(one month, by construction). `M2` is **June**. `NFCI` is weekly to **08-14**.

---

## §B · Positioning — CFTC COT (Tue close, 3–4d lag ⇒ **context, not a trigger**) and FINRA

### B-1 · COT — and two cells moved hard

| Instrument | Net spec | Wk Δ | 1y %ile | Read |
|---|---:|---:|---:|---|
| **S&P 500 (E-mini)** | +11,280 | **+38,538▲** | **88%** | 🟢 crowded-long — ⚠ **flipped from 82% on 07-31 and the weekly Δ is the largest on the table** |
| **Nasdaq-100** | −42,905 | −7,899▼ | **0%** | 🔴 crowded-short — **the most extreme reading this desk has recorded**, down from the 5th %ile |
| Russell 2000 | −13,943 | −5,044▼ | 18% | 🔴 crowded-short |
| **UST 10Y** | −915,053 | **+64,190▲** | **7%** | 🔴 crowded-short, **but shorts were CUT by 64k into a 4.65–4.70 yield** |
| UST 2Y | −1,021,043 | −16,815▼ | 63% | 🟡 |
| **USD Index** | +21,409 | −1,090▼ | **80%** | 🟢 crowded-long — ⚠ **against a dollar at the 11.5th percentile of 3 months** |
| WTI Crude | +23,226 | +193▲ | **10%** | 🔴 crowded-short — ⚠ **into a 3-week high in Brent** |
| Nat Gas | −197,135 | +411▲ | **2%** | 🔴 crowded-short |
| Gold | +217,940 | +20,306▲ | 49% | 🟡 — ⚠ **neutral positioning into a 3-month price high** |
| **Copper** | +80,388 | +3,265▲ | **100%** | 🟢 crowded-long, the second 100th-percentile print in a month |
| Silver | +23,646 | +1,366▲ | 33% | 🟡 |

★ **Two contradictions are on the table and both are recorded rather than resolved**: speculators are
**crowded LONG the dollar at the 80th percentile while the dollar sits at the 11.5th percentile of
three months**, and **crowded SHORT WTI at the 10th percentile while Brent makes a three-week high**.
⚠ **The desk's own `D6` rejected ledger bars COT contrarianism as a signal** — these are cited as
*context* and no proposition below uses a percentile as a trigger.

### B-2 · FINRA daily short-vol z, settled **2026-08-20** — the B-grade axis

| 🔴 z ≥ +1.5 | | 🟢 z ≤ −1.5 | |
|---|---:|---|---:|
| **`WMT`** | **+3.02** (5v5 +10.9▲) | **`STLD`** | **−4.40** (5v5 −13.9▼) |
| **`NOC`** | **+2.43** (+2.9▲) | **`NUE`** | **−2.33** (+1.2▲) |
| **`PSX`** | **+1.95** (+13.5▲) | **`AVGO`** | **−1.60** (−1.9▼) |
| **`LMT`** | **+1.76** (−5.4▼) | | |

★★ **Two findings the price axis does not contain.**
1. **The defense complex's short axis turned as a group** — `NOC` +2.43, `LMT` +1.76, `LHX` +1.35 on
   one settled close, **against OBV 매집 at all three**. `D6` says the B-grade axis outranks the
   C-grade one; the disagreement is handed to DEEP-INDU rather than averaged.
2. **`NUE` reversed from 🔴 to 🟢.** The carried §3a line said *"the sheet's only 🔴 FINRA axis
   (z +1.99)"* with a kill at *"z > +1.5 for 5 sessions"*. Measured today: **z −2.33 = short
   covering**, short% 35.8 against a 20-day base of 50.6. **The kill did not fire; it inverted.**
   Corrected in §H, not deleted.
3. **`PSX` is now the refiner trio's odd name** (+1.95 🔴, 5v5 +13.5▲) against `MPC` −0.52 and
   `VLO` +0.49 — on the same three-name thesis, on the same settled close.

---

## §C · The tape — settled through **2026-08-20**

### C-1 · Sector excess, 5 settled sessions **08-13 → 08-20**, `SPY` **−1.964%** — **[measured]**

| Rank | Sector ETF | exc5 vs `SPY` | | Rank | Sector ETF | exc5 vs `SPY` |
|---:|---|---:|---|---:|---|---:|
| 1 | **`XLE`** | **+6.370** | | 7 | `XLY` | +0.470 |
| 2 | **`XLV`** | **+4.346** | | 8 | `XLC` | +0.303 |
| 3 | `XLB` | +2.175 | | 9 | `XLF` | −0.284 |
| 4 | `XLRE` | +1.876 | | 10 | `XLI` | −1.276 |
| 5 | `XLU` | +1.351 | | 11 | **`XLK`** | **−2.056** |
| 6 | `XLP` | +1.174 | | | | |

**Eight of eleven beat a falling index.** The three that did not are **Financials, Industrials and
Information Technology** — and the desk's tilts are aimed at two of the three.

★ **The `P78` estimator moved toward branch B and it is worth saying before it settles.** The
cross-sectional **range** of exc5 across {`XLU`,`XLRE`,`XLP`,`XLV`} is **3.172 = the 50.8th percentile**
of its own trailing 252 (mean 3.189, sd 1.471, p15 1.688, p85 4.707), against **3.888 = 73.4th** at its
08-20 registration. **The dispersion narrowed by ~22 percentile points in one session.** `P78` settles
08-26; this is a reading, not a score.

★ **And the spread that actually describes the week**: `XLE` exc5 minus EW{`XLU`,`XLRE`,`XLP`,`XLV`}
exc5 = **+4.183 = the 87.7th percentile** of its own trailing 252 (mean +0.613, sd 3.383, p85 +3.961,
p95 +5.734). **Energy is not merely leading; it is beating the entire defensive complex at a near-p90
rate.** That is the object `P81` brackets.

### C-2 · The energy complex — the control leg that carried the thesis has FAILED — **[measured]**

Settled 08-20: **Brent `BZ=F` 93.78 · WTI `CL=F` 87.83 · 3-2-1 crack 66.26 = 93.2nd percentile of 250
sessions · distillate crack 100.34 = 98.4th percentile · gasoline crack 49.21.**
`EW{MPC,VLO,PSX}` exc5 (08-13 → 08-20) = **+3.060**.

🚨 **`Brent's own 5-session return is +7.71%.** `P70`'s registered control leg is *"`BZ=F` 5d ≤ +2.0%"*
— on 08-19 it read **+0.66%** and passed; today it fails by **5.7pp**. ⇒ **the claim "the refiners pay
WITHOUT the barrel" is no longer supported by its own control.** The margin thesis may still be right;
**the evidence that separated it from a crude beta is gone this week**, and `P83` re-registers the
separation on an observable the barrel cannot manufacture.

**The kill counter, re-computed rather than carried** (`D298`): the five most recent 5-session changes
in the 3-2-1 crack, most recent first, are **`[+0.41, +6.51, −7.98, +0.82, −2.96]`** ⇒ **the two most
recent are both positive, so the "second consecutive decline" kill is still RESET.** ⚠ But **+0.41 is
functionally flat**, and that is stated rather than rounded up into a positive.

### C-3 · The AI-compute complex — still at an extreme, and the extreme eased — **[measured]**

`EW{AVGO, ANET, HPE, COHR, LITE}` exc5 (08-13 → 08-20) = **−7.178**, against `P79`'s registration
reading of **−12.425 = the 0.8th percentile of two years** and its own **p05 = −7.715**.
⇒ **It has climbed back to roughly the 5th percentile from the 0.8th.** Per name: `AVGO` **−10.910** ·
`HPE` −9.620 · `COHR` −9.404 · `ANET` −7.794 · **`LITE` +1.836** — the basket is not one object
this week either.

⚠ `P79` settles **2026-08-25, one session before the `NVDA` print, by construction.** Two sessions
remain. **No conclusion is drawn here.**

### C-4 · Flow, 3-axis, settled **08-20** — sector level (`eqflow` preferred to `wflow`, `G5`)

Universe: **n=299 · `wflow` −0.105 · 7 🟢 : 68 🔴**.

| Sector | `wflow` | `eqflow` | 🟢:🔴 | breadth | Δ (1 session) |
|---|---:|---:|---:|---:|---:|
| Energy | +0.169 | **+0.160** | 1:1 | 0.06 | −0.029 |
| Health Care | +0.150 | **+0.159** | 1:3 | 0.03 | −0.133 |
| Communication Services | 🚩+0.090 | **+0.151** | 0:1 | 0.00 | +0.352 |
| Consumer Discretionary | +0.010 | **+0.107** | 0:2 | 0.00 | +0.243 |
| Consumer Staples | +0.050 | **+0.086** | 1:1 | 0.05 | −0.038 |
| Materials | +0.008 | **−0.010** | 0:2 | 0.00 | +0.107 |
| Financials | −0.020 | **−0.097** | 2:8 | 0.04 | −0.011 |
| Information Technology | −0.279 | **−0.208** | 2:21 | 0.04 | +0.004 |
| Industrials | −0.247 | **−0.212** | 0:13 | 0.00 | −0.162 |
| Real Estate | −0.335 | **−0.231** | 0:4 | 0.00 | −0.026 |
| Utilities | −0.647 | **−0.606** | 0:12 | 0.00 | −0.079 |

★ **The single most useful row on this table is Utilities**, for the second run: `eqflow` **−0.606**,
`ex_top1` −0.648, **0 green of 15, 12 red**, against **exc5 +1.351**. **The purest duration leg has the
worst flow on the board and a positive price** — the same contradiction, one session older and
slightly wider.
🚩 **Communication Services' `wflow` is flipper-owned and is not used** (`G3`); its `eqflow` **+0.151**
and its `breadth` **0.00 (zero green of 12)** disagree with each other, and that disagreement is the
finding rather than a number to average.

---

## §D · News — `--scope foreign`, coverage stated before anything is concluded

### D-0 · Coverage accounting — because `tail = 0` is not a coverage claim

`brief --date 2026-08-20 --scope foreign --body 2` after `embed sync` (**5,403 received · 5,387
embedded · cursor `2026-08-21T22:21:32`**).

| Quantity | Value |
|---|---:|
| `denominator.articles` (after `excluded_not_news`) | **4,991** |
| clusters | 1,426 |
| events ≥2 sources | **789** |
| head / body / **tail** | 86 / 703 / **0** |
| `subevents_recovered` | **190** |
| `single_source_clusters` · shown | **637** · **15** ⇒ **622 withheld** |
| `excluded_nonmarket` | 0 (foreign feed carries no `nb` — classifier is Korean-only) |

🚨 **Two coverage facts must travel with every claim below.**
1. **622 single-source clusters are unshown**, and on the foreign feed the sample is **random, not
   score-ranked** (`nb` is `null` throughout) — so this run **cannot** say what is in them. Any
   "nothing happened in bucket X" sentence in this report carries that denominator.
2. ★ **Yesterday's run read this same day at `articles = 1,953`; today it reads 4,991.** The 08-20 US
   desk ran at 22:1x KST *on* 08-20, i.e. mid-session ET, and measured a day that was **39% complete**.
   **A same-day `brief` on a US pre-market run is a partial-day read by construction**, and that is a
   structural property of this desk's clock rather than a defect of the tool. Registered in §I.

### D-1 · Events — the head, with denominators

| # | Event | articles / outlets | Axis |
|---:|---|---:|---|
| 1 | **Oil rises to 3-week high as Iran war impasse fuels Middle East supply concerns** | **50 / 21** | ENERGY |
| 2 | **US debt tops $40 trillion threshold** | 30 / 19 | RATES/FISCAL |
| 3 | **Walmart shares tumble as sales growth slows to six-year low** | 34 / 17 | CONSUMER |
| 4 | **Trump vows 'economic warfare' on countries helping Iran** | 22 / 16 | GEOPOLITICS |
| 5 | **AI drives network equipment demand as parts shortages deepen** | **43 / 13** | AI/SEMI |
| 6 | Bitcoin rockets past $71,000 as regulatory hopes ignite crypto comeback | 43 / 11 | CRYPTO |
| 10 | Stock Market Today: Walmart Stock Drops on Disappointing Comparable Sales | 37 / 10 | CONSUMER |
| 15 | US stock market today: Wall Street drops as **Walmart, bond yields** drag it lower | 25 / 8 | RATES |
| 16 | **Dollar at three-month low as Treasury moves to soothe bond jitters** | 17 / 8 | FX/RATES |
| 18 | **Treasury bond buybacks complicate Fed's path to price stability** | 27 / 7 | RATES |
| 21 | **US Set to Cut Tariffs on Canada Metals, Autos in Trade Deal** | 15 / 7 | TARIFF/MATR |
| 28 | US Treasury buyback briefly eases bond rout, but debt worries persist | 20 / 6 | RATES |
| 35 | Japan's core inflation accelerates in July, bolsters case for rate hike | 8 / 6 | GLOBAL RATES |
| 46 | **Gold hovers near early-June high on lower bond yields** | 12 / 5 | METALS |

**From the body tier (2–4 outlets — where this desk's own instructions say the macro prints hide):**
- **`$1.65 of Target's $4.11 Quarterly Profit Came From Tariff Refunds`** (5/3) — **40.1% of `TGT`'s
  quarterly profit is a refund, not operations.** `TGT` printed 08-19 and is one of `S100`'s two legs.
- **`Fed Minutes Show Growing Support For Rate Hike By September`** (4/2) and
  **`'Many' Fed officials think higher rates will be…`** (ENDED thread, **peak 17 outlets**).
- **`Treasury rout restarts one day after Bessent's beefed-up buyback plan`** (3/3) ·
  **`US 30-Year Bonds Erase Gains From Treasury's Buyback Surprise`** (4/2) ·
  **`JPMorgan Team Sees Credibility Risk in Treasury's Bond Buybacks`** (3/3) ·
  **`Treasury Bond Fix Could Backfire, Warns JPMorgan`** (4/2).
- **`Warsh faces Fed independence test as Bessent moves in on central bank's turf`** (cnbc 08-20,
  5,912-char body) — the institutional frame behind the `P82` bracket.
- **`How the A.I. Borrowing Binge Helps Drive Up Government Bond Yields`** (3/3) — the mechanism
  `P67` is tracking, now printed by name.
- **`The energy market's rising 'crack spread' is threatening to break the American consumer`** (4/3).
- **`US Initial Jobless Claims dropped to 206K last week`** (5/4) — the only labour print in window.
- **`Samsung repays 20 trillion won SDC loan early as memory demand surges`** (3/3).
- **`KKR Data Center Chief Vaults to Prominence With Nvidia Pact`** (6/4) — `KKR` is carried.

⚠ **Both halves of the one full print in window** (`C2`): `US Initial Jobless Claims` **206K last
week**; the report gives no sequential figure in these bodies, so **the print is cited as a level with
its missing half named** and is **not** used as a proposition anchor.

### D-2 · Trajectories — `thread --days 7`, foreign

Per-day denominators first (`T24`): **08-15 282 · 08-16 294 · 08-17 756 · 08-18 826 · 08-19 822 ·
08-20 789 · 08-21 384**. **The 08-21 column is a 49%-of-yesterday partial day and no FADING tag
resting on it is read as a fade.**

| Thread | Tag | Outlet curve | Read |
|---|---|---|---|
| **Oil / Iran impasse** | FADING | **5→12→16→17→17→21→12** | **Peaked at 21 outlets on 08-20** — the day it was the #1 event. The final `12` is on the partial day ⇒ **not scored as a fade** |
| **`'Many' Fed officials think higher rates…`** | **ENDED** | 9→5→17→4, peak **17** | The FOMC-minutes thread. **An ENDED thread under a live rate proposition is a staleness flag** — and `P82` is the re-justification |
| **Walmart tumble** | **ENDED** | 5→17, peak 17 | Two days, high intensity, closed |
| `Trump pauses tariffs on Canada after last-minute deal` | FADING | 7→19→23→**7→5** | Peaked at 23; the metals/autos leg printed 08-20 at 7 outlets |
| `Dollar Falls Sharply as Prospects Dim for Fed Rate Rise` | FADING | 8→8→7→8→2 | ⚠ **Directly contradicts the ENDED minutes thread above.** Both are in this week's corpus |
| `Global bond yields hit multi-decade highs as governments…` | **REIGNITED** | 4→2 | |
| `Houthis Claim Third Attack on Saudi Aramco Refinery` | **REIGNITED** | 2→2 | ★ **The second refining mechanism** (`P62`), independent of Hormuz transit |
| `Nvidia to provide up to US$105bn guarantee for O…` | REIGNITED | 2→3→**15**→5→5 | |
| `Micron CEO Says AI 'Can't Scale' Without Memory` | REIGNITED | 2→3 | |
| `Samsung, SK Hynix prep record shareholder returns` | BUILDING | 4→7 | |
| `Gold rallies to three-month high, eyes third week` | BUILDING | 2→5→5→6 | ★ `$4,600` named on 08-21 |
| `Japanese inflation rises as BoJ weighs rate rise` | BUILDING | 6→8 | |
| `Constellation vs Vistra: Who Leads the AI Power…` | BUILDING | 3→4 | |

★ **The contradiction is the finding, and it is registered rather than resolved**: a FADING
*"prospects dim for a Fed rate rise"* thread and an ENDED *"many officials think higher rates will be
needed"* thread are both in the same week's corpus, at peaks of 8 and 17 outlets. **`P82` is written
so that Warsh's speech settles which one the market believes**, on an observable neither thread can
manufacture.

### D-3 · Bucket sweep — terms passed as **separate argv**, `--mode or --days 2 --scope foreign`

| Bucket | Terms | Hits | vs 08-20 |
|---|---|---:|---:|
| **RATES/CURVE** | yields · Treasury · Fed · buyback · curve | **3,272** | +189 |
| CREDIT/FIN | credit · spreads · default · bankruptcy · lending · banks | 3,242 | −11 |
| GEOPOLITICS | Iran · Hormuz · Russia · Ukraine · sanctions · tariff | 2,189 | −71 |
| GROWTH/LABOR | payrolls · unemployment · recession · GDP · consumer | 1,935 | −7 |
| AI/SEMI | semiconductor · chips · GPU · HBM · datacenter | 1,712 | −29 |
| ENERGY/OIL | oil · crude · Brent · refinery · OPEC · diesel | 1,498 | −79 |
| INFLATION | inflation · CPI · PPI · disinflation · deflation | 1,388 | +11 |

**Single-term controls, so a near-zero cannot be a mis-passed argv**: `buyback` **769** (⬆ from 557 —
**+38% in one day, the largest single-term move on the board**) · `Iran` 1,109 · `Hormuz` 503 ·
`semiconductor` 857 · `inflation` 1,357 · `refinery` 129 · **`bankruptcy` 52** · **`Warsh` 132** ·
**`debasement` 25** · `gold` 690.

⚠ **`debasement` at 25 is small and is reported with its denominator** — the word is in the corpus
(`US Dollar: Debasement worries weigh after buyback – Scotiabank`, 2 outlets) but it is **not** a
mass narrative, and no proposition below rests on it.

### D-4 · `theme_age` — with denominators, as `T24` requires

| Term | Tag | Age (d) | 7d avg | Accel | **n** |
|---|---|---:|---:|---:|---:|
| **`Treasury buybacks`** | 🟢 **FRESH** | **2** | **19.3** | — (no baseline) | **135** |
| **`Jackson Hole`** | 🟡 ACCELERATING | ≥90 | 11.4 | **7.0×** | **134** |
| `long-end yields` | 🟡 ACCELERATING | ≥90 | 8.7 | **14.52×** | 86 |
| `sovereign debt` | ⚪ ECHO | ≥90 | 3.3 | 1.52× | 122 |
| `memory shortage` | ⚪ ECHO | ≥90 | 15.0 | 1.51× | 553 |
| `crack spread` | ⚪ ECHO | ≥90 | 5.7 | 1.48× | 165 |
| `tariff refund` | ⚪ ECHO | ≥90 | 29.3 | 1.37× | 887 |
| `optical interconnect` | ⚪ ECHO | ≥90 | 3.4 | 1.27× | 155 |
| `rate hike` | ⚪ ECHO | ≥90 | 103.7 | 0.97× | 6,094 |
| `Strait of Hormuz` | ⚪ ECHO | ≥90 | **126.9** | **0.84×** | 8,022 |
| `AI capex` | ⚪ ECHO | ≥90 | 15.4 | 0.67× | 1,125 |
| `refinery outage` | ⚪ ECHO | 52 | 0.4 | 0.58× | ⚠ **27** |

★★ **`Treasury buybacks` holds 🟢FRESH for a second day and its base more than doubled (64 → 135,
7d average 9.1 → 19.3).** This is the second consecutive US run to produce a 🟢FRESH, and it continues
to be the positive case for `R83`'s **rewritten** mechanism — the readout is not capped; the
conjunction simply needs a genuinely newborn theme, and one was born on 08-19.
★ **`Strait of Hormuz` is ⚪ECHO at 0.84× on n=8,022** — the largest denominator on the board and
**decelerating**, on the same day its equity expression (`XLE` exc5 +6.370) led the market. **Attention
and price have separated on this axis**, which is exactly what `S84`/`S92`/`S95` were registered to
catch. `T24` satisfied on the denominator.
🚫 **`refinery outage` at n=27 is below the `T24` floor** and its 0.58× is **not** cited as a reading;
it is used only as the reachability check for `P83`'s anti-signal.

### D-5 · Blind-spot pass — `blindspot --days 2 --scope foreign`, sample read raw

Denominator **17,015** articles (blind pool = the whole window; no fixed set). **Token-0 emergent
terms, top of the frequency table**: `Earnings` 1,329 · `AI` 1,138 · `Trump` 456 · **`Treasury` 433** ·
`China` 351 · `Bitcoin` 311 · **`Bond` 265** · `Iran` 252 · `Nvidia` 244 · **`Fed` 237** ·
`Oil` 234 · **`Dollar` 226** · `Energy` 195 · **`Yields` 162**.

★ **The vocabulary-free instrument independently ranks the same complex the fixed buckets do**:
`Treasury` + `Bond` + `Fed` + `Dollar` + `Yields` = **1,323 mentions**, larger than any single non-AI
token. **The fiscal/rates axis is not an artifact of the desk's own term list.**
⚠ The raw sample is dominated by earnings-season and PR boilerplate (`prnewswire` awards,
`sec_edgar` 8-Ks, analyst-upside pieces) — **no new macro term survived a raw read**, and that is
reported rather than padded.

**New terms folded into the living table**: `Jackson Hole` · `Warsh` · `debasement` · `tariff refund`.

---

## §E · Propositions — falsifiable, both directions, mandatory anti-signal

★ **ID 3-grep at WRITE time**: `grep -rE "\bP(81|82|83|84)\b"` across `handoff/*.md`,
`llm_outputs/2026-08-*/industry_US/*.md` and `REPORT/` returned **0 files**. Highest existing **P80**
(2026-08-20).

### E-0 · Rulings on live rows, made on the CLAUSE before the branch is visible

**`S95` — the anti-signal is UNMEASURED and this stage says so rather than scoring it.** Its VOID
clause names *"a US refinery outage, PADD3 hurricane landfall, or an OPEC+ quota decision inside the
window."* Reachability probe: `theme_age "refinery outage"` **⚪ECHO 0.58× on n=27**, and the term
`refinery` returns **129** hits over two days, whose head item is
**`Houthis Claim Third Attack on Saudi Aramco Refinery`** — **a Saudi facility, not a US one**, so it
does **not** fire the clause as written. **No OPEC+ decision and no PADD3 landfall appears in the
window's 4,991-article corpus.** ⇒ **On the evidence pulled, the clause has not fired** — recorded as
*probed and not fired*, which is a weaker and more honest statement than *"not fired."* The row's
observable stands at **Brent 93.78 (08-20 settle), already above branch A's 93.00**, and it settles on
the 08-21 close.

**`S84`/`S92` — no ruling needed, but the attention/price split is registered.** Their object
(Hormuz) is ⚪ECHO **0.84×** on the largest denominator on the board while its equity expression led
the market by **+6.37pp**. Neither row is re-frozen; the split is handed to PREMORTEM.

---

### P81 — ★★★ Is this a FISCAL repricing or a FED repricing? They point the dollar opposite ways

**Claim.** Two stories are being told about the same week and this desk has been carrying both.
**(a) Fed repricing**: FOMC minutes show *"many officials"* open to hikes (ENDED thread, peak **17
outlets**), *"growing support for a rate hike by September"* (2 outlets) — this is **dollar-positive**.
**(b) Fiscal / debt repricing**: US debt through **$40tn** (19 outlets), Treasury doubling long-dated
buybacks, `JPMorgan` *"credibility risk"*, and the long end giving back **4.3bp `[CBOE]`** the very
next session — this is **dollar-negative and gold-positive**.
**Measured, the tape is voting (b)**: `DX-Y.NYB` **98.79 = 11.5th percentile of three months**, its
5-session return **−1.060% ≈ the 7th percentile** of its own 252; `GLD` 5-session **+4.086%, just
above its own p85 (+3.990)**; `DGS2` **pinned at 4.19**. **A genuine hike repricing cannot leave the
2y flat and the dollar at a 3-month low.**

- **Direction A (FISCAL owns it):** at the first `[FRED]` close covering **2026-08-28**, `DGS2`
  **≤ 4.22** (i.e. the front end stays pinned within +3bp) **AND** `DX-Y.NYB` closes **below 99.20** ⇒
  the long-end move is debt-supply/term-premium, not policy; **`XLE`'s +0.1534 pp/bp rate beta (the
  desk's only measured rate-exposed tilt) is the correct sign**, and every duration-underweight
  argument that rests on "the Fed is about to hike" is unsupported.
- **Direction B (FED owns it):** `DGS2` **≥ 4.32** (+13bp) **AND** `DX-Y.NYB` **above 100.20** ⇒ the
  minutes are being priced, the front end leads, and the four duration underweights get their
  mechanism back for the first time since `S102`'s regression measured them at ≈0 rate beta.
- **Between = C, and C is the favourite — disclosed at registration.**
- ★ **`D93` executed BEFORE freezing.** `DGS2` 3-observation change, trailing 252: **mean +0.56bp ·
  sd 6.87 · p10 −8.0 · p50 0.0 · p90 +10.0** ⇒ a ±13bp move over ~5 observations sits outside p90.
  `DX-Y.NYB` 5-session return, trailing 252: **p05 −1.183 · p15 −0.722**; the current −1.060 is at
  ~p07. The **99.20 / 100.20** levels are ±0.4% / +1.4% from 98.79. ⇒ **A ≈20% · B ≈10% · C ≈70%.**
- **State at registration:** `DGS2` **4.19** (`[FRED]` 08-19) · `DX-Y.NYB` **98.79** (live 08-21,
  labelled — the settled 08-20 print is 98.90 and either side of the band is >0.3% away, so the
  live/settled choice does not decide the row).
- 🚨 **Mandatory anti-signal (VOID):** an **intermeeting FOMC action**, an **actual quarterly refunding
  announcement**, or a **US sovereign-rating action** inside the window ⇒ the two channels become
  inseparable. ⚠ **Reachability-checked and NOT already fired** (the `D296`/`D300-KR` rule applied at
  registration): the next quarterly refunding falls outside a one-week window; no FOMC meeting falls
  inside it; and a rating action has a **base rate near zero** — the term `downgrade` does not appear
  in the head or body tiers of a 4,991-article day. **The clause is deliberately NOT written to include
  "a Fed speech", because Warsh speaks inside the window by design — that is `P82`'s object, and a
  clause that voids on it would void almost surely.**
- **Information content (`L3`): HIGH and symmetric.** A removes the policy leg from four underweights;
  B restores it. **Neither branch merely confirms.**
- **Owner:** `industry_US`. **Settles at the first `[FRED]` close covering 2026-08-28.**

### P82 — ★★★ The MANDATORY D-0 bracket: Warsh's Jackson Hole debut, which no calendar carried

**Claim.** The window's only D-0 dated binary is **today's Jackson Hole speech by the new Fed chair**,
and `catalyst_calendar --days 10` returns **zero rows** for it (§D, headline). A one-way rate frame
into an unbracketed Fed-chair debut is precisely the protocol violation this stage exists to prevent.
The information at stake is unusually high because **the two live threads point opposite ways**: an
ENDED *"many officials think higher rates"* thread at peak 17 outlets against a FADING *"prospects dim
for a Fed rate rise"* thread at peak 8.

- **Observable:** `DGS2` **and** `30y−10y`, `[FRED]`, at the **first close covering 2026-08-25**
  (the first settled read fully after the speech; 08-24 is a Monday and the release lags one day).
- **Direction A (hawkish — the minutes are ratified):** `DGS2` **≥ 4.29** (+10bp ≈ p90 of its own
  3-obs change) ⇒ the front end reprices, the **bear-flattener** returns, and — per `S102`'s own
  measured betas — the ENRG overweight is the tilt that is *helped* (`XLE` +0.1534 pp/bp) while the
  four duration underweights, at ≈0 rate beta, are **not** the expression.
- **Direction B (dovish / independence-defensive):** `DGS2` **≤ 4.09** (−10bp) **AND** `30y−10y`
  **≥ 59bp** (its own 252-obs median) ⇒ the chair declines to ratify the hawkish minutes, the curve
  re-steepens from the long end, and the "term premium owns the move" reading survives.
- **Between = C — the favourite, and disclosed**: `DGS2`'s realised range over the last 10 observations
  is **4.15–4.25**, entirely inside C.
- ★ **`D93` executed BEFORE freezing**: `DGS2` 3-observation change, trailing 252 — **mean +0.56bp,
  sd 6.87, p10 −8.0, p50 0.0, p90 +10.0.** `30y−10y` trailing 252 — **p15 51.0 · p50 59.0 · p85 65.0**,
  current **54.0**. ⇒ **A ≈10% · B ≈10% · C ≈80%.**
- **State at registration:** `DGS2` **4.19** · `30y−10y` **54.0bp** (both `[FRED]` 08-19).
- 🚨 **Mandatory anti-signal (VOID):** a **Treasury buyback-schedule change or refunding announcement**
  inside the window ⇒ the debt-management channel and the policy channel become inseparable, which is
  exactly what happened to `S102`. ⚠ **This clause is reachability-checked and its base rate is
  disclosed** (`D300-KR`, applied at registration): Treasury has made **one** such announcement in the
  window's history (08-19), the schedule is published in advance, and no further change is scheduled
  before 08-25 ⇒ **the clause will not fire almost-surely**, which is the defect that made `S98` and
  `S102` unscoreable. ⚠ **Warsh's own speech is deliberately NOT an anti-signal** — it is the event.
- **Information content (`L3`): HIGH.** **A** falsifies the desk's *"the front end is pinned"* reading
  (carried in §A-2 today) and hands the rate mechanism back to the duration underweights. **B**
  falsifies the hawkish-minutes reading that three separate threads printed this week.
- **Owner:** `industry_US`. **Settles at the first `[FRED]` close covering 2026-08-25.**

### P83 — ★★ The refiners' separation from the barrel has FAILED its own control, and this is the successor

**Claim.** `P70`/`P80` carried the refining thesis on *"the refiners pay **without** the barrel"*,
enforced by a control leg `BZ=F 5d ≤ +2.0%`. **On 08-19 that leg read +0.66% and passed; on 08-20 it
reads +7.71% and fails by 5.7pp.** ⇒ **this week the refiner excess (`EW{MPC,VLO,PSX}` exc5 +3.060)
cannot be separated from a crude beta by that instrument.** The margin thesis is not thereby refuted;
**its evidence is.** The separation has to be re-registered on a quantity the barrel cannot
manufacture — and there is one: **the distillate−gasoline spread**, which widens on capacity
destruction and is flat-to-negative on a pure crude move.

- **Observable:** the **distillate crack minus the gasoline crack** (`HO=F`×42 − `CL=F`, minus
  `RB=F`×42 − `CL=F`, i.e. **(`HO=F` − `RB=F`)×42**), settled closes, at the **2026-08-27** close,
  measured as the **change from the 08-20 settle**.
- **Direction A (capacity destruction is the driver):** the spread **widens by ≥ +4.0 $/bbl** ⇒
  distillate is bid against gasoline; the mechanism is refining capacity (Russian strikes, the Houthi
  Aramco attacks, the Ukrainian Taneco strike), **not** the barrel, and `L2`'s peak-margin trap becomes
  the binding constraint rather than crude.
- **Direction B (it was the barrel):** the spread **narrows by ≥ −4.0 $/bbl** ⇒ the week's refiner
  excess was crude beta, `P70`'s control failure was the true signal, and the "capacity" framing has
  been carrying a crude position under another name.
- **Between = C.**
- ★ **`D93` executed BEFORE freezing.** Current levels, settled 08-20: distillate crack **100.34 =
  98.4th percentile of 250 sessions** · gasoline crack **49.21** ⇒ **spread 51.13**. The 3-2-1 crack's
  own 5-session changes, most recent first, are **`[+0.41, +6.51, −7.98, +0.82, −2.96]`** — sd of that
  series ≈ **5.1 $/bbl**, so a ±4.0 band is **inside one standard deviation of the composite's weekly
  move** and both branches are genuinely reachable. **Stated up front, including that this makes C
  less dominant than on most rows this desk writes.**
- **State at registration:** spread **51.13**, distillate at the **98.4th percentile**, gasoline crack
  **49.21**, Brent **93.78**, `EW{MPC,VLO,PSX}` exc5 **+3.060**.
- 🚨 **Mandatory anti-signal (VOID):** an **issuer event at `MPC`/`VLO`/`PSX`** (guidance, unplanned
  outage, M&A) or a **PADD3 hurricane landfall** inside the window. ⚠ **Reachability-checked and not
  fired**: `theme_age "refinery outage"` ⚪ECHO **0.58×, n=27**; `refinery` **129** hits over two days
  whose head item is a **Saudi** facility. ⚠ **Named now so it cannot be used as an escape hatch
  later**: the **Houthi attacks on Saudi Aramco** and the **Ukrainian strikes on Russian refineries**
  are **non-US** capacity events — they **support** branch A's mechanism and do **not** fire this
  clause.
- ⚠ **`W3`**: this measures whether the mechanism is what the desk says it is, **not** whether the
  position pays. No sizing (P4).
- **Owner:** `industry_US`. **Settles 2026-08-27.**

### P84 — ★★ The consumer print is being read as demand, and 40% of one leg was a tax refund

**Claim.** The week's consumer evidence is being carried as a demand signal — `WMT` sales growth at a
**six-year low** (17 outlets), *"A Rare U.S. Sales Miss for Walmart Is Concerning for the Economy"*.
**But the other leg of the same basket is contaminated in the opposite direction**: `$1.65 of Target's
$4.11 quarterly profit came from tariff refunds` (3 outlets) = **40.1% of `TGT`'s reported profit is a
one-off government refund, not operations** — and `TGT` is the leg carrying `S100`, `S93` and the
Staples flow reading (`flow_score` +0.889, the sector's best). ⇒ **`S100`'s EW basket averaged a
+3.784 / −9.861 split (13.6pp, against a registered unconditional sd of 2.27pp) in which one leg's
earnings quality is a refund and the other's is a demand miss. The basket cannot see that.**

- **Observable:** `TGT` **minus** `WMT`, cumulative return **2026-08-20 close → 2026-09-03 close**,
  in percentage points. **Both prints are behind us**, so this measures what the market does with the
  *composition* once the headline has decayed.
- **Direction A (the refund is seen through):** the spread **≤ −6.0pp** ⇒ `TGT`'s post-print premium
  gives back as the refund line is stripped out; the Staples flow reading was an earnings-quality
  artifact and `S100`'s basket construction is the reason the desk could not see it.
- **Direction B (the market prices the operating gap, not the refund):** the spread **≥ +6.0pp** ⇒
  `TGT`'s operating result is what moved it, `WMT`'s six-year low is the real signal, and the
  intra-basket dispersion is information rather than noise.
- **Between = C, the favourite.**
- ★ **`D93` executed BEFORE freezing**: `S100`'s own registration measured the `EW{TGT,WMT}`
  unconditional 2-session |excess| at **sd 2.27pp** with **P(≥+3.0) 11.1% / P(≤−3.0) 7.9%**. A 10-session
  pair spread is wider; the ±6.0pp bands are set at roughly **2.6× that 2-session sd**, and the
  realised 2-session spread just printed **13.6pp**, i.e. **both branches are reachable and C is not
  overwhelming.** ⚠ **The estimator is a pair spread, not an excess vs a benchmark — no benchmark is
  named because none enters the arithmetic** (`C1` satisfied by construction, and said so explicitly).
- **State at registration:** `TGT` **158.25** · `WMT` **103.84** (both settled 08-20). Two-session
  history: `TGT` **+3.784%** vs `WMT` **−9.861%** (08-18 → 08-20).
- 🚨 **Mandatory anti-signal (VOID):** a **guidance revision, M&A, or a further tariff-refund/tariff-
  policy announcement naming either issuer** inside the window ⇒ the spread stops measuring the
  composition question. ⚠ Reachability: `tariff refund` is ⚪ECHO **1.37× on n=887** — a live but
  decelerating term, so the clause is **neither dead nor near-certain**.
- **Information content (`L3`): MODERATE-HIGH.** **A** falsifies the desk's Staples flow reading and
  `S100`'s instrument at once. **B** falsifies this proposition. ⚠ **`W5` is the reason this row
  exists** — an EW basket over two names with opposite earnings quality is the wrong unit.
- **Owner:** `industry_US`. **Settles 2026-09-03.**

---

## §F · Self-backtest — the settled scores, and one carried claim inverted

| ID | Claim | Registered KPI | Settle | **Observed (settled 08-20)** | Verdict |
|---|---|---|---|---|---|
| **`P65`** (08-16) | Long end is a **bull** steepener; `DGS2` **not pinned** | `30y−10y` ≥0.58 **∧** `DGS2` ≤4.15 | **08-21 — DUE** | `30y−10y` **0.540** ❌ · `DGS2` **4.190** ❌ | ★ **MISS — both legs fail, and by more than last run.** The spread fell 0.570 → **0.540**, now **below its own 252-obs median (0.59)** and near p15 (0.51), while `DGS2` stayed pinned. **The bull-steepener framing is dead on this desk's own numbers** |
| **`P66`** (08-16) | The distillate bid has a **physical** driver | `HO=F−CL=F` 20d gap + a further dated strike | **08-21 — DUE** | 20d gap **`HO=F` +3.19% vs `CL=F` −4.73% = +7.92pp** ✅ · **`Houthis Claim Third Attack on Saudi Aramco Refinery`** (REIGNITED thread) ✅ | ★★ **HIT on both legs.** The 20d gap widened from +5.48 at registration to **+7.92**, and a second, independently-sourced dated strike arrived |
| **`P69`** (08-17) | Does a Hormuz shutdown reprice crude at all? | `BZ=F` at 08-21: A ≥93.00 · B ≤86.50 | **08-21 — settles on tonight's close** | **`BZ=F` 93.78 (08-20 settle)** — already above A | **DEFERRED to the D+1 scorer.** ⚠ Its twin `S95` carries an anti-signal that this stage **probed and found not fired** (§E-0) |
| **`P70`** (08-17) | Refiners pay **without** the barrel | EW exc5 ≥+2.0 **∧** `BZ=F` 5d ≤+2.0% | **08-21** | EW **+3.060** ✅ · **`BZ=F` 5d +7.71%** ❌ | 🚨 **The control leg FAILED, and it is the leg that carried the claim.** On 08-19 it read +0.66% ✅. **`P83` is the successor and re-registers the separation on the distillate−gasoline spread** |
| `P67` (08-16) | AI capex bill migrating to debt; credit does not see it | `HY OAS` ≥2.85% at first close covering 08-28 | 08-28 | **`HY OAS` 2.73**, 10bp off the 365d low | **CARRIED, branch B tracking.** ★ And the mechanism printed by name this run: *"How the A.I. Borrowing Binge Helps Drive Up Government Bond Yields"* (3 outlets) — **narrative arrived, credit still has not moved** |
| `P75` (08-19) | The refining leg is decided by 0.37pp on its control | crack ≥95 **∧** EW exc5 ≥+2.0 (A) | **08-21** | 3-2-1 crack **66.26** ❌ · distillate crack **100.34** ✅ · EW **+3.060** ✅ | ⚠ **AMBIGUOUS AS WRITTEN, for a second run** — the row says *"the crack"* without naming the series, and the two series answer oppositely. **Recorded, not resolved; `P80`/`P83` name both series** |
| `P76` (08-19) | A new BUILDING robotics cycle the registry does not carry | ≥5 outlets on ≥3 days by 09-02 **∧** a `us_top300` supplier named | 09-02 | Unitree thread absent from this run's 7-day trajectory list | **CARRIED, tracking toward B.** ⚠ Absence from a top-of-list view is not a zero; the denominator is not cited as a score |
| `P77` (08-20) | Can Treasury cap the long end? | `DGS30` at first close covering 08-26: A ≤5.18 · B ≥5.38 | 08-26 | `DGS30` **5.19** `[FRED]` 08-19 — **1bp above branch A**; `^TYX` `[CBOE]` **5.237** on 08-20 | **CARRIED, and the 08-20 give-back moved it AWAY from A.** The buyback bought **one session** |
| `P78` (08-20) | The duration complex is a DISPERSION question | range of exc5 across 4 legs at 08-26: A ≥4.71 · B ≤1.69 | 08-26 | **3.172 = 50.8th %ile** (was 3.888 = 73.4th at registration) | **CARRIED, moved 22 percentile points toward B** in one session |
| `P79` (08-20) | AI-compute drawdown: flush or de-rate? | EW exc5 at 08-25: A ≥+8.02 · B ≤−7.72 | **08-25** | **−7.178** (was −12.425 = 0.8th %ile) | **CARRIED.** Now ≈5th percentile — **0.54pp from branch B, on the wrong side of it** |
| `P80` (08-20) | The refiners' kill has RESET | crack ≥65 **∧** EW exc5 ≥+0.86 (A) | 08-26 | 3-2-1 crack **66.26** ✅ · EW **+3.060** ✅ | **CARRIED, branch A tracking on both legs.** ⚠ The kill counter, **re-computed** this run (`D298`), is still reset — but its most recent rate is **+0.41, functionally flat** |
| `P52` `P73` `P74` | — | — | — | — | Settled/VOID on 08-20; not re-scored |

**Running tally this run: 1 MISS (`P65`) · 1 HIT (`P66`) · 1 control-leg FAILURE that retires a claim
(`P70` → `P83`) · 6 CARRIED · 1 construction defect repeated and recorded (`P75`) · 1 deferred to the
D+1 scorer (`P69`).**
★ **The honest summary is that this desk's rate framing lost twice this week** — `P65` missed on both
legs and `P74` was refuted yesterday — **while its energy framing hit on the physical leg (`P66`) and
lost its own control leg (`P70`) on the same day.** Both are recorded; neither is smoothed.

---

## §G · ★ SECTOR TRANSMISSION MATRIX — wind direction only, all 11 GICS

> ROTATION's input. **Not** a ranking of research effort, **not** a position. `eqflow` is used in
> preference to `wflow` throughout (37-day-old cap weights, `G5`). Driving proposition in the last
> column.

| # | GICS sector | Wind | Why, in one line (settled 08-20) | Driver |
|---|---|---|---|---|
| 1 | **Energy** | **OW** | **#1 on both axes and it is not close**: exc5 **+6.370** (rank 1), `eqflow` **+0.160** (rank 1), distillate crack at the **98.4th percentile**, and `XLE`−defensives at the **87.7th percentile**. ⚠ **Two caveats printed in the same line**: `P70`'s control leg **failed** (Brent 5d **+7.71%** — this week it is not separable from crude), and `PSX` carries a fresh **🔴 FINRA z +1.95** | **`P83`** · `P80` · `S88` · `S95` |
| 2 | **Health Care** | **OW** | Holds rank 2 on both axes — exc5 **+4.346**, `eqflow` **+0.159** — and **`S82` FIRED-A**: it decoupled **upward** out of the duration complex, so this is idiosyncratic, not a rate leg. ⚠ breadth **0.03**, 1🟢/3🔴 — the flow is thin under the price | `S82` (scored) · `P78` |
| 3 | **Materials** | **N** | ⬆ **from N−.** exc5 **+2.175** (rank 3), and the sector's two ledger objects both improved on the B-grade axis: **`NUE` FINRA z +1.99 → −2.33** and **`STLD` −4.40**, i.e. **short covering, not accumulation**. ⚠ Against that: `eqflow` **−0.010**, **0🟢/2🔴**, and *"US Set to Cut Tariffs on Canada Metals"* (7 outlets) is a **negative** for domestic steel. **One notch, on the FINRA reversal, and no further** | `S77` handoff · §B-2 |
| 4 | **Consumer Staples** | **N** | Unchanged. `eqflow` **+0.086**, exc5 **+1.174** — but the sector is now **two opposite prints**: `WMT` six-year-low sales growth, **−9.15% on 08-20**, FINRA **+3.02 🔴**; `TGT` flow **+0.889** with **40.1% of its quarterly profit from tariff refunds**. ⚠ **`R82` bars a promotion and this run does not attempt one** | **`P84`** · `S100` |
| 5 | **Communication Services** | **N** | 🚩 `wflow` is flipper-owned and unusable (`G3`). On the admissible axes `eqflow` **+0.151** (rank 3) against **breadth 0.00 (zero green of 12)** — the two disagree and neither is promoted on. `GOOGL` Δ **+0.459** is the board's 2nd largest but `D293` bars a Δ-only verdict | HANDOVER §1 |
| 6 | **Consumer Discretionary** | **N** | `eqflow` **+0.107**, exc5 **+0.470**, Δ **+0.243**. `HD` **+0.480** exc5 against `WMT` −8.146 ⇒ the consumer split is **across** the two GICS labels, not inside one | `S91` · `S93` |
| 7 | **Real Estate** | **N−** | ⬆ **from UW, one notch, and only on price**: exc5 **+1.876** (rank 4) against `eqflow` **−0.231** and **0🟢/4🔴**. **The price-vs-flow contradiction is unresolved and the notch is the minimum admissible expression of it** — `DLR` exc5 **−1.153** sits inside `S90`'s C band | `P78` · `S90` |
| 8 | **Utilities** | **UW** | **The worst flow on the board by a distance for a second run**: `eqflow` **−0.606**, `ex_top1` −0.648, **0🟢/12🔴** — against exc5 **+1.351**. ★ **This row remains the single strongest evidence for `P78`**: the purest duration leg is the *weakest* of the four in a window the duration story says it should lead | **`P78`** |
| 9 | **Financials** | **N−** | `eqflow` **−0.097** (below `wflow` −0.020 ⇒ cap-weighted is the better half), exc5 **−0.284**, 2🟢/8🔴. ⚠ A **bear flattener (`P82` branch A) is the state that would change this**, and it is bracketed rather than assumed | `P82` |
| 10 | **Industrials** | **UW−** | `eqflow` **−0.212**, exc5 **−1.276**, **0🟢/13🔴**. ⚠ **The desk's position here is defense**, and the defense complex's **short axis turned as a group** (`NOC` +2.43, `LMT` +1.76, `LHX` +1.35 against OBV 매집 at all three). 🚨 **`S99`'s pre-settle has `ETN` moving with the AI basket on all three of branch A's conditions** — if that settles A, this sector's "diversifying leg" is an AI-compute unit | `S97` · **`S99`** |
| 11 | **Information Technology** | **UW** | **Worst on both axes**: `eqflow` **−0.208**, exc5 **−2.056**, **21 red of 56**. §C-3: the AI-compute basket is at ~the **5th percentile of two years** and the desk holds all five names. ⚠ **`Nasdaq-100` spec is at the 0th percentile short** — rebound ammunition, `[COT 08-18]`, **context and not a trigger** (`D6`) | **`P79`** · `S85` · `S86` |

**Wind summary: OW ×2 (ENRG, HLTH) · N ×4 · N− ×2 · UW− ×1 · UW ×2.**
**Changes from 08-20: Materials N− → N · Real Estate UW → N−.** Both are **one notch, both are made on
a non-Δ leg** (`D293`), and both are stated with the axis that contradicts them.

⚠ **The board's own shape is the caution.** Eight of eleven sectors beat a falling index, and **six of
the eleven print a positive `eqflow`** — on a session the benchmark fell. **A promotion rule keyed to
absolute `eqflow` would promote most of the board** (`D302-KR`, measured on the KR side this morning
and reproduced in form here). **The two promotions above are made on rank and on a B-grade axis, not
on a level**, and ROTATION should apply the same cross-sectional discipline.

---

## §H · §4c — claims asserted and then refuted, in this run

1. ★★ **This run's own HANDOVER §6 said *"No binary lands ≤48h from this run"*, and this stage refutes
   it.** The Jackson Hole speech by the new Fed chair is **today**. The HANDOVER sentence is **left in
   place**; the correction lives here and in `P82`. ⚠ **The failure is the instrument's, not the
   sentence's** — `catalyst_calendar --days 10` returned four binaries and none of them was this one —
   but the stage that trusted it is still accountable, and that is why the rule is *"do not edit,
   append."*
2. ★★ **The carried refiner claim *"the refiners pay without the barrel"* is refuted by its own
   registered control**, not by an outside argument: `BZ=F` 5-session **+7.71%** against a control of
   **≤ +2.0%**. **`P83` replaces the instrument rather than the conclusion.**
3. ★ **The carried §3a line *"`NUE` is the sheet's only 🔴 FINRA axis (z +1.99)"* is false as of the
   08-20 settle** (z **−2.33**, short covering). Marked **stale and updated by measurement**, per the
   `M168` convention — and it is the **third** instance in two runs of the `D298` class (a state
   variable in prose with nothing that re-computes it).
4. ★ **The desk's *"the whole 60-session move in the 10y is REAL"* frame is confirmed at 60 obs and
   inverted at 5 obs**, and both are printed rather than the convenient one.

⚠ **And one thing this stage caught in itself before publishing.** The first draft of §G promoted
Materials on *"exc5 rank 3 and two FINRA reversals"*. **A short-covering reading is not an accumulation
reading** — `NUE` and `STLD` both have falling short-volume ratios on **zero** green and a negative
`eqflow`, and the sector's live news item (*Canada metals tariff cut*) points the other way. The
promotion was kept at **one notch and re-worded to say what it rests on**, rather than dropped or
inflated.

---

## §I · Failed or empty lookups this run

| Lookup | Result | Handling |
|---|---|---|
| `[FRED]` `DTWEXBGS` | last print **2026-08-14**, 7 days stale | **Not cited.** `DX-Y.NYB` substituted and labelled `[CBOE/ICE]` |
| `[FRED]` yield series for the 08-20 session | absent (terminate 08-19) | `^TNX`/`^TYX` substituted with a **provenance check on the shared 08-19 date** (agreement to 0.4bp), labelled `[CBOE]` |
| `catalyst_calendar --days 10` | returned 4 binaries; **missed the Jackson Hole speech** | Hand-injected as `P82`; **`D18`/`D288-KR` reproduction logged** |
| `fts search "Warsh speech"` (quoted 2-token) | **0 hits** | Re-run as separate single terms (`Warsh` **132**) — the quoted-multi-token failure class, avoided rather than read as absence |
| `blindspot` z-scored token view | this invocation returned the **frequency** view, not the z view | Reported as measured; no z-score is quoted |
| `brief` single-source tier | **622 of 637 clusters withheld**, foreign feed has **no `nb` score** ⇒ random sample | Stated in D-0 and carried into every "nothing in bucket X" claim |
| CF realized natural-gas cost (HANDOVER §3) | **no reachable series** | Recorded as a condition-writing defect, not scored |

---

## ✅ EXIT CHECK — self-audit

- [x] Catalysts injected (`catalyst_calendar --days 10`, 4 binaries) **and one hand-injected** after the
      news pass refuted the tool's "none ≤48h".
- [x] Events read with **`--body 2`**, `tail = 0`, and **`tail = 0` is explicitly NOT used as the
      coverage claim** — `single_source` 637/15 (622 withheld), `excluded_nonmarket` 0/0 (foreign feed
      has no classifier), `subevents_recovered` **190**, all quoted in D-0.
- [x] Denominator quoted **after** `excluded_not_news`: **4,991**.
- [x] Trajectories read (`thread --days 7`); every proposition carries a thread tag+curve or says "no
      thread"; **the ENDED FOMC-minutes thread is flagged as a staleness flag under a live rate
      proposition** and `P82` is the re-justification.
- [x] Every "nothing in bucket X" claim carries its denominator (`bankruptcy` 52 beside `HY OAS` 2.73
      and `NFCI` −0.559, per `T23`; `debasement` 25 stated as small).
- [x] **All bucket terms passed as separate argv**; single-term controls run; the one quoted-multi-token
      zero (`"Warsh speech"`) is named in §I as a CLI artifact, not an observation.
- [x] Headline prints cited with both halves where both exist; the one print with a missing half
      (jobless claims 206K) is **named as half-quoted and not used as an anchor** (`C2`).
- [x] Every relative-performance number names its benchmark inline (`SPY` throughout §C; `P84`'s pair
      spread states that no benchmark enters the arithmetic).
- [x] Credit axis read and cited (`HY OAS` 2.73 · `IG OAS` 0.81 · `NFCI` −0.559); every "rout" /
      "debasement" sentence is labelled **narrative-only**.
- [x] `real_10y` quoted **with** `breakeven_10y`, at three horizons, with the inversion stated.
- [x] Transmission matrix produced, all 11 sectors, one line each, with the driver ID.
- [x] Self-backtest scored and the running tally appended — **including the two losses**.
- [x] New blind-spot terms folded into the living table (`Jackson Hole`, `Warsh`, `debasement`,
      `tariff refund`).
- [x] **No tag used as evidence anywhere** (`R81`); **no Δ-only verdict** (`D293`); **no Communication
      Services `wflow` sign** (`G3`); **no news velocity or theme freshness from the sweep** (`G1`).
- [x] **Linter run on this stage's own output** — `python -X utf8 scripts/report_lint.py "llm_outputs/2026-08-21/industry_US/MACRO_REPORT.md"` → **0 findings** (rules C1, C2, S6, D6). ⚠ It checks form only; a clean run is not a correct report.


---

# §5 · DRIFT ADDENDUM — appended post-run by Stage 11 (append-only; nothing above is edited)

> `drift_watch.py --report llm_outputs/2026-08-21/industry_US/MACRO_REPORT.md`, run **2026-08-21
> 23:2x KST**. **The report above is left exactly as written; this section sits beside it.**

## 1 · The instrument result, and its window is TOO SHORT — `D282` reproduces

`drift_watch` reports *"완주(2026-08-21T22:44) 이후 **0.7h** 감시"* against the stage's own **+3–6h**
specification. **`D282` reproduces for a third run**: a term-burst instrument reading a lagging news
corpus for forty minutes has little chance of seeing a regime change, and **it did not see the one
that matters** (§3). The burst list is reported for completeness; **the finding below came from
body-reading it, not from the z-scores.**

**Two 🚨 candidates (burst ≥3.0×):**

| Term | Post-run count | vs baseline | Body-read verdict |
|---|---:|---:|---|
| `downgrade` | 7 | **6.4×** | 🚫 **NOT a regime item — the `D29` class.** All three titles are analyst-target boilerplate: *"Qiagen Reaches Analyst Target Price"*, *"QTRX Crosses Above Average Analyst Target"*, *"Hanmi Financial Corporation's Big Run Higher Doesn't Justify A Downgrade Just Yet"*. **Counted, body-read, discarded** |
| **`blockade`** | 6 | **4.0×** | ★★★ **REAL, and it moved in BOTH directions on the same day — see §2–§3** |

**Non-burst activity, for the denominator** (`T24`): `Strait of Hormuz` 5 · `rate hike` 5 · `default`
4 · `invasion` 3 · `bankruptcy` **2** · `new tariff` 1 · `ceasefire` **1**.
⚠ **`bankruptcy` at 2 and `ceasefire` at 1 are consistent with §A-3's credit reading** — `HY OAS`
2.73%, 10bp off a 365-day low. **No credit-stress term is bursting.**

## 2 · 🚨 A STATE FACT the report above does not carry: the Strait of Hormuz is CLOSED

**The report treats Hormuz as a transit-*risk* axis. Four independent outlets say it is currently
shut**, and the body-read is unambiguous:

- `aljazeera` **08-21**, full body: *"…the critical **Strait of Hormuz in the Gulf remains closed to
  shipping**, upending global energy and financial markets. **Before the war, some 20 percent of
  global oil and natural gas supplies were shipped through this waterway.**"*
- `nasdaq` **08-18**: *"Crude Oil Advances As U.S.-Iran Faceoff Deepens **Leaving Strait Of Hormuz To
  Remain Shut**"* · `nasdaq` **08-19**: *"…**Leaving Strait Of Hormuz Effectively Shut**"*
- `toi` **08-20**: *"Crude remains above $90 as **Hormuz operations remain disrupted**"*
- `oilprice` **08-19**: *"Strait of Hormuz Shipping Slows After Vessel Attack"*

⚠ **And the corpus contradicts itself, which is recorded rather than resolved**: `cnbc` **08-18** —
*"Ship attack in Hormuz results in one casualty while **Trump says strait is 'open and operating'**"*.
⇒ **The desk cannot verify the physical state from this corpus; what it can verify is that four
outlets describe it as shut and one quotes an official calling it open.** Tagged `[news]`,
**not** `[measured]`.

★ **Why this matters to rows already registered, stated plainly.** `S84`, `S92` and `S95` are all
written around a **Hormuz REOPENING**. If the strait is already shut, **branch A of `S84`
("Hormuz de-escalates") is a larger move than its ±3.174pp band was calibrated for**, and `S95`'s
Brent observable is sitting at **93.78 (already above its branch-A line of 93.00)** for a reason the
report above attributes to "transit risk" rather than to a closure.
🚫 **No threshold is moved and no row is re-frozen** (`D242`). **The state fact is recorded so the
D+1 scorer reads the branches against the right world.**

## 3 · ★★★ And the same day printed the OPPOSITE signal — the de-escalation the desk is one-way into

Inside the same 0.7h window, three outlets carried an Iranian de-escalation signal:

- `euronews` **08-21**: *"**Iran's president calls for end to war** from 'position of power' as US ups
  pressure"*
- `bloomberg` **08-21**: *"**Iranian President Calls for End to US War** While Tehran Is Ahead"*
- `investing_en` **08-21**: *"Iran's president calls for end to war with US"*

**Against it, on the same day:** `aljazeera` *"Iran war live: US vows toughest Iran sanctions, urges
China support"*; Treasury Secretary Bessent on CNBC saying the new "economic warfare" could include
**secondary sanctions on other nations and companies** doing business with Iran; and `economictimes`
**08-21**: *"Crude oil nears $95 as **Iran peace deal hopes fade**"*.

⇒ ★ **The escalation and de-escalation legs printed within hours of each other, and this is exactly
the oscillating-regime-variable class this stage's own instructions name as the recurring failure
mode.** **The report above does not bank either direction** — `S84`, `S92`, `S95` and `S109` are all
two-sided, and `P83` deliberately re-registered the refining separator on a spread **crude cannot
manufacture**. **That construction is what makes this addendum a note rather than a correction.**

## 4 · What changes in the report above — **one thing, and it is a label, not a verdict**

**Nothing in §A–§I is retracted.** The single change:

**§D-2's Hormuz thread reading — *"⚪ECHO 0.84× on n=8,022 … attention and price have separated"* —
is CORRECT on attention and INCOMPLETE on state.** The theme is decelerating in *coverage volume*
**while the underlying waterway is described as shut by four outlets**. ⇒ **"Attention is fading"
must not be read as "the risk is fading."** Added here rather than edited above, so the original
sentence stays visible next to its qualification.

⚠ **And one obligation this addendum creates for the D+1 scorer**: `S95`'s anti-signal (a **US**
refinery outage, PADD3 hurricane landfall, or an **OPEC+ quota decision**) — **the drift sweep shows
no such item** (`new tariff` 1, no OPEC term bursting, `refinery` head item still the **Saudi** Jazan
facility). **Probed twice now and not fired**, which is a stronger statement than the single probe in
§E-0 and is recorded as such.

## 5 · Honest limits of this check

1. **The window is 0.7h against a 3–6h specification** — `D282`, third run. **The Hormuz-closure fact
   was NOT surfaced by the burst z-scores**; it came from body-reading the one real burst term.
   **A term-burst instrument did not find the largest state fact in its own window.**
2. **The de-escalation leg is `[news]` at three outlets with no body** (two title-only, one paywalled
   feed) — **direction is corroborated, magnitude is not**, and no bracket is written on it.
3. **The US session was open throughout this check** (23:2x KST = 10:2x ET). **No price is quoted in
   this addendum** for exactly that reason; the crude figure in the `aljazeera` body ($86.20 → $86.70
   WTI) is reported **as the article's own text**, not as this desk's measurement — and it disagrees
   with `economictimes`'s *"nears $95"* on the same day, which is a Brent-vs-WTI conflation in the
   press and is named here so no stage adopts either number.
