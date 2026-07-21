# MACRO_REPORT — industry_KR · 2026-07-16 (Thu)

> Stage 1 / L1·MACRO. Runtime `--market kr`, English-instructions / KR-market output. Primary data:
> **cross-read same-day-ish US `MACRO_REPORT §A` [FRED via US-desk, asof 2026-07-15 — 1 session STALE]**
> (KR desk has no FRED module) + **KR-native BOK decision (today, realized)** + `module_news_data` via
> **NEWS API server `http://127.0.0.1:8787` (routed /exec — server DB, local fallback OFF)**, 7-bucket
> velocity + blindspot. Deliverable = the **§4 transmission matrix** (ROTATION's input). Zero buy/sell calls.

---

## §0 Catalyst injection (run-start, from CATALYST_WATCH.json + KR calendar)
| When | Event | Axis | Binary? |
|---|---|---|---|
| **TODAY 2026-07-16** | **BOK 금통위 — 만장일치 25bp 인상 (REALIZED, 종합)** | rates | ✅ **RESOLVED intraday** — see §1 |
| **TODAY 07-16** | TSM · NFLX earnings (US) | earnings | 🔀 binary (spillover to KR semi/COMM) |
| Undated / live | **Iran "Strait of Hormuz open" (TACO trigger)** — blockade persists | oil | ✅ open-ended → both-sides bracket |
| 07-21 (D-5) | SCHW earnings (US fin read-through) | earnings | 🔀 |
| **07-20 → 07-23** | **KB금융 자사주 종료(7/20) → 2Q 실적(7/23, 컨센 ~1.83조)** | KR banks | 🔀 binary → FIN leg |

⚠ **BOK hike RESOLVED today** — the prior KR BET_SHEET (07-15) FIN thesis M-01 was betting a 9/10-consensus
hike; it **fired, unanimous, with a hawkish "continue the hiking bias" statement.** No longer a forward binary
— now a realized regime fact (§1). Hormuz remains the one live both-sides bracket for ENRG.

---

## §1 Regime read — primary numbers explicit

### ★ KR-native regime event (TODAY, realized): **BOK hikes 25bp, unanimous, hawkish continuation**
- **한은 기준금리 0.25%p 인상 — 금통위원 만장일치** [news · Yonhap 속보 07-16]. Framing: *"물가 높고 성장 개선"* /
  *"향후 통화정책, 금리 인상 기조 이어갈 필요"* [Yonhap 07-16] and *"올해 성장률 2.6% 큰 폭 상회 예상"* [Yonhap 07-16].
- **Transmission (the KR spine, mirror-image of the US easing regime):** BOK **HIKING into an upgraded-growth /
  firm-inflation read** → variable-rate loan **immediate repricing → bank NIM expansion** (FIN OW, the confirmed leg)
  while **rate-sensitive RE / long-duration** takes the direct headwind. This is *not* an oscillating one-off — the
  statement explicitly guides continuation, so the KR curve wind is durable, not a single print.
- ⚠ **Divergence from the US desk:** the US MACRO (07-15) reads a **cool-CPI, Fed-on-hold-to-easing** regime;
  KR is **actively hiking**. The two desks' rate winds point opposite ways this run — do not import the US
  "rate-relief risk-on" frame into KR wholesale. KR's risk-on is coming from **flow (foreign return) + 밸류업**,
  not from a dovish central bank.

### Cross-read of US primaries [FRED via US-desk MACRO_REPORT §A, asof 2026-07-15 — 1 session STALE]
| Series | US latest (07-13/asof) | KR read-through |
|---|---|---|
| US 10Y | 4.62% (bear-steepened pre-CPI; post-CPI "temporary relief") | Global long-end term-premium = imported cost-of-capital headwind for KR growth/RE |
| US 2Y / real 10Y | 4.26% / 2.36% | High global real yields cap KR long-duration multiples |
| DXY | 120.5, **softening post-CPI** | A rolling-over dollar = **USD/KRW relief → foreign-inflow tailwind** (matches the 07-15 3조 buy) |
| VIX | 17.2 (creeping) | Mild global hedging bid; KR VKOSPI-equivalent not panic (PULSE 07-16: VIX 16.2) |
| Fed funds | 3.62% (easing-mature, on hold) | **Fed easing vs BOK hiking = narrowing KR-US rate gap → KRW-supportive, foreign-friendly** |

**Net regime:** KR is in a **hiking-into-recovery** regime with a **softening-dollar / narrowing-rate-gap**
foreign-inflow tailwind — structurally FIN-positive, RE-negative, and supportive of a foreign-led 밸류업 rotation.

---

## §2 Positioning — KR flow (the KR edge axis) + US COT cross-read

### KR investor-type flow (the measured "who is buying" the US desk lacks) — **whipsaw week, foreign turn on 07-15**
| Datapoint | Value | Read |
|---|---|---|
| **Foreign, 07-15 session** | **+3조원 "폭풍매수", 장 시작 6분 매수 사이드카** [MT/Yonhap 07-15] | ⚠ **Potential cut of the 6-month 46.9조 net-sell** — the exact "미절단" flag the 07-15 BET_SHEET raised |
| 07-13 session | 코스피 **−8%**, 기관·외인 순매도; Goldman: *"레버리지 ETF 기계적 매도가 낙폭 키움"* | Whipsaw — the buy is 1 session, not yet a confirmed trend |
| 07-16 (today, PULSE) | KR 본토 삼성전자 +3.3 / 하이닉스 +3.7 rebound vs **US ADR SKHY −10.2** | KR domestic **decoupled up** from US-ADR memory froth unwind |
| Domestic institutions | Banks 기관 +322만(KB)/+99만(하나) net-buy [BET_SHEET 07-15] | 밸류업 rotation is domestic-institution-led; foreign now *joining* on the index |

### US COT cross-read [context, not trigger — us_flow --cot, Tue-close +3-4d lag]
- **WTI crude 13%ile 🔴 crowded-SHORT into a live Hormuz premium** → same squeeze asymmetry feeds **KR ENRG (S-Oil)**.
- **Copper 95%ile 🟢 crowded-LONG (overheated)** → caution flag on KR Materials / 이차전지 소재 chasing.
- **Nasdaq-100 4%ile 🔴 crowded-SHORT** → any US semi squeeze read-through supports KR semi *sentiment* (not flow).

**Positioning verdict:** the decisive KR tell is **the 07-15 foreign 3조 buy** — if it holds >1–2 sessions it
cuts the 46.9조 overhang and upgrades the whole rotation; if 07-13-style whipsaw returns it was mechanical. This
is the single KPI ROTATION/SWEEP must confirm with per-investor actuals.

---

## §3 Narrative velocity — 7-bucket sweep [server DB /exec · domestic · 7d · OR+kr+syn]
| Rank | Bucket | 7d count | Note |
|---|---|---|---|
| 1 | 반도체 / HBM / 메모리 / 하이닉스 | **4,639** | Loudest; but froth-unwind headwind (below) |
| 2 | 원전 / SMR / 전력 / 데이터센터 | **2,792** | AI-power buildout + 한미일 SMR bloc |
| 3 | 트럼프 / 관세 / 무역 / 환율 | **2,189** | Persistent export overhang (KR deal undated) |
| 4 | 바이오 / 제약 / 헬스케어 | 570 | Background; HLB emergent |
| 5 | 이차전지 / 배터리 / 전기차 | 408 | Quiet — no fresh catalyst |
| 6 | 은행 / 금융지주 / 한국은행 / 금리 | 345 | Low *count* but **highest-conviction** (BOK hike = the event, §1) |
| 7 | 방산 / 조선 / 방위산업 / 수출 | 52 | Trigram-thin (2-char terms under-index); treat count as floor, not truth |

⚠ **Count ≠ conviction:** the FIN bucket is count-rank #6 but event-rank #1 (the realized BOK hike). And the 방산/조선
count (52) is depressed by the KR trigram 2-char-term blind spot — do not read it as "no defense/shipbuilding wind."

### Blindspot pass [3,851-row blind-pool sample, domestic 7d, token-0 emergent]
- **비료 관련주 ↑ on 중동 긴장 재고조 · 공급망 우려** [Yonhap 07-14 특징주] → a **Materials/agri leg leaking off the
  Hormuz axis** the fixed 7-bucket set never queries. **New term: 비료(fertilizer) / 공급망.**
- **메타, 9월부터 자체 AI칩 생산 — 엔비디아 의존 축소** [Donga 07-10] → a **structural anti-signal for the HBM/GPU demand
  chain** (hyperscaler in-housing silicon). Latent, not thesis-ending, but a kill-switch to track. **New term: 자체 AI칩 / 내재화.**
- **中 CXMT 상장으로 14조 조달 — D램 시장 흔든다** [Donga 07-15] → confirms the **memory oversupply** anti-signal
  (folds into M-04). Same axis as the PULSE 07-16 froth-unwind catalyst.
- **얼라인파트너스, JB·BNK 금융지주 합병 공개제안 (자산 234조 지방 메가뱅크)** [Yonhap/Sedaily 07-14] → an **activist /
  consolidation leg inside FIN** beyond the big-4 밸류업 story. **New term: 지방금융 합병 / 행동주의.**
- **스페이스X 장기채 외면받았다 — "AI 투자열풍 속 이상신호"** [Sedaily 07-14] → the **AI-capex-skepticism kill-switch**
  (mirror of the US moratorium anti-signal) — feeds M-03's anti-branch. **New term: AI capex 회의.**
- **Living term-table additions this run:** `비료/공급망`, `자체 AI칩/내재화`, `CXMT`, `지방금융 합병/행동주의`, `AI capex 회의`, `밸류업 순환매`.

---

## §4 ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)
> Wind direction only, one line per GICS sector. Not equal-weight analysis. Driving prop IDs in §4a.

| # | GICS Sector | Tilt | Driving prop | One-line why (KR) |
|---|---|---|---|---|
| 1 | **Financials (FIN)** | **OW** (highest conviction) | M-01, M-05 | **BOK 25bp hike FIRED today + hawkish continuation → NIM**; 밸류업 domestic-institution 매집 + foreign 07-15 return; the one macro+flow双확증 leg |
| 2 | **Information Tech (IT/반도체)** | **OW-but-GATED** | M-04 | HBM 펀더 최강(삼성 HBM 1위 전망·2028 공급부족·한미 record-Q2) ↔ **US-ADR froth unwind + CXMT 14조 oversupply + 메타 자체칩** — thesis OW, flow gate |
| 3 | **Industrials (INDU)** | **OW (split)** | M-03, M-06 | 전력기기(변압기·케이블 AI-DC 병목 규제화·LS일렉 인피니언 MOU) + 조선/방산 수출 — orderbook strong, flow still waiting |
| 4 | **Energy (ENRG)** | **tactical OW** | M-02 | **Hormuz 봉쇄 프리미엄 잔존 + WTI crowded-short squeeze** → S-Oil 정제마진; NOT demand-pull; 과열 주의 |
| 5 | **Consumer Disc (DISC)** | **modest OW** | M-05 | K뷰티 ODM 순환매(화장품 6월 수출 역대최대·한국콜마)·성장→가치 rotation 반사 |
| 6 | **Utilities (UTIL/원전)** | **Neutral** | M-03 | 한미일 SMR 협력·SMR 특별법 = thesis fresh ↔ 돈 이탈(두산 falling-knife)·RE100 원자력 제외 역풍 — offsetting |
| 7 | **Materials (MATR)** | **Neutral→UW** | M-02, M-05 | 이차전지 소재 velocity 낮음(408) + copper 95%ile overheated; **단 비료주 Hormuz leg는 tactical(blindspot)** |
| 8 | **Comm Services (COMM)** | Neutral | — | No distinct KR wind this run; NFLX/TSM spillover only |
| 9 | **Health Care (HLTH)** | Neutral | — | 바이오 background(570), HLB emergent — no macro wind, defensive ballast |
| 10 | **Consumer Staples (STPL)** | Neutral→UW | M-01 | Risk-on/순환매 rotates out of defensives; hike = no relief |
| 11 | **Real Estate (RE)** | **UW** | M-01 | **BOK hike = direct variable-rate repricing + PF 부실 risk**; 부동산 규제(동탄 blindspot); most rate-negative |

### §4a Falsifiable propositions (both branches on oscillating variables; M- = KR macro spine)
- **M-01 — BOK hike / curve (REALIZED):** *Unanimous 25bp hike + "continue hiking" + 2.6% growth → variable-rate
  repricing → bank NIM expansion → FIN OW; rate-sensitive RE/STPL UW.*
  - **Anti-signal / other branch:** 증시활황發 **핵심예금 이탈**(코스피 1%p↑ → 예금유입 9,300억 둔화 [BET_SHEET]) offsets NIM,
    OR **부동산 PF 부실 재점화** turns hike into a credit-cost event. Track KPI: bank 2Q NIM prints (KB 7/23), 연체율, 예금 mix. Catalyst: **KB 2Q 07-23**.
- **M-02 — Oil / Hormuz (oscillating, both branches equal):** *Blockade premium persists × WTI crowded-short → tactical ENRG (S-Oil) + 비료/공급망 leg.*
  - **Anti:** **TACO** — Iran declares strait open → 브렌트 gaps to $70s, crowded-short covers, premium gone in a day. One-way tilt here = protocol violation. Track: Hormuz transit, 브렌트 spot.
- **M-03 — AI-power / DC capex:** *AI-DC 전력 병목 규제화(뉴욕주 유예) + 한미일 SMR 협력 → INDU 전력기기 · UTIL 원전.*
  - **Anti (KR-specific kill-switch):** **스페이스X 장기채 외면 = AI-capex 회의**(blindspot) spreading + **RE100 산단 원자력 제외**(수요측 규제) → orderbook throughput slows, the *already-priced* 원전/변압기 leg re-rates down. Track: DART 단일공급계약 전환(현재 0건), AI-capex 회의 narrative spread.
- **M-04 — Memory supercycle:** *펀더 무손상(삼성 HBM 글로벌 1위 전망·2028 공급부족·한미 record-Q2 +51%·삼성 OBV +18 유일 매집) → IT thesis-OW.*
  - **Anti (dominant near-term):** **froth unwind**(US-ADR SKHY −10% 07-16) spreads from 大형 price to KR breadth(0.01) + **CXMT 14조 oversupply** + **메타 자체 AI칩**(demand 내재화) + 외국인 매도 미확정 절단. Gate = breadth 확산 + OBV 매집 확산. Track: 삼전닉스 domestic breadth, CXMT 애플 채택, 외국인 절단 지속.
- **M-05 — 밸류업 / 외국인 복귀 rotation:** *07-15 외국인 3조 폭풍매수·매수 사이드카 = 46.9조 순매도 절단 신호 후보 → FIN·건설(GS건설)·화장품 순환매.*
  - **Anti:** 07-13-style **whipsaw** returns (레버리지 ETF 기계적 매도), 외국인 buy was 1-session mechanical, not trend. Track: **per-investor net-buy over next 1–2 sessions** (the SWEEP KPI).
- **M-06 — Tariff / 무역 (export overhang):** *한국-미국 상호관세 딜 미확정(인도 진통·인니 임박 대비 KR 공백) → 수출주(반도체·조선·방산) 오버행.*
  - **Anti:** 유리한 KR 딜 타결 → relief rally for exporters. Track: KR-US 협상 headlines, 관세율 확정.

---

## §5 Self-backtest (running hit-rate)
⚠ No prior KR `MACRO_REPORT.md` exists (this is the first KR MACRO artifact). Scoring is against the
**07-15 KR BET_SHEET propositions + handoff ledger** (the only prior KR desk record).

| Prior proposition (BET_SHEET 07-15) | +Δ to 07-16 | Score |
|---|---|---|
| **[FIN] M-01 — BOK 7월 인상 컨센 9/10 → NIM** | **인상 FIRED today, 만장일치, hawkish continuation** | **HIT** — the highest-conviction leg confirmed on realized data |
| [IT] flow gate — froth vs fundamentals (ADR +27% but breadth 0.01) | 07-16 US-ADR SKHY **−10%** froth unwind; KR 본토 +3% decoupled | **HIT (call validated)** — "froth not fundamentals" proved right; gate stays |
| [INDU] 전력기기 orderbook strong, flow waiting | LS일렉 인피니언 MOU 07-13 = orderbook↑; flow still 🔴 | **HALF** — thesis compounding, money not yet |
| [UTIL] 원전 테제 fresh, 돈 이탈 (두산 falling-knife) | 한미일 SMR 협력·SMR 특별법 = thesis fresh; RE100 원자력 제외 역풍 지속 | **HALF** — both branches still live |
| **외국인 순매도 미절단 flag (46.9조)** | 07-15 외국인 **3조 폭풍매수** = potential cut | **FLIPPED → upgraded to live watch** (M-05); confirm over 1–2 sessions |

**Recurring failure class watched this run:** one-sided reads of oscillating variables — **M-02 (Hormuz)** and
**M-05 (foreign whipsaw)** both carry both branches by design. The BOK hike (M-01) is now *realized*, so it is
scored as fact, not a forward one-way bet.

### §5a ADDENDUM (append-only — realized-data correction from DEEP stage, 07-16)
- ⚠ **The BOK hike day printed RISK-OFF, not risk-on.** DEEP-FIN surfaced that **07-16 코스피 ≈ −7% with a 매도
  사이드카** — the market read the unanimous hike + hawkish continuation as a **de-rating / tightening** event, **not**
  the "foreign-inflow risk-on" the §1/§2 framing leaned toward (that was the 07-15 snapshot: 외국인 3조 buy, softening dollar).
  **Correction:** M-05 (밸류업/foreign-return rotation) is now **one-branch-down** — the 07-15 foreign 3조 buy did NOT
  carry; it whipsawed to risk-off on 07-16, so the 46.9조 net-sell "cut" is **NOT confirmed** (M-05 anti-branch fired).
- **What survived the correction:** FIN still worked on a **relative** basis — banks were **accumulated into the selloff**
  (금융 flow +0.17 top-of-board, 하나 OBV +108%, KB 기관 +322만), i.e. **defensive-into-tightening**, not a broad risk-on
  bid. So M-01 (hike→NIM→FIN OW) holds as a *relative* call; the *index-level* risk-on premise does not. BET must size
  FIN as relative-strength-into-selloff, and treat the whole tape as tightening-de-rating (reinforces RE/growth UW, IT gate).
- Track: does 07-16 risk-off extend (tightening de-rating spreading to banks too) or was it a one-day hike-shock digestion?

### §5b ADDENDUM (append-only — WebSearch live correction, 07-16)
- ⚠ **Framing error corrected — the KRW is WEAK, not "softening-dollar-supported."** Live source [CNBC/KED/Yahoo 07-16]:
  BOK hiked to **2.75% (first hike since Jan 2023)** driven by **CPI 3.2% June (accel from 3.1% May, above 2% target) +
  WON WEAKNESS + household-credit/property**. My §1/§2 premise "softening dollar → won-supportive → foreign-inflow tailwind"
  is **wrong** — the won is a *driver of the hike*, i.e. weak. **M-05 (foreign-return rotation) is therefore weaker than
  framed**: the 07-15 foreign 3조 buy was a one-session whipsaw into a weak-won, risk-off tape, not a durable inflow.
- ✅ **What UPGRADED: the forward hike path is real.** Market prices **another hike Oct → 3.00% year-end, 2 more this year /
  3–4 through 2027** [KED survey]. So **M-01 (hike→NIM) is DURABLE, not one-off** — the bank NIM tailwind extends, which is
  the fresh bettable leg (not today's priced-in hike). Mortgage repricing +1.8~5.5조 interest = NIM tailwind AND credit-risk (both sides).
- ✅ **Hormuz premium is LIVE/escalating, not fading** [CNBC/AlJazeera 07-16]: blockade **Day 137**, transits **10/day vs 88 baseline**,
  US reinstated naval blockade 07-15, **Brent $85.36 (+9.6% biggest daily since May 2020)**. M-02 oil-leg fundamentally intact
  and current — but that means the *premium is now consensus-long* → TACO (Iran reopens) = the sharp both-sides reversal risk.

---
**EXIT CHECK:** ✅ catalysts injected (BOK hike RESOLVED intraday) · ✅ narrative(7-bucket + blindspot) + indicators
(US §A cross-read + KR flow) + positioning read · ✅ continuity anchor (07-15 KR BET_SHEET + handoff ledger) read ·
✅ 11-sector transmission matrix produced · ✅ self-backtest appended · ✅ new blindspot terms folded into term table.
**News source = server DB via NEWS API `127.0.0.1:8787` (routed, not local fallback).**
**→ proceed to SWEEP.**
