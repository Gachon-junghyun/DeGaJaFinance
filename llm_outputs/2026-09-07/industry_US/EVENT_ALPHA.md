# EVENT_ALPHA — industry_US · 2026-09-07 (Mon, US Labor Day) · Stage 5 / L1·EVENT_ALPHA

> Bottom-up complement to MACRO's top-down matrix. **Scope `--scope foreign` on every call** — no
> KR-feed input anywhere in this file. **P4: no sizing, no buy/sell language.**
> ⚠ **Every flow tag below is `asof` 2026-09-04** (third consecutive run on the same settled session).
> ⚠ **The sweep's news axis is dead (17.39%)** — every narrative reading here comes from **direct**
> `module_news_data` calls, never from `SECTOR_FLOW_US.json`'s velocity column.

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: **4,254 daily events → 3,314 threads → 505 multi-day → 99 alive**
(2,809 one-day, of which 177 new today). Per-day event denominators
**09-01 858 · 09-02 944 · 09-03 879 · 09-04 732 · 09-05 291 · 09-06 271 · 09-07 279** — the last
three days run at **~1/3** the weekday rate (weekend + US holiday), so **every 🔴FADING tag whose
curve crosses that boundary is partly arithmetic** and is re-read on weekday legs only (`M1367`).

**Selected: 8 of 99. Not selected: 91** — the largest excluded groups being India IPO/market threads
(no US exposure vehicle), UK/EU domestic politics, crypto-price threads with no equity chain, and
sports/consumer clusters. **Counted, not dropped silently.**

⚠ **Precursor-form pass ran first** (curve starting ≤2 outlets and climbing). **Two qualified**:
the `$40tn US debt` thread (3→3→5) and the `China bank recapitalisation` thread (3→7). Both are
carried below. No 2-outlet climber with a US equity chain was set aside.

---

## Card 1 — ★★★ The ECB hikes on **Thursday 2026-09-10**, and this desk's calendar does not carry it

| | |
|---|---|
| **Thread** | REIGNITED · 5 days · outlets **4→6→2→9→5** · 61 articles · window denominator 4,254 events / 3,314 threads |
| | 09-01 *"Euro area: Inflation jump supports ECB hike – Commerzbank"* [4] → 09-02 *"Euro: ECB guidance may trigger asymmetric downside risks"* [6] → 09-03 *"ECB succession and data support resilience – BNY"* [2] → 09-04 *"**Fed Rate Hike Impact on Markets and Bonds**"* [9] → 09-07 *"European markets edge lower, **ECB decision in focus**"* [5] |
| **Direction (BODY-READ, not headline)** | `[news — economictimes/Reuters, 2026-09-07, body read in full]`: *"The European Central Bank **is widely expected to raise interest rates on Thursday**"*; *"Markets have **fully priced in a 25-basis-point increase, which would take the deposit rate to 2.5%**"*; eurozone inflation **back above 3% in August**, *"largely because of higher energy costs"*; European natural gas prices at their **highest since early 2023**. ⇒ **the hike itself is not the event — the GUIDANCE is**, and the driver named in the body is **energy**, not wages or growth |
| **Exposure (US-listed, one hop past the headline)** | This is a **rates** card, not a name card. The transmissible object is **US duration**: `DGS10` **4.77 = 98.8th pctile** · `DGS30` **5.25 = 96.0th** · `DGS2` 5-session **+14 bp = 92.1st** (all `[FRED]`, asof 09-03). Book-relevant sector baskets, `asof 2026-09-04`: **Real Estate** `eqflow` −0.124, `exc5` **1/12 positive** · **Utilities** `eqflow` +0.050 with `exc5` 7/15 · **Financials** `eqflow` −0.023, `exc20` **+1.92/+1.04** |
| **Crowding note** | 🚨 **UST 10Y specs are crowded-SHORT at the 9th percentile and added 70,300 to the short in the week** `[COT 09-01]` — i.e. **the market is already positioned for this**, which is the opposite of an un-chased move. ⚠ COT is **6 days stale** and pre-dates everything in §B |
| **Future — IF the thread keeps building** | ECB hikes 09-10 **with hawkish guidance** ⇒ the global long end takes a second leg; **US Aug CPI 09-11 lands into it**; **track KPI**: `DGS30` holds ≥ 5.25 and `bond selloff` `theme-age` holds ≥ 2×. **Horizon 2026-09-11.** |
| **ELSE — kill condition** | ECB hikes and **signals a pause**, or `DGS30` closes below **5.05** by 09-11 ⇒ the card is dead and the duration read reverts to a Fed-only story. **Also killed if `hy_oas` ≥ 3.10% on a close** — then it is a credit event, not a rates event |
| **Cell** | **CONFIRMED-EARLY (rates, not equity)** — narrative building **and** the money axis (COT + yields at 1-year extremes) already moving |
| **Hand-off** | 🚨🚨 **TO PREMORTEM, MANDATORY.** `catalyst_calendar --days 10` lists **PPI 09-10 · CPI 09-11 · FOMC 09-16** and **nothing else** — **the ECB decision on 09-10 is a dated, ≤72h, fully-priced-direction binary that the desk's calendar does not contain.** A one-way tilt into it is a protocol violation. Registered as **`D562`** (the US instance of the `D391`/`D510` structural-calendar gap: the tool carries no foreign central-bank dates) |

---

## Card 2 — ★★★ The yen is strong because Tokyo is **selling US Treasuries**, and that inverts the desk's own mechanism

| | |
|---|---|
| **Thread** | REIGNITED · outlets **2→6** today, plus three siblings: **5→6→7→3** (yen/BoJ rate bets), **3→2** (Commerzbank JPY), **2→2** (JPY near August highs) |
| **Direction (BODY-READ — and it CONTRADICTS the carry-unwind framing)** | `[news — CNBC, 2026-09-07, body read in full]`: Japan's foreign reserves fell **6.18% in August to $1.207tn** (from $1.287tn), *"their fastest pace since ministry records started in 2000"*, **4th straight monthly decline**. MoF official via Kyodo: the drop is *"due to **interventions** aimed at propping up the yen **and a decline in the value of government bonds**, following a jump in yields."* State Street's Masahiko Loo: *"the decline is primarily the result of Japan's recent **dollar-selling, yen-buying FX interventions**."* Cumulative 2026 intervention **¥27.1tn — the largest yearly amount ever**, beating ¥20.4tn (2003); the end-July round was **the first coordinated JP–US yen intervention since 1998** (the US sold euros to support the yen). Yen: **40-year low 163.98 on 07-23 → 155.98 now.** And `[seekingalpha 09-07]`: *"**Japan likely sold a portion of its U.S. Treasury holdings to finance its currency intervention**."* |
| **★ Why this is a correction, not a confirmation** | This stage's own MACRO section registered **`P143`** two hours ago with the mechanism written as *"a BoJ hike → carry unwind → US duration."* **The body read says the transmission actually running this month is intervention-funded UST SELLING — a SUPPLY channel, which operates whether or not the BoJ hikes.** `P143`'s **observable and thresholds are unchanged** (`D242`); its **stated mechanism is corrected here** and the original sentence is left standing in `MACRO_REPORT §D` rather than edited (`D48`) |
| **Exposure** | Again a **rates** object, and it is the missing supply-side explanation for Card 1: `DGS30` **5.25 = 96.0th pctile**, `DGS10` **98.8th**, `bond selloff` `theme-age` **5.93× — the highest acceleration this desk has ever recorded on a foreign measurement** (⚠ base **247**, ~2.4 articles/day, stated). Instrument: **`FXY`**, 5-session **+2.48% = 94.8th pctile** (settled 09-04) |
| **Crowding note** | The same 9th-percentile crowded-short UST positioning as Card 1 — **one crowd, two stories.** ⚠ `FXY` is **not** in `us_top300`, so it carries **no** flow/OBV/RS/short tag from this desk's instruments; it is a price series only |
| **Future — IF it keeps building** | Further intervention or a September BoJ move ⇒ **continued UST supply from the largest foreign holder** while specs are already max-short. **Track KPI**: `FXY` 5-session change stays ≥ **+0.704%** (p85) **and** `DGS30` does not close below 5.05. **Horizon 2026-09-14** (`P143`'s settle) |
| **ELSE — kill condition** | `FXY` 5-session ≤ **−1.062%** (p15) ⇒ the intervention was the move, not a policy turn, and the channel closes. **Also killed by an announced fresh MoF/BoJ intervention inside the window** — then the observable measures policy, not positioning (this is `P143`'s registered anti-signal) |
| **Cell** | **CONFIRMED-EARLY** — building narrative **and** a measured money mechanism (¥27.1tn of actual flow), with an instrument at the 94.8th percentile |
| **Hand-off** | To ROTATION as the **second, non-Fed driver** behind the Real Estate / Utilities / Financials duration cluster. To PREMORTEM: **this is the "what if the duration move is not about the Fed at all" branch**, and no existing row contains it except `P143`, registered today |

---

## Card 3 — ★★★ The refining thesis has a **hard supply-destruction number** the desk has never carried

| | |
|---|---|
| **Thread** | New today · 4 outlets · *"Shipping Fuel Shortage Looms as Refiners Prioritize Diesel"*; siblings `diesel` +3.9% and `refinery` +4.7% raw over 7 days (5th and 8th of 18 terms) |
| **Direction (BODY-READ)** | `[news — yahoo_finance/oilprice, Reuters-sourced, 2026-09-07, body read in full]`: ★★ *"per the **International Energy Agency**, as much as **a fifth of that refining capacity, totaling some 9.6 million barrels daily, has been knocked out by hostilities**"* in the Middle East · Ukrainian drone attacks hit Russian diesel output *"to the extent that the country **imposed a ban on diesel exports**"* · *"**Refinery margins are running at record highs across the world**"* · bunker-fuel shortage **218,000 b/d this quarter** (Energy Aspects) vs **6,000 b/d** in the 2025 episode — a **36×** step · *"**Record-low gasoline and diesel inventories** will incentivise refiners globally to maximise secondary unit runs"* |
| **Why it matters to a live row** | 🚨 **This is direct evidence on `P140`, which settles 2026-09-11.** `P140` asks whether to read the crack's **LEVEL** (95.6th pctile) or its **RATE** (3-session −$7.02/bbl = 6.0th pctile). **The fundamentals read supports branch B (the level reasserts): 9.6 mb/d of destroyed capacity and a Russian export ban are not three-session phenomena.** The tape supports branch A. **This is recorded as evidence, NOT as a score** (`D242`) — the row settles on the price observable and nothing here changes its thresholds |
| **Exposure** (`asof 2026-09-04`) | **`MPC`** flow +0.694 · OBV **+0.621 매집 (board-leading)** · rs20 **+30.8** · surge 1.05 → 🟡 · **held** · **`PSX`** +0.750 · OBV +0.434 · rs20 +25.5 · surge 1.15 → 🟡 · **held** · **`VLO`** +0.700 · OBV +0.482 · rs20 +24.7 · surge 1.06 → 🟡 · not held. **All three are 🟡, not 🟢, and §SWEEP_READ §3 shows why: they miss the `vol_surge` gate by 0.05–0.15 while a rank-34 name with flow +0.231 passes it on a dead axis.** Their absence from `US_LIVE_SHORTLIST.json` is a **filter artifact, not evidence** |
| **Crowding note** | `[FINRA 09-04]` `MPC` carries **the sheet's largest 5v5 short build (+8.9)** at an unremarkable z (+0.43) — carried from 09-06 unchanged. ⚠ **Chart instrument disagreement is live**: `PSX` shows a **bearish RSI divergence** that `MPC` does not (`M1373` class, `C25`) |
| **Future — IF it keeps building** | Q4 fuel-oil shortage confirmed and the Russian ban persists ⇒ the crack's level holds and `P140` settles **B**. **Track KPI**: `refining margin` `theme-age` leaves its 5-run decline (currently **0.68×**, age 81) — this is the falsifier the narrative axis owes, because **the fundamentals and the narrative instrument currently point opposite ways** |
| **ELSE — kill condition** | The distillate crack's **5-session** change reaches `P140`'s branch A line (**≤ −4.209 $/bbl**) at the 09-11 close, or an **IEA/EIA revision** cuts the 9.6 mb/d outage figure materially ⇒ the supply-destruction premise is wrong and the level-based carry loses its basis |
| **Cell** | **CONFIRMED-EARLY on fundamentals · CONTESTED on the tape** — the honest cell, because the money axis (OBV accumulation, rs20 +25 to +31) confirms while the *rate* of the driver does not |
| **Hand-off** | To ROTATION (Energy OW's mechanism, restated as **supply destruction**, not war premium). To BET §B: **`VLO` is the un-held leg of a three-name node whose other two are held** — flagged as a composition observation, **not** a recommendation |

---

## Card 4 — ★★★ Hormuz LNG: **QatarEnergy force majeure extended into November**, and the desk owns **zero** measurable exposure

| | |
|---|---|
| **Thread** | REIGNITED · outlets **5→3→2→3→2** · *"Asia Spot LNG Prices Hit 5-Month High as Hormuz Blockage Drags On"* → *"Asian LNG Prices Surge to Highest Since 2022"* → today *"European Gas Climbs on LNG Supply Concerns Ahead of Winter"* [3] |
| **Direction (BODY-READ)** | `[news — oilprice/Bloomberg, 09-01 and 09-03, both bodies read]`: Asia spot LNG **$23.388 (08-28) → $24.614 (09-01) → $25.908/mmBtu (09-02)**, *"a 5% weekly gain"*, **the highest since 2022** · ★ *"**QatarEnergy extended the force majeure on its LNG deliveries into November** amid still-blocked transits through the Strait of Hormuz"* · buyers in **South Korea, India, Taiwan, Bangladesh** tendering for **Oct/Nov** spot cargoes · **Pakistan rejected a BP cargo priced above $27/mmBtu** — i.e. the price is high enough to destroy demand · Trump, quoted: *"We took out all of the new equipment that they tried to build along the Strait of Hormuz... we're prepared to do another one any time we want."* |
| 🚨🚨 **Exposure — and this is the card's real finding** | **The entire US LNG export chain is ABSENT from `data/us_universe/us_top300.csv`.** Checked by name: **`LNG` (Cheniere) · `CQP` · `NFE` · `GLNG` · `FLNG` · `VG` — none in universe.** Gas E&P: **`EQT` · `EXE` · `AR` · `RRC` · `CTRA` — none in universe.** Tankers: **`FRO` · `STNG` · `DHT` · `INSW` · `TNK` · `TDW` — none in universe.** What IS measurable is one hop away and diluted: `WMB` +0.769 🟢 (surge 1.39, OBV +0.151, rs20 **+5.7**) · `OKE` +0.689 🟡 · `TRGP` +0.442 🟡 · `KMI` +0.174 🟡 — **US midstream, which moves domestic gas and does not price Asian spot LNG** |
| **Why this is the SWEEP stage's own invariant, reproduced** | The stage's field note records that the book once held **`TSM` and `LNG`** and *"neither was in the sweep universe… logged for 9 consecutive runs without connecting it to the universe file."* **`LNG` is still not in the universe, 54 days after the last build.** ⇒ on the day the desk's own body-read confirms a force majeure into November and a 2022-high price, **the desk cannot produce a flow, OBV, RS or short reading for a single direct beneficiary.** Registered as **`D563`**: *the universe is built from index membership plus current holdings, so a cycle the desk does not yet own is a cycle it cannot measure — the exposure gap and the measurement gap are the same gap.* |
| **Crowding note** | **Not assessable.** No FINRA short-z, no COT, no OBV for any direct name. ⚠ **Stated as unmeasured, not as neutral** |
| **Future — IF it keeps building** | Force majeure runs into November as stated and European gas holds its 2023 high into winter. **Track KPI**: `LNG` `theme-age` (today ⚪ECHO **1.24×**, base 1,832) leaves ECHO, **and** the universe is rebuilt so the chain becomes measurable. **Horizon 2026-09-14** |
| **ELSE — kill condition** | QatarEnergy **lifts** the force majeure, **or** Asia spot LNG closes below **$20/mmBtu**, **or** a Hormuz-reopening statement fires (the undated binary `catalyst_calendar` already carries as `[news👁]`) ⇒ the card dies with the blockade |
| **Cell** | 🚨 **STORY-ONLY — BY INSTRUMENT DEFECT, NOT BY EVIDENCE.** The money axis was not tested and could not be. **This is the distinction the stage's own rule demands: an absence must be diagnosed before it is cited** |
| **Hand-off** | **NOT handed to BET as a candidate** — a STORY-ONLY name may not leak into the candidate list, and there is no measurable name to leak. Handed to **ALPHA/PREMORTEM as an instrument action**: rebuild `data/us_universe/` with an explicit LNG/gas/tanker include-list (**P5 — human approval; this stage does not rebuild the universe**). Filed to the **missed** ledger as a *thread that cleared the narrative axis and could not be tested on the money axis* |

---

## Card 5 — ★★ Venezuela: the body read **kills one leg** of a live row's basket

| | |
|---|---|
| **Thread** | Tagged 🔴FADING · **22→19→14→21→13→9→13** · ⚠ **the tag is not supported**: today's **13 exceeds yesterday's 9 on a smaller denominator** (279 vs 271 events). Read on weekday legs the thread is **flat-to-firm**, not fading. `theme-age` **2.47×** 🟡ACCELERATING (down from **2.95×** on 09-06); raw 7-day count **461, −5.3%** |
| **Direction (BODY-READ — and it contradicts a carried framing)** | `[news — yahoo_finance/Motley Fool, 2026-09-06, body read]`: **`CVX` "just signed a landmark deal"** positioning it to **double output over five years**; CEO Wirth: *"You have to hang in there until all the conditions come together."* ★★ **`XOM` and `COP` both LEFT in 2007** after nationalisation and are *"far behind"*; **`XOM`'s own CEO Darren Woods called Venezuela "uninvestable" this past January**, and the only counter is that *"President Trump recently said that Exxon would be going back."* `COP` holds a **$12bn arbitration award** it has been trying to recover for years |
| **Why it matters to a live row** | 🚨 **`P139` (registered 09-06, settles 2026-09-14) has branch A as `EW{XOM, CVX, SLB}` — the "Venezuela is paid upstream" leg.** The body read says **`XOM` is not an operational Venezuela beneficiary in any dated sense**; its inclusion rests on a **presidential remark**, against its own CEO's on-record "uninvestable". ⇒ **construction note recorded on a live row; thresholds and basket UNCHANGED** (`D242`). It also **resolves the standing `XOM` story-vs-tape contradiction in favour of the tape**: `XOM` is **dead last of 16** in Energy on flow (**+0.027**, OBV −0.071 중립, rs60 −0.3) *while carrying a velocity* (rank 19, inside the news wall) — so that weakness is **measured, not filtered** |
| **Exposure** (`asof 2026-09-04`) | **`CVX`** flow +0.661 · OBV **+0.371 매집** · rs20 +12.2 → tagged 🟢 ⚠ **but its 🟢 is a `D561` artifact** (surge **0.99**, below the gate; it passes only because rank 35 gives it a velocity) ⇒ **the tag is not citable; the underlying axes are** · **`XOM`** +0.027 🟡 · **`COP`** +0.639 · OBV +0.222 매집 · rs20 **+14.6** · surge 0.95 → 🟡 (filtered out of the shortlist, not absent from the tape) · **`SLB`** +0.883 · OBV **+0.439** · rs20 +14.2 · surge 1.39 → 🟢 · `[FINRA]` z **−1.21 = ✅ low-short/short-cover** |
| **Future — IF it keeps building** | The deal executes and the upstream/services leg is paid ⇒ `P139` settles **A** (≥ +2.719). **Track KPI**: `heavy crude` leaves ⚪ECHO **and** `XOM`'s flow turns positive — the second is the harder test and it is the one that discriminates |
| **ELSE — kill condition** | `P139`'s own anti-signal: a **reversal or suspension of the US–Venezuela arrangement**, a sanctions action re-closing it, or announced M&A among the six names, inside 09-08 → 09-14 |
| **Cell** | **LATE-MONEY on `CVX`** (deal signed, price has moved, rs20 +12.2) · **CONFIRMED-EARLY on `COP`/`SLB`** (accumulating with clean short profile, still 🟡/unfiltered) · **DEAD on `XOM` as a Venezuela story** — ⚠ **and "DEAD" here is a MONEY verdict AND a story verdict simultaneously**, which is the only case where the drop is unambiguous |
| **Hand-off** | To BET §B: `SLB` and `COP` as CONFIRMED-EARLY. `XOM` **re-filed rather than dropped** — its thesis line is rewritten from *"named Venezuela beneficiary"* to *"an integrated with the sector's worst flow and no operational Venezuela leg"*, with a **dated re-check at `P139`'s settle, 2026-09-14** |

---

## Card 6 — ★★ The $40tn / $1.25tn thread: a **fiscal** duration driver with no bracket anywhere on this desk

| | |
|---|---|
| **Thread** | 🟢 **BUILDING** · 3 days · outlets **3→3→5** · 15 articles · **precursor-form: qualified on the ≤2-outlet-and-climbing pass** |
| | 09-03 *"Stanley Druckenmiller Says the 30-Year Treasury Bond Is…"* [3] → 09-06 *"The U.S. National Debt Just Surpassed **$40 Trillion**"* [3] → 09-07 *"'**Uncharted territory**': The $40 trillion U.S. national debt just got uglier as **interest payments rise to $1.25 trillion a year**"* — Fortune [5] |
| **Direction (headline-level + one corroborating body)** | ⚠ **Body read is PARTIAL and that is stated**: the Fortune piece was reached by title and its body was not retrieved in this stage's window. Corroborating body from Card 1's pull: *"attention is shifting to… **the impact of rising global bond yields**."* A sibling body in the same alive set — *"Amazon, Meta Are Now Serious Competition to Uncle Sam: **Big Tech's AI Debt Boom 'Driving' Treasury Yields Higher**"* [4 outlets] — supplies a **second, independent supply channel** into the same object |
| **★ The convergence worth naming** | **Three independent supply stories now point at the same instrument**: (1) Japan selling USTs to fund intervention (Card 2), (2) $40tn debt / $1.25tn interest (this card), (3) hyperscaler AI debt issuance crowding Treasuries. **All three are SUPPLY. None of them is the Fed.** The desk's entire duration exposure (`RE` UW−, `UTIL` N−, `STPL` UW, `FIN` N) has been argued on a **Fed/policy-path** frame (`P121`) for weeks |
| **Exposure** | `DGS30` **5.25 = 96.0th pctile** · the 2s10s at **+0.43 = 17.5th pctile** (a *flat* curve, i.e. the move is not a classic bear-steepener yet). Equity legs are the same three UW buckets |
| **Crowding note** | Same 9th-percentile crowded-short UST specs. ⚠ Also the only bearish-side reading that is NOT crowded: `hy_oas` **2.0th pctile** and `VIXCLS` **2.4th** say **credit and vol have not priced any of this** |
| **Future — IF it keeps building** | Long-end supply narrative persists through the 09-10 ECB and 09-11 CPI. **Track KPI**: `bond selloff` `theme-age` holds ≥ 2× **and** `DGS30` ≥ 5.25 at the 09-11 close. **Horizon 2026-09-11** |
| **ELSE — kill condition** | `DGS30` closes below **5.05**, **or** the thread falls back to ≤2 outlets for two consecutive weekdays ⇒ it was a round-number story ($40tn), not a supply story |
| **Cell** | **STORY-ONLY, provisionally** — the narrative is building but the **only** money confirmation is a yield level that three other cards also claim. ⚠ **A round-number milestone is exactly the kind of thread that builds on arithmetic rather than news**, and that is stated rather than resolved |
| **Hand-off** | To PREMORTEM as a **lens**, not a card: *"the duration bet is a SUPPLY bet the desk has been arguing as a POLICY bet."* Filed to the **missed** ledger with `--enters-if` **`DGS30` ≥ 5.40 on a close** |

---

## Card 7 — ★★ `NVDA`/Hugging Face: real fading, and it is `S130`'s driver

| | |
|---|---|
| **Thread** | 🔴 **FADING** · **4→28→9→2→2** · ★ **this one is NOT a weekend artifact**: the collapse from **28 → 9** happened **inside the weekday block (09-02 → 09-03)**, before the denominator fell |
| **Direction** | Headline-level only, and labelled as such: *"History Says What Nvidia's Last Big Acquisition Became. **Hugging Face Will Cost Nearly Twice as Much**"* [4 outlets today]. The tape's own reading: `NVDA` flow **−0.032**, OBV **−0.084 분산**, rs20 +3.3, rs60 +8.8, surge 1.01 → 🟡 (`asof 09-04`) |
| **Why it matters to a live row** | **`S130` settles 2026-09-10** on this event. **This is not a score** (`D242`) — it is the deceleration recorded at **D−3** rather than argued at scoring (`D450`) |
| **Future / ELSE** | IF the thread re-ignites above 8 outlets before 09-10 ⇒ the deal is contested and `S130`'s window carries real information. **ELSE** ⇒ the row settles on a decayed narrative and the verdict should be read with that stated |
| **Cell** | ⚠ **NOT DEAD.** The 2×2's DEAD cell requires **both** axes — FADING **and** 🔴 dispersing. `NVDA` is **🟡 with OBV −0.084**, which is 중립-to-분산, **not** a 🔴 verdict. ⇒ **re-filed, not dropped**: thesis line rewritten from *"an acquisition catalyst"* to *"an epicenter holding with a decayed catalyst and a flat tape"*, **dated re-check 2026-09-10** |
| **Hand-off** | To ROTATION (IT). **No drop, so no `reject_ledger` entry** — the rule is that DEAD is a money verdict, and the money verdict is not in |

---

## Card 8 — ★ China's €45bn bank/insurer recapitalisation — precursor-form, no clean US vehicle

| | |
|---|---|
| **Thread** | 🟢 **BUILDING** · 2 days · **3→7** · 13 articles · precursor-form (started at 3 outlets, climbing) |
| | 09-06 *"China to pump billions into state banks, insurers in cap…"* [3] → 09-07 *"**China injects over €45 billion** into state banks and insurers as growth slows"* [7], sub-event *"China insurer recapitalisation **may ease capital constraints and support stock investments**"* [2] |
| **Direction** | Headline + sub-event only; **no full body read** — stated. The sub-event's own framing is the transmissible claim: recapitalised insurers have **more balance-sheet room to buy equities** |
| **Exposure** | 🚨 **No clean US-listed vehicle in `us_top300`.** The honest map is second-order: US financials with China revenue exposure, none of which is separable on this desk's instruments. **`FXI`/`KWEB` are not in the universe** |
| **Future / ELSE** | IF it keeps building **and** a US-listed vehicle becomes identifiable ⇒ re-open. **ELSE** it stays a foreign-domestic policy story. **Dated re-check 2026-09-14** |
| **Cell** | **STORY-ONLY** — and, like Card 4, **story-only by instrument absence rather than by evidence**. Distinguished explicitly |
| **Hand-off** | **Not** handed to BET. Filed to the **missed** ledger (`M.숏리스트탈락`) with `--enters-if` *a US-listed vehicle enters the universe*, dated **2026-09-14** |

---

## 9 · Book cross-check — ENDED threads under open positions

| holding | thesis rides on | thread state | flag |
|---|---|---|---|
| `MPC` · `PSX` | distillate crack / refining margin | 🟢 **alive and materially strengthened today** (Card 3, IEA 9.6 mb/d) — ⚠ **but the narrative instrument disagrees**: `refining margin` `theme-age` **0.68×**, a **5th consecutive decelerating run** | ⚠ **flag: fundamentals and narrative axis point opposite ways.** Not an ENDED flag |
| `NVDA` · `ANET` · `AVGO` · `HPE` | AI-compute | Hugging Face thread 🔴 fading (Card 7); `data center` `theme-age` **0.97×**, `AI capex` raw **−1.0%** | ⚠ **flag: no thread is currently building under the book's largest theme.** `AVGO` is the weakest name on the tape (flow −0.356, OBV **−0.454 분산**, rs20 **−15.9**) — `S127` settles it **09-08** |
| `RTX` | missile-defense / rearmament | 🚨 **no thread at all.** The node printed a **7.1st-percentile 5-session extreme** with **zero** narrative carriage (`M1377`), and `cycle_registry.json` sets **no bar** for rank-3, so `CYCLE_EXPOSURE`'s GAP check is **silent on it by construction** | 🚨 **flag to the book desk: a held position whose cycle has neither a thread nor a registry bar.** `S150` settles it 09-14 |
| `ETN` | AI-power / electrical | no thread; flow **−0.662 🔴분산**, rs20 −8.0. ⚠ **500d/750d `risk_units` merge `ETN` with `ANET` into ONE unit** spanning two theme labels | ⚠ **flag: the book counts this as diversification and the measurement says it is one risk** |
| `MET` · `NDAQ` · `NUE` | insurers / exchanges / steel | no thread; all 🟡/🔴 | no flag beyond the tape |

---

## ✅ EXIT CHECK — EVENT_ALPHA

- [x] **Scope market-correct** — `--scope foreign` on every `brief`, `thread`, `fts` and `theme-age` call. No KR-feed input.
- [x] **Selection logged** — 99 alive → **8 selected**, **91 not selected**, with the excluded groups named. Precursor pass ran first and its 2 qualifiers are both carried.
- [x] **Direction body-read done on every card that carries one** — Cards 1, 2, 3, 4, 5 have full bodies quoted verbatim. **Cards 6, 7 and 8 are explicitly labelled headline-level / partial**, with the reason, rather than presented as body-read.
- [x] **Every exposure name carries a flow tag with its `asof`** (2026-09-04 throughout), and **two tags are explicitly declared non-citable** (`CVX`, `PG`) under `D561`. **Names absent from the universe are declared unmeasured, not neutral** (Cards 4, 8).
- [x] **STORY-ONLY names did not leak into the candidate hand-off** — Cards 4 and 8 are explicitly not handed to BET, and both were filed to the **missed** ledger with `--enters-if` conditions instead.
- [x] **Every card carries both branches, a kill condition and a dated horizon.**
- [x] **DEAD applied as a money verdict** — `NVDA` was **not** dropped despite a fading thread: its tag is 🟡 with `flow_score` −0.032, `rs20` +3.3, `rs60` +8.7 and `vol_surge` 1.01 alongside `obv_norm` −0.084, i.e. **not a 🔴 verdict on any axis** (**RULE D6 exempt — the verdict here rests on the composite `flow_score` and the RS/surge axes, not on OBV alone; OBV is quoted as one of four**); it was **re-filed** with a rewritten thesis line and a dated re-check. `XOM` is the one unambiguous DEAD (story **and** money) and is likewise **re-filed, not dropped**.
- [x] **ENDED-thread book flags emitted** (§9) — three flags, including a 🚨 on `RTX`.
- [x] **CONFIRMED-EARLY handed forward**: `SLB` · `COP` (Card 5), plus Cards 1–3 as sector-level cross-evidence for ROTATION. **`P143`'s mechanism corrected in the open** (Card 2), original left standing.
- [ ] Handoff ledger update — performed at run end per `pipeline/handoff.md` (this stage records what it hands over; the ledger write is the run-end step).

---

> P4 — analytical only. No sizing, no buy/sell language. "Held" marks a measurement subject, not a view.
