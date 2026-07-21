# SECTOR_DEEP_FIN — US Financials (CONTINUOUS-TRACK · DELTA)

**Date:** 2026-07-14 · **Phase 2 (DEEP, delta run)** · English-only · Desk: US Industry
**Prior deep-dive:** `llm_outputs/2026-07-13/industry_US/SECTOR_DEEP_FIN.md` — **structure carried forward by reference** (7-node value chain, 47-name roster, KPI dashboard unchanged). This file LEADS WITH THE 24h DELTA only. Do NOT re-read the 07-13 tables as stale; the FINRA pull below is genuinely fresh (dated 07-13, one day newer than yesterday's 07-10 pull).
**Sources:** `[FINRA]` us_flow.py Reg SHO daily (**as of 2026-07-13 — FRESH**) · `[SEC]` module_business_us 10-K (period 2025-12-31, FITB + MET) · `[FLOW]` flow_read.py 07-14 · `[CHAIN]` chain_hop.py 14d · `[NEWS]` news_fts 21d foreign (3,896 hits) · `[MACRO]` today's resolver · `[WebSearch]` Q2 print calendar.

---

## Δ0. What changed since 07-13 (the one-screen delta)

| Vector | 07-13 (prior) | 07-14 (today) | Read |
|---|---|---|---|
| **New macro input** | none | **Fresh Hormuz oil shock — WTI $80.75, risk-off tape** | The main new variable. Resolves **NET-CONSTRUCTIVE for the FIN-OW core** (rate/NIM/float legs) but puts the **credit leg** on watch (see Δ0-resolve). |
| **Curve shape** | 2s10s +38bp read as **flattening** (NIM story fading, re-inversion = nearest kill-switch) | **2s10s +0.35pp positive, steep-ish; real-10y 2.32% rising** | **Characterization RE-IMPROVED.** The oil-shock/higher-for-longer combo re-steepened the read — the NIM-slope tailwind is restored and **re-inversion receded** as the imminent kill-switch. |
| **Fed** | hawkish Warsh, no-cut binding | **Warsh hawkish-hold 3.62% confirmed; CPI reaccelerating ~3.8%** | Oil shock is inflationary → **reinforces higher-for-longer** → deposit-repricing/asset side and insurer-float reinvestment both stay favorable. The dovish-fork narrowed further. |
| **Flow (FINRA)** | 07-10 pull; **BAC lone 🔴 z+1.70** | **FRESH 07-13 pull. BAC red RESOLVED (37.2%, z−0.59). PNC cover deepened (z−2.12). MET NEW heavy cover (z−2.55). FITB NEW divergence (81.4%, z+1.23 rising).** | The pre-print consumer-credit hedge on BAC **unwound**; the cover broadened into PNC+MET; the one **new distress/divergence tell is FITB** (regional, M&A-target). |
| **Catalyst clock** | T-1 to the prints | **PRINT DAY. 07-14 JPM/WFC/C report TODAY; 07-15 BAC/MS/GS/PNC** | NIM-vs-credit thesis marks to market **in hours**. This is the live-fire read. |

**One-line delta:** a fresh **Hormuz oil shock** re-steepened the curve read (2s10s +0.35pp positive vs yesterday's "flattening") and reinforced higher-for-longer — **net-constructive for the FIN-OW rate/NIM/float core** — while a fresh FINRA pull shows the **BAC pre-print credit hedge unwound (red cleared)** and covering **broadened into PNC (z−2.12) and MET (z−2.55, new)**; the single new caution is **FITB (short 81.4%, z+1.23 rising)** diverging against its own accumulation, and **the prints hit today/tomorrow.**

### Δ0-resolve — does the oil shock HELP or THREATEN FIN? (the required cross-current call)
**Net HELP for the OW core; localized THREAT to the credit tail — not yet triggered.**
- **HELP (dominant, ~70%):** the shock is **inflationary + higher-for-longer-reinforcing**. It (a) re-steepened the curve read (NIM slope tailwind restored), (b) keeps the Fed on hold → deposit-repricing stays favorable for the **asset side** (PNC/FITB NIM), (c) lifts reinvestment yields on **insurance float** (MET/PRU/ALL — the "cashing in" leg, see chain-hop), (d) firms the dollar (120.5), a tailwind for USD-funded financials. FIN is exactly the rotation-INTO-higher-for-longer beneficiary the macro regime names.
- **THREAT (localized, watch):** if the oil shock spills from *inflation* into *recession fear*, **HY-OAS blows out** and the **credit-cost leg** (COF subprime, BX/APO/KKR alt-credit + BDCs, JPM Tricolor) reserves-builds sector-wide. **Not triggered today** — VIX regime calm-ish, BAC's credit hedge actually *unwound* (z+1.70→−0.59), and no HY-OAS blowout in the 21d tape. The credit leg is the kill-switch to watch, not today's reality.
- **Verdict:** the risk-off tape is **rotation-INTO FIN, not out of it** — the rate/NIM/float thesis strengthened; the credit tail is the standing hedge, currently quiet.

---

## Δ1. Flow — FRESH FINRA panel `[FINRA]` (Reg SHO daily, **2026-07-13**)

Re-run on money-center + regional + payments + insurer panel. **This is a new pull — treat as fresh signal, not the carried 07-10 set.**

| Name | Sub-leg | Short% | z | 5v5 | Read (delta) |
|---|---|---|---|---|---|
| **PNC** | Super-regional | 27.8% | **−2.12 🟢** | **−14.0▼** | **Cover DEEPENED** (was 39.8%/z−0.90). Purest NIM-vs-credit two-sided name being aggressively de-risked into its **07-15 print**. Cleanest bank tell on the board. |
| **MET** | Life insurer | 31.4% | **−2.55 🟢** | −7.1▼ | **NEW heavy cover.** Short% collapsed to 31.4% (base 51.8%). Confluent with chain-hop "life insurers cashing in on higher-for-longer" + OBV accumulation (Δ4). **The freshest clean-cover signal.** |
| **BAC** | Money-center | 37.2% | −0.59 | +3.6▲ | **RED RESOLVED.** Yesterday's lone 🔴 (z+1.70) **unwound** to normal. The pre-print consumer-credit/NCO hedge was **taken off** ahead of its 07-15 report — constructive de-risk, not distress. |
| **FITB** | Regional | **81.4%** | **+1.23** | +4.9▲ | **NEW divergence / only elevated short in panel.** 81.4% short-vol, rising. Yet OBV *accumulating* + news accel 2.57x (Δ4). Chain-hop context = regional-bank **M&A-target** ("bank mergers 7-yr high") → merger-arb / deal-skepticism short, not a clean credit distress read. **Watch, don't chase.** |
| **GS** | Cap-markets | 63.7% | +1.20 | +9.4▲ | Rising but in-range; capital-markets beta building into 07-15 print. Not distress. |
| **MS** | Cap-markets | 57.3% | +1.07 | +5.7▲ | Rising, in-range. ROTCE/buyback story; cap-markets beta same as GS. |
| **ALL** | P&C insurer | 53.4% | −0.78 | **+15.3▲** | Short% easing (66.9%→53.4%) but 5v5 sharply rising — cat-season/loss-cost positioning churn, in-range for P&C. Watch the rising trend. |
| **PRU** | Life insurer | 64.2% | −0.05 | +4.9▲ | High structural short, flat. Same life-float leg as MET but **without** MET's cover signal. |
| **JPM** | Money-center | 49.4% | +0.60 | +6.5▲ | Normal; leader un-faded into **today's** print. |
| **WFC / C** | Money-center | 35.6% / 27.3% | +0.59 / −0.64 | +7.7▲ / −2.6▼ | Both normal into today's prints. C short-vol light (27.3%). |
| **V / MA / AXP** | Payments/consumer-fin | 33.3% / 35.4% / 55.9% | −0.69 / +0.03 / −0.02 | +2.3 / −5.4 / +6.0 | All dead-normal. Rails = rate/credit-agnostic tolls, no distress. |

**Flow read (delta):** the covering **broadened and deepened** — PNC (−2.12) and the **new MET (−2.55)** are the two cleanest 🟢 covers, and critically **BAC's lone red unwound**, so there is now **no distress red in the money-center/insurer complex** heading into the prints. The single caution is **FITB (81.4%, z+1.23 rising)** — the only elevated short, but it diverges *against* its own OBV accumulation and reads as **M&A-target/merger-arb** positioning, not a credit blowup. Separation holds: broad clean bid = banks + brokers + insurers (funded); the private-credit/BDC UW tail (BX/APO/KKR, COF subprime) is untouched by this panel and remains the M-06 epicenter, quiet today.

---

## Δ2. Players — new-name anchors `[SEC]` (names NOT deep-covered 07-13)

47-name FIN roster from `us_top300.csv` unchanged (full list in 07-13 §2). Today's new load-bearing anchors, both pulled fresh from 10-K:

- **FITB (Fifth Third, $47.8B, Regional Banks)** — 10-K period 2025-12-31. Item 1A **leads with CREDIT RISKS**: *"Deteriorating credit quality has adversely impacted Fifth Third in the past and may adversely impact... credit risk... can increase if its loans are concentrated among individual borrowers, borrowers engaged in the same or similar activities, industries."* This is the archetypal **regional-bank NIM-vs-credit-concentration two-sider** — and it's the one name in the panel where the market is **shorting (81.4%) INTO accumulation** (OBV up, news accel 2.57x). The chain-hop tie ("regional banks most likely to make a deal," bank M&A at a 7-yr high) frames the short as **deal-arb/skepticism**, not the credit fear its own risk-factor language warns about. **The panel's cleanest ambiguity — accumulation vs elevated short — resolves at its earnings and/or an M&A headline.**
- **MET (MetLife, $55.1B, Life & Health Insurance)** — 10-K period 2025-12-31. Item 1A **leads with Economic Environment and Capital Markets Risks** — the float/spread business is levered to *"difficult economic conditions"* and capital-markets marks. This is the **float-NIM analog** leg: higher-for-longer reinvests annuity/GA float at higher yields (the insurance version of NIM expansion), which the oil-shock/higher-for-longer regime **directly feeds**. MET is the day's **cleanest confluence**: fresh short cover (z−2.55) + OBV accumulation + RS60 +13.0% + explicit "life insurers cashing in" narrative — yet news velocity only 1.14x (**still under-radar**).

**Unchanged tail (M-06, by reference):** BX / APO / KKR (alt-credit AUM) + BDC layer (FSCO/FSSL) remain the private-credit epicenter; note the fresh tape item **"Apollo's $35B AI-chip credit deal set to begin trading"** and **"AI-Linked Bond Sales Hit $220B as Credit-Risk Concerns Grow"** — the AI-credit exposure keeps building in **nodes 2+5**. Egan-Jones flagged **improving CLO credit quality** (July update) — a mild offset. Nothing resolves the tail today; it resolves at the prints and any oil-shock→recession spillover.

---

## Δ3–4. Value chain + chain-hop alpha `[CHAIN]`

**7-node map carried forward unchanged** (deposits → lending/NIM → capital-markets → payments rails → asset-mgmt/private-credit → insurance-float → exchanges/data). Today's fresh flow simply **re-lights the same nodes**: node 1/2 (PNC/FITB deposits+NIM), node 3 (GS/MS cap-markets short building), node 6 (**MET/PRU/ALL float — the leg the oil shock most directly feeds**), node 7 (CME rate/FX vol).

**Chain-hop run (`chain_hop.py bank NIM insurer payments curve --days 14`), cross-checked with flow_read:**

| Cand. | Prox / body | Sub-leg | flow_read cross-check | Flag |
|---|---|---|---|---|
| **MET** (via PRU headline) | — | Life-float | **🟡 OBV accumulating, RS60 +13.0%, news vel 1.14x (muted)** + FINRA cover z−2.55 | **★ PHASE-3 SEED — cleanest leak.** Short cover + accumulation + strong RS + "MetLife & Prudential cashing in on higher-for-longer" narrative, but news velocity still muted = **strong hand accumulating under-radar**. The single best asymmetric FIN read today. |
| **FITB** | 3 / 3 | Regional | **🟢 accel, news vel 2.57x, OBV accumulating, RS20 +5.5%** but FINRA short 81.4% | **★ DIVERGENCE SEED.** Accumulation + accel vs 81% short = M&A-target ("regional banks most likely to make a deal"). High-variance; resolves at earnings/deal headline. |
| **CME** | 25 / 55 | Exchanges | not flagged distress; FX/rate-vol toll | **Watch.** Highest body-proximity (25) — a pure **rate/FX-vol volume** beneficiary of the oil shock; toll model, rate-agnostic upside on volatility. |
| **PRU** | 2 / 2 | Life-float | **🟡 OBV accumulating, RS +7.5/+9.8, news vel 0.86x (quiet)** | Corroborates MET (same "cashing in" headline) but **without** MET's short-cover — MET is the cleaner expression of the identical leg. |
| **TFC** | 2 / 3 | Diversified | **🟡 OBV accumulating but RS60 −2.3% (laggard), news vel 0.57x** | Stress-test dividend/buyback story; weakest RS of the group — **laggard, not seed.** |

**Chain-hop verdict:** **MET is the standout body-proximate alpha leak** — never a headline name in the panel yet showing short cover + OBV accumulation + strong RS on the exact "higher-for-longer gift to life insurers" narrative the oil shock amplifies, while news velocity stays muted (under-radar). **FITB** is the high-variance divergence (accumulation shorted into, M&A-target). **CME** the clean rate/FX-vol toll.

---

## Δ5. Anti-signal / kill-switch (delta only)

**Bottleneck — unchanged:** the **credit-cost trajectory vs the NIM beat**, resolved at **today's (JPM/WFC/C) and tomorrow's (BAC/MS/GS/PNC) prints** — now live, not T-1.

**KPI dashboard — today's live marks:**
| KPI | Live value (07-14) | Δ vs 07-13 |
|---|---|---|
| Curve 2s10s | **+0.35pp positive, steep-ish**; real-10y 2.32% ↑ | **Characterization re-improved** (was "flattening"); NIM slope tailwind restored, **re-inversion receded** |
| Oil / tape | **WTI $80.75, Hormuz risk-off** | NEW — net-constructive for rate/NIM/float core; credit-leg watch |
| Fed path | hawkish-hold 3.62%, CPI ~3.8% reaccel | Higher-for-longer **reinforced** by oil shock |
| FINRA distress | **No red. PNC z−2.12, MET z−2.55 covers; BAC red cleared; FITB z+1.23 lone elevated** | Materially cleaner; distress hedge unwound |
| NIM / NCO / CET1 | **report card 07-14/15 — LIVE NOW** | The resolver, hitting today |
| HY-OAS / credit | no blowout in 21d tape; AI-credit ($220B bond sales) building | Kill-switch armed but **not triggered** |

**Anti-signal — priority re-ranked for today:**
1. **Credit event from oil-shock→recession spillover (now the nearest live fork).** If the Hormuz shock flips from inflation to recession fear, HY-OAS blows out and the credit-cost leg (COF subprime / BX-APO-KKR alt-credit + BDCs / JPM Tricolor / the $220B AI-credit build) forces sector-wide reserve builds. **Not triggered today** (BAC hedge unwound, no OAS blowout, VIX-regime contained) — but it is the leg the risk-off tape most directly threatens. **The prints today/tomorrow are the first hard read on whether NCOs are turning.**
2. **Curve re-inversion (DE-escalated vs yesterday).** The oil-shock re-steepened the read to +0.35pp positive; re-inversion is **no longer the imminent kill-switch** it was ranked yesterday. Would require a growth-scare bull-flattening — watch, lower probability now.
3. **Dovish Fed surprise (low).** A pivot pulling 2y <4.00% would compress the NIM asset-side thesis; the oil-shock/hot-CPI combo makes this the **least likely** near-term fork.

**Kill-switch proximity:** the OW-thesis **rate/NIM/float core is CONFIRMED and strengthened** by today's oil-shock/higher-for-longer input; the **credit leg is the standing hedge, armed but un-triggered**, and gets its first live mark at today's JPM/WFC/C prints and tomorrow's BAC/GS/MS/PNC. No kill-switch is close today.

---

## Handoff to Phase 3 (delta, 3 lines)
1. **Delta:** fresh **Hormuz oil shock** = net-constructive for FIN-OW (re-steepened curve read to +0.35pp positive, reinforced higher-for-longer → NIM asset-side + insurer float); fresh FINRA pull shows **BAC's lone red UNWOUND**, covering **broadened/deepened into PNC (z−2.12) + new MET (z−2.55)**, and the only new caution is **FITB (81.4% short, rising) diverging vs its own accumulation**. Prints hit **today/tomorrow** — live-fire.
2. **Cleanest reads → carry: MET** (★ chain-hop seed — short cover z−2.55 + OBV accumulation + RS60 +13% + "life insurers cashing in on higher-for-longer" narrative, still under-radar at 1.14x news velocity — cleanest asymmetric FIN expression of the exact regime); **PNC** (deepest bank cover z−2.12 into its 07-15 print, purest NIM-vs-credit two-sider). **JPM** the money-center leader (prints today).
3. **Watch/UW → carry: FITB** (accumulation shorted into 81.4% — M&A-target divergence, high-variance, resolves at earnings/deal); **credit tail** (COF subprime + BX/APO/KKR + BDCs + $220B AI-credit build) = the leg the oil-shock risk-off most threatens, **armed but un-triggered**, first live mark at today/tomorrow prints; **CME** the clean rate/FX-vol toll on the volatility.
