# HANDOVER — industry_US · 2026-09-05 (Sat) · Stage 2 / L1·HANDOVER

> Read before anything is decided. Inherits the **analytical carry**, not the coverage ledger.
> Sources read this run: `handoff/STANDING_VIEW.md` (shared spine — §1 regime call, §2 measured
> chain head, §5 retracted ledger incl. the 2026-09-05 KR block, §6 open contradictions, asof
> chain), `handoff/STANDING_VIEW_US.md` (§2 blocks + §3a registry through 2026-09-02),
> `handoff/SCENARIOS.md` (master index + the un-split master scoring log, incl. the 2026-09-05 KR
> block), `handoff/SCENARIOS_US.md` (every row named below opened), `handoff/RESEARCH.md` Parts
> A/B/C, `handoff/README.md`. **Other-market file opened**: `SCENARIOS_KR.md` / the KR run block, for
> the three **US-owned** rows the KR desk scored this morning.
> Prior-run report opened as a primary source: `llm_outputs/2026-09-04/industry_US/HANDOVER.md`
> (§3a) and `llm_outputs/2026-08-26/industry_US/MACRO_REPORT.md` §D (`P101`/`P102` registration).
> Mechanical ledger cross-queried: `module_report_tags show` (80 reports, 297 names, refreshed
> 2026-09-05T10:08 by the KR run).
> **P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.**

---

## 0 · The carry state, and it improved — but this desk's own last run is still the hole

**`handoff/*.md` was written 2026-09-05 ~10:0x KST by the `industry_kr` run.** The spine is **fresh
by twelve hours** — the two-day gap the 09-04 US run inherited is closed on the KR side.

| run | output written | carry written back |
|---|---|---|
| `industry_kr` **2026-09-05** | full run, HANDOVER → BET | ✅ **yes** — `R127`/`R128`, `M1262`–`M1280`, `D491-KR`–`D501-KR`, 5 scored rows |
| `industry_US` **2026-09-04** | full run through DRIFT | ❌ **no** — **8 scored verdicts + `D487`–`D490` live only in `llm_outputs/2026-09-04/industry_US/`** |
| `industry_US` **2026-09-03** | sweep JSON only | ❌ died in stage 1 |

⇒ **This run's first obligation is a fold-in, not a scoring** (§3a). The KR run named this exactly —
`D494-KR`: *"a proposition living only in a run report was bad; a **scoring** living only in a run
report is worse, because the row still reads `ARMED` to everyone else."* It has already cost real
work: the KR run hand-picked `D485`–`D490` and collided with IDs the unwritten US runs had issued.

⚠ **`D490` therefore reproduces on this desk specifically.** Three of the last four `industry_US`
runs produced `llm_outputs` without a `handoff/` writeback. **This run pre-commits to the writeback
at run end and names it here so the commitment is checkable** (`W3`-style: saying it is not doing it).

---

## 1 · Instrument health inherited FIRST (`preflight/PREFLIGHT.md`, written 22:09–22:19 KST)

**PREFLIGHT ran and exists.** Its verdicts govern every number below.

| gate | verdict | what it removes from this run |
|---|---|---|
| **G0** | ✅ **PASS — the tape is clean and STAYED clean** (1/301 NaN on all 14 sessions, `EA` only) | nothing, except any verdict on **`EA`** |
| **G1** | 🔴 sweep news axis **16.39%** (49/299) · ✅ direct path live · ★ **mechanism found** | 🚫 no theme-freshness / velocity / "it is quiet" **from the sweep**, *including* the 49 that scored — they are the 49 largest caps |
| **G2** | ✅ scale continuous, true one-session Δ, **both sides post-heal** | nothing — ✅ **the `delta` column inside `SECTOR_FLOW_US.json` is citable again** (it was barred on 09-04) |
| **G3** | ✅ full 11-row list printed (1 flipper) | 🚫 no `wflow` verdict on **Cons. Disc.** (AMZN 40.2%) or **Comm. Services** (Alphabet 76.6% under two tickers) |
| **G4** | 🔴 **12 / 11 / 10** units across 250/500/750d | 🚫 no single-number concentration claim; `--days` on the same line |
| **G5** | 🔴 universe **52 days** stale (cover ✅ 11/11) | 🚫 no cap-weight / sector cap share / `top1_w%` cited as current |
| **G6** | 🔴 accrual 0.56/day, **1.8×** slow | `kelly_size --ic` is "mechanical 1/4" if used at all |
| **G7** | 🟡 42/44 `--help` clean; chart live 3/3 | 🚫 no `margin_history` output |

★ **The two gate movements that matter, and one is a genuine restoration.**
1. ✅ **`G2`'s revocation is LIFTED.** The 09-04 run had to bar the JSON's own `delta` column outright
   and substitute a rebuilt baseline, because the healing put the contamination on the *older* side
   of the subtraction (mean |Δ| 0.1078, 19 sign flips). Today **both** sides — the stored 09-03
   snapshot and today's 09-04 scoring — were computed off healed caches. **No baseline repair was
   performed, none is claimed, and the Δ column may be cited directly.** This is the first run since
   2026-08-28 with an unqualified flow object.
2. ★ **`G1` moves from "signature identified" to "mechanism identified", and it is self-inflicted.**
   The 09-04 run established the failure is **positional** (a wall at 50 names), falsifying its own
   09-02 "≥9s spacing" prescription. Today reproduces the wall **exactly** (velocities at universe
   positions **0–48**, `None` at **49–299**, zero exceptions) and closes the loop with a recovery
   clock: the identical probe is **6/6 before the sweep**, **0/4 immediately after**, dead at t+20s
   and t+40s, and **alive at t+60/+80/+100s (3/3, identical count 4102)**. ⇒ **The sweep's own burst
   trips the tunnel at ~49 names / ~98 queries, and then keeps firing into a dead endpoint that
   needs ~60 idle seconds to recover.** The pipe is not down; this desk knocks it down. `D489`'s
   prescription (chunk below the burst count) is now supported by a *measured recovery constant*,
   not only by a cutoff position.

**Citable flow object today: the PRIMARY `SECTOR_FLOW_US.json`** (299 scored, 3-axis `nonews`,
asof **2026-09-04 — a settled Friday close**), **including its own Δ column.** No `_REPAIRED.json`
exists and none is needed; a downstream stage that globs for one falls back to the primary file.

★ **And one clock fact that removes a whole class of caveat.** Every run since 09-01 had to reason
about partial bars — the 09-04 run ran at 09:10 ET with NYSE unopened and truncated a half-formed
row. **This run is Saturday: the market is closed, 09-04 is settled and complete.** `D74`-class
intraday contamination is **structurally absent**, not merely checked.

---

## 2 · Inherited standing view — the regime call carried in

**Carried from the 2026-09-02 `industry_US` asof entry and the 09-04 run's §2, unchanged unless
MACRO measures otherwise:**

- **The repricing is a POLICY-PATH repricing, not an inflation repricing.** `[measured]` `M1234`:
  3-session (Δbreakeven − Δreal) at **−11.0bp = the 5.2nd percentile of 252**. `M1235`: the 09-01
  curve **bear-flattened**. Carried as **`P121`**, with **`P125`** registered as its own falsifier.
  ⚠ **Neither can be scored today** — `DFII10`/`DGS2` stop at **09-03** (§3c).
- **US credit sits at a one-year TIGHT while global yields print multi-decade highs.** `[measured]`
  `M1236`. Refreshed this run: `hy_oas` **2.65** (09-03) · `ig_oas` **0.81** · `NFCI` **−0.558**
  (08-28, weekly). Still the single strongest fact standing **against** the `FIN UW`.
- **Energy's OW is a CHAIN-POSITION bet whose centre of gravity is moving upstream.** `[measured]`
  `M1245`/`M1246`. ⚠ Carried with the 09-04 run's own tension attached: Energy was **rank-1 on level
  and rank-11 on clean Δ** — handed forward to ROTATION, unresolved here (P4).
- **IT is not one bet, and the split is wider than most whole-sector gaps.** `[measured]` `M1251`
  (software/services/security +0.092 vs semicap/test −0.759, gap **0.851**), `M1252` (dispersion
  **1.878**, widest on the board). ★ **This run scores the bracket built on exactly that split
  (`P101`, §3b) and the split INVERTED** — see §9.
- **The same input is priced in opposite directions in Energy and IT.** `[measured]` `M1253`.
- **Utilities' binding constraint is regulatory, not industrial.** `[measured]` `M1257`/`M1258`.
- **Communication Services has been carried on a number wrong by ~0.7.** `[measured]` `M1206`/`D459`.
  ★ **Reproduced an 11th time today at 0.661** (G3): ex-both-Alphabet-classes `wflow` **−0.389 →
  +0.272**, and `eqflow` **−0.035** independently agrees the sector is flat, not negative.
- **Two open, unowned exposures.** `T` and `CBRE` are ~16.6% of real invested capital with no thesis
  (`C23`/`M1169`). `S107` settled `FIRED-C` on 09-03 — the orphan survives its first and only test
  without resolving.

**`[inferred]` rows carried but NOT citable as evidence:** the "duration event is global" reading
(EVENT_ALPHA Card 3, `STORY-ONLY`); the "memory shortage is demand not capacity" reading on `MU`.

### §5 retracted ledger — read BEFORE forming today's view
Nothing in today's opening frame matches a retracted entry. Four retractions bind this run:
- **`R120`** (09-01) — the 5m-proxy error bound. Moot: the proxy is retired (G0), second run running.
- **`R122`-KR** (09-02) — missing bars move a benchmark window's **start**. `W1` bars importing the
  KR conclusion; the **check** transfers and was re-run: today's cache has **1 NaN per session
  (`EA`)** and `SPY` is not in the sweep universe but the 20-session window is hole-free for all 300
  scored names ⇒ the US `rs20` axis is not exposed. Stated because it was checked.
- 🆕 **`R127`-KR** (09-05) — *"the index close does not exist because the vendor lacks it."* `W1`
  bars importing the KR instance, but **its general form is a US-relevant rule and is adopted**:
  a vendor's silence is not the world's silence; before writing "X does not exist", name a second
  venue. ★ Directly applicable today — **G1's whole finding is that a `None` meant *our own outage*,
  not *no news*.** The KR desk retracted the same error class this morning on a different instrument.
- 🆕 **`R128`-KR** (09-05) — a one-day vocabulary spike is not an axis migration. `W1` bars the
  content; the construction lesson (don't promote a d3 count to a regime claim) binds EVENT_ALPHA.

### §6 open contradictions — carried, not resolved
| id | state this run |
|---|---|
| **`C21`** RSI convention | untouched; its 08-28 rider stays retired (no holed window remains) |
| **`C22`** the two ledgers name different hands | **quiet again** — 0 due on both after a 30-row KR clear-out (§4). One busy run does not make a habit; carried |
| **`C23`** three books, none self-identifying | ★ **reproduced a 6th time and the KR desk flagged it NEWLY URGENT**: `exposure_rule`'s target moved **55% → 95% in one session while the position did not move**, and `cycle_exposure` reads a *different* book (real KIS, **$5,255 invested of ≈$11,022 ⇒ 52.3% cash**). **Human call (P5)** |
| **`C24`** copper spec at the 100th percentile vs a Materials bucket | ⚠ Materials today **−0.025 `wflow` / −0.107 `eqflow`**, Δ **−0.037** — now negative on both cuts. **`P102` settles the two-name question 09-09.** Carried a 6th run |
| **`C25`** two instruments read OBV's sign oppositely | ★ **the KR run narrowed it this morning**: where KIS per-investor actuals exist, `D6`'s grade ordering resolves it (two KR names settled). **The US half is UNCHANGED and cannot be narrowed the same way** — `W1`, and the US has no investor-type feed at all. Carried |
| **`C26`** primary vs repaired sweep disagree | ✅ stays closed-by-disappearance (2nd run with no repaired file) |
| **`C27`** `MSTR`'s two rejections give opposite answers | carried; `due` surfaces them **09-18 / 09-22**. ⚠ `MSTR` is **the single best 5-session name in the whole IT software leg today (+12.17%)** while carrying a standing rejection (`D463`) |

### 🆕 `C29` opened by this stage
**A desk cannot audit an axis it has no ledger for, and it is currently trading on the other desk's
answer by refusing to look at it.** `ic_ledger score` is stamped **`# IC LEDGER — KR`**. Its
strongest cell — `vol_surge` h=1, **n=45 · n_eff 45 · mean IC −0.0414 · t(NW) −3.61**, clearing the
Bonferroni |t| > 2.8 bar for a **third consecutive run** — says the axis's sign is **negative**,
while `sector_flow`'s 🟢 gate weights it **positively**, in **both** markets, from the same code.
`W1` correctly bars importing the KR *conclusion*. But `W1` does not bar **running the same
measurement on US data**, and `D395`/`D428` have asked for exactly that for weeks with nothing built.
⇒ **The contradiction is not KR-vs-US; it is "we have a measurement that would settle a live gate and
we are neither using it nor reproducing it."** Registered as a contradiction rather than a dig
because the resolution requires choosing which of the two is authoritative for the US board (P5).

---

## 3 · Scenario settlement — a fold-in, one new score, and three blocked

> Run clock **KST 2026-09-05 22:09 → 23:0x = Sat 09:09 ET.** NYSE **closed**. Last settled US session
> **2026-09-04**, complete. `D426` does not bind today — nothing is mid-formation.

**Folded in from the unwritten 09-04 run: 8 (+1 VOID). Scored by the KR desk this morning: 3
US-owned. Newly scored by this run: 1. Blocked and named: 3. `EXPIRED`: 0. Silent skips: 0.**

### 3a · FOLD-IN — verdicts that exist but never reached the ledger (`D494-KR`)

**Transcribed, not re-scored.** Provenance: `llm_outputs/2026-09-04/industry_US/HANDOVER.md` §3a,
written by this desk on 2026-09-04 against the pre-registered observables. `D242` forbids improving
a threshold after the fact; it equally forbids re-deriving a verdict that was correctly derived once.

| row | observable | measured | verdict |
|---|---|---|---|
| **`S109`** | `FRO` exc5 vs `SPY`, 08-26 → 09-02 | 41.20 → 45.42 vs `SPY` 766.08 → 765.16 ⇒ **+10.363pp** | ★ **FIRED-A** (≥ +8.043) |
| **`S105`** | [`MRVL` exc10] − [`AVGO` exc10] @ 09-03 | −18.190 − (−3.273) ⇒ **−14.917pp** | ★★ **FIRED-A** (≤ −10.836) |
| **`S106`** | `MSFT` exc10 vs `SPY` @ 09-03 | **+4.635pp** | **FIRED-C** |
| **`S107`** | `EW{T,VZ}` exc10 vs `SPY` @ 09-03 | **+2.105pp** | **FIRED-C** |
| **`S110`** | [`HPE` exc5] − [`DELL` exc5] @ 09-03 | −9.289pp (would be B) | 🚨 **VOID** — both names printed inside the window (`D488`) |
| **`S114`** | `EW{NUE,STLD}` exc5, 08-26 → 09-03 | **+3.134pp** | ★ **FIRED-B** (≥ +0.826) |
| **`S132`** | `AVGO` exc1, first settled close after the print | **−3.792pp** | **FIRED-C** (±9.00) |
| **`S138`** | same observable, wider band | **−3.792pp** | **FIRED-C** (±11.00) |
| **`S141`** | `SMH` exc1 vs `SPY`, 09-02 → 09-03 | **−0.662pp** | **FIRED-C** (A +1.802 / B −1.732) |

★ **One of these needs re-reading against today's tape, and it changes the reading of the other
eight.** `S141` asked *"does the `AVGO` print move the SECTOR"* and answered **no** (−0.662pp on
09-03). **On 09-04, `SMH` printed +2.61% against `SPY` −0.39% = +3.00pp excess** — 1.7× branch A's
line, one session outside the bracket's window. ⇒ **The row's verdict stands (it settles on 09-03 and
`D242` binds), and the desk should record that the sector move it was built to catch arrived on the
next bar.** This is not a re-score; it is the reference state that makes `S141` a *timing* miss
rather than a *direction* miss. Filed as **`M1281`**.

### 3b · Scored BY THE KR DESK this morning — read, not re-derived (`P5`, `D464-KR`)

| row | measured | verdict |
|---|---|---|
| **`S126`** | `XLI` −1.056% vs `SPY` +0.109% ⇒ **−1.165pp** (A ≥ −0.087 / B ≤ −2.500) | **FIRED-C** |
| **`S134`** | `XLF` +0.000% vs `SPY` +0.109% ⇒ **−0.109pp** (A ≥ +2.00 / B ≤ −2.00) | **FIRED-C** |
| **`S139`** | EW{`XLU`,`XLRE`,`XLP`} +0.062% vs `SPY` +1.104% ⇒ **−1.042pp** (A ≥ +1.653 / B ≤ −1.757) | **FIRED-C** |

⚠ **The KR desk attached a criticism of this desk's bracket construction and it is accepted, with one
correction.** `D497-KR`: three `FIRED-C` on bands of ±1.65–2.00pp over 3–5 sessions, realized
0.109 / 1.042 / 1.165pp ⇒ *"C is the modal branch and the rows could not buy information by
construction."* **Accepted as a hypothesis, and the KR desk itself scoped it (`C4`, n=3).** The
correction: **all three rows disclosed C as the favourite at registration**, so this is not a hidden
defect — it is the known cost of a bracket whose informative branch is the tail. The actionable half
is `D497-KR`'s *positive* form, which this desk should adopt: **take short-window sector-ETF bands
from measured dispersion (`D93`) rather than from round pp figures.** Carried into §7's dig list.

### 3c · NEWLY SCORED BY THIS RUN — `P101`, and it is the run's most informative settle

`P101` (registered 2026-08-26 MACRO §D, owner `industry_US`) settles at the **2026-09-04 close**.
It is a `D449`-class row — registered in a MACRO report, never written into the master index — which
is why no prior run scored it and why the KR desk flagged it this morning as *"the next US run's item."*

**Frozen observable** (verbatim): `EW{Application Software, Systems Software, IT Consulting; n=19}`
minus `EW{Semiconductors, Semi Materials & Equipment, Tech Hardware/Storage, Electronic Components,
Electronic Equipment, EMS, Communications Equipment; n=37}`, **5-session returns**, `us_top300`
constituents, settled closes.

**Constituent reconstruction verified against the registration's own counts: 19 and 37, exact.**
Window **2026-08-28 close → 2026-09-04 close** (5 sessions: 08-31, 09-01, 09-02, 09-03, 09-04).

| leg | n | mean 5-session return | participation (% positive) |
|---|--:|--:|--:|
| Software + consulting | 19 | **−4.458%** | **21.1%** |
| Hardware + semis + semicap | 37 | **+2.053%** | **73.0%** |
| **Spread (SW − HW)** | | **−6.511pp** | |

| branch | line | fired? |
|---|---|:--:|
| **A** — software keeps winning through both prints | ≥ **+3.196** (p85) | ❌ |
| **B** — hardware repairs | ≤ **−7.906** (p15) | ❌ |
| **C** | between | ✅ |

⇒ **`P101` = `FIRED-C`.** VOID checked and **not fired**: no GICS reclassification moved ≥3 of the 56
IT constituents between legs (MSCI's 08-31 review was pre-declared a non-voider), and neither `NVDA`
nor `AVGO` had a trading halt ≥1 full session.

★★ **The C is loud, and it is loud in the direction the row said would be informative.** The spread
was **+6.228 = the 89.7th percentile** at registration and finished at **−6.511** — a **−12.74pp**
move that stopped **1.40pp short of branch B**. More decisive than the level: **participation
inverted completely.** Registration measured Application Software **91.7% positive** against Tech
Hardware **16.7%** and Semicap **0.0%**; the settle measures software **21.1%** against hardware
**73.0%**. ⇒ **The "hardware air-pocket" reading is not confirmed by the bracket, but it is no longer
contradicted by it either** — and the carried `M1251`/`M1252` framing ("IT's weak half is
semicap/test") is **inverted on this window**: the drag names are `ADSK −16.40 · CDNS −14.01 ·
SNPS −11.02 · PANW −10.32 · DDOG −10.15` — **EDA and security software**, not hardware. Filed as
**`M1282`** and handed to ROTATION/DEEP as the run's live IT question. ⚠ `C4`: one 5-session window.

### 3d · Due but NOT READABLE at this run's clock — named, not skipped

| row | settle condition | blocker | reference state (**explicitly NOT a score**, `D242`) |
|---|---|---|---|
| **`P121`** | first `[FRED]` close covering 09-04 | 🚨 **`DGS2` stops at 2026-09-03 (4.34)** | A needs `DGS2` ≥ 4.50 **and** `T10YIE` ≤ 2.36; B needs ≤ 4.18. At 09-03: `DGS2` **4.34** = neither; `T10YIE` **2.35** would satisfy A's second leg alone |
| **`P114`** | same | same | — |
| **`P125`** | *"the first observation where **BOTH** `T10YIE` and `DFII10` carry 2026-09-04"* | 🚨 **`T10YIE` carries 09-04 (2.35); `DFII10` stops at 09-03 (2.42)** | 3-session (Δbreakeven − Δreal) through 09-03: `T10YIE` 2.35→2.35 = **0bp**, `DFII10` 2.44→2.42 = **−2bp** ⇒ **+2.0bp**, inside C (A ≥ +5.0 / B ≤ −6.0) |

🚨 **`D427` reproduces for a 5th time, and this run measured it twice.** Two independent pulls of
`module_macro_us` (full 120-day and a 10-day two-series call) return the identical picture:
**`T10YIE` and `RRPONTSYD` carry 2026-09-04 while `DGS2`/`DGS10`/`DGS5`/`DGS30`/`DFII10` all stop at
09-03.** The H.15-derived series **do not publish together**. ★ **`P125` is the one row on the board
that was written knowing this** — its observable names the *joint* date rather than a calendar date,
explicitly citing `D427`. **The row's construction is working: it is unscoreable rather than
mis-scoreable.** That is a design result worth recording, not a failure.
⚠ Also stale: **`DTWEXBGS` stops at 2026-08-28 — 7 days**, the dollar series' recurring lag.

**Not `EXPIRED`** — for all three, the settle condition itself has not arrived.

### 3e · Still armed, no date reached — nothing dropped
`S122`(09-30) · `S123`(09-12) · `S127`(09-08) · `S128`(09-09) · `S129`(09-09) · `S130`(09-10, dead
thread) · `S133`(09-14) · `S135`(09-11) · `S136`/`S137`(09-09) · `S140`(09-08) · `S142`(09-11) ·
`P102`(09-09) · `P111`(09-14) · `P122`/`P123`(09-08) · `P124`(09-18) · `P126`(09-09) · `P127`(09-10) ·
`P128`(09-08) · `P67` · `P81` · `P85` · `P87`–`P89` · `P115`–`P117` · `S3` · `S4`.

⚠ **`P102` reference state, since `C24` turns on it** (explicitly **not** a score, settles 09-09):
Materials is **−0.025 `wflow` / −0.107 `eqflow`** today with Δ **−0.037** and 2🟢/2🔴 of 12 — i.e.
the *sector* has gone flat-to-negative on both cuts since the row was written at a **98.8th
percentile** two-name spread. That is branch **B**'s shape, which the row disclosed as the favourite.

### 3f · Named again rather than dropped
**`S8` — 38th consecutive run unscoreable.** The date field is still `[blank]`. **A human must
`VOID` it or re-register it with a date (P5).** The 38th writing of this line is the finding.

⚠ **`D472` reproduces.** `grep ARMED SCENARIOS_US.md` still returns rows whose verdicts are in the
master log — and **today the set grows by the nine folded-in rows plus `P101`.** The defect is
structural: scoring and header hygiene are two different writes, and only one of them has ever
happened at run end. Header hygiene is **explicitly included in this run's writeback pre-commitment**.

---

## 4 · Both ledgers audited — quiet, and the quiet is now measured rather than assumed

| ledger | total | resolved | legacy (no condition) | **due today** |
|---|---:|---:|---:|---:|
| `reject_ledger` | **293** | **185** | **0** | **0** |
| `missed_ledger` | **312** | **207** | **0** | **0** |

Both `due` calls were run (not substituted with `score`). Both return *"확인할 항목 없음"* — every
row is conditional and no recheck date has arrived.

★ **This is a genuine zero, not a skipped audit, and the movement proves the ledgers are live.**
Rejections resolved **176 → 185** and misses **186 → 207** since the 09-04 US run wrote its numbers:
the 09-04 run resolved 7+3 US rows and the 09-05 KR run resolved **30** (9 rejection + 21 missed).
The 15-run "0 due" streak that ended on 09-04 was a maturing cohort; it has now been worked through
and the ledger is back to quiet **with legacy at 0/0 for both**, a 14th consecutive run.

⚠ **`carryover.md`'s own warning applies and is honoured**: a clean `due` is not proof of health.
The evidence that the practice is taking hold is the **legacy count**, and it is **0 on both ledgers**
— it cannot shrink further, so the standing check becomes "does it stay at 0 as new rows are filed."

🚨 **`D463` binds ALPHA this run and is loaded now, not at ALPHA.** `due` answers *"what is owed a
re-check"*, not *"is this name currently rejected."* Standing rejections that will be live at ALPHA,
with today's state attached:
- **`MSTR`** — 09-01 `L.vehicle없음`, recheck 09-22. ★ **The best 5-session return in the entire IT
  software leg (+12.17%)** and 9th-best flow on the board on 09-03. The rejection stands, unexamined.
- **`CRM`** — 08-31 `B.모멘텀only`, revives 09-30; needs rs20 > +20 **AND** a new dated catalyst.
  5-session **+1.26%** — the price leg has stopped extending.
- **`INTU`** — 08-31 `G.섹터중립`, revives 09-30; needs *IT returns to OW* or z < −1.0. 5-session
  **−7.08%**, i.e. moving toward the z-leg, not the OW-leg.
- **`RTX`**-thread — 09-01 `K.본문반증`. `RTX` is **held**; 09-04 **−0.66%**, 5-session context weak.
- **`VLO`**/`DLR`/`CIEN`/`GLW`/`VST` — all reaffirmed 09-04 on stated legs; `VST` missed its
  accumulation cut by **0.003** (`C5`) and `DLR`'s hard half was met — **both are near-misses that a
  single session can flip, and neither has a recheck date before 09-15.**

### 4a · KR rows the 09-04 US run assigned — closed out
The 09-04 run named **19 KR ledger rows** (5 rejections + 14 misses) whose observables this US-pure
desk cannot read (`W1` + the `--scope foreign` hard rule), and warned they would cross a second
HANDOVER if the KR desk skipped them again. ✅ **The KR desk's 09-05 run resolved 30 due rows.** The
debt named on 09-04 is discharged; recorded so the cross-desk hand-off is closed rather than dropped.

---

## 5 · What changed in the tape since the last carry (facts only, no verdict)

### 5a · 09-04 was the August payroll session, and the index hid the move
| | 09-03 → **09-04** (settled) |
|---|---|
| tone | **narrow — one sector carried the tape against a lower index** |
| `SPY` | **−0.39%** |
| leaders | **`SMH` +2.61** · `XLK` +0.70 · `XLI` +0.41 · `IWM` +0.28 · `QQQ` +0.18 |
| laggards | `XLY` −1.33 · `XLC` −1.19 · `XLV` −1.04 · `XLE` −0.87 · `GLD` −0.84 · `XLP` −0.80 · `XLF` −0.79 |
| vol | **`^VIX` +1.47% to 14.53** |

★ **`SMH` +2.61% against `SPY` −0.39% is a +3.00pp single-session excess** — larger than branch A of
`S141`, which had just measured the *`AVGO` print* as not moving the sector (§3a). ⚠ Facts only;
whether the payroll print or the semi tape owns this is MACRO's question, not this stage's.

5-session context (08-28 → 09-04): `SMH` **+2.51** · `XLE` **+2.20** · `XLU` +0.82 vs `XLY` **−1.96**
· `XLB` −1.39 · `XLRE` −1.24 · `XLI` −1.06 · `XLP` −1.02. `SPY` **+0.11**.

Book, 09-03 → 09-04: **`ETN` +3.46% · `ANET` +1.22% · `NVDA` +0.84% · `MPC` +0.31% · `AVGO` +0.21% ·
`PSX` +0.17%** · `NUE` −0.53% · `RTX` −0.66% · `MET` −1.62% · `NDAQ` −1.85% · **`HPE` −4.48%**.
⚠ `HPE` gave back most of its 09-03 print pop (+5.04% → −4.48%); `ETN` was the book's best name on
a day `XLI` printed +0.41%.

### 5b · The sweep, asof 2026-09-04 (primary file, Δ column citable)

| sector | wflow | eqflow | Δ | breadth | 🟢/🔴 | flip | n |
|---|---:|---:|---:|---:|---:|:--:|---:|
| **Energy** | **+0.440** | **+0.562** | **+0.054** | 0.19 | 3/0 | False | 16 |
| Health Care | +0.098 | +0.190 | −0.043 | 0.06 | — | False | 32 |
| Utilities | +0.071 | +0.050 | −0.037 | 0.00 | — | False | 15 |
| Materials | −0.025 | −0.107 | −0.037 | 0.17 | — | False | 12 |
| Information Technology | −0.090 | −0.195 | −0.010 | 0.07 | — | False | 56 |
| Real Estate | −0.116 | −0.124 | −0.020 | 0.00 | — | False | 12 |
| Financials | −0.118 | −0.023 | −0.004 | 0.00 | — | False | 47 |
| Consumer Staples | −0.182 | −0.098 | −0.018 | 0.00 | — | False | 19 |
| Consumer Discretionary | −0.255 | −0.251 | −0.004 | 0.04 | — | **True** | 28 |
| **Industrials** | **−0.379** | −0.354 | **+0.082** | 0.02 | — | False | 50 |
| Communication Services | −0.389 | **−0.035** | +0.007 | 0.00 | — | False¹ | 12 |

¹ `D459`, 11th reproduction — see §2 and G3.

Universe: **`wflow` −0.153 · 10 🟢 / 92 🔴 of 299** (09-03: 12🟢/89🔴 — **breadth deteriorated on
both sides**). ★ **Energy is now the only sector positive on level AND Δ AND breadth, and it is
3🟢/0🔴** — the 09-04 run's flagged "level says rank-1, Δ says rank-11" tension **resolved toward the
level in one session** (Δ −0.151 → **+0.054**). ⚠ `XLE` was nonetheless a 09-04 **laggard** (−0.87%);
the flow object and the price object disagree by one day. Handed to ROTATION, unresolved here (P4).
★ **Industrials has the board's largest positive Δ (+0.082) from the board's worst level (−0.379)** —
the second tension of the day, and it lands on the sector `S126` just settled `FIRED-C`.

### 5c · Instrument facts this run adds
- **The 08-28 heal held for a second session.** 1/301 NaN on every one of the last 14 sessions;
  the only name is `EA`, absent on all of them — structurally missing, not a hole.
- ★ **The news-tunnel recovery constant is measured: ~60 seconds of idle.** Dead at t+0/+20/+40s
  after the sweep, alive at t+60/+80/+100s, identical counts. The wall in the sweep is at universe
  positions **0–48 / 49–299**, exact, reproducing the 09-04 position finding on a fresh run.
- **`D427`'s split publication reproduced on two independent pulls**: `T10YIE` carries 09-04,
  `DGS2`/`DGS10`/`DGS5`/`DGS30`/`DFII10` stop at 09-03.
- **Risk-unit membership is not merely re-counted across windows, it is re-drawn**: `ANET`+`ETN`
  merge at 500d/750d but split at 250d; `AVGO`+`NVDA` merge only at 750d; and at 500/750d the merged
  `ANET`+`ETN` unit **spans two book theme labels**, so `MAX_THEME_PCT` counts one risk as two.

---

## 6 · Exposure state carried forward (size context for BET/ALPHA — **not** a size)

| book | reading | state |
|---|---|---|
| **Real KIS account** (`cycle_exposure`, 2026-09-05) | total ≈ **$11,022** · invested **$5,255** ⇒ **52.3% cash** | ✅ **no top-rank cycle GAP**: AI-compute epicenter **17.48%** (bar ≥12%), Energy/refining **10.47%** (bar ≥8%), missile-defense 3.64% (no bar set) |
| **KR contest / timefolio** (`exposure_rule state` + `show --tail 6`) | **85.2% invested vs a 95% target · band gap −9.8pp · 19th consecutive session outside** · verdict **정상** | cumulative **−9.79pp = cash −5.32pp + selection −4.47pp**, **n=18** |

⚠ **Not a cold start** (n=18) and **not `밴드미설정`**. ⚠ **`C23` applies** (§2) — carried side by
side because reconciling them is a human call (P5).
🚨 **`n` has now been flat at 18 for FOUR calendar days.** The 09-01, 09-03 and 09-04 rows exist but
carry **no decomposition columns**, so the denominator the report's own note asks to raise by 1/day
has not moved since 09-02. The 09-04 run recorded this at three days; **it is worse, not resolved.**
Repeating "n=18" reads like a constant when it is a stall.
🚨 **The KR desk measured a second failure on the same instrument this morning**: `exposure_rule`'s
target moved **55% → 95% in one session while the position did not move at all** (`M1266`). ⇒ the
band gap quoted above rests on a target that changed by 40pp for non-market reasons. **Quoted as
inherited context, not as a size input.**
⚠ `exposure_rule` prints **🚨🚨ARMED (`TIMEFOLIO_EXECUTE=1`)** on **all 48 ledger rows**. Recorded
because it is on the instrument's own output. **This run issues no order of any kind.**

---

## 7 · RESEARCH triggers loaded as BINDING constraints (not summarised)

| group | fires when | IDs | binds, this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO and every stage.** ★ `C4` live twice: `P101`'s inversion is **one 5-session window**, and `D497-KR`'s bracket-width criticism is **n=3** and says so. ★ `C5` live: risk units agree at dist 0.40–0.60 and diverge only at the chosen 0.65. ★ `C3` live: **`EA` is *unmeasurable*, not *absent*** |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **any stage citing a test.** ★ `S5` live: the 250d risk-unit window (249 obs) again has the **highest** fit (+0.8511) with a **low** ARI (0.3874). ★ `S2` live: the news-axis null was "no news" and is now measured to be "our own outage" |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · L2 indicators/money_trail.** ★ `D4` **stands down** — no contaminated stretch and no partial bar today (Saturday). ★ `D5` live and *satisfied*: `D427` reproduced on two independent pulls. ★ `D1` live: `R127`-KR's rule — a vendor's silence is not the world's silence |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ `W1` live three ways: the KR `ic_ledger` verdict, `R127`/`R128`-KR's content, and `D497-KR`'s n=3 — all **named, none imported**. ★ `W5` live and *load-bearing*: `P101` is a within-sector dispersion row and its participation legs (21.1% vs 73.0%) carry more information than its mean |
| **L** (lenses) | — | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★ `L3` live: `D497-KR` is a direct attack on this desk's branch-information practice and is carried as dig #4. ★ `L2` live on `MPC`/`PSX`/`VLO` — all three above consensus mean targets on +45–85%/90d revisions |

### Dig list ranked for today (candidate DEEP / PREMORTEM assignments)

| rank | dig | why today |
|---|---|---|
| **1** | **`D490`** — a run that writes `llm_outputs` without a `handoff/` writeback | **this desk is the offender**: 3 of its last 4 runs. It cost the KR desk an ID collision and cost this run a whole fold-in stage (§0/§3a). **Pre-committed to at run end** |
| **2** | 🆕 **`D502`** — the sweep's news failure has a **measured recovery constant (~60s idle)**, not just a burst count | upgrades `D489` from "chunk below 50" to "chunk **and** insert a ≥60s idle after a trip" — the 4th axis is recoverable inside one run |
| **3** | **`D459`** — collapse dual-class issuers before `top1_w` | **11th reproduction**, measured at 0.661 today; silently bars a whole sector verdict again |
| **4** | 🆕 **`D503`** — short-window sector-ETF brackets take bands from measured dispersion (`D93`), not round pp | `D497-KR`'s positive form; three US rows fired C on 0.109/1.042/1.165pp realizations |
| **5** | **`D463`** — check **standing** rejections, not just `due`, before ALPHA tags | `MSTR` is the best 5-session name in IT software (+12.17%) and carries an unexamined rejection |
| **6** | **`D427`** — H.15 series publish on different days | **5th reproduction**, blocking `P121`·`P114`·`P125` for a 2nd consecutive run. `P125` shows the workaround (settle on the *joint* date) — the dig is now "apply that form to every FRED row" |
| **7** | 🆕 **`D504`** — a `D449` row (registered in a MACRO report, absent from the master index) is unscoreable by anyone but its author | `P101` sat unscored for 10 days and was only reached because the KR desk named it; `P102`·`P126`·`P127`·`P128` are in the same state |
| **8** | **`D472`** — a scored row's header still reads `ARMED` | **10 more rows** joined the set today (9 folded in + `P101`) |
| **9** | **`D488`** — the earnings-date field is wrong and every VOID clause reads it | unfixed; cost `S110` a VOID on 09-04 |
| **10** | **`D395`/`D428`** → now **`C29`** — the US desk has no `ic_ledger` | escalated from dig to open contradiction this run (§2): the KR cell clears Bonferroni for a 3rd run against a gate that weights the axis the other way |
| **11** | **`D416`** — the AI-power cycle has no registry row | `P123` settles 09-08; `ETN` was the book's best name on 09-04 (+3.46%) |
| **12** | **`D294`** — `action_bracket` names a binary then prints "none in window" | 7 reproductions; today has no ≤48h binary (Sat), so this is a **PREMORTEM** check, not a MACRO one |
| **13** | **`D446`** — a rolling-window axis states bars-present per name | kept live deliberately: it is the instrument that would have made the 4-run 08-28 outage visible on day one |
| **14** | **`D282`** — DRIFT at +0.6h vs its 3–6h spec | 7 reproductions; the fix is scheduling, i.e. human |
| **15** | **`D379`** — PREFLIGHT reads §5 first | **9th run unwired**; done manually again today |
| **16** | **`D10`** — news-body boilerplate | open code defect, **server console required (P6)**, human-approval item — carried, not re-discovered |
| **17** | **`D9`** — does a holdco mismatch **block** or only **warn** | half-closed; the remaining half is a human call |

### 🆕 Registered by this stage (IDs from `module_evidence next-id D --count 4`; highest existing `D501`)
- **`D502`** — *The sweep's news tunnel has a measured **recovery constant**: it trips at ~49 names /
  ~98 queries and returns after **~60 seconds of idle**. A fan-out is therefore chunked **and**
  back-off-idled, not merely slowed.* **Measured origin:** identical probe **6/6** pre-sweep, **0/4**
  immediately post-sweep, ❌ at t+0/+20/+40s, ✅ at t+60/+80/+100s (3/3, identical count 4102); sweep
  coverage is universe positions **0–48** with `None` at **49–299**, zero exceptions. **This upgrades
  `D489` from a cutoff observation to a repair specification.**
- **`D503`** — *A short-window (≤5 session) sector-ETF excess bracket takes its branch lines from the
  observable's own measured dispersion (`D93`), never from a round pp figure.* **Measured origin:**
  `S126`/`S134`/`S139` all fired C on bands of ±1.65–2.00pp against realizations of
  **0.109 / 1.042 / 1.165pp** (`D497-KR`, n=3, scope-limited). The rows disclosed C as favourite, so
  this is a **width** defect, not a disclosure defect.
- **`D504`** — *A proposition registered inside a `MACRO_REPORT §D` and never written into
  `SCENARIOS.md`'s master index is unscoreable by any run except its own author's next one, and the
  author's next run is exactly the run most likely to be interrupted.* **Measured origin:** `P101`
  settled 09-04 and was reached today only because the 09-05 KR run named it in its own log's §D;
  `P102`·`P126`·`P127`·`P128` sit in the same state right now, with `P102` settling **09-09**.
  **Generalises `D449` from propositions to their settlement path.**
- **`D505`** — *A bracket's verdict and the phenomenon it was built to catch can be one session
  apart, and the desk records the near-miss rather than only the verdict.* **Measured origin:**
  `S141` measured "the `AVGO` print does not move the sector" at **−0.662pp** on 09-03; **`SMH`
  printed +3.00pp excess on 09-04**, 1.7× branch A's line, one bar outside the window. `D242` keeps
  the verdict; nothing currently keeps the near-miss.

---

## 8 · Stale flags and cleared suspensions

| item | asof | state |
|---|---|---|
| `us_top300.csv` cap weights | **2026-07-15** | 🔴 **52 days** — every `wflow` and every `top1_w%` is weighted seven and a half weeks stale (G5). `us_all_v2_candidate.csv` (08-10) exists, **not wired**; switching is a human-approval item |
| `handoff/*.md` carry | **2026-09-05 ~10:0x** | ✅ **fresh (12h)** — the KR desk closed the 2-day gap. ⚠ but it does **not** contain this desk's 09-04 output (§0) |
| `DTWEXBGS` | **2026-08-28** | ⚠ **7 days** — the dollar leg of any policy-vs-risk read is a week behind. Recurring, not new |
| `DGS2`/`DGS10`/`DGS5`/`DGS30`/`DFII10` | **2026-09-03** | 🔴 the **09-04 payroll rate reaction is not in this run at all**; three rows blocked (`D427`, 5th) |
| `08-28` vendor hole | **healed 2026-09-04** | ✅ cleared for a 2nd session. **`D446` stays live** — it is the detector that would have caught the outage on day one, and the healing does not retire it |
| `exposure_rule` ledger `n` | **flat at 18 since 09-02** | 🔴 **4 days** — a stall wearing the clothes of a constant (§6) |
| `S8` date field | `[blank]` | 🔴 **38th run** — human `VOID` or re-registration required (P5) |
| `TIMEFOLIO_EXECUTE=1` armed flag | live on **all 48** ledger rows | 🚨 human-owned operational flag, not an analytical one |

**Cleared suspension converted to a dig instruction:** the 09-04 run's `G2` revocation ("the JSON's
own `delta` column may not be cited at all") **has cleared** — but it cleared because *both* sides of
the subtraction happen to be post-heal, not because anything was fixed. ⇒ **the standing instruction
is: state which baseline a Δ was computed against, every run.** Folded into `D446`'s scope rather
than given a new number.

---

## 9 · Self-refutations and inherited refutations (§4c / `D48`) — written down, not edited away

1. ★★ **The carried IT framing is inverted by this run's own scoring of its own bracket.** `M1251`
   and `M1252` have carried, for four runs, that IT's weak half is **semicap/test** (−0.759 against
   software's +0.092, gap 0.851). `P101` — a row this desk wrote specifically to test that split —
   settles at **software −4.458% vs hardware +2.053%** with participation **21.1% vs 73.0%**, and the
   five worst names in the sector are **EDA and security software** (`ADSK`, `CDNS`, `SNPS`, `PANW`,
   `DDOG`). The carried sentence is not deleted; it is **dated**. What survives is the *shape* of the
   claim (IT is not one bet, dispersion is the widest on the board); what is refuted is the
   *assignment of which half is weak*. ⚠ `C4`: one 5-session window, and `P101` fired **C**, so this
   is a directional observation the bracket did not certify.
2. ★ **The 09-04 run's own headline instrument judgement is confirmed rather than refuted — and the
   confirmation is the smaller finding.** That run recorded, in bold, that the 09-02 conclusion
   ("08-28 is frozen, not lagging; the repaired file is the standing instrument for four weeks") was
   refuted by 24 hours of data. Today is the second session of the heal holding. **Two observations
   of a heal are not proof of permanence either** — the same n=2 error class, now pointing the other
   way. Recorded so the desk does not congratulate itself into the mirror-image mistake.
3. ★ **This stage asserted a diagnosis and then narrowed it inside the same stage.** The preflight's
   first framing of `G1` was the inherited one — *"positional cutoff at 50 names"* — which is a
   description, not a cause. The recovery-clock probe run **after** that sentence was written showed
   the tunnel is **not permanently down but idle-recoverable in ~60s**, which changes the repair from
   "chunk the fan-out" to "chunk **and** back off". The earlier sentence stands in `PREFLIGHT.md`
   §G1(d); the correction is appended as `D502` rather than substituted for it.
4. **Zero self-refutations would itself be a finding.** Three are recorded. All three came from
   **running a measurement**, not from re-reading prose — which is the only kind that has ever
   produced one on this desk.

---

## ✅ EXIT CHECK — HANDOVER

- [x] Shared spines read (`STANDING_VIEW.md` §1 regime · §2 chain head · §5 retracted ledger incl.
      the 09-05 KR block · §6 contradictions · asof chain; `SCENARIOS.md` master index + master
      scoring log incl. the 09-05 KR block), plus `STANDING_VIEW_US.md`, `SCENARIOS_US.md` (every row
      named above opened), `RESEARCH.md` Parts A/B/C, `README.md`.
      **Other-market material opened**: the 09-05 KR run block, for the three **US-owned** rows it
      scored and for `R127`/`R128`. Mechanical ledger cross-queried (`module_report_tags show`).
- [x] **Retracted ledger read BEFORE forming today's view** (§2). No claim here matches a retracted
      entry. `R127`-KR's *general form* is adopted as a US rule with its content left in KR (`W1`).
- [x] **Every past-dated row scored, folded in, or explicitly named.** 9 folded in from the unwritten
      09-04 run (8 scored + 1 VOID), 3 read from the KR desk's log, **1 newly scored (`P101`
      `FIRED-C`)**, 3 blocked-and-named with reference states (`P121`·`P114`·`P125`), `S8` named for
      a 38th time. **0 `EXPIRED`, 0 silent skips.**
- [x] **`reject_ledger.py due` run** — **0 due**, legacy **0**, totals 293/185 reported. The zero is
      shown to be a worked-through cohort (176→185 since 09-04), not a skipped audit.
- [x] **`missed_ledger.py due` run** — **0 due**, legacy **0**, totals 312/207. Sign inversion noted;
      the two ledgers' `excess` columns are **not** summed anywhere in this run.
- [x] **Exposure state read and carried** (§6): 4-state verdict **정상**, target 95% vs current
      85.2%, band gap **−9.8pp**, cumulative **−9.79pp = cash −5.32 + selection −4.47**, **n=18**.
      Not a cold start; not `밴드미설정`. The `n` stall and the KR-measured 55%→95% target jump are
      both flagged as reasons this is context, not a size input.
- [x] 🚨 **Instrument health inherited before any number is trusted** (§1) — `PREFLIGHT.md` read in
      full; every FAIL converted into a named revocation and applied above (no sweep velocity cited;
      no `wflow` verdict on CD or COMM; `--days` carried with every unit count; no cap weight cited
      as current).
- [x] **Self-refutations written down, not edited away** (§9) — three, all from re-measurement.
- [x] Stale rows flagged with `asof`; the one cleared suspension (`G2`'s Δ revocation) converted into
      a standing instruction rather than a silent trust (§8).
- [x] `[measured]` / `[inferred]` tags preserved; the two `[inferred]` carries are named and barred
      from evidence use (§2).
- [x] **RESEARCH triggers loaded as binding constraints**, grouped C/S/D/W + lenses L, each with the
      downstream stage it binds and a live instance (§7).
- [x] `HANDOVER.md` written. **`handoff/*.md` writeback is pre-committed for run end (§0), and it
      explicitly includes the nine folded-in verdicts, `P101`, `M1281`/`M1282`, `C29`, `D502`–`D505`,
      and `ARMED` header hygiene for every row scored (`D472`).**
- [x] No position sizing, no buy/sell language anywhere in the carry (P4).


---

## 📋 RUN LOG — open decisions resolved without a human (unattended run), one line each

1. **`REPORT_DIR` (`industry_us.md` §File-output rules, PROMPT_MAP §6)** — resolved as **copy the
   finalized reports into `REPORT/industry_US/`**, matching existing practice; `module_report_tags
   update` then ran against the default `REPORT/` and reported **80 reports / 297 tickers**
   (2 changed on the final pass). ⚠ Scratch artifacts (`_brief*.json`, `_fred*.json`) were **removed
   from `REPORT/`** after the first copy so the ledger scans reports only.
2. **PREMORTEM's 4 lenses and DEEP's 4 sectors** — resolved as **run IN-CONTEXT and serially, not as
   parallel adversarial agent fan-outs**, matching the documented practice both desks have declared
   for 9+ consecutive runs. **Declared at the top of both files as a weakness**, not omitted.
3. **`handoff_compact` is `OVER` on every file (US run reads 2,838.9 KB vs a 250 KB budget)** —
   resolved as **do NOT run `--apply`**. Compaction rewrites the live analytical carry, which is a
   human-approval item (P5). Budget reported, not acted on.
4. **`P125`/`P121`/`P114` blocked by `D427`** — resolved as **named-and-blocked, NOT `EXPIRED`**.
   `DGS2`/`DFII10` were re-pulled **three times** across the run (full 120d, a 10-day two-series
   call, and a final 8-day call) and stop at **09-03** every time, while `T10YIE` carries 09-04.
   The settle condition has not arrived.
5. **`action_bracket` armed PPI while PREMORTEM declined to bracket it** — resolved as **carry both,
   reconcile neither**, and register the structural cause as `D518` (date-proximity vs information
   content are different selection rules).
6. **New bracket registration** — resolved as **written into `handoff/SCENARIOS_US.md` and the
   `SCENARIOS.md` master index INSIDE the PREMORTEM stage**, not deferred to writeback, because
   `D490`/`D504` are two of this run's own dig items.

**Failed lookups this run: 0.** Every retry that was attempted succeeded or returned a stable,
reproducible stale state (`D427`, three pulls). The one instrument failure — the news tunnel dropping
after the sweep — was **measured rather than worked around** (`D502`) and did not block any stage.
