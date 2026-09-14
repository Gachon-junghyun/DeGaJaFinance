# SECTOR_DEEP_FIN — Financials, non-bank mandate · 2026-07-22 (Stage 6 / L1·DEEP)

> **CONTINUOUS track, 8th pass. RECENCY-STARVED** — deep-dived 07-21 (twice), 07-19, 07-17, 07-15.
> Baselines carried **BY REFERENCE, not reprinted**: the 6-node value-chain map, the JPM/TRV/NDAQ 10-K
> anchors and the sub-sector player table live in `llm_outputs/2026-07-21/US_2/SECTOR_DEEP_40.md` §2/§4;
> the PYPL M&A resolution, the SCHW pre-print bracket and the bank-leg null result live in
> `llm_outputs/2026-07-21/industry_US/SECTOR_DEEP_FIN.md` §1/§3/§4. Neither is re-derived here.
> Mandate narrowed by ROTATION to **non-bank financials**. Flow asof **2026-07-21 close**
> (`SECTOR_FLOW_US.json`); FINRA z asof 2026-07-21; fundamentals pulled live 2026-07-22 pre-open.
> **Every rs20/rs60 below is vs SPY.** OBV / 🟢🟡🔴 are C-grade, corroborant only.
> Zero buy/sell, zero sizing.

## §0 · THE DELTA — three things moved since the two 07-21 files

1. **The 07-21 crowded-short ledger largely resolved, and its own falsifier fired.** [07-21 FIN] §5 wrote
   *"GS falsifier: z reverts below +1.0 within 3 sessions."* Measured 07-21: **GS z −0.11 (정상)** from
   +1.59 🔴. **STT z −0.13** from +1.50 🔴. Both anti-signals are **spent, not confirmed**. The new
   crowded short is **CB, z +1.61 🔴** (5v5 +14.8▲), and **TRV z −2.00 🟢** — extreme covering.
2. **The 20-day leg of the insurance bid is decelerating while the IB leg's 60-day is still building.**
   TRV rs20 vs SPY **+20.3 → +18.5**, CB **+9.6 → +8.6**, PGR **+4.2 → −1.2**; against GS rs60 vs SPY
   **+8.5 → +10.9**, MS **+6.1 → +9.1**. The A-grade axis is moving *against* the flow-score rotation.
3. **The "unrefreshed" reinsurance-pricing KPI from [07-19]/[07-21] is now REFRESHED — and it softened.**
   *"Arch Capital: The Real Test Begins As Reinsurance Pricing Softens"* [seekingalpha, 07-17] and
   **W. R. Berkley's own Q2 call: "pricing is becoming more competitive in parts of property and
   reinsurance"** [07-20], with WRB's Reinsurance & Monoline Excess loss ratio **57.7% vs 53.1%
   estimated**. The insurance leg's named bottleneck is confirming *against* the leg.

---

## §1 · Q1 — the steepening thesis is being expressed, but not where it was written, and not by the buyers

**Financials n=47, eqflow +0.357 > wflow +0.212, 5 greens.** Decomposed by sub-industry (mean flow · mean
rs20 vs SPY · mean rs60 vs SPY):

| Sub-leg | n | flow | rs20 vs SPY | rs60 vs SPY | Paid by |
|---|---|---|---|---|---|
| Payments | 4 | **+0.697** | +15.0 | +6.8 | consumer volume (PYPL is M&A — see [07-21 FIN] §4) |
| Insurance (all) | 12 | **+0.599** | +9.8 | +5.6 | underwriting margin, then float reinvestment |
| Banks (9) | 9 | +0.415 | +4.1 | +3.8 | **curve slope** |
| Exchanges/Data | 7 | +0.352 | +4.7 | −9.9 | volume/volatility |
| Asset mgmt / custody | 7 | +0.203 | +1.4 | +0.7 | AUM level + front-end NII |
| **IB / brokerage** | 5 | **−0.151** | **−0.5** | **+13.5** | **activity: fees, underwriting, trading** |

**The answer is that these are three different variables, and only one of them is the steepener.**

- **Inside the bank leg the steepener IS expressed — in super-regionals, not money-centers.** USB +0.783,
  PNC +0.647, FITB +0.642, HBAN +0.622 sit above JPM +0.420, WFC +0.328, BAC +0.318, C −0.611. Regionals
  borrow short and lend long; they are the purest 2s10s (**+0.39**) expression on the board and they are
  the best-bid banks. MACRO P1's mechanism is intact — the label "banks" was simply too coarse.
- **What pays P&C is not the curve.** TRV's Q2 combined ratio **83.6% (from 90.3% PY)** on cats **$518M
  vs $927M PY** and favorable prior-year development **$578M** [07-21 US_2 §3] is an underwriting-cycle
  number. Chubb's Q2 prints **both halves against each other**: *"Chubb Limited Announces Fall in Q2
  Income"* — net income **down YoY** — while *"Chubb exceeds Q2 earnings estimates on strong P&C
  underwriting"* on revenue **$15.xB** [nasdaq/seekingalpha, 07-21]. Float reinvestment at real 10y
  **2.35%** (FRED asof 07-20) with breakeven **2.26%** (asof 07-21) is a slow second-order contributor,
  not the driver of a one-quarter combined-ratio move of 6.7pp.
- **What pays custody is the front end and the market level, not the slope.** STT's NII is client-cash
  sweep income geared to Fed funds **3.63%** / 2y **4.21%** — both flat — plus AUC/A and AUM marks. Its
  own coverage says so: *"Macro Conditions Continue To Drive Healthy Operating Leverage"*, *"Favorable
  Macro And Expense Control Drive Strong Q2"* [seekingalpha 07-16/07-17]. Nothing there is a 2s10s trade.
- **What is being sold is an activity peak, and it is not a rates or a credit signal.** GS, MS and IBKR
  all carry the same shape: **positive rs60 vs SPY (+10.9 / +9.1 / +18.8) with negative rs20 vs SPY
  (−2.4 / −5.2 / −3.0)**. That is post-print mean reversion off a record quarter, not a downtrend —
  and it lands the same week *"Goldman Sachs and Morgan Stanley had a monster quarter"* [marketwatch,
  07-22]. **C is the only genuinely broken bank: −9.3 rs20 / −2.3 rs60 vs SPY, negative on both axes.**
  Grouping C with GS/MS as "the investment banks are being sold" mixes two mechanisms.

**Verdict on Q1:** the steepening thesis is being expressed *correctly* — in super-regionals. The bid in
insurers and custody is paid by **different variables entirely** (underwriting margin; AUM level and
front-end NII). The IB sale is paid by a **third** variable (deal/trading activity that just peaked).
Three variables, one GICS label.

---

## §2 · Q2 — the concentration audit: the double-count is in the *rationale*, not in the *exposure*

The PREMORTEM's charge is that long P&C plus short Utilities/Real Estate *on a rising-real-yield
rationale* is one levered bet on real 10y (**2.35%, 120-day high**, breakeven **2.26%**) counted twice,
and that S9 branch A (real 10y **<2.20%** with breakeven rising) takes out both legs on one tick.
Quantified against the tape, the charge holds for the **stated reason** and fails for the **executed
position**:

- **The genuinely rate-levered long leg is 3 names of 47.** Life insurers — the sub-leg with long-dated
  liabilities and a spread book — are MET, PRU, AFL: mean flow +0.579, rs60 vs SPY **+17.1 / +20.1 /
  +1.7** but rs20 vs SPY only **+6.1 / +9.0 / +5.5**, with **negative flow deltas at MET (−0.029) and
  AFL (−0.058)**. The purest duration expression in Financials has *already stopped adding.*
- **The 20-day insurance bid is led by the sub-leg with no rate mechanism at all.** Insurance brokers
  AJG **+18.2**, AON **+14.1**, MRSH **+12.9** rs20 vs SPY — fee-on-premium businesses with no float to
  reinvest. If this were a real-yield trade, brokers would not be at the top of it.
- **The short side, as the tape has it, is not a duration short.** Real Estate's **top two names on rs20
  vs SPY are WELL +16.0 and VTR +17.0** — classic duration REITs, bid at a 120-day-high real yield.
  Mean rs20 vs SPY of the five classic-duration REITs (WELL, VTR, SPG, O, PLD) = **+9.7**; mean of the
  four digital-infra REITs (AMT, DLR, EQIX, CCI) = **−8.5**. An 18.2pp spread inside a 12-name sector.
  In Utilities, only 2 of 15 names are 🔴 (CEG −0.615, PEG −0.425); regulated names are positive on
  rs20 vs SPY (PCG +4.6, ED +2.2, D +2.1, NEE +1.6, DUK +1.4).
- **S9-A tested name-by-name against the five FIN greens.** TRV/CB — second-order (combined ratio
  dominates); USB — a real-yield fall driven by front-end cuts *steepens* and helps; STT — front-end
  geared, indifferent to the 10y; PYPL — rate-neutral M&A. **S9-A hits zero of the five cleanly** and
  only partially hits the three life names.

**Verdict on Q2: no — the Financials OW is not a rates bet in disguise.** It is an underwriting-cycle
plus fee/AUM bet whose rates leg is 3 of 47 names and is decelerating. **But the PREMORTEM's warning
still binds, with the failure mode relocated:** if the UW on Real Estate and Utilities is expressed at
*sector* level, the desk goes short WELL/VTR/DUK — the duration longs its own rationale says to be short
— and *that* mismatch, not the FIN OW, is the live correlation error.

---

## §3 · Q3 — bank credit costs vs HY OAS: P2 gains a second, independent evidence class

KeyCorp was the day's largest news cluster (40 articles / 4 outlets). The credit-cost content, body tier,
`--scope foreign`: **"KEY Q2 Earnings Beat as NII & Fee Income Grow Y/Y & Provisions Dip"** [yahoo_finance,
07-21], with the article's own sub-head **"KeyCorp's Credit Quality: A Mixed Bag."** ⚠ The provision
*magnitude* did not surface in the snippet tier (MACRO's measured body-blind rate is 63.7%) — the
direction is sourced, the size is **[blank]** and not guessed. Both halves where available: NII and fee
income up **YoY**; provision direction down; **sequential provision not surfaced.**

The rest of the print wave, all dated 07-16 → 07-21, `--scope foreign`:

| Name | Credit-cost line | Direction |
|---|---|---|
| TFC (Truist) | provision **$395M**, *"modestly below net charge-offs"* | reserve release |
| MTB | provision fell **sequentially to $120M**; annualized NCOs **23bp** | down |
| WFC | commercial net loan charge-offs **declined to 10bp** | down |
| USB | Q2 NCO ratio **0.53%**, *"was down"* | down |
| ALLY | retail auto NCOs **157bp, down 18bp** | down |
| COF | total NCO **3.4%**; consumer banking **1.48%**; domestic card **4.x%** | high level, benign trend |
| SYF | *"strength in delinquency and net charge-off performance"*; FY26 reaffirmed — **but profit declined** | mixed |
| UCB | bank-only NCOs **9bp**, total **16bp** | down |
| Counter-evidence | **FSUN** — Pomerantz investigating claims citing **$42–43M charge-offs** [07-16]; **BayFirst** — *"elevated nonperforming loans, net charge-offs"* [07-17] | idiosyncratic, sub-$10B tier |

**This supports MACRO P2, and upgrades it.** P2's evidence was one asset class — HY OAS **2.69%** (−4bp
d/d, **6bp off its 365-day low**), IG **0.78%**, NFCI **−0.538** loosening three straight weeks [FRED,
asof 07-20 / 07-10]. The Q2 credit-cost lines are a **second, independent** evidence class saying the
same thing, and they come from the borrowers' balance sheets rather than the spread market. ⚠ **Two
honest limits.** (a) Provisions and NCOs are **lagging**: the Q2 window is Apr–Jun and cannot speak to
July. (b) COF's *level* — 3.4% total / 4.x% card — is high in absolute terms; only the direction is
benign, and CNBC's framing (*"good enough but didn't answer the big question"*) is recorded as such.
The exceptions are all at the sub-$10B-cap tier, i.e. **idiosyncratic, not systemic**. P2's own kill
line (HY OAS >3.10% on a close) is untouched.

---

## §4 · Valuation next to what the denominator is doing (live, 2026-07-22 pre-open)

30d = change in the **current-year (0y)** consensus EPS over 30 days; revisions = 0y up:down, 30 days.

| Name | Px | fwd P/E | ttm P/E | P/B | 0y EPS 30d Δ | 0y rev. | Px vs consensus target | Read |
|---|---|---|---|---|---|---|---|---|
| **GS** | 1085.56 | 14.80 | 16.29 | 2.96 | **59.49 → 70.64 = +18.8%** | **9↑ : 0↓** | −2.5% (tgt 1112.85) | ★ **the dislocation** — best revision book in the cohort, worst flow (−0.450) |
| **STT** | 183.30 | **12.02** | 16.18 | 2.11 | 12.48 → 13.57 = **+8.7%** | **4↑ : 0↓** (all 4 periods) | −6.9% (tgt 196.90) | cleanest long-side combination: rising denominator, falling multiple |
| **TRV** | 369.63 | 12.39 | 9.90 | 2.33 | 28.15 → 31.17 = **+10.7%** | 2↑ : 0↓ | **+9.7% ABOVE** (tgt 336.92) | ⚠ fwd EPS **29.83 vs ttm 37.33 = −20.1%**; +1y EPS **29.17 < 0y 31.17** — the Street models the cycle rolling |
| **CB** | 354.80 | 12.15 | 12.55 | 1.87 | 27.09 → 27.13 = **+0.1%** | 2↑ : 2↓ | −1.5% (tgt 360.30) | flow +0.822 on a **flat** estimate book |
| **USB** | 63.71 | **11.02** | 12.72 | 1.64 | 5.087 → 5.223 = +2.7% | 4↑ : 1↓ | −8.5% (tgt 69.66) | modest but positive on both axes |
| **JPM** | 345.23 | 14.00 | 14.79 | 2.60 | 22.39 → 24.07 = +7.5% | 4↑ : 1↓ | −6.0% (tgt 367.45) | revisions good, flow only +0.420 |
| **MET** | 93.37 | 8.50 | 18.06 | 2.21 | 9.899 → 9.885 = **−0.1%** (0q **−2.9%**) | 0q 1↑ : 2↓ | −2.7% (tgt 96.00) | rs60 +17.1 vs SPY on a **falling** near-term estimate |
| **PRU** | 118.59 | 8.15 | 12.21 | **1.29** | +0.3%; **+1y cut −4.1% over 90d** | +1y 3↑ : 4↓ | **+13.7% ABOVE** (tgt 104.27) | cheapest book value, weakest forward revision |
| **AON** | 359.40 | 16.81 | 19.73 | **7.81** | 19.118 → 19.103 = **−0.1%** | **1↑ : 3↓** (0q 1↑ : 5↓) | −8.6% (tgt 393.11) | the broker bid (rs20 +14.1 vs SPY) has **no** estimate support |
| **PYPL** | 55.85 | 9.71 | 10.48 | 2.49 | +0.06% | **0↑ : 3↓** (all 3 in 7d) | **+6.5% ABOVE** (tgt 52.42) | reconfirms [07-21 FIN] §4: M&A, not fundamentals |

★ **The single sharpest fact in this file: the market is paying up for names whose denominators are flat
(CB +0.1%, PYPL +0.06%, AON −0.1%) and selling the name whose denominator is rising fastest (GS +18.8%,
9↑:0↓).** GS's current-year multiple compressed from ~18.2x to **15.4x in 30 days on the earnings raise
alone.** That is the signature of a de-rate against an activity peak — not credit, not rates.
⚠ **And the sell-side is leaning against the OW's flagship**: *"Goldman Sachs downgraded Travelers to
Sell from Neutral, $350 target"* [07-20], with TRV's rating book moving to **3 sell + 2 strongSell** this
month from **0 sell + 3 strongSell** last month, while the stock trades **9.7% above** consensus target
and **0.6% below** its 52-week high.

---

## §5 · Value-chain nodes that CHANGED (rest carried by reference to [07-21 US_2] §4)

- **Node [3] Capital markets / IB — state change, from "confirming" to "confirming and de-rating."**
  Fundamentals still improving (GS 0y EPS +18.8%/30d, 9↑:0↓); price no longer paying for it (flow −0.450,
  rs20 −2.4 vs SPY). This node is now a **multiple event, not an earnings event.**
- **Node [2] Lending / NIM — the binding constraint was measured directly this run, and it loosened.**
  [07-21 US_2] §4 named credit quality as the binding fundamental constraint. §3 above is the first run
  where that constraint is read off printed credit-cost lines rather than off spreads. It is not binding
  yet. **Sub-node correction: the node's live expression is super-regionals (USB/PNC/FITB/HBAN), not
  money-centers.**
- **NEW node [7] Insurance brokerage (AON, AJG, MRSH).** Absent from the 07-21 map. Fee-on-premium, no
  float, no credit exposure — and therefore the cleanest test of whether the insurance bid is a rate
  trade (it is not, §2). Bid on price, unsupported by estimates (AON 0q 1↑:5↓).
- **★ The binding constraint of the *insurance* leg is now named and confirming against the leg:
  P&C / reinsurance pricing is softening** (Arch 07-17; WRB's own call 07-20; WRB Reinsurance & Monoline
  Excess loss ratio 57.7% vs 53.1% est). A softening rate environment caps the combined-ratio engine that
  §1 shows is the actual driver — **this, not the real-yield branch, is what most plausibly ends the P&C bid.**

---

## §6 · Track KPIs and anti-signals — dated observables

| Observable | State (dated) | Falsifier / confirmer |
|---|---|---|
| **P&C pricing cycle** ★ | Softening: Arch 07-17, WRB call 07-20, WRB reins. loss ratio 57.7% vs 53.1% est | **Confirmer:** a second carrier calls property/reinsurance pricing competitive by **07-31**. **Falsifier:** CB/TRV Q3 guide underlying CR flat-or-better |
| **TRV estimate cliff** | +1y EPS **29.17 < 0y 31.17 (−6.4%)**; fwd EPS 29.83 vs ttm 37.33 | **Falsifier:** +1y consensus revised above 0y. **Confirmer:** a second Sell-side downgrade after GS's 07-20 $350 |
| **GS dislocation** | 0y EPS +18.8%/30d, 9↑:0↓ **against** flow −0.450, rs20 −2.4 vs SPY | **Falsifier:** rs20 vs SPY crosses 0 while revisions hold → the de-rate was a post-print air pocket. **Confirmer:** revisions roll to net-down by **07-31** |
| **CB crowded short (new)** | FINRA z **+1.61 🔴**, 5v5 +14.8▲, asof 07-21 | z back below +1.0 within 3 sessions (by **07-24**) = spent, same test GS just passed |
| **07-21 anti-signals now SPENT** | GS z +1.59 → **−0.11**; STT z +1.50 → **−0.13** | Recorded as falsified, not carried forward |
| **Credit costs (P2)** | Provisions/NCOs down at KEY, TFC, MTB, WFC, USB, ALLY, UCB; exceptions FSUN/BayFirst, sub-$10B tier | **Kill:** HY OAS **>3.10%** on a close (now 2.69%), or NFCI positive-ward 2 weeks running (now −0.538) |
| **Rates frame (S9)** | real 10y **2.35%** (asof 07-20) **with breakeven 2.26%** (asof 07-21); 2s10s **+0.39**; 2y 4.21% | S9-A: real 10y <2.20% **with** breakeven rising. §2 finds this hits 0 of the 5 FIN greens cleanly — **the branch is bracketed but mis-aimed at this sector** |
| **Insurance-broker air pocket** | AON rs20 **+14.1** / AJG **+18.2** vs SPY on 0y revisions 1↑:3↓ | rs20 vs SPY crossing 0 with revisions still net-down = price was the whole story |
| Dated catalysts | FOMC **07-28~29**; next WTI COT **07-24**; V/MA fiscal-Q3 late July `[exact date blank]` | — |

---

## §7 · Dispersion (W5)

**Financials rs20 spread vs SPY = 44.4pp** (PYPL +31.4 to APO −13.0) against a **median name move of
+6.1** vs SPY — the spread is **7.3× the sector's own central move.** Excluding the PYPL special
situation it is still **31.2pp (AJG +18.2 to APO −13.0), ~5×.** rs60 spread vs SPY is **44.2pp**
(HOOD +21.7 to CME −22.5). Sub-leg flow spans **+0.697 (payments) to −0.151 (IB/brokerage)**, a 0.85-point
range around a sector mean of +0.357.

**"Financials" is the wrong unit of analysis this run**, and the failure is not marginal: the sector
number +0.357 describes no sub-leg in it. The analysable units are **(i) super-regional NIM**
(USB/PNC/FITB/HBAN — the actual steepener), **(ii) P&C underwriting into a softening pricing cycle**
(TRV/CB), **(iii) custody fee/NII on AUM levels** (STT/BNY), **(iv) an IB activity peak de-rating against
rising estimates** (GS/MS/IBKR), and **(v) two orphans** (PYPL M&A, C's genuine weakness). Any statement
made about "Financials" that does not name which of the five it means is not a measurement.

---

**EXIT CHECK:** ✅ Delta led (3 numbered, each with a measured number vs both prior files); value chain
and player table carried by reference · ✅ Q1 answered — three different variables, steepener correctly
expressed in super-regionals · ✅ Q2 answered with the concentration quantified: double-count is in the
rationale, not the exposure; failure mode relocated to sector-level UW expression · ✅ Q3 answered — P2
supported by a second evidence class, with the lag and level caveats stated and the sub-$10B exceptions
named · ✅ every rs number carries **vs SPY**; real 10y quoted **with** breakeven; every credit claim
cites HY OAS or NFCI; both halves cited where available and `[blank]` where not · ✅ dispersion stated
and the sector label rejected as the unit · ✅ zero buy/sell, zero sizing. **→ proceed.**
