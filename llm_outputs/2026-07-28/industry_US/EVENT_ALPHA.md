# EVENT_ALPHA — industry_US — 2026-07-28 (Tue)

> Stage 4/10. The **bottom-up** cross-check on MACRO's top-down matrix: which stories are *building*,
> and is money already following. Scope **`--scope foreign`** on every call (hard rule).
> Flow tags from `SECTOR_FLOW_US.json`, **`asof 2026-07-27 settled`**. Benchmark **SPY** inline (C1).
> **This stage never sizes** (P4). Analytical only.

---

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: **4,209 daily events → 3,223 threads → 523 multi-day → 157 alive**
(2,700 one-day, of which 226 new today). Per-day denominators **816 · 863 · 780 · 297 · 287 · 773 ·
393** — ⚠ today's 393 is **half the prior weekday's**, and this stage ran **pre-open**, so an intraday
US event cannot be in it (the D84 lesson, applied to the US session).

**8 threads selected · 149 alive threads NOT selected.** Selection rule applied in order:
(i) precursor form (starts ≤2 outlets and climbing) — **2 threads qualified: CXMT and Innolight**;
(ii) remaining BUILDING/REIGNITED by peak.

⚠ **Deliberately not selected, with reasons** (so the cap is a decision, not a truncation): the
litigation-alert thread (`2→2→2→2→2→2→3`, 144 articles — a law-firm press-release factory, D29 class);
the Zacks/ETF-comparison threads (`VDC vs FTXG`, `SCHD vs VIG` — syndication, not events); the Japan
earthquake and the France/Spain heatwave (**REIGNITED and large, but no listed transmission this desk
can measure**); the Ukraine warehouse-strike thread (REIGNITED 9→5→14→6→8→9 — the largest alive
non-market thread, carried by MACRO's geopolitical axis rather than by a card).

## ⚠ 0b · The exposure instrument failed this run, and the cards say so

**`chain-hop` is unusable on the US feed today, measured two ways:**
1. **D58 reproduces**: `chain-hop "DRAM memory capacity"` (3 tokens) scanned **0 articles**;
   `"Hormuz transit fee"` scanned **1**. Single tokens scan 257–1,464. **A silent zero.**
2. ★ **New — D10 (news-body boilerplate) is now measured on the US side.** With single tokens the
   headline-named lists are dominated by **GOOG/GOOGL/NDAQ/TSLA/META** on *every* theme, including
   `Hormuz` (GOOGL 258 body hits, NDAQ 222, META 156). Those are **embedded market-data widgets**, not
   content — verified directly: the CXMT body read for Card 1 contains an *"S&P 500 Top Gainers /
   Losers"* table listing SLB, DLR and INTC inside an article about a Chinese DRAM IPO.
3. ★ **New — `DRAM` is a poisoned token on the US feed**: it is also a **listed ETF ticker**, so
   *"DRAM, LASC: Big ETF Inflows"* and *"T-REX to Launch First-Ever U.S. 2X Inverse DRAM ETF (RAMZ)"*
   enter the theme. Same class as D63's `exchanges` (9,809 hits for a 7-name node).

⇒ **Every exposure map below was built BY HAND from `SECTOR_FLOW_US.json` and named in the card**, and
**no card claims coverage of "un-named beneficiaries one hop down."** (This is the discipline the KR
desk adopted when `module_industry_map` returned 0 rows — D59.) Filed as **D90**.

---

## Card 1 ★★★ — China's funded DRAM entrant: the supply-side falsifier, and the tape traded it today

| | |
|---|---|
| **Thread** | `[BUILDING] 2→2` *"Micron Rival CXMT's Stock Soars 466% After IPO"* — **precursor form** · plus `[BUILDING] 3→5` *"China is using the steel playbook on AI"* · `[REIGNITED] 3→4` *"China's reported chip breakthrough…"* · `[BUILDING] 5→2→10` *"Asia Stocks Slide, Weighed Down by Chip"* · `[REIGNITED] 3→6` *"SK Hynix, Samsung Drag Down KOSPI as China Chip Fears Spread"* |
| **Term axis** | **CXMT 3.51× pool-normalized — the only term on the board that separates**; `theme_age` **17.74× on n=273** against a runner-up of 5.32×; **85% of the week's coverage printed today** |
| **Denominator** | 2,475 articles → 393 events (07-28) |

**Direction (body-read, `[news]` Reuters via economictimes 07-27 + yahoo_finance) — and the headline
inverts it.** The headline is *"investors are betting big"*; the body is a **supply** statement:

- **¥57.92bn = $8.6bn raised**, and the prospectus states the proceeds go to *"expand production
  capacity, improve manufacturing technology and increase investment in R&D."*
- ★ **New numbers this desk did not have**: **Q1'26 revenue +719% YoY to ¥50.8bn ($7.51bn)**, and
  **H1'26 revenue guided to ¥110–120bn ≈ 2× the whole of FY2025 (¥61.8bn)**.
- **World #4 DRAM at ~7.7% share (2025)**; debut ¥49.50 vs an ¥8.66 IPO price = **+470%**;
  **mcap ≈ $487bn, past ICBC = China's most valuable listed company**, and *"roughly half that of
  Micron and SK Hynix"* on a far smaller share ⇒ **a strategic premium, priced.**
- **State-owned 36.29% pre-IPO** (Hefei/Anhui vehicles + the "Big Fund").
- ⚠ **Both halves (C2)**: it **lags badly in HBM**, has **no EUV**, is **~2 process generations
  behind**, is a **DoD "Chinese Military Company"**, and was *"approved by a US interagency committee
  for possible addition to the Entity List, though the move had not yet been implemented."*

**Exposure** — built by hand; flow tags `asof 2026-07-27 settled`:

| Ticker | Chain position | Flow tag | RS20 / RS60 vs SPY | Crowding |
|---|---|---|---|---|
| **MU** | The directly-substituted incumbent | **🔴분산** (−0.318), OBV 분산 | **−21.9 / +69.8** | Headline layer. FINRA 5v5 **+5.4▲** |
| **SNDK** | NAND-adjacent, the board's worst RS20 | **🔴분산** (−0.179) | **−40.2 / +16.2** | *"SNDK… Extend Slide Overnight Amid China's AI Challenge"*. 5v5 **+11.5▲** |
| **WDC · STX** | Storage, the second-order leg | 🟡 (−0.009 / −0.008) | −16.5 / +16.8 · **−10.6 / +23.1** | ★ **STX misses 🟢 by 0.03 of `vol_surge`, and prints 07-29** |
| **AMAT · LRCX · KLAC** | Equipment — **the leg that SELLS to a capacity build** | **🔴분산 all three** | −18.9 / +31.2 · −24.5 / +13.4 · −19.6 / +8.1 | ⚠ **The tape is treating a capacity announcement as bad news for the toolmakers, which is the opposite of the mechanical read.** Un-narrated |
| **AVGO** | The only non-boilerplate chain-hop candidate (15 proximity hits) | 🟢 **on velocity 2.06 with `vol_surge` 0.61** | +3.6 / **−9.3** | Held epicenter; ranks bottom of its own bucket |

**Future — both branches, mandatory.**
- **IF the thread keeps building AND a primary capacity figure lands** → **S34 branch A** (≥350k wpm by
  year-end): the regime call's *mechanism* changes from demand to supply, **commodity DRAM and HBM must
  be scored separately from here (W5)**, and **L2's peak-margin read on MU strengthens**.
  **Track KPI: CXMT 12-inch wafer capacity per month, from a Chinese regulatory filing / annual report
  / earnings call — NOT from news.** Horizon **2026-10-31**.
- **ELSE (kill condition)** → an **actual Entity List designation** blocking equipment access (the money
  then cannot be spent), **or** a disclosed capex plan materially below the raise, **or** the company
  guiding the 350k target down ⇒ **S34 branch B**, the card voids, and the regime call stands on its
  existing demand/price axes.
- ⚠⚠ **Do NOT score this card on the KOSPI.** Today's **−10.84% / −11.55%** KR session is a **price
  reaction**, and S34 forbids it as an observable at registration. It is cited here as *evidence the
  thread is being traded*, never as evidence of the capacity claim.

**Cell**: **CONFIRMED-EARLY on the narrative axis, LATE-MONEY on the incumbent leg.**
**Hand-off**: → **ROTATION §Info Tech** (this is the third independent axis pointing at the same split)
and → **PREMORTEM** (the equipment leg's reaction is un-narrated and points the wrong way).

---

## Card 2 ★★★ — Hormuz: the headline says "talks", the body says a TOLL BOOTH

| | |
|---|---|
| **Thread** | `[BUILDING] 3→5` *"U.S. and Iran edge toward talks as Hormuz shipping hits…"* → *"Iran and Oman Seek Agreement on the Hormuz in Bid to Jumpstart…"* [6 art/5 outlets] |
| **Term axis** | `de-escalation` **1.80× pool-normalized** (d1 76) · `Hormuz` 0.96× · `ceasefire` 0.95× · **`escalation` 0.82× = decelerating** · ⚠ **`reopen` 1.11× on d1 = 73** |
| **Day rank** | The day's **#1 event** is its consequence: *"Oil prices at lowest in over a week as pause in attacks brings…"* [**33 art / 15 outlets**] |

**Direction (body-read — and this is the card's whole point).** `[news]` **scmp/AFP 07-26** and
**bloomberg 07-27** *"Iran-Oman Talks Focused on Restarting Hormuz Shipping Traffic"*:

> Iran and Oman are discussing management of the Strait of Hormuz — **including imposing service fees,
> a move the US opposes.**

The talks are about *"common principles and operational mechanisms"* for safe passage **"while
respecting the sovereign rights of the two states."**

⇒ ★★ **This is not a reopening; it is a negotiation to convert the strait into a TOLLED waterway** —
a **permanent structural cost added** to the energy/freight chain, not a cost removed. Two further
body facts cut against the de-escalation read: **the US opposes the fee**, so Iran–Oman agreement is
not sufficient; and **a June MoU already existed and the US resumed strikes after it.**
★ **M184's pattern replicates exactly** (*"a negotiation, not a reopening"*), one week later, on a
different set of outlets.

**Exposure**, flow tags `asof 2026-07-27`:

| Ticker | Chain position | Flow tag | RS20 / RS60 | Note |
|---|---|---|---|---|
| **XOM · CVX** | Integrated — the war-premium carriers | **🟢 both, but on a velocity path** (`vol_surge` 0.82 / 0.78; `velocity` 3.02 / 2.14) | **+12.0 / −3.8** · **+9.7 / −5.0** | ★ **RS60 negative on both ⇒ M177's base-less leg. S31 settles XOM by 08-05** |
| **VLO · MPC · PSX** | Refining — the margin leg | 🟡 all three, **OBV 매집**, blocked by `vol_surge` 0.84 / 0.98 / 0.96 | +16.2 / +17.5 · **+21.6 / +25.3** · +19.7 / +15.9 | **The shortlist absence is a FILTER ARTIFACT (SWEEP §3)**, not money leaving |
| **STNG** | Tanker rates — the direct beneficiary of *longer* voyages | 🟡, news velocity **0.00×** | **+6.6 / −7.1** | **Prints 07-30 (S21)** — the only event-covering straddle, ±10.0% |
| **SLB · BKR** | Services | **SLB 🟢** (+0.789, `vol_surge` 1.22 = a **volume** path) · BKR 🟡 | +8.3 / **−11.4** · +5.7 / −15.8 | SLB is one of only three Energy greens and the only one on volume |

**Future — both branches.**
- **IF the thread keeps building AND the fee is actually agreed** → **the correct read is a permanent
  transit tax, i.e. structurally higher freight and a structurally wider Brent–WTI**, not a
  normalisation. **Track KPI: whether any published agreement text contains a fee schedule**, and the
  **settled 3-2-1 crack** (68.117 on 07-27; **kill at <60, now 8.12 points away**). Horizon: **S21
  settles 07-30; S8 has no date by construction.**
- **ELSE (kill condition)** → an actual **Iranian "Strait open" statement with no fee**, **or** the
  settled 3-2-1 crack below 60 ⇒ the card is wrong and this was ordinary de-escalation.
- ⚠ **Pre-declared no-information**: any STNG move **inside ±10.0%** (S21 branch C).

**Cell**: **CONFIRMED-EARLY (story building, money present but pointed at the wrong leg).**
**Hand-off**: → **ROTATION §Energy** with the explicit warning that the sector's greens are the
base-less integrated leg and the based leg is filter-suppressed.

---

## Card 3 ★★ — The physical leg is BUILDING while the price leg FADES, and they are the same sector

| | |
|---|---|
| **Thread** | `[BUILDING] 4→4→2→2→5` — *"Chinese Tankers Push Through Bab el-Mandeb"* → *"Saudi Red Sea Crude Exports Have Sunk 41% Since March Peak"* → *"Red Sea Tanker Traffic Falls to Multi-Month Low"* → **today: *"Tankers Divert to Egypt as Houthi Threat Upends Red Sea Trade"* [5/5]** |
| **Against it** | `[FADING] 15→27→19→5→14→22→15` — *"Oil prices jump back above $100 per barrel"*, the 7-day price thread, now rolled over |

**Direction (body-read, oilprice 07-28 + bloomberg 07-28)**: shippers are *"divert[ing] tankers to the
Suez Canal in Egypt to bypass"* the Bab el-Mandeb threat. **Saudi Red Sea crude exports −41% from the
March peak; Red Sea traffic at a multi-month low.** ⇒ **Physical disruption is deepening on the same
days the price of crude is falling.**

★★ **This is the card's finding and it is a contradiction inside one bucket**: the desk's
`Shipping/geo` bucket read **0.86× pool-normalized — the LOWEST on the board — on a day whose #1 event
was in it.** The bucket nets a fading *price* narrative against a building *physical* one. **D78's
exact shape, and SWEEP has already flagged that a bucket split is needed but was not made mid-run
(it would break comparability with the prior five sweeps).**

**Exposure**: **STNG · FRO · INSW · DHT · TNK** — ⚠ **an instrument gap the desk already carries: four
of the five are OUTSIDE `us_top300`, so this desk cannot tag them at all** (STANDING_VIEW §3a).
**STNG** is the only readable one: 🟡, **RS20 +6.6 / RS60 −7.1**, news velocity **0.00×**, short
**5.4% of float BUILDING**, on the reject ledger as `A.flow미도착` with recheck **2026-08-06**.

**Future — both branches.**
- **IF physical disruption keeps building AND STNG's Q2 shows it** → **S21 branch B** (TCE up, Q3
  bookings ≥ Q2, move outside ±10.0%) ⇒ **M45's "the blockade's literal beneficiaries are not being
  bought" becomes a genuine dislocation rather than a correct market judgment.**
  **Track KPI: STNG Q2 TCE $/day + % of Q3 days booked.** Horizon **2026-07-30**.
- **ELSE (kill condition)** → **S21 branch A** (TCE flat/down, Q3 bookings below Q2) ⇒ **the Red Sea
  rerouting rent has already peaked, S8 branch A arrives without any Hormuz statement**, and the
  Energy tilt's war-premium half is confirmed as the driver rather than the margin.
- **Cross-check KPI, pre-registered in S21**: the settled 3-2-1 crack holding **≥65** through 08-06
  invalidates branch A's read-across to refining. **It is at 68.117.**

**Cell**: **STORY-ONLY** — the story is building and **the desk has no instrument for four of the five
names**. **Hand-off**: watchlist with a dated re-check **2026-08-06**; **not** a candidate. ⚠ It did
**not** leak into the ROTATION hand-off.

---

## Card 4 ★★ — The dollar is making a one-month high on hike pricing while the breakeven falls

| | |
|---|---|
| **Thread** | `[BUILDING] 2→6` — *"Euro: Energy risks cap recovery against US Dollar – ING"* → **today: *"Dollar hits one-month high on lingering chances of Fed hike"* [16 art/6 outlets]**. Alongside: `[REIGNITED] 3→5→3` *"Federal Reserve: Holding rates while watching inflation"* · `[REIGNITED] 6→7→9→2→7→6` *"Why bond investors are pushing up some of your interest…"* · [6/6] *"8 Words From Fed Chair Kevin Warsh That Signal Where Interest…"* |
| **Term axis** | Rates/Fed **1.00× = exactly the pool rate** — the loudest thread on the board is **not** an elevated term (M186's shape again) |

**Direction (body-read + `[FRED]`)**: the narrative is a hike; **the curve did the opposite on the last
print — 2y −4bp to 4.33%, 10y −2bp to 4.69%** — and **the only series that advanced to 07-27, the
breakeven, FELL 5bp to 2.21%, three bp off its 120-day LOW.** ⇒ **The dollar's strength and the hike
pricing are riding a REAL-rate story whose inflation leg is deflating**, and the narrated trigger for
the whole thing (oil, per M69/M185) just made its lowest close in over a week.

**Exposure**, flow tags `asof 2026-07-27`:

| Ticker | Chain position | Flow tag | RS20 / RS60 | Note |
|---|---|---|---|---|
| **JPM · BAC** | Rate-sensitive banks | **🟢 both** (BAC is a `new_green`) | +6.9 / +11.3 · +6.0 / +13.6 | ⚠ **S23's flattener-hold is the live risk, not a hike** |
| **CB · TRV** | The FIN OW's internal hedge (β 0.125 / 0.339) | **CB 🟢** · **TRV 🟡 at flow +0.750, blocked by `vol_surge` 1.15** | +3.7 / +6.3 · **+17.9 / +25.3** | TRV's 🟡 is a filter artifact |
| **PCG · VST · CEG · NEE** | The rate-proxy short side | **all 🟡, Utilities 0 greens of 15** | −0.1 / +3.6 · −5.3 / −1.7 · +0.9 / −13.0 · −1.1 / −9.5 | ★ **PCG, carried as "Utilities' only 🟢", is no longer green** |
| **AMT · CCI** | The duration REITs | **🔴분산 both** | −6.4 / −10.3 · −11.7 / −17.5 | Falling with the real yield at its 120-day max |

**Future — both branches.**
- **IF the thread keeps building AND DGS2 closes >4.45% by 08-05** → **S19 branch H fires**; the
  duration de-rate becomes a regime call rather than positioning. **Track KPI: DGS2 daily, with DFII10
  quoted alongside T10YIE (S9's two-series rule).** Horizon **2026-08-05**. Distance **12bp**.
- **ELSE (kill condition)** → **DGS2 <4.15%** (18bp away), **or** the decomposition flipping to
  real-down / breakeven-up ⇒ the hike pricing was an oil echo and the card dies. **S19 branch M
  ("no conclusion changes") is the current state.**
- ⚠ **The branch neither of those covers is S23** — a hold with a further flattening, which kills NIM
  without tripping either threshold. **T10Y2Y is +0.36 and moved AWAY from its +0.20 trigger.**

**Cell**: **STORY-ONLY** — loud narrative, and the instrument it names moved the other way on the last
print. **Hand-off**: → **PREMORTEM** (three registered brackets, S19/S23/S9, all key off one 07-29
event). Dated re-check **2026-08-05**.

---

## Card 5 ★★ — The AI data-centre's live variable is the cost of capital, not the narrative

| | |
|---|---|
| **Thread** | `[REIGNITED] 4→2` *"Tech Stocks Tumble On Spending Worries"* **against** `[REIGNITED] 5→5` *"'The AI trade is still on': Wall Street sees Big Tech'[s]…"* — **two opposite-signed threads alive on one day.** Body tier: *"The Price to Finance the AI Data Center Boom Is Rising, Just Ask Meta"* [wsj] · *"Nvidia behind $50bn lease on Texas data centre"* [4 outlets] · *"Amazon winds down most flagship AI models in strategy overhaul"* [15/9] |
| **Term axis** | AI-capex **0.94×** · `AI spending` **1.00×** · `AI bubble` 0.99× · `digestion` 0.92× · `spending discipline` 0.88× · **`capex cut` 1.00× — measured for the first time on a correctly-formed query (R25)** |

**Direction (body-read)**: the axis has moved from *whether* hyperscalers spend to **what the spending
costs**. Corroborated on the primary: **M134 — GOOGL's Q2 free cash flow was −$5.86bn and it raised
$49.6bn of equity to fund AI capex.** ⇒ **HY OAS (2.79%, +11bp off its 365-day low over three prints)
is this node's live variable**, and the WSJ item names Meta specifically the day before Meta prints.
⚠ **Amazon "winding down most flagship AI models" is a product-strategy event, not a capex number** —
recorded as an event, **not** read as a capex signal.

**Exposure**, flow tags `asof 2026-07-27`:

| Ticker | Chain position | Flow tag | RS20 / RS60 | Note |
|---|---|---|---|---|
| **META · MSFT** | The spenders | **🟢 both — on VELOCITY** (`vol_surge` 0.65 / 0.69) | +6.5 / **−15.1** · +2.9 / **−12.2** | ★ **Their greens are pre-earnings press coverage, not accumulation (SWEEP §4).** META RS5 **−7.64**; FINRA z **−3.43 🟢** |
| **DLR · EQIX** | The physical landlords | **DLR 🟡 (RS20 exactly 0.0)** · **EQIX 🔴분산 (−0.629)** | 0.0 / −3.2 · −5.5 / −7.7 | **P5's anti-signal has fired: DLR's 20-day excess fully retraced.** EQIX prints **07-30** |
| **VST · CEG · GEV · VRT** | The power layer | **all 🟡; Utilities 0 greens of 15** | median RS20 **−5.68** | **S24 branch A holding** (threshold >0 by 08-12) |
| **DELL · HPE** | The server layer | **DELL 🟢 on velocity (`vol_surge` 0.58)** · **HPE 🟡 (`vol_surge` 0.46, the lowest measured)** | +5.5 / **+103.7** · +8.9 / **+66.4** | ★ **Both tags are artifacts; the case is RS-only.** Blind-spot pass surfaced *"HPE Rose on Strong AI Server Demand and Juniper Integration"* |

**Future — both branches.**
- **IF the financing-cost thread keeps building AND HY OAS reaches ≥3.10% on a close with NFCI turning
  positive WoW** → **S26 branch B**: this stops being an IT story and becomes the credit event in which
  **all three OW tilts lose together on one shared beta** (JPM 0.932 · DLR 0.769 · PLD 0.766 · PSX
  0.747). **Track KPI: HY OAS daily, NFCI weekly.** Horizon **2026-08-12**. Distance **31bp**.
- **ELSE (kill condition)** → spreads hold below 3.00% and the capex prints land without a financing
  question ⇒ **S26 branch A**, the three tilts remain three bets, and this card reduces to noise.
- ⚠ **NFCI is 11 days stale (07-17) against its own ≤7-day lag** — any financial-conditions claim this
  week must quote that.

**Cell**: **LATE-MONEY on the spenders** (greens are velocity paths into prints) · **STORY-ONLY on the
financing angle** (no instrument prices it). **Hand-off**: → **PREMORTEM** — S13/S16/S24/S26 all key
off the same 07-29→07-31 cluster.

---

## Card 6 ★ — "Overcapacity" is now a two-government argument, and it sits on top of Card 1

| | |
|---|---|
| **Thread** | `[BUILDING] 4→3→3→3→5` — *"US targets China in move to ban military-grade drone imports"* → *"The Persistence of US Trade Remedies Against China"* → *"China opposes US 'forced labor' tariffs"* [18/5] → **today: *"China hits back at criticism over excess industrial capacity"* [6/5]**. Alongside: *"China accuses U.S. of 'AI hegemonism,' threatens countermeasures"* [5/5] · *"US probes Chinese factories in Vietnam"* · *"Chinese AI developers may shift to 'paid weights'"* |
| **Term axis** | Tariff/trade **0.93×** · **`overcapacity` d1 = 4 ⇒ UNUSABLE n, recorded for comparability only (the D63 lesson)** |

**Direction (body-read)**: the trade thread has acquired a **supply-side vocabulary**. "Excess
industrial capacity" is the *same claim* Card 1 makes about CXMT, made by two governments about each
other — and **the DoD "Chinese Military Company" designation plus the un-implemented Entity List
approval are the mechanism that would stop CXMT's capacity money from being spendable.**
⇒ **Cards 1 and 6 are one risk, not two: the Entity List is simultaneously P9's anti-signal and this
card's escalation.**

**Exposure**: the same list as Card 1 (MU · SNDK · WDC · STX · AMAT · LRCX · KLAC), **plus the
equipment leg specifically** — an Entity List action is a *toolmaker* revenue event before it is a
memory event. Flow, with the **A-grade axis first (rule D6)**: **AMAT RS20 −18.9 / RS60 +31.2 ·
LRCX −24.5 / +13.4 · KLAC −19.6 / +8.1 vs SPY**, all three 🔴 (−0.400 / −0.312 / −0.321), with **OBV
분산 agreeing as a C-grade corroborant, not as the finding.**

**Future — both branches.**
- **IF the thread keeps building AND an Entity List designation is actually implemented** → **P9's
  registered anti-signal fires**: CXMT's capacity money cannot be spent, S34 tilts to branch B, and
  the equipment leg takes a China-revenue hit that the memory leg does not. **Track KPI: the Federal
  Register / BIS entity-list notice.** Horizon **`[blank]` — no date is guessed.**
- **ELSE (kill condition)** → the approval stays un-implemented through 2026-10-31 (S34's date) ⇒ the
  constraint is rhetorical and Card 1 runs unimpeded.

**Cell**: **STORY-ONLY** (no dated instrument). **Hand-off**: → **PREMORTEM** as **the anti-signal leg
of Card 1**, not as a separate candidate.

---

## Card 7 ★ — A second Chinese AI-hardware capital raise inside one week

| | |
|---|---|
| **Thread** | `[BUILDING] 3→3` — *"Innolight Is Said Set to Price Hong Kong Listing Below Maximum"* (07-27) → *"Zhongji Innolight raises $8.8 billion in Asia's second-largest listing"* (07-28) — **precursor form** |

**Direction (body-read)**: an optical-transceiver maker — the **interconnect** layer of an AI
datacentre — raised at scale in Hong Kong, **priced BELOW its maximum**. Read together with Card 1
this is a pattern: **China is capitalising two different layers of the AI hardware stack in one week,
and the market is paying up for the memory one (+470%) while marking the interconnect one down (below
max).** ⇒ **The premium is being paid for *substitution of a constrained input*, not for AI exposure
generally.** That distinction is the reason Card 1 is a supply card and this one is not.

⚠⚠ **Provider disagreement, declared not resolved (D5)**: **bloomberg 07-28 headlines it
*"Innolight Prices $6.8 Billion Hong Kong Listing Below Maximum"*** while the thread's own later title
says **$8.8 billion**. **Two figures for one deal, in the same feed, within a day.** No figure is
adopted; the card is written on the *direction* (priced below max), which both agree on.

**Exposure** (US-listed interconnect/optical adjacency, tags `asof 2026-07-27`): **ANET** — 🟡, prints
**2026-08-04**; **AVGO** — 🟢 on velocity 2.06 / `vol_surge` 0.61, RS20 +3.6 / RS60 **−9.3**;
**CIEN** and **COHR** are outside the tagged set here. ⚠ **This card's exposure is the weakest of the
eight and is stated as such.**

**Future — both branches.**
- **IF the pattern keeps building** (a third Chinese raise in another AI-hardware layer within
  ~4 weeks) → the "China funds its own AI supply chain layer by layer" read becomes a **thesis** rather
  than two datapoints. **Track KPI: count of Chinese AI-hardware primary raises ≥$1bn.** Horizon
  **2026-08-25** (4 weeks).
- **ELSE (kill condition)** → no third raise by 2026-08-25 ⇒ two deals in a week was an IPO-window
  artifact and the card dies.

**Cell**: **STORY-ONLY**. **Hand-off**: watchlist, dated re-check **2026-08-25**. Did **not** enter the
candidate hand-off.

---

## Card 8 ★ — Japan: the duration channel that the desk still may not cite

| | |
|---|---|
| **Thread** | `[BUILDING] 3→3→3→2→4` — the yen/BoJ thread, 5 days · `[REIGNITED] 4→2` *"BOJ Is Said to Be Open to Faster Pace of Rate Hikes"* · today *"Japanese Yen stays range-bound as Fed, BoJ seen on hold but ha[wkish]"* [5/4] · *"Japanese Market Sharply Lower, Tumbles 4%"* · *"Losses May Accelerate For Japan Stock Market"* |

**Direction (body-read)**: the BoJ is signalling a faster tightening pace into an FOMC week, and the
Japanese equity market fell 4% on the same chip rout as Korea. **P7's status is HELD in the scored
tier for a second consecutive run.**

⚠⚠ **This card is written and may NOT be cited as evidence by any downstream stage.** The claim
*"BOJ tightening leads US long-end yields"* is **`[unverified]` under rule W2** and **D22 — the lag
table that would settle it — has never been built.** The 07-25 escalation was *"either D22 gets built
or P7 is retired"*; **two consecutive runs in the scored tier now argue for building it.**

**Exposure**: **none named.** ★ **That is deliberate and is the card's honest position** — naming US
tickers off an unverified lead/lag claim is precisely the R5 failure (*"EDA leads semis by 12–18
months"*, measured coincident at 0.63 same-month vs 0.02–0.05 at lag-12).

**Future — both branches.**
- **IF D22 is built and the lag table shows a real lead** → P7 becomes citable and this card acquires
  an exposure map. **Track KPI: the correlation table itself.** Horizon **`[blank]` — it is a build, not
  an event.**
- **ELSE (kill condition)** → **P7 leaves the scored news tier for two consecutive runs** ⇒ retire it.

**Cell**: **STORY-ONLY, flagged non-citable.** **Hand-off**: → **the dig list (D22)**, not to ROTATION.

---

## 9 · DEAD verdicts and the reject ledger

⚠ **DEAD is a MONEY verdict, not a story verdict** — FADING/ENDED **×** 🔴 dispersing, *both* axes.
**No card scored DEAD this run.** In particular:

- **The oil-price thread is 🔴FADING but XOM/CVX are 🟢** ⇒ **not DEAD.** It is re-filed as Card 2 with
  a rewritten thesis line (*"a toll negotiation, not a reopening"*) and a dated re-check, exactly per
  the rule that produced the 475150 lesson.

**Two US rejections filed this run** (D27: keep filing ≥1 per US run — the ledger's asymmetry finding
was measured on KR data only and does not transfer under **W1**). Both carry `--revives-if` and
`--recheck-date`; the script accepts no other form.

| Ticker | Class | Basis (measured) | Revives if | Recheck |
|---|---|---|---|---|
| **JNJ** | `K.본문반증` | Health Care's **only** 🟢 of 32, and its green is a **velocity path** (`velocity` 2.57, `vol_surge` 0.96 — no volume confirmation). The body identifies the news that produced it: **the $5.5bn talc settlement, 10 articles / 10 outlets.** A litigation settlement is not accumulation | A 🟢 with `vol_surge` ≥1.2 (a volume path), **or** any 🟢 from outside the HLTH top-6 by cap — which is **C7's own registered resolving observable** | **2026-08-06** (C7's horizon) |
| **GEV** | `A.flow미도착` | OBV **분산** with **RS20 −6.0 / RS60 −10.1 vs SPY** while carrying **`velocity` 2.97 — the loudest news of the four-name AI-power basket.** Story present, money leaving | RS20 vs SPY turning positive **and** OBV flipping to 매집 | **2026-08-12** (S24's own horizon) |

⚠ **GEV is a member of S24's frozen basket.** Filing a rejection **does not touch S24** — the bracket's
observable is the four-name median and stays exactly as frozen. Stated so the two are not confused.

## 10 · Book cross-check — ENDED threads under an open position

**No ENDED thread sits under an open book position.** ⚠ But one book fact surfaced in SWEEP §5 belongs
here: `CYCLE_EXPOSURE.json` shows the adjacent/fuel layer collapsing from **(VST, KMI, LNG) → (LNG)**
and Energy's held epicenter going **XOM → PSX, XOM**, with the book at roughly **62% cash**.
**n = 1 session (S1); reported to the book desk as an observation to confirm, not a conclusion.**

## 11 · Hand-off

**CONFIRMED-EARLY → ROTATION / BET §B**: **Card 1 (China DRAM supply)** and **Card 2 (Hormuz toll)**.
**STORY-ONLY → watchlist with dated re-checks**: Card 3 (08-06) · Card 4 (08-05) · Card 6 (`[blank]`) ·
Card 7 (08-25) · Card 8 (non-citable).
**LATE-MONEY → valuation-gate note**: Card 5's spender leg (META/MSFT greens are velocity paths into
their own prints).
**No STORY-ONLY name leaked into the candidate hand-off.**
