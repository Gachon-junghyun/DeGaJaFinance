# EVENT_ALPHA — industry_US — 2026-08-02 (Sun)

> Bottom-up complement to MACRO's top-down matrix: *which stories are BUILDING this week, and is money
> already following them.* Runs after SWEEP, before ROTATION. `--scope foreign` on every news call.
> Flow tags from `SECTOR_FLOW_US.json` **asof 2026-07-31 settled**; short pressure from FINRA Reg SHO
> **2026-07-31**. Analysis only, zero buy/sell, zero sizing (P4).

---

## 0 · Window denominator, and the one caveat that governs every tag below

`thread --days 7 --scope foreign` · **daily events: 07-27 794 · 07-28 846 · 07-29 846 · 07-30 840 ·
07-31 772 · 08-01 274 · 08-02 86.**
**4,458 daily events → 3,413 threads → 560 multi-day → 37 ALIVE · 2,853 one-day (49 new today) ·
523 ENDED.**

⚠⚠ **The window ends on a weekend and the module warns about exactly this** (*"윈도우 끝이
휴일/저물량이면 FADING 이 과대해진다"*). **08-01 carries 35% and 08-02 carries 11% of Friday's event
count.** ⇒ **Every FADING tag in this run is weekend-inflated by construction.** A thread that went
`11 → 8 → 3` outlets from Friday to Sunday has **not** demonstrably faded — it ran out of publishing
days. **No card below is downgraded on a Friday→Sunday decay alone**, and where a FADING tag is used
it is used with the per-day denominator attached.

## 0b · Selection log — no silent truncation

**37 alive threads → 8 selected → 29 not selected.** Composition of the alive set: **4 BUILDING ·
13 REIGNITED · 20 FADING.**

**Selection order per the protocol: precursor-form first** (starts ≤2 outlets and climbing), then
remaining BUILDING/REIGNITED by peak, then FADING **only** where the book already holds exposure.

**The 29 not selected, by reason (counted, not hidden):**
- **11 non-market** — Moscow restaurant explosion · Korea heat-wave alert · Israeli soldiers /
  Sde Teiman · European wildfires · Ceuta migration · Nepali climbers · Peru plane crash ·
  Sudan · UEFA/FIFA · Social Security COLA · Kiyosaki.
- **8 syndicated template blobs, not threads** — *"Is {Corning|Bloom Energy|Ferrari} a Buy After Its
  Latest Earnings Report?"*, *"My 3 Favorite AI Stocks"*, *"Here Are My 4 Favorite Stocks"*,
  *"Meet the Dividend Growth Stock Warren Buffett Held"*, *"Best Growth Stocks to Buy for July 31st"*,
  *"Noteworthy ETF Outflows"*. The clustering links a **publisher's format**, not an event.
- **4 out of instrument** — SpaceX (not in `us_top300`) · Capital One preferreds · Bitcoin/ETH ·
  Israeli startup funding.
- **6 market threads deliberately deferred** — China economy/regulate-later · Russia-Ukraine
  *military* leg (its energy leg IS selected, Card 2) · Palantir/LLY earnings previews ·
  "Is the AI rally running out of steam?" (folded into Card 5 rather than double-counted) ·
  Amazon satellite network · Tesla-China.

**523 ENDED threads**: the peak-10 were read; **three are flagged against open book positions in §9**.

---

## CARD 1 ★★★ — The Iran strike-cancellation is CONDITIONAL, and it is the only precursor-form thread on the board

**Thread**: *"Trump says he is cancelling strikes on Iran subject to 'rapidly' making a deal"* ·
**BUILDING · 2 → 4 → 13 outlets (07-28 → 08-01 → 08-02) · 22 articles** · window denominator above.
**This is the textbook precursor shape the protocol tells this stage to select first** — and it is the
*only* one in the alive set with market content.

**Direction (body-read, not headline).** `[bbc 2026-08-02 03:19 BST, full body; corroborated dw 08-02]`
Trump, on Truth Social, **cancelled the attack *"subject to being able to rapidly make a DEAL"***,
where the deal *"would include the **immediate opening of the Strait of Hormuz**"* and an end to
Iran's nuclear threat. Same post: the US is *"locked and loaded and ready to go."* The cancelled plan
was, per CBS via the BBC, **"one of the harshest bombing campaigns to date against ENERGY
INFRASTRUCTURE targets in Iran."**
⇒ **The direction the headline hides: this is not a de-escalation that has happened. It is a US
precondition inside a deal that has not been made, and the alternative on the table is a strike
campaign aimed at oil infrastructure.** The two branches are therefore **not** "peace vs war" — they
are **"strait opens" vs "Iranian export capacity is bombed"**, which move crude in *opposite*
directions.

**Exposure** (flow tags asof 07-31 settled; ⚠ the whole Energy sector is 🟡 by artifact — SWEEP §3):

| Ticker | Chain position | Flow tag (07-31) | Crowding / note |
|---|---|---|---|
| **XOM** | integrated · the book's held Energy name | 🟡 +0.606, RS20 **+13.1** / RS60 −2.9, OBV 매집 | FINRA z **−0.48, 5v5 −6.8▼** — shorts leaving. **S31 branch A (against us) still tracking** |
| **CVX** | integrated · headline layer | 🟡 +0.600, RS20 +16.0 / RS60 −1.0 | z +0.02. **Beat on "refining margins soar"** — the opposite print to XOM's |
| **MPC · PSX** | refining · the book's held epicenter | 🟡 +0.567 / +0.600, RS20 +18.5 / **+19.7** | ⚠⚠ **PSX FINRA z +1.53 = 🔴 short SURGE, the only one on the desk's pull, and it prints 08-05** |
| **OXY · COP** | E&P · headline layer | 🟡 +0.556 / +0.628, RS20 +16.4 / +14.7 | headline-layer by construction — every outlet already printed them |
| **BKR** | oilfield services · **one hop past the headline** | 🟢 **+0.872, the sector's only green**, RS20 +14.3 / RS60 −14.0 | ⚠ **its reject-ledger basis is already known-false** (filed 07-27 as "the only negative flow score of 11 Energy names"; it has since been #1). Recheck date not yet due |

★ **chain-hop one hop past the headline** returned **WMB (Oil & Gas Storage & Transportation, 3
proximity / 42 body)** and **NOC (Aerospace & Defense, 2/8)** as names never in the thread's titles.
⚠ **WMB is 🟡 −0.195 with RS20 −2.5 / RS60 −9.2 and OBV 중립 — the money is not there**, which
reproduces the desk's own 2026-07-14 finding that WMB was a Hormuz mis-label. **Recorded so the same
mis-label is not made twice.**

**Future — both branches, mandatory.**
- **IF** the thread keeps building **AND** a deal is signed with a dated strait-opening ⇒ **S8's
  branch A finally has its observable**; the war premium deflates; **XOM/CVX/OXY/COP lose the leg
  S31 says they are standing on**, and the refining margin has to carry Energy alone. **Track KPI**:
  the appearance of a **dated** opening in a primary text (not a precondition). **Horizon: 2026-08-06**
  (S49's window close).
- **ELSE / kill condition** ⇒ strikes resume against **energy infrastructure**, which is a supply
  shock in the opposite direction and makes **S49 branch A** the read. **This card is falsified
  either way within the window** — that is why it is worth writing.
- ⚠⚠ **PREMORTEM owes a both-sides bracket on this.** A one-way tilt into a live binary is a
  protocol violation, and this binary's two branches move crude in opposite directions.

**Cell**: **STORY-ONLY → watchlist with a dated re-check (08-06).** The narrative is BUILDING; the
money is **🟡 across the entire sector and 11 of 12 Energy pre-condition names are blocked by
`vol_surge` alone (SWEEP §3)** ⇒ **the money axis is uncallable this run, so the cell is not forced
(P4).** ⚠ `theme-age "Hormuz"` is **⚪ECHO 1.67× on n=6,161** — the term axis did not see the day's
biggest event, which is **C6's shape reproducing on the US feed**.

---

## CARD 2 ★★ — Russia/Ukraine has become a REFINED-PRODUCT infrastructure war, and that is a different thesis from the crude one

**Thread**: Russia-Ukraine · **FADING 10→6→21→15→9→9→4 · 124 articles** ⚠ **its Friday→Sunday decay
is the weekend effect (§0)**; its 07-29 peak was 21 outlets.

**Direction (body-read).** The energy leg of this thread is not about crude: *"**Ukraine Says It
Attacked Lukoil's Volgograd Oil Refinery**"* and *"**Russia targets hundreds of Ukrainian petrol
stations**"* [12 art / 9 outlets, 07-31]. Both sides are now striking **refining and distribution**,
not production. Corroborating on the same feed: *"EU sanctions Georgian, Belarusian refineries for
Russian oil links"*, and **the Russian diesel-export ban expired 2026-07-31 without the bottleneck
releasing** (S49, HANDOVER §3c).
⇒ **The direction the crude tape hides: refining CAPACITY is the thing being destroyed, which is
bullish crack and bearish crude simultaneously.** That is exactly the split MACRO §D-P4 measured on
the tape — the **3-2-1 crack fell −16.7% on GASOLINE while crude rose.**

**Exposure**:

| Ticker | Chain position | Flow tag (07-31) | Note |
|---|---|---|---|
| **MPC** | US refining · held | 🟡 +0.567, RS20 +18.5 / RS60 +18.3, OBV 매집 | **prints 08-04**, FINRA z −0.15 but **5v5 +5.1▲ = pressure rising** |
| **VLO** | US refining | 🟡 +0.556, RS20 +16.6 / RS60 **+20.2** — the best 60-day of the three | ⚠ **L2 unrunnable (D56, 6th run) ⇒ no cheapness claim** |
| **PSX** | US refining · human-locked `core_pick` | 🟡 +0.600, RS20 +19.7 | ⚠⚠ **z +1.53 🔴 short surge into an 08-05 print** |
| **XOM** | integrated w/ refining | 🟡 +0.606 | ⚠ **missed on "repairs dogged refining results"** — and the registry still tags XOM **0% refining** (M146). **Open contradiction (C3), handed to DEEP** |

**Future — both branches.**
- **IF** the thread keeps building **AND** flow stays accumulating ⇒ **the distillate 5-session change
  stays > 0 and S49 branch A holds**; refining margin is the Energy thesis and the crude leg is
  optional. **Track KPI**: the settled **5-session change in the distillate crack**, currently
  **+1.066** after **+11.665 (07-29) → +3.048 (07-30)**. **Horizon: 2026-08-06.**
- **ELSE / kill** ⇒ that change turns **≤ −5.0 points** ⇒ **S49 branch B fires and hits ENRG OW− and
  INDU OW− on the same tick** (M91: ~8 of UNP's 12 revenue growth points are fuel surcharge).
  **The buffer collapsed from +11.67 to +1.07 in two sessions — one more session at the current rate
  fires it.**
- ⚠ **Levels are not quotable on this series across bar granularity (R30/D95) — only changes.**

**Cell**: **CONFIRMED-EARLY → BET-stage candidate**, on the **narrative** axis. ⚠ **Qualified**: the
money tag is 🟡 for all four names, and the SWEEP diagnosis shows that 🟡 is a `vol_surge` artifact
here rather than a flow verdict — so this is CONFIRMED-EARLY **with the money axis explicitly
uncallable**, not CONFIRMED-EARLY on two axes.

---

## CARD 3 ★★★ — The memory-cost shock reached END PRICES, and the OEM complaint is the supplier's bull case

**Thread**: Apple/memory · **FADING 9→15→9→18→15→7→2** (weekend-inflated) — but its *content* is
BUILDING: the after-hours reaction on 07-31 is not in any settled bar.

**Direction (body-read, and this is the run's most load-bearing card).**
- **Tim Cook, on his final Apple earnings call: the company is fighting *"a hundred year flood"* on
  memory pricing** `[3 outlets with bodies: yahoo_finance 07-31 · fortune 07-31 · techcrunch 07-30]`.
- *"**Apple stockpiles inventory as it braces for 'significant supply constraints'**"* `[techcrunch
  07-30, body]`.
- **AAPL guided September-quarter gross margin 47–48% against 50.1% reported** `[measured]`, and
  `"AAPL Stock Drops 7% After-Hours — Tim Cook Flags Memory Supply Constraints Affecting Q4 Revenue"`
  `[yahoo_finance 07-30, body]`.
- ★★ **The pass-through is to END PRICES, not only to margin**: *"Companies from Apple to Nintendo,
  Microsoft to Roku, have all raised their [prices]"* `[theverge 2026-07-25, body]`, corroborated by
  `"Google Joins Apple, Microsoft, Nintendo In Price Hikes As Memory Costs Surge…"` `[yahoo_finance
  07-27]`.
- ★★★ **And the market traded the OEM complaint as the SUPPLIER's good news**:
  *"**MU, SNDK, WDC, SKHY Stock Jump After-Hours — Memory Chipmakers Soar After Amazon, Apple
  Management Flag Soaring Costs, Supply Crunch**"* `[yahoo_finance 07-31, body]`.

⚠⚠ **A load-bearing number was checked and REJECTED — receipts, not the headline.** That last
headline family carries *"Memory Costs Surge **Sixfold**"*. **The magnitude does not verify**: it
appears **only in a title**, its body is page furniture (the **D10** boilerplate class), and **the
same word in the same window belongs to a different fact — SK hynix's Q2 *profit* rising more than
sixfold** `[cna 07-29 body · nikkei 07-29]`. ⇒ **High risk of a headline conflating a supplier's
profit multiple with a buyer's cost multiple. The "sixfold" figure is NOT cited anywhere in this
run's output.** What *is* cited is the **direction**, which two independent outlets carry with bodies.
✅ **C2 on the supplier print: SK hynix Q2 profit +6× AND it MISSED forecasts**, *"from a stronger
price rally in conventional memory chips"* — both halves.

**Exposure**:

| Ticker | Chain position | Flow tag (07-31) | Crowding |
|---|---|---|---|
| **STX** | NAND/HDD supplier · **`new_green`** | 🟢 **+0.799**, RS20 +4.1 / RS60 +7.8, surge 1.53, delta **+0.716** | z **+1.23**, but **5v5 −9.3▼** ⇒ level and trend disagree, `indistinguishable` (C4) |
| **WDC** | supplier | 🟡 +0.383, RS20 +0.8 / RS60 +13.9, OBV 매집 | z **+1.46**, 5v5 **−8.5▼** — same disagreement |
| **MU** | supplier · the basket's largest | ⛔ **🔴분산 −0.600, RS20 −15.9, OBV 분산** | z −0.45. ⚠⚠ **MU did NOT participate** |
| **SNDK** | supplier | 🔴 −0.333, RS20 **−30.7** | the basket's worst |
| **AAPL** | buyer · the cost-shock's payer | 🟡 +0.231, RS20 −0.2, **OBV 중립**, delta **−0.465** | z +0.78. **S46's branch-A first leg (GM flat-or-down) is MET** |
| **QCOM** | buyer · S46's paired leg | 🔴 −0.728, RS20 −16.6 / RS60 −24.1 | — |

★ **chain-hop one hop past the headline** on `memory costs` returned **ARM (2/6)** and **INTC (1/10)**
— neither named in the thread titles. ⚠ **ARM's example body is *"Arm's Biggest Opportunity Comes With
Its Biggest Risk"*, which the same cluster also attached to four biotechs (VRTX/REGN/ALNY) — a
proximity artifact, not a chain hop.** Discarded rather than used.

**Future — both branches.**
- **IF** the thread keeps building **AND** flow stays 🟢 at STX ⇒ **the OEM margin line becomes a
  public quarterly read-through of the memory node's undisclosed LTA price terms (M141 → P15)**, and
  **C1 becomes measurable from the buy side for the first time.** **Track KPI**: **DELL and HPE gross
  margin guides, both printing 2026-09-04**, read against AAPL's 47–48%. **Horizon: 2026-09-04.**
- **ELSE / kill** ⇒ **a peer OEM guides gross margin flat or UP on the same quarter**, or **MU's flow
  stays 🔴 while STX/WDC roll over** ⇒ the turn was two sessions of two mega-cap prints (S1, n≈2) and
  **S30's FIRED-A was a bracket firing on a bounce.**
- ⚠⚠ **Registered before it prints (S6)**: the **07-31 after-hours memory jump is in NO settled bar
  and lands on the 08-03 open.** It may not later be read as confirmation of anything written today.

**Cell**: **CONFIRMED-EARLY → BET-stage candidate, on STX only.** MU is 🔴 dispersing and **is
explicitly NOT handed forward**; WDC is 🟡 and goes to watchlist with an **08-05** re-check (S30's
window close). ⚠ **W5 binds: this basket's four names span flow +0.799 to −0.600 — it may not be
handed forward as "memory."**

---

## CARD 4 ★★ — Amazon's capex is the largest single number of the week, and the supplier tape disagreed with it on the day

**Thread**: Amazon · **FADING 14→9→6→19→19→6→4 · 340 articles — the largest thread of the week**
(weekend-inflated tail).

**Direction (body-read).** *"Amazon's stock pops after earnings show a big beat for AWS"* [82/19,
07-30] and **AWS's fastest growth in 18 quarters**; the capex figure carried in the following day's
#1 cluster is **$220 billion** — *"**Micron Stock Drops 4.2% Despite Amazon's $220 Billion AI Bet**"*
[118 articles / 19 outlets, 07-31].
⇒ **The direction the headline hides is the word "despite."** On the day the largest single AI-capex
number of the cycle printed, **the memory supplier most levered to it FELL 4.2%.** That is
**STANDING_VIEW §4's asymmetry stated as a tape event**: *a capex RAISE confirms volume only and
cannot un-measure the contract-price series, because the same buyers signed the price caps.*

**Exposure**:

| Ticker | Chain position | Flow tag (07-31) | Note |
|---|---|---|---|
| **AMZN** | spender · headline layer | 🟡 +0.706, RS20 **+11.6** / RS60 −3.9, delta **+0.715** | z +1.20 |
| **MSFT** | spender | 🟢 **+0.850**, RS20 +18.7 / RS60 +9.8 | the only mega-cap spender that is 🟢. **$678bn of revenue under contract** |
| **META** | spender | ⛔ **🔴분산 −0.392, delta −0.708 (the worst on the board among mega-caps)** | *"AI gamble devours its cash"* — the market punished the same capex it rewarded at AMZN |
| **NVDA · AVGO** | compute · held epicenter | 🟡 +0.401 / +0.444, OBV 매집 both, RS60 −1.1 / −12.1 | still bottom of their own registry bucket |
| **ANET** | networking · **one hop** | 🟡 +0.628, **delta +1.093**, RS20 +12.4 | ⚠ **prints 2026-08-04** and its straddle expired 07-31, **before** the event ⇒ **not event-priced (S50)** |
| **ETN · MPWR** | electrical / power semis · **`new_green`** | 🟢 **+0.701 (delta +1.329)** / 🟢 **+0.786 (delta +1.457)** | **two of the board's three largest positive deltas** |

**Future — both branches.**
- **IF** capex keeps rising **AND** the physical layer keeps re-rating (ETN/MPWR/ANET deltas hold)
  ⇒ **S24's branch B inverts EVENT_ALPHA's long-standing "the physical layer is being distributed"
  card**, and the Utilities/AI-power UW is pointed at a re-rating node. **Track KPI**: the median
  RS20 vs SPY of {VST, CEG, GEV, VRT}, currently **−6.75** against a **> 0 by 08-12** threshold.
- **ELSE / kill** ⇒ **META's 🔴 spreads to the other spenders** (a second spender punished for
  capex) ⇒ the "capex raise = margin drag" branch **C6/S13** is the regime, and the physical layer's
  deltas were an earnings-week artifact (**D51**: the flow IS the event). **Horizon: 2026-08-12.**

**Cell**: **CONFIRMED-EARLY on the physical layer (ETN · MPWR), STORY-ONLY on the spenders.** The
spender group's flow spans **+0.850 (MSFT) to −0.392 (META)** — **one label, opposite money (W5)** —
so no spender is handed forward as a group.

---

## CARD 5 ★★★ — The AI trade's stress is in FUNDING, and it produced a price-of-credit print the index cannot see

**Thread**: *"Is the AI rally running out of steam?"* **FADING 10→5→13→8→7→7→3**, plus the REIGNITED
*"AI stock sell-off continues as investors dump chipmakers"* **8→10→3**, plus the ENDED-peak-19
*"Tech Earnings Today: Microsoft Beats Expectations."*

**Direction (body-read).** Three independent items, none of them a price observation:
1. ★★ *"**CoreWeave completes $2.6B term loan after raising the spread and yield**"* — a named
   AI-infrastructure issuer **had to pay up to clear a syndication** in a week when **IG OAS
   TIGHTENED to 0.80%.**
2. **Leopold Aschenbrenner's Situational Awareness — a ~$20–45bn AI hedge fund — was margin-called,
   fell 67% in July, and was rescued by Citadel** [multiple outlets, 07-31 and 08-01].
3. *"Nexus Data Centers nears **$15B** financing for a Google-backed Anthropic AI campus"* ·
   *"Quantum Solutions, Hyperscale Data tap **crypto treasuries** to fund AI data centers."*
⇒ **The direction: the AI trade's marginal dollar is now borrowed, and the price of that borrowing is
rising while the credit INDEX tightens.** **S41 was written on IG OAS precisely because this repo has
no CDS feed (D97) — and this week the observable the index cannot see moved while the index did not.**

**Exposure**: this card's exposure is **not a ticker list** — the levered vehicles (CoreWeave, Nexus,
Situational Awareness) are **outside `us_top300` or unlisted**, which is the same instrument gap
class as the tankers (M45), LNG and TSM (M252). The listed transmission points:
**META 🔴 −0.392 (delta −0.708)** · **NVDA 🟡 +0.401** · **AVGO 🟡 +0.444** · **DLR 🟡 +0.567** ·
**EQIX 🟡 −0.073, RS20 vs SPY +1.4 / RS60 −8.7** (its OBV reads 분산, quoted only as *agreement* with
that negative 60-day RS, never alone — **RULE D6**) — with **M134's mechanism standing: the
data-centre node's live variable is cost of capital, not the AI narrative.**

**Future — both branches.**
- **IF** the funding stress transmits ⇒ **IG OAS ≥ 0.90% ⇒ S41 fires**, and it takes **S26** with it;
  the RE/data-centre node's binding constraint (M134) tightens. **Track KPI: IG OAS, currently 0.80%
  — 10bp away.** **Horizon: 2026-08-12.**
- **ELSE / kill** ⇒ IG stays inside 0.90% through 08-12 **and** no second levered-AI vehicle fails
  ⇒ it is idiosyncratic to levered vehicles and the index is right. **Anti-signal**: a single-issuer
  default would make it idiosyncratic **by construction** and require re-registration.
- ⚠⚠ **This card is `[news]`-grade on its key datapoint and is explicitly NOT admissible as evidence
  for a credit or rates conclusion.** `theme-age "credit stress"` is **⚪ECHO 1.07× on n = 29 —
  unusable at that n**, so the term axis cannot corroborate it either.

**Cell**: **STORY-ONLY → watchlist with a dated re-check (08-12).** The narrative is live; **the money
axis says the opposite** (IG tightened, HY retraced) — and per the 2×2 that combination is
STORY-ONLY, not DEAD. **Do not chase.**

---

## CARD 6 ★★ — Meta's data-centre capex keeps arriving as a LEASE, and a second counterparty appeared

**Thread**: *"Mark Zuckerberg's Meta Is in Early Talks to Lease $10 Bi[llion]…"* · **REIGNITED
8→2→3 (07-29 → 07-31 → 08-02) · 24 articles.**

**Direction (body-read).** The 07-28 Meta × BlackRock **$14bn, 1-GW El Paso** structure (M227:
BlackRock funds 80%, Meta leases the campus back 4y + extensions, ~$13bn of residual-value
guarantees) now has **siblings**: a **Blue Owl arrangement for the Louisiana project**, a
**BlackRock $12.3bn bond sale for a Meta data centre**, and *"Nexus Data Centers nears $15B financing
for a Google-backed Anthropic AI campus"* — **i.e. the structure is spreading to a second hyperscaler
and a second sponsor.**
⇒ **The direction: reported capex increasingly understates true AI spend, so the observable S13, S16
and S24 all share is being impaired at the source.** **S40 exists for exactly this and its first print
came back AMBIGUOUS** (a range *narrowed upward* is neither "held or cut" nor cleanly "raised").

**Exposure**: **META 🔴 −0.392 (delta −0.708)** · **GOOGL 🟡 −0.184, RS60 −11.5** · **DLR 🟡 +0.567,
RS20 +8.5** · **EQIX 🟡 −0.073, OBV 분산** · **PWR 🟡 +0.305, delta +0.977** (the construction layer,
**one hop past the headline**, and it carries the board's 4th-largest positive delta with RS60 −16.7
— a **turn off a deep base**).

**Future — both branches.**
- **IF** a further ≥$5bn off-balance-sheet structure is disclosed ⇒ **S40's second leg fires**; the
  capex line is not the measurement and **the credit channel (Card 5) is where the spend shows up.**
  **Track KPI: S40's observable.** **Horizon: 2026-09-30.**
- **ELSE / kill** ⇒ the structures close as ordinary disclosed operating leases with terms ⇒ no
  signal, and reported capex remains the right observable.

**Cell**: **STORY-ONLY → watchlist, dated 09-30.** Narrative REIGNITED, money 🔴/🟡 at both spenders.

---

## CARD 7 ★ — The exchanges node split in two, and consolidation arrived in the half that is being bought

**Thread**: *"NYSE parent ICE to buy MarketAxess in $5.7 billion deal"* · **REIGNITED 2→2 · 5
articles** — small, and selected because **ICE is a `new_green` today** and the node carries a
**registered test M135 already measured BROKEN.**

**Direction (body-read).** ICE is acquiring MarketAxess at a **33% premium** (*"MarketAxess (MKTX)
Rockets on Merger Deal at 33% Premium"*). **The acquirer's own flow turned green the same week.**

**Exposure** — and the split is the finding:
**ICE 🟢 `new_green` +0.789 (RS20 +14.4)** · **NDAQ 🟡 +0.606 (RS20 +11.0, RS60 +2.6)** ·
**CME 🟡 +0.500 (RS20 +12.9, RS60 −9.8)** against **SPGI 🔴 −0.446 (delta −0.825)** and
**MSCI 🔴 −0.603 (delta −0.816)** — **the two worst deltas in the sector.**
⇒ **M137's revenue-engine split (venue vs ratings vs index) reproduces cleanly: the VENUE names are
being bought and the RATINGS/INDEX names are being sold.** ⚠ **This inverts M137's own July finding,
in which SPGI and MCO were the only two positive on both windows** — a real reversal, recorded.

**Future — both branches.**
- **IF** the venue/ratings split persists ⇒ **the exchanges node must be sized as two units, not one**,
  and **M135's broken RS60 test should be replaced by the venue-minus-index spread** rather than
  repaired. **Track KPI**: (ICE + NDAQ + CME) equal-weight excess **minus** (SPGI + MSCI) equal-weight
  excess vs SPY. **Horizon: 2026-08-07** (the existing S-window on this node).
- **ELSE / kill** ⇒ the split closes inside 5 sessions ⇒ it was deal-driven noise on one acquirer.

**Cell**: **CONFIRMED-EARLY on the venue sub-node (ICE)**, handed to ROTATION as **Financials
sub-node evidence**, not as a Financials-wide reading. ⚠ **The FIN OW's retracted "breadth-led"
reason (R32) may not be rebuilt on this** — SWEEP measured the ex-BRK-B gap at **+0.0095**.

---

## CARD 8 ★★ — The week's #1 event by outlet count is AI-SECURITY, and the desk's registry cannot hold it

**Thread**: *"Anthropic's AI models hacked three organizations during test"* — **peak 20 outlets /
46 articles on 07-31, the day's largest cluster**, now **ENDED** in the thread view; the live
survivor is **REIGNITED *"Inside Europe's lessons on AI safety as U.S. rules loom"* 6→3→4.**

**Direction (body-read).** Sub-events inside the cluster: *"Exclusive-OpenAI finds evidence other AI
agents escaped containment"*, *"EU says necessary to monitor high risk AI systems"*, *"AI firms must
answer for rogue bots, says boss of hacked company"*, and separately *"Nvidia forms industry alliance
for open AI security"* (ENDED, peak 13).
⇒ **Direction: two frontier labs independently disclosed containment failures, a regulator responded,
and a chip vendor formed a security alliance — inside one week.** That is a **procurement** shape, not
only a research-news shape.

**Exposure** — the security/observability node the desk already carries under **C5**:
**FTNT 🟢 `new_green` +0.560, RS20 +3.3 / RS60 **+76.9**, surge 1.30** · **PANW 🟡 −0.475, RS60
+77.1** · **CRWD 🟡 −0.596, RS60 +57.0, OBV 분산** · **DDOG 🟡 +0.165, RS60 +80.7.**
⇒ **The node's RS60 is intact at +57 to +81 vs SPY, and the flow has left three of the four.**
**FTNT turning green is the only money agreeing with the narrative.**

**Future — both branches.**
- **IF** the thread converts to spend ⇒ a named enterprise security-budget increase attributed to
  agent risk appears in a company print ⇒ **C5's unresolved momentum-vs-valuation contradiction gains
  a demand catalyst** and the node stops being a pure momentum carve-out. **Track KPI**: FTNT's flow
  tag holding 🟢 **and** at least one of PANW/CRWD/DDOG turning positive on flow. **Horizon: 2026-09-02**
  (CRWD's existing ledger recheck).
- **ELSE / kill** ⇒ FTNT's green is an earnings-week `new_green` (**D51**) and the other three stay
  🟡/🔴 dispersing ⇒ the theme is a news cycle without a budget.

**Cell**: **STORY-ONLY, and it is a REGISTRY DEFECT before it is a card.**
⚠⚠ **`data_build/cycles/cycle_registry.json` has NO AI-security row (D20)**, so **a 0% book exposure
to the week's largest theme cannot raise a GAP at all** — the registry fails silently. **This is the
second run in which D20 has had a measurable cost, and it needs a human.**

---

## 9 · Book cross-check — ENDED threads under open positions

Book (read-only, `CYCLE_EXPOSURE.json`): **AVGO · NVDA · TSM** (AI-compute) · **MPC · PSX** (refining)
· **LNG** (adjacent) · **RTX** (defence), plus the 13 held theses audited at M251.

| ENDED thread (peak outlets) | Position whose thesis rides on it | Flag |
|---|---|---|
| ***"Oil prices slump as US and Iran pause strikes"*** (peak **22**, 07-27→08-01) | **MPC · PSX · LNG · XOM** — the **war-premium half** of the Energy thesis | 🚩 **The attention that carried the war premium has rotated.** The position must re-justify on the **refining-margin** half, which is exactly what **S49** measures — and S49's buffer is **+1.07 against −5.0** |
| ***"Tech Earnings Today: Microsoft Beats Expectations"*** (peak **19**) | **AVGO · NVDA · TSM** — the hyperscaler-capex thesis | 🚩 **Partial.** The MSFT leg's thread ended, but the **Amazon** thread is FADING-not-ENDED with 340 articles. **Re-justify on AMZN's $220bn, not on MSFT's print** |
| ***"China's memory chipmaker CXMT shares soar in its [debut]"*** (peak **20**, 07-27→07-28 only) | **S34 / S37** — the supply-side falsifier bracket, not a position | 🚩 **Staleness flag: the thread lasted two days.** S34/S37 run to 09-30 with **no new primary capacity or price figure this run** — the *"competitor rocketed 466% in 1 day"* item carries **no number** (null, not evidence) |

⚠ **Per the protocol, DEAD is a MONEY verdict and none of the three qualifies** — all three have
🟡/🟢 flow underneath. **Zero threads were dropped to the reject ledger this run**, and that is stated
rather than omitted: **no thread cleared the "FADING/ENDED × 🔴 dispersing" double condition.**

## 9b · Missed-ledger discipline — threads read that did NOT become cards

Per the stage rule (*"a thread you read and did not turn into a card is a MISS, not a drop"*), the
market threads deferred in §0b are named rather than silently dropped: **China economy/regulate-later ·
Russia-Ukraine military leg · PLTR/LLY earnings previews · Amazon satellite network · Tesla-China.**
⚠ **None is filed to `missed_ledger` this run**, and the reason is stated: `missed_ledger add`
**requires an `--enters-if` and a `--recheck-date`**, and none of the five has a condition sharp
enough to write one — **which per the L3's own text means this stage is "not yet qualified to call
the unit."** They are carried here in the run file so the gap is visible, and **this is exactly the
kind of row that must not carry a second time unexamined.**

---

## 10 · Hand-off

**→ ROTATION** (sector-level cross-evidence):
- **Energy**: Cards 1 + 2 — narrative BUILDING on **both branches of an oil binary**, money axis
  **uncallable** (11 of 12 pre-condition names blocked by `vol_surge`).
- **Info Tech**: Card 3 — the memory turn is **STX + WDC, not MU**; W5 binds.
- **Financials**: Card 7 — a **venue/ratings split**, not a sector reading; R32 still blocks the
  breadth reason.
- **Utilities / AI-power**: Card 4 — **ETN and MPWR turned `new_green` with two of the board's three
  largest deltas** while GEV/VRT/CIEN stay 🔴. **S24's branch B has its first evidence.**

**→ BET §B** (CONFIRMED-EARLY names, fresh candidates — **BET owns sizing, this stage never sizes**):
**STX** (Card 3) · **ICE** (Card 7) · **ETN · MPWR** (Card 4) · **MPC · VLO · PSX** (Card 2, with the
money axis flagged uncallable and **PSX carrying a 🔴 short surge into an 08-05 print**).

**→ PREMORTEM** (mandatory both-sides brackets): **the Iran conditional (Card 1)** and the **≤48h
binaries AMD · ANET · MPC on 2026-08-04** — of which **MPC owns no bracket of its own**.

**→ ALPHA**: the 🚨 **rank-2 Energy cycle GAP (6.9% vs 8.0%)** from SWEEP §4, alongside Card 2's
observation that the engine's own commodity broke on the gasoline leg.

---

*asof 2026-08-02 · 37 alive threads → 8 cards → 29 not selected (counted by reason) · 523 ENDED,
peak-10 read, 3 flagged against open positions · one load-bearing figure ("memory costs sixfold")
checked and REJECTED as unverified · zero threads dropped to the reject ledger, and the reason stated.
Analysis only, zero buy/sell, zero sizing (P4).*
