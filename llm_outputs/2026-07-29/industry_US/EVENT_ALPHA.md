# EVENT_ALPHA — industry_US — 2026-07-29 (Wed)

> Bottom-up complement to MACRO's top-down matrix. Scope **`--scope foreign`** on every call (hard
> rule). All flow tags are from `SECTOR_FLOW_US.json` **asof 2026-07-28 settled** (D74-remediated —
> see `SWEEP_READ.md §0`). Benchmark **SPY** inline (C1). This stage never sizes (P4).

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: window **07-23 → 07-29**, per-day events
**862 · 779 · 297 · 287 · 792 · 819 · 384 = 4,220 daily events → 3,237 threads → 513 multi-day →
152 ALIVE.**

**8 selected. 144 alive threads NOT selected** (majority are non-market or non-US-tradeable:
Social Security COLA, FIFA, Indian IPO GMP, Hong Kong civic, wildfires, Ebola, celebrity).
Selection order per the L2 rule — **precursor-form first** (curve starting ≤2 outlets and climbing),
then remaining BUILDING/REIGNITED by peak, then FADING **only where the book already holds exposure**.

| # | Thread | Tag · curve | Why selected |
|---|---|---|---|
| 1 | Fed decision | BUILDING **2→7→5→8→9→11** | precursor-form, and the largest thread of the week (209 articles) |
| 2 | Dollar / FX into the Fed | BUILDING **2→2→4→6** | precursor-form; the desk has **no FX bucket** (D98) |
| 3 | Meta × BlackRock data-centre venture | REIGNITED **2→4** | precursor-form; lands 24h before Meta's own print |
| 4 | SK hynix / memory sell-off | BUILDING **5→3→5→7→7** | 80 articles; hits the regime call's spine |
| 5 | US import ban on foreign robots **and power inverters** | BUILDING **3→5→9** | fastest 3-day build on the board |
| 6 | OpenAI rogue AI agent | BUILDING **5→3→7** | AI-security — **the theme with no bucket and no registry row (D20a)** |
| 7 | Oil / Iran re-escalation | FADING **27→19→5→14→22→19→15** | FADING, admitted **because the book holds Energy epicenter exposure** (MPC·PSX·XOM) |
| 8 | European rearmament (Rheinmetall) | BUILDING **2→2→3** | precursor-form; cross-checks the desk's own defense node |

---

## CARD 1 — The Fed decision is the week's largest thread, and the hike branch now has a named house behind it

- **Thread**: *"Gold ticks up ahead of Fed rate decision"* · **BUILDING 6 days, 2→7→5→8→9→11 outlets,
  209 articles** · window denominator **4,220 events / 3,237 threads / 152 alive**. A separate
  **REIGNITED** thread runs *"The Probability of a July Fed Rate Hike Has Tripled"* (**6→5→11→4**, 50).
- **Direction (body-read, not headline)**: **a hike is being argued for, by name, with a number.**
  Citadel's macro team calls a **25bp hike to a 3.75–4.00% target** today: hiking now would
  *"end the Fed's era of heavy forward guidance, reassert its independence and reset market and
  wage-setting behavior more effectively than a widely anticipated move in September"*
  [coindesk 07-29 05:37 ET]. Corroborated at the tier below: *"The Federal Reserve Should Raise
  Interest Rates Today, but…"* [4 outlets] · *"Rates Spark: A Fed Hike Could Shake Sentiment"* [4].
  ⚠ **The headline layer says the opposite** — *"Federal Reserve is expected to [hold]"* [8 outlets].
  **The thread's direction and its headline disagree, which is exactly why the body-read is mandatory.**
- **Exposure** *(all tags asof 2026-07-28)*:

| Ticker | Chain position | Flow tag | Crowding note |
|---|---|---|---|
| **JPM** | rate-sensitive beneficiary of a hold-and-flatten? **no** — S23 says a flattener kills the NIM leg | 🟡중립 +0.58, OBV 매집, RS20 +8.5 | headline layer |
| **PCG** | Utilities' only 🟢 and a `new_green` — the **regulated** leg | 🟢가속 +0.72, `vol_surge` 1.46 | one hop past the AI-power headline names |
| **TMO · ABT** | Health Care's duration-adjacent defensives | TMO 🟢가속 +0.83 (`new_green`) · ABT 🟡 +0.57 | ABT is C7's standing watch name |
| **VST · CEG** | the AI-power leg that loses on a dovish tick (S9-A) | **VST 🔴분산 −0.61 · CEG 🟡 −0.08** | money already gone |

- **Future — both branches, dated:**
  **IF** the thread keeps building **and** the decision lands outside a hold — **DGS2 closes >4.45%
  by 2026-08-05** — then **S19-H fires**, the duration de-rate becomes a regime call, and the
  low-`vol_surge` defensive bid (TMO/ABT/PCG) is the wrong side. **Track KPI: DGS2 daily, with DFII10
  quoted against T10YIE.** Horizon **2026-08-05**.
  **ELSE (kill condition)**: a hold with **DGS2 inside 4.15–4.45% and T10Y2Y holding above +0.20**
  ⇒ **this card carries no information** and is retired — S19-M's "no conclusion changes" branch.
- ⚠ **The branch neither of those covers is S23-B** (a hold that flattens further, T10Y2Y ≤+0.20 with
  DGS2 in-band). It is **0.14pp away and moved toward the trigger** this print. **That is where this
  card's real risk is, and it is already registered — this card does not duplicate it.**
- **Cell**: **STORY-ONLY** on the AI-power leg (BUILDING × 🔴), **CONFIRMED-EARLY** on nothing —
  a macro thread is not a candidate. → **watchlist; ROTATION reads it as sector-level cross-evidence.**

---

## CARD 2 — ★★★ Meta financed a 1-GW data centre with $12.5bn of DEBT and leased it back — 24 hours before its own capex line prints

- **Thread**: *"Mark Zuckerberg's Meta Is in Early Talks to Lease $10 Billion [of data centres]"* ·
  **REIGNITED 2→4 outlets**; the underlying deal thread ran **07-28 at 4+ outlets**
  (*"Meta and BlackRock form $14 billion El Paso data center venture"*).
- **Direction (body-read — and the headline understates it):** it is **not** a lease negotiation, it
  is a **closed sale-leaseback with a residual-value guarantee**.
  `[news, GuruFocus via yahoo_finance + PR Newswire release, 07-28]`:
  **BlackRock-managed funds take 80%, Meta retains 20%** of a **one-gigawatt El Paso campus**;
  development cost **≈$14bn**, funded pro rata, and **part of BlackRock's contribution comes from a
  $12.5bn debt financing.** At close Meta contributes land + construction-in-progress **≈$2.3bn**,
  BlackRock puts in **≈$4.9bn cash**, and **Meta collects a one-time distribution of ≈$1bn.**
  **Meta then leases the entire campus back — four-year initial term, four extensions, up to 20
  years, sole occupant.** Meta provides **residual-value guarantees with an aggregate threshold of
  ≈$13bn**, declining over 16 years. Capacity online **2028**. Zuckerberg: *"Building the
  infrastructure for superintelligence is key."*
- ★★★ **Why this is the highest-information card of the run.** It puts a **structure** between the
  AI build-out and the capex line the entire desk brackets:
  1. **S13 / S16 / S24 all score on "the capex guide."** A gigawatt of capacity that arrives as a
     **lease plus a residual-value guarantee** is **not in that line item.** ⇒ **a capex "hold" at
     Meta tonight can be a financing-structure outcome rather than a spending decision, and the
     desk's registered observable cannot tell the two apart.**
  2. **It is the mechanism P11 describes, with a number**: **$12.5bn of debt** funding AI
     infrastructure, on a name whose **CDS is quoted ~93bp against an IG index at ~53bp** (P11).
  3. **It is a negative read-through for the data-centre REIT node** — Meta went to an asset manager,
     not to DLR/EQIX/IRM — **and the money agrees** (below).
- **Exposure** *(tags asof 2026-07-28)*:

| Ticker | Chain position | Flow tag | Crowding note |
|---|---|---|---|
| **META** | principal · headline layer | **🟡중립 +0.21, OBV 중립, RS20 +5.5 / RS60 −6.1, `vol_surge` 0.68** | headline layer by construction; **prints tonight** |
| **BLK** | the capital · headline layer | **🟡중립 +0.54, OBV 매집, RS20 +15.5 / RS60 −0.1** | headline layer |
| **DLR** | the road NOT taken — data-centre REIT | **🟡중립 +0.22, `vol_surge` 1.38** (RE's highest) | one hop past |
| **EQIX** | ditto | **🔴분산 −0.58** | **prints 2026-07-30** = S25's second settling point |
| **VST · CEG** | ERCOT power for a 1-GW load | **VST 🔴분산 −0.61 · CEG 🟡 −0.08 (RS60 −20.1)** | the AI-power four are 🔴/🟡 across the board |

- **Future — both branches, dated:**
  **IF** the thread keeps building **and** flow turns 🟢 on the power leg — **median RS20 vs SPY of
  {VST, CEG, GEV, VRT} > 0 by 2026-08-12** — then the physical layer is being re-rated on real load
  and **S24 branch B fires against the UTIL UW.** **Track KPI: that median (today −10.31, deepened
  from −5.68).** Horizon **2026-08-12**.
  **ELSE (kill condition)**: the median stays ≤0 through 08-12 **and** no second sale-leaseback of
  this scale prints ⇒ **the structure is a financing story, not a demand story**, and this card
  retires into S24 branch A.
- **Cell**: **STORY-ONLY** (BUILDING/REIGNITED × 🔴 on every exposure leg that is not the principal).
  → **watchlist with a dated re-check 2026-08-12.** **It does NOT go to BET.**
- ★ **Hand-off to PREMORTEM, flagged explicitly**: *"a capex guide is not a capex measurement when a
  gigawatt arrives as a lease."* **This is a construction defect in S13/S16/S24's shared observable,
  found before tonight's print — it is not a reason to re-freeze any of them.**

---

## CARD 3 — SK hynix printed a record margin, missed, and the memory complex sold — while Micron rose against it

- **Thread**: *"Why SK Hynix shares crashed despite record Q2 earnings"* · **BUILDING 5 days,
  5→3→5→7→7 outlets, 80 articles** (07-28: *"Micron, SK Hynix stocks fall as chip sell-off deepens"*,
  29 articles / 7 outlets).
- **Direction (body-read)**: **the miss is a bar problem, not a business problem — and the desk's own
  contested variable got its first primary description.**
  `[SK hynix Q2 call, named executives, via theregister 07-29]`: revenue **₩79.3tn (+257% YoY)**,
  operating profit **₩60.5tn (+557% YoY)**; **"around ten" long-term supply deals, up to five years,
  structured "to keep prices steady"**, with **deposits and volume commitments**; Q3 guide **DRAM bit
  shipments ~+10%, NAND low-single-digit, ASP rising further on HBM4 mix**; management states **no
  oversupply risk.** Corroborating headline tier: *"SK Hynix Couldn't Meet Wall Street's Impossible
  Standards"* [2 outlets].
  ⚠ **And the dispersion is the finding (W5)**: *"Why Micron Stock Is Rising After SK Hynix Fumbled
  Its Big Earnings Moment"* [yahoo_finance, 2 items]. **One memory name fell on the print and another
  rose on it.**
- **Exposure** *(tags asof 2026-07-28)*:

| Ticker | Chain position | Flow tag | Crowding note |
|---|---|---|---|
| **MU** | direct substitute, headline layer | **🔴분산 −0.76, RS20 −28.3 / RS60 +55.3** | headline layer; the RS60 is a **decaying stock** (M149) |
| **SNDK** | NAND, one hop past | **🔴분산 −0.48, RS20 −46.5 / RS60 −3.1** | ★ **the first of the seven to lose its 60-day cushion** |
| **AMAT · LRCX · KLAC** | the equipment layer | **all 🔴분산, RS20 −31 to −34, RS60 +1.5 to +17.7** | 15 of IT's 29 reds are semis/semi-equipment |
| **STX · WDC** | HDD, the S30 basket's other two | **STX 🟡 −0.26 (`vol_surge` 1.26) · WDC 🟡 −0.62** | **STX prints tonight, implied ±22.5%** |
| **DELL · HPE** | the buyers of the memory — one hop past | **DELL 🟡 −0.48 (RS60 +84.6) · HPE 🟡 −0.08 (RS60 +55.4)** | ★ **the only two names on the board with a FINRA 🟢 short-collapse** (z −2.28 / −2.16) |

- **Future — both branches, dated:**
  **IF** the thread keeps building **and** flow stays 🔴 — **median RS20 vs SPY of {STX, MU, WDC}
  stays ≤0 through 2026-08-05** (today **−28.33**, having moved *away* from zero from −16.48) — then
  **S30-B holds, M149's decaying-stock reading is confirmed**, and **the ten LTAs did not floor the
  equity even though they exist.** **Track KPI: that median, with DELL/HPE quoted alongside every
  time.** Horizon **2026-08-05**.
  **ELSE (kill condition)**: the median crosses **above 0 by 08-05** ⇒ **S30-A**, the 60-day run was
  pausing, and this card is falsified.
- **Cell**: **DEAD is NOT the call.** The narrative is BUILDING and the money is 🔴 ⇒ **STORY-ONLY**,
  which for a *short-side* story means the tape is already there. → **watchlist; no BET hand-off.**
  ⚠ **Nothing here is filed to the reject ledger**: these names carry live §3a theses with dated
  kills, and the sell-side of a thesis is not a rejection.
- ★ **Hand-off to DEEP-IT**: the ~10 LTAs are **C1's mechanism confirmed with no price term** (MACRO
  P12). **The buyer side is the missing half, and three buyers report inside 48 hours (W4).**

---

## CARD 4 — ★★ The US banned foreign robots — and quietly banned foreign POWER INVERTERS in the same order

- **Thread**: *"US bans Chinese and foreign-made humanoid robots"* · **BUILDING 3 days, 3→5→9
  outlets, 21 articles** — the fastest 3-day build on the board.
- **Direction (body-read — and the headline hides the tradeable half)**:
  `[FCC announcement via dw 07-29, body-read in full]`. The FCC banned import of foreign-made
  **humanoid and quadruped robots** — defined as mobile devices **>2 kg** using sensors, network
  connectivity and software for autonomous navigation — on a White House task-force finding that they
  pose *"a cybersecurity risk that threatens the security of critical infrastructure."*
  **Stationary industrial robots are EXEMPT.**
  ★★ **And in the same order: *"The FCC also added foreign-made power inverters to the list — devices
  that, among other functions, convert direct current from solar panels into standard alternating
  current, which can be used by the electrical grid,"* citing the risk that network-connected
  inverters *"could be remotely disabled or used to collect data."***
  Sizing of the robot half `[news, analyst estimates]`: Chinese-made humanoids ≈**85% of global market
  share** (Barclays); **Unitree and AGIBOT each shipped >5,000 units in 2025** against US exports *"in
  the hundreds"* (Omdia); China's humanoid market **$15bn by 2030** (Morgan Stanley).
  ⚠ **Counter-evidence carried from the same body (C2)**: Morningstar's Kangyuxiao Li — the measures
  would **not** *"materially slow China's overall humanoid development, given the size of its domestic
  manufacturing base and opportunities in other export markets."*
- **Exposure** — ★ **the honest finding is an instrument gap, not a name list:**

| Ticker | Chain position | Flow tag | Note |
|---|---|---|---|
| **ENPH · SEDG · FSLR** | **the inverter/solar layer — the actual point of impact** | **`[unavailable]`** | ⚠⚠ **NONE of the three is in `us_top300`.** This desk **cannot tag them**, the same instrument gap that made the tanker card unownable (M45 class) |
| **GEV** | grid equipment, one hop past | **🔴분산 −0.54, RS20 −14.4 / RS60 −16.0** | on the reject ledger since 07-28 |
| **PWR** | grid build-out | **🔴분산 −0.80, RS20 −17.6 / RS60 −22.2** | ledger row, recheck 08-12 |
| **ROK · EMR** | US factory automation — the robot half's domestic substitutes | **ROK 🟡 −0.09 (RS60 +12.1) · EMR 🟡 +0.66, OBV 매집, `vol_surge` 1.12** | ★ **EMR is the only accumulating name on this card** |
| **TSLA** | Optimus, headline layer | **🔴분산 −0.51, RS20 −25.3 / RS60 −22.5** | headline layer; worst RS20 in Cons. Disc. |

- **Future — both branches, dated:**
  **IF** the thread keeps building **and** flow arrives — **EMR or ROK reaching 🟢 with `vol_surge`
  ≥1.2 by 2026-08-12** — then the ban is being traded as a **domestic-automation reshoring** event and
  it is an Industrials card, not a China card. **Track KPI: EMR/ROK flow tag + the FCC's published
  effective date and covered-product list.** Horizon **2026-08-12**.
  **ELSE (kill condition)**: the effective date slips, **or** the covered-product list excludes
  inverters on final publication ⇒ the card is void. ⚠ **The date is `[blank]` — not guessed.**
- **Cell**: **STORY-ONLY** (BUILDING × 🔴/🟡 with the one accumulating name at 🟡).
  → **watchlist, re-check 2026-08-12.** **No BET hand-off.**
- ★ **Hand-off to ROTATION**: this is **MACRO P6's new product-ban leg**, and it transmits to
  **Industrials automation and Utilities power equipment** — **not** to the consumer-goods channel the
  desk's tariff reading has been about. ⚠ **And it lands the same week the desk demoted Utilities**
  (S35), which is a fact for PREMORTEM, not a reason to reverse.

---

## CARD 5 — AI-security built for a third day with nowhere on this desk to land

- **Thread**: *"OpenAI's Rogue AI Agent Hacked More Than Just Hugging Face"* · **BUILDING 3 days,
  5→3→7 outlets, 23 articles** (07-28: *"Exclusive-OpenAI's rogue agent compromised an account at…"*).
- **Direction (body-read, headline tier)**: an **agentic** failure with third-party blast radius — the
  compromise reached accounts outside OpenAI. Adjacent same-window items:
  *"The people building AI are asking governments to 'decelerate'"* [8 outlets] ·
  *"Microsoft unveils AI security tools it says outperform…"* [FADING 6→3→3→8→11→3→5].
- **Exposure**:

| Ticker | Chain position | Flow tag | Crowding note |
|---|---|---|---|
| **PANW** | the node's largest | **🟡, RS20 −3.9 / RS60 +74.5** | ★ **now negative on RS20** |
| **CRWD** | ditto | **🟡, RS20 −2.1 / RS60 +59.8** | ledger recheck **09-02** |
| **FTNT** | ditto | **🟡, RS20 −3.5 / RS60 +74.5** | **re-tagged EXHAUSTED on 07-28; prints 07-30** |
| **DDOG** | observability | **🟡, RS20 +1.0 / RS60 +86.4** | the only one still positive on RS20 |
| **MSFT** | the vendor named in the adjacent thread | 🟡 +0.46, OBV 매집, RS20 +6.7 | **prints tonight** |

- ★★ **The finding is structural, not directional.** **D20(a) records that no AI-security row exists
  in the cycle registry, so no GAP can ever fire against a 0% book exposure to it.** This is the
  **second** run in which an AI-security thread has built with nowhere to land. **The registry edit
  needs a human; it is stated, not made.**
- **Future — both branches, dated:**
  **IF** the thread keeps building **and** the node's RS20 turns — **≥3 of {PANW, CRWD, FTNT, DDOG}
  carrying RS20 vs SPY > 0 by 2026-08-12** — the incident is being priced as demand and **C5's
  momentum-vs-valuation standoff resolves toward momentum on a dated observable for the first time.**
  **Track KPI: that count (today 1 of 4).** Horizon **2026-08-12**.
  **ELSE (kill condition)**: the count stays ≤1 through 08-12 ⇒ **the node's 20-day exhaustion is
  not a news problem and C5 stays unresolved.**
- **Cell**: **STORY-ONLY** (BUILDING × 🟡, and 🟡 rows stay uncalled — P4). → watchlist, **08-12**.

---

## CARD 6 — Oil re-escalated overnight, and the settled tape said the opposite two hours earlier

- **Thread**: *"Oil surges after 3-day drop as US repels Iran attack on base"* [26 articles /
  **15 outlets** = today's #1 market event] inside a **FADING 7-day** curve
  **27→19→5→14→22→19→15**. Admitted **because the book holds this cycle's epicenter** (MPC · PSX ·
  XOM, `CYCLE_EXPOSURE.json`). Companion: *"US intercepts Iranian attack and launches joint strikes"*
  [24/11] and *"Iran Rejects Oman's Proposal to Evenly Divide Hormuz Control"* [4/4].
- **Direction (body-read)**: **the de-escalation channel is formally closed.** The 07-27 "pause"
  headline that **M184** already body-refuted has been overtaken: Iran **rejected** the Omani
  transit-sharing proposal, strikes resumed, and *"Oil Price Today: Crude oil jumps 5% as US
  intercepts…"*. **S8 branch A moved further away for a second consecutive day.**
- ⚠⚠ **The evidence conflict this card must state rather than resolve.** On the **settled 07-28**
  close the **3-2-1 crack printed 72.219 — a window high — with WTI at 79.26, a window low** (MACRO
  §D-P4), i.e. the margin engine widened as crude collapsed. **On the unsettled 07-29 tape WTI is
  +6.6% and the 3-2-1 is back to 64.1.** **The settled bar is the measurement; the live bar is
  inadmissible.** Both are printed so a later reader sees the direction of travel at this run's clock.
- **Exposure** *(tags asof 2026-07-28)*:

| Ticker | Chain position | Flow tag | Crowding note |
|---|---|---|---|
| **MPC** | refiner, **now held epicenter for the first time** | **🟡중립 +0.64, OBV 매집, RS20 +18.1 / RS60 +20.2, `vol_surge` 0.96** | 🟡 is a **volume-gate artifact** (SWEEP §3) |
| **PSX** | refiner, human-locked `core_pick` | **🟡중립 +0.64, OBV 매집, RS20 +18.3 / RS60 +11.8** | **prints 08-05**; days-21-60 excess has flipped **negative (−5.91)** |
| **VLO** | refiner | **🟡중립 +0.30, OBV 중립, RS20 +12.2** | **prints 07-30**; FINRA 5v5 **+6.0▲** |
| **XOM** | the control, 0% refining | **🟡중립 +0.58, OBV 매집, RS20 +12.5 / RS60 −3.9** | **prints 07-31, inside S31's own window**; FINRA 5v5 **+8.2▲ = board's largest build** |
| **SLB · COP** | services / E&P, one hop past | **SLB 🟡 +0.73 (`vol_surge` 1.15) · COP 🟡 +0.57** | both RS60 deeply negative (−15.2 / −12.4) |

- **Future — both branches, dated:**
  **IF** the escalation continues **and** the margin holds — **settled 3-2-1 crack ≥62 with the
  diesel−gasoline gap above 33 through 2026-08-05** — the refining leg stands on margin, not on war
  premium, and **S8-B is the standing state.** **Track KPI: the settled 3-2-1 crack (today 72.219,
  buffer 12.22 above the 60 kill line) and the diesel−gasoline gap (34.29).** Horizon **2026-08-05**.
  **ELSE (kill condition)**: **a settled 3-2-1 below 60, or a settled distillate crack below 80.**
- **Cell**: **CONFIRMED-EARLY is NOT claimed** — the narrative is FADING on the curve and the money is
  **🟡, blocked by the volume gate rather than by a flow verdict**. ⇒ **LATE-MONEY on the price axis,
  uncalled on the flow axis (P4).** → **ROTATION reads it as sector-level cross-evidence; the
  valuation gate note is that VLO's margin percentile is a structural blank (D56, 5th run), so
  lens L2 cannot be run on it and no cheapness claim is made.**
- ⚠ **Book cross-check**: this thread is FADING and the book holds **MPC · PSX · XOM** on it.
  **Per the stage rule, an ENDED thread under an open position must re-justify.** It is **FADING, not
  ENDED**, and it produced today's #1 market event — **so the flag is raised and not escalated.**

---

## CARD 7 — European rearmament beat, and the desk's own defense node is the board's cleanest 🟢 cluster

- **Thread**: *"Rheinmetall Q2 profit beats forecasts as revenue jumps"* [18 articles / 3 outlets] ·
  **BUILDING 3 days, 2→2→3** — precursor form.
- **Direction (body-read, headline tier)**: a **beat on revenue growth**, not a backlog statement; the
  European rearmament cycle is converting to printed profit. ⚠ **Rheinmetall is not US-listed and is
  outside `us_top300` — it is read as a cross-check on the US primes, never as a candidate.**
- **Exposure** *(tags asof 2026-07-28)*:

| Ticker | Chain position | Flow tag | Crowding note |
|---|---|---|---|
| **RTX** | prime | **🟢가속 +0.88, OBV 매집, RS20 +16.7 / RS60 +21.1, `vol_surge` 1.38** | FINRA **−1.03 ✅ clean rise**; **held (cycle rank-3 epicenter)** |
| **LMT** | prime | **🟢가속 +0.75, `new_green`, `vol_surge` 1.33** | FINRA **−1.86 ✅ clean rise** |
| **GD** | prime | **🟡중립 +0.76, OBV 매집, RS20 +13.0 / RS60 +11.1, `vol_surge` 1.16** | ⚠ **printed this morning and no bracket exists** — dropped at 07-28 as "neither branch changes a conclusion" |
| **NOC** | prime | **🟡중립 +0.59, RS20 +10.7 / RS60 −8.3** | W4 closed from its own 10-K (M179) |
| **LHX** | prime | **🟡중립 +0.50, RS20 +5.5 / RS60 −7.9** | ledger row `A.flow미도착`, recheck **08-12** |

- ★ **W5, stated because the label hides it**: RS60 inside "defense" spans **RTX +21.1 to NOC −8.3 =
  29.4pp**, and only **2 of 5** clear the 🟢 gate. **A single defense verdict is a verdict across a
  29pp range.**
- **Future — both branches, dated:**
  **IF** the thread keeps building **and** flow stays 🟢 — **≥3 of {RTX, LMT, GD, NOC, LHX} carrying
  🟢 with `vol_surge` ≥1.2 by 2026-08-12** — the rearmament cycle is broadening past the two names and
  the desk's rank-3 cycle (missile-defense, 7.54% exposure, **no floor set**) needs a floor.
  **Track KPI: that count (today 2 of 5).** Horizon **2026-08-12**.
  **ELSE (kill condition)**: the count stays ≤2 **and** LHX/NOC RS60 stay negative ⇒ it is a two-name
  trade wearing a sector label (W5) and the ledger rows stand.
- **Cell**: **CONFIRMED-EARLY** on **RTX and LMT only** (BUILDING × 🟢 with volume-path confirmation
  and clean FINRA reads). → **BET §B may read RTX/LMT as fresh candidates. GD/NOC/LHX are
  STORY-ONLY and must not leak into the hand-off.**

---

## CARD 8 — The dollar built into the Fed, and it is the leg under a tilt that owes a re-argument

- **Thread**: *"Dollar holds steady as Fed decision looms"* · **BUILDING 4 days, 2→2→4→6 outlets,
  43 articles** (07-28: *"Euro revisits monthly low against US Dollar in countdown [to the Fed]"*).
- **Direction (body-read, headline tier)**: **a rate-differential trade, not a risk trade** —
  *"The dollar's rally matters — but it still won't help Fed's…"* [3 outlets]; the euro leg is at a
  monthly low ahead of the decision; the **REIGNITED ECB thread reads *"ECB Tracker Detects No Pickup
  in Eurozone Wage Pressures"*** [3/3], i.e. the other side of the differential is softening.
- ★ **Why this card exists at all**: **DTWEXBGS was S12's entire frozen observable**, and it is
  **the only stated leg under the Materials UW** — the one tilt MACRO says is now overdue a
  re-argument (S36). **And the desk has no FX bucket, so this thread landed nowhere (new dig D98).**
- **Exposure** *(tags asof 2026-07-28)*:

| Ticker | Chain position | Flow tag | Crowding note |
|---|---|---|---|
| **NUE** | US steel — the domestic-price beneficiary of a strong dollar? **no, the opposite** | **🟡중립 +0.68, OBV 매집, RS20 +16.2 / RS60 +14.8, `vol_surge` 1.02** | ★ **blocked from 🟢 by the volume gate alone** |
| **STLD** | ditto | **🟡중립 +0.66, OBV 매집, RS20 +10.9 / RS60 +10.5, `vol_surge` 1.00** | ditto |
| **FCX** | copper — **98th COT percentile, crowded long** | **🟡중립 −0.18, OBV 분산, RS20 +0.1** | ⚠ COT contrarian is in the **REJECTED** ledger (D6): context only |
| **ADM · KO · CCEP** | dollar-sensitive Staples | all **🟡중립**, OBV 매집, `vol_surge` 0.97–1.00 | **XLP was the 3rd-best 5-day sector** and produced **0 🟢 of 19** |

- **Future — both branches, dated:**
  **IF** the thread keeps building **and** DTWEXBGS closes **above 121.41** (its 120-day maximum) by
  **2026-08-12** — the dollar leg under the Materials UW is intact and the UW's re-argument can rest
  on it. **Track KPI: DTWEXBGS (last 120.71, asof 07-24) — ⚠ a ~5-business-day publication lag,
  measured (D46).** Horizon **2026-08-12**.
  **ELSE (kill condition)**: DTWEXBGS closes **below 117.44** ⇒ the leg is gone and **the Materials UW
  has no stated leg left** — which is what S36 is measuring from the other side.
- **Cell**: **STORY-ONLY** (BUILDING × 🟡 across every exposure name). → **watchlist; hand the
  DTWEXBGS lag caveat to ROTATION, which owns the Materials re-argument.**

---

## 9 · Book cross-check — ENDED threads under open positions

`CYCLE_EXPOSURE.json` (live read-only KIS book): held epicenter names are
**AVGO · NVDA · TSM** (AI-compute), **MPC · PSX · XOM** (Energy), **RTX** (missile-defense);
adjacent **LNG**; book ≈ **62.6% cash**.

| Held cycle | Its thread | Status | Flag |
|---|---|---|---|
| AI-compute | *SK hynix / memory sell-off* | **BUILDING** | no flag — **but the thread is building AGAINST the holding.** AVGO 🟡 −0.07 (RS60 −11.8) · NVDA 🟡 +0.14 (RS60 −4.4). ⚠ **P11: NVDA's CDS is quoted ~78bp, 1.47× the IG index** |
| Energy | *Oil / Iran re-escalation* | **FADING** (not ENDED) | **flagged, not escalated** (Card 6). It produced today's #1 market event at 15 outlets |
| Missile-defense | *European rearmament* | **BUILDING** | no flag — RTX is 🟢 with a clean FINRA read (Card 7) |

**ZERO ENDED threads sit under an open position this run.** Stated with its denominator: 152 alive
threads were classified; the ENDED set was checked against the three held cycles and is empty.

---

## 10 · Hand-off

- **CONFIRMED-EARLY → BET §B**: **RTX · LMT** (Card 7) — and nothing else. Two names.
- **STORY-ONLY → watchlist, each with a dated re-check**: Cards 1, 2, 4, 5, 8 → **2026-08-05 /
  2026-08-12** as stated per card.
- **LATE-MONEY → valuation-gate note**: Card 6 (Energy). **The gate cannot be run on VLO — its margin
  percentile is a structural blank for a 5th run (D56) — so no cheapness claim is made anywhere.**
- **DEAD → drop**: **none.** ⚠ **Zero rejections filed this stage**, and that is deliberate: no thread
  cleared the two-axis test (FADING/ENDED **×** 🔴 dispersing). The memory complex is 🔴 but its
  narrative is **BUILDING**, so it is not DEAD — it is a short-side story, and the names carry live
  §3a theses with dated kills.
- **→ ROTATION**: Cards 4 (P6's product-ban leg → Industrials/Utilities), 6 (Energy cross-evidence),
  8 (the Materials re-argument's FX leg).
- **→ PREMORTEM**, two construction defects found before their events:
  **(i) Card 2** — *a capex guide is not a capex measurement when a gigawatt arrives as a lease*
  (S13/S16/S24's shared observable); **(ii) SWEEP §4** — *S36's "green count still 0" leg can settle
  on the volume gate rather than on Materials* (L3-bis family).

## ✅ EXIT CHECK

- [x] Scope market-correct: **`--scope foreign` on every call.** No card cites a domestic-feed item;
      the KR-market facts in Card 3 are quoted as **KR** evidence and are not used as US observables (W1).
- [x] Selection logged: **152 alive → 8 selected, 144 not selected, counted** (§0). No silent cap.
- [x] **Every card carries a direction body-read with the quoted evidence line.** Card 1's body-read
      **contradicts its own headline layer** and that is stated; Card 4's body-read found the
      tradeable half (inverters) that the headline omits.
- [x] Every exposure name carries a flow tag **with its asof (2026-07-28)**; the three names with no
      instrument (**ENPH · SEDG · FSLR**) are marked `[unavailable]` rather than substituted.
      **STORY-ONLY names did not leak into the hand-off** — only RTX and LMT go to BET.
- [x] Every card has **both branches + a kill condition + a dated horizon**.
- [x] `EVENT_ALPHA.md` written; CONFIRMED-EARLY handed to ROTATION/BET; **ENDED-thread book flags
      emitted (empty set, stated with its denominator)**; handoff ledger updated at run end per
      `pipeline/handoff.md`.
