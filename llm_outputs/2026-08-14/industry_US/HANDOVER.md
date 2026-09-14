# HANDOVER — industry_US · 2026-08-14 · Stage 2/11 (L1·HANDOVER)

> Inheritance step. Reads `handoff/` (the analytical carry), scores every past-dated bracket, audits
> both ledgers, loads the RESEARCH triggers as binding constraints, and hands a rights table to MACRO.
> **No sizing, no buy/sell language anywhere in this file (P4).**

## 0. Run clock — and the one thing it settles

**KST 2026-08-14 22:10–23:0x = ET 2026-08-14 09:10–10:0x, Friday, PRE-OPEN** (US cash opens 09:30 ET).

★ **The 2026-08-13 settled close now EXISTS.** That single fact is what this run inherits: the
2026-08-13 `industry_US` run named six rows it could not score because it ran twenty minutes before
the open, and this morning's `industry_kr` run wrote the deadline explicitly —
*"🚨 오늘 밤 US 런이 이 넷을 안 채점하면 그때부터 EXPIRED 다"* (`SCENARIOS.md`, MASTER log appended
2026-08-14 by `industry_kr`). **All four are scored below. `EXPIRED` = 0.**

---

## 1. Inheritance read — what was opened, in full

| File | Read | What it changed here |
|---|---|---|
| `handoff/STANDING_VIEW.md` (shared spine) | ✅ incl. the **D165 truncation banner**, §1 regime call, §2 seed chain, **§5 retracted ledger through R68**, §6 | R64–R68 (all five written by the 08-13 US run's own later stages) checked against every claim in this file |
| `handoff/STANDING_VIEW_US.md` | ✅ §2 fact rows through **M632**, §3a registry incl. rows overwritten 08-13 | per-name carry |
| `handoff/SCENARIOS.md` (shared spine) | ✅ MASTER scoring log **through the 2026-08-14 `industry_kr` append**, MASTER index (97 brackets) | the four-row hand-forward, read as an instruction |
| `handoff/SCENARIOS_US.md` | ✅ S63 · S69 · S71 frozen text pulled **verbatim** before any number was computed | scoring below |
| `handoff/SCENARIOS_KR.md` | ✅ opened — **checked for past-dated rows this desk must score: zero.** `S38`/`S48-KR` are KR-owned and their first scoring clock is **2026-08-17** by the KR desk's own T+2 arithmetic (M634) | nothing inherited to score |
| `handoff/RESEARCH.md` | ✅ Part A rules · Part B lenses · Part C dig list | §6 below, loaded as constraints |
| `module_report_tags show` | ✅ cross-queried | §4b — **the drift closed, see below** |

### 1a. The D165 pre-commitment
Writeback at run end is **append-only**. No whole-file `'w'` rewrite of any `handoff/*.md`.
(The 2026-08-05 incident truncated `STANDING_VIEW.md` to 0 bytes exactly that way.)

### 1b. §5 retracted ledger read BEFORE today's view formed
R64–R68 bind this run directly. Two of them constrain sentences this stage would otherwise write:
- **R65** — a **mislabelled window** is this desk's most reproducible error (`D253`). It is the reason
  §2 below decomposes MET's RS20 change into "did the name move" vs "did the window roll" **before**
  reporting a branch fire, rather than after.
- **R67** — *"attention rotated, the object did not."* It is the reason §3a/§3b resolve the three
  tanker rows on **what can be measured**, and refuse to convert a title-level thread into the
  body-proximity observable those rows actually froze.

---

## 2. Scenarios — four settlements, all on the 2026-08-13 settled close

**Method, stated once (D140 · C1):** prices **re-pulled in full at scoring** — `yfinance`,
`auto_adjust=False`, benchmark **`SPY` named inline on every leg**. RS20 = 20-session % return of the
name minus 20-session % return of SPY, on settled daily closes.
★ **Method validated against three independent prior computations before any new number was read**:
this pull reproduces the 08-12 anchors **exactly** (XLU **−5.394** · XLRE **−2.499** · XLF **+0.062** ·
MET **+2.495** · PSX **+12.656**) and reproduces the KR desk's 08-13 numbers **exactly**
(MPC **+12.900** · VLO **+10.590** · PSX **+11.925**).

### 2a. `S63` — **`FIRED-C`** · the three-label duration bet is neither confirmed nor falsified

| Leg (RS20 vs SPY) | 2026-08-05 anchor | 08-12 | **08-13 settle** |
|---|---|---|---|
| `XLU` | −7.02 | −5.394 | **−6.763** |
| `XLRE` | −0.89 | −2.499 | **−4.366** |
| `XLF` | +2.24 | +0.062 | **−0.957** |
| **`DUR` = (XLU+XLRE)/2 − XLF** | **−6.197** | −4.009 | **−4.6075** |

Bands (frozen, D93-measured): **A ≥ −3.3** (against us — the three labels are one exposure) ·
**B ≤ −9.2** (with us) · **C** between. Observed **−4.608 ⇒ C**, **1.308pp from A**, **4.59pp from B**.

★ **The path is the finding, not the level.** The CPI session moved DUR **toward** branch A
(−6.197 → −4.009), and the PPI session moved it **back away** (−4.009 → −4.608). ⇒ **the cool CPI
did start to pull the three tilts together and the split PPI un-did it inside one session.** That is
the same object `S71` measures independently below, and the two agree.
⚠ **C4 scope**: C means the question is **not answered**. It does not mean the three labels are
three exposures.
⚠ **Carried defect, NOT resolved and NOT re-cut** (`D249`): on 252 days the measured third leg of
this complex is **STPL, not FIN** (`XLU`–`XLF` 0.24) while the 60-day window reads `XLF`-complex 0.70
— a live **C5** window-choice problem inside a row that just scored.
✅ **Invalidation clause checked, did not fire**: no utility rate-case **ruling**, REIT M&A, or
bank-specific guidance event inside 08-05→08-13 evidenced by a filing plus two independent outlets.
⚠ **Named rather than smuggled**: the Virginia governor's intervention in the **NEE/Dominion** merger
is a real in-window event with two independent outlets (`cnbc` 08-06 · `bloomberg` 08-06) — but it is
**08-06, and it is not one of the three named classes**, so it does not VOID the row. It is recorded
because `R40` already established that `D` is a merger-arb security (corr +0.89 to NEE, −0.21 to SPY)
sitting inside `XLU`, i.e. **a standing, known contaminant of any XLU-based duration read.**

### 2b. `S69` — **`FIRED-A`** · and it fired on a WINDOW ROLL-OFF, not on a decline

**Frozen observable**: MET RS20 vs SPY at the 2026-08-13 settle, **quoted with its full-year revision
breadth (C2)**. Registration state (08-06 settle): **+7.413**, FY breadth net-down.

| Branch | Line | Observed |
|---|---|---|
| **A — against the flow tag** | RS20 **≤ +2.53** | **+0.406 ⇒ FIRES, 2.124pp inside** |
| B — with the tag | RS20 ≥ +12.24 | — |

**Companion axis, quoted as the row demands (C2)** — `module_fundamentals_us MET`, pulled today:
FY consensus **9.79, −0.6% / 90d**; FY revision breadth **30d 5↑ / 9↓** and **7d 0↑ / 3↓** (net-down);
next-year **10.88, −1.0% / 90d**, 30d 4↑/5↓. ⇒ **the revision book is unchanged from registration and
still net-down.** Branch A's stated meaning — *the revision book led and the flow tag lagged* — is
therefore supported on **both** axes.

🚨 **And here is the qualifier that must travel with the fire.** MET's RS20 fell **+2.495 → +0.406
= −2.089pp in one session, while MET itself OUTPERFORMED**: MET **+0.838%** vs SPY **+0.698%** on
08-13 = **+0.140pp excess**. The entire −2.089 came from the **back** of the rolling window: the bar
that rolled out was **2026-07-16**, and 07-15→07-16 was a **+1.627% MET / −0.542% SPY = +2.17pp
excess session**. Removing it removed the branch's margin.
⇒ **The frozen observable fired and is honoured exactly as written — no threshold was improvised —
but "the flow tag lagged" is measured HERE by a July session leaving the window, not by August
weakness.** Same family as `D233` (anchor-vs-window) and `R65`/`D253` (mislabelled window), which is
why it is decomposed rather than reported flat. **Registered as `D257` (§7).**
✅ **Invalidation checked, did not fire**: no MET catastrophe-loss disclosure and no M&A in-window.
⚠ In-window and **not** in the clause, so recorded rather than acted on: MET reported Q2 on **08-06**
(`nasdaq` 08-06 *"MetLife Tops Q2 Earnings Estimates on Strong Investment Income"*) and authorised a
**$3bn buyback** the same day (`nasdaq` 08-06). The registration used the 08-06 settle, i.e. **after**
the print.
⚠ **S58 also owns MET on a different observable and NEITHER row is re-frozen** — if they disagree,
the disagreement is the finding (S14-ANNEX / S35-ANNEX precedent).

### 2c. `S71` — **`FIRED-C`** · the CPI and PPI prints did **not** materially disagree

**Frozen observable**: `Δ` = [XLU 1-session excess vs SPY on **08-13**] − [same on **08-12**].

| | Value |
|---|---|
| XLU excess, 08-12 (CPI day) | **+0.2309pp** |
| XLU excess, 08-13 (PPI day) | **−0.2415pp** |
| **Δ** | **−0.4724pp** |

Bands (D93, trailing-252: mean +0.0063 · sd 1.6268 · q15 −1.686 · q85 +1.571):
**A ≥ +1.57** · **B ≤ −1.69** · **C** between. ⇒ **C**, **1.22pp from B**, **2.04pp from A**.

✅ **Anti-signal (a) — either print delayed or off-schedule ⇒ VOID: did NOT fire.** July CPI released
**2026-08-12** (FRED-confirmed by the 08-13 run) and July PPI released **2026-08-13 08:30 ET**, both
on schedule.
✅ **Anti-signal (b) — a non-macro XLU-specific event on 08-12 or 08-13 ⇒ AMBIGUOUS: did NOT fire, and
this was MEASURED rather than asserted.** Two candidate contaminants existed and both were tested by
decomposing the Δ across XLU's large constituents (1-session excess vs SPY, 08-12 → 08-13 → Δ):

| | 08-12 | 08-13 | Δ |
|---|---|---|---|
| **XLU** | +0.231 | −0.242 | **−0.472** |
| `DUK` (Ohio/Kentucky storm outages, prnewswire 08-12 · 08-13) | −0.007 | +0.112 | **+0.119** |
| `NEE` (Dominion merger intervention) | −0.204 | −0.430 | −0.226 |
| `D` (the merger-arb leg) | −0.339 | +0.037 | **+0.376** |
| `SO` · `AEP` · `XEL` · `PEG` (regulated bulk) | +0.402 / +0.615 / +0.960 / +0.627 | −0.406 / −0.112 / −0.214 / −0.619 | −0.808 / −0.727 / −1.174 / −1.246 |

⇒ **10 of 14 constituents carry a negative Δ and the two candidate contaminants push the OTHER way
(DUK +0.119, D +0.376).** The move is **broad regulated-utility**, not name-specific. The
anti-signal's own purpose test — "does a single name explain the reading" — **fails to fire.**
⚠ **Registered defect `D248` carried, band NOT moved**: the +0.231 base made branch A a **6.0%** event
and branch B a **10.3%** event, so **C was the heavy favourite before the settle and was graded
no-information at registration.** The C is honoured; it is also close to uninformative by construction,
and `S80` (→ 08-19) was registered on 08-13 precisely to replace this row's job on a 4-session window.

### 2d. Rows this desk did NOT need to score, named rather than dropped

| ID | State | Why |
|---|---|---|
| **S67** | ✅ **already `FIRED-C`** | scored by the **2026-08-14 `industry_kr`** run on the same 08-13 settle (median{MPC,VLO,PSX} RS20 = **+11.925**, band A ≤−2.20 / B ≥+13.56, **1.635pp from B**). ✅ **Independently reproduced by this run's own pull to the third decimal.** ⚠ The KR run disclosed it did **not** check `S67`'s D149 invalidation at a primary source; **this run checked and it does not fire** — no refinery-specific incident filing in-window |
| **S68** | ✅ **already `FIRED-A`** | scored 08-13 by `portfolio_US` on leg (ii) (DIS FY 30-day breadth **1↑/7↓**), **settle-invariant** at a 6-count margin; leg (i) VOID by construction (`S68-ANNEX`: EA went private 08-04) |
| **S64** | 🚫 **already `VOID`** | settle-invariant: WTI 08-12 settle **83.27** vs the row's base **75.22**; crude **rose 10.7%** over the window the row needed a fall in. `D249` (the row measures XLI while the position is defense) is **moot** — it never scores |
| **S73 Leg 1** | ✅ **already `N`** | determined by the published leg alone: `hy_oas` 08-12 **2.71** = the 08-06 anchor **2.71** ⇒ ΔHY = 0.00 forecloses both conjunctions regardless of `DGS2` |
| **S74** (→08-24) · **S75 · S76 · S77 · S78** (→08-19) · **S79** (→08-27) · **S80** (→08-19) · **S81** (→08-27) · **S82** (→08-20) · **S83** (→08-20) | **ARMED** | none past-dated |
| 🚨🚨 **S8** | **un-scoreable, 12th consecutive run** | registered `[blank]` with **no date**, so no settlement condition exists. **A human must `VOID` it or re-register it with a date (P5).** Named again, not dropped |

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows left unscored = 0.**

---

## 3. Both ledgers audited — `due` run on each, **every row resolved**

### 3a · 3b. The three tanker rows — resolved after **three** HANDOVERs, and the resolution is a defect report

`reject_ledger.py due` surfaced **1** row (`DHT`, recheck 2026-08-13); `missed_ledger.py due`
surfaced **2** (`INSW`, `FRO`). All three were entered 2026-07-31 and all three carry the **same
two-leg condition**: a price leg and a **body-proximity** news leg.

| Row | Leg 1 — RS60 vs SPY (08-13 settle) | Leg 2 — body-proximity confirm | Resolved |
|---|---|---|---|
| `DHT` (reject, `A.flow미도착`) | **+1.89 ⇒ PASSES** (was −4.0 at rejection — the sign flipped) | ❌ **cannot be run** | `reaffirmed` |
| `INSW` (missed, `U.발굴부재`) | **+6.26 ⇒ PASSES** (base +7.2 — held) | ❌ **cannot be run** | `reaffirmed` |
| `FRO` (missed, `U.발굴부재`) | **+2.06 ⇒ PASSES** (base +1.9 — held, thinly) | ❌ **cannot be run** | `reaffirmed` |

🚨 **Why leg 2 cannot be run, measured not assumed.** `module_news_data chain-hop` — the tool the
condition names — raises **`sqlite3.OperationalError: no such table: news_fts`** (the local index has
been **0 bytes since 08-12**), and the remote bridge returned **`URLError` 5/5** at 22:15 KST
(PREFLIGHT **G1 FAIL**). **A price answer cannot discharge a conjunction**, so the rows stay out.

⚠ **The title-level thread is alive and escalating, cited as context and explicitly NOT as the frozen
observable** (the client store carries **titles**, the condition froze **bodies**):
**270 `Hormuz` title hits / 43 `tanker` / 15 `Red Sea` in the 7-day window**, with
`zerohedge` 08-13 *"Recruitment Ad Offers Tanker Crews Double Pay To Brave Drone Strikes"*,
Reuters via `google_en` 08-12 *"Saudi Red Sea oil exports go dark as Houthi attack threat grows"*,
`semafor` 08-12 *"Houthis kill 6 in attack on Red Sea cargo ship"*, `bbc` 08-13 *"UK defends seizing
shadow fleet tanker"*.
⚠ **Counter-evidence held in view rather than discarded**: `S61` scored **FIRED-C** on 08-12 — the
EW{STNG,FRO} 5-session excess **never reached** branch A (+6.80; max +3.174) and **terminated
positive**. So a 60-session RS says "positive" on three names while a 5-session excess said "no
premium appeared" — **the two windows disagree and neither is re-cut** (C5 again).

★ **The finding this closes, and it is a design defect, not a market call: all three conditions name
a TOOL, not an OBSERVABLE.** The moment `chain_hop` died, the rows became **permanently
unresolvable** — which is how they crossed three HANDOVERs. **Registered as `D258`** (§7).
✅ **Post-resolution state: reject ledger 163 rows · 88 resolved · legacy 0 · due 0.**
**Missed ledger 120 rows · 49 resolved · legacy 0 · due 0.** Legacy held at **0 for an 18th run**.

### 3c. Rejection-ledger `score` — context, never a gate
84 scored rows · mean excess **+2.3pp** · 28 harmful / 21 helpful / **35 noise (42%)**.
By type: **measured +2.7pp (n=68)** · narrative +2.5pp (n=10) · **structural −3.2pp (n=6)**.
Worst class **`E.상관가드` −11.3pp (n=4)**; best **`H.밸류소진` +4.5pp (n=7)**.
⚠ Loss-sum **+437.7pp** vs gain-sum **−246.3pp** — i.e. **rejecting has cost more than it saved in
aggregate**, on a small sample over a short window. **Accumulation, not an edge (P4).**

### 3d. Exposure state — read, and it is **NOT this desk's book** (W1)
`exposure_rule.py state` benchmarks **`069500.KS`** and reports the **KR contest book**: rule state
**정상**, target invested **95%**, **current invested % UNAVAILABLE** (account query failed) ⇒
**the band gap cannot be computed** and no number is substituted (P5).
Ledger `show --tail 6`: 35 rows, last 5 of 6 are **`live` (unsettled) bars**; 08-14 reads invested
**68.0%** with a **🚨 band deviation −27.0pp**; cumulative **n=8**, total excess **−14.21pp =
cash −6.26pp + selection −7.95pp**.
🚫 **Not carried as size context for this desk's BET/ALPHA.** It measures a different book in a
different currency on a different benchmark — **W1 forbids the transfer**, and the same reasoning is
why this protocol's DEEP budget stays **N=4** while `industry_kr` cut to N=2.
⚠ Also standing: the ledger prints **`🚨🚨ARMED(TIMEFOLIO_EXECUTE=1)`** on every row. This desk issues
no orders (P4) and this run runs no `--execute`; the flag is recorded because it is on.

### 3e. Signal scoreboard (`ic_ledger score`) — and the transfer rule that binds it
Header prints **`# IC LEDGER — KR`**; **404 rows, all 21 tests KR.** Carrying only `n_eff ≥ 4`:

| Axis | h | n_eff | mean IC | t(NW) | verdict (Bonferroni \|t\|>2.8) |
|---|---|---|---|---|---|
| **`vol_surge`** | 1 | 26.0 | **−0.0481** | **−3.20** | ★ **significant** |
| **`vol_surge`** | 5 | 4.2 | **−0.0405** | **−2.90** | ★ **significant** |
| `obv_norm` | 5 | 4.2 | −0.0738 | −1.70 | indistinguishable |
| `rs60` | 5 | 4.0 | −0.1428 | −1.46 | indistinguishable |
| `flow_score` | 1 / 5 | 26.0 / 4.2 | −0.0442 / −0.0814 | −1.07 / −1.25 | indistinguishable |
| `rs20` | 1 / 5 | 25.0 / 4.0 | −0.0480 / −0.1083 | −0.92 / −1.13 | indistinguishable |

★ **Two horizons clear multiple comparison on the same axis with the same (negative) sign — and
`sector_flow` weights `vol_surge` POSITIVELY in its 🟢 gate.** Standing item, now in its second run.
🚫 **The gate is NOT changed by this run** — code changes are a human item — and the reservation
stands: **all 21 cells have a negative mean IC** (M642), so the significance may be a property of the
**regime**, not of the axis. **Not distinguished today (C3).**
🚨 **`D243` re-confirmed, 2nd run: the US desk ranks 300 names every run and has ZERO IC cells of its
own.** `R3`/`W1` forbid reading the KR table as a US verdict ⇒ **this desk still cannot say whether
its own ranking has a sign, in either direction.**

---

## 4. Reconciliation, staleness, and one ledger that started moving again

### 4a. Stale rows and cleared suspensions
| Object | asof | State |
|---|---|---|
| US equity prices / all excess returns | **2026-08-13 settled** | ✅ `D74` = 0 (PREFLIGHT G0 PASS, last-bar volume median **0.732×**, `SPY` carries the same terminal bar) |
| `SECTOR_FLOW_US.json` | **asof 2026-08-13**, 3-axis (`vel_coverage` 0.170, `dropped_missing_axis` 0) | Δ vs `history.json["2026-08-12"]`, same mode ⇒ **one-session Δ, 300/300 names** (G2 PASS) |
| `us_top300.csv` | **2026-07-15 — 30 days old** | 🔴 stale caps on every `wflow` / `top1_w`. **`EA` still present, still returning a NULL close (2nd run)** |
| `cycle_registry.json` | **2026-07-17 — 28 days old** | 🔴 3 cycles; rank-3 floor `0.0` ⇒ **that check is silently OFF**; HLTH unregistered; `core_pick_why` still quotes **`R8`, a retracted claim** |
| Book | 2026-08-14 | 13 holdings (US 11 · KR 2). **Total ₩17,912,656**, cash **KRW 4,938,207 + USD 1,904** |
| News corpus (client store) | **current to 2026-08-14** (1.045 GB, mtime 08:55) | **42,192 articles** in the 7-day window; the desk's *search* path is what is dead, not the corpus |

### 4b. ✅ Mechanical ledger vs the analytical carry — **`D244` has CLOSED**
`module_report_tags show` now reports **`갱신: 2026-08-14T09:44` · 54 reports · 277 tickers · 12
sectors**, and its per-name "latest report" column cites **`industry_US/2026-08-13/…`** files.
Yesterday this tool's newest row was **2026-07-16** — four weeks stale — and the L1's three mandated
cross-reads were **unavailable**. They are available again. Spot-reconciliation:

| Cross-read | Result |
|---|---|
| Coverage without belief | `NEM` (14 reports, latest `ACTION_TICKETS.md` 08-13) has heavy coverage and **no standing §3a thesis** — it is also the name that made MATR "one sector, one name". ⇒ **candidate DEEP**, and it is already ranked #1 in §7 |
| Belief without coverage | none surfaced among the 11 held US names — all carry ledger rows |
| Resolved-but-live | `EA` carries verdicts incl. **LIVE** while the security **went private 08-04** (`S68-ANNEX`) and now prints a null bar ⇒ **stale tag, flagged; the desk cannot make any flow claim on it (G5)** |

### 4c. ID hygiene, checked at READ time
Highest existing: **M632 · D253 (unsuffixed) / D250-KR · R68 · S83 (US) / S61-KR (KR)**.
This run takes **`D257`–`D259`** unsuffixed and will take `M`-ids from **M653** at writeback
(the KR run took M633–M652 this morning). ⚠ **`D211` — the dig-counter collision — is a human item
for an 8th consecutive run.**

---

## 5. 🚨 Instrument health inherited — what this run may NOT claim

From `llm_outputs/2026-08-14/preflight/PREFLIGHT_US.md` — **PASS 3 / FAIL 5**.

| Gate | Verdict | Binding consequence for this run |
|---|---|---|
| **G0** bars/dates | 🟢 PASS | ✅ **RS may be compared at fine grain; `vol_surge` readable in both directions**; `asof 2026-08-13` needs no caveat. Second consecutive clean US clock |
| **G1** news axis | 🔴 FAIL (17.0%, 51/300) | 🚫 **No velocity, no theme freshness, no "it went quiet".** `theme_age` / `chain_hop` **confirmed dead** (`no such table: news_fts`). **DRIFT must report its instrument was dead, not report "no drift."** The 51 survivors are a **survivor sample** and are unusable too. **See the scope narrowing below — it is not a reversal** |
| **G2** scale continuity | 🟢 PASS | ✅ Δ valid, spans exactly ONE settled session (08-12 → 08-13), 300/300 names |
| **G3** sector sign owner | 🟢 PASS | 🚫 **Information Technology, Health Care and Materials may not be promoted or demoted on `wflow`** (flippers `NVDA` 19.4% · `LLY` 19.4% · `LIN` 24.7%). ★ **IT is new to this list and it is the board's largest sector: ex-`NVDA` its wflow is −0.078, not +0.016** |
| **G4** risk units | 🔴 FAIL (11 / 10 / 10) | 🚫 No single-number concentration guard; **the `--days` window goes on the same line as any concentration claim**; no verdict on whether `AVGO`+`NVDA` or `ANET`+`ETN` are one unit (250d says two, 500/750d say one) |
| **G5** universe | 🔴 FAIL (age) | 🚫 `wflow` is **not** current-cap weighted — 30-day-old caps. 🚫 No flow/RS/OBV verdict on **`EA`**. ✅ **11/11 US holdings inside the universe AND scored** — zero held-but-unmeasurable names, 3rd run |
| **G6** estimate accrual | 🔴 FAIL (2.4×) | 🚫 No `kelly_size --ic` figure as evidence-backed size. Any size is **"mechanical ¼"** |
| **G7** tools | 🔴 FAIL (2/46) | `margin_history.py` · `module_chart` fail `--help` for a **5th run**; both pass functional probes ⇒ citable **only via those probe command lines** |

### ★ Scope narrowing on G1, recorded as a narrowing and not as a reversal
**Measured during this stage:** the desk's news capability is **two paths, and only one is dead.**

| Path | State | Consequence |
|---|---|---|
| FTS / remote `/exec` (`search`, `fts search`, `theme-age`, **`chain-hop`**) | ❌ **DEAD** — `URLError` 5/5 remote; local index **0 bytes** ⇒ `no such table: news_fts` | **G1's revocations stand in full.** The sweep's velocity column stays revoked |
| Client-owned vector store (`data/news_vectors.db`, 1.045 GB, current to 08-14) via **`thread`** / direct query | ✅ **ALIVE** — `thread --days 7 --scope foreign` returned per-day denominators (08-08 283 · 08-09 289 · 08-10 787 · 08-11 798 · 08-12 756 · 08-13 725 · **08-14 0**), 3,638 daily events → 2,882 threads | **News facts may be cited with source + date on the line** — this is exactly the escape hatch G1 rule 5 requires |

⚠ **Two hard limits on the alive path, so it is not over-read.** (i) It carries **titles, not bodies**
— it cannot satisfy any body-proximity observable (§3a). (ii) **08-14 has 0 articles at this clock**,
so every multi-day thread is tagged `ENDED` / `살아있는 0` **by window-end artifact**; the tool warns
about this itself. 🚫 **No `FADING` / `ENDED` verdict may be quoted from today's `thread` run.**
⚠ **`D245` (the bridge is intermittent, not down) gains a 4th data point**: DEAD 08-13 22:14 → ALIVE
08-14 08:40 (KR desk) → **DEAD 08-14 22:15**. The pattern *"alive at the KR desk's morning clock,
dead at the US desk's night clock"* has now held **two consecutive days** and is still uncharacterised.

---

## 6. RESEARCH triggers loaded as binding constraints

| Group | Fires when | Binds, this run specifically |
|---|---|---|
| **C** — C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | you cite a number | **MACRO** — every excess return names `SPY` inline. ★ **C5 is the load-bearing rule of this run**: it is live and unresolved in **three** places at once — S63's third leg (STPL vs FIN, 252d vs 60d), the tanker rows (RS60 positive vs a 5-session excess that saw nothing), and **S69's rolling window**. **C4** binds every C-branch above: "not answered" ≠ "answered neutrally" |
| **S** — S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample ≠ done · S5 short samples · S6 future labels | any statistical claim | **SWEEP / ROTATION**: the Δ is **one** session — S1 forbids "the trend turned". **S5** binds §3e (19 of 21 IC cells unusable or indistinguishable), §3c (84 rows, 42% noise) and G4's 249-bar window. **S2** binds G1: the null was diagnosed (pipe, not silence) before being reported |
| **D** — D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · **D6 signal grade (OBV is C)** | you read data | **SWEEP · ALPHA**: OBV is **grade C** and carries no verdict alone — ⚠ with the velocity axis dead its *load* rises while its *grade* does not. **D4** binds §3e directly: the IC significance may be a regime property |
| **W** — W1 cross-market transfer · W2 inherited lead/lag · W3 real ≠ profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | you write a conclusion | ★★ **W1 binds §3d and §3e** (both ledgers are KR objects) and is why the DEEP budget stays **N=4**. **W5** binds **IT** hardest this run — ex-`NVDA` the sector inverts — and **ENRG** (refiners ≠ integrateds) |
| **L** — L1 second derivative · L2 peak-margin trap · L3 branch information content | lenses | **DEEP · PREMORTEM.** **L3** owns tonight's mandatory bracket (the `CATALYST_WATCH` binary, §7). **L2** owns MET: forward P/E **8.96** with FY estimates **−0.6%/90d** is the low-multiple/falling-denominator shape the lens names |

---

## 7. Dig list — ranked for today, plus the three this run registers

### New this run (`D257`–`D259`, unsuffixed US namespace)

| # | Dig | How it was found | Human needed? |
|---|---|---|---|
| **D257** | ★★★ **A branch can fire on a rolling window's BACK END while the name moves the other way, and nothing in the registration grammar shows it.** `S69` fired branch A at **+0.406** after a **−2.089pp** one-session RS20 move in which **MET outperformed SPY by +0.14pp** — the whole move was the **07-16 bar (+2.17pp excess) rolling out**. The fire is correct and honoured; the *reading* would have been wrong. **Positive-form remedy: any RS-window observable is reported with its two-part decomposition — front-end (the session) and back-end (the roll-off) — on the same line as the branch verdict.** Third member of the family with `D233` and `D253` | §2b, applying `R65` before writing the verdict | **PREMORTEM (adopt the decomposition at registration)** |
| **D258** | ★★★ **Three ledger rows named a TOOL instead of an OBSERVABLE and became permanently unresolvable when the tool died.** `DHT` / `INSW` / `FRO` all froze *"body-proximity confirm"* = `chain_hop`, which now raises `no such table: news_fts` on a 0-byte index. Their price legs all PASS; the rows still cannot be revived, and they crossed **three** HANDOVERs. **Positive-form remedy: `revives_if` / `enters_if` must name a quantity with a source and a threshold (a rate, a price, a filing), never a tool invocation. Re-file the three on a tanker-RATE observable if the watch is to continue.** | §3a/§3b, running `due` and then trying to actually satisfy the conditions | **human (re-file the three rows) · BET/ALPHA (condition grammar)** |
| **D259** | ★★ **The desk's news capability is TWO paths and the rights table treats it as one.** The FTS/remote path is dead; the **client vector store is alive and current to today** (42,192 articles / 7d) and answered `thread` normally. Every G1 FAIL to date has revoked *all* news citation, which is **stricter than the measurement supports** — and the reverse error (reading the live path as restoring velocity) is equally available. **Positive-form remedy: PREFLIGHT G1 splits into G1a (search/FTS/chain-hop) and G1b (client store), each with its own revocation list, so a run knows which sentences it may still write.** ⚠ Carries a hard limit: the store holds **titles, not bodies** | §5, after `chain-hop` died and `thread` did not | **idle_probe (design the split) · human (adopt)** |

### Carried digs re-confirmed rather than re-discovered
**`D243`** (no US IC ledger — 2nd run) · **`D244`** ✅ **CLOSED this run** (the tag ledger is current
again) · **`D245`** (intermittent bridge — 4th data point, pattern now 2 days consistent) ·
**`D249`** (S63's third leg is STPL at 252d — the row scored with the defect carried) ·
**`D248`** (S71 graded no-information before its settle — **and it scored C, as graded**) ·
**`D211`** (dig-counter collision, human, **8th run**) · **`D17`** (`drift` absent from
`DB_READ_CMDS` — **9th run**, DRIFT will hit it at stage 11) · **`D6`** (OBV grade C) ·
🚨🚨 **`S8` undated — 12th run, human item.**

### ★ The ≤48h binary, read from `catalyst_calendar` at this clock
**1 binary in window**: *"Iran 'Strait of Hormuz open' statement (TACO trigger)"*, axis **oil**,
**undated**. ⇒ **PREMORTEM (stage 7) must produce a both-sides bracket** — a one-way tilt into a known
binary is a protocol violation. ⚠ `S74` already owns the Hormuz reopening (→08-24) and **`D239`**
records that its branch B enumerates **two acts** while a transit collapse fires neither; **`R67`**
records that the outlet curve fell while the physical condition tightened. **The premortem inherits a
bracket that is known to be under-specified, not a clean slate.**
⚠ **`D155`**: `action_bracket` returns a **silent false negative** on runs crossing local midnight.
This clock is **22:1x KST, pre-midnight** ⇒ not exposed, but the run may cross midnight later.

### Ranked for THIS run's DEEP slots (N=4: 2 continuous + 2 rotating)
1. **IT** — 🚨 **new and load-bearing**: it entered the G3 flipper list. `wflow +0.016` becomes
   **−0.078 ex-`NVDA`**, breadth **0.09 with 5🟢 / 10🔴 of 56**, and its Δ is the board's **second
   largest positive (+0.152)**. The board's only non-negative non-Energy `wflow` is **one name**.
2. **MATR** — `S57` FIRED-A twice and the tilt was carried anyway; `S77` is its replacement falsifier
   (→08-19). Still a flipper (`LIN` 24.7%), breadth **0.00**, `wflow −0.179` vs **ex-top1 +0.016**.
3. **ENRG** — continuous. `wflow +0.259` is the **only clearly positive sector on the board**, but its
   **Δ is −0.157, the board's second-worst**, and `S67` scored **C** at 1.635pp from the with-us branch.
   The promotion is still un-adjudicated.
4. **INDU** — continuous. `wflow −0.046`, **0🟢 / 10🔴 of 50**, and `D249` says the desk's live bracket
   measures `XLI` while the position is **defense** (defense EW exc20 **+7.81** vs XLI **+0.89**).
5. *(bench)* **HLTH** — new flipper (`LLY` 19.4%), breadth **0.00**, **Δ −0.228 = the board's worst**,
   and `S82` (→08-20) is already the highest-information open row on the board.

---

## 8. Claims this stage asserted and then refuted (§4c · D48)

**Two, both left visible rather than edited away:**

1. **Asserted** while resolving the tanker rows: *"the news leg is dead, therefore leg 2 is
   unmeasurable and that is the end of it."* **Refuted by this stage's own next command** — `thread`
   ran normally against the client store and returned a live 7-day trajectory, so *some* news
   capability exists. **What survives**: leg 2 specifically **is** unmeasurable, because the store
   holds **titles** and the condition froze **bodies**. **What was withdrawn**: the general claim that
   the desk cannot read news today. ⇒ **`D259`**.
2. **Asserted** while drafting §2b: *"MET's RS20 collapse confirms the flow tag was wrong."*
   **Refuted by decomposing the window in the same minute** — MET **outperformed** on 08-13 (+0.14pp);
   the entire move was the 07-16 bar leaving the window. **What survives**: branch A fires on the
   frozen observable, and the revision axis independently agrees. **What was withdrawn**: the causal
   sentence. ⇒ **`D257`**.

⚠ A third, adjacent: this stage began to treat **`S71` C** as "the PPI was a non-event". It is not —
C means the **XLU-measured** divergence was inside ±1.6pp, and `S63` independently shows the PPI
session moved DUR **away from convergence**. Two different objects, one of which found a signed move.

★ Zero self-refutations would itself be a finding (it usually means the controls were not adversarial).

---

## 9. What this stage hands to MACRO

- **Inherited tilts, verbatim from `SECTOR_ROTATION.md 2026-08-13 §1`**:
  **`INDU OW− · ENRG OW− · FIN N · IT N · HLTH N+ · DISC N · MATR N− · COMM UW · UTIL UW · STPL UW− ·
  RE UW`**
- **Regime call inherited unchanged** `[inferred]`: *memory is a price-cycle industry in
  rate-of-change deceleration while its level stays tight* — carried, **not cited as evidence**.
- **§4 asymmetry, unchanged**: a hyperscaler capex **cut** changes the thesis; a **raise** only moves
  its timing. **NVDA prints 2026-08-26 (D-12)** and is bracketed by `S79` / `S81`.
- **The macro premise of the day, inherited and to be re-pulled at `[FRED]`**: a **cool July CPI
  (08-12)** followed by a **split July PPI (08-13)** — headline 0.0%, goods −0.7%, **core +0.4% MoM /
  +4.7% 12m**, still tagged `[inferred-source]` (the BLS primary returned HTTP 403 yesterday).
  ★ **Two independently-scored rows now say the market did not resolve the two prints into one story**:
  `S71` C (XLU day-over-day Δ **−0.472pp**, inside band) and `S63` C with DUR moving **−4.009 → −4.608**,
  i.e. **away** from convergence on the PPI session.
- **Four rows scored** (S63 C · S69 **A** · S71 C, plus S67 C reproduced) · **ten still ARMED**, the
  next settling **2026-08-19**.
- **The rights table (§5)**: speak with **settled prices through 08-13**, RS at fine grain, OBV
  (grade C), breadth, `vol_surge` in both directions, FINRA short pressure, COT positioning, `[FRED]`,
  primary filings, and **hand-cited news facts with source + date from the client store**.
  🚫 Do **not** speak with the sweep's news velocity, theme age, `chain_hop`, a `FADING`/`ENDED`
  thread tag, a single concentration number, or an `--ic`-backed size.

---

## 10. 🚨 APPENDED AT 22:45 KST BY THE MACRO STAGE — this stage's §3a/§3b reasoning was REFUTED 20 minutes after it was written

> ⚠ **Appended, not edited.** §3a/§3b above stand exactly as written. This is the **D48** rule applied
> to this stage's own output: *a run that shows only its surviving claims has hidden its own error rate.*

**What happened.** §3a/§3b resolved `DHT` · `INSW` · `FRO` as `reaffirmed` on the reasoning that their
body-proximity leg was **unmeasurable** because `chain_hop` was dead. **The news bridge came back alive
at 22:34:57 KST** — 3,835 `Nvidia` hits, **19 minutes after 5/5 `URLError` at 22:15** — and `chain-hop`
then ran normally. **The leg was not unmeasurable. It was unmeasurable for nineteen minutes.**

**Re-measured 22:38–22:41 KST, and the three rows split — which is what the condition was written to do:**

| Row | Leg: body-proximity, re-measured on the live bridge | New outcome |
|---|---|---|
| **`INSW`** | ✅ **MET.** 10 body hits / 7d, foreign scope: *"International Seaways shares gain as **record Q2 profit** beats expectations"* [`yahoo_finance` 08-10] · *"INSW Beats Q2 Earnings and Revenue Estimates"* [`nasdaq` 08-10] · Q2 call transcript [`seekingalpha` 08-10]. **Proximity to the theme is direct**: that same article is one of the **8 body hits for the term `tanker rates`**, and `"International Seaways" AND "Hormuz"` returns **1 body match**. Theme corroboration: *"Black Sea Oil Tanker Rates **Surge to Record** on Drones Barrage"* [`bloomberg` 08-12] · *"Hormuz risk premium: who wins and loses in the tanker trade"* [`seekingalpha` 08-10] | **`entered`** — supersedes the earlier `reaffirmed` |
| **`DHT`** | ❌ **FAILS ON THE DATA.** `"DHT Holdings"` = **0** body matches / 7d. Bare `DHT` = 3, and **all three are DRI Healthcare Trust (`DHT.UN:CA`)**, a different entity ⇒ **zero body presence while the theme is loud** | `reaffirmed` — outcome unchanged, **basis corrected** |
| **`FRO`** | ⚠ **UNMEASURABLE, for a QUERY-FORM reason** — a different defect from the one §3b named. `Frontline` = 107 matches whose top BM25 hits are **Socket Mobile industrial mobility, an AI-trucking piece and NATO/Poland airspace** ("frontline" is a common adjective); `Frontline Ltd` **0**, `Frontline Plc` **0**, `Frontline tanker` **0**. **Neither the 107 nor the 0s are admissible.** M68/R29 class, first reproduction on a US ticker | `reaffirmed` — outcome unchanged, **basis corrected** |

★ **The finding is that the condition WORKED.** Given a live instrument, the same two-leg grammar
separated **INSW (price ✅ + narrative ✅)** from **DHT (price ✅ + narrative ✗)** on the same theme in
the same week. §3a called that grammar a design defect (**`D258`**); the defect is **narrower** than
stated — it is *"a condition that names a tool inherits the tool's uptime"*, not *"a condition that
names a tool is unresolvable"*. **`D258` is amended, not withdrawn**, and `FRO` shows the残 real
defect: a name-string observable on a company whose name is an ordinary English word can never be
measured. ⇒ **the re-file remedy for `FRO` is a RATE observable (Baltic VLCC TCE), not a better string.**

⚠ **`D259` is likewise amended**: the split is not "FTS dead / client store alive". It is
**"the FTS path has an availability window measured in minutes and the desk probes it once."**
A single probe at 22:15 revoked citation rights that were available at 22:34. **Positive-form remedy:
PREFLIGHT G1 probes three times spaced ≥10 minutes before it revokes anything.**

⚠ **What does NOT change**: `SECTOR_FLOW_US.json` was scored at **22:12, inside the dead window**, so
its **`vel_coverage` 17.0% and its 51-name survivor sample remain revoked** — that measurement is a
property of the outage and re-running the bridge later does not retro-fix the file. See `MACRO_REPORT.md §0`.
