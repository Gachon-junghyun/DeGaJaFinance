# EVENT_ALPHA — industry_US · 2026-08-14 · Stage 5/11 (L1·EVENT_ALPHA)

> Bottom-up complement to MACRO's matrix: **which stories are BUILDING, and is money already
> following them.** Scope **`--scope foreign` on every call** (US desk, market-locked).
> Flow tags asof **2026-08-13 settled** (`SECTOR_FLOW_US.json`). **This stage never sizes (P4).**

## §0 · Selection log — no silent truncation

`thread --date 2026-08-13 --days 7 --scope foreign`. Per-day denominator: **08-07 720 · 08-08 283 ·
08-09 289 · 08-10 787 · 08-11 798 · 08-12 756 · 08-13 725.** 4,358 daily events → 3,389 threads,
**522 multi-day of which 214 ALIVE**.
⚠ **The 08-13 terminal date is deliberate.** Run on today's date the same command returns **214 → 0
alive** because 08-14 has no articles yet at this clock — a window-end artifact that would have made
every thread read `ENDED` (`MACRO_REPORT.md §D-2`).

**214 alive → 8 selected · 206 not selected** (counted, not truncated). Selection rule: precursor-form
first (curve opening ≤2 outlets and climbing), then remaining BUILDING by peak.

🚨 **One intended card was KILLED BY A QUERY-FORM DEFECT and is not fabricated.** The precursor thread
*"A huge day and week for **Corning** as the S&P 500 approaches…"* (**2→3→5→9**, textbook precursor
shape) could not be body-read: `fts search Corning` returns **252 hits and the top BM25 results are
`CORN Crosses Above Key Moving Average`, `Corn Feeling Modest Pressure`, `Corn Ticking Higher`** — the
index stems `Corning` into `Corn` (agricultural futures). **Second query-form defect measured today**
(after `Frontline`, `HANDOVER.md §10`) ⇒ registered **`D262`**. The optical layer is covered instead
by **Card 6**, built from tickers rather than from a company-name string.

✅ **And the L1's own rule paid**: `Microsoft AI chip` as one quoted phrase returned **0 hits**;
the same terms **as separate argv** returned **419**. A quoted multi-word bucket silently returns ~0 —
Card 2 exists only because that rule was applied.

---

## §1 · FORWARD CARDS

### Card 1 — ★★★ The memory shortage reached the CHECKOUT COUNTER, and the market is punishing the pass-through

- **Thread**: *Apple / soaring memory costs* — **BUILDING 7 days, outlets 2→3→3→7→5→5→7, 115 articles**
  · window denominator 4,358 events / 3,389 threads. **Precursor form: opened at 2 outlets.**
- **Direction (body-read, not headline)**: the shortage has stopped being a supplier story and become
  a **consumer price event at two separate handset makers in one week** —
  *"**Apple Already Increased the Price of iPhones Up to $300.** Their Price Hikes Might Be Just
  Starting."* [`yahoo_finance` 08-11] · *"**Google Raises Pixel 11 Prices by $100**"* [`yahoo_finance`
  08-12] · *"**Alphabet stock slides as Google hikes Pixel 11 prices**"* [`yahoo_finance` 08-12] ·
  *"Apple (AAPL) Downgraded as **Soaring Memory Costs** Test iPhone…"* [40 articles/7 outlets, 08-10] ·
  *"Jefferies downgrades Apple stock to **sell**"* [`yahoo_finance` 08-11].
  ★ **The headline says "memory costs"; the body says the equity market is marking down the company
  that RAISED price.** That is a demand-destruction read, not a cost read.
- **Exposure** (flow tags asof 2026-08-13):

| Ticker | Chain position | Flow tag | Crowding / note |
|---|---|---|---|
| `MU` | supplier — DRAM | 🟡중립 flow −0.004 · RS20 **+7.7** · RS60 **+34.1** | **Δflow +0.585 — the largest positive delta of any name in this card** |
| `SNDK` | supplier — NAND | 🟡중립 flow +0.057 · RS20 +4.7 · RS60 +9.3 | **Δflow +0.757 — the largest in the whole exposure map** |
| `WDC` | supplier — NAND/HDD | 🟡중립 flow −0.029 · RS20 +0.8 | **Δflow +0.510** |
| `AAPL` | **buyer** (headline layer) | 🔴**분산** flow −0.715 · **RS20 −12.0** · OBV 분산 | headline-layer name **by construction**; the crowded side |
| `GOOGL` | **buyer** | 🟡중립 flow −0.562 · RS20 −5.9 · **RS60 −18.1** | Δflow +0.252 |

  ⇒ ★★ **The three suppliers carry the three largest positive flow deltas on this card while both
  buyers are negative on RS20 and one is outright 🔴 distributing.** The money is on the supplier side
  of the pass-through, and it moved before this week's price headlines.
- **Future — both branches, mandatory**:
  - **IF the thread keeps building AND supplier flow stays positive** → the memory cycle's
    *second-derivative deceleration* (this desk's carried regime call) is **wrong about timing**: an
    industry passing $300 of cost to consumers is not a decelerating price cycle.
    **Track KPI**: `MU` RS20 vs SPY **and** `MU` FY revision breadth, at the **2026-08-21** settle.
    **Horizon: 2026-08-21.**
  - **ELSE — kill condition**: **if `MU`'s Δflow turns negative AND `AAPL` RS20 vs SPY recovers above
    −5.0 by 2026-08-21**, the pass-through is being absorbed and this card is dead.
- **Cell**: **CONFIRMED-EARLY (supplier leg) · LATE-MONEY (buyer leg)** ⇒ **handed to ROTATION and BET
  §B as `MU`/`SNDK`/`WDC`. `AAPL`/`GOOGL` are the crowded headline layer and are NOT handed forward.**
- ⚠⚠ **Direct tension with this run's own MACRO §D-3**, stated rather than reconciled away: the term
  sweep has **`memory` 0.81× · `DRAM` 0.79× · `HBM` 0.60× · `AI capex` 0.40× — all decelerating.**
  **The narrative about memory is fading while the price effect is arriving at the till.** Both are
  measured; this card asserts only that the second one is dated and the first one is a share-of-voice
  statistic. **C4: this does not resolve which leads.**

### Card 2 — ★★★ Maia 300: a NAMED, DATED, UNIT-COUNTED in-house chip, and the book is long both sides of it

- **Thread**: *Microsoft AI silicon* — **BUILDING 7 days, outlets 7→4→2→6→7→5→9, 135 articles**
  (troughs at 2 mid-week then climbs to 9 — a re-ignition, not a fresh birth).
- **Direction (body-read)**: this is not "Microsoft likes AI" — it is a **product with a date and a
  volume**: *"Microsoft to unveil **Maia 300** AI chip this fall, **targets 300,000 units**"*
  [`yahoo_finance` 08-10] · *"Microsoft could unveil Maia 300 **as early as September**"*
  [`economictimes` 08-11] · *"Microsoft **Plans Production Boost** for AI Chips"* [`yahoo_finance`
  08-10]. ★ **And the chain hop is named for us**: *"Microsoft New AI Chip Could Be a **Big Win for
  Marvell and TSMC**"* [`yahoo_finance` 08-11]. Corroborating the same direction from a second buyer:
  *"**Anthropic** Enters The AI Chip Race With In-House Chip Team"* [`yahoo_finance` 08-06].
- **Exposure**:

| Ticker | Chain position | Flow tag | Crowding / note |
|---|---|---|---|
| `MRVL` | **custom-ASIC beneficiary** (named) | 🟡중립 flow +0.378 · OBV **매집** · RS20 +14.4 · RS60 **+26.2** | **Δflow +0.291**; not a headline-layer name |
| `AVGO` | custom-ASIC incumbent · **HELD** | 🟡중립 flow +0.406 · OBV 매집 · RS20 +8.0 · **RS60 −6.0** | **Δflow +0.300** |
| `MSFT` | the buyer | 🟡중립 flow +0.472 · OBV 매집 · **RS20 +20.3** | headline layer |
| `NVDA` | **merchant GPU — the displaced layer · HELD** | 🟢가속 **DISQUALIFIED** (`SWEEP_READ §2`: its green needs the revoked velocity axis; `vol_surge` 0.76) · RS20 +5.0 · **RS60 −4.0** | ⚠ read as **🟡** this run |
| `TSM` | foundry (named beneficiary) | ⛔ **NOT IN `us_top300` — cannot be tagged on any axis (G5)** | absence of a tag is not absence of a move |

  ⇒ ★★★ **The book holds `NVDA` (displaced) and `AVGO` (beneficiary) simultaneously.** This card
  **cannot be expressed by the book's current construction** — any outcome hits one holding and helps
  the other. **That is the finding**, and it is the object `S81` (→08-27) already brackets.
  ⚠ **`NVDA` RS60 −4.0 vs `MRVL` RS60 +26.2**: the displacement is **already in the 60-day tape**.
- **Future — both branches**:
  - **IF Maia 300 launches in September at anything near 300k units** → the AI-compute epicentre's
    **share** shifts to custom silicon; `MRVL`/`AVGO` RS60 leadership over `NVDA` persists.
    **Track KPI**: [`MRVL` RS60 − `NVDA` RS60] vs SPY, currently **+30.2pp**, at the **2026-09-15**
    settle. **Horizon: 2026-09-15** (the launch window the reports name).
  - **ELSE — kill condition**: **if that spread narrows below +10pp by 2026-09-15, OR the Maia 300
    unveil slips past September without a restated unit target**, the displacement thesis is dead and
    the merchant layer keeps the share.
- **Cell**: **CONFIRMED-EARLY** ⇒ **`MRVL` handed to ROTATION/BET §B as a fresh name.** `MSFT` is
  headline-layer and is not handed forward. `TSM` is flagged as an **un-taggable** exposure, not a
  candidate.
- ⚠ **`NVDA` prints 2026-08-26 (D-12)** and is bracketed by `S79`/`S81`. **This card's kill date sits
  AFTER that print by design** — the print is a level event, the displacement is a share event.

### Card 3 — ★★★ The crack has a NAMED physical cause and it is still firing

- **Thread**: *Ukraine drone strikes on Russian refining* — **BUILDING, outlet curve
  12→11→16→13→16→15, flat-to-rising**, inside the Ukraine cluster [32 articles/15 outlets].
- **Direction (body-read)**: named facilities, named capacity, and it **continued into 08-14** —
  *"Ukraine Strikes Gazprom's **200,000-Bpd Salavat Refinery** in the Urals"* [`oilprice` 08-13] ·
  *"Ukraine's drones hit a major Russian refinery **800 miles from the border**, sparking a fire"*
  [AP via `google_en` 08-13] · *"**Drone Strike Sparks Blaze at Key Russian Oil and Fuel Terminal**"*
  [`oilprice` **08-14**] · *"Kyiv hit as Ukraine targets Russian refineries and shadow fleet"*
  [`investing_en` 08-08].
  ★ **This is the supply-side mechanism MACRO §C-3 measured from the price side**: 3-2-1 crack
  **59.34 → 65.84 (+6.50 points / 5 sessions)** with **products outrunning crude** (HO +9.50% vs
  CL +5.12%). **Two independent instruments, one mechanism.**
- **Exposure**:

| Ticker | Chain position | Flow tag | Crowding / note |
|---|---|---|---|
| `MPC` | refiner · **HELD** | 🟢**가속** flow +0.811 · OBV 매집 · RS20 **+12.9** · RS60 **+32.0** · `vol_surge` **1.26** | ✅ **the only admissible 🟢 in the entire book** (`SWEEP_READ §2`) |
| `PSX` | refiner · **HELD** | 🟡중립 flow +0.637 · OBV 매집 · RS20 +11.9 · RS60 +24.1 | 🚨 **🟡 only because `vol_surge` 1.04 < 1.2** — filtered out of its own sector's shortlist |
| `VLO` | refiner | 🟡중립 flow +0.639 · OBV 매집 · RS20 +10.6 · RS60 **+27.3** | 🚨 same artifact, `vol_surge` **0.95** |
| `XOM` | integrated | 🟡중립 flow +0.397 · RS20 **+5.1** · **RS60 −6.5** | **Δflow −0.247** — yet `XOM` is **30.5% of the sector's cap weight**, i.e. it owns `wflow` |

  ⇒ **The three refiners lead on both RS windows and the integrated that owns the sector's `wflow`
  has the worst delta on the card.** `SWEEP_READ §3` reached this from the flow side independently.
- **Future — both branches**:
  - **IF the strikes continue AND the crack holds ≥63** → the ENRG strength is **physical margin, not
    war premium** (P58 direction A), and the expression is refiners rather than integrateds.
    **Track KPI**: 3-2-1 crack level **and** [median{MPC,PSX,VLO} RS20 − `XOM` RS20], currently
    **+6.8pp**, at the **2026-08-19** settle (`S75`).
  - **ELSE — kill condition**: **if the crack falls ≥5 points while crude holds ±3%**, the margin
    story is over regardless of the strikes (this is P58's own anti-signal (b), deliberately shared so
    the two objects cannot disagree silently).
- **Cell**: **CONFIRMED-EARLY** ⇒ `VLO` handed to ROTATION/BET §B as the **un-held** expression;
  `MPC`/`PSX` are already held and are handed as **thesis-confirmation**, not as new candidates.
- ⚠⚠ **`R47` binds: no stage may state "the distillate bottleneck released" as fact** — `S55` scored C
  and the physical-vs-premium split is **still unseparated.** This card adds a *cause*, not a *split*.

### Card 4 — ★★ The optical/interconnect layer turned on 20 days while still negative on 60

- **Thread**: no clean single thread — assembled from tickers because the company-name route is broken
  (§0, `D262`). Adjacent live evidence: *"Lumentum, CoreWeave, SMCI, and More Stocks That Explain…"*
  [28 articles/5 outlets, 08-12] inside a **BUILDING 6-day** thread.
- **Direction**: the layer's **20-day and 60-day windows disagree in sign across all four names** —
  a fresh turn inside a drawdown, which is the early shape rather than the crowded one.
- **Exposure**:

| Ticker | Flow tag | RS20 | **RS60** | Note |
|---|---|---|---|---|
| `COHR` | 🟢가속 flow **+1.000** (the universe's maximum) · `vol_surge` **1.77** | **+14.5** | **−15.1** | ✅ 3-axis green, **admissible** |
| `LITE` | 🟢가속 flow +0.844 · `vol_surge` 1.32 | **+21.0** | **−5.8** | ✅ 3-axis green, **admissible** |
| `CIEN` | 🟡중립 flow +0.273 | +10.3 | **−20.9** | **Δflow +0.622 — 2nd largest on the whole board** |
| `GLW` | 🔴**분산** flow −0.592 · OBV 분산 | −3.5 | −16.5 | ⚠ **the name whose thread was the precursor is the one the money is LEAVING** |

- **Future — both branches**:
  - **IF the 20-day leadership holds while RS60 turns positive** → this is a genuine new leg of the
    AI-compute build-out (the interconnect layer), and it is **the layer the book has zero exposure
    to**. **Track KPI**: `COHR` and `LITE` RS60 vs SPY crossing above 0, at the **2026-09-30** settle
    (`S48`, the desk's registered bracket on exactly this layer).
  - **ELSE — kill condition**: **if either name's RS20 falls below +5 before RS60 crosses zero**, the
    turn was a bounce inside a downtrend and the card dies.
- **Cell**: **CONFIRMED-EARLY (COHR · LITE) · DEAD-on-money (GLW)** ⇒ `COHR`/`LITE` handed forward.
  ⚠ **`GLW` is a MONEY verdict**: 🔴 dispersing **and** negative on both windows — both axes, so the
  DEAD call is legitimate rather than a story judgement. Filed to the rejection ledger below.

### Card 5 — ★★ The Fed's hike premium is trading as an OIL derivative (macro card — no name exposure)

- **Thread**: *Fed inflation path* — **BUILDING 7 days, 6→3→3→6→7→8→8, 194 articles = the largest
  thread on the board**; and *Dollar/FX* — **BUILDING 5→3→6→6, 125 articles**.
- **Direction (body-read)**: *"Fed's Barkin: still an **'open question'** if rate hike will be
  needed"* [Reuters via `google_en` 08-13] · *"**Hammack backs increase** on inflation concerns"*
  [`economictimes` 08-13] · *"Fed's Goolsbee: Inflation is the **'biggest problem'**"* [28/7, 08-11] ·
  ★ **the coupling** — *"**Traders Pare Bets on Fed Rate Hike This Year as Oil Prices Fall**"*
  [`bloomberg` 08-13] and *"Dollar treads water as **Fed hike bets pared on benign US** data"*
  [30 articles/6 outlets, 08-13].
- **Exposure**: **deliberately none.** This is a *wind*, not a chain — the term `rate hike` is
  **2.79× accelerating against `rate cut` at 2 hits** (MACRO §D-3) and the correct consumer is the
  transmission matrix, not a name list. ⚠ **Any single-name expression here would be fabricated.**
- **Future — both branches**: identical to **P57** (MACRO §E) and deliberately **not re-registered** —
  duplicating a proposition into a card is how one object becomes two scoreboards.
- **Cell**: **hand-off to ROTATION as macro cross-evidence only. NOT a BET candidate.**

### Card 6 — ⚠ European power stress: real, physical, and **not expressible in this desk's universe**

- **Thread**: *European extreme heat / power* — head cluster **17 articles/12 outlets**, plus
  *"Romania **shuts nuclear plant**, Hungary dams dry Danube River"* [8/8, 08-13].
- **Direction (body-read)**: *"**When extreme heat threatens Europe's nuclear power**"* [`dw` 08-10] ·
  *"**Europe's economy shrivels** as heatwave grips the continent"* [`semafor` 08-13] ·
  *"France will test crisis response with a **2027 blackout drill**"* [`politico` 08-07].
- **Exposure**: 🚫 **NONE THAT THIS DESK CAN MEASURE.** The universe is `us_top300`; the affected
  assets are European utilities. ⚠ **W1 forbids the transfer** — "European thermal derating" is not a
  US-utility signal, and the US utility complex reads **0🟢 / 9🔴 of 15, `wflow` −0.491** in the
  opposite direction.
- **Future**: **kill condition instead of a scenario** — *if a US grid operator (ERCOT/PJM/MISO) issues
  an emergency alert before **2026-08-28**, this stops being a European story and gets a real card.*
- **Cell**: **STORY-ONLY** ⇒ watchlist with a **dated re-check 2026-08-28**. **Explicitly NOT handed
  to the candidate list.**

### Card 7 — ★★ Hormuz / Red Sea: the ≤48h binary, handed to PREMORTEM rather than carded

- **Thread**: *Iran war / Hormuz* — **BUILDING 5→4→5→7→10**; and *US strikes on Houthis* —
  **BUILDING 4→4→5**. Term share **`Hormuz` 1.07× (flat, 327 hits)** while **`Iran` is 0.77×
  (decelerating)**.
- **Direction (body-read)**: the *deal* thread is decaying (**15→9→7→6→5→4**) while the *physical*
  condition is not — *"Running The Hormuz Gauntlet: Recruitment Ad Offers Tanker Crews **Double Pay**
  To Brave Drone Strikes"* [`zerohedge` 08-13] · *"**Black Sea Oil Tanker Rates Surge to Record** on
  Drones Barrage"* [`bloomberg` 08-12] · *"US strikes targeting Houthis killed 153 civilians"*
  [6/5, 08-13] · yet the day's **largest event of all** was *"Oil prices **cool** despite US-Iran
  deadlock"* [44/17] with **OPEC cutting its 2026 demand forecast**.
  ⇒ ★ **`R67` reproduced exactly: attention rotated, the object did not.**
- **Exposure**: `MPC`/`PSX`/`VLO` (Card 3) · `INSW` — ⚠ **`INSW` is outside `us_top300` and carries no
  flow tag (G5)**; its ledger row moved to **`entered`** this run on the body-proximity leg
  (`HANDOVER.md §10`), **which is a ledger state, not a card.**
- **Future**: 🚫 **This card deliberately registers NO branches.** `catalyst_calendar` flags the
  Hormuz-reopening statement as an **undated 🔀 binary**, and the protocol requires **PREMORTEM
  (stage 7) to produce the both-sides bracket.** Writing branches here would pre-empt the stage that
  owns the requirement. **Handed forward as the mandatory binary.**
- **Cell**: **hand-off to PREMORTEM.**

### Card 8 — ⚠ Consumer Discretionary is the only sector where short pressure is actively LEAVING

- **Thread**: *"Why Netflix Stock Rallied Today"* — **BUILDING 5→2→3→7**; and the retail/consumer
  thread *"Why Target (TGT) Outpaced the Stock Market Today"* — **BUILDING 5→4→6→5→5→10, 134 articles**.
- **Direction (body-read)**: mixed and **not confirmatory** — *"Netflix Is Down **42% From Its High**.
  Here's Why I'm Buying"* [11/5, 08-10] and *"Netflix: **I Underestimated The Sector Trend And
  Cannibali[sation]**"* [2/2, 08-11] point **opposite ways within the same thread**.
- **Exposure**: the sector, not a name — `XLY` is the board's **only 🟢 FINRA short-covering signal**
  (z **−1.61**, 5v5 **−9.3▼**) while its `wflow` is **−0.416** and exc20 **−2.672**.
- **Future — both branches**: **IF** `XLY`'s short z stays below −1.0 **and** exc5 turns positive by
  **2026-08-21** → the covering is accumulation and the sector's negative flow is stale.
  **ELSE — kill**: if exc5 is still negative on 08-21 with z back above −0.5, the covering was
  mechanical (expiry/hedge unwind) and means nothing.
- **Cell**: **STORY-ONLY** — the body-read **contradicts itself**, so no name is handed forward.
  ⚠ Recorded because **an un-carded thread that cleared the money axis is a MISS, not a drop** (§2).

---

## §2 · Ledger writes — drops and misses both get a scoreboard

**Rejection ledger (a DROP — money verdict on BOTH axes):**
- **`GLW` Corning** — `C.차트붕괴` — 🔴분산 (OBV 분산 −0.10) **and** negative on both windows
  (RS20 −3.5 / RS60 −16.5) while its own thread was the week's cleanest precursor shape (2→3→5→9).
  **`--revives-if`**: `GLW` OBV state returns to 매집 **AND** RS20 vs SPY > 0 · **recheck 2026-09-04.**

**Missed-entry ledger (threads that cleared the money axis and did NOT become candidates):**
- **`MSFT`** — `M.숏리스트탈락` — OBV 매집, **RS20 +20.3**, but it is the **buyer/headline layer** of
  Card 2 and this stage hands forward the chain, not the headline.
  **`--enters-if`**: `MSFT` RS20 vs SPY > 0 **AND** the Maia 300 launch is confirmed by a company
  source (not a report) · **recheck 2026-09-15.**
- **`XLY` complex** — `Q.확신부족` — the only short-covering signal on the board, dropped because the
  thread's own body-read is self-contradictory. **`--enters-if`**: `XLY` exc5 vs SPY > 0 **AND** FINRA
  short z still ≤ −1.0 · **recheck 2026-08-21.**

## §3 · Book cross-check — positions whose thesis rides on a thread that has stopped

| Held name | Thesis thread | State | Flag |
|---|---|---|---|
| **`MET`** | life-insurer / rate-sensitive | **no live thread found in the 214 alive set** | 🚨 **`S69` fired branch A today** (RS20 **+0.406** vs a ≤+2.53 line) **and** its FY revision breadth is **still net-down (30d 5↑/9↓)**, **and** its Δflow is **−0.174**. **Three independent axes now point the same way and there is no narrative supporting the position.** Flagged to the book desk to **re-justify on something alive** |
| **`NDAQ`** | exchanges / volatility | no live thread | ⚠ **Δflow −0.288 = the book's worst**; flow −0.315, RS20 −0.1. `S59` scored **C** on 08-13 (underperformed `XLF` by 2.07pp but inside band). **Re-justify or retract** |
| **`NVDA`** | AI-compute epicentre | **alive but INVERTED** (Card 2) | ⚠ the live thread on this name's theme is about **its customer building a substitute**. Position is not flagged for exit — flagged because **its 🟢 tag is disqualified** and its **RS60 is −4.0 vs `MRVL` +26.2** |
| `MPC` · `PSX` | refining | **alive and building** (Card 3) | ✅ thesis confirmed by an independent physical mechanism |
| `AVGO` · `ANET` · `HPE` · `ETN` · `RTX` · `NUE` | — | alive / neutral | no flag |

## ✅ EXIT CHECK

- [x] **Scope market-correct** — `--scope foreign` on every `thread` / `fts search` / `brief` call.
- [x] **Selection logged**: 214 alive → **8 selected · 206 not selected** (counted). One further card
      **killed by a named query-form defect** rather than fabricated (`D262`).
- [x] **Every card has a direction body-read** with quoted evidence and a dated source. Card 1's body
      read **reversed** the headline's implication (cost story → demand-destruction/pass-through
      story); Card 8's body-read **contradicted itself** and the card was demoted for that reason.
- [x] **Every exposure name carries a flow tag with asof 2026-08-13**; names outside the universe
      (`TSM`, `INSW`) are marked **un-taggable (G5)** rather than given a tag.
- [x] **STORY-ONLY names did not leak into the hand-off** — Cards 6 and 8 hand forward nothing.
- [x] **Both branches + kill condition + dated horizon on every card that registers a future**
      (Cards 1·2·3·4·6·8). Cards 5 and 7 register none **by design** and say why (duplication of P57;
      PREMORTEM owns the binary).
- [x] `EVENT_ALPHA.md` written · CONFIRMED-EARLY handed to ROTATION/BET (**`MU` `SNDK` `WDC` `MRVL`
      `VLO` `COHR` `LITE`**) · ENDED-thread book flags emitted (§3) · ledger rows specified (§2).

⚠ **The disqualified-green rule from `SWEEP_READ §2` is applied throughout this file**: `NVDA` and
`CVX` appear as 🟡, not 🟢.
