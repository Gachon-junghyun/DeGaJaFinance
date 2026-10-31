# PROTOCOL — industry_kr

> A protocol = an ordered composition of L1 blocks (references only). **Order is owned by this file**.
> Shares the **same L1s** as industry_us — only the composition and runtime deltas differ.
> Purpose: same spine — financial environment → earnings from DART → industry structure → flow as confirmation →
> lens → handover. Output root `llm_outputs/{YYYY-MM-DD}/industry_KR/` (same file-output rules as industry_us:
> `kr_live_shortlist` reads `SECTOR_FLOW_KR.json` there; previous folders read-only; load-bearing names
> `MACRO_REPORT.md` · `SECTOR_FLOW_KR.json` · `KR_LIVE_SHORTLIST.json` · `SECTOR_DEEP_{code}.md` · `BET_SHEET.md`).
> Runtime = `--market kr`.

## Before stage 1 — run protocol `preflight` (`--market kr`); HANDOVER copies its permission table.

## Composition (L1 order)

| # | L1 block | Output (cap) |
|---|---|---|
| 1 | [HANDOVER](../L1_stages/handover.md) | `HANDOVER.md` (8 KB) |
| 2 | [MACRO](../L1_stages/macro.md) | `MACRO_REPORT.md` (14 KB) |
| 3 | [EARNINGS](../L1_stages/earnings.md) | `EARNINGS.md` (24 KB) |
| 4 | [COMPETITION](../L1_stages/competition.md) | `SECTOR_DEEP_{code}.md` **×2** (12 KB each) |
| 5 | [FLOW_CHECK](../L1_stages/flow_check.md) | `SECTOR_FLOW_KR.json` · `KR_LIVE_SHORTLIST.json` · `FLOW_CHECK.md` (4 KB) |
| 6 | [BET](../L1_stages/bet.md) | `BET_SHEET.md` (16 KB) + lens Q IDs |
| 7 | [ALPHA](../L1_stages/alpha.md) | `BET_SHEET §B` tags |
| — | HANDOVER §6 close-out | write-back · `module_lens export` · coverage ledger |

## FOCUS budget — **N = 2** (1 continuous + 1 rotating)
MACRO reads this line (the L1 owns the rule, this protocol owns N; `industry_us` keeps 4). Cut from 4 to 2 on
2026-07-31, on measurement: the 07-31 run spent ~710k sub-agent tokens on sector theses that cannot be verified at
the rate they are produced (selection yields ~10–20 independent observations a year, C4); that week's +16.86pp lead
was ~14pp cash weight and +2.54pp selection carried by one name. Coverage that shrinks must shrink **visibly**:
MACRO names the unslotted OW sectors in `DEEP_LOG`. (The «retention, not discovery» leak ordering once cited here
was withdrawn 2026-07-31 — it inverted on a longer horizon; do not re-argue the guard with a single-window mean.)
⚠ The 2026-10-31 rebuild moves effort inside each focus sector from flow tables to filings; it does not raise N.

## KR runtime deltas (vs industry_us)
- **No PREMORTEM**; drift in HANDOVER close-out only when a binary ≤48h was open. No CYCLE_EXPOSURE / ACTION_TICKETS.
- MACRO: no FRED module for KR → cross-read the same-day US `MACRO_REPORT.md §1` cited `[FRED via US desk]`; add KRW,
  KTB and `module_KIS --futboard` basis/OI (context). Transmission lines name KR exposures: exporters' USD revenue
  share, banks' NIM sensitivity, refiners/airlines' fuel cost share, builders' PF guarantees
  (`module_disclosure <6자리> --guarantees`).
- News `--scope domestic` + `news_fts --kr` (trigram: 2-char Korean terms return 0 — not absence; use 3+ chars).
  Universe `kr_all` (KRX sectors).
- **Earnings legs for a «cheap» claim** (D70/D120): (i) margin in its own history — `scripts/margin_history.py
  <6자리>` (DART; 11/11 fiscal years on 042700 and 005930; undefined for financials and cost-by-nature filers —
  105560 · 086790 · 035420 measured), annual `operating_margin_pct` from `--json`; (ii) estimate direction — the
  consensus trend page `navercomp.wisereport.co.kr/v2/company/c1050001.aspx?cmp_cd=<6자리>` (1w/1m/3m/1y) via
  `web_errand`. ⚠ Naver's 목표주가 상승여력 is someone else's price estimate, not the denominator's direction.
  If (ii) was not reached, tag `[revision leg: not read]` with what was tried. (Before 2026-10-31 this delta said
  «KR value claims are half-powered by construction; momentum and flow carry the rest». Retired: the trend page
  exists, and flow scored 5/32 in the lens ledger.)
- ⚠ KR H1/Q figures from DART: read the cumulative column and difference it (034020: OCF/OP reported −2.82, actual
  −1.62; revenue 4.72조 reported, 8.99조 actual).
- **KIS investor actuals** (foreign/institution net-buy) are graded **B** in the D6 table (L2 indicators — a confirmation
  layer, never a standalone system; foreign flow is non-stationary), and they stay a **confirmation**: FLOW_CHECK writes them as agree/disagree, BET may cap them inside the flow
  weight, and a KIS outage removes a confirmation line — it does not stop the desk from concluding on earnings and
  competition. (Measured: with KIS dead, three consecutive runs wrote «cannot confirm any new name» and produced
  nothing — K1 §2-4. And M224 graded all four sweep axes inside the noise band: ρ −0.21~+0.19, n=22, threshold 0.43.)

**Start → protocol `preflight`, then HANDOVER, and execute in order.** Pass each EXIT CHECK; finish with HANDOVER
§6 close-out.
