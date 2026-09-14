# EVENT_ALPHA — industry_US · 2026-09-14 (Mon, 13:5x–14:1x KST, NYSE pre-open) · Stage 5 / L1·EVENT_ALPHA

> Scope: **foreign only** — every narrative input below is from the foreign pool. **Analytical output only; no
> buy/sell language; BET owns sizing.**

## 0 · Instrument state — what "thread" means today, and what it does not
- `thread --days 7` / `chain-hop` / `theme-age` **could not run** (remote dead from 13:19; the client derivative's
  cursor is 09-09 08:44). **Substitute, declared**: a **per-day distinct-outlet curve computed on the local
  09-13 pull** (`_thread_proxy_local.txt`; foreign-titled rows only; regex on title+summary). It is a *proxy*:
  🚨 **the pool's per-day denominator is grossly uneven** — 09-07 **39** · 09-08 113 · 09-09 176 · 09-10 440 ·
  09-11 **780** · 09-12 749 · 09-13 160 (a one-shot RSS pull keeps recent items) — so every curve is
  **mechanically BUILDING into 09-11/09-12**. Curves are read **only for within-day outlet counts and for the
  09-12 → 09-13 direction**, never as "started at 2 and climbed" (the precursor shape cannot be seen in this
  pool). Direction body-reads: **0** (no bodies in the pool) — every direction line below is a **title-read**
  and is tagged; per the L1 rule *"headline-only cards are a failed stage"*, **no card is handed to BET as
  CONFIRMED-EARLY on narrative alone** — the hand-off column says so.
- Money leg: `module_flow … --bench SPY` (`_flow_ea.json`, settled to 09-11) + `[FINRA 09-11]` + sweep OBV.
  ⚠ `module_flow`'s news-velocity column ran on the local fallback (e.g. `ORCL` 4.29×, the artifact) — **the velocity
  column is quarantined**; tags are read with their OBV/surge/RS components stated.

## 1 · Selection log
Alive threads found in the pool (outlet count on the peak day): Saudi East-West pipeline (7s) · Houthi/Bab
el-Mandeb (9s) · Fed hike/Warsh/G7 (12s) · Anthropic/AI-slowdown (17s) · OpenAI IPO (10s) · Oracle/Ellison (7s) ·
SpaceX/NDX (4s) · Dell/AI-server (5s) · Nvidia (9s) · Micron/memory (5s) · Diesel/distillate (7s) · Tanker rates
(4s) · ECB/Lagarde (5s) · BoJ (3s) · Yen carry (2s) · Canada/USMCA (5s) · Germany far-right (7s) · Amgen/Regeneron/
FDA (3s) · Copper (2s, fading to 0) · US blockade on Iran (1s) — **20 read**.
**Selected 8** (below). **Not selected 12**: ECB (settled 09-10, `S152` owns the `TLT` read), BoJ + yen (no US
equity exposure; `P153` registered at MACRO), Canada (`S129`-C settled; no live name), Germany (`P146` settles
tonight), Amgen/REGN (`S133`/`P150` own it; the REGN item is a class-action solicitation), copper (0 outlets on
09-11/12/13 — the thread faded while `C24` positioning did not), blockade (1 outlet), Nvidia-general (absorbed
into cards 4 and 6), OpenAI IPO (merged into card 4), diesel (merged into card 2), tanker rates (merged into
card 1). **Silent truncation: none.**

## 2 · Forward cards

### Card 1 — The second chokepoint: Saudi East-West line shut + Houthis at Bab el-Mandeb → the freight leg
- **Thread**: *Saudi pipeline* 09-11 4s → 09-12 **7s/9a** → 09-13 2s; *Houthi/Red Sea* 09-10 5s → 09-11 8s → 09-12
  **9s/13a** → 09-13 3s/7a (the 09-13 Sunday pool is 160 rows; 3 of them = the day's top-3 share). Window
  denominator above. **No `thread` tag** — proxy only.
- **Direction (title-read)**: supply-route loss on the *non-Hormuz* export path plus a second strait under
  hostile control ⇒ **tanker-days and war-risk premia rise; barrel bid; product offered live** (MACRO §A-4).
  Quoted title: *"Oil tanker rates reach record highs on surging risks to Middle East shipping"* (SA, 09-11).
- **Exposure** (asof 09-11 settled, `module_flow`): `FRO` 🟢 OBV accumulating rs20 +23.2 surge 1.37 · `DHT` 🟢 accumulating +16.3 /
  1.26 · `INSW` 🟢 accumulating +10.7 / 1.41 · `TNK` 🟢 accumulating +22.4 / 1.29 · `STNG` 🟢 accumulating +9.4 / 1.25 — **all five 🟢 on
  OBV+surge (velocity column quarantined)**; headline-layer by construction (the titles name "tankers");
  **none in `us_top300`** (no FINRA z, no sweep score — `D563`). One hop past: E&P barrel names `XOM`/`CVX`/
  `COP`/`OXY`/`DVN`/`EOG` all 🟡 OBV accumulating with surge 0.85–1.05 (the sweep's filter artifact, SWEEP_READ §2-1).
  Crowding: tanker basket already **+7.95pp vs `SPY` on the week = 91.7th pctile, +16.4pp / 20 sessions**.
- **Future**: IF the East-West line stays shut through the week AND the tanker basket holds 🟢 → `P152`-A
  (≥ +6.24pp vs `SPY`, 09-14 → 09-21); track KPI = `P149` (barrel vs `XLE`) and `S156` (crack). ELSE (a ≥3-outlet
  reopening *and* transit-restored title, or basket OBV turns distributing) → **kill**: the freight leg was the crowded
  expression (`P152`-B ≤ −4.31pp).
- **Cell**: BUILDING (proxy) × 🟢 ⇒ **CONFIRMED-EARLY on the money axis, headline-layer on the story axis** —
  hand-off to BET **as a bracketed leg (`P152`), not as a name**: the five are outside the universe and the
  desk cannot tag them daily. ⚠ Anti-crowding note: state-at-registration is already above A.

### Card 2 — Products vs barrel: the distillate crack gave back ≈6.6 $/bbl in one Asia session
- **Thread**: *Diesel/distillate* 09-10 2s → 09-11 **7s/10a** → 09-12 4s/6a → 09-13 0. Titles: *"U.S. diesel prices
  are now 60% higher than before the Iran war"* (Fortune), *"Diesel in Portugal hits record high"* (Euronews).
- **Direction (title-read + live tape)**: the *level* story is at peak outlets while the live tape prints
  `HO=F` −1.79% / `RB=F` −3.75% against `CL=F` +2.85% (`M1502`) — **the narrative is at its high-outlet day and
  the product tape is going the other way**. This is the `L1` (rate-over-level) reading the desk lost on
  `P140`-B last week; it is **not re-asserted as a verdict** — `S156` is the pre-committed bracket.
- **Exposure**: refiners `VLO` 🟡 OBV accumulating +0.37 rs20 +15.6 rs60 **+58.1** surge 1.14 · `MPC` (held) 🟡 accumulating +0.48
  / +12.8 / +56.2 · `PSX` (held) 🟡 accumulating +0.32 / +13.3 / +49.0 — extended-but-live on 09-12's read, all with
  FINRA z ≈ 0 (shorts not leaning in). Chain position: **bottleneck beneficiaries of scarcity, casualties
  of a crack collapse**.
- **Future**: IF the crack holds ≥ 100 through 09-18 AND OBV stays accumulating → the level thesis survives (`S156`-C/B);
  ELSE (`S156`-A ≤ −4.25 on the settled 09-18 close, or `MPC` < MA20 $374 / `PSX` < $247.5 per 09-12 rails) →
  **kill the crack leg of the Energy OW** — the barrel leg (`P149`) is a separate object.
- **Cell**: FADING-into-peak (proxy, 09-13 = 0 outlets) × 🟢-OBV/🟡-tag ⇒ **LATE-MONEY** — valuation gate
  (09-12: FY27 consensus −17…−36%, every refiner target below price) before any add; **book flag** (§3).

### Card 3 — "Rate-hike fever across G7": the hike is consensus; the split inside Financials is the live object
- **Thread**: *Fed hike/Warsh* 09-10 3s → 09-11 **12s/43a** → 09-12 12s/14a → 09-13 6s/6a — the pool's most
  populated Friday thread; titles ≥9 outlets (MACRO §B-1 #3).
- **Direction (title-read)**: a 25 bp hike on 09-16 is priced (*"Futures Traders Just Dramatically
  Repriced…"*, *"Investors brace for possible rate hike at uncertain Fed meeting"*); the desk's measured side
  says the same (`DGS2` +93 bp over `DFF`). **A consensus thread is not alpha** — the card is about *who
  inside Financials wins the level vs loses the flattening*.
- **Exposure**: `MET` (held) 🟡 OBV accumulating rs60 +9.3 surge 0.78 **FINRA z +1.95 🔴** (shorts leaning in at a 20-day
  extreme — the against-us tell) · `NDAQ` (held) 🔴 distributing rs20 −4.8 z +1.21 · `AIG` 🟢 (the sector's only 🟢,
  z +1.36) · duration trio `XLU` 🟡 neutral / `XLRE` 🔴 distributing / `XLP` 🟡 neutral (`S135`-A: one object).
- **Future**: IF `P151`-C/A (hike delivered, hawkish) AND `MET` OBV stays accumulating → insurers' asset-yield leg holds
  while exchanges/alt-managers stay the losers (09-12 `M1480` split); track KPI = `MET` z falling back < +1.0
  by 09-18. ELSE (`P151`-B dovish surprise, or `MET` z > +2.5 with OBV flipping) → **kill**: the book holds
  both sides of the hike by accident and the wrong one is winning.
- **Cell**: BUILDING × 🟡 ⇒ **uncalled (🟡)** — re-check **09-17** (post-FOMC settled close). Not handed to BET
  as a candidate; handed to ROTATION as the Financials split.

### Card 4 — AI governance + IPO supply: the weekend's largest cluster, and none of it is demand
- **Thread**: *Anthropic/AI-slowdown* 09-09 5s → 09-10 5s → 09-11 8s → 09-12 **17s/29a** → 09-13 3s; *OpenAI IPO*
  09-10 8s → 09-11 9s → 09-12 10s/14a. ≥18 outlets combined (MACRO §B-1 #1).
- **Direction (title-read)**: three CEOs call for slower model development; OpenAI rules out a 2026 IPO;
  Nvidia *in talks* to put ~$10bn into Anthropic's IPO (Reuters via cointelegraph/CNA); *"Anthropic Targets
  $2 Trillion Valuation"* (TradingKey). **Two opposite reads in one cluster**: (a) slower model cadence =
  slower compute demand growth; (b) an Anthropic IPO at ~$2tn with `NVDA` as anchor = more capital *into* the
  same capex chain. **Neither is body-read; both stated.**
- **Exposure**: `NVDA` (held) 🔴 distributing −0.24 rs20 −1.4 surge 0.85 (09-12: DISTRIBUTION node) · `AMZN` 🔴 distributing ·
  `GOOGL` 🔴 distributing rs60 −11.2 (Anthropic backers; both headline-layer) · `MSFT` 🟡 accumulating rs60 +24.0 surge 0.53
  (OpenAI) · `QQQ` 🔴 distributing. **Money is 🔴 on every headline-layer name.**
- **Future**: IF an Anthropic S-1 or a dated IPO appears with `NVDA` as anchor investor (EDGAR, not a title) →
  re-file as an *AI-IPO-supply* thread with a `[measured]` size; track KPI = `NVDA` OBV. ELSE → the cluster is
  governance narrative; **kill** for this desk on **09-21** if no filing.
- **Cell**: BUILDING × 🔴 ⇒ **STORY-ONLY** — watchlist, dated re-check 09-21. ⚠ Held `NVDA` rides the *demand*
  thread, not this one; flag to book (§3) that the sector's loudest story is not a demand print.

### Card 5 — SpaceX into the Nasdaq-100: the 09-18 rebalance now has a named seller
- **Thread**: *SpaceX* 09-11 3s → 09-12 **4s/7a** → 09-13 3s. Titles: *"SpaceX to Get Weighting Boost in Nasdaq
  100 After Rebalance"* (Bloomberg), *"Musk's secretive backer builds $40bn SpaceX stake"* (FT), *"3 Reasons
  SpaceX Stock Could Crash in Q4"* (fool/Nasdaq).
- **Direction (title-read)**: a weighting *increase* for one name inside a capped index is a **mechanical
  sale of the rest** on the rebalance date (09-18 — inside every 09-18 bracket window). Size **unknown**
  (`C3`); the desk's own `S56` (SPCX unlock, Aug) is the precedent for counted-supply rows.
- **Exposure**: `QQQ` 🔴 distributing · `AAPL` 🟡 accumulating rs20 +10.6 surge 1.07 · `MSFT` 🟡 accumulating · `NVDA` 🔴 — the names that
  lose weight; SpaceX itself carries **no flow instrument on this desk** (universe/registry blind, `D592`).
- **Future**: IF Nasdaq publishes the pro-forma weights (official source) before 09-18 → PREMORTEM/next MACRO
  registers a counted-supply bracket on the 09-18 close (`QQQ` vs `SPY` 1-session); ELSE → the item stays a
  title. **Kill**: no pro-forma by 09-17.
- **Cell**: BUILDING × 🔴 (index) ⇒ **STORY-ONLY** — dated re-check **09-17**; hand to PREMORTEM as a
  structural-supply candidate (calendar row *"sp quarterly rebalance"* gains this mechanism).

### Card 6 — AI-server orders and the optics race beyond 1.6T: the assembler/optics sub-leg, two-sided in titles
- **Thread**: *Dell/AI-server* 09-11 3s → 09-12 **5s/6a** → 09-13 3s/4a. Titles: *"Dell Booked More AI Server
  Orders in 3 Months Than It Recorded in Total Revenue"* (Nasdaq/fool), *"AI server exports to US slow;
  electronics parts jump 1.5× in August"* (Digitimes), *"AI server tracker: Taiwan optics race beyond 1.6T"*
  (Digitimes), *"Pegatron's AI server engine starts to outweigh notebook drag"*.
- **Direction (title-read)**: orders/backlog up at the US assembler while **Taiwan export volume slows** —
  consistent with 09-12's `HPE` inventory read (component allocation into assemblers, visible as working
  capital). Optics: the race is at 1.6T — the layer `S48`/`S86` flagged as unowned.
- **Exposure**: `DELL` 🟢 OBV accumulating +0.28 rs20 +16.5 rs60 +38.5 surge 1.22, FINRA z −0.95 ✅ (the board's only
  clean rise) · `HPE` (held) 🟢 accumulating +0.10 / +5.5 / +26.5 / 1.47, z +0.58 · `LITE` 🟡 accumulating +0.14 rs20 +7.0 · `COHR`
  🔴 distributing rs60 −22.1 · `GLW` 🟡 neutral rs20 +6.7 (velocity 1.25× quarantined). Chain: assemblers = bottleneck
  *holders*; optics = bottleneck *makers*.
- **Future**: IF `DELL`/`HPE` hold 🟢 through 09-18 AND `P111` (memory, tonight) does not fire B (i.e. memory
  keeps lagging the assemblers) → the assembler sub-leg stays the live node; KPI = `HPE` OBV > +0.25 by 09-18
  (09-12 rail). ELSE (`DELL` < $506.6 / `HPE` < $55.2, or optics `COHR`/`LITE` both 🔴) → **kill**.
- **Cell**: BUILDING × 🟢 (DELL/HPE) ⇒ **CONFIRMED-EARLY on money; title-only on story** — hand-off to BET
  **conditional on a body-read** (Dell's order figure is a title until the 8-K/transcript is read; `C3`).
  `COHR` = STORY-ONLY (money 🔴); `LITE` 🟡 uncalled, re-check 09-18.

### Card 7 — Memory: the thread rebuilt into `P111`'s settle night
- **Thread**: *Micron/memory* 09-10 2s → 09-11 **4s/13a** → 09-12 5s/14a → 09-13 2s. Titles: *"Is Micron Stock the
  Next Nvidia?"*, *"Broadcom vs. Micron…"*, *"Druckenmiller Dumped Broadcom, Intel, and Micron for This Chip
  Stock"* (Yahoo/fool) — **retail-channel titles, no primary print**.
- **Direction (title-read)**: attention without a fact. `P111` (EW{MU,SNDK,WDC} exc10 vs `SPY`) settles
  **tonight**; state leaning A (memory ignored the $160bn commitment).
- **Exposure**: `MU` 🟡 neutral rs20 +4.4 rs60 −6.3 surge 0.73 · `SNDK` 🟡 neutral +8.6 / −19.8 · `WDC` 🔴 distributing −6.5 /
  −36.2 — **money is neutral-to-dispersing on all three**; `MU` FQ4 **09-30** (`D488`).
- **Future**: IF `P111`-B (≥ +5pp — the tape was slow, not indifferent) → the deceleration leg is over-weighted
  and the memory node re-enters DEEP scope; ELSE (A or C) → the second-derivative framing survives; **kill for
  this desk**: `WDC` OBV < −0.30 with `MU` rs60 < −10 by 09-18.
- **Cell**: BUILDING (retail titles) × 🟡/🔴 ⇒ **uncalled** — the verdict is `P111`'s, tonight.

### Card 8 — Oracle: the insider withdraws $7.5bn of supply, the stock is still distributing
- **Thread**: *Oracle/Ellison* 09-10 4s → 09-11 **7s/17a** → 09-12 5s/7a → 09-13 4s/5a. Two titles in sequence:
  *"adopts trading plan to sell up to $7.5bn"* → *"cancels/scraps plan"* (WSJ, CNBC, PRN, CNA, Nasdaq, ET).
- **Direction (title-read)**: a cancelled 10b5-1 plan removes a *known* overhang; the cause is not in any
  title (`C3`). 09-12 `M1479`: FY27 capex $90–95bn **maintained, not raised**; *"Oracle's AI Chips Ran 97.9%
  Utilized"* (fool/Nasdaq) is a utilisation title, not a capex print.
- **Exposure**: `ORCL` 🟡 tag with **OBV distributing** rs20 −2.1 rs60 −22.1 surge **1.39** (volume without accumulation;
  velocity 4.29× = the artifact, ignored) — headline-layer. One hop: the AI-infra suppliers already in card 6.
- **Future**: IF `ORCL` OBV turns accumulating with rs20 > 0 on a settled close by 09-21 → the overhang removal was the
  turn; ELSE → supply withdrawal without demand; **kill** 09-21.
- **Cell**: BUILDING × 🔴-OBV ⇒ **STORY-ONLY** — watchlist, re-check 09-21. Not a candidate.

## 3 · Book cross-check — open positions whose thesis rides a thread that is not building
| position | thread it rides | state | flag |
|---|---|---|---|
| `MPC` · `PSX` | product scarcity / crack level | thread at peak-and-fading (0 outlets 09-13); **live crack −6.6** | ⚠ **re-justify on `S156` tonight → 09-18**; rails from 09-12 §3a |
| `NVDA` · `AVGO` · `ANET` | AI-compute demand | the loudest AI thread is governance/IPO-supply (Card 4), money 🔴 on `NVDA`; `AVGO` absent from every weekend title except retail comparisons | ⚠ demand thread **not measurable** (no thread tool); carried, not re-justified |
| `HPE` | AI-server backlog | BUILDING (Card 6), 🟢 | ✅ alive |
| `MET` · `NDAQ` | hike level vs flattening | BUILDING (Card 3), `MET` 🟡 with z +1.95 🔴, `NDAQ` 🔴 | ⚠ both sides held; `P151` decides |
| `RTX` | missile-defense / rearmament | Houthi/Saudi escalation titles (Card 1) — the *demand* side of the defense node is present in titles at ≥6 outlets, but `RTX` 🔴 −0.83 z +1.40 | ⚠ `S150` settles tonight |
| `NUE` · `ETN` | steel / power-equipment | **no thread in the pool** (0 titles) | ⚠ thesis rides nothing alive this week — carried to BET §holdings as *no narrative support measurable* |

## 4 · Ledger writes (this stage)
- `missed_ledger add`: **`AAPL`** (`Q.확신부족` — OBV accumulating rs20 +10.6 surge 1.07 with three product titles (A20 Pro
  2nm, foldable, TSMC), read and not carded; `enters_if`: tag 🟢 on a settled sweep with surge ≥ 1.2 OR rs60 > +15;
  recheck 09-21) · **`FRO`** (`N.유니버스부재` — cleared the money axis 🟢, cannot be tagged by the sweep;
  `enters_if`: universe rebuilt with a tanker include-list AND `P152` does not settle B; recheck 09-21).
- `reject_ledger add`: **`COHR`** (`A.flow미도착` — optics thread building, OBV distributing rs60 −22.1; `revives_if`: OBV
  turns accumulating with rs20 > 0 on a settled close; recheck 09-25) · **`WDC`** (`C.차트붕괴` — rs60 −36.2, OBV distributing;
  `revives_if`: `P111` fires B AND WDC OBV turns accumulating; recheck 09-25).
- No drop is a DEAD-cell drop (no thread is FADING × 🔴 on a *measured* curve today — the proxy cannot say FADING).

## ✅ EXIT CHECK — EVENT_ALPHA
- [x] Scope foreign-only; no KR feed used.
- [x] Selection logged: 20 read → 8 selected → 12 not selected, each with the reason. No silent cap.
- [x] Direction body-reads: **0 — stated, not hidden.** Every card's direction is a title-read and is tagged;
      the two money-confirmed cards (1, 6) are handed to BET **as a bracket (`P152`) and as body-read-conditional**,
      not as CONFIRMED-EARLY names on narrative alone. This is the declared degradation under G1.
- [x] Every exposure name carries a flow tag with asof (09-11 settled) and the velocity column's quarantine;
      STORY-ONLY names (`NVDA`-as-IPO-story, `AMZN`, `GOOGL`, `ORCL`, `COHR`, `QQQ`) are not in the candidate hand-off.
- [x] Every card has both branches, a kill condition and a dated horizon.
- [x] `EVENT_ALPHA.md` written; hand-offs: ROTATION (Financials split, Energy two-leg), BET (`P152` leg; `DELL`/`HPE`
      conditional), PREMORTEM (SpaceX/NDX structural supply, BoJ gap); book flags §3; ledger writes §4
      (executed after this file is written — receipts in `out/*_ledger*.jsonl`).
