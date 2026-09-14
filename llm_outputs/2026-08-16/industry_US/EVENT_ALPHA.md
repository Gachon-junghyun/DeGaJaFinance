# EVENT_ALPHA — industry_US · 2026-08-16 · Stage 5/11 (L1·EVENT_ALPHA)

> Bottom-up complement to MACRO's transmission matrix. **Which stories ARE building, and is money
> already following them.** `--scope foreign` on every news call (hard rule). Flow tags are `asof
> 2026-08-14` from `SECTOR_FLOW_US.json` — the last settled close — and every one is stated as such.
> No sizing (P4); BET owns that.

## §0 · Selection log — and the instrument defect that changed how selection was done

`thread --days 7 --scope foreign`: **4,286 daily events → 3,305 threads → 539 multi-day → 52 alive.**
**52 alive → 8 selected → 44 not selected** (no silent truncation).

🚨 **The `thread` tool's ranking could not be used this run, and the reason is measured.** Its longest
`BUILDING` chains are **syndicated evergreen column templates**, not stories:
*"Airbnb vs. McDonald's → Booking vs. Celsius → Adobe vs. AppLovin → Amazon vs. Comcast → Arista vs.
Intel → Reddit vs. Snowflake"* — **6 days, 89 articles, tagged BUILDING**, one publisher's recurring
format. Three more chains of the same shape rank in the top ten (`"X vs Y: Which Stock Is a Better
Buy"`, `"Here's How Much Money You'd Have..."`, `"3 [Sector] Stocks That..."`).
⇒ **Selection was done on substance from `brief` + the term sweep + targeted body searches, and the
`thread` tags are reported as curves only, never as evidence.** This is stated rather than silently
worked around.

⚠ **A second selection constraint, from PREFLIGHT**: the window contains **two weekend days** (08-15
events 269, 08-16 **112**, against a weekday norm near 780 — a **6.6× collapse**). **No thread is
called FADING or DEAD on curve shape inside this window.** A card may only be killed on the **money**
axis, which is what the L1's own rule requires anyway.

---

## Card 1 — ★★★ Ukraine is destroying Russian refining capacity, and there is a NAMED political off-switch

| | |
|---|---|
| **Thread** | Russian refining under drone attack · **REIGNITED/BUILDING** · 5 dated strikes in 6 days · `refinery` term velocity **1.33× = fastest of the 16-term sweep** (7d 354 / 30d 1,140) |
| **Denominator** | Foreign pool 7d = **35,627 articles**; ⚠ title+summary recall on this axis measured at **39.1%** — **60.9% body-blind** |

**Direction (body-read, not headline).** Physical capacity destruction, escalating, with a supply
consequence already visible in Russia's own behaviour:
- **08-10** *"Ukraine drone strike on oil refinery deep inside Russia kills at least 13"* [`guardian`]
- **08-11** *"Ukraine Drone Attack Hits Major Oil Refinery Deep Inside Russia"* [`oilprice`]
- **08-13** *"Ukraine Strikes Gazprom's Salavat Refinery"* — **200,000 bpd, Urals** [`oilprice` + `bloomberg`]
- **08-14** *"Drone Strike Sparks Blaze at Key Russian Oil and Fuel Terminal"* [`oilprice`]
- **08-14** *"Russia admits new petrol shortages amid ongoing long-range Ukrainian strikes"* [`euronews`]
- **08-12** *"Russia Imports Indian Fuel as Refinery Crisis Deepens"* [`oilprice`] — ★ the importer/exporter inversion
- **08-13** *"Russia's Diesel Exports Crash to Multiyear-Low amid Tight Global Market"* [`yahoo_finance`]

⚠⚠ **The other half, and it is not buried (C2):** **08-12 — *"Kyiv stops strikes on Russian port after
request from JD Vance"*** [`semafor`]. **A named US actor is already braking this exact mechanism.**

**Exposure** (chain position · flow tag `asof 2026-08-14` · crowding):

| Ticker | Chain position | Flow | Crowding / note |
|---|---|---|---|
| **`MPC`** | Refining — direct crack beneficiary | **🟢가속** (flow +0.806 · OBV 매집 · RS20 +9.3 · RS60 **+29.3** vs `SPY` · surge 1.25) | ✅ **FINRA clean-rise, short z −0.71.** The sector's **only admissible 🟢** (3-axis producible) |
| **`PSX`** | Refining | 🟡중립 (+0.628 · OBV 매집 · RS20 +8.5 · RS60 +22.3) | ⚠ 🟡 **on `vol_surge` 1.01 alone** — `D251`: a sector leader filtered out of its own shortlist |
| **`VLO`** | Refining | 🟡중립 (+0.490 · OBV 매집 · RS20 +5.9 · RS60 +24.3) | ⚠ same — `vol_surge` **0.84** |
| `XOM` | Integrated — **0% refining exposure** (`M146`) | 🟡중립 (+0.244 · OBV 중립 · RS60 **−7.3**) | **Headline layer.** The 36-point RS60 spread between refiners and integrateds is the whole card |
| `CVX` | Integrated | 🟢가속 (+0.401) | ⚠ **Velocity-produced green** (`vol_surge` 0.95) — **not admissible** as an ignition |

**Future — both branches, dated.**
- **IF the thread keeps building AND flow stays 🟢** → the distillate leg widens further: `HO=F` 20-day
  return exceeds `CL=F` 20-day by **> +4pp** at the **2026-08-21** settle, and at least one further
  **dated** strike on Russian refining capacity appears in the foreign corpus. **KPI**: `HO=F` − `CL=F`
  20d gap; refiner-vs-integrated RS60 spread vs `SPY`. **Horizon 2026-08-21.**
- **ELSE (kill)** → the gap closes to **≤ 0pp**, **OR** a US-brokered halt to strikes on Russian energy
  infrastructure is reported by **≥3 independent outlets**. The `semafor` item is branch B's first
  datapoint, already on the board.
- 🚨 **VOID condition**: a US refinery outage or a PADD3 hurricane landfall inside the window makes
  distillate strength a domestic-supply artifact.

**Cell: CONFIRMED-EARLY** (story building × money 🟢 on `MPC`). → **ROTATION** as Energy cross-evidence;
**BET §B** may treat `MPC` as a fresh candidate. `PSX`/`VLO` hand forward as **filtered-out leaders**,
not as fresh greens.
⚠ **`P66` in MACRO §E is this card's registered form.**

---

## Card 2 — ★★★ Microsoft is building its way off Nvidia, and the desk's cycle registry has no row for it

| | |
|---|---|
| **Thread** | Microsoft custom AI silicon · **REIGNITED** · 6 days · outlet curve **6→7→5→10→4→5** · **132 articles** · peak **10 outlets 08-13** |

**Direction (body-read).** Vertical integration away from merchant GPUs, with a unit target and a date:
- **08-10** *"Microsoft to unveil Maia 300 AI chip this fall, **targets 300,000 units**"* [`yahoo_finance`]
- **08-10** *"Microsoft Plans to Ramp Up Homegrown AI Chip Production **Next Year**"* [Market Chatter]
- **08-11** *"Microsoft could unveil **Maia 300** AI chip as early as **September**"* [`economictimes`]
- ★ **08-10 — *"Microsoft Rethinks Its Nvidia Reliance"*** [`yahoo_finance`] — the headline states the direction outright
- ★ **08-11 — *"Marvell Could Be Next Winner in Microsoft AI Bet"*** [`yahoo_finance`] — the named beneficiary

⚠ **Sourcing grade is `[news]`, not primary.** Every item traces to *"The Information, Report Says"* —
**no Microsoft filing or press release is in the corpus.** `W4` is only half met: the *customer* is
named (Microsoft), the *supplier contract* is not.

**Exposure** (flow `asof 2026-08-14`):

| Ticker | Chain position | Flow | Note |
|---|---|---|---|
| `MSFT` | The buyer, doing the substituting | 🟡중립 (+0.444 · OBV 매집 · RS20 **+21.3** · RS60 +12.9 vs `SPY`) | Headline layer. `vol_surge` **0.60** ⇒ 🟡 is a volume artifact (§SWEEP 2c) |
| **`MRVL`** | Custom-silicon ASIC design — **the named beneficiary** | 🟡중립 (+0.378 · OBV 매집 · RS20 +13.2 · RS60 +20.1) | ★ **Lost its 🟢 THIS RUN on a velocity move of 0.10 with zero price change** (`vol_surge` **0.48**) |
| `AVGO` | Custom-silicon incumbent | 🟡중립 (+0.207 · OBV 매집 · RS60 **−10.2** vs `SPY`) | **Held by the book.** Ranks near the bottom of its own registry bucket |
| **`NVDA`** | The **displaced** party | 🟡중립 (+0.458 · OBV 매집 · RS60 **−3.7** vs `SPY`) | ★ **Also lost its 🟢 this run to a 0.04 velocity move.** Prints **2026-08-26** |
| `COHR` · `LITE` | Optical/interconnect — the layer neither substitution touches | **🟢가속** (COHR +0.99 surge 1.67 · LITE +0.817 surge 1.27) | ★ **The only two admissible 🟢 in IT**, and both are 3-axis producible |

**Future — both branches, dated.**
- **IF the thread keeps building** → a Maia 300 unveiling with a named foundry/ASIC partner lands by
  **2026-09-30**, and `MRVL` − `NVDA` 20-day excess vs **`SPY`** is **positive** at the **2026-08-26**
  `NVDA` print. **KPI**: `MRVL` − `NVDA` 20d excess vs `SPY`; a primary Microsoft or partner filing.
- **ELSE (kill)** → no primary source materialises by **2026-09-30** (the story stays *"Report Says"*),
  **OR** `NVDA` beats and guides up on 08-26 with `MRVL` − `NVDA` 20d excess **≤ −3pp**.
- 🚨 **VOID**: if Microsoft's own capex guide changes inside the window, substitution and demand move
  together and the card cannot be read (`§4` asymmetry — a capex CUT changes the thesis; a RAISE only
  moves timing).

**Cell: STORY-ONLY** — the thread is loud (10 outlets at peak) and **the money is 🟡 on every exposure
name**. It does **not** go to BET. → **watchlist with a dated re-check 2026-08-26** (`NVDA` print).
★ **And the finding that outlives the card**: this is `D250`'s named gap. **`cycle_registry.json` is
29 days stale and has NO ENTRY for "custom AI silicon"** — the desk's PREMORTEM Lens 4 cannot flag an
exposure gap on a cycle that does not exist in its registry.

---

## Card 3 — ★★★ Trump threatened to declare the Strait of Hormuz US territory, and `S8` still has no date

| | |
|---|---|
| **Thread** | Hormuz / Iran standoff · `Hormuz` velocity **1.15×** (7d 1,442 / 30d 5,367) against `Iran` **0.88×** |
| **★ The pair is the finding** | The **country** story decelerates while the **chokepoint** story accelerates — the narrative has moved from politics to plumbing |

**Direction (body-read) — escalation and de-escalation on the same tape:**
- ★★ **08-14 — *"Trump threatens to declare strait of Hormuz 'territory of the United States'"*** [`guardian`]
- 08-15 — *"Trump asks Americans to accept high pump prices as Iran standoff drags on"* [`seekingalpha`, **1 outlet**]
- 08-14 — *"CNBC Daily Open: Washington tightens squeeze on the Iranian economy"* [`cnbc`]
- ★ **08-15 — *"Depleted strategic oil reserve nears level that raises concerns about damage to caverns, operations"*** [`cnbc`] — the **US's own shock absorber** is now a constraint
- ⚠ **08-13 — *"Crude Prices Undercut as Persian Gulf Tensions Ease Slightly"*** [`nasdaq`] and *"Oil falls on weaker demand outlook"* [`yahoo_finance`] — **the de-escalation half, same week**

🚨 **This is the object `CATALYST_WATCH.json` carries as its ONLY binary in window — and it is still
`undated`.** `S8` has been unscoreable for **14 consecutive runs**. **A human must `VOID` it or
re-register it with a date (P5).** **PREMORTEM must bracket this both ways — a one-way tilt into a
known binary is a protocol violation**, and this card exists partly to make that unavoidable.

**Exposure.** Same refining chain as Card 1, **plus the positioning asymmetry**:
**`WTI` speculative net is at the 18th percentile SHORT** (COT, Tue **08-11**) — i.e. **positioning was
frozen BEFORE the 08-14/08-15 escalation.** Context, never a trigger (D6).
⚠ **The literal beneficiaries remain untaggable**: the tanker block (`STNG·FRO·INSW·DHT·TNK`) is
**outside `us_top300`**, so this desk has **no** flow/RS/OBV/short axis for them (`M45`'s measured case,
still open).

**Future — both branches, dated.**
- **IF escalation continues** → a dated US action on the Strait (declaration, escort regime, or
  interdiction) reported by **≥3 independent outlets** by **2026-08-31**, with `CL=F` above its 08-14
  close of **82.40**.
- **ELSE (kill)** → `CL=F` closes **below 78.00** on any settled session through 08-31 with no dated US
  action, i.e. the standoff prices out.
- 🚨 **VOID**: an OPEC+ production decision inside the window makes the barrel non-attributable.

**Cell: STORY-ONLY on the direct names / CONFIRMED-EARLY only through Card 1's refining leg.**
→ **PREMORTEM (mandatory both-sides bracket)**; **not** to BET as a standalone.

---

## Card 4 — ★★ $70bn of "shadow credit" backstops for AI companies — a NEW object, and the credit tape is silent

| | |
|---|---|
| **Thread** | AI financing structures · **new this week** · `shadow`+`credit` velocity **1.29× = #2 of the 16-term sweep** (7d 28 / 30d 93) |
| **Curve** | 08-11 `wsj` → **08-15 `bloomberg`** → **08-16 two syndications** (The Edge Singapore, The Business Times) — **spreading on a Sunday**, which is unusual for a credit story |

**Direction (body-read).**
- **08-15** *"Bond Traders Agonize Over AI Companies' **$70 Billion** of Shadow Credit Backstops"* [`bloomberg`; body via `yahoo_finance`]
- 08-11 *"Private-Credit Firms Clamp Down on Loan Sweeteners in Fear of **'Shadow Defaults'**"* [`wsj`]
- ★ **The dated instance, same week**: **`AMD` borrowed $4.75bn — more than triple its prior bond sale**
  [`fool`/`nasdaq`/`yahoo_finance` 08-15/16], and **the stock rose 5.6% the session the deal landed**
  [`yahoo_finance` 08-14].
- **Equity-side precedent already on file** (`M134`): `GOOGL` Q2 free cash flow **−$5.86bn**, funded by a
  **$49.6bn** equity raise.

⇒ **AI capex is migrating onto balance sheets and into structures bond desks are calling shadow.**

⚠⚠ **And the instrument says nothing.** `HY OAS` **2.71% = 10.3rd percentile of the pull, unchanged for
5 sessions**; `IG OAS` 0.79 flat; `NFCI` **−0.549 = 7.1st percentile, the loosest of the year**.
⇒ **Labelled `narrative-only`.** This is the exact failure the desk logged 2026-07-21 (*"a whole credit
surprise stack built from narrative while HY OAS sat 6bp off its 365-day low"*), and the label is the
whole point of writing the card.

**Exposure** (flow `asof 2026-08-14`) — **the node this decides is Real Estate's data-centre unit**:

| Ticker | Chain position | Flow | Note |
|---|---|---|---|
| `DLR` | Data-centre REIT | 🟡중립 (+0.439 · OBV **매집** · RS20 +10.7) | Inside a sector every aggregate axis calls UW |
| `EQIX` | Data-centre REIT | 🟡중립 (+0.444 · OBV **매집**) | `vol_surge` 0.93 |
| `IRM` | `M131`'s measured data-centre unit member | 🟡중립 (+0.182 · OBV **매집**) | |
| `CBRE` | Development/leasing | 🟡중립 (+0.322 · OBV **매집** · RS60 +13.5 vs `SPY`) | |
| `AMD` | The borrower | 🟡중립 (−0.151 · RS60 **+18.4** vs `SPY`) | ⚠ RS20 −0.7 — the 60-day is stock, not flow |

★ **The contradiction worth handing on**: **4 of Real Estate's 12 names are accumulating and all four
are the data-centre unit**, inside the board's most uniformly negative sector.

**Future — both branches, dated.**
- **IF the credit instrument catches up** → `BAMLH0A0HYM2` **≥ 2.85%** (+14bp) at the first `[FRED]`
  close covering **2026-08-28**. The RE UW's premise (duration) would then be **replaced**, not
  confirmed — the node would be selling on **cost of capital**.
- **ELSE (kill)** → `BAMLH0A0HYM2` **≤ 2.71%** at the same settle: the story spread and the market
  charged nothing for it ⇒ the card is narrative and is dropped to the ledger.
- 🚨 **VOID**: a non-AI credit event (sovereign, bank, broad HY default wave) inside the window makes
  any widening non-attributable.

**Cell: STORY-ONLY** (loud story × 🟡 money × a flat credit instrument). → **watchlist, dated re-check
2026-08-28**. Registered as **`P67`** in MACRO §E. **Not** handed to BET.

---

## Card 5 — ★★ "Data centres are turning energy stocks into AI plays" — the story is peaking while the tape distributes

| | |
|---|---|
| **Thread** | AI power / nuclear · `data`+`center` **1.09×** on the largest absolute pool of the sweep (7d **3,269** / 30d 12,810) |
| **Curve** | **5 outlets on 08-16** (*"Why Data Centers Are Turning Energy Stocks Into AI Plays"*, syndicated `fool`→`yahoo_finance`→`nasdaq` 08-15/16) + *"3 Nuclear Energy Stocks Riding the AI Power Surge in August"* (08-16) + *"Could $5,000 in This Nuclear Stock Turn Into a Life-Changing Sum?"* (08-15, 3 outlets) |

**Direction (body-read).** ⚠ **This is retail-facing syndicated advocacy, not reporting.** Every item in
the cluster is a Motley Fool-family "should you buy" column; **no operator announcement, PPA, filing or
interconnection award is in the cluster.** The direction the *text* asserts is bullish AI-power.

**Exposure — and the money says the opposite, on every single name** (flow `asof 2026-08-14`):

| Ticker | Chain position | Flow | Verdict |
|---|---|---|---|
| `NEE` | Regulated + renewables | **🔴분산** (−0.679 · OBV **분산** · RS20 −7.4 · RS60 −10.1 vs `SPY`) | dispersing |
| `VST` | Merchant power — the classic AI-power name | **🔴분산** (−0.708 · OBV **분산** · RS20 −9.1) | dispersing |
| `CEG` | Nuclear merchant | 🟡중립 (+0.185 · OBV 중립 · RS20 +7.5) | flat |
| `GEV` | Turbines/grid equipment | **🔴분산** (−0.588 · OBV **분산**) | dispersing |
| `VRT` | Data-centre thermal/power | 🟡중립 (−0.182 · RS60 **−14.7** vs `SPY`) | |
| `PWR` | Grid EPC | 🟡중립 (+0.346 · OBV 매집 · RS60 −9.8) | |

★ **Utilities is the ONE sector on this board whose zero is real**: **0 of 15 names pass `OBV 매집 ∧
RS20>0`** — it survives the `vol_surge` correction that turns every other 0.00 breadth into an artifact
(SWEEP §2c). ⇒ **Story loud, money genuinely absent.** This is the cleanest **STORY-ONLY** cell the desk
has measured this week, and it is a **direct contradiction of the syndicated narrative**, not a
confirmation of it.

**Future — both branches, dated.**
- **IF the story is right and money follows** → **any** Utilities name posts `OBV 매집 ∧ RS20>0` by the
  **2026-08-28** settle (from a base of **0 of 15**).
- **ELSE (kill)** → still **0 of 15** at 08-28 ⇒ the theme is confirmed as narrative-only for a second
  measurement and the card is dropped with `--revives-if "any UTIL name passes OBV 매집 ∧ RS20>0"`.
- 🚨 **VOID**: a heatwave/grid-emergency event inside the window makes merchant power a weather trade.

**Cell: STORY-ONLY.** → **watchlist, dated re-check 2026-08-28**. **Not** to BET.
⚠ **Book cross-check**: `ETN` (held, `AI-power/electrical`) sits in this lane. Its own flow is
**🟡중립 +0.478, OBV 매집, RS20 +8.4, RS60 +15.6 vs `SPY`** — i.e. **`ETN` is NOT participating in the
dispersion** the pure-play power names show. **Flagged to the book desk as "thesis lane weakening
around a position whose own flow is not"**, which is a re-justification request, not a drop.

---

## Card 6 — ★★ NATO is shooting drones down over its own territory, two countries in three days

| | |
|---|---|
| **Thread** | European air defence · **REIGNITED** · outlet curve **10 → 5** · 15 articles |
| **Dates** | **08-14 Latvia** (`politico`·`cnbc`·`dw`·`scmp`·`zerohedge`, **10 outlets**) → **08-16 Romania** (`politico`, 5 outlets) |

**Direction (body-read).** Not a market story in its text — it is an **escalation datapoint** that
transmits to a sector the desk already holds an OW− on. Latvia attributed the incursion to *"Russian
electromagnetic warfare"*; the Romania event is a separate country three days later.
⚠ **No procurement, budget or contract item appears in either cluster.** The transmission is `[inferred]`.

**Exposure** (flow `asof 2026-08-14`) — ★ and this is where SWEEP's biggest contradiction lands:

| Ticker | Chain position | Flow | Note |
|---|---|---|---|
| `RTX` | Missiles/air defence — **held by the book** | 🟡중립 (+0.467 · OBV **매집** · RS20 +10.8 · RS60 **+22.0** vs `SPY`) | ⚠ 🟡 on `vol_surge` **0.64** alone |
| `LMT` | Air defence / interceptors | 🟡중립 (+0.544 · OBV **매집** · RS20 **+15.2**) | blocked on `vol_surge` 0.78 |
| `NOC` | Air defence | 🟡중립 (+0.429 · OBV **매집** · RS20 +7.9) | blocked on 0.58 |
| `GD` | Land/combat systems | 🟡중립 (+0.188 · OBV 매집 · RS60 +10.6) | |
| `LHX` | C4ISR / EW — the literal counter-drone layer | 🟡중립 (+0.197 · OBV 매집 · **RS20 −1.0**) | the closest chain fit has the weakest tape |

★★ **Industrials carries the board's HIGHEST accumulation count — 25 of 50 pass `OBV 매집 ∧ RS20>0`,
more than IT's 22 of 56 — and produced ZERO shortlist names, 100% blocked by `vol_surge` alone.**
⇒ **This card is the narrative half of `D249`.** The Industrials OW− bracket measures **`XLI`** while
the position is **defense**, and it has been unresolved for **5 runs**.

**Future — both branches, dated.**
- **IF the thread keeps building** → a **third** NATO member reports a drone incursion/shootdown by
  **2026-08-31**, **and** the defense EW basket (`RTX·LMT·NOC·GD·LHX`) 20-day excess vs **`SPY`** stays
  **positive**.
- **ELSE (kill)** → no further incursion by 08-31 **and** the basket's 20-day excess vs `SPY` turns
  **negative** ⇒ the escalation did not transmit and the card drops.
- 🚨 **VOID**: a Ukraine ceasefire announcement inside the window.

**Cell: STORY-ONLY, pending the `D249` resolution.** → **ROTATION and the INDU DEEP mandate**, not to
BET. ⚠ **`HII`, the pure-play US Navy shipbuilder, is outside `us_top300`** — the desk cannot measure
one of the most exposed listed names in the adjacent naval lane (carried from 08-15).

---

## Card 7 — ★★ The US consumer printed its first retail-sales decline in nine months, and the calendar missed the week

| | |
|---|---|
| **Thread** | US consumer demand · dated prints + a dated earnings cluster |
| **Denominator** | `recession` 1.07× · `layoffs` **0.83×** — ⚠ neither is elevated; **this card does not claim a narrative surge** |

**Direction (body-read).**
- **08-14** *"**US retail sales post first decline in nine months in July**"* [`yahoo_finance`]
- **08-14** *"'Nobody escaped': **Walmart, Bank of America, TransUnion** raise major red flag over US
  consumers"* [`yahoo_finance`]
- 08-14 *"Trump's 'Golden Age' economy pitch fizzles with midterm voters"* [`fortune`·`yahoo_finance`]
- ★ **08-15 — *"Earnings Week Ahead: WMT, BABA, HD, TGT, and more"*** [`seekingalpha`]

🚨 **`catalyst_calendar --days 5` printed `[EARNINGS] (none in window / yfinance unavailable)`.**
**`WMT`, `HD` and `TGT` all report into this window** and the desk's own catalyst instrument carries
**zero** of them. Named as an instrument failure, not worked around.

**Exposure** (flow `asof 2026-08-14`):

| Ticker | Chain position | Flow | Note |
|---|---|---|---|
| `WMT` | Mass retail — reports this week | 🟡중립 (−0.226 · OBV 중립 · RS20 −3.5 · RS60 **−19.9** vs `SPY`) | |
| `HD` | Big-ticket discretionary — reports this week | **🔴분산** (−0.683 · OBV **분산** · RS20 −4.4) | the sector's weakest large name |
| `TGT` | Mass retail — reports this week | 🟡중립 (**+0.503** · OBV **매집** · RS20 +6.2 · RS60 +15.6) | ⚠ **inverts the other two** |
| `COST` | Mass retail | **🔴분산** (−0.480 · OBV 분산 · RS60 −18.0) | |
| `AMZN` | 40.2% of `XLY` cap | 🟡중립 (−0.391 · OBV **분산**) | |
| **`ABNB`** | **Services**, not goods | **🟢가속** (+0.881 · OBV 매집 · RS20 **+21.6** · RS60 **+34.5** vs `SPY` · surge 1.55) | ✅ FINRA clean-rise, short z **−0.94**. **3-axis producible** |

★ **`W5` fires hard here**: `ABNB` (+34.5 RS60) and `HD` (🔴분산) are in the **same GICS label**. The
goods/services split is the finding; "Consumer Discretionary" cannot express it. And `TGT` accumulating
against `WMT`/`COST` dispersing means the label does not even hold inside Staples.

**Future — both branches, dated.**
- **IF the consumer is genuinely rolling** → `WMT` **and** `HD` **and** `TGT` each print a guidance cut
  or a comp miss by **2026-08-21**, and `XLY` 5-day excess vs **`SPY`** stays negative.
- **ELSE (kill)** → **≥2 of the 3** beat and hold guidance ⇒ the July retail print was a single month,
  and the DISC UW-side wind loses its dated driver.
- 🚨 **VOID**: a tariff announcement affecting consumer goods inside the window.

**Cell: CONFIRMED-EARLY on the SHORT side of goods / STORY-ONLY overall.** → **ROTATION** (DISC), and
the `ABNB` leg goes to **BET §B** as the one name in this card the money confirms.

---

## Card 8 — ★ `Reddit` joins the S&P 500 on 2026-08-18 — a dated structural catalyst the instrument did not carry

| | |
|---|---|
| **Thread** | Index rebalance · single dated event · **08-14** *"Reddit Shares Surge as S&P 500 Inclusion Set for August 18"* [`yahoo_finance`] |

🚨 **`catalyst_calendar --days 5` printed `[STRUCTURAL] (none in window — data/catalysts/structural_schedule.json 을 사람이 갱신한다)`.** An index rebalance **two sessions out** is precisely
what that block exists to carry. **Human-maintained file (P5); named, not fixed.**

**Direction.** Mechanical index demand, dated and known. **No thesis is attached and none is claimed.**
`RDDT` is **not in `us_top300`** — the desk has **no** flow/RS/OBV/short axis for it.

**Future — both branches.**
- **IF the structural block matters** → the next `catalyst_calendar` run inside 5 days of a known
  rebalance carries **≥1** `[STRUCTURAL]` row.
- **ELSE** → it prints `(none in window)` again ⇒ the block is **decorative** and should be reported as
  a permanently empty instrument rather than as a clean check.

**Cell: neither — this is an INSTRUMENT card.** → **PREMORTEM / the dig list.** No exposure, no BET.

---

## §9 · Threads read and NOT carded — counted, not dropped silently

**44 of 52 alive threads were not selected.** Composition, so the truncation is legible:

| Reason | Count | Examples |
|---|---|---|
| **Syndicated evergreen template** (§0 defect) | **~18** | `"X vs Y: Which Stock Is a Better Buy"` chains ×4 · `"Here's How Much Money You'd Have..."` · `"3 [Sector] Stocks That..."` · `"Record Highs: Should You Chase The Rally?"` |
| **Non-market** (accidents, sport, culture, weather) | ~12 | Polish bus crash (7 outlets) · Belgium wildfires · Indonesia quake · Virgin Mary statue |
| **Market-adjacent, single name, no chain** | ~8 | `MSTR`/Bitcoin · `IonQ` foundry purchase · `TTD` crash · CoreWeave insider sale · `PLTR` |
| **Already inside a selected card** | ~4 | Riot Platforms $9bn compute deal (→ Card 4's financing axis) · SpaceX/Morgan Stanley valuation |
| **Ukraine war (non-energy legs)** | ~2 | North Korean troops/missiles — real, but the transmission is Card 1/6, already carded |

⚠ **Two of these deserve a named `missed_ledger` entry rather than a shrug** (L1: *"a thread you read
and did not turn into a card is a miss, not a drop"*):
- **`MSTR` / Bitcoin treasury** — cleared the money axis (velocity **1.07**, 7d 91 / 30d 365, probed
  20:24 KST) and got no card. Class `Q.확신부족`, `--enters-if "MSTR OBV 매집 ∧ RS20>0 vs SPY"`.
- **Riot Platforms' $9bn compute contract** (4 outlets, 08-16) — an AI-compute demand datapoint from
  outside the hyperscaler set. Class `M.숏리스트탈락` (not in `us_top300` ⇒ untaggable),
  `--enters-if "RDDT/RIOT enters us_top300 on the v2 universe promotion"`.

---

## §10 · Book cross-check — ENDED threads under open positions

**No thread an open position's thesis rides on is ENDED.** Two flags, both **re-justification requests,
not drops** (a DEAD verdict needs **both** axes — FADING/ENDED **×** 🔴 dispersing):

| Position | Thread it rides | State | Flag |
|---|---|---|---|
| **`ETN`** (`AI-power/electrical`) | Card 5 — AI power | Story **loud**, lane money **🔴분산 on the pure-plays** (`NEE`·`VST`·`GEV`) | ⚠ **The lane is dispersing and `ETN`'s own flow is not** (🟡, OBV 매집, RS20 +8.4, RS60 +15.6 vs `SPY`). **Not a drop.** Re-check **2026-08-28** with Card 5's KPI |
| **`NVDA` · `AVGO`** (`AI-compute-EPICENTER`) | Card 2 — Microsoft substitution | Story **building against them** | ⚠ Both **lost their 🟢 this run to a velocity move with zero price change** — an **instrument** event, not a market one. **No thesis change is warranted on it.** `NVDA` prints **2026-08-26** |
| `MPC` · `PSX` (`energy-refining`) | Card 1 | **CONFIRMED-EARLY** | ✅ The only book lane whose thread strengthened this run |
| `RTX` (`defense-missile`) | Card 6 | STORY-ONLY, `D249` open | ⚠ Its OW− sits on a bracket measuring `XLI`, not defense — **5th run** |

---

## ✅ EXIT CHECK

- [x] **Scope market-correct** — `--scope foreign` on every `brief`, `thread`, `fts` and `coverage`
      call in this stage. No cross-market feed is cited in any card.
- [x] **Selection logged** — **52 alive → 8 selected → 44 not selected**, and the 44 are **composed by
      reason** in §9 rather than counted and dropped. ★ The selection *method* was changed and the
      change is disclosed (§0): the `thread` ranking is contaminated by syndicated templates, so
      selection ran on substance and thread tags are quoted as curves only.
- [x] **Every card has a direction body-read** — Cards 1·2·3·4·5·6·7 all rest on read bodies, and
      **Card 5's body-read CONTRADICTS its own headline cluster** (syndicated advocacy vs 🔴 dispersing
      money), which is exactly the case the rule exists for.
- [x] **Every exposure name carries a flow tag with `asof 2026-08-14`**, and the four velocity-produced
      greens (`NFLX`·`CVX`·`CSCO`·`BAC`) are marked **not admissible** wherever they appear.
      **STORY-ONLY names did not leak into the candidate hand-off** — only `MPC` (Card 1) and `ABNB`
      (Card 7) go to BET §B.
- [x] **Every card has both branches + a kill condition + a dated horizon** (08-21 · 08-26 · 08-28 ·
      08-31 · 09-30), plus an explicit **VOID** condition where the window can be confounded.
- [x] **`EVENT_ALPHA.md` written; CONFIRMED-EARLY handed to ROTATION/BET; book flags emitted** (§10);
      two `missed_ledger` candidates named with `--enters-if` conditions (§9) rather than shrugged.
- [x] ⚠ **`P66` (Card 1) and `P67` (Card 4) are the registered MACRO forms of two of these cards** —
      the cards and the propositions are the same objects, not duplicates.
