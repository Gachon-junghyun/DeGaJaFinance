# L1 · SIZE — risk-based sizing (stage)

> Phase 3. Turn each ENTER/ADD verdict into a share count the risk model allows — never a gut number. Calls L2.
> Output: `ORDERS.md`.

## L2 called
- [risk_model](../L2_modules/risk_model.md) — `module_paper_book size <ticker> --price P --stop S [--core]`:
  shares from `risk_amount / (price − stop)`, capped by max-position %; plus `concentration_check` for the
  theme/correlation caps.

## What this stage does
- For each ENTER/ADD: compute the share count from the **stop distance** (risk = equity × risk% ÷ per-share-risk),
  bounded by **max-position %**. ★core uses the lower **core-risk %** (a starter, not a full bet).
- If DECIDE stamped a name "hard-stop required" (momentum-only / ⚡crowded-short) but the report gave no stop,
  the model falls back to the default stop-% — state that the stop is synthetic, not report-anchored.
- **Enforce the caps as a batch, not per-name:** after tentatively sizing every ENTER, re-run the concentration
  check on the resulting book. If a theme breaches max-theme %, scale the correlated names down together
  (the "one risk unit" is sized once) — do not let five small ENTERs sum past the correlated cap.
- Respect available cash per sleeve (KRW / USD); if cash-constrained, rank by conviction and state what was cut.


### ★ 불확실성을 사이즈에 넣는다 (PLAY28, 배선 2026-07-22)
`module_paper_book size` 는 **스탑 거리로만** 크기를 정한다 — 변동성도, 엣지의 질도, 그 엣지
추정의 오차도 들어가지 않는다. 그래서 연변동성 47% 종목과 70% 종목이 같은 크기가 나온다.
교차확인으로 `python -X utf8 scripts/kelly_size.py <TKR> --ic <가정> --ic-n <관측수>` 를 돌린다.

- ⚠ **IC 는 측정값이 아니라 사람이 넣는 가정**이다. 근거 없는 IC 는 근거 없는 크기를 낳는다.
  lab 눈금: 외국인 수급 좋았던 부분표본 IC 0.33~0.44 · **앞 18개월 ≈ 0.015(사실상 0)**.
- ⚠ **IC 자체가 추정치다.** SE≈1/√n 이라 n=200·IC=0.05 면 95% 하한이 **−0.089** — 부호조차
  확립 못 한다. 하한이 IC 의 13%라도 남으려면 관측 **~2,030개**가 필요하다.
  이 경우 정답은 '거래 금지'가 아니라 **full Kelly 를 정당화할 수 없다**는 것이다.
- **1/4 Kelly** 권고 — 이상 성장률의 ~44% 를 안전마진 4배와 맞바꾼다. full Kelly 는 실측에서
  **in-sample 에서조차 손실**(연 −5%, MDD −71%).
- **무거래 밴드는 신호 z 1.5σ** — 신호 공간의 단위다. 가격 %로 환산하는 것은 신호가 가격기반
  (모멘텀·RS)일 때만 성립한다. 수급·추정치 리비전 신호에 그대로 쓰면 단위 혼동이다.
  공짜도 아니다 — 뒤집힘 국면에서 MDD 악화(−32%→−52%).
- ⚠ 권고 크기가 **1주 미만**이면 최소단위가 사이징을 대신 정하게 된다. 그 사실을 적고 넘어간다.

### 🚨 관측수가 IC 값보다 먼저 사이즈를 죽인다 (실측 2026-08-09)
`--ic` 를 **0.02 든 0.32 든** 넣어도 `IC하한`이 **0.0%** 로 나오는 구간이 있다. 구속조건은 IC 값이
아니라 **관측수**다 — `n=2` 면 SE≈0.707 이라 95% 하한 IC = **−1.336**, 즉 *"이 표본으로는 엣지의
부호조차 확립 못 한다"*. 하한이 IC 의 13%라도 남으려면 **2,030개**가 필요하다.
⇒ 이때 출력되는 `1/4 Kelly x%` 는 **엣지가 정당화한 크기가 아니라 full Kelly 의 기계적 삭감**이다.
그 사실을 적지 않고 그 숫자를 쓰면 근거 없는 크기를 근거 있는 것처럼 보고하는 것이다.
⇒ **그리고 「왜 못 사는가」를 뿌리까지 따라가라.** 실측: `n=2` 인 이유는 `eps_trend` 가 히스토리가
아니라 스냅샷이고, 그 해법(dig **D16**, 매일 저장)이 **조용히 죽어 있었다** — 19일에 6개, 간격이
2→3→4→6 으로 벌어지는데 화면은 *"35일 더"* 라고 말했다(개수를 일수로 셌다). **못 사는 사유가
종목이 아니라 계측 재고일 수 있다.**
⚠ **추정치 리비전 IC 는 `--ic` 근거로 쓸 수 없다** — 통제 실험에서 IT 섹터 로딩으로 판정됐다
(전체 W1 +0.403 / W2 −0.299 vs ex-IT +0.074 / −0.064, Q5−Q1 +9.4pp → **−1.1pp**). DEEP 참조.

### 🚨 「한 위험단위」를 라벨이 아니라 **실측**으로 센다 (D9, 배선 2026-08-10)
`concentration_check` 의 테마 상한은 포지션에 **사람이 적어 넣은 `theme` 문자열**로 묶는다. 그래서
**모회사와 자회사가 다른 라벨을 달면 다른 위험단위로 계산된다** — PLAY15 실측, 상위 20 상관쌍 중
**6개가 지주–자회사**. ★ **매핑표는 필요 없다**: 잔차상관이 임계를 넘으면 `risk_units` 가 자동으로
한 단위로 묶는다. 빠져 있던 건 표가 아니라 배선이었다.
- `python -X utf8 scripts/risk_units.py --book --exposure` → `llm_outputs/{date}/RISK_UNITS.json`
- `module_paper_book mark` 가 이제 그 파일을 읽어 **라벨 기준과 실측 기준을 나란히** 내고,
  갈리는 지점을 플래그한다: `unit_split_across_labels`(시장은 한 단위인데 라벨이 쪼개짐 ⇒ **상한이
  헐거워진다**) · `label_split_across_units`(반대 ⇒ 과하게 조인다).
- 합성 검증: 라벨 기준 각 33.3% < 40% 로 **통과**하는 책이 실측 기준 한 단위 **66.7% > 40% 위반**.
⚠ **실측 단위 자체가 창 선택에 민감하다** — 같은 8종목에서 `--days 250` 은 **5단위**, `500/750` 은
**7단위**({AVGO,NVDA,TSM} 가 1년 창에서 통째로 해체). 그리고 `--days 500` 은 **아무도 고른 적 없는
기본값**이다(규칙 C5). ⇒ **라벨을 대체하지 말고 나란히 쓰고, 쓴 `--days` 를 결론과 같은 줄에 적어라.**
⚠ 도구가 뱉는 `ARI`(안정성)를 **순위로 쓰지 마라** — 그룹핑이 **완전히 동일한** 두 창에 0.239 와 1.0 을,
혼자 다른 그룹핑을 낸 창에 0.65 를 매겼다. 도구 자신의 캡션(*"ARI 를 먼저 봐라"*)이 반대를 가리킨다.

## ✅ EXIT CHECK
- [ ] Every ENTER/ADD has a module-computed share count + stop; ★core sized at core-risk %.
- [ ] Post-batch concentration re-checked; correlated breaches scaled down together (logged).
- [ ] Cash-sleeve limits respected; any name cut for cash/caps stated with reason.
- [ ] **Kelly 교차확인 실행** — `scripts/kelly_size.py`. 스탑기반 크기와 차이가 3%p 넘으면
      그 차이를 적고, 어느 쪽을 왜 택했는지 남긴다(변동성·엣지오차를 무시한 결과인지 확인).
- [ ] **IC 가정이 명시**돼 있고, 그 IC 의 관측수(n)와 95% 하한이 같이 적혀 있다.
- [ ] 🚨 **95% 하한이 0 이하면 그 사실이 크기 옆에 적혀 있다** — *"이 크기는 엣지가 정당화한 것이
      아니라 full Kelly 의 기계적 1/4"*. 그리고 관측수가 부족한 **사유**(어느 계측이 안 쌓였나)가
      한 줄로 적혀 있다. 추정치 리비전 IC 는 `--ic` 근거로 쓰이지 않았다.
- [ ] 🚨 **집중도를 라벨과 실측 양쪽으로 쟀다** (`risk_units --book` → `mark`). 미스매치 플래그가
      있으면 그 이름들이 **한 단위로 함께** 축소됐고, **쓴 `--days` 가 결론과 같은 줄에** 적혀 있다.
      `RISK_UNITS.json` 이 없으면 그 사실이 사유와 함께 적혀 있다(조용한 라벨 폴백 금지).
- [ ] ⚠ **드라이런 통과를 실행 가능의 증거로 쓰지 않았다.** 실측 2026-08-09 — USD 슬리브 잔액이
      **0** 인데 `paper_book fill` 드라이런이 `BUY MU 1 @ 877.57` 을 그대로 통과시켰다(통화 슬리브
      검사는 `_allocate` 경로에만 있다). 통화 레그가 막혀 있으면 **주문 크기가 아니라 그 사실**을
      먼저 적는다 — `D155`(action_bracket 의 조용한 거짓음성)와 같은 가족이다.
