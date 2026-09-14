# EVENT_ALPHA — industry_US · 2026-08-30 (Stage 5 / L1·EVENT_ALPHA)

> Bottom-up cross: which stories are BUILDING × is money already following. Scope **`foreign`**
> throughout (hard rule). Flow tags are from `SECTOR_FLOW_US_REPAIRED.json`, **asof 2026-08-28**,
> repaired basis — every tag below carries that label. This stage never sizes (P4).

## 0 · Rights that bind these cards

- 🚫 **No freshness/velocity claim from the sweep** (G1). Thread curves are from `thread`, a direct
  query, and are labelled as such.
- 🚫 **The window ends 2026-08-28, not today.** `M1090`: the foreign ingest returned **3 articles on
  08-29 and 0 on 08-30**. ⇒ **Running `thread --days 7` with today's default window returns 525 ENDED
  and ZERO alive threads — an artifact, not a market fact.** Every curve below is from
  `thread --date 2026-08-28 --days 7 --scope foreign`, which ends on a populated day and returns
  **217 alive threads**. **A run that had used the default window would have concluded the entire
  news tape went dead, and issued no cards at all.**
- 🚫 Flow tags are **repaired-basis** and may not be described as native tool output.

## 1 · Selection — logged, no silent truncation

**596 multi-day threads → 145 alive (BUILDING + REIGNITED) → 20 in precursor form** (starts ≤2 outlets
and climbing — the measured 5-day-runway shape) **→ 8 selected → 5 survived the body-read.**
**Not selected: 137 alive threads**, of which **12 were precursor-form** — named as a count, not
dropped silently. Selection rule applied in order: precursor-form first, then remaining
BUILDING/REIGNITED by peak, with market relevance as the tiebreak.

**The 3 killed at the body-read gate — and 2 of the 3 died the same way:**

| thread | curve | why killed |
|---|---|---|
| *"NVIDIA expects ~70% FY2028 revenue growth as it **resets gross margin outlook to 72–73%**"* | BUILDING 2→3→3 | 🚨 **The thread's own members are a `seekingalpha` guidance-recap TEMPLATE series** — Zoom FY27, Okta FY27, HealthEquity FY27, and the 08-28 member is **Luxshare Precision**, not NVDA. **The engine linked on title FORMAT, not subject.** Logged `reject_ledger` `K.본문반증`, revives-if ≥3 NVDA-subject members from ≥3 outlets, recheck **09-15** |
| *"Micron (MU) Falls More Steeply Than Broader Market"* | REIGNITED 2→2→2 | Same defect: members are **ACN, NEM, BlackBerry** — a Zacks-style auto-title. Logged `K.본문반증`, recheck **09-15** |
| *"Here's Why I Believe AI Is Not a Bubble"* | BUILDING 4→6→7→13 | **Opinion cluster, not an event** — members are *"Is Oklo the Next Great AI Story or Just Nuclear Hype?"*, *"AI Can't Thrive Without This Stock"*, *"Big Tech's AI spending is bigger than you think"*. **13 outlets of commentary is still commentary**; an exposure map built on it would be built on sentiment. No ledger row (nothing was rejected — there was never a testable claim) |

★ **`D414` registered** `[measured]`: **the thread engine links by title template, and two of eight
selected threads this run were format clusters wearing subject headlines.** Both would have produced
cards naming a company the thread was not about. **Positive form**: a thread whose members' *subjects*
differ while their *title syntax* matches is flagged before selection — testable by checking whether
≥2 members share a title skeleton with different entity slots.

⚠ One more thread was read and **not** killed but **not** carded: *"Ivonescimab… Overall Survival
Benefit vs Durvalumab in 1L Biliary Tract Cancer"* (REIGNITED 2→5→4→3, `prnewswire` **primary
source**). The **event is real**; the **thread is contaminated** (its 08-28 member is a Dolly Parton
obituary item). ⇒ the fact is carried into `SECTOR_DEEP_HLTH`'s input, the thread is not carded.

---

## 2 · The five surviving cards

### CARD 1 — ★★★ The hawkish repricing is **global**, not a US speech

- **Thread**: *"Warsh says Fed has 'work to do' if above-target inflation persists"* ·
  **BUILDING, precursor form 2→6→8→11→6→19**, 185 articles · window denominator **4,591 day-events →
  3,483 threads → 217 alive** (07-22→08-28). Sibling thread *"Key Takeaways From Warsh's Jackson Hole
  Speech"* **6→3→5→7→13→21**, 157 articles.
- **Direction (body-read, not headline)**: the timeline is a *build*, not a surprise —
  08-25 *"What the Fed's Latest Warning to Wall Street Could Mean"* → 08-26 *"Fed's Preferred Inflation
  Gauge Remains Above Target Range"* (`wsj`) → 08-27 *"Fed's Collins says readings are 'mixed'"* →
  08-28 *"Warsh says Fed has 'work to do'"* [19 outlets / 82 articles]. Subevents: *"Warsh signals
  **rate hikes may be needed**"* (AP), *"Cites 'Readiness to Act'… **Markets See a September Rate
  Hike**"* (Barron's). Primary source in the evidence list: **`federalreserve`, "Warsh, In Our Time."**
- ★ **The cross-check that makes this a card rather than a headline**: **three separate central-bank
  threads run hawkish in the same window.**
  - *"Global Market: **ECB may raise rates in September** as Iran war fuels inflation concerns"* ·
    REIGNITED **2→4→5→5**, 43 articles · evidence `bloomberg` ***"ECB's Schnabel Says Rates Must Rise
    More on Resilient Economy"***, `fxstreet` *"ECB tightening outlook offers support against US Dollar"*,
    08-28 *"ECB's Kocher: Europe's Economy Is Gaining More Momentum."*
  - *"**Australia Inflation Overshoots Estimates, Boosting Hike Bets**"* · FADING 4→7→2→8→3→2, peak 8.
  ⇒ **`M1090`-class observation**: this is a **synchronised global tightening impulse**, which is
  materially different from "the new Fed chair gave a hawkish first speech."
- **Exposure** (flow tags asof **08-28, repaired basis**):
  | name | chain position | flow | note |
  |---|---|---|---|
  | `XLF` complex — `JPM` +0.036 · `BAC` +0.138 · `C` +0.082 · `WFC` −0.055 · `MS` −0.024 · `GS` −0.078 | the paid-by-rates leg | all **🟡중립** | ★ **6 of 7 majors are OBV 매집** (JPM +0.176 · C **+0.377** · BAC +0.125 · WFC +0.113 · MS +0.089) **with rs20 all mildly negative (−0.9 to −2.7)** |
  | `XLU` complex — `NEE` −0.658 🔴 · `VST` −0.750 🔴 · `CEG` −0.077 | the pays-rates leg | **🔴분산** ×2 | the board's worst bucket |
  | `MSTR` +0.883 🟢 | the long-duration speculative leg (headline layer — crowded by construction) | 🟢가속 | rs20 +33.5 but **rs60 −1.4** |
- ★ **This card CORRECTS a diagnosis this run made 40 minutes earlier and I am appending, not editing**
  (`D48`). `SWEEP_READ §4` wrote that Financials' *"zero accelerating names in a 47-name sector"*
  contradicts its 60-day price leadership and that the desk *"does not have a rule that says which
  wins."* **The name-level pull resolves it**: the banks are **accumulating on OBV and flat on rs20**
  ⇒ the "0 greens" is a **tag threshold** outcome (the 🟢 tag needs momentum, not just accumulation),
  **not distribution**. The honest statement is *"money is still entering while relative strength has
  stalled"*, which is a different — and weaker — claim than either of the two the earlier file offered.
  `M1096`-adjacent; the SWEEP_READ text stands unedited.
- **Future — both branches, dated**:
  - **IF the thread keeps building AND `DGS2` holds the repricing** → the paid-by-rates leg keeps its
    60-day lead and the pays-rates leg keeps losing. **Track KPI: `DGS2` ≥ 4.32 at the first `[FRED]`
    close covering 2026-09-04** (this is `P115` branch A — *the card does not re-freeze it*).
    **Horizon 2026-09-08.**
  - **ELSE / KILL** → **`DGS2` ≤ 4.12 at that date** falsifies the card: the speech was positioning,
    and the `XLU`/`XLRE` weakness needs a non-rate cause. **Also kills it**: an Aug-NFP miss ≥100k in
    either direction on **09-04**, which moves the same instrument for a different reason.
- **Cell**: **CONFIRMED-EARLY on the money axis for the rates-paid leg** (OBV accumulation is present
  and pre-dates the speech), **STORY-ONLY on the tape axis** (rs20 has not turned). ⇒ **handed to
  ROTATION as sector-level cross-evidence, NOT to BET as a fresh name.**

### CARD 2 — ★★ The dollar is moving and the desk's only FX instrument cannot see it

- **Thread**: *"Dollar jumps after Warsh comments, set for weekly gain"* · **BUILDING, precursor form
  2→4→3→3→5**, 46 articles.
- **Direction (body-read)**: a clean four-day build, and the mechanism is named inside it —
  08-25 *"Dollar Slightly Lower on Strong Stocks and Weak Crude"* → 08-26 *"Dollar Rises on US Economic
  News"* → 08-27 ***"US Dollar Index gains support as strong US data sparks rate hike expectations"***
  → 08-28 *"Dollar jumps after Warsh comments"* [5 outlets]. **The thread's own body attributes the move
  to rate-hike expectations**, which is Card 1's mechanism seen in a second asset.
- 🚨 **The instrument finding is the card's core**: `DTWEXBGS` — this desk's only broad-dollar series —
  **last publishes 2026-08-21**, nine days back, at **118.06, the 8.2nd percentile of its year**.
  ⇒ **The desk's dollar reading is a nine-day-old series sitting near a yearly LOW while five outlets
  report a weekly GAIN.** `D333`'s 12th reproduction, and the first time the lag demonstrably hides a
  **direction** rather than a level. Corroborating side-evidence in the same window: **Japan spent a
  record $96.5bn supporting the yen over the past month** [5 outlets] — i.e. the other side of the
  trade is intervening.
- **Exposure**: this card deliberately names **no equity**. A dollar move with a nine-day-blind
  instrument cannot support a name-level claim, and pretending otherwise is the `C3` failure.
  The affected book exposure is stated instead: the two refiners (`MPC` +0.650 🟡 · `PSX` +0.388 🟡,
  both OBV 매집) and `NUE` −0.307 🟡 are the dollar-sensitive legs the book actually holds.
- **Future — both branches, dated**:
  - **IF** `DTWEXBGS` publishes a bar ≥ **119.00** covering any date 08-24→09-11 → the dollar leg is
    real and the desk was blind to it for ≥2 weeks; **this becomes an instrument escalation, not a trade.**
  - **ELSE / KILL** → `DTWEXBGS` publishes ≤ **117.50** for that window → the news layer over-read a
    session move and the stale series was, by luck, not misleading. **Horizon 2026-09-11.**
- **Cell**: **STORY-ONLY (instrument-blind)** → watchlist with a dated re-check **2026-09-11**.
  **Not handed to BET.** ⚠ Filed this way deliberately: the alternative — inferring an FX direction
  from headlines because the series is stale — is exactly what `C3` forbids.

### CARD 3 — ★★ Hormuz: the strait is reported open and shut in the same 24 hours

- **Thread**: *"Qatar Extends LNG Force Majeure as Hormuz Traffic Remains Halted"* · **REIGNITED
  3→2→4→6**, 29 articles · evidence `bloomberg` · `oilprice` *"Gas Prices in Asia and Europe Jump as
  Qatar Extends LNG Force Majeure"* · `hellenicshipping`. Parent thread *"As Iran war hits six-month
  mark"* **BUILDING 3→3→4→5→5→16**.
- **Direction (body-read) — and it splits**:
  - **Shut**: `bloomberg` "Traffic Remains **Halted**"; subevent *"**Hormuz Tanker Traffic Drops**
    Despite Recovery in Oil Flows"*; gas prices **jump** in Asia and Europe.
  - **Open**: `nasdaq` *"Crude Prices Slip as **More Oil Flows Through** the Strait"*; `chain-hop`
    surfaced *"**Strait of Hormuz Traffic Ticks Higher** Amid New Diplomatic Push"* and *"Oil Price
    Today (Aug 27): Crude dips to $87, 4th session down amid **Hormuz reopening**"*; the 14-outlet
    head cluster is *"Crude heads for **weekly losses**."*
  - ⚠ **Contrary item inside the bullish leg**: 08-26 *"Woodside Energy: **LNG Upside Capped**
    (Downgrade To Hold)"* — a sell-side downgrade sitting inside the force-majeure thread.
  ⇒ **The card's content is the contradiction itself**, and it is `P117`'s object.
- **Exposure — one hop past the headline** (`chain-hop "Hormuz" --days 7`, proximity-based; flow asof
  08-28, repaired):
  | name | chain position | proximity / body hits | flow |
  |---|---|---:|---|
  | `CVX` | integrated, headline-adjacent | 10 / 34 | **+0.072 🟡**, OBV +0.093 매집, rs20 −0.4 |
  | `COP` | E&P, **not** headline-named | 4 / 16 | **+0.324 🟡**, OBV +0.097 매집, rs60 +7.5 |
  | `OXY` | E&P, not headline-named | 2 / 13 | **−0.025 🟡**, OBV +0.056 neutral |
  | `SLB` | services — **the chain layer nobody carded** | — | **+0.661 🟡**, OBV **+0.318 매집**, rs20 **+12.6**, but **rs60 −1.2** |
  | `XOM` | the sector's top-1 and its only 🔴 | — | **−0.486 🔴분산**, OBV −0.201 |
  ⚠ **Proximity noise disclosed**: the same query returned `META` (14), `WMT` (9), `HD` (9), `KO` (3)
  — all artifacts of market-wrap articles that mention the strait in passing. **Not carried.**
- **Future — both branches, dated**:
  - **IF the thread keeps building AND the shut leg is right** → `BZ=F` settled close **≥ 95.00** on any
    bar through **2026-09-18** (this is `P117` branch B; the card does not re-freeze it). Track KPI:
    **whether Qatar's force majeure is lifted or extended again.**
  - **ELSE / KILL** → `BZ=F` **≤ 85.00** on any bar through 09-18 ⇒ the war premium is out and Energy
    must stand on refining margin — **which `R89`/`P83` say this desk has no surviving instrument to
    measure.** ⚠ **VOID condition**: a **Venezuela supply event** (the *"weighs OPEC exit"* cluster ran
    **14 outlets / 29 articles** on 08-28, and Chevron is *"near a deal to invest billions"*) moves
    Brent for a non-Hormuz reason. **Base rate checked and NOT remote.**
- **Cell**: **LATE-MONEY on the headline names** (`XOM` is distributing while the story is loud) ·
  **CONFIRMED-EARLY-adjacent on `SLB`** (OBV 매집 + rs20 +12.6 with **rs60 still −1.2** = accumulation
  that has not yet produced a 60-day leg — the shape the stage says is the real chain-hop alpha).
  ⇒ **`SLB` handed to ROTATION/BET as an ENRG cross-check candidate**, with the valuation gate unset
  and the `R89` prohibition attached. Logged to `missed_ledger` (`M.숏리스트탈락`, enters-if a green
  tag under ≥80% coverage **or** rs60 turning positive with OBV still accumulating, recheck **09-12**).

### CARD 4 — ★★ The AI-capex denominator, seen from a country the desk never looks at

- **Thread**: *"**Australia's Capex Drops as Data Center Spending Hits Air Pocket**"* · **BUILDING
  4→4**, 8 articles, `bloomberg` primary. Members: 08-28 *"Australia data centre firm **NextDC**
  reports rising water, energy use with **profit beat**"*, `seekingalpha` *"DigitalBridge expands in
  Australia with PLUS ES smart-meter deal"*, `japantimes` *"Albanese **eases** demand that Australian
  data centres use only renewables."*
- **Direction (body-read)** — **internally contradictory, and that is why it is worth a card**:
  national capex **down** on a data-centre air pocket, while the country's listed data-centre operator
  **beats on profit** and the regulator **relaxes** a renewables constraint. ⇒ **the aggregate is
  falling while the incumbent's economics improve** — the signature of *concentration*, not of a cycle
  turning down.
- ★ **Why this thread was selected out of 145**: it is the only alive thread in the window that
  measures **AI-capex as a national statistic** rather than as a company's guidance. The desk's entire
  AI-capex evidence base is issuer-sourced (`NVDA`'s $279bn commitment, `IREN`'s $2.4bn financing,
  *"Big Tech's AI spending is bigger than you think"*), and **an issuer-sourced denominator cannot
  falsify an issuer-sourced numerator.** Four outlets in Australia can.
- **Exposure** (flow asof 08-28, repaired · **no Australian listing is in `us_top300`, stated as a
  coverage limit, not worked around**):
  | name | chain position | flow |
  |---|---|---|
  | `VRT` | data-centre electrical, headline-named (crowded layer) | **+0.153 🟡**, OBV +0.093 매집, rs20 +3.3, **rs60 −24.5** |
  | `ETN` (held) | AI-power/electrical | **−0.061 🟡**, OBV +0.202 매집, rs20 −6.0, rs60 −6.4 |
  | `PWR` | grid construction | **−0.622 🔴분산**, OBV −0.117 |
  | `GEV` | AI-power generation (and the subject of a separate REIGNITED 4→6 thread, *"GE Vernova vs Bloom Energy"*) | **−0.640 🟡**, rs20 −11.0, rs60 −7.0 |
  | `NEE` · `VST` | utility-side AI-power | **−0.658 🔴** · **−0.750 🔴** |
  ⇒ ★ **Every name on the AI-power chain is negative on flow, and two are outright distributing.**
  `VRT`'s **rs60 −24.5** against its positive OBV is the sharpest single divergence in this card.
- **Future — both branches, dated**:
  - **IF the air-pocket generalises** → the AI-power complex's negative flow persists and `XLU`'s
    `exc20` **−6.69** is a capex signal, not a rate signal. **Track KPI: `XLU` `exc20` vs `SPY` at
    2026-09-18 ≤ −4.00pp** while `DGS2` is **inside** `P115`'s C band (i.e. rates did *not* move) —
    that conjunction separates the two causes.
  - **ELSE / KILL** → `XLU` `exc20` **≥ 0.00pp** by 09-18, or `GEV`/`VRT`/`ETN` flow turning ≥ +0.30
    on the same axis ⇒ the air pocket was an Australian statistical artifact. **Horizon 2026-09-18.**
- **Cell**: **DEAD on the money axis is NOT the verdict — the story is BUILDING while the flow is 🔴,
  which is the top-left/bottom-right diagonal, not the DEAD cell.** ⇒ **re-filed as a watchlist item
  with a rewritten thesis line**: *"AI-power is being distributed while AI-capex commitments are still
  being announced; the falsifier is the national capex statistic, not the issuer guidance."*
  Dated re-check **2026-09-18**. **Not handed to BET.**

### CARD 5 — ★★★ The memory producers' own CEO is arguing the desk's regime call is wrong

- **Thread**: *"Here's Why Micron Stock Can Double Next Year"* · **BUILDING 3→3→3→4**, 33 articles.
  Companion alive thread *"Micron Under Pressure: Is the AI Memory Boom Losing Momentum?"* ·
  **BUILDING 3→3→3**, 16 articles. **Two alive threads on one complex, pointing opposite ways.**
- **Direction (body-read) — and this is the card's whole point**:
  - 08-24 ***"'No AI Without Memory': Micron CEO says the chip industry's old boom-bust playbook is
    breaking"***
  - 08-27 ***"Why Micron Stock Is Getting a Boost From Nvidia's Memory Price Warning"***
  - 08-28 ***"Micron (MU) CEO: AI Shift Breaks Traditional Memory Market Cycles"***
  - against 08-25 *"Micron Under Pressure: Is the AI Memory Boom Losing Momentum?"* and 08-27
    *"Not SanDisk. Not Micron. This AI Semiconductor Powerhouse Could Be the Biggest Winner"*
    and `seekingalpha` *"SK hynix: Cheap Despite A Historic Memory Boom."*
  ⇒ 🚨 **The desk's oldest carried belief — `[inferred]`, spine §1: *"Memory is a price-cycle industry
  in rate-of-change deceleration"* — is being publicly contested by the producer's own CEO, twice in
  one window, with a named mechanism ("the old boom-bust playbook is breaking").** That is not
  evidence the call is wrong; **it is a dated, sourced challenge to it**, and the desk has never
  recorded one before.
- **Exposure** (flow asof 08-28, repaired) — ★ **and the complex splits along producer / equipment**:
  | name | chain position | flow | OBV |
  |---|---|---|---|
  | `MU` | producer | **+0.346 🟡** | **+0.126 매집**, rs20 +10.3, **rs60 −15.6** |
  | `SNDK` | producer | **+0.358 🟡** | **+0.100 매집**, rs20 **+19.3**, **rs60 −20.9** |
  | `WDC` | producer | **−0.839 🔴분산** | −0.182, rs20 −18.6, rs60 −24.6 |
  | `AMAT` | equipment | **−0.839 🔴분산** | −0.235 |
  | `KLAC` | equipment | **−0.647 🟡** | −0.080 |
  | `LRCX` | equipment | **−0.022 🟡** | +0.104 매집, **rs60 −14.2** |
  ⇒ **`M1097`-adjacent**: **two of three producers are accumulating with strong 20-day and deeply
  negative 60-day legs; the equipment layer is distributing across the board.** That is the shape of a
  **turn being bought at the producers and not yet believed at the equipment layer** — or of a bounce
  in a downtrend. **The card does not choose; `P111` brackets it.**
  ⚠ `WDC` breaks the producer pattern and is named rather than dropped from the average.
- **Future — both branches, dated**:
  - **IF the CEO's framing is right (the cycle is broken)** → **`EW{MU,SNDK,WDC}` 10-session excess vs
    `SPY` ≥ +5.00pp, 2026-08-28 → 2026-09-14** — this is **`P111` branch B**, and the card does **not**
    re-freeze it. Track KPI: whether a **second** producer-side capacity commitment ≥$10bn appears
    (that is `P109`; SK Hynix's Indiana **$5bn** on 08-28 failed it on magnitude).
  - **ELSE / KILL** → `EW{MU,SNDK,WDC}` exc10 **≤ −3.00pp** (`P111` branch A) ⇒ the regime call
    survives and the CEO's framing is a seller talking his book.
  - ⚠ **VOID**: a producer-specific dated announcement (guidance revision, pre-announcement, or M&A) at
    any of `MU`/`SNDK`/`WDC` inside the window. **Base rate not remote** — both are mid-re-rating.
- **Cell**: **CONFIRMED-EARLY at the producer layer** (`MU`·`SNDK`: OBV 매집 + rs20 positive, rs60 not
  yet turned) · **LATE/DEAD at the equipment layer** (`AMAT`·`KLAC` distributing while the story is
  loud). ⇒ **producer layer handed to ROTATION as an IT cross-check**; equipment layer flagged as the
  crowded/exiting side. **No name handed to BET** — `P111` owns the test and it is 1 of 10 sessions in.

---

## 3 · Book cross-check — threads an open position's thesis rides on

| position | its thesis rides on | thread state (window ending **08-28**) | flag |
|---|---|---|---|
| `NVDA`·`ANET`·`AVGO`·`HPE` (AI-compute) | AI-capex continuing | the **only** alive AI-capex threads are an **opinion cluster** (killed, §1) and a **format cluster** (killed, §1). The one *event*-grade capex thread in the window is **Card 4, and it points down** | 🚨 **The book's largest cluster has no surviving event-grade thread supporting it this window.** Its 08-28 tape was the board's worst (`HPE` −3.90 · `NVDA` −4.58 · `ANET` −2.87, 5m-proxy). **Named for ROTATION; not a sell signal and not sized here** (P4) |
| `ETN` (AI-power) | AI-power buildout | Card 4 — BUILDING **against** it, and every chain name is negative on flow | 🚨 flagged |
| `MPC`·`PSX` (refining) | refining margin | Card 3 alive and **two-sided**; both names OBV 매집 with the board's best 60-day legs (`rs60` +36.0 / +30.1) | ⚠ **`R89`/`P83`: the desk may not assert margin-vs-barrel separation on any instrument.** The strength is recorded, the attribution is not |
| `RTX` (defense) | rearmament | no alive defense thread in the window; `ITA` `exc20` **−5.88** | ⚠ **`W4` unpaid 211 days** (the customers have never been named). Flagged, 2nd run |
| `MET`·`NDAQ` (FIN) | Card 1's rates leg | alive and building | ✅ thesis has a live thread |
| `NUE` (steel) | — | no alive thread | ⚠ flagged |

⚠ **No ENDED-thread flag is issued this run, and the reason is instrumental**: with the default window
every thread reads ENDED (`M1090`), and with the 08-28 window the tag is trustworthy but the window
ends two days ago. **A stale-thesis flag would be indistinguishable from the ingest gap**, so none is
raised. Stated rather than silently skipped.

## 4 · Hand-off

- **To ROTATION (sector-level cross-evidence)**: Card 1 (`FIN` accumulation vs stalled rs20; `UTIL`
  distribution) · Card 3 (`ENRG` top-1 `XOM` distributing while the sector's other names accumulate) ·
  Card 4 (AI-power chain uniformly negative) · Card 5 (memory producers vs equipment split).
- **To BET §B as CONFIRMED-EARLY fresh candidates**: **`SLB` only** — and with the `R89` prohibition
  and an unset valuation gate attached. **No other name is handed forward.** `MU`/`SNDK` are
  CONFIRMED-EARLY on the axis but are `P111`'s registered observable and are therefore **withheld from
  BET to keep the test clean** (`S4` — an in-sample name is not a candidate).
- **STORY-ONLY, did not leak to the hand-off**: Card 2's dollar names (none issued by construction),
  Card 4's `VRT`/`GEV`.
- **Ledger rows written this stage**: `reject_ledger` ×2 (`NVDA` thread, `MU` thread — both
  `K.본문반증`, recheck **09-15**) · `missed_ledger` ×2 (`SLB` `M.숏리스트탈락`, `CRM` `Q.확신부족`,
  recheck **09-12**). ★ **`CRM` is the run's cleanest money signal** (flow **+1.000** = the cap,
  OBV +0.305, rs20 +36.3, rs60 +32.4, `vol_surge` 1.64, FINRA short z −0.76) **and it has no thread at
  all** — logged as a **miss, not a rejection**, because this stage requires the narrative × money
  cross and it only has one half.

## ✅ EXIT CHECK
- [x] **Scope market-correct** — `--scope foreign` on every `thread`, `brief`, `chain-hop` and `fts` call.
- [x] **Selection logged**: 596 multi-day → **145 alive** → 20 precursor-form → **8 selected** → 5 carded; **137 not selected (12 of them precursor-form)**, counted, not silently capped.
- [x] **Every card carries a direction body-read**, and the gate actually fired: **3 of 8 killed on the body-read**, two of them for the same newly-named defect (`D414`, format clusters).
- [x] **Every exposure name carries a flow tag with its asof date** (`2026-08-28`, repaired basis, stated on every table). **STORY-ONLY names did not leak** into §4's hand-off.
- [x] **Every card has both branches + a kill condition + a dated horizon.** Where a branch reuses an existing registered row (`P115`, `P117`, `P111`), the card says so and **does not re-freeze it** (`D242`).
- [x] `EVENT_ALPHA.md` written; **CONFIRMED-EARLY handed to ROTATION/BET (one name)**; book cross-check emitted with the reason no ENDED flag was raised; **both ledgers written** (2 rejections, 2 misses, all with `revives-if`/`enters-if` + recheck dates).

---

## 🚨 POST-HOC CORRECTION — appended 2026-08-30 23:3x KST (`D48`; full detail in `MACRO_REPORT.md`)

**§0's third bullet and §1's framing are WITHDRAWN.** This file said the default `thread` window
returns "525 ENDED and ZERO alive threads — an artifact" because *"the foreign ingest is dark since
08-28"*. **The ingest was never dark.** `brief`/`thread` read a **client-side mirror** that was 38
hours stale because `embed sync` was not run (the MACRO L2 spec asks for it explicitly). After
syncing: **50 alive threads** on the 08-24→08-30 window; per-day market events 791 / 832 / 832 / 854 /
733 / **295** / **123**.

**What survives, and it is most of the file:**
- ✅ **Using `thread --date 2026-08-28` was still the right call** — the mirror genuinely ended there,
  so every curve quoted in the five cards is a real measurement of a real window. **No card's
  trajectory number changes.**
- ✅ The three body-read kills (`D414` format clusters ×2, the opinion cluster) are unaffected —
  they were judgments about thread *composition*, not about window coverage.
- ✅ All flow tags, exposure maps and ledger rows are unaffected.

**What changes:**
- ⚠ **Cards 1–5 are dated to a window that ends 2026-08-28, and two sessions of foreign news now exist
  beyond it.** The cards are **not re-written** (their observables and kill conditions are frozen), but
  the gap is named here so BET does not read them as current.
- 🚨 **Card 3 (Hormuz) has a live update it could not see**: the 08-30 head layer carries **"Furore
  grows as Venezuela defends US oil deal with Trump" [9 outlets / 13 articles]** — and a **Venezuela
  supply event is `P117`'s registered VOID condition**, which the card itself flagged as "base rate
  checked and NOT remote". It has grown from a 14-outlet 08-28 cluster to a weekend head item.
  **Recorded on the row's own terms; not scored.** A second BUILDING thread on the same axis:
  *"New U.S. sanctions will hit ordinary Iranians hard"* → *"Iran war live: Tehran stands firm over US
  sanctions"* (3→3, 08-29→08-30).
- ⚠ **Card 4 (AI-capex air pocket) and Card 5 (memory) were not re-checked against the two recovered
  days.** Stated as an unmet check, not as an absence of news.
