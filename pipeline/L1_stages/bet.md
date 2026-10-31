# L1 · BET — the bet sheet: one conclusion per name, with its evidence weighed (stage)

> Big stage. Turns EARNINGS + COMPETITION (+ MACRO transmission, + FLOW_CHECK agreement) into one file.
> **Reads**: upstream files only (cite, never re-print), `REPORT/COMPANY_SCOREBOARD.md`, the decision ledgers.
> **Output**: `BET_SHEET.md` — one file, per-sector sections §A–§E (filename load-bearing; paper_desk ·
> wrap_account · 미러링 read it) — **cap 16 KB**. Every conclusion is also registered in the lens ledger.
> **Next stages use**: ALPHA takes §B per name and the Q IDs; HANDOVER close-out takes theses and retractions.

## L2 called
- [lens](../L2_modules/lens.md) — `find → ask → ev → advise → think --weights` per conclusion (below).
- `module_valuation <6자리> --peers …` (KR) · `module_fundamentals_us <TKR> --json` (US) · `module_math_check` on
  every derived figure — called directly.

## ★ Scoreboard confirmation gate — before re-deriving a name
If `REPORT/COMPANY_SCOREBOARD.md` has a row (protocol `company`, mode `research`), **confirm by citation and write
only the delta**, unless a test fails:
| test | fails when | then |
|---|---|---|
| age | row older than 10 settled sessions | re-dig |
| observation point | a dated observation point matured | grade it first — the grading is the delta |
| event | an earnings print / 8-K / 주요사항 landed after the row | re-dig |
| driver band | the roll-adjusted driver percentile crossed a band | re-dig that driver only |
| thesis | this run's EARNINGS or COMPETITION evidence contradicts the row's thesis | re-dig; a flow-only disagreement is stated, not acted on |
A score is research quality, not a promotion; a high-scoring `PASS` is a success. `axes_measured < 4` ⇒ not
rank-comparable. No row ≠ no coverage — check `module_report_tags ticker <T>` and the batch skip list.

## What this stage does — per focus sector, per candidate
- **§A numbers** — multiples, growth, **operating margin series and guide (from EARNINGS)**; XBRL↔yfinance cross-check;
  blanks are blanks.
- **§B thesis** — one sentence: what earnings will do and why (competition, transmission); ALPHA adds freshness.
- **§C flow** — FLOW_CHECK's one line, cited (agrees / disagrees / not measurable).
- **§D competition** — the name's row from COMPETITION: share or rank, price action, capacity, customers. Required.
- **§E refutation + dated catalyst** — the strongest bear case and the observable that would prove it.
- If a cycle GAP was flagged, an epicenter-starter note exists regardless of tape; tape gates only the remainder.
- Sizing language is illustration only and must match HANDOVER's exposure state; if the state is `복귀` and the
  sheet cannot supply enough names, say so plainly.

### The conclusion rule
A conclusion (include / set aside / re-file) **must stand on at least one fundamental kind** — `filing`, `estimates`,
`macro` (transmission to this company's P&L) or competition (COMPETITION's table, registered as `filing`/`report`) —
and say which. `price` (RS, trend, setup), flow and positioning are **confirmation lines only**: a sentence whose only
«because» is the tape (price and/or flow) is not a conclusion; rewrite it or drop it. (Measured why: lens ledger
filings 6 of 8, price 39 of 90 = 0.43, flow 5 of 32.)

### Register it in the lens ledger — evidence by kind, with weights
For each included or set-aside name (and each sector verdict that changed):
1. `module_lens find "<name/sector question>"` — reuse an open question on the same observable and date.
2. `ask "<question>" --subject <TKR> --market US|KR --desk industry_US|industry_KR --settle <date> --observable
   "<earnings observable first: text:FY guide · fred:… · pxx:<TKR>:20>"`.
3. One `ev` row per reading with its true `--kind` (`filing` · `estimates` · `macro` · `report` · `price` · `flow` ·
   `positioning` · `news`), source link and as-of; dead methods as `--dead` rows with weight 0.
4. `advise --item "kind:key:method:branch" …` — the ledger's recommended weights from impact × learned credit
   (equal weights when history is thin). **Read the credit line per kind before choosing.**
5. `think <QID> --branch … --weights e…=…` with the **actual** weights (sum 100). Cap: `flow` + `positioning`
   together ≤ 30% — `think` rejects more (human decision 2026-10-31; ledger: flow 5/32 right vs filings 6/8). Same cap as `company`.
6. Put the Q ID and the weight split by kind on the name's §B line, e.g. `Q41 · filing 45 · estimates 25 · macro 15 · flow 15`.
Exit 2 from the CLI is a failed registration: keep the reason in the file and fix the input; never backdate.

### Setting aside, re-filing, missing — every name leaves a scored record
- Set aside ⇒ L3 [reject_ledger](../L3_functions/reject_ledger.md):
  `python -X utf8 scripts/reject_ledger.py add --date <d> --ticker <T> --name <n> --cls <class> --why "<one line>"
  --stage BET --revives-if "<condition>" --recheck-date <YYYY-MM-DD>` (both fields script-enforced). Measured: 67%
  of rejections changed nothing and the loss tail ran 2.2× the gain tail, almost all from two rejections filed
  without a revival condition.
- **Removal needs a measured fundamental reason** — earnings, guidance, competition or transmission; a broken price
  structure may set the timing or stop, never the removal by itself. A story
  going quiet is not one: re-file with a new thesis line and a dated re-check. Flow still arriving is **written into
  `--revives-if`** (e.g. «foreign+institution 5-session net-buy ≥ 3/5»), not used as a veto. (Origin: 475150 was
  removed twice on «theme faded» narrative, costing +41.2pp and +26.9pp; the fix is a measured removal reason and
  a revival condition, not a flow veto.)
- Surfaced upstream but never reached ⇒ L3 missed_ledger: `python -X utf8 scripts/missed_ledger.py add --date <d> --ticker <T>
  --name <n> --cls <class> --why "<one line>" --stage BET --enters-if "<condition>" --recheck-date <YYYY-MM-DD>`
  (`P.현금부족` for exposure-blocked names). The script refuses a ticker×date already rejected.

## ✅ EXIT CHECK
- [ ] Scoreboard consulted; each row-holder CONFIRMED (cited) or RE-DUG with the failing test named; matured
      observation points graded.
- [ ] Every focus sector has a section; every candidate has §A–§E; **§D competition and the §A operating-margin
      line are present for every included name** (or the EARNINGS/COMPETITION attempt is cited).
- [ ] No conclusion rests on flow/positioning alone; each names its non-flow kind.
- [ ] **Every included or set-aside name has a lens Q ID with weights by kind summing to 100**, `advise` was read,
      and flow+positioning ≤ 30% (`think` enforces it).
- [ ] Every set-aside name is in `reject_ledger` with class + `--revives-if` + recheck date; every surfaced-but-
      unreached name is in `missed_ledger`; a multi-name run with zero of both says why.
- [ ] Sizing language matches the exposure state; numbers math-checked; `BET_SHEET.md` is ONE file ≤ 16 KB.
- [ ] Linter run: `python -X utf8 scripts/report_lint.py <file>`.
