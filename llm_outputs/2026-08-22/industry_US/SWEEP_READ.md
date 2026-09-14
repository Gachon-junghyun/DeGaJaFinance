# SWEEP_READ — industry_US · 2026-08-22 (Sat) · Stage 4 / L1·SWEEP

> **The reading, not a second copy of the data.** Numbers live in `SECTOR_FLOW_US.json` ·
> `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.json` and stay on disk all run. Sector rows and
> shortlist rows are **not reprinted here** (2026-07-21: 100% of tickers / 97% of numbers were
> restatement). This file exists to feed ROTATION §2. `asof` **2026-08-21**, settled.

## 0 · 🚨 Instrument health line — read BEFORE the numbers

`§scoring` = `vel_axis false · vel_coverage 0.0 · n_axes 3 · scored 299 · dropped_missing_axis 0`.

**Coverage is exactly ZERO, and that is the best case, not the worst.** `dropped_missing_axis = 0`
confirms all 299 names were scored on the **same** three axes, so none of the four 2026-08-09 defects
is live: no per-name axis drop, no `clip(nan) = +1.0`, no scope error, and — because coverage is 0
rather than partial — **no selection bias in the tag layer either** (`PREFLIGHT_US ③` + its
correction). **A low `vel_coverage` is evidence about the pipe, not about the news**, and today's
pipe mechanism is measured: a ~100-call budget with a ~90 s cooldown.

⇒ **Nothing in this file cites news velocity, theme freshness, or any absence claim from the sweep.**
Tags **are** citable today and are read as **3-axis unanimity** (`obv매집 ∧ rs20>0 ∧ vol_surge≥1.2`).

## 1 · Universe headline — three numbers

**n = 299 / 300** (`EA` unmeasurable, 10th run) · **wflow −0.076** · **🟢 6 / 🔴 71**, breadth **2%**.
⚠ `wflow` carries **38-day-old cap weights** (`G5`) and decides nothing below.

## 2 · Cross-checks against the MACRO matrix — where the money agrees, and where it does not

**The board is unusually coherent this run. Nine of eleven sectors rank within two places of each
other on price (`exc5` vs `SPY` −1.368%) and flow (`eqflow`). Two do not, and both are informative.**

| Contradiction | The measurement | Which side the money is on |
|---|---|---|
| 🚨 **Real Estate — the largest rank gap on the board** | `exc5` **rank 6 (+0.948)** vs `eqflow` **rank 10 (−0.446)**, gap **4 places**, **0🟢 / 6🔴 of 12** | **Flow.** And this run it is not a judgement call: `S90` **FIRED-A** — the registered falsifier of the 08-21 price-only promotion. MACRO took RE **N− → UW** on it |
| 🚨 **Information Technology — the price is worse than the flow, not the reverse** | `exc5` **rank 11 (−2.158, worst)** vs `eqflow` **rank 8 (−0.102)**. **`eqflow − wflow` = +0.129, the widest positive gap on the board** | **Flow is the less-bad half.** ⇒ this is **not** a broad IT distribution; it is **mega-cap-led weakness**. `P79` (−5.609, moved 1.57pp *away* from branch B) says the same. ⚠ Pair with `Nasdaq-100` spec at the **4th %ile** `[COT 08-18]` — **context, not a trigger (`D6`)** |
| ⚠ **Consumer Discretionary — flow rank 2 with ZERO greens** | `eqflow` **+0.103 (rank 2)** · `breadth` **0.00 of 28** · `exc5` rank 5 | **Neither, cleanly.** A positive equal-weight flow with **not one name clearing the 3-axis gate** means the sector is *broadly mildly positive and nowhere ignited*. MACRO's **N** is the honest expression |
| ⚠ **Energy — OW #2 on both axes with ZERO greens** | `exc5` **+4.162 (rank 2)** · `eqflow` **+0.102 (rank 3)** · **breadth 0.00 of 16** — and it was 1🟢 on 08-21 | **Flow, but see §3.** The zero is a **filter artifact, diagnosed below**, not evidence of absence |
| ✅ **Health Care — both axes rank 1, and the same caveat as the matrix** | `exc5` **+5.700** · `eqflow` **+0.229** · breadth **0.03 (1🟢 of 32 — `MRK` alone)** | **Both agree.** The price is thin under the flow, and both stages say so |
| ✅ **Utilities — both axes bottom** | `exc5` rank 10 · `eqflow` **−0.621 (rank 11)** · **0🟢 / 13🔴 of 15** | **Both.** Third run as the worst flow on the board; `C12` still carries no mechanism |
| ✅ **Industrials — both axes rank 9** | `eqflow` **−0.231** · **0🟢 of 50** | **Both** |

★ **Breadth-led vs mega-cap-led, stated once because ROTATION needs it:** `eqflow > wflow` in
**7 of 11** sectors — widest at **IT +0.129**, **RE +0.097**, **Staples +0.061**. `eqflow < wflow` in
four — widest at **Financials −0.037**. ⇒ **The board's weakness is concentrated in its largest names,
not in its breadth**, in every sector except Financials.
⚠ **Consumer Staples inverts sign across the two**: `wflow` **−0.013** vs `eqflow` **+0.048**. That is
the G3 flipper (`WMT`, 28.9%) seen from the other side, and it is why **`wflow` may not decide that
line**.

## 3 · Shortlist — read the ABSENCES, and diagnose them before citing them

**6 names of 299 clear the filter** (mcap ≥ $10B ∧ 🟢 ∧ top-15 flow). **Five sectors that MACRO ranks
positively produced ZERO**, and the important one is Energy.

🚨 **The Energy zero is a `vol_surge` artifact, and it reproduces the 2026-07-21 finding exactly.**
The four best Energy names are **all OBV-accumulating with positive `rs20`** — `PSX` +0.728 (surge
1.11), `MPC` +0.700 (1.06), `COP` +0.694 (1.05), `VLO` +0.506 (0.71). **Every one is blocked by the
volume axis alone.** ⇒ **"Energy has no live names" is a false sentence and is not written anywhere in
this run.**

**The general form, measured across the whole universe — `M144`/`M25`, 12th measurement and the
cleanest yet, because today the tag layer has no news contamination to argue about:**

| Test | Count |
|---|---|
| Names passing **`OBV 매집 ∧ rs20 > 0`** | **94** |
| Of those, tagged 🟢 | **6** |
| **Blocked — and 100% of them on `vol_surge` alone** | **88** |
| Names clearing `vol_surge ≥ 1.2` | 22 |
| …of which **not** 🟢 | **16** |

⇒ **The US 🟢 tag is a volume gate.** 88 of the 94 names that are OBV-accumulating **and** carry a
positive `rs20` **vs `SPY`** (the benchmark the sweep computes RS against — named inline, `C1`) are
excluded by a single axis — **and that axis is the one measured at `t(NW) −3.86` (h=1) and `−3.38` (h=5) in the KR
`ic_ledger`**, i.e. **negatively** related to forward returns. 🚫 **`W1` bars this desk from acting on
a KR-measured result** (`HANDOVER §6`), so this is written as the sharpest available statement of the
open question, not as a verdict: **the shortlist's gate and the only axis with a measured sign point in
opposite directions, and the US desk cannot yet tell which is right.**

**Other absences, one line each:** Industrials 0 of 50 · Consumer Discretionary 0 of 28 ·
Communication Services 0 of 12 · Real Estate 0 of 12 · Utilities 0 of 15. **For RE and Utilities the
zero is corroborated by `eqflow` (−0.446, −0.621) and is a real reading.** For Industrials and
Consumer Discretionary it is the same `vol_surge` gate as Energy and is **not** cited as evidence.

★ **What the shortlist did find is worth one line**: its only "clean rise" (🟢 with low/covering short)
is **`MSTR`, short-z −1.23** — and `COIN` sits beside it at flow **+1.000**. **Two of the six greens
are the same crypto tape** that §B-2 of MACRO measured at 12 outlets and +20–25% on the week.
**Financials' single green is not a bank.**

## 4 · Cycle exposure — no GAP, for the first time in this file's recent history

`CYCLE_EXPOSURE.json`, real KIS book (read-only): **AI-compute rank 1 — epicenter 16.52% vs a 12.0%
floor ✅** (`NVDA`, `ANET`) · **Energy/refining rank 2 — 9.84% vs 8.0% ✅** (`MPC`, `PSX`) ·
Missile-defense rank 3 — 3.79%, **no floor set ⚪**.
**Verdict: no top-rank cycle GAP.** The 2026-07-14 failure mode (zero exposure to the #1 cycle's
epicenter) is not present.

⚠ **Two standing caveats travel with that ✅ and neither is closed:**
1. **`D250`/`M731` — `cycle_registry.json` still has no row for optical/interconnect**, so the
   registry cannot flag a gap there **by construction**. `S86` and `S96` both settled branch **B** this
   morning while `Fabrinet` guided *"AI optical demand fueling years of growth"* (5 outlets, 08-21).
   **A cycle the desk cannot measure is showing a price-vs-fundamental split — routed to ROTATION.**
2. **Rank 3 has no floor**, so `RTX` at 3.79% is `⚪ n/a`, not `✅`. **An unset threshold is not a pass.**

## ✅ EXIT CHECK
- [x] `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.md`/`.json` all written to
      the protocol's paths; sweep ran **before** the shortlist (the serial S1→S2 rule).
- [x] **`§scoring` health line read first** and its consequence stated: zero coverage, uniform axes,
      no news citation anywhere in this file.
- [x] Universe headline in three numbers; **no sector table and no shortlist table reprinted.**
- [x] **Cross-checks against the MACRO matrix stated as confirmations and contradictions**, with the
      side the money is on named for each — including the one verdict change (RE) and its scored
      bracket.
- [x] **Absences diagnosed before being cited**: the Energy zero is a `vol_surge` filter artifact
      (94 → 6, 88 blocked on that axis alone), and no "no live names" claim is made for it.
- [x] **Held-vs-universe invariant checked**: 11/11 US book names in `us_top300` and scored; `EA` is
      the only universe hole and is labelled **unmeasurable, 10th run** — never "no signal".
- [x] `asof` **2026-08-21** stated; the US market has not traded since, so no same-day catalyst sits
      outside these numbers.
