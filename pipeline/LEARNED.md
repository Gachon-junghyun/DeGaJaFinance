# LEARNED — 채점된 장부가 다음 회차에 시키는 것 (자동 생성)

> **뭐냐:** `module_lens` 의 정산 결과(credit·calib)로 기계가 쓴 방법 선호·금지·확률 눈금. 손으로 고치지 마라 — `python -X utf8 -m module_lens playbook` 이 다시 쓴다.
> **언제 읽나:** 루틴 메인이 자식에게 일을 넘길 때 이 파일 본문을 지시문 끝에 붙인다. 자식은 근거 방법을 고를 때 이 순서를 따른다.
> **안 담는 것:** 주문·투자총량·금지 목록(루틴 본문이 정본이고 이 파일로 못 바꾼다) · 말로 된 교훈(개선 루틴이 루틴 문서에 직접 쓴다).

생성 2026-10-31T20:52+09:00 · 정산된 물음 1473건 · 문턱: 정산 5회 이상, «변동성 기준률 대비 브라이어 개선»의 90% 구간 전체가 0 위면 먼저, 아래면 금지. 금지는 정산이 3개월 이상에 퍼졌을 때만.

## 먼저 쓸 방법
- (아직 문턱을 넘은 방법이 없다)

## 쓰지 않을 방법 — 기준률보다 확률을 나쁘게 만들었다. 근거 비중에 넣지 마라(맥락으로 읽는 것까지는 된다)
- classify the prior session's return as a volatility-scaled shock and read its forward excess base rate — 정산 120, 변동성 기준률 대비 브라이어 개선 -0.055 (90% -0.084~-0.026) · 적중 46/120
- classify the regulatory disclosure type on the filing and read post-filing drift — 정산 70, 변동성 기준률 대비 브라이어 개선 -0.036 (90% -0.066~-0.006) · 적중 23/70
- size a supply contract disclosure against trailing revenue — 정산 30, 변동성 기준률 대비 브라이어 개선 -0.052 (90% -0.101~-0.004) · 적중 8/30
- read preliminary operating profit change versus the prior-year quarter — 정산 30, 변동성 기준률 대비 브라이어 개선 -0.080 (90% -0.125~-0.035) · 적중 12/30

## 지켜보는 방법 (정산 3회 이상, 아직 문턱 사이 — 겨뤄 볼 후보)
- read deterministic chart structure turn verdict — 정산 65, 변동성 기준률 대비 브라이어 개선 -0.005 (90% -0.048~+0.039) · 적중 32/65
- read module flow tag from on-balance volume relative strength and volume surge — 정산 64, 변동성 기준률 대비 브라이어 개선 -0.006 (90% -0.048~+0.037) · 적중 27/64
- compare company news velocity with its own trailing baseline — 정산 64, 변동성 기준률 대비 브라이어 개선 +0.005 (90% -0.042~+0.052) · 적중 26/64
- measure semantic novelty of company news against its recent coverage — 정산 62, 변동성 기준률 대비 브라이어 개선 -0.028 (90% -0.066~+0.010) · 적중 29/62
- combine learned likelihood ratios across inflection signals with Bayesian adjudication — 정산 60, 변동성 기준률 대비 브라이어 개선 +0.002 (90% -0.054~+0.058) · 적중 24/60
- retrieve nearest past news-shock analogs by headline embedding and average their realized excess return — 정산 60, 변동성 기준률 대비 브라이어 개선 -0.028 (90% -0.078~+0.022) · 적중 24/60
- classify same-session headline types and read their historical forward excess return — 정산 60, 변동성 기준률 대비 브라이어 개선 -0.039 (90% -0.088~+0.011) · 적중 23/60
- count independent outlets covering the same news event before the close — 정산 59, 변동성 기준률 대비 브라이어 개선 -0.013 (90% -0.069~+0.043) · 적중 20/59
- compare weighted and equal-weight flow with underlying breadth and volume gates — 정산 58, 변동성 기준률 대비 브라이어 개선 -0.022 (90% -0.072~+0.027) · 적중 24/58
- read settled flow score and on-balance-volume state — 정산 58, 변동성 기준률 대비 브라이어 개선 -0.037 (90% -0.086~+0.013) · 적중 28/58
- measure narrative age and acceleration of a company's coverage — 정산 58, 변동성 기준률 대비 브라이어 개선 -0.017 (90% -0.065~+0.031) · 적중 25/58
- trace value-chain spillover from a peer news shock to a company without its own news — 정산 57, 변동성 기준률 대비 브라이어 개선 -0.022 (90% -0.072~+0.028) · 적중 17/57
- classify the current report items and read post-filing drift — 정산 55, 변동성 기준률 대비 브라이어 개선 -0.028 (90% -0.060~+0.004) · 적중 31/55
- compare reported earnings per share with the consensus estimate at report time — 정산 40, 변동성 기준률 대비 브라이어 개선 -0.028 (90% -0.070~+0.015) · 적중 16/40
- learn sector direction after large daily moves in rates, dollar, oil or credit spreads — 정산 33, 변동성 기준률 대비 브라이어 개선 -0.009 (90% -0.046~+0.029) · 적중 7/33

## 확률을 고치는 정책 — 되돌려 돌린 시뮬레이션(`replay`)에서 90% 구간 전체가 브라이어를 낮춘 것만 시킨다
- 시뮬레이션 표본: 갈래 확률이 있는 정산 1345건 중 평가 1325건, 정산 5회 이상 방법 30개.
  - calib_k5: 브라이어 차 -0.001 (90% -0.003~+0.001) → 아직 효과 확인 못 함
  - calib_k20: 브라이어 차 -0.001 (90% -0.003~+0.001) → 아직 효과 확인 못 함
  - base_rate_20: 브라이어 차 -0.002 (90% -0.004~-0.001) → 채택
  - base_rate_40: 브라이어 차 -0.002 (90% -0.006~+0.001) → 아직 효과 확인 못 함
  - vol_rate_40: 브라이어 차 -0.015 (90% -0.020~-0.011) → 채택
  - vol_rate_70: 브라이어 차 -0.019 (90% -0.026~-0.012) → 채택
- 🟢 **변동성 기준률 채택** — 갈래 확률을 매길 땐 먼저 그 종목의 60일 일간 수익 표준편차(σ60)로 아래 칸을 찾아 그 빈도에서 출발하고, 근거로 옮기는 건 그다음이다(시뮬: 확률을 이 칸 쪽으로 70% 당기면 브라이어가 낮아졌다).
  - h=5 (정산 949건): σ60 0.0~1.7% → A 20 / C 55 / B 24 · σ60 1.7~2.4% → A 27 / C 43 / B 30 · σ60 2.4~3.3% → A 31 / C 36 / B 33 · σ60 3.3~4.8% → A 31 / C 26 / B 43 · σ60 4.8~% → A 39 / C 22 / B 38
  - h=1 (정산 324건): σ60 0.0~1.6% → A 15 / C 64 / B 21 · σ60 1.6~2.1% → A 32 / C 50 / B 18 · σ60 2.1~2.9% → A 25 / C 54 / B 21 · σ60 2.9~4.3% → A 24 / C 49 / B 28 · σ60 4.3~% → A 43 / C 18 / B 40

## 갈래 치우침 — 근거가 어느 갈래를 지지했고 실제로 무엇이 일어났나
- 근거가 지지한 갈래: {'B': 507, 'A': 289, 'C': 573} · 실제 일어난 갈래: {'B': 415, 'A': 388, 'C': 542}
- 일어난 쪽(대개 가운데·현상유지 갈래)을 지지하는 근거가 적으면, **현상유지 갈래를 지지하는 근거를 일부러 하나 찾아 붙인다**(극단 갈래만 근거를 모으는 치우침).

## 확률 눈금 (참고)
- 80~100% 라고 한 갈래는 실제로 60% 일어났다(표본 5, 말한 평균 82%). 이 구간을 매길 땐 일어난 빈도 쪽으로 옮겨라.

## 근거 종류별 브라이어 (낮을수록 잘 맞음)
- report: 0.14 (물음 1)
- options: 0.43 (물음 16)
- price: 0.60 (물음 226)
- macro: 0.61 (물음 116)
- positioning: 0.62 (물음 33)
- flow: 0.63 (물음 217)
- filing: 0.66 (물음 202)
- other: 0.67 (물음 72)
- estimates: 0.68 (물음 73)
- news: 0.68 (물음 457)

## 변경 이력
- 2026-10-31 — 자동 생성. 이력은 git 과 개선 루틴 일기(`pipeline/routines/UPGRADE_LOG.md`)에 남는다.
