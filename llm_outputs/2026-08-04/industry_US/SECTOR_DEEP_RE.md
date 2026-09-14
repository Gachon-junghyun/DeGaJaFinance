# SECTOR_DEEP_RE — Real Estate — industry_US — 2026-08-04 · ROTATING → **FULL FRESH MAP**

> Last covered **2026-07-30**. Read, **not carried** — every number below is re-derived.
> Benchmark **SPY inline (C1)**. Flow asof **2026-08-03 settled**; price ladder computed on
> `index <= 2026-08-03` (settled closes only, no live bar — D74). Clustering re-run fresh.
> **Analytical only (P4). No position language, no sizing.**
> ⚠ **M152**: `module_report_tags` silently returns 0 for `O` and `WELL`. **It was not called.** No
> conclusion here rests on it.

---

## 0 · ⛔ The indictment answered first

**The indictment's arithmetic is CORRECT and I reproduce it independently.** Fresh yfinance, settled
closes to 08-03, RS = name simple return − SPY over the same window:

| | indictment | **my recompute** |
|---|---|---|
| VTR RS5 | −11.8 | **−11.76** |
| WELL RS5 | −8.7 | **−8.65** |
| DLR RS5 | −4.8 | **−4.83** |
| EQIX RS5 | −4.0 | **−3.98** |
| DLR RS60 / seg 21-60 | −7.1 / −15.1 | **−7.11 / −16.35** |
| EQIX RS60 / seg 21-60 | −8.2 / −10.4 | **−8.24 / −10.65** |
| VTR RS20 +15.03 → | −2.33 | **−2.33** |
| WELL RS20 +12.04 → | −0.67 | **−0.67** |

**I concede three of its claims outright:**
1. **DLR's +9.24 RS20 is recovery of ground already lost, not new excess.** RS60 is still **−7.11**.
   Over 60 sessions DLR has *underperformed*. That is exactly what the indictment said.
2. **VTR and WELL have completed their reversion.** +15.03 → −2.33 and +12.04 → −0.67. True.
3. **The desk's "breadth-led" rationale for this sector is weaker than the label implies** — see §1.
   The sweep's own green-count breadth for Real Estate is **0.0, the worst value available.**

**Three things in it are wrong, and they are the load-bearing three.**

**(a) "Every real-estate name on the board is negative in the freshest leg" is FALSE on the 12-name
sector board.** Three names are POSITIVE over the 5-session leg: **AMT +1.24 · CCI +1.01 ·
CBRE +0.65.** The claim survives only if "the board" means the four names it already chose.

**(b) The four names are TWO measured risk units, not four observations.** Fresh
`scripts/risk_units.py`, 498 days, SPY-residual: **VTR–WELL +0.788** and **DLR–EQIX +0.639** are the
sector's #2 and #3 residual pairs, and at the 5-unit resolution they are literally **U3 = {VTR, WELL}**
and **U1 = {DLR, EQIX, IRM}**. Citing VTR *and* WELL as two pieces of evidence double-counts one unit.
Combined with **S1 (one date is n≈1)** on a 5-session leg, the indictment's evidentiary base is
**n ≈ 2 units × 1 leg**, not 4 names.

**(c) The freshest leg is mostly beta, and where it is not beta it points the other way.**
Over the last 3 sessions SPY returned **+3.87%** (5-session **+2.51%**). Regressing each name's RS on
its measured beta-to-SPY (from the same 498-day fit):

- **corr(beta, RS3) = +0.767** ⇒ **59% of the 3-session cross-section is beta ordering.** A low-beta
  sector underperforming a +3.87% SPY rip is a mechanical result, not a verdict on the sector.
- **corr(beta, RS5) = +0.035** ⇒ over 5 sessions beta explains **nothing**. The RS5 dispersion is
  **idiosyncratic**, and it is concentrated almost entirely in **one measured unit, {VTR, WELL}.**

**(d) And that unit's damage arrived AFTER a beat-and-raise from both members** (primary, EDGAR
Item 2.02 + call transcript):
- **VTR (8-K 07-29)**: *"10% total company same-property NOI growth"*, FY normalized FFO **raised to
  $3.85–3.90**, **$4.5bn of 2026 senior-housing investments** planned.
- **WELL (8-K 07-27)**: **FFO $1.60, beat by $0.05; revenue $3.54bn, beat by $150m**; guidance raised;
  dividend maintained at $0.85 and boosted per the release coverage.

⇒ **The reversion in VTR/WELL is a multiple event, not an operating event.** M149's measure is a
price measure; it cannot distinguish those, and the indictment reads the price move as if it were a
verdict on the asset.

**(e) On M149's own terms, "EXHAUSTED" is the wrong word for DLR and EQIX.** M149 defines exhaustion
as *a decaying stock of PAST EXCESS* — share = RS20/RS60 near or above 100%. **DLR and EQIX have no
past excess to decay: RS60 is −7.11 and −8.24.** You cannot exhaust a stock you never accumulated.
The correct label is the one D154 registered — see §2.

**Verdict on the slot.** The indictment is right that this sector's 20-day leg has stalled and right
that the OW's stated rationale is thin. It is wrong that the sector is one exhausted run. **It is two
opposite geometries pointed in opposite directions**, and the four names it chose are one from each,
which is why they looked uniform. **The slot's process ground (binding variable settles 08-12) is
intact, and this file does not defend the OW tilt — §1 partially concedes it.**

---

## 1 · Flow — and an honest qualification of the desk's own "breadth-led" label

`SECTOR_FLOW_US.json`, asof **2026-08-03 settled**: **wflow +0.121 · eqflow +0.155 · green 0 · red 1
of 12 · breadth 0.000 · delta +0.044.**

Real Estate is **one of only three sectors with positive `delta`** (RE +0.044 · Utilities +0.050 ·
Materials +0.042) and **the only OW-family sector where eqflow > wflow** (gap +0.034).

⚠ **But "breadth-led" overstates a 2-name effect (C5/W5).** The sector's green-count breadth is
**literally 0.000 — zero greens of twelve, the worst value on the scale.** The eqflow>wflow gap is
produced by the two best flow scores sitting on two of the three smallest names:

| driver | mcap | flow |
|---|---|---|
| **IRM** | $38.0B | **+0.675** (best) |
| **CBRE** | $38.5B | **+0.600** (2nd) |
| vs **WELL** | $145.9B | **−0.209** |
| vs **PLD** | $131.0B | **+0.242** |
| vs **EQIX** | $107.7B | **+0.195** |

⇒ **a +0.034 gap carried by 2 of 12 names is not breadth.** The desk's OW rationale should say
"the small names are outperforming the large ones," which is a different and smaller claim.

**Full board, `asof 2026-08-03`** (flow, tag, OBV are **C-grade — RULE D6**; RS is the A-grade axis):

| Name | industry | mcap$B | flow | tag | OBV | RS20 | RS60 | **seg 21-60** | vol_surge | delta |
|---|---|---|---|---|---|---|---|---|---|---|
| **IRM** | Other Specialized | 38.0 | **+0.675** | 🟡 | 매집 | +5.77 | −8.92 | **−14.69** | 1.18 | +0.139 |
| **CBRE** | RE Services | 38.5 | **+0.600** | 🟡 | 매집 | +4.76 | −1.26 | **−6.02** | 1.12 | +0.137 |
| **DLR** | Data Center | 66.1 | +0.550 | 🟡 | 매집 | **+9.24** | −7.11 | **−16.35** | 0.79 | −0.017 |
| **AMT** | Telecom Tower | 82.0 | +0.408 | 🟡 | 중립 | +5.87 | −6.57 | **−12.44** | 1.21 | +0.089 |
| **PLD** | Industrial | 131.0 | +0.242 | 🟡 | 중립 | +1.97 | −1.91 | −3.88 | 1.02 | **−0.232** |
| **EQIX** | Data Center | 107.7 | +0.195 | 🟡 | 중립 | +2.41 | −8.24 | **−10.65** | 1.16 | **+0.268** |
| **PSA** | Self-Storage | 55.9 | +0.167 | 🟡 | 중립 | −0.26 | +2.94 | **+3.20** | 1.35 | +0.178 |
| **CCI** | Telecom Tower | 35.8 | +0.109 | 🟡 | 중립 | +1.58 | **−17.48** | **−19.06** | 1.11 | +0.244 |
| **WELL** | Health Care | 145.9 | −0.209 | 🟡 | 분산 | −0.67 | +4.54 | **+5.21** | 1.04 | +0.026 |
| **VTR** | Health Care | 39.7 | −0.219 | **🔴** | 분산 | −2.33 | +1.98 | **+4.31** | 1.24 | −0.166 |
| **SPG** | Retail | 68.5 | −0.251 | 🟡 | 중립 | +1.00 | **+9.22** | **+8.22** | 0.69 | +0.073 |
| **O** | Retail | 56.2 | **−0.411** | 🟡 | 분산 | +0.03 | −3.05 | −3.08 | 0.89 | +0.029 |

**XLRE vs SPY**: exc1d **−1.18** · exc5d **−3.78** · exc20d **+1.16** · exc60d **−1.65** · exc120d
**−1.17**. ⚠ **C3 — discrepancy declared**: the mandate's sweep carries exc60d **−2.27**; my
settled-close recompute gives **−1.65**. 1d/5d/20d match to the decimal. **The 60-day figure differs
by 0.62pp and I do not know which is right** — most likely a dividend-adjustment or window-edge
difference. Not resolved, not averaged, not used as a load-bearing number.

---

## 2 · Momentum geometry, with D154's guard applied

**D154 says the ratio share = RS20/RS60 is undefined when |RS60| is small, and has no branch for
RS20 < 0 < RS60. In this sector that guard disqualifies 8 of 12 names.** Classification first:

**Class A — RS20 < 0 < RS60 (D154's UNBRANCHED case; M149 has no ruling here at all):**
**WELL (−0.67 / +4.54) · VTR (−2.33 / +1.98) · PSA (−0.26 / +2.94).**
⇒ ★ **The indictment invokes M149 against VTR and WELL. M149's method has no branch for VTR and
WELL.** Their ratios would be −118% and +14.7%, meaning nothing. **Report the segment instead:
VTR +4.31, WELL +5.21 — both POSITIVE.**

**Class B — |RS60| < 3, ratio explodes (D154's primary defect):**
**PLD** 1.97/−1.91 = **−103%** · **CBRE** 4.76/−1.26 = **−378%** · **VTR** −118% · **PSA** −8.8%.
⇒ **All four ratios discarded. Segments used: PLD −3.88 · CBRE −6.02 · PSA +3.20 · VTR +4.31.**

**Class C — RS20 > 0 > RS60 (sign-flipped; a hole partly refilled, NOT exhaustion):**
**DLR (+9.24 / −7.11, seg −16.35) · AMT (+5.87 / −6.57, seg −12.44) · IRM (+5.77 / −8.92, seg −14.69)
· EQIX (+2.41 / −8.24, seg −10.65) · CCI (+1.58 / −17.48, seg −19.06) · O (+0.03 / −3.05).**
⇒ **This is the class the indictment calls "EXHAUSTED." It is the opposite of M149's definition.**
These names dug a hole in days 21-60 and have refilled part of it in the last 20. **Whether a refill
becomes a base is unresolved and is exactly what the KPI in §8 is frozen to measure (C4).**

**Class D — the only well-defined ratio in the sector: SPG.** RS20 +1.00 / RS60 +9.22 ⇒
**share = 10.8%.** ⇒ **89% of SPG's 60-day excess was earned BEFORE the last 20 sessions and has NOT
been given back.** Under M149 that is old excess **holding**, not decaying.

### ★ The finding: the sector splits into two opposite geometries, and they are near-perfectly inverse

| | **Group FRESH** (RS20 > 0, segment NEGATIVE) | **Group BASED** (RS20 ≤ 0 or ~0, segment POSITIVE) |
|---|---|---|
| names | DLR · IRM · AMT · CBRE · EQIX · PLD · CCI · O | **SPG · WELL · VTR · PSA** |
| median RS20 | **+3.59** | **−0.46** |
| median segment | **−13.57** | **+4.76** |
| median flow | **+0.33** | **−0.21** |

**The four names with a real 40-day foundation underneath are the four with the weakest 20-day leg
and the weakest flow. The eight with the strongest 20-day leg have no foundation at all.**
⇒ **There is no single "run" in this sector to be over.** The indictment took DLR/EQIX from Group
FRESH and VTR/WELL from Group BASED, and the two groups are negative in the freshest week **for
opposite reasons** — Group FRESH because its refill stalled, Group BASED because a beat-and-raise was
sold. **W5: RS5 range across the 12 is 13.0pp (VTR −11.76 to AMT +1.24), sd 3.69.**

---

## 3 · Value-chain map and the binding constraint

Left → right. **Cross-sector chain marked ⊗.**

```
[1] CAPITAL SUPPLY          [2] LANDLORD / DEVELOPER      [3] POWER ⊗Utils      [4] SHELL+FIT-OUT ⊗Inds
 IG OAS 0.79 · HY 2.85       LISTED: DLR EQIX IRM          on-site gas 1.6GW     PWR +0.340 rs60 −16.6
 bank bridge (MS-led)   ──▶  PRIVATE: Nexus, BlackRock ──▶ CEG 🟡 rs60 −18.5 ──▶ ETN 🟢 +0.867
 infra equity BX KKR APO     Blue Owl, Blackstone          VST 🟡 · NEE 🟡분산    VRT 🔴 rs20 −18.3
                                                           Utils: 1🟢/8🔴         GEV 🔴 −0.667
        │                             │                                                │
        └──────── ⊛ BOTTLENECK ───────┘                                                ▼
                                                                        [5] TENANT ⊗Tech/Comm
[8] AFFO → distribution ◀── [7] RENT / OCCUPANCY ◀── [6] END DEMAND ◀──  AMZN 🟢 +0.906 rs20 +15.5
 EQIX AFFO guide RAISED       EQIX 281 DCs             GOOGL cloud +82%   MSFT 🟢 +0.933 rs20 +25.2
 VTR FFO $3.85-3.90           VTR SP-NOI +10%          AI labs: Anthropic META 🔴 −0.174 · GOOGL 🟡 rs60 −9.4
```

### The binding constraint is node [1]→[2]: **the price of third-party capital that competes for the same asset.** It is NOT demand, and it is NOT power.

**Demand is not a bottleneck** (a bottleneck is a constraint, not enthusiasm — and every demand
reading this window is UP):
- **EQIX raised its multi-year algorithm**: annual revenue growth **10–13% through 2029, up from
  7–10%**; **AFFO/share growth 9–12% annually, up from 5–9%**; FY26 AFFO **$42.69–43.29** raised from
  $42.31–43.11 [Reuters via yahoo_finance/cna, 07-29/30, full body].
- **AMZN raised its capex forecast** and the stock printed **+14.68%** [yahoo_finance, 07-31].
- **GOOGL cloud revenue +82% YoY.**
- **VTR same-property NOI +10%; WELL revenue beat by $150m.**

**Power is not the near-term bottleneck at the marginal campus either** — the Nexus/Anthropic campus
**builds its own 1.6 GW gas plant on site**, routing around the grid queue. ⚠ **That is one project,
n=1 (S1)**, and the Utilities tape (**wflow −0.234, 1🟢/8🔴**) says the listed power leg is the
weakest link on the board regardless.

**What IS binding — and it changed shape this window.** Three primary-adjacent readings, same week:

1. **Nexus Data Centers / Anthropic / Google — ~$15bn, Hubbard TX** [Reuters+WSJ via yahoo_finance
   and seekingalpha, 07-30/31, full body]: **$14bn bridge loan + revolver, Morgan Stanley-led bank
   syndicate**; **Google guarantees Anthropic's lease and power-purchase commitments** across four
   leases, *"limited to the minimum level required by lenders to complete the financing"*, and takes
   **~20% equity** in the project; Broadcom vendor-finances the TPUs separately.
2. **M227 (carried, still live)**: Meta × BlackRock, **1 GW El Paso, ~$14bn, BlackRock funds 80%,
   Meta leases the campus back with ~$13bn of residual-value guarantees.**
3. **Goldman Sachs: Big Tech will fund more than a third of its AI investment with DEBT in 2027**
   [yahoo_finance, 07-28, headline+body lead].

⇒ **★ The structural reading this map hands forward: on the marginal AI gigawatt, the LANDLORD role
is being taken by bank-financed private developers and infrastructure funds, not by the listed REITs.**
The listed data-centre REITs are **not the counterparty** in El Paso, **not** in Hubbard, **not** in
the Blue Owl Louisiana arrangement. **They are being disintermediated on the largest new campuses.**

**C2 — the other half, stated with equal weight.** The listed REITs are **not shrinking**, and two
facts say the disintermediation is partial, not total:
- **DLR bought three N. Virginia data centres from Blackstone for $3.5bn** and raised FY AFFO guide.
- **EQIX's product is different**: 281 facilities, customers **Nvidia, Netflix, Adobe** —
  interconnection and network density for enterprises, not build-to-suit gigawatt campuses. **Raising
  a multi-year growth algorithm by ~4pp at both ends is not the behaviour of a disintermediated
  asset.** ⇒ the hyperscale-campus and colocation/interconnect businesses may simply be **two
  different products**, in which case the private-capital surge does not compete with EQIX at all.
  **This DEEP does not resolve which reading is right (C4).**

### ★ M227's question answered: what a lease-financed buildout does to a landlord's node

Three effects, and **the third cuts the opposite way from the first two**:
1. **It expands landlord capacity without using REIT cost of capital.** Private vehicles fund at bank
   bridge + infra-equity rates against a hyperscaler guarantee. The listed REIT funds at its own
   equity cost — **EQIX dividend yield 2.02%, WELL 1.45%, DLR 2.59%.** ⇒ REIT scarcity value on the
   AI narrative falls.
2. **It converts tenant capex into CREDIT.** Meta's ~$13bn residual-value guarantees and Google's
   guarantee of Anthropic's lease and power payments mean **the hyperscaler balance sheet is now the
   credit backstop for the landlord's rent roll.** ⇒ **this confirms M134 at a deeper level: the
   node's sensitivity is credit, and the credit is now explicitly contractual, not inferred.**
3. ⚠ **But widening spreads are NOT unambiguously bad for the listed REIT.** Its current competitive
   threat *is* cheap third-party capital. If IG/HY widen, the bridge-loan/infra-fund bid retreats and
   the investment-grade listed REIT regains the marginal deal. **Against that, the REIT funds with
   debt too** — EQIX alone has **seven listed senior-note series (0.25% '27 through 4.00% '34)**.
   ⇒ **the net sign of a spread-widening on the listed data-centre node is genuinely
   INDISTINGUISHABLE from this file's evidence (C4). The desk's framing of S41 as a clean sector kill
   is one-sided and should not be inherited as such.**

**Live values**: **IG OAS 0.79 vs S41's 0.90 line = 11bp · HY OAS 2.85 vs S26's 3.10 = 25bp. Both
settle 2026-08-12.** ⚠ Fitch (07-27): AI-related investment added **1.4% to US Q1'26 GDP growth** and
named *"re-evaluation of long-run returns potential"* as a corporate-credit channel; Morgan Stanley
(June) puts 2026 AI-related corporate debt issuance at **~$570bn**.

---

## 4 · The three-unit structure re-tested (M131) — pairs held, the partition did not

**Fresh run**: `python -X utf8 scripts/risk_units.py DLR EQIX IRM AMT CCI PLD WELL VTR SPG O PSA CBRE
--days 499`. Window **2024-08-08 → 2026-08-04, 498 aligned trading days**, bench SPY, calendar loss
**0 for all 12**, max gap 4d.

**★ M148's required disclosure: ARI (first half vs second half) = 0.355** at the default threshold
(**0.324** at 0.55). **Last run disclosed 0.5987.** ⇒ **membership stability has DEGRADED by ~40%.
The partition below should be treated as unstable and the pairs as the real finding.**
Within-group residual corr **+0.4639** vs between **+0.2420** (fit improved while stability fell —
exactly the S5 pattern the script warns about).

**C5 — threshold is arbitrary, so both resolutions are reported:**

| threshold | units | membership |
|---|---|---|
| **0.65** (corr ≥ 0.35, default) | **3** | **U0** {AMT, CCI, O, PLD, PSA, SPG, VTR, WELL} · **U1** {DLR, EQIX, IRM} · **U2** {CBRE} |
| **0.50–0.60** (corr ≥ 0.40–0.50) | **5** | **U0** {AMT, CCI, O, PSA} · **U1** {DLR, EQIX, IRM} · **U2** {PLD, SPG} · **U3** {VTR, WELL} · **U4** {CBRE} |
| 0.40 | 8 | fragments |
| 0.80+ | 1 | collapses |

**What survived, and it is the whole point: `U1 = {DLR, EQIX, IRM}` is IDENTICAL at every threshold
from 0.50 to 0.70.** M131's most contested claim — that the real data-centre node **includes IRM and
excludes CCI** — **reproduces exactly on fresh data.**

**M131's four cited pairs reproduce to within 0.01 across a re-fit window:**

| pair | M131 (07-30) | **fresh (08-04)** | Δ |
|---|---|---|---|
| AMT–CCI | +0.822 | **+0.8250** | +0.003 |
| WELL–VTR | +0.793 | **+0.7880** | −0.005 |
| DLR–EQIX | +0.641 | **+0.6390** | −0.002 |
| DLR–IRM | +0.600 | **+0.6070** | +0.007 |

⇒ ★ **The pairwise structure is stable to three decimals while the partition's ARI fell from 0.60 to
0.36.** That is not a contradiction — it is the correct reading of M148: **trust the pairs, distrust
the grouping.** Also fresh: **O–PSA +0.626**, and the sector's weakest links are all **CBRE**
(CBRE–EQIX **+0.133**, CBRE–WELL +0.162, CBRE–IRM +0.169).

**M131's headline inequality HOLDS and widened.** Cross-unit residual means at the 5-unit resolution:

| | mean |
|---|---|
| towers/duration {AMT,CCI,O,PSA} ↔ **health-care** {VTR,WELL} | **+0.3860** |
| towers/duration ↔ cyclical {PLD,SPG} | **+0.3894** |
| towers/duration ↔ **data-centre** {DLR,EQIX,IRM} | **+0.2662** |
| data-centre ↔ cyclical | **+0.2315** |
| **data-centre ↔ health-care** | **+0.2195** ← the sector's lowest |

⇒ **Towers sit closer to duration-style REITs (+0.386) than to data centres (+0.266), gap +0.120** —
M131 measured +0.321 vs +0.273, gap +0.048. **The gap has more than doubled.** And **{DLR, EQIX, IRM}
now has the three lowest cross-unit correlations in the sector** ⇒ **the data-centre node is the most
isolated bet on this board.**

**Measured betas vs SPY (498d)** — these carry §0's beta result and are worth having explicitly:
**AMT −0.071 · CCI +0.056 · O +0.115 · VTR +0.137 · WELL +0.208 · PSA +0.405 · EQIX +0.646 ·
SPG +0.723 · PLD +0.747 · DLR +0.762 · CBRE +0.915 · IRM +0.960.**
⇒ **M133's finding that the towers are the lowest-beta names in the sector reproduces exactly.**

---

## 5 · Players ∪ thematic, with the mandated flow cross-check

**Bound**: named ≥2× in the sector's news window **AND** a real ticker **AND** mcap ≥ ~$2B.
⚠ **Mandate #4 enforced: a news co-mention alone is NOT a candidate. Flow cross-checked on every row
before anything is described as interesting.**

**Core 12** — §1's table, all above the bound.

**Thematic union — the financing layer that appeared in the value chain:**

| Ticker | mcap$B | why in the window | flow | tag | OBV | RS20 | RS60 | seg | delta |
|---|---|---|---|---|---|---|---|---|---|
| **BX** | 151.3 | sold DLR 3 N.Va DCs $3.5bn; Blackstone infra | **+0.717** | 🟡 | 매집 | +8.30 | **+4.80** | −3.5 | +0.158 |
| **KKR** | 87.1 | AI-infra credit/equity | **+0.739** | 🟡 | 매집 | +10.20 | **+2.50** | −7.7 | +0.064 |
| **BLK** | 163.0 | **M227 counterparty — funds 80% of Meta El Paso** | +0.165 | 🟡 | 중립 | +10.60 | +1.70 | −8.9 | +0.024 |
| **APO** | 79.3 | AI-infra credit | +0.501 | 🟡 | 매집 | +5.10 | −3.30 | −8.4 | −0.027 |
| **MS** | 352.0 | **leads the $15bn Nexus bank syndicate** | −0.239 | 🟡 | 중립 | −5.70 | +6.00 | **+11.7** | **−0.420** |
| **AVGO** | 1957.0 | vendor-finances Anthropic's TPUs | +0.258 | 🟡 | 매집 | +4.10 | −11.10 | −15.2 | −0.325 |
| **ETN** | 163.8 | fit-out, node [4] | **+0.867** | **🟢** | 매집 | +5.20 | +0.70 | −4.5 | +0.166 |
| **VRT** | 127.9 | fit-out, node [4] | −0.177 | **🔴** | 분산 | **−18.30** | **−30.00** | −11.7 | +0.056 |
| **CEG** | 97.9 | power, node [3] | +0.487 | 🟡 | 매집 | +10.50 | **−18.50** | **−29.0** | −0.052 |
| **PWR** | 105.4 | build, node [4] | +0.340 | 🟡 | 중립 | +0.10 | −16.60 | −16.7 | +0.035 |

**Cross-check result, stated plainly:**
- **Nexus Data Centers and Anthropic are PRIVATE — no ticker, excluded by the bound.** The largest
  single item in this window's value chain **is not investable on this board**, and that is itself
  the §3 finding.
- **Not one financing-layer name is 🟢가속.** The best are **BX +0.717 and KKR +0.739**, both 🟡 with
  OBV 매집 and **positive RS60** — the only two rows here with a positive 60-day base.
- ⚠ **MS — the lead bank on the deal the news is loudest about — carries this table's WORST delta
  (−0.420) and a negative RS20 (−5.70).** ⇒ **a textbook case of news co-mention diverging from
  flow. It reaches BET as a named divergence, not as a candidate.**
- **The node-[3]/[4] chain is split, not confirmed**: ETN 🟢 against VRT 🔴 (RS20 −18.30) and
  CEG's seg 21-60 **−29.0**, the deepest negative segment anywhere in this file.

---

## 6 · Customers (W4) and the lease-financing question

**The data-centre node's customers are the hyperscalers. Disclosed spend, this window:**

| Customer | disclosed spend | flow | tag | RS20 | RS60 |
|---|---|---|---|---|---|
| **AMZN** | **RAISED capex forecast** (stock +14.68% on the print) | **+0.906** | **🟢가속** | **+15.50** | 0.00 |
| **MSFT** | capex **held at $190bn** (carried, M-prior) | **+0.933** | **🟢가속** | **+25.20** | +14.60 |
| **GOOGL** | **RAISED** FY capex; **Q2 FCF −$5.86bn**, $49.6bn equity raise (M134); cloud rev **+82% YoY** | −0.005 | 🟡 | +1.10 | **−9.40** |
| **META** | narrowed upward (carried); **M227 lease, not capex** | −0.174 | **🔴분산** | −2.50 | −6.90 |

★ **The customers' spend and the customers' tape have DECOUPLED, and the split is by funding mode.**
**AMZN and MSFT — the two that funded from operating cash and did not shock the market — are 🟢가속
with RS20 +15.5 and +25.2. GOOGL and META — the two that moved AI spend onto the balance sheet or off
it — are 🟡 at RS60 −9.4 and 🔴분산.** [yahoo_finance 07-30, full body]: *"Alphabet… was hammered last
week after raising its full-year capex guidance and posting negative free cash flow"* despite 82%
cloud growth. **The market is no longer paying for capex; it is pricing how the capex is funded.**

⇒ **W4's answer for the landlord node: demand from these four is not deteriorating on any disclosed
number. The variable that moved is FUNDING MODE, and the funding mode is migrating to leases,
guarantees and third-party debt** (M227 · Nexus/Anthropic · Goldman's >1/3-debt-by-2027 forecast).

⚠ **The honest limit (C3)**: **I did not obtain a hyperscaler lease-vs-own mix, and no repo module
produces one.** That is the single number that would settle whether the listed REITs capture this
demand or are routed around. **It is named as a gap, not proxied.** Also **n=1 on the observation
that a leased gigawatt bypassed the listed REITs entirely** — El Paso and Hubbard are two projects,
not a measured rate (S1).

---

## 7 · Valuation on AFFO/FFO, with margin percentile (M151 · B2)

**M151 enforced: GAAP EPS is a category error for a REIT. Both metrics shown (C2).**

| | price | **GAAP fwd P/E** | rank | **AFFO/FFO basis** | **× AFFO/FFO** | **rank** |
|---|---|---|---|---|---|---|
| **VTR** | $89.37 | **109.43** | 4th (dearest) | FY norm. FFO guide **$3.85–3.90** (primary, call) | **23.1×** | **1st (cheapest)** |
| **DLR** | $191.88 | 65.42 | 2nd | FY AFFO guide **$8.15–8.20** | **23.5×** | 2nd |
| **EQIX** | $1,042.58 | **55.96** | **1st (cheapest)** | FY26 AFFO guide **$42.69–43.29** (raised 07-29) | **24.2×** | 3rd |
| **WELL** | $228.00 | 69.62 | 3rd | Q2 FFO $1.60 **annualized ×4 = $6.40** ⚠ proxy, not a guide | **~35.6×** | **4th (dearest)** |

★ ★ **The category error does not merely shift the level — it REVERSES the ordering at both extremes.
On GAAP, VTR is the most expensive name in this table and EQIX the cheapest. On the correct metric,
VTR is the CHEAPEST and EQIX is third.** M151 said use AFFO; this table shows what ignoring it costs.

**Corroborating the same error in the revision data (both halves, C2):**
- **M132's carried claim that EQIX holds "the sector's BEST revision book (FY+1 +9.6%/90d, 4↑:0↓)"
  is DEAD on today's data**: EQIX FY+1 is **−1.0%/90d**, current quarter **−5.4%**, next quarter
  **−7.4%.**
- ⚠ **But BOTH the old +9.6% and today's −1.0% are GAAP-EPS consensus, and therefore BOTH are
  uninformative for a REIT (M151).** EQIX forward GAAP EPS is **$18.63** against AFFO **$42.99** —
  the consensus series is tracking something that is less than half the cash metric.
- **The A-grade revision fact is the company's own: EQIX RAISED FY AFFO guidance and raised its
  multi-year AFFO growth algorithm from 5–9% to 9–12%.** ⇒ **M132's conclusion (EQIX's fundamentals
  and flow disagree) SURVIVES; its stated evidence does not.** Use the guide, retire the +9.6%.
- **VTR's "current-quarter consensus −33.3%/90d" is STILL in the feed** (0.165→0.11). **Still GAAP.
  Still ≈1.6% of a ~$3.87 FFO base. Still not a signal.**

**★ What EQIX actually got sold for on 07-29**: shares fell ~3% because **Q3 revenue guidance
$2.53–2.58bn had a midpoint ~1% below the $2.58bn estimate** — while the **multi-year AFFO growth
algorithm was raised by ~4pp at both ends** and FY revenue guidance was raised. **One quarter's
revenue midpoint outweighed a three-year algorithm raise.** EQIX also carries **the sector's best
`delta` (+0.268)** on the same tape.

### B2 — margin percentile in the name's own history

⚠ **M233 CONFIRMED AND EXTENDED**: `scripts/margin_history.py PLD` returns **`연간 데이터 없음`** —
**and so does `DLR`.** ⇒ **No margin percentile exists for PLD or DLR. Their multiples are reported
as bare facts and NOT characterised as cheap or expensive (C3).** For the record: **PLD forward P/E
42.49 > trailing 32.20**; **DLR trailing 239.85 / forward 65.42**, both GAAP and both category errors.

**EQIX is the one name where the series runs** — 18 years, SEC XBRL, FY2008–2025:

| | value |
|---|---|
| **FY2025 gross margin** | **51.1%** on $9.2bn revenue |
| rank in own history | **2nd of 18** ⇒ **~94th percentile** |
| max / median / min | 52.6% (FY2015) / **48.9%** / 41.1% (FY2008) |

⇒ ★ **B2's answer for EQIX: 24.2× AFFO is being paid on profitability at the 94th percentile of its
own 18-year record, not on depressed margins.** The multiple is not obviously stretched **on that
metric**, but there is **no margin-recovery leg left to fund a re-rating** — the improvement would
have to come from the volume algorithm the company just raised. **Stated as a fact about where the
margin sits, not as a valuation verdict (C3).**

**Dispersion (W5)**: **IRM's analyst target range is $44 low vs $149 high — a 3.4× spread**, the
widest on this board, against a $123.92 price and a **Price/Book of −30.34 (negative book equity)**.
**SPG carries the sector's worst sell-side book — 1 Strong Buy / 6 Buy / 13 Hold / 1 Strong Sell,
mean target +1.8% upside — while holding the sector's only clean positive base (§2 Class D).**

---

## 8 · Track KPIs · anti-signals · dates

**Frozen KPI #1 — the two-geometry convergence test.** *(replaces last run's four-green KPI, which
named a green set that no longer exists — the sector has zero greens)*
**Group FRESH median segment 21-60 = −13.57 vs Group BASED median +4.76, spread 18.33pp, at
2026-08-03.** **A sector-wide move is one where this spread NARROWS. A rotation inside the sector is
one where it holds or widens.** Re-measure next rotating slot; **the spread, not the direction, is
the observable.**

**Frozen KPI #2 — the node that survived clustering.** **{DLR, EQIX, IRM} residual correlations:
DLR–EQIX +0.639, DLR–IRM +0.607, EQIX–IRM +0.530.** **If any falls below ~0.45, the one stable
structure in this sector is gone** and the data-centre node stops being a single bet.

**Frozen KPI #3 — stability itself.** **ARI 0.355 (was 0.5987).** **Re-report every rotation. Two
consecutive readings below 0.30 ⇒ the partition should not be used for any grouping claim at all.**

| Date | Observable | Why it settles something |
|---|---|---|
| **2026-08-07** | **NFP (S51)** | the rate path that sets node [1] |
| **2026-08-08** | **S25 window closes** | ⚠ **already scored ZERO-INFORMATION (D122)** — records the close, claims nothing |
| **2026-08-12** | **S41: IG OAS ≥ 0.90 (11bp away)** · **S26: HY OAS ≥ 3.10 (25bp away)** | **the binding variable of §3** |
| **~late Oct** | **EQIX Q3 print vs its own $2.53–2.58bn guide** | whether the "soft guide" that cost 3% was conservatism or deceleration |
| **~late Oct** | **VTR Q3 occupancy / RevPOR-ExpPOR spread** | ⚠ **still NOT in this repo's feed — named as a gap for a 2nd consecutive run, not proxied** |
| **no fixed date** | **Nexus/Anthropic $15bn syndicate closing or failing** | the cleanest single read on whether private capital is still bidding for the marginal gigawatt |

**Anti-signals — what would break the readings in THIS file (C2, applied to my own claims):**
1. **A listed REIT (DLR/EQIX) winning a gigawatt-scale hyperscale build-to-suit** ⇒ **§3's
   disintermediation reading is refuted.** This is the cleanest kill on my own central claim.
2. **EQIX walking back the 9–12% AFFO algorithm** ⇒ §7's "sold a raise" reading collapses into "the
   market was right early."
3. **VTR/WELL's RS damage continuing into Q3 WITH occupancy/RevPOR deterioration** ⇒ §0(d) is wrong,
   the reversion was operating after all, and the indictment wins that point retroactively.
4. **The Group FRESH names losing their RS20 as well** ⇒ Class C was a dead-cat refill, not a turn,
   and the sector genuinely has no leg.
5. ⚠ **Spread-widening is explicitly NOT listed as an anti-signal**, because §3(3) shows its sign on
   the listed data-centre node is indistinguishable. **The desk should stop treating S41 as a
   one-directional sector kill.**

---

## 9 · What this DEEP hands to BET

1. **The indictment is half-right and should be inherited in its corrected form.** Its arithmetic
   reproduces exactly. But its four names are **two measured risk units**, its 3-session leg is
   **77% beta-ordered (corr +0.767)**, three of the twelve board names were **positive** in that leg,
   and **"EXHAUSTED" is a misapplication of M149 to names with negative RS60** — you cannot exhaust
   excess that was never accumulated. **D154's guard disqualifies the ratio on 8 of 12 names.**
2. **There is no single sector run to be over. There are two inverse geometries** — eight names with
   a fresh leg and no base (median segment **−13.57**) against four with a base and no fresh leg
   (median **+4.76**), spread **18.33pp**. The indictment sampled one from each column.
3. **§1 partially CONCEDES the OW rationale.** The sector's green-count breadth is **0.000**, and
   "breadth-led" rests on a **+0.034 eqflow gap carried by 2 of 12 names.** BET should not inherit
   the word "breadth."
4. **{DLR, EQIX, IRM} is the one structure that survived re-clustering at every threshold**, and it
   now has the **lowest cross-unit correlations in the sector** — the most isolated bet on the board.
   **But ARI fell 0.5987 → 0.355**: trust the **pairs**, not the partition (M148).
5. **The value chain's bottleneck moved.** It is not demand (every disclosed number is up: AMZN
   raised capex, EQIX raised a multi-year algorithm, GOOGL cloud +82%, VTR SP-NOI +10%) and not
   near-term power. **It is the price of competing third-party capital** — and on the marginal
   gigawatt **the listed REITs are not the landlord.** ⚠ **Whether that is disintermediation or
   simply two different products is UNRESOLVED (C4).**
6. **M227's question answered, and the answer is two-sided.** Lease financing converts tenant capex
   into contractual credit (confirming M134 concretely: Google guarantees Anthropic's leases; Meta
   guarantees ~$13bn of residuals) — **but widening spreads also retire the REITs' cheapest
   competitor.** ⇒ **S41's sign on this node is indistinguishable. Do not inherit it as a kill.**
7. **M151 costs more than a level: it reverses the ranking.** GAAP says EQIX cheapest / VTR dearest.
   AFFO says **VTR 23.1× cheapest, DLR 23.5×, EQIX 24.2×, WELL ~35.6× dearest.** **M132's EQIX
   revision claim must be retired as stated (FY+1 is now −1.0%/90d, and it was always GAAP) while its
   conclusion survives on the company's own raised guide.**
8. **One flagged divergence for BET, not a candidate**: **MS is the lead bank on the window's loudest
   deal and carries the thematic table's worst delta (−0.420) with RS20 −5.70.** News co-mention
   against flow. **Nexus and Anthropic — the actual principals — are private and off this board.**

## ✅ Coverage

indictment answered with independent recompute ✅ (all 8 cited figures reproduced) · D154 guard applied
✅ (8 of 12 ratios disqualified, segments substituted) · flow ✅ (all 12 re-derived, OW rationale
partially conceded) · M131 re-tested ✅ (**ARI 0.355 disclosed per M148**, 2 resolutions per C5, 4 pairs
reproduced to <0.01) · chain map ✅ (8 nodes, 3 cross-sector marked, bottleneck = competing capital,
demand explicitly rejected as a bottleneck) · players ∪ thematic ✅ (bounded; **flow cross-checked on
every row; private principals excluded and named**) · W4 ✅ (4 customers, disclosed spend, funding-mode
split) · M227 ✅ (answered 3 ways, third contradicting the first two) · B2/M151 ✅ (**M233 confirmed AND
extended to DLR**; EQIX margin at 94th percentile) · KPI ✅ (3 frozen, all dated) · anti-signals ✅ (5,
including 3 aimed at this file's own claims) · C2 both halves ✅ · C3 unknowns named ✅ (XLRE exc60d
discrepancy, VTR RevPOR feed gap, hyperscaler lease-vs-own mix) · C4 ✅ (2 unresolved, stated) ·
W5 ✅ (RS5 range 13.0pp; IRM target spread 3.4×) · D6 ✅ (OBV corroborant only, never the claim) ·
S1 ✅ · **P4 — analytical only, zero position language, zero sizing.**
