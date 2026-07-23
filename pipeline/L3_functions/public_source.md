# L3 · public_source — one claim → one source the READER can check

> **Single-role unit.** Independent — no ordering; an L1/L2 calls it when needed. Does ONE thing.

- **Role**: take one desk claim and return it as a reader-facing line **with a source that exists
  outside this repo** and **the time the thing actually happened, in KST** — or return nothing. The
  desk's own filenames, stage names, tags and module output are **not sources**. They are where we
  wrote it down, not where it came from.
- **Input**: one claim + wherever the desk recorded it.
- **Output**: `{line, 발생시각(KST), source, url}` in the reader's language, or `DROP` + the reason.

## ⚠ Rule 0 — the article's date is NOT the event's date
The event pass bins by **publish** time, so a story the outlets ran today reads as a thing that
happened today. Verify occurrence externally (WebSearch/WebFetch) before writing any item.
**Measured 2026-07-23** — the first draft's items, against what actually happened:

| Draft implied | Actually occurred | Gap |
|---|---|---|
| US–Iran fighting "today" | US soldiers killed **7/18 KST**, retaliation strikes **7/19–20 KST**; campaign in its **2nd week**, Hormuz traffic already largely stalled | **4–6 days** |
| USTR tariff "today" | Proposal **6/3 KST** (60 countries, 10–12.5%), hearing **7/8 KST**; only the "final action tomorrow" line was new | **51 days** |
| Alphabet capex "today" | US 7/22 after-close = **7/23 05:00 KST** — genuinely overnight, correct for a morning brief | 0 |

Both errors are one error: the date was inherited from the article. A 4-day-old escalation presented
as new makes the reader think the situation just changed; a 51-day-old proposal presented as new
makes a scheduled step look like a shock.

## ⚠ Rule 0b — everything in KST, with the local time in parentheses
The reader is in Korea. A US market event stamped with its US date is off by one and the reader has
no way to know which. Convert, then show both: `발생: 7월 23일 새벽 5시경 (미국 동부 7월 22일 장 마감 후)`.
- US Eastern (EDT) = **KST − 13h** → a 16:00 close is **05:00 KST next day**.
- London (BST) = KST − 8h · Middle East = KST − 6h.
- A US "tomorrow" is **two calendar days out** for the Korean reader. Measured: USTR's "as soon as
  tomorrow" said on US 7/23 lands **7/25 새벽 KST** — writing "내일" would have been wrong by a day.
- Scheduled events get the same treatment: FOMC 14:00 ET → **익일 03:00 KST**; PCE 08:30 ET →
  **당일 21:30 KST**.
- When only the date is knowable and not the hour, say the date and stop. Do not invent a time.

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

## The URL goes on the item's own `출처:` line — **Korean outlet preferred**
`출처: {발행처} {URL}`, directly under each item. No separate link block at the bottom: a reader who
doubts item 6 should not have to scroll to a footer and match numbers.
- **Prefer a Korean-language article** over the English original whenever one exists, even for a
  foreign event. The reader is Korean; an English wire is a worse source *for this reader* than a
  domestic paper reporting the same thing. Reach for the foreign original only when nothing domestic
  covered it.
- Korean coverage is also the better date check, because it states the local time explicitly —
  measured 2026-07-23: an English wire's "as soon as tomorrow" (published KST 7/23) was read as
  US 7/24; the Korean articles said 「22일(현지시간) 상원 금융위 서면발언, 이르면 23일 발표」,
  which puts it **tonight KST**, not two days out. Same fact, one day of error removed.
- Korean coverage frequently carries figures the English wire omits. Measured, same day: 브렌트유
  **94.07달러 (+3.36%)** and WTI 86.83 from 서울경제 vs a rounded 94.13 from a data aggregator;
  Alphabet's **2004년 상장 이후 첫 분기 잉여현금흐름 마이너스** appeared in the Korean write-ups
  and not in the English summary at all.
- Items whose date was never externally checked are still listed with their issuing body — and named
  in one closing line so they do not read as verified.

## ⚠ Rule 0c — never republish a number the desk's own files disagree on
If two internal sources carry different values, the brief does **not** pick one. Go out and get the
issuing body's figure, or drop the line. **Measured 2026-07-23**: the desk's files carried the 7/22
KOSPI close as both **6,797.70** and **7,153**, with the conflict already flagged in an upstream
report — and the draft published 7,153 without checking. The verified close was **6,797.70 (+49.75p,
+0.74%)**: the index touched 7,000 intraday on a semiconductor surge, tripped a buy-side circuit
breaker at 09:06, then gave the gain back. Publishing the unchecked figure would have put a ~5%
error in front of outside readers, and the *reason* for the two numbers (an intraday reversal) was
itself the story.

## ⚠ Rule 0d — a quarter and a cumulative are two different facts; print both
Same failure class as the desk's own "cite both halves of a print" rule, arriving in the publication
layer. **Measured 2026-07-23**: 「LG디스플레이 상반기 흑자 전환」 is true and reads as a turnaround —
but **Q2 alone was an operating loss of ₩107.7bn**, and the half-year profit came from Q1. A reader
given only the cumulative concludes the quarter was profitable. Write both, in the same sentence.

## DROP conditions (state the count, never silently)
- No source outside the repo → DROP.
- The number cannot exist at the brief's timestamp (see the gather stage's availability rule) → DROP
  or replace with the prior session's figure, labelled with which session.
- Position language (진입·비중·손절) → DROP. A brief is not a pitch and carries no recommendation.
