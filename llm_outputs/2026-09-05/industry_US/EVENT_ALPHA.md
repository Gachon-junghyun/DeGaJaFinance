# EVENT_ALPHA — industry_US · 2026-09-05 (Sat) · Stage 5 / L1·EVENT_ALPHA

> Bottom-up complement to MACRO's transmission matrix: *which stories are BUILDING, and is money
> already following?* Every news call `--scope foreign` (hard rule; `all` banned inside a desk run).
> Flow tags from `SECTOR_FLOW_US.json`, **asof 2026-09-04 settled close**.
> **Analytical output only — no sizing, no buy/sell language (P4). BET owns sizing.**

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`: 4,576 events → 3,525 threads, **581 multi-day, 54 alive**.
Per-day denominators **08-30 293 · 08-31 755 · 09-01 858 · 09-02 943 · 09-03 875 · 09-04 705 ·
09-05 147**.

⚠⚠ **The window ends on a SATURDAY at 147 articles against a 705–943 weekday run.** The tool's own
warning applies: **every `FADING` tag in this run is inflated by that bar.** Selection was therefore
made on **weekday legs**, and the single biggest consequence is in Card 1.

**Selected: 8.** Precursor-form first (starts ≤2 outlets and climbing), then BUILDING/REIGNITED by
peak, then FADING **only where the book holds exposure** (Cards 1 and 6 qualify on that clause).
**Not selected: 46 of the 54 alive threads** — counted, not silently dropped. The 46 break down as:
**~30 stock-comparison / listicle content-farm threads** (*"BYD vs. Rivian"*, *"Applied Digital vs.
IREN"*, *"3 Millionaire-Maker AI Stocks"*, *"The 1 Metric I Check Before Buying Any Dividend
Stock"*), **~9 non-US-market threads** (Walmart product listings, Ig Nobels, UK subsidence, Purple
Style Labs IPO, German-language litigation), and **~7 live market threads that did not clear the
money leg** (US-Canada trade war 3→8→2, Ukraine/Russia 13→…→11, Alphabet ad-tech ruling 3→2,
TCS $7.4bn AI data centre 3→2, Tesla Cybercab→NHTSA 2→2, "Stock Market Sounds an Alarm" 5→3→4,
10y-yield-highest-since 4→4→4). ⚠ The last group is where a miss would hide; three of them are
covered by existing registered rows (`S123` trade war 09-12, `P125`/`P138` the yield thread) and are
named here rather than re-carded (`D343`).

🚫 **`vel_coverage` is 16.39% and the news axis is DEAD in the sweep (`PREFLIGHT §G1`).** No card
below cites a sweep velocity. Every narrative number here comes from a **direct** `module_news_data`
call made outside a sweep burst, which `G1` explicitly permits.

## 0b · 🚨 The exposure-discovery tool failed today, and that is a finding, not a gap

`chain-hop` was run on three themes (`"rare earth" magnet`, `diesel refinery`, `DRAM memory`).
**It returned zero valid one-hop candidates, and every top-ranked name is an artifact.** Body-read
before carding, which is what caught it:

| candidate | rank | why it is an artifact |
|---|---|---|
| **`LIN`** (Industrial Gases) on rare earth | 5 proximity / 8 body | 🚨 **`LIN` is Lindian Resources' ASX ticker**, in a PR Newswire release *"STRATEGIC PARTNERSHIP WITH CARESTER FOR OXIDE SEPARATION"* — **not Linde plc.** Verified: `fts search Carester` returns *"Lindian Resources locks in Carester partnership and long-term rare earths offtake"* |
| `GD`, `NOC` on rare earth | 2/4, 2/3 | both from *"Boeing vs. Lockheed Martin: Which Aerospace Stock Is a Better Buy in 2026?"* — a stock-comparison listicle, not a supply-chain link |
| **`GOOGL` 16/95 · `GOOG` 16/95 · `META` 10/76 · `AMZN` 4/26** on **diesel** | ranks 1–4 | 🚨 **`D10` reproducing, and this is the first time this desk has quantified its effect on `chain-hop`**: three ad-platform names are the top body co-mentions on a *diesel* query. That is page boilerplate (sign-in widgets, ad scripts, share buttons) counted as body text |
| `MMM` 7/28 on DRAM | rank 1 | from *"Is the Memory Supercycle Peak Near for Micron and SK Hynix?"* — boilerplate again |

★ **`M1296` [measured] — `chain-hop`'s ticker matching produces issuer false positives on
three-letter tickers, and `LIN` is the third instance in two runs** (`AME` 6,159 hits and `HES`
6,364 were recorded on 09-04). ⇒ registered as **`D509`**: *a `chain-hop` candidate is not a
candidate until one of its example articles has been opened and the ticker confirmed to mean the
issuer.* The only survivor of a manual read is **`FDX`** (3 proximity / 4 body) on
*"US diesel prices hit a record high, pushing up transportation costs for a long list of goods"* —
a genuine linkage, and it is a **cost headwind**, not a beneficiary (Card 2 carries it as such).

⇒ **Exposure maps in the cards below were built from GICS industry + the flow object, with
`chain-hop` used only as a falsified input.** Stated so no card looks better-sourced than it is.

---

# ★ FORWARD CARDS

## Card 1 — 🟢 **CONFIRMED-EARLY** · The distillate crack is the Energy trade, and three instruments say the story has left it

**Thread.** *"The Commodities Feed: Oil maintains gains amid Persian Gulf escalation"* —
printed **`FADING` 19→22→22→19→13→21→4**, denominator 530 articles over 7 days.
🚨 **Read on weekday legs the tag is wrong: the curve RISES 13 → 21 into 09-04**, and the "4" is
Saturday's 147-article bar. Sub-thread *"Asian Refiners Turn to Argentina as Iran War Disrupts Oil"*
`REIGNITED` 8→3 is the **chain** leg running separately from the barrel leg.

**Direction (body-read, not headline).** The event is a **refined-product** supply shock, not a
barrel shock, and the wires name the mechanism: *"Diesel Cracks Hit Record Highs as Global Fuel
Squeeze Deepens"* [oilprice 09-02], *"US Diesel Crack Near $100 As US-Iran Strikes Resume"*
[zerohedge 08-31], *"Diesel hits record high as Ukraine and Iran wars knock out refineries"*,
*"Why Oil Majors Don't Want to Build New U.S. Refineries"* [09-03], *"Global Refining Crunch Could
Keep Fuel Prices High Into 2027 — 'Refining capacity will not come back'"* [09-03]. ⇒ **capacity
destruction with a structurally blocked supply response.**

**★ Two news numbers corrected against the primary source (futures, `auto_adjust=False`):**

| claim in the wires | measured, 2026-09-04 settle |
|---|---|
| *"Crude at **$96**"* [10-outlet cluster] | **WTI `CL=F` = 91.48.** The $96 is a Brent print; **WTI is the citable US barrel** (`D5`/`C1`) |
| *"Diesel cracks hit **record** highs"* [09-02] | **Distillate crack 99.21 = the 95.6th percentile.** Its 2-year max **106.23 was set 2026-09-01** — the record is **three sessions old and 7.0 points below today**. ⇒ **"at a record" is stale by 09-04 and this card does not write it** |

**And the decomposition is the finding.** 5-session changes into 09-04: **WTI +8.08** ·
**distillate crack −0.37** (holding at the 95.6th pctile) · **gasoline crack −19.64** (63.18 → 43.53)
· **3-2-1 crack −13.22**. ⇒ **`M1297` [measured] — the barrel rose and the refiner's blended margin
FELL, because gasoline collapsed while distillate held.** The **distillate−gasoline spread is
55.68 = the 98.4th percentile of the trailing year.**
⚠ **This reverses `P83`, which FIRED-B on 08-27 because that same spread had collapsed −13.562.**
Eight sessions later it is at a 98th percentile. Recorded as a fact about the observable's
volatility, **not** as a re-score (`D242`).

**Exposure** (flow tags asof **2026-09-04**; ⚠ `[FINRA]` z from the same date):

| name | chain position | flow | OBV | rs20 / rs60 | crowding note |
|---|---|---|---|---|---|
| **`MPC`** (held) | Gulf-Coast refiner, high distillate yield | +0.694 🟡 | **+0.621 매집** — the strongest OBV in the whole chain | **+30.8 / +41.5** | 🟡 z +0.43. ⚠ **above consensus mean target** (`L2` peak-margin lens) |
| **`PSX`** (held) | refiner + midstream | +0.750 🟡 | **+0.434 매집** | +25.5 / +34.2 | 🟡 z −0.36 |
| `VLO` (not held) | pure refiner | +0.700 🟡 | **+0.482 매집** | +24.7 / +37.5 | ⚠ **standing rejection** 08-21 `H.밸류소진`, reaffirmed 09-04. Filed to the miss ledger this run |
| `SLB` | oilfield services — **headline layer** (shortlist 🟢) | +0.883 🟢 | +0.439 매집 | +14.2 / **−2.6** | ✅ short-cover z −1.21. 60-day RS is **negative** — the 🟢 is 20-day |
| `XOM` | integrated, the sector's `top1` | **+0.027 🟡** | **−0.071 중립** | +4.6 / −0.3 | ⚠ **the sector's largest name is its weakest**; ex-top1 `wflow` +0.621 vs +0.440 |

🚨 **`M1298` [measured] — the shortlist's Energy names are NOT the sector's strongest names, and the
gate that decides it is the one under an open contradiction.** `MPC`/`PSX`/`VLO` carry OBV
**+0.43 to +0.62 매집** with rs20 **+24.7 to +30.8** and are tagged **🟡**, while `SLB`/`WMB`/`CVX`
are tagged **🟢** on OBV +0.15 to +0.44 and rs20 +5.7 to +14.2. The separator is **`vol_surge`**:
the refiners print **1.05–1.15**, just under the gate's **1.2**. ⇒ **this is `M25`'s ENRG-shortlist
artifact measured live**, and the axis doing the separating is the one `C29` (opened this run) has
scoring **IC −0.0414, t(NW) −3.61 on the KR ledger, significantly NEGATIVE.** `W1` bars importing
that conclusion — but it means **no stage may read the refiners' 🟡 as weakness.**

**Future — both branches.**
- **IF** the thread keeps building (weekday outlet count ≥ 18) **AND** flow stays accumulating →
  the distillate leg is a capacity event with no supply response, and Energy's `exc20 +12.29` is
  early rather than late. **Track KPI: `refining margin` theme-age turns above 1.0×** (it has read
  **0.66× for three consecutive runs**) and the distillate−gasoline spread holds ≥ its 85th pctile.
  **Horizon: 2026-09-14** (`P136`'s settle).
- **ELSE / kill condition** — any ONE of: (i) the **distillate−gasoline spread falls below its 50th
  percentile**; (ii) **`MPC` or `PSX` OBV state leaves 매집**; (iii) 🚨 **a US policy action against
  refiner margins** — the live one, named in the body-read: *"U.S. diesel price soars to more than
  four-year high **as Trump ramps up pressure on refiners**"* [seekingalpha 09-01]. This is the
  card's most under-priced risk and it is **not** in `P136`'s VOID clause, which names OPEC+/SPR/
  Hormuz. Stated here so it is on the record before it is needed.

**Cell + hand-off.** **CONFIRMED-EARLY** — the only card this run in that cell.
→ **ROTATION**: Energy is the one label where five instruments agree (SWEEP_READ §4).
→ **BET §B**: `MPC`, `PSX` as **already-held** names whose thesis is *re-specified* from "the barrel"
to "the distillate crack"; `VLO` is **not** handed forward (standing rejection, `D463`).
⚠ `W3`: this says a spread persists. It does not say a position was right, and it sizes nothing.

---

## Card 2 — 🟡 **STORY-ONLY** · The diesel print is a cost shock, and the only clean chain-hop link is a VICTIM

**Thread.** *"US diesel prices hit an all-time high"* — **head cluster, 10 outlets**, plus
*"US fuel production rose in August"* [7]. **No multi-day thread yet** — stated explicitly; it is a
one-day cluster the `brief` layer carries, which is precursor form.

**Direction (body-read).** *"...pushing up transportation costs for a long list of goods"*;
*"Diesel price surges to all-time high, fueled by wars"*; *"US Retail Diesel Hits Record as Hormuz,
Russia Crises Stretch On"* [bloomberg]. ⇒ the **downstream** reading is an **input-cost shock to
freight and to goods inflation**, which is the opposite sign from Card 1's producer reading.

**Exposure** (the only `chain-hop` survivor of a manual read):

| name | chain position | flow | OBV | rs20 / rs60 | note |
|---|---|---|---|---|---|
| **`FDX`** | air freight — **fuel is a pass-through with a lag** | −0.183 🟡 | **−0.270 분산** | +1.6 / −5.1 | the one valid chain-hop hit (3 prox / 4 body) and it is a **victim**, not a beneficiary |
| `UPS` | same node | −0.251 🟡 | −0.041 중립 | −1.7 / −7.1 | Δ **−0.251**, one of the board's larger single-session declines |
| `ODFL` | LTL trucking | **−0.343 🔴분산** | −0.130 분산 | **−13.7 / −27.4** | worst RS in the node; surge 1.47 |
| `NSC` · `UNP` · `CSX` | rail — diesel is a **surcharge pass-through**, historically | +0.068 / −0.031 / +0.003 🟡 | all 중립 | ≈ 0 / ≈ 0 | ⚠ `NSC` Δ **+0.403** and `UNP` Δ **+0.236**, two of the board's top Δs — **the rails are moving and the truckers are not** |

★ **The rail/truck divergence is the card's only real content, and it has a carried caveat.**
`R38` retracted the desk's *"~8 of UNP's 12 revenue growth points are fuel surcharge"* claim in
August — the **mechanism survived, the magnitude did not**. ⇒ **this card may state the divergence
and may NOT state that fuel surcharge explains it** (`W1` on our own retraction).

**Future — both branches.**
- **IF** the diesel print builds into a multi-day thread **AND** rail Δflow stays positive while
  truck/parcel Δflow stays negative → the pass-through asymmetry is real and it is a **within-
  Industrials** dispersion trade, not a sector call. **Track KPI: `diesel` theme-age above 1.2×**
  (today **1.02×** on a base of 2,003). **Horizon: 2026-09-19.**
- **ELSE / kill condition:** rail Δflow turns negative, **or** `diesel` theme-age stays ≤ 1.05×
  through 09-19 — i.e. an all-time-high print that never generated a story is a price event with no
  transmission, and this card is then a false start.

**Cell + hand-off.** **STORY-ONLY** — money is **dispersing** on every named victim and only
*Δ*-positive (not level-positive) on the beneficiaries. → **watchlist with a dated re-check
2026-09-19.** **Not handed to BET.** No name from this card enters the candidate hand-off.

---

## Card 3 — 🔴 **DEAD (money verdict) → RE-FILED** · Chinese rare-earth shipment halt: a real supply shock the desk cannot touch

**Thread.** *"Pentagon rare earth push collides with China's grip"* [8] — printed `FADING` 3→8→2 —
**plus a NEW 09-04 item that has not joined the curve**: *"China rare earth firms halt some US
shipments over geopolitical worries, sources say"* [Reuters, **6 outlets**] and
*"Chinese Rare-Earth Suppliers Halt US Shipments As Decoupling Fears Surge"* [zerohedge].

**Direction (body-read).** Unambiguous supply shock: *"Chinese rare earth suppliers are quietly
refusing U.S. shipments."* ⚠ **And the tape already said what it thinks**:
*"USA Rare Earth Rises 4%, **Then Coughs Up Gains** as Chinese Suppliers Refuse U.S. Shipments"* —
the headline beneficiary gave back the move inside the session.

**Exposure — there is none, and that IS the card.**
- **No rare-earth or critical-minerals pure play is in `us_top300`.** `MP` returns
  *"not in universe"*. The desk **cannot tag what it cannot see** (`SWEEP` invariant).
- **`chain-hop` returned only artifacts** (§0b): `LIN` = Lindian Resources' ASX ticker, `GD`/`NOC`
  from a stock-comparison listicle.
- The one us_top300 name with any real linkage, `LIN` (Linde plc, Industrial Gases), is
  **+0.045 🟡 · OBV +0.101 매집 · rs20 −2.1 · rs60 −12.4** — and its inclusion here rests on an
  artifact, so **it is named as excluded, not as exposure.**

★ **`M1299` [measured] — this is the 2026-08-26 "no gold vehicle" finding reproducing on a second
theme.** That run recorded *"the desk has NO gold vehicle tagged in this thread even though `NEM` is
`exc5 +16.72 / exc20 +44.28`."* Today the same structure appears in critical minerals, with the
additional feature that **`rare earth` theme-age reads 0.88× — DECELERATING — on the day of the
shipment halt**, the same physical-extreme-with-flat-narrative shape as Cards 1 and 2.

**Future — both branches.**
- **IF** a us_top300 vehicle appears (universe rebuild) **AND** the thread rebuilds above 8 outlets →
  the card becomes real. **Track KPI: `rare earth` theme-age > 1.2×.** **Horizon: 2026-09-19.**
- **ELSE / kill condition:** `rare earth` stays ≤ 1.0× through 09-19 with no vehicle — the theme is
  then permanently outside this desk's instrument and should be said so rather than re-discovered.

**Cell + hand-off.** ⚠ **Formally the 2×2's DEAD cell requires FADING **and** 🔴 dispersing on the
money axis. There is no money axis here at all** — a third state the 2×2 does not have. Per the
stage's own rule (*"DEAD is a MONEY verdict"*), this is **re-filed, not dropped**:
→ **`reject_ledger` row filed** — `MP`, class **`L.vehicle없음`**, `--revives-if` *"a rare-earth or
critical-minerals name enters `us_top300` via `build_us_universe`, OR `chain-hop` returns a
us_top300 candidate whose body linkage survives a manual read"*, `--recheck-date 2026-09-19`.

---

## Card 4 — 🟡 **STORY-ONLY** · `NVDA` / Hugging Face: the narrative is alive, the money is not — and the inherited label was wrong

**Thread.** *"Nvidia to Acquire Hugging Face for $12.9 Billion"* — tagged `ENDED`, curve
**4→28→9 with a peak of 28 outlets** (09-02→09-04), and the 09-04 head still carries
*"Nvidia's $13 Billion Hugging Face Deal Expands Open-Source AI"* at **9 outlets**.
`theme-age "Hugging Face"` = **🟡ACCELERATING · 3.11× · base 1,022 · age 74**.

🚨 **`R129` — the inherited label is retracted.** The 2026-09-04 HANDOVER carried `S130`
(settles **09-10**) annotated **"dead thread"**. A 28-outlet peak with a 3.11× theme acceleration is
not a dead thread. **What survives**: the `ENDED` *tag* is a curve shape, not an importance
judgement — the tool says so itself. **What is withdrawn**: this desk's reading of that tag.
⇒ **`S130` is a LIVE row settling in five days.** (Generalised as **`D508`** in `MACRO §D-5`: a
`thread` tag and a `theme-age` reading can contradict, and the numeric instrument wins.)

**Direction (body-read) — and it splits.** Confirmed transaction: *"Nvidia confirms it will buy
Hugging Face for $12.9 billion"* [techcrunch 09-03]; *"leaving it as an open source platform"*
[09-03]. **Counter-leg, and it is regulatory**: *"Hugging Face is too important to fall into
Nvidia's hands"* [The Register 09-04]. **Adjacent, same window**: *"Nvidia has built a $99 billion
equity portfolio from almost scratch in 2 years"* [6 outlets] — the same balance-sheet story from a
second angle.

**Exposure.**

| name | chain position | flow | OBV | rs20 / rs60 | crowding note |
|---|---|---|---|---|---|
| **`NVDA`** (held) | acquirer — **headline layer** | **−0.032 🟡** | **−0.084 분산** | +3.3 / +8.8 | 🟡 z **−0.51**, surge 1.01. **The money leg is absent** |
| `MSFT` | open-model hosting rival | +0.065 🟡 | +0.132 매집 | +0.3 / +19.6 | surge 0.60 |
| `META` | the incumbent open-weights sponsor — **the name with the most to lose** | +0.469 🟡 | **+0.302 매집** | +4.6 / +1.8 | one hop past the headline; ⚠ it is 09-04's `exc1` −1.09 sector |
| `ORCL` | model-hosting cloud | +0.511 🟡 | +0.211 매집 | +8.4 / **−27.3** | rs60 is the worst in the group |

★ **The narrative and the money point opposite ways on the headline name.** `NVDA` is the single
most-written-about company in the blind-spot token count (**421 mentions in 3 days**) and its OBV is
**dispersing**. That is the textbook STORY-ONLY signature.

**Future — both branches.**
- **IF** the thread stays BUILDING/REIGNITED **AND** `NVDA` OBV turns 매집 → the deal is being
  accumulated and the card is upgraded. **Track KPI: `NVDA` `obv_state`.** **Horizon: `S130`'s
  settle, 2026-09-10.**
- **ELSE / kill condition:** `NVDA` OBV stays 분산 through the 09-10 settle, **or** a regulatory
  review is opened on the transaction — in which case the thread is a *risk* story, not an
  exposure story, and the card inverts rather than dying.

**Cell + hand-off.** **STORY-ONLY.** → watchlist, dated re-check **2026-09-10** (= `S130`).
→ **`reject_ledger` row filed** on the **thread as an entry reason** — `NVDA`, class
**`A.flow미도착`**, `--revives-if` *"`NVDA` obv_state turns 매집 while the thread is still
BUILDING/REIGNITED, OR `S130` fires its accumulation branch"*, `--recheck-date 2026-09-10`.
⚠ **This rejects the thread as a REASON TO ADD. It says nothing about the held position** (P4).

---

## Card 5 — 🟢 **CONFIRMED-EARLY (instrument-conditional)** · Storage and memory carry the board's largest Δ and are invisible to the 🟢 gate

**Thread.** Two threads, pointing opposite ways, which is why this card exists.
`REIGNITED` *"China Is Grabbing Memory Market Share. This Stock Could Be a Big Loser"* → *"China's
Biggest Memory Chip Stock Is Almost as Good as M[icron]"*, **2→3 outlets**; and the 09-04 cluster
*"Micron, SanDisk Jump 4% Even as Hot Jobs Report Briefly Flips Fed Hike Odds Above 50%"* —
**recovered from the `single_source` random sample, at ONE outlet** (`MACRO §B-1`).

**Direction (body-read) — the narrative leg is BEARISH.** *"China Is Grabbing Memory Market Share.
This Stock Could Be a Big Loser"* [09-03]; *"Is the Memory Supercycle Peak Near for Micron and SK
Hynix?"*; *"Memory Stocks Are the New Stars of FOMO Investing. Why I'm Waving a Yellow Flag Here."*;
*"Billionaire Stanley Druckenmiller Kicked Micron to the Curb."* ⚠ Offsetting, same window:
*"SK Hynix's $720B AI Memory Expansion"*, *"SK hynix Looks to Build a New Plant in Japan"*.
⇒ **the story is a share-loss / peak-cycle story; the tape is doing the opposite.**

**Exposure — and the numbers are the card.**

| name | chain position | flow | **Δflow** | OBV | rs20 / rs60 | **`vol_surge`** |
|---|---|---|---:|---|---|---:|
| **`STX`** | HDD / nearline storage | +0.047 🟡 | **+0.728 — #1 on the board** | +0.034 중립 | +4.9 / −2.1 | **0.59** |
| **`WDC`** | HDD / NAND | +0.068 🟡 | **+0.718 — #2** | −0.042 중립 | +8.0 / −10.8 | **0.68** |
| **`AMD`** | compute | −0.245 🟡 | **+0.566 — #3** | +0.005 중립 | −0.8 / −0.6 | **0.60** |
| **`SNDK`** | NAND | +0.633 🟡 | +0.061 | **+0.351 매집** | **+43.9** / −0.3 | 0.94 |
| **`MU`** | DRAM/HBM | +0.478 🟡 | +0.231 | **+0.194 매집** | +16.2 / +7.8 | **0.66** |
| `DELL` | server OEM — **headline layer**, the shortlist's #1 | **+1.000 🟢** | 0.000 | +0.252 매집 | +15.9 / +35.6 | **2.48** |

🚨 **`M1300` [measured] — the board's three largest Δflows are all in storage/memory, and NOT ONE of
them is tagged 🟢, because every one prints `vol_surge` below 0.70.** The gate needs ≥ 1.2 alongside
OBV and RS (`M25`). Meanwhile the sole 🟢 in the node, `DELL`, prints **surge 2.48** — it passed on
the volume axis, not on the flow axis (its Δ is exactly **0.000**).
⇒ **`C29` is live and load-bearing here**: the axis separating these names is the one the KR
`ic_ledger` scores at **IC −0.0414, t(NW) −3.61, n_eff 45**, clearing Bonferroni for a third run
with a **negative** sign, while `sector_flow`'s gate weights it **positively**. `W1` bars importing
that verdict to the US board and the US desk has no ledger of its own (`D395`/`D428`).
⇒ **This card is CONFIRMED-EARLY on the OBV+RS+Δ axes and would be invisible to any stage reading
only the tag.** It is labelled *instrument-conditional* for exactly that reason.

★ And it **reconciles `P101`** (settled `FIRED-C` today): the hardware leg beat software **+2.05% vs
−4.46%** over five sessions, and the winners were **`SNDK` +17.17 · `DELL` +14.88 · `MU` +8.98 ·
`INTC` +7.07 · `NVDA` +5.89** — **memory and storage, not semicap.** Semicap is separately and
clearly weak: `AMAT` **🔴 −0.817**, `KLAC` **🔴 −0.645**, `TER` −0.592, `ASML` −0.455.
⇒ **"IT's weak half is semicap" and "the hardware leg won" are BOTH true, on different nodes**
(`W5`), and the carried `M1251` framing is dated rather than wrong.

**Future — both branches.**
- **IF** the storage Δ persists **AND** `MU`/`SNDK` hold OBV 매집 **alongside rs20 > 0 and a positive Δflow** (`RULE D6` — OBV is a C-grade signal at r≈0.49 with no lead, so it never carries a branch alone; the US desk has no investor-type feed to pair it with, so RS and Δflow are the pairing) → the payroll-session semi rip
  (`SMH` +3.00pp excess) was a node event with real accumulation behind it, and the bearish
  share-loss narrative is the fade. **Track KPI: `STX`/`WDC` OBV turns 매집 from 중립** (today both
  are neutral — the Δ moved before the OBV did). **Horizon: 2026-09-11** (`P137`'s settle).
- **ELSE / kill condition:** `MU` **or** `SNDK` OBV leaves 매집, **or** `P137` fires branch **B**
  (`SMH` 4-session excess ≤ −2.886), which would say the 09-04 short-volume spike (z **+2.99**) was
  distribution and this card read a squeeze as accumulation.

**Cell + hand-off.** **CONFIRMED-EARLY, instrument-conditional.**
→ **ROTATION**: IT's `exc1 +1.52` is this node, not the sector (SWEEP_READ §4).
→ **BET §B**: handed forward as a **node**, not as names — no name here is 🟢 and BET must be told
why (`C29`). ⚠ **`SNDK` filed to the miss ledger** this run (`Q.확신부족`) because the direction
body-read is bearish and this stage does not card a name on the money leg alone.

---

## Card 6 — 🟡 **STORY-ONLY → BOOK FLAG** · The AI-power lane is accumulating and the book's only holding in it is dispersing

**Thread.** *"AI Power Demand Is Exploding, But How Much Actually Gets Built?"* → *"How
mechanization and AI have transformed the workforce"* → *"Widespread AI Outage Hitting OpenAI,
Claude And Others"*, printed `FADING` **7→11→18→21→19→13→5**, 373 articles. **On weekday legs this
one IS decelerating** (21 → 13), unlike Card 1. Adjacent, still `REIGNITED`: *"Gas Turbine Prices
Are on Track to Nearly Triple"* 5→3→8 and *"Bloom Energy's Backlog Will Top $50 Billion"*.
`gas turbine` theme-age **⚪ECHO 1.40×**, base 493. `data center` **⚪ECHO 0.98×**, base 19,718.

**Direction (body-read).** The build-out is real but the thread's own lede is the **bottleneck**
question — *"how much actually gets built"* — and the 09-04 head carries the physical-siting
counter-leg: *"Civil rights groups urge a halt to South Africa data centers boom amid water and
power fears"* [AP], *"How to Build Data Centers People Won't Hate"* [5]. ⇒ **the constraint story is
where the attention is, not the demand story.** That is consistent with the desk's carried
`M1257`/`M1258` (Utilities' binding constraint is regulatory, not industrial).

**Exposure — and 🚨 the book is on the wrong side of it.**

| name | chain position | flow | **Δflow** | OBV | rs20 / rs60 | note |
|---|---|---|---:|---|---|---|
| 🚨 **`ETN`** (**HELD**) | electrical components | **−0.662 🔴분산** | +0.012 | **−0.115 분산** | **−8.0** / +3.3 | **the book's only AI-power name, and the lane's only 🔴.** ⚠ **`[FINRA]` z +2.16** on a session it rose **+3.46%** |
| `VRT` | electrical / thermal for DC | +0.129 🟡 | **+0.444** | **+0.082 매집** | +3.4 / −6.3 | 5th-largest Δ on the board |
| `VST` | merchant power | +0.619 🟡 | **+0.491** | **+0.207 매집** | +6.6 / +1.6 | 4th-largest Δ. ⚠ **standing rejection** 08-14, reaffirmed 09-04 on an OBV cut missed by **0.003** (`C5`) |
| `CEG` | nuclear merchant power | +0.644 🟡 | +0.050 | **+0.188 매집** | +11.2 / +17.2 | best rs60 in the lane |
| `GEV` | heavy electrical / turbines | −0.186 🟡 | +0.245 | +0.022 중립 | −4.5 / +2.5 | the gas-turbine thread's direct name |
| `PWR` | grid construction | −0.506 🟡 | +0.024 | −0.050 중립 | −6.7 / −10.2 | weakest in the lane |

🚨 **`M1301` [measured] — of six AI-power names, four are accumulating (`VRT`, `VST`, `CEG` OBV
매집; `GEV` Δ +0.245) and the ONE the book owns is the only 🔴분산 in the group**, with the lane's
worst rs20 (**−8.0**). ⇒ **book flag emitted** (below).
⚠ **And the lane spans three GICS labels** — `ETN`/`VRT` in Industrials, `VST`/`CEG` in Utilities,
`GEV` in Industrials — so **no sector verdict can express it.** `D416` (the AI-power cycle has no
registry row) reproduces, and `P123` settles the *"did the AI marginal dollar move to power"*
question on **09-08**.

**Future — both branches.**
- **IF** the constraint story keeps the attention **AND** `VST`/`CEG`/`VRT` hold OBV 매집 → the
  marginal dollar is in **generation and thermal**, not in components, and `ETN`'s label is the
  wrong exposure to the right cycle. **Track KPI: `gas turbine` theme-age > 1.6×** (today 1.40×).
  **Horizon: 2026-09-08** (`P123`).
- **ELSE / kill condition:** `VST` **and** `CEG` both leave OBV 매집, **or** `ETN` returns to
  OBV 매집 with rs20 > 0 — either would say the lane is one object again and the split was noise.

**Cell + hand-off.** **STORY-ONLY** on the thread (decelerating on weekdays) but the **money leg is
unambiguous**, so it does **not** go to the DEAD cell — the stage's own rule. → watchlist, dated
re-check **2026-09-08**. → **`VST` filed to the miss ledger** (`S.테마회피`) because this stage does
not overturn a standing rejection. → **ROTATION**: read Utilities' `eqflow +0.050 / 0 greens` against
this — the flow is in two names, not the bucket.

**📌 BOOK FLAG (the stage's mandatory book cross-check).**
> **`ETN` is held. The thread its thesis rides on is decelerating on weekday legs (21 → 13), and
> `ETN` is the only 🔴분산 name in its own lane while four peers accumulate.** Attention rotated and
> the flow rotated with it. **The position must re-justify on something still alive** — passed to
> the book desk and to `SECTOR_DEEP` / BET, **with no sizing implication attached here** (P4).

---

## Card 7 — 🟡 **STORY-ONLY** · The yen is the axis the term table did not carry, and the tape moved before the desk noticed

**Thread.** **No multi-day thread** — stated explicitly. This card is built from the 09-04 head
(*"Japan warns against weak yen, stands ready to intervene"* [5]; *"Japan's Katayama says will
closely monitor bond markets with heightened urgency"* [7]; *"Yen's changing fortunes might finally
be spooking the..."* 4→2) plus the **blind-spot pass**, where **`Yen` (257) is the top token-0 term
outside the fixed set**, and a **direct measurement: `yen` = 857 hits (7d, phrase, foreign)** —
larger than `Treasury yield` (778) or `payrolls` (613) (`M1293`).

**Direction (body-read) — and it contradicts the headline frame.** The wires are a **weak-yen**
story: *"USD/JPY repeatedly breaks above 160 despite record FX interventions"* [Commerzbank via
fxstreet 09-03], *"Intervention ceiling guides BoJ path"* [BNY], *"Yen Suddenly Spikes Sparking
Intervention Chatter"* [zerohedge 09-02].
🚨 **`M1302` [measured] — the tape says the opposite: `JPY=X` = 156.22 at the 34.1st percentile of
the trailing year, DOWN 1.95% over five sessions (the yen STRENGTHENING), against a 1-year high of
163.86.** The *"above 160"* figure is a past or forward reference, not the current level.
⇒ **A yen rally is the carry-unwind mechanism itself.** The narrative is describing the risk; the
tape is already expressing it.
⚠ **`DX-Y.NYB` 99.16** (53.6th pctile, **−0.54%** over 5 sessions) — dollar softening, consistent.
This is a `D5` cross-provider fill: **`DTWEXBGS` is 7 days stale** at 08-28.

**Exposure — deliberately none at the name level.** A carry/term-premium channel expresses itself in
**US duration and in rate-sensitive sectors**, both of which are already bracketed (`S135` UTIL/RE/
STPL 09-11; `P128` credit 09-08). Naming equity tickers here would be inventing a transmission the
body-read does not support. ⚠ **An undated binary is named rather than guessed**: Commerzbank's
*"BoJ meeting to decide JPY path"* implies a scheduled BoJ meeting whose **date this desk does not
have**. Per the schedule L2's rule, it is written as **`[blank]`**, not estimated.

**Future — both branches.** *(the observable is `P138`, registered at MACRO §D this run)*
- **IF** the carry-unwind channel reaches US duration → the **30y−5y curve STEEPENS**:
  `P138` branch **A**, ≥ **+4.40 bp** over four sessions from the 09-04 close.
- **ELSE / kill condition:** the curve keeps **bear-flattening** from its **2.0th-percentile** level
  (`P138` branch **B**, ≤ −5.97 bp) — in which case the Fed path owns the curve, the yen story has
  no US transmission, and **`yen` should be removed from the term table as fast as it entered.**
  **Horizon: 2026-09-11.**

**Cell + hand-off.** **STORY-ONLY** (no money leg identified at the name level, by construction).
→ watchlist, dated re-check **2026-09-11**. → **MACRO** already converted it into `P138`.
→ **No name enters the candidate hand-off from this card.**

---

## Card 8 — 🟡 **STORY-ONLY** · Anthropic IPO mid-October — the only clean precursor-form thread on the board

**Thread.** *"Exclusive-Anthropic IPO launch shifts toward mid-October"* → *"Anthropic IPO launch
shifts toward mid-October, sources"* — **`BUILDING`, 2 → 6 outlets in one day, 9 articles.**
★ This is the **precursor shape the selection rule prioritises** (starts ≤2 outlets and climbs), and
it is the **only one of the three BUILDING threads that is a market event** — the other two are
stock-comparison content farms (§0).

**Direction (body-read).** A **timing** disclosure on a private-company listing, sourced
("Exclusive", "sources"). ⚠ **It is not a valuation, a size, or a confirmation** — and this desk has
a standing retraction (`R128`-KR, 09-05) against promoting a one-day vocabulary spike into a regime
claim. **The card is registered at that weight and no higher.**

**Exposure — the honest answer is a structural one, and the desk has an instrument for it.**
- **No `us_top300` name is a clean Anthropic vehicle.** The chain is private (Anthropic) or
  diluted-across-a-mega-cap.
- **The adjacent, dated, structural item is in the same window and IS tradeable-adjacent**:
  *"All Eyes Are on SpaceX's Next Share Unlock on Sept. 9"* [6-outlet cluster, 09-04] — a
  **known-in-advance lockup date**, the exact `D13`-STRUCTURAL class the news calendar routinely
  misses and which `catalyst_calendar` does **not** carry (its `[STRUCTURAL]` block reads
  *"none in window — `data/catalysts/structural_schedule.json` 을 사람이 갱신한다"*).
- Index-structural, same window, also uncarried: **`Bloom Energy`, `Illumina`, `Everpure` rise on
  S&P 500 inclusion** [5 outlets] — an index-rebalance flow event.

★ **`M1303` [measured] — three dated structural events (SpaceX unlock 09-09, an S&P inclusion
already executed, an IPO window in mid-October) appeared in one day's foreign feed, and the desk's
structural calendar is EMPTY.** ⇒ registered as **`D510`**: *`structural_schedule.json` is
human-maintained and has been empty for every run this desk has logged, while the news feed carries
dated structural catalysts weekly — the feed should seed it.*

**Future — both branches.**
- **IF** the thread keeps building above 6 outlets **AND** a listing venue/size is disclosed → it
  becomes a dated structural catalyst for the AI-compute complex's private-market comparables.
  **Track KPI: outlet count and the presence of a disclosed size.** **Horizon: 2026-09-19.**
- **ELSE / kill condition:** the thread does not exceed 6 outlets by 09-19, **or** the mid-October
  window slips again — a twice-slipped IPO date is a non-event and the card dies.

**Cell + hand-off.** **STORY-ONLY.** → watchlist, dated re-check **2026-09-19**.
→ **No name enters the candidate hand-off.** → **`D510`** handed to the dig list.

---

## 9 · Hand-off summary

| cell | cards | handed to |
|---|---|---|
| 🟢 **CONFIRMED-EARLY** | **Card 1** (distillate crack: `MPC`, `PSX` — **held**, thesis re-specified) · **Card 5** (storage/memory **node**, instrument-conditional) | **ROTATION** as sector-level cross-evidence · **BET §B** as candidates. ⚠ BET is told explicitly that Card 5's names are **not** 🟢-tagged and why (`C29`) |
| 🟡 **STORY-ONLY** | Cards 2, 4, 6, 7, 8 | watchlist with dated re-checks: **09-08** (Card 6, `P123`) · **09-10** (Card 4, `S130`) · **09-11** (Card 7, `P138`) · **09-19** (Cards 2, 8) |
| 🔴 **DEAD → re-filed** | Card 3 | `reject_ledger` `L.vehicle없음`, recheck 09-19 |

**Ledger writes this stage: 5.**
`reject_ledger` ×2 — `MP` (`L.vehicle없음`, 09-19) · `NVDA`-thread (`A.flow미도착`, **09-10**).
`missed_ledger` ×3 — `VLO` (`M.숏리스트탈락`, 09-19) · `SNDK` (`Q.확신부족`, 09-19) ·
`VST` (`S.테마회피`, 09-19). **All five carry both required fields; all `--sample prospective`.**

**📌 Book flag emitted: `ETN`** (Card 6) — held, thread decelerating on weekday legs, and the only
🔴분산 name in a lane where four peers accumulate.

---

## ✅ EXIT CHECK — EVENT_ALPHA

- [x] **Scope market-correct** — `--scope foreign` on every call (`brief`, `thread`, all `fts search`,
      `theme-age`, `blindspot`, `chain-hop`). No card cites a cross-market feed.
- [x] **Selection logged** — 54 alive threads → **8 selected**, **46 not selected and broken down by
      reason** (§0). No silent cap.
- [x] **Direction body-read on every card.** Three cards' body-reads **contradicted their headline
      layer** and the cards carry the contradiction: Card 1 (the `FADING` tag is a weekend artifact;
      the curve rises 13→21), Card 5 (the thread is bearish while the tape accumulates), Card 7 (the
      wires say weak yen; `JPY=X` is **−1.95% in five sessions**, i.e. the yen is strengthening).
      ★ **Two news numbers were corrected against primary sources** (WTI 91.48 not "$96"; the
      distillate-crack record was set **09-01**, not on 09-04).
- [x] **Every exposure name carries a flow tag with its asof date** (2026-09-04) plus OBV state,
      rs20/rs60 and, where measured, `[FINRA]` z. **STORY-ONLY names did not leak into the candidate
      hand-off** — §9's hand-off column lists only Cards 1 and 5.
- [x] **Every card has both branches, a kill condition and a dated horizon.** Kill conditions are
      falsifiable and name an instrument, not a feeling. ★ Card 1's most likely kill (**US policy
      pressure on refiner margins**) is named even though it is **not** in `P136`'s VOID clause.
- [x] **`EVENT_ALPHA.md` written**; CONFIRMED-EARLY handed to ROTATION/BET; **book flag emitted**
      (`ETN`); **5 ledger rows filed**, both ledgers, all with `--revives-if`/`--enters-if` +
      `--recheck-date`.
- [x] **No sizing, no buy/sell language anywhere** (P4). `⚡crowded-short` and 🟢 tags are reported
      with their instrument caveats attached (`D6`, `C29`).
