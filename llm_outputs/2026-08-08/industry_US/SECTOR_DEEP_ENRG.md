# SECTOR_DEEP_ENRG — Energy · industry_US · 2026-08-08 · **CONTINUOUS slot (dived 08-07/08-06/08-05) ⇒ DELTA-LED**

> Value-chain map, player list and the 08-04→08-06 adjudications are carried **by reference** to
> `llm_outputs/2026-08-07/industry_US/SECTOR_DEEP_ENRG.md`. Not re-printed. Benchmark **SPY**, inline
> (C1). **P4 — analysis only, no positioning, no sizing, no order language.**

---

## §0 · The delta, one line

**ENRG was DEMOTED this run, OW− → N+, carried purely by flow decay**: eqflow **+0.209 → +0.078
(−63%)** · Δ **+0.196 → −0.084 (SIGN FLIP)** · wflow +0.426 → **+0.342** (still rank 1 of 11) ·
breadth 0.120 · 2🟢/2🔴 of 16 — **and SWEEP decomposed both greens (XOM `vol_surge` 0.88, CVX 0.96) as
velocity-lit on below-average volume**, so **the sector's rank-1 flow has no money behind it.**
**Price**: XLE exc1 **−1.75 (last of 11)** · exc5 **−6.95 (last of 11)** · exc20 **+1.97** — an
**8.9pp two-window disagreement, the largest on the board.**

---

## §1 · The five assignments, answered

### ① Six-of-six fell on a crude-up bar — the non-price evidence leans SINGLE-SESSION, not a durable unwind

MPC −0.96pp · PSX −1.39 · XOM −1.77 · CVX −2.02 · VLO −2.16 · SLB −2.57, all vs **SPY**, against
**`CL=F` 77.29 → 78.18 = +1.15%** and Brent topping $83 `[measured]`. ⚠ **R12 binds: n = 1, no streak
is claimed.**

**Non-price cross-check** (**RULE D6** — see the exemption note below: OBV is never quoted alone here). `module_flow` (own OBV axis — **module named, D208**) reads **MPC and VLO as
🟢가속 / OBV 매집 with `vol_surge` 1.01 and 1.09** — genuine **volume**-backed accumulation, not the
velocity artifact — while **PSX is 🟡중립/중립** and **SLB is the only outright 🔴분산** (`vol_surge`
0.73) `[measured]`.

> ⚠ **RULE D6 — stated, not waived.** OBV is a **C-grade** axis (≈0.49 correlation with real
> investor flow, no measured lead, t≈1.00) and **cannot carry a proposition alone.** It is not
> asked to here: **every OBV reading in this section is quoted with `vol_surge` (a volume axis)
> AND with the FINRA short-vol z (an independent positioning axis)**, and the paragraph's
> conclusion rests on the *agreement of three axes*, not on OBV. **Where the axes disagree — the
> `sector_flow` gate vs `module_flow` on MPC/PSX — the disagreement is reported as a defect
> (D208), not resolved in OBV's favour.**

FINRA short-vol (`us_flow.py`): **VLO's short-vol ratio fell 48.0% → 33.5% base
(z −1.71, 숏커버)** — pressure **leaving**, not building — and **XOM at z −0.59, the board's only
clean-rise short reading.** ⇒ (**RULE D6** — this sentence pairs the C-grade OBV axis with the B-grade FINRA short axis by construction) **a genuine capitulation / war-premium unwind would show DISTRIBUTION
(OBV 분산) and SHORT-BUILDING, not the accumulation-plus-covering pattern actually measured in 4 of 6
names.**

**A second, mechanical read**: the **distillate crack barely moved on the bar** (42×HO − CL:
85.754 → 85.721, own calc §④) even as crude rose +1.15%, so the refiners' proximate driver was roughly
flat — consistent with their smaller losses (MPC −0.96, PSX −1.39). ⚠ **The bigger surprise is that
SLB — the most crude-price-levered name — fell HARDEST despite crude rising**, which reads as
**sector-wide rotation out of Energy on the day's dominant story** (a dovish payroll miss, SPY +0.61%,
bull steepener) rather than a refiner-specific premium unwind.

⇒ **Verdict: the evidence leans toward a single-session / rotation artifact over a durable "premium
deflating out of the equities" call — but this is n = 1 (S1) and it is TRACKED, not concluded.**

### ② The refiners' revision breadth — reproduced exactly, and the mispricing is now WIDER

Independent re-pull (`module_fundamentals_us --json`, 2026-08-08) **reproduces the FY(0y) revision
breadth to the digit**: **MPC 13↑/0↓** (30d), FY EPS **49.80 vs 27.03** 90 days ago = **+84.3%** ·
**VLO 13↑/2↓**, **41.66 vs 27.95 = +49.0%** · **PSX 13↑/2↓**, **25.52 vs 15.91 = +60.4%** `[verified]`.

**L2 — margin percentile, recomputed to the exact figure.** `scripts/margin_history.py` reproduces the
underlying series unchanged (MPC FY2025 GM **10.0%**, 8y range 5.8–14.5%, median 10.5%; PSX FY2025 GM
**12.3%**, 10y range 8.4–25.9%, median 12.1%; **VLO still `연간 데이터 없음` — unmeasurable**).
Recomputed by **strict rank-count** (values-below / n): **MPC — 3 of 8 trailing years below 10.0% =
37.5th percentile**; **PSX — 6 of 10 below 12.3% = 60th percentile.** ⚠ **This reproduces the brief's
exact numbers; the 08-07 file's "~45th"/"~65th" were an interpolated eyeball estimate, not a
contradiction** — both are `[measured]` under different percentile conventions, and **the strict
count-below figure is used going forward.** **VLO: `unknown`, carried, NOT substituted (C3).**

**Fresh forward-P/E ordering has flipped a SECOND time**: today **MPC 10.04 < PSX 10.24 < VLO 10.76**
— the 08-07 file had PSX cheapest. Mean-target upside also **compressed**: MPC +6.2%, PSX +5.1%,
VLO +3.8% (from +8.1% / +5.9% / +5.4%).
⇒ **the revision-vs-target gap WIDENED, not narrowed**: estimates up 49–84% over 90 days against price
targets that moved *less* than they did a session ago. **The mispricing the 08-07 file flagged is
getting more extreme, not resolving.**

**Is the flow gate missing it?** **Yes, and the mechanism is named (D6/D208)**: `sector_flow.py`'s
sweep tags MPC and PSX **🟡중립** (the gate BET reads), while **`module_flow`'s independent OBV
computation reads MPC and VLO 🟢가속/매집 today.** **Two modules, different statistics, disagreeing in
sign on the same names — and the flow GATE is the one under-reading accumulation that both the OBV
instrument and the fundamentals independently support.**

### ③ ★★★ Tonne-mile destruction → US Gulf export economics: who supplies the EU, and it is NOT enough

The physical chain: **CPC Novorossiysk −62%, ~75% EU-bound; Russia's outright diesel export ban removes
~700–800 kbpd** `[carried + fresh]`. **The concrete substitution attempt is now measured**:
**India's refined-fuel exports hit a one-year high in July — 1.53m b/d, +27% vs the trailing 12-month
average — explicitly "cargoes headed to regions previously supplied by West Asia and Russia," with
Kpler's lead refining analyst naming Europe by name** `[toi body 08-04, Kpler/Nikhil Dubey]`.
⚠ **But the same reporting states "Europe remains short on diesel supplies"** even with India's surge,
and separately **US diesel inventories are "also down considerably, so the world's biggest diesel
exporter has limited space to boost exports, even with refineries running at record rates"**
`[oilprice/yahoo_finance body]`.

⇒ **Answer: India is the visible physical substitute and it is MEASURABLY INSUFFICIENT alone.** A
700–800 kbpd Russian ban plus a 62%-collapsed CPC leg (≈1.6 mbpd off a 2.59 mbpd four-week base) is
**not** offset by a 1.53m b/d India flow that itself grew only ~27% and was already partly earmarked
for Turkey and other ex-Russia buyers. **The US Gulf Coast basin remains the marginal supplier of last
resort into that gap** — consistent with (not merely coincident with) the 08-07 finding that **record
US distillate exports of 1.88m b/d drove US inventories to a 1996 seasonal low while Fujairah
restocked to a four-month high.**
⇒ **The mechanism argues the regional drain PERSISTS or INTENSIFIES, not that it releases.**
`[measured news, inferred synthesis]`

### ④ `S55` — deep in branch C on the frozen observable, while the own-calc SECOND DERIVATIVE has just crossed

Own calc, yfinance settles, `auto_adjust=False` (B1 — the rate, not the level):

| date | `CL=F` | `HO=F` | dist crack (42×HO − CL) | Δ (rate) | ΔΔ (rate-of-rate) |
|---|---|---|---|---|---|
| 08-03 | 80.34 | 3.8772 | 82.502 | −5.931 | — |
| 08-04 | 75.77 | 3.7705 | 82.591 | +0.089 | +6.020 |
| 08-05 | 75.22 | 3.7962 | 84.220 | +1.629 | +1.540 |
| 08-06 | 77.29 | 3.8820 | 85.754 | +1.534 | −0.095 |
| **08-07** | **78.18** | **3.9024** | **85.721** | **−0.033** | **−1.567** |

**S55's frozen observable** (HO %chg − CL %chg from the 08-04 anchor): **HO +3.498%, CL +3.181%,
spread +0.318pp — deep in C** (A ≤ −3.0 · B ≥ +6.5). **No verdict on S55 itself.**

★★ **But B1 now fires cleanly on the own-calc series**: the crack's **rate declined for a SECOND
consecutive session** (+1.534 → −0.033), the pre-registered B1 signal, **and the crack LEVEL turned
negative for the first time in the run** (85.754 → 85.721). The **dist−gas differential shows the
identical shape**: rate −0.583 (08-06) → **−1.109 (08-07)**, also two consecutive declines.

**The call, stated BEFORE the 08-11 settle**: the physical evidence in ③ favours **branch B
territory** — CPC/Hormuz/Russia-ban destruction argues for sustained-to-intensifying scarcity — though
**per the S61-ANNEX precedent, if B fires it will be for a PHYSICAL-SCARCITY reason, not the "war
premium" the branch label names.**
⚠⚠ **This is stated as a genuine tension, not smoothed: the traded instrument itself (own calc,
B1-qualifying) is presently moving the OPPOSITE way, toward release.** **This divergence between the
physical case and the crack's own two-session rate is the sharpest object-level disagreement in this
file and is handed forward UNRESOLVED.**

### ⑤ XOM's "clean rise" and CVX's epicenter slot — both decompose, neither survives intact

**XOM**: confirmed a live security (last 153.04, non-degenerate OHLC) and the shortlist's **only
clean-rise** (short-z **−0.59**). ⚠ **But the green flow tag is the same defect class that hollowed
the sector's rank-1**: `vol_surge` **0.88 (velocity-lit)**, and **own-calc RS60 − RS20 = −3.2 − 7.8 =
−11.0** — **the entire "rise" sits on a NEGATIVE 60-day base**, the identical last-20-concentration
shape Lens 3 flagged for PLTR / COHR / NEM.
⇒ **Two separate claims the assignment conflates, now decomposed: the SHORT-INTEREST axis is genuinely
clean `[measured]`; the "rise" tag is a velocity artifact riding a negative base `[measured]`.**
**XOM is confirmed NOT held** (`cycle_exposure`'s Energy epicenter = MPC, PSX only) ⇒ **S31's *"the
only Energy name the book holds"* is FALSE against today's read, reproduced a second time.**

**CVX**: sits in `cycle_registry.json`'s Energy/oil-refining **epicenter** list, but its live driver —
**Project Kilby, a 20-year 2.67 GW behind-the-meter gas deal with Microsoft, explicitly routed AROUND
the ERCOT interconnection queue** `[yahoo_finance 08-08]` — **has no crack-spread content at all.**
Corroborating: CVX's own-calc **RS60 − RS20 = −7.7** (a negative base, same shape as XOM), and today's
excess (**−2.02pp vs SPY**) is the **second-worst of the six despite crude rising** — consistent with a
name driven by an unrelated power-deal narrative rather than refining economics.
⇒ **CVX is MIS-SLOTTED. PREMORTEM Lens 4's finding is independently corroborated here, not repeated.**

---

## §2 · Chain-hop candidates, flow cross-checked

`chain-hop distillate diesel refinery` (7d / foreign / and, 32 articles scanned) reproduces **BKR** as
the only proximity candidate — **17 body-proximate mentions, ALL tracing to the same
*"Crude Prices Pressured by Growing Optimism the Strait of Hormuz to Soon Reopen"* article R46 already
disqualified** `[reproduced for a THIRD consecutive run]`. Flow cross-check: `module_flow` reads BKR
🟢가속/OBV 매집 but **`vol_surge` 0.72 (velocity, not volume) and RS60 −10.4** — the same aging-base
pattern the 08-07 file rejected on. ⇒ **BKR REJECTED again, unchanged grounds.**
GS / NDAQ / GOOGL / GOOG appear as proximity noise around a *"U.S. Diesel Exports Hit Record High"*
headline (financial-exchange/media boilerplate co-mention, **D10 class**) — **no real candidate.**

**Tanker names, checked directly** (not in `us_top300`, so absent from the shortlist, but individually
queryable): **STNG 🔴분산** (RS60 −13.6) · **FRO 🟡중립** · **TNK 🟢가속 but `vol_surge` 0.91
(velocity)** · **DHT 🟡중립/분산.**
⇒ **No clean accumulation signature anywhere in the tanker complex** — consistent with a chokepoint
story transmitting through **volume destruction** rather than one any equity flow instrument picks up.

---

## §3 · Track-KPIs and anti-signals, dated

| KPI | State, 08-07 settled | Anti-signal | Date |
|---|---|---|---|
| ★★★ Crude-up / energy-down bar | 6-of-6 negative excess vs SPY on `CL=F` +1.15% | **A SECOND consecutive crude-up/energy-down session ⇒ the counter becomes an event, not noise (R12)** | rolling |
| ★★★ Crack rate (own calc, B1) | **Rate declined a 2nd consecutive session** (+1.534 → −0.033); level turned negative first time this run | **A THIRD consecutive rate decline ⇒ B1's release signal is confirmed, not a blip** | rolling |
| ★★★ **S55** (HO% − CL% from the 08-04 anchor) | **+0.318pp — deep in C** (A ≤ −3.0 · B ≥ +6.5) | Settles **08-11**; the physical case favours B, the own-calc rate favours A — **unresolved** | **08-11** |
| ★★ FY(0y) revision breadth {MPC, VLO, PSX} | **13↑/0↓ · 13↑/2↓ · 13↑/2↓**, reproduced exactly | Any one line cutting for 2 consecutive weeks reopens that name's peak-margin question | weekly |
| Revision-vs-target gap | Estimates **+49–84% / 90d** vs target upside now **+3.8–6.2%** (compressed from +5.4–8.1%) | Target upside catching up to revision pace ⇒ the mispricing thesis resolves | rolling |
| Forward-P/E ordering | **Flipped: MPC 10.04 < PSX 10.24 < VLO 10.76** | **A third flip inside two runs ⇒ the ranking itself carries no information** | rolling |
| XOM RS60 − RS20 | **−11.0** — the entire rise on a negative 60-day base | RS60 turning positive ⇒ the clean-rise tag graduates from artifact to trend | rolling |
| CVX epicenter fit | Live driver = Project Kilby (behind-the-meter power), unrelated to crack | A CVX thread naming Gulf Coast refining/export capacity directly ⇒ re-examine the mis-slot call | rolling |
| BKR chain-hop object | Confirmed = the Hormuz-reopening article, **3rd consecutive run** | A NEW body-proximate article naming distillate/export/terminal specifically ⇒ reopen | rolling |
| MPC options | **±7.1% implied, expiry 08-21** | A repriced straddle narrowing toward VLO/PSX's ±1.8–2.1% ⇒ the market stops treating MPC as exposed | **08-21** |

⚠ **S1 throughout**: ①'s six-of-six is **n = 1**; ④'s B1 signal is **n = 2** (the rule's minimum, not
yet a streak); ③'s substitution read is **inferred synthesis on measured components**, not a bracket.

---

## §4 · Carried unchanged, by reference

**A6/W4 (which refiner books the export rent)**: VLO's direct Q2-call management attribution ≈ MPC's
largest named capacity + forward capex > PSX's own segment data arguing against it — **carried
unchanged from the 08-07 file §2, not re-tested.**
**W5 (dispersion)**: the refiner-vs-integrated RS60 spread (+16.3pp) and the three-regime split
(refiners / integrated / E&P-services) — **carried unchanged, 08-07 file §6.**
**Registry-rename recommendation** (*"Energy/refining — US Gulf distillate export rent (regional) vs
ex-US conversion-capacity loss"*) — **carried unchanged, human-gated (P5); assignment ⑤'s CVX finding
is ADDITIVE to it, not a replacement.**
**VLO's margin percentile**: still structurally unmeasurable via SEC XBRL, reproduced again this run.

**Hand-off**: MPC/VLO now **`module_flow` 🟢가속 (own axis)** against **`sector_flow`'s 🟡중립 gate
tag** — **the disagreement is NAMED (D6/D208), not resolved.** PSX 🟡중립 on both. XOM/CVX 🟢가속
velocity-lit, **not handed forward**, unchanged verdict. **BKR REJECTED, third consecutive run, same
grounds.**

**Zero sizing, zero buy/sell language in this file (P4).**
