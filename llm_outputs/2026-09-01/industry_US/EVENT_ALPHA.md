# EVENT_ALPHA — industry_US · 2026-09-01 (Tue) · Stage 5 / L1·EVENT_ALPHA

> Bottom-up complement to MACRO's top-down matrix. **Scope `--scope foreign` on every call** (W6 /
> market-lock). Flow tags from `SECTOR_FLOW_US_REPAIRED.json`, **asof 2026-08-31** — the primary
> file's OBV axis is revoked (PREFLIGHT G0b). **This stage never sizes** (P4).
> IDs: **M1190–M1196 · D456–D458**.

## 0 · Selection log — no silent truncation

`thread --days 7 --scope foreign`, window denominators **08-26 832 · 08-27 854 · 08-28 734 ·
08-29 307 · 08-30 292 · 08-31 717 · 09-01 383 (partial)**; 4,119 daily events → 3,167 threads,
**517 multi-day, 136 ALIVE**, 2,650 one-day (241 new today).

**136 alive → 8 selected → 128 not selected.** Selection rule applied as written: **precursor form
first** (curve starting ≤2 outlets and climbing), then remaining BUILDING/REIGNITED by peak.

⚠ **Two selection notes stated rather than hidden:**
1. **The board's largest thread was deliberately NOT carded.** *"Energy stocks rally as fresh
   U.S.-Iran attacks drive oil prices higher"* (**15→16→17→16→19→22→15**, 22 outlets / 86 articles at
   peak) is already carried both-sided by **`P122`**, registered at MACRO this run. Carding it would
   double-count one observation. **Named here so the absence is not read as a miss.**
2. ⚠ **`FADING` tags in this window are partly an artifact**: 09-01 is a **partial day (383 vs 717
   articles)**. Every curve below is read against that denominator, per the protocol's own warning.

---

## Card 1 — ★★★ Memory tightness, stated from the BUYER's side

| | |
|---|---|
| **Thread** | *"Tim Cook Ends Tenure As Apple CEO"* → 09-01 *"Tim Cook's Last Warning as Apple CEO Was That Memory Chip Shortages Won't Improve Any Time Soon"* · **BUILDING 7→8→6→4→3→14→21** · events 4,119 / threads 3,167 / alive 136 |
| **Direction (body-read)** | **Not a succession story — a cost story.** Bodies [nasdaq · yahoo_finance · fool, 09-01] carry it verbatim: memory chip shortages *"won't improve any time soon"*, framed as a question about **Apple's margins under John Ternus**. ⇒ the desk's memory-tightness frame now has a **buy-side, named, dated corroborator** — the largest hardware OEM's outgoing CEO saying the input is scarce. This is the first time the frame has come from the customer rather than the supplier. **`M1190`** |
| **Exposure** (chain position · flow tag asof 08-31 · crowding) | **`MU`** supplier/epicenter · **+0.270 🟡중립**, OBV **+0.095 매집**, `rs20` **+14.3 vs `SPY`**, **Δ +0.255** · not crowded (`vol_surge` 0.53) — ⚠ **headline layer** · **`SNDK`** supplier · **+0.481 🟡**, `rs20` **+20.4**, **Δ +0.343** · **`STX`** supplier · −0.056 🟡, OBV +0.104 매집 · **`WDC`** supplier · **−0.861 🔴분산**, `rs20` −15.8, `rs60` **−23.0** · **`AAPL`** buyer/cost-payer · +0.261 🟡, OBV +0.234 매집, **Δ +0.830 = the largest single-name Δ in the 299-name universe** |
| ★ **The split inside the chain, measured** | **`M1191`** — the memory complex is **not** moving as one: `MU`/`SNDK` are accumulating with positive Δ while **`WDC` is the 10th-worst name on the entire board.** ⇒ "memory is tight" does **not** transfer to every memory ticker; NAND/HDD and DRAM are being priced apart. Any card that treats them as one bet is wrong by measurement, not by opinion |
| **Future — IF** the thread keeps building **AND** `MU` flow stays ≥ 🟡 with OBV 매집 → the shortage is a **pricing** event and the supplier leg re-rates; **KPI** `MU` `rs20 vs SPY` (now +14.3) and `MU` Δ (now +0.255); **horizon 2026-09-24** (`MU` FQ4 print, already on the calendar) |
| **ELSE — kill condition** | `MU` OBV turns **분산** *or* `rs20 vs SPY` < 0 on a settled close before 09-24 ⇒ the tightness is being absorbed by the buyer, not paid to the supplier, and `AAPL`'s +0.830 Δ was the whole trade |
| **Cell** | **CONFIRMED-EARLY** on the supplier leg (`MU`, `SNDK`) — handed to BET §B. ⚠ **`WDC` explicitly NOT handed forward** |
| **Relationship to the carry** | `R111` (retracted 08-30) established that the take-or-pay frame **does** transfer to memory. This card is the demand-side half of the same claim. `P111` settles 09-14 |

---

## Card 2 — ★★★ A September rate HIKE is now a coin flip, and the labour print is the trigger

| | |
|---|---|
| **Thread** | *"Warsh Sounds Hawkish, but Will There Be a September Rate…"* → *"The Odds of a September Rate Hike Have Nearly Doubled"* · ★ **precursor form, BUILDING 2→5** · same denominator |
| **Direction (body-read)** | Unambiguous and multi-outlet: *"September Fed decision is now a coin flip as rate hike odds increase post Warsh"* [cnbc, 08-28] · *"The Jobs Report May Force A September Rate Hike And Send Rates Soaring"* [seekingalpha, 08-30] · *"US Dollar: September hike odds stay elevated"* [BBH via fxstreet, 09-01] · *"Barclays turns hawkish on Fed, sees two rate hikes in 2026"*. ⇒ **the market is pricing a HIKE, not a pause**, and the bodies name **the August payroll print (09-04)** as the decider |
| **Exposure** | Sector-level, not name-level (`C1`, `SPY` benchmark): **`XLU` `exc20` −6.04pp · `XLRE` −3.61 · `XLP` −1.10 · `XLI` −5.62** — the duration-proxy complex. Financials `XLF` `exc2` **+0.23pp** is the only positive-facing leg, and it is a **barred bucket** on `wflow` this run (SWEEP §0) |
| **Future — IF** the thread keeps building through the 09-04 print → `P121` branch A (`DGS2` ≥ 4.50 with `T10YIE` ≤ 2.36); **KPI** `DGS2` (4.34) and `T10YIE` (2.31) |
| **ELSE — kill condition** | `DGS2` ≤ 4.18 at the first `[FRED]` close covering 09-04 ⇒ the hawkish read did not survive the labour print; the whole duration-underweight leg loses its driver |
| **Cell** | **CONFIRMED-EARLY at the sector level**, already bracketed (`P121` · `S126` · `P114`). **No new name handed forward** — the card's job here is to date the trigger, not to add candidates |

---

## Card 3 — ★★★ It is a GLOBAL duration event, not a US one. The frame was too narrow.

| | |
|---|---|
| **Thread** | *"Why bonds are the most important market in the world"* → *"Global bond yields soar to multi-decade highs as Middle [East…]"* · ★ **precursor form, BUILDING 3→7** |
| **Direction (body-read)** ★ | **The body inverts the desk's own framing.** *"From the U.K. to Japan, bond yields are jumping as U.S. bonds tumble"* [marketwatch, 09-01] · *"Long-term government borrowing costs leap to a 28-year high ahead of the Budget"* [independent, UK] · *"Market Fear Index Rises as Bond Yields Spark Panic"* [yahoo_finance, 09-01] · and the `blindspot` raw sample *"Longer-dated US Treasury yields climb as Iran and US restart military attacks"* [economictimes, 08-31]. **`M1192` [measured] — MACRO §A read the 08-28 move as a Warsh/policy-path repricing. The corpus says the same move is happening in the UK and Japan simultaneously, and links it to the Gulf.** A US-only explanation cannot produce a UK 28-year high |
| ⚠ **What this does NOT overturn** | §A's **decomposition** is unaffected — `DGS10` +6bp = real +8 / breakeven −2 is arithmetic and stands. What widens is the **attribution**: the driver may be global term premium rather than the Fed path alone, and **`P121`'s KPI is exactly the instrument that separates them** (branch A firing *with* `T10YIE` above 2.42 would say the mechanism is wrong) |
| **Exposure** | ⚠ **The desk has no clean vehicle for this and says so** (`L.vehicle없음` class). US sector proxies are contaminated: the same underweights that express "Fed hawkish" express "global term premium", so **no card-level exposure is claimed**. ⇒ **`D456`** |
| **Future — IF** the thread keeps building → the duration underweights keep paying **for a reason the desk has not measured**; **KPI** `DGS30` (5.22) vs `^TYX` (5.249) — if the long end starts leading the front end, the global-term-premium reading wins |
| **ELSE — kill condition** | `DGS2` and `DGS30` move together on the 09-04 print (front-led) ⇒ policy path, and this card is a coincidence of calendars |
| **Cell** | **STORY-ONLY** — no exposure name is handed forward. **Filed with a dated re-check (09-04), not dropped** |

---

## Card 4 — ★★★ AI compute is being contracted in GIGAWATTS, and the number is now public

| | |
|---|---|
| **Thread** | *"Anthropic signs $35 billion cloud deal with Nvidia-backed Lambda"* · **BUILDING 4→4** (2 days) |
| **Direction (body-read)** | Confirmed across [yahoo_finance · cna, 09-01]: **$35bn**, counterparty **Lambda**, and — the load-bearing detail — *"…in a Deal Where **Chip Giant Holds the Lease**"*. ★ Paired same-day: *"**Sundar Pichai Says Alphabet Can't Build AI Capacity Fast Enough, and Anthropic Has Secured 5 Gigawatts of It.**"* ⇒ **`M1193`: the unit of the AI trade has become the gigawatt, stated publicly by a hyperscaler CEO**, and the vendor is taking lease risk on its own customer's capacity |
| **Exposure** | **`NVDA`** epicenter/lessor · +0.246 🟡, OBV **−0.098** (⚠ *not* accumulating), `vol_surge` **1.39** (highest in the book), **Δ −0.301** — ⚠ **headline layer, crowded by construction** · **`ANET`** networking · +0.319 🟡, OBV +0.192 매집, `rs60` +16.6 · **`MSFT`** +0.261 🟡, OBV **+0.327 매집**, `rs60` **+17.2** · **`ORCL`** +0.237 🟡 but `rs60` **−38.2 vs `SPY`** |
| **Future — IF** the thread keeps building **AND** flow stays ≥🟡 → capacity contracts convert into a **power** bottleneck (Card 5 is the test); **KPI** `NVDA` OBV (now −0.098) — a turn to 매집 with `vol_surge` holding would be the first accumulation signal in the epicenter this run |
| **ELSE — kill condition** | `NVDA` OBV stays 분산-side **and** `vol_surge` falls below 1.0 ⇒ the contracts are being announced into distribution |
| **Cell** | **LATE-MONEY** — the story is unambiguous and the epicenter's OBV is **negative with the highest surge on the book**, which is the shape of a crowded layer. **Valuation gate note attached; not handed to BET as fresh** |

---

## Card 5 — ★★★ THE FALSIFIER: Texas halted data-center power, and the corpus names the mechanism "ghost demand"

| | |
|---|---|
| **Thread** | *"Analysis — Texas' halt on powering data centers reflects US reckoning over 'ghost' demand"* [reuters via yahoo_finance **and** cna, **2026-09-01**] · **new, 2 outlets — precursor form, day 1** |
| **Direction (body-read)** ★★ | **This is the card that argues against Cards 4 and against `P123` branch A**, and it is registered as such rather than omitted. A US state has **halted** new data-center power interconnects, and the reporting frame is that the interconnection queue contains **duplicate / speculative "ghost" requests** — i.e. the headline demand number is **not** a delivery number. Corroborating same-window bodies: *"AI Power Demand Is Exploding, But How Much Actually Gets Built"* [13 outlets, 08-31] and *"'Clearly, people hate data centers': Sam Altman admits Americans hate what he's wrought as his own data centers head quits"* [fortune, 08-27] |
| ★ **The tape agrees with the falsifier, not with the story** | **`M1194` [measured] — EVERY measurable AI-power name is 🟡 or 🔴; not one is 🟢.** `ETN` −0.339 🟡 (**Δ −0.687**) · `VRT` −0.215 🟡 (**Δ −0.687**, `rs60` **−21.4**) · `NEE` −0.254 🟡 · `CEG` −0.396 🟡 · **`VST` −0.767 🔴** · **`PWR` −0.597 🔴** · **`FIX` −0.783 🔴** · **`DUK` −0.672 🔴** · **`SO` −0.597 🔴**. ⇒ **the story is building while the money disperses**, and this thread supplies the *mechanism* for the divergence rather than leaving it as a puzzle |
| **Exposure** | The names above, **short-side of the narrative** — ⚠ **this desk issues no directional recommendation** (P4). The card's function is as a **kill condition**, not a position |
| ⚠ **Disclosed against `P123`, registered THIS RUN, one stage earlier** | `P123`-A needs `EW{SLB, ETN, NEE, VRT} − SMH ≥ +5.00pp`. The basket's flow reads **`SLB` +0.822 🟢 against `ETN` −0.339 / `NEE` −0.254 / `VRT` −0.215** — **one strong leg and three weak ones.** ⇒ **the post-registration evidence points to branch B or C.** **The threshold is NOT moved** (`D242`); this is recorded as a **disclosed pre-settle state, explicitly NOT a score** — and per HANDOVER §F-2 this desk's pre-settle reads have been wrong **four for four** |
| **Future — IF** more states or utilities follow Texas → `P123` **B**; **KPI** `VRT` Δ (now **−0.687**, joint-worst in the universe) |
| **ELSE — kill condition** | ≥2 of {`ETN`, `NEE`, `VRT`, `CEG`} turn OBV 매집 with `rs20 > 0 vs SPY` on a settled close before **09-08** ⇒ the halt was a local regulatory event and the power leg is real |
| **Cell** | **STORY-ONLY (bear side)** → watchlist with a dated re-check **2026-09-08**. ⇒ **`D457`**: *a card whose function is to falsify another card in the same run is written as its own card, not as a caveat inside the one it attacks* |

---

## Card 6 — ★★ Optical: the leg is real, but its two names have separated

| | |
|---|---|
| **Thread** | *"MXL's AI Optical Growth Accelerates: Can It Challenge …"* · **REIGNITED 8→2** · plus same-window bodies *"AI-Driven Optical Transceiver Investment Surges as Hyperscale Demand and Strategic M&A Reshape Global Connectivity Infrastructure"* [yahoo_finance, 08-31] · *"AI Chips Update — Optical Transceivers Propel AI Data Center Growth"* [08-31] · **"Luxnet eyes orders through 2028, DCI revenue set to double in 2027"** [digitimes, 08-31] |
| **Direction (body-read)** | Demand statements are **dated forward to 2027–2028** (Luxnet's DCI revenue doubling in 2027, order book through 2028), not to the current quarter. ⇒ **a duration story, and the tape should not be expected to pay it this month** |
| **Exposure** | **`LITE`** · **+0.533 🟡**, OBV **+0.284 매집**, `rs20` **+16.1 vs `SPY`**, `rs60` −4.5, Δ −0.017 · **`COHR`** · **−0.188 🟡**, OBV +0.051, `rs20` −4.8, **`rs60` −35.5**, **Δ −0.805 = the worst Δ in the entire 299-name universe** · `CIEN` −0.413 🟡 (`rs60` −29.8) · `GLW` −0.130 🟡 (`rs60` −26.1) |
| ★ **Direct consequence for an ARMED row** | **`M1195` — `S137` (settles 09-09) is `EW{LITE, COHR} − SMH`, and its two legs are moving in opposite directions** (`rs60` +16.1 vs −35.5 on `rs20`; Δ −0.017 vs −0.805). An equal-weight basket of a diverging pair measures the **average of two different stories**. **The row is NOT re-banded** (`D242`) — the divergence is disclosed now so the settle is not read as a clean optical verdict. ⇒ **`D458`** |
| **Future — IF** the thread keeps building AND `LITE` holds OBV 매집 → optical is its own leg (`S137` A); **KPI** `LITE` OBV (+0.284) and the `LITE`−`COHR` `rs60` spread (now **51.6pp**) |
| **ELSE — kill condition** | `LITE` OBV turns 분산 before 09-09 ⇒ `D250` should be **closed as not-a-gap**, per `S137`-B's own wording |
| **Cell** | **CONFIRMED-EARLY on `LITE` only** — handed to BET §B as a single name, **explicitly not as an optical basket.** `COHR` is **not** handed forward |

---

## Card 7 — ★★ The named bottleneck is copper, and positioning is already at its own extreme

| | |
|---|---|
| **Thread** | *"Nvidia just lined up $500 billion. Frank Holmes says the thing that's scarce isn't money, it's copper"* [yahoo_finance, 08-31] — one-day, and it is carried here because it **names the physical constraint** that Cards 4 and 5 argue about |
| **Direction (body-read)** | The claim is a **substitution of the binding constraint**: capital is abundant, the metal is not. ⚠ Single-outlet on this framing — **labelled**, and it is used as a *frame*, not as evidence |
| **Exposure** | **`FCX`** · **+0.700 🟡**, OBV +0.202 매집, `rs20` **+17.8 vs `SPY`**, `rs60` +7.4, `vol_surge` **1.06** · **`NEM`** · **+0.772 🟡** (rank **6 of 299**), OBV **+0.355 매집**, `rs20` **+30.9**, `rs60` **+15.1**, `vol_surge` **1.19** |
| ★ **The contradiction is the card** | **`M1196` — `C24` reproduces for a third run and now has a narrative attached.** Copper spec positioning is at the **100th percentile of its year** `[COT 08-25]` — the single most crowded reading on the entire positioning board — while the Materials sector reads **0 greens / 2 reds of 12** and fell from flow rank 1 to rank 2. **The story is arriving at a position that is already maximally held.** That is the LATE-MONEY shape, stated |
| **Future — IF** copper spec %ile falls below **80** while `FCX`/`NEM` hold OBV 매집 → the crowding unwound without the price, which is the only configuration that makes this ownable; **KPI** copper 1-year spec percentile (now **100**) |
| **ELSE — kill condition** | `FCX` **or** `NEM` OBV turns 분산 while spec stays ≥90th %ile ⇒ distribution into a crowded long |
| **Cell** | **LATE-MONEY** — valuation/crowding gate note attached. ⚠ **`NEM` filed to the miss ledger this stage** (`M.숏리스트탈락`, recheck **09-08**): it ranks 6th of 299 on flow and was excluded from the shortlist **solely because `vol_surge` 1.19 missed the 1.2 bar by 0.01** |

---

## Card 8 — ★★ Shein's debut prices the tariff regime, and it prices it badly

| | |
|---|---|
| **Thread** | *"How Shein lost its shine ahead of long-awaited stock market …"* → *"Shein shares slide in Hong Kong trading debut"* · **BUILDING 4→17** (the largest 1-day outlet jump in the alive set) |
| **Direction (body-read)** | The bodies name the cause and it is **policy, not execution**: *"Shein Stock Waited Years to IPO Only to Flop. **Blame Trump.**"* [yahoo_finance] · *"shares plunge up to 28% in grey market ahead of Hong Kong debut"* [scmp] · *"shares fall up to 10% after long-awaited trading debut"* [marketwatch] · *"shares drop 7% in Hong Kong market debut"* [cnbc]. ⚠ **The magnitude is reported three different ways (−28% grey / −10% / −7%)** — the direction is corroborated 4-of-4, **the number is not**, and it is not used |
| **Exposure** | ⚠ **No clean US vehicle.** Shein is HK-listed and outside `us_top300`. The read-through is to the **de-minimis / cross-border tariff channel**, which lands in Consumer Discretionary — a bucket **barred from a `wflow` verdict this run** (`AMZN` 40.2% flipper). `AMZN` itself is **−0.822 🔴분산** (OBV −0.492, the 3rd-worst on the board) with its own dated cause (the FTC/22-state suit, 13 outlets) |
| **Future — IF** the thread keeps building → the tariff channel is repricing a whole cross-border cohort, and `INDU`/`DISC` underweights gain a second driver; **KPI** the `tariff` 7-day count (**2,025**, direct query outside the sweep window) |
| **ELSE — kill condition** | Shein trades back above its offer price within 5 sessions ⇒ a pricing failure, not a regime read |
| **Cell** | **STORY-ONLY** — no name handed forward, and the reason is `L.vehicle없음`, not low conviction |

---

## 9 · Threads read and NOT carded — ledgered, not dropped silently

| thread | outlets | why no card | ledger |
|---|---|---|---|
| *"U.S. Army Secretary Driscoll resigns after Pentagon leadership rift"* | BUILDING **6→8** | ★ **Killed on the direction body-read.** Bodies [upi · axios · scmp · bbc · seekingalpha] describe an 18-month tenure ending in a rift with Hegseth and name **zero** program, budget or procurement change. The headline reads as defense turmoil; the bodies contain no measurable exposure change | ✅ **`reject_ledger`** — `RTX`, `K.본문반증`, revives-if *"a named US Army program cancellation, restructuring or budget line change reported by ≥2 independent foreign outlets"*, recheck **2026-09-15** |
| `NEM` (Card 7) | — | cleared the money axis (rank 6 of 299) but was filtered out of the shortlist by 0.01 of `vol_surge` | ✅ **`missed_ledger`** — `M.숏리스트탈락`, enters-if *"`vol_surge` ≥ 1.20 with 매집 held and `rs20` > 0 vs `SPY`"*, recheck **2026-09-08**, `--sample prospective` |
| `MPC` (SWEEP §3) | — | rank 9 of 299, OBV +0.427 매집, `rs60` +38.5 vs `SPY`; excluded by `vol_surge` 1.08 — the 2026-07-21 refiner artifact reproducing | ✅ **`missed_ledger`** — `M.숏리스트탈락`, same enters-if, recheck **2026-09-08**, `--sample prospective` |
| **128 non-selected alive threads** | — | below the precursor/peak cut | **counted, not silently truncated** |

## 10 · Book cross-check — ENDED threads under open positions
- ⚠ **`AVGO`** (held, **−0.616 🔴분산**, `rs60` **−12.9 vs `SPY`**): the *"Nvidia tops earnings estimates,
  guides to $108 billion"* thread is **FADING 18→15→5→5→5→8→3** and the AI-print attention that
  carried the whole compute complex has decayed four sessions after the print. **`AVGO` prints
  09-02/09-03** (`S132`, ±9.00pp) — the position re-justifies on its own print, and it is the only
  book name with a dated event inside 48h. **Flagged to the book desk.**
- ⚠ **`ETN`** (held, −0.339 🟡, **Δ −0.672**, `rs20` −9.5 vs `SPY`): its thesis rides the AI-power
  layer, which **Card 5 just supplied a named falsifier for.** Attention has not ended, but the
  **money has**: every power name on the board is 🟡 or 🔴. **Flagged.**
- ✅ **`MPC` · `PSX`**: threads alive (Energy, peak 22 outlets), flow positive, `rs60` **+38.5 / +32.6
  vs `SPY`**. No re-justification owed.
- ⚠ **`S130`** (armed to 09-10) rides the *"Nvidia agrees to acquire Hugging Face for $12.9B"* thread,
  **ENDED 15→2 on 08-28**. Staleness flag raised for a **2nd** run — the row may still score; its
  premise no longer has an audience.

## 11 · Hand-off
- **→ ROTATION (sector-level cross-evidence)**: Energy confirmed a 5th independent way (Card 7's
  copper aside, Cards 1/4/5 all route capital toward *physical* inputs); **the AI-power layer is a
  story with no money behind it** (Card 5) — which cuts **against** any Utilities/Industrials
  promotion on an AI-power argument; the duration underweights gain a driver (Card 2) but the
  **attribution is contested** (Card 3).
- **→ BET §B (CONFIRMED-EARLY candidates, unsized)**: **`MU`**, **`SNDK`** (Card 1) · **`LITE`**
  (Card 6, single name, not a basket). **Nothing else.** STORY-ONLY names (`Card 3` vehicles, Shein
  read-throughs) did **not** leak into this list.

## ✅ EXIT CHECK
- [x] Scope market-correct — **`--scope foreign` on every `brief`/`thread`/`fts` call** in this stage.
- [x] Selection logged: **136 alive → 8 selected → 128 not selected**, plus one deliberate
      non-selection (the Energy thread, owned by `P122`) named with its reason.
- [x] **Every card has a direction body-read**, and **two cards were changed by it**: Card 1
      (succession → cost), Card 3 (US policy → global duration). **One thread was killed by it**
      (Driscoll) and ledgered.
- [x] Every exposure name carries a flow tag **with asof 2026-08-31**; **STORY-ONLY names did not
      leak** into the §11 hand-off.
- [x] Every card carries **both branches + a kill condition + a dated horizon**.
- [x] ENDED-thread book flags emitted (§10, four of them). Reject/miss ledgers written with
      `--revives-if` / `--enters-if` and recheck dates — **3 rows filed this stage**.
- [x] `EVENT_ALPHA.md` written; CONFIRMED-EARLY handed to ROTATION/BET.

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **ROTATION** (Stage 6).
> ⚠ ROTATION inherits three barred `wflow` buckets (DISC · FIN · COMM), the IT breadth contradiction
> (41/56 positive excess vs `eqflow` −0.014), and Card 5's finding that the AI-power layer has
> **zero** 🟢 names.
