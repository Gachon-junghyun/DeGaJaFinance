# SECTOR_ROTATION — industry_US — 2026-08-02 (Sun)

> **Delta-only.** MACRO owns the 11-sector verdict and `SECTOR_FLOW_US.json` owns the flow numbers;
> both are on disk all run. This file writes **only what changes and why**, then picks the N DEEP
> targets. **N = 4** per `pipeline/protocols/industry_us.md` (2 continuous + 2 rotating).
> Analysis only, zero buy/sell, zero sizing (P4).

---

## §1 · Inherited — one line, verbatim from `MACRO_REPORT.md §E`

`ENRG OW− · FIN OW− · IT N · DISC N+ · COMM N · RE N · STPL N · HLTH N · INDU UW− · MATR UW · UTIL UW−`

Flow source for every number below: **`SECTOR_FLOW_US.json` asof 2026-07-31 settled**
(n=300 · universe wflow **+0.002** · 🟢16 / 🔴86 · every sector's `delta` negative except
Consumer Discretionary).

---

## §2 · Deltas — four, each carried by a flow number

| Sector | Matrix said | Flow evidence (wflow · eqflow · breadth · Δd/d · 🟢/🔴) | **New verdict** | Who resolves |
|---|---|---|---|---|
| **Energy** | **OW−** | **wflow +0.519 · eqflow +0.463 — #1 on BOTH, by 4.3× the runner-up · breadth 0.06 · Δ −0.039 (2nd-smallest decay on the board) · 🟢1 / 🔴0 — the ONLY sector on the board with zero red names** | ★ **OW** (promote one notch) | **DEEP-ENRG.** ⚠⚠ **The promote comes with the run's #1 divergence attached, and DEEP must resolve it first**: on the very session this flow was measured, the settled 3-2-1 crack fell **−16.7% in two sessions on its gasoline leg while crude rose**, and S49's distillate buffer collapsed to **+1.07 against a −5.0 line**. **The equities and the commodity moved opposite ways inside one bar.** Early or trap — that is the DEEP mandate |
| **Industrials** | **UW−** | **breadth 0.10 — the board's BEST · 5 🟢 (ITW +0.79 · RTX +0.78 · TRI +0.78 · ETN +0.70 · GD +0.55) = the most of any sector, 31% of the universe's 16 greens on 17% of its names · eqflow +0.048 ABOVE wflow +0.001 ⇒ breadth-led, not mega-cap-led · Δ −0.072 (3rd-smallest decay)** | ★ **N** (promote one notch) | **DEEP-INDU.** Rule (b): *money moved before the thesis.* ⚠ The price disagrees hard (**XLI −2.52pp exc20d / −2.64pp exc5d vs SPY**), so this is a **matrix×flow divergence, not a confirmation** — DEEP owns early-vs-trap. ⚠ **S42's branch-B second leg is currently failing: only 1 of the 4 capital-goods names (ITW) still carries 🟢** |
| **Health Care** | **N** | **Δ −0.472 — the WORST on the board · wflow −0.112 and eqflow −0.051, both negative · 🟢0 / 🔴7 of 32** | ★ **N−** (demote one notch) | **carried; no DEEP slot this run.** ⚠⚠ **The demote is carried by the delta and the two flow scores ONLY — NOT by the zero green count**, which SWEEP §3 diagnosed as partly a `vol_surge` artifact (6 names pass the accumulation pre-condition and all 6 are blocked: BMY 1.11 · REGN 1.03 · TMO 1.02 · ABT 0.83). **C7's belief-vs-money gap has closed from the money side; its re-check is 08-06 and its resolving observable's definition still needs a human (C5)** |
| **Materials** | **UW** | **wflow −0.313 (worst) · eqflow −0.199 · breadth 0.00 · 🟢0 / 🔴5 of 12** | **UW — and this run's ROTATION WITHDRAWS its own 2026-07-30 promote to N** | **DEEP not required.** The 07-30 ROTATION moved MATR **UW → N** on the *disqualification* of S36's green-count leg (M238/M273). **S36 has since FIRED-B on its surviving price leg** (XLB 5-day excess vs SPY **+3.12 at registration → −2.72 settled 07-31**), and the flow board agrees on every axis. ⇒ **the N had no surviving support and is reverted.** ⚠ Name-level caveat carried: **NUE (RS20 +16.3, FINRA z −1.40 = the cleanest short-collapse on the desk's pull) and STLD (+13.7)** are the two names that reach the accumulation pre-condition — the sector call is not a name call |

---

## §2b · Changes considered and DECLINED — logged rather than taken

The stage's own rule: *a delta must be carried by a flow number; re-arguing the macro thesis here is
not a delta.* Four candidate moves failed that test and are recorded so "we never looked" stays
distinguishable from "we looked and passed."

| Candidate | Why it was tempting | Why declined |
|---|---|---|
| **Financials OW− → N** | **Δ −0.300 · 🟢2 / 🔴6 of 47 · breadth 0.04**, and **R32 killed the OW's stated "breadth-led" reason** — SWEEP re-tested it today at **all-47 gap +0.0370 vs ex-BRK-B +0.0095**, i.e. **74% of the statistic is one $1,055.7bn row at flow −0.116** | **Declined.** Δ −0.300 ranks **5th worst of 11**, not an outlier, and **XLF is the only sector positive on all three price windows (+0.02 exc5d · +2.07 exc20d · +7.16 exc60d vs SPY)**. Demoting the board's best price on a mid-pack delta would be a **macro re-argument wearing a flow number.** The OW− is held **and its reason is explicitly open** — that is the DEEP mandate, not a verdict change |
| **Comm Services N → N−** | wflow −0.217 (3rd worst) · Δ −0.340 (4th worst) · **exc60d −9.60pp vs SPY, the board's worst 60-day** | **Declined.** eqflow **−0.071 is mid-pack** and exc20d −1.54 is mid-pack — the case rests on the 60-day price window, which is **MACRO's axis, not this stage's.** Logged as *"macro re-argument, declined"* |
| **Cons. Staples N → N−** | **Δ −0.431, 2nd worst on the board** | **Declined.** wflow −0.130 / eqflow −0.126 are **mid-pack**, exc20d −0.23 is flat, and **no proposition in MACRO §D claims Staples at all** — a verdict change on a sector nothing argues is noise |
| **Real Estate N → anything** | **wflow +0.078 / eqflow +0.091 (positive AND breadth-led) with Δ −0.343** — the two halves point opposite ways | **Declined — the instrument is uncallable here.** SWEEP §3 measured RE at **0 🟢 AND 0 🔴 of 12**, with **4 names passing the pre-condition and all 4 blocked** (DLR 0.82 · PLD 1.08 · IRM 1.14 · CBRE 1.17). **A sector with no greens and no reds is an instrument saying nothing, not a market saying nothing.** Held at N and stated |

---

## §2c · Matrix × flow divergences named, with a resolution owner (AGREE is §1, not a paragraph)

| Divergence | Matrix | Flow | Owner |
|---|---|---|---|
| ⛔ **Info Tech — the S30 turn is MEGA-CAP-NARROW** | **N**, restated as "split, now asymmetric" | **wflow +0.081 vs eqflow −0.144 = the widest wflow−eqflow gap on the board (+0.225)**, with **🔴25 of 56 — the worst red count anywhere** — against only 4 greens (MSFT +0.85 · STX +0.80 · MPWR +0.79 · FTNT +0.56) | **DEEP-IT.** The bracket **S30 FIRED-A against the desk** on a median that crossed above zero, and the flow says the participation is four names. **Both are true; DEEP resolves whether the turn is the sector or the quartet** |
| ⛔ **Industrials — best breadth, worst-but-two price** | UW− → **N** (§2) | breadth 0.10 · 5🟢 · eqflow > wflow | **DEEP-INDU** |
| ⛔ **Energy — equities and commodity split inside one bar** | OW− → **OW** (§2) | wflow +0.519, zero reds | **DEEP-ENRG** |
| ⚠ **Utilities — the desk's own two brackets fired in OPPOSITE directions in 48h** | **UW−**, and the flow agrees (wflow −0.284 / eqflow −0.289 · 🟢1 / 🔴8) | ⇒ **no delta; the tape and the flow both hold UW−** | ⚠⚠ **But S35 FIRED-A** (*the demote was wrong* — regulated median crossed to +0.39 on the 07-29 settled close) **and S47 FIRED-B** (*the legs re-converged* — spread +14.74 → +1.88pp) **on the same seven names.** S47's registration pre-committed that **the disagreement is the finding.** **No verdict moves on it — but it is the highest-value unanswered question on the board and it is logged into DEEP_LOG rather than dropped** |
| ⚠ **Cons. Discretionary — the board's ONLY positive delta, and it is one name** | **N+** | **Δ +0.032 (the only positive) · but 🟢1 / 🔴9 and eqflow −0.045 below wflow +0.072 ⇒ mega-cap-narrow** | **Held at N+, flagged AMZN-carried.** The single green is **GRMN (+0.915, the sweep's #1 flow of all 300)** — **and GRMN has had no thesis anywhere for three consecutive runs** |

---

## §3 · DEEP picks and DEEP_LOG

**Recency input, `DEEP_LOG` lines read from disk**: `07-22 [ENRG,FIN]` · `07-23 [ENRG,FIN]/[HLTH]` ·
`07-28 [ENRG,FIN]/[IT,COMM]` · `07-29 [ENRG,FIN]/[INDU]` · `07-30 [ENRG,FIN]/[HLTH,RE]` ·
`07-31 [ENRG,FIN]/[IT,UTIL]`.

### ① Continuous track — ⌈4/2⌉ = 2

- **ENRG** — today's #1 OW; **held a continuous slot in the previous run and is still top-N OW**
  ⇒ **anti-thrash continuity applies and the slot is KEPT** (stated per the rule).
- **FIN** — today's #2 OW; same continuity condition; **and its stated reason is retracted (R32) with
  no replacement that survives SWEEP's ex-BRK-B test.** A continuous slot on a sector whose thesis is
  currently unwritten is the correct use of the slot.

### ② Rotating track — ⌊4/2⌋ = 2

⚠ **The padding prohibition is checked first and it binds in an unusual way this run: only TWO
sectors carry an OW-family verdict (ENRG, FIN), and both are taken by the continuous track.** The
rule says *never pad with Neutral/UW to reach N — fewer is fine if stated.* It also provides the
**recency-starved fallback**: *"if every OW was recently covered → fall back to next-highest
regardless, and SAY recency-starved."* **Both conditions hold simultaneously — ENRG and FIN have held
the continuous slots for six consecutive runs — so the fallback is invoked explicitly rather than
silently.**

- **IT** — *selected against the recency preference, and the reason is stated.* IT held a rotating
  slot on **07-28 and 07-31**, so this is inside the ~3-run window. **It is selected anyway because
  S30 FIRED-A against a carried verdict this run** — the IT-Neutral's own stated defence ("wait for
  the 08-19→09-07 roll-off") is what branch A says is wrong — **and the recency rule is a tiebreak
  among comparable candidates, not a veto on a bracket that just falsified a desk position.**
  **DEEP mandate**: is the turn the sector or the quartet (MSFT/STX/MPWR/FTNT)? **MU is 🔴분산 at
  −0.600 with RS20 −15.9 and did NOT participate**, while STX is 🟢 `new_green`. **W5 binds — this
  basket spans +0.799 to −0.600 and may not be handed forward as "memory."**
- **INDU** — *selected on recency and on this run's own delta.* Last covered **07-29 (2 runs ago)**,
  and it is the **only verdict promoted into the N-or-better band this run.** **DEEP mandate**:
  the board's best breadth (0.10, 5🟢) against the board's 3rd-worst 20-day price (−2.52pp vs SPY) —
  early or trap — **and S42's branch-B second leg is failing at 1 of 4 🟢 while the in-bracket control
  CAT sits at RS20 −15.7.**

### ⚠ OW-family and high-value sectors left WITHOUT a slot — named, not dropped

- **UTIL** — the highest-value unanswered question on the board (**S35-A vs S47-B, opposite
  directions, 48 hours, same seven names**). **Not selected only because it held the rotating slot on
  07-31**; taking it again would repeat the previous run rather than rotate. **First in line next run.**
- **MATR and DISC** — **the two sectors with NO DEEP in the entire 07-22 → 07-31 DEEP_LOG window.**
  They are the genuinely recency-starved pair; **MATR's verdict was just reverted to UW and DISC is
  N+ on one name (GRMN, no thesis, 3rd run).** Logged so the next run's recency rule can see them.
- **HLTH** — demoted **N → N−** this run and last covered 07-30; carried without a slot,
  **re-check 08-06 (C7)**.

## DEEP_LOG 2026-08-02: continuous=[ENRG, FIN] rotating=[IT, INDU] · uncovered=[UTIL(next-in-line), MATR, DISC, HLTH, RE, COMM, STPL]

---

## ✅ EXIT CHECK

- [x] **§1 is ONE line**, inherited verbatim from `MACRO_REPORT.md §E`. No unchanged sector has a row,
      paragraph, or restated flow number.
- [x] **Every §2 delta cites a flow number** (wflow · eqflow · breadth · Δ · 🟢/🔴). **Four changes
      considered and declined are logged in §2b, two of them explicitly as *"macro re-argument,
      declined."***
- [x] Every matrix×flow divergence named with a resolution owner (§2c).
- [x] **N=4 picked by the rule**: continuity stated for both continuous slots; **the padding
      prohibition checked and the recency-starved fallback invoked explicitly**; **IT's selection
      against the recency preference is stated with its reason.** No padding with UW sectors.
- [x] **OW-family and high-value sectors left without a slot are named in DEEP_LOG**, not dropped.
- [x] Linter — see below.
- [x] DEEP_LOG line appended for the next run.
- [x] Delta count is **4**, so the "0-delta short file" branch does not apply — and **no delta was
      manufactured**: §2b records four that were declined.

**Linter**: `python -X utf8 scripts/report_lint.py llm_outputs/2026-08-02/industry_US/SECTOR_ROTATION.md`
→ result appended at run end. ⚠ Form only (C1 · C2 · S6 · D6); a clean run is not a correct report.

---

*asof 2026-08-02 · flow asof 2026-07-31 settled · 4 deltas taken (ENRG↑ · INDU↑ · HLTH↓ · MATR
revert), 4 declined and logged · DEEP N=4. Analysis only, zero buy/sell, zero sizing (P4).*
