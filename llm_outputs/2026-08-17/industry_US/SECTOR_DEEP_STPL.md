# SECTOR_DEEP_STPL — Consumer Staples (UW−) · industry_US · 2026-08-17 · **ROTATING track — last covered 2026-08-10 = 7 runs ⇒ FULL FRESH MAP**

> The board's longest gap, declined on 08-16 for an empty mandate and re-weighed today per that run's
> own pre-commitment. Flow numbers are the **settled 3-axis sweep** (`asof 2026-08-14`). P4 throughout.

## 0 · 🚨 ⛔ Mandate rebuttal first — **and this stage refutes its own earlier claim before using it**

**Correction, written down rather than edited away (§4c / D48).**
`EVENT_ALPHA` Card 6 and `SECTOR_ROTATION §2c/§3` describe `TGT` as **"🟢가속"**. **On the admissible
instrument it is not.** The settled 3-axis sweep tags `TGT` **🟡중립** with `vol_surge` **1.01**.

| Source | Tag | `vol_surge` | velocity | Why they differ |
|---|---|---|---|---|
| **Settled sweep** (3-axis, `asof 08-14`) | **🟡중립** | **1.01** | **`None`** — the sweep's velocity query for `TGT` failed | tag = `flow_tag(price, velocity)` with velocity missing |
| `module_flow TGT` standalone, **22:48 KST** | 🟢가속 | 0.79 | **2.38×** — the standalone probe answered | the same code, same prices, **one extra input** |

⇒ **The identical function returns a different tag for the same name on the same closes, depending
only on whether the news bridge answered.** This is `D261` in its cleanest form yet, and it caught this
desk mid-run: **the 🟢 I quoted downstream rests on the axis PREFLIGHT revoked.**
**The claim is withdrawn. `TGT` is 🟡중립.** What survives, and it is enough for the mandate: **`TGT` is
the sector's #1 `flow_score` at +0.503 on the 3-axis score** — nearly double the #2 — with OBV
accumulating and the best RS60 in the bucket.

## 1 · Full map — 19 names, ranked, with the split marked

| # | Name | flow | OBV | rs20 | rs60 | surge | tag | node |
|---|---|---|---|---|---|---|---|---|
| 1 | **`TGT`** | **+0.503** | 매집 +0.115 | +6.2 | **+15.6** | 1.01 | 🟡 | general merch |
| 2 | `KO` | +0.279 | 매집 +0.186 | +3.1 | +1.3 | 0.67 | 🟡 | beverages |
| 3 | `HSY` | +0.236 | 매집 **+0.307** | +3.0 | −10.3 | 0.60 | 🟡 | snacks |
| 4 | `MDLZ` | +0.125 | 매집 +0.237 | −0.2 | −2.0 | 0.64 | 🟡 | snacks |
| 5 | `CCEP` | +0.008 | 매집 +0.075 | −2.1 | +11.4 | 0.89 | 🟡 | beverages (bottler) |
| 6 | `KVUE` | −0.008 | 매집 +0.126 | −3.3 | +6.1 | 0.76 | 🟡 | household/personal |
| 7 | `KMB` | −0.051 | 매집 +0.153 | −2.6 | +8.6 | 0.53 | 🟡 | household |
| 8 | `KDP` | −0.215 | 분산 −0.033 | −2.7 | +3.2 | 0.94 | 🟡 | beverages |
| 9 | **`WMT`** | −0.226 | flat +0.015 | −3.5 | **−19.9** | 0.80 | 🟡 | mass grocery |
| 10 | `SYY` | −0.258 | 분산 −0.031 | −2.9 | +4.6 | 0.87 | 🟡 | foodservice distn |
| 11 | 🚨 `MNST` | −0.260 | 분산 −0.082 | **−57.6** | **−52.9** | **1.44** | 🔴 | beverages |
| 12 | `PG` | −0.264 | 매집 +0.076 | −8.1 | −3.5 | 0.84 | 🟡 | household |
| 13 | `PEP` | −0.269 | flat +0.011 | −1.8 | −12.2 | 0.61 | 🟡 | beverages/snacks |
| 14 | `CL` | −0.439 | flat −0.008 | −5.6 | −3.7 | 0.66 | 🟡 | household |
| 15 | **`COST`** | −0.480 | 분산 −0.083 | −2.3 | **−18.0** | 0.62 | 🔴 | warehouse club |
| 16 | `PM` | −0.607 | 분산 −0.098 | −5.8 | −6.4 | 0.71 | 🔴 | tobacco |
| 17 | `MO` | −0.612 | 분산 **−0.155** | −15.9 | −17.0 | 1.08 | 🔴 | tobacco |
| 18 | `ADM` | −0.656 | 분산 **−0.357** | −10.8 | −4.5 | 1.02 | 🔴 | agri processing |
| 19 | **`KR`** | **−0.856** | 분산 −0.296 | −8.1 | **−25.5** | 0.66 | 🔴 | grocery |

**Sector aggregate**: `wflow −0.242` · `eqflow −0.213` · `breadth 0.00` · **0 greens, 5 reds**.
⚠ `wflow` `top1` is `WMT` at **28.9%** — **not** a sign-flipper (the sector stays negative without it),
so `wflow` is admissible here. Cap weights are **33 days stale**.

## 2 · ★★★ The finding: the sector's weakness is ONE node, and it is not "staples"

| Node | Names | EW rs60 |
|---|---|---|
| **Household / personal care** | `KVUE` +6.1 · `KMB` +8.6 · `PG` −3.5 · `CL` −3.7 | **+1.88** |
| **Beverages / snacks** *(ex-`MNST`)* | `KO` +1.3 · `CCEP` +11.4 · `HSY` −10.3 · `MDLZ` −2.0 · `KDP` +3.2 · `PEP` −12.2 | **−1.43** |
| **Food retail / grocery** | `WMT` −19.9 · `COST` −18.0 · `KR` −25.5 | **−21.13** |
| **`TGT`** *(classified staples, trades as discretionary-adjacent)* | +15.6 | **+15.60** |

⇒ **A 36.73pp spread between `TGT` and the grocery EW inside one GICS sector**, and `TGT` vs `KR`
alone is **41.1pp**. The sector's UW− is really a **food-retail** call wearing a staples label.
⚠ **W5 satisfied, and it inverts the usual reading**: staples is normally the defensive node; here the
defensive sub-nodes (household, beverages) are roughly flat and the **retail** node is collapsing.
That is a **consumer-transaction** signal, not a rate/duration signal — which matters directly for `S98`.

## 3 · ★★ `S98` / `S80` — does STPL behave like a duration leg? The map says no

`S80` (08-19) and the new `S98` (08-20) ask whether UTIL + RE + STPL (+HLTH) are one duration bet.
**Inside STPL the evidence points against that framing**: if the sector were being sold on rates, the
**bond-proxy** nodes — tobacco (`PM` −6.4, `MO` −17.0, the classic yield substitutes) and household
staples — would lead the decline together with grocery. Instead **household is the sector's best node
(+1.88)** while **grocery is −21.13**. ⇒ **The dispersion is transactional, not rate-driven.**
⚠ **Honest limit (C4)**: n = 19 names, one 60-day window, one sector. This is **evidence for branch B
of `S98`** (the four legs split), not a settlement of it — and `S98` scores on 08-20 regardless.

## 4 · The `TGT` question, stated as the DEEP's real deliverable

| Item | Reading |
|---|---|
| Rank | **#1 `flow_score` (+0.503)**, nearly 2× the #2 (`KO` +0.279) |
| OBV | **accumulating +0.115** |
| RS | rs20 **+6.2** · rs60 **+15.6** — best in sector, against `WMT` −19.9 and `COST` −18.0 |
| Volume gate | `vol_surge` **1.01** ⇒ blocked, tag 🟡 (see §0) |
| σ20d | **1.48% — the lowest of every name this run measured** |
| Short pressure | 3.7% float, **covering**, DTC 4.3 |
| 🚨 **Positioning** | implied **±6.7%** (expiry 08-21, **D4**) · **P/C 1.74 = put-heavy** · skew **+37.5** |
| 🚨 **Event** | **reports ~2026-08-20** |

★★ **The disagreement is the finding.** OBV is accumulating and RS leads the sector, while the options
market is paying **±6.7% — 4.5× the name's own 1.48% daily sigma** — with a put-heavy book and a
+37.5 downside skew. **Flow says accumulation; positioning says fear.** One of them is wrong and the
print settles it in three sessions.
⚠ **This is exactly the `COHR`/`LITE` lesson from 08-16**: a name whose flow is dated to its own
earnings event is showing **reaction volume, not accumulation**. `TGT` has not printed yet, so the
accumulation is **pre-print** — the opposite case, and therefore the more interesting one.
⇒ **Watch, not candidate.** A name that reports in three sessions is a coin flip (the desk's own rule).

## 5 · Track KPIs and anti-signals

| # | KPI | Threshold | Date |
|---|---|---|---|
| 1 | `TGT` 1-session excess vs `SPY` at its print | ≥ +6.7% ⇒ the flow read beat the options read · ≤ −6.7% ⇒ the reverse | **~08-20** |
| 2 | Grocery EW (`WMT`+`COST`+`KR`) rs60 vs `SPY` | stays ≤ −15pp ⇒ the node, not the sector, is the UW− | 08-21 |
| 3 | `XLP` 5-session excess sign vs `XLU`/`XLRE`/`XLV` | all four agree = one duration bet | **08-20** (`S98`) |
| 4 | Household EW rs60 | stays ≥ 0 ⇒ §3's "not a duration leg" holds | 08-21 |
| 🚨 | **Anti-signal** | A **`TGT`-specific event** (guidance pre-announcement, CEO change, M&A) inside the window ⇒ KPI 1 is idiosyncratic ⇒ **VOID** |
| 🚨 | **Anti-signal 2** | An **FOMC-dated communication or CPI print** inside the window ⇒ KPI 3 moves for a reason that is not the duration structure ⇒ `S98` **VOID** |

## 6 · Named for the record — the outlier this map surfaced

🚨 **`MNST` rs20 −57.6 / rs60 −52.9 with `vol_surge` 1.44** — the only name in the sector whose volume
gate is *open*, and it is open on a collapse. The desk has **no thesis, no ledger row and no coverage**
on it, and none is invented here (P4). **Registered as an unowned observation for the next STPL DEEP**;
a −52.9pp 60-day excess inside a "defensive" sector is not something a map should pass over silently.

## ✅ Verdict for BET

**UW− held — it is the board's floor and no demote exists.** The 7-run gap produced three things worth
carrying: (i) the UW− is a **food-retail** call, not a staples call (36.73pp internal spread); (ii)
that dispersion is **transactional, not rate-driven**, which is evidence for `S98` branch B; and
(iii) **`TGT` is a pre-print flow/positioning disagreement**, watch-only, settling ~08-20.
🚫 **And this file withdrew its own upstream "🟢가속" claim on `TGT` (§0)** — the correction is the
most load-bearing line in it.
