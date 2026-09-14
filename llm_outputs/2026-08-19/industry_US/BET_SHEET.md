# BET_SHEET — industry_US · 2026-08-19 · Stage 9/11 (L1·BET)

> ONE file, per-sector sections. Downstream desks glob this exact filename — never split it.
> **Analytical only. Zero buy/sell recommendation. Sizing language is influence-illustration (P4).**
> Candidate set = (DEEP thesis leaders) ∪ (`us_setup_screener --sector` setups, run this stage for all
> five DEEP sectors) ∪ (`US_LIVE_SHORTLIST.json`). Every name that did not survive to §A/§B is in §G
> with a class, a revival/entry condition and a re-check date — **17 rows filed by this stage**
> (10 rejections + 7 missed); the date's full ledger totals and who wrote the rest are reconciled in §G.

## 0 · Reading rules that bind every number below

**⏱ Clock.** This stage ran **KST 2026-08-19 23:35–00:20 = ET 2026-08-19 10:35–11:20, US cash session
LIVE** (bell was 22:30 KST). PREFLIGHT **G0 revoked right #2** — *"no stage may re-pull prices after
22:30 KST and treat the result as comparable to the sweep."* That rule is obeyed by splitting the
vintage of every column and never subtracting across the split.

| Rule | Applied here |
|---|---|
| **Price vintage is split and labelled** | **Settled 2026-08-18 close**: `flow_score` · tag · `obv_state` · RS20/RS60 · `vol_surge` · two-session Δ (all from `SECTOR_FLOW_US.json`, `asof 2026-08-18`) and FINRA short-vol (`date 2026-08-18`). **Live intraday 2026-08-19**: price · every multiple · target gap · implied move · P/C · short %float · the per-name news-velocity probe. **The two are never compared to each other** |
| **`flow_score` is a 3-axis score** | `vel_axis false · vel_coverage 17.06% · n_axes 3 · scored 299 · dropped_missing_axis 0`. Stated on the same line as any conclusion drawn from it |
| **G1 — sweep news axis is dead** | 🚫 No theme-freshness verdict, no "it went quiet", no sweep velocity anywhere. ★ The **hand probe at 23:5x KST answered on 7 of 7 names** (§C-2), so those readings are cited **with their probe time** and only as corroborant. **A per-name velocity that answered is not a repair of the sweep axis** |
| **G2 — every Δ is TWO sessions** | The `delta` column compares **2026-08-14 → 2026-08-18**, not one session. Any "improved by" in this file carries that window |
| **G3 — flippers** | `CAT` (INDU, 8.7%) · `LIN` (MATR, 24.7%) · `BRK-B` (FIN, 13.9%). No sector-level promotion/demotion is argued from `wflow` for those three, and `CAT`'s own rejection (§G) is written on **name-level** OBV+RS, not on the sector sign |
| **G4 — no single concentration number** | ⚠ Risk units are **250d 11 · 500d 10 · 750d 10**. Any unit statement in this file names its `--days`. No concentration guard is quoted as one number |
| **G5 — universe staleness + `EA`** | `us_top300.csv` is **35 days old** (limit ≤8) ⇒ every sector weight quoted downstream inherits it. **`EA` is unmeasurable for the 7th run** and is a Communication Services name — §D says "not measurable", never "no signal" |
| **G6 — sizing** | `kelly_size --ic` is **not** evidence-backed (accrual ETA ≈76d vs ideal 30 = 2.6×). ⇒ **no size is computed anywhere in this file**, mechanical or otherwise |
| **G7 — dead tools** | `module_chart` and `scripts/margin_history.py` return non-zero `--help`. Neither is cited in this file |
| **Date-clustering (S1)** | `MPC`/`PSX`/`VLO` moved on **the same driver in the same sessions** ⇒ **n≈1, not n=3.** "Three refiners confirm it" is unavailable and is not written |
| **D6 — OBV is grade C** | No OBV reading appears in this file without RS20 or RS60 vs `SPY` in the same sentence |

### 0a · ★★★ NEW THIS STAGE — "the book" is **two different objects**, and five of fourteen names live in only one of them

⚠ **Credit where it is due: `D288`, registered earlier in this same run, already named this** — *"`G5`
must read the same book the exposure gate reads, or print both and diff them"*, with the five-name diff
and the balance gap. **This section is not the discovery.** What it adds is the second denominator's
coverage test, below. The two units:

| Unit | Source | US names |
|---|---|---|
| `risk_units --book` → `RISK_UNITS.json` (what **PREFLIGHT G5** measured) | `module_paper_book` DB | **11**: `AVGO NDAQ NVDA ANET ETN HPE MET MPC NUE PSX RTX` |
| `cycle_exposure` → `CYCLE_EXPOSURE.md` (what **DEEP COMM §3** measured) | live KIS `fetch_overseas_balance` | **12**: `NVDA LITE ANET PSX T RTX HPE ETN MPC AVGO COHR NUE` |

**Shared: 9. Paper-only: `NDAQ` `MET`. Real-only: `LITE` `T` `COHR`.**
⇒ A stage that writes *"the name the desk holds"* means a different set depending on which unit it
called. **This is not an error in either tool** — they are different books by design.

★ **The addition this stage makes to `D288`: re-run G5's own test on the OTHER book.** G5's "11/11 US
holdings inside `us_top300` **and** scored ✅" is a **paper-book** statement. Against the **real** book
it is **12/12 — also all present and all scored** (verified here by direct membership test:
`NVDA LITE ANET PSX T RTX HPE ETN MPC AVGO COHR NUE`, zero missing from the sweep).
⇒ **The gate is not returning a false ✅. It is returning a true ✅ about a different portfolio than the
one the exposure rule governs** — which is a narrower and more actionable statement than "the books
disagree", and it means no flow/RS judgment in this file is void for want of coverage.**

★ **One number changes as a result.** DEEP COMM §3 reads *"`T` is 9.59% of invested capital."* Measured
live at 23:52 KST on the real book: **`T` = 9.74%**, and **9.59% is `RTX`** — the adjacent row.
The magnitude of COMM's argument is unaffected (`T` really is ~9.7% of invested and really is
unlabelled); **the digit is corrected here rather than carried.**

---

## §A · Numbers — the candidate set, cross-checked

**Prices and every multiple are LIVE intraday 2026-08-19, pulled 23:45–23:52 KST (10:45–10:52 ET).**
Blanks are blanks. `vsTgt` = live price vs sell-side **target median** — reported because it inverts
against the flow ranking, ⚠ **not a valuation verdict** (a target median is a crowd artifact, not a
measurement; sell-side targets lag price by construction).
`Δeps90` = +1y consensus EPS now vs 90 days ago; `rev30` = +1y revisions up:down over 30 days —
**the direction of the denominator**, read next to the multiple and never alone (lens L2).

| Name | Sector | px (live) | fwd P/E | trail P/E | PEG | P/S | P/B | mcap | tgt med | **vsTgt** | β | **Δeps90** | **rev30** | next print |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `MPC` | ENRG | 365.11 | **11.34** | 12.65 | 1.76 | **0.69** | 5.42 | $102.5B | 322.00 | 🚨 **+13.4%** | 0.51 | **+44.4%** | **12↑/4↓** | 11-03 |
| `PSX` | ENRG | 243.58 | **11.46** | 13.90 | 1.35 | **0.64** | 3.08 | $97.7B | 220.00 | 🚨 **+10.7%** | 0.69 | **+29.8%** | **13↑/3↓** | 10-29 |
| `VLO` | ENRG | 348.87 | **11.43** | 14.55 | **4.08** | 0.76 | 4.02 | $100.5B | 323.00 | 🚨 **+8.0%** | 0.55 | **+51.9%** | **13↑/2↓** | 10-22 |
| `XOM` | ENRG | 167.75 | 15.77 | 21.62 | 1.25 | 1.91 | 2.66 | $689.8B | 169.00 | −0.7% | **0.17** | +2.1% | 10↑/10↓ | 10-30 |
| `LMT` | INDU | 601.67 | 18.39 | 22.17 | 1.26 | 1.80 | **15.78** | $138.9B | 620.00 | −3.0% | **0.11** | +1.8% | **18↑/0↓** | 10-20 |
| `NOC` | INDU | 587.22 | 19.29 | 18.67 | **4.05** | 1.94 | 4.66 | $83.4B | 640.00 | −8.2% | **−0.11** | +0.8% | 14↑/3↓ | 10-20 |
| `GD` | INDU | 393.92 | 21.24 | 24.00 | 2.75 | 1.94 | 3.97 | $106.6B | 430.00 | −8.4% | 0.33 | +2.4% | **17↑/1↓** | 10-28 |
| `RTX` ⬛ | INDU | 224.88 | **28.63** | **39.59** | 2.77 | 3.24 | 4.57 | $303.1B | 239.00 | −5.9% | 0.29 | +4.0% | **22↑/0↓** | 10-20 |
| `ETN` ⬛ | INDU | 424.80 | 26.49 | **45.58** | 3.25 | 5.49 | 8.15 | $165.0B | 486.00 | −12.6% | **1.18** | +1.9% | 15↑/2↓ | 11-03 |
| `NUE` ⬛ | MATR | 264.31 | 14.15 | 21.75 | **5.21** | 1.66 | 2.73 | $60.0B | 291.00 | −9.2% | **1.89** | **+19.9%** | **10↑/0↓** | 10-27 |
| `FCX` | MATR | 69.39 | 16.83 | 35.05 | **5.45** | 3.76 | 4.96 | $97.2B | 75.00 | −7.5% | 1.38 | +10.9% | 9↑/6↓ | 10-22 |
| `GOOGL` | COMM | 343.70 | 23.31 | 17.24 | **0.94** | 9.43 | 6.75 | $4,202.9B | 428.00 | **−19.7%** | 1.24 | +2.4% | **33↑/12↓** | 10-29 |
| `T` ⬛ | COMM | 25.37 | **9.89** | **8.37** | 1.66 | 1.37 | 1.58 | $173.8B | 28.00 | −9.4% | 0.42 | +0.3% | 13↑/5↓ | 10-21 |
| `WMT` | STPL | 116.49 | **35.51** | **40.87** | **4.39** | 1.28 | 9.83 | $927.0B | 140.00 | **−16.8%** | 0.60 | **−0.4%** | 🚨 **1↑/7↓** | **08-20** |
| `TGT` | STPL | 159.55 | 17.65 | 20.88 | 2.83 | **0.68** | 4.42 | $72.5B | 147.50 | **+8.2%** | 0.97 | +5.4% | 7↑/1↓ | 🚨 **08-19 (today)** |
| `KKR` ✦ | FIN | 111.83 | 15.14 | 35.73 | **0.59** | 4.00 | 3.56 | $103.3B | 126.00 | −11.2% | **1.79** | −1.5% | 10↑/8↓ | 11-05 |
| `LITE` ⬛✦ | IT | 854.69 | 25.89 | *(blank — no trailing EPS)* | **0.63** | **25.44** | **20.61** | $76.7B | 1121.00 | **−23.8%** | 1.51 | +6.9% | **6↑/0↓** | 11-06 |
| `ORCL` ✦ | IT | 140.36 | **12.86** | 24.08 | 0.85 | 6.00 | 10.76 | $404.3B | 240.00 | 🚨 **−41.5%** | 1.72 | +1.9% | 20↑/6↓ | 09-11 |

⬛ = held in the **real** KIS book · ✦ = cross-sector `US_LIVE_SHORTLIST` name (sector holds no DEEP slot).

### A-1 · The pattern §A exists to surface, and it is the same shape as 08-17

★ **The four names above their consensus target median are the four with the strongest recent tape;
the four furthest below it are the ones the tape has left behind.** `MPC` +13.4% · `PSX` +10.7% ·
`TGT` +8.2% · `VLO` +8.0% **vs** `ORCL` −41.5% · `LITE` −23.8% · `GOOGL` −19.7% · `WMT` −16.8%.
⚠ This inverts exactly against the flow ranking, which is why it is reported — **not** as a valuation
verdict. The mechanism is mechanical: targets are revised **after** price moves.

### A-2 · The denominator, which is where the refining node's case actually lives

**`MPC` +44.4% · `VLO` +51.9% · `PSX` +29.8%** on the +1y consensus EPS over 90 days, with revision
breadth **12↑/4↓ · 13↑/2↓ · 13↑/3↓**. ⇒ The "11.3–11.5× forward" on those three is a multiple whose
denominator has been **racing upward for a quarter**, which is the opposite of a cheapness claim — it
is the **peak-margin exposure** DEEP ENRG §3 named. **Read the two together or not at all (lens L2).**
Against them, `XOM` — which owns the barrel rather than the crack — sits at **+2.1% with 10↑/10↓**,
i.e. **dead flat in both level and breadth.** That contrast is DEEP ENRG's margin-vs-barrel answer
showing up in the estimate axis independently of price.

🚨 **The mirror image is `WMT`, hours before it prints:** the only name on the sheet with a **negative**
90-day estimate change (**−0.4%**) and the only inverted revision breadth (**1↑/7↓**). It is also the
sector's **new-🟢** and the carrier of Consumer Staples' `UW− → UW` promotion. **The flow axis and the
estimate axis point opposite ways on the same name, and its print is tomorrow.**

### A-3 · XBRL cross-checks — including the ones that failed

- 🚨 **The refiner period-tagging signature reproduces exactly as on 08-17.** `MPC` quarterly revenue
  steps **$34.20B (2026-03-31) → $51.99B (2026-06-30)**; `PSX` **$32.54B → $51.00B**. Two refiners
  posting the same ~+52% sequential (QoQ) step is a **6-month cumulative filed against a quarterly
  tag**, not an operating event. ⇒ **Marked `unknown` (C3). No growth figure — sequential or
  year-on-year — is derived from it, this run or last.**
- `LITE` has **no trailing EPS** ⇒ trailing P/E is **blank, not zero**; and its `P/S 25.44` / `P/B
  20.61` could not be cross-checked against a filing (XBRL quarterly revenue ends 2025-03-29).
  Reported from yfinance only and labelled as such.
- `CTVA`'s `next_earnings_date` field returns **2026-07-31 — a past date.** The field is stale, not a
  forward catalyst; it is **not** used in §E and the name is rejected in §G on other grounds.
- `VLO`'s `quarterly_revenue_xbrl` is empty ⇒ blank stays blank.

---

## §B · Thesis and ALPHA tag *(right column filled by Stage 10 · ALPHA, 2026-08-19)*

⚠ **Freshness authority.** PREFLIGHT **G1 FAILED** (sweep coverage 17.06%, 7th consecutive run) ⇒ the
**sweep's** velocity axis may not be cited by any stage. The per-name probes below **did answer** and
carry their probe time; **an empty or low reading is never read as "cooled"** — the same pipe returned
0/40 and then 40/40 inside four minutes at preflight.

| Name | Thesis, one line | **ALPHA tag · residual · re-check date** |
|---|---|---|
| `MPC` | **Refining-capacity destruction, not a crude trade — and this run finally attributed it.** The distillate crack ran **88.41 → 101.96 $/bbl (+13.56)** over 20 sessions in which `BZ=F` returned **+0.011%**; the crack owns **70% of the fitted 5-session excess vs `SPY` and 100% of the 20-session**. Refiners took **+4.74pp more than the integrateds** who own the barrel, same window, same benchmark `SPY` | 🟡 **PARTIAL** — residual: the **second consecutive** crack-rate decline (one has fired). Re-check **08-21** |
| `PSX` | Same node, same driver, and the node's **#2 by settled `flow_score` (0.694)**. Shortlisted at a relaxed `vol_surge ≥ 1.0` gate (**1.05**) — blocked from the real shortlist by the 1.2 volume gate alone, 4th run | 🟡 **PARTIAL** — residual: `vol_surge` ≥ 1.2 while OBV 매집 and RS20 +12.1 vs `SPY` hold. Re-check **08-21** |
| `VLO` | Same node. **Highest estimate revision of the three (+51.9% / 13↑/2↓)** against the **worst PEG in the sheet's energy block (4.08)**. ⚠ Its own missed-ledger entry fired on the price leg (RS60 **+41.87** vs `SPY`, 2.8× the +15 bar) for the **second** consecutive run | 🟡 **PARTIAL** — residual: PEG **4.08** must close, or it is the node's worst expression. Re-check **08-21** |
| `XOM` | **The control, not a candidate.** Owns the barrel; +2.1% estimate change and 10↑/10↓ breadth is the flat reading that makes the crack attribution legible | 🔴 **RESOLVED — dropped from the bettable list**, logged `A.flow미도착` (08-19, ALPHA). Flat on every axis; that is what makes it the control. Revives if revision breadth turns ≥2:1 up **and** RS60 vs `SPY` > +10. Re-check **09-16** |
| `LMT` `NOC` `GD` | **The defense accumulation is real and it is not `RTX`'s.** `LMT` `NOC` `GD` `BA` `AXON` all replicate on **both** OBV instruments; 9/10 of the A&D group accumulate and 8/10 are positive on RS20 **vs `SPY`**; `M719` strengthened to **+5.11pp on 60 days** (from +4.32pp). Revision breadth is the sheet's cleanest: **18↑/0↓ · 14↑/3↓ · 17↑/1↓** | 🟡 **PARTIAL** — residual: two-instrument OBV replication holding with RS20 vs `SPY` positive, A&D accumulation ≥6/10. Re-check **08-21** (`S97`) |
| `RTX` ⬛ | 🚨 **Thesis RE-FILED, not removed.** The run's "new-🟢" evidence **did not survive DEEP**: `vol_surge` **0.83** (0 of 50 INDU names clear 1.2), the 🟢 came off a **REVOKED** velocity axis that does not reproduce same-day, and the OBV reading flips sign on the second instrument. What survives is **RS20 +13.9 / RS60 +24.8 vs `SPY`** and **22↑/0↓** revisions — the group's tape, not a name-specific one. **New thesis line: `RTX` is the defense group's beta, not its leader**, and it carries a **negative tech beta (−0.51, t −4.96)** that makes it the book's diversifier | 🟡 **PARTIAL — momentum-only flag NOT stamped, C-grade disagreement stamped instead.** RS20 +13.9 / RS60 +24.8 vs `SPY` (A-grade) *agree* with the direction; the disagreement is between two **OBV** instruments, which is **grade C** and per D6 downgrades the tag without converting the bet into a tape trade. Residual: RS20 vs `SPY` staying positive while `vol_surge` stays under 1.2. Re-check **08-21** |
| `ETN` ⬛ | **In the right sector.** Loads **2.3× more on `XLI` than on `XLK`**; `S99`'s two branches do not contain that answer (construction note filed, thresholds untouched). **Most expensive trailing multiple on the sheet (45.58)** against +1.9% estimate change | 🟡 **PARTIAL** — residual: `XLI` loading staying above `XLK` on a refreshed 252-day window. Re-check **08-21** (`S99`) |
| `NUE` ⬛ | **The move is a post-earnings re-rate that PREDATES the tariff thread by twelve sessions** (DEEP MATR §7a) ⇒ EVENT_ALPHA Card 4's driver attribution is refuted by dating. What is left is a **+19.9% estimate change with 10↑/0↓** — the sector's only clean revision breadth — against **PEG 5.21** and **β 1.89, the highest on the sheet** | 🟡 **PARTIAL — positioning flag stamped.** FINRA short z **+1.99 🔴** against OBV 매집 with RS20 +10.7 vs `SPY`; ⚡ a short build is **turn-conditional fuel, never a standalone read** (REJECTED axis: "short building = bearish"). Residual: which of the two survives `S77`. Re-check **08-20** |
| `FCX` | **The live risk, not the thesis.** `Copper` COT sits at the **100th percentile** — the most extreme reading on the whole positioning board — and `FCX` carries **β +1.177pp per 1% `HG=F`, r +0.663 over 120 sessions.** But ex-`FCX` moves the sector observable **0.007pp** ⇒ the COT **cannot reach** the Materials verdict in either direction | 🔴 **RESOLVED — dropped**, logged `I.테제반증` (08-19, ALPHA). The COT-as-sector thesis is refuted by measurement (ex-`FCX` moves the observable **0.007pp**; `HG=F` needs **+49%**). The name-level copper beta survives as a **risk**, not a thesis. Revives if `HG=F` +20% from the 08-18 close with RS20 vs `SPY` > 0. Re-check **09-16** |
| `GOOGL` | **Half of the COMM underweight is already wrong.** β-adjusted excess **+1.227 vs `SPY`**, and the settled 08-18 close **344.20 sits 0.08% below its own 344.48 trigger.** The UW is carried by `META` (β-adj **−6.704 vs `SPY`**), not by the label | 🟡 **PARTIAL** — residual: a close above **344.48** (settled 08-18 close 344.20, 0.08% below) with OBV turning 누적 and RS60 vs `SPY` above −10. Re-check **08-21** |
| `T` ⬛ | 🚨 **An orphan position, stated as one.** 9.74% of invested (corrected, §0a), in a 3.6%-weight node whose `eqflow` is **+0.404** and whose three names are 3/3 OBV-accumulating with **median RS20 +8.3 vs `SPY`** — but with **no cycle label, no card, no thread, no bracket and no KPI** in any live artifact. Cheapest multiple on the sheet (**fwd 9.89 / trail 8.37**). *The desk cannot claim credit for a position it has no thesis for, and cannot manage one either* | 🟡 **PARTIAL — and the residual is a label, not a price.** Telecom-ex-`TMUS` `eqflow` +0.404 (6th straight tape > +0.25) with RS20 +9.3 vs `SPY`; what is missing is a cycle label, a card and a KPI. Re-check **08-26** |
| `WMT` | **The promotion's carrier and its own strongest counter-argument.** One of the run's two new-🟢 and the largest single contributor to the board's largest two-session Δ (+0.446) — while its estimate axis is the sheet's **only negative** (−0.4%, **1↑/7↓**). Frame-transfer answered: **membership-fee income is the real take-or-pay analogue and `WMT` discloses it** (up to 22.6% of group operating income; Sam's Club U.S. at 103.4% of segment operating income) **while `TGT` does not quantify its equivalent at all** — yet `S100` equal-weights the two | 🟡 **PARTIAL** — residual: **its own print, 08-20**, implied **±4.9%**, against an estimate axis of −0.4% / 1↑7↓. Re-check **08-20** |
| `TGT` | **The under-computed leg.** At **1.8% sector cap weight** it is invisible to every cap-weighted instrument the run read, yet it carries the sector's best settled `flow_score` (**0.713**) and its **only `vol_surge` above 1.1 (1.12)**. It is also **the node's only positive-β name (+0.455, 252d vs `SPY`)**, which is precisely the name the "defensive-β" explanation cannot cover | 🟡 **PARTIAL** — residual: **its print today**, implied ±3.4%, P/C 1.74. Re-check **08-20** |
| `KKR` ✦ | The relocated Financials breadth node — **highest settled `flow_score` on the whole board (0.757)** with the sheet's cheapest growth-adjusted multiple (**PEG 0.59**). ⚠ Sector is flipper-blocked, so no sector route exists to it | 🟡 **PARTIAL** — residual: no sector route exists while Financials is flipper-blocked; the name's own axes are the board's best. Re-check **09-02** |
| `LITE` ⬛✦ | **Optical/interconnect — the only node in EVENT_ALPHA where story and money both cleared** (Card 7). Settled `vol_surge` **1.25**, one of three sweep names above 1.2. ⚠ Card 7's "clean rise" label was corrected to half-wrong in the same run's §11d, and the settled **Δ −0.274** is among the board's weakest | 🟡 **PARTIAL** — residual: `vol_surge` holding ≥1.2 while RS60 vs `SPY` (−12.8) turns. Re-check **09-02** |
| `ORCL` ✦ | **The widest price-to-consensus gap on the sheet (−41.5%)** with 20↑/6↓ revisions and settled **RS20 +9.8 vs `SPY`** against **RS60 −28.1** — a name whose 20-day and 60-day tapes disagree by 38pp | 🟡 **PARTIAL** — residual: the **38pp** RS20/RS60 gap vs `SPY` resolving upward rather than downward. Re-check **09-11** (print) |

### B-1 · 🚨 Why there is not one 🟢LIVE on this sheet — **two independent reasons, and neither is "the market is quiet"**

**🟢LIVE fired 0 times. That is the 9th consecutive US run at zero, and this run can name both causes.**

**Reason 1 — the right is revoked.** PREFLIGHT **G1 FAILED**. The rule is explicit: *when G1 FAILs,
ALPHA may not issue a freshness verdict at all.* So the tags above are issued on the **non-news** axes
(price/RS vs `SPY`, OBV, `vol_surge`, revisions, positioning, dated prints) and **no tag anywhere in
this file rests on a freshness reading** — including the two 🔴RESOLVED, which rest on measured
arithmetic (`XOM` flat on every axis; `FCX` refuted by a 0.007pp sensitivity).

**Reason 2 — the gate could not fire even with a live pipe.** 🟢FRESH needs **age ≤14d AND accel ≥2×**.
Probed **23:5x KST, 8 terms, foreign scope, 8 of 8 answered**:

| theme | tag | age | 7d avg | accel | total |
|---|---|---|---|---|---|
| `retail earnings` | 🟡ACCELERATING | ≥90 | 12.3 | **52.65×** | 98 |
| `telecom fiber` | 🟡ACCELERATING | **35** | 0.1 | 4.29× | ⚠ **2** |
| `defense backlog` | 🟡ACCELERATING | **30** | 0.7 | 2.68× | ⚠ 13 |
| `optical interconnect` | ⚪ECHO | ≥90 | 3.9 | 1.63× | 147 |
| `AI data center` | ⚪ECHO | ≥90 | 85.3 | 1.02× | 4365 |
| `refining margins` | ⚪ECHO | 82 | 6.0 | 1.00× | 234 |
| `steel tariffs` | 🔴FADING | 81 | 0.1 | 0.48× | ⚠ 14 |
| `distillate crack` | 🔴FADING | 34 | 0.0 | 0.00× | ⚠ **4** |

★ **`F1` is narrowed by this table, not merely repeated.** The 08-17 statement was *"17 of 19 terms read
`>=90`, so the age readout is capped and 🟢FRESH is structurally unreachable."* Today **three of eight
returned a real numeric age below 90 (30, 34, 35)** ⇒ **the age readout is not always capped; it returns
real values when the theme genuinely is younger.** The acceleration leg cleared **three times** (52.65× ·
4.29× · 2.68×). ⇒ **The binding constraint today is the conjunction, not a broken instrument:** the terms
young enough to pass the age leg are `defense backlog` (30d) and `telecom fiber` (35d), and 14 days is
still well below both. **A US desk trading multi-quarter industrial cycles will keep reading zero here,
and now it is arithmetic on this run's own numbers rather than an inference.**

⚠ **And three of the eight rows are too thin to read in any direction**: `telecom fiber` **n=2**,
`distillate crack` **n=4**, `steel tariffs` **n=14**. 🚫 **`distillate crack` reading 🔴FADING is NOT
evidence the ENRG thesis's driver cooled** — the driver is a **price series** (88.41 → 101.96 $/bbl,
measured), and four articles cannot contradict it. **A thin denominator is not a signal**, and under G1
it is not even admissible as one.

🚫 **Standing consequence, unchanged**: no bet may be marked 🔴RESOLVED on a freshness reading, because
the instrument cannot issue the contrasting tag. **Both of today's 🔴RESOLVED were issued on measured
non-news axes, and both carry a ledger row with a revival condition.**

### B-2 · Carry-forward — tags follow the NAME, not the sector's turn in the rotation

**All 14 🟡PARTIAL names below are carried into the next run's inheritance packet regardless of whether
their sector holds a DEEP slot.** Measured origin: `006360` carried an ALPHA tag with real flow on
07-20, its sector rested, nothing tracked it, and it ran **+12.3% over five sessions, unowned.**

| Re-check date | Names |
|---|---|
| **08-20** | `NUE` · `WMT` · `TGT` |
| **08-21** | `MPC` · `PSX` · `VLO` · `LMT` `NOC` `GD` · `RTX` · `ETN` · `GOOGL` |
| **08-26** | `T` |
| **09-02** | `KKR` · `LITE` |
| **09-11** | `ORCL` |
| **09-16** (revival watch, 🔴) | `XOM` · `FCX` |

⚠ **`KKR` `LITE` `ORCL` are the load-bearing rows here** — Financials and IT hold **no DEEP slot** this
run, so without this list they would leave the pipeline entirely at the sector boundary. `LITE` is also
**a real-book holding at 12.17% of invested**, which is the exact 006360 shape.

---

## §C · Flow and positioning cross-read

### C-1 · Settled 2026-08-18 — the admissible axes

`flow_score` is **3-axis** (news axis dropped, coverage 17.06%). FINRA short-vol `date 2026-08-18`.

| Name | score | tag | `obv_state` | **RS20 vs `SPY`** | **RS60 vs `SPY`** | `vol_surge` | Δ (2-sess) | short z | 5v5 |
|---|---|---|---|---|---|---|---|---|---|
| `MPC` | 0.700 | 🟡중립 | 매집 | **+12.0** | **+44.1** | 1.06 | −0.106 | +0.03 | −2.0▼ |
| `PSX` | 0.694 | 🟡중립 | 매집 | **+12.1** | **+36.6** | 1.05 | +0.066 | +1.22 | +13.8▲ |
| `VLO` | 0.511 | 🟡중립 | 매집 | +8.6 | **+41.9** | 0.72 | +0.021 | +0.60 | +9.5▲ |
| `XOM` | 0.371 | 🟡중립 | 매집 | +6.6 | +3.3 | 0.82 | +0.127 | +1.43 | −0.1· |
| `LMT` | 0.528 | 🟡중립 | 매집 | **+17.2** | +12.8 | 0.75 | −0.016 | −0.07 | +1.3▲ |
| `NOC` | 0.483 | 🟡중립 | 매집 | +12.4 | +3.5 | 0.67 | +0.054 | −0.10 | −3.7▼ |
| `GD` | 0.256 | 🟡중립 | 매집 | +4.4 | +12.8 | 0.53 | +0.068 | +1.32 | +6.1▲ |
| `RTX` ⬛ | 0.572 | 🟢가속 | 매집 | **+13.9** | **+24.8** | 0.83 | +0.105 | +0.30 | −15.8▼ |
| `ETN` ⬛ | 0.360 | 🟡중립 | 매집 | +4.5 | +9.7 | 0.71 | −0.118 | −1.08 | −7.9▼ |
| `NUE` ⬛ | 0.483 | 🟡중립 | 매집 | +10.7 | +13.3 | 0.67 | +0.022 | 🔴 **+1.99** | +3.7▲ |
| `FCX` | −0.100 | 🟡중립 | 중립 | +3.4 | +3.1 | 0.64 | **−0.426** | −0.47 | +6.0▲ |
| `GOOGL` | −0.450 | 🟡중립 | 중립 | −3.4 | −14.5 | 0.61 | +0.022 | 🟢 **−2.00** | −10.1▼ |
| `T` ⬛ | 0.383 | 🟡중립 | 매집 | +9.3 | −5.1 | 0.49 | −0.006 | 🟢 **−1.98** | −3.7▼ |
| `WMT` | 0.220 | 🟢가속 | 매집 | +1.8 | −8.4 | 0.83 | **+0.446** | −0.27 | +11.3▲ |
| `TGT` | 0.713 | 🟡중립 | 매집 | +7.5 | **+17.5** | **1.12** | +0.210 | −0.85 | +6.4▲ |
| `KKR` ✦ | **0.757** | 🟢가속 | 매집 | +7.8 | +9.8 | **1.32** | −0.182 | −1.47 | −1.7▼ |
| `LITE` ⬛✦ | 0.543 | 🟢가속 | 매집 | +1.7 | −12.8 | **1.25** | −0.274 | −1.07 | −4.6▼ |
| `ORCL` ✦ | 0.508 | 🟢가속 | 매집 | +9.8 | **−28.1** | 0.76 | −0.070 | −1.20 | −3.7▼ |

**Three readings that carry weight, each with the counter-axis attached:**

1. 🚨 **`NUE` is the only 🔴 on the short axis — and it is a book holding.** Short-volume ratio **63.2%
   vs its own 20-day base 51.1%, z +1.99, trend +3.7▲.** Against it: **OBV 매집 with RS20 +10.7 / RS60
   +13.3 vs `SPY`** and revisions **10↑/0↓**. **Two admissible axes disagree on a held name and neither
   is dismissed here.** The correct next instrument is `S77`'s settle, not a third opinion.
2. **`GOOGL` and `T` are the only two names on the sheet where the marginal seller is measurably
   leaving** (short z **−2.00** and **−1.98**, both with negative 5v5). For `GOOGL` this sits beside a
   β-adjusted excess of **+1.227 vs `SPY`** — i.e. **the half of the COMM underweight that is already
   wrong is also the half the shorts are exiting.**
3. **The volume gate binds almost everything.** Of the 18 names above, only **`KKR` 1.32 · `LITE` 1.25 ·
   `TGT` 1.12 · `MPC` 1.06 · `PSX` 1.05** clear or approach 1.2. This is `M144`'s 7th replication and it
   is a **gate property, not an absence of money** — Energy's sector maximum is 1.06 and Health Care's
   is 1.00, so "0 green" in those sectors may **not** be cited as weakness.

### C-2 · Live intraday 2026-08-19, quarantined — implied move, options, short float

**Pulled 23:5x KST, mid-session. 🚫 Not comparable to §C-1 and not subtracted from it (G0 rule #2).**
Nearest expiry **2026-08-21 (D2)** except `GOOGL` (D0). Implied move = ATM straddle to expiry, i.e. the
**total** move to that date, not the isolated event contribution.

| Name | live tag | **implied move** | short %float · direction | P/C OI | IV skew | news velocity *(probe 23:5x)* |
|---|---|---|---|---|---|---|
| `MPC` | 🟡중립 | **±3.0%** (08-21, D2) | 2.8% · covering, DTC 3.4 | 1.06 | +61.0 | 1.07× |
| `RTX` ⬛ | 🟡중립 | **±1.3%** (D2) | 1.3% · **building**, DTC 3.6 | 0.73 | +49.4 | 1.04× |
| `NUE` ⬛ | 🟡중립 | **±2.4%** (D2) | 2.1% · covering, DTC 2.6 | 0.75 | +22.0 | 0.84× |
| `TGT` | 🟢가속 | **±3.4%** (D2) | 3.7% · covering, DTC 4.3 | 🚨 **1.74** | +42.9 | **2.82×** |
| `WMT` | 🟢가속 | 🚨 **±4.9%** (D2) | 1.6% · covering, DTC 3.2 | 0.67 | +0.3 | 1.70× |
| `GOOGL` | 🟡중립 | ±0.8% (**D0**) | 1.2% · covering, DTC 2.4 | 0.75 | +17.1 | 1.12× |
| `T` ⬛ | 🟡중립 | ±1.7% (D2) | 1.9% · **building**, DTC 1.5 | 0.83 | +17.6 | 1.09× |

🚨 **The `S100` bracket is live right now and the two legs are not symmetric.** `WMT` prints **08-20**
with a **±4.9%** implied move — **the largest on the sheet** — a **flat** IV skew (+0.3) and a
**call-tilted** book (P/C 0.67), against an estimate axis that is **negative and 1↑/7↓**. `TGT` prints
**today (08-19)** with **±3.4%**, a **put-heavy** book (P/C **1.74**) and the sheet's best settled flow.
**Two names, one bracket, opposite option postures, one estimate axis pointing down on the one with the
bigger implied move.** ⚠ **The print itself has not been read by this desk** and no direction follows.

⚠ **Two live/settled disagreements, named rather than reconciled:** `TGT` reads **🟢가속 live** vs
**🟡중립 settled**, and `RTX`'s short direction reads **building live** vs **z +0.30 / 5v5 −15.8▼
settled**. Both are vintage artifacts of a mid-session pull. **The settled reading governs; the live one
is recorded because the next run will have it as history.**

---

## §D · Competition and peers

| Node | Names | Relative position, measured |
|---|---|---|
| **Refining (ENRG)** | `MPC` `PSX` `VLO` vs `XOM` `CVX` | **The node beat the barrel by +4.74pp over the same five sessions vs `SPY`.** Intra-sector dispersion is **48.73pp against `XLE`'s +4.37pp excess vs `SPY` — 11.2×** ⇒ *"Energy"* is the wrong unit of analysis. ⚠ `MPC` has **no take-or-pay floor** (read from the 10-K; contracted share `unknown`) — a merchant structure with margin above its own peak year |
| **Defense primes (INDU)** | `LMT` `NOC` `GD` `RTX` `BA` `AXON` (+`LHX`) | Primes are **11.3% of INDU cap** and correlate **+0.082** with the label's other 40 names, while machinery (**+0.862**) and electricals (**+0.836**) are the label and are **one object with each other (+0.754)**. ⇒ Defense is **not in this sector** in any statistical sense; the label's internal spread is **36×** its own two-session move |
| **Electricals (INDU)** | `ETN` vs `XLI` / `XLK` | `ETN` loads **2.3× more on `XLI`**; `RTX` carries a **negative** tech beta (−0.51, t −4.96). ⇒ `S99`'s "wrong sector" framing is refuted; `RTX` is the diversifier, `ETN` is not misplaced |
| **Materials chain** | `NUE` `FCX` `CTVA` `LIN` `CRH` +6 | `S77` = **−3.231 EW over 5 settled sessions vs `SPY`, 10 of 11 negative**, reproduced independently to the third decimal; **β-adjusting makes it worse (−3.307)**, and it is **flipper-proof** because it is equal-weighted (`LIN` enters at 1/11, not 24.7%). ⇒ the underweight is **not a `NEM` artifact** (`NEM`'s own 5-session excess vs `SPY` is −0.646). ⚠ It does **not** mean deterioration: the same 11 are **+0.637 vs `SPY` over 60 sessions** |
| **Comm Services** | `META` vs `GOOGL`/`GOOG` vs telecom vs streaming | The sector **has no sign** — `wflow −0.439` and the `XLC` β-adjusted print are **the same cap-weighted reading twice**. Corrected: cap-weighted **+0.049**, equal-weighted **−0.166** — both flat. Median `flow_score` **+0.148**, 6 of 12 positive, ex-mega `eqflow` **+0.178**. ⇒ **the UW is a single-stock short of `META` wearing an eleven-name label.** ⚠ **`EA` is not measurable** (7th run) ⇒ the sector's composition here is **12 of 13** and every statistic above carries that denominator |
| **Staples retail** | `WMT` vs `TGT` vs grocery/distribution | The label is the wrong unit **by 5–16×**, and the node **inverted since 08-17**: big-box is now the sector's best node and grocery/distribution its worst. `WMT` discloses membership-fee income (the real take-or-pay analogue); **`TGT` does not quantify its equivalent at all** — and `S100` equal-weights them |
| **Cross-sector ✦** | `KKR` `LITE` `ORCL` | No DEEP slot covers Financials or IT this run. `LITE` is the optical node's survivor (`vol_surge` 1.25); `KKR` is the board's highest settled `flow_score`; `ORCL` carries the widest consensus gap. **All three are carried to §A/§B without a sector mandate behind them, and that is stated rather than implied** |

### D-1 · The screener's own answer, and where it disagrees with the money

`us_setup_screener --sector` was run this stage across all five DEEP sectors. ⚠ **It re-downloads
prices, so its RSI / px-vs-200DMA readings sit on a LIVE partial 08-19 bar** — they are used for
**candidate generation only** and are never compared to §C-1.

| Sector | A. leader pullback | B. de-rate snapback | C. washout | ⇒ |
|---|---|---|---|---|
| **Energy** | 0 | 0 | 0 | **Nothing to add.** The node the DEEP is built on offers no setup at all — consistent with names already extended above their target medians (§A-1) |
| **Industrials** | `PCAR` `GWW` `DAL` `UAL` | 0 | 0 | 4 new names, **and not one of them is a defense prime** — the setup screen and the accumulation evidence point at different halves of the sector |
| **Materials** | `CTVA` | `CRH` | 0 | Both are `S77` legs — `CTVA` the only positive one, `CRH` the worst |
| **Comm Services** | 0 | 0 | 0 | **Nothing.** A sector with no sign also has no setup |
| **Consumer Staples** | `CCEP` `SYY` `PM` | 0 | `MNST` | 4 new names on the day the sector was promoted |

★ **The disagreement is the finding.** The screener surfaced **10 names**, and the settled flow axis
rejects or de-prioritises **every one of them**: `GWW` −0.789, `CTVA` −0.771, `CRH` −0.558, `PCAR`
−0.413, `DAL` −0.369, `SYY` −0.275, `UAL` −0.241, `PM` −0.096, `MNST` +0.173, `CCEP` +0.104 — **8 of 10
negative, none above +0.18.** A setup screen selects on price structure; the flow axis selects on
accumulation. **On this tape they overlap on nothing**, and all 10 are disposed of in §G rather than
left implicit.

---

## §E · Refutation and dated catalyst — one per name

| Name | **What would refute the thesis** | **Dated catalyst / observable** |
|---|---|---|
| `MPC` | The **rate** of the distillate crack turning negative for a **second consecutive** decline (one has fired) — the price-cycle rule, since refining is a commodity node and the level is not the signal | `P75`/`P70` settle **2026-08-21**; next print **11-03** |
| `PSX` | `vol_surge` failing to clear 1.2 for a 5th consecutive run while OBV 매집 persists with RS20 +12.1 vs `SPY` ⇒ the accumulation is not being funded | **08-21** (`S88`); print **10-29** |
| `VLO` | PEG **4.08** not closing while the node's crack rate rolls ⇒ the node's worst expression | **08-21**; print **10-22** |
| `LMT` `NOC` `GD` | Group OBV replication breaking on the **second** instrument while RS20 vs `SPY` stays positive, or A&D accumulation falling below 6/10 | `S97` (`LHX`) settles **08-21**; prints **10-20 · 10-20 · 10-28** |
| `RTX` ⬛ | RS20 vs `SPY` turning negative while the group stays positive ⇒ the name is not the group's beta after all | **08-21**; print **10-20**. 🚨 **The customer has not been measured in 203 days** — that, not the flow, is this thesis's open exposure, unchanged across four consecutive DEEP slots |
| `ETN` ⬛ | `XLI` loading falling below the `XLK` loading on a refreshed 252-day window | `S99` settles **08-21** (construction note filed; thresholds untouched) |
| `NUE` ⬛ | The short z holding **above +1.5 for 5 sessions** while OBV 매집 and RS20 +10.7 vs `SPY` persist ⇒ the disagreement resolves against OBV (grade C loses to the measured axis) | `S77` settles **tonight 08-19**; print **10-27** |
| `FCX` | `HG=F` moving **+49%** — the measured magnitude the `Copper` COT would need to reach the sector observable. **It is a live risk on the name and cannot reach the sector** | COT weekly, Tue-close +3–4d lag; print **10-22** |
| `GOOGL` | Failing to close above **344.48** while OBV stays 중립 and RS60 vs `SPY` stays below −10 | Settled 08-18 close **344.20 = 0.08% below the trigger**; print **10-29** |
| `T` ⬛ | Telecom-ex-`TMUS` `eqflow` falling below **+0.25** while `T`/`VZ` 20-day OBV slopes stay negative and RS60 vs `SPY` stays under 0 ⇒ the accumulation is older than 20 days and the breakout was the top | 6th straight tape above +0.25; print **10-21** |
| `WMT` | 🚨 **Its own print, tomorrow.** The estimate axis (**−0.4%, 1↑/7↓**) refuting the flow promotion is the single cleanest falsification available on this sheet | **2026-08-20**, implied **±4.9%** |
| `TGT` | Its print today resolving against the under-computed-leg reading, i.e. the 1.8%-weight name failing to carry the sector's rank | **2026-08-19 (today)**, implied **±3.4%**, P/C **1.74** |
| `KKR` ✦ | Settled `flow_score` losing the board's #1 slot while `vol_surge` falls under 1.2 | `S78` settled **08-19**; print **11-05** |
| `LITE` ⬛✦ | `vol_surge` falling below 1.2 while RS60 vs `SPY` stays negative (**−12.8**) ⇒ Card 7's node had one buyer, not a bid | Print **11-06** |
| `ORCL` ✦ | RS20 vs `SPY` (**+9.8**) rolling back toward RS60 vs `SPY` (**−28.1**) instead of RS60 rising ⇒ the 38pp disagreement resolves the wrong way | Print **2026-09-11** |

---

## §F · Epicenter / cycle exposure — **no GAP is flagged, and the reason that matters is the registry, not the book**

`CYCLE_EXPOSURE.md` reports **✅ no top-rank cycle GAP**: AI-compute epicenter **19.82% of total**
(need ≥12.0%), Energy/refining **9.64%** (need ≥8.0%), missile-defense **5.97%** (no threshold set).
⇒ **No epicenter-starter module is required by the pre-mortem this run**, and none is written.

🚨 **The instrument's coverage is the finding — and it is a REPLICATION, not a discovery.**
`STANDING_VIEW_US §3a` already carries a row registered by the **2026-08-17** run: *"the desk's registry
does not contain the cycle owning its two best-scoring names"* (optical/interconnect). **That row is
credited here rather than re-found.** What this stage adds is the **count, the dollar magnitude, and a
third name the 08-17 row did not reach.** Of the **12** US names in the real book, **5 appear nowhere in
`data/cycles/cycle_registry.json`** — verified by direct membership test: `LITE` ✗ · `COHR` ✗ · `HPE` ✗ ·
`T` ✗ · `NUE` ✗ (present: `NVDA` `AVGO` `ANET` `ETN` `MPC` `PSX` `RTX`). ★ **`HPE` is the addition** — it
is not an optical name, so the 08-17 framing ("the optical cycle is missing") does not cover it, and the
**paper book's own theme label for it is literally `AI-compute-chain`.** ⇒ the gap is **registry
coverage generally**, not one absent cycle.

| Unlabelled name | live eval | read |
|---|---|---|
| `LITE` | $856.01 | optical/interconnect — **the AI-compute chain**, and EVENT_ALPHA Card 7's own subject |
| `COHR` | $296.65 | same node |
| `HPE` | $530.10 | the **paper** book's own theme label for it is literally `AI-compute-chain` |
| `T` | $684.99 | genuinely off-cycle — the orphan COMM §3 named |
| `NUE` | $263.74 | genuinely off-cycle (steel) |

**`LITE + COHR + HPE` = $1,682.76 = 23.93% of invested = 14.75% of total** — all three are AI-compute
chain names by the desk's own labelling elsewhere, and **the registry counts none of them.**
⇒ Reported AI-compute any-layer exposure **23.64% of total** would read **≈38.39%** if the registry
covered what the desk already believes it owns. **The GAP flag is therefore conservative in the safe
direction — under-counting cannot manufacture a false ✅ — but the exposure number it prints is
understated by roughly 15pp of total assets, and no stage would see that from the output.**
⚠ **No exposure decision follows from this** (P4). It is a registry-coverage defect, filed to the carry
as a dig; **editing the registry is a human call.**

---

## §G · Names set aside, and names never reached — both ledgers written

**10 rejections + 7 missed entries filed BY THIS STAGE.** Every row carries a class **and** a
revival/entry condition **and** a re-check date — the script refuses to write without both.

⚠ **The date's totals are larger than this section, and the difference is not this stage's.** Reading
`out/*_ledger.jsonl` for **2026-08-19**: **13 rejections** (11 stamped `BET`, 2 `ALPHA`) and **22 missed**
(18 stamped `BET`, 4 `EVENT_ALPHA`). The extra `BET`-stamped rows were written **before** this stage by
this run's own PREMORTEM — the **eleven `S101` "erased runners"** (`ABNB` `DASH` `DELL` `AXON` `SHOP`
`BKNG` `TMO` `PYPL` `PANW` `CRWD`) plus `NEM` — i.e. the basket whose frozen 5-session spread vs the
admitted shortlist **is** `S101`'s observable. **They are not re-filed here and they are not double
counted.** ⚠ One row, `000810`, is a **KR** ticker stamped `BET` on this date and belongs to the sibling
desk's run; **ledger counts must be read by stage AND market, not by date alone.**

### G-1 · Rejections (`reject_ledger.py add --stage BET`)

| Ticker | Class | Why (one line) | Revives if | Re-check |
|---|---|---|---|---|
| `CAT` | C.차트붕괴 | settled flow **−0.657**, OBV 분산, **RS20 −8.1 vs `SPY`** | OBV returns 매집 **and** RS20 vs `SPY` > 0 on a settled sweep | 09-02 |
| `GWW` | A.flow미도착 | screener pullback (RSI 42.5) vs settled flow **−0.789**, OBV 분산, **RS20 −6.0 vs `SPY`** — setup and money point opposite ways | OBV 매집 **and** `flow_score` > 0 | 09-02 |
| `CTVA` | A.flow미도착 | `S77`'s **only positive leg (+2.62 vs `SPY`)** yet settled flow −0.771, **RS20 −12.9 vs `SPY`**, OBV 분산; revisions 1↑/2↓ | RS20 vs `SPY` > 0 **and** OBV 매집 | 09-09 |
| `CRH` | C.차트붕괴 | worst `S77` leg (**−7.53 vs `SPY`**); settled flow −0.558, OBV 분산, **RS20 −9.1 vs `SPY`**; the −31.7% gap to target is a **de-rate, not a discount** | px reclaims its 200DMA **and** OBV 매집 | 09-09 |
| `MNST` | C.차트붕괴 | screener **washout** bucket: RSI **7.7**, px/200 **−41%**, ~50DMA −46%; settled **RS20 −52.9 / RS60 −48.8 vs `SPY`** ⇒ the STPL sector-max `vol_surge` **1.62 is this collapse**, not accumulation | RS20 vs `SPY` > −10 **and** OBV 매집 | 09-16 |
| `META` | A.flow미도착 | carries the entire COMM sign (β-adj **−6.704 vs `SPY`**); settled flow −0.733, OBV 분산, **RS20 −18.1 vs `SPY`**; revisions **8↑/39↓** | β-adj 5-session excess vs `SPY` turns positive **and** revision breadth reaches 1:1 | 09-02 |
| `KMI` | A.flow미도착 | ties the ENRG sector-max `vol_surge` **1.06** with OBV 매집, but **RS20 −1.0 / RS60 −5.2 vs `SPY`** — volume present, relative bid absent | RS20 vs `SPY` > 0 with OBV still 매집 | 09-02 |
| `CSCO` | G.섹터중립 | LIVE-shortlist green, but **IT holds no DEEP slot** and sits at N; **RS20 −3.1 vs `SPY`** | IT receives a DEEP slot **or** settled RS20 vs `SPY` > +5 with `vol_surge` ≥ 1.2 | 09-02 |
| `MA` | G.섹터중립 | LIVE-shortlist green in **flipper-blocked** Financials (`BRK-B` 13.9%), held N− with `eqflow` −0.087 | Financials receives a DEEP slot **or** `vol_surge` ≥ 1.2 with RS20 vs `SPY` > +5 | 09-02 |
| `BAC` | G.섹터중립 | same block; strongest OBV of the three (0.490) with **RS60 +21.4 vs `SPY`**, but `vol_surge` 0.81 and no admissible sector route | as `MA` | 09-02 |

🚨 **`CSCO`/`MA`/`BAC` are `structural`, not `measured`, rejections — and the ledger's re-print at the
ALPHA stage says this is the desk's most expensive rejection class, not a safe one.** `reject_ledger.py
score` over **96 scored rows** puts the *type* `structural` at **−1.0pp (n=6)**, but the specific class
used here, **`G.섹터중립`, at +13.9pp (n=2)** — and in this ledger **a positive excess means the
rejection cost us.** Two observations is not a rule (P4) and the window is short, but the number points
the wrong way for exactly the move being made, so it is written next to the move rather than in a
footnote. **The three rows stand — no sector mandate reaches these names and inventing one would be
worse — but they are filed knowing the prior is against them, with the shortest revival conditions on
the sheet (09-02).**

### G-2 · Missed — surfaced upstream, never reached a rejection (`missed_ledger.py add`)

| Ticker | Class | Why it never reached the sheet | Enters if | Re-check |
|---|---|---|---|---|
| `PCAR` | M.숏리스트탈락 | INDU screener pullback (RSI 37.9), **RS60 +13.8 vs `SPY`** — the INDU DEEP was scoped to the defense-vs-machinery question | OBV 매집 on a settled sweep **and** RS20 vs `SPY` > 0 | 09-02 |
| `DAL` | M.숏리스트탈락 | Transport is **14.5% of INDU cap with 0 of 9 accumulating** ⇒ the node was passed over wholesale; **RS60 +10.0 vs `SPY`** | Transport reaches ≥3/9 accumulating **and** RS20 vs `SPY` > 0 | 09-09 |
| `UAL` | M.숏리스트탈락 | same node; **RS60 +15.8 vs `SPY`** is the node's best, against a **Δ −0.516** that is the sweep's 2nd-largest two-session decline | Δ turns positive on a settled sweep **and** OBV 매집 | 09-09 |
| `WBD` | Q.확신부족 | **highest COMM `flow_score` (+0.604)** with the sector's best Δ (**+0.470**) and OBV 매집 with **RS20 +7.7 vs `SPY`** — zero cards name it and the DEEP resolved at sector level | sector max `vol_surge` clears 1.2 on `WBD` **or** a dated 8-K catalyst is sourced | 09-02 |
| `CCEP` | M.숏리스트탈락 | STPL screener pullback (RSI 38.3), **RS60 +10.8 vs `SPY`**, OBV 매집; the STPL DEEP was scoped to the print bracket | `vol_surge` ≥ 1.2 **and** RS20 vs `SPY` > 0 | 09-09 |
| `PM` | M.숏리스트탈락 | carries the **sector's largest two-session Δ (+0.511) — larger than `WMT`'s +0.446** — and is unnamed anywhere in the run | OBV turns 매집 with RS20 vs `SPY` > 0 | 09-02 |
| `SYY` | M.숏리스트탈락 | STPL screener pullback in the **grocery/distribution node the DEEP called the sector's worst**; dropped with the node | the distribution node stops being the sector's worst **and** OBV 매집 | 09-16 |

⚠ **Sign discipline**: the two ledgers' `excess` signs are **inverted** (`reject` +excess = the rejection
cost us; `missed` +excess = missing it cost us). They are **not summed** here.

★ **`PM` is the row this section exists for.** It carries the largest two-session flow improvement in
the sector this run's promotion was written about, and **no stage named it once** — not SWEEP, not
EVENT_ALPHA, not the DEEP, not ROTATION. Without this ledger it would have left **no trace at all**,
which is exactly the F2 gap ("we were disciplined" and "we never saw it" producing identical evidence).

### G-3 · Re-filed rather than removed

- **`RTX`** — its 🟢 evidence was refuted inside this run (§B), but its **measured** axes still pass
  (**RS20 +13.9 / RS60 +24.8 vs `SPY`**, revisions **22↑/0↓**, OBV 매집). Per the BET rule, a name whose
  money still arrives is **re-stated at lower conviction, not deleted** — new thesis line and a dated
  re-check (**08-21**) are in §B/§E. **No rejection row was written for it.**

---

## ✅ EXIT CHECK

- [x] **Every DEEP sector has a section** — ENRG · INDU · MATR · COMM · STPL are represented across
      §A–§E, and the cross-sector `US_LIVE_SHORTLIST` names are handled explicitly: **`KKR` `LITE`
      `ORCL` carried into §A/§B; `CSCO` `MA` `BAC` dropped with a stated reason and filed as
      rejections; `RTX` and `WMT` sit inside their DEEP sectors.** Zero shortlist names unaccounted for.
- [x] **Numbers cross-checked; blanks are blanks.** The `MPC`/`PSX` +52% sequential step is marked
      `unknown` (period-tagging signature, not an operating event); `LITE` trailing P/E and `VLO` XBRL
      revenue are **blank**; `CTVA`'s past-dated `next_earnings_date` is named as a stale field and not
      used as a catalyst.
- [x] **Flow/positioning cross-read present per candidate, one file written** — §C-1 settled 08-18 for
      all 18 names, §C-2 live/quarantined for the 7 finalists, vintages never subtracted across.
- [x] **Every set-aside name is in the ledger with a class AND a revival condition** — 10 rejections,
      0 with an empty condition, 0 permanent bans. No stored condition came true at this stage
      (HANDOVER §3a's three due rows — `EMR` `AME` `VLO` — belong to that stage and were named there).
- [x] **No name removed on narrative grounds while its measured flow still passed** — `RTX` is the
      case in point and it is **re-filed at lower conviction with a dated re-check**, not absent (§G-3).
- [x] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** — 7 rows
      from this stage, all with an entry condition, on top of the 11 PREMORTEM wrote earlier in the run
      (§G). The funnel is scored in both directions, and the screener's 10 surfaced names are disposed
      of **3 by rejection + 7 by miss, none left implicit**.
- [x] **Sizing language is consistent with the exposure state carried by HANDOVER §3c** — state `정상`,
      invested **81.0%**, ⚠ band deviation **−14.0pp**, `n=9`, row **unsettled/live**. Because the state
      and the band **disagree** and a correction is a human call (P5), **this sheet computes no size at
      all** and proposes no target; `--ic` is separately revoked by G6. **The sheet does not claim to
      fill a target it cannot verify, and says so rather than leaving the gap silent.**
- [x] **Linter run on this file** — `scripts/report_lint.py` (C1·C2·S6·D6): **0 findings**, 0 exemptions claimed. ⚠ Form only; a clean run is not a correct report.
- [x] **Zero buy/sell recommendation, zero direction, zero size (P4).**


---
---

# ⚠ APPEND-ONLY ADDENDUM — second BET pass, same date, same file

> **Why this is an addendum and not a rewrite.** A complete `BET_SHEET.md` (§0–§G + EXIT CHECK, 18
> names, 17 ledger rows) was written to this path at **23:53:32 KST** by a concurrent `industry_US`
> BET pass. The desk's standing rule from the 2026-06-30 collision is explicit: **when a completed file
> already exists at the globbed path, do not clobber it — append.** Everything above this line is that
> pass's work, unedited. Everything below is a second pass and **adds only what the base sheet does not
> contain.** No verdict, number or ledger row above is altered.
>
> **Same bindings apply and are restated so this block stands alone**: benchmark **`SPY`**, named
> inline on every relative figure · terminal settled bar **2026-08-18**, no 08-19 settled price ·
> every `delta` is **TWO sessions (08-14 → 08-18)** · the **🟢/🔴 tag, the new-🟢 count and shortlist
> membership are NOT evidence** (only 3 of 8 greens clear `vol_surge` 1.2; `RTX WMT ORCL MA BAC` are
> velocity-tagged on the axis `G1` revoked) · **`delta` may not be cited without its earned component**
> · **the book is the real KIS account** (`AVGO LITE NVDA ANET COHR ETN HPE MPC NUE PSX RTX T`; it does
> **not** hold `MET` or `NDAQ`) · `EA` is **not measurable** · G3 flippers `BRK-B` `CAT` `LIN`, and
> **COMM's flipper test is void** (it removes `GOOGL` and leaves `GOOG`; ex-both-classes `wflow`
> −0.289, ex-mega-platform **+0.222**).
> **Zero buy/sell. Zero position sizing.** "Influence" lines below grade **evidence quality**, never
> capital: **A** = carries a judgement alone · **B** = carries it with a named partner · **C** = may
> narrow a range, never move it.
>
> ⏱ **Live-tape quarantine.** This pass ran **KST 23:22–00:4x = ET 10:22–11:4x, US cash session LIVE.**
> Every settled figure (`flow_score`, `obv_norm`, RS20/RS60 vs `SPY`, `vol_surge`, `delta`, close) is
> from `SECTOR_FLOW_US.json` `asof 2026-08-18`. Every **multiple** is computed off a **live 08-19
> intraday quote** and is tagged `[live 08-19]`. Margins, revenue, consensus EPS and revision breadth
> are **not** price-derived and carry no such tag. `module_flow --positioning` is cited for
> short-interest stock, P/C, IV skew and implied move only; `module_chart --read` for **shape only**.

## ADD-0 · 🚨 The gap this addendum exists to close: **the ten erased runners appear nowhere in the base sheet, and neither does `S101`**

`BLINDSPOT_PREMORTEM` §4a measured ten names beating `SPY` that the `vol_surge` gate erased, and
recorded that **nine of the ten have zero mentions across all five of this run's documents.** Counted
against the base sheet above: **`DELL` 0 · `PANW` 0 · `SHOP` 0 · `ABNB` 0 · `PYPL` 0 · `DASH` 0 ·
`CRWD` 0 · `TMO` 0 · `BKNG` 0 · `AXON` 2 (both incidental) · the string `S101` 0.**
⇒ **The stage that was supposed to answer the blind-spot finding reproduced it.** `S101` (settles
**2026-08-26**) is the frozen bracket that scores exactly this, and its baskets are **not re-membered
here.** Below, **all ten are disposed of**: three carry full §A–§E blocks and **ten are filed to the
missed ledger** with an `--enters-if` and a `--recheck-date`.

**The ten, settled 2026-08-18, benchmark `SPY` inline** — `flow_score` · OBV `obv_norm` paired per
`RULE D6` with RS20/RS60 vs `SPY` · `vol_surge` read directly · two-session Δ:

| ticker | sector | flow | OBV | RS20 vs `SPY` | **RS60 vs `SPY`** | `vol_surge` | Δ (2-sess) | disposition |
|---|---|---|---|---|---|---|---|---|
| `DELL` | IT | +0.094 | 중립 −0.067 | +13.4 | ★ **+82.1** | 0.82 | −0.172 | **block + missed** |
| `AXON` | INDU | +0.511 | 매집 +0.323 | **+18.7** | **+55.7** | 0.72 | −0.145 | missed |
| `PANW` | IT | +0.023 | 중립 −0.053 | +6.8 | +44.6 | 0.73 | +0.186 | missed |
| `SHOP` | IT | +0.506 | 매집 +0.211 | **+16.6** | +36.5 | 0.71 | −0.055 | missed |
| `ABNB` | DISC | ★ **+0.717 (#2 on the board)** | 매집 +0.169 | ★ **+24.6** | +33.2 | **1.09** | −0.164 | **block + missed** |
| `PYPL` | FIN | +0.345 | 매집 +0.155 | +5.6 | +33.1 | 0.62 | +0.053 | missed |
| `DASH` | DISC | +0.594 | 매집 **+0.389** | +12.5 | +32.5 | 0.87 | −0.006 | **block + missed** |
| `CRWD` | IT | −0.108 | **분산 −0.129** | +8.8 | +28.1 | 0.69 | +0.298 | missed |
| `TMO` | HLTH | +0.461 | 매집 +0.266 | +10.0 | +27.8 | 0.63 | +0.126 | missed |
| `BKNG` | DISC | +0.455 | 매집 +0.157 | +13.5 | +27.1 | 0.63 | +0.152 | missed |

★ **The basket is not uniform and the sheet says so rather than treating "erased" as a thesis.**
**Seven of ten are OBV-accumulating with positive RS20 vs `SPY`; `DELL` and `PANW` are OBV-neutral and
`CRWD` is OBV-dispersing** — so three of the ten fail the desk's own accumulation test *before* the
volume gate is reached, and their inclusion in `S101`'s frozen basket is a property of the bracket, not
an endorsement. ⚠ Two of the ten (`PYPL`, `CRWD`) are also in the run's **5-name OBV instrument-conflict
set**, so no claim about either rests on OBV (`RULE D6`).
⚠ **Sector routing matters and is stated**: `ABNB` `DASH` `BKNG` are **Consumer Discretionary, held
N−**; `DELL` `PANW` `SHOP` `CRWD` are **IT, held N with no DEEP slot**; `TMO` is **Health Care, the one
sector promoted to N+ this run and excluded from DEEP on recency — a logged cost.** **None of the ten
sits in a sector this desk gave a mandate to**, which is a second, independent reason they were never
worked, and it is a different reason from the volume gate.

---

## ADD-1 · Erased runners — full blocks

### `ABNB` — Airbnb · travel services · Consumer Discretionary (N−) · **the strongest single name the gate erased**

**§A — numbers.** `[live 08-19]` P/E trailing **42.89** / forward **30.60** · PEG **1.97** · P/S
**8.55** · P/B **14.21**; `mcap` **$84.5bn** settled. Target mean **$174.73 vs the 08-18 settled close
$183.25 — the target sits 4.7% BELOW the tape**; mix 4 SB / 20 B / **18 H** / 2 S / 1 SS. Revenue
FQ2-2026 **$3.61bn, +16.5% YoY and +34.7% QoQ** — ⚠ **the sequential is northern-hemisphere travel
seasonality, not an acceleration**, and both halves are given (`RULE C2`). Consensus current-year
**5.29, +3.9% over 90 days**, 30-day breadth **24up/5down**; next year 6.18, +2.4%, **20up/11down**.
Gross margin **FY2025 83.0%, against its own 7-year record: max 83.1% (FY2024), min 74.1% (FY2020),
median 82.2%** ⇒ **the margin is at the top of its own (short) record**, so the peak-margin lens is
live and **no cheapness claim is made at 30.6x forward.**

**§B — thesis.** `ABNB` is the cleanest counter-example to the desk's own gate: **`flow_score` +0.717 is
the second-highest score on the entire 299-name board**, it is OBV-accumulating with **RS20 +24.6 and
RS60 +33.2 vs `SPY`**, and its `vol_surge` of **1.09** missed the 1.2 gate by 0.11 — the whole reason
it is absent from every document this run produced. It is **not** a name the desk rejected; it is a
name the desk never saw.
**[ALPHA-FRESHNESS: ____ ]**

**§C — flow / positioning cross-read.** Settled 08-18: `flow_score` **+0.717** · OBV **매집 `obv_norm`
+0.169**, paired per `RULE D6` with **RS20 +24.6 and RS60 +33.2 vs `SPY`**, and corroborated on a
second instrument: `module_chart ABNB --read` gives **CONFIRMED-TURN, OBV 20d 누적 +198%, no
divergence, bull stack 5>20>60>120, price 4 of 4 MAs above** — **both OBV instruments agree in sign.**
⚠ **RSI 78.4 with momentum20d +36.7% and a Bollinger width of 43.5% — extended, not early**;
`BLINDSPOT` §4b's own re-tag for this name is **EXTENDED-BUT-LIVE**. `vol_surge` **1.09**; Δ **−0.164**
against a Consumer Discretionary earned component of **−0.67** (i.e. the sector lost ground to `SPY`
while printing +0.51 — this name's negative Δ is the honest half of that board). Live positioning
(quarantined): short **3.1% of float, covering, DTC 3.9**; P/C **0.88**; skew **+31.5**; implied move
**±2.0% (D2, 2026-08-21)**.

**§D — competition / peers.** Against the other travel name in the ten, `BKNG`: `ABNB` leads on
`flow_score` (+0.717 vs +0.455), on OBV (+0.169 vs +0.157), on RS20 (+24.6 vs +13.5 vs `SPY`) and on
RS60 (+33.2 vs +27.1 vs `SPY`), and trails on valuation (30.6x vs `BKNG`'s cheaper forward) and on
margin history length. Against the whole erased basket it ranks **1st on `flow_score`, 1st on RS20 vs
`SPY`, and 4th on RS60 vs `SPY`.** ⚠ `BKNG`'s own margin percentile is **unmeasurable** —
`margin_history.py BKNG` returns FY2008–FY2017 only, ending nine fiscal years short — so the two cannot
be compared on that axis at all (C3).

**§E — refutation + dated catalyst.** **What kills this**: (i) **a record-area gross margin on a
seven-year record with the next-year revision breadth already split 20up/11down** — the denominator is
not confirming the price; (ii) an 18-Hold sell-side mix with a target mean **below** the tape; (iii)
RSI 78.4 and +36.7% 20-day momentum say the entry window, if there ever was one, is behind; (iv) the
sector routing — Consumer Discretionary is **N−** with an **earned** two-session excess of **−0.67 vs
`SPY`**, so the desk has no mandate that reaches this name. **Dated**: **`S101` settles 2026-08-26** and
`ABNB` is a frozen member of its erased basket (A ≥ +4.45pp ⇒ the gate is an alpha filter with the
wrong sign; B ≤ −3.88pp ⇒ the gate earned its keep; **state at registration −0.677, mid-band**); next
issuer print **2026-11-06**. **Influence: B** — two flow instruments agree and the RS evidence vs `SPY`
is A-grade, but the margin percentile and the extension are open, so it may not carry a judgement alone.

### `DASH` — DoorDash · specialized consumer services · Consumer Discretionary (N−)

**§A — numbers.** `[live 08-19]` P/E trailing **115.36** / forward **27.62** · PEG **4.69** · P/S
**5.98** · P/B **9.57**; `mcap` **$75.6bn** settled. Target mean **$251.94 vs the 08-18 settled close
$216.35 (+16.4%)**; mix 8 SB / 26 B / 10 H / 0 S. Revenue FQ2-2026 **$4.45bn, +35.6% YoY and +10.4%
QoQ** — **the strongest growth in the erased basket on both halves.** Consensus current-year **2.55,
−0.6% over 90 days**, 30-day breadth **14up/8down**; next year 4.46, **+1.5%**, **16up/6down**.
🚨 **Margin percentile `unknown` (C3)**: `scripts/margin_history.py DASH` returns *"연간 데이터 없음"*
— **the axis that separates "cheap on a growing denominator" from "peak-margin trap" does not exist for
this name on this instrument, so no cheapness claim is made at 27.6x forward.**

**§B — thesis.** `DASH` carries **the highest OBV reading of the entire erased basket (`obv_norm`
+0.389)** on the basket's fastest revenue line, and it is the only one of the ten whose two-session Δ
is essentially flat (**−0.006**) — i.e. it neither gained from the roll-off nor gave back.
**[ALPHA-FRESHNESS: ____ ]**

**§C — flow / positioning cross-read.** Settled 08-18: `flow_score` **+0.594** · OBV **매집 `obv_norm`
+0.389 — the basket's highest**, paired per `RULE D6` with **RS20 +12.5 and RS60 +32.5 vs `SPY`**, and
corroborated on a second instrument: `module_chart DASH --read` gives **CONFIRMED-TURN, OBV 20d 누적
+78%, no divergence, bull stack 5>20>60>120, price 4 of 4 MAs above** — **both OBV instruments agree.**
⚠ **RSI 74.0, momentum20d +29.5%, Bollinger width 28.7% — extended.** `vol_surge` **0.87**; Δ
**−0.006**. Live positioning (quarantined): short **4.4% of float, covering, DTC 4.8 — the highest
short stock and the highest days-to-cover in the erased basket**; P/C **0.39 — the most call-skewed
book among the ten**; skew **+7.0**; implied move **±3.3% (D2, 2026-08-21)**. ⚠ **A 4.4% short stock
being covered against a call-heavy option book is squeeze-shaped, and this sheet does not claim it is
one** — short *stock* and short *volume* are different objects (`D289`) and only one was read here.

**§D — competition / peers.** Within Consumer Discretionary's erased trio (`ABNB` `DASH` `BKNG`),
`DASH` has the best OBV and the fastest revenue and the worst valuation transparency. Against the
board, its `flow_score` +0.594 ranks it above every name on the LIVE shortlist except `KKR` (+0.757) —
**a name with a higher score than six of the eight shortlisted names was never mentioned once**, which
is the same measurement `ADD-0` makes at basket level, restated at name level.

**§E — refutation + dated catalyst.** **What kills this**: a **missing margin history** (C3) on a
115x trailing multiple; a current-year consensus that has **fallen 0.6% in 90 days** while the price
ran +32.5 vs `SPY` over 60 sessions; the extension (RSI 74.0); and the same Consumer Discretionary
routing problem as `ABNB` (**N−, earned two-session excess −0.67 vs `SPY`**). **Dated**: **`S101`
settles 2026-08-26**; next issuer print **2026-11-05**. ⚠ `S101`'s own anti-signal is an earnings print
at ≥3 of the ten inside the window ⇒ **VOID**; `DASH`'s print is outside it. **Influence: B.**

### `DELL` — Dell Technologies · computer hardware · IT (N) · **the largest RS60 vs `SPY` on the board**

**§A — numbers.** `[live 08-19]` P/E trailing **34.39** / forward **19.51** · PEG **0.81** · P/S
**2.08** · **P/B −199.67 — negative book value; the P/B is not a valuation statistic for this name and
is not used.** `mcap` **$264.6bn** settled. Target mean **$506.61 vs the 08-18 settled close $468.65
(+8.1%)**; mix 5 SB / 14 B / 8 H / 0 S. Revenue latest reported **$43.84bn, +87.5% YoY and +31.4%
QoQ** — ⚠ **both halves are extraordinary and both are stated; the XBRL cross-check covers only 1
common quarter (0.00% difference), which is a thin check and is labelled as one.** Consensus
current-year **18.64, +43.4% over 90 days**, 30-day breadth **3up/0down**; next year 19.30, **+53.1%**,
**1up/0down** — ⚠ **a one-analyst next-year panel is not breadth and is not read as one.**
Margin percentile: **not run this stage ⇒ `unknown` (C3)**; **no cheapness claim is made at 19.5x
forward.**

**§B — thesis.** `DELL` is the extreme case of the blind-spot finding: **RS60 +82.1 vs `SPY` is the
single largest 60-session relative performance on the 299-name board**, and it appears in **zero** of
this run's six documents including the base sheet above. It is also the case that **most tests the
desk's own gate would have applied to it fail** — which is why it is written up rather than promoted.
**[ALPHA-FRESHNESS: ____ ]**

**§C — flow / positioning cross-read.** Settled 08-18: `flow_score` **+0.094 — near zero, and the
lowest of the seven erased names with positive OBV-or-RS evidence** · OBV **중립 `obv_norm` −0.067 —
NOT accumulating**, paired per `RULE D6` with **RS20 +13.4 and RS60 +82.1 vs `SPY`**. 🚨 **Instrument
conflict, recorded**: `module_chart DELL --read` returns **누적 +36%** against the sweep's 중립
−0.067 — a sign disagreement, and per `SECTOR_DEEP_MATR` §7c the settled reconstruction of OBV agrees
with the sweep on 12 of 12 names when the live bar is excluded, so **the disagreeing instrument is the
one carrying an in-progress 08-19 bar.** Recorded, not resolved; **no claim here rests on OBV.**
`module_chart` also returns **PULLBACK-TO-SUPPORT**, price only **2 of 4 MAs above**, RSI **55.5**,
momentum20d **−1.7%**, trigger `close > 443.76`, swing stop 369.64. `vol_surge` **0.82**; Δ **−0.172**.
Live positioning (quarantined): short **4.4% of float, BUILDING, DTC 2.0**; P/C **0.72**; skew
**+28.1**; implied move **±5.2% (D2, 2026-08-21)**.
🚨 **A live observation for the settling desk, quarantined and not used here**: `DELL` traded **431.89
at 23:2x KST against its 08-18 settled close of 468.65 = −7.8% intraday.** `DELL` is a frozen `S101`
basket member; **this is not a close and it is not read as tracking anything.**

**§D — competition / peers.** Against `HPE` — the book's own hardware line — `DELL` has the larger
RS60 vs `SPY` (**+82.1 vs +60.6**) and the **weaker** flow (**+0.094 vs +0.594**) and the weaker OBV
(**중립 −0.067 vs 매집 +0.303**). ⇒ **The desk already owns the better-flowing half of this pair**, and
that is the most useful thing this block establishes. Within the erased basket `DELL` is 1st on RS60
vs `SPY` and **8th of 10 on `flow_score`.**

**§E — refutation + dated catalyst.** **What kills this**: **OBV is neutral and the price momentum has
already rolled** (momentum20d −1.7%, only 2 of 4 MAs above, a trigger 5.4% above the settled close that
has not been taken); a next-year revision panel of **one analyst**; negative book value; a **building**
short stock; and IT holds no DEEP slot this run. ⇒ **The largest RS60 vs `SPY` on the board is also one
of the weakest current-flow readings among the ten — those two facts belong in the same sentence.**
**Dated**: **`S101` settles 2026-08-26**; **next issuer print 2026-09-02, which is INSIDE nothing that
settles first** and is the nearest dated catalyst of the whole erased basket. **Influence: C** — one
axis (long-window RS vs `SPY`), a contradicting second (OBV/structure), and a thin third (revisions).

---

## ADD-2 · Per-sector §A–§E the base sheet does not carry

The base sheet's §A works 18 names. These five surfaced in the wide net — `us_setup_screener --sector`
hits and DEEP thesis leaders — and are absent from it.

### `TRGP` — Targa Resources · midstream · **ENRG (OW)** · the sector's largest Δ, and the Δ is the problem

**§A.** `[live 08-19]` P/E trailing **28.21** / forward **24.50** · PEG **1.25** · P/S **3.78** · P/B
**20.18**; target mean **$301.81 vs the 08-18 settled close $297.77 (+1.4%)**; mix 6 SB / 14 B / 3 H.
Revenue FQ2-2026 **$4.44bn, +4.2% YoY and +8.4% QoQ — the slowest growth of any Energy name worked in
either pass, on both halves**; **XBRL vs yfinance 0.00% across 4 quarters.** Consensus current-year
**11.47, +2.7% over 90 days, breadth 1up/1down**; next year 12.03, +1.7%, **1up/2down** ⚠ **an almost
empty revision panel — two analysts is not a trend.** 🚨 **Gross margin FY2025 38.3% — the HIGHEST of
its own 10-year record** (FY2016–2025; min 11.5% FY2017, median 24.6%). **Record margin + flat
denominator ⇒ no cheapness claim is available and none is made.**

**§B.** There is no midstream thesis on this desk. `TRGP` is here because it produced **the largest
two-session `flow_score` delta in Energy (+1.066)** and **the best 5-session excess vs `SPY` of any
Energy name (+12.6, better than `MPC`'s +9.3)** — and a wide net that dropped it would be selecting on
the story rather than on the data. **[ALPHA-FRESHNESS: ____ ]**

**§C.** Settled 08-18: `flow_score` **+0.252** · OBV **중립 `obv_norm` +0.063 — NOT accumulating**,
paired per `RULE D6` with **RS20 +3.7 and RS60 +6.9 vs `SPY`** ⇒ ★ **the move is price-and-score, not
accumulation.** `module_chart TRGP --read` **agrees on the OBV sign** (중립, 20d slope −10%) while
printing **BREAKOUT**, bull stack 5>20>60>120, price 4 of 4 MAs above, RSI 66.7, and a **bullish**
divergence — the two instruments agree on OBV and disagree on what to call the structure.
`vol_surge` **0.94**. Live positioning (quarantined): short **2.5% of float, covering, DTC 3.8**; P/C
**0.12 — the most call-skewed book in this addendum**; implied move **±3.3% (D2, 2026-08-21)**.
🚨 **Its Δ of +1.066 is exactly the number that may not be read alone.** Energy is the one sector whose
Δ was **earned** (+3.75 earned against a −0.56 roll-off drag), but **no per-name earned/roll-off split
exists**, so the honest statement is that `TRGP`'s Δ is **undecomposed**, not that it is earned.

**§D.** Midstream node `KMI TRGP OKE WMB`: **EW 5-session excess vs `SPY` +7.04, the #2 node in the
sector**, off an EW 60-session of **−0.82 vs `SPY`**; `OKE` Δ +0.580 and `DVN` Δ +0.675 are the next
largest deltas. **A laggard node closing, not a leader extending.** ⚠ **No lead/lag relationship
between midstream and refining was measured this run; any such claim would be `[unverified]`.**

**§E.** **What kills this**: a record gross margin, a two-analyst revision panel, a **neutral** OBV, and
an undecomposable Δ — the only live axis is price. **Dated**: next issuer print **2026-11-05**; **there
is no dated `TRGP` catalyst inside 60 days**, which is itself the finding. **Influence: C.**

### `COP` — ConocoPhillips · E&P · **ENRG (OW)** · the control on the refining thesis

**§A.** `[live 08-19]` P/E trailing **17.45** / forward **14.12** · PEG **1.00** · P/S **2.46** · P/B
**2.43**; target mean **$144.50 vs the 08-18 settled close $129.72 (+11.4%)**; mix **4 SB / 15 B / 6 H
/ 0 S**. Revenue FQ2-2026 **$19.16bn, +36.8% YoY and +21.6% QoQ**; **XBRL vs yfinance 0.00% across 4
quarters.** Consensus current-year **10.28, +8.7% over 90 days, breadth 6up/1down**; next year 9.32,
+3.9%, **5up/6down — the near year is being raised and the out year is split**, and both are stated.
★ **Gross margin FY2025 56.9% against its own 10-year median 57.1%** (max 63.6% FY2019, min 40.9%
FY2020) ⇒ **at its median, so the peak-margin lens does NOT fire — the one thing `COP` has that `MPC`
does not.**

**§B.** `COP` is the **control** on the refining thesis rather than a version of it: integrateds hold
the barrel, refiners hold the spread, and the node split (**+4.15 vs +8.89 EW 5-session excess vs
`SPY`**) is the discriminator that needs no Brent threshold at all. **[ALPHA-FRESHNESS: ____ ]**

**§C.** Settled 08-18: `flow_score` **+0.586 (Energy rank 3)** · OBV **매집 `obv_norm` +0.336 — the
highest of the seven Energy accumulators**, paired per `RULE D6` with **RS20 +7.8 and RS60 +4.3 vs
`SPY`**, and corroborated on a second instrument: `module_chart COP --read` gives **CONFIRMED-TURN,
OBV 20d 누적 +20%, price 4 of 4 MAs above, RSI 72.9** — **both OBV instruments agree.** 🚨 The same
chart also prints a **bearish divergence (price HH · RSI LH)** — the identical shape `MPC` carries.
`vol_surge` **0.87**; Δ **+0.054**. ⇒ **the sector's strongest accumulation reading sits on its weakest
RS60 vs `SPY` among the leaders**, and both halves are stated because either alone would mislead.

**§D.** Against `XOM` (`obv_norm` +0.094, RS20 +6.6, RS60 +3.3 vs `SPY`) and `CVX` (+0.289, +5.1,
+4.4 vs `SPY`), `COP` leads the integrated/E&P complex on both OBV and RS20 vs `SPY`; against the
refiners it trails RS60 vs `SPY` by 30–40pp. **The E&P node's EW 60-session excess vs `SPY` is +0.97
against refining's +40.84.**

**§E.** **What kills this**: `BLINDSPOT` §3b measured `XLE` at **−0.233pp per 1% Brent decline**, and
`S95` branch B (Brent 91.02 → ≤86.50) maps to **`XLE` −1.56pp**; a barrel break hurts `COP` **more
directly** than the refiners because it has no spread to widen into it. The divergence is unresolved.
**Dated**: `S95`/`P69` settle **2026-08-21** on `BZ=F` (A ≥93.00 · B ≤86.50; **91.02 at the settle, C
and moving toward A**); next issuer print **2026-11-05**. **Influence: B.**

### `STLD` — Steel Dynamics · **MATR (N−)** · the sector's cleanest peak-margin pass, and its only rising short

**§A.** `[live 08-19]` P/E trailing **23.11** / forward **12.96 — the lowest forward multiple in
Materials** · PEG **11.95** · P/S **1.72** · P/B **3.76**; target mean **$272.64 vs the 08-18 settled
close $249.81 (+9.1%)**; mix 2 SB / 7 B / 4 H / 1 S. Revenue FQ2-2026 **$6.09bn, +33.4% YoY and +17.0%
QoQ**; **XBRL vs yfinance 0.00% across 4 quarters.** Consensus current-year **16.76, +11.0% over 90
days, 30-day breadth 6up/2down**; next year 19.02, +10.9%, **5up/5down**. ★ **Gross margin FY2025
13.2%, BELOW its own 19-year median of 14.8%** (max 29.1% FY2021, min 9.6% FY2015) ⇒ **below-median
margin + rising denominator + the sector's lowest multiple = the cleanest pass of the peak-margin test
in Materials.**

**§B.** The same index-linked steel mechanism the desk owns through `NUE`, one notch cheaper and one
notch weaker on flow — and **the only name in Materials being shorted more while it gets cheaper.**
That disagreement is the block's content; it is stated and **not resolved.**
**[ALPHA-FRESHNESS: ____ ]**

**§C.** Settled 08-18: `flow_score` **+0.322** · OBV **매집 `obv_norm` +0.317**, paired per `RULE D6`
with **RS20 +4.4 and RS60 +4.4 vs `SPY`**. `vol_surge` **0.65**; Δ **−0.025** against a Materials
earned component of **−0.66** (the sector lost ground to `SPY` while printing +0.75). 🚨
**Second-instrument conflict, recorded**: `module_chart STLD --read`, run with the 08-19 session open,
returns **분산, OBV 20d slope −45%**, **PULLBACK-TO-SUPPORT**, price **1 of 4 MAs above**, RSI **44.8**,
coiling 11.7%, trigger `close > 251.46` against a settled close of **249.81 — 0.7% below, and no 08-19
close exists to test it.** Per `SECTOR_DEEP_MATR` §7c the settled OBV reconstruction agrees with the
sweep on **12 of 12** Materials names, so this is most likely the same clock artifact; recorded, not
resolved, and **no claim here rests on OBV.** Live positioning (quarantined): short **3.6% of float,
BUILDING, DTC 3.4 — the only Materials name with rising short interest**; P/C **0.50**; skew **+9.8**;
implied move **±3.2–3.3% (D2, 2026-08-21)**.

**§D.** `STLD` is **the 3rd-worst name in `S77` (5-session excess vs `SPY` −4.860)** while carrying the
sector's best valuation configuration. Against `NUE`: cheaper (12.96x vs 14.15x forward), lower margin
percentile (below median vs **at** its 19-year median 11.9%), weaker flow (+0.322 vs +0.483), weaker
RS60 vs `SPY` (+4.4 vs +13.3). **One of the two sides — the multiple or the short build — is wrong.**

**§E.** **What kills this**: the rising short stock against a falling multiple; a structure that has
not triggered; and the shared HRC-rate risk (`HRC=F` QoQ rate in its second decline, +14.5 → +10.6 →
+7.7p, printing **2026-10-01**). **Dated**: `S77` settled **tonight 2026-08-19**; **`STLD` is the
sector's next issuer print, 2026-10-19 — the first in roughly nine weeks**, because all 12 Materials
names last reported 07-20 → 07-31. **Influence: B.**

### `ECL` — Ecolab · specialty chemicals · **MATR (N−)** · the sector's sharpest price-vs-flow disagreement

**§A.** `[live 08-19]` P/E trailing **38.30** / forward **30.24 — the highest forward multiple in
Materials** · PEG **2.85** · P/S **4.75** · P/B **7.95**; target mean **$324.67 vs the 08-18 settled
close $280.00 (+16.0%)**; mix 5 SB / 15 B / 5 H / 0 S. Revenue FQ2-2026 **$4.42bn, +9.7% YoY and +8.6%
QoQ**; **XBRL vs yfinance 0.00% across 4 quarters.** Consensus current-year **8.17, −3.1% over 90
days**, 30-day breadth **7up/4down**; next year 9.43, **−2.2%**, 9up/5down. ★ **Gross margin FY2025
44.5% — exactly its own median 44.5%** (max 50.8% FY2007, min 37.8% FY2022) ⇒ **median margin, FALLING
denominator, highest multiple in the sector: no "cheap" claim is available and none is made.**

**§B.** `ECL` is on this sheet for one reason: it carries **the best two-session `flow_score` delta in
Materials, +0.628 — rank 5 of all 299 scored names** — against a **5-session excess vs `SPY` of
−1.223**. **[ALPHA-FRESHNESS: ____ ]** ⚠ `chain-hop "copper smelter"` and `"steel tariff"` scanned
**0 and 1 articles** against **114 `copper` and 68 `steel` FTS hits** in the same minutes — an
instrument defect reproducing for the second consecutive Materials run, so **no Materials chain-hop
null may be read as theme absence** and no theme claim is made here.

**§C.** Settled 08-18: `flow_score` **+0.436** · OBV **매집 `obv_norm` +0.144**, paired per `RULE D6`
with **RS20 +3.4 and RS60 +8.6 vs `SPY`**. `vol_surge` **0.99 — the Materials sector maximum, and still
0.21 short of the gate**, which is why the sector's zero-green count is an artifact and may not be read
as weakness. 🚨 **Second-instrument conflict**: `module_chart ECL --read` returns **분산, OBV 20d slope
−15%** and **NEUTRAL/CHOP**, price 4 of 4 MAs above, RSI 58.9, coiling 8.7% — same clock caveat as
`STLD`; recorded, not resolved. Live positioning (quarantined): short **1.3% of float, covering, DTC
2.5**; P/C **1.15**; skew **+5.5**; implied move **±3.5% (D2, 2026-08-21)**.
🚨 **Materials' earned component is −0.66**, so a large positive per-name Δ in this sector is precisely
the shape roll-off produces — **the one axis carrying this name is the contaminated one.**

**§D.** Coatings/hygiene node `SHW`+`ECL`: **EW 5-session excess vs `SPY` −3.037** off an EW 60-session
of **+8.438 — the sector's second-best long-window node.** `SHW` is the better name on flow (+0.407,
OBV 매집 +0.174, RS20 +5.9 vs `SPY`) and on revisions (**21up/0down, the sector's cleanest**) and worse
on margin position (near its own FY2016 max of 49.9%). ⇒ **inside one node, one name has the clean
denominator and the peak margin and the other has the median margin and the falling denominator.**

**§E.** **What kills this**: a falling consensus on the highest multiple in the sector, with the only
supporting axis a Δ that may not be read alone, plus an unresolved OBV conflict. **Dated**:
`SECTOR_DEEP_MATR` §9 KPI 7 tests exactly this — **whether `delta` leads price at a two-session
horizon** — and resolves at the next `asof` advance; next issuer print **2026-10-27**. **Influence: C.**

### `VZ` — Verizon · **COMM (UW)** · the second leg of the node the gate cannot see

**§A.** `[live 08-19]` P/E trailing **12.89** / forward **9.37** · PEG **0.92** · P/S **1.48** · P/B
**1.98** · dividend yield **5.83% — the highest worked in either pass**; target mean **$51.56 vs the
08-18 settled close $48.54 (+6.2%)**; mix 3 SB / 8 B / **15 H** / 0 S. Revenue FQ2-2026 **$34.25bn,
−0.73% YoY and −0.54% QoQ — both halves negative**; **XBRL vs yfinance 0.00% across 4 quarters.**
Consensus current-year **5.01, +1.2% over 90 days, 30-day breadth 22up/0down — the cleanest in the
sector**; next year 5.28, +0.1%, **13up/8down**. 🚨 **Margin percentile `unknown` (C3)**:
`margin_history.py VZ` returns **FY2007–FY2017 only**, and the series carries a **definition break**
(58.6% through FY2012, then 86.4% in FY2013) that makes even the in-window median unusable.
**No cheapness claim is made at 9.37x forward.**

**§B.** The second leg of the telecom node that has been invisible to the desk's gate for six
consecutive settled tapes — and the cheaper one on every usable multiple. **[ALPHA-FRESHNESS: ____ ]**

**§C.** Settled 08-18: `flow_score` **+0.400** · OBV **매집 `obv_norm` +0.180**, paired per `RULE D6`
with **RS20 +8.3 and RS60 −2.8 vs `SPY`**. `vol_surge` **0.52 — the second-lowest in the sector**, and
**the sector maximum is 0.91**, so **low-turnover mega-cap telcos structurally cannot clear a
volume-surge gate.** Δ **+0.056** against a COMM earned component of **−0.23** (the sector lost ground
to `SPY` while printing +1.04). ⚠ **Three-way instrument conflict, same shape as `T`**: `module_chart
VZ --read` reads **분산, 20-day OBV slope −28%, bearish divergence**, RSI **75.1**, price 4 of 4 MAs
above — against the sweep's 매집 +0.180. ⇒ **the accumulation is OLDER than 20 days and the last 20
sessions are price-up-on-declining-OBV.** Live positioning (quarantined): short **2.0% of float,
covering, DTC 2.5**; P/C **0.80**; skew **+19.5**; implied move **±2.6% (D2, 2026-08-21)**. FINRA
short-volume z **−1.43, 5v5 −9.6 falling.**

**§D.** Telecom-ex-`TMUS` (`T VZ CMCSA`, 3.6% of sector cap): **`eqflow` +0.404 — the sector's best
node — 3 of 3 OBV-accumulating, median RS20 +8.3 vs `SPY`**, against the mega-platform node at
`eqflow` **−0.567, 0 of 3 accumulating, median RS60 −14.3 vs `SPY`**. ★ **That node `eqflow` has been
above +0.25 on six distinct settled tapes and the sector was held UW at every one** — the 08-14 file's
anti-signal 3, **fired 6 of 6.** Against `T`: `VZ` is cheaper and higher-yielding, with **worse revenue
on both halves** (−0.73% YoY / −0.54% QoQ vs `T`'s +2.30% / +0.16%), a cleaner current-year breadth
(22up/0down vs 15up/3down), weaker OBV (+0.180 vs +0.291) and weaker RS20 vs `SPY` (+8.3 vs +9.3).
⚠ `CMCSA` has the node's best Δ (+0.107) and the only **positive** RS60 in it (+1.1 vs `SPY`) at
forward P/E **7.42**, but `margin_history.py CMCSA` returns *"연간 데이터 없음"* ⇒ **its cheapness is
unmeasurable too (C3)**, and its next-year breadth is **4up/15down**.

**§E.** **What kills this**: revenue shrinking on both halves; a 15-Hold mix; the 20-day OBV slope; and
🚨 **the frame that would dress this node as scarcity does not exist** — the `T` FY2025 10-K returns
**0 hits** for remaining performance obligation, take-or-pay, backlog, tower, IRU and regulated rate,
and the genuine tower/lease analogue is classified **outside this sector** (`AMT` `CCI`, GICS Real
Estate, which this desk holds UW). ⇒ **the node's positive flow is a price-and-carry reading, not a
contract reading.** **Dated**: next issuer print **2026-10-20**; the node's own anti-signal —
telecom-ex-`TMUS` `eqflow` falling below +0.25 while `T`/`VZ` 20-day OBV slopes stay negative —
resolves at the next `asof` advance. **Influence: C.**

---

## ADD-3 · Epicenter-starter — restated, because the base sheet and this pass measured the registry differently

Both passes agree on the verdict and **disagree on one number**, and both readings are left standing.
**Verdict: `CYCLE_EXPOSURE.md` flags no top-rank cycle GAP** (AI-compute epicenter **19.82%** vs a
12.0% floor; Energy/refining **9.64%** vs 8.0%; missile-defense **5.97%** with no threshold set) ⇒
**no epicenter-starter module is required this run and none is written by either pass.**
**The caveat that changes what the ✅ means**, from `BLINDSPOT_PREMORTEM` Lens 4 and carried here as the
mandate requires: the registry covers **62.4% of invested capital**, is **33 days stale**, and has **no
entry for optical/interconnect — which is 16.28% of invested via `LITE` (12.01%) + `COHR` (4.27%),
larger than the registered rank-2 Energy epicenter (`PSX`+`MPC` = 15.45%) and larger than defense
(`RTX` 9.60%).** A cycle absent from the registry cannot produce a GAP flag, so ✅ reads **"no gap among
the cycles we listed"**, not "no gap".
⚠ **Open numeric disagreement, not resolved here**: the base sheet's §F measures the unregistered set as
**`LITE` + `COHR` + `HPE` = 23.93% of invested** on a live 23:52 KST evaluation and re-states `T` as
**9.74%** with **9.59% belonging to `RTX`**; the PREFLIGHT G5 correction and `BLINDSPOT` Lens 4 read
`T` at **9.59%** and `RTX` at **9.60%** — **adjacent rows, and the two passes read them in opposite
order.** The **magnitude** is identical on either reading (`T` is ~9.6–9.7% of invested and unlabelled);
**only the digit differs, and it is left visible rather than silently harmonised.** Registry editing is
a human call (P5).

---

## ADD-4 · Ledgers filed by this pass — additive only, no row above is touched

**The base pass filed 17 rows (10 rejections + 7 missed) and they stand unchanged.** This pass adds
**11 missed rows**, all with `--enters-if` and `--recheck-date`, and **files zero rejections** — every
name below was set aside by a *gate*, not by a measurement, which is what the missed ledger is for.
⚠ **The boundary is machine-enforced**: `missed_ledger` refuses a ticker×date already present in the
rejection ledger, so `CAT` `GWW` `CTVA` `CRH` `MNST` `META` `KMI` `CSCO` `MA` `BAC` — the base pass's
rejections — are **structurally unavailable** to this pass and none was attempted.

| Ticker | Class | Why it never reached a decision | Enters if | Re-check |
|---|---|---|---|---|
| `ABNB` | M.숏리스트탈락 | `flow_score` **+0.717 = #2 on the 299-name board**, OBV 매집 with **RS20 +24.6 / RS60 +33.2 vs `SPY`**, erased by `vol_surge` **1.09** missing the 1.2 gate by 0.11 | `vol_surge` ≥ 1.2 with OBV still 매집 and RS20 vs `SPY` > 0 | **08-26** (`S101`) |
| `DASH` | M.숏리스트탈락 | highest OBV of the erased ten (**+0.389**) with **RS20 +12.5 / RS60 +32.5 vs `SPY`**; `vol_surge` 0.87 | same | **08-26** |
| `DELL` | M.숏리스트탈락 | **RS60 +82.1 vs `SPY` — the largest on the board** — against OBV **중립 −0.067** and `flow_score` +0.094 | OBV turns 매집 on a settled sweep while RS20 vs `SPY` > 0 | **08-26** |
| `AXON` | M.숏리스트탈락 | **RS20 +18.7 / RS60 +55.7 vs `SPY`** with OBV 매집 +0.323 replicating on both instruments; `vol_surge` 0.72 | `vol_surge` ≥ 1.0 with OBV still 매집 | **08-26** |
| `SHOP` | M.숏리스트탈락 | `flow_score` +0.506, OBV 매집 +0.211, **RS20 +16.6 / RS60 +36.5 vs `SPY`**; `vol_surge` 0.71 | `vol_surge` ≥ 1.0 with OBV still 매집 and RS20 vs `SPY` > 0 | **08-26** |
| `BKNG` | M.숏리스트탈락 | `flow_score` +0.455, OBV 매집 +0.157, **RS20 +13.5 / RS60 +27.1 vs `SPY`**; `vol_surge` 0.63 | same | **08-26** |
| `TMO` | M.숏리스트탈락 | `flow_score` +0.461, OBV 매집 +0.266, **RS20 +10.0 / RS60 +27.8 vs `SPY`**; Health Care was promoted to **N+** this run **and excluded from DEEP on recency — a logged cost** | Health Care receives a DEEP slot, **or** `vol_surge` ≥ 1.0 with OBV still 매집 | **08-26** |
| `PYPL` | M.숏리스트탈락 | OBV 매집 +0.155 with **RS60 +33.1 vs `SPY`**, but `mcap` **$37.5bn** and it is one of the run's 5 OBV instrument-conflict names | OBV agrees across both instruments **and** RS20 vs `SPY` > +5 | **08-26** |
| `PANW` | M.숏리스트탈락 | **RS60 +44.6 vs `SPY`** with OBV **중립 −0.053** — no accumulation to pair the momentum with (`RULE D6`) | OBV turns 매집 while RS20 vs `SPY` > 0 | **08-26** |
| `CRWD` | M.숏리스트탈락 | **RS60 +28.1 vs `SPY`** against OBV **분산 −0.129** and `flow_score` −0.108; also an OBV-conflict name | OBV turns 매집 while RS60 vs `SPY` stays > +20 | **08-26** |
| `NEM` | M.숏리스트탈락 | Materials' **best RS20 (+22.8 vs `SPY`)** and **lowest multiple (11.77x)**, but the denominator is being cut (**−9.0% / 90d, 30-day breadth 1up/11down**) and `margin_history.py NEM` returns no data ⇒ **cheapness is unmeasurable (C3)**; gold's QoQ rate has **two complete declines** | margin series resolves, **or** current-year breadth turns net-positive with RS20 vs `SPY` > 0 | **09-16** |

**Re-filed rather than deleted — `COHR`.** Already filed twice today (`R.타이밍대기` re-check 08-26 by
EVENT_ALPHA; `M.숏리스트탈락` by the Card-1 pass). **Its flow gate still passes — `vol_surge` 1.70 is
rank 1 of all 299 names — and only the story leg moved**, so per the standing rule it is **re-stated
with a new thesis line rather than removed**: settled 08-18 `flow_score` **+0.254**, OBV **매집
`obv_norm` +0.082**, **RS20 −6.0 and RS60 −22.3 vs `SPY`**, and **Δ −0.733 — the second-worst
two-session delta in the entire universe.** ⚠ **It is 4.27% of invested and sits in the
optical/interconnect node the registry does not carry (ADD-3).** No new row is written; the existing
08-26 re-check governs.

---

## ✅ EXIT CHECK — this addendum only

- [x] **Base sheet preserved byte-for-byte.** A completed file existed at the globbed path; per the
      2026-06-30 collision rule this pass **appended and did not clobber**. Filename unchanged, one
      file, per-sector material added.
- [x] **The run's own blind-spot finding is engaged, not repeated.** All ten erased runners are
      disposed of — **3 full §A–§E blocks + 10 missed-ledger rows** — and `S101`'s settle date
      (**2026-08-26**) and frozen baskets are named. The base sheet mentioned none of them; that gap is
      measured in ADD-0 rather than described.
- [x] **Per-sector §A–§E added for five names the base sheet does not carry** — `TRGP` `COP` (ENRG),
      `STLD` `ECL` (MATR), `VZ` (COMM) — each with multiples, growth on **both halves**, margin
      position in its own history **or** an explicit `unknown` (C3), a flow/positioning cross-read, a
      peer set and a dated refutation.
- [x] **Blanks are blanks.** `DASH` and `CMCSA` margin history: **`unknown` (C3)**. `VZ` margin series
      ends FY2017 **with a definition break** ⇒ unusable. `NOC`, `RTX`, `T`, `BKNG` margin percentiles:
      **unmeasurable on this instrument.** `DELL` P/B is **negative and not used**. No blank is guessed.
- [x] **Benchmark `SPY` named inline on every relative figure; every OBV reading is paired with RS20 or
      RS60 vs `SPY` in the same paragraph (`RULE D6`); every YoY carries its sequential (`RULE C2`).**
- [x] **Every Δ is labelled two-session and carried with its sector's earned component** — Energy
      **+3.75 earned**, COMM **−0.23**, MATR **−0.66**, INDU **−0.48**, DISC **−0.67**. No name is
      carried on Δ alone.
- [x] **Instrument conflicts recorded, not resolved to the convenient side** — `DELL`, `STLD`, `ECL`,
      `VZ` all show a sweep-vs-`module_chart` OBV sign disagreement, and each is attributed to the live
      08-19 bar with the settled 12-of-12 reconciliation cited, then set aside.
- [x] **Live-tape quarantine held.** Every multiple is tagged `[live 08-19]`; `DELL`'s −7.8% intraday
      print is recorded for the settling desk and used for nothing.
- [x] **Epicenter-starter: not required, said explicitly**, with the 62.4% registry-coverage caveat and
      the 16.28%-of-invested optical hole carried — and the base pass's conflicting `T`/`RTX` digit left
      visible rather than harmonised.
- [x] **Zero buy/sell language. Zero position sizing.** Influence grades A/B/C describe evidence
      quality only.

---

## ⚠ ORCHESTRATOR NOTE — the "concurrent pass" attribution is UNPROVEN and probably wrong

*(Appended by the run orchestrator after both passes closed. **No content above this line is
altered** — the append-only handling was the correct action regardless of what caused the collision,
which is exactly why it is the standing rule.)*

The addendum attributes the base sheet to *"a concurrent `industry_US` BET pass"* that wrote at
**23:53:32 KST**. **This run launched exactly one BET pass**, and the following is what can actually
be checked from here:

| Check | Result |
|---|---|
| BET passes launched by this run | **1** |
| `run_protocol.py industry_us --status` | **one run**, single state, at stage 9/11 |
| Other `industry_US` outputs written to `llm_outputs/2026-08-19/industry_US/` outside this run's sequence | **none found** |
| The two passes' own clock lines | base **23:35–00:20**; addendum **23:22–00:4x** — the addendum pass *started earlier* and finished later |

⇒ **The most likely explanation is a self-collision misread as a sibling desk**: the same pass wrote a
complete draft, hit a modified-file state on a later write, and attributed its own artifact to another
run. That cannot be proven from here, and it is recorded as **unproven rather than resolved**.

**Why it matters even though the content does not change**: a future run reading this file would
otherwise conclude that **two `industry_US` desks ran concurrently on 2026-08-19** and could invoke
the concurrent-collision playbook on a false premise. **They did not, so far as this run can
establish.** ⇒ Registered as dig **`D294`** — *a pass that finds an unexpected file at its own output
path must record the file's mtime **and** whether its own prior write could account for it, before
attributing the write to another desk.*

★ **What the collision handling got right, and it is worth keeping**: faced with a complete file at a
globbed path, the pass **appended and did not clobber**, restated its bindings so the block stands
alone, and altered no verdict, number or ledger row above it. **That is the correct behaviour whether
the other writer was a sibling desk or itself.**

### Ledger reconciliation, verified independently from the ledger files (not from either pass's prose)

**`out/reject_ledger.jsonl` — 13 rows dated 2026-08-19** (`000810` `CAT` `GWW` `CTVA` `CRH` `MNST`
`META` `KMI` `CSCO` `MA` `BAC` `XOM` `FCX`; `000810` belongs to the sibling KR desk, which shares the
ledger). **`out/missed_ledger.jsonl` — 22 rows dated 2026-08-19**, of which **three were filed earlier
in this run** (`TSLA`, `COHR` at EVENT_ALPHA/PREMORTEM) and **`103590`/`011200` belong to the KR desk**.
**Every row carries both a revival/entry condition and a re-check date** — the script enforces it.

★ **All ten erased runners are on the missed ledger with a 2026-08-26 re-check — the same date `S101`
settles.** `DELL` `PANW` `SHOP` `ABNB` `PYPL` `DASH` `CRWD` `TMO` `BKNG` `AXON`. **The gap that
`S101` was registered to punish is now closed in the one place that will be re-read automatically.**
