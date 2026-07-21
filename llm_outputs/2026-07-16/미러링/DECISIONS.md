# DECISIONS — 미러링 Stage 5 DECIDE (2026-07-16 목)

> PM 판단(모듈 데이터 위 추론). 입력 = INTAKE_LEDGER + BOOK_STATE. epistemics prior = **없음(첫 패스)**.
> 게이트 순서: ①하드게이트(스탑히트→EXIT·RESOLVED→out) ②신선도→컨빅션 ③가격vs스탑 ④상관가드(one-risk-unit) ⑤★core.
> **분석/예시 — 매수매도 권유 아님. 집행은 사람(STAGE_ORDERS는 intent만).**

## 보유 포지션 판정
| 종목 | 판정 | 컨빅션 | 근거 | flip 조건 |
|---|---|---|---|---|
| **삼성전기 009150** | **HOLD-to-stop (EXIT-bias)** | 低 | 🔴RESOLVED(dead-cat) but 스탑히트 아님(+3.6%)·외국인 bid(IBK·+45.6만)·2Q 임박. RESOLVED 게이트는 **스탑규율로 이행**(hope-hold 아님) | close<1,260,000→**EXIT(자동)** / close>1,370,200+2Q beat→업그레이드 |
| AVGO | HOLD | 高 | 🟢LIVE ★진앙(AI-compute)·오늘 +1.3 | US SEMI 테제 붕괴 |
| NVDA | HOLD | 高 | 🟢LIVE ★진앙 | 동상 |
| TSM | HOLD | 中 | 🟢LIVE 파운드리·−1.8 미실현 | 파운드리 수급 |
| VST | HOLD | 中 | 🟢LIVE AI-power | **DC 모라토리엄 확산**(US 킬스위치) |
| KMI | HOLD | 中 | 🟢LIVE energy·미드스트림 | energy 유닛(아래) |
| LNG | HOLD | 中 | −3.5 오늘(걸프/나스가스 눌림, 펀더 훼손 아님)·미실현 +5.7 | 나스가스 급락 |
| RTX | HOLD | 中 | defense·호르무즈 봉쇄 Day137 프리미엄 live | **TACO(해협 재개)→give-back** |
| MA | HOLD | 中 | 결제·조용 | — |

## 신규 후보 판정 (ENTER / PASS)
| 종목 | 판정 | 방식 | 컨빅션 | 근거 + 상관가드 |
|---|---|---|---|---|
| **SK이노 096770** | **ENTER** | **시장가 now** | 中高 | 🟢LIVE·clean entry(베이스 재가속)·오일+전환 브릿지. 책에 **KR 에너지전환 0 → diversify**. 오일 59%가 energy-fuel와 부분 상관이나 전환레그(SK온·SMR·ESS) 차별화 = 순수 stack 아님. 하드스탑 89,500 |
| **하나금융 086790** | **ENTER** | **LIMIT 122,000(MA20 되돌림)** | 中 | 🟢LIVE·RR 최선(PBR0.80·소각·외국인5일전환). 파라볼릭 꼭지라 **되돌림 지정가**(추격 금지). **★S4 긴축 de-rate 헤지**(AI-멀티플 상쇄). 하드스탑 109,700 |
| KB금융 105560 | **PASS(watch)** | — | — | 🟢LIVE지만 **하나와 同 리스크유닛(KR은행 NIM) → 상관가드上 stack 금지.** 하나(RR 우위) 단일 표현 선택. KB는 7/23 2Q NIM 확인 후 재고(PBR1.07·외인소진79% 열위) |
| S-Oil 010950 | **PASS** | — | — | 🟡·RSI 85.9 극단 + **책 energy-fuel 이미 21%(최대유닛) → 상관 stack 금지.** 눌림(MA20 117k) 대기 |
| SK이터닉스 475150 | PASS(watch) | — | — | 🟡·신재생 FADING·PER62·코일. 돌파+ESS 정책 후 |
| 한미반도체 042700 | PASS(watch) | — | — | 🟡 GATE(close>275,338)·책 AI-compute 유닛과 중복 |
| 아모레090430·한국콜마161890 | PASS | — | — | 🟡 froth·환율/관세 역풍 |

## 상관가드 요약 (핵심 규율)
- **KR은행 = 1 리스크유닛 → 하나 1종만 ENTER(KB는 watch).** ← 앞서 즉흥으론 둘 다 스테이징(stack 위반)했던 것 교정.
- **energy = 1 유닛(KMI+LNG 21%) → S-Oil 추가 PASS.** SK이노는 전환레그로 차별화돼 diversify로 허용.
- **AI-compute = 진앙 유닛(AVGO/NVDA/TSM 보유) → 한미반도체 중복 PASS.**
- 신규 ENTER 2종(SK이노·하나) = **서로 무상관 + 책 편중(AI-멀티플) 완화** 방향.

## ✅ EXIT CHECK
- [x] 보유 9종 HOLD/EXIT-bias 판정·신규 🟢LIVE ENTER/PASS.
- [x] 하드게이트(삼성전기 RESOLVED→스탑규율·스탑히트 없음)·momentum/hard-stop 스탬프.
- [x] 상관가드 적용(은행 1종·S-Oil PASS·각 판정 flip 조건).
