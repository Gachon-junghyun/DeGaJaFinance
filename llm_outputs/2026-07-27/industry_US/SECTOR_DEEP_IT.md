# SECTOR DEEP — INFORMATION TECHNOLOGY · PREMORTEM PROMOTION (not a rotation pick)

**Asof: 2026-07-24 settled close** for every RS/OBV/flow number (`SECTOR_FLOW_US.json`). Written
2026-07-27 (Mon), ~09:4x ET, US session minutes old. **Last settled US close = Friday 2026-07-24.**
No `module_flow <TKR>` live call is used anywhere in this file (measured this run: SPY's 07-27 volume
was 8.6% of a full session; a live STX pull returns RS60 +22.9 where the settled value is +43.3 —
D74, third confirmation this run). Filings, fundamentals and news are called live and dated.
Analytical only — **zero buy/sell, zero sizing (P4)**.

**IT is Neutral, board's worst breadth: wflow +0.155 / eqflow −0.206, 25 🔴 / 4 🟢 of 56.** This file
was promoted on **information content** (three of four premortem lenses converged here), not on
flow. It does not re-print the 07-25 DEEP (`SECTOR_DEEP_IT.md`, the AI-server hardware/OEM leg
map) — this is a different mandate, answering three specific contradictions.

---

## §0 · Three verdicts, up front

**① P9/CXMT.** A funded fourth DRAM entrant is real and changes the *count* of the capacity clock,
but the one number available on its own pricing (2.2% premium over the Big Three in its home
market) says the **entrant is not undercutting** — i.e., new evidence, from the supply side, that
**C1 (LTA price floors) leans toward "floors hold."** That evidence is **single-source
(tomshardware, sourced to one X account, n=1 SKU, 1 retailer)** and could not be corroborated by a
second outlet in this run's search. **Keep it at single-source grade.** It says nothing yet about
*when* or on *which product* the $8.6bn raise binds — see §1c, `[blank]` where genuinely unknown.

**② STX.** The strongest revision book in the leg (current-qtr +30.6%, next-qtr +32.5%, next-FY
+38.3%/90d) sits on the single hardest-confirmed peak-margin case the desk has measured on any name
(FY25 GM 35.2% = 100th percentile of a 17-year, three-full-cycle series) at 28–30× forward. **L2
verdict: CONFIRMED, not a trap and not "cheap."** Both numbers, side by side, settle nothing about
direction — they settle that a multiple without a margin percentile is not a valuation, and here we
have both, and they point at the same conclusion from opposite directions: **the market is paying a
growth multiple for a name at its own all-time-record profitability, on a book that hasn't cut once
in 30 days.** That tension resolves on **2026-07-29**, inside a **±14.6% pre-declared no-information
band**.

**③ S30.** DELL and HPE are the control pair, and they hold: **DELL RS20 +6.2 / HPE +1.4** against
**memory-median RS20 −23.7 (STX −17.6, MU −24.7, WDC −23.7)**. The supplier leg's 20-day reversal has
not touched the two OEM names whose 60-day excess sits in days 21–60. **If the memory median crosses
above 0 by 2026-08-05 while DELL/HPE do not move with it, that is a memory-specific event, not an
IT-beta event** — exactly the discrimination S30 was built to make. HPE remains the board's
best-documented "flagged, not concluded" name: unanimous revisions, unmeasurable margin (§3).

---

## §1 · P9 / CXMT — does a funded fourth DRAM entrant change the capacity clock?

**The standing supply clock (M7, seed):** *"New DRAM capacity online: SK M15X + Micron Idaho
mid-2027; Samsung P5 2028."* Three suppliers, no fourth.

**What arrived 2026-07-27**, corroborated across five outlets in this run's own news search
(`fts CXMT --scope foreign --days 5`: economictimes, AP/yahoo_finance, fortune, scmp, AFP/yahoo —
121 total matches, cross-checking on every headline number):
- CXMT (ChangXin Memory Technologies) IPO'd on Shanghai's STAR market. Raised **¥57.92bn = $8.6bn**
  (AFP cites ¥66.6bn/$9.8bn gross including over-allotment — the two figures differ by the
  over-allotment option, both are `[news]`, neither is an issuer filing read by this desk).
  Asia's largest IPO of 2026; China's second-largest mainland IPO ever after Agricultural Bank of
  China (2010, $22.1bn) per SCMP.
- Opened **¥49.50 vs ¥8.66 IPO price = +470%** (AP/AFP put the intraday peak near +531%); market cap
  **≈¥3.3tn = $487bn**, passing ICBC ⇒ China's most valuable listed company.
- **World's 4th-largest DRAM producer.** Prospectus (as relayed by Reuters/economictimes): **~7.7%
  share in 2025**. Counterpoint Research (cited by AP), a different methodology (by shipments, not
  revenue): **~8% in 2025**, **~9% in Q1 2026**, forecast **~11% by 2028**, with Counterpoint's own
  research director stating CXMT needs "at least a 15% global market share to be competitive in the
  long term." Samsung 36% / SK hynix 29% / Micron ~24% by the same Counterpoint count. **Two
  independent estimates converge on ~8%, both `[news]`, neither an issuer number checked against a
  primary filing by this desk.**
- **Q1 revenue +719% YoY to ¥50.8bn ($7.51bn)**; **H1 2026 expected ¥110–120bn**, ≈2× FY2025's
  ¥61.8bn — **a company expectation stated in the prospectus, not a print** (C2/C3, see 1d).
  **Lags badly in HBM** — every outlet agrees on this, and it is the single most repeated caveat in
  the coverage.
- State shareholders **36.29%** pre-IPO (Hefei/Anhui municipal vehicles + China's "Big Fund").
  **Use of IPO proceeds, per the prospectus: "expand production capacity, improve manufacturing
  technology, increase R&D."** No dollar split disclosed between the three uses; no capacity date
  given (`[blank]`).
- **US DoD has designated CXMT a "Chinese Military Company."** A US interagency committee has
  **approved** a possible Entity List addition; **not yet implemented** (Reuters, relayed identically
  by AP/economictimes). Separately, **US House China Committee chair Moolenaar + Rep. Whitesides
  sent a letter (reported by tomshardware, 07-17, citing the Financial Times) asking Commerce to add
  CXMT to the Entity List and to block US firms from buying Chinese-made memory** — because, per the
  same reporting, **Apple has reportedly been seeking approval to source memory from CXMT**, and
  Corsair/Patriot already sell CXMT- and YMTC-based modules. This is the demand-side mirror of the
  capacity story: a hyperscaler-adjacent US buyer testing the entrant's output, against an active
  political effort to close that door. Neither the Apple sourcing report nor the Entity List timeline
  has a dated resolution (`[blank]`).

### (a) Corroboration attempt on the price observation — **failed to find a second source**

The single number that cuts against the "fourth entrant relieves the shortage" read
`[tomshardware, 2026-07-26, sourced to one X account @harukaze5719, n=1 SKU at 1 retailer]`:

> *"A 64GB DDR5-5600 RDIMM based on memory from Samsung or SK hynix costs 18,595 CNY ($2,745) at
> JD.com, whereas a module featuring the same capacity and specification, but using DRAMs from CXMT
> is priced at 18,999 CNY ($2,805)."*

**⇒ CXMT modules sell at a 2.2% PREMIUM to Big-Three modules in CXMT's own home market.** I ran
three independent full-text searches across this run's foreign-scope news corpus trying to
corroborate or refute it — `RDIMM` (7 matches, 15 days), `JD.com` (22 matches, 10 days — none about
DRAM pricing), `harukaze5719` (1 match) — and the tomshardware piece is the **only** hit in every
search. **No second outlet carries this observation.** I could not corroborate or refute it.
**It stays single-source grade — not laundered into a desk fact.** For scale-context only (not a
corroboration, a different market): the same article notes a Samsung-made 64GB DDR5-5600 RDIMM
sells for **$2,425 at Amazon.com in the US** — cheaper than either Chinese-market price, which says
the China market itself is running hot on both sides of the CXMT/Big-Three line, a separate fact
from the CXMT-vs-incumbent spread.

### (b) What it does and does not do to C1 and M1

**C1 (carried, unmeasured since seed): "LTA price floors — do they hold?"** This is genuinely **new
evidence, and it points toward "yes, they hold."** The tomshardware piece's own stated mechanism is
consistent with an LTA-floor story even though it never uses the term: *"as everyone is capacity
constrained these days, there is little incentive for CXMT to price its DRAMs significantly below
those from renowned makers,"* plus an older node (higher power, lower performance, worse
overclockability) and validation costs (Apple/Dell/Corsair-grade qualification) that "erase the
chip-level discount before it reaches a module." If the newest, state-subsidized, lowest-cost-basis
entrant into the single most price-sensitive consumer sub-segment (retail DDR5 modules) cannot or
will not discount, that is one data point against the "a funded new entrant crashes the cycle" fear
— but it is one SKU, one day, one retailer, in one geography, in the segment furthest from where the
margin story actually lives (enterprise/server DRAM and HBM, not retail consumer RDIMM).

**M1 (server-DRAM contract price, QoQ): 1Q26 +90~95% → 2Q26 +58~63% → 3Q26 +13~18%.** This CXMT
observation **does not touch M1 directly** — it is a *retail consumer DDR5* data point; M1 is
*server* DRAM contract pricing, a different product and a different customer (OEM/hyperscaler LTA
vs. JD.com retail). **Under lens L1 (level vs. rate): this is a level/funding fact — a capacity raise
and a single-point price observation — not a rate fact.** It says nothing about whether the M1
deceleration (already three quarters running) continues, accelerates, or reverses. **I agree with
the mandate's framing: treat this as level, not rate.**

### (c) Mechanism — when, and on which product

**When**: `[blank]`. No dated capacity-online figure exists for CXMT in any source pulled this run —
the prospectus language ("expand production capacity...") is a use-of-proceeds statement, not a
project timeline. Contrast this with M7's dated entries for the incumbents (SK M15X/Micron Idaho
mid-2027, Samsung P5 2028) — **CXMT has no comparable date and should not be given one by inference.**

**Which product**: the evidence so far is bimodal and the desk should keep both halves separate
(C3, unknown bucket):
- **Commodity DDR (consumer + likely enterprise DDR5/DDR4)**: this is where CXMT already ships and
  where the one pricing data point sits. If a capacity raise binds anywhere first, structurally it
  binds here — CXMT is a real, if small (~8%), supplier today, and Apple/Corsair/Patriot sourcing
  reports are all in this bucket.
- **HBM (the product that actually drives the AI-server margin story, M1/M2/M3)**: **every source
  this run agrees CXMT "lags badly."** No source gives CXMT an HBM shipping date. The capacity raise
  is explicitly use-of-proceeds language that does not name HBM. **This is the product where the
  desk's peak-margin thesis (MU, and by extension the whole M1 series) actually lives, and CXMT's own
  prospectus supplies no evidence it reaches there.** `[blank]` on a date.

**⇒ the honest mechanism statement**: a funded fourth entrant changes the *count* of suppliers in
commodity DRAM, with no evidence yet that it changes the *count* in HBM, and no dated capacity figure
in either product. The capacity-clock (M7) should record CXMT as **a note, not a fourth ticker-dated
row** — consistent with the premortem's own registry-edit proposal (`capacity_clock` field, for a
human).

### (d) Weak-number tags (C2/C3)

- **7.7% (or ~8%, Counterpoint) share is a 2025 figure.** Not current; both estimates are trailing by
  at least six months relative to this write.
- **+719% Q1 YoY is one quarter off a small base** (¥50.8bn on what was presumably a much smaller
  prior-year quarter, itself not disclosed here — `[blank]`). A single quarter's YoY off a low base
  is not a run-rate.
- **The H1 ¥110–120bn figure is a company expectation stated in a prospectus, not a print.**
  Prospectus forward guidance from the issuer raising the money is the single weakest-grade forecast
  category this desk handles — it should carry the same skepticism as any management guidance ahead
  of an IPO roadshow, arguably more.

---

## §2 · The STX contradiction — strongest revision book, most extreme margin percentile, one ticker

**Revision book, pulled fresh this run** (`module_fundamentals_us STX`, 2026-07-27):

| Horizon | current | 90d ago | 90d Δ | 30d breadth (↑:↓) |
|---|---|---|---|---|
| Current-quarter | 5.09 | 3.90 | **+30.6%** | 3↑ : 0↓ |
| Next-quarter | 5.87 | 4.42 | **+32.5%** | 4↑ : 0↓ |
| This-year | 14.89 | 13.12 | +13.5% | 3↑ : **1↓** |
| Next-year | 28.48 | 20.59 | **+38.3%** | 5↑ : 0↓ |

Last-quarter revenue **$3.11bn, +44.1% YoY** — confirmed against SEC XBRL cross-check (4/4 quarters
agree within 5%). ⚠ **The mandate's "0 downward revisions in 30 days" holds for current- and
next-quarter, and next-year — it does NOT hold for this-year, which carries the leg's only
downgrade (1↓/30d).** Carry both halves (C2): the book is exceptionally clean but not perfectly
clean.

**Margin (SEC XBRL, `scripts/margin_history.py STX`, 17-year annual series FY2009–2025):**

| | value |
|---|---|
| FY2025 gross margin | **35.2%** |
| Percentile of 17-year series | **100th** (series max) |
| Prior annual peak (FY2012) | 31.4% |
| Median of series | 27.7% |
| Latest reported quarter GM | 46.5% (per prior-run pull) |

**+15.1pp "above its own prior peak"** is the **latest quarter's 46.5%** measured against the
**annual** FY2012 peak of 31.4% — a quarterly-vs-annual mix (flagged honestly, not smoothed over,
C2). On a like-for-like annual basis the move is smaller (35.2% vs 31.4% = +3.8pp) but **still the
series max in 17 years and three completed cycles** (the series contains FY2012 and FY2016 troughs
and at least two full up-cycles before this one) — either way you cut it, **this is the top of the
series, not a mid-cycle read.**

**Forward multiple, fresh pull today**: 28.37× forward P/E (trailing 76.5×, P/S 16.6×). Live price
today (2026-07-27, unsettled) is $808, down from Friday's settled $851.69 close (SECTOR_FLOW_US.json)
— a ~5% intraday move that coincides with the CXMT IPO news hitting the whole memory/storage
complex (the same news search shows MU −6.99% and SK hynix −8.81% quoted intraday today). **This is
a live, low-volume, unsettled number and is cited for context only — not as an RS or flow reading**
(the run-clock warning applies here as much as anywhere: today's tape is 8.6%-of-normal volume).

**Settled flow (07-24, benchmark SPY): STX flow −0.103 / RS20 −17.6 / RS60 +43.3 / vol_surge 1.19.**
**STX prints 2026-07-29. Implied ±14.6% (expiry 07-31, D4, from this run's BLINDSPOT_PREMORTEM §5
`module_flow --positioning` pull), skew −5.8 (negative = the option market pays up for upside),
P/C 1.58.** ⚠ Any STX move inside ±14.6% on the print is **pre-declared no-information.**

**L2 verdict**: **CONFIRMED — the hardest-confirmed peak-margin case in the leg**, and it sits
alongside — not resolved by — the cleanest revision book. **A multiple without a margin percentile
is not a valuation; here both exist, and 28–30× forward is not the discount that usually accompanies
a name already at its own 17-year record.** The revision book says the Street believes the earnings
keep compounding through next year; the margin series says that compounding is happening from the
statistical top of three completed cycles. Both can be true simultaneously and often are, right up
until the cycle turns — which is precisely why this is flagged as a DEEP contradiction rather than
resolved into a directional call (P4: no verdict beyond this is offered).

---

## §3 · S30 — the supplier leg's 20-day reversal, DELL/HPE as control

**Frozen observable (registered this run in BLINDSPOT_PREMORTEM S30)**: median RS20 vs SPY of
{STX, MU, WDC}, settled closes. **Frozen threshold**: crosses above 0 by 2026-08-05 ⇒ branch A (the
60-day run was pausing, not topping; M149 falsified). **Current (07-24 settled)**:

| | RS20 vs SPY | RS60 vs SPY |
|---|---|---|
| STX | −17.6 | +43.3 |
| MU | −24.7 | +78.8 |
| WDC | −23.7 | +29.1 |
| **median** | **−23.7** | — |

**Control pair inside the bracket — the only two names whose 60-day excess sits in days 21–60 rather
than the last 20**: **DELL RS20 +6.2 / RS60 +108.6** and **HPE RS20 +1.4 / RS60 +66.8**.

**M149 (share of the 60-day excess earned in the LAST 20 sessions, negative = the last 20 SUBTRACTED
from the 60-day stock)**: MU −31.5% · SNDK −99.7% · WDC −81.9% · AMAT −55.3% · MRVL −139.1% ·
LRCX −141.2%, against **DELL +5.9% and HPE +2.2%.** ⇒ the memory/equipment complex is giving back a
stock of old excess right now; DELL and HPE are not — their excess was built in days 21–60 and has
neither continued nor reversed in the last 20. **An A-grade signal must also be live; six of eight
names in this leg currently are not.**

**Eight dated expiries** as the days-21-to-60 segment rolls out of each 60-day window: **SNDK
07-31 · MRVL 08-19 · LRCX 08-20 · WDC/STX 08-21 · MU 08-25 · DELL 08-26 · HPE 08-27 · KLAC 09-02 ·
AMAT 09-07.** Median of the memory/equipment cluster ≈ 08-20/21; DELL and HPE sit at the far end
because their excess is spread, not concentrated.

**HPE — the pre-mortem's "most likely wrongly avoided" name, re-verified this run:**
`module_fundamentals_us HPE` (fresh, 2026-07-27) shows **17↑:0↓ current-quarter, 17↑:0↓ next-quarter,
19↑:0↓ this-year, 17↑:0↓ next-year (all 30d)** — unanimity on all four horizons, matching the
premortem's characterization exactly, and the only such unanimity anywhere in this leg. Against
that: **RS20 vs SPY +1.4 — indistinguishable from the benchmark (C4: "indistinguishable," not
"rejected").** Forward P/E **11.82×** (fresh pull). **`scripts/margin_history.py HPE` returns a
6-year annual series, FY2013–2018 only** (78.5% → 54.4%, "peak" FY2013, "trough" FY2018) — this is
the **pre-2015-spinoff** HPE (Enterprise Services still consolidated), a fundamentally different
business mix from the post-reorg three-segment HPE reporting today. **It cannot be used as a margin
percentile for the current entity, and I am not inventing one.** ⇒ **the "cheap on 11.8× forward"
observation stands flagged, not concluded** — L2 forbids calling it cheap without a comparable
percentile, and none exists in this dataset. HPE prints **2026-09-04**, outside every window this
file can see; its RS60 defence expires **08-27**.

**M140 (carried, do not average HPE and DELL)**: five-quarter gross margin **HPE 28.4% → 36.5%
(+8.1pp)** vs **DELL 21.1% → 17.8% (−3.3pp)**, on revenue +40% and +87.5% YoY respectively. **HPE's
Cloud AI segment grew revenue +22.9%** (barely AI-server volume) while **DELL's ISG grew +181%**
(**AI-optimized servers $16.1bn vs $1.9bn = +757% YoY**). Roughly half of HPE's margin lift is
Juniper networking mix, and that lift's own QoQ rate has decelerated to **+0.6pp** — the mix
anniversaries out. DELL's ISG gross margin fell **−12.6pp** while ISG **operating** margin still
**expanded +0.86pp** (opex 22.0% → 8.5% of segment revenue) — an operating-leverage engine
absorbing a gross-margin hit, not the same shape as HPE's mix-driven lift. **Both print 2026-09-04,
outside every current window** — nothing here resolves before then.

**M141 — a second, independent route into C1**: **DELL's 10-Q MD&A** names *"substantial inflation
in memory component costs"*; **HPE's** names a *"worldwide shortage in memory components."* The OEM
gross-margin line is therefore a public, dated read-through of the memory node's private LTA terms.
**First reads land 2026-07-28 (CLS) and 2026-07-29 (FLEX)** — neither name is in `us_top300`, so the
desk must pull them manually; neither is DELL or HPE (both print 09-04).

---

## §4 · Excluded by name — the security/observability node

**This node is EXCLUDED from any blanket IT verdict.** RS60 vs SPY, all positive RS20 (settled
07-24): **DDOG +83.8 (RS20 +11.1) · PANW +75.1 (RS20 +9.8) · FTNT +73.9 (RS20 +1.0) · CRWD +57.3
(RS20 +7.4)** — the four cleanest live instances of the desk's only A-grade verified signal (RS
vs SPY, both windows positive simultaneously).

Revision pulls (30d, per premortem lens fan-out, not independently re-pulled this run — carried):
**DDOG 37↑:0↓ current-qtr · PANW 40↑:1↓ (but next-qtr flips to 1↑:4↓) · FTNT 38–40↑:0↓ across three
horizons yet mean target sits 13.8% BELOW spot with 28 Hold vs 11 Buy · CRWD 29↑:11↓ = the most
downgrades of any name reviewed** in this leg — and that is exactly the axis its ledger row was
filed on.

**FTNT prints 2026-07-30, implied ±13.0%, P/C 2.85.** ⚠ **C5 stays unresolved and must stay
unresolved**: this node pairs the desk's strongest measured momentum signal with its weakest
measured valuation discipline (a mean target below spot despite a clean-to-perfect revision book,
on FTNT), and **this repo has never built a valuation factor** — there is no tool here that can
adjudicate "is 28 Hold vs 11 Buy at a below-spot target right, or is the revision book right." Both
readings are stated; neither is resolved.

---

## §5 · W4 — name the node's customers, check disclosed spend

The assembly/memory/security legs above all sell into (or protect) the same buyers. **MSFT prints
2026-07-29, META 07-29, AMZN 07-30 — per one provider; `yfinance`'s own calendar disagrees (MSFT
07-30, META 07-30, AMZN 07-31).** ⚠ Write on **windows**, not a single day, given the provider
dispute.

**Carried capex facts**: hyperscaler 2026 capex **>$800B** consensus. **Alphabet raised FY26 capex
guidance $180–190B → $195–205B** (this run's own S1-bracket firing, STANDING_VIEW "S1 FIRED-A" —
n≈1, one guidance event, not a trend). **GOOGL Q2 capex +100.1% YoY with free cash flow −$5.86bn,
funded by a $49.6bn equity raise** (M134) — the desk's own standing read is that the data-centre
node's live sensitivity is **cost of capital** (HY OAS), not the AI narrative itself. **None of
this was re-verified live this run — it is carried from the 07-24/07-25 record and stated as
such.** The three largest prints of the window (MSFT/META/AMZN) all have straddles that **expire
before their own events** (M89, replicated a fifth time per the premortem) — there is no admissible
price threshold for any of the three; any read on them at print time will be written on
capex/margin disclosure language, not price.

---

## §6 · Value chain, left → right, binding constraint marked

| # | Node | Named tickers | State |
|---|---|---|---|
| 1 | **Memory / HBM / NAND (+ new entrant)** | MU · SNDK · WDC · STX · *(Samsung, SK hynix, unlisted)* **· CXMT (unlisted, no clean US expression)** | ★★ **BINDING CONSTRAINT** |
| 2 | Wafer-fab equipment | AMAT · LRCX · KLAC · ASML | Serves node 1's 2027+ capacity; not binding today |
| 3 | GPU / custom ASIC | NVDA · AMD · AVGO · MRVL | Allocated, not scarce at the margin |
| 4 | Assembly / OEM | DELL · HPE · SMCI · CLS · FLEX | Price-taker on node 1; margin engines differ (§3, M140) |
| 5 | Networking | ANET · CSCO · HPE (Networking segment) · CIEN · LITE | Margin-rich, re-rating separately |
| 6 | Security / observability | **DDOG · PANW · FTNT · CRWD** | ★ Excluded by name from a blanket IT verdict (§4) |
| 7 | Datacentre shell | DLR · EQIX | Node 4's landlord |
| 8 | Power & cooling | VRT · ETN · GEV · PWR · VST · CEG | Long-lead, negative flow board-wide |

**The binding constraint remains memory**, dated by two primary 10-Q filings (HPE 06-02, DELL
06-09 — carried from the 07-25 DEEP, both cite memory shortage/inflation directly in MD&A) and now
by a fourth supplier whose own numbers (§1) do not yet show it relieving that constraint. CXMT sits
in node 1 as a **capacity-clock note**, not a new row with a clean US-tradeable expression — it
carries a DoD "Chinese Military Company" designation and a pending, not-yet-implemented Entity List
action, so there is no US-book instrument that expresses it directly.

---

## §7 · Sub-node dispersion — is "Information Technology" the right unit? (C8)

**The spread inside the sector dwarfs the sector's own move.** Sector-level: wflow +0.155 / eqflow
−0.206 (a modest, roughly-balanced-sounding pair). Inside it, RS60 vs SPY ranges from **+108.6
(DELL)** to **−8.4 (AVGO, adjacent)** — a spread of **>115 points** inside one GICS sector, and the
20-day flow deltas run from **+0.378 (HPE)** to **−0.412 (AMAT)**, a spread nearly **twice the
sector's own eqflow reading.** **Yes — the sector label is the wrong unit of analysis here, and this
is C8's third measured instance of the same shape** (the same desk has now found this pattern at
least twice before this run, per the 07-25 DEEP's own C8 note on the assembly/OEM leg).

At minimum, four legs sit under one GICS code with opposite or unrelated drivers this run:
1. **Memory/storage** (MU, STX, WDC, SNDK) — RS60 strongly positive, RS20 sharply negative, revision
   books strong-to-unanimous, margins at or near series records. Exhausted-on-the-20-day-window per
   Lens 3 (STX), extended-but-live per the same lens (MU, WDC, SNDK).
2. **Assembly/OEM** (DELL, HPE, SMCI, CLS, FLEX) — the only cell with simultaneously positive 60-day
   excess and improving 20-day flow (DELL, HPE); margin engines run in opposite directions (M140);
   three of five relevant tickers (SMCI, CLS, FLEX) are outside `us_top300` entirely.
3. **Security/observability** (DDOG, PANW, FTNT, CRWD) — cleanest dual-positive RS signal on the
   board, paired with the desk's least-tested valuation question (C5) and, in CRWD's case, the most
   revision downgrades of any name reviewed.
4. **Equipment** (AMAT, LRCX, KLAC) — uniformly 🔴, uniformly negative 20-day flow, but AMAT carries
   the strongest revision book in the entire leg (25–26↑:0↓) while KLAC is the **only name in the
   set with net negative breadth** (current-qtr 0↑:1↓ 7d).

**A blanket "IT Neutral" verdict averages a name whose margin is decompressing under AI-server
volume (DELL) with a name that supplies the shortage causing that decompression (MU) with a name
that has nothing to do with either (FTNT). That average is not a measurement of anything real.**

---

## §8 · Track KPIs and anti-signals, as dated observables

| # | Observable | Date | What it settles | What it does NOT settle |
|---|---|---|---|---|
| K1 | **CLS prints** | **2026-07-28** | First public assembly-margin read in the window since CXMT's IPO; a second, independent route into C1 (M141) | Nothing about CXMT, DELL, or HPE directly — different filer, different node slice |
| K2 | **STX prints** | **2026-07-29** | Whether GM extends past 46.5% (§2); whether the leg's one downgrade (this-year, 1↓/30d) grows. Implied ±14.6%, any move inside that band is no-information | Nothing about DELL/HPE (both print 09-04) or about CXMT's HBM ambitions |
| K3 | **FLEX prints** | **2026-07-29** | Second independent assembly-margin read | — |
| K4 | **FTNT prints** | **2026-07-30** | Whether the unresolved C5 valuation/momentum split (§4) moves; implied ±13.0%, P/C 2.85 | Nothing about DDOG/PANW/CRWD individually |
| K5 | **S30 median RS20 crosses above 0** | by **2026-08-05** | Whether the memory/equipment 20-day reversal was pausing (branch A) or the stock of past excess is genuinely decaying (branch B, M149 confirmed) | Whether DELL/HPE move with it — if not, the event is memory-specific, not IT-beta (§3) |
| K6 | **Eight RS60 arithmetic expiries** | SNDK 07-31 · MRVL 08-19 · LRCX 08-20 · WDC/STX 08-21 · MU 08-25 · DELL 08-26 · HPE 08-27 · KLAC 09-02 · AMAT 09-07 | The date after which IT-Neutral's RS60-based defence cannot be restated on the same numbers, name by name | Flat-forward assumption only — **not a price forecast** |
| K7 | **Issuer-grade CXMT DDR5 price corroboration** | none scheduled — desk must re-search | Whether the 2.2% premium observation graduates from single-source to corroborated, or is refuted | Nothing about server DRAM/HBM pricing, a different product |
| K8 | **CXMT Entity List action** | unscheduled, "approved... not yet implemented" | Whether the one clean US-policy lever on this entrant fires | Whether it fires before or after any capacity actually comes online (`[blank]` on capacity dates) |
| K9 | **DELL / HPE print** | **2026-09-04** (both) | Whether the memory-cost MD&A language (M141) recurs or is walked back — the highest-value single confirmation of C1 available anywhere in this leg | Outside every other window in this file |

**Anti-signals that would break this file's §0 verdicts:**
1. **A downgrade entering STX's current- or next-quarter column** — the cleanest cut against §0②;
   currently 0↓ on both.
2. **A second, independent source corroborating (or refuting) the CXMT 2.2%-premium price
   observation** — moves §0① off single-source grade in either direction.
3. **DELL's or HPE's Δ (20-day flow) turning negative**, or a down-revision entering either book —
   the only axis separating them from the memory/equipment median in S30 (§3).
4. **Any disclosed LTA price floor** (SK hynix/Samsung/AVGO issuer filing, tracked since 07-25,
   target by 2026-08-08) — strengthens node 1's margin case, worsens node 4's cost line
   simultaneously; the two halves of this leg respond to the same disclosure with opposite signs.
5. **A dated CXMT capacity-online figure appearing in a primary source** — currently `[blank]`
   everywhere; its appearance would let M7 gain a real fourth row instead of a capacity-clock note.

**`[blank]` — the unknown column (C3), carried honestly rather than filled by inference:** CXMT's
capacity-online date; whether CXMT's raise is earmarked for commodity DDR or HBM tooling; whether
Apple's reported CXMT-sourcing approval request has been granted; HPE's current-entity margin
percentile (XBRL only reaches FY2018, pre-spinoff business mix); DELL's and HPE's AI-server gross
margin taken separately from their consolidated segment number.

---

## ✅ EXIT CHECK

- [x] **§0 leads with the three mandated verdicts**, none re-derived as a rotation call — P9/CXMT,
      the STX contradiction, and S30 all stated up front with the deciding numbers named.
- [x] **All RS/OBV/flow numbers sourced from `SECTOR_FLOW_US.json`, asof 07-24 settled** — no
      `module_flow <TKR>` live call used; live price/fundamentals pulls are dated and flagged as
      unsettled where cited (STX's live $808 today, §2).
- [x] **§1** — CXMT corroborated across 5 outlets on the IPO facts; the single load-bearing price
      claim searched against 3 independent terms and found in exactly one outlet — **kept at
      single-source grade, not laundered.** C1/M1 relationship stated as level-not-rate (L1);
      mechanism dated where a date exists, `[blank]` where none does; C2/C3 weak numbers tagged.
- [x] **§2** — STX revision book re-pulled fresh and the "0↓/30d" claim corrected on its one
      exception (this-year 1↓); margin percentile re-pulled from SEC XBRL; the annual-vs-quarterly
      mix in "+15.1pp" stated rather than smoothed; L2 verdict given with both numbers side by side.
- [x] **§3** — S30 observable/threshold reproduced from settled data; DELL/HPE re-verified live
      (HPE's 17-19↑:0↓ unanimity confirmed fresh); HPE's margin gap re-confirmed (XBRL stops
      FY2018, pre-spinoff mix, unusable) — flagged, not concluded (C4); M140/M141 carried with
      attribution, not re-derived.
- [x] **§4** — security/observability explicitly excluded from the blanket verdict; C5 (momentum vs.
      valuation) stated as unresolved and left that way — no valuation tool exists in this repo to
      adjudicate it.
- [x] **§5** — W4 customer-spend check stated on windows given the provider date dispute (C1-style
      naming discipline); S1 in "S1 FIRED-A" and M89's fifth replication both cited as n≈1/no
      admissible threshold, not overinterpreted.
- [x] **§6/§7** — value chain given with the binding constraint named from primary filings; sub-node
      dispersion (W5) measured against the sector's own move and found larger — C8's third instance,
      stated as such, not a new finding claimed.
- [x] **§8** — every KPI dated with what it does and does not settle; anti-signals stated as
      falsifiers of §0, not restated as confidence; `[blank]` bucket kept rather than filled by
      inference (C3).
- [x] **No sizing, no buy/sell language, no `--execute`, no position language anywhere in this file
      (P4).**
