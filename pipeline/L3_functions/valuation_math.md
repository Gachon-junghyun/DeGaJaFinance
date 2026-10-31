# L3 · valuation_math — split the group, solve the price backwards, build the ladder forwards

> **Single-role unit** (merged 2026-10-31 from holdco_split · implied_expectation · target_bridge). Does ONE job:
> turn a price and stated assumptions into **conditions and a per-share number**. No verdict (P4).
> §A runs in CO_STRUCTURE (when listed subsidiaries exist); §B–§C in CO_VALUE. All three measured on
> 2026-08-28, 034020 두산에너빌리티, where each **changed the call** — and the order is the safety: without §A
> the other two compute wrong numbers precisely.

## §A · Holdco split — value and earnings left for the parent's own business
034020: consolidated revenue 17.06조 = parent 7.79조 (45.7%) + **Bobcat 8.79조 (51.5%)** + Fuel Cell 0.42조.
2026E controlling NI 3,193억: 🔴 **Bobcat share ≈ 2,713억 = 85%**, parent ≈ 1,000억, Fuel Cell share **−400억**.
Market cap 56.50조 − Bobcat stake 2.91조 − Fuel Cell stake 1.03조 = **parent 52.55조**. «Forward PER 177×» had excavator profit in the denominator.
1. Stake and **share count** from the original: KR DART `otrCprInvstmntSttus` (`trmend_blce_qy`, `trmend_blce_qota_rt`); US 10-K Ex 21 (percent only ⇒ lower precision).
2. Stake value = shares held × **same-day** close (not % × subsidiary cap — treasury/preferred break it).
3. Value: parent cap − Σ listed stakes = parent cap; + **parent-segment** net debt (not consolidated) = parent EV.
4. Earnings: subsidiary consensus controlling NI × stake = its share; parent = consolidated − Σ shares. Loss-making subsidiaries stay **negative**.
5. Write the residual (034020: −120억); never delete it.
Guards: no holdco discount here (it is judgment; downstream may apply it once). 🔴 **Check reporting currency** —
Bobcat's DART statements are **USD** ($6.182B FY2025); read as KRW they look like 6.18조 and «consolidation is broken».
Annualized parent earnings (034020: H1 535억 ×2) are marked **estimate**. Unlisted subsidiaries at book, labeled, kept out of the remainder.
Output: value table + earnings table + one line «the parent earns X% of consolidated controlling NI».

## §B · Implied expectation — what must be true for today's price
Inputs from §A (never consolidated figures).
1. PER candidates ×3: required earnings = parent cap ÷ PER; multiple of today = required ÷ current.
2. Revenue/margin: EV ÷ `1/(WACC − g)` = required EBIT; required revenue per margin scenario. **Print WACC and g.**
3. Order industries: parent EV ÷ backlog vs the industry range.
034020: PER 25/40/60 ⇒ parent earnings **21× / 13× / 9×** today; WACC 9%, g 2% ⇒ EBIT 3.96조 ⇒ revenue 33조 at 12% (4.0×) or 26조 at 15% (3.2×);
EV/backlog **2.15×** (industry 0.3–0.8). «It is expensive» is taste; «earnings must grow 21×» is arithmetic.
Guards: back-solving is not refutation; 🔴 a depressed denominator (cycle low, one-off, loss-making subsidiary) inflates the multiples —
state the denominator's nature in one line (034020: annualized H1, segment margin 3.7% near cycle low).

## §C · Target bridge — ladder, scenarios, one target
Route A (12 months): one earnings metric (EBITDA for order/equipment names; mark estimates as estimates) × **global measured peer
multiples, dated** (3–5; domestic-only peers float with the theme) ⇒ − net debt + stake values ÷ shares. 🔴 **Put today's price on the ladder.**
Route B (3–5 years): 3–4 scenarios incl. «the world today's price assumes»; target-year cap discounted (print rate and years); probabilities with who set them.
Narrow: one table of both routes, pick **one** target with one line why — stand on the generous side (a conservative target is dismissed as engineered).
034020 ladder on parent 2027E EBITDA 7,600억 (estimate): 25× (Siemens Energy 24.3) 29,500 · 33× (BWXT 32.9) 39,000 · 40× 47,300 ·
**46.5× 55,000 (adopted, −37.6%)** · 63× (GE Vernova 62.7) 74,600 · 🔴 **74.5× = market 88,200** — 19% above the world's most expensive peer.
Cross-checks: scenario-weighted 34,000 · peer PER median 33,700 · top domestic multiple 71,800.
Guards: 🔴 write the estimate the target hangs on into «확인 못 한 것» (034020: undisclosed segment 2027E EBITDA). Broker targets are a
**control group** only — convert to a multiple (034020 consensus 129,000 = **2028E PER 103×**). Take stake values from §A, never recompute.
Output: ladder (with market row) + method comparison + adopted target + the hanging estimate.
