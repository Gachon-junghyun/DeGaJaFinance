# 미러링 RUN — 2026-07-15 (Wed) · KIS 실계좌 미러 + 오늘 판단 적용

> Protocol `미러링` (mirror). Engine `module_paper_book` (+`module_order_desk` stack, `module_epistemics` vault).
> **모든 추천은 분석/예시 — 데스크가 주문을 내지 않는다. 사람이 [체결]로 하나씩 발사. 투자자문 아님.**

## 1) MIRROR_INGEST — 실계좌를 paper book 에 반영 (US 한정)
스크린샷(2026-07-15) 기준, KIS 잔고를 fx≈1380 으로 역산(qty = 시장가÷fx÷현재가, 평단 = 현재가÷(1+손익%)).
총자산 재구성 **10,977,073 KRW** vs 실제 총자산(KIS) 11,004,125 — fx/시점 오차 내 일치 ✅.

| 보유 | qty | 평단$ | 테마(상관단위) | 손익 |
|---|---|---|---|---|
| KMI | 34 | 32.70 | energy-fuel / AI-power-adjacency | −1.0% |
| LNG | 3 | 242.08 | energy-fuel / AI-power-adjacency | +6.6% |
| VST | 3 | 156.32 | AI-power-IPP | +5.7% |
| CEG | 1 | 261.59 | AI-power-IPP | −1.0% |
| MA | 2 | 533.35 | payments / FIN | +1.1% |
현금 KRW 5,869,093 · 외화현금 $0. (국내 삼성전기 009150 = 미국 지식 스코프 밖 → 미러 제외, 참고만.)

**진단(오늘 판단의 출발점):** 이 책은 **AI-power *결과(consequence)*** — 연료(KMI/LNG) + 전력IPP(VST/CEG) —
에 몰려 있고, **AI-compute *엔진(engine)* 은 0%**. 이건 industry_US 사이클노트의 🚨 GAP(rank-1 AI-compute
epicenter 0% < 12% 필요)를 실계좌가 그대로 안고 있는 상태. 에너지/전력이 하나의 상관단위로 뭉쳐 있음.

## 2) DECIDE — 오늘 판단 (industry_US 07-15 근거 + epistemics 시드)
| 액션 | 종목 | 컨빅션 | 근거 | 게이트 |
|---|---|---|---|---|
| **ENTER** | **TSM** 1 | high | epicenter 코어(모노폴리 파운드리) — 0% 엔진 GAP 해소, tape-independent | 코어 0.8%리스크 |
| **ENTER** | **AVGO** 1 | high | epicenter 코어(커스텀 ASIC) — ASML 가이던스 상향 07-15, PEG 0.45 | 코어, stop 360 |
| **ENTER** | **NVDA** 1 | high | epicenter **게이티드** add — 나스닥 크라우디드숏 4%ile 스퀴즈연료 | **하드스탑 193 필수** |
| **ENTER** | **RTX** 4 | med | 방어 다변화 — CONFIRMED-TURN, 책의 에너지/전력과 **무상관** | un-gated, stop 182 |
| **TRIM** | **CEG** 1 | med | IPP 소진(다운그레이드+NY 모라토리엄) — 결과→엔진 로테이션 | — |
| HOLD | KMI·LNG·VST·MA | — | 에너지연료/IPP/결제 유지(추가 매수 없음 — 이미 과집중) | — |

**로직:** ①하드게이트(스탑히트 없음; CEG 소진→트림) ②GAP 우선(엔진 0%→코어 신규) ③상관가드(에너지/전력에
더 얹지 않음; 무상관 방어·엔진으로 분산) ④드라이파우더 규율(현금 47%→34%만 투입, 절반 이상 남김).

## 3) SIZE & 적용 결과 (paper book 반영 완료)
FX 전환 2,153,660 KRW → $1,561 (외화현금 $0 이라 US 매수 위해 전환 — 실계좌도 동일 선행 필요).

| 지표 | 미러 직후 | 추천 적용 후 |
|---|---|---|
| 총자산(KRW) | 10,977,073 | **10,964,467** |
| 원화현금 | 5,869,093 | **3,715,433** (34% dry powder 유지) |
| **AI-compute-EPICENTER 노출** | **0원 (0%)** | **1,410,498원 (~12.9%)** — 🚨 GAP **해소** (≥12% 충족) |
| 테마: energy-fuel / IPP / defense / payments | 2.59M / 0.68M / 0 / 1.49M | 2.59M / 0.68M / **1.07M** / 1.49M |
스탑히트 없음 · 집중도 한도 내.

## 4) STAGE_ORDERS — KIS 주문 데스크 스택에 적재 (`out/order_desk/kis_stack.json`)
사람이 데스크에서 카드별 [체결]로 발사. **자동 발사 없음.**
```
BUY  TSM  1 @ 427   [epicenter core, tape-independent]
BUY  AVGO 1 @ 393   [epicenter core, stop 360]
BUY  NVDA 1 @ 212   [epicenter GATED — hard-stop 193]
BUY  RTX  4 @ 196   [defense diversifier, stop 182]
SELL CEG  1 @ 259   [TRIM exhausting IPP]
```

## 5) EPISTEMICS 축적 (판단 근거 되먹임 → `epistemics/sensitivity/`)
오늘 판단의 factor 를 종목별 원장에 시드(다음 실행이 prior 로 조회, catalyst 후 실제반응으로 update):
`TSM·AVGO(AI-capex/CoWoS +강 0.8)` · `NVDA(GPU/CoWoS +강 0.75)` · `RTX(missile-defense/Golden Dome +중 0.65)` ·
`CEG(datacenter-load-growth 무/- 0.6 — 소진)`.

---
**다음 관측점:** TSM 07-16 실적(엔진 확증) · NVDA 하드스탑 193 · GEV 07-22(전력장비 소진 tell) · Hormuz(에너지연료 KMI/LNG) ·
CEG 소진 확증 시 잔여 IPP(VST) 재평가. **실행은 사람 몫 — 이 데스크는 계획만 올린다.**
