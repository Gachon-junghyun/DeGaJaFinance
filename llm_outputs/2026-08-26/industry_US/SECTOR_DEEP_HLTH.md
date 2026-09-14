# SECTOR_DEEP_HLTH — industry_US · 2026-08-26 · **CONTINUOUS TRACK (6th consecutive run) — DELTA-LED**

> Structure carried by reference to `llm_outputs/2026-08-25/industry_US/SECTOR_DEEP_HLTH.md`.
> **Delta-led** per the continuous-track rule. **Zero sizing, zero buy/sell (P4).**
> Price: equal-weight `us_top300`, excess vs **`SPY`**, **settled 2026-08-25 close**.
> Flow: 2026-08-26 sweep ⚠ **pre-market bar (`D355`)**.
> 🚫 **G3 note**: PREFLIGHT attached a weighted-flow restriction to this sector this morning off the
> 08-25 baseline. **On this run's own sweep `LLY` prints `top1_flips_sign: false` and the restriction
> is LIFTED** (`SECTOR_ROTATION §2`). The sector is nevertheless ranked on **price and `eqflow`** below,
> not on `wflow` — because `wflow` still carries 42-day-old caps (G5).

---

## §1 · 🚨 THE DELTA, and it begins with a correction to THIS RUN'S OWN MACRO (`D48`)

**`MACRO_REPORT §E` and `M945` of this run wrote: *"the 08-25 payer/distributor overhang has largely
CLOSED."*** That claim was built on **sub-industry mean `exc5` at 100% participation** — Distributors
`+3.25`, Managed Care `+1.15`, both at 100%.

**The name-level flow and the 20-session window refute the strong form of it, and the refutation is
written here rather than the earlier sentence being edited:**

| Payer / services / distributor name | flow | tag | OBV | `rs20` | `exc5` | **`exc20`** | `exc60` |
|---|---:|---|---|---:|---:|---:|---:|
| **`CVS`** | **−0.856** | **🔴분산** | 분산 | **−16.7** | −1.92 | **−18.42 — the sector's worst** | +0.86 |
| **`UNH`** | **−0.699** | **🔴분산** | 분산 | −9.2 | +0.88 | **−10.89** | +3.03 |
| **`CI`** | **−0.674** | **🔴분산** | 분산 | −9.2 | +0.50 | **−10.60** | −0.55 |
| **`MCK`** | −0.599 | **🔴분산** | 분산 | −2.7 | +4.32 | −1.63 | +20.66 |
| `CAH` · `COR` | −0.159 / −0.286 | 🟡 | 중립 | −1.0 / −1.9 | +1.45 / +3.97 | −1.05 / −0.73 | +19.65 / +20.55 |
| `HUM` · `ELV` | +0.337 / +0.112 | 🟡 | 매집 | +4.1 / +1.5 | +2.22 / +0.35 | −3.12 / +0.03 | +26.35 / +0.20 |

⇒ **What actually happened**: the payer node's **5-session** excess turned positive (which is what
`M945` measured), while its **20-session** excess remains the three worst readings in the sector and
**three of the five names are 🔴분산 with `flow_score` −0.674 to −0.856 and `rs20` −9.2 to −16.7** (**RULE D6** — the C-grade OBV state is one of four axes here, never the sole one).
★ **The correct sentence is: the payer overhang closed on FIVE sessions and did not close on TWENTY.**
`M945` is **narrowed, not withdrawn** — its `exc5`/participation numbers are correct as measured.
⚠ **This is the second time in one run that a 5-session reading has been shown to be a one-week
object** (`M944` was the first). **The pattern is the finding.**

### 1b · What genuinely DID change: the weak node moved, and it moved to Equipment
**Health Care Equipment: `exc5 +0.19` at 37.5% participation — the sector's only sub-industry below
50%.** Inside it: `SYK` **🔴분산, flow −0.794, `exc20` −8.00**; `IDXX` `exc20` −6.81; `ISRG`
`exc60` **−13.68**. Against `BDX` (+0.443, 매집, `exc60 +27.75`) and `ABT` (`exc60 +34.42`).
⇒ **Equipment is the sector's new dispersion node (`W5`), and the desk has been watching Payers.**

---

## §2 · The one 🟢, and it is the sector's whole story on every window

**`MRK` — the sector's ONLY 🟢가속, and the board's 3rd-highest flow score.**

| Axis | Value | Rank in sector |
|---|---|---|
| `flow_score` | **+0.767** | **1 of 32** |
| tag / OBV | **🟢가속 · 매집** | only 🟢 |
| `vol_surge` | **1.18** | **1 of 32** — and one of only 4 names on the entire 299-name board above 1.15 on a bar carrying 2.48% of normal volume |
| `rs20` / `rs60` | **+13.0 / +32.6** | 2nd / 2nd |
| `exc1` / `exc5` / `exc20` / `exc60` | **+3.5 / +15.94 / +15.30 / +30.53** | **1st on all four** |
| FINRA short | `z −1.20`, 5v5 −1.2▼ (`LLY` reference) | — |

⚠ **The counter-evidence, carried `[measured]` from 08-25 and NOT re-verified this run**: `MRK` was
recorded trading **at or above its consensus mean target within 3.5% of its 52-week high**, which is
the `L2` shape. **A name that is first on all four windows and at its target is an extended name, and
this file says so rather than reading the flow score alone.**
⇒ **Track KPI below.**

---

## §3 · Node map — 8 sub-industries, participation as the ordering axis

| Node | n | `exc5` | `exc20` | participation (exc5 > 0) | Read |
|---|---:|---:|---:|---:|---|
| Life Sciences Tools | 4 | **+5.80** | +5.51 | **100%** | `A` `TMO` `DHR` `WAT` — all flow positive (+0.194…+0.633) with `rs60` +7.6…+26.5 and 100% participation, the C-grade OBV state agreeing (**RULE D6**). **The most internally consistent node in the sector** |
| Pharmaceuticals | 5 | **+5.16** | +5.04 | **100%** | Carried by `MRK` (+15.94); `PFE` +5.04, `BMY` +3.03, `JNJ` +0.95, **`LLY` +0.85** |
| Health Care Facilities | 1 | +4.34 | −0.85 | 100% | `HCA`, n=1 ⇒ **not a node, a name** (`C4`) |
| Biotechnology | 6 | +4.02 | +3.31 | **100%** | `AMGN` `REGN` `GILD` `VRTX` all OBV 매집 with `exc60 +9…+34`; ⚠ **`ALNY` is `exc20 −20.14` / `exc60 −21.74` with `exc5 +5.22`** — a violent bounce off a collapse, **not** a node member on any longer window |
| Health Care Distributors | 3 | +3.25 | −1.14 | 100% | ★ **the node `M945` said had closed — and `MCK` inside it is 🔴분산** |
| Managed Health Care | 3 | +1.15 | −4.66 | 100% | `HUM` `ELV` 🟡; **`UNH` 🔴분산 with `exc20 −10.89`** |
| **Health Care Equipment** | 8 | **+0.19** | +1.47 | **37.5%** | 🚨 **the sector's weak node this run** — `SYK` 🔴, `IDXX`, `ISRG` |
| Health Care Services | 2 | −0.71 | **−14.51** | 50% | **`CVS` 🔴분산, `exc20 −18.42` — the sector's worst single reading** |

**Bottleneck / binding constraint — stated as a constraint, not as demand.** The sector's 60-day
excess is broad and positive (`exc60` ≥ +19 on 12 of 32 names), while its 20-day excess is negative on
15 of 32. **The binding constraint is not demand — it is the payer/reimbursement leg**, and it is
identifiable because **every negative-`exc20` outlier in the sector is a payer, a service, or a
distributor**, while every manufacturer node runs 100% participation. ⚠ **Strong demand ≠ bottleneck**:
the biotech/pharma nodes are not constrained, they are simply not the thing being repriced.

---

## §4 · Track KPIs and anti-signals

| KPI | Now | Confirms if | Refutes if | Date |
|---|---|---|---|---|
| Payer node `exc20` (`CVS`,`UNH`,`CI`) | **−18.42 / −10.89 / −10.60** | closes to > −5 on all three | any goes below −20 | **09-08** |
| `MRK` position vs consensus target | at/above target (carried, unverified) | consensus target rises with price | price ≥ target while revisions turn negative ⇒ `L2` | **09-08** |
| Health Care Equipment participation | **37.5%** | ≥ 60% | ≤ 25% ⇒ the weak node has widened | **09-08** |
| Sector `eqflow` rank | **1 of 11 (−0.000)** | stays top-3 | falls below rank 6 | rolling |
| `LLY` `top1_flips_sign` | **false** this run (was **true** on 08-25) | stays false ⇒ the sector's sign is not one name | flips true ⇒ **G3 restriction re-attaches and the OW may not be argued on `wflow`** | every run |

**Anti-signals that would kill the `OW`**: a **drug-pricing policy action** (the term reads
🟡**1.76× on a base of 166**, in band, **down from 2.19× on 08-25** — decelerating); a payer-node
contagion into the manufacturer nodes (participation falling below 50% in Pharma **or** Biotech);
or `MRK` losing 🟢 while remaining the sector's only one.

---

## §5 · What this deep-dive could NOT do
- ⚠ **No primary filing opened for any Health Care name this run.** The `MRK` target/valuation facts
  are **carried `[measured]` from 08-25** and are labelled inherited, not re-verified.
- ⚠ **`ALNY`'s `exc5 +5.22` against `exc20 −20.14`** is exactly the reversal shape `S128` was
  registered to test — but `ALNY` is **not** in either `S128` basket (its `rs20 −22.1` **and**
  `rs60 −20.6` are both negative), so the row cannot speak to it.
- ⚠ **`vol_surge` is unusable for all 32 names except `MRK`, `A` and `BSX`** (`D355`) — 29 of 32 sit
  below 0.80 on a bar carrying 2.48% of normal volume.
- ⚠ **No chain-hop pass was run for this sector.** The 08-25 run's chain-hop attempt on a different
  theme returned zero candidates; this run spent its news budget on the Energy and IT threads and
  **says so rather than implying coverage.**
