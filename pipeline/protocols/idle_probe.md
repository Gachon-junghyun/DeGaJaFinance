# PROTOCOL — idle_probe (놀고 있는 능력을 가설로 바꿔 닫는다)

> A protocol = an ordered composition of L1 blocks. **Order is owned by this file.** L1s are referenced only.
> Purpose: 이 리포가 **소유하고 있으나 부른 적 없는 실행표면**을 찾아, 데스크가 **이미 등록해 둔 미해결
> 질문**과 교차시켜 가설을 만들고, 통제군까지 돌려 **닫는다.** 엔진은 유휴 모듈 자신 + `module_epistemics`
> + `module_paper_book`/`module_order_desk`. 산출 루트 `llm_outputs/{YYYY-MM-DD}/idle_probe/`.
> 런타임 `--market us|kr`.

## 왜 이 프로토콜이 존재하는가 (측정된 기원, 2026-08-09)
`handoff/README.md` 는 자기 도구표 서문에 *"아무도 안 부르는 능력은 존재하지 않는 능력"* 이라 적어놓고,
**그 표 안에 호출 0 인 명령을 3주간 담고 있었다**(`scripts/measure_ic.py`). 인구조사를 처음 돌리자
완전 유휴 6개가 나왔고, 그중 하나(`module_disclosure_us`)를 데스크의 3주 묵은 열린 모순(**C1**)과
등록된 dig(**D1**)에 이었더니 — **최상단 레짐 콜의 증거 1번을 다시 쓰게 만드는 1차 출처**가 나왔다.
새 데이터도, 새 모델도 아니었다. **이미 산 도구를 처음 겨눈 것뿐이다.**

## What this desk is (and is NOT)
- **IS:** 유휴 능력 → 가설 → 통제된 측정 → **착지물**로 바꾸는 실험 루프. 산업 데스크가 *판정*을 내는
  동안, 이 데스크는 **판정에 쓰이는 계기와 미해결 질문 자체**를 대상으로 삼는다.
- **IS NOT:** 집행자. 마지막 스테이지도 **intent 카드만** 쌓는다 — 사람이 [체결]로 하나씩 발사(P5).
  `--execute` 없음, 자동발사 없음. 분석·예시이며 **투자자문이 아니다.**
- **IS NOT:** 캐리 기록자. 🚨 **이 프로토콜은 `handoff/` 에 쓰지 않는다.** R/M/D/S 카운터는 산업 데스크
  런이 소유하고 **충돌이 미해결 dig(D137·D211)** 로 열려 있다. 여기서 나온 것은 *후보*로 산출 파일에
  적고, 번호 부여와 캐리 반영은 **다음 산업 런 또는 사람**이 한다.

## File-output rules
- 런 산출 → `llm_outputs/{date}/idle_probe/`: `CENSUS.md` · `HYPOTHESES.md` · `PROBE_LOG.md` ·
  `CONTROL.md` · `FINDINGS.md`(착지물 + 캐리 후보).
- 상태 변경 파일: `out/order_desk/kis_stack.json`(스테이징 카드, `--clear` 금지 — 기존 카드 보존) ·
  `out/ic/axes/*`(새 축을 등록한 경우) · `data/estimates/*`(회수한 스냅샷).
- 시크릿 금지. 모든 파생 숫자는 모듈이 계산한 것.

## Composition (L1 order)

| # | L1 block | Output |
|---|---|---|
| 0 | [CENSUS](../L1_stages/census.md) ★idle | `CENSUS.md` — 실행표면 인구조사 → 완전유휴 / 배선안됨 / shim |
| 1 | [PAIR](../L1_stages/pair.md) ★idle | `HYPOTHESES.md` — 유휴 능력 × 등록된 미해결 질문. 분기 정보량·검정력 사전판정 |
| 2 | [PROBE](../L1_stages/probe.md) ★idle | `PROBE_LOG.md` — v번호 사슬(실패한 v 포함) · 1차/2차 등급 |
| 3 | [CONTROL](../L1_stages/control.md) ★idle | `CONTROL.md` — 통제군 · 기본값 스윕 · 자기주장 재검(D48) |
| 4 | [ADJUDICATE](../L1_stages/adjudicate.md) ★idle | 축 등급 기반 충돌 구조화 · 사후확률 · 잔여충돌 |
| 5 | [SIZE](../L1_stages/size.md) | 크기를 **고르지 않고 기계에 묻는다** — `kelly_size` IC 스윕 |
| 6 | [STAGE_ORDERS](../L1_stages/stage_orders.md) | 조건부 intent 카드 → `kis_stack.json`(사람이 발사) |

## ★ 종결 규칙 — 산문으로 끝나면 그 사이클은 없었던 것이다
모든 가설은 아래 넷 중 **하나 이상**으로 착지해야 한다. 어디에도 안 닿으면 그 사이클은 실패로 적는다.

| 착지 형태 | 어디로 | 왜 |
|---|---|---|
| **ic_ledger 축** | `out/ic/axes/{market}_{run}.json` | 런 1개 = 관측 1개로 누적된다. 이 리포의 시계 |
| **스택 카드** | `out/order_desk/kis_stack.json` | 사람이 발사할 수 있는 형태. 조건과 반증을 카드 노트에 |
| **등록된 dig** | `FINDINGS.md` 의 캐리 후보 | 사람 승인이 필요한 코드 결함·구조 결함 |
| **철회 후보** | `FINDINGS.md` 의 캐리 후보 | 캐리된 주장이 깨진 경우. **번호는 여기서 안 붙인다** |

## Runtime deltas (vs 산업 데스크)
- **대상이 시장이 아니라 계기와 질문이다.** 시장 판정을 바꾸는 것은 부산물이지 목표가 아니다.
- **SIZE 는 크기를 고르지 않는다.** `--ic` 를 여러 값으로 스윕해 *"거래가 열리려면 IC 가 얼마여야 하나"* 를
  기계에 묻는다. 실측 — 어떤 IC 를 넣어도 `IC하한 0.0%` 였고, 구속조건은 IC 값이 아니라 **관측치 2개**였다.
  ⇒ **"살 수 없다"의 사유가 종목이 아니라 계측 재고일 수 있다. 그 경우 사유를 뿌리까지 따라간다.**
- **막힌 레그는 소리 내어 남긴다.** 실측 — USD 슬리브 0 이라 원화로 US 매수 불가인데 `fill` 드라이런은
  그걸 **통과시킨다**(조용한 거짓양성). 드라이런 통과를 실행 가능의 증거로 쓰지 않는다.
- **PROBE 는 재구현하지 않는다.** 외부 호스트가 막으면 그 호스트와 이미 말하는 모듈을 import(P1).

**Start → read [CENSUS](../L1_stages/census.md) and execute.** EXIT CHECK 를 통과한 뒤에만 다음으로.
마지막에 `FINDINGS.md` 의 캐리 후보를 **사람에게 넘긴다** — 이 데스크는 캐리에 직접 쓰지 않는다.
