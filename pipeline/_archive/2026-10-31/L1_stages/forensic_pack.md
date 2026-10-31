# L1 · FORENSIC_PACK — STEP 0 deterministic datapack (stage)

> Phase 0. Freeze every number **before** reasoning, so the write-up cites data, not memory. This is the
> forensic desk's "박제" step: assemble the pack, read it whole, then start the blocks. Calls L2. Output: `DATAPACK.md`.

## Belief
Nothing enters the report that isn't in ① this pack or ② a DART original with its rcept_no. A WebSearch
number gets a `[WebSearch]` tag and is never the spine of a decision. **미확보 is a finding, not a failure.**

## L2 called
- [deepdive](../L2_modules/deepdive.md) — `module_valuation`(현재가·**컨센 목표주가/투자의견**·PER TTM/Fwd·PBR·외인%) ·
  `module_business`(DART 사업보고서 본문: 사업의내용·매출분해·ASP·고객집중) · `module_disclosure --days 120`(공시 digest + red-flags) ·
  `module_chart <code>.KS/.KQ --read` (**풀 그리드 정독** — 요약 tail 말고 `chart_{code}.txt` 본문).
- [money_trail](../L2_modules/money_trail.md) — investor_flow(외/기/개 일별) · insider/treasury/capital(DART) · short%(KRX) · accruals.
- [news](../L2_modules/news.md) — `fts search "<한글명>" --days 30`(velocity 7d/30d + 최근 제목). **검색키=한글 종목명**(티커 0건).
- L3 [filing_diff](../L3_functions/filing_diff.md) — 공시 언어 diff(Lazy Prices), best-effort.

## Ticker-format trap (violate → 0 data)
| source | KR format | US format |
|---|---|---|
| KIS·valuation·disclosure·business | 6-digit `009150` | — (US uses yfinance/EDGAR) |
| yfinance / chart / flow | `.KS`(코스피)/`.KQ`(코스닥) `009150.KS` | plain `PSX` |
| news_fts | **한글 종목명** `삼성전기` (ticker → 0 hits) | company name **and** ticker; `--scope foreign` |
| EDGAR (`module_disclosure_us`·`module_fundamentals_us`) | — | plain ticker → CIK via cache |

## Data gaps by market (state explicitly, do not lean on)
**KR**: no single-stock option flow · insider **trade price 미상**(direction/qty only) · procurement needs
`DATA_GO_KR_KEY` · per-investor short 미제공.
Counter-edge: **per-day foreign/inst net-buy + short balance are KR-only axes — use them.**
**US**: **no per-investor flow at all** — the closest substitutes are `us_flow.py <T>` (FINRA daily
short-vol z) and `module_flow --positioning` (short %float, P/C OI, IV skew, **implied move**). Insider
data is *better* than KR (Form 4 carries price; Form 144 announces intent) but
⚠ **`module_disclosure_us` lists Form 4/144 without parsing them** — direction and size need the XML.
Measured 2026-08-21 (PSX): 6 Form 4s in 60d, **5 carrying transaction code `S`**, and 9 Form 144s of
which only 1 parsed ($315k). ⇒ report direction as observed and **size as 미측정** — do not imply a scale
the parse did not give you.

## 🔴 KR 반기·분기 — 팩이 조용히 틀리는 자리 (measured 2026-08-28, 034020)
DART 반기·분기 손익계산서에는 **3개월 단독 칸(`thstrm_amount`)과 누계 칸(`thstrm_add_amount`)이 함께**
들어 있는데, 현금흐름표에는 **누계뿐**이다. `module_fundamentals_kr` 은 손익에서 3개월 칸을 읽으므로
(`_dart_fin.py:173,192`) 「OCF/영업이익」·「매출채권/매출」·「미청구/매출」이 **기간이 어긋난 채** 나온다.

| 034020 2026 반기 | 모듈 보고값 | DART 원문 누계 |
|---|---:|---:|
| 매출액 | 4.72조 (2분기 단독) | **8.99조** |
| 영업이익 | 3,143억 (2분기 단독) | **5,478억** |
| OCF / 영업이익 | **-2.82** ← 반기 OCF ÷ 2분기 영업이익 | **-1.62** |

⇒ **예외가 안 난다. 그럴듯한 숫자가 나온다.** 반기·분기 팩은 `thstrm_add_amount` 를 직접 읽고,
쓰는 쪽에 「누계 기준」이라고 적어라. 연간(사업보고서)은 이 문제가 없다.

## US segment P&L — the pack's most-missed axis
`module_business_us` returns 10-K **prose** (Item 1/1A/7): it names the segments and carries no segment
earnings. The table lives in the **earnings 8-K exhibit 99.1**, which `module_disclosure_us` categorizes
but does not fetch. Pull it via L3 [segment_pnl](../L3_functions/segment_pnl.md) — the pack is not frozen
until the segment split and the Basis-of-Presentation scope line are in it.

## ✅ EXIT CHECK
- [ ] `DATAPACK.md` written; every axis has a status (ok/미확보). Chart full grid read, not just CHART_READ.
- [ ] Consensus target/rating captured (Block C ① seed). Foreign/inst/retail 20d flow captured.
- [ ] prev_research loaded if the ledger has this code (feeds SELF_SCORE). Pack read whole before any block starts.
- [ ] **Segment P&L present** (share of level AND of the swing) + the Basis-of-Presentation scope line (`none` is an answer). A pack without it hands DRIVER_TEST a company it cannot decompose.

---

## 🚨 U2 · 공시가 파트너·고객을 **이름으로 대면, 그 이름들의 CIK 를 즉시 조회한다**

대상 회사의 공시는 **자기에게 유리한 것만** 담는다. 상대방이 상장사면 **그 10-Q 가 나머지 절반**을 준다.

**실패 실측 (2026-09-03 NVDA)**: NVDA 8-K(EX-99.1)가 Vera Rubin 파트너로
**CoreWeave · Google Cloud · Microsoft Azure · Oracle Cloud · Nebius** 를 이름으로 댔다.
이 런은 그 이름들을 **서사로만 읽고 검증 대상으로 쓰지 않았다.** 열어봤더니:

> CoreWeave 10-Q (acc `0001769628-26-000366`) — *"In January 2026, we entered into a securities
> purchase agreement with **NVIDIA Corporation** for a private placement of approximately
> **23 million shares** … at **$87.20 per share** … **$2.0 billion**."*
> *"**all of the GPUs used in our infrastructure today are NVIDIA GPUs**"* ·
> *"our current customers have **contractually specified** our use of NVIDIA GPUs"*

⇒ **NVDA 공시 어디에도 없는 $2.0bn 이 상대방 공시에 있었고, 순환이 양쪽에서 닫혔다.**

**절차 (팩 단계에서 3분)**
```bash
# 1) 이름 → CIK
curl -sL -A "<UA>" 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=<이름>&type=10-Q'
# 2) 그 회사 파일링에서 대상 회사 이름이 나오는가 (로그인·키 없음, 초 단위)
curl -sL -A "<UA>" 'https://efts.sec.gov/LATEST/search-index?q=%22<대상회사>%22&forms=10-Q&entityName=<이름>'
# 3) 제출 이력 / 파일 목록
curl -sL -A "<UA>" 'https://data.sec.gov/submissions/CIK<10자리>.json'
curl -sL -A "<UA>" 'https://www.sec.gov/Archives/edgar/data/<cik>/<accession_nodash>/index.json'
```
⚠ **디렉토리 HTML 을 긁지 마라** — SEC 네비게이션 링크만 나온다. **반드시 `index.json`.**
⚠ **8-K 가 "10-Q 에 exhibit 로 낸다"고 적으면 그 10-Q 의 `index.json` 에 계약 원문이 있다.**
   실측: NVDA `nvda2027q2ex101.htm` = 잔존가치보증 계약 원문 **43,964자**, 공시 목록 요약엔 한 줄도 없다.
