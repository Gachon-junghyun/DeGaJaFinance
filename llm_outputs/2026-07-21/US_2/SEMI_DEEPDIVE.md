# 반도체 종합 심층분석 — 2026-07-21 (KST 2026-07-22)

> 5개 리서치 에이전트 병렬 조사 종합(메모리 · GPU/ASIC · 파운드리/장비 · 개발자·SNS 현장 · 비AI/오토/중국).
> 뉴스 DB(사내 API) 401 다운 → **전부 라이브 WebSearch 기반, 출처 링크 인라인.** 참고용 분석이며 매매 권유 아님.
> 데이터 asof: 미 동부 2026-07-21 장 세션. 일부 실적은 7/15~16 발표분(TSMC·ASML 확정), TXN·구글은 발표 예정.

---

## ★ 한 줄 결론
**수요는 "진짜"다** — 기업 실적 · 파운드리 가동률 · 개발자 현장이 삼중 확인. 논쟁은 "수요가 있냐"가 아니라
**"그 수요에 지금 밸류에이션이 값하냐(ROI)"** 하나로 좁혀졌다. 오늘(7/21) 반등은 이 진짜 수요 위에 얹힌 반등이며,
**"턴 확정"은 이번 주 캡엑스 발표(구글·AMD 이벤트)가 판정**한다.

---

## 1. 큰 그림 — 시장이 두 쪽, 그리고 AI가 나머지를 잠식

- **AI 데이터센터 = 폭발.** 하이퍼스케일러 캡엑스 **$725B (+77% YoY)**, 아무도 안 줄이고 전부 상향 중.
  (아마존 ~$200B, 구글 $175-185B, 메타 $125-145B, MS $110-120B) — [valueaddvc](https://valueaddvc.com/blog/ai-hyperscaler-capex-compared-why-microsoft-google-meta-and-amazon-are-all-spending-at-once), [CreditSights](https://know.creditsights.com/insights/tech-raising-hyperscaler-capex-2026-estimates/)
- **WSTS 2026 시장 $1.51조 (+90% YoY)** — [WSTS](https://www.wsts.org/76/103/Global-Semiconductor-Market-Surges-Beyond-15T-2026)
  - ⚠ **착시 주의:** +90%의 대부분은 **메모리 "가격" 폭등**(DRAM 매출 +171% YoY)이지 물량 증가가 아님.
- **핵심 트위스트 — AI가 나머지 공급을 빨아들임.** 2026년 생산 메모리의 **~70%를 AI 데이터센터가 소비**,
  HBM이 일반 DRAM 웨이퍼를 밀어냄 → 오토·산업·PC·폰은 수요는 회복하는데 **AI발 공급/원가 압박**에 얻어맞음.
  — [Tom's Hardware](https://www.tomshardware.com/pc-components/ram/data-centers-will-consume-70-percent-of-memory-chips-made-in-2026-supply-shortfall-will-cause-the-chip-shortage-to-spread-to-other-segments), [enkiAI](https://enkiai.com/ai-market-intelligence/semiconductor-scarcity-2026-the-ai-vs-auto-chip-war/)

---

## 2. 세그먼트별 수요 현황 (한눈에)

| 세그먼트 | 판정 | 근거 |
|---|---|---|
| **메모리 / HBM** | 🔥 초타이트 | HBM 3사 2026 완판, DRAM/NAND 계약가 +13~18%(4분기째), 젠슨황 "메모리가 AI 최대 병목" |
| **GPU (엔비디아)** | 🔥 완판 | 블랙웰 mid-2026 매진(백로그 360만대), 루빈 7월 양산, 중국=가이던스 제로(순수 업사이드) |
| **커스텀 ASIC (브로드컴·마블)** | 🔥 급증 | AVGO AI FY26 ~$56B(3배)·백로그 $73B, 커스텀 고객 6곳(OpenAI 신규), 구글TPU 2031년까지 |
| **파운드리·패키징 (TSMC)** | 🔥 완판 2027 | 3nm 가동률 100%↑, CoWoS 2026 완판·리드타임 52~78주, 엔비디아 증설분 ~50-60% 선점 |
| **장비 (ASML·AMAT·LAM)** | 🟢 선단 강세 | WFE 2026 ~$140B 상향, 성장의 80%가 선단/DRAM/패키징. **단 중국 WFE 0%(정체)** |
| **아날로그·오토·산업** | 🟢 회복 확인 | ADI +37%(기록), TXN 산업재 +30%, onsemi 7분기 만에 첫 오토 플러스 = 재고조정 끝 |
| **PC / 스마트폰** | 🟡 눌림 | 수요는 있으나 **메모리값 폭등에 출하 감소**(가트너), AI-PC "활주로 위 대기" |
| **중국 국산화** | 🟡 가속 but 병목 | 화웨이 Ascend 950PR·SMIC 7nm, 그러나 **HBM 병목**(CXMT 아직 상용급 미달) |

---

## 3. 기업별 현황

### AI 컴퓨트
- **엔비디아(NVDA)** — 최강·공급제약. 블랙웰 mid-2026 매진, 루빈 7월 양산(썸열 이슈 해소), 다음분기 ~$91B,
  중국 H20 재개 승인됐으나 아직 미출하 → **가이던스는 중국 제로**라 순수 업사이드.
  [Nvidia](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2026), [CNBC](https://www.cnbc.com/2026/02/26/nvidia-china-chip-sales-export-controls-ai-competition.html)
- **AMD** — 이번 주 최대 촉매. **7/20 MS Azure에 Helios 랙(MI455X GPU + Venice CPU + Pensando + ROCm)
  프론티어 인퍼런스용 대량 채택, H2 2026 출하.** 메타 6GW + OpenAI 6GW = ~12GW 약정. 점유율 ~4.5% vs 엔비디아 95%.
  **7/22-23 Advancing AI 이벤트**(MI450 상세 가능). [Yahoo/TheStreet](https://finance.yahoo.com/technology/ai/articles/amd-just-landed-biggest-ai-180300334.html), [hothardware](https://hothardware.com/news/amd-azure-ai-new-microsoft-infrastructure-deal)
- **브로드컴(AVGO)** — 수요 강한데 심리는 미회복(6월 가이던스 $16B vs $17.2B 쇼크로 −12.6%, 아직 고점 −24%).
  AI FY26 ~$56B·백로그 $73B, 커스텀 고객 6곳(구글·OpenAI '할라피뇨'·Anthropic·메타+2), 구글TPU 2031년까지.
  [techtimes](https://www.techtimes.com/articles/317846/20260605/nvidia-not-only-ai-chip-winner-broadcom-forecasts-56-billion-custom-silicon-demand-surges.htm), [Digitimes](https://www.digitimes.com/news/a20260604VL202/broadcom-anthropic-openai-revenue-2026.html)
- **마블(MRVL)** — DC 매출 기록 $6.1B, 커스텀 실리콘 18개 설계승리(아마존 트레이니엄·MS 마이아·메타), 엔비디아 $2B 투자.
  [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia)

### 메모리
- **마이크론(MU)** — 2026 HBM 완판(HBM4 포함 가격·물량 락인), 1-gamma DRAM 최대볼륨 노드, 캡엑스 >$25B.
  BofA 목표가 $1,550(7/21 업그레이드가 당일 랠리 촉매). ⚠ 절대 매출 숫자가 역사적 규모 대비 과해 보임 — 원본 공시 크로스체크 권장.
  [Micron FQ3](https://investors.micron.com/static-files/631b1a32-5537-46ae-8f40-82e42fc79dfe), [247WallSt 7/21](https://247wallst.com/investing/2026/07/21/sandisk-rises-8-western-digital-jumps-9-micron-adds-7-as-memory-rebound-accelerates/)
- **SK하이닉스** — HBM 1등(루빈 HBM4 ~60-70% 추정), 2026 완판, 오히려 HBM4 램프를 늦춰 일반 DRAM 타이트닝에 투입.
  [TrendForce](https://www.trendforce.com/news/2026/06/23/news-memory-giants-split-on-hbm4-strategy-samsung-hbm4-sales-reportedly-tops-1b-sk-hynix-slows-ramp/)
- **삼성** — 엔비디아+AMD HBM4 퀄 통과(6/5 젠슨황 확인), 2월 양산, **HBM4 매출 $1B 최속 돌파** = 2026 역전 스토리.
  [Yahoo/Reuters](https://finance.yahoo.com/sectors/technology/articles/nvidia-certifies-samsung-sk-hynix-133001560.html)
- **샌디스크(SNDK)/WDC** — NAND 순수 수혜, NAND 가격/매출 기록. 샌디스크 YTD +502%(센티멘트 과열 게이지), 7/21 +8~9%.

### 파운드리·장비
- **TSMC** — Q2 매출 +36%·마진 67.7%(기록), **연간 가이던스 40%+ 상향**, 캡엑스 $60-64B, 3nm 100%↑,
  CoWoS "2026 완판", "AI 수요 2029-30까지." [techtimes](https://www.techtimes.com/articles/320696/20260716/tsmc-posts-record-quarter-ai-chip-demand-pushes-full-year-growth-outlook-past-40.htm), [Yahoo/Bloomberg](https://finance.yahoo.com/technology/articles/tsmc-targets-40-sales-growth-194152888.html)
- **ASML** — Q2 확정, 가이던스 €43-45B 상향, EUV 60대, **인텔에 첫 High-NA 납품**. 중국 매출 36%→19% 급감.
  [techtimes](https://www.techtimes.com/articles/320577/20260715/asml-raises-full-year-guidance-intel-ships-first-high-na-euv-logic-chip.htm)
- **AMAT/LAM/KLA** — ex-중국 +20% 성장, 중국 노출분 약세. WFE 2026 ~$140B(성장의 80%가 선단/DRAM/패키징).
- **인텔 파운드리** — 18A 외부 대형고객 아직 없음(자사 Panther Lake), 14A는 **테슬라 간판 수주** + SpaceX/xAI 협의.
  [wccftech](https://wccftech.com/intel-14a-wins-tesla-major-customers-foundry-business-gamble-pays-off/)

### 비(非)AI · 오토·아날로그
- **ADI** — Q2 기록 $3.62B(+37%), 산업 +56% "회복 이제 시작." **TXN** 산업 +30%(Q2는 7/22 발표). **NXP** +12%(오토·산업).
  **onsemi** 7분기 만에 첫 오토 YoY 플러스(변곡). **STM**만 지각(2H26). 다 **가격 인상 중** = 상승사이클 시그널.
- **퀄컴** — Q2 비트, 애플 모뎀 이탈 대비 다변화(오토 +38%, IoT +9%).

### 중국
- **SMIC**(7nm/5nm DUV 한계) · **CXMT**(HBM3 2026 양산 계획이나 상용 AI훈련급 미달, ~2M 스택=Ascend 25-30만개분) ·
  **화웨이 Ascend 950PR**(완전 국산 스택이나 7nm 한계·외국 HBM 재고 의존). 미국은 **화웨이 칩 전세계 사용 금지**로 통제 강화.
  [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/u-s-issues-worldwide-crackdown-on-using-huawei-ascend-chips-says-it-violates-export-controls)

---

## 4. 🗣️ 개발자·SNS 현장 목소리

> ⚠ Reddit API가 이 환경에서 차단 → r/LocalLLaMA 등은 이를 인용한 블로그 경유(2차). HackerNews는 1차 링크. 클라우드 가격은 주간 변동.

**① 공급 여전히 빡빡, 렌탈비 오히려 상승 (글럿 아님)**
- H100 온디맨드 렌트 가을 이후 **+40%**($1.70→$2.35/hr), H200 ~$4/hr, B200 ~$6.25/hr. 글럿이면 나올 수 없는 그림.
- DC GPU 리드타임 **36~52주**, 블랙웰 3~7개월. 근본원인 = GPU 다이 아니라 **CoWoS+HBM**(2027 중반까지 할당 완료).
  [Spheron GPU Shortage 2026](https://www.spheron.network/blog/gpu-shortage-2026/), [Broadband Breakfast](https://broadbandbreakfast.com/ai-compute-shortage-challenges-bubble-narrative/)

**② 개발자 최대 불만 = 메모리값 폭등 (가장 많이 반복된 현장 그리번스)**
- DDR5 32GB 킷 ~$375(1년 반 전의 4배), RTX 5090 길거리값 $4,300~5,000+. HBM이 DRAM 웨이퍼 23% 잠식 →
  홈랩 빌더 밀려남. 완화 2027 말 이후. [runaihome](https://www.runaihome.com/blog/ddr5-ssd-price-surge-ai-hbm-impact-local-builds-2026/), [Wccftech](https://wccftech.com/roundup/memory-crisis/)

**③ 인퍼런스 폭발 — "효율 좋아지면 수요 죽는다"는 틀렸다 (Jevons)**
- 토큰 수요 6M/분(2025.10) → **15B/분(2026.3)**, 인퍼런스가 컴퓨트의 2/3.
- DeepSeek식 효율(DSpark 속도 +85%·양자화)로 토큰값 하락 → **싸지니 더 씀(에이전트·롱컨텍스트)** = 총수요 증가.
  "DeepSeek이 엔비디아 죽인다" 공포는 현장에선 **틀린 걸로 정리.** [J.P. Morgan tech trends](https://www.jpmorganchase.com/content/dam/jpmorganchase/documents/technology/2026-tech-trends-inference-demand.pdf), [SCMP DSpark](https://www.scmp.com/tech/big-tech/article/3358647/faster-ai-lower-costs-dspark-eases-inference-bottlenecks-and-chip-strain-says-deepseek)

**④ AMD는 종이 위에선 따라왔지만 실전은 여전히 CUDA**
- MLPerf 6.0: MI355X가 B200의 한 자릿수% 이내, ROCm이 H100의 90-95%. 개발자 합의: *"PyTorch+vLLM이면 ROCm 쓸 만,
  TensorRT-LLM/FlashAttention3 필요하면 CUDA 남아라."* [HN 187코멘트 스레드](https://news.ycombinator.com/item?id=43535943). 소프트 해자 얇아졌지만 여전.

**⑤ 애플 실리콘 로컬 강세**
- 통합메모리가 킬러: 64GB 맥이 24GB 4090이 못 돌리는 모델 돌림. M5에서 MLX가 llama.cpp보다 30-40% 빠름.
  개인 로컬 추론은 GDDR/HBM 대란 우회(단 DC 수요 상쇄는 아님). [9to5Mac](https://9to5mac.com/2025/11/20/apple-shows-how-much-faster-the-m5-runs-local-llms-compared-to-the-m4/)

**⑥ 버블 논쟁 — 현장 vs 월가**
- 개발자는 **"컴퓨트는 진짜"**에 동의(본인이 못 구하니까). 회의는 **"수요 없다"가 아니라 "돈값 하냐/순환출자냐."**
  HN 1면 *"AI 비용이 매출보다 먼저 뜬다"*(원가 46/28/19% 급증 vs 매출 9-15%). 정서가 "쓸모없나"→"일자리 뺏나"로 이동 =
  오히려 실사용 증거. 지배 프레임: **"인플렉션 버블 — 기술은 진짜, 자본은 태우며 간다."**
  [HN: costs before revenue](https://news.ycombinator.com/item?id=43391073)

---

## 5. 종합 판정 & 오늘 반등 재해석

세 층위가 같은 말을 한다:
- **기업 실적층** → HBM/GPU/CoWoS 완판, 캡엑스 다 상향.
- **파운드리 물리층** → 3nm·패키징 가동률 100%+, 2027까지 매진.
- **개발자 현장층** → 렌탈비 오르고 못 구함, 메모리값이 아파서 우회 중.

→ **"수요 붕괴"의 증거는 어느 층에도 없다.** 6월 폭락은 수요가 아니라 **밸류에이션(눈높이)**이 깨진 것 —
이제 "그냥 좋음"엔 안 오르고 "블로우아웃"이어야 오른다.

**오늘 반등은?** "바닥 탄탄한 반등"이 맞다. 오늘 촉매(마이크론 BofA 업그레이드·AMD-MS 딜)가 전부 위 진짜 수요의 조각이라
순수 데드캣은 아니고, **"턴 확정"은 이번 주 캡엑스 발표가 판정**한다.

### 🔴 진짜 리스크는 수요가 아니라 이것들
1. **ROI/캡엑스 지속성** — "비용이 매출보다 먼저 뜬다"가 심해져 하이퍼스케일러가 **캡엑스를 줄이면** = 진짜 꼭지.
2. **실질금리 >2.55%** — 밸류에이션 천장(현재 2.31% 상승 중).
3. (곁가지) 메모리 절대 숫자가 과열 사이클처럼 커서(마이크론류) 원본 공시 크로스체크 권장. 샌디스크 +502% YTD = 센티멘트 과열.

### ✅ "진짜 턴 vs 그냥 반등" 판정 체크리스트 (이번 주)
- 구글(KST 7/23 새벽)·AMD 이벤트(7/22-23)에서 **캡엑스 또 상향** → 수요 검증, 반등 아님.
- NVDA 종가 >206.27·AVGO >403.56를 **OBV 누적과 함께** 돌파 → 확정 턴.
- 나스닥 포지션이 4%ile에서 상승 → 공포 해소(스퀴즈 완성).
- 🔴 반증: 하이퍼스케일러 캡엑스 컷 **또는** 실질금리 >2.55% → 오늘은 데드캣.

---
*출처: 상기 인라인 링크(WebSearch, asof 2026-07-21). 사내 뉴스 DB 401 다운으로 전부 공개 웹 기반. 일부 수치(마이크론 절대매출,
중국 생산량, HBM 점유율)는 추정/2차라 인라인에 플래그. 참고용 분석이며 매매 권유 아님.*
