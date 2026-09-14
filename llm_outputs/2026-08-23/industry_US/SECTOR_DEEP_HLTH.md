# SECTOR_DEEP_HLTH — Health Care (OW) · industry_US · 2026-08-23 (Sun) · Stage 8 / L1·DEEP
### Continuous slot 2 of 2 — **DELTA-led** (covered 08-22; structure carried by reference)

> ⚠ **`n_new_sessions_since_prior_run = 0`.** All flow numbers are the **2026-08-21** settle,
> identical to the 08-22 file. **The delta in this file is a MEASUREMENT delta, not a price delta.**

## 0 · ★★★ The mandate, answered — and answering it broke the instrument the mandate was written in

ROTATION's mandate: *"18 names blocked by `vol_surge` alone — the largest blocked set of any sector.
Is the leadership broad, or is it `LLY` plus 18 names the gate cannot see?"*

### The answer: **the leadership is emphatically BROAD, and the two largest weights are its weakest participants.**

| | Reading |
|---|---|
| Names with `OBV 매집` **and** `rs20 > 0` | **19 of 32 = 59.4%** — the **second-highest participation on the board** |
| Names clearing 🟢 (adds `vol_surge ≥ 1.2`) | **1 of 32** (`MRK`) |
| `eqflow` **+0.229** vs `wflow` **+0.196** | `eqflow` > `wflow` ⇒ **breadth-led, not mega-cap-narrow** |
| **`LLY`, 19.4% of the sector** | flow **+0.160**, **OBV 중립 +0.056**, rs20 **+1.3** — ranks **22nd of 32** on flow |
| **`JNJ`, 10.9%** | flow **+0.197**, rs20 **−1.0** — ranks **21st of 32** |
| Top of the sector | `MRK` +0.978 · `A` +0.711 · `BSX` +0.683 · `AMGN` +0.639 · `HCA` +0.611 · `BDX` +0.589 — **weights 5.6% / 0.7% / 1.3% / 3.6% / 1.6% / 0.8%** |

⇒ **The 30.3% of the sector that is `LLY` + `JNJ` contributes almost none of its strength.** The
sector's OW is carried by mid-weight pharma and devices. `top1_flips_sign` is **false** (`wflow`
+0.196 → ex-`LLY` **+0.205** — removing the largest name makes it *stronger*).

### `M835` — 🚨 **`breadth` in `SECTOR_FLOW.json` is NOT a participation measure. It is the 🟢 rate.**

Answering the mandate required computing participation by hand, and that exposed the metric every
stage of this run has been quoting. **Source, verbatim — `scripts/sector_flow.py:342`:**

```python
"breadth": round(greens / len(names), 2),
```

**`breadth` ≡ 🟢 / n.** And 🟢 requires the three-axis gate **including `vol_surge ≥ 1.2`.**
⇒ **`breadth` is a volume-surge frequency wearing a participation label.**

**The board, with both numbers side by side:**

| Sector | n | `breadth` (=🟢/n) | **true participation** (`OBV 매집 ∧ rs20>0`)/n |
|---|---:|---:|---:|
| **Communication Services** | 12 | **0.000** | **66.7%** (8/12) — **highest on the board** |
| **Health Care** | 32 | 0.031 | **59.4%** (19/32) |
| **Consumer Discretionary** | 28 | **0.000** | **39.3%** (11/28) |
| **Energy** | 16 | **0.000** | **37.5%** (6/16) |
| Consumer Staples | 19 | 0.053 | 31.6% (6/19) |
| Information Technology | 56 | 0.036 | 30.4% (17/56) |
| Financials | 47 | 0.021 | 29.8% (14/47) |
| Materials | 12 | 0.083 | 25.0% (3/12) |
| Real Estate | 12 | **0.000** | 16.7% (2/12) |
| Industrials | 50 | **0.000** | 16.0% (8/50) |
| **Utilities** | 15 | **0.000** | **0.0%** (0/15) |

★★★ **The six sectors reading `breadth 0.000` span participation from 66.7% to 0.0%, and the metric
cannot tell them apart.** Utilities is the **only** sector where the two agree — and it is the one
this run gave a DEEP slot to on that reading, which is luck, not method.

🚨 **Self-refutation, written down rather than edited away (`D48`).** **This run's own ROTATION §2
attempt 3 cited *"breadth 0.000 of 28 names"* as evidence for demoting Consumer Discretionary.** That
evidence was misread: DISC's true participation is **39.3%**. **The verdict does not change — the
demotion was declined — but the reasoning that supported the decline was wrong**, and SWEEP §3's
reading of Communication Services as *"structurally unreadable"* is now known to be the opposite:
**COMM has the highest participation on the board.**
⇒ Registered as a dig at run end. **Positive-form remedy: publish `participation` = (`OBV 매집` ∧
`rs20 > 0`)/n beside `breadth`, and rename `breadth` to `green_rate`.**

## 1 · The sector is TWO businesses, and only one of them is the OW (`W5`)

| Node | Names | Flow | OBV | rs60 |
|---|---|---|---|---|
| **Pharma + devices + tools — the OW** | `MRK` +0.978 · `A` +0.711 · `BSX` +0.683 · `AMGN` +0.639 · `BDX` +0.589 · `PFE` +0.583 · `MDT` +0.583 · `TMO` +0.568 · `DHR` +0.552 · `GILD` +0.550 · `REGN` +0.550 · `ISRG` +0.539 · `VRTX` +0.539 · `ABT` +0.528 · `WAT` +0.471 · `BMY` +0.379 · `EW` +0.325 | **all positive** | **매집 ×17, no exception** | **+34.1 to −11.5**, median **≈ +23** |
| 🚨 **Managed care + distribution — the drag** | `CVS` **−0.783 🔴** · `UNH` **−0.719 🔴** · `CI` −0.651 · `MCK` −0.403 · `HUM` −0.349 · `CAH` −0.252 · `COR` −0.206 | **all negative** | **분산 ×3, 중립 ×4 — zero 매집** | −4.9 to +21.7 |

★ **17 of 17 in the first group are OBV 매집; 0 of 7 in the second are — and OBV is the third agreeing axis, not the claim (`RULE D6`): all 17 also carry `flow_score` > 0 AND rs20 > 0, while all 7 carry `flow_score` < 0.** The split is total, with no
overlap — the same shape `M805` measured in Financials (six of six large banks sharing one form, five
of nine reds insurers). ⇒ **`W5` fires: an OW on "Health Care" is an OW on pharma/devices and an
implicit UW on managed care.** The desk holds neither.
⚠ **`UNH` and `CVS` together are 9.7% of the sector** and are the only two 🔴.

## 2 · The 18 blocked names — what the gate is actually excluding

**18 of the 19 participating names fail 🟢 on `vol_surge` alone.** Their median surge is **0.85**,
against a gate of 1.20 and a universe median of 0.82. Highest-conviction of the blocked set by the
two axes that are allowed to speak:

| Ticker | flow | `obv_norm` | rs20 | rs60 | surge |
|---|---:|---:|---:|---:|---:|
| `REGN` | +0.550 | **+0.656** (2nd-highest OBV in the sector) | **+23.5** | +30.8 | 0.79 |
| `BDX` | +0.589 | +0.437 | **+19.2** | +28.4 | 0.86 |
| `ABT` | +0.528 | +0.461 | +9.6 | **+34.1** | 0.75 |
| `A` | +0.711 | +0.186 | +11.1 | **+35.2** | 1.08 |
| `TMO` | +0.568 | +0.339 | +7.1 | **+35.9** | 0.89 |
| `PFE` | +0.583 | **+0.517** | +10.8 | +5.1 | 0.85 |

⇒ **These are not marginal names.** `REGN`, `BDX`, `ABT`, `A` and `TMO` carry rs60 of **+28 to +36**
with OBV accumulating, and every one is excluded by a volume statistic that the desk's own
`ic_ledger` measures at **t(NW) −3.86** — in the wrong direction, in another market (`W1`).
⚠ **No name is advanced to BET from this list** (P4, and the `W1` bar). **The finding is about the
gate, not about the names.**

## 3 · Track KPIs and anti-signals

| KPI / anti-signal | Current | What kills the OW |
|---|---|---|
| `eqflow` rank | **+0.229, rank 1 of 11** | falls below rank 4 |
| Participation | **59.4%** | falls below 40% |
| Pharma/devices OBV unanimity | **17 of 17 매집** | any 4 of the 17 leave 매집 |
| Managed-care contagion | `UNH`/`CVS` contained at 9.7% weight | a third and fourth name turns 🔴, i.e. the drag stops being one node |
| Duration exposure | ⚠ `DGS30` at the **96.4th %ile** — Health Care is the longest-duration OW the desk holds | `S112` (Jackson Hole, settles 08-31) branch B |

## 4 · Verdict on the mandate

**Broad, and the mandate's own premise was the wrong worry.** The concern was that the sector was
`LLY` plus invisible names. **It is the opposite: `LLY` and `JNJ` are 30.3% of the weight and 21st and
22nd of 32 on flow, while 19 of 32 names participate.**
★ **The mandate's real yield is `M835`** — answering it required a participation number the desk does
not publish, and computing that number showed **`breadth` has never measured breadth.**
⚠ **P4 — no sizing, no names advanced.**
