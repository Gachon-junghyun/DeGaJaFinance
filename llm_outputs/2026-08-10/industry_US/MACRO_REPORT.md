# MACRO_REPORT — industry_US · 2026-08-10 (Mon) · Stage 3/11 (L1·MACRO)

> Analytical output only. Zero buy/sell language (P4). `--scope foreign` on every news call.

## ⚠⚠ THE CLOCK, AND IT MOVED WHILE THIS STAGE RAN

**Stage opened 09:18 ET · the US cash market opened 09:30 ET · this stage closed after that.**

- **Every price number in this report was pulled BEFORE 09:30 ET and is a settled 2026-08-07 close.**
  Verified, not assumed: the pre-open pull reproduced ten inherited bracket observables to three
  decimals (HANDOVER §2b-i), which a live bar could not do.
- **A pull taken at 09:36 ET returned live 08-10 rows** (SPY 772.70, NEM 113.67) — recorded here so
  the difference is on the record, and **every downstream stage must use the pre-open panel or
  re-pull with an explicit `≤ 2026-08-07` filter.** This is **D74** caught inside a single stage.
- ⇒ **This is the THIRD consecutive US run on the 08-07 bar.** Prices are **one observation (S1)**.
  **What is new today is the news axis, the FRED publication pattern, and one disclosed corporate
  event** — and those are what this report is about.

---

## §A · The rate/credit axis — `[FRED]`, this run's own pull, with the publication lag stated

`module_macro_us --json`, pulled 2026-08-10 09:1x ET.

| Series | FRED id | Last print | `asof` |
|---|---|---|---|
| 2y Treasury | `DGS2` | **4.25** | 2026-08-06 |
| 10y Treasury | `DGS10` | **4.69** | 2026-08-06 |
| **derived 2s10s** | `DGS10 − DGS2` | **+0.44** | 2026-08-06 |
| real 10y | `DFII10` | **2.43** | 2026-08-06 |
| **10y breakeven** | `T10YIE` | **2.25** | **2026-08-07** |
| HY OAS | `BAMLH0A0HYM2` | **2.71** | 2026-08-06 |
| IG OAS | `BAMLC0A0CM` | **0.78** | 2026-08-06 |
| VIX | `VIXCLS` | **15.15** | 2026-08-06 |
| effective fed funds | `DFF` | **3.63** | 2026-08-06 |
| **SOFR** | `SOFR` | **3.62** | **2026-08-07** |
| **overnight RRP** | `RRPONTSYD` | **1.45** | **2026-08-07** |
| financial conditions (weekly) | `NFCI` | **−0.529** | 2026-08-01 week (2026-07-31) |
| broad dollar | `DTWEXBGS` | **119.7034** | **2026-07-31 — 6 publication days** |

**`real_10y` quoted with `breakeven_10y` (protocol requirement):** real **2.43** vs breakeven **2.25**.
⚠ **They are one day apart** (2.43 is 08-06, 2.25 is 08-07), so **the decomposition of the 08-07
session into real vs inflation is `unknown` (C3)** — not zero, not benign. It is the same hole that
has blocked S66/S70 for four runs.

**Credit axis, cited as the EXIT CHECK requires:** HY OAS **2.71** — **39bp** from S26's 3.10 kill
line and, on the last published print, **tightening** into the payroll shock (2.75 → 2.71). IG OAS
**0.78**, unchanged for a **6th** consecutive print. NFCI **−0.529**, still loosening.
⇒ **No credit-stress claim is available on the published data, and none is made.** Any risk-off
reading of the 08-07 session in this report would be **narrative-only** and is labelled as such.

### A-1 · ★★★ `D212` replicates a THIRD time and widens to a THREE-series pattern

| Prints **2026-08-07** | Stops **2026-08-06** |
|---|---|
| `T10YIE` 2.25 · `RRPONTSYD` 1.45 · **`SOFR` 3.62 (new this run)** | `DGS2` · `DGS10` · `DGS30` · `DGS5` · `DFII10` · `BAMLH0A0HYM2` · `BAMLC0A0CM` · `VIXCLS` · `DFF` |

The split is **not random and now has a shape**: the series that carry 08-07 are **money-market
prints and a derived series**; the ones that do not are the **H.15 constant-maturity block and the
ICE BofA OAS block**. And one of the three (`T10YIE ≡ DGS10 − DFII10`) is **arithmetically derived
from two that stop a day earlier** — the anomaly that opened D212 on 08-08.

⇒ **Four rows are blocked by this and three of them were DUE TODAY**: **S51** (derived 2s10s at the
settled 08-07 close), **S66** (ΔDGS2 + ΔHY OAS), **S70** (HY OAS alone). The 08-08 run wrote *"expect
2026-08-10"*; **it is 2026-08-10 and at 09:18 ET the print is not there.**
★ **This stage pre-commits to a second pull before writeback**, at least three hours later in the ET
day. If the H.15 block posts, the three rows are scored in this run's DRIFT addendum. If it does not,
**the retry hour is reported** rather than the failure being restated.

---

## §B · Positioning — ⚠ the COT is the SAME 08-04 file the 08-08 and 08-09 runs used

`us_flow.py --cot`. **Published Friday 08-08 15:30 ET on Tuesday-08-04 data; next publication 08-14.**

| Instrument | Net spec | Wk Δ | 1y %ile | Read |
|---|---|---|---|---|
| S&P 500 (E-mini) | −27,258 | −10,062 ▼ | **80** | crowded long |
| **Nasdaq-100** | −35,006 | −25,091 ▼ | **0** | **crowded short — the floor of the year** |
| Russell 2000 | −8,899 | −7,520 ▼ | 26 | neutral |
| **UST 10Y** | −979,243 | −103,124 ▼ | **3** | crowded short |
| UST 2Y | −1,004,228 | +120,346 ▲ | 65 | neutral, shorts covering |
| **USD Index** | +22,499 | **+5,302 ▲** | **81** | **crowded long, and BUILDING** |
| WTI | +23,033 | +3,275 ▲ | 18 | crowded short |
| Nat Gas | −197,546 | −6,747 ▼ | **1** | crowded short |
| Gold | +197,634 | +15,564 ▲ | 29 | neutral |
| **Copper** | +77,123 | +9,842 ▲ | **100** | **the trailing-year maximum** |
| Silver | +22,280 | +63 ▲ | 29 | neutral |

⚠⚠ **This snapshot PRE-DATES the 08-07 payroll print and is three runs old.** Nothing in it may be
presented as a reaction to NFP, to the Hormuz news, or to anything after Tuesday 08-04.
⚠ **COT contrarian sits in the REJECTED signal grade (D6)** — this is context, never a trigger.

---

## §C · The tape, settled 2026-08-07 — re-derived pre-open, not inherited

Bench **SPY**, named inline on every row (C1). Excess = simple % change difference over N sessions.

| ETF | exc1 | exc5 | exc20 | exc60 |
|---|---|---|---|---|
| XLK (IT) | +0.81 | **+3.69** | −1.25 | +2.54 |
| XLB (Materials) | +0.71 | **+1.31** | +1.45 | −3.37 |
| XLY (Disc) | +0.88 | −0.26 | −0.19 | −3.42 |
| XLU (Utilities) | −0.08 | −5.18 | **−6.39** | −8.25 |
| XLV (Health) | +0.14 | −1.59 | +0.58 | **+8.84** |
| XLI (Industrials) | −0.38 | −0.54 | −0.63 | +1.46 |
| XLRE (Real Estate) | −0.23 | −3.71 | −1.23 | −3.85 |
| XLC (Comm) | −0.55 | −0.73 | −2.77 | **−8.73** |
| XLP (Staples) | −0.60 | −3.43 | −1.24 | −3.95 |
| XLF (Financials) | −0.97 | −2.35 | +0.97 | +6.92 |
| XLE (Energy) | −1.75 | **−6.95** | +1.97 | −4.87 |

**Cross-asset, same bar:** GLD **+7.25%/5d, +5.69%/20d** · SLV **+9.82%/5d** · UUP **−0.35%/5d,
−1.13%/20d** · FXY +1.01/+2.64 · FXE +0.18/+1.31.
✅ **UUP reproduces the 08-09 run's P39 figures exactly (−0.43 / −0.35 / −1.13)** — a C1 check, not a
second observation.

### C-1 · ★★★ Materials is ONE NAME, and that name's driver was DISCLOSED THIS MORNING

XLB's 5-session excess is **+1.31**, and **S57 branch A fires above +1.9** — 0.59pp away, at any
settled close through 08-12. **M502** already measured that removing NEM alone takes it to **+0.194**
and removing {NEM, ALB, FCX} takes it to **−0.485 — a sign flip on 6.6% of fund weight.**

**Measured this run, settled 08-07, bench SPY inline:**

| | 1-session | 5-session |
|---|---|---|
| **NEM** absolute | **+7.16%** | **+20.56%** |
| **NEM excess vs SPY** | **+6.55pp** | **+17.05pp** |
| XLB excess vs SPY | +0.71 | +1.31 |

⇒ **one name's 5-session excess is 13× the entire sector ETF's**, and on M502's own decomposition
**NEM accounts for ~85% of XLB's total (+1.113 of +1.307).**

★★★ **And this morning the driver printed, from the issuer.** `[globenewswire press release + nasdaq
body, 2026-08-10]`, corroborated by `[wsj]` and `[mining]`:

- **Newmont and Barrick reached an agreement** to contribute excluded properties into the **Nevada
  Gold Mines joint venture** and **settle all outstanding disputes.**
- **NEWMONT WILL PAY BARRICK $1.95 BILLION.**
- **Newmont formally consented to Barrick's proposed IPO of its North American gold assets.**
- Newmont's Fiberline and Mike developments and Barrick's Fourmile development go into the JV.

⚠⚠ **The direction of the cash matters and a headline-only read gets it backwards.** The WSJ title is
*"Barrick Mining Settles Newmont Nevada Dispute for $1.95 Billion"*, which reads as Barrick paying.
**The body says Newmont pays Barrick.** ⇒ **C1, and the desk's own dominant failure class (naming the
wrong object) available in a five-word headline.**

**Independent cross-check on the price leg (D5):** the nasdaq body states NEM closed Friday **+7.16%**
and Barrick **+5.58%**; this run's own yfinance settles give **+7.16%** and **+5.58%**. **Two
independent sources agree to two decimals.**

⇒ **The consequence for S57 is specific and dated**: the observable that is 0.59pp from firing is
**85%-carried by a name whose live driver is a JV settlement, an IPO consent and a $1.95bn cash
outflow — none of which is a materials-cycle signal.** **S57-ANNEX was registered before the branch
could fire precisely to hold this**; today it acquires a named, dated, primary-sourced object.
**PREMORTEM owns the extension. ROTATION may not make a Materials call on XLB's aggregate.**

### C-2 · The one live-bar reading in this report, quarantined

`S55`'s legs (`HO=F`, `CL=F`) trade an electronic session that was already open pre-market:

| | settled (08-07) | live (08-10 electronic) |
|---|---|---|
| HO %chg from the 08-04 anchor | +3.498 | **+8.047** |
| CL %chg from the 08-04 anchor | +3.181 | **+4.949** |
| **spread (the observable)** | **+0.318** | **+3.097** |

⇒ **+2.78pp = 0.60σ of S55's own measured 4.671pp sigma, on a row that settles tomorrow.**
**The settled value is the only one used.** The live one is recorded because **its direction is
information about a proposition below (P42), not about the bracket** — distillate is outrunning crude
**+4.39% vs +1.71%** into Monday.

---

## §D · News — events, trajectories, buckets, blind spot (`--scope foreign`, every call)

### D-1 · Denominator, corrected, and the coverage claim stated honestly

`brief --scope foreign --body 2 --singles-nb 10`, market day **2026-08-10**:

```
articles 2,209 → clusters 795 → events(2+ outlets) 349 → market 349 · non-market 0
head(≥5 outlets) 30 · body(2–4) 319 · tail 0
subevents_recovered 70
single_source clusters 446 — shown 15 — ⚠ scored 0, scorable 0, UNSCORED 446
excluded_nonmarket 0 of 0 · excluded_not_news {}
```

⚠⚠ **`tail = 0` is NOT the coverage claim.** **431 single-outlet clusters were not opened**, and the
module states they are **UNSCORED, not low-scored** — the relevance classifier is Korean-only, so on
`--scope foreign` the single-source tier is a **random sample**, not a ranked one. **Every "quiet"
statement in this report carries the number 431.**
✅ `excluded_nonmarket` is genuinely 0 this run (band −3.0), so no boundary-band event was withheld.

### D-2 · Trajectories (`thread --days 7`), and the tags disagree with the curves

Per-day event counts: **08-04 825 · 08-05 845 · 08-06 816 · 08-07 719 · 08-08 283 · 08-09 277 ·
08-10 349.** ⚠ **The window contains two weekend days at ~1/3 the weekday rate**, so every
`FADING` tag is partly a calendar artifact. **Curves are cited; tags are not trusted alone.**

| Thread | Tag | Outlet curve 08-04 → 08-10 | Read |
|---|---|---|---|
| **Oil / Hormuz price** | FADING | **22 → 13 → 13 → 16 → 6 → 7 → 17** | ⚠ **the tag is on the 7-day shape; the last three days are 6 → 7 → 17 = re-accelerating.** Today's head cluster is **30 articles / 17 outlets, the day's largest** |
| **Iran diplomacy** | FADING | **8 → 18 → 14 → 12 → 15 → 9 → 4** | attention decaying **while the statement gets more concrete** — the opposite pairing to the price thread |
| **Ukraine strikes on Russia** | FADING | 14 → 17 → 20 → 19 → 12 → 11 → 10 | includes *"Ukraine hits refineries deep inside Russia"* at **peak 20 outlets** |
| **Warsh / Fed** | REIGNITED | 6 → 7 → 6 → **9** | today: *"New Fed Chair Kevin Warsh Has Refused to Give Forward Guidance"* 14/9 |
| **Gold ↔ Hormuz** | REIGNITED | 3 → 8 → 8 → 5 | the metals leg is explicitly narrated **as a Hormuz derivative** |
| **Dollar / FX** | REIGNITED | 3 → 4 → 6 → **5** | today: *"Dollar near two-month trough as US inflation data awaited"* **15 articles / 5 outlets** |
| **Earnings-call boilerplate** | BUILDING | 3 → 2 → 2 → 2 → 2 → 2 → 3 | **498 articles** — the **D10** class, excluded from every ranking below |

### D-3 · The 7-bucket sweep — run with an EXPLICIT `--mode or`, because of a rescued finding

★ **`D230` (rescued from the orphaned 08-09 run, HANDOVER §11) is not merely recorded — it is
applied.** `fts search` defaults to **`and`**, `search` defaults to **`or`**, and the protocol's own
L2·news text instructs *"OR-mode per bucket"* on the AND instrument. **Every count below carries an
explicit `--mode or`.**

Pool denominators, measured in the same session: **d1 = 2,209 articles** (this day's brief),
**d7 = 38,565 articles** (`coverage`, 7-day foreign window).

| bucket (single-token argv) | d1 | d3 | d7 | **d1 share ÷ d7 share** |
|---|---|---|---|---|
| credit (spreads · default · downgrade) | 333 | 838 | 1,897 | **3.06** |
| trade/tariff (tariff · tariffs · sanctions) | 328 | 869 | 1,902 | **3.01** |
| rates/Fed (Fed · yields · payrolls · inflation) | 1,016 | 2,554 | 5,910 | **3.00** |
| metals/USD (copper · dollar · rare · earths) | 977 | 2,599 | 5,690 | **3.00** |
| refining (refinery · refineries · distillate · diesel) | 128 | 345 | 747 | **2.99** |
| **oil/Hormuz (Hormuz · strait · tanker)** | 321 | 758 | 1,978 | **2.83** |
| **AI-capex (datacenter · capex · hyperscaler · Stargate)** | 246 | 676 | 1,707 | **2.52 — the lowest** |

⚠⚠ **The ratios are ~3.0 for almost everything, and that is a POOL property, not a bucket property**:
the 7-day window contains two weekend days at a third of the weekday article rate, so a weekday's
share is mechanically ~3× the window average. **What is legible is the dispersion, and it is tiny
(2.52–3.06).** **No bucket is running away from the pool.**
★★ **And for a third consecutive measurement, the day's single largest event does not rank first on
term velocity**: oil/Hormuz owns the head cluster at **17 outlets** and sits **second-lowest** on
front-loading. **This is C6's mechanism** — the desk logged it originally on `capex cut`, and it
reproduces on the opposite kind of event (loud, not silent).

★ **A correction available here, and it goes the desk's way.** `coverage tariff --days 7 --scope
foreign` reports **title+summary recall 15.2% / body-blind 84.8% 🔴**. That 84.8% belongs to the
**`search`** instrument, **not** to this bucket table: `fts search tariff --days 7 --mode or` returns
**1,449** against `coverage`'s reachable union of **1,450 — 99.9%**. ⇒ **the 7-bucket sweep, on `fts`
with explicit OR, is body-inclusive and is NOT the blind instrument.** Stated so a future run does
not discount its own numbers by 6×.

### D-4 · Blind-spot pass (`blindspot --days 2 --scope foreign`)

Pool **9,594** articles / 2 days, random sample 400. Emergent-token ranking is dominated by the
**D10** earnings boilerplate (**Earnings 1,421 · Highlights 368 · Results 360 · Presentation 172**).
**Filtered, the ranking is:**

**Trump 231 · China 210 · Iran 160 · Fed 151 · SpaceX 138 · Hormuz 135 · Energy 127 · Bitcoin 110.**

★★ **`SpaceX` is again a top-5 non-boilerplate token — 138, above `Hormuz` — while
`CATALYST_WATCH.json`'s `[STRUCTURAL]` block is EMPTY and `S56` settles on the SPCX unlock on
08-11.** **`D18`, second consecutive run with a number attached.**

### D-5 · The events that move something, read at body level

| Event | Reach | Why it is here |
|---|---|---|
| **IRGC names the reopening conditions** — *"Iran will reopen the Strait of Hormuz once the US accepts its conditions"*; conditions are **an end to the US naval blockade** and **compensation for war damages**; ★ **"the reopening does NOT depend on how talks with Oman develop"** | `[dw body 08-08]` + `[aljazeera body 08-09]` | **S8's object, named for the first time in nine runs** (P41) |
| **VP Vance: Iranian leaders *"told us they have no plans to toll the Strait of Hormuz"*** | `[aljazeera body 08-09]` | **contradicts a leg P40 carried as live** (P41) |
| *"Stock futures mixed as hopes for Hormuz reopening fade after Iran raised additional demands"* | `[seekingalpha body 08-10]` | today's direction |
| **Ukrainian drone strike kills 12 in a major attack on a Russian refining hub**; earlier **fire at Russia's Ilsky refinery** | `[oilprice body 08-10]` · `[bloomberg 08-08]` · `[hellenicshipping body 08-07]` | **distillate supply, physically attacked** (P42) |
| **Houthis attack a Saudi refinery** — *"Fire erupts at Saudi Aramco's Jazan refinery"* — after the kingdom signed a defence pact | `[scmp body]` · `[euronews body]` · `[zerohedge]`, 08-09, 67 hits/3d | **second physical distillate-supply event in four days** (P42) |
| **Apple is testing China's CXMT memory chips for iPhones and MacBooks** (WSJ-sourced), *"amid AI-fuelled supply crunch"*; separately **CXMT cleared DDR5-8800 on an AMD platform, "closing the gap with SK hynix"** | `[wsj via yahoo_finance bodies 08-09/08-10]` · `[tomshardware body 08-08]`, **43 hits/3d, 5+ outlets** | **a supply-side axis the desk's regime call does not model** (P43) |
| **Newmont pays Barrick $1.95bn; Nevada JV disputes settled; Newmont consents to Barrick's NA IPO** | `[globenewswire PR + nasdaq body + wsj + mining, 08-10]` | **§C-1 — the carrier of S57's observable** (P44) |
| **Intel plans a $15bn share sale as the turnaround rally lifts the stock** | 15/7 | IT supply/dilution, un-owned by any bracket |
| **TSMC sales +45%; TSMC and Sony to invest billions in advanced chips** | 16/6 | AI-compute demand confirm |
| *"AI data center bans surge past 500 nationwide as local US [opposition grows]"* · *"Data-Center Backlash Leads to a New Land Rush in Texas"* · *"Amazon's new 7.65 GW Texas AI data center power plant"* | 2/2 each, BUILDING | the behind-the-meter mechanism the desk logged on Project Kilby, broadening |
| **BOJ summary flags upside price risks and a possibly faster hike path** | 13/8 | global duration |
| **ADNOC Gas unveils an $8.2bn expansion** | 13/6 | gas supply, against a 1st-percentile spec short |

---

## §E · Propositions — falsifiable, both branches, mandatory anti-signal

> ID counters checked at write time (D137). **HANDOVER took `D227`–`D232` (four rescued, two new).**
> **This stage takes `M560–M572` and registers NO new dig and NO new bracket** — **PREMORTEM owns
> registration** and must apply the `D216` σ-distance test before freezing anything.

### P41 — ★★★ Hormuz: the reopening condition is NAMED for the first time, and it is NOT the Oman deal

- **Claim** `[measured, news — primary participant quoted]`: the IRGC has stated the Strait reopens
  **once the US accepts its conditions**, and named them: **an end to the US naval blockade** and
  **compensation for war damages** `[dw body 08-08 · aljazeera body 08-09]`. **The same statement says
  the reopening does not depend on the Oman talks.**
- ★★★ **This retires a mechanism the desk has been watching since 08-05.** Every carried framing —
  *"Iran says reached a deal with Oman on Hormuz" (08-05, 18 outlets)*, *"deal in final stage" (08-06)*,
  *"Iran says Hormuz deal close" (08-08)* — treated **the Oman track as the path to reopening.** The
  party that controls the Strait says it is not. ⇒ **watching the Oman track is watching the wrong
  object** (the R46 class, restated on a live axis).
- **Direction A (conditions get met or dropped, ~40%)**: a US blockade stand-down is an observable,
  dated event; crude falls further, **S54's airline-beneficiary branch becomes the live object**, and
  the rate-hike-odds channel keeps working.
- **Direction B (the conditions bind, ~60%)**: *"hopes fade after Iran raised additional demands"*
  `[seekingalpha 08-10]` and the price thread re-accelerated **6 → 7 → 17 outlets** over three days.
  **S61's tanker leg and the whole ENRG complex stay bid.**
- **Track KPI**: (i) any dated US statement on the naval blockade; (ii) the oil/Hormuz thread's outlet
  curve (**17 today**); (iii) **S61's EW{STNG, FRO} 5-session excess, −4.184 settled**.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** an **unconditional** Iranian reopening statement —
  which is exactly S8's registered trigger — kills B; **(b)** a strike on a transiting VLCC, or a
  formal US refusal of the two named conditions, kills A.
- 🚨 **What this does for `S8`**: S8 has been undated `[blank]` and un-scoreable for **nine** runs.
  **Its observable now exists** — an unconditional "Strait open" statement, against a public,
  conditional one whose two conditions are named and checkable. **MACRO does not re-register (P4 /
  stage ownership); PREMORTEM is handed the object.**
- **Catalyst**: undated `[news👁 🔀binary]` — recorded as `[blank]`, **not guessed.**

### P42 — ★★ The distillate mechanism was withdrawn on 08-07, and the physical supply axis has been attacked TWICE since

- **Claim** `[measured, news + settled prices]`: the desk withdrew **P4⁗** when dist−gas compressed on
  two consecutive settles, and **P38** left Energy's N+ resting on flow alone. **In the four days
  since, two named refining assets were physically hit**: a **Ukrainian drone strike on a Russian
  refining hub (12 killed)** `[oilprice body 08-10]`, preceded by a **fire at the Ilsky refinery**
  `[bloomberg 08-08]`; and a **Houthi drone strike on Saudi Aramco's Jazan refinery** `[scmp ·
  euronews · zerohedge, 08-09]`.
- **Direction A (the withdrawal stands, ~45%)**: refinery strikes are a recurring feature of this
  window and have not held the crack — **the refining bucket is at 2.99 on front-loading, mid-pack**,
  and the 3-2-1 spent four sessions under the carried 60 line last week. **The compression continues
  and Energy's N+ has no macro carrier.**
- **Direction B (the release was a gasoline event and supply is re-tightening, ~55%)**: the
  compression came from **gasoline rising while distillate was flat** (M545, rescued), which is a
  milder statement than *"the bottleneck ended"* — and **into Monday, distillate is outrunning crude
  +4.39% vs +1.71%**, moving **S55's observable +0.318 → +3.097 on the live bar.**
- **Track KPI**: **S55's HO%−CL% at the 08-11 settle** (branch B ≥ +6.5, branch A ≤ −3.0; settled now
  **+0.318**), the dist−gas spread, and **S67's refiner median RS20 (+3.852, all three legs positive)**.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** if the **08-11 settle** brings the spread back
  toward/below zero, the live-bar move was an overnight risk premium and B is wrong; **(b)** if
  distillate falls **while gasoline holds** on a settled close, A is the correct reading.
  ⚠⚠ **P4⁗ stays withdrawn either way** — a threshold moved after the fact is a description, not a
  forecast (L3). **This proposition does not un-withdraw it and must not be read as doing so.**
- ⚠ **This is a LIVE-BAR-informed proposition and says so.** The settled evidence is two news events;
  the price leg is unsettled and quarantined in §C-2.
- **Catalyst**: **S55 settles 08-11 · S67 settles 08-13.**

### P43 — ★★★ CXMT is a supply-side axis the regime call's own asymmetry does not cover

- **Claim** `[measured, news — WSJ-sourced, 5+ outlets, 43 hits/3d]`: **Apple is testing CXMT memory
  chips for iPhones and MacBooks** *"amid an AI-fuelled supply crunch"* `[wsj via yahoo_finance
  bodies 08-09/08-10]`, and **CXMT cleared DDR5-8800 on an AMD platform, described as closing the gap
  with SK hynix** `[tomshardware body 08-08]`.
- ★★★ **Why this is a new axis rather than another datapoint.** `STANDING_VIEW §4` states the
  governing asymmetry as **"a hyperscaler capex CUT changes the thesis; a capex RAISE only moves its
  timing"** — a **demand-side** asymmetry. **M7** dates new supply as **SK M15X + Micron Idaho
  mid-2027, Samsung P5 2028.** **A qualified Chinese DRAM supplier at a tier-1 Western OEM is neither
  leg**: it is supply arriving from a source the chain does not model, at a date the chain does not
  carry. ⇒ **the regime call (§1) is exposed on a third side, and no bracket touches it.**
- **Direction A (qualification is slow and narrow, ~60%)**: Apple *testing* is not Apple *buying*;
  DDR5-8800 is not HBM; the AI-server bottleneck (HBM, advanced packaging) is untouched, so **M1's
  price-deceleration path is unaffected and this is a consumer-DRAM story.**
- **Direction B (this is the supply answer arriving early, ~40%)**: the article's own framing is that
  **the shortage is pushing Apple toward CXMT** — demand pull, not political push — and a qualified
  second source at scale **caps the LTA floor that C1's open contradiction rests on.**
- **Track KPI**: (i) any **Apple or CXMT filing/confirmation** (not press); (ii) **MU's revision
  breadth**, carried at FY **29↑/1↓, +26.7%/90d**; (iii) whether the item reaches **HBM** rather than
  commodity DDR5.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** a named CXMT HBM qualification at any hyperscaler
  kills A; **(b)** an Apple statement, or a Micron/SK LTA disclosure with a floor, that shows the
  price term is unchanged kills B.
- ⚠ **`[news]` grade, second-hand (WSJ via aggregators).** **No issuer filing exists** — the same
  grading M122 carries. **It may not be cited as a measurement of supply.**
- **Catalyst**: `[blank]` — **not guessed.**

### P44 — ★★★ Materials' only live falsifier is 85% one name, and that name's driver is a JV settlement

- **Claim** `[measured — settled prices + issuer press release]`: **XLB exc5 = +1.31 and NEM alone is
  +17.05pp of excess**; on M502's decomposition **NEM contributes +1.113 of the +1.307**, i.e. **~85%**.
  **Today Newmont disclosed that it will pay Barrick $1.95bn** to settle the Nevada Gold Mines
  disputes and **consented to Barrick's North American IPO** `[globenewswire + nasdaq body]`.
- **Direction A (S57's branch A fires and means nothing about Materials, ~60%)**: a 0.59pp gap on an
  observable **85%-carried by a name in an M&A/JV event** clears on idiosyncratic flow. **S57-ANNEX's
  registered concern becomes a dated fact rather than a caution.**
- **Direction B (there is a real sector leg underneath, ~40%)**: the **dollar** is the one non-NEM
  mechanism — UUP **−1.13%/20d** with the COT spec long at the **81st percentile and BUILDING** — and
  **copper sits at the 100th percentile**. If XLB holds while NEM gives back the settlement pop, the
  sector leg is real.
- **Track KPI**: **XLB exc5 (+1.31)**, **XLB exc5 ex-NEM (+0.194 at last measurement)**, **UUP**, and
  **`DTWEXBGS` the moment it prints** (6 publication days stale).
  ⚠ **UUP is a DXY-basket proxy and `DTWEXBGS` is the BROAD trade-weighted index — different objects;
  no UUP value is substituted for a `DTWEXBGS` value (D1/D2).**
- ⚠ **Mandatory anti-signal, both sides**: **(a)** if XLB's ex-NEM excess turns positive on a settled
  close, A is wrong and there is a sector leg; **(b)** if NEM gives back the move and XLB falls with
  it, B is wrong and the sector reading was one name throughout.
- **Catalyst**: **S57 settles 2026-08-12 · CPI 2026-08-12.**

### P45 — ★★ The dollar's narrative and its positioning point opposite ways, and the desk's own instrument is blind

- **Claim** `[measured, prices + news + COT]`: the feed carries *"Dollar near two-month trough as US
  inflation data awaited"* (**15 articles / 5 outlets**, a REIGNITED thread) against settled **UUP
  −0.35%/5d, −1.13%/20d**, **FXY +2.64%/20d** and **FXE +1.31%/20d** agreeing in sign (**D5**) —
  while the **COT spec long is at the 81st percentile and ADDED +5,302.** **`DTWEXBGS` has not printed
  since 2026-07-31.**
- **Direction A (a crowded long unwinding, ~55%)**: the position is the marginal seller ⇒ dollar
  weakness extends, supporting **P44's branch B** and the metals complex independently of rates.
- **Direction B (this is rate-cut repricing and reverses with CPI, ~45%)**: a hot 08-12 CPI reprices
  September, the dollar recovers, and **P44-B loses its non-NEM leg.**
- **Track KPI**: **UUP**, **`DTWEXBGS` on print**, and the **08-12 CPI**.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** if UUP rises while the COT long keeps building, A
  is wrong — the position is not the marginal seller; **(b)** if the dollar falls **and** copper's
  100th-percentile long unwinds together, this is **one** positioning event, not two, and P44/P45 are
  a single claim rather than two.
- ⚠ **The COT leg is a Tuesday-08-04 snapshot that pre-dates NFP** (§B). **It is context, not a trigger.**
- **Catalyst**: **2026-08-12 CPI** `[bls✓ 🔀binary]`.

---

## §F · Self-backtest — 1 scored, 3 refused, 1 rescued

| Proposition | Registered condition | Settled outcome | Score |
|---|---|---|---|
| **P40** (08-09) — *"Hormuz is genuinely two-sided, and the desk's own bracket for it is un-scoreable"* | anti-signals: (a) a dated signed reopening kills B · (b) a confirmed closure or a VLCC strike kills A | ★ **Neither anti-signal fired. The two-sidedness HELD** and gained primary content (§D-5). ⚠ **But one leg P40 named as live is contradicted**: P40 cited *"a joint industry open letter opposing compulsory tolls"* as evidence for B, and **VP Vance states Iran told the US it has "no plans to toll the Strait"** `[aljazeera body 08-09]` | **HALF** — thesis holds, one named leg refuted |
| **P37** (08-09) — the hike is being re-timed | Track KPI = **`DGS2` at the first FRED close covering 08-07** | **blocked — the print does not exist (§A-1)** | **UNSCOREABLE** — not scored |
| **P38** (08-09) — the distillate mechanism is withdrawn | Track KPI = dist−gas · 3-2-1 level · S55's spread | **no new settled bar**; its anti-signal (b) becomes testable at tonight's settle | **UNSCOREABLE** — carried into **P42** |
| **P39** (08-09) — the dollar falls while its spec long builds | Track KPI = UUP · `DTWEXBGS` on print | **UUP reproduced exactly (C1); `DTWEXBGS` still 07-31** — no new observation | **UNSCOREABLE** — carried into **P45** |
| ★ **P4⁗** (08-07), rescued | anti-signal = dist−gas compressing on two consecutive settles ⇒ **withdraw** | fired **08-06 (−0.584)** and **08-07 (−1.109)**; the 08-08 run did not score it; the 08-09 run scored it **and its carry was lost (`D229`)** | **WITHDRAWN — re-recorded so the withdrawal survives this time** |

**Running hit-rate, appended.** ⚠⚠ **This run adds ONE scored row and refuses three, and the refusal
is the discipline, not the failure.** Three consecutive runs on one bar can only produce hits by
counting one observation many times — **the exact defect `D227` found inside the IC ledger.** ★ **And
`D227-KR` warns from the other side**: a proposition of the form *"two instruments disagree"* is
almost always true and cannot MISS. **P41 · P42 · P43 · P44 · P45 each name a settlement point at
which one side is wrong**, and P40 is scored HALF **with the refuted leg named** rather than waved
through.

---

## §G · ★ Sector transmission matrix — all 11 GICS. **This is ROTATION's input.**

🚨 **The inherited line is `2026-08-08/SECTOR_ROTATION.md §1 + §2` (the POST-delta verdict)** — the
08-09 run established that reading it from a MACRO §F reproduces a known error, and the 08-09 run's
own carry was lost, so **this is inherited from the last COMPLETED run's ROTATION, verified on disk.**

**Inherited:** `INDU OW− · ENRG N+ · FIN N+ · IT N · HLTH N · DISC N · MATR N− · COMM UW · UTIL UW ·
STPL UW− · RE UW` — **one overweight on the board and it is OW−.**

| # | Sector | Wind (this stage) | Driving prop | Numbers (settled 08-07, bench SPY) |
|---|---|---|---|---|
| 1 | **Industrials** | **OW− held** | — | exc1 −0.38 · exc5 −0.54 · exc20 −0.63 · **exc60 +1.46**. The only sector with a positive 60-day and three negative shorter windows — **a decaying stock, not a live lead (M149's class)** |
| 2 | **Energy** | **N+ held; its macro carrier is CONTESTED, not absent** | **P41 · P42** | **exc5 −6.95, worst of 11**, vs exc20 +1.97 — an **8.9pp** two-window gap. ★ **New today**: two physical refinery strikes and a named Hormuz condition set. **The mechanism is live again but unsettled** |
| 3 | **Financials** | **N+ held** | — | exc1 −0.97 (10th of 11) · exc5 −2.35 · exc20 +0.97 · exc60 +6.92. 2s10s **+0.44**, 24bp from the line that kills the NIM mechanism. **S65 settles 08-11 · S51/S66/S70 blocked** |
| 4 | **Information Technology** | **N held** | **P43** | **exc5 +3.69 = best sector on the week** against exc20 −1.25 — **the two windows disagree in sign.** ★ **New today: CXMT/Apple is a supply-side item no bracket owns** |
| 5 | **Health Care** | **N held** | — | **exc60 +8.84 = the board's best 60-day** with exc5 −1.59 — the INDU shape with the short window inverted |
| 6 | **Consumer Discretionary** | **N held** | — | exc1 +0.88 · exc5 −0.26 · exc20 −0.19 · exc60 −3.42 — **≈ zero on every window (C3: no signal, not a neutral verdict)** |
| 7 | **Materials** | **N− held** | **P44 · P45** | exc5 **+1.31** · exc20 +1.45, against GLD +7.25%/5d and SLV +9.82%/5d. 🚨 **S57 branch A fires at any settled close through 08-12 and is 0.59pp away — and 85% of the observable is NEM, whose driver printed today as a $1.95bn JV settlement.** **ROTATION may not make a MATR call on the aggregate** |
| 8 | **Communication Services** | **UW held** | — | exc1 −0.55 · exc5 −0.73 · exc20 −2.77 · **exc60 −8.73 — negative on all four windows, the only sector that is.** ⚠ **R56 binds: any breadth claim re-derived ex-EA; EA is still in the universe** |
| 9 | **Utilities** | **UW held** | — | exc5 −5.18 · **exc20 −6.39, worst on the board.** S62 FIRED-B but **DEGENERATE** (branch A 19.16pp away, D206) ⇒ **the fire is not evidence.** ★ Feed carries **500+ local AI-datacenter bans** and a 7.65 GW Texas project — the behind-the-meter mechanism broadening |
| 10 | **Consumer Staples** | **UW− held** | — | exc5 −3.43 · exc20 −1.24. Demoted 08-08 on the worst eqflow **and** the worst Δ. **Never deep-dived in recorded history** |
| 11 | **Real Estate** | **UW held** | — | exc5 −3.71 · exc20 −1.23. S25 pre-declared zero-information (D122) |

⚠⚠ **NO VERDICT CHANGE IS PROPOSED BY THIS STAGE, and the reason is stated rather than implied**:
every **price** input above is the same settled bar the 08-08 verdicts were set on, and a delta
computed from an unchanged observation is not a delta. ★ **What IS new is non-price** — the Hormuz
condition set (ENRG), the CXMT item (IT), the NEM disclosure (MATR) — **and those are handed to
ROTATION as arguments, not as deltas.** **ROTATION owns the decision.**

---

## §H · Catalysts injected at run start

`catalyst_calendar.py --days 10` → `llm_outputs/2026-08-10/CATALYST_WATCH.json`

| When | Event | Axis | Type |
|---|---|---|---|
| 🚨 **D-2 · 2026-08-12 08:30 ET** | **July CPI** | inflation | 🔀binary `[bls✓]` |
| **D-3 · 2026-08-13** | **July PPI** | inflation | 🔀binary `[bls✓]` |
| **undated** | Iran *"Strait of Hormuz open"* statement | oil | 🔀binary `[news👁]` |
| ⚠ D-0 · 2026-08-10 | "VST earnings" | power | 🔀binary — **STALE, see below** |

🚨🚨 **THE ≤48h CLAUSE IS TRIGGERED.** CPI releases **2026-08-12 08:30 ET**, which is **47h12m** from
this stage's 09:18 ET clock. ⇒ **PREMORTEM MUST produce a both-sides bracket on CPI. A one-way tilt
into it is a protocol violation**, and this run has **eight rows settling 08-12–08-13** whose readings
CPI moves (S13 · S24 · S26 · S41 · S42 · S57 · S59 · S61 · S72 · then S46 · S63 · S64 · S67 · S68 ·
S69 · S71).

⚠ **The `[EARNINGS]` block's ONLY row is wrong, and this is a new shape of `D18`.** It lists **VST
earnings at D-0 (2026-08-10)**. **VST reported on 2026-08-07** — `[nasdaq body: "Vistra Q2 26 Earnings
Conference Call At 10:00 AM ET", Fri 08-07]`, plus three follow-up notes dated 08-07/08-08/08-09 —
and **R58 already retracted the desk's "VST reports AMC" carry for the same reason.** Previous runs
recorded this block as **empty**; today it is **populated with a pattern-estimate for an event three
days past**. ⇒ **an empty block and a wrong block fail the same way, and the wrong one is worse
because it looks like coverage.**
🚨 **`[STRUCTURAL]` is EMPTY for a third consecutive run**, so the **SPCX unlock that `S56` settles on
08-11 is invisible to the desk's own schedule** while `SpaceX` ranks **#5 (138)** in the blind pool.

---

## §I · New facts registered by this stage

> ⚠ **`M544–M559` were consumed by the KR runs of 08-09/08-10 while the orphaned 08-09 US MACRO also
> claimed `M544–M552`.** Those nine US facts are **re-registered at M560+ at writeback with their
> original text and a note that their first numbering was lost** (HANDOVER §11). This stage's own new
> facts start after them.

| # | Fact | Value | Source | asof |
|---|---|---|---|---|
| **M569** | ★★★ **The IRGC named the Hormuz reopening conditions, and excluded the Oman track** | reopening *"once the US accepts its conditions"* = **end of the US naval blockade + compensation for war damages**; explicitly *"does not depend on how talks with Oman develop"* | `[dw body 08-08]` + `[aljazeera body 08-09]` | 2026-08-08/09 |
| **M570** | ★★ **A US-official statement contradicts the toll leg the desk carried** | VP Vance: Iranian leaders *"told us they have no plans to toll the Strait of Hormuz"* | `[aljazeera body 08-09]` | 2026-08-09 |
| **M571** | ★★★ **Newmont pays Barrick $1.95bn; the WSJ headline reads the cash the other way** | NEM contributes excluded properties to Nevada Gold Mines, settles all disputes, **consents to Barrick's NA gold IPO**, and **pays $1.95bn**. Headline: *"Barrick Mining Settles Newmont Nevada Dispute for $1.95 Billion"* | `[globenewswire PR + nasdaq body + wsj + mining]` | 2026-08-10 |
| **M572** | ★★★ **NEM is ~85% of S57's observable, measured on this run's own settles** | NEM **exc1 +6.55pp · exc5 +17.05pp** vs SPY (absolute +7.16% / +20.56%) against **XLB exc5 +1.31**; M502's ex-NEM figure is **+0.194**. ✅ **NEM +7.16% and Barrick +5.58% reproduce the nasdaq body's own figures to 2dp (D5)** | own calc, settled yfinance + `[nasdaq body]` | 2026-08-07 |
| **M573** | ★★ **Apple is testing CXMT DRAM, and CXMT cleared DDR5-8800 on an AMD platform** | 43 hits / 3d, 5+ outlets; *"amid AI-fuelled supply crunch"*; tomshardware: *"closing the gap with SK hynix"*. ⚠ **`[news]`, WSJ via aggregators — no issuer filing** | `[wsj via yahoo_finance bodies]` · `[tomshardware body]` | 2026-08-08/10 |
| **M574** | ★★ **Two physical refining assets were struck in four days** | Ukrainian drone strike on a Russian refining hub, **12 killed**; fire at Russia's Ilsky refinery; **Houthi drone strike on Saudi Aramco's Jazan refinery** after the kingdom signed a defence pact | `[oilprice body 08-10]` · `[bloomberg 08-08]` · `[scmp/euronews bodies 08-09]` | 2026-08-08/10 |
| **M575** | ★★★ **`D212` is a three-series pattern with a shape** | 08-07 prints: **`T10YIE` 2.25 · `RRPONTSYD` 1.45 · `SOFR` 3.62**. Stops 08-06: the **entire H.15 constant-maturity block and both ICE BofA OAS series**. **`T10YIE ≡ DGS10 − DFII10`** | `[FRED]` via `module_macro_us --json` | 2026-08-10 09:1x ET |
| **M576** | ★★ **The bucket sweep is NOT the body-blind instrument, and the measurement separates them** | `coverage tariff` d7 foreign: title+summary **221 = 15.2% recall**, reachable union **1,450**; **`fts search tariff --mode or` returns 1,449 = 99.9% of the union.** The 84.8% blindness belongs to `search`, not to `fts` | own paired measurement | 2026-08-10 |
| **M577** | ★ **Term velocity again fails to rank the day's largest event** | oil/Hormuz owns the head cluster (**30 articles / 17 outlets**) and is **2nd-lowest of 7** on d1-vs-d7 share (**2.83** vs a 2.52–3.06 range); AI-capex is lowest at 2.52. Pool: d1 **2,209** / d7 **38,565** | `fts search --mode or` × 7 buckets + `coverage` | 2026-08-10 |
| **M578** | ★ **The `[EARNINGS]` block is now wrong rather than empty** | `CATALYST_WATCH.json` lists **VST earnings D-0 2026-08-10**; VST reported **08-07** (`[nasdaq body]`, and R58 already retracted the same error). `[STRUCTURAL]` empty a 3rd run while **`SpaceX` ranks #5 (138) in the blind pool** and **S56 settles 08-11** | `catalyst_calendar.py --days 10` + `blindspot` + news | 2026-08-10 |
| **M579** | **The foreign single-source tier is UNSCORED, not low-scored, and it is 446 clusters** | 2,209 articles → 349 events; **single_source 446, shown 15, scored 0, scorable 0** — the relevance classifier is Korean-only ⇒ on `--scope foreign` this tier is a **random sample**. **431 unopened** | `brief --scope foreign --body 2` | 2026-08-10 |

**New digs: none by this stage.** (HANDOVER registered D227–D232.)
**New brackets: none.** **PREMORTEM owns registration** and must apply the **`D216`** σ-distance test
— flagging both `>3σ` (unreachable) and `<0.25σ` (inevitable) — before freezing anything, **and must
bracket CPI both ways (§H).**

---

## ✅ EXIT CHECK

- [x] **Catalysts injected** (`--days 10`, beyond the default because `SCENARIOS` names 08-11/08-12/08-13) → `CATALYST_WATCH.json`; **the ≤48h clause is TRIGGERED by CPI (47h12m) and handed to PREMORTEM**; indicators read (`module_macro_us --json` + `us_flow --cot`); **daily anchor read** = the 08-09 `MACRO_REPORT.md` **and** the 08-08 `SECTOR_ROTATION.md` (§G inherits from the latter, deliberately)
- [x] **Events read via `brief --body 2`**, `--scope foreign`; **tail = 0**
- [x] **`tail = 0` is NOT the coverage claim**: `single_source` **15 shown of 446** — and the module states the 446 are **UNSCORED**, not low-scored — · `excluded_nonmarket` **0 of 0** · `subevents_recovered` **70**. **431 single-outlet clusters were not opened and every "quiet" statement in this report carries that number**
- [x] **Denominator corrected**: **2,209 articles → 795 clusters → 349 events**, non-market **0**, `excluded_not_news` **{}**
- [x] **Trajectories read** (`thread --days 7`); every proposition names its thread's curve; ⚠ **FADING tags are declared partly calendar-driven** (two weekend days at ~1/3 the weekday rate) **and only per-day outlet curves are cited** — including the one that contradicts its own tag (oil/Hormuz **6 → 7 → 17**)
- [x] Every "nothing in bucket X" claim carries its denominator — **and no such claim is made this run**
- [x] **No bucket's count trusted at the default**: all seven buckets run with an explicit **`--mode or`** (the rescued `D230`), single-token argv, and the `fts`-vs-`search` recall difference measured rather than assumed (**M576**)
- [x] **Both halves cited on every headline print**: NEM **+7.16% 1-session** *and* **+20.56% 5-session**; the Newmont/Barrick item cited with **who pays whom**, not the headline; CXMT cited as **testing**, not buying
- [x] **Every relative-performance number names its benchmark inline (SPY)**; no cross-market statistical transfer (W1)
- [x] **Credit axis cited**: HY OAS **2.71** (39bp from S26's line) · IG **0.78** (6th unchanged print) · NFCI **−0.529**. **No credit-stress claim is made, and any risk-off reading would be narrative-only**
- [x] **`real_10y` quoted with `breakeven_10y`**: **2.43 (08-06)** vs **2.25 (08-07)** — ⚠ **one day apart, so the 08-07 real-vs-inflation decomposition is `unknown` (C3)**
- [x] **Linter run on this stage's own output**
- [x] **Transmission matrix produced, all 11 sectors**, inherited from the last COMPLETED run's post-delta ROTATION line
- [x] `MACRO_REPORT.md` written; **self-backtest appended (1 scored HALF · 3 refused as unscoreable · 1 withdrawal rescued)**; new blind-spot terms folded back
- [x] **No position sizing, no buy/sell language (P4)**
