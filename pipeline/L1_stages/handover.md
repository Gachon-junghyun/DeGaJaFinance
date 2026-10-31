# L1 · HANDOVER — settle what is due, inherit what is current, and close the run (stage)

> Big stage. **Runs first** in industry_us and industry_kr (after the separate `preflight` protocol), and its
> §6 close-out runs **last**. Absorbs DRIFT (2026-10-31). `--market us|kr`.
> **Reads**: the lens ledger, the two decision ledgers, `PREFLIGHT.md`, the thin `handoff/*.md` files, the
> previous run's `MACRO_REPORT.md` and `BET_SHEET.md`.
> **Output**: `HANDOVER.md` — **cap 8 KB** — plus append-only write-back at close-out.
> **Next stages use**: the due list (EARNINGS candidate source b), the instrument permissions (every stage),
> the exposure state (BET sizing language), the binding rule groups (each stage's carry rules).

**Why it is lean now.** The old stage read the shared spines «in full» (3.3–3.6 MB per run) and the final sheets
cited them 0–1 times. Numbers now live in the lens ledger; the handoff files hold only what is current.
The archive `handoff/_archive/` is **not** read during a run; open it only to look up a specific ID by grep.

## L2 called
- [lens](../L2_modules/lens.md) — the first check; its records are authoritative. Old bracket prose is archived.
- [schedule](../L2_modules/schedule.md) — `drift_watch` at close-out.

## What this stage does

### 0. Gate — is there anything new to read?
If no market session has settled since the previous run of this desk (holiday, weekend re-run), do §1 only, write
`HANDOVER.md` with one line `NO_NEW_SESSION — last settled <date>; desk not run`, and stop. Measured: KR 3 of 3 and
US 1 of 3 recent runs re-stamped the same 09-23 snapshot with zero changed verdicts (K1 §4-1, rank 2).

### 1. Settle the lens ledger first
`python -X utf8 -m module_lens score` → `python -X utf8 -m module_lens due`. Every past-due question (including the
other market's) is resolved — `resolve <QID> <branch> --value "<observed>" --scorer <desk> --link "<source>"` —
or marked `AMBIGUOUS` with a reason. Re-run `due`. Then the «NOT in the ledger» table of `handoff/SCENARIOS.md`
(`P###` · `M-###` · colliding `S##-KR` brackets never migrated): score each past-dated row by hand against its
frozen threshold, or mark it `EXPIRED` with the reason. No silent deferral, no post-event threshold change. Score the
registered observable, not the price reaction.

### 2. Audit both decision ledgers
`python -X utf8 scripts/reject_ledger.py due` and `python -X utf8 scripts/missed_ledger.py due` (never `score`
alone). Each surfaced row is `resolve`d this run (revived on fresh evidence / reaffirmed) or named as pending. A
due row that crosses a second HANDOVER unexamined is a process failure. Report the legacy (no-condition) count —
a clean `due` (nothing due) is **not** evidence the ledger is healthy; only a legacy count that shrinks run over run is.
⚠ `missed_ledger` excess sign is inverted; never sum the two without aligning signs.

### 3. Instruments and exposure
- Read `llm_outputs/{date}/preflight/PREFLIGHT.md` (protocol `preflight`) or write that it was not run. Copy its
  permission table: a FAILED gate removes that citation right for every stage of this run (dead news axis ⇒ no
  theme-freshness claim; a sign-flipping bucket ⇒ no verdict on its `wflow`).
- `python -X utf8 scripts/exposure_rule.py state` and `target --json` → the 4-state verdict, invested vs target,
  cash target (single source). Empty `show` ⇒ write **cold start** (measured: cold start read 방어/−1.9pp where the
  backfilled path read 복귀/−37.2pp). `밴드미설정` ⇒ 🚨, no number substituted.

### 4. Inherit the current view
- Read `handoff/STANDING_VIEW.md` + this desk's `STANDING_VIEW_{US|KR}.md`, `handoff/RESEARCH.md`,
  `handoff/SCENARIOS.md` (thin files — read whole). `[inferred]` claims may be carried but not cited as evidence.
- Retracted ledger (§5 of STANDING_VIEW) **before** forming today's view; a claim matching a retracted ID is dropped
  or re-argued with a new measurement that names the old one.
- Stale-check: rows whose `asof` is past the horizon and suspensions whose clearing date passed become dig items;
  `RESEARCH.md` Part C (live digs) supplies today's candidate dig assignments.
- `python -X utf8 -m module_report_tags show` — coverage vs belief: a belief with no recent coverage is demoted.
- Previous run's `BET_SHEET.md`: names tagged by ALPHA are carried **independently of their sector's slot**
  (measured: 006360 lost its tag when INDU rested, +12.3% in five sessions unowned).
- Load `RESEARCH.md` rule groups as binding and write in `HANDOVER.md` which group binds which stage:
  C (citing a number → every stage) · S (statistical claims) · D (reading data → FLOW_CHECK, indicators) ·
  W (writing a conclusion → EARNINGS, COMPETITION, BET) · L lenses (COMPETITION, PREMORTEM).

### 5. Self-refutation is written down (D48)
A claim this run asserts and later refutes stays in the file with what broke it. Zero self-refutations in a run
that ran controls is itself worth a line.

### 6. Close-out — after ALPHA (the protocol calls this)
- If `STANDING_VIEW*.md` or `RESEARCH.md` would pass **30 KB**, first move its oldest dated rows to
  `handoff/_archive/<date>/` (keep every §5 retracted ID's one-line entry; leave a pointer line), then write.
  Not `scripts/handoff_compact.py` — it expects the pre-2026-10-31 layout.
- Write back to `handoff/*.md`, append-only: changed theses with `[measured]`/`[inferred]`, retractions with the
  measurement that killed them, new dig items. Numbers go to the lens ledger, not to prose.
- `python -X utf8 -m module_lens export` (backup; nightly routine runs `learn`).
- `python -X utf8 scripts/axis_inflection.py` then `python -X utf8 scripts/ic_ledger.py log` — the IC ledger only
  learns when it is called (it used to ride the carryover L2, which this stage no longer loads).
- Update the coverage ledger per [handoff](../handoff.md).
- **Drift (US; KR when a binary ≤48h was open)**: +3–6h after the run, `python -X utf8 scripts/drift_watch.py
  --report <today's MACRO_REPORT.md>`. On 🚨 body-read the triggering articles and **append** a `§ DRIFT ADDENDUM` to
  `MACRO_REPORT.md` — never rewrite the original call (proof case 2026-07-13: the Iran/Hormuz read flipped intraday
  after a 15:59 finish). If the previous run's drift was never run, run it on that report at the next §1.

## ✅ EXIT CHECK
- [ ] §0 gate applied; a no-new-session day stops after §1 with the one-line file.
- [ ] `module_lens score` then `due` run; every past-due question resolved or AMBIGUOUS with a reason.
- [ ] `reject_ledger due` and `missed_ledger due` run; each row resolved or named pending; legacy count reported.
- [ ] PREFLIGHT permission table copied (or «not run» written); exposure state carried with cold-start/band caveats.
- [ ] Thin handoff files read; retracted ledger read before any view; stale rows flagged; tags preserved.
- [ ] Rule groups mapped to stages in `HANDOVER.md`; no sizing or buy/sell language (P4).
- [ ] `HANDOVER.md` ≤ 8 KB.
- [ ] **Close-out**: write-back append-only, `module_lens export` run, coverage ledger updated, drift run or scheduled.
