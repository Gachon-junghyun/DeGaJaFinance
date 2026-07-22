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

## ✅ EXIT CHECK
- [ ] Every ENTER/ADD has a module-computed share count + stop; ★core sized at core-risk %.
- [ ] Post-batch concentration re-checked; correlated breaches scaled down together (logged).
- [ ] Cash-sleeve limits respected; any name cut for cash/caps stated with reason.
- [ ] **Kelly 교차확인 실행** — `scripts/kelly_size.py`. 스탑기반 크기와 차이가 3%p 넘으면
      그 차이를 적고, 어느 쪽을 왜 택했는지 남긴다(변동성·엣지오차를 무시한 결과인지 확인).
- [ ] **IC 가정이 명시**돼 있고, 그 IC 의 관측수(n)와 95% 하한이 같이 적혀 있다.
