# US TRADING-STRATEGY DESK — TRACK.md (scheduled run)
**Run date:** 2026-07-15 (Wed, weekday 2) · **Mode:** TRACK · **Desk:** strategy-US (apex)
**Books:** 모의·검증·공격 (executed) · 실전 & 광기 (read-only context). Seed ≈ $10,900/book.
**Tracks:** 2026-07-13 (Mon) FULL watchlist. *Note: 7/14 (Tue) desk never ran — this TRACK is the first run since the FULL and therefore resolves the CPI master node.*

---

## VERDICT (one line)
**The master node resolved to the reprieve side, and cleanly. June CPI (2026-07-14) printed DECISIVELY COOL — headline 3.5% YoY vs 3.8% expected (down from 4.2% May, first pullback since January), MoM −0.4% vs −0.2% (biggest monthly decline since April 2020), core 2.6% vs 2.9% — an energy-swoon-driven downside surprise. The tape confirmed the long-duration snap-back the 7/13 build named as the "cool" branch: NVDA +4.06%, GOOGL +1.99%, AVGO +1.32%, ETN +3.15%, VIX→16.5. The 공격/ETN CPI-gate's CONFIRM condition fired (CPI cool + ETN close 415.52 > 200DMA 372 + OBV 매집) — BUT ETN ran +3.15% away from the entry, collapsing at-market R/R to (455−415.52)/(415.52−372) = **0.91 < 1.5 rail**. So the disciplined call is NOT to chase: the confirmed-turn is real, the thesis validated, but the entry math now fails the hard ≥1.5 rail. ETN stays on the live <390 buy-zone alarm (which restores R/R ~3.6) with the hard deploy-or-source-alternative decision handed to tomorrow's 7/16 FULL. Housekeeping: 2 valid raise-only stop-raises executed (AVGO 369.84→369.88, RTX 191.54→191.57, both stop<px sanity-checked); no hard STOP_HIT. The single live risk is TSM sitting exactly ON its stop (px 420.39 / stop 419.9) D-1 into its own 7/16 TSMC earnings — held to stop, engine enforces. Net: 0 buys, 0 sells, 2 stop raises, ETN not chased on a rail-blocked entry.**

---

## STEP 1 — STATE + SELF-MONITOR
- **track-record (7d):** ✓ OK — consecutive-zero-*execution* streak **0**. No freeze flag.
- **portfolio-audit:** ✓ 건전. Autonomous deployed $13,541. Deploy: 모의 22% / 검증 30% / 공격 **14% (still 1 name — the ETN overhang, which the runaway entry leaves open by design, see below)**. Cross-book (mine): GD 26%, AVGO 11%. All within caps.
- **dashboard:** regime **risk_on** (1.0), VIX **16.5 live** (calm, not a hot-CPI blowup) · absorption **strong** (KORU +15.2%, SMH +2.5%) · RS leader **power** +31.4% vs chips +22.2%. (Snapshot bar 7/13 stale; live prices used below.)
- **exits / enforce (dry-run):** hard STOP_HIT **0** · FABER_EXIT **0** (mine). RAISE_STOP: AVGO #44 → 369.88, RTX #47 → 191.57 (both executed). STOP_IMMINENT (watch, no action): TSM #28 (1.001), RTX #47 (1.010). (광기 GD #42 / AVGO #46 raises = NOT mine, skipped.)
- **📋 Rulebook check (docs/rulebook_audit_lessons.md 🌱staged, apex-binding):** **R-001** — CPI regime read NOT taken on tape-inference alone: corroborated the print via WebSearch (CNBC/BLS 2026-07-14) before hardening it into the master-node verdict. **R-004** — the "CPI cool" narrative was a fresh reading that CONFIRMED (not contradicted) the 7/13 "cool branch"; still verified rather than assumed. Also flagged the honest tension: the cool print was **energy-swoon-driven**, which partially undercuts the WMB "Hormuz oil-premium" leg (b) inherited from 7/13 — surfaced below, not rationalized away [[feedback_corroborate_inherited_tape]]. **R-007** — ETN not deployed precisely because trade R/R fell to 0.91 < 1.5; disclosed. **R-003** — no deal-status claims made this run.

---

## MASTER NODE RESOLUTION — June CPI (2026-07-14)
| Metric | Print | Expected | Prior (May) | Read |
|---|---|---|---|---|
| Headline YoY | **3.5%** | 3.8% | 4.2% | COOL — first pullback since January |
| Headline MoM | **−0.4%** | −0.2% | — | biggest monthly decline since Apr-2020 |
| Core YoY | **2.6%** | 2.9% | 2.9% | COOL |
| Driver | energy-price swoon | | | ← the caveat (see WMB) |

**Regime consequence:** the hot-branch (hike-tilt validated, duration/crowded-AI de-rate) did NOT trigger. The **cool-branch reprieve** did: 10y relief, crowded-beta risk premium returned, long-duration + AI-semi snapped back. Confirmed by the 7/14 close: **NVDA +4.06% · GOOGL +1.99% · AVGO +1.32% · ETN +3.15% · GEV +2.25% · WMB +2.04%** vs defensives lagging (RTX −1.53%, TSM −0.28%). VIX 16.5. **Source (R-001/R-004):** [CNBC June 2026 CPI](https://www.cnbc.com/2026/07/14/consumer-price-index-inflation-report-june-2026.html), [BLS CPI June 2026](https://www.bls.gov/news.release/cpi.htm).

---

## PER-POSITION OBSERVATION-POINT TRACK

### 공격 / ETN (ARMED candidate) — the headline decision
- **OP1 (CPI 7/14 + ETN hold):** predicted "CPI cool + ETN close>372 w/ OBV 매집 → deploy earned." **CONFIRM fired:** CPI cool ✓, ETN close 415.52 > 200DMA 372 ✓, OBV **매집** ✓ (flow_read: RS20 +4.8%, short 2.4%-float covering, P/C 0.7 → 🟡중립). The >412 momentum-reclaim alarm (#202) also fired = confirmed-turn.
- **BUT the entry ran away.** ETN gapped +3.15% to 415.52 on the CPI-relief pop. At-market R/R = (455−415.52)/(415.52−372) = **0.91 < 1.5** — the 7/13 plan's "@mkt (or better on <390 buy-zone)" was valid at ~403 (R/R 1.69); at 415.52 the math breaks the mandatory rail.
- **ACTION → DO NOT CHASE. HOLD ARMED, buy-zone only.** This is not a freeze: the thesis is *confirmed*, the reason for no-deploy is an objective ≥1.5 R/R rail (not indecision), and it is mechanized + dated — the <390 buy-zone alarm (#201, restores R/R ~3.6) stays live, and the hard deploy-or-source-alternative call is handed to the **7/16 FULL** (tomorrow, one session out). If ETN pulls back to buy-zone → deploy at good R/R; if it keeps running → correctly not chased.
- **Honest ledger:** 공격 stays at 14% / 1 name for one more session. The runaway entry (not desk indecision) caused this; 7/16 FULL must either catch an ETN pullback OR source a fresh earned 공격 leg at ≥1.5 R/R (that candidate-sourcing is FULL-mode work, not a TRACK task).

### 모의
- **TSM #28** — px **420.39**, stop **419.9**, −3.5%. **STOP_IMMINENT (1.001)** and **D-1 into TSMC 7/16 earnings.** Rail ⑤ (no D-1 new entry into a catalyst) applies to adds, not to holding an existing position at its stop. **ACTION → HOLD TO STOP** (engine enforces on break). Knife-edge: a 7/16 beat bounces it, a break stops it out clean first — both are acceptable, disciplined outcomes. No add (extended + D-1). 
- **GEV #34** — px **1066.01**, +12%, stop **1015.72**. +2.25% on cool CPI. Funded-load electrical-backbone intact but extended (+31% >200DMA). No exit signal. **ACTION → HOLD to stop**, no add (extended).
- **WMB #52** — px **75.98**, stop **72.85**, +2.04%. OBV 매집. **Add-R/R now mechanically restored:** (83−75.98)/(75.98−72.85) = 2.24 ≥ 1.5. **ACTION → HOLD, no add.** *Why decline a passing R/R:* the cool CPI was **energy-swoon-driven**, which just weakened the "Hormuz oil-premium" half of WMB's thesis (leg b); the gas-midstream cash-flow-now half (leg a) is intact (+2% today). Adding on an oil-premium rationale the same day the data shows energy swooning would be internally inconsistent — the honest call is hold and let the 7/16 FULL reassess the thesis legs with fresh eyes.

### 검증
- **NVDA #40** — px **211.80**, +4.06%, stop **194.08**. Crowded-AI beta snapped back hardest on dovish CPI = "rotation-not-rupture" validated. No raise flagged (engine snapshot pre-move; watch for a raise next run). **ACTION → HOLD to stop**, no add (rail: no chase on +4% green).
- **AVGO #44** — px **389.11**, +1.32%, stop **369.84 → 369.88 (RAISED ✓).** $30B Apple captive deal repairs the ASIC-drift crack; OBV neutral. **ACTION → HOLD, stop raised.**
- **RTX #47** — px **193.39**, −1.53%, stop **191.54 → 191.57 (RAISED ✓).** Defense lagged on the risk-on rotation (money into AI beta). Thesis (7/23 Q2 earnings target reset) intact; STOP_IMMINENT (1.010). **ACTION → HOLD, stop raised**, add still gated to 7/23.
- **GOOGL #36** — px **359.51**, +1.99%, stop **340.87**. Rate-sensitive single-factor — a direct dovish-CPI beneficiary (long-duration snap-back). **ACTION → HOLD to stop**, no add (single-factor; let it ride).

### 공격 (held)
- **GD #41** — px **~369.5**, +5.5%, stop **359.52**, RSI **81** extended, near target 393, into **7/22 earnings (D-7)**. No raise flagged for 공격 #41. **ACTION → RIDE into earnings**, no add (extended).

---

## EXECUTED THIS RUN
- ✅ **RAISE_STOP AVGO #44** 369.84 → **369.88** (Chandelier hh22 414.6 − 3ATR; raise-only ✓, stop<px 389.11 ✓ — marginal, keeps trail current).
- ✅ **RAISE_STOP RTX #47** 191.54 → **191.57** (Chandelier hh22 203.9 − 3ATR; raise-only ✓, stop<px 193.39 ✓ — marginal).
- 🔒 **ETN — NOT executed (rail ≥1.5 R/R blocks the runaway entry).** Buy-zone alarm #201 (<390) live; hard decision handed to 7/16 FULL.
- **DECLINED adds:** WMB (R/R restored but oil-premium leg weakened by energy swoon), NVDA (+4% no-chase), AVGO/GOOGL/GEV (held), GD (RSI 81 extended), RTX (gated to 7/23).
- **Turnover:** 0 buys / 0 sells / 0% · **new betting entries:** 0 · hard STOP_HIT: 0.

---

## PHASE 4 — VERIFY
- **① Alpha-freshness:** CPI-cool regime read CORROBORATED via WebSearch (not tape-inferred). ETN thesis confirmed but entry 🟡 (ran away, R/R-blocked). No 🔴RESOLVED alpha chased. WMB oil-premium leg 🟡DOWNGRADED (energy swoon) — surfaced, position held not added.
- **② math_check:** ETN @mkt R/R = (455−415.52)/(415.52−372) = 39.48/43.52 = **0.91** < 1.5 → no deploy ✓; buy-zone R/R at 390 = (455−390)/(390−372) = **3.61** ✓ (alarm live); WMB add R/R = (83−75.98)/(75.98−72.85) = **2.24** (mechanically eligible, declined on thesis-leg grounds, not math); stop raises raise-only + stop<px: AVGO 369.88>369.84 & <389.11 ✓, RTX 191.57>191.54 & <193.39 ✓; turnover 0%, new entries 0, non-LETF, no chase.
- **③ Adversarial self-review (inline):** *Q: "Is 'ETN R/R 0.91, don't chase' just the 공격 freeze recycled under a rail?"* — **No.** The 7/13 build ARMED ETN to deploy on a cool CPI; CPI came cool and I did NOT reflexively skip — I checked the actual entry math, and it objectively fails the ≥1.5 rail because the name gapped +3.15%. That is the market removing the entry, not the desk avoiding one. The buy-zone alarm keeps a *good-R/R* entry live and the hard call is dated to 7/16 (one session). *Q: "Then is 공격 permanently stuck at 1 name?"* — the risk is real; the 7/16 FULL is now explicitly tasked to either catch an ETN pullback OR source a fresh ≥1.5 leg (FULL-mode candidate work). If 7/16 comes and 공격 is neither deployed nor has a dated live trigger, THAT is the freeze — and it's now pinned. *Q: "Should NVDA's +4% rip be banked/trimmed?"* — no; it's a held core, the stop (194.08) banks the gain, and trimming a validated snap-back into a cooling-inflation tape is not earned. **ACCEPTED.**

### Honest risk ledger
- **0 buys on a confirmed-dovish tape** — the reprieve branch fired, which normally argues for *adding* risk; I added none because (a) the one armed candidate (ETN) ran past its R/R rail, (b) held names are extended (GEV +31%, GD RSI 81, NVDA +4%) or catalyst-gated (RTX 7/23), and (c) fresh candidate-sourcing is FULL-mode work for 7/16. Defensible for a TRACK day, but 7/16 must convert the dovish reprieve into at least one earned deployment or explicitly document why not.
- **TSM held on its stop D-1 into its own earnings** — deliberate: the stop IS the risk control; the engine enforces a clean exit if 419.9 breaks, and a 7/16 beat is the upside. No pre-earnings trim because the stop already caps the downside tighter than a discretionary trim would.
- **WMB oil-premium leg weakened by the very print that drove the tape** — held, not added, and flagged for 7/16 thesis re-examination.

---
*Next: 7/16 (Thu) FULL — **the 공격 ETN hard decision** (deploy on a <390 buy-zone pullback restoring R/R, OR source a fresh ≥1.5 earned 공격 leg; drop ETN only on close<372) + **TSMC 7/16 earnings** (TSM held on stop 419.9 — the supercycle-length test) + full regime rebuild on the post-CPI dovish-reprieve tape. Watch: RTX add gated to 7/23; NVDA/AVGO stop-raises next run as the snap-back extends; defense earnings cluster GD 7/22 / NOC 7/21 / LMT 7/23.*
