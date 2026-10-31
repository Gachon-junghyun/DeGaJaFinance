# L1 · CHAIN_ALPHA — value-chain & contract alpha, analyst grade (stage)

> Block A+ for a single company. Where the reused DEEP maps a *sector*, this maps **one name's position
> in its chain** at the depth a sell-side/buy-side analyst actually models: who captures margin at each
> node, is this the binding bottleneck, does the backlog convert, and where is the mis-priced node.
> Calls L2 + L3. Output: the CHAIN_ALPHA section of REPORT (feeds SET_DIFF's ② measured list).

## Why this exists (the analyst lens)
"AI 수혜주"는 결론이 아니다. 애널리스트는 **밸류체인에서 마진이 어디서 잡히고, 이 회사가 그 층을 쥐고 있는지,
계약이 실제 매출로 언제 전환되는지, 그리고 시장이 *어느 노드*를 잘못 값매기는지**를 본다. 이 스테이지는 그
7개 렌즈를 한 종목에 전수로 건다. 각 렌즈는 `[검증함]/[차트만]/[직감]` 라벨 필수.

## L2 / L3 called
- [deepdive](../L2_modules/deepdive.md) — `module_industry_map "<체인 논지어>"`(노드 5~8·서브서플라이어) ·
  `module_business <code>`(세그먼트 매출·ASP·원재료/공급사·고객집중) · `module_valuation <code> --peers <p1,p2>`(상대멀티플) ·
  `module_disclosure <code> --days 400`(수주·계약) · `module_chart <code>.KS/.KQ --read`.
- [news](../L2_modules/news.md) — 밸류체인 hop 후보(본문 근접 미명명 수혜주 — 헤드라인 동시언급만으론 후보 아님).
- L3 [competitors](../L3_functions/competitors.md) · [related_companies](../L3_functions/related_companies.md) ·
  [contract_alpha](../L3_functions/contract_alpha.md)(수주 → book-to-bill·매출전환·상대사·단가).

## The 7 analyst lenses (전수 — 데이터 없으면 "후속" 라벨, 생략 금지)
1. **밸류체인 마진포착 지도** — 원재료→부품→모듈→세트로 노드 5~8개 좌→우. **각 노드의 마진 귀속**을 표시하고
   이 회사가 *마진을 쥐는 병목 노드*인지 *지나가는 패스스루*인지 판정. 병목의 근거 = 리드타임·백로그/매출 배율·
   대체 공급 부재. (수요가 강하다 ≠ 병목이다 — 이익은 병목이 먹는다.)
2. **세그먼트 단위 이코노믹스** — 사업부별 매출·비중·**세그먼트 마진**과 **믹스 시프트**(고마진 세그먼트 비중이
   느는가). ASP 추이를 세그먼트별로(예: 프리미엄 믹스가 aggregate 마진을 끌어올리나). 회사 aggregate 뒤에 숨은
   *진짜 이익 엔진 세그먼트*를 분리해 지목.
3. **계약·백로그 알파** — L3 contract_alpha: 신규 수주 금액·매출대비%·**book-to-bill**(>1 백로그 팽창)·
   **매출 전환 타임라인**(언제 P&L에 뜨나·lumpiness)·상대사 실명(익명이면 밸류체인/뉴스로 추정 [직감]). 백로그가
   보고매출 성장과 정합하나(B1의 실물 교차와 연결).
4. **고객·공급 의존 그래프** — 최대 고객 집중도(예: 특정 세트社 %)와 그 함의(가격협상력·경기민감). 상류 핵심
   원재료의 소싱 병목(공급사 실명·대체 가능성). *진짜 병목은 위/아래 어디인가*를 그래프로.
5. **경쟁 포지셔닝 (스펙·마진 대조표)** — 국내외 경쟁사 **최소 1곳**의 동일 지표(마진·점유율·제품 세대 스펙)
   대조표를 만든다(예: MLCC=무라타, FC-BGA=이비덴/신코/대덕). 스펙표 없는 "기술 우위"는 [직감]으로 강등. 어느
   축에서 이기고 어느 축에서 지는지 명시.
6. **가격전가력** — 투입원가 상승분을 ASP로 전가하나(분기 ASP·마진 추이). 전가되면 pricing power(병목 확인),
   마진이 눌리면 pass-through 종속.
7. **미스프라이싱 노드 (알파 누수)** — 시장이 헤드라인 종목에 수렴하는 동안 *체인의 어느 저관심 노드*(서브서플라이어·
   장비·소재·후공정)가 같은 수요를 더 싸게 노출하나. 본문 근접 미명명 수혜주만(뉴스 동시언급 ≠ 후보), 플로우 교차 후.

## Guards
- 숫자는 데이터팩/DART 원문만. 경쟁사 1곳 이상 같은 잣대로 대조(스펙표 없으면 우위 주장 강등).
- 병목 판정은 "수요 강함"이 아니라 *구속 제약*(리드타임·대체불가·가격전가)으로. 아니면 "수요는 진짜여도 이익은 남 얘기"라 쓴다.
- 익명 계약상대는 추정하되 [직감] 라벨 — 실명 공시가 아니면 결론 주축 금지.

## ✅ EXIT CHECK
- [ ] 밸류체인 노드 5~8 + **각 노드 마진귀속** + 이 회사 병목/패스스루 판정.
- [ ] 세그먼트별 마진·믹스시프트로 *진짜 이익엔진 세그먼트* 지목. ASP 추이 세그먼트별.
- [ ] contract_alpha: book-to-bill + 매출전환 타임라인 + 상대사(실명/[직감]) 산출.
- [ ] 고객집중·상류 소싱 병목 그래프. 경쟁사 ≥1 스펙/마진 대조표. 가격전가력 판정. 미스프라이싱 노드 1개(또는 "없음").
