# EVENT_ALPHA — industry_US · 2026-09-06 (Sun) · Stage 5 / L1·EVENT_ALPHA

> Bottom-up complement to MACRO's top-down matrix. **All news calls `--scope foreign`, without
> exception** (`W6`/market-lock rule). Flow tags are `SECTOR_FLOW_US.json`, **asof 2026-09-04**.
> **P4 — cards are analysis. No sizing, no buy/sell language.**

## §0 · Instrument conditions that bind every card below

1. 🚫 **No theme-freshness or news-velocity from the sweep** (PREFLIGHT G1). Every novelty number
   below comes from a **direct** `theme-age` / `fts` call made outside a sweep burst.
2. 🚫 **No card may say a thread is "quiet"** — 249 of 299 names were not measured for news, and
   **325 of 621 clusters (52.3%) on 09-05 exist only as a count** (`D474`/`D506`).
3. ⚠ **The thread window ends on two low-volume days** — per-day events `08-31 755 · 09-01 858 ·
   09-02 944 · 09-03 877 · 09-04 727 · **09-05 281 · 09-06 104***. **Every FADING tag in this window
   is weekend-inflated** (`D508`), so each card below reads its curve's **weekday legs separately**.
4. ⚠ **The flow tags are `asof 2026-09-04` and the last two days of news are NOT in them.** Three of
   the eight cards below are built on events that post-date the entire price frame — that is stated
   on each card rather than hidden, and it is why every card's kill condition names a **settled**
   close.
5. 🚨 **The 🟢 tag is unreliable for the 50 largest names** (`SWEEP_READ §2` / `D537`): `flow_tag`
   reads a news axis `flow_score` has dropped, and that axis exists only for universe positions
   0–49. **Where a card's exposure name sits in that prefix, the card cites `flow_score`, `obv_norm`
   and `rs20` — never the tag alone.**

## §1 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: **4,546 daily events → 3,501 threads → 572 multi-day → 44 ALIVE**
(2,929 one-day, 60 of them new today).

**Selected: 8. Not selected: 36 alive threads**, by category —
19 single-line REIGNITED/FADING with no market chain this desk can reach (India IPO GMP, FIFA,
Nomad Games, Croatia toxic waste, Egypt drugs case, Nepal floods, Kumamoto shelters, Dover port
protest, Bolivia base explosion, Philippines/Duterte, Malaysia PAS, Taiwan mayoral, Greenland/EU,
Farage/Burnham, AfD state election, Indonesia/Krakatau, Victoria's Secret, Opendoor/Constellation,
Dodgers) · 9 generic listicle clusters (*"Why X Stock Dropped/Climbed This Week"*, *"1 Top
Cryptocurrency…"*, *"If a Market Crash Is Coming…"*, Social Security, dividend screens) which are
**publisher artifacts, not events** · 5 crypto/BTC price-commentary threads (no chain past
`COIN`/`HOOD`/`MSTR`, all three already carried) · 3 already-carried and settled or bracketed
(`S130` Hugging Face, Apple CEO succession, Cybercab/NHTSA) .

⚠ **One item admitted that is NOT a thread**, and it is Card 2. See its header.

---

## Card 1 — ★★★ The tanker war: a two-way military escalation on the desk's only OW sector, entirely outside the price frame

| | |
|---|---|
| **Thread** | 🟡 **REIGNITED**, 5 days · outlets **2 → 10 → 7 → 3 → 4** (08-31 · 09-01 · 09-02 · 09-03 · **09-06**) · window denominator **4,546 events / 3,501 threads / 44 alive**. ⚠ The final `4` sits on a **104-event Sunday**, i.e. a high per-day share, not a decay. **Two sibling FADING threads carry the same axis and both read differently once the weekend is stripped**: *"U.S. strikes on Iran send oil prices higher"* **22→22→19→14→21**→(13→7 weekend) and *"US launches new strikes as war escalates"* **12→16→9→5→10→16**→(5) — **the second is RISING into Friday** |
| **Direction — body-read, not headline** | **A tit-for-tat escalation around oil EXPORT infrastructure, with a blockade framing.** 09-05: the US struck **three Iranian oil tankers**, CENTCOM framing them as financing *"regional proxies"* [**16 outlets**: aljazeera·bbc·cnbc·ft·bloomberg·axios·scmp·wsj·ft·dw·politico·euronews·AP·fortune·forbes·guardian], one strike **near Kharg Island**, Iran's principal export terminal [euronews]. 09-06: **Iran targeted a US naval drone entering the Strait** [euronews·scmp] and the IRGC **claimed attacks on US warships "over a naval blockade"** [aljazeera], warning of a *"more painful"* response [cnbc]. ⚠ Fortune's own framing is the useful one: *"a new escalation that could transform the war"* — **the object moved from shipping harassment to export-capacity destruction** |
| **⚠ The other side, read BEFORE the card was written** (`C2`, `M1327`) | **Bessent (US Treasury Secretary) publicly forecasts $40 crude and lower yields post-war** [economictimes·seekingalpha, 09-05] · **OPEC+ met 09-06 and kept policy UNCHANGED** [7 outlets] · Trump calls the conflict **"small potatoes"** [3 outlets] · Bloomberg reframes it as **"economic endurance"** (attrition, not shock) [09-06] · Iraq is **sourcing tankers for Hormuz runs**, i.e. the workaround is being built [bloomberg 09-04]. **The de-escalation side is larger in outlet count than the escalation side and is NOT dismissed here** |
| **Exposure — one hop past the headline names** | Headline layer (crowded by construction): none — **no US-listed equity is named in any of the 46 tanker articles.** Chain layer, all asof 09-04: **`MPC`** refining · `flow +0.69 · OBV +0.62 매집 · rs20 +30.8 · rs60 +41.5` · 🚨 **`[FINRA]` 5v5 short build +8.9, the largest on the sheet** · **HELD** · **`PSX`** refining · `+0.75 · +0.43 매집 · +25.5 · +34.2` · **HELD** · **`VLO`** refining · `+0.70 · +0.48 매집 · +24.7 · +37.5` · standing rejection, reaffirmed 09-04 · **`XOM`** integrated · 🚨 `+0.03 · −0.07 중립 · +4.6 · −0.3` — **the sector's weakest name is the one most exposed to Iranian barrels leaving the market** · **`OKE`/`WMB`** midstream · `+0.69/+0.77`, both 매집, **`WMB` carries the sector's largest Δ +0.35**. ⚠ **All six tags predate the escalation by two days** |
| **Future — branch A (thread keeps building AND flow stays accumulating)** | Export-capacity destruction is priced into the **barrel** before the **crack**: WTI holds above **$91.48** (the 09-04 settle) through **2026-09-11**, and the distillate crack fails to recover its 09-01 peak of 106.23. ⇒ the refiners' input cost rises without product following, and the OW's **chain-position** specification breaks. **Track KPI**: the distillate−gasoline spread (98.4th percentile on 09-04) narrows below the 90th |
| **Future — branch B / kill condition** | **KILLED IF**, at the **2026-09-11 settled close**, WTI is **below $85.76** (the 08-31 settle, i.e. the entire escalation move retraced) **OR** a dated US–Iran de-escalation event is carried by ≥5 outlets. Either would make Bessent's $40 framing the live one and this card a story |
| **Horizon** | **2026-09-11** (settled close). First readable session **2026-09-08** |
| **Cell** | ⚠ **UNCLASSIFIABLE ON THE 2×2 THIS RUN, and that is the honest answer.** The narrative axis is alive-and-two-way; **the money axis cannot be read, because the last settled tape predates the event by two sessions.** ⇒ filed as **STORY-PENDING-MONEY** with a dated re-check, **not** as CONFIRMED-EARLY. **It is NOT handed to BET as a fresh candidate.** ROTATION reads it as evidence that Energy's driver has fractured (MACRO §E tension 1) |

---

## Card 2 — ★★★ Venezuela: 487 hits, 2.95× accelerating, and it is on **no** thread, **no** term table and **no** row

| | |
|---|---|
| **⚠ NOT A THREAD — admitted on different instruments, and that is the finding** | `thread --days 7` returns **no Venezuela thread**, because the cluster titles differ every day and the linker never joins them. It is admitted here on **term counts and `theme-age`**: **`fts` 487 hits/7d** (would rank **9th of 18** on the term table, above `refinery` 275 and `diesel` 280) · **7d = 72.7% of the 14d total** · **3d = 42.5% of the 7d** · **`theme-age` 🟡ACCELERATING 2.95× on a base of 1,562**. ★★ **2.95× is the ONLY theme this run measured that clears the 2× bar, and it is 1.6× the next-highest** (`payrolls` 1.89×). ⇒ **`D538`**: *a story whose daily cluster titles never repeat is invisible to the thread instrument regardless of size; term velocity and `theme-age` are the fallback and must be run independently* |
| **Direction — body-read, ~15 outlets over 8 days** | **A dated structural supply opening, followed by a turn.** 08-29/30: Trump hails *"the biggest oil deal in world history"*; **the US strikes a deal over 65 billion barrels of Venezuelan reserves** [axios·semafor·toi] and says it will **refill the SPR with Venezuelan crude** [aljazeera]. 08-31: **Trump says `XOM` will enter**; **`CVX`·`HAL`·`ONGC`·`GEV` near final deals** [oilprice·yahoo]; *"`SLB`'s Venezuela bet"* [yahoo]. 09-01: White House details; **China demands a rights guarantee** as a US firm secures a 100-year concession [scmp]. 09-02: ★ **`CVX` commits $7bn to DOUBLE output in five years**; the US energy secretary **"vows output will double"** [scmp·france24·economictimes]. 09-03: US firms and Eni expand [aljazeera·euronews]. **09-04/09-05: the turn — "Trump's Big Venezuela Deal Leaves US Oil Industry BLINDSIDED", 13 outlets** [bloomberg ×2 · japantimes] |
| **🚨 The hole, named rather than guessed** | **The body of the "blindsided" leg is unreadable on every outlet that carried it.** `fts` and `search --field any` both return `[no body]` for the two Bloomberg items and `[error]` for the Japan Times one (Bloomberg is on the scraper's blocked list — `D10` class). ⇒ **the desk has the SUBJECT from three outlets across two days and NOT the mechanism**, and the difference between *"the terms are bad for US producers"* and *"they were not consulted"* is the difference between a thesis and a headline. **`D535`.** This card is written so that **either** mechanism is scoreable |
| **Mechanism the card DOES assert, with its physical basis** | Venezuelan crude is **heavy sour** — the design feed of the US Gulf Coast refining complex. A structural rise in heavy-sour supply is **bearish the barrel** and **bullish the heavy–light differential**, i.e. **bullish the refining margin**. ⇒ **the Venezuela axis and the Iran axis (Card 1) push the desk's OW sector in OPPOSITE directions on the barrel and possibly the SAME direction on the crack.** Corroborating instrument: **`heavy crude` theme-age 1.55× on a base of 140** |
| **Exposure — and the split is already visible in the tape** | **Named beneficiaries, asof 09-04**: **`SLB`** `flow +0.88 (Energy #1) · OBV +0.44 매집 · surge 1.39 · rs20 +14.2 · rs60 **−2.6**` — ★ **positive rs20 on a NEGATIVE rs60 is the signature of a NEW catalyst, not a continuing trend**, and it earned its 🟢 at universe position **173 with `velocity = None`**, i.e. **with no news leg available at all** (`SWEEP_READ §3`) · **`CVX`** `+0.66 · +0.37 매집 · rs20 +12.2` ⚠ **its 🟢 TAG is partly a news artifact (position 34, `velocity` 1.46) — its 3-axis `flow_score` is not, and only the score is cited here** · **`XOM`** 🚨 `+0.03 · −0.07 중립 · rs60 −0.3` — **named by Trump and dead last of 16** · **`GEV`** `−0.19 · +0.02 중립 · rs20 −4.5` — named, and negative. **`HAL` and `MP` are not in `us_top300`** ⇒ 🚫 **unmeasurable, not absent** (`C3`, `M25` class). Refining feed side: `MPC`·`PSX`·`VLO` as Card 1 |
| **Future — branch A** | The deal pays the **upstream/service** leg: `EW{XOM,CVX,SLB}` − `EW{MPC,PSX,VLO}` ≥ **+2.719** (p85) over the 5 settled sessions to **2026-09-14**. The OW's centre of gravity moves upstream and `M1245`/`M1246`'s chain-position finding is superseded. **Track KPI**: `heavy crude` theme-age leaves ⚪ECHO |
| **Future — branch B / kill condition** | **KILLED AS AN UPSTREAM STORY IF** that spread is **≤ −4.689** (p15) at the 09-14 close — the market read it as a refiner-feed story or ignored it, and the chain-position bet replicates through a second supply shock. **VOIDED IF** the arrangement is suspended or re-sanctioned inside 09-08→09-14 (base rate checked: 487 hits, **no** reversal item; Caracas's "sovereignty" line is rhetorical and is explicitly **not** a voider) |
| **Horizon** | **2026-09-14** — registered as **`P139`** (MACRO §D) |
| **Cell** | ★ **CONFIRMED-EARLY on `SLB` only.** `SLB` is the one name where narrative (named beneficiary), flow (`+0.88`, sector #1, 매집), independent instrument (`us_live_shortlist` **✅ 저숏/숏커버, `[FINRA]` z −1.21**) and **a clean signal free of the tag artifact** all agree. **Handed to ROTATION and to BET §B as a fresh candidate.** `CVX` = **STORY-ONLY** (tag contaminated), re-check **09-14**. `XOM` = **STORY-vs-TAPE CONTRADICTION**, filed to the missed ledger, not carded |

---

## Card 3 — ★★ The AI-power lane: the money is in GENERATION, the backlash is arriving at the LAND, and the book holds the distributing node

| | |
|---|---|
| **Thread** | 🟢 **BUILDING**, 3 days · outlets **2 → 3 → 3** (09-02 · 09-05 · 09-06), head item 09-06 *"AI data centers are transforming rural land markets — and fueling a backlash"* [cnbc]. ★ **Precursor form** — starts at 2 outlets and climbs, the shape the stage's own spec says to select first. Corroborating burst on today's partial day: **`TURBINES`** enters as a new word (3 articles, 100% market-related, 3 outlets) and **`HYPERSCALERS`** prints z **17.9** (6 articles vs a 0.050% baseline share) ⚠ **z's are inflated by a 557-article Sunday denominator** and are read as a *pattern*, not a magnitude |
| **Direction — body-read** | **Two-sided, and the sides are at different points in the chain.** Demand side: *"6 Hyperscalers Driving the AI Revolution Are Projected to Spend **$1.3 Trillion** on Capex in 2027"* [4 outlets, 09-06]; *"Elon Musk Says His New **Foundry** Can Get **Gas Turbines** Online 18 Months Faster"* [3 outlets, 09-06]; *"Wall Street is turning AI's massive electricity appetite into a **$61 billion bond market**"* [09-05]. Constraint side: the cnbc body is about **local landowner resistance and land-market distortion**, i.e. a **siting** constraint, which is the same class as the Texas *"ghost demand"* halt `P127` already carries. ⇒ **capital is abundant and SITES are the binding constraint** — that is the direction, and it is not what either headline says alone |
| **Exposure — asof 09-04** | **Generation (the money):** `CEG` `flow +0.64 · OBV +0.19 매집 · rs20 +11.2 · rs60 +17.2` · `VST` `+0.62 · +0.21 매집 · rs20 +6.6 · **Δ +0.49, the board's 3rd-largest**`. ⚠⚠ **Both are 🟡, NOT 🟢, and both are blocked by `vol_surge` alone (0.96 / 1.02 vs a 1.2 gate)** — `SWEEP_READ §3`. **Electrical equipment (the drain):** `ETN` 🔴 `−0.66 · −0.12 분산 · rs20 −8.0` **HELD** · `PWR` `−0.51 · −0.05` · `GEV` `−0.19 · +0.02` · `VRT` `+0.13 · +0.08 매집` but `surge 0.67` and **Δ +0.44**. **Turbine/foundry hop**: `GEV` is the only listed pure play and it is **negative on flow and rs20** |
| **Future — branch A** | The marginal AI dollar stays in **generation**: `EW{VST,CEG,VRT}` − `ETN` ≥ **+7.651** (p95, the asymmetric line `S146` registered because the state was already at the 92.9th percentile) at the **2026-09-14** close, and `P127`'s power-minus-compute spread ≥ **+4.555** at **09-10**. **Track KPI**: `gas turbine` theme-age leaves ⚪ECHO (**1.39× on 498** today, up from 1.42× on 476 — flat) |
| **Future — branch B / kill condition** | **KILLED IF** `P127` prints **≤ −5.790** at the 09-10 close (compute takes the marginal dollar back) **OR** a dated federal/ERCOT action on data-center siting lands inside the window — which would make the *constraint* side, not the *capital* side, the tradeable one and would invert this card's exposure map |
| **Horizon** | **2026-09-10** (`P127`) and **2026-09-14** (`S146`) |
| **Cell** | **CONFIRMED-EARLY on the generation node** (`CEG`, `VST` — narrative building, OBV accumulating, positive rs20) ⚠ **with the explicit caveat that neither carries a 🟢 tag and the reason is an axis this desk's own IC ledger scores negatively** (`C29`). Handed to ROTATION as evidence **against** reading Utilities' breadth 0.00 as absence. **`ETN` — see §3 book flag.** `GEV`/`PWR` = **DEAD on the money axis** (FADING narrative is not claimed; the flow is 🔴/negative and the narrative is building — so this is a **thesis-rewrite**, re-filed with a dated re-check, not a drop) |

---

## Card 4 — ★★ Gold leaving America: a dated, quantified de-dollarization datapoint under the desk's live duration thesis

| | |
|---|---|
| **Thread** | 🟡 **REIGNITED**, 5 days · outlets **5 → 8 → 2 → 4 → 4** (08-31 · 09-02 · 09-03 · 09-04 · 09-06). Weekday legs **5→8→2→4**; the final 4 is on the 104-event Sunday |
| **Direction — body-read** | **A named central bank moved a measured quantity for a stated reason.** *"As U.S. Treasury intervened in the bond market, the **Netherlands rushed 86 tons of gold** out of America because of **'geopolitical unrest'**"* [fortune, 09-03]; *"Dutch bank moves **$11.6B** of gold bullion out of the US and Canada **to London**"* [yahoo, 09-04]; *"The Dutch Central Bank Just Moved Its Gold out of North America"* [yahoo, 09-03]; *"Europe is moving its gold out of America; where is it headed"* [toi, 09-06]. ★ **The fortune body ties the move explicitly to a US Treasury bond-market intervention** — which is the same object `P138`/`M1285` measure as a 2.0th-percentile curve flattening. ⚠ **Counter-read in the same corpus**: *"Investors buoy gold price as central banks **slow**"* [mining, 09-04] — **central-bank buying is decelerating even as custody moves**, so this is a **custody** story, not a **demand** story, and the card says so |
| **Exposure — asof 09-04** | `NEM` (Newmont) `flow +0.71 · OBV +0.14 매집 · surge 1.14 · rs20 +13.8 · **rs60 +31.9, the best 60-day in Materials**` — ⚠ 🟡, blocked by surge 1.14 vs the 1.2 gate. `GLD` is not in `us_top300` ⇒ 🚫 **unmeasurable, not absent**. ⚠ **This is a ONE-NAME exposure map in a 12-name sector rated `N−`, and a one-name map is a `W5` failure waiting to happen** — stated rather than padded with names that have no chain to the story |
| **Future — branch A** | Custody relocation is an early tell for the term-premium leg: `NEM`'s rs60 (+31.9) holds above +25 through **2026-09-14** **and** the 30y−5y curve stays inside the bottom decile (**69.6bp = the 2.0th percentile** on 09-04). **Track KPI**: a second named central bank moves bullion, carried by ≥4 outlets |
| **Future — branch B / kill condition** | **KILLED IF** no second central bank is reported by **2026-09-14** — one Dutch move is an anecdote, and this desk has a standing rule against promoting a d3 count to a regime claim (`R128`-KR). **ALSO KILLED IF** `NEM`'s OBV turns 분산 on a settled close |
| **Horizon** | **2026-09-14** |
| **Cell** | **STORY-ONLY** — the narrative is dated and quantified, the exposure is one name in an `N−` sector, and the counter-read (central banks slowing) is in the same corpus. **Watchlist with a dated re-check 09-14. NOT handed to BET.** ⚠ Filed to the **missed ledger** as `Q.확신부족` with `--enters-if`: *a second named central bank relocation ≥4 outlets AND `NEM` rs20 > +15 on a settled close* |

---

## Card 5 — ★★ Pentagon rare-earth push vs China's grip: the third consecutive run with a dated shock and no vehicle

| | |
|---|---|
| **Thread** | 🟡 **REIGNITED**, 4 days · outlets **6 → 4 → 7 → 6** (08-31 · 09-03 · 09-04 · 09-06). ★ **Weekday legs 6→4→7 are flat-to-rising**; the 09-06 six is on a 104-event Sunday, i.e. **its share is the highest of the four** |
| **Direction — body-read** | **A named military supply-chain dependency with a quantified gap.** *"Pentagon rare earth push collides with China's grip"* [mining, 09-04]; ★ *"'Some of These Lasers Were the Size of Buildings': Now They Need **12 minerals China cut off**"* [yahoo, 09-04] — the specific, countable claim. Diplomatic counter-leg in the same window: *"China's Xi to bring a **large CEO delegation** on a US visit"* [yahoo/reuters, 09-04] and *"Asia-Pacific media outlets forge partnerships ahead of the **Shenzhen APEC summit**"* [09-05] ⇒ **the escalation and the negotiation are running simultaneously, and the card does not pick between them** |
| **Exposure** | 🚨 **NONE MEASURABLE, for the third consecutive run.** `MP` returns **not-in-universe**; `chain-hop` on this theme returned **only artifacts** on 09-05 (`D509` three-letter-ticker collisions: `LIN` matched Lindian Resources ASX, not Linde). The nearest listed proxies are `LIN` `flow +0.04 · rs60 −12.4` and `FCX` `+0.23 · +0.07 중립` — **neither is a rare-earth chain name**, and saying otherwise would be inventing a transmission. ⇒ **`M25`-class instrument gap: a dated, multi-outlet supply shock with no vehicle in `us_top300`** |
| **Future — branch A** | Not statable as a price branch, because **there is no price to state it on.** The only honest branch is an **instrument** branch: *the universe rebuild (`build_us_universe.py`, union of index ∪ current ∪ held ∪ `--include`) admits a rare-earth name by the next `us_top300` refresh*, which is a **human-approval** item (`P5`, the file is 53 days stale) |
| **Future — branch B / kill condition** | **KILLED IF** `rare earth` theme-age falls below **0.80×** (today **0.88× → this run 176 hits, −5.6% share-normalized**) on a settled weekday window, i.e. the shock decays before a vehicle exists |
| **Horizon** | **2026-09-19** (the theme's existing missed-ledger recheck date) |
| **Cell** | 🔴 **DEAD BY INSTRUMENT, NOT BY MONEY** — and the distinction is the point. The narrative is alive (flat-to-rising weekday legs) and the money axis **cannot be read at all**. Per the stage's own rule that DEAD requires **both** axes, this is **NOT a drop**: it stays on the rejection ledger as `L.vehicle없음` with `--revives-if` *a rare-earth pure play enters `us_top300`*, recheck **09-19**. **Third consecutive run.** ⚠ The repeat is the finding: `M1299` recorded the identical structure on gold (08-26) and on rare earths (09-05) — **`D539`**: *a universe that is refreshed on a weekly cadence and is currently 53 days stale cannot admit a vehicle for any shock younger than the staleness, so "no vehicle" is partly a file-age result, not only a market fact* |

---

## Card 6 — ★★ Anthropic's IPO: the AI private-capital cycle prints a dated public marker, and the listed exposure is all dispersing

| | |
|---|---|
| **Thread** | 🟢 **BUILDING** across 09-03 → 09-06 · outlets **7 on 09-05** (head), with a 3-outlet body cluster on 09-05 and 4 on 09-06. Related live cluster: *"Anthropic Could Be the Next Mega IPO: 2 Magnificent Stocks That Already Own a Piece"* [3 outlets] |
| **Direction — body-read** | **A dated slip plus two structural terms that both point at supply.** *"Anthropic IPO launch shifts toward **mid-October**"* [7 outlets, 09-05]; *"planning to unveil the IPO **prospectus after Labor Day**"* [yahoo·fool, 09-03]; ★ *"**Why Anthropic May Let Early Investors SELL Shares**, Unlike SpaceX and Cerebras"* [09-04]; ★ *"Anthropic Weighs **Lockup Periods Longer Than the Standard 180 Days**"* [09-05]; *"could value it at **30× revenue**"* [09-05]; *"**AMD committed up to $5 billion** to Anthropic"* [4 outlets, 09-05]. ⇒ **the two lockup items point in OPPOSITE directions on float** (early-investor sales = more supply; >180d lockups = less), which is exactly why this is a supply story and not a valuation story |
| **Exposure — asof 09-04, and it is uniformly weak** | `AMD` `flow −0.24 · OBV +0.01 중립 · surge **0.60** · rs20 −0.8` ⚠ **but Δ +0.57, one of the board's largest positive deltas from a negative level** · `GOOGL` 🔴 `−0.54 · −0.14 분산 · rs20 −4.1 · rs60 −11.2` · `AMZN` 🔴 `−0.74 · −0.39 분산 · rs20 −5.4`. ★ **All three named holders/backers are neutral-to-dispersing.** ⚠ `GOOGL` and `AMZN` are the `top1` of the two buckets whose `wflow` is **barred** (G3/`D459`) — so **no sector-level inference may be drawn from this card**, only name-level. Adjacent dated structural events in the same corpus: **SpaceX share unlock 09-09** [6 outlets] and *"Insiders and Early Investors Are **Selling** SpaceX Stock and Index Funds Are **Buying** It"* [09-05] |
| **Future — branch A** | The AI private-capital cycle converts to public float without a de-rate: Anthropic prices in mid-October **and** `AMD`'s Δflow (+0.57) converts to a positive level (`flow_score` > 0) on a settled close by **2026-09-19**. **Track KPI**: `AI capex` term count stops declining (102 this run, share **+1.1%**) |
| **Future — branch B / kill condition** | **KILLED IF** `AMD`'s `flow_score` is still negative at the **09-19** settled close **OR** the IPO slips a second time past mid-October. ⚠ **A third kill**: if `GOOGL`/`AMZN` remain 🔴분산 through 09-19, the "already own a piece" trade has no tape and the card is a story about someone else's balance sheet |
| **Horizon** | **2026-09-19** |
| **Cell** | **STORY-ONLY.** Narrative dated and building; **every measurable exposure name is neutral or dispersing.** Watchlist, re-check **09-19**. **NOT handed to BET.** Filed to the missed ledger as `Q.확신부족` with `--enters-if`: *`AMD` `flow_score` > 0 with OBV 매집 on a settled close* |

---

## Card 7 — ★ Volkswagen's €135bn / 50,000-job plan: a margin-restructuring story with no clean US vehicle

| | |
|---|---|
| **Thread** | 🟡 **REIGNITED**, 3 days · outlets **7 → 11 → 2** (09-03 · 09-04 · 09-06). ⚠ The **11 is the peak and it is on a full weekday**; the 2 is Sunday |
| **Direction — body-read** | **A margin target funded by headcount, and the market read it as positive.** *"Volkswagen Plans to Cut 50,000 Jobs"* [7 outlets, 09-03] → *"Volkswagen Targets **10% Margin by 2030** With **€135B Plan**"* [11 outlets, 09-04] → *"Automotive giant's stock **surges** amid plan to cut 50,000"* [09-06]. Same-window sibling: **Jaguar Land Rover confirms job cuts** [FADING 4→3, plus a UK minister meeting on 09-06]. ⇒ **European auto is restructuring capacity, which is a supply-side positive for surviving volume and a demand-side negative for the industrial chain that supplies it** |
| **Exposure — asof 09-04** | 🚫 **VW and JLR are not US-listed and are not in `us_top300`** ⇒ the primary names are **unmeasurable, not absent**. One-hop US chain: `GM` `flow +0.25 · OBV +0.13 매집 · rs20 +0.6` · `F` `+0.48 · +0.15 매집 · rs20 +5.0 · rs60 −3.9` · supplier layer `APH` `+0.14 · +0.12 매집` and `TEL` `−0.26 · −0.06 중립 · rs20 −3.2`. ⚠ **The whole chain sits inside `DISC` (`eqflow` −0.280, 21 of 28 negative on `exc5`) and `IT`** — the sector wind is against every name on this map |
| **Future — branch A** | European capacity cuts show up as US-listed supplier weakness: `TEL` and `APH` both print negative `rs20` on the **2026-09-14** settled close. **Track KPI**: a third European OEM announces a restructuring, ≥5 outlets |
| **Future — branch B / kill condition** | **KILLED IF** `F` and `GM` both hold positive `rs20` at the 09-14 close — the restructuring is being read as OEM-positive and does not transmit to the US supply chain. **ALSO KILLED IF** the thread does not reappear on a weekday by 09-11 (the 09-06 two-outlet leg is a weekend artifact, not a curve) |
| **Horizon** | **2026-09-14** |
| **Cell** | **STORY-ONLY**, and weakly so — the primary names are unmeasurable and the one-hop chain sits in two sectors the matrix rates `UW` and `N`. Watchlist, re-check **09-14**. **NOT handed to BET.** ⚠ Carded rather than dropped only because it is the second-largest weekday peak (11 outlets) in the alive set and dropping it silently would be a `missed_ledger` entry by another name |

---

## Card 8 — ★★ Memory spot vs contract: a 5-outlet direct challenge to a carried `[inferred]` claim

| | |
|---|---|
| **Thread** | Not a multi-day thread — a **head item on 09-05 at 5 outlets / 7 articles**, with two same-window siblings at 3–4 outlets: *"Recent News From Nvidia and SK Hynix Reveals Exactly What the Market Expects for Micron"* [4 outlets] and *"China's Biggest Memory Chip Stock Is Almost as Good as Micron"* [3]. ⚠ Admitted as a card because it **directly contradicts a claim the desk is carrying**, which the stage's spec makes a selection criterion in its own right |
| **Direction — body-read of the title's own claim** | *"**Spot Memory Prices Are Running 4 Times Contract Prices. That Is Not What a Cycle Peak Looks Like.**"* [5 outlets, 09-05]. The claim is structural: a 4× spot/contract ratio says the **contract** book is the lagging series, so a decelerating contract price is **arithmetic**, not demand. ⚠⚠ **This is exactly the residual the desk has flagged as `unknown` for two runs**: `MU`'s **contracted share of take-or-pay volume is `C3`-unknown**, and `STANDING_VIEW` carries *"the memory shortage is demand not capacity"* as **`[inferred]` and barred from evidence use**. ⇒ **the card does NOT resolve it; it dates it.** A 5-outlet trade-press claim is not a filing |
| **Exposure — asof 09-04** | `MU` `flow +0.48 · OBV +0.19 매집 · rs20 +16.2 · rs60 +7.8` ⚠ `surge 0.66` — **another `vol_surge`-suppressed name**, and its chart carries a **bearish divergence** against OBV 누적 (`M1321` carry) · `SNDK` `+0.63 · +0.35 매집 · rs20 **+43.9** · rs60 −0.3` — the run is 20 days old, not 60 · `WDC` `+0.07 · −0.04 중립 · rs20 +8.0 · **Δ +0.72, the board's #2**` · `STX` `+0.05 · +0.03 중립 · rs20 +4.9 · **Δ +0.73, the board's #1**`. ★★ **The board's two largest Δflows are both in this node and NEITHER is 🟢, both blocked by `vol_surge` 0.68 / 0.59** — `M1300` reproduces exactly, and `S145` (09-11) is the row that tests it |
| **Future — branch A** | The spot/contract gap is real and the node re-rates: `S145` prints branch A (`EW{STX,WDC,AMD}` − `SMH` ≥ **+6.825**) at the **2026-09-11** close. **Track KPI**: `MU`'s `flow_score` rises with OBV staying 매집 through its **2026-09-30 16:00 ET** print |
| **Future — branch B / kill condition** | **KILLED IF** `S145` prints branch B at 09-11 — the low-`vol_surge` sub-node does **not** lead its sector, which would simultaneously settle `C29`'s US leg **against** this card. ⚠ **Also killed as EVIDENCE (not as a story) the moment `MU`'s contracted-volume share is read from a filing and contradicts it** — that read has not been done for three runs (`D514`) |
| **Horizon** | **2026-09-11** (`S145`) · **2026-09-30** (`MU` print) |
| **Cell** | **STORY-ONLY, deliberately.** The narrative is dated and multi-outlet; the flow is accumulating on `MU`/`SNDK`; **but the claim it makes is the exact one the desk has ruled `[inferred]` and inadmissible**, and a trade-press ratio does not convert an `[inferred]` carry into a `[measured]` one. **NOT handed to BET.** Re-check **09-11** |

---

## §2 · Hand-off

| destination | items |
|---|---|
| **ROTATION** (sector-level cross-evidence) | ① **Energy's driver has fractured three ways** (Cards 1, 2) — level evidence unanimous, driver evidence opposed, and two of the three drivers post-date the price frame. ② **Utilities' breadth 0.00 is a filter artifact** (Card 3 + `SWEEP_READ §3`): `CEG`/`VST` are 매집 with positive `rs20`, blocked by `vol_surge`. ③ **Comm. Services and Real Estate absences are genuine evidence**, not artifacts. ④ **Industrials' defense node is uniformly 🔴 dispersing** — see §3 |
| **BET §B** (CONFIRMED-EARLY, fresh candidates) | **`SLB` only.** One name. Every other card is STORY-ONLY, STORY-PENDING-MONEY, or DEAD-BY-INSTRUMENT. ⚠ **This stage never sizes** (P4) |
| **PREMORTEM** | The **09-10 double binary** (US Aug PPI ∧ KOSPI200 quad witching, `D533`) · **`ORCL` earnings this week**, on no calendar and in no row · the **SpaceX 09-09 share unlock** [6 outlets] |
| **Rejection ledger** (`--revives-if`) | rare-earth complex `L.vehicle없음`, revives *if a rare-earth pure play enters `us_top300`*, recheck **09-19** (3rd run) · `GEV`/`PWR` **thesis-rewrite**, not a drop: narrative building while flow is 🔴/negative, recheck **09-14** |
| **Missed ledger** (`--enters-if`) | `NEM` `Q.확신부족` — enters if *a second named central-bank relocation ≥4 outlets AND rs20 > +15* (09-14) · `AMD` `Q.확신부족` — enters if *`flow_score` > 0 with OBV 매집* (09-19) · `CEG`/`VST` `M.숏리스트탈락` — dropped by the shortlist filter **on `vol_surge` alone**, enters if *`S145` settles against the `vol_surge` gate* (09-11) · `XOM` `Q.확신부족` — a named beneficiary of a 2.95×-accelerating story sitting **last of 16 on flow**, enters if *`flow_score` > +0.30 with OBV turning 매집* (09-14) |

## §3 · Book cross-check — ENDED/dispersing threads under open positions

| position | thread state | flag |
|---|---|---|
| **`ETN`** (held, AI-power/electrical) | The lane's narrative is **BUILDING** (Card 3) while `ETN` is **🔴분산 `flow −0.66 · OBV −0.12 · rs20 −8.0`** and **four of five lane peers accumulate** | 🚨 **Carried unchanged from 09-05 and NOT re-measured this run** — there is no new session. `S146` settles **09-14**. The thesis, not the thread, is what needs rewriting |
| **`RTX`** (held, defense/missile) | 🚨 **NEW THIS RUN.** The entire defense node is dispersing on the settled tape: `RTX` **−0.79 / OBV −0.29 분산 / rs20 −9.6** · `LMT` −0.74 · `NOC` −0.72 · `LHX` −0.65 · `GD` −0.52 (OBV **−0.44**) · `HWM` −0.32 · `EME` −0.63. **Seven of seven negative, six of seven 분산, every rs20 between −7.6 and −10.3.** ⚠ **And `RTX` is the WORST flow of the seven** — the book holds the weakest name in a uniformly weak node, the identical structure `M1317` found on `ETN` | 🚨 **Flagged to the book desk.** ⚠ **The narrative side is UNREAD**: no defense thread appears in the alive set, and the desk has no card on it. **This is a flow-only flag and says so** (`D6` — OBV is a C-grade axis and this is seven names of it, not one). Filed as **`M1370`**, re-check **2026-09-08** on the first settled close |
| **`MPC`/`PSX`** (held, refining) | Narrative **two-way and alive** (Cards 1, 2); flow **strongly accumulating**; 🚨 `MPC` carries the sheet's **largest 5v5 short build (+8.9)** | Not a kill — but the card that governs them is **STORY-PENDING-MONEY**, so the desk cannot claim confirmation until **09-08** |
| **`NVDA`/`ANET`/`AVGO`/`HPE`** (held, AI-compute) | `S130`'s Hugging Face thread is **ENDED by tag and ALIVE by `theme-age`** (`R129`) — settles **09-10**. `AVGO` is **−0.45 OBV 분산 with rs20 −15.9** | Carried; `R129` bars re-inheriting "dead thread" a fourth time |

---

## §4 · Ledger writes actually PERFORMED by this stage (not merely specified)

All entries `--sample prospective` (the only unbiased class), all with both required fields.

| ledger | ticker | class | recheck | enters/revives if |
|---|---|---|---|---|
| missed | **`NEM`** | `Q.확신부족` | **09-14** | a **second** named central-bank bullion relocation ≥4 outlets **AND** rs20 > +15 |
| missed | **`AMD`** | `Q.확신부족` | **09-19** | `flow_score` > 0 with OBV 매집 on a settled close |
| missed | **`CEG`** | `M.숏리스트탈락` | **09-11** | `S145` fires against the `vol_surge` gate, **or** the tag turns 🟢 |
| missed | **`VST`** | `M.숏리스트탈락` | **09-11** | same |
| missed | **`XOM`** | `Q.확신부족` | **09-14** | `flow_score` > +0.30 with OBV turning 매집 |
| reject | **`GEV`** | `A.flow미도착` | **09-14** | `flow_score` > +0.30 with OBV 매집 **and** rs20 > 0 |
| reject | **`PWR`** | `A.flow미도착` | **09-14** | OBV turns 매집 with rs20 > 0, **or** `P127` fires branch A |

**Totals after the writes** — `reject_ledger` **302** (was 300, **+2**) · `missed_ledger` **326**
(was 321, **+5**) · **legacy 0/0 on both**, a 17th consecutive run · **0 due**.

⚠ **The rare-earth complex is NOT re-added** — its `L.vehicle없음` row from 09-05 is live with a
**09-19** recheck. Re-filing it would double-count the same rejection, which is the sort of thing that
makes a ledger's totals stop meaning anything.

★ **Two of the seven writes (`CEG`, `VST`) are logged against the DESK'S OWN FILTER, not against the
names.** `M.숏리스트탈락` is the correct class precisely because nothing about those two companies was
judged — a volume axis dropped them, and the ledger is where that decision becomes scoreable instead
of invisible.

---

## ✅ EXIT CHECK — EVENT_ALPHA

- [x] **Scope market-correct** — `--scope foreign` on every `brief`, `thread`, `fts`, `theme-age` and
      `blindspot` call. No card cites a domestic-feed number.
- [x] **Selection logged** — **44 alive → 8 selected · 36 not selected, counted and categorized**
      (§1). No silent cap.
- [x] **Direction body-read on every card.** Card 1 read 46 tanker articles and found the *blockade*
      framing the headlines do not carry; Card 3 found the binding constraint is **siting**, which
      neither its demand nor its constraint headline says; Card 6 found **two lockup items pointing
      opposite ways on float**; Card 2's body-read is what surfaced the story at all. ⚠ **Card 2's
      "blindsided" leg is explicitly recorded as UNREADABLE rather than inferred** (`D535`).
- [x] **Every exposure name carries a flow tag with its asof (2026-09-04)**, and every name inside
      the velocity-eligible prefix is cited on `flow_score`/`obv_norm`/`rs20` rather than on its tag
      (`D537`). **Unmeasurable names (`HAL`, `MP`, `GLD`, VW, JLR) are marked unmeasurable, not
      absent** (`C3`).
- [x] **STORY-ONLY names did not leak into the hand-off** — exactly **one** name (`SLB`) reaches
      BET §B, and §2 says so explicitly.
- [x] **Every card carries both branches, a kill condition and a dated horizon.** ⚠ Card 5's branch A
      is an **instrument** branch, because there is no price to state a price branch on — declared,
      not faked.
- [x] **`EVENT_ALPHA.md` written**; CONFIRMED-EARLY handed to ROTATION/BET; **two book flags emitted**
      (`ETN` carried, **`RTX` new**); rejection and missed ledger entries specified with
      `--revives-if` / `--enters-if` conditions and dates (§2).
- [x] **DEAD used as a MONEY verdict, not a story verdict** — Card 5 is `DEAD BY INSTRUMENT` and is
      explicitly **not dropped**; `GEV`/`PWR` are **thesis-rewrites**, not drops, because their
      narrative is building while their flow is negative.

---

## 📋 Stage run log — open decisions resolved without a human

1. **Whether a story with no thread may be carded** — resolved as **yes, with the instrument named**
   (Card 2). `Venezuela` is invisible to `thread` because its cluster titles never repeat; it is
   admitted on term velocity + `theme-age`, and the invisibility is registered as `D538`.
2. **Whether Card 1 can be CONFIRMED-EARLY** — resolved as **no**: the money axis is unreadable
   because the tape predates the event. Filed **STORY-PENDING-MONEY** rather than forced onto the 2×2.
3. **Whether to card the defense node** — resolved as **flag it in §3 without a card**, because the
   flow is measured and the **narrative side is unread** (no defense thread in the alive set). A card
   with one axis is a half-card; the flag says which half is missing.
