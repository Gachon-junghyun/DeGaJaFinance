# SWEEP_READ — industry_US · 2026-08-28 (Stage 4 / L1·SWEEP)

> **The reading, not a second copy of the data.** Numbers live in `SECTOR_FLOW_US.json` and
> `US_LIVE_SHORTLIST.json`; sector rows and per-name rows are **cited, not reprinted**.

---

## §0 · Instrument health, read before the numbers

**`scoring` block, quoted verbatim** — `SECTOR_FLOW_US.json §scoring`:
`{vel_axis: false, vel_coverage: 0.1672, n_axes: 3, scored: 299, dropped_missing_axis: 0}`

**News axis dead again (16.7% vs the 80% bar) — and it is the pipe, not silence.** Probed twice, not
assumed: (1) PREFLIGHT's live CLI probe this run — `Nvidia` **5,161** · `Eli Lilly` **180** ·
`Nucor` **26** · `Marathon Petroleum` **23** (`--days 7 --scope foreign`), two orders of magnitude
apart ⇒ the pipe answers and discriminates. (2) ★ **`R103`'s cap reproduces inside this run's own
sweep for a 5th time**: the 50 names carrying a velocity are `us_top300` **ranks 1–50, contiguous,
zero gaps** (verified against `data/us_universe/us_top300.csv`). ⇒ **`M1020`.**

🚫 **Enforced here and handed to ROTATION**: no theme-freshness or velocity citation; **the `news`
column of `US_LIVE_SHORTLIST.json` (`MRVL` 1.90 · `JNJ` 1.26, with `CRM` and `A` reading `n/a`) is not
quoted as evidence** — two of four shortlist names are inside the rank-50 prefix and two are outside
it, so the column is a **mega-cap-only** sample, not a cross-section. No name is called quiet.

**`n_axes` = 3**, same as every snapshot 08-20 → 08-28 ⇒ Δflow arithmetic is scale-legal (G2 PASS);
`dropped_missing_axis` = 0. ⚠ **`§asof` checked too, per HANDOVER §0**: today reads `asof 2026-08-28`
and yesterday `2026-08-27` — **distinct**, so the Δ is a real difference and not the self-subtraction
the 08-22/23/24 band would have produced.

### 🚨 `D355` reproduces a **4th** consecutive run — this sweep ran on a pre-market stub bar

Measured on the sweep's own price cache (`llm_outputs/sector_flow/prices_2026-08-28.pkl`), 08-28
volume ÷ 08-27 volume across all 300 names: **median 2.40%** · mean 3.81% · **1 of 300 above 50%**,
2 above 20% · **aggregate 5.12%.** (08-27: 4.65% median, 2 of 300; 08-26: 2.48%, 0 of 299.) ⇒ **`M1021`.**

🚫 **Therefore the universe's 4 🟢 / 76 🔴, every `breadth` figure and every `delta` are NOT read as
levels or as changes in this file.** They are declined. What survives a stub bar is the
**cross-sectional ordering** of `eqflow` — all 299 names share the same partial session — and that is
all §2 uses.

### 🚨 The `top1_flips_sign` list CHANGED between PREFLIGHT's baseline and this run's own sweep

PREFLIGHT read the **08-27** snapshot and removed the promotion right from **Health Care and Energy**.
**Today's live sweep names a different pair: Health Care (`LLY`) and INFORMATION TECHNOLOGY (`NVDA`).
Energy is no longer a flipper; IT now is.** ⇒ **`M1022`.**
**Both lists are applied, union-wise and conservatively** — a right is not restored by a fresher
instrument mid-run: **Health Care, Energy AND Information Technology may not be promoted or demoted on
`wflow` this run.** The fresher measurement (IT) is the *binding* one and it is the one that matters,
because IT is the sector MACRO put the wind behind.

---

## §1 · Universe headline — three numbers

**n = 299** (of 300 requested; the 44-day-old universe again supplies one uncomputable name) ·
**universe `wflow` −0.208** · **4 🟢 / 76 🔴.**
⚠ `wflow` carries the **44-day cap stamp** (G5) and the counts sit on the stub bar — quoted because §1
requires three numbers, **not used below**.

---

## §2 · Cross-checks against the MACRO transmission matrix — where the money disagrees

### ✅ CONFIRMS (3)
- **Health Care N+** — `eqflow` **+0.057, 2nd of 11**, and the **only sector on the board with
  non-zero breadth (0.06)**. MACRO put it N+ on `XLV exc60 +15.68` vs `SPY`; the flow agrees on a
  different axis. ⚠ Ranked on `eqflow`, **not** `wflow` (−0.046), because `LLY` owns that sign (G3).
- **The duration underweights** — `eqflow` Utilities **−0.546** (last), Real Estate **−0.384**,
  Staples **−0.282**. MACRO's UW/UW/UW is where the money is not.
- **Energy cut from OW to N** — `eqflow` **−0.093, 5th**, and **13 of 16 names are 🟡 with 3 🔴 and
  zero 🟢**. The cut is confirmed by flow, not only by `XLE exc5 −3.40` vs `SPY`.

### 🚨 CONTRADICTS (2) — and this is the file's reason to exist

**★★★ 1. Information Technology: MACRO's `OW−` is one company, and the sweep says so twice.**
`wflow` **+0.035** (positive) vs `wflow_ex_top1` **−0.042** and `eqflow` **−0.029** — **both negative**
— with `top1_flips_sign: TRUE` on `NVDA` and breadth **0.04 (2 green of 56)**.
⇒ **the sector's only positive number is `NVDA`'s, and removing that one name flips the sign.**
This is the same object §A-4 of MACRO measured from the other side (`XLK` 1st on exc1/5/20, **last on
exc60**), reached by an independent instrument. **The money is on: it is one name, not a sector.**
⇒ ROTATION may not promote IT on `wflow` (G3, and now measured live).

**★★ 2. Materials: the board's best flow, and MACRO gave it no proposition at all.**
`wflow` **+0.146** *and* `eqflow` **+0.087** — **the only sector positive on both** — with
`top1_flips_sign: FALSE` (`LIN`), i.e. **not a one-name artifact and not subject to any removed right.**
MACRO's matrix row 6 wrote *"N · no proposition owns this and that is stated."* **The sweep says that
absence is the run's largest unowned signal.** Handed to ROTATION as a candidate, with the copper
100th-percentile positioning attached as `D6` **context, never a direction**.

---

## §3 · Shortlist composition — the absences, diagnosed before they are cited

**4 names of 299 survive the filter** (`mcap ≥ $10B` ∧ `tag 🟢가속`): `CRM` · `A` · `MRVL` · `JNJ`.
**Nine of eleven sectors produced ZERO shortlist names.** The absences are the finding, and two are
diagnosed here rather than read:

**★ The Materials absence is a gate artifact, not evidence — the same class as 08-27's ENRG-0.**
Materials leads the board on `eqflow` and is **12 of 12 🟡중립, zero 🟢**. `FCX` carries flow
**+0.650**, OBV **매집**, `rs20 +21.0` and is blocked from 🟢 by **`vol_surge` 0.97** alone; `NEM`
+0.544 at surge 0.78. ⇒ **`M1023`.**

**★★ And the gate is being applied to a 2.40%-volume bar.** `vol_surge` is the one axis that reads a
*volume level*, and §0 measured today's bar at **2.40% of the prior session**. ⇒ **the 🟢 count is
mechanically suppressed across the whole universe**, which is why 4 of 299 pass on a day the index
rose. **The shortlist's shortness is an artifact of the hour this desk runs at, not a statement about
the market.** ⇒ **`M1024`.**
🚨 **Compounding, and it is the uncomfortable half**: HANDOVER §5 records `vol_surge` h=1 as the one
cell that **clears Bonferroni with a NEGATIVE sign** (IC −0.0444, `t(NW) −3.84`, n_eff 39) — while the
sweep weights it **positively** and uses it as the 🟢 gate. ⚠ **That measurement is KR-labelled and is
not transferred (`W1`)**; it is stated because the gate producing this shortlist is the same axis, not
because the KR result licenses changing it (P4).

**The two `new_green` names are the informative part of a 4-name list**: `CRM` **+0.828 = 1st of 299**
and `A` **+0.778 = 2nd**, both flipping green today.
★ **`CRM` was named by MACRO's blind-spot pass BEFORE the sweep ranked it** — `SAASPOCALYPSE`
(`M1016`, 7 articles / 4 outlets / 100% market relevance) with *"Salesforce Surges 23% on Anthropic"*
in the 08-27 tape. **Two independent instruments, one name, and the term-based one was first.** That
is the blind-spot pass doing exactly what it exists for. ⇒ **`M1025`.**

⚠ `MRVL` is the shortlist's only **⚡crowded-short (FINRA z +2.70)** — squeeze fuel, turn-conditional,
**never a standalone signal (`D6`)**. `CRM` (z −0.89) and `JNJ` (z −1.72) are clean rises; `A` is
normal (+0.50).

---

## §4 · Held-name coverage and cycle GAP

**All 11 US book names are in the universe** (G5 coverage leg clean), so every holding is taggable —
the `TSM`/`LNG` invariant holds this run.
FINRA short on the book, 08-27: **`MPC` z +2.04 🔴 short surge** is the only red; `ETN` +1.30 and
`ANET` +0.63 are elevated-normal; `NDAQ` −1.47, `NUE` −1.30, `AVGO` −1.22, `MET` −1.11, `NVDA` −1.04
are shorts leaving. ⚠ **`MPC`'s short surge lands on the same name whose two separation instruments
both failed today** (`P83` B, `P96` B — MACRO §E-2). Recorded, not resolved; DEEP's item.

`cycle_exposure`: **no GAP** — AI-compute epicenter **17.42%** (need ≥12.0%), Energy/refining
**9.83%** (need ≥8.0%). ⚠ **Rank-3 (missile-defense, `RTX` 3.81%) still has no threshold set**, so it
neither passes nor fails — 🚫 not read as ✅. ⚠ **`cycle_registry.json` still carries no optical row —
`D250`, 13th run** ⇒ optical exposure remains **unmeasurable, not zero**.
