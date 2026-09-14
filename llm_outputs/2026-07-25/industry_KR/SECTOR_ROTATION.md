# SECTOR_ROTATION — industry_KR · 2026-07-25 (토, asof 07-24 종가)

> Delta-only. MACRO §4가 11섹터 판정을 소유, `SECTOR_FLOW_KR.json`이 flow 숫자를 소유(디스크 상주).
> 이 파일은 **바뀌는 것만** 쓴다. 매수/매도 권유 0건 (P4).
> ⚠ **이번 스윕은 RS20/RS60 전 종목 nan** — flow_score가 OBV(C급)+vol_surge만. 규칙 D6에 따라 flow
> 단독으로 판정 이동 불가, **B급 KIS 실측이 있는 델타만 유효**.

## §1 상속 (MACRO §4 그대로 한 줄)
`ENRG tactical OW+ · HLTH OW-shelter · IT/반도체 N(게이트 절반·순풍) · INDU N(split, 전력레그 산 레그) ·
COMM N(OW 약함) · FIN N(R15 강등) · STPL/DISC/RE N · MATR UW · UTIL UW(anti-branch)`

## §2 델타 (돈이 논지와 불일치하는 섹터만 · flow 숫자 필수)

| 섹터 | 매트릭스 | flow 증거 | 신규 판정 | 해소자 |
|---|---|---|---|---|
| **통신(COMM)** | N (OW 약함) | wflow **+0.640**(보드 top-3) · Δ **+0.514**(#1) · 🟢 1(SK텔레콤) | **N 유지 — 승격 declined** | ⚠ **flow가 매트릭스보다 강하나 승격 declined**: (a) 태그가 KIS축 미반영(C9/D37, 통신 실측 3/5 vs 태그), (b) Δ는 단일날짜(D38), (c) SK텔레콤 KIS는 기관 매수·**외국인 매도**(여력한도 76.5%), (d) 07-29에 KT제재(S18)+지배구조(S11) 이중 바이너리. **RS nan이라 flow가 C급 = 이 발산은 상당부분 측정 아티팩트** → **DEEP-COMM이 조기 vs 함정 판정** |
| **금융(FIN)** | N (R15 강등) | eqflow **+0.186** > wflow +0.074(breadth처럼 보임) · 증권 −0.103 | **N 확정 — 델타 아님** | eqflow>wflow는 **D9/M54 홀드코 54.4% 아티팩트**(실제 금융 19종 +0.286). R15가 07-23 폭발일 벤치하회로 이미 OW 철회. 증권 −0.103 = 브로커리지 감속 확증(M52). **재DEEP 불필요, 07-24 커버** |

**나머지는 flow가 매트릭스 확증(§1 그대로) — 델타 없음:**
- **ENRG**: 정유(SK이노 OBV매집+KIS 외+35.1만/기+313.4만·S-Oil 기+113.7만) = B급 real-hands 확증 → OW 유지.
- **IT/반도체**: 전기·전자 Δ **+0.6 = 보드최고 점화** 확증하나 메가캡 OBV 분산(삼전 0.228·하이닉스 −0.123)
  = 점화가 breadth/중소형, 메가캡 아님 → N 유지(게이트 절반). **이 발산이 DEEP-IT #1 질문**.
- **MATR**: 금속 −0.141 🔴 → UW 확증. **UTIL/DISC/STPL/RE**: 이동 근거 없음.

⚠ **macro 재논증으로만 이동한 섹터 0건** — 이동은 전부 flow 숫자(또는 flow 부재) 근거.

## §3 DEEP 4선 + DEEP_LOG

**선정(관성+재귀성 규칙):**
1. **ENRG** — *연속-트랙*. 07-24 연속 슬롯 유지 + 오늘도 최상위 OW → 안티-스래시 유지(**6런 연속**). 해소
   질문: C4(마진 vs 전쟁프리미엄, 정유 KIS real-hands 확증됨) + W4 미충족(S-Oil 2Q일 blank, D45).
2. **IT/반도체** — *회전 #1*. **마지막 DEEP 07-17 = 최장 기아**, 07-24·이전 로그가 **2회 "다음 런 #1
   발산"으로 명시 지목**, 그리고 오늘 **보드최고 점화 Δ+0.6**. 해소 질문: 이 점화가 진짜 breadth인가
   메가캡-분산 함정인가(게이트 절반열림).
3. **HLTH** — *회전 #2*. OW-shelter, 제약 wflow +0.514/Δ+0.304. OW 중 IT 다음으로 최장 미커버(07-23).
   해소 질문: 셀트리온 vs 삼바 마진엔진 반대(W5) 지속 + 방어 rotation의 real-hands.
4. **COMM** — *회전 #3*. §2 발산(wflow +0.640/Δ+0.514 vs N)이 이번 런 최대 매트릭스×flow 갭이고 07-29
   이중 바이너리(S11·S18) 아래. ⚠ 07-24 커버했으나 **신규 flow 발산 + 07-24 DEEP 자체가 승격 약함으로
   판정** → 재검 정당(스래시 아님). 해소 질문: flow가 진짜인가 KIS-blind/단일날짜 아티팩트인가.

**declined**: FIN(R15로 해소·07-24 커버) · INDU(07-24 커버, 전력레그는 EVENT_ALPHA 카드4에서 처리) ·
MATR/UTIL(UW 유지, 이동 근거 없음). **패딩 없음 — 4개 전부 규칙 근거.**

## DEEP_LOG 2026-07-25: continuous=[ENRG (6런 연속, 안티-스래시 유지 · 정유 KIS real-hands 확증)] rotating=[IT/반도체 (07-17 이후 최장기아 + 2회 "#1 발산" 약속 이행 + 보드최고 점화 Δ+0.6), HLTH (OW-shelter, IT 다음 최장 미커버 07-23), COMM (신규 flow발산 wflow+0.640/Δ+0.514, 07-29 이중 바이너리)] · declined: FIN (R15 해소·07-24), INDU (07-24·전력레그 EA카드4), MATR/UTIL (UW 유지) · 휴식: DISC/STPL/RE (이동근거 없음) · ⚠ RS nan 런이라 flow가 C급 — DEEP은 KIS 실측(B급) 우선

## ✅ EXIT CHECK
- [x] §1 한 줄로 MACRO 매트릭스 상속. 불변 섹터에 행/문단/재출력 없음.
- [x] §2 델타마다 flow 숫자 인용(통신 wflow+0.640/Δ+0.514, 금융 eqflow+0.186). macro 재논증 이동 0.
- [x] 매트릭스×flow 발산(통신) 해소자(DEEP-COMM) 명시.
- [x] DEEP 4선 규칙(관성 ENRG·재귀성 IT/HLTH/COMM 명시), 패딩 없음.
- [ ] 린터 실행 → 아래 별도.
- [x] DEEP_LOG 부착.
