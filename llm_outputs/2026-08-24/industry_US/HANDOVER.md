# HANDOVER — industry_US · 2026-08-24 (Mon) · Stage 2/11 · L1·HANDOVER

> Inheritance packet. **This stage transports analysis; it makes no market call, names no size and
> issues no buy/sell language (P4).** Run clock **KST 22:10–23:0x = ET 09:10–10:0x, MONDAY** —
> US cash **opens at 09:30 ET, inside this stage's window**. Terminal settled bar throughout:
> **2026-08-21 (Friday close)** — **the same bar the previous two runs ended on.**
> Read: `handoff/STANDING_VIEW.md` (spine §1–§6, retracted ledger through **`R97`**, `§6` open
> contradictions through **`C15`**, incl. the `industry_kr` block appended **this morning 10:09 KST**) ·
> `STANDING_VIEW_US.md` · `SCENARIOS.md` (spine scoring log + MASTER INDEX) ·
> `SCENARIOS_US.md` (**S1–S117**, `P13`–`P92` — `S74` and `S102` opened in full) ·
> `SCENARIOS_KR.md` (**opened** — no past-dated row; earliest KR settle **2026-09-04**) ·
> `RESEARCH.md` (Part A/B/C through **`D329`** / **`D330-KR`–`D335-KR`**) ·
> `REPORT/COMPANY_SCOREBOARD.md` (**body opened, not just the listing** — `D330-KR`'s remedy, applied
> the run after it was written).

---

## ★★★ The three things this packet exists to hand forward

1. ★★★ **`R98` — the US signal ledger exists, it has existed for weeks, and it says the OPPOSITE of
   the KR one on the axis that gates every 🟢.** Yesterday's §6 concluded *"the ledger is `market=kr`
   … the US desk has **no equivalent measurement** and therefore no verdict."* **That is false and was
   false when written.** `ic_ledger.py score` **defaults to `--market kr`**; run with `--market us` it
   returns a 15-test table over **33 US run-dates**. And the sign inverts: **`vol_surge` h=1 is
   `IC +0.0398`, `t(NW) +3.40`, 67% positive — a Bonferroni pass in the POSITIVE direction** (`M854`),
   against KR's `−0.0454 / −3.86 / 24%`. **The 🟢 gate weighting `vol_surge` positively is vindicated
   on US data and condemned on KR data.** The `W1` block was correct; what was wrong was concluding
   the US had nothing to say. §6, §7.
2. ★★★ **The strongest cell in either ledger is `rs60` in the US, and it is negative.**
   h=5: `IC −0.1310`, **`t(NW) −5.46`**, **7% positive**, `n_eff 5.4` — Bonferroni pass; h=1 the same
   sign (`−0.0635 / −2.77`) (`M855`). **Two of the sweep's four surviving axes are relative-strength
   legs, and in this window they rank against 1–5-session forward returns.** This is a `[measured]`
   US fact, not an import. Regime label required on every citation (§6).
3. ★★★ **`S74` is SCORED — `FIRED-C` — and its own anti-signal (a) partially fired at the same time.**
   A **partial Hormuz reopening happened** (Iran issued special permits for some Iraqi tankers, IRNA
   via Reuters 08-22, ≥3 outlet bodies) **with no statement on either of the two named conditions** —
   it ran on bilateral Iraqi diplomacy instead. S74's registered anti-signal (a) says exactly this
   case means *"the conditions were never the binding variable and this row's whole framing is
   wrong."* **The bracket settles C and simultaneously reports that its own frame is partly wrong**
   (`M857`). §2.

---

## §0 · Instrument health inherited — what this run may NOT claim

`llm_outputs/2026-08-24/preflight/PREFLIGHT_US.md` **was run** (22:10–22:30 KST, this run's stage −1).
**PASS 3 / FAIL 5** — the same verdict *pattern* for a third consecutive day. The rights table binds
every stage below and is not re-litigated here.

**Revoked for this run:**
- ★ **Any sentence of the form "since our last run, X moved / turned / accelerated."** False by
  construction — **`n_new_sessions_since_prior_run = 0` for the second run running**, and today's
  persisted sweep is element-identical to both 08-23's and 08-22's (0 of 299 `flow_score`, 0 of 299
  tags, 0 of 11 sector `wflow`). Friday's Δ (08-20→08-21) is citable **as Friday's Δ**, labelled as
  the same one two prior runs used.
- ★ **New today: no blending of a live Monday quote into the `asof = 2026-08-21` frame.** The bell
  rings at 09:30 ET inside this window. A post-open print is a **live intraday print** and carries
  that label. (One such print is used below, correctly labelled: Brent **−1.3% to $93.16**, WTI
  **−1.9% to $85.42**, quoted at **04:32 ET 08-24** in a wire body — §2.)
- The sweep's **news-velocity axis** (`vel_coverage` exactly **0.0**) · any *"it went quiet"* sentence
  sourced from sweep silence · the **Consumer Staples `wflow` sign** (`WMT` **28.9%** owns it) · any
  concentration number without its `--days` · market-cap-weighted claims resting on universe weights
  (**40 days** stale) · any flow/RS/OBV/short call on **`EA`** (12th run unmeasurable) · `--ic`-derived
  sizes as evidence-backed · **KR-holding P&L, stops, or percent-of-total-assets** (the book prints
  `n/a` on both KR marks for a 5th run ⇒ the **17,607,290 KRW** denominator is computed without them) ·
  **any 08-22 / 08-23 / 08-24 settled price** (no bar exists).
- ★ **New today: the news-coverage defect may not be described as random, scattered or
  self-cancelling.** PREFLIGHT §1 measured the bucket positionally: **universe ranks 0–48, contiguous
  from rank 1, the identical 49 names as yesterday (49/49), 16.4% of names but 69.0% of universe
  market cap** (`M856`). Breadth must be re-derived from the **score** column, which never sees `vel`.

**Granted:** settled prices and every price-derived statistic through the **2026-08-21** close ·
`flow_score`, RS, OBV, `vol_surge` · `eqflow` for all 11 sectors and `wflow` signs for the ten
non-flippers · **today's tag layer** (`velocity: null` on all 299 ⇒ provably velocity-free, citable as
*3-axis unanimity*, never as *news-confirmed*, and never compared to a pre-08-22 run's breadth) ·
FINRA short pressure · CFTC COT · FRED (**with each series' own last-observation date on the same
line** — `D333-KR`) · primary filings · `module_chart --read` and `margin_history <T>` (with the
"`--help` dead, output probed" stamp) · **direct news calls made outside a sweep window** — today
**44/44 successful**, including a 40-name falsification probe that returned **40/40 valid**.

★ **The news mechanism is no longer inherited — it is measured.** PREFLIGHT §1 today established the
bucket by *position*, so the standing "≈100 remote calls ≈51 names, hard contiguous cut" is promoted
from inference to measurement. **Practical consequence for every stage below: the sweep spends the
entire news budget on the 49 largest caps, so any name outside the top 49 is guaranteed
velocity-free, and any hand query should be spent on ≤50 names at a time on the handful that matter.**
Cumulative falsification ledger: **400 hand-checks over ten runs, 0 false silences.**

---

## §1 · Inherited regime call and standing view

**Regime (spine §1, `[inferred]`, unchanged):** *memory is a price-cycle industry in rate-of-change
deceleration while its level stays tight* — the equity tracks the **second derivative** of price, not
the level, which is why "shortage persists" and "stocks struggle" are both true.
**This run produces no new price measurement bearing on it** (zero new settled sessions).

⚠ **The per-name table below is NOT a fresh measurement.** Every figure is the **08-21 settled close**,
identical to what the 08-22 and 08-23 packets carried; this run's sweep reproduced them with **zero
differences**. Reproduced as *inheritance*, explicitly stamped — a HANDOVER that silently reprints
yesterday's numbers under today's date is manufacturing evidence.
⚠ Per `C11`, every OBV figure names its instrument: all are the sweep's **`obv_norm`** — a 20-session
change of cumulative signed volume ÷ 20-day mean volume (a **LEVEL**), not `module_chart`'s 10-session
slope of a rolling-20 (a **RATE**).

**The 11 book names, 08-21 settle — reproduced, not re-measured (0 differences vs the 08-23 file):**

```
PSX  +0.728 rs20 +13.8 rs60 +37.0 OBV accum   MPC  +0.700 rs20 +13.0 rs60 +44.0 OBV accum
HPE  +0.489 rs20  +8.5 rs60 +41.6 OBV accum   ANET +0.417 rs20  +4.8 rs60 +20.2 OBV accum
NUE  +0.319 rs20  −5.2 rs60  −3.2 OBV accum   ETN  +0.210 rs20  +0.1 rs60  +1.1 OBV accum
NDAQ −0.025 rs20  +3.0 rs60  +6.5 OBV neutral RTX  −0.122 rs20  −5.0 rs60 +16.8 OBV neutral
MET  −0.164 rs20  −4.1                        NVDA −0.181 rs20  +0.2 OBV neutral
AVGO −0.221 rs20  −7.2 OBV neutral
```
**All 11 tag 🟡중립 for a third run.** With `vel_coverage = 0.0` that is the honest output of a
velocity-free tag layer, **not a statement about the book** (PREFLIGHT G5).
★ **New interaction measured today**: **9 of the 11 holdings sit below universe rank 49**, so on a
partial-coverage run their tags could not have been contaminated at all. **`NVDA` and `AVGO` are the
only two book names inside the news bucket** — the only two whose tags a partial run could move.

**Carried per-name state (tags preserved, `asof` 2026-08-21 on every price figure):**

| Node | Carried state | Tag | Stale? |
|---|---|---|---|
| **`MPC` · `PSX` · `VLO`** | Refining-**capacity** destruction; the constraint is `L2` peak margin, not the barrel. `M831`: MPC's 10-Q has **zero** take-or-pay and the only long-term structure (MPLX minimum-volume commitments) runs the **wrong way** ⇒ **Micron's contracts floor REVENUE, Marathon's floor COST** | `[measured]` price · `[filing]` structure | ⚠ **The FY2025 10-K Item 1A remains unopened** — carried as unopened for a 2nd run |
| **`RTX`** | The defense group's **beta**, not its leader; `M778` put `ETN`–`RTX` at **−0.006** so the diversifier claim survives | `[measured]` | ⚠ delta −0.304 is now a **FOUR-day-old** delta. **Customer unmeasured, 207 days (`W4`)** |
| **`NUE`** | Post-earnings re-rate; FINRA **z −2.33 (covering)**; clears the surge leg (1.41), **fails rs20** ⇒ not 🟢 | `[measured]` | `S114` settles **09-03** |
| **`WMT` · `TGT`** | The Staples carriers, and they disagree — `TGT` **+0.950 🟢** vs `WMT` **−0.333 🔴**, **17.1pp intra-sector on one window (`W5`)** | `[measured]` | 🚨 **`WMT` is the G3 flipper for a 3rd run AND one of the six tag-contaminated names for a 2nd.** PREFLIGHT §1 now shows **the two defects share a cause**: it is contaminated *because* it is a mega-cap and it flips the sign *because* it is a mega-cap |
| **`GOOGL`** | Half the COMM underweight is already wrong. Not a flipper (COMM +0.108 → ex-top1 +0.022) | `[measured]` | ⚠ **`D297` still unfixed**: `GOOG` is a second **38.3%** row ⇒ the Alphabet complex is **76.6%** of COMM while `top1_w` reports half |
| **`NVDA` / `ANET` / `AVGO`** | One book theme label spanning **2–3 measured risk units** (`M837`): `NVDA` a **singleton in all three windows**, `ANET`+`AVGO` merging at 500d/750d ⇒ `label_split_across_units`, **theme cap TOO TIGHT** (`M838`, human call, `D329`) | `[measured]` | ⚠ **`NVDA` prints 08-26** — two sessions out |
| **`XOM`** | 🔴 RESOLVED — the crack-attribution **control**, and a control is not a bet | `[measured]` | Ledger `A.flow미도착` → **09-16** |
| **`NEM` / `FCX` / Copper COT** | 🔴 RESOLVED — survives as a risk, not a thesis. `S89` fired **B on exhaustion geometry** (`M779`: 246.4% of `NEM`'s rs60 sits in the last 20 sessions) | `[measured]` | **B is a price fact, not evidence of a base** |
| **Optical / interconnect cycle** | 🚨 `cycle_registry.json` has **no row** ⇒ exposure is **unmeasurable, not zero**. `LITE` +0.639 accum · `COHR` +0.158 neutral · `CIEN` −0.380 🔴 rs60 −34.0 | `[measured]` | `D250`/`M731` unfixed for a 3rd run |

---

## §2 · Scenarios — **1 scored, 1 not-yet-arrived, 0 `EXPIRED`, 0 silent skips**

### (a) The exhaustive settle table, checked against 2026-08-24

| Settle | Rows | Status |
|---|---|---|
| ≤ 2026-08-21 | `S84`–`S101`, `P65`–`P75` and all earlier | **ALL SCORED** (verified 08-23) |
| 2026-08-22 · 2026-08-23 | **none** | — |
| **2026-08-24 (today)** | **`S74`** | ★ **SCORED THIS RUN → `FIRED-C`** (b) |
| *(date-conditional)* | **`S102`** — "first close covering 2026-08-21" | **NOT-YET-ARRIVED, 7th independent pull** (c) |
| 2026-08-25 | `P79` · `S108` (⚠ premise void, settles as registered per `D242`) | armed |
| 2026-08-26 | **`NVDA` print · `P90`** · `S79` · `S101` · `S103` · `P77` · `P78` · `P80` | armed |
| 2026-08-27 | **`MRVL` print · `S115` · `S117`** · `S81` · `P83` · **Jackson Hole opens** | armed |
| 2026-08-28 | **July PCE · `S116`** · `P67` · `P81` · `S111` · `P85`–`P89` · `FRO` | armed |
| 2026-08-31 | `S92` · `S94` · `S104` · `S112` · MSCI review | armed |
| 2026-09-01 → 09-30 | `S113` · `S109` · `S105`–`S107` · `S110` · `P84` · `S114` · `S48` | armed |

**KR-owned rows** (`SCENARIOS_KR.md`, opened): earliest settle **2026-09-04** (`S67-KR`) — none past-dated.
`grep` for any row settling 08-22…08-24 across both files returned **`S74` only**.

### (b) ★★★ `S74` — SCORED `FIRED-C`, and the row reports its own frame as partly wrong

> **The KR desk handed this over at 10:1x KST today** with a branch-by-branch table (*"A 3 legs all
> unfired · B 2 candidates fail the letter · anti-signal (a) 1 candidate"*), because it does not own
> the row and the settle day had not ended. **This run is the owner. The hand-off is credited, and the
> legs below were re-pulled independently rather than copied** — same conclusion, arrived at from the
> bodies. All calls **direct, outside a sweep window**.

**Frozen observable** (unchanged): a **dated, attributable statement or action** on the IRGC's two
named conditions — (a) an end to the US naval blockade, (b) compensation for war damages —
**corroborated in ≥2 outlet BODIES**. Grade `[news]`, never `[measured]`.

| Branch | Leg | Measured today | Verdict |
|---|---|---|---|
| **A** | dated US stand-down / partial lift of the blockade | 🚫 **Opposite direction.** The US announced its **strictest-ever** sanctions round; Treasury Secretary **Bessent** published an FT op-ed calling it an *"economic D-Day"*; press conference **14:00 ET today**. Bodies: `hellenicshipping` 08-24, `dw` 08-24, `aljazeera` 08-21, `guardian` 08-24, `scmp` 08-22 | **unfired** |
| **A** | compensation framework announced | 🚫 **A demand, not a framework.** Iran's president restated the conditions on 08-21 — *"including Iranian control over Hormuz and financial compensation for the war"* (`euronews` body 08-21). No counterparty, no framework | **unfired** |
| **A** | **unconditional** Iranian reopening statement | 🚫 **Explicitly conditional.** Iran issued **special permits for SOME Iraqi tankers** (IRNA via Reuters 08-22; `aljazeera` 08-22, `hellenicshipping` 08-23 and 08-24 bodies), **number of vessels and schedule undisclosed** — while NSC Secretary **Mohsen Rezaee** said **"not a single drop of oil will be exported"** through Hormuz *"if the economic war continues"* | **unfired** |
| **B** | **formal** US refusal of the two named conditions | ⚠ **Fails the letter, not the spirit.** Sanctions escalation + *"presses China to help reopen Hormuz"* (`toi` 08-21) is a hardening, but no document or statement formally addresses and refuses the blockade-lift and compensation demands | **unfired (letter)** |
| **B** | a strike on a transiting **VLCC** | ⚠ **Fails on vessel class, measured precisely.** A transiting vessel **was** struck fatally: **MINOAN DIGNITY** (IMO 9294484), Liberia-flagged **bulk carrier**, 76,801 DWT, projectile into the engine room outbound in the **southern corridor** overnight **08-17→18**, **chief engineer killed**, UKMTO-confirmed. **AMARA** (IMO 9333280), a 186 m **products tanker**, was **boarded and seized** near Qeshm 08-17 — the first confirmed Iranian seizure since 06-22. **The VLCCs in the same report ABORTED transits; none was struck.** `SKIROS` (159k DWT) was struck by a **Ukrainian** drone at **Novorossiysk** — wrong theatre | **unfired (vessel class)** |
| **C** | neither, by 2026-08-24 | ✅ **This is what happened** | ★ **`FIRED-C`** |

**`S74` · event date 2026-08-24 · `FIRED-C` · observed: no leg of A or B met as written · threshold was:
frozen as above. Effect on the standing view: no grade change to ENRG or INDU from this row.**

🚨 **But the row does not settle silently, because its registered anti-signal (a) partially fired.**
S74 wrote: *"if a reopening happens with **no** statement on either named condition, the conditions
were never the binding variable and this row's whole framing is wrong."* **A partial reopening
happened on bilateral Iraqi diplomacy** — IRNA states the permits followed *"repeated requests by the
Iraqi government through various diplomatic channels"*, and Iraq's parliament speaker asked Ghalibaf
for *"special status"* on **08-19** in Baghdad. **Neither named condition appears anywhere in that
chain** (`M857`).
⇒ **Carried forward, unresolved and not laundered:** *the two named IRGC conditions gate the Strait
for the general fleet, but they are demonstrably NOT the binding variable for at least one
counterparty.* The mechanism S74 retired on 08-10 (the Oman track) was replaced by the conditions
frame; today shows a **third** channel — bilateral exception-granting — that neither frame covers.
★ **A successor bracket belongs to PREMORTEM, not to this stage.** Registered here as a dig (`D338`).

★ **Scale context, all `[news]`-grade and non-price**: pre-war Hormuz carried ~20% of world crude and
**>130 vessels/day**; current traffic is *"single digits"*; Iraq's oil revenue fell **$6.8bn (Feb) →
~$2.3bn (May/Jun)** with ~90% of its federal budget on oil. IRGC high-speed-craft readings rose to
**338** (08-09→16) from **209** the prior window.
⚠ **The tape's same-day read, labelled: LIVE INTRADAY PRINT, not a settled bar** — Brent **−1.3% to
$93.16**, WTI **−1.9% to $85.42** at **04:32 ET 08-24**, attributed in the body to the Iraqi-tanker
permits. **It is not in this run's `asof = 2026-08-21` frame and no stage may treat it as one.**

### (c) `S102` — not-yet-arrived, **5th consecutive US run**, and the diagnosis is now CORRECTED (not by us)

Observable: `DGS2` **and** `30y−10y` from `[FRED]`, at the **first close covering 2026-08-21**; frozen
thresholds `DGS2 ≥ 4.30` (A) / `DGS2 ≤ 4.08 ∧ 30y−10y ≥ 0.59` (B) / between (C).

**Pulled twice today by two independent paths** (`module_macro_us --json`, and a direct
`api.stlouisfed.org` call bypassing the module):

| Series | Last observation | Value |
|---|---|---|
| `DGS2` · `DGS10` · `DGS30` · `DFII10` · `DTB3` | **2026-08-20** | 4.19 · 4.69 · 5.23 · 2.35 · 3.71 |
| `T10YIE` | **2026-08-21** | 2.34 |
| `SOFR` | **2026-08-21** | 3.65 |

🚫 **The 08-20 values are NOT substituted.** (For the record only, and not as a score: `DGS2` 4.19 and
`30y−10y` **0.54** would both sit inside branch **C** — the row's own disclosed favourite. That is a
preview, not a verdict, and the next run must re-pull rather than inherit it.)

★★ **Attribution, and this is the point of §8.** The correction to `D309` — *"not the weekend; a
per-series publication lag, with the H.15 family at least one business day behind `T10YIE`"* — was
**already made by the `industry_kr` desk at ~10:00 KST today** and filed as **`M840` / `D333-KR`**.
**This run re-derived it before reading the spine tail and must not claim it.** What this run adds is
narrow and stated as such: **an independent US-side reproduction on two code paths, extending the
series list** (`DFII10` and `DTB3` also lag; `SOFR`, a NY-Fed series outside H.15, does not) — logged
as **`M858`, a reproduction**, not a discovery. **This is `R97`'s lesson applied one run later, and it
was very nearly missed again** (§8).
⇒ **Successor run: 2026-08-25** — the first business day on which the H.15 family should publish 08-21.

### (d) 🚨 `S8` — undated and unscoreable for the **23rd** consecutive run

Still `[blank]`-dated on `CATALYST_WATCH` (*"Iran 'Strait of Hormuz open' statement"*, axis=oil).
**A human must `VOID` it or re-register it with a date (P5).** This run does not fix it and only
increments the count. ★ **Today the count acquires a cost**: `S74`, the row written **because** `S8`
was unscoreable, has now settled `FIRED-C` and been retired — **so the desk's only Hormuz bracket is
once again the undated one**, on a day the Strait produced a fatality, a seizure, a partial reopening
and a sanctions round. **The gap is now open, not merely old.**

**Score this run: 1 scored (`S74` → `FIRED-C`) · 0 `EXPIRED` · 0 silent skips · 1 not-yet-arrived with
a corrected structural diagnosis and a named successor date · 1 undated and named for the 23rd time.**

---

## §3 · Both ledgers — audited symmetrically

`reject_ledger.py due` **and** `missed_ledger.py due` were both run (not `score` alone).

| Ledger | Rows | Resolved | Past due | Legacy (no revival/entry condition) |
|---|---:|---:|---:|---:|
| Rejections | **227** | 134 | **0** | **0** |
| Misses | **221** | 112 | **0** | **0** |

★ **Both clean — 0 due and 0 legacy on each, third consecutive run; legacy has now held at 0 for
13 runs**, which is a trend, not a quiet pass. Row counts rose (+2 rejections, +15 misses vs the
08-23 US reading) because the `industry_kr` run filed 2 rejections and 4 misses this morning and the
08-23 US run filed 11 misses — i.e. **both ledgers are being fed, not merely audited.**
⚠ **Sign hygiene (`3c`)**: the two `excess` columns are **inverted** relative to each other and are
**not summed** anywhere in this packet.
⚠ **`score` is accumulation, not an edge** — the miss ledger's first six rows are outcome-selected and
the script says so itself.
★ Carried and still binding (`T25`): any structural rejection this run makes must re-print the
rejection ledger's loss-asymmetry number beside it.

---

## §4 · Exposure state — carried as size context for BET/ALPHA (read-only; this stage never logs)

`exposure_rule.py state` + `show --tail 10`, both run.

- **State `정상` (normal)**, prior state normal, *"no trigger condition"*. Benchmark `069500.KS`
  **105,995**, session **−3.623%**, **−3.69%** from the 20-day high, **+20.95%** off the 20-day low,
  volume **0.729×**.
- **Target invested 95% · today's ledger row reads 85.3% ⇒ band gap 🚨 `−9.7pp`**, the narrowest of
  the last six rows (**−39.4 → −27.1 → −14.0 → −13.9 → −9.9 → −9.7pp**). The gap is closing but has
  been open for **6 consecutive rows**.
- ⚠ **`state` itself could not compute the split** (*"NAV/invested weight unavailable — account query
  failed or arguments not supplied"*). The invested % above comes from the **ledger row**, not from
  `state`. Two instruments, one number — say which, every time.
- **Cumulative decomposition, n=12**: total excess **−13.29pp = cash −5.90pp + selection −7.39pp**.
  ⚠ **n=12 is not a sign.** The script's own line: at n≈20 the sign may be asked. Also `D323`: the
  ETA is written in **calendar** days while accrual is keyed to **sessions** — n 12 → 20 is **~11
  calendar days, not 8**.
- 🚨 **`ARMED (TIMEFOLIO_EXECUTE=1)` on every row for the 10th run.** Carried as a standing flag;
  this desk neither arms nor disarms it (P5).

---

## §5 · Reconciliation — belief vs mechanical coverage

`module_report_tags show` run. **21 `industry_US` documents indexed** + `COMPANY_SCOREBOARD.md` at root.

- ★ **`D330-KR`'s remedy applied the run after it was written**: `REPORT/COMPANY_SCOREBOARD.md` was
  **opened as a body, not as a listing line.** Contents: `company_batch` run 1 (2026-08-21), **5 names,
  all KR** — 036460 `PASS` 92.5 · 011200 `PASS` 79.5 · 316140 `HOLD` 76.2 · 028050 `HOLD` 64.7 ·
  000660 `PASS` 58.8. **Overlap with today's US candidate set: 0 names.** ⇒ no US belief is
  contradicted or pre-empted by it, and that statement now rests on the body rather than the filename.
  ★ Its cross-finding is carried anyway because it is market-agnostic and this desk is exposed to the
  same error: **4 of 5 names scored `frame_integrity 0`** — the recent max leg was **sector beta, not
  the name**. The US analogue is `M779` (`NEM`) and `M803` (`LHX`), both of which found the same shape.
- **Beliefs with no ledger coverage** — `LITE` / `COHR` / `CIEN` (the optical node) still have **no
  `SECTOR_DEEP` or company file of their own**; they are carried in the standing view on sweep numbers
  alone. **4th consecutive run.** ⇒ demote or dig (dig list, §9).
- **Coverage with no standing thesis** — `SECTOR_DEEP_SEMI.md` is dated **2026-07-15** (40 days) and
  no current thesis points at it; `BOOK_THESIS.md` is **08-12** (12 days).
- **🔴RESOLVED with a live thesis** — none newly detected; `XOM` and `NEM` are both correctly filed
  🔴 with explicitly non-thesis roles.
- ⚠ **`T` remains unindexable by `module_report_tags` (`M152`)**, unchanged.

---

## §6 · ★★★ The signal scoreboard — the US ledger exists, and it inverts the KR verdict

`axis_inflection.py` → `ic_ledger.py log` → `ic_ledger.py score` — **all three run, and this time with
`--market us`.**

**`log --market us` accrued 185 new rows.** The US ledger now holds **405 rows over 33 run-dates
(2026-07-13 → 2026-08-20)** (`M853`). The KR ledger holds 509. **Total 914.**

| Axis | h | n | `n_eff` | mean IC | **t(NW)** | positive | verdict (Bonferroni \|t\|>2.8, k=15) |
|---|---|---|---|---|---|---|---|
| **`rs60`** | **5** | 27 | **5.4** | **−0.1310** | **−5.46** | **7%** | ★ **significant, passes** |
| `rs60` | 10 | 21 | 2.1 | −0.2014 | −3.87 | 10% | 🚨 `n_eff<4` — unquotable |
| **`vol_surge`** | **1** | 33 | **33.0** | **+0.0398** | **+3.40** | **67%** | ★ **significant, passes — POSITIVE** |
| `obv_norm` | 10 | 21 | 2.1 | −0.0429 | −3.03 | 38% | 🚨 `n_eff<4` — unquotable |
| `rs60` | 1 | 33 | 33.0 | −0.0635 | −2.77 | 21% | significant on a standalone bar only |
| `vol_surge` | 5 | 27 | 5.4 | +0.0119 | +0.44 | 63% | indistinguishable |
| `flow_score` | 1 | 33 | 33.0 | −0.0277 | −1.06 | 42% | indistinguishable |

**Two quotable cells (`n_eff ≥ 4` and Bonferroni-passing), and they say different things:**

1. ★★★ **`vol_surge` h=1 is POSITIVE in the US** — `IC +0.0398`, `t(NW) +3.40`, `n_eff 34.0`, **67% of
   run-days positive** (`M854`). In KR the same axis at the same horizon is `−0.0454 / −3.86 / 24%`.
   **Same axis, same horizon, both Bonferroni-passing, opposite signs.**
   ⇒ **The 🟢 gate's `vol_surge ≥ 1.2` requirement is measured to select FOR 1-day forward returns in
   the US.** Yesterday's carried hypothesis — *"if the KR-measured negative IC generalises, the gate is
   selecting against forward returns"* — **does not generalise. It inverts.** This is the cleanest
   `W1` confirmation this desk has produced: not "we declined to transfer", but "we transferred
   nothing and then measured the transfer would have been backwards."
   ⚠ **`vol_surge` h=5 in the US is `+0.0119 / t +0.44` — indistinguishable.** The positive result is
   **horizon-1 only** and must be quoted with its horizon. `D105` (agreement across two horizons) is
   **NOT** satisfied for `vol_surge` in the US.
2. ★★★ **`rs60` h=5 is the strongest cell in either market's ledger, and it is NEGATIVE** —
   `IC −0.1310`, **`t(NW) −5.46`**, **7% of run-days positive**, `n_eff 5.4` (`M855`). h=1 carries the
   same sign (`−0.0635 / −2.77`, standalone-significant). **`D105` IS satisfied here** — two horizons,
   same sign, and the axis set with a consistent sign across ≥2 horizons is
   `['flow_score','obv_norm','rs20','rs60']`.
   ⇒ **In this window, high 60-day relative strength — the sweep's `rs60`, measured against `SPY`
   (benchmark named inline, `C1`) — ranks AGAINST 1–5-session forward returns in the US top-300.**
   `rs20` and `rs60` are two of the sweep's four surviving axes.

**⚠ Constraints that bind every citation of the two cells above:**
- **Regime label required.** The 33 US run-dates span **2026-07-13 → 2026-08-20**, a window containing
  the mid-August drawdown. **A mean-reversion result measured across a drawdown does not generalise to
  a trending tape**, and `rs60`'s −5.46 is exactly the shape a drawdown produces.
- **`n_eff 5.4` is above the bar but only just.** The h=10 rows (`rs60 −0.2014 / t −3.87`) look even
  stronger and are **unquotable** at `n_eff 2.1` — the same trap that produced the fake `t=+6.7` on
  2026-07-31. Do not reach for them.
- **This is a ranking-level measurement, not a position-level one.** It says the sweep's ordering has
  a sign; it does not say any single name will do anything.
- 🚫 **No axis is flipped, killed or re-weighted by this stage.** Code changes are a human call (P5).
  What changes today is that **the US arm of `C15` now has a number where yesterday it had a `W1`
  block**, and the number does not agree with the KR arm. **`C15` stays open and gets wider, not
  narrower** — which is what §6 of the spine is for.

---

## §7 · 🚨 `R98` — the retraction this run files against its own predecessor

**The claim.** The 2026-08-23 `industry_US` HANDOVER §6 wrote: *"**0 new rows accrued (729 rows,
`market=kr`)** … The ledger is `market=kr`. Importing a KR-measured axis IC into the US sweep is
exactly the `W1` violation this repo keeps logging … **The threshold cleared in KR; the US desk has no
equivalent measurement and therefore no verdict.**"*

**What killed it.** `scripts/ic_ledger.py:336` — `p.add_argument("--market", choices=["kr","us"],
**default="kr"**)`, on **all three** subcommands, and `carryover.md` §3e prints the command block
**without the flag**. So `ic_ledger.py score` run by a US desk silently returns the KR table.

**Two separate errors, both arithmetic and both checkable at the time:**

| Written 08-23 | Measured 08-24 |
|---|---|
| *"729 rows, `market=kr`"* | **729 was the whole file.** Today: **509 kr + 405 us = 914**, of which **185 were accrued by this run** ⇒ **729 − 509 = 220 US rows were already on disk on 08-23** |
| *"the US desk has **no equivalent measurement**"* | Those **220 rows** are ~15 US run-dates × 15 (axis × horizon) cells — **enough for an h=1 verdict at n≈15.** The measurement existed; it was one CLI flag away |
| *(implied)* *"if the KR sign generalises, the gate selects against forward returns"* | **The sign does not generalise. `vol_surge` h=1 is `+3.40` in the US against `−3.86` in KR** (`M854`) |

**What survives, and it is most of it.** The `W1` refusal itself was **right** — importing the KR IC
would have been a violation, and today's US measurement proves it would also have been **wrong in
direction**. What is retracted is the *"no equivalent measurement"* clause and the row count, not the
discipline that produced them.
⚠ **The exact pre-accrual date coverage of those 220 rows cannot be reconstructed** — the ledger is
append-only with no vintage column, so which `(run_date, axis, horizon)` cells predated today's `log`
is not recoverable. **Stated as unrecoverable rather than estimated** (P4).
⇒ **Positive-form remedy → `D336`.**

---

## §8 · What this run asserted and then refuted — written down, not edited away (`§4c`, `D48`)

1. 🚨🚨 **This run re-derived `D333-KR` and was one step from filing it as new.** After the FRED pull
   returned `DGS2` @ 08-20 while `T10YIE` and `SOFR` carried 08-21, this stage drafted the finding as
   a **correction of `D309`** — the exact sentence the `industry_kr` desk had already written at
   **~10:00 KST this morning** as `M840` / `D333-KR`, twelve hours earlier, in a file this stage was
   required to read. **It was caught by reading the spine tail, not by suspecting itself.**
   **The draft is not edited away; it is recorded here, and the finding is downgraded to a
   reproduction (`M858`).** ⇒ This is **`R97` / `D330-KR`'s class, one run later, in the other
   market** — and it argues the remedy should not stop at `COMPANY_SCOREBOARD.md`. ⇒ **`D337`.**
2. ⚠ **This stage began by trusting `ic_ledger.py score`'s bare invocation** — the same call the prior
   run made — and only checked `--market` after the KR table's header (`# IC LEDGER — KR`) was read
   against a US run. **The header said `KR` on 08-23 too.** A label that states the defect and is read
   past is not a working guard; the guard was the arithmetic (509 ≠ 729), not the banner.
3. ⚠ **PREFLIGHT §1's "the bucket is arbitrary" language, inherited from two runs, was refuted inside
   this run's own stage −1** — positions `[0…48]`, contiguous, 49/49 identical to yesterday. Recorded
   there as a retraction rather than a silent edit; repeated here because the downstream consequence
   (69.0% of market cap, not 16.4% of anything that matters) binds ROTATION and SWEEP.

★ **Three self-refutations, two of them against claims this desk published under its own name.**
A run reporting zero would mean its controls were not adversarial.

---

## §9 · Stale flags, digs registered, and the dig list ranked for today

**Stale flags (`asof` older than this run's horizon):**

| Item | `asof` | Age | Consequence |
|---|---|---|---|
| `us_top300.csv` | 2026-07-15 | **40 days** | No cap-weighted claim may rest on it (PREFLIGHT G5). ★ **And it now decides bucket membership** (§0) |
| `us_all_v2_candidate.csv` | 2026-08-10 | **14 days unpromoted** | Human call |
| `SECTOR_DEEP_SEMI.md` | 2026-07-15 | 40 days | Coverage without a live thesis (§5) |
| `BOOK_THESIS.md` | 2026-08-12 | 12 days | — |
| MPC FY2025 **10-K Item 1A** | never opened | **2nd run** | The document carrying refining margin risk factors |
| `RTX` customer identification | — | **207 days** | `W4` unmet on a held name |
| `cycle_registry.json` optical row | missing | 3rd run | Exposure **unmeasurable, not zero** |

**Cleared suspensions converted to digs:** none cleared this run (`S102`'s clearing date moved to
**08-25** by the corrected `D333-KR` diagnosis, so it is a dated dig, not a cleared suspension).

**Digs registered by this run** (3-grep at WRITE time across `handoff/*.md`, `llm_outputs/**`,
`REPORT/**` — `R98` **0 hit**, `M853`–`M858` **0 hit**, `D336`–`D338` **0 hit**; current highest
`R97` / `M852` / `D329` (US) + `D335-KR`):

| id | Finding | Positive-form remedy |
|---|---|---|
| **`D336`** | 🚨 **`ic_ledger.py` defaults `--market kr` on all three subcommands, and `carryover.md` §3e prints the commands without the flag — so a US desk that follows the protocol literally is handed the KR ledger, with only a header line to notice it by.** Cost measured: **one run** concluded *"the US desk has no equivalent measurement"* while **220 US rows** sat in the same file (`R98`), and the KR number it deferred to has **the opposite sign** (`M854`) | **① Make `--market` a REQUIRED argument on `log`/`score`/`show` (no default). ② Have `carryover.md` §3e write `--market {us\|kr}` into all three command lines. ③ Print `rows(market) / rows(file)` in the header so a mismatch is arithmetic, not typographic.** (human approval: CLI signature) |
| **`D337`** | 🚨 **`R97`'s remedy is scoped to one filename, and the same failure recurred one run later on a different object.** `D330-KR` prescribed *"open `COMPANY_SCOREBOARD.md`'s body"*; today this desk nearly filed **`D333-KR`**, written 12 hours earlier by the sibling desk **inside a file HANDOVER is already required to read**. The class is not "that report" — it is **"a finding published since the last run, in the shared spine, by the other market"** | **Add to `carryover.md` §1: before writing any finding, `grep` the spine's newest block (the tail append of `STANDING_VIEW.md` / `RESEARCH.md` Part C) for the object being claimed, and cite it as a reproduction if it is there.** A one-line mechanical check on the file already open |
| **`D338`** | ★★★ **`S74` settled `FIRED-C` while its own anti-signal (a) fired — the Strait has a THIRD channel neither the Oman frame (retired 08-10) nor the two-conditions frame covers: bilateral exception-granting.** Measured: Iran granted transit permits to some Iraqi tankers on **repeated Iraqi diplomatic requests** (IRNA 08-22, ≥3 bodies), with **neither named condition mentioned anywhere in the chain**, while simultaneously threatening a total halt (`M857`). **The desk's only remaining Hormuz bracket is now the undated `S8`** (23rd run) | **Register a successor bracket at PREMORTEM keyed to the exception channel** — observable: *counterparty-specific transit permits granted or revoked, ≥2 bodies*, with branches on **widening** (more counterparties ⇒ de-facto reopening without any condition being met) vs **revocation**. Both-sided, thresholds set outside the implied move, per standing practice |

**Dig list ranked for today (candidate DEEP / stage assignments):**

1. **`D336`** — cheapest of the three and it unblocks §6 permanently. *(no DEEP slot needed)*
2. **`D338`** → **PREMORTEM**, and it is the run's only genuinely open forward object.
3. **MPC FY2025 10-K Item 1A** → **ENRG DEEP** (2nd run unopened; `M831`/`M833`'s contradiction —
   +106.7% YoY R&M margin on **lower** utilisation, attributed by the issuer to *conflict-driven
   supply disruption* — cannot be resolved without the risk-factor text).
4. **The optical/interconnect `cycle_registry.json` row** (`D250`/`M731`) → whichever stage owns
   `CYCLE_EXPOSURE`; 4th run with three names carried on sweep numbers and no file.
5. **`D297`** (Alphabet double-count: `GOOGL` 38.3% + `GOOG` 38.3% = **76.6%** of COMM while `top1_w`
   reports half) → **ROTATION**, because it silently halves a flipper test.
6. **`D325`** (`breadth` is the 🟢 rate, not breadth) → **SWEEP/ROTATION**; the KR desk measured the
   US-side gap's KR analogue at **+26.4pp** (`D332-KR`). ★ **And §6 changes its weight for the US
   desk**: the gatekeeper `vol_surge` is **positive** here, so the US `breadth` field is mis-*named*
   but not obviously mis-*signed* — the KR argument for distrusting it does not carry over (`W1`).

---

## §10 · RESEARCH triggers loaded as binding constraints — which group binds which stage

Loaded from `handoff/RESEARCH.md` as constraints, not as a summary. **Group → the stages it binds in
THIS protocol:**

| Group | Fires when | IDs | Binds, this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · **C4 "indistinguishable"** · **C5 arbitrary choice** | **MACRO · every stage.** ★ Hot today: **C4** on the exposure split (n=12 is not a sign) and on `vol_surge` h=5 (`t +0.44`); **C5** on `risk_units` `dist 0.65` (0.40–0.60 all give 12 units) and on the sweep's own `--days` |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · **S4 in-sample ≠ done** · **S5 short samples** · S6 future labels | **§6 above, and any stage citing it.** ★ **S5 is the binding one**: `rs60` h=10 (`n_eff 2.1`) is unquotable however good it looks; `risk_units` 250d runs on **n=249** and warns so itself |
| **D** | you read data | D1 second venue · **D2 proxy sign** · **D3 signed vs unsigned** · **D4 regime contamination** · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · L2 indicators / money_trail.** ★ **D4** binds §6's regime label; **D3** binds any COT citation (`D327`: a "crowded long" label on a **net −10,560 short**); **D6** binds every `obv_norm` sentence |
| **W** | you write a conclusion | **W1 cross-market transfer** · W2 inherited lead/lag · W3 real ≠ profitable · **W4 name the customers** · **W5 sub-sector dispersion** · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ **W1 is the run's headline constraint and today it has a price tag** (§6/§7); **W4** is unmet on `RTX` for 207 days; **W5** is live on Staples (`TGT` vs `WMT` **17.1pp**) and on Health Care |
| **L** | lenses, not triggers | L1 second derivative · **L2 peak-margin trap** · **L3 branch information content** | **DEEP · PREMORTEM.** ★ **L2** is the standing frame on the refiners and `M831` closed its escape hatch; **L3** governs `D338`'s successor bracket |

⚠ **Loaded as binding constraints.** Measured 2026-07-22: three of six reversals in one session broke
rules that already existed, written as prose in a folder referenced zero times.

---

## §11 · Write-back plan (executed at run end, not now)

Per the stage spec, `handoff/*.md` is updated **at run end**, append-only for retractions:
- `STANDING_VIEW.md` §5 ← **`R98`** with the measurement that killed it (§7).
- `STANDING_VIEW.md` §6 ← **`C15` annotated** with its US arm (`M854`) — **annotated, not resolved**;
  the contradiction widens rather than closes.
- `STANDING_VIEW_US.md` §2 ← **`M853`–`M858`**.
- `SCENARIOS.md` MASTER scoring log ← **`S74` · 2026-08-24 · `FIRED-C`** with the observed values and
  the anti-signal note; `SCENARIOS_US.md` ← the same, annotated in place (thresholds untouched).
- `RESEARCH.md` Part C ← **`D336`–`D338`**.
- asof chain ← this run's entry.
**No scenario is registered by this stage** (registration belongs to PREMORTEM / ALPHA).

---

*Inheritance only. No position sizing, no buy/sell language, no grade change anywhere in this packet (P4).*
