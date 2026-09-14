# HANDOVER — industry_US · 2026-09-14 (Mon, 13:16–13:5x KST = Mon 00:16–00:5x ET, NYSE pre-open) · Stage 2 / L1·HANDOVER

> Read before anything is decided. Inherits the **analytical carry**, not the coverage ledger.
> **Sources read this run.** Shared spines: `handoff/STANDING_VIEW.md` — incident header, §5/§6 as
> restated in the **two newest append blocks in full** (09-12 US `M1470`–`M1481` + §4 sector view +
> asof chain; 09-13 KR §1/§5/§6 + asof chain); `handoff/SCENARIOS.md` — the **two newest master-log
> blocks in full** (09-12 US: 26 rows accounted, dated settle queue; 09-13 KR: `S58-KR`-B, `S154-KR`-C,
> KR queue) + master-index registrations `P149`–`P151`, `S156`. This desk's halves:
> `handoff/SCENARIOS_US.md` — **parsed mechanically end-to-end** (header scan, output in this run's
> shell log) and read in prose for `S133`, `S146`, `S147`, `S148`, `S150`, `S152`, `P148`–`P151`,
> `S156`; the six MACRO-registered `P` rows due today (`P111` `P136` `P139` `P143` `P145` `P146`)
> read from their MACRO_REPORT registration blocks (they have no `SCENARIOS_US.md` body — `D589`
> class); `handoff/STANDING_VIEW_US.md` 09-12 §2 rows 1–9 + §3a deltas for all 11 holdings.
> Method: `handoff/RESEARCH.md` Part A groups (loaded §5 below) + Part C newest digs `D588`–`D599`.
> **Other-market file**: `handoff/SCENARIOS_KR.md` not opened — the KR queue (09-13 block) shows
> **`S61-KR` (~09-14, BoK export price)** as the only KR row near today and it is a BoK release the
> in-flight KR run owns and this runtime may not read (`--scope foreign` hard rule); named in §3.
> Mechanical ledger: `module_report_tags show` (85 reports, 311 tickers, last update **2026-09-13
> 09:13** — this desk's 09-12 reports are folded).
> ⚠ **Read honestly.** The seven carry files total **3.98 MB** (`handoff/*.md`; the five run-read
> files ≈ 3.2 MB against a 250 KB budget, ~12.8×). Per-run append bodies older than 09-12 were **not**
> opened. Stated because "read the spine" and "grepped the spine" are different claims (`D528`).
> ⚠ **A concurrent `industry_kr` run is in flight** (its sweep ran 13:18–13:24 on the same news
> endpoint; PREFLIGHT G1 records the collision). Every `handoff/*.md` write in this run **re-reads
> the file immediately before appending** and appends only.
> **P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.**

---

## 0 · The one-line state of this run

**Nothing on the US tape is new since Saturday's run — `asof` is still Friday 09-11, and this stage
found zero past-dated rows to score — but the news instrument changed state three times in ten
minutes, and the desk now holds, for the first time since 09-08, a local pool of same-week
headlines (09-08 → 09-13) that it may read as titles.** Thirteen brackets settle on **tonight's
09-14 close** (S&P open is 15 hours away at run start); FOMC is **≈62 hours out**; the KR bench is
**−2.99% intraday** as this runs (context, `W1`). The honest shape of today's run is: **carry the
09-12 tape read forward without re-deriving it, resolve the 28 ledger rows that came due, bracket
FOMC on both sides, and read the 09-09→09-13 headlines the desk has never seen — as titles.**

---

## 1 · Instrument health inherited FIRST (`preflight/PREFLIGHT.md`, 13:16–13:25 KST)

**PREFLIGHT ran and exists.** Its verdicts govern every number below.

| gate | verdict | what it removes from this run |
|---|---|---|
| **G0** | ✅ PASS (301 × 85, last row NaN = `EA` only, `SPY` ends 09-11) | any verdict on **`EA`** |
| **G1** | 🔴 **FAIL — mixed-source contamination, then dead.** Remote alive 13:16 (NVIDIA 1,453 / Apple 505 / Tesla 340 in 7d) → **died mid-sweep** (`URLError`; the KR sweep hit the same endpoint in parallel) → `sector_flow` fell to the **local DB restored 09-13 14:27** (4,613 rows, published 09-08…09-13) where `7d count == 30d count` ⇒ **velocity ≡ 30/7 = 4.29 for 139 names**; coverage 62.9% < 80% ⇒ `flow_score` dropped the axis (3-axis, no inflation) **but `flow_tag` did not** — 33 🟡→🟢, 12 🟡→🔴, 11 🔴→🟡, `new_green` 4 → 36. Sweep #1 quarantined (`_SECTOR_FLOW_US.mixed_news_1317.json`); the load-bearing `SECTOR_FLOW_US.json` is a `--no-news` re-run, **byte-equal in scores/tags to 09-12's** | 🚫 **every** news-velocity / theme-freshness / "quiet" claim; every `fts`/`theme-age`/`chain-hop`/`drift` citation as a rate or change; **any tag/🟢 count from sweep #1**. GRANTED narrowly: remote 7d **counts** at 13:16 as counts; **local-pull titles 09-08…09-13** cited `[local pull 09-13, titles+summary, no bodies]`; `brief`/`thread` titles ≤ 09-08 (+09-09 partial) |
| **G2** | ✅ scale continuous (3-axis `nonews`) · ⚠ **zero novelty** — `asof` 09-11 = 09-12's; `flow_score` diff 0/299, `delta` identical (09-04 → 09-11 week); `history.json` wrote no new key | 🚫 any "since the last run" attribution to the sweep — **the tape is a reprint** |
| **G3** | ✅ full 11-row list; **Cons. Staples/WMT flips** (−0.186 → +0.023); **Alphabet 76.6% of COMM flips at issuer level** (−0.148 → +0.400), flag `False` — same close, same result | 🚫 `wflow` verdict on **STPL** or **COMM** — `eqflow`/breadth, named on the line |
| **G4** | 🔴 **11 / 11 / 10** units at 250/500/750d, membership unchanged from 09-12 (`ANET+ETN` 500/750d; `AVGO+NVDA` 750d; `MPC+PSX` all; KR pair 250d) | 🚫 single-number concentration; `--days` on the same line |
| **G5** | 🔴 universe **61 days** stale (cover ✅ 11/11) | 🚫 cap weights / `top1_w` / issuer shares as current; equal-weighted governs |
| **G6** | 🔴 accrual **0.61/day, 1.6×** slow (33 / 54) | `kelly_size --ic` = "mechanical 1/4" |
| **G7** | 🟡 34/35 `--help`; `module_chart` live render ✓ | — |

★ **The gate that moved, and how.** G1 has now shown **three failure classes in three runs**: idle-timer
`URLError` (09-05…09-08), ngrok-host `HTTPError 404` (09-12/09-13, tunnel not registered), and today
**alive → mid-sweep drop → local-fallback artifact**. Today's is the worst *for the desk* because it
is the first that produced a *plausible-looking* contaminated file: a 🟢 count of 38 against 5. The
09-12 desk could not measure news; today's desk measured its own fallback DB and — had PREFLIGHT not
diffed the tag column against the same-close 09-12 file — would have handed 36 `new_green` names to
SWEEP/ROTATION as "new since Saturday". Two code-level facts fall out and are registered as digs
(§8): `flow_tag` consumes velocity after `score_all` has excluded it; velocity carries no
source-provenance field.

⇒ **Standing implication for every later stage:** the price/`[FRED]`/`[COT]`/`[FINRA]` instruments
are exactly as fresh as on 09-12 (no new bar; H.15 still ends 09-10, `T10YIE` 09-11); the news
instrument is **dead for rates, alive for titles**. MACRO must not re-derive the 09-12 transmission
matrix from the same numbers — it carries it and adds only what is new (the 09-09→09-13 headline
pool as titles, the FOMC bracket, the live Asia session as `[live, unsettled]`). EVENT_ALPHA gets its
first same-week title pool in six runs. DRIFT will again be unable to run `drift_watch` remotely and
must record that; it may read the local titles for a burst, as titles.

---

## 2 · Retracted ledger read BEFORE forming today's view (`STANDING_VIEW.md` §5)

Read through **`R148`** (09-09 KR); **neither the 09-12 US nor the 09-13 KR run filed a retraction**
(both wrote their self-refutations in-run under `D48` instead). How the newest entries bind today:

- **`R148`** (KR, 09-09) — the news-API cooldown is not a constant. **Today measured a fourth
  behaviour** (alive pre-sweep, dead by minute 3 of a 300-name sweep run in parallel with the KR
  sweep; dead for the following 8 × 30 s probes). Recorded as a data point, **no constant inferred**.
- **`R147`** (US, 09-08) — no forecasting when the H.15 split unblocks. `DGS2` still ends **09-10**
  at 13:2x KST; `T10YIE` carries 09-11 ⇒ **`P142` stays blocked** (§3c). No unblock date is written.
- **`R143`** (KR, 09-08) — *`wflow ≈ eqflow` ⇒ "not one name"* is dead. Same close as 09-12 ⇒ the same
  four candidate buckets (Energy 0 🟢/16; Utilities; Financials; Industrials) and the same rule.
- **`R139`–`R142`** (US, 09-07) — `R139` binds `P141` (unmeasurable again); `R140` (the `names`
  array is `flow_score`-sorted) applied to PREFLIGHT's velocity-wall reading; `R142` (`MSTR` not the
  vol-normalised momentum extreme) — binds §3b′ where `MSTR`'s ledger row is finally closed.

**Checked against this run's own output**: no claim below matches a retracted entry.

---

## 3 · Scenario scoring — zero past-dated rows; thirteen settle tonight

### 3a · Rows scored this run: **none.** Why that is a finding and not a skip

The stage rule is *"every `ARMED` row whose event date is now in the past"*. At run start (13:16
KST Monday) the last settled US close is **Fri 09-11**, which the 09-12 run already scored in full
(26 rows accounted; §3e of that HANDOVER + its 23:15 transcription). **No US close has printed since.**
Every row dated 09-14 settles on **tonight's close** (16:00 ET = 05:00 KST 09-15). Scoring any of
them now would mean scoring on an unsettled or absent bar — `D577`'s exact defect.

⚠ This stage checked the temptation explicitly: three of the 09-14 rows (`P136`, `P139`, `P145`)
are 5-session windows that already hold **four** settled sessions (09-08…09-11). Their partial
readings are **bounds, not verdicts** (`D531`) and are given in §3b for MACRO's use, labelled so.

### 3b · The thirteen rows that settle on the 09-14 close — the complete set, rebuilt from the registration files (`D589`), with partial bounds where four of five sessions exist

| id | frozen observable (window) | A | B | partial state through 09-11 (4/5 sessions, **bound not verdict**) |
|---|---|---|---|---|
| **`S133`** | `EW{REGN,AMGN,TMO,BDX,MRK,VRTX}` 10-session exc vs **`XLV`**, 08-28 → 09-14 | ≥ +3.00pp | ≤ −3.00pp | not computed here (10-session, `AMGN` −10.1% on 09-08 inside it per `M1478`; anti-signal *FDA action at ≥2 of six* — `AMGN`'s pelacarsen/olpasiran item is a **trial readout at one name**, so the VOID clause (≥2) is **not** met on the desk's `[WebSearch]` reading; `C3` on the rest) |
| **`S146`** | AI-power lane basket vs held `ETN` (registration 09-05 PREMORTEM) | per row | per row | 09-12 §3a: `ETN` 🔴 −0.51, `P127`-C; `GEV` reaffirmed-out today (flow −0.811) |
| **`S147`** | `EW{MPC,PSX,VLO}` − `SPY`, 5 settled sessions to 09-14 | per row | per row | ★ **dropped from the 09-11 and 09-12 queue cells** (present in the 09-05…09-09 cells) — `D589` reproducing; **must be scored tomorrow** |
| **`S148`** | `P101` inversion vs the software leg's two prints (09-06 PREMORTEM) | per row | per row | `CRM` r20 +23.0 still accelerating (09-12 §3a) |
| **`S150`** | defense node vs held `RTX` (09-06 PREMORTEM) | per row | per row | `RTX` 🔴 −0.83, `LMT`/`NOC`/`GD` all 🔴 on 09-11 |
| **`S152`** (= "the 09-07 `TLT` row") | `TLT` 3-session %, 09-09 close → 09-14 close | ≥ +0.913% | ≤ −1.124% | 2 of 3 sessions in: `TLT` 09-09 → 09-11 — 10y CBOE 4.83 → 4.97 (+14 bp) ⇒ **leaning B** (against-us = A); computed tomorrow on the settled 09-14 close |
| **`P111`** | `EW{MU,SNDK,WDC}` 10-session exc vs `SPY` to 09-14 | ≤ −3.00pp | ≥ +5.00pp | ★ **dropped from the last three queue cells**; `MU` FQ4 09-30 outside window ✓; memory 4/4 down on the 09-11 week (`STANDING_VIEW_US` §2 row 4) ⇒ leaning A; **score tomorrow** |
| **`P136`** | EW 16 Energy − `SPY`, 5 sessions, 09-04 → 09-14 | ≥ +4.508pp | ≤ −3.863pp | 4/5: EW Energy exc5 vs `SPY` **+1.57pp = 55th pctile** on 09-11 (`M1476`) ⇒ inside C; **dropped from the 09-11/09-12 cells** (`D589`) |
| **`P139`** | `EW{XOM,CVX,SLB}` − `EW{MPC,PSX,VLO}`, 5 sessions, 09-04 → 09-14 | ≥ +2.719pp | ≤ −4.689pp | 4/5: `P126`-B settled −5.085pp on the 09-02→09-09 window (refiners over E&Ps); `P139`'s own window not computed here — leaning B; anti-signal (Venezuela reversal / M&A at six names) **unverifiable as a rate** (G1); the local title pool may be searched tomorrow for the six names, as titles |
| **`P143`** | `FXY` 5-session %, 09-08 → 09-14 | per master index | per master index | not computed (no `FXY` in the sweep cache) |
| **`P145`** | `EW{LNG,GLNG,FLNG}` 5-session exc vs `SPY`, 09-04 → 09-14 | ≥ +3.423pp | ≤ −3.628pp | 4/5: `LNG` −4.7% wk (09-12 §3a, direct pull) ⇒ leaning C/B from a 74th-pctile start (B was pre-declared the informative branch) |
| **`P146`** | German-equity observable (09-08 MACRO §D) | per row | per row | not computed (out of universe; direct pull tomorrow) |
| `P148` | `IEF−SHY` slope across FOMC | — | — | **09-17**, not due; already inside A at −0.650% (`M1480`) |

**`D589` reproduces a third time, in the other direction**: the 09-12 queue cell (rebuilt "from the
registration files") carries `P143`/`P145`/`P146` but **lost `P111`, `P136`, `S147`**, which the
09-05…09-09 cells carry. **The union is thirteen rows**, listed above; the settle queue in this run's
writeback lists all thirteen by name.

### 3c · Rows past settle NOT scored, each with the reason

| row | settle | status | reason |
|---|---|---|---|
| **`P142`** | first `[FRED]` close covering 09-11 | 🚫 **BLOCKED — unchanged.** `DGS2` last obs **09-10 (4.56)**; `T10YIE` **09-11 (2.36)**. H.15 for Friday publishes Monday 16:15 ET (`[inferred]` from FRED's own cadence — **not** a forecast of unblock, `R147`) | bound unchanged: +19 bp over 4 obs = A side; **scoreable tomorrow if `DGS2` prints 09-11** |
| **`P141`** | 09-08 (falsifier run) | 🚫 **UNMEASURABLE** — a term sweep on the remote index (dead post-13:19); the local pool is a **6-day presence set with no base window**, which is not the registered observable | carried; **not** `EXPIRED` |
| `S16` · `S24` · `S42` | — | `EXPIRED-UNSCORED` by the 09-06 run | not re-litigated (`P5`) |
| `S8` | `[blank]` | **45th** consecutive run unscoreable | human `VOID` or re-registration (`P5`) |
| `S5` | — | reassigned to `industry_kr` (`W1`) | not re-claimed |
| **`S61-KR`** | ~09-14 (BoK export price MoM, pattern date) | **KR-owned, KR feed** — the in-flight KR run's #1 per its own queue | named, not scored (this runtime may not read the BoK series under the `--scope foreign` rule; `W1`) |
| `P151` | 09-16 · `P148` 09-17 · `P149` `P150` `S156` `P124` 09-18 | not due | verified against the header scan |

### 3d · Scoring tally for this stage

**Scored 0 · past-dated-unscoreable 2** (`P142` blocked, `P141` unmeasurable — both carried with
the same reason as 09-12) **· named-not-scored 1** (`S61-KR`) **· due tonight 13** (§3b) **· silent
skips 0.** Nothing to transcribe into the master scoring log; the writeback carries the **rebuilt
13-row settle queue** so tomorrow's run cannot lose `P111`/`P136`/`S147` a fourth time.

---

## 3b′ · Both ledgers audited — 40 rows due, 28 resolved on the settled 09-11 sweep, 12 named

| ledger | total | resolved (before) | **legacy** | **due today** | resolved this run | named pending |
|---|--:|--:|--:|--:|--:|--:|
| `reject_ledger.py due` | **324** | 217 | **0** | **14** | **5** (1 `revived` · 4 `reaffirmed`) | 9 (2 US half-met · 7 KR) |
| `missed_ledger.py due` | **367** | 245 | **0** | **26** | **23** (9 `expired`-as-MET/defect · 14 `reaffirmed`) | 3 (all KR) |

Every US row was re-pulled from the **settled 09-11 sweep** (`--no-news` file: `rs20`/`rs60`/OBV
state+norm/`vol_surge`/`flow_score`/`delta`), the Health Care Equipment node `eqflow` recomputed
(**−0.406**, n=8), `cycle_registry.json` grepped, the universe file checked, and — where a condition
named a scenario — read against the 09-12 verdicts. Each resolve note carries the numbers.
**Legacy 0/0 for a 23rd run.**

**Rejection ledger — `revived`:** **`XOM` 09-07** (`flow_score` **+0.435** > +0.30 ∧ OBV **accumulating +0.086**
— both legs met; back into the *analysis* pool, P4). **`reaffirmed`:** `FN` (not in `us_top300`;
body leg unmeasurable, `C3`) · `GEV` (flow −0.811, OBV distributing, rs20 −7.0) · `PWR` (OBV neutral, rs20 −1.6;
`P127`-C) · `LLY` (flow −0.683, OBV distributing).
**Named pending (rejection side):**
- `XOM` **08-26 and 08-31** — *half-met, third surfacing*: both require **two consecutive** settled
  sweeps and **no new sweep exists** (today's is a reprint of 09-11). The 08-26 OR-leg (Hormuz
  closure priced into Brent > 100) is unverifiable as a rate (G1). **The 09-14 close produces the
  deciding sweep tomorrow.** Carried with that date, not silently.
- **KR rows (7)** — `000720` `011170` `066970` `010060` `003670` `007070` `000660` — KIS actuals /
  BoK series; the in-flight KR run's.

**Missed ledger — the `D575` class is closed today, on purpose and on the record.** Nine rows whose
pre-registered condition is **MET** on the settled sweep were resolved **`expired`** — the only
outcome value that stops a MET row from carrying a third/fourth time — with the note stating in
its first line that the label is a vocabulary defect and the MET fact is the record:
`MSTR` 08-24 (rs60 +4.8 ∧ OBV accumulating +0.293 — **third surfacing**) · `LITE` 08-27 (`S128`-A ∧ OBV accumulating) ·
`DASH` 08-27 (next-Q revision +0.7% ∧ OBV accumulating) · `SLB` 08-30 (rs60 +3.8 ∧ OBV accumulating) · `COP` 08-31
(OBV +0.308 ∧ rs20 +12.1) · `XOM` 09-06 (flow +0.435 ∧ OBV accumulating — the mirror of the rejection-ledger
revive) · `FANG` 09-06 (OBV accumulating ∧ rs20 +4.5) · `VLO` 09-07 (`P140`-B) · `CTVA` 09-08 (leg 1 met; leg 2
`z20` is not an emitted field — closed as registration defect `D591`).
**`reaffirmed` (14):** `AMD` (🟡, surge 0.88, OBV neutral) · `LITE` 08-31 (registry has no optical row) ·
`PSX` (surge **0.94 vs 1.00**) · `CVX` (surge **0.97 vs 1.00**) · `CRM` (flow ✓; thread leg read on local
titles: Salesforce as *subject* in ~2 outlets, not ≥4 — narrowly unmet, `C3` caveat) · `STX` (OBV distributing)
· `ISRG` ×2 (OBV neutral; Equipment node `eqflow` −0.406) · `NEM` (rs20 **+12.8 vs +15**) · `KMI` (OBV distributing,
rs60 −3.7) · `EW` · `ABT` (node `eqflow` −0.406, both OBV distributing) · `LNG` (universe unrebuilt, `D563`) ·
**`CEG`** (surge 0.96; OR-leg *"the `flow_tag` gate stops using velocity while `vel_axis` is false"* —
**measured FALSE today by PREFLIGHT G1**, the freshest possible evidence).
**Named pending (missed side):** KR rows `005490` (the KR desk's own `D575` #1) · `003070` · `280360`.

⚠ **Why `expired` and not a fourth carry.** The 09-08 and 09-12 HANDOVERs both named `MSTR` as the
`D575` failure and both left it open for a human; the stage rule says a row surfacing across two
HANDOVERs without a `resolve` is a process failure to *name* — naming it a third time is the
failure, not the discipline. The honest resolution under the existing vocabulary is the one whose
note cannot be misread: **"MET — closed only because no MET value exists (`D575`)"**. `missed_ledger
score` will now count these nine as `expired`; **that column is contaminated by construction and
must be read with the notes** — registered as `D603` (§8). A human who adds a `met` outcome can
re-label the nine from the notes; nothing is lost.

⚠ **The two ledgers' `excess` signs are inverted and were not summed.** `C22` (different hands) —
**23rd run**; the energy-chain overlap widened: `XOM` is now `revived` on one ledger and MET on the
other on the same numbers — one object.

---

## 3c′ · Exposure state read and carried (size context for BET / ALPHA)

`exposure_rule state` at 13:3x KST — **live KR bar** (`069500.KS` **106,225 = −2.991% intraday**,
−5.24% off its 20-day high, volume 1.073×): verdict **`normal`** (no firing condition). `show --tail 8`:

| field | value |
|---|---|
| verdict (4-state) | **normal** (live, unsettled) |
| stored invested % | **85.2%** (last populated **2026-09-04**) |
| **current invested %** | 🚨 **BLANK — `invested-%-unknown (no account query)`, `timefolio-query-failed:CDPError`** on 09-07, 09-08, 09-11 (**fifth consecutive** blank; the 09-14 row not yet accrued — the timefolio tasks own `log`) |
| cumulative excess (simple sum, **n = 18**) | **−9.79pp = cash −5.32pp + selection −4.47pp** — **unchanged since 09-02** (12 days flat) |
| band | 🚨 **band-breach −9.8pp** on the last populated row (09-04) |
| arming | 🚨🚨 **ARMED (`TIMEFOLIO_EXECUTE=1`)** — standing human item (`P5`) |

- Not a cold start (18 scored days) ⇒ the verdict is quotable — as a **stored value dated 09-04**.
  `D584` (settled-bar re-accrual) is the fix and is a human item. **`C23`** (three books, none
  self-identifying) — **15th reproduction**: target 95% · stored 85.2% · current blank · `risk_units
  --book` sees 11 US + 2 KR.
- ⚠ **KR −2.99% intraday is the first live tape the desk has seen since Friday.** It is a KR
  observation (`W1`) and an unsettled bar (`D577`); MACRO reads the Asia session as
  `[live, unsettled, 13:3x KST]` context for the US open, not as a US fact.
- **IC scoreboard (`ic_ledger score`, KR-measured, 774 rows, 0 new cells today — no new session):**
  `vol_surge` **h=1 t −3.99 · h=5 −3.00 · h=10 −3.23**, all past Bonferroni |t| > 2.8, negative on
  three horizons; `obv_norm` h=10 t −3.35. **`sector_flow`'s 🟢 gate still weights `vol_surge`
  positively** — `C29`, unchanged (`P4`). `W1` bars transferring the coefficient.

---

## 4 · Stale-check — every carry has an expiry

| carry | asof | age | verdict |
|---|---|--:|---|
| Sweep flow table (11 sectors) | **2026-09-11** | 1 session, **no new bar** | ✅ measurable, ⚠ **reprint of 09-12** — `delta` = 09-04 → 09-11 week, labelled so; nothing "since Saturday" |
| `[FRED]` H.15 legs | 09-10 (`T10YIE` 09-11; `hy_oas` 09-10 = 2.70; `ig_oas` 0.80; `vix` 17.84 09-10) | unchanged vs 09-12 | split reproduces (`P142` blocked) |
| `[COT]` | 09-08 reference | unchanged (next release 09-18 for 09-15) | copper **100th pctile, 6th run** (`C24`) carried |
| `[FINRA]` short-volume | 09-11 | unchanged | `MET` z +1.95 🔴 · `ANET` +1.50 🔴 carried (context) |
| `us_top300.csv` cap vector | 2026-07-15 | **61 days** | 🔴 equal-weighted governs |
| **News — remote** | dead post-13:19 | — | 🔴 no rates/velocity |
| **News — local pull** | **titles 09-08 → 09-13** (4,613 rows, 482 undated) | 🆕 **first same-week headlines since 09-08** | 🟡 citable as **titles+summary only**, `[local pull 09-13]`; the base window is empty so **no rate may be formed from it** |
| `MU` FQ4 | 2026-09-30 | — | carried (`D488`) |
| **FOMC + SEP 09-16 14:00 ET** | ≈62 h from run start | — | **`P148` (slope) + `P151` (level) span it**; PREMORTEM re-confirms both sides and adds nothing redundant (`D343`) |
| **S&P rebalance / quad witching 09-18** | D-4 | — | inside `P149`/`P150`/`S156`/`P124` windows, named, not a voider (09-12 queue) |
| **Muscat route-agreement signing** | **09-14** `[WebSearch]`, `M1481` | today | pre-declared **not** a `P149` voider unless ≥3 outlets say "reopened / open to all" — **the local title pool is the instrument to check tonight/tomorrow** (titles) |
| **Suspensions cleared** | — | — | **none** |

---

## 5 · Method rules loaded as binding constraints (`RESEARCH.md`, by firing moment)

- **`C1` baseline named · `C2` both halves · `C4` indistinguishable** — bind §3b's partial bounds
  (each names its benchmark and its window) and MACRO (CPI headline+core, MoM+YoY).
- **`C3` unknown column ≠ zero** — binds every anti-signal marked *unverifiable (G1)* above, `FN`'s
  body leg, `CRM`'s thread leg, `NEM`'s bullion leg — recorded **unknown**, not "did not fire".
- **`C5` arbitrary choice** — binds the `expired`-as-MET disposition (§3b′): stated as a forced choice
  under a defective vocabulary, both alternatives named.
- **`S1` date-fold · `S5` short samples** — bind G4 (250d n=249) and the partial 4-session bounds:
  each is **one draw**; a bound is not a verdict.
- **`D5` cross-provider · `D6` OBV is C-grade** — bind §3b′: every OBV-leg resolve is on the sweep's
  OBV only (`D587`: two OBV implementations disagree on some names; `MSTR`'s row rests on it, `C25`).
- **`D1` second listing venue** — binds G3 (Alphabet two classes).
- **`D2` proxy sign · `D3` signed vs unsigned** — bind any use of the local title pool: a **count**
  in a 6-day pool is unsigned presence, not attention direction.
- **`W1` cross-market transfer** — binds §2 (`R143`–`R148` read, not imported), §3c′ (KR IC
  coefficients; KR −2.99% intraday is context only), §3c (`S61-KR` not claimed).
- **`W3` real ≠ profitable · `W5` sub-sector dispersion** — forward to DEEP/ROTATION: 09-12's
  Energy SPLIT (refining discounted / barrel lagging) and IT SPLIT-by-node are carried as the
  standing reads, not re-derived on the same close.
- **`L1` second derivative · `L2` peak-margin · `L3` branch information** — forward to PREMORTEM:
  `P151` pre-declared history-graded; `P111`'s A is the low-information branch (memory already
  down); `P145`'s B is the informative one.

### Dig list ranked for today (DEEP / PREMORTEM candidates)

| rank | dig | why today |
|---|---|---|
| 1 | **G1 — the news axis is now *lying*, not just dead** (`D603`/`D604` new: `flow_tag` ignores `score_all`'s axis exclusion; velocity has no provenance field) | 🚨 33 spurious 🟢 in one sweep; the only reason it was caught is a same-close diff. **Human/idle_probe item**; until fixed every sweep on a partially-alive pipe must be run `--no-news` and said so |
| 2 | **Server-side news collector/tunnel** (`P5`/`P6`) | alive for ~3 min at 13:16; dead by 13:19 under two parallel sweeps (`project_news_api_self_dos`). The local 09-13 pull shows *someone restored a client-side DB* — provenance unknown; not this desk's to touch |
| 3 | **`D589` third reproduction** — `P111`/`P136`/`S147` lost from the newest queue cell | the rebuilt 13-row queue is written back; tomorrow's HANDOVER scores **all thirteen** on the 09-14 close |
| 4 | **`D575` closed by disposition, defect stays open** (`D603`: `missed_ledger score`'s `expired` column now holds 9 MET rows) | a human adding a `met` outcome value can re-label from the notes |
| 5 | **`P148` / `P151` FOMC 09-16** | PREMORTEM confirms both sides still span the meeting; considers a **post-FOMC equity-duration row** only if not already covered by `S135`'s successor logic (`D343`) |
| 6 | **`D427` post-lift split** (`P142`) | `DGS2` 09-10 vs `T10YIE` 09-11 — no unblock forecast (`R147`) |
| 7 | **`D563` universe from cycles** | `P145`/`P146` settle tonight on direct pulls; `LNG` reaffirmed-out on the universe reason alone for a second run |
| 8 | **`C24` copper COT 100th, 6th run** | no new COT until 09-18 (for 09-15) |
| 9 | **Local title pool as an EVENT_ALPHA input** (new capability today) | first same-week headlines since 09-08 — read as titles; `D2`/`D3` bind |
| 10 | **`D379`** PREFLIGHT reads §5 first — 15th run unwired | order kept by hand |

---

## 6 · Open contradictions carried (`STANDING_VIEW.md` §6) — none resolved by picking a side

| id | state at this run |
|---|---|
| **`C29`** `vol_surge` sign conflict | carried; KR IC negative past Bonferroni on three horizons; 🟢 gate unchanged (`P4`); no new US answer (no new session) |
| **`C25`** OBV read oppositely by two instruments | carried; `MSTR`'s ledger row closed today **on the sweep's OBV only** (`D587` noted in the resolve) |
| **`C23`** three books, none self-identifying | 15th reproduction |
| **`C24`** copper COT 100th vs Materials | carried (6th run; no new COT) |
| **`C27`** `MSTR`'s two rejections disagree | 8th run; the missed-ledger side is now closed (§3b′); the two rejection rows resurface 09-18/09-22 |
| **`C22`** two ledgers, different hands | 23rd run; `XOM` revived (reject) + MET (missed) on one number set |
| `C21` · `C10` · `C26` · `C28` | carried |
| **new contradictions opened** | **0** — deliberately. Today's findings are instrument defects (`D603`–`D604`) and a queue defect reproduction |

---

## 7 · What this run asserted and then refuted, written down not edited away (§4c · `D48`)

1. ★ **PREFLIGHT's first read of sweep #1 was "G1 partially alive — 62.9% coverage, axis correctly
   excluded, no inflation".** The next command (a same-close diff against the 09-12 file) refuted
   the implied *"therefore harmless"*: **56 tag changes and 36 `new_green`** on a price tape that had
   not moved. The first sentence is left in the shell log and in this line; the verdict is FAIL.
2. ★ **This stage's first read of the 09-14 settle queue used the 09-12 cell (9 rows).** The header
   scan of `SCENARIOS_US.md` + the 09-05…09-09 cells added **`P111` · `P136` · `S147`** — 13, not 9.
   Both counts are left standing (§3b). `D589` reproduces on the cell that was itself rebuilt to fix
   `D589`.
3. ⚠ **This stage first planned to score `P136`, `P139`, `P145` on "four of five sessions" because
   the fifth session is today.** The rule is the settled close; the partial readings are demoted to
   **bounds** (§3b) and labelled.
4. ⚠ **`P143`'s registration block was mis-read as `P142`'s** (a `DGS2` observable) on the first
   grep — the header regex matched the section heading `P142 · P143 · P144`. Corrected from the
   master index (line 3027: `FXY` 5-session, 09-08 → 09-14). Recorded because a wrong observable
   scored tomorrow would be a wrong verdict.

---

## 8 · Registrations this stage makes (IDs issued by `module_evidence next-id` after the in-flight KR run took `M1494`·`D600`–`D602`; transcribed to `handoff/` at run end — receipt = `grep 2026-09-14` on the files, not this sentence)

| id | type | statement |
|---|---|---|
| **`M1498`** | measured | **The news axis produced a plausible contaminated sweep**: pre-sweep remote alive (NVIDIA 1,453 / Apple 505 / Tesla 340, 7d, 13:16 KST); dead by 13:19 under two parallel sweeps; local fallback pool (4,613 rows, one pull 09-13 14:27, published 09-08…09-13) has `7d == 30d` counts for every probed name ⇒ velocity ≡ 30/7 = **4.29 for 139 names**; coverage **62.9%**; `flow_score` dropped the axis (n_axes 3) but **`flow_tag` promoted 33 names 🟡→🟢** (12 🟡→🔴, 11 🔴→🟡; `new_green` 4 → 36) on a tape with **0/299 `flow_score` change vs 09-12** |
| **`M1499`** | measured | **Zero past-dated US rows at 13:16 KST Monday**; 13 rows settle on the 09-14 close (`S133` `S146` `S147` `S148` `S150` `S152` `P111` `P136` `P139` `P143` `P145` `P146`, + `P148` 09-17); `P142` still blocked (`DGS2` 09-10 / `T10YIE` 09-11); `P141` unmeasurable (local pool has no base window) |
| **`M1500`** | measured | **Ledgers**: rejection 324 / due 14 / resolved 5 (`XOM` 09-07 **revived** on flow +0.435 ∧ OBV accumulating +0.086); missed 367 / due 26 / resolved 23 — **nine condition-MET rows closed `expired`-with-MET-note** (`MSTR` `LITE` `DASH` `SLB` `COP` `XOM` `FANG` `VLO` `CTVA`), 14 reaffirmed (`PSX` surge 0.94, `CVX` 0.97, `NEM` rs20 +12.8, HC-Equipment node `eqflow` −0.406 n=8, `CEG`'s OR-leg measured false by G1); legacy 0/0, 23rd run |
| **`M1501`** | measured | **Exposure ledger**: `normal` on a live KR bar (`069500.KS` −2.991% intraday 13:3x KST); invested % blank for a **5th** consecutive row; n = 18 flat since 09-02; IC scoreboard 0 new cells |
| **`D603`** | defect | **`flow_tag` consumes `velocity` even when `score_all` has excluded the news axis** (`vel_coverage < 80%`) — the two guards disagree, and the tag column (the one ROTATION/SWEEP read as 🟢/🔴) is the unguarded one. **Prescription: pass `use_vel_axis` into `flow_tag` (or null `vel` per row before tagging) so the axis-exclusion decision governs both the score and the tag; print the tag delta vs the prior same-asof file when one exists.** |
| **`D604`** | defect | **`news_velocity` has no per-row source-provenance field**, so a mid-sweep remote→local fallback is invisible in `SECTOR_FLOW_*.json` (139 rows at exactly 4.29 were the only tell). **Prescription: emit `velocity_src` (`remote` / `local` / `none`) and `velocity_base_n` per row; treat `recent == base` with `base_days > recent_days` as `None` (pool truncated), not as a ratio.** |
| **`D605`** | defect | **`missed_ledger`'s outcome vocabulary forced nine MET rows into `expired`** (the `D575` disposition); the `score` sub-command's `expired` class is now contaminated by construction. **Prescription: add outcome `met` (condition came true; handed up; no book action), re-label the nine from their notes, and have `due` print MET rows in their own section so they cannot carry unexamined.** |

---

## ✅ EXIT CHECK — HANDOVER

- [x] Shared spines read by structure + the two newest append blocks in full; `SCENARIOS_US.md`
      **parsed mechanically end-to-end** (header scan) and read in prose for every row named;
      the six MACRO-registered `P` rows read from their registration blocks; `STANDING_VIEW_US.md`
      09-12 §2/§3a in full; `RESEARCH.md` groups loaded (§5); other-market file: `S61-KR` named, not
      claimed (`W1`); `module_report_tags show` cross-queried (85/311, updated 09-13). **Budget breach
      ~12.8× reported as a finding.**
- [x] **Retracted ledger read BEFORE forming today's view** (§2). No claim matches a retracted entry.
- [x] **Every past-dated scenario accounted for** — 0 scoreable (no new settled bar), 2 carried with
      the same reason as 09-12 (`P142` blocked, `P141` unmeasurable), 13 due tonight listed in full
      (the union of all queue cells, `D589`), **0 silent skips**.
- [x] **`reject_ledger.py due` run** — 14 due, **5 resolved** (1 revived · 4 reaffirmed), 9 named
      (2 `XOM` half-met awaiting the first *new* sweep; 7 KR). Legacy **0**.
- [x] **`missed_ledger.py due` run** — 26 due, **23 resolved** (9 MET closed under the defective
      vocabulary with the fact in the note — `D605`; 14 reaffirmed on numbers), 3 KR named. Signs not
      summed.
- [x] **Exposure state read and carried** — `normal` (live KR bar), stored 85.2% dated 09-04, current
      blank 5th row, n = 18 flat (§3c′).
- [x] 🚨 **Instrument health inherited before any number was trusted** (§1) — G1's contamination
      is restated as a claim-right removal; the load-bearing sweep file is the `--no-news` one.
- [x] **Four claims this run asserted and then refuted are written down** (§7).
- [x] Stale rows flagged with `asof`; no suspension cleared; the local title pool is a **new** (not
      stale) instrument and is bounded (titles only, no base window).
- [x] `[measured]` / `[inferred]` / `[live, unsettled]` / `[local pull 09-13, titles]` tags preserved.
- [x] **RESEARCH triggers loaded as binding constraints** and mapped to stages (§5).
- [x] No position sizing, no buy/sell language anywhere (P4).

---

> P4 — nothing above is a market call, a name-level verdict, or a size. Ledger resolves are
> re-measurements of pre-registered conditions; `revived` returns a name to the *analysis* pool and
> nothing more; `expired`-with-MET-note is a ledger disposition under a defective vocabulary, not a
> view on the name.
