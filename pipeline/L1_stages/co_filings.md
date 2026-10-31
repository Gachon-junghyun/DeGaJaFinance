# L1 · CO_FILINGS — earnings, margins, guidance and estimates, read from the filing itself

> Company stage 2 (all modes). Merges the old FORENSIC_PACK, PRIMARY_SOURCE, estimate_revision and
> filing_diff. This is the stage the desk kept skipping: it must end with the **operating numbers read
> from the original document**, not with a flow table.
> **Reads (primary sources)**: DART/EDGAR filings (periodic report, earnings release / 8-K ex 99.1,
> 주요사항), company IR deck, the consensus **trend** page. **Writes**: `DATAPACK.md` (cap **20 KB**) +
> `SOURCES.md` (URL + access time per source, cap **8 KB**).
> **Next stages use**: the segment table (CO_STRUCTURE's denominator), margin and guidance lines
> (CO_VALUE's earnings input), the revision table (CO_VALUE's trust weight), dated catalysts (CO_VERDICT).

## Belief
Nothing enters the report that is not in ① this pack or ② a primary document with its id (rcept_no /
accession). A WebSearch figure is tagged `[WebSearch]` and never the spine of a decision. **미확보 is a
finding.** 🔴 **A summary is not "read".** Search summaries and list APIs keep table values and drop
sentence-level constraints and time series — and what remains looks complete. Grade every source
`직접 봄 / 원문 봄 / 요약만 봄 / 확인 못 함`.
Measured weight (module_lens first learning, 2026-10-31): filings/earnings/guidance evidence was right
**6 of 8 (0.70)**; flow **5 of 32 (0.18)**. Word impact: 영업이익 1.62× · FY 2.56× · GUIDANCE 1.64× day move.

## 1. Deterministic pack (calls L2 [deepdive](../L2_modules/deepdive.md))
Valuation snapshot + consensus target/rating · business text · `module_disclosure --days 120` digest ·
financials (`module_fundamentals_kr <code>` / `module_fundamentals_us <T> --json`, incl. estimate momentum) ·
`module_chart --read` (read the full grid, not the tail) · news velocity `module_news_data fts search "<한글명>" --days 30`.
**Segment P&L** — L3 [segment_pnl](../L3_functions/segment_pnl.md): share of level **and of the swing** +
the Basis-of-Presentation scope line (`none` is an answer). US: the table lives in the **earnings 8-K
exhibit 99.1**, not in the 10-K prose `module_business_us` returns.

| ticker format (violate → 0 data) | KR | US |
|---|---|---|
| KIS · valuation · disclosure · business | 6-digit `009150` | — |
| yfinance / chart / flow | `009150.KS` / `.KQ` | plain `PSX` |
| news_fts | **한글 종목명** (ticker → 0 hits) | name **and** ticker, `--scope foreign` |
| EDGAR | — | plain ticker → CIK via cache |

🔴 **KR half-year/quarter — the pack is silently wrong** (measured 2026-08-28, 034020). DART income
statements carry a 3-month column (`thstrm_amount`) and a cumulative one (`thstrm_add_amount`); the
cash-flow statement is **cumulative only**. `module_fundamentals_kr` reads the 3-month column
(`_dart_fin.py:173,192`), so OCF/operating profit, receivables/sales, 미청구/sales come out with
mismatched periods: 034020 H1 reported **−2.82**, true **−1.62** (revenue 4.72조 Q2-only vs 8.99조 cumulative;
OP 3,143억 vs 5,478억). No exception, a plausible number. ⇒ read `thstrm_add_amount` directly and write «누계 기준». Annual reports are unaffected.

**Data gaps — state them, do not lean on them.** KR: no single-stock options · insider **price 미상**
(direction/qty only) · procurement needs `DATA_GO_KR_KEY`. US: no per-investor flow; ⚠ `module_disclosure_us`
lists Form 4/144 **without parsing** — measured PSX 2026-08-21: 6 Form 4 in 60d, 5 with code `S`, 9 Form 144
of which 1 parsed. Report direction as observed and size as 미측정.

## 2. Primary sources the pack structurally lacks
| axis | why the pack lacks it | KR destination | US |
|---|---|---|---|
| **consensus trend** (1w/1m/3m/**1y**) + earnings surprise | DART/KIS give only "what it earns now" | `navercomp.wisereport.co.kr/v2/company/c1050001.aspx?cmp_cd={6}` — no login; `innerText` gives the tables (⚠ `c1040001` is financials, **`c1050001` is consensus**; Naver's 종목분석 tab only iframes this — go direct) | paid-terminal axis → 미확보; accumulate own snapshots (`snapshot_estimates.py`) |
| **segment orders · backlog · annual plan / guidance** | the periodic report has segment revenue, not segment OP/backlog/plan | company IR deck PDF (`curl -sL -o x.pdf`) | 8-K ex 99.1 + call transcript; backlog is company-specific |
| **filing sentences** (dated catalysts, constraints) | list APIs give title + amount only | DART `dsaf001/main.do` → 🔴 **frameset shell**: pull the iframe `report/viewer.do?rcpNo=..&dcmNo=..` | 8-K says "filed as 10-Q exhibit" ⇒ the contract text is in that 10-Q's `index.json` (NVDA `…ex101.htm` 43,964 chars, one line nowhere in the list) |

Browser: `module_webctl` (CDP 9222). ⚠ **Traps measured** (2026-08-28 / 09-03):
1. 🔴 Tabs are matched by **title/URL substring, not id** — open the tab **with the destination URL**
   (`newtab <URL>` → wait → `text --match <domain>`); `--match` before the tab exists dies `CDPError: 매칭 타깃 없음`.
2. 🔴 `dsaf001` `innerText` is TOC + buttons → misread as "empty body".
3. 🔴 IR PDFs do not open in `Read` (no `pdftoppm`) — extract with **PyMuPDF (`fitz`)**.
4. ⚠ IR decks put labels in shapes; leading characters get clipped («대형원전»→«형원전»). Trust the numbers, re-check sentences.
5. Retreat: captcha / 429 / login wall ⇒ stop hitting that source today; official API or 미확보. A locked account costs more than a blank.
6. EDGAR: never scrape directory HTML (nav only) — use `index.json`, `data.sec.gov/submissions/CIK{10}.json`,
   `efts.sec.gov/LATEST/search-index?q=...` (no key; phrase presence across a filer in seconds).
   Register new sites and dead ends in `module_webctl/site_map.json` (`developer.nvidia.com/cuda-zone` = dead end, no counts).

🚨 **Counterparties named in the filing → look up their filings now** (measured 2026-09-03 NVDA): the 8-K
named CoreWeave/Oracle/Nebius…; CoreWeave's 10-Q held a **$2.0bn NVIDIA private placement at $87.20** and
«all of the GPUs … are NVIDIA GPUs» — absent from every NVDA filing. The other half of the story is in the
counterparty's filing (name → CIK → `efts` search for the subject's name).

## 3. Read the numbers as a time series
- **Revision table** `metric · 1y · 3m · 1m · 1w · now · Δ%` + the stock return **over the same window**.
  Measured 034020: 2026 OP consensus **−21%**, EPS **−38%** in a year while the stock rose **+36.1%** —
  the multiple, not earnings, lifted it; invisible from the current level. Past miss of actual vs 3-month-prior
  estimate: 2024 **−19.7%**, 2025 **−20.4%** ⇒ default to the same haircut on forward years.
  Print the **opposite signal** too (034020: two straight quarterly beats +20.3%/+19.5% = inflection candidate).
  Guards: a cut ≠ sell; check scope is the same a year ago (split/merger/consolidation breaks the comparison).
- **Margin and guidance lines** — segment margin, last 4–8 quarters, and the company's own guidance
  sentence quoted with its document id. Long-run gross margin: `scripts/margin_history.py <ticker>`.
- **Language diff** (Lazy Prices) — diff «사업의 내용 / 위험» (US: Item 1/1A) against the prior same-form
  filing: added / deleted sentences + jaccard, tagged `[best-effort]` (no dedicated module). One filing only ⇒
  `미확보 — 직전 대비 불가`, never a fake diff. Added lines = where management moves the narrative; deleted = quiet retreat.

## ✅ EXIT CHECK
- [ ] `DATAPACK.md`: every axis has a status (ok/미확보); segment P&L with share of swing + scope line; consensus target/rating.
- [ ] Revision table with the 1-year column and same-window price return (current level only ⇒ **incomplete**).
- [ ] Guidance/backlog/annual plan extracted from IR or release text (`none` is an answer); KR H1/Q figures on the cumulative column.
- [ ] Every filing with an irreversible procedure or catalyst read in its **viewer body**; otherwise graded «요약만 봄».
- [ ] `SOURCES.md` lists URL + access time + grade per source; failures listed as 미확보 with the reason.
- [ ] Named counterparties checked in their own filings, or `없음`.
