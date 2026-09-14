# SECTOR_DEEP_DISC — Consumer Discretionary (N+) · industry_US · 2026-08-23 (Sun) · Stage 8 / L1·DEEP
### Rotating slot 1 of 2 — **FULL FRESH MAP** (last covered 2026-08-15 = ~8 runs, worst recency on the board)

> ⚠ **`n_new_sessions_since_prior_run = 0`.** All flow numbers are the **2026-08-21** settle.
> ⚠ **No live bracket owns this sector** — `S91` was VOIDed on 08-22 (`D300-KR`: its anti-signal named
> "a September-FOMC-dated headline", which an 8-day US window contains almost surely). **The sector
> that had the board's largest untested contradiction also lost its only test.**

## 0 · ★★★ The mandate, answered

ROTATION's mandate: *"`exc20` rank 1 (+4.244) against `exc60` rank 10 (−4.938) with breadth 0.000
across 28 names. Reversal with a base, or five names?"*

### The answer: **it is a reversal with a real base in ONE node, and the 60-day deficit is TWO mega-caps.**

**First, the mandate's own premise has to be corrected** (`M835`, DEEP-HLTH): **`breadth` is the 🟢
rate, not participation.** DISC's true participation — `OBV 매집` **and** `rs20 > 0` — is
**11 of 28 = 39.3%**, the **third-highest on the board**, not zero.

**The decomposition, which is what "reversal or five names" actually asks:**

| | 20-day (`exc20` **+4.244**, rank 1) | 60-day (`exc60` **−4.938**, rank 10) |
|---|---|---|
| **Who carries it** | The **travel / delivery / marketplace** node: `ABNB` rs20 **+29.1** · `DASH` **+25.6** · `GRMN` +17.7 · `BKNG` +14.5 · `CMG` +12.4 · `CVNA` +12.0 — **and `TSLA` +12.3 with the board's 3rd-largest one-session delta, +0.519** | **Two mega-caps**: `TSLA` (**23.0%** of the sector) rs60 **−19.6** and `AMZN` (**40.2%**) rs60 **−6.9**. Together **63.2% of the weight** |
| **The node's own quality** | `DASH` `obv_norm` **+0.595** — the highest in the sector; `ABNB` +0.226; `BKNG` +0.169; all 매집, all rs60 **+22.5 to +39.8** | `AMZN` is **OBV 분산 −0.110** with flow **−0.076** |

★★ **`AMZN` at 40.2% of the sector is a DRAG, not a driver**, and the flipper field proves it:
`top1_flips_sign` is **false** because removing `AMZN` takes `wflow` **+0.122 → +0.254**, i.e.
**ex-Amazon the sector is twice as strong.** ⇒ **The sector's cap weight is fighting its own tape.**

⇒ **Verdict: NOT "five names."** The 20-day leadership is a **coherent node of six-plus travel /
delivery / marketplace names with rs60 between +22.5 and +39.8 and OBV accumulating** — i.e. the
20-day move sits **on top of** a 60-day base in that node. **The 60-day sector deficit is a
mega-cap-weight artifact.** `eqflow` **+0.103 (rank 2 of 11)** against `wflow` +0.122 says the same
thing from the other direction.

## 1 · Value chain — 6 nodes, left → right, with the binding constraint marked

| # | Node | Names (flow · OBV · rs60) | Read |
|---|---|---|---|
| 1 | **Discretionary income / credit** | *(cross-sector: `AXP` delta **+0.626** rank 2 of 299, `HOOD` **+1.230** rank 1 — both Financials)* | The consumer's *funding* is inflecting harder than the consumer's *spending*. ⚠ Cross-sector, logged not owned |
| 2 | **Experiences — travel & leisure** | `ABNB` +0.700 매집 +39.8 · `BKNG` +0.494 매집 +22.5 · **vs** `MAR` **−0.750 🔴** 분산 −9.7 · `HLT` **−0.479 🔴** 분산 −5.0 · `RCL` −0.075 · `CCL` −0.491 | 🚨 **The node SPLITS: asset-light platforms accumulate, asset-heavy hotels and cruise disperse.** `ABNB` +0.700 vs `MAR` −0.750 = **1.45 of flow spread inside one node** (`W5`) |
| 3 | **Delivery / marketplace** | `DASH` +0.717 매집 **+0.595 OBV** +39.8 · `MELI` +0.370 매집 +11.3 · `PDD` +0.404 매집 +0.0 · `EBAY` −0.050 | **The strongest node on both axes.** `DASH`'s OBV is the sector's highest |
| 4 | **★ BOTTLENECK — the two mega-caps** | `AMZN` **−0.076, 분산, 40.2% weight** · `TSLA` +0.600 매집 but **rs60 −19.6, 23.0% weight** | **The binding constraint is not demand — it is that 63.2% of the sector's cap sits in two names whose 60-day performance is negative.** No node-level improvement can move `wflow` without them |
| 5 | **Home / big-ticket retail** | `HD` **−0.378 🔴** 분산 · `LOW` +0.110 (**delta −0.347**) · `DHI` −0.296 · `ORLY` +0.079 · `AZO` −0.280 | Uniformly weak. The rate leg (`DGS30` 96.4th %ile) is the obvious mechanism and is **not** measured here |
| 6 | **Apparel / off-price** | `TJX` **−0.333 🔴** 분산 −0.231, **surge 1.64** · `NKE` **−0.299 🔴** 분산, surge 1.22 · `ROST` +0.396 매집, **surge 1.61, delta +0.424** | 🚨 **Three of the sector's four highest volume surges are here, and two of the three are 🔴.** High surge is distribution here, not accumulation — a direct illustration of why `vol_surge` is `W1`-suspect |

## 2 · Chain-hop / under-named candidates — **none advanced**

`ROST` is the only DISC name clearing `vol_surge ≥ 1.2` with OBV 매집 (+0.102) — and it **fails the
🟢 gate on rs20 (−3.6)**. `YUM` (surge 1.16) and `LOW` (1.30) are 중립. ⚠ **`TJX` and `NKE` clear the
surge gate while dispersing** — which is the cleanest single illustration in this run that
`vol_surge` does not carry a sign.
⇒ **No name advanced to BET** (P4).

## 3 · Track KPIs and anti-signals — as observables

| KPI / anti-signal | Current (08-21 settle) | What kills the N+ |
|---|---|---|
| Travel/delivery node OBV | `ABNB` · `DASH` · `BKNG` · `MELI` **all 매집** | any 2 of 4 leave 매집 |
| `AMZN` | flow −0.076, **분산**, 40.2% weight | 🚨 **A further leg down in `AMZN` alone can take the sector negative regardless of the node** |
| `exc20` rank | **1 of 11** | falls below rank 5 |
| Participation (`M835`) | **39.3%** | falls below 25% |
| ⚠ **Tariff exposure** | The **50% US–Canada tariff took effect 2026-08-22** — *after* this flow frame — and the desk's own `forbes` 08-21 item names **Walmart and Target** receiving tariff refunds, i.e. the mechanism reaches retail | `P92` branch A (settles 08-28) |
| ⚠ Rate leg | `DGS30` **5.23 = 96.4th %ile**; node 5 is the transmission | `S112` branch B |

## 4 · What this file could NOT measure, stated rather than glossed

- **No live scenario owns this sector.** `S91` VOIDed; nothing replaces it. ⇒ **The sector with the
  board's best 20-day excess and worst recency has zero pre-registered falsifiers.** Handed forward as
  the highest-priority registration gap.
- **The credit/funding node (node 1) is cross-sector** and this desk maps it in Financials, so the
  consumer's funding condition is not read here. `HOOD` (+1.230) and `AXP` (+0.626) carrying the
  board's two largest one-session deltas is **noted, not interpreted**.
- **`vol_surge` cannot be used as evidence in this sector in either direction** — its three highest
  readings are `TJX` 1.64 🔴, `ROST` 1.61 🟡, `LOW` 1.30 🟡.

## 5 · Verdict on the mandate

**A reversal with a base, plus a mega-cap weight problem — not five names.**
The travel/delivery node is **six-plus names, all OBV-accumulating, rs60 +22.5 to +39.8**. The 60-day
sector deficit is **`TSLA` −19.6 and `AMZN` −6.9 at 63.2% combined weight**, and removing `AMZN`
**doubles** `wflow`. ⇒ **MACRO's N+ is confirmed on `eqflow`, and the sector's cap-weighted number
should not be used to judge it.**
⚠ **P4 — no sizing, no names advanced.** ⚠ And the mandate's premise (`breadth 0.000`) was itself a
misreading of the instrument (`M835`).
