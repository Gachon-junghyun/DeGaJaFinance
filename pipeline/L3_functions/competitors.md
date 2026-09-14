# L3 · competitors — competitors & value-chain neighbors

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing.

- **Role**: extract a company's competitors/value-chain neighbors and fix its relative position
  (bottleneck node? beneficiary node?).
- **Input**: ticker · sector thesis terms · (optional) peer codes.
- **CLI**:
  ```bash
  python -X utf8 -m module_industry_map "<sector thesis terms>"                # chain nodes 5–8
  python -X utf8 -m module_valuation <ticker> --peers <peer1>,<peer2>          # relative multiples
  python -X utf8 -m module_business <ticker>                                   # business reality check (US = module_business_us --json)
  ```
- **Output**: competitor list + bottleneck-node position + peer-relative multiples
  (a de-rated lane vs peers = open alpha, if the business check supports it).

---

## 🚨 U3 · 경쟁 제품은 **상대 회사 1차 출처**로 확인한다 — 그리고 **직전 세대를 먼저 본다**

**실패 실측 (2026-09-03 NVDA)**: 이 런은 `Maia 300`(9월 공개·30만 유닛, 전부 `[news]`)만 추적했다.
마이크로소프트 자기 뉴스룸을 열어보니 **한 세대 전이 이미 떠 있었다**:

> *"Our newest AI accelerator **Maia 200 is now online in Azure**. Designed for industry-leading
> inference efficiency, it delivers **30% better performance per dollar than current systems**."*
> — `news.microsoft.com/source`, **2026년 1월 26일**

그리고 **`Maia 300` 은 그 뉴스룸에 0건** — 보도만 존재한다는 뜻이라 `[news]` 등급은 옳았다.
⇒ **틀린 것은 등급이 아니라 «어느 세대를 보고 있었나» 다.**
대체 위협을 «다가올 미래»로 잡으면, **이미 배치된 현재**를 놓친다. 그리고 그게
`DRIVER_TEST` 의 「고객 capex 증분 점유율이 QoQ −16.5pp 벌어졌다」에 **날짜가 맞는 후보**였다.

**절차 (순서를 지킨다)**
1. **상대 회사 뉴스룸/공시부터** — `news.microsoft.com/source/?s={query}` · 상대사 8-K/10-K.
   ⚠ 상세 URL 을 추측하면 404 다. **검색 결과 페이지에서 링크를 뽑아라.**
2. **직전 세대가 이미 출하됐는지 먼저 확인** — 최신 세대 루머보다 배치된 이전 세대가 더 중요하다.
3. 회사가 주장하는 **성능/가격 우위 수치**를 그대로 인용(형용사 말고 숫자).
4. **분모를 요구하라** — 「30만 유닛」이 대상 회사 물량의 몇 %인지 없으면 대체율은 `미확보` 다.
