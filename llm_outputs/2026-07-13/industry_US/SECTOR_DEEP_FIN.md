# SECTOR_DEEP_FIN — US Financials (CONTINUOUS-TRACK · DELTA)

**Date:** 2026-07-13 · **Phase 2 (DEEP, delta run)** · English-only · Desk: US Industry
**Prior deep-dive:** `llm_outputs/2026-07-12/industry_US/SECTOR_DEEP_FIN.md` — **structure carried forward by reference** (7-node value chain, player roster, KPI dashboard unchanged). This file LEADS WITH THE DELTA only.
**Sources:** `[FINRA]` us_flow.py Reg SHO daily (as of 2026-07-10, same pull as prior) · `[SEC]` module_business_us 10-K (period 2025-12-31) · `[FLOW]` sector_flow sweep asof 07-10 · `[MACRO]` today's resolver · `[WebSearch]` Q2 calendar.

---

## Δ0. What changed since 07-12 (the one-screen delta)

| Vector | 07-12 (prior) | 07-13 (today) | Read |
|---|---|---|---|
| **Curve shape** | 2s10s +38bp, called **bear-steepening** (NIM tailwind) | 2s10s +38bp, called **flattening**; real-10y **2.31% rising** | **Same level, worse characterization.** The steepening-into-NIM leg is losing its slope story — flattening is a mild NIM headwind and moves **re-inversion** (the M-01 kill-switch) closer. |
| **Fed** | no-cut Warsh | **hawkish Warsh confirmed, higher-for-longer binding; NO dovish offset** (inflation 4.2%/core 2.8% binds even as NFP 57K/U 4.2% crack) | **Constructive for the NIM thesis' asset side** — no cut = deposit repricing stays favorable. The dovish-pivot fork narrows: CPI **this week** can still flip it. |
| **Flow (FINRA)** | BAC lone 🔴 z+1.70 | **Unchanged — same 07-10 pull.** BAC still the only 🔴 | No new short signal. Do not re-read as fresh. |
| **Sector flow rank** | FIN freshest rotation | **FIN #1 of 11, broad — wflow +0.231, eqflow +0.214, 12 green / 1 red** | **The bid broadened past money-center** into brokers/insurers/regionals. Cleanest, widest bid on the board. |
| **Shortlist tilt** | JPM/MS/GS + COF/BX tail | **PNC, SCHW, COF, ALL, PRU** (🟢 accel + mcap≥$10B) | Rotation is now **super-regional bank + broker + P&C/life insurer** — the "broad NIM/float" leg, not just the capital-markets leg. |
| **Catalyst clock** | written INTO the print | **T-1 to the print** — 07-14 JPM/WFC/C, 07-15 BAC/MS/GS/**PNC** | Thesis marked to market in **24–48h**. This is the last pre-print read. |

**One-line delta:** the FIN-OW bid got **broader and cleaner** (sector-flow #1, 12/13 green, shortlist now spans regional-bank + broker + insurer), while the macro backdrop shifted the NIM story from *steepening-tailwind* toward *flat-curve-but-no-cut* — supportive on the asset/deposit side, but with **curve re-inversion now the nearest kill-switch** and Q2 prints (T-1) about to resolve NIM-vs-credit.

---

## Δ1. Flow — new shortlist names, short-pressure overlay `[FINRA]` (Reg SHO daily, 2026-07-10)

Panel re-run on the today shortlist. **No name diverges from its narrative** except the carried-forward BAC surge.

| Name | Short% | z | 5v5 | Read |
|---|---|---|---|---|
| **COF** | 28.8% | −0.22 | −3.8▼ | **Cleanest of the shortlist** — short% collapsed to 28.8% (vs ~40–45% normal), a *short exit* into the print. The credit-tail name is being **covered, not pressed** — market not pre-positioning for a COF blowup. |
| **PNC** | 39.8% | −0.90 | −10.9▼ | Short pressure easing hard (5v5 −10.9). Super-regional NIM name **de-risking** into its own 07-15 print. Constructive. |
| **PRU** | 61.7% | −0.37 | −1.1▼ | High structural short% but easing; life-insurer float name, in-range. |
| **SCHW** | 38.8% | +0.46 | −3.6▼ | Normal, trend easing. Broker/asset-gatherer — no distress signal. |
| **GS** | 49.2% | −0.21 | +4.9▲ | Normal; capital-markets beta intact. |
| **MS** | 49.2% | −0.01 | +5.3▲ | Dead-normal. Buyback/ROTCE story unchallenged by shorts. |
| **JPM** | 44.8% | −0.24 | +4.3▲ | Normal — leader still not faded pre-print. |
| **ALL** | 66.9% | +0.66 | +9.3▲ | High short% + rising 5v5, but **in-range for a P&C insurer** (loss-cost/cat-season positioning, not credit distress). The one shortlist name with a *rising* short trend — watch, don't flag. |
| **BAC** | 52.7% | **+1.70 🔴** | +3.6▲ | **Carried forward — still the lone red.** The pre-earnings consumer-credit/NCO hedge has a name; reports 07-15. Unchanged from 07-12. |

**Flow read (delta):** the broadening is *clean* — the three names the sector-flow sweep pushed up (PNC, SCHW, and especially **COF at short%-28.8, a cover**) show **easing** short pressure, not building. That corroborates a genuine broad bid rather than a squeeze. The only distress tell remains **BAC (z+1.70)**; **ALL** is the only shortlist name with a *rising* short trend but stays in-range (P&C cat/pricing positioning). **Separation holds:** broad-bid = regional/money-center banks + brokers + insurers (funded); UW tail = BDC/private-credit (BX/APO/KKR + FSCO/FSSL), untouched by this shortlist and still the M-06 epicenter.

---

## Δ2. Players — new-name anchors `[SEC]` (names NOT deep-covered 07-12)

Roster of 47 FIN top300 members unchanged (JPM, V, MA, BAC, MS, GS, WFC, C, AXP, BLK, SCHW, BX, CB, COF, SPGI, PGR, BNY, HOOD, PNC, USB, CME, **KKR, APO, MCO, MRSH, ICE, AON, TRV, TFC, AFL, ALL, MET, AJG, FITB, STT, NDAQ, XYZ, COIN, IBKR, MSCI, AMP, AIG, PYPL, PRU, HIG, HBAN**). New anchors on the today shortlist:

- **PNC** — 10-K, period 2025-12-31. Super-regional diversified bank (retail + corporate/institutional + asset mgmt), Pittsburgh. Item 1A is **textbook rate/NIM**: "changes in interest rates affect the difference between interest earned on assets vs paid on liabilities → net interest income and margin," and the same rate move "can increase our credit losses" on variable-rate loans. **The purest NIM-vs-credit two-sided bet in the shortlist** — and FINRA shows shorts *easing* (z−0.90) into its 07-15 print. Carries residual FDIC special-assessment (SVB-legacy) noise in the outlook.
- **SCHW** — 10-K, period 2025-12-31. Savings-and-loan holding co: wealth mgmt + brokerage + banking + asset mgmt. **$11.90T client assets, 38.5M brokerage accounts, 2.2M banking accounts.** Item 1A concentration risks = mortgage/HELOC geography + single-issuer margin/securities-lending + **"client cash and net new client assets."** The tell: SCHW is a **rate-two-way** name — higher-for-longer helps its bank-segment NIM but the **cash-sorting** drag (clients moving idle cash to higher-yield) is the offset; a *no-cut* regime is net supportive for the balance-sheet-transactional-revenue recovery. Broker beta on the breadth rotation.
- **ALL / PRU** — P&C (Allstate) and Life (Prudential) insurers = the **float-NIM analog** leg the rotation added. Higher-for-longer reinvests float at higher yields (the insurance version of NIM expansion). Binding variable is *not* NIM but loss-cost/severity (ALL, cat season → rising short 5v5) and spread/annuity flows + credit-portfolio marks (PRU). Both 🟡 in-range on FINRA.

**Unchanged tail (M-06, by reference):** BX / APO / KKR (alt-credit AUM) + BDC layer (FSCO/FSSL) remain the private-credit epicenter; First Brands/Tricolor ~$2B marked losses and JPM's direct Tricolor subprime-auto exposure carry forward as the concrete anti-signal. Nothing in today's data resolves it — it resolves at the prints.

---

## Δ3–4. Value chain — no structural change

7-node map (deposits → lending → capital-markets → payments → asset-mgmt/private-credit → insurance-float → exchanges/data) **carried forward unchanged** from 07-12 §4. Today's shortlist simply **lights up more nodes of the same map**: node 1/2 (PNC deposits+lending), node 3 (SCHW brokerage-adjacent + GS/MS), node 6 (ALL/PRU float). The AI-credit / private-credit cross-exposure still concentrates in **nodes 2 + 5** (COF subprime + BX/APO/KKR alt-credit); rails + exchanges/data (V/MA/CME/SPGI/ICE) remain the rate-and-credit-agnostic tolls. No new deal, spin, or plumbing shift since SPGI's 07-01 Mobility separation.

---

## Δ5. Bottleneck + KPI + anti-signal (delta only)

**Bottleneck — unchanged:** not loan demand, not NIM direction — **the credit-cost trajectory vs the NIM beat**, resolved at the 07-14/15 prints (now T-1).

**KPI dashboard — carried forward; today's live marks:**
| KPI | Live value (07-13) | Δ vs 07-12 |
|---|---|---|
| Curve 2s10s | +38bp, now read as **flattening**; real-10y 2.31% ↑ | characterization worsened; **re-inversion = nearest kill-switch** |
| VIX | **15.8 calm** | ~flat (was 15.84) — no stress priced |
| Fed path | hawkish Warsh, **no-cut binding** | confirmed; supports deposit-repricing/asset side |
| FINRA distress | **BAC z+1.70 lone red**; shortlist (PNC/COF/PRU) shorts *easing* | unchanged pull; broad bid corroborated as clean |
| Sector-flow rank | **#1/11, 12 green / 1 red** | broadened materially |
| NIM / NCO / CET1 | **report card 07-14/15** | still pending — the resolver |
| Private-credit/BDC marks | First Brands/Tricolor ~$2B, unresolved | unchanged |

**Anti-signal — priority re-ranked for today:**
1. **Curve re-inversion (elevated today).** With the curve now *flattening* (not steepening) and real-10y rising into a hawkish-Warsh/hot-CPI week, a flip back through zero compresses NIM and kills M-01 from the rate side. **This is the nearest fork — CPI this week is the trigger.** (Prior run ranked the credit event first; today the rate-side risk is the fresher one.)
2. **Credit event (unchanged).** A neocloud/leveraged-loan/private-credit/subprime default (First Brands/Tricolor template) forcing sector-wide reserve builds. BAC's z+1.70 is the market's pre-position; COF's short-*cover* (28.8%) says the tail is not being pressed into the print.

---

## Handoff to Phase 3 (delta, 3 lines)
1. **Delta:** FIN-OW bid **broadened + cleaned up** — sector-flow **#1/11, 12 green/1 red**, shortlist now spans regional-bank (PNC) + broker (SCHW) + P&C/life insurer (ALL/PRU), all with FINRA shorts *easing*; macro shifted the NIM story from steepening-tailwind to **flat-curve-but-no-cut** (supportive asset side, **re-inversion now the nearest kill-switch**). Prints at **T-1**.
2. **Cleanest broad-NIM beneficiary → carry: PNC** — purest two-sided NIM-vs-credit super-regional, shorts easing (z−0.90) into its own 07-15 print; **SCHW** the cleaner *asset-gatherer* alt ($11.9T client assets, no-cut regime eases cash-sorting drag). **JPM** remains the money-center leader (unchanged).
3. **Watch/UW → carry: BAC (z+1.70, lone red)** the pre-print consumer-credit worry (07-15); **COF** flagged as tail but FINRA shows a short-*cover* (28.8%) = not being pressed; **BX/APO/KKR + BDCs** unchanged private-credit epicenter, unresolved until the prints.
