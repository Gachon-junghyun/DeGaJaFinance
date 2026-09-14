# BET_SHEET — industry_US — 2026-07-27 (Mon)

> Stage 8/10. ONE file, per-sector sections (downstream desks glob this exact filename — never split).
> Flow/RS `asof` **2026-07-24 settled**, benchmark **SPY** inline (C1). Options data pulled **07-27**.
> **Zero buy/sell recommendations, zero position sizing (P4).** Sizing language, where it appears at
> all, is influence illustration only. Freshness tags in §B are **ALPHA's** to fill.

## ★ Read this before any number below

**No US session has occurred since the prior US run.** Every price-derived figure is the 07-24 settled
close. **The 07-27 intraday tape is inadmissible** — the sweep's first pass was run on it and had to be
re-run (SWEEP §0, dig **D74**). Options and filings *are* fresh.

★★ **And the run's two most decision-relevant findings both invert an inherited framing:**
1. **The refiners are NOT at peak margin.** Fresh SEC XBRL this run: **MPC FY25 gross margin 10.0% =
   37.5th percentile of its own 8 years · PSX 12.3% = 60th percentile of its own 10 years.** Neither is
   near a peak. **L2, as usually stated, does not describe this sector** — the low forward multiple
   comes from the FY26→FY27 consensus cliff, not from a peaking denominator.
2. **UPS is cheap next to a margin TROUGH, not a peak.** **FY25 operating margin 8.9% = ~21st
   percentile of 19 years; Q1'26 6.0% = ~11th percentile.** The carried framing *"the only cheap name
   is the only one the money is not in"* should read **cheap-and-depressed**, not cheap-and-euphoric —
   which changes what its 07-28 print would falsify.

---

# §A · ENERGY (OW−) — the numbers

| | VLO | MPC | PSX | XOM |
|---|---|---|---|---|
| flow_score | +0.583 | +0.611 | **+0.644** | +0.667 |
| tag | 🟡 | 🟡 | 🟡 | **🟢** |
| RS20 vs SPY | +18.0 | **+21.3** | +19.8 | +13.5 |
| RS60 vs SPY | +22.1 | **+29.1** | +21.4 | **+0.4** |
| **days 21–60 excess** | **+4.1** | **+7.8** | +1.6 | **−13.1** |
| last-20 share of 60d | 81.4% | **73.2%** | 92.5% | >100% |
| FY26→FY27 consensus cliff | **−31.6%** | −25.8% | **−7.2%** | −4.7% |
| gross-margin percentile (own history) | **`[blank]` — see below** | **37.5th (8y)** | **60th (10y)** | — |
| implied move | **±5.4%** (exp 07-31, D4) | — | — | — |
| FINRA 07-24 (short% / base20 / z) | 41.9 / 42.5 / −0.10 ✅in band | 46.6 / **55.1** / −1.15 ❌**suppressed** | 41.8 / 40.2 / **+13.8▲ 5v5** ✅in band | 38.5 / 40.9 / −0.32 ✅in band |

⚠ **VLO's margin percentile is a `[blank]`, and it is a structural blank, not a skipped flag.**
`margin_history.py VLO` returns *"연간 데이터 없음"* for a **third consecutive run (D56)**, and the
DEEP agent attempted the quarterly-XBRL route this run rather than repeating the gap uncommented:
`RevenueFromContractWithCustomerIncludingAssessedTax` against `CostsAndExpenses` matches **only 2
quarters (2017-03, 2017-06)** before the tag pairing breaks. **No percentile invented.**
⚠ **VLO's `risk_factors` field came back EMPTY for a third consecutive run (D54)** — the anti-signal
source the protocol designates is unavailable on this name, and that is stated rather than read as
*"this filer discloses no risks."*

## §B · ENERGY — thesis lines *(freshness tag: ALPHA fills)*

**The sector's verdict this run is a branch, and it is scored on the last bar that CAN be scored.**
On the **07-24 settled** close, **both S8 branch-B conditions hold** (crude fell −3.1% WTI / −3.9%
Brent; distillate crack **86.275 ≥ 84**) and **neither branch-A condition holds** (3-2-1 crack 64.304
is **4.30 pts** from the <60 kill line; distillate is **6.28 pts** from <80). ⇒ **a GASOLINE event with
the distillate bottleneck INTACT — input-cost relief, NOT against the tilt.**
⚠ **The 07-27 intraday tape (crack 61.665, distillate 85.614) narrows the distance on both legs but
crosses neither.** It is an observation, not a score; the frozen line settles after 16:00 ET today.

★ **The decomposition is the run's new content, and it splits the sector in two.**
**Every integrated / E&P / services name carries a NEGATIVE days-21–60 excess vs SPY (XOM −13.1,
CVX −12.9, COP −19.5, OXY −17.4, SLB −19.5, BKR −19.1)** — before the last 20 sessions they were net
*underperforming* SPY, so their entire RS60 reading is a pure last-20-day event with no standing base.
**All three refiners are positive (VLO +4.1, MPC +7.8, PSX +1.6)** — smaller than their 20-day reading,
but never negative. ⇒ **the war-premium signature sits on the integrated leg, and the base sits under
the refining leg.** This is **S31**'s exact subject (registered this run, settles 2026-08-05).

⚠⚠ **M146's epicenter mismatch replicates a THIRD time and now has a numeric edge**: the book's only
held Energy name is **XOM (0% refining, days 21–60 −13.1)**; the registry's human-locked `core_pick` is
**PSX (unheld)**; and the LIVE shortlist surfaces **XOM again** because the refiners are 🟡, blocked by
a volume gate — **a filter artifact, not weak flow.** **Three instruments, one blind spot.**

## §C · ENERGY — flow / positioning cross-read

**PSX carries the set's only material short build on an in-band baseline (5v5 +13.8▲)** and prints
**last (08-05)**. **MPC's z is suppressed** — its 55.1% baseline sits 10pp above the tool's own
40–45% band (D52/D73). VLO and XOM are neutral and readable.

## §D · ENERGY — peers / competition
Refining trio = **ONE risk unit** (SPY-residual ρ **+0.878**, MPC–VLO). Integrated/E&P is a separate
leg whose 60-day base is absent. **Midstream (KMI +0.099, WMB −0.491) is a third thing again.**

## §E · ENERGY — refutation + dated catalysts

- **Kill (restated on ONE axis):** a **settled 3-2-1 crack below 60**, regardless of crude. Distance on
  the last settled close: **4.30 points** — the closest of the entire advance.
- **Second kill, from the DEEP:** the **distillate crack breaking below 80** (6.28 pts away) — that is
  the bottleneck itself going, not a gasoline event.
- **Physical counter-evidence accumulating, three items**: **Singapore stocks rose — and the DEEP found
  it is NOT purely a bunker-fuel story (middle distillates rose too)**, making it a **second, broader**
  hub inversion after Fujairah's +35%; **Russia's diesel export ban EXPIRES 2026-07-31**; **India on
  track for 1.55M bpd of July distillate exports vs 866k in May.** ⚠ **D59 stays a lead, not evidence**
  — the *"India Hikes Diesel and Jet Fuel Export Tax"* headline is still unconfirmed in a body.
- ⚠ **A supplied premise was CORRECTED by the DEEP agent**: this run's MACRO cited *"Novorossiysk
  resumed crude loadings"*; **the freshest body the agent found reports the terminal offline on 07-27.**
  **Flagged, not resolved** — recorded here so the correction is not lost (the D48 discipline).
- **Dated**: **VLO 07-30** (±5.4%, D4 — ⚠ **any move inside ±5.4% is pre-declared no-information**) ·
  **STNG 07-30 (S21)** · **XOM 07-31 (contaminates S31's own observable — declared at registration)** ·
  **Russian ban expiry 07-31** · **MPC 08-04** · **PSX 08-05**.
- **W4 — customers**: DAL **+67%** and UAL **+84%** fuel costs YoY, verified from primary Q2 releases
  this run; **both carry 🔴 flow tags**, and **FDX joins them 🔴**. **UPS is the 5th and prints
  tomorrow.**

---

# §A · FINANCIALS (OW−) — the numbers

| | CB | TRV | JPM | MA | V | SCHW | GS |
|---|---|---|---|---|---|---|---|
| flow_score | **+0.900** | +0.806 | +0.579 | +0.617 | +0.569 | +0.606 | −0.071 |
| tag | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟡 | 🟡 |
| RS20 vs SPY | +8.1 | **+21.0** | +4.8 | +9.7 | +7.0 | +13.4 | −1.0 |
| RS60 vs SPY | +5.1 | +21.1 | +9.6 | **+2.5** | +11.2 | +8.4 | +10.7 |
| **last-20 share of 60d** | **158.8%** | 99.5% | 50.0% | **388.0%** | 62.5% | — | — |
| vol_surge | **1.42** | 1.25 | 0.83 | 0.68 | 0.64 | 0.89 | 0.75 |
| implied move | — | — | — | **±4.7%** (07-31, D4) | — | — | — |

## §B · FINANCIALS — thesis lines *(freshness: ALPHA)*

★★ **The OW's surviving leg is weaker than the headline number, in two separate layers.**
**Layer 1, mechanical and it is most of the gap**: **BRK-B is $1,055.7B = 13.94% of the sector's cap
(larger than JPM) at a flow score of +0.012 — effectively flat.** Dropping that one name cuts the
eqflow−wflow gap **56% (+0.064 → +0.028)**. **Most of "cap-weighted money is behind while breadth is
ahead" is one enormous flow-flat holding company diluting the cap-weighted side.**
**Layer 2, real but narrow**: after removing it, **payments+insurance (16 of 47 names) still carries
46.8% of gross positive flow at 1.55× the sector mean and holds 4 of the 5 green tags**, while
**capital markets nets to flat (+0.009 — reproducing carried M40's +0.005)** and **all three red tags
sit in banks / brokers / consumer finance.** ⇒ **the breadth is real inside one sub-node, not
sector-wide.** ⚠ **C5 satisfied**: the alternative (native 12-way GICS) grouping was run and **does not
dissolve the finding — it sharpens it** (the five best sub-industries carry zero reds; the four worst
carry all three).

★ **M150's exhaustion geometry, decomposed for all five greens rather than TRV alone** — and it
reclassifies two of them: **TRV 99.5%** (a steady late-window run, reproducing M150's 98.6%) ·
**JPM 50.0%** (roughly linear) · **V 62.5%** · **CB 158.8%** and **MA 388.0%** — the last two are
**V-shaped reversals**, where the last 20 sessions erased an SPY-relative deficit rather than extended
a lead. **CB's is dated and explained (Q2 printed 07-22; CY EPS 26.98 → 27.56, +2.1%/90d) — an n≈1
earnings event. MA's is not**: it does not report until **07-30**, and its own book is **flat to
slightly down (current-quarter 4.85 → 4.78, −1.6%/90d; current-year +0.3%)**.

## §C · FINANCIALS — flow / positioning
**S23 is 0.14pp away.** **T10Y2Y is +0.34 against the ≤+0.20 trigger, with DGS2 at 4.37% — inside the
4.15–4.45% band the bracket requires.** Deposit-funded banks (16 names) show weak flow and no estimate
momentum ⇒ still curve-exposed. **IB & brokerage (5 names) already re-rated on RS60 with strong GS/JPM
books, but their 20-day flow has gone flat-to-negative** ⇒ the migration to markets revenue is priced
and now fading, not extending.

## §D · FINANCIALS — peers
**MA/V is a DIFFERENT SPY-residual unit from JPM/TRV/CB** (MA–JPM +0.238, TRV–MA +0.382) — an MA miss
does not read across to the OW's other survivors. **CB (β 0.125) and TRV (β 0.339) are the OW's hidden
internal hedge, and it is the only tilt on the board that carries one.**

## §E · FINANCIALS — refutation + dated catalysts
- **The exchanges node's replacement observable has NOT moved and that is itself the finding**:
  equal-weight excess of {NDAQ, SPGI, ICE, CME, MCO, MSCI, COIN} vs SPY was **−3.00pp** at
  registration and **`asof` is still 07-24 — no settled close exists yet.** **Reported as unchanged
  rather than fabricated.** ⚠ The *registered* RS60 test remains **BROKEN, not passed** (M135: on
  frozen prices it reports CONFIRM and cannot report falsify). **SPGI prints 07-28, ICE 07-30.**
- ⚠ **MA is RE-FILED, not rejected.** Its measured flow still passes (🟢 +0.617), so per the
  475150 precedent it is not removed on a narrative. **New, lower-conviction thesis line: "the
  least-supported of the five green tags — a near-4× concentration of trailing excess into 20 sessions,
  on a flat book, with the print still ahead of it."** ⚠ **S14-num's frozen band is ±3.9% and stands as
  written; today's straddle reads ±4.7%. Any MA move inside ±3.9% is pre-declared no-information and
  may NOT be read as confirming the FIN OW.** **Re-check: 2026-07-30.**
- **Dated**: **FOMC 07-29** (S19 hike / S23 flattener / S9 dovish) · **V 07-29** · **MA 07-30** ·
  **June PCE 07-30** · **SPGI 07-28 · ICE 07-30**.
- ⚠ **R11 must not resurface**: the bear-steepener framing is retracted; **the OW's steepener leg is
  gone and breadth — layer-2 narrow — is all that is left.**

---

# §A · INDUSTRIALS (OW−) — the numbers

| | UNP | CSX | NSC | UPS | LMT | RTX | NOC | GD | LHX |
|---|---|---|---|---|---|---|---|---|---|
| flow_score | **+0.867** | +0.856 | +0.767 | +0.360 | +0.856 | +0.792 | +0.744 | +0.661 | +0.283 |
| tag | 🟢 | 🟢 | 🟡 | 🟡 | 🟢 | 🟢 | 🟢 | 🟡 | 🟡 |
| RS20 vs SPY | +14.2 | +11.6 | +11.7 | +4.4 | +14.7 | +13.4 | +8.0 | +11.6 | +3.4 |
| RS60 vs SPY | +11.0 | +13.9 | +6.9 | +6.6 | +9.9 | **+17.3** | **−10.0** | **+19.5** | **−11.4** |
| vol_surge | 1.36 | 1.34 | 1.18 | 0.91 | 1.34 | 1.10 | 1.23 | 0.99 | 1.12 |
| fwd multiple | 21.9× | 23.3× | 25.0× | **14.25×** | — | — | — | — | — |
| **margin percentile (own history)** | — | — | — | **~21st (FY25) / ~11th (Q1'26), 19y** | — | — | — | — | — |
| implied move | — | — | — | **±6.8%** (07-31, D4) | — | — | — | — | — |

## §B · INDUSTRIALS — thesis lines *(freshness: ALPHA)*

★★ **"Industrials" is THREE sectors and the split is measured STABLE, not a snapshot.** Defense primes
**+0.667 mean flow, 3🟢/0🔴, 11.3% of cap** · rails/freight **+0.368, 2🟢/1🔴, 9.9%** · capital goods
+ everything else **−0.193, 0🟢/16🔴, 78.8% of cap.** **Spread 0.860 against a sector mean of −0.040 —
21× the sector's own move (W5 satisfied: the label is the wrong unit).**
⚠ **M36's caution was applied, not cited**: dropping the single biggest mover on each side (LMT, VRT)
leaves the spread at **0.795**, still above M26's original 0.705; a median-based cut is **wider still
(1.045)**. ⇒ **The spread did not decay — the desk was comparing the wrong two nodes for one session.**
★ One honest exception so "0 green in capital goods" is not over-read: **CTAS carries the sector's best
RS20 (+21.1 vs SPY) but stays 🟡** on `vol_surge` 1.02 — it fails the 3-axis green test (M25), not the
strength test.

★★ **UPS's cheap multiple sits next to a margin TROUGH.** FY25 operating margin **8.9% = ~21st
percentile of 19 years**; **Q1'26 6.0% = ~11th percentile** (only FY2007 and FY2012 lower). **This is
the inverse of the desk's recurring peak-denominator trap.** It changes what tomorrow's branches mean:
a **fuel-led** guide-down is consistent with a business still working through a trough; a **volume-led**
cut says the trough has further to go.

★ **Defense W4 closed 3 of 5 from primary sources.** **NOC's own 8-K: record backlog $104.7bn,
book-to-bill 1.83×, and its 10-K's #1 risk bullet names single-customer (US Government) dependence
verbatim — the exact opposite of AXON's defect (R9).** RTX and LMT were closed by S7 ($289bn and a
record $230.4bn). **GD is genuinely partial** (68% USG revenue, backlog $130.8bn — Q1 data; prints
**07-29**). **LHX is unmet.**

## §C · INDUSTRIALS — flow / positioning
⚠⚠ **The positioning axis is UNREADABLE on the two names that decide tomorrow.** FINRA 07-24:
**UPS short 52.0% on a 57.7% baseline (z −1.12)** and **UNP 31.8% on a 52.2% baseline (z −2.41)** —
**both baselines sit 7–13pp outside the tool's own 40–45% band, so both verdict strings are
SUPPRESSED** (D52/D73). Readable: **CSX 37.7/35.9, z +0.18, 5v5 −10.2▼** · **NSC 48.0/42.6, z +0.78**.
★ **New and dated**: **UPS's skew compressed +11.1 (07-25) → +1.6 (today)** while short interest and
DTC ticked up — a real shift toward complacency **on the desk's own registered falsifier**, with
**P/C 0.34.**

## §D · INDUSTRIALS — peers / cross-sector chains
★ **The rail node IS the Energy bet through a different income statement (M91)**: ~8 of UNP's 12
revenue growth points are **fuel surcharge**; CSX intermodal +26% revenue on +9% volume, RPU +16%, in
the company's own words *"driven by fuel surcharge."* ⇒ **UNP is double-hit on S20 branch B** — a
volume cut plus a rolling crack is one shock counted twice.
★ **Second cross-sector chain: DAL and UAL sit in the capital-goods 🔴 bucket** — the refiners' own
customers, sold on flow while their fuel bill runs **+67% / +84% YoY**.
★ **Third: AI→power→transformers→copper runs through GEV, PWR and VRT — all three 🔴 here.**
**`chain-hop` on the defense theme returned ZERO flow-passing candidates** — recorded as a null result.

## §E · INDUSTRIALS — refutation + dated catalysts
- **S20 + S20-ANNEX fire TOMORROW (07-28).** Frozen observable: **median RS20 vs SPY of {CSX, UNP, NSC}
  turns negative by 2026-08-04.** It currently reads **+11.7, unmoved in sign.**
  ⚠ **Any UPS same-day move inside ±6.9% is pre-declared no-information** (today's straddle: ±6.8%).
- ⚠ **D51 still contaminates the flow numbers and the DEEP says so plainly**: CSX filed its 8-K Item
  2.02 on **07-22** and UNP/NSC on **07-23**, 0–1 sessions before the flow snapshot. **The flow score,
  OBV state and volume surge ARE the event.**
- **LHX FILED to the ledger** (`A.flow미도착`; revives-if = a primary backlog read with b:b > 1.0 **and**
  RS60 vs SPY turning positive; recheck **2026-08-12**) — the one prime whose W4 is unmet, on the
  node's worst RS60 (−11.4 vs SPY).
- **Dated**: **UPS 07-28** · **GD 07-29** · **LHX 07-30**.

---

# §A · INFORMATION TECHNOLOGY (N — a PREMORTEM promotion, not a flow slot)

| | STX | MU | WDC | DELL | HPE | DDOG | PANW | FTNT | CRWD |
|---|---|---|---|---|---|---|---|---|---|
| flow_score | −0.103 | −0.350 | −0.192 | +0.353 | −0.247 | +0.478 | +0.357 | −0.228 | +0.197 |
| tag | 🟡 | 🔴 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 | 🟡 |
| RS20 vs SPY | **−17.6** | **−24.7** | −23.7 | +6.2 | +1.4 | +11.1 | +9.8 | +1.0 | +7.4 |
| RS60 vs SPY | **+43.3** | **+78.8** | +29.1 | **+108.6** | +66.8 | +83.8 | +75.1 | +73.9 | +57.3 |
| last-20 share of 60d (M149) | — | **−31.5%** | **−81.9%** | **+5.9%** | **+2.2%** | — | — | — | — |
| revision book (30d ↑:↓) | 3:0 / 4:0 / **3:1** / 5:0 | 25:0 · FY 29:0 | 1–4:0 | **20–23:0** | **17–19:0 all four** | 37:0 | 40:1 (next-q **1:4**) | 38–40:0 | **29:11** |
| margin percentile | **100th of 17y** | 100th of 17y | +1.5pp over own peak | not at peak | **`[blank]` — XBRL stops FY2018** | — | — | GM 80.5 ≈ FY24 peak 80.6 | — |
| implied move | **±14.6%** (07-31, D4, skew −5.8) | — | — | — | — | — | — | **±13.0%** (D4, P/C 2.85) | — |

## §B · IT — thesis lines *(freshness: ALPHA)*

★★★ **P9 / CXMT — the capacity clock gained a fourth name, and the one price observation available
points the OTHER way.** The IPO is **cross-confirmed across five outlets** (economictimes, AP, fortune,
SCMP, AFP): **$8.6bn raised explicitly for capacity, $487bn market cap, world's #4 DRAM producer at
~7.7–8% share (a 2025 figure), no HBM presence, no dated capacity-online figure anywhere — `[blank]`,
not guessed.** Against that, the single number on its own pricing says **CXMT modules sell at a 2.2%
PREMIUM to Big-Three modules on JD.com**.
⚠ **The DEEP agent searched three independent terms (RDIMM, JD.com, the cited handle) and found that
price observation in EXACTLY ONE outlet. It is kept at single-source grade and is NOT laundered into a
desk fact.** ⇒ **New evidence on C1 leaning toward "floors hold," at single-source strength.**
Under **L1** this is a **level/funding fact, not a rate fact — it does not touch M1.**

★★ **STX — the strongest revision book and the most extreme margin percentile are on one ticker, and
both are now verified.** Book: current-quarter **+30.6%**, next-quarter **+32.5%**, next-year **+38.3%**
over 90 days. ⚠ **A correction to this run's own mandate**: the *"0 downward revisions in 30 days"* is
true for current-quarter, next-quarter and next-year — **it is NOT true for this-year, which carries the
leg's only downgrade (3↑:1↓).** Both halves carried (C2). Margin: **FY25 GM 35.2% = the 100th
percentile of a 17-year, three-cycle series** at 28–30× forward. ⚠ **A second correction to the
mandate**: the carried *"+15.1pp above its own prior peak"* mixed a **quarterly** 46.5% against an
**annual** FY2012 peak of 31.4%. **Like-for-like annual it is +3.8pp — still the series max in 17
years, but the carried figure overstated it 4×.** **L2 verdict: CONFIRMED — not a trap, and not cheap.**

★ **S30's control pair holds.** **DELL RS20 +6.2 / HPE +1.4 vs a memory median of −23.7.** The
supplier leg's 20-day reversal has **not** touched the two OEM names whose 60-day excess sits in days
21–60. **If the memory median crosses above 0 by 08-05 while DELL/HPE do not, it is a memory-specific
event, not IT beta** — the discrimination S30 exists to make.
★ **HPE remains the board's best-documented "flagged, not concluded" name**: **17–19 analysts up and
ZERO down on all four horizons** — the only such unanimity in a 24-name set — with **RS20 +1.4,
indistinguishable from SPY.** ⚠ **Its margin percentile is unobtainable (XBRL stops at FY2018,
pre-spin mix), and L2 forbids calling anything cheap without one. Flagged, not concluded.**

## §C · IT — flow / positioning
**The sector's flow does not support the slot and the file says so**: wflow +0.155 against **eqflow
−0.206**, **25 🔴 / 4 🟢 of 56 — the board's worst breadth.** The promotion is on information content.

## §D · IT — peers / dispersion (C8, third instance)
**RS60 vs SPY inside one label spans >115 points** (DELL +108.6 → ORCL −34.5). **The spread dwarfs the
sector's own move ⇒ "Information Technology" is the wrong unit of analysis.**
⚠ **The security/observability node is EXCLUDED BY NAME from any blanket IT verdict** — DDOG +83.8,
PANW +75.1, FTNT +73.9, CRWD +57.3 vs SPY, all with positive RS20, are the four cleanest instances of
the desk's only A-grade verified signal. ⚠ **C5 stays unresolved and deliberately so**: this repo has
**never measured a valuation factor**, so gating them on 46–122× multiples would let an unmeasured axis
veto a measured one. **CRWD's 29↑:11↓ book is the exception, and it is exactly the axis its existing
ledger row was filed on** (recheck 09-02).

## §E · IT — refutation + dated catalysts
- **Kill on P9**: an **actual Entity-List designation** (the capacity money then cannot be spent), **or**
  a **second independent source showing CXMT modules at a DISCOUNT** — which would reopen the bear branch.
- **Kill on the IT-Neutral defence**: it **expires arithmetically on eight dated crossings** —
  **SNDK 07-31 · MRVL 08-19 · LRCX 08-20 · WDC/STX 08-21 · MU 08-25 · DELL 08-26 · HPE 08-27 ·
  KLAC 09-02 · AMAT 09-07.**
- **Dated**: **MSFT/META 07-29 · AMZN 07-30 · STX 07-29 · FTNT 07-30** ⚠ (provider dispute D5 — every
  bracket is written on a window, not a day) · **DELL and HPE both 09-04, outside every window** ·
  **CLS 07-28 / FLEX 07-29** are the first public read-through of memory cost into an OEM gross margin
  (M141) **and neither is in `us_top300`.**

---

# §F · CROSS-SECTOR LIVE SHORTLIST — names outside the four DEEP sectors

`US_LIVE_SHORTLIST.json` (mcap ≥ $10B ∧ 🟢 ∧ top-15 by flow, `asof 07-24`). Seven names sit outside the
DEEP set. **None is dropped silently.**

| Ticker | Sector | flow / RS20 / RS60 vs SPY | Disposition |
|---|---|---|---|
| **PLD** | Real Estate | +0.706 / +4.4 / +0.5, `vol_surge` **1.34**, `new_green` | **Carried.** RE's only 🟢 and the **only event-free control in S25**. ⚠ Flow and fundamentals point opposite ways: frozen **0↑:0↓** book, negative revisions on 3 of 4 periods, +6.9% to target near a 52-week high |
| **PCG** | Utilities | +0.68 / +3.9 / +6.0, `vol_surge` 1.33, `new_green` | **Carried.** The **regulated** leg being bought while the AI-power leg is sold, 9.89× forward, +28.7% to target. ⚠ **1↑:5↓ (7d) book and no print until 2026-10-22** — it is an S23/S19-branch-D rip name with no catalyst of its own |
| **TMO · JNJ** | Health Care | +0.88 / +11.7 · +0.69 / +6.9 | **Carried as the C7 test, not as candidates.** C7's resolving observable is **one 🟢 from outside the top-6 by cap — still zero of 26.** ⚠ TMO's **120-day excess is −8.9 vs SPY**: a 20-day re-rate off a flat base. Horizon **08-06** |
| **T** | Comm Services | **+0.96** — the shortlist's #1 flow / +7.0 / — | **Carried with an explicit caveat.** ⚠ **`T` is one of the 28 tickers `module_report_tags` silently CANNOT index (M152/D65)** — its ledger coverage reads 0 and that is a tool artifact, not a gap. No desk thesis exists on it; **first-claim for a future run** |
| **AAPL** | Info Tech | +0.662 / **+20.4** / +19.2, OBV +0.49 | **Carried.** The strongest two-window agreement in IT and **the only IT name with no thesis attached in any desk file** — an unowned coverage gap of exactly the shape that surfaced 009150 |
| **PLTR** | Info Tech | +0.629 / +14.0 / **−16.8** | **Carried, low conviction.** RS20 strong and RS60 deeply negative — the mirror image of the memory complex's geometry, i.e. a name with no 60-day base |

---

# §G · EPICENTER-STARTER MODULE — 🚨 the rank-1 cycle GAP

**Per the standing rule, a partial core in the #1 cycle's epicenter belongs on this sheet regardless of
tape; the tape gates only the remainder.** `../CYCLE_EXPOSURE.md`:

| Cycle | rank | epicenter % | floor | **margin_pp** | Flag |
|---|---|---|---|---|---|
| **AI-compute / semiconductors** | 1 | **8.55%** | 12.0% | **−3.447pp** | 🚨 **GAP — outside D61's 0.5pp band, so it is real, not borderline** |
| Energy / oil-refining | 2 | 8.03% | 8.0% | **+0.027pp** | ⚠ **UNRESOLVED, not a pass** (inside the 0.5pp band) |
| Missile-defense | 3 | 7.53% | — | — | ⚪ ungated by design |

★★ **M146 completes on its sixth run**: with the held set (**AVGO, NVDA, TSM**) **unchanged**, the
AI-compute margin ran **−0.001 → +0.252 → +0.254 → +0.136 → +0.011 → −3.447pp. Nothing was bought or
sold — the flag moves on mark-to-market drift alone.**
★ **The book holds the label, not the engine**: **AVGO RS60 −8.3 and NVDA −6.8 vs SPY**, while the
bucket's movers run away — **DELL +108.6 · MU +78.8 · HPE +66.8 · AMD +57.7 · AMAT +36.9.**
**Cleanest epicenter expressions by the numbers**: **MU (+78.8)** and **AMAT (+36.9)**, both
epicenter-layer. ⚠ **Both carry deeply negative RS20 (−24.7 / −20.4 vs SPY) — that gates TIMING, not
existence.** ⚠⚠ **And the honest tension this sheet must not hide: MU is simultaneously the desk's
L2-confirmed peak-margin case (GM 84.6% = 100th percentile of 17 years, with the margin RATE now
decelerating +18.4 → +10.2pp).** The GAP is a **coverage measurement**; it is not a recommendation, and
these two facts are presented together rather than one being suppressed (P4).
✅ **D62 CLOSED this run**: `CYCLE_EXPOSURE.json` carries `[AVGO, NVDA, TSM]` on **all six dates
07-21 → 07-27** from a live read-only KIS account call, while `RISK_UNITS.json` shows **TSM 14× on
07-22 and 0× on 07-24/07-25 — and AVGO, indisputably held, also drops to 0× on 07-25.** ⇒ **RISK_UNITS
is a correlation utility whose universe churns with data availability, not a position record.
cycle_exposure is authoritative. The 12.01% figure it was blocking is unblocked.**

---

# §H · Ledger actions this run

| Ticker | Class | Basis (measured axis) | revives-if | recheck |
|---|---|---|---|---|
| **PWR** | `A.flow미도착` | EVENT_ALPHA Card 4: flow **−0.872 = 2nd worst of 300**, OBV −0.25, RS20 −13.5 vs SPY, `vol_surge` 0.63 — an S24 2nd-tier name with the narrative building and the money absent | flow turns positive ∧ RS20 vs SPY > 0, **or** S24 branch B fires | **08-12** |
| **LHX** | `A.flow미도착` | DEEP-INDU: the one prime whose **W4 is UNMET**, on the node's worst **RS60 −11.4 vs SPY** | a primary backlog read with b:b > 1.0 ∧ RS60 vs SPY turning positive | **08-12** |
| **BKR** | `A.flow미도착` | DEEP-ENRG: the **only negative flow score** among 11 Energy names (−0.085), **RS60 −19.2** and days-21–60 **−19.1pp**, with no exposure to the refining mechanism the tilt rests on | flow ∧ RS20 vs SPY both turn positive, **or** an upstream capex read gives services its own driver | **08-14** |

**Re-filed rather than rejected (measured flow still passes — the 475150 precedent):**
**MA** (§E-FIN) — new thesis line + re-check **07-30**. **Tanker complex** (STNG/FRO/INSW/DHT/TNK) —
unmeasurable, not negative; **outside `us_top300` entirely**, re-check **08-06** via S21.
**Every set-aside above carries BOTH `--revives-if` and `--recheck-date`; the script does not permit
otherwise.** Ledger state after this run: **57 rows · 12 resolved · 0 due · 12 legacy** (legacy trend
**21 → 19 → 18 → 12**, and every legacy row is KR-owned).

---

## ✅ EXIT CHECK

- [x] **Every DEEP sector has a section** (§ENRG · §FIN · §INDU · §IT), and the **cross-sector LIVE
      shortlist names are all accounted for in §F — none dropped silently.**
- [x] **Numbers cross-checked**: the DEEP agents independently reproduced the crack series to three
      decimals from raw yfinance closes, the Financials wflow to the third decimal from raw
      mcap × flow_score, and the Industrials node table from all 50 raw rows. **Blanks are blanks** —
      VLO's margin percentile, HPE's margin percentile and CXMT's capacity date are all `[blank]`
      **with the reason stated**, not filled.
- [x] Flow / positioning cross-read present per candidate, **with FINRA baselines reported and three
      out-of-band verdicts suppressed** (UPS, UNP, MPC — D52/D73).
- [x] **BET_SHEET.md written as ONE file** with per-sector sections.
- [x] **Every set-aside name is in the ledger with a class AND both required fields** (§H);
      **zero rows due**, and no name was set aside on narrative grounds while its measured flow passed
      — **MA and the tankers are re-filed with new thesis lines and dated re-checks, not deleted.**
- [x] **Epicenter-starter module present** (§G) with the 🚨 GAP, its cleanest expressions, the timing
      caveat, and the L2 tension stated rather than suppressed.
- [x] Linter run — result recorded below.
- [x] **Zero buy/sell recommendations, zero position sizing (P4). English-pure.**

---

# §I · ALPHA FRESHNESS GATE — filled by stage 9

> Separates "interesting" from "bettable NOW". Tags follow the **name**, not its sector's turn in the
> rotation, and every one is carried forward in the next run's inheritance packet.

## §I-0 · `theme_age` — ten probes, and the tool's own limit reported with them

`--scope foreign`, hit count printed beside every ratio (**D55/D63**):

| Theme | Verdict | Age (d) | 7d avg | **Accel** | n (90d) |
|---|---|---|---|---|---|
| **CXMT** | 🟡 | **74** | 17.6 | **10.98×** | **187** |
| diesel | 🟡 | ≥90 | 35.6 | 5.59× | 609 |
| backlog | 🟡 | ≥90 | 116.3 | 5.50× | 1,918 |
| freight | 🟡 | ≥90 | 51.0 | 5.10× | 906 |
| insurance | 🟡 | ≥90 | 143.4 | 4.06× | 2,925 |
| refining | 🟡 | ≥90 | 85.6 | 3.82× | 1,999 |
| data center | 🟡 | ≥90 | 357.7 | 3.72× | 7,751 |
| DRAM | 🟡 | **76** | 33.3 | 2.93× | 774 |
| Hormuz | 🟡 | ≥90 | 172.3 | 2.91× | 5,457 |
| rate hike | 🟡 | ≥90 | 101.6 | 2.27× | 3,609 |

⚠⚠ **M112/M154 replicates a FOURTH time: ten probes, every one 🟡ACCELERATING — zero 🟢FRESH, zero
🔴FADING. A gate that never discriminates is not a gate**, and its verdict column is therefore **not
used as a gate anywhere below.** What *is* used is the acceleration ratio read next to its n.
★ **On that axis one theme separates decisively: CXMT at 10.98× is 2.0× the next-highest ratio on the
board, on n=187 — well above the n-floor that made `tower REIT` (17.14× on SEVEN hits) unusable.**
The newest theme by age (74 d) is also the most-accelerating — **and it is the one two prior desk runs
missed while it built from 3 to 16 outlets (D71).**

## §I-1 · Freshness tags — every §B thesis

| Name / thesis | Tag | Evidence label + date | Residual / re-check |
|---|---|---|---|
| **VLO · MPC · PSX** — refining margin | **🟡 PARTIAL** | `[measured]` settled 07-24: **both S8 branch-B legs hold**, crack 4.30 pts from its kill line | **The residual is the settled 07-27 close**, against thresholds frozen pre-outcome. **Re-check 2026-07-28** |
| **XOM** — the book's held Energy name | **🟡 PARTIAL** | `[measured]` 07-24: **days 21–60 excess −13.1 vs SPY** — no base under the 60-day reading | **S31 settles it. Re-check 2026-08-05** |
| **CB** — insurance, front-book | **🟢 LIVE** | `[measured]` 07-24: flow **+0.900** (board's 2nd-highest), **`vol_surge` 1.42 = volume-confirmed**, positive on both windows | ⚠ **158.8% last-20 share, but dated and explained** (Q2 printed 07-22, CY EPS +2.1%/90d) ⇒ n≈1. **Re-check 2026-08-06** |
| **TRV** — insurance | **🟡 PARTIAL**, momentum-only stamp | `[measured]` **99.5% of 60-day excess in the last 20 sessions**, corroborated on FINRA (z +1.41, 5v5 +5.4▲) | **hard-stop required.** Re-check **2026-08-06** |
| **MA** — payments | **🟡 PARTIAL**, lowered conviction | `[measured]` **388% last-20 share on a flat book (−1.6%/90d) with NO print behind it** | **Re-check 2026-07-30** (its print). ⚠ inside ±3.9% = no-information |
| **JPM · V** | **🟡 PARTIAL** | `[measured]` 50.0% / 62.5% last-20 share — **the two most linear of the five greens** | **FOMC 07-29 / V 07-29. Re-check 2026-08-08** |
| **The exchanges node** | **🟡 PARTIAL** | `[measured]` the replacement observable is **unchanged at −3.00pp because no settled close exists yet** — reported, not fabricated | **SPGI 07-28 · ICE 07-30. Re-check 2026-08-07** |
| **UNP · CSX · NSC** — rails | **🟡 PARTIAL**, momentum-only stamp | `[measured]` flow 🟢 and volume-confirmed — ⚠ **but D51 still stands: CSX filed 8-K 07-22, UNP/NSC 07-23, 0–1 sessions before the snapshot. The flow IS the event** | **S20 fires 2026-07-28. Re-check 2026-08-04** |
| **UPS** | **🟢 LIVE** | `[measured]` **margin percentile attached this run: FY25 op margin ~21st / Q1'26 ~11th percentile of 19 years** ⇒ cheap next to a **trough**, not a peak | **Prints 2026-07-28.** The window's only genuinely event-priced straddle, on a complacent book (P/C 0.34) |
| **RTX · LMT** — defense | **🟢 LIVE** | `[measured]` volume-confirmed 🟢 (`vol_surge` 1.10 / 1.34) **with W4 closed via S7** (backlogs $289bn / record $230.4bn) | **Re-check 2026-08-06** |
| **NOC** — defense | **🟢 LIVE** (upgraded this run) | `[measured]` ★ **W4 CLOSED from its own 8-K: record backlog $104.7bn, b:b 1.83×, 10-K #1 risk names USG single-customer dependence** — the opposite of AXON's defect (R9) | ⚠ **RS60 −10.0 vs SPY** — the node's weakest strength axis. Re-check **2026-08-06** |
| **GD** — defense | **🟡 PARTIAL** | `[measured]` W4 **partial** (68% USG revenue, backlog $130.8bn — Q1 data) | **Prints 2026-07-29** |
| **LHX** — defense | **🔴 RESOLVED → DROPPED** | `[measured]` **W4 UNMET; RS60 −11.4 vs SPY, the node's worst** | **Ledger `A.flow미도착`, revives-if + recheck 2026-08-12** |
| **BKR** — oilfield services | **🔴 RESOLVED → DROPPED** | `[measured]` **the only negative flow score of 11 Energy names; RS60 −19.2, days 21–60 −19.1pp** | **Ledger `A.flow미도착`, revives-if + recheck 2026-08-14** |
| **PWR** — AI-power physical layer | **🔴 RESOLVED → DROPPED** | `[measured]` flow **−0.872 = 2nd worst of 300**, RS20 −13.5 vs SPY | **Ledger `A.flow미도착`, revives-if + recheck 2026-08-12** |
| **STX** | **🟡 PARTIAL** | `[measured]` **the strongest revision book and the 100th-percentile margin on one ticker.** ⚠ **two corrections filed to this run's own mandate** (§B-IT) | **Prints 2026-07-29**, inside a ±14.6% no-information band |
| **MU · WDC** | **🟡 PARTIAL**, momentum-only stamp | `[measured]` **RS20 −24.7 / −23.7 vs SPY with RS60 +78.8 / +29.1 — a decaying stock of past excess (M149)** | **S30 settles 2026-08-05.** Defence expires **08-25 / 08-21** |
| **DELL · HPE** | **🟡 PARTIAL** | `[measured]` **the only two names whose 60-day excess sits in days 21–60** (+5.9% / +2.2% last-20 share), on **20–23↑:0↓** and **17–19↑:0↓ on all four horizons** | ⚠ **HPE's margin percentile is `[blank]` (XBRL stops FY2018) and L2 forbids "cheap" without one.** Both print **2026-09-04**, outside every window. Re-check **2026-08-27** (HPE's expiry) |
| **DDOG · PANW · FTNT** — security | **🟡 PARTIAL** | `[measured]` the cleanest instances of the desk's only A-grade signal (RS60 +83.8 / +75.1 / +73.9 vs SPY) | ⚠ **C5 unresolved and deliberately so — this repo has never measured a valuation factor.** FTNT prints **07-30** |
| **CRWD** | **🔴** (already ledgered) | `[measured]` **29↑:11↓ — the most downgrades of any name reviewed**, the exact axis its row was filed on | **Existing ledger row, recheck 2026-09-02** |
| **PLD** | **🟡 PARTIAL** | `[measured]` RE's only 🟢, `vol_surge` 1.34, `new_green` | ⚠ **frozen 0↑:0↓ book**; the only event-free control in **S25**. Re-check **2026-08-08** |
| **PCG** | **🟡 PARTIAL** | `[measured]` Utilities' only 🟢, `new_green`, +28.7% to target | ⚠ **1↑:5↓ (7d) book and NO print until 2026-10-22** — an S23/S19-D rip name with no catalyst of its own |
| **TMO · JNJ** — HLTH | **🟡 PARTIAL** | `[measured]` carried as **C7's test, not as candidates** — the resolving observable (one 🟢 from outside the top-6 by cap) is **still zero of 26** | **Re-check 2026-08-06** |
| **T** | **🟡 PARTIAL** | `[measured]` the shortlist's **#1 flow (+0.96)** and **no desk thesis exists** | ⚠ **`T` is one of 28 tickers `module_report_tags` silently cannot index (M152/D65)** — its 0 coverage is a tool artifact. **First-claim next run** |
| **AAPL** | **🟡 PARTIAL** | `[measured]` **+20.4 RS20 / +19.2 RS60 vs SPY — the strongest two-window agreement in IT**, and **no thesis in any desk file** | **An unowned coverage gap of the shape that surfaced 009150. First-claim next run** |
| **PLTR** | **🟡 PARTIAL**, momentum-only stamp | `[measured]` RS20 +14.0 / **RS60 −16.8 vs SPY** — no 60-day base | hard-stop required. Re-check **2026-08-12** |

## §I-2 · Positioning gate stamps

- ⚡ **Crowded-short is turn-conditional squeeze fuel, never a standalone read**: **WTI 11th COT
  percentile, Nat Gas 11th, UST 10Y 12th, Nasdaq-100 5th** — all stamped context-only, and **COT
  contrarian sits in the REJECTED ledger (D6)**.
- ❌ **Three positioning verdicts SUPPRESSED for out-of-band baselines** (D52/D73): **UPS (57.7%),
  UNP (52.2%), MPC (55.1%)** — including **the two names tomorrow's binary settles on.**
- ✅ **In-band and readable**: CSX, NSC, VLO, XOM, **PSX (5v5 +13.8▲, the set's only material build)**.

## §I-3 · Carry-forward list (independent of next run's DEEP rotation)

**🟢 LIVE**: CB · UPS · RTX · LMT · NOC.
**🟡 PARTIAL with dated re-checks**: VLO/MPC/PSX **07-28** · MA **07-30** · GD **07-29** · STX **07-29** ·
rails **08-04** · XOM **08-05** · MU/WDC **08-05** · exchanges **08-07** · PLD **08-08** · JPM/V **08-08** ·
TRV/CB/TMO/JNJ **08-06** · PLTR **08-12** · DELL/HPE **08-27** · PCG *(no catalyst until 10-22)* ·
T and AAPL *(first-claim, no thesis exists)*.
**🔴 dropped to the ledger this run**: PWR · LHX · BKR — **all three with `--revives-if` and a
`--recheck-date`; the script accepts no other form.**

★ **The rule this section exists to honour**: a tagged name stays tracked even when its sector rotates
out of DEEP. Measured cost of not doing it — **006360 carried an ALPHA tag with +64.40% consensus
upside, its sector rested, nothing tracked it, and it ran +12.3% over the next five sessions, unowned.**

## §I-4 · ACTION_TICKETS

Written to `llm_outputs/2026-07-27/ACTION_TICKETS.md` (script-owned path, one level up):
five both-sides brackets (**S20 · FOMC · CAPEX · S8/S31 · S30 · S14**) plus the **🚨 cycle-GAP
core-starter**. ★ **The core-starter's own finding is arithmetic**: the AI-compute gap is
**−3.447pp × $11,575 = $399**, which is **sub-one-share on both of the cleanest epicenter expressions
(MU $920.95, AMAT $536.25)** ⇒ **the GAP is not currently actionable at this book size, and saying so
is more useful than issuing a ticket.**
