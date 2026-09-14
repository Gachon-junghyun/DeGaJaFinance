# EVENT_ALPHA — industry_US — 2026-07-25 (Sat)

> Stage 4/10. Bottom-up complement to MACRO's matrix: *which stories are BUILDING, and is money
> already following them.* Scope **`--scope foreign`** on every call (hard rule).
> Flow tags are **asof 2026-07-24 settled close**, from `SECTOR_FLOW_US.json`; OBV is **C-grade (D6)**.
> **Zero sizing, zero buy/sell (P4).** Cards are dated and falsifiable or they are not written.

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: **4,455 daily events → 3,377 threads → 583 multi-day → 59 ALIVE.**
Window denominators: 07-19 **221** · 07-20 **701** · 07-21 **949** · 07-22 **816** · 07-23 **860** ·
07-24 **764** · **07-25 144 (Saturday, ~17% of a weekday — deflates every outlet count below)**.

**Selected 8 of 59 alive. 51 alive threads were NOT selected** — the cap is the stage's own ≤8, and
the count is stated rather than the list silently truncated. Selection rule applied in order:
(i) precursor form (starts ≤2 outlets and climbing) → **Card 1**; (ii) remaining BUILDING/REIGNITED
by peak → Cards 2, 3, 8; (iii) threads with a dated binary inside 10 days → Cards 4, 6, 7;
(iv) one thread selected **because the desk holds exposure to it** → Card 5.

⚠ **Tool defect logged before any card is read**: `chain-hop` returned **`기사 0건 스캔`** — a silent
zero — on every **3-token** query (`"refining diesel crack"`, `"memory supply agreement HBM"`), while
1- and 2-token queries scanned 1,500 articles. This is the US analogue of **M68** (KR: multi-token
`AI 서버 MLCC` → 4 hits vs single-token `MLCC` → 519). **No 0-result chain-hop in this run is treated
as evidence.** Registered as dig **D58**.

---

## Card 1 — ★★★ The $950bn Korea–US memory supply commitment · **CONFIRMED-EARLY (volume leg only)**

**Thread**: *"South Korea's SK Hynix, Samsung Elec sign $950 billion partnership with US big tech"* ·
**BUILDING, 3 days, outlets 3 → 2 → 6, 23 items** · precursor form (dipped to 2, then jumped to 6 on
a 144-event Saturday).

**Direction (body-read, not headline)** `[news — Reuters citing ROK presidential adviser Kim
Yong-beom; NOT an issuer disclosure]`: **SK hynix ≈$750bn to US buyers incl. NVIDIA "through
long-term agreements"; Samsung ≈$200bn to Broadcom; a separate SK hynix programme >$500bn with
NVIDIA; SKT to build a 2-GW facility on NVIDIA Vera Rubin + SK hynix HBM4, phase 1 operating 2027;
supply talks also under way with Anthropic. Korean officials put US buyers at 80–90% of the demand
behind Korea's planned expansion.**

★ **The body-read changes the meaning the headline carries.** A headline reading "$950bn of deals"
implies pricing power. The body says **volume commitments through LTAs, with no price term, ASP,
floor or escalator disclosed anywhere.** Per STANDING_VIEW §4 that moves the *timing* of the margin
call and not the call.

**Exposure** (one hop past the headline names, which are SK hynix / Samsung / NVIDIA / Broadcom —
the crowded layer by construction):

| Ticker | Chain position | Flow tag (asof 07-24) | Crowding |
|---|---|---|---|
| **DELL** | **AI-server assembly — the layer that consumes both the memory and the racks** | 🟡중립 · `obv=중립` · **RS60 +108.6** · Δ **+0.231** | ★ **Un-named**: appears in no thread title this week; **the board's highest RS60** |
| **HPE** | same layer, second vendor | 🟡중립 · **RS60 +66.8** · Δ **+0.378** | ★ Un-named; 2nd-highest RS60 on the board |
| MU | the US-listed instance of the same product cycle | 🔴분산 · RS20 **−24.7** · **RS60 +78.8** · Δ −0.258 | Headline layer |
| AVGO | the named counterparty of Samsung's $200bn leg | 🟡중립 · RS20 +0.2 · **RS60 −8.3** | Headline layer — **and the flow is not in it** |
| MRVL | custom-silicon alternative to AVGO | 🟡중립 · RS20 **−31.6** · RS60 +22.9 · `vs` 0.44 | One hop |

★ **The sharpest fact on this card**: the two names positioned to consume $950bn of memory —
**DELL (+108.6) and HPE (+66.8)** — carry **the two highest RS60 readings on the entire 300-name
board**, are **both blocked from 🟢 by `vol_surge` 0.44–0.58 alone (M75)**, and **neither appears in
any thread title this week.** The named counterparty **AVGO is negative on RS60 (−8.3)**.

**Future — both branches, mandatory:**
- **IF** the thread keeps building **AND** an *issuer* (SK hynix DART / Samsung DART / AVGO 8-K)
  discloses the contract with a term structure **→** the volume leg is confirmed at `[primary]`
  grade, and **C1 becomes measurable for the first time** (does the LTA carry a floor, a cap, or
  both). **Track KPI: an issuer filing, not a wire.** **Horizon: 2026-08-08.**
- **ELSE / KILL**: no issuer disclosure by **2026-08-08**, or a disclosed figure materially below
  $950bn ⇒ the number was a state-summit artifact and the card is dropped with its reason.
- ⚠ **Anti-signal specific to this card**: a disclosed **price** term showing hard floors would
  *strengthen* the memory-margin thesis rather than weaken it — the branch the desk has never priced
  (C1). It must not be read as bullish-by-default.

**Cell**: **CONFIRMED-EARLY**, but only on the **volume** axis. → ROTATION (Info Tech) / **dig D1**.

---

## Card 2 — ★★ The Warsh FOMC repricing · **STORY-ONLY (no clean equity exposure)**

**Thread**: *"Prediction: Kevin Warsh and the FOMC…"* + *"Kevin Warsh Just Vowed to Bring a 'Regime
Change' to the Fed"* · **REIGNITED, 6 days, outlets 5→5→5→9→5→5, 62 items** — the only continuously
alive macro thread into **D-4**.

**Direction (body-read)**: the thread's content is **reaction-function uncertainty, not a policy
signal** — six days of "what will Warsh do" with no new data. The measurable side sits in `[FRED]`
and `[COT]`, not in the feed: **2y 4.37% / real 10y 2.43%, both 120-day highs, with the breakeven
falling to 2.26%** (MACRO §A-1), against **UST 10Y spec positioning at the 12th percentile —
crowded short, and shorts ADDED 48,031 into the week.**

**Exposure**: deliberately **none named.** A rates thread with a 34.7%-priced hike and a crowded-short
positioning extreme has **no clean single-name expression** on this board, and the desk's own R11
retraction came from converting a curve read into a sector tilt too quickly. The transmission is
already carried at the matrix level (MACRO §E: Financials OW−, Utilities/RE/Staples on the duration
side).

**Future — both branches:**
- **IF** the FOMC holds and the 2y retraces below 4.15% → P1's own anti-signal fires and the
  duration tilts across §E must be re-cut in one move. **KPI: DGS2. Horizon: 2026-07-30.**
- **ELSE** the 2y closes **>4.45%** or real 10y **>2.55%** → **S9 fires** and duration de-rate becomes
  a regime call, not a tilt.
- **KILL**: the thread ENDS without the FOMC moving either threshold ⇒ it was six days of narrative
  around a hold.

**Cell**: **STORY-ONLY** → watchlist, dated re-check **2026-07-30**. **No name is handed forward.**

---

## Card 3 — ★★★ The AI-datacentre buildout: the announcement layer is at maximum velocity while the physical layer is being distributed · **LATE-MONEY**

**Thread cluster** (three alive threads read as one node, because they share a driver):
*"NAVER, NVIDIA and Brookfield to Expand Korea's National AI [Factory]"* [9/5] · *"India's HCLTech to
invest $1.48 billion in AI data centres"* [6/3] — **BUILDING 2 days, 3→5** · plus
*"Nvidia Delivers Fantastic News for Nebius"* / *"Super Micro Just Delivered Fantastic News to Nvidia
Investors"* — **BUILDING 2 days, 3→3**.

**Direction (body-read + tape cross)**: the announcements are **real and accelerating** — Korea's
national AI factory, HCLTech $1.48bn, SKT's 2-GW facility (Card 1), **DLR's $3.5bn Blackstone
Northern-Virginia acquisition and raised FY guide (Card 4)**, Verizon's **>$1bn dark-fiber deal**
[5/3], and 200 firms incl. NextEra/Duke/Equinix joining a US AI power-usage pledge.

★★ **And the money in the physical supply chain is going the other way.** Every name that has to
build the thing:

| Ticker | Chain position | Flow tag (asof 07-24) |
|---|---|---|
| **VRT** | datacentre power & cooling | **🔴분산 · flow −0.911 · RS20 −11.4 · RS60 −8.6 · Δ −0.253** |
| **PWR** | construction & engineering | **🔴분산 · flow −0.872 · RS20 −13.5** |
| **CIEN** | optical networking | **🔴분산 · flow −0.878 · RS20 −20.0 · RS60 −21.3** |
| **GEV** | heavy electrical equipment | **🔴분산 · Δ −0.274** |
| ETN | electrical components | 🟡중립 · **Δ −0.467** |
| ANET | datacentre switching | 🟡중립 · Δ −0.249 |
| VST · CEG · NEE | the power leg | 🟡중립 · **Δ −0.470 / −0.212 / −0.229** — the three worst deltas in Utilities |

⇒ **Seven of eight physical-layer names carry a negative delta and four are 🔴분산, in the week the
announcement layer printed its largest numbers ever.** The one chain-hop headline the tool surfaced
for this node — *"Why Vertiv Stock Zoomed 107% in Just Six Months of 2026"* — is the story; the
20-day money is the opposite of the story.

**Future — both branches:**
- **IF** the thread keeps building **AND** the physical layer's deltas turn positive → the
  distribution was a rotation inside an intact buildout, and this node is where the un-crowded
  exposure is. **KPI: VRT + PWR + GEV mean delta, and their RS20 vs SPY.** **Horizon: 2026-08-08.**
- **ELSE / KILL**: the physical layer's RS20 vs SPY stays negative through **2026-08-08** while
  announcements continue ⇒ **the market is pricing announcements it does not believe will be
  built**, and the card converts into the strongest available evidence for **S13 branch A** (capex
  raise read as margin drag) — from the supply side rather than the spender side.
- ⚠ **This card must NOT be read as "the AI cycle is over."** Card 4 measures the demand side
  beating consensus by 42.5%. The card's claim is narrower and exact: **announcement velocity and
  physical-layer money have decoupled.**

**Cell**: **LATE-MONEY** on the headline layer; **the physical layer is a valuation-gate note**, not a
candidate. → ROTATION (Industrials / Utilities / Info Tech cross-evidence).

---

## Card 4 — ★★★ Data-centre landlord demand beat, and it contradicts the desk's own carried explanation · **CONFIRMED-EARLY**

**Thread**: *"Digital Realty raises annual FFO forecast on robust data center demand"* [Reuters /
economictimes / yahoo_finance] + *"S&P 500 Movers: CHRW, DLR"* + the Q2 call transcript · **new,
event-anchored, 44 matches in 3 days.**

**Direction (body-read of the release)**: **Q2 revenue $1.92bn, +29% YoY vs $1.66bn consensus (a
15.7% beat); adjusted FFO $2.65 vs $1.86 (a 42.5% beat); FY26 AFFO guide raised to $8.15–8.20 from
$8.00–8.10; FY revenue guide raised to $6.85–6.95bn from $6.65–6.75bn**, attributed to *"resilient
leasing momentum from cloud and AI customers"* — plus **a $3.5bn cash-and-stock purchase of a larger
stake in three Northern Virginia data centres from Blackstone.**

⚠⚠ **Grade and n, stated before the conclusion**: **8-K filed 2026-07-23**, call 07-23 17:00 ET,
**session reaction 07-24 = +11.01% = +6.05σ** on a flat SPY (+0.10%) — after only **+3% in extended
trading**, i.e. the regular session added ~8pp beyond the initial reaction. **EQIX has no 8-K in seven
days and no earnings coverage ⇒ its +4.90% / +3.22σ is sympathetic spillover.** **n = 1 event, 1
sympathetic name.** This is the **C-B** shape and it is labelled as such rather than waived.

**Exposure**:

| Ticker | Chain position | Flow tag (asof 07-24) | Crowding |
|---|---|---|---|
| DLR | the event itself | 🟡중립 · `obv=중립` · RS20 +2.8 · **RS60 −1.5** · **Δ +1.099 = the largest single-name delta of all 300** | Headline layer |
| EQIX | peer, unreported | **🔴-side · flow −0.449 · `obv=분산`** · RS60 −3.1 · Δ +0.258 | Headline layer |
| **PLD** | ★ **industrial/logistics REIT — the third RE leg the desk has never named** | **🟢가속 · `new_green` · flow +0.706 · `vs` 1.34 · Δ +0.337** | ★ Un-named in every prior RE read |
| AMT · CCI | towers — **the control pair** | 🟡 · flow −0.321 / −0.249 · **RS60 −10.4 / −16.9** · Δ +0.341 / +0.316 | Control |

★ **What this card does to a carried belief**: R7/M24/M37/M88 read the digital-infra 🔴 cluster as
*"a third copy of the AI-datacenter short"* — the narrative topping. **The largest listed pure-play
datacentre landlord just beat on demand by 42.5% and bought $3.5bn more of it.** The **measurement
survives** (RS60 spread duration +11.1 vs digital-infra −7.98 = **19.1pp**, a fifth replication); the
**stated driver does not.** Direction right, driver wrong — **the same failure class the desk logged
for the KR bank NIM leg (R15) and the KR utilities leg.**

**Future — both branches:**
- **IF** DLR and EQIX hold their excess vs SPY past the print week **AND** AMT/CCI stay flat → the
  "digital infrastructure" bucket was **two things** and the RE underweight is a tower/duration call.
  **KPI: DLR and EQIX RS vs SPY measured from the 07-24 close; AMT/CCI as control. Horizon: 2026-07-31.**
- **ELSE / KILL**: DLR's excess fully retraces by **2026-07-31** ⇒ it was an earnings pop and R7 keeps
  its explanation intact.
- **Second, independent settling point**: **EQIX's own Q2 print — date `[blank]`, in no calendar
  (dig D54).**

**Cell**: **CONFIRMED-EARLY** → **ROTATION (Real Estate) as the run's top DEEP candidate**; PLD handed
forward as the un-named third leg.

---

## Card 5 — ★★ The refining margin: the physical evidence and the price evidence point opposite ways · **held open, both sides carried**

*(Selected under rule (iv): the book holds Energy exposure — `cycle_exposure` shows XOM at 11.4% of
the epicenter allocation.)*

**Thread**: *"Oil Slips From $100 As OPEC Signals More Supply"* [6/4] + *"OPEC+ Set to Raise Output
Again — Even as Members Can't Pump It"* [07-23], against a Red Sea / Houthi head event [9/7] and
*"Saudi-led coalition attacks Yemen's Hodeida port"* [3/2].

**Direction — and this is why the body-read matters**: the two sides are **both primary-adjacent and
they disagree.**

- **AGAINST the margin** `[measured, settled 07-24]`: 3-2-1 crack **−3.29% to 64.30**; **the distillate
  leg fell HARDER than gasoline (−4.31% vs −2.45%) so the diesel-minus-gasoline gap NARROWED 35.50 →
  32.96 — the first narrowing of the run-up**; the settled weekly mean turned **−0.89% WoW**, the
  first negative week of the six-week advance; **Brent back below $100 (96.78)**.
- **FOR the margin** `[news, body-read, oilprice 07-20 quoting Morgan Stanley and Argus/Insights
  Global]`: *"Our supply/demand modeling points toward European diesel inventories falling to
  multi-year lows toward year-end"* — **"the picture is genuinely tight"**; European diesel refining
  margins hit **a record high >$60/bbl** after Russia's export ban; **diesel inventories are below the
  five-year seasonal range in PADD1, PADD3, ARA, Fujairah AND Singapore simultaneously**; Saxo's Ole
  Hansen on the record that *"refined products face far fewer mitigation options"* than crude.
- ⚠ **Staleness declared**: the supportive evidence is **dated 2026-07-20**, four sessions before the
  gap narrowed. It is a structural claim about year-end inventories, not a claim about 07-24.
- ⚠ **A lead, not evidence**: an oilprice sidebar carries *"India Hikes Diesel and Jet Fuel Export
  Tax"* — **body not in the DB, headline only.** If real it cuts directly against **M93**, which
  named India's record 1.55M bpd July distillate exports as the mechanism that ends the margin. **Not
  used as evidence; registered as dig D59.**

**Exposure**:

| Ticker | Chain position | Flow tag (asof 07-24) | Crowding |
|---|---|---|---|
| MPC | refining, the highest crack beta of the three on price | 🟡중립 · `obv=매집` · **RS60 +29.1** · Δ **−0.006** · blocked by `vs` 0.90 alone | Headline layer |
| PSX | refining + 4 other segments | 🟡중립 · RS60 +21.4 · Δ **−0.023** | Headline layer |
| VLO | refining, **prints first (07-30)** | 🟡중립 · RS60 +22.1 · Δ **−0.011** | Headline layer |
| XOM | **the control — M96 measured its crack correlation at +0.078, indistinguishable from zero** | 🟢가속 · **RS60 +0.4** | The book's only Energy holding |
| **SLB** | ★ oil services — one hop, un-named in the thread | 🟡중립 · `obv=매집` · **Δ +0.414 = one of the board's best** · `vs` 1.16 | ★ Un-named |

★ **The one-line reconciliation**: **the level is at the 88.9th percentile of 90 days and the rate is
now below zero on both the daily and the weekly axis, while all three refiner deltas are negative and
their RS60 is still +21 to +29 vs SPY.** Level top, rate turning — **lens L1, the identical structure
this desk carries for memory (M1/M18), in a second industry.**

**Future — both branches:**
- **IF** the diesel gap re-widens and the crack stabilises ≥65 → 07-24 was OPEC-headline noise into
  VLO's print, and Morgan Stanley's inventory model is the operative frame. **KPI: the
  diesel-minus-gasoline gap on settled closes. Horizon: 2026-07-30 (VLO).**
- **ELSE / KILL**: **a settled 3-2-1 crack below 60 (one axis, crude level removed — see MACRO §D-P4's
  declared registration defect), or a SECOND consecutive narrowing of the diesel gap** ⇒ the margin
  engine is rolling and the Energy tilt sits on crude/integrated alone. **Distance to the crack kill
  today: 4.30 points, the closest it has been.**
- ⚠ **The C4 detachment counter is NOT incremented** by 07-24 (crack −3.29% while refiners were flat:
  MPC −0.49σ, VLO −0.34σ, PSX −0.05σ). **M96 measured the counter under-powered** — at r≈0.30 a
  3-day sign disagreement happens ~6.5% of the time by chance. **Observation recorded, counter frozen.**

**Cell**: **held open — neither CONFIRMED-EARLY nor DEAD.** → ROTATION (Energy) as a DEEP candidate,
explicitly with **both** evidence sets attached.

---

## Card 6 — ★★ "Corporate America has decided to stop blowing money on AI" · **STORY-ONLY, and it is the un-bracketed branch acquiring a voice**

**Thread**: *"Corporate America Has Suddenly Decided to Stop Blowing Money on AI"* — **WSJ, 07-25**,
carried by wsj + google_en syndication ⇒ **effectively one source, title-only (WSJ bodies are not
scraped)**. Adjacent, same week: *"Oracle Is Spending Billions on AI. Why It Might Not Pay Off."*
[4/3] · *"Alphabet's cash burn raises alarm for Big Tech"* (carried, M82) · *"Tesla Misses Badly on
Earnings as Free Cash Flow Turns Negative"* [07-23, found only in the blind-pool sample].

**Direction**: the branch **C6** was logged to detect — *a capex raise priced as a margin drag* — is
being narrated. **It is not being narrated in the desk's vocabulary.**

| Probe | d1 | d7 | 90d |
|---|---|---|---|
| **`capex cut`** — C6's registered probe | **0** | **1** | **5** |
| `margin drag` | 0 | 1 | 2 |
| **`AI spending`** | **259** | — | 1,403 |
| `digestion` | 84 | — | — |
| `overbuild` | 7 | 32 | — |

⇒ **Four consecutive ~0 readings on the registered probe while the branch runs at 259 hits in 24
hours under other words and reaches the WSJ front page.** **C6's finding is stronger than ever; C6's
instrument is broken** (dig **D52**, raised at MACRO).

**Exposure**: **none handed forward.** ORCL is the only named instance with a tag
(**🔴분산, flow −0.233, RS20 −25.2, RS60 −34.5**) and a single 🔴 is not an exposure map. The correct
expression of this branch is **S13's line item** (MSFT/META capex guidance on 07-29), **not a ticker**.

**Future — both branches:**
- **IF** MSFT or META raises capex on **2026-07-29** and its multiple compresses → **S13 branch A**,
  and Card 3's decoupling gets its cause.
- **ELSE** the spenders re-rate on the same raise → the vocabulary was commentary and both the 07-23
  and 07-24 sessions were noise.
- **KILL**: `AI spending` velocity falls back below the pool while the spenders re-rate.

**Cell**: **STORY-ONLY** → watchlist, dated re-check **2026-07-30** (the session after S13's event).

---

## Card 7 — ★ Red Sea / Bab el-Mandeb: the thread is alive and its literal beneficiaries are still not bought · **DEAD on the money axis, RE-FILED not dropped**

**Thread**: *"Houthi Claim Missile Strikes on Southern Saudi Arabia"* [9/7] with `└` *"Saudi-led
coalition attacks Yemen's Hodeida port"* [3/2]; carried: *"Trump says US 'locked and loaded'"* [4/3].
`theme-age "ceasefire"` **4.76×**, `"OPEC"` **3.68×** — both 🟡ACCELERATING, and **nothing on the
board is 🟢FRESH or 🔴FADING for a second consecutive run** (M112 replicating; a tool-discrimination
defect, not a market fact).

**Direction (body-read)**: physically real — named tankers struck, a declared blockade, a 13th
consecutive US strike wave — **and the price went the other way this week**: Brent **−3.88%**, WTI
**−3.12%**, with OPEC signalling more supply.

**Exposure and the finding**: **M45's measurement replicates.** The blockade's literal beneficiaries
(STNG, FRO, INSW, DHT, TNK) are **not in `us_top300`**, so this desk cannot tag them from the sweep —
**an instrument gap, stated rather than substituted.** What is measurable: **WMB 🔴분산 (flow −0.491,
Δ −0.376)** and **KMI 🟡 (Δ −0.040)**, the two US midstream names the chain-hop attached to *"the Bab
al-Mandab blockade threat helped push oil back above $100."*
⚠ **WMB is a NATURAL GAS pipeline name and its attachment to a crude-blockade story is a mis-label** —
the desk has made exactly this error before and it is not repeated here.

⚠ **DEAD is a MONEY verdict on BOTH axes.** The narrative is **alive** (9/7 outlets); the money is
🔴 dispersing at the only US names the tool attaches. Per the stage rule, **this is re-filed with a
rewritten thesis, not dropped**: *"a geopolitical thread whose US-listed expression this desk cannot
measure, because the instruments are outside `us_top300`."*
**Dated re-check 2026-08-06** — which is also when **S21 (STNG, 07-30)** will have settled and will
deliver **S8 branch A on a dated observable** without needing a Hormuz statement.

**Cell**: **DEAD on the money axis / RE-FILED with a new thesis.** No name handed forward.

---

## Card 8 — ★ AMZN and NVDA ignited 4–5 sessions before their own binaries · **LATE-MONEY (positioning, not discovery)**

**Thread**: *"Is Now a Good Time to Buy Amazon Stock?"* [9/6] with `└` ***"Amazon CEO Jassy may deliver
a July 30 AWS earnings shock"*** [2/2] · plus *"Nvidia Delivers Fantastic News for Nebius"* /
*"Super Micro Just Delivered Fantastic News to Nvidia Investors"* — **BUILDING 2 days, 3→3.**

**Direction**: **the sweep's `new_green` list is 5 names and two of them are AMZN and NVDA**
(`new_green=True`, AMZN flow +0.438 / Δ +0.066, NVDA flow +0.420 / Δ +0.034), with **MSFT already 🟢
(+0.608, Δ +0.109)** and **META 🟢 (+0.596)** — four days before MSFT/META print (07-29) and five
before AMZN (07-30).

★ **By the C-B lesson this is positioning, not discovery.** An ignition inside a scheduled binary's
window is the event's own footprint; counting it as independent confirmation of a thesis is precisely
the error retracted four days ago on the rails. **It is written here so that no later stage can read
these four greens as breadth.**

⚠ **Corroborating positioning, demoted grade (M95)**: **MSFT FINRA short-vol z −2.82 and META z −2.35**
into their own prints — short pressure collapsing ahead of the event.
⚠ **And the AMZN date is 07-30, sourced to a 2-outlet body item — while `CATALYST_WATCH.json`
contains no AMZN row at all** (D18, §0 of MACRO).

**Future — both branches:**
- **IF** MSFT/META/AMZN raise capex and hold their 🟢 through **2026-07-31** → the ignition was
  informed and **S13 branch B** (the single IT label survives) gains.
- **ELSE / KILL**: any of the four loses 🟢 within 2 sessions of its print ⇒ the ignition was event
  positioning and unwinds, and Card 3's decoupling is the operative read.

**Cell**: **LATE-MONEY** → valuation-gate note. **Explicitly NOT handed to BET as fresh candidates.**

---

## 9 · Book cross-check — ENDED threads under live exposure

`cycle_exposure.py` (asof 2026-07-25, book ≈ $8,260): epicenter holdings **AVGO, NVDA, TSM**
(AI-compute, rank 1) · **XOM** (Energy, rank 2) · **RTX** (rearmament, rank 3). **No GAP flagged.**

**No ENDED thread sits under a live position.** Two weaker flags are raised instead:

1. ⚠ **AVGO** is the named counterparty of Card 1's $200bn Samsung leg **and carries RS60 −8.3 vs
   SPY**, ranking **10/10 in its own registry bucket (M81)**. The story is arriving at a name the
   money has been leaving for 60 days. **Not an ENDED thread — a thesis/tape divergence.**
2. ⚠ **XOM** is the book's only Energy epicenter name and Card 5 measures it as **the control**
   (crack correlation +0.078 ≈ zero, RS60 +0.4 against refining +21 to +29). **The ✅ is satisfied by
   the leg with the least exposure to the cycle's own driver** — M81 replicating on fresh numbers.

Both are handed to ROTATION/PREMORTEM as **exposure-quality** notes. **No sizing, no action (P4).**

## 10 · Rejection-ledger entries filed by this stage

**None.** Card 7 is **re-filed with a rewritten thesis rather than dropped** (the money axis is 🔴 but
the instruments are outside the measurable universe — an instrument gap is not a rejection), and no
other card reached a DROP verdict. **The one legacy row audited this run (`010120`, `reaffirmed`) was
closed at HANDOVER, not here.**

---

## ✅ EXIT CHECK
- [x] Scope was **`--scope foreign`** on every `brief` / `thread` / `fts` / `theme-age` / `chain-hop`
      call. No card cites a cross-market feed.
- [x] Selection logged: **59 alive → 8 selected, 51 not selected (counted, not silently capped)**,
      with the selection rule stated in order and the window denominators quoted (including the
      Saturday deflation).
- [x] **Every card carries a direction body-read**, not a headline: Card 1 (the $950bn is *volume*,
      no price term), Card 4 (the FFO beat and the $3.5bn deal), Card 5 (Morgan Stanley/Argus
      inventories against the settled crack), Card 7 (alive narrative, dispersing money). Card 6's
      source is **explicitly title-only** and no conclusion rests on its body.
- [x] Every exposure name carries a flow tag **with its asof (2026-07-24 settled)**; OBV cited as
      **C-grade (D6)**; **STORY-ONLY names (Cards 2, 6) were handed forward to nothing.**
- [x] Every card has **both branches + a kill condition + a dated horizon**.
- [x] `EVENT_ALPHA.md` written. **CONFIRMED-EARLY → ROTATION/BET: Card 1 (volume leg only, DELL/HPE
      as the un-named layer) and Card 4 (Real Estate / PLD).** Book flags emitted (§9). Handoff ledger
      is updated at run end per `pipeline/handoff.md`.
- [x] **Zero sizing, zero buy/sell language (P4).**

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **ROTATION**.
