# SECTOR_DEEP_IT — industry_US · 2026-08-13 · Rotating slot 2 · **FULL FRESH MAP**

> Scope: Information Technology, GICS-labelled, `us_top300` (56 names). **Benchmark = `SPY`, declared
> here and named inline throughout (C1).** Flow `asof settled 2026-08-12`; no 08-13 bar is used
> anywhere. TRACK = ROTATING, last covered **2026-08-10** (2 runs). **P4 — analytical only, zero
> buy/sell language, zero sizing.** Every number below was pulled or computed on this run unless
> tagged `[inherited]`.

---

## §0 · THE VERDICT — the three stages are not in conflict; they are reading three different axes, and two of them are measuring the same axis at two different window lengths

**Resolution, stated as a decision rather than a hedge: the promotion was correctly declined, but ROTATION declined it for a reason that does not survive decomposition, and EVENT_ALPHA's counter-evidence does not replicate.** The three readings reconcile completely, and here is the arithmetic that does it.

`sector_flow.py:176` defines `flow_score` as the mean of exactly three clipped axes — `clip(obv_norm/0.16)`, `clip(rs20/8.0)`, `clip((vol_surge−1.0)/0.6)`. Decomposing IT's two refusal numbers into those three axes, computed this run over all 56 names:

| Weighting | OBV axis | RS20 axis (vs `SPY`) | **VOLUME axis** | = flow |
|---|---|---|---|---|
| **Cap-weighted** (`wflow`) | **+0.055** | **−0.004** | **−0.461** | **−0.136** |
| **Equal-weighted** (`eqflow`) | −0.032 | **+0.112** | **−0.379** | **−0.099** |
| *(universe, 300 names, for scale)* | +0.146 | +0.073 | −0.313 | −0.032 |

★★★ **Both of ROTATION's refusal numbers are volume readings wearing a flow label.** On the cap-weighted book the two *direction* axes sum to **+0.051** (a positive contribution of +0.017 to the mean) and the volume axis alone contributes **−0.154** — i.e. **the volume axis supplies 113% of the negative sign, and the direction axes actively oppose it.** Equal-weighted, the same decomposition: direction contributes **+0.027**, volume **−0.126**. **On neither weighting is IT's negative flow score a statement that money is leaving. It is a statement that 48 of 56 names (85.7%) traded below their own 20-day average volume**, at a sector mean `vol_surge` of **0.774** against a universe mean of 0.821 — **10th of 11 sectors**.

⇒ **MACRO and ROTATION were never in disagreement.** MACRO measured direction (`XLK` excess vs `SPY`: exc1 **+1.24**, exc5 +1.24, exc20 +1.67, exc60 +2.64 — positive on all four). ROTATION measured a composite whose sign in this sector is set by participation. **Both are correct and they are compatible: IT rose against `SPY` on all four windows on the thinnest volume of any sector but one.**

★★ **And that reading is not neutral — it converts the positioning counter from a separate objection into the same one.** A sector that outperforms `SPY` on all four windows, on 0.774× volume, with `XLK` FINRA short-volume z at **−1.91 (covering)**, into a **Nasdaq-100 spec net −35,006 at the 0th percentile of a 1-year lookback** (re-pulled this run, `us_flow.py --cot`, 2026-08-12) is describing **a low-participation short-cover, not a demand-led bid.** The volume axis is the *mechanism* of the squeeze objection, not an unrelated third refusal. **Three stages, one phenomenon.**

**What this changes, precisely:** ROTATION's sentence *"the flow axis refuses it"* should read *"the participation axis refuses it; the direction axis does not."* The **N tilt is correct and this file does not disturb it** — but the reason on the record is wrong, and a future run that repeats "both flow axes negative" as evidence of distribution will be repeating a volume reading as a money reading.

**The one leg that is NOT resolved this way — and it fails for a different reason:** EVENT_ALPHA Card 4. See §6: **the desk's second OBV producer reports the opposite state on five of the six names Card 4 rests on**, and Card 4's shape carries an 11.0% base rate across the whole 300-name universe.

---

## §1 · ★ SUB-SECTOR DISPERSION — the sector label is the wrong unit, and the spread is 7.3× the sector's own move

Per stage rule `W5`. Clusters cut on GICS `industry`, all 56 names, settled 08-12:

| Cluster | n | mcap sh. | avg flow | OBV ax | RS20 ax vs `SPY` | VOL ax | 🟢 | 🔴 | avg Δ |
|---|---|---|---|---|---|---|---|---|---|
| **Networking** (LITE·ANET·CSCO·MSI·CIEN) | 5 | 3.3% | **+0.423** | **+0.517** | **+0.823** | −0.070 | 2 | **0** | **+0.323** |
| **IT services** (ACN·IBM) | 2 | 1.2% | +0.386 | +1.000 | +1.000 | −0.842 | 0 | **0** | +0.111 |
| **Software** (17, incl. EDA) | 17 | 19.7% | +0.113 | +0.247 | +0.329 | −0.237 | 2 | 4 | −0.017 |
| **Electronic/EMS** (COHR·APH·GLW·TEL·JBL·KEYS) | 6 | 2.3% | +0.054 | −0.103 | +0.565 | −0.300 | 1 | 1 | +0.235 |
| **HW/Storage** (AAPL·DELL·HPE·STX·WDC·SNDK) | 6 | 21.0% | −0.133 | −0.024 | −0.090 | −0.286 | 0 | 2 | +0.209 |
| **Semiconductors** (14) | 14 | 44.2% | −0.464 | −0.371 | −0.446 | −0.575 | 1 | **8** | +0.126 |
| **Semicap** (AMAT·LRCX·KLAC·ASML·TER·Q) | 6 | 8.2% | **−0.569** | **−0.770** | −0.342 | −0.594 | 0 | **4** | +0.107 |

**Spread between cluster means = 0.992 (Networking +0.423 → Semicap −0.569).** The sector's own move is `eqflow` **−0.099** and `wflow` **−0.136**. **The dispersion is 10.0× the equal-weighted reading and 7.3× the cap-weighted one ⇒ per `W5`, "Information Technology" is the wrong unit of analysis this run, and this file declines to issue one IT verdict.** This is the **second consecutive replication** of the same finding (08-10 measured a 6.5× spread on a different clustering).

★ **The "6 green AND 19 red" paradox dissolves on the same cut, and it is not a paradox at all — it is a clean bisection.** The 6 greens are **LITE · CSCO** (networking), **PLTR · ORCL** (software), **COHR** (optical), **NVDA** (semis). The 19 reds are **DDOG · APP · CDNS · SNPS** (software, 2 of them EDA = silicon-design), **INTC · MCHP · ON · ADI · AMD · NXPI · QCOM · TXN** (semis), **ASML · KLAC · LRCX · AMAT** (semicap), **WDC · SNDK** (storage), **GLW**. ⇒ **16 of the 19 reds (84%) sit in the silicon chain; 5 of the 6 greens (83%) sit outside it.** IT is not "simultaneously the biggest accumulator and the biggest distributor" — **it is two populations sharing a label, and the sector is large enough (56 names) to top both counts by size alone.**

⚠ **The one number that does NOT bisect: the volume axis is negative in all seven clusters**, from −0.070 (networking) to −0.842 (IT services). **Thin participation is the sector-wide fact; direction is the sector-split fact.** That is why the cluster cut resolves the green/red count but does not rescue the flow score.

---

## §2 · VALUE CHAIN — 8 nodes, fresh, BINDING CONSTRAINT named

| # | Node | `us_top300` names | Reading (settled 08-12, `SPY` bench) |
|---|---|---|---|
| **1** | **Demand anchor — hyperscaler capex** | MSFT · AMZN · GOOGL · META (*not IT-labelled; see §5*) | **Accelerating on disclosed filings, §5.** The node the whole chain discounts, and the only one measured from primary sources this run |
| **2** | **AI accelerator / platform** | NVDA · AVGO · AMD · ARM | Split: NVDA 🟢 +0.213 (OBV +0.099 accumulating, RS20 **+3.1 vs `SPY`**), AVGO 🟡 +0.106 — against AMD 🔴 −0.798 (OBV −0.151, RS20 −11.1) and ARM 🟡 −0.590 |
| **3** | **Advanced foundry** | **TSM — outside universe. HARD GAP, not a zero** | No `us_top300` substitute exists. Third consecutive run this node is unmeasurable |
| **4** | **Semicap equipment** | AMAT · LRCX · KLAC · ASML · TER · Q | Worst cluster (−0.569). Prices *future* wafer starts, 1–2 cycles ahead of node 5's realized ASP. **But 7-day estimate breadth splits it — LRCX 4↑/0↓, KLAC 1↑/2↓ (§4)** |
| **5** | ★ **MEMORY / DRAM–NAND — BINDING CONSTRAINT NODE** | MU · SNDK · WDC · STX | **The take-or-pay ceiling/floor band sits here (§3).** Contracted share is **no longer `unknown` — see §3** |
| **6** | **New external supply** | **CXMT — unlisted-in-US, outside universe** | **P43. Refreshed this run after 4 stale runs — §7.** Enters at client DRAM, **and it is raising prices, not cutting them** |
| **7** | **Networking / optical interconnect** | LITE · ANET · CSCO · COHR · CIEN · APH | **Best cluster (+0.423), zero reds, OBV axis +0.517 with RS20 axis +0.823 vs `SPY`.** The chain layer that consumes node 1's capex without owning node 5's price risk |
| **8** | **System OEM / buyer** | AAPL · DELL · HPE · STX | AAPL 🟡 −0.656, RS20 **−10.1 vs `SPY`**, and at 16.6% of sector cap it is the largest single cap-weighted drag — **`wflow` ex-AAPL is −0.033 vs −0.136 with it, i.e. AAPL alone owns ~76% of the sector's cap-weighted negative flow** |

**BINDING CONSTRAINT, stated once:** node 5's realized pricing for a **now-quantified** share of volume is contractually banded — ceiling ≈ 2Q CY2026 market price, floor for the contract term — which mechanically damps the pass-through from nodes 1–4's demand signal into node 5's *reported* series **in both directions**. Node 7 is the layer most exposed to node 1's capex and least exposed to node 5's band, which is a plausible structural reason its flow reads +0.423 while node 4/5 read −0.569/−0.5 — **offered as the most parsimonious available explanation, not as a measured causal link.**

---

## §3 · THE CONTRACT TERMS — read from the FILING, and the 08-10 `unknown` (C3) is now CLOSED with a number

**Primary source, fetched and read in full this run** (`module_disclosure_us MU --days 150` → 10-Q filed **2026-06-25**, period ended **2026-05-28**, FY26Q3; `sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm`). Verbatim, Item 2 MD&A:

- *"Strategic customer agreements are structured as **take-or-pay** agreements, with **binding commitments for specific volumes** over the multi-year contract terms."*
- *"The largest agreements generally have a **ceiling price** for existing products that **approximates the market price in the second calendar quarter of 2026**, and a **floor price through the term** of the agreement."*
- *"We expect gross margins from our strategic customer agreements with price bands, **even at floor pricing levels**, to yield gross margins **well above our peak quarterly margins in any past cycle**."*

★★ **Two clauses the 08-10 read did not extract, and both matter:**
1. *"We recently executed certain strategic customer agreements, **including agreements executed subsequent to May 28, 2026**"* and *"**In the third and fourth quarters of 2026**, we entered into, and expect to continue to enter into, strategic customer agreements."* ⇒ **the SCA book is mostly younger than the balance-sheet date**, which is why RPO is small.
2. *"Our remaining performance obligations disclosure is based on **minimum committed volumes and minimum pricing** and is **not expected to be indicative of future revenue** under these contracts."* ⇒ **the ~$5.0bn RPO ($422mn booked as contract liabilities, ~one-third converting within 12 months) is a FLOOR-PRICED, minimum-volume number on a partial book.** It was never the contracted book, and the 08-10 file's inference that it is "a lower bound on a narrower base" is confirmed by the issuer's own sentence.

**★ The contracted share — `unknown` is RETIRED, and replaced by two disagreeing graded numbers, not one:**

| Figure | Source | Grade |
|---|---|---|
| **16 SCAs; ~20% of DRAM volume and ~1/3 of NAND volume; 14 of 16 ≈ $100bn minimum contracted revenue; ~$22bn cash deposits; most run 5 years 2026–2030; mgmt expects SCAs to eventually cover "half or more" of revenue** | Zacks via `yahoo_finance` 2026-08-11, sourced to MU's FQ3 disclosure/call | `[news, issuer-sourced]` — **not** in the 10-Q text |
| **"Long-term contracts covering roughly 40% of Micron's DRAM bits"** | Citi via GuruFocus/`yahoo_finance` 2026-08-07 | `[news, sell-side]` |

⚠ **The two disagree by 2×** (20% of volume vs 40% of bits) and **neither appears in the filing** — the 10-Q quantifies only RPO. **The band's SIZE is therefore `[news]`-grade, bounded 20–40%, and is NOT promoted to `[measured]`.** But it is no longer `unknown`, and being bounded is what makes §4's arithmetic possible.

### 3a · ★★ Is a CEILING producing the QoQ series? — Measured answer: **it contributes, and it is arithmetically INSUFFICIENT.**

The desk's regime call rests on `M1` `[inherited]` (server DRAM contract price, TrendForce, seed 2026-07): **1Q26 +90~95% → 2Q26 +58~63% → 3Q26 +13~18% QoQ.** Test, with the share now bounded:

| If spot QoQ is | and capped share is 20% | and capped share is 40% |
|---|---|---|
| +90% | blended **+72.0%** | blended **+54.0%** |
| +58% | blended **+46.4%** | blended **+34.8%** |

⇒ **At the maximum plausible contracted share (40%), a +58% spot quarter blends to +34.8% — it cannot reach +13~18%. The ceiling can account for at most ~40% of the observed deceleration; the residual is not arithmetic.** ⚠ Two limits stated rather than buried: (i) `M1` is a **market index**, and MU's band is a **MU-specific contract term** — the band cannot move the index itself, only MU's realized blend, so this test bounds the contamination of *reading MU off M1*, which is exactly what the regime call does; (ii) the ceiling binds on *"existing products"* only.

**⇒ Verdict on the binding carry rule: the band is REAL, primary-sourced, now SIZED (20–40%, `[news]`), and it CONTAMINATES the second-derivative read — but it CANNOT explain it away. The 08-10 position ("the filing does not disclose enough to tell the two apart") is superseded: enough is now known to bound the arithmetic, and the arithmetic falls short.** The residual deceleration remains a demand-or-index question, not a contract-mechanics question.

---

## §4 · ★ THE MEMORY PRICE NODE — QoQ series, built from PRIMARY FILINGS this run

**`M1` is `[inherited]` and second-hand. This run built an independent, issuer-sourced QoQ series** by fetching MU's FY25 10-K (filed 2025-10-03, `mu-20250828.htm`), the FY26Q2 10-Q (`mu-20260226.htm`) and the FY26Q3 10-Q, and differencing the *Revenue by Technology* tables:

| Quarter | DRAM revenue | **QoQ (sequential)** | ≈ calendar |
|---|---|---|---|
| FQ1'25 | $6,400mn | — | Sep–Nov 2024 |
| FQ2'25 | $6,123mn | **−4.3%** | Dec 24–Feb 25 |
| FQ3'25 | $7,071mn | **+15.5%** | Mar–May 2025 |
| FQ4'25 | $8,984mn | **+27.1%** | Jun–Aug 2025 |
| FQ1'26 | $10,812mn | **+20.3%** | Sep–Nov 2025 |
| FQ2'26 | $18,768mn | **+73.6%** | Dec 25–Feb 26 |
| **FQ3'26** | **$31,328mn** | **+66.9%** | **Mar–May 2026** |

*(C2 satisfied — this is the sequential series; the YoY comparators from the same tables are FQ3 $31,328mn vs $7,071mn and nine-month $60,908mn vs $19,594mn, and the sequential figures above are the ones this section reasons from.)*

★★★ **The two series disagree, and the disagreement is the finding.** Aligning roughly on calendar: `M1`'s **2Q CY26 leg is +58~63%**, and **MU's realized DRAM revenue in the quarter that mostly overlaps it (FQ3'26, Mar–May 2026) grew +66.9% sequentially — ABOVE the index, not below it.** A binding ceiling produces the opposite sign. **And `M1`'s decisive third leg (3Q CY26, +13~18%) has NO issuer counterpart yet**: MU's FQ4'26 (Jun–Aug 2026) has not been reported and prints **late September 2026**. ⇒ **The desk's regime call — "rate-of-change deceleration" — is currently resting its sharpest leg on an index quarter that the issuer has not yet confirmed, while the two issuer quarters that ARE reported decelerate by only 6.7pp (+73.6% → +66.9%), not by the ~45pp the index shows.** That is a materially weaker deceleration than the regime call describes, measured from primary filings.

**Regime call status: stays `[inferred]`, and this run REDUCES its support rather than corroborating it.** It is not falsified — the untested leg may well print — but it should be carried with the note that its issuer-side check, where available, runs the other way.

**Gross margin, computed directly from the filings' own income statements** (not from a data vendor): FQ3'25 rev $9,301mn / COGS $5,793mn = **37.7%**; FQ2'26 $23,860 / $6,105 = **74.4%**; FQ3'26 $41,456 / $6,400 = **84.6%**.

---

## §5 · VALUATION — every "cheap on forward multiple" claim, with margin-in-own-history and revision trend, and the IT-loading caveat applied

🚨 **IT-LOADING CAVEAT, binding and applied to every line below.** Measured 2026-08-09, the revision-breadth effect is **an IT loading (ex-IT Q5−Q1 = −1.1pp)**. **The revision table is a description of the denominator's DIRECTION, is NOT a leading indicator, and carries NO independent weight on an IT name.** Nothing below is argued from breadth. Breadth appears only as the denominator's direction, beside the multiple and the margin.

**MU** (`module_fundamentals_us MU`, this run): **forward P/E 6.04** vs trailing 21.16, PEG 0.13, price $935.23.
- **Margin in its own history** (`margin_history.py MU`, SEC XBRL, 17 years FY2009–2025): FY2025 **39.8%**, 17-yr **median 32.0%**, prior **cycle high FY2018 58.9%**, cycle low FY2009 **−9.2%**. Current *quarterly* GM from the 10-Q is **84.6%** — **25.7pp above the highest annual gross margin in MU's recorded history and 52.6pp above its own median.** ⇒ **The forward multiple is 6.04 because the denominator sits at an all-time extreme. "Cheap" is not an available reading of this number on its own.**
- **Revision trend, stated as denominator direction only:** current-year +26.2%/90d (30d breadth 29↑/1↓), next-year +52.1%/90d.
- ★★ **But the window matters, and this is the resolution of the run's "sharpest input."** The task framed MU's estimates as *"revised up massively WHILE the money leaves."* **On matched windows there is no contradiction.** The +26.2% is a **90-day** number and MU's `rs60` is **+21.2 vs `SPY`** — same window, same sign. **On the 7-day window every single estimate bucket is flat-to-DOWN**: current-Q 31.31→**31.30**, next-Q 34.83→**34.80**, current-year 73.40→**73.39**, next-year 155.09→**154.89**, with next-year 7-day breadth **0↑/1↓ — the first down-revision anywhere in MU's table** — and MU's `rs20` is **−1.6 vs `SPY`**. **Same window, same sign again.** ⇒ **The estimate axis and the price axis agree on both windows. The apparent contradiction was a window mismatch (90d estimates read against a 20d price), not a genuine divergence between fundamentals and flow.**

**HPE**: `[confirms PREMORTEM Lens 3 — EXHAUSTED]`. Flow +0.467, **OBV +0.318 accumulating alongside RS20 +21.7 and RS60 +73.1 vs `SPY`** (2nd-highest 60-day in the 300) — D6 satisfied by the paired RS axes. But the estimates are stalled: current-Q 0.92→**0.93** over 7/30/60 days, FY 3.41→**3.42**, next-year 4.00→**4.03**, and **the +41.5% FY headline is entirely 90-day-old (2.42→3.41 happened between the 90d and 60d marks and has moved +0.3% since).** ⇒ **The estimate move and the RS60 are the same 90-day object counted twice. `vol_surge` 0.64 says nobody is transacting it now. PREMORTEM's tag is confirmed on independent data.**

**ANET**: `EXTENDED-BUT-LIVE`, confirmed and sharpened. Flow +0.606, **OBV +0.358 accumulating with RS20 +20.1 / RS60 +43.8 vs `SPY`** (D6 paired). **Unlike HPE the movement is in the last 7 days, not 90**: current-Q **0.92 → 1.08 (+17.4%) inside 7 days**, next-Q 0.97→1.15, FY 3.64→4.11, next-year 4.47→5.16, all four buckets 3↑/0↓ on 7 days. **FINRA z −0.79 (no crowding).** ⇒ **ANET is the one name in the sector whose estimate move and price move share the SAME short window.** No multiple claim is made — the point is the window alignment, not cheapness.

**DELL**: `rs60` **+95.7 vs `SPY`** = highest in the 300, delta **+0.909** = largest in the universe, FY +42.7%/90d (3↑/0↓), current-Q +66.8%/90d. **But FINRA short-volume z re-pulled this run = +3.31 (extreme vs its own 20-day base, short% 62.1% vs base 41.5%, 5v5 trend +7.5 rising)** ⇒ **the largest delta in the universe is being met by the heaviest crowding-short of the runners, and the two are not independent readings of the same tape.** `CSCO` carries the same conflict (flow +0.600, delta +0.394, **OBV +0.367 accumulating with RS20 +8.5 vs `SPY`** — D6 paired — but FINRA z **+3.80**, the highest measured). **KLAC z +2.42** is the third.

**ORCL**: flow +0.546, RS20 **+13.3 vs `SPY`** but **RS60 −25.1 vs `SPY`** — the only 🟢 in the sector whose 60-day is deeply negative. ⇒ **a recovery shape, structurally the inverse of the memory chain's (positive 60-day / negative 20-day) and worth naming as its mirror image, not as a confirmation.**

---

## §6 · ★★★ AUDIT OF EVENT_ALPHA CARD 4 — it fails two independent tests run this run

Card 4 asserts: *"Five of six carry the identical signature: a strong 60-day, a negative 20-day, and OBV distribution"* and *"The money agrees, and it is unambiguous."* **The signature is a conjunction of an RS60 leg and an RS20 leg (both vs `SPY`) with an OBV leg, so it is auditable on its two A/B-grade axes independently of the C-grade one — and §6a below fails it on the `RS60` leg alone.** **Three findings, all measured this run.**

### 6a · The count is wrong on Card 4's own table
The signature requires a **strong 60-day**. **`WDC`'s RS60 is −10.3 vs `SPY` and `SNDK`'s is −9.0 vs `SPY`** — both negative, both printed in Card 4's own table. ⇒ **4 of 6 carry the signature (MU, AMAT, LRCX, KLAC), not 5 of 6.** And **3 of those 4 are semicap equipment, not memory**: the "memory sub-chain" claim is carried by **one memory maker and three equipment makers**.

### 6b · The signature is not memory-specific — universe base rate measured
Applying `rs60>0 ∧ rs20<0 ∧ obv_norm<0` (vs `SPY`) across all 300 names:

| | hits / n | rate |
|---|---|---|
| **Financials** | 11 / 47 | **23.4%** |
| Real Estate | 2 / 12 | 16.7% |
| **Information Technology** | 8 / 56 | **14.3%** |
| Utilities | 2 / 15 | 13.3% |
| Industrials | 6 / 50 | 12.0% |
| **UNIVERSE** | **33 / 300** | **11.0%** |

⇒ **The "identical signature replicated across a value chain" occurs in 11.0% of the whole market and IT ranks only 3rd of 11 — Financials carries it at a 64% higher rate (GS, MS, AXP, MCO, SPGI, HOOD, BNY, STT…).** It is **the generic 60-day-winner / 20-day-fader shape of a market-wide rotation**, not a memory-chain diagnosis. Card 4 did not test the base rate, and against an 11.0% background the IT clustering is not a distinctive event.

### 6c · ★★★ The OBV state does not replicate on the desk's SECOND producer — 6 of 7 names contradict
`module_chart <TKR> --read` run on every chain name this run, against `SECTOR_FLOW_US.json`'s `obv_state` on the **same settled 08-12 bar**:

| Ticker | `SECTOR_FLOW` `obv_norm`/state | `module_chart --read` OBV | Chart turn-verdict | Verdict |
|---|---|---|---|---|
| **MU** | −0.161 · 분산 | **누적 accumulating, 20d slope +43%** | PULLBACK-TO-SUPPORT, no divergence | 🚨 **CONTRADICT** |
| **AMAT** | −0.108 · 분산 | **누적, +33%** | PULLBACK-TO-SUPPORT | 🚨 **CONTRADICT** |
| **LRCX** | −0.179 · 분산 | **누적, +45%** | PULLBACK-TO-SUPPORT | 🚨 **CONTRADICT** |
| **KLAC** | −0.139 · 분산 | **누적, +33%** | PULLBACK-TO-SUPPORT | 🚨 **CONTRADICT** |
| **SNDK** | −0.176 · 분산 | **누적, +38%** | PULLBACK-TO-SUPPORT | 🚨 **CONTRADICT** |
| **STX** | **+0.215 · 매집** | 중립, −6% | PULLBACK-TO-SUPPORT | 🚨 **CONTRADICT (opposite direction)** |
| WDC | −0.112 · 분산 | 분배, −64% | **BASING, BULLISH divergence** | ✅ agree on state |

> **RULE D6 — exemption stated with its reason.** This table makes an OBV state the **subject** of a two-producer disagreement, not the **evidence** for a proposition. D6 forbids a C-grade axis from carrying a claim alone; the claim here is *"two desk producers disagree,"* which cannot be written without naming both readings, and neither reading is used to support anything downstream. The RS20/RS60 values vs `SPY` for every name in this table are printed in §1 and §2.

⇒ **EVENT_ALPHA Card 4's central assertion — *"the money agrees, and it is unambiguous"* — is the output of ONE of the desk's two OBV producers, and the other producer reports the opposite state on 5 of 6 names, plus the opposite sign on the 7th.** Five of those names additionally read **PULLBACK-TO-SUPPORT with no divergence** — a trend-pullback shape, not a distribution top. **This is the second instance of this exact producer conflict** (`D208`, 08-10, on PLTR) and by far the largest: **7 names on one bar.**

★ **And Card 4 is one leg from its own kill condition.** Its stated kill: *"if MU's OBV turns to accumulation AND RS20 vs `SPY` turns positive."* **Leg 1 is already satisfied on `module_chart` (누적, +43%).** Leg 2 is not (MU RS20 **−1.6 vs `SPY`**). **The card should be carried as ONE OBSERVABLE from being killed by its own terms, not as settled counter-evidence.**

### 6d · Two omissions from Card 4's chain that cut the other way
- **`STX` (Seagate) is absent from Card 4's table** despite being a node-5 storage name. It reads flow **+0.454**, **OBV +0.215 accumulating with RS20 +3.7 and RS60 +5.9 vs `SPY`** (D6 paired), delta **+0.553** = 2nd-largest positive change in the sector, and **its estimates jumped +29.0% in 30 days** (FY 27.74 → 35.78, 7-day breadth 3↑/0↓). ⇒ **"Every US expression of the memory chain is distributing" is false as written; the counter-example was in the universe and was not listed.**
- **The Δ column contradicts the direction of travel.** Card 4's own six carry **5 of 6 POSITIVE one-session deltas** (MU **+0.272**, AMAT +0.143, LRCX +0.115, KLAC +0.060, WDC +0.055; only SNDK −0.039) on the Δ that ROTATION itself certified as *"the cleanest Δ this desk has had in a week"* (PREFLIGHT G0+G2 PASS). **Whatever the level says, the change is improving across the chain.**

### 6e · Estimate axis also refuses "identical" — the chain is dispersed on 7-day breadth
| | 7-day breadth (current-Q) | 7-day value move | Reading |
|---|---|---|---|
| **LRCX** | **4↑ / 0↓** (all 4 buckets 3–4↑/0↓) | — | actively revising **up** |
| **STX** | 3↑ / 0↓ | FY +29.0% in 30d | **strongest live revision in the node** |
| AMAT | 0↑ / **1↓** | next-yr 17.05→17.34 | mixed |
| MU | 1↑ / 0↓ | **all 4 buckets flat-to-down** | **stalled** |
| **KLAC** | **1↑ / 2↓** (30d: 5↑/**6↓**) | — | **the only NET-NEGATIVE breadth in the chain** |

⇒ **On the estimate axis the "identical signature" fully dissolves: LRCX and STX are accelerating, MU is stalled, KLAC is the only genuine deterioration.** (IT-loading caveat from §5 applies — this is denominator direction, carrying no independent weight; it is used here **only** to refute a claim of uniformity, which is a claim about dispersion, not about level.)

---

## §7 · CUSTOMERS — the hyperscalers, from disclosed capex (primary filings, this run)

The memory node's regime call is a **demand** proposition, and the demand sits with four buyers **who are not in this sector's 56 names**. `PaymentsToAcquirePropertyPlantAndEquipment`, SEC XBRL companyconcept, pulled this run:

| Buyer | Latest **disclosed** capex | **Sequential (QoQ)** | Filed | Next print |
|---|---|---|---|---|
| **AMZN** | **$54.21bn** (qtr ended 2026-06-30) | **+22.6%** vs $44.20bn (Q1'26) | **2026-07-31** | ~late Oct 2026 |
| **GOOGL** | **$80.60bn** (1H 2026) ⇒ Q2 ≈ **$44.93bn** | **≈ +26.0%** vs $35.67bn (Q1'26) | **2026-07-23** | ~late Oct 2026 |
| **META** | **$49.11bn** (1H 2026) ⇒ Q2 ≈ **$30.11bn** | **≈ +58.5%** vs $19.00bn (Q1'26) | **2026-07-30** | ~late Oct 2026 |
| **MSFT** | **$115.95bn** (FY26, ended 2026-06-30) ⇒ Q4 ≈ **$35.80bn** | **≈ +15.9%** vs $30.88bn (Mar-Q) | **2026-07-29** (10-K) | ~late Oct 2026 |

*(GOOGL/META/MSFT quarterly figures are differenced from disclosed cumulative periods — `[computed from filings]`, not separately tagged line items.)*

★★ **All four buyers accelerated sequentially in the June 2026 quarter, aggregate ≈ $165bn, and every one of those disclosures is 2–3 weeks OLD (filed 07-23 to 07-31) — they were public BEFORE the 08-12 tape this run reads.** ⇒ **The demand anchor is disclosed, sequential, accelerating, and already in the price. It is a level fact, not a fresh catalyst,** and it is consistent with `STANDING_VIEW §1`'s *"level stays tight."* **The next observable on this node is the late-October Q3 print cluster** — **no hyperscaler capex disclosure arrives between now and then**, which is a dated, structural gap in the chain's information flow, not a signal.

⚠ **Lead/lag discipline:** no claim is made here that capex leads memory pricing. **That relationship is `[unverified]` — it was not measured this run** and the desk has no measured lead/lag estimator on this pair. The four prints are reported as a **contemporaneous level and its sequential direction**, nothing more.

---

## §8 · ★★★ P43 — CXMT / Apple. **CLOSED with a dated answer after four stale runs.**

**The news tunnel is up and was actually used.** `python -X utf8 -m module_news_data fts search CXMT --days 30` → **1,037 matches** (denominator stated). Follow-ups: `fts search CXMT price cut --days 14` → **64 matches**; `fts search CXMT refused prices --days 7` → **4 matches**, full body read. **Filing check run: `module_disclosure_us MU --days 150` → 50 filings, and `--days 400` → 1 10-K, 3 10-Q, 11 8-K. NOTHING mentioning CXMT appears in any MU filing; the 10-Q body was fetched and searched directly — zero hits.** For AAPL the same axis is `[news]`-only. ⇒ **Filing status: NOTHING FOUND, denominator 50 filings/150d.**

**★ The finding reverses the axis's expected sign, and this is the run's second-most important result after §0.**

`[news — yahoo_finance body 2026-08-12, "Apple is testing Chinese DRAM even after CXMT refused to cut prices"]`, read in full:
> *"its attempt to negotiate cheaper pricing did not go as planned. **CXMT quoted prices comparable to or even higher than Samsung and SK Hynix.** Huawei, Xiaomi, and other Chinese manufacturers have also **locked up much of its available output through long-term agreements**, giving CXMT little reason to offer Apple the kind of discount it usually expects."*

Corroborated on four independent bodies pulled this run:
- *"Apple's interest in CXMT is **primarily about securing supply rather than cutting costs**"* [`yahoo_finance` 08-10]
- *"Lexar lists 32GB DDR5 with homegrown Chinese chips — 3,999 Yuan ($592) price **undercuts hopes for cheaper CXMT-powered RAM**"* [`tomshardware` 08-03]
- *"CXMT has been able to **increase its prices** and gain [share]"* [`fool`/`nasdaq` 07-31]
- *"HP, Asus, and Acer using **'small amounts'** of CXMT chips in **limited number of notebooks for non-US market**"* [`tomshardware` 08-04]
- Also surfaced and NEW to the desk: **CXMT listed in Shanghai 2026-07-27 on a $9.8bn IPO, +466% on debut** [multiple, 07-27], and **"CXMT plans second chip plant in Beijing and is in talks on its funding"** [`yahoo_finance` exclusive, 08-03].

⇒ **P43 VERDICT, dated 2026-08-13.** The CXMT axis is **REAL, is CLIENT/CONSUMER DRAM only** (DDR5-8800 on an AMD platform; iPhone/MacBook; "small amounts"; non-US notebooks — **no HBM or server qualification named in any of the 1,037 matches**), and — **contrary to how a new-entrant supply story is normally carried — it is NOT a price-relief axis.** CXMT is **quoting at or above the incumbents, refusing discounts, has its output pre-committed to Chinese OEMs under long-term agreements, and is raising prices.** Apple is reported to be pursuing it **to secure volume, not to lower cost**, and is seeking US-government clearance first. ⇒ **On the evidence available today the CXMT axis corroborates the "level stays tight" half of `STANDING_VIEW §1` and supplies NO support for the price-deceleration half.** Its capacity build (IPO proceeds + second Beijing fab) is a **2027-and-beyond supply argument**, not a 2026 price argument.

**Grade: `[news]`, multi-outlet (5+ independent bodies), issuer-filing corroboration = ZERO. Not promoted. Not handed to BET.** **Explicit anti-signal, unchanged and now dated: a named CXMT HBM or server-DRAM qualification at any hyperscaler or GPU vendor.** **Re-check: 2026-08-27.**

---

## §9 · FRAME-TRANSFER QUESTION — one, answered

**Q: Insurance underwriting distinguishes a *hard market* (price rises because capacity left) from a *capacity-constrained market* (price rises because demand outran committed supply, with capacity still arriving). The tell is not the price level — it is whether incumbents are writing multi-year fixed contracts. Which is memory in?**

**A: Memory is behaving like a *capacity-constrained* market that its incumbents are converting into contracted infrastructure — and the desk's price-cycle frame is the wrong template for the contracted portion.** The evidence, all pulled this run: MU has written **16 take-or-pay agreements, mostly 5-year 2026–2030, ~$100bn minimum contracted revenue, ~$22bn cash deposits**, and management targets **"half or more" of revenue** under them; **SanDisk discloses 8 contracts / 6 customers / $93.9bn, targeting half of bit production covered in FY27 and two-thirds in FY28** [`yahoo_finance`/Zacks 08-11]. **Underwriters do not lock five-year floors into a market they expect to stay hard — they lock floors when they expect the hard phase to END and want to carry the peak forward.** ⇒ **The producers' own contracting behaviour is a bet that prices fall, and simultaneously the mechanism that stops the fall reaching their P&L for the covered share.** The frame transfer therefore says something the price-cycle frame cannot: **for the contracted 20–40%, "peak margin must mean-revert" is not a price question at all — it is a counterparty-credit and take-or-pay-enforceability question**, and *that* is the risk the desk is not currently tracking. **The uncontracted 60–80% remains a pure price-cycle exposure and the peak-margin lens applies to it in full** (84.6% quarterly GM vs a 58.9% all-time annual high, §5).

---

## §10 · TRACK KPIs AND ANTI-SIGNALS — dated observables

**KPIs (what would confirm this file's readings):**
1. **`XLK` volume normalises above `vol_surge` 1.0 while it holds positive excess vs `SPY`** ⇒ §0's "thin squeeze" reading is wrong and the bid is demand-led. **Check every run; first meaningful window 2026-08-19.**
2. **Nasdaq-100 spec net rises off the 0th percentile** (`us_flow.py --cot`; COT is Tuesday-dated, Friday-released, 3–4 day lag). **Next release 2026-08-14, then 08-21.**
3. **MU's `SECTOR_FLOW` `obv_state` flips to 매집 AND `rs20` turns positive vs `SPY`** ⇒ **EVENT_ALPHA Card 4 is killed by its own stated terms.** Leg 1 already reads accumulating on `module_chart` (§6c). **Check every run.**
4. **MU FQ4'26 results (~late September 2026)** — the **first issuer print covering the 3Q CY26 quarter where `M1` claims +13~18%.** This is the single highest-information dated observable on the regime call. **§4's series gets its decisive point here and nowhere earlier.**
5. **Hyperscaler Q3 capex cluster, ~late October 2026** (AMZN/GOOGL/META 10-Q, MSFT FY27Q1). **No capex disclosure exists between now and then (§7).**
6. **Networking cluster (node 7) holds `eqflow` > 0 with 0 reds** — it is the cleanest expression of node-1 capex without node-5 price risk. **Check every run.**

**ANTI-SIGNALS (what would break this file):**
- **A named CXMT HBM or server-DRAM qualification at any hyperscaler or GPU vendor** ⇒ §8's client-only containment fails and P43 becomes a node-5 price event. **Re-check 2026-08-27.**
- **`module_chart` and `SECTOR_FLOW` OBV states RECONVERGE on the memory chain with both reading 분산** ⇒ §6c's producer-disagreement finding collapses and Card 4 stands. **Check next run.**
- **IT `vol_surge` stays below 0.8 while `XLK` excess vs `SPY` turns negative on exc5** ⇒ §0's decomposition was right about the mechanism but the direction axis was late, and the N tilt should be re-examined downward.
- **MU 7-day estimate breadth turns net-negative across two or more buckets** (currently 0↑/1↓ on next-year only) ⇒ §5's "stalled, not falling" reading becomes "falling," which would be the first genuine estimate-side deterioration at node 5. **Check every run.**
- **`DELL` or `CSCO` FINRA z drops below +1.0 while their deltas stay positive** ⇒ the crowding conflict named in §5 resolves in favour of the delta and those readings need re-basing.

---

## §11 · WHAT WOULD SETTLE WHAT THIS FILE COULD NOT

Two things remain genuinely unresolved and neither is resolvable with the desk's current instruments:

1. **The contracted share is `[news]`-graded and the two sources disagree 2× (20% of DRAM volume vs 40% of DRAM bits).** **What would settle it:** MU's **FY2026 10-K**, expected ~early October 2026, which will be the first annual filing written entirely after the SCA book was signed and is the first document obliged to describe it at full-year scope. Until then §3a's bound is 20–40% and the arithmetic in that range is what it is.
2. **The OBV producer conflict (§6c) has no arbiter on this desk.** `module_chart` uses a 20-day OBV slope; `SECTOR_FLOW` uses a normalised `obv_norm`. **What would settle it:** a real investor-flow series (the KR desk has `module_kis --investor`; **the US desk has no equivalent and this is the third distinct run where that gap has decided an argument**). Absent it, **no US verdict on this desk should rest on OBV state alone** — which is exactly what rule D6 already says and what Card 4 did anyway.

---

**EXIT CHECK** — 1) full fresh chain map, §2, 8 nodes, binding constraint named ✅ · 2) explicit resolution verdict on the three-stage disagreement, §0 ✅ · 3) QoQ series for the memory price node, §4, built from three primary filings ✅ · 4) forward-multiple claims carry margin-in-own-history + revision trend + IT-loading caveat, §5 ✅ · 5) contract terms read from the filing, share now bounded 20–40% (`unknown` retired), ceiling tested and found insufficient, §3/§3a ✅ · 6) one frame-transfer question answered, §9 ✅ · 7) customers named, disclosed capex pulled, print dates given, §7 ✅ · 8) lead/lag claims measured or tagged `[unverified]`, §7 ✅ · 9) sub-sector dispersion measured at 7.3–10.0× the sector move, sector label declared the wrong unit, §1 ✅ · 10) KPIs + anti-signals as dated observables, §10 ✅ · 11) dated P43 answer with denominators, §8 ✅

**Linter**: `python -X utf8 scripts/report_lint.py llm_outputs/2026-08-13/industry_US/SECTOR_DEEP_IT.md` — result recorded at run time. One declared exemption: **§6c's D6 exemption**, stated in-place with its reason (the OBV state is the *subject* of a producer disagreement, not evidence for a downstream claim; RS20/RS60 vs `SPY` for every name in that table are printed in §1–§2).

**The place this file would break first**: §0's decomposition assumes `flow_score`'s three axes are equally weighted and un-clipped at the margin. They are equally weighted by construction (`sector_flow.py:176`, verified by reading the source), but **clipping is asymmetric in practice** — a name at `vol_surge` 0.4 floors the volume axis at −1.0 while a name at `vol_surge` 1.6 caps it at +1.0. **Zero of 300 names floored this run** (checked), so the decomposition is clean today; **on a high-volume day it would not be, and the "volume axis owns the sign" claim must be re-derived rather than carried forward.**
