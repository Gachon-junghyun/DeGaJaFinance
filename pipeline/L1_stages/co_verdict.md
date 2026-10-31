# L1 · CO_VERDICT — one verdict, its gates, its ledger row, and its weights in module_lens

> Company stage 8 (all modes). Merges the old BET_VERDICT (research/report) and VERDICT (forensic).
> **Reads**: upstream files only. **Writes**: `COMPANY_VERDICT.md` (cap **6 KB**) + `verdict.json`; ledger row;
> lens question + evidence + weights. **Next uses**: CO_CARRY of the next run grades the observation points;
> `company_batch` scores `verdict.json`; `industry_*` BET confirms the `thesis` line; PUBLISH_REPORT (report mode).

## The first line of the file is the delta
`평결: {previous}→{this}` (first ever ⇒ `신규→{this}`); on a transition add one sentence naming **which axis cracked or
confirmed, and when**. The axis change leads; the level is what the market already prices.

## Verdict by mode
- **research / report** — `ENTER · ADD · HOLD · TRIM · EXIT · PASS` + stop (a number) + horizon + `NEEDS_SIZE` hand-off
  (sizing is a separate, human-run SIZE stage against the live book; this protocol never sizes). report mode also writes
  the execution table (new / hold / stop / re-buy) the document will carry.
- **forensic** (참고-only, `binding:false`, READ-ONLY) — **REAL** (product and money verified, alpha_delta non-empty) ·
  **REAL-but-PRICED** (alpha_delta empty) · **INFLATED** (narrative > substance) · **BROKEN** (demand gone, earnings non-cash, capital structure cracking).

## Gates (research/report) — print each with the value that cleared or failed it
**The direction of the action is set by filings, earnings, competition and macro transmission — never by tape.**
Price and flow decide *when and how* to act (timing lines below), not *whether*.
| # | gate | rule |
|---|---|---|
| G1 | earnings direction | the action agrees with CO_FILINGS: margin trend, guidance sentence (with document id) and revision direction. ENTER/ADD against falling margins **and** cut estimates must name the filing fact that overrides them |
| G2 | competitive position | the action agrees with CO_STRUCTURE: competitor table (≥ 1 rival), pricing power, D1 covered share. A thesis resting on a segment below D1's coverage must say so |
| G3 | catalyst | a **dated** catalyst exists (from CO_FILINGS / transition signals), or value trap ⇒ PASS |
| G4 | reward/risk | `upside/|downside| ≥ 1.5` using the **own target** (CO_VALUE) and a written stop — never the broker target |
| G5 | anchoring | FALSIFY's bear case quoted verbatim before the verdict line |
| G6 | frame | D3 FAILED ⇒ the shared leg is beta, not name evidence |
| G7 | consensus exceeded | price > consensus mean target ⇒ a low forward P/E may not be called cheap unless next-year EPS direction is on the same line (PSX: $245.51 vs $221.68 target, fwd P/E 11.55, next-year EPS −15.4% = peak-year arithmetic) |
| G8 | position conflict | held in the book **and** unresolved in the reject ledger ⇒ resolve in this file first (PSX: held +21.3% while a 2026-08-02 `B.모멘텀only` rejection had not revived — FINRA z +0.98 failed its leg) |

## Timing lines (research/report) — not gates; they never flip the direction
| # | line | use |
|---|---|---|
| T1 | price vs SMA200 | below ⇒ enter in tranches and place the stop under a stated structure level; above ⇒ one entry allowed. Print the level |
| T2 | tape confirmation | A-grade (RS20/RS60) or KR B-grade (KIS investor actuals) agreeing ⇒ full first tranche; disagreeing ⇒ smaller first tranche and a dated re-check. **OBV alone (C-grade) may not set timing either** — it adds no leading power once real flow is known (r≈0.49) |
Write both into the execution table: entry split, stop level, re-check date. (Until 2026-10-31 these two were gates G1/G2 that could veto ENTER/ADD regardless of filings — removed because runs ended carried by tape; flow evidence was right 5 of 32.)

## Ledger — exactly one row (a PASS with no row is a failed run)
- research/report: PASS/TRIM/EXIT ⇒ `python -X utf8 scripts/reject_ledger.py add --date … --ticker … --name … --cls … --why … --stage CO_VERDICT --revives-if "…" --recheck-date …`;
  looked-but-not-bought ⇒ `scripts/missed_ledger.py add … --enters-if "…" --recheck-date …` (the script refuses a ticker/date already in the reject ledger).
  Exposure context: `python -X utf8 scripts/exposure_rule.py target --json` is the single source of the cash target; never invent one.
  🚨 `reject_ledger.py score` prices rows off a **KR** cache and benchmark: the ~100 US rows score `채점불가` silently
  (PSX's rejection was worth +18.63pp vs SPY, in no class average). With `--market us`, write the row and **state it cannot be scored today**.
- forensic: merge `llm_outputs/real_alpha_kr/ledger.json` (observation points replaced with this run's; op counters from CO_CARRY).
- Mid-run failure: do **not** write `verdict.json` or merge the ledger; write `FAILED.md` with the reason (the name re-runs next time).

## Observation points and lens weights (L2 [lens](../L2_modules/lens.md))
- 2–3 dated, falsifiable points: «by {date}, if {Y} does not appear, this verdict is wrong».
- Register the main one: `find` first (reuse an open Q on the same observable/date) → `ask --subject {T} --desk company --settle … --observable …`
  → one `ev` per **carrying** reading with its kind (`filing`, `estimates`, `macro`, `flow`, `price`, `news`; competition rows use `--key competition_*`) and link →
  `advise` → `think --weights …` (alive weights sum to 100). Dead methods get `--dead` with weight 0.
- 🔴 **Flow + positioning weight cap 30%** — `think` rejects more (human decision 2026-10-31). Measured: flow 5/32 right, filings 6/8.
  A verdict whose weights put flow first is a verdict carried by flow — rewrite or downgrade.
- `verdict.json` fields (batch contract in `batch_fanout`): verdict · gates (non-applicable = `null`, never `false`) · driver ·
  frame · set_diff · rr · stop · horizon_days · evidence_grade · evidence_mix (lens weights by bucket) · **thesis** (refutable) · observation_points · ledger_row · lens_q.

## Close (4 layers)
1 essence → 2 causal chain (filings → structure → environment → money) → 3 the numbers → 4 one line. Every number traces to
DATAPACK or a document id; an unlabeled number means unfinished. Not licensed advice; the book is untouched.

## ✅ EXIT CHECK
- [ ] First line is the delta; one verdict for the mode with the cracked/confirmed axis named.
- [ ] research/report: G1–G8 printed with values; G4 computed on the own target; stop is a number; T1/T2 written as entry split + stop level, not as a veto.
- [ ] Exactly one ledger row with condition **and** recheck date (forensic: ledger.json merged); US scoring defect stated if US.
- [ ] 2–3 dated observation points; one lens question with evidence rows and weights committed (`show` checked); flow + positioning ≤ 30%.
- [ ] `verdict.json` written (or `FAILED.md` and no verdict.json).
