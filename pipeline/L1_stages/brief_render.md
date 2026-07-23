# L1 · BRIEF_RENDER — write it so a stranger can check every line (stage)

> Stage 3 of `morning_brief`. Render the ranked list into the published file. Calls L3.
> Output: `MORNING_BRIEF.md` under `llm_outputs/{date}/morning_brief/` — **this is the artifact that
> leaves the desk**, so it is the one place where the desk's private vocabulary is forbidden.

## Form
```
[YYYY-MM-DD]

1. {한 문장 사실 + 숫자}. {필요하면 왜 중요한지 한 절.}
출처: {독자가 확인할 수 있는 발신처}

2. …
```
- **Korean, plain text.** The file is Markdown so it renders anywhere, but the body must survive
  being pasted into a chat window with no formatting: no tables, no headers inside items, no bold
  runs, no emoji tags. A line that needs a table is a line that needs to be shorter.
- 2–4 lines per item on a phone. Numbers keep their units and their scale (억/조/%/bp).
- `출처:` on its own line, one per item.

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

## ✅ EXIT CHECK
- [ ] **Ban list swept**: not one internal name, tag, module, or CLI string survives in the file.
      Grep it; do not eyeball it.
- [ ] Every item's `출처:` names a body, a filing, or an outlet — something checkable without this
      repo. Any item that failed this was dropped upstream and counted, not softened.
- [ ] Every desk tag that carried information was **translated, not deleted** — the observation and
      its number survive in plain Korean.
- [ ] Hedges are inline and in normal language (예고/속보치/전 거래일 기준), not footnoted.
- [ ] Zero recommendations, zero position language.
- [ ] Item count stated against the cut count from the ranking stage, so the reader knows the brief
      is a selection and not the whole day.
- [ ] `MORNING_BRIEF.md` written; it pastes into a chat window unmangled.
