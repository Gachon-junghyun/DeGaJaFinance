# SECTOR_DEEP_INDU — Industrials (UW−) · industry_US · 2026-08-21 · **PROMOTED 5th slot (PREMORTEM Lens 1)**

> Not an OW sector. **Promoted by PREMORTEM because `S99` and `S97` both settle on tonight's close and
> `S99`'s pre-settle meets all three of branch A's conditions** — a live sizing input, on a grouping
> question `G4` has failed **12 consecutive runs**. Last covered 2026-08-19.
> **No sizing, no buy/sell language (P4).** Settled bar **2026-08-20**; one `module_chart` read is
> **intraday 08-21** and is labelled. Benchmark **`SPY`** named inline (`C1`).

## 0 · ★★★ The finding: `S99` will probably fire branch A tonight, and branch A is the WRONG ANSWER

**`S99`'s pre-settle (08-14 → 08-20, 4 of 5 sessions):** `M` = EW{`ANET`,`AVGO`,`HPE`} exc5
**−6.517** · `E` = `ETN` exc5 **−6.252**. Branch A needs \|M\|≥3.0 ∧ sign(E)=sign(M) ∧ \|E\|≥1.5.
**All three conditions are already met, by wide margins.** If it settles there, the registered reading
is *"Industrials OW− contains a 5th AI-compute risk unit; the book's AI concentration is 5-of-12."*

🚨 **This file ran the successor test `S99`'s own annex named — the JOINT-LOADING regression — and it
says branch A's reading is wrong.**

`ETN` daily returns regressed on `XLI` **and** `XLK` jointly (the annex's specification, not a
correlation):

| Window | β`XLI` | t | β`XLK` | t | R² |
|---|---:|---:|---:|---:|---:|
| **60 daily obs** | **+1.402** | **+6.12** | **+0.620** | **+5.14** | 0.714 |
| **120 daily obs** | **+1.255** | **+8.17** | **+0.488** | **+4.90** | 0.628 |

⇒ **`ETN` loads on Industrials roughly 2.3–2.6× as heavily as on Technology, and BOTH loadings are
significant at t > 4.9 in both windows.** The answer is not *"`ETN` is AI-compute"*; it is
**"`ETN` is an industrial with a real, significant technology loading"** — and **a sign test on a
5-session window cannot separate those two states.**

**The raw correlations reproduce the annex's machinery control and STRENGTHEN it** (60 daily obs):

| pair | ρ | | pair | ρ |
|---|---:|---|---|---:|
| **`ETN`–`CMI`** | **+0.818** | | `ETN`–`ANET` | +0.719 |
| **`ETN`–`VRT`** | **+0.816** | | `ETN`–`XLI` | +0.763 |
| **`ETN`–`CAT`** | **+0.800** | | `ETN`–`XLK` | +0.726 |
| `ETN`–`PWR` | +0.748 | | `ETN`–`NVDA` | +0.568 |
| `ETN`–`GEV` | +0.736 | | `ETN`–`AVGO` | +0.533 |
| `ETN`–`AME` | +0.727 | | `ETN`–`HPE` | +0.484 |

**Three machinery/industrial names beat `ETN`–`ANET`, and every AI-compute name the desk actually
holds (`AVGO` +0.533, `NVDA` +0.568, `HPE` +0.484) is BELOW it.**
⇒ **`S99` settles as registered and is not withdrawn (`D242`) — but its branches do not contain the
answer, and this file says so BEFORE the settle** (`§4c`/`D48`).

★ **What this means for the number PREMORTEM computed.** Lens 4 wrote that a branch-A fire moves
AI-compute epicenter exposure from **19.8% → 23.57% of total assets (32.8% → 39.0% of invested)**.
**On the joint-loading evidence that re-classification is not warranted**: `CYCLE_EXPOSURE.json`'s
existing treatment — `ETN` as the **adjacent** layer at **$420.4** — is the better-supported one.
**The concentration guard should not be moved on `S99` alone.**

## 1 · ★★ And the diversification claim the desk carries is CORRECT — measured, for the first time

The carried §3a line calls `RTX` *"the defense group's beta, not its leader… the book's diversifier."*
**Measured on 60 daily observations: `ETN`–`RTX` correlation = −0.006.**
⇒ **The book's two Industrials holdings are genuinely, almost exactly uncorrelated.** The
diversification is real **inside** the sector, and it is real for a reason the label does not carry:
`RTX`'s own correlation to `XLI` is only **+0.360**.
⚠ **`G4`'s standing failure is exactly this pair**: 250d splits `ANET`↔`ETN`, 500d/750d merge them
(`--days` stated on the same line, per the revoked-rights rule). **The joint-loading and pairwise
numbers above are this desk's first direct evidence on the question, and they favour the 250d
answer.**

## 2 · Flow — the sector is the board's second-worst and the desk's position is not in it

**Sector: `wflow` −0.247 · `eqflow` −0.212 (rank 9 of 11) · **0🟢 / 13🔴 of 50** · breadth 0.00 ·
Δ −0.162.** exc5 **−1.276** (rank 10).

**The sector's true shape is a bimodal one**, and it is not defense-vs-rest:

| Sub-node | Names | flow | Read |
|---|---|---|---|
| **Services / data / payroll** | `TRI` **+0.700** · `ADP` +0.583 · `PAYX` +0.508 · `FAST` +0.449 | **+0.56 avg** | ★ **the sector's entire positive half is non-industrial** |
| **Aerospace & defense** | `AXON` +0.478 · `NOC` +0.356 · `GE` +0.208 · `RTX` +0.182 · `LMT` +0.133 · `GD` +0.025 · `LHX` +0.019 · `BA` +0.010 · `HWM` −0.391 · `TDG` −0.564 | **+0.05 avg** | ≈ flat, wide dispersion |
| **Electrical / power equipment** | `EMR` +0.301 · `AME` −0.048 · `ETN` −0.075 · `ROK` −0.601 · `VRT` −0.549 · **`GEV` −0.787 🔴** | **−0.29 avg** | 🚨 **the AI-power node is the sector's worst; `GEV` Δ −0.460** |
| **Machinery / transport / building** | `CAT` **−0.767 🔴** · `CMI` **−0.811 🔴** · `CARR` −0.811 🔴 · `ODFL` −0.822 🔴 · `TT` −0.840 🔴 · `GWW` −0.861 🔴 · **`HON` −0.898 🔴** · `UPS` −0.778 🔴 | **−0.82 avg** | the destruction |

**Top-to-bottom spread: 1.598 flow points against a sector `eqflow` of −0.212** ⇒ **`W5`/`B5` fires
again: the label is the wrong unit.** ⚠ **ROTATION declined to demote INDU on exactly this ground and
routed it here; this file confirms the reason.**

★ **The un-obvious part**: the **AI-power node is negative** (`GEV` 🔴, `VRT` −0.549, `ROK` −0.601,
`ETN` −0.075) at the same time as the **AI-compute node is at ≈the 5th percentile of two years**.
**Two layers of one cycle are weak together** — which is an argument *for* `S99`'s question and
*against* its branch labels: the co-movement is cycle-wide, not unit-membership.

## 3 · 🚨 The defense short axis turned as a GROUP, and the price axis does not show it

**FINRA daily short-vol z, settled 2026-08-20:**

| Name | z | 5v5 trend | OBV (sweep) | exc5 | exc20 | exc60 |
|---|---:|---|---|---:|---:|---:|
| **`NOC`** | **+2.43 🔴** | **+2.9▲** | 매집 | +0.07 | +2.39 | −0.33 |
| **`LMT`** | **+1.76 🔴** | −5.4▼ | 매집 | −2.47 | −2.80 | +5.64 |
| **`LHX`** | **+1.35** | **+8.6▲** | 매집 | **−4.28** | **−13.06** | **−15.33** |
| `GD` | +1.23 | −0.3· | 매집 | +0.21 | −2.19 | +10.42 |
| `RTX` **(held)** | +0.53 | −3.8▼ | 매집 | −1.75 | −1.81 | +17.02 |

**RULE D6 exemption for this table**: the C-grade OBV column is 매집 at all five and is printed
**only** so the reader can see that the **B-grade FINRA column disagrees with it** — no claim here
rests on OBV.

⇒ **Four of five defense names carry a positive short-vol z while all five accumulate on OBV.**
`D6` ranks the B-grade axis above the C-grade one; **on that ranking the defense node's flow reading
is negative, not positive**, and the sweep's 매집 is the weaker evidence.
⚠ **Defense EW excess vs `SPY`, settled 08-20**: 5-session **−1.645** · 20-session **−3.495** ·
60-session **+3.484**. **Ex-`LHX`**: **−0.985 / −1.103 / +8.187.**
⇒ **`M704`'s finding replicates: `LHX` is the group's only name negative on both 20d and 60d, and
removing it more than doubles the 60-day EW.** **`S97` settles tonight already inside branch A
(−5.557 against a −4.0 line)**, whose registered consequence is *"`M704`'s defense EW must be re-run
ex-`LHX`."* **This file has pre-computed that re-run so the scorer does not have to.**

★ **And the sector's single best momentum name is a defense name nobody on this desk carries**:
`AXON` exc60 **+57.82**, exc20 **+21.57**, flow +0.478, OBV 매집. **It has no thesis line, no bracket
and no ledger row** — the `R9`/`AXON` geometry the desk named its own exhaustion lens after, now
running again, uncovered. **Named rather than left out.**

## 4 · Value chain — 7 nodes, and the binding constraint is ELECTRICAL EQUIPMENT, not orders

| # | Node | Names | Constraint |
|---|---|---|---|
| 1 | **Defense demand / budgets** | (policy) | Not binding — backlogs at record (`S7` history) |
| 2 | **Primes** | `RTX` `LMT` `NOC` `GD` `LHX` | flow ≈ flat; **B-grade axis negative** (§3) |
| 3 | **Aero structures / aftermarket** | `HWM` −0.391 · `TDG` −0.564 🔴 · `BA` +0.010 | negative |
| 4 | ★ **Electrical / power equipment (the bottleneck)** | `ETN` `EMR` `AME` `VRT` `ROK` `GEV` | 🚨 **binding, and deteriorating**: `GEV` **−0.787 🔴 Δ −0.460**, `VRT` rs60 **−19.9** |
| 5 | **Construction & engineering** | `PWR` −0.108 · `EME` −0.375 · `FIX` −0.761 🔴 · `FER` −0.177 | the datacenter build's contractors, all negative |
| 6 | **Machinery / freight** | `CAT` `CMI` `DE` `UNP` `CSX` `NSC` `UPS` `ODFL` | **the destruction node** — `DE` is the exception (`vol_surge` **1.37**, Δ **+0.629** = sector's largest) |
| 7 | **Services / data** | `TRI` `ADP` `PAYX` `FAST` `CTAS` | the only positive node |

★ **Node 4 is the binding constraint and it is the one the desk's `ETN` position sits in.** The AI
build-out's *demand* is not in question; **the equipment layer's flow is the sector's worst**, and
`GEV`'s Δ −0.460 is the second-largest single-session deterioration on the whole board.
⚠ **`DE`'s Δ +0.629 (sector-largest, `vol_surge` 1.37) is NOT read as a signal** — it is one session
on a Δ-only basis and `D293` bars that. Logged for the next run's recency.

## 5 · Chart structure — `ETN`, **intraday 2026-08-21**, labelled

OBV **분배 −40%** (⚠ **contradicts the sweep's 매집 on the settled 08-20 bar** — different windows,
one includes a live bar; **neither is picked**) · divergence **none** · MA **강세스택 5>20>60>120**
with price above **2/4** · Bollinger expanding 26.3% · **RSI 40.9** · 20d momentum **+5.9%** · turn
**PULLBACK-TO-SUPPORT** · ignition trigger **close > 429.18** · swing-low stop **360.99**.
⇒ **A trend pullback, not a break** — and `RSI 40.9` with a 강세스택 is the structural definition of
one. **No verdict is drawn from a single intraday read.**

## 6 · KPIs and anti-signals

| Track KPI | Current (08-20 settle) | Note |
|---|---|---|
| **`ETN` joint loading β`XLI` : β`XLK`** | **+1.402 : +0.620** (60 obs, both t>5) | the successor test; **re-run each time `S99`-class questions recur** |
| `ETN`–`RTX` correlation | **−0.006** (60 obs) | the diversification claim, now measured |
| **defense EW exc20, ex-`LHX`** | **−1.103** (vs **−3.495** including it) | `S97`'s consequence, pre-computed |
| defense FINRA z, count ≥ +1.5 | **2 of 5** (`NOC`, `LMT`); ≥+1.2: **4 of 5** | the B-grade axis |
| `GEV` Δ | **−0.460** | node 4's deterioration |
| `AXON` exc60 | **+57.82** | uncovered, no thesis line |

**Anti-signals (as observables):**
1. **`S99` firing branch A tonight AND the joint-loading β`XLI`/β`XLK` ratio falling below 1.5 on the
   next 60-obs re-run** ⇒ the label re-classification would then be warranted and the concentration
   guard should move. **Currently 2.26×.**
2. **Defense EW exc20 ex-`LHX` turning negative beyond −3.0** ⇒ the group weakness is not one name and
   `M704`'s ex-`LHX` repair does not hold.
3. **`ETN` closing below its swing-low stop 360.99** ⇒ the PULLBACK read becomes a break.
4. **Node 4 (`ETN`,`EMR`,`AME`,`VRT`,`ROK`,`GEV`) EW flow staying below −0.25 for three runs** while
   AI-compute recovers ⇒ the electrical layer is being structurally de-rated, not cyclically weak.

## ✅ Sector-level resolution of the ROTATION divergence
ROTATION **declined to demote INDU `UW−` → `UW`** on the ground that *"the desk's actual position is
defense, whose OBV is 매집 at all four names."* **This file partially REFUTES that reasoning**: on the
higher-grade FINRA axis the defense node is **negative** (4 of 5 names z ≥ +1.2, two ≥ +1.5), and the
defense EW is **−1.645 / −3.495** on 5- and 20-session excess.
⇒ **The decline to demote still stands — but not for the reason ROTATION gave.** It stands because
**the sector's worst node (machinery/freight, −0.82 avg) is not where the desk is**, and because
**`RTX` and `ETN` are measured to be uncorrelated (−0.006)**, so the label's aggregate does not
describe either position. **The correction is recorded here rather than left in ROTATION's file.**
