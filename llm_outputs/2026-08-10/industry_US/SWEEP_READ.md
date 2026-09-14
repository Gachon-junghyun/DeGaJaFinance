# SWEEP_READ — industry_US · 2026-08-10 · Stage 4/11 (L1·SWEEP)

> **The reading, not a second copy of the data.** Numbers live in `SECTOR_FLOW_US.json` ·
> `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.json`. Nothing here reprints a table those hold.
> Analytical only (P4).

## 0. 🚨 The instrument's health line, read BEFORE its numbers

`SECTOR_FLOW_US.json §scoring`:

```
vel_axis false · vel_coverage 0.0 · n_axes 3 · scored 299 · dropped_missing_axis 1
```

**The news axis is DEAD in this run — coverage 0.0%, not low.** And it is **the pipe, not silence**,
probed rather than assumed:

- `fts search Nvidia --days 7 --scope foreign --count` → **3,321**. `tariff` → 1,439 ·
  `Federal Reserve` → 1,119 · `natural gas` → 731 · `Broadcom` → 306.
- ★ **Two sweeps, twelve minutes apart, on identical cached prices, measured `vel_coverage`
  16.0% then 0.0%.** A path that returns a different coverage each call while the pool is unchanged
  is **non-deterministic**; the fault is the sweep's per-name velocity hop, not collection or indexing.

⇒ **All 299 names are scored on 3 axes (OBV · RS20 · vol_surge), uniformly.** The scores are
internally consistent and **not comparable to any 4-axis run (G2)**. **No Δ is cited anywhere in this
file**, and the one the tool printed is disqualified separately (§4).

---

## 1. Universe headline — three numbers

**n = 299 of 300 · wflow −0.042 · 🟢 15 / 🔴 76** (asof settled **2026-08-07**).

---

## 2. ★★★ The cross-check that matters: this run is an unplanned ABLATION and it CONFIRMS M513

The 08-08 run decomposed all 23 greens and pre-registered a mechanism (**M513 / R59 / D205**):
the `velocity` field is populated on a **stable ~50-name whitelist**, and **both Energy greens (XOM
`vol_surge` 0.88, CVX 0.96) and three of four Financials greens (JPM 0.65, BAC 0.73, BRK-B 0.85) were
velocity-lit on BELOW-average volume.** It predicted, in effect: *remove velocity and those greens
disappear.*

**Today velocity was removed — not by design, by defect — while the price bar stayed identical.**
Three runs, the same settled 08-07 close, the same universe file:

| | 08-08 | 08-09 | **08-10 (velocity dead)** | M513's prediction |
|---|---|---|---|---|
| universe 🟢 | 23 | 22 | **15** | — |
| **Energy** 🟢/16 | **2** | **2** | **0** | **2 → 0** ✅ |
| **Financials** 🟢/47 | **4** | **4** | **1** | **4 → 1** ✅ |
| IT 🟢/56 | 5 | 4 | 3 | — |
| Health Care 🟢/32 | 5 | 5 | 4 | — |

**Both pre-registered numbers landed exactly.**

### 2a. And a second, independent confirmation of the same mechanism — from the sectors that did NOT move

On an unchanged price bar, eight of eleven sectors' `wflow`/`eqflow` moved between the 08-08/08-09
runs and this one. **Three did not — byte-identical across all three runs:**

**Materials (−0.038 / +0.040) · Real Estate (−0.032 / −0.025) · Utilities (−0.395 / −0.381).**

Cross-referenced against `us_top300.csv` by market-cap rank:

| Sector | names in mcap-rank **top 50** | flow moved on an unchanged bar? |
|---|---|---|
| **Materials · Real Estate · Utilities** | **0 · 0 · 0** | **NO — byte-identical** |
| IT 20 · FIN 8 · HLTH 5 · STPL 5 · COMM 4 · DISC 3 · INDU 3 · ENRG 2 | ≥2 each | **YES — all eight moved** |

⇒ **11 of 11 agreement.** The sectors that contain a velocity-whitelisted name are exactly the
sectors whose flow numbers move when the velocity axis dies, and the sectors that contain none are
exactly the ones that do not. **R59's "~50-name whitelist" is confirmed by where the movement is
absent**, which is a stronger test than confirming it where the movement is present.

⚠ **What this does NOT license.** It is **not** a Δ reading (G2 forbids that, and no flow_score level
here is compared across scoring modes). It is a **membership** comparison of a tag whose mechanism was
pre-registered two runs ago, on an unchanged price input. **The green counts are the observable; the
scores are not.**

---

## 3. Cross-checks against the MACRO transmission matrix — where flow and price disagree

The matrix carried into this stage: `INDU OW− · ENRG N+ · FIN N+ · IT N · HLTH N · DISC N · MATR N− ·
COMM UW · UTIL UW · STPL UW− · RE UW`.

**① CONTRADICTION — Energy ranks #1 on flow and LAST on price, and §2 explains it.**
`SECTOR_FLOW_US.json §sector_rotation` puts Energy **first of eleven on wflow**. MACRO §C puts **XLE
exc5 at −6.95, worst of eleven**. The gap was previously argued (08-08) from a decomposition; today
it is argued from an ablation: **Energy's flow rank survives on mega-cap weight while its breadth is
now 0 greens of 16 with eqflow +0.063.** ⇒ **the N+ is a cap-weighted artifact on this instrument,
and the money-side case for it is weaker than the rank suggests.** **ROTATION owns the call.**

**② CONTRADICTION — Financials ranks #2 on flow with breadth 1/47 (2%).**
Same shape, same cause. **DEEP-FIN's 08-08 finding that exactly ONE of 47 names clears
volume-confirmed accumulation (PRU) is reproduced today by a different route**: with velocity gone,
**PRU is the one Financials name left on the shortlist.** Two instruments, two runs, one name.

**③ CONFIRMATION — Industrials is genuinely breadth-led, and it is the only sector where that is true.**
**eqflow (+0.098) exceeds wflow (+0.041)** with **5 greens of 50**, and **three of the fifteen
shortlist names are Industrials (EMR, PH, AME)** — none of them mega-caps. This is the one place the
board's single OW− is corroborated by breadth rather than by weight.

**④ CONFIRMATION — Utilities UW, on the board's only fully-consistent negative.**
wflow **−0.395** and eqflow **−0.381** — the two agree, breadth 0/15, and MACRO has XLU at the worst
20-day excess on the board (−6.39). **No decomposition rescues it.** ⚠ It is also one of the three
sectors §2a shows the instrument cannot move — so this reading is the *same* reading three runs
running, not three observations (S1).

**⑤ CONTRADICTION, and it is a caution rather than a call — Comm Services.**
wflow **−0.262** against eqflow **+0.050**: the sector's weight is negative while its breadth is
positive. **R56 binds — its 2 greens must be re-derived ex-EA, and EA is still in the universe** (§5).

**⑥ Materials cannot be called from this instrument at all.** It is the run's only `top1_flips_sign`
bucket (§4), **and** it is one of the three sectors §2a shows are frozen. **Two independent reasons
not to move it; MACRO §C-1 supplies the third (85% of its live falsifier is one name in an M&A event).**

---

## 4. The `top1_flips_sign` list, in full — handed to ROTATION as a prohibition

**One sector of eleven flips sign when its largest name is removed:**

| Sector | wflow | ex-top1 | top1 | share of sector cap | n |
|---|---|---|---|---|---|
| **Materials** | **−0.038** | **+0.173** | **LIN (Linde)** | **24.7%** | 12 |

**ROTATION may not promote or demote Materials on `wflow`.** Ten sectors keep their sign ex-top1;
for the record the largest non-flipping magnitude shifts are **Consumer Discretionary −0.033 →
−0.273 (AMZN)**, **Energy +0.286 → +0.151 (XOM)**, **IT −0.008 → −0.110 (NVDA)**, **Industrials
+0.041 → +0.105 (CAT)**.

🚫 **And the Δ column is disqualified this run (`D232`).** `prev_snapshot()`'s mode guard worked — it
refused all thirteen 4-axis snapshots — and then matched **2026-07-20, the only other 3-axis entry in
`history.json`, which holds FIVE tickers** (the residue of a `--tickers` scratch run). Consequently
**294 of 299 names carry `delta = null`**, only **2 of 11 sectors carry a Δ**, and the printed line
`Δ상승: NVDA ▲0.95 …` is **18 calendar days over a 1.7%-complete baseline**, not day-over-day. The
`신규🟢` list is the same artifact. **No Δ and no "new 🟢" is cited by this desk today.**

---

## 5. Shortlist — read the absences, and one name that should not be there

15 names cleared `mcap ≥ $10B ∧ 🟢가속`, ranked by flow (`US_LIVE_SHORTLIST.json`).

**① The absences are the finding, and they are the same two sectors as §3.**
**Energy contributes ZERO shortlist names and Financials contributes ONE (PRU).** ⚠ **Diagnosed, not
cited**: this is **not** evidence that money left them — it is the **direct arithmetic consequence of
the velocity axis dying** (§2), because their greens were the velocity-lit ones. **An ENRG shortlist
of 0 was previously ruled a filter artifact on this desk (07-15); today the artifact's mechanism is
measured rather than suspected.** Also absent entirely: **Utilities, Real Estate, Materials, Consumer
Staples, Consumer Discretionary** — all five have 0 greens, and three of them are the frozen sectors.

**② Composition:** Industrials 3 (EMR, PH, AME) · Health Care 3 (BMY, AMGN, IDXX) · IT 3 (PLTR, SHOP,
COHR) · Comm 2 (DIS, EA) · Financials 1 (PRU) · plus TRI, WAT, BA. **Breadth-led sectors dominate it,
which is consistent with §3③.**

**③ 🚨 EA is on the shortlist and EA does not trade.** The **D207 liveness assertion was executed on
all 15 names** (last-two settled bars: `volume = 0` on either **or** `O=H=L=C` on both):

```
15 tested → 1 FAIL (EA: volume 0 and 0) · 0 false positives
```

**Fourth consecutive run, same single true positive, zero false positives.** EA carries the board's
**highest OBV (+0.75)** and a flow score of **+0.67** on a security that went private 08-04/05.
**EA is excluded from every downstream read**, and **R56 binds on Comm Services breadth.**
⚠ **`D215` still stands** — the rebuilder the sweep's own stderr names (`build_top300.py`) does not
exist. ★ **But a path does**: `data/us_universe/build_us_universe.py` exists and produced
`us_all_v2_candidate.csv` (1,522 names) **today at 00:53**. **Pointing the sweep at it is a human
decision (P5); naming that the option exists is this stage's job.**

**④ Short-pressure axis (FINRA z, the US substitute for KR's investor actuals):**
one **✅ clean rise** — **BA, z −1.80** (low short / covering, the only one) — and one
**⚡ crowded short** — **WAT, z +2.27** (squeeze fuel, turn-conditional, never a standalone read).
The other thirteen are `△normal`. ⚠ **US has no investor-type feed; this is a proxy, and it is
context.**

---

## 6. 🚨 The universe invariant, and a NEW finding: the desk has TWO books and does not say which

**Held-but-not-in-universe check, run rather than assumed:**

| Book | US names | outside `us_top300` | outside `us_all_v2_candidate` |
|---|---|---|---|
| **paper book** (`module_paper_book status`) | AVGO · KMI · **LNG** · MA · NVDA · RTX · **TSM** · VST | 🚨 **LNG · TSM** (11th run) | **0** |
| **real KIS account** (`cycle_exposure`, cycle-tagged names) | ANET · AVGO · ETN · MPC · NVDA · PSX · RTX | **0** | **0** |

★★ **The two books overlap on THREE names: AVGO, NVDA, RTX.** The paper book holds KMI/LNG/MA/TSM/VST
that the real account does not; the real account holds ANET/ETN/MPC/PSX that the paper book does not.

⇒ **`HANDOVER §6`'s five-run-old finding — *"S31 says XOM is the only Energy name the book holds, and
the book holds no XOM"* — is now sharper: the desk has two books, its stages read different ones, and
neither holds XOM.** The paper book's Energy is **KMI/LNG**; the real account's is **MPC/PSX**.
**A reconciliation line that says "the book" without naming which one cannot be right about eight of
eleven names.** ⇒ **`D233`**, handed to PREMORTEM alongside the S31 re-registration.
⚠ **Scope (C4)**: this does not say either book is wrong. It says **the word "the book" is ambiguous
in this desk's own files**, which is a naming defect — the class §1b of HANDOVER calls this desk's
dominant one.

**🚫 Rights, restated from PREFLIGHT G5:** **LNG and TSM carry NO flow / RS / OBV / short verdict
today.** They are **"not measured," never "no signal."** ★ And this is now a **wiring** gap rather
than a data gap: both are in the 1,522-name candidate file built this morning.

---

## 7. Cycle-exposure GAP — ✅ none, and the reason it is worth one line anyway

`CYCLE_EXPOSURE.json`, real KIS account, total ≈ **$10,950** (invested $6,413):

- **AI-compute rank 1**: epicenter **19.56%** vs a **12.0%** floor — margin **+7.56pp**. ✅
- **Energy/oil-refining rank 2**: epicenter **10.51%** vs **8.0%**. ✅
- **Missile-defense rank 3**: 6.18%, **no floor set** ⇒ `⚪ n/a`.

**No 🚨 to hand to ALPHA's action bracket.** ⚠ Two standing cautions carried, not re-derived:
**`D217`** (the rank-3 GAP check cannot fire by construction — a guard that cannot fire is not a
guard) and **M146** (this ✅ has previously cleared by **1.1 basis points** on mark-to-market drift
with nothing bought). **Today's margin is +7.56pp, which is not that case** — stated so the caution
is applied rather than recited.

---

## ✅ EXIT CHECK

- [x] 🚨 **`scoring` block read and quoted first** — `n_axes 3` · `vel_coverage 0.0` ·
      `dropped_missing_axis 1`. Coverage < 80% ⇒ this file states **"news axis dead this run"** and
      names the cause as **pipe, not silence**, having **actually probed it** (5 probes, 306–3,321 hits)
      and having measured the path to be **non-deterministic** (16.0% → 0.0%, twelve minutes apart)
- [x] **Every `top1_flips_sign` sector listed with its top1 and cap share** — Materials / LIN / 24.7% /
      n=12 — **and handed to ROTATION as a prohibition** (§4)
- [x] **Held-but-not-in-universe check RUN, for both books** — 🚨 **LNG · TSM outside `us_top300` for an
      11th run**, reported here rather than left for a later stage (§6)
- [x] sector_flow sweep done → `SECTOR_FLOW_US.json`; sector ranking read; **new-🟢 explicitly
      DISQUALIFIED and not read** (`D232`, §4)
- [x] `US_LIVE_SHORTLIST.json` written; short-pressure verdicts read (**BA ✅ clean · WAT ⚡ crowded**)
- [x] `CYCLE_EXPOSURE` GAP read — **none**; nothing handed to ALPHA's action bracket (§7)
- [x] **No table in this file exists in the JSONs** — sector rows and per-name rows are cited by
      artifact. The three tables present are a **cross-run ablation**, a **top-50-by-sector census**,
      and a **two-book comparison** — none of which any JSON holds
- [x] **At least one cross-check that confirms or contradicts the MACRO matrix**: six, with the side
      the money is on named for each (§3)
- [x] **Absences diagnosed before being cited** — the ENRG-0 / FIN-1 shortlist is traced to the dead
      velocity axis, not read as evidence of outflow (§5①)
- [x] **No position sizing, no buy/sell language (P4)**
