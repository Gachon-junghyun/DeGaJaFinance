# SECTOR_DEEP_INDU — Industrials / Defense-Aerospace — 2026-07-22

> **DEEP slot ③, PROMOTED BY THE PRE-MORTEM** (BLINDSPOT_PREMORTEM Third Finding), not selected by
> ROTATION. Reason for promotion: ROTATION cut Industrials **N+ → N−** on a 50-name sector number
> ~24 hours before the sector's only dated catalysts (**RTX + LMT, 2026-07-23**), and the best RS pair
> in all 50 names (**AXON**) was never mentioned by any stage of this run.
> ROTATING pick — full fresh map. Priors read, not deltaed: `2026-07-21/US_2/SECTOR_DEEP_20DEF.md`,
> `2026-07-15/industry_US/SECTOR_DEEP_INDU.md`.
> **Every RS figure below is vs SPY**, asof `SECTOR_FLOW_US.json` **2026-07-21 close**. Fundamentals
> pulled 2026-07-22 (`module_fundamentals_us --json`). FINRA short-vol asof 2026-07-21.
> Written **06:5x ET, US session not open.** Zero buy/sell, zero sizing (P4).

---

## §1 · (a) Is the N− right on the sector and wrong on the defense sub-node? — the arithmetic

I split the 50 Industrials names by node and re-aggregated `SECTOR_FLOW_US.json` myself:

| Node | n | mcap | mcap share | wflow | eqflow | median rs20 vs SPY | median rs60 vs SPY | 🟢 | 🔴 |
|---|---|---|---|---|---|---|---|---|---|
| **All Industrials** | 50 | $5,220B | 100% | **−0.167** (#9/11) | −0.116 | −2.0 | −4.8 | 2 | 17 |
| **Capital goods + electricals** | 25 | $2,728B | **52.3%** | **−0.455** | −0.410 | −4.9 | −6.0 | 0 | **14 of the 17** |
| **5 primes** (GD RTX NOC LMT LHX) | 5 | $591B | 11.3% | **+0.250** | +0.146 | **+2.2** | −9.9 | 0 | **0** |
| primes + AXON | 6 | $626B | 12.0% | +0.261 | +0.196 | +4.1 | −3.8 | 0 | 0 |

**Answer: yes on both halves, and the sector number is a weighted average of two opposite things.**
The spread between the two sub-nodes is **0.705 flow-score points**; the node carrying the downgrade
(capital goods) is **52.3% of the sector's market cap and 14 of its 17 reds**, and it contains every
name the pre-mortem cited (PWR −0.800, VRT −0.817, CAT −0.678, DE −0.593). The primes contribute
**zero reds**. The N− is a correct statement about Industrials' *mass* and a false statement about
defense.

**But the sub-node evidence is a 20-day turn, not a 60-day lead — and I will not overstate it.**
Decomposing days 21–60 (rs60 − rs20, vs SPY): GD **+3.2**, RTX −3.6, LMT −12.1, LHX −18.1,
NOC −18.9. **Four of five primes lost to SPY in days 21–60**; the rs20 recovery is coincident with the
strike campaign that began 07-11. Median prime rs60 is **−9.9 vs SPY**. GD is the only prime positive
on both horizons (+6.6 / +9.8).

⚠ The GICS label "Aerospace & Defense" is *also* the wrong unit: it holds 10 names at wflow −0.012,
because it mixes the primes with commercial aero — **BA −0.725 🔴 (rs20 −7.8 / rs60 −18.2 vs SPY),
TDG −0.707 🔴, HWM −0.581 🔴**. Those are paid by airline/OEM build rates, not by a budget line.

**Restatement, not a re-rating:** Industrials cannot carry one verdict. Two nodes, two customers,
opposite tapes. S7's frozen branches remain the only thing that can move the sector label (§3).

## §2 · (b) AXON — what it is, and is the acceleration orders or multiple?

**What it is (10-K, filed 2026-02-25, FY2025):** public-safety technology, two segments —
*Software and Services* (Axon Evidence, **Draft One** AI report drafting, Records, Fusus real-time
ops; **annual recurring revenue $1.3B as of 2025-12-31**) and *Connected Devices* (TASER CEDs, body
and fleet cameras, **drone and counter-drone incl. Dedrone**, VR training; **net sales +29.1% FY25**,
TASER +$163.7M on TASER 10 volume). Formerly TASER International.

**W4 — name the customer, and it is not a defense budget line.** The filing says: *U.S. federal,
state, and local governments, international governmental entities, commercial enterprises, and
consumers*, and **"No customer represented more than 10% of total net sales"** for FY25/24/23. Axon's
budget line is **thousands of municipal and state public-safety appropriations**, not DoD
procurement/RDT&E. The pre-mortem filed AXON inside the defense sub-node; the primary source says the
07-23 primes binary and the $87.6bn Pentagon supplemental **do not transmit to it**.

**Denominator test (the answer):**

| | value | vs 90 days ago | read |
|---|---|---|---|
| Forward P/E | **48.6x** (fwd EPS 10.516) | — | trailing P/E **204.5x** on EPS 2.50 |
| FY26 EPS est (0y) | 7.68894 | **7.78519 → −1.24%** | **cut** |
| Next-qtr EPS est (+1q) | 2.01757 | 2.03395 → **−0.81%** | **cut** |
| FY27 EPS est (+1y) | 10.57333 | 10.56877 → +0.04% | flat |
| Revision count, +1q (30d) | **8 up / 9 down** | — | net negative |
| Analyst book | strongSell **0 → 1** in the last month | — | the only change in 3 months |

**Verdict: this is a multiple story, not an order/backlog story.** Over the window in which price
outran SPY by +24.6pp, the FY26 denominator was **cut 1.2%** and the next quarter **0.8%**. The word
**"backlog" does not appear anywhere in the 10-K** — the only disclosed forward metric is ARR $1.3B,
so an order story cannot be measured here the way it can at RTX/LMT/NOC. Revenue is growing (2026Q1
$807.3M, **+33.7% YoY**) but at the same ~31–34% rate as the four prior quarters — steady, not
inflecting; QoQ was **+1.3%**.

**And "still accelerating" needs correcting with the desk's own arithmetic.** rs20 +24.1 ≈ rs60 +24.6
does **not** mean 60 days of compounding — it means days 21–60 contributed **+0.5pp** and ~98% of the
60-day excess was earned in the last 20. That is the identical shape S8 already adjudicated at VLO
(rs20 +28.6 / rs60 +29.0 vs SPY → "~100% of the 60-day gain earned in the last 20 days"), and the
desk's conclusion there was that the shape describes a 20-day event, not a trend.
**Level context nothing in this run stated:** last **$511.17** against a 52-week high of **$885.92** —
**−42.3% from the high**, +50.8% off the $339.01 low. This is a recovery inside a drawdown.
Short-vol (C-grade, corroborant only): 69.1% vs a 62.3% base, z **+0.78, 5v5 +11.9▲** — building.
**Dated catalyst: 2026-08-04 earnings — outside this run's window.**

## §3 · The primes into the 07-23 binary — S7 thresholds respected, not moved

**S7 (ARMED, `handoff/SCENARIOS.md`) — one binary, not two.** S1 fold-by-date: RTX and LMT print the
same date, so "both beat" is **n ≈ 1 effective date**. Observable frozen at registration: **backlog /
book-to-bill at both**. Implied moves **RTX ±5.0% / LMT ±5.4%** (expiry D2). Branch A = backlog up at
both *and* both outside their bands → restores N+. Branch B = one outside, one inside → **split, no
verdict**. Branch C = backlog flat/down at either → N− stands. **I move none of these.**

| | RTX (07-23) | LMT (07-23) | GD (**07-29**, not in S7) | NOC (printed 07-21) | LHX |
|---|---|---|---|---|---|
| Price / fwd P/E | $193.67 / **25.5x** | $507.09 / **15.8x** | $367.73 / 20.2x | $512.29 / 16.9x | — |
| PEG | 2.65 | **1.08** | 2.74 | 3.90 | — |
| FY26 est vs 90d ago | **+1.18%** | −0.14% | **+2.43%** | (stale — see ⚠) | — |
| Revisions 30d (0y) | 2↑ / 0↓ | 1↑ / 1↓ | **3↑ / 0↓** | 1↑ / 0↓ | — |
| flow · rs20 · rs60 vs SPY | +0.444 · +6.0 · +2.4 | −0.010 · +2.2 · −9.9 | **+0.508 · +6.6 · +9.8** | +0.087 · +0.5 · −18.4 | −0.298 · −3.4 · **−21.5** |
| FINRA short-vol z (07-21) | +0.13 | +0.44 | **−1.53 covering** | **+2.27 🔴 building** | −1.86 |
| % below 52w high | −9.7% | **−26.7%** | −3.4% | −33.8% | — |

**GD carries the only clean upward revision book of the six** (3↑/0↓ across every period, FY26 est
+2.43% over 90 days) *and* the best flow *and* the only positive pair on both RS horizons *and*
short-vol covering. **GD does not print on 07-23** — it prints 07-29 and must not be folded into S7.
⚠ **NOC data-lag flag:** the module's FY26 consensus reads 27.9501 while NOC's own 07-21 guidance
raise was to **$28.60–29.10** — the vendor consensus has not refreshed. NOC's revision block is not
current and is not used as evidence. LHX is the node's worst 60-day (−21.5 vs SPY); its z −1.86 means
shorts *left*, which is not accumulation.

**W4 — the customer is a budget line, and here is the disclosed spend.** DoD procurement + RDT&E +
FMS. In-window, body-confirmed: Hegseth testified **07-21 seeking $87.6bn additional Pentagon
funding**, citing *"critical shortfalls"* in replenishing **munitions**, after putting the Iran war
cost at **$37.5bn** [guardian 07-21, fortune 07-21, bbc 07-22, aljazeera 07-21 — 4 art / 3 outlets].
Already-awarded confirmation: **"Lockheed Wins $35 Billion US Deal to Boost Interceptor Output"**
[bloomberg body, in-window]; a Patriot interceptor now costs **less than half a regular interceptor**
[businessinsider 07-21] — cost-down is what buys volume at a fixed appropriation.
**Contradicting evidence, quoted:** **Sen. Patty Murray challenged the request in the same hearing**
[fortune 07-21]. It is a **request, not an appropriation**, and it has **no dated vote** — not in
`CATALYST_WATCH.json`, `[blank]`, not guessed.
Book context only, no positioning statement: RTX is a **9.49%** live position (`CYCLE_EXPOSURE.json`,
rank-3 rearmament). This file makes no recommendation about it.

## §4 · (c) The civil-nuclear leg — verified, and it stays removed

**Verification run against `names[]` (n=300, 0% NaN this run):** **BWXT, SMR, CCJ, LEU all return
NOT IN `us_top300`.** Westinghouse is private. **EVENT_ALPHA Card 6's removal is correct on the facts.**

The three in-universe candidates, one at a time:
- **GEV — the only real transmission, and it is immaterial.** GE Vernova owns GE Hitachi's BWRX-300
  SMR line, the sole reactor product in the universe. But its revenue mass is gas turbines and grid
  (07-15 deep: $163B backlog, orders +71% organic) — a Saudi civil-nuclear award is a rounding line
  against that. Tape: flow −0.322, **rs20 −4.8 / rs60 −11.8 vs SPY**, OBV 중립. **FAIL.**
- **GE — this is a chain error and must be named as one.** GE is **GE Aerospace**; GE Vernova was
  separated in 2024. GE's +0.175 flow and **rs60 +15.0 vs SPY** are an **aero-engine aftermarket**
  story with **zero nuclear content**. Citing it as nuclear transmission attributes a commercial-aero
  cash flow to a civil-nuclear headline. **FAIL — wrong company.**
- **ETN** — switchgear/BOP electrical is generic to any generation project, un-attributable to a Saudi
  award, and the tape is flow −0.506, **rs20 −8.1 / rs60 −10.7 vs SPY**. **FAIL.**

**Conclusion: no in-universe name has material transmission.** Card 6 stays STORY-ONLY with its
`2026-08-21` re-check unchanged (named US vendor + dollar value, **and** GEV rs20 vs SPY crossing
positive). The nuclear leg does not come back into the Industrials case this run.

## §5 · (d) Does the money follow the news, or is it story-only?

| Thread | In-universe epicenter | Flow cross-check | Verdict |
|---|---|---|---|
| **China military-grade drone import ban** [aljazeera 07-22 body; zerohedge 07-21 "FCC Moves To Ban Foreign Military-Grade Drone Imports"; 27 FTS hits/7d] | **None.** Skydio, Anduril, X-Bow = private; Ondas below the cut; **AVAV and KTOS verified NOT in us_top300**. Only AXON has a drone/counter-drone line (Dedrone + Axon Air inside "Platform Solutions") and the 10-K **does not size it** | cannot be run — no epicenter | **STORY-ONLY** |
| **Autonomous uncrewed fighter jets** [Reuters/japantimes/investing_en 07-22, 3/3] | Bodies name **BAE's 'Brontanax'**, the **first British-designed CCA** (07-22), **Canada joining GCAP** (scmp 07-22) — this week's CCA news is a **UK/European program story**, not a US budget line. US CCA primes GA-ASI, Anduril = private | in-universe adjacents move the wrong way: **BA −0.725 🔴 (rs60 −18.2)**, NOC rs60 −18.4, LMT rs60 −9.9 vs SPY | **STORY-ONLY, FAIL on flow** |
| **Iran campaign 11th night · $37.5bn cost · $87.6bn supplemental sought** [4 art/3 outlets] | **RTX / LMT / NOC** — the munitions-replenishment line, with a named award (**LMT $35B interceptors**) | RTX +0.444 (+6.0/+2.4), LMT −0.010 (+2.2/−9.9), NOC +0.087 (+0.5/−18.4) vs SPY — **20-day positive at all three, 60-day negative at two of three** | **PARTIAL PASS** — money follows over 20 days, not 60 |

**Answer: one of the three has money behind it, and it is the one with a dollar figure and a signed
award.** The two drone/autonomy threads have **no in-universe epicenter at all** — the same structural
coverage hole PREMORTEM Lens 4 recorded for the tanker leg, now confirmed a second time on a second
cycle. And the money-follows leg is a **request under contest**, so the transmission is conditional.

## §6 · Value chain, left to right — with the binding constraint named

```
[1] APPROPRIATED BUDGET LINE — DoD procurement + RDT&E; FY27 ~$1.5T advancing;
    ★ $87.6bn supplemental REQUESTED 07-21, contested (Murray), UNDATED [blank]
      ▼
[2] PROGRAM OFFICES / AWARD FLOW — LMT $35B interceptor output; RTX AIM-9X; FMS Europe/Gulf
      ▼
[3] PRIMES / SYSTEMS INTEGRATION — RTX LMT NOC GD LHX   (wflow +0.250, zero 🔴)
      ▼
[4] TIER-1 STRUCTURES & PROPULSION — HWM −0.581 🔴, TDG −0.707 🔴 in-universe;
    HII / KTOS / AVAV verified OUT of universe
      ▼
[5] ★★ ENERGETICS · SOLID ROCKET MOTORS · NITROCELLULOSE = BINDING CONSTRAINT ★★
    private or foreign; LHX/Aerojet is the only listed in-universe touch — and it is the
    node's worst 60-day tape (rs60 −21.5 vs SPY)
      ▼
[6] FINAL ASSEMBLY & TEST THROUGHPUT  →  [7] SUSTAINMENT / AFTERMARKET (TDG; LDOS/BAH out of
    universe)  →  [8] FMS / EXPORT DELIVERY
```

**The bottleneck is [5], not [1] — strong demand is not a bottleneck.** A $1.5T budget and an $87.6bn
top-up are demand statements. Hegseth's own words are a *throughput* complaint, not a funding one:
*"critical shortfalls… replenish munitions."* The 07-21 deep established this tier with primary
sources; this week's testimony tests it and it holds. **Consequence: backlog size is not the KPI —
backlog conversion is**, which is exactly S7's frozen observable. ⚠ And the constraint is
**structurally unownable here**: no `us_top300` ticker expresses the energetics tier. That is a
coverage finding, not a name to substitute around.

## §7 · Chain-hop candidates — PASS/FAIL (co-mention alone is not a candidate)

Ran `chain-hop defense drone munitions --days 14 --scope foreign` (1,500 articles, ±300-char
proximity). Headline-named/crowded: **BA 27 titles, LMT 20, RTX 14, NOC 7**.
Candidates emitted: **V (12 prox), GM (6), WMB (3), AXP (2), NEE (2), ISRG (2), CRM (2), CMG (2)**.

**All 8 FAIL, and the tool's own example column proves it before any flow check:** V's example article
is *"Trump Urges Faster Submarine Production, Singles Out General Dynamics"* (the ticker "V" collides
with ordinary text); GM's is a TSMC revenue story; AXP's and NEE's is *"Pre-Markets in Green After
Week of Losses"*, a market wrap; CMG's is a podcast round-up. Flow cross-check run anyway on the two
with any conceivable link, both FAIL there too: **NEE** +0.244 but **rs60 −14.3 vs SPY**; **ISRG**
−0.115, **rs20 −13.6 / rs60 −32.5 vs SPY**.

**Zero PASS.** The genuine body-proximate beneficiaries this theme produces are **KTOS, AVAV, HII,
LDOS, BAH, TXT, SPR, HEI, CW — all verified NOT in `us_top300`** — or private (Anduril, GA-ASI,
Skydio, X-Bow, Saronic). **The drone/munitions chain has no expressible chain-hop inside this
universe.** Recorded as a coverage finding, not worked around.

*(One real, non-chain-hop item the tool surfaced: Trump pressed **GD to invest $2.5B in submarine
construction** [bloomberg 07-15, yahoo 07-16]. ⚠ That is capex demanded **of** the contractor, not
revenue **to** it — it hits FCF before it hits backlog. GD prints 07-29.)*

## §8 · Track KPIs and anti-signals — as dated observables

**KPIs**
- **2026-07-23 pre-open** — RTX & LMT **backlog $ and book-to-bill**. S7 frozen bands RTX ±5.0% /
  LMT ±5.4%. Anchors to beat (07-21 deep, flagged unconfirmed): RTX ~$271B, LMT ~$194B. Printed
  comparator: **NOC 07-21 — $105B backlog, +17% YoY, b-t-b ~1.84x, FY guide raised to $28.60–29.10.**
- **2026-07-29** — GD prints (**not** part of S7). Watch Electric Boat throughput and whether the
  $2.5B submarine capex appears as guidance.
- **2026-08-04** — AXON prints. The only test of whether +24.1 rs20 vs SPY has a revenue line behind
  it: ARR vs the **$1.3B** 2025-12-31 base; Connected Devices vs FY25's **+29.1%**; and whether the
  FY26 EPS estimate **stops being cut** (−1.24% over 90 days today).
- **`[blank]`** — a committee mark or floor vote on the **$87.6bn** supplemental. Not in
  `CATALYST_WATCH.json`; not guessed.
- **2026-08-21** — Card 6 civil-nuclear re-check (named US vendor + $ value **and** GEV rs20 vs SPY >0).

**Anti-signals**
- **The 07-21 NOC pattern repeating**: beat + raise + record backlog and the stock still fell **2.7%**.
  If RTX or LMT does that on 07-23, the news is priced — and per **S7 branch B a split is no verdict**,
  not a bull confirmation.
- **Book-to-bill <1.0** at either name → S7 branch C, N− stands.
- A **fixed-price development program charge** at any prime.
- The **supplemental cut or stalled** in committee — the Murray objection is already on the record.
- **AXON**: another FY26 estimate cut while 48.6x fwd holds; or **rs20 vs SPY crossing below 0** —
  the pre-mortem's own registered flip for the EXTENDED-BUT-LIVE tag, which I do not move.
- **Hormuz de-escalation** (S8): removes the replenishment urgency carrying the munitions node — ⚠ and
  it hits the desk's Energy OW on the same tick. One event, two positions.

## §9 · Dispersion statement (W5)

**The intra-Industrials spread vs SPY is 39.6pp on rs20 (AXON +24.1 → VRT −15.5) and 46.1pp on rs60
(AXON +24.6 → LHX −21.5), with population σ(rs20) = 9.02pp and flow scores from +0.922 (CTAS) to
−0.817 (VRT). The sub-node wflow spread is 0.705 points (primes +0.250 vs capital goods −0.455).**

**At that dispersion the sector label is the wrong unit and must not carry a verdict.** The two nodes
have **different customers**: capital goods is paid by private capex (datacenter, construction, farm),
the primes by an appropriated budget line. A single number averages them and prices neither. This is
the same complaint SWEEP_READ §2 raised for the ~40pp intra-IT spread and did not apply here; it is
applied here now.

⚠ **Dispersion cuts both ways.** It does not license reading the primes as leadership: **median prime
rs60 is −9.9 vs SPY**, only **GD** is positive on both horizons, and AXON's excess was earned almost
entirely in one 20-day window while its earnings estimates were being cut. The finding is *use two
units*, not *the second unit is winning*.

---

*Sources: `SECTOR_FLOW_US.json` (asof 2026-07-21 close, re-aggregated by node in this file) ·
`module_fundamentals_us --json` AXON/GD/RTX/LMT/NOC (2026-07-22) · `module_business_us AXON --json`
(10-K filed 2026-02-25, FY2025) · `scripts/us_flow.py` FINRA Reg SHO (2026-07-21) ·
`module_news_data chain-hop / fts search --scope foreign` · `CATALYST_WATCH.json` ·
`handoff/SCENARIOS.md` S7/S8 · priors 2026-07-21 US_2 and 2026-07-15. Every RS figure vs SPY.
No guessed numbers; NOC's vendor consensus flagged stale. Zero buy/sell, zero sizing.*
