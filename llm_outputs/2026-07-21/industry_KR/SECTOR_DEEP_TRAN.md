# SECTOR_DEEP — TRAN (운송·창고) · industry_KR · 2026-07-21 (Tue)

> Stage 5 / L1·DEEP (Phase 2) · **ROTATING sector, rule-(b) flow-led promote, NEVER deep-dived by this desk
> → FULL FRESH MAP.** Not in the GICS-11 matrix. Not an OW.
> Inputs re-read from disk: `SWEEP_READ.md` §3/§4(e) · `EVENT_ALPHA.md` **CARD 8** · `SECTOR_ROTATION.md`
> §2(g)/§4 · `MACRO_REPORT.md` §1(KRW)/§4a M-02 · `SECTOR_FLOW_KR.json` (829 names, asof 2026-07-21).
> Tools: `module_flow` (`.KS` suffix — bare 6-digit silently returns empty) · `module_business` ·
> `module_disclosure` · `module_valuation` · `module_chart --read` · `module_news_data fts` (domestic) ·
> yfinance balance sheet · `module_report_tags`.
> **Zero buy/sell calls. P4: blanks stay blanks.**

---

## §0 ★ THE ANSWER UP FRONT

**ROTATION asked: *what is buying HMM, if not freight rates?***

**Verdict: it IS the freight rate — but the LEVEL and the LAGGED earnings it has already booked, not the
weekly direction that CARD 8 measured.** CARD 8's fact was correct and its inference was wrong, and the
refutation is inside the very article CARD 8 quoted:

| | Value | Source |
|---|---|---|
| SCFI, 2026-07-20 (after **2 down weeks**) | **3,080.31** (−104.51pt, −3.3% wow) | 해진공 via donga 07-21 (**the CARD 8 article**) |
| SCFI, **2Q 2026 average** — the level already in the books | **2,336** (+42% YoY, **+55% QoQ**) | 에프앤가이드 via mt 07-07 |
| **Today's level vs the 2Q average that produced the earnings** | ★ **+31.9%** | derived |
| HMM 2Q OP consensus | **₩3,400억 (+46% YoY)** | 에프앤가이드 via mt 07-07 |
| HMM **3Q** OP consensus (freight books with a **contractual lag**) | ★ **>₩9,000억 = 2.65× 2Q** | 에프앤가이드 via mt 07-07 |
| HMM FY OP consensus | **₩2조에 근접** | 에프앤가이드 via mt 07-07 |
| Net cash (FY25: cash+STI ₩13.35조 − total debt ₩5.19조) | **₩8.16조 = 43% of mcap** | yfinance BS, asof 2025-12-31 |
| **EV = mcap ₩18.96조 − net cash** | **₩10.80조** → **EV/OP ≈ 5.4×** | derived |

**A two-week −7.4% fade from 3,327 (07-03) leaves the index 31.9% above the quarterly average that
generated a +46% YoY print and a 2.65× sequential consensus.** CARD 8 read a *direction* where the
operative variable is a *level* with a booking lag. **That is the resolution.**

**And the desk got a free, clean, same-day negative control on the hypothesis it killed** — see §4(v):
on **07-21 the Houthis declared a naval blockade of Saudi Arabia** (the maximal Red Sea headline; Reuters:
up to **7% of world oil supply** at risk) and **the KR shipping tape gave the whole spike back within one
session** — 흥아해운 **+16.97% intraday → +2.69% close**, STX그린로지스 **+27.29% intraday → −3.62% close**,
팬오션 **−0.60%**, 대한해운 **−1.27%** [yonhap 07-21 16:08]. **HMM is not named in either article.**
**So CARD 8 was right that HMM is not a Red Sea trade. It was wrong that HMM is not a freight trade.**

**대한항공: the FX hypothesis is REFUTED, and its sign is disputed.** The driver named by the company's own
07-13 print, by Bloomberg's cross-carrier analysis and by two broker target raises inside the window is
**AI air cargo** — 2Q 화물매출 **$1.03B, +38.4% QoQ**, TAC index Seoul/HK/Taipei→US at a **2022-since high**.
Fuel dominates FX by **~2.2×** on the cost line, and on the operating line **won strength is net NEGATIVE**
(−₩3,036억/yr) because KAL's FX-linked revenue (₩13.78조) is 2.5× its USD purchases (₩5.49조). §5.

**→ BET: nothing from this file. §10 states why, and the exact dated condition under which that changes.**

---

## §1 Flow — the sector, and the one number that reframes it

**Sector aggregate** (`SECTOR_FLOW_KR.json`, asof 2026-07-21 close, bench `^KS11`):
**n=24 · wflow +0.272 · eqflow +0.058 · 2🟢/0🔴 · breadth 0.08 · Δ +0.078** — 4th best sector of 28.

⚠ **First correction to the inherited read.** SWEEP/ROTATION carried "2🟢/0🔴" alongside HMM and 대한항공.
**The two 🟢 in the JSON are NOT HMM and 대한항공 — they are 흥아해운 (₩0.42조) and 한익스프레스 (₩0.03조).**
The sector's green count is **two micro-caps totalling ₩0.45조**, i.e. **0.9% of the sector's ₩51.6조**.
**wflow +0.272 vs eqflow +0.058 is a 4.7× wedge: this sector is two large names, not a sector.**

⚠ **Second correction — a live-vs-snapshot tag divergence, recorded not smoothed.** The JSON tags HMM and
대한항공 **🟡중립**; a live `module_flow` re-run at 18:29 tags both **🟢가속**. Conversely the JSON tags
흥아해운 **🟢가속** and the live run **downgrades it to 🟡중립** on the KIS weak-hands gate. **The live run is
the operative one** (it carries the KIS per-investor gate). Both are recorded so the next run can see the drift.

### Live `module_flow` (18:29 KST, bench `^KS11`) — the six names that matter
| Ticker | Name | Tag | OBV | RS20 | RS60 | 서지 | 외국인 20d | 기관 20d | 개인 20d | 공매도 |
|---|---|---|---|---|---|---|---|---|---|---|
| **011200.KS** | **HMM** | **🟢가속** | **매집** | **+28.8%** | −10.4% | 0.98× | **+21.9만** | **+303.9만** | −328.8만 | **1.05% ⚠주목, covering(−0.13)** |
| **003490.KS** | **대한항공** | **🟢가속** | 매집 | **+19.7%** | −6.6% | 0.97× | −121.5만 | ★ **+748.2만** | −606.3만 | 0.2% flat(−0.02) |
| 028670.KS | 팬오션 | 🟡중립 | 중립 | +27.9% | −17.4% | 0.53× | **+97.7만** | **+340.2만** | −429.6만 | 0.09% covering |
| 003280.KS | 흥아해운 | 🟡중립 | 매집 | +34.4% | **−46.8%** | **1.57×** | ⚠ **−229.8만** | +1.2만 | ⚠ **+227.2만** | 0.62% **building(+0.17) ⚠주목** |
| 044450.KS | KSS해운 | 🟡중립 | 중립 | +29.7% | −27.3% | 0.84× | −11.7만 | +2.1만 | −0.5만 | 0.54% flat ⚠주목 |
| 005880.KS | 대한해운 | 🟡중립 | **분산** | +18.3% | −40.0% | 0.51× | **+210.5만** | −53.1만 | −160.3만 | 0.34% **building(+0.14)** |

★ **The signature that separates the real bid from the theme trade, and it is unambiguous:**
- **HMM · 대한항공 · 팬오션** — 외국인/기관 net buy, 개인 net sell (개인 −328.8만 / −606.3만 / −429.6만).
- **흥아해운** — 외국인 **−229.8만**, 개인 **+227.2만**, short **building +0.17**. **Textbook 약한손 흡수**, and
  it is precisely the name that spiked +17% and gave it back today. **The JSON's 🟢 is a retail print.**

⚠ **RS20 in this tape is not "went up".** `^KS11` is **−25.97%/1m**; RS20 is *relative*. Confirmed by the
chart reads below: HMM's absolute 20d momentum is **+8.1%** (it really rose); 대한항공's is **−2.1%**
(it fell, less). **Treating both +28.8% and +19.7% as "accumulation" without this split is an error the
sector table invites.** They are different animals.

### CHART_READ — embedded VERBATIM per L2

**011200.KS HMM**
```
OBV: 중립 (20d기울기 +15%)
다이버전스: 없음
MA정렬: 혼조 · 가격 3/4 MA 위
볼린저: 수축(코일링) 12.2% · 중단
RSI: 71.1 · 모멘텀20d +8.1%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>20,284 + OBV→누적 / 스탑(스윙저점): 18,310
```

**003490.KS 대한항공**
```
OBV: 분배(매도압력↑) (20d기울기 -47%)
다이버전스: 약세(가격 고점↑ · RSI 고점↓)
MA정렬: 혼조 · 가격 1/4 MA 위
볼린저: 수축(코일링) 18.2% · 하단밴드
RSI: 34.9 · 모멘텀20d -2.1%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>26,070 + OBV→누적 / 스탑(스윙저점): 25,350
```

⚠⚠ **A HARD TOOL CONFLICT ON 대한항공, and it must not be smoothed.** `module_flow` reads
**OBV 매집 (+0.18)**; `module_chart` reads **OBV 분배(매도압력↑), 20d slope −47%, 약세 다이버전스, RSI 34.9,
하단밴드**. Two modules, same name, same close, **opposite OBV verdicts.** The desk's largest single
institutional print of the run (기관 +748.2만) sits on a name whose chart engine says **distribution**.
**Neither reading is discarded here** — the divergence is itself the finding, and it is why §10 sends
nothing to BET. Whichever is right, **대한항공's 🟢가속 is not a price-confirmed accumulation**: RSI 34.9
at the lower Bollinger band with 모멘텀20d −2.1% is not what accumulation looks like.

---

## §2 Players — all 24 names, then narrowed

**Full sector (`sector == 운송·창고`, 24 names, mcap-ranked, asof 2026-07-21):**

| # | Ticker | Name | mcap(조) | flow | tag | OBV | RS20 | RS60 | 서지 | Δ | Sub-lane |
|---|---|---|---:|---:|---|---|---:|---:|---:|---:|---|
| 1 | 011200 | **HMM** | **18.48** | +0.65 | 🟢* | 매집 | +28.8 | −10.4 | 0.97 | **+0.243** | 컨테이너 원양 |
| 2 | 086280 | 현대글로비스 | 14.09 | −0.28 | 🟡 | **분산** | +19.0 | −24.4 | 0.50 | 0.000 | 3PL/PCTC |
| 3 | 003490 | **대한항공** | **9.56** | +0.65 | 🟢* | 매집 | +19.7 | −6.6 | 0.97 | −0.016 | 항공 여객+화물 |
| 4 | 028670 | 팬오션 | 2.81 | +0.05 | 🟡 | 중립 | +27.9 | −17.4 | 0.53 | **−0.274** | **건화물 벌크** |
| 5 | 000120 | CJ대한통운 | 1.68 | −0.13 | 🟡 | 분산 | +18.8 | −39.0 | 0.64 | −0.003 | 택배/계약물류 |
| 6 | 020560 | 아시아나항공 | 1.44 | −0.09 | 🟡 | 분산 | +22.9 | −9.8 | 0.62 | **+0.154** | 항공 (**피합병**) |
| 7 | 005880 | 대한해운 | 0.62 | −0.13 | 🟡 | 분산 | +18.3 | −40.0 | 0.51 | −0.056 | 벌크/LNG |
| 8 | 003280 | 흥아해운 | 0.42 | +0.98 | **🟢** | 매집 | +34.4 | −46.8 | **1.57** | +0.224 | **케미컬탱커 (테마주)** |
| 9 | 089590 | 제주항공 | 0.35 | −0.33 | 🟡 | 분산 | +15.8 | −31.3 | 0.27 | 0.000 | LCC |
| 10 | 272450 | 진에어 | 0.27 | −0.33 | 🟡 | 분산 | +11.8 | −31.3 | 0.35 | 0.000 | LCC (**통합 LCC 존속**) |
| 11 | 091810 | 티웨이항공 | 0.27 | −0.56 | 🟡 | 분산 | +2.3 | −49.4 | 0.42 | +0.229 | LCC |
| 12 | 005430 | 한국공항 | 0.25 | +0.11 | 🟡 | 분산 | +22.2 | ★ **+31.3** | 1.20 | +0.061 | 지상조업 |
| 13 | 298690 | 에어부산 | 0.24 | +0.01 | 🟡 | 중립 | +17.4 | −37.4 | 0.71 | −0.128 | LCC (**피합병**) |
| 14 | 002320 | 한진 | 0.24 | −0.10 | 🟡 | 분산 | +17.7 | −30.7 | 0.82 | −0.017 | 택배/항만 |
| 15 | 004360 | 세방 | 0.24 | −0.23 | 🟡 | 분산 | +21.3 | −25.7 | 0.59 | +0.033 | 항만하역 |
| 16 | 000650 | 천일고속 | 0.23 | +0.33 | 🟡 | 매집 | +12.1 | −34.6 | **0.06** | +0.025 | 육상여객 |
| 17 | 044450 | KSS해운 | 0.22 | +0.23 | 🟡 | 중립 | +29.7 | −27.3 | 0.84 | **+0.332** | **가스/케미컬 탱커** |
| 18 | 009070 | 케이씨티시 | 0.12 | −0.05 | 🟡 | 분산 | +16.6 | −43.3 | 0.91 | +0.117 | 항만하역 |
| 19 | 004140 | 동방 | 0.09 | −0.12 | 🟡 | 중립 | +21.7 | −42.6 | 0.45 | +0.187 | 항만/중량물 |
| 20 | 009180 | 한솔로지스틱스 | 0.08 | +0.03 | 🟡 | 중립 | +24.4 | −18.5 | 0.59 | **+0.300** | 3PL |
| 21 | 084670 | 동양고속 | 0.08 | −0.58 | 🟡 | 분산 | +2.1 | −45.3 | **0.06** | +0.121 | 육상여객 |
| 22 | 129260 | 인터지스 | 0.06 | −0.21 | 🟡 | 분산 | +21.3 | −28.0 | 0.62 | +0.033 | 물류(동국) |
| 23 | 014130 | 한익스프레스 | 0.03 | +0.95 | **🟢** | 매집 | +34.5 | −25.0 | **2.09** | −0.022 | 화학물류 |
| 24 | 465770 | STX그린로지스 | 0.02 | +0.54 | 🟡 | 중립 | ★ **+105.3** | −39.0 | ★ **7.34** | **−0.456** | **해운 (테마주)** |

*🟢 for 011200/003490 = live `module_flow`; the JSON snapshot said 🟡 — see §1.

### Narrowing — and what the distribution says
1. **Concentration is total.** HMM + 대한항공 + 현대글로비스 = **₩42.1조 of ₩51.6조 (81.6%)**. There are
   **three** names ≥₩2조 outside those. **This is not a sector with breadth; it is two stocks and a tail.**
2. **The tail is uniformly broken.** **21 of 24 names carry a negative RS60**; the median RS60 is **≈ −31%**.
   The only positive RS60 in the entire sector is **한국공항 +31.3%** (ground handling, ₩0.25조).
3. **Every single name has a positive RS20** (+2.1 to +105.3). **In a −25.97%/1m index, a universally
   positive RS20 across 24 names is a defensiveness artifact, not 24 discoveries.**
4. **현대글로비스 is the sector's #2 by mcap and it is 분산 with flow −0.28** — the largest name that the
   "money is entering 운송·창고" story does not cover. It is the control that shows this is not sector flow.
5. **Volume is absent where the money is.** HMM 0.98×, 대한항공 0.97× — dead average. **The only 서지 >1.3×
   readings in the sector are 흥아해운 1.57×, 한익스프레스 2.09×, STX그린로지스 7.34×** — the three smallest
   or most theme-driven names. Per M-05's standing rule (*a story without 서지 is a story*), **the volume
   this sector produced today went to the ₩0.02–0.42조 테마주, not to the ₩18조 accumulation.**

**→ Narrowed set for the rest of this file: 011200 HMM · 003490 대한항공 · 028670 팬오션 (control) ·
003280 흥아해운 (negative control) · 020560·272450·298690 (the merger complex).**

**Handoff ledger** (`module_report_tags`, `DEGAJA_REPORT_DIR=llm_outputs`):
- **011200 HMM — 1 report only**: `2026-07-17/industry_KR/SECTOR_DEEP_ENRG.md` (CONFIRMED LIVE 🔴🟡). Essentially uncovered.
- **003490 대한항공 — ZERO reports. Never covered by this desk.** ₩9.56조 carrying the run's largest
  institutional print, and no prior desk work exists on it.

---

## §3 IR anchor — who does what, from primary filings

### 011200 HMM (`module_business 011200` — DART 사업보고서 「II. 사업의 내용」, 2026 누적 연결)
> *"당사는 컨테이너, 벌크(유조선/건화물선), 기타(터미널 등)의 사업부문을 영위하고 있으며, 2026년 누적 기준,
> 컨테이너 **585만 TEU** 및 벌크 **4,569만 MT** 등의 생산능력을 보유하였습니다."*

| 사업부문 | 품목 | 매출액 (백만원) | **비중** |
|---|---|---:|---:|
| **컨테이너** | 컨테이너 운송 | **9,243,368** | ★ **84.9%** |
| **벌크** | **유조선 + 건화물선** | **1,447,048** | **13.3%** |
| 기타 | 터미널 운영 등 | 201,027 | 1.8% |
| **합계** | | **10,891,443 (₩10.89조)** | 100.0% |

⚠ **Tool discrepancy recorded:** `module_business`'s derived "매출 분해" table renders these as
**6.96조 / 1.24조**, which does not reconcile with the raw filing table it printed immediately above
(₩9.24조 / ₩1.45조). **The raw filing figures are used throughout this file**; the module's parsed column
is treated as unreliable for HMM and should be checked before reuse.

★ **This single table settles hypotheses (i) and (ii) by size** — see §4.
Other primary anchors: 주요 매출처 = **얼라이언스 소속선사, GS칼텍스, 현대글로비스**. Structural note from
the same section: *"글로벌 상위 10개 해운선사 중 8개 선사는 해운동맹(얼라이언스)을 구성"* and
*"선박 건조에 장기간이 소요되고 자본 투입이 필요하여 **공급은 비탄력적**"* — **the inelastic-supply
statement is the company's own, and it is the mechanical basis for the bottleneck in §6.**

**Balance sheet** (yfinance, FY2025 asof 2025-12-31): cash+STI **₩13.35조**, total debt **₩5.19조** →
**net cash ₩8.16조**; 자본총계 **₩26.57조**; 총자산 ₩33.56조.
**Valuation** (`module_valuation 011200`, 07-21): 현재가 **20,100원** · 시총 **₩18.96조** · **PBR 0.68배**
(cross-check vs yfinance equity: 18.96/26.57 = **0.714** — the two agree to ~5%) · TTM PER 13.15 ·
**12M Fwd PER 13.0 (EPS 1,557원)** · 동일업종 PER 11.11 · 컨센 목표주가 22,700원 · 외국인 소진율 7.87% ·
배당수익률 3.48%.

### 011200 filings, 60d (`module_disclosure 011200 --days 60`) — 6건
| 일자 | 공시 | Read |
|---|---|---|
| **2026-07-09** | **풍문또는보도에대한해명(미확정)** | ★ **A rumour-clarification filing 12 days before this run, inside the 20d window.** Body **NOT obtained** — the module's detail parser returned `{}`, and a 21-day domestic news search on `HMM 매각 인수 합병 해명` returns **0 hits**. **P4: the subject of this filing is UNKNOWN and is left blank.** ⚠ It is the single largest unexamined object in this file |
| 2026-06-26 | 단일판매·공급계약 — **Mercuria Shipping Pte. Ltd., ₩3,118억** | Trading-house charter counterparty. Only 수주 in 60d |
| 2026-06-24 | 신규시설투자등 | Capex; amount not parsed |
| 2026-06-01 | 기업지배구조보고서 · 대규모기업집단현황 ×2 | Routine |

**No 자기주식, no 자본변동, no 지분변동, no 실적 filing in 60 days.** ⚠ **There is therefore NO filed
buyback, NO capital action and NO disclosed 5% holder change to explain HMM's institutional accumulation.**

### 003490 대한항공 (`module_business 003490` + `module_disclosure --business-report`, FY2025 별도)
- 영업수익 **₩16조 5,019억 (+2.4% YoY)** · 영업이익 **₩1조 5,393억 (−₩3,641억 YoY)**
- **여객 노선수익 ₩9조 8,447억** — 국제선 **₩9조 3,744억 = 95.2%**, 국내선 ₩4,703억 = 4.8%
- **화물 노선수익 ₩4조 4,093억 (−0.1% YoY)** · 화물기 **23대**, 여객기 142대, 33개국 96개 도시
- Revenue mix (filing table): 여객(국제) **56.8%** · **화물 26.7%** · 기타 8.9% · 항공우주 2.9%
- 항공우주: 군용기 MRO/U, **보잉·에어버스 날개/동체 구조물**, **대형 무인기 양산**
- ★ **원재료 매입 (단위: 천USD)** — **항공유 US$2,922,099천 (= $2.922B)** [GS칼텍스·Shell 외] +
  부품 US$798,924천 → **합계 US$3,721,023천 = $3.721B/yr of USD-denominated purchases**
- Company's own forward language: *"전자상거래 및 **AI 연관 산업**이 지속 성장하며 **항공화물 수요를 견인**"*

### 003490 filings, 60d — 25건, and **three of them are the story**
| 일자 | 공시 | Read |
|---|---|---|
| ★ **2026-07-13** | **영업(잠정)실적(공정공시)** | **A preliminary earnings print, dead centre of the 20d window.** Contents not in the filing parser — **but fully corroborated by news bodies**, §5 |
| ★ **2026-07-13** | **기업설명회(IR)개최 ×2 (same day)** | Two IR notices on the print date |
| ★ **2026-07-01** | **주식등의대량보유상황보고서(약식) — 국민연금공단** | ★ **A named institution filing on the name carrying 기관 +748.2만.** Direction/size not parsed — **blank** |
| 06-25 → 07-14 | **증권신고서(합병)** 정정제출요구(06-25·07-06) → [기재정정] 07-13 · **회사합병결정(종속회사)** 06-26·07-14 | ★ **A LIVE, twice-corrected merger registration.** See §4(iv) |

---

## §4 ★ THE VERDICT — testing the five candidates in the order ROTATION assigned

### (i) Tanker (VLCC) rates on a Middle East reroute — ❌ **RULED OUT, on two independent measurements**
1. **Size.** HMM's **벌크 부문 — which the filing defines as 유조선 AND 건화물선 combined — is 13.3% of
   revenue.** Tankers are a *fraction* of that 13.3%; the filing does not split them. **The container
   book is 84.9%.** For tanker rates to drive an ₩18.5조 mcap RS20 of +28.8%, they would have to move a
   revenue line that is at most one-eighth of the company, against 84.9% pulling the other way.
   **Arithmetically unavailable.**
2. **The pure-plays don't confirm.** If a tanker reroute were the bid, the KR tanker names would carry it.
   **They do not:** **KSS해운** (가스/케미컬 탱커) — 기관 **+2.1만**, 외국인 −11.7만, 혼조, 서지 0.84×;
   **흥아해운** (케미컬 탱커) — 외국인 **−229.8만**, 개인 **+227.2만**, short **building +0.17**.
   **Zero institutional accumulation in KR tankers.** The only tanker-adjacent buying is retail.
3. ⚠ **The one fact that superficially supports (i), and why it does not survive:** 해수부 issued a
   **second Red Sea avoidance advisory** to domestic carriers — *"유조선·필수선박은 제외"* —
   *"'단순 통과를 위한 진입'을 자제"* [mk 07-20, 단독]. **Tankers are EXEMPTED from the advisory; container
   ships and bulkers are the ones told to reroute.** That is a *cost/routing* event for HMM's container
   book, not a tanker-rate windfall. **(i) is dead.**

### (ii) Dry bulk (BDI) — ❌ **RULED OUT as HMM's driver; ✅ ALIVE as a separate, smaller lane**
- Same 13.3% ceiling as (i), shared with tankers. **Cannot drive HMM.**
- **But 팬오션 (₩2.81조, pure dry bulk) has its own genuine institutional bid**: 외국인 **+97.7만** /
  기관 **+340.2만** / 개인 −429.6만, RS20 **+27.9%**, and a **07-21 broker target raise** —
  *"[클릭 e종목] **이익 다변화 기대되는 팬오션, 목표가↑**"* [asiae 07-21]. ⚠ **Headline-level only** — the
  retrieved body was related-link boilerplate with no substance; **the note's numbers are blank.**
- ⚠ **And 팬오션 closed −0.60% on the Houthi blockade headline** [yonhap 07-21] while OBV is **중립** and
  서지 **0.53×** (half-normal volume). **Institutional buying with no volume and no headline response.**
- **Verdict: (ii) is not the HMM answer. 팬오션 is logged as an independent watch item with a named blank
  (the 07-21 note's contents), NOT as evidence for HMM and NOT as a BET candidate.**

### (iii) NAV / valuation rerate — ⚠ **REAL, but it is an AMPLIFIER, not the TRIGGER**
- **Net cash ₩8.16조 = 43.0% of the ₩18.96조 market cap.** **PBR 0.68–0.71.**
- **EV = ₩10.80조.** Against the consensus FY OP *"₩2조에 근접"* → **EV/OP ≈ 5.4×.**
- ★ **This is why the earnings revision has such leverage: every ₩1조 of OP revision moves ~9.3% of EV.**
- ❌ **But it cannot be the trigger.** Net cash and a sub-book PBR are **standing facts** — they were true
  in January. **A standing fact does not produce a 20-day accumulation.** And HMM is **not cheap on
  earnings**: **Fwd PER 13.0 / TTM 13.15 vs 동일업종 PER 11.11** — it trades at an **18% premium** to its
  sector on earnings while at a discount on assets. **A "cheap stock" story does not survive that pair.**
- **Verdict: (iii) explains the SIZE of the move once a revision starts. It does not explain the START.**

### (iv) Index / passive flow — ❌ **NOT SUPPORTED for HMM; ⚠ REAL but for the WRONG NAME**
- **HMM: no supporting observable.** **서지 0.98×** — a rebalance or ETF inclusion prints as a *volume*
  event, and there is none. **No 자본변동/지분변동/자기주식 filing in 60 days.** Foreign 소진율 only 7.87%.
  ⚠ **I did not have an index-calendar source** (no MSCI/FTSE/KRX review data on hand) — **so this is
  "no positive evidence found", not a proof of absence. Blank stays blank.**
- ★ **BUT the mechanism is live on 대한항공 instead, and nobody named it:** a **증권신고서(합병)** filed
  06-25, **rejected twice by the regulator** (정정제출요구 06-25 and 07-06) and **refiled 07-13**, plus
  **회사합병결정(종속회사)** 06-26/07-14. Corroborated in the tape: *"12월 한가족 되는 대한항공·아시아나항공"*
  [mt 07-10], *"통합 대한항공, 마일리지는 따로?…독과점 우려 해소해야"* [yonhap 07-15].
  **A merger share issuance is an index-weight and arbitrage event.** Consistent with 아시아나항공's
  **Δ +0.154** and 에어부산 −0.128 / 진에어 (통합 LCC 존속법인) flat. ⚠ **I did not obtain the merger ratio
  or the new share count** — the filings' details were not parsed. **Left blank. This is a named,
  testable lead for the next run, not a conclusion.**

### (v) ★ Something else — ✅ **THIS IS THE ANSWER: an already-booked freight LEVEL + a lagged earnings revision**

**The mechanism, entirely from body-reads inside the accumulation window:**

> ***"운임 상승에 HMM 실적 기대감 '쑥'…성수기 선반영 변수"*** [mt, **2026-07-07**]
> — *"HMM의 2분기 영업이익 컨센서스는 **3400억원** 수준… 실현된다면 전년 동기 대비 **46% 증가**한 수준"*
> — *"2분기 평균 상하이컨테이너운임지수(SCFI)는 **2336포인트**… 지난해 같은 기간보다 **42%**, 올해 1분기보다
>   **55%** 오른 수준. 지난 3일 기준 SCFI는 **3327포인트**까지 뛰며 2024년 홍해 통항 중단 당시 기록한
>   **3733포인트**에 가까워졌다"*
> — ★ *"**컨테이너선 운임은 계약 구조상 실제 실적에 반영되기까지 일정한 시차가 있다.** 이 때문에 2분기보다
>   **3분기 실적 개선 폭이 더 클 수 있다**… 3분기 영업이익 컨센서스는 **9000억원을 웃돈다**. 연간 영업이익도
>   **2조원에 근접**할 것으로 전망된다"*
> — Drivers named: **홍해·중동 긴장** AND ★ **미국 관세 회피 pull-forward** (*"기업들이 관세 부담이 커지기
>   전에 제품을 미리 보내려 하면서 선적 수요가 앞당겨졌고"*). Corroborated globally: *"세계 2위 컨테이너선사
>   **머스크가 최근 영업이익 전망치를 상향**"*.

**Now re-read CARD 8's own source with the level in hand:**
> ***"컨 운임지수 2주 연속 하락…'일부 원양항로 선복 확대 영향'"*** [donga, **2026-07-21**]
> — *"20일 기준 **KCCI는 전주보다 114포인트(2.6%) 내린 4204**"*
> — *"**SCFI도 전주보다 104.51포인트(3.3%) 내린 3080.31**"*
> — ★ *"해진공은 **미주 서안과 남미 항로 등 일부 원양항로의 선복 추가 투입**으로 수급 여건이 완화되면서
>   종합 운임지수 하락을 이끈 것으로 분석"*
> — ★ *"**미주 동안과 중동 항로는 운항 제약과 지정학적 위험이 지속되면서 상대적으로 높은 운임 수준을 유지**"*

**Three things CARD 8 could not see because it read the direction and not the body's numbers:**
1. **3,080.31 is +31.9% above the 2Q average of 2,336** that produced the +46% YoY print. The decline is
   **−7.4% from the 07-03 spike of 3,327** and leaves the index **−17.5% from the 2024 blockade peak** —
   i.e. **still in the top decile of the last three years.** A fall from a near-record to a very-high level
   does not falsify an earnings revision computed off a *much lower* average.
2. **The lag is explicit and it runs the desk's way.** Container freight books to P&L with a contractual
   delay; **3Q consensus is 2.65× 2Q.** The money accumulating in July is positioned for a print that
   reflects **Q2's 2,336 and July's 3,000+**, not this week's tick.
3. **The cause of the decline is capacity added on 미주 서안/남미 — not the Middle East easing.** The same
   article says **미주 동안·중동 항로 remain elevated** and **중동 항로 will stay volatile until Hormuz
   transit is confirmed stable.** The geopolitical leg CARD 8 thought had failed **is explicitly still on.**

**★ And the free negative control the market ran today, which settles what this is NOT:**
> ***"[특징주] '후티 홍해차단'에 해운주 반짝 급등후 상승분 반납(종합)"*** [yonhap, **07-21 16:08**]
> — 후티 반군이 **사우디에 대한 해상 봉쇄를 선언**; 로이터: 바브엘만데브 차단 시 **세계 원유 공급 최대 7% 감소**
> — **흥아해운 개장 직후 +16.97% (2,130원) → 종가 +2.69% (1,870원)**
> — **STX그린로지스 한때 +27.29% → 종가 −3.62% (3,990원)**
> — **대한해운 −1.27%, 팬오션 −0.60%** — 여타 해운주 **약세로 마감**
> — *"두 종목은 올해 들어 중동 지정학적 위기가 고조될 때마다 주가가 들썩이는 **테마주 양상**"*
> — **HMM is not mentioned in either the 10:05 or the 16:08 article.**

**On the day of the maximal Red Sea headline, the Red Sea trade round-tripped inside one session, it was
carried entirely by two names totalling ₩0.44조 that the wire itself calls 테마주, and HMM did not
participate.** Combined with the earlier measurement that `홍해·해상운임·컨테이너운임·봉쇄` returns only
**3 hits in 4 days** on the domestic feed [EVENT_ALPHA CARD 8], the conclusion is firm:

> ### ★★ VERDICT: What is buying HMM
> **An earnings revision, not a headline.** Foreign+institutional money (기관 +303.9만, 외국인 +21.9만,
> 개인 −328.8만) is positioned for a **3Q OP consensus of >₩9,000억 (2.65× 2Q) and an FY approaching ₩2조**,
> which is computed off a **2Q SCFI average of 2,336 that is already booked** and a **July level still
> +31.9% above it**, and which is **geared 5.4× on EV** because **43% of the market cap is net cash**.
> **The freight rate is the driver — the LEVEL and its BOOKING LAG, not the weekly print.**
> **RULED OUT: (i) tanker · (ii) dry bulk · (iv) index flow.** **(iii) is the amplifier, not the trigger.**
> **CARD 8 was right that this is not a Red Sea trade and wrong that it is not a freight trade.**
>
> ⚠ **Residual unknowns, stated rather than papered over:**
> **(a)** The **07-09 풍문·보도 해명공시** body is **not obtained** and returns 0 news hits — an undisclosed
> corporate event inside the window remains possible. **(b)** HMM's chart is **NEUTRAL/CHOP with RSI 71.1
> and 서지 0.98×** — *no volume has confirmed this*, and per M-05 that is a caution, not a green light.
> **(c)** The industry names its own decay: *"성수기 물량이 앞당겨진 만큼 **8~9월 물동량은 다른 해보다 약할
> 수 있다**"* and *"신조선 인도에 따른 **선복 공급 부담은 여전히 남아 있다**"* [mt 07-07] — **the pull-forward
> that created the revision is borrowed from Q3/Q4 demand.**

---

## §5 ★ 대한항공 — the FX hypothesis, CONFIRMED-OR-REFUTED

**REFUTED. Twice over: on magnitude, and on sign.**

### (a) Magnitude — fuel dominates FX by ~2.2×, from the filing's own USD purchase line
Primary input (사업보고서 「3. 원재료」, **단위: 천USD**): **항공유 US$2,922,099천** + 부품 US$798,924천
= **US$3,721,023천/yr**. At 1,475.28원 that is **₩5.49조 of USD-denominated purchases**, of which
**fuel alone = ₩4.31조 = 26.1% of FY25 별도 영업수익 (₩16.50조)**.

| Leg | Move (1m, asof 07-21) | Annualised won impact | Derivation |
|---|---|---:|---|
| **FX tailwind** on USD costs | KRW=X **−3.66%/1m** | **+₩2,009억** | $3.721B × 1,475.28 × 3.66% |
| **Fuel headwind** (WTI) | CL=F **+10.05%/1m** | **−₩4,332억** | $2.922B × 1,475.28 × 10.05% |
| **Fuel headwind** (Brent) | BZ=F **+14.17%/1m** | **−₩6,109억** | $2.922B × 1,475.28 × 14.17% |
| **Net (WTI basis)** | | ★ **−₩2,323억** | fuel beats FX **2.16×** |

### (b) ★ Sign — on the operating line, a stronger won is NET NEGATIVE for 대한항공
KAL's **FX-linked revenue** (국제선 여객 ₩9.37조 + 화물 ₩4.41조 = **₩13.78조**) is **2.5× its USD purchases
(₩5.49조)**. A 3.66% won appreciation therefore **deflates ~₩5,045억 of revenue to save ~₩2,009억 of cost**
→ **net operating FX effect ≈ −₩3,036억/yr.** ★ **And the sell-side says the same thing in words:**
> *"여객 부문은 유류 할증료 인상으로 아웃바운드 수요가 둔화했지만, 외항사 공급 감소에 따른 환승 수요와
> **원화 약세에 따른 인바운드 수요**가 이를 보완했다"* — 최민기, 신한투자증권 [yonhap, 07-15]

**The broker credits won WEAKNESS for the passenger support. The desk's hypothesis assumed won STRENGTH
was the tailwind. The sign is not merely unproven — it is disputed by the only analyst in the window who
addresses it.** ⚠ *Caveat stated: KAL's international revenue is multi-currency (USD/JPY/EUR/CNY) and
Korea-origin tickets are sold in KRW, so ₩13.78조 is an **upper bound** on FX-linked revenue. The
**balance-sheet** leg (USD lease liabilities / aircraft debt revaluation) is where won strength genuinely
helps — **but I could not size it: no FX sensitivity or 외화순부채 disclosure exists in the 「사업의 내용」
section, and I did not obtain the 재무제표 주석. That number stays blank.*** ⚠ Against it: the 07-13 print
**went to a quarterly NET LOSS** (*"분기순이익은 '적자 전환'"* [chosun 07-13]) — i.e. **the below-the-line
in the reported quarter was a negative, not an FX rescue.**

### (c) ★ So what IS buying 대한항공: **AI air cargo** — three independent sources inside the window
> ***"한국·대만 화물기 가득 채우는 AI 반도체…운임도 4년來 최고치"*** [mk, **07-16**, Bloomberg 분석 인용]
> — **대한항공 2Q 화물 매출 $1.03B (₩1조 4,800억), 전분기 $744.23M 대비 +38.4%**
> — 중화항공 **+43.6%**, 에바항공 **+44%** — *"양국 항공사 화물사업 매출 **모두 약 40% 급등**"*
> — **화물 매출 비중: 대한항공 30.7% (+4.2%p YoY)**, 중화항공 43.5%, 에바항공 30.3%
> — ★ *"**TAC 인덱스** 공식 화물 운임 데이터에 따르면 **홍콩·서울·대만발 미국행** 주요 항공화물 노선의 운임은
>   최근 몇 주 사이 **2022년 이후 최고 수준**까지 상승"*
> — 대한항공: *"글로벌 AI 투자 덕분에 **화물 매출이 50% 가까이 급증**"*; 에바항공: *"대만발 미국행 항공화물의
>   **40~50%가 AI 서버 관련**"*
> — ★ **BofA: *"AI 관련 화물이 아태 지역의 다른 화물을 대체… 항공사 화물 사업이 여객 사업과 달리 항공유
>   비용 상승분을 **완전히 만회**"*** · 네이선 지(BofA 아태 운송 리서치 총괄): *"**2027년까지** 항공화물 시장
>   펀더멘털을 낙관… **AI 슈퍼사이클**과 견조한 전자상거래 물동량, 공급 부족에 따른 강력한 가격 결정력"*

Corroborating, both **dated inside the 20d window**:
- **하나증권 07-14** — 목표가 38,000 → **41,000원 (+7.9%)**: *"프리미엄 항공 수요와 항공화물 수요의
  **비탄력성**을 확인… **내년 영업이익은 연결 기준 2조3000억원까지 증가**"* [mt 07-14]
- **신한투자증권 07-15** — 목표가 35,000 → **38,000원**: *"**화물 운임 추정치를 높이고 유류비 가정을 낮춰**
  목표주가를 상향"*; *"제트유 가격 하락 폭보다 **항공화물 운임 하락 폭이 크지 않아** 하반기 화물 실적 전망을
  높일 필요"*; **아시아나 합병 효과 → 기업가치 재평가** [yonhap 07-15]
- The company's own 07-13 print: **2Q 별도 매출 ₩5조 199억 (+25.9% YoY) — 역대 최대**; 영업이익 **₩2,618억
  (−34% YoY)**; **순이익 적자전환** [mt/sedaily/donga/chosun 07-13, 4 outlets]
- **"기름값 1조 늘자…대한항공, '못 줄이던 국내선' 손댔다"** [mt 07-19] — the fuel bill rose **₩1조**
- **"같은 항공주인데…올해 들어 대한항공만 주가 26% 뛴 이유"** [hankyung 07-08] — ⚠ headline-level only,
  body not read; recorded as the dispersion marker, not as evidence

### (d) ★ Why the FX correlation looked real — it is a **common cause**, not a link
MACRO §1 attributes the won's move to *"**record semiconductor export print**"* (*"원화 국제화"*-independent),
and 반도체 수출 through 07-20 is **$22.1B, 역대 최대 재경신** [asiae headline, 07-21 — ⚠ related-link
headline, body not read]. **The same semiconductor export surge that firmed the won is the cargo that
fills 대한항공's freighters.** FX and KAL are **siblings, not parent and child.** Trading KAL as an FX proxy
buys the correlation and misses the driver — and, per (b), **gets the sign wrong on the operating line.**

> ### ★★ VERDICT: 대한항공 is an **AI-air-cargo trade**, not an FX trade — and not cleanly a "fuel victim" either
> **FX: refuted** (fuel beats it 2.16×; net operating FX effect −₩3,036억/yr; the in-window broker credits
> won *weakness*). **Fuel: a confirmed COST that cut OP −34% and the quarter to a net loss — but it is
> passed through** on both sides (§6 node 6) and BofA measures the cargo leg as **fully offsetting** it.
> **The 라이언에어 −34% analogy does not transfer**: Ryanair is ~100% short-haul passenger with no cargo
> book; **KAL is 26.7% cargo, and that is the segment that grew 38.4% QoQ.**
> ⚠ **But the money and the price disagree**: 기관 **+748.2만** (largest print on the board) against a chart
> reading **OBV 분배 (−47% slope), 약세 다이버전스, RSI 34.9, 하단밴드, 모멘텀20d −2.1%.** **The institution
> is buying a stock that is not going up.** That is either early accumulation or an index/merger mechanic
> (§4(iv)) — **and this file cannot distinguish them.** Stated as unresolved.

---

## §6 Value chain — 7 nodes, left → right, with the binding constraint marked

```
[1] 화주 수요          [2] 지정학·항로        [3] 선복/기재 공급    [4] 운임 지수        [5] 캐리어 P&L
    ── AI 서버·반도체 ──▶  ── 홍해·호르무즈 ──▶  ── 신조선 인도    ──▶  SCFI 3,080 ────▶  HMM  3Q OP >9,000억
       (수출 $22.1B/7월      해수부 통항자제        (탱커 제외)         KCCI 4,204          EV/OP 5.4×
        관세 pull-forward)   2차 권고 07-20         화물기 3대 증편      TAC 2022년來 최고    KAL  화물 +38.4%QoQ
                                                                                            │
                             ┌──────────────────────────────────────────────────────────────┘
                             ▼
                      [6] 가격 전가 장치            [7] 최종 수요 반응
                      ── 유류할증료 33→14단계 ──▶  ── 운수업 카드승인 4월 −10.9%
                         (규제 테이블, ~2개월 시차)     5월 −14.2% → 8월 인하로 회복 기대
                         컨테이너 계약 시차             아웃바운드 탄력성
```

### ★ The binding constraint is **node [3] 선복/기재 공급** — and it is binding in BOTH directions
**Why [3] and not [1] or [2]:** demand is strong (node 1) and geopolitics is loud (node 2), but
**strong demand is not a bottleneck.** The company's own filing states the constraint mechanically:
> *"선박 건조에 장기간이 소요되고 자본 투입이 필요하여 **공급은 비탄력적**… 수급불균형에 따른 **주기적 호·불황**"*
> — HMM 사업보고서 「II. 사업의 내용」

**And the tape shows [3] binding in real time, in both directions on the same day:**
- **RELAXING (bearish):** the SCFI/KCCI fall is attributed *only* to supply — *"**미주 서안과 남미 항로 등
  일부 원양항로의 선복 추가 투입**으로 수급 여건이 완화"* [donga 07-21]. **Capacity, not demand, is what
  broke the rate.**
- **TIGHTENING (bullish):** *"**미주 동안과 중동 항로는 운항 제약**과 지정학적 위험이 지속되면서 상대적으로
  **높은 운임 수준을 유지**"* [donga 07-21]; and in air, *"**공급 부족**에 따른 강력한 가격 결정력"* (BofA),
  with 에바항공 needing until **2028** to add 3 freighters [mk 07-16].
- **The overhang:** *"**신조선 인도에 따른 선복 공급 부담은 여전히 남아 있다**"* [mt 07-07].

**→ Every KPI and anti-signal in §8/§9 is written as an observable on node [3] or on node [6], because
those are the only two nodes where the outcome is actually decided.** Nodes [1] and [2] generate headlines
that the market demonstrably round-trips (§4(v)).

**Cross-sector chain — and it is the one this desk did not have:**
> **AI capex → 반도체/AI 서버 출하 → 항공화물 (KAL 화물 30.7%, TAC 2022년來 최고) → 운송·창고**

**TRAN's largest institutional print is downstream of the IT axis that MACRO holds Neutral and that
EVENT_ALPHA CARD 3 marked STORY-ONLY.** ★ **This is a chain the desk has been carrying only on its
upstream end.** ⚠ It cuts both ways: it means **대한항공 is not a diversifier against an AI-capex
disappointment — it is a second expression of the same bet**, exactly as SWEEP warned HMM was a second
expression of M-02's oil bet. **Two names, one sector, both correlated to positions the desk already holds.**

**Node [6] is the second-most important and the most under-appreciated** — see §8.

---

## §7 Chain-hop candidates — body-proximate only, flow cross-checked

**Rule applied: a news co-mention is NOT a candidate. Every name below was surfaced from a BODY, then
cross-checked against `module_flow` BEFORE being listed. Names failing the flow check are shown failing.**

| Candidate | Body proximity (source) | Flow cross-check | **Gate** |
|---|---|---|---|
| **028670 팬오션** | Named in the 07-21 shipping-tape body [yonhap] and in a 07-21 broker target raise [asiae, **body blank**] | 기관 **+340.2만**, 외국인 **+97.7만**, 개인 −429.6만, RS20 +27.9% ✅ — **but** OBV 중립, **서지 0.53×**, closed **−0.60%** on the max headline | ⚠ **WATCH ONLY.** Real institutional flow, **zero volume and zero headline response**. Broker note's contents are **blank**. **Does NOT reach BET** |
| **005430 한국공항** (지상조업) | ❌ **Not body-named.** Surfaced from flow only | ★ **The sector's ONLY positive RS60 (+31.3%)**, 서지 1.20× — **but OBV 분산 (−0.40)** and mcap ₩0.25조 | ❌ **FAILS the body-proximity rule.** Logged as an anomaly for the next run, **not a candidate** |
| **020560 아시아나항공** | Body-named in the merger complex [mt 07-10, yonhap 07-15] and in KAL's own 증권신고서(합병) | Δ **+0.154**, RS20 +22.9%, **but flow −0.09, OBV 분산** | ❌ **Merger-mechanical, not fundamental.** Terminal security in a live, twice-corrected registration. **Not a candidate — a risk note** |
| **003280 흥아해운 · 465770 STX그린로지스** | Body-named [yonhap 07-21] — ★ **explicitly as 테마주** | 흥아 외국인 **−229.8만** / 개인 **+227.2만**, short **building +0.17**; STX Δ **−0.456**, 서지 **7.34×** | ❌ **EXCLUDED BY FLOW.** The wire calls them theme stocks and the KIS actuals confirm retail absorption. **This is the row the flow cross-check exists for** |
| **010140 삼성중공업 · 042660 한화오션 · 009540 HD한국조선해양** | Body-named as the tanker/LNG newbuild beneficiaries of *"글로벌 해운 대란"* [sedaily 07-18] | ❌ **Not cross-checked here** | ❌ **OUT OF SECTOR + already owned by EVENT_ALPHA CARD 1 (dated 07-24 binary, 한화오션 short 1.44% building).** Deliberately not re-opened — **it belongs to INDU, and double-counting it here would manufacture breadth** |

**★ Net: ZERO chain-hop candidates clear the gate to BET.** One (팬오션) is logged as WATCH with a named
blank. **The sector's genuine "hop" is not a stock at all — it is the AI-capex → air-cargo link in §6,
which lands back on 대한항공 itself and on names the desk already holds.**

---

## §8 Track KPIs — observables, with sources and cadence

| # | KPI | Now (asof) | Where it prints | Why it decides |
|---|---|---|---|---|
| **1** | ★ **SCFI level vs 2,336** (NOT direction) | **3,080.31 (07-20) = +31.9%** | 해진공 주간, 매주 화 국내 보도 | **The entire HMM thesis is "level > booked average". Sub-2,336 removes the revision, not a down week** |
| **2** | **KCCI (한국발)** | **4,204 (07-20), −2.6% wow** | 해진공 주간 | KR-origin proxy; HMM's own trade lane |
| **3** | ★ **HMM 3Q OP consensus** | **>₩9,000억** (FY ≈ ₩2조) | 에프앤가이드; **3Q 잠정실적 ~10월** | **The revision IS the thesis. A cut here is the thesis, cut** |
| **4** | ★ **유류할증료 단계** | 3월 **6** → 5월 **33 (제도 도입 최고)** → 6월 27 → 7월 **19** → **8월 14 (−25%)** | 대한항공 월중 발표 (~매월 16일) | **Node [6]. The demand throttle AND the fuel pass-through — the single most informative monthly number for the airline leg** |
| **5** | ★ **TAC index 서울→美 항공화물 운임** | **2022년 이후 최고 수준** (07-16) | TAC Index; Bloomberg/mk 인용 | **The 대한항공 driver. Not the won** |
| **6** | **대한항공 화물 매출 비중** | **30.7% (2Q), +4.2%p YoY**; 매출 **$1.03B, +38.4% QoQ** | 분기 실적 (3Q ~10월) | Whether the AI-cargo mix keeps expanding |
| **7** | **운수업 카드 승인액 YoY** | 4월 **−10.9%**, 5월 **−14.2%** (유일한 감소 업종) | 여신금융협회 월간 | **Node [7]: does the 8월 surcharge cut actually revive outbound?** |
| **8** | **HMM 공매도 %float + direction** | **1.05%, covering (−0.13) ⚠주목** | KRX 일간 | Covering into accumulation = confirmation; a flip to building = the other side arrived |
| **9** | **HMM 서지** | **0.98× — NOT confirmed** | `module_flow` 일간 | **M-05: no volume, no confirmation.** The revision has not been bought loudly yet |
| **10** | **HMM chart trigger** | **close > 20,284 + OBV→누적** (stop 18,310) | `module_chart --read` | The desk's own stated ignition line; **currently 20,100 = unbroken** |
| **11** | **대한항공 OBV conflict** | flow **매집** vs chart **분산 (−47%)** | both, daily | **Whichever resolves first tells you if 기관 +748.2만 was early or mechanical** |
| **12** | **KAL–아시아나 합병 신고서 효력** | 06-25 제출 → 정정요구 ×2 → **07-13 재제출**; 통합 **12월** | DART | Merger ratio + new share count = the §4(iv) index leg. **Both currently blank** |
| **13** | **반도체 수출 (일별·순별)** | 7월 20일까지 **$22.1B, 역대 최대** ⚠headline-only | 관세청 순별 | **Upstream of node [1] for the air-cargo leg** |

---

## §9 Anti-signals — stated as observables, each with a threshold

| # | Anti-signal (observable) | Threshold that kills it | Status 07-21 |
|---|---|---|---|
| **A1** | ★ **SCFI falls THROUGH the 2Q average** | **SCFI < 2,336** — *not* "SCFI falls" | **3,080.31 = +31.9% above.** ⚠ At −3.3%/wk it takes **~9 weeks** to breach → **first plausible breach ≈ 2026-09-22** |
| **A2** | ★ **The pull-forward reverses.** Industry's own words: *"성수기 물량이 앞당겨진 만큼 **8~9월 물동량은 다른 해보다 약할 수 있다**"* [mt 07-07] | 8~9월 물동량 YoY negative, or a 3Q OP consensus cut | ⚠ **Undated and unmeasured — the desk has no volume series.** **The largest known blind spot in this file** |
| **A3** | ★ **신조선 인도** — *"선복 공급 부담은 여전히 남아 있다"* [mt 07-07]; already visible as *"미주 서안·남미 **선복 추가 투입**"* [donga 07-21] | The 선복-driven decline spreads from 미주서안/남미 to **미주 동안·중동** (the lanes still elevated) | ⚠ **ACTIVE AND ALREADY FIRING on two lanes.** This is the mechanism actually breaking the rate |
| **A4** | ★ **TACO / ceasefire.** Same trigger as M-02 — **HMM is a SECOND expression of the oil bet, not a hedge** (SWEEP §3, restated and confirmed) | Ceasefire signature; Hormuz transit confirmed stable (해진공's own stated condition) | ⚠ Live: US desk carries a 10-day ceasefire proposal; ⚠ **but 07-16 reports the truce "흔들" and 공습 재개** — currently pointing the other way |
| **A5** | ★★ **The market refuses to pay for the Red Sea headline** | A max headline produces an intraday spike that fully round-trips | ★ **ALREADY FIRED, TODAY.** 흥아해운 +16.97%→+2.69%, STX +27.29%→−3.62%, 팬오션 −0.60%, 대한해운 −1.27% [yonhap 07-21]. **The geopolitical premium is being sold, not bought** |
| **A6** | **HMM's revision is not volume-confirmed** | 서지 stays <1.3× while RS20 decays | **서지 0.98×, RSI 71.1, NEUTRAL/CHOP.** ⚠ **RSI 71 with no volume is a fade setup, not an ignition** |
| **A7** | ★ **대한항공: the chart says distribution** | `module_chart` OBV 분산 persists / 다이버전스 widens / close < 25,350 | ⚠ **FIRING NOW: 분산 −47% slope, 약세 다이버전스, RSI 34.9, 하단밴드, 모멘텀20d −2.1%** |
| **A8** | ★ **9월 유류할증료 RE-RISES** — the 3-month relief ends | 9월 단계 > 8월's 14단계 | ⚠ **POINTING THAT WAY: BZ=F +14.17%/1m, 브렌트 $85 초과 on 07-16, 종전합의 흔들·공습 재개.** *"9월에도 하락세가 이어질지는 불투명"* [mt 07-16]. **The 8월 cut may be the last one** |
| **A9** | **AI-cargo is the same bet as the desk's IT/AI exposure** | An AI-capex disappointment (M-03's kill-switch, **already firing** per MACRO §4a) | ⚠ **Structural, not dated. 대한항공 is NOT a diversifier** |
| **A10** | ★ **The 07-09 해명공시 turns out to be material** | Any follow-on filing or news naming its subject | ⚠ **UNKNOWN. Body not obtained, 0 news hits.** Explicitly carried as an unexamined risk |
| **A11** | **Merger dilution / arbitrage pressure on 대한항공** | 합병 신고서 효력 발생 + 신주 발행 규모 | ⚠ **Blank — ratio and share count not obtained.** A third rejection would itself be the signal |

---

## §10 → Hand-off

### ★ To BET: **NOTHING.** Neither name is forwarded, and this is a positive decision, not an omission.

**011200 HMM — thesis EXPLAINED, but not BET-ready.** The question ROTATION asked is answered and the
mechanism is measured (§4(v)). But **three of the desk's own standing rules block it**:
1. **M-05 — a story without 서지 is a story.** **0.98×.** The revision has not been bought with volume.
2. **The chart engine says NEUTRAL/CHOP at RSI 71.1**, below its own stated trigger (**close > 20,284**;
   last 20,100). **Buying an unconfirmed RS20 at RSI 71 in a −25.97%/1m index is a fade setup.**
3. **SWEEP's concentration warning survives intact and is now confirmed: HMM is a second expression of
   M-02's oil/Middle-East bet** (A4), and the desk already holds 096770·010950·475150 as **one driver**.
   **Adding HMM would be adding a fourth unit to a bet already flagged for concentration.**
   ⚠ Plus **A10**: an unexamined rumour-clarification filing sits inside the accumulation window.

**003490 대한항공 — driver identified, but the internal evidence CONFLICTS.** The largest institutional
print on the board sits on a name whose **chart engine reads distribution with a bearish divergence at
RSI 34.9**, and whose flow module reads accumulation. **Two of the desk's own tools disagree about what
the money is doing.** Until that resolves, forwarding it would be forwarding a coin flip with a story
attached. **A8 (9월 유류할증료 re-rise) and A11 (merger dilution) are both live and both unsized.**

### ★ To ROTATION / next run — what this file changes
1. ★ **CARD 8's kill is OVERTURNED IN PART, and the reason is method, not data.** The SCFI fact was
   correct; the inference from *direction* to *thesis* was not. **A rate index needs a LEVEL vs the
   booked average and a KNOWN BOOKING LAG before a 2-week move can falsify an earnings-driven bid.**
   Proposed standing rule: ***when a commodity/rate index is the mechanism, always read the level against
   the period average already in the P&L, and always ask where the contract lag puts it.***
2. ★ **CARD 8's kill is UPHELD in full on the Red Sea leg** — and today's tape (A5) is the cleanest
   confirmation the desk will get. **운송·창고 must not be carried as a geopolitical/Red Sea lane.**
3. ★ **TRAN's real identity is a DOWNSTREAM AI-CAPEX lane**, not a shipping lane. **대한항공's cargo book
   (30.7%, +38.4% QoQ, TAC 4-year high) belongs to the AI axis MACRO holds Neutral.** ⚠ **It is therefore
   correlated with existing exposure, not diversifying — the same warning SWEEP issued about HMM/oil.**
4. ★ **The "2🟢/0🔴" that promoted this sector was two micro-caps totalling ₩0.45조**, one of which is
   a **retail-absorbed 테마주** (외국인 −229.8만 / 개인 +227.2만). **The rule-(b) promote was justified by
   the ₩10조+ institutional prints, not by the green count — the green count was noise.**
5. **Carried forward as named blanks (P4):** HMM **07-09 풍문·보도 해명공시** body · **국민연금 07-01
   대량보유 direction/size** · **합병비율 + 신주 발행 규모** · **KAL 외화순부채 / FX 민감도** · **팬오션
   07-21 목표가 note contents** · **8~9월 물동량 series (A2)**.
6. **Tooling, for the unit:** ⚠ `module_business`'s parsed 매출 table for 011200 **does not reconcile**
   with the raw filing table it prints (6.96조/1.24조 vs 9.24조/1.45조) — **use the raw table.**
   ⚠ `module_flow` (live, KIS-gated) and `SECTOR_FLOW_KR.json` (snapshot) **disagree on tags for 3 of 6
   names** — the live run is operative. ⚠ `module_flow` and `module_chart` **disagree on 대한항공's OBV**;
   neither was discarded. ⚠ `.KS` suffix confirmed mandatory again.

---

## ✅ EXIT CHECK
- [x] **Full fresh map** — rotating sector, never previously deep-dived; no prior file referenced by
      inheritance. **All 24 sector names listed** (§2) from `SECTOR_FLOW_KR.json`, then narrowed to 7 with
      stated criteria (concentration 81.6%, RS60 distribution, 서지 location).
- [x] **flow → players → IR → chain map(+chain-hop) → bottleneck/KPI/anti-signal** — §1→§9, in order.
      **CHART_READ embedded VERBATIM for both names** (§1), including the 대한항공 conflict it exposed.
- [x] **IR anchor from PRIMARY filings** — HMM 사업보고서 segment table (**컨테이너 84.9% / 벌크 13.3%**,
      the number that kills hypotheses (i)+(ii)); KAL 원재료 table (**항공유 US$2.922B**, the number that
      sizes fuel-vs-FX); DART 60d lists for both, with the **07-09 해명공시** and the **07-13 잠정실적 +
      IR ×2 + 국민연금 07-01** surfaced from the filing list rather than from news.
- [x] **7-node value chain left→right with the bottleneck marked as a BINDING CONSTRAINT** (§6) — node [3]
      선복/기재 공급, justified by the issuer's own inelastic-supply language and shown **binding in both
      directions on the same day**. **Cross-sector chain marked** (AI capex → 반도체 → 항공화물 → TRAN),
      including the warning that it is **correlated with existing desk exposure, not diversifying**.
- [x] **Chain-hop candidates body-proximate only and flow cross-checked BEFORE any could reach BET** (§7).
      **Five rows, ZERO cleared to BET**; 흥아해운/STX **excluded by the flow check** exactly as the rule
      intends; 한국공항 **excluded for failing body-proximity** despite the sector's best RS60.
- [x] **Anti-signals stated as OBSERVABLES with thresholds** (§9) — 11 rows, **three already firing**
      (A5 today's round-trip, A7 KAL distribution, A3 선복 투입), one dated (**A1 ≈ 09-22 at current rate**).
- [x] ★ **EXPLICIT resolution verdict on the ROTATION-flagged divergence** (§0, §4(v)): **it IS freight —
      the LEVEL and the LAG, not the direction.** (i) tanker **ruled out** on 13.3% revenue + zero
      institutional flow in KR tankers · (ii) 벌크 **ruled out for HMM**, logged as a separate 팬오션 watch ·
      (iii) net cash 43% / EV/OP 5.4× = **amplifier not trigger** · (iv) **not supported for HMM** (서지
      0.98×, no filings) **but found live on 대한항공 instead** (merger registration) · (v) **the answer.**
      **Residual unknowns named, not smoothed** (A2, A10).
- [x] ★ **대한항공 FX hypothesis given an explicit verdict: REFUTED** — on magnitude (fuel 2.16×) **and on
      sign** (net operating FX **−₩3,036억/yr**; the in-window broker credits 원화 **약세**). Replacement
      driver identified with **three independent sources** and the FX correlation explained as a
      **common cause** (semiconductor exports).
- [x] **No manufactured story. A clean negative result was delivered where the evidence supported one**
      (§7 zero candidates, §10 zero BET forwards) **and a positive correction where it supported that**
      (§4(v)). **Sources + asof dates on every claim; six blanks left explicitly blank; zero buy/sell calls.**
