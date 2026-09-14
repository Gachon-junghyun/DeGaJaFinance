# EVENT_ALPHA — industry_US · 2026-09-02 (Wed) · Stage 5 / L1·EVENT_ALPHA

> The **bottom-up** complement to MACRO's top-down matrix. Every news call `--scope foreign`
> (market-locked; a card citing a cross-market feed is void). Flow tags from
> `SECTOR_FLOW_US_REPAIRED.json`, **asof 2026-09-01**. **No sizing anywhere (P4).**

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: daily events **4,187** → threads **3,228** (multi-day **503**,
**alive 138**, one-day 2,725). Per-day denominator **08-27 856 · 08-28 735 · 08-29 307 · 08-30 293 ·
08-31 745 · 09-01 830 · 09-02 421**.
⚠ **09-02 is a partial collection day** (421 vs 745–856) — every window-end tag is provisional and no
FADING tag is read as attention decay (`D475`).

**138 alive → 8 selected → 130 not selected.** Selection rule applied in order: (i) precursor form
(starts ≤2 outlets and climbing) — `Commodities: Middle East Escalation` 2→4, `Global Bond Selloff
Weighs on Stocks` 2→4, `Bessent Says Hormuz Will Soon Be 'Worthless'` 2→2; then (ii) remaining
BUILDING/REIGNITED by peak — `Gas Turbine Prices…Nearly Triple` peak **8**, `Markets slide as
inflation fears trigger global bond selloff` peak **7**, `Euro area: Inflation jump supports ECB hike`
peak 6, `How Japan's bond rout is turning the tide of global capital` peak 5; then (iii) one FADING
thread admitted **only because the book holds exposure to it** (`5 Reasons to Buy Broadcom Stock
Before Its Sept. 2 Earnings`, `AVGO` held). Four bond-selloff threads were **consolidated into one
card** rather than counted four times.

---

## Card 1 — 🚩 **The gas-turbine reignition is an ENTRANT story, and the headline says the opposite**

| | |
|---|---|
| **Thread** | *"Gas Turbine Prices Are on Track to Nearly Triple. These Stocks Are Cashing In."* · **REIGNITED** · **5→3→8** · alive 138 / threads 3,228 |
| **Direction (body-read, not headline)** | 🚩 **The headline and the body point opposite ways.** `fts search gas turbine --days 4 --scope foreign` returns **67 matches**, and the mass of them is not "incumbents cash in" — it is **SpaceX entering the turbine-blade business**: *"Elon Musk says SpaceX will build its own gas turbine parts to meet surging AI power demand"* [businessinsider 08-31] · *"The limiting factor for nat gas turbine production is casting the blades"* [techcrunch 08-30] · *"SpaceX Is Coming For A $10B Market, Says Jefferies"* [08-31] · and the decisive one, surfaced by `chain-hop`: ***"Elon Musk's SpaceX Blade Plan Knocks Howmet As HWM Suffers Steepest Slide In 16 Months."*** ⇒ **the story confirms AI-power DEMAND and simultaneously attacks the incumbent that owns the bottleneck.** |
| **Exposure** (one hop past the headline via `chain-hop "gas turbine" blade casting`) | **`HWM`** Industrials · *the bottleneck incumbent (turbine-blade castings)* · **🔴분산 (09-01)**, OBV **−0.185**, `rs20` **−10.3 vs `SPY`**, **`vol_surge` 1.49 — the highest in this exposure set** · **crowded: no, distributed on volume** ★<br>**`GEV`** Industrials · *the named "cashing in" OEM* · **🔴분산**, OBV −0.259, `rs20` −10.5, surge 0.88<br>**`VST`** Utilities · *merchant power offtake* · 🟡중립, OBV −0.070, but **Δ +0.432 — the 2nd-largest positive Δ among Utilities**<br>**`CEG`** Utilities · *nuclear/PPA offtake* · 🟡중립, OBV +0.029, `rs20` **+6.1**, Δ +0.183<br>**`CAT`** Industrials · *reciprocating gensets, the substitute for a turbine you cannot get* · **🔴분산**, OBV **−0.389**, `rs60` **−17.1** |
| **Future — branch 1 (thread keeps building AND flow turns 🟢)** | The squeeze is real and the *offtake* layer monetises it before the *equipment* layer does ⇒ `VST`/`CEG` lead and `HWM`/`GEV` stay distributed. **Track KPI**: `CEG` `rs20` holds > +5 vs **`SPY`** **and** `HWM`'s `vol_surge` falls below 1.2 (distribution exhausting). **Horizon 2026-09-10.** |
| **Future — branch 2 / KILL condition** | **The card is falsified if `HWM` re-accumulates** — OBV > 0 with `rs20` > 0 vs **`SPY`** at any settled close through **2026-09-10** — because that would mean the entrant threat is being priced as noise and the headline read was right after all. |
| **Cell** | **STORY-ONLY → watchlist.** The narrative is live and the money is *against* the headline names; there is no 🟢 in the exposure set, so nothing is handed to BET. **Dated re-check 2026-09-10.** |
| ⚠ | **`gas turbine` is ⚪ECHO at 1.42× on a base of 476** (`theme-age`) — the REIGNITED tag is a curve shape, not novelty (`D461` discipline applied to the confirmer as well as the falsifier). And **`NRG` is not in `us_top300`**, so one obvious offtake name cannot be tagged at all. |

## Card 2 — ★★★ **Hormuz: the escalation now pays FREIGHT and REFINING while the barrel's physical flow is being restored**

| | |
|---|---|
| **Thread** | *"Commodities: Middle East Escalation Pushes Energy Prices"* **REIGNITED 2→4** (precursor form) + *"Bessent Says Hormuz Will Soon Be 'Worthless' as Oil By…"* **BUILDING 2→2** + *"Two More Oil Tankers Are Attacked in the Strait"* tagged **ENDED 3→2→12** — ⚠ **an "ENDED" thread whose final observation is its peak**, i.e. the partial-day artifact, flagged and **not** read as a death |
| **Direction (body-read)** | **Three distinct facts, none of them "oil up".** (i) **The doctrine changed**: *"U.S. strikes Iran tankers under new 'tanker for tanker' policy"* [axios 09-02]. (ii) **The barrel is flowing again under escort**: *"Energy secretary Chris Wright tells CNBC more than 17 million barrels of oil transited Hormuz on Monday"* [cnbc 09-02] — while *"Hormuz Shipping Slumps as U.S.-Iran Strikes Rattle Oil Markets… the number of tankers traversing remains below the…"* [oilprice 09-02]. (iii) ★ **The gas leg did NOT recover with the oil leg**: *"LNG Exports Through Hormuz Remain Stalled Even as Oil Flows Rebound"* [bloomberg 08-31] + *"Qatar Extends LNG Force Majeure"* + *"Asia Spot LNG Prices Hit 5-Month High"* [4 outlets]. And the ton-mile channel is explicit: *"Hormuz shutdown reroutes Saudi crude, and Korean yards are booking the ships that carry it"* [hellenicshipping 09-01]. ⇒ **the payoff is in DISTANCE and MARGIN, not in the barrel count.** |
| **Exposure** | **`SLB`** Energy · *services, the board's #2 flow* · **🟢가속**, OBV **+0.351**, `rs20` **+13.7 vs `SPY`**, surge **1.41** · `[FINRA]` z +0.47 △<br>**`WMB`** Energy · *midstream / gas* · **🟢가속**, OBV +0.181, surge 1.31 · `[FINRA]` z **−3.08 ✅ clean rise**<br>**`MPC`** (held) · *refining, the margin leg* · 🟡중립, OBV **+0.425**, `rs60` **+42.9 vs `SPY`** · z +1.49<br>**`PSX`** (held) · 🟡중립, OBV +0.301, `rs60` +34.4 · ⚠ **`vol_surge` 0.99 — misses the 🟢 gate by 0.01** (`C5`)<br>⚠ **headline-layer, crowded by construction**: `XOM` (🟡, OBV −0.001), `CVX` (🟡, OBV +0.342) |
| ⚠ **The exposure this desk cannot tag** | ★ **`FRO` (tankers) is not in `us_top300` and `LNG` (Cheniere) is not in the universe at all.** The two names that sit *directly* on the freight and gas legs the body-read just identified are **priceable but not flow-taggable** — `S109` says so in its own text, and `D416`-class blindness reproduces here on a **second** cycle. **This is the card's largest weakness and it is stated, not worked around.** |
| **Future — branch 1** | Freight/margin keeps paying while the barrel normalises ⇒ **`P126` fires B** (barrel-EW minus refiner-EW ≤ −4.443 at the 09-09 close) and the OW stays chain-positioned. **Track KPI**: the 3-2-1 crack widens while `CL=F` is flat-to-down. |
| **Future — branch 2 / KILL** | ★ **The card is already under live challenge from the flow Δ**: the **two largest positive Δ in the entire 298-name universe are `FANG` +0.840 and `EOG` +0.693 — both E&P, i.e. the barrel leg.** If `P126` fires **A** (≥ +2.312) the "chain-position, not barrel" reading is dead and `M1201`/`M1202` are superseded. **Horizon 2026-09-09.** |
| **Cell** | **CONFIRMED-EARLY → handed to ROTATION and BET §B**: `SLB` and `WMB` (both 🟢, both with the flow *and* the body-read behind them; `WMB` additionally the board's 2nd-most-extreme short exit). **`PSX` handed as a gate-artifact note, not as a 🟢.** |

## Card 3 — ★★★ **The global bond selloff: the narrative is fiscal, the US curve is not**

| | |
|---|---|
| **Thread** | *"Markets slide as inflation fears trigger global bond selloff"* **BUILDING 4→4→7** · *"Euro area: Inflation jump supports ECB hike"* **BUILDING 5→2→2→4→6** · *"Global Bond Selloff Weighs on Stocks"* **BUILDING 2→4** (precursor) · *"How Japan's bond rout is turning the tide of global capital"* **BUILDING 4→5**. Consolidated: **four threads, one card** |
| **Direction (body-read)** | *"Bond selloff deepens as inflation risks, oil prices jolt markets"* [reuters 09-02] · *"Global Bond Selloff Extends as Rate Hike Expectations Grow"* [morningstar 09-01] · *"European government bond yields surge to 15-year highs"* [euronews] · *"Governments should heed the bond market's warning"* [FT]. **The stated cause is fiscal/inflation.** 🚩 **The US curve disagrees with the stated cause**: `^FVX` **+5.0 bp** > `^TNX` +3.8 bp > `^TYX` **+1.9 bp** on 09-01 — a **bear-flattening**, which is a policy-path shape, not a term-premium shape (`M1235`). |
| **Exposure** | ⚠ **No clean US equity vehicle — the card is filed `L.vehicle없음` on the direction leg.** Every US sector proxy for "global duration event" is the same proxy the desk already uses for "Fed hawkish", and `D456` already ruled that a contaminated proxy must not carry a card. What *is* taggable is the **transmission**: `XLU` exc20 **−2.28** · `XLRE` exc5 **−2.37** · `XLI` exc5 **−2.64** / exc20 **−6.10** vs **`SPY`**, and `T` — a duration-like telecom — is **OBV +0.409 매집** with `rs60` **+11.0**, the opposite of the complex it sits next to |
| **Future — branch 1** | If the leg is genuinely inflation, `P125` fires **A** (Δbreakeven − Δreal ≥ +5.0 bp at the joint 09-04 observation) and the duration underweights are being held for the **wrong reason** even while they work. **Track KPI**: `^TYX − ^FVX` **steepens**. |
| **Future — branch 2 / KILL** | If `P125` fires **B** (≤ −6.0 bp), the four-run carry survives and this card collapses into `P121`. ⚠ **B is the WEAK-information branch — the registration state is already −11.0 bp = the 5.2nd percentile.** **Horizon 2026-09-04 (August NFP).** |
| **Cell** | **STORY-ONLY → no candidate hand-off.** `bond selloff` is 🟡ACCELERATING at **3.81× on a base of 196** — the newest macro axis on the board — and the desk still has no vehicle for it. **Dated re-check 2026-09-04.** |

## Card 4 — ★★ **Texas halts data-center power over "ghost demand" — the falsifier, written as its own card (`D457`)**

| | |
|---|---|
| **Thread** | *"Analysis: Texas' halt on powering data centers reflects US reckoning over 'ghost' demand"* · **6 outlets on 09-01, up from 3 on 08-31** · related and pointing the other way: *"Trump Says 'Let Data Reign' As He Slams Data Center Backlash"* [3] and the **ENDED** *"Trump: Communities that reject data centers will…"* 11→3 |
| **Direction (body-read)** | The mechanism is **speculative interconnection queues**: developers file for capacity at multiple sites for the same project, so the queue overstates real demand, and the grid operator has begun refusing. **This attacks the DENOMINATOR of every AI-power forecast**, not the price of power. |
| **Exposure** | The whole AI-power layer: `VST` 🟡 (Δ **+0.432**) · `CEG` 🟡 (`rs20` +6.1) · `NEE` 🟡 (Δ **+0.481**, the board's best Utilities Δ) · `PWR` **🔴분산** (`rs60` **−15.3**) · `ETN` (held) **🔴분산** (Δ **−0.633**) · `GEV` 🔴분산. ★ **Not one name in the AI-power layer carries 🟢** — the same measurement the 09-01 run made, reproduced |
| **Future — branch 1** | If the halt spreads (a second ISO or a FERC-level action) the layer de-rates and `P127` fires **B** (power minus compute ≤ −5.790). **Track KPI**: `theme-age` on `ghost demand` leaves 🟢FRESH-but-thin and reaches a base ≥ 25. |
| **Future — branch 2 / KILL** | **The card dies if `VST` or `CEG` prints 🟢** (all three price axes positive) at any settled close through **2026-09-10** — that would mean the offtake layer is being accumulated straight through the falsifier. |
| **Cell** | **STORY-ONLY.** ⚠ **`ghost demand` is 🟢FRESH on n = 3 ⇒ FRESH-but-thin and excluded from the freshness gate** (`D461`). **A gate that can fire at n=3 can fire on noise, and this card does not let it.** **Dated re-check 2026-09-10.** |
| ⚠ **Book cross-check** | `ETN` (held, real book **7.5%**) rides this thread on its adjacent-layer label. Its flow Δ is **−0.633**, the 4th-worst in the universe, and `[FINRA]` z is **−1.72** (shorts leaving a **falling** name). **Flagged to the book desk: the position's thesis rides a thread whose own falsifier gained 3 outlets this week.** |

## Card 5 — ★★ **Japan's bond rout / BOJ hike pricing — the one leg with a measurable, dated policy event**

| | |
|---|---|
| **Thread** | *"How Japan's bond rout is turning the tide of global capital"* **BUILDING 4→5** · *"BOJ's Takata urges nimble rate hikes to counter inflation"* **REIGNITED 4→2→6** · *"BOJ's Himino Vows Inflation Vigilance as Rate-Hike Bets…"* **REIGNITED 6→4** · *"Japanese Yen: BoJ hike expectations shape FX"* **BUILDING 2→3→3** |
| **Direction (body-read)** | *"Japanese Yen weakens as 10-year bond yield hits 3% for first time since 1996"* [**12 outlets**] · *"Analysis: Japan faces day of policy reckoning as Bessent calls time on big stimulus"* [5] · *"Bessent meets BOJ's Ueda, calls for sound policy to avoid currency volatility"* [5] · *"Yen hangs near 160 amid BOJ rate-hike bets"* [2]. ⇒ **A 30-year regime break in JGBs with the US Treasury Secretary publicly pressing on it.** The carry-trade channel is the transmission, and it is the one leg of Card 3 with an identifiable actor and a date. |
| **Exposure** | ⚠ **No clean US vehicle again** — the desk has no FX or JGB instrument, and the equity proxies (`XLF`, `MET` held) conflate a yen-carry unwind with a domestic rate call. `MET` (held): 🟡, `[FINRA]` z **−0.16**, 5v5 **−4.8**. **Filed `L.vehicle없음`.** |
| **Future — branch 1 / branch 2** | **1**: a BOJ hike or a yen break through 160 ⇒ carry unwind pressures the highest-multiple US assets first; **KPI** `SMH` exc5 vs **`SPY`** stays negative (it is −1.37 now). **2 / KILL**: yen strengthens back inside 155 **or** JGB 10y falls back below 2.75% ⇒ the card is a currency story with no equity content and is dropped. **Horizon 2026-09-11.** |
| **Cell** | **STORY-ONLY.** No name is handed forward. |

## Card 6 — ★★ **Nvidia's supply-chain money is buying the interconnect layer, not more compute**

| | |
|---|---|
| **Thread** | *"Nvidia's $279 Billion Supply-Chain Gamble"* **REIGNITED 4→3→3** · *"Nvidia agrees to acquire Hugging Face for $12.9B"* **REIGNITED 15→2→4** (⚠ the `S130` thread previously logged as ENDED — **status change recorded, row not re-scored**) · *"Equinix Expands NVIDIA Partnership To Launch AI Inference…"* BUILDING 3→3 |
| **Direction (body-read)** | *"Nvidia pours $3.5 billion into MediaTek — company will adopt NVLink Fusion for its custom AI accelerators"* [**6 outlets**, 09-01] and *"Anthropic signs $35 billion cloud deal with Nvidia-backed Lambda"* [5]. ⇒ **The capital is going into the INTERCONNECT standard and into captive demand, not into more silicon.** That is a moat-widening use of cash and it re-rates the *fabric* layer, not the accelerator layer. |
| **Exposure** | **`NVDA`** (held, real book **21.3%**) · *the printer* · 🟡중립 but **OBV −0.195 분산** on **`vol_surge` 1.38** — distribution on heavy volume — with `[FINRA]` z **+2.18 🔴** and Δ **−0.210**<br>**`ANET`** (held, **14.6%**) · *the fabric incumbent NVLink Fusion attacks* · 🟡, OBV +0.070 but `vol_surge` **0.64** and Δ **−0.494**, `[FINRA]` z **+2.25 🔴 — the board's most extreme short build**<br>**`MRVL`** · *custom-silicon / interconnect* · **🔴분산**, `rs60` **−23.4**, Δ **−0.662**<br>**`AVGO`** (held) · **🔴분산**, `rs60` −7.4, prints **tonight** |
| **Future — branch 1** | If NVLink Fusion is a genuine standard land-grab, the *incumbent* fabric names de-rate while `NVDA` holds ⇒ `ANET`'s `rs60` **+19.4** decays toward zero. **KPI**: `ANET` `rs20` (now **+0.6**) turns negative vs **`SPY`**. |
| **Future — branch 2 / KILL** | **The card dies if `ANET` re-accumulates through the `AVGO` print** — OBV > +0.15 with `vol_surge` > 1.0 at the 09-10 close. **Horizon 2026-09-10.** |
| **Cell** | **LATE-MONEY → valuation-gate note, no candidate hand-off.** Both held names are being distributed *and* shorted into a story that is still building; that is the definition of late money, and the correct output is a note to BET, not a name. |
| ⚠ **Book cross-check** | **`NVDA` 21.3% + `ANET` 14.6% = 35.9% of real invested capital sits inside this card**, and the card's direction body-read is that the money is moving to the layer between them. **Flagged.** |

## Card 7 — ★★★ **`AVGO` prints tonight — the D-0 binary, and the desk's brackets already exist**

| | |
|---|---|
| **Thread** | *"5 Reasons to Buy Broadcom Stock Before Its Sept. 2 Earnings"* **FADING 3→3→2** ⚠ (partial-day) · *"Broadcom Faces Crucial Earnings Test After AI Chip Sales Surge 143%"* [3] · *"Broadcom's earnings loom, but this reveal came first"* [3] · *"Broadcom Set to Report Q3 Earnings: Buy, Sell or Hold"* [3]. **Admitted despite FADING because the book holds `AVGO`** (the stage's own exception) |
| **Direction (body-read)** | The cited growth number is **AI chip sales +143%**, i.e. the bull case is already the consensus case; the flow says the opposite: **🔴분산**, OBV **−0.264**, `rs60` **−10.4 / −7.4 vs `SPY`**, Δ **−0.095**, `[FINRA]` z +0.79 with 5v5 **+3.8▲**. ⇒ **a name being distributed into a print whose bull case is public.** |
| **Exposure** | `AVGO` (held, real book **not** among the 9 — held in the **paper** book; `C23` applies, and the two books are not merged here) · `MRVL` 🔴분산 · `NVDA` 🟡 |
| **Future — both branches** | **Already registered and both-sided**: `S138` (±11.00pp, deliberately **outside** the measured ±9.6% implied move) settles at the first settled close after the print; `S127` (A ≥ +5.928 / B ≤ −4.922, settles 09-08) stays armed on its own bands; `S132` (±9.00pp) is **pre-declared NO-INFORMATION** (`M1197`) and is restated as such here so a later reader cannot mistake its `C` for evidence (`D451`). **This card registers no new row** (`D343` — three already point at this event). |
| **Cell** | **Not a candidate. Hand-off to PREMORTEM** as the ≤48h binary that must carry a both-sides bracket. |
| ⚠ | **`module_disclosure_us AVGO` has still never been opened** — the contracted-share question the 09-01 run raised is `unknown` for a **second** run, hours before the print (`C3`). Named, not filled in. |

## Card 8 — ★★ **The FTC/22-state suit attacks `AMZN`'s highest-margin line**

| | |
|---|---|
| **Thread** | *"FTC sues Amazon for manipulating ad auction prices"* **FADING 4→9→5→4→13→13→5** ⚠ (partial-day) — **peak 13 on two consecutive days** |
| **Direction (body-read)** | *"FTC alleges Amazon illegally made **$20 billion** by rigging billions of ad auctions"* [arstechnica 09-01] · *"secret ad surcharge scheme"* [techcrunch, yahoo_finance] · *"FTC Lawsuit Puts Amazon's (AMZN) **High-Margin Advertising** Business in Focus"* [08-31]. ⇒ **a margin-line attack, not a headline-risk story** — advertising is the segment carrying the group's incremental margin. |
| **Exposure** | **`AMZN`** · **🔴분산**, OBV **−0.463 — the worst in this entire card set**, `rs20` −6.9 vs **`SPY`**, `vol_surge` 0.75, Δ +0.062 |
| **Future — branch 1 / branch 2** | **1**: the suit reaches a remedy phase or a second jurisdiction joins ⇒ the ad-margin line is repriced; **KPI** `AMZN` OBV stays < −0.30. **2 / KILL**: `AMZN` OBV recovers above 0 by **2026-09-15** ⇒ the tape read it as headline risk and the card is dropped. |
| **Cell** | **STORY-ONLY → watchlist, dated re-check 2026-09-15.** ⚠ **PREFLIGHT G3 bars any `wflow` verdict on Consumer Discretionary because `AMZN` is 40.2% of it** — so this card is explicitly a **name-level** observation and must not be laundered into a sector call by ROTATION. |

---

## 9 · Book cross-check — ENDED/challenged threads under open positions

| position | real-book weight | thread it rides | state | flag |
|---|---:|---|---|---|
| **`NVDA`** | **21.3%** | Card 6 (Nvidia supply-chain) | REIGNITED, but the name is **distributed on 1.38× volume with `[FINRA]` z +2.18** | ⚠ **story alive, money leaving** |
| **`ANET`** | **14.6%** | Card 6 | the thread's own direction is an attack on this layer; **z +2.25, the board's largest short build**; Δ −0.494 | 🚨 **flagged to the book desk** |
| **`ETN`** | **7.5%** | Card 4 (AI-power) | the card's **falsifier** gained 3 outlets this week; Δ **−0.633** | 🚨 **flagged** |
| **`PSX`** | **14.7%** | Card 2 (Hormuz) | thread alive, OBV **+0.301 매집**, `rs60` **+34.4** — **misses 🟢 by 0.01 on `vol_surge`** | ✅ story and money agree; the tag does not |
| **`MPC`** | 7.4% | Card 2 | OBV **+0.425**, `rs60` **+42.9** | ✅ |
| **`T`** | **13.8%** | **no thread, no thesis** | OBV **+0.409 매집**, `rs60` +11.0 | ⚠ **carried as an open gap for a 2nd run (P5)** |
| **`CBRE`** | **2.8%** | **no thread, no thesis — new this run** | **🔴분산**, OBV −0.251 | ⚠ **newly surfaced; 16.6% of invested capital now has no thesis** (with `T`) |
| **`RTX`** | 7.9% | rearmament (not selected this run) | 🔴-ish; `[FINRA]` z +1.21 · a standing `K.본문반증` rejection sits on its thread | ⚠ carried |

## 10 · Ledger writes — the funnel's widest stage gets a scoreboard

**Rejections filed** (`reject_ledger add`, each with `--revives-if` and `--recheck-date`):
- **`HWM`** `I.테제반증` — the thread's headline says it benefits; the body says a new entrant attacks
  its bottleneck and the tape already knocked it. Revives if OBV > 0 **and** `rs20` > 0 vs `SPY`.
  Re-check **2026-09-10**.
- **`GEV`** `A.flow미도착` — the named "cashing in" OEM is 🔴분산 with OBV −0.259. Revives if the tag
  reaches 🟢 or OBV > +0.10. Re-check **2026-09-10**.

**Misses filed** (`missed_ledger add`, each with `--enters-if`):
- **`PSX`** `M.숏리스트탈락` — accumulating (OBV +0.301, `rs60` +34.4) and **excluded by 0.01 of
  `vol_surge`**. Enters if `vol_surge ≥ 1.00`. Re-check **2026-09-09**.
- **`CVX`** `M.숏리스트탈락` — OBV **+0.342 매집**, `rs20` +12.1, `vol_surge` **0.99**. Same gate, same
  0.01. Enters if `vol_surge ≥ 1.00`. Re-check **2026-09-09**.
- **`EOG`** `M.숏리스트탈락` — **Δ +0.693, the universe's 2nd-largest**, OBV +0.082, surge 0.98.
  Enters if OBV > +0.15 **and** `vol_surge ≥ 1.00`. Re-check **2026-09-09**.
- **`FANG`** `M.숏리스트탈락` — **Δ +0.840, the universe's largest**, surge 1.03 but OBV only +0.051.
  Enters if OBV > +0.15. Re-check **2026-09-09**.
- **`CEG`** `Q.확신부족` — the only AI-power name with positive OBV and positive `rs20`/`rs60`, inside
  a card the desk filed STORY-ONLY. Enters if 🟢 or `P127` fires A. Re-check **2026-09-10**.
- **`FRO`** `N.유니버스부재` — the freight leg the body-read identified; **priceable, not taggable**.
  Enters if `us_top300` is rebuilt to include it. Re-check **2026-09-09**.
- **`LNG`** `N.유니버스부재` — the gas leg; *"LNG Exports Through Hormuz Remain Stalled"* while oil
  rebounds, and **the desk has logged this name as untaggable for 10+ runs**. Enters on the same
  condition. Re-check **2026-09-09**.

## ✅ EXIT CHECK
- [x] **Scope market-correct** — `--scope foreign` on every `brief`, `thread`, `fts`, `chain-hop` and
      `theme-age` call in this stage. No card cites a domestic feed.
- [x] **Selection logged** — 138 alive → **8 selected**, **130 not selected**, rule stated in §0, four
      same-story threads consolidated rather than double-counted.
- [x] **Direction body-read on every card** — and it **changed the verdict on Card 1** (headline
      "incumbents cash in" vs body "entrant knocks the incumbent") and **sharpened Card 2** (freight
      and margin, not barrels). No card rests on a headline.
- [x] **Every exposure name carries a flow tag with its asof date (2026-09-01)** and a crowding note.
      **STORY-ONLY names did not leak into the hand-off** — only `SLB` and `WMB` (Card 2,
      CONFIRMED-EARLY) go to ROTATION/BET.
- [x] **Every card has both branches, a kill condition and a dated horizon.**
- [x] **ENDED/challenged-thread book flags emitted** (§9), including two positions totalling **16.6%
      of real invested capital with no thesis at all**.
- [x] Ledger writes listed in §10 and executed against `reject_ledger` / `missed_ledger`.
- [x] **No sizing anywhere (P4).**

---
> Handed to ROTATION: **`SLB` · `WMB`** (CONFIRMED-EARLY) · the Card 2 ↔ `P126` contradiction
> (`FANG`/`EOG` carry the universe's two largest Δ and are **barrel** names) · the Card 4 ↔ Utilities
> contradiction already raised in `SWEEP_READ §4`. Handed to PREMORTEM: **Card 7 (`AVGO`, D-0)**.
