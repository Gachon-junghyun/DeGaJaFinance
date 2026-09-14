# HANDOVER — industry_US · 2026-09-08 (Tue) · Stage 2 / L1·HANDOVER

> Read before anything is decided. Inherits the **analytical carry**, not the coverage ledger.
> **Sources read this run.** Shared spines: `handoff/STANDING_VIEW.md` (§5 retracted ledger through the
> 2026-09-08 KR block `R143`–`R146`, §6 open contradictions, the asof chain including the 09-07 US and
> 09-08 KR entries), `handoff/SCENARIOS.md` (master index, the un-split master scoring log, the dated
> settle queue as updated by the 09-07 US run). This desk's halves: `handoff/SCENARIOS_US.md`
> — **parsed mechanically end-to-end by an independently written scanner this run** (156 id-bearing
> headers → **135 distinct ids**; see §3b), `handoff/STANDING_VIEW_US.md`. Method:
> `handoff/RESEARCH.md` Part C (US digs `D553`–`D567` from 09-07; KR digs `D568`–`D571` from this
> morning), `handoff/README.md`.
> **Other-market file opened**: the 2026-09-08 `industry_kr` blocks in both spines — required, because
> that run registered **`D568`** (a benchmark/asset bar-misalignment that biases every `rs20`/`rs60`)
> **fourteen hours before this run started**, and it is the same code path this desk's US sweep uses.
> PREFLIGHT §G0 therefore ran an explicit US-side check for it. See §1.
> Mechanical ledger cross-queried: `module_report_tags show`.
> ⚠ **Read honestly**: the spines total **~3.7 MB**. `STANDING_VIEW.md` §5/§6 were read by targeted
> extraction of the four most recent append blocks; `SCENARIOS_US.md` was parsed **mechanically in
> full** and read **in prose for every row named below**. Stated because "read the spine" and "grepped
> the spine" are different claims (`D528`).
> **P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.**

---

## 0 · The one-line state of this run

**The tape is unchanged for a fourth run — but for a different reason than the last three, and the
new reason is a standing property of this desk rather than a calendar accident.** 09-05 and 09-06
were weekend closures; 09-07 was Labor Day. **Today the market is open — the desk simply runs at
09:11 ET, nineteen minutes before it opens.** `asof` is `2026-09-04` for the fourth time and all 11
sectors are byte-identical to the 09-07 file. ⇒ the price-based work available today is the same
work that was available on Friday, and **every row on today's settle date settles on a close that
has not happened yet** (§3a). What this stage produced instead: an **independently implemented**
re-run of the `D551` back-scan, which found a **fourth** member of the `S16`/`S24`/`S42`
never-scored class the 09-06 run reported as three — **`S13`, unscored for 41 days** — and scored
the half of it that is mechanically scoreable (§3c).

---

## 1 · Instrument health inherited FIRST (`preflight/PREFLIGHT.md`, written 22:09–22:22 KST)

**PREFLIGHT ran and exists.** Its verdicts govern every number below.

| gate | verdict | what it removes from this run |
|---|---|---|
| **G0** | ✅ **PASS — fifth consecutive clean run** (1/301 NaN on all 14 sessions, `EA` only; **partial-NaN 0**). ★ **`SPY` and the 300 names both end 2026-09-04** — the KR desk's `D568` misalignment was checked for **explicitly on the US side this morning** and does not fire here. ★ **No 09-08 partial bar exists** (probed directly at 09:10 ET, pre-open) | nothing, except any verdict on **`EA`** |
| **G1** | 🔴 sweep news axis **17.39%** (52/299) · ✅ direct path 8/8 pre-sweep · ★ mechanism replicated a **5th** time | 🚫 no theme-freshness / velocity / "it is quiet" **from the sweep**, *including* the 52 that scored — they are exactly the 52 largest caps. **Absolute for UTIL / MATR / RE: zero names measured each** |
| **G2** | 🟡 **scale continuous, NOVELTY ZERO for a 4th run** — `asof` 2026-09-04 == the 09-05, 09-06 and 09-07 runs' `asof`; **11/11 sectors identical on 11/11 fields** | 🚫 **Δflow may not be worded as "today's move"**; it is the **09-03 → 09-04** change, now restated four times |
| **G3** | ✅ full 11-row list printed (1 flipper by the flag; **2 by issuer**) | 🚫 no `wflow` verdict on **Cons. Disc.** (AMZN 40.2%) or **Comm. Services** (Alphabet 76.6% under two tickers) |
| **G4** | 🔴 **12 / 11 / 10** units across 250/500/750d, ARI **0.3874 / 0.2328 / 0.7937** | 🚫 no single-number concentration claim; `--days` on the same line |
| **G5** | 🔴 universe **55 days** stale (cover ✅ 11/11, missing 0) | 🚫 no cap-weight / sector cap share / `top1_w%` / issuer share cited as current |
| **G6** | 🔴 accrual **0.57/day, 1.75×** slow | `kelly_size --ic` is "mechanical 1/4" if used at all |
| **G7** | 🟡 **51/53** `--help` clean; chart live 3/3 | 🚫 no `margin_history` output |

★ **The one gate reading that MOVED, and it moved in this run's favour.**
G1's recovery observation: the 09-07 run's 20s polling produced **0/5 through t+100s** and left a
hypothesis it could not separate — *is the outage longer, or does each failed probe reset the idle
timer?* This run followed `D553`'s own prescription and **did not poll**: it left the endpoint alone
and found it **alive (2/2) after ~5 minutes**. That is **consistent with** the idle-timer reading and
inconsistent with nothing — it is one observation at a different burst size and **is not the
controlled test** `D553` asks for. Recorded as a partial, not a closure.

★ **The gate reading that did NOT move, and is the more important one.** The wall stayed at rank
**52** (history 49 → 50 → 52 → 52) and the sector coverage of the measured 52 was **recomputed, not
carried**: IT 20/56 · COMM 4/12 · STPL 5/19 · FIN 9/47 · HLTH 5/32 · ENRG 2/16 · DISC 3/28 ·
INDU 4/50 · **MATR 0/12 · UTIL 0/15 · RE 0/12**. Three sectors are unmeasurable on news for a fifth
consecutive run.

⇒ **Standing implication, inherited into every later stage**: the price tape is four runs stale, and
today that staleness is **structural, not calendrical**. Whatever is genuinely new today must come
from the **non-price instruments** — and unlike yesterday those are actually live: Labor Day
suppressed Monday's US macro releases and filings, so **today is the first day since Friday that
FRED, EDGAR and the US news wire can carry anything new.** MACRO must go there.

---

## 2 · Retracted ledger read BEFORE forming today's view (`STANDING_VIEW.md` §5)

Read through the 2026-09-08 KR block. The four newest entries are **KR-owned** — `R143` (*"`wflow ≈
eqflow` is the signature that a sector is NOT one name"*, killed four hours later by its own DEEP),
`R144` (a single-instrument zero recorded as an anti-signal, twice), `R145` (a ±30% band between two
instruments that do not share a unit), `R146` (the quoted-juxtaposition workaround fails at the
**token**, not the query syntax, for 2-character terms). **`W1` bars this desk from importing any of
them as conclusions.** They are recorded as read, not used.

★ **One of them is nevertheless load-bearing here, and the reason is mechanical rather than
analogical.** `R143`'s **replacement rule** — *"`wflow ≈ eqflow` is the signature that the
cap-weighted top is NEUTRAL, which is a different statement from breadth; to separate them, measure
the 🟢 names' share of sector market cap"* — is a statement about **the shared scoring code**, not
about the Korean market. It is carried forward as a **method** constraint on ROTATION (§5), which is
what `W1` permits; the KR *verdicts* it produced are not carried.

**The four newest US retractions** (`R139`–`R142`, all 09-07) are re-read and each is checked against
this run's own output: `R139` (share-normalised term counts uninterpretable) — **binds MACRO today**,
because `P141`'s falsifier is scheduled for **this run** and `D557` says it will not find what it was
built to find; `R140` (the `names` array is `flow_score`-sorted) — **applied**, this run's wall was
computed through `us_top300.csv` `rank` from the first attempt; `R141` (`P141`'s cause replaced, its
observation intact); `R142` (`MSTR` was not the board's momentum extreme once volatility-normalised)
— **directly relevant**, because `MSTR` is the one row the opportunity-cost ledger surfaced today
(§3b′).

**Checked against this run's own output**: no claim below matches a retracted entry.

---

## 3 · Scenario scoring

### 3a · Five rows settle TODAY, and **none of them is scoreable at this run's clock**

The dated settle queue's 09-08 cell (as written by the 09-07 run) holds **`S127` · `S140` · `P122` ·
`P123` · `P128`**. Every one of them was read in prose this run. Their frozen observables:

| row | frozen observable | why it cannot be scored at 09:11 ET |
|---|---|---|
| **`S127`** | `AVGO` 5-session excess vs `SPY`, **09-01 close → 09-08 close** | the terminal close is 6h19m away |
| **`S140`** | COUNT of the 56 IT names with positive 5-session excess vs `SPY`, **at the 09-08 close** | same |
| **`P122`** | (A) `[COT]` for 09-08 WTI spec 1-yr pctile ≥65 **AND** `CL=F` close ≥88.00 on that date; (B) `CL=F` close ≤80.00 on or before 09-08 | same — **and see the asymmetry below** |
| **`P123`** | `EW{SLB,ETN,NEE,VRT}` − `SMH`, 5-session sum, first settled close after 09-01 → **09-08** | same |
| **`P128`** | `hy_oas` `[FRED]` 5-session change in bp, at the **first `[FRED]` close covering 09-08** | FRED has not published 09-08; `D427` says the H.15 legs will lag further |

★ **This is a standing property of the desk, not today's accident, and it is being written down for
the first time.** The `industry_US` runtime fires at **22:00 KST = 09:00 ET**, i.e. **always before
the US open**. Therefore **a row whose observable terminates on the close of date `D` can only be
scored by the run of `D+1`.** Nothing is lost by this — the 09-09 run will find all five past-dated
and score them — but it means:
1. the queue's "next cell = today" is **never** an instruction to score today; and
2. a row registered to settle on the **last** day before a multi-day closure is unscoreable for the
   whole closure plus one.
Registered as **`D572`**.

★ **One branch can nevertheless be bounded on already-settled data, and bounding is not scoring.**
`P122` branch **B** requires a `CL=F` **settled close ≤ 80.00** on or before 09-08. Settled closes
since the registration state: **08-31 85.76 · 09-01 90.22 · 09-02 91.01 · 09-03 91.30 · 09-04
91.48** (window min **85.76**). For B to fire, 09-08 must close at or below 80.00, i.e. **−12.55%
in one session** from Friday's 91.48. ⇒ **B is arithmetically all-but-closed.** This is stated as a
**bound with its arithmetic shown**, explicitly **not** as a verdict (`D531` — an interim tracking
line that reads like a verdict is the defect, and this desk's pre-settle reads are on record as
**0 for 4**).

★ **And `P122` carries the `D556` asymmetry in a new form.** Its branch A has **two legs that settle
on different days**: the `CL=F` price leg settles at the 09-08 close, but the **`[COT]` positioning
leg for 09-08 does not publish until the CFTC's Friday release (~09-11)**. So A is unscoreable until
09-11 while B is decidable on 09-08. **A row can therefore be simultaneously past-settle and
unscoreable, without anything being broken.** This is `D556`'s pattern (asymmetric leg degradation)
in its **third** observed form — price-vs-fundamental (`S14`), price-vs-categorical (`S13`, §3c), and
now **price-vs-positioning-release-calendar**. Registered as **`D573`**.

### 3b · The `D551` back-scan, re-implemented independently — and it found a fourth row

`D551` (registered by the KR desk 09-07, reproduced on the US file by the 09-07 US run) says a
verdict may be confirmed **only** by a table row whose **first cell** is that id. This run wrote a
**new scanner from scratch** rather than reusing yesterday's, deliberately, to test whether the
finding is a property of the rule or of yesterday's implementation.

| stage | count |
|---|--:|
| id-bearing headers parsed in `SCENARIOS_US.md` | **156** |
| distinct ids | **135** |
| past-dated (settle < 2026-09-08) whose **header** carries no verdict token | **89** |
| of those, **no first-cell verdict row anywhere** in `handoff/*.md` ∪ `llm_outputs/**` ∪ `REPORT/**` | **12** |
| resolved on prose inspection (verdict exists, id not in a first cell) | **11** |
| ⇒ **genuinely never scored** | **1 — `S13`** |

The 11 resolved: `S16` · `S24` · `S42` (already `EXPIRED-UNSCORED` with reasons, 09-06 run — **not
re-litigated**, `P5`) · `S23` · `S26` (condition-settled rows, buffers re-measured by the desk that
owns them) · `S31` (`AMBIGUOUS`, twice) · `S50` (verdict lives on `S50-KR`) · `S54` · `S73` · `S81`
(verdicts in prose/master-index rows) · `P121` (blocked by `D427`, named every run since 09-04 —
**5th consecutive blocked run**, see §3e).

⇒ **`D551` is a property of the rule, not of an implementation**: an independently written scanner
reproduces the class and adds a member yesterday's did not name. Filed as **`M1452`**.

### 3c · `S13` scored — 41 days late, and only half of it was ever scoreable

**`S13`** (registered 2026-07-23 by PREMORTEM, settle 2026-07-29, observable measured over the **10
sessions after the print, to ≈2026-08-12**). Three legs, all frozen at registration:
(1) the **capex guide** at MSFT and META (raised / held / cut); (2) the **spenders'** NTM P/E change;
(3) the **suppliers'** (MU, AMAT, LRCX, KLAC) median **RS20 vs SPY**.

**Leg 3 — suppliers, measured on settled closes this run** (`auto_adjust=False`, benchmark named per
`C1`):

| date | MU | AMAT | LRCX | KLAC | **median** |
|---|--:|--:|--:|--:|--:|
| 2026-07-29 (print) | −33.66 | −37.32 | −39.45 | −41.27 | **−38.38** |
| 2026-08-12 (+10 sessions) | −1.57 | −7.74 | −5.12 | −9.58 | **−6.43** |

⇒ the supplier median **rose 31.95pp but never crossed zero.** Leg 3's condition is *"turns
positive"* — **NOT MET**, and not marginally: **every one of the four is still negative** on the
terminal date.

**Leg 2 — spenders' NTM P/E, from this repo's own `data/estimates/` accrual** (the instrument `D16`
exists to build), price ÷ `eps_trend['+1y'].current`, both legs post-print so the fiscal roll is not
straddled:

| name | 07-31 price | 07-31 +1y EPS | P/E | 08-12 price | 08-12 +1y EPS | P/E | change |
|---|--:|--:|--:|--:|--:|--:|--:|
| MSFT | 464.72 | 23.085 | **20.13** | 492.43 | 23.553 | **20.91** | **+3.9%** |
| META | 556.71 | 34.408 | **16.18** | 578.85 | 33.948 | **17.05** | **+5.4%** |

⇒ the spenders' multiple **EXPANDED at both.** Leg 2's condition is *"compresses"* — **NOT MET.**
⚠ **Instrument caveat stated rather than hidden**: MSFT's `+1y` series jumps **19.38 → 23.08** between
the 07-27 and 07-31 snapshots. That is a **fiscal-period roll, not a revision**, and any P/E change
computed **across** it would be fabricated. Both readings above are taken **after** the roll. Filed
as **`D574`**.

**Leg 1 — the capex guide — is where this row dies, and the cause is a registration defect.** The
categorical wording is *raised / held / cut*. What the admissible feed (`--scope foreign`,
**body-read**, not title-read) actually returns for the 07-29/07-30 prints:
- **META** — *"reported weaker-than-expected earnings and **narrowed its expectations** for 2026
  capital expenditures"* [barrons via yahoo_finance, 2026-07-30]. ★ The **headline of that same
  article** reads *"Meta Stock Falls Sharply on Weak Earnings and **CapEx Boost**"* — **the title and
  the body of one article point in opposite directions.** This is `R134`/`D541`'s prescription
  (body-read, never title-read) earning its keep on its first US use.
- **MSFT** — *"**Lower-Than-Expected Q4 Capex**, Strong Azure Sales Boost Sentiment"*
  [yahoo_finance, 2026-07-29]. "Lower than **expected**" is a statement about **consensus**, not
  about the **guide's direction**, which is what the row froze.
⇒ **Neither name yields a documented *raise* or a documented *cut*.** Widening "narrowed" or
"lower-than-expected" into "raised" or "cut" is precisely the improvisation `D242` forbids.

**Verdict — `S13` = `A-RULED-OUT · B/C AMBIGUOUS`.**
- **Branch A is definitively dead** on the two **measured** legs alone, independent of the categorical
  leg: the multiple expanded (not compressed) **and** the supplier median stayed negative (did not
  turn positive). ⇒ **the row's high-information claim — *"Info Tech's single N label is wrong on
  BOTH halves at once, IT must be split"* — did NOT fire.**
- **B vs C cannot be separated** because their discriminator is the unresolvable categorical leg.
- ⇒ recorded in the `S31` **`AMBIGUOUS`** class — **its third instance on this desk**, and the second
  time (`S14` was the first) that a bracket's **price legs scored cleanly while its non-price leg was
  unretrievable**. Filed as **`M1453`**; `D556` gets its **second** independent instance.

⚠ **What this verdict does NOT license.** It says nothing about whether `IT` should be split. It says
the **specific triple-legged test** the desk registered to answer that question **produced no answer
on two of three legs and a dead branch on the third**. `D566` (there is no sector-level fact in IT to
attach a verdict to; `IT N→UW` declined seven times on seven reasons) is **unaffected and unhelped**.

### 3d · What this run did NOT score, and why

- **`S128`** · **`S129`** — settle **2026-09-09**, not due. Verified against their own registrations,
  not against the queue alone (the 09-07 queue carried them with an asterisk on both dates).
- **`S130`** · **`P127`** — settle **2026-09-10**. Not due.
- **`S16`** · **`S24`** · **`S42`** — `EXPIRED-UNSCORED` with reasons by the 09-06 run. **Not
  re-litigated** (`P5`).
- **`S5`** — reassigned by name to `industry_kr` by the 09-07 run (`W1`). **Not re-claimed here.**
- **`S8`** — **42nd consecutive run unscoreable**, date field still `[blank]`. Human `VOID` or
  re-registration (`P5`). The 42nd writing of this line is the finding.

### 3e · `P121` / `P114` / `P125` — `D427`'s 9th reproduction, and today is the day it should break

These three settle at *"the first `[FRED]` close covering 2026-09-04"*. They have been blocked for
**five consecutive runs** because H.15 splits its publication and does not publish on a federal
holiday. **Today is the first business day after that holiday**, so the H.15 legs (`DGS2`/`DGS5`/
`DGS10`/`DGS30`/`DFII10`) should finally carry **09-04**. ⚠ **This stage does not pull FRED** — that
is MACRO's instrument and MACRO must check it and say so either way. **Handed forward as a named
obligation, not an assumption**: if MACRO finds the legs still stopped at 09-03, that is `D427`'s
**9th** reproduction and a **6th** blocked run; if it finds 09-04, the three rows become scoreable
**by MACRO in this run** and must not be deferred to 09-09.

### 3f · Scoring tally for this stage

**Newly scored 1** (`S13`, half — A ruled out, B/C ambiguous with the reason named) ·
**bounded-not-scored 1** (`P122` branch B, arithmetic shown) ·
**due-today-but-structurally-unscoreable 5** (`S127`/`S140`/`P122`/`P123`/`P128`, §3a, with the
reason registered as `D572`) · **blocked-and-handed-forward 3** (`P121`/`P114`/`P125` → MACRO §3e) ·
**not-due, verified against registration 4** (`S128`/`S129`/`S130`/`P127`) · **silent skips 0.**

⚠ **`S13`'s verdict is transcribed into `handoff/SCENARIOS.md`'s MASTER SCORING LOG *inside this
stage*, not deferred to run end** — following the 09-05/09-06/09-07 precedent, because `M1352`'s
measured failure mode is precisely that the scoring log is the writeback target that gets dropped.

---

## 3b′ · Both ledgers audited — and this run has the first `due` row in twenty runs

| ledger | total | resolved | **legacy (no revive/enter condition)** | **due today** |
|---|--:|--:|--:|--:|
| `reject_ledger.py due` | **309** | 193 | **0** | **0** |
| `missed_ledger.py due` | **345** | 217 | **0** | **1 — `MSTR`** |

- **Legacy 0/0 for a 20th consecutive run.** ✅ The stage's own warning is honoured: a clean `due` is
  not proof of health; the **legacy counter** is, and it has been at zero since the class was closed.
- ⚠ Totals moved **303 → 309** rejections and **337 → 345** misses since the 09-07 US run. The six
  new rejections and eight new misses were filed by the 09-08 KR run, not by this desk. **`C22`**
  (the two ledgers name different hands) carried, **20th run**.
- ⚠ **The two ledgers' `excess` signs are inverted and were not summed.**

### The `MSTR` row — re-pulled, measured, and **explicitly named as still-pending with the reason**

Row: `2026-08-24 · MSTR · MicroStrategy · [Q.확신부족] · entry condition: **rs60 turns ≥ 0 AND OBV
stays accumulating**`. First appearance in `due` — it is **not** a second silent carry.

**Re-pulled this run** (settled closes to 2026-09-04, sweep `asof` 2026-09-04):

| leg | instrument | reading | condition met? |
|---|---|---|---|
| `rs60` ≥ 0 | `SECTOR_FLOW_US.json` (`MSTR` **is** in `us_top300`, rank-scored) | **+17.6** | ✅ **YES** — and `rs20` **+43.2** |
| `rs60` ≥ 0 | direct yfinance recompute vs `SPY`, 60 sessions | **+17.63** (MSTR +23.80% vs SPY +6.17%) | ✅ **YES** — two instruments agree to 0.03pp |
| OBV accumulating | sweep | `obv_state` **매집**, `obv_norm` **+0.326** | ✅ yes |
| OBV accumulating | `module_chart --read` | **중립**, 20d slope **+2%** | 🟡 **weakly positive, labelled neutral** |

⇒ **The `rs60` leg is unambiguously met on two independent instruments. The OBV leg is met on one
instrument and labelled neutral by the other — `C25` reproducing, on this exact name.** Both readings
carry the **same sign**; they disagree on **label strength**, not direction. Under `D6` (OBV is a
**C-grade** signal) the honest statement is: **the registered entry condition reads as MET, with its
decisive leg resting on the desk's lowest-graded axis.**

🚨 **This run did NOT call `missed_ledger resolve`, and the reason is a defect in the ledger's own
vocabulary, not an evasion.** The available outcomes are `entered` / `reaffirmed` / `expired`.
- `reaffirmed` ("stays out on fresh evidence") would be **a false record** — the evidence says the
  condition fired.
- `entered` is **a book action**, which this desk does not take (`P4`; the book is `P5`/human).
- `expired` is false — the condition is live.
⇒ **There is no outcome value for *"the pre-registered condition is MET, and the decision that
follows is not this desk's to make."*** Named here in full, per the stage's sanctioned alternative
("explicitly named as still-pending in `HANDOVER.md`"), and registered as **`D575`**.
⚠ **If this row surfaces in `due` again on 09-09 without a resolution path, that IS the process
failure** — the second carry, not this one.

⚠ **`R142` binds the reading of this row**: `MSTR`'s +46.7% 20-day momentum, retracted yesterday as
the board's momentum extreme, is **z = +1.53** on a 6.27% daily σ — the **least** extreme of the
three biggest raw runners. The entry condition is met; the *"it already ran"* framing that kept it
out is the part that was measured wrong.

🚨 **`C27` / `D463` — `MSTR`'s two opposite rejections remain unexamined for a 6th consecutive run.**
`reject_ledger due` surfaces them **09-18 / 09-22**. ★ It is now sharper than "the desk waits for the
tool": **the opportunity-cost ledger says `MSTR`'s entry condition fired today, while the rejection
ledger holds two contradictory rejections of the same name that nothing will look at for ten more
days.** Named, not dropped.

---

## 3c′ · Exposure state read and carried (size context for BET / ALPHA)

`exposure_rule show` — **`live` / `정상`**, latest row **2026-09-08** (today's row exists):

| field | value |
|---|---|
| verdict (4-state) | **정상** (normal) |
| stored invested % | **85.2%** (last populated **2026-09-04**) |
| **current invested %** | 🚨 **BLANK — `투자비중미상(계좌조회 없음)`, `timefolio조회실패:CDPError`** |
| cumulative excess (simple sum, **n = 18**) | **−9.79pp = cash −5.32pp + selection −4.47pp** |
| band | 🚨 **밴드이탈 −9.8pp** on the last populated row (09-04) |
| arming | 🚨🚨 **ARMED (`TIMEFOLIO_EXECUTE=1`)** — standing human item (`P5`) |

- **Not a cold start** (18 scored days), so the verdict is quotable — **but the current-invested-%
  field is now empty for a THIRD consecutive run** (09-07, and today's 09-07+09-08 rows both carry
  `CDPError`). ⇒ **BET/ALPHA may cite the 85.2% only as a *stored* value with its 09-04 date
  attached, never as "current".**
- ⚠ **`n` has been flat at 18 for seven calendar days.** The stated purpose of this ledger is to raise
  `n` by one per day; it has raised it by **zero in a week**, and the cause is the same account-query
  failure. The tool's own line — *"n≈20 in a month, and only then may you ask about the sign (`C4`)"*
  — is receding, not approaching. Carried.
- **`C23`** (three books, none self-identifying) — **11th reproduction**: `exposure_rule` target 95% ·
  `show` stored 85.2% · `state` current **blank** · `module_paper_book status` total **₩17,791,092**
  with `028050`/`316140` marked `n/a` on price.

---

## 4 · Stale-check — every carry has an expiry

| carry | asof | age at this run | verdict |
|---|---|--:|---|
| Sweep flow table (all 11 sectors) | **2026-09-04** | **4 runs, 0 new sessions** | 🚫 **not stale — but not new either.** May be cited only with the **09-03→09-04** label |
| `us_top300.csv` cap vector | 2026-07-15 | **55 days** | 🔴 **stale.** Equal-weighted readings govern where the two disagree |
| `M1361` — distillate crack 3-session **−$7.02/bbl = 6.0th pctile** while its **level is 95.6th** | 2026-09-04 | 4 sessions, no new data | carried **unchanged with `D565` attached**: the sign **changes with the window** (3-session 6.0th pctile · 5-session 45.6th · quarterly +40.5%). **`P140` settles on the 5-session leg**, not the 3-session one `M1361` quotes |
| `M1364` (raw leg) — 17/17 carried terms fell on raw counts | 2026-09-06 | 2 days | ✅ **raw leg stands**; the **share-normalised leg is RETRACTED** (`R139`, `D557`) |
| `P141` — *"re-run the 17 terms on a window ending on a full weekday, next opportunity **2026-09-08**"* | 2026-09-06 | **DUE TODAY** | ⚠ **The test is due this run and its stated cause is already superseded** (`R141`). MACRO must run it **and** report it under `D557`'s constraint: RAW counts + inter-term dispersion, denominator from the **same** tool |
| `MU` FQ4 date | `D488`-corrected to **2026-09-30 16:00 ET** | — | carried; three sources gave three dates, `Ticker.earnings_dates` governs |
| **`D564` live commitment** | registered 09-07 | — | 🚨 **the FOMC + SEP (2026-09-16) bracket must be registered by the 2026-09-11 run at the latest.** Deferred on 09-06 and 09-07 with valid reasons. **Today is the third opportunity and there are three runs left.** Handed to PREMORTEM |
| **Suspensions cleared** | — | — | **none cleared this run** |

---

## 5 · Method rules loaded as binding constraints (`RESEARCH.md`, by firing moment)

Loaded, not summarised. The ones that bind **this** run, with why:

- **`C1` baseline named · `C2` both halves · `C4` "indistinguishable"** — bind §3c. `S13`'s supplier
  leg quotes **all four names on both dates** and names `SPY` as the benchmark on the same line;
  the spender leg quotes **price, EPS and the quotient** rather than the quotient alone.
- **`C3` unknown column ≠ zero** — binds §3c leg 1: *"lower than expected"* is a **consensus** column,
  not the **guide-direction** column the row froze. It is recorded as unknown, not as "held".
- **`C5` arbitrary choice** — binds G4 (12/11/10 by `--days`; 0.65 threshold itself load-bearing) and
  `R145`'s KR lesson about bands between instruments that do not share a unit.
- **`S1` date-fold · `S5` short samples** — bind G4's 250d window (249 < 250, ARI **0.3874** against a
  flattering **+0.8511** fit). ★ And `D568` gave `S1` its most expensive instance this morning:
  *"identical to yesterday"* was **not** evidence of stability, it was evidence that a defect was
  unobservable while two series happened to align. **PREFLIGHT §G0 checked for exactly that on the US
  side rather than inheriting the reassurance.**
- **`D5` cross-provider · `D6` signal grade (OBV is **C**)** — bind §3b′: the `MSTR` OBV leg is
  `C`-grade and the two instruments disagree on its **label** (`C25`). The `rs60` leg, which two
  instruments agree on to 0.03pp, carries the weight.
- **`D1` second listing venue** — binds G3: Alphabet's **two share classes** are why the built-in
  `top1_flips_sign` prints `False` on a 76.6% single-issuer sector (`D459`, **13th** reproduction).
- **`W1` cross-market transfer** — **binds hard today, twice**: (i) `R143`–`R146` are read and their
  **conclusions** are not used, while `R143`'s **shared-code method rule** is (§2); (ii) `S5` stays
  reassigned to KR.
- **`W3` real ≠ profitable · `W5` sub-sector dispersion** — flagged forward to DEEP. `D566` measured
  IT's dispersion-to-move ratio at **4.6×** and Utilities' at **≈23×**; a sector verdict on either is
  a verdict on an object that does not exist at sector level.
- **`L3` branch information content** — binds PREMORTEM: `S13`'s post-mortem is that **two of its
  three legs were unmeasurable or unretrievable at settle**, which is an information-content failure
  registered *at registration time*, not at scoring time.

### Dig list ranked for today (the DEEP / PREMORTEM candidates)

| rank | dig | why today |
|---|---|---|
| 1 | **`D564`** *(attach a deadline to every deferral)* | 🚨 **live commitment**: FOMC+SEP 09-16 bracket must be registered **by the 09-11 run**. Three runs left. → PREMORTEM |
| 2 | **`P141` + `D557` + `R139`** *(term-count denominators)* | **the test is DUE TODAY** and its stated cause is already superseded. → MACRO |
| 3 | **`D427`** *(H.15 split publication)* | **today is the first business day after the holiday** — `P121`/`P114`/`P125` either become scoreable in MACRO or reproduce a **9th** time. → MACRO |
| 4 | **`D563`** *(build the universe from cycles, not only index ∪ holdings)* | ★ **a scoring exposure, not only a measurement one**: `TLN`/`NRG` sit inside `P127`'s basket, a **LIVE row settling 09-10**, and are absent from `us_top300.csv`. Also every LNG name. → SWEEP/DEEP |
| 5 | **`D561`** *(the 🟢 tag's gate is rank-dependent)* | binds SWEEP directly — the tag falls back on `velocity`, which exists only for ranks 1–52 while `vel_axis` is `false`. Mis-measured **three** sectors last run |
| 6 | **`D551` → `M1452`** *(verdict-grep is not verdict confirmation)* | ✅ **worked again today** — an independent implementation found a **fourth** never-scored row. Carry the **method** |
| 7 | **`D556` → `D573`** *(register the retrieval path / the settle calendar for every non-price leg)* | **two new instances today**: `S13`'s categorical leg, `P122`'s COT-release leg |
| 8 | **`D566`** *(dispersion-to-move ratio as the unit-of-analysis test)* | `IT N→UW` declined **7** times on 7 reasons. **Human-owned protocol change (`P5`)** — carried, not acted on |
| 9 | **`D507`** *(no US market holidays in `catalyst_calendar`)* | **yesterday was the holiday.** Every N-session window written off `--days` is mis-dated unless 09-07 is excluded by hand — **this bites today, not yesterday** |
| 10 | **`D379`** *(PREFLIGHT should read §5 first)* | **12th run unwired**; order kept by hand again |

---

## 6 · Open contradictions carried (`STANDING_VIEW.md` §6) — none resolved by picking a side

| id | state at this run |
|---|---|
| **`C29`** an axis with opposite signs on two instruments (`vol_surge`) | 🚨 **carried, and the KR desk hardened it this morning**: `D570` records that `vol_surge` h=1 has passed **Bonferroni for six consecutive runs with a NEGATIVE sign** while `sector_flow`'s 🟢 gate weights it **positive**. **Not changed** (`P4`) — but every 🟢 tag this run reads carries that known sign conflict |
| **`C25`** two instruments read OBV's sign oppositely | **carried, and it landed on today's one decision-relevant name** (`MSTR`, §3b′). Signs agree; labels do not |
| **`C23`** three books, none self-identifying | **11th reproduction** (§3c′) |
| **`C24`** copper spec at the 100th percentile vs a Materials bucket | **11th run.** ⚠ MATR has **zero** news-measured names for a 5th run, so no "the story is absent" reading is available |
| **`C27`** `MSTR`'s two rejections disagree | **6th run unexamined** (`D463`) — and now colliding with a fired entry condition on the other ledger (§3b′) |
| **`C22`** the two ledgers name different hands | **20th run**, legacy **0/0** |
| **`C21` · `C10` · `C26` · `C28`** | carried; `C26` closed-by-disappearance for a 5th run |
| **new contradictions opened this run** | **0.** Today's findings are **defects** (`D572`–`D575`), not contradictions. Opening a `C` is the easy side and this run deliberately did not |

---

## 7 · What this run asserted and then refuted, written down not edited away (§4c · `D48`)

1. ★ **This stage's first back-scan reported `S13` among 12 "never scored" rows and treated all 12 as
   candidates for scoring.** Prose inspection refuted 11 of the 12 within the same stage — their
   verdicts exist, just not in a first cell. **The 12 is left standing and the 1 is written beside
   it.** The lesson is the mirror image of `D551`: the strict rule has a **false-positive** rate as
   well as a false-negative one, and it must be followed by a prose read, not trusted alone.
   Registered as **`D576`**.
2. ★★ **This stage's first read of the `S13` capex leg took the article headline — *"Meta Stock Falls
   Sharply on Weak Earnings and CapEx Boost"* — as evidence that capex was RAISED.** The **body of
   the same article** refuted it: *"narrowed its expectations for 2026 capital expenditures."* Had the
   headline been trusted, `S13` would have been scored **`FIRED-B`** instead of `AMBIGUOUS`, on a leg
   the feed cannot actually resolve. `R134`/`D541` (body-read, never title-read) was registered by
   the KR desk and **this is its first measured US save.**
3. ⚠ **This run's opening framing of the stale tape was *"the fourth run in a row the market was
   shut."*** It is wrong: **the market is open today** and the desk is simply early. The corrected
   framing is in §0 and the defect is `D572`. **The wrong sentence is recorded, not deleted** — it is
   the exact class of error `D4` (regime contamination by an inherited label) warns about, applied to
   a calendar rather than to a data window.

---

## 8 · Registrations this stage makes (transcribed to `handoff/` at run end)

| id | type | statement |
|---|---|---|
| **`M1452`** | measured | **`D551` is a property of the RULE, not of one implementation.** An independently written scanner (156 headers → 135 ids → 89 past-dated unverdicted headers → 12 with no first-cell verdict row) reproduces the class and names a **fourth** never-scored row, `S13`, which yesterday's scan did not surface |
| **`M1453`** | measured | **`S13` = `A-RULED-OUT · B/C AMBIGUOUS` at 41 days.** Supplier median RS20 vs `SPY` **−38.38 → −6.43** (never crossed zero; all four names still negative) and spender NTM P/E **EXPANDED** (MSFT 20.13→20.91, META 16.18→17.05) ⇒ **branch A dead on measured legs alone.** B vs C is separated only by a categorical capex leg the admissible feed does not resolve |
| **`M1454`** | measured | **The `MSTR` opportunity-cost entry condition FIRED.** `rs60` **+17.6** (sweep) / **+17.63** (independent recompute vs `SPY`) — two instruments agreeing to 0.03pp — with `rs20` **+43.2**; OBV **매집 / +0.326** on the sweep and **중립 / +2% slope** on `module_chart` (same sign, different label, `C25`) |
| **`D572`** | defect | **The `industry_US` runtime fires at 09:00 ET, before the US open ⇒ a row whose observable terminates on the close of date `D` is structurally unscoreable by the run of `D`.** Five rows sat on today's settle cell and none could be scored. **Prescription: the settle queue must carry a "scoreable from" date, which is `settle + 1 run`, not `settle`** |
| **`D573`** | defect | **A bracket's legs can settle on different CALENDARS, not just different instruments.** `P122`-A pairs a `CL=F` close (settles 09-08) with a `[COT]` positioning read for the same date (**publishes ~09-11**) ⇒ the row is past-settle and unscoreable simultaneously. `D556`'s third form. **Prescription: register each leg's publication date, not only its observation date** |
| **`D574`** | defect | **`data/estimates/`'s `+1y` field ROLLS fiscal periods without a marker** — MSFT **19.38 → 23.08** between the 07-27 and 07-31 snapshots is a period roll, not a revision. Any multiple or revision series computed **across** a roll is fabricated, and nothing in the file says where the rolls are. **Prescription: store the period end-date alongside the value** |
| **`D575`** | defect | **`missed_ledger resolve` has no outcome for *"the pre-registered condition is MET and the decision that follows is not this desk's to make."*** `entered` is a book action (`P4`/`P5`), `reaffirmed` would be a false record, `expired` is false. Origin: `MSTR` 2026-08-24, first `due` appearance. **Prescription: add `condition-met-handed-up`** |
| **`D576`** | defect | **`D551`'s strict first-cell rule has a FALSE-POSITIVE rate too** — 12 flagged, **11** had verdicts in prose or in master-index rows. **The rule finds candidates; only a prose read produces the verdict.** Recorded so the next run does not treat the scanner's output as a finding |

---

## ✅ EXIT CHECK — HANDOVER

- [x] Shared spines read by structure + targeted extraction of the four most recent append blocks;
      **`SCENARIOS_US.md` parsed mechanically end-to-end by an independently written scanner (156
      headers / 135 ids)**; `STANDING_VIEW_US.md` and `RESEARCH.md` Parts A/B/C loaded as binding
      constraints (§5); **other-market file opened** (the 09-08 KR blocks — required, because `D568`
      is a shared-code defect); `module_report_tags show` cross-queried.
- [x] **Retracted ledger read BEFORE forming today's view** (§2). `R143`–`R146` (KR) read and their
      conclusions **not** imported (`W1`); `R139`–`R142` (US) applied — `R140`'s method was used from
      the first attempt this run.
- [x] **Every past-dated scenario scored or explicitly accounted for** — 1 scored (`S13`, half, with
      the unresolvable leg named), 1 bounded-not-scored with its arithmetic (`P122`-B), 5 named as
      structurally unscoreable at this clock with the cause **registered as a defect** (`D572`), 3
      blocked and **handed forward to MACRO with an obligation to report either way**, 4 verified
      not-due against their own registrations, **0 silent skips**.
- [x] **`reject_ledger.py due` run** — 0 due, legacy **0**, totals reported (309/193).
- [x] **`missed_ledger.py due` run** — **1 due (`MSTR`)**, re-pulled on two instruments, measured, and
      **explicitly named as still-pending with the reason** (the ledger has no truthful outcome value
      — `D575`). Signs **not** summed with the rejection ledger.
- [x] **Exposure state read and carried** with its 4-state verdict, the **blank current-%** flagged 🚨
      for a third run, and the cumulative cash/selection split at **n=18, flat for seven days** (§3c′).
- [x] 🚨 **Instrument health inherited before any number was trusted** (§1); every FAIL's revoked
      claim-right is restated here, not merely referenced. The KR desk's `D568` was **checked for on
      the US side** rather than assumed absent.
- [x] **Three claims this run asserted and then refuted are written down, not edited away** (§7) —
      including one that would have produced a **wrong verdict** on `S13`.
- [x] Stale rows flagged with their `asof`; the one **live commitment with a deadline** (`D564`,
      FOMC+SEP by the 09-11 run) is surfaced at rank 1 of the dig list.
- [x] `[measured]` / `[inferred]` tags preserved. No `[inferred]` claim is passed downstream as
      evidence.
- [x] No position sizing, no buy/sell language anywhere (P4).

---

> P4 — nothing above is a market call, a name-level verdict, or a size. Scenario verdicts are
> *scores against pre-registered thresholds*, which is the opposite of a new view. `MSTR` appears as
> a **ledger row whose pre-registered condition was re-measured**, not as a recommendation.
