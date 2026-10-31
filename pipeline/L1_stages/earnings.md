# L1 · EARNINGS — operating profit, margin, guidance and estimates, read from the filing (stage)

> Big stage, shared by industry_us and industry_kr (`--market us|kr`). Runs right after MACRO
> (US: after PREMORTEM), before COMPETITION. Calls L2.
> **Reads (primary sources)**: DART periodic reports and 잠정실적/주요사항 공시 · EDGAR 10-Q/10-K and the
> earnings 8-K exhibit 99.1 · company IR deck/release · consensus trend page. WebSearch summaries are
> **not** a source for a number here (P6 grade «summary only»).
> **Output**: `EARNINGS.md` (one file, per focus-sector sections) — **cap 24 KB**.
> **Next stages use**: COMPETITION takes the segment table and margin lines as its denominator; FLOW_CHECK
> takes the candidate set; BET takes §1–§3 per name as its «why» column and the lens `filing`/`estimates` rows.

## Why this stage exists (measured 2026-10-31)
Across six completed runs operating income was asked **0 times** in KR and twice in US; guidance was a WebSearch
summary or absent; customers and orders rode as `unknown` for three runs. Yet the lens ledger scored filings/
guidance evidence **6 of 8** vs flow **5 of 32**, and earnings words move the day most (영업이익 1.62× · FY 2.56× ·
GUIDANCE 1.64×; `lab/NEWS3D_20261030.md` E2). This stage is not optional and is not a table of yfinance ratios.

## L2 called
- [web_errand](../L2_modules/web_errand.md) — any number the modules do not return (8-K exhibit, IR PDF,
  consensus trend page, DART viewer body). `module_webctl find <topic>` first; `access=api` means a module owns it.
- [lens](../L2_modules/lens.md) — `find "<name> guidance"` before digging (reuse a method that scored well).
- L3 [segment_pnl](../L3_functions/segment_pnl.md) — segment revenue **and** segment operating profit with the
  basis-of-presentation line. A consolidation-scope change is invisible in the number and fatal to a YoY.

## What this stage does

### 1. Candidate set — earnings first, flow is one source among six
Build the per-sector list from, in this order, and tag each name with its source:
(a) names held in the book · (b) lens/reject/missed rows that came due in HANDOVER · (c) MACRO's focus sectors'
players (`python -X utf8 -m module_industry_map "<sector thesis terms>"`; large caps ∪ thematic names with
mcap ≥ ~$2B / ₩1조) · (d) **names in those sectors that printed earnings, pre-announced, or filed a guidance
change in the last 10 sessions** (`catalyst_calendar` + `module_disclosure <6자리> --category earnings` /
`module_disclosure_us <TKR> --days 30` 8-K list) · (e) company scoreboard rows (`REPORT/COMPANY_SCOREBOARD.md`) ·
(f) the **previous** run's FLOW_CHECK shortlist names (tagged `flow`). This run's FLOW_CHECK runs after this stage,
so its new names are handed to the **next run's** EARNINGS as candidates — never carried into this run's BET without
the four numbers.
⚠ A name may not enter on a news co-mention alone — it needs a filing, a customer/supplier link in a filing, or
a print. (Old DEEP rule asked for a *flow* cross-check here; that made flow the entrance. Removed 2026-10-31.)

### 2. Per name — the four numbers, from the filing
| field | US source | KR source | rule |
|---|---|---|---|
| **operating income and operating margin, last 4–8 quarters** | 8-K ex 99.1 / 10-Q income statement (`module_disclosure_us <TKR>` → filing URL → web_errand) | `python -X utf8 scripts/margin_history.py <6자리> --json` (annual `operating_margin_pct`) + `module_fundamentals_kr <6자리> --period q1\|half\|q3 --json` for quarters | KR H1/Q from DART: read the **cumulative column** (`thstrm_add_amount`) and difference it; the 3-month column next to a cumulative cash-flow statement mis-periods every ratio (measured 034020: OCF/OP reported −2.82, actual −1.62) |
| **gross margin percentile in the name's own history** | `python -X utf8 scripts/margin_history.py <TKR>` | same, 6-digit | undefined (not broken) for financials and cost-by-nature filers — say «undefined», never a blank that reads as a pass |
| **guidance: this print vs the prior guide** | release / call text via web_errand | 잠정실적 공시 · IR deck · annual plan | quote both guides and the date of each; `none issued` is an answer; a WebSearch paraphrase is not |
| **MACRO §2 exposure number** (each proposition naming this company's sector) | 10-K/10-Q notes: rate sensitivity, FX exposure, fuel/input cost share, floating-rate debt | 사업보고서 주석: 금리·환율 민감도, 원가 구성, 변동금리 차입, PF 보증 (`module_disclosure <6자리> --guarantees`) | quote the number with filing and page/section; `not disclosed (looked: <where>)` is allowed, an unasked one is not — this is where MACRO's transmission reaches a company |
| **estimate trend** | `module_fundamentals_us <TKR> --json` §추정치 모멘텀 (7/30/60/90d + up:down) | consensus trend `navercomp.wisereport.co.kr/v2/company/c1050001.aspx?cmp_cd=<6자리>` (1w/1m/3m/1y) via web_errand | describes the denominator's **direction**; never a leading indicator, and no independent weight on an IT name (measured: the effect was an IT loading, ex-IT Q5−Q1 −1.1pp) |

- ⚠ Cite both halves of every print (rule C2): YoY and sequential on a like-for-like window.
- ⚠ «Cheap on forward multiple» needs both legs on the same line: margin percentile **and** estimate direction.
  KR estimate history now has a source (the trend page above); if it was not reached, tag
  `[revision leg: not read]` and say what was tried.
- ⚠ A cyclical at peak margin prints its lowest forward multiple (lens L2). Measured: MU forward P/E 6.31× at
  gross margin 84.6% vs a prior-cycle peak of 59%.

### 3. Events that change earnings (absorbed from EVENT_ALPHA)
Read the week's event threads only for what moves the four numbers above: orders/contracts, price changes,
capacity, customer capex, regulation with a dated effect. `python -X utf8 -m module_news_data thread --days 7
--scope {domestic|foreign}` (KR=domestic, US=foreign; `all` is banned in a desk run). For each kept thread:
body-read the direction (the biggest measured thread was a LOSS its headline never said), name the exposed
names one hop past the headline, and write both branches with a dated check on an **earnings observable**
(guide, order, price, margin), not on the tape. Count the threads not kept (no silent cap).

### 4. Hand-down
Per name: source tag · OP margin series · GM percentile · guide vs prior guide · estimate direction · dated next
print. Per sector: one line on whether earnings are accelerating, flat or rolling over, with the names behind it.

## ✅ EXIT CHECK
- [ ] Candidate set written with a source tag per name; flow-sourced names are ≤ half of any sector's list, or
      the file says why.
- [ ] **Every name carried to BET has an operating-margin series of ≥4 periods from a filing**, or the line says
      what was tried (module, URL, viewer) and why it failed. `unknown` with no attempt fails this check.
- [ ] **Guidance compared to the prior guide from a primary source** (release, call, 공시, IR) with both dates,
      or `none issued`. No WebSearch-summary guidance is cited as read.
- [ ] **Every MACRO §2 exposure number aimed at a carried name is answered** (number + filing section, or
      `not disclosed (looked: …)`); MACRO_REPORT §2 proposition IDs cited.
- [ ] Estimate direction stated with its source and as-of; KR names carry the trend page reading or the
      `[revision leg: not read]` tag.
- [ ] Every «cheap» claim carries margin percentile + estimate direction on the same line.
- [ ] Event threads: kept ones body-read, both branches on an earnings observable with a date; dropped count given.
- [ ] `EARNINGS.md` ≤ 24 KB; nothing restated from MACRO_REPORT (cite it).
- [ ] Linter run: `python -X utf8 scripts/report_lint.py <file>`; findings fixed or exempted with rule ID.
