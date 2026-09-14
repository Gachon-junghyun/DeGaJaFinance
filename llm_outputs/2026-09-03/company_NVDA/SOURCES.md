# SOURCES — NVDA · 2026-09-03 · Stage 4/13 (L1·PRIMARY_SOURCE)

> **이 단계는 해석하지 않는다. 본문을 손에 넣는 것이 산출물이다.**
> 접속 시각 **KST 2026-09-03 11:0x~11:2x** (= ET 2026-09-02 22:0x~22:2x). 전부 `curl -sL --compressed` + UA 지정.
> ⚠ **시장 델타**: 이 종목은 US 다. KR 경로(FnGuide `c1050001.aspx` · DART `dsaf001→viewer.do` · IR PDF)는
> **해당 없음**. US 대응축은 아래 표대로 갈아탔고, 갈아탄 자리마다 **등급을 명시**한다.

---

## 0 · 세 축 × US 대응 — 무엇을 실제로 손에 넣었나

| 축 | KR 경로 (해당없음) | **US 에서 실제로 뜬 것** | 등급 |
|---|---|---|---|
| **컨센서스 추이** | FnGuide `c1050001.aspx` | ① yfinance `eps_trend` 90일 스냅샷 ② **데스크 자체 누적 `data/estimates/eps_*.json` 43일 실측 24파일** | ✅ **본문 확보 (2소스 교차)** · ⚠ **1년 전 대비는 미확보** |
| **부문 수주·잔고·연간계획** | 회사 IR 분기 PDF | 8-K EX-99.2 CFO Commentary **"Commitments"·"Additional Commitments"·"Guarantees"** 표 3개 | ✅ **본문 확보** · **수주잔고는 `none`** (§3) |
| **공시 본문의 문장** | DART `viewer.do` | **8-K 2026-08-17 전문** · **10-Q EX-10.1 계약 원문 43,964자** · EX-99.1/99.2 전문 | ✅ **본문 확보 (viewer 등급)** |

---

## 1 · ★★★ S130 Leg 1 — **NVDA 파일링에 Hugging Face 인수는 없다**

> HANDOVER §2d 가 이 스테이지의 1순위 dig 로 지정한 항목. `S130` 은 **2026-09-10 정산**이며
> Leg 1 의 관측면은 *"09-10 까지 **NVDA 회사 성명 또는 SEC 공시**가 그 인수를 명명하는가"* 다.

**EDGAR 전문검색 (efts.sec.gov, `q="Hugging Face"` · `ciks=0001045810`) — 전 기간 전 서식:**

| accession : file | 제출일 | Form |
|---|---|---|
| `0001045810-23-000171 : q2fy24pr.htm` | **2023-08-23** | 8-K |
| `0001045810-23-000175 : nvda-20230730.htm` | **2023-08-28** | 10-Q |
| `0001045810-24-000262 : q2fy25pr.htm` | **2024-08-28** | 8-K |

**총 3건, 전부 2023~2024년.** 2026년 문서는 **0건.**

**교차 확인 — 보도(2026-08-27) 이후 NVDA 가 제출한 8-K:**
`module_disclosure_us --days 120` 의 8-K 7건 전수 = **08-26 · 08-17 · 07-02 · 06-30 · 05-20 · 05-08**
⇒ **08-27 보도 이후 제출된 8-K 가 하나도 없다.** 마지막 8-K(08-26)와 마지막 10-Q(08-26)는 **보도 전날**이다.

### ⏳ Leg 1 의 현재 상태 — **명시적으로 점수가 아니다 (`D242`)**
**미확인 (unconfirmed)**, 정산까지 **7일 남음**. 이것은 *"부인됐다"* 가 아니라 *"명명한 1차 문서가 없다"* 이다.
- **VOID 조항은 발동하지 않았다**: VOID 는 *"NVDA 또는 HF 의 **회사 성명**에 의한 공식 부인"* 을 요구하는데,
  부인 성명도 **없다**. 보도 vs 보도는 VOID 가 아니라고 행이 명시했다.
- ⚠ **`D94` 적용 — 0건은 부재의 증거가 아닐 수 있다.** 다른 표면형으로 다시 물었다:
  검색어를 `"Hugging Face"` 단일 구문으로만 걸었고, 회사가 **코드네임이나 미명명 처리**했을 가능성은 남는다.
  다만 8-K 자체가 **08-27 이후 0건**이라는 사실은 표면형 문제가 아니다 — 그래서 이 결론은 두 다리로 선다.
- ⇒ **SET_DIFF·VALUATION 은 Hugging Face 인수를 «사실»로 쓸 수 없다.** 뉴스 4개 매체가 전부
  *"report says"* 였고(행의 등록 시점 기록), **1차 출처가 7일째 침묵**이다.

---

## 2 · ★★★ 컨센서스 추이 — 두 소스, 그리고 **상향이 언제 생겼는지**

### 2a · yfinance `eps_trend` (90일 룩백, asof 2026-09-03)

| 기간 | 현재 | 7일전 | 30일전 | 60일전 | 90일전 | 90일 변화 |
|---|---:|---:|---:|---:|---:|---:|
| 0q (FQ3 FY27) | 2.4698 | 2.3669 | 2.3453 | 2.3388 | 2.3388 | +5.6% |
| +1q | 2.7457 | 2.6822 | 2.6604 | 2.6473 | 2.6473 | +3.7% |
| 0y (FY27) | 9.2944 | 9.0173 | 8.9614 | 8.9374 | 8.9243 | +4.1% |
| **+1y (FY28)** | **15.4043** | 13.0410 | 12.8362 | 12.7102 | **12.6011** | **+22.2%** |

### 2b · ★ 데스크 자체 누적 스냅샷 — **독립 2번째 소스** (`D5` 프로바이더 교차)

`data/estimates/eps_*.json`, **24파일 / 2026-07-22 → 2026-09-03 (43 캘린더일)**.
NVDA 는 FY 가 1월 종료라 **이 구간 내내 `0y`=FY27 · `+1y`=FY28 로 라벨이 안 바뀐다** ⇒ 시계열 비교 가능.

| 스냅샷 일자 | `0y` (FY27) | **`+1y` (FY28)** | 비고 |
|---|---:|---:|---|
| **2026-07-22** (첫 스냅샷) | 8.98594 | **12.84363** | 프린트 35일 전 |
| **2026-08-21** | 9.00521 | **12.99922** | **프린트 5일 전** |
| **2026-09-03** (오늘) | 9.29436 | **15.40425** | 프린트 8일 후 |

★★★ **상향의 시점이 이 표에 박혀 있다**:

| 구간 | 일수 | `+1y` 변화 |
|---|---:|---:|
| 07-22 → **08-21** (프린트 **전**) | 30일 | **+1.21%** (12.84 → 13.00) |
| **08-21 → 09-03** (프린트 **포함**) | 13일 | **+18.50%** (13.00 → 15.40) |

⇒ **90일 룩백이 보여준 +22.2% 는 «추세»가 아니다. 프린트 하나가 만든 «점프»다.**
프린트 직전 한 달간 FY28 컨센은 **사실상 평평했다(+1.2%)**.
⚠ **이것이 `DATAPACK.md` §1b 를 정정하지는 않는다** — 거기 적힌 "+22.2%" 는 맞다. 여기서 더해지는 것은
**그 22%가 언제 생겼는가**이고, 그건 90일 표만 봐서는 **구조적으로 안 보인다**. 이게 이 스테이지의 존재 이유다.
⇒ **VALUATION 에 직접 물린다**: Fwd PER **14.57** 의 분모(Fwd EPS 15.40)는 **8일 된 숫자**다.

### 2c · ⚠ 미확보 — **1년 전 대비 컨센**
EXIT CHECK 이 요구하는 **1년 전 대비**는 **두 소스 모두 못 준다**: yfinance 는 90일이 최대,
데스크 스냅샷은 **첫 파일이 2026-07-22 = 43일**. 프로토콜 런타임 델타표가 US 를
*"유료 단말 축 — 미확보로 두고 자기 스냅샷 누적으로 대체"* 로 못박은 그 자리다.
⇒ **미확보로 남긴다. 소급 복구 불가**(스냅샷 도구 자체 경고). **1년 리비전 논거는 이 런에서 금지.**
🚨 그리고 그 누적이 **0.55개/일 = 이상 대비 1.8배 느리다**(PREFLIGHT G6 🔴 와 같은 수치) —
목표 40일치까지 실측속도로 **약 29일**. 오늘 이 결손이 다시 확인됐다.

---

## 3 · 부문 수주·잔고·연간계획 — **`none` 도 답이다**

- **수주잔고(backlog): NVDA 는 공시하지 않는다.** 프로토콜 런타임 델타표가 US 에 대해
  *"segment P&L 은 있으나 **수주잔고는 회사별로 없다**"* 라고 예고한 그대로다. ⇒ **`none` — 미제공 확인.**
- **대체축은 존재하고, 그것이 훨씬 크다**: 회사는 잔고 대신 **«미래 약정(future commitments)»** 표를 낸다.
  `DATAPACK.md` §6a/§6b 에 전문 인용 — **약정 $366bn + 추가 $56bn = $422bn**, **보증 최대노출 $108.5bn**.
- **연간 가이던스**: NVDA 는 **분기 가이던스만** 낸다(FQ3: 매출 $108.0bn ±2%, GM 74.0% ±50bp,
  opex GAAP $9.2bn). **연간 매출·이익 가이던스는 없다** — 다만 **FY27 세율 16.0~18.0%** 는 연간으로 준다.
- ⇒ **수주산업 프레임(잔고→미래매출)은 이 종목에 적용 불가.** VALUE_CHAIN 이 대신 쓸 물량 앵커는
  회사 자체 진술: *"PORTS-Pike 의 NVDA 인프라 **1세대 ≈ 150만 GPU ≈ 매출 $150~200bn**"* (8-K 99.2).

---

## 4 · 공시 본문 — **viewer 등급으로 뜬 것 3건**

> 「목록 요약만 봄」이 아니라 **본문 전문을 떴다**. 각 문서의 accession·URL·글자수를 적는다.

### 4a · 8-K **2026-08-17** — accession `0001045810-26-000069`
`https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm`
**Item 1.01 + Item 2.03 + 7.01 + 9.01.** 전문 직독 완료 — 인용은 `DATAPACK.md` §6b.
Item 2.03 표제 그대로: **"Creation of a Direct Financial Obligation or an Obligation under an
Off-Balance Sheet Arrangement of a Registrant"**, 본문은 *"The information set forth in Item 1.01
above is hereby incorporated by reference into this Item 2.03."*
⇒ **회사 스스로 이 보증을 «부외약정»으로 분류했다.**

### 4b · 8-K **2026-08-26** EX-99.1 / EX-99.2 — accession `0001045810-26-000073`
`.../000104581026000073/q2fy27pr.htm` (실적 보도자료) · `.../q2fy27cfocommentary.htm` (CFO 코멘터리)
전문 직독. 손익·BS·CF·세그먼트·약정·보증 전부 `DATAPACK.md` §2~§6.

### 4c · ★ 10-Q **2026-08-26** **EX-10.1 「FORM OF RESIDUAL VALUE GUARANTY」** — accession `0001045810-26-000075`
`https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda2027q2ex101.htm` · **43,964자 전문**
8-K 가 *"the form of which **will be filed as an exhibit to NVIDIA's Quarterly Report on Form 10-Q**
for the fiscal quarter ended July 26, 2026"* 라고 예고한 그 문서다. **예고대로 제출됐고, 이 런이 그것을 떴다.**

**계약 구조 (원문에서 직접):**
- 당사자: **NVIDIA Corporation = Guarantor** · Landlord = 델라웨어 LLC · **Tenant = `[***]` 비공개**
  · **Tenant Parent = `[***]`** (리스 전체 의무를 보증하는 joinder 를 이미 실행)
- 물건: **오하이오주 Piketon 시** 소재 부동산 (8-K 의 Pike County PORTS 캠퍼스와 일치)
- 곁가지 계약 2개가 **보증의 발효 조건**: **Power Affiliate 의 PPA**(소매 전력 구매) +
  **GridCo 향 Transmission Agreement**(송전망 업그레이드 완공 담보)
  → 원문: *"Landlord has agreed to enter into the Lease, and the Power Affiliate has agreed to enter
  into the PPA and the Transmission Agreement … **if and only if Guarantor executes and delivers to
  Landlord this Guaranty.**"*
  ⇒ ★ **NVDA 의 서명이 없으면 리스도 전력계약도 송전망 계약도 성립하지 않는다.** 보증은 부수조건이
  아니라 **프로젝트의 성립 조건**이다.
- **GMV(보증최소가치)의 구성**: *"the GMV … is comprised of **data center, power, and transmission
  related costs**, and that the GMV is related to **four and one quarter (4.25) GW of critical IT
  load** in the aggregate at the Premises and the Related Premises"* — Schedule II 로 추가 보증 시 조정.
- **Landlord's Equity 에 대한 IRR 정의**가 계약에 박혀 있다(XIRR, 부채상환 후 현금흐름 기준)
  ⇒ 임대인의 수익률이 보증 산식의 변수다.
- **보증 종료 사유 9개** — (iii) Tenant/Tenant Parent 가 신용등급 **`[***]`** 이상 기관의 은행보증·LC·
  보증증권 제공 · **(iv) Tenant 또는 Tenant Parent 가 신용등급 `[***]` 달성** ·
  (v) Replacement Tenant 가 신용등급 `[***]` 달성 · (vi)(vii)(viii) **`[***]` 3개 전부 비공개** ·
  **(ix) Commencement Date 의 20주년**
- **Guarantor Property 조항**: NVDA(또는 계열) 소유 장비가 Premises 안에 있고, 멸실·훼손 시
  **Tenant 가 NVDA 에 대체원가를 상환하고 면책**한다.

**🚨 미확보 (redaction) — 규모를 좌우하는 칸이 가려져 있다:**
문서 머리말: *"CERTAIN INFORMATION IDENTIFIED BY "[***]" HAS BEEN EXCLUDED … BECAUSE IT IS BOTH
NOT MATERIAL AND IS THE TYPE OF INFORMATION THAT THE REGISTRANT TREATS AS PRIVATE OR CONFIDENTIAL."*
- **Tenant 이름** = `[***]` — 8-K 는 OpenAI 라고 적었으나 **계약서 자체는 익명이다**
- **신용등급 문턱 값** = `[***]` — 8-K 의 *"satisfactory credit rating"* 이 **정확히 무엇인지 알 수 없다**
- **종료사유 (vi)(vii)(viii)** = `[***]`
- **GMV 의 실제 금액과 Schedule I/II** = 미첨부
⇒ **보증의 기대손실을 계산할 재료는 원문에도 없다.** `DATAPACK.md` §6d 의 `C3` unknown 열 유지.
⚠ 회사는 이 값들을 **"not material"** 로 분류했다 — 그 판단 자체가 관측대상이며, FALSIFY 가 다룬다.

---

## 5 · 못 뜬 것 — 「미확보」로 남긴다 (P4)

| 항목 | 왜 못 떴나 | 등급 |
|---|---|---|
| **1년 전 컨센서스** | yfinance 90일 한계 + 데스크 스냅샷 43일. **소급 복구 불가** | 🔴 미확보 (구조적) |
| **보증 GMV 금액 / 신용등급 문턱 / Tenant 명** | 계약서에서 `[***]` 로 **적법 삭제** | 🔴 미확보 (발행인 삭제) |
| **Form 144 6건 · Form 4 22건** | 미파싱 (§DATAPACK §8 이 4건만 파싱) | 🟡 부분 — MONEY_FORENSIC 과제 |
| **Form 4 의 10b5-1 플랜 각주** | XML 각주 미확인 | 🟡 부분 — MONEY_FORENSIC 필수 |
| **424B5 2건이 동일 딜인지** | 두 accession 의 diff 미수행 | 🟡 부분 |
| **ACIE→Hyperscale 재분류된 회사명** | 회사 미공개 | 🔴 미확보 |
| **10-Q 본문(1.5MB)의 우발채무 주석** | 이 스테이지는 EX-10.1 을 우선했다. 본문 주석 미독 | 🟡 **다음 스테이지 과제** |

⚠ **후퇴 신호 없음** — 캡차·429·로그인 벽을 만나지 않았다. `efts.sec.gov` 와 `www.sec.gov/Archives`
둘 다 UA 지정 + `--compressed` 로 정상 응답. 재시도·우회 시도 0회.

---

## 6 · 지도에 등록할 것 (등록 안 하면 다음 사람이 같은 벽에 박는다)

1. ★ **US 판 「DART viewer 함정」의 대응물**: `module_disclosure_us` 는 8-K 를 **분류만 하고
   exhibit 를 안 가져온다.** 실제 숫자(세그먼트·약정·보증)는 전부 **EX-99.1/99.2 안**에 있다.
   경로: `https://www.sec.gov/Archives/edgar/data/{CIK}/{accession_nodash}/index.json` 로
   **파일 목록을 JSON 으로 받는다** — 디렉토리 HTML 을 긁는 것보다 확실하다(실측: HTML 긁기는
   SEC 사이트 네비게이션 링크만 돌려줬다).
2. ★ **8-K 가 「10-Q 에 exhibit 로 낸다」고 적으면 그 10-Q 의 `index.json` 을 봐라.** 이번 건은
   `nvda2027q2ex101.htm` 이 그 자리에 있었고, **계약 원문 43,964자**가 목록 요약에는 한 줄도 안 나온다.
3. ★ **EDGAR 전문검색 API**: `https://efts.sec.gov/LATEST/search-index?q=%22구문%22&ciks=0001045810`
   — 로그인·키 없음. 특정 발행인의 전 파일링에서 구문 존재 여부를 **초 단위**로 판정한다.
   **사전공약 브래킷의 「회사가 이걸 공시했나」 레그를 채점하는 정확한 도구다.**
4. 🚨 **`module_disclosure_us` 의 카테고리 맵에 증권발행 축이 없다** — **424B5 2건 + FWP 1건이
   「기타 20건」에 묻혔다.** $25bn 채권발행이 digest 요약에서 안 보인다. (`DATAPACK.md` §9 와 동일 dig)
5. ⚠ **`module_valuation` 은 US 티커에 6자리 0-패딩(`00NVDA`)을 해서 네이버를 친다** — 공란표가 나온다
   (`DATAPACK.md` §7a).

---

## ✅ EXIT CHECK

- [x] **컨센서스 추이 표가 실제로 손에 있다** — 현재값만이 아니다(§2a 90일 4스냅샷 + §2b 데스크 자체 43일 3점).
      ★ 그리고 **상향이 프린트 전 30일 +1.2% vs 프린트 포함 13일 +18.5%** 로 분해됐다.
      ⚠ **1년 전 대비는 미확보**로 명시(§2c) — 없는 걸 있는 척하지 않았다
- [x] **부문 수주·잔고·연간계획** — **잔고 `none`(회사 미공시 확인)**, 대체축인 약정 $422bn·보증 $108.5bn 표를
      텍스트로 확보, 연간 가이던스는 세율만 존재함을 명시(§3)
- [x] **되돌릴 수 없는 절차가 걸린 공시는 viewer 본문을 떴다** — 8-K 08-17 전문 · **10-Q EX-10.1 계약원문
      43,964자** · EX-99.1/99.2 전문(§4). 「요약만 봄」으로 남은 것은 10-Q 본문 주석 하나이며 §5 에 등급 표기
- [x] **뜬 것마다 accession · URL · 접속시각**이 붙었다. 못 뜬 것 7건은 이유와 함께 미확보(§5)
- [x] **새 사이트·함정 5건 등록**(§6) — 특히 `index.json` 경로와 EDGAR 전문검색 API
- [x] ★ **HANDOVER 의 1순위 dig(`S130` Leg 1)에 답을 냈다**: **NVDA 파일링에 Hugging Face 인수는 없다**
      (EDGAR 전 기간 3건, 전부 2023~2024). 정산 7일 전, `D242` 준수해 **점수가 아님**을 명시
- [x] **해석하지 않았다** — 본문과 인용만. 판단은 하류 (P4)
