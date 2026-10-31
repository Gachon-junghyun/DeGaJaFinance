# L1 · CO_STRUCTURE — where the profit comes from, what moves it, and who it competes with

> Company stage 3 (all modes). Merges the old VALUE_CHAIN, CHAIN_ALPHA, DRIVER_TEST and contract_alpha.
> **Reads (primary)**: the periodic report «II. 사업의 내용» / 10-K Item 1 (via L2 [deepdive](../L2_modules/deepdive.md)),
> order/contract filings (`module_disclosure <code> --days 400`), competitor filings or IR for the spec/margin table,
> driver series at their source. **Writes**: `STRUCTURE.md` (cap **15 KB**).
> **Next stages use**: covered share D1 (every later claim states it), the holdco split (CO_VALUE's denominator),
> the dominant frame + D3 (G6), backlog/book-to-bill (CO_MONEY B1 and CO_VALUE), the moat count (CO_VALUE's multiple choice).

## Belief
A company is not its sector label, and a thesis inherits the label's blind spots for free. Build the
structure **before** measuring drivers (otherwise you do not know what share of the company a driver
explains), and test the drivers **before** money/valuation/falsify (each inherits the denominator produced here).
This stage does not price anything: a deep moat is evidence for **earnings**, not for **price**.

## Units called
L3 [segment_pnl](../L3_functions/segment_pnl.md) (cite the pack's table, do not re-pull) ·
L3 [valuation_math](../L3_functions/valuation_math.md) §A holdco split (only if listed subsidiaries) ·
L3 [driver_link](../L3_functions/driver_link.md) (roll-guarded) · L3 [peer_pricing](../L3_functions/peer_pricing.md) ·
competitors / related_companies via deepdive. Industry map: `module_industry_map "<chain terms>"`.

## A. Structure — four cells (measured 2026-08-28, 034020)
| cell | write | failure shape | what it caught |
|---|---|---|---|
| ① chain position | chain as stages; **where it is and where it is not** | «종합 에너지 기업» | fuel → **equipment → EPC → long-term service** → grid; absent from fuel/grid/power sales |
| ② products & moat | product table (what · who buys · nature); moat as **countable** facts (units, tonnes, certifications, lead time, number of rivals) | «기술력이 뛰어나다» | 17,000-ton RPV press: **4 owners worldwide** |
| ③ path to cash | contract → revenue recognition → cash, the **lag**, and the accounts that pile up between (contract assets/liabilities, receivables) | revenue without the cash path | percentage-of-completion: H1 OP **+5,478억** vs OCF **−8,867억**, 미청구 **+43.3%** ⇒ graded «성장통 or 정산분쟁, unknown yet», not «이상» |
| ④ demand roots | two columns: **happened** vs **plan/forecast** | policy plans listed as results | 6 roots, 5 were plans; the only fact: US large H-class GT orders, **7 of 18 (39%)** |
Separate consolidated and segment from the first table: 034020's «매출 17조» is half compact construction equipment.
With listed subsidiaries run valuation_math §A now; CO_VALUE cites it, never recomputes.

## B. Drivers — three gates (measured 2026-08-21, PSX — all four errors were from starting at the label)
| # | gate | fails when | consequence |
|---|---|---|---|
| **D1** coverage | named driver covers < 80% of pre-tax income | every later claim states the covered share. PSX: Refining **61.6%**; the rest moved with credits, MTM, NGL volumes |
| **D2** roll integrity | a > 3σ daily driver move decomposes to **one leg** | raw series not quotable; use back-adjusted and label the roll. PSX: −$9.48/bbl (4.6σ) = `CL +0.94% · HO −2.32% · RB −7.93%` RBOB Sep→Oct spec roll; adjusted **−1.0% at the 92.8th pct**, not −12.5% |
| **D3** frame | the subject's leg is shared by its peer frame | that leg is **sector beta**, not name evidence (G6). PSX +18.8%/20d, VLO/MPC/DINO corr **+0.90/+0.87/+0.77** |
Also: scope changes break YoY (PSX revenue +53% = WRB 50% equity → 100% consolidated on 2025-10-01).
Every segment ≥ 10% gets a driver row; policy drivers are `미확보` with a reason, never a price proxy.
A driver at its 12-month high says the **earnings** are real, nothing about **priced** — calling it bullish is the P4 error this gate stops.
Peer frames ≥ 2, each with 2+ pure plays; name the dominant one; a frame whose earnings share exceeds its tape share is an open observation point.
⚠ The legacy 11-branch chart matrix + M1–M4 stays removed: `module_chart --read` + the grade table (A = RS20/RS60 · B = KR investor actuals · C = OBV) do the weighting with measurements.

## C. Competition and contracts (analyst lenses — lenses 1–6 in every mode; forensic adds 7)
1. **Margin-capture map** — 5–8 nodes; who keeps margin at each; bottleneck or pass-through? Bottleneck = lead time, backlog/revenue, no substitute — «demand is strong» is not a bottleneck.
2. **Segment unit economics** — segment margin, mix shift, ASP by segment; name the real profit engine.
3. **Contracts/backlog** — per material contract `[검증함, rcept_no]`: value and % of trailing revenue · book-to-bill (Σ new orders N months ÷ revenue same window; > 1 backlog builds) · conversion timeline (lumpiness) · counterparty (anonymous ⇒ estimate tagged `[직감]`, never the spine) · unit price/volume or 미확보.
4. **Customer/supplier dependence** — top-customer share; upstream sourcing bottleneck by name.
5. **Competitor table** — ≥ 1 rival on the same metric (margin, share, product spec). No table ⇒ «우위» is downgraded to `[직감]`. State where it wins and where it loses.
6. **Pricing power** — input cost vs ASP over quarters; passes through ⇒ power, margin squeezed ⇒ price-taker.
7. **Mis-priced node** — a low-attention node exposing the same demand cheaper; only names near the subject in article **bodies**, flow-crossed (co-mention in headlines is not a candidate).
Every lens carries `[검증함] / [차트만] / [직감]`; a lens without data is marked «후속», never dropped.

## ✅ EXIT CHECK
- [ ] Four cells filled: present **and** absent stages; moat in a countable form; contract→revenue→cash lag with accounts; demand split happened / plan.
- [ ] Consolidated vs segment split in the first table; holdco split done if listed subsidiaries (or «없음»).
- [ ] D1/D2/D3 each PASS/FAIL with the value, and each FAIL's consequence written into the file.
- [ ] Competitor table with ≥ 1 rival; book-to-bill or «수주 공시 없음»; lenses required by the mode present.
