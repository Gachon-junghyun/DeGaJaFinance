# BET_SHEET — industry_US — 2026-07-22

> Stage 8/10. ONE file, per-sector sections (downstream desks glob this exact filename — never split).
> **Zero buy/sell recommendations, zero position sizing** (P4). Every RS figure is **vs SPY**; flow is
> asof **2026-07-21 close** (`SECTOR_FLOW_US.json`); fundamentals pulled **2026-07-22 pre-open**
> (`module_fundamentals_us --json`); FINRA short-vol z asof 2026-07-21. Written 06:5x ET, **US session
> not open**. Blanks are stated as blanks — nothing is guessed.
>
> Candidate set = (DEEP thesis leaders) ∪ (LIVE_SHORTLIST, incl. cross-sector) ∪ (PREMORTEM-promoted).
> ⚠ **Binding from PREMORTEM**: the Info Tech UW is re-scoped by name to memory + semicap; the
> security/observability node is excluded from it and appears here as §D. IT + Real Estate + Utilities
> may not be treated as three independent underweights — they are one AI-datacenter exposure.

---

## §A · ENERGY — the refining node (DEEP ①)

### A-1 Numbers

| Name | Px | P/E FY26 cons. | P/E FY27 cons. | FY26→FY27 cons. EPS | 30d rev. (FY26) | flow | RS20 vs SPY | RS60 vs SPY | FINRA z |
|---|---|---|---|---|---|---|---|---|---|
| **VLO** | 314.80 | **9.4x** | 13.8x | 33.46 → 22.88 = **−31.6%** | 9↑ / 3↓ | +0.689 🟡 | **+28.6** | +29.0 | −0.77 |
| **MPC** | 319.76 | **8.8x** | 11.9x | 36.26 → 26.91 = **−25.8%** | 4↑ / 2↓ | +0.583 🟡 | **+28.8** | **+39.0** | **+1.69 🔴** |
| **PSX** | 212.27 | 10.8x | 11.6x | 19.74 → 18.32 = −7.2% | 7↑ / 1↓ | +0.617 🟡 | +25.5 | +27.4 | +0.01 |
| **XOM** *(control)* | 151.71 | 13.6x | 14.2x | 11.18 → 10.66 = −4.7% | **1↑ / 3↓** | +0.578 🟡 | +9.0 | **−4.8** | +0.74 |

★ **The margin percentile sits next to the multiple, as the rule requires: the self-computed 3-2-1 crack
closed $68.23/bbl on 07-21 = the 99.5th percentile of 3 years** (3y range $14.4–69.5). The 8.8–9.4x is a
**peak-denominator** multiple. **This does not need to be asserted — consensus already models it**: the
sell side carries FY27 EPS **−31.6% (VLO)** and **−25.8% (MPC)** below FY26.

### A-2 Thesis + freshness *(ALPHA fills the tag)*
Refining margin, not crude beta, is the object. Binding constraint identified in DEEP: **middle-distillate
conversion capacity in the Atlantic basin** — distillate crack **$88.41** vs gasoline **$58.14**, a
**$30.27 gap** — with Europe drawing (Russian export ban, Fujairah middle distillates −15% MoM). ⚠ **The
constraint binds in Europe, not the US**: US distillate inventories built **+2.3mb then +1.759mb** in
consecutive weeks. US Gulf refiners are levered to the **export arb**, a more fragile object than a
domestic shortage. One structural leg survives any truce: **VLO's 10-K discloses Benicia (170k BPD)
ceasing refining by end-April 2026** out of a 3.19M BPD system.
**Freshness (ALPHA, 2026-07-22):** 🟡 **PARTIAL** — `theme-age "refining margin" --scope foreign` =
**🟡ACCELERATING, age 54d, 7d avg 2.6 articles, accel 8.57×, n=30**. This is an **old theme re-igniting**,
not a golden-zone birth, so it needs *stronger* live evidence to survive. **Residual that keeps it off
🟢:** the crack sits at the **99.5th 3-year percentile** and the detachment counter is at **3**.
⚠ `theme-age "diesel crack spread"` returned **⚫SILENT, n=0** — that is a **term artifact** (the desk's
phrase, not the feed's), *not* evidence of quiet. Same failure class as the quoted-bucket trap.

### A-3 Flow / positioning cross-read
All four names are 🟡 **only** because of the `vol_surge<1.2` gate; all four carry OBV accumulating **and**
RS20>0 (C-grade OBV is corroboration; the A-grade RS pair carries the read). ⚠ **Participation is thin
and that is real, not an artifact**: only 4 of 16 Energy names pass the OBV+RS20 pre-gate at all — the
other 12 fail on OBV (SLB, BKR, OKE, DVN distributing) or RS20 (WMB −2.6, KMI −0.1). **MPC is the only
FINRA short-vol spike (z +1.69, base20 56.3%→66.1%)** — C-grade, carries nothing on its own. PSX's
07-21-flagged z +2.01 has **fully normalized to +0.01**; that anti-signal is spent, not confirmed.

### A-4 Competition / peers
XOM is the deliberate control: **RS60 −4.8 vs SPY against MPC's +39.0**, and it is the only one of the
four whose **estimates are being cut (1↑/3↓)**. Integrated names dilute the crack into upstream beta.
Services are the chain's weak node (**SLB RS60 −20.5, BKR −18.2 vs SPY**).
⚠ **Coverage hole (a finding, not something to substitute around):** the entire independent-refiner tier
(**PBF, DINO, CVI, DK, PARR**) and the whole tanker/Hormuz-transit leg (**FRO, STNG, INSW, DHT**) are
**not in `us_top300`**. The refining epicenter is reachable from this universe through exactly three
large caps; the transit expression is not reachable at all.

### A-5 Refutation + dated catalysts
- **Detachment counter (the prior run's own falsifier) is now at 3**: on 07-17, 07-20 and 07-21 the crack
  fell every session (**69.41 → 69.33 → 68.23**) while crude rose **+7.5%** and all three refiners rose
  every day. VLO's daily increment decayed **+3.13 → +1.18 → +0.48**. Three observations is
  **indistinguishable** from noise on its own — carried as a counter, not a conclusion. **At 5 the equity
  is priced off something other than its KPI.** Next reading: **2026-07-22 close.**
- **Second-derivative rule fired once already**: weekly crack rate **+6.42 → +4.21 → +2.08** (06-28 →
  07-12) = two consecutive declines in the rate — then overwritten by the 07-10 truce collapse (+5.71).
- **Revision second derivative**: VLO current-quarter **+2.42 → +0.49 → −0.02 → +0.12** (rolling), but the
  **out-quarter is accelerating up** (VLO +1.80, MPC +2.76 in the last 7 days). A single-digit multiple
  whose out-quarter estimates are being marked up fastest on a 99.5th-percentile margin is **consensus
  chasing the print, not cheapness.**
- **Anti-signals (observables):** two consecutive weekly crack means **<$60.00**; distillate−gasoline gap
  **<$15**; a 3rd and 4th consecutive US distillate build with the crack still >95%ile.
- **Dated:** EIA inventories **07-22 (today)** and **07-29** · WTI COT **07-24** (S8's frozen cross-check)
  · customer prints **LUV 07-23**, **UPS 07-28** · **VLO 07-30 · XOM 07-31 · MPC 08-04 · PSX 08-05**.
- **Bracket S8 is frozen and governs this section**: crude down **with cracks rolling** = against us;
  **crude down with cracks holding is NOT against us** (input-cost relief).
- ⚠ **Gap this run did not close:** DAL (07-10), UAL (07-16) and FDX (06-24) already printed inside the
  war window and their fuel-cost lines were **not pulled**. Named, not filled with a guess.

---

## §B · FINANCIALS — non-bank mandate (DEEP ②)

### B-1 Numbers

| Name | Px | fwd P/E | ttm P/E | P/B | 0y EPS Δ30d | 0y rev. 30d | Px vs consensus target | flow | RS20 / RS60 vs SPY | FINRA z |
|---|---|---|---|---|---|---|---|---|---|---|
| **GS** | 1085.56 | 14.80 | 16.29 | 2.96 | 59.49 → 70.64 = **+18.8%** | **9↑ : 0↓** | −2.5% (tgt 1112.85) | **−0.450 🔴** | −2.4 / **+10.9** | **−0.11** (was +1.59) |
| **STT** | 183.30 | **12.02** | 16.18 | 2.11 | 12.48 → 13.57 = **+8.7%** | **4↑ : 0↓** (all periods) | −6.9% (tgt 196.90) | +0.751 🟢 | +5.0 / +15.6 | **−0.13** (was +1.50) |
| **TRV** | 369.63 | 12.39 | 9.90 | 2.33 | 28.15 → 31.17 = +10.7% | 2↑ : 0↓ | **+9.7% ABOVE** (tgt 336.92) | +0.906 🟢 | +18.5 / +14.6 | **−2.00** covering |
| **CB** | 354.80 | 12.15 | 12.55 | 1.87 | 27.09 → 27.13 = **+0.1%** | 2↑ : 2↓ | −1.5% (tgt 360.30) | +0.822 🟢 | +8.6 / +1.0 | **+1.61 🔴** |
| **USB** | 63.71 | **11.02** | 12.72 | 1.64 | +2.7% | 4↑ : 1↓ | −8.5% (tgt 69.66) | +0.783 🟢 | +8.0 / +6.9 | +0.96 |
| **PYPL** | 55.85 | 9.71 | 10.48 | 2.49 | **+0.06%** | **0↑ : 3↓** (all in 7d) | **+6.5% ABOVE** (tgt 52.42) | **+1.000 🟢** | +31.4 / +6.6 | −0.32 |
| **AON** | 359.40 | 16.81 | 19.73 | **7.81** | **−0.1%** | **1↑ : 3↓** (0q 1↑:5↓) | −8.6% (tgt 393.11) | +0.395 🟡 | +14.1 / — | — |
| **MET / PRU** | 93.37 / 118.59 | 8.50 / 8.15 | 18.06 / 12.21 | 2.21 / **1.29** | −0.1% / +0.3% | 0q 1↑:2↓ / +1y 3↑:4↓ | −2.7% / **+13.7% ABOVE** | +0.571 / +0.639 | +6.1 / +17.1 · +9.0 / +20.1 | — |

★ **The sharpest fact on the sheet: the market is paying up for flat denominators and selling the fastest-
rising one.** CB **+0.1%**, PYPL **+0.06%**, AON **−0.1%** are bid; **GS's current-year EPS rose +18.8% in
30 days on 9↑:0↓ and its flow is the sector's worst (−0.450)**. GS's current-year multiple compressed
~18.2x → **15.4x on the earnings raise alone** — the signature of a **de-rate against an activity peak**,
not credit and not rates.

### B-2 Thesis + freshness
**"Financials" is the wrong unit and the sheet says so**: the sector's rs20 spread vs SPY is **44.4pp**
against a **median name move of +6.1** — **7.3× the sector's own central move**. Five analysable units:
(i) **super-regional NIM** — the actual 2s10s (+0.39) expression: USB +0.783, PNC +0.647, FITB +0.642,
HBAN +0.622, all above JPM +0.420 / BAC +0.318 / WFC +0.328; (ii) **P&C underwriting** into a softening
pricing cycle (TRV, CB) — TRV's combined ratio **83.6% from 90.3%** is an underwriting number, not a
curve number; (iii) **custody fee/NII on AUM levels and the front end** (STT — Fed funds 3.63% flat, 2y
4.21% flat; nothing there is a 2s10s trade); (iv) an **IB activity peak de-rating against rising
estimates** (GS, MS, IBKR — all positive RS60, negative RS20 vs SPY); (v) two orphans (PYPL = M&A, and
**C is the only genuinely broken bank**: −9.3 RS20 / −2.3 RS60 vs SPY).
**Freshness (ALPHA, 2026-07-22):** split by sub-leg —
**P&C (TRV, CB) 🟡 PARTIAL**: `theme-age "reinsurance pricing"` = **🟢FRESH, age 5d** — but **n = 1**, so
the freshness verdict is **indistinguishable from noise on count alone** and is carried on the two named
primary sources (Arch 07-17, WRB's own call 07-20), not on the tag. **The fresh thing is the bearish
constraint**, which is why the leg cannot be 🟢. Residual: TRV **+9.7% above** consensus target with
**+1y EPS below 0y**, and a GS **Sell/$350** on 07-20.
**GS dislocation 🟢 LIVE** — no catalyst required; it is a live, measurable divergence (0y EPS **+18.8%
in 30 days, 9↑:0↓** against the sector's **worst flow, −0.450**). **STT 🟢 LIVE** (4↑:0↓ across all four
periods, 12.02x fwd, −6.9% to target). **USB 🟢 LIVE** as the super-regional steepener expression.
**PYPL 🔴 RESOLVED → DROPPED** — it is an **M&A situation, not a fundamentals bet** (0y EPS +0.06%,
revisions **0↑ : 3↓ all inside 7 days**, price **+6.5% above** target). Logged so "flow +1.000, the
board's best" cannot resurface next run as if it were a thesis.

### B-3 Flow / positioning cross-read
Financials is the only sector with **eqflow +0.357 > wflow +0.212** — breadth-led, 5 of the board's 11
greens. **Both 07-21 crowded-short anti-signals are now SPENT, not confirmed**: GS z +1.59 → **−0.11**,
STT z +1.50 → **−0.13** (the prior file's own 3-session falsifier fired). The new crowded short is
**CB z +1.61 🔴** (5v5 +14.8▲) and **TRV z −2.00** = extreme covering. C-grade throughout — corroboration only.

### B-4 Competition / peers
The sell side is leaning against the OW's flagship: **Goldman Sachs downgraded Travelers to Sell, $350
target (07-20)**, TRV's rating book moved to **3 sell + 2 strongSell** this month from 0 sell + 3
strongSell, and TRV trades **9.7% above** consensus target and 0.6% below its 52-week high — while its
**+1y EPS (29.17) sits BELOW its 0y (31.17)** and fwd EPS 29.83 vs ttm 37.33 = **−20.1%**. The Street is
already modelling the underwriting cycle rolling.

### B-5 Refutation + dated catalysts
- ★ **The binding constraint on the insurance leg is named and is confirming AGAINST the leg: P&C /
  reinsurance pricing is softening.** Arch Capital (07-17); **W. R. Berkley's own Q2 call (07-20):
  "pricing is becoming more competitive in parts of property and reinsurance"**, with its Reinsurance &
  Monoline Excess loss ratio **57.7% vs 53.1% estimated**. **This, not the real-yield branch, is what most
  plausibly ends the P&C bid.**
- **The insurance-broker air pocket**: AJG **+18.2** / AON **+14.1** RS20 vs SPY on estimate books of
  1↑:3↓ (AON 0q 1↑:5↓). Brokers have **no float to reinvest** — if this were a real-yield trade they
  would not be leading it. Falsifier: RS20 vs SPY crossing 0 with revisions still net-down.
- **S9 (dovish real-rate branch) is bracketed but mis-aimed at this sector**: tested name-by-name,
  S9-A (real 10y <2.20% with breakeven rising) hits **zero of the five FIN greens cleanly** — TRV/CB are
  second-order to the combined ratio, USB is *helped* by a front-end-driven steepening, STT is front-end
  geared, PYPL is rate-neutral. The genuinely rate-levered leg is **3 names of 47** (MET, PRU, AFL) and it
  is already decelerating (negative flow deltas at MET −0.029, AFL −0.058).
  ⚠ **The correlation error is relocated, not dismissed**: if the Real Estate and Utilities UW is expressed
  at *sector* level, the desk shorts **WELL (+16.0) and VTR (+17.0) RS20 vs SPY** — the duration longs its
  own rationale says to be short. Classic-duration REIT mean RS20 **+9.7** vs digital-infra REIT mean
  **−8.5** = an 18.2pp spread inside a 12-name sector.
- **Credit (P2) gains a second, independent evidence class** — from borrowers' books rather than spreads:
  provisions/NCOs down at **KEY** (direction sourced, magnitude **[blank]** — 63.7% body-blind), **TFC**
  ($395M, below NCOs), **MTB** ($120M, NCOs 23bp), **WFC** (10bp), **USB** (0.53%), **ALLY** (−18bp),
  **UCB** (9bp). Exceptions (FSUN, BayFirst) are sub-$10B-cap, i.e. idiosyncratic. ⚠ Two honest limits:
  provisions **lag** (Apr–Jun window says nothing about July), and **COF's level is high** (3.4% total,
  4.x% card) even though the trend is benign. **Kill line untouched: HY OAS >3.10% on a close** (now
  2.69%, 6bp off a 365-day low), or NFCI positive-ward two weeks running (now −0.538).
- **Dated:** **FOMC 07-28~29** · **CB z test by 07-24** (same 3-session test GS just passed) · a second
  carrier calling reinsurance pricing competitive **by 07-31** would confirm the softening constraint ·
  V/MA fiscal-Q3 late July `[exact date blank]`.

---

## §C · INDUSTRIALS — defense/aero (DEEP ③, PREMORTEM-promoted)

### C-1 Numbers

| Name | Px | fwd P/E | PEG | FY26 est vs 90d | 30d rev. (0y) | flow | RS20 / RS60 vs SPY | FINRA z | % below 52w high |
|---|---|---|---|---|---|---|---|---|---|
| **GD** | 367.73 | 20.2x | 2.74 | **+2.43%** | **3↑ / 0↓** | **+0.508** | **+6.6 / +9.8** | **−1.53 covering** | −3.4% |
| **RTX** | 193.67 | 25.5x | 2.65 | +1.18% | 2↑ / 0↓ | +0.444 | +6.0 / +2.4 | +0.13 | −9.7% |
| **LMT** | 507.09 | **15.8x** | **1.08** | −0.14% | 1↑ / 1↓ | −0.010 | +2.2 / **−9.9** | +0.44 | −26.7% |
| **NOC** | 512.29 | 16.9x | 3.90 | ⚠ **stale** | 1↑ / 0↓ | +0.087 | +0.5 / **−18.4** | **+2.27 🔴 building** | −33.8% |
| **LHX** | — | — | — | — | — | −0.298 | −3.4 / **−21.5** | −1.86 | — |
| **AXON** | 511.17 | **48.6x** (ttm 204.5x) | — | **−1.24% (CUT)** | +1q **8↑ / 9↓** | +0.444 | **+24.1 / +24.6** | +0.78 | **−42.3%** |

⚠ **NOC's vendor consensus is stale**: the module reads FY26 27.9501 against NOC's own **07-21 guidance
raise to $28.60–29.10**. Its revision block is **not current and is not used as evidence.**

### C-2 Thesis + freshness
**The sector number is a weighted average of two opposite things, and DEEP measured the split**:
capital goods + electricals = **25 names, 52.3% of sector mcap, wflow −0.455, and 14 of the sector's 17
reds** (PWR −0.800, VRT −0.817, CAT −0.678, DE −0.593); the **5 primes = wflow +0.250 with ZERO reds**.
A **0.705-point flow spread inside one GICS label.** ROTATION's N− is a correct statement about the
sector's *mass* and a false statement about defense.
⚠ **But it is a 20-day turn, not a 60-day lead, and the sheet will not overstate it**: decomposing days
21–60 (RS60−RS20 vs SPY), **four of five primes lost to SPY** — GD +3.2, RTX −3.6, LMT −12.1, LHX −18.1,
NOC −18.9 — and the median prime RS60 is **−9.9 vs SPY**. The RS20 recovery is coincident with the strike
campaign that began 07-11. **GD is the only prime positive on both horizons.**
⚠ "Aerospace & Defense" is *also* the wrong unit — it mixes the primes with commercial aero
(**BA −0.725, RS60 −18.2 vs SPY**; TDG −0.707; HWM −0.581), which is paid by OEM build rates, not a budget line.
**Freshness (ALPHA, 2026-07-22):** **🟡 PARTIAL, pending S7.** `theme-age "munitions replenishment"`
returned **🔴FADING on n = 1** — ⚠ **a FADING verdict on one article is not a measurement**; it is
recorded as **indistinguishable** and the leg is carried on the primary sources instead (Hegseth's
07-21 **$87.6bn** testimony, the **LMT $35B** interceptor award). **GD 🟢 LIVE** — the only clean
3↑/0↓ revision book, best flow, short-vol covering (z −1.53), positive on both RS horizons; prints
**07-29**, outside S7. **RTX / LMT 🟡 PARTIAL** — frozen behind S7's 07-23 observable.
**AXON 🔴 RESOLVED as a defense thesis → DROPPED from this bucket and logged**: its customer is
municipal/state public safety with **no customer >10% of net sales**, its FY26 estimate was **cut
1.24%** while price outran SPY by 24.6pp, and its 10-K contains **no backlog line at all**. It is a
multiple story; it may not re-enter as "the most accelerating defense name" next run.

### C-3 Flow / positioning cross-read
GD: best flow, only clean 3↑/0↓ revision book across every period, **short-vol covering (z −1.53)**, and
the only positive RS pair. NOC is the mirror: **z +2.27 building** with RS60 −18.4 vs SPY. LHX's z −1.86
means shorts **left**, which is not accumulation.

### C-4 Competition / peers — **AXON is a multiple story, not an order story**
The PREMORTEM promoted this slot partly on AXON. **DEEP refuted that half of the case, which is what the
stage is for.** Over the window in which AXON outran SPY by **+24.6pp**, its **FY26 EPS estimate was CUT
1.24%** and the next quarter **0.81%**, with +1q revisions **8↑ / 9↓** and strongSell going **0 → 1**.
The word **"backlog" does not appear in its 10-K** — the only disclosed forward metric is ARR $1.3B.
**W4 — its customer is not a defense budget line**: the 10-K says municipal/state/federal public safety
with **"no customer represented more than 10% of total net sales."** The 07-23 primes binary and the
$87.6bn Pentagon supplemental **do not transmit to it.** And RS20 +24.1 ≈ RS60 +24.6 means days 21–60
contributed **+0.5pp** — ~98% of the excess was earned in the last 20 days, **the identical shape S8
adjudicated at VLO as a 20-day event, not a trend.** Level context nothing else in this run stated:
**−42.3% from its 52-week high.** Next catalyst **2026-08-04 — outside this run's window.**

### C-5 Refutation + dated catalysts
- **S7 is frozen and NOT moved**: RTX **±5.0%** / LMT **±5.4%** (expiry D2), observable = **backlog /
  book-to-bill at both**, **2026-07-23**, one binary (**n≈1** by fold-by-date). Branch B (**one outside,
  one inside**) = **split, no verdict** — a 50-name breadth cut is not overturned by a single primes re-rate.
- **GD prints 2026-07-29 and must NOT be folded into S7.**
- **W4 disclosed spend, dated:** Hegseth testified **07-21** seeking **$87.6bn** additional Pentagon
  funding citing munitions shortfalls, after putting the Iran war cost at **$37.5bn** [4 articles / 3
  outlets]; a signed **LMT $35B interceptor** award is in-window. ⚠ The $87.6bn is **contested and undated**.
- **News-vs-money (d):** of three defense threads, **one has money.** The China drone-import ban and the
  uncrewed-fighter story have **no in-universe epicenter** (AVAV/KTOS out of universe; Anduril, GA-ASI,
  Skydio private; this week's CCA bodies are a BAE/GCAP UK-European program story) and the in-universe
  adjacent moves the wrong way (**BA RS60 −18.2 vs SPY**). Only the **munitions-replenishment** leg carries
  both money and a dollar figure.
- **Nuclear leg verified removed** (EVENT_ALPHA Card 6): **BWXT, SMR, CCJ, LEU all confirmed NOT in
  `us_top300`**. Only GEV has real transmission (GE Hitachi BWRX-300) and it is immaterial to its own P&L
  at **RS20 −4.8 / RS60 −11.8 vs SPY**. ⚠ **GE is a chain error** — GE Aerospace and Vernova separated in
  2024, so GE's +15.0 RS60 is engine aftermarket with **zero** nuclear content. ETN is generic.
- **Binding constraint** named in DEEP: **energetics / solid-rocket-motor capacity** — and it is flagged
  **structurally unownable in this universe**.
- **Zero chain-hop candidates PASS** (all 8 emitted are proximity artifacts).

---

## §D · SECURITY / OBSERVABILITY — excluded from the IT underweight (EVENT_ALPHA Card 3 → PREMORTEM)

This node exists on the sheet because the blanket IT UW would otherwise short the four cleanest live
instances of the desk's only A-grade verified signal. **It is presented with its own refutation, not as a
recommendation.**

| Name | Px | fwd P/E | ttm P/E | PEG | 0y EPS Δ90d | 0y rev. 30d | +1y EPS Δ90d | +1y rev. 30d | Px vs target mean | RS20 / RS60 vs SPY | flow | Next earnings |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **DDOG** | 254.79 | 88.4x | **670.5x** | **1.61** | 2.152 → 2.422 = **+12.5%** | 1↑ : 1↓ | 2.639 → 2.881 = **+9.2%** | 4↑ : 1↓ | **−0.1% (at target)** | **+14.6 / +93.7** | +0.472 | **2026-08-06** |
| **FTNT** | 158.10 | 46.1x | 61.3x | 3.65 | 2.980 → 3.158 = **+6.0%** | **39↑ : 0↓** | 3.310 → 3.426 = +3.5% | **39↑ : 0↓** | **+31.8% ABOVE** (tgt 119.92) | +8.2 / +85.4 | +0.384 | **2026-07-30** ★ |
| **CRWD** | 191.15 | **122.4x** | n/a (loss) | **6.6** | 1.213 → 1.232 = +1.5% | 47↑ : 0↓ | 1.543 → 1.562 = +1.2% | 39↑ : 6↓ | +1.0% above (tgt 189.18) | +12.7 / +66.0 | +0.511 | 2026-09-02 |
| **PANW** | 342.15 | 82.9x | 302.8x | 3.97 | 3.691 → 3.773 = +2.2% | 47↑ : 1↓ | ⚠ 2.299 → **1.951 = −15.1%** | **3↑ : 7↓** (8↓ in 7d) | +3.3% above (tgt 331.34) | +18.9 / +91.9 | +0.539 | 2026-08-19 |

**Refutation, per name — the differentiation the RS ranking cannot give you:**
- **DDOG has the best combination and appeared in NO stage of this run** until the pre-mortem found it:
  the fastest-rising denominator (**0y +12.5% / +1y +9.2% over 90 days**), the **lowest PEG (1.61)** of the
  four, and it trades **at** consensus target. Its trailing 670.5x is the honest counterweight — this is a
  forward-earnings story with essentially no trailing earnings base.
- **FTNT has the cleanest revision breadth on the sheet (39↑ : 0↓ on both 0y and +1y)** and the **worst
  price-vs-target gap of any name in this file: +31.8% above consensus target.** Both are true and they
  point opposite ways. ★ **It is also the only name in §D with a catalyst inside the near window —
  2026-07-30.**
- **CRWD is the most expensive on both axes** (fwd **122.4x**, PEG **6.6**) with the *slowest* estimate
  growth of the four (+1.5% / +1.2%). Its 47↑:0↓ breadth is real but the level is barely moving.
- **PANW's out-year book is being cut** (+1y 3↑ : 7↓, 8 downgrades in 7 days) even as the current year is
  raised 47↑:1↓. ⚠ **Data caveat, stated rather than banked**: 0y 3.773 against +1y 1.951 is a −48% step,
  which is implausible for this business and points at a **fiscal-period definition artifact** in the
  vendor feed. **The −15.1% is flagged, not used as evidence**, pending a second source.

**Freshness (ALPHA, 2026-07-22):** `theme-age "AI security" --scope foreign` = **🟡ACCELERATING, age
77 days, 7d avg 5.3 articles, accel 3.05×, n=156** — a **77-day-old theme re-igniting**, i.e. **not the
golden zone**, so per the gate it needs stronger live evidence than a fresh theme would.
⚠ `theme-age "agentic AI risk"` returned **🔴FADING on n = 2** — **that is not a measurement**; it is
the desk's phrasing, not the feed's, and is recorded as **indistinguishable**, not as a fade.
Per-name: **FTNT 🟢 LIVE** — the only §D name with a catalyst inside the near window (**2026-07-30**) and
the cleanest breadth (39↑:0↓ both periods); ⚠ carried with its own contradiction, **+31.8% above
consensus target**, the widest premium in this file. **DDOG 🟢 LIVE** — fastest denominator
(+12.5%/90d), lowest PEG (1.61), **at** target; catalyst 08-06. **CRWD 🟡 PARTIAL** — residual: fwd
**122.4x**, PEG **6.6**, the slowest estimate growth of the four, and its catalyst (09-02) is far outside
the window. **PANW 🟡 PARTIAL** — residual: out-year book 3↑:7↓ **and** a suspected vendor
period-definition artifact that must be resolved on a second source before it counts either way.

**Anti-signal for the whole node (from PREMORTEM, unchanged):** RS20 vs SPY crossing below 0, **or** the
OpenAI/Hugging Face thread falling to ≤2 outlets for 3 consecutive days. **Re-check 2026-08-21.**
⚠ **The honest gate here is the RS20 flip, not the multiple** — gating a verified momentum signal on a
valuation factor this repo has never measured lets an unmeasured axis veto a measured one.

---

## §E · CROSS-SECTOR LIVE SHORTLIST — names outside the DEEP sectors

`US_LIVE_SHORTLIST.json` returned 11 names. Six are already covered above (TRV, CB, STT, USB, PYPL in §B;
none in §A). The remaining five, with the **PREMORTEM's mandatory 🟢-downgrade applied** (on the US path
`has_conviction` can only be satisfied by OBV, so every US 🟢 is OBV-gated and is read as 🟡 with a stated
RS agreement or disagreement):

| Name | Sector | flow | RS20 / RS60 vs SPY | vol_surge | FINRA z | Verdict |
|---|---|---|---|---|---|---|
| **CTAS** | Industrials (services) | +0.922 | **+17.7 / +7.2** | 1.46 | +0.08 | **KEPT** — RS agrees on both horizons. Not a defense name; it is one of the 2 greens the sector's N− has to live with |
| **TRI** | Industrials (services) | +0.789 | +18.0 / **−5.0** | 1.22 | +0.09 | **MIXED** — 20-day strong, 60-day negative vs SPY. Carried, not promoted |
| **ABT** | Health Care | +0.900 | +13.0 / +2.2 | 1.42 | +0.96 | **KEPT** — RS agrees. Devices node, **no pharma-tariff import exposure**; the sector's ±40pp device dispersion (ISRG −32.5, BSX −39.9 RS60) is stated |
| **UNH** | Health Care | +0.756 | +6.8 / +17.4 | 1.25 | +0.14 | **KEPT with a flag** — ⚠ it is the **only 🟢 of the managed-care trio while carrying 1/5th of HUM's RS60 (+82.5)**. The C-grade tag is outranking the A-grade axis again |
| **EA** | Comm Services | +0.665 | +2.5 / **−2.4** | 1.41 | +1.08 | **DROPPED** — RS negative on the 60-day and barely positive on the 20-day; the tag is a volume-surge artifact |
| **T** | Comm Services | +0.636 | **+0.2 / −22.0** | **1.53** | +1.27 | **DROPPED, explicitly** — a 🟢 built on a one-day volume spike in a name that has underperformed SPY by **22% over 60 days**. This is the clearest single instance of defect **D11** on the board |

**Not on the shortlist but named by the pre-mortem and carried here so they are not lost:**
**HUM (RS60 +82.5 / RS20 +11.6, flow +0.661)** and **CVS (+34.6 / +8.7, +0.667)** — managed care has **no
import transmission** from the announced up-to-200% pharma tariff, and is the actual RS leadership of a
sector this run calls Neutral. Catalyst **`[blank]`**; valuation **not pulled this run — stated as a gap**.
**WELL (+16.0) and VTR (+17.0) RS20 vs SPY** — the Real Estate sector's top two, inside a sector the matrix
calls "the purest duration expression." Nominated for DEEP on **07-19 and never delivered; second run
of silence. First claim next run.**

---

## §F · EPICENTER-STARTER MODULE (cycle GAP flagged — coverage statement, not a signal)

`CYCLE_EXPOSURE.json` reports rank-2 **Energy / oil-refining (Hormuz + Russia crack)** at **0.00% epicenter
exposure against an 8.0% requirement (−8.00pp)** — and the pre-mortem established this is **4 for 4**:
0.00% on **07-17, 07-19, 07-21 and 07-22**. The book touches the cycle only through KMI and LNG
(RS20 −0.1 / RS60 −3.6 vs SPY at KMI) — beta to the consequence, none to the engine.

**Exhaustive in-universe epicenter set: VLO · MPC · PSX** — the only three `Oil & Gas Refining & Marketing`
rows in `us_top300`. There is no fourth. XOM/CVX are Integrated and dilute the crack into upstream beta.
**The transit expression (FRO, STNG, INSW, DHT) and the independent-refiner tier (PBF, DINO, CVI, DK,
PARR) are not reachable from this universe at all.**

**Rules that govern this module and are restated because four runs have not moved the number:**
a 🔴/crowded tape **gates ADD timing; it never justifies 0% core** in a rank-2 multi-year cycle — but a
**GAP is a coverage statement about the book, not a buy signal**, and this run's own oil variable
**reversed twice in two sessions** (S8 is explicitly two-sided, and branch B says crude down with cracks
holding is *not* against the thesis). **Both of those are true at once, and this sheet states both rather
than resolving them into an action.** Rank-1 AI-compute is nominally compliant at **12.25% vs 12.0%** —
⚠ that is **0.25pp of margin, it fired a GAP on 07-21 at 12.00%, and the bucket scores MU (RS60 +95.9) and
AVGO (RS60 −13.6) as the same thing**, ~109pp of dispersion inside one "epicenter" list.

---

## §G · Arithmetic and data-quality register

- **Derived figures recomputed here** (all consistent): VLO FY26→FY27 33.46 → 22.88 = **−31.62%**;
  MPC 36.26 → 26.91 = **−25.79%**; crack gap 88.41 − 58.14 = **$30.27**; primes-vs-capgoods flow spread
  0.250 − (−0.455) = **0.705**; Financials RS20 spread 31.4 − (−13.0) = **44.4pp** ÷ median 6.1 = **7.28×**;
  Energy RS60 spread 39.0 − (−20.5) = **59.5pp**; DDOG 0y 2.15218 → 2.42213 = **+12.54%**;
  FTNT price/target 158.10 ÷ 119.92 = **+31.84%**; PANW 0y→+1y 3.77344 → 1.95095 = **−48.3%** (flagged suspect).
- **Blanks left as blanks:** KeyCorp provision magnitude · LHX fundamentals · HUM/CVS valuation ·
  AXON backlog (**not disclosed — no backlog line exists in the 10-K**) · pharma-tariff effective date ·
  BOJ meeting date · V/MA fiscal-Q3 date.
- **Stale/suspect data flagged, not used:** NOC vendor consensus (pre-dates its own 07-21 guidance raise)
  · PANW +1y period definition · `BZ=F`/`RB=F` 07-22 prints (contract-roll artifact, excluded from the
  crack series) · the cycle registry (`data/cycles/cycle_registry.json`, `updated: 2026-07-17`, 5 days
  stale; `scripts/cycle_exposure.py`'s docstring still cites a non-existent `data_build/` path).
- **Sizing language:** none anywhere in this file, by design (P4).

## ✅ EXIT CHECK
- [x] Every DEEP sector has a section (§A Energy, §B Financials, §C Industrials) plus the
      PREMORTEM-mandated §D and the cycle-GAP §F.
- [x] Cross-sector LIVE_SHORTLIST names all accounted for — 6 covered in §B, 4 kept/mixed and **2
      explicitly dropped with the reason** (§E).
- [x] Numbers cross-checked and recomputed (§G); blanks are blanks; stale and suspect data flagged.
- [x] Flow/positioning cross-read present for every candidate; every 🟢 downgraded per the OBV-gate rule.
- [x] Written as ONE file under the load-bearing filename.
- [x] Linter run on this file.
