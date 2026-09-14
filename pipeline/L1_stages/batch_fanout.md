# L1 · BATCH_FANOUT — N subagents, one company each, all in one message

> Phase 2 of the company batch. Spawns **one subagent per roster row**, each running the
> `company_research` protocol on its single name and returning a **structured verdict**, not prose.
> Not a module — an Agent fan-out, same idiom as PREMORTEM's four lenses. Output: one
> `company_batch/{ticker}/` directory per name, each with `REPORT.md` + `verdict.json`.

## Why a subagent and not this session
Ten companies × (datapack + segment table + driver series + peer set + news + filings) does not fit one
context, and a batch that degrades as it goes produces its worst research on the last names — which is
indistinguishable, in the output, from those names being worse. **Isolation makes the tenth report as
good as the first.** The parent keeps only the roster and the returned verdicts.

## Calls
- **Agent fan-out — all N in ONE message (parallel).** Each subagent's brief is built from the roster row
  and MUST contain, verbatim:
  1. the working directory and the compiled protocol path — `pipeline/protocols/_compiled/company_research.md`
     — with the instruction to **read it whole before acting**; it governs all detail and every guard;
  2. the **ticker and its market**, plus the ticker-format table for that market (violate → 0 data);
  3. the row's **mandate** (from BATCH_SELECT: the due `--revives-if`, the unanswered question, or
     `first research`) — the subagent starts from the question, not from zero;
  4. the **output contract** below, stated as the definition of a completed run;
  5. the stage range: **FORENSIC_PACK → BET_VERDICT** (skip PULSE and SIZE; the batch is research, and
     sizing belongs to a human-run SIZE against the live book).
- A subagent that cannot finish writes `FAILED.md` with the reason and **does not write `verdict.json`** —
  a missing verdict must stay missing so the next batch retries the name (real_alpha's rule, same reason).

## Output contract — every subagent returns this file, or the name did not complete
`company_batch/{ticker}/verdict.json`:
```json
{"ticker":"PSX","market":"us","date":"2026-08-21","verdict":"ENTER|ADD|HOLD|TRIM|EXIT|PASS",
 "gates":{"G1":true,"G2":true,"G3":true,"G4":false,"G5":true,"G6":false,"G7":true,"G8":true},
 "driver":{"coverage_pct":61.6,"percentile":92.8,"roll_clean":true},
 "frame":{"dominant":"refiner","beta_leg":true},
 "set_diff":{"alpha_delta":["…"],"risk_unseen":["…"]},
 "rr":{"upside_pct":6.0,"downside_pct":-9.7,"ratio":0.62},
 "stop":221.68,"horizon_days":60,"evidence_grade":"A|B|C",
 "thesis":"one line a top-down run can confirm or refute",
 "observation_points":[{"date":"2026-08-28","test":"falsifiable"}],
 "ledger_row":{"which":"reject|missed","cls":"…","condition":"…","recheck_date":"…"}}
```
- **A gate that does not apply is `null`, never `false`.** `company_score.py` drops nulls from the
  denominator; writing `false` for "not applicable" turns *not measured* into *failed*, which is the
  `clip(nan)=+1.0` trap this repo already paid for once (2026-08-10).
- `evidence_grade` = the **highest** grade among the axes actually carrying the verdict, per L2
  indicators' A/B/C table. A verdict resting on OBV alone is **C** — say so; it is not a punishment,
  it is the scale telling the next reader how much to lean.
- `thesis` is the field the top-down run confirms. Write it so it can be **wrong**: a sentence no
  observation could refute is not a thesis and BET will have to re-derive the name anyway.

## ⚠ Parent-side rules
- **Do not re-run any of this in the parent.** The parent reads `verdict.json`; if it wants prose it
  opens the child's `REPORT.md`. Re-deriving a number in the parent is P1 duplication across processes.
- **Do not average the children.** N verdicts are N observations, not a portfolio view. Ranking is
  BATCH_SCORE's job and it is arithmetic, not judgment.
- Report **completed / failed / skipped** counts. A batch of 10 that returns 7 verdicts and says "done"
  has hidden 3 — and those 3 are exactly the names that will be missing when BET goes looking.

## ✅ EXIT CHECK
- [ ] One subagent per roster row, all dispatched in **one** message (parallel), none run serially in the parent.
- [ ] Each brief carried the compiled-protocol path, the ticker+market format table, the mandate, and the output contract.
- [ ] Every completed name has BOTH `REPORT.md` and `verdict.json`; every failed name has `FAILED.md` and **no** `verdict.json`.
- [ ] Non-applicable gates are `null`, not `false`, in every returned verdict (spot-check at least two files).
- [ ] Completed / failed / skipped counts printed and they sum to the roster size.
