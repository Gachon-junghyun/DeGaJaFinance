# SECTOR_ROTATION — industry_US — 2026-08-08 (Sat) · **delta-only**

> Flow numbers: `SECTOR_FLOW_US.json §sector_rotation` (**asof 2026-08-07 SETTLED · D74 = 0**).
> Matrix: `MACRO_REPORT.md §F`. Reading: `SWEEP_READ.md`. All on disk — **this file writes only what
> changes and why.**

## §0 · 🚨 A within-run correction to this run's own MACRO §F, before anything else

**`MACRO_REPORT.md §F` inherited the 08-07 run's PRE-delta matrix instead of its POST-delta verdict.**
It wrote *"OW Financials · N+ Energy"*; the 08-07 `SECTOR_ROTATION.md §2` had already moved **ENRG
N+ → OW−** and **FIN OW → OW−**, and its own DEEP withdrew **COMM UW− → UW**.

**The correct inherited line is §1 below.** ⚠ **This changes the starting point of two of this run's
three deltas** (both are demotes; from OW− they land at N+, not from N+/OW). **Caught inside the run
by the stage that owns the ledger — the D48 pattern executed rather than logged.**

## §1 · Inherited, one line — the true post-delta verdict of 2026-08-07

`FIN OW− · ENRG OW− · INDU OW− · IT N · HLTH N · DISC N · MATR N− · COMM UW · UTIL UW · STPL UW · RE UW`

**Universe context, three numbers**: n=300 · wflow **+0.057** (was **+0.127**) · **23🟢 / 77🔴**
(was 27🟢 / 78🔴) ⇒ **the headline flow HALVED and the green count fell by four while reds held.**

---

## §2 · Deltas — three verdict changes, four attempts DECLINED

| Sector | inherited | flow evidence (wflow · eqflow · breadth · Δ · 🟢/🔴) | new verdict | who resolves |
|---|---|---|---|---|
| **Energy** | **OW−** | 🚨 **every axis that produced the 08-07 promotion decayed or flipped in ONE session**: eqflow **+0.209 → +0.078 (−63%)** · **Δ +0.196 → −0.084 — a SIGN FLIP** · wflow +0.426 → +0.342 (still rank 1) · breadth 0.120 · 2🟢/2🔴 of 16. ★ **And SWEEP §2a decomposed both greens: XOM `vol_surge` 0.88 · CVX 0.96 — BOTH velocity-lit on below-average volume**, so the rank-1 wflow has no volume behind it | ⬇ **N+** *(down one notch, rule (a))* | **DEEP-ENRG** (continuous) |
| **Financials** | **OW−** | 🚨 **second consecutive run of deterioration on every axis**: eqflow **+0.190 → +0.125 → +0.050** (halved twice) · breadth **0.149 → 0.130 → 0.090** · **Δ negative twice (−0.076 → −0.069)** · wflow +0.317 → +0.241 → **+0.172** · and **4🟢 against 7🔴 = red-dominant inside the sector the sweep ranks #2**. ★ **3 of the 4 greens are velocity-lit on `vol_surge` 0.85 / 0.73 / 0.65 — JPM's is the lowest of any green on the board** | ⬇ **N+** *(down one notch, rule (a))* | **DEEP-FIN** (rotating) |
| **Consumer Staples** | **UW** | 🚨 **the 08-07 deferral's third observation did not decay — it INVERTED to the worst on the board on BOTH axes**: eqflow **−0.017 → −0.165 (worst of 11)** · **Δ +0.084 → −0.151 (worst of 11)** · 0🟢 / 6🔴 of 19 · breadth 0.000 | ⬇ **UW−** *(down one notch, rule (a) inverted)* | logged — **no DEEP slot** (see §3) |

**Each of the three is carried by a flow number and nothing else.** The macro arguments available on
all three — MACRO §B-1's *"FIN was 10th of 11 on the bull-steepener session"*, §B-2's *"six of six
energy names fell on a crude-up bar"* — are **deliberately NOT used as carriers.** They corroborate;
they do not carry. **Using them here is the duplication this stage's own field note measures.**

### Attempts DECLINED — each with the number that declined it

| Attempt | Why declined |
|---|---|
| **HLTH N → N+** on **breadth 0.160 = the HIGHEST of 11 for a 3rd consecutive run**, **Δ +0.049 = the ONLY positive delta on the entire board**, both axes positive (wflow +0.155 / eqflow +0.121), 5🟢/6🔴, and — new this run — **4 of its 5 greens are VOLUME-lit, making it the only breadth signal on the board that is not a velocity artifact** (SWEEP §2) | 🚫 **Declined on the sector's OWN registered anti-signal, firing for a THIRD consecutive run.** The 2026-07-30 DEEP-HLTH registered *"XLV's 5-day excess vs SPY turning negative **while SPY rises**"* as the kill. Measured on the settled bar: **SPY +3.51% over 5 sessions, XLV excess −1.59pp. Both conditions met.** Prior reads: −6.78pp (08-05) · −3.05pp (08-07) · **−1.59pp today** ⇒ ⚠ **the anti-signal is firing but WEAKENING, three runs running.** **N stands** — a promotion against a live registered anti-signal is the violation R9 was written for. **The trend in the anti-signal's own magnitude is recorded so the next run reads a fourth observation, not a first** |
| **MATR N− → either direction** | 🚫 **Declined in BOTH directions, and the reason is that the two axes now disagree at maximum width.** *Down*: eqflow **+0.167 → +0.076 → +0.040** and Δ **+0.204 → −0.070 → −0.040** — decayed a third time, which would carry a downgrade. *Up*: **XLB's 5-session excess vs SPY is +1.307 and S57's branch A (+1.9) fires at ANY close through 08-12** — but **the sector has 0🟢 of 12 and breadth 0.000**, so an upgrade would have **no flow carrier at all** and would be the macro re-argument this stage forbids. ⇒ **held at N−, handed to DEEP.** ★ **This is the run's most decision-relevant disagreement and it is why MATR finally takes a slot (§3)** |
| **UTIL UW → UW−** on wflow **−0.372 → −0.395**, eqflow −0.356 → **−0.381**, **0🟢 / 11🔴 of 15 (was 9🔴)**, sitting **0.363 below the next-worst sector (RE −0.032)** | 🚫 **Declined — because the notch would be redundant, not because the evidence is weak.** ✅ **The 08-07 run logged UTIL's marginally positive Δ (+0.025) as "a first observation so the next run can read a second." The second observation is in: Δ −0.023, REVERSED.** ⇒ **the UW is confirmed on its own pre-registered second look, and `S62` FIRED-B on the settle.** **A UW that is already the most one-sided sector on the board by 0.363 does not need a notch to say so** |
| **COMM UW → UW−** *(the 08-07 shape has RE-FORMED: eqflow +0.119 EXCEEDS wflow −0.087, breadth 0.150 = 2nd of 11)* | 🚫 **Declined, and this is R56 binding on a fresh bar.** **EA is STILL tagged 🟢가속** with the board's highest `vol_surge` (+3.66) and highest OBV (+0.749) — **and it is a delisted security** (D207's liveness assertion, run on all 23 greens, returns **1 FAIL, 0 false positives, and the FAIL is EA**). **Recomputed ex-EA: eqflow +0.119 → +0.073 (−39%), 2🟢/2🔴 → 1🟢/2🔴 of 12, breadth 0.150 → ~0.083.** ⇒ **the same notch the 08-07 run wrote and then withdrew would have been written again. COMM = UW** |
| **IT · DISC · RE** *(no attempt)* | **IT** ✅ N confirmed: **eqflow −0.092 against wflow +0.084** and **22🔴 of 56 = 29% of the board's entire red count in one sector.** Mega-cap-narrow is what a working Neutral looks like. **DISC** — ★ **for the first time in five runs the two windows AGREE** (exc5 −0.26 / exc20 −0.19, both flat-negative), with **0🟢/8🔴 and breadth 0.000** ⇒ the four-run disagreement has closed onto *no direction*, which is the same verdict by a cleaner route. **RE** — 0🟢 but only **1🔴 of 12**, wflow −0.032 / eqflow −0.025 ≈ flat ⇒ **no signal in either direction (C3)**, not confirmation |

**Post-delta tilt**: `INDU OW− · ENRG N+ · FIN N+ · IT N · HLTH N · DISC N · MATR N− · COMM UW ·
UTIL UW · STPL UW− · RE UW`

⚠⚠ **The board has ONE overweight left, and it is OW−.** Three runs ago it had FIN OW plus two OW−.
**That is not a decision this stage made; it is the arithmetic of three consecutive demotes carried by
flow numbers.** **Named so PREMORTEM can attack it as a portfolio-level statement rather than as three
separate sector calls.**

---

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol's DEEP budget line: 2 continuous + 2 rotating)

### Continuous (⌈4/2⌉ = 2) — today's top ranks

| Slot | Sector | Rule applied |
|---|---|---|
| **DEEP-INDU** | **Industrials (OW−)** | ★ **The board's ONLY remaining overweight.** Its flow is the quietest thing on the board — wflow +0.073, eqflow **+0.106 (eqflow > wflow = breadth-led)**, Δ −0.015, 5🟢/9🔴 — and **XLI's exc1/exc5/exc20 are −0.38 / −0.54 / −0.63, all inside ±0.7pp.** ⚠ **Anti-thrash does NOT apply** (INDU was *rotating*, not continuous, on 08-07); it takes a continuous slot because it is the only OW |
| **DEEP-ENRG** | **Energy (N+, demoted today)** | ⚠ **Anti-thrash checked and NOT applied**: ENRG held a continuous slot on 08-07 but is **no longer top-N OW** (it is N+), so the rule's condition fails and the slot is re-earned rather than inherited. It takes it because **it is still rank-1 on wflow while its Δ flipped sign in one session and both its greens are velocity-lit** — the largest single-session axis reversal on the board |

### Rotating (⌊4/2⌋ = 2) — and one deliberate, stated deviation from the recency rule

| Slot | Sector | Rule applied |
|---|---|---|
| **DEEP-MATR** | **Materials (N−)** | ★★★ **A written pre-commitment honoured on its third ask.** `DEEP_LOG 2026-08-06` wrote *"MATR — ★next run's first rotating pick"*; **08-07 broke it** and re-wrote *"★next run's first rotating pick **unless its carriers decay again**."* ⚠⚠ **The escape clause TECHNICALLY FIRED — eqflow decayed again, +0.076 → +0.040 — and it is deliberately NOT used.** The reason the pre-commitment existed (aggregate vs names diverging) has become **dated and measurable**: **0🟢 of 12 against a price observable 0.59pp from firing S57's branch A on 08-12**, with **`S57-ANNEX` registered today**. **A third deferral on a technicality, while the sector became the most decision-relevant on the board, is the process failure this desk logs.** **Last covered 2026-08-03 — six runs** |
| **DEEP-FIN** | **Financials (N+, demoted today)** | Moves **continuous → rotating** on its second consecutive demote. **Last covered 08-07**, so this **breaks the ~3-run recency filter, deliberately and stated**: the sector has now deteriorated on **every axis for two consecutive runs** and its 🟢 tags were shown today to be **news-velocity on below-average volume**. **A name-level read is owed before a third notch is considered.** ⚠ **`S65` settles 08-11 and `S66`/`S70` ~08-10** — three brackets on one sector inside four days |

⚠ **Deviation declared, not hidden.** The rotating rule reads *"next-highest OW not deep-dived in the
last ~3 runs; if every OW was recently covered → fallback to next-highest OW regardless, and SAY
recency-starved."* **Every OW (there is one: INDU) was covered in each of the last three runs**, so the
fallback points back at INDU — **which already holds a continuous slot.** ⇒ **the rule's fallback is
degenerate this run**, and rather than padding it, both rotating slots go to **non-OW sectors chosen on
stated grounds** (a twice-broken pre-commitment; a two-run axis deterioration with three brackets
settling). **This is the "never pad with Neutral/UW" line being deviated from on purpose. Logged.**

### 🚨 Not covered, and it is the run's clearest coverage gap

**Consumer Staples was DEMOTED to UW− today on the worst eqflow and the worst Δ on the board — and it
has NEVER received a DEEP slot in this desk's recorded DEEP_LOG history.** ⚠ **A sector can now be
moved two notches across five runs without a single name-level read.** **ADM and CTAS sit on the
missed ledger with a 08-16 recheck.** **Named, not resolved.**

**HLTH is the other**: **best breadth on the board for a third run, the only positive delta, and the
only non-velocity breadth signal** — declined three runs running on an anti-signal whose own magnitude
is **weakening** (−6.78 → −3.05 → **−1.59pp**). **If it fires a fourth time at a smaller magnitude,
the anti-signal itself becomes the thing to re-examine, not the sector.**

## DEEP_LOG 2026-08-08: continuous=[INDU, ENRG] rotating=[MATR, FIN] · N=4/4 · ★ **MATR's twice-broken written pre-commitment HONOURED on its third ask — the escape clause technically fired (eqflow +0.076→+0.040) and was deliberately NOT used; last covered 08-03 = 6 runs** · INDU continuous as **the board's only remaining OW** (anti-thrash N/A — it was rotating on 08-07) · ENRG continuous re-earned, **anti-thrash checked and NOT applied** (no longer top-N OW after today's demote) · **FIN continuous→rotating, recency filter broken deliberately and stated** (covered 08-07; 2nd consecutive demote; S65 08-11 + S66/S70 ~08-10) · ⚠ **rotating rule's OW fallback was DEGENERATE this run (the only OW already holds a continuous slot) ⇒ both rotating slots are non-OW by declared deviation** · **three deltas, all demotes, all carried by flow alone: ENRG OW−→N+ (Δ sign flip +0.196→−0.084), FIN OW−→N+ (eqflow halved twice, breadth fell twice, 4🟢/7🔴), STPL UW→UW− (eqflow −0.165 and Δ −0.151, both worst of 11)** · **four attempts declined with numbers: HLTH N+ (own anti-signal, 3rd run, magnitude WEAKENING −6.78→−3.05→−1.59), MATR both directions (axes disagree at max width — handed to DEEP), UTIL UW− (redundant; its Δ's 2nd observation REVERSED +0.025→−0.023 as pre-registered), COMM UW− (**R56 — EA still 🟢 and still delisted; ex-EA eqflow +0.119→+0.073, 1🟢/2🔴**)** · uncovered=[**STPL(UW−, demoted today on the board's worst eqflow AND worst Δ — ★NEVER deep-dived in recorded history; ADM/CTAS missed-ledger recheck 08-16 — ★next run's first rotating pick)**, HLTH(N, covered 08-06; breadth rank 1 for a 3rd run and the only non-velocity breadth signal on the board; declined on an anti-signal whose magnitude is weakening — **a 4th firing at a smaller magnitude should re-examine the anti-signal, not the sector**), IT(N, covered 08-05, 22🔴 of 56 = 29% of the board's reds, S13 08-12), UTIL(UW, covered 08-05, **S62 FIRED-B on the settle at +13.252 — but DEGENERATE, branch A was 19.16pp away (D206)**; 0🟢/11🔴), COMM(UW, covered 08-07, **the un-owned telecom node T/VZ/CMCSA is still un-owned** — VZ 🟡 rs20 +9.30 / T 🟡 +10.20 / CMCSA 🟡 +5.20, all positive rs20 with **TMUS 🔴분산 flow −0.669**), DISC(N, covered 08-03, ★**the 4-run window disagreement CLOSED — both windows now agree on ~zero**), RE(UW, covered 08-04, 1🔴 of 12 = no signal either direction (C3), S25 08-08 pre-declared zero-information)]

## ✅ EXIT CHECK

- [x] **§1 is ONE line**, inheriting the true post-delta verdict verbatim — **and §0 names the
      inheritance error it had to correct to get there.** No unchanged sector gets a paragraph
- [x] **Every §2 delta cites a flow number and nothing else** — the available macro arguments are
      explicitly named as corroboration and **declined as carriers**
- [x] **Every matrix × flow divergence named with a resolution owner** (ENRG → DEEP-ENRG · FIN →
      DEEP-FIN · MATR → DEEP-MATR · COMM → R56/D207, no DEEP · STPL → logged, no DEEP)
- [x] **N=4 picked by the rule at the protocol's DEEP budget line**, with **continuity checked and
      NOT applied (stated twice, with the reason)** and the **recency rule's degeneracy declared**;
      no padding to reach N. **OW sectors without a slot: none exist** — the one OW holds a slot
- [x] **Linter run on this stage's own output** (below)
- [x] **DEEP_LOG line appended** with every uncovered sector, its last-covered date, and its dated
      brackets
