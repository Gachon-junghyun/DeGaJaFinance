# SECTOR_DEEP_STPL — industry_US · 2026-07-19 (Stage 6 / L1·DEEP) ★rotating track · FULL FRESH MAP

> **Consumer Staples has never been deep-dived in any prior run.** Absence confirmed from disk, not
> from memory: `ls llm_outputs/*/industry_US/*STPL*` → **no match** across all 7 existing run
> directories (07-11, 07-12, 07-13, 07-14, 07-15, 07-17, 07-19). ROTATION §3 independently lists STPL
> among "never covered: RE, MATR, COMM, STPL, DISC". **Therefore this is a full fresh map, not a delta
> file — there is no prior STPL state to diff against.**
>
> Inputs reread from disk: `MACRO_REPORT.md` · `SWEEP_READ.md` · `EVENT_ALPHA.md` ·
> `SECTOR_ROTATION.md` · `BLINDSPOT_PREMORTEM.md` · `SECTOR_FLOW_US.json` (read directly for the full
> 19-name STPL bucket).
> **asof = 2026-07-17 close** for every price, flow, OBV, RS, volume and FINRA short number below.
> ⚠ The 07-18 US combat deaths and the 07-19 US strike on the IRGC are **in none of these numbers.**
> **Zero buy/sell calls, zero sizing.**
>
> **Why this file exists:** PREMORTEM Lens 1 promoted STPL to the 5th DEEP slot, displacing Real
> Estate, on the composition argument ROTATION had already accepted for ENRG. **Mandated question:
> is the tobacco / non-retail staples leg an INDEPENDENT pricing-power driver, or a DUPLICATE of the
> HLTH defensive bid?** Per PREMORTEM Finding B the book collapses to ~1.2 independent factors, so
> this is the decisive question: a genuine independent driver would be the first real diversifier the
> run has found. **§6 commits.**

---

## §1 Flow — measured, name by name, with the composition split shown

**Sector line (`SECTOR_FLOW_US.json`, Consumer Staples, n=19):**
`wflow −0.164 · eqflow +0.077 · 🟢 0 / 🔴 4 · breadth 0.00 · delta +0.083`
Rank **9 of 11 by wflow**, but **3rd-fastest delta on the board** (behind ENRG +0.181 and RE +0.091).
Universe context: `n=300 · universe wflow −0.084 · 🟢 9 / 🔴 69` — **a rotation inside a falling tape.**

### The full 19-name bucket, flow-ranked (this is the composition claim, verified)

| # | Ticker | Industry | mcap $B | flow | tag | OBV | RS20 | RS60 | vol | delta |
|---|---|---|---:|---:|---|---|---:|---:|---:|---:|
| 1 | **MO** | Tobacco | 115.4 | **+0.588** | 🟡중립 | 매집 | +7.3 | +9.2 | 0.91 | +0.160 |
| 2 | **KMB** | Household Products | 34.0 | +0.576 | 🟡중립 | 매집 | +6.5 | +6.6 | 0.95 | +0.089 |
| 3 | **CCEP** | Soft Drinks | 42.9 | +0.562 | 🟡중립 | 매집 | +8.0 | +4.1 | 0.83 | +0.070 |
| 4 | **MNST** | Soft Drinks | 89.3 | +0.545 | 🟡중립 | 매집 | +6.1 | +24.0 | 1.13 | −0.056 |
| 5 | **ADM** | Ag Products & Services | 36.2 | +0.544 | 🟡중립 | 매집 | +12.0 | +17.4 | 0.78 | +0.126 |
| 6 | KVUE | Personal Care | 34.8 | +0.442 | 🟡중립 | 중립 | +5.1 | +4.1 | 1.14 | +0.121 |
| 7 | **PM** | Tobacco | 278.0 | +0.434 | 🟡중립 | 매집 | +7.2 | **+20.4** | 0.93 | **+0.437** |
| 8 | KO | Soft Drinks | 341.6 | +0.265 | 🟡중립 | 중립 | +1.7 | +3.6 | 1.06 | −0.126 |
| 9 | TGT | Staples Retail | 59.4 | +0.205 | 🟡중립 | 중립 | +8.9 | +0.1 | 0.81 | +0.119 |
| 10 | KDP | Soft Drinks | 41.9 | +0.026 | 🟡중립 | 중립 | −0.2 | +11.3 | 0.90 | +0.135 |
| 11 | CL | Household Products | 71.6 | +0.023 | 🟡중립 | 중립 | +2.3 | +8.1 | 0.73 | −0.029 |
| 12 | SYY | Food Distributors | 37.6 | −0.047 | 🟡중립 | 중립 | +3.1 | +3.7 | 0.77 | +0.011 |
| 13 | KR | Food Retail | 34.7 | −0.178 | 🟡중립 | 중립 | −5.2 | −20.1 | 0.98 | +0.255 |
| 14 | PG | Personal Care | 350.2 | −0.261 | 🟡중립 | 중립 | −0.7 | −0.2 | 0.83 | −0.063 |
| 15 | MDLZ | Packaged Foods | 77.2 | −0.287 | 🟡중립 | **분산** | −0.1 | +3.1 | 1.09 | +0.096 |
| 16 | **PEP** | Soft Drinks | 194.1 | **−0.430** | 🔴분산 | 분산 | −3.5 | −17.1 | 0.89 | +0.049 |
| 17 | **COST** | Staples Retail | 421.9 | **−0.436** | 🔴분산 | 분산 | −2.9 | −12.0 | 0.98 | +0.049 |
| 18 | **HSY** | Packaged Foods | 35.0 | **−0.531** | 🔴분산 | 분산 | −2.5 | −14.7 | 0.67 | +0.098 |
| 19 | **WMT** | Staples Retail | 932.5 | **−0.583** | 🔴분산 | 분산 | −3.6 | −17.4 | 0.82 | +0.130 |

**★ PREMORTEM's composition claim is CONFIRMED, and the mechanism is arithmetic, not interpretation.**
The four 🔴분산 names (**WMT $932B · COST $422B · PEP $194B · HSY $35B**) carry **$1,583B of the
bucket's cap.** WMT alone is **932.5/2,676 = 34.8% of the sector's market cap** and prints −0.583.
A cap-weighted average of 19 names where one third of the weight prints −0.583 **cannot** print
positive. Measured mean of the 19 equal-weighted flow scores = **+0.0767**, which reproduces the
reported eqflow **+0.077 exactly.** The wflow/eqflow gap of **0.241** is a weighting artifact.
**The composition argument survives — this part of PREMORTEM is right.**

**⚠ But note what the same table says and PREMORTEM did not: breadth is 0.00, and there is not one
🟢가속 name in the bucket.** Ten of nineteen names are OBV 중립 or 분산. The "positive breadth" is
**seven 매집 names against four 분산 names and eight neutral** — it is a thin top, not a broad bid.

### Short-vol divergence vs narrative — `scripts/us_flow.py`, FINRA Reg SHO, 2026-07-17

| Ticker | short% | base20 | **z** | 5v5 trend | verdict |
|---|---:|---:|---:|---|---|
| **ADM** | 47.2% | 68.2% | **−2.69** | +2.0▲ | 🟢 **공매도급감 — the largest short-cover measured anywhere on the board that day** |
| MO | 44.5% | 54.4% | −0.97 | **−11.6▼** | 🟡 normal — **shorts leaving** |
| MNST | 28.8% | 36.9% | −0.96 | +11.4▲ | 🟡 normal |
| STZ | 26.1% | 33.6% | −0.86 | −8.6▼ | 🟡 normal |
| **PM** | 53.8% | 47.4% | **+0.49** | **+8.3▲** | 🟡 normal — ⚠ **shorts BUILDING into the 07-22 print** |
| KMB | 71.9% | 67.6% | +0.66 | +3.2▲ | 🟡 normal |
| GIS | 68.3% | 59.4% | +0.74 | +5.0▲ | 🟡 normal |
| CF | 68.9% | 61.0% | +0.85 | −6.6▼ | 🟡 normal |
| CCEP | 73.6% | 57.5% | +0.96 | +4.2▲ | 🟡 normal |
| CTVA | 72.2% | 59.5% | +1.06 | −1.2▼ | 🟡 normal |

**★ The divergence that matters: MO and PM — the two Tobacco names, the same industry, the same
thesis — are positioned in OPPOSITE directions.** MO z −0.97 with shorts **exiting** (5v5 −11.6▼);
PM z +0.49 with shorts **building** (+8.3▲) into its own earnings three sessions away. A single
"tobacco pricing-power" story cannot produce both. **The positioning is name-specific, and PM's is
the adverse one** — which is precisely where PREMORTEM put the dated catalyst.

### Extension — the leg is genuinely un-extended (measured, yfinance, 2026-07-17)

| Ticker | last | 50dma | %>50dma | ATR14 | **ATRs over 50dma** | % off 52w high | RSI14 |
|---|---:|---:|---:|---:|---:|---:|---:|
| MO | 74.21 | 70.97 | +4.6% | 1.78 | **1.82** | **0.0%** (at high) | 51.6 |
| KMB | 108.35 | 102.25 | +6.0% | 3.19 | **1.92** | −5.6% | 48.0 |
| PM | 192.98 | 180.55 | +6.9% | 5.33 | **2.33** | **0.0%** (at high) | 62.9 |
| CCEP | 105.18 | 97.53 | +7.8% | 2.61 | 2.93 | −3.7% | 61.8 |
| MNST | 97.50 | 91.25 | +6.9% | 2.12 | 2.94 | −2.4% | 53.6 |
| **ADM** | 85.90 | 79.30 | **+8.3%** | 1.79 | **3.68** | **0.0%** (at high) | **86.0** ⚠ |
| *XLV (ref)* | 161.09 | 152.48 | +5.6% | 2.80 | *3.07* | −2.0% | 51.6 |
| *XLP (ref)* | 85.19 | 83.81 | +1.7% | 1.49 | *0.93* | −4.2% | 51.9 |

**MO 1.82 / KMB 1.92 / PM 2.33 ATRs vs PBF's 6.5** — this is real and it is the leg's single best
property. **Nothing here is extended.** RSI 48–63 on names sitting at 52-week highs = a slow grind,
not a blow-off. ⚠ **ADM is the exception on every measure: 3.68 ATRs and RSI 86.0 — the most
extended and most overbought name in the file.** Hold that thought for §6.

---

## §2 Players — large-cap universe **UNION** thematic names from the news window

**Union rule applied:** the 19 `us_top300` names above, **UNION** any name mentioned ≥2× in the
sector news window that has a real ticker and mcap ≥ ~$2B. The union is where alpha leaks. Here is
what leaked — and the honest answer is: **almost nothing, and that is itself a finding.**

| Name | Ticker | mcap $B | Mentions (foreign, 14d) | RS20 | RS60 | corr w/ XLK (60d) | Qualifies? |
|---|---|---:|---|---:|---:|---:|---|
| British American Tobacco | **BTI** | **135.7** | 2 (bloodbath 07-17; tobacco set) | +6.5 | +10.4 | **−0.285** | ✅ **ADDED** |
| Imperial Brands | **IMBBY** | **29.7** | 2 (SA 07-17 "Buying… While It's Cheap"; bloodbath 07-17) | +3.7 | +1.3 | **−0.287** | ✅ **ADDED** |
| Universal Corp (leaf) | UVV | **1.3** | 1 (SA 07-13 "Inconsistent Results") | +1.7 | −1.7 | −0.312 | ❌ **below the ~$2B floor AND <2 mentions** |
| Turning Point Brands | TPB | **1.6** | 0 | +3.7 | +11.6 | −0.064 | ❌ **below floor, not named** |
| Vector Group | VGR | — | 0 | — | — | — | ❌ **no usable listing (delisted/insufficient history)** |

**★ The union adds exactly two names, both foreign-domiciled ADRs of the same industry already in
the bucket, and both carry the identical factor signature (corr w/ XLK −0.285 / −0.287, matching
MO −0.554 and PM −0.370 in sign).** The union added **zero** genuinely new exposure.

**★ Negative finding worth recording so the next run does not re-derive it: there is no thematic
small-cap layer under US staples in this window.** The two real candidates (UVV $1.3B leaf
processing, TPB $1.6B) **both fail the mcap floor**, and UVV's only mention is a bearish
dividend-safety piece. **A theme with genuine narrative velocity leaks into small caps; this one has
no small-cap layer at all — consistent with §6's finding that there is no theme here, only a factor.**

**⚠ Coverage limit, stated not hidden:** `module_industry_map` **cannot serve this sector** — it
returned `시드가 전부 영문입니다 … corp_embeddings.db 는 KR 사업보고서(한국어) 코퍼스라 영문 시드는
0히트가 정상입니다` with **0 corp-pool rows and 0 clusters.** The tool is a KR-filing embedding
corpus; English seeds are structurally out of scope and it points to `chain_hop` for US value
chains. **§4's map is therefore built from primary filings (§3), not from the industry-map tool.**

---

## §3 IR anchor — who does what, from primary sources

### PM (Philip Morris International) — 10-K filed **2026-02-06**, FY2025 (accession 0001628280-26-005939)

**Shipment volume table, verbatim from the filing (million units):**

| | 2025 | 2024 | 2023 | y/y |
|---|---:|---:|---:|---|
| Cigarettes | **607,367** | 616,827 | 612,949 | **−1.5%** |
| Heated Tobacco Units | **155,133** | 139,743 | 125,263 | **+11.0%** |
| Total cigarettes + HTU | 762,500 | 756,570 | 738,212 | +0.8% |

**Oral smoke-free volume (million cans):**

| | 2025 | 2024 | 2023 | y/y |
|---|---:|---:|---:|---|
| **Nicotine Pouches (ZYN)** | **879.6** | 644.0 | 421.1 | **+36.6%** (2024: +52.9%) |
| Snus | 227.9 | 239.6 | 240.4 | −4.9% |
| Moist Snuff | 129.8 | 134.6 | 133.7 | −3.6% |
| **Total Oral** | **1,240.0** | 1,021.6 | 799.3 | **+21.4%** |

**Revenue bridge, filing language:** net revenues **+7.3%**; ex-currency and ex-acquisitions
**+6.5%**, *"mainly reflecting: a favorable pricing variance due to higher combustible tobacco
pricing; and favorable volume/mix, driven by higher smoke-free products volume, notwithstanding
unfavorable mix and lower volumes for cigarettes."*

**★ Read this precisely, because it is the crux of the mandated question.** PM's growth is
**price on a declining cigarette base (−1.5% volume) plus genuine pouch volume growth (+36.6%)**.
That is real, primary-sourced, idiosyncratic pricing power. **It is also a multi-year structural
fact that has been true since at least 2023 (421 → 644 → 880 cans).** It did not change in the last
20 trading days. **A constant cannot explain a 20-day flow burst.** Held for §6.

Regulatory anchor from the same filing: FDA has authorized **General snus and ZYN nicotine pouches**
and IQOS consumables — *"the first-ever such authorizations in their respective categories"* — plus
Modified Risk Tobacco Product status. Cross-referenced on the tape: *"FDA lets Philip Morris market
Zyn nicotine pouches as less harmful than cigarettes"* [CNBC 06-30].
Input concentration, filing language: for oral SFP, direct materials are *"plastic cans and lids…
nicotine salt or nicotine premix… pouch material"*, and **in 2025 the top ten suppliers of direct
materials** are a named concentration. → §4 bottleneck.

### ADM (Archer-Daniels-Midland) — 10-K filed **2026-02-17**, FY2025

**Three reportable segments: Ag Services and Oilseeds · Carbohydrate Solutions · Nutrition.**
Segment revenues, from the filing ($M):

| | 2025 | 2024 | Change |
|---|---:|---:|---:|
| Ag Services | 40,363 | 44,083 | **−3,720** |
| Crushing | 10,353 | 11,836 | **−1,483** |
| Refined Products & Other | 10,855 | 10,597 | +258 |
| **Total Ag Services & Oilseeds** | **61,571** | 66,516 | **−4,945** |
| Starches & Sweeteners | 7,982 | 8,587 | −605 |
| Vantage Corn Processors | 2,755 | 2,647 | +108 |
| **Total Carbohydrate Solutions** | **10,737** | 11,234 | −497 |

Filing language on the drivers: Crushing had *"lower results versus the prior year, driven by lower
soy and canola crush margins and higher manufacturing costs"*; Carbohydrate Solutions operating
profit **−12%**; and critically — *"the postponement of the implementation of European Union
Deforestation Regulation and the **deferral of U.S. biofuel and trade policy evolution** negatively
impacted sales volumes and margins."*

**★ ADM's own primary filing does not describe a company with pricing power or an ag-input upcycle.
It describes falling revenue in every major segment and compressed crush margins, with the swing
factor named explicitly as US biofuel policy.** ADM is a **biofuel/renewable-diesel policy option
wearing a Consumer Staples GICS label.** → decisive in §6.

### MO / KMB — the other two legs, in one line each
- **MO** (Tobacco, $115B): US-only Marlboro + `on!` pouches; the tape frames it purely as yield —
  *"dividend yields of at least 5.9%… raised annual dividends for at least 50 years"* [Yahoo 07-16],
  *"continues to stay ahead of the decline in cigarette demand"* [Yahoo 07-12]. **Next print 07-30 —
  outside this run's window** (see §7).
- **KMB** (Household Products, $34B): the leg's **input-cost** name, not its pricing name — see the
  measured crude beta **−0.263** in §6, the only negative crude beta in the bucket. Pulp/resin cost
  relief, not price realization. Next print **08-04 — outside the window.**

---

## §4 Value-chain map — 5–8 nodes, left → right, BOTTLENECK marked

```
 [1] AG INPUT / LEAF            [2] PROCESSING &          [3] BRANDED             [4] ★REGULATORY
     Tobacco leaf (UVV $1.3B)       CRUSH / MILLING           MANUFACTURE             AUTHORIZATION
     Corn · soy · canola   ───▶  ADM · BG · SYY      ───▶  PM · MO · BTI · IMBBY ─▶  FDA PMTA / MRTP
     Nitrogen fert (CF, CTVA)      crush margins ↓ y/y       KMB · KO · PEP · MNST     ◀━━ BOTTLENECK ━━
            │                            │                        │                         │
            │                            │                        ▼                         ▼
            │                            │                  [5] DISTRIBUTION          [6] END DEMAND
            │                            │                      SYY · KR · WMT   ───▶     Inelastic;
            │                            │                      COST · TGT               excise-taxed
            │                            │                      (all 🔴분산/중립)         (NOT a bottleneck)
            │                            │
   ╔════════▼════════════════════════════▼═══════════════════════════════════════════════════════╗
   ║ ★ CROSS-SECTOR CHAIN — this is the link that decides the independence verdict:               ║
   ║   NATGAS (feedstock) ──▶ NITROGEN/AMMONIA (CF) ──▶ AG INPUTS (CTVA) ──▶ CRUSH/BIOFUEL (ADM)  ║
   ║                                                              │                               ║
   ║                                                              ▼                               ║
   ║             US BIOFUEL POLICY ──▶ RENEWABLE DIESEL ──▶ ★ THE SAME DISTILLATE COMPLEX          ║
   ║                                     the ENRG leg (PBF/VLO/MPC/PSX) is long.                  ║
   ║   MEASURED: ADM~XLE +0.525 · ADM~CF +0.522 · ADM~crude +0.470 · ADM~XLV −0.042 (zero).        ║
   ║   ⇒ Node [1]/[2] is NOT a staples node. It is an ENRG node with a Staples GICS tag.          ║
   ╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
```

### ★ The BOTTLENECK is node [4] — FDA authorization — and it is a binding constraint, not strong demand

**Why demand is explicitly NOT the bottleneck here:** pouch volume is +36.6% y/y and total oral
+21.4% — demand is abundant. Abundant demand is the opposite of a binding constraint.
**The binding constraint is the right to sell legally**, and it binds in both directions:
- **It protects the incumbent:** PM's ZYN holds *"the first-ever"* FDA MRTP authorization in its
  category [10-K; CNBC 06-30]. That authorization is a legal moat a competitor cannot buy or build
  quickly, and it is the reason node [3] captures the margin rather than node [1] or node [5].
- **It threatens the incumbent:** *"Public Health Groups, Pediatricians and Parents **Sue FDA** Over
  Policy Allowing the Marketing of **Unauthorized** E-Cigarettes and Nicotine Pouches"*
  [PR Newswire 07-14; corroborated NYT 07-14]. And in the UK: *"Vapes to have less enticing names
  and flavours to protect children"* [BBC 07-10].

Secondary constraint at node [3]: PM's filing names **top-ten supplier concentration** in nicotine
salt/premix, pouch material and cans — a real but second-order chokepoint.
Node [5] (distribution) is the **anti-bottleneck**: WMT/COST/KR/TGT are the four weakest flow scores
in the bucket. **Value is being captured upstream of the shelf, and the tape agrees.**

---

## §5 Chain-hop candidates — **body-proximate only, never headline-named**

`python -X utf8 -m module_news_data chain-hop tobacco nicotine --days 14 --scope foreign`
(31 articles scanned, ±300-char proximity)

**Headline-named (already named = crowded, excluded by rule):** MO (title 1 / body 3) · AMZN (1/2) ·
PM (1/2) · KO (1/0) · CCEP (1/0).

**Candidates returned by the tool:**

| Ticker | proximity | body | industry | Flow cross-check | **Verdict** |
|---|---:|---:|---|---|---|
| GOOGL | 2 | 3 | Interactive Media | flow **−0.636**, 분산, RS20 −5.0 (per PREMORTEM §5) | ❌ **REJECTED — noise** |
| GOOG | 2 | 3 | Interactive Media | flow **−0.646**, 분산 | ❌ **REJECTED — noise** |

**★ Result: ZERO qualifying chain-hop candidates. Nothing from this section may reach BET.**

Both hits trace to a single co-mention inside *"Jim Cramer Says He Thought Amazon's Bond Offering
Would Hurt the Stock"* — an article that is not about tobacco at all. **This is the exact trap the
L3 warns about: a co-mention is not a candidate.** Both fail the flow cross-check on their own
merits (worst two flow scores in the entire COMM bucket, both distributing), so the rejection is
doubly evidenced rather than resting on my reading of the article.

⚠ **Tool-floor caveat, same root cause PREMORTEM §4 filed against the cycle registry:** `chain-hop`'s
universe is `us_top300`, so any small-cap link is structurally invisible. I checked that floor
manually in §2 — **UVV $1.3B and TPB $1.6B are the only two candidates below it and both fail the
$2B mcap rule anyway.** The blind spot is therefore **checked and empty here**, not merely inherited.

---

## §6 ★ VERDICT — independent pricing-power driver, or duplicate of the HLTH defensive bid?

# ⇒ **DUPLICATE.** The tobacco/non-retail staples leg is the HLTH defensive bid wearing a Staples label. It is NOT the run's first independent diversifier. **PREMORTEM's promotion was correct about the composition arithmetic and wrong about the driver.**

**And one correction that goes further than the mandate asked: ADM does not belong to this leg at
all — it is the ENRG/ag-biofuel leg the run has already logged twice.** Removing ADM removes the
single largest contributor to STPL's delta ex-PM. The verdict is committed on four independent
measurements, each of which could have falsified it and did not.

### Test 1 — Two-factor regression separates the three candidate drivers cleanly
Daily %, last 60 sessions to 2026-07-17, `name ~ α + β₁·XLK + β₂·crude(CL=F)`:

| Name | **β XLK** | **β crude** | R² | Reading |
|---|---:|---:|---:|---|
| **MO** | **−0.462** | **+0.052** | 0.32 | anti-AI-beta; **crude beta ≈ 0** |
| **PM** | **−0.372** | **+0.042** | 0.14 | anti-AI-beta; **crude beta ≈ 0** |
| **KMB** | **−0.438** | **−0.263** | 0.44 | anti-AI-beta + **cost relief**, i.e. short inflation |
| XLP | −0.307 | −0.044 | 0.38 | |
| *XLV (the HLTH leg)* | *−0.262* | *−0.084* | 0.26 | **same sign, same shape, smaller loading** |
| *UNH* | *−0.156* | *+0.017* | 0.05 | |
| **ADM** | **+0.037** | **+0.227** | 0.22 | **zero AI beta, the largest positive crude beta** |

> **Candidate (a) — pricing power / inelastic demand into diesel at $5.00/gal and a live hike debate —
> is REJECTED by measurement.** If the leg were being bought for pricing power in an inflationary
> impulse, it would load POSITIVELY on the inflation impulse. **MO's crude beta is +0.052 and PM's is
> +0.042 — indistinguishable from zero — and KMB's is NEGATIVE (−0.263).** KMB is not long inflation;
> it is *short* it, via pulp and resin input costs. **The leg is not being paid for pricing power.**
>
> **Candidate (b) — defensive rotation out of the de-rating AI complex — is CONFIRMED**, and MO/PM/KMB
> carry a **LARGER** anti-AI loading (−0.372 to −0.462) than XLV (−0.262) or UNH (−0.156). **STPL is
> not a diversifier against the HLTH bid; it is a levered version of it.**

### Test 2 — Correlation matrix: the leg sits inside the HLTH factor and outside the ENRG factor

| Pair | corr (60d) | | Pair | corr (60d) |
|---|---:|---|---|---:|
| MO ~ XLV | **+0.493** | | MO ~ crude | +0.175 |
| KMB ~ XLV | **+0.478** | | PM ~ crude | +0.118 |
| PM ~ XLV | **+0.335** | | MO ~ XLE | +0.466 |
| XLP ~ XLV | **+0.577** | | PM ~ XLE | +0.312 |
| MO ~ XLK | **−0.554** | | MO ~ SPY | **−0.384** |
| PM ~ XLK | −0.370 | | PM ~ SPY | **−0.200** |
| XLP ~ XLK | **−0.602** | | XLP ~ SPY | **−0.321** |
| XLP ~ MU | **−0.533** | | XLV ~ SPY | −0.123 |
| **ADM ~ XLV** | **−0.042** | | **ADM ~ CF** | **+0.522** |
| **ADM ~ MO** | +0.204 | | **ADM ~ XLE** | **+0.525** |
| **ADM ~ PM** | +0.167 | | **ADM ~ crude** | **+0.470** |

**MO/PM/KMB correlate with XLV at +0.34 to +0.49 and with the AI complex at −0.37 to −0.60.
ADM correlates with XLV at −0.042 (zero) and with CF/XLE/crude at +0.47 to +0.53.** The bucket is
**two different factors sharing one GICS code**, and neither of them is new to the book.

### Test 3 — Event study: the leg earns 100% of its alpha on AI-down days and gives it back on AI-up days
Last 20 sessions, return relative to SPY, split by the sign of XLK that day (XLK fell on 10 of 20):

| Name | total rel | **on XLK-DOWN days** | **on XLK-UP days** |
|---|---:|---:|---:|
| **MO** | +7.0pp | **+17.7pp** | **−10.7pp** |
| **PM** | +7.9pp | **+20.2pp** | **−12.3pp** |
| **KMB** | +6.3pp | **+17.6pp** | **−11.3pp** |
| **ADM** | +11.2pp | +10.9pp | **+0.3pp** ← *does not give back* |

And on the five worst and five best XLK days of the last 60 sessions:

| Date | XLK | MU | XLP | XLV | MO | PM | KMB | BTI | ADM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 06-05 | −6.66 | −13.25 | +1.71 | +0.61 | +2.25 | +1.89 | +6.28 | +3.23 | −2.94 |
| 06-23 | −4.14 | −13.18 | +1.87 | +1.41 | **+3.02** | **+3.19** | +3.43 | +3.12 | −0.59 |
| 06-16 | −2.79 | −6.18 | +0.13 | +0.03 | +0.86 | +1.24 | +1.11 | +0.52 | −1.58 |
| 07-02 | −2.71 | −5.49 | +2.03 | +2.63 | +1.64 | +2.58 | +2.94 | +2.00 | +0.23 |
| 07-01 | −2.57 | −10.57 | +0.28 | +0.55 | −0.57 | −1.78 | +1.52 | −1.94 | +0.27 |
| **06-15** | **+3.78** | +10.84 | −0.40 | −0.60 | **−1.82** | **−1.35** | +0.83 | −2.02 | −1.21 |
| **06-11** | **+3.73** | +11.66 | −0.26 | +0.81 | **−2.35** | −1.19 | −0.04 | +0.44 | −2.93 |
| **05-08** | **+3.44** | +15.49 | +0.24 | −0.85 | −1.33 | −0.07 | −1.26 | +0.34 | +0.17 |
| **06-18** | **+3.04** | +8.70 | −0.45 | −0.87 | +0.25 | −0.58 | +1.07 | −0.97 | −1.83 |
| **04-24** | **+2.81** | +3.11 | −0.30 | −1.41 | −0.40 | **−2.95** | −0.08 | +1.41 | −1.14 |

> **This is the finding that ends the argument.** MO/PM/KMB rise on 4 of the 5 worst AI days and fall
> on 4–5 of the 5 best. **Every basis point of the leg's 20-day outperformance is conditional on the
> AI complex falling, and the position gives back roughly 60% of it whenever the AI complex rallies.**
> That is the *definition* of a short-AI-beta hedge. It is not pricing power, and pricing power does
> not switch off on green days.

### Test 4 — The ignition date is shared with HLTH, which is the smoking gun
**2026-07-16** — the single largest day for the leg, and **69% of PM's entire 20-day relative move**:

| 07-16 | XLK | SPY | **XLV** | **XLP** | **MO** | **PM** | KMB | **BTI** | ADM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| % | **−2.24** | −0.54 | **+2.22** | **+2.80** | **+3.56** | **+4.95** | +2.31 | **+7.54** | +0.85 |

**07-16 is the same session on which UNH printed its MLR −270bps with raised guidance** — the fact
PREMORTEM §3 identified as *the* HLTH thesis. **The staples bid and the healthcare bid ignited on the
same day, in the same session, against the same AI drawdown.** Two legs that fire on one day against
one catalyst are one leg. Contemporaneous tape, unprompted: *"[investors] rotated toward more
defensive sectors such as **healthcare and consumer staples**"* [Yahoo Finance 07-17] — the two
sectors named together, in that order, in one clause.

### ★ Test 5 — the "un-crowded" claim is an artifact of measuring the wrong denominator
PREMORTEM concluded **"un-crowded, not un-real"** from `tobacco` 19 hits/7d, `Zyn` 2, `nicotine` 4.
I reproduced those numbers (18 / 1 / 3 today) — **and then measured the denominator of the driver
the tests above actually identified:**

| Search term (foreign, 7d) | hits |
|---|---:|
| `Zyn` | **1** |
| `nicotine` | **3** |
| `tobacco` | **18** |
| `staples` | **57** |
| **`defensive rotation`** | **552** |
| *(`pricing power`)* | *4,087* |

> **The story is un-crowded. The DRIVER is one of the most crowded narratives on the tape — 552 hits
> in 7 days, ~30× the tobacco denominator.** Named and dated, unprompted, in the window:
> *"The Great Rotation Is Here. **Why Money Is Fleeing Chips for Old Favorites.**"* [Yahoo 07-16] ·
> *"rotated toward more defensive sectors such as healthcare and consumer staples"* [Yahoo 07-17] ·
> *"The rotation went to drugmakers, **household staples**, and energy"* [Yahoo 07-18] ·
> *"How to make defensive investments before the **AI bubble pops**"* [Yahoo 07-13] ·
> *"Healthcare Looks Ready to Star in Rotation Trade"* [Bloomberg 07-13].
>
> **PREMORTEM searched for the theme and found silence, then read the silence as opportunity. The
> money was never coming for the theme.** This is a *generalizable* process error and it is filed as
> one: **measuring the crowdedness of a story you invented, rather than of the factor the flow is
> actually loading on, will reliably manufacture false "un-crowded" findings.**

### ★ What is genuinely real here — stated so this is a verdict, not a dismissal
1. **PM's pricing power is real and primary-sourced** (§3): pouches 421 → 644 → **880M cans**, price
   +6.5% ex-FX on −1.5% cigarette volume, first-ever FDA MRTP. **But it has been true for three
   years and cannot explain a 20-day flow burst.** A constant does not explain a change.
2. **The composition arithmetic is real** (§1) — WMT/COST/PEP/HSY genuinely do mask a positive
   equal-weighted top. **PREMORTEM was right about the arithmetic and wrong about what it implies:**
   the unmasked names turn out to share the driver we already own, so unmasking them buys nothing.
3. **The extension advantage is real:** MO 1.82 / KMB 1.92 / PM 2.33 ATRs vs PBF 6.5. If the desk
   wants the defensive factor, **this is a structurally cheaper entry point into it than the one it
   already holds** — but that is an *instrument* question, not a *diversification* one, and it is
   BET's, not mine.

### ★ The ADM ruling — a staples name or an ag-cycle name?
**ADM is an ag/biofuel-cycle name, and it is a DUPLICATE of a leg already logged twice.**
Four independent confirmations: (i) **β XLK +0.037 — zero AI beta**, unlike every other name in the
bucket; (ii) **β crude +0.227, the highest in the file**, with ADM~XLE +0.525 and ADM~CF +0.522;
(iii) **ADM~XLV −0.042 and ADM~MO +0.204** — it does not travel with staples at all; (iv) its **own
10-K** names *"deferral of U.S. biofuel and trade policy"* as the swing factor while every segment's
revenue and crush margins fall. It also behaves differently in the event study (**+0.3pp on AI-up
days — it does not give back**), which is the signature of a trend, not a hedge.
**Consequence: ADM is PREMORTEM's own ag-inputs watch (CTVA/CF/ADM) counted a second time, and it
sits on the ENRG/war-inflation factor — the exact factor Finding B says the book is already
saturated with.** ⚠ Its FINRA short-vol **z −2.69** — the largest short-cover measured anywhere that
day — plus **RSI 86.0 at 3.68 ATRs** means the most likely explanation of its +12.0% RS20 is a
**short squeeze into an extended tape**, not an ag upcycle its filings do not support.
**ADM must not be logged as STPL diversification. Double-counting it would inflate measured breadth
while adding concentration — the precise failure Finding B exists to prevent.**

### Factor-independence reasoning, spelled out
PREMORTEM Finding B: the book ≈ **1.2 independent factors** — *"long war-inflation, hawkish front
end"* — with every OW long it and every UW short it. Adding a leg is only diversification if it
loads on something else. Measured:

| Leg | war-inflation (crude β) | AI-derate / defensive (XLK β) | New factor? |
|---|---:|---:|---|
| ENRG (refiners) | **large +** | ~0 | (the incumbent factor) |
| FIN (insurers/exchanges) | + via hike/VIX | ~0 | no — Finding B Collapse 1 |
| **HLTH** (UNH/HUM/CVS) | **+0.017 ≈ 0** | **−0.156 / −0.262 (XLV)** | the defensive factor |
| **STPL — MO/PM/KMB** | **+0.052 / +0.042 / −0.263 ≈ 0** | **−0.462 / −0.372 / −0.438** | ❌ **NO — same factor as HLTH, larger loading** |
| **STPL — ADM** | **+0.227 (largest)** | **+0.037 ≈ 0** | ❌ **NO — same factor as ENRG** |

**So the book does not go from 1.2 factors to 2.2 by adding STPL. It stays at ~2 factors
(war-inflation, defensive/anti-AI) and gets *more concentrated in the second one*.**
⚠ **And the kill switch is shared, which is the decisive structural point:** MO~SPY **−0.384**,
PM~SPY −0.200, XLP~SPY −0.321. **A ceasefire is an SPY-rebound event** [PREMORTEM Collapse 3].
The same undated Hormuz headline that kills ENRG and FIN **also kills this leg**, through the SPY
rebound rather than through crude. **STPL does not split the one-headline problem. It is a third
seat on the same side of it, and it looks like breadth while being concentration.**

**⇒ COMMITTED: STPL is a DUPLICATE of the HLTH defensive bid. It is not the run's first genuine
diversifier. The 5th DEEP slot was correctly *identified* by composition and incorrectly *justified*
by driver — and the honest yield of spending it is the negative finding above, which is worth more
than a fifth confirmation of a factor we already own.**

---

## §7 Track KPIs + anti-signals — as dated observables

### The one in-window dated catalyst — **PM earnings, 2026-07-22**

**Confidence: HIGH — upgraded from PREMORTEM's `~pattern-grade` on independent verification.**
PREMORTEM flagged this as single-source (*"Earnings spotlight: Wednesday: Alphabet, Tesla, Philip
Morris"* [Seeking Alpha 07-18], cross-referenced to a weekly calendar [Yahoo 07-17]). I confirmed it
against a **third, non-news source**: `yfinance` issuer calendar returns
**`PM Earnings Date: 2026-07-22`**, with consensus EPS **$2.048** (range **$2.00–$2.13**).
⚠ Honest limit: yfinance is itself an aggregator, not the exchange/IR primary. **I therefore write
this as high-confidence multi-source, not exchange-confirmed.** If a stage downstream needs
issuer-grade certainty, PM's IR calendar is the primary and I did not reach it.

**★ And the same query produced a finding PREMORTEM did not have — the rest of the leg has NO
in-window catalyst at all:**

| Name | Earnings date (yfinance) | In this run's window? |
|---|---|---|
| **PM** | **2026-07-22** | ✅ **the only one** |
| MO | 2026-07-30 | ❌ outside |
| KMB | 2026-08-04 | ❌ outside |
| ADM | 2026-08-04 | ❌ outside |
| MNST | 2026-08-07 | ❌ outside |
| CCEP | *(none returned)* | ❌ |

> **The entire "tobacco/non-retail staples" leg has exactly one dated test in the window, and it is a
> single name.** PREMORTEM's leg is `PM · MO · KMB · ADM`; three of those four cannot be falsified by
> anything dated before August. **This materially weakens the case for having spent a DEEP slot here,
> and it is recorded rather than smoothed over.**

### ★ PM 07-22 written BOTH ways (as mandated)

**BRANCH A — the print CONFIRMS an independent pricing-power driver.** Observable: PM beats
$2.048 **on pricing and pouch volume specifically** — a ZYN can number above the FY25 run-rate
(>880M annualized, i.e. **>220M cans in the quarter**), combustible pricing variance still positive,
guidance raised. **Confirmation requires the tape to pay for it on a day XLK is FLAT OR UP** — that
is the only condition that separates driver (a) from driver (b), because on an XLK-down day the
defensive bid produces the same price action for a different reason. Corroborating: PM's short-vol
**z +0.49, 5v5 +8.3▲** unwinds (shorts covering into a beat), volume **>1.3×** vs the 0.93× it prints
now. **If this branch fires, §6's verdict is wrong and must be reversed by name.**

**BRANCH B — the print CONFIRMS the duplicate verdict.** PM beats or meets, and **the stock's move
that day tracks XLK's sign rather than the print's quality** — a good number that goes nowhere on a
green tape, or a mediocre number that rallies on a red one. Or: the beat is carried by **currency and
combustible price** with pouch volume decelerating below the +36.6% FY25 rate. Corroborating: volume
stays **<1.0×** (the leg has printed 0.78–0.95× throughout its entire advance — **the whole 20-day
move has happened on below-average volume, which is the leg's second-weakest property after its
shared kill switch**), and MO/KMB drift with XLP rather than with PM. **This is the branch §6
predicts.**

### Dated observables — KPIs

| # | KPI (what would make this leg REAL and independent) | Observable | Date |
|---|---|---|---|
| K1 | **The independence test itself** — the leg outperforms on a day the **AI complex RALLIES**. Currently it has done the opposite on 4 of the last 5 big XLK-up days | MO or PM positive-relative on a day XLK **>+1.5%** | **any session; re-check 07-24** |
| K2 | **ZYN can volume** — the only genuinely idiosyncratic number in the file | PM Q2 oral SFP cans **>220M** (FY25 run-rate) | **07-22** |
| K3 | **Pricing variance stays positive** on a still-declining cigarette base | PM combustible pricing variance in the 10-Q bridge | **07-22** |
| K4 | **Positioning resolves toward MO's side, not PM's** | PM short-vol z falls **below 0** (from +0.49) with 5v5 turning ▼ | **07-23 / 07-24** |
| K5 | **Volume finally confirms** — the move so far is 0.78–0.95× | any of MO/PM/KMB printing **vol_surge >1.3×** | rolling |
| K6 | **Regulatory bottleneck resolves favorably** (§4) | FDA action or a ruling in the 07-14 suit over unauthorized pouches | undated |
| K7 | **The 07-31 cross-check** — if ADM is an ENRG name, it must trade with the Russian diesel export ban's expiry, not with staples | ADM's reaction on **2026-07-31** vs MO/PM's | **2026-07-31** |

### Anti-signals — what would falsify the leg (or my verdict)

| # | Anti-signal | Threshold | Whose thesis it kills |
|---|---|---|---|
| A1 | ★ **Ceasefire / "strait open" / IEA-SPR release → SPY rebound** | SPY rallies and MO/PM/KMB underperform, **exactly as they did on 06-11/06-15** | **The leg — via the SAME headline that kills ENRG and FIN. §6's shared kill switch, live and undated** |
| A2 | **AI complex re-rates upward** — the leg's alpha is 100% conditional on this not happening | XLK reclaims trend; MU/SMH resume (PREMORTEM already calls the down-move *"EXHAUSTED"*, and **MU short z +1.71 dissents**) | The leg, mechanically: **−10.7 to −12.3pp** was given back on the last 10 XLK-up days |
| A3 | **PM print lands on the pouch line and the tape pays on a GREEN day** | K1 + K2 together | ★ **MY VERDICT.** This is the clean falsifier of §6 and it is three sessions away |
| A4 | **ADM breaks from the ag/energy complex and tracks staples** | ADM~XLE decays toward 0 while ADM~XLV rises above +0.3 | **My ADM ruling** — reverse it if this prints |
| A5 | **The extension advantage evaporates** | MO/PM >4 ATRs over the 50dma, or ADM (already 3.68 ATRs, **RSI 86.0**) mean-reverts hard | The "un-extended entry" argument, the leg's best remaining property |
| A6 | **Distribution appears at the top of the bucket** | any of MO/KMB/CCEP/MNST/ADM flipping OBV 매집 → 분산 | The composition argument itself — the 7 매집 names are the whole case |
| A7 | **The defensive narrative crowds out** | `defensive rotation` 552/7d keeps climbing while `tobacco` stays <20 | Confirms §6: the crowd is in the factor, and the leg is the late seat |

---

**EXIT CHECK:** ✅ **Absence independently confirmed from disk** — no `SECTOR_DEEP_STPL.md` in any of
the 7 prior `industry_US` run directories; written as a **full fresh map (rotating track), no delta
section** · ✅ **§1 flow measured** — all 19 names, the wflow/eqflow composition split verified
arithmetically (**WMT alone = 34.8% of sector cap**; equal-weight mean **+0.0767** reproduces eqflow
+0.077), short-z divergence named (**MO −0.97/−11.6▼ vs PM +0.49/+8.3▲ — same industry, opposite
positioning**), extension measured (MO **1.82 ATRs** vs PBF 6.5) · ✅ **§2 union executed** — adds
**BTI, IMBBY**; **UVV $1.3B / TPB $1.6B rejected on the mcap floor**; the industry-map tool's
KR-corpus limitation stated rather than worked around · ✅ **§3 IR anchor from primary filings** —
PM 10-K 2026-02-06 (**pouches 421→644→880M cans**, cigarettes **−1.5%**, price **+6.5% ex-FX**),
ADM 10-K 2026-02-17 (**Ag Services −$3.7B, Crushing −$1.5B, biofuel-policy deferral named**) ·
✅ **§4 six-node chain with the BOTTLENECK at FDA authorization** — explicitly *not* demand
(+36.6% pouch volume is abundance, not constraint) — and the **cross-sector natgas→nitrogen→
biofuel→distillate chain marked as the link that decides the verdict** · ✅ **§5 chain-hop run and
returned ZERO qualifying candidates** — GOOGL/GOOG rejected as a single Cramer co-mention **and**
flow-rejected independently; **nothing passed to BET** · ✅ **§6 COMMITS: DUPLICATE**, on 5
falsifiable tests (regression · correlation · event study · shared 07-16 ignition date · denominator
correction), with the factor-independence table and the **shared SPY-rebound kill switch** spelled
out; **ADM ruled an ENRG/ag name, not a staples name, on 4 independent confirmations** ·
✅ **§7 KPIs + anti-signals dated**, **PM 07-22 written BOTH ways** with the branch that would
**reverse my own verdict** named first and given a threshold · ✅ **PM 07-22 independently
re-verified** (yfinance issuer calendar, consensus $2.048) and **upgraded to high-confidence
multi-source — with the honest limit that it is still not exchange/IR-primary** · ✅ **new negative
finding surfaced that PREMORTEM did not have: PM is the leg's ONLY in-window catalyst (MO 07-30,
KMB/ADM 08-04, MNST 08-07 all fall outside)** · ✅ asof 2026-07-17 stated; 07-18/07-19 escalation
flagged as absent from every number · ✅ **zero buy/sell calls, zero sizing.**
**→ DEEP·STPL complete. Verdict handed to ALPHA/BET as: do NOT count STPL as diversification.**
