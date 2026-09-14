# SECTOR_DEEP_COMM — industry_US — 2026-08-07 (Fri) · **ROTATING → FULL FRESH MAP**

> 10 runs uncovered (last 2026-07-28). Everything below is re-measured, not inherited. Flow `asof
> 2026-08-06 settled` unless marked live; fundamentals/EDGAR pulled 2026-08-07. Bench **SPY** inline
> throughout (C1). Analytical only — zero sizing, zero buy/sell language (P4). Read-only.

## 0 · The two mandate questions, one line each

1. **Neither pure rotation nor pure small-N artifact — it's a mislabeled breadth claim.** The eqflow>wflow
   relationship survives excluding either `new_green` alone, but collapses when both are excluded
   together (§1) — and one of the two, **EA, is not a live equity** (§2/§4): it delisted 2026-08-04. Once
   that correction is made, the real breadth carrier is **telecom/cable (T, VZ, CMCSA), not gaming**.
2. **Built for Meta on primary evidence (§6); could not be built for Alphabet — tagged `[unverified]`
   (§7).** Meta's own 10-Q already names the AG's $62.85bn tail-risk ask; no 8-K exists for either event.

---

## 1 · Flow, decomposed — the leave-one-out arithmetic

`SECTOR_FLOW_US.json`: n **13** · wflow **+0.058** · eqflow **+0.136** · breadth **0.150** (2🟢/13≈0.154,
close enough to be the definition) · Δ **−0.026**.

| Universe | n | eqflow | vs wflow +0.058 | Breadth-led? |
|---|---|---|---|---|
| Full sector | 13 | **+0.136** | eqflow > wflow | ✅ yes |
| Excl. DIS only | 12 | +0.087 | still > | ✅ yes |
| Excl. EA only | 12 | +0.089 | still > | ✅ yes |
| **Excl. BOTH** | 11 | **+0.031** | **< wflow** | ❌ **no — flips** |
| **Excl. EA only (data-integrity correction, see §2)** | **12** | **+0.087** | **still >** | **✅ yes, survives the correction** |

⇒ **S5 binds (n=13 is small) but this is not a single-name artifact**: removing either carrier alone
leaves eqflow>wflow intact; only removing *both* kills it, and EA should be removed on data-integrity
grounds regardless (§2), not as a robustness test — **the read survives on the corrected n=12.** Mcap
check: Σ(flow×mcap)/Σmcap = **0.0576**, matching wflow 0.058 (**GOOGL+GOOG = 76.3% of sector cap; sector
cap $11.77tn**).

**History correction (S1/A5)**: `BLINDSPOT_PREMORTEM.md`/`SECTOR_ROTATION.md` both call today's eqflow
*"2nd-highest of 17 sessions."* Reconstructed from `llm_outputs/sector_flow/history.json` with the
identical 13-ticker mean: **today (+0.1363) is 3rd-highest of 17** — 07-29 (+0.2777) and 07-14 (+0.1758)
both exceed it. The mean **+0.0108** matches but is dragged down by **07-20, a session where only 2 of 13
tickers had data** (a coverage collapse, not a reading). **Excluding it: n=16, mean +0.0473, today ranks
3rd of 16.** Conclusion unchanged (not a one-day spike; risen 2 straight sessions: −0.070→+0.094→+0.136)
but the prior magnitude claim needed this fix before being carried forward again.

---

## 2 · ★★★ The assignment: does ANY name have a positive revision book?

Pulled all 13 (`module_fundamentals_us`, 2026-08-07). Table: 90-day EPS estimate momentum (both quarterly
and annual — C2) and 30-day current-year revision breadth.

| Ticker | CQ 90d | NQ 90d | CY 90d | CY breadth 30d | Read |
|---|---|---|---|---|---|
| **DIS** 🟢 | −4.1% | −2.9% | +1.3%* | **1↑/7↓** | Deteriorating (confirmed) |
| **EA** 🟢 | `unknown` (C3) | `unknown` | −13.6%/7d | 0↑/1↓ | **See below — not a live security** |
| GOOGL 🟡 | −0.3% | +1.7% | +44.7%⚠ | 44↑/0↓ | Suspect base-effect, flag below |
| GOOG 🟡 | −0.4% | +1.7% | +44.5%⚠ | 38↑/0↓ | Same instrument, same flag |
| META 🔴 | −4.3% | −3.2% | −2.9% | 8↑/9↓ | Negative |
| NFLX 🟡 | −2.4% | −1.1% | −0.3% | 12↑/23↓ | Negative |
| **TMUS** 🟡 | +0.5% | **+5.7%** | `unknown` (C3, 90d col=0.00) | **15↑/3↓** | **Genuinely positive, broad** |
| **VZ** 🟡 | −0.7% | +1.8% | +1.2% | **10↑/2↓** | **Genuinely positive, broad** |
| T 🟡 | −0.8% | −3.9% | +0.9% | 15↑/3↓ | Mixed: near-term down, CY breadth up |
| CMCSA 🟡 | −3.5% | −4.9% | −0.5% | 9↑/9↓ | Negative-to-flat |
| WBD 🔴 | n/m (near-$0 base) | n/m | n/m | 1↑/3↓ | Base too small to trust the % |
| TTWO 🔴 | n/m (sign-flip base) | −32.1% | −44.3% | 4↑/0↓ | **Contaminated by today's print, see §4** |
| LYV 🟡 | −12.4% | +7.0% | n/m (near-$0 base) | 1↑/1↓(n=2) | Too small-n to read |

*DIS CY 90d reads +1.3% against a 1↑/7↓ breadth — the level and the breadth disagree; breadth is the
better read here per this desk's own standing rule.

⇒ **Yes — a positive revision book exists in this sector, but not where the flow tag put it.** **TMUS**
(NQ +5.7%/90d, CY breadth 15↑/3↓) and **VZ** (broad positive breadth, CY 10↑/2↓) are genuinely, broadly
upward-revising — both 🟡, neither a `new_green`. **The two names actually carrying the promotion (DIS,
EA) do not have one.** ⚠ **GOOGL/GOOG's +44.7%/+44.5% CY 90d-change is flagged, not used**: the
90-day-ago base (14.22/14.23) is inconsistent with both companies' own quarterly run-rate (CQ+NQ ≈ 6.3,
four-quarter implied CY ≈ 12–13) and trailing EPS ($19.93/$19.94) — reads as a **data-series base-effect**,
not 47 analysts organically converging to a unanimous 44↑/0↓. **Tagged `unknown` (C3)**, not carried.
**Margin percentile (L2), where obtainable**: TMUS 45.0% GM = **20th %ile** (fwd P/E 12.40×) · VZ 58.0% =
**0th %ile** but truncates at FY2017 (stale 9yr) · EA 79.0% = **89th %ile**, near record (fwd P/E 21.78×)
· DIS/CMCSA: **no annual series returned at all.** ⇒ **5 of 13 names have unusable/truncated margin
history — an instrument gap, stated per D91, not substituted.**

**Verdict on ROTATION's own framing**: the sector-level claim (*"no name has a positive book, notch comes
back"*) is **falsified — TMUS/VZ exist** — but the promotion-specific claim (*"the two carriers of the
promotion are deteriorating"*) **still stands, and is now worse than deteriorating for one of them.**

---

## 3 · Players ∪ thematic — who does what, IR-anchored

| Name | mcap | Node | What it does | IR anchor (primary) |
|---|---|---|---|---|
| GOOGL/GOOG | $4.49tn/$4.48tn | Ad platform + cloud | Search/YouTube ads, Cloud, Gemini | 8-K Item 2.02, 2026-07-22 (Q2 print) |
| META | $1.47tn | Ad platform | Facebook/Instagram/WhatsApp ads | 8-K Item 2.02, 2026-07-29; 10-Q filed 2026-07-30 |
| NFLX | $326bn | Streaming | Subscription video | — |
| TMUS | $197bn | Wireless carrier | Postpaid/prepaid wireless | — |
| VZ | $189bn | Integrated carrier | Wireless + fixed broadband | — |
| DIS | $180bn | Studio/streaming/parks | Content, Disney+, parks | 90d/30d revision pull above |
| T | $153bn | Integrated carrier | Wireless + fiber, marketed debt 07-27 (FWP, per 07-28 file) | — |
| CMCSA | $80bn | Cable/broadband | Xfinity broadband, NBCUniversal | — |
| WBD | $66bn | Broadcasting/studio | HBO Max, linear networks | — |
| EA | $51bn (frozen) | **Now private** | Sports/interactive games | **8-K Item 2.01/5.01, Form 25-NSE, both 2026-08-04** |
| TTWO | $44bn | Interactive gaming | GTA, sports titles | 10-Q/earnings 2026-08-07 (beat, GTA6 preorders "exceptional") |
| LYV | $40bn | Live events | Concert promotion, ticketing | — |

---

## 4 · Value-chain node map, with the binding constraint marked

| Node | Names | flow (RS20/RS60 vs SPY) | **Binding constraint** |
|---|---|---|---|
| **① Ad platforms** | GOOGL 🟡+0.118 (−2.6/−11.9) · GOOG 🟡+0.051 (−2.1/−11.8) · META 🔴−0.275 (−8.8/−5.5) | 89% of sector cap | **Regulatory/product-design risk (§6)** — not demand, not capacity. First US ruling to touch the product surface, not the balance sheet |
| **② Telecom carriers** | T 🟡+0.556 (+10.4/−8.6) · VZ 🟡+0.457 (+9.0/−4.5) · TMUS 🟡−0.236 (−3.1/−9.7) | Genuinely positive revisions (§2) | Capital cost / debt-funding, not demand — T marketed debt 07-27 per the 07-28 file |
| **③ Cable/broadband** | CMCSA 🟡+0.472 (+5.6/−3.4) | — | Secular cord-cutting/broadband-share erosion; **not** a bottleneck in the classic sense — demand is the thing declining |
| **④ Streaming/studio** | NFLX 🟡+0.112 (−4.6/−17.7) · DIS 🟢+0.734 (+6.6/−4.0) · WBD 🔴−0.237 (−3.1/−7.0) | DIS's book is negative (§2) | Content-slate timing and subscriber-growth deceleration; not supply-constrained |
| **⑤ Interactive gaming** | EA — **delisted 2026-08-04**, frozen · TTWO 🔴−0.697 pre-print (−7.8/+1.0) | Real print today: beat, GTA6 preorders | **The binding constraint is GTA6's own delivery timeline** — TTWO's Zacks-cited FY estimates ($6.86 CY, $8.56bn revenue) assume the title ships; no confirmed date found this run |
| **⑥ Live events** | LYV 🟡+0.017 (−2.7/+7.6) | — | Venue/tour-calendar supply — the one node where "strong demand" is arguably real and not mistaken for a bottleneck (flagged so as not to violate the framing rule) |

Strong demand is explicitly **not** marked as a binding constraint anywhere above except where a name's
own supply timeline (⑤) is the actual gate.

---

## 5 · Chain-hop candidates

`chain-hop age verification teen --days 5` returned **zero credible body-proximate candidates** — the
top "un-named-beneficiary" hits (GS/C/AVGO/VZ/BRK-B/LRCX…) are boilerplate co-occurrence in unrelated
listicle articles ("If I Were in My 20s, I'd Buy This ETF…"), the D10 boilerplate-dominance failure mode
already logged by this desk. **No candidate reaches BET this run** — a null result, not fabricated. VZ
appears in the noise list but is already a named sector constituent (§2), not an un-named beneficiary.

---

## 6 · The Meta judgment — building the legal-liability observable

**Primary evidence assembled**: `module_disclosure_us META` (90-day EDGAR window) shows **no 8-K filed
for the 08-06 ruling as of this check** — only the 07-29 earnings 8-K and the 07-30 10-Q are on file. Per
D186 (measured false negatives), this is stated as **"no observable found,"** not proof none exists.
⚠ Direct SEC fetch of the 10-Q (`meta-20260630.htm`) and the EDGAR submissions API both returned **HTTP
403** this run — a tool-access limit, not a disclosure absence.

**What IS confirmed, body-quoted, primary-adjacent** (`[cnbc 08-06 full body]`): *"Meta noted in its
second-quarter financial filing that, 'the New Mexico Attorney General has indicated that they intend to
seek up to $62.85 billion in penalties in this case.'"* ⇒ **the risk was already disclosed in the 10-Q
before the ruling landed**, and the $942M actual judgment is **1.5% of the AG's own disclosed ask** —
this is the receipt for "$942M is immaterial at Meta's scale."

**Testing the engagement-cap-as-revenue-mechanism reading**: `module_flow META --positioning` (live):
**short 1.7% float building, DTC1.9 · options P/C 0.65 (call-heavy) · IV skew −2.0 (no elevated downside
fear) · implied move ±1.3% (D0, expiry 2026-08-07).** ⇒ **options are not pricing this as a structural
earnings-mechanism event** — a call-heavy skew with negligible downside premium is the opposite of what
a genuine ARPU-impairing ruling would print. **META settled 589.90, +0.19%**, agreeing with the options
read, not the "revenue mechanism" framing. This does not resolve which read is right; it says **the
market has not yet priced the injunctive leg as material** — either early, or the framing overstates it.

**Replication risk, quantified rather than asserted** (`[fox business 08-07 full body]`): *"More than 40
states and over 1,300 school districts have already filed public nuisance lawsuits against social media
companies"*, and AG Torrez called the ruling **"a blueprint… other states, and other countries… have a
roadmap they can follow."** ⇒ **this is the observable**: track a second state's court **adopting** the
public-nuisance theory (not merely filing — New Mexico's own suit was filed in 2023, three years before
this ruling) by **2026-09-06**, cross-referenced against META's RS20 vs SPY. `EVENT_ALPHA.md` Card 4 has
already framed this identical KPI/kill-condition pair — **not duplicated here, cited and adopted.**

---

## 7 · The Alphabet leg — personnel event, no measurable mapping

`module_disclosure_us GOOGL`: the only Item 5.02 8-K in the 90-day window is dated **2026-06-05**,
five weeks before the Hassabis/Dean reshuffle (thread ran 08-01→08-06 per ROTATION). **No 8-K exists for
this event.** Consistent with the facts (`[businessinsider 08-07 full body]`): Hassabis moves to Chief
Scientist at Alphabet and stays DeepMind chairman — **he does not depart the company**, which is the
likely reason no Item 5.02 filing was triggered (an internal reassignment, not an executive departure).
Jeff Dean's departure to found a new company is the closer fit for an 8-K-triggering event and still has
none filed.

⇒ **`[unverified]` (A5): this repo has no disclosure-side or flow-side instrument that maps a personnel
event to a security-specific observable independent of the price action already captured by RS20/exc5.**
The only measurable fact is price: **GOOGL fell up to 6% intraday on the news** (`[businessinsider]`) and
**live flow now reads RS20 −2.8% / RS60 −12.9%** (vs the settled −2.6/−11.9, a small further slip), with
**exc5 vs SPY now +3.60 per ROTATION's own read — absorbed on the 5-day window.** **Do not drop P28′'s
KPI** (2027 capex guide language) — no capex disclosure has occurred, and personnel is not a substitute
observable for a capex commitment.

---

## 8 · W5 dispersion — is "Communication Services" the wrong unit?

RS20 vs SPY spans **T +10.4 to META −8.8 = 19.2pp**; RS60 spans **NFLX −17.7 to TTWO +1.0 (pre-print) =
18.7pp**. Against **XLC settled +0.28% on the day, exc5 +0.69 / exc20 −1.64 vs SPY.**

The split is **not** advertising-vs-everything by mcap weight — it is **telecom+cable (T/VZ/CMCSA, all
positive RS20, all OBV 매집) against everything else (GOOGL/GOOG/META/NFLX/TMUS all negative RS20)**, the
same carriers-vs-platforms axis found 07-28, sign **unchanged** (carriers still lead). **19.2pp of RS20
spread inside 13 names against a sector ETF move of +0.28% on the day — roughly 69× the label's own daily
move.** ⇒ **S5/B5: "Communication Services" is the wrong unit for anything except the carrier sub-node.**
Two integrity notes belong here, not a footnote: **GOOGL+GOOG are one company filed twice** (effective
distinct-company n=12), and **EA is delisted but still counted as live** (effective tradable n=11). **Of
the nominal 13, 11 are single, live, distinct, tradable companies.**

---

## 9 · Track KPIs and anti-signals, dated

| KPI | Now | Test |
|---|---|---|
| **S68 leg (i) integrity** | median RS20 of {DIS, EA} registered +2.943 | 🚨 **EA's price has been frozen at $209.70 since 2026-08-04 close (0 volume 08-05, 08-06 — verified via yfinance history)**; its RS20 between now and the 2026-08-13 settle is a **deterministic function of −SPY's own cumulative return**, not a market signal. **New dig, not a re-score**: whoever settles S68 should know leg (i) is half contaminated by a non-trading security |
| **TMUS/VZ revision persistence** | CY breadth 15↑/3↓ and 10↑/2↓ (30d) | Re-check 7-day breadth next run; if it holds, this is the sector's actual A-grade leg, not DIS/EA |
| **DIS revision breadth** | 1↑/7↓ (30d), unchanged from 07-28's T-adjacent read | If it turns net-positive at any horizon, the notch's narrowing (§2) needs revisiting upward |
| **META second-state adoption** | 0 states have adopted the public-nuisance theory beyond NM as of today | 2026-09-06 horizon (adopted from `EVENT_ALPHA.md` Card 4) |
| **GOOGL capex guide language** | pending, no disclosure yet | P28′ KPI, unchanged, next disclosure date not yet in window |
| **TTWO/EA node** | TTWO beat, GTA6 preorders "exceptional," stock rising 08-07 | EA cannot re-price on this (delisted); the gaming node's only live expression going forward is TTWO alone |

**Anti-signals**: a genuine organic (not print-triggered) reversal in TMUS/VZ breadth to net-negative ·
any 8-K on the Meta ruling appearing (would resolve the D186 absence question) · a second state court
ruling adopting the public-nuisance theory before 2026-09-06.

---

## 10 · What this hands to BET

- **Names with a real, broad, positive revision book in this sector**: **TMUS** (CY breadth 15↑/3↓,
  NQ +5.7%/90d) and **VZ** (CY breadth 10↑/2↓) — flow **🟡**, not `new_green`, margin percentile 20th
  (TMUS) and stale/`unknown` (VZ). `asof 2026-08-06 settled`.
- **EA (`ticker`, flow 🟢, `vol_surge` 3.78) should be struck from any forward flow read** — confirmed
  delisted 2026-08-04 (Form 25-NSE + 8-K Item 2.01/5.01, same date), price frozen $209.70, zero volume
  08-05/08-06. The `vol_surge` reading is the merger-close-day liquidation volume (48.7M shares on
  08-04), not incremental interest. `data/us_universe/us_top300.csv` was last rebuilt 2026-07-15 and
  still carries EA as live — a universe-staleness defect affecting any downstream module that reads it.
- **DIS**: flow 🟢 stands on price, but revision book (1↑/7↓, CY) is negative — unchanged from the notch's
  own stated caveat.
- **META**: 🔴분산, options positioning (P/C 0.65, skew −2.0) does not price the ruling as structural;
  10-Q already discloses the AG's $62.85bn tail figure; track per §6/§9.
- **GOOGL/GOOG**: 🟡, CY 90d revision figure (+44.7%/+44.5%) flagged `unknown` (C3) on suspected base
  effect — do not carry as a fundamental positive without independent confirmation.
- **Chain-hop**: no candidate cleared this run (§5) — null result, not absence of effort.
- **Sector unit**: treat COMM's carrier sub-node (T/VZ/TMUS/CMCSA) separately from the platform sub-node
  (GOOGL/GOOG/META) going forward — a 19.2pp RS20 spread inside 13 names says the label conflates two
  different trades (§8).
