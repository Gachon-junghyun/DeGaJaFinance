# SWEEP_READ — industry_US · 2026-09-12 (Sat) · Stage 4 / L1·SWEEP

> **The reading, not a second copy of the data.** Sector rows live in `SECTOR_FLOW_US.json
> §sector_rotation`; per-name rows in `US_LIVE_SHORTLIST.json`. Neither is reprinted here.
> Sweep ran 14:55 (`--json --refresh`, asof **2026-09-11 settled**); shortlist + cycle_exposure re-run
> 22:23 (serial, after the sweep). Saturday — no bar has changed since 14:55.

## 0 · Instrument health line, read BEFORE the numbers

`§scoring` = `{vel_axis: false, vel_coverage: 0.0, n_axes: 3, scored: 299, dropped_missing_axis: 0}`.

🚨 **The news axis is DEAD this run — 0 of 299 (0.0%) against an 80% bar — and the cause is the PIPE,
not silence.** Probed, not assumed: **0/8 queries answered 14:52 → 22:10 (HTTP 404 from the ngrok
host, not the idle-timer `URLError` of 09-05…09-08)**; local `news_alert.db` 0 bytes. The sweep logged
its own 🚨 line and scored all 299 on the same 3 axes (`dropped_missing_axis = 0`) — the scale is
continuous with 09-04 (`3 / nonews / 299`), so **Δflow is legal and it is the 09-04 → 09-11 weekly
change** (G2). No name and no sector is "quiet" from this file. **Every velocity cell is `n/a`**, and
the 🟢 tag can only have been unlocked by OBV (C-grade) — every 🟢 below is read as **🟡 with a stated
OBV-only conviction** (`D6`, `D11`).

## 1 · Universe headline — three numbers

**n = 299 · universe `wflow` −0.169 (from −0.153 on 09-04) · 🟢 5 vs 🔴 129 (25.8 : 1, from 11 vs 92 = 8.4 : 1).**
Red count +37 in a week in which `SPY` fell −0.77%: the flow axes (OBV/RS/surge) read the week as
**distribution-broad** — 129 of 299 tagged 🔴, 34 of them Industrials, 23 IT, 19 Discretionary.

## 2 · Cross-checks against the MACRO §E matrix — confirm / contradict

| matrix line | sweep says | verdict |
|---|---|---|
| **Energy OW** (`eqflow` +0.431 the only positive sector) | 15 of 16 names `OBV 매집` or 중립, **but 0 🟢 of 16** — every name 🟡 (`VLO` +0.37 rs20 +15.6 · `DVN` +0.44 · `MPC` +0.48 · `PSX` +0.32 · `COP` +0.31); only `KMI` 🔴 | **CONFIRMS the sign, and the absence of 🟢 is a filter artifact, not evidence** (the 2026-07 ENRG-0 precedent): with velocity `n/a`, 🟢 needs OBV 매집 **and** the score gate; the sector is OBV-accumulating across the board with `rs20` +4.5…+15.6 (A-grade RS agrees with C-grade OBV). `R143` check: `wflow` +0.470 vs `eqflow` +0.431, `XOM` 30.5% ex-top1 +0.486 — **not one name** |
| **IT N → N+ candidate on breadth** (EW exc5 +3.40, 40/56) | `eqflow` **−0.207**, 3 🟢 / 23 🔴, Δflow −0.012 | **CONTRADICTS on the flow axes.** The price tape ran +3.4pp vs `SPY` on 40 names while OBV/RS-60/surge still read distribution on 23. The 3 🟢 (`QCOM` 0.83 · `DELL` 0.79 · `HPE` 0.71) are all AI-hardware, the 23 🔴 are software/semis-equipment-heavy ⇒ **the sweep sees the two tiers MACRO §E described, and weights the losing tier more**. ROTATION: a promotion on breadth must say the flow axis disagrees (`S140`'s 30/56 → 40/56 is a 5-session count; `eqflow` is 60-session RS-heavy) |
| **Health Care N+ → N** (EW exc5 −3.18, 4/32) | `eqflow` +0.190 → **−0.059 = Δ −0.250, the board's largest drop**; 0 🟢 / 8 🔴; `LLY` 19.4% not a flipper | **CONFIRMS** — the flow axis fell with the tape, as a sector (breadth 0.0). Money is on the down side; `P150` armed |
| **Utilities N−** | Δflow **−0.340 (largest negative)**, 0/9 red, `eqflow` −0.273 | CONFIRMS the `S135`-A duration read — the trio fell together on flow too (RE Δ −0.203, STPL Δ −0.004 the exception: STPL flow flat while price fell) |
| **Financials N → N− candidate** | `eqflow` −0.269, Δ −0.170, 1 🟢 (`AIG` 0.62) / 14 🔴; `BRK-B` 13.9% not a flipper | CONFIRMS the demotion direction; the one 🟢 is an insurer, the reds cluster in exchanges/brokers/alt managers (matches MACRO §E's rates-split read) |
| **Industrials UW−** | `eqflow` −0.470 (worst), **34 🔴 of 50 (68%)**, 0 🟢 | CONFIRMS; the most distributed sector on the board on both axes |
| **Materials N−** | 0 🟢 / 6 🔴, `eqflow` −0.200 | CONFIRMS; nothing promotes |
| **Comm. Services — no verdict (G3)** | `eqflow` −0.054, **Δflow +0.241 (the board's largest positive)**, 1 🟢 = `META` (0.79, new) | ⚠ the largest positive weekly flow change on the board sits in the sector the desk cannot rank. Not a verdict (Alphabet 76.6% issuer flip); **handed to ROTATION as a named contradiction**: `eqflow` flat, `wflow` −0.148, Δ +0.241, `META` the only new-🟢 outside IT |
| **Staples UW (eqflow/breadth only)** | `eqflow` −0.059, flip **True** (`WMT` 28.9%: −0.186 → +0.023) | flipper listed; no promotion/demotion on `wflow` |

**`top1_flips_sign` buckets handed to ROTATION (may not promote/demote on `wflow`):**
**Consumer Staples — `WMT`, `top1_w` 28.9%** (built-in flag). Issuer-level (PREFLIGHT G3):
**Communication Services — Alphabet (GOOGL+GOOG), 76.6%**, −0.148 → +0.400 ex-issuer. All other 9: no flip.

## 3 · Shortlist — read the ABSENCES

`US_LIVE_SHORTLIST.json`: **5 names**, all 🟢, mcap ≥ $10bn: `QCOM` · `META` · `DELL` · `HPE` · `AIG`.
**New-🟢 this week: 4 of 5** (`QCOM`, `META`, `HPE`, `AIG`); `DELL` is the only survivor from 09-04's 11.
**Dropped from 🟢 since 09-04 (10)**: `MDT`, `DE`, `SLB`, `CTVA`, `TSLA`, `HOOD`, `WMB`, `CVX`, `RSG`, `PG`
— a **91% turnover** of the ignition list in one week; `HOOD` −7.8%, `SLB` −2.5%, `WMB` −1.8%, `CVX`
+2.6% on the week — the tag turned on three names that went *up* (`CVX`, `SLB` OBV still 매집), which
says the 🟢 gate is surge/RS-20-sensitive, not a trend tag.

**Absences, diagnosed:**
- **Energy: 0 shortlist names** — **filter artifact** (§2): 15/16 OBV-accumulating, `rs20` positive on
  14/16, all 🟡. The OW sector produces no "LIVE" name because the gate's news leg is dead and its
  surge leg did not fire on a +9% oil week (the equity leg lagged — `P149`). Cited as *cannot be
  tagged*, not as *no flow*.
- **Health Care, Utilities, Real Estate, Materials, Staples, Discretionary, Industrials: 0** —
  **evidence**, consistent with 🔴-heavy sector rows and negative `eqflow` in every one.
- **Financials: 1** (`AIG`, insurer, `rs20` +0.8, shortZ +1.36 = shorts building into it) — a weak 🟢.
- **IT: 3 of 5** — the AI-hardware tier (`QCOM` custom-silicon-for-Amazon thread `[titles 09-08]`,
  `DELL` ✅ low-short clean rise, `HPE` +19.4% on the week with shortZ +0.58). **The only ✅ "clean rise"
  on the board is `DELL`.**
- **Comm. Services: 1** (`META`).

**Held names (11) vs the sweep**: `NVDA` 🟡 · `ANET` 🔴 (shortZ +1.50) · `AVGO` 🟡 · `HPE` **🟢** · `ETN` 🔴 ·
`MET` 🔴 (shortZ **+1.95**) · `MPC`/`PSX` 🟡 rs20 +12.8/+13.3 with OBV 매집 · `NDAQ` 🔴 (−5.9% wk) · `NUE` 🟡 · `RTX` 🟡. All 11
in-universe and scored (G5 coverage PASS; freshness FAIL 59 d — cap shares not current).

## 4 · CYCLE_EXPOSURE (day-folder root, 22:23) — no 🚨 GAP
Registry rank 1 **AI-compute** epicenter **17.18%** (need ≥12%; `NVDA`, `ANET`) ✅ · rank 2 **Energy /
refining** **10.67%** (need ≥8%; `MPC`, `PSX`) ✅ · rank 3 missile-defense 3.59% (`RTX`, no bar set).
Book ≈ $11,003, invested $5,350 (read-only KIS balance). **Nothing handed to ALPHA's action bracket
from this file.** ⚠ G4: `ANET+ETN` are one measured unit at 500/750d — the "AI-compute" epicenter and
the "AI-power" leg are not independent exposures at those windows.

## ✅ EXIT CHECK — SWEEP
- [x] `scoring` block quoted; news axis **dead this run — pipe (404 ×8), probed 14:52/15:15/22:10**.
- [x] Flippers listed with `top1`/`top1_w` (STPL/`WMT` 28.9%; COMM/Alphabet 76.6% issuer-level).
- [x] Held-but-not-in-universe: **0 of 11** (PREFLIGHT G5); universe 59 d stale, stated.
- [x] Sweep → `SECTOR_FLOW_US.json` (asof 09-11); ranking + new-🟢 (4) read.
- [x] `US_LIVE_SHORTLIST.json` written (5; ✅ `DELL` only).
- [x] `CYCLE_EXPOSURE` read — no GAP.
- [x] No JSON table reprinted; absences diagnosed (Energy = artifact; the rest = evidence).
- [x] Cross-checks: Energy/HLTH/UTIL/FIN/INDU **confirm**; **IT contradicts** (tape +3.4pp on 40/56 vs `eqflow` −0.207); COMM Δflow +0.241 named for ROTATION.

> P4 — no buy/sell language; 🟢/✅ are instrument tags, not calls.
