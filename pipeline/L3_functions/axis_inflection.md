# L3 · axis_inflection — 패턴 발견기의 산출을 IC 축으로 내보낸다

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing.
> 엔진 = `scripts/axis_inflection.py`. 소비자 = L3 [ic_ledger](ic_ledger.md).

- **Role**: `module_inflection` 의 패턴 신호를 **채점 가능한 축**으로 바꾼다. 발견과 검증을 잇는 배관.
- **CLI**:
  ```bash
  python -X utf8 scripts/axis_inflection.py            # 모든 런 날짜에 축 파일 생성
  python -X utf8 scripts/axis_inflection.py --status
  python -X utf8 scripts/ic_ledger.py log              # 새 축이 자동으로 잡힌다(원장 수정 0)
  ```
- **Output**: `out/ic/axes/kr_{run}.json` = `{"축이름": {"티커": 점수}}`.

## 내보내는 축

| 축 | 뜻 | 왜 |
|---|---|---|
| `mention_z` | 종목별 뉴스 언급수 z (직전 30일, 당일 제외) | **군중의 관심이 지금 비정상적으로 몰렸나** = 심리 축 |
| `mention_z_chg` | 그 z 의 1일 변화 | 관심의 **가속**. 수준과 변화는 다른 축이다(렌즈 B1 의 관심축 버전) |

⚠ **방향 가설을 여기서 세우지 않는다.** 관심 급증이 선행인지 꼭지인지는 **IC 가 답한다**(P4).
⚠ **선행참조 금지**: `mention_z` 는 정의상 직전 30일만 본다(당일 제외) — 런 시점에 알 수 있는 값이다.
⚠ **P6**: mention 계열은 CPU·sqlite 다. `module_inflection` 의 GPU 경로(`analog --text`)는 쓰지 않는다.

## 이 유닛이 존재하는 진짜 이유 — 이 리포에 없던 것은 발견기가 아니었다

패턴 발견기는 이미 여러 개다: `module_inflection`(변곡·언급·전례) · `lab/ECONOPHYSICS`(수급·심리
PLAY17~28) · `module_news_data thread`(사건 궤적). **없던 것은 눈금자다.**

그 대가는 실측돼 있다 — 2026-07-31 하루에만:
- `leak_scan` 의 *"보유가 샌다"* 가 **지평만 바꾸니 부호 반전**(D105)
- `missed_ledger` 첫 관측이 **결과선택 편향**으로 뒤집힘(D106)
- `ic_ledger` 첫 실행이 **`t=+6.7` 짜리 거짓 패턴** 생산(3개 창이 전부 같은 반등)
- 그리고 이 유닛의 `mention_z` 가 **n=7 에서 필요n 44 → n=14 에서 757** 로 신호 증발

**발견기는 거짓 패턴을 대량 생산한다.** 828종목 × 지표 × 지평을 훑으면 |t|>2 가 우연히 수십 개다.
⇒ **순서는 눈금자 → 발견기.** 이 배관이 있으면 새 패턴 모듈은 마음껏 탐색해도 된다 —
산출을 축 파일로 떨구는 순간 `ic_ledger` 가 자동으로 채점하고, 안 되는 축은 몇 달 뒤 스스로 죽는다.

## 다음 축을 붙이는 법

`ic_ledger` 도 이 파일도 **고치지 않는다.** 새 생산자가 같은 서식으로
`out/ic/axes/{market}_{run}.json` 에 자기 축을 추가하면 끝이다(같은 파일에 병합됨).
경제 레짐·군중심리·수급 물리 축이 늘어나도 원장은 그대로다.
