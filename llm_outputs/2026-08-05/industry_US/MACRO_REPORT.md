# MACRO_REPORT — industry_US — 2026-08-05 (Wed) · run clock 09:1x–10:0x ET, **market opens mid-stage**

## ★★★ What this stage is obliged to say first

**On the 2026-08-04 settled session, WTI fell 5.69% and BOTH product cracks were FLAT.**

| Series | 08-03 | 08-04 | move |
|---|---|---|---|
| `CL=F` WTI | 80.34 | **75.77** | **−5.69%** |
| `HO=F` × 42 − WTI (distillate crack) | 82.502 | **82.591** | **+0.089 (FLAT)** |
| `RB=F` × 42 − WTI (gasoline crack) | 44.261 | **44.022** | **−0.239 (FLAT)** |
| `SPY` | 757.67 | **771.33** | **+1.80%** |

**That combination has a name in this desk's own registry, and it is not the one the desk used
yesterday. It is `S8` branch B, verbatim: *"Crude falls but cracks hold — NOT against us. This is
input-cost relief. OW Energy stands on refining margin rather than on the war."***

⚠⚠ **The 08-04 run scored `S49-B` and registered its meaning as *"the bottleneck is releasing"*
(a product-led break). One settled session later the product legs did not break — the BARREL did.**
The **fire is not reopened** (L3: a settled verdict on a frozen observable stands, and S49's
5-session change in fact deepened to **−12.487**). **What is falsified is the single-session
attribution.** ★ **And the desk had already built the instrument for exactly this**: `S55` brackets
**HO% − CL%**, and on 08-04 that reads **+2.94pp** (HO −2.75% vs CL −5.69%) — **branch B's
direction**, i.e. *"the collapse was the geopolitical premium deflating across the whole barrel;
**ENRG OW− must NOT be cut on S49-B**."* **S55's window is 08-04 → 08-11 and is NOT scored here.**

**Second thing, and it is a defect this stage found in its own instrument — §C-4:**
🚨 **`fts search` defaults to `--mode and`, while `pipeline/L2_modules/news.md` instructs an
"OR-mode per bucket" sweep and never passes the flag.** Measured this run: the rates bucket returned
**0** as five ANDed terms and **1,869** as an OR union — while `Fed` alone returns **578**.
**Every multi-term bucket count this desk has ever quoted was an AND-intersection presented as a
union.** Registered **D166**.

**Run clock.** Stage start **09:1x ET, pre-market**; equity bars for 08-05 **do not exist** (verified
`NaN`). ⚠ **Commodity futures already carry a live 08-05 bar** (`CL=F` 75.98 · `HO=F` 3.7730 ·
`RB=F` 2.5992) — **recorded as 🟡live, used for no verdict (D74).** Every equity/flow figure below is
stamped **`asof 2026-08-04 settled`**.

---

## §A · Indicators — primaries `[FRED]`

| Series | 07-30 | 07-31 | 08-03 | 08-04 | Read |
|---|---|---|---|---|---|
| `DGS10` | 4.68 | 4.75 | **4.70** | — | −5bp off the 365d high (4.75) |
| `DGS2` | 4.23 | 4.28 | **4.25** | — | −3bp |
| **derived 2s10s** (C5 — derived, not a FRED series) | +0.45 | +0.47 | **+0.45** | — | ⚠ **flattened 2bp — the first move toward S23/S51's line in the window** |
| `DFII10` real 10y | 2.41 | 2.47 | **2.43** | ⚠ no print (**D139**) | ✅ **S9 buffer WIDENED 8bp → 12bp** |
| `T10YIE` breakeven | 2.27 | 2.28 | 2.27 | **2.23** | ★ **−4bp on the oil-collapse session** |
| `BAMLH0A0HYM2` HY OAS | 2.84 | 2.85 | **2.78** | — | ★ **tightened 7bp — S26 buffer 25 → 32bp** |
| `BAMLC0A0CM` IG OAS | 0.80 | 0.79 | **0.78** | — | S41 buffer 11 → **12bp** |
| `VIXCLS` | 17.09 | 15.99 | **15.86** | ⚠ no print | 90d mean 18.19 |
| `DTWEXBGS` | 119.6753 | **119.7034** | ⚠ **no print, 3 publication days** | — | P7's anti-signal (≥ +1.0% from 119.70) **not fired** |
| `NFCI` | — | **−0.53** (07-31) | — | — | loosening a 7th week |
| `UNRATE` · `CPIAUCSL` | **4.20% · 332.57, both `2026-06-01`** — ⚠ **monthly, ~1 month stale. Quoted as stale, not as current.** |

**★ Composition, on the newest COMMON date only (D139 — `DFII10` lags `T10YIE` by one publication):**
**07-31 → 08-03: `DGS10` −5bp = `DFII10` −4bp + `T10YIE` −1bp ⇒ ~80% REAL.** ⚠ **Then 08-04's
`T10YIE` fell another 4bp with no matching `DFII10`** — so the *oil-collapse session's* decomposition
is **`unknown` (C3)**, not "inflation-led". **Stated as unmeasurable rather than guessed.**

**★★ The three risk axes all eased on the same session and they agree**: real rates **−4bp**, HY
**−7bp**, IG **−1bp**, VIX at a 120-day low area, equities **+1.80%**, crude **−5.69%**. **This is a
coherent disinflationary-relief signature and it is the first session in this window where the rate,
credit and commodity axes point the same way.** ⚠ **VIX and DFII10 have no 08-04 print, so the
signature is measured on 08-03 for two of its five legs** — stated, not smoothed.

### Positioning `[CFTC COT]` — 🚨 the SAME release for a FOURTH consecutive read

| Instrument | net-spec | wk Δ | 1yr %ile | tag |
|---|---|---|---|---|
| S&P 500 E-mini | −17,196 | −412 | **82** | 🟢 crowded-long |
| Nasdaq-100 | −9,914 | −222 | **5** | 🔴 crowded-short |
| UST 10Y | −876,119 | +3,587 | **13** | 🔴 crowded-short |
| **WTI Crude** | **+19,758** | −281 | **10** | 🔴 **crowded-short** |
| Nat Gas | −190,799 | −19,661 | **3** | 🔴 crowded-short |
| **Copper** | +67,281 | −6,696 | **96** | 🟢 crowded-long |

🚨🚨 **This file has not refreshed since the 2026-07-31 release; the next publication is 2026-08-07**
(S57's registered warning, D104/D140 class). ⇒ **No percentile above may be leaned on this run, and
the copper 96th in particular may not be used to argue the Materials UW.** ⚠ **And note what the
staleness costs**: the WTI 10th-percentile crowded-short reading **pre-dates a −12.3% two-session
crude collapse**, so it describes positioning into a move that has already happened. **It is a
historical fact, not a squeeze setup.** Stated because the opposite reading is the tempting one.

---

## §B · The US equity axis — settled 2026-08-04, benchmark **SPY** inline (C1)

| ETF | d1% | d5% | **exc5 vs SPY** | exc20 vs SPY |
|---|---|---|---|---|
| **XLK** Info Tech | **+4.98** | +9.24 | **+5.13** | +1.15 |
| QQQ | +3.40 | +7.16 | +3.05 | −1.13 |
| OIH oil services | +2.62 | +5.60 | +1.49 | +3.90 |
| XLY Cons Disc | +0.07 | +5.17 | +1.05 | −2.39 |
| **SPY** | **+1.80** | **+4.11** | **0.00** | **0.00** |
| XOP E&P | −1.34 | +3.35 | −0.76 | **+6.11** |
| XLC Comm | +0.63 | +2.16 | −1.95 | −2.24 |
| XLI Industrials | +1.77 | +2.14 | −1.97 | −0.95 |
| **XLE Energy** | **−0.46** | +1.65 | **−2.46** | **+3.94** |
| KRE regional banks | +1.01 | +1.37 | −2.75 | +0.53 |
| IYT Transports | +2.29 | +1.01 | −3.10 | −2.38 |
| XLF Financials | +0.87 | +0.49 | −3.63 | +0.11 |
| **XLB Materials** | +1.94 | −0.65 | **−4.76** | −2.21 |
| XLRE Real Estate | −0.02 | −1.83 | −5.94 | −2.54 |
| XLP Staples | +0.60 | −1.94 | −6.05 | −2.56 |
| **XLV Health** | −0.09 | −3.09 | **−7.20** | −4.58 |
| **XLU Utilities** | −0.56 | −3.10 | **−7.21** | **−6.64** |

★★ **Three readings this table forces, each of which contradicts something the desk carried:**

1. **XLE fell only −0.46% on a session crude fell 5.69%, and XOP fell −1.34%.** ⇒ **The Energy
   equity complex did NOT track the barrel down.** That is the single strongest piece of evidence
   for **S31's** *"business, not war premium"* side and against a mechanical ENRG cut — **and it is
   the observation `S60` (the 08-04 XLE full exit) is bracketed on.** ⚠ **One session, n=1 (S1).**
2. **XLK's exc5 (+5.13) exceeds QQQ's (+3.05).** ⇒ **the Tech move is NOT purely the NDX mega-cap
   quartet** — XLK's non-NDX weight outperformed. ⚠ **But the COT NDX crowded-short reading that
   would corroborate a squeeze is the stale file** (§A) and **may not be cited.**
3. **XLB's exc5 = −4.76pp**, reproduced independently here from `auto_adjust=False` closes. ⇒
   **S36 branch B** (§D-2) and **S57's branch-B region** (< −2.4pp) both confirmed on the same number.

---

## §C · The news axis — 2,516 foreign articles → 372 events, and the day has ONE story

### C-1 · Denominator, stated before any "quiet" claim (EXIT CHECK)

```
articles 2,516 → events 372 → market 372 · non-market 0
head (≥5 outlets) 38 · body (2–4) 334 · tail (2 outlets) 0 shown (sample only)
single_source 15 shown / 429 total   ⇒ ⚠⚠ 414 WITHHELD
excluded_nonmarket 0 / 0 (band nb > −3.0)
subevents recovered 75
```
⚠⚠ **`tail = 0` is NOT the coverage claim, and this run's gap is larger than usual and has a named
cause: 429 of the single-source items are UNSCORED because the non-market classifier is
Korean-only.** ⇒ **414 single-source foreign items were not seen by any filter.** **No "nothing
happened in bucket X" claim in this report is made without that number attached.** Per the L2's own
measurement, single-source is exactly where FX and rates primaries live — **so this run's rates/FX
reads carry a stated blind spot.**

### C-2 · ★★★ The day's story: the US government said the Strait is "free and open" — and it still does not clear S52 branch A

**BUILDING thread, 3 days, outlets 2 → 9 → 13:**
```
08-02 [ 2건/ 2매체] Iran says negotiations with Oman over Strait of Hormuz…
08-04 [13건/ 9매체] Iran and Oman make progress on a deal to reopen the Strait…
08-05 [17건/13매체] U.S. says Strait of Hormuz is 'free and open' as Bessent…
```

**The two primary texts, pulled rather than paraphrased:**

| # | Primary text | What it actually says |
|---|---|---|
| 1 | **US CENTCOM, post on X** | *"the southern route of the Strait of Hormuz remains **free and open**"*, with **1,000+ commercial vessels assisted** in transit despite Iranian aggression |
| 2 | **Treasury Secretary Bessent, CNBC "Squawk Box", direct quote** | *"There is **a chance we may** have a deal **today or tomorrow** to open the Strait and move towards a more normalized position."* Asked about an Iranian toll: *"I think it would be **freedom of movement**."* |
| 3 | Trump | deal *"could be agreed Wednesday or Thursday"* |

**⇒ S52 branch A adjudication: NOT FIRED.** Branch A requires *"a **dated** Strait-reopening **term**
in a primary text … **NOT** a repeat of the 08-02 conditional wording."*

- **CENTCOM's statement is primary and is about the Strait — but it is a STATUS assertion about the
  SOUTHERN ROUTE under military escort, not a reopening term, and it carries no date or "effective"
  language.** ★ **"We are escorting 1,000 vessels through" is the opposite of "the strait has been
  reopened by agreement" — it describes the blockade being *worked around*, not lifted.**
- **Bessent's quote carries a date, but the date attaches to the DEAL, not to the OPENING, and the
  modal verb is *"a chance we may."*** That is precisely the excluded class.

⇒ **S52 → tracking C. S49's registered invalidation (*"a Hormuz reopening statement ⇒ S8 owns
it"*) does NOT trigger. S49-B stands unqualified.**

★★★ **And here is the finding that matters more than the adjudication.** **The tape has already
paid −12.3% of crude over two sessions on wording this desk's own pre-registered evidentiary bar
rejects.** Both halves are carried (C2), neither resolved:
- **Reading 1** — the bar is calibrated too strictly, and a desk that will not fire a branch against
  its own OW until a signed text exists will be last to every de-escalation. ⚠ **This is now the
  THIRD consecutive run in which this desk declines to fire a branch that would go against its own
  Energy tilt.** Named, because that pattern is how a threshold quietly becomes a preference.
- **Reading 2** — the bar is doing its job, and the price is running ahead of an event with real
  probability of not landing. **Evidence for this half, same session, same pool:**
  - `hellenicshipping`: **"Strait of Hormuz: Tanker lull PERSISTS despite Trump's peace pledge"** —
    ⇒ **the physical transit series has not moved while the price has.**
  - `hellenicshipping`: **"U.S. aims to announce Hormuz deal by Wednesday, Iran warns of DELAY"**
  - `guardian`: *"US and Iran signal hope … but **terms unclear**"*
  - `fortune`: *"could come as soon as today — **with a truckload of caveats**"*
  - **🚨 An ESCALATION printed the same day**: *"Yemen's Houthis claim ballistic missile strike on
    Saudi oil [terminal]"* **[9 articles / 8 outlets, BUILDING 3→8]**, plus *"Projectile sinks
    Indian-flagged ship off Yemen"*.

⚠ **S52 branch B checked explicitly and NOT fired**: it requires a strike on **named IRANIAN** energy
infrastructure. **A Houthi strike on a SAUDI oil facility is not that**, and the bracket is not bent
to fit an event it did not name. ⇒ **The escalation is real, is against the de-escalation trade, and
NO registered bracket owns it.** **PREMORTEM's gap to fill.**

★ **One physical counter-datum in the other direction, recorded for symmetry:**
*"Qatar Sends Its First LNG Shipment Through Hormuz in T[wo months]"* — FADING thread 6→6→2→3→2.
⇒ **Physical flow has partially resumed for LNG while the tanker lull persists for crude.**
**Two physical series disagree.** ⚠ **Both are `[title-only]` = D6 C-grade, direction only.**

### C-3 · The other events that move a sector line

| Event | Outlets | Bears on |
|---|---|---|
| **"AMD falls as investors seek bigger AI payoff"** · *"AMD data centre sales DOUBLE but shares slide"* · *"Arista delivers its first $3 BILLION quarter"* | 25건/8 + 7건/4 | **S50** (AMD/ANET 08-04, settles 08-06). ★ **Both beat on the AI line and AMD sold off** ⇒ the read is *positioning/expectation*, not guidance |
| **SpaceX debut earnings — "slides as AI spending worries overshadow early returns", −10%** + **"Lockup Expires Aug. 6 — 911.5 Million shares"** | 15건/10 + 12건/11, both BUILDING | **S56** (SPCX 08-06 unlock; 219.3M shares short ≈34% of float vs up to 911.5M unlocking) |
| **"US Companies Added FEWER Jobs Than Expected in July: ADP"** | 7건/4 | **NFP 08-07 · S51** — the first labor datum of the window and it is soft |
| **"Fed's Schmid says TIGHTER policy needed to reduce inflation"** + *"Warsh considering fewer annual FOMC meetings"* | 20건/8 | Rates. ⚠ **A hawkish Fed voice on the same day breakevens fell 4bp** — the two point opposite ways |
| **"Why Japan is propping up the yen with US help"** · *"Yen steadies after intervention, dollar near 6-week low"* | 12건/7 + 7건/4 | **P7′.** ⚠ **`DTWEXBGS` has not printed for 3 publication days** ⇒ the desk's own dollar series cannot corroborate |
| **Disney beats · Shopify beats · Uber beats · Apple's iPhone quarter "even better"** | 13/9, 7/5, 6/5, 9/5 | Broad DISC/COMM earnings tone is **positive**, against XLY exc20 −2.39 |

### C-4 · 🚨 D166 — the bucket sweep has been running AND where the protocol says OR

**Measured this run, same DB, same window (2 days, `--scope foreign`):**

| Query | Count |
|---|---|
| `fts search Fed FOMC inflation CPI "rate cut"` (5 terms, **default mode**) | **0** |
| `fts search Fed` alone | **578** |
| `fts search Fed FOMC` (2 terms, default) | **75** ⇒ **strictly fewer than `Fed` alone ⇒ AND** |
| `fts search Fed FOMC inflation CPI "rate cut" --mode or --syn` | **1,869** |

**Root cause, read from the source rather than inferred**: `module_news_data/_fts.py:198`
`s.add_argument("--mode", choices=["and","or"], **default="and"**)`, and line 117
`match = (" AND " if mode=="and" else " OR ").join(groups)`. **The protocol
(`pipeline/L2_modules/news.md`) says *"7-bucket narrative sweep (FTS `--syn`, OR-mode per bucket)"*
and never passes `--mode or`.**

⇒ **Every multi-term bucket figure this desk has quoted is an AND-intersection reported as a union**,
which **systematically manufactures "quiet"** — the exact failure the EXIT CHECK was written to
prevent, produced by the CLI's own default rather than by a mis-typed argv. **Registered `D166`.**
★ **The fix is one flag in one L2 file and needs no code change** — stated positively, and this run
uses the corrected form below.

### C-5 · 7-bucket sweep — **`--mode or --syn`**, with a stated pool denominator

| # | Bucket | hits (2d, foreign) | share of pool |
|---|---|---|---|
| 4 | **dollar / FX** | **2,264** | 18.9% |
| 7 | **geopolitics / trade** (tariff·sanctions·Hormuz·Iran) | **2,091** | 17.5% |
| 1 | **rates / inflation** | **1,869** | 15.6% |
| 5 | **oil / energy** | **1,658** | 13.9% |
| 3 | **credit** | **1,468** | 12.3% |
| 6 | **AI-capex** | **1,434** | 12.0% |
| 2 | **labor / growth** | **891** | 7.5% |
| — | **pool proxy** (`the`, 2d foreign) | **11,949** | — |

⚠⚠ **These are NOT comparable to any prior run's bucket numbers** — prior runs quoted AND-intersections
(§C-4) and this one quotes unions. **The series restarts here. No velocity claim is made across the
break** (C1: a baseline that changed definition is not a baseline).
⚠ **`the` is a crude pool proxy and overstates coverage of non-English items.** Stated.

### C-6 · `theme_age` — ZERO 🟢FRESH for a **12th** consecutive foreign-feed measurement

| Theme | verdict | age | 7d avg | accel | n |
|---|---|---|---|---|---|
| **`windfall tax`** | 🟡ACCELERATING | 43 | 2.9 | **10.71×** (was 8.57×) | **29** |
| `Hormuz` | ⚪ECHO | ≥90 | 176.0 | 1.82× | 6,688 |
| `OPEC` | ⚪ECHO | ≥90 | 22.7 | 1.83× | 830 |
| `distillate` | ⚪ECHO | ≥90 | 19.0 | 1.64× | 540 |
| `data center` | ⚪ECHO | ≥90 | 349.6 | 1.93× | 10,990 |

⚠ **`windfall tax` is the only accelerating theme and n = 29 — thin (S5).** Its acceleration rose
while its absolute base barely moved; **the ratio is direction only.**

---

## §D · Bracket-facing measurements this stage owes

### D-1 · S49's observable, re-pulled IN FULL (D140's remedy executed, not cited)

| Settled | HO=F | CL=F | crack | 5-session Δ |
|---|---|---|---|---|
| 2026-07-28 | 4.1509 | 79.26 | 95.078 | +6.671 |
| 2026-07-29 | 4.3701 | 84.46 | 99.084 | +11.665 |
| 2026-07-30 | 4.2094 | 83.59 | 93.205 | +3.048 |
| 2026-07-31 | 4.1215 | 84.67 | 88.433 | +2.158 |
| 2026-08-03 | 3.8772 | 80.34 | 82.502 | **−7.575 ← FIRED-B** |
| **2026-08-04** | **3.7705** | **75.77** | **82.591** | **−12.487** |

✅ **D140 reproduces clean for a second consecutive run** — the 07-31 value re-pulls at **+2.158**,
matching the prior two pulls. **The revision has settled.**
★ **The 5-session change deepened to −12.487, but ONLY because the base rolled off 07-28's +95.078.
The crack LEVEL rose +0.089 on 08-04.** ⚠⚠ **Quoting the change without the level today would invert
the meaning (C2, both halves) — this is the sharpest instance of C2 the desk has produced.**

### D-2 · The four brackets whose window closes on TODAY's close — measured, pre-committed

*(HANDOVER §2c owns the full statement; reproduced here with MACRO's own independent numbers.)*

| ID | 08-04 settled measurement | Pre-committed | Margin |
|---|---|---|---|
| **S30** | STX **−1.0** · MU **−8.0** · WDC **−0.1** ⇒ **median −1.0** | **B** | 🚨 **1.0pp** |
| **S31** | XOM RS20 **+5.5** / RS60 **−0.4** | 🚨 **AMBIGUOUS — neither branch; the bracket does not partition its own observable** | A needs +4.5 · B needs −5.5 |
| **S36** | XLB exc5 **−4.76pp** (reproduced §B) | **B** | 4.76pp inside |
| **S53** | PSX prints today | **carried to 08-06** | — |

### D-3 · S55, S57, S60 running values — recorded, **NOT scored** (windows open)

| ID | Observable | Running value asof 08-04 | Which region |
|---|---|---|---|
| **S55** | HO% − CL%, 5-session, 08-04 → 08-11 | **08-04 single session +2.94pp** | ⇒ **branch B's direction** (B needs ≥ +6.5 over the full window) |
| **S57** | XLB 5-session excess vs SPY → 08-12 | **−4.76pp** | **inside branch B's region** (< −2.4) |
| **S60** | XLE 5-session excess vs SPY, 08-04 → 08-11 | XLE exc5 **−2.46pp** (anchor bar itself) | **C region** so far (A ≥ +3.90 · B ≤ −5.05) |

---

## §E · Propositions

> Each carries direction both ways, a **mandatory anti-signal**, a tracked KPI, and a dated catalyst.
> Anchors `[FRED]` > `[news]`. `[inferred]` claims are tagged and are not evidence.

**P4″ — ★★★ REPLACED. The crack did not break on 08-04; the BARREL did, and the cracks held.
`[own calc, yfinance DAILY settled, one source]`**
See §D-1. **Crude −5.69%, distillate crack +0.089, gasoline crack −0.239.** ⇒ **`S8` branch B's
signature (input-cost relief), on the session AFTER `S49-B` fired on branch-A-shaped economics.**
*Against*: **n = 1 settled session (S1)**; `distillate` runs ⚪ECHO **1.64×** so the narrative axis
does not corroborate (**C6** — not evidence of absence, not confirmation either); and the 5-session
change **deepened** to −12.487, which is the frozen observable and points the other way. **KPI**: the
distillate crack **LEVEL and 5-session change together, never one alone** (C2). **Anti-signal**: the
crack level falling **> 3 points** on a settled close while WTI is flat-to-up ⇒ the break really is
product-led and P4″ is withdrawn in favour of the 08-04 run's reading. **Catalyst**: **S49 window
08-06 · S55 08-11.**

**P18″ — ★★★ The US government said "free and open" and S52 branch A still does not fire — and the
tape does not care. `[PRIMARY: CENTCOM post + Bessent CNBC quote, 13 outlets]`**
See §C-2. **New vs 08-04**: a **primary US-government statement naming the Strait** (CENTCOM) and a
**second dated conditional** from the same Treasury Secretary. **Unchanged**: the statement describes
the **southern route under escort**, not a reopening term; the deal remains *"a chance we may."*
*Against this refusal*: **third consecutive run declining to fire against the desk's own tilt**, and
the price has moved **−12.3%** on the wording. *For it*: **tanker lull persists · Iran warns of
delay · terms unclear · a Houthi missile hit a SAUDI oil facility the same day.**
**KPI**: a primary text in which **the opening**, not the deal, carries a date or "effective"
language. **Anti-signal**: exactly that ⇒ **S52-A ⇒ OXY · COP · CVX · XOM lose the leg S31 says they
stand on.** **Catalyst**: **S52 window 08-06**; Bessent's own stated horizon is **today**.

**P22 — ★★★ NEW · An ESCALATION printed on the de-escalation day and NO bracket owns it.
`[news, 9 articles / 8 outlets, BUILDING 3→8]`**
*"Yemen's Houthis claim ballistic missile strike on Saudi oil [terminal]"* + *"Projectile sinks
Indian-flagged ship off Yemen"*. **S52 branch B is explicitly about IRANIAN infrastructure and is NOT
bent to cover this.** ⇒ **the desk's Iran-axis brackets are blind to the Red Sea / Saudi leg of the
same conflict**, which transmits to the **same** crude and freight variables. *Against*: **2 days,
n small (S5)**, and Houthi claims are frequently unverified — **claim ≠ event.** **KPI**: a **named**
Saudi facility with a **confirmed** production or export impact, ≥2 independent outlets on one
primary. **Anti-signal**: 7 days with no confirmed facility impact ⇒ rhetoric-only, drop the leg.
**Catalyst**: `[blank]` — **no date exists and none is invented.**

**P1″ — ★★ The long end FELL and its composition is ~80% real on the last common date — then went
unmeasurable. `[FRED]`**
07-31 → 08-03: `DGS10` **−5bp** = `DFII10` **−4bp** + `T10YIE` **−1bp**. **08-04: `T10YIE` −4bp more,
`DFII10` no print ⇒ that session's split is `unknown` (C3).** ★ **S9's kill line moved AWAY: buffer
8bp → 12bp**, reversing the 08-04 run's "closest kill line on the board" flag. *Against*: **two
prints (S1)**, and D139's one-day lag makes every same-day decomposition unavailable by construction.
**KPI**: `DFII10` **with** `T10YIE`, on the newest common date only. **Anti-signal**: `DFII10` ≥ 2.55
⇒ S9 kill. **Catalyst**: **S9 settles today** · **CPI 08-12.**

**P13″ — ⚠ The bear steepener STOPPED steepening — first flattening of the window. `[FRED, derived — C5]`**
2s10s **+0.47 (07-31) → +0.45 (08-03)**. S23's ≤ +0.20 line is **25bp away** (was 27bp **receding**;
it is now **approaching**). S51's branch-A floor (≥ +0.35) still satisfied with **10bp** to spare.
*Against*: **2bp on one print is inside any reasonable noise band (S1/C4)** — this is a direction
change, not a magnitude. ⚠ **W3: the NIM leg migrated to markets/financing (M138)**; a steepener does
not hit where the 2023-vintage thesis assumed. ★ **And the tape agrees with the flattening: XLF exc5
−3.63, KRE exc5 −2.75.** **KPI**: derived 2s10s on settled FRED closes. **Anti-signal**: ≤ +0.20 ⇒
**FIN OW− loses its only non-retracted leg (R32 killed breadth).** **Catalyst**: **NFP 08-07 (S51)**;
⚠ **S23's window closes TODAY, before NFP.**

**P2″ — Credit EASED on the oil-collapse session; conditions still loosening. `[FRED]`**
HY **2.85 → 2.78 (−7bp)**, its lowest of the window; IG **0.79 → 0.78**; NFCI **−0.53**, loosening a
7th week. Buffers **widened**: S26 needs HY ≥ 3.10 ⇒ **32bp**; S41 needs IG ≥ 0.90 ⇒ **12bp**.
*Against*: the credit bucket runs at **12.3% of pool** with no directional read, and — per §C-1 —
**414 single-source items were withheld**, which is where credit primaries would sit. **Anti-signal**:
HY ≥ 3.10 on a close. **Catalyst**: **S26 · S41 both 08-12.**

**P23 — ★★ NEW · Energy EQUITIES decoupled from the barrel, which is S31's question answered on the
tape rather than in the bracket. `[own calc, settled 08-04, bench SPY inline]`**
**WTI −5.69% · XLE −0.46% · XOP −1.34% · OIH +2.62%**, and **XLE's exc20 is still +3.94** while its
exc5 is −2.46. ⇒ **a 5.7% barrel move produced a 0.5% sector move, and the SERVICES sub-leg rose.**
*Against*: **n = 1 session (S1)**; **W5 — "Energy" is at least three businesses (integrated, E&P,
services) and they disagreed by 3.96pp on one day**, so the sector label is the wrong unit here;
and **R39 means the desk's own registry tag for XOM's refining share is wrong**, so any
integrated-vs-refining decomposition is `unknown` (C3). **KPI**: XLE/XOP/OIH excess vs SPY quoted as
three numbers, never one. **Anti-signal**: a second session where crude falls >3% and XLE falls with
it ⇒ the decoupling was one-day noise. **Catalyst**: **S60 08-11 · S31 today.**

**P20′ — The windfall-tax leg ACCELERATED and still has no instrument. `[news]`**
`windfall tax` 🟡ACCELERATING **10.71×** (from 8.57×), age 43, **n = 29**. **KPI unchanged**: a named
legislative or executive instrument (bill number, EO, Treasury rule) in a primary text — **not a
further quote.** **Anti-signal**: 14 days from 08-04 with no named instrument ⇒ rhetoric-only, drop
the leg (**deadline 2026-08-18**). *Against*: **n = 29 (S5)**; the ratio moved while the base did not.
**Catalyst**: `[blank]`.

**P24 — ★★ NEW · Both AI-silicon prints BEAT and one sold off hard — the read is positioning, not
guidance. `[news, 25건/8 + 7건/4]`**
*"AMD data centre sales DOUBLE but shares slide"* · *"Arista delivers its first $3 billion quarter"* ·
*"How Intel's earnings turned AMD's beat into a sell-off."* ⇒ **S50's branch structure (only the CUT
branch changes a conclusion) is being tested by an outcome it did not anticipate: a raise that the
tape sold.** *Against*: **`[title-only]` = D6 C-grade**; **no guidance line has been read from a
primary transcript by this stage**, and the settled reaction bar is 08-05, unsettled. ⚠ **And XLK
still printed exc5 +5.13 on the same session** — the sector did not follow AMD. **KPI**: the settled
08-05 close vs S50's registered bands. **Anti-signal**: XLK exc5 turning negative with AMD still
down ⇒ this was a sector event after all. **Catalyst**: **S50 settles 08-06.**

**P7″ — The yen channel is loud and the desk's dollar instrument has gone dark. `[news] + [FRED]`**
*"Why Japan is propping up the yen with US help"* [12건/7] · *"Yen steadies after intervention,
dollar near 6-week low"* [7건/4]; **dollar/FX is the #1 bucket at 18.9% of pool.** ⚠⚠ **`DTWEXBGS`
has NOT printed for 3 publication days** (last 119.7034, 07-31) — **the series that just cleared an
11-day suspension has gone quiet again.** P7's anti-signal (≥ +1.0% from 119.70) **cannot fire while
the series is silent** — stated as an instrument gap, not an all-clear. ⚠ **D22's lag table is still
absent** ⇒ `[unverified]` as transmission (W2). **KPI**: `DTWEXBGS`'s next print. **Catalyst**: ~08-07.

**P25 — ★★ NEW · The first labor datum of the NFP window is SOFT and the Fed voice is HAWKISH.
`[news, 7건/4 + 20건/8]`**
*"US Companies Added FEWER Jobs Than Expected in July: ADP"* against *"Fed's Schmid says TIGHTER
policy needed"* — **on the same session breakevens fell 4bp.** ⇒ **the labour and policy axes point
opposite ways going into NFP 08-07 (S51).** *Against*: **ADP is a proxy with a documented weak
mapping to NFP (D2 — proxy sign)**; **no ADP number was read from a primary release by this stage**;
one Fed president is not the committee. **KPI**: NFP 08-07 headline **and** the revision to the prior
month (both halves, C2). **Anti-signal**: NFP in line-to-hot with 2s10s ≤ +0.20 ⇒ **P13″'s
anti-signal and S51 branch B fire together and FIN OW− is done.** **Catalyst**: **NFP 2026-08-07.**

**P8 — Housing/consumer rate transmission remains unmeasurable in this repo. MISS by construction,
ELEVENTH consecutive run.** `MORTGAGE30US` is not in the catalog (**D99**). Stated so the gap does
not read as a quiet channel.

---

## §F · ★ Self-backtest — the 2026-08-04 propositions scored

| ID | Registered KPI | Verdict |
|---|---|---|
| **P4′** | 5-session distillate change; anti-signal = *change returning > 0 by 08-06* | ⚠⚠ **HALF, and the informative half is the MISS.** The **change** deepened to −12.487 (anti-signal did not fire) ⇒ **HIT on the frozen observable.** But P4′'s *claim* was *"the break is product-led"* — and on 08-04 **the crack level was FLAT while crude fell 5.69%**, which is not product-led. ⇒ **the observable held and the attribution failed.** Recorded as a half, not laundered. |
| **P18′** | *a primary text in which the OPENING carries a date* | ★★ **HIT — and it discriminated a second time.** A **primary US-government statement about the Strait arrived** (CENTCOM "free and open") and **P18′'s own threshold correctly refused it** because it is a status claim about a route, not a dated reopening term. **Two consecutive runs where the threshold caught a near-miss.** |
| **P19′** | *settled WTI vs the crack; anti-signal = crude falling with the crack RISING ⇒ it is an OPEC event and P4′ is mis-attributed* | 🚨🚨 **THE ANTI-SIGNAL FIRED.** 08-04: **crude −5.69% and the distillate crack +0.089 (rising).** ⇒ **by P19′'s own registered wording, P4′ IS mis-attributed.** ★ **This is a proposition killing a sibling proposition on a pre-registered condition, one session after both were written. Recorded as the run's cleanest self-correction.** |
| **P1′** | DFII10 with T10YIE; anti-signal DFII10 ≥ 2.55 | ★ **HIT.** DFII10 **2.47 → 2.43**, buffer 8 → **12bp**. The "closest kill line on the board" flag is **withdrawn on the next print** — and the withdrawal is the point: a kill line that only ever approaches is a trend, not a threshold. |
| **P13′** | derived 2s10s; anti-signal ≤ +0.20 | ⚠ **HALF.** P13′ said *"27bp away and RECEDING."* It is now **25bp away and APPROACHING.** Direction claim **MISS**, level claim HIT. |
| **P2′** | HY OAS; anti-signal ≥ 3.10 | ★ **HIT.** 2.85 → **2.78**, buffer 25 → **32bp**. "Elevated, not deteriorating" confirmed on a fresh print. |
| **P21** | VIX settled with SPY's own move; anti-signal VIX > 20 with the crack still falling | **UNSCOREABLE — `VIXCLS` has no 08-04 print.** ⚠ Logged as a **data gap**, not a hold. |
| **P7′** | DTWEXBGS's next print; anti-signal ≥ +1.0% | **UNSCOREABLE — no print for 3 publication days.** ⚠ **Second consecutive run where this series cannot be scored.** |
| **P20** | a named legislative/executive instrument | **HELD, and the theme accelerated 8.57× → 10.71×.** No instrument named. **Deadline 08-18.** |
| **P10** *(carried)* | median RS20 {STX, MU, WDC} | ★★ **The reversal REVERSED AGAIN.** 08-02 **FIRED-A** (>0) → 08-03 **−9.55** → **08-04 −1.0.** ⇒ **three sign-relevant moves in three sessions on the observable a bracket was frozen on.** **S30 is not re-scored (L3).** This is now measured **twice** as a threshold sitting on noise, and it is the strongest available evidence for **L3's** rule that branch information content must be checked against the observable's own volatility **before** freezing. |
| **P3** | supplier−spender spread | ⚠ **INVERTED.** XLK exc5 **+5.13** and QQQ exc5 **+3.05** ⇒ the spender/mega-cap leg is now **lagging** the broader tech sector, the opposite of the carried shape. n=1. |
| **P16** | breadth, two windows | ⚠ **The two windows disagree AGAIN and the sign flipped from yesterday**: XLY **exc5 +1.05 / exc20 −2.39.** Still n≈1 event. |
| **P15 · P17 · P6 · P5 · P11** | — | **HELD, unadvanced.** P6 `[blank]` for a 5th run; P17's D20 unfixed. |
| **P8** | `MORTGAGE30US` | ★ **MISS by construction, ELEVENTH run.** |

**Running hit-rate, this run:** **HIT 4 · HALF 3 · MISS-by-construction 1 · ANTI-SIGNAL FIRED 1 ·
UNSCOREABLE 2 · HELD 6.** ⚠ **Two of the fifteen were unscoreable because a FRED series did not
print** — that is 13% of the board lost to publication lag, and it is the second run running.

---

## §G · ★ Sector transmission matrix — the deliverable

> All 11 GICS, one line each. **Direction only** — ROTATION sizes it. **No buy/sell language (P4).**
> ⚠ **D161's interim rule applies**: no line below cites a `sector_flow` 🟢 tag, because SWEEP has
> not run and because a green tag may not be quoted without decomposing which axis lit it.

| # | Sector | Tilt | Driving proposition | The one number |
|---|---|---|---|---|
| 1 | **Energy** | **OW− → OW−− (weakened, NOT cut)** | **P4″ · P23 · P18″** | Crude **−12.3%/2 sessions** but **cracks FLAT** and **XLE only −0.46%**. ⚠ **A cut here would be executing S49-B's attribution, which P19′'s anti-signal just falsified.** **S55 (08-11) owns the decision.** |
| 2 | **Information Technology** | **N → N+** | **P24 · P3** | **XLK exc5 +5.13, the board's best**, and it **beat QQQ (+3.05)** ⇒ not purely mega-cap. ⚠ AMD sold off on a doubled data-centre line. |
| 3 | **Financials** | **OW− → N+** | **P13″ · P25** | 2s10s **flattened 2bp — first of the window**; **XLF exc5 −3.63 · KRE −2.75.** ⚠ The tilt's only non-retracted leg is now moving the wrong way with **NFP 08-07** ahead. |
| 4 | **Materials** | **UW− (confirmed on a fresh number)** | **P2″ · S36/S57** | **XLB exc5 −4.76pp**, inside S57's branch-B region. ⚠ **Copper's 96th percentile may NOT be cited — stale COT file.** |
| 5 | **Utilities** | **UW (new — was the promoted DEEP slot)** | **P1″** | **exc5 −7.21 · exc20 −6.64, worst on the board on both windows.** ⚠ **R40: the "regulated seven" basket is contaminated; S35/S47 settle 08-07 on the regulated SIX.** **CEG 08-06 · VST 08-07 print.** |
| 6 | **Health Care** | **UW** | — | **exc5 −7.20**, worst-tied. ⚠ *"Novo Nordisk shares plunge after a key trial fails"* is the only named driver and it is **[title-only]**. |
| 7 | **Industrials** | **N (two-sided, unchanged)** | **P4″ · M91** | **XLI exc5 −1.97 · IYT −3.10.** ⚠⚠ **Both directions live**: crude −12.3% is **input-cost relief** for airlines, and **revenue drag** on the rail fuel-surcharge leg (M91, magnitude retracted by R38). **Do not net them.** |
| 8 | **Consumer Discretionary** | **N** | **P16** | **exc5 +1.05 / exc20 −2.39** — the two windows still disagree. Disney/Uber/Shopify all beat. |
| 9 | **Communication Services** | **N−** | — | **exc5 −1.95 · exc20 −2.24.** Alphabet's drop is a named head event, unread at body level. |
| 10 | **Consumer Staples** | **UW−** | — | **exc5 −6.05.** Consistent with a risk-on tape; no independent driver measured. |
| 11 | **Real Estate** | **UW−** | **P1″** | **exc5 −5.94** on a session real rates FELL 4bp ⇒ **the rate-sensitivity story did not transmit.** ⚠ **S25 settles 08-08.** |

★★ **The matrix's own honest weakness, stated rather than buried:** **nine of eleven lines are
carried by the same one-week ETF excess table (§B)**, which is **one settled session of new
information on top of four carried ones**. **W5 binds every line** — XLE's three sub-legs disagreed
by **3.96pp on a single day**, so a sector label is demonstrably the wrong unit for at least one of
these rows, and probably more. **DEEP is where that gets fixed, not here.**

---

## §H · New digs registered by this stage

| ID | Dig |
|---|---|
| **D166** | 🚨 **`fts search` defaults to `--mode and` while `L2/news.md` specifies an OR-mode bucket sweep and never passes the flag.** Measured: 5-term rates bucket = **0** (AND) vs **1,869** (OR), with `Fed` alone = 578. **Every multi-term bucket figure in this desk's history is an AND-intersection reported as a union**, systematically manufacturing "quiet". **Fix = one flag in one L2 file; no code change.** |
| **D167** | ⚠ **Two of fifteen propositions were unscoreable because `VIXCLS` and `DTWEXBGS` did not print** — 13% of the board lost to publication lag, second consecutive run. **A proposition whose KPI is a lagging FRED series needs a stated fallback venue at registration (D1), or it is unscoreable by construction on any fast-moving day.** |
| **D168** | 🚨 **The desk's Iran-axis brackets (S8 · S52) are scoped to IRAN and are blind to the Red Sea / Saudi leg of the same conflict**, which transmits to the same crude and freight variables. A Houthi strike on a Saudi oil facility fires nothing. **Registered as a scope gap for PREMORTEM, not patched by widening S52 after the fact.** |

**ID counters verified at write time** against all `handoff/*.md` (D137): highest `M###` **M393** ·
`D###` **D165** · `R##` **R46** · `S##` **S60 (US) / S52-KR** ⇒ this stage takes **D166–D168**.

---

## §I · Hand-forward to SWEEP

1. ⚠⚠ **The market opens mid-stage. SWEEP must trim its price cache to ≤ 2026-08-04 and REPORT which
   side of 09:30 ET its pull landed on** (D74 · D31 · M204 · M247).
2. **D161's interim rule binds**: **no 🟢 count may be quoted without decomposing which axis lit it**
   — and `vol_surge` cleared Bonferroni with a **negative** IC on the KR ledger while the US ledger
   reads **positive and 구분 불가**. **W1: do not import the KR kill; DO decompose.**
3. **D126**: report which side of the `velocity` 0/300 ↔ 50/300 oscillation this run landed on.
4. **Energy is the run's contested node and its sub-legs disagreed by 3.96pp in one session** —
   SWEEP's sector aggregate for ENRG is expected to be uninformative; **say so rather than ranking it.**
5. **Materials arrives with two independent confirmations of the same UW** (S36-B, S57 branch-B
   region) — **and R41 forbids calling it "the worst on the board" without stating the scanned
   population.**

## §J · Post-run DRIFT hook

`drift_watch --report` runs at stage 10 against this file. **Anti-signals it should watch for a
burst on**: `crack level falling >3 points with WTI flat` (P4″) · `named Saudi facility impact`
(P22) · `dated reopening term` (P18″) · `HY ≥ 3.10` (P2″) · `DFII10 ≥ 2.55` (P1″) ·
`2s10s ≤ +0.20` (P13″).

---

# ★ IN-RUN CORRECTION — appended by EVENT_ALPHA (append-only), same run, ~10:2x ET

## §C-2 and P22 named the wrong OBJECT: the Houthi target was a TANKER, not a facility

**What this stage wrote**: *"a Houthi missile hit a **SAUDI oil facility** the same day"* (§C-2) and
**P22**'s KPI as *"a **named Saudi facility** with a confirmed production or export impact."*

**What the body-read returned** (EVENT_ALPHA Card 3, from bodies rather than titles):
`hellenicshipping` — *"Yemen's Houthis claim ballistic missile strike on **Saudi oil TANKER in the
Red Sea**"*; `zerohedge` — *"Brent Bounces As Houthis Attack, **Sink Vessel** Off Yemen With Sea
Drone"*.

⇒ **The transmission is FREIGHT and war-risk premium, not crude production or export capacity.**
**P22's direction survives** (an escalation printed on the de-escalation day and no bracket owns it)
**and P22's KPI is wrong as written.** ⇒ **KPI corrected to: a named Saudi FACILITY (not a vessel)
with a confirmed production or export impact, ≥2 independent outlets on one primary — vessel strikes
alone do NOT satisfy it.** ⚠ **The original wording is left standing above rather than edited away,
per the append-only convention; this block is the authoritative version.**

★ **And the corrected object produced a better finding than the wrong one.** The same body-read
surfaced `hellenicshipping` — ***"Four in five vessels talk their way past Bab el-Mandeb"*** — which
is the **same pattern CENTCOM describes in Hormuz**: *passage by escort and negotiation, not by
settlement*. **Two chokepoints, one mechanism, measured on two independent physical series.** That
strengthens §C-2's "Reading 2" (the price is running ahead of the event) on evidence §C-2 did not
have when it was written.

⚠ **This is the D48 pattern — a later stage killing a claim its own earlier stage wrote the same
morning — 1st US instance this run.** It is recorded as evidence that the mandatory body-read step
is doing work, not as an incident.

---

# §5 · ADDENDUM — appended by DRIFT (stage 10), 2026-08-05 ~10:2x ET · **append-only, nothing above is rewritten**

## A-1 · ⚠ Instrument failure, logged and substituted (D17 class, 7th instance)

`python -X utf8 scripts/drift_watch.py --report …/MACRO_REPORT.md` **failed twice** (retried once per
the unattended-run rule):

```
drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용).
허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']
```
⇒ **`drift` is not in `__main__.DB_READ_CMDS`, so the server refuses to execute it**, while
**P6 means the client owns no local news DB** (`sqlite3.OperationalError: unable to open database
file` on the `DEGAJA_NEWS_API=` fallback). **The stage's own primary instrument is unreachable by
construction on a client machine.** ⚠ **The documented substitute `burst` ALSO failed** — the news
API returned `TimeoutError: The read operation timed out` on two consecutive calls, then recovered.
**Registered as `D172`: `drift` and `burst` are both unavailable to a client-side DRIFT stage —
`drift` permanently (allowlist), `burst` intermittently (API timeout).** ★ **The fix for the first
is one line in `__main__.DB_READ_CMDS` plus a server `git pull` + API restart; it needs no new code.**

**Substituted with the allowlisted path**: targeted `fts search --count` + `search --field title`
on this report's own registered anti-signal terms. **Counts, 1 day, `--scope foreign`:
`Hormuz` 611 · `Saudi` 181 · `refinery` 103.**

## A-2 · 🚨 THE OBJECT MOVED AFTER THE BASELINE — and it moved against the tape, not with it

Two items are in the pool that were **not** in §C-2's read when this report was written:

| Source | Item | Why it matters |
|---|---|---|
| `fortune` [6,828자] | ***"Trump claims — YET AGAIN — that a deal to reopen Hormuz is close"*** | **The outlet is flagging the repetition itself.** §C-2 refused S52 branch A because the wording was *"a repeat of the 08-02 conditional"*; **an independent outlet reached the same characterisation on its own.** ⇒ **P18″'s refusal is corroborated from outside the desk.** |
| `zerohedge` **[title-only, D6 C-grade]** | 🚨 ***"Iran Set To Emerge With MORE Hormuz Leverage Than Before The War Under Draft US-Oman Deal"*** | **Two genuinely new facts: (a) a DRAFT text is reported to exist — closer to S52-A's bar than any verbal conditional so far; (b) its reported TERMS point the opposite way from the tape.** |

★★★ **And (b) is a direct contradiction of the primary quote this report is built on.**
**Bessent, on the record**: asked whether a deal would let Iran charge a toll — ***"I think it would
be freedom of movement."*** **The draft, as reported**: Iran emerges with **MORE** leverage than
before the war. **Those two statements cannot both describe the same agreement.**

⇒ **What this does and does not do:**
- **It does NOT fire S52 branch A.** A *draft* is not *"a dated Strait-reopening term in a primary
  text"*, and the source is **title-only, single-outlet, C-grade (D6)**. **The bar is not lowered
  because the story got more interesting.**
- **It does NOT change S52's tracking-C status, and it does not reopen S49.**
- ⚠⚠ **It DOES sharpen §C-2's "Reading 2" and it is the third independent datum for that side**,
  after the tanker lull and the Houthi Red Sea strikes: **the market is pricing a settlement whose
  reported draft terms are worse for the de-escalation trade than the verbal framing implies.**
  Same session, `aljazeera`: ***"US stock market hits record high amid hopes for Strait of Hormuz
  reopening"*** — **the tape is at a record on the hope while the draft's reported terms are
  contested.**

## A-3 · What this ADDENDUM changes in the report above — stated precisely

| Item | Status |
|---|---|
| **P18″** | **STRENGTHENED, not revised.** Its refusal now has independent outlet-level corroboration (`fortune`) and a reported-terms contradiction (`zerohedge` vs Bessent). **The proposition's KPI is unchanged**: *the OPENING, not the deal, carrying a date or "effective" language in a primary text.* |
| **S52** | **Still tracking C. Branch A NOT fired.** ⚠ **A new sub-observable is named for the 08-06 run**: *does a draft text surface in a primary source, and does it contain a toll/leverage term?* **If it does, Bessent's "freedom of movement" becomes a scoreable false statement about the object** — which is a different and sharper test than the one S52 currently holds. **Named, NOT registered** — registering a new bracket at DRIFT would bypass PREMORTEM's D93 band discipline. **PREMORTEM's job on 08-06.** |
| **§C-2's two readings** | **Reading 2 gains its third datum.** Neither reading is resolved; **the run's C2 discipline holds.** |
| **P22 (Red Sea)** | **Unchanged.** No named Saudi facility impact appeared; `Saudi` at 181 hits/1d is elevated but the corrected KPI (a **facility**, not a vessel) is still unmet. |
| **P4″ · P1″ · P2″ · P13″ · P23 · P24 · P25** | **No burst against any of their anti-signals.** The crack, credit, rate and labour terms produced nothing after the baseline. |

## A-4 · ⚠ Clock disclosure — this DRIFT ran EARLY

The L1 specifies **post-run, +3–6h**. **This stage ran ~1h after MACRO's baseline, at ~10:2x ET, with
the US market open ~51 minutes.** ⇒ **the post-close drift window is NOT covered by this run**, and
that includes **the PSX earnings call at 12:00 ET**, which is the residual on this sheet's own
🟡PARTIAL tag for PSX. **The 2026-08-06 run inherits an uncovered drift window, and it is named here
rather than left to be discovered.**
