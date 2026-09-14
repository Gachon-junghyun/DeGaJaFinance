# UPGRADE_PROBE — NVDA 런 사후 탐색 · 2026-09-03

> 프로토콜 완주 후, **미확보로 남긴 칸 중 실제로 닫을 수 있었던 것**을 실험·브라우저로 다시 친 기록.
> 목적은 보고서 수정이 아니라 **다음 런의 규칙을 바꾸는 것**이다.
> 도구: EDGAR 전문검색·XBRL·Form4/144 직파싱 · `module_webctl`(CDP 9222, Chrome 151) · yfinance 교차.

---

## A · 분석을 실제로 바꾸는 발견 (4건)

### A1 🚨🚨 **「ACIE 고객은 감사받는 대응 계열이 구조적으로 없다」는 틀렸다**

`DRIVER_TEST` §2b · `SET_DIFF` R1 · `FALSIFY` B-4 가 전부 이 전제 위에 서 있었다. **반박된다.**

**NVDA 자기 8-K(2026-08-26 EX-99.1)가 Vera Rubin 파트너를 이름으로 댔다** —
CoreWeave · Google Cloud · Microsoft Azure · Oracle Cloud · **Nebius**.
그중 **CoreWeave(CRWV)와 Nebius(NBIS)는 상장사이고 10-Q 를 제출한다.**

| | CoreWeave (CRWV) | Nebius (NBIS) |
|---|---:|---:|
| 시가총액 | $44.6bn | $55.5bn |
| **총차입금** | **$51.6bn** | $10.2bn |
| 현금 | $5.5bn | $8.0bn |
| EBITDA | $3.8bn | $0.3bn |
| **차입금/EBITDA** | **13.6배** | **34배** |
| 선행 PER | **−41.5 (적자)** | **−68.1 (적자)** |
| 최근 분기 매출 | $2.58bn (2026-06) | $0.40bn (2026-03) |

⇒ **NVDA CFO 가 쓴 *"many are growing faster than their balance sheets and long-term credit
profiles can support"* 는 수사가 아니라 «측정 가능한 서술»이었다.** 이 두 회사가 그 문장의 실체다.

### A2 🚨🚨🚨 **순환이 «상대방의 감사받는 공시»에서 양쪽으로 문서화된다**

CoreWeave 10-Q (2026-06-30 분기, acc `0001769628-26-000366`) 원문:

> *"**In January 2026, we entered into a securities purchase agreement with NVIDIA Corporation for a
> private placement of approximately 23 million shares of our Class A common stock at a purchase
> price of $87.20 per share, for aggregate gross proceeds of $2.0 billion.**"*
> *"as a result of our obligations in our current customer contracts, **all of the GPUs used in our
> infrastructure today are NVIDIA GPUs**"*
> *"**our current customers have contractually specified our use of NVIDIA GPUs**"*

**루프가 닫힌다, 전부 1차 출처로**:
`NVDA 가 CRWV 지분 $2.0bn 매입` → `CRWV 는 전량 NVDA GPU 만 구매(계약상 강제)` →
`NVDA 매출 인식` → `NVDA 가 CRWV 지분 평가익 인식`.

**그리고 그 지분은 지금 손실 중이다** (측정):

| | 값 |
|---|---:|
| 매입 (2026-01) | 23,000,000주 × **$87.20** = **$2.006bn** |
| 시가 (2026-09-02) | 23,000,000주 × **$80.93** = **$1.861bn** |
| **평가손익** | **−$144M (−7.19%)** |

⇒ `MONEY_FORENSIC` B2-c 가 "지분평가익 $23.7bn(6M)"을 **총액으로만** 다뤘는데,
**개별 포지션 단위로 검증 가능하다.** 최소 한 건은 **손실**이다.

### A3 ★★ **대체재는 «9월에 올 것»이 아니라 «1월에 이미 왔다»**

`VALUE_CHAIN` §2c 는 Maia **300**(9월·30만유닛, 전부 `[news]`)만 추적했다.
**마이크로소프트 자기 뉴스룸(news.microsoft.com/source)을 브라우저로 열어보니**:

> *"Our newest AI accelerator **Maia 200 is now online in Azure**. Designed for industry-leading
> inference efficiency, it delivers **30% better performance per dollar than current systems**…
> It joins our broader portfolio of CPUs, GPUs and custom accelerators."* — **2026년 1월 26일**

- **Maia 200 = 1차 출처 있음, 이미 가동 중, 성능/달러 30% 우위를 회사가 직접 주장.**
- **Maia 300 = 마이크로소프트 뉴스룸에 없음** (검색 결과 6건 중 0건) ⇒ `[news]` 등급 유지가 맞았다.

★ **이것이 `DRIVER_TEST` §2a 의 −16.5pp 갭에 이름 붙은 후보를 준다.**
고객 capex 는 +29.6% 늘었는데 NVDA 하이퍼스케일 매출은 +13.1% 만 늘었다.
**Maia 200 이 2026-01 에 Azure 에 들어갔다** — 갭이 벌어진 분기(2026-04~06)와 시점이 맞는다.
⚠ 인과가 아니라 **날짜가 맞는 후보**다. `P130`(11-06 정산)이 이제 훨씬 날카로워진다.

### A4 ★ 내부자 — 미확보였던 「보유의 몇 %」가 나온다

Form 4 XML 에는 `<sharesOwnedFollowingTransaction>` 과 `<directOrIndirectOwnership>` 이 있다.
`MONEY_FORENSIC` B3-a 가 *"잔여 보유량 미파싱 ⇒ 확신 상실로 읽을 수 없다"* 로 남긴 칸이 닫힌다:

| 항목 | 값 |
|---|---:|
| Stevens 2026-09-02 매도 | 1,848,501주 — **전량 `I` (간접) · `By Trust`** |
| 그 신탁 라인 거래後 잔량 | **3,358,770주** |
| **하루에 판 비중 (해당 라인)** | **35.5%** (1,848,501 ÷ 5,207,271) |

⚠ **함정 발견**: 여러 Form 4 의 `sharesOwnedFollowingTransaction` 을 그냥 «마지막 값»으로 읽으면
11,543,401 → **15,017,750 으로 «늘어난다»**. 직접/간접 라인이 섞이고 accession 도 섞이기 때문이다.
**`directOrIndirectOwnership` + `natureOfOwnership` 로 라인을 갈라야 한다.**

---

## B · 🚨 가장 큰 것 — **비상장이라도 «상대방의 지분법»으로 측정된다**

`SET_DIFF` R1/R2 와 `FALSIFY` 가 *"OpenAI 의 지급능력은 이 데스크가 접근 가능한 어떤 1차 출처로도
확인되지 않는다"* 로 닫았다. **닫으면 안 됐다.**

**마이크로소프트 10-Q (2026-03-31 분기, acc `0001193125-26-191507`)**:

> *"We have a long-term strategic partnership with OpenAI. In October 2025, we signed a new
> definitive agreement… OpenAI formed a **public benefit corporation** and completed a
> recapitalization ('OpenAI Recapitalization'). **We have an investment of approximately 27 percent
> of OpenAI on an as-converted basis accounted for under the equity method of accounting.**…
> We calculate our equity method income or loss using the **hypothetical liquidation at book value
> ('HLBV')** method"* · OpenAI 는 **VIE** 로 분류(마이크로소프트가 primary beneficiary 아님)

**Note 3 — 숫자가 명시돼 있다**:

> *"Other income (expense), net included **$19 million of net losses** and **$5.9 billion of net
> gains** for the three and nine months ended March 31, 2026, respectively, and **$768 million** and
> **$2.7 billion of net losses** for the three and nine months ended March 31, 2025, respectively,
> **from investments in OpenAI**, primarily net recognized gains (losses) on our equity method
> investment… The net gains for the nine months ended March 31, 2026 primarily relate to the
> **dilution gain from the OpenAI Recapitalization**."*

| 기간 | 마이크로소프트가 인식한 OpenAI 관련 손익 |
|---|---:|
| FY25 3개월 (2025-03 분기) | **−$768M** |
| FY25 9개월 | **−$2,700M** |
| FY26 3개월 (2026-03 분기) | **−$19M** |
| FY26 9개월 | **+$5,900M** (대부분 **재자본화 희석이익**, 영업 아님) |

⇒ ★★★ **OpenAI 경제성에 대한 «감사받는 분기 시계열»이 존재한다.**
그리고 **FY26 3개월 손실이 −$768M → −$19M 로 급감한 것 자체가 정보다** — HLBV 하에서는
지분법 손실 배분이 소진되면 인식이 멈춘다. **「손실이 줄었다」가 아니라 「인식 한도가 찼을 수 있다」**로
읽어야 하며, 그 구분은 다음 런이 파고들 자리다.

⚠ **HLBV 는 지분율 단순 그로스업을 막는다** — 27% 로 나눠서 OpenAI 전체 손실을 역산하면 안 된다.
**측정 가능한 것은 «마이크로소프트가 인식한 몫»이지 «OpenAI 의 총손실»이 아니다.** 그 선을 지킨다.

---

## C · 프로토콜 업그레이드 제안 (규칙으로)

| # | 규칙 | 어디에 박나 | 근거 |
|---|---|---|---|
| **U1** ★★★ | **「비상장이라 측정 불가」는 3단 확인 후에만 쓴다**: (a) 그 상대방이 상장인가 (b) **상장 회사가 지분법·VIE 로 그것을 인식하는가** (c) 자기 공시에 이름이 있는가. 셋 다 아니어야 `미확보` | `L3 driver_link` · `L1 set_diff` 가드 | A1·B — 이 런은 (a)(b) 둘 다 참인데 `미확보`로 닫았다 |
| **U2** ★★★ | **공시가 파트너·고객을 «이름으로» 대면 그 이름들의 CIK 를 즉시 조회한다.** 상장이면 그 10-Q 가 **양방향 검증**을 준다 | `L1 forensic_pack` · `L1 primary_source` | A2 — CoreWeave 10-Q 가 NVDA 공시에 없는 $2.0bn 을 줬다 |
| **U3** ★★ | **경쟁 제품은 «보도»가 아니라 «상대 회사 뉴스룸/공시» 1차로 확인한다.** 최신 세대만 쫓지 말고 **직전 세대가 이미 떴는지**를 먼저 본다 | `L3 competitors` | A3 — Maia 300 만 쫓다 이미 가동 중인 Maia 200 을 놓쳤다 |
| **U4** ★★ | **Form 4 는 `sharesOwnedFollowingTransaction` + `directOrIndirectOwnership` + `natureOfOwnership` 까지 파싱한다.** 세 줄 추가로 「보유의 몇 %」가 나온다. **라인을 안 가르면 보유가 «늘어» 보인다** | `L2 money_trail` | A4 |
| **U5** ★ | **Form 144 는 같은 창의 Form 4 와 금액이 일치하면 스킵해도 된다** — 실측: 6,536,514 / 3,343,863 / 133,750 셋 다 Form 4 와 **완전 일치**. 새 정보 0 | `L1 forensic_pack` 의 「미확보」 목록에서 제외 | 이 런 실측 |
| **U6** ★★ | **지분 포트폴리오는 총액이 아니라 «건별 시가평가»로 잰다.** 매입가·주식수가 상대방 10-Q 에 있으면 손익이 산출된다 | `L3 accruals_check` | A2 — CRWV 지분 **−7.19%** |
| **U7** ★ | **`module_webctl` 은 `--match` 전에 반드시 `newtab <목적지 URL>`** — 목적지로 탭을 먼저 열지 않으면 `매칭 타깃 없음`으로 죽는다. 이번에도 그대로 밟았다 | `L1 primary_source` 함정 목록 (이미 있으나 **US 경로에도 적용됨**을 명시) | 이 런 실측 |

---

## D · 계기 결함 — 진단과 수정안

### D-1 🚨 `module_paper_book` 의 무증상 stale (이 런이 실제로 물린 것) — **원인 규명 완료**

`module_paper_book/_mark.py:51` `price_move()`:
```python
h = yf.Ticker(yq).history(period="7d")["Close"].dropna()
last = float(h.iloc[-1])
chg_1d = (last / float(h.iloc[-2]) - 1) * 100
```
**최근 봉의 `Close` 가 NaN 이면 `.dropna()` 가 그 행을 조용히 지운다** ⇒ `iloc[-1]` 이 **전 세션**,
`iloc[-2]` 가 **그 전 세션**이 되어 **«전전일 대비 전일 등락»을 «당일 등락»으로 출력**한다.
예외 없음, 경고 없음. 그리고 **`price_move` 는 asof 날짜를 아예 반환하지 않는다** — 이게 진짜 결함이다.
헤더는 `# LIVE PULSE (오늘 뭔일? — 당일 데이터)` 라고 적혀 있다.

**재현성**: 2026-09-03 **10:52 KST 재현**(217.44 = 09-01 종가), **11:3x 에는 재현 안 됨**(224.41 정상).
⇒ **간헐적**. `D402`(yfinance 가 US 종목에 `Close=NaN` 을 낸다) 계열이며 **`D353`(캘린더 롤로 자가치유)와
같은 클래스** — 고쳐진 게 아니라 지나간 것이다.

**수정안 (최소 침습, 3줄)**:
```python
raw = yf.Ticker(yq).history(period="7d")["Close"]
h = raw.dropna()
stale = len(raw) > len(h) and raw.index[-1] != h.index[-1]   # 최근 봉이 NaN 이었나
return {..., "asof": h.index[-1].date().isoformat(), "stale": stale}
```
그리고 `cmd_pulse` 가 **asof 를 헤더에 찍고, `stale` 이면 ⚠ 를 붙인다.**
⇒ 이러면 이 런의 `D48` 오답이 **애초에 발생하지 않는다.**

### D-2 `module_flow --positioning` (`D315`, 7번째 재현)
만기 선택이 **이벤트를 span 하지 않는다**. 이 런에서 09-04(D1)를 집었고, 정산 창은 09-10 이었다.
**수정안**: `--positioning` 에 `--through YYYY-MM-DD` 를 받아 **그 날짜 이후 첫 만기**를 고른다.
없으면 «span 하는 만기 없음»을 출력하고 **±nan% 대신 침묵**한다.
(체인 직독은 이 런에서 성공: 09-11 ±3.97% · 09-18 ±5.39%.)

### D-3 `module_valuation` — US 티커에 6자리 0-패딩(`00NVDA`)해 네이버를 친다
**공란표가 나오고 예외는 안 난다.** **수정안**: 티커가 6자리 숫자가 아니면 **거부하거나**
`module_fundamentals_us` 로 분기. 지금은 「조회했는데 데이터가 없다」로 오독된다.

### D-4 `module_disclosure_us` — 카테고리 맵에 **증권발행 축이 없다**
**$25bn 채권발행(424B5 2건 + FWP)이 「기타 20건」에 묻혔다.** 요약표만 보면 안 보인다.
**수정안**: `424B*` · `FWP` · `S-3` · `S-1` 을 「증자/채무(Item 3.02/2.03)」 카테고리에 매핑.

### D-5 `module_webctl` — 새 목적지 5곳, **지도에 미등록**
`find CUDA` → *"지도에 없다 — 그냥 가되, 끝나고 site_map.json 에 등록해라"*.
등록 대상: `efts.sec.gov`(EDGAR 전문검색 API) · `www.sec.gov/Archives/.../index.json`(파일목록 JSON) ·
`data.sec.gov/submissions/CIK*.json` · `news.microsoft.com/source`(경쟁사 1차 뉴스룸) ·
`developer.nvidia.com`(개발자 수 **없음** — 헛걸음이었다는 것도 등록 가치가 있다).

---

## E · 여전히 닫히지 않은 것 (정직하게)

| 항목 | 왜 아직 안 되나 |
|---|---|
| **OpenAI 의 «총» 손실** | HLBV 라 27% 로 그로스업 불가. 측정 가능한 건 마이크로소프트 인식분뿐 |
| **보증 GMV 실제 금액 / 신용등급 문턱** | 계약서에서 `[***]` 적법 삭제. 상대방(SB Energy·소프트뱅크) 공시는 미확인 — **다음 탐색 후보** |
| **CUDA 개발자 수** | `developer.nvidia.com/cuda-zone` 본문에 **없음**(브라우저로 확인). GTC 키노트 자료가 다음 후보 |
| **1년 전 컨센** | 자체 스냅샷 43일이 최선. 소급 복구 불가 — **다만 U1 처럼 «상대 경로»가 있는지 아직 안 뒤졌다** |
| **Maia 200 의 실제 배치 규모** | 마이크로소프트가 유닛 수를 안 밝힘. capex 분해로 역산하는 것이 다음 실험 |

---

## F · 이 탐색이 «보고서»를 바꾸는가

**목표주가 $248 · HOLD 는 바뀌지 않는다.** 새 증거는 양쪽으로 갈린다:
- **약세 쪽**: CRWV 차입금/EBITDA **13.6배**, NVDA 의 CRWV 지분 **−7.19%**, Maia 200 이 **이미 가동**
- **강세 쪽**: OpenAI 관련 마이크로소프트 인식손실이 **−$768M → −$19M** 로 급감,
  CRWV 매출이 **$0.98bn → $2.58bn (5분기)** 로 성장

⇒ **평결은 유지하되, `SET_DIFF` 의 `risk_unseen` R1·R2 가 «측정 불가»에서 «측정 가능, 아직 안 쟀음»으로
등급이 바뀐다.** 그게 더 나쁜 상태다 — **핑계가 사라졌다.**
**다음 런의 첫 과제는 CRWV·NBIS 10-Q 를 NVDA 매출의 대응 계열로 정식 편입하는 것이다.**
