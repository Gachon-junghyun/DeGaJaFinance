# EVENT_ALPHA — industry_US · 2026-08-27 (Stage 5 / L1·EVENT_ALPHA)

> Bottom-up complement to MACRO's top-down matrix: **which stories ARE building, and is money already
> following.** Scope **`--scope foreign` on every call** (market-locked). Analytical only, no sizing (P4).
> Flow tags are from **this run's own sweep, asof 2026-08-27**, which is a **pre-market stub bar**
> (median volume 4.65% of the prior session) — so **`vol_surge` and the 🟢/🟡/🔴 tag are declined
> throughout**, and only `OBV` state, `RS20`/`RS60` and `flow_score` **rank** are used.
> 🚫 **G1 FAIL**: no theme-freshness or velocity number appears anywhere; trajectories are outlet-count
> curves from `thread`, which are counts.

---

## §0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: **4,204 daily events → 3,221 threads → 528 multi-day → 154 alive**
(2,693 one-day, of which 244 new today).
**154 alive → 8 selected → 146 not selected.** The 146 are counted here, and the **classes** that were
excluded are named below rather than dropped silently.

⚠ **Today's last day is a PARTIAL DAY**: per-day denominators **771 · 288 · 323 · 792 · 829 · 792 ·
409** ⇒ **08-27 is 51.6% of the prior settled day**. Per `D373-KR`'s rule, **BUILDING is read as
conservative** (a partial day understates a climb) and **no FADING tag is used unless it also falls on
the full 08-26 day**.

### 🚨 `D367` reproduces, and this run measured how much of the precursor-form tier is boilerplate

The selection rule takes **precursor form first** (curve starting ≤2 outlets and climbing). Measured on
this board, that rule hands **first pick** to wire boilerplate:

| excluded class | example thread | curve | articles |
|---|---|---|---|
| **securities-litigation wires** | *Cogent … Sued for Securities* → *EquipmentShare Shareholder Alert* → *PRCT FINAL DEADLINE* → *PNR INVESTOR DEADLINE* → *REPL Investors Have Opportunity to Lead* | **2→2→2→2→2** | **142** |
| **Zacks blog highlights** | *The Zacks Analyst Blog Highlights Alphabet, Marvell…* | 2→2→2→2→2 | 42 |
| **listicles** | *3 Large-Cap Stocks on Our Buy List* / *3 Dividend Stocks to Hold for the Next 10 Years* | 3→3→2→3→4→4→7 | 94 + 79 + 24 + 16 |
| **index wraps** | *Stock Market Today, Aug. 26* | 4→6→7 | 87 |
| **non-English consumer PR** | *METLEN … Abfallverbrennung* / *LumenStim* / *Zendure* / *Swedencare* | 2→2→2→2 | 23 |

🚨 **The single largest-article multi-day thread on the board (142 articles) is a securities-class-action
wire chain, and it is in perfect precursor form.** It is not a *false* thread — those press releases
really were published — it is a thread with **no direction to body-read**. ⇒ **`M990`.**
**Six of the top ten precursor-form candidates were of this class**, and the failure is asymmetric
because each one **displaces a real card** from a hard cap of 8. Excluded by class, counted here.

⚠ **One exclusion is a judgement call and is disclosed**: *"Why Photronics' Stock Briefly Soared 27%
This Morning"* (BUILDING 5→6) describes a **real** 27% intraday move, but two of the five top bodies on
`PLAB` in the window are **`prnewswire` class-action deadline alerts**, and the headline itself says
**"Briefly"**. `PLAB` is also **outside `us_top300`** (`D341`), so this desk cannot tag its flow.
**Not carded; named here rather than dropped.**

---

## §1 · Cards

### Card 1 — 🚨 `NVDA` agrees to buy **Hugging Face** for **$12.9bn**, the day after its own print

| | |
|---|---|
| **Thread** | *"Nvidia agrees to buy Hugging Face for $12.9 billion"* · **REIGNITED** · **3→3→12 outlets** · window denominator: 154 alive threads / 4,204 daily events |
| **Direction (body-read, not headline)** | **Real, dated, and it has a four-day precursor this desk can see.** 08-23 `yahoo_finance`: *"Hugging Face exploring sale valuing it at $13 billion, Business Insider says"* [2 outlets]. 08-24 `techcrunch`: *"Hugging Face reportedly in talks to be acquired for $13B"* — body states *"It's not clear who Hugging Face has been in talks with."* **08-27**: `cnbc`, `techcrunch`, `fortune`, `yahoo_finance` all carry the agreement at **$12.9bn**, with `cnbc`'s body noting *"Deal talks began after Hugging Face…"*. **The precursor named the price four days before it named the buyer.** |
| **Exposure** | `NVDA` — **epicenter, held, largest single position**. Flow asof 2026-08-27: **OBV −0.069 중립**, `RS20` **+11.4**, `RS60` **−0.5**, `flow_score` **+0.140**, `delta` **−0.114**. **Crowding note: this is the headline layer by construction** — 5 of the 08-26 head layer's top-15 clusters are `NVDA`. |
| | `META`, `GOOGL` — one hop: the open-source-model distribution layer this acquisition consolidates. `META` **OBV +0.349 매집**, `RS20` +2.1, **`delta` +0.630 = among the board's largest positive deltas**; `GOOGL` **OBV −0.000 중립**, `RS20` −2.0. ⚠ COMM is **un-measurable at sector level by rule** (`D297`, 9th run) — these are name-level reads only. |
| **Future — branch 1** | IF the thread keeps building **AND** `NVDA`'s OBV turns 매집 on a **settled** bar → the market is pricing the acquisition as strategic rather than defensive. **Track KPI**: `NVDA` OBV state + whether a body names **antitrust review or a financing structure**. **Horizon 2026-09-10.** |
| **Future — branch 2 (kill)** | The card is **falsified** if by **2026-09-10** either (a) the deal is denied or repriced by a company statement, or (b) the thread ends without a second-source *confirmation* (all four 08-27 bodies say *"report says"* / *"reports"* — **none is a company announcement**, and that is stated here, not smoothed over). |
| **Cell · hand-off** | **STORY-ONLY → watchlist with a dated re-check (2026-09-10).** 🚫 **Explicitly NOT CONFIRMED-EARLY**: the money axis is **중립, not accumulating** (`OBV −0.069`, `delta −0.114`), and this desk's own 08-26 run was caught handing two names forward as CONFIRMED-EARLY without checking a denominator, both refuted two stages later. **This card does not repeat that.** |

### Card 2 — ★★★ The optical / interconnect turn: the headline name is a **kill**, and the tradeable layer is elsewhere

| | |
|---|---|
| **Thread** | *"Fabrinet Sees AI Optical Demand Fueling Years of Growth"* · **REIGNITED** · **5→2 outlets** |
| **Direction (body-read — and it CONTRADICTS the headline, so the headline name is killed)** | `FN` reported **Q4 FY26 on 08-24 with "record quarterly results"** (`fool`/`nasdaq` transcript bodies) — and the same body carries **`FN −3.56%`**, while a `yahoo_finance` 08-24 piece runs the line **"Fabrinet Just Lost Billions in Market Value."** **Record results plus a large negative reaction is a guidance or mix problem the headline does not name.** ⇒ **`FN` is dropped** and written to the rejection ledger (`K.본문반증`, revives-if + recheck **2026-09-10**). ⚠ `FN` is also **outside `us_top300`** (`D341`), so this desk could not have tagged its flow either way. |
| **Exposure — the layer that IS taggable** | Three in-universe optical/interconnect names, all printing **the same turn shape** (asof 2026-08-27 sweep): |
| | `MRVL` — **OBV +0.362 매집**, `RS20` **+32.6**, `RS60` **−15.3**. 🚨 **Reports TODAY**, bracketed by `S116` (settles 08-28). In today's shortlist. `C18` live on it: FINRA `z −0.64` ⇒ "✅저숏" against `module_flow`'s 08-25 **"4.8% float BUILDING"** — **neither overrules the other**. |
| | `LITE` — **OBV +0.339 매집**, `RS20` **+32.4**, `RS60` **−9.5**. |
| | `COHR` — **OBV +0.168 매집**, `RS20` **+17.9**, `RS60` **−30.3**. |
| | **Crowding note**: none of the three is in the head layer; the headline layer here was `FN`, and `FN` is the one the body-read killed. |
| **Future — branch 1** | IF the RS20-positive / RS60-negative / OBV-accumulating shape survives **settled** bars through **2026-09-09**, this is a genuine mid-cycle turn in the layer the desk has no registry row for. **Track KPI**: `RS60` crossing zero on any of the three, and `S128`'s verdict (its reversal basket contains exactly this shape). **Horizon 2026-09-09 = `S128`'s settle.** |
| **Future — branch 2 (kill)** | Falsified if `S128` settles against the `rs60` reversal, or if two of the three lose OBV 매집 on settled bars by 09-09. |
| **Cell · hand-off** | **STORY-ONLY on `FN` (dropped, ledgered) · candidates NOT handed to BET.** 🚨 **The reason is an instrument gap, and it is the 13th run of it**: `cycle_registry.json` carries **no optical/interconnect cycle**, so `cycle_exposure` **cannot emit a GAP flag** for this layer no matter what the book holds (`D250`/`M731`). `COHR` and `LITE` are written to the **missed ledger** (`Q.확신부족`, enters-if + recheck 09-09/09-10) so the opportunity cost is scored rather than invisible. **Handed to ALPHA as a registry defect, not to BET as a name.** |

### Card 3 — `NVDA`'s first-ever year-ahead forecast is what is still spreading, not the print

| | |
|---|---|
| **Thread** | *"Nvidia projects 70% revenue growth in 2028"* → *"Nvidia gave its first-ever year-ahead forecast—a 70% gro…"* · **BUILDING** · **5→6 outlets** (and BUILDING is conservative on a 51.6% partial day) |
| **Direction (body-read)** | The **print** itself is already ENDED as a thread; **the forward guide is the live object.** `nasdaq`/`fool` body: *"the company projects that full-year sales will skyrocket by another 70% in fiscal 2028. This compares to Wall Street's revenue growth estimates of 44%."* Quoted in-body from `@munster_gene`: *"guided next year revenue growth to at least 70%. The street was at 44%."* **A 26pp gap between guidance and consensus is the content**, not the beat. |
| **Exposure** | `NVDA` (held, headline layer — see Card 1 for flow). `AVGO` — **the negative-readthrough leg and it is held**: **OBV −0.103 분산**, `RS20` **−9.5**, `RS60` **−25.4**, `flow_score` **−0.715 = 🔴분산**, `delta` **−0.228**. **`AVGO` is the worst-reading held name on the board** and prints **09-02** (`S127` armed). `MU` — the memory leg: OBV **+0.125 매집**, `RS20` +4.8, `RS60` −12.1; prints 09-24. |
| **Future — branch 1** | IF the guide-vs-consensus gap closes upward (consensus revisions follow), the AI-capex cycle re-rates on **duration** rather than on a quarter. **Track KPI**: `module_fundamentals_us NVDA` next-year consensus, currently **13.13 (+4.2% / 90d, breadth 4↑:0↓ over 30d)** — branch 1 needs that to accelerate. **Horizon 2026-09-24 (`MU` print).** |
| **Future — branch 2 (kill)** | Falsified if next-year consensus fails to move by **09-24** — a 26pp guidance gap that the sell side does not follow is a credibility problem, not an upgrade cycle. |
| **Cell · hand-off** | **STORY-ONLY → ROTATION as IT cross-evidence.** ⚠ It **contradicts** the IT flow reading (`eqflow` rank 5, `delta` 2nd-worst) and **agrees** with the IT price reading (`exc20` best of 11) — i.e. this card sits **exactly on `C16`**, and is handed to `P105` (settles 09-09) rather than resolved. |

### Card 4 — The oil axis is oscillating, and both branches are alive in the same 48 hours

| | |
|---|---|
| **Threads (two, deliberately carded together)** | *"Iran, Oman Agree to Temporary Strait of Hormuz Deal"* · **ENDED at its peak, 9→13 outlets** — an event that resolved, not one that faded. **Against**: *"Iran threatens 45 tankers with fines, confiscation"* · **REIGNITED, 5→3.** And above both: *"US threatens toughest sanctions yet against Iran"* · **ENDED, 9→6→6→17→14→4**, peak 17. |
| **Direction (body-read)** | The 08-26 head layer carries *"The Commodities Feed: Oil falls as Strait of Hormuz talks advance"* [15 outlets] **and** *"Trump declares 'Mission Accomplished' in Iran, as conflict drags on"* [7 outlets] on the same day. **De-escalation is priced in the barrel while the enforcement channel re-ignites underneath it.** 🚫 **This card takes no side** — banking one side of an oscillating regime variable is the failure class MACRO is told to watch. |
| **Exposure** | `MPC` (held) — **OBV +0.289 매집**, `RS20` **+12.3**, `RS60` **+37.3**; `PSX` (held) — OBV **+0.151 매집**, RS20 +11.7, `RS60` **+31.8**; `VLO` (not held, on the rejection ledger `H.밸류소진`) — OBV **+0.148 매집**, RS20 +8.8, `RS60` **+34.5**. **All three refiners are accumulating with the board's strongest 60-day relative strength.** Against them: `XOM` — **OBV −0.255 분산, flow −0.621 🔴분산** — the sector's `top1` at **30.5% weight** and **a G3 flipper**, so `wflow` may not carry the sector either way. |
| **Future — branch 1** | IF the Hormuz deal holds **AND** the refiners keep OBV 매집 on settled bars → the refining bid is **margin**, not war premium, and survives de-escalation. **Track KPI**: **`P103`** (registered this run, settles **09-02**) is exactly this test on the commodity leg, roll-free by construction. |
| **Future — branch 2 (kill)** | Falsified if the refiners lose OBV 매집 **while** the tanker-threat thread keeps reigniting — that would mean the bid was the premium and the premium is not being paid. **Also killed** if `P103` settles branch B, i.e. the whole crack signal was a contract roll. |
| **Cell · hand-off** | **LATE-MONEY → valuation gate note.** `RS60` of **+31 to +37** on three names in one node is a crowded 60-day leg, and `VLO` already sits on the rejection ledger for **`H.밸류소진`** (recheck 09-04). **No name handed to BET as fresh.** ⚠ `S119` settles tonight on the Energy equity leg — **not scored here.** |

### Card 5 — The long end sells off **through** a Treasury buyback programme designed to stop it

| | |
|---|---|
| **Thread** | *"Bond Yields Rise Despite Treasury Efforts to Curb Borrowing"* · **REIGNITED** · **5→2→3 outlets** |
| **Direction (body-read)** | The 08-26 head layer carries four separate clusters on this: *"The Bond Market Is Sending an Unmistakable Message to Fed Chair Kevin Warsh and the FOMC: Act!"* [7 outlets], *"Why a chorus of market pros is criticizing the Treasury's plan to tame the bond market"* [7], *"The Bond Sell-Off Is Rattling the Stock Market"* [5], *"Why turmoil in the bond market is boosting gold and Bitcoin"* [6]. **The criticism is of the instrument, not of the fiscal path** — which is exactly `P77`'s registered claim, and `P77` has now been **unreadable for two consecutive runs** (`D333`, 10th). |
| **Exposure** | Not a stock card — **a rate card**, and the desk's rate-exposed positions are its *underweights*. `[FRED]` **`DGS30` 5.17 @08-25 = 92.0th percentile** of 365 days; `DGS10` 4.64 (92.0th); **real `DFII10` 2.32 (88.3rd) against breakeven `T10YIE` 2.32 (48.4th) ⇒ the move is entirely real.** Duration-sensitive sector reads (asof 08-27 sweep): `RE` **eqflow −0.389 rank 10**, `UTIL` **−0.552 rank 11** — the two worst on the board, both carrying `UW`/`N−`. **Crowding note**: `UST 10Y` specs are at the **5th percentile (crowded short)** while the yield sits at the 92nd — the sell-off is arriving into positioning that is already fully on that side. |
| **Future — branch 1** | IF `DGS30` publishes an 08-26 bar **at or below 5.18**, `P77`'s branch A ("the cap holds") completes and every UW justified by "the long end is repricing" is on borrowed time. **The last published value is 5.17 — 1bp inside branch A** 🚫 **and is NOT a score** (`P77`'s frozen observable is the 08-26 bar). **Horizon: the first `[FRED]` publication.** |
| **Future — branch 2 (kill)** | Falsified if `DGS30` ≥ 5.38 (`P77` branch B) or if the thread ends without a policy response, i.e. the criticism was commentary. |
| **Cell · hand-off** | **STORY-ONLY → ROTATION as duration cross-evidence** (`RE`, `UTIL`). ★ **And a book flag** — see §2. |

### Card 6 — The tape said "muted inflation" and "more likely to hike" on the **same day**

| | |
|---|---|
| **Thread** | *"Watch Muted Inflation Advance Offers Fed Breathing Room"* · **BUILDING** · **2→4 outlets** — precursor form, and BUILDING is conservative on today's 51.6% partial day |
| **Direction (body-read — a direct contradiction inside one day's tape)** | The **July core PCE printed 08-26** at **+3.3% YoY unchanged / +0.2% MoM, both in line** (`M977`, 6 outlets). The 08-26 head layer carries **both** *"Inflation index prized by Fed holds steady in July"* [14 outlets] **and** *"Fed seen a bit more likely to hike after inflation data"* [`reuters`, 5 outlets] — plus **"Australia Inflation Overshoots Estimates, Boosting Hike Bets"** [12] and **"ECB may raise rates in September as Iran war fuels inflation concerns"** [5]. **An in-line print produced a hawkish global read.** Meanwhile `DGS2` **fell 7bp into it** (4.24 → 4.17). |
| **Exposure** | Rate-path card. `[FRED]` `DGS2` **4.17 @08-25 = 86.5th percentile**, range 3.38–4.37. `HY OAS` **2.70% at the 6.9th percentile** and **`NFCI −0.566` = the loosest reading in its entire 57-observation series** ⇒ 🚫 **no "conditions are tightening" claim is admissible** and none is made. Sector legs: `STPL` **eqflow −0.329 rank 8**, `HLTH` **+0.086 rank 1** — the two defensive legs disagree with each other. |
| **Future — branch 1** | IF `DGS2` reaches **≥ 4.32** at the first `[FRED]` close dated ≥ **09-02**, the front end has believed the hawkish read. That is **`P104`**, registered this run. **Horizon 2026-09-02.** |
| **Future — branch 2 (kill)** | Falsified if `DGS2` **≤ 4.08** — the hawkish tape was noise and `P86`'s branch A completes. **Also**: `S120` (Warsh at Jackson Hole, settles 08-28) and `S111` sit on the same axis. |
| **Cell · hand-off** | **STORY-ONLY → MACRO/`P104`.** 🚫 Not a name card. |

### Card 7 — Canada / USMCA: the **investment-risk** framing is the precursor, and it outlives the tariff headline

| | |
|---|---|
| **Threads** | *"Canada: Investment risk and USMCA reliability – Societe…"* · **REIGNITED** · **2→3→5→4** — precursor form. **Against** *"Canada set to announce retaliatory tariffs against US"* · **FADING** · **11→24→20→21→29→14→7**, peak 08-25 |
| **Direction (body-read)** | The **headline** thread is fading — and **it is a real fade, not a partial-day artifact**: it halves on the **full** 08-26 day (29 → 14 outlets). **But the second-order thread is climbing**: 08-26 head layer carries *"U.S. and Canada Are Bracing for Prolonged Trade Dispute"* [**14 outlets**] and *"'We got attacked': Canadians unite in fury over Trump's latest tariff salvo"* [5]. ⇒ **attention is rotating from the announcement to the durability**, which is the leg with the dated catalyst. |
| **Exposure** | `INDU` — sweep `eqflow` **−0.244 rank 7**, **0 🟢 / 15 🔴 of 50 = the most reds on the board**; MACRO price `exc5` −0.678 with **26 of 50 negative = worst 5-day breadth**. `CAT` (top1) OBV **+0.038 중립**, `RS20` −1.8, `RS60` −10.6; `DE` OBV **+0.150 매집**, `RS20` +0.6. `STPL` — the dairy/agricultural leg of the retaliation list: **`ADM` OBV −0.154 분산, flow −0.643 🔴분산.** |
| **Future — branch 1** | IF the durability thread keeps building into the **09-08 effective date**, the tariff is a **capex/allocation** event rather than a price event, and it lands on `INDU` (standing `UW−`) and on `STPL`'s agricultural node. **Track KPI**: whether `ADM` and `DE` diverge — the two names on opposite sides of the retaliation list. **Horizon 2026-09-08.** |
| **Future — branch 2 (kill)** | Falsified if a negotiated carve-out is announced before 09-08, or if the durability thread ends without the effective date arriving. |
| **Cell · hand-off** | **STORY-ONLY → ROTATION (`INDU`, `STPL`).** 🚨 **`D342`'s gap persists for a 3rd run**: **the 09-08 effective date is bracketed only by `S123` (settles 09-12)**, and the `STPL`/agricultural leg has **no bracket at all** — **named here for PREMORTEM**, which owns mandatory bracketing. |

### Card 8 — Crypto's legislative bid, and the two names carrying the universe's highest flow scores

| | |
|---|---|
| **Thread** | *"Crypto Is Surging After President Trump Pushes Congress"* · **REIGNITED** · **5→4 outlets**; alongside *"Trump Pushes CLARITY Act as Bitcoin Surges"* [5] and *"Bitcoin rally triggers short squeeze"* (REIGNITED 4→3) in the 08-26 head layer |
| **Direction (body-read)** | The driver named in the bodies is **legislative** (the CLARITY Act), not adoption — and one body attributes the move to a **short squeeze**, i.e. a positioning mechanic. A third head cluster runs the other way: *"US bank lobby wants stablecoin holders to open an account before cashing out"* [8 outlets] — **an incumbent-friction story inside the same complex.** |
| **Exposure** | `COIN` — **the universe's #1 flow score (+0.828)**, OBV **+0.174 매집**, `RS20` +9.4, `RS60` +5.1, `delta` **−0.150**. `MSTR` — **#2 (+0.789)**, OBV **+0.458 매집** (the highest OBV in the sweep), `RS20` **+26.3**, `RS60` −7.8, `delta` **−0.150**. `HOOD` — OBV **+0.169 매집**, `RS20` **+23.3**, `RS60` **+23.5** — positive on **both** windows, the only one of the three that is. **Crowding note: `COIN` and `MSTR` are both in the head layer via the Bitcoin clusters.** |
| **Future — branch 1** | IF the legislative thread keeps building **AND** OBV 매집 survives settled bars → the bid is regulatory clarity and it is durable. **Track KPI**: whether the **bank-lobby friction** thread grows against it. **Horizon 2026-09-11.** |
| **Future — branch 2 (kill)** | **Already half-armed, from this desk's own prior work**: the 08-26 BET measured **`COIN` CY consensus +1.01 → −2.06 (−303.5%)** and **`MSTR` +43.82 → −6.69 (−115.3%)** — **the universe's two highest flow scores are the two names whose consensus was cut to a loss** (`M956`), and `MSTR` trades at a **2.52× forward P/E**, `L2`'s peak-multiple trap in its purest form. The card is **falsified now** unless a body explains the revision collapse. |
| **Cell · hand-off** | **LATE-MONEY → valuation gate note. 🚫 NOT handed to BET as CONFIRMED-EARLY.** ⚠ **This is the exact pair the 08-26 EVENT_ALPHA handed forward as CONFIRMED-EARLY and that the same run refuted two stages later.** That hand-off is **not repeated**; `MSTR` already sits on the rejection ledger (`H.밸류소진`, recheck 09-16). 🚨 **And `M956`'s cause is still unread** — the single largest `C3` gap the desk is carrying. |

---

## §2 · Book cross-check — ENDED threads under open positions

| position | the thread its thesis rides on | tag | verdict |
|---|---|---|---|
| `MPC` · `PSX` (energy-refining) | *"US threatens toughest sanctions yet against Iran"* **ENDED** (peak 17 outlets) and *"Iran, Oman Agree to Temporary Hormuz Deal"* **ENDED at peak** | 🚨 **BOTH ENDED** | **Flag raised.** The war-premium leg's attention has rotated away. ⚠ **This is NOT a drop signal**: the money axis is **🟢 accumulating** on all three refiners (OBV 매집, `RS60` +31 to +37), so per the stage rule this is *"a name whose thesis needs rewriting"*, not a DEAD cell. **The re-written thesis must rest on margin, and `P103` (09-02) is the dated test.** |
| `NVDA` (AI-compute epicenter) | the **print** thread is ENDED; the **FY2028 guide** thread is BUILDING | ⚪ mixed | No flag — the successor thread is alive (Card 3). |
| `AVGO` (AI-compute epicenter) | no live thread names `AVGO` in this window | 🚨 **no thread at all** | **Flag raised.** The board's worst-reading held name (`flow −0.715 🔴분산`, `RS60 −25.4`) has **no narrative support in a 154-thread alive set**, prints **09-02**, and its **customer has been unnamed for the life of the position** (`W4`, open). `S127` brackets the print; **`W4` is still open.** |
| `RTX` (defense-missile) | *"The big lesson one NATO military is taking away…"* / *"US Says Troops Review Will Speed Up Europe Taking on Own…"* **BUILDING 4→5** | ✅ alive | No flag. |
| `NUE` (steel) · `MET` · `NDAQ` · `ETN` · `HPE` | no named thread in the alive set | ⚪ | Not flagged as ENDED — **absence of a thread is not an ended thread**, and it is recorded as such rather than converted into a verdict. |

---

## §3 · Ledger writes made by this stage

| ledger | ticker | class | revives/enters-if | recheck |
|---|---|---|---|---|
| **reject** | `FN` Fabrinet | `K.본문반증` | re-enters `us_top300` **OR** a body names the guidance line behind the 08-24 de-rate **AND** `FN` prints a positive 5-session excess vs `SPY` | **2026-09-10** |
| **missed** | `COHR` Coherent | `Q.확신부족` | an optical/interconnect row is added to `cycle_registry.json` **OR** `COHR` prints `RS60` above zero with OBV still 매집 on a settled bar | **2026-09-10** |
| **missed** | `LITE` Lumentum | `Q.확신부족` | `S128` settles without falsifying the `rs60` reversal **AND** `LITE` still prints OBV 매집 on a settled bar | **2026-09-09** |

⚠ **All three conditions carry a market-side conjunct** — checked against **`C19`** (registered by the
sibling desk this morning: three existing rows have revival conditions whose only observable is a *desk
action*, so no market outcome can settle them). **None of these three is that class.**

---

## §4 · IDs registered by this stage

> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`, excluding this
> run's own files: **`M990` → 0 hits.** Highest before this append: `M989` (this run's SWEEP).

- **`M990`** — the precursor-first selection rule hands first pick to wire boilerplate: the board's
  largest multi-day thread by article count (**142 articles**, securities-class-action wires) is in
  perfect precursor form and has no direction to read; six of the top ten precursor candidates are of
  that class. (`D367`, reproduced with a count.)

---

## ✅ EXIT CHECK
- [x] **Scope market-correct** — `--scope foreign` on every `thread`, `brief` and `fts` call. No card
      cites a cross-market feed.
- [x] **Selection logged**: 154 alive → **8 selected**, **146 not selected**, with the five excluded
      **classes** named and counted (§0). No silent cap.
- [x] **Every card carries a direction body-read** — and one card's body-read **killed its own headline
      name** (`FN`, Card 2), which is the check working rather than passing.
- [x] **Every exposure name carries a flow tag with its asof (2026-08-27)** — and the stub-bar caveat is
      stated once at the top and applied throughout (`vol_surge` and the 🟢/🟡/🔴 tag declined).
      **STORY-ONLY names did not leak into the candidate hand-off**: **zero names were handed to BET as
      CONFIRMED-EARLY this run**, and §1 Card 8 states explicitly why the 08-26 hand-off is not repeated.
- [x] **Every card has both branches, a kill condition and a dated horizon.**
- [x] `EVENT_ALPHA.md` written; **ENDED-thread book flags emitted (§2, two raised)**; three ledger rows
      written (§3); handoff ledger update is owed at run end.
