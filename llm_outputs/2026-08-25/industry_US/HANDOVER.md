# HANDOVER — industry_US · 2026-08-25 (Tue) · Stage 2/11 · L1·HANDOVER

> Run clock: **2026-08-25 22:15 KST = 09:15 ET**, i.e. **US pre-market, 15 minutes before the open**.
> This stage transports analysis. **No sizing, no buy/sell language** (P4).

---

## ★★★ The three things this packet exists to hand forward

**1. The tape moved. For the first time in four runs.**
The 08-22, 08-23 and 08-24 runs each recorded `n_new_sessions_since_prior_run = 0` with a terminal
bar frozen at **2026-08-21 (Fri)**. Today the terminal settled bar is **2026-08-24 (Mon)** — **one new
settled session**. Every stage that spent three runs writing "the numbers did not change" now has a
changed number to read, and the change is **not small** (below). ⇒ **the standing excuse is withdrawn:
a stage that declines to move a verdict today must decline on the new data, not on the absence of it.**

**2. `P79` has crossed into its own falsifying branch, one session before settle.**
`P79` (registered 08-20 MACRO) settles **tonight, 2026-08-25 close**, deliberately one session before
the `NVDA` print. Its observable is `EW{AVGO, ANET, HPE, COHR, LITE}` trailing **5-session** excess
vs `SPY`; branch **B ≤ −7.72** (its own 252d p05), branch A ≥ +8.02 (p85).
**Measured at the 08-24 settled close: −10.852.** Three runs ago it read −7.178, two runs ago −5.609
("moved 1.57pp **away** from B"). It has now moved **5.24pp back through B**. ⚠ **This is a pre-settle
reading, not a score** — it is handed to MACRO as the run's single most consequential inherited number
and to the 08-26 run as a row that must be scored on arrival.

**3. `S102` is settled and the owner's VOID ruling is this desk's to make — and it is NO-VOID.**
The `industry_kr` desk scored `S102` **`FIRED-C`** this morning (its 7th independent pull finally
found `DGS2` **4.24 @ 2026-08-21**) and correctly deferred the VOID question to the registering desk.
**Ruled below (§2b): the anti-signal did NOT fire; `FIRED-C` stands.**

---

## §0 · Instrument health inherited (EXIT-CHECK gate — read before trusting any number)

`llm_outputs/2026-08-25/industry_US/preflight/PREFLIGHT.md` **was run** this morning, ahead of this
stage. Verdicts: **G2 PASS · G3 PASS · G7 PASS · G1 FAIL · G4 FAIL · G5 FAIL · G6 FAIL.**

**Five citation rights are removed from every downstream stage of this run:**

| From | This run may NOT |
|---|---|
| **G1** | cite **news velocity** or **theme freshness** from the sweep, and may not call any name or sector **"quiet"**. The sweep's `vel_coverage` is **0.0% (0/299)** while hand probes answer and discriminate (Nvidia 4137 / Nucor 27 / Marathon Petroleum 25 / Nasdaq Inc 6, `--days 7 --scope foreign`) ⇒ **the sweep could not count; the pool is not silent.** BET_SHEET §B freshness tags must read `UNMEASURED (G1 FAIL)`. **Hand-run single-name news lookups remain legal** — they are the probe that passed. |
| **G4** | quote any concentration figure without its `--days` on the same line. **250d → 11 units, 500d → 10, 750d → 10, and the groupings disagree**: at 250d the book reads as four independent AI-complex risks, at 500/750d as two. |
| **G5** | treat `wflow` as a **current** weighting. `us_top300.csv` is **41 days old** (mtime 2026-07-15, bar ≤8). Coverage itself is clean — **11 of 11 US book names are inside the universe** — but the caps that weight `wflow` are stale, and (per `M856`) the same stale file **decides news-bucket membership**. ⇒ **where `wflow` and `eqflow` disagree, `eqflow` is the citable one.** |
| **G3** | promote or demote **Consumer Staples** on the weighted-flow bucket. It is the run's **only** flipper (1 of 11; top1 `WMT`, wflow −0.013, n=19). Rank it on `eqflow`/`breadth` and say so inline. |
| **G6** | describe any fraction as IC-backed. `snapshot_estimates --status`: **17 files / 35 calendar days = 0.49/day = 2.1× slower** than ideal. Any fraction is **"mechanical 1/4 — IC not yet estimable"**. |

⚠ **G2's PASS is conditional and SWEEP must re-check it.** `n_axes` = 3 on 08-20/21/22/23/24 —
Δflow arithmetic is scale-legal **because the news axis has been consistently absent**, not because it
is healthy. If today's sweep recovers coverage ≥80%, `n_axes` becomes 4 and **differencing against the
3-axis history becomes illegal**.

---

## §1 · Inherited standing view

### 1a. Regime call — carried unchanged, tag preserved
> *"Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight."*
> **`[inferred]`** — built on the measured chain, not itself a measurement.

**Carried, not re-derived, and not citable as evidence** for any new proposition (RESEARCH group W).
This run has **one** new settled session bearing on it, which is `n=1` (rule S5) — not enough to move
a regime call, and the honest statement is that the new session **does not test it**: the memory
complex's own print (`MU`) is 2026-09-24.

### 1b. Retracted ledger (§5) — read BEFORE forming today's view
The ledger now runs to **`R98`** (filed 2026-08-24). Read in full at this stage. The entries that bear
on what today's stages are most likely to re-assert:

| Retraction | What it forbids today |
|---|---|
| **`R98`** (08-24) | Do **not** write that the US desk has no IC measurement. It has **405 rows over 33 run-dates**, reachable only with `--market us` (`D336`). ★ And the KR verdict it would have borrowed has the **opposite sign**. |
| **`R81`/`R78`** | Do **not** promote on a **flow tag**. `M25`'s tag arithmetic was refuted on the desk's own board; with G1 down again today the tag's news leg is unmeasurable. |
| **`R10`** | Do **not** re-assert "IT + Real Estate + Utilities are ONE risk concentration" in its strong form. Measured: four separate units. The **weak form survives** — shared *catalyst*, i.e. event concurrency, not correlation. |
| **`R7`** | Do **not** call Real Estate "the purest duration expression". |
| **`R11`** | Do **not** re-assert the long-end move as bear-**steepening** without re-measuring the front end — and today the front end **moved** (`DGS2` 4.19 ×4 sessions → **4.24** on 08-21, a parallel +5/+5/+4bp shift). |
| **`R3`, `W1`** | Do **not** import a KR-measured relationship into the US frame. `M854` is the cleanest demonstration this desk owns: the transfer would have been **backwards**, not merely unlicensed. |

### 1c. Open contradictions (§6) — carried, not resolved
- **`C15`** — the gatekeeper-axis contradiction, now **two-sided**: `vol_surge` h=1 is `t(NW) +3.40`
  **positive** in the US and `−3.86` **negative** in KR, **both Bonferroni-passing**. ⚠ US h=5 is
  `+0.44` = indistinguishable ⇒ **`D105` two-horizon agreement is NOT satisfied in the US**; the
  positive result is **horizon-1 only and must be quoted with its horizon**. Resolution path unchanged:
  accrue `participation` as an axis in both ledgers and read the sign at `n_eff ≥ 4`.
- **`C14`**, **`C10`**, **`C1`**, **`C9`** carried unresolved. **`C2`** remains settled-with-a-sharper-
  question (KR-side object; not this desk's to move).
- 🚫 **No contradiction is resolved by picking a side this run.** Resolving requires a measurement.

### 1d. Per-name carry (US registry §3a, latest rows 2026-08-22) — with today's new session attached
Tags below are the registry's; the **exc columns are this run's own pull to the 2026-08-24 settled
close** (`yfinance auto_adjust=False`, benchmark `SPY`), so the carry is dated, not stale.

| Name | Carried state (`asof` 08-21) | Tag | exc1 (08-24) | exc5 | exc20 | Stale? |
|---|---|---|---|---|---|---|
| `MPC` | Thesis intact; **separation claim dead at settle** (`P70` MISS). 🚨 contract read 3 runs unopened → **discharged 08-24** (`M875`) | `[measured]` | +0.79 | +2.68 | **+13.08** | fresh |
| `PSX` | Same node; refining accumulating vs `XOM` distributing | `[measured]` | −0.08 | +2.31 | **+13.75** | fresh |
| `RTX` | **Downgraded** — left accumulation, delta −0.304 (book's largest). `W4` unpaid **205 days** | `[measured]` | −0.03 | −4.41 | −7.19 | ⚠ `W4` obligation now **208 days** |
| `ANET` | **New divergence** — best flow improvement (+0.384) **and** the only 🔴 short axis (FINRA z +1.82) | `[measured]` | +0.03 | −5.57 | +6.89 | fresh |
| `NUE` | 🚩 live thread against it, direction ambiguous after `M808`. `S114` → 09-03 | `[measured]` | +0.71 | **−9.09** | −4.60 | fresh |
| `MRK` | Sector's only 🟢 **and the sheet's strongest refutation datum** — RSI 86.7, revisions **1↑/5↓** | `[measured]` | — | — | — | recheck **09-03** |
| `MSTR` | `COIN`+`MSTR` = **ONE risk unit, two GICS labels**. Rejected 08-24 (`C.차트붕괴`) | `[measured]` | — | — | — | revive check **09-08** |
| `T` | **Orphan at 9.74% of real invested, 5th run** — no cycle label, no card. `S107` → 09-03 | `[measured]` | — | — | — | 🚩 **6th run** |
| optical node | `LITE`/`COHR` re-filed, not dropped. **Registry still has no optical row — 10th run** (`D250`) | `[measured]` | `COHR` **−20.37** · `LITE` **−13.13** (5-sess) | | | 🚩 **11th run** |
| `ETN` | `S99`'s construction defect stands: `ETN` loads **2.3× more on `XLI` than `XLK`** | `[measured]` | −2.22 | **−9.07** | −0.53 | fresh |

★ **Two stale flags escalate this run, both by one:** `T` is an unlabelled orphan for a **6th** run,
and the optical node has no registry row for an **11th**. Neither is a new finding; both are
**dig instructions that keep not being executed**, which is the failure `D250` names.

★ **The new session is concentrated and it is one-sided.** Of the 11 US book names, the 08-24
session's excess is negative at 5 and positive at 6, but the **magnitude** sits entirely in the
AI-compute complex on the 5-session view: `ETN −9.07`, `NUE −9.09`, `AVGO −7.39`, `HPE −7.80`,
`NVDA −6.16`, `ANET −5.57` against `NDAQ +3.37`, `MPC +2.68`, `PSX +2.31`. **Sector confirmation
from the ETF cut (own pull, 08-24 close): `XLK exc5 −4.21` and `XLI exc5 −2.74` are the only two
negative sectors of eleven**, while `XLV +5.77`, `XLP +4.46`, `XLB +3.76` lead. ⇒ the drawdown that
`P79` brackets is **not** a broad tape event; it is the AI-compute complex specifically, on a week
when nine of eleven sectors beat `SPY`.

---

## §2 · Scenarios — settled, ruled, and pre-settle

### 2a. Exhaustive settle table — the device that separates "nothing was due" from "we did not look"

| Row | Owner | Settle | Status this run | Disposition |
|---|---|---|---|---|
| **`S102`** | `industry_US` | "first close covering 08-21" | **SCORED `FIRED-C`** by `industry_kr` this morning; **VOID ruling deferred to this desk** | **Ruled NO-VOID (§2b). `FIRED-C` stands.** |
| **`P79`** | `industry_US` | **2026-08-25 close** | **NOT YET ARRIVED** — settles tonight, ~6h 45m after this stage | **Pre-settle reading recorded (§2c). Handed to the 08-26 run as past-due on arrival.** |
| **`S108`** | `industry_US` | **2026-08-25 close** | **NOT YET ARRIVED** — same clock | **Pre-settle reading recorded (§2c).** |
| **`S119`** | `industry_US` | 2026-08-27 | ARMED; window opened at the 08-24 close | 2 sessions out |
| **`S118`** · **`S120`** | `industry_US` | 2026-08-28 | ARMED | `S120`'s observation-lag clause is written into the row (`D333-KR`) |
| **`S103`** | `industry_US` | 2026-08-29 | ARMED | ⚠ `D295` obligation **still open**: its ±5.0pp bands are hand-set and must be re-derived from an 08-26-or-later straddle **before the print**. **2 sessions left.** |
| **`S109`** | `industry_US` | 2026-09-02 | ARMED | ⚠ `FRO` is outside `us_top300` (`D341`) |
| **`S110`** · `S107` · `S114` · `P84` | `industry_US` | 2026-09-03 | ARMED | `S110`'s VOID margin is **one session** (`HPE` prints 09-04) |
| **`S123`** · `S122` · `S112` · `S92` · `S94` · `S104` · `S48` | `industry_US` | 09-05 → 09-30 | ARMED | — |
| **KR-owned** | `industry_kr` | earliest **2026-09-04** (`S67-KR`) | **0 past-dated** — verified in the 08-25 KR run's own exhaustive table | Nothing for this desk to score |
| 🚨🚨 **`S8`** | `industry_US` | **`[blank]` undated** | **UNSCOREABLE — 25th consecutive run** | **A human must `VOID` it or re-register it with a date (P5).** |

**Run totals: 0 newly scored by this desk · 1 owner-ruling issued (`S102`) · 2 pre-settle readings
recorded (`P79`, `S108`) · 0 `EXPIRED` · 0 silent skips · 1 unscoreable-by-construction (`S8`).**

⚠ **The zero-newly-scored is a CLOCK fact, not a diligence fact, and it is stated as such.** This desk
runs pre-market; a row dated D settles on D's US close and is therefore always scored by the D+1 run.
`P79` and `S108` are dated **today**. They will be past-due on arrival for the 08-26 run and are
named here so they cannot be quietly skipped.

### 2b. ★ Owner ruling on `S102` — **NO VOID. `FIRED-C` stands.**

**The question.** `S102`'s anti-signal: *"an **intermeeting Fed policy action** or a **Treasury
refunding announcement** inside the window."* On **2026-08-19**, inside the window, Treasury Secretary
Bessent **doubled the long-bond buyback programme**. The 08-22 US run flagged a VOID recommendation;
the KR desk scored the row on its letter and explicitly handed the disposition to the owner.

**The evidence, pulled fresh this stage** (`fts search "Treasury buyback" --days 10 --scope foreign`,
**239 matches**): the event is consistently reported as a **buyback-programme doubling** —
*"Bessent Doubling The Treasury Buyback Program"* [seekingalpha 08-23], *"Deutsche Bank calls Treasury
buyback doubling similar to 'operation twist'"* [investing_en 08-19], *"Equities Fall Intraday as
Yields Rise Despite Treasury Buyback Plan"* [yahoo_finance 08-20]. **No outlet describes a refunding
announcement**, and none reports a Fed action of any kind inside the window.

**The ruling, on three grounds:**
1. **The letter.** A quarterly refunding announcement (QRA) is a distinct, named, scheduled Treasury
   event. A buyback-schedule expansion is not one. The clause names two things and **neither occurred**.
2. **The desk's own later construction agrees.** The 08-22 PREMORTEM, writing a fresh anti-signal three
   days later, drew exactly this line — *"an **emergency Treasury operation** (not a scheduled
   buyback)"* — and justified it by noting *"the buyback expansion already executed on 08-19."*
   ⇒ the desk had already ruled this class out-of-scope in a row it wrote after the event.
3. **The protocol.** Widening a frozen clause after the fact converts a forecast into a description.
   Reading "refunding announcement" as "any debt-management action" is exactly that widening.

⚠ **The counter-argument is recorded rather than suppressed**, because it is not weak: a buyback
doubling is a deliberate intervention **on the long end**, which is the leg `S102`'s branch B is built
on (`30y−10y ≥ 0.59`), and `M870` measured that the long end **did not move** in response
(`DGS30` at the 96.4th percentile the day after). A reader who thinks the row's *intent* was
"no exogenous long-end intervention" would VOID it. **This desk rules on the letter and says so.**
⇒ **new dig `D348`** (§5): an anti-signal that names a specific instrument (`refunding announcement`)
when the mechanism it fears is general (`any Treasury long-end intervention`) will be litigated at
every settle. **Positive-form remedy: name the mechanism, then list the instruments as examples.**

★ **And one carried observation is overturned by the same settle.** `M859` (this desk, 08-24) read
*"`DGS2` printed 4.19 on FOUR consecutive sessions — the front end did not move on the minutes."*
The 08-21 print is **4.24, +5bp**. The curve moved **in parallel** (2y +5 · 10y +5 · 30y +4bp), so the
correction is to the **level** statement, not to the slope statement. `M859`'s slope half survives.

### 2c. Pre-settle readings (⏳ **NOT scores** — recorded so the 08-26 run inherits a baseline)

| Row | Frozen observable | Bands | **Measured at the 08-24 settled close** | Read |
|---|---|---|---|---|
| **`P79`** | `EW{AVGO,ANET,HPE,COHR,LITE}` trailing **5-session** excess vs `SPY` | **A ≥ +8.02** (p85) · **B ≤ −7.72** (p05) · C between | **−10.852** — legs `COHR −20.37`, `LITE −13.13`, `HPE −7.80`, `AVGO −7.39`, `ANET −5.57` | 🚨 **Inside branch B with one session to run.** Trajectory: −12.425 (registration 08-20) → −7.178 (08-21) → −5.609 (08-22) → **−10.852 (08-24)**. ⚠ **The partial window from 08-18 reads −5.298**, i.e. the estimator's answer depends on which of the two 5-session windows is meant; **the row's own construction ("trailing 5-session at the settle") gives −10.852 at D−1.** Both are written down. |
| **`S108`** | `EW{XLU,XLRE,XLP}` **3-session** excess vs `SPY`, window 08-20 close → 08-25 close | **A ≥ +1.68** (p85) · **B ≤ −1.76** (p15) · C between (disclosed favourite, ≈70%) | **+0.484** with 2 of 3 sessions elapsed — legs **`XLP +2.38`, `XLRE +0.44`, `XLU −1.37`** | ⏳ **Inside C, and moving AWAY from A** (state at registration was +1.432 = 78.6th percentile). ★ **The more informative fact is the dispersion**: the three legs span **3.75pp** and `XLU` is *negative* ⇒ **whatever settles tonight, "the three underweights rip together" is not what the tape is doing.** That is the row's own premise weakening ahead of its settle. |
| `S118` (context) | `EW{MU,SNDK,WDC}` vs `NVDA` | A ≥ +6.50 · B ≤ −6.50 | window opens 08-26; 08-20→08-24 run-up reads **−2.958** | not yet in window — recorded as a starting state only |

⚠ **All three are `[measured]` price pulls made by this stage, on settled closes, benchmark `SPY`.**
None is a verdict. **The 08-26 run must score `P79` and `S108` on arrival.**

---

## §3 · Both ledgers audited — symmetric, or it is not a scoreboard

| Ledger | Total | Resolved | **`due` this run** | Legacy (no condition) |
|---|---|---|---|---|
| `reject_ledger.py due` | **232** | 135 | **0** | **0** |
| `missed_ledger.py due` | **230** | 117 | **0** | **0** |

**Both `due` calls were actually run** (not substituted with `score`). **Zero rows surfaced; zero rows
are being carried a second time unexamined.**

⚠ **The clean run is NOT quoted as proof the ledgers are healthy** (`carryover.md` §3b's explicit
warning). The evidence that the practice has taken hold is the **legacy count**, and it reads
**0 for a 14th consecutive run** — down from 24-of-25 rows with no revival condition on 2026-07-23.
**That, not the empty `due` list, is the number worth carrying.**

⚠ **Sign discipline**: the two `excess` columns are **inverted** relative to each other
(`reject`: `excess > 0` = the rejection cost us; `missed`: `excess > 0` = the miss cost us).
**They are not summed anywhere in this run.**

---

## §4 · Exposure state — size context for BET/ALPHA (read-only; this stage never logs)

| Field | Value |
|---|---|
| Rule state | **`정상` (normal)** — prior state also normal; no firing condition |
| Target invested | **95%** |
| Ledger invested (today's accrued row) | **85.3%** |
| **Band gap** | **−9.7pp** — tied with 08-24 for the narrowest of the last seven rows (−39.4 → −27.1 → −14.0 → −13.9 → −9.9 → −9.7 → **−9.7**) |
| Cumulative decomposition | **n = 13**, total **−12.67pp = cash −5.93 + selection −6.74** |
| Benchmark | `069500.KS` 106,795, +0.755% on the day; −2.97% from its 20-day high |

⚠ **Not a cold start** — the ledger holds **40 rows**, so the verdict is quotable (the 2026-07-31
cold-start distortion, `방어`/−1.9pp vs backfilled `복귀`/−37.2pp, does not apply).
⚠ **The state is NOT `밴드미설정`**, so no 🚨-and-no-number case arises.
⚠ **`exposure_rule.py state` could not read the account** (`투자비중미상`, NAV/invested-% unavailable
— account lookup failed), so the **85.3% above comes from the accrued ledger row, not from a live
account call**. Stated rather than silently substituted (P4).
⚠ **`n = 13` is not a sign.** −12.67pp cumulative is **not** evidence the desk's selection is negative;
the ledger's own line says the sign becomes askable at n ≈ 20 (C4). Carried as *size context*, never as
a verdict on skill.
🚨 **The ledger carries `ARMED (TIMEFOLIO_EXECUTE=1)` on every row.** Noted as inherited state; **this
run touches no execution path and issues no order** (P4/P5).

---

## §5 · IC ledger — does this desk's own ranking have a sign yet? (`--market us`, per `R98`/`D336`)

**405 rows · 33 run-dates · 15 tests.** Only cells with `n_eff ≥ 4` are quoted; the Bonferroni bar for
k=15 is **|t| > 2.8**.

| Axis | h | n | n_eff | mean IC | t(NW) | % positive | 필요n | Verdict |
|---|---|---|---|---|---|---|---|---|
| **`rs60`** | **5** | 27 | **5.4** | **−0.1310** | **−5.46** | 7% | 2 | ★ **Bonferroni-passing, NEGATIVE** |
| **`vol_surge`** | **1** | 33 | **33.0** | **+0.0398** | **+3.40** | 67% | 12 | ★ **Bonferroni-passing, POSITIVE** |
| `rs60` | 1 | 33 | 33.0 | −0.0635 | −2.77 | 21% | 18 | standalone-significant, same sign as h=5 ⇒ **`D105` satisfied** |
| `vol_surge` | 5 | 27 | 5.4 | +0.0119 | +0.44 | 63% | 211 | indistinguishable ⇒ **`D105` NOT satisfied for `vol_surge`** |
| `flow_score`, `obv_norm`, `rs20` (h=1, 5) | | | 5.4–33.0 | −0.023 … −0.046 | −0.91 … −1.41 | 30–42% | 36–165 | **구분 불가** (indistinguishable) |

**Unquotable this run (`n_eff < 4`): all six h=10 cells** — including `rs60 h=10` at `−0.2014 / −3.87`,
which looks like the strongest number in the table and **is not readable at `n_eff 2.1`**.

★ **Two carries for the downstream stages, both binding:**
1. **`rs60` ranks AGAINST 1–5-session forward returns in the US top-300** over 2026-07-13→08-20, at
   two horizons with the same sign. `rs20`/`rs60` are **two of the sweep's four surviving axes**
   (the news axis is dead — G1). ⇒ **any stage that promotes a name *because* its `rs60` is high is
   leaning on the ledger's most strongly negative cell and must say so.**
2. **Every 🟢 citation must carry its horizon.** The 🟢 gate selects **for** `vol_surge`, an axis
   measured **positive at h=1** and **indistinguishable at h=5**. "🟢" without a horizon is not a claim.

⚠ **Regime label, required and given**: the window **2026-07-13 → 2026-08-20 contains the mid-August
drawdown.** `rs60`'s −5.46 is the shape a drawdown produces (yesterday's winners lead the fall). **This
IC does not generalise to a trending regime**, and nothing in this run may treat it as a standing law.
🚫 **No axis is flipped, killed or re-weighted here — code changes are a human call (P5).**
★ **Standing item, reported every run**: `vol_surge` is the axis where the two markets **contradict
each other with both sides Bonferroni-passing** (`C15`). The gate is not flipped.

---

## §6 · Reconciliation — what we believe vs what we covered (`module_report_tags show`)

- **Coverage without a live belief** → candidate DEEP. `SECTOR_DEEP_UTIL.md` (08-24, *"The answer: No.
  Zero. And 'zero' is measured, not inferred"*) and `SECTOR_DEEP_RE.md` both carry recent deep work
  with **no per-name row in the US registry**. UTIL is also the **only sector where `green_rate` and
  `participation` agree at 0.0%** (`M865`) — i.e. the one absence that is evidence rather than a
  `vol_surge` filter artifact (`M866`).
- **Belief without coverage** → demote or dig. **`T`** carries a registry row and **9.74% of real
  invested** with **no cycle label and no card, 6th run**. The **optical node** (`LITE`/`COHR`) has
  reports and brackets but **no registry row, 11th run** — and it is today's **worst-performing pair
  on the board** (−13.13 / −20.37 five-session excess). ⇒ **both are ranked digs below.**
- **Resolved-but-live**: none newly detected this run.
- ⚠ The ledger is **`REPORT/`-scanning**; this run resolves the open `DEGAJA_REPORT_DIR` decision by
  **copying finalized reports into `REPORT/industry_US/` at run end** (documented practice).

---

## §7 · RESEARCH rules loaded as BINDING constraints — which group binds which stage

Not summarized — loaded. `handoff/RESEARCH.md` is the single source (21 triggers + 3 lenses).

| Group | Fires when | IDs | **Binds, this run** |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO** (FRED baselines, and `C5` on every cohort cut) · **every stage**. ★ `C4` is live at three places today: exposure `n=13`, the IC cells marked 구분 불가, and `S108`'s C branch. |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample ≠ done · S5 short samples · S6 future labels | **any stage citing a test** — above all **§5's IC table** (`S1`: one observation = one run, not one name; `S5`: the h=10 cells). |
| **D** | you read data | D1 second listing venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · **D6 signal grade (OBV is C-grade)** · D5 cross-provider | **SWEEP** · **ALPHA** · L2 indicators · L2 money_trail. ★ **`D6` is load-bearing today**: with the news axis dead (G1) and `rs60` measured negative (§5), the sweep's surviving axes are **OBV (C-grade)** plus two relative-strength axes the ledger ranks against. |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real ≠ profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION**. ★ **`W5` is pre-loaded with four measured splits** from 08-24 that DEEP must not re-derive: IT software vs semis **19.17pp** (`M876`) · HLTH 24-vs-8 **12.62pp** (`M878`) · ENRG four businesses, war premium **separable** from capacity (`M879`) · STPL `TGT`−`WMT` **26.23pp/20d** (`M880`). ★ **`W4` is unpaid on `RTX` for 208 days.** |
| **L** | lenses, not triggers | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM**. ★ **`L2` is now closed against the desk in refining**: MPC's FY2025 Item 1A carries `take-or-pay` 0 / `fixed-price` 0 / `crack` 0 (`M875`) ⇒ **no contractual escape hatch**, and a **legislated ceiling** exists (California SB 2, `D344`). |

---

## §8 · Dig list ranked for today (RESEARCH Part C) — top candidates for DEEP/PREMORTEM

| Rank | Dig | Why today |
|---|---|---|
| **1** | **`D295`** — `S103`'s hand-set ±5.0pp bands must be re-derived from an **08-26-or-later straddle before the `NVDA` print** | **Two sessions left.** An un-re-derived bracket on the board's biggest binary repeats exactly what `S100` fixed inside its own window. **PREMORTEM owns this.** |
| **2** | **`D341`** — the desk cannot flow-tag the names its own discovery layer surfaces (`AA` `X` `WY` `LYB` `DOW` `BABA` `FRO` all outside `us_top300`) | Compounded today by **G5**: the universe is **41 days old**, and `M856` shows that same file **decides news-bucket membership**. `S109` is armed on `FRO`, which the desk cannot tag. |
| **3** | **`D297`** — `top1_flips_sign` is a **demonstrated false negative** on COMM (both Alphabet classes flip `wflow` +0.108 → −0.193 while the flag prints `false`) | **6th run unfixed.** G3 passed *this morning on that same flag* — so PREFLIGHT's G3 PASS is itself only as good as a test known to miss share-class pairs. **SWEEP and ROTATION must apply the issuer-level check by hand.** |
| **4** | **`D250`/`M731`** — no optical/interconnect row in `cycle_registry.json`, **11th run** | The optical pair is **the board's worst 5-session excess today** (`COHR −20.37`, `LITE −13.13`) and it is the largest contributor to `P79`'s move into branch B. Exposure to it is **unmeasurable, not zero.** |
| **5** | **`D338`** — register a successor bracket keyed to the **Hormuz exception channel** (counterparty-specific transit permits, ≥2 outlet bodies) | `S74` retired 08-24; `S8` is undated for a **25th** run ⇒ the general-fleet Hormuz axis is **unbracketed**. `M883`'s fourth channel (China+Jordan) opened after the last report closed. |
| **6** | **`D336`** — make `--market` required on `ic_ledger`'s three subcommands | Human approval (CLI signature). Carried so it is not re-discovered a third time. |
| **7** | **`D344`** — add a `regulated-margin-cap` row to the ENRG DEEP KPI table; track **California SB 2** as a dated observable | ENRG is the desk's only rate-exposed *overweight* and refining's `exc20` is **+12.85** — the ceiling bites exactly where the thesis is longest. |
| **8** | **`D348` (NEW, this stage)** — anti-signals must name the **mechanism** and list instruments as examples | Registered from the `S102` VOID litigation (§2b). |
| **9** | **`T`'s orphan status, 6th run** | Not a numbered dig and that is itself the problem: **9.74% of real invested with no cycle label** has been "carried" five times without ever being assigned. |
| — | **`D10`** — news-body boilerplate | **Carried forward, not re-discovered.** Needs human approval **and a server console** (FTS writes are server-only, P6). |
| — | **`D9`** — half-closed: holdco mismatch is measured and surfaced; whether it **blocks** or only **warns** is a **human call**. | Unchanged. |

---

## §9 · What this run asserted and then refuted (§4c · `D48`) — written down, not edited away

**One, and it is this stage's own.**

🚨 **This stage drafted `P79`'s pre-settle reading as "−5.298, still outside branch B" before checking
which window the row's own registration freezes.** The registration (08-20 MACRO) reads *"the same EW
basket's **5-session** excess"* at the settle — a **trailing** 5-session window, which at the 08-24
close runs **08-17 → 08-24 = −10.852**, i.e. **inside branch B, not outside it.** The −5.298 figure is
the partial window 08-18 → 08-24 (4 sessions), which is not what the row freezes.
**The draft is left standing and the correction is appended beside it** (§2c carries both numbers).
⇒ The near-miss is the `C1` failure mode — *measure the window yourself, including any baseline you
were handed* — caught by re-opening the registration rather than by trusting the running commentary in
three prior MACRO reports.

⚠ **One self-refutation, on a run that ran controls, is a LOW count and is flagged as such.** The 08-24
run recorded four. A run that finds nothing to refute in itself has usually not been adversarial —
this stage read primarily inherited material, which is the smallest available surface for
self-refutation, and downstream stages should not read the low count as a clean bill of health.

★ **And one inherited claim was overturned by new data, which is a different object**: `M859`'s
*"the front end did not move on the minutes"* — refuted at the level (`DGS2` 4.19 → **4.24**), upheld
at the slope (parallel shift). Recorded in §2b.

---

## §10 · Handoff to MACRO — the four things stage 3 must not re-derive

1. **The tape advanced one session (terminal bar 2026-08-24).** The "no new information" framing of
   the last three runs is **withdrawn**. Nine of eleven sectors beat `SPY` over five sessions; the two
   that did not are **`XLK −4.21`** and **`XLI −2.74`**.
2. **`P79` sits at −10.852 = inside branch B**, settling tonight, one session before the `NVDA` print
   by construction. `S108` sits at **+0.484** with its three legs **3.75pp apart**.
3. **`S102` is `FIRED-C`, NO-VOID, ruled by this desk** — and its settle overturns `M859`'s level half.
   The curve moved in **parallel** (+5/+5/+4bp), so today's rate framing is a **level** story, not a
   slope story.
4. **Five citation rights are gone (§0).** In particular: **no theme-freshness or news-velocity
   citation, and no "quiet" verdict**, anywhere in this run.

---

## ✅ EXIT CHECK
- [x] Shared spines read in full — `STANDING_VIEW.md` (§1 regime, §2 chain, **§5 retracted ledger read
      BEFORE forming today's view**, §6 contradictions, asof chain) and `SCENARIOS.md` (scoring log +
      MASTER index) — plus this desk's `STANDING_VIEW_US.md` / `SCENARIOS_US.md` and `RESEARCH.md`.
- [x] **Other-market file opened**: the 2026-08-25 `industry_kr` block was read because it holds a row
      this run had to disposition — **`S102`, US-registered and KR-scored**. Its exhaustive KR table
      confirms **0 past-dated KR rows** (earliest 2026-09-04, `S67-KR`).
- [x] Mechanical ledger cross-queried (`module_report_tags show`) — belief/coverage reconciled in §6,
      two gaps named (`T`, optical node) and two coverage-without-belief sectors named (UTIL, RE).
- [x] **Every past-dated scenario scored or explicitly dispositioned.** 1 owner-ruling (`S102`),
      2 pre-settle (`P79`, `S108`, both dated **today**, settling after this run ends), 1 undated
      (`S8`, named for the 25th time). **`EXPIRED` 0 · silent skips 0.**
- [x] **`reject_ledger.py due` run** — 232 rows, **0 due, 0 legacy**. Not substituted with `score`.
- [x] **`missed_ledger.py due` run** — 230 rows, **0 due, 0 legacy**. Legacy 0 for a **14th** run,
      reported as the real evidence rather than the empty `due` list. Sign inversion stated; not summed.
- [x] **Exposure state read and carried** — `정상`, target 95% vs ledger 85.3%, band gap **−9.7pp**,
      cumulative n=13 **−12.67pp = cash −5.93 + selection −6.74**. Not a cold start (40 rows). Not
      `밴드미설정`. The account-read failure is stated, not papered over.
- [x] 🚨 **Instrument health inherited before any number was trusted** — `PREFLIGHT.md` read; 4 FAILs
      converted into 5 explicit removed citation rights (§0), including the G2 conditional for SWEEP.
- [x] **A claim this stage asserted and then refuted is written down, not edited away** (§9), and the
      low self-refutation count is itself flagged.
- [x] Stale rows flagged with their `asof`; two escalate (`T` 6th run, optical node 11th run) and are
      converted into ranked digs.
- [x] `[measured]`/`[inferred]` tags preserved. The regime call stays `[inferred]` and is **not** cited
      as evidence anywhere in this packet.
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W/L**, with the binding stage
      named for each group (§7).
- [x] `HANDOVER.md` written. `handoff/*.md` writeback occurs **at run end** (append-only), per the stage.
- [x] **No position sizing and no buy/sell language anywhere in this packet** (P4).
