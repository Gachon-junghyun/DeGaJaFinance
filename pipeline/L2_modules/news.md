# L2 · news — news (orchestration)

> Called by L1s. Narrative collection, verification, blind-spot discovery. Composes L3 atomic steps.

## Two axes — they are NOT substitutes
Term-search answers **"is my theme hot?"**; it cannot answer **"what happened today?"**. Measured on
2026-07-07 (KOSPI −8%, circuit-breaker day): the term `코스피` ran at only **1.3× its normal share**, so
every term-frequency tool ranked it **nowhere** (`영업이익` won at 23.6×). The event view put the same
day's crash at **[39 articles/8 outlets]**. A term spikes when it is *new*; an event ranks when it is *big*.
Use the event axis for coverage, the term axis for discovery — and run both when the stage needs both.

## Calls — A. event axis (what happened, all of it — and how it is MOVING)
0. L3 [daily_events](../L3_functions/daily_events.md) — `brief --body 2` (articles → **events**,
   tiered + denominator). Same story told 27–54× collapses to one line; ranking = how many outlets ran it.
   ⚠ **Pass `--body 2`** — the default samples a random 10 of the tail and drops the rest (measured
   2026-07-17: TSMC ₩148tn / 환율 1480원 / CXMT HBM bypass were ALL at 2 outlets = invisible).
   ⚠ Client-only (GPU). ⚠ Says *what*, not *why* — see that unit's ⚠ before acting on any event.
0b. L3 [event_threads](../L3_functions/event_threads.md) — `thread --days 7` (the same events
   re-linked ACROSS days → per-day outlet curves + BUILDING/FADING/REIGNITED/ENDED). The daily
   brief is a photograph; this is the film. Measured: the BOK rate-hike saga was visible **5 days
   early** as a 2-outlet tail item climbing (`2→7→6→7→5→8`) — a single day's brief can never show
   that. Run it right after the brief: today's events inherit their history, and "new today" vs
   "day 5 of a crowded saga" becomes a fact, not a guess. ⚠ Client-only (GPU). ⚠ Tags are curve
   shapes, not importance — and a holiday window-end inflates FADING (see the unit's ⚠).

## Calls — B. term axis (L3 pipeline = news → companies → competitors)
1. L3 [random_news](../L3_functions/random_news.md) — `blindspot` (blind-pool sample + emergent terms).
2. L3 [drill_detail](../L3_functions/drill_detail.md) — body-inclusive confirm (`--field any` / `fts --full`).
3. L3 [related_companies](../L3_functions/related_companies.md) — `chain-hop` (beneficiaries never named in titles).
4. L3 [competitors](../L3_functions/competitors.md) — `industry_map` (value-chain neighbors).

## Direct search (when an L1 needs it)
- `python -X utf8 -m module_news_data fts search 반도체 메모리 HBM --scope domestic --mode or --syn --snippet`
  ⚠ **Never quote a multi-word bucket — it fails silently to ~0.** `terms` is `nargs='+'`: one argv =
  one term. Measured: `fts search "반도체 메모리 HBM"` (quoted = one 13-char *phrase*) → **1 hit**;
  the same three words as three args → **31,698**. `coverage "반도체,금리,환율"` (comma-joined) → **0**.
  Nothing warns you — a mis-passed bucket just looks quiet, which is exactly the P4 trap the calling
  L1's EXIT CHECK is meant to catch. Write terms as separate argv, always.
  ⚠ Use **OR-mode + `--syn`** for bucket-wide sweeps; **AND-mode** for multi-token body drills
  (a bare common word in body-LIKE floods with noise). `--count` = token-0 velocity.
  `--kr` searches the trigram index: ~15% more hits (반도체 25,243 → 29,247). Not required for Korean
  terms — they work without it — but prefer it for KR bucket sweeps.
- `python -X utf8 -m module_news_data coverage 반도체 금리 환율 --days 7` — what % of the pool my terms see.
  ⚠ **A zero denominator prints 🟢 양호.** Measured: `coverage "반도체,금리,환율"` → 0건 / recall 0.0% /
  **"🟢 양호 — 관련기사의 0.0%가 안 보임"**; the same terms as three argv → 1,936건 / recall 38.9% /
  **"🔴 심각"**. A 🟢 verdict sitting on 0건 means you passed the terms wrong — it is not good news.
- ⚠ KR FTS is trigram: 2-char Korean terms return 0 (absence of INDEX, not absence of news) — use 3+ char synonyms.

## Output
Verified narratives + emergent themes + related/competitor companies + (if the event axis ran) the
day's events with their denominator. **The calling L1 folds them into its propositions/candidates —
and appends any confirmed new term to the protocol's living term table.**

⚠ **Cite the denominator, not just the hits.** The event axis hands you `articles → clusters → events`
and a tail count; a claim like "nothing else happened" is only allowed if that number backs it (P4).
