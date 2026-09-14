# SECTOR_DEEP_ENRG — industry_US · 2026-09-05 (Sat) · **CONTINUOUS TRACK → DELTA-LED**

> Slot: continuous (held from 2026-09-02, still top-1 OW). Verdict today **`OW+`** (promoted).
> Structure carried by reference to `llm_outputs/2026-09-02/industry_US/SECTOR_DEEP_ENRG.md`;
> **this file leads with the delta.** Flow asof **2026-09-04 settled close**.
> ⚠ **Run in-context, not as a parallel agent fan-out** — session constraint, declared.
> **Analytical output only — no sizing, no buy/sell language (P4).**

## Δ1 · The thesis is RE-SPECIFIED, not confirmed: this is a distillate trade, not a barrel trade

The carried line (`M1245`) is *"Energy's OW is a CHAIN-POSITION bet whose centre of gravity is moving
upstream."* **Measured this run, that is now wrong in its direction.** Primary source: futures
settles, `auto_adjust=False`.

| 5-session change into 2026-09-04 | |
|---|---:|
| WTI (`CL=F`) barrel | **+8.08** (to 91.48, 79.0th pctile) |
| **Distillate crack** | **−0.37** (holding at **99.21 = the 95.6th pctile**) |
| **Gasoline crack** | **−19.64** (63.18 → **43.53**) |
| **3-2-1 blended crack** | **−13.22** (to 62.09) |
| **distillate − gasoline spread** | **55.68 = the 98.4th percentile of the trailing year** |

★ **`M1297` — the barrel rose and the refiner's BLENDED margin fell, because gasoline collapsed while
distillate held.** The centre of gravity moved **downstream and into one product**, not upstream.
⚠ **This reverses `P83`, which FIRED-B on 08-27 because the same spread had collapsed −13.562.**
Eight sessions later it is at a 98th percentile. Recorded as a fact about that observable's
volatility, **not** as a re-score (`D242`).

### ★ The QoQ rate-of-change series the B1 lens demands (this is a price-cycle node)

Quarterly **average** crack, and the **rate** series — the lens says the signal is *two consecutive
declines in the rate*, not the level:

| quarter | distillate crack | **QoQ %** | 3-2-1 crack | **QoQ %** |
|---|---:|---:|---:|---:|
| 2025Q1 | 28.46 | +21.6 | 20.71 | +21.6 |
| 2025Q2 | 26.97 | **−5.2** | 25.52 | +23.2 |
| 2025Q3 | 33.63 | +24.7 | 26.45 | +3.6 |
| 2025Q4 | 38.21 | +13.6 | 25.30 | **−4.3** |
| 2026Q1 | 51.16 | +33.9 | 32.06 | +26.7 |
| 2026Q2 | 64.47 | +26.0 | 50.96 | **+59.0** |
| **2026Q3 (QTD)** | **90.59** | ★ **+40.5** | **65.40** | **+28.3** |

⇒ **`M1311` [measured] — the distillate rate is ACCELERATING (+26.0 → +40.5) and the blended rate is
DECELERATING (+59.0 → +28.3), and NEITHER has printed two consecutive declines.** The B1 kill signal
has **not** fired on either series. **The two series disagree, and the disagreement is the node map**
(Δ3): distillate is the leg, gasoline is the drag.
⚠ **Contractual-band check, run before reading the rate as demand (`D-lens` escape hatch):** refined
products are sold into **spot/index-linked** markets — there is no floor/ceiling band pinning this
series, unlike the memory contracts that flattened MU's. ⇒ **the deceleration in the blended crack IS
gasoline weakness, not arithmetic hitting a cap.** Stated because the check is now mandatory.

## Δ2 · Flow: the tension the 09-04 run handed forward RESOLVED, in one session

| | 09-03 (carried) | **09-04 (today)** |
|---|---:|---:|
| `eqflow` | +0.506 | **+0.562 — rank 1 of 11** |
| Δflow | **−0.151 (rank 11)** | **+0.054 (rank 2)** |
| breadth | 0.12 | **0.19 — rank 1** |
| 🟢 / 🔴 | 2 / 0 | **3 / 0 — the board's only zero-red sector** |

⇒ ROTATION promoted `OW → OW+` on **that sign flip**, not on the level. ✅ Non-flipper: `XOM` is
30.5% of the bucket and the sector is **more** positive without it (`wflow` +0.440 → **+0.621**).

🚨 **`M1298` — and the sector's own shortlist is selecting the WRONG names.** The three 🟢 tags
(`SLB`, `WMB`, `CVX`) carry OBV +0.15 to +0.44 and rs20 +5.7 to +14.2. The three refiners are tagged
**🟡** on OBV **+0.43 to +0.62** and rs20 **+24.7 to +30.8**. The separator is `vol_surge`: refiners
print **1.05–1.15** against the gate's 1.2. ⇒ `M25`'s ENRG-shortlist artifact, measured live, on the
axis under `C29`. **No stage may read the refiners' 🟡 as weakness.**

## Δ3 · Value-chain node map — 6 nodes, with the binding constraint named

`barrel (upstream E&P) → gathering/midstream → REFINING → refined-product logistics → distributors/
retail → end-users (freight, air, ag)`

| # | node | names (`us_top300`) | flow / OBV / rs20 | read |
|---|---|---|---|---|
| 1 | **Upstream E&P** | `EOG` +0.635 · `COP` +0.639 · `DVN` +0.633 · `OXY` +0.553 · `FANG` +0.431 | all 매집 except `FANG` (중립); rs20 +6.3 to +14.6 | Participating, **not leading**. rs60 is **negative at 4 of 5** — the barrel's 20-day move has not yet become a 60-day one |
| 2 | Oilfield services | `SLB` +0.883 🟢 · `BKR` +0.308 | 매집; `SLB` rs20 +14.2 but **rs60 −2.6** | 🟢 on a **20-day** move only. ✅ short-cover z −1.21 |
| 3 | Midstream | `WMB` +0.769 🟢 (Δ **+0.347**) · `OKE` +0.689 · `TRGP` +0.442 · `KMI` +0.174 | `WMB` new-🟢 this session; `KMI` OBV 중립 | ★ **the frame-transfer answer, see Δ5** |
| 4 | ★ **REFINING — the binding constraint** | **`MPC` +0.694 · `PSX` +0.750 · `VLO` +0.700** | **OBV +0.621 / +0.434 / +0.482 매집** · rs20 **+30.8 / +25.5 / +24.7** · rs60 **+41.5 / +34.2 / +37.5** | **Strong demand is not a bottleneck; destroyed capacity is.** *"Why Oil Majors Don't Want to Build New U.S. Refineries"* [09-03]; *"Global Refining Crunch Could Keep Fuel Prices High Into 2027 — 'Refining capacity will not come back'"* [09-03] |
| 5 | Integrated | **`XOM` +0.027 · OBV −0.071 중립 · rs20 +4.6 · rs60 −0.3** | 🚨 **the sector's largest name is its weakest** | An integrated is long the barrel and short its own refining input; it captures the *level*, not the *spread* |
| 6 | **End-users (cross-sector: → Industrials)** | `FDX` −0.183 OBV **분산** · `UPS` −0.251 · `ODFL` **−0.343 🔴** · rails `NSC`/`UNP`/`CSX` ≈ 0 with Δ **+0.403 / +0.236 / +0.300** | | **The victims are visible in the flow**: parcel/LTL distributing, rails' Δ rising. ⚠ `R38` bars attributing the rail/truck split to fuel surcharge — the mechanism survived that retraction, the magnitude did not |

**Bottleneck: node 4, and it is a CAPACITY constraint, not a demand one.** The distillate crack at the
95.6th percentile with a **structurally blocked supply response** is the whole thesis. Gasoline's
−19.64 collapse in the same week is the direct evidence that this is **not** a general
refined-products bid.

**Chain-hop candidates: ZERO valid.** `chain-hop diesel refinery` returned `GOOGL` 16/95 ·
`GOOG` 16/95 · `META` 10/76 · `AMZN` 4/26 as its top four — **page boilerplate counted as body text
(`D10`, first quantification on `chain-hop`)**. The only survivor of a manual read is **`FDX`**, and
it is a **victim**, already at node 6. **No chain-hop name reaches BET from this sector.**

## Δ4 · 🚨 The primary-source finding that cuts AGAINST the promotion — insider-sale notices

`module_disclosure_us`, SEC EDGAR, Form **144** (notice of proposed insider sale), each name against
**its own** 365-day base rate:

| name | 144s / 365d | **144s / last 30d** | last-30 vs own monthly base | held? |
|---|---:|---:|---:|:--:|
| **`MPC`** | 20 | **7** | ★ **4.2×** | ✅ held |
| **`PSX`** | 25 | **6** | **2.9×** | ✅ held |
| `VLO` | 8 | **0** | **0×** | ✗ not held |

★★ **`M1312` [measured] — insider-sale notices at the two refiners the book HOLDS are running 4.2×
and 2.9× their own twelve-month base rate, while the one it does NOT hold is at zero.** The dated
cluster at `MPC` is 08-12, 08-17, 08-20, 08-24, 08-27, 08-28, 08-31 — **seven notices in twenty
days**, sitting exactly on the window in which the distillate crack went vertical.
⚠⚠ **Three honest limits, stated rather than argued around:**
- A Form 144 is a **notice of a proposed sale**, frequently a scheduled 10b5-1 execution. **It is an
  unsigned count** (`D3`): the *direction* is sale-side by definition, but the **share count and
  dollar value are `unknown` in this instrument** (`C3`) — the module returns form type and date only.
- **A rising base rate is what a rising price produces mechanically** (options vesting into strength).
  This is a correlation with price, not independent evidence.
- **`n` is small**: 7 and 6 events.
⇒ **Carried as a `[measured]` fact with its limits attached, and NOT used to argue against the
promotion** — but it is the single most concrete negative in this file and it belongs in front of
BET, not in a footnote.

## Δ5 · Frame-transfer question — answered, and one leg transfers

*"Name a frame this desk trusts elsewhere and say whether it applies here."*
The desk's take-or-pay / RPO / contracted-volume frame (applied to `KMI`'s $35.67B RPO, `LNG`'s
tolling, `VST`'s 20-year PPA floor, and — belatedly, on 08-10 — to `MU`'s take-or-pay memory
contracts).

- ❌ **It does NOT apply to node 4, refining margin.** Refined products sell at spot/index. There is
  **no floor, no ceiling, no contracted volume** to flatten the crack series. ⇒ **the margin is fully
  exposed to mean reversion and the desk should not import comfort from the KMI/LNG frame.**
  *"Checked, does not apply"* is the pass condition and this is it.
- ✅ **It DOES apply one node up.** `MPC` is a **three-segment** company — Refining & Marketing,
  **Midstream**, Renewable Diesel (per its own business description) — and the Midstream segment is
  MPLX, a contracted/fee-based structure of exactly the `KMI` type. ⇒ **the frame the desk trusts
  applies to a part of a name it holds, and no desk file has ever said which share.**
- 🚨 **`C3` — the contracted share is `unknown` and is marked so.** `module_disclosure_us --days 365`
  returns **three 10-Qs** for `MPC` but the module surfaces form/date, not segment text; **this run
  did not open the filing body**, so the Midstream share of operating income is **not stated here
  and is not estimated.** ⇒ registered as **`D514`**: *the desk's own take-or-pay frame has never
  been pointed at the Midstream segment of a refiner it holds, and the number needed to point it is
  one filing read away.* This is the "capability aimed at only one target" failure class, verbatim.

## Δ6 · Customers named, and their disclosed spend / print dates

The B-lens rule: a supply-chain verdict without the buyers' spend is missing its own demand side.

| customer node | named buyers | disclosed spend / print date |
|---|---|---|
| **Air freight & parcel** | `FDX`, `UPS` | 🚨 **Not read this run.** `FDX`'s next print is not in this run's window and the desk has **not** pulled it. The last read (`M34`, 2026-07) had fuel costs **+66% to +84% YoY** at `DAL`/`UAL`/`FDX`/`LUV` with **two cutting or missing Q3 guidance on fuel**. That is **six weeks old** and is labelled as such |
| **LTL / ground** | `ODFL` | **🔴분산, rs60 −27.4** — the worst RS in the whole node. The tape has already marked it |
| **Rail** | `NSC`, `UNP`, `CSX` | Δflow **+0.403 / +0.236 / +0.300**, all three among the board's top Δs. ⚠ **`R38` bars the surcharge attribution**; the divergence is stated, the cause is not |
| **Airlines** | *not in `us_top300` at the sector level* | ⚠ `DAL` is referenced in the 09-04 feed (*"Delta Air Lines Is Up 10% This Year"*, 5 outlets) but **airlines are outside this desk's universe** — an instrument gap, named |

⇒ **The demand side is confirmed as a COST, not as volume growth.** *"US diesel prices hit a record
high, **pushing up transportation costs for a long list of goods**"* [10 outlets]. **The refiner's
margin is the customer's expense line**, and three of four customer nodes are visibly weak in the
flow object. ★ **That is internally consistent with the thesis and it is also the mechanism by which
policy intervenes** — see the anti-signal.

## Δ7 · Valuation, with margin percentile and revision breadth (both required)

`module_fundamentals_us` `MPC`, 2026-09-05:

| | |
|---|---|
| Price / fwd P/E | **$388.90** / **12.24** (trailing 13.48, PEG 1.86, P/B 5.77) |
| Consensus mean target | **$326.83** ⇒ **−16.0% implied downside** (low 186 / high 413; 4 Strong Buy · 6 Buy · **8 Hold** · 1 Sell) |
| **Estimate momentum, 90d** | current qtr **+117.8%** (9.10 → 19.82) · next qtr **+83.5%** · this year **+?%** with breadth **14↑ / 0↓ (30d)** on the current quarter, **12↑ / 0↓** on the year |
| **★ Where margin sits in its own history** | quarterly operating margin: 5.61 → 4.81 → 5.67 → 3.03 → **13.42% (2Q26)**. Annual: 2022 **10.69** · 2023 8.48 · 2024 3.78 · 2025 4.35 ⇒ **2Q26's 13.42% is the highest print in the visible five-year series and is ABOVE the 2022 annual peak** |
| same, peers | `PSX` 3.57 → 2.80 → 4.75 → 0.35 → **8.39%** (annual peak 5.66, 2022) · `VLO` 3.34 → 4.69 → 5.19 → 5.35 → **11.68%** (annual peak 8.93, 2022) — **all three at five-year highs** |

★★ **`M1313` [measured] — the margin that set those five-year highs was earned in 2Q26, which ENDED
2026-06-30, on a distillate crack averaging 64.47. The current quarter is averaging 90.59, +40.5%.**
⇒ **The peak is not in the printed numbers yet.** The next print is **2026-11-03**, outside every
bracket this run holds.
⚠⚠ **`L2` peak-margin trap, stated in full and NOT resolved in the thesis's favour**: a forward P/E
of 12.24 on a denominator at a **five-year high** with estimates revised **+117.8% in 90 days on
14↑/0↓ breadth** is **consensus chasing, not cheapness** — and the tape is **16.0% above the
consensus mean target** with **8 of 19 analysts at Hold**. This is the exact basis on which `VLO`'s
rejection was reaffirmed on 09-04, and it applies to `MPC` and `PSX` identically. **`S147` (settles
09-14) is registered specifically to test EXTENDED-BUT-LIVE against this.**

## Δ8 · Chart structure (`module_chart --read`, `MPC`)

`OBV 누적 +52% (20d)` · divergence **none** · MA **강세스택 5>20>60>120, price above 4/4** ·
Bollinger **coiling 18.9%, upper band** · **RSI 76.0** · momentum20d **+21.7%** ·
**turn verdict: CONFIRMED-TURN** · swing-low stop **319.45**.
⚠ **RSI 76.0 is the overbought half of that reading and it is printed beside the confirmation, not
after it.** ✅ **`C25` does not fire**: the sweep (`obv_norm +0.621 매집`) and `module_chart`
(`누적 +52%`) **agree** on this name.

## Δ9 · Track KPIs and anti-signals, as observables

**Track KPIs (what would confirm):**
1. **distillate−gasoline spread ≥ its 85th percentile** at the 09-14 close (today **98.4th**).
2. **`refining margin` theme-age > 1.0×** — it has read **0.66× for three consecutive runs**, i.e.
   the narrative has *not* arrived. A turn here is the earliest available confirmation.
3. **`MPC`/`PSX` OBV state stays 매집** (today +0.621 / +0.434).
4. **The distillate crack QoQ rate does not print two consecutive declines** (today +26.0 → +40.5).

**Anti-signals (what kills it), as dated observables:**
1. 🚨 **A US federal policy action against refiner margins or fuel pricing.** The live thread is
   *"U.S. diesel price soars to more than four-year high **as Trump ramps up pressure on refiners**"*
   [seekingalpha, 09-01]. ⚠ **This is NOT in `P136`'s VOID clause** (frozen without it, and not
   amended — `D242`). **`S147` carries it explicitly.** ★ It is the anti-signal with the clearest
   mechanism, because Δ6 shows the margin is the customer's cost line, which is what makes it
   politically reachable.
2. An **announced Hormuz-open statement** (the `catalyst_calendar` TACO trigger, **undated** — written
   `[blank]`, not estimated) or an **OPEC+ emergency production decision**. Both are in `P136`'s VOID.
3. **The distillate−gasoline spread falling below its 50th percentile** — the single number that would
   say this is a general refined-products move rolling over rather than a distillate event.
4. **`MPC` or `PSX` OBV leaving 매집.**

## Δ10 · Sub-sector dispersion (`W5`) — is "Energy" the right unit?

5-session excess vs `SPY`, by node: **refining +25 to +31 rs20** · midstream +2.2 to +13.3 ·
E&P +6.3 to +14.6 · services +3.6 to +14.2 · **integrated `XOM` +4.6**.
The sector's own `exc5` is **+1.89 mean / +1.44 median with 1 of 16 negative**.
⇒ **Unlike IT, the label mostly holds here**: median ≈ mean and 15 of 16 participate. **But the
rs20 spread from `XOM` (+4.6) to `MPC` (+30.8) is 26.2pp**, and the flow spread from `XOM` (+0.027) to
`SLB` (+0.883) is **0.856** — **wider than the gap between the board's best and worst sectors**.
⇒ **`Energy` is a fine unit for a WIND direction and a poor unit for a POSITION.** The position-level
unit is **refining**, and `S147` brackets exactly that sub-node against `P136`'s sector-level one.

## Δ11 · The ROTATION divergence this file was asked to resolve

> *"Every flow and price instrument agrees; every news instrument decelerates."*

**Verdict: the divergence is REAL and it is a narrative-lag, not a flow error — and the file names
the one reading that would make it a trap.**
- The flow/price side is broad (15 of 16 participating, zero reds, breadth rank 1) and is
  corroborated by a **physical** series the news does not set (the distillate crack's QoQ rate,
  +40.5%). **A decelerating narrative cannot falsify a futures settle.**
- The trap reading, stated because it is the one that would hurt: **narrative deceleration at a
  95th-percentile physical extreme is what the LATE stage of a commodity move looks like** — the
  story is over because everyone already knows. `M1312`'s insider-sale cluster (4.2× base at `MPC`)
  and `M1313`'s five-year-high margin with a −16.0% implied downside to consensus are both
  consistent with that reading.
⇒ **The two readings are separated by ONE observable: whether the distillate crack's QoQ rate prints
its second consecutive decline.** It has not printed its first. **`P136` (sector, 09-14) and `S147`
(refiner sub-node, 09-14) are co-dated to force the answer**, and this file states the trap reading
now rather than discovering it at scoring.
