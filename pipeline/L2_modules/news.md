# L2 · news — news (orchestration)

> Called by L1s. Narrative collection, verification, blind-spot discovery. Composes L3 atomic steps.

## Two axes — they are NOT substitutes
Term-search answers **"is my theme hot?"**; it cannot answer **"what happened today?"**. Measured on
2026-07-07 (KOSPI −8%, circuit-breaker day): the term `코스피` ran at only **1.3× its normal share**, so
every term-frequency tool ranked it **nowhere** (`영업이익` won at 23.6×). The event view put the same
day's crash at **[39 articles/8 outlets]**. A term spikes when it is *new*; an event ranks when it is *big*.
Use the event axis for coverage, the term axis for discovery — and run both when the stage needs both.

## Calls — A. event axis (what happened, all of it)
0. L3 [daily_events](../L3_functions/daily_events.md) — `brief` (articles → **events**, tiered + denominator).
   Same story told 27–54× collapses to one line; ranking = how many outlets ran it.
   ⚠ Client-only (GPU). ⚠ Says *what*, not *why* — see that unit's ⚠ before acting on any event.

## Calls — B. term axis (L3 pipeline = news → companies → competitors)
1. L3 [random_news](../L3_functions/random_news.md) — `blindspot` (blind-pool sample + emergent terms).
2. L3 [drill_detail](../L3_functions/drill_detail.md) — body-inclusive confirm (`--field any` / `fts --full`).
3. L3 [related_companies](../L3_functions/related_companies.md) — `chain-hop` (beneficiaries never named in titles).
4. L3 [competitors](../L3_functions/competitors.md) — `industry_map` (value-chain neighbors).

## Direct search (when an L1 needs it)
- `python -X utf8 -m module_news_data fts search "<theme>" --scope foreign|domestic --syn --snippet`
  ⚠ Use **OR-mode + `--syn`** for bucket-wide sweeps; **AND-mode** for multi-token body drills
  (a bare common word in body-LIKE floods with noise). `--count` = token-0 velocity.
- `python -X utf8 -m module_news_data coverage "<terms>"` — what % of the pool my terms see (with denominator).
- ⚠ KR FTS is trigram: 2-char Korean terms return 0 (absence of INDEX, not absence of news) — use 3+ char synonyms.

## Output
Verified narratives + emergent themes + related/competitor companies + (if the event axis ran) the
day's events with their denominator. **The calling L1 folds them into its propositions/candidates —
and appends any confirmed new term to the protocol's living term table.**

⚠ **Cite the denominator, not just the hits.** The event axis hands you `articles → clusters → events`
and a tail count; a claim like "nothing else happened" is only allowed if that number backs it (P4).
