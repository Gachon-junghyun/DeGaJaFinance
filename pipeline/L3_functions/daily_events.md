# L3 · daily_events — the day's events (not articles)

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing.

- **Role**: turn a day's raw article flood into **events** — same story told 27–54 times collapses
  to one line, ranked by **how many outlets ran it** (= editors independently judging it news).
  This is the "what actually happened today, all of it" axis; term-frequency tools cannot give it.
- **Input**: `--date` (market day, published_at-based) · `--scope domestic|foreign|all`.
- **CLI** (client-only — needs the GPU vector store; run `embed sync` first, ~2s/day):
  ```bash
  python -X utf8 -m module_news_data embed sync                          # catch up (server→client)
  python -X utf8 -m module_news_data brief --date <D> --scope domestic --body 2 --json
  ```
  ⚠ **`--body 2` is not optional for a stage that must see the day.** At the default (`--body 3`)
  every 2-outlet event falls into `tail`, which emits a **random 10 and drops the rest**. `--body 2`
  empties the tail into one-line-per-event body rows. Measured 2026-07-17 (domestic): default =
  head 5 + body 18 + tail 45 (10 shown) = **33 of 68 market events, 6,915 B / ~4.8k tok**;
  `--body 2` = head 5 + body 63 + tail 0 = **all 68, 10,198 B / ~7.1k tok**. **+2.3k tokens buys
  +35 events.** The tiering was sized against the *article* count (the module header's "제목 전부 =
  146k 토큰" is 4,279 **articles**) — clustering already collapsed that to ~512 events/day, so the
  token argument for sampling the tail no longer holds.
- **Output**: tiered — `head` (≥`--head` outlets, with evidence) · `body` (one line each) ·
  `tail` (below `--body`: **count + random 10; the other rows are not emitted**) ·
  `denominator` (articles→clusters→events) · `excluded_nonmarket` (**count + first 5 only**).
  Measured 2026-07-07: 3,782 articles → 512 events → 394 market → head 61 / body 143 / tail 190 ≈ 44k tokens.

⚠ **The tail hides structural prints.** Measured 2026-07-17 (제헌절 holiday, 725 articles):
  **TSMC's ₩148tn US fab expansion, 환율 1480원 + the 24h FX-market opening, and CXMT's 667억위안
  HBM-moat bypass all sat at 2 outlets** — inside the tail the default never shows, and all three were
  macro-transmission input. Same failure as the milder "Korea–Singapore FTA renegotiation at 2
  outlets". `--body 2` fixes it.

⚠ **Do NOT invert that into "the head is fluff" — measured, that read was wrong.** The same day's
  head, 최태원 "SK하이닉스 주가는 우상향…가만히 갖고 있어야" [10 art/**7 src**, the day's most-carried
  item], scans as a chairman's platitude. It was damage control after SK하이닉스 closed **−11.53%**
  the prior session (−28% on the month; KOSPI −6.37% to 6,820, −18% in 11 sessions). Seven desks ran
  it because it mattered — outlet-count ranked domestic attention **correctly**. What outlet-count
  cannot do is rank *importance to a position*, and **`brief` carries no prices**: this unit alone
  cannot tell you which events matter. Read the tape first (PULSE / `module_flow`), then rank.

⚠ **`nb` is a sort hint, not a gate — and the nonmarket bucket is a real blind spot.** The classifier
  splits at `nb > 0`, and `excluded_nonmarket` emits **only 5 of them** (hardcoded `nonmarket[:5]`,
  **no CLI flag opens it**) at a self-declared 10–14% LOSO error — so ~40 nonmarket events × 10–14%
  ≈ **4–6 real market events per day you cannot see**. Measured 2026-07-17: 트럼프's "China interfered
  in the 2020 election" sat in head at nb=0.1 while the same thread's 트럼프 부정선거론 연설 fell to
  nonmarket at nb=−2.7; a TV AI talk scored nb=11.0 against TSMC's ₩148tn at nb=17.9. Read every event
  line and judge direction yourself (P4); do not treat `nb` ordering as importance.
⚠ **This does not say direction.** 2026-07-07's top event [54 articles/9 outlets] was Hanwha Ocean
  **LOSING** the Canada submarine deal, not winning it. The headline alone misleads; `--lede` would
  carry the why but is **off by default** (asiae·sedaily bodies are 100% page furniture in the first
  400 chars → 22% of ledes belonged to a different article). Until the scraper is fixed, confirm
  direction with [drill_detail](drill_detail.md) before you act on any event.
⚠ Market/non-market filtering is **domestic-only** (the classifier is Korean-trained). Foreign feeds
  are 82% finance by source selection, so nothing is filtered there — `nb` comes back null, not 0.
