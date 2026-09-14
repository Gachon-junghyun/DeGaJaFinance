# SWEEP_READ — industry_US · 2026-09-06 (Sun) · Stage 4 / L1·SWEEP

> **The reading, not a second copy of the data.** Sector rows, per-name rows and shortlist rows live
> in `SECTOR_FLOW_US.json §sector_rotation` / `§names` and `US_LIVE_SHORTLIST.json` and are **cited,
> not reprinted**. This file holds only what those JSONs cannot say.

## 0 · Instrument health line, read BEFORE the numbers

`scoring = { vel_axis: false · vel_coverage: 0.1672 (50/299) · n_axes: 3 · scored: 299 ·
dropped_missing_axis: 0 }` · `asof 2026-09-04`.

**Coverage 16.72% ≪ 80% ⇒ the news axis is DEAD in this run's score.** Cause **probed, not assumed**:
the falsification probe returned **6/6 alive before the sweep**, **0/4 immediately after**, dead at
t+20s/t+40s, **alive at t+60/+80/+100s** (identical count 3841). ⇒ **the pipe, not the market** — and
specifically **this desk's own burst**, which trips the tunnel at ~50 names / ~100 queries and then
keeps firing into a dead endpoint. **"Quiet" is not a permitted word in this run** (PREFLIGHT G1).

⚠ **The Δ column is the `09-03 → 09-04` change and today's `asof` equals the 09-05 run's** — nothing
here is a move that happened since the last report (PREFLIGHT G2).

## 1 · Universe headline — three numbers

**n = 299 · `wflow` −0.153 · 11 🟢 / 92 🔴** (196 🟡). Against the 09-05 run: **10 🟢 → 11 🟢**, reds
unchanged at 92, on **identical settled data**. That one-name difference is §2's finding.

## 2 · 🚨 The finding: **the 🟢 tag is on a different scale from `flow_score`, and only 50 names can reach it**

This run and the 09-05 run read the **same** settled session (`asof 2026-09-04`) and produce an
**identical** 11-sector table on all nine fields. **The per-name tags are not identical.** `PG` moved
**🟡중립 → 🟢가속** with:

| field | 09-05 | 09-06 |
|---|---|---|
| `flow_score` | 0.231 | **0.231** |
| `obv_norm` | +0.124 | **+0.124** |
| `vol_surge` | 0.89 | **0.89** |
| `rs20` | +0.8 | **+0.8** |
| universe position | 33 | **33** |
| **`velocity`** | **1.13** | ★ **1.26** |

**Every scored axis is byte-identical. Only the news velocity moved — in a run where `vel_axis` is
`false` and `n_axes` is 3.** ⇒ **`flow_score` correctly drops the velocity axis; the TAG does not.**

★★ **And the tag's news leg is reachable by 50 names out of 299.** Velocity exists for universe
positions **0–49 only** (contiguous, zero exceptions — the tunnel wall). So:

| | count | share |
|---|--:|--:|
| universe inside the velocity-eligible prefix | 50 / 299 | **16.7%** |
| **🟢 greens inside that prefix** | **4 / 11** | ★ **36.4%** — 2.2× the base rate (expected 1.8) |
| 🔴 reds inside that prefix | 14 / 92 | **15.2%** — the base rate, within noise |

**The leg only PROMOTES. It never demotes.** That is the identical asymmetry the `scoring` block was
built to kill after it inflated every score by +0.305 — **reappearing in the tag instead of the score.**

★ **The mechanism is visible in the composition.** The four prefix greens are the ones with *weak*
non-news axes — `PG` (surge 0.89, OBV +0.12, rs20 +0.8: three failing legs) and `CVX` (surge 0.99,
below the 1.2 gate) are 🟢 **only because a velocity was available to them**. Every one of the seven
non-prefix greens carries **`vol_surge` ≥ 1.21**: with no news leg available, they had to clear the
volume gate on merit.

⇒ **`M1369`** [measured] · **`D537`**: *`flow_tag` reads an axis `flow_score` has dropped, and that
axis is structurally available to only the largest 50 names, so the 🟢 label is systematically easier
to earn the larger the company.* ★ This is an **independent US reproduction of `M1328-KR`** (the KR
desk measured the same truncation reaching `flow_tag` this morning, on a different universe with a
different constant) — **the structure is confirmed twice across two markets; neither number is
imported** (`W1`).

⚠⚠ **This partially refutes this run's own PREFLIGHT.** `G2` concluded "today's sweep contains zero
new market information" on the basis of an 11-sector × 9-field comparison. **That comparison was
complete for the sector table and did not cover the per-name tags, where one name did change.** The
`G2` sentence stands in `PREFLIGHT.md` and this is appended, not substituted (`§4c` / `D48`).
The corrected form: **zero new *market* information, one new *instrument* artifact.**

## 3 · Cross-checks against the MACRO matrix — **one confirmation, one contradiction**

**✅ CONFIRMS §E row 1 (Energy OW), on an instrument the matrix does not use.**
`SLB` clears the 🟢 gate at universe position **173 with `velocity = None`** — i.e. it earned the tag
with **no news leg available at all**, on `vol_surge` 1.39 / OBV +0.439 / rs20 +14.2 — and
`us_live_shortlist` independently classes it **✅ 저숏/숏커버 (clean rise)** on `[FINRA]` z **−1.21**.
Three instruments that do not share an input (flow axes, short volume, news) agree on the sector's
#1 name. ★ **This matters specifically for `P139`**: `SLB` is a named Venezuela beneficiary and its
signal is **not** a news artifact. ⚠ **`CVX`, the other named beneficiary, IS partly a news artifact**
(§2) — its **tag** is contaminated, its **`flow_score` 0.661 is not** (3-axis, velocity excluded).
`P139` is written on the flow score and the news chain, not on the tag; stated so it is checkable.

**🚫 CONTRADICTS the matrix's use of breadth for Utilities, and the money is on the sweep's side.**
§E row 5 reads Utilities as *"breadth 0.00 ⇒ a few names, not a sector."* Breadth 0.00 means **zero
🟢**, and §2 shows the 🟢 gate is not a clean instrument. Direct measurement: **28 of 299 names carry
`flow_score` > 0.5 AND `obv_norm` > +0.15 AND `rs20` > 0 and are excluded from 🟢 *solely* by
`vol_surge` < 1.2** — **2.5× the number the gate admits.** In Utilities those two names are
**`CEG` (surge 0.96, OBV +0.19, rs20 +11.2)** and **`VST` (surge 1.02, OBV +0.21, rs20 +6.6)** — the
exact merchant-power pair `M1316` identifies as the sector's only positive-`rs20` names.
⇒ **Utilities' breadth 0.00 does not mean nothing in Utilities is accumulating. It means the two
things that are, print below a volume threshold.** ROTATION may not read that zero as evidence.

⚠ **`vol_surge` is the axis this desk's own KR `ic_ledger` scores at IC −0.0414, t(NW) −3.61, n_eff
45 — clearing Bonferroni NEGATIVE for a 4th consecutive run — while this gate weights it POSITIVE**
(`C29`). §2 and §3 are now the **third and fourth** legs of that contradiction. **Authority is a human
call (P5)**; the US instrument is `S145`, settling 09-11.

Surge-suppression by sector (count of names meeting all three merit conditions but blocked):
**HLTH 8 · ENRG 7 · IT 5 · FIN 4 · STPL 2 · UTIL 2 · all others 0**, against greens of
1 / 3 / 1 / 1 / 1 / 0. ★ **Health Care is the most suppressed bucket on the board** — 8 blocked
against 1 green, which is the same object `M1318` measured from the other side (22 of 32 accumulating,
1 green).

## 4 · Shortlist composition — the ABSENCES, each diagnosed

11 names pass (`mcap ≥ $10B` · tag 🟢 · flow desc top15) — see `US_LIVE_SHORTLIST.json`.

| sector | shortlist names | diagnosis of the absence |
|---|--:|---|
| **Utilities** | **0** | 🚨 **FILTER ARTIFACT, not evidence.** `CEG` and `VST` meet every merit condition and are blocked by `vol_surge` alone (§3) |
| **Real Estate** | **0** | ✅ **EVIDENCE.** Its four best names are OBV 매집 (`WELL` +0.17 · `AMT` +0.17 · `DLR` +0.14 · `VTR` +0.10) **but their `flow_score` tops out at 0.360** — genuinely below the gate on the non-news axes, not suppressed by one leg. 11 of 12 negative on `exc5` agrees |
| **Comm. Services** | **0** | ✅ **EVIDENCE, with a caveat.** `WBD` (+0.49), `META` (+0.47), `T` (+0.41), `VZ` (+0.39) are **all 매집 with positive `rs20` (+4.6 to +8.3)** — but all four score below 0.5, so this is not the `vol_surge` artifact. ⚠ The caveat is `D459`: this is the bucket the desk cannot aggregate at all |
| **Industrials** | 2 (`DE`, `RSG`) | ⚠ **Two greens out of the board's WORST sector** (`eqflow` −0.354, 33/50 negative on `exc5`). Both cleared on merit (`velocity = None`, surge 1.44 / 1.22). The `UW` and the two greens are both true and the matrix says so |
| **Energy** | 3 (`SLB`, `WMB`, `CVX`) | The board's only multi-name 🟢 cluster, and the only sector where the shortlist and the matrix agree without qualification — ⚠ **except `CVX`'s tag** (§3) |
| Health Care | 1 (`MDT`) | ⚠ `MDT` is the sector's only green **and it sits in the sector's WEAK node** (Equipment, `eqflow` −0.044) — carried from `M1319`, unchanged |

★ **The composition finding: 4 of 11 shortlist names come from sectors the MACRO matrix rates `UW`
or `N−`** (`DE`, `RSG` from INDU-UW; `TSLA` from DISC-UW; `CTVA` from MATR-N−). **A shortlist built
from flow does not respect the matrix's wind direction, and that disagreement is the point of running
both** — ROTATION owns the reconciliation, not this stage.

## 5 · Held-but-not-in-universe check

✅ **All 11 US book holdings are in `us_top300.csv` (300 rows). Missing: 0.** (PREFLIGHT G5 coverage
leg; the two KR holdings are out of scope by design.) 🔴 **The file is 53 days stale** (mtime
2026-07-15, bar ≤8) — so every weighted number this run rests on a seven-and-a-half-week-old cap
vector, and `eqflow` is the citable cut wherever the two disagree.

## 6 · Cycle-exposure GAP

`cycle_exposure` on the **real KIS book** (total ≈ **$11,022**, invested **$5,255** ⇒ **52.3% cash**):
✅ **no GAP.** AI-compute epicenter **17.48%** (bar ≥12%, holds `NVDA`/`ANET`) · Energy/refining
**10.47%** (bar ≥8%, holds `MPC`/`PSX`) · missile-defense 3.64% (no bar set). **Nothing is handed to
ALPHA's action bracket from this leg.**
⚠ Carried unchanged from `M1308`: **the AI-power cycle is not in `cycle_registry.json` at all**, so
its absence reads as ✅ rather than as a GAP, and the book's only lane exposure is `ETN` — the lane's
one distributing name (`D416`, `S146` settles 09-14). **A registry that cannot see a cycle cannot
flag a gap in it.**

---

> P4 — analytical only. No sizing, no buy/sell language. The 🟢/⚡/✅ marks are instrument states
> (short pressure, flow tags), not recommendations, and §2 is an argument that one of them is
> currently unreliable.
