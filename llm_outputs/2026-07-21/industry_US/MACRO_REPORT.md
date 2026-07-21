# MACRO_REPORT — industry_US · 2026-07-21 (Tue)

> Stage 1 / L1·MACRO. Runtime `--market us`, English-pure. Primary data: `module_macro_us` [FRED],
> `us_flow --cot` positioning, `module_news_data` events (`brief --body 2`, 07-20 + 07-21) +
> `thread --days 7` trajectories + 7-bucket velocity + blindspot, tape via `module_flow` / yfinance.
> Deliverable = the **§4 transmission matrix** (ROTATION's input). Zero buy/sell calls.
> Continuity anchor: `llm_outputs/2026-07-19/industry_US/MACRO_REPORT.md` (incl. its DRIFT addendum).
> Handoff ledger mode: **`DEGAJA_REPORT_DIR=llm_outputs module_report_tags show`** —
> 201 reports / 272 tickers / 15 sectors, updated 2026-07-20T00:27. Inherited coverage read from it.

---

## ⚠⚠ THE CAVEAT THAT INVERTS FROM LAST RUN
The 07-19 report ran on a **Sunday**, with a Friday tape blind to a weekend escalation. **This run has
the opposite problem, and it is smaller but real:**

- **The tape is asof the 2026-07-20 (Mon) close — the first full post-escalation session. That is good.**
- **The FRED daily curve prints stop at 07-17.** Fed funds, 10Y, 2Y, real 10Y, DXY and the FRED VIX
  **do not contain Monday.** Every rate number in §1 is **1 session behind the equity tape**.
- **Today's (07-21) news pool is 14 articles → 0 events.** The US session has not reported. The event
  axis for this run is **07-20 only**, and it is a full day (2,649 articles → 372 events, tail = 0).

**The single largest regime fact of the window is a two-sided one that landed on 07-20:**
**mediators put a 10-day ceasefire proposal to Iran** [WSJ · Bloomberg · zerohedge] — *"New Ceasefire
Hopes Add **$550 Billion** to US Stocks as Oil Retreats"* — **while the US struck Iran for a 9th
consecutive night, Khamenei called the ceasefire "worthless", Iran suspended its commitments, and the
Houthis declared a maritime embargo on Saudi Arabia [8 art / 8 outlets].**
**The TACO trigger this desk has carried as "undated" now has a document on the table and has NOT fired.**

---

## §0 Catalyst injection (run-start, `CATALYST_WATCH.json` → `llm_outputs/2026-07-21/`)
**6 binaries in window — PREMORTEM must bracket each both ways.**

| When | Event | Axis | Note |
|---|---|---|---|
| Undated / **LIVE, now concrete** | **Iran ceasefire / Hormuz (TACO trigger)** | oil | ★ Upgraded from "undated" to **a specific 10-day proposal, rejected-so-far**. The report's largest two-sided risk |
| **D-0 · 07-21 (today)** | **SCHW** earnings | FIN | The dated test of P5; **prints after this stage's data cutoff** |
| D-1 · 07-22 | **TSLA** earnings | DISC | TSLA −2.96% on 07-20 into it; robotaxi/Optimus expectations |
| D-1 · 07-22 | **KMI** earnings | ENRG | ⚠ 07-17 DRIFT measured this date as a pattern-estimate that slipped to 07-23 — **still unverified** |
| D-2 · 07-23 | **RTX** earnings | INDU/defense | ★ The dated test of P4's revival condition |
| D-2 · 07-23 | **LMT** earnings | INDU/defense | ★ Same |

**Not in `CATALYST_WATCH.json` but carried forward from the 07-19 PREMORTEM/DRIFT and confirmed on the
07-20 tape** — *"Earnings live: **Google, Tesla** to kick off 'Magnificent Seven' q…"* [10a/3s],
*"Here are the major earnings **before the open Tuesday**"* [3a/2s]:
**GOOGL 07-22 · INTC 07-23** (INTC = P2′'s dated falsification test). ⚠ The calendar still does not
carry them. Filed against the calendar for a third run.

---

## §1 Regime read — primary numbers explicit

### ★ The core wedge this run: **the AI de-rate split in two, and only half of it survived**
The 07-19 report ran one proposition (P2′) over the whole AI complex, with an explicit falsifying
price: **"MU reclaims 848.95."** On 07-20 **MU closed 865.46 (+1.94%)**. **The line was reclaimed —
the named falsifying observable fired.** At the same time, on the same day, in the same complex:
**IBM is −26.61% over five sessions on 2.44× volume**, the largest single-name move on the board.

**The complex did not move together, so it can no longer be carried as one proposition.** §4a splits it.

### The primaries [FRED — asof dates explicit, freshness flagged not assumed]
| Series | Latest | vs 07-19 report | Read |
|---|---|---|---|
| Fed funds | **3.63%** (07-17) | 3.63 flat | Policy unchanged — the repricing is still in the curve, not the target |
| US 10Y | **4.55%** (07-17) | 4.57 → **−2bp** | Long end came **back down** |
| US 2Y | **4.18%** (07-17) | 4.16 → **+2bp** | ★ Front end still rising while the long end falls |
| **2s10s** | **+37bp** | was **+41bp** (and +42bp on 07-15) | ★★ **Bear-flattening ACCELERATED.** 42 → 41 → **37** |
| Real 10Y | **2.31%** (07-17) | 2.35 → **−4bp**; +37bp/120d | ⚠ **Fell** — the RE/UTIL cost driver eased slightly |
| Core CPI idx | 336.065 (**Jun**) | unchanged | ⚠ ~1mo lag |
| CPI idx | 332.568 (**Jun**) | unchanged | Realized June disinflation, **stale** |
| Unemployment | 4.2% (**Jun**) | unchanged | Labor firm |
| **DXY** | **120.53** (**07-17**) | was 120.50 (**07-10**) | ★ **The 07-19 blind spot is now 90% closed** — DXY is 1 session stale, not 9. It rose 120.33→120.53 into the escalation |
| VIX | 18.77 (07-17, FRED) | — | live **^VIX 18.65** (07-20, +8.7%/5d) — off the Friday spike |
| M2 | $23,052B (**May**) | expanding | Liquidity tailwind, lagging |

⚠ **Freshness discipline, restated because it changed shape:** last run the monthlies were the stale
part. This run **the dailies are stale too** — every curve print above is 07-17 and the equity tape is
07-20. A Monday that added **$550B of US market cap on ceasefire hopes** is **not in the 2s10s figure.**

### The tape [yfinance, asof 2026-07-20 close — the first full post-escalation session]
| Ticker | Last | 1d | 5d | 1m | Flow (`module_flow`) | Read |
|---|---|---|---|---|---|---|
| **CL=F** | **82.20** | **−0.35%** | +5.2% | +7.1% | — | ★ **Crude fell on the day** — the ceasefire proposal capped it. Still elevated, no longer compounding |
| **BZ=F** | 88.61 | +0.58% | +6.4% | +11.4% | — | Brent held better than WTI |
| **VLO** | **313.31** | **+1.18%** | +5.9% | **+30.7%** | **RS20 +33.2%, 매집** | ★★ **Up on the day crude fell.** The P3′ anti-fragility claim got a live test and passed |
| **MPC** | 315.31 | +0.87% | +6.2% | +28.9% | RS20 **+30.4%**, 매집 | Improved from +27.5% |
| **PSX** | 208.80 | +0.94% | +5.3% | +24.9% | RS20 **+26.3%**, 매집 | Improved from +23.4% |
| XOP | 170.04 | −0.08% | +2.9% | +9.7% | RS20 +11.5%, 매집 | E&P lags refining by ~3× |
| XLE | 57.94 | +0.45% | +2.1% | +6.8% | RS20 +8.4%, **매집** | Sector-level accumulation intact |
| **MU** | **865.46** | **+1.94%** | −7.6% | −17.0% | RS20 −23.1%, **분산**, vol 0.86× | ★★ **RECLAIMED the 848.95 kill-line.** But see the quality caveat below |
| **IBM** | **213.00** | +0.16% | **−26.61%** | −18.8% | RS20 −13.9%, **분산**, **vol 2.44×** | ★★ **The board's largest move and its only 2.4× volume print.** Software-AI de-rate, violently confirmed |
| SMH | 558.83 | +0.41% | −4.6% | −10.4% | RS20 **−14.7%** (was −11.1%), 분산 | ⚠ **Deepened** even as MU bounced |
| TSM | 402.30 | +0.99% | −4.6% | −6.9% | RS20 −12.3%, 분산, **vol 1.24×** | Still distributing on real volume |
| AMD | 503.57 | +1.58% | −5.8% | −1.7% | RS20 −5.7%, 중립 | Microsoft AI deal [32a/4s] |
| NVDA | 203.28 | +0.23% | −0.1% | −0.7% | RS20 −2.9%, 분산 | Flat |
| QQQ | 696.06 | +0.10% | −2.2% | −3.6% | RS20 −5.4%, 분산 | — |
| **SPY** | **742.09** | −0.16% | **−0.95%** | +0.4% | RS 0.0%, 분산, vol 0.89× | ★ **Less bad than last run's −1.54%/5d** — the de-risking qualifier weakened again |
| ^VIX | 18.65 | −0.64% | +8.7% | +1.1% | — | Came off the Friday 18.77 spike |
| XLF | 56.04 | −0.39% | −0.1% | +4.0% | RS20 **+5.2%**, 매집, **vol 1.10×** | ★ The **only** sector ETF with a volume surge >1.0× |
| **XLV** | **159.25** | **−1.14%** | **−1.34%** | +6.1% | RS20 +7.2%, 매집 | ★ **The worst sector on a risk-on day.** Behaving as a hedge, exactly as 07-19 DRIFT said |
| XLK | — | — | — | — | RS20 −7.6%, 분산, vol 0.67× | — |
| XLI | — | — | — | — | RS20 −0.9%, 중립, vol 0.89× | Sector ETF still says nothing |
| XLY | — | — | — | — | RS20 −1.6%, RS60 **−8.0%**, 중립 | — |
| XLP | — | — | — | — | RS20 +2.5%, 중립 | Still **no** accumulation |
| XLU | — | — | — | — | RS20 +1.0%, RS60 −4.2%, **분산** | AI-power headlines are **not** in the sector ETF |
| XLB | 50.03 | −0.99% | −1.1% | −3.5% | RS20 −2.8%, RS60 −7.8%, 분산 | — |
| **XLRE** | 45.23 | −0.42% | +1.2% | +3.8% | RS20 **+3.7%** (was +3.0), **매집** | ★ Divergence (a) **widened**, and real 10Y **fell** to 2.31 |
| **RTX** | 194.44 | +0.48% | −1.0% | +1.0% | RS20 **+5.4%**, **매집**, vol 0.72× | ★ **Flipped to accumulating** |
| **GD** | 370.60 | +0.55% | −0.6% | +2.6% | RS20 **+6.5%**, **매집**, vol 0.88× | ★ **Flipped to accumulating** |
| LMT | 509.54 | +0.15% | −2.1% | −4.3% | RS20 **+0.3%** (was −16.6% RS60), 중립, **vol 0.71×** | RS stopped falling; **no volume** |
| NOC | 523.96 | +0.46% | −3.3% | −4.8% | RS20 +1.1%, 중립, vol 0.98× | Same |
| GEV | 1079.18 | **+2.02%** | +3.5% | +2.9% | RS20 −2.1%, 중립 | Price up, flow flat |
| VST | 157.99 | +1.64% | −0.1% | −0.4% | RS20 −2.9%, 중립 | AI-power flow **not** confirming the headlines |
| IREN | 40.20 | **+19.57%** | +3.1% | −30.8% | RS20 −32.3%, 분산 | $9.8B-class AI datacenter leases; a **−31%/1m** name bouncing, not a trend |
| TSLA | 369.57 | **−2.96%** | −6.4% | −6.8% | RS20 −7.1%, 중립, vol 0.64× | Into the 07-22 binary |

**⚠ The MU reclaim, judged honestly rather than mechanically.** The rule fired, and it is recorded as
fired. But the *quality* of the fire is poor: it happened **in one session**, on a **market-wide
ceasefire-relief day** that added $550B of cap, with MU's OBV still **distributing**, volume **0.86×**,
RS20 **deteriorating** (−23.1%), and **SMH's RS20 getting worse (−11.1% → −14.7%)** on the same day.
**A kill-line reclaimed on beta, on below-average volume, with the sector's relative strength still
falling, is a falsification that must be honored and distrusted at the same time.** §4a does both:
P2′ is **split and downgraded from CONFIRMED to CONTESTED**, and a **harder, volume-qualified line is
set** rather than quietly moving the goalposts.

---

## §2 Positioning — CFTC COT [`us_flow --cot`; Tue-close, 3–4d lag → **context, not a trigger**]
| Instrument | Net spec | Wk Δ | 1Y %ile | Tag |
|---|---|---|---|---|
| **Nasdaq-100** | −10,313 | −1,572▼ | **4%ile** | 🔴 crowded-SHORT — **unchanged, still unlit** |
| **Nat Gas** | −178,612 | −13,305▼ | **6%ile** | 🔴 crowded-short |
| **WTI Crude** | +19,783 | −1,139▼ | **10%ile** | 🔴 crowded-SHORT |
| **Copper** | +64,385 | +113▲ | **95%ile** | 🟢 crowded-LONG (overheated) |
| S&P 500 | −38,938 | +3,953▲ | 78%ile | 🟡 |
| Russell 2000 | +103 | +990▲ | 67%ile | 🟡 |
| USD Index | +13,173 | −96▼ | 58%ile | 🟡 |
| UST 10Y / 2Y | −831,675 / −1,157,477 | −17,413▼ / +103,531▲ | 22% / 52%ile | 🟡 |
| Gold / Silver | +186,682 / +25,074 | −7,564▼ / −2,941▼ | 23% / 40%ile | 🟡 |

⚠ **The COT print is byte-identical to 07-19's.** CFTC publishes Friday on Tuesday-close data; no new
release has landed between the two runs. **This table carries zero new information this run** — stating
that plainly rather than re-reading the same numbers as if they were fresh evidence.

### Obeying §5 failure class 2 (positioning may only AMPLIFY, never BE, a proposition)
- **WTI 10%ile** — its catalyst (escalation) is now **contested by a ceasefire proposal**. It amplifies
  P3 *less* than last run, and it is symmetric ammunition: a ceasefire squeezes nothing, it just removes
  the bid. ✅
- **Nasdaq 4%ile + record short bets against US equities** [3a/2s] + **hedge funds selling US tech at a
  record pace** [Goldman, 4a/3s] → this is now **three independent readings of the same crowded short**.
  It STILL does not promote IT on its own. But **MU's kill-line reclaim is the first thing resembling an
  igniter in five runs**, and §4a names exactly what would count as one. ✅

---

## §3 Narrative — events, trajectories, velocity, blindspot

### Event axis — full denominator, `--body 2`, tail = 0 [`brief --scope foreign`]
| Day | Articles → clusters → events | head / body / tail | nonmarket |
|---|---|---|---|
| **07-20** | **2,649 → 878 → 372** | 17 / **355** / **0** | 0 |
| **07-21** | **14 → 0 → 0** | 0 / 0 / 0 | 0 |

**All 372 event lines for 07-20 were read** (tail = 0; the terminal view caps the body at 30 rows with
`… 외 325개`, so the remaining 325 were read from `out/news_brief/2026-07-20_foreign.json` — **the
display cap is a second, undocumented sampling trap on top of the tail, and it was defeated**).
`nb` is null throughout (foreign scope filters nothing) — **nothing was silently excluded.**

**07-21 is empty and that is a fact, not an omission:** the pool holds 14 articles and 0 events. The US
session has not reported into the DB. Any claim about "today" in this report would be fabrication.

**War / oil — two-sided on the same day:**
- [**33a/7s**] ***Oil prices reverse lower amid report of 10-day cease-fire*** ← ★ the TACO proposal
- [13a/**7s**] *US petrol prices climb back above **$4** as Iran war intensifies*
- [11a/6s] *US launches fresh strikes on Iran, as Trump warns of retaliation*
- [**8a/8s**] ***Yemen's Houthis announce 'maritime embargo' on Saudi Arabia*** ← a **new** supply vector
- [8a/5s] *Magnolia Oil & Gas to Acquire WildFire Energy for **$4.06 Billion*** ← ENRG M&A at the top
- [5a/3s] *Brent: **Geopolitics support crude and cracks** – Societe Generale* ← names the crack leg
- [4a/3s] *President Trump Just **Reimposed the Iran Blockade***
- [3a/3s] *Ten killed as Russian attacks on **merchant ships in Black Sea** intensify*
- [2a/2s] *WTI Oil rally **takes a breather** as Tehran leaves the door open to diplomacy*
- [2a/2s] *How **Houthis' Red Sea Threat** Risks Bigger Oil Shock* · [2a/2s] *U.S. hits Iran for **ninth consecutive night***

**AI / semis — the split, visible in one day's tape:**
- [**32a/4s**] ***AMD Jumps on Expanded Microsoft AI Deal***
- [7a/2s] ***Micron Says Memory Chip Supply Will Remain Tight Beyond 2027***
- [2a/2s] ***Chip industry lead time continues to accelerate, pricing rises*** — Susquehanna ← **pricing power**
- [5a/2s] *TSMC sees long-term AI chip demand as **Arizona investment expands to $265 billion***
- [6a/2s] *Could AI chip boom make **ASML Europe's first trillion-dollar firm**?* · [2a/2s] ASML €20k retention bonus
- [17a/4s] *Alphabet Readies **AI Chip With Built-In Gemini***
- [6a/2s] *Dow Rises On **Peace Hopes**; Nvidia, Micron, Sandisk **Rebound***
- **↔ against:**
- [**6a/2s**] ***Why Did IBM Stock Plunge 25% in One Day?*** ← ★★ the counter-move
- [2a/2s] ***SOXX Enters Bear Market***: Yardeni says semis could fall **another 12%**
- [**4a/3s**] ***Goldman Says Hedge Funds Sell US Tech Stocks at Record Pace***
- [**3a/2s**] ***Short Bets Against US Equities Hit Record*** as AI Risks Mount
- [3a/2s] *Why **China's Kimi K3** is sparking anxiety in Silicon Valley* · [2a/2s] *Kimi 3.0 Might Be a **DeepSeek Moment***
- [3a/3s] *TSMC, SK Hynix, NVIDIA: **Only 1** Chip Stock is a Screaming Buy Amid the **Semi Meltdown***
- [4a/2s] *South Korea's **Kospi drops 4.5%*** as some AI stocks swoon

**Trade — ★ the run's genuinely new axis:**
- [**9a/9s** — dispersion **1.00**] ***Trump imposes 50% tariff on Canadian imports*** ← max dispersion on the board
- [8a/5s] *U.S. hits Canada with stiff new tariffs, **escalating trade tensions***
- [3a/3s] *Trump order targets **China-linked military mineral** supply chains*
- [5a/3s] *China is exporting **20% fewer magnets** to US despite trade truce*
- [2a/2s] *US Offers to **Halve Aluminum Duties** for Firms Building in US* · [4a/3s] *EU Expects to Hit **$1.35T** Spending Goal Agreed With Trump*

**Rates / Fed / credit:**
- [7a/3s] *Fed Chair Kevin Warsh **Vowed to End 5 Years of High Inflation*** · [3a/2s] *The new Fed boss is **tight-lipped***
- [3a/2s] ***Inflation is broadening out**, says Goldman economist* · [3a/2s] *Fed's July Inflation Forecast… a **Red Flag***
- [7a/2s] *USD Index struggles to lure buyers despite Iran tensions, **Fed hike bets***
- **↔ anti:** [3a/2s] *Dollar struggles as **softer inflation dims Fed hike bets*** · [3a/3s] *Canada's June inflation **cools to 2.8%***
- [**7a/5s**] ***NY Fed survey finds highest credit application rate in nearly…*** · [3a/2s] *student-loan **defaults** surge post-forbearance*
- [3a/2s] ***Jamie Dimon** says markets underestimate risks and **he wouldn't buy stocks or Treasurys*** at current prices
- [2a/2s] *The **$1.5 Trillion** Warning Signal: **Leverage Is Peaking*** · [3a/2s] *Bond Market's Yields Have a **Chilling Message** for Stocks*
- [3a/2s] *Gilts Fall as **Burnham's Fiscal Flexibility** Comments Spook Market* ← the UK PM change [26a/**9s**] has a rates leg

**Defense / aerospace — ★ the first activity in five runs:**
- [12a/4s] ***Boeing Wins Big As Farnborough Airshow Takes Off. Airbus, RTX…*** · [3a/2s] *Boeing Lands **100-Jet SMBC Order***
- [5a/4s] ***Lockheed Martin unveils lower-cost Patriot missile, counter-drone***
- [13a/4s] *GE Aerospace unveils **breakthrough in hybrid-electric flight***
- [7a/5s] *Trump's new Air Force One to be **'maxed out'** following missile…* · [3a/3s] *Cathie Wood Adds $18M Worth Of SpaceX, **These Defense Names***
- [2a/2s] ***Archer, Anduril** unveil autonomous aircraft platform for defense*

**Financials · Health · AI-power · Consumer (the rest of the regime-relevant read):**
- FIN: [5a/3s] *Morgan Stanley becomes Wall Street's **top bank for AI debt deals*** · [2a/2s] *Goldman **Breaks Own Stock-Trading Revenue Record** Again* · [3a/2s] Zions Q2 · [2a/2s] *W. R. Berkley **down as Q2 revenue falls short***
- HLTH: [4a/3s] *Novartis faces **drug pipeline test** with valuation premium in focus* · [2a/2s] *Samsung Biologics to acquire **PolyPeptide $1.81bn*** · [11a/2s] *Bristol Myers **buys Nvidia's** latest AI computing system* · [3a/2s] *Vertex **Dipped** More Than Broader Market*
- AI-power: [8a/4s] *IREN Lifts AI Cloud Revenue Target; **Hut 8 Lands $9.8 Billion** Deal* · [4a/2s] *AI Energy Infrastructure: These Stocks **Eye Buy Points, One Breaks Out***
- DISC: [**28a/7s**] ***Companies Are Beginning to Rehire After AI Layoffs*** ← the run's one clean labor positive · [3a/2s] *Ryanair profits drop as **Iran war** puts off passengers and **lifts fuel costs*** ← the oil→consumer transmission, priced · [2a/2s] *Domino's shares jump as franchise operators **spend more on ingredients***
- China stimulus: [2a/2s] *China's **'national team' buys $9bn** of shares to prop up market* · [4a/3s] *Hang Seng jumps on **stimulus hopes***

⚠ **Fourth consecutive run confirming the `--body 2` rule, and this run adds a second trap.** Every
item above that changes a tilt — the Houthi Saudi embargo (8 outlets, but in the body), record hedge-fund
tech selling, record equity shorts, Micron's supply-tightness call, chip pricing power, the Patriot
unveil, Dimon's warning — **sat below the head**. And **325 of the 355 body rows are not printed by the
terminal view at all**; they had to be read from the JSON artifact. **A stage that reads only stdout is
still 87% blind even with `--body 2`.**

### Trajectory axis [`thread --date 2026-07-20 --days 7 --scope foreign --top 25`]
⚠ **A tooling trap caught and worked around, stated because it would have inverted the whole read.**
Run with the default window end (today, 07-21), the unit reports **0 alive threads and 122 ENDED** — the
07-21 pool is empty, so *every* thread mechanically dies. That is the L3's documented
"holiday/low-volume window end inflates FADING" failure in its most extreme form. **Re-run with
`--date 2026-07-20`: 77 alive threads, 146 multi-day.** The per-day denominators are the tell and were
read first: `07-14 211 · 07-15 202 · 07-16 226 · 07-17 267 · 07-18 98 · 07-19 100 · **07-20 372**`.

⚠ **Reading tags this run requires the inverse correction of last run.** 07-19's window ended on a
weekend trough (46 events) and printed false FADING. **This window ends on a 372-event spike — 3.7×
the weekend and 1.4× the prior weekday peak — which mechanically inflates BUILDING/REIGNITED.** Curve
shape is being read against that, not naively.

| Thread | Curve (outlets) | Tag | Corrected read |
|---|---|---|---|
| **Oil / Middle East fighting** | 9→8→5→6→2→4→**7** | FADING | ★ **Not fading — re-accelerating.** It was tagged FADING at 07-19 too, and the curve has since turned back up 2→4→7. The 07-19 rule (*"an ENDED/FADING thread whose physical driver is live is an attention gap, not resolution"*) was **right twice** |
| **US airstrikes on Iran** | 3→4→7→3→7→8→**6** | FADING | Same family. Peaked at **8 outlets on 07-19** — the escalation. **6 outlets on a 372-event day is a bigger share than 8 on a 100-event day** |
| **Houthis / Saudi** | 4→**8** | **REIGNITED** | ★ **The cleanest new signal in the trajectory set.** Dormant since 07-14, back at **8 outlets** with a *maritime embargo*. A supply vector **independent of Hormuz** |
| **US petrol >$4 / gold** | 2→3→2→5→2→**7** | REIGNITED | The **consumer-facing** leg of the oil shock, at its highest outlet count of the window |
| **Canada tariffs** | 5→4→3→**5** | REIGNITED | ★ Started 07-14 as *"Dongfeng eyes Canada EV entry"*, ran through *"Trump threatens Canada over wildfire smoke"*, resolved 07-20 into **a 50% tariff**. **Four days of runway, visible, and this desk did not name it** |
| **AI buildout / labor** | 3→5→3→7→3→4→**7** | BUILDING | Substance rotated again: bubble → data-center backlash → **"Companies Are Beginning to Rehire After AI Layoffs"** |
| **IBM / software** | 5→4→3→3→2→3→**2** | **FADING** | ⚠ **The clearest divergence in the set: the thread is fading at 2 outlets while the stock is −26.6% on 2.44× volume.** *"Software Stocks Sink as IBM Miss Delivers 'Devastating'"*. **Price is primary** (failure class 4) |
| **TSMC $100B US spend** | 8→3→3→**2** | FADING | Peaked 8 outlets, decayed — but the 07-20 tape carries *Arizona to **$265B***. Attention left; capex did not |
| **Chip selloff** | 3→5→2→**3** | REIGNITED | *"Chip stocks have been routed — but investors are forgetting one…"* |
| **AMD / Microsoft** | 2→**4** | REIGNITED | The MU-reclaim day's igniter candidate |
| **Warsh / Fed** | 2→**3** | BUILDING | Small but building; **P1 finally has a thread** (it had none last run) |
| **Kimi K3** | 5→2→**2** | REIGNITED | The China-model threat, alive but small |
| **SpaceX below IPO** | 3→7→4→6→2→2→**3** | FADING | Still the window's biggest by article count |
| **ENDED — NY Fed's Williams on inflation** | 6→6→5→4→3, peak 6 | ENDED | An inherited-proposition staleness flag for P1's dovish branch |

**Inherited-proposition staleness flags:** P5-banks **still has no live thread** (the only bank threads
are one-day earnings items). P7-HLTH **has no thread at all** — five runs in, health care has never
generated a multi-day narrative, which is itself evidence for the "hedge, not destination" read.

### Velocity — 7-bucket sweep [fts, foreign, 7d, OR-mode + `--syn`, **terms as separate argv**]
| Rank | Bucket (argv recorded verbatim) | 7d count | vs 07-19 | Rank Δ |
|---|---|---|---|---|
| **1** | `tariff trade China truce` | **5,628** | 3,860 | **= #1** |
| 2 | `AI datacenter power capex` | 5,355 | 3,758 | = #2 |
| 3 | `banks financials JPMorgan lending` | 4,679 | 3,266 | = #3 |
| 4 | `rates Fed inflation Warsh` | 3,899 | 2,834 | = #4 |
| 5 | `oil energy Hormuz refinery` | 3,449 | 2,364 | = #5 |
| 6 | `defense missile military Iran` | 2,432 | 1,645 | = #6 |
| 7 | `semiconductor chips memory HBM` | 2,037 | 1,429 | = #7 |

⚠ **argv are byte-identical to 07-19's** (fix-forward from that run's caveat — cross-run deltas are now
comparable for the first time). **Every bucket is non-zero.** But the honest reading:
**every bucket rose 34–48%, and the rank order is unchanged in all seven slots.** That is not seven
signals — it is **one signal: the pool grew**, because the 07-19 window contained a weekend and this one
contains a 2,649-article Monday. **No tilt in §4 rests on a bucket count this run.** Uncontaminated
company-level denominators, which are pool-size-sensitive but far less so, carry the actual news:

| Clean term | 7d now | 7d on 07-19 | Read |
|---|---|---|---|
| `Lockheed` | **50** | 19 | ★ **2.6×** — Patriot unveil + Farnborough |
| `Northrop` | **26** | 10 | 2.6× |
| `defense budget` | **64** | 33 | 1.9× |
| `munitions` | 30 | 24 | 1.25× |
| `refiner` | **301** | 184 | 1.6× |
| `refining margin` | **76** | 30 | ★ **2.5×** |
| `crack spread` | **32** | 14 | ★ **2.3×** |
| `ceasefire` | **239** | — | ★ **new** — the TACO axis now has a denominator |
| `Houthi` | **144** | — | ★ **new** — the independent supply vector |
| `Canada` / `tariff` | **561** / **516** | — | ★ **new** — the 50%-tariff axis |
| `hike` / `hawkish` / `Warsh` | **735** / **232** / **330** | 299(3d) / 93(3d) / 107(3d) | Large, and still two-sided |
| `IBM` / `software` | **210** / **1,090** | — | The de-rate's surviving half |
| `Kimi` | 163 | — | China-model threat, real denominator |

⚠ **The defense bucket contamination flagged on 07-19 (it contains `Iran`) is unfixed and the bucket is
therefore still unusable.** The clean names are what moved: **`Lockheed` 19 → 50 and `Northrop` 10 → 26
are the first real defense-industry denominators in five runs.** That is a fact about attention, and
§4a P4 checks it against volume before letting it move anything.

### Blindspot pass [27,014-article/14d window, 9,454 random sample, token-0 emergent terms]
Sample rows read **raw**. Emergent-term ranks (07-19 in parentheses):
`AI 2534 (2075) · **Earnings 1013 (741, #3→#2)** · China 873 (761) · **Iran 870 (671)** · Trump 728 (627) ·
Fed 686 (649) · **Oil 522 (417, #9→#7)** · Dollar 505 (467) · SpaceX 485 (422) · Nvidia 421 (378) ·
Apple 401 (378) · Bank 381 (307) · Meta 368 (337) · Energy 356 (302) · Inflation 339 (295)`
- **Every top-15 term rose** — same pool-growth caveat as the buckets. The **rank jumps** are the signal:
  `Earnings` #3→#2 (the Mag-7 week) and `Oil` #9→#7 **while crude went sideways** — attention is *still*
  arriving at oil after the price already moved.
- **`Iran` #4 (870) holds its rank** against a 50%-larger pool — the war is not losing share.
- ★ **`Canada` does NOT appear in the top 30, despite 561 hits/7d and a 9-outlet 50%-tariff event.**
  This is the blindspot pass working as designed and as a warning: a 14-day emergent-term window
  **structurally cannot see a one-day regime event**. **The 50% Canada tariff is a genuine blind spot
  of the term axis, caught only by the event axis.** Named, not papered over.
- **`Dollar` #8 (505) — the 07-19 blind spot is now mostly closed**: DXY is 1 session stale (120.53,
  07-17), not 9 days. It rose into the escalation. Remaining gap: no DXY print for the $550B relief day.
- Raw sample rows worth the read: *"Marvell Vs. Credo: The Better Network Connectivity Stock"*
  (seekingalpha — the AI-networking sub-lane, never in any bucket); *"Microsoft and Palantir Stocks Both
  Hit **52-Week Lows**"* (yahoo — software de-rate corroborant from the blind pool);
  *"Europe's Grapes Are Withering in the Heat. **Economic Growth Could Be Next**"* (WSJ — a European
  agri/climate lane); *"Top 5 Australian Mining Stocks"* (nasdaq — MATR outside the copper story).
- **Living term-table additions:** `ceasefire` · `Houthi` · `maritime embargo` · `Canada tariff` ·
  `chip lead time` · `memory supply tight` · `hedge fund tech selling` · `record short` · `Farnborough` ·
  `counter-drone` · `AI rehire` · `network connectivity` · `52-week low`.

---

## §4 ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)
> Wind direction only, one line per GICS sector. Not equal-weight analysis. Proposition IDs in §4a.
> **All flow tags asof the 2026-07-20 close (post-escalation). All rate inputs asof 07-17 (1 session behind).**

| # | GICS Sector | Tilt | Δ vs 07-19 | Prop | One-line why |
|---|---|---|---|---|---|
| 1 | **Energy (ENRG)** | **OW ★strongest** | = (composition shifts) | P3, P3′ | **VLO/MPC/PSX RS20 +33.2/+30.4/+26.3, ALL improved, ALL accumulating** — and **VLO rose +1.18% on the day crude fell −0.35%**. `refining margin` 2.5×, `crack spread` 2.3×. XLE 매집 +8.4%. New independent vector: **Houthi maritime embargo on Saudi [8 outlets]**. **⚠ The TACO trigger is now a concrete 10-day proposal — no longer hypothetical** |
| 2 | **Financials (FIN)** | **OW (on flow only)** | ↑ to #2 by default | P1, P5 | **XLF RS20 +3.8→+5.2%, accumulating, vol 1.10× — the ONLY sector ETF with a volume surge.** Goldman record trading revenue; MS top AI-debt bank. ⚠ Thesis still broken (2s10s +41→**+37bp**), no live thread, and the credit anti-signals multiplied: **NY Fed record credit-application rate, student-loan defaults, Dimon "wouldn't buy stocks or Treasurys", "$1.5T leverage peaking"**. **SCHW prints today** |
| 3 | **Information Tech (IT)** | **UW → Neutral (SPLIT)** | ★★ **↑ from UW** | P2a, P2b | ★ **The falsifying observable fired: MU reclaimed 848.95 → 865.46.** Hardware corroborants are real and multiplying (**Micron: supply tight beyond 2027; chip lead times accelerating with pricing rising; TSMC Arizona $265B; AMD×MSFT**). ⚠ **But software is the opposite trade: IBM −26.6%/5d on 2.44× vol.** And SMH RS20 **deepened to −14.7%**. **One sector, two signs — ROTATION must split it** |
| 4 | **Health Care (HLTH)** | **OW → Neutral (hedge role)** | ★ **↓ from OW** | P7 | **Downgraded on its own evidence.** XLV RS20 +7.2% and accumulating — but it was **the worst sector on 07-20 (−1.14%) on a +$550B risk-on day**, and −1.34%/5d. That is the definition of a hedge, confirming 07-19 DRIFT's β −0.16 finding. **An OW built on "rotation destination" is not supported; a hedge allocation might be. ROTATION owns which** |
| 5 | **Industrials (INDU)** | **Neutral (two lanes, one now moving)** | = tilt, ↑内容 | P4 | **XLI RS20 −0.9%, OBV neutral, vol 0.89× — the sector says nothing.** But underneath: **RTX and GD both flipped to ACCUMULATING (RS20 +5.4/+6.5)**, `Lockheed` 19→**50**, `Northrop` 10→**26**, Farnborough (Boeing wins big, 100-jet SMBC order, GE hybrid-electric, LMT Patriot unveil). **⚠ Volume disqualifies it: LMT 0.71×, RTX 0.72×, GD 0.88× — the >1.3× revival condition is NOT met.** First crack in 5 runs; **RTX+LMT print 07-23** |
| 6 | **Comm Services (COMM)** | **UW** | = | P2b | Software/services de-rate is the surviving half of the AI trade. `software` 1,090 hits; Microsoft & Palantir at **52-week lows**; Meta Tennessee trial. Counter to watch: **Alphabet's Gemini AI chip + GOOGL 07-22** |
| 7 | **Consumer Disc (DISC)** | **UW** | = | P3, P1 | **XLY RS20 −1.6%, RS60 −8.0%, no accumulation.** The oil→consumer transmission is now **priced, not theoretical**: petrol back above **$4** [13a/7s], **Ryanair profits dropped on fuel + war**, Domino's franchisees paying more for ingredients. **TSLA −2.96% into the 07-22 binary.** ⚠ One real counter: **"Companies Are Beginning to Rehire After AI Layoffs" [28a/7s]** |
| 8 | **Materials (MATR)** | **UW** | = | P6 | **XLB distributing, RS20 −2.8%, RS60 −7.8%; copper still 95%ile crowded-long.** ★ Now with a live event: **50% Canada tariff + an offer to halve aluminum duties for US builders + a Trump order on China-linked military minerals**. Two-sided by construction — a tariff wall is input-cost negative and domestic-capacity positive |
| 9 | **Utilities (UTIL)** | **Neutral (weak)** | = | P2a | **XLU OBV DISTRIBUTING, RS60 −4.2%.** ⚠ The AI-power *headlines* were loud (**Hut 8 $9.8B lease, IREN +19.6%**) and the *sector flow* did not follow (VST RS20 −2.9% neutral, GEV RS20 −2.1% neutral). **Real 10Y fell to 2.31% — a small tailwind that has not shown up.** Headline ≠ flow, recorded as such |
| 10 | **Consumer Staples (STPL)** | **Neutral** | = | P1 | RS20 +2.5% but **OBV neutral — still no accumulation, 5 runs running.** Defensive money keeps choosing HLTH over staples |
| 11 | **Real Estate (RE)** | **UW (contested)** | = tilt, **divergence widened** | P1 | **XLRE RS20 +3.0→+3.7%, still accumulating**, and **real 10Y FELL 2.35→2.31%** — the UW's own driver eased. Against: *"Sell Alert: 3 REITs Facing Likely Dividend Cuts"*. **This is the second consecutive run where thesis and flow disagree and nobody resolved it** ← §4x (a) |

**Net wind:** **the "out of AI, into ENRG+HLTH" call of 07-19 half-broke in one session.** ENRG holds and
its *refining* leg strengthened; **HLTH revealed itself as a hedge, not a destination**; and **IT stopped
being a clean UW** the moment its own named kill-line was reclaimed. What is *new* and un-owned: a
**50% tariff on Canada**, a **Houthi blockade of Saudi Arabia**, and **record hedge-fund tech selling
into a crowded-short tape**. SPY −0.95%/5d (better than last run's −1.54%) and VIX off its spike: **the
de-risking read weakened for a second consecutive run.**

### §4x ★ Divergences ROTATION must resolve (matrix × flow, named explicitly per the L1 rule)
- **(a) RE — matrix UW, flow accumulating. UNRESOLVED FOR TWO RUNS AND NOW WIDER.** XLRE RS20 +3.0→+3.7%,
  accumulating; real 10Y fell 4bp. **Owner: DEEP.** ⚠ 07-19 assigned this to DEEP and **DEEP did not take
  it** (no `SECTOR_DEEP_RE`). **Escalated: either ROTATION resolves it or it must be explicitly declined
  in writing.**
- **(b) IT — one sector, two opposite signs. THE run's primary divergence.** Hardware: kill-line
  reclaimed, pricing power, supply tightness, $265B capex. Software: −26.6% in a week on 2.44× volume.
  **Owner: ROTATION — do not emit a single IT tilt.**
- **(c) INDU — attention doubled, flow flipped to accumulating, volume absent.** RTX/GD accumulating,
  `Lockheed` 2.6×, but every volume reading <1.0×. **Owner: DEEP/PREMORTEM.** The 07-23 prints settle it.
- **(d) HLTH — flow says accumulate, price says hedge.** Accumulating with RS20 +7.2%, yet the worst
  performer on the day the market added $550B. **Owner: ROTATION** — decide whether this desk holds
  hedges as OW positions at all. (07-19 DRIFT already found only **HUM** is genuinely orthogonal.)
- **(e) UTIL / AI-power — headline flow vs actual flow.** $9.8B lease and a +19.6% day in IREN against
  XLU **distributing** and VST/GEV neutral. **Owner: DEEP.** Is AI-power a name-level trade with no
  sector expression?
- **(f) ★ NEW — the crowded short is now triple-confirmed and still unlit.** Nasdaq 4%ile (COT) +
  *"Short Bets Against US Equities Hit **Record**"* + *"Hedge Funds Sell US Tech at **Record Pace**"*
  (Goldman). **Owner: PREMORTEM.** This is the squeeze-risk side of the IT UW, and it must be bracketed.

---

### §4a Falsifiable propositions (both branches mandatory on oscillating variables)

- **P1 — The rate axis is two-sided and bear-flattening is winning the KPI (CONTINUED, KPI moved toward
  the hike branch without crossing).**
  *Evidence: **2s10s +42 → +41 → +37bp** across three runs — 2Y 4.16→**4.18** while 10Y 4.57→**4.55**.
  `hike` **735 hits/7d**, `Warsh` **330**, `hawkish` **232**. "Warsh Vowed to End 5 Years of High
  Inflation" [7a/3s]; "**Inflation is broadening out**, says Goldman economist"; "the Fed's July
  inflation forecast contains a **red flag**". **DXY 120.53, rising.***
  **Thread:** ★ P1 now **has** a thread for the first time — Warsh/Fed **BUILDING 2→3**. The NY Fed
  Williams dovish thread **ENDED** (6→6→5→4→3).
  **Anti-signal (equal weight, mandatory):** *"Dollar struggles as **softer inflation dims Fed hike
  bets**"* [3a/2s]; Canada's June CPI **cooled to 2.8%, below estimates**; **real 10Y FELL 4bp to
  2.31%** — the market's own real-rate expectation eased in the same week the front end rose.
  **Track KPI (unchanged so the series stays comparable):** 2s10s **+37bp** (>+45bp = dovish branch,
  **<+30bp = hike branch — now 7bp away**), real 10Y **2.31%** (>2.50% = FIN duration-loss trigger),
  2Y **4.18%**. **Catalyst:** next CPI/FOMC dates **[blank]** — still not in CATALYST_WATCH; not guessed.
  ⚠ **No sector tilt in §4 rests on a hike happening.** Third run holding that discipline.

- **P2a — ★ SPLIT/NEW: the AI HARDWARE de-rate is CONTESTED — its own kill-line was reclaimed.**
  *07-19 named the falsifying price: **"MU reclaims 848.95."** **MU closed 865.46 (+1.94%). It fired.**
  Corroborants arrived with it, and they are fundamental, not price: **"Micron Says Memory Chip Supply
  Will Remain Tight Beyond 2027"** [7a/2s]; **"Chip industry lead time continues to accelerate, pricing
  rises"** — Susquehanna [2a/2s]; **TSMC Arizona expands to $265B** [5a/2s]; **AMD × Microsoft expanded
  AI deal** [32a/4s]; ASML trillion-dollar-firm talk. This is the third consecutive run in which
  independent methods flag accelerating hardware fundamentals against a falling price.*
  **Verdict: DOWNGRADED from a UW driver to CONTESTED. IT moves UW → Neutral on the hardware leg.**
  ⚠ **Why this is not a promotion to OW — the falsification is low-quality and it is named as such:**
  the reclaim took **one session**, on a **market-wide +$550B ceasefire-relief day**, with MU's OBV
  still **distributing**, volume **0.86×**, RS20 **deteriorating to −23.1%**, and **SMH's RS20 getting
  worse (−11.1% → −14.7%)**. *"SOXX Enters Bear Market"* and Yardeni's further −12% call are live.
  **Anti-signal / new kill-line (volume-qualified, so it cannot be re-fired by beta):**
  **MU holds ≥ 848.95 for 3 consecutive sessions AND SMH RS20 turns > −8%** → the de-rate is dead and
  the **4%ile Nasdaq short becomes squeeze fuel**. **Conversely, MU back below 848.95 on >1.2× volume**
  → the reclaim was relief-day beta and the UW is restored.
  **Dated test: INTC 07-23, GOOGL 07-22** — *"is raised capex rewarded on the capex line?"*

- **P2b — ★ SPLIT/NEW: the SOFTWARE de-rate is CONFIRMED, violently.**
  ***IBM −26.61% over five sessions on 2.44× volume** — the largest move and the only >2× volume print
  on the board. *"Software Stocks Sink as **IBM Miss Delivers 'Devastating'**"*; *"Why Did IBM Stock
  Plunge **25% in One Day**?"* [6a/2s]; **Microsoft and Palantir both at 52-week lows** (found in the
  blind pool); `software` **1,090 hits/7d**; the standing *"IBM: Structurally Ill-Suited To Capture AI
  Demand"* thesis. **This is the half of P2′ that survived, and it is where COMM's UW now lives.***
  ⚠ **Trajectory divergence, stated: the IBM thread is FADING at 2 outlets while the stock is −26.6%.**
  Failure class 4 applied — **price is primary, thread-tag is corroborant.**
  **Anti-signal:** a software name printing accelerating AI-attributed revenue **and being rewarded**;
  or IBM stabilizing on >1.3× volume (capitulation-then-base). **Track:** IBM 213.00, `software` count.

- **P3 — Oil war-premium (CONTINUED, but the two-sided risk became CONCRETE).**
  *CL=F 81.78 → **82.20**, +5.2%/5d; Brent **88.61**, +6.4%/5d. Petrol back above **$4** [13a/7s]. The
  escalation is intact — **9th consecutive night of US strikes**, Trump reimposed the Iran blockade,
  Trump says the MOU is "over", IRGC pledges an "unforgettable lesson", Pezeshkian calls it "full-scale
  war". ★ **NEW independent vector: the Houthis declared a maritime embargo on Saudi Arabia [8a/8s],
  REIGNITED 4→8** — a supply threat that does not run through Hormuz.*
  **Thread:** the oil thread is tagged FADING and is **re-accelerating (2→4→7)**; the airstrike thread
  peaked at 8 outlets on 07-19. **The 07-19 rule that an ENDED/FADING oil thread with a live physical
  driver is an attention gap has now been right twice.**
  **Anti-signal (equal weight — and it is no longer hypothetical): the TACO trigger has a document.**
  **Mediators floated a 10-day ceasefire** [WSJ, Bloomberg, zerohedge, 33a/**7s**]; *"New Ceasefire Hopes
  Add **$550 Billion** to US Stocks as Oil Retreats"*; *"WTI rally takes a breather as **Tehran leaves
  the door open to diplomacy**"*; `ceasefire` **239 hits/7d**. **Crude fell on the day.** Against it:
  **Khamenei called the ceasefire "worthless"** and Iran suspended its commitments. **A one-way tilt
  here remains the exact violation PREMORTEM exists to prevent — and the trigger is now days away, not
  undated.** **Track:** CL=F **82.20**, BZ=F 88.61, `ceasefire` 239, `Houthi` 144, `Iran` emergent #4 (870).

- **P3′ — The durable ENRG leg is REFINING (CONTINUED — and it passed a live test).**
  ***Every refiner improved: VLO RS20 +28.8→+33.2%, MPC +27.5→+30.4%, PSX +23.4→+26.3%, all still
  accumulating**, +25–31%/1m. ★ **The test: on 07-20 crude fell −0.35% and VLO rose +1.18%.** The claim
  that refining is mechanically separable from the crude premium got its first real trading day and
  held. Denominators confirm: `refining margin` **30→76**, `crack spread` **14→32**, `refiner`
  **184→301**. New corroborant naming the mechanism: **"Brent: Geopolitics support crude **and cracks**"**
  — Societe Generale [5a/3s]. Physical destruction continues (Black Sea merchant-ship attacks, 10 killed).*
  ⚠ **The sign of this proposition was stated three different ways inside the 07-19 run** (MACRO said
  anti-fragile to a TACO; PREMORTEM reversed it; DEEP·ENRG measured corr(Δcrack, crude) = **+0.365** and
  called it two-sided). **07-20's tape is one datapoint on the MACRO side. One day does not settle a
  +0.365 correlation — the standing DEEP verdict (genuinely two-sided) is NOT overturned here.**
  **Anti-signal (specific, unchanged):** **Russian/Ukrainian refining capacity returning** (Afipsky,
  Syzran), a lifted diesel export ban, or crack spreads normalizing. **Not** a Hormuz headline.
  **Track:** VLO RS20 **+33.2%**, `crack spread` **32**, VLO-vs-crude daily sign divergence.

- **P4 — Defense primes (STILL RETIRED — but the first genuine crack in five runs, and the date is D-2).**
  *For four runs this desk measured a perfect catalyst producing zero flow. **This run, three of the four
  inputs moved for the first time:** (1) **attention** — `Lockheed` 19→**50**, `Northrop` 10→**26**,
  `defense budget` 33→**64**; (2) **events** — **Farnborough** (Boeing wins big, 100-jet SMBC order, GE
  Aerospace hybrid-electric breakthrough), **LMT unveils a lower-cost Patriot + counter-drone** [5a/4s],
  Archer×Anduril autonomous platform, Cathie Wood adding defense names; (3) **flow** — **RTX and GD both
  flipped to ACCUMULATING** with RS20 **+5.4%/+6.5%**, and **LMT's RS stopped falling (RS60 −16.6% →
  RS20 +0.3%)**.*
  ⚠ **The fourth input did not move, and it is the one the revival condition names: VOLUME.**
  **LMT 0.71× · RTX 0.72× · GD 0.88× · NOC 0.98× — all below average. The stated condition is >1.3×.**
  **P4 therefore stays RETIRED. The condition is not "close enough"; it either fires or it does not.**
  **Revival condition (unchanged — not moved to fit the data): LMT/NOC/GD/RTX volume surge >1.3× on an
  appropriations or order event. Dated test: RTX 07-23 and LMT 07-23.**
  **Un-tunneling note carried forward:** the European defense lane (EU €1.35T spending goal, France–
  Germany nuclear deal) **still may not transmit through US primes**. Logged as a term, not a tilt.

- **P5 — Bank earnings leg (CONTINUED on flow; the anti-signals multiplied faster than the thesis).**
  *XLF RS20 +3.8→**+5.2%**, accumulating, and **vol 1.10× — the only sector ETF with a volume surge**.
  **Goldman broke its own stock-trading revenue record again**; **Morgan Stanley is now Wall Street's
  top bank for AI debt deals** [5a/3s].*
  ⚠ **Staleness flag holds: still no live bank thread** (only one-day earnings items). P1's steepener —
  the macro reason for the OW — **flattened further (+41 → +37bp)**.
  **Anti (and this run it got specific and stacked):** **SCHW prints today 07-21** (binary, after this
  stage's cutoff); **NY Fed reports the highest credit-application rate in nearly a decade** [7a/**5s**];
  **student-loan defaults surging post-forbearance**; **W. R. Berkley missed on revenue**; and the
  loudest: **Jamie Dimon says markets underestimate risks and he "wouldn't buy stocks or Treasurys at
  current prices"** [3a/2s] + *"The **$1.5 Trillion** Warning Signal: **Leverage Is Peaking**"*.
  **Track:** SCHW 07-21, XLF OBV + the 1.10× volume (does it persist), credit-cost commentary.

- **P6 — ★ PROMOTED: trade re-escalation is no longer a watch — the promotion condition fired, and the
  axis rotated from China to North America.**
  *07-19 set the condition explicitly: **"an actual Chinese retaliation headline or a formal tariff
  re-escalation."** On 07-20: **Trump imposed a 50% tariff on Canadian imports** — **9 articles / 9
  outlets, dispersion 1.00, the maximum-consensus event on the board** — plus *"U.S. hits Canada with
  stiff new tariffs, escalating trade tensions"* [8a/5s]. Alongside it: a **Trump order targeting
  China-linked military mineral supply chains** [3a/3s], **China exporting 20% fewer magnets to the US
  despite the truce** [5a/3s], and **an offer to halve aluminum duties for firms building in the US**.
  Denominators: `Canada` **561**, `tariff` **516**; the bucket is #1 at 5,628. **Thread: Canada tariffs
  REIGNITED 5→4→3→5, running since 07-14** — four days of visible runway.*
  ⚠ **The honest self-criticism: this desk watched the wrong country.** P6 was written as a China
  proposition for two runs; the escalation came against **Canada**, and the **blindspot pass could not
  see it** (`Canada` is absent from the 14-day emergent top-30 — a one-day regime event is structurally
  invisible to a 14-day term window). **Only the event axis caught it.**
  **What it moves:** it **reinforces the existing MATR UW** and adds a two-sided input (input-cost
  negative, US-domestic-capacity positive). **It does not create a new tilt** — there is still no
  measured price transmission. **Anti-signal:** the tariff is rescinded/negotiated down within days
  (this administration's established pattern), or Canadian retaliation fails to appear.
  **Track:** `Canada` 561, `tariff` 516, XLB RS20 (−2.8%), copper 95%ile.

- **P7 — Health Care (DOWNGRADED from "rotation destination" to "hedge" — on its own evidence).**
  *The flow leg is intact and improved: **XLV RS20 +6.6→+7.2%, still accumulating**. **The destination
  claim is falsified:** on 07-20, a session that added **$550B** of US market cap on ceasefire hopes,
  **XLV was the worst-performing sector at −1.14%**, and it is **−1.34%/5d**. A destination rises with
  risk appetite; a hedge falls with it. **This is precisely what 07-19 DRIFT measured independently
  (XLV β to SPY −0.16, up-day excess −0.74%) — and this run the live tape reproduced it.***
  ★ **Additional structural evidence: five runs in, HLTH has never produced a multi-day news thread.**
  A sector with sustained accumulation and zero narrative is a **positioning** phenomenon, not a
  **thesis** phenomenon — which is exactly what "hedge" means.
  **What changes:** **OW → Neutral (hedge role).** **ROTATION owns the actual question, stated plainly:
  does this desk carry hedges as OW allocations?** (07-19 DRIFT: only **HUM**, corr to SPY **+0.05**,
  is genuinely orthogonal.) New corroborants are stock-specific, not sectoral: Novartis pipeline test,
  Samsung Biologics–PolyPeptide $1.81bn, Bristol Myers buying Nvidia systems, Vertex underperforming.
  **Anti-signal:** XLV outperforms on an **up** day (which would restore the destination read), or OBV
  flips to distributing (which would kill both readings). **Track:** XLV RS20 (+7.2%), up-day excess.

---

## §5 Self-backtest — scoring the 07-19 propositions at +1 session (07-20 close, post-escalation)

| 07-19 proposition | Realized by 07-20 close | Score |
|---|---|---|
| **P3′** the durable ENRG leg is **refining** | **VLO/MPC/PSX RS20 all IMPROVED (+33.2/+30.4/+26.3), all accumulating; VLO +1.18% on a day crude fell −0.35%**; `refining margin` 2.5×, `crack spread` 2.3× | **HIT ★★** |
| **P3** oil war-premium, escalating | CL=F **82.20 (+5.2%/5d)**, Brent 88.61, petrol >$4, 9th night of strikes, **Houthi Saudi embargo REIGNITED 4→8** | **HIT** (weakened — the anti became concrete) |
| **P6** China truce risk, watch-with-teeth; promote on "a formal tariff re-escalation" | **Trump imposed a 50% tariff on Canada [9a/9s, dispersion 1.00]** + a China-mineral order + magnet-export drop | **HIT** — condition fired (**on the wrong country**) |
| **P1** rate axis two-sided, hike debate; KPI 2s10s | **2s10s +41 → +37bp** (toward the hike branch, 7bp short of it); `hike` 735/7d; **but real 10Y FELL to 2.31%** — both branches got evidence, as written | **HIT** (the two-sided framing held; no tilt rested on it) |
| **P5** bank earnings leg | **XLF RS20 +3.8→+5.2%, accumulating, vol 1.10×** (the only volume surge); Goldman record trading revenue | **HIT** (flow) / **OPEN** (SCHW prints today) |
| **P7** HLTH as the **rotation destination** (flow-led) | Flow right (**RS20 +7.2%, accumulating**); **framing wrong — worst sector (−1.14%) on a +$550B risk-on day** | **HALF** |
| **P2′** AI capex de-rate; kill-line **MU 848.95** | ★ **MU 865.46 — the named falsifying observable FIRED.** But **IBM −26.6%/5d on 2.44× vol** and **SMH RS20 deepened to −14.7%** | **HALF (SPLIT)** — hardware falsified, software confirmed |
| **P4** defense retired; revival = **volume >1.3×** | Attention 2.6×, **RTX/GD flipped to accumulating** — **volume 0.71–0.98×, condition NOT met** | **OPEN** (test dated 07-23) |

**This run: 5 HIT / 2 HALF / 1 OPEN (n=8).**
**Running hit-rate across three scored runs: 13 HIT / 3 HALF / 4 MISS / 2 OPEN (n=22) — 59% strict
(HIT/n), 66% credited (HIT + ½·HALF, excluding OPEN).** Prior two runs: 43% → 57% → **59%**.

**★ The one that matters more than the score: a named kill-line fired against this desk, and it was
reported as fired.** P2′ was the desk's highest-conviction UW driver. Its falsifying price was written
in advance, in public, as a number. **MU reclaimed it, and IT moved UW → Neutral in §4 as a result** —
rather than the line being quietly restated. **The counter-discipline was applied in the same breath:
the reclaim's quality was measured (one session, relief-day beta, 0.86× volume, RS20 still falling) and
the replacement line was made HARDER (3 consecutive sessions + an SMH RS20 threshold), not softer.**

### Recurring failure classes — carried and updated
1. **(carried, WORKING)** One-sided reads of oscillating variables → P1 and P3 both carry equal-weight
   branches. P3's anti-branch went from hypothetical to **a document on the table**. **Keep.**
2. **(carried, WORKING)** Extreme positioning may only AMPLIFY a proposition with its own catalyst →
   the Nasdaq 4%ile short is now **triple-confirmed** (COT + record equity shorts + record hedge-fund
   tech selling) and **still did not promote IT by itself**; IT moved only because **its own named
   price line broke**. **Keep.**
3. **(carried, WORKING)** An anti-signal must be the **mechanism** most likely to kill the thesis →
   P3′'s anti stays "Russian refining capacity returns", not a Hormuz headline. **Keep.**
4. **(carried, WORKING — and inverted this run)** For supply-shock assets, **price is primary,
   thread-tag corroborant.** ★ **07-19's corollary was "a weekend window-end inflates FADING." This run
   the SAME artifact ran the other way: a 372-event Monday (3.7× the weekend) mechanically inflates
   BUILDING/REIGNITED.** And the default `thread` invocation — window-ending on an empty 07-21 —
   printed **0 alive / 122 ENDED**, which would have inverted the entire narrative read.
   **Generalized rule: read the per-day denominator FIRST and, when the last day is anomalous in either
   direction, re-run the window with an explicit `--date` on the last complete session.**
5. **(carried, CONFIRMED AGAIN)** An ENDED/FADING thread whose physical driver is still active is an
   attention gap, not resolution. → The oil thread was tagged FADING for the second run in a row and
   **re-accelerated 2→4→7**. **Keep — this rule is now 2-for-2.**
6. **(carried, UNFIXED)** A bucket contaminated by a cross-domain term is worse than no bucket. → The
   `defense missile military Iran` bucket is **still contaminated and was still not used**; the clean
   company denominators (`Lockheed` 50, `Northrop` 26) carried the finding instead. **Keep, and fix the
   bucket next run.**
7. **★ NEW — cross-run bucket deltas are worthless when the pool size changes.** All seven buckets rose
   34–48% and **all seven kept their exact rank** — because the 07-19 window held a weekend and this one
   holds a 2,649-article Monday. **New rule: a velocity bucket may only move a tilt if its growth
   exceeds the pool's growth, or if a rank ORDER changes. Absolute counts across runs are noise.**
   *(Applied: no tilt in §4 rests on a bucket count this run.)*
8. **★ NEW — the 14-day blindspot window is structurally blind to one-day regime events.** A **50%
   tariff on Canada** at **9 outlets / dispersion 1.00** does not appear in the emergent top-30, because
   561 hits inside a 27,014-article 14-day pool cannot outrank a 14-day incumbent. **New rule: the
   blindspot pass discovers slow themes only. One-day regime events are the EVENT axis's job — never
   conclude "nothing new emerged" from the term axis alone.**
9. **★ NEW — `--body 2` is necessary but not sufficient: the terminal view caps the body at 30 rows.**
   Measured 07-20: head 17 / body **355** / tail 0, and stdout printed **30 body lines then
   `… 외 325개`**. **87% of the day's events are invisible to a stdout-only read even with the
   documented flag set.** Every tilt-changing item this run (Houthi embargo, record hedge-fund tech
   selling, Micron's supply call, chip pricing power, the Patriot unveil, Dimon's warning) was in the
   unprinted 325. **New rule: for a stage that must see the day, read `out/news_brief/{date}_{scope}.json`,
   not stdout.**

---
**EXIT CHECK:** ✅ catalysts injected (**6 binaries**; the undated TACO trigger upgraded to a **concrete
10-day ceasefire proposal**; GOOGL 07-22 / INTC 07-23 carried in manually — calendar gap re-filed) ·
✅ events read via `--body 2` for **07-20 (2,649 → 878 → 372, tail = 0, ALL 355 body lines read from the
JSON artifact after catching the 30-row stdout cap)**, and **07-21 declared empty (14 articles → 0
events) rather than fabricated** · ✅ trajectories read (`thread --days 7`) — **the default invocation's
0-alive/122-ENDED artifact was caught and re-run with `--date 2026-07-20` (77 alive)**; per-day
denominators read **before** tags; **every proposition names its thread's tag+curve or states "no
thread"** (P5 flagged: still no live thread; P7 flagged: no thread in five runs) · ✅ 7-bucket sweep with
**argv byte-identical to 07-19's**, every bucket non-zero — **and explicitly declared unusable for tilts
this run (new failure class 7: all seven grew with the pool and none changed rank)**; clean company
denominators used instead · ✅ blindspot pass, `sample[]` + emergent terms read raw; **the 07-19 `Dollar`
blind spot closed (DXY now 1 session stale, 120.53)**; **a NEW structural blind spot named — the 50%
Canada tariff is invisible to the 14-day term axis (failure class 8)**; new terms folded into the living
table · ✅ indicators (FRED primaries with explicit freshness flags — **the dailies are now 1 session
behind the tape, stated** — + COT positioning, **declared byte-identical to 07-19 and therefore
information-free this run**) · ✅ continuity anchor (07-19 MACRO_REPORT **incl. its DRIFT addendum**)
read; **handoff ledger read** (201 reports / 272 tickers / 15 sectors), mode stated in the header ·
✅ **11-sector transmission matrix** produced, **every matrix×flow divergence named with an owner
(§4x a–f)**, incl. an escalation of the RE divergence DEEP declined last run · ✅ self-backtest scored
with running hit-rate (**5H/2½/1O this run; 59% strict / 66% credited, n=22**) + **3 new failure
classes** · ★ **a named kill-line fired against the desk's highest-conviction position (MU 848.95) and
was reported as fired — IT moved UW → Neutral, and the replacement line was made harder, not softer.**
**→ proceed to SWEEP.**

### §5 DRIFT stamp (append-only — populated by stage 9)

## §5 ADDENDUM — DRIFT (2026-07-21 post-run) · append-only
> **Append-only by rule: not one line above this was edited.** The original call stays visible next to
> its correction — that asymmetry is what feeds the next run's self-backtest.

### ⚠ Tooling note (P6): `drift_watch.py` is unusable on this client for a THIRD consecutive run
```
drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용).
허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']
```
Identical to the 07-19 failure: a `DEGAJA_NEWS_API` route exists, but **`drift` was never added to
`__main__.DB_READ_CMDS`**, so the DRIFT stage's own tool cannot run on the machine the stage runs on.
**Filed a third time.** Worked around exactly as 07-17 and 07-19 did, via `burst` (which **is** in the
allowlist). ⚠ **A defect that survives three consecutive filings is not a fluke — it belongs in a
repo issue, not in a run log.**

### Burst scan — **no 🚨 regime flip. The report stands.**
Denominators: the **07-20** foreign pool (2,649 articles → 878 clusters → 372 events) and the **07-21**
pool, which **filled from 14 articles at report baseline to 863 hits on an OR probe by drift time** —
i.e. the day did populate after the report was written, which is exactly the condition this stage exists
to catch.

**Category ② ("words that never appear normally") returned `(없음)` — literally zero unknown-word
emergence on 07-21.** On 07-20 it returned AIRBUS · AIRSHOW · **LOCKHEED · RTX · PATRIOT** · **HELIOS ·
AZURE** · PAYPAL · LUMENTUM · CITIGROUP — **every one of which the desk had already named** (Farnborough
in EVENT_ALPHA CARD 4, the AMD/Helios deal in CARD 3 and DEEP·SEMI, PYPL in DEEP·FIN). **The blind-word
axis found nothing the desk missed — the first clean sweep in several runs.**

| Burst | z | n / outlets | Body-read verdict |
|---|---|---|---|
| **SEVEN / MAGNIFICENT** | **13.3 / 9.7** — the day's largest | 3 / 3 (dispersion **1.00**) | ★ **NOT a regime event, but NOT noise either — a third category.** Body-read: *"**Citi Says Magnificent Seven Tag Is Obsolete** in AI Stock Winners"* [Bloomberg] · *"'**Mag 7 Is Dead**'"* · *"**Everyday Investors Are Over the Mag Seven and Into New AI Darlings**"* [WSJ] · *"Why it's time to **retire** the 'Magnificent 7' name"* [MarketWatch/Citigroup]. This is a **taxonomy** story, so it moves no tilt — **but it is a dispersion signal, and it independently corroborates two findings this run reached from flow data alone**: SWEEP's *"IT = 0 green of 56"* and ROTATION §2(f)'s *"COMM's damage is mega-cap-concentrated, not sector-wide."* **Logged as corroboration, not as a new proposition.** |
| BOEING / AEROSPACE *(07-20)* | 4.4 / 3.8 | 34 / 8 · 27 / 8 | Farnborough — **already carried** (EVENT_ALPHA CARD 4). No new information. |
| AMD *(07-20)* | 2.1 | 48 / 7, **100% market-relevant** | Helios/Azure — **already carried** (CARD 3, DEEP·SEMI). No new information. |
| NETFLIX / MICROSOFT / ALPHABET / BANK | 6.2 / 4.8 / 3.4 / 3.0 | 3–4 each | Mag-7 earnings-week previews. **GOOGL prints 07-22 — already bracketed (ALPHA B3).** |

★ **Method note: the day's largest burst was body-read and correctly classified as neither regime event
nor noise.** Last run's DRIFT rejected its biggest z (Buffett, z 7.2) as syndication noise; this run's
biggest z is genuine market commentary that **moves nothing but confirms something.** Both outcomes came
from reading rather than counting.

### The binary this stage exists to re-check: **unchanged**
`fts search Iran ceasefire --days 1` → 127 matches, **every substantive item still 07-19/07-20 vintage**:
*"Mediators Float 10-Day Ceasefire As Pezeshkian Tells Citizens Iran Engaged In 'Full-Scale War'"* ·
*"Iran War Mediators Push for Traction on a New Ceasefire"* · *"War on Iran: War resumes 30 days after
MoU"*. **No acceptance, no rejection, no resolution. The TACO trigger remains live, undated, and
armed both ways in ALPHA bracket B1.** ★ Also re-verified: **SCHW's print has still NOT landed in the
pool** (25 matches, all previews/calendar rows) — **the FIN binary is genuinely pending, not
un-searched.**

### ★ Corrections this run's LATER stages made to the report above (stated, never silently patched)
The append-only rule matters more this run than usual: **the downstream stages contradicted this report
in six places, and every one of the originals stays visible above.**

1. ★★ **§1 and §4a P3′ celebrated *"VLO +1.18% on the day crude fell −0.35% — the decoupling test passed
   live."* DEEP·ENRG §0 D1/D2 showed that this conflated two different claims and that the more
   important one FAILED.** Self-computed distillate crack (`HO=F×42 − CL=F`, one continuous pull):
   **90.34 → 88.22 → 85.31** across 07-16/17/20 — **down two consecutive sessions while VLO, PBF, MPC and
   PSX rose on both.** The 07-19 file had pre-committed that exact pattern as its Day-2 falsifier, and
   **it fired.** On 07-20 **product fell MORE than crude** (`HO=F` −1.83% vs `CL=F` −0.27%). **The
   refiners did not decouple from crude; they decoupled from their own margin.** ⚠ **This is the second
   consecutive run in which P3′'s sign or framing was restated mid-run — flagged on 07-19 as "that
   instability is itself the finding", and it recurred. It is now a standing defect of this
   proposition, not a one-off.**
2. ★★ **§1 and §4 upgraded IT from UW to Neutral on MU's kill-line reclaim. ROTATION reversed it to UW,
   and three further methods backed the reversal.** SWEEP: **0 green of 56, eqflow −0.334** (worst
   breadth in the market). `module_chart MU --read`: the reclaim cleared only the **STOP**; the chart's
   own **ignition trigger (close >872.42 + OBV→누적) never fired**, OBV **분배 −57%/20d**, RSI 24.5,
   volume **0.86×**. DEEP·SEMI: **AMD's OBV is distributing at −58%/20d too** — *the Helios rally moved
   price, not money.* **Honoring the pre-committed kill-line was right; upgrading the SECTOR on one
   name was not. The distinction is the lesson.**
3. ★★ **§4 carried HLTH·RE·UTIL·STPL as four independent rows. PREMORTEM FINDING 0 measured them as ONE
   bet** (90d pairwise ≈0.57), and **DEEP·HLTH found it TIGHTER in the fresh window: 20d pairwise
   0.67–0.80, XLV–XLRE 0.801.** With **2s10s at +37bp, 7bp from the hike branch**, a single number
   (real 10Y >2.50% / 2s10s <+30bp) invalidates all four at once. **The matrix's apparent
   diversification across three Neutrals and an OW was largely illusory.**
4. ★ **§3 and §4x named `Dollar` as a resolved blind spot and RE as DEEP's problem. Both moved.**
   `Dollar` is closed (DXY 1 session stale). **RE's three-run divergence is now EXPLAINED, not merely
   escalated**: PREMORTEM LENS 1 found XLRE's OBV is driven by **WELL (매집, RS20 +19.1%) and SPG**,
   while **AMT/EQIX/DLR — the data-center REITs — are all distributing.** It is duration money, not an
   AI-power story — which is correction 3 arrived at independently, from names instead of correlations.
5. ★ **Two positioning premises the desk was relying on REVERSED SIGN inside two trading days, and
   neither would have been caught without re-measurement.** **PSX**: the registry's *human-locked*
   `core_pick` rationale reads *"the only Energy name with shorts actively exiting (z −1.43)"* —
   **measured 07-20: z +2.01 (극단)**. **HUM**: 07-19's diversifier case rested on *"shorts at z −0.60,
   the lowest in the leg"* — **measured 07-20: z +1.97**, the sector's most crowded short. ⚠ **New
   standing rule for the next run: a positioning number older than ~2 sessions may not be quoted as
   current. Both of these were 2 days old and both had flipped.**
6. ★ **PREMORTEM Lens 3 called PYPL *"the name the desk is most wrong to avoid"* (#1 flow score in the
   300-name sweep, never covered in any report). DEEP·FIN then found the cause and inverted the
   conclusion:** a reported **Stripe + Advent $53B (~$60.50/share) bid** the board called *"inadequate"*,
   with price at **56.82** and the **sell-side median target at 48.00 — 15.5% BELOW the market.**
   **It is a merger-arbitrage spread, not accumulation** — and PYPL's own 10-K carries an anti-signal
   (**TPV +7% YoY on transaction count −4% YoY**). **The lens was right that the desk had never looked;
   it was wrong about what it would find. Both halves recorded.**

### ★ Calendar defect — THREE dated catalysts inside the window that `CATALYST_WATCH.json` never held
**AMD "Advancing AI" 07-22** (found by PREMORTEM Lens 1) · **CB earnings 07-22** and **T earnings 07-22**
(found at the BET stage from `module_fundamentals_us`'s `next_earnings_date`) — plus **GOOGL 07-22 /
INTC 07-23**, carried forward manually for a **third** consecutive run. ★ **CB is the sharpest miss: it
is the dated test of the only Financials sub-leg still alive after DEEP·FIN relocated the verdict onto
insurance, and it prints tomorrow.** ⚠ **`module_fundamentals_us` already exposes `next_earnings_date`
for every ticker — the calendar could be cross-checked against the sheet's own candidates
automatically. Filed as a concrete fix, not just a complaint.**

### Other defects filed this run (so they are not re-discovered a fourth time)
- **`module_industry_map` is KR-corpus-only** and returns nothing usable for US work — found
  independently by **two** DEEP agents. It is called by L2 `deepdive` for both markets. **Either the L2
  should mark it KR-only, or the module should gain a US corpus.**
- **`brief`'s terminal view caps the body at 30 rows** (`… 외 325개`) even with `--body 2` — **87% of the
  day's events are invisible to a stdout-only read.** The full set is in
  `out/news_brief/{date}_{scope}.json`. *(New failure class 9, §5 above.)*
- **`action_bracket.py` announced *"both-sides armed below"* and emitted no brackets**; it also prints
  **fx 1482** while same-day `cycle_exposure.py` prints **fx 1380** — a 7.4% disagreement between two
  script-owned artifacts. Both filed in `ACTION_TICKETS.md`.

### What does NOT change
**The report stands.** No 🚨 regime flip; the Iran binary is unresolved in both directions; SCHW is
genuinely pending. **The tilts as ROTATION left them are unchanged by this scan** — ENRG OW (with its
epicenter hole and its now-qualified refining leg), HLTH OW-as-hedge (as one sleeve, not one sector),
FIN OW on flow only (relocated to insurance, tested tomorrow by CB), IT UW (breadth, pending 07-22/23).

**DRIFT EXIT CHECK:** ✅ drift run — via the API-routed `burst` after `drift_watch.py` proved unusable a
**third** consecutive run (**tooling defect re-filed with the same failure mode; escalated from run-log
note to repo-issue recommendation**) · ✅ **every flagged item body-read, not counted** — the day's
largest burst (SEVEN/MAGNIFICENT, z 13.3) was read and classified as **neither regime event nor noise
but corroboration**, and **category ② returned zero unknown words: the blind-word axis found nothing the
desk had missed** · ✅ the live binary re-checked directly (Iran ceasefire **unresolved**; SCHW **still
not printed**, verified rather than assumed) · ✅ **§5 ADDENDUM appended, append-only — no line above was
rewritten**, with **six downstream corrections to this report recorded next to the originals** ·
✅ **no 🚨 regime flip: the report stands.**
