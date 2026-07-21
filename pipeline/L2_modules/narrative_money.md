# L2 · narrative_money — narrative trajectory × money flow (orchestration)

> Called by L1s. Crosses the event axis's TRAJECTORY (is the story building?) with the TAPE
> (is money already following?). Neither alone is a signal: narrative without money is a story;
> money without narrative means you don't know what you're holding. Composes L3s + flow modules.

## Market separation — HARD RULE
`--scope domestic` for the KR desk, `--scope foreign` for the US desk. **Never let the KR feed
rank the US frame**: measured, the KR pool ran 787 rate-cut hits against 0 US-bank hits in a US
bank-earnings week — the KR feed's obsession is not the US market's attention. `--scope all` is
banned inside a desk run (it is a research tool, not a desk input).

## Calls — A. narrative leg
1. L3 [event_threads](../L3_functions/event_threads.md) — `thread --days 7 --scope {domestic|foreign}`.
   Select **alive market threads**: every BUILDING + REIGNITED, plus any precursor-form curve
   (starts ≤2 outlets and climbing — the measured 5-day-runway shape). FADING only if the book
   already holds exposure to it.
2. L3 [drill_detail](../L3_functions/drill_detail.md) — **direction body-read per selected thread.**
   A thread says *what grew*, never *which way it cuts* (the 27-article Hanwha Ocean thread was a
   LOSS). No thread enters the cross below on its headline alone.

## Calls — B. exposure leg (story → tickers)
3. L3 [related_companies](../L3_functions/related_companies.md) — US: `chain-hop "<thread terms>"`;
   KR: `module_industry_map "<thread terms>"`. Go **one hop past the headline names** — the names in
   the thread's own titles are the crowded layer by construction (every outlet already printed them).
4. L3 [competitors](../L3_functions/competitors.md) — fix each candidate's chain position
   (bottleneck / beneficiary / bystander).
5. Handoff — `python -X utf8 -m module_report_tags ticker <T>` per candidate: if a desk already
   covered it, inherit that verdict instead of re-searching ([handoff](../handoff.md)).

## Calls — C. money leg (same module calls indicators/money_trail own — do not re-derive)
- `python -X utf8 -m module_flow <tickers…> --bench SPY|^KS11 --json` → 🟢/🟡/🔴 per name.
  KR adds `--names` → **per-investor net-buy actuals** (⑦ foreign/institution real hands) + ⑧ short
  balance. US has no investor-type feed — substitute `python -X utf8 scripts/us_flow.py <TICKERS…>`
  (FINRA short-vol z; z≥+1.5 building pressure) + COT percentile as *context, not trigger*.

## The cross (output) — where narrative meets money
| narrative \ money | 🟢 accelerating | 🔴 dispersing |
|---|---|---|
| **BUILDING / REIGNITED** | **CONFIRMED-EARLY** → bet-stage candidate | **STORY-ONLY** → watchlist + dated re-check; do not chase |
| **FADING / ENDED** | **LATE-MONEY** → crowded chase or quiet re-rate; valuation gate before touching | **DEAD** → drop; flag any open position riding it |

🟡 rows stay uncalled — say 🟡, schedule the re-check, don't force a cell (P4).
⚠ The cell is where judgment STARTS, not where it ends: every CONFIRMED-EARLY still needs the
direction body-read (A.2) and a falsifiable forward statement from the calling L1.
⚠ Cite denominators: each thread carries its curve + the window's per-day event counts; each flow
tag carries its asof date. A card whose evidence lacks either is not eligible for the bet stage.
