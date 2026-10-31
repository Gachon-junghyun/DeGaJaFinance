---
name: upgrade-routine
description: 금융 하네스 개선 루틴(꿈, 매일) — 채점된 장부(lens credit·calib)와 루틴들이 남긴 시행착오(RUN/TRIALS.md·module_table)를 읽고, 근거가 있으면 금융 파이프라인 문서·자식 지시문·일정표를 직접 고친다. 고치기 전에 떠 두고, 고친 뒤 성적이 나빠지면 스스로 되돌린다. 주문은 하지 않는다.
---

# 개선 루틴 — 채점이 수행 지시문을 바꾸게 하는 고리

> **뭐냐:** 금융 하네스가 사람이 안 봐도 «채점 → 고치기 → 다시 채점»으로 스스로 나아지게 하는 주간 루틴의 절차서.
> **언제 읽나:** 이 루틴을 돌 때(예약 작업 `finance-upgrade`, 매일 06:30 — 미장 마감 뒤라 전날 물음이 정산된 다음). 루틴 문서를 손으로 고치기 전에도.
> **안 담는 것:** 채점 식(→ `module_lens/DESIGN.md`·`_learn.py`) · 주문 판단(→ `order_routine.md`) · 목표 표 꿈 절차(→ DeGaJa `RULES/채점.md` §3, 이 루틴은 그 금융판이다).

## 권한 — 사람 결정 (2026-10-31)
사람: *«금융 하네스는 너의 꿈과 근거가 있으면 막 바꿔도 되네»*. 그래서 이 루틴은 **근거가 붙은 변경**을 사람 승인 없이 적용한다.
- **고쳐도 되는 것:** 비중을 정하는 규칙(총 투자비중·종목 비중의 근거와 문턱 — 2026-10-31 사람이 목표 비중 규칙을 없앴다) · `pipeline/` 아래 문서 전부(루틴·스테이지·L2·L3 지시문) · `data/catalysts/*.json` · `pipeline/LEARNED.md`(재생성) · 자식 지시문 문구 · 문턱 숫자(사건 창 일수, 파급력 계산, 이름 목록 규칙).
- 🔴 **못 건드리는 것:** 주문 제출 금지와 `--execute` 규칙 · 깨지지 않는 선 셋(빚 없음·매도 ≤ 보유·제출은 사람) · 각 루틴의 «⛔ 절대 하지 않는 것» 목록 · 리포 `CLAUDE.md` 원칙(P1~P6) · 시크릿·계좌 · 모듈 코드(`module_*` — 코드 변경은 작업 세션 몫이고, 이 루틴은 «고쳐야 할 코드»를 일기에 적는다).
- **근거란:** lens 물음 번호(정산된 것) · credit/calib 숫자 · `RUN/TRIALS.md` 의 같은 실패 두 번 이상(서로 다른 날) · `module_table` 시도 번호. 근거 없는 «더 나을 것 같다»는 고치지 않고 `idea` 로만 남긴다.
- **만든 쪽이 아닌 세션이 고친다.** 이 루틴은 주문안 루틴과 다른 예약 작업으로 돈다.

## §1 모으기 (아무것도 안 고친다)
```bash
cd C:/Users/fivep/DeGaJaFinance
python -X utf8 -m module_lens score && python -X utf8 -m module_lens learn && python -X utf8 -m module_lens playbook
python -X utf8 -m module_lens calib > out/upgrade/calib_{오늘}.json
python -X utf8 -m module_lens replay > out/upgrade/replay_{오늘}.json   # 정책을 과거 장부에 되돌려 돌린 결과
python -X utf8 -m module_lens due
```
- 지난 실행(`pipeline/routines/UPGRADE_LOG.md` 맨 위 날짜) 뒤의 `llm_outputs/*/order_routine/TRIALS.md`·`DECISIONS.md` 를 읽는다.
- `cd C:/Users/fivep/DeGaJa_Agent && python -X utf8 -m module_table show 80` (금융 루틴 목표)와 그 아래 시도.
- 판정일이 지났는데 `text:` 라 안 매겨진 물음은 **데스크를 가리지 않고 전부**(하루 최대 10건, 오래된 것부터) 원문으로 결과를 확인해 `resolve` 한다. 이게 고리의 연료다 — 안 매기면 아무것도 배우지 못한다. 확인 못 하면 `AMBIGUOUS` 와 이유.

- 🔁 **매달 첫 실행: 과거 시뮬레이션을 새로 돌린다.** `out/sim/<갈래>/work/` 의 스크립트(news·inflection·flow·fundamentals·macro, 순서는 각 REPORT.md)를 평가 창을 최근 60거래일로 옮겨 다시 돌리고 `python -X utf8 -m module_lens import-sim <갈래…>` 로 넣는다(지금 채점기로 다시 재고, 장부 사본을 먼저 뜬다). 지시 꼴은 `out/sim/BRIEF.md`. 스크립트가 깨지면 고치고 그 사실을 일기에. 이게 사람이 가만히 있어도 표본이 쌓이는 두 번째 길이다(첫째는 루틴 §4-3).

## §2 패턴 보기 (아무것도 안 고친다)
변경 후보를 표로 만든다: **무엇을 · 어느 문서 어느 줄 · 근거(번호) · 기대 효과 · 되돌릴 기준**.
- 같은 도구 실패가 서로 다른 날 두 번 이상 → 그 자식 지시문에 «이렇게 하라» 한 줄.
- LEARNED 의 «쓰지 않을 방법»을 지시문이 아직 명시적으로 시키고 있음 → 그 지시를 다른 방법으로 바꾼다(«지켜보는 방법» 중 하나를 겨뤄 볼 후보로).
- calib 눈금이 3회 연속 같은 쪽으로 벌어짐 → 갈래 확률 매기는 규칙을 루틴 §4-2 에 숫자로.
- 데스크별 브라이어(`by_desk`)가 최근 정산 10건 이동평균으로 나빠짐 → 가장 최근에 바뀐 줄부터 의심한다(§4).
- 🎲 «지켜보는 방법»이 하나도 겨뤄지지 않았다면, 다음 주 루틴에 그 방법을 한 자식이 하나만 같이 재게 하는 줄을 넣는다(국소 최적 금지).

- 🔴 **숫자 손잡이(확률 눈금·기준률 당기기·방법 금지 문턱)는 `replay` 로만 고른다.** 후보 손잡이를 `module_lens/_replay.py` 의 `POLICIES` 처럼 과거 장부에 되돌려 돌려, 90% 구간 전체가 브라이어를 낮출 때만 채택한다. 시뮬레이션이 «아직 효과 확인 못 함»이면 손잡이는 그대로 두고 일기에 표본 수만 적는다. 새 후보 손잡이가 떠오르면 코드에 정책 하나를 더하는 건 작업 세션 몫이라 «고쳐야 할 코드»에 적는다.

## §3 고치기
1. **먼저 뜬다:** 고칠 문서마다 `out/upgrade/{오늘}/<경로를 _ 로 바꾼 이름>` 로 복사. 사본이 없으면 고치지 않는다.
2. 후보마다 고친다. 줄 끝에 `<!-- up {오늘} · 근거: Q168,Q171 · 되돌림: order_routine 최근 정산 10건 brier 평균이 {지금 값} 보다 0.05 이상 나빠지면 -->` 꼬리를 단다.
3. 하루 세 건까지. **같은 줄은 그 변경 뒤 정산이 5건 쌓이기 전에 다시 고치지 않는다**(매일 돌므로 효과를 잴 틈을 둔다). 고칠 근거가 없는 날은 고치지 않고 §4 되돌림 점검과 일기만 한다 — 그것도 정상 실행이다.

## §4 되돌리기 (자동)
- 지난 변경 꼬리(`<!-- up … -->`)마다 되돌림 기준을 지금 숫자로 잰다. 넘었으면 사본으로 그 줄만 되돌리고 일기에 «되돌림: 무엇 · 숫자»를 적는다.
- 정산된 물음이 변경 뒤 5건 미만이면 판단하지 않고 «보류»로 둔다.

## §5 일기와 보고
- `pipeline/routines/UPGRADE_LOG.md` 맨 위에 한 덩이: 고친 것(문서·줄·근거) · 되돌린 것 · 보류 · 고쳐야 할 코드(작업 세션 몫) · 확인 못 한 것.
- 표: 고친 것마다 `cd C:/Users/fivep/DeGaJa_Agent && python -X utf8 -m module_table ok|partial "<일반 규칙>" "<근거·숫자>" --id 80 --link "C:/Users/fivep/DeGaJaFinance/pipeline/routines/UPGRADE_LOG.md"`.
- 폰(보고 봇, 결재 아님 — 짧게, 계좌·금액 없이). **고친 것이나 되돌린 것이 있는 날만 보낸다** — 매일 «변경 없음»을 울리면 사람이 끈다:
  `cd C:/Users/fivep/DeGaJa_Agent && python -X utf8 -c "import io,module_voice as V; V.push_text('금융 하네스 개선 · {오늘}', io.open(r'C:/Users/fivep/DeGaJaFinance/pipeline/routines/UPGRADE_LOG.md',encoding='utf-8').read()[:3000])"`
- 커밋·푸시는 하지 않는다(사본과 일기가 되돌릴 그물이다).
