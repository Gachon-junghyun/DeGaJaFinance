# SECTOR_DEEP_ENRG — Energy (OW−, held) · 2026-08-14 · CONTINUOUS track ⇒ **DELTA-led**

> Continuous slot, 3rd consecutive run (anti-thrash applied). **Leads with the delta**; unchanged
> structure is carried by reference to `llm_outputs/2026-08-13/industry_US/SECTOR_DEEP_ENRG.md`.
> Prices **pinned to the 2026-08-13 settled close**, benchmark **`SPY` inline (C1)**. Zero buy/sell (P4).
> ⚠ **Executed in-context, not as a parallel agent fan-out** — see `BLINDSPOT_PREMORTEM.md §0`.

## 1 · The mandate, answered first

ROTATION asked: **why is the level best-of-board while Δ is 2nd-worst, and is the expression refiners
or integrateds?** Decomposing the 16-name sector into five nodes answers both at once:

| Node | n | wflow | eqflow | med RS20 | **med RS60** | **med Δ** | OBV 매집 |
|---|---|---|---|---|---|---|---|
| **Refining** (`MPC` `VLO` `PSX`) | 3 | **+0.697** | **+0.696** | **+11.9** | **+27.3** | **−0.017** | **3 / 3** |
| Integrated (`XOM` `CVX`) | 2 | +0.420 | +0.427 | +4.5 | **−5.5** | **−0.165** | 2 / 2 |
| E&P (`COP` `EOG` `FANG` `OXY` `DVN`) | 5 | +0.142 | +0.001 | +1.3 | **−8.3** | **−0.257** | 2 / 5 |
| Midstream (`WMB` `KMI` `TRGP` `OKE`) | 4 | **−0.426** | −0.435 | −5.5 | **−9.2** | **−0.252** | 1 / 4 |
| Oilfield services (`SLB` `BKR`) | 2 | +0.154 | +0.191 | +7.8 | **−11.8** | −0.020 | 1 / 2 |

★★★ **The answer is unambiguous and it is the delta of this run: REFINING IS THE ONLY NODE WITH A
POSITIVE 60-DAY. Every other node's median RS60 is negative** (−5.5 · −8.3 · −9.2 · −11.8).
⇒ **the sector's entire 60-day performance is three companies at 11.1% of sector cap.**

★★ **And the Δ decomposition is equally clean.** Refining's median Δ is **−0.017 (flat)** while E&P is
**−0.257** and midstream **−0.252**. **`XOM` alone — 30.5% of sector cap at Δ −0.247 — contributes
−0.075 of the sector's −0.157, i.e. 48% of the entire delta decay.**
⇒ **The "best level / worst delta" paradox is not a paradox. It is two different businesses wearing
one GICS label, and the sweep's cap weighting reports the one that is decaying.**

## 2 · Delta since the 2026-08-13 deep — what actually changed

| | 08-13 deep | **08-14** | Change |
|---|---|---|---|
| `XLE` exc5 vs SPY | +6.140 (`R65`-corrected) | **+3.774** | narrowed, still positive |
| `XLE` exc20 / exc60 | — / −1.83 | **+3.467 / −4.519** | ⚠ **the 60-day got worse** |
| 3-2-1 crack | — | **65.84** | **+6.50 pts / 5 sessions**, still **below 69.45** (20 sessions ago) |
| `S67` | settling | **`FIRED-C`** — median{MPC,VLO,PSX} RS20 **+11.925**, band A ≤−2.20 / B ≥+13.56 | **1.635pp short of the with-us branch** |
| Sector Δ | +0.074 (08-12) | **−0.157** | ⚠ **reversed sign in two sessions** |

### 2a · ★ The second-derivative read the L1 requires (lens B1) — and it says the RATE turned up

Refining is a commodity node, so the level is the distraction and the **rate** is the signal:

| 3-2-1 crack | 20 sessions ago | 5 sessions ago | **2026-08-13** |
|---|---|---|---|
| Level | 69.45 | 59.34 | **65.84** |
| Change over the leg | — | **−10.11** | **+6.50** |

⇒ **the rate of change flipped from strongly negative to strongly positive.** Two legs is a small
sample (S5), but the sign flip is what B1 asks for, and it is corroborated by composition:
**products outran crude on the 5-day (`HO=F` +9.50% · `RB=F` +6.45% vs `CL=F` +5.12%)** — margin
expansion, not a barrel-price effect. ⚠ **On 08-13 itself the whole complex fell** (CL −2.43% ·
HO −1.24% · RB −0.81%), so the last observation in the series points the other way.

### 2b · ★★ The physical cause, which is new this run and is a PRIMARY-adjacent read
`chain-hop`/`fts` (bridge restored, `MACRO_REPORT §0`) returns named facilities and named capacity:
- *"Ukraine Strikes Gazprom's **200,000-Bpd Salavat Refinery** in the Urals"* [`oilprice` 08-13]
- *"Ukraine's drones hit a major Russian refinery **800 miles from the border**, sparking a fire"*
  [AP via `google_en` 08-13]
- *"**Drone Strike Sparks Blaze at Key Russian Oil and Fuel Terminal**"* [`oilprice` **08-14**]
- *"US refiners **ramp up buybacks** as Iran war boosts fuel margins"* [surfaced by `chain-hop` as a
  body-proximate article naming **`MPC`** and **`PSX`**]

⇒ **the crack's expansion has a named supply mechanism that is still firing, and it is REFINING
capacity being destroyed — not crude supply.** That is exactly why the refining node and the E&P node
are moving in opposite directions.
⚠ `refinery` is the fastest non-CPI term on the board (**1.61× pool-normalised**, 33 vs 21 hits).

## 3 · Valuation, with the margin percentile beside it (lens B2 — mandatory)

`margin_history MPC` (functional probe, `--help` broken — G7): gross margin **FY2025 10.0%** ·
median **10.5%** · high **FY2022 14.5%** · low **FY2020 5.8%**.
⇒ ★ **`MPC` sits essentially AT the median of its own 17-year margin history, not at a peak.**
**This is the opposite of the peak-margin/low-multiple trap.** B2's warning — *a cyclical at peak
earnings prints its lowest forward multiple because the denominator is peaking* — **does not apply
here**, because the denominator is mid-cycle.
⚠ **C4 scope**: this says the trap is absent; it does **not** say the name is cheap. **No valuation
claim is attached** — a margin percentile is one leg of a valuation, not a valuation.

## 4 · Value chain — 6 nodes, and the binding constraint

`crude supply → shipping/transit → REFINING CAPACITY → product inventory → distribution → end demand`

**Bottleneck = REFINING CAPACITY**, and it is binding for a physically verifiable reason: **capacity
is being destroyed** (200 kbpd struck 08-13, a terminal 08-14) while crude supply is **not**
constrained — OPEC **cut** its 2026 demand forecast on 08-13 and crude fell −2.43% the same session.
⚠ **Strong demand ≠ bottleneck**: the constraint here is **conversion**, which is why the crack
expands while the barrel falls. That divergence *is* the thesis.
⚠ **Cross-sector chain**: refining margin → distillate → **freight/airline cost** (M34's transmission,
carried) and → **the Fed's hike premium via headline energy CPI** (P57).

## 5 · Chain-hop candidates — body-proximate only, flow-crossed

`chain-hop Hormuz tanker --days 7 --scope foreign` returned `MPC` (3 proximate / 22 body) and `PSX`
(3 / 16) as **body-proximate, non-headline-named** — both already held.
🚫 **No new candidate is promoted from this sector.** The chain-hop table's other Energy entry is
`COP` (4 / 26), whose **RS60 is −5.3 and Δ −0.077** ⇒ **fails the flow cross-check**, and a news
co-mention alone is not a candidate.
⚠ `VLO` is **not** in the chain-hop output but **is** handed forward by EVENT_ALPHA Card 3 on flow
(+0.639, OBV 매집, RS20 +10.6, RS60 +27.3) — **the two instruments disagree about VLO and the
disagreement is recorded, not resolved.**

## 6 · Track KPIs and anti-signals — stated as observables

| Track KPI | Current | Reads |
|---|---|---|
| 3-2-1 crack level | **65.84** | vs 59.34 (5d) and 69.45 (20d) |
| median{MPC,VLO,PSX} RS20 − `XOM` RS20 | **+6.8pp** | the node-separation spread |
| refining node med Δ vs sector Δ | **−0.017 vs −0.157** | is the decay reaching refining? |
| `XLE` exc60 | **−4.519** | the window that has not turned |

**Anti-signals (what kills the OW−, as observables):**
1. **Crack falls ≥5 points while crude holds ±3%** ⇒ the margin story is over regardless of the
   strikes. *(shared verbatim with `P58` anti-signal (b) so the two objects cannot disagree silently)*
2. **Refining node median Δ turns ≤ −0.15** ⇒ the decay that has taken E&P and midstream has reached
   the only node that works.
3. **`S75` fires against us at the 08-19 settle.**
4. 🚨 **`S84` branch A (≤ −3.174 at the 08-21 settle)** ⇒ a Hormuz de-escalation compresses this
   sector *and* lifts the three tilts it is paired against — **the correlated-loss path PREMORTEM
   registered.**
⚠⚠ **`R47` binds: no stage may state "the distillate bottleneck released" as fact.** `S55` scored C
and the physical-vs-premium split is **still unseparated.** This file adds a *cause*, not a *split*.

## 7 · Verdict on the mandate

**The OW− is on refining, not on Energy.** Held unchanged (ROTATION declined the promotion to OW on
Δ −0.157). ⇒ **the honest statement of this desk's Energy position is a 3-name node at 11.1% of
sector cap, wearing an 11-sector label whose other 13 names are negative on 60 days.**
