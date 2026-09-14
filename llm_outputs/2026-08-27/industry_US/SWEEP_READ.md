# SWEEP_READ — industry_US · 2026-08-27 (Stage 4 / L1·SWEEP)

> **The reading, not a second copy of the data.** Numbers live in `SECTOR_FLOW_US.json` and
> `US_LIVE_SHORTLIST.json`; sector rows and per-name rows are **cited, not reprinted**.

---

## §0 · Instrument health, read before the numbers

**`scoring` block, quoted** — `SECTOR_FLOW_US.json §scoring`:
`{vel_axis: false, vel_coverage: 0.1672, n_axes: 3, scored: 299, dropped_missing_axis: 0}`

**News axis DEAD this run** (16.7% vs the 80% bar). **Cause: the pipe, not silence — and it was probed,
not assumed.** Two probes:
1. **PREFLIGHT's live falsification** (this morning, before the sweep): `Nvidia` **4,756** ·
   `Nucor` **31** · `Marathon Petroleum` **22** · `Nasdaq Inc` **6**, `--days 7 --scope foreign`.
   Three orders of magnitude apart ⇒ the pipe answers and discriminates.
2. ★ **`R103`'s cap hypothesis reproduces INSIDE this run's own sweep, a 4th time.** The 50 names that
   received a velocity are `us_top300` **ranks 1–50, contiguous, zero gaps** (verified against
   `data/us_universe/us_top300.csv`). Previous reproductions: ranks 1–51 on 08-25 and 08-26 (`M947`),
   byte-identical to each other. **The axis is CAPPED at a call count, not dying stochastically.**
   ⇒ **`M987`.**

🚫 **Consequences enforced in this file and handed to ROTATION**: no theme-freshness or velocity
citation anywhere; **the `news` column of `US_LIVE_SHORTLIST.json` (MRK 2.23 · MRVL 1.91 · JNJ 1.21) is
NOT quoted as evidence** — those three are inside the rank-50 prefix and the other two read `n/a`
because of the cap, so the column is a **mega-cap-only** sample, not a cross-section; no name is called
"quiet".

**`n_axes` = 3, same as every snapshot 08-20 → 08-27** ⇒ Δflow arithmetic is scale-legal (G2 PASS).
`dropped_missing_axis` = 0.

🚨 **`D355` reproduces for a 3rd consecutive run — this sweep ran on an UNSETTLED pre-market bar.**
`asof 2026-08-27` at **09:2x ET**, before the open. Measured on the sweep's own price cache
(`prices_2026-08-27.pkl`): **median volume 4.65% of the prior session; only 2 of 300 names above 50%**
(08-26: 2.48% and 0 of 299 — better, still a stub). ⇒ **`M988`.**
🚫 **Therefore: the universe's 5 🟢 / 67 🔴, every `breadth` figure, and every `delta` are NOT read as
levels or as changes in this file.** They are declined. What survives a stub bar is the **cross-sectional
ordering** of `eqflow` (all 299 names share the same partial session), and that is all this file uses.

---

## §1 · Universe headline — three numbers

**n = 299** (299 of 300 scored; the 43-day-old universe again supplies one uncomputable name) ·
**universe `wflow` −0.182** · **5 🟢 / 67 🔴.**
⚠ `wflow` carries the **43-day-old cap stamp** (G5) and the 🟢/🔴 counts sit on the stub bar — quoted
here because §1 requires three numbers, **not used below.**

---

## §2 · 🚨 The flipper list, in full — and it changed AGAIN between PREFLIGHT and SWEEP

**Handed to ROTATION, which may not promote or demote on these buckets** (`§sector_rotation[].top1_flips_sign`):

| sector | top1 | top1 weight | `wflow` | `wflow_ex_top1` | citable substitute |
|---|---|---|---|---|---|
| **Health Care** | `LLY` (Lilly) | **19.4%** | −0.033 | **+0.038** | `eqflow` **+0.086** (rank 1 of 11) · breadth **0.06** |
| **Energy** | `XOM` | **30.5%** | −0.091 | **+0.140** | `eqflow` **+0.042** (rank 2 of 11) · breadth 0.00 |

**Two of eleven.** The other nine carry `top1_flips_sign: false`.

🚨 **This is the 4th consecutive run in which the flipper set changed identity, and the 2nd consecutive
run in which it changed BETWEEN this run's own PREFLIGHT and its own SWEEP.**

| | flipper set |
|---|---|
| 08-24 baseline | Consumer Staples (`WMT`) |
| 08-25 baseline | Health Care (`LLY`) |
| 08-26 baseline / **today's PREFLIGHT** | Consumer Discretionary (`AMZN`) · Materials (`LIN`) · Energy (`XOM`) |
| **today's SWEEP** | **Health Care (`LLY`) · Energy (`XOM`)** |

⇒ **Rights change mid-run, and the change is in BOTH directions:**
- 🔴 **LIFTED** since PREFLIGHT: **Consumer Discretionary** and **Materials** are **not** flippers on
  today's snapshot. Their weighted-flow buckets are rankable again — which matters, because both are
  cross-checks this file needs (§3).
- 🟢 **ATTACHED** since PREFLIGHT: **Health Care**, for the third time in four runs.
- **Energy is the only sector whose restriction has persisted across the two stages.**

**Flipper identity has no run-to-run persistence and none may be inherited from memory** — including
from this run's own PREFLIGHT, four hours old.

---

## §3 · Cross-checks against the MACRO matrix — what the money confirms and what it contradicts

> MACRO's frame is **price excess vs `SPY` on settled 08-26 closes**; the sweep's frame is **flow on an
> unsettled 08-27 stub bar**. Two different instruments *and* two different bars — so agreement here is
> genuinely independent, and disagreement is informative rather than an artifact of shared inputs.

**✅ CONFIRMS (3)**

1. **Health Care `OW` — the flow instrument now agrees with the price instrument, on the horizon that
   matters.** Sweep: `eqflow` **+0.086 = rank 1 of 11**, and **the only sector on the board with
   positive breadth (0.06; 2🟢 / 3🔴 of 32)** — every other sector prints breadth 0.00 or 0.02–0.06 with
   no greens. MACRO: `exc60` **+14.028 = best of 11**. ⚠ **Stated with its substitution**: HLTH is a
   flipper this run, so this line is built on `eqflow` and `breadth`, **not** on `wflow −0.033`.
2. **Materials — the cleanest agreement on the board, and it is newly citable.** Sweep: **0 red of 12 —
   the only zero-red sector in the universe** — with `eqflow −0.042` rank 4. MACRO: `exc5` **+3.144 =
   best of 11**, `med5 +2.215`, **3 of 12 negative = best breadth**. **Two instruments, two bars, same
   answer.** ⚠ And unlike this morning, `MATR` is **no longer a flipper**, so the agreement carries no
   substitution caveat. Standing verdict is `N`.
3. **Consumer Discretionary — both instruments agree it is the soft end, and the restriction has
   lifted.** Sweep: `eqflow` **−0.339 = rank 9**, 0🟢/11🔴 of 28. MACRO: `exc1` **−0.866 = worst of 11**,
   `med5` **−1.227 = worst**. Standing verdict `N`. **This is the first run in six in which the
   board's widest `C5` gap (`D`-logged as DISC's flow-vs-price contradiction) has CLOSED** — both sides
   now read soft. ⇒ **`M989`.**

**🚨 CONTRADICTS (2)**

4. **`C16` persists and today it is sharper, on the desk's largest sector call.** Sweep: IT `eqflow`
   **−0.062 = rank 5**, `delta` **−0.087 = 2nd-worst on the board**, 9 red of 56. MACRO: IT `exc20`
   **+6.708 = best of 11** with only 20 of 56 negative on that window. **The flow instrument says IT is
   deteriorating; the 20-day price instrument says it is leading.** Standing verdict is **`UW`**.
   🚫 **Not resolved here by preference** — routed to **`P105`** (registered this run, settles 09-09),
   which puts the 20-day excess itself in a both-sided bracket. ⚠ The `delta` is on a stub bar and is
   therefore quoted **only** as a cross-sectional rank (2nd-worst of 11), never as a magnitude.
5. **Energy's two horizons disagree and the flow axis sides with neither cleanly.** Sweep: `eqflow`
   **+0.042 = rank 2**, but **0 🟢, breadth 0.00** — a positive mean with no participation. MACRO:
   `exc1` **+1.109 = best of 11** against `exc5` **−1.040 = worst of 11**. ⚠ **Flipper — `wflow −0.091`
   is barred**; the substitute (`eqflow` rank 2) argues *against* a demotion while breadth 0.00 argues
   against a promotion. Standing verdict **`OW`**, and the commodity leg is now bracketed by **`P103`**
   (the RBOB-roll row registered at MACRO §C-3), the equity leg by `S119` (settles tonight).

**One further note for ROTATION**: **Consumer Staples' sweep and price readings disagree in the
opposite direction to yesterday's demotion.** Sweep `eqflow` **−0.329 = rank 8** with 0🟢/7🔴 of 19;
MACRO `exc5` **+0.939** with only 4 of 19 negative. The 08-26 ROTATION demoted STPL to `N−` on
non-cap-weighted flow. **Both halves are stated; this file takes no side.**

---

## §4 · Shortlist composition — the absences, diagnosed

`US_LIVE_SHORTLIST.json`: **5 names** from a filter of mcap ≥ $10.0B ∧ tag 🟢가속 ∧ top-15 by flow.
Names are in the JSON and are not reprinted.

**Sector coverage of the 5**: Financials **2** · Health Care **2** · Information Technology **1**.
**Absent: Energy · Materials · Industrials · Utilities · Real Estate · Consumer Staples · Consumer
Discretionary · Communication Services — 8 of 11 sectors produced no name.**

🚫 **The absences are a FILTER ARTIFACT, not evidence, and the diagnosis is measured**: the whole
universe produced **5 🟢 out of 299** on a bar whose median volume is **4.65% of a session**. The 🟢 tag
requires `OBV 매집 ∧ RS20 > 0 ∧ vol_surge ≥ 1.2`, and **`vol_surge` cannot be satisfied on a 4.65%
bar except by an accident of pre-market print** — so the filter is gating on the stub, not on flow.
⇒ **An 8-sector absence today says nothing about those 8 sectors.** This is the same class as the
measured 2026-07-21 case where an Energy shortlist of 0 turned out to be a tag artifact while the
refiners were OBV-accumulating.
⚠ **In particular, Materials' absence is contradicted by Materials' own sweep row** (0 red of 12, best
5-day price breadth on the board) — which is the cleanest available proof that the absence is the
filter, not the sector.

★ **One shortlist name is worth flagging for its timing, not its score**: **`MRVL` appears on the
morning it reports** (`S116` brackets it, settles 08-28) — and it is exactly where **`C18`** lives:
today's FINRA read is **`z −0.64` ⇒ "✅저숏/숏커버"**, against `module_flow`'s 08-25 read of
**"4.8% float BUILDING"**. 🚫 **Neither instrument is graded highly enough to overrule the other and no
`⚡crowded-short` stamp is issued.** The contradiction is carried, not resolved.
🚫 **The `news` column is not used for any of the 5** (G1, §0).

---

## §5 · Invariant checks

- ✅ **Held-but-not-in-universe: 0.** All **11** US book names (`ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA
  PSX RTX`) are inside `us_top300` (n=300), verified at PREFLIGHT G5. **The desk can tag everything it
  holds.** ⚠ The universe file is **43 days old** — membership itself may be stale, so this is
  "everything held is in the *July 15* universe".
- ✅ **`CYCLE_EXPOSURE` GAP: none.** AI-compute (rank 1) epicenter **17.41%** vs need ≥12.0%
  (`NVDA`, `ANET`); Energy/refining (rank 2) **9.77%** vs need ≥8.0% (`MPC`, `PSX`). Missile-defense
  (rank 3) has **no threshold set** ⇒ ⚪ n/a, not ✅.
  🚨 **`D250`/`M731` reproduces for a 13th run**: `cycle_registry.json` still carries **no
  optical/interconnect cycle**, on a board where `COHR`/`LITE` sit inside `S128`'s reversal basket and
  where `MRVL` — an optical/interconnect franchise — is both in today's shortlist and reporting today.
  **A cycle with no registry row cannot produce a GAP flag**, so the ✅ above is a statement about the
  three cycles the registry knows, not about the book. **Handed to ALPHA.**
- ⚠ `cycle_exposure` reads the **REAL KIS account** (total ≈ $11,154, invested $5,258), not the paper
  book. The percentages above are of the real account and are **not** comparable to the paper book's
  weights. Stated, not reconciled (P4 — no sizing).

---

## §6 · IDs registered by this stage

> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`, excluding this
> run's own files: **`M987`–`M989` → 0 hits.** Highest before this append: `M986` (this run's MACRO).

- **`M987`** — the news-axis cap reproduces a 4th time, **inside this run's own sweep**: 50 covered
  names = `us_top300` ranks 1–50, contiguous.
- **`M988`** — this sweep's bar is a pre-market stub: median volume **4.65%** of the prior session,
  **2 of 300** names above 50%. 3rd consecutive run (`D355`).
- **`M989`** — DISC's flow-vs-price contradiction, logged as the board's widest `C5` gap for five
  consecutive runs, **has closed**: both instruments now read DISC as the soft end.

---

## ✅ EXIT CHECK
- [x] 🚨 `scoring` block read and quoted (§0) — `n_axes` 3 · `vel_coverage` 16.7% · `dropped_missing_axis` 0.
      The file states **"news axis dead this run"** and names the cause as **the pipe (a rank cap), having
      probed it twice** — including a fresh in-run reproduction, not an assumption.
- [x] **Every `top1_flips_sign` sector listed with its `top1` and `top1_w`** (§2), plus the full
      cross-stage diff showing which restrictions lifted and which attached.
- [x] **Held-but-not-in-universe check run** — 0 outside, with the universe's 43-day staleness stated (§5).
- [x] Sweep done → `SECTOR_FLOW_US.json`; sector ranking read; **new-🟢 declined with a measured reason**
      (stub bar, §0) rather than cited.
- [x] `US_LIVE_SHORTLIST.json` written; short-pressure verdicts read; the `news` column withheld by rule.
- [x] `CYCLE_EXPOSURE` GAP read; the registry's missing optical/interconnect row handed to ALPHA as a
      🚨 that the ✅ cannot cover.
- [x] **No table in this file exists in the JSONs** — the 11 sector rows and the 5 shortlist rows are
      cited by artifact; the only per-sector numbers reproduced are the specific figures that carry a
      cross-check argument.
- [x] **Five cross-checks stated, three confirming and two contradicting the MACRO matrix**, each naming
      which side the money is on; **the shortlist's absences are diagnosed as a filter artifact with the
      measurement that proves it.**
