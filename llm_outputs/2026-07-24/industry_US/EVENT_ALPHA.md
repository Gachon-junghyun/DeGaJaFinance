# EVENT_ALPHA — industry_US — 2026-07-24 (Fri)

> Stage 4/10. The **bottom-up** complement to MACRO's top-down matrix: not "which sectors should
> benefit from my propositions", but **"which stories ARE building, and is money already following"**.
> Scope **`--scope foreign`** on every call (market-locked; a card citing the KR feed is void).
> Flow tags asof **2026-07-23 close** (`SECTOR_FLOW_US.json`); short-pressure z asof **2026-07-23**
> (`us_flow.py`, FINRA). Zero buy/sell — this stage never sizes.

---

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`, window **2026-07-18 → 2026-07-24**.
Per-day denominators: **187 · 221 · 701 · 948 · 812 · 840 · 350**.
Daily events **4,059 → 3,073 threads → 538 multi-day → 131 ALIVE** (2,535 one-day, 212 new today).

**131 alive → 8 selected → 123 not selected.** Selection rule applied in order: precursor-form first
(curve starting ≤2 outlets and climbing), then BUILDING/REIGNITED by peak, then FADING **only where
the book already holds exposure** (which admits the oil thread and nothing else).

⚠⚠ **The window ends on a partial day and this materially distorts the tags.** Today collected
**350 events against 840 yesterday** because the US session has not opened at run clock. The L3 states
that a low-volume window end **mechanically inflates FADING** — so **no card below treats a FADING tag
as attention rotation**, and two of the eight selected threads carry FADING tags that are read as
"unconfirmed today", not "over".

---

## Card 1 ★★ — "AI spending is eating free cash flow" · the branch the desk has bracketed but never seen narrated

- **Thread**: *"Analysis: AI investment boom puts Big Tech's free cash flow under pressure"* ·
  **REIGNITED 3→6→3** · plus four sibling threads all pointing the same way:
  *"Google's profits are outrunning its AI spending boom"* (peaked **16 outlets**, 2→4→12→16→14→2) ·
  *"Alphabet's cash burn raises alarm for Big Tech"* (5→2→6→3) · *"CapEx Is Exploding as Alphabet Goes
  On a Spending Spree"* (4→3) · *"Why Most AI Projects Will Fail"* [11 art / **8 outlets**, head tier].
  Window denominator: 350 events today / 131 alive threads.
- **Direction (body-read)**: the argument is **cash consumption, not demand doubt**. Chain-hop's own
  example line: *"Big tech's AI spending boom raises cash flow concerns despite early retur[ns]"* —
  i.e. the returns are conceded and the **funding cost** is the complaint. Corroborated on the term
  axis: **`free cash flow` 1.41× and `capex` 1.40× are the two fastest terms in the whole sweep
  (pool-normalized)** while **`capex cut` = 0 hits in 24 hours for a third consecutive measurement**.
- ★ **Why this card exists**: `STANDING_VIEW` **C6** logged that the margin-drag branch was
  **un-narrated**, and **S13** was registered because it *"cannot be anticipated from the news axis."*
  **It is now narrated — under different words.** The desk was measuring the wrong string.
- **Exposure** (spenders = the crowded, headline layer by construction; chain-hop's own headline table
  puts GOOGL at **210 title mentions**, TSLA 151, AMZN 45, MSFT 44):

| Ticker | Chain position | Flow tag (asof 07-23) | Crowding |
|---|---|---|---|
| GOOGL | headline layer — **the named subject** | **🔴분산**, flow −0.200, RS20 **−8.7** vs SPY | 210 title mentions = maximally crowded |
| MSFT | headline layer | 🟢가속, flow +0.499, RS20 +3.7 vs SPY, RS60 **−13.4** | 44 titles |
| META | headline layer | 🟢가속, flow +0.646, RS20 **+8.0** vs SPY, RS60 −13.9 | 18 titles |
| **STX** | ★ **one hop past the headline** — 0 title mentions, 5 body-proximate | 🟡중립, flow +0.156, RS20 −8.7, **RS60 +50.1** vs SPY, OBV **매집**, vol_surge 1.28 | **uncrowded by construction** |
| SPGI | one hop (0 titles, 5 proximate) — data/index toll on the capex debate itself | not in a 🟢 bucket | uncrowded |

- **Future — both branches, dated**:
  - **IF the thread keeps building AND the spender tags stay 🔴/🟡 through the 07-29 prints** →
    S13 branch A gets its second observation and **Info Tech's single label must split** (spenders
    de-rate on multiple, suppliers protected by the same raise). **Track KPI**: the
    supplier-minus-spender RS20-vs-SPY spread. **Horizon: 2026-08-12** (S13's registered 10 sessions).
  - **ELSE (kill condition)** → **`free cash flow` velocity falls back below 1.2× pool-normalized
    AND GOOGL's RS20 vs SPY turns positive by 2026-08-06.** That would make this a one-week
    post-earnings echo rather than a repricing.
- **Cell**: **STORY-ONLY on the spenders** (BUILDING × 🔴/mixed money) → watchlist, dated re-check
  **2026-08-06**. **STX is the only CONFIRMED-EARLY-shaped name here** (OBV accumulating, RS60 +50.1,
  vol_surge already >1.2) — **but its RS20 is −8.7**, so it fails the A-grade 20-day test and is
  handed on as **🟡 with the disagreement stated**, not as a candidate (P4).

---

## Card 2 ★★ — "The bond market flipped to a July rate HIKE" · the regime item no scenario brackets

- **Thread**: *"The Probability of a July Fed Rate Hike Has Tripled Over the Last Week"* ·
  **REIGNITED 4→7 outlets** [8 articles], with `└` *"Bond Market Just Flipped to 'Rate Hike in July'"*.
  Companion 4-day BUILDING thread: *"U.S. Investors Are Doing Something They've Never Done Before"* /
  *"The bond market is telling investors it's time to start…"* / *"Investors fear Japanese bond bets
  risk becoming new 'widowmaker'"* (5→6→2→6).
- **Direction (body-read, and it cuts against the headline's alarm)**: **CME FedWatch hike odds went
  10.7% (07-15) → 34.7% (07-22)**. But **TD Securities, on the record, calls the pricing excessive** —
  *"it would be the second-largest deviation between market pricing and actual Fed action in the past
  decade… we maintain a receive July OIS position"* — and names the driver as **oil, not core
  inflation**: *"pricing for rate hikes moved alongside oil."* Deutsche Bank corroborates the
  hawkish repricing while noting **equities rose anyway on a chip rebound**.
  ⇒ **The headline says "hike coming"; the bodies say "a hike is being priced, and at least one
  primary dealer is fading it."** Both go on the card.
- **Exposure** — this is a **rate-channel** card, so the exposure is sector-shaped rather than
  name-shaped, and the two legs that lose *together* are already registered as **S9**:

| Node | Chain position | Flow tag (asof 07-23) | Crowding |
|---|---|---|---|
| Utilities (DUK/NEE/CEG/VST) | bond-proxy, loses on higher real rates | **0🟢 of 15**, sector wflow −0.051; CEG RS60 **−15.8** vs SPY | not crowded, not bid |
| Digital-infra REITs (AMT/CCI/DLR/EQIX) | duration + AI-capex, loses on both | **all four 🔴분산**, negative on **both** RS20 and RS60 vs SPY | — |
| P&C insurers (TRV/CB) | front-book earner, **wins** on higher front-end | TRV 🟢가속 flow +0.917 (**FINRA z +2.21 = crowded-short**); CB 🟢 +0.81 | TRV crowded-short |
| Duration REITs (WELL/VTR) | ⚠ **bid despite the rate move** — R7's replicated anomaly | WELL 🟡 flow +0.511 RS20 **+10.9**; VTR 🟡 +0.500 RS20 **+12.4** (**FINRA z +1.83**) | VTR short-pressure spiking |

- **Future — both branches, dated**:
  - **IF the FOMC hikes on 2026-07-29, or holds with a hike explicitly on the table** → **P1 branch (b)
    fires**, the duration de-rate becomes a regime call, and **S9's own grid is revealed as incomplete
    because it brackets only 2.20%/2.55% on the real 10y**. Track KPI: **DGS2** and **CME hike odds**.
    Horizon: **2026-07-29**.
  - **ELSE (kill condition)** → the FOMC holds with dovish language and **DGS2 closes below 4.15%**;
    TD's fade was right and this was event positioning. Horizon: **2026-08-05**.
- **Cell**: **CONFIRMED-EARLY on the rate channel, but there is no clean single-name expression** —
  handed to **ROTATION as a sector-tilt input and to PREMORTEM as a mandatory both-sides bracket**,
  not to BET as a name.

---

## Card 3 — Oil through $100 / Red Sea blockade · the day's #1 event, and the book holds it

- **Thread**: *"Oil prices jump back above $100 per barrel"* · **FADING 5→6→17→18→12→29→11** (peak
  **29 outlets**) — ⚠ **the FADING tag lands on a 350-event partial day and is read as "unconfirmed
  today", not "over"** — alongside **REIGNITED** *"Oil price rises above $95"* (7→7) and today's #1
  head event *"Oil set for weekly rise amid Red Sea shipping attacks"* [**30 articles / 11 outlets**].
  Admitted despite the FADING tag **because the real book holds 11.33% Energy epicenter exposure**
  (`CYCLE_EXPOSURE.json`), which is the L2's stated exception.
- **Direction (body-read)**: escalation is **physical and continuing** — *Trump weighs "massive attack"
  on Iran* [10 art/9 outlets] · *US launches new strikes on Iran over shipping routes* [7/6] ·
  *Tanker Exits Red Sea Dark as Another China Ship Heads to Strait* [5/4] · *China Rushes to Buy East
  Russian Oil* [5/4]. Confirmed on the tape: **Brent settled 100.69, WTI 92.19, Brent−WTI +$8.50**
  (a coherent spread — **D30's artifact does not reproduce**).
  ★ **And the margin leg did NOT break**: settled 3-2-1 crack **66.49, −0.56%**, at the **89th
  percentile of 90 days** (MACRO §D-P4 / retraction **R17**).
- **Exposure**:

| Ticker | Chain position | Flow tag (asof 07-23) | Short-pressure (FINRA z, 07-23) |
|---|---|---|---|
| **XOM** | crude/integrated — headline layer | **🟢가속**, flow +0.696, RS20 **+13.9** vs SPY, **RS60 only +2.7** | **z +3.13 — the board's extreme, second consecutive run** |
| **MPC** | refining margin | 🟡중립 (blocked by vol_surge 0.91), flow +0.617, RS20 **+26.0**, RS60 **+34.2** vs SPY, OBV 매집 | ★ **z −3.29 = the strongest short-covering reading on the board** |
| **VLO** | refining margin — prints **2026-07-30** | 🟡, flow +0.594, RS20 +25.2, RS60 +24.9 vs SPY, OBV 매집 | z +0.38 normal |
| **PSX** | refining margin | 🟡, flow +0.667, RS20 +22.1, RS60 +22.9 vs SPY, OBV 매집 | z −0.33 normal |
| STNG/FRO/INSW | ★ the blockade's **literal** beneficiaries — prints 07-30 (STNG) | **`A.flow미도착` on the reject ledger since 07-23**, recheck 2026-08-06 | — |

- ★ **The measured tension this card exists to state**: **crude carries the 🟢 and the crowded short;
  refining carries the momentum.** XOM's RS60 is **+2.7** vs SPY against MPC's **+34.2** — on the
  desk's only A-grade axis the refining leg has led by ~31pp over 60 days while MACRO §E wrote the OW
  onto the crude leg from a single session. **SWEEP §2b said the same thing independently.**
- **Future — both branches, dated**:
  - **IF Red Sea escalation persists AND the settled crack holds ≥65** → the refining margin is real
    rather than war premium, which is **S8 branch C**, and VLO's **2026-07-30** print is the read-through.
    Track KPI: **settled 3-2-1 crack** (settled closes only — this is now a rule after R17).
    Horizon: **2026-07-30**.
  - **ELSE (kill condition)** → a Hormuz "open" statement (**S8**, undated `[blank]` — not guessed),
    **or** the settled crack closing **below 60** while WTI holds above $90. Either kills the margin leg.
- **Cell**: **CONFIRMED-EARLY on refining** (BUILDING/REIGNITED narrative × OBV-accumulating money
  with the best RS in the sector) → **BET §B candidate**. **LATE-MONEY caution on XOM**: it is the
  crowded, headline-layer, extreme-short-z name whose own 60-day relative strength is ~flat.

---

## Card 4 ★ — "Chipmaking equipment rises on Intel's capex bump" · S6's transmission, named in a headline

- **Thread**: *"Intel rises as strong forecasts signal AI boost for turnaround"* [18 articles/6 outlets,
  head tier] with `└` ***"AMSL, AMAT, KLAC, LRCX: Chipmaking Equipment Stocks Rise On Intel's CapEx
  Bump"***; parent thread *"Intel's stock jumps 11% as chipmaker rides AI boom"* 4→8→3→10→6.
- **Direction (body-read)**: the article title itself names the mechanism — **Intel's capex bump**, not
  Intel's EPS. That is exactly the observable **S6** froze (*"a named external 18A/foundry customer,
  **or** capex/utilisation guided up"*), and **S6 scored FIRED-A at this run's HANDOVER**. INTC traded
  **+2.96%** in the article's own ticker strip after closing **−2.33%** on 07-23 pre-print.
- **Exposure**:

| Ticker | Chain position | Flow tag (asof 07-23) | Short-pressure (FINRA z, 07-23) |
|---|---|---|---|
| AMAT | semicap — the capex beneficiary | 🔴분산 (**OBV-derived**), RS20 −5.1 / **RS60 +35.8** vs SPY | z +1.01 normal |
| LRCX | semicap | 🔴분산 (OBV), RS20 −15.4 / **RS60 +20.0** vs SPY | z +0.92 normal |
| KLAC | semicap | 🔴분산 (OBV), RS20 −9.7 / **RS60 +11.9** vs SPY | z +1.07 normal |
| ASML | semicap, named in the title | 🟡중립, RS20 +1.6 / RS60 +22.7 vs SPY | — |
| INTC | the spender itself | 🔴분산, RS20 −24.5 / RS60 +14.7 vs SPY | ★ **z +2.17 = short spike into the print** |

- ⚠ **Rule D6 applied explicitly**: all three semicap 🔴 tags are **OBV-derived, i.e. C-grade**, sitting
  on **positive RS60 vs SPY**, which is A-grade. **The reds may be reported; they may not be cited as
  evidence the equipment leg is broken.** This is the same C-grade-red audit SWEEP §2i ran across the
  whole sector (10 of IT's 26 reds have positive RS60).
- **Future — both branches, dated**:
  - **IF the semicap RS20 vs SPY turns positive within 10 sessions of MSFT/META's capex lines** →
    the 20-day pullback resolves upward and **S13 branch A's supplier leg is confirmed**.
    Track KPI: median RS20 vs SPY of {AMAT, LRCX, KLAC}. **Horizon: 2026-08-12.**
  - **ELSE (kill condition)** → their RS20 vs SPY is still negative on **2026-08-12** *and* RS60 has
    fallen below +10 — at which point "pullback inside an uptrend" is no longer a defensible reading
    and the standing thesis on that node must be retracted rather than rolled.
- **Cell**: **CONFIRMED-EARLY on the narrative axis, 🟡-blocked on the money axis** (OBV disagrees
  with RS60 and OBV is C-grade). **Handed to ROTATION as the DEEP ① mandate, not to BET as a name** —
  the honest gate is the RS20 flip, which has not happened.

---

## Card 5 — "Big banks wade back into commercial real-estate lending" · ★ the body **contradicts** the headline

- **Thread**: *"Big Banks Are Wading Back Into Commercial Real-Estate Lending"* [10 articles/**9
  outlets**, head tier] · **BUILDING 5 days, 5→7→3→5→9** — the longest-running BUILDING thread on the
  board and the only one whose outlet count peaks **today**.
- **Direction (body-read — and this is why the card survives selection but not the cell it looked like)**:
  the WSJ item is **title-only in the pool (no body)**. The nearest bodied members of the same thread
  say the **opposite** at the individual-bank level: BankUnited's Q2 call, 07-22 — *"loan growth lagged
  expectations because of tougher competition and tighter pricing in lending, prompting BankUnited to
  cut some business and **lower its full-year core loan growth outlook to 4% to 5%**."* Earlier members
  are a Q2-beat item (M&T) and a **profit-target raise** (UniCredit) — i.e. **margin and capital-return
  news, not volume news**.
  ⇒ **The thread is being carried by bank *earnings*, and the one bank that quantified *lending volume*
  guided it DOWN.** The headline's claim is not confirmed by any body in the pool.
- **Exposure**: money-centers are **absent from the entire 🟢 shortlist** (SWEEP §3). Financials'
  greens are **insurance and payments-adjacent (TRV +0.917, CB +0.81)**, and the sector is breadth-led
  (**eqflow +0.329 > wflow +0.257**). The would-be beneficiaries of a CRE-lending upturn — the regional
  and money-center banks — carry none of the sector's flow.
- **Future — both branches, dated**:
  - **IF** a second bank quantifies **CRE loan growth upward** on a Q2 call by **2026-08-08** → the
    headline is real and Financials' OW− gains a volume leg it currently does not have.
  - **ELSE (kill condition, and this is the live one)** → no bank quantifies it and the thread's
    outlet count falls below 5; the story was an editorial theme assembled from earnings beats.
- **Cell**: **STORY-ONLY** (BUILDING narrative × money that is in the *wrong names* — insurance and
  payments, not lenders) → watchlist, dated re-check **2026-08-08**. **No name handed to BET.**
  ★ This card is the stage's own EXIT-CHECK case in the wild: **a 9-outlet head event whose direction
  body-read removed it from the candidate flow.**

---

## Card 6 ★ — Stripe's $53B bid for PayPal · a live, **unconsummated** deal sitting inside S14's observable

- **Thread**: *"Stripe Plans to Acquire PayPal for $53 Billion"* · **REIGNITED 3→2→4**.
- **Direction (body-read — the decisive detail)**: **the deal is NOT agreed.** *"On July 15, Stripe
  made an offer to buy PayPal (NASDAQ: PYPL) for $53 billion. While PayPal has not accepted that offer
  as of July 22, with its **board opting on July 20 to hold out for a higher price**, the acquisition
  could still very well go through."* Strategic rationale in the body: stablecoin rails (Stripe's Tempo
  chain, launched 03-18, with Visa among design partners).
- ★★ **Why this card matters far beyond PYPL, and it is a warning about a registered scenario.**
  **S14** (MA Q2, 2026-07-30) tests whether Financials' breadth is real by asking whether
  **{MA, V, PYPL} RS20 vs SPY stays positive**. Measured today: **PYPL carries RS20 +31.2 vs SPY — the
  highest of all 71 volume-blocked names in the universe** (SWEEP §2j/§3). **That RS20 is a takeover
  premium, not payments breadth.** ⇒ **S14's branch-A observable is contaminated by a merger-arb
  spread in one of its three legs**, and scoring it as written would credit "breadth" to a bid.
  **Registered as a scenario defect below, in the same family as D28/D35/D46.**
- **Exposure**:

| Ticker | Chain position | Flow tag (asof 07-23) | Short-pressure (FINRA z, 07-23) |
|---|---|---|---|
| **PYPL** | the target | 🟡중립 (blocked by vol_surge 0.97), flow +0.650, **RS20 +31.2** vs SPY, OBV 매집 | z −0.94 normal |
| MA | S14's subject — prints **07-30** | flow-positive, RS20 vs SPY positive, **not 🟢** | z −1.37 normal |
| V | the named Tempo design partner | not 🟢 | ★ **z +1.68 = short spike** |

- **Future — both branches, dated**:
  - **IF the bid is raised or accepted before MA's 2026-07-30 print** → PYPL's RS20 is decisively
    deal-driven and **S14 must be scored on {MA, V} only**, with PYPL excluded and the exclusion logged.
  - **ELSE (kill condition)** → the bid lapses and PYPL's RS20 vs SPY falls below +10 by
    **2026-08-06**, confirming retrospectively that the "payments breadth" reading was a merger spread.
- **Cell**: **LATE-MONEY / not a thesis name.** PYPL's move is event-driven, so a valuation or flow
  read on it measures the deal, not the sector. **Handed to PREMORTEM as an S14 scoring correction,
  not to BET as a candidate.**

---

## Card 7 ★ — Novo Nordisk v. Eli Lilly escalates · Health Care **does** have a narrative, and C7 says it does not

- **Thread**: *"Novo Nordisk suing Eli Lilly over GLP-1 'outdated' advertising"* · **REIGNITED**,
  **34 articles / 10 outlets on 07-21 → 6 articles / 3 outlets today**.
- **Direction (body-read)**: escalation, dated today. *"Novo Nordisk announced **Friday** that it has
  asked a U.S. court to issue a **preliminary injunction** halting a series of obesity and diabetes drug
  advertisements run by Eli Lilly, **marking a new front** in the two companies' legal confrontation."*
- ★★ **Why this card is filed at all.** `STANDING_VIEW` **C7** — the desk's largest belief-vs-money
  gap — rests partly on the clause *"**no health-care thread exists among the 145 alive threads** —
  money without narrative."* **That clause is false on this window**: a 10-outlet, multi-day,
  REIGNITED health-care thread exists, and it names the sector's single largest flow contributor.
  **C7 keeps its `indistinguishable` verdict (C4) — but on one leg fewer**, exactly as SWEEP §2c
  removed the Δ leg. **Two of C7's "against the flow" arguments have now been removed by measurement
  in a single run.**
- **Exposure**:

| Ticker | Chain position | Flow tag (asof 07-23) | Short-pressure (FINRA z, 07-23) |
|---|---|---|---|
| **LLY** | defendant; **+1.97% on 07-23 (+3.20pp vs SPY)** | **🟢가속**, flow +0.555, RS20 +5.5 / **RS60 +33.4** vs SPY | z +1.10 normal |
| ABBV | non-GLP-1 large-cap pharma, unaffected leg | 🟢가속, flow +0.633, RS20 +8.7 / RS60 **+26.9** vs SPY | z −0.39 normal |
| JNJ | ditto | 🟢가속, flow +0.724, RS20 +6.9 / RS60 +11.8 vs SPY | z +0.69 normal |
| **MRK** | ⚠ **the contradiction name** — 🟢 flow with the board's worst revision book | 🟢가속, flow +0.615, RS20 +7.5 / RS60 +15.2 vs SPY | z +0.39 normal |
| TMO | ★ **`new_green` ignition today**, life-sciences tools (picks-and-shovels, not GLP-1) | **🟢가속**, flow +0.806, RS20 **+15.6** / RS60 +19.1 vs SPY | ✅ z −1.33 = clean rise |

- **Future — both branches, dated**:
  - **IF the injunction is granted** → an advertising-channel constraint on the category leader, which
    is a **revenue-timing** event, and the sector's flow leadership would have a name-specific cause
    rather than a defensive-rotation one. Track KPI: the court's ruling; LLY RS20 vs SPY.
    **Horizon: 2026-08-22** (no hearing date is published — the horizon is a review date, not a guess).
  - **ELSE (kill condition)** → the injunction is denied or withdrawn **and** XLV's RS20 vs SPY turns
    negative by **2026-08-06** — at which point the whole HC flow reading was a risk-off artifact.
- **Cell**: **CONFIRMED-EARLY at the sector level** (REIGNITED narrative × the board's best breadth,
  0.19, and 6🟢) → **ROTATION cross-evidence and DEEP ④ mandate**. ⚠ Not a single-name hand-off: the
  narrative is a **litigation** between two names, and the flow is spread across seven.

---

## Card 8 — China's memory/AI catch-up · precursor-form, and it aims at the desk's regime call

- **Thread**: *"How a homegrown Chinese chip maker became the memory ind[ustry's]…"* [07-18, 5 art/3
  outlets] → *"China's new chip stores data with a single electron"* [07-23, 2/2] → *"Inside China's
  All-Out Push to Catch Up With American AI"* [07-24, 5/3] · **BUILDING 3→2→3**, i.e. **precursor form**
  (starts ≤3 outlets, still climbing in article count). Sibling: *"China slaps export controls on 14 EU
  entities"* [27 art/**9 outlets**, head tier].
- **Direction (body-read)**: capability build-out, not a shipping product — the items describe a
  domestic memory champion and a research-stage single-electron storage device. **The relevant channel
  is supply**, and the desk's own carry already names it: `STANDING_VIEW` **C1** (do LTA price floors
  hold?) and **M7** (no new DRAM capacity before mid-2027). **A credible Chinese memory entrant is the
  one thing that could break M7's supply timeline** — and it was previously logged by this desk as a
  2-outlet item that went invisible (**CXMT's HBM-moat bypass, 2026-07-17**).
- **Exposure**:

| Ticker | Chain position | Flow tag (asof 07-23) | Note |
|---|---|---|---|
| MU | the incumbent whose margin the entrant would compress | 🟡중립, flow −0.092, RS20 −6.2 / **RS60 +85.6** vs SPY | **the highest RS60 in Information Technology** |
| SNDK | storage incumbent | 🔴분산, RS20 −16.6 / RS60 **+47.3** vs SPY | C-grade red on a strong A-grade RS60 (D6) |
| STX | storage incumbent — also Card 1's chain-hop name | 🟡중립, RS20 −8.7 / **RS60 +50.1** vs SPY, OBV 매집 | one hop, uncrowded |
| AMAT/LRCX/KLAC | the equipment sold **into** any new entrant — a partial hedge | 🔴 (OBV, C-grade) / RS60 +11.9 to +35.8 vs SPY | see Card 4 |

- **Future — both branches, dated**:
  - **IF the thread reaches ≥6 outlets with a *shipping-product or capacity* claim** (not a research
    result) → **M7's "no new capacity before mid-2027" is at risk and STANDING_VIEW §1's amplitude
    assumption must be re-examined**, feeding open dig **D1**. Track KPI: outlet count + whether any
    item names **capacity in wafers or bits**. **Horizon: 2026-08-22.**
  - **ELSE (kill condition)** → the thread stays ≤3 outlets and remains research-stage through
    **2026-08-22**; it is a technology-press story, not a supply event.
- **Cell**: **STORY-ONLY** (BUILDING narrative × no money yet moving on this cause) → watchlist with a
  dated re-check. ★ Filed deliberately as a **precursor**: the measured shape (a 2-outlet item climbing)
  is the only one that has ever given this desk five days of runway, and its 07-17 predecessor was
  missed precisely because it sat at 2 outlets.

---

## 9 · Book cross-check — ENDED threads under live exposure

Threads that **ENDED** inside this window, against the real book (`CYCLE_EXPOSURE.json`: AI-compute
12.14% via AVGO/NVDA/TSM · Energy 11.33% via XOM · missile-defense 10.27% via RTX):

| ENDED thread | Peak | Book exposure riding it? | Flag |
|---|---|---|---|
| *Oil hits $90 per barrel as US-Iran war escalates* (07-20~21) | 15 outlets | **Yes — XOM** | ⚠ **Not a real rotation**: the successor thread (*Oil jumps back above $100*, peak 29) is alive and today's #1 head event. Attention moved **up** the price ladder, not away |
| *Iran strikes another tanker in Strait of Hormuz* (07-20~22) | 11 | Yes — XOM | Same successor. No flag |
| *Oil prices rise slightly after US announces new [strikes]* (07-20~22) | 15 | Yes — XOM | Same successor. No flag |
| *China is considering export controls on AI tech* (07-18~23) | 11 | **Yes — AVGO/NVDA/TSM** | ⚠ **Flagged.** The thread ENDED, but a *different* export-control thread is today's **#2 head event at 9 outlets** (China's 14 EU entities). **Same policy instrument, new target.** The AI-compute exposure's China-risk leg has not gone quiet; it changed jurisdiction |
| *Dow Jones Shrugs Off Oil Shock While Nasdaq Take[s]…* (07-18~23) | 13 | Indirect | No position rides a market-commentary thread |

**No open position's thesis is riding a thread that both ENDED and has no live successor.** Two flags
are raised for the desk's records (oil-price-ladder rotation; China export-control jurisdiction shift),
neither of which requires a re-justification this run.

---

## 10 · Hand-off

| Destination | Content |
|---|---|
| **ROTATION** (sector cross-evidence) | Card 3 (refining leads crude on the A-grade axis — agrees with SWEEP §2b) · Card 4 (IT's semicap reds are C-grade) · Card 7 (Health Care **does** have a narrative — C7 loses a second leg) · Card 5 (Financials' CRE headline is body-refuted) |
| **BET §B** (CONFIRMED-EARLY names) | **MPC · VLO · PSX** only — the refining node from Card 3. Every other card resolved to STORY-ONLY, LATE-MONEY, or a 🟡 with a stated disagreement. **No STORY-ONLY name leaked into this hand-off.** |
| **PREMORTEM** | Card 2 (a July HIKE is bracketed by no scenario — mandatory both-sides) · Card 6 (**S14's branch-A observable is contaminated by a live takeover bid in PYPL**) · Card 1 (S13's branch is now narrated, so its "un-anticipatable" premise needs restating) |
| **DEEP** | ① semicap/IT split (Card 4) · ② Energy crude-vs-refining (Card 3) · ④ Health Care (Card 7) |

**Reject-ledger entries filed by this stage**: **none this stage.** Every thread that failed resolved
to STORY-ONLY with a dated re-check rather than a drop — and **DEAD requires both axes** (FADING/ENDED
**×** 🔴 dispersing), which no selected thread satisfied. **D27's "≥1 US row per run" obligation passes
to BET/ALPHA and is named here so it cannot be lost.**

---

## 11 · New scenario defect registered by this stage

| # | Defect | Why it matters | Owner |
|---|---|---|---|
| **D50** | **S14's branch-A observable ({MA, V, PYPL} RS20 vs SPY staying positive) contains a name under a live, unconsummated $53B takeover bid.** PYPL's **+31.2 RS20 vs SPY** is the highest of the 71 volume-blocked names in the universe, and the body-read shows the bid was made 07-15 and **rejected as too low on 07-20** | The scenario was written to test whether Financials' breadth is genuine. **A merger-arb spread scores as "breadth" under the observable as written.** ⇒ **Registration rule: before freezing a multi-name observable, check each leg for a live corporate action.** Same family as D28 (a price reaction inside an observable), D35 (a grid on two axes) and D46 (a window shorter than the observable's publication lag) — **four registration defects in nine scenarios** | PREMORTEM (registration discipline) |

---

## ✅ EXIT CHECK

- [x] **Scope market-correct** — `--scope foreign` on every `thread`, `fts`, `search` and `chain-hop`
      call. No KR feed touched this stage.
- [x] **Selection logged**: 131 alive → **8 selected, 123 not selected**, with the rule stated and the
      partial-day FADING distortion applied rather than quoted.
- [x] **Direction body-read on every card.** Two of the eight materially changed their card:
      **Card 5** (the 9-outlet CRE headline is contradicted by the only bank body that quantified loan
      growth) and **Card 6** (the "acquisition" is an unaccepted bid the target's board rejected).
- [x] **Every exposure name carries a flow tag with its asof (2026-07-23)** plus, where pulled, its
      FINRA short-z. **No STORY-ONLY name entered the BET hand-off** — that list is three refiners.
- [x] **Every card carries both branches, a kill condition, and a dated horizon.** Where no date is
      publishable (S8's Hormuz statement, the injunction hearing) it is `[blank]` or an explicit
      review date, **never a guess**.
- [x] `EVENT_ALPHA.md` written · CONFIRMED-EARLY handed to ROTATION/BET · **two ENDED-thread book
      flags emitted** · handoff-ledger update deferred to run end per `pipeline/handoff.md`.

> ✅ → ROTATION.
