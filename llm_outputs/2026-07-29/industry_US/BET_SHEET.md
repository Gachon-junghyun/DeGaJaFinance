# BET_SHEET — industry_US — 2026-07-29 (Wed)

> ONE file, per-sector sections (downstream desks glob this exact filename — never split it).
> DEEP sectors: **ENRG · FIN · INDU · UTIL** (UTIL promoted by PREMORTEM Lens 1).
> All flow/RS **settled 2026-07-28**; benchmark **SPY** inline (C1). Freshness tags in §B are
> **placeholders for ALPHA**. **Sizing language is influence illustration only — zero buy/sell
> recommendation (P4).**

## ⚠ 0 · Three instrument caveats binding on every number below

1. **The 🟢 tag is a volume test today.** `velocity` is **null on 300/300** names, so the gate collapsed
   to 3-axis unanimity, and **95 of 95 names passing `OBV-매집 ∧ RS20>0` are blocked by `vol_surge`
   alone** (SWEEP §4, the mechanism's 7th replication across two markets). ⇒ **a 🟡 in this sheet is
   not a flow verdict**, and every 🟢 here cleared on **volume**, not on news.
2. ★★★ **Lens L2 is unrunnable on the MAJORITY of this sheet, and that is a finding.**
   `scripts/margin_history.py` was attempted on **18 names this run** and produced a usable
   current-year percentile on **7 (39%)**:
   - **usable** — MPC · PSX · WAB · ITW · MMM · PCAR · LMT
   - **`연간 데이터 없음`** — **VLO (D56, 5th run) · XOM (NEW) · CSX · UNP · NSC · PLD**
   - **series truncated before FY2025** — **RTX (ends FY2017) · TMO (FY2017) · T (FY2014, confirming
     D91) · GM (FY2021)**
   - **artifact** — **CAT returns 99.9% for FY2024/25 against a 30.3% median** (XBRL tag pairing)
   ⇒ **No cheapness claim is made on any of the eleven unmeasurable names.** Blanks are blanks (C3).
3. **The desk has no investor-type feed in the US.** Every "who is buying" read here is the **FINRA
   short-vol proxy** (`us_flow`, 2026-07-28) plus COT **positioning context, never a trigger** (D6).

---

# §ENRG — Energy (continuous DEEP)

## §A · Numbers

| Ticker | Fwd P/E | Trail P/E | P/B | To mean target | FY25 gross margin | Own-series percentile | Next-yr est. Δ90d |
|---|---|---|---|---|---|---|---|
| **MPC** | **11.27** | 20.62 | 5.47 | **−2.9%** | **10.0%** | ★ **≈37.5th — BELOW its own median (10.5)** | **+35.1%** |
| **PSX** | **11.06** | 20.72 | 2.95 | **−2.1%** | **12.3%** | ≈55th (median 12.1) | **+25.1%** |
| **VLO** | 12.24 | 22.45 | 3.82 | **−5.8%** | ⚠ `blank` | ⚠ **STRUCTURAL BLANK — D56, 5th run** | **+35.8%** |
| **XOM** | 14.85 | 26.75 | 2.56 | **+6.3%** | ⚠ `blank` | ⚠ ★ **NEW BLANK, same class as VLO's** | +4.1% |

⚠ **Arithmetic cross-check (`module_math_check` class, done inline)**: MPC trailing EPS **$15.18** →
forward **$27.77** = **+82.9%**; PSX $10.13 → $18.98 = **+87.4%**; VLO $13.69 → $25.12 = **+83.4%**.
**The consensus denominator has already almost doubled at all three.**

## §B · Thesis + freshness `[ALPHA fills the tag]`

**"Refining margin, not crude beta"**, and this run's evidence is the strongest yet on one axis and
the most ambiguous yet on another.
- **For**: settled 3-2-1 crack **68.117 → 72.219 (window high)** with WTI **82.61 → 79.26 (window
  low)**; distillate crack **95.078**, also a window high; **P4's one-axis kill is 12.22 points away**,
  from 4.30 five sessions ago. **S8 branch B in its cleanest form.**
- **Against**: **the margin percentile says mid-cycle while the revision book says top-of-cycle** —
  MPC is **below** its own 8-year median gross margin while its next-year consensus is **+35.1%/90d**.
  Under L2 that is **consensus chasing, not cheapness**, and all three refiners trade **at or below**
  their mean targets. ⚠ **PSX's days-21-60 excess flipped NEGATIVE (−5.91)** while MPC's stayed
  **+2.30** — **the human-locked `core_pick` is the degrading leg** (M177 degrading, 2nd run).
- ⚠ **Live tape at the run clock disagrees with the settled bar**: unsettled 07-29 shows WTI **+6.6%**
  and the 3-2-1 back to **64.1**. **Inadmissible** (R17/D83); recorded, not used.

Freshness: `[ALPHA]`

## §C · Flow / positioning cross-read

| Ticker | Tag | flow | RS20 / RS60 | `vol_surge` | FINRA z · 5v5 (07-28) | Implied move |
|---|---|---|---|---|---|---|
| MPC | 🟡 | +0.64 (OBV 매집) | **+18.1 / +20.2** | 0.96 | — | 08-04 print |
| PSX | 🟡 | +0.64 (OBV 매집) | **+18.3 / +11.8** | 0.95 | — | 08-05 print |
| VLO | 🟡 | +0.30 | +12.2 / +15.2 | 0.80 | **+0.10 · +6.0▲** | **±4.8% (D2)** — 07-30 |
| XOM | 🟡 | +0.58 (OBV 매집) | +12.5 / **−3.9** | 0.85 | **−0.48 · +8.2▲ = the board's largest build** | **±4.1% (D2)** — 07-31 |

★ **All four are 🟡 for one reason only: `vol_surge`.** 8 of Energy's 16 names pass the accumulation
pre-condition and **8 of 8 are blocked on volume** ⇒ **the sector's zero-green count is an instrument
artifact, not evidence** (ROTATION §2, DEEP-ENRG §2).

## §D · Competition / peers

Refiners **{VLO, MPC, PSX} are ONE risk unit** (SPY-residual ρ **+0.878**, M147) — three tickers, one
bet. **XOM is the declared control**: same-day crack correlation **+0.078 ≈ 0**, **0% refining
exposure**, and its RS60 is **−3.9** against the refiners' +11.8 to +20.2. **Days-21-60 excess splits
the sector 25.3pp wide** (MPC +2.30 → BKR −23.00), which is why the sector label is the wrong unit (W5).

## §E · Refutation + dated catalyst

**Kills it (one axis)**: **a settled 3-2-1 crack below 60** (12.22 away) **or a settled distillate
crack below 80** (15.08 away). **Second refutation, already live**: the KR refiners underperformed
**their own betas** by a median **3.57pp** on the first session that knew the crack held (S33, branch B
on the adjusted axis) ⇒ **one vote for the war-premium reading. C4 stays `indistinguishable`.**
**Dates**: VLO **07-30** · Russian diesel-ban expiry **07-31** · XOM **07-31** (S31's window, declared
contaminated at registration) · MPC **08-04** · PSX **08-05**.

---

# §FIN — Financials (continuous DEEP)

## §A · Numbers

| Ticker | Fwd P/E | Trail P/E | P/B | To mean target | Margin percentile | Next-yr est. Δ90d |
|---|---|---|---|---|---|---|
| **BX** | **17.39** | 29.08 | **11.53** | **+9.2%** | ⚠ n/a — an alt-manager has no comparable GM series (C3) | ⚠ **−1.1%** |
| **CB** | 12.46 | 12.87 | 1.86 | **+0.6%** | ⚠ n/a (insurer) | **−0.3%** |
| TRV | — | — | — | — | ⚠ n/a (insurer) | carried: fwd 12.88× on CY 34.01 → 30.04 (**−11.7%**) |

## §B · Thesis + freshness `[ALPHA fills]`

**★ BX — the coverage gap closed at the flow/valuation level and NOT at the thesis level.**
HANDOVER ranked it **first-claim #1** for a second run. Measured today: **🟢가속 +0.783, `new_green`,
`vol_surge` 1.21 (a VOLUME path), RS20 +16.6 / RS60 +3.5, FINRA z −0.71 on an in-band baseline.**
★★ **And its ignition has no earnings event under it** — `module_disclosure_us`: 19 filings in 90
days, **2 8-Ks, neither an Item 2.02, and zero 수주/계약/M&A** ⇒ **the D51/C-B pattern that explains
four of this run's other greens does not apply to BX. The test discriminates.**
⚠⚠ **No 4Phase exists, so under the carried rule NO THESIS MAY BE BUILT on it**, and the fundamental
axis cuts the other way: **a flat-to-declining revision book (CY +0.9%, next-yr −1.1%/90d) at 17.4×
forward and 11.5× book.** **Handed forward as a NAMED coverage item with a stated prohibition.**

**CB / TRV — the OW's hidden internal hedge.** CB is **the sector's only volume-path green**
(`vol_surge` 1.42, RS20 +5.9 / RS60 +8.1, β 0.125); TRV is 🟡 +0.75 (`vol_surge` 1.15, RS20 +19.7 /
RS60 +27.1, β 0.339). **Both sit on S26/S41's rips-on-B list** — the only tilt on this board carrying
an internal hedge its label hides. ⚠ **M150: 98.6% of TRV's 60-day excess landed in its last 20
sessions** (the R9/AXON geometry); PREMORTEM Lens 3 re-tagged it **EXTENDED-BUT-LIVE**, not exhausted.

Freshness: `[ALPHA]`

## §C · Flow / positioning cross-read

Sector: **eqflow +0.374 > wflow +0.294** — and **ex-BRK-B the gap halves, +0.080 → +0.043** ⇒
**46% of "the board's only breadth-led sector" is one inert holding company** (M173 replicates at a
smaller magnitude). Sub-nodes: **payments+insurance +0.540 eqflow (1.6× the sector)** · **banks 0
greens in 9 names, wflow > eqflow** · **capital markets +0.200 with GS RS20 +1.3 on flow −0.357.**
**Only 2 of 47 names are 🟢.**

## §D · Competition / peers

**MA/V is a DIFFERENT SPY-residual unit from JPM/TRV/CB** (MA–JPM +0.238, TRV–MA +0.382) ⇒ an MA miss
does not read across. **Exchanges' replacement observable** (EW excess of the 7 vs SPY, 07-24→08-07)
reads **+3.21pp**, from +3.17 — **one settled session moved it 0.04pp.** **ICE/NDAQ/CME/COIN are pure
last-20 events; SPGI and MCO are the only two positive on both windows** (M137's ratings split).

## §E · Refutation + dated catalyst

**Kills it**: **S23-B — T10Y2Y ≤ +0.20 by 2026-08-05 with DGS2 inside 4.15–4.45%.** Now **+0.34 with
DGS2 4.31% ⇒ 0.14pp away, and it moved TOWARD the trigger this print.** Second refutation: **S14's
{MA, V, PYPL} RS20 flipping negative by 08-06.** Third, registered this run: **S41 — IG OAS ≥0.90% by
08-12.** **Dates**: FOMC **07-29 14:00 ET** · **V 07-29** (⚠ **option P/C OI 5.90, the heaviest put
positioning on the board, bracketed nowhere**) · **MA 07-30** (implied **±3.5%** vs S14-num's frozen
**±3.9%** — **any move inside ±3.9% is pre-declared no-information**) · PCE **07-30**.

---

# §INDU — Industrials (rotating DEEP, recency-starved)

## §A · Numbers — ★ the four greens are TWO OPPOSITE MARGIN ENGINES

| Ticker | Fwd P/E | Trail P/E | To mean target | FY25 gross margin | Own-series percentile | CY est. Δ90d · breadth |
|---|---|---|---|---|---|---|
| **WAB** | **24.25** | 40.37 | +8.1% | **34.1%** | ★ **100th — the MAX of an 18-year series** | +2.8% · — |
| **ITW** | **24.10** | 27.48 | **−5.4%** | **44.1%** | **≈93rd** (max 44.3 FY24) | +1.6% · ⚠ **0↑:1↓ (30d)** |
| **MMM** | **18.76** | 31.52 | **−0.0%** | **39.9%** | ★ **≈12th — near its own TROUGH** (median 47.6) | +2.8% · **4↑:0↓ (30d)** |
| **PCAR** | **19.72** | 28.35 | **−6.8%** | **20.1%** | ★ **≈12th — near its own trough** | +3.2% · — |
| **RTX** | 27.71 | 38.07 | +6.3% | ⚠ series ends FY2017 | ⚠ **unobtainable** | **+3.4%** |
| **LMT** | **17.62** | 21.23 | +9.0% | **10.2%** | **≈30th — below its own median (11.1)** | +1.6% |
| **UNP** | 20.70 | 24.03 | **+12.3%** | ⚠ `blank` | ⚠ **unobtainable** | +3.3% |
| **CSX** | 22.31 | 29.38 | +4.6% | ⚠ `blank` | ⚠ **unobtainable** | **+5.4%** |
| **NSC** | 23.67 | 28.80 | +7.7% | ⚠ `blank` | ⚠ **unobtainable** | **+5.9%** |

★★ **Two of the four capital-goods greens are at or near their own margin MAXIMUM at ~24× forward and
two are near their own TROUGH at ~19×. Never average them (M140's rule).**
★ **LMT is the one defense prime whose L2 can be run, and it comes out BELOW its own median margin at
17.6× forward** — the opposite of the trap.

## §B · Thesis + freshness `[ALPHA fills]`

⚠⚠ **This section states a finding AGAINST this run's own ROTATION verdict.**
ROTATION promoted INDU **OW− → OW** on **breadth 0.180** carried by nine greens including four capital
goods. **DEEP re-derived M174 from all 50 rows: primes +0.694 mean / +0.761 wflow (2🟢/0🔴) · rails
+0.270 / +0.379 (3🟢/1🔴) · capital goods+ −0.023 mean but −0.122 CAP-WEIGHTED, with 4🟢 and 12🔴 in
39 names.** ⇒ **the split COMPRESSED (0.860 → 0.717), it did not invert; the four greens are 10.3% of
a node whose money is still leaving on a cap-weighted basis.**
★★★ **And D51 fires in its purest instance yet**: `module_disclosure_us` Item 2.02 8-K dates —
**PCAR 2026-07-28 and ITW 2026-07-28 = the SAME session as the flow snapshot**, **WAB 07-22**,
**MMM 07-21.** **All four within five sessions; two at zero. The flow IS the event.**
⇒ **The OW is carried by primes and rails — the legs the desk already held — not by a capital-goods
turn.** **S42 (registered this run) brackets it, and this evidence makes its branch A more likely.**

Freshness: `[ALPHA]`

## §C · Flow / positioning cross-read

WAB **+1.00, `vol_surge` 1.84 = the board's highest** · UNP +0.92 (**FINRA z −3.13 ✅ clean rise**) ·
PCAR +0.89 (z −0.56 ✅) · RTX +0.88 (z −1.03 ✅, `vol_surge` 1.38) · LMT +0.75 (**z −1.86 ✅**) ·
MMM +0.78 · ITW +0.78 · NSC +0.76 (z +0.42 △) · CSX +0.74 (z +0.45 △).
**6 of the 15 shortlist names read ✅ clean-rise**; **none reads crowded-short.**

## §D · Competition / peers — the chain's bottleneck is NOT the OEMs

**① steel (NUE 🟡 +0.68, STLD +0.66 — both blocked on volume)** → **② electricals (VRT 🔴 −0.81,
ETN 🟡 −0.30, EMR 🟡 +0.66)** → **③ machinery OEM (WAB/PCAR/ITW 🟢; CAT 🔴 −0.76)** → **④ EPC /
interconnection (PWR 🔴 −0.80 · EME 🔴 −0.73 · FER 🔴 −0.68)** → **⑤ rails 🟢** → **⑥ primes 🟢🟡**.
★ **Node ④ is 3 of 3 🔴 with RS60 between −13.5 and −23.9** — **the layer that physically installs the
AI-power and grid capacity everyone forecasts is the layer money is leaving hardest.** That is the
binding constraint, and **no tilt on this board expresses it.**
★ **Two uncovered names sit at the top of the sector's RS book and are blocked from 🟢 by `vol_surge`
alone**: **CTAS (RS20 +27.1 / RS60 +19.9)** and **TRI (+25.0 / +4.9)**. Named in a table row so the
handoff ledger indexes them (**D60/M183** — a bare ticker in a prose list does not register).

## §E · Refutation + dated catalyst

**Kills the promote**: **S42 — median RS20 vs SPY of {WAB, PCAR, MMM, ITW} ≤ 0 by 2026-08-12**
(now **+13.2**), with **CAT (RS20 −18.6) as the in-bracket control**. **Kills the rail leg**:
**S20-ANNEX — median RS20 of {CSX, UNP, NSC} ≤ 0 by 2026-08-04** (now **+7.03**, from +8.38 and +11.7).
⚠ **M91 unretracted: ~8 of UNP's 12 revenue growth points are FUEL SURCHARGE** ⇒ the rail leg is the
Energy bet through a different income statement. **Dates**: **GD prints TODAY with no bracket** (dropped
07-28: neither branch changes a conclusion) · S20-ANNEX **08-04** · S42 **08-12**.

---

# §UTIL — Utilities (PREMORTEM-promoted DEEP)

## §A · Numbers

| Ticker | Fwd P/E | P/B | To mean target | Revision breadth (30d) | Margin percentile | Prints |
|---|---|---|---|---|---|---|
| **PCG** | **9.92** | **1.22** | ★ **+28.0%** | 4↑:2↓ (**2↑:0↓ 7d**) | ⚠ n/a — regulated utility, no comparable GM series (C3) | **2026-10-22** |
| **D** | 18.75 | 2.23 | −0.8% | 1↑:1↓ | ⚠ n/a | **07-31** |
| **EXC** | 15.65 | 1.66 | +4.2% | ⚠ **4↑:6↓ — the only net-negative book of the seven** | ⚠ n/a | **07-30** |

## §B · Thesis + freshness `[ALPHA fills]`

**The W5 hypothesis is CONFIRMED and it does not rescue the sector.**
**Regulated seven median RS20 −1.99 vs AI-power four median −10.31 = an 8.3pp gap inside one 15-name
sector** — so S35's branch A has a real mechanism. **But both legs are negative, wflow ≈ eqflow (no
mega-cap artifact), and only 2 of 15 names reach the accumulation pre-condition** — against Energy's
8/16 and Financials' 32/47. ⇒ **unlike Energy and Materials, the Utilities absence is EVIDENCE.**
**N− stands.** ⚠ **S24's own basket straddles two GICS sectors** (GEV and VRT are Industrials), which
is itself a label defect.
**Two names are carried for the ledger, not as candidates**: **`D`** (the only one of the seven whose
A-grade axis is positive on both windows, RS20 +2.1 / RS60 +6.4, accumulating on the sector's **lowest**
`vol_surge` 0.48, flat book, prints 07-31) and **`PCG`** (the only 🟢 and a `new_green`, **9.92×
forward at 1.22× book with +28.0% to target** — ⚠ **but it does not report until October, so it cannot
be what the sector is trading this week, and its percentile is unobtainable so no cheapness claim is
made**). **Neither carries a 4Phase ⇒ no thesis may be built on either.**

Freshness: `[ALPHA]`

## §C · Flow / positioning cross-read

Sector **wflow −0.265 ≈ eqflow −0.270 · 1🟢 / 6🔴 · breadth 0.070.** Regulated: WEC 🔴 −0.57 ·
ETR 🔴 −0.60 · EXC 🟡 −0.18 · SO 🟡 −0.32 · XEL 🟡 −0.58 · **AEP 🔴 −0.69** · D 🟡 −0.03.
AI-power: **VST 🔴 −0.61 · CEG 🟡 −0.08 (RS60 −20.1) · GEV 🔴 −0.54 · VRT 🔴 −0.81.**

## §D · Competition / peers

**The bottleneck is grid equipment and interconnection (nodes ③–④), not generation** — all four of
GEV/VRT/PWR/EME are 🔴 with RS60 between −13.5 and −23.9 while the regulated generators sit near flat.
**Two dated facts landed on this chain in 48h and point opposite ways**: the **FCC added foreign-made
power inverters to its import-ban list** (a domestic-content constraint on node ③) and **Meta ×
BlackRock closed a $14bn, 1-GW ERCOT campus with capacity online 2028** (named, dated load at node ⑤).

## §E · Refutation + dated catalyst

**Kills the UW**: **S35 — median RS20 vs SPY of the seven > 0 by 2026-08-07** (now **−1.99**, improved
1.2pp from registration). **Kills the AI-power read**: **S24 — median RS20 of {VST, CEG, GEV, VRT} > 0
by 2026-08-12** (now **−10.31**, deepened from −5.68). **Third**: **real 10y > 2.55%** (now **2.44%**,
11bp away, quoted with breakeven **2.20%**) hits the regulated leg first (S9-C).
**Dates**: **WEC · ETR today · EXC · SO · XEL · AEP 07-30 · D 07-31 — ALL SEVEN absent from
`CATALYST_WATCH.json` (D18).**

---

# §X — Cross-sector LIVE shortlist names (outside the DEEP sectors)

`US_LIVE_SHORTLIST.json` carries 15 names; **11 sit inside the four DEEP sections above.**
**The four that do not are carried here rather than dropped**, per the stage rule:

| Ticker | GICS | Tilt | Flow / RS20 / RS60 / surge | Numbers | Verdict |
|---|---|---|---|---|---|
| **T** | Comm Svcs | **N−** | 🟢 +0.94 · **+13.0 / −8.7** · **1.49** | fwd **9.50** > trail 8.06 (**forward EPS is FALLING, $3.03 → $2.57**), P/B 1.52, **+17.6% to target**, next-yr **+0.5%/90d** | ⚠ **D51, now FIVE sessions**: the board's #2 flow is a post-earnings drift off an 8-K filed 07-22. ⚠ **Margin percentile unobtainable — series truncates at FY2014, confirming D91.** **Not called cheap.** Carried, no new thesis |
| **PLD** | Real Estate | **N** | 🟢 +0.85 · +5.9 / +0.5 · 1.48 | **fwd 42.49 > trail 32.20**, P/B 2.51, +9.1% to target, next-yr **+0.7%/90d** | ⚠ **Flow and fundamentals point opposite ways** (carried thesis, unchanged): a frozen book at a **rising** forward multiple. **Margin percentile `blank`.** ★ **It is S25's only event-free control** |
| **TMO** | Health Care | **N** | 🟢 +0.83, **`new_green`** · **+13.8 / +17.3** · 1.36 | fwd 21.06, P/B 4.14, +8.4% to target, next-yr +0.6%/90d | ★ **Health Care's ONLY green — and it is INSIDE the named top-6 cap block, so C7's resolving observable ("one 🟢 from OUTSIDE the top-6") reads ZERO for a 4th run.** FINRA **z −1.39 ✅ clean rise.** ⚠ Percentile unobtainable (series ends FY2017) |
| **GM** | Cons. Disc. | **N−** | 🟢 +0.80 · **+16.8 / +14.4** · 1.24 | **fwd 6.24** vs trail 40.65, **P/B 1.29**, +8.3% to target, next-yr **+5.3%/90d** | ⚠ **Every measured axis passes and the sector tilt is N−.** Per the carried rule this desk **does not reject a name on a sector label while its measured flow passes** — so it is **re-filed here with no thesis**, not dropped. ⚠ **Percentile unobtainable (series ends FY2021) ⇒ the 6.24× forward is NOT called cheap** |

---

# §GAP — Cycle-exposure epicenter module (PREMORTEM Lens 4 → BET)

`CYCLE_EXPOSURE.json`, live read-only KIS book: **≈$11,582 total, $4,332 invested, ~62.6% cash.**

| Cycle | rank | epicenter % | floor | margin | Flag |
|---|---|---|---|---|---|
| AI-compute / semiconductors | 1 | **8.32%** | 12.0% | **−3.683pp** | 🚨 **GAP — real** |
| Energy / oil-refining | 2 | **7.72%** | 8.0% | **−0.277pp** | ⚠ **INSIDE D61's ±0.5pp band ⇒ `unresolved`, not a fail** |
| Missile-defense | 3 | 7.54% | **none set** | — | ⚪ **a rank-3 cycle with no floor can never fire a GAP** |

**The rule this module exists for**: *a partial core in a top-rank cycle's epicenter belongs on the
sheet regardless of tape; the tape gates only the remainder.* **Stated as influence illustration, not
a recommendation (P4).**
★★ **And this run cannot name a clean expression, which is itself the finding.** Held epicenter is
**NVDA 🟡 +0.14 (OBV 매집, RS20 +1.1 / RS60 −4.4)** and **AVGO 🟡 −0.07 (RS60 −11.8)** — both negative
on the 60-day window, **inside a sector with 0 greens of 56 and 29 reds.** **There is no 🟢 anywhere in
Information Technology to point at.** The cleanest measured expressions in the value chain are
**DELL and HPE**, which are **one layer off the epicenter** and whose **RS20 has just crossed
(DELL −5.4)**. ⇒ **The GAP is real, the registry offers no clean instrument today, and no name is
manufactured to fill it.**
★ **Energy: MPC now reads as held epicenter for the first time**, joining PSX and XOM.

---

# §R — Rejection ledger, this run

**Three filed, each with BOTH required fields** (`add` will not run without them):

| Date | Ticker | Class | One-line basis | `--revives-if` | `--recheck-date` |
|---|---|---|---|---|---|
| 2026-07-29 | **CAT** | `C.차트붕괴` | INDU's worst RS20 (**−18.6 vs SPY**) with RS60 −8.6 and flow −0.76, **inside the same capital-goods node as this run's four greens**; margin percentile **UNUSABLE (99.9% XBRL artifact)** so L2 cannot support a cheapness case at fwd 26.66× | RS20 vs SPY back above 0 on settled closes **AND** a 🟢 tag with `vol_surge` ≥1.2 | **2026-08-12** |
| 2026-07-29 | **EXC** | `A.flow미도착` | flow −0.18 with RS20 only **+0.4**, and **the only net-negative revision book in the regulated seven (30d 4↑:6↓)**; prints 07-30 into an S35 window tracking branch B | 30-day revision breadth turns net-positive **AND** `flow_score` > 0 | **2026-08-12** |
| 2026-07-29 | **AEP** | `D.약한손` | **the weakest of the seven regulated names on every axis** — flow −0.69, RS20 −3.6 / RS60 −6.1, `vol_surge` 0.63 | `flow_score` > 0 **with** RS20 vs SPY above 0 on settled closes | **2026-08-12** |

**Names deliberately NOT filed, with the reason** (the 475150 precedent — *removal is for names the
**measured** axes reject*):
- **GM** — sector tilt is N−, **every measured axis passes.** Re-filed in §X with no thesis.
- **T** — its #2 flow is a post-earnings drift (D51, 5 sessions) and its forward EPS is falling, **but
  RS20 +13.0 and a volume-path 🟢 both pass.** Carried, conviction unchanged, **not rejected**.
- **PLD** — flow and fundamentals disagree; **the flow passes**, so it is re-filed rather than removed.
- **PANW · CRWD** — re-tagged **EXHAUSTED** by PREMORTEM Lens 3 (RS20 crossed negative). ⚠ **Not
  filed**: they remain the **named carve-out** from the IT N−, and a momentum re-tag is not a measured
  rejection. **CRWD already carries a ledger recheck 09-02.**

**Revived this run: none.** `reject_ledger.py due` returned **0 rows with a passed recheck date**.
**One legacy row was audited and resolved `reaffirmed` at HANDOVER (373220 LG에너지솔루션) ⇒ legacy 5 → 4.**

---

## ✅ EXIT CHECK

- [x] **Every DEEP sector has a section** (ENRG · FIN · INDU · UTIL), and the **four cross-sector LIVE
      shortlist names are carried in §X**, none dropped silently.
- [x] Numbers cross-checked inline (the trailing→forward EPS arithmetic in §ENRG §A); **blanks are
      blanks** — eleven names carry an explicit `unobtainable` / `blank` percentile and **not one of
      them is called cheap** (§0-2).
- [x] Flow/positioning cross-read present per candidate; **ONE file**, per-sector sections.
- [x] **Every set-aside name is in the ledger with a class AND both required fields** (§R). **No
      rejection was filed with an empty revival condition.** Names whose stored condition has come
      true: **none** (`due` = 0).
- [x] **No name was removed on narrative grounds while its measured flow still passed** — GM, T, PLD,
      PANW and CRWD are each **re-filed or carried with the reason stated**, not absent.
- [x] **Zero buy/sell language.** The §GAP module is written as influence illustration and explicitly
      declines to name an instrument the data does not support.

---

# §ALPHA — freshness gate (stage 9 fills the §B placeholders above)

## ★ ZERO 🟢LIVE tags were issued this run, and the reason is deterministic

`theme-age --scope foreign`, ten probes, **each term passed as separate argv**:

| Theme | Verdict | Age (d) | 7d avg | Acceleration | n |
|---|---|---|---|---|---|
| **CXMT** | 🟡ACCELERATING | **76** | 35.6 | ★ **19.4×** | 320 |
| backlog | 🟡ACCELERATING | ≥90 | 121.4 | 4.46× | 2,166 |
| freight | 🟡ACCELERATING | ≥90 | 50.7 | 3.90× | 1,008 |
| diesel | 🟡ACCELERATING | ≥90 | 31.9 | 3.39× | 681 |
| insurance | 🟡ACCELERATING | ≥90 | 145.3 | 3.15× | 3,299 |
| humanoid | 🟡ACCELERATING | ≥90 | 33.1 | 2.95× | 806 |
| refining | 🟡ACCELERATING | ≥90 | 80.9 | 2.79× | 2,182 |
| **inverter** | 🟡ACCELERATING | ≥90 | **6.9** | 2.24× | **212** |
| `data` / `center` | 🟡 / 🟡 | ≥90 | 1,351.6 / 597.1 | 2.61× / 2.89× | 37,007 / 15,525 |
| `rate` / `hike` | 🟡 / 🟡 | ≥90 | 962.1 / 205.0 | 2.98× / 2.42× | 24,487 / 6,440 |

★ **Every probe returned 🟡ACCELERATING. Zero 🟢FRESH, zero 🔴FADING — the SIXTH consecutive
replication of M112/M154/M180/M210 on the foreign feed.** The verdict column carries **no
discrimination**, so **it was not used as a gate anywhere**; only the acceleration ratio **read beside
its n** was.
⇒ **A 🟢LIVE tag would have to rest on a freshness axis that produced no signal.** Following the
precedent the 2026-07-29 `industry_kr` run set — *a desk that manufactures a 🟢 on a run like this is
describing its own appetite, not the tape* — **this run issues 🟡PARTIAL or 🔴RESOLVED only.**

★★ **CXMT separates a third consecutive run and by more: 19.4× on n=320 against a runner-up of 4.46×
= 4.4× the next-highest**, and its own ratio rose **17.74× → 19.4×** with n **273 → 320**.
⚠ **This DISAGREES with MACRO §C-1's pool-normalized reading, which had CXMT DECELERATING
(3.51× → 1.79×).** The two measure different things — `theme-age` is a 7-day mean against the term's
whole history; the bucket sweep is d1 against d7/7 on a partial day. **Both are reported; neither is
resolved into the other (C4).** ★ **And the accelerating theme is the one that runs AGAINST the
desk's memory proposition (S34/S37), not one it is positioned in.**
⚠ **D88-class note**: `data center` and `rate hike` were split into single tokens by the tool, so
those rows are two tokens each, **not the phrase** — read as such, not as a phrase measurement.
⚠ **`inverter` is real but tiny**: 2.24× on a 7-day average of **6.9 articles/day**. The FCC ban's
tradeable leg is a small theme, and its direct instruments are outside `us_top300`.

## §B tags — every name on the sheet, with its evidence label, date and re-check

> **A 🟡PARTIAL is a dated appointment, not a shelf.** Every residual below carries an explicit
> re-check date and is handed to `carryover` for the next run — **independently of whether its sector
> holds a DEEP slot** (the 006360 lesson: an ALPHA-tagged name went +12.3% over five unowned sessions).

| Name | Tag | Residual — what is still missing | Flags | **Re-check** |
|---|---|---|---|---|
| **MPC** | 🟡PARTIAL | Settled crack at a window high with the kill line **12.22 away**, but the **live 07-29 tape reversed it** and the print is unread | — | **2026-08-05** |
| **PSX** | 🟡PARTIAL | Same, **plus its days-21-60 excess flipped NEGATIVE (−5.91)** while MPC's held | ⚠ `core_pick` is human-locked and its ticket rationale is stale (§T) | **2026-08-06** |
| **VLO** | 🟡PARTIAL | **Margin percentile structurally blank (D56, 5th run)** ⇒ L2 cannot run | ⚠ FINRA 5v5 **+6.0▲** into its print | **2026-07-31** |
| **XOM** | 🟡PARTIAL | RS60 **−3.9** against RS20 +12.5 — S31's own 20-vs-60 gap; **percentile now blank too (NEW)** | ⚠ FINRA 5v5 **+8.2▲ = board's largest build**, into its print | **2026-08-03** |
| **BX** | 🟡PARTIAL | ★ **No 4Phase exists ⇒ no thesis may be built.** Flow and valuation gaps closed; the thesis gap is not | ⚠ next-yr revisions **−1.1%/90d** at P/B 11.5 | **2026-08-06** |
| **CB** | 🟡PARTIAL | **+0.6% to the mean target — the move is made**; the surviving case is the S26/S41 hedge, not upside | — | **2026-08-06** |
| **TRV** | 🟡PARTIAL | **98.6% of its 60-day excess landed in the last 20 sessions** (M150, R9/AXON geometry) | ★ **MOMENTUM-ONLY — hard-stop required** | **2026-08-06** |
| **WAB** | 🟡PARTIAL | ★ **FY25 gross margin = the MAX of an 18-year series at 24.25× forward** (L2 CONFIRMED) | ★ **MOMENTUM-ONLY — hard-stop required.** 8-K 07-22, 4 sessions before the snapshot (D51) | **2026-08-12** |
| **PCAR** | 🟡PARTIAL | Near its own margin **trough** at 19.7× — the inverse shape — but **−6.8% to its mean target** | ★★ **MOMENTUM-ONLY — 8-K Item 2.02 filed 2026-07-28, the SAME session as the flow snapshot. Hard-stop required** | **2026-08-12** |
| **ITW** | 🟡PARTIAL | ≈93rd-percentile margin at 24.10× with a **0↑:1↓** book | ★★ **MOMENTUM-ONLY — 8-K filed 2026-07-28, same session. Hard-stop required** | **2026-08-12** |
| **MMM** | 🟡PARTIAL | ≈12th-percentile margin (near trough) at 18.76× on a **4↑:0↓** book — the cleanest of the four — but **0.0% to its mean target** | ★ **MOMENTUM-ONLY — 8-K 07-21. Hard-stop required** | **2026-08-12** |
| **RTX** | 🟡PARTIAL | **Margin percentile unobtainable (series ends FY2017)** ⇒ no valuation claim at 27.71× | held epicenter of the rank-3 cycle, which **has no floor set** | **2026-08-12** |
| **LMT** | 🟡PARTIAL | ★ **The one prime whose L2 runs: FY25 10.2% is BELOW its own median (11.1) at 17.62× forward** — not a peak-margin name | FINRA **z −1.86 ✅ clean rise** | **2026-08-12** |
| **UNP · CSX · NSC** | 🟡PARTIAL | **All three percentiles blank.** ⚠ **M91 unretracted — ~8 of UNP's 12 revenue growth points are FUEL SURCHARGE**, so this is the Energy bet again | UNP **z −3.13 ✅** = the cleanest short-collapse on the sheet | **2026-08-04** (S20-ANNEX) |
| **D** | 🟡PARTIAL | Positive on both windows but on `vol_surge` **0.48** and a **flat** book; prints 07-31 | accumulation on no volume | **2026-08-07** (S35) |
| **PCG** | 🟡PARTIAL | **9.92× at 1.22× book with +28.0% to target — and no percentile exists, so it is NOT called cheap.** ⚠ **Does not report until 2026-10-22** | — | **2026-08-07** |
| **T** | 🟡PARTIAL | Forward EPS is **falling** ($3.03 → $2.57) so fwd 9.50 > trail 8.06; **percentile unobtainable (D91 confirmed)** | ★ **MOMENTUM-ONLY — post-earnings drift now FIVE sessions (D51). Hard-stop required** | **2026-08-06** |
| **PLD** | 🟡PARTIAL | **fwd 42.49 > trail 32.20 on a frozen book**; flow and fundamentals point opposite ways | S25's only event-free control | **2026-08-08** (S25) |
| **TMO** | 🟡PARTIAL | ★ **Health Care's only 🟢 and it is INSIDE the named top-6 cap block ⇒ C7's observable reads ZERO a 4th run** | FINRA **z −1.39 ✅** | **2026-08-06** (C7) |
| **GM** | 🟡PARTIAL | Every measured axis passes inside an **N−** sector; **percentile unobtainable (series ends FY2021) ⇒ the 6.24× forward is NOT called cheap** | — | **2026-08-12** |
| **CAT** | **🔴RESOLVED — DROPPED** | Worst RS20 in INDU (**−18.6**) with the percentile **unusable** | filed `C.차트붕괴` | **2026-08-12** |
| **EXC** | **🔴RESOLVED — DROPPED** | Only net-negative revision book of the regulated seven (**4↑:6↓**) | filed `A.flow미도착` | **2026-08-12** |
| **AEP** | **🔴RESOLVED — DROPPED** | Weakest of the seven on every axis | filed `D.약한손` | **2026-08-12** |

**All three 🔴 are logged as LEDGER ROWS with a reason class, a `--revives-if` condition and a
`--recheck-date`** (BET §R) — **not as prose.** ⚠ **PANW and CRWD were re-tagged EXHAUSTED by
PREMORTEM Lens 3 and were deliberately NOT filed**: a momentum re-tag is not a measured rejection,
and they remain the **named carve-out** from the IT N−.

## §T — ACTION_TICKETS.md, and two caveats that must travel with it

`scripts/action_bracket.py` wrote **4 conditional DRY-RUN tickets** to
`llm_outputs/2026-07-29/ACTION_TICKETS.md`: two **CORE-STARTERs** (NVDA for the AI-compute GAP, PSX
for the Energy GAP) and a **both-sides FOMC bracket** (`A_cool` → NVDA · `B_hot` → XLE).
**Analysis→ticket conversion only; a human executes separately, and no order is sent by the script.**

⚠ **Caveat 1 — D19 fires a FOURTH time: PSX's `why core` string is stale.** It reads *"cheapest large
refiner on forward (11.2, PEG 1.17) … FINRA short-vol z −1.43, 5v5 −16.6▼"*. **R8 retracted the
"cheapest" claim on 2026-07-22** on a like-for-like FY26 basis, and **the FINRA figures are a frozen
string this run did not re-pull.** ★ **Measured today, the basis-dependence R8 identified cuts the
other way**: on forward P/E, **PSX 11.06 < MPC 11.27 < VLO 12.24** — so PSX *is* currently the lowest
of the three on *this* basis, at **11.06, not 11.2**. **The ticket's number is close and its basis is
still unstated, which is exactly D19's complaint.** ⚠ `core_pick` is **human-locked and no stage may
rewrite it.**

⚠ **Caveat 2 — the Energy GAP the PSX ticket closes is `unresolved`, not a fail.** Its margin is
**−0.277pp against a 8.0% floor**, which sits **inside D61's proposed ±0.5pp band** and flipped sign
on drift alone one session ago with nothing traded (M181). **The AI-compute GAP (−3.683pp) is outside
the band and is real.** ★ **And this run could not name a clean epicenter expression for it**: the
held names are **NVDA 🟡 (RS60 −4.4)** and **AVGO 🟡 (RS60 −11.8)** inside a sector with **0 greens of
56 and 29 reds. No name was manufactured to fill the gap.**

## ✅ EXIT CHECK (stage 9)

- [x] **Every §B tag filled with an evidence label and a date.** **Zero 🟢LIVE issued, with the
      deterministic reason stated** (six consecutive all-🟡 theme-age runs ⇒ the freshness axis carries
      no discrimination and was not used as a gate).
- [x] **All three 🔴RESOLVED names dropped AND logged as ledger rows** with a class, a `--revives-if`
      condition and a `--recheck-date` (`reject_ledger.py add` accepted all three; it rejects calls
      missing either field).
- [x] **Every 🟡PARTIAL carries an explicit re-check date**, and **every ALPHA-tagged name above is
      listed for carry-forward independently of its sector's DEEP slot** next run.
- [x] **Momentum-only flags stamped** (WAB · PCAR · ITW · MMM · T · TRV — each with `hard-stop
      required`), and **positioning flags stamped** (XOM 5v5 +8.2▲ · VLO +6.0▲ into their prints;
      **no name on the shortlist reads ⚡crowded-short**).
- [x] **`ACTION_TICKETS.md` written** (both-sides FOMC bracket + two cycle-GAP core-starters), with
      **two caveats attached** — the stale D19 rationale string and the `unresolved` Energy GAP.
