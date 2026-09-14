# BLINDSPOT_PREMORTEM — industry_US · 2026-09-05 (Sat) · Stage 7 / L1·PREMORTEM ★US-only

> Four adversarial lenses argue **AGAINST this run's own tilt**, before the deep budget is committed.
> Born from the 2026-07-14 postmortem: bank leg missed · cool-CPI semi rip missed · "already ran"
> names wrongly avoided · zero exposure to the #1 cycle's epicenter.
> **Analytical output only — no sizing, no buy/sell language (P4).**

## ⚠ Execution mode, declared first

**The four lenses were run IN-CONTEXT and serially, not as parallel adversarial agent fan-outs.**
This is a standing session constraint and it is the same one the KR desk has declared for nine
consecutive runs and the US desk for several. It is stated here rather than buried: an in-context
lens shares the author's priors by construction, which is exactly what the fan-out exists to break.
**Treat every "the lens found X" below as weaker evidence than the same sentence from a fan-out.**

## §0 · The draft tilt being attacked

`ENRG OW+ · HLTH OW · MATR N · IT N · STPL UW · UTIL UW · RE UW · FIN N · DISC UW · INDU UW− ·
COMM no-verdict` — with **3 deltas issued today** (`ENRG OW→OW+`, `FIN UW→N`, `STPL N→UW`) and
**DEEP filled 2 of 4** (continuous `ENRG`, `HLTH`; both rotating slots empty, offered here).

## §0b · 🚨 The dated binaries, and the instrument that CANNOT price them

`CATALYST_WATCH.json` (`--days 10`): **3 binaries in window.**

| catalyst | date | D− | source | ≤48h? |
|---|---|---|---|:--:|
| **August PPI** | **2026-09-10** | D−5 | `bls✓` official | no |
| **August CPI** | **2026-09-11** | D−6 | `bls~est` | no |
| Iran *"Strait of Hormuz open"* statement (TACO trigger) | **undated** | — | `news👁` | undated |

⇒ **The protocol's mandatory ≤48h both-sides rule is NOT triggered** (today is Saturday; the nearest
binary is five sessions out). It is stated rather than assumed, and **both dated binaries are
bracketed both ways anyway** (§Lens 2).
🚨 **And `D507` binds every window below: 2026-09-07 is Labor Day and the calendar does not carry
it.** Every N-session window here is counted in **settled sessions**, so a "5-session" bracket from
the 09-04 close settles **09-14, not 09-11**.

### 🚨 The implied-move instrument is unusable for these binaries, and that is measured, not assumed

`module_flow --positioning`, run this stage:

| ticker | implied move | expiry | tag |
|---|---:|---|---|
| `SPY` | **±0.5%** | **2026-09-08 (D3)** | P/C 0.85 · skew +19.0 |
| `SMH` | **±1.8%** | **2026-09-08 (D3)** | **P/C 4.24** · skew +9.4 |
| `XLE` | **±1.6%** | **2026-09-09 (D4)** | P/C 1.43 · skew +1.4 |

★ **`M1305` [measured] — every available straddle EXPIRES BEFORE both binaries.** PPI is 09-10 and
CPI is 09-11; the nearest expiries are 09-08 and 09-09. ⇒ **these are not event-priced, and any
threshold taken from them would be fabricated.** This is `M47`'s exact shape reproduced
(*"META ±4.4% · MSFT ±2.9% · VLO ±3.2% all expire 07-24, BEFORE their 07-29/07-30 events"*).
⇒ **Every bracket registered below takes its threshold from `D93` measured dispersion instead**, and
each says so on its own line. **No threshold in this file is presented as "outside the implied move"
because no implied move covers the event.**
⚠ **One number from that table is used, and only as evidence, not as a threshold**: `SMH`'s
**put/call OI = 4.24** — a heavy protective-put load — which is direct support for the *hedging*
reading of the 09-04 short-volume spike (`P137`'s branch A) and against the *distribution* reading.

---

# LENS 1 — UNDER-COMPUTED LEGS

*"What is the strongest bull case for a sector or sub-leg we did NOT deep-dive that has a catalyst
≤~5 trading days?"*

| leg | catalyst ≤5 sessions | the strongest case AGAINST our not covering it | verdict |
|---|---|---|---|
| **IT** (`N`, declined 5 consecutive runs) | **`S140` 09-08** · PPI 09-10 · CPI 09-11 | 🚨 **The sector's own bracket settled TODAY and inverted the thesis the desk has been carrying.** `P101` `FIRED-C` with software **−4.46%** vs hardware **+2.05%** over 5 sessions and participation **21.1% vs 73.0%** — `M1251`'s "IT's weak half is semicap/test" is **dated**. Meanwhile `eqflow` improved rank **10 → 5** and the board's **three largest Δflows are all inside IT** (`STX` +0.728, `WDC` +0.718, `AMD` +0.566). ROTATION declined the demotion *and* has no slot to examine the promotion. **The desk is carrying a stale sub-sector map on its largest book concentration.** | ★ **PROMOTE-TO-DEEP** |
| **UTIL / the AI-power lane** (`UW`, declined 5 consecutive runs) | **`P123` 09-08** · `P122` 09-08 | 🚨 **The lane spans three GICS labels, so no sector verdict can express it, and the book is on the wrong side of the split.** `VST` Δ **+0.491**, `CEG` +0.644 flow OBV 매집, `VRT` Δ **+0.444** — all accumulating — while the book's **only** AI-power holding `ETN` is **🔴분산 −0.662** with the lane's worst rs20 (−8.0). `D416` (the AI-power cycle has no registry row) is **unbuilt** and this is the second consecutive run where it costs a live question. UW sectors do not take rotation slots **by rule**, which is exactly what a PREMORTEM promotion is for | ★ **PROMOTE-TO-DEEP** |
| **MATR** (`N`) | **`P102` 09-09** | `eqflow` has deteriorated three runs running (+0.030 → −0.076 → **−0.107**) and `exc20` median is **−2.99**, yet copper spec sits at the **100th COT percentile for a 5th run** (`C24`, 6th run carried). The bull case against us: **if `P102` fires branch A, the two-name concentration extends and the desk's `N` is under-weighting a live momentum trade.** ⚠ But `P102` settles in **two sessions** and a DEEP four days before its own bracket would pre-empt it | **WITHIN-RUN-WATCH** — resolves 09-09, no slot |
| **INDU** (`UW−`, last DEEP 08-27 = 6 runs) | CPI 09-11 (capital-goods pricing) | **The board's largest positive Δflow (+0.082) sits on the board's worst sector**, and ROTATION declined the promotion because the Δ decomposes to four names (`VRT` +0.444, `NSC` +0.403, `GWW` +0.352, `CAT` +0.352). ⚠ **The adversarial reading is that "four names" is how a turn starts** — and two of the four (`VRT`, `NSC`) are in threads EVENT_ALPHA carded (AI-power, diesel/freight). `S126` settled `FIRED-C`, i.e. the bracket bought nothing | **WITHIN-RUN-WATCH** — no slot; named in DEEP_LOG |
| **RE** (`UW`, last DEEP 08-26 = **7 runs, the board's longest gap for a 2nd run**) | CPI 09-11 · `S135` 09-11 | **11 of 12 negative on `exc5`, 0🟢, breadth 0.00** — the most internally consistent bucket on the board. The bull case against us is the **cool-CPI branch**: RE is the purest duration proxy and the 2026-07-14 postmortem's own named miss was a **cool-CPI rip the desk sat out**. ⚠ `S135` already brackets it as one of three | **WITHIN-RUN-WATCH** — bracketed by `S135`; the 7-run gap is logged, not fixed |
| **STPL** (`UW`, demoted **today**, last DEEP 08-27 = 6 runs) | CPI 09-11 · `S135` 09-11 | A demotion issued on `eqflow` −0.098 / breadth 0.00 / 0🟢-7🔴, **four sessions before the print that most directly tests it**. The adversarial case: the demotion is a **rate call wearing a flow label**, and `S135` will answer it | **WITHIN-RUN-WATCH** — `S135`, 09-11 |

★ **`M1306` [measured] — the two promotions exactly fill the two rotating slots ROTATION could not
fill, and neither is an OW sector.** DEEP goes **2/4 → 4/4** through the PREMORTEM path rather than
through padding. ⚠ This is the **second consecutive run** that reached its budget only this way
(09-02 also promoted `IT` and `UTIL`), which is evidence for `M1304`'s question — *does the US desk's
N=4 fit its board?* — and is recorded as such rather than celebrated.

---

# LENS 2 — REGIME-FLIP / BOTH-SIDES

*"For each known binary, what is the AGAINST-US branch: what rips, which of our OWs gets hit, with a
trigger and an invalidation?"*

### Binary 1 — **August PPI, 2026-09-10** (`bls✓`, D−5)

| | |
|---|---|
| **Our tilt into it** | `ENRG OW+` (promoted today), `INDU UW−`, `STPL UW` (demoted today) |
| **AGAINST-US branch = a HOT PPI** | Producer prices confirm the energy/diesel pass-through ⇒ this **confirms** `ENRG OW+` and **also** hits `INDU`/`STPL` margins, i.e. it confirms three verdicts at once |
| **AGAINST-US branch = a COOL PPI** | The diesel/crack story is **not** reaching producer prices ⇒ the `P136` transmission has no macro leg, and the `ENRG OW+` promotion issued today rests on flow alone |
| ⚠ **Information grading (`B4`)** | 🚨 **Neither branch changes the conclusion, and this is stated rather than bracketed.** A hot print confirms; a cool print is absorbed by `P136`'s existing kill condition. **No new bracket is spent on PPI.** Existing coverage: `S130` (09-10), `P127` (09-10), and the windows of `P136`/`S146`/`S147` all contain it |

### Binary 2 — **August CPI, 2026-09-11** (`bls~est`, D−6) — the one that matters

| | |
|---|---|
| **Our tilt into it** | Nominal yields at the **96th–99th percentile**, `hy_oas` at the **2.0th**, `vix` at the **2.4th** (`M1286`); UW on **RE / STPL** and `UTIL UW`; `FIN` promoted to `N` **today** |
| ★ **AGAINST-US branch = a COOL CPI** | **This is the desk's own named historical miss.** Yields fall ⇒ the three duration proxies (`RE`, `STPL`, `UTIL`) rip **together**, and the desk is UW all three. **What rips**: `XLRE`, `XLP`, `XLU`, plus the long-duration software the desk has watched de-rate (`ADSK` −16.4, `CDNS` −14.0, `SNPS` −11.0 over 5 sessions). **Which OW gets hit**: `ENRG OW+` — a cool print takes the inflation bid out of the barrel. **Trigger**: `^TYX − ^FVX` steepens ≥ +4.40 bp (= `P138` branch A). **Invalidation**: it bear-flattens ≤ −5.97 bp (`P138` branch B) |
| **AGAINST-US branch = a HOT CPI** | Hike odds — already *"briefly above 50%"* on the payroll print (`M1289`) — reprice up. **What rips**: `FIN` (the promotion issued today), and the crowded **UST 10Y spec short at the 9th percentile** (`M1294`) becomes **rebound ammunition** rather than fuel. **What gets hit**: the desk's `HLTH OW` (a duration-sensitive bucket) and the storage/memory node EVENT_ALPHA just carded |
| **Information grading (`B4`)** | ✅ **Both branches can falsify.** A cool print falsifies three UW verdicts at once; a hot print falsifies the `HLTH OW` and puts the `FIN N` promotion on the right side for the wrong reason. **Worth bracketing** |
| **Existing both-sides coverage** | `P137` (SMH, settles 09-11, both branches) · **`P138`** (curve shape, settles 09-11, both branches, registered by MACRO this run **because of** this exact ambiguity) · `S135` (UTIL/RE/STPL, 09-11) · `S142` (FIN, 09-11) · `S125` (09-11). ⇒ **the CPI is bracketed both ways on five independent observables.** No sixth is registered — that would be padding |

🚨 **`S142`'s premise inverted inside its own window, and the correct response is an ANNEX, not a
re-band.** `S142` was registered 09-02 as *"the against-us branch of the **FIN UW** issued today"*.
**Today ROTATION moved `FIN UW → N`.** ⇒ **`S142-ANNEX` registered** (§Registrations): the frozen
observable and threshold are **untouched** (`D242`), and the annex records only that **the verdict
the row was written to attack no longer exists**, so its branch labels must be read against the
09-02 verdict, not today's. **The row is still scored on 09-11 exactly as frozen.**

### Binary 3 — **Hormuz "open" statement (undated)**

**The against-us branch is a single sentence and it hits the run's newest promotion.** `ENRG OW+`
was issued today; a credible Hormuz-open statement collapses the war premium in the barrel and,
through it, the distillate crack that EVENT_ALPHA Card 1 rests on. ⇒ **already in `P136`'s VOID
clause**, explicitly named. **No date exists and none is invented** — written as `[blank]`, per the
schedule rule.
⚠ **And Card 1 named a SECOND kill condition that no bracket covers**: *"U.S. diesel price soars to
more than four-year high **as Trump ramps up pressure on refiners**"* [seekingalpha 09-01]. A US
policy action against refiner margins is **not** in `P136`'s VOID clause (which names OPEC+/SPR/
Hormuz). **This lens does not add it retroactively** (`D242`) — it records the gap, and `S147`
(below) is written with it in view.

### ⚠ The correlated-UW check (the 2026-07-15 field note)

**`RE` + `STPL` + `UTIL` are one bet in disguise, and the desk has three UW labels on it.** All three
are duration proxies against a rate complex at the 96th–99th percentile; all three have breadth
**0.00**; **none** has a single green. ⇒ **The desk's UW count over-states its diversification: it is
one macro position wearing three sector names.** `S135` (09-11) is exactly this bracket and it is
already armed — **stated so the count is not mistaken for conviction breadth.**
★ **And it now extends to a fourth**: today's **`STPL N→UW`** demotion increased the count on the
same single bet. ROTATION carried it on `eqflow`/breadth rather than on rates, which is the right
form — but **the position it produced is correlated with two the desk already had.**

---

# LENS 3 — MOMENTUM-CONTINUATION *("already ran" ≠ avoid)*

Every name with `rs60 ≥ +20` **or** `rs20 ≥ +25` vs `SPY`, re-tagged with its flip condition.
⚠ **`D6` binds**: OBV is C-grade and carries nothing alone; each tag below pairs it with RS, Δflow
and, where available, `[FINRA]` z.

| name | rs20 / rs60 | flow · Δ · OBV · surge | re-tag | flip condition |
|---|---|---|---|---|
| **`MPC`** (held) | **+30.8 / +41.5** | +0.694 🟡 · 0.000 · **+0.621 매집** · 1.05 | ★ **EXTENDED-BUT-LIVE** — the cycle KPI (distillate crack **95.6th pctile**, dist−gas spread **98.4th**) is still at an extreme, and it carries the **strongest OBV in the entire Energy chain** | distillate−gasoline spread < its 50th percentile, **or** OBV leaves 매집 |
| **`PSX`** (held) | +25.5 / +34.2 | +0.750 🟡 · +0.028 · +0.434 매집 · 1.15 | **EXTENDED-BUT-LIVE** | same |
| `VLO` | +24.7 / +37.5 | +0.700 🟡 · +0.044 · +0.482 매집 · 1.06 | **EXTENDED-BUT-LIVE** ⚠ standing rejection `H.밸류소진` (price above consensus mean target) — the `L2` peak-margin lens is loaded here | same, **or** the rejection's own revival leg |
| **`CRM`** | **+34.9** / **+45.5** | +0.728 🟡 · **−0.189** · +0.282 매집 · 1.11 | ⚠ **turning** — the board's best RS pair with a **negative** Δ. Not EXHAUSTED, not confirmed | Δ negative for a 2nd consecutive session ⇒ EXHAUSTED. ⚠ standing rejection, revives 09-30 |
| **`MSTR`** | **+43.2** / +17.6 | +0.756 🟡 · −0.005 · +0.326 매집 · 1.16 | **EXTENDED-BUT-LIVE** — flat Δ, accumulating OBV, and it is a **bitcoin proxy** whose underlying *"$80,000 breakout just failed after a blowout jobs report"* [8 outlets, 09-04] | BTC loses $78k (the level the thread itself names), **or** OBV leaves 매집. ⚠ standing rejection `L.vehicle없음`, recheck 09-22 |
| **`SNDK`** | **+43.9** / −0.3 | +0.633 🟡 · +0.061 · +0.351 매집 · 0.94 | ★ **EXTENDED-BUT-LIVE** — **+17.17% over 5 sessions, the best name in `P101`'s winning leg**, on a **negative** rs60 (i.e. the run is 20 days old, not 60) | rs60 fails to turn positive by 09-19, **or** the memory thread's bearish direction body-read is confirmed by a price break |
| **`HOOD`** | +31.3 / +35.2 | +0.783 🟢 · +0.039 · +0.215 매집 · 1.21 | **EXTENDED-BUT-LIVE** — new-🟢 ignition this session, ✅ low-short (z −0.64) | OBV leaves 매집 |
| **`DELL`** | +15.9 / **+35.6** | **+1.000 🟢** · **0.000** · +0.252 매집 · **2.48** | ⚠ **EXTENDED — flag on the tag.** It is the board's #1 flow score and its **Δ is exactly zero**; it passed the 🟢 gate on **`vol_surge` 2.48**, the axis under `C29`. **The score is a level, not a change** | Δ turns negative, **or** surge < 1.2 (which would drop the tag without any price move) |
| **`NEM`** | +13.8 / +31.9 | +0.711 🟡 · **−0.072** · +0.144 매집 · 1.14 | **turning** — gold, and `GLD` was a 09-04 laggard (**−0.84%**) | Δ negative a 2nd session |
| **`ANET`** (held) | +3.1 / **+21.5** | +0.047 🟡 · **+0.404** · +0.067 중립 · **0.60** | ⚠ **the inverse case: Δ is 6th-best on the board while the level is flat and OBV is NEUTRAL.** Not a runner — a **potential** turn | OBV must reach 매집; surge 0.60 means the 🟢 gate cannot fire regardless |
| **`PLTR`** | +1.7 / **+27.7** | −0.074 🟡 · **−0.557** · −0.008 중립 · 0.77 | ★ **EXHAUSTED** — board's **2nd-worst Δ**, flat OBV, and it sits in the software leg `P101` measured at **−4.46%** | Δ positive two sessions running |
| **`PANW`** | −8.0 / **+20.4** | −0.483 🔴 · +0.006 · −0.194 분산 · 1.33 | ★ **EXHAUSTED** — 🔴분산 with rs20 **−8.0**; **−10.32% over 5 sessions**, one of `P101`'s five drag names | OBV returns to 매집 |
| `MDT` · `DE` · `CTVA` | +8.4/+11.2 · +12.1/+17.7 · +14.8/+11.8 | all 🟢 · Δ +0.02~+0.05 · all 매집 · surge 1.35–1.47 | **EXTENDED-BUT-LIVE** — the three 🟢 with genuine surge **and** OBV **and** positive Δ; the cleanest tags on the board | OBV leaves 매집 |

★ **`M1307` [measured] — the "already ran" cohort splits cleanly along the `P101` fault line, not
along how far it ran.** Every EXHAUSTED name (`PLTR`, `PANW`) is in the **software** leg; every
EXTENDED-BUT-LIVE name with an accelerating cycle KPI is in **refining** or **storage/memory** — the
hardware leg. ⇒ **the 2026-07-14 postmortem's "already ran ≠ avoid" lesson holds, and today the
discriminator is a leg, not a magnitude.**

---

# LENS 4 — CYCLE-EXPOSURE (registry × coverage × the REAL book)

`CYCLE_EXPOSURE.md`, real KIS account, 2026-09-05: total ≈ **$11,022**, invested **$5,255**
(**52.3% cash**).

| cycle | rank | epicenter % | bar | held epicenter | GAP |
|---|---|---:|---:|---|---|
| AI-compute / semiconductors | 1 | **17.48%** | ≥12% | `NVDA`, `ANET` | ✅ |
| Energy / oil-refining | 2 | **10.47%** | ≥8% | `MPC`, `PSX` | ✅ |
| Missile-defense / rearmament | 3 | 3.64% | — | `RTX` | ⚪ no bar set |

**✅ The deterministic GAP flag is clean: no rank≤2 cycle lacks a core.** But the lens's job is the
**epicenter vs one-layer-off audit**, and three things fail it:

1. 🚨 **`M1308` — the AI-POWER cycle is not in the registry at all, and the desk's one holding in it
   is the lane's worst name.** `D416` has asked for this row for weeks. The lane is measurable and
   coherent — `VST` Δ **+0.491**, `CEG` +0.644 flow / OBV 매집, `VRT` Δ **+0.444**, all accumulating
   — and the book's exposure to it is **`ETN`, 🔴분산 −0.662, rs20 −8.0, the lane's only distributing
   name.** ⇒ **This is not a GAP by the registry's arithmetic and it IS a gap by the lens's
   question.** The registry cannot flag a cycle it does not contain. **Handed to BET's
   epicenter-starter module as a named structural gap, and bracketed as `S146`.**
2. ⚠ **`M1309` — the rank-1 cycle's held epicenter is on the wrong side of its own node's flow.**
   `NVDA` is **OBV −0.084 분산**, flow −0.032, and `ANET` is **OBV +0.067 중립** with `vol_surge`
   0.60. Meanwhile the node that actually moved — storage/memory (`STX` Δ +0.728, `WDC` +0.718,
   `SNDK` rs20 +43.9, `MU` OBV 매집) — is **0% of the book**. ⇒ **17.48% of "AI-compute epicenter"
   exposure is entirely in the half of the cycle that is not accumulating.** The registry counts the
   label; the flow object counts the node.
3. ⚠ **`M1310` — the rank-2 cycle's exposure is correctly placed, and it is the only one that is.**
   `MPC`+`PSX` are the highest-OBV names in the entire Energy chain (+0.621, +0.434) with rs20
   +30.8/+25.5, and the cycle's KPI (distillate crack 95.6th pctile, dist−gas 98.4th) is at an
   extreme. ✅ **Stated because a lens that only finds problems is not adversarial, it is
   pessimistic.**

⚠ **Concentration guard, with its window on the same line (`G4`):** the book's measured risk units
are **12 at `--days 250` · 11 at 500 · 10 at 750**, membership differs, and at 500/750d
**`ANET`+`ETN` merge into ONE unit spanning two book theme labels** — so `MAX_THEME_PCT` counts one
risk as two. **No single-number concentration claim is made here.**

---

# §Registrations — three brackets + one annex

> All thresholds from **`D93` measured trailing-252 dispersion**, executed BEFORE freezing.
> 🚫 **None is stated against an implied move, because no straddle covers the binaries** (`M1305`).
> All windows in **settled sessions** (Labor Day 09-07, `D507`).

### `S145` — ★★★ Does the LOW-`vol_surge` sub-node lead its own sector? (the desk's first US-market read on the axis `C29` is about)

**Why it exists.** The board's three largest Δflows — `STX` **+0.728**, `WDC` **+0.718**,
`AMD` **+0.566** — all print **`vol_surge` 0.59–0.68** and are therefore **structurally excluded from
the 🟢 tag**, while the node's one 🟢 (`DELL`) passed on **surge 2.48** with a Δ of exactly **0.000**.
The KR `ic_ledger` scores `vol_surge` h=1 at **IC −0.0414 · t(NW) −3.61 · n_eff 45**, clearing
Bonferroni for a third run with a **NEGATIVE** sign, while `sector_flow`'s gate weights it
**positively**. `W1` bars importing that verdict; **it does not bar running the measurement here**,
and `D395`/`D428` have asked for a US-market read for weeks.

| | |
|---|---|
| **Frozen observable** | `EW{STX, WDC, AMD}` **minus `SMH`**, **4 settled-session** returns, `auto_adjust=False`, 2026-09-04 close → **2026-09-11** close |
| **Branch A** (the low-surge/high-Δ sub-node leads ⇒ the surge gate cost information) | **≥ +6.825** (p85) |
| **Branch B** (it lags its own sector ⇒ the gate filtered correctly) | **≤ −3.406** (p15) |
| **Branch C** | between |
| **`D93` BEFORE freezing** | trailing 252: mean **+1.567** · sd 5.051 · p05 −5.887 · **p15 −3.406** · p50 +1.647 · **p85 +6.825** · p95 +10.300 ⇒ A ≈15% · B ≈15% · C ≈70%. ★ **centre POSITIVE (+1.567)** — these three beating `SMH` is the *normal* state, so B is the harder branch and the row is written knowing it |
| **State at registration** | **+0.712 = the 44.8th percentile** — dead middle, slightly **below** its own mean. **No edge in either direction at the start** |
| **Anti-signal (VOID)** | an **earnings print at `STX`, `WDC` or `AMD`** inside 09-05 → 09-11 (checked via `Ticker.earnings_dates`, **not** the forward-calendar field — `D488`), or a semiconductor-specific US export-control **action** (a published rule, not a draft) |
| **Information content (`B4`)** | **A** says a whole node was invisible to this desk's own green gate for the wrong reason and the tag should not gate candidates. **B** says the gate earned its keep on US data and `C29` is a KR-only finding that does not transfer. **Neither merely confirms**, and either way the US desk finally has one own-market observation on the axis |
| **Non-redundancy (`D343`)** | `P137` asks whether **`SMH` itself** extends vs `SPY`; **`S145` asks whether the sub-node beats `SMH`** — the two can fire in opposite directions and the pair is more informative than either. `S140` (09-08) is a **breadth** row |
| **Owner** | `industry_US` |

### `S146` — ★★★ Is the AI-power lane one object, or is the book holding its worst name?

**Why it exists.** Lens 4 finding `M1308` + EVENT_ALPHA Card 6's **book flag**. `ETN` is **held**,
**🔴분산 −0.662**, rs20 **−8.0**, while `VST` (Δ +0.491), `CEG` (+0.644, OBV 매집) and `VRT`
(Δ +0.444, OBV 매집) all accumulate — **and the four sit in two different GICS sectors**, so no
sector verdict can express the split (`D416`).

| | |
|---|---|
| **Frozen observable** | `EW{VST, CEG, VRT}` **minus `ETN`**, **5 settled-session** returns, `auto_adjust=False`, 2026-09-04 close → **2026-09-14** close (09-07 is Labor Day) |
| **Branch A** (the split widens — generation/thermal is the lane and components are not) | **≥ +7.651** (**p95, not p85**) |
| **Branch B** (`ETN` catches up ⇒ the split was noise and the book's placement is fine) | **≤ −5.037** (p15) |
| **Branch C** | between |
| **`D93` BEFORE freezing** | trailing 252: mean **+0.103** · sd 4.967 · p05 −7.534 · **p15 −5.037** · p50 +0.394 · p85 +4.956 · **p95 +7.651** ⇒ A ≈5% · B ≈15% · C ≈80% |
| **⚠ Asymmetric branch design, declared** | **A is set at p95, not p85, because the state is ALREADY at the 92.9th percentile.** Using p85 (+4.956) would make A near-certain and therefore uninformative (`B4`) — the same construction `P102` used from a 98.8th-percentile state |
| **State at registration** | **+6.681 = the 92.9th percentile.** ⚠ **DISCLOSED: mean reversion is the base case from here, so B is the harder-to-reach but higher-information branch, and C is the favourite** |
| **Anti-signal (VOID)** | an **announced acquisition or merger involving any of the four**, or a **PJM/ERCOT capacity-auction result or emergency order** inside 09-05 → 09-14. ⚠ **Base rate checked**: no scheduled capacity auction falls in the window; the desk's own carried `M367` notes PJM cleared at the price cap in a prior auction, which is a *past* event and not a voider |
| **Information content (`L3`)** | **A** says the desk's one AI-power holding is the wrong expression of a live cycle and the registry's missing row (`D416`) has a measurable cost. **B** says the 09-04 flow split was a one-session artifact and the lane is one object. **Neither merely confirms** |
| **Non-redundancy (`D343`)** | `P123` (09-08) asks whether the AI marginal dollar moved **to power at all** — a cross-cycle question. **`S146` asks WHICH NAMES inside the lane**, which `P123` cannot answer. `S127`–`S130` are name-level AI-compute rows |
| **⚠ `W3`** | this measures a spread, not whether any position was right, and it sizes nothing (P4) |
| **Owner** | `industry_US` |

### `S147` — ★★ The refiner sub-node: EXTENDED-BUT-LIVE, or is `L2`'s peak-margin trap loaded?

**Why it exists.** Lens 3 tagged `MPC`/`PSX`/`VLO` **EXTENDED-BUT-LIVE** on an accelerating cycle KPI,
**and all three trade above consensus mean targets on +45–85%/90d revisions** — the textbook `L2`
peak-margin setup, and the exact basis on which `VLO`'s rejection was reaffirmed on 09-04.
**ROTATION promoted this sector to `OW+` today.** The sub-node deserves its own test because
**`P136` measures the 16-name sector and can fire `C` while the three-name refiner leg does
something else** (`W5`).

| | |
|---|---|
| **Frozen observable** | `EW{MPC, PSX, VLO}` **minus `SPY`**, **5 settled-session** returns, `auto_adjust=False`, 2026-09-04 close → **2026-09-14** close |
| **Branch A** (EXTENDED-BUT-LIVE confirmed — the sub-node leads the promotion) | **≥ +7.059** (p85) |
| **Branch B** (the peak-margin trap is loaded and springs) | **≤ −3.740** (p15) |
| **Branch C** | between |
| **`D93` BEFORE freezing** | trailing 252: mean **+1.275** · sd 5.266 · p05 −7.669 · **p15 −3.740** · p50 +0.809 · **p85 +7.059** · p95 +10.846 ⇒ A ≈15% · B ≈15% · C ≈70%. ★ centre **positive**, so the refiners beating `SPY` is the normal state and the row says so |
| **State at registration** | **+4.955 = the 75.4th percentile** — leaning A but inside C |
| **⚠ Event contamination — OWNED, not voided** | the window contains **PPI 09-10** and **CPI 09-11**, both 🔀binary. There is no clean 5-session window; making them anti-signals would be the designed-to-void defect |
| **Anti-signal (VOID)** | 🚨 **the one Card 1 named and `P136` does NOT cover**: a **US federal policy action directed at refiner margins or fuel pricing** (an executive order, a price mechanism, an export restriction on refined products) inside 09-05 → 09-14 — the live thread is *"Trump ramps up pressure on refiners"* [seekingalpha 09-01]. Also VOID on an **OPEC+ emergency production decision** or an **announced Hormuz-open statement**. ⚠ **`P136` was frozen without the policy clause and is NOT amended** (`D242`); `S147` carries it and the difference between the two rows is deliberate |
| **Information content (`L3`)** | **A** says an EXTENDED tag with an accelerating cycle KPI beats a valuation objection, which is a rule the desk can carry. **B** says `L2` loaded and the `ENRG OW+` promotion issued today bought the top of a margin cycle. **Neither merely confirms** |
| **Non-redundancy (`D343`)** | `P136` = the **16-name sector** vs `SPY`, 5 sessions to 09-14 — **same window, different unit.** ★ **The pair is deliberately co-dated**: if `P136` fires `C` and `S147` fires `A` or `B`, the sector verdict and the sub-node verdict have separated, which is the `W5` question this desk keeps re-discovering by accident |
| **Owner** | `industry_US` |

### `S142-ANNEX` — the row's premise inverted inside its own window

**Registered, not re-banded.** `S142` (settles **2026-09-11**) was written 09-02 as
*"the against-us branch of the **FIN UW** issued today"*. **`FIN` moved `UW → N` on 2026-09-05**
(ROTATION §2, carried by `eqflow` −0.220 → −0.023 and Δ −0.220 → −0.004).
⇒ **The frozen observable and thresholds are UNTOUCHED** (`D242`). The annex records only that
**the branch labels must be read against the 09-02 verdict, not against today's**, so the scorer on
09-11 does not read a confirmation as a contradiction. ★ Filed as **`D511`**: *a bracket written
against a verdict can outlive the verdict, and nothing currently links the two — a row's branch
LABELS should carry the verdict they were written against.*

### Digs registered by this stage
- **`D511`** — *a bracket's branch labels are written against a verdict that can change inside the
  bracket's own window.* **Measured origin**: `S142`, above.
- **`D512`** — *the desk's UW count over-states its diversification: `RE`, `STPL` and `UTIL` are one
  duration bet under three sector labels, and today's `STPL N→UW` demotion added a fourth position
  to the same bet.* **Measured origin**: all three carry breadth **0.00**, **zero greens**, and are
  bracketed as one object by `S135`. The 2026-07-15 correlated-UW field note, reproduced.
- **`D513`** — *`CYCLE_EXPOSURE`'s GAP flag can only see cycles the registry contains, so a missing
  registry row reads as "no gap."* **Measured origin**: the AI-power lane (`M1308`) — four coherent
  names across two GICS sectors, the book holds the only distributing one, and the run's GAP verdict
  is ✅. **`D416` upgraded from "no registry row" to "the absence is invisible to the flag."**

---

## §Final DEEP set

**`N = 4/4` — continuous `[ENRG, HLTH]` + PREMORTEM-promoted `[IT, UTIL/AI-power lane]`.**
Both promotions come from Lens 1 with named catalysts (`S140` 09-08 · `P123` 09-08) and named
evidence (`P101`'s inversion · the `ETN` book flag). **Neither is an OW sector**, which is why they
required a promotion rather than a rotation — stated so the next run's recency rule reads them
correctly.

---

## ✅ EXIT CHECK — PREMORTEM

- [x] **4 lenses run**, each returning **named tickers and dated catalysts**. ⚠ **Run in-context and
      serially, NOT as parallel agent fan-outs** — declared at the top as a weakness, not omitted.
- [x] **Every bracket names its observable + frozen threshold + date, with BOTH branches.**
      `S145` (09-11) · `S146` (09-14) · `S147` (09-14) · `S142-ANNEX`. **No one-way bracket** —
      each has A, B and C with explicit lines. ✅ **Registration EXECUTED IN THIS STAGE, not deferred
      to writeback**: appended verbatim to `handoff/SCENARIOS_US.md` and indexed in the
      `handoff/SCENARIOS.md` master index (both backed up as `*.bak_0905us` first). This is
      deliberate — `D504`/`D490` are two of this run's own dig items, and a stage that criticises
      deferred writes and then defers its own would be the failure it just named.
- [x] **Every magnitude threshold stated against the implied move** — and the finding is that
      **no implied move covers either binary** (`M1305`: `SPY` ±0.5% / `SMH` ±1.8% expire **09-08**,
      `XLE` ±1.6% expires **09-09**, against PPI **09-10** and CPI **09-11**). ⇒ all four thresholds
      come from **`D93` measured dispersion** and each says so. **No threshold is presented as
      "outside the implied move" when nothing prices the event.**
- [x] **Each branch graded by information content.** ★ **August PPI was DROPPED with the reason
      stated** — neither branch would change the conclusion (`B4`), so no bracket was spent on it.
      The CPI carries five independent both-sides rows and no sixth was added.
- [x] `BLINDSPOT_PREMORTEM.md` written — under-computed legs (2 promoted, 4 logged as within-run
      watch, **none silently dropped**) · both-sides brackets per binary · momentum re-tags for 13
      names with flip conditions · cycle-GAP audit.
- [x] **Brackets handed to ALPHA's action bracket; the cycle finding handed to BET** as a named
      structural gap (`M1308`/`D513`) rather than as a registry ✅.
- [x] **DEEP set updated and stated: `N=4/4`, `[ENRG, HLTH]` + `[IT, UTIL/AI-power]`.**
- [x] ⚠ **The lenses did NOT all agree with the draft** — Lens 1 promoted two sectors ROTATION had
      declined five runs running, Lens 2 found a registered row whose premise this run inverted, and
      Lens 4 found a cycle gap the deterministic flag cannot see. **Three of four lenses corrected an
      earlier stage of this same run.**
