# SCENARIOS — how to read and score pre-registered questions (thin spine)

> **What this is.** The numbers for every pre-registered question now live in the **`module_lens` ledger**
> (`data/lens_ledger.db`; 165 legacy `S` brackets migrated, independent check 96%). This file says how to use it, lists
> what is still open, and keeps the scoring rules. Rebuilt 2026-10-31; the 564 + 556 + 200 KB prose files are in
> [`_archive/2026-10-31/`](_archive/2026-10-31/) byte-identical (`SCENARIOS.md` = legend, master scoring log, master index).
> **When to read:** HANDOVER first check, every run; PREMORTEM before registering. **Not here:** bracket prose, branch
> tables, the master index — `show <Q>` or the archive.

## Use the ledger (run from the repo root, `python -X utf8 -m module_lens …`) — full protocol: [`pipeline/L2_modules/lens.md`](../pipeline/L2_modules/lens.md)

| When | Command | What it gives |
|---|---|---|
| HANDOVER, first | `score` then `due` | auto-settles `px:`/`pxx:`/`fred:` observables; lists every past-due question (both markets) |
| Settle a `text:` row | `resolve Q12 A --value … --scorer <desk> --link <src>` (or `AMBIGUOUS`/`VOID` with a reason) | outcome + Brier + price horizons |
| Before registering | `find "<question>" --deep` · `show Q12` | similar past questions, their outcomes, which methods hit or missed |
| Legacy ID → Q | `find S163` (legacy `S` IDs are searchable; `-KR` suffix dropped, e.g. `S173-KR` → `Q165`) | the Q ID to cite |
| Register | `ask` → `ev` (one reading per row, dead methods too) → `advise` → `think --branch … --weights …` | frozen forecast |
| Run end | `learn` · `export` (backup JSONL to `handoff/lens/`) | method credit; recovery copy |

## Open questions in the ledger — `module_lens due --today 2099-12-31`, run 2026-10-31 (cwd = DeGaJaFinance)

All 16 open ledger questions. The first 15 were already **past due on 2026-10-31** (`due` with today's date prints the same 15).
They must be resolved or marked `AMBIGUOUS` with a reason by the next HANDOVER — never silently carried.

```
Q23 2026-08-05 [text] text:T10Y2Y level with DGS2 inside 4.15-4.45 percent | Will a Fed hold flatten the yield curve enough to break the Financials mechanism?
Q26 2026-08-12 [text] text:HY OAS level and NFCI weekly direction | Will index credit stress make the three overweight carriers lose together?
Q160 2026-09-29 [text] text:EW{MPC,VLO,PSX} five-session excess versus SPY, September22 close to September29 close | Will conditional Hormuz reopening drain the refining equity premium?
Q161 2026-09-29 [text] text:EW{A,TMO,DHR} four-session excess versus SPY, September23 close to September29 close | Will life-science tools rerate into the second Section 232 tariff tier?
Q37 2026-09-30 [text] text:MU forward P/E and next-year EPS versus 8.0 and 153.74 | Will Micron rerate on an intact earnings denominator after the funded entrant's listing?
Q40 2026-09-30 [text] text:META FY capex direction; further AI structures of at least 5 billion dollars | Will lease financing weaken the meaning of hyperscaler capital expenditure guidance?
Q45 2026-09-30 [text] text:Form of chairman-tenure clause in the FSC package actually announced by September 30 | Will the FSC announce a statutory tenure clause or softer governance guidance?
Q48 2026-09-30 [text] text:Median CIEN/ANET/AVGO/MRVL RS20 vs SPY | Will incumbent optical suppliers recover after the funded entrant's listing?
Q121 2026-09-30 [text] text:Definitive Shell US chemicals agreement naming buyer and price in at least two outlet bodies by Sep30 | Will Exxon be the buyer in a definitive Shell US chemicals sale agreement?
Q150 2026-09-30 [text] text:005930/000660 foreign 20d net signs three settled sessions after tariff rate/quota announcement D0 | Will Korean memory foreign buying survive the announcement of targeted semiconductor tariffs?
Q163 2026-09-30 [text] text:EW{XLU,XLRE,XLP} one-session excess versus SPY, September29 close to September30 close | Will the duration underweight basket rebound on August PCE day?
Q165 2026-10-01 [text] text:MU Oct1/Sep30 excess vs SPY and 000660 same-date excess vs KS11; compare signs if abs MU excess>=3% | Will SK hynix match the sign of a material Micron earnings excess return?
Q164 2026-10-02 [text] text:EW{XLU,XLRE,XLP} minus XLK one-session returns, October1 close to October2 close | Will payrolls break the technology-versus-duration factor?
Q152 2026-10-09 [text] text:30d public/semi-public order value share and same-day public-procurement 90d article count by Oct9 | Will Daewoo public orders remain strong while the public-procurement narrative stays silent?
Q34 2026-10-31 [text] text:Primary-source CXMT 12-inch wafer capacity per month: 300k baseline, 350k company year-end target | Will a primary source confirm CXMT capacity at 350000 wafers per month?
Q156 2026-11-16 [text] text:DART 3Q CFS contract-asset growth versus revenue growth and stand-alone third-quarter OCF sign | Will Hyundai Engineering turn contract assets into cash in the third quarter?
```

## ⚠ Open brackets that are NOT in the ledger (archive only — migration gap found 2026-10-31)

The migration carried `S` brackets only. MACRO propositions `P###` (US) and `M-###` (KR), and KR brackets whose
number collides with a US one (`S46-KR`…`S68-KR` range), stayed in the prose. From the last settle queue
(2026-09-28 `industry_kr`, A=`SCENARIOS.md` L3886–L3888), these were still open and have no Q ID:

| ID | Mkt | Settle | Observable (shortened) | Archive |
|---|---|---|---|---|
| `M-152` | KR` | 09-28 close | KRX reopen gap test after three US sessions (holiday) | SCENARIOS.md L3875 |
| `M-149 · M-150` | KR` | 09-29 close | 5 settled sessions; M-150 VOID if KIS still dead | SCENARIOS.md L3598 |
| `M-151` | KR` | 09-29 close | s1 of 3; s1 −1.39pp, B-direction | SCENARIOS_KR.md L2286 |
| `M-134` | KR` | 09-30 close (rule ④) | 수혜6 vs 반도체2 median rs20 spread ±5pp · KRW 1,400 anti-signal | SCENARIOS.md L3473 |
| `M-148` | KR` | re-score at first KIS-alive run | 삼성전자 5-session institution sum · 금융투자 share · foreign sum | SCENARIOS.md L3533 |
| `S54-KR` | KR` | 09-30 | C10 — is KR renewables oil-linked? settle on an unconfounded session | SCENARIOS.md L119 |
| `S60-KR` | KR` | 10-12 | grid MOU → order disclosure within 60 days? | SCENARIOS.md L611 |
| `S49-KR` | KR` | 10-30 | 롯데렌탈 control transfer on the issuer's re-disclosure deadline | SCENARIOS.md L203 |
| `S53-KR` | KR` | 10-31 | FSC package: does a statutory 3rd-term ban make the final text? (content leg of S11) | SCENARIOS.md L118 |
| `S59-KR` | KR` | 11-04 | S55-KR re-registration (band ±200k sh), tariff effective D-30 | SCENARIOS.md L496 |
| `P173` | US` | 09-28 close | EW{XLU,XLRE,XLP} 3s excess vs SPY 09-23→09-28; A ≤ −1.852pp / B ≥ +1.619pp | SCENARIOS.md L3723 |
| `P171` | US` | 09-29 close | CCL 1d residual vs EW{RCL,NCLH,VIK}; A ≥ +1.04 / B ≤ −1.40 | SCENARIOS.md L3642 |
| `P174` | US` | 10-01 close | CLX26 5s % from 94.61; A ≤ −3.317% (deal priced) / B ≥ +5.486% | SCENARIOS.md L3764 |
| `P175` | US` | 10-02 close | ^TNX bp change from 5.184; A ≥ +10.6bp / B ≤ −7.1bp | SCENARIOS.md L3810 |
| `EVENT_ALPHA card 5` | KR` | 09-28 close | 010950·096770 reaction to settled Brent | SCENARIOS.md L3886 |

Until these are migrated (a human/K-branch decision — this file does not write the ledger), score them **in the archive**
prose and say so in the run's HANDOVER. `S8` (US, undated `[blank]`) is in the ledger as Q8.

## Scoring rules (the ones that survive into the ledger era)

- **Legend** (A=`SCENARIOS.md` L1): `ARMED` pending · `FIRED-A/B/C` branch that occurred · `EXPIRED` date passed unscored
  (a process failure — log it) · `VOID` premise invalidated before the event. Ledger equivalents: `resolve <k>` / `AMBIGUOUS` / `VOID`.
- **Score at the next HANDOVER after the event date, whether or not anyone remembers** (L123). An unscored question is how a
  desk keeps its wins and forgets its losses. Every past-due row, **including the other market's**, is this run's job.
- **Observable not yet formed ≠ EXPIRED** (D682, 2026-09-28): a "day-X close" row met by a day-X pre-open run is carried
  as "not yet formed" to the next run — never back-filled, never called expired.
- **Freeze before the event**: observable, thresholds and branches are fixed at registration; never rewrite them after
  seeing the event (`think` is rejected on/after the settle date). A price reaction is **not** part of an observable —
  keep implied-move bands in a separate, labelled reaction test (D28, S7).
- **Both branches, a date, an information grade** (lens L3): say before the event which branch would change the view.
  Thresholds from measured dispersion / implied move (`module_flow --positioning`), not round numbers (D497-KR).
- **One observation seen three times is one** (U6, date-clustering): e.g. `S171`-A, `S172`-B, `P175`-B were one rate
  observation. **Do not register a second row on an observable/date an open question already covers** — reuse its Q (D343).
- **Reachability-check anti-signals at write time** (D272-KR): an anti-signal naming an observable that does not exist is a
  construction defect. Record it; never tighten the threshold afterwards (D496-KR).
- **Price reaction is separate from whether the observable fired** (lens.md §5) — score the observable, report the price as context.

## Change log
- 2026-10-31 — rebuilt as a ledger guide by orchestra branch K3; prose moved to `_archive/2026-10-31/` (byte-identical).
