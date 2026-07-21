# MACRO_REPORT — industry_US · 2026-07-19 (Sun)

> Stage 1 / L1·MACRO. Runtime `--market us`, English-pure. Primary data: `module_macro_us` [FRED],
> `us_flow --cot` positioning, `module_news_data` events (`brief --body 2`, 07-18 + 07-19) +
> `thread --days 7` trajectories + 7-bucket velocity + blindspot, tape via `module_flow` / yfinance.
> Deliverable = the **§4 transmission matrix** (ROTATION's input). Zero buy/sell calls.
> Continuity anchor: `llm_outputs/2026-07-17/industry_US/MACRO_REPORT.md` (incl. its DRIFT addendum).
> Handoff ledger mode: **`DEGAJA_REPORT_DIR=llm_outputs module_report_tags show`** — ledger now EXISTS
> (39 reports / 129 tickers / 12 sectors, updated 2026-07-17T18:35). Inherited coverage read from it.

---

## ⚠⚠ THE SINGLE MOST IMPORTANT CAVEAT FOR EVERY DOWNSTREAM STAGE
**Today is Sunday. The entire tape in this report is asof the Friday 2026-07-17 close.**
The two largest events of the window happened **after** that close:
- **07-18 [10 art / 7 outlets]** *US Says Two Service Members Killed by Iran Strikes in Jordan*
- **07-19 [6 art / 5 outlets — the day's only head event]** *U.S. strikes Iran's Revolutionary Guard after attack kills U.S. troops in Jordan*

**No price in §1 has seen US combat deaths or the IRGC retaliation strike.** Every flow tag, every
RS number, every "defense is not moving" observation below is **pre-escalation**. ROTATION and
PREMORTEM must treat Monday's open as a gap event, not a continuation.

---

## §0 Catalyst injection (run-start, `CATALYST_WATCH.json` → `llm_outputs/2026-07-19/`)
**6 binaries in window — PREMORTEM must bracket each both ways.**

| When | Event | Axis | Note |
|---|---|---|---|
| Undated / **LIVE** | **Iran "Strait of Hormuz open" (TACO trigger)** | oil | The single largest two-sided risk in the report |
| D-2 · 07-21 | **SCHW** earnings | FIN | Tests the P5 bank leg |
| D-3 · 07-22 | **TSLA** earnings | DISC | Robotaxi/Optimus expectations; SpaceX funding doubt attached |
| D-3 · 07-22 | **KMI** earnings | ENRG | ⚠ 07-17 DRIFT measured the calendar's date as a pattern-estimate that slipped to 07-23 — verify |
| D-4 · 07-23 | **RTX** earnings | INDU/defense | ★ The **dated test of P4's revival condition** |
| D-4 · 07-23 | **LMT** earnings | INDU/defense | ★ Same — into a live shooting war with US casualties |

⚠ Calendar entries are `~` pattern-estimates. The 07-17 DRIFT proved this class of error (NFLX carried
as a forward binary after it had already printed). Do not treat these dates as confirmed.

---

## §1 Regime read — primary numbers explicit

### ★ The core wedge this run: **the rate axis flipped from "on hold" to "hike on the table"**
The 07-17 report's P1 rested on a **bull-steepener** (2Y falling faster than 10Y). That engine has
reversed. The front end is now leading **up**, and the reason is on the tape in two places at once —
an oil shock and a hawkish new Fed chair.

Denominator first (P4), 3-day foreign window, terms as separate argv:
`hike` **299** · `rate hike` **236** · `Warsh` **107** · `hawkish` **93** · OR-mode union **395 matched**.
This is not a 2-outlet whisper; it is one of the largest denominators in the report. Body evidence:
- *"2-year Treasury yield keeps going higher after spiking on **hawkish start to Warsh's Fed**"* [CNBC 07-18]
- *"Fed Chair Kevin Warsh Just Drove a Dagger Through Wall Street's Heart… **interest rate hikes remain firmly on the table**"* [Yahoo Finance 07-16]
- *"'WarshGPT'… clients that Warsh's policy-relevant comments were **'overwhelmingly hawkish'**"* [CNBC 07-18]
- *"**Kalshi traders see roughly 50% odds of a rate hike in 2026**"* [CNBC 07-09]
- *"**Will the Fed hike interest rates this month?**"* [MarketWatch 07-18]
- **Counter-view, equally sourced:** *"DoubleLine Paper: Chairman Warsh Swiftly Puts His Stamp on the Fed… expects **Warsh to deliver zero hikes in 2026**"* [PRNewswire 07-17]; *"**Inflation cools** as the Federal Reserve says the fight… is far from over"* [4 outlets, 07-18].

**Read:** this is an *oscillating* regime variable of exactly the class §5 says we mis-call one-way.
It is written below (P1) with **both branches carrying equal weight**, not as a hike call.

### The primaries [FRED — asof dates explicit, freshness flagged not assumed]
| Series | Latest | vs 07-17 report | Read |
|---|---|---|---|
| Fed funds | **3.63%** (07-16) | 3.63 flat | Policy unchanged — the *repricing* is in the curve, not the target |
| US 10Y | **4.57%** (07-16) | 4.55 → **+2bp** | Long end drifting up |
| US 2Y | **4.16%** (07-16) | 4.13 → **+3bp** | ★ Front end rising **faster** than the long end |
| **2s10s** | **+41bp** | was **+42bp** | ★ **Bull-steepener → bear-FLATTENER.** P1's engine has stopped |
| Real 10Y | **2.35%** (07-16) | 2.32 → +3bp; **+42bp/120d** | Structural driver intact and still rising |
| Core CPI idx | 336.065 (**Jun**) | unchanged data | ⚠ ~1mo lag — describes a world before the oil shock |
| CPI idx | 332.568 (**Jun**) | fell m/m | Realized June disinflation is real, and **already stale** |
| Unemployment | 4.2% (**Jun**) | unchanged | Labor firm |
| DXY | 120.50 (**07-10**) | ⚠ **9 days stale** | Do not treat as current |
| VIX | 16.73 (07-16, FRED) | ⚠ stale — **live ^VIX 18.77** (07-17, **+24.9%/5d**) | Use the live print |
| M2 | $23,052B (**May**) | expanding | Liquidity tailwind, lagging |

⚠ **Freshness discipline:** CPI · Core CPI · Unemployment · M2 are monthly (**June/May**, ~1mo lag).
They pre-date this week's **+14.5% crude move** entirely. The only *current* macro facts are the
daily curve prints — and even those stop at Thursday/Friday.

### The tape [yfinance, asof 2026-07-17 close — PRE-ESCALATION]
| Ticker | Last | 5d | 1m | Read |
|---|---|---|---|---|
| **CL=F** | **81.78** | **+14.5%** | +9.3% | ★ The war premium **compounded** (was 78.69 on 07-16) |
| **BZ=F** | **88.10** | **+15.9%** | +13.1% | Brent confirms — not a WTI-basis artifact |
| **VLO** | **309.65** | **+10.3%** | **+31.0%** | ★★ RS20 **+28.8%**, accumulating — the run's strongest single lane |
| **MPC** | 312.60 | +10.2% | +28.7% | RS20 +27.5%, accumulating |
| **PSX** | 206.86 | +9.8% | +24.5% | RS20 +23.4%, accumulating |
| XOP | 170.18 | +7.3% | +11.0% | RS20 +9.0%, accumulating |
| XLE | 57.68 | +4.7% | +7.3% | RS20 +5.2%, accumulating |
| **MU** | **848.95** | **−13.3%** | **−25.1%** | ★ **Broke the 853.20 kill-line to the DOWNSIDE.** RS20 −18.9% |
| **SMH** | 556.53 | **−8.9%** | **−15.7%** | RS20 **−11.1%** (was −7.7%) — distributing |
| **TSM** | 398.37 | −8.2% | −13.8% | 🔴 distributing on **1.28× volume** — the board's only real surge |
| QQQ | 695.33 | −4.2% | −6.1% | Distributing |
| NVDA | 202.81 | −3.9% | −3.7% | Neutral; no longer "holding up better" |
| **SPY** | **743.29** | **−1.54%** | −0.46% | ★ was −0.56%/5d last run — **the index is now moving too** |
| **^VIX** | **18.77** | **+24.9%** | +1.8% | Rising into a weekend war escalation |
| XLF | 56.26 | +1.0% | +5.0% | RS20 +3.8%, **accumulating** — thesis engine broke, flow did not |
| XLV | 161.09 | +0.2% | **+7.8%** | RS20 **+6.6%**, accumulating — the rotation destination |
| XLRE | — | — | — | RS20 **+3.0%, accumulating** ← ★ contradicts the real-yield UW (§4 divergence) |
| XLB | 50.53 | −0.7% | −2.5% | RS60 −8.0%, distributing |
| **LMT** | **508.77** | **−2.8%** | −0.4% | RS60 −16.6%, distributing, **vol 0.68×** — into a shooting war |
| **NOC** | 521.57 | −3.4% | +0.0% | RS60 **−20.2%**, distributing |
| GD / RTX | 368.58 / 193.51 | −1.7% / −1.2% | +5.3% / +4.3% | Neutral flow — the bifurcation from 07-15 still holds |
| GEV | 1057.84 | −3.1% | −4.7% | ★ **flipped to accumulating** (RS20 +0.5%) after last run's −5.1% |

**The rotation call is intact but the "not a crash" qualifier is weakening.** Last run: semis −7%
against SPY −0.6%. This run: semis −8.9% against SPY **−1.54%**, VIX +24.9%. Money is still rotating
(ENRG/FIN/HLTH accumulating while IT distributes), but the index is no longer absorbing it cleanly.

---

## §2 Positioning — CFTC COT [`us_flow --cot`; Tue-close, 3–4d lag → **context, not a trigger**]
| Instrument | Net spec | Wk Δ | 1Y %ile | Tag |
|---|---|---|---|---|
| **Nasdaq-100** | −10,313 | −1,572▼ | **4%ile** | 🔴 crowded-SHORT (still loaded, still unlit) |
| **Nat Gas** | −178,612 | −13,305▼ | **6%ile** | 🔴 crowded-short |
| **WTI Crude** | +19,783 | −1,139▼ | **10%ile** | 🔴 crowded-SHORT — ★ *shorts were still adding into a +14.5% week* |
| **Copper** | +64,385 | +113▲ | **95%ile** | 🟢 crowded-LONG (overheated) — unchanged |
| S&P 500 | −38,938 | +3,953▲ | 78%ile | 🟡 |
| Russell 2000 | +103 | +990▲ | 67%ile | 🟡 |
| USD Index | +13,173 | −96▼ | 58%ile | 🟡 |
| UST 10Y / 2Y | −831,675 / −1,157,477 | −17,413▼ / +103,531▲ | 22% / 52%ile | 🟡 — ★ 2Y shorts **covered hard** (+103k), consistent with the front-end repricing |
| Gold / Silver | +186,682 / +25,074 | −7,564▼ / −2,941▼ | 23% / 40%ile | 🟡 |

### Obeying §5 failure class 2 (the rule this desk paid for)
**Positioning may only AMPLIFY a proposition that already has its own catalyst; it may never BE the
proposition.** Applied here:
- **WTI 10%ile + a live catalyst (US strikes IRGC)** → legitimately amplifies P3. ✅
- **Nasdaq 4%ile with no igniter** → **does NOT** promote IT. The 07-15 desk made exactly that error
  and paid −6.9%. It stays UW. ✅

---

## §3 Narrative — events, trajectories, velocity, blindspot

### Event axis — full denominator, `--body 2`, tail = 0 [`brief --scope foreign`]
| Day | Articles → clusters → events | head / body / tail | nonmarket |
|---|---|---|---|
| **07-19** | **328 → 196 → 46** | 1 / 45 / **0** | 0 |
| **07-18** | **589 → 307 → 82** | 1 / 81 / **0** | 0 |

**All 128 event lines across both days were read** (tail = 0 both days — nothing sampled away).
`nb` is null throughout: market/non-market filtering is domestic-only, foreign scope filters nothing,
so **nothing was silently excluded**. The regime-relevant lines, with outlet counts:

**War / oil (the day's head both days):**
- [6a/**5s**] *U.S. strikes Iran's Revolutionary Guard after attack kills U.S. troops in Jordan* — 07-19 head
- [10a/**7s**] *US Says Two Service Members Killed by Iran Strikes in Jordan* — 07-18 head
- [2a/2s] *U.S. refiner margins spiked to **record highs** this week as fuel shortage concerns grow*
- [6a/2s] *Global Oil Supply Is Being **Squeezed From Two Directions at Once***
- [2a/2s] *Caspian Pipeline Consortium oil loadings **suspended** after drone attacks on tankers* [Reuters]
- [2a/2s] *Oil's Battered Shock Absorbers Risk **Price Spike** as War Returns*
- [2a/2s] *UK's Burnham faces test as **Trump seeks British bases for Iran attack***
- [2a/2s] *Iran, U.S. trade heavy fire; Israel continues to bomb Lebanon*

**Rates / Fed:**
- [2a/2s] *Warsh Shows His **Inner Hawk** as Inflation Debate Heats Up* [Bloomberg]
- [3a/3s] *'WarshGPT': How Wall Street is adapting to the Fed's new era of communication*
- [2a/2s] *Will the Fed hike interest rates this month?* · [3a/2s] same thread
- [4a/**4s**] *Consumer: **Inflation cools** as the Federal Reserve says the fight… is far from over*
- [2a/2s] *Fed Chair Kevin Warsh Just Hammered Home the 2 Words… **Worrisome for Wall Street***

**AI / semis (the P2 axis):**
- [2a/2s] ***TSMC: The AI Supercycle Just Got Stronger*** ← the live counter-thesis, named
- [2a/2s] *IBM: **Structurally Ill-Suited** To Capture AI Demand* (6-day thread, see below)
- [6a/3s] *Amid **Growing Data Center Backlash**, Nvidia Could Have the Answer*
- [3a/2s] *How a **homegrown Chinese chip maker** became the memory industry's big wild card* ← the CXMT/MU leg
- [2a/2s] *AMD Stock Faces Fresh AI Pressure After **China Unveils Kimi K3***
- [4a/2s] *Multiple Compression Is a Real Threat to Microsoft Stock*
- [3a/2s] *Korea's AI-Heavy Market Now Sets the Tone for Global Stocks*

**Financials / other:**
- [2a/2s] *The Bull Case For JPMorgan Chase Could Change Following **Record-Breaking Q2 2026 Profit And Guidance***
- [2a/2s] ***Financial stocks overbought*** amid tech selloff; BofA, PayPal among gainers
- [2a/2s] *Vanishing CLO Profits Are Sparking Infighting: Credit Weekly* ← credit-cost watch for P5's anti
- [2a/2s] *France and Germany reach **nuclear deal as Europe builds up defences***
- [2a/2s] *Tesla Just Posted Its Best Q2 Deliveries Ever. Here's the 1 Number That Will Move the Stock on **July 22***
- [5a/2s] *SpaceX Stock Just Quietly Fell to **$124 a Share** — and It's Still Not a Buy*

⚠ **Once again the entire regime story lives at 2 outlets** — refiner record margins, the CPC pipeline
suspension, the Warsh hawk turn, the JPM record print. At the default `--body 3` this report would
have seen **two headlines and nothing else.** Third consecutive run confirming the `--body 2` rule.

### Trajectory axis [`thread --days 7 --scope foreign --top 25`]
Per-day denominators first, because they change the reading:
`07-13 218 · 07-14 210 · 07-15 199 · 07-16 223 · 07-17 265 · **07-18 82 · 07-19 46**`
1,243 daily events → 995 threads (128 multi-day, 16 alive).

⚠ **The weekend collapse (265 → 82 → 46) mechanically inflates FADING.** The unit warns about exactly
this, and it is the difference between a correct and an inverted read this run:

| Thread | Curve (outlets) | Tag | Corrected read |
|---|---|---|---|
| **US–Iran war** | 4→3→5→3→6→**4→4** *(49 art)* | "FADING" | ★ **NOT fading.** On 07-18 it took **7 of 82** events and on 07-19 **5 of 46** — its *share* rose while the pool shrank 5×. And the price says +14.5%. **§5 failure-class-4 rule applied: for supply-shock assets, price is primary, theme-age is corroborant.** |
| Russia–Ukraine strikes | 2→3→4→4→2→**4** *(23 art)* | **BUILDING** | Real. Afipsky refinery fire → Kyiv ballistic attack → *"Ukraine hits oil facility"*. **This is the second oil-supply direction** ("squeezed from two directions"). |
| IBM software warning | 5→4→3→3→2→**2** *(43 art)* | FADING | The *coverage* faded; the **thesis did not** — 07-19's line is *"IBM: Structurally Ill-Suited To Capture AI Demand"*. Software-AI de-rate is live. |
| SpaceX below IPO | 5→3→7→4→6→2→**2** *(100 art)* | FADING | 100 articles in a week is the window's biggest thread. Now $124 vs IPO. **DISC/TSLA input.** |
| AI buildout / bubble | 4→3→5→3→6→4→**4** *(99 art)* | FADING | Same weekend artifact; the *substance* rotated from "bubble?" to "data-center **backlash**". |
| TSMC | 3→2→**2** | FADING | ★ But its 07-19 line is *"The AI Supercycle Just Got **Stronger**"* — the P2 counter-thesis is alive at 2 outlets. |
| **ENDED** — *"Oil prices jump as fighting flares in Middle East"* | 8→9→8→5→6→2, **peak 9 outlets** | **ENDED** | ★★ **The attention-rotation ledger's sharpest signal this run: the market STOPPED writing about the oil war on 07-18 — and the oil war then killed two US soldiers and drew an IRGC strike.** Editors rotated away exactly one day before the escalation. |
| **ENDED** — *"Consumer prices rose 3.5% annually in June, less than…"* | 3→6, peak 6 | ENDED | The cool-CPI story is **over** as a narrative — superseded by the hike debate. |
| **ENDED** — *"Trump's Strait of Hormuz Fee Could Double the Cost…"* | 8→8→3, peak 8 | ENDED | — |

**Every proposition in §4a names its thread's tag + curve, or states "no thread".**
**Inherited-proposition staleness flags:** P4-defense rides a thread that peaked at **9 outlets and
ENDED** — but the *price* leg (crude) is at highs. P5-banks has **no live thread** (bank earnings
threads all ENDED); it now rests on a single 2-outlet JPM line + the tape.

### Velocity — 7-bucket sweep [fts, foreign, 7d, OR-mode + `--syn`, **terms as separate argv**]
| Rank | Bucket (argv recorded verbatim) | 7d count | vs 07-17 |
|---|---|---|---|
| **1** | `tariff trade China truce` | **3,860** | was 2,921 (#2) → **new #1** |
| 2 | `AI datacenter power capex` | 3,758 | was 2,312 |
| 3 | `banks financials JPMorgan lending` | 3,266 | was 3,643 (#1) → **lost the top slot** |
| 4 | `rates Fed inflation Warsh` | 2,834 | was 2,246 |
| 5 | `oil energy Hormuz refinery` | 2,364 | was 1,840 |
| 6 | `defense missile military Iran` | 1,645 | was 771 |
| 7 | `semiconductor chips memory HBM` | 1,429 | was 1,165 |

⚠ **Comparability caveat, stated honestly: the argv are NOT identical to 07-17's.** Cross-run deltas
are **directional only**. Two specific traps in my own numbers:
- The **defense bucket contains `Iran`**, a war term, not a defense-*industry* term. Its 2.1× jump is
  **contaminated** and must not be read as defense-sector interest. The clean industry denominators
  are: `Lockheed` **19**/7d · `Northrop` **10**/7d · `munitions` **24** · `defense budget` **33**.
  **The defense industry is still nearly silent while its war rages.** (→ P4)
- **Every bucket is non-zero** — no silent-zero from a mis-passed multi-word argv. *(Fix-forward
  from 07-17 applied: argv recorded verbatim above so the next run can diff exactly.)*

### Blindspot pass [22,067-article/14d window, 7,723 random sample, token-0 emergent terms]
Sample rows read **raw** (no pre-named bucketing). Emergent-term ranks:
`AI 2075 · China 761 · Earnings 741 · **Iran 671** · **Fed 649** · Trump 627 · **Dollar 467** ·
SpaceX 422 · **Oil 417** · Nvidia 378 · Apple 378 · Meta 337 · Bank 307 · **Energy 302** · Inflation 295`
- **`Iran` jumped to #4** (was 552 and 4th on 07-17 → **671**) — consistent with, and now ahead of, the price.
- **`Fed` at #5 (649) and `Inflation` (295)** — corroborates the §1 hike wedge with a large denominator.
- **`Dollar` #7 (467)** is a **new entrant to the top-10** and there is **no DXY reading fresher than
  07-10** to price it against. ⚠ **Named blind spot, not resolved:** a 9-day-stale dollar under a
  hawkish-Fed + oil-shock regime is a material hole. Flagged for ROTATION/DEEP, not papered over.
- Raw sample rows worth the read: *"Australian Dollar strengthens… as **soft US CPI tempers Fed
  tightening bets**"* (fxstreet 07-15 — the dovish counter-branch, in the blind pool);
  *"South Korea's Hanwha, TKMS near **Canada sub decision**"* (upi — the 07-07 event's sequel);
  *"EU to Prioritize **European Providers** in Public Service Contracts"* (Bloomberg — with the
  France–Germany nuclear/defence deal, a **European** defense-spend lane that does **not** run through LMT/NOC).
- **Living term-table additions:** `rate hike` · `hawkish` · `WarshGPT` · `refining margin` ·
  `crack spread` · `data center backlash` · `Kimi K3` · `CPC pipeline` · `European defence buildup`.

---

## §4 ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)
> Wind direction only, one line per GICS sector. Not equal-weight analysis. Proposition IDs in §4a.
> **All flow tags asof the Friday 07-17 close — pre-escalation.**

| # | GICS Sector | Tilt | Δ vs 07-17 | Prop | One-line why |
|---|---|---|---|---|---|
| 1 | **Energy (ENRG)** | **OW ★strongest** | ↑ (was OW, now the #1 lane) | P3, P3′ | **CL=F +14.5%/5d, Brent 88.10**; **refiners VLO/MPC/PSX RS20 +28.8/+27.5/+23.4%**, all accumulating, on **record refining margins**; supply squeezed from **two** directions (Iran + Russia/CPC). WTI still **10%ile** = fuel remains. **⚠ TACO-reversible in one session** |
| 2 | **Health Care (HLTH)** | **OW** | **↑↑ from Neutral** | P7 | **XLV RS20 +6.6%, +7.8%/1m, OBV accumulating** — the only *defensive* sector with real accumulation. Carried from 07-17 DRIFT's ISRG burst (vol 1.45×, OBV accumulating). The rotation destination the tape actually names |
| 3 | **Financials (FIN)** | **OW (weakened)** | ↓ conviction, same tilt | P1, P5 | **XLF RS20 +3.8%, accumulating**; **JPM record Q2 profit + guidance**. ⚠ But **the engine reversed**: 2s10s +42→**+41bp**, bear-flattening — and *"Financial stocks **overbought**"* [2 outlets]. **Flow is intact; the thesis that justified it is not.** ← §4 divergence (c) |
| 4 | **Information Tech (IT)** | **UW** | = UW, **deepened** | P2′ | **MU broke 853.20 → 848.95** (kill-line resolved *against* the bull branch). SMH RS20 −11.1%, TSM distributing on **1.28× vol**, XLK RS20 −5.8%. IBM software warning + Kimi K3 + CXMT. The **4%ile Nasdaq short still did not fire** |
| 5 | **Comm Services (COMM)** | **UW** | = | P2′ | Capex-as-cost persists; *"Multiple Compression… Microsoft"*, *"data center backlash"*. No accumulation anywhere |
| 6 | **Industrials (INDU)** | **Neutral** | = | P2′, P4 | **XLI accumulating but RS20 −0.4%** — no wind. Split verdict: AI-power **GEV flipped to accumulating** (+0.5% RS20, vs −5.1% last run) while **defense primes broke further** (NOC RS60 −20.2%). Two legs, opposite directions |
| 7 | **Consumer Disc (DISC)** | **Neutral→UW** | ↓ from Neutral | P1, P3 | **XLY RS20 −0.4%, RS60 −8.5%**, no accumulation. **Crude +14.5% is a gasoline tax on the consumer**; TSLA 07-22 binary; SpaceX at $124 (100-article thread) |
| 8 | **Consumer Staples (STPL)** | **Neutral** | = | P1 | RS20 +1.5% but **OBV neutral — no accumulation**. Defensive money went to HLTH, not here. SPY −1.54% is not yet risk-off enough to bid staples |
| 9 | **Utilities (UTIL)** | **Neutral (weak)** | ↓ lean | P1, P2′ | **RS60 −5.1%, OBV neutral**. Squeezed both ways: rising **real 10Y 2.35%** hurts the bond proxy, and the AI-power demand story is the thing being repriced |
| 10 | **Materials (MATR)** | **UW** | = UW | P1, P6 | **XLB distributing, RS60 −8.0%**; **copper still 95%ile crowded-long** = overheated; China-truce risk is now the **#1 velocity bucket** (3,860) |
| 11 | **Real Estate (RE)** | **UW** | = UW | P1 | **Real 10Y 2.35%, +42bp/120d** and a live hike debate set this sector's cost. ⚠ **BUT XLRE RS20 +3.0% and OBV accumulating** — thesis and flow disagree ← §4 divergence (a) |

**Net wind:** out of the AI complex (IT/COMM) — **into ENRG (refining specifically) and HLTH**, with
FIN held on flow rather than on thesis. The rotation is still intra-equity, but **SPY −1.54% + VIX
+24.9%** means the "this is not a de-risking" qualifier is now weaker than last run's −0.56%.

### §4x ★ Divergences ROTATION must resolve (matrix × flow, named explicitly per the L1 rule)
- **(a) RE — matrix UW, flow accumulating.** Real yields say UW; XLRE OBV says money is arriving.
  **Owner: DEEP.** Early-vs-trap question: is this a rate-cut bet being placed *against* the hike
  debate, or defensive duration-seeking? A hike would settle it violently.
- **(b) FIN — thesis broken, flow intact.** The steepener that justified the OW has flattened, yet
  XLF accumulates and JPM printed a record. **Owner: DEEP.** Is XLF late money, or does a hike
  regime (NIM up) simply replace the steepener as the driver? **SCHW 07-21 is the dated test.**
- **(c) INDU — one sector, two opposite legs.** GEV accumulating vs NOC RS60 −20.2%. A single
  INDU tilt is not meaningful; **ROTATION should treat AI-power and defense as separate lanes.**
- **(d) Defense — a perfect catalyst and zero flow, for the 4th run.** US combat deaths, US strikes
  on the IRGC, Europe rearming, France–Germany nuclear deal — and `Lockheed` runs **19 hits/7d**
  with LMT vol **0.68×**. ⚠ **But the tape is pre-escalation.** This is now a **dated, falsifiable
  test: RTX and LMT both print 07-23.**
- **(e) HLTH — promoted on flow alone, with no macro proposition behind it.** Honest: P7 is a
  *flow-led* promotion (rule (b): money moved before the thesis). **Breadth caveat carried from
  07-17 DRIFT: ISRG RS20 −3.6%/RS60 −19.5% — "broad accumulation, uneven performance."**

---

### §4a Falsifiable propositions (both branches mandatory on oscillating variables)

- **P1 — ★ NEW/REPLACES the bull-steepener: the rate axis is now two-sided and the market is
  debating a HIKE.**
  *Evidence: 2Y 4.13→**4.16** rising faster than 10Y 4.55→4.57; **2s10s +42→+41bp (bear-flattening)**;
  real 10Y **2.35%**; `hike` **299 hits/3d**, `rate hike` **236**, union **395 matched**; CNBC 07-18
  "2-year yield keeps going higher after **hawkish start to Warsh's Fed**"; Kalshi **~50% odds of a
  2026 hike**; COT shows **2Y shorts covering +103,531** in a week.*
  **Thread:** the cool-CPI thread **ENDED** (3→6, peak 6); the hike/Warsh story has **no single
  thread** — it is distributed across the pool, which is why the *denominator*, not a curve, carries it.
  **Anti-signal (equal weight, mandatory):** DoubleLine's published call of **zero hikes in 2026**
  [PRNewswire 07-17]; *"soft US CPI tempers Fed tightening bets"* [fxstreet, found in the **blind
  pool**]; June CPI **fell m/m**. If crude round-trips on a ceasefire, the inflation impulse vanishes
  and the front end re-rallies → the **bull-steepener resumes and P1 flips back to the 07-17 version**.
  **Track KPI:** 2s10s (**+41bp** — a move back above +45bp = dovish branch; below +30bp = hike
  branch), real 10Y (**2.35%**; **>2.50% = the FIN duration-loss trigger**), 2Y (**4.16%**).
  **Catalyst:** next CPI/FOMC dates **[blank]** — not in CATALYST_WATCH; **do not guess them**.
  ⚠ This is precisely §5's failure class 1 (one-sided reads of oscillating variables). **Neither
  branch is favored in the matrix**: no sector tilt above rests on a hike *happening*.

- **P2′ — AI capex sign-flip / capital-intensity de-rate (CONTINUED — its kill-line resolved).**
  *07-17 named the falsifying price: "MU holds above **853.20** → this was TSMC-specific." **MU closed
  848.95 — the line broke to the downside.** The de-rate is therefore **not falsified** and deepened:
  SMH RS20 −7.7%→**−11.1%**, TSM distributing on **1.28× volume**, XLK RS20 −5.8%. New corroborants:
  IBM's software warning thread (43 art/6d), "data center **backlash**", AMD vs **Kimi K3**, and the
  CXMT memory wild-card [3a/2s].*
  **Anti-signal (mandatory, and it is live at 2 outlets):** *"**TSMC: The AI Supercycle Just Got
  Stronger**"* [07-19]; *"Amid Growing Data Center Backlash, **Nvidia Could Have the Answer**"*
  [6a/3s]. If **NVDA/GOOGL/INTC print and raised capex is rewarded** (stock up *on* the capex line),
  or **MU reclaims 853.20** and SMH RS20 turns positive, the de-rate was a TSMC-specific event and the
  **Nasdaq 4%ile short becomes squeeze fuel after all** (still loaded, still unlit).
  **Track KPI:** **MU 848.95** (new line, replacing 853.20), SMH RS20 (−11.1%), NVDA's reaction to
  the next capex headline. **Catalyst:** GOOGL/TSLA/INTC print the week of 07-20 [2a/2s *"Google,
  Tesla, Intel To Headline Earnings Next Week"*] — exact dates **[blank]**.

- **P3 — Oil war-premium (CONTINUED — escalating, NOT fading).**
  *CL=F 78.69 → **81.78 (+14.5%/5d)**, Brent **88.10 (+15.9%)**, XLE +4.7%, XOP RS20 +9.0%. WTI still
  **10%ile crowded-short** with specs **still adding shorts** into the rally. The catalyst is now
  kinetic: **US service members killed (07-18, 7 outlets) → US strikes the IRGC (07-19, 5 outlets)**.*
  **Thread:** the US–Iran thread is tagged FADING **only because the weekend pool collapsed 265→46**;
  its outlet *share* rose. Meanwhile *"Oil prices jump as fighting flares"* (peak **9 outlets**)
  **ENDED** — ★ **the market rotated attention away one day before the escalation.**
  **Anti-signal (equal weight — this is the report's largest two-sided risk):** the **TACO trigger** —
  Iran declares the strait open / a ceasefire lands (undated, live in CATALYST_WATCH) → crude gaps
  down, the 10%ile short covers into relief, **ENRG round-trips in a single session** and P1's
  inflation impulse dies with it. A one-way tilt here is the exact violation PREMORTEM exists to prevent.
  **Track:** CL=F **81.78**, BZ=F 88.10, Hormuz transit rate, `Iran` emergent rank (**#4, 671**).

- **P3′ — ★ NEW: the durable ENRG leg is REFINING, not the crude premium.**
  *This promotes 07-17's DRIFT correction into a first-class proposition. **VLO RS20 +28.8% / MPC
  +27.5% / PSX +23.4%, all OBV-accumulating**, +25–31% on the month — a far bigger move than XLE
  (+5.2%) or crude itself. The mechanism is on the tape: **"U.S. refiner margins spiked to record
  highs this week as fuel shortage concerns grow"** [2a/2s] + Russian refinery destruction
  (Afipsky, BUILDING thread) + the **CPC pipeline suspension after drone attacks** [Reuters 2a/2s]
  + Ukraine hitting oil facilities. **Refining capacity is being physically destroyed** — which is
  mechanically **independent of the Strait of Hormuz**.*
  **Why this matters:** it means a TACO event **does not kill the whole ENRG OW.** Crude round-trips;
  destroyed refineries do not come back in a session. **This is the anti-fragile half of the OW.**
  **Anti-signal (specific, not generic):** **Russian refining capacity coming back online** (Afipsky/
  Syzran repairs), a lifted diesel export ban, or crack spreads normalizing. **Not** a Hormuz headline.
  **Track:** `refining margin` **30 hits/7d**, `crack spread` **14**, `refiner` **184**, VLO RS20.
  ⚠ **Low news denominator (30/14) on the run's strongest price move** — this is the *inverse* of the
  failure-class-4 trap and the same rule applies: **price is primary, velocity is corroborant.**

- **P4 — Defense primes (STAYS RETIRED — 4th consecutive failure — with a DATED revival test).**
  *Given the most ideal catalyst imaginable — **US combat deaths, a US strike on the IRGC, Europe
  rearming, a France–Germany nuclear deal, Germany raising its terror threat level** — the primes
  did this: **LMT −2.8%/5d, RS60 −16.6%, vol 0.68×, distributing; NOC −3.4%, RS60 −20.2%,
  distributing.** Industry denominators: `Lockheed` **19 hits/7d**, `Northrop` **10**. The
  war-premium transmits to **crude and refining**, not to the primes. Confirmed a fourth time.*
  ⚠ **The honest caveat that keeps this falsifiable: the tape is asof Friday's close and the two
  biggest escalations happened on Saturday and Sunday.** This is *not* a resolved question — it is a
  **live forward test**, and unlike the last three runs it has a **date**.
  **Revival condition (unchanged, falsifiable):** LMT/NOC/GD volume surge **>1.3×** on an
  appropriations or NATO order. **Dated test: RTX 07-23 and LMT 07-23 both print.**
  **Un-tunneling note:** the blindspot pass surfaced a lane the primes don't own — *"EU to Prioritize
  **European Providers** in Public Service Contracts"* [Bloomberg] + the France–Germany nuclear deal.
  **European defense spend may not transmit through US primes at all.** Logged as a term, not a tilt.

- **P5 — Bank earnings leg (CONTINUED — but now standing on less).**
  *JPMorgan **record Q2 2026 profit and guidance** [2a/2s]; XLF OBV accumulating, RS20 +3.8%.*
  ⚠ **Staleness flag (per the trajectory rule): every bank-earnings thread has ENDED.** The bucket
  also **lost the #1 velocity slot** (3,643 #1 → 3,266 #3). And P1's steepener — the *macro* reason
  for the OW — has reversed. So FIN's OW now rests on **earnings + flow**, not on the curve.
  **Anti:** **SCHW misses 07-21 (binary)**, credit-cost surprise — *"**Vanishing CLO Profits** Are
  Sparking Infighting"* [Credit Weekly, 2a/2s] is the named mechanism — or *"financial stocks
  **overbought**"* resolving into distribution. **Track:** SCHW 07-21, XLF OBV, CLO/credit commentary.

- **P6 — China truce risk (PROMOTED from watch → the denominator now supports it, but only as a
  watch-with-teeth, not a driver).**
  *07-17 logged this at **2 outlets** and correctly refused to build a tilt on it. This run the
  `tariff trade China truce` bucket is the **#1 velocity bucket at 3,860 hits/7d**, `China` is the
  **#2 emergent term (761)**, and the tape carries *"Hungary Crackdown on $20 Billion EV Sector Puts
  China on Notice"*, *"China's Siemens Competitor Eyes Buying Its Way Into Europe"*, *"SA Asks: Who
  will be most impacted by the **nonrenewal of the USMCA trade deal**?"*.*
  ⚠ **What is still missing: a retaliation event.** Velocity is not an event (§3's two-axis rule).
  **No sector tilt rests on this** — it informs the existing MATR/IT UW, it does not create one.
  **Promotion-to-driver condition:** an actual Chinese retaliation headline or a formal tariff
  re-escalation. **Track:** the bucket count (3,860), `China` emergent rank.

- **P7 — ★ NEW: Health Care as the rotation destination (FLOW-LED, thesis pending).**
  *Rule (b) promotion — money moved before the thesis. **XLV RS20 +6.6%, +7.8%/1m, OBV accumulating**,
  the only defensive sector with accumulation while SPY −1.5% and VIX +24.9%. Corroborated by 07-17
  DRIFT's ISRG burst (z 12.4, vol 1.45×, OBV accumulating, delta +0.27) and today's [7a/3s] *"IHE vs.
  BBH: Which Healthcare ETF Is the Better Buy"* + *"The Most Overlooked Reason **Eli Lilly** Stock
  Keeps Surging"*.*
  ⚠ **Stated honestly: this has no macro proposition behind it.** It is a flow observation with a
  plausible story (defensive rotation out of a de-rating AI complex), and **DEEP owes it a thesis or
  a rejection.** Breadth caveat: ISRG RS20 −3.6%/RS60 −19.5% → **"broad accumulation, uneven
  performance"**, not broad strength.
  **Anti-signal:** XLV OBV flips to distributing, **or** SPY rebounds and XLV's relative gain
  evaporates (i.e. it was only ever a hedge, not a destination). **Track:** XLV RS20 (+6.6%), OBV.

---

## §5 Self-backtest — scoring the 07-17 propositions at +2d (07-17 close, pre-escalation)

| 07-17 proposition | Realized by 07-17 close | Score |
|---|---|---|
| **P2′** AI capex sign-flip → UW IT/COMM; kill-line **MU 853.20** | **MU 848.95 — line broke DOWN.** SMH RS20 −7.7%→−11.1%, TSM distributing 1.28× | **HIT** |
| **P3** oil war-premium × WTI crowded-short | **CL=F 78.69 → 81.78 (+14.5%/5d)**, Brent +15.9% | **HIT** |
| **P4** defense retired (war transmits to crude, not primes) | US combat deaths + IRGC strike; **LMT −2.8% vol 0.68×, NOC RS60 −20.2%** | **HIT** (the *retirement* was the correct call) |
| **P5** bank earnings leg | **JPM record Q2 profit + guidance**; XLF accumulating | **HIT** |
| **DRIFT correction:** "the durable ENRG leg is **refining**, not the oil premium" | **VLO RS20 +28.8%, MPC +27.5%, PSX +23.4%** on **record margins** — 5× XLE's move | **HIT ★** (the correction outperformed the original thesis) |
| **P1** bull-steepener → FIN OW, RE/MATR UW | Tilts right (XLF +3.8%, XLB RS60 −8.0%) — but the **engine reversed**: 2s10s +42→+41bp, bear-flattening; and **XLRE is accumulating** against the RE UW | **HALF** |
| **P6** China truce (kept as watch, not a driver) | Became the **#1 velocity bucket (3,860)** with **still no retaliation event** | **OPEN** (the refusal to promote it was correct) |

**This run: 5 HIT / 1 HALF / 1 OPEN (n=7).**
**Running hit-rate across the two scored runs: 8 HIT / 1 HALF / 4 MISS / 1 OPEN (n=14) ≈ 57%.**
Prior run was 3/7 (43%). **What changed: the three new failure-class rules were applied and all three
paid.** Specifically —
- *Failure class 2* (positioning ≠ trigger) → Nasdaq 4%ile was **not** promoted → IT UW → correct.
- *Failure class 3* (name the real kill-switch) → P2′'s kill-line was a **price (853.20)**, not a
  headline. It broke, and the answer was unambiguous.
- *Failure class 4* (price primary for supply-shock assets) → the US–Iran thread reads "FADING" and
  the ENDED oil thread peaked at 9 outlets; **the rule said trust the price, and the price was +14.5%.**

### Recurring failure classes — carried and updated
1. **(carried, WORKING)** One-sided reads of oscillating variables. → P1 and P3 both carry equal-weight
   branches this run. **Keep.**
2. **(carried, WORKING)** Extreme positioning may only AMPLIFY a proposition with its own catalyst.
   → WTI 10%ile amplified P3 (catalyst: IRGC strike); Nasdaq 4%ile amplified nothing. **Keep.**
3. **(carried, WORKING)** An anti-signal must be the **mechanism** most likely to kill the thesis.
   → P3′'s anti is *Russian refining capacity returning*, explicitly **not** a Hormuz headline. **Keep.**
4. **(carried, WORKING — and now generalized)** For supply-shock assets, **price is primary and
   theme-age/thread-tag is corroborant, never the reverse.** ★ **New corollary measured this run:
   a weekend/holiday window-end collapses the pool (265 → 82 → 46 events) and mechanically prints
   FADING on threads whose outlet *share* is actually rising. Read the per-day denominator before
   any tag.** The US–Iran thread would have been misread as decaying on the exact weekend it escalated.
5. **★ NEW — an ENDED thread is not a dead risk; it can be a blind spot forming.** *"Oil prices jump
   as fighting flares"* peaked at **9 outlets and ENDED on 07-18** — the day US soldiers were killed.
   **New rule: when a thread ENDS while its underlying physical driver is still active, treat the
   attention gap as an opportunity/risk flag, not as resolution.**
6. **★ NEW — a bucket contaminated by a cross-domain term is worse than no bucket.** My own
   `defense missile military Iran` bucket doubled (771→1,645) purely because `Iran` is a war term.
   Uncontaminated industry counts (`Lockheed` 19, `Northrop` 10) say the opposite. **New rule: for
   an industry bucket, at least one term must be industry-exclusive, and the count must be
   cross-checked against a company-name denominator before it may move a tilt.**

### §5 DRIFT stamp (append-only — populated by stage 9)

## §5 ADDENDUM — DRIFT (2026-07-19 post-run) · append-only
> **Append-only by rule: not one line above this was edited.** The original call stays visible next
> to its correction — that asymmetry is what feeds the next run's self-backtest.

### ⚠ Tooling note (P6): `drift_watch.py` is STILL unusable on this client — and it now fails a NEW way
The 07-17 DRIFT filed this defect: `scripts/drift_watch.py` opens the server-owned DB directly
(`FTS_DB = data/news_fts.db`) with no `DEGAJA_NEWS_API` branch. **Since then a `DEGAJA_NEWS_API`
route was clearly added, but `drift` was never added to the read-command allowlist**, so it now dies
one layer later:
```
drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용).
허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']
```
**The DRIFT stage's own tool remains unusable on the machine the stage runs on — two runs in a row,
now for a different reason.** Filed again. Worked around exactly as 07-17 did, via the API-routed
equivalent (`burst` **is** in `DB_READ_CMDS`):
`python -X utf8 -m module_news_data burst --date 2026-07-19 --scope foreign --top 25`

### Burst scan — **no 🚨 regime flip. The report stands.**
Denominator: the 07-19 foreign pool (**328 articles → 196 clusters → 46 events**).
**Category ② ("words that never appear normally") returned only BUNCH / LIKES / PASSED / CRASHED** —
3 articles each, 2–3 outlets. `CRASHED` was checked and rejected on the same 2-outlet bar this desk
applies everywhere else. **No unknown-word emergence.**

| Burst | z | n / outlets | distributing | Body-read verdict |
|---|---|---|---|---|
| **WARREN / BERKSHIRE / BUFFETT** | **7.2 / 6.8 / 5.6** — the run's largest | 15 / 5 | 0.87–0.95 | **NOT a regime event — rejected on body-read.** *"Warren Buffett Set a New Goal: Give Away All of His $140 Billion Berkshire Stake by 2034"* — **the identical article syndicated across nasdaq · yahoo_finance · fool.** The distributing score is high because syndication looks like independent editors. Philanthropy, not markets. **No action.** ★ *Method note: the biggest z of the day was noise — outlet-count ranked it correctly as widely-carried and completely mis-ranked it as important. Exactly the failure the `brief` unit warns about, caught here by reading rather than counting.* |
| ★ **SEMICONDUCTOR / ASML** | **6.8 / 2.9** | 13 / 5 · 7 / 4 (**100% market-relevant**) | 0.88 / 0.92 | ★ **REGIME-RELEVANT — and it lands precisely on P2′'s weakest seam.** Body evidence: ***"Earnings From Taiwan Semiconductor and ASML Show SOARING DEMAND, So Why Are AI Stocks Falling?"*** [Yahoo/Fool 07-19] · *"**ASML shares fall after HIKING sales forecast for the second time this year** on strong AI chip demand"* [CNBC 07-15] · *"**ASML looks to INCREASE PRICES** of its Low-NA EUV tools… to capture the value of all the advantages its tools offer"* [Tom's Hardware 07-17] — **pricing power, the literal opposite of a capex de-rate.** |

### The one escalation this stage makes (a correction, not a reversal)
**§5 scored P2′ a clean HIT** (MU broke 848.95 < the 853.20 kill-line). **PREMORTEM downgraded it to a
CONTESTED HIT** (the line broke on **0.85× volume** in the same week ASML *raised* guidance twice and
DRAM was called *"abnormally high"*). **This drift scan now surfaces the same contradiction a third
time, independently, from the burst axis — a scan that knew nothing of the pre-mortem's argument.**

> **Three independent methods have now flagged that P2′'s fundamentals are accelerating while its
> price falls. That is no longer a caveat; it is the report's largest live falsification risk.**

**What does NOT change:** IT stays **UW**. The tape is the tape — SMH RS20 −11.1%, TSM distributing on
1.28× volume, XLK −5.8%; **a thesis is not a price.** MACRO §5 failure class 2 cuts both ways: a
fundamental datapoint may only *amplify* a proposition that has its own price confirmation, and the
bull case here has none yet.
**What DOES change — P2′'s falsification test is promoted from a caveat to a dated, first-class KPI:**
- **Falsifying observable:** **MU reclaims 848.95**, *or* **SMH RS20 turns positive** (−11.1% now),
  *or* a hyperscaler/foundry prints raised capex and **is rewarded on the capex line**.
- **Dated test: INTC prints 2026-07-23** (a date `CATALYST_WATCH.json` did not have — added by
  PREMORTEM §5). GOOGL **07-22**. Both inside the window.
- **The dissent that keeps it honest and is NOT papered over: MU short-vol z +1.71, 5v5 +3.2▲ — the
  only 🔴 reading on the board. Shorts are actively building.** AMAT points the other way
  (z **−2.08**, the strongest short-cover measured). **The two most informed positioning reads in
  semis disagree with each other. Recorded, not resolved.**

### Corrections this stage makes to the report above (stated, not silently patched)
1. **§4/§4a P3′ as written above is superseded twice over.** MACRO framed refining as *"anti-fragile
   to a TACO"*; **PREMORTEM Finding A reversed the sign** (escalation = crack-negative, ceasefire =
   crack-positive); **DEEP·ENRG then corrected PREMORTEM's generalization with data** — over 1 year
   corr(Δcrack, crude) = **+0.365** and on 33 crude>+3% days the crack **rose 67% of the time**.
   **Final standing version: the Hormuz binary is genuinely TWO-SIDED for refiners.** The original
   one-way claim stays visible above, per append-only. ⚠ **DRIFT flags for the next run: this sign
   was stated three different ways in one run. That instability is itself the finding.**
2. **§4 promoted HLTH to OW as a diversifier. DEEP·HLTH says the SECTOR is a defensive hedge** —
   XLV β to SPY **−0.16**, up-day excess **−0.74%** — so **PREMORTEM's Collapse 3 STANDS at sector
   level.** Only **HUM** is genuinely orthogonal (corr to SPY **+0.05**, the only positive up-day
   excess, **+0.45%**). **P7 as written above over-claimed.**
3. **§4's FIN OW is contradicted by its own deep-dive: DEEP·FIN returned LATE MONEY** and **BET
   promoted zero FIN candidates.** The exchange mechanism the OW was re-based onto **does not exist**
   in the numbers (CME RS60 −19.4%, z +1.88).
4. **§3's blindspot pass called `Dollar` (#7, 467) an unresolved blind spot. It is still unresolved** —
   DXY remains **9 days stale (07-10)** and nothing downstream priced it. Carried forward, not closed.
5. **P7's original corroborant has broken:** ISRG flow **−0.085**, delta **−0.41** (the sector's
   worst), OBV 매집→중립, RS20 −3.6% → **−14.4%**, vol **2.06×**. The 07-17 DRIFT built part of the
   HLTH case on ISRG's burst; **that leg is now gone**, and the HLTH case survives on the MLR print
   instead — a *better* foundation, arrived at by accident.

**DRIFT EXIT CHECK:** ✅ drift run — via the API-routed `burst` after `drift_watch.py` proved unusable
a second consecutive run (**tooling defect re-filed with its new failure mode, not hidden**) ·
✅ **every flagged item body-read, not counted** — the day's **largest** burst (Buffett, z 7.2) was
**rejected** on the read, and a smaller one (ASML, z 2.9) was **promoted** · ✅ **§5 ADDENDUM appended,
append-only — no line above was rewritten** · ✅ **no 🚨 regime flip: the report stands**, with P2′'s
falsification test escalated to a dated first-class KPI (INTC 07-23) and five corrections recorded.

---
**EXIT CHECK:** ✅ catalysts injected (**6 binaries**, incl. RTX/LMT 07-23 as P4's dated test) ·
✅ events read via `--body 2` across **both** market days, **tail = 0 both days, all 128 lines read**,
denominators cited (328→196→46 and 589→307→82) · ✅ trajectories read (`thread --days 7`) — **every
proposition names its thread's tag+curve or states "no thread"** (P1 "no thread, carried by
denominator"; P5 flagged: **its threads have ENDED**); per-day denominator read **before** interpreting
tags, and the weekend-FADING artifact corrected explicitly · ✅ 7-bucket sweep with **terms as separate
argv, recorded verbatim**, every bucket non-zero (3,860/3,758/3,266/2,834/2,364/1,645/1,429) — **plus a
self-caught contamination in my own defense bucket, cross-checked against `Lockheed` 19 / `Northrop`
10** · ✅ blindspot pass, `sample[]` + emergent terms read raw; **`Dollar` flagged as an unresolved
blind spot (DXY 9 days stale)**; new terms folded into the living table · ✅ indicators (FRED primaries
with explicit freshness flags + COT positioning as context-not-trigger) · ✅ continuity anchor
(07-17 MACRO_REPORT **incl. DRIFT addendum**) read; **handoff ledger EXISTS and was read** —
mode `DEGAJA_REPORT_DIR=llm_outputs`, stated in the header · ✅ **11-sector transmission matrix**
produced, **every matrix×flow divergence named with an owner (§4x a–e)** · ✅ self-backtest scored
with running hit-rate (**5H/1½/1O this run; 57% cumulative n=14**) + **2 new failure classes**.
**→ proceed to SWEEP.**
