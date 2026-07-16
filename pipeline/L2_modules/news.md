# L2 · news — news (orchestration)

> Called by L1s. Narrative collection, verification, blind-spot discovery. Composes L3 atomic steps.

## Calls (L3 pipeline = news → companies → competitors)
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
Verified narratives + emergent themes + related/competitor companies. **The calling L1 folds them
into its propositions/candidates — and appends any confirmed new term to the protocol's living term table.**
