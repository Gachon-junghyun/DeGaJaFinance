# SWEEP_READ — industry_US · 2026-08-19 · Stage 4/11 (L1·SWEEP)

> The reading only. Every sector row and every shortlist row lives in
> `SECTOR_FLOW_US.json §sector_rotation` / `US_LIVE_SHORTLIST.json` and is **cited, not reprinted**.

## 0 · 🚨 Instrument health line, read before any number

`SECTOR_FLOW_US.json §scoring` — `vel_axis false · vel_coverage 0.1706 · n_axes 3 · scored 299 ·
dropped_missing_axis 0`. `asof` **2026-08-18**.

**News axis DEAD this run (7th consecutive), and the cause is the pipe, not silence — probed, not
assumed.** 40 names the sweep called silent returned **0/40** at 21:53 and **40/40** at 21:57 on the
identical call; the CLI returned **0/5** at 21:54 and **3/3** at 21:58; the transport failure surfaces
as `SSLEOFError` at the TLS handshake. Cumulative falsification record: **0 genuinely quiet in 200
hand-probes.** Full detail in `preflight/PREFLIGHT_US.md §G1`.
⇒ `velocity`, the 51 survivors as a set, theme freshness, and `breadth` as a news-independent
statistic are **all revoked for this stage and every stage downstream**.

✅ `dropped_missing_axis 0` — all 299 names scored on the **same** 3 axes. The 08-09 inflation path
(+0.305 average) stayed closed.

## 1 · Universe headline

**n = 299 · wflow −0.170 · 8 🟢 / 63 🔴 · new-🟢 2 (`RTX`, `WMT`).**
⚠ Per `M25` the 🟢 count is a **`vol_surge` count, not a flow count** — see §3, where that turns out to
be the whole story of this sweep.

★ **`asof` moved 08-14 → 08-18: two settled sessions, the first advance in six runs.** Every `delta`
in the JSON is therefore a **two-session** change, not a daily one (PREFLIGHT G2).

## 2 · Cross-checks against the MACRO transmission matrix

**Two confirmations, two contradictions. The contradictions are the useful half.**

**✅ CONFIRMS — Utilities UW.** The only sector with **0 of 15** names on `OBV 매집 ∧ RS20>0`, and
`eqflow −0.376` ≈ `wflow −0.397` ⇒ the weakness is **uniform, not one name**. MACRO's β-adjusted price
column reads +0.150 (flat), and the `utility` term ran the board's **highest CLI velocity, 1.22×**.
⇒ **Attention up, money absent, price flat.** Money and matrix agree; only the narrative disagrees.

**✅ CONFIRMS — IT's downgrade.** IT carries **`delta −0.218`, the board's only materially negative
two-session delta** (next worst `XLRE` −0.015). MACRO marked IT `N+ → N (watch)` on `XLK` being the
week's worst raw sector. The flow axis moved the same way independently.

**🚨 CONTRADICTS — Communication Services.** `wflow −0.439` vs `eqflow −0.009`: a **0.430 gap, the
widest on the board**, i.e. the cap-weighted print is almost entirely `GOOGL` (38.3% weight) and the
median name is flat. But MACRO's **β-adjusted** price column puts `XLC` at **−0.930, the board's
worst**. ⇒ **Flow says "one name"; risk-adjusted price says "the whole sector".** The money is on the
flow side (`eqflow` is the breadth statistic and it is ~0); the price side is measuring something the
flow axes do not carry. **Carried to ROTATION as an open split, not resolved here.**

**🚨 CONTRADICTS — Consumer Staples.** The sector holds the board's **largest two-session delta,
+0.325**, and is one of only two sectors where `wflow` is positive while `eqflow` is negative
(**+0.083 / −0.020**) — a mega-cap-led improvement, with `WMT` one of the run's two new-🟢. MACRO
holds Staples at **UW−** and its β-adjusted excess is **−0.592** (the raw +0.852 flips sign under
adjustment). ⇒ **The flow axis says Staples improved more than anything else on the board over these
two sessions; the risk-adjusted price says it is a laggard whose raw print was misleading.**
Both readings are measured. **ROTATION must not resolve this by picking the more convenient one.**

⚠ **Binding on all four**: `Financials · Industrials · Materials` may not be promoted or demoted on
`wflow` (G3 flippers `BRK-B` 13.9% · `CAT` 8.7% · `LIN` 24.7%), sector weights are **35 days stale**,
and `breadth` is news-contaminated and may not be read as an independent statistic.

## 3 · Shortlist composition — the absences, each diagnosed

`US_LIVE_SHORTLIST.json`: **8 names** past `mcap ≥ $10bn ∧ 🟢가속`. **7 of 11 sectors produced zero.**

★ **The absences are not evidence about those sectors. They are one filter, measured:**

| Sector | names | `OBV 매집 ∧ RS20>0` | of those, `vol_surge ≥ 1.2` | max `vol_surge` in sector |
|---|---|---|---|---|
| **Energy** | 16 | **7** | **0** | **1.06** |
| **Health Care** | 32 | **17** | **0** | **1.00** |
| Communication Services | 12 | 6 | 0 | 0.91 |
| Consumer Staples | 19 | 6 | 0 | **1.62** |
| Utilities | 15 | **0** | 0 | 1.45 |

- 🚨 **Energy — the sharpest artifact on the board.** Energy is **rank 1 by `wflow` (+0.354)**, the only
  sector whose MACRO lead survives β-adjustment (**+3.919**), and it produced **0 shortlist names and
  0 🟢 and 0 🔴 — all 16 names are 🟡.** Seven are OBV-accumulating with positive RS20, and **not one
  clears `vol_surge` 1.2; the sector's maximum is 1.06** (`MPC` 1.06 flow +0.700 · `PSX` 1.05 flow
  +0.694 · `COP` 0.87 · `BKR` 0.78 · `VLO` 0.72). ⇒ **A pure volume-gate exclusion — this is the
  documented "ENRG shortlist of 0" artifact reproducing exactly.** The absence is **not** evidence
  against Energy and may not be cited as such.
- 🚨 **Health Care — the same artifact, and it is `S76` leg 2.** **17 of 32** pass `OBV 매집 ∧ RS20>0`
  and **0 of 17** clear `vol_surge` 1.2; the sector's maximum is **1.00**. This is `M144`'s **7th**
  replication and it is what `S76`'s leg 2 was registered to test (settles tonight; the pre-settle
  count is 17, mid-band between A ≤10 and B ≥22).
- ✅ **Utilities — a genuine absence, not an artifact.** **0 of 15** pass the accumulation test at all,
  *before* the volume gate is applied, even though the sector's max `vol_surge` is **1.45** (i.e. the
  volume was there; the accumulation was not). This is the only one of the five that is real evidence.
- **Communication Services / Consumer Staples** — mixed: both have accumulation candidates blocked by
  the gate, but Staples' max `vol_surge` **1.62** shows volume does exist there, so its absence is a
  per-name gate failure rather than a sector-wide one.

**Composition of the 8 that did pass** (rows in the JSON, not reprinted): Financials 3 · IT 3 ·
Industrials 1 · Staples 1. Short-pressure verdicts: **3 clean-rise** (`KKR` −1.47 · `LITE` −1.07 ·
`ORCL` −1.20 FINRA short-z) · 5 normal · **0 crowded-short** ⇒ no squeeze fuel on this board, and no
name here is carried on a short-cover mechanism.
⚠ `LITE` is one of `S96`'s two names (settles 08-21) and appears here on a **`velocity`-free** basis —
its `flow_score` +0.54 uses no news at all, which is the only reason it is admissible today.

## 4 · ✅ Held-but-not-in-universe check

**0 — all 11 US holdings (`ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX`) are in `us_top300` AND
scored.** The `TSM`/`LNG` invariant holds this run.
⚠ Separately, **`EA` is in the universe and absent from the sweep for the 7th consecutive run** — not
a held name, so it is not a 🚨 here, but it remains **unmeasurable**, never "no signal".

## 5 · CYCLE_EXPOSURE GAP

`llm_outputs/2026-08-19/CYCLE_EXPOSURE.md` — **✅ no top-rank cycle GAP.**
AI-compute/semis rank 1: epicenter **19.82%** vs need 12.0% (`AVGO`, `NVDA`, `ANET`) ·
Energy/oil-refining rank 2: **9.64%** vs need 8.0% (`MPC`, `PSX`) ·
Missile-defense rank 3: 5.97% (`RTX`), ⚪ no threshold set.
⇒ **Nothing to hand to ALPHA's action bracket this run.**
⚠ The registry still carries **no entry for optical/interconnect** (`S94`) and none for the robotics
cycle `P76` registered today — a cycle absent from the registry cannot produce a GAP flag, so a ✅ here
is *"no gap among the cycles we listed"*, not *"no gap"*.

## ✅ EXIT CHECK
- [x] `scoring` block read and quoted; coverage **17.06% < 80%** ⇒ stated **"news axis dead this run"**
      with the cause **probed** (pipe, TLS-layer), not assumed.
- [x] Every `top1_flips_sign` sector listed with `top1` and `top1_w`: **Financials/`BRK-B` 13.9% ·
      Industrials/`CAT` 8.7% · Materials/`LIN` 24.7%** — handed to ROTATION as un-promotable on `wflow`.
- [x] Held-but-not-in-universe check run — **0**.
- [x] Sweep done → `SECTOR_FLOW_US.json`; sector ranking + new-🟢 (`RTX`, `WMT`) read.
- [x] `US_LIVE_SHORTLIST.json` written; short-pressure verdicts read (3 clean-rise, 0 crowded-short).
- [x] `CYCLE_EXPOSURE` GAP read — ✅ none, with the registry-coverage caveat stated.
- [x] **No table here exists in the JSONs** — the §3 table is a *diagnosis* of the filter, computed
      here and present in no artifact.
- [x] Four cross-checks against the MACRO matrix (2 confirm, 2 contradict), and **every shortlist
      absence diagnosed as artifact vs evidence** with the number that decides it.

---

## ⚠ APPEND-ONLY CORRECTION — the 🟢 tag is NOT a `vol_surge` count this run, and both new-🟢 rest on the revoked axis

*(Found 23:1x KST by DEEP-INDU; independently re-measured from `SECTOR_FLOW_US.json` before being
recorded. §1 above is left exactly as written — §4c forbids editing it away.)*

**What §1 said**: *"new-🟢 2 (`RTX`, `WMT`)"* and *"per `M25` the 🟢 count is a **`vol_surge` count**,
not a flow count."*

**What the JSON actually contains — all 8 greens, re-measured:**

| ticker | `vol_surge` | `velocity` | OBV | RS20 vs `SPY` | 🟢 rests on |
|---|---|---|---|---|---|
| `KKR` | **1.32** | None | 매집 +0.122 | +7.8 | **volume — admissible** |
| `LITE` | **1.25** | None | 매집 +0.182 | +1.7 | **volume — admissible** |
| `CSCO` | **1.43** | 2.31 | 매집 +0.128 | −3.1 | **volume — admissible** |
| **`RTX`** | **0.83** | **1.55** | 매집 +0.368 | +13.9 | 🚫 **velocity — REVOKED (G1)** |
| **`WMT`** | **0.83** | **1.35** | 매집 +0.115 | +1.8 | 🚫 **velocity — REVOKED (G1)** |
| `ORCL` | 0.76 | 1.23 | 매집 +0.148 | +9.8 | 🚫 **velocity — REVOKED (G1)** |
| `MA` | 0.84 | 1.35 | 매집 +0.125 | +4.1 | 🚫 **velocity — REVOKED (G1)** |
| `BAC` | 0.81 | 1.49 | 매집 +0.490 | +2.4 | 🚫 **velocity — REVOKED (G1)** |

**Only 3 of 8 greens clear `vol_surge ≥ 1.2`. Five carry `vol_surge < 1.2` and a live `velocity`, and
BOTH new-🟢 (`RTX`, `WMT`) are in that five.**
Cross-check from the other side: **9 names in the whole universe clear `vol_surge ≥ 1.2`** — `KKR`
1.32 🟢 · `LITE` 1.25 🟢 · `CSCO` 1.43 🟢 · **`COHR` 1.70 🟡 · `MNST` 1.62 🟡 · `SNDK` 1.25 🟡 ·
`EBAY` 1.20 🟡 · `WEC` 1.45 🔴 · `NKE` 1.40 🔴**. A pure volume gate would have produced a different
set in both directions.

### 🚨 What this refutes, named rather than quietly fixed

1. **`M25` does not hold this run.** *"The US 🟢 tag is a volume-surge count, not a flow count"* was
   carried into `HANDOVER §1` and repeated in §1 above. **Measured: 5 of 8 greens are velocity-tagged.**
   `M25` is withdrawn for this run's board (→ `R81`).
2. **`R78` reproduced, on the run that claimed to have pre-empted it.** `HANDOVER §1` wrote
   *"`R78`'s lesson is pre-empted this run: no stage may promote on a tag today."* **Then SWEEP_READ §1,
   `SECTOR_ROTATION §2b`/§3 and `EVENT_ALPHA` Card 8 each used the tag.** The guard was stated and not
   applied — which is the `D48` pattern at its most expensive.
3. **Withdrawn claims** (the underlying price/OBV numbers survive; only the **tag** is withdrawn):
   - SWEEP_READ §1's *"new-🟢 2 (`RTX`, `WMT`)"* — **non-citable**.
   - `SECTOR_ROTATION §2b`'s use of *"`WMT` = one of the run's two new-🟢"* as STPL-promotion evidence.
     ⚠ **The promotion itself stands**: it was carried by Δ **+0.325** and `wflow_ex_top1` **+0.027**,
     both price-only. The new-🟢 leg is struck; the verdict does not move.
   - `SECTOR_ROTATION §3`'s INDU mandate line citing `RTX` as a new-🟢. `RTX`'s **OBV 매집 +0.368** and
     **RS20 +13.9 vs `SPY`** are untouched and carry the mandate on their own.
   - `EVENT_ALPHA` Card 8's *"`RTX` +0.572 🟢가속 (a run new-🟢)"* — read `RTX` as 🟡 with the OBV/RS
     numbers standing.
4. **`US_LIVE_SHORTLIST.json` is contaminated**: 5 of its 8 names are admitted on the revoked axis.
   ⚠ **`S101`'s "admitted" basket is frozen and is NOT re-membered** — but the row's meaning sharpens:
   it was registered to test a **`vol_surge` gate**, and the gate turns out to be
   **velocity-contaminated**. Recorded against the row, thresholds untouched.
5. **A second instrument conflict, from DEEP-INDU and consistent with `D261`**: `RTX`'s OBV reads
   **매집 +0.368 in the sweep** and **분배 −25% in `module_chart --read`**. That is the 6th name in the
   5-of-22 conflict set. **No `RTX` claim may rest on OBV alone today** (rule D6).

**🚫 Right revoked for the rest of this run**: **no stage may cite the 🟢/🔴 tag, the new-🟢 count, or
shortlist membership as evidence.** The admissible substitutes are `flow_score`, `obv_norm` **paired
with** RS20/RS60 vs `SPY`, and `vol_surge` read directly. Registered as dig **`D290`** — *`flow_tag`
must take the run-level axis set, exactly as `flow_score` already does (`D225-KR`); until then the tag
and the score disagree about which axes exist.*
