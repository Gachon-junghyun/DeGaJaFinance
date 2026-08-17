# L1 · BRIEF_RENDER — write it so a stranger can check every line (stage)

> Stage 3 of `morning_brief`. Render the ranked list into the published file. Calls L3.
> Output: `MORNING_BRIEF.md` under `llm_outputs/{date}/morning_brief/` — **this is the artifact that
> leaves the desk**, so it is the one place where the desk's private vocabulary is forbidden.

## Form
```
[YYYY-MM-DD] 08:30 · 장 시작 전
※ 모든 시각은 한국시간(KST)입니다. 해외 발생 건은 현지시각을 괄호에 함께 적었습니다.

■ 간밤에 일어난 일 (오늘 새벽)
1. {한 문장 사실 + 숫자}. {필요하면 왜 중요한지 한 절.}
발생: {KST 시각} ({현지 시각})
출처: {발행처} {URL — 한국 기사 우선}

■ 이어지고 있는 일 (오늘 새로 생긴 것이 아닙니다)
■ 전 거래일 마감 기준
■ 오늘 예정 (아직 일어나지 않았습니다)
■ 이번 주 남은 일정 (한국시간)
```
- The four `■` buckets come from the gather/rank stages and are **load-bearing, not decoration**: a
  reader must be able to tell at a glance what is new, what is continuing, and what has not happened
  yet. Never merge them to save space.
- `발생:` before `출처:` on every item. KST first, local time in parentheses.
- The URL sits on the item's own `출처:` line. **Cite the Korean outlet that carried it**, including
  for foreign events — see the public_source unit for why (it is the better date check, and it carries
  figures the English wires drop).
  ★ **This is the render-side face of W6, and by this stage it should already be free**: if the rank
  stage admitted foreign rows on the domestic-print test, every foreign item **already has a Korean
  outlet attached**. A foreign item that arrives here with only an English source is the signal that
  the test was skipped upstream — **send it back to ranking rather than citing the wire**. Measured
  2026-07-24: all five published foreign items carried Korean sources, and two of them
  (두바이유 90달러선, 원·엔 900원선) carried figures that existed **only** in the Korean copy.
- **Korean, plain text.** The file is Markdown so it renders anywhere, but the body must survive
  being pasted into a chat window with no formatting: no tables, no headers inside items, no bold
  runs, no emoji tags. A line that needs a table is a line that needs to be shorter.
- 2–4 lines per item on a phone. Numbers keep their units and their scale (억/조/%/bp).
- `출처:` on its own line, one per item.

## Length — locked at ~9,000–9,500 characters
15 news items at 3–4 lines each, plus the two calendar blocks. That is the settled size; do not
compress below it to make the file "chat-sized."
- **The background clauses are the readable part, not padding.** Measured 2026-07-23: the tariff item
  is only interesting because the merged history rides with it — a June 12.5% proposal, a
  pre-agreed 15% cap, LG's unretracted $28bn delay warning. Strip those and the line becomes
  "관세 발표 예고", which tells the reader nothing about what is at stake tonight. The same holds for
  the Iran item (why the oil bid is there) and the petrochemical item (why 7,000억 is being spent).
- If a chat window cannot take it in one message, **split at the `■` boundaries** — never mid-item,
  and never by dropping the `발생:`/`출처:` lines. An item without its date and source is not a
  shorter item; it is an unverifiable one.
- Going shorter is a coverage decision, not a formatting one: it means fewer than 15 items, and the
  cut count in the closing note has to move with it.

## L3 called
- [public_source](../L3_functions/public_source.md) — the binding rule for this stage: cite the
  **origin**, never our own filename; translate every desk tag into what it means; drop what has no
  outside source. That unit carries the substitution table and the measured failure behind it.

## What this stage does
- Write each item as fact-first: the thing that happened and its number, then at most one clause of
  interpretation. Interpretation is never a separate numbered item and never carries a `출처:`.
- **State uncertainty inline, in normal Korean.** "발표 예고" ≠ "발표". "속보치" ≠ "확정치".
  "전 거래일 종가 기준" belongs in the line, not in a footnote nobody reads.
- Close with the dated calendar item (what lands today / this week), split into domestic and foreign
  when both exist — a KR reader needs the domestic mechanism named, not buried among US earnings.
- One trailing note, only if true: what the brief could not see this morning (e.g. that domestic
  news volume at 08:30 is structurally near-zero, so nothing here reflects today's KR flow).

## Forbidden in the published file (the curse-of-knowledge gate)
- Our filenames and stage names: `MACRO_REPORT`, `EVENT_ALPHA`, `BET_SHEET`, `SECTOR_DEEP_*`,
  `CATALYST_WATCH`, `SCENARIOS`, `HANDOVER`, `§`, `L1/L2/L3`, `EXIT CHECK`.
- Our module names and CLI: `module_flow`, `module_paper_book`, `brief`, `thread`, `--scope …`.
- Our measurement vocabulary: 사건/스레드/분모/nb/회수율/BUILDING/FADING/RS20/RS60/🟢🟡🔴/D-0/★core.
- Book language: 진입·비중·손절·사이징·목표가 — **and any recommendation at all.** This is a brief.
- Any number whose only provenance is "우리가 계산했다" without the input being public.

## Linting a file that forbids rule IDs — record the exemption in `BRIEF_RANK.md`

`scripts/report_lint.py` asks that any finding you decline to fix be marked **with its rule ID in the
paragraph**. The ban list above forbids exactly that string in this file. **So declare exemptions in
`BRIEF_RANK.md`** — the desk file, where internal vocabulary is allowed — and let the published file
carry the same information **in plain Korean**.

Measured 2026-07-24: the Intel item tripped **C2** (a YoY figure with no sequential half). Handled by
(a) putting the opposing half into the item — *"같은 분기 손실 폭은 오히려 커졌습니다"* — and
(b) telling the reader why the missing half is missing — *"국내 보도에는 전분기 대비 수치가 실리지
않아"*, then (c) writing `RULE C2 · 면제 사유 …` into `BRIEF_RANK.md`.
★ **The pattern: the published file says what a reader needs in their language; the rule ID lives
where the next run will look for it.** A lint flag that survives on a published file is fine **once
the desk file explains it** — and that explanation is what the next run inherits.

## ✅ EXIT CHECK
- [ ] **Every item carries `발생:` in KST**, with the local time in parentheses for anything foreign.
      No item's date was inherited from when an article was published.
- [ ] Items sit in the right occurrence bucket; nothing in "간밤" happened days ago, nothing in
      "오늘 예정" is written as if it already landed (no results, no numbers from it).
- [ ] **Every `출처:` carries a URL where one exists, Korean-language wherever available.** Items
      with no link are named as unverified in the closing note, not left looking checked.
- [ ] **Every foreign item cites the Korean outlet that carried it (W6).** By this stage that should
      cost nothing — the rank stage admitted foreign rows precisely because a domestic outlet had run
      them. An English-only source here means the test was skipped upstream: return the item to
      ranking instead of citing the wire.
- [ ] **The closing note states the domestic/foreign split in plain Korean** — how many of the
      published items came from the prior domestic session versus overnight abroad, and how many
      events were knowable in each pool. Measured 2026-07-24 phrasing: *"전 거래일 국내에서 확인
      가능했던 시장 관련 사건은 357건, 간밤 해외는 810건이었고 이 글은 그중 15건을 골랐습니다."*
      **A reader who can see the split can judge the frame; one who cannot has to trust it.**
- [ ] **No index level, close, or headline price was copied from a desk file without checking the
      issuing body** — and any figure the desk's own files disagree on was re-sourced or dropped.
- [ ] **The overnight US line quotes all three indices together (Dow · S&P · Nasdaq) with a source,
      never one paraphrased from a cluster.** A single-index line inverts the mood: measured
      2026-07-25, a "다우 +360" line (wrong number, Dow-only) omitted that Nasdaq fell 0.6% on an
      AI-stock sell-off. Oil carries its level, daily direction, and the day it crossed — not just "100달러".
- [ ] **Every earnings line carries the quarter AND the cumulative when they point different ways.**
      A cumulative-only profit line on a loss-making quarter is a defective item, not a short one.
- [ ] **Ban list swept**: not one internal name, tag, module, or CLI string survives in the file.
      Grep it; do not eyeball it.
- [ ] **Linter run, and every surviving finding is explained in `BRIEF_RANK.md` with its rule ID** —
      never in the published file, which the ban list keeps free of rule IDs. The published file
      carries the same caveat in plain Korean.
- [ ] Every item's `출처:` names a body, a filing, or an outlet — something checkable without this
      repo. Any item that failed this was dropped upstream and counted, not softened.
- [ ] Every desk tag that carried information was **translated, not deleted** — the observation and
      its number survive in plain Korean.
- [ ] Hedges are inline and in normal language (예고/속보치/전 거래일 기준), not footnoted.
- [ ] Zero recommendations, zero position language.
- [ ] Item count stated against the cut count from the ranking stage, so the reader knows the brief
      is a selection and not the whole day.
- [ ] `MORNING_BRIEF.md` written; it pastes into a chat window unmangled.
