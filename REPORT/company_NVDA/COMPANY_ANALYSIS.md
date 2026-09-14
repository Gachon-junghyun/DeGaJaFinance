# COMPANY ANALYSIS — NVDA (NVIDIA Corporation) · 2026-09-03

> 색인 문서. **본문은 사람이 읽는 Word/PDF 다** — 아래 산출물 항을 보라.
> 프로토콜 `pipeline/protocols/기업분석.md` 13블록 완주. 기준가 2026-09-02 종가 **$224.41**.

## 평결
**HOLD** · 목표주가 **$248** (+10.5%) · 손절 **$208.48** (−7.10%) · 호라이즌 **2026-11-18**
손익비 **1.481** ⇒ G4 게이트 **FAIL(0.019 차)** ⇒ ADD 불가. 원장 1행 append
(`reject_ledger` `J.사이즈미미`, 재확인 2026-11-19).

## 이 런이 찾은 것
- **8-K 2026-08-17 (Item 1.01+2.03)**: SB Energy 4.25GW 리스에 잔존가치보증, **상한 $105bn**,
  임차인 **OpenAI**, 20년. 10-Q **EX-10.1 계약원문**: *"if and only if Guarantor executes… this Guaranty"*.
  종료조항 (iv) = **임차인이 신용등급 달성**. 보증 최대 총노출 **$108.5bn**, 약정 총계 **$422bn**
  — **어떤 배수에도 안 들어간다.**
- **424B5**: **$25bn 선순위 무담보 채권** 7트랜치(2028~2056, 4.25~5.625%). 같은 분기 주주환원 $25.8bn(FCF 의 120.8%).
- **매출 절반은 교차확인된다**: 고객 3사 capex **+97.7% Y/Y** vs NVDA Hyperscale **+101.6%** (괴리 3.9pp).
  **나머지 41.9%(ACIE, 분기 스윙의 55.6%)에는 감사받는 대응 계열이 없다.**
- **OCF/NI 0.403** · **DSO 45→60일** · GAAP 순이익의 **20.1%(6M)가 지분평가익**.
- **본체 EV/EBITDA 20.4배** = 메모리 제외 AI-compute 피어 **전부보다 낮다** (AMD 77.1 · MRVL 64.0 · ANET 47.7 · AVGO 42.6).
- 상위 2 직접고객 = 매출의 **36%** (FY25 23% → FY26 **+13pp**).
- `S130` Leg1: **NVDA 파일링에 Hugging Face 인수 없음** (EDGAR 전기간 3건, 전부 2023~24).

## 🔄 1차 개정 (2026-09-03 사후 탐색) — 평결 불변, **초판의 전제 하나가 반박됨**

- 🚨 **초판의 "ACIE 고객은 감사받는 대응 계열이 구조적으로 없다"는 틀렸다.** NVDA 8-K 가 이름을 댄
  **CoreWeave(CRWV)·Nebius(NBIS) 가 상장사**다. CRWV **차입금 $51.6bn > 시총 $44.6bn · 차입금/EBITDA 13.6배 · 적자**,
  NBIS **34배·적자**.
- 🚨 **순환이 상대방 공시에서 양쪽으로 닫힌다**: CRWV 10-Q — *"securities purchase agreement with
  **NVIDIA** … 23M shares @ **$87.20** … **$2.0bn**"* + *"**all of the GPUs … are NVIDIA GPUs**"*.
  그 지분은 지금 **−$144M (−7.19%)**.
- 🚨 **OpenAI 손익은 측정된다**: 마이크로소프트가 **27% 를 지분법(VIE·HLBV)** 으로 인식.
  Note 3 — FY25 3M **−$768M** · FY25 9M **−$2.7bn** · FY26 3M **−$19M** · FY26 9M **+$5.9bn**(희석이익).
- ★ **대체재는 미래가 아니라 과거**: **Maia 200 이 2026-01-26 부터 Azure 가동**, MSFT 자체 주장 **성능/달러 +30%**.
  Maia 300 은 MSFT 뉴스룸 0건. ⇒ **capex 점유 갭 −16.5pp 에 시점이 맞는 후보.**
- 내부자: Stevens 09-02 매도는 **전량 신탁 라인**, 잔량 3,358,770주 ⇒ **그 라인의 35.5%**.
- 관측점 **P133**(CRWV 차입금배수, 11-12) · **P134**(MSFT의 OpenAI 인식손익, 10월말) ·
  **P135**(CRWV 지분 시가평가, 11-12) 추가.

⇒ `risk_unseen` R1·R2 가 **「측정 불가」→「측정 가능, 아직 안 쟀음」** 으로 재등급.
**보고서를 좋게 만들지 않는다 — 핑계가 사라졌다.**

## 산출물
- **`REPORT/company_NVDA/엔비디아_기업분석_20260903.docx`** (52.6KB) · **`.pdf`** (314.9KB) — 사람이 읽는 본문
- **`llm_outputs/2026-09-03/company_NVDA/UPGRADE_PROBE.md`** — 사후 탐색 전문(규칙 U1–U7 · 계기 수정 D-1–D-5)
- 스테이지 산출(5건 개정 블록 포함): `llm_outputs/2026-09-03/company_NVDA/` — PULSE · HANDOVER · DATAPACK · SOURCES ·
  SELF_SCORE · VALUE_CHAIN · DRIVER_TEST · MONEY_FORENSIC · SET_DIFF · VALUATION · FALSIFY · COMPANY_VERDICT

## 관측점 (날짜 박힘)
P129 DSO(11-18) · P130 capex 점유 갭(11-06) · P131 FQ3 GM(11-18) · P132 보증 노출(11-18) ·
S143 HF 공시 유무(09-30) · S144 Maia 300 1차출처(09-30)
