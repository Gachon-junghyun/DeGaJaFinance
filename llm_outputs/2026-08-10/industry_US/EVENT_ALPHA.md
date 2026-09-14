# EVENT_ALPHA — industry_US · 2026-08-10 · Stage 5/11 (L1·EVENT_ALPHA)

> Bottom-up: which stories ARE building, and is money already following. `--scope foreign` on every
> news call (hard rule). Analytical only — **this stage never sizes** (P4).

## 0. Selection log — no silent truncation

`thread --days 7 --scope foreign`: **4,114 daily events → 3,183 threads → 509 multi-day → 136 ALIVE.**
**8 selected · 128 not selected.** Precursor-form first (curve starting ≤2 outlets and climbing),
then BUILDING/REIGNITED by peak reach.

⚠ **The selection universe is itself narrower than the day**: **431 single-outlet clusters were not
opened**, and on `--scope foreign` that tier is **UNSCORED** (the relevance classifier is Korean-only),
so it is a random sample rather than a ranked tail. **No card below claims a topic is absent.**

## 0a. 🚨 Two flow-instrument warnings that bind every card

**① The tags here come from TWO producers and they disagree by construction (`D208`).**

| Producer | asof | velocity axis |
|---|---|---|
| `SECTOR_FLOW_US.json` (the sweep) | **settled 2026-08-07** | **DEAD — 0/300** |
| `module_flow <tickers> --bench SPY` | ⚠ **LIVE 2026-08-10 intraday** (the market opened 09:30 ET) | **ALIVE — 0.57×–3.18× on every name queried** |

★★ **That contrast is itself a measurement, and it localises the defect.** `module_flow` returned a
populated `news_velocity` for **24 of 24** names queried this run while `sector_flow` returned **0 of
300** on the same morning against the same news API. ⇒ **the news pipe is alive; the SWEEP's per-name
velocity lookup path is what is broken.** (The KR desk measured the identical split as `M545`; this is
an **independent US measurement of the same code path**, not a cross-market import — W1 respected.)

**② Every `module_flow` number in this file is an OPEN-MARKET bar and is labelled `[live]`.**
**Settled tags are labelled `[settled 08-07]` and come from the sweep JSON.** Where they disagree,
**the settled one governs the verdict and the live one is context.** This is `D74` handled, not avoided.

---

## Card 1 — ★★★ Hormuz: the reopening condition was NAMED, and it is not the Oman deal

- **Thread**: two of them, and **their curves diverge, which is the finding.**
  - *price leg* — `"Oil rises amid uncertainty over U.S.-Iran Strait of Hormuz deal"` · tagged FADING
    on the 7-day shape · outlet curve **22 → 13 → 13 → 16 → 6 → 7 → 17** — **the last three days are
    6 → 7 → 17, re-accelerating**, and today it is the day's **largest cluster (30 articles / 17 outlets)**.
  - *diplomacy leg* — `"Iran says it will reopen the Strait of Hormuz — as soon as the U.S. …"` ·
    outlet curve **8 → 18 → 14 → 12 → 15 → 9 → 4** — **attention decaying while the statement gets
    more concrete.** Window denominator: **2,209 articles → 349 events**.
- **Direction (body-read, not headline)**: **the IRGC named the conditions** — reopening happens
  *"once the US accepts its conditions"*, and the conditions are **an end to the US naval blockade**
  and **compensation for war damages** `[dw body 08-08]` `[aljazeera body 08-09]`. ★ **The same
  statement says the reopening *"does not depend on how talks with Oman develop."*** ⇒ **the Oman
  track — which every desk file since 08-05 has watched — is named by the controlling party as not
  the path.** Today: *"hopes for a reopening faded after Iran raised additional demands"*
  `[seekingalpha body 08-10]`.
- **Exposure** (chain position · tag · crowding):
  | Name | Chain position | `[settled 08-07]` | `[live 08-10]` | Crowding |
  |---|---|---|---|---|
  | **XOM** | integrated, headline layer | 🟡 +0.592 · OBV 매집 · RS20 +7.8 · **RS60 −3.2** | 🟡 vel 1.17× | headline layer by construction |
  | **CVX** | integrated, headline layer | 🟡 +0.449 · RS20 +3.3 · **RS60 −4.4** | 🟢 vel 1.21× | headline layer; ⚠ its live driver is Project Kilby, **not** crude (§3a) |
  | **STNG · FRO** | tanker rate, one hop past the barrel | 🚫 **NOT MEASURABLE — outside the sweep universe** | STNG 🔴 분산 · FRO 🟡 중립 (live) | **S61's own two legs** |
  | **MPC · VLO · PSX** | refining margin, two hops | 🟡 +0.414 / +0.535 / +0.394 · all OBV 매집-or-중립 · **RS60 +13.6 / +16.0 / +11.5** | MPC 🟢 · VLO/PSX 🟡 | the only leg with a positive 60-day base |
- **Future — both branches, dated**:
  - **IF the conditions bind** (thread keeps re-accelerating on the price leg) → crude and the
    distillate crack stay bid; **S61's tanker leg and S67's refiner leg are the live objects**;
    track **S61's EW{STNG,FRO} 5-session excess, settled −4.184**, and the oil/Hormuz outlet curve
    (**17 today**). **Horizon 2026-08-12 (S61 settles).**
  - **ELSE — kill condition**: an **unconditional** Iranian reopening statement, or a dated US
    stand-down on the naval blockade. **Either kills this card outright.**
- **Cell**: **CONFIRMED-EARLY on the refining leg** (money and story both present, 60-day base positive)
  · **STORY-ONLY on the tanker leg** — and it is story-only *because the desk cannot measure it*, not
  because the money is absent. **Handed to ROTATION as ENRG evidence; the tanker names are NOT handed
  to BET** (§6).
- 🚨 **`S8`**: this card's object is S8's trigger, and S8 has been undated `[blank]` for **nine runs**.
  **PREMORTEM receives the named conditions.** MACRO/EVENT_ALPHA do not register (stage ownership).

## Card 2 — ★★★ The distillate bottleneck the desk just wrote off has been physically attacked twice

- **Thread**: `"Ukraine hits refineries deep inside Russia"` — **7 days, outlet curve 14 → 17 → 20 →
  19 → 12 → 11 → 10, peak 20**, the most persistent thread on the board. Plus a second, separate
  event stream: **Houthi strikes on Saudi refining**, 67 hits / 3 days.
- **Direction (body-read)**: **two named refining assets struck in four days.** *"Ukrainian Drone
  Strike Kills 12 in Major Attack on Russian Refining Hub"* `[oilprice body 08-10]`; *"Fire at
  Russia's Ilsky Refinery"* `[bloomberg 08-08]`; ***"Fire erupts at Saudi Aramco's Jazan refinery"***
  after the kingdom signed a defence pact `[scmp · euronews bodies 08-09]`.
  ★ **Against this, the desk withdrew `P4⁗` on 08-07 and `P38` left Energy's N+ on flow alone.**
- **Exposure**: **MPC** 🟡 +0.414 · RS60 **+13.6** `[settled]` / 🟢가속 vel **1.48×** `[live]` ·
  **VLO** 🟡 +0.535 · RS60 **+16.0** / vel 1.01× · **PSX** 🟡 +0.394 · RS60 **+11.5** / vel **1.92×**
  — ⚠ **all three are 🟡 on the settled instrument and up to 🟢 on the live one; `D208` binds.**
  Headline layer: XOM/CVX (marked as such).
- **Future — both branches, dated**:
  - **IF supply stays impaired** → **S55 branch B (HO%−CL% ≥ +6.5 from the 08-04 anchor)**. The
    settled reading is **+0.318**; the **08-10 electronic session reads +3.097** — distillate
    outrunning crude **+4.39% vs +1.71%**. ⚠ **The live number is context, NOT a score.**
    **Track: S55 at the 2026-08-11 settle · S67 at 08-13.**
  - **ELSE — kill condition**: the **08-11 settle** brings the spread back to or below **zero**,
    ⇒ the Monday move was an overnight risk premium and P4⁗'s withdrawal was right on the mechanism
    as well as the threshold. ⚠⚠ **P4⁗ stays withdrawn either way** — a threshold moved after the
    fact is a description, not a forecast (L3).
- **Cell**: **CONFIRMED-EARLY** (persistent thread + positive 60-day base + a same-week catalyst),
  ⚠ **with the honest qualifier that its price leg is unsettled.** Handed to ROTATION as the
  contested half of ENRG's N+.

## Card 3 — ★★★ CXMT: a second DRAM source is being qualified at a tier-1 Western OEM

- **Thread**: **43 hits / 3 days, 5+ outlets**, entering the body tier today
  (`"Apple Tests China's CXMT Memory Chips for iPhones and MacBooks"`, 15 articles / 4 outlets).
  ⚠ **New thread — no multi-day curve yet.**
- **Direction (body-read)**: **Apple is *testing*, not buying** — *"Apple tests China's CXMT memory
  chips for iPhones and MacBooks, WSJ reports"*; the framing is **shortage-driven pull**
  (*"The Memory Shortage Pushes Apple Toward China's CXMT"*), not political push. Separately
  **CXMT cleared DDR5-8800 on an AMD platform**, described as *"closing the gap with SK hynix"*
  `[tomshardware body 08-08]`.
- ★★★ **Why this card exists at all**: `STANDING_VIEW §4`'s governing asymmetry is **demand-side**
  (*a capex CUT changes the thesis, a RAISE only moves timing*), and **M7** dates new supply at
  **mid-2027 / 2028**. **A qualified Chinese DRAM supplier at Apple is neither leg.** The desk's
  regime call is exposed on a third side **and no bracket touches it.**
- **Exposure**: **MU** 🔴분산 −0.817 · RS20 −12.8 · **RS60 +9.7** `[settled]` (vel 1.22× live) ·
  **WDC** 🔴 −0.556 · RS20 −27.9 · RS60 −15.9 · **SNDK** 🔴 −0.589 · **RS20 −39.2, the board's worst**
  · **STX** 🟡 −0.024 · RS20 −13.1 · **AAPL** 🟡 +0.027 · RS20 −3.1 (the *buyer*, and W4's answer:
  **name the customer** — here the customer is named and it is looking elsewhere).
  ⚠ **The memory complex is already 🔴 on the settled instrument before this story.**
- **Future — both branches, dated**:
  - **IF this reaches HBM or a supply agreement** → the LTA price floor that **open contradiction C1**
    rests on is capped from a source the chain does not model. **Track: MU's revision breadth
    (carried at FY 29↑/1↓, +26.7%/90d) and any Apple or CXMT filing.**
  - **ELSE — kill condition**: an Apple statement, or a Micron/SK LTA disclosure showing the price
    term unchanged; **or** the item staying inside commodity DDR5 and never touching HBM.
    **Dated re-check: 2026-08-19.**
- **Cell**: **STORY-ONLY.** ⚠ **Explicitly NOT handed to BET.** The money axis is 🔴 on three of five
  exposure names and the evidence is `[news]` second-hand (WSJ via aggregators) with **no issuer
  filing** — the M122 grade. **Watchlist with a dated re-check.**

## Card 4 — ★★ Behind-the-meter power: the precursor-form thread on this board

- **Thread**: **the only ≤2-outlet climbing thread with a market mechanism.**
  `"Amazon's new 7.65 GW Texas AI data center power plant"` (08-09, 2 outlets) →
  `"Data-Center Backlash Leads to a New Land Rush in Texas"` (08-10, 2 outlets) — **BUILDING 2 → 2**,
  alongside `"AI data center bans surge past 500 nationwide as local US [opposition grows]"` (2 outlets)
  and the head-tier `"Tech leaders say AI means less work"` cluster (17 articles / 10 outlets).
- **Direction (body-read)**: **local permitting is becoming the binding constraint, and the response
  is to route around the grid.** This is the same mechanism the desk already logged on **Project Kilby
  — a 20-year, 2.67 GW behind-the-meter gas deal with Microsoft, routed AROUND the ERCOT queue** —
  which **PREMORTEM Lens 4 used on 08-08 to kill an EVENT_ALPHA kill condition** (the R46 class).
  ⇒ **the mechanism is broadening from one deal to a category.**
- **Exposure**: **VST** 🔴분산 −0.361 · RS20 −13.9 · surge **1.55** `[settled]`, vel **2.27×** `[live]`
  · **CEG** 🟡 −0.034 · RS20 +4.9 · **RS60 −12.8**, vel 1.86× · **NRG** 🚫 **outside the universe**
  (vel **3.18×**, surge **1.90×** `[live]` — the loudest of the three and unmeasurable by the sweep)
  · **GEV** 🔴 **−0.850, the worst of 300** · **ETN** 🟡 +0.654 · OBV 매집 · RS20 +7.7 · **RS60 +7.0**
  · **PWR** 🟡 −0.033 · **RS60 −17.0**.
- ★★ **The card's real content is the contradiction**: **the news axis on the merchant-power trio is
  the loudest on the board (2.27× / 1.86× / 3.18×) while the settled money axis is 분산 on all three.**
  **Story without money** — and the desk's registered position is that this is *not* a signal.
- **Future — both branches, dated**:
  - **IF** behind-the-meter procurement converts to disclosed contracts **and** the flow turns → the
    UTIL UW (worst 20-day excess on the board, −6.39) is being carried into a re-rating.
    **Track: VST's OBV state and `vol_surge`; GEV's current-year revision breadth (7↑/10↓).**
    **Horizon 2026-08-14 (GEV/CAT/EMR ledger re-checks) and 2026-08-20 (VST ledger row).**
  - **ELSE — kill condition**: the flow stays 분산 through **08-20** ⇒ the 500-ban story is a
    permitting story, not an earnings story, and the UW is right.
- **Cell**: **STORY-ONLY** (loud narrative, dispersing money). ⚠ **Not handed to BET.**
  ⚠ **NOT filed as DEAD** — DEAD requires FADING/ENDED **×** 🔴, and this thread is BUILDING.

## Card 5 — ★★ The dollar: a two-month trough in the feed against a crowded long in the data

- **Thread**: `"Dollar near two-month trough as US inflation data awaited"` — **REIGNITED**, outlet
  curve **3 → 4 → 6 → 5**, **20 articles / 5 outlets today**; sub-cluster *"Dollar steadies after
  payrolls drop, yen falls"*.
- **Direction (body-read)**: the feed attributes the trough to **the payroll print and the pending
  CPI**, i.e. a rate-differential story, not a credit story — consistent with **HY OAS tightening to
  2.71** rather than widening.
- **Exposure**: **UUP −0.35%/5d, −1.13%/20d** with **FXY +2.64%/20d** and **FXE +1.31%/20d** agreeing
  in sign `[settled 08-07]` (**D5**) — against **CFTC COT USD Index at the 81st percentile and
  ADDED +5,302** ⚠ **on a Tuesday-08-04 snapshot that pre-dates NFP.** Equity exposure:
  **NEM** 🟡 +0.476 · **RS20 +16.1** / RS60 **−10.4** · **FCX** 🟡 +0.130 · RS20 +10.7 ·
  **LIN** 🔴 **−0.683** (and the sector's `top1_flips_sign` name).
  🚨 **`DTWEXBGS`, the desk's own broad-dollar series, last printed 2026-07-31 — six publication days.**
- **Future — both branches, dated**:
  - **IF the crowded long is the marginal seller** → dollar weakness extends and supplies **the one
    non-NEM mechanism under S57 branch A**. **Track: UUP, and `DTWEXBGS` the moment it prints.**
    ⚠ **UUP is a DXY-basket proxy and `DTWEXBGS` is the BROAD trade-weighted index — different
    objects; no UUP value is substituted for a `DTWEXBGS` value (D1/D2).**
  - **ELSE — kill condition**: a hot **08-12 CPI** that reprices September and lifts UUP **while the
    COT long keeps building** ⇒ the position was never the marginal seller. **Horizon 2026-08-12.**
- **Cell**: **LATE-MONEY caution rather than a candidate** — the story is broadly narrated (5 outlets)
  and the position is at the 81st percentile. **Handed to ROTATION as the MATR cross-check, not to BET.**

## Card 6 — ★★★ Newmont pays Barrick $1.95bn, and it lands on the carrier of a live bracket

- **Thread**: **NEW, today, 5 outlets** including a primary press release — `"Barrick and Newmont
  Reach Agreement Regarding Nevada Gold Mines Joint Venture"` `[globenewswire]`, `[nasdaq body]`,
  `[wsj]`, `[mining]`. Adjacent: **`"Barrick Reports Second Quarter 2026 Results"`, same day.**
- **Direction (body-read — and the headline gets it backwards)**: **NEWMONT WILL PAY BARRICK
  $1.95 BILLION** to contribute excluded properties into the Nevada Gold Mines JV and settle all
  disputes; **Newmont formally consented to Barrick's proposed IPO of its North American gold assets.**
  ⚠⚠ **The WSJ headline reads *"Barrick Mining Settles Newmont Nevada Dispute for $1.95 Billion"***,
  which parses as Barrick paying. **A headline-only card would have had the cash flowing the wrong way**
  — the exact failure this stage's EXIT CHECK exists to prevent.
- **Exposure**: **NEM** 🟡 +0.476 · OBV 매집 · **RS20 +16.1** vs **RS60 −10.4** `[settled 08-07]`,
  🟢가속 vel **1.51×** `[live]` — **and it is ~85% of S57's entire observable** (XLB exc5 **+1.31**,
  ex-NEM **+0.194**, M502/M572). **NEM alone: +7.16% on the session, +20.56% over five, = +6.55pp /
  +17.05pp excess vs SPY.** **Barrick (B)** 🚫 **not in the universe at all** (foreign domicile) —
  **−7.99% on the live bar** after **+5.58%** settled Friday.
- ★ **Chain note (W4)**: this is **not a gold-price event and not a materials-cycle event.** It is a
  JV restructuring, a cash transfer and an IPO consent. **The desk's Materials reading rests on it.**
- **Future — both branches, dated**:
  - **IF S57's branch A (XLB 5-session excess > +1.9) fires** on this — 0.59pp away, firing at **any**
    settled close through **08-12** — **it fires on a one-name M&A event and means nothing about
    Materials.** **Track: XLB exc5 and XLB exc5 ex-NEM (+0.194 at last measurement).**
  - **ELSE — kill condition**: XLB's **ex-NEM** excess turns positive on a settled close ⇒ there is a
    real sector leg and this card is wrong to discount it. **Horizon 2026-08-12 (S57 settles).**
- **Cell**: **CONFIRMED-EARLY as evidence, NOT as a candidate.** ⚠ **NEM is not handed to BET** — it
  is 🔴RESOLVED with a ledger row already filed (08-13) on **revision breadth cut 9-to-1**, and this
  card does not revive it. **It is handed to PREMORTEM to extend `S57-ANNEX`.**

## Card 7 — ★★ Intel's $15bn equity raise into its own rally

- **Thread**: **REIGNITED 6 → 7**, `"Intel plans $15 billion share sale as turnaround rally lifts
  [the stock]"` — **15 articles / 7 outlets today**.
- **Direction (body-read)**: an issuer selling **$15bn of equity into a rally** is the funding-mode
  signal the desk already tagged on **GOOGL (negative FCF −$5.86bn and a $49.6bn equity raise, M134)**
  — the same shape, a second issuer. **Dilution is disclosed and dated; the rally is the reason given.**
- **Exposure**: **INTC** 🔴분산 **−0.800** · RS20 −9.9 · **RS60 −20.5** · vel **0.66× (below 1)**
  — **the story is loud in outlets and quiet in term velocity, on a name the money is leaving.**
  Adjacent: **AMD** 🔴 −0.589 · RS60 +3.1 · **MU** 🔴 −0.817.
- **Future — both branches, dated**:
  - **IF** the raise is absorbed and IT's week-leading tape holds (**XLK exc5 +3.69, best sector**)
    → the sector's two windows resolve upward and the IT `N` is too cautious.
  - **ELSE — kill condition**: INTC's flow stays 🔴 through **2026-08-19** and XLK's exc20 (**−1.25**)
    does not turn ⇒ the week's leadership was a rebound, not a turn.
- **Cell**: **LATE-MONEY** — narrative present, money 🔴, and a dilution event dated. **Not handed to
  BET.** Filed to the **missed ledger is NOT appropriate** (it cleared no money axis); **filed as a
  watchlist item with the 08-19 re-check.**

## Card 8 — ★★ Warsh's Fed refuses forward guidance while three speakers lean hawkish

- **Thread**: **REIGNITED, outlet curve 6 → 7 → 6 → 9**; today `"New Fed Chair Kevin Warsh Has
  Refused to Give Forward Guidance"` **14 articles / 9 outlets**, with `"How Kevin Warsh is rewiring
  the Fed"` and `"Morning Bid: Fed's Cook grilled again"` as sub-clusters. Earlier in the window:
  `"Trump Said to Call Warsh In Latest Signal of Push to Remove [Cook]"` (7 outlets).
- **Direction (body-read)**: **a policy-communication regime change, not a policy change** — the
  desk's carried M549 has **Cook "prepared to act" on a hike, Musalem "should have hiked at the last
  meeting", Kashkari "gradual rate hikes in 2026"** against futures that repriced **September 55% →
  44% while December HELD at 77%** (M504). ⇒ **the committee is arguing with its own data, and the
  chair has removed the instrument that usually settles it.**
- **Exposure**: **JPM** 🟡 +0.297 · OBV 매집 **+0.374** · RS20 +3.8 · **RS60 +12.5** ·
  **BAC** 🟡 +0.325 · OBV **+0.296** · **RS60 +19.6** `[settled]` — ⚠ **and Financials' breadth is
  1 green of 47** (§SWEEP). **Duration side: VST/CEG/NEE-complex and RE, both UW.**
- **Future — both branches, dated**:
  - **IF** guidance stays absent, realised vol on rate-sensitives rises and **S51/S66/S70's readings
    matter more, not less** — ⚠ **and all three are blocked because `[FRED]`'s yield/credit block
    stops at 08-06 for a fourth run.**
  - **ELSE — kill condition**: a Warsh statement giving explicit forward guidance, **or** the
    December hike probability printing below 60% (P37's registered line). **Horizon 2026-08-12 (CPI).**
- **Cell**: **STORY-ONLY** — it moves the *variance* of every rate-sensitive card without moving a
  name. **Handed to ROTATION as context; no candidate.**

---

## 5. Book cross-check — ENDED threads under open positions

| Position | Thesis rides on | Thread state | Flag |
|---|---|---|---|
| **VST** (paper book) | AI-power / merchant power | **BUILDING** (Card 4) | ⚠ **story alive, money 분산 for the 3rd run** — the position's thesis is alive and its money is not. **Not an ENDED flag; a money flag** |
| **KMI** (paper book) | energy-fuel / AI-power gas | no dedicated thread in the alive set; the adjacent one is **ADNOC Gas $8.2bn expansion** (13/6) — **a supply expansion, i.e. the wrong side** | ⚠ **flagged**: KMI 🟡 −0.381 · RS20 −6.4 · RS60 −9.7 `[settled]`. **Thesis has no live thread of its own** |
| **LNG · TSM** (paper book) | LNG export / AI-compute | 🚫 **cannot be flow-checked — outside the universe, 11th run** | **"not measured," never "no signal"** (§6) |
| **MPC · PSX** (real KIS account) | refining | **Card 2, the board's most persistent thread** | ✅ story and 60-day money both present |
| **RTX** (both books) | missile-defense | adjacent: *"Egypt could be the latest addition to the Mecca defense pact"* (**BUILDING 2 → 3**) | ✅ 🟡 +0.639 · OBV **+0.360** · RS20 +11.4 · **RS60 +19.9** — the book's strongest settled 60-day base |

## 6. 🚨 A universe finding this stage tripped over, and it is not staleness

Three cards above needed a flow tag the sweep cannot produce. Checking why:

| Name | Card | mcap (v2 file, built today) | In `us_top300`? |
|---|---|---|---|
| **LNG** (Cheniere) | held | **$52.90B — rank 233** | ❌ |
| **TSM** | held | **$2.18T — rank 7** | ❌ |
| **NRG** | Card 4 | $24.83B — rank 388 | ❌ (legitimately below the cutoff) |
| **STNG · FRO** | Card 1 / **S61's own legs** | $3.81B · $8.85B | ❌ (legitimately below) |
| **B** (Barrick) | Card 6 | not in the 1,522-name file either | ❌ (foreign domicile) |
| *reference* — the file's own 300th name | — | **KMB $34.04B** | ✅ |

★★★ **`us_top300.csv` excludes LNG at $52.9B while retaining KMB at $34.0B.** Checked against
staleness rather than assumed: **LNG closed $255.83 on 2026-07-15 (the file's build date) and $256.14
on 08-07 — +0.1%**, so its market cap on the build date was ~$52.8B, **≈55% above the file's own
300th-place cutoff.** ⇒ **the absence is NOT staleness. The file applies an unstated
membership/domicile filter, and its name asserts a size rank it does not implement.**
⇒ **`D234`.** ★ And a **live bracket is affected**: **S61's two legs (STNG, FRO) are structurally
outside a top-300 universe**, so the desk brackets a pair its primary flow instrument can never tag.

---

## 7. Hand-off

- **To ROTATION** — Card 1 (ENRG, refining leg confirmed / tanker leg unmeasurable) · Card 2 (the
  contested half of ENRG's N+) · Card 4 (UTIL: loud story, dispersing money) · Card 5 (MATR
  cross-check) · Card 6 (**MATR may not be called on XLB's aggregate**) · Card 8 (rate context).
- **To PREMORTEM** — Card 1's **named Hormuz conditions** (the object `S8` has lacked for nine runs)
  · Card 6 for **extending `S57-ANNEX`** · Card 3 as **an un-bracketed exposure of the regime call**
  · ⚠ **and CPI at 47h12m ⇒ a both-sides bracket is MANDATORY.**
- **To BET §B** — **CONFIRMED-EARLY candidates: the refiner leg only (MPC · VLO · PSX).** Everything
  else is STORY-ONLY or LATE-MONEY and **did not leak into the candidate hand-off.**
- **Ledgers** — **no new rejection is filed by this stage** (no card reached a DEAD verdict: DEAD
  requires FADING/ENDED **×** 🔴 on both axes, and every card here has at least one axis alive).
  **No missed-ledger entry either** — the two cards that cleared the money axis (1's refining leg, 2)
  **were both turned into candidates**, which is the condition under which no `M.숏리스트탈락` row is owed.
  **Both `due` lists were empty at HANDOVER and remain so.**

## ✅ EXIT CHECK

- [x] **Scope market-correct** — `--scope foreign` on every `brief`, `thread`, `fts search` and
      `blindspot` call in this stage. No `--scope all`, no domestic feed
- [x] **Selection logged** — 136 alive → **8 selected, 128 not selected**, plus the 431 unopened
      single-outlet clusters named as a narrower-than-the-day caveat. **No silent cap**
- [x] **Direction body-read on every card** — and it changed a reading on Card 6 (the WSJ headline
      reverses the direction of a $1.95bn payment) and on Card 1 (the IRGC excludes the Oman track)
- [x] **Every exposure name carries a flow tag with its asof** — and the **two producers are labelled
      separately** (`[settled 08-07]` sweep vs `[live 08-10]` `module_flow`, `D208` + `D74`), with the
      settled one governing every verdict
- [x] **Every card has both branches, a kill condition and a dated horizon**
- [x] **STORY-ONLY names did not leak into the candidate hand-off** — only the refiner trio is handed
      to BET; Cards 3, 4, 5, 7, 8 are explicitly withheld
- [x] `EVENT_ALPHA.md` written; ENDED/money-flag book cross-check emitted (§5); ledger state stated (§7)
- [x] **No position sizing, no buy/sell language (P4)**

---

## ADDENDUM (appended at PREMORTEM, same run) — §6's stated CAUSE is refuted; its measurement stands

> ⚠ **Written by append, not by editing §6.** The desk's rule is that verification arriving after an
> assertion is a finding, and the earlier sentence stays visible (the `D48` pattern). This is an
> instance of it inside this run's own output.

**What §6 asserted**: that `us_top300.csv` applies *"an unstated membership/domicile filter"*, and it
listed Barrick's absence under **foreign domicile**.

**What the next measurement showed** — the domicile half is wrong:

| Name | Domicile | mcap (v2 file, built 2026-08-10) | in `us_top300`? |
|---|---|---|---|
| **ASML** | Netherlands | $668.71B — rank 18 | ✅ **IN** |
| **ARM** | UK | $301.78B — rank 42 | ✅ **IN** |
| **TSM** | Taiwan | **$2.18T — rank 7** | ❌ ABSENT |
| **LNG** (Cheniere) | US | **$52.90B — rank 233** | ❌ ABSENT |
| *reference:* **KMB** | US | **$34.04B** — the file's own 300th | ✅ IN |

⇒ **Two foreign-domiciled names ARE in the file and the largest company on the list is not**, so
**domicile does not explain the exclusions.** Nor does size: LNG at $52.9B is out while KMB at $34.0B
is in, and §6 already ruled out staleness by price (LNG +0.1% between the build date and 08-07).

**What survives** — and it is the part that binds the desk:
1. **`us_top300.csv` is not a market-cap top 300.** Measured three ways, unchanged.
2. **The exclusion rule is `[unknown]` (C3)** — neither size, nor domicile, nor staleness accounts
   for it. **"Unknown" is the honest column value; it is not "index membership".**
3. **The consequences are unchanged**: `LNG` · `TSM` (held) and `STNG` · `FRO` (both legs of `S61`)
   and `NRG` · `SMCI` · `TLN` carry **no flow/RS/OBV/short verdict** from this instrument —
   **"not measured", never "no signal".**

⇒ **`D234` is re-scoped at registration rather than after it**: the dig is *"the universe file's
inclusion rule is undocumented and unexplained by size or domicile"*, **not** *"it filters by index
membership"*. ★ **Registering the cause as `[unknown]` is the point** — the 08-09 run's own headline
was that this desk's dominant failure is naming the wrong object, and a confident wrong cause on the
registration line would have been exactly that.
