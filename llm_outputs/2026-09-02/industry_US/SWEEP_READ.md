# SWEEP_READ — industry_US · 2026-09-02 (Wed) · Stage 4 / L1·SWEEP

> **The reading, not a second copy of the data.** The numbers live in `SECTOR_FLOW_US_REPAIRED.json`
> and `US_LIVE_SHORTLIST.json` and are **cited, not reprinted** (no sector rows, no per-name rows).

## 0 · 🚨 Instrument health line — read before any number below

`SECTOR_FLOW_US_REPAIRED.json §scoring`: **`n_axes` 3 · `vel_coverage` 0.0 · `scored` 298 ·
`dropped_missing_axis` 0**, asof **2026-09-01**, `mode` `nonews`.
Primary `SECTOR_FLOW_US.json §scoring`: `n_axes` 3 · **`vel_coverage` 0.1711 (51/298)** ·
`scored` 298 · `dropped_missing_axis` 0.

🚨 **The news axis is DEAD this run, and the cause is the PIPE, not silence — probed, not assumed.**
PREFLIGHT G1 ran ten names at 1.5s spacing (**7 of 10 returned `None`**) and the **same seven** at 9s
spacing minutes later (**7 of 7 returned real velocities**: `CRM` 2.07 · `MDT` 1.87 · `WMB` 1.86 ·
`AVGO` 1.35 · `NEM` 0.81 · `APP` 0.63 · `TER` 0.34). Headline probes were **6/6 pre-sweep** and
**4/4 post-sweep**. ⇒ **the sweep's 300-query burst rate-limits itself**; 247 of 298 names were never
counted, and none of them may be described as quiet.

🚫 **The primary file's OBV axis is revoked** (PREFLIGHT G0: 259 of 298 scored names carry two
sessions zeroed out of a 20-session OBV window; 17% label-flip rate on the 42-name control). Every
number below is the **repaired** file. **Δ is direction-only** — its 08-31 baseline is yesterday's
holed primary snapshot.

## 1 · Universe headline — three numbers
**n 298 · `wflow` −0.197 · 🟢 6 / 🔴 99.**

## 2 · `top1_flips_sign` — the list ROTATION may not promote or demote on

- **Repaired (citable): 1 of 11** — **Consumer Discretionary**, `top1` **AMZN**, `top1_w` **40.2%**,
  −0.286 → **+0.033**.
- **Primary: 2 of 11** — adds **Consumer Staples**, `top1` **WMT**, `top1_w` **28.9%**.
  ⇒ **the two instruments disagree about Staples, so its sign is established by neither.**
- ★ **The guard misses the largest case entirely.** Alphabet is **76.6%** of Communication Services
  under **two** tickers (`GOOGL` 38.3% + `GOOG` 38.3%); the guard removes one **row**, prints
  `top1_flips_sign: False`, and ex-both-classes `wflow` is **−0.506 → +0.257** (swing **0.763**).
  ⇒ **ROTATION is barred from a `wflow` verdict on Comm. Services in either direction** (`D459`,
  2nd reproduction, larger than at registration).

**Handed to ROTATION: Cons. Disc. · Cons. Staples · Comm. Services — no `wflow` promotion or demotion.**

## 3 · Held-but-not-in-universe — ✅ invariant holds, and it surfaced something else

Real KIS book read live (`fetch_overseas_balance`, read-only): **9 US positions, $5,158 invested**.
**All 9 are in `us_top300.csv` — 0 missing.** The `TSM`/`LNG` failure class does not reproduce.

⚠ **But two positions carry no thesis in the analytical carry**, and only one of them was known:
`T` **13.8%** of invested capital (carried as an open gap since 09-01) and — **new this run** —
**`CBRE` 2.8%**, which appears in no `STANDING_VIEW_US` §3a row, no scenario, and no ledger.
⇒ **16.6% of real invested capital is unowned by any thesis.** Recorded here as a **`missed`-class
observation, not filed** — a miss row would mis-file positions already owned (the same reasoning the
09-01 run applied to `T`). Assigning theses is a human call (P5).
⚠ **`PSX` is 14.7% of the real book and sits at `vol_surge` 0.99** — see §5.

## 4 · Cross-checks against the MACRO matrix — where the money confirms, and where it contradicts

| MACRO §E line | flow says | verdict |
|---|---|---|
| **Energy OW** (exc1/5/20 all best on the board) | `eqflow` **+0.551** — the board's only strongly positive sector — **and the best Δ (+0.295)**; breadth **0.12**, the only non-trivial breadth on the board | ✅ **CONFIRMS, on the one sector where every instrument agrees** |
| **Industrials UW** (worst exc5 and exc20) | `eqflow` **−0.447**, Δ **−0.222**, breadth **0.00** | ✅ **CONFIRMS** — the most internally consistent negative |
| **Utilities UW** | 🚩 **CONTRADICTS**: Δ **+0.267**, the board's 2nd-best, and exc1 **+1.47**, the board's 2nd-best — against exc20 **−2.28** | ⚠ **The money is on the CONTRADICTING side over 1 session and on the matrix's side over 20.** `P127`'s dated falsifier (Texas "ghost demand", 6 outlets) and its dated confirmer (gas-turbine reignition, 5→3→8) sit on opposite sides of exactly this. **Unresolved and handed to ROTATION as unresolved** |
| **Materials N, contested** | Δ **−0.208** (2nd-worst) while `NEM` turns 🟢 with `[FINRA]` z **−3.14** | 🚩 **Split** — the sector's Δ and its best name point opposite ways; `C24` (copper spec 100th %ile) is the 4th reproduction |
| **IT N**, "the label is two bets" (`XLK` +1.58 vs `SMH` −1.37 on exc5) | `eqflow` **−0.252** with breadth **0.02** — 1 green (`CRM`) of 55 | ✅ **CONFIRMS the split reading**, and adds that the *breadth* side is uniformly weak whichever half you take |
| **Health Care OW−** | `eqflow` **+0.265**, Δ **+0.214**, **2 of the 6 greens** (`A`, `MDT`) | ✅ **CONFIRMS**, and it is the only OW besides Energy the shortlist reaches |
| **Comm. Services** — no verdict issued | `eqflow` **−0.013** = flat | ✅ the flow file agrees there is nothing to verdict on `wflow` |

★ **The one cross-check that matters most:** **`eqflow` is below `wflow` in 8 of 11 sectors**
(Energy and Health Care are the exceptions, Comm. Services is the inverse case). ⇒ **this is not a
breadth-led tape; it is a mega-cap-supported tape with a weak middle**, which is the same shape the
`RSP − SPY` exc5 of **−1.35pp** prints independently.

## 5 · Shortlist composition — the ABSENCES, diagnosed before being cited

`US_LIVE_SHORTLIST.json`: **6 names**, from **4 sectors** (Energy · Health Care · Materials · IT).
**7 of 11 sectors produced no name**: Financials · Industrials · Utilities · Real Estate ·
Cons. Disc. · Cons. Staples · Comm. Services.

🚩 **Diagnosed as a FILTER ARTIFACT, not as evidence — measured, not asserted.**
- **102 of 298 names are OBV-accumulating AND beating `SPY` over 20 sessions.** Of those, only **19**
  clear `vol_surge ≥ 1.0` and only **6** earn 🟢.
- Universe-wide the gate is the binding axis: mean clipped **OBV −0.132 · RS20 −0.042 ·
  SURGE −0.269**, with **54 of 298** above `vol_surge` 1.0 and a **median of 0.81**.
- With the news axis dead the 🟢 tag needs **3 of 3** price axes (`M1188` — the ceiling falls from 4
  to 3, so the gate silently becomes **unanimity**). **6 greens is a floor produced by a dead pipe,
  not a level.**
- The near-miss band (`0.85 ≤ vol_surge < 1.0`, OBV > 0, `rs20` > 0) spans **all 11 sectors** and
  contains **`CVX` 0.99 · `PSX` 0.99 · `WELL` 0.99 · `EOG` 0.98 · `OKE` 0.97 · `TSLA` 0.96 ·
  `LLY` 0.94 · `COP` 0.92 · `TGT` 0.91 · `ED` 0.91 · `ECL` 0.91 · `AJG` 0.90 · `KO` 0.90 ·
  `ADBE` 0.87**.
- ★ **`C5` reproduces on a held name this time**: **`PSX` misses the gate by 0.01** and is **14.7% of
  the real book**. Yesterday the 0.01 name was `NEM`, which crossed the gate today and is now the
  shortlist's cleanest row. **A threshold that reorders the board on 0.01 is reporting its own
  arbitrariness, not the tape.**

⇒ **No sector may be described as "quiet" or "empty" from this shortlist.** The absence of Energy
names beyond `SLB`/`WMB` is the 2026-07-21 refiner artifact reproducing: **`CVX`, `PSX`, `EOG`, `OKE`
and `COP` are all accumulating and outperforming, and all are tag-filtered.**

**Composition of the 6, by short-pressure verdict** (cited from the JSON, not reprinted): 2 are
**✅ clean-rise** (low-short / short-cover) — **`NEM` z −3.14** and **`WMB` z −3.08**, the board's two
most extreme short exits — and 4 are **△ normal**. **0 crowded-short.** ⚠ US has no investor-type
feed; FINRA short-z is a proxy and includes market-maker hedging (`D6`).

## 6 · CYCLE_EXPOSURE GAP

**✅ No GAP.** AI-compute (rank 1) epicenter **16.8%** vs a 12.0% floor (`NVDA`, `ANET`; `ETN`
adjacent, any-layer 20.35%); Energy/refining (rank 2) **10.3%** vs 8.0% (`MPC`, `PSX`);
missile-defense (rank 3) 3.75% (`RTX`, no floor set). **Nothing to hand to ALPHA's action bracket.**
⚠ `D416` still stands: **the AI-power cycle has no registry row**, so `P127`'s question — the one
sector cross-check that contradicted the matrix in §4 — **cannot be answered by this instrument at
all.** Sixth run.

---
> Artifacts: `SECTOR_FLOW_US_REPAIRED.json` (citable) · `SECTOR_FLOW_US.json` (primary, OBV revoked) ·
> `US_LIVE_SHORTLIST.json` · `../CYCLE_EXPOSURE.md` / `.json` (day-folder root, script-owned).
> Next: **EVENT_ALPHA** (Stage 5).
