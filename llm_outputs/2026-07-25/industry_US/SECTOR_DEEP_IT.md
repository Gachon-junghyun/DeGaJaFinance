# SECTOR DEEP — INFORMATION TECHNOLOGY · the AI-SERVER HARDWARE LEG

**Asof: 2026-07-24 settled close.** Written 2026-07-25 (Sat, US closed). Benchmark: **SPY** on every
RS number in this file (C1). Flow tags from `SECTOR_FLOW_US.json`, `asof 2026-07-24`. OBV is
**C-grade (D6)**; RS vs SPY is A-grade; revision breadth and FINRA short-volume are B-grade.
**FULL FRESH map — this leg has never had a DEEP file.** Analytical only: no sizing, no buy/sell.

---

## §0 · Verdict — a genuine un-owned node, but it is TWO nodes, and only one of them is the leg

**Verdict: the AI-server hardware leg is a genuine un-owned node, and the promotion was correct — but
"HPE · DELL · STX" is not one node. It is three different businesses that GICS files under one
sub-industry code, and the file's job is to stop them being averaged.**

**The measurement that decides it** is the intersection of two axes that no prior stage crossed.
Inside the 56-name IT sector, **HPE (Δ +0.378, 5th) and DELL (Δ +0.231, 8th) are the only two names
in the sector's top-8 20-day flow deltas that also carry a positive RS60 vs SPY.** Every other
high-delta name in IT is a name whose 60-day excess is negative (NOW +5.3, MSTR −48.5, CRM −13.6,
SHOP −10.6, ACN −21.1, MSI −7.7, INTU −29.8). Every other high-RS60 name in IT carries a negative
delta (MU −0.258, STX −0.259, WDC −0.220, AMAT −0.153, MRVL −0.182). **DELL and HPE occupy the only
cell on the board where a large 60-day excess and improving 20-day money are the same two names.**

An independent B-grade axis agrees and is not derived from price. FINRA Reg SHO daily short-volume,
settled 07-24: **DELL z −1.36 with a 5v5 trend of −4.8 (falling)** and **HPE z +0.76, trend −0.8**,
against **WDC +20.1 ▲, STX +18.5 ▲, SNDK +12.0 ▲** — short pressure is being *built* on the
storage/memory names and *released* on the two OEMs, on the same settled date.

**Why this is not the R9/AXON failure shape.** AXON earned ~98% of its 60-day excess in the last 20
sessions **while its estimate was cut**. Here both halves invert: **DELL earned 5.9% and HPE 2.2% of
their 60-day excess in the last 20 sessions** (reproduced below, my own pull), so the move sits in
days 21–60; and the estimate book is being **raised** — DELL current-quarter **20↑:0↓ over 30 days**,
HPE **17↑:0↓**. R9's shape is *price up, estimate cut*; this is *price consolidating, estimate up*.

**But the node splits, and the split is the finding.** STX belongs with DELL/HPE on no axis measured
here — flow delta, short trend, or margin engine (§4, §6) — and HPE, on its own segment note, is
**barely in AI-server volume at all** (§4). What survives as a genuinely un-owned assembly node is
**DELL, plus two assemblers the desk's universe cannot see (§2, §7).**

---

## §1 · The stale-RS60 correction — reproduced, and given a date

I recomputed the decomposition myself from adjusted closes (yfinance, 101 sessions, last bar
2026-07-24), excess = name total return minus SPY total return over the same sessions. It reproduces
the pre-mortem exactly.

| | RS60 vs SPY | last-20 excess | days 21–60 excess | % of RS60 earned in last 20 | off own 60d high |
|---|---|---|---|---|---|
| MU | +78.6 | −24.7 | +137.2 | **−31.5%** | −24.1% |
| SNDK | +39.2 | −39.1 | +129.5 | **−99.7%** | −38.5% |
| WDC | +28.9 | −23.7 | +69.3 | **−81.9%** | −30.3% |
| AMAT | +36.8 | −20.4 | +72.1 | **−55.3%** | −25.8% |
| MRVL | +22.7 | −31.6 | +80.1 | **−139.1%** | −38.6% |
| LRCX | +17.5 | −24.7 | +56.6 | **−141.2%** | −29.6% |
| **DELL** | **+108.7** | **+6.4** | +95.4 | **+5.9%** | −6.0% |
| **HPE** | **+67.0** | **+1.4** | +64.2 | **+2.2%** | −14.8% |
| STX | +43.1 | −17.6 | +73.8 | **−40.8%** | −22.1% |

**What this does to `SECTOR_ROTATION.md`.** ROTATION declined **IT N→UW** on rule D6, holding that
C-grade OBV reds may not override "A-grade RS60 of +78.8 / +39.5 / +36.9 / +29.1 / +22.9 / +17.7."
**The verdict stands; the stated reason does not.** All six of those readings are a *stock* of excess
earned more than 20 sessions ago and currently being given back. A signal whose entire content is
historical and whose current increment is negative is not a live A-grade reading — D6 protects the
*grade* of an axis, not the *staleness* of a number carried on it. What actually carries the decline
to hold at Neutral is the **revision book**, a B-grade fundamental axis ROTATION never cites: MU
**25↑:0↓ (30d), 24↑:1↓ (7d)**; AMAT **25↑:0↓ (30d), 26↑:0↓ (7d)**.

**The expiry, now dated rather than approximated.** Holding forward excess flat (the name tracks
SPY), I rolled the window forward and solved for the first session at which each RS60 crosses zero:

`SNDK 2026-07-31 · MRVL 08-19 · LRCX 08-20 · WDC 08-21 · STX 08-21 · MU 08-25 · KLAC 09-02 · AMAT 09-07`

**Median of the six ROTATION names: 2026-08-20/21.** "Mid-August" is right at the median and wrong at
both tails — SNDK's defence expires in **four sessions**, AMAT's survives six more weeks. ⚠ This is
an arithmetic property of a rolling window under a flat-forward assumption, **not a forecast**; any
actual excess in either direction moves it. For contrast, **DELL 08-26 and HPE 08-27** sit at the far
end because their excess is spread through days 21–60 rather than concentrated in one burst.

---

## §2 · Player map — large-cap ∪ thematic (bar: named ≥2× in the sector's news window, real ticker, mcap ≥ ~$2B)

⚠ **Data hygiene**: `SECTOR_FLOW_US.json` market caps disagree with a fresh yfinance pull by 10–52%
on five names (SNDK 323.5 vs 212.7 · MU 1278.8 vs 1040.1 · WDC 257.2 vs 179.2 · STX 242.1 vs 192.7 ·
DELL 264.6 vs 282.7). Fresh pull used for the bar.

| Ticker | mcap | Node | In `us_top300`? | RS60 | Δ (20d flow) | Next print |
|---|---|---|---|---|---|---|
| **DELL** | $283B | AI-server assembly (ISG) | yes | +108.7 | +0.231 | **2026-09-04** |
| **HPE** | $63B | networking + server/storage | yes | +67.0 | +0.378 | **2026-09-04** |
| **STX** | $193B | HDD / nearline storage | yes | +43.1 | −0.259 | **2026-07-29** ⚠ |
| WDC | $179B | HDD / nearline storage | yes | +28.9 | −0.220 | 2026-08-06 |
| SNDK | $213B | NAND | yes | +39.2 | −0.128 | 2026-08-06 |
| MU | $1,040B | DRAM / HBM / NAND | yes | +78.6 | −0.258 | 2026-09-24 |
| **SMCI** | **$19.5B** | **pure AI-server assembly** | ★ **NO** | +6.4 | *(no row)* | **2026-08-12** |
| **CLS** | **$35.1B** | **EMS / AI rack assembly** | ★ **NO** | −19.7 | *(no row)* | ★ **2026-07-28** |
| **FLEX** | **$43.4B** | **EMS / power + rack** | ★ **NO** | +31.9 | *(no row)* | ★ **2026-07-29** |
| **NTAP** | **$32.9B** | **enterprise storage / AI data** | ★ **NO** | +51.3 | *(no row)* | 2026-09-03 |
| HPQ | $23.5B | PC / print (the non-AI half of the old HP) | ★ NO | *(n/a)* | *(no row)* | 2026-08-27 |
| ANET | $219B | datacentre switching | yes | +1.2 | −0.249 | 2026-08-05 |
| VRT | $111B | datacentre power & cooling | yes | −8.9 | −0.253 | 2026-07-29 |
| NVDA | $5,103B | GPU | yes | −7.0 | +0.034 | *(not in window)* |
| AVGO | $1,957B | custom ASIC / networking silicon | yes | −8.4 | −0.053 | *(not in window)* |

★★ **Five of the eleven most relevant hardware names are absent from `us_top300`, so no stage of this
desk can see them** — including **SMCI, the single most news-named AI-server company in the window**,
and **CLS (07-28) and FLEX (07-29), which print INSIDE the window.** This is a universe-coverage
defect, not an alpha finding, and it is the reason the node reads as "un-owned": the desk's universe
literally omits the pure plays.

---

## §3 · Value chain, left → right, with the binding constraint marked

| # | Node | Named tickers | State |
|---|---|---|---|
| 1 | **Memory / HBM / NAND** | MU · SNDK · WDC · STX *(+Samsung, SK hynix, unlisted here)* | ★★ **BINDING CONSTRAINT** |
| 2 | Wafer-fab equipment | AMAT · LRCX · KLAC · ASML | Serving node 1's 2027 capacity; not binding today |
| 3 | GPU / custom ASIC | NVDA · AMD · AVGO · MRVL | Allocated, not scarce at the margin |
| 4 | **Assembly / OEM** | **DELL · HPE · SMCI · CLS · FLEX** | ★ The node this file maps — **price-taker on node 1** |
| 5 | Networking | ANET · CSCO · **HPE (Networking segment)** · CIEN · LITE | Margin-rich, separately re-rating |
| 6 | Datacentre shell | DLR · EQIX | Node 4's landlord |
| 7 | Power & cooling | VRT · ETN · GEV · PWR · VST · CEG | Long-lead, negative flow across the board |

**The binding constraint is memory, and both OEMs say so in their own 10-Q — primary, not inferred.**
HPE (filed 2026-06-02, period 2026-04-30) discloses a *"worldwide shortage in memory components"*
expected to continue *"in the medium term."* DELL (filed 2026-06-09, period 2026-05-01) discloses
that memory-capacity limits have produced *"substantial inflation in memory component costs."*

**Strong demand is not a bottleneck; a supply limit that lands in someone's cost line is.** Node 4's
gross margin is where it lands (§4). New DRAM capacity is dated **mid-2027 at the earliest** (M7), so
node 1 stays binding through the whole of the window this file can see.

---

## §4 · The HPE-vs-DELL split, from the segment notes — do not collapse them

Both consolidated five-quarter series in the brief reproduce from yfinance and cross-check 4/4 against
SEC XBRL revenue: **HPE gross margin 28.4 → 29.2 → 33.5 → 35.9 → 36.5% (+8.1pp)** with operating
margin **3.9 → 7.7%**; **DELL 21.1 → 18.3 → 20.7 → 20.2 → 17.8% (−3.3pp)** with operating margin
**5.3 → 8.6%**. ⚠ Note the second half of the DELL line, which the brief omits: **its operating
margin ROSE +3.3pp over the same five quarters in which its gross margin fell 3.3pp.**

**The segment notes explain both, and they do not say what "opposite margin engines" implies.**

**HPE** reorganised into **three** segments effective FY26 Q1 (Networking · Cloud AI · Corporate) —
the five-segment description still carried in yfinance's business summary is stale. Q ended
2026-04-30 vs prior year, from Note 2:

| HPE segment | Revenue | YoY | Gross margin | Operating margin |
|---|---|---|---|---|
| **Networking** | $2,690M | **+148%** (Juniper) | **61.1% → 60.7%** | 25.0% → 21.6% |
| **Cloud AI** (server + storage + fin. services) | $7,707M | **+22.9%** | **24.1% → 29.0%** | **6.6% → 12.4%** |

**DELL**, Note 15, quarter ended 2026-05-01 vs prior year:

| DELL segment / line | Revenue | YoY | Gross margin | Operating margin |
|---|---|---|---|---|
| **ISG** (servers + networking + storage) | $29,009M | **+181%** | **31.7% → 19.1%** | 9.7% → **10.5%** |
| — of which **AI-optimized servers** | **$16,132M** | **+757%** | *(not disclosed separately)* | — |
| — traditional servers & networking | $8,543M | +92% | — | — |
| — storage | $4,334M | **+8.5%** | — | — |
| CSG (PCs) | $14,609M | +16.8% | — | 5.2% → 8.0% |

**★ The correction the brief's framing needs.** "Same layer, second vendor" is wrong — but so is a
simple "opposite margins" read. **HPE's server node grew +22.9% while DELL's grew +181%: HPE is
barely in AI-server volume at all.** Roughly half of HPE's +8.1pp consolidated lift is a *mix*
artifact — Networking went from 14.2% to 25.2% of revenue at a ~61% gross margin — and the other half
is genuine Cloud AI expansion (+4.9pp) earned precisely by **not** chasing that volume. DELL took it,
paid **−12.6pp of ISG gross margin**, and recovered it below the gross line: ISG opex fell from 22.0%
to 8.5% of segment revenue, so ISG operating margin still expanded +0.86pp.

**So: DELL is an operating-leverage engine whose unit economics are deteriorating at the gross line;
HPE is a mix-and-price engine with small AI-server exposure whose lift is largely an acquisition.**
Not two vendors of one thing. HPE's 10-K names **Juniper integration** as a live Item 1A risk, and
the quarter shows its cost — intangible amortization $323M vs $37M, R&D +71% YoY.

**L1 applied to the margin engines themselves** (QoQ change in gross margin, pp, five quarters):
**HPE +0.8 → +4.3 → +2.4 → +0.6** — the rate of HPE's margin expansion has decelerated for two
consecutive quarters and the last quarter added 0.6pp. The Juniper mix lift anniversaries out. **DELL
−2.8 → +2.4 → −0.5 → −2.4** — no trend, oscillation around a downward drift.

---

## §5 · The $950bn LTA and contradiction C1

**Source grade: `[news — Reuters citing ROK presidential adviser Kim Yong-beom; NOT an issuer
disclosure]`.** Thread BUILDING 3 days, outlets 3 → 2 → 6; `fts "950 billion" --scope foreign
--days 3` returns 5 matches — four the same wire re-carried, one an unrelated tariff story.
**No price term, ASP, floor or escalator appears anywhere in the body.** The content is volume: SK
hynix ≈$750bn to US buyers incl. NVIDIA "through long-term agreements"; Samsung ≈$200bn to Broadcom;
a separate SK hynix programme >$500bn; SKT's 2-GW facility on Vera Rubin + HBM4, phase 1 **2027**.

**What it can and cannot do to the regime call.** STANDING_VIEW §4 is exact and this does not touch
it: *a capex CUT changes the thesis, a RAISE only moves its timing.* A volume commitment signed **by
the buyers who also sign the price caps** confirms the volume leg and leaves **M1** (server-DRAM
contract price, +90~95% → +58~63% → **+13~18% QoQ**) untouched. It is another volume confirm on a
question whose disputed variable was never volume. **The regime call is unmoved.**

**Where it becomes newly measurable — and this is what this leg adds.** C1 asks whether LTA price
floors hold margin. The desk has carried it as *unmeasured* because the contracts are private. **But
node 4's cost line is a public read-through of node 1's price terms.** DELL has now put memory-cost
inflation into its own MD&A as the named driver, and its ISG gross margin fell 12.6pp in the quarter
that happened. **The OEM gross margin is therefore an observable proxy for whether memory ASPs are
being passed through, absorbed, or capped** — one that prints on a schedule, from filers who have no
incentive to flatter node 1. C1 does not become *resolved*; it becomes **measurable from a second
direction**, and the first reads land 07-28/07-29 (CLS, FLEX), not 09-04.

⚠ **Anti-signal, stated in advance**: if a disclosed price term shows hard floors, that *strengthens*
the memory-margin thesis and *weakens* node 4's cost outlook. The two halves of this leg respond to
the same disclosure with opposite signs. Track KPI stays as EVENT_ALPHA set it: **an issuer filing
(SK hynix DART / Samsung DART / AVGO 8-K) by 2026-08-08**, not a wire.

---

## §6 · L2 applied name-by-name, honestly (`scripts/margin_history.py`, SEC XBRL)

| | own-history gross-margin percentile | vs own prior peak | fwd P/E | revision trend | L2 verdict |
|---|---|---|---|---|---|
| **MU** | latest quarter **84.6%**; 17y annual series FY09–25, peak **FY2018 58.9%**, median 32.0%, two negative years | **+25.7pp** | **5.99×** | +1y **+52.9%/90d**, 25↑:0↓ | ★ **CONFIRMED** — canonical |
| **STX** | latest quarter **46.5%**; 17y series FY09–25, peak **FY2012 31.4%**, FY25 **35.2% = 100th pct**, median 27.7% | **+15.1pp** | **29.91×** | +1y +38.3%/90d; ⚠ **CY 3↑:1↓ — the only ↓ in the leg** | ★★ **CONFIRMED, and the series is long enough to mean it** (3 full cycles) |
| **WDC** | FY25 **38.8%** = 100th pct of a **9-year** series (FY17–25), prior peak **FY2018 37.3%** | **+1.5pp** | **28.03×** | +1y +30.2%/90d | **NOT a low-multiple-on-peak-margin trap** — barely above peak, and at 28× it is not cheap on forward either. Pre-mortem confirmed |
| **SNDK** | FY25 30.1% on a **3-year** post-spin series (FY23–25: 7.1 → 16.1 → 30.1), **monotonic, no cycle** | **undefined** | 6.75× | +1y +86.2%/90d | ★ **UNMEASURABLE, not confirmed** (C3/C5). Keep the unknown column |

⚠ **Measurement caveat to carry**: M18's "+25.7pp over its own prior peak" compares a **quarterly**
84.6% against an **annual** peak of 58.9%. Directionally sound — no MU quarter in the series
approached 84.6% — but not like-for-like, and the same mixing makes STX's headline number look milder
than it is (annual FY25 35.2% vs quarterly 46.5%).

**L1, second derivative, on the price-cycle nodes** (QoQ revenue rate · QoQ gross-margin change in
pp, five quarters through each name's latest reported period):

| | revenue QoQ rate | gross margin ΔQoQ (pp) | reading |
|---|---|---|---|
| **MU** | +21.6 → +20.6 → +74.9 → **+73.8** | +7.0 → +11.3 → +18.4 → **+10.2** | ★ **the margin rate turned down** — first deceleration, corroborating M1 at company level |
| **SNDK** | +11.8 → +21.6 → +30.7 → **+97.0** | +3.7 → +3.6 → +21.1 → **+27.5** | both still accelerating — no turn yet |
| **STX** | +13.0 → +7.8 → +7.6 → **+9.9** | +2.2 → +2.0 → +2.2 → **+4.9** | ★ **flat volume, accelerating price** — the purest ASP-only shape in the leg |
| **WDC** | +13.5 → +8.5 → +7.1 → **+10.6** | +1.2 → +2.5 → +2.2 → **+4.5** | same shape as STX |

**The honest reading of STX**: its ~8–10% QoQ revenue against +4.9pp of margin in a single quarter is
almost entirely price, on a 17-year series that has three completed cycles in it and is now at its
own top. That is the L2 signature at full strength, and STX's 29.9× forward is **not** the cheap
multiple that usually accompanies it — which cuts both ways and is why the verdict here is
"confirmed", not "peaked". **STX is a price-cycle node wearing the same GICS code as DELL. It is not
part of the assembly leg.**

---

## §7 · Chain-hop candidates — body-proximate only

`chain-hop "AI server" --scope foreign --days 7` (191 articles scanned). ⚠ **DELL (5 title / 34 body)
and HPE (3 / 15) are HEADLINE-NAMED**, which settles the correction in §9.

Title-count 0 with ≥2 proximate body co-mentions: **AVGO (4 prox / 17 body)** · **MRVL (3 / 7)** ·
**VRT (2 / 2)** · AMZN (6 / 33) · META (3 / 30) · T · MS · LMT · RTX · PGR · MMM · ADBE.

| Candidate | Why it surfaced | Flow cross-check (07-24 settled) | Status |
|---|---|---|---|
| **AVGO** | named counterparty of Samsung's $200bn leg | 🟡 · RS20 +0.2 · **RS60 −8.4** · Δ −0.053 | **The flow is not in it.** Fails |
| **MRVL** | custom-silicon alternative | 🟡 · RS20 **−31.6** · RS60 +22.7 · Δ −0.182 | Stale-RS60 shape (§1, −139.1%). Fails |
| **VRT** | rack power & cooling | 🔴 · flow −0.911 · RS20 −11.4 · **RS60 −8.9** · Δ −0.253 | Fails on every axis |
| AMZN · META | co-mention as **customers**, not suppliers | — | Correctly classified as node-4 demand (W4) |

**No chain-hop candidate clears a flow cross-check. None may reach BET.** The names that *would*
matter — **SMCI, CLS, FLEX, NTAP** — cannot appear in this table at all: `chain-hop` maps onto
`us_top300`, and all four are outside it. **The gap is in the universe, not in the news.**

---

## §8 · Track KPIs and anti-signals, as dated observables

| # | Observable | Date | What it settles | What it does NOT settle |
|---|---|---|---|---|
| K1 | **CLS prints** | **2026-07-28** | First public read on **AI-rack assembly gross margin** in this window. CLS is a pure contract assembler — its margin is node 4's cost pass-through with no networking mix to hide it | Nothing about DELL's own mix; CLS is not in the universe, so the desk must pull it manually |
| K2 | **STX prints** | **2026-07-29** (⚠ one news body says 07-28 — **conflict carried, not resolved**) | Whether HDD gross margin extends past **46.5%**, i.e. whether the +4.9pp QoQ rate held a second quarter. Settles the **L1 rate**, and STX's **1↓** current-year revision | ★ **It settles nothing about DELL or HPE.** Different node, different constraint, and both OEMs print **2026-09-04** — outside every window this run can see |
| K3 | **FLEX prints** | **2026-07-29** | Second independent assembly-margin read, one day after CLS | — |
| K4 | **Issuer disclosure of the $950bn LTA** | by **2026-08-08** | Whether the wire becomes `[primary]`, and whether any **price term** is disclosed (C1) | Volume confirmation alone does not move M1 or STANDING_VIEW §4 |
| K5 | **RS60 arithmetic expiry** | SNDK **07-31** · MRVL 08-19 · LRCX 08-20 · WDC/STX **08-21** · MU 08-25 · DELL 08-26 · HPE 08-27 · KLAC 09-02 · AMAT 09-07 | The date after which ROTATION's RS60-based defence of IT-Neutral cannot be restated on the same numbers | Flat-forward assumption only — **not a price forecast** |
| K6 | **SMCI prints** | **2026-08-12** | Whether the reported record **$60B backlog** and doubled gross margin `[news, not yet checked against a filing]` show up in a 10-Q. SMCI's last *filed* quarter shows GM **9.9%** | ⚠ Anti-signal already live: despite +13%/+20% single-day pops, SMCI is **−40.0% off its own 60-day high with RS20 −5.6 vs SPY**. **One-day moves are n≈1 (S1)** |
| K7 | ANET 08-05 · WDC/SNDK 08-06 · HPQ 08-27 | as dated | Adjacent nodes | — |

**Anti-signals that would break this file's §0 verdict:**
1. **Any down-revision entering DELL's or HPE's current-quarter column.** Both are 30d **20↑:0↓** and
   **17↑:0↓** with zero downs; a single ↓ is the cheapest available falsifier.
2. **DELL's Δ or HPE's Δ turning negative** on a subsequent flow run — the delta is the *only* axis
   separating them from the six stale-RS60 names, and it is a 20-day statistic.
3. **A disclosed LTA price floor** — strengthens node 1, worsens node 4's cost line (§5).
4. **HPE's Networking mix anniversarying** — the QoQ margin lift is already down to **+0.6pp**.
5. ⚠ **A correction the desk must carry forward**: the brief's "current-year EPS +60.9% / +64.9% over
   90 days" for HPE/DELL is the **current-QUARTER** figure. Current-year is **+41.2% / +42.3%**.
   Likewise DELL's **20↑:0↓** is current-quarter; its next-year book is **4↑:0↓**. Both corrected
   here against a fresh `module_fundamentals_us` pull.

**`[blank]` — the unknown column (C3):** DELL does not disclose AI-server gross margin separately;
HPE does not break Cloud AI into server vs storage; neither discloses a backlog figure in the 10-Q
text pulled here; and STX's true print date is `[blank — provider conflict, 07-28 vs 07-29]`.

---

## §9 · Corrections this file carries out of the run

1. **EVENT_ALPHA Card 1's "un-named, in no thread title this week" is refuted at the article level.**
   `fts --scope foreign --days 7` returns **DELL 181 · STX 110 · HPE 58** matches, incl. *"Dell
   Technologies (DELL) Climbs 9.3% on Booming Demand for Nvidia-Powered AI Servers"* [07-23] and
   *"Hewlett Packard Enterprise: Networking Is Now The Profit Engine, And Nobody Repriced It"*
   [07-21]; `chain-hop` independently classifies both as **headline-named**. **The leg is
   UN-THREADED, not undiscovered — the clustering tool missed it. That is a tool finding, not an
   alpha finding**, and must not be re-used as evidence of non-crowding.
2. **The prior US IT DEEP files (07-11 / 12 / 13 / 15 / 23) never analysed this node** — DELL and HPE
   appear only as table rows tagged *"server/AI infra beneficiary, not a spender"* (07-23), with no
   segment work, no margin history, no customer check. **Zero-coverage verified, not assumed.**
3. **C8 gains a fourth leg.** IT is carried as one label over three legs (spenders / suppliers /
   security). The segment notes show a **fourth**: assembly/OEM, whose margin moves *inverse* to the
   suppliers' because it buys their output. A blanket IT verdict shorts a node that is long the same
   shortage the suppliers are short.

---

## ✅ EXIT CHECK

- [x] **§0 verdict first**, deciding measurement named, R9/AXON contrast stated on **both** halves
      (excess timing and revision direction, both inverted).
- [x] **§1 decomposition reproduced independently** from adjusted closes vs **SPY**; ROTATION's
      **verdict stands, reason replaced**; expiry given as **eight dated crossings, median
      2026-08-20/21**, flat-forward assumption stated.
- [x] **§2** player map at the stated bar; **five absent names flagged as a universe defect**, not an
      alpha claim.
- [x] **§3** 7 nodes left→right, binding constraint **memory** from **two primary 10-Q filings**.
- [x] **§4 W5** taken from **SEC segment notes**, not consolidated ratios; the brief's framing
      corrected in both directions. **Not collapsed.**
- [x] **§5** source graded `[news, not issuer]`; STANDING_VIEW §4 applied unchanged; **C1 given a new
      measurement direction without being declared resolved**; two-sided anti-signal stated (L3).
- [x] **§6 L2 name-by-name** on each name's own SEC XBRL series — **MU confirmed · STX confirmed ·
      WDC not a trap · SNDK UNMEASURABLE (C3/C5)** — plus **L1 rate tables** kept separate from levels.
- [x] **§7** body-proximate only; **all candidates fail the flow cross-check; none reaches BET.**
- [x] **§8** dated observables with what each does **not** settle; STX date conflict carried both
      ways; `[blank]` where unknown; **S1 applied to SMCI's one-day moves**.
- [x] **D6** — no OBV-derived claim carries a verdict here; verdicts rest on RS vs SPY (A) or
      revision breadth / FINRA short-volume / segment filings (B). Nothing from **STANDING_VIEW §5**
      cited as evidence.
- [x] **No sizing, no buy/sell language, no `--execute`.**
