# SECTOR_DEEP_IT — Information Technology (software / cyber leg)

Run: 2026-07-15 (Wed) · Desk: industry_US · Analyst leg: IT (non-semi flow leaders)
Scope: cybersecurity + application software + mega-cap platform/hardware. **The AI-compute
semiconductor epicenter (TSM/ASML/AVGO/NVDA/MU) is a separate deep-dive (SEMI) — not covered here.**
Stance: IT is a top OW into the run (cool CPI = long-duration relief; Nasdaq crowded-short ~4%ile = squeeze fuel).
No buy/sell calls. Blanks stay blank.

---

## 0. Bottom line (4 lines)

- **Why cyber leads:** the same AI-capex-crowds-out-software-budgets shock that crashed IBM on 07-14 is what *spares* cyber — reallocation pressure falls on IT-services/SI and deferrable app-software, not on breach-cycle/board-mandated security spend. [WebSearch][flow]
- **Bottleneck:** AI-capex crowding out non-AI software opex (the binding constraint sector-wide); for cyber specifically, platform-consolidation displacement lengthens deal cycles / defers revenue recognition. [WebSearch][filing]
- **Top KPI:** NGS/net-new ARR + platformized-customer count & NRR (PANW NGS ARR $8.1B +60% YoY, 120% NRR on platformized base; CRWD Q1 net-new ARR $256M +32% YoY). [WebSearch]
- **Anti-signal:** AI-capex bleeding from IT-services into app-software and eventually cyber budgets; and a rate re-lift that kills the long-duration multiple the whole OW rests on. [WebSearch]

---

## 1. Flow cross-check — cyber cluster accumulation + mega-cap-narrow breadth

### 1a. Sector-level breadth (the wflow≫eqflow reconciliation) [flow]
From `SECTOR_FLOW_US.json` (asof 2026-07-14), Information Technology, n=56:

| metric | value | read |
|---|---|---|
| wflow (cap-weighted) | **0.263** | positive, ranks mid-pack |
| eqflow (equal-weighted) | **0.129** | ~half of wflow |
| green / red | **1 / 8** | one 🟢 vs eight 🔴 |
| breadth | **0.02** | near-zero participation |

**Reconciliation:** wflow (0.263) is ~2× eqflow (0.129) → IT's positive flow is carried by a
handful of mega-caps while the *median* IT name is going the other way (8 red vs 1 green). The
lone 🟢 is **IBM (flow_score 0.887, 🟢가속)** — the STALE TRAP that crashed ~−23% on earnings 07-14
(see §7); ignore it. Strip IBM and IT breadth is effectively negative. IT strength is real but
**narrow**, and the true non-stale flow leaders sit *above* the mega-caps: the cyber cluster.

### 1b. Non-stale IT flow leaders (from names table) [flow]
| ticker | industry | flow_score | tag | velocity | OBV state |
|---|---|---|---|---|---|
| **PANW** | Systems Software (cyber) | **0.667** | 🟡 | 1.92 | 매집 (accum) |
| **FTNT** | Systems Software (cyber) | **0.613** | 🟡 | 1.94 | 매집 (accum) |
| **CRWD** | Systems Software (cyber) | **0.504** | 🟡 | 1.24 | 매집 (accum) |
| ANET | Comms Equipment (net) | 0.500 | 🟡 | 1.20 | 매집 |
| AAPL | HW/Storage | 0.483 | 🟡 | 1.16 | 매집 |
| INTU | Application Software | 0.465 | 🟡 | 1.38 | 중립 |
| MSFT | Systems Software | 0.408 | 🟡 | 1.06 | 매집 |
| NOW | Systems Software | 0.335 | 🟡 | 1.91 | 중립 |
| ORCL | Application Software | 0.317 | 🟡 | 1.22 | **분산 (distribution, OBV −0.576)** |
| CRM | Application Software | **−0.079** | 🟡 | 1.02 | **분산 (distribution, OBV −0.339)** |

**Signal:** the cyber trio (PANW / FTNT / CRWD) are the top three non-stale IT flow scores, each
*above* every mega-cap platform. All three show OBV = accumulation. In contrast the app-software
mega-caps **ORCL and CRM are in distribution** — a clean divergence: money is accumulating cyber
while leaving legacy app-software. This is the flow-leading sub-leg.

### 1c. Flow snapshot (`module_flow … --bench SPY`) [flow]
All six mapped names print **🟡 neutral** (RS20/RS60 = NaN this run, so no relative-strength
confirmation — treat flow_score + OBV as the live read). News velocity: INTU 2.28× (hottest),
PANW 1.91×, AAPL 1.17×, CRWD 1.15×, MSFT 1.04×, FTNT 1.01×. OBV = accumulation for
PANW/FTNT/CRWD/AAPL/MSFT; INTU neutral. Volume surge <1.0 across the board (0.65–0.81×) — flow
is accumulation-by-drift, **not** a volume-thrust breakout yet.

### 1d. Short-vol pressure (`scripts/us_flow.py`, FINRA Reg SHO 2026-07-14) [flow]
| ticker | short% | base20 | Z | 5v5 trend | verdict |
|---|---|---|---|---|---|
| PANW | 55.8% | 51.1% | +0.59 | −0.6 ▼ | 🟡 normal range |
| FTNT | 35.2% | 38.8% | −0.35 | +4.2 ▲ | 🟡 normal range |
| CRWD | 50.8% | 49.1% | +0.28 | +2.8 ▲ | 🟡 normal range |

At the single-name level the cyber trio short-vol is *normal* (Z within ±0.6) — the "Nasdaq
crowded-short ~4%ile squeeze fuel" is an **index/basket** phenomenon, not a name-specific squeeze
set-up in cyber. PANW's short-vol is high (55.8%) but flat-to-falling (−0.6 trend); FTNT/CRWD
short trend is rising (+4.2 / +2.8) into accumulation — a mild build, not an extreme.

---

## 2. Sub-leg map — driver, recurring-rev quality, rate sensitivity

### 2a. Cybersecurity — PANW / FTNT / CRWD (+ ZS) — **the flow-leading sub-leg**
- **Driver:** non-deferrable demand. Breach cycle + AI-driven threats have made security a
  board-level line item that is "harder to defer," and post-breach 63% of orgs *increase* spend
  (+23.5% YoY). Gartner security spend $213B in 2026 (+12.5%); dedicated AI-security budgets now at
  30% of orgs (up from 20%). [WebSearch]
- **AI-attach:** AI is a *demand tailwind* for cyber (more attack surface, AI-SOC/agentic-defense
  upsell) rather than a cannibalization risk — the opposite of the app-software fear.
- **Recurring-rev quality:** subscription/NGS ARR models; PANW platformized base runs 120% NRR,
  single-digit churn. [WebSearch]
- **Rate sensitivity:** high-multiple long-duration names → direct beneficiaries of cool CPI /
  lower discount rate.

### 2b. Application software / AI-monetization — MSFT / ORCL / CRM / NOW / INTU
- **Driver:** the 2026 narrative pivot from "AI disruption" to "AI monetization." Hybrid seat+usage
  pricing is now standard (~65% of AI-adopting SaaS); CRM's AELA moves to flat-rate seat-based
  unlimited agentic use (predictability over per-token). [WebSearch]
- **Recurring-rev quality:** strong, but this is the sub-leg most exposed to the crowding-out risk —
  and the flow table already shows **ORCL/CRM in distribution, NOW low flow (0.335)** despite hot
  velocity. The seat-vs-usage transition is a revenue-timing overhang.
- **Rate sensitivity:** high, same long-duration multiple beneficiary as cyber — but with a demand
  question mark cyber doesn't carry.

### 2c. Mega-cap hardware — AAPL
- **Driver:** installed-base services + eventual on-device-AI refresh cycle; flow_score 0.483,
  velocity 1.16, OBV accumulation. Lower-multiple, lower-duration than software → smaller direct
  beneficiary of the discount-rate move; behaves as the sector's ballast rather than its leader.

### 2d. ANET (networking, SEMI-borderline)
- Flow_score 0.500, OBV accumulation. AI-datacenter Ethernet fabric play — **overlaps the SEMI
  deep-dive**; noted here for completeness, mapped there.

---

## 3. Why cyber is leading — the catalyst [WebSearch]

The evidence points to a single, coherent mechanism that both explains cyber's flow lead **and**
ties it to the IBM crash that headlines the IT tape today:

1. **Structural budget shock (07-14):** IBM warned AI spending is crowding out software budgets;
   clients shifted capex toward servers/storage/memory (supply-constrained, HBM-driven DRAM
   scarcity) ahead of price increases, and "numerous large deals" failed to close (rev miss
   ~$660M). Stock fell ~−23%. ServiceNow −8%, MSFT −3%, CRM/ACN/WDAY fell in sympathy. [WebSearch]
2. **Where the pressure lands:** per the same channel work, reallocation pressure is **heavier on
   IT services / systems integrators** (IBM's core) "than on cloud infrastructure or
   cybersecurity." Goldman flagged "crowding out of category spend *not tied to AI*." [WebSearch]
3. **Why cyber is the exception:** breach cycle + AI-driven threats keep security board-mandated
   and non-deferrable; 63% of breached orgs raise spend; AI *adds* attack surface to defend. So the
   money leaving deferrable IT-services and app-software is **not** leaving cyber — which is exactly
   the divergence the flow table shows (cyber accumulating, ORCL/CRM distributing). [WebSearch][flow]

**Name-level confirmation (recent guides / analyst moves):** [WebSearch]
- **PANW:** NGS ARR $8.1B +60% YoY (organic +28% ex-acquisitions); FY2026 target ~$11.3B revenue /
  ~53% NGS ARR growth; FY2027 NGS ARR guide ~$10.95B; FY2030 target $20B NGS ARR + 4,000
  platformized customers. Street PT raises early July: Wells Fargo $420, Needham $425, BTIG $380.
- **CRWD:** Q1 FY2027 (ended Apr 30, 2026) record net-new ARR $256M +32% YoY; ARR $5.51B +24% YoY;
  raised FY net-new-ARR growth to ~27.7% (an *acceleration*); record FCF $468M; announced 4-for-1
  split. (Caveat: post-print the stock had sold ~−13% on "modest guidance" — high bar, hot RSI.)
- **FTNT:** Q1 2026 revenue $1.85B +20% YoY, product revenue $645M +41% YoY (hardware/firewall
  refresh reaccelerating), ~80% gross margin, ~28.6% net margin.

---

## 4. IR / filings — PANW 10-K [filing]

Source: PANW FY2025 Form 10-K, period 2025-07-31, filed 2025-08-29, accession 000132756725000027.
URL: https://www.sec.gov/Archives/edgar/data/1327567/000132756725000027/panw-20250731.htm

- **Item 1 (business):** subscription + support security platform; sells substantially all product
  through channel partners; growth strategy centers on cross-selling additional
  product/subscription modules into large enterprise end-customers (the "platformization" motion).
- **Item 1A (anti-signals / risk factors):** revenue is recognized **over the service term**, so a
  demand downturn hits reported revenue on a *lag* (deferred-revenue cushion masks a slowdown, then
  reveals it later); dependence on **cross-sell to large enterprises** (platformization is the
  growth engine *and* the concentration risk); **channel-partner reliance** for nearly all sales;
  risk that **sales prices decrease** (discounting to win platform deals compresses gross profit);
  period-to-period result volatility + seasonality; unfavorable macro/geopolitical conditions.
- **Item 7 (MD&A):** management monitors GAAP + non-GAAP key metrics (ARR the central KPI); MD&A is
  organized Overview → Key Financial Metrics → Results of Operations. (This run's extract returned
  the MD&A framing/boilerplate; the live ARR growth figures are carried from IR/earnings in §3.)

*Note:* the 10-K anti-signal that matters most for the platformization thesis is the combination of
**over-term revenue recognition + discounting to land platform deals** — it means a strong ARR
headline can coexist with softening billings/margin for several quarters before it shows in revenue.

---

## 5. Value chain / competitive structure

### Cybersecurity — platform consolidation vs point solutions
- **Structure:** PANW is running "platformization" — bundling network, cloud, and SecOps into a
  single platform to *displace point solutions* and lift NRR (120% on platformized customers). This
  is share-gain within a growing pie: PANW/FTNT/CRWD consolidate budget that used to fan out across
  dozens of niche vendors (ZS and others are the displaced/contested layer).
- **Bottleneck (binding constraint):** **sales-cycle length + displacement friction.** Platform
  deals are large, multi-year, and often discounted to win — they lengthen the cycle and, under the
  10-K's over-term recognition, defer the revenue. Consolidation is a tailwind for the winners but
  the *timing* of billings→revenue is the constraint on how fast flow converts to reported growth.

### Application software — AI-monetization (seat vs usage)
- **Structure:** the open question is whether AI expands seats (predictable) or shifts to usage
  (variable, and potentially *fewer* seats if agents replace users). CRM's flat-rate seat-based
  AELA is a defensive answer; hybrid seat+usage is the emerging standard. [WebSearch]
- **Bottleneck (binding constraint):** **AI-capex crowding out software opex.** This is the
  sector-wide binding constraint and it went from thesis to fact on 07-14 (IBM). If enterprises
  divert budget to AI infrastructure (servers/storage/HBM), non-AI software opex is the swing
  variable that gets cut first — hitting app-software (already distributing in the flow table)
  before it reaches board-mandated cyber.

**Sector bottleneck, one line:** the binding constraint is *not* demand for security — it is
**whether AI-capex reallocation stays confined to IT-services/app-software or spreads into cyber
budgets**; today's evidence says it is confined, which is why cyber leads.

---

## 6. Chart read — verbatim [module_chart]

**PANW `--read`:**
```
OBV: 누적(매수압력↑) (20d기울기 +68%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 4/4 MA 위
볼린저: 확장 35.4% · 중단
RSI: 67.2 · 모멘텀20d +24.0%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 279.90
```

**CRWD `--read`:**
```
OBV: 누적(매수압력↑) (20d기울기 +114%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 4/4 MA 위
볼린저: 확장 28.2% · 상단밴드
RSI: 74.3 · 모멘텀20d +21.6%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 168.26
```

**Read (deterministic only, no call):** both are CONFIRMED-TURN with bullish MA stacks, no
divergence, and steep OBV accumulation slopes (PANW +68%, CRWD +114% over 20d) — the chart confirms
the flow-table accumulation. Caution flags: **CRWD RSI 74.3 and riding the upper Bollinger band**
(extended/hot), vs PANW RSI 67.2 mid-band (more room). Structural stops (swing lows) reported at
PANW 279.90 / CRWD 168.26.

---

## 7. Track-KPIs + anti-signals

### KPIs to track (the leading indicators of this sub-leg)
| KPI | why | current read [WebSearch] |
|---|---|---|
| **NGS / net-new ARR** | the recurring-rev growth engine | PANW NGS ARR $8.1B +60% YoY; CRWD Q1 net-new ARR $256M +32% YoY (accel.) |
| **Platformized-customer count + NRR** | consolidation share-gain proof | PANW 120% NRR, single-digit churn; FY2030 target 4,000 customers / $20B ARR |
| **Seat vs usage growth (app-sw)** | tells if AI expands or erodes seats | CRM moving to flat-rate seat (AELA); hybrid seat+usage now ~65% of AI SaaS |
| **Product-revenue reaccel (FTNT)** | firewall/hardware refresh cycle | FTNT product rev +41% YoY |
| **Discount rate / CPI path** | the multiple driver | inflation ~2.1% → Fed path toward ~3.0% terminal (cool CPI = relief on) |

### Anti-signals (watch to invalidate)
1. **AI-capex crowding out software opex — already live.** IBM −23% (07-14), NOW −8%, MSFT −3%,
   CRM/ACN/WDAY in sympathy; Goldman: "crowding out of category spend not tied to AI," hesitancy on
   larger IT projects. **Trip-wire:** the pressure spreading from IT-services → app-software →
   *cyber* budgets. So far it is confined to IT-services/app-software (which is *why* cyber leads);
   the moment cyber ARR guides soften, the whole thesis inverts. [WebSearch][flow]
2. **Rate re-lift kills the long-duration multiple.** The entire OW rests on cool CPI (2.1%) → lower
   discount rate. A hot CPI print / hawkish Fed repricing reverses the multiple relief that is the
   primary bid under high-ARR-multiple software and cyber. [WebSearch]
3. **STALE TRAP hygiene:** IBM's 🟢가속 (flow_score 0.887) in the sector table is a lagging news/OBV
   artifact from *before* the 07-14 crash — do not read it as an IT green light; it is the anti-
   signal's origin, not a flow leader. [flow]
4. **Name-level extension:** CRWD RSI 74.3 on the upper band + a ~−13% post-earnings reaction on
   "modest guidance" = high bar / crowded expectations; accumulation is real but the entry-risk is
   elevated vs PANW. [module_chart][WebSearch]

---

## Sources
- [flow] `module_flow` out/flow/2026-07-15.json; `scripts/us_flow.py` (FINRA Reg SHO 2026-07-14);
  `SECTOR_FLOW_US.json` (asof 2026-07-14).
- [filing] PANW FY2025 10-K, SEC EDGAR accession 000132756725000027 (period 2025-07-31).
- [module_chart] `module_chart PANW/CRWD --read`, 2026-07-15.
- [WebSearch] Futurum / Seeking Alpha / Needham / Wells Fargo (PANW NGS ARR & PT raises); CrowdStrike
  IR Q1 FY2027 release + Yahoo Finance; Fortinet Q1 2026; Gartner / IBM / Help Net Security (cyber
  budget 2026); TechTimes / Communications Today / CFO Brew / Goldman commentary (IBM 07-14 AI-capex
  crowd-out); GetMonetizely / Chargebee / Seeking Alpha (AI-monetization seat-vs-usage); FinancialContent (CPI/rate path).
```
