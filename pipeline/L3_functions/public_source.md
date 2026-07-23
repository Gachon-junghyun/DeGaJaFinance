# L3 · public_source — one claim → one source the READER can check

> **Single-role unit.** Independent — no ordering; an L1/L2 calls it when needed. Does ONE thing.

- **Role**: take one desk claim and return it as a reader-facing line **with a source that exists
  outside this repo** — or return nothing. The desk's own filenames, stage names, tags and module
  output are **not sources**. They are where we wrote it down, not where it came from.
- **Input**: one claim + wherever the desk recorded it.
- **Output**: `{line, source}` in the reader's language, or `DROP` + the reason.

⚠ **This unit exists because of a measured failure.** The first morning-brief draft (2026-07-23)
  carried eight items; **four cited sources only this repo can resolve** — `EVENT_ALPHA Card 1`,
  `MACRO_REPORT §1`, `module_flow KIS 실측`, `SCENARIOS S8-C`. Every one of those facts had a real
  public origin (USTR's own statement, 한국은행, 거래소, 외신) that the draft walked **past** on its
  way to citing our own file. That is worse than citing nothing: an unresolvable reference still
  *reads* as authority, so the reader trusts a claim they cannot check — the exact inversion of P4.

## The substitution rule
**Cite the origin, not the ledger.** Ask: "where did this fact enter the world?"

| Recorded as | Cite instead |
|---|---|
| `MACRO_REPORT §1` GDP line | 한국은행 (2분기 국민소득 속보치, 발표일) |
| `EVENT_ALPHA` card | the statement itself + how many outlets carried it |
| `module_flow` / KIS actuals | 한국거래소 투자자별 매매동향 (거래일 명시) |
| `module_disclosure` / DART | 금융감독원 전자공시 (공시 종류: 잠정실적·단일판매공급계약 등) |
| `CATALYST_WATCH.json` | the issuing body's own calendar (연준·BEA·회사 IR) |
| `SECTOR_DEEP_*` / `BET_SHEET` | the underlying filing, print, or article — never the report |
| a news event cluster | the outlet(s), with the count if the count is the point |

If the answer is "it came from our own reasoning" → it is **not a fact line**. It may appear as one
clause of interpretation attached to a sourced fact, never as its own numbered item.

## Vocabulary — translate, do not drop
The tags carry real information; the reader just can't decode them. Never emit the token — emit what
it means, and only if the underlying observation has a public source.

| Desk token | Reader line |
|---|---|
| 🟢가속 매집 / 🔴분산 | "기관이 20거래일 연속 순매수" / "외국인이 20거래일간 N만주 순매도" |
| BUILDING 스레드 4일 (3→2→4→4) | "나흘째 보도가 늘고 있다" |
| FADING / ENDED | "보도량은 줄었다 (사안 종결은 아님)" |
| RS20 / RS60 | "1개월/6개월 상대수익률" |
| nb, 사건, 스레드, 분모 | (never appears — internal measurement vocabulary) |
| D-0 / D-6 | "오늘" / "다음 주 수요일(7/29)" |
| 🟢LIVE / 🔴RESOLVED | "아직 유효" / "이미 반영됨" |
| §, 스테이지, L1/L2/L3, EXIT CHECK | (never appears) |
| ★core, 하드스탑, 사이징 | (never appears in a public brief — that is book language) |

⚠ **Translating is not softening.** "외국인 3,740만주 순매도"는 그대로 숫자로 간다. 지우는 건
  **우리 내부 이름**이지 관측값이 아니다.

## DROP conditions (state the count, never silently)
- No source outside the repo → DROP.
- The number cannot exist at the brief's timestamp (see the gather stage's availability rule) → DROP
  or replace with the prior session's figure, labelled with which session.
- Position language (진입·비중·손절) → DROP. A brief is not a pitch and carries no recommendation.
