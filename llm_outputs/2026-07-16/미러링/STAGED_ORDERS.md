# STAGED_ORDERS — 미러링 Stage 7 (2026-07-16 목) · 종착

> 사이즈된 판단 → **사람이 발사하는 intent 카드**(`out/order_desk/kis_stack.json`). **집행 0 · --execute 없음 · 자동발사 없음.** 분석/예시 — 투자자문 아님. 사람이 KIS 데스크에서 확인창으로 하나씩 [체결].

## 스택 정리
- **--clear로 스택 리셋**: 기존 8건 제거 = ①07-15 US 5건(TSM/AVGO/NVDA/RTX buy·CEG trim — **대부분 이미 보유=stale**) ②앞서 즉흥 KR 3건(사이즈 오류·KB는 상관가드上 PASS·노트 깨짐). 이번 정식 run 결정으로 대체.
- US 슬리브 = **전부 HOLD**(신규 주문 0) → US 카드 없음. KR ENTER 2건만 적재.

## 적재된 intent 카드 (2건, 총 2건)
| # | 시장 | side | 종목 | qty | price | 하드스탑 | 근거 |
|---|---|---|---|---|---|---|---|
| 1 | KR | buy | **SK이노 096770** | **6** | 시장가 | 89,500 | 🟢LIVE clean-entry·오일+전환 브릿지·diversify·리스크1.5% |
| 2 | KR | buy | **하나 086790** | **3** | **LIMIT 122,000** | 109,700 | 🟢LIVE RR최선 은행 스타터·S4 헤지·단일은행유닛(KB=watch)·현금버퍼 |

- 배치 = 744k(SK이노 확정) + 366k(하나 체결 시) ≤ 출금가능 1.69M, 버퍼 ~576k(인상/TACO 바이너리).
- **PASS/watch:** KB(은행 단일유닛)·S-Oil(energy 과편중)·SK이터닉스/한미/DISC(🟡). **보유 삼성전기 = HOLD-to-stop(EXIT-bias), close<1,260,000 시 EXIT.**

## epistemics 피드백 (원장 축적)
- `096770`: factor=oil_refining+SKon_battery, dir=up, conf=0.6 기록.
- `086790`: factor=BOK_rate_NIM, dir=up, conf=0.6 기록. → 다음 run이 `learned_sensitivity`로 참조.

## ✅ EXIT CHECK
- [x] 사이즈된 판단 2건 intent 카드화(note=테제+게이트)·kis_stack.json 기록.
- [x] paper book ↔ 스택 일치·epistemics 팩터 기록(2종).
- [x] **명시: intent만 · 사람이 각 카드 [체결] · 자동 0 · 투자자문 아님 · 집행 0.**
