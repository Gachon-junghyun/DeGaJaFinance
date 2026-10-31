# L3 · estimate_revision — 컨센서스가 «깎이는 중»인가 «올라가는 중»인가, 그리고 원래 잘 맞았나

> **Single-role unit.** Independent — no ordering; an L2/L1 calls it when needed. Does ONE thing:
> read the consensus **as a time series of itself** — how the current-year and next-year estimates moved
> over 1주/1개월/3개월/**1년**, and how far past estimates missed the eventual print. It reports the
> direction of revision and the historical hit rate. It does not value anything.
> Different from a consensus **level** (target price, forward PER), which every pack already carries.

## Why this exists (measured 2026-08-28, 034020 두산에너빌리티)
The current level said the name was expensive. **The revision series said something the level could
not**: the estimates had been cut hard *while the stock rose*.

| 2026년 컨센서스 | 1년 전 | 3개월 전 | 1주 전 | 현재 | 변화 |
|---|---:|---:|---:|---:|---:|
| 영업이익 | 14,348억 | 11,242억 | 11,302억 | **11,308억** | 🔴 **-21%** |
| EPS | 808원 | 458원 | 493원 | **499원** | 🔴 **-38%** |
| 주가(1년 수익률) | | | | | 🟢 **+36.1%** |

⇒ **이 상승은 이익이 만든 것이 아니라 배수가 만든 것이다.** 현재값만 보면 «PER 172배»까지는 보이지만
«왜 172배가 됐나»가 안 보인다. 분자가 오르고 분모가 깎였다는 사실은 **이 표에서만 나온다.**

과거 적중률을 같이 재면 다음 해 추정을 그대로 쓸지도 갈린다:

| 연도 | 3개월 전 추정 대비 실제 영업이익 | 6~9개월 전 추정 대비 |
|---|---:|---:|
| 2024 | **-19.7%** | -23.7% |
| 2025 | **-20.4%** | -31.1% |

⇒ 이 데스크의 2027E·2028E 는 **같은 비율로 깎일 가능성을 기본값**으로 두는 편이 안전하다.
⚠ 반대 신호도 같이 적어라 — 034020 은 2026년 1·2분기가 **연속 어닝 서프라이즈**(+20.3%·+19.5%)였다.
«추세는 깎임, 최근 2분기는 상회»는 모순이 아니라 **변곡 후보**다. 둘 다 적어야 다음 사람이 판단한다.

## Where the numbers come from
| market | source | 경로 |
|---|---|---|
| **KR** | FnGuide 기업정보 «컨센서스 추이» | `navercomp.wisereport.co.kr/v2/company/c1050001.aspx?cmp_cd={6자리}` — 로그인 없음. 본문을 `innerText` 로 통째 뜨면 표가 텍스트로 나온다(셀렉터 불필요) |
| | 어닝 서프라이즈(분기 컨센 vs 잠정) | 같은 페이지 하단 |
| **US** | 컨센 추이는 유료 단말 축이라 **미확보로 둔다** | 대체: 발표 전후 추정 이동은 `snapshot_estimates.py` 의 자기 스냅샷 누적 |

⚠ **네이버 증권 종목 페이지의 «종목분석» 탭은 이 사이트를 iframe 으로 물고 있을 뿐이다.** 직접 가라.
⚠ 페이지 번호와 이름이 안 맞는다 — `c1040001` 은 재무분석, **`c1050001` 이 컨센서스**다.

## ⚠ Guards
- **깎였다 ≠ 팔아라.** 하향 사이클의 끝에서 주가가 먼저 도는 일은 흔하다. 이 단위는 **방향과 속도**만 낸다.
- **1년 전 값과 오늘 값의 회계 범위가 같은지 확인하라.** 분할·합병·연결범위 변경이 있으면 비교가 깨진다.
- **주가 수익률을 같은 창으로 맞춰라.** 추정은 1년 전, 주가는 6개월 수익률이면 문장이 거짓이 된다.

## Output (표 하나 + 두 줄, 판단 없음 — P4)
`지표 · 1년 전 · 3개월 전 · 1개월 전 · 1주 전 · 현재 · 변화율` + 같은 창의 주가 수익률 한 줄
+ 과거 2~3개 연도의 «추정 대비 실제» 미달률 한 줄. 상향·하향 어느 쪽이든 **반대 신호가 있으면 같이 적는다.**
