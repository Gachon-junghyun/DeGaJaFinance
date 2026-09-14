# SECTOR_ROTATION — industry_US — 2026-07-27 (Mon)

> Stage 5/10. **Delta-only.** The 11-sector verdict lives in `MACRO_REPORT.md §E`; the flow numbers
> live in `SECTOR_FLOW_US.json`. Both are on disk. This file writes **only what changes and why.**
> Flow `asof` **2026-07-24 settled** · benchmark **SPY** inline (C1).

## §1 · Inherited — one line, verbatim from MACRO §E

`ENRG OW− · FIN OW− · INDU OW− · HLTH N · RE N · IT N · STPL N · COMM N− · UTIL N− · DISC N− · MATR UW`

⚠ **Binding constraint on this stage**: **no US session has occurred since the sweep that produced
these numbers.** `SECTOR_FLOW_US.json` (`asof 07-24`, wflow +0.109, 🟢 25 / 🔴 72) reproduces the
2026-07-25 run's file to within 0.001 and one name. **Any "change" claimed here would be a change in
reading, not in data** — and this stage's own rule forbids re-arguing macro.

## §2 · Deltas

| Sector | Matrix said | Flow evidence (`asof 07-24`) | New verdict | Who resolves |
|---|---|---|---|---|
| **Cons. Staples** | **N** | wflow **−0.101** · eqflow **−0.120** · **breadth 0.00** · **0 🟢 / 4 🔴 of 19** · Δ +0.058 | **N → N−** | — (settled here) |

**One delta.** Both aggregate axes are negative, and **Staples and Materials are the only two sectors
on the board with breadth 0.00.** The matrix's stated reason for holding N was that XLP was 3rd-best on
07-24 *"consistent with the day's rotation-out-of-tech read"* — a one-session return, against a 20-day
flow that is negative on both axes with **zero greens in 19 names.** The cut is carried entirely by
flow numbers; no macro argument is used.

⚠ **W5 dispersion stated, because it bounds the cut to one notch**: the sector is not uniformly weak —
**PM +0.673 and ADM +0.606** are healthy flow scores. **N− is a breadth verdict, not a verdict on
those two names.**

## §3 · Divergences named, changes DECLINED — with the reason each time

Three sectors show a matrix×flow divergence large enough to move a notch under this stage's own rules.
**All three declines are logged rather than silently skipped.**

**① Energy — flow says PROMOTE, and the promote is declined on the sweep's `asof`.**
Energy is **#1 on wflow (+0.44) and #2 on eqflow (+0.305)** on a board whose universe wflow is +0.109 —
rule (b)'s "flow-led sector the matrix under-rated." **Declined.** The reason is this stage's own
field note, not a macro re-argument: **the sweep is `asof 07-24` and the sector's largest catalyst in
six weeks landed AFTER it** (the 07-27 oil repricing, MACRO §C-1). **Promoting a sector on a flow
number that pre-dates its own catalyst is the same error class as reading an unsettled bar.**
⚠ Second reason, also a number: the composite 3-2-1 crack sits **4.30 points from P4's kill line on
the last settled close**, the closest of the entire advance.

**② Financials — the board's only breadth-led sector, and the notch is declined pending its own dated
resolver.** FIN is **the only sector where eqflow (+0.342) exceeds wflow (+0.278)**, with 5 🟢 / 3 🔴 of
47. M40 measured this gap **narrowing** (+0.145 → +0.067) on 07-22; on the 07-24 close it has
**re-widened to +0.064** — i.e. the breadth leg the OW rests on (the only leg left after **R11** killed
the steepener) is intact. **Declined:** the sector's registered resolvers land inside three sessions —
**S23 (bear-flattener hold, FOMC 07-29)** and **S14/S14-num (MA 07-30)** — and a notch set today on
3-day-old flow would be re-set 48 hours later on strictly better information. **→ DEEP's #1 question.**

**③ Real Estate — the second-highest sector Δ on the board, declined as an event footprint counted
twice (D51).** RE carries **Δ +0.226** (2nd of 11) and is **the only sector with ZERO reds** (1 🟢 / 0 🔴
of 12). **Declined:** the Δ is **DLR's +1.099**, the largest single-name delta of all 300, and DLR
**filed its 8-K on 2026-07-23, one session before the flow date.** **The flow score, OBV state and
volume surge ARE the earnings event** — counting them as independent confirmation of it is exactly
**D51**, which this desk registered after making the identical error in two sectors on one date.

**④ Industrials — a rule-(a) divergence at the label, declined on a flow DECOMPOSITION measured this
run.** The label reads **wflow −0.04, 5 🟢 / 17 🔴 of 50** against an OW− tilt, which rule (a) would cut.
Decomposed on this run's own JSON:

| Node | n | mean flow | 🟢 / 🔴 | mcap share |
|---|---|---|---|---|
| **Defense primes** (LMT·RTX·NOC·GD·LHX) | 5 | **+0.667** | **3 / 0** | 11.3% |
| **Rails / freight** (UNP·CSX·NSC·ODFL·UPS·FDX) | 6 | **+0.368** | 2 / 1 | 9.9% |
| **Capital goods + everything else** | 39 | **−0.193** | **0 / 16** | **78.8%** |

★ **All five of the sector's greens are defense and rails. Zero of the 39 capital-goods names is
green, and 16 of the sector's 17 reds sit there** — on **78.8% of the sector's market cap.** The
primes-minus-capital-goods spread is **+0.860 flow points**, the **widest yet measured** (M26 0.705 →
M36 0.285 → **0.860 today**). ⇒ **The label's negative aggregate is 78.8% of mcap dragging, while the
two nodes the OW− actually rests on carry the entire green count.** Cutting the label would be the
**W5** error the desk has now measured three times. **Declined on a flow decomposition, not a macro
argument. → DEEP resolves.**
⚠ Worth naming: **DAL and UAL sit in that 🔴 capital-goods bucket** — the refiners' own customers
(M34/W4), red on flow while their fuel costs run +66–84% YoY.

**⑤ Materials — an AGREE with content, and it resolves a declared disagreement.** The matrix carried an
explicit tape disagreement (*"XLB +1.93% was the 2nd-best sector on 07-24 — against the tilt"*) and
pre-committed to re-arguing the UW if XLB beat SPY again. **No session has occurred, so that test is
deferred, not passed.** But the flow is unambiguous: **Materials is worst on wflow (−0.358), worst on
eqflow (−0.300), 0 🟢 / 5 🔴, breadth 0.00.** ⇒ **the one-session return and the 20-day flow point
opposite ways, and the UW is on the flow side.** No change; the disagreement stays **declared**.

## §4 · DEEP picks — three, not four, and the fourth is declined rather than padded

**Recency input, `DEEP_LOG` lines read from disk**: `07-22 continuous=[ENRG,FIN]` ·
`07-23 [ENRG,FIN]+HLTH` · `07-24 [ENRG,FIN]+HLTH` · `07-25 [ENRG,FIN]+RE`.

**① Continuous-track (anti-thrash rule applied and stated): ENRG · FIN.** Both held continuous slots in
the previous run and both remain top-4 OW today ⇒ **they keep the slots by rule.**
⚠⚠ **Declared RECENCY-STARVED — this is their FIFTH consecutive run.** The rule keeps them; the
mitigation is the same one the 07-22 run used, **a narrowed mandate that must be a question no prior
DEEP has answered:**
- **ENRG mandate — NOT the crack level again.** ① Is the composite's fall a **gasoline** event with the
  **distillate bottleneck intact** (S8 branch B) or the bottleneck itself going (branch A)? Resolve on
  the **settled** 07-27 close against the thresholds MACRO §F froze **before** the outcome.
  ② **M146's epicenter mismatch, now on its 3rd replication**: the only held Energy name is **XOM with
  0% refining**, the registry's human-locked `core_pick` is **PSX (unheld)**, and the shortlist surfaces
  XOM while the refiners are blocked by a volume gate. **Three instruments, one blind spot** — is the
  blind spot in the instruments or in the thesis?
- **FIN mandate — §3②'s declined divergence, and only that.** Is **eqflow > wflow** genuine breadth or
  the **payments/insurance concentration M40 measured** (34% of names, 45% of gross positive flow, at
  2× the sector mean)? And does **S23's bear-flattener** hit the half **M138** says has migrated to
  markets/financing NII? ⚠ The exchanges sub-node's registered test is **BROKEN, not passed (M135)** —
  use the replacement observable (equal-weight excess of the 7 vs SPY, 07-24 → 08-07), not RS60.

**② Rotating: INDU — one, not two.** Last DEEP'd 2026-07-24. It is taken back inside the recency
window **for a reason no other sector has: its registered falsifier settles in under 24 hours.**
**S20 + S20-ANNEX fire on UPS tomorrow (07-28)**, testing the rail node's median RS20 vs SPY **and**
closing **W4/D23**'s last unread refiner customer. ⚠ **D52/D73 makes the positioning axis unreadable on
the two names that matter** (UPS baseline 57.7%, UNP 52.2%, both far outside the tool's 40–45% band) —
**DEEP must state that rather than quoting the z.**
**Mandate**: resolve §3④ — is Industrials one sector or three? And does the rail node survive a
volume-driven UPS cut, given **M91** (~8 of UNP's 12 revenue growth points are fuel surcharge, so a
volume cut plus a rolling crack is one shock counted twice)?

**③ NOT padded to four — stated, per the rule.** Only **three sectors carry an OW notch** (ENRG, FIN,
INDU) and all three are taken. **HLTH, RE and IT are Neutral**, and *"never pad with Neutral/UW to
reach 4."* **Every OW sector on this board has been deep-dived inside the last three runs — the
rotation pool is exhausted, and that is said plainly rather than filled.**

**④ Escalated to PREMORTEM as the #1 promotable extra: Information Technology / memory.**
Precedent: the 07-22 run escalated HLTH and IT the same way. The case is **not** a flow number — IT's
flow is the board's worst breadth (**eqflow −0.206, 25 🔴 / 4 🟢 of 56**) and would not earn a slot.
The case is that **MACRO §D-P9 is a brand-new proposition about the supply side of the desk's own
regime call**, built on an event (**CXMT's $8.6bn capacity raise**) that **no DEEP has ever examined**
and that **two prior runs missed while it built from 3 to 16 outlets** (D71). **PREMORTEM decides;
ROTATION does not promote a Neutral sector by the back door.**

## §5 · Divergences and their resolution owners — the checklist this stage owes

| Divergence | Owner |
|---|---|
| ENRG: flow #1 on both axes vs a tilt cut on its own KPI | **DEEP ENRG** (settled 07-27 close vs MACRO §F's frozen thresholds) |
| FIN: eqflow > wflow — real breadth or payments/insurance concentration | **DEEP FIN** (and S14, 07-30) |
| INDU: label −0.04 vs a +0.860 internal spread | **DEEP INDU** (and S20, 07-28) |
| RE: 2nd-highest Δ that is one 8-K's footprint | **PREMORTEM** (D51 discipline) + S25's 08-08 observable |
| IT: worst breadth on the board vs a brand-new supply-side proposition | **PREMORTEM** (promotable 5th) + S13, 07-29 |
| MATR: 07-24's 2nd-best sector return vs the board's worst flow | **deferred, no session** — re-test on the next settled close |

## ✅ EXIT CHECK

- [x] **§1 is one line**, inherited verbatim from MACRO §E. No unchanged sector gets a row or a
      restated flow number.
- [x] **The one delta (STPL N → N−) cites flow numbers only** — wflow, eqflow, breadth, 🟢/🔴 counts.
      **Zero macro re-arguments were used to move anything.**
- [x] **Four declined changes logged with their reasons** (ENRG asof · FIN pending its dated resolver ·
      RE D51 event footprint · INDU flow decomposition), plus one AGREE-with-content (MATR).
- [x] **Every divergence has a named resolution owner** (§5).
- [x] **DEEP targets picked by the rule**: continuity applied and stated (ENRG/FIN, 5th run,
      **declared recency-starved** with narrowed mandates), rotation applied (INDU), **and the 4th slot
      explicitly NOT padded** because only three OW sectors exist.
- [x] Linter run — result below.
- [x] DEEP_LOG line appended.
- [x] Zero buy/sell language, zero sizing (P4). English-pure.

**Linter**: `python -X utf8 scripts/report_lint.py llm_outputs/2026-07-27/industry_US/SECTOR_ROTATION.md`
→ **✅ 0 findings** (C1 · C2 · S6 · D6). ⚠ Form-only — it cannot see that four notch changes were
declined on purpose, which is this file's actual content.

## DEEP_LOG 2026-07-27: continuous=[ENRG, FIN] rotating=[INDU]
(3 picks, NOT padded to 4 — only 3 OW sectors exist after §2/§3. ENRG+FIN keep continuous slots by the
anti-thrash rule for a **5th consecutive run** and are **declared RECENCY-STARVED**, mitigated by
narrowed mandates: ENRG → the gasoline-vs-distillate decomposition + M146's XOM/PSX epicenter mismatch;
FIN → eqflow-vs-wflow breadth + S23's flattener, using M135's **replacement** observable because the
registered one is broken. INDU taken back inside its recency window because **S20 fires on UPS in under
24h**. Delta this run: **STPL N → N−** (breadth 0.00, 0🟢/4🔴 of 19, both axes negative). Declined and
logged: **ENRG promote** (sweep `asof` pre-dates its own 07-27 catalyst) · **FIN promote** (its dated
resolvers land inside 3 sessions) · **RE promote** (Δ +0.226 is DLR's 8-K footprint — D51) ·
**INDU cut** (label −0.04 hides a **+0.860** primes-vs-capital-goods spread, the widest yet measured;
all 5 greens are defense/rails, all 16 capital-goods names are 🔴 on 78.8% of mcap). MATR UW held with
its tape disagreement still **declared and deferred** — no session occurred to re-test it. Escalated to
PREMORTEM as promotable extra: **IT/memory #1** — not on flow (worst breadth on the board) but because
**P9/CXMT is a supply-side proposition no DEEP has examined and two runs missed it while it built 3→16
outlets (D71)**.)
