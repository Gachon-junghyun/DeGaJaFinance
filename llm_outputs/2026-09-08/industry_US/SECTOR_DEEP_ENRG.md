# SECTOR_DEEP_ENRG — Energy · industry_US · 2026-09-08 (Tue) · Stage 8 / L1·DEEP

> **CONTINUOUS TRACK** (deep-dived 09-07, 09-06, 09-05, 09-02 …) ⇒ **leads with the DELTA.**
> Unchanged structure is carried **by reference** to `llm_outputs/2026-09-07/industry_US/SECTOR_DEEP_ENRG.md`.
> ⚠ Declared runtime constraint: the four DEEP sectors were written **serially and in-context**, not as
> a parallel agent fan-out (this session's harness forbids spawning subagents unattended). Stated, not hidden.
> All price numbers filtered to `index <= 2026-09-04` (`D577` — a partial 09-08 bar appeared mid-run).

## 0 · Mandate from ROTATION — one question

*"EVENT_ALPHA Card 2 says the scarce asset is refining CAPACITY (IEA: 9.6 mb/d destroyed, record-high
margins, record-low inventories) while carried `M1361` says the distillate crack's 3-session rate is at
the **6.0th percentile**. `D565` shows the sign flips with the window. **Which cut is the sector's
actual driver, and does `P140`'s 5-session leg measure it?**"*

## ★ 1 · The answer, measured — and `M1361` was quoting 1 of 4 windows

Distillate crack = `HO=F` × 42 − `CL=F`, settled closes to **2026-09-04**, percentiles against its own
trailing 252:

| window | change | percentile of 252 |
|---|--:|--:|
| **level** | **$99.21** | ★ **95.6th** |
| 3-session | **−$7.02** | 🔻 **6.0th** ← *the only figure `M1361` carries* |
| 5-session | −$0.37 | **45.6th** ← *the window `P140` actually settles on* |
| 20-session | **+$13.49** | **77.8th** |
| 60-session | **+$37.51** | ★ **91.3rd** |

⇒ **The rate is negative in exactly one of four windows, and it is the shortest one.** At 20 and 60
sessions the *rate* sits at the 78th and 91st percentiles — i.e. the crack has been **accelerating**,
not decelerating, on every horizon a quarterly earnings cycle can feel. **`M1361`'s 3-session figure is
not wrong; it is unrepresentative, and it has been carried alone for five runs.** `D565` is confirmed
and sharpened: this sector's own driver **changes sign with the window**, so any crack claim must state
its window on the same line.

**And `P140` is measuring the right thing.** It settles on the **5-session** leg (45.6th percentile =
genuinely mid-pack), not the 3-session one. ⇒ the row is well-constructed and **this stage does not
touch it** (`D242`).

## ★ 2 · The product-mix split is the mechanism, and it is visible in the futures arithmetic

| crack | level (pctile) | 5-session change (pctile) |
|---|---|---|
| **distillate** | $99.21 — **95.6th** | −$0.37 — **45.6th** |
| **gasoline** | $43.53 — 68.7th | 🚨 **−$19.64 — the 0.0th percentile of 252** |

**The gasoline crack just printed the single worst 5-session move in its own year while the distillate
crack barely moved.** That is not two independent facts — it is the **arithmetic footprint of the
behaviour Card 2's body-read described**: *"refiners have prioritized diesel fuel production, which
means they are making less fuel oil"* (and less gasoline), with *"record-low gasoline and diesel
inventories"* and a shipping-fuel shortfall of **218,000 b/d this quarter vs 6,000 b/d in 2025**
[Energy Aspects via Reuters, 09-07, body-read].

⇒ **The sector's driver is a MIX constraint inside a capacity constraint**, not a barrel price. The
binding node is the **distillate hydrotreater / coker**, not the wellhead — which is `R135`'s surviving
half (*"the scarce asset is the COKER, not the barrel"*), now with the crack arithmetic behind it
instead of a single VLO quote.

## 3 · Flow — node decomposition (sector row by reference to `SECTOR_FLOW_US.json §sector_rotation`)

Sub-node equal-weight flow, `n`, and 5-session excess median vs `SPY` (benchmark named inline, `C1`):

| sub-node | n | eqflow | exc5 median | 🟢 |
|---|--:|--:|--:|--:|
| **Refining & Marketing** | 3 | ★ **+0.715** | ★ **+5.10** | 0 |
| Equipment & Services | 2 | +0.596 | +0.92 | 1 (`SLB`) |
| E&P | 5 | +0.578 | +1.39 | 0 |
| Storage & Transportation | 4 | +0.518 | +0.53 | 1 (`WMB`) |
| Integrated | 2 | +0.344 | +2.44 | 1 (`CVX`) |

★ **Refining is the top node on BOTH axes and holds ZERO greens.** `MPC` (+0.694), `VLO` (+0.700) and
`PSX` (+0.750) are all **🟡 with OBV 매집** and `rs60` **+41.5 / +37.5 / +34.2** — the sector's three
strongest relative-strength readings sit in the node the tag never turns green. Per `D561` that is the
expected behaviour (none of the three carries a `velocity`; all three are outside universe rank 52), so
**the 🟡 is an instrument state, not a flow verdict** — stated on the line as required.

**Dispersion / sector-move = 1.737 / 1.894 = 0.92×** — ★ **the only sector on the board below 1.0**
(`D566` measured IT 4.6×, HLTH 3.0×, UTIL ≈23×). ⇒ **Energy is the one bucket where a sector-level
statement is admissible**, because the names move together relative to the size of the move. That is
the quantitative form of "this is a real sector, not a label", and it is why this desk's only
unambiguous OW is here.

## 4 · The DELTA vs the 09-07 file — what is new, what is carried

| | |
|---|---|
| **NEW ①** | The **crack window table above**. The 09-07 file carried `M1361`'s 3-session figure with a warning; this run **measured all four windows and the level**, and the warning becomes a correction |
| **NEW ②** | The **gasoline-crack 0.0-percentile print** — a fact no prior file has, and the one that turns "refiners prioritize diesel" from a wire quote into arithmetic |
| **NEW ③** | ★★ **A whole sub-node the sector's own instrument cannot see.** EVENT_ALPHA Card 1: Asia spot LNG **$24.614/MMBtu** (5-month high), TTF **€70→€71.20/MWh** (3.5-year high, since Jan-2023), **QatarEnergy force majeure extended into November**, tenders from Korea/India/Taiwan/Bangladesh for Oct–Nov cargoes. **`LNG`, `GLNG`, `FLNG` are all outside `us_top300.csv`** ⇒ no flow, no OBV, no RS, no shortlist, and `chain-hop`'s universe *is* `us_top300` so the tool cannot reach them either (`D563`) |
| **CARRIED unchanged** | the 09-07 file's value-chain map, IR anchors and player list. `XOM` at 30.5% of the sector is **top-heavy but NOT a flipper** (+0.440 → ex-top1 **+0.621**); the sector is *more* positive without it |
| **CARRIED with its warning** | `theme-age Hormuz` **⚪ECHO 0.78× on a 10,568 base** — the narrative decelerates for a 6th run **while the physical event escalates**. `Venezuela` **−8.89% raw** (2nd consecutive decelerating run, after −5.3%) is a live warning against **`P139`**'s driver, stated and not scored (`D242`) |

## 5 · The gas/LNG sub-node — folded in by PREMORTEM, and what the desk CAN say about it

Direct `module_flow` (which does not require universe membership) — ⚠ **asof 2026-09-08 INTRADAY /
PARTIAL** (`D577`), so these are tags, not settled readings:

| name | chain position | tag | OBV | rs60 | vol-surge | `[FINRA]` z (settled 09-04) |
|---|---|---|---|--:|--:|---|
| `LNG` Cheniere | **US export terminal — the substitution beneficiary** | 🟢가속 | 매집 | **+11.2%** | **1.25×** | +0.02, 5v5 **+16.0▲** |
| `FLNG` Flex LNG | shipping / freight-rate leg | 🟢가속 | 매집 | −0.6% | **1.21×** | 🟢 **−1.85 = short-covering** |
| `GLNG` Golar | FLNG vessels | 🟡중립 | 매집 | −2.2% | 0.69× | 🟢 **−1.65 = short-covering** |
| `WMB` Williams *(in universe)* | US gas transport, **headline-named layer** | 🟢가속 | 매집 | −3.6% | 1.39× | −1.16, 5v5 −11.6▼ |

**Vol-normalised (`B3`/`R142`)**: `LNG` ret20 **+14.00%** on a **1.55%** own-sigma = **z20 +2.03** —
one of only two names on the board that are 2σ+ while looking ordinary on raw returns. ⇒ *"it hasn't
run"* is false; the raw screen hides it because its sigma is the board's smallest.

⇒ **What this desk may state**: the gas leg is measurable on price and short-pressure, it is **not**
measurable on any sector-aggregate instrument, and **`P145` (settles 09-14) is the only object that
will settle the question.** `GLNG`/`FLNG` are logged to `missed_ledger` as **`N.유니버스부재`**.

## 6 · Track KPIs and anti-signals (observables, not opinions)

| | observable | current |
|---|---|---|
| **KPI 1** | `refinery` term raw Δ, run-over-run, phrase convention | **+12.50% = the board's top riser** |
| **KPI 2** | distillate crack **20-session** change percentile (not the 3-session) | **77.8th** |
| **KPI 3** | `theme-age LNG` | ⚪ECHO **1.18×** — under Card 1's A branch it clears 2× |
| **ANTI-SIGNAL 1** | a confirmed restart of **≥3 mb/d** of Middle East refining capacity | not observed |
| **ANTI-SIGNAL 2** | **Russia lifts its diesel export ban** | not observed |
| **ANTI-SIGNAL 3** | a **confirmed Strait-of-Hormuz reopening** (≥3 outlets) — 🚨 **this is the correlated hit**: it takes the gas leg, the refining premium, the breakevens and the three duration UWs at once (PREMORTEM §2a) | `catalyst_calendar` carries it as an **undated 🔀binary** |
| **ANTI-SIGNAL 4** | ⚠ the QatarEnergy force majeure **expiring in November** without renewal — a *dated* kill, not a headline one | dated **November 2026** |

## 7 · What this file does NOT claim

- **No verdict change.** ROTATION holds `ENRG OW` and this stage does not promote it; the promoting
  argument (Card 2) is a **news** argument and ROTATION already declined it as a macro re-argument.
- **No claim that the sector is quiet or loud on news** — `theme-age` is admissible (it is computed
  inside one instrument) but the **sweep's** velocity axis is dead at 17.39% coverage (G1).
- **No sizing.** `P4`.
- ⚠ **`M1361` is corrected, not deleted**: the 3-session −$7.02 / 6.0th-percentile figure is real and
  is printed above beside the three windows that contradict its implication.
