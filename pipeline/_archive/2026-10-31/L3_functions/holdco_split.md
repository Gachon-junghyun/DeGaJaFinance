# L3 · holdco_split — 연결 실체를 지분율로 쪼개, 본체에 남는 «값»과 «이익»을 분리한다

> **Single-role unit.** Independent — no ordering; an L2/L1 calls it when needed. Does ONE thing:
> take a consolidated parent that carries **listed subsidiaries**, subtract those stakes at market,
> and report what is left for the parent's own business — on **two axes at once**: value (SOTP) and
> earnings (attribution). It does not value the remainder; it only isolates it.
> Different from [segment_pnl](segment_pnl.md), which splits **one legal entity** into operating
> segments. This unit splits **one consolidated group** into legal entities the market prices separately.

## Why this exists (measured 2026-08-28, 034020 두산에너빌리티)
The name trades as a nuclear/gas-turbine story. Its consolidated statements say something else, and
**both the story and the statements are true at the same time** — the split is what reconciles them.

| axis | consolidated headline | what the split shows |
|---|---|---|
| 매출 | 2025년 **17.06조** | 본체 7.79조(45.7%) · **두산밥캣 8.79조(51.5%)** · 두산퓨얼셀 0.42조 |
| 지배순이익 | 2026E **3,193억** | 🔴 **밥캣 지분 몫 약 2,713억 = 85%** · 본체 약 1,000억 · 퓨얼셀 지분 몫 **-400억** |
| 시가총액 | **56.50조** | 밥캣 지분 2.91조 + 퓨얼셀 지분 1.03조 → **본체에 52.55조** |

⇒ 한 줄: **이 주식이 지금 버는 돈의 85%는 북미 소형 건설기계에서 나온다.** 그것이 나쁘다는 판정이
아니라, 뒤따르는 어떤 배수도 **분모를 틀리게 잡고 있었다**는 뜻이다. 이 단계 없이 계산한
「PER 177배」는 밥캣 이익까지 원전 이야기의 분모로 쓴 값이다.

## Method (deterministic)
1. **지분율과 주식수를 원문에서 뜬다** — 추정 금지. KR: DART `otrCprInvstmntSttus`(타법인 출자현황),
   `trmend_blce_qy`(기말 주식수)와 `trmend_blce_qota_rt`(지분율). 분기·반기 보고서마다 갱신된다.
2. **자회사 시가를 같은 날 종가로 맞춘다.** 부모와 자회사의 기준일이 하루라도 어긋나면 SOTP 가 흔들린다.
   지분가치 = 보유주식수 × 그날 종가. **지분율 × 자회사 시총으로 계산하지 마라** — 자사주·우선주 때문에 어긋난다.
3. **가치 축**: 부모 시총 − Σ(상장 자회사 지분가치) = **본체에 매겨진 시총**.
   여기에 **부모 «부문» 순차입금**(연결 순차입금이 아니다)을 더해 본체 EV 를 만든다.
4. **이익 축**: 자회사 컨센 지배순이익 × 지분율 = 자회사 몫. 부모 연결 지배순이익 − Σ(자회사 몫) = **본체 몫**.
   ⚠ 적자 자회사는 **음수 그대로** 넣는다(퓨얼셀 -400억). 빼먹으면 본체 이익이 과소평가된다.
5. **잔차를 적는다.** 위 계산의 잔차(연결조정·기타)는 지우지 말고 한 줄로 남긴다 — 034020 은 -120억이었다.

## ⚠ Guards
- **지주 할인을 이 단계에서 적용하지 마라.** 할인은 판단이고 이 단계는 분해다. 할인 없이(=회사에 유리하게)
  내고, 쓰는 쪽이 필요하면 깎는다. 할인을 여기 넣으면 하류 배수가 두 번 깎인다.
- 🔴 **자회사가 외화로 보고하면 통화를 확인하라.** 실측: 두산밥캣의 DART 재무제표는 **USD 표기**다
  (FY2025 매출 $6.182B). 원화로 착각하면 6.18조로 읽혀 **부모 사업보고서의 8.79조와 안 맞고**,
  「연결이 이상하다」로 오진한다. `currency` 필드를 반드시 읽어라.
- **본체 이익이 「연 환산」이면 그렇게 적어라.** 034020 의 본체 1,000억은 부문 반기 순이익 535억의
  연 환산 추정이다. 회사는 부문별 순이익을 공시하지 않는다 — **추정임을 산출물에 박는다**(P4).
- **비상장 자회사는 시가가 없다.** 장부가로 대체하되 「장부가」라고 표기하고, 본체 잔여값에 섞지 마라.

## Output (표 둘 + 한 줄, 판단 없음 — P4)
- **가치표**: `부모 시총 · 자회사별 (보유주식수 × 종가 = 지분가치) · 본체 시총 · + 부문 순차입금 · 본체 EV`
- **이익표**: `출처 · 금액 · 비중 · 산출근거` (자회사 몫 / 본체 몫 / 적자 자회사 / 잔차)
- 한 줄: **본체가 연결 지배순이익의 몇 %를 버는가.** 이 숫자가 하류 밸류에이션의 분모를 정한다.
