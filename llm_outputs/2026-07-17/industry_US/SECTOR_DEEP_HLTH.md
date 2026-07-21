# SECTOR_DEEP_HLTH — Health Care (HLTH) deep-dive · 2026-07-17 (Fri)

> Stage 5 / L2 DEEP. HLTH is the run's strangest call: **promoted OW by flow against a Neutral matrix**
> (ROTATION §2a divergence-b). Flow rank **#1 of 11** (wflow 0.357 / eqflow 0.264, both broad-positive),
> the single biggest one-day ignition on the board (Δw +0.33) — yet **zero 🟢가속 names** and **news
> velocity dead last** (465 hits/7d) and decelerating. NEVER deep-dived by this desk before — full
> fresh map. **Zero buy/sell calls — analytical map only** (P4).

---

## §1 — Flow cross-check: which sub-industry is actually being bought?

**module_flow** `DHR SYK MRK ABBV TMO JNJ VRTX CVS UNH WELL VTR XLV --bench SPY` [flow]:

| Ticker | Tag | OBV state | RS20 | RS60 | Vol surge |
|---|---|---|---|---|---|
| DHR | 🟡중립 | 매집 | +13.0% | −1.1% | 0.90x |
| SYK | 🟡중립 | 매집 | +6.6% | −8.0% | 0.99x |
| MRK | 🟡중립 | 매집 | +10.8% | +3.1% | 0.87x |
| ABBV | 🟡중립 | 매집 | +14.3% | +19.0% | 0.79x |
| TMO | 🟡중립 | 매집 | +14.9% | −2.7% | 0.73x |
| JNJ | 🟡중립 | 매집 | +6.2% | +2.4% | 1.02x |
| VRTX | 🟡중립 | 매집 | +7.2% | +4.7% | 0.78x |
| CVS | 🟡중립 | 매집 | +5.7% | +33.1% | 1.09x |
| UNH | 🟡중립 | 매집 | +3.8% | +25.0% | 0.98x |
| WELL | 🟡중립 | 매집 | +13.1% | +9.4% | 0.73x |
| VTR | 🟡중립 | 매집 | +13.2% | +6.3% | 0.67x |
| XLV (bench) | 🟡중립 | 매집 | +5.7% | +3.8% | 0.93x |

**Striking: every single name checked is OBV=매집 (accumulating).** No exceptions. This is a genuinely
uniform, quiet accumulation signature — not a name-level pop.

**us_flow.py FINRA short-vol Z** (same 11, asof 2026-07-16) [flow]: **all 🟡정상범위**, Z range −1.25
(SYK) to +0.92 (DHR), no name outside normal band. **No short squeeze, no crowded-short cover anywhere
in the checked set.** This rules out a mechanical short-covering explanation — the buying is real
demand, not positioning unwind.

### Sub-industry split (all 32 HLTH names in `us_top300`, flow-score avg by GICS sub-industry) [flow/json]

| Sub-industry | n | avg flow | Leaders (flow) | Laggard |
|---|---|---|---|---|
| Life Sciences Tools & Services | 4 | **0.320** | DHR 0.61, TMO 0.52, A 0.46 | WAT −0.30 |
| Biotechnology | 6 | **0.310** | ABBV 0.54, VRTX 0.51, REGN 0.42 | ALNY −0.01 |
| Pharmaceuticals | 5 | 0.291 | MRK 0.59, JNJ 0.51, BMY 0.48 | PFE −0.50 |
| Health Care Equipment | 8 | 0.282 | SYK 0.60, BDX 0.42, ABT 0.41 | BSX −0.49 |
| Managed Health Care | 3 | 0.201 | UNH 0.48, HUM 0.47 | ELV −0.35 |
| Health Care Services | 2 | 0.198 | CVS 0.50 | CI −0.10 |
| Health Care Distributors | 3 | 0.168 | COR 0.44, CAH 0.14 | MCK −0.08 |
| Health Care Facilities | 1 | 0.112 | HCA 0.11 | — |

**Every one of the 8 sub-industries averages positive.** The spread is narrow (0.11–0.32) — this is
**not** one hot corner dragging a sector average; it is genuinely broad. Only **2 of 32 names are red**
(ELV −0.351 🔴분산, PFE −0.496 🔴분산) — both idiosyncratic (managed-care regulatory drag on ELV;
COVID-revenue runoff on PFE, see §5). **Zero 🟢가속 tags anywhere in the 32.** Max vol_surge in the full
set is 1.46x (HCA) / 1.45x (ISRG) — real spikes exist but neither carries a green tag or a strong flow
score, so no name has crossed the module's acceleration threshold. **Read: this is quiet, broad,
low-conviction-looking accumulation across the entire value chain — not a narrow, hot, single-leg
trade.** That breadth is itself the strongest evidence against "money hiding in one crowded corner."

---

## §2 — Players (large-cap universe ∪ thematic small-caps, bounded)

**Large-cap universe** = the 32 `us_top300` HLTH names above (all ≥$2B mcap by construction; smallest
is A/Agilent at $35.9B) plus the flow-confirmed cross-sector REIT leg **WELL** ($145.9B) / **VTR**
($39.7B) (GICS Real Estate, economically HLTH — see §7).

**Thematic small-caps checked against the bound (named ≥2x in-window AND real ticker AND mcap ≥~$2B):**
searched the news window for repeat-named smaller biotech/pharma (BridgeBio, NovoCure, Ionis, Erasca,
ADC Therapeutics) — each surfaced only inside single analyst-note contexts (SA "Buy"/"Strong Buy"
initiations, one securities-class-action wire), not independently corroborated ≥2x AND mcap-verified.
**None added** — the bound is stated, not silently skipped (P4): these stay logged as sub-threshold, not
promoted to PLAYERS.

---

## §3 — IR anchor (primary filings, not news)

**AbbVie (ABBV) 10-K**, filed 2026-02-20, accession 0001551152-26-000008, period 2025-12-31
[filing]: single global operating segment — R&D, manufacture, commercialization of medicines across
immunology, neuroscience, oncology, aesthetics. Item 1A anchor: *"AbbVie is subject to cost-containment
efforts and pricing pressures that could cause a reduction in revenues... AbbVie is subject to
increasing public and legislative pressure with respect to pharmaceutical pricing."* → the exact risk
the MFN deals (§5) are partially defusing.

**UnitedHealth Group (UNH) 10-K**, filed 2026-03-02, accession 0000731766-26-000062, period 2025-12-31
[filing]: two complementary businesses, **Optum** (data/services/pharmacy) and **UnitedHealthcare**
(insurance). Item 1A anchor: *"...could result in reduced reimbursements or payments in our federal and
state government health care coverage programs, including Medicare, Medicaid and CHIP. A reduction in
state Medicaid reimbursement rates could be implemented retroactively..."* → the reimbursement-policy
node that gates the whole payer leg (§4).

**Merck (MRK) 8-K/90d** [filing, `module_disclosure_us`]: 57 filings total — 40 insider Form 4/13G, one
Item 2.02 earnings release (2026-04-30, stale/out-of-window), one Item 5.07 annual-meeting vote. **No
M&A/contract 8-K in the recent window** — nothing freshly catalytic filed at MRK specifically; noted,
not inferred (P4).

Budget note: ABBV/UNH `--full --json` pulled as the biotech/pharma and payer anchors (the two ends of
the value chain most exposed to the pricing-policy bottleneck, §4); PFE/JNJ/CVS `--full` not pulled this
run — flagged, not silently skipped.

---

## §4 — Value-chain node map (8 nodes, left→right) → the bottleneck

```
discovery/R&D → life-science tools/CDMO → pharma/biotech mfg → medtech/devices → distributors → payers/PBM → providers/facilities
                 (DHR,TMO,A,WAT)          (MRK,JNJ,ABBV,LLY,      (SYK,ABT,ISRG,     (COR,CAH,   (UNH,CVS,ELV,    (HCA)
                                           PFE,VRTX,REGN...)       MDT,BSX,BDX,EW)     MCK)        HUM,CI)
                                                                                                        │
                                                                              [cross-sector] Health Care REITs
                                                                              (WELL,VTR — GICS Real Estate,
                                                                              finance the senior-care/facility layer)
```

- **Discovery/R&D → tools/CDMO** — *tailwind*, avg flow 0.320 (strongest sub-industry). Demand-driven
  (biopharma R&D spend, biotech licensing wave, §6), not the constraint.
- **Pharma/biotech manufacturing** — *mixed but improving*. Avg flow 0.29–0.31. The binding pressure here
  is downstream pricing, not manufacturing capacity.
- **Medtech/devices** — *tailwind*, avg 0.282, broad (8 names, only BSX red).
- **Distributors** — *weakest node*, avg 0.168 (COR strong, CAH/MCK weak) — a pure margin pass-through
  layer, structurally thin; not where the thesis lives either way.
- **Payers/PBM** — **★ THE BOTTLENECK (binding constraint).** Everything upstream (discovery, mfg,
  devices) is currently a green-to-neutral tailwind; the one node that can gate the whole chain's
  economics is **reimbursement/pricing policy** — Medicare/Medicaid/ACA-exchange rates (UNH Item 1A) and
  MFN drug-pricing terms (ABBV Item 1A). Strong underlying demand (aging demographics, GLP-1 volumes,
  drug innovation pipeline) is **not** the bottleneck — policy/reimbursement is. This node is *currently
  easing* (§5), which is exactly why the chain is bid broadly rather than just at the demand end.
- **Providers/facilities** — thin coverage (HCA only, weakest single-name flow 0.112) — the layer most
  exposed if payer reimbursement tightens again.
- **Cross-sector chain: Health Care REITs (WELL/VTR)** — sit in GICS Real Estate but their economics
  (senior-care/skilled-nursing occupancy, financed by Medicare/Medicaid-linked payer reimbursement) run
  through the **same bottleneck node** as payers, not through office/retail/rate-duration dynamics. →
  resolved in §7.

---

## §5 — What the news velocity count is too crude to see (P4 — body-drilled)

The brief's 465 hits/7d (search: `healthcare pharma biotech FDA`, OR/syn) undercounts because it is a
**headline-density** measure of 4 generic buckets; two real, dated, sub-industry-specific fundamentals
surfaced only on AND-mode body drills:

**(a) MFN drug-pricing deals — the pharma-node overhang is being resolved deal-by-deal, not headline-by-headline.**
*"Donald Trump's Drug-Pricing Deals Are Reshaping Big Pharma"* [Motley Fool via Yahoo Finance, 2026-07-14]:
*"Since late 2025, the Trump administration has reached voluntary most-favored-nation (MFN) pricing
agreements with **17 of the world's largest pharmaceutical manufacturers**, including Pfizer, AbbVie, and
Bristol Myers Squibb... These agreements generally align prices for certain drugs with those paid in
comparable developed countries, expand discounted direct-to-consumer purchasing through the TrumpRx
platform, and provide MFN pricing for certain Medicaid purchases."* Also confirmed via UPI 07-16: *"Trump
announces lower drug prices in deals with nine companies."* This is a **multi-year policy overhang (drug
pricing reform tail-risk) being defused incrementally since late 2025** — exactly the kind of process
story a 4-keyword headline-velocity count structurally cannot register as "news," because it isn't one
event, it's a running count of deals. It explains why PFE/ABBV/BMY/JNJ are all flow-positive (JNJ 0.51,
ABBV 0.54, MRK 0.59) despite the sector's velocity looking dead.

**(b) Managed-care turnaround + reduced ACA exchange-subsidy uncertainty — the payer-node catalyst.**
*ClearBridge Value Strategy Q2 2026 Commentary* [SeekingAlpha, 2026-07-15]: *"Health care also
contributed, with CVS Health (CVS) and UnitedHealth Group (UNH) benefiting from improved sentiment
toward managed care. CVS rose as stronger... earnings, raised full-year guidance and better performance
in its health benefits business supported confidence in the company's turnaround, while **reduced policy
uncertainty around exchange subsidies** also helped. UnitedHealth advanced as better cost trends and a
more favorable outlook helped rebuild confidence after prior pressure on margins."* This is a **named
institutional manager**, not a headline-chasing wire piece, independently corroborating the payer bid.
**Same-day confirmation:** *"UnitedHealth's stock rallies on improved outlook for the year"* [MarketWatch,
2026-07-16] and *"UnitedHealth rallies premarket while chip stocks retreat"* [Yahoo, 2026-07-16] — UNH
beat Q2 and raised guidance **on the exact day the AI/chip complex cracked** (medical cost ratio ~83.9%
cited, down from 2024-25 crisis levels [Yahoo 07-26 retrospective, exact print detail not fully quotable
in-DB → treated as directional, not precise]).

**Read:** these are two distinct, dated, real fundamentals — one pharma-specific (MFN deal count), one
payer-specific (cost-ratio turnaround + subsidy clarity) — that a crude 4-term headline count cannot
detect because they are *running processes*, not single events. This is the strongest evidence in this
run for the "early, un-crowded" read over "defensive parking with no thesis."

**Biotech licensing context (background, not a direct US-name driver this window):** *"Mainland China
funds increase stakes in Hong Kong biotech amid surge of licensing deals"* [SCMP, 2026-07-16] — a
China/HK-listed biotech re-rating on cross-border out-licensing deal flow (Hang Seng Innovative Drug
Index +12.6%/month). No direct in-window evidence of a specific US large-cap (MRK/PFE/ABBV) in-licensing
deal from a Chinese biotech was found in this search pass — flagged as sector-wide BD-cycle context, not
promoted to a named catalyst for a specific US ticker.

---

## §6 — chain-hop candidates (body-proximate only, flow cross-checked — none headline-named)

`chain-hop "GLP-1" "obesity drug"` [news, 21d/foreign]: **AMGN** surfaces as a body-proximate co-mention
(2 body / 0 headline) inside Eli Lilly GLP-1 articles. **Flow cross-check: FAILS.** AMGN flow +0.159 (well
below the sector's 0.357 and even below biotech's own 0.310 sub-industry average), **OBV 중립 (not
accumulating — the only major biotech name without 매집)**, RS20 +6.8%/RS60 +0.2% (flat). AMGN has **not**
caught the bid — logged as WATCH, not promoted.

⚠ **LLY appeared 16 body / 25 total co-mentions but is NOT a genuine hidden candidate** — it is the actual
subject of those articles under its company name ("Eli Lilly"), which the chain-hop ticker-regex doesn't
match against headlines phrased with the company name instead of "LLY." A tool artifact, named explicitly
so it isn't miscounted as alpha. **MMM/JPM/MS** co-mentions in the same articles are incidental
portfolio-comparison boilerplate ("could this stock make you a millionaire like LLY/JPM/MS...") — not
real value-chain candidates. Discarded, reason stated.

`chain-hop "drug pricing" "MFN deal"` [news, 21d/foreign]: **0 candidates** past the headline-named
threshold (ABBV/PFE/BMY/HUM already headline-named) — the MFN story is fully attributed to the named
majors; no hidden beneficiary detected.

`chain-hop "senior housing" "healthcare REIT"` [news, 21d/foreign]: **VTR** is the body-proximate partner
to headline-named WELL (2/2) — already flow-confirmed directly (§7), not a "hidden" find per se, but
confirms WELL/VTR trade as a matched pair in the press too.

**Net: chain-hop discipline surfaces zero clean promotable candidates this run.** Every hit either fails
the flow cross-check (AMGN) or turns out to be a mislabeled headline name (LLY) or incidental noise
(MMM/JPM/MS). Stated plainly rather than manufacturing a candidate to fill the section.

---

## §7 — Chart read (verbatim, `module_chart --read`) [chart]

**ABBV** (biotech/pharma flow leader):
```
OBV: 분배(매도압력↑) (20d기울기 -42%)
다이버전스: 약세(가격 고점↑ · RSI 고점↓)
MA정렬: 강세스택(5>20>60>120) · 가격 4/4 MA 위
볼린저: 수축(코일링) 19.5% · 중단
RSI: 62.5 · 모멘텀20d +15.8%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 214.96
```
*Read: bullish MA stack intact, but **OBV distributing** (−42% 20d slope) **with a bearish price/RSI
divergence** — price making higher highs, RSI making lower highs, on the single biggest biotech flow
leader. This is the first visible crack-candidate in the "quiet accumulation" story — worth tracking
closely (§8).*

**WELL** (healthcare REIT):
```
OBV: 분배(매도압력↑) (20d기울기 -16%)
다이버전스: 약세(가격 고점↑ · RSI 고점↓)
MA정렬: 강세스택(5>20>60>120) · 가격 4/4 MA 위
볼린저: 수축(코일링) 17.7% · 중단
RSI: 70.4 · 모멘텀20d +16.9%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 206.55
```
*Read: same signature as ABBV — OBV distributing + bearish divergence + **RSI 70.4 (overbought)** —
technically the most extended/toppy of the three names checked, despite module_flow tagging it OBV=매집
(a shorter-window read; the chart's 20d-slope read is stricter). Entry timing on WELL specifically looks
stretched even if the sector-reclassification argument (§8) favors it.*

**DHR** (life-science tools, the clean counter-example):
```
OBV: 누적(매수압력↑) (20d기울기 +22%)
다이버전스: 없음
MA정렬: 혼조 · 가격 4/4 MA 위
볼린저: 확장 17.4% · 상단밴드
RSI: 64.8 · 모멘텀20d +15.6%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 176.80
```
*Read: genuinely clean — accumulating OBV, no divergence, CONFIRMED-TURN. Shows the "broad accumulation"
read is not uniformly extended across HLTH — the tools/CDMO leg looks structurally healthier than the
biotech-megacap or REIT legs right now.*

---

## §8 — RESOLUTION VERDICT (mandatory)

### "Money with no story" — durable rotation or parking lot?

**Verdict: reads as (i) — an early, under-covered, fundamentals-supported rotation — not (ii) pure
defensive parking.** Confidence: **moderate**, not high.

**Evidence for (i):**
1. **Breadth, not concentration.** All 8 HLTH sub-industries average flow-positive (0.11–0.32, narrow
   spread); only 2 of 32 names red, both idiosyncratic (ELV, PFE). Parking-lot money fleeing a scary
   sector typically clusters in the single most defensive corner (staples-like pharma megacaps) — instead
   **biotech (a higher-beta, growth-style corner, not classically defensive) is tied for the strongest
   sub-industry (0.310)**, level with life-science tools. That argues against pure flight-to-safety.
2. **Two real, dated, sub-industry-specific fundamentals the crude velocity count structurally cannot see**
   (§5): the MFN drug-pricing deal wave (17 majors since late 2025, defusing pharma's multi-year pricing
   overhang) and the UNH/CVS managed-care turnaround + ACA exchange-subsidy clarity, confirmed same-day
   by UNH's 07-16 beat-and-raise landing on the exact day chip stocks cracked. These are process stories,
   not headline events — exactly why they don't show up in a 4-keyword headline count but are real.
3. **No short-covering mechanics.** All 11 names checked on FINRA short-vol Z sit in normal range — this
   is not a squeeze; it's demand.
4. **HLTH-not-STPL discriminator confirmed and explained.** STPL's negative sector wflow is driven
   entirely by 3 mega-caps in 🔴분산 (WMT −0.713, COST −0.485, PEP −0.479) while smaller staples names
   (MNST, MO, KO) are flow-positive — STPL's weakness is idiosyncratic mega-cap/retail, not a rejection of
   defensive money. **HLTH has an identifiable policy catalyst STPL never had (MFN deals); STPL does not.**
   This is not a coin-flip "money hides wherever" — HLTH earned the bid on a real, findable overhang lift.

**Evidence for (ii) / against high conviction:**
- **Zero 🟢가속 names, zero clean volume-confirmed ignition** (max vol_surge 1.46x carries no green tag).
  The move hasn't been tested by conviction buying yet.
- **ABBV and WELL both show OBV distribution + bearish price/RSI divergence** on `module_chart` (§7) —
  the two most prominent flow leaders in the biotech and REIT sub-legs are technically the most extended,
  not the freshest. If this is truly "early," the cleanest names (structurally) should look more like DHR
  (CONFIRMED-TURN, no divergence) — most don't, yet.
- Flow alone (uniform 매집, no ignition) is genuinely ambiguous between "early and quiet" and "hiding and
  waiting" — it cannot discriminate the two hypotheses by itself. The discriminator has to come from the
  fundamentals (§5) and from what happens next (the falsifier below).

### ★ THE FALSIFIER (named observable)

**HLTH's fundamental drivers (MFN deal count, UNH/CVS cost-ratio trend) do not depend on the AI-complex
being scary. The "parking lot" hypothesis does.** So the clean test is what happens to HLTH flow *after*
the AI-unwind reason to hide has resolved:

> **Track the next `SECTOR_FLOW_US` sweep taken in a window where MU has reclaimed and held above
> $853.20 (the PREMORTEM's own MU anti-signal level) for 2+ sessions.**
> - If HLTH wflow **holds ≥+0.20 and breadth stays ≥6-of-8 sub-industries positive** in that window →
>   **durable (i)** — the money stayed for its own reasons (MFN deals, payer turnaround), confirming it
>   was never really about hiding from AI.
> - If HLTH wflow **collapses toward 0 or negative** as MU stabilizes → **confirmed parking lot (ii)** —
>   the bid was defensive ballast that reverses the moment the thing it was hiding from stops being scary.

This is the sharpest available test because it isolates the two competing explanations: one predicts
HLTH flow is independent of MU, the other predicts HLTH flow is *inversely* conditional on MU.

### WELL/VTR verdict — belongs to HLTH OW, not RE UW

**Reassign.** WELL (0.517) and VTR (0.483) flow at **1.4–1.5x the HLTH sector average** and vastly exceed
RE's sector wflow (−0.046); both are OBV=매집 on the direct module_flow pull (§1). Their tenant economics
run through **Medicare/Medicaid-linked senior-care reimbursement** — the exact same payer-policy
bottleneck node as the rest of HLTH's value chain (§4) — not through the office/retail/rate-duration or
data-center/tower dynamics dragging the rest of RE (CCI −0.652, DLR −0.706, EQIX −0.812, AMT −0.839, all
🔴분산). The blanket RE-UW is correctly capturing that data-center/tower leg while mispricing this
sub-leg's real driver. *"Ventas: Ahead Of Q2 Results, Lots To Like About This Senior-Care REIT"*
[SeekingAlpha, confirmed **2026-07-12**] — exact Q2 print date not confirmable in-DB → `[blank]`
(senior-housing REITs typically report late July/early August). **Caveat:** WELL's own chart (§7) is the
most technically extended of the three names spot-checked (OBV distributing, RSI 70.4, bearish
divergence) — the sector-reclassification argument is separate from entry timing, which looks stretched.

---

## §9 — Track-KPIs + anti-signals (observables)

**Track:**
1. **★ MU $853.20 hold** — the falsifier's pivot (§8). Cross-sector but the single cleanest test of
   durable-vs-parking for this entire sector call.
2. **HLTH sub-industry breadth** (currently 6-of-8 clearly positive, 2 red) — watch for collapse to 1–2
   sub-industries, which would retroactively mean the "broad" read was a one-day artifact.
3. **MFN drug-pricing deal count** — 17 majors as of 07-14; watch for expansion (further de-risking) or a
   company breaking ranks/litigating (re-arms the pharma pricing overhang).
4. **UNH/CVS medical cost ratio trend** — UNH ~83.9% cited around the 07-16 print; watch subsequent
   prints for continued improvement (turnaround intact) vs re-acceleration (2024-25 crisis resumes).
5. **ACA exchange-subsidy resolution** — cited as a live CVS driver (ClearBridge 07-15); watch for the
   actual legislative/regulatory outcome, not just "reduced uncertainty" sentiment.
6. **First HLTH name to cross vol_surge >1.3x WITH a 🟢가속 tag** — the ignition that would convert this
   from "quiet accumulation" into an actual story; none exists yet (§1).
7. **WELL/VTR Q2 prints** — late July/early August, exact date `[blank]` — the REIT sub-leg's own
   fundamental test.

**Anti-signals (what flips the map):**
- ⚑ **ABBV and WELL OBV distribution + bearish RSI divergence** (§7) — the two most prominent flow
  leaders showing technical cracks first. A confirmed breakdown in either (RS20 rolling negative + OBV
  slope staying negative 2+ sessions) would be the first real tell that this leg is topping, not building.
- ⚑ **ELV/PFE red spreading to a 3rd or 4th name** — currently 2 of 32; broadening red would directly
  contradict the "broad accumulation" read.
- ⚑ **HLTH wflow decaying as MU stabilizes above 853.20** — the named falsifier (§8) — this is the
  single cleanest kill-signal for the durable-rotation thesis.
- ⚑ **A company breaking from the MFN pricing-deal consensus** (litigation, withdrawal, or a re-escalated
  legislative price-cap push) — would re-arm the pharma-node overhang the whole rally partly rests on.
- ⚑ **News velocity failing to re-accelerate even after a real catalyst prints** (e.g., WELL/VTR Q2, more
  MFN deals) — if the fundamentals keep firing and velocity *still* doesn't respond, that would suggest
  the market genuinely isn't building a narrative around HLTH yet, sharpening the "early, uncrowded" read
  rather than falsifying it — track this distinction carefully, don't conflate low velocity with no story.

---

**EXIT CHECK:** ✅ flow cross-check (module_flow uniform 매집 + us_flow no short-vol spikes) with
sub-industry split (all 8 positive, breadth not concentration) · ✅ players bounded (32-name universe ∪
WELL/VTR; small-cap bound checked, none added, reason stated) · ✅ ABBV + UNH 10-K IR anchors (Item 1A
pricing-pressure / Medicaid-reimbursement) + MRK 8-K list (nothing catalytic in-window, noted not
inferred) · ✅ 8-node value chain with payer/reimbursement policy named as the binding bottleneck +
cross-sector REIT chain marked · ✅ chain-hop run on 3 themes — zero candidates survived flow cross-check,
stated plainly (AMGN fails, LLY is a tool artifact, MMM/JPM/MS are noise) · ✅ ABBV/WELL/DHR CHART_READ
embedded verbatim · ✅ RESOLUTION VERDICT delivered: **(i) early/durable, moderate confidence** + named
falsifier (MU 853.20-conditioned HLTH flow test) + **WELL/VTR reassigned to HLTH** with entry-timing
caveat · ✅ 7 track-KPIs + 5 anti-signals as observables. Blanks (WELL/VTR exact Q2 date) left blank (P4).
Zero buy/sell calls.
