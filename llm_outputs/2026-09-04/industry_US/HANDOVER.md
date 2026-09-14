# HANDOVER — industry_US · 2026-09-04 (Fri) · Stage 2 / L1·HANDOVER

> Read before anything is decided. Inherits the **analytical carry**, not the coverage ledger.
> Sources read this run: `handoff/STANDING_VIEW.md` (shared spine — §1 regime call, §5 retracted
> ledger, §6 open contradictions, asof chain), `handoff/STANDING_VIEW_US.md` (§2 `M1234`–`M1261`
> and the §3a registry through 2026-09-02), `handoff/SCENARIOS.md` (shared master index + un-split
> master scoring log), `handoff/SCENARIOS_US.md` (every row named below opened in full),
> `handoff/RESEARCH.md` Parts A/B/C, `handoff/README.md`.
> Mechanical ledger cross-queried: `module_report_tags show`.
> **P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.**

---

## 0 · 🚨 The carry is TWO DAYS STALE, and that is this stage's first finding

**`handoff/*.md` was last written 2026-09-02 23:2x–23:3x.** Since then **three desk runs produced
output and none wrote back**:

| run | output written | carry written back |
|---|---|---|
| `industry_US` **2026-09-03** | `SECTOR_FLOW_US.json` + `_REPAIRED.json` + preflight scratch only — **no `PREFLIGHT.md`, no `HANDOVER.md`, no `MACRO_REPORT.md`** | ❌ died inside stage 1 |
| `industry_kr` **2026-09-03** | full run — `HANDOVER` → `BET_SHEET`, registering **`D485-KR`** and **`D486-KR`** | ❌ **none** — both digs exist only in `llm_outputs/2026-09-03/industry_KR/` |
| `industry_kr` **2026-09-04** | an **empty** `preflight/` directory | ❌ died before stage 1 produced a file |

⇒ **This run inherits from 2026-09-02, not from yesterday**, and it must score **two sessions** of
matured rows rather than one. That is done in §2. ⚠ The KR desk's `D485-KR`/`D486-KR` are read from
its run directory and carried here **as KR-owned observations** (`W1` bars importing their
conclusions); this run does not write them into the shared spine on the KR desk's behalf.

---

## 1 · 🚨 Instrument health inherited FIRST (`preflight/PREFLIGHT.md`, written 22:10–22:22 KST)

**PREFLIGHT ran and exists.** Its verdicts govern every number below:

| gate | verdict | what it removes from this run |
|---|---|---|
| **G0** | ✅ **PASS — the 08-28 hole HEALED** (258/301 → **2/301** in 24h) | nothing about the **09-04** tape (NYSE unopened at run time); `EA`/`APH` unscored |
| **G1** | 🔴 sweep news axis **16.72%** · ✅ direct path live | no theme-freshness / velocity / "it is quiet" **from the sweep** |
| **G2** | ✅ scale continuous, true one-session Δ · ★ **clean baseline rebuilt** | 🚫 **the `delta` field inside `SECTOR_FLOW_US.json` may not be cited at all** — use `preflight/_cleanbase.json` |
| **G3** | ✅ list printed (1 flipper) | no `wflow` verdict on **Cons. Disc.** (AMZN 40.2%) or **Comm. Services** (Alphabet 76.6% under two tickers) |
| **G4** | 🔴 **12 / 11 / 10** units across 250/500/750d | no single-number concentration claim; `--days` on the same line |
| **G5** | 🔴 universe **51 days** stale | no cap-weight cited as "current size" |
| **G6** | 🔴 accrual 0.56/day, **1.8×** slow | `kelly_size --ic` is "mechanical 1/4" if used |
| **G7** | 🟡 42/44 `--help` clean; chart live 3/3 | no `margin_history` output |

★ **Two gate changes govern the whole run, and they point in opposite directions.**
1. ✅ **The four-run OBV revocation is LIFTED.** The vendor backfilled 08-28 for **256 more names**
   overnight and returned the 42 already-official bars **byte-identical** (mean |err| 0.000000%).
   The primary `SECTOR_FLOW_US.json` is citable on OBV for the first time since 2026-08-28, and
   **no `SECTOR_FLOW_US_REPAIRED.json` exists today** — a downstream stage that globs for it must
   fall back to the primary file.
   ⚠ **The 09-02 HANDOVER's standing instruction is thereby refuted by 24 hours of data.** It said:
   *"the desk should stop treating this as a lag that will resolve and start treating it as a partial
   session that will sit inside every 20-session window until it rolls out (~2026-09-25) … the
   repaired file is not a one-day workaround but the standing instrument for the next four weeks."*
   **It was a lag. It resolved in one night.** Recorded, not edited away (§8).
2. 🔴 **The healing moves the contamination to the OTHER side of the subtraction.** The stored 09-02
   baseline was scored on holed data. Measured by rescoring 09-02 off today's healed cache:
   mean |Δ| **0.1078** · max **0.5570** · **19 of 299 sign flips**, and at sector level the stored Δ
   is wrong by up to **0.177** — Utilities stored **+0.308** vs clean **+0.131**, Health Care stored
   **−0.207** vs clean **−0.069**. **Three sectors change ordinal rank between the two columns.**
   A clean 09-02 baseline was rebuilt inside PREFLIGHT, so Δ is citable **as a magnitude** today —
   from `preflight/_cleanbase.json`, never from the JSON's own column.

**Citable flow object today: the PRIMARY `SECTOR_FLOW_US.json`** (298 scored, 3-axis `nonews`,
asof **2026-09-03**), **plus `preflight/_cleanbase.json` for every Δ.**

---

## 2 · Inherited standing view — the regime call carried in

**Carried from the 2026-09-02 `industry_US` asof entry, unchanged unless MACRO measures otherwise:**

- **The repricing is a POLICY-PATH repricing, not an inflation repricing.** `[measured]` `M1234`:
  the 3-session (Δbreakeven − Δreal) spread sat at **−11.0bp = the 5.2nd percentile of 252**.
  `M1235`: the 09-01 curve **bear-flattened** (`^FVX` +5.0 > `^TNX` +3.8 > `^TYX` +1.9), the opposite
  of a term-premium event. Carried as **`P121`**, which settles **at the first FRED close covering
  today** — and **today is the August payroll print**, so MACRO inherits this as the live question.
- **US credit sits at a one-year TIGHT while global yields print multi-decade highs.** `[measured]`
  `M1236`: `hy_oas` **2.63 = 0.4th percentile** of trailing 252, −6bp over 5 sessions; `ig_oas` 0.80;
  `NFCI` −0.558 and easing. This is the single strongest fact standing **against** the `FIN UW`.
- **Energy's OW is a CHAIN-POSITION bet whose centre of gravity is moving upstream.** `[measured]`
  `M1245`: level ordering refining > services > midstream > barrel, **Δ ordering exactly reversed**.
  `M1246`: Energy was **16 of 16 positive with zero reds** — the only sector where the label is the
  right unit.
- **IT is not one bet, and the split is wider than most whole-sector gaps.** `[measured]` `M1251`:
  software/services/security (n=21) **+0.092** vs semicap/test (n=6) **−0.759** ⇒ gap **0.851**.
  `M1252`: IT dispersion **1.878, the widest on the board**.
- **The same input is priced in opposite directions in Energy and IT.** `[measured]` `M1253`:
  Energy estimates +48–82%/90d at 52-week highs with consensus targets **below** price; IT estimates
  +6–51% at 6–26% below highs with targets **30–61% above** price ⇒ lens `B2` loads in Energy and
  does not load in IT.
- **Utilities' binding constraint is regulatory, not industrial.** `[measured]` `M1257`/`M1258`: every
  equipment name distributed; the "ghost demand" attack is **two** grid operators (ERCOT halt at 6
  outlets; PJM removed a Meta-backed 750MW project).
- **Communication Services has been carried on a number wrong by ~0.7.** `[measured]` `M1206`/`D459`.
  ★ **Reproduced again today at 0.690** (§4c).
- **Two open, unowned exposures.** `T` and `CBRE` are **16.6% of real invested capital with no
  thesis** (`C23`/`M1169`). ⚠ `S107`, the first falsifiable statement ever registered about `T`,
  **settled today at C** (§2a) — so the residual survives its own first test without resolving.

**`[inferred]` rows carried but NOT citable as evidence:** the "duration event is global" reading
(EVENT_ALPHA Card 3, `STORY-ONLY`); the "memory shortage is demand not capacity" reading on `MU`.

### §5 retracted ledger — read BEFORE forming today's view
Nothing in today's opening frame matches a retracted entry. Two recent retractions bind this run:
- **`R120`** (2026-09-01) — the 5m-proxy error bound. ★ **Now moot**: the proxy is not used at all
  today (G0). The retraction stands on the record; the instrument it governed is retired.
- **`R122`-KR** (2026-09-02) — missing bars move a benchmark's window **start**. `W1` bars importing
  the KR conclusion, but the **check** transfers and was re-run: `SPY` has **0 missing bars** in the
  20-session window ending 09-03 (verified 0/16 on the direct probe across all 13 sessions) ⇒ the US
  `rs20` axis is not exposed to `D468-KR`. Stated because it was checked, not assumed.

### §6 open contradictions — carried, not resolved
| id | state this run |
|---|---|
| **`C21`** RSI convention | untouched. ★ Its 08-28 rider is **retired** — no window spanning 08-28 is holed any more (G0) |
| **`C22`** the two ledgers name different hands | ★ **the 15-run drought of samples ENDS today** — 12 rejection rows and 20 miss rows came due at once (§3) |
| **`C23`** three books, none self-identifying | ★ **reproduced a fifth time.** `cycle_exposure` reads the **real KIS** account (**$5,254 invested of ≈$11,022 ⇒ 52.3% cash**); `exposure_rule show` reads the **KR contest** book (**85.2% invested, band gap −9.8pp, 18th consecutive session outside**); `module_paper_book` reads a third. **Human call (P5)** |
| **`C24`** copper spec at the 100th percentile vs a Materials bucket | ⚠ Materials is now **+0.013 `wflow` / −0.062 `eqflow`**, i.e. flat-to-negative, with clean Δ **−0.035**. The metals/gases split inside one label still has no escape hatch. Carried a **5th** run |
| **`C25`** two instruments read OBV's sign oppositely | ★ **the specific US instance is dissolved**: it arose because one interior bar was missing. With 08-28 restored, the sweep and `module_chart` agree on `DLR` today (매집 / 누적 +51%). ⚠ **This does not close `C25`** — it removes the *cause* the desk had identified, which is a different claim |
| **`C26`** primary vs repaired sweep disagree | ✅ **CLOSED by disappearance, not by resolution.** There is no repaired file today. Recorded as closed-because-the-instrument-is-gone, which is not the same as the two having been reconciled |
| **`C27`** `MSTR`'s two rejections give opposite answers | carried; `due` surfaces them **09-18 / 09-22** for a human resolve (P5). ⚠ `MSTR` is **9th of 298 by flow today (+0.761)** with OBV **+0.425 매집** — the pressure is up again |

### 🆕 `C28` opened by this stage
**A revival condition can be true on the day it is written, and nothing checks.** `LYV` was rejected
2026-07-28 under `H.밸류소진` with the OR-leg *"operating margin turns positive"*. Measured today:
TTM operating margin **+2.935%** (opinc 771.2M / rev 26,272.5M, TTM ending 2026-06-30) — **and it was
already +2.903% at the TTM ending 2026-03-31, the latest print available on the day the row was
written.** ⇒ **the row was revivable on day one and rejected nothing for 38 days.** Resolved as
`revived` per `D242` (the stored observable is met; improvising a stricter one is the forbidden move),
with the construction defect logged as **`D487`** rather than used as an excuse to refuse.

---

## 3 · Scenario settlement — two sessions of matured rows, every one named

> Run clock **KST 22:10 → 22:35 = 09:10 → 09:35 ET.** Last settled US session **2026-09-03**.
> `D426` applies: a row settling on the **09-04** close cannot be scored by a desk that fires at the
> open. **August payrolls printed 08:30 ET today**, i.e. ~40 minutes before this run began.

**Scored this run: 8. VOID: 1. `EXPIRED`: 0. Silent skips: 0. Not-yet-settled and named: 6.**

### 3a · Scored — all against the pre-registered observable only (`D242`)

| row | observable | measured | verdict |
|---|---|---|---|
| **`S109`** | `FRO` exc5 vs `SPY`, 08-26 → **09-02** close | `FRO` 41.20 → **45.42**; `SPY` 766.08 → 765.16 ⇒ **+10.363pp** | ★ **FIRED-A** (≥ +8.043) |
| **`S105`** | [`MRVL` exc10] − [`AVGO` exc10] @ 09-03 | `MRVL` 251.01 → 208.83 (**−18.190**) · `AVGO` 364.03 → 357.16 (**−3.273**) ⇒ **−14.917pp** | ★★ **FIRED-A** (≤ −10.836) |
| **`S106`** | `MSFT` exc10 vs `SPY` @ 09-03 | 481.15 → 510.12 ⇒ **+4.635pp** | **FIRED-C** |
| **`S107`** | `EW{T,VZ}` exc10 vs `SPY` @ 09-03 | `T` +2.749 · `VZ` +1.460 ⇒ **+2.105pp** | **FIRED-C** |
| **`S110`** | [`HPE` exc5] − [`DELL` exc5] @ 09-03 | `HPE` −0.213 · `DELL` **+9.076** ⇒ **−9.289pp** (would be B) | 🚨 **VOID** — see 3b |
| **`S114`** | `EW{NUE,STLD}` exc5, 08-26 → 09-03 | `NUE` +2.900 · `STLD` +3.369 ⇒ **+3.134pp** | ★ **FIRED-B** (≥ +0.826) |
| **`S132`** | `AVGO` exc1, first settled close after the print | 367.24 → 357.16 (**−2.745%**) vs `SPY` +1.047% ⇒ **−3.792pp** | **FIRED-C** (band ±9.00) |
| **`S138`** | same observable, wider band | **−3.792pp** | **FIRED-C** (band ±11.00) |
| **`S141`** | `SMH` exc1 vs `SPY`, 09-02 → 09-03 | 550.48 → 552.60 ⇒ **−0.662pp** | **FIRED-C** (A +1.802 / B −1.732) |

**What the scored rows change, stated rather than left in the table:**

- ★★ **`S105` is the most informative settle of the run.** It was registered at **+25.780 = the 93.7th
  percentile, already near branch B**, with B disclosed as *"displacement — `AVGO`'s thesis line must
  be rewritten"* and **A as the adversarial ask**. The spread moved **−40.7pp in ten sessions** and
  fired **A**. ⇒ **The Google→`MRVL` warrant did not displace `AVGO`.** `AVGO`'s carried §3a thesis
  line survives, and `S116`'s B-leaning read that `MRVL` took the socket is **falsified**. The
  mechanism is visible in the legs: `MRVL` printed on **08-27 AMC** (EPS 0.94 vs 0.93, **+0.99%
  surprise**) and lost **18.19pp of excess**; `AVGO` printed on **09-02 AMC** (EPS 3.32 vs 3.24,
  **+2.53% surprise**) and lost only 3.27pp.
- ★ **`S114` FIRED-B was the branch that carried the row**, needing **+9.45pp of mean reversion from
  the 3rd percentile**, and it got **+11.76pp**. ⇒ The steel pair fully reverted and the tariff-thread
  attribution on a **held** name (`NUE`) does not convict it on this window. ⚠ **Read against
  `M808`'s re-statement**: branch B's meaning was never altered by the 08-22 tariff reversal, so this
  verdict is clean. VOID checked: **no Section 232 steel action or steel-specific tariff** inside
  08-26 → 09-03 (23 `Section 232` hits over 12 days are aluminium premium, solar cells/wafers, pharma
  pricing and Canada trade-talk copy — **zero steel actions**; `steel tariff` 6 hits, none an action).
- ★ **`S109` FIRED-A means `M45` did NOT replicate.** The freight leg **was** paid: `FRO` +10.36pp
  excess over five sessions. ⚠ Two disclosures the row itself demands: **A was pre-declared the WEAK
  branch** (registration state +9.467 = 89.3rd percentile), so this is a persistence result, not a
  surprise; and **`FRO` printed Q2 earnings on 2026-08-28, inside the window**, which is **not** in
  the row's anti-signal list — the contaminant is disclosed rather than used to void a settle after
  the fact. VOID checked: no `FRO` corporate action (`Frontline Ltd` 1 hit/10d), no OPEC+ supply
  decision (`OPEC output` 2 hits) and no tanker-rate collapse — rates rose.
- **`S132` / `S138` / `S141` all fired C, and the C is the finding.** `AVGO` **beat** (+2.53% EPS
  surprise) and the tape **sold it**: −2.745% on a +1.047% `SPY` session. The excess **−3.792pp** sits
  inside both name-level bands and `SMH`'s **−0.662pp** sits inside the sector band. ⇒ **Neither the
  "discount was wrong" nor the "franchise loss is real" reading survives**, and the sector did not
  move on the print at all. ★ `S141` was written to ask *"does the print move the sector"* and the
  answer is **no, measurably**. VOID checked: no `AVGO` guidance withdrawal (0 hits), no M&A (0), and
  the only export-control item in the 09-02 → 09-03 window is a **draft**-rules report — the exact
  class the row pre-declared as non-voiding.
- **`S106` and `S107` fired C and change nothing**, which both rows disclosed in advance as the modal
  outcome (C ≈ 90% and ≈ 70%). ⚠ `S107` matters anyway: it was **the first falsifiable statement ever
  registered about `T`**, a position that is ~13.8% of real invested capital, and it **decayed from
  the 92.9th percentile at registration to +2.105pp** — the orphan is still an orphan, now with one
  uninformative test behind it rather than none.

### 3b · 🚨 `S110` is VOID, and the reason is an instrument defect this run measured

`S110`'s anti-signal is *"an earnings print at **either** name inside the window"* (08-27 close →
09-03 close). **Both** names printed inside it:

| name | actual print | source | surprise |
|---|---|---|---|
| **`DELL`** | **2026-09-01 16:00 ET** | `yfinance Ticker.earnings_dates` | EPS **7.04** vs 4.92 = **+43.14%** |
| **`HPE`** | **2026-09-02 16:00 ET** | same | EPS **1.11** vs 0.94 = **+18.41%** |

⇒ `DELL`'s **+9.076pp** exc5 is a print reaction, `HPE`'s 09-03 **+5.04%** session is its own print
reaction, and the "pair divergence" the row was written to measure is **two earnings prints**.
**VOID, not FIRED-B** — the measured −9.289pp is recorded but carries no verdict.

★ **The registration was wrong on a checkable fact, and it said so in advance in the wrong
direction:** the row reads *"`module_fundamentals_us` puts `HPE`'s next print at **2026-09-04**, i.e.
one day **after** the settle — outside by one session, **and that margin is stated because it is
thin**."* The margin was not thin. It was **negative by two sessions**.

**Root cause, reproduced on demand:** `module_fundamentals_us` renders *"다음 실적 발표"* from
`yfinance`'s forward calendar field, which **today still reports 2026-09-03 for BOTH `HPE` and `AVGO`
— two days after both actually printed.** The truth lives in `Ticker.earnings_dates`, which carries a
timestamp *and* the reported EPS. ⇒ registered as **`D488`** (§7). **This field is what every VOID
clause in `SCENARIOS_US.md` is checked against.**

★ **The same defect resolves `D420` in the opposite direction from the issuer calendar.** The dispute
was `catalyst_calendar` (09-02) vs the issuer calendar (09-03) for `AVGO`. `earnings_dates` settles
it: **2026-09-02 16:00 ET, EPS 3.32 reported.** **`catalyst_calendar` was right**; the calendar field
was wrong. ⇒ `S132`/`S138`/`S141` do settle on the 09-03 close, as scored above.

★ **And it contaminates `S105`'s registration note, which is corrected rather than deleted.** `S105`
reads *"`AVGO` has no print inside the window (next 2026-09-04, checked at registration)"*. `AVGO`
printed **09-02, inside the 08-20 → 09-03 window.** An earnings print is **not** in `S105`'s VOID
clause (which names only change-of-control/M&A), so **`S105` FIRED-A stands** — but the leg is
post-print and that is now on the record.

### 3c · Not yet settled — named rather than dropped

| row | settles | why not scored | reference state (**explicitly NOT a score**, `D242`) |
|---|---|---|---|
| **`S126`** | 09-04 close | `XLI` exc5 needs today's close | 4 of 5 sessions run; A ≥ −0.087 / B ≤ −2.500 |
| **`S134`** | 09-04 close | `XLF` exc5 needs today's close | 08-28 → 09-03 (4 of 5) = **+0.295pp**; A ≥ +2.00 / B ≤ −2.00 |
| **`S139`** | 09-04 close | `EW{XLU,XLRE,XLP}` exc3 needs today's close | 09-01 → 09-03 (2 of 3) = **−0.964pp** (`XLU` −0.391 · `XLRE` −1.018 · `XLP` −1.483); A ≥ +1.653 / B ≤ −1.757 |
| **`P114`** · **`P121`** | first FRED close covering 09-04 | FRED daily yields for 09-04 publish after the close | `P121` needs `DGS2` ≥ 4.50 **and** `T10YIE` ≤ 2.36 for A; ≤ 4.18 for B. **MACRO pulls the 09-03 state** |
| **`S67-KR`** | 09-04 | KR-registered, KR observable | opened per the split rule; **no US-desk observable** — left to the KR desk |
| **`S138`** | ✅ settled above | — | the print was 09-02, not 09-03 (`D420` resolved) |

**Still armed, no date reached**: `S122`(09-30) · `S123`(09-12) · `S125`(09-11) · `S127`(09-08) ·
`S128`(09-09) · `S129`(09-09) · `S130`(09-10, dead thread) · `S133`(09-14) · `S135`(09-11) ·
`S136`/`S137`(09-09) · `S140`(09-08) · `S142`(09-11) · `P111`(09-14) · `P122`/`P123`(09-08) ·
`P124`(09-18) · `P128`(09-08) · `P67` · `P81` · `P85` · `P87`–`P89` · `P115`–`P117` · `S3` · `S4`.

### 3d · Named again rather than dropped
**`S8` — 36th consecutive run unscoreable.** The date field is still `[blank]`. **A human must
`VOID` it or re-register it with a date (P5).** This is the 36th time this line has been written,
which is itself the finding.

⚠ **`D472` (registered 09-02) reproduces and is now measured**: `grep ARMED SCENARIOS_US.md` still
returns rows whose settle dates are past and whose verdicts are in the master log. **Eight more rows
joined that set today** (§3a). The headers were not updated by this run either — writeback happens at
run end, and the defect is that scoring and header-hygiene are two different writes.

---

## 4 · Both ledgers audited — and after 15 quiet runs, both have work

| ledger | total | resolved | legacy (no condition) | **due today** |
|---|---:|---:|---:|---:|
| `reject_ledger` | **293** | 169 → **176** | **0** | **12** (7 US · 5 KR) |
| `missed_ledger` | **308** | 183 → **186** | **0** | **20** (6 US · 14 KR) |

★ **The "0 due, 15 consecutive runs" streak ends today.** Replayed to confirm it is real and not an
instrument change: `reject_ledger.py due --asof 2026-09-02` returns **0**, `--asof 2026-09-04`
returns **12**, on the identical 293-row ledger — every one of the 12 carries `recheck_date`
**2026-09-04** (`D+0`; the leading date printed on each line is the *rejection* date, not the
recheck date). This is a scheduled cohort maturing, not a defect.

### 4a · US rejection rows — resolved this run

| ticker | rejected | stored condition | measured @ 09-03 settled close | outcome |
|---|---|---|---|---|
| **`AAPL`** | 08-14 `B.모멘텀only` | OBV 매집 **AND** rs20 > −5.0 | OBV **매집 +0.109** ✅ · rs20 **+4.5** ✅ (flow +0.276 🟢, rs60 +8.1) | ★ **REVIVED** |
| **`LYV`** | 07-28 `H.밸류소진` | op. margin turns positive **OR** rs20 > +5 | TTM op. margin **+2.935%** ✅ · rs20 −3.0 ❌ | ★ **REVIVED** — see `C28`/`D487` |
| `GLW` | 08-14 `C.차트붕괴` | OBV 매집 **AND** rs20 > 0 | OBV **분산 −0.127** ❌ · rs20 −7.7 ❌ | reaffirmed |
| `VST` | 08-14 `G.섹터중립` | flow > 0 **AND** OBV 매집 | flow **+0.128** ✅ · OBV **중립 +0.047** ❌ — **misses the 0.05 accumulation cut by 0.003** (`C5`) | reaffirmed |
| `CIEN` | 08-21 `A.flow미도착` | rs60 > −15 **AND** OBV 매집; **or** `S86`/`S96` branch A | rs60 **−32.6** ❌ · OBV 분산 ❌ · **`S86` and `S96` both FIRED-B** ❌ | reaffirmed |
| `VLO` | 08-21 `H.밸류소진` | back **below** consensus mean target w/ next-yr breadth positive; **or** distillate−gasoline ≥ +4.0/bbl by 08-27 (`P83`-A) w/ fwd P/E < 12 | price **370.69 vs mean target 319.63** — **above**, −13.8% implied ❌ (breadth 13↑/2↓ ✅ but it is the AND-partner); **`P83` FIRED-B, the spread collapsed −13.562** ❌ (fwd P/E 11.88 ✅, also an AND-partner) | reaffirmed |
| `DLR` | 08-21 `A.flow미도착` | above its Bollinger coil w/ OBV 매집 on **both** instruments; **or** `ig_oas` ≥ 0.85 (`S111`-A) w/ rs20 > 0 | ★ **the hard half is MET** — sweep OBV **+0.147 매집** *and* `module_chart` **누적, 20d slope +51%**; but the band has **expanded to 10.0%** with price at the **middle**, turn NEUTRAL/CHOP, ignition `close>191.67` unfired, RSI 32.5 ❌. **`S111` FIRED-C at `ig_oas` 0.79** ❌ | reaffirmed — **the closest of the seven** |

### 4b · US miss rows — resolved this run

| ticker | missed | stored condition | measured | outcome |
|---|---|---|---|---|
| `CIEN` | 08-14 `Q.확신부족` | rs60 > −5.0 **AND** flow > +0.5 | −32.6 ❌ · −0.461 ❌ | reaffirmed |
| `PH` | 08-14 `M.숏리스트탈락` | Δflow > 0 **AND** rs20 > +5.0 | clean Δ **−0.291** ❌ · rs20 −10.4 ❌ | reaffirmed |
| **`APH`** | 08-20 `M.숏리스트탈락` | OBV 매집 w/ surge ≥ 1.2; **or** `S96` settles EARLY | 🚨 **leg A is UNMEASURABLE, not failed** — `APH` carries NaN Close at 08-28/09-01/09-02/09-03 and is one of the **2 names dropped from the scored set**; leg B: **`S96` FIRED-B** ❌ | reaffirmed, **measurement-blocked** |

### 4c · US miss rows deferred to ALPHA **within this run** — named, not carried
Three rows' conditions are **conditional on this run's own DEEP / EVENT_ALPHA output** and cannot be
evaluated at HANDOVER. They are resolved at ALPHA, not next run:
- **`MRK`** — *"appears in a `SECTOR_DEEP_HLTH` value-chain node with a named driver, **or** rs20 > 0
  while a Health Care DEEP slot is taken."* rs20 is **+18.1** ✅, so **this resolves the moment
  ROTATION allocates or declines a HLTH slot.**
- **`AXON`** — *"an INDU DEEP or EVENT_ALPHA card names `AXON`, **or** `AXON` in `US_LIVE_SHORTLIST`
  with a volume-confirmed green on a run where `vel_axis` is true."* ★ **Leg B is structurally
  unreachable today — `vel_axis` is FALSE** (G1). ⚠ And `AXON` carries **the largest clean Δ on the
  whole board, +0.838**, so leg A is live and EVENT_ALPHA must look at it deliberately rather than
  by luck.
- **`ECL`** — *"a MATR DEEP maps the specialty-chemicals node with a named driver, **or** rs60 > +15
  while OBV 매집."* Leg B fails now (rs60 **+0.6**); leg A depends on this run.

### 4d · KR rows due — named and assigned, not silently carried
**Rejections (5):** `015760` 한국전력 · `267260` HD현대일렉트릭 · `007340` DN오토모티브 ·
`089860` 롯데렌탈 · `439260` 대한조선.
**Misses (14):** `181710` NHN · `078930` GS · `005830` DB손해보험 · `003230` 삼양식품 ·
`375500` DL이앤씨 · `000270` 기아 · `034020` 두산에너빌리티 · `000720` 현대건설 · `005380` 현대차 ·
`006360` GS건설 ×2 · `010130` 고려아연 · `128940` 한미약품 · `361610` SK아이이테크놀로지.
**Every one of the 19 has a KIS investor-flow observable** (외국인/기관 20일 순매수) that this
US-pure desk does not read — `W1` and the `--scope foreign` hard rule both bar it. ⇒ **assigned to
`industry_kr`, whose 09-03 and 09-04 runs did not write back (§0).** ⚠ **If the KR desk's next run
also skips them they will have crossed two HANDOVERs**, which is the process failure `carryover.md`
names. Recorded here so the debt is visible from either desk.

🚨 **`D463` binds ALPHA this run and is loaded now, not at ALPHA.** `due` answers *"what is owed a
re-check"*, not *"is this name currently rejected."* Standing rejections that will be live at ALPHA:
- **`CRM`** — 08-31 `B.모멘텀only`, revives **09-30**; needs rs20 > +20 ✅ (**+41.0**) **AND** a new
  dated catalyst inside 30 days. ⚠ `CRM` is **rank-3 by flow today (+0.917)** with velocity **1.51
  (direct query, outside the sweep window)**.
- **`INTU`** — 08-31 `G.섹터중립`, revives 09-30; needs *IT returns to OW* or z < −1.0.
- **`MSTR`** — 09-01 `L.vehicle없음`; **9th of 298 by flow (+0.761)**, OBV **+0.425 매집**.
- **`RTX`**-thread — 09-01 `K.본문반증`. ⚠ `RTX` is **held** and is today's **5th-worst name on the
  board (−0.800, OBV −0.312 분산, rs20 −10.1)**.

---

## 5 · What changed in the tape since the last carry (facts only, no verdict)

### 5a · Two settled sessions, and the second one reversed the first
| | 09-01 → 09-02 | **09-02 → 09-03** |
|---|---|---|
| tone | (carried) | **broad risk-on** |
| `SPY` | — | **+1.05%** |
| leaders | — | GLD +1.85 · **XLF +1.56** · XLY +1.39 · XLK +1.29 · XLRE +1.19 · QQQ +1.19 |
| laggards | — | XLP −0.32 · UUP −0.57 · XLB −0.62 · **XLE −0.74** |
| vol | — | **`^VIX` −5.79% to 14.32** |

Book, 09-02 → 09-03: **`HPE` +5.04% · `NDAQ` +3.12% · `MET` +2.91% · `ANET` +2.87% · `NVDA` +1.80% ·
`ETN` +1.60% · `RTX` +0.67% · `MPC` +0.18%** · `PSX` −0.56% · `NUE` −0.57% · **`AVGO` −2.74%**.
⚠ **`XLE` was the day's worst major sector** while the desk's Energy OW is its highest-conviction
carry — noted as a fact, resolved by ROTATION, not here.

### 5b · The healed sweep, asof 2026-09-03

| sector | wflow | eqflow | **clean Δ** | breadth | green/red | flip | n |
|---|---:|---:|---:|---:|---:|:--:|---:|
| **Energy** | **+0.386** | **+0.506** | **−0.151** | 0.12 | 2/0 | False | 16 |
| Health Care | +0.140 | +0.240 | −0.069 | 0.06 | 2/3 | False | 32 |
| Utilities | +0.108 | +0.091 | **+0.131** | 0.00 | 0/1 | False | 15 |
| Materials | +0.013 | −0.062 | −0.035 | 0.17 | 2/2 | False | 12 |
| Information Technology | −0.080 | −0.190 | +0.018 | 0.07 | 4/18 | False | 55 |
| Real Estate | −0.096 | −0.101 | +0.091 | 0.00 | 0/3 | False | 12 |
| Financials | −0.114 | −0.039 | **+0.077** | 0.00 | 0/10 | False | 47 |
| Consumer Staples | −0.164 | −0.102 | −0.031 | 0.00 | 0/5 | False | 19 |
| Consumer Discretionary | −0.251 | −0.251 | +0.023 | 0.04 | 1/14 | **True** | 28 |
| Communication Services | −0.396 | **+0.029** | +0.058 | 0.00 | 0/3 | False¹ | 12 |
| Industrials | **−0.461** | −0.398 | +0.051 | 0.02 | 1/30 | False | 50 |

¹ ★ **`D459` reproduces at 0.690.** Alphabet is **76.6%** of the bucket under two tickers
(`GOOGL` 38.3% flow −0.562 + `GOOG` 38.3% flow −0.651); ex-both-classes `wflow` is **+0.294**, and
the instrument prints `top1_flips_sign: False`. The other ten names are **7 accumulating / 3 not**
(`WBD` +0.521 · `VZ` +0.474 · `META` +0.399 · `T` +0.400 · `CMCSA` +0.317 · `DIS` +0.236 ·
`NFLX` +0.056 vs `LYV` −0.386 · `TTWO` −0.367 · `TMUS` −0.091).

Universe: **`wflow` −0.152 · eqflow-basis 12 🟢 · 89 🔴 of 298.** (09-02: 6🟢/99🔴 — **breadth
improved on both sides of the count.**) Greens include `DELL` +1.000 · `SLB` +0.956 · `CRM` +0.917 ·
`MDT` +0.881 · `DE` +0.872 · `CTVA` +0.839 · **`HPE` +0.800** · `NEM` +0.783 · `MSTR` +0.761.

★ **The Δ column and the level column disagree about Energy, and the Δ is the newer information.**
Energy is rank-1 on level (+0.386) and **rank-11 on clean Δ (−0.151)** — the only sector where those
two disagree that violently. `XLE` −0.74% on 09-03 is the third instrument saying the same thing.
⇒ **handed to ROTATION as the run's primary tension**, unresolved here (P4).

### 5c · Instrument facts this run adds
- **The 08-28 hole healed**: 258 → 2 missing in 24h; the 42 already-official bars returned
  **byte-identical** (0.000000% mean and max error) ⇒ additive backfill, not a rewrite.
- **The stored 09-02 baseline is contaminated by mean 0.1078 / max 0.5570 / 19 sign flips**, measured
  by rescoring 09-02 on healed data. Worst: `CVS` −0.615→−0.147 · `TRI` +0.031→+0.517 ·
  `FANG` +0.151→+0.702 · `LLY` +0.433→−0.124 · **`ANET` −0.284→−0.720**.
- ★ **The news-axis diagnosis of 09-02 is OVERTURNED by its own method.** That run prescribed **"≥9s
  request spacing"** after finding 7/7 `None`s flip at 9s. Today, on a fresh fixed ten-name set:
  **8/10 return real velocities at 1.5s**, the **same 8** at 9s, **0 flips on cadence**; and a
  **40-name / 80-query burst at ~0s spacing scored 40/40**. The true signature is **positional** —
  the sweep measured universe positions **0–49 and nothing after**. ⇒ spacing is not the variable;
  **burst volume inside one sweep** is.
- **Two ticker-token false positives recorded, not acted on**: `AME` returns **6159** 7-day foreign
  hits and `HES` **6364** — three-letter tickers colliding with ordinary English tokens.

---

## 6 · Exposure state carried forward (size context for BET/ALPHA — **not** a size)

| book | reading | state |
|---|---|---|
| **Real KIS account** (`cycle_exposure`, 2026-09-04) | total ≈ **$11,022** · invested **$5,254** ⇒ **52.3% cash** | ✅ **no top-rank cycle GAP**: AI-compute epicenter **17.54%** (bar ≥12%, `NVDA`+`ANET`), Energy/refining **10.21%** (bar ≥8%, `MPC`+`PSX`), missile-defense 3.64% (`RTX`, no bar set) |
| **KR contest / timefolio** (`exposure_rule show`) | **85.2% invested vs a 95% target · band gap −9.8pp · 18th consecutive session outside** · verdict **정상** | cumulative excess **−9.79pp = cash −5.32pp + selection −4.47pp**, **n=18** |

⚠ **Not a cold start** (n=18). ⚠ The state is **not** `밴드미설정`. ⚠ **`C23` applies** — two books,
neither output says which is authoritative for research; carried side by side because reconciling
them is a human call (P5).
⚠ **`n` has not moved in three calendar days.** The 09-03 and 09-04 rows exist but carry **no
decomposition columns**, so the denominator that the report's own note asks to raise by 1/day is
**flat at 18 for a third run**. Recorded because "n=18" repeated three times reads like a constant
when it is a stall.
⚠ `exposure_rule` prints **🚨🚨ARMED (`TIMEFOLIO_EXECUTE=1`)** on every row — recorded because it is
on the instrument's own output. **This run issues no order of any kind.**

---

## 7 · RESEARCH triggers loaded as BINDING constraints (not summarised)

| group | fires when | IDs | binds, this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO and every stage.** ★ `C5` live twice: `VST`'s reject stands on OBV **+0.047 vs a 0.05 cut**; risk units agree at dist 0.40–0.60 and diverge only at the chosen 0.65. ★ `C3` live: `APH` is *unmeasurable*, not *absent* |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **any stage citing a test.** ★ `S5` live: the 250d risk-unit window (249 obs) again has the **highest** fit (+0.8511) with the **second-lowest** ARI (0.3188) |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · L2 indicators/money_trail.** ★ `D4` **stands down** — 08-28 is no longer a contaminated stretch. ★ `D1`/`D5` live: the earnings-date field and `earnings_dates` are two venues that **disagree by two days** (`D488`) |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ `W1` live: 19 KR ledger rows and `D485-KR`/`D486-KR` may be **named** but not **imported** · ★ `W5` live: `M1251`'s IT gap 0.851 and `M1252`'s dispersion 1.878 both stand on healed data |
| **L** (lenses) | — | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★ `L2` live on `MPC`/`PSX`/`VLO` — all three trade **above** consensus mean targets on +45–85%/90d revisions; `VLO`'s reject was reaffirmed on exactly that |

### Dig list ranked for today (candidate DEEP / PREMORTEM assignments)

| rank | dig | why today |
|---|---|---|
| **1** | 🆕 **`D488`** — the earnings-date field is wrong and every VOID clause reads it | **cost one row a VOID and one row a false registration note today** (`S110`, `S105`); the fix is one field swap to `Ticker.earnings_dates` |
| **2** | **`D459`** — collapse dual-class issuers before `top1_w` | reproduced at **0.690**; silently bars a whole sector verdict for a **10th** run |
| **3** | **`D463`** — check **standing** rejections, not just `due`, before ALPHA tags | `CRM` (rank-3) and `MSTR` (rank-9) both carry standing rejections **and** both cleared their price legs |
| **4** | 🆕 **`D489`** — the sweep's news axis dies at a **fixed burst count**, not a spacing | falsified the 09-02 prescription today; a chunked/back-off fetch would restore the 4th axis outright |
| **5** | 🆕 **`D487`** — a revival condition that is already true when written | `LYV` sat rejected for 38 days behind a condition met on day one |
| **6** | **`D294`** — `action_bracket` names a binary then prints "none in window" | **7 reproductions**; today's binary (**August NFP**) already printed |
| **7** | 🆕 **`D490`** — three consecutive runs wrote outputs and no carry | §0; the handoff spine is 2 days behind its own `llm_outputs` |
| **8** | **`D472`** — a scored row's header still reads `ARMED` | **8 more rows** joined the set today |
| **9** | **`D416`** — the AI-power cycle has no registry row | `P123` settles 09-08; Utilities is the only sector with a positive clean Δ **and** a positive level |
| **10** | **`D395`/`D428`** — the US desk has no `ic_ledger` of its own | the 🟢 gate rests on `vol_surge`; only the KR desk has measured its IC sign, and `W1` bars using it |
| **11** | **`D282`** — DRIFT at +0.6h vs its 3–6h spec | 7 reproductions; the fix is scheduling, i.e. human |
| **12** | **`D379`** — PREFLIGHT reads §5 first | **8th run unwired**; done manually again today |
| **13** | **`D10`** — news-body boilerplate | open code defect, **server console required (P6)**, human-approval item — carried, not re-discovered |
| **14** | **`D9`** — does a holdco mismatch **block** or only **warn** | half-closed; the remaining half is a human call |

### 🆕 Registered by this stage (IDs from `module_evidence next-id D --count 4`; highest existing `D486`)
- **`D487`** — *A revival/entry condition is checked against the data available **on the day it is
  written**, and a condition already true at registration is rejected as a condition.*
  **Measured origin:** `LYV`'s *"operating margin turns positive"* was met at registration
  (TTM +2.903% at the 2026-03-31 TTM, the latest print on 2026-07-28) and is met now (+2.935%).
  38 days of "rejected" rested on a leg that never rejected anything.
- **`D488`** — *An earnings-date VOID clause is checked against `Ticker.earnings_dates` (timestamped,
  with reported EPS), never against the forward calendar field.* **Measured origin:**
  `module_fundamentals_us` reports *"다음 실적 발표: 2026-09-03"* for **both `HPE` and `AVGO`**, two
  days after both printed (09-02 16:00 ET, EPS 1.11 and 3.32 reported). Cost: `S110` **VOID**,
  `S105`'s registration note **false**, and `D420` mis-adjudicated in favour of the issuer calendar.
- **`D489`** — *The sweep's news axis fails at a fixed **burst count**, not at a request spacing;
  a fan-out is chunked below that count rather than slowed down.* **Measured origin:** coverage is
  universe positions **0–49 and nothing after** (a cutoff at exactly 50 names = 100 requests), while
  **40 names / 80 queries at ~0s spacing scored 40/40** and a fixed ten-name set gave **identical**
  answers at 1.5s and 9s. **This falsifies the 2026-09-02 prescription of "≥9s spacing."**
- **`D490`** — *A run that produces `llm_outputs` without a `handoff/` writeback leaves the spine
  behind its own evidence.* **Measured origin:** `industry_US` 09-03 (died in stage 1), `industry_kr`
  09-03 (full run, `D485-KR`/`D486-KR` written only to its run directory), `industry_kr` 09-04 (empty
  `preflight/`). `handoff/RESEARCH.md` mtime **2026-09-02 23:32**.

---

## 8 · Stale flags and cleared suspensions

| item | asof | state |
|---|---|---|
| `us_top300.csv` cap weights | **2026-07-15** | 🔴 **51 days** — every `wflow` is weighted seven weeks stale (G5). `us_all_v2_candidate.csv` (08-10) exists, **not wired**; switching is a human-approval item |
| `handoff/*.md` carry | **2026-09-02** | 🔴 **2 days / 3 runs behind** (§0, `D490`) |
| `history.json` 09-02 snapshot | 2026-09-03 | ⚠ holed-OBV; **superseded for this run** by the rebuilt clean baseline. Writing a corrected snapshot into shared history is a human-approval item (P5) |
| `08-28` vendor hole | **healed 2026-09-04** | ✅ **cleared suspension → converted to a dig**: `D446` (*a rolling-window axis states bars-present per name*) is **not** retired by the healing — it is the instrument that would have made the four-run outage visible on day one. Kept live |
| `S8` date field | `[blank]` | 🔴 **36th run** — human `VOID` or re-registration required (P5) |
| `TIMEFOLIO_EXECUTE=1` armed flag | live on every `exposure_rule` row | 🚨 human-owned operational flag, not an analytical one |

---

## 9 · Self-refutations and inherited refutations (§4c / `D48`) — written down, not edited away

1. ★★ **The 09-02 HANDOVER's central instrument judgement is refuted by 24 hours of data.** It
   recorded, in bold, that 08-28 was *"frozen, not lagging"* and that the repaired file was *"the
   standing instrument for the next four weeks."* **The vendor backfilled 256 names that night.**
   The earlier sentence stands in the 09-02 file; the general form is: **two observations of zero
   change are not a proof of permanence** — the desk drew a category conclusion (lag → frozen) from
   n=2, which is the same error class as the "0/42 label flips" claim it corrected the day before.
2. ★★ **This desk's own falsification method refuted this desk's own conclusion from it.** The 09-02
   run changed one variable (spacing) on a fixed name set and concluded spacing was the cause.
   Today the same design on a fresh fixed set gives **0 cadence flips** and a **40/40 zero-spacing
   burst**. The 09-02 experiment was not wrong to run — it was under-powered against an alternative
   (burst position) it never varied. **`S2` (diagnose the null) applies to controls, not only to
   hypotheses.**
3. ★ **A registration-time "checked" claim was false, and it was labelled thin at the time.**
   `S110` stated `HPE`'s print was *"outside by one session, and that margin is stated because it is
   thin."* It was inside by two. **Stating that a margin is thin is not the same as measuring it
   against a reliable field.**
4. **Zero self-refutations would itself be a finding.** Three are recorded; all three came from
   re-running a prior measurement rather than from re-reading prior prose.

---

## ✅ EXIT CHECK — HANDOVER

- [x] Shared spines read (`STANDING_VIEW.md` §1 regime · §5 retracted ledger · §6 contradictions ·
      asof chain; `SCENARIOS.md` legend + master scoring log + master index), plus
      `STANDING_VIEW_US.md` (§2 `M1234`–`M1261`, §3a registry), `SCENARIOS_US.md` (every row named
      above opened in full), `RESEARCH.md` Parts A/B/C, `README.md`.
      **Other-market file opened**: `SCENARIOS_KR.md` for `S67-KR` (settles 09-04, KR observable,
      left to the KR desk and said so). Mechanical ledger cross-queried (`module_report_tags show`).
- [x] **Retracted ledger read BEFORE forming today's view** (§2). No claim in this run matches a
      retracted entry; `R120` is noted as moot-by-retirement and `R122`-KR's *check* was re-run on
      US data rather than imported.
- [x] **Every past-dated scenario scored or explicitly named.** 8 scored, 1 VOID with its mechanism,
      6 not-yet-settled and listed with reference states, `S8` named for a 36th time. **0 EXPIRED,
      0 silent skips.**
- [x] **`reject_ledger.py due` run** — 12 rows, **7 US resolved this run** (2 revived, 5 reaffirmed),
      5 KR named and assigned. Legacy count **0**, reported rather than passed over; the streak of
      0-due runs is reported as **ended**, with a replay proving it is a maturing cohort, not a bug.
- [x] **`missed_ledger.py due` run** — 20 rows, **3 US resolved**, **3 US deferred to ALPHA inside
      this run and named**, 14 KR named and assigned. ⚠ `excess` sign inverted; the two ledgers are
      **not** summed.
- [x] **Exposure state read and carried** (§6): 4-state verdict, target vs current invested %,
      cumulative cash/selection split, both books side by side. Not a cold start (n=18), not
      `밴드미설정`; the **stalled n** is flagged.
- [x] 🚨 **Instrument health inherited before any number is trusted** (§1). Two gate changes govern
      the run: the OBV revocation lifted, the Δ column revoked in its place.
- [x] **Self-refutations written down, not edited away** (§9) — three, all from re-measurement.
- [x] Stale rows flagged with their `asof`; the one cleared suspension (the 08-28 hole) converted
      into a dig rather than a silent trust (§8).
- [x] `[measured]` / `[inferred]` tags preserved. No `[inferred]` claim passed downstream as evidence.
- [x] **RESEARCH triggers loaded as binding constraints**, grouped C/S/D/W + lenses L, with the
      stages each group binds named (§7).
- [x] `HANDOVER.md` written; `handoff/*.md` updated at run end (append-only for retractions).
- [x] No position sizing, no buy/sell language anywhere in the carry.

---
> Next: **MACRO**. It inherits one live question above all — **`P121`**: the August payroll report
> printed at 08:30 ET today, and the row asks whether the repricing is the policy path
> (`DGS2` ≥ 4.50 **with** `T10YIE` ≤ 2.36) or a Jackson-Hole artifact (`DGS2` ≤ 4.18). MACRO reads
> the **09-03** FRED close and the print's own numbers from news; the row itself settles tomorrow.
