# DEEP · ENRG — 2026-07-22 (Wed) ★US-only · **CONTINUOUS TRACK · REFINING NODE ONLY**

> Stage 7 / L1·DEEP. `--market us`, news `--scope foreign`. Zero buy/sell, zero sizing (P4).
> Run clock **06:5x ET — the US regular session has not opened**; equity tape is asof **2026-07-21 close**.
> **Prior deeps carried by reference, not re-printed:** `llm_outputs/2026-07-21/industry_US/SECTOR_DEEP_ENRG.md`
> (value-chain map §4, Bab el-Mandeb node, services node, tanker-hop kill, the PSX/MPC/VLO 10-K placements)
> and `llm_outputs/2026-07-21/US_2/SECTOR_DEEP_10.md` (§4 chain map, §2 player list).
> Crack series below is **self-computed** (`yfinance CL=F/RB=F/HO=F`, one continuous pull) so it is
> internally consistent; it does **not** reconcile to the prior file's levels (see the vintage note in §1).

---

## §0 · DELTA since 2026-07-21 — the lead

Four things changed. **(1)** The margin is now measurable against its own history and it is extreme:
the self-computed 3-2-1 crack closed **$68.23/bbl on 07-21 = the 99.5th percentile of 3 years**
(98.4th of 1y; 3y range $14.4–$69.5). **(2)** The prior file's own falsifier — *"2 consecutive sessions
where the crack falls and refiners still rise"* — is now at **three consecutive sessions** (07-17, 07-20,
07-21), and this time crude *rose* on all three. **(3)** The 07-21 flow file's concentration statistic,
which PREMORTEM B5 read as proof of a war-premium echo, **is matched almost exactly by the crack's own
concentration** — a correction to B5, derived below. **(4)** PSX's FINRA short-volume z, flagged at
**+2.01 "extreme"** in the prior file, has fully normalized to **+0.01**; the spike is now in **MPC
(z +1.69 🔴, base20 56.3% → 66.1%, 5v5 +6.1▲)**. Everything else in the chain map is carried unchanged.

---

## §1 · The refining question (a) — is the lead margin or war-premium echo?

**It is a margin story whose cause is the war, and B5's inference from RS-concentration does not survive.**

B5 and `handoff/SCENARIOS.md` S8 both anchor on: VLO rs20 **+28.6** vs rs60 **+29.0**, PSX +25.5 vs +27.4,
MPC +28.8 vs +39.0 (**all vs SPY**) — ~100% (VLO) / ~93% (PSX) of the 60-day excess earned in the last
20 days, and infer *"a war-premium position wearing a crack-spread label."* Measured against the crack
itself over the identical windows:

| Window | 3-2-1 crack $/bbl | change |
|---|---|---|
| 60 sessions ago (2026-04-23) | 56.92 | — |
| 20 sessions ago (2026-06-22) | 52.12 | **−8.4%** |
| 2026-07-21 | **68.23** | **+30.9%** |

**The crack also earned more than 100% of its 60-day gain in the last 20 days.** The equity's
concentration is not excess concentration — it tracks its own KPI's concentration. B5's premise is
correct and its inference is not: RS-concentration alone cannot separate margin from premium here.

**The second derivative (binding rule), weekly means of the 3-2-1 crack:**

| Wk ending | 06-07 | 06-14 | 06-21 | 06-28 | 07-05 | 07-12 | 07-19 | 07-26* |
|---|---|---|---|---|---|---|---|---|
| level | 45.04 | 47.03 | 49.23 | 55.65 | 59.86 | 61.94 | 67.65 | 68.78 |
| **Δ rate** | — | +1.99 | +2.20 | **+6.42** | **+4.21** | **+2.08** | +5.71 | +1.13 |

**Two consecutive declines in the rate fired 06-28 → 07-12** (+6.42 → +4.21 → +2.08) — the signal the
rule names. It was then **overwritten by the 07-10 truce collapse** (+5.71), and the current week is
+1.13 on one clean session. \*07-26 excludes 07-22: `BZ=F` printed **84.46 below `CL=F` 87.13** and
`RB=F` fell −4.4% on 7,232 lots — a **contract-roll artifact**, not a margin event. It is excluded
rather than used, and said so rather than hidden.

**Where the echo actually shows.** Over the last three clean sessions the crack fell every day while
crude rose every day and all three refiners rose every day:

| Date | CL=F | crack 3-2-1 | VLO | MPC | PSX |
|---|---|---|---|---|---|
| 07-16 | 78.95 | 69.45 | +2.60% | +2.23% | +2.63% |
| 07-17 | 82.49 | **69.41** | +3.13% | +2.21% | +2.75% |
| 07-20 | 83.23 | **69.33** | +1.18% | +0.87% | +0.94% |
| 07-21 | 84.91 | **68.23** | +0.48% | +1.41% | +1.66% |

Crude **+7.5%**, crack **−1.8%**, equities up on all three. **That last leg is the echo** — and VLO's own
daily increment decayed +3.13 → +1.18 → +0.48 through it. Three sessions is a three-observation sample;
on its own it is **indistinguishable** from noise, which is why it is registered as a running counter in
§6 rather than a conclusion.

---

## §2 · Margin percentile NEXT TO the multiple, and the revision stream

Margin percentile is common to all three: **3-2-1 crack at the 99.5th percentile of 3 years** (asof 07-21).

| Name | px | P/E on FY26 cons. | P/E on FY27 cons. | cons. FY26→FY27 EPS | 30d revisions (FY26) | FINRA short-vol z |
|---|---|---|---|---|---|---|
| **VLO** | 314.80 | **9.4x** | 13.8x | 33.46 → 22.88 = **−31.6%** | 9 up / 3 down | −0.77 🟡 |
| **MPC** | 319.76 | **8.8x** | 11.9x | 36.26 → 26.91 = **−25.8%** | 4 up / 2 down | **+1.69 🔴** |
| **PSX** | 212.27 | **10.8x** | 11.6x | 19.74 → 18.32 = −7.2% | 7 up / 1 down | +0.01 🟡 |
| **XOM** | 151.71 | 13.6x | 14.2x | 11.18 → 10.66 = −4.7% | **1 up / 3 down** | +0.74 🟡 |

**The peak-margin trap is explicit in consensus itself.** Nobody has to assert normalization: the
sell side already models FY27 EPS **−31.6% (VLO)** and **−25.8% (MPC)** below FY26. The 8.8–9.4x
"cheap" multiple is a peak-denominator multiple attached to a margin in its 99.5th 3-year percentile.

**Revision second derivative** (increment between estimate snapshots, current-quarter, $/sh):
VLO **+2.42 → +0.49 → −0.02 → +0.12** — two consecutive declines in the rate, then flat.
XOM **+0.30 → +0.16 → −0.02 → −0.04** — two consecutive negatives; **XOM's estimates are being cut**
while the refiners' are raised. But the *next* quarter inverts it: VLO +1q **+1.69 → +0.51 → +1.11 →
+1.80** and MPC +1q **+1.70 → +0.83 → +1.67 → +2.76** — accelerating hardest in the last 7 days.
**Read with the multiple as the rule requires: a single-digit multiple whose out-quarter estimates are
being marked up at an accelerating rate on a 99.5th-percentile margin is consensus chasing the print,
not cheapness.** MPC is the extreme of that on every axis and is simultaneously the only short-volume
spike in the four (C-grade — corroborant only, carries nothing).

---

## §3 · Customers & the demand side (W4)

The node's customers are the **fuel buyers**: airlines (jet/distillate), truck and parcel (diesel), and
wholesale rack distributors. Disclosed-spend status, with dates:

- **Already printed inside the war window, and not read by this run's deterministic tools:**
  **DAL 2026-07-10**, **UAL 2026-07-16**, **FDX 2026-06-24**. Their fuel-cost lines exist and this file
  did not pull them — named as a gap rather than filled with a guess.
- **Pending, dated:** **LUV 2026-07-23 (tomorrow)** · **UPS 2026-07-28**.
- **What the tape says in the meantime (vs SPY):** DAL rs20 **−2.0** / rs60 **+18.2**; UAL **−1.3** /
  **+23.4**; UPS **+8.0** / **+2.4**; FDX **−4.7** / **−6.0**. The two jet-fuel buyers have rolled over
  on the 20-day axis while holding large 60-day gains — the same shape, inverted, as the refiners.
  **Consistent with the customer paying**, not proof of it; the confirmation is the 07-23 and 07-28 prints.

---

## §4 · Value chain — only what changed. The binding constraint is named.

Nodes carried unchanged by reference (crude logistics/Hormuz + Bab el-Mandeb, services, midstream,
integrated): see the two prior files cited in the header. **Two nodes changed:**

**(i) The binding constraint is middle-distillate conversion capacity in the Atlantic basin — not crude,
and not demand.** A bottleneck is a *binding constraint*; strong demand is not one. Measured: on 07-21
the **distillate crack was $88.41/bbl against a gasoline crack of $58.14 — a $30.27 gap**. Body-proximate
corroboration `[news, foreign]`: *"Europe Faces Diesel Crunch as Inventories Head Toward Multi-Year Lows"*
(07-20), *"Russia's diesel export ban adds fresh fuel to rising prices"* (07-17), Fujairah middle
distillates **−15% vs last month** (07-17). **Counter-evidence in the same feed, and it matters:**
US distillate inventories **rose +2.3mb then +1.759mb in consecutive weeks** (07-21), and US crude
inventories built. **The constraint binds in Europe, not in the US** — so the US Gulf Coast refiners'
exposure runs through the *export arb*, which is a different and more fragile object than a domestic shortage.

**(ii) A permanent US capacity reduction inside the cycle window.** VLO's 10-K (filed 2026-02-25) discloses
**Benicia, California — 170,000 BPD — to be idled and refining ceased by end of April 2026**, against a
15-refinery, 3.19M BPD system; plus a St. Charles FCC optimization project starting H2 2026. This is the
one leg of the margin story that **survives a truce**, and it is PADD-5, i.e. a different market than the
Gulf Coast export node above. Both are structural; neither is a war variable.

---

## §5 · Chain-hop candidates — **ZERO promoted, fifth consecutive run**

`chain-hop refinery diesel crack --days 14 --scope foreign`, 633 articles scanned. Title-0 body-proximate
candidates, each flow-cross-checked before it may reach BET (a co-mention alone is not a candidate):

| Candidate | Proximity / body | Flow · rs20 / rs60 vs SPY · OBV | Verdict |
|---|---|---|---|
| **MS** | 6 / 17 (*Europe Faces Diesel Crunch*) | −0.333 🔴분산 · −5.2 / +9.1 · 분산 | **FAIL** — flow contradicts |
| **CME** | 2 / 7 (*benchmark diesel price 2nd-largest jump*) | −0.452 🔴분산 · −3.7 / **−22.5** · 분산 | **FAIL** |
| **KKR** | 3 / 4 | +0.021 · −0.3 / −10.1 · 중립 | **FAIL** |
| **AMP** | 3 / 3 (*Bonds unsettled as oil and gas climb*) | +0.247 · +11.6 / +9.3 · 중립 | **FAIL on mechanism** — a macro co-mention, no chain position |
| **META** | 4 / 160 (*"…Finally Crack the Stock Market"*) | — | **FAIL** — lexical false positive |

The tool also returned **VLO itself** as title-0 (via *"Five Oil and Gas Stocks Ready for a Hormuz Spike"*);
that is the named node, not a hop.

---

## §6 · Track KPIs + anti-signals — stated as dated observables

1. **3-2-1 crack** (self-computed). 68.23 asof 07-21, 99.5%ile/3y. **Anti-signal:** two consecutive
   *weekly means* below 60.00 → the margin turned, independent of the war. Observable daily.
2. **Distillate−gasoline crack gap.** $30.27 asof 07-21. **Anti-signal:** gap < $15 → the binding
   constraint in §4(i) has released. Daily.
3. **EIA weekly distillate inventories.** +2.3mb then **+1.759mb** (latest 07-21). **Anti-signal:** a
   third and fourth consecutive build with the crack still >95%ile → the US leg is supplied and the
   whole margin is a European arb. Next prints **2026-07-22 (today)** and **2026-07-29**.
4. **Detachment counter** (the prior file's own falsifier, carried). **Now 3** (07-17, 07-20, 07-21).
   Next reading **2026-07-22 close**. At 5 consecutive the equity is priced off something other than its KPI.
5. **WTI COT %ile** — 10%ile, **next print 2026-07-24** (S8's frozen cross-check).
6. **Estimate second derivative.** Re-pull `module_fundamentals_us --json` weekly. **Anti-signal:** the
   **+1q** increment negative on two consecutive pulls (currently VLO +1.80, MPC +2.76 — accelerating up).
7. **Prints:** **VLO 07-30** · **XOM 07-31** · **MPC 08-04** · **PSX 08-05**. Observable inside them:
   realized refining margin $/bbl by region and the Q3 guide, read against a 99.5th-percentile crack.
8. **XOM as the control.** Estimates 1 up / 3 down over 30d, rs60 −4.8 vs SPY. If XOM's revisions turn
   up while the crack falls, the move was crude, not margin — and the refining thesis loses its engine.

---

## §7 · Answers to (b) and (c), and the dispersion statement

**(b) Is Energy's breadth 0.00 / 0-green-of-16 fully explained by the `vol_surge<1.2` artifact?
Partly — and "fully" is the wrong word.** Verified independently on all 16 Energy rows: exactly **four**
names carry OBV 매집 **and** rs20>0 — **XOM, VLO, MPC, PSX** — and all four are blocked solely by
`vol_surge` (0.84 / 1.04 / 0.85 / 0.91, all <1.2). SWEEP_READ §3's measurement reproduces. **But the
artifact explains the ZERO, not the narrowness it conceals: only 4 of 16 pass the pre-gate at all** —
the other 12 fail on OBV (SLB, BKR, OKE, DVN distributing) or on rs20 (WMB −2.6, KMI −0.1). With just
**1 red of 16**, this is not a sector being sold; it is a sector where **11 names are doing nothing** and
four are carrying it. And one of those four (XOM) is having its estimates cut. **The honest statement:
breadth 0.00 is a filter artifact; participation of 3/16 is real.**

**(c) The 🚨 0.0% vs 8.0% epicenter GAP, now flagged for a fourth consecutive run (07-17, 07-19, 07-21,
07-22).** The cleanest in-universe epicenter expressions are, exhaustively, **VLO · MPC · PSX** — those
are the only three `Oil & Gas Refining & Marketing` rows in `us_top300`; XOM/CVX are Integrated (the
crack is diluted into upstream beta, and XOM's rs60 is **−4.8 vs SPY** against MPC's +39.0). There is no
fourth. **The coverage hole is wider than the mandate states**: verified absent from `us_top300` are not
only the tanker/Hormuz-transit leg (**FRO, STNG, INSW, DHT**) but also the **entire independent-refiner
tier (PBF, DINO, CVI, DK, PARR)** — which is where the prior file measured the sharpest moves — plus
MPLX/ET/LNG. So the registry's epicenter is reachable from this universe only through three large caps,
and the transit leg is not reachable at all. ⚠ Per SWEEP and P4, **a 🚨 GAP is a coverage statement about
the book, not a signal**; it is recorded, not acted on, and BET owns whatever follows.

**Dispersion (W5).** Energy's **median rs60 is −3.5 vs SPY**. The intra-sector spread is **59.5pp**
(MPC **+39.0** to SLB **−20.5**), with BKR −18.2, DVN −14.0, COP −11.1 on the other side.
**The spread is roughly seventeen times the sector's own median displacement.** "Energy" is therefore an
unusable unit of analysis this run — the object is the three-name refining node, and every number above
is stated about that node, not about the sector.
