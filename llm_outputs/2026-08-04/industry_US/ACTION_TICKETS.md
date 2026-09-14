
---

# ★ ADDENDUM — ALPHA, 2026-08-04 (appended; `core_pick` is HUMAN-LOCKED and was NOT modified)

## A-1 · ⚠⚠ This file's FIRST generation was a SILENT FALSE NEGATIVE — new defect D155

The first `action_bracket.py` call, run with no `--date`, printed:

> `_No tickets — no cycle GAP and no dated binary in window._`

**Both halves of that sentence are false.** `cycle_exposure.py` returned a **🚨 GAP on the rank-2
Energy cycle (2.88% vs an 8.0% floor)** and `catalyst_calendar.py` returned **11 binaries in the
window, three of them D-0.**

**Cause, read from the source**: `scripts/action_bracket.py:190` — `date = a.date or
_dt.date.today().isoformat()` — and lines 89–90 read `CYCLE_EXPOSURE.json` / `CATALYST_WATCH.json`
from `llm_outputs/{date}/`. **This run started 2026-08-04 10:0x ET and crossed local midnight KST
mid-run, so `date.today()` resolved to 2026-08-05 while every input the run produced lives under
`llm_outputs/2026-08-04/`.** The script found an empty folder and **reported absence as a finding.**

⇒ ⚠⚠ **The desk's anti-tunnel backstop — the artifact whose entire job is to force a both-sides
bracket on every binary and a tape-independent core on every GAP — returns "nothing to do" whenever a
run crosses local midnight, which is the normal shape of a US run executed from KST.** It fails
**silently and in the safe-looking direction.**
**Remedy: the caller passes `--date <run date>` (done here), or the script inherits the run folder
from the protocol rather than from the clock.** Registered as **D155**.

★ Second-order observation from the same two calls, minutes apart: **`fx` printed 1380 then 1430
(+3.6%)** and book total 14,862,573 → 14,860,944 KRW. **A live FX quote inside a sizing artifact
moves the illustrative share count by ~3.6% between two runs of the same script on the same data.**
Recorded as context, not as a finding.

## A-2 · ⚠⚠ The regenerated ticket, and why it may not be read as evidence — D19, 9th consecutive run

The ticket produced is a **`CORE-STARTER (BUY)` on PSX**, *"establish NOW regardless of tape."*
**Its stated rationale is retracted, its number is stale, and its subject left the book today.**

| Clause in the ticket | Status |
|---|---|
| *"cheapest large refiner on forward (11.2, PEG 1.17)"* | ⛔ **RETRACTED as R8 on 2026-07-22.** On a like-for-like basis the ordering was **MPC 8.8× · VLO 9.4× · PSX 10.8×** — PSX was the **most expensive** of the three. **This run's own DEEP-ENRG measures MPC 11.29× vs PSX 10.85×** — the ordering has since flipped, but **not for the reason the string gives**, and the string has never been recomputed. |
| *"the only Energy name with shorts actively exiting (FINRA short-vol z −1.43)"* | ⛔ **Wrong in FOUR different directions across five runs**: measured **+2.01 (07-20) · +0.01 (07-21) · +1.03 (07-23)**, and **today 2.3% of float `covering`** with **P/C 0.19 and skew −5.0**. **A frozen string, not a measurement.** |
| *"clean structural entry, not an extended one (cf. MPC RSI 85.7)"* | ⚠ **PREMORTEM Lens 3 measured PSX at an 88.5% last-20 concentration on a days-21-to-60 segment of +1.4** ⇒ *"essentially nothing underneath it"* — **the most fragile of the three refiners on the desk's own momentum lens.** |
| *"Crack-spread leverage, not crude beta"* | ⚠⚠ **This run's headline event is that the crack's own pre-registered falsifier FIRED (S49-B).** The ticket's stated edge is the axis that just broke. |
| *"establish NOW regardless of tape"* — the GAP rule | ⚠⚠ **The GAP's magnitude is `unknown` (C3)**: **R39** killed the registry tag it is computed on, **D152** shows LNG is double-counted into two cycles, and **D151** shows the floor is denominated on total assets including idle KRW cash. **PREMORTEM Lens 4's verdict is adopted: the FLOOR is the wrong object and needs human re-derivation before it can be obeyed.** |
| the subject itself | ⚠⚠⚠ **PSX was filed 🔴RESOLVED by this desk's own ALPHA stage on 2026-08-02, and PREMORTEM Lens 4 measured it LEAVING THE BOOK on this session** — rank-2 epicenter **$731.68 → $308.86 (−57.8%)**, `epi_names` **[MPC, PSX] → [MPC]**, with **+$683.87 rotating into names no registry cycle tags.** **The desk's only BUY-shaped artifact points at a name the desk sold today.** |

⇒ **This ticket is recorded, not acted on, and it may NOT be cited as evidence by any stage.**
⚠ **`core_pick` is HUMAN-LOCKED — no stage may rewrite it, so the correction is written here as an
addendum rather than applied.** **D19 is now 9 consecutive runs old and is the single oldest
unactioned defect on the desk's list.**

## A-3 · The both-sides brackets that DO exist — carried from PREMORTEM, not from this script

`action_bracket` emitted **one** bracket line (*"Nearest binary: AMD earnings (D-0) — both-sides armed
below"*) **and then armed nothing below it** — the same announce-without-emit behaviour logged as
**D19** since 2026-07-22. **The actual both-sides coverage for all 11 binaries in the window is in
`BLINDSPOT_PREMORTEM.md` §2**, produced by PREMORTEM Lens 2, and the registered rows are:

| Binary | Owner bracket | Both-sides source |
|---|---|---|
| AMD 08-04 · ANET 08-04 | **S50** (+ **S50-ANNEX 2nd entry**, registered today) | PREMORTEM §2 |
| MPC 08-04 · PSX 08-05 | **S53** ⚠ collapsed to a name-level footnote by its own registration once S49-B fired first | PREMORTEM §2 |
| SPCX unlock 08-06 | ★ **S56**, registered today | PREMORTEM §2 |
| CEG 08-06 · VST 08-07 | **S35 / S47** (both → 08-07) ⚠ **scored on the regulated-SIX only — R40** | PREMORTEM §2 |
| LNG 08-06 | logged as a **CONTROL observation**, deliberately unbracketed on L3 | PREMORTEM §2 |
| NFP 08-07 | **S51** + the **`S51-A-BULL`** qualifier ⚠ **DEEP-FIN measured the print NON-INFORMATIVE as written** (S23 0/249, S51-A 94% of the year) | PREMORTEM §2 / DEEP-FIN §1 |
| Hormuz (undated) | ★ **S55**, registered today | PREMORTEM §2 |
| CPI 08-12 · PPI 08-13 | **S9 · S26 · S41 · S42** ⚠ **three of them EXPIRE ON CPI DAY** — a calendar collision flagged for the next run | PREMORTEM §2 |
| MATR after 08-05 | ★ **S57**, registered today | PREMORTEM §2 |

**No one-way tilt into a known binary survives this run.** ✅
