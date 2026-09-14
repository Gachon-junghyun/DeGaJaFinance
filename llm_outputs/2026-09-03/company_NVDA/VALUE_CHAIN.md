# VALUE_CHAIN — NVDA · 2026-09-03 · Stage 6/13 (L1·VALUE_CHAIN)

> **숫자를 세기 전에 구조를 세운다.** ① 사슬 어디에 서 있나 ② 무엇을 팔고 왜 남이 못 만드나
> ③ 계약이 매출과 **현금**이 되기까지 얼마나 걸리나 ④ 수요의 뿌리는 무엇인가.
> **이 단계는 값을 매기지 않는다.** 해자가 깊다는 사실은 «이익»의 근거지 «가격»의 근거가 아니다.
> 출처: 10-K FY2026 (acc `0001045810-26-000021`, 2026-02-25) · 8-K/10-Q 2026-08-26 · 8-K 2026-08-17.

---

## 0 · 연결/부문 구분 — **첫 표에서 명시한다**

| 구분 | Q2 FY27 매출 | 비중 | 비고 |
|---|---:|---:|---|
| **연결 총매출** | **$96,221M** | 100% | |
| ├ **Compute & Networking** (보고 세그먼트) | 88,299 | **91.77%** | |
| └ Graphics | 7,922 | 8.23% | |
| *(플랫폼 뷰)* Data Center | 89,023 | 92.52% | Hyperscale 48,710 + ACIE 40,313 |
| *(플랫폼 뷰)* Edge Computing | 7,198 | 7.48% | |

- ✅ **상장 자회사 없음 ⇒ `holdco_split` 해당 없음.** 034020 형 「연결 매출이 남의 이익을 섞고 있다」
  문제는 이 종목에 **없다**. 연결 = 실질 본체다. **분모 오염 0.**
- ⚠ **단, 다른 종류의 분모 오염이 있다**: GAAP 순이익의 **20.1%(6개월)가 지분증권 평가익**이며
  이건 «영업»이 아니다(`DATAPACK` §4). 세그먼트 표는 매출만 나누고 그 이익은 안 나눈다.

---

## 1 · ① 사슬 위치 — **있는 단계와 없는 단계를 둘 다 적는다**

**AI 인프라 사슬 (전력에서 토큰까지):**

```
① 전력생산·계통  ② 부지·전력·건물(shell)  ③ 냉각·배전  ④ HBM 메모리  ⑤ 웨이퍼 파운드리
   ⑥ 첨단패키징(CoWoS)  ⑦ 조립·테스트(ODM)  ⑧ ★GPU/CPU 설계 + 시스템·네트워킹 + 소프트웨어★
   ⑨ 데이터센터 운영(CSP/네오클라우드)  ⑩ 모델 학습·추론  ⑪ 애플리케이션·토큰 판매
```

| 단계 | NVDA 위치 | 근거 (10-K Item 1) |
|---|---|---|
| ⑤ 파운드리 | ❌ **없다** — 위탁 | *"We utilize foundries, such as **TSMC** and **Samsung**, to produce our semiconductor wafers"* |
| ④ HBM | ❌ **없다** — 구매 | *"We purchase memory from **SK Hynix, Micron, and Samsung**"* |
| ⑥ 패키징 | ❌ **없다** — 위탁 | *"We utilize **CoWoS** technology for semiconductor packaging"* |
| ⑦ 조립·테스트 | ❌ **없다** — 위탁 | *"**Hon Hai, Wistron, Fabrinet** to perform assembly, testing and packaging"* |
| **⑧ 설계+시스템+네트워킹+SW** | ✅ **여기 있다. 유일하게 여기다** | *"chips, networking, systems, software, and algorithms are **holistically architected**"* |
| ⑨ DC 운영 | ❌ **없다** — 그러나 ★2026년에 **경계가 무너졌다** (§3c) | |
| ①②③ 전력·부지·냉각 | ❌ **없다** — 그러나 ★**보증으로 리스크는 들어왔다** (§3c) | 8-K 2026-08-17 |
| ⑩⑪ 모델·앱 | ❌ **없다** — 그러나 ★**지분으로 들어갔다** ($94.0bn 지분증권, §3c) | |

★★ **이 표가 이 런의 핵심 구조 발견이다.**
**NVDA 는 사슬의 «한 칸»(⑧)에서만 물건을 만든다.** 그런데 **2026년에 ①②③⑨⑩⑪ 여섯 칸에
«소유 없이 리스크만» 들어갔다** — 보증($108.5bn), 지분($94.0bn), 리스 재배정($20bn), 매출쉐어 계약.
**한 칸에서 벌고, 일곱 칸의 위험을 진다.** 이게 사슬 위치의 정확한 서술이다.
「종합 AI 인프라 기업」이라고 쓰면 이 비대칭이 통째로 사라진다.

---

## 2 · ② 제품과 해자 — **세어지는 형태로만**

### 2a · 제품군

| 제품군 | 무엇 | 누가 사나 | 성격 |
|---|---|---|---|
| **Data Center 가속 플랫폼** (Blackwell Ultra → **Vera Rubin**) | GPU + CPU + NVLink + 스위치 + 시스템을 **랙 단위 통짜 설계** | CSP·AI 모델메이커·네오클라우드·소버린·엔터프라이즈 | **$89.0bn = 매출의 92.5%.** 아키텍처 2년 주기 |
| **네트워킹** (Spectrum-6, NVLink, InfiniBand) | 스케일업/스케일아웃 인터커넥트 | 위와 동일 | C&N 세그먼트에 합산 — **별도 공시 없음 = 미확보** |
| **소프트웨어 (CUDA + 라이브러리/SDK/API 수백종)** | 개발 플랫폼 | 개발자 생태계 | ★ 해자의 본체. **매출 별도 공시 없음 = 미확보** |
| **Edge / Graphics** (GeForce, RTX, 워크스테이션) | 게이밍·프로 비주얼·워크스테이션 | 소비자·OEM | $7.2bn = 7.5%. **회사 스스로 "메모리·시스템 가격 상승에 눌린 소비자 PC 판매"로 성장 둔화 설명** |
| **자동차·로보틱스** | DRIVE, Isaac, GR00T | OEM·티어1 | C&N 에 합산 — **별도 공시 없음 = 미확보** |

### 2b · 해자 — **세어지는 것만 적는다** (형용사 금지)

| 해자 | **세어지는 형태** | 출처 | 강도 판정 |
|---|---|---|---|
| **누적 R&D** | **$76.7bn** 누적 투자 | 10-K Item 1 | 재현 비용의 하한 |
| **CUDA 설치기반** | 🔴 **NVDA 는 개발자 수·설치 GPU 수를 공시하지 않는다** — *"large and growing number of developers"* 라는 **형용사만** 준다 | 10-K Item 1 | ⚠ **미확보. 이 데스크는 CUDA 해자를 «숫자로» 인용할 수 없다** |
| **랙 스케일 통합** | 1세대 캠퍼스 = **약 150만 GPU** 를 **하나의 컴퓨터**로 묶는 설계 | 8-K 99.2 | ⚠ 회사 자체 추정 |
| **파운드리 대안 개수** | **2** (TSMC, Samsung) — 단, 최선단·CoWoS 실효 대안은 미공시 | 10-K | 🟡 |
| **HBM 공급사 개수** | **3** (SK하이닉스·마이크론·삼성) | 10-K | 🟡 |
| **조립 파트너 개수** | **3** (홍하이·위스트론·파브리넷) | 10-K | 🟡 |
| **패키징 기술** | **CoWoS 1종**에 명시적 의존 | 10-K | 🔴 **단일 기술 의존** |

★ **해자의 방향이 갈린다**: **소프트웨어 쪽(CUDA)은 세어지지 않고**, **하드웨어 쪽은 세어지는데
전부 «남의 개수»다** — 파운드리 2, HBM 3, 조립 3, 패키징 1.
⇒ **034020 의 「1만7천톤 프레스 보유사 전 세계 4곳」 같은 «내가 가진 물리적 희소성»은
이 회사에서 나오지 않는다.** NVDA 의 희소성은 **설계·소프트웨어**에 있고 그건 이 팩의 1차 출처에서
**개수로 증명되지 않는다.** ⇒ 🚫 **하류 스테이지는 "CUDA 락인"을 «측정된 해자»로 인용할 수 없다.**
(`[inferred]` 로만 운반 가능.)

### 2c · 🔴 해자가 «세어지는 형태로» 공격받고 있는 자리 — `M717` (c) 다리 재측정

`SELF_SCORE` §1a 가 미확인으로 남긴 다리를 여기서 잰다.

| 항목 | 값 | 출처·등급 |
|---|---|---|
| 대체재 이름 | **Microsoft Maia 300** | `yahoo_finance` 2026-08-10 · `economictimes` 08-11 |
| 날짜 | **올가을 / 이르면 9월 공개** | 〃 |
| 수량 | **300,000 유닛 목표** | 〃 |
| 공동설계 수혜자 | **Marvell (MRVL)**, TSMC | `yahoo_finance` 08-11 "Maia 300 Could Be a Win for Marvell and TSMC" · 08-25 Rosenblatt: *"custom-silicon ramps in fiscal 2028 and 2029 tied to Microsoft Maia"* |
| 다른 대체재 | **AWS Trainium** · **Google TPU** · **Meta MTIA** | 08-17 "Who's Really The King of Custom Silicon" |

⇒ **`M717` (c) 는 유지된다 — 이름·날짜·수량이 박힌 대체재가 실재하고, 30일 뉴스축에서
1,148건이 매칭된다.** ⚠ 등급: **전부 «보도»이며 1차 출처(MSFT 공시/발표) 미확인 = `[news]`.**
⚠ **`W4` 준수 — 고객을 이름으로 세운다**: 이 대체재를 만드는 주체는 **NVDA 의 최대 고객군 그 자체**다
(§2d). 대체재 리스크와 고객집중 리스크는 **같은 한 명**이다.

### 2d · 🚨 고객 집중 — **세어지는 형태, 그리고 악화 중**

| 회계연도 | 직접고객 집중 | 상위 2사 합 |
|---|---|---:|
| FY2024 | 1사 13% | — |
| FY2025 | 1사 12% · 2사 각 11% | **23%** (상위2) |
| **FY2026** | **1사 22% · 다른 1사 14%** | **36%** |

★ **상위 2 직접고객 비중이 FY25 23% → FY26 36% = 1년에 13pp 상승.** 전부 C&N 세그먼트.
그리고 10-K 원문:
> *"Our revenue is concentrated among a limited number of direct and indirect customers and **this
> trend may continue**."*
> *"We estimate that **one AI research and deployment company** contributed to a meaningful amount of
> our revenue **purchasing cloud services from our customers** in fiscal year 2026."*

⇒ ★★★ **마지막 문장이 순환구조를 회사 스스로 적은 자리다.** 한 «AI 연구·배포 회사»가
**NVDA 의 고객으로부터 클라우드를 사서** NVDA 매출에 유의미하게 기여했다. 그리고 2026-08-17,
NVDA 는 **바로 그 성격의 회사(OpenAI)의 리스료를 $105bn 한도로 보증**했다.
**10-K 의 이 한 문장과 8-K 의 보증은 같은 하나의 사실이다.**

---

## 3 · ③ 돈이 되는 경로 — 계약 → 매출 → 현금의 시차와 그 사이 계정

### 3a · 시차 구조 — **034020 과 정반대다**

두산에너빌리티는 **진행률 인식**이라 「오늘 매출 = 2~4년 전 계약」이고 수주잔고가 미래매출이었다.
**NVDA 는 시점 인식(제품 인도)이다.** ⇒ **수주잔고가 없고(회사 미공시, `SOURCES` §3),
매출은 출하와 거의 동시에 잡힌다.** 그래서 미래매출의 앵커가 잔고가 아니라 **약정(commitments)**이다.

```
[상류] 공급약정 $279bn (주로 메모리 선매입)  ──►  재고 $31.6bn (119.3일)
                                                      │  Vera Rubin 램프 대비 선재고
                                                      ▼
[인식] 제품 인도 시점에 매출 인식  ──►  매출채권 $63.1bn
                                                      │  ★DSO 45일 → 60일
                                                      ▼
[현금] OCF $24.1bn (순이익의 40.3%)  ──►  자사주 $19.7bn + 배당 $6.0bn
                                                      ▲
                                          부채 $24.9bn 조달로 보충
```

### 3b · 그 사이에 쌓이는 계정 — 실측

| 계정 | 2026-07-26 | 2026-01-25 | 변화 | 회전 지표 |
|---|---:|---:|---:|---|
| **매출채권** | $63,059M | $38,466M | **+63.9%** | **DSO 60일** ← 직전분기 **45일** |
| **재고자산** | $31,575M | $21,403M | +47.5% | **119.3일** (COGS 기준) |
| 매입채무 | $15,059M | $9,812M | +53.5% | |
| 계약자산/계약부채 | — | — | — | **NVDA 는 별도 공시 안 함 = 미확보** |

**회사가 DSO 상승의 이유를 스스로 적었다**:
> *"Accounts receivable was $63.1 billion with 60 days sales outstanding (DSO), up from 45 days
> sequentially, **due to extended payment terms on large, multi-quarter agreements with certain
> investment-grade customers**."*

⇒ ★ **이 구조를 미리 세워두면 MONEY_FORENSIC 이 OCF/NI 0.403 을 「이상」이 아니라
「성장 선재고+결제조건 연장인지, 회수 부실인지 아직 모름」으로 정확히 등급 매길 수 있다.**
⚠ 그리고 **회사 자신의 설명 안에 검증 가능한 주장이 하나 있다 — "investment-grade customers".**
§2d 의 «한 AI 연구·배포 회사»와 §3c 의 보증 대상(신용등급을 아직 못 받은 임차인)이
**investment-grade 인지 아닌지**가 그 주장의 시험대다. → **MONEY_FORENSIC 과제.**

### 3c · ★★★ 2026년에 새로 생긴 «두 번째 수익 경로» — 이게 이 회사의 구조 변화다

10-K(2026-02) MD&A 가 이 변화를 **미리 진술했다**:
> *"The availability of data centers, energy, and **capital** to support the buildout of NVIDIA AI
> infrastructure by our customers and partners is crucial… **access to capital can be particularly
> constrained for less-capitalized companies**, which may face difficulties securing financing for
> large-scale infrastructure."*

그리고 6개월 뒤 CFO 코멘터리(2026-08-26)가 **그 대응을 적었다**:
> *"AI clouds and model makers… **many are growing faster than their balance sheets and long-term
> credit profiles can support**. In response, we have entered into arrangements that help select
> customers secure the land, power and data center capacity needed to support their growth."*
> *"we will earn revenue on the upfront sale of our infrastructure and **if certain criteria are met,
> we will participate in revenue share** generated by the AI clouds from their third-party customers."*

**새 경로를 사슬 그림으로:**

```
NVDA 지분투자 ($94.0bn)  ──►  AI 모델메이커 / 네오클라우드 / 인프라 파이낸서
       │                              │
       │ 평가익 (GAAP 순이익의 20.1%) │ 이들이 NVDA GPU 를 산다 → 매출
       ▼                              ▼
   NVDA 순이익                    NVDA Data Center 매출 $89.0bn
       ▲                              ▲
       │                              │
NVDA 보증 ($108.5bn) ──► 임대인(SB Energy) ──► 리스 성립 ──► OpenAI 가 입주
       │                                                        │
       └── 리스는 NVDA 서명 «없이는 성립하지 않는다» ◄───────────┘
           (EX-10.1: "if and only if Guarantor executes and delivers this Guaranty")
```

**세어지는 형태로**:

| 새 경로의 크기 | 값 | 출처 |
|---|---:|---|
| 지분증권 보유 (시장성 + 비시장성) | **$93,940M** (42,783 + 51,157) | BS 2026-07-26 |
| 6개월 지분증권 순취득 | **$42,404M** | CF |
| 6개월 지분증권 평가·처분익 | **$23,707M = GAAP 순이익의 20.1%** | CF |
| **보증 최대 총노출** | **$108,500M** (SB Energy 105.0 + AI클라우드 3.5) | 8-K 99.2 |
| 약정 총계 (공급·클라우드·리스·지분·capex) | **$366bn** + 추가 **$56bn** = **$422bn** | 8-K 99.2 |
| 제3자 재배정 예정 DC 리스 | **$20bn**, 15년, FY28~29 개시 | 8-K 99.2 |
| 회사 추정 PORTS-Pike 1세대 매출 | **$150~200bn** (약 150만 GPU) | 8-K 99.2 |

⚠ **보증의 시차**: 8-K 는 첫 효력 발생을 **FY2029**(ready-for-service 조건)로 적었다.
⇒ **오늘의 손익에는 한 푼도 안 들어와 있고, 오늘의 대차대조표에도 «부외»다**
(Item 2.03 표제가 *"Off-Balance Sheet Arrangement"*).
**그래서 이 구조는 배수로도, 발생액으로도, 재무비율로도 안 보인다.** 여기서 안 쓰면 영영 없다.

---

## 4 · ④ 수요의 뿌리 — **「이미 일어난 일」 / 「계획·전망」을 갈라서**

| # | 근거 | **이미 일어난 일 (측정됨)** | **계획·전망 (아직 아님)** |
|---|---|---|---|
| 1 | Data Center 매출 | **$89.0bn, Y/Y +117%, Q/Q +18%** — 정산된 분기 실적 | — |
| 2 | ACIE (AI네이티브·엔터프라이즈·소버린) | **$40.3bn, Y/Y +138%, 분기 스윙의 55.6%** | — |
| 3 | Vera Rubin | **"full production" 진입, CoreWeave·Google Cloud·Azure·OCI·Nebius 랙 가동** (회사 진술) | 매출 기여는 **FQ3 부터** |
| 4 | FQ3 가이던스 | — | **매출 $108.0bn ±2%** (회사 전망) |
| 5 | 공급약정 | **$119bn → $279bn 로 실제 체결됨** (계약은 일어난 일) | 그 물량이 팔릴지는 전망 |
| 6 | PORTS-Pike 캠퍼스 | **보증계약 서명됨 (2026-08-17)** · 부지 오하이오 Piketon | **4.25GW 는 미준공**, 첫 ready-for-service **FY2029**, 매출 $150~200bn 은 **회사 추정** |
| 7 | OpenAI 임차 | **리스 joinder 실행됨** (EX-10.1 recital B) | 20년 리스료 지급능력은 **미검증** |
| 8 | 중국 데이터센터 | **당분기 Hopper 출하 = DC 매출의 1% 미만** (일어난 일: 거의 없음) | **가이던스에 0으로 반영** — 상방옵션이자 미확정 |
| 9 | 컨센 FY28 EPS 15.40 | — | **전망. 그리고 그 +18.5%가 8일 전 프린트 하나로 생겼다**(`SOURCES` §2b) |

★ **갈라 적으니 남는 것**: **수요의 «이미 일어난» 증거는 강하다** — 1·2·5 는 정산된 숫자이고,
Y/Y +117% 는 전망이 아니라 실적이다. **약한 자리는 «지속»이 아니라 «누가 낼 것인가»다** —
6·7·8·9 가 전부 **아직 안 일어난 칸**이고, 그중 6·7 은 **NVDA 자신이 보증으로 떠받치는 칸**이다.

⚠ **`W3` — real ≠ profitable**: 위 표는 수요가 **실재**함을 보인다. 그것이 **주주에게 남는지**는
이 스테이지가 답하지 않는다(값을 매기지 않는다). SET_DIFF·VALUATION 의 몫이다.

---

## 5 · 이 구조가 하류에 넘기는 것

1. **DRIVER_TEST 의 분모는 확정됐다**: Data Center 92.5%, 그 안에서 **스윙의 55.6%가 ACIE**.
   하이퍼스케일 단일 드라이버 모델은 **회사의 44%를 설명하고 56%에 침묵한다.**
2. **MONEY_FORENSIC 의 과녁 3개**: ① DSO 45→60 의 "investment-grade customers" 주장 검증
   ② GAAP 순이익의 20.1%인 지분평가익의 성격 ③ 나머지 Form 4/144 파싱.
3. **SET_DIFF 의 «값에 안 든 것» 후보**: **보증 $108.5bn 과 약정 $422bn 은 어떤 배수에도 안 들어간다.**
   PER·PBR·EV/EBITDA 전부 이 항목을 못 본다.
4. **FALSIFY 의 최강 각도**: §2b — **이 회사의 해자는 «내 것»이 아니라 «남의 개수»로만 세어진다**,
   그리고 그 «남»이 곧 최대 고객이자 대체재 제조자다(§2c·§2d).

---

## ✅ EXIT CHECK
- [x] **사슬 단계가 적혔고 있는 단계(⑧ 하나)와 없는 단계(①~⑦·⑨~⑪)가 둘 다 명시**(§1) —
      그리고 «소유 없이 리스크만 들어간» 여섯 칸을 별도로 표시
- [x] **제품군 표 존재**(§2a), **해자를 세어지는 형태로**(§2b): R&D $76.7bn · 파운드리 2 · HBM 3 ·
      조립 3 · CoWoS 1 · 150만 GPU/캠퍼스. 🔴 **CUDA 는 회사가 숫자를 안 줘서 «미확보»로 명시** —
      형용사를 해자로 승격시키지 않았다
- [x] **계약 → 매출 → 현금의 시차와 그 사이 계정**(§3a/§3b): 시점 인식 · 잔고 없음 · **DSO 45→60일** ·
      재고 119.3일 · 공급약정 $279bn. 계약자산/부채는 미공시로 표기
- [x] **수요 근거가 「일어난 일」/「계획·전망」 두 열로 갈렸다**(§4) — 9개 항목 전수
- [x] **연결/부문 구분이 첫 표에서 명시**(§0), **상장 자회사 없음 ⇒ `holdco_split` 해당 없음**을 명기
      (재계산하지 않았다)
- [x] **값을 매기지 않았다** — 목표주가·배수·매수매도 언어 0 (P4)


---

# 🔄 개정 1 — 2026-09-03 (사후 탐색) · **§2c 가 한 세대를 놓쳤다**

> `D48`: 원문 유지, 반박 첨부.

## §2c 정정 — 대체재는 «9월에 올 것»이 아니라 **«1월에 이미 왔다»**

원문은 `Maia 300`(9월 공개·30만 유닛, 전부 `[news]`)만 추적했다.
**마이크로소프트 자기 뉴스룸**(`news.microsoft.com/source`, 브라우저 직독)을 열어보니:

> *"Our newest AI accelerator **Maia 200 is now online in Azure**. Designed for industry-leading
> inference efficiency, it delivers **30% better performance per dollar than current systems**…
> It joins our broader portfolio of CPUs, GPUs and custom accelerators, giving customers more
> options to run advanced AI workloads faster and more cost-effectively on Azure."*
> — **2026년 1월 26일**, 마이크로소프트 1차 출처

| | 원문이 알던 것 | 실제 |
|---|---|---|
| Maia **300** | 9월 공개·30만 유닛 (`[news]`) | **마이크로소프트 뉴스룸 0건** — `[news]` 등급은 옳았다 |
| Maia **200** | **언급 없음** | 🔴 **2026-01-26 부터 Azure 가동 중**, 회사 자체 주장 **성능/달러 +30%** |

⇒ **틀린 것은 등급이 아니라 «어느 세대를 보고 있었나»** 다. 대체 위협을 «다가올 미래»로 잡으면
**이미 배치된 현재**를 놓친다.

★ **이것이 `DRIVER_TEST` §2a 의 −16.5pp 갭에 «날짜가 맞는» 후보를 준다** —
고객 capex 는 QoQ +29.6% 인데 NVDA 하이퍼스케일 매출은 +13.1% 만 늘었고,
그 분기(2026-04~06)는 **Maia 200 이 Azure 에 들어간 뒤**다.
⚠ **인과가 아니라 시점 일치**이며, 분모(30만 유닛이 NVDA 물량의 몇 %인가)는 여전히 `미확보` 다.

## §2b 보강 — CUDA 해자는 **브라우저로도 숫자가 안 나온다** (확인함)
`developer.nvidia.com/cuda-zone` 본문을 직독했다. **개발자 수·설치 GPU 수 숫자가 없다.**
⇒ 원문의 *"측정된 해자로 인용 불가"* 판정은 **유지되고, 이제 헛걸음까지 기록됐다**
(`module_webctl/site_map.json` 에 등록).
