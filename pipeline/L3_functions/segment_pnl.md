# L3 · segment_pnl — one company → segment-level P&L and each segment's share of the swing

> **Single-role unit.** Independent — no ordering; an L2/L1 calls it when needed. Does ONE thing:
> break a company's latest quarter into **segment pre-tax income**, and state each segment's share of
> (a) the level, (b) the QoQ swing, (c) the YoY swing. It does not interpret. It supplies the
> denominator that every single-driver thesis silently assumes is 100%.

## Why this exists (measured 2026-08-21, PSX)
The desk modeled Phillips 66 entirely off the 3-2-1 crack spread, because every available one-line
description — `yfinance longBusinessSummary`, the sector label `Oil & Gas Refining & Marketing`, the
news pool — says **refiner**. The segment table says otherwise:

| segment | 2Q26 pre-tax $M | share of level | share of QoQ swing |
|---|---:|---:|---:|
| Refining | 3,062 | **61.6%** | **60.6%** |
| Marketing & Specialties | 583 | 11.7% | 15.8% |
| Midstream | 785 | 15.8% | 4.1% |
| Renewable Fuels | 544 | 10.9% | 12.4% |
| Chemicals (CPChem 50% JV) | 404 | 8.1% | 6.2% |
| Corporate | (407) | — | — |

⇒ the crack model was right about **~61%** of the company and silent about the rest — and the rest is
driven by things that do not move with a crack at all: **regulatory credits** (Renewable Fuels' swing
was reported as *"higher regulatory credits from higher pricing"* — a policy variable), **mark-to-market**
(M&S and Chemicals, a timing item the release names explicitly), and **NGL/LPG volumes** (Midstream).
**A single-driver model of a multi-segment company is wrong by the share of the segments it ignores.**

## Where the numbers come from (NOT the 10-K)
| market | source | why not the obvious one |
|---|---|---|
| **US** | the **earnings 8-K exhibit 99.1** (`module_disclosure_us <T> --days 120` → the `Item 2.02` row → fetch the `ex99` attachment from that accession's index) | the 10-K is annual and qualitative; `module_business_us` returns Item 1/1A/7 **prose**, which names the segments but carries no segment P&L |
| **KR** | DART 사업보고서 **부문별 정보** (`module_disclosure <code> --business-report`, section 재무제표 주석) | the 사업의 내용 section gives 매출 분해, not segment 이익 |

⚠ **`module_disclosure_us` categorizes the 8-K but does not fetch its exhibit.** Today that last hop is
manual (fetch the accession index, pick the `ex99` file). Wiring it is registered as an open item in the
protocol header — do not pretend the categorizer gave you the table.

## ⚠ Read the Basis of Presentation before any YoY
Consolidation scope changes are invisible in the number and fatal to the comparison. Measured on the
same run: PSX revenue printed **+53% YoY**, and the release's Basis of Presentation says *"beginning
October 1, 2025, includes 100% of Borger Refinery and Wood River Refinery consolidated due to the
acquisition of the remaining 50% of WRB"* — i.e. a chunk of that growth is an **equity-method →
full-consolidation switch**, not demand. The desk had already written "+53% yoy 매출" as growth.
**Any YoY quoted from this unit carries the scope note or it is not quoted.**

## Output (a table, no verdict — P4)
`segment · latest · prior-Q · year-ago · share of level · share of QoQ swing · share of YoY swing ·
[the release's own stated cause, quoted]` + a scope-change line (`none` is an answer) + `asof` filing date.
Segments the source does not report separately stay blank; **do not allocate corporate overhead by guess.**
