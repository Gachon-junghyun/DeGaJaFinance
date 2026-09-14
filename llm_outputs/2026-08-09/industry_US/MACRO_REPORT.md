# MACRO_REPORT — industry_US · 2026-08-09 (Sun) · Stage 2/10 (L1·MACRO)

> Analysis only — zero buy/sell, zero position sizing (P4-principle). English-pure runtime.
> Every price object below is a **settled 2026-08-07 close**, verified by pulling the bar
> (`last bar: 2026-08-07`) rather than assumed. **D74 contamination = 0.**

## ⚠⚠ THE CAVEAT THAT GOVERNS EVERY NUMBER BELOW

**There has been no US session since the 08-08 run.** Same settled bar, same FRED `asof` (08-06 for
the yield/credit block). ⇒ **every price and rate number in this report is the SAME OBSERVATION the
08-08 run used — n = 1, not 2 (S1).** They are re-derived here from source rather than inherited
(C1), and they **reproduce**; they are not a second measurement.

🚨 **And the news feed is worse than flat: `2026-08-09` has ZERO foreign articles.**

| market_day | foreign articles | events |
|---|---|---|
| 08-05 | — | 844 |
| 08-06 | — | 812 |
| 08-07 | 5,178 | 701 |
| **08-08** | **1,855** | **274** |
| **08-09 (today)** | **0** | **0** |

⇒ **the US-pure desk has no same-day news at all.** This report's news axis therefore reads
**2026-08-08**, which is genuinely new — the 08-08 run executed at **09:10 ET Saturday** and could
only have seen a fraction of its own day. ⚠ **`--scope all` shows 262 articles for 08-09, all of
them domestic-classified**, which is why the KR desk had a day and this one does not.

⇒ **The correct output of a second closed-market run is a near-zero verdict delta.** What this run
produces instead of a manufactured delta: **four scoring/verification jobs the 08-08 run left open**,
two of which change a carried proposition.

---

## §A · ★★★ The job the last run left open: **P4⁗'s anti-signal FIRED and was never scored**

The **2026-08-07** run wrote, in advance:

> *"**P4‴'s registered anti-signal requires TWO consecutive compressions.** ⇒ **HALF-FIRED. One more
> and P4‴ is withdrawn.** Tonight's settle decides it — **stated in advance, not after.**"*

**Tonight's settle was 2026-08-07.** The 08-08 run had it. **Its §H self-backtest scored six
propositions — P29 · P30 · P31 · P27′ · P28′ · P1⁗ — and P4⁗ is not among them.**

**Measured now, settled daily closes, one instrument (yfinance `CL=F`/`RB=F`/`HO=F`, `auto_adjust=False`):**

| date | distillate crack | gasoline crack | **dist − gas** | Δ |
|---|---|---|---|---|
| 2026-08-03 | 82.502 | 44.261 | 38.241 | +0.445 |
| 2026-08-04 | 82.591 | 44.022 | 38.569 | +0.328 |
| 2026-08-05 | 84.220 | 44.010 | **40.211** | +1.642 |
| 2026-08-06 | 85.754 | 46.127 | **39.627** | **−0.584** ← compression 1 |
| **2026-08-07** | 85.721 | 47.203 | **38.518** | **−1.109** ← **compression 2, and LARGER** |

> ### **`P4⁗` · 2026-08-07 · WITHDRAWN by its own registered anti-signal.**
> **Two consecutive settled compressions of the distillate-minus-gasoline spread**, the second
> **1.9× the first.** The pre-commitment was written before the settle and the settle went against it.

★ **Why this is the run's most useful output**: the L2·carryover text names this exact failure —
*"an armed condition that nobody re-reads is an idea the desk paid for and never collected."*
**This one was armed by one run, inherited by the next, and dropped.** ⇒ **`D229`.**

⚠ **Scope discipline (C4).** This withdraws **the distillate-bottleneck leg's continuation**, i.e.
the claim that the widening dist−gas spread was the live mechanism. It does **not** assert the
opposite mechanism, and it does **not** by itself change a sector verdict — the 08-08 run had already
demoted Energy **OW− → N+ on flow alone**, explicitly declining the macro argument as a carrier.
**What changes is that the mechanism leg the desk was holding in reserve is now gone**, so the N+ is
carried by flow and by nothing else.

### A-1 · ★★ And a second, unrecorded crossing on the SAME complex: the carried 60 kill line

**M235 is carried in `STANDING_VIEW_US.md` and quotes *"P4's buffer to the 60 kill line: 4.30 → 8.12
→ 12.22"*.** ✅ **Estimator verified against M235's own frozen values before use (C1)** — the
formula `(2·RB·42 + HO·42 − 3·CL)/3` reproduces **64.304 (07-24) · 68.117 (07-27) · 72.219 (07-28)**
to the third decimal.

**On that verified estimator, the 3-2-1 crack has been BELOW 60 on four consecutive settled sessions
and no desk file records the crossing:**

| date | WTI | 3-2-1 crack | buffer to 60 |
|---|---|---|---|
| 2026-07-31 | 84.67 | 63.236 | +3.236 |
| **2026-08-03** | 80.34 | **57.008** | **−2.992** |
| **2026-08-04** | 75.77 | **56.879** | **−3.121** ← window low |
| **2026-08-05** | 75.22 | **57.413** | **−2.587** |
| **2026-08-06** | 77.29 | **59.336** | **−0.664** |
| **2026-08-07** | 78.18 | **60.042** | **+0.042** |

⇒ **the level crossed its carried kill line, spent four sessions beneath it, and has come back to
+0.042 — four hundredths of a point above the line.**
⚠⚠ **Two honesty constraints on this, both stated rather than glossed:**
1. **The 60 line belongs to the ORIGINAL `P4`, whose observable was a LEVEL.** Its descendants
   (`P4′`→`P4⁗`) replaced the observable with a **change** and then a **spread**. **So this is not a
   live bracket firing** — it is a **carried fact (M235) whose stated buffer is stale by 12 points and
   a sign.** It is recorded so the next run does not quote M235's buffer as current.
2. **This complex has a measured revision defect** — the 07-31 bar was revised **+3.371 points** after
   publication (`D86`/`M202`/`M236`: the futures Volume field is forward-filled *and* revised).
   **Today's 08-07 value may revise.** Quoted with that caveat, not as a settled certainty.

---

## §B · The rate axis — and the genuinely new information is that the FOMC is arguing with the data

### B-1 · `[FRED]`, this run's own pull, with the publication lag stated

| Series | Value | `asof` | vs prior print |
|---|---|---|---|
| `DGS2` | **4.25** | 2026-08-06 | 4.28 (07-31) → 4.25 → 4.20 → 4.18 → **4.25** |
| `DGS10` | **4.69** | 2026-08-06 | 4.75 (07-31) → 4.70 → 4.63 → 4.63 → **4.69** |
| derived **2s10s** | **+0.44** | 2026-08-06 | **24bp above S23/S51's ≤ +0.20 line** |
| `DFII10` (real 10y) | **2.43** | 2026-08-06 | **12bp below S9's 2.55 kill line** |
| `T10YIE` (breakeven) | **2.25** | **2026-08-07** | 2.26 (08-06) ⇒ **−1bp on the NFP session** |
| `BAMLH0A0HYM2` (HY OAS) | **2.71** | 2026-08-06 | **2.85 (07-31) → 2.71 = −14bp over the week; credit TIGHTENED into the shock** |
| `BAMLC0A0CM` (IG OAS) | **0.78** | 2026-08-06 | unchanged, 5th consecutive |
| `NFCI` | **−0.529** | 2026-07-31 | still loosening |
| `VIXCLS` | **15.15** | 2026-08-06 | 15.99 (07-31) |

★ **The real 10y is quoted with its breakeven, as the EXIT CHECK requires**: real **2.43** against
breakeven **2.25**. Over the week the nominal fell 6bp and the real fell 4bp ⇒ **~2/3 of the move is
real, ~1/3 inflation-expectation.** ⚠ **Both legs stop at 08-06 and therefore exclude the payroll
session**; the only 08-07 observable is the breakeven's −1bp, which **cannot decompose nominal vs
real** and is **not used to call the direction (C3).**

★★ **`D212` replicates, and with a SECOND series.** `T10YIE` (08-07) **and `RRPONTSYD` (08-07 = 1.45)**
both carry the business day that `DGS2`/`DGS10`/`DGS30`/`DGS5`/`DFII10`/`BAMLH0A0HYM2`/`BAMLC0A0CM`/
`VIXCLS`/`SOFR`/`DFF` all lack. **Two series, not one anomalous series** ⇒ a per-series publication
pattern, and it blocks **S66** and **S70** for a **third** run.

### B-2 · ★★★ NEW — three named FOMC voices pushed the other way inside the window

The 08-08 run's **P32** framed the 08-07 move as *"a RE-TIMING of a hike, not a pivot"* on futures
pricing (September hike **55% → 44%**, December **held at 77%**, M504). **What it did not carry is
that the committee itself was on the record, hawkish, in the same window** `[news, foreign scope]`:

| Speaker | Item | Source tier |
|---|---|---|
| **Governor Cook** | *"prepared to act"* on a rate **hike** to address inflation; backs hold but **warns a hike is possible if disinflation stalls** | **body, 2 outlets** (cnbc 2,139 chars · fxstreet 3,141) + 2 title-only (google_en, American Banker) |
| **Musalem** | the Fed *"should have hiked rates at last meeting"* | title-only `[Reuters via google_en]` |
| **Kashkari** | calls for **gradual rate hikes in 2026** | title-only `[qz.com]` |
| — | *"With Cook sending hawkish signals, a Fed rate hike is in play for September"* | title-only `[Scotsman Guide]` |

**Against them, in the same feed and also body-level**: *"Euro edges higher as weak US labor data,
lower Oil prices temper Fed hike bets"* `[fxstreet body]` · *"Swiss Franc gains as US economic data
disappoints and Fed hike bets weaken"* `[fxstreet body]` · *"Gold Extends Gain as **Hormuz Deal
Progress Lowers Rate-Hike Odds**"* `[bloomberg, title]`.

⇒ ★★★ **The reaction function is being pushed by three forces at once and two of them are not the
data**: the **payroll print** (dovish), **oil/Hormuz de-escalation** (dovish, and it is named as the
transmission channel in a bloomberg headline), and **the committee's own speakers** (hawkish).
**This is the M69 mechanism — *"pricing for rate hikes moved alongside oil"* — running a second time,
now with the FOMC leaning against it.**
⚠ **Tier discipline (C1/D10)**: only the Cook item has a body at more than one outlet. **Musalem and
Kashkari are title-only and are tagged `[title-only]`, not treated as read.**

### B-3 · July NFP, both halves (C2), with the FRED half added

| Half | Value | Source |
|---|---|---|
| Payrolls | **−23,000** vs **+80,000** consensus; June revised to **+20,000** | `[BLS via 4+ outlet bodies]` (M505, inherited) |
| **Unemployment rate** | **FELL to 4.1%** | ★ **`[FRED] UNRATE` 2026-07-01 = 4.1, from 4.2 (June) and 4.3 (Mar–May)** — this run's own pull, an independent confirmation of the inherited news figure |
| Wages | AHE **+3.2% YoY vs +3.5%** | `[BLS via bodies]` |

**Both halves point opposite ways and both are true**: the establishment survey contracted while the
household survey's unemployment rate made a **four-month low**. **A one-half quotation of this print
is not admissible as a proposition anchor**, and the hawkish-speaker cluster in B-2 is most simply
read as the committee quoting the *other* half.

---

## §C · The tape, settled 2026-08-07 — re-derived, not inherited

`yfinance`, `auto_adjust=False`, benchmark **SPY inline**, verified `last bar 2026-08-07`.
**SPY: 1d +0.61% · 5d +3.51% · 20d +2.43%.**

| ETF | exc1 | **exc5** | exc20 | exc60 |
|---|---|---|---|---|
| **XLK** | +0.81 | **+3.69** | −1.25 | +2.54 |
| **XLB** | +0.71 | **+1.31** | +1.45 | −3.37 |
| XLY | +0.88 | −0.26 | −0.19 | −3.42 |
| XLI | −0.38 | −0.54 | −0.63 | +1.46 |
| XLC | −0.55 | −0.73 | −2.77 | −8.73 |
| XLV | +0.14 | −1.59 | +0.58 | **+8.84** |
| **XLF** | **−0.97** | −2.35 | +0.97 | +6.92 |
| XLP | −0.60 | −3.43 | −1.24 | −3.95 |
| XLRE | −0.23 | −3.71 | −1.23 | −3.85 |
| **XLU** | −0.08 | **−5.18** | **−6.39** | −8.25 |
| **XLE** | −1.75 | **−6.95** | **+1.97** | −4.87 |
| *(GLD)* | +1.65 | **+3.74** | +3.27 | −12.71 |
| *(SLV)* | +2.34 | **+6.31** | +4.15 | −31.55 |
| *(UUP)* | −1.04 | −3.87 | −3.55 | −2.49 |
| *(USO)* | −1.36 | **−12.17** | +6.11 | −22.99 |

✅ **These reproduce the 08-08 run's published figures** (XLE exc5 −6.95 · XLU exc20 −6.39 · XLF exc1
−0.97 · XLB exc5 +1.31 vs its +1.307). **C1 estimator verification, discharged independently.**

### C-1 · ★★ Two things the 08-08 run did not compute, both available on its own bar

**(i) On the week, the BARREL led the energy equities — not the other way round.**
The 08-08 run's **P36** direction A read *"the war premium is deflating out of the equities **ahead of
the barrel**"* (~55%). Measured on the same settled bar, absolute 5-session returns:

| | 5d absolute | vs SPY |
|---|---|---|
| **`CL=F` (WTI)** | **−7.67%** | — |
| **`BZ=F` (Brent)** | **−7.29%** | — |
| **USO** | **−8.66%** | **−12.17** |
| **XLE** | **−3.44%** | **−6.95** |

⇒ **the barrel fell roughly twice as much as the energy equities over the week.** ⚠ **This is not a
falsification of P36-A** — P36-A is a *within-session* lead claim scored on 08-07, and USO is a
futures vehicle with its own roll and beta (**D3**: a levered proxy is a different physical variable).
**What it establishes is that on the 5-session window the ordering is the opposite of the one P36-A
describes**, so P36-A **may not be extended past its own one-session window** without re-measuring.
**Recorded as a scope constraint on a carried proposition, not as a score.**

**(ii) ★★★ The dollar leg S57 calls "dormant" is NOT dormant — the desk was only looking at the stale series.**
`DTWEXBGS` last printed **2026-07-31 = 119.7034 — six publication days ago**, which is why S57's
dollar leg is carried as dormant. But a **settled daily** proxy exists and moved:

| | 1d | **5d** | 20d | 60d | asof |
|---|---|---|---|---|---|
| **UUP** (USDX proxy) | **−0.43%** | **−0.35%** | **−1.13%** | +2.26% | 2026-08-07 |
| **FXE** (EUR) | +0.36% | +0.18% | +1.31% | −1.53% | 2026-08-07 |
| **FXY** (JPY) | +0.60% | **+1.01%** | **+2.64%** | −0.05% | 2026-08-07 |

**Two independent crosses agree with the proxy's sign (D5 satisfied): the dollar is lower on 1d, 5d
and 20d, and the yen is its strongest counterparty (+2.64% over 20 sessions).**
⇒ ★★ **Against the COT: the USD Index spec long sits at the 81st percentile and ADDED +5,302 into
that decline.** **A crowded long, still building, against a falling price on three windows** — and
the desk could not state it because it reads a series that stopped six days ago.
⚠⚠ **D2 (verify the proxy's sign) and D1 (different instrument):** **UUP tracks the DXY basket;
`DTWEXBGS` is the BROAD trade-weighted dollar.** They are **not the same object** and their levels
are not interchangeable. **What is claimed here is a direction on a settled daily instrument, not a
substitute value for `DTWEXBGS`.** The correct reading is: **S57's dollar leg is unobserved, not
inert**, and the un-observation is a tooling gap.

---

## §D · Positioning — ⚠ the COT is the SAME file the 08-08 run used

`us_flow.py --cot`, **Tuesday 2026-08-04 close, published Friday 08-07 15:30 ET. Next publication
2026-08-14.**

| Instrument | Net spec | Wk Δ | 1y %ile | Read |
|---|---|---|---|---|
| **Copper** | +77,123 | **+9,842▲** | **100%ile** | 🟢 crowded long, at the trailing-year MAXIMUM and building |
| **USD Index** | +22,499 | **+5,302▲** | **81%ile** | 🟢 crowded long, building — **against the price in §C-1(ii)** |
| **S&P 500** | −27,258 | −10,062▼ | 80%ile | 🟢 crowded long |
| UST 2Y | −1,004,228 | +120,346▲ | 65%ile | 🟡 shorts covering |
| Gold / Silver | +197,634 / +22,280 | +15,564▲ / +63▲ | 29% / 29% | 🟡 **⇒ the metals rally in §C is NOT a crowded-positioning event** |
| WTI Crude | +23,033 | +3,275▲ | **18%ile** | 🔴 crowded short |
| **Nasdaq-100** | −35,006 | −25,091▼ | **0%ile** | 🔴 the most crowded short measurable |
| **UST 10Y** | −979,243 | −103,124▼ | **3%ile** | 🔴 crowded short |
| Nat Gas | −197,546 | −6,747▼ | 1%ile | 🔴 crowded short |
| Russell 2000 | −8,899 | −7,520▼ | 26%ile | 🟡 |

⚠⚠ **Two constraints, both binding:**
1. **This snapshot PRE-DATES the 08-07 payroll print by three days.** It cannot be read as a reaction
   to it. **Nothing below cites it as a response to the NFP.**
2. **It is byte-for-byte the same release the 08-08 run quoted.** ⇒ **no cross-run positioning delta
   exists this run**, and none is claimed.

★ **One genuinely new cross-read is available without new data**: **gold and silver sit at the 29th
percentile** while **GLD/SLV are the two best excess performers on the board (+3.74 / +6.31 over five
sessions)**. **A rally at a 29th-percentile spec position is not a crowded trade** — which cuts
*against* the reflex reading of the 08-08 run's **P33** (*"the move is a rates trade wearing a
Materials label"*) being a positioning phenomenon. **P33's own mechanism (hike odds) survives; the
"crowded" framing was never in it and must not be added.**

---

## §E · News — events, trajectories, buckets, blind spot

**Denominator, corrected**: **2026-08-08 foreign — 1,855 articles → 274 events (274 market / 0
non-market)**, head tier **30**, body tier **244**, **tail 0**, **single-outlet 270 of which 15 shown**,
**94 sub-events swallowed by the 0.65 threshold**.
⚠⚠ **The coverage claim this run is entitled to make is bounded**: **255 of the 270 single-outlet
articles were not shown, and the module states those 270 are UNSCORED — the classifier is Korean-only —
so they are not low-scored, they are unmeasured.** Every "quiet" statement below carries that number.

### E-1 · The events that move a live bracket

| Event | Outlets | Which bracket / proposition |
|---|---|---|
| ★★★ **"Iran says Hormuz deal close amid attack on UAE tanker"** — sub-events: *"deal on Strait of Hormuz is close **but not enough**"* (4/4) · *"Trilateral **Mecca defence pact** signed"* (2/2) · *"**UAE says one of its ships was targeted by missile**"* (2/2) | **15 articles / 14 outlets, dispersion 0.99 — the day's #1** | **S8** (un-scoreable, 8 runs) · **S52** · **S54** · **S55** · **S61** |
| ★★★ **"Iran Says U.S. Must Meet Demands Before Strait Of Hormuz Reopens"** | **7 / 7, dispersion 1.00** — a **second, independent** head cluster on the same axis | same |
| ★★ **"US employers unexpectedly cut 23,000 jobs"** + *"How the weak jobs report could make inflation harder to manage"* | 8 / 5 | **S51 · S65 · S66 · S70 · P32** |
| ★★ **"Why SpaceX Stock Just Gained +15.8%"** | 15 / 5 | **S56** (08-06 unlock, settles 08-11) |
| ★★ **Berkshire Q2: operating profit +16% to $12.98bn, cash at a record**; **"Greg Abel's First Big Deal as Berkshire CEO Was a $6.8 Billion…"** | 9 / 7 and 13 / 8 | 🚨 **S65's BRK-B leg** — the 08-08 DRIFT addendum pre-committed to this contamination and it is now numbered |
| **"Nvidia to invest up to $3 billion in Stargate data center…"** | 10 / 5 | **S24 · S40 · S48** |
| **"Jeff Bezos' Amazon Just Raised Its AI Spending to $220 Billion"** | 3 / 3 | ⚠⚠ **`[narrated]`, NOT `[disclosed]`** — the 08-08 run's DEEP-IT established the $220bn is a **Polymarket-derived probability (62.5% odds)** carried in an opinion piece. **It is now propagating in the head tier and must keep its tag** |
| **"US announces $400m investment in Australian rare earth mine"** | 4 / 4 | **S57 / MATR** |
| **"India wary of potential 100% US tariffs over Russian oil"** · **"Ukraine Drone Strike Sparks Fire at Russia's Ilsky Refinery"** | 3 / 3 · 2 / 2 | **ENRG — refining capacity destruction** |
| **"Only 2 of These 5 Nuclear Stocks Sell Fuel Today"** · **"The AI Trade Rotation: Money Is Moving Out of Chips and Into T…"** | 5 / 4 · 6 / 4 | **UTIL · IT** |

### E-2 · Trajectories (`thread --days 7`) — ⚠⚠ **and every tag in this pass is contaminated**

**Per-day denominator: 08-03 855 · 08-04 825 · 08-05 844 · 08-06 812 · 08-07 701 · 08-08 274 · 08-09 0.**

🚨 **The unit reports `다일 522 — 살아있는 0`: ZERO live multi-day threads. All 522 are ENDED.**
**That is arithmetically forced by a window whose last day has zero articles** — the unit's own
warning (*"a holiday/low-volume window end inflates FADING"*) applies at its maximum. ⇒ **no
FADING/ENDED tag is admissible as evidence this run**, and no proposition below cites one as a
direction. **Only the per-day curves are used**, which are unaffected.

| Thread | Curve (08-03 → 08-08) | Peak outlets | Read (curve only) |
|---|---|---|---|
| **"Iran says reached a deal with Oman on Strait of…"** | **15→8→18→14→12→10** | **18** | **six days, never below 8** — sustained and oscillating, **not** monotone in either direction |
| **"Ukraine hits refineries deep inside Russia as Mo…"** | **15→14→17→20→19→12** | **20** | **six days, top-3 all week** — the refining-capacity destruction axis is the most persistent story on the board |
| "U.S. Treasury yields fall as oil prices plunge o…" | 23→22→13→14→16→6 | 23 | the rate↔oil linkage of §B-2, in the tape's own words |
| "US Loses 23,000 Jobs in July, Unemployment Rate…" | 3→21→5 | **21** | a one-day spike on the print |
| "Why SpaceX Stock Is Dropping After Earnings" | 9→18→25→14→10→5 | **25** | ⚠ **and 08-08's head reads "+15.8%"** — a violent two-way name into an **08-11** bracket |
| "Opinion \| AI Companies Need to Drill, Baby, Drill" | 17→14→11→13→8→10 | 17 | AI-power, persistent |
| **"US and Japan and yen intervention"** | 19→9→6→3 | **19** | ★ **an FX story the desk's stale `DTWEXBGS` cannot see** (§C-1 ii; FXY +2.64%/20d) |

### E-3 · ★★★ The 7-bucket sweep — and the instrument defect is the finding, again, at the source

**D214** recorded that `search` and `fts search` differ ~6× on identical terms and are **not nested**
(the AI bucket **inverted**), concluding *"they use different matching semantics on multi-word terms."*
**This run found the semantics, in the source, and they are worse than "different".**

```
module_news_data/_fts.py:198    s.add_argument("--mode", choices=["and","or"], default="and")
module_news_data/_search.py:99  p.add_argument("--match-mode", choices=["or","and"], default="or")
```

⇒ 🚨🚨 **the two instruments have OPPOSITE DEFAULTS**, and **the protocol's own L2·news text
instructs the 7-bucket sweep to be run *"FTS `--syn`, **OR-mode per bucket***"* — on the instrument
whose default is **AND**.

**Measured, `--scope foreign`, identical terms, identical windows, single-token argv:**

| bucket (terms) | **d7 with `--mode or`** | **d7 at the DEFAULT (`and`)** | OR ÷ AND |
|---|---|---|---|
| oil/Hormuz (Hormuz · strait · tanker) | **1,793** | 295 | **6.1×** |
| refining (refinery · refineries · distillate · diesel) | **690** | 37 | **18.6×** |
| rates/Fed (Fed · yields · payrolls · inflation) | **5,618** | 136 | **41.3×** |
| **AI-capex (datacenter · capex · hyperscaler · Stargate)** | **1,678** | **0** | **∞** |
| credit (spreads · default · downgrade) | **1,818** | 6 | **303×** |
| trade/tariff (tariff · tariffs · sanctions) | **1,808** | 76 | **23.8×** |
| metals/USD (copper · dollar · rare · earths) | **5,430** | 83 | **65.4×** |

**Three consequences, all measured:**
1. ★★★ **A bucket's count FALLS as its definition BROADENS.** `Hormuz` alone returns **1,599**;
   the three-term bucket containing it returns **295** at the default. **Under a union that is
   impossible.** ⇒ **every multi-term bucket count this desk has produced on `fts search` without an
   explicit `--mode or` is an INTERSECTION reported as a UNION.**
2. ★★★ **A four-term bucket can read exactly 0 while its topic is the day's news.** **AI-capex = 0**
   at the default, on a day whose head tier carries *"Nvidia to invest up to $3 billion in Stargate
   data center"* (10 articles / 5 outlets). **Its components individually return `datacenter` 77 ·
   `Stargate` 18 · `capex` 934 · `hyperscaler` 1,000.** **A silent zero on a gate is
   indistinguishable from an empty universe** — the same sentence `D219` used for `theme-age`, and
   this is the **FIFTH** tool in the class, but the **first whose mechanism is a documented flag
   default rather than quoting.**
3. ✅ **`D214` is now EXPLAINED, not just replicated** — including its strangest observation, the
   **inverted** AI bucket. Two instruments with opposite defaults produce a ratio that depends on how
   many terms a bucket has and how correlated they are; **an inversion is exactly what a 4-term AND
   against a 4-term OR produces.** ⇒ **`D230`, and the fix is one flag.**

**Corrected bucket table (all `--mode or`, one named instrument, two windows measured in the same
session so the comparison is internal, never cross-run — `D214`'s own rule):**

| bucket | d3 | d7 | d3 ÷ (d7 × 3/7) |
|---|---|---|---|
| trade/tariff | 1,039 | 1,808 | **1.34** |
| refining | 392 | 690 | **1.33** |
| metals/USD | 2,864 | 5,430 | 1.23 |
| credit | 918 | 1,818 | 1.18 |
| rates/Fed | 2,824 | 5,618 | 1.17 |
| AI-capex | 821 | 1,678 | 1.14 |
| **oil/Hormuz** | 857 | 1,793 | **1.12 — the LOWEST, on the day's #1 event** |

⚠⚠ **The share column is NOT an acceleration measurement and is not used as one.** The 3-day window
contains a day with **zero** foreign articles, so its denominator is ~2 days of content in a 3-day
box. **What is legitimate to read**: the ordering is remarkably flat (**1.12–1.34**), i.e. **no bucket
is running away from the pool**, and **the Hormuz bucket is the least front-loaded despite owning the
day's largest event** — consistent with E-2's oscillating six-day curve rather than a breakout.

### E-4 · Blind-spot pass (`blindspot --days 2 --scope foreign`)

Top emergent tokens are dominated by earnings-report boilerplate (**Earnings 2,164 · Results 594 ·
Presentation 336 · Highlights 276** — the **D10** class). **Filtering that out, the ranking is:**

**SpaceX 195** · Trump 270 · China 235 · **Fed 187** · **Energy 159** · **Iran 150** · **Hormuz 130** ·
**Jobs 128**.

★★ **`SpaceX` is the #1 non-boilerplate single name in the blind pool — above `Fed`, `Iran` and
`Hormuz`** — while **`CATALYST_WATCH.json`'s `[STRUCTURAL]` block is EMPTY**, so the **SPCX 08-06
unlock that `S56` settles on 08-11 is invisible to the desk's own schedule** while being the loudest
name in the pool it does not read. **`D18` again, and this time with a number attached.**
Other un-owned items in the random sample: **"Venezuela's Oil Production Grows at a Crucial Time"**
(an ENRG supply leg no bracket touches).

---

## §F · Propositions — falsifiable, both-branch, with a mandatory anti-signal

> ID counters checked at write time (D137): highest `M543` · `D226-KR`/`D219` · `R61` · `S72`(US)/`S57-KR`(KR).
> **HANDOVER took `D227`–`D228`. This stage takes `M544–M552` · `D229`–`D230`.** No new bracket is
> registered by MACRO; **PREMORTEM owns registration** and must apply the `D216` σ-distance test first.

### P37 — ★★★ The hike is being re-timed by TWO exogenous forces while the committee leans against both

- **Claim** `[measured, FRED + news]`: the 08-07 repricing (Sept **55% → 44%**, Dec **held at 77%**,
  M504) has **two named non-data drivers** — the payroll contraction **and** Hormuz de-escalation
  (*"Gold Extends Gain as Hormuz Deal Progress **Lowers Rate-Hike Odds**"* `[bloomberg]`) — while
  **three FOMC speakers pushed the other way inside the same window** (§B-2).
- **Direction A (re-timing survives, ~60%)**: the committee's hawkishness caps how far the front end
  can rally ⇒ **December stays ≥70% and `DGS2` does not break below ~4.10** ⇒ **duration does not get
  paid and the UW duration tilts (UTIL, RE) stay coherent.**
- **Direction B (the exogenous pair wins, ~40%)**: **a Hormuz reopening AND a soft CPI together**
  push December below 60% ⇒ **RE/UTIL underweights become the desk's most exposed calls.**
- **Track KPI**: **`DGS2` at the first FRED close covering 08-07** (blocked, `D212`), and the
  December hike probability.
- ⚠ **Mandatory anti-signal (BOTH sides)**: **(a)** an **08-12 CPI upside surprise** that re-prices
  September above 55% kills B's premise; **(b)** **a hawkish FOMC speaker retracting, or December
  printing below 60%**, kills A outright.
- **Thread**: "U.S. Treasury yields fall as oil prices plunge" peak **23 outlets**; rates/Fed bucket
  **5,618 / d7**, share **1.17**. ⚠ **All ENDED tags this run are window-contaminated (E-2) and none
  is cited.**
- **Catalyst**: **2026-08-12 CPI** `[bls✓, 🔀binary]` · **2026-08-13 PPI** `[bls✓, 🔀binary]`.

### P38 — ★★ The distillate mechanism is withdrawn, and Energy's N+ now rests on flow alone

- **Claim** `[measured]`: **P4⁗'s anti-signal fired on two consecutive settled closes (§A)**, and the
  **3-2-1 level spent four sessions below the carried 60 line and sits +0.042 above it (§A-1)**.
- **Direction A (the product-tightness leg is over, ~60%)**: dist−gas keeps compressing ⇒ the
  refining thesis's mechanism is gone and **the N+ is a pure flow call with no macro carrier.**
- **Direction B (the compression is a two-session gasoline event, ~40%)**: **gasoline crack rose
  44.010 → 46.127 → 47.203 on the two compressing sessions while distillate was FLAT (85.754 →
  85.721)** ⇒ **the spread narrowed from the GASOLINE side, not by distillate weakening** — which is
  a different, milder statement than "the bottleneck ended".
- **Track KPI**: dist−gas (**38.518**), the 3-2-1 level (**60.042**), and **`S55`'s HO%−CL% from the
  08-04 anchor (+0.318pp)**.
- ⚠ **Anti-signal (BOTH sides)**: **(a)** if **distillate itself** falls while gasoline holds, B is
  wrong and A is the correct reading; **(b)** if dist−gas expands on the next settled close, A is
  wrong and the withdrawal was a two-session artifact — **but P4⁗ stays withdrawn either way, because
  a threshold moved after the fact is a description, not a forecast (L3).**
- **Thread**: **"Ukraine hits refineries deep inside Russia"** — **six days, peak 20 outlets**, the
  most persistent thread on the board; refining bucket **690 / d7**, share **1.33 (2nd highest)**.
- **Catalyst**: **S55 08-11 · S67 08-13**.

### P39 — ★★ The dollar is falling on a settled instrument while its spec long builds — and the desk cannot see it

- **Claim** `[measured]`: **UUP −0.43% / −0.35% / −1.13% (1d/5d/20d)** with **FXY +2.64%/20d** and
  **FXE +1.31%/20d** agreeing on sign (**D5**), against a **COT spec long at the 81st percentile,
  +5,302 ADDED**. **`DTWEXBGS` has not printed since 2026-07-31.**
- **Direction A (a crowded long unwinding, ~55%)**: the position is the marginal seller ⇒ dollar
  weakness extends, which **supports the metals leg of XLB independently of the rate story** and is
  the **one mechanism under S57 branch A that is not NEM-specific**.
- **Direction B (the decline is the rate-cut re-pricing and reverses with it, ~45%)**: a hot CPI
  re-prices September, the dollar recovers, and **S57's branch A loses its non-NEM leg.**
- **Track KPI**: **UUP**, and **`DTWEXBGS` the moment it prints** — ⚠ **UUP is a DXY-basket proxy and
  `DTWEXBGS` is the BROAD trade-weighted index; they are different objects and no UUP value is
  substituted for a `DTWEXBGS` value (D1/D2).**
- ⚠ **Anti-signal (BOTH sides)**: **(a)** if UUP rises while the COT long keeps building, A is wrong
  (the position is not the marginal seller); **(b)** if the dollar falls **and** copper's 100th-%ile
  long unwinds together, this is one positioning event, not two, and both P39 and P33 are one claim.
- **Thread**: **"US and Japan and yen intervention", peak 19 outlets.**
- **Catalyst**: **2026-08-12 CPI · S57 settles 08-12.**

### P40 — ★★★ Hormuz is genuinely two-sided for the first time, and the desk's own bracket for it is un-scoreable

- **Claim** `[measured, news]`: **within one day's head tier, both directions carry independent
  multi-outlet clusters** — *"deal is close"* / *"route coordinates agreed with Oman"* / *"trilateral
  Mecca defence pact signed"* **against** *"U.S. must meet demands before reopening"* / *"UAE ship
  targeted by missile"* / *"Houthis strike a Saudi tanker off Yanbu"* `[hellenicshipping, 12,771-char
  body]`. **The six-day curve is 15→8→18→14→12→10 — oscillating, not trending.**
- **Direction A (reopening lands, ~50%)**: crude falls further (already **−7.67%/5d**), the
  rate-hike-odds channel of §B-2 keeps working, and **S52/S54's beneficiary map is the live object.**
- **Direction B (conditions bind and attacks continue, ~50%)**: the toll dispute alone is live — a
  **joint industry open letter opposing "compulsory tolls or charges" in the Strait** `[hellenicshipping
  body]` — and a missile strike on a transiting VLCC re-prices the whole complex.
- **Track KPI**: weekly Hormuz transit counts (**33 vs 50 = −34%**, M506); **S61's EW{STNG,FRO}
  5-session excess (−4.184)**.
- ⚠ **Anti-signal (BOTH sides)**: **(a)** a dated, signed reopening with tolls resolved kills B;
  **(b)** a confirmed closure or a strike on a transiting VLCC kills A.
- 🚨🚨 **The registration failure this proposition sits on top of**: **`S8` — the desk's only Hormuz
  bracket — is undated `[blank]` and has been un-scoreable for EIGHT consecutive runs.** The single
  loudest event axis in the feed has **no scoreable bracket**, and **P5 says a human must VOID or
  re-register it.** **Named again, not dropped.**
- **Catalyst**: **undated `[news👁 🔀binary]`** — recorded as `[blank]`, **not guessed.**

### Self-scoring note on the 08-08 propositions (P32–P36)

⚠⚠ **P32 · P33 · P34 · P35 · P36 are `UNSCOREABLE` this run — there is no new session and every one
of their track KPIs is a price or a FRED series that has not printed.** They are **not** scored
"HALF" or "HIT" on a re-read of the same bar. **One thing did change on one of them:**

| Prop | Its registered anti-signal | Status today |
|---|---|---|
| **P34** | **(a)** `[bloomberg 08-08, title only]` *"US Says Ukraine to Avoid Targeting Tankers"* — ***if corroborated in a body*, loadings recover and A's mechanism unwinds** | ⚠ **NOT CORROBORATED.** A dedicated `--field any` body search over 3 days returns **no body for that item**. What it returns instead, with a **12,771-character body**, is *"Route Avoidance Is No Longer Enough: **The Houthis Strike a Saudi Tanker Off Yanbu**"*, plus the head tier's **UAE ship missile strike**. ⇒ **the kill condition did not fire, and two independent attack events run the other way.** ★ This does **not** confirm P34-A (C4) — **it means the armed condition was re-read and did not fire**, which is the job the last run's own text set |

---

## §G · ★ Sector transmission matrix — all 11 GICS. **This is ROTATION's input.**

🚨 **The inherited line is taken from `2026-08-08/SECTOR_ROTATION.md §1 + §2` (the POST-delta
verdict), NOT from that run's `MACRO §F`.** The 08-08 run's own §0 recorded that it had inherited a
PRE-delta matrix and was corrected by ROTATION; **this run does not repeat that error.**

**Inherited (true post-delta of 2026-08-08):**
`INDU OW− · ENRG N+ · FIN N+ · IT N · HLTH N · DISC N · MATR N− · COMM UW · UTIL UW · STPL UW− · RE UW`
— **one overweight on the board and it is OW−.**

| # | Sector | Wind (this stage) | Driving prop | Numbers |
|---|---|---|---|---|
| 1 | **Industrials** | **OW− held** | P37 | **XLI exc1 −0.38 · exc5 −0.54 · exc20 −0.63 · exc60 +1.46.** ⚠ The only sector whose 60-day excess is positive while all three shorter windows are negative — **a decaying stock, not a live lead (M149's class).** DEEP owns it |
| 2 | **Energy** | **N+ held, but its MECHANISM is now withdrawn** | **P38** · P40 | **XLE exc5 −6.95 (worst of 11) vs exc20 +1.97** — an **8.9pp** two-window gap. **P4⁗ withdrawn (§A)** ⇒ **the N+ has no macro carrier left, only flow.** ⚠ On the week the **barrel fell twice as far as the equities** (§C-1 i) |
| 3 | **Financials** | **N+ held** | P37 | **XLF exc1 −0.97 (10th of 11) · exc5 −2.35 · exc20 +0.97 · exc60 +6.92.** 2s10s **+0.44**, 24bp from the line that kills the NIM mechanism. **S65 settles 08-11 · S66/S70 expect 08-10** |
| 4 | **Information Technology** | **N held** | — | **XLK exc5 +3.69 = the best SECTOR on the week**, against **exc20 −1.25** ⇒ **the two windows disagree in sign.** ⚠ The feed carries *"The AI Trade Rotation: Money Is Moving Out of Chips"* (6/4) **while the tape has Tech leading** — **narrative and tape disagree; the tape is the measurement (P4-principle)** |
| 5 | **Health Care** | **N held** | — | **exc60 +8.84 = the board's best 60-day**, with **exc5 −1.59**. Same decaying-stock shape as INDU, opposite sign on the short window. **Never carried as OW; breadth rank was 1 for three runs** |
| 6 | **Consumer Discretionary** | **N held** | — | exc1 +0.88 · exc5 −0.26 · exc20 −0.19 · exc60 −3.42 — **≈ zero on every window (C3: no signal, not a neutral verdict)** |
| 7 | **Materials** | **N− held** | **P33 (inherited) · P39** | **XLB exc5 +1.31 · exc20 +1.45**, against **GLD +3.74 / SLV +6.31** ⇒ **the sector is being carried by precious metals.** 🚨 **S57's branch A fires at ANY settled close through 08-12 and is 0.59pp away** — **ROTATION may not make a MATR call without it**. ★ **New non-NEM leg available: the dollar (P39)** |
| 8 | **Communication Services** | **UW held** | — | **XLC exc1 −0.55 · exc5 −0.73 · exc20 −2.77 · exc60 −8.73 — negative on all four windows, the only sector that is.** ⚠ **R56 binds: any breadth claim must be re-derived ex-EA, and EA is still in the universe (row 236)** |
| 9 | **Utilities** | **UW held** | P37 | **XLU exc5 −5.18 · exc20 −6.39 — worst 20-day on the board.** **S62 FIRED-B 08-07 but DEGENERATE (branch A 19.16pp away, D206)** ⇒ **the fire is not evidence.** Feed carries a nuclear-fuel item (5/4) |
| 10 | **Consumer Staples** | **UW− held** | — | **XLP exc5 −3.43 · exc20 −1.24.** Demoted 08-08 on the board's worst eqflow **and** worst Δ. **Never deep-dived in recorded history** |
| 11 | **Real Estate** | **UW held** | P37 | **XLRE exc5 −3.71 · exc20 −1.23** on a bull-steepening bar. **S25 pre-declared zero-information (D122).** P37-B is the branch that would make this the desk's most exposed call |

⚠⚠ **NO VERDICT CHANGE IS PROPOSED BY THIS STAGE, and the reason is stated rather than implied:
every input to every row above is the same settled bar the 08-08 verdicts were set on.** A delta
computed from an unchanged observation is not a delta. **ROTATION owns the decision; SWEEP's flow
panel is the only place a genuinely new number can enter, and it will be the same 08-07 bar too.**

---

## §H · Catalysts injected at run start

`catalyst_calendar.py --days 10` → `llm_outputs/2026-08-09/CATALYST_WATCH.json`

| When | Event | Axis | Type |
|---|---|---|---|
| **D-3 · 2026-08-12** | **July CPI** | inflation | 🔀binary `[bls✓]` |
| **D-4 · 2026-08-13** | **July PPI** | inflation | 🔀binary `[bls✓]` |
| **undated** | **Iran "Strait of Hormuz open" statement** | oil | 🔀binary `[news👁]` |

**Three binaries in window ⇒ PREMORTEM must bracket each BOTH ways.** ⚠ **No binary sits ≤48h**, so
the ≤48h clause is not triggered today; the ≤10-day clause is.
🚨🚨 **`[EARNINGS]` is EMPTY for a second consecutive run** inside earnings season, against a
**303-article/4-outlet earnings-call cluster** in this run's own brief (CRH, AUR, GEGYY, CPT, GH,
FTS, CSTL + 13 more). **`[STRUCTURAL]` is EMPTY too**, so the **SPCX unlock `S56` settles on 08-11 is
invisible to the schedule** while `SpaceX` is the #1 non-boilerplate token in the blind pool (§E-4).
**`D18`, with two independent numbers attached this run.**

---

## §I · Self-backtest — and the honest tally is that only ONE row is scoreable

| Proposition | Its registered condition | Settled outcome | Score |
|---|---|---|---|
| ★★★ **P4⁗** (08-07) | anti-signal = **dist−gas compressing on TWO consecutive settled closes ⇒ withdraw** | **−0.584 (08-06) then −1.109 (08-07)** | 🚨 **WITHDRAWN — the anti-signal fired, and the 08-08 run did not score it** |
| **P32 · P33 · P34 · P35 · P36** (08-08) | all track a price or a FRED series | **no new session; FRED still `asof` 08-06** | **UNSCOREABLE — not scored** |
| **P34's anti-signal (a)** | *"US Says Ukraine to Avoid Targeting Tankers" — if corroborated in a body* | **no body found; two attack events found instead** | **DID NOT FIRE** (re-read, not assumed) |

**Running hit-rate, appended.** ⚠⚠ **This run adds exactly ONE scored row to the record and refuses
five.** The standing warning applies in the opposite direction to usual: **R15's HIT→MISS reversal
came from scoring on the wrong window; the failure available today would be scoring on NO window.**
**A desk that re-reads yesterday's bar and calls the result a hit has a hit rate made of one
observation counted many times** — which is precisely the defect `HANDOVER §5` found inside the IC
ledger this morning. **Same class, two instruments, one run.**

---

## §J · New facts registered by this stage

| # | Fact | Value | Source | asof |
|---|---|---|---|---|
| **M544** | ★★★ **`P4⁗`'s anti-signal fired on the settle the 08-07 run named, and the 08-08 run did not score it** | dist−gas **40.211 → 39.627 (−0.584) → 38.518 (−1.109)**; the 08-08 §H scored P29/P30/P31/P27′/P28′/P1⁗ and **not P4⁗** | own calc, settled `CL=F`/`RB=F`/`HO=F`; cross-read of the 08-08 report | 2026-08-07 |
| **M545** | ★★ **The compression came from the GASOLINE side, not from distillate weakening** | gasoline crack **44.010 → 46.127 → 47.203** while distillate was **85.754 → 85.721 (flat)** | own calc | 2026-08-07 |
| **M546** | ★★★ **The 3-2-1 crack spent FOUR settled sessions below the carried 60 kill line and no file records it** | **57.008 · 56.879 · 57.413 · 59.336** (08-03…08-06), back to **60.042** on 08-07 = buffer **+0.042** vs M235's carried **+12.22**. ✅ **Estimator verified: reproduces M235's 64.304 / 68.117 / 72.219 exactly** | own calc | 2026-08-07 |
| **M547** | ★★★ **`fts search` defaults to AND and `search` defaults to OR — and the protocol instructs OR on the AND instrument** | `_fts.py:198 default="and"` vs `_search.py:99 default="or"`; OR÷AND by bucket **6.1× / 18.6× / 23.8× / 41.3× / 65.4× / 303× / ∞**; **AI-capex = 0 at the default** while its components read 18–1,000 | own read of source + 14 paired measurements | 2026-08-09 |
| **M548** | ★★ **The dollar fell on three windows while its spec long built** | **UUP −0.43 / −0.35 / −1.13% (1d/5d/20d)**, **FXY +2.64%/20d**, **FXE +1.31%/20d**; COT USD Index **81st %ile, +5,302 ADDED**; **`DTWEXBGS` last printed 07-31** ⚠ UUP=DXY basket ≠ broad TWD (D1/D2) | yfinance settled + CFTC COT | 2026-08-07 / 08-04 |
| **M549** | ★★ **Three named FOMC speakers were hawkish inside the window the futures repriced dovish** | **Cook "prepared to act" on a hike** `[cnbc + fxstreet bodies]`; **Musalem "should have hiked at the last meeting"** `[Reuters, title-only]`; **Kashkari "gradual rate hikes in 2026"** `[qz, title-only]` — against three body-level items naming weak labour data and Hormuz as *lowering* hike odds | `[news, --scope foreign]`, tiers stated | 2026-08-06 / 08-08 |
| **M550** | ★★ **The 2026-08-09 foreign news denominator is ZERO** | 08-07 5,178 art / 701 ev · **08-08 1,855 / 274** · **08-09 0 / 0**; `--scope all` gives **262**, all domestic-classified. **All 522 multi-day threads report ENDED with `살아있는 0`** — forced by the zero-article window end | `brief` + `thread`, `--scope foreign` | 2026-08-09 |
| **M551** | ★ **`SpaceX` is the #1 non-boilerplate token in the blind pool while `[STRUCTURAL]` is empty** | SpaceX **195** > Fed 187 > Iran 150 > Hormuz 130 > Jobs 128, after removing the D10 earnings boilerplate (Earnings 2,164 · Results 594); `CATALYST_WATCH.json` `[STRUCTURAL]` and `[EARNINGS]` both empty; **S56 settles 08-11** | `blindspot --days 2 --scope foreign` + `catalyst_calendar` | 2026-08-09 |
| **M552** | ★ **Gold and silver led the board from a 29th-percentile spec position** | GLD exc5 **+3.74** / SLV **+6.31** (the two best on the board) with COT gold **29th %ile** and silver **29th %ile** ⇒ **the metals leg is NOT a crowded-positioning event** | own calc + CFTC COT | 2026-08-07 / 08-04 |

**New digs: `D229`** (an armed anti-signal was pre-committed by one run and dropped by the next —
P4⁗) · **`D230`** (`fts search` default `and` vs `search` default `or`; the protocol's 7-bucket
instruction names the wrong mode, and a 4-term bucket silently reads 0 — the fifth tool in the
silent-zero class and the first whose mechanism is a flag default).

**New brackets: none.** MACRO does not register; **PREMORTEM owns registration** and must apply the
**`D216`** σ-distance test (flag `>3σ` unreachable **and** `<0.25σ` inevitable) before freezing.

---

## ✅ EXIT CHECK

- [x] Catalysts injected (`--days 10`, beyond the default because `SCENARIOS` names 08-11/08-12/08-13); indicators read (`module_macro_us --json` + `us_flow --cot`); **daily anchor read** = the 08-08 `MACRO_REPORT.md` **and** `SECTOR_ROTATION.md` (the latter is what §G inherits from, deliberately)
- [x] Events read via `brief --body 2` — **for `--date 2026-08-08`, because 08-09's foreign denominator is 0**; tail = 0
- [x] **`tail = 0` is NOT the coverage claim**: `single_source` **15 shown of 270** (⚠ the module states the 270 are **UNSCORED**, not low-scored — the classifier is Korean-only) · `excluded_nonmarket` **0 of 0** · `subevents_recovered` **94**. **255 single-outlet articles were not opened and every "quiet" statement above carries that number**
- [x] **Denominator corrected**: 1,855 articles → 274 events, non-market 0 (08-08); 08-09 = **0 foreign / 262 all-scope with 16 `translation_dup` removed**
- [x] Trajectories read (`thread --days 7`); ⚠ **every FADING/ENDED tag is declared inadmissible this run** (zero-article window end, `살아있는 0`) and **only per-day curves are cited**
- [x] Every "nothing in bucket X" claim carries its denominator — **and the one that would have been made (AI-capex = 0) was traced to a CLI default and refused (§E-3)**
- [x] **No bucket's 0/near-0 count trusted**: all seven buckets re-measured with **explicit `--mode or`** after the AND/OR default defect was found in source
- [x] **Both halves of the headline print cited** — payrolls **−23,000** *and* unemployment **4.1% (FRED, a four-month low)**
- [x] **Every relative-performance number names its benchmark inline (SPY)**; no cross-market statistical transfer (W1)
- [x] **Credit axis cited**: HY OAS **2.71** (−14bp on the week) · IG **0.78** · NFCI **−0.529**
- [x] **`real_10y` quoted with `breakeven_10y`**: **2.43** vs **2.25**, with the decomposition and its 08-06 cut-off stated
- [x] **Linter run on this stage's own output** — `scripts/report_lint.py llm_outputs/2026-08-09/industry_US/MACRO_REPORT.md` → **0 findings across C1/C2/S6/D6.** ⚠ **A clean lint is form, not correctness** — the unit says so and this run repeats it
- [x] Transmission matrix produced, all 11 sectors, **inherited from ROTATION's post-delta line, not from MACRO §F**
- [x] `MACRO_REPORT.md` written; self-backtest appended (**1 scored, 5 refused as unscoreable**); new blind-spot terms folded back
