## Status legend
`ARMED` registered, event pending · `FIRED-A/B/C` branch that occurred · `EXPIRED` date passed unscored
(a scoring failure, log it) · `VOID` premise invalidated before the event

---

## Scoring log

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| S1 | 2026-07-22 | 2026-07-22 AMC | **FIRED-A** | 2026-07-23 HANDOVER (industry_kr) | FY26 capex guide $180–190B → $195–205B; observable pulled cleanly, no judgment call |
| S2 | 2026-07-22 | 2026-07-29 | — | — | ARMED |
| S3 | 2026-07-22 | ~2026-09/10 | — | — | ARMED |
| S4 | 2026-07-22 | ~2026-09 | — | — | ARMED |
| S5 | 2026-07-22 | ~2026-08-11 | — | — | ARMED |
| ~~S6~~ | 2026-07-22 (PREMORTEM) | 2026-07-23 | — | — | *original row, kept per append-only — **superseded by the annotated S6 row below***|
| ~~S7~~ | 2026-07-22 (PREMORTEM) | 2026-07-23 | — | — | *original row, kept per append-only — **superseded by the scored S7 row below*** |
| S8 | 2026-07-22 (PREMORTEM) | `[blank]` undated | — | — | ARMED |
| S9 | 2026-07-22 (PREMORTEM) | 2026-07-29 + running | — | — | ARMED |
| S10 | 2026-07-23 | 2026-07-24 | — | — | ARMED |
| S11 | 2026-07-23 | 2026-07-29 | — | — | ARMED — found via a 10-day catalyst-calendar re-pull; the standard 5-day window misses this date entirely |
| **S6** | 2026-07-22 (PREMORTEM) | 2026-07-23 AMC | — | — | **ARMED (annotated 2026-07-23)** — the registered ±4.4% was tagged D0 / "a FLOOR, not a fair estimate"; a fresh pull gives **±12.7% (expiry 07-24, D1, covers the event)**, i.e. **2.9× the registered figure — the floor caveat is measured to have been correct.** ⚠ The **frozen observable is UNCHANGED** (a named external 18A customer, or capex/utilisation guided up); only the magnitude context is annotated |
| **S7** | 2026-07-22 (PREMORTEM) | 2026-07-23 pre-mkt | **FIRED-A (backlog leg)** · band leg **deferred** | 2026-07-23 HANDOVER (industry_US) | RTX backlog **$289B** (from $271B), FY26 revenue guide raised to **$95–96B**; LMT **record $230.4B** on **$65B of quarterly orders** (b:b ≈3.2×), FY sales guide raised to $79.75–81.75B. **Backlog up at both, unambiguous.** ⚠ Branch A also required both to move outside their implied bands — **unscoreable at run clock (09:1x ET, session not open)**; scoreable only against the 07-23 close, at the next HANDOVER. ★ **Registration defect logged (dig D28)**: S7 put a *price reaction* inside the branch condition of an *observable*, contradicting L3 `scenario_score`'s own rule. Future brackets put implied-move bands in a separate, labelled reaction test |
| S12 | 2026-07-23 (PREMORTEM) | 2026-07-23 | — | — | ARMED — D-0 binary **absent from CATALYST_WATCH** (D18, 3rd consecutive run). Information grade **modest**, kept small on purpose |
| **S13** | 2026-07-23 (PREMORTEM) | 2026-07-29 | — | — | ARMED — ★ **the branch nothing in the book bracketed**: a capex RAISE priced as a margin drag. Cross-condition; no usable implied move (both straddles expire before the event) |
| S14 | 2026-07-23 (PREMORTEM) | 2026-07-30 | — | — | ARMED — settles DEEP ②'s own question (is FIN's eqflow +0.320 breadth, or a payments/insurance concentration?) |
| S15 | 2026-07-23 (PREMORTEM) | 2026-07-30 | — | — | ARMED — the independent series that can break P1's "reaction-function, not inflation" framing. ⚠ threshold is judgement, flagged |
| S16 | 2026-07-23 (PREMORTEM) | 2026-07-29 | — | — | ARMED — tests whether COMM N− is a sector verdict or a misapplied single-name one (GOOGL 🔴 vs META 🟢 on the same 07-22 close) |
| **S6** | 2026-07-22 (PREMORTEM) | 2026-07-23 AMC | **FIRED-A** | **2026-07-24 HANDOVER (industry_kr)** | **Both legs of the frozen observable fired.** (i) **Named external foundry customer: Fortinet** — *"Fortinet becomes Intel 4's first foundry customer"* [tomshardware 07-22, yahoo_finance 07-21], announced **before** the print. ⚠ The node is **Intel 4 (mature), not 18A** — satisfies the "foundry customer" clause, not the "18A" clause; logged so the next registration names the node. (ii) **Capex guided up**: *"Intel sales, profit forecast beat estimates; **company boosts spending plans on AI boom**"* [yahoo_finance 07-23]; KR confirm: *"인텔, 2분기 매출 25%↑ 어닝서프라이즈…15년 만에 최대 성장"* [yonhap 07-24]. **Leg (ii) alone satisfies branch A**, so the node dispute does not affect the verdict. Price (context only, not the score): 07-23 regular close **100.23** (−2.3%, *pre*-print), **+10~11% after hours**. ★ The registered ±4.4% "a FLOOR, not a fair estimate" caveat is now **measured correct** (fresh pull ±12.7%). **Meaning**: the US equipment leg (AMAT/LRCX/KLAC) was a pullback, not a downtrend — the industry_US IT underweight is short the wrong thing |
| **S7** (band leg) | 2026-07-22 (PREMORTEM) | 2026-07-23 | **FIRED-A — branch A now COMPLETE** | **2026-07-24 HANDOVER (industry_kr)** | The 07-23 US desk scored the backlog leg and **deferred the band leg** as unscoreable at its run clock. Scored today on the settled 07-23 closes: **RTX 194.88 → 209.16 = +7.33% vs ±5.0% implied → outside** · **LMT 514.36 → 568.59 = +10.54% vs ±5.4% → outside**. **Both outside ⇒ branch A's second condition met**, so backlog-up-at-both ∧ both-outside-bands is satisfied in full. ⚠ **Registration defect D28 stands regardless of the outcome** — a *price reaction* was placed inside an *observable's* branch condition; future brackets put implied-move bands in a separate, labelled reaction test |
| **S10** | 2026-07-23 (industry_kr) | 2026-07-24 | **FIRED-B** | **2026-07-24 HANDOVER (industry_kr)** | Fired **before the KR open**. *"美, 60개국에 '301조 강제노동 관세' 확정…**한국은 12.5%**"* [yonhap 속보 07-24; mk·mt same-hour; 45 articles / 8 outlets = the day's largest cluster]. Threshold was "at or near 12.5–15%" ⇒ **clean FIRED-B**. ★ Direction body-read, which the headline inverts: Korea's government was fighting for a **15% cap** right up to the print (*"정부, 15% 상한선에 촉각"* [yonhap 07-23], *"韓정부, 15% 사수 총력"* [mk 07-23]) — **12.5% landed BELOW the cap they were defending.** Registered meaning holds: LG그룹's disclosed **$28.0bn** US-investment delay risk is unresolved. **Score each name separately (W5)** — measured the same week, **034220 LG디스플레이** (foreign 20d **−652.0만주**, short **5.07%float building +0.98 🔥**) vs **066570 LG전자** (foreign **+85.9만** AND institution **+77.3만**, RS60 **+38.4% vs `^KS11`**): same headline, opposite money. ⚠ **Registration scope was too narrow (new dig D34)**: the bracket named only the two LG entities, while the day's domestic feed named **포스코·현대제철** as additional tariff exposure, and a **`└` sub-event** carried a KR chemicals node (무역위 中 부틸 아크릴레이트 anti-dumping **19.17%**). A 60-country, all-industry measure bracketed on two tickers is a scenario defect, not market noise |
| **S12** | 2026-07-23 (PREMORTEM) | 2026-07-23 | — **PENDING, not EXPIRED** | (checked 2026-07-24) | **The decision printed; the frozen observable did not.** ECB **held at 2.25%** with a **hawkish** tilt — *"ECB Keeps Rates Unchanged, Warns 'Full Energy Inflationary Shock Yet To Come'"* [zerohedge] · *"ECB holds rates at 2.25% as the reignited Iran war keeps a second hike in play"* [euronews] · Lagarde: *"Some asked whether we should consider a hike"* [fxstreet]; market pricing a **September hike** [cnbc / Commerzbank / ING]. **But the frozen observable is `DTWEXBGS`, whose latest FRED print is still 120.53 asof 2026-07-17 — the same value as at registration, i.e. pre-event.** The 3-session invalidation window is still running ⇒ **not EXPIRED. Re-check by 2026-07-28; if DTWEXBGS still has not printed, score `AMBIGUOUS` with the reason and do NOT substitute another proxy.** ⚠ **Registration defect (new dig D35)**: the branches were "hawkish surprise" (A) and "hold-with-**dovish** tilt" (B). **What actually happened — hold with a HAWKISH tilt — is in neither branch.** On the decision axis this is already `AMBIGUOUS`; only the DXY axis remains scoreable. Branch grids must be written on **one** observable axis, or fill the grid on both |
| **S17** | **2026-07-24 (industry_kr MACRO)** | 2026-07-29 → 08-05 | — | — | ARMED — ★ **written because S2's ADR leg turned out to have an unscoreable observable.** Replaces "does conversion open" with the daily-printing ADR premium. Anti-signal: an issuer disclosure raising the ceiling voids it |
| **S18** | **2026-07-24 (industry_kr DEEP-COMM)** | 2026-07-29 | — | — | ARMED — KT sanction hearing, max ₩200bn ≈ 1.5% of cap. **Absent from `CATALYST_WATCH.json` = D18's 4th consecutive occurrence**, and the **6th** trigger stacked on 2026-07-29 |

### Scoring-log rows added 2026-07-30 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S39** | 2026-07-29 (industry_kr DEEP-HLTH/ALPHA, 08:39 KST pre-open) | **2026-07-29 close** (event-conditional: next `069500.KS` ≤ −3.0% session) | **FIRED-B** | **2026-07-30 (industry_kr MACRO §F-0)** | ★★ **It fired on its own registration day and this run's HANDOVER missed it.** The trigger condition — a benchmark session ≤−3.0% — was met the same afternoon: `069500.KS` closed **−6.344%**. HANDOVER listed S39 as *"ARMED · event-conditional"* and **did not check whether the condition had already been met**; MACRO caught it three stages later. **Named as a process failure, same class as an unscored past-dated row**: an undated bracket can be silently filed as not-yet-due. **Observed** (method frozen at registration: β on the 60 sessions ending the day before, `residual = excess − (β−1)×bench`): **207940 −3.38pp** (β 0.18, absolute −4.52%) · **068270 +2.98pp** (β 0.24, absolute **+1.47%**). Registration betas were 0.200/0.258; the shift is the frozen one-day window roll. **Threshold was** A = both > +1.0pp · B = **either < 0** · C = both 0~+1.0pp ⇒ **B fired on 207940.** ★ **Effect on the standing view, exactly as branch B pre-stated**: the 07-28 shelter reading is **n=1 luck**, **M-07 loses its only tested price axis**, and **M-13's shelter half dies — so M-13 is dead on both halves** (driver already gone with R26). ⇒ **R27 filed.** ★ **What survives is a sharper claim**: the property is **one name's**, not 제약's — 068270 ran **+2.16 → +2.98 monotone** while 207940 went **+2.49 → −3.38**, and the rest of the bucket lost (**128940 −11.82 · 326030 −2.76**). ⚠ Scored on the observable, not the price narrative. ⚠ **n = 2 sessions (S1)**, and this run separately measured the estimator's own residual σ at **2.3–3.8pp in a sibling cohort** ⇒ see **S43-ANNEX** |
| **S11** | 2026-07-23 (`catalyst_calendar --days 10`) | 2026-07-29 | — **PENDING, not EXPIRED** | (pulled 2026-07-30) | **The observable was pulled and it has not printed.** Four separate domestic sweeps (`금융위 선진화` 1 hit / irrelevant · `지배구조 금융지주` 6 · `독립이사` 4 · `금융위원회` 70 over 2 days) contain **no FSC governance-package announcement on 07-29**; the term axis agrees (`지배구조` pool-normalised **0.90× = no acceleration on its own event date**). What exists is **hankyung 07-27 [단독]**: the FSC has **drafted** a 금융회사지배구조법 amendment allowing **one reappointment only (3+3 = six years maximum)**, **2/3 shareholder approval to reappoint**, `사외이사`→`독립이사` with an **all-independent 임추위**, and nomination rights at **0.1% ownership** — *"final version to be announced as early as this week."* **Independently corroborated the same day: the announcement was expected 07-22, slipped, and an FSC official states the date is still not set.** ⇒ **REGISTRATION DEFECT, logged**: the branches ask whether the limit is **enacted** (a National Assembly act) while the registered date was an **executive announcement** date — two observables that cannot settle on one day (**same structure as D46**). The draft's content is branch A's *shape*, but drafting is not enacting and **is not scored as A.** **Re-check deadline 2026-08-06**; if still unprinted, score **`AMBIGUOUS`** with the reason and **do not widen the threshold**. ★ Successor **S45** registered on a scoreable observable (the announced clause form). ★ Load-bearing detail carried forward: the draft names **KB금융 (105560), whose next chairman is selected in November, as the first holdco affected** — the first material that could split KB out of the `E.상관가드` risk unit it has been rejected under for five runs |
| **S18** | 2026-07-24 (industry_kr DEEP-COMM) | 2026-07-29 | — **PENDING, not EXPIRED** | (pulled 2026-07-30) | **The deliberation was held on the registered date; the observable publishes today.** Two primary bodies say so explicitly: yonhap 07-29 06:00 (*"개보위, KT 제재안 오늘 심의"*, plenary that afternoon) and **mt 07-29** (*"개인정보위 29일 전체회의, **30일** KT 과징금 제재 수준 발표"*). Web corroboration agrees the final disposition is disclosed ~07-30. ★ **The frozen denominator is confirmed and slightly sharpened**: the statutory cap is **3% of the relevant segment's trailing-3-year average revenue**, and wireless revenue is **₩6.6689tn (yonhap) / ~₩6.5tn (mt)** ⇒ cap **≈₩200bn / ≈₩190bn**, so branch A's ₩150bn line (75% of max) stands unchanged. **Facts logged, not scored** — aggravating: real monetary harm (**368 people · 777 transactions · ₩243m**) and a **2024 server-malware infection not reported to the government** (43 servers); mitigating: **USIM authentication keys were NOT leaked**, scale of **22,227** vs SKT 23m / Coupang 37m, a **₩450bn** customer-compensation programme and femtocell replacement. **Precedents from the same regulator under the same law: Coupang ₩624.6bn ≈ 2% of revenue · SKT ₩127.8bn ≈ 1%.** ⚠ **Not pre-scored**: arithmetic only — branch A requires **≈2.3% of relevant revenue**, above Coupang's 2% and 2.3× SKT's 1%. Tagged `[inferred]`, **not admissible as evidence.** **Scoring deadline: the next run's HANDOVER (2026-07-31). Carrying it a second time is a failure to log as one** |
| **S43 · S43-ANNEX · S44 · S45** | **2026-07-30 (industry_kr MACRO / ALPHA)** | see `SCENARIOS_KR.md` | — | — | ARMED — ★ **S43** is S39's successor and separates *name vs sector* on the shelter property · **S43-ANNEX** is a construction-defect notice registered **hours after S43** because this run's own DEEP measured the estimator's residual σ (2.3–3.8pp) to be **wider than S43's ±1.0pp band** — **S43 is NOT re-frozen** · **S44** scores the crash's *agent* from the KRW sign (the axis `fts --kr` cannot reach at all, D63) · **S45** replaces S11's unsettleable "enacted" observable with the announced clause form |

### Scoring-log rows added 2026-07-31 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S18** | 2026-07-24 (industry_kr DEEP-COMM) | 2026-07-29 심의 → **2026-07-30 발표** | **FIRED-B** | **2026-07-31 HANDOVER (industry_kr)** | **The observable printed and it is not close.** 개인정보보호위 07-29 제15회 전체회의 의결, **07-30 발표: 과징금 ₩539.79bn (539억7,900만원)** [yonhap 07-30 11:27 본문 · mt 07-31 본문 · asiae ×5 = 6개 매체]. Threshold was **A ≥ ₩150bn** / **B < ₩150bn or deferred** ⇒ **B fired at 36% of the line.** **Frozen denominator confirmed from the primary and NOT adjusted after the fact**: 산정매출 **₩6.6689tn** (무선 3년 평균), 법정 상한 3% ≈ **₩190–200bn** — the registration's "≈₩200bn max" was right. **부과율 0.81%**, against 선례 SKT ~1% and 쿠팡 1.8%. ★ **The prior run's `[inferred]` arithmetic was WRONG and was correctly not used as evidence**: it computed that branch A needed ≈2.3% of relevant revenue and tagged the reasoning inadmissible; the outcome came in **below even SKT's 1%**. **Effect, as branch B pre-stated: a sector-level non-event** — ₩53.98bn against KT 본사 annual OP ≈₩800bn is **about a quarter of one quarter's operating profit** (yonhap). ⚠⚠ **REGISTRATION DEFECT, logged as D100**: the bracket froze **the amount only**, so it could not see that **the same 의결 referred KT to prosecutors (거짓자료 제출·로그 삭제) and requested a criminal investigation of LG유플러스 (조사 착수 전 서버 폐기, 공무집행방해)** — a criminal track now open at **2 of the 3 telcos**. The amount is a non-event; the legal track is not. **The verdict is scored on the frozen observable regardless (L3 rule); the defect is recorded, not used to re-score.** Next regulatory bracket writes **amount** and **sanction type** as separate legs |
| **S29** | 2026-07-27 (industry_kr DEEP-HLTH / ALPHA) | **by 2026-08-06** (price-trigger form) | **FIRED-A** | **2026-07-31 MACRO §F-0 (industry_kr)** | ★ **It fired 7 days early, and this run's HANDOVER classified it "미도래" — the SECOND consecutive run in which a bracket's condition was already met while HANDOVER filed it as not-yet-due (S39 was the first, one day earlier).** Both frozen legs, reported separately and not merged: **(1) `068270 close > 189,737` → 07-30 close 190,000 ✅** (margin +₩263 = +0.14%); **(2) 5d/50d volume ratio > 1.0 → 1.783 ✅** (0.78 at registration = a 2.3× rise). ⇒ branch A: *"the accumulation was leading, and it finally cleared the elastic retail supply inside the ₩170,100–183,600 box."* ★★ **The registration's own instruction — "a future scorer must read the FOREIGN leg (M168)" — was executed and it REVERSES M168's leg identification**: into the breakout the foreign leg was **net SELLING three sessions straight (07-27 −8.7만 · 07-28 −15.6만 · 07-29 −14.0만 = −38.3만)** and turned only on the day itself (+4.9만); the buyer was **institution (20d +204.5만 against retail −239.3만)**. **M168's "the live leg is foreign" is marked stale — updated by measurement, not retracted.** ⚠ **Two honest caveats recorded WITHOUT moving the threshold**: (i) the 5-day window contains the 07-28/07-29 circuit-breaker sessions, so 1.783 carries a market-wide volume event — **partially defended by a counter-example measured the same run: 009150's ratio is 0.842 on the identical window**, so the ratio is not pure market beta; (ii) the breakout margin is +0.14%, and the threshold was declared hand-set at registration (no KR implied-move axis exists). **This does NOT substitute for S43** — S43 asks a shelter question that is only testable on a ≤−3.0% session, and 07-30 was −2.199% |
| — | — | — | ★ **Condition-check executed on every event-conditional row (the S39 lesson, first execution)** | 2026-07-31 HANDOVER (industry_kr) | **S43 and S44 both trigger on "the next `069500.KS` session ≤ −3.0%".** Measured: **07-27 +1.283% · 07-28 −11.190% · 07-29 −6.344% · 07-30 −2.199%** ⇒ **the condition has NOT been met since registration; both stay legitimately ARMED.** This is recorded as a *check performed*, not a skip. ⚠ **−2.199% sits just under the line** and the benchmark has fallen 18.5% in three sessions, so either may fire on any session. **S22's event date is 2026-07-31 = today and its observable had not printed at the 09:1x KST re-check (DART: 475150 최근 2일 1건 = 07-30 [기재정정]타인에대한담보제공결정 only; 006120 SK디스커버리 지분변동 0건; domestic news 0 hits) ⇒ NOT scoreable, NOT `EXPIRED` — named here as the next run's #1 scoring job (the S28 precedent).** **S11 re-pulled and still PENDING (deadline 08-06)**: mt 2026-07-30 primary — the 8-holdco 간담회 was **cancelled**, deferral is *"8월 이후"* with a source calling it *"무기한 연기된 분위기"*, the 3연임 statutory ban is **still unconfirmed**, and a **new cause is named — the market crash pushed the package down the priority list.** ⇒ an `AMBIGUOUS` verdict at 08-06 is now the likely outcome and **the threshold will not be widened** |

### Scoring-log rows added 2026-08-02 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S22** | 2026-07-25 (industry_kr BET/ALPHA) | **2026-07-31** | ★★★ **FIRED-B — the carried kill fired** | **2026-08-02 HANDOVER (industry_kr)** | **Both counterparties filed the same amendment on the event date.** `[PRIMARY — DART]` **SK디스커버리 rcpNo 20260731801112**「[기재정정]타법인주식및출자증권처분결정」, 정정사유 ***"거래종결 예상일 변경에 따른 처분예정일자 변경"***, **처분예정일자 2026-07-31 → 2026-08-11**; **SK이터닉스 rcpNo 20260731801128**「[기재정정]투자판단 관련 주요경영사항」, 정정사유 ***"처분예정일 변경"***, same dates. ⇒ **the SPA did not close on 07-31, and this is the SECOND deferral** (06-30 filing had set 07-31). **Branch B, not C**: 처분주식수 **10,455,825주 (30.98%)** and 처분금액 **₩247,800,000,000** are **both unchanged** — only the date moved, so "terms revised" did not fire. ✅ **Registered price re-derived from the primary: 247,800,000,000 ÷ 10,455,825 = ₩23,700/share, matching the registration exactly (C1 — the handed-down number was re-measured).** ★ **New facts recorded but NOT used to score (L3)**: buyer is **Eclipse Holdco L.P.**, an SPV of a KKR-managed fund, 처분후 지분 **0%**; a **conditional earn-out of ₩22.1bn** tied to revenue/OP milestones sits **on top of** the ₩247.8bn base; **공정거래위원회 신고대상 미해당** ⇒ antitrust cannot be the cause of the delay; **풋옵션 없음**; 처분목적 *"포트폴리오 리밸런싱을 통한 재원 확보"*. ★★ **What this scoring says about the desk, and it is not flattering**: **S28 scored FIRED-A on 07-28** (both KKR nominees elected 99.4%/99.5%, an explicit 거래종결 정지조건) and its registration text said *"S22 branch A becomes materially more likely"* — **the condition precedent cleared and the closing slipped anyway.** Registered as **D109**. ★★ **And the news axis never saw it**: `search "SK이터닉스" --days 5 --scope domestic` → 1 irrelevant hit; `fts search 이터닉스`·`KKR`·`SK디스커버리 --days 7 --kr` → **0 mentions of the deferral across all three** ⇒ **two independent query forms agree, so this is genuine absence of coverage, not a query-vocabulary failure (the mirror image of R29)** — registered as **D110**. Price context, **not the score**: 475150 closed **45,450 (+8.73%)** against a **+24.174%** benchmark ⇒ residual **−3.46pp** on β 0.504 with an **own-residual σ of 10.37pp** ⇒ **inside its own noise; the tape did not price the deferral on the day** |
| **S46-KR** | 2026-07-31 (industry_kr MACRO) | **2026-07-31 close** | **FIRED-B** | **2026-08-02 HANDOVER (industry_kr)** | **Anti-signal checked first, and neither VOID condition fired as written**: `069500.KS` was **+24.174%** (the condition is ≤ −3.0%) and Brent `BZ=F` **+1.22%** (the condition is ±5%). ⇒ scoreable. **Observed, frozen method (β on the 60 sessions ending 07-30, `residual = excess − (β−1)×bench`)**: 096770 **−5.232%** vs bench **+24.174%** ⇒ excess **−29.41pp**, **residual −11.03pp on the frozen β 0.24** (β **re-measured by this run at +0.232, R² 0.063 — the registration reproduces**). **Threshold was ±3.8pp ⇒ B fired at 2.9× the band.** ★ **Robustness the registration did not require and this run did anyway**: sweeping β across **0 → 0.5** gives residuals **−5.23 → −17.3pp**, all below −3.8 ⇒ **the verdict is not decided by window choice (M253's failure mode avoided)**; and against the **`^KS200`** benchmark instead of the ETF the residual is **−9.87pp** ⇒ **not an artifact of M298's ETF premium either.** ⚠⚠ **Two honest caveats recorded WITHOUT moving the threshold**: (i) **D104 stands and cost something** — the anti-signal was written one-sided, so a **+24.17%** session is not a VOID condition even though it is the same "cannot separate the name from a market event" problem in the other direction (**successor rule staged as D111: write `|bench| ≥ x%`**); (ii) **the ±3.8pp band came from M260's σ measured on ordinary sessions**, and this session's own base rate is **mean −2.23pp, sd 3.73pp** (M299) ⇒ **recentred, the threshold should have been ≈ −6.03pp, which −11.03 still clears; and 096770's own estimation-window σ is 4.38pp, already wider than the band.** ★ **Control measured the same session and NOT merged into the verdict**: **010950 −0.78pp** (≈ +1.45pp *above* the session mean) · 068270 −6.96 · 475150 −3.46 ⇒ **096770 is the complex's own event, not a refining-node event** — ⚠ weak leg, because 010950's β is indistinguishable from zero (M253) |
| **S32** *(US-owned, scored by KR)* | 2026-07-27 (industry_US PREMORTEM) | 2026-07-28 COT → **2026-07-31 release** | **FIRED-B** | **2026-08-02 HANDOVER (industry_kr)** | ★ **Scored by the KR desk because the US desk has not run since 07-30 and the CFTC release published 07-31** — the spine's "a past-dated row in the other file is still this run's to score" rule, executed. **Feed freshness verified before scoring** (the 07-28 US run had caught a byte-identical stale snapshot and logged that the tool prints no `asof`): **7 of 8 instruments moved** vs the 07-21 read — S&P 84→**82**%ile · R2K 88→**57** · UST10Y 12→**13** with **−48,031 → +3,587** · WTI 11→**10** · NatGas 11→**3** · Copper 98→**96** ⇒ **the release is fresh and NDX holding at the 5th percentile is the observation, not staleness.** **Observed**: **NDX net-spec −9,914, 1-year percentile 5%** ⇒ **0 points of rise from the registered 5th, so branch A's ">15 points" leg fails and branch B's "<10th" leg is met**; **QQQ RS5 vs SPY = −0.55pp** (07-24→07-31: QQQ +0.55% · SPY +1.10%) ⇒ **≤ 0, branch B's second leg met.** **Invalidation (HY OAS ≥ 3.10% on a close) did not fire — 2.84% (FRED 07-30).** ⇒ **B: "positioning stayed crowded-short; the prints were settled on fundamentals"** ⇒ **S13 and S16 keep their fundamental basis.** ⚠ **The registration's constraint is carried forward intact and is NOT relaxed by this scoring**: *"COT crowded-long/short contrarian sits in this desk's REJECTED ledger (D6) and this bracket does NOT re-buy it — it may not be cited as a signal by any stage."* |
| — | — | — | ★ **Condition-check executed on every condition-settled row (second consecutive run)** | 2026-08-02 HANDOVER (industry_kr) | Every ARMED row was classified **date-settled vs condition-settled** and each condition-settled row was compared against today's data — the promotable form of the rule candidate that S29 defeated. **S43 and S44 both trigger on "the next `069500.KS` session ≤ −3.0%": measured 07-30 −2.00% · 07-31 +24.17% ⇒ the condition has NOT been met; both stay legitimately ARMED.** **S44's second leg checked separately: `DTWEXBGS` is still 120.71 asof 2026-07-24 — unprinted (next ~08-04)** ⇒ both legs pending. ⚠ **The prior run recorded 07-30 as −2.199% and the same series now returns −2.00%** (0.2pp, dividend-adjustment presumed, **unverified — C3**); **the ≤−3.0% verdict is identical either way.** **S11 re-pulled and still PENDING (deadline 08-06)**: primary **mt 2026-07-30「금융지주 지배구조 개선안 발표, 8월 이후로 또 밀려」** independently reproduces the prior run's finding ⇒ **an `AMBIGUOUS` verdict at 08-06 remains the likely outcome and the threshold will not be widened.** **S17 is in-window and NOT scored (settles 08-05)**, but its series was **independently rebuilt by this run and reproduces the prior run's values** (07-22 +33.64 vs +33.6 · 07-24 +29.53 vs +29.5 · 07-30 +62.56 vs +62.6); **the new in-window point 07-31 is +18.85% = branch C territory, the first non-B reading inside the window** — carried, not concluded. **`EXPIRED` = 0 · silent skips = 0.** |


### Scoring-log rows added 2026-08-03 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S47-KR** | 2026-07-31 (industry_kr MACRO) | **2026-08-03 10:00** | — **NOT SCOREABLE, NOT `EXPIRED`** | (polled 5× 2026-08-03) | ⛔⛔ **The observable is absent from the filing that landed, and the run ended before the one that carries it.** DART polled at **08:59 (0 실적) · 09:15 (0) · 09:29 (공정공시 게시 — ahead of its own registered 10:00) · 09:52 · 09:56**. **`rcpNo 20260803800274` 「연결재무제표기준영업(잠정)실적(공정공시)」 carries NO segment split and NO inventory-gain figure**; its own text points to *"첨부자료 또는 홈페이지 … 경영실적발표 자료"* and declares **「정보제공(예정) 2026년 8월 3일 10:00 · 2분기 실적발표 컨퍼런스 콜」**. ⇒ ★ **Branch C ("the company does not disclose an inventory-gain figure") was DELIBERATELY NOT scored early — the company had not finished disclosing, and an early `AMBIGUOUS` is observable fabrication in the other direction.** ★★ **Named as the 2026-08-04 run's #1 scoring job (the S28 precedent): read 「재고관련이익 ÷ 정유부문 영업이익」 from the IR pack or the 반기보고서, score A(≥50%) / B(<50%) / C(non-disclosure), and DO NOT substitute an estimate (D95).** ★ **What the 공정공시 DID give, recorded but not used to score**: 매출 **₩11,343,488m (+26.8% QoQ · +40.9% YoY)** · **영업이익 ₩965,015m (−21.6% QoQ · 흑자전환 YoY)** ⇒ **OPM 13.766% → 8.507% = −5.26pp** `[own calc]`, i.e. **the same "level high, rate turning" shape 096770 printed** (**C2 both halves quoted**). ⚠ Side facts, explicitly outside the observable: 한국투자증권's ₩1tn forecast vs the actual **₩965bn = −3.5% miss**; **the lubricants mechanism is common to both refiners** (yonhap 08-03: SK엔무브 2Q OP **₩691.9bn, +414.4% YoY**), and **theme `윤활기유` 🟡 82d / 2.14× / n=14** — **a mechanism corroboration may not substitute for the frozen ratio** |
| — | — | — | ★ **Condition-check executed on every condition-settled row (THIRD consecutive run)** | 2026-08-03 HANDOVER (industry_kr) | Every ARMED row was classified **date-settled vs condition-settled** and each condition-settled row compared against today's data. **S43 and S44 both trigger on "the next `069500.KS` session ≤ −3.0%": settled closes 07-27 +1.283 · 07-28 −11.190 · 07-29 −6.344 · 07-30 −2.199 · 07-31 +24.174 ⇒ the condition has NOT been met; both stay legitimately ARMED.** **S44's second leg checked separately: `DTWEXBGS` still 120.7105 asof 2026-07-24 — unprinted for 10 calendar days (next ~08-04)** ⇒ both legs pending. ★ **The 07-30 value discrepancy the prior run logged as `[unverified, C3]` is RESOLVED and it is a call convention, not a mystery**: `auto_adjust=False` gives **−2.199%**, the default `True` gives **−2.00%** — **the ≤−3.0% verdict is identical either way**, and the standing convention proposed is `auto_adjust=False` with the flag stated. **S11 re-pulled and still PENDING (deadline 08-06)**: `search "금융지주 지배구조" --days 5 --scope domestic` returns **exactly one article, the same mt 2026-07-30 「금융지주 지배구조 개선안 발표, 8월 이후로 또 밀려」** ⇒ **a third consecutive run reproducing the same finding; an `AMBIGUOUS` at 08-06 remains the likely outcome and the threshold will not be widened.** **S17 is in-window and NOT scored (settles 08-05)** — its series was **independently rebuilt a second time and reproduces to the decimal** (07-22 +33.64 · 07-24 +29.53 · 07-27 +14.83 · 07-30 +62.56 · **07-31 +18.85**), and the window now reads **B · B · C**; the series was also **extended backwards two sessions (07-20 +27.46 · 07-21 +38.13)**. **The 000660 flow suspension stays on.** **`EXPIRED` = 0 · silent skips = 0.** ⚠ **Note for S38 and S48-KR (both settle 2026-08-12)**: this run measured the **KOSPI200 front-month final trading day as 2026-08-13** — **one session after both brackets settle** — so an index-expiry roll sits directly against a stock-of-shorts observable. **Neither bracket is re-frozen; the fact is registered as D133 and must be recorded at scoring** |

### Scoring-log rows added 2026-08-03 by the `industry_US` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S43** *(KR-owned, scored by US)* | 2026-07-30 (industry_kr MACRO) | **event-conditional — TRIGGERED 2026-08-03** | ★★ **`VOID`** | **2026-08-03 HANDOVER (industry_US)** | ★★★ **The anti-signal was checked FIRST and it fired.** `[PRIMARY — DART]` **rcpNo 20260803800514**, filed **2026-08-03 by 셀트리온**: 「**투자판단관련주요경영사항** (CTP44(다잘렉스 바이오시밀러) 한국 임상 3상 시험계획…)」 — a company-specific material disclosure **landing on the trigger session itself**; 국민연금공단 `대량보유상황보고서(약식)` filed the same date. S43's registered anti-signal: *"a 068270-specific disclosure (trial data, an order, an equity raise) landing on that session ⇒ the low-beta axis and the news axis become inseparable ⇒ score `VOID` and re-register on a different session."* ⇒ **VOID.** ⚠ **The interpretive edge is stated rather than resolved in the desk's favour**: this is a trial *plan*, not results — but the governing phrase is *"a 068270-specific disclosure"* and the stated mechanism applies. **Narrowing an anti-signal after the print is the same violation as widening a threshold.** ★★ **The observable had been computed and would have scored the other way**: trigger `069500.KS` **−8.928%**; β on the 60 sessions ending 07-31, `residual = excess − (β−1)×bench` — **068270 −1.194pp** (β 0.136, R² 0.067) · 207940 −3.289 · 128940 +7.045 · 326030 +1.676 ⇒ **branch B on the frozen arithmetic. NOT recorded as a B**, because the anti-signal precedes the observable. ★★★ **S43-ANNEX's requirement executed anyway and it is the more useful output**: 068270's **own-window residual σ = 2.923pp** against a **±1.0pp band and a −1.194pp verdict = 0.41σ** ⇒ **the band sits entirely inside the estimator's own noise, exactly as the ANNEX predicted from a different cohort — D93 confirmed prospectively, and the second KR instance of L3-bis.** ⚠ **Beta sweep: the verdict flips sign inside the plausible range** (β 0.00 → −2.410 · **0.24 registration → −0.268** · 0.30 → **+0.268** · 0.50 → +2.054) ⇒ B holds at the frozen and measured β and **dies at β ≥ 0.27.** ⇒ **Even absent the anti-signal this bracket could not have carried a conclusion.** ★ Caught by the US desk because the `industry_kr` run of the same date ended at **08:59 KST, one minute before the KR open** — the condition was met at the **15:30 KST close, seven hours later.** **Not a KR-desk failure; the shared-spine rule working as designed.** |
| **S44** *(KR-owned, scored by US)* | 2026-07-30 (industry_kr MACRO) | **event-conditional — TRIGGERED 2026-08-03** | **FIRED-B** | **2026-08-03 HANDOVER (industry_US)** | **Leg 1, the frozen sign pair**: `069500.KS` **−8.928% ≤ −3.0%** ∧ **KRW=X 1,420.60 (07-31) → 1,428.08 (08-03) = +0.527% ⇒ the won WEAKENED** ⇒ **branch B: *"ordinary capital-flight shape ⇒ M-15 is retracted."*** ⇒ **R42 filed.** **Leg 2, reported separately and NOT used to score** (B does not require it): **`DTWEXBGS` still 120.7105 asof 2026-07-24 — unprinted for 10 calendar days**, a 4th consecutive run pending. ⚠⚠ **Three caveats recorded WITHOUT moving the threshold.** (i) **`KRW=X` is a 24-hour OTC quote, not a KRX-session close**, and the registration named no venue ⇒ **registration defect D138**. Direction corroborated by **DXY 99.800 → 99.783 (−0.02%, flat)** ⇒ the won weakened against a **stationary** dollar, which strengthens the read (it is not the dollar-side artifact branch C exists to catch). (ii) **n = 1 (S1)**, as the registration pre-stated; the +0.53% magnitude is not cited. (iii) ★★★ **found two stages later, at EVENT_ALPHA, and it is material**: **a *rare Japan-Korea joint FX intervention* occurred 2026-07-31** [straitstimes], so the won's 07-31 base (1,420.60, a −1.503% single-session strengthening) is **an intervened level** and part of the 08-03 weakening is intervention decay rather than capital flight. **The verdict is NOT changed — re-interpreting a pre-registered sign after the print is exactly what L3 forbids** — but it is **a registration defect of D138's family, logged as D142.** ★ Hand-forward to the KR desk: **the yen hit a 3-month high on 08-03 while the won weakened — the two currencies DIVERGED three sessions after a joint intervention.** |
| **S47-KR** *(KR-owned)* | 2026-07-31 (industry_kr MACRO) | 2026-08-03 10:00 | — **STILL NOT SCOREABLE, NOT `EXPIRED`** | (carried 2026-08-03, industry_US) | The 09:29 KST 공정공시 (`rcpNo 20260803800274`) carries **no segment split and no inventory-gain figure** — verified by the KR run at five separate clocks; the 10:00 KST IR pack is the carrier. **This US desk did not reach the IR pack, and per D95 an estimate is not admissible.** ⇒ **carried forward to the 2026-08-04 `industry_kr` run as its #1 job, exactly as that run designated it — named HERE so the hand-forward is visible in both files rather than living only in the KR run's own report.** |
| — | — | — | ★ **Condition-check executed on every condition-settled row — FIRST US execution, and it caught two rows on its first pass** | 2026-08-03 HANDOVER (industry_US) | Every ARMED row classified **date-settled vs condition-settled**. **S43 · S44 fired (above).** **S8** — undated `[blank]`, and **R30/D95 measured its own 60/84 kill lines un-scoreable on this data** ⇒ **carried as un-scoreable for a 2nd consecutive run and named as needing a human `VOID` or re-registration.** **S52** — condition-settled ≤48h class; **tracks branch C**: *"talks begin Monday"* is a date for **TALKS**, not the *"dated Strait-reopening term in a primary text"* branch A requires, and is an extension of the exact conditional S52 was registered on; branch B's named-infrastructure strike is absent. **The 07-27 run refused to score S8-A off a precondition and S52's registration says that refusal binds — it binds.** **S49 · S26 · S41 · S9 · S23** all re-pulled: **no new settled US bar exists**, so all are unchanged. **`EXPIRED` = 0 · silent skips = 0.** |

### Scoring-log rows added 2026-08-04 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S47-KR** | 2026-07-31 (industry_kr MACRO) | 2026-08-03 10:00 | ★★★ **FIRED-B** | **2026-08-04 HANDOVER (industry_kr)** | ★★ **The hand-forward worked: two prior runs named this "the next run's #1 scoring job" and it was scored on the first clock that could see the observable.** **Observed**: the frozen ratio 「재고관련이익 ÷ 정유부문 영업이익」 = **₩113.7bn ÷ ₩532.4bn = 21.36%** against a **≥50%** branch-A line ⇒ **B at 43% of the threshold.** `[PRIMARY-adjacent — the company's own 2Q conference call, yonhap 2026-08-03 11:09 종합2보 body: *"윤활 부문이 대부분을 차지한 2분기 재고 관련 이익은 1천137억원으로, 전 분기(6천434억원) 대비 크게 감소"* · *"정유 부문은 **정제마진 상승** 등의 영향으로 매출 9조293억원, 영업이익 5천324억원"*]` — the segment OP figure is carried by **3 outlets** (yonhap 종합2보 · mt 종합 · sedaily), the inventory figure by yonhap alone. ⚠⚠ **The true ratio is LOWER than 21.36%**: the company attributes most of that ₩113.7bn to the **lubricants** segment, so 21.36% is a **conservative upper bound** computed with the whole-company numerator. **Either way B, decisively.** ★ **Anti-signal checked FIRST and did not fire**: the registered VOID condition was a **재고자산평가손실** from a post-quarter crude collapse — what printed is a shrunken inventory *gain*, not a valuation *loss*. ⇒ **Meaning, exactly as branch B pre-stated: the 86% is SK-specific, M-19's generalisation is WITHDRAWN (R43), and the two refiners must be tracked on different KPIs.** ⇒ **Branch A's consequence did NOT happen: `정제마진` is NOT dropped as this node's KPI — the company itself attributed refining OP to it.** ★ **Side observations recorded, not scored**: **샤힌** is answered for the first time (mechanical-completion verification + pre-commissioning under way, **4Q startup → commercial operation early 2027, 2026 capex ₩2.1tn held, "no large 2027 investment planned"**) — the body EVENT_ALPHA could not obtain on 07-31; and **M-12's loss-compensation booking is still blank, but for the first time the reason comes from a primary speaker**: *"정산위원회가 보상 기준과 산정 방식을 마련하고 있는 단계라 구체적 보상 규모는 예측하기 어렵다."* ⚠ **Evidence grade stated: this is a conference-call figure carried by news bodies, NOT a DART filing** — the observable does not exist in the 공정공시 form. **The 1차 substitute is the 반기보고서 segment note (~2026-08-14) and re-confirmation there is scheduled** (the 08-03 staged rule candidate #1: when a filing exists for the same event, the filing decides the magnitude). |
| — | — | — | ★ **Condition-check executed on every condition-settled row — FOURTH consecutive run, and this time it came back EMPTY** | 2026-08-04 HANDOVER (industry_kr) | Every ARMED row was classified **date-settled vs condition-settled**. ⇒ **KR condition-settled rows remaining: ZERO.** S39 (FIRED-B), S43 (`VOID`), S44 (FIRED-B) closed the class. **This is recorded as a check performed with a null result, not as a skip** — the practice has caught a bracket on each of its first three runs (S39/S29 · S22 · S43+S44) and today there was nothing left to catch. **KR ARMED rows are now all date-settled**: S11 (08-06) · S17 (08-05) · S27 (~08 late) · S34 (10-31) · S38 (08-12) · S45 (09-30) · S48-KR (08-12) · S49-KR (10-30). **`SCENARIOS_US.md` was opened and checked for past-dated rows this desk owes a score: S49/S50/S51/S52/S53/S54 all settle 2026-08-05 or later ⇒ zero US rows due.** **S17 is in-window and NOT scored (settles 08-05); its anti-signal was re-checked at the primary — `module_disclosure 000660 --days 5` returns 2 filings, neither an issuer disclosure raising the 2.5% ceiling ⇒ the 000660 flow suspension stays on.** **S11 re-pulled, still PENDING (deadline 08-06); `AMBIGUOUS` remains the likely outcome and the threshold will not be widened.** ⚠ **New fact for S11's scoring, recorded now so it is not mistaken for a signal later: `지배구조` measures 🟡ACCELERATING 2.27× on n=1,025 today, but the S11-specific query still returns exactly ONE article (the same mt 2026-07-30 deferral piece) for a FOURTH consecutive run** ⇒ **the theme acceleration's denominator is almost certainly the 08-03 세제개편, not the FSC package. Do not read it as an S11 imminence signal (C3).** ⚠ **D133 restated for S38/S48-KR (both settle 08-12): the KOSPI200 front-month final trading day is 2026-08-13, measured again today from the board (`잔존일수 10 · futs_last_tr_date 20260813`). Neither bracket is re-frozen; the fact is recorded so it is stated at scoring.** **`EXPIRED` = 0 · silent skips = 0.** |
| **S50-KR · S51-KR** | **2026-08-04 (industry_kr MACRO / DEEP-ENRG)** | see `SCENARIOS_KR.md` | — | — | ARMED — **S50-KR** brackets the run's own largest instrument finding (the desk benchmark deviating from its index) **on its own anti-signal, and its threshold is taken from a measured spread rather than a round number** · **S51-KR** converts today's news-body scoring of S47-KR into a **primary-source re-confirmation** on the 반기보고서, i.e. it pre-commits the desk to checking its own evidence grade |

### Scoring-log rows added 2026-08-04 by the `industry_US` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S49** | 2026-07-30 (industry_US PREMORTEM Lens 2) | **event-conditional — TRIGGERED on the 2026-08-03 settled close** | ★★★ **FIRED-B** | **2026-08-04 MACRO §D (industry_US)** | ★★ **The 08-03 HANDOVER pre-named this as *"the bracket most likely to fire next… tonight's 08-03 close is the first bar that can settle it"* — and it fired. The first time this desk has pre-named the next bracket to fire and been right on the next session.** **Observed, frozen method (5-session change in the settled distillate crack HO×42 − WTI, yfinance DAILY settled bars, one source): 82.502 (08-03) − 90.077 (07-27) = −7.575 against a branch-B line of ≤ −5.0 ⇒ B, by 2.575 points.** ★ **D140's remedy EXECUTED rather than cited — the whole window was re-pulled, and the 07-31 value reproduced at the REVISED +2.158 (not the +1.066 an earlier pull carried), so the revision has settled.** ⚠⚠ **The MEANING is annexed, not scored — see `S49-ANNEX` (registered the same day) for five measured objections**, of which the two largest are: **(i) the crack LEVEL 82.502 sits at the 92.1st percentile of the trailing year (n=252, mean 51.15, sd 18.48), so *"the bottleneck is releasing"* describes a bottleneck tighter than 92% of the past year**; and **(ii) DEEP-ENRG measured the break to be a GASOLINE event — 5/21/63-session rates distillate −7.575/+17.540/+18.694 vs gasoline −12.875/−9.575/−4.797, with the distillate−gasoline spread WIDENING +5.300 to 38.241 on the firing session, and widening a further +10.4 points on the live 08-04 bar. A releasing distillate bottleneck COMPRESSES that spread.** ★ **On the D93 test S49 never ran, its threshold survives: the 5-session-change estimator measures mean +2.170 · σ 6.221 (trailing 60), so −5.0 sits at ≈ mean −1.15σ and fires in 6.7% of trailing-60 windows — NOT inside noise. Set by hand without measurement, and it got lucky.** ⚠⚠ **INVALIDATION — evaluated, and NOT resolved in the desk's favour.** S49's clause reads *"a Hormuz reopening statement ⇒ S8 owns that as a narrative event, not this."* **On 08-02/08-03 the feed carried Trump's *"Perimeters Of A Deal Reached With Iran To Reopen Hormuz"*, Iran's *"negotiations with Oman… in final stages"*, and bloomberg's *"Iran Says Strait of Hormuz Talks Are Underway"* — against aljazeera's *"Tehran DENIES it is in talks"* the same day.** **The fire is recorded because the nearest OPERATIONALISED standard — S52 branch A, written by this desk on 08-02 and checked as unmet by the 08-03 run — was not met.** ⇒ ★★★ **`D149` registered: an invalidation clause must carry the same evidentiary standard as the branches it can override. A human ruling that S49's eight-word clause means what its words say would make this `VOID`. The crack MEASUREMENT survives either ruling; only the score is at stake.** ★ **Free consistency check now armed and previously unstated: S54 branch A is the SAME physical event with the opposite sign (rail surcharge = revenue, airline fuel = cost). Measured on the settled 08-03 bar, S54 = +3.567pp on the branch-A side, with UAL +5.82% · ALK +5.82% · DAL +4.75% · LUV +4.67% vs SPY +1.42% — the day's biggest winners. ⇒ R44 filed against this run's own PREMORTEM line that said otherwise.** |
| — | — | — | ★ **Condition-check executed on every condition-settled row — SECOND US execution** | 2026-08-04 HANDOVER (industry_US) | Every ARMED row classified **date-settled vs condition-settled**. **S49 FIRED-B (above) and leaves the class.** **S8** — undated `[blank]`, un-scoreable on this data (R30/D95) — **carried for a 3rd consecutive run and named again**: ★ **S49-B has now delivered S8 branch A's *economics* without S8's *narrative trigger*, so the bracket is not merely unscoreable — its question has been answered by a different instrument. It should be formally `VOID`ed or re-registered by a human.** **S52** re-checked against the fresh foreign pool: **branch A evaluated and NOT fired** — Bessent, verbatim on CNBC, *"There is a chance we **may** have a deal today or tomorrow to open the strait… It would be freedom of movement"* is **a dated conditional about a DEAL, not a dated term for the OPENING**, and S52-A explicitly excludes *"a repeat of the 08-02 conditional wording"*; the counterparty **denies the talks exist** and WSJ reports the opening *"Uncertain After New Strike."* **Branch B (a strike on NAMED Iranian energy infrastructure, ≥2 outlets on one primary) is ABSENT** — the strikes in the feed are on third-party shipping. **Tracks C; window 08-06.** ⚠ **Recorded honestly: this is the second consecutive run in which this desk declines to fire a branch that runs against its own OW.** **S9** — `[FRED]` **DFII10 2.47 (07-31), up from 2.41 held flat for four prints ⇒ the buffer HALVED, 14bp → 8bp, and it is now the closest US kill line on the board.** **S23/S51** — derived **2s10s +0.47**, 27bp from S23's line and receding. **S26** HY **2.85** (25bp) · **S41** IG **0.79** (11bp) ⚠ `ig_oas` needed a retry after a **FRED 502**. **S44 leg 2** — ★★ **`DTWEXBGS` PRINTED after 11 calendar days and 4 pending runs: 120.7105 (07-24) → 119.7034 (07-31) = −0.83%. Recorded, NOT used to re-score** — branch B fired on leg 1 alone and a settled verdict is not reopened by a late-arriving leg. **S12 checked explicitly rather than assumed** (the print could look like it reopens it): **already scored FIRED-B / AMBIGUOUS on 2026-07-28. Closed, stays closed.** **`SCENARIOS_KR.md` opened: ZERO KR rows past-dated for this desk** — the 08-04 `industry_kr` run scored S47-KR itself and closed the KR condition-settled class. **`EXPIRED` = 0 · silent skips = 0.** |
| **S55 · S56 · S57 · S49-ANNEX · S50-ANNEX(2nd)** | **2026-08-04 (industry_US PREMORTEM Lens 2)** | see `SCENARIOS_US.md` | — | — | ARMED / notices — ★ **S55** is the row that decides what to do with S49-B (physical release vs whole-barrel de-risking, `HO% − CL%`), **and D93 executed BEFORE freezing CHANGED its design: the estimator's centre is +1.981, not 0, so a symmetric band would have been biased toward branch B by construction — the third independent reproduction of that bias** · **S56** is a dated, share-counted natural experiment on the desk's own **REJECTED** positioning rule (D6), **registered with its weakness in the text (n=32 overlapping windows, 35 post-IPO sessions, no unlock precedent)** · **S57** exists because **S36 closes 08-05 and leaves MATR UW− with no live falsifier** · **S49-ANNEX** records five measured objections to S49-B's meaning (**S49 NOT re-frozen; the FIRE stands**) · **S50-ANNEX 2nd entry** records that **AMD's straddle now COVERS its print for the first time (±8.2%, expiry 08-05)** and that **ANET's band drifted ±11.7% → ±10.7% in ONE session** (**S50 NOT re-frozen**) |

### Scoring-log row added 2026-08-05 by the `industry_US` desk (post-run scoring of an 08-04 print)

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S50** | 2026-07-31 (industry_US PREMORTEM Lens 2) | 2026-08-04 AMC → window 08-06 | ⚠ **`AMBIGUOUS`** — and it is a **registration** finding, not a market one | **2026-08-05 (industry_US, post-run)** | **The ANET leg scores cleanly and the AMD leg cannot be scored in the form it was frozen.** ★ **ANET** `[Reuters + company call, 4 outlets]`: Q2 revenue **$3.04bn (+40% y/y, +12% q/q)** vs $2.82–2.83bn consensus, adj EPS **$1.02** vs $0.88–0.89; **Q3 guide $3.3bn against a $2.94–2.95bn consensus** and adj EPS **$1.06–1.08** vs $0.91 — *"forecast third-quarter revenue **above** Wall Street estimates … betting on strong demand for its networking gear as companies expand their **AI infrastructure**"*, and **the outlook was raised for the second consecutive quarter.** ⇒ **branch B's ANET disjunct ("guides next-Q datacenter/cloud-titan revenue DOWN y/y") is decisively NOT met.** ⚠ **Evidence-grade note: no separate *cloud-titan* revenue line appears in any body read; the scoring is on the datacenter/AI direction, and Reuters records the opposite-signed nuance that ANET *"has been expanding beyond its core cloud customer base … to diversify"* — a mix shift, recorded, not scored.** ⛔ **AMD**: the print is strong — revenue **$11.54bn (+50% y/y)** vs $11.28bn expected, adj EPS **$1.66** vs $1.62, non-GAAP GM **56%**, **Data Center $6.7bn, +107% y/y, 58% of total (from 42% a year earlier)**, Q3 revenue guide **~$13bn ±$300m (+41% y/y, +13% q/q)** against a $12.52bn consensus. **But branch A's threshold is *"next-Q DATACENTER revenue guide ≥ prior-Q Y/Y GROWTH RATE"* (i.e. ≥ +107%), and AMD guides the segment SEQUENTIALLY and QUALITATIVELY: *"AMD expects strong double-digit SEQUENTIAL growth in both data center and embedded revenue."*** **No y/y datacenter guide exists, and it cannot be derived from the disclosed material without importing an out-of-sample Q3'25 segment figure — which D95 forbids.** ⇒ **branch A's AMD conjunct is UNSCOREABLE; branch B does not fire (a sequential-growth guide is not a y/y cut); branch C ("one up, one down") does not describe it either, because BOTH legs are up.** ⇒ **`AMBIGUOUS`, per L3: the observable printed but does not cleanly map to any branch.** ★★ **And the bracket's INSTINCT was right even though its instrument could not settle: the deceleration branch A was written to catch IS visible — total revenue growth guides from +50% y/y to +41% y/y, and the market sold a beat-and-raise (see the reaction test).** ⇒ **registration defect `D157`: a branch may not compare a Y/Y GROWTH RATE against a line the issuer gives SEQUENTIALLY and QUALITATIVELY. Same family as D46 (a bracket that cannot settle in the form it was written) and D149.** ★ **Reaction test, SEPARATE and LABELLED (the D28 fix), and NOT part of the verdict**: AMD's regular-session 08-04 close was **+7.00%** — but that is **PRE-print** (the release is AMC), so the band test is **not yet scoreable**; the after-hours move is reported at **−8%** [yahoo_finance body: *"then fell 8% after hours"*] and **">10%"** [CNBC video caption] — **two figures, both recorded (C2/C3), against the ±8.2% band pulled 2026-08-04 (expiry 08-05, D1).** **Score it on the 08-05 settled close.** ANET was **+3.04%** in the regular session and **"up 3 per cent after the bell"** [Reuters]. ⚠ **The registration's own rule binds symmetrically and is stated: *"scored on the stated guide, NOT the price reaction — a cut the tape buys still scores as a cut."* ⇒ a RAISE the tape SELLS still scores as a raise, and the −8% is not evidence about the guide.** |

### Scoring-log rows added 2026-08-05 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S17** | 2026-07-24 (industry_kr MACRO) | 2026-07-29 → **2026-08-05 = today** | — **NOT scoreable yet, NOT `EXPIRED`** · ★ **but branch B is already ELIMINATED** | (measured 2026-08-05 08:5x, industry_kr HANDOVER) | ⛔ **The window's last bar does not exist at this run's clock.** S17 froze *"the ADR-to-ordinary premium, measured on closes, 07-29 → 08-05"*; the 08-05 KR close prints at 15:30 KST and the 08-05 ADR close ~13.5h later. ⇒ **named as the 2026-08-06 run's #1 scoring job (the S22 / S47-KR precedent), not `EXPIRED`.** ★★ **What IS settled without the final bar: branch B (*"stays ≥25% through 08-05"*) is falsified.** This run rebuilt the series independently for the **third** time (`SKHY × 10 × KRW=X ÷ 000660.KS − 1`, `auto_adjust=False`) and it reproduces to the decimal (07-29 **+31.51** · 07-30 **+62.56** · 07-31 **+18.85** · 08-03 **+30.76** · 08-04 **+39.84**). **07-31 printed 18.85% < 25%** ⇒ B dead. ★★★ **And S17-ANNEX's required dual reading AGREES for the first time**: lagging the ADR leg one session so the two legs share an information timestamp gives 07-29 +35.02 · 07-30 +38.33 · **07-31 +23.21** · 08-03 +31.69 · 08-04 +29.28 — **also below 25% on the same day.** ⇒ **the third KR instance of L3-bis, and the first where the two readings CONVERGE**: the timestamp mismatch the ANNEX identified is real (it compresses the range from 14.8~62.6% to 23.2~38.3%, a 2.4× amplitude difference) **but it does not change a branch verdict here.** Branch **A (≤15%) was never touched in-window** on either reading (minima 18.85 / 23.21); the 14.83% reading is dated **07-27, before the window opened**, exactly as the ANNEX pre-stated. ⇒ **the only live branch is C (15–25%), whose registered meaning is "partial — re-register with a tighter band; do not read a partial move as resolution."** ★ **Anti-signal checked FIRST and did not fire**: `module_disclosure 000660 --days 7` returns 3 filings (07-29 연결영업(잠정)실적 공정공시 · 07-30 최대주주등소유주식변동신고서 · 07-31 최태원 임원소유상황보고) — **no issuer disclosure raising the 2.5% ADR ceiling** ⇒ **the 000660 flow suspension stays on, and a C landing is a reason to hold it longer, never to lift it (D1 / retracted R1).** ⚠ Corroborated independently by the domestic feed the same morning: 「월가 증권사들 "SK하이닉스 저평가"…**ADR 주가 급등세**」[2 articles / 2 outlets] — the news axis and the price axis agree, and both point **away** from branch A |
| **S11** | 2026-07-23 (`catalyst_calendar --days 10`) | 2026-07-29 | — **PENDING, deadline 2026-08-06 = tomorrow** | (re-pulled 2026-08-05) | **A FIFTH consecutive run reaching the same single primary** — `search "금융지주 지배구조" --days 5 --scope domestic` still returns exactly one article, mt 2026-07-30 「금융지주 지배구조 개선안 발표, 8월 이후로 또 밀려」. ⇒ **`AMBIGUOUS` at 08-06 remains the likely outcome and the threshold will not be widened.** ⚠ **The C3 warning the 08-04 run registered is restated because the divergence widened**: `지배구조` measures 🟡ACCELERATING **2.25× on n=1,024** (theme-age) and **2.27× on the bucket instrument**, while the S11-specific query returns **one** article — **the denominator of that acceleration is the 08-03 세제개편 (🟡 **14.6×**, doubled from 7.5× in one run), not the FSC package.** Do not read it as an S11 imminence signal |
| — | — | — | ★ **Condition-check executed on every condition-settled row — FIFTH consecutive run, SECOND consecutive empty result** | 2026-08-05 HANDOVER (industry_kr) | Every ARMED row classified date-settled vs condition-settled. **KR condition-settled rows remaining: ZERO** (S39 FIRED-B · S43 `VOID` · S44 FIRED-B closed the class on 08-04). **All KR ARMED rows are date-settled**: S11 (08-06) · S17 (**today**) · S27 (~late 08) · S34 (10-31) · S38 (08-12) · S45 (09-30) · S48-KR (08-12) · S49-KR (10-30) · S50-KR (→08-07) · S51-KR (→08-17) · **S52-KR (→08-19, registered today)**. **Recorded as a check performed with a null result, not a skip.** **`SCENARIOS_US.md` opened and checked: ZERO US rows past-dated for this desk** — the run clock 08:46 KST = **08-04 19:46 ET**, so the 08-04 US session had settled (and the 08-04 `industry_US` run scored S49 itself) while the **08-05 US session had not opened**; every US row dated 08-05 (S9 · S19 · S23 · S30 · S31 · S36 · S53 · PSX) is **today's, not past-dated**. ⚠ **One genuine cross-desk open item is named rather than dropped: `S8`** — undated `[blank]`, carried un-scoreable for **three** consecutive US runs, and the 08-04 US run wrote that S49-B has now delivered S8 branch A's economics without its narrative trigger ⇒ **it needs a human `VOID` or re-registration; the KR desk cannot rule on it (P5).** **`EXPIRED` = 0 · silent skips = 0.** |
| **S52-KR** | **2026-08-05 (industry_kr DEEP-HLTH)** | → **2026-08-19** | — | — | ARMED — ★★★ registered because **S43's `VOID` on 08-03 left this node with no falsifier at all**, and this run then found that **S29's own ignition session (07-30) carried the same 068270-specific-disclosure contamination that killed S43** — three consecutive weeks of such filings (07-24 · 07-30 · 08-03), never recorded. **S52-KR fixes both of S43's measured failure modes by construction**: every threshold is taken from a measured σ (**O1**: the larger of two measured 10-session log-change sds, **6.916pp**, giving 199,105 / 173,384 — cross-checked against the daily residual sd 2.832~2.983pp that reproduces S43's post-hoc 2.923pp; **O2**: a binomial null sd 3.391 that the **measured 20-session sd 3.35 confirms**, autocorrelation-inflated ×1.508, giving 28.14 / 25.06), **and the two observables are scored INDEPENDENTLY so that one contaminated leg cannot VOID the bracket** (AS-1 VOIDs O1 only). ⚠ AS-1's base rate is explicitly recorded as **high** rather than assumed away |


### Scoring-log rows added 2026-08-06 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S17** | 2026-07-24 (industry_kr MACRO) | 2026-07-29 → **2026-08-05 (창 종료)** | ⚠ **`AMBIGUOUS`** — 관측값 **+29.34%**, 동결 임계 **A ≤15 / B ≥25 유지 / C 15–25 착지** | **2026-08-06 HANDOVER (industry_kr)** | ★ **창의 마지막 봉이 양쪽 다 존재하는 첫 시계에서 채점했다**(런 08:19 KST = 08-05 19:19 ET ⇒ 08-05 KR 종가·ADR 종가 둘 다 정착). 동일일자 계열(4번째 독립 재구축, `SKHY×10×KRW=X÷000660.KS−1`, `auto_adjust=False`): 07-29 **+31.51** · 07-30 **+62.56** · 07-31 **+18.85** · 08-03 **+30.76** · 08-04 **+39.84** · **08-05 +29.34**. **A 미발화**(창 내 최저 18.85 > 15). **B 미발화**(07-31 이 25 를 깼다). **C 도 미발화 — 종료값 29.34% 는 15–25 밴드 밖이고 밴드 안 프린트는 07-31 하나뿐**이다. ⇒ **셋 중 어느 것도 깨끗이 발화하지 않으므로 `AMBIGUOUS`**, 그리고 **이것은 시장이 아니라 등록에 대한 발견이다(D173)**: A·B 는 **경로조건**, C 는 **종점조건**이라 **밴드에 들어갔다 나오는 계열은 셋 다 만족하지 않는다.** ⚠ 08-05 런의 *"유일한 생존 분기는 C"* 는 **소거법**이었고 C 의 문자 조건은 오늘 충족되지 않았다 — L3 는 사후에 더 합리적인 임계로 비교하는 것을 금하므로 **소거법으로 C 를 발화시키지 않았다.** ★ **다만 두 읽기의 처방은 같다**: C 의 등록된 의미(*"부분적 — 더 좁은 밴드로 재등록"*)와 `AMBIGUOUS` 가 동일하게 **000660 유동 판독 정지 유지**를 낸다. ★★★ **그리고 S17-ANNEX 의 이중읽기가 규약 의존임이 드러났다(R48)**: ANNEX 는 *"ADR 다리를 한 세션 지연"* 만 규정하고 **환율 다리의 타임스탬프를 쓰지 않았다.** ADR지연+FX당일(08-05 런의 구현) → 07-31 **+23.21**(B 깨짐); ADR지연+**FX 동반지연**(이번 런) → 07-31 **+25.09**(B **0.09pp 차로 유지**). ⇒ **08-05 런의 *"두 읽기가 처음으로 수렴한다"* 는 문장을 철회한다(R48).** 동결 관측값(동일일자)의 판정은 영향 없다. **D174 등록**: 두 시장 종가로 스프레드를 동결할 때 지연 규약은 **가격 다리와 환율 다리 둘 다** 명시한다. ★ **안티시그널 먼저 확인, 미발화**: `module_disclosure 000660 --days 9` = 5건(08-05 SK스퀘어 대량보유 · 07-31 최태원 임원소유 · 실적 1 · 기타 2) — **발행사의 2.5% ADR 한도 상향 공시 없음** ⇒ **정지 유지(D1 / 철회된 R1: A 만이 정지를 풀 수 있다)** |
| **S11** | 2026-07-23 (`catalyst_calendar --days 10`) | 2026-07-29 → **마감 2026-08-06 = 오늘** | **`FIRED-B`** — 관측값 **"발표 연기(간담회 잠정취소 · 8월 이후 · 무기한 연기 분위기) · 3연임 법적금지 최종 미확정"**, 동결 임계 **A 원안대로 입법 / B 권고수준 완화 ∨ 지연 / C 철회** | **2026-08-06 HANDOVER (industry_kr)** | ★★★ **6런 만에 처음으로 새 1차 자료가 나왔고, 그것이 나온 이유는 세계가 아니라 질의형이었다.** 등록 질의 `search "금융지주 지배구조" --days 5 --scope domestic` 는 오늘도 **1건**(mt 07-30)인데, **같은 코퍼스에 `fts search "3연임" --days 10 --kr`(본문 trigram 색인)를 걸면 11건**이고 그중 **mt 2026-08-05 「[광화문]3연임 금지가 금융지배구조 선진화? 번지수 틀렸다」** 는 제목이 「금융**지배구조**」라 **등록 질의로는 영원히 못 닿는다.** **M406**: 제목+요약 LIKE **1건** vs 본문 FTS **11건**, 동일 코퍼스·동일 창 ⇒ **R29(테마축)·R25(`capex cut`)의 세 번째 재현 — 도구가 아니라 질의가 틀렸다.** **본문(mt 07-30, 1,303자)**: 금융위 간담회 **잠정 취소**(8대 지주 회장 소집 예정이었으나 무산), 관계자 *"무기한 연기된 분위기… 상당 기간 못 나올 가능성"*, 개선안은 청와대·정무위에 **보고된 상태이나 3연임 법적 금지안은 최종 미확정**, 이억원 위원장 07-29 정무위 답변 *"조만간 내놓겠다"* 면서 **연임 횟수 제한 미확정**. **지연 사유로 명시된 것: 여당 내 반대 · 증시 폭락으로 우선순위 밀림 · 당국–청와대 이견.** ⚠ **등록 문구의 「위헌 심판이 지연시킨다」는 본문에 없다** ⇒ **D175**: B 가 결과(지연)에 메커니즘(위헌 심판)을 묶어 놨고 지연은 다른 메커니즘으로 왔다. **승격형: 분기는 관측값으로만 쓰고 메커니즘은 「의미」 칸에만 적는다.** ★★ **그리고 B 의 등록된 의미가 지금 상황을 과소서술한다 — 여기가 이 채점의 알파다**: mt 08-05 칼럼이 *"개선안에 결국 **3연임 금지를 포함시키기로 가닥**을 잡았다. 금융당국은 **주주총회 의결 기준을 대폭 강화하는 선에서** 대책을 마련했지만 **청와대가 3연임 금지를 밀어붙인 것**으로 알려졌다"* 고 적는다 ⇒ **일정은 B 로, 내용은 A 쪽으로 갈렸다.** ⚠ **증거등급 정직하게**: 단일매체·칼럼·"알려졌다" ⇒ `[news — 단일매체·칼럼·무출처]`, **방향만이고 분기 판정의 근거로 쓰지 않았다.** ⇒ **후속 브래킷 `S53-KR` 등록**(내용 다리, →2026-10-31). ★ **독립 확인**: `지배구조` 버킷 배율 **2.27× → 0.28×** 로 붕괴한 반면 `세제개편` 은 **3.52× 유지** ⇒ **08-05 런이 등록한 경고(*"지배구조 가속의 분모는 세제개편이지 FSC 패키지가 아니다"*)가 두 축의 분리로 확증됐다(M411).** ⚠ **D162 확정**: 316140 우리금융의 부활조건 다리 2 는 **S11 branch C(철회)** 를 AND 참조하는데 **B 가 발화한 이상 C 는 영원히 발화할 수 없다.** 다리 1(외국인 20d 순매수 부호 반전)은 08-05 런에서 **+104.9만주로 이미 충족** ⇒ **다리 1 충족 · 다리 2 도달불가 ⇒ AND 영구 미충족. 다음 런이 `resolve` 로 닫아야 할 1순위** |
| — | — | — | ★ **조건정산형(condition-settled) 행 점검 — 6번째 연속 실행, 3번째 연속 공집합** | 2026-08-06 HANDOVER (industry_kr) | 모든 ARMED 행을 날짜정산형/조건정산형으로 분류. **KR 조건정산형 잔여 ZERO**(S39 FIRED-B · S43 `VOID` · S44 FIRED-B 가 07-30~08-03 에 클래스를 닫았다). **수행했고 결과가 null 인 점검**으로 기록 — 생략이 아니다. **`SCENARIOS_US.md` 열었다**: 런 시계 08-06 08:19 KST = **08-05 19:19 ET** 라 08-05 US 세션이 마감됐고 **08-05자 US 행(S9·S19·S23·S30·S31·S36·S53·PSX)은 오늘부로 날짜가 지났다.** ⚠ **이 런은 그중 어느 것도 채점하지 않았고 숨기지 않는다** — 사유: (i) 08-05 `industry_US` 런이 이미 돌아 S50 을 사후 채점했고 그 행들을 자기 창으로 들고 있다, (ii) **KR 데스크는 이 시계에 US 데이터 축(FRED·COT·FINRA)을 갖고 있지 않다** ⇒ **08-06 `industry_US` 런의 몫으로 명시 인계.** ★ **S8** (무날짜 `[blank]`)은 **여전히 열린 크로스데스크 항목**이고 **사람이 `VOID` 하거나 재등록해야 한다 — KR 데스크는 판정할 수 없다(P5).** **`EXPIRED` = 0 · 조용한 생략 = 0.** |
| **S53-KR** | **2026-08-06 (industry_kr HANDOVER)** | → **2026-10-31** | — | — | ARMED — ★★ **S11 의 내용 다리 후속.** S11 은 *일정* 을 물었고 `FIRED-B` 로 닫혔다. **내용(3연임 법적금지가 최종안에 들어가는가)은 아직 관측되지 않았고, FIN 섹터 전체를 동시에 때리는 축은 그쪽이다.** 전문은 `SCENARIOS_KR.md`. **D173 적용 — 세 분기 전부 종점조건**(발표 시점의 조항 형태), 경로조건 없음. **D175 적용 — 분기 문구에 메커니즘(청와대/여당) 이름을 넣지 않았다.** |
| **S54-KR** | **2026-08-06 (industry_kr MACRO §I)** | → **2026-09-30** | — | — | ARMED — ★★ **C10(*"재생에너지 = 유가연동인가"*)을 교란 없는 세션에서 정산한다.** 오늘 두 번째 관측이 나왔는데 **부호가 반대**다: 07-27 은 크루드 붕괴 → KR 재생에너지 4종 −12.7~−29.4%; 오늘 창은 브렌트 5일 **−12.54%** → 475150 초과 **+16.40pp** · 010060 **+28.22pp**(둘 다 벤치 `069500.KS`). **두 관측 다 교란요인이 있어 표본으로 못 쓴다** ⇒ 트리거 세션을 사전에 정의하고 σ 를 그 자리에서 산출한다. 전문은 `SCENARIOS_KR.md`. **DEEP-MATR 이 교란 크기를 쟀다: 관세 2세션 기여 +2.18pp = 010060 20일 초과 +40.00pp 의 ~5%** ⇒ **교란은 있지만 20일 움직임을 설명하지 못한다.** |

---

**Scoring rule**: a scenario is scored at its next HANDOVER after the event date, whether or not
anyone remembers to look. An `EXPIRED` row is a process failure and is logged as one — an unscored
scenario is how a desk keeps its wins and forgets its losses.

---


---

## ★ MASTER INDEX — every registered bracket, its owner desk, and its file

> **Added 2026-07-29 when this file was split by market.** ⚠ **Ownership is the REGISTERING desk,
> not the subject market** — **S5** is about Korean exports and is US-owned; **S8** was registered
> by US and **scored by KR**; **S33** was registered by KR and **scored by US**.
> ⇒ **A desk may not skip the other file when it has a row to score there.** This index exists so
> that "which brackets exist" is answerable from the spine alone, at ~2 KB instead of ~137 KB.

| ID | Owner | File | Bracket |
|---|---|---|---|
| **S1** | US | `SCENARIOS_US.md` | S1 — Alphabet Q2 print |
| **S52-KR** | KR | `SCENARIOS_KR.md` | S52-KR — Is the pharma OW a sector or a one-name proposition (→2026-08-19) |
| **S2** | US | `SCENARIOS_US.md` | S2 — The 2026-07-29 cluster |
| **S3** | US | `SCENARIOS_US.md` | S3 — 4Q26 DRAM contract guidance |
| **S4** | US | `SCENARIOS_US.md` | S4 — Micron FQ4 print + FQ1'27 guide |
| **S5** | US | `SCENARIOS_US.md` | S5 — KR semiconductor exports, 1–10 August |
| **S6** | US | `SCENARIOS_US.md` | S6 — Intel FQ2 print |
| **S7** | US | `SCENARIOS_US.md` | S7 — RTX + LMT |
| **S8** | US | `SCENARIOS_US.md` | S8 — Hormuz "Strait open" / oil de-escalation |
| **S9** | US | `SCENARIOS_US.md` | S9 — The DOVISH real-rate branch |
| **S10** | KR | `SCENARIOS_KR.md` | S10 — USTR Section 301 "forced-labor tariff" on Korea |
| **S11** | KR | `SCENARIOS_KR.md` | S11 — Financial holding company governance reform |
| **S12** | US | `SCENARIOS_US.md` | S12 — ECB rate decision |
| **S13** | US | `SCENARIOS_US.md` | S13 — ★ MSFT + META capex, and the branch nothing in the book brackets |
| **S14** | US | `SCENARIOS_US.md` | S14 — Mastercard Q2 |
| **S14-ANNEX** | US | `SCENARIOS_US.md` | S14-ANNEX — ★ pre-registered contamination notice (NOT a rewrite of S14) |
| **S14-num** | US | `SCENARIOS_US.md` | S14-num — Mastercard Q2 |
| **S15** | US | `SCENARIOS_US.md` | S15 — June PCE |
| **S16** | US | `SCENARIOS_US.md` | S16 — Meta Q2 |
| **S17** | KR | `SCENARIOS_KR.md` | S17 — ★ SK hynix ADR–ordinary premium |
| **S18** | KR | `SCENARIOS_KR.md` | S18 — KT regulatory sanction hearing |
| **S19** | US | `SCENARIOS_US.md` | S19 — ★★ FOMC 2026-07-29 |
| **S20** | US | `SCENARIOS_US.md` | S20 — UPS Q2 |
| **S20-ANNEX** | US | `SCENARIOS_US.md` | S20-ANNEX — UPS Q2 |
| **S21** | US | `SCENARIOS_US.md` | S21 — STNG Q2 |
| **S22** | KR | `SCENARIOS_KR.md` | S22 — SK이터닉스 KKR SPA closing |
| **S23** | US | `SCENARIOS_US.md` | S23 — ★ FOMC 2026-07-29 |
| **S24** | US | `SCENARIOS_US.md` | S24 — ★ MSFT/META/AMZN capex 2026-07-29→31 |
| **S25** | US | `SCENARIOS_US.md` | S25 — ★ RE OW− |
| **S26** | US | `SCENARIOS_US.md` | S26 — ★★ The credit escape hatch |
| **S27** | KR | `SCENARIOS_KR.md` | S27 — ★★ Korea's 9th 석유제품 최고가격 designation |
| **S28** | KR | `SCENARIOS_KR.md` | S28 — ★ SK이터닉스 임시주총 |
| **S29** | KR | `SCENARIOS_KR.md` | S29 — 셀트리온: which branch is live |
| **S30** | US | `SCENARIOS_US.md` | S30 — ★ The SUPPLIER leg's 20-day reversal |
| **S31** | US | `SCENARIOS_US.md` | S31 — ★ Is the book's Energy epicenter the business or the war premium? |
| **S32** | US | `SCENARIOS_US.md` | S32 — ★★ The positioning branch nothing brackets |
| **S33** | KR | `SCENARIOS_KR.md` | S33 — ★ KR refiners on the first session that knows the crack held |
| **S33-ANNEX** | KR | `SCENARIOS_KR.md` | S33-ANNEX — ★★ beta-contamination notice (**S33 is NOT re-frozen**) |
| **S34** | KR | `SCENARIOS_KR.md` | S34 — ★★★ CXMT's capacity ramp: the supply-side falsifier the regime call n… |
| **S35** | US | `SCENARIOS_US.md` | S35 — ★★ The regulated-Utilities print cluster |
| **S36** | US | `SCENARIOS_US.md` | S36 — ★★ Materials: the A-grade price and the sweep's breadth disagree |
| **S37** | US | `SCENARIOS_US.md` | S37 — ★★★ The CXMT branch in which a funded entrant is BULLISH for the incu… |
| **S38** | KR | `SCENARIOS_KR.md` | S38 — ★ 006360 GS건설: accumulation against the largest crowded short this de… |
| **S39** | KR | `SCENARIOS_KR.md` | S39 — ★★ The pharma shelter property: a second observation, beta-adjusted a… |
| **S40** | US | `SCENARIOS_US.md` | S40 — ★★★ A capex GUIDE is not a capex MEASUREMENT when a gigawatt arrives … |
| **S41** | US | `SCENARIOS_US.md` | S41 — ★★ The AI-issuer credit channel S26 explicitly excluded |
| **S42** | US | `SCENARIOS_US.md` | S42 — ★★ This run's own new verdict, bracketed against itself |
| **S43** | KR | `SCENARIOS_KR.md` | S43 — ★★ Is the shelter property a NAME or a SECTOR? (S39's successor) |
| **S43-ANNEX** | KR | `SCENARIOS_KR.md` | S43-ANNEX — ★★ estimator-error notice (**S43 is NOT re-frozen**) |
| **S44** | KR | `SCENARIOS_KR.md` | S44 — ★★ Who sold? The crash's agent, read off the KRW sign |
| **S46** | US | `SCENARIOS_US.md` | S46 — ★★ AAPL: a ledger revival, hours before a binary the calendar did n… |
| **S47** | US | `SCENARIOS_US.md` | S47 — ★★★ The Utilities SPREAD: the object neither S35 nor S24 contains |
| **S48** | US | `SCENARIOS_US.md` | S48 — ★★ The optical / interconnect layer, which no bracket has ever cove… |
| **S49** | US | `SCENARIOS_US.md` | S49 — ★★★ S8's successor: a crack observable that survives its own data |
| **S50** | US | `SCENARIOS_US.md` | S50 — ★★ AMD/ANET 08-04 AI-capex-guidance read (asymmetric; only the CUT branch changes a conclusion) |
| **S51** | US | `SCENARIOS_US.md` | S51 — ★★ NFP 08-07 FIN OW− flattener risk (2s10s ≤ +0.20 breaks the NIM mechanism) |
| **S45** | KR | `SCENARIOS_KR.md` | S45 — ★★ The FSC governance package's announced clause form (S11's successor) |
| **S17-ANNEX** | KR | `SCENARIOS_KR.md` | S17-ANNEX — ★★ leg-timing notice (**S17 is NOT re-frozen**) |
| **S46-KR** | KR | `SCENARIOS_KR.md` | S46-KR — ★★★ the first session that knows SK이노's profit was lubricants, not crack |
| **S47-KR** | KR | `SCENARIOS_KR.md` | S47-KR — ★★ Does S-Oil reproduce the "86% inventory gain" refining split? |
| **S48-KR** | KR | `SCENARIOS_KR.md` | S48-KR — ★★★ S38's bigger twin: a 4.0%-float crowded short against the sheet's largest measured accumulation, on the SAME settlement date |
| **S49-KR** | KR | `SCENARIOS_KR.md` | S49-KR — ★★ 롯데렌탈: the control-transfer the theme axis could not see, on the issuer's own re-disclosure deadline |
| **S52** | US | `SCENARIOS_US.md` | S52 — ★★★ Iran: a DATED Strait reopening vs resumed strikes on Iranian ENERGY INFRASTRUCTURE |
| **S53** | US | `SCENARIOS_US.md` | S53 — ★★ MPC (08-04) + PSX (08-05): the equity-EXECUTION leg S49 cannot see |
| **S35-ANNEX** | US | `SCENARIOS_US.md` | S35-ANNEX — ★★★ basket-contamination notice: D is a merger-arb security (NEE/D DEFM14A 07-28) — **S35 and S47 are NOT re-frozen** |
| **S54** | US | `SCENARIOS_US.md` | S54 — ★★★ The beneficiaries of S52 branch A, whom S52's own exposure map omits |
| **S50-ANNEX** | US | `SCENARIOS_US.md` | S50-ANNEX — ★★ implied-move availability notice (**S50 is NOT re-frozen**) |
| **S50-KR** | KR | `SCENARIOS_KR.md` | S50-KR — ★★★ Is the desk's own benchmark tracking its index? (`069500.KS` vs `^KS11`) |
| **S51-KR** | KR | `SCENARIOS_KR.md` | S51-KR — ★★ S47-KR's primary-source re-confirmation on the 반기보고서 (evidence-grade pre-commitment) |
| **S55** | US | `SCENARIOS_US.md` | S55 — ★★★ Is the crack release PHYSICAL or WAR-PREMIUM? The leg discrimination S49 cannot perform (HO% − CL%, → 08-11) |
| **S56** | US | `SCENARIOS_US.md` | S56 — ★★★ SPCX 08-06 unlock: counted supply vs counted positioning, on the desk's own REJECTED rule (D6) |
| **S57** | US | `SCENARIOS_US.md` | S57 — ★★ Materials UW− has NO live falsifier after 2026-08-05 (S36 closes; the DTWEXBGS row is dormant by construction) |
| **S49-ANNEX** | US | `SCENARIOS_US.md` | S49-ANNEX — ★★★ five measured objections to S49-B's MEANING (**S49 is NOT re-frozen; the FIRE stands**) |
| **S50-ANNEX (2nd)** | US | `SCENARIOS_US.md` | S50-ANNEX 2nd entry — ★★ AMD's straddle now COVERS its print for the first time (**S50 is NOT re-frozen**) |
| **S58** | US | `SCENARIOS_US.md` | S58 — ★★★ MET 2026-08-06 print: a binary entered without a bracket, registered after the fact (→ 2026-08-11) |
| **S59** | US | `SCENARIOS_US.md` | S59 — ★★ NDAQ: the slope-transmission mechanism DEEP-FIN named but never registered an observable for (→ 2026-08-12) |
| **S60** | US | `SCENARIOS_US.md` | S60 — ★★ the XLE sale's falsifier, standing in for the fact that this desk has NO ledger that scores an exit (D159) (→ 2026-08-11) |
| **S61** | US | `SCENARIOS_US.md` | S61 — ★★ The Red Sea / tanker war-risk premium: the leg the Iran-scoped brackets cannot reach (STNG+FRO vs SPY, → 2026-08-12) |
| **S62** | US | `SCENARIOS_US.md` | S62 — ★★★ Are INDU OW− and UTIL UW one bet wearing two GICS labels? The correlated-tilt falsifier ({EMR,ETN,AME,PWR} median RS20 − XLU RS20, → 2026-08-07) |

**Count: 78 brackets — 54 US-owned · 24 KR-owned.**
⚠⚠ **S61 · S62 registered 2026-08-05 by the `industry_US` PREMORTEM (Lens 2).** IDs checked at
**WRITE time** (D137 / D76 / M319) against every row in **all three** SCENARIOS files **and** both
STANDING_VIEW files **and** RESEARCH.md: `grep` for `S61`/`S62` returned **0 registrations in all
seven**; highest existing was **S60 (US) / S52-KR (KR)**.
⚠ **S58 · S59 · S60 were registered 2026-08-05 by the human-execution loop directly into
`SCENARIOS_US.md` and were MISSING from this index until now** — added here by the 08-05
`industry_US` PREMORTEM. ★ **An index that does not contain a registered bracket is exactly the
failure this index was created to prevent**; the omission is recorded rather than silently repaired.
⚠ Those three rows are written in **Korean inside the English-pure US file** — a human call, named
once and not changed by a pipeline stage.
⚠⚠ **S55 · S56 · S57 · S49-ANNEX · S50-ANNEX(2nd) registered 2026-08-04 by the `industry_US`
PREMORTEM (Lens 2).** IDs checked at **WRITE time** (D137 / M319) against EVERY row in **all three**
SCENARIOS files **and** both STANDING_VIEW files **and** RESEARCH.md: `grep` for `S55`/`S56`/`S57`
returned **0 registrations in all seven files**; highest existing was **S54 (US) / S51-KR (KR)**.
⚠ **`S55` returns exactly ONE textual hit — prose inside the 08-03 collision note** (*"grep for
S54/S55/S50-ANNEX returned 0"*) — **checked and confirmed not to be a registration, rather than
assumed.** **The shared-counter proposal for a human now stands for a TWELFTH run.**
★ **And this run ran D137's three-grep check as written** — highest `M###` **355**, highest `D###`
**148**, highest `R##` **43** — before assigning **M356–M370 · D149–D154 · R44**.
⚠⚠ **S50-KR · S51-KR registered 2026-08-04 by the `industry_kr` run.** IDs checked at **WRITE time**
(**D137**'s measured requirement, per-counter) against EVERY row in **all three** SCENARIOS files **and**
both STANDING_VIEW files **and** RESEARCH.md: `grep` for `S50-KR`/`S51-KR` returned **0 in all seven
files**; highest existing was **S54 (US) / S49-KR (KR)**. The **`-KR` suffix is mandatory here** — S50
and S51 are already US-owned (registered 2026-07-31). **The shared-counter proposal for a human now
stands for an ELEVENTH run.** ★ **And this run ran D137's three-grep check as written** — highest
`M###` **343**, highest `D###` **142**, highest `R##` **42** — before assigning M344–M355 · D143–D148 · R43.
⚠⚠ **S54 · S50-ANNEX registered 2026-08-03 by the `industry_US` PREMORTEM.** IDs checked at **WRITE
time**, not read time (**M319**'s measured requirement) against EVERY row in BOTH files: `grep` for
`S54`/`S55`/`S50-ANNEX` returned **0 in all three files**; highest existing was **S53 (US) / S49-KR
(KR)**. **The shared-counter proposal for a human now stands for a TENTH run.**
⚠⚠ **S52 · S53 registered 2026-08-02 by the `industry_US` PREMORTEM (Lens 2).** IDs checked against
every existing row in BOTH files (**D76**); highest existing was **S51 (US)** and **S49-KR (KR)** —
**no collision.** ★ **And this run observed the collision hazard live for the first time: the
`industry_kr` desk registered S48-KR/S49-KR into THIS FILE while the US run was mid-stage**, so the
US run's first read of the master index (61 brackets) was already stale by the time it wrote. **The
append-only discipline held and nothing was clobbered — but "check IDs at write time, not at read
time" is now a MEASURED requirement rather than a precaution.** **The shared-counter proposal for a
human now stands for a NINTH run, and it is the second same-day concurrent-write instance
(cf. the 2026-06-30 `industry_US` double-run).**
⚠ **S48-KR · S49-KR registered 2026-08-02 by the `industry_kr` BET/ALPHA stages.** IDs checked
against every existing row in BOTH files (**D76** collision class); highest existing was **S51 (US)**
and **S47-KR (KR)**. **The shared-counter proposal for a human now stands for an eighth run.**
⚠ **S50 · S51 registered 2026-07-31 by the `industry_US` PREMORTEM.** IDs checked against every existing
row in BOTH files (**D76** collision class); highest existing ID was S49 (US) / S47-KR (KR). **The
shared-counter proposal for a human now stands for a seventh run.**
⚠ **S46-KR · S47-KR are suffixed `-KR` deliberately: `S46`–`S49` were already taken by the
2026-07-30 `industry_US` PREMORTEM.** The **D76** ID-collision class was checked against every
existing row in BOTH files before writing. **The shared-counter proposal for a human now stands for a
sixth run** — and this run is the first that had to *work around* the collision rather than merely
report it.
⚠ **S46–S49 registered 2026-07-30 by the `industry_US` PREMORTEM.** IDs were checked against EVERY existing row in BOTH files before writing (the **D76** collision class); the highest existing ID was S45, taken by the `industry_kr` run the same morning. **The shared-counter proposal for a human now stands for a fifth run.**
⚠ **The master scoring log above stays SHARED and un-split** — an `EXPIRED` row is a process
failure in whichever market it sits, and splitting the log would hide half of them from each desk.

| **S58 · S59 · S60** | **2026-08-05 (human-execution loop, 파이프라인 스테이지 아님)** | see `SCENARIOS_US.md` | — | — | ARMED — ★ **2026-08-04 KIS 실계좌 집행 4건을 사후에 채점 가능하게 만든 행들이다.** **S58(MET)** 은 **브래킷 없는 바이너리에 단방향 진입한 규칙 위반의 기록**이고(MET 는 08-05 장마감후 프린트였다), **S59(NDAQ)** 는 **DEEP-FIN 이 회귀로 지목했으나 관측치를 등록하지 않은 메커니즘**에 벤치를 XLF 로 두어 시장베타를 뺀 검정이며, **S60(XLE 매도)** 은 **이 데스크에 매도를 채점할 원장이 없다는 사실의 대리물**이다(**D159**). ⚠ **세 밴드 모두 trailing-252 실측 분위수에서 뽑았고(D93), 세 추정량 모두 중심이 0 이 아니어서 그 편향을 등록 시점에 밝혔다** — MET +0.130 · NDAQ−XLF −0.159 · XLE−SPY +0.332 |
| **S58** | US | `SCENARIOS_US.md` | S58 — ★★★ MET 08-06 프린트: 브래킷 없이 들어간 바이너리를 사후 등록 (실집행 채점) |
| **S59** | US | `SCENARIOS_US.md` | S59 — ★★ NDAQ: DEEP-FIN 이 회귀로 지목했으나 관측치가 없던 메커니즘 (벤치 XLF) |
| **S60** | US | `SCENARIOS_US.md` | S60 — ★★ XLE 매도의 반증조건 — 집행 채점 원장 부재(D159)의 대리물 |

| **S63** | US | `SCENARIOS_US.md` | S63 — ★★★ Are UW Utilities + UW Real Estate + OW Financials ONE duration bet wearing three GICS labels? (DUR composite, CPI 08-12 → 08-13) |
| **S64** | US | `SCENARIOS_US.md` | S64 — ★★ Do N+ Energy and OW− Industrials take the SAME crude tick in opposite directions? (XLI forward-6-session excess vs SPY, → 08-13) |
| **S65** | US | `SCENARIOS_US.md` | S65 — ★★★ FIN's OW promotion tested on the axis it was made on — median RS20 {JPM,BAC,WFC,BRK-B} vs SPY (NFP 08-07 → 08-11) |

## Scored by the 2026-08-06 `industry_US` run (appended to the MASTER scoring log — the log stays shared and un-split)

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S30** | 2026-07-27 (industry_US PREMORTEM Lens 2) | → 2026-08-05 settle | ★★ **FIRED-B** | **2026-08-06 HANDOVER §2b (industry_US)** | **Frozen observable, median RS20 vs SPY of {STX, MU, WDC} on the 2026-08-05 settled close: STX −5.87 · MU −9.13 · WDC −8.93 ⇒ median −8.93, against branch B's "stays ≤ 0".** ★★★ **The knife-edge did not merely hold — it inverted.** The observable ran **−23.7 (registration 07-24) → −9.55 (08-03) → −1.0 (08-04) → −8.93 (08-05)**: nine sessions of convergence toward branch A **reversed −7.9pp on the final bar**. ⇒ **M149's decaying-stock reading is NOT falsified and the roll-off defence holds.** ★★★ **And the registration's own control pair decided the MEANING in the direction the desk did not get to claim**: DELL and HPE were **both already positive** (+3.84 / +15.87 on 08-05), so per S30's text *"if both turn it is an IT-beta event"* — **had the median flipped, the reading was pre-committed to IT-beta.** It did not flip, so **the memory leg reversed while the IT-beta control pair stayed positive** = the cleanest memory-specific signature the bracket could produce. ⚠ **The 08-05 HANDOVER pre-committed "B at a 1.0pp margin" one day early; the final bar came in at 8.93pp.** ★ **Estimator verified before scoring (C1): the RS convention was re-derived from scratch and reproduced the 08-05 run's independently-computed 08-04 figures to 0.1pp on all five names.** ⚠ **P10's carried note stands: the observable moved in a sign-relevant way on four of four sessions, which is the strongest evidence this desk has produced for L3's rule that branch information content must be checked against the observable's own volatility BEFORE freezing** |
| **S31** | 2026-07-27 (industry_US PREMORTEM Lens 2) | → 2026-08-05 settle | 🚨 **`AMBIGUOUS`** — and it is a **registration** finding, not a market one | **2026-08-06 HANDOVER §2b (industry_US)** | **XOM RS20 vs SPY on the 2026-08-05 settled close = +4.17, with RS60 vs SPY +0.52 quoted alongside as the frozen observable requires.** Branch A needs **> +10**, branch B needs **≤ 0** — **XOM finished inside the unassigned corridor, where it sat all week (+5.5 on 08-04).** ⇒ **per L3, `AMBIGUOUS` is a finding about the scenario: the two branches do not partition the observable's range and the MODAL outcome was given no meaning at registration.** ⚠⚠ **Second consecutive `AMBIGUOUS` on this row — the 08-05 run pre-committed exactly this verdict and the final bar confirmed it. Two occurrences is a pattern, not an accident.** ★ One measured detail carried forward: the **13.1pp RS20/RS60 gap at registration closed to +3.65pp, and it closed by RS20 FALLING, not RS60 rising** — the exhaustion geometry the bracket was written to detect, arriving without a scoreable branch. ⚠ **The branch labels also inherit R39** (*"the one with 0% refining exposure (M146)"*) — scored on the frozen observable regardless, meaning-inheritance recorded not smoothed. 🚨 **And a reconciliation fact found the same run: XOM is NOT in the book** (`cycle_exposure` reads the held Energy epicenter as **MPC, PSX**), so a bracket written throughout as *"the only Energy name the book holds"* has been describing a position that no longer exists. ⇒ **PREMORTEM must re-register with an exhaustive partition, or retire it** |
| **S36** | 2026-07-28 (industry_US PREMORTEM Lens 2) | → 2026-08-05 settle | **FIRED-B** | **2026-08-06 HANDOVER §2b (industry_US)** | **XLB 5-day excess return vs SPY on settled closes = −3.79pp ⇒ branch B ("excess ≤ 0, or the green count rises above 0").** Green count is separately still **0 of 12**, so B fires on the excess leg alone and the second leg is not needed. Pre-committed **B by 4.76pp** on the 08-04 bar; final bar **B by 3.79pp**. ⚠⚠ **The fire does NOT settle the divergence it was written to settle.** On the same day the flow axis went the other way: **MATR eqflow +0.167 (3rd of 11) and Δ +0.204 (3rd) against 0 greens and breadth 0.00**, which moved ROTATION to upgrade MATR **UW− → N−**. ⇒ **the price axis fired B while the breadth axis strengthened — three straight weeks of the two axes disagreeing, and a settled bracket did not resolve it.** **S57 carries the same series to 08-12 and is already inside its branch-B region by 1.39pp.** ⚠ **Copper's 96th COT percentile was NOT cited** — byte-identical 07-28 file for a 5th read (next publication 08-07) |
| **S53** | 2026-08-02 (industry_US PREMORTEM Lens 2) | MPC 2026-08-04 + PSX 2026-08-05 | **FIRED-A** *(confirmatory, LOW information **by its own registration**)* | **2026-08-06 HANDOVER §2b (industry_US)** | **Both legs A, scored on the STATED GUIDE as registered — not on the price reaction.** **PSX (08-05)**: revenue **$52.04bn (+55.3% y/y)**, EPS **$9.41 vs $7.68 consensus (+22.5% surprise)**, worldwide realised refining margin **$24.08/bbl vs a $23.15 four-analyst estimate**, and the guide — *"expects soaring refining margins will last through the next quarter and **into 2027**, as the impacts of supply disruptions from the war in Iran likely will continue to weigh on markets for fuels such as gasoline and diesel"* `[seekingalpha body + bloomberg title + Reuters via google_en — 3 independent outlets]`. **MPC (08-04)**: *"Beats Q2 Earnings and Revenue Estimates"* / *"Q2 2026 earnings beat on refining margin surge"* `[nasdaq 4,847자 + yahoo_finance bodies]`. **No hedging-timing lag, no unplanned turnaround drag, no compression language in either.** ⚠⚠ **C2 — the half that does NOT confirm, recorded rather than smoothed: PSX's Atlantic Basin/Europe margin printed $14.44/bbl against a $19.77 four-analyst estimate, a 27% MISS and the ONLY regional miss** (Western/Pacific $29.65 vs $19.93 · Central $29.56 vs $26.35 · Gulf Coast $24.25 vs $22.42 all beat). **The branch is scored on the guide as registered; the regional dispersion is recorded as a fact and NOT folded into the verdict.** ★ **And it is a 2.05× spread inside one company, in the geography physically closest to the Russian distillate shortfall — W5 with a receipt, handed to DEEP-ENRG.** ⚠ **The registration's own caveat binds: n ≈ 1** (the prints are date-clustered 08-04/08-05 and are not independent samples, S1), and **branch A can only confirm — no conclusion changes** |
| **S52** | 2026-08-02 (industry_US PREMORTEM Lens 2) | → 2026-08-06 | **FIRED-C** (neither branch) | **2026-08-06 HANDOVER §2a + DRIFT (industry_US)** | ★★★ **The evidence CLASS branch A demanded finally arrived, and it still fails the threshold.** Branch A requires *"a **dated** Strait-reopening term in a **primary text** … a direct Iran-government statement carrying **a date or 'effective' language**."* On 2026-08-05 Iran's Foreign Ministry spokesperson **Esmaeil Baghaei** stated on the record `[hellenicshipping 2,626자 · bbc 3,153자 · aljazeera 3,525자 · guardian · euronews · scmp · upi · ft — 8+ independent outlets, bodies read]` that Iran and Oman have agreed **the geographic coordinates for a shipping route**, that a joint announcement is **"in its final stage, provided certain third parties do not interfere"**, and — decisively — that **"any agreement between Iran and Oman does not, by itself, guarantee security in the strategic waterway."** ⇒ **coordinates of a route ≠ a dated reopening. No date. No "effective" language. An explicit non-guarantee.** ⚠ **C2, both halves**: `guardian`, citing a senior Iranian source and two regional officials via Reuters, records that they **"pushed back against assertions by Donald Trump that a deal reopening the strait was imminent, saying important details still had to be agreed"**, and that the reported terms would **"give Tehran control over ships entering the gulf"** — a concession, not an opening. **Branch B separately NOT met**, and R46's category rule is what caught it: an `Iranian AND refinery AND strike` query surfaces, at the top, two 08-05 items reading *"strikes have deepened a nationwide gasoline shortage, with several major refineries shut down"* — **body-read, those refineries are RUSSIAN** `[nasdaq/Barchart + oilprice bodies]`. **A title-level read fires branch B on the wrong country.** ★★★ **This threshold has now refused FOUR escalating near-misses across four consecutive runs** (a Bessent conditional · a CENTCOM "free and open" post · a Trump "perimeters of a deal" post · a direct Iran-government route agreement) **while the price paid −12%+ against the desk.** ⚠ Scoring clock stated: HANDOVER measured it at **09:11 ET** with ~15 hours of the window remaining, pre-committed **C**, and **DRIFT re-checked before writeback with no change** |

## Scored by the 2026-08-07 `industry_kr` run (appended to the MASTER scoring log — the log stays shared and un-split)

> ⚠ Written by **append** (`cat >>`), never a whole-file `'w'` rewrite — the **D165** pre-commitment
> after the 2026-08-05 truncation, kept for a third consecutive run.

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S50-KR** | 2026-08-04 (industry_kr MACRO) | → **2026-08-07** (observable = the 08-04/08-05/08-06 settled closes) | ★★★ **FIRED-A** | **2026-08-07 HANDOVER §2a (industry_kr)** | **Frozen observable, `\|069500.KS daily % − ^KS11 daily %\|` on the three settled sessions, `auto_adjust=False`: 08-04 `069500` +1.2361% vs index +1.6221% ⇒ **0.386pp** · 08-05 +3.9569% vs +3.7634% ⇒ **0.194pp** · 08-06 −5.1774% vs −4.5751% ⇒ **0.602pp**. Branch A required all three < 1.5pp ⇒ **A, with the largest of the three at 40% of the line.** ⇒ **the 07-31 (+6.26pp) / 08-03 (−3.80pp) deviation was a crash/rebound ETF-premium artifact; only those two sessions' residuals are contaminated and the benchmark `exposure_rule` uses does NOT become a human decision item.** ★ **The registration's own substitution rule was executed rather than improvised**: `^KS11` **has no 2026-08-06 bar** (it stops at 08-05 — **D130's 4th consecutive occurrence**), and the bracket had pre-written *"substitute the `module_KIS --futopt` 기초지수 종합 and say so — do NOT use `^KS200` (D146: path-dependent)."* Substitute pulled at 08:45 KST pre-open: `A05608` → **기초지수 종합 6,296.38 at 0.00% on the day** (i.e. the settled 08-06 close) against the 08-05 `^KS11` close 6,598.2598 ⇒ **−4.5751%**; the same call's **KOSPI200 982.92** is recorded for cross-check. ⚠ **Anti-signal checked FIRST and did not fire**: the VOID condition is *"a KRX-wide trading halt / circuit breaker truncating any of the three sessions"* — a 4-day domestic sweep returns **zero circuit-breaker activations** (all 21 `서킷브레이커` hits are retrospective/analysis pieces). ⚠⚠ **Recorded without widening the anti-signal**: a **KOSPI sell sidecar fired on 08-06** [chosun 속보 · mt · yonhap] and **KOSDAQ buy sidecars ran three consecutive sessions 08-03~08-05 (a first)**. **A sidecar is a 5-minute program-trading halt, not a KRX-wide halt, so it is not the registered VOID condition** — narrowing or widening an anti-signal after the print is the same violation as moving a threshold. The fact is logged, not used. ⚠ **Scope held exactly as registered (C4)**: branch A establishes *"the desk's benchmark and the most-quoted index do not diverge repeatedly"*, **NOT** *"the ETF has no tracking error"* — `069500.KS` tracks **KOSPI200** while the comparison index is the **composite**, and the composite-vs-200 dispersion is still measurable on the same bar (`069500.KS` 98,900/100 = **989.0 vs KOSPI200 982.92 = +0.62% premium**). ⚠ **n = 3 sessions (S1)**: A says the two crash-window gaps were the exception, not that the gap cannot reopen in the next dislocation |
| — | — | — | ★ **Condition-check executed on every event-conditional row (SIXTH consecutive run) — and the class is now CLOSED** | 2026-08-07 HANDOVER §2b (industry_kr) | **Every ARMED row was classified date-settled vs condition-settled. Result: there are ZERO condition-settled KR rows left.** S39 (FIRED-B 07-30), **S43 (`VOID` 08-03)** and **S44 (FIRED-B 08-03)** all consumed the *"next `069500.KS` session ≤ −3.0%"* trigger. ⚠⚠ **And that is itself the finding: `069500.KS` closed −5.177% on 2026-08-06 and NO registered observable was settled by it.** The desk bracketed the crash class three times, spent all three, and currently has **no instrument that a down session can pay** — registered as **D194**, an *registration* gap rather than a market one. **All remaining KR ARMED rows are date-settled**: S27 (~late 08) · S34 (10-31) · S38 (08-12) · S45 (09-30) · S48-KR (08-12) · S49-KR (10-30) · S51-KR (08-17, filing window 08-14 ±3 business days) · S52-KR (08-19) · S53-KR (10-31) · S54-KR (09-30). **`EXPIRED` = 0 · silent skips = 0.** ★ **`SCENARIOS_US.md` opened and checked (the shared-spine rule)**: the 08-06 `industry_US` run closed its past-dated rows (S30 FIRED-B · S31 `AMBIGUOUS` · S36 FIRED-B · S53 FIRED-A · S52 FIRED-C), and S21/S32/S49/S50 already carry verdicts in this log ⇒ **no US row was left past-dated for this desk to score.** ⚠ **The US rows dated 2026-08-07 (S35 · S35-ANNEX · S47 · S62, and S65's NFP trigger) were deliberately NOT scored**: NFP prints 08-07 08:30 ET = 21:30 KST and this run's clock is **08:45 KST**, so scoring them would be observable fabrication. Handed to the US desk explicitly |

## MASTER INDEX — appended 2026-08-07 by the `industry_kr` run

| **S55-KR** | KR | `SCENARIOS_KR.md` | S55-KR — ★★★ 관세 서명 직후 첫 3세션의 외국인 순매수 (R53 이 만든 관측 공백을 브래킷한다, → 2026-08-13) |

**Count: 79 brackets — 54 US-owned · 25 KR-owned.**
⚠⚠ **S55-KR registered 2026-08-07 by the `industry_kr` BET/ALPHA stages.** IDs checked at **WRITE
time** (D137, per-counter) against every row in **all three** SCENARIOS files **and** both
STANDING_VIEW files **and** RESEARCH.md: `grep S55-KR` returned **0 in all seven**; highest existing
was **S65 (US) / S54-KR (KR)**. The **`-KR` suffix is mandatory** — S55 was taken by the 2026-08-04
`industry_US` PREMORTEM (D76). **The shared-counter proposal for a human now stands for a THIRTEENTH run.**
★ **And this run ran D137's three-grep check as written** — highest `M###` **450**, highest `D###`
**192**, highest `R##` **52** — before assigning **M451–M465 · D193–D201 · R53–R55**.

## MASTER INDEX — appended 2026-08-07 by the `industry_US` run (PREMORTEM registrations)

> IDs checked at WRITE time against EVERY row in BOTH scenario files (the D76 collision class):
> highest existing was **S65 (US) / S55-KR (KR)** ⇒ this run took **S66 – S69**.

| **S66** | US | `SCENARIOS_US.md` | S66 — ★★★ The BULL-steepener-with-credit-fear leg S51's own text refuses to score (ΔDGS2 + ΔHY OAS from the 08-05 anchor; **four branches A / A′ / B / C — the first exhaustive partition written on this desk**, NFP 08-07 → first FRED close covering it, expect 08-10) |
| **S67** | US | `SCENARIOS_US.md` | S67 — ★★★ Was this run's own ENRG N+ → OW− promotion right? (median RS20 vs SPY of {MPC, VLO, PSX}, → 08-13) |
| **S68** | US | `SCENARIOS_US.md` | S68 — ★★★ Is the COMM UW → UW− promotion money broadening or a revision mirage? (two independently-scored legs: median RS20 vs SPY of {DIS, EA} + DIS current-year revision breadth, → 08-13) |
| **S69** | US | `SCENARIOS_US.md` | S69 — ★★ MET: a 🟢가속 flow tag against FALLING estimates (MET RS20 vs SPY quoted with its FY revision breadth, → 08-13) |

| **S68-ANNEX** | US | `SCENARIOS_US.md` | S68-ANNEX — 🚨🚨 leg (i) is half a NON-TRADING security: **EA went private 2026-08-04/05 ($55bn Saudi-led buyout, Form 25-NSE + 8-K 2.01/5.01)**; price frozen 209.70 on two ZERO-volume bars. **S68 NOT re-frozen — leg (i) VOID BY CONSTRUCTION, leg (ii) (DIS revision breadth) stands.** D50 third instance; the COMM promotion it tested is WITHDRAWN |

## Scored by the 2026-08-08 `industry_kr` run (appended to the MASTER scoring log — the log stays shared and un-split)

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, **6런 연속 유지.**

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| — | — | — | ★ **날짜 지난 KR 행 0건 — 채점할 것이 없었고, 그 사실을 확인한 과정을 적는다** | 2026-08-08 HANDOVER §2 (industry_kr) | 모든 ARMED 행을 날짜정산형/조건정산형으로 전수 분류. **이벤트 날짜가 2026-08-08 이전인 KR 행이 하나도 없다** — 직전 런이 S50-KR 을 `FIRED-A` 로 닫으면서 큐가 비었고, **다음 정산점은 08-11(S22)** 이다. **조건정산형(event-conditional) 잔여 = ZERO, 4런 연속** (S39 FIRED-B · S43 `VOID` · S44 FIRED-B 가 클래스를 닫았다). ⚠⚠ **그리고 그 공백이 오늘도 비용을 낳는다 — `D194` 는 메워지지 않은 채 두 번째 런을 넘어간다**: 이 데스크에는 **하락 세션을 정산할 등록 관측값이 여전히 0개**이고, 08-06 의 **−5.177%** 세션은 끝내 어떤 브래킷도 사지 못했다. ⇒ **오늘 `S56-KR` 을 등록해 부분적으로 메운다.** ★ **`SCENARIOS_US.md` 열어서 확인(공유 스파인 규칙)**: 08-07 `industry_US` 런이 자기 창을 들고 있고, **S35(FIRED-A) · S47(FIRED-B) 은 이미 08-02 에 채점 완료**돼 로그에 있다 ⇒ **이 데스크가 채점해야 할 날짜 지난 US 행은 없다.** ⚠ **여전히 열린 크로스데스크 항목 `S8`**(무날짜 `[blank]`)은 **다섯 번째 런째** 정산 불가로 넘어간다 — **KR 데스크는 판정할 수 없고(P5) 사람이 `VOID` 하거나 재등록해야 한다.** 조용히 넘기지 않고 다시 적는다. **`EXPIRED` = 0 · 조용한 생략 = 0.** |
| **S55-KR** | 2026-08-07 (industry_kr BET/ALPHA) | → 2026-08-13 (관측창 08-07·08-10·08-11) | — **세션 1/3 관측, 판정 없음** | (관측 2026-08-08 HANDOVER/MACRO §F-1) | **첫 세션 = 08-07 정착: 010060 외국인 −4.1만주**(밴드 ±20만 안). 함께 보고(판정 미합산): 기관 +4.3만 · 개인 +0.6만 · 종가 272,500 **+11.68%**; 레인 확인용 009830 외국인 **−112.5만주 = 5일 창 최대 매도**, 기관 +136.1만, 종가 33,900 **+11.51%**. ★ **안티시그널 3건 전수 확인, 전부 미발화**: (i) **한국 예외조항 — 라이브 WebSearch 로 확정적으로 부재**(한국은 예외가 아니라 **Section 232 + HTSUS Column 1 합산 15% 상한** 대상이고 EU·일본·대만·스위스·리히텐슈타인과 동일 처우) · (ii) `module_disclosure 010060 --days 5` = **공시 0건** · (iii) 08-07 KRX 전체 거래정지 없음. ⇒ **정상 ARMED, 남은 세션 08-10 · 08-11.** ⚠ **말레이시아산 처우는 1차 미확인으로 `unknown` 유지(C3)** — 유진투자증권의 *"테라서스 말레이시아산은 15% 관세 대상이 아니다"* 는 증권사 서술이고 포고령 본문으로 확인하지 못했다 |

## MASTER INDEX — appended 2026-08-08 by the `industry_kr` run

| **S56-KR** | KR | `SCENARIOS_KR.md` | S56-KR — ★★★ 「탑재량(GB/GPU) 레버」가 HBM 순수도로 000660/005930 을 가르는가 (벤치 `069500.KS` 일간 초과수익 차의 부호 다수결, 3세션, → 2026-08-12) |

**Count: 80 brackets — 54 US-owned · 26 KR-owned.**
⚠⚠ **S56-KR registered 2026-08-08 by the `industry_kr` MACRO/ALPHA stages.** IDs checked at **WRITE
time** (D137, per-counter) against **all three** SCENARIOS files **and** both STANDING_VIEW files
**and** RESEARCH.md: `grep S56-KR` returned **0 in all seven**; **`S56` (US) exists in 11 places** ⇒
**the `-KR` suffix is mandatory** (D76 collision class). Highest existing was **S69 (US) / S55-KR (KR)**.
**The shared-counter proposal for a human now stands for a FOURTEENTH run.**
★ **And this run ran D137''s three-grep check as written** — highest `M###` **486**, highest `D###`
**210**, highest `R##` **59** — before assigning **M487–M500 · R60**.
🚨 **New counter finding, stated rather than papered over**: **the dig counter has the same collision
the scenario counter had.** This run''s stages wrote **D202-KR … D208-KR** and its DEEP-IT agent wrote
**D209-KR … D214-KR**, while the 2026-08-07 `industry_US` run already owns **D202–D210 unsuffixed**.
**The `-KR` suffix keeps them distinct and that is how they are registered in `RESEARCH.md`** — but the
defect is now on the record as **D211** (see RESEARCH Part C).


## Scored by the 2026-08-08 `industry_US` run (appended to the MASTER scoring log — the log stays shared and un-split)

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, **7th
> consecutive run.**

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S62** | 2026-08-05 (industry_US PREMORTEM Lens 2) | → 2026-08-07 settle | ★★ **FIRED-B** — **and it is DEGENERATE by its own registration** | **2026-08-08 HANDOVER §2a (industry_US)** | **Frozen observable, settled 2026-08-07 close: (median RS20 vs SPY of {EMR, ETN, AME, PWR}) − (XLU RS20 vs SPY). EMR +11.529 · ETN +7.740 · AME +5.986 · PWR −0.406 ⇒ median +6.863; XLU −6.389; SPREAD +13.252**, against branch B ≥ +7.42 ⇒ **B, cleared by 5.83pp.** ★ **Estimator verified BEFORE scoring (C1)**: the convention was re-derived from scratch and reproduced the 08-07 HANDOVER's independently-computed **08-06** figures on **every leg to ≤0.004pp** (EMR 11.626 vs 11.63 · ETN 8.196 vs 8.20 · AME 5.651 vs 5.65 · PWR −2.291 vs −2.29 · median 6.924 vs 6.925 · XLU −6.119 vs −6.12 · spread **13.043 vs 13.045**). ⇒ **What it establishes: INDU-electrical and Utilities are SEPARABLE on this observable — the correlated-tilt objection PREMORTEM raised is NOT confirmed by its own registered test.** ⚠⚠ **What it does NOT establish, and this is the larger finding: branch A sat 19.16pp away on the final bar, so the fire is ONE-WAY CONFIRMATION with near-zero information content — `D206` confirmed on a settle rather than predicted.** ★★ **The named contamination mechanism did NOT fire**: the 08-07 HANDOVER flagged that **VST prints from inside XLU** and a large beat would compress the spread toward A without moving the leg it is long. Measured on the settle — **VST −0.56% · XLU +0.53% · SPY +0.61%**, so XLU lost only **0.08pp** to SPY and **the spread WIDENED +0.209pp**, in the direction it was already tracking. ⇒ **`R58` (VST reported PRE-market, not AMC) was RIGHT about the mechanism and it turned out not to change the outcome — both halves recorded rather than the convenient one.** ⚠ **Scoring clock: 09:1x ET Saturday, market closed since Friday's settle ⇒ the scoring bar is fully settled, D74 = 0** |
| — | — | — | ★ **Condition-check executed on every event-conditional US row** | 2026-08-08 HANDOVER §2b (industry_US) | **Against a `[FRED]` pull one day fresher than the 08-07 run had (`asof` 2026-08-06): `S9` real 10y 2.43 vs a ≥2.55 kill = 12bp buffer (⚠ narrowed 14 → 12bp, THIRD consecutive narrowing) · `S23`/`S51` derived 2s10s 4.69 − 4.25 = +0.44 vs a ≤+0.20 kill = 24bp (narrowed 25 → 24; the 08-07 widening did NOT continue) · `S26` HY OAS 2.71 vs ≥3.10 = 39bp (★ WIDENED 35 → 39bp — credit TIGHTENED into the print) · `S41` IG OAS 0.78 vs ≥0.90 = 12bp, unchanged for a 4th read.** ★★★ **`S66` is correctly NOT scoreable and the reason is now a measurable defect: `DGS2`, `DGS10`, `DFII10` and `BAMLH0A0HYM2` all stop at 08-06, so the 08-07 print is uncovered — while `T10YIE`, which IS `DGS10 − DFII10`, printed 08-07 at 2.25.** ⇒ **`D212`; S66 stays ARMED, expect 08-10.** ⚠ **The 10y breakeven's 1bp fall is recorded as the ONLY post-print FRED observable in existence and is explicitly NOT used to call the direction (C3).** 🚨🚨 **`S8` carried un-scoreable for a SEVENTH consecutive run — undated `[blank]`, must be `VOID`ed or re-registered BY A HUMAN (P5). Named again, not dropped.** **`EXPIRED` = 0 · silent skips = 0 · past-dated rows unscored = 0** |
| — | — | — | ★★ **`D206`'s staged rule EXECUTED for the whole board — the first branch-REACHABILITY audit on this desk** | 2026-08-08 HANDOVER §2c (industry_US) | **Distance to the nearest branch, on the settled bar: S62 A 19.16pp ❌ unreachable (settled today) · S57 A 0.59pp ✅ · S61 B 0.006pp ✅ · S60 B already past by 1.90pp ✅ · S58 A 1.33pp with one session left △ · S65 A 3.01 / B 3.46pp ✅ genuinely two-sided · S55 A 3.32 / B 6.18pp △ · S59 blocked by its 2s10s CONDITIONING leg, not by level · S68 leg (i) VOID by construction.** ⇒ ★ **the statistic this produces is about REGISTRATION QUALITY, not any one row: of nine live US brackets, one settled degenerate, one is void on half its construction and one is blocked by a conditioning leg — a third of the board could not have paid information this week regardless of what the market did.** 🚨 **And PREMORTEM Lens 2 found the SIBLING failure: `S61` sits 0.006pp from branch B against ±7.2–8.7% implied moves ⇒ it will cross on ordinary noise, i.e. it is not unreachable but INEVITABLE.** ⇒ **`D216` — reachability must be checked in BOTH directions, and this desk measured both failure modes inside one week** |
| — | — | — | 🚨 **A correction to the 08-07 run's own HANDOVER: `S61` was read on the WRONG ESTIMATOR** | 2026-08-08 HANDOVER §2d (industry_US) | **The 08-07 §2c table reported S61 as *"STNG −2.07 · FRO +5.96 · ★★ FRO has FLIPPED POSITIVE"*. Those are RS20 values; S61's frozen observable is a 5-SESSION CUMULATIVE EXCESS.** On the bracket's own axis the same 08-06 bar reads **STNG −2.50 · FRO −2.45 · EW −2.472** — **FRO was NEGATIVE, not positive** ⇒ **the row's reported direction was inverted by an estimator substitution.** ⚠ **Not cosmetic: on the correct axis the row has since moved to −4.184, six thousandths from branch B, which the RS20 reading would never have surfaced.** ⇒ **`D213`, and this run's operating rule — every branch line is re-read from `SCENARIOS_US.md` AT SOURCE each HANDOVER, which is how the whole §2b table above was built.** ⚠ **C4 scope: this corrects ONE row's reading in ONE file. S61's registration text and bands are untouched, and it does NOT imply the 08-07 run's other rows were mis-estimated — S62's were verified to 0.002pp** |

## MASTER INDEX — appended 2026-08-08 by the `industry_US` run

> IDs checked at **WRITE time** (D137 / D76 / M319) against EVERY row in **all three** `SCENARIOS*.md`
> **and** both `STANDING_VIEW*.md` **and** `RESEARCH.md`: `grep S70` / `S71` / `S72` returned **0 in
> all nine files**; highest existing was **S69 (US) / S56-KR (KR)** ⇒ this run took **S70 – S72**.
> ★ **And this run ran D137's three-grep check as written** — highest `M###` **500**, `D###` **211**,
> `R##` **60** — before assigning **M501–M524 · D212–D219 · R61**.

| **S70** | US | `SCENARIOS_US.md` | S70 — ★★★ Did the 08-07 credit print read RELIEF or FEAR? The leg S66 leaves open, scored ALONE so one lagging series cannot swallow the question (HY OAS at the first `[FRED]` close covering 08-07, expect **2026-08-10**) |
| **S71** | US | `SCENARIOS_US.md` | S71 — ★★★ The CPI→PPI DIVERGENCE: the one genuinely un-covered falsifiable gap (XLU 1-session excess vs SPY on 08-13 MINUS on 08-12; bands from trailing-252 quantiles, → **2026-08-13**) |
| **S72** | US | `SCENARIOS_US.md` | S72 — ★★★ Is the four-tilt cluster ONE bet? Two stages of one run disagreed about WHICH tilts are correlated, so the disagreement is registered rather than resolved (sign pattern of XLI/XLF/XLB/XLU/XLE 1-session excess vs SPY, → **2026-08-12**) |
| **S57-ANNEX** | US | `SCENARIOS_US.md` | S57-ANNEX — ★★★ contamination notice on branch A's stated MEANING (**S57 NOT re-frozen; thresholds unchanged**). **SIX independent legs** |
| **S61-ANNEX** | US | `SCENARIOS_US.md` | S61-ANNEX — ★★★ mechanism + information-content notice (**S61 NOT re-frozen; bands unchanged**). Branch B's label says *"no premium appears / D168 inert"* while D168's event is the most active object in the run, **and the branch is 0.006pp from being mechanically inevitable** |

**Count: 85 brackets — 59 US-owned · 26 KR-owned.**
⚠⚠ **The shared-counter proposal for a human now stands for a FIFTEENTH run.**
🚨 **And the dig counter carries the same collision the scenario counter had**: the 08-07 `industry_US`
run owns **D202–D210 unsuffixed** while the 08-08 `industry_kr` run wrote **D202-KR – D214-KR**,
distinguished only by suffix (registered as **D211**). **This run took D212–D219 unsuffixed, which does
not collide with either** — checked at write time.


## Scored by the 2026-08-09 `industry_kr` run (appended to the MASTER scoring log — the log stays shared and un-split)

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, **7런 연속 유지.**

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| — | — | — | ★ **날짜 지난 KR 행 0건 — 채점할 것이 없었고, 그 사실을 확인한 과정을 적는다** | 2026-08-09 HANDOVER §2 (industry_kr) | 모든 ARMED 행을 날짜정산형/조건정산형으로 전수 분류. **이벤트 날짜가 2026-08-09 이전인 KR 행이 0건**이고, **다음 정산점은 08-11(S22)** 이다. **조건정산형(event-conditional) 잔여 = ZERO, 5런 연속**(S39 FIRED-B · S43 `VOID` · S44 FIRED-B 가 클래스를 닫았다). ⚠⚠ **`D194` 가 세 번째 런을 넘어간다** — 08-08 이 등록한 `S56-KR` 은 *하락*이 아니라 *두 이름의 상대 부호*를 재는 브래킷이라 **부분 해소일 뿐**이고, **「벤치가 −3% 이상 빠지는 세션이 무엇을 지불하는가」는 오늘도 미등록**이다. ⇒ **오늘 `S57-KR` 을 등록해 이벤트 세션 쪽을 한 칸 더 메운다.** ★ **`SCENARIOS_US.md` 열어서 확인(공유 스파인 규칙)**: 08-08 `industry_US` 런이 **S62 `FIRED-B`** 로 자기 창을 닫았고 조건정산형(S9·S23·S26·S41·S51)은 전부 그 데스크가 버퍼를 재측정했다 ⇒ **이 데스크가 채점해야 할 날짜 지난 US 행은 없다.** 🚨🚨 **`S8` 은 무날짜 `[blank]` 인 채 정산 불가로 넘어간다 — US 데스크 기준 8런째, KR 데스크가 이 사실을 적는 것은 7번째.** **KR 은 판정할 수 없다(P5) — 사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다. 조용히 넘기지 않는다.** ⚠ **US 소유 `S66` 도 오늘 채점 불가**이고 그 이유를 KR 데스크가 **독립 재현**했다(`DGS2`·`DGS10`·`DFII10`·`BAMLH0A0HYM2` 전부 08-06 정지, `T10YIE` 만 08-07 = 2.25 ⇒ **`D212` 2일 연속**). **`EXPIRED` = 0 · 조용한 생략 = 0.** |
| **S55-KR** | 2026-08-07 (industry_kr BET/ALPHA) | → 2026-08-13 (관측창 08-07·08-10·08-11) | — **세션 1/3 유지, 새 세션 없음** | (확인 2026-08-09 DEEP-MATR §5) | **주말 휴장으로 새 관측 세션이 없다.** ★ **안티시그널 3건 전수 재확인, 전부 미발화**: (i) 한국 예외조항 — 08-08 런이 라이브 WebSearch 로 부재 확정(한국 = Section 232 + Column 1 합산 **15% 상한**, EU·일본·대만·스위스 동일 처우), 오늘 새 정보 없음 (ii) `module_disclosure 010060` 신규 공시 0건 (iii) 08-07 KRX 전체 거래정지 없음. ⇒ **정상 ARMED, 남은 세션 08-10 · 08-11.** ⚠ **말레이시아산(테라서스) 처우는 1차 미확인 `unknown` 유지(C3) — 포고령 본문 미도달 3런 연속.** ★ 오늘 국내 1매체가 *"폴리실리콘에 美 15% 관세… **영향 적고 반사이익 기대**"*[mt 08-09]를 실었고 **R60 의 방향과 같은 쪽**이나, **기록만 하고 브래킷을 흔들지 않는다**(L3: 사후에 기준을 바꾸지 않는다). ⚠ **두 이름은 오늘 보드의 `❌약한손` 전부**이고 **둘 다 🟢 가 `vol_surge` 단독 점화(velocity 결측)라 D6 로 인용 불가.** |
| **S56-KR** | 2026-08-08 (industry_kr MACRO/ALPHA) | → 2026-08-12 (3세션 부호 다수결) | — **세션 0/3, 관측창 미개시** | (확인 2026-08-09 EVENT_ALPHA C4) | **관측창은 08-10 부터.** 오늘 앞당기지 않는다. 서사축 확인: 「삼성·SK AI 메모리」 스레드가 **REIGNITED 4→7→7→5→7→2, 총 134건, nb 25.0 = 살아있는 스레드 중 최고**로 살아 있다. ★ **반대 절반도 같은 창에 있다**(C2): *"중국 추격·이익배분 시험대"* · *"중국, DUV까지 국산화?"* · 블라인드 신흥어 **`CXMT` 4런 연속 상위**. ⚠ **새 사건 2건이 §3b 에 없다**: **"SK하이닉스, 중국 충칭 패키징공장 지분매각 등 검토"**[6건/5매체 08-08] · **"SK하이닉스 통합노조 신설 추진"**[08-09] |
| **S27** | 2026-07-27 (industry_kr MACRO/DEEP-ENRG) | ~2026-08 말 | — **관측면 미도래, 그리고 오늘 그 사실이 1차에 가깝게 확인됐다** | (확인 2026-08-09 MACRO §G) | **9차 최고가격 지정은 아직 없다** — *"주유소 기름값 **12주째 하락**…휘발유·경유 1,800원대"*[yonhap·sedaily 08-08]의 본문이 **7차 최고가격을 현행으로 서술**한다(M538). ⇒ **12주 연속 하락은 9차 지정 압력을 낮추는 방향의 관측**이고, 그것 자체가 브랜치 정보다. **정상 ARMED.** |

## MASTER INDEX — appended 2026-08-09 by the `industry_kr` run

| **S57-KR** | KR | `SCENARIOS_KR.md` | S57-KR — ★★★ 호르무즈 재개방이 KR 정유 두 이름에서 「전쟁 프리미엄」과 「시설 병목」을 가르는가 (010950+096770 등가중 초과 vs `069500.KS`, 밴드 −6.07pp = 실측 120세션 sd, → **2026-08-20**) |

**Count: 81 brackets — 54 US-owned · 27 KR-owned.**
⚠⚠ **S57-KR registered 2026-08-09 by the `industry_kr` MACRO/BET stages.** IDs checked at **WRITE
time** (D137, per-counter) against **all three** SCENARIOS files **and** both STANDING_VIEW files
**and** RESEARCH.md: `grep S57-KR` returned **0 in all seven**; `grep S73` returned **0**. Highest
existing was **S72 (US) / S56-KR (KR)**. **The `-KR` suffix is mandatory** (D76 collision class).
**The shared-counter proposal for a human now stands for a FIFTEENTH run.**
★ **And this run ran D137's three-grep check as written** — highest `M###` **524**, highest `D###`
**219**, highest `R##` **61** — before assigning **M525–M543 · D220-KR–D226-KR**.
★ **이 런의 철회(R) 는 0건이다** — 그리고 그 이유를 적는다: **이 런이 저지른 오류(MACRO §H 의
승계값 4칸 오기)는 캐리에 들어간 적이 없어 R 번호를 주지 않는다.** ROTATION §0 이 같은 런 안에서
잡아 ADDENDUM 으로 교정했다(**D48 패턴의 KR 12번째 인스턴스**).
🚨 **dig 카운터 충돌은 15런째 미해결** — 이 런은 **`-KR` 접미사**로 `D220-KR ~ D226-KR` 을 썼고,
무접미사 `D220~D226` 은 비어 있으나 **US 데스크가 다음 런에 가져갈 수 있다**(D211).


## Scored by the 2026-08-10 `industry_kr` run (appended to the MASTER scoring log — the log stays shared and un-split)

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, **8런 연속 유지.**

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| — | — | — | ★ **날짜 지난 KR 행 0건 — 그리고 US 파일도 열어 확인했다** | 2026-08-10 HANDOVER §2 (industry_kr) | 전 ARMED 행을 날짜정산형/조건정산형으로 전수 분류. **이벤트 날짜가 2026-08-10 이전인 KR 행이 0건**, **다음 정산점은 08-11(`S22`)**. **조건정산형 잔여 = ZERO, 6런 연속.** ★ **`SCENARIOS_US.md` 열어 확인**: **US 소유 `S70`(08-07 커버 HY OAS, expect 08-10)과 `S66` 은 오늘도 채점 불가**이고 그 이유를 KR 데스크가 **3일 연속 독립 재현**했다 — `BAMLH0A0HYM2`·`DGS2`·`DGS10`·`DFII10` 전부 **08-06 정지**(HY OAS 2.71), `T10YIE` 만 **08-07 = 2.25**(`D212`). ⚠ **`DTWEXBGS` 는 07-31 정지 = 10일.** 🚨🚨 **`S8` 은 무날짜 `[blank]` 인 채 정산 불가로 넘어간다 — US 기준 9런째, KR 데스크가 이 사실을 적는 것은 8번째. KR 은 판정할 수 없다(P5).** **`EXPIRED` = 0 · 조용한 생략 = 0.** |
| **S55-KR** | 2026-08-07 (industry_kr BET/ALPHA) | → 2026-08-13 (관측창 08-07·08-10·08-11) | — **세션 2/3 관측일이나 미정착** | (확인 2026-08-10 HANDOVER §2a) | **오늘이 세션 2/3 인데 런 시각이 08:29 KST = 개장 전**이라 관측값이 아직 없다. **미정착 봉으로 세지 않는다(D74).** 세션 1/3(08-07 정착) 유지: 010060 외국인 **−4.1만주**(밴드 ±20만 안). ★ **안티시그널 3건 재확인 전부 미발화**: (i) 한국 예외조항 새 1차 정보 없음 (ii) `module_disclosure 010060` 신규 0건 (iii) 08-07 KRX 전체 거래정지 없음. ⚠ **말레이시아산 처우 `unknown` 4런 연속.** ⚠ **오늘 서사 축이 반대로 움직였다**: **「폴리실리콘 15% 관세」 스레드가 ENDED(피크 8매체)** 이고 **버킷 배율 0.19×** 인데 **`theme-age` 는 🟡ACCELERATING 45.13×** — `D223-KR` 최대 격차(237배). **기록만 하고 브래킷을 흔들지 않는다(L3).** |
| **S56-KR** | 2026-08-08 (industry_kr MACRO/ALPHA) | → 2026-08-12 (3세션 부호 다수결) | — **세션 0/3, 관측창 오늘 개시** | (확인 2026-08-10 EVENT_ALPHA 카드 8 / BET §B) | **관측창이 오늘 열리는데 08-10 봉이 없다** ⇒ **세션 0/3 유지.** 서사 확인: **오늘 두 이름을 「묶는」 재료가 크다**(삼전·SK하닉 프리마켓 반등[12건/3매체] + 모건스탠리 *"메모리 조정 끝"*[3건/2매체]), **가르는 재료는 1매체에 있다** — **chosun nb 25.5 「엔비디아 베라 루빈, 원가의 62%가 메모리… HBM4보다 비중 큰 소캠2」** = **이 브래킷의 레버(탑재량)가 원가비중 숫자로 처음 인쇄**됐다. ⚠ **그런데 `소캠` 테마는 🔴FADING 0.0×(n=31, 나이 80일)** ⇒ **레버는 인쇄됐고 서사는 없다.** ⚠ **두 이름 모두 오늘 🔴분산 · 개인 흡수**(005930 외 −782.0만/개 +1,750.7만 · 000660 외 −273.9만/개 +342.5만) — **브래킷은 가격만 보므로 VOID 사유가 아니다.** 반대 절반(C2): **"애플, 中반도체 도입 추진"[5건/4매체]** · **[中반도체굴기]①[4건/2매체]** · 블라인드 `CXMT` **5런 연속**. |
| **S52-KR** | 2026-08-05 (industry_kr DEEP-HLTH) | → 2026-08-19 (11세션 창) | — **관측값 2개 모두 실측, 채점 아님** | (측정 2026-08-10 DEEP-HLTH §2) | **O2 = 31/46**(앵커 26.60 · 상한 28.14 ⇒ **+2.85 SE**); 창 내 확보 세션 **08-05 = 30 · 08-07 = 31 ⇒ 평균 30.5**. **O1 = 199,300 vs 상한 199,105 = +0.10%.** ★★ **`D225-KR` 오염 가설을 세웠다가 통제 실험으로 반박했다** — 같은 정착 바를 구코드·신코드 세 파일로 계산해 **31/31/31 동일**(랭크 비교라 단조변환에 불변, 최대 이동 종목 207940 은 top-2 제외) ⇒ **O2 는 오염되지 않았다.** 안티시그널 전수: **AS-1 미발화**(068270 공시 2건은 **08-03 = 창 시작 전**: 투자판단관련주요경영사항 CTP44 · 국민연금 대량보유) · **AS-2 미발화**(n=48) · **AS-4 미발화**(top-2 시총비중 **78.4% = 앵커와 일치**) · **AS-5 미발화**(외 +60.1만 ∧ 기 +146.7만) · **AS-3 는 창 미완이라 `unknown`(C3)**. 🚨 **새 결함 `D230-KR`: 창 11세션 중 08-06 정착 바가 어떤 산출물에도 없다**(`sector_flow.py` 에 `--asof` 부재) ⇒ 정산 시 n<11, 브래킷의 SE 1.542 는 과소. |
| **S38 / S48-KR** | 2026-07-29 / 2026-08-02 | → **2026-08-12 (둘 다)** | — **분기 거리 첫 측정(2런째 미측정이던 항목)** | (측정 2026-08-10 DEEP-INDU 델타②) | **006360: 4.42% `building(+1.13)` 🔥** — 등록 시점 3.63% `building(+0.08)`(07-28) 대비 **+0.79pp/9세션**, **building 계수가 14배 가속**. **B(≥5.00%)까지 0.58pp · A(≤2.00%)까지 2.42pp** ⇒ **D216: B 도달가능, A 사실상 불가.** **006340: 3.03% `covering(−0.12)` 🔥** — 등록 4.00% `building(+0.99)`(07-31) 대비 **−0.97pp/6세션, 부호 반전**. **A(≤2.50%)까지 0.53pp · B(≥5.50%)까지 2.47pp** ⇒ **A 도달가능, B 불가.** ★★★ **같은 날짜에 같은 구성의 n=2 를 만들려던 쌍이 정반대로 가고 있다** ⇒ 08-12 에 나올 것은 한 방향 2관측이 아니라 **갈림**일 가능성이 높다. ⚠ **밴드를 사후에 바꾸지 않는다(L3) — 위는 거리 보고이지 예측이 아니다.** ⚠ **`S38` 안티시그널 감시**: BUILDING 4일 「은행 가계대출 조이기」 스레드가 정책 이벤트로 격상되면 `S38` **`VOID`**. 🚨 **`D148` 11런 미실행 ⇒ 정산일에도 백분위를 말할 수 없다.** ⚠ **006340 의 안티시그널 2건(HG=F ±10% · 006340 개별공시)은 오늘 확인하지 않았다.** |
| **S27** | 2026-07-27 | ~2026-08 말 | — **관측면 미도래** | (확인 2026-08-10 MACRO §D-3) | `최고가격` 테마 **⚪ECHO 1.05×**(n=126, 어제 1.00×). 9차 지정 관련 새 1차 재료 없음. **정상 ARMED.** |

## MASTER INDEX — appended 2026-08-10 by the `industry_kr` run

| **S52-KR-ANNEX** | KR | `SCENARIOS_KR.md` | S52-KR-ANNEX — ★★★ 정보량 통지: **O1 이 분기선 위 +0.10% = 일간 sd 의 1/29** ⇒ A/B 가 노이즈로 갈린다(`D216` 「불가피」형의 KR 첫 사례). **`S52-KR` 은 재동결하지 않는다 — 임계·밴드·분기·정산일 전부 불변** |

**Count: 82 brackets — 54 US-owned · 28 KR-owned.**
⚠⚠ **`S52-KR-ANNEX` registered 2026-08-10 by the `industry_kr` DEEP-HLTH stage.** IDs checked at
**WRITE time** (D137, per-counter) against **all three** SCENARIOS files **and** both STANDING_VIEW
files **and** RESEARCH.md: `grep S52-KR-ANNEX` returned **0 in all seven**. 기존 최고
**S72(US) / S57-KR(KR)** · **M543 · D226-KR · R61**.
**The shared-counter proposal for a human now stands for a SIXTEENTH run.**
★ **And this run ran D137's three-grep check as written** before assigning **M544–M559 · D227-KR–D230-KR**.
⚠ **애넥스는 브래킷이 아니다** — 카운트에는 넣되 **`S52-KR` 의 어떤 값도 바꾸지 않는다.**

---

## MASTER INDEX — appended 2026-08-10 by the `industry_US` run

> IDs checked at **WRITE time** (D137 / D76 / M319) against EVERY row in **all three** `SCENARIOS*.md`
> **and** both `STANDING_VIEW*.md` **and** `RESEARCH.md`: `grep S73` / `S74` returned **0 in all nine
> files**; highest existing was **S72 (US) / S57-KR (KR)** ⇒ this run took **S73 – S74**.
> ★ **D137's three-grep check run as written** — highest `M###` **559**, `D###` **D230 (as `-KR` only;
> unsuffixed D227–D230 were empty and reserved for this desk by the 08-10 KR run's own note at
> `RESEARCH.md:1884`)**, `R##` **61** — before assigning **M560– · D227–D232 · R62–**.
> ⚠⚠ **Provenance note that matters for the count**: the **2026-08-09 `industry_US` run never wrote
> back** (it produced five output files and stopped before writeback; `handoff/` holds zero trace of
> it). Its `D227`/`D228` (HANDOVER) and `D229`/`D230` (MACRO §J) are **rescued at their original
> numbers by this run**, and its `M544–M552` are **re-registered at M560+ because the KR runs of
> 08-09/08-10 consumed M544–M559 in the interval.** **The absence itself is registered as `D231`.**

| ID | Owner | File | One line |
|---|---|---|---|
| **S73** | US | `SCENARIOS_US.md` | S73 — ★★★ **July CPI 2026-08-12, the ≤48h binary the protocol makes MANDATORY.** **TWO legs scored independently** (the S70 pattern applied at registration, because `D212` has blocked S51/S66/S70 for four runs): **macro leg** ΔDGS2 ≥ +0.15 ∧ ΔHY OAS ≥ +0.10 (branch H) vs ΔDGS2 ≤ −0.15 ∧ ΔHY OAS ≤ −0.05 (branch C), anchored on the 08-06 close; **equity leg** median 1-session excess vs SPY of {JPM,BAC,XLI} ≤ −1.50pp vs XLU ≥ +2.00pp on the **08-12 session**. All legs **1.4σ–2.9σ**, base rates 6.7%/10.0%, and **outside** the ±1.9–2.2% D4 implied moves. **Branch H falsifies INDU/FIN/STPL simultaneously; branch C falsifies UTIL/RE/MATR simultaneously** |
| **S74** | US | `SCENARIOS_US.md` | S74 — ★★★ **Hormuz: the reopening condition is NAMED for the first time in nine runs.** The IRGC's two conditions (end of the US naval blockade · compensation for war damages), explicitly **decoupled from the Oman track** — which retires the mechanism every desk file has watched since 08-05. `[news]` grade, ≥2 outlet **bodies** required. **`S8` is NOT touched (human-gated, P5).** ⚠ **S61 explicitly REFUSED as the price confirmation (0.001σ from firing = D216 *inevitable*); `S54` used instead at ±1.0σ symmetric.** → **2026-08-24** or first occurrence |
| **S57-ANNEX-2** | US | `SCENARIOS_US.md` | S57-ANNEX-2 — ★★★ the carrier's driver is now **dated and primary-sourced** (**S57 NOT re-frozen; thresholds unchanged**). NEM = **~85% of the observable**, its 5-session excess **+17.05pp = its own trailing-60 MAXIMUM, +3.32σ**, and on 2026-08-10 the issuer disclosed **Newmont PAYS Barrick $1.95bn** + consent to Barrick's NA IPO. ★ **Its 21–60-day base is −26.50pp — the whole move sits on a losing base** (computed twice independently this run, agreeing to 0.01pp) |

**Count: 88 brackets — 62 US-owned · 26 KR-owned.**
⚠⚠ **The shared-counter proposal for a human now stands for a SEVENTEENTH run.**
🚨 **And this run made the collision worse in the one direction that was still clean**: it took
**D227–D230 unsuffixed**, which now exist alongside **D227-KR–D230-KR**, distinguishable only by
suffix — the exact class `D211` was registered to complain about. **It was done deliberately**, because
the 08-10 KR run's own note reserved those four numbers for this desk and because rescuing the
orphaned findings under *different* numbers would have created two ids for one defect. **The cost is
stated rather than hidden, and it strengthens rather than weakens the case for a human to fix the
counter.**

## Scored by the 2026-08-12 `industry_kr` run (appended to the MASTER scoring log — the log stays shared and un-split)

| ID | 등록 | 정산 | 결과 | 확인 위치 | 근거 |
|---|---|---|---|---|---|
| **S22** | 2026-07-25 (industry_kr BET/ALPHA) | 07-31 → **재정산 08-11** | ✅ **`FIRED-A`** | 2026-08-12 HANDOVER §2-1 | **DART 1차**(rcept 20260811800737): **거래종결일 2026-08-11**, 최대주주 **30.74% → 43.15%**, 이클립스㈜가 SK디스커버리 10,455,825주 + 한앤코 4,225,455주 취득. ★★ **그런데 이 채점은 두 가지를 죽인다**: ① **인수자가 KKR 이 아니다** ⇒ **R62** ② **브랜치 B 의 「두 번째 연기 = 킬」 규칙 자체가 반증됐다**(07-31 을 넘기고 종결) — 1차에는 **연기 기록이 없고** SPA 03-06 체결·종결 08-11 이 한 문서에 있다 ⇒ **우리가 센 것은 회사가 아니라 우리 캘린더의 오차** ⇒ **R63**. ★ **S28**(07-28 임시주총 두 후보 선임 = A)이 예고한 대로 정산 — **리딩 인디케이터가 처음으로 본 브래킷을 맞혔다** |
| **S55-KR** | 2026-08-07 (industry_kr BET/ALPHA) | → 2026-08-13 (관측창 08-07·08-10·08-11) | ✅ **`FIRED-C` (AMBIGUOUS)** | 2026-08-12 HANDOVER §2-4 | **010060 외국인 3세션 합 −12.1만주**(−4.1 / −5.1 / −2.9), 밴드 **±20만 안**. 병기(판정 미합산): 기관 **+9.2만** · 개인 **+4.3만** · 레인 확인 **009830 외국인 −105.4만주**. **관측창이 08-11 로 닫혔고 값이 더 바뀔 수 없어 오늘 채점**했다(정산일 08-13 은 창 다음 런). 등록 문언대로 **밴드를 넓히지 않고 발효 D-30(2026-11-04)로 재등록 ⇒ `S59-KR`**. ⚠ **교란 1건 기록**: 010060 이 **08-10 「자기주식취득신탁계약 해지결정」 2건**(본사·자회사) 공시 — **등록된 안티시그널 열거(유상증자·대규모수주·지분변동)에 자기주식이 없어** VOID 사유로 쓰지 않았다. 브랜치가 C(무정보)라 실무 결론은 불변 |
| **S38** · **S48-KR** | 2026-07-29 / 2026-08-02 | **2026-08-12 = today** | ⛔ **`PENDING-DATA` — 정산 불가, `EXPIRED` 아님** | 2026-08-12 HANDOVER §2-2 | **동결 관측값(「08-12 의 KRX %float」)이 아직 인쇄되지 않았다** — 잔고 시계열의 마지막 행이 **2026-08-07**(08-10·08-11 조차 없음) ⇒ **공표 지연을 등록 시점에 계산하지 않은 구성 결함**(**D231-KR**). **밴드 불변, 대체 관측값 없음.** 거리 보고: **006360 4.61%(C 구간, B 까지 0.39pp)** · **006340 3.22%(C 구간, A 까지 0.72pp, `covering(−0.34)`)**. ★★ **`D148` 을 12런 만에 집행**(M562): 006360 **92.1 백분위**·자기최대 6.30%(05-08) ⇒ **B 에 전례 있음** · 006340 **93.2 백분위**·**자기최대 4.00% = 정확히 S48-KR 등록일(07-29)** ⇒ **극값에서 등록됨, 평균회귀가 귀무가설**(**D236-KR**). ⚠ **D133 재기재**: 관측값 인쇄 시점(≈08-14~18)이 **KOSPI200 최종거래일 08-13 이후**라 만기 효과가 섞인다. **다음 런의 #1 채점 작업** |
| **S56-KR** | 2026-08-08 (industry_kr MACRO/ALPHA) | → 2026-08-12 (3세션 부호 다수결) | ⛔ **PENDING — 결정 세션이 이 런의 시계 뒤에 있다** | 2026-08-12 HANDOVER §2-3 | 세션별 차 = (000660 초과)−(005930 초과) vs `069500.KS`: **08-10 +0.292(+)** · **08-11 −3.778(−)** · **08-12 (−2.061) 미정착**. ★ **안티시그널 (ii) 가 실제로 발화해 08-10 을 제외했다** — **2026-08-10 10:10 KRX 조회공시요구**(4조 충칭 지분매각) + 같은 날 **「미확정」 답변**(M567) = 000660 고유 사건. 남는 세션 2개 ⇒ VOID 아님. **유효 1세션 부호 `−`, 오늘 15:30 정착분이 결정한다.** ⚠ 005930 쪽 지분변동 6건은 **전부 임원 소유상황보고서(일상)** — 문자대로면 VOID 지만 실질이 아니다 ⇒ **열거를 좁혀야 한다(D233-KR)**. ⚠ **오전 크론인 이 데스크는 당일 정산 브래킷을 구조적으로 못 센다(D232-KR)** |
| — | — | — | ★ **날짜 지난 행 전수 채점 · `EXPIRED` = 0 · 조용한 생략 = 0** | 2026-08-12 HANDOVER §2 (industry_kr) | 전 ARMED 행을 날짜정산형/조건정산형으로 분류. **조건정산형 잔여 = ZERO, 7런 연속.** ★ **`SCENARIOS_US.md` 열어 확인**: 이 데스크가 채점할 날짜 지난 US 행은 **`S8` 외에 없다**. 🚨🚨 **`S8`(무날짜 `[blank]`)은 오늘도 정산 불가 — KR 데스크가 이 사실을 적는 것은 9번째.** **KR 은 판정할 수 없다(P5)** — 사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다. ⚠ **`D194`(−3% 하락 세션을 살 브래킷)는 오늘도 0 — 7런째.** ★ **`D212`(FRED 정지) 4런 만에 해소** — DGS2·DGS10·DFII10·HY OAS 전부 08-10, T10YIE 08-11 |

## MASTER INDEX — appended 2026-08-12 by the `industry_kr` run

| ID | 시장 | 파일 | 한 줄 |
|---|---|---|---|
| **S58-KR** | KR | `SCENARIOS_KR.md` | S58-KR — ★★★ 000660 충칭 패키징 지분매각(₩4조): 회사가 스스로 박은 재공시 기한 → **2026-09-09** |
| **S59-KR** | KR | `SCENARIOS_KR.md` | S59-KR — ★★ `S55-KR` 재등록(밴드 불변 ±20만주), 관세 발효 D-30 → **2026-11-04** |

⚠⚠ **S58-KR·S59-KR registered 2026-08-12 by the `industry_kr` ALPHA/handoff stages.** IDs checked at
**WRITE time** with a 3-grep across all handoff files: 기존 최고 **S74(US) / S57-KR(KR)** ⇒ 이 런은
**`-KR` 접미사**로 **S58-KR · S59-KR** 을 쓴다(**D76** 충돌 클래스 · **D211** 카운터 충돌 사람 대기 5런째).

---

## Scored by the 2026-08-12 `industry_US` run (appended to the MASTER scoring log — the log stays shared and un-split)

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, held.
> ★★ **TEN rows scored in one run — the largest batch this desk has run** — because **there was no
> `industry_US` run on 2026-08-11 at all** (`llm_outputs/2026-08-11/` holds only `PULSE.md`) and the
> FRED yield/credit block published on 08-10, releasing four rows blocked for four consecutive runs.

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S51** | 2026-07-31 (PREMORTEM Lens 2) | → 2026-08-10 | ★ **FIRED-A** | 2026-08-12 HANDOVER §2b (industry_US) | Derived 2s10s = `DGS10 − DGS2` at the settled **2026-08-07** close = **4.65 − 4.19 = +0.46** ≥ the +0.35 line ⇒ **the bear steepener persisted and the FIN NIM mechanism is intact on a fresh, non-retracted measurement.** ⚠ Its own registered bull-steepener caveat is scored separately by **S66** and did **not** fire. **Blocked for 2 days by `D212`, then released when the H.15 block published through 08-10.** |
| **S66** | 2026-08-07 (PREMORTEM Lens 2) | → first `[FRED]` close covering 08-07 | ★ **FIRED-B (with us)** | 2026-08-12 HANDOVER §2b | Anchored on the 08-05 print (`DGS2` 4.18 · HY OAS 2.75). At the covering close: **ΔDGS2 = +0.01** and **ΔHY OAS = −0.05** ⇒ branch B (`ΔDGS2 > −0.05` **and** `ΔHY OAS < +0.08`) fires. **Neither leg of the growth-scare conjunction moved on a −23k payroll.** ⚠ Branch A was pre-declared a sub-1% conjunction and **B is the modal outcome — reported as modal, not as a win.** ⚠ Branch **A′** (exactly one leg clearing its tail) also did not fire. |
| **S70** | 2026-08-08 (MACRO) | → first `[FRED]` close covering 08-07 | ★ **FIRED-A (relief)** | 2026-08-12 HANDOVER §2b | `BAMLH0A0HYM2` at the covering close = **2.70%** ≤ the 2.71 line ⇒ **credit TIGHTENED 1bp through the payroll shock** (2.75 → 2.71 → 2.70). ⇒ **the 08-07 rally reads as rate relief, not credit fear.** ⚠ **DEEP-FIN's own grading is carried with the verdict: A is the MODAL branch and mostly confirms the tape; the information was entirely in branch B, which did not fire.** **Blocked for four consecutive runs by `D212`.** |
| **S54** | 2026-08-03 (PREMORTEM Lens 1) | → 2026-08-10 | 🚨 **AMBIGUOUS — not scored** | 2026-08-12 HANDOVER §2b | ★★★ **A construction defect, registered as `D233`.** The frozen text names *"the equal-weight **5-session** excess … from the **2026-07-31 close** to the **2026-08-10 close**"* — **but 07-31 → 08-10 is SIX sessions.** The two readable constructions give **different branches**: anchored **−1.467pp (C)** vs rolling-5 ending 08-10 **−5.130pp (B, < −4.5)**. ★ **The ambiguity was invisible until today by arithmetic accident** — at the 08-07 bar the two coincide (07-31 → 08-07 *is* five sessions), which is why every prior run reported one number (+2.110) and saw no conflict. **No threshold was improvised (the L3 rule); both readings are recorded so a human can settle the anchor-vs-window convention once, for every anchored row on the board.** |
| **S55** | 2026-08-04 (PREMORTEM Lens 2) | → 2026-08-11 settle | **FIRED-C** | 2026-08-12 HANDOVER §2b | `HO=F` **+13.828%** − `CL=F` **+10.611%** = **+3.217pp**, inside the −3.0 / +6.5 band (registration state −2.953pp). ⇒ **the physical-vs-war-premium cause STAYS UNSEPARATED and `R47` stands: no stage may state "the distillate bottleneck released" as fact.** ★ **The economically loud fact sits inside branch C: BOTH legs rallied double digits**, which is the whole-barrel signature the row was written to detect — pointing weakly at B without reaching it. **Both bars re-pulled in full at scoring (D140).** |
| **S56** | 2026-08-04 (PREMORTEM Lens 2) | → 2026-08-11 (3 sessions from the 08-05 settle) | ★★★ **FIRED-A, by 24pp** | 2026-08-12 HANDOVER §2b | SPCX 3-session excess vs SPY, 08-05 settle → 08-10 settle = **+27.722pp** (108.27 → 138.74) against a +3.5 line. ⇒ **the counted short (219.3M sh ≈ 34% of public float) beat the counted supply (up to 911.5M sh) decisively.** ★★ **This threatens a METHOD conclusion, as registered: `D6` ("positioning is not a signal") survives for *percentile* positioning and is measured WRONG for *share-counted* positioning. PREMORTEM owns writing the scope limit; the rule is not overturned by one event.** ⚠⚠ **The D149 invalidation check (lock-up waiver / secondary / index inclusion) COULD NOT BE RUN — it requires the news path, which PREFLIGHT G1 revoked. The verdict is recorded WITH that gap named, not laundered.** ⚠ **S1: σ rests on 32 overlapping windows over 35 post-IPO sessions with no unlock in sample — the weakest estimator on this board, as disclosed at registration.** |
| **S57** | 2026-08-04 (PREMORTEM Lens 2) | → 2026-08-12 (branch A at ANY settled close through) | ★★ **FIRED-A (against the tilt)** | 2026-08-12 HANDOVER §2b | `XLB` 5-session excess vs SPY crossed the +1.9 line on **two** settled closes: **+2.227 (08-10)** and **+2.484 (08-11)**; path −4.762 → −3.789 → −2.596 → +1.307 → +2.227 → +2.484. ⇒ **Materials outperformed while the dollar fell (`DTWEXBGS` 119.5977 → 119.0649) and copper net-spec hit the 100th percentile ⇒ MATR UW− loses BOTH of its stated legs.** ★★★ **And `S57-ANNEX`/`ANNEX-2`'s NEM-contamination concern was TESTED and did not hold**: ex-NEM cap-weighted **+1.203**, equal-weighted **+0.908**, **8 of 12 names positive**, NEM only **11.6%** of sector cap ⇒ **P44's own registered anti-signal fired and P44 is scored MISS** (MACRO §F). ⚠ **ROTATION nonetheless DECLINED the promotion** on the `top1_flips_sign` rule (LIN 24.7%) and on `eqflow` decaying +0.040 → +0.018 ⇒ **the tilt ran without a falsifier until `S77` replaced it the same day.** |
| **S58** | 2026-08-05 (human-execution loop) | → 2026-08-11 | **FIRED-C** | 2026-08-12 HANDOVER §2b | MET cumulative excess vs SPY over the first 3 settled sessions after the 08-05 AMC print (08-06 · 08-07 · 08-10) = **+3.993 → +1.118 → +0.379pp**, inside the −2.70 / +2.45 band. ⇒ **the print carried NO information for the thesis**, and the row's own registered meaning applies to the desk rather than the market: *"the price of entering a binary one-way is that risk was taken to learn something we did not need to know."* ★ It **touched +3.99 on day 1 and gave it all back** — a within-window path a single endpoint hides. |
| **S60** | 2026-08-05 (human-execution loop) | → 2026-08-11 settle | ★★ **FIRED-A (the SALE was wrong)** | 2026-08-12 HANDOVER §2b | `XLE` 5-session excess vs SPY, 08-04 settle → 08-11 settle = **+4.218pp** ≥ the +3.90 line (path −1.993 → +2.616 → +4.218). ⇒ **the 2026-08-04 XLE liquidation was wrong on its own observable**: the integrated complex re-rated, the *"denominator artifact"* reading did not hold, and **"unmeasurable ⇒ sell" cost something measurable.** ⚠ **The row's registration disclosed its own bias (estimator centred +0.332, so A is the structurally easier branch) — carried WITH the verdict and it does not change it: +4.218 clears the measured 85th percentile.** ★ **This is the desk's substitute for the execution-scoring ledger it does not have (`D159`), and the substitute came back negative.** |
| **S65** | 2026-08-06 (PREMORTEM Lens 2) | → 2026-08-11 settle | **FIRED-C** | 2026-08-12 HANDOVER §2b | Median RS20 vs SPY of {JPM, BAC, WFC, BRK-B} at the 08-11 settle = **+2.871** (JPM +3.09 · BAC +3.08 · WFC +0.04 · BRK-B +2.66), inside +0.34 / +6.81. ⇒ **the velocity-lit breadth that carried the 08-06 FIN promotion NEITHER converted NOR collapsed through the binary — the promotion is neither validated nor falsified on the axis it was made on.** ★ **The BRK-B contamination pre-commitment is fully DISCHARGED**: ex-BRK-B median **+3.084** vs headline **+2.871** = a **0.21pp** gap ⇒ **branch C cannot be attributed to BRK-B in either direction.** ⚠ Its unresolved question is re-armed as **`S78`** on the same basket with fresh bands. |

**Not scoreable this run, named rather than dropped**: **S59 · S61 · S72** (all settle at the **08-12**
close, which has not occurred at this clock) · **S73** (its equity leg settles tonight; its **macro leg
settles at the first `[FRED]` close covering 08-12, which on the measured publication clock is
≈08-13/08-14, NOT tomorrow**) · **S63 · S64 · S67 · S68 · S69 · S71** (→ 08-13) · **S74** (→ 08-24).
🚨🚨 **`S8` remains undated `[blank]` and un-scoreable for a TENTH consecutive run — a human must VOID
or re-register it (P5). Named again, not dropped.**
**`EXPIRED` = 0 · silent skips = 0 · past-dated rows unscored = 0.**

---

## MASTER INDEX — appended 2026-08-12 by the `industry_US` run

> IDs checked at **WRITE time** (D137 / D76 / M319) against EVERY row in **all three** `SCENARIOS*.md`
> **and** both `STANDING_VIEW*.md` **and** `RESEARCH.md`: `grep S75` / `S76` / `S77` / `S78` returned
> **0 in all nine files**; highest existing was **S74 (US) / S57-KR (KR)** ⇒ this run took **S75 – S78**.
> ★ **All four bracket TILT CHANGES MADE BY THIS RUN** — the protocol's rule that a changed tilt without
> a falsifier is a one-way bet, applied to the desk's own three deltas plus the one decline that left a
> live tilt uncovered.

| ID | Owner | File | One line |
|---|---|---|---|
| **S75** | US | `SCENARIOS_US.md` | **ENRG N+ → OW− promoted today.** `XLE` 5-session excess vs SPY at the **08-19** settle: **A ≤ −3.60 · B ≥ +3.94** (D93 mean +0.280 · sd 3.815). State **+4.218 — already above B, disclosed**; **A is the adversarial ask at 2.05σ** |
| **S76** | US | `SCENARIOS_US.md` | **HLTH N → N+ promoted today on a breadth artifact.** **TWO legs scored independently** — leg 1 `XLV` exc5 (**A ≤ −2.67 · B ≥ +2.62**); ★ **leg 2 = the HLTH count at `OBV 매집 ∧ RS20>0` (A ≤ 10 · B ≥ 22 of 32, anchored on today's 18)** — the leg that tests the *mechanism* the promotion was argued from |
| **S77** | US | `SCENARIOS_US.md` | ★★★ **MATR's REPLACEMENT falsifier.** S57 fired twice and the N− was carried anyway. **EW 5-session excess vs SPY of the 11 NON-NEM `us_top300` Materials names (listed in full): A ≥ +2.03 forces a tilt change · B ≤ −2.04 is the UW's first NEM-free confirmation.** **The most nearly centred estimator of the four (A 0.52σ · B 1.38σ)** |
| **S78** | US | `SCENARIOS_US.md` | **FIN N+ → N demoted today on `eqflow` while S51 CONFIRMED its mechanism.** Median RS20 {JPM,BAC,WFC,BRK-B} at 08-19: **A ≥ +4.68 (the demote was wrong) · B ≤ −5.65**. Deliberately re-uses S65's basket — its question settled **C = unresolved, not answered** |

**Count: 92 brackets — 66 US-owned · 26 KR-owned.**
⚠⚠ **The shared-counter proposal for a human now stands for an EIGHTEENTH run.**
★ **This run's own ID hygiene, stated with its cost**: `handoff_id_audit` reported **max M559** because
**the 2026-08-10 `industry_US` run's writeback reached only TWO of five handoff files** — its facts,
digs, retractions and asof entry never landed (see this run's `HANDOVER.md §5`). **This run rescues
them**, which forced a renumbering of **its own** MACRO facts from M573–M580 to **M580–M587**; the
correction is appended visibly to `MACRO_REPORT.md §I-CORRECTION` rather than silently applied.

---

## MASTER INDEX addendum — registered by the **2026-08-12 `industry_US` RUN-2** (post-CPI-print, pre-open)

> ⚠ **Second `industry_US` run of 2026-08-12.** RUN-1 (10:50–11:47 KST) closed with the July CPI still
> ~10h away; RUN-2 (22:10–23:40 KST) ran **53 minutes after the print and 7 minutes before the cash
> open.** All RUN-2 outputs are **append-only addenda** to RUN-1's files — nothing was overwritten.

| ID | Owner | File | One line |
|---|---|---|---|
| **S79** | US | `SCENARIOS_US.md` | ★★★ **NVDA 2026-08-26 — the binary RUN-1's DRIFT surfaced as un-bracketed and handed forward; it is now INSIDE the `CATALYST_WATCH` 14-day window.** **TWO legs scored independently.** **Leg 1 (the name)**: NVDA 1-session excess vs SPY on the **08-27** settle — **A ≥ +5.0pp · B ≤ −5.0pp · N between** (D93 mean −0.081 · sd 2.028 ⇒ **±2.5σ**, each tail fired **1/60 = 1.7%**). ★ **Leg 2 (the risk unit — the informative leg)**: same session, AVGO and TSM excess vs SPY — **U-ONE** (both same sign as NVDA **and** ≥2.0pp) · **U-SPLIT** (NVDA ≥5.0pp while both peers <2.0pp) · **U-MIXED**. **Leg 2 converts PREFLIGHT G4's three-run-old window artifact — `{AVGO,NVDA,TSM}` merges at 500/750d, splits at 250d — into one dated observation.** Anti-signals: print moved ⇒ VOID · 08-27 halt ⇒ VOID · **a separate ≤48h macro binary on 08-26/27 ⇒ Leg 2 AMBIGUOUS** (a macro shock counterfeits U-ONE) |

**Count: 93 brackets — 67 US-owned · 26 KR-owned.**
⚠⚠ **The shared-counter proposal for a human now stands for a NINETEENTH run** — and RUN-2 adds a
**new instance of the same defect class**: `handoff_id_audit` reports **`D233`–`D236` declared twice**,
once by today's `industry_kr` block (`D231-KR ~ D237-KR`) and once by today's `industry_US` block
(`D227–D236`). **Two desks allocated dig numbers from one counter on the same date.** M-side: **153
colliding ids, max M587**, of which **M561–M572** is the 08-10-rescue-vs-today collision RUN-1
documented in `MACRO_REPORT.md §I-CORRECTION`; the **M22–M256** bulk is the known 2026-07-29
split duplication.

> ⚠⚠ **CORRECTION to the RUN-2 index block immediately above (D48 — left visible, not rewritten).**
> That block states *"`D233`–`D236` declared twice… **Two desks allocated dig numbers from one counter
> on the same date**."* **That is FALSE.** `handoff/RESEARCH.md` registers the KR rows as
> **`D231-KR`…`D237-KR` (suffixed)** and the US rows as **`D233`–`D236` (unsuffixed)** — **two
> correctly-formed namespaces, no shared counter.** `handoff_id_audit` parses the `##` range header by
> its numerals and **drops the `-KR` suffix**, producing a false-positive collision. **The defect is
> the audit tool's and is registered as `D240`.**
> ✅ **The `M###` half of that block STANDS** (153 colliding ids, max **M587**, `M561`–`M572` = the
> 08-10-rescue overlap, `M22`–`M256` = the known 2026-07-29 split duplication) — **those are
> same-namespace collisions.** ⚠ **RUN-2 asserted the collision before opening the file; that is this
> desk's dominant failure mode reproduced inside the stage that catalogues it.**


---

## Scored by the 2026-08-13 `industry_kr` run (appended to the MASTER scoring log — the log stays shared and un-split)

| id | 정산 | 판정 | 관측값 (동결된 것 그대로) | 임계값이었던 것 |
|---|---|---|---|---|
| **S56-KR** | 2026-08-12 | **`FIRED-A`** | `069500.KS` 벤치 일간 초과의 차 = (000660 초과)−(005930 초과). **08-10 제외**(안티시그널 (ii) 발화: 000660 조회공시요구·답변, DART 1차 확인) · **08-11 −3.778** · **08-12 −1.137**(000660 +5.544% / 005930 +6.681% / 벤치 +4.015%) ⇒ **유효 2세션 전부 음(−)** | **A = 3세션 중 2세션 이상 차<0** · 안티시그널 (ii) 의 «남는 세션 2개 미만이면 VOID» 는 **2개 남아 미발화** |
| **S38** | 2026-08-12 | **`PENDING-DATA` (2런 연속)** | 006360 KRX 공매도잔고 **최신 4.71%(08-10)**, 08-12 값 **미인쇄**. ★ **공표 지연을 이번에 실측했다: T+2 정착세션**(08-12 조회 시 마지막 08-07 · 08-13 조회 시 08-10) ⇒ **08-12 잔고는 2026-08-14 인쇄** | A ≤2.00% / B ≥5.00% — **밴드 불변, 대체 관측값 없음.** 현재 **B까지 0.29pp**, 추세 `building(+0.81)` |
| **S48-KR** | 2026-08-12 | **`PENDING-DATA` (2런 연속)** | 006340 KRX 공매도잔고 **최신 3.36%(08-10)**, 08-12 값 미인쇄. 같은 T+2 지연 | A ≤2.50% / B ≥5.50% — 밴드 불변. 추세 `covering(−0.10)` |
| **S8** | `[blank]` | **정산 불가 — KR 데스크가 이 사실을 적는 것이 11번째** | 무날짜 등록이라 정산 조건이 존재하지 않는다 | **KR 은 판정할 수 없다(P5).** 사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다 |

**`EXPIRED` = 0 · 조용한 생략 = 0.**
⚠ **오늘의 정산 실패 2건(S38·S48-KR)은 시장이 아니라 등록 문법이 만든 것이고, 이번 런이 그 결함의 수치를 확정했다**
(`D231-KR` 의 수리값 = **KRX 공매도잔고 T+2**). **다음 KR 런이 첫 채점 기회다.**

## MASTER INDEX — appended 2026-08-13 by the `industry_kr` run

| id | owner | file | 한 줄 |
|---|---|---|---|
| **S60-KR** | KR | `SCENARIOS_KR.md` | S60-KR — 전력망 업무협약이 60일 안에 수주 공시로 전환되는가 (→ 2026-10-12) |

---

## Scored by the 2026-08-13 `industry_US` run (appended to the MASTER scoring log — the log stays shared and un-split)

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, held.
> Run clock **2026-08-13 09:10–10:20 ET (pre-open into the first hour)**. Every settlement below uses
> the **2026-08-12 settled close**; **no 08-13 bar is used anywhere** (D74). Prices re-pulled in full
> at scoring (D140): `yfinance`, `auto_adjust=False`, benchmark named inline (C1).

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S59** | 2026-08-05 (human-execution loop) | → 2026-08-12 | **FIRED-C** | 2026-08-13 HANDOVER §2a (industry_US) | `NDAQ − XLF` 10-session cumulative, **2026-07-29 → 2026-08-12**: NDAQ **+0.115%** vs XLF **+2.188%** = **−2.073pp**, inside the −5.17 / +4.43 band. ⇒ **the slope-dominant exchange name UNDERPERFORMED its own sector across a window containing both NFP and CPI, but not far enough to falsify M363's β +33.2.** ★ **Scoreable despite the FRED gap**: the 2s10s direction is a qualifier on branches A and B only, and the observable landed **between** them ⇒ C fires on either 2s10s path. ⚠ The row's own text predicted C would be frequent *because the mechanism is conditional* — **it was, for that reason, not a new one.** |
| **S61** | 2026-08-05 (PREMORTEM Lens 2) | → 2026-08-12 | **FIRED-C** | 2026-08-13 HANDOVER §2a | EW{`STNG`,`FRO`} 5-session cumulative excess vs `SPY`. Path: 08-05 −9.863 · 08-06 −2.472 · 08-07 −4.184 · 08-10 **−4.711** · 08-11 −2.411 · **08-12 +3.174**. **Branch A (≥ +6.80 at ANY settled close) never reached** (max +3.174); **branch B (≤ −4.19 at the 08-12 close) not met** — the terminal value is **positive**. ⇒ **no Red Sea war-risk premium appeared in tanker equities; `D168` stays named-but-inert.** 🚨 **CONSTRUCTION FINDING → `D242`: branch B WAS satisfied at the 08-10 close (−4.711 ≤ −4.19), but B settles only on the terminal bar while A settles on ANY bar.** The asymmetry is in the frozen text and is **honoured — no threshold was improvised.** ⚠ Instrument disclosure repeated: **STNG/FRO are outside `us_top300`**, so this is a hand-built series with no flow/RS/short row. |
| **S72** | 2026-08-08 (PREMORTEM Lens 2) | → 2026-08-12 | 🚨 **AMBIGUOUS — by its own PRE-REGISTERED rule, not by a scorer's choice** | 2026-08-13 HANDOVER §2a | 1-session excess vs `SPY` on the 08-12 CPI close: **XLI −0.154 · XLF −0.043 · XLB −1.490 · XLU +0.231 · XLE −0.086.** **THREE of five legs read \|excess\| < 0.20pp** ⇒ the row's own clause fires verbatim (*"any leg reading \|excess\| < 0.20pp is recorded as `flat` and the row scores AMBIGUOUS rather than being forced into a sign"*). ★★ **This is the desk pre-registering its own failure mode and the failure mode arriving on schedule.** The only two non-flat legs — **XLB −1.490 and XLU +0.231 — carry OPPOSITE signs** ⇒ **neither MACRO's three-tilt grouping nor Lens 2's four-tilt grouping gains support. The question is NOT answered and must not be reported as C.** ⚠ Anti-signals (a) CPI delay and (b) an intraday halt **did not fire**; the AMBIGUOUS is structural, not a VOID. |
| **S73 · Leg 2 (equity)** | 2026-08-10 (PREMORTEM Lens 2) | → 2026-08-12 close | **NEITHER equity branch fired** | 2026-08-13 HANDOVER §2a | **H-equity**: median 1-session excess vs SPY of {JPM **+0.617**, BAC **+1.015**, XLI **−0.154**} = **+0.617**, against a **≤ −1.50** line ⇒ not fired. **C-equity**: `XLU` **+0.231**, against **≥ +2.00** ⇒ not fired. ⇒ **the July CPI produced no tail equity reaction in either direction.** ★ **Leg 2 did exactly the job it was registered for** — it settled on the CPI session itself and **could not be blocked by the FRED lag that is once again blocking Leg 1.** ⚠ Its registration pre-stated that Leg 2 is *"a directional CONFIRMATION, not a second discriminator"* ⇒ **a null Leg 2 is NOT evidence that Leg 1 will be null.** |

**Not scoreable this run, NAMED rather than dropped:**
- **S73 Leg 1 (macro)** — 🚨 **`PENDING-DATA`, exactly as the row pre-declared.** `[FRED]` publishes
  `DGS2` · `DGS10` · `BAMLH0A0HYM2` through **2026-08-11 only**; the 08-12 CPI-day close is
  unpublished. The row's own text: *"the first FRED close covering 08-12 may not print until
  08-14–08-18. That is NOT grounds to re-date it."* **Band unchanged.** ★ The lag is now measurably
  **shorter** than when the row was written — **1 session, not the 3–4** that blocked four runs
  (`T10YIE` already prints 08-12 at **2.26**, −1bp).
- **S63 · S64 · S67 · S68 · S69 · S71** — all six settle on the **2026-08-13 SETTLED CLOSE**, which
  was ~20 minutes in the future at this run's clock. **Re-read at source this run to confirm none
  settles earlier.** ⚠⚠ **The next `industry_US` run inherits SIX settlements at once — the largest
  scheduled batch on this board.**
- **S74** (→ 08-24) · **S75 · S76 · S77 · S78** (→ 08-19) · **S79** (→ 08-27) — ARMED.
- 🚨🚨 **`S8` remains undated `[blank]` and un-scoreable for an ELEVENTH consecutive run by this desk.
  A human must `VOID` it or re-register it with a date (P5). Named again, not dropped.**

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows left unscored = 0.**

⚠ **Two live rows are measuring the wrong object, found by this run's PREMORTEM and recorded WITHOUT
moving either band** (`D249`): **`S64`** scores **`XLI`** while the actual INDU position is **defense**
(defense EW exc20 vs SPY **+7.81** vs XLI **+0.89**; corr(defense, XLI) **0.48**), and **`S63`**
brackets **UTIL+RE+FIN** while the measured third leg on 252 days is **STPL** (`XLU–XLF` **0.24**) —
⚠ though the 60-day window reads `XLF`–complex **0.70**, so this is also a **C5 window-choice** problem.
**Both settle tonight on their frozen text.**

⚠ **One live row is graded NO-INFORMATION before its own settle** (`D248`): **`S71`**'s branches are
symmetric in σ (+0.97σ / −1.04σ, firing ~14.7% / ~14.3% of 252) but **asymmetric in practice** — its
08-12 base bar (+0.231) makes branch A a **6.0%** event and branch B a **10.3%** event, so **the
against-us branch is 1.7× harder to fire.** Its differencing also inflated sd by **√2** and induced
negative autocorrelation. **The band is NOT moved; `S80` replaces its job on a 4-session window.**

---

## MASTER INDEX — appended 2026-08-13 by the `industry_US` run (PREMORTEM registrations)

> IDs checked at **WRITE time** (D137 / D76 / M319) against EVERY row in **all three** `SCENARIOS*.md`
> **and** both `STANDING_VIEW*.md` **and** `RESEARCH.md`: `grep S80` / `S81` / `S82` / `S83` returned
> **0 in all nine files**; highest existing was **S79 (US) / S60-KR (KR)** ⇒ this run took **S80 – S83**.
> ★ **Every band was MEASURED on a trailing-252 distribution by the registering run**, and every
> magnitude threshold is stated against a measured implied move (`module_flow --positioning`, this run).

| ID | Owner | File | One line |
|---|---|---|---|
| **S80** | US | `SCENARIOS_US.md` | ★★★ **Is the UTIL/RE/STPL underweight ONE duration bet, and is it right?** EW{XLU,XLRE,XLP} **4-session** excess vs SPY at the **08-19** settle: **A ≥ +1.85 (against us — all three UWs wrong together) · B ≤ −2.29 (first multi-session confirmation)**. D93: mean −0.245 · sd 2.068 ⇒ ±1.0σ, **A 15.5% · B 13.1% · no-settle 71%**. State **−0.408**. **Replaces `S71`'s job**, which was graded no-information before its own settle |
| **S81** | US | `SCENARIOS_US.md` | ★★ **NVDA 08-26 READTHROUGH, with NVDA deliberately EXCLUDED.** EW{AVGO,ANET,HPE} **2-session** excess vs SPY, 08-25 → **08-27**: **A ≥ +3.66 · B ≤ −2.86 (the book's 4-of-11 concentration is ONE correlated loss)**. D93: mean +0.403 · sd 3.258. ★ **Band size = the measured beta**: β(basket~NVDA) **0.35 (252d) / 0.33 on top-decile \|NVDA\| days (n=26)** ⇒ a 10% NVDA gap maps to ~3.3pp. **Converts PREFLIGHT G4's four-run-old window artifact into one dated observation** |
| **S82** | US | `SCENARIOS_US.md` | ★★★ **The highest-information row on the board: two lenses of THIS pre-mortem disagreed about HLTH and this settles it.** [XLV 5-session excess vs SPY] MINUS [EW{XLU,XLRE,XLP} 5-session excess vs SPY] at the **08-20** settle: **A ≥ +2.45 (idiosyncratic med-tech leg — the zero-exposure GAP is real) · B ≤ −1.62 (HLTH is the 4th leg of a factor we are UW three times ⇒ the tilt set is internally inconsistent)**. D93: mean +0.414 · sd 2.065. State **+3.091 — already above A, DISCLOSED; B is the adversarial ask** |
| **S83** | US | `SCENARIOS_US.md` | ★★ **The book holds ANET and HPE as one AI-compute position — are they?** [ANET 5-session excess vs SPY] MINUS [HPE 5-session excess vs SPY] at the **08-20** settle: **A ≥ +7.16 · B ≤ −9.68**. D93: mean −1.260 · **sd 8.417 = the widest estimator on this board, DISCLOSED at registration ⇒ C is the heavy favourite**. Registered anyway because the desk sizes the two as one theme and **no row tests that** |

**Count: 97 brackets — 71 US-owned · 26 KR-owned.**
⚠⚠ **The shared-counter proposal for a human now stands for a TWENTIETH run.**
★ **This run's own ID hygiene**: `handoff_id_audit` reports **max M612 · 153 colliding M ids** (real,
same-namespace) and **D237–D241 "declared 2×"** — 🚨 **the D-side collisions are FALSE POSITIVES and
this run OPENED `RESEARCH.md` BEFORE saying so**, which is the correction 08-12 RUN-2 had to make in
place. `RESEARCH.md:1948` declares `D231-KR ~ D237-KR` (suffixed) and `:2045` declares `D237–D241`
(unsuffixed): **two correctly-formed namespaces**, i.e. `D240` reproducing. **This run takes
`D242`–`D251` unsuffixed**, the range the 2026-08-13 `industry_kr` run explicitly reserved for this
desk at `RESEARCH.md:2075`.

---

## Scored by the 2026-08-13 `portfolio_US` desk (appended to the MASTER scoring log — the log stays shared and un-split)

> **Run clock: KST 2026-08-14 00:00 = ET 2026-08-13 11:00, Thursday — the US cash session is OPEN
> and has ~5h to run.** Seven rows were handed to this desk to score "on the 2026-08-13 settled
> close". **That close does not exist yet.** Four of the seven are therefore **NOT SCORED**, and the
> refusal is the finding rather than an omission.
>
> 🚨 **The failure this prevents is registered on this desk in `S63`'s own text**: *"the first
> verification pass accidentally included the LIVE 2026-08-06 partial bar and read DUR −5.336;
> pinning to the 08-05 settle gave −6.197. The 0.86-point gap is D74."* **Scoring the four price
> rows tonight would have reproduced D74 on four rows at once.**
>
> **Mechanical proof the last bar is live, not settled** (last-bar volume ÷ prior-20-session median):
> `SPY` **0.20×** · `XLU` **0.26×** · `XLI` **0.35×** · `ANET` **0.21×**. `HPE` reads 0.81× — **a
> volume-heavy session in progress, not a settled bar**, and it is the one name where the ratio alone
> would not have caught it. ⇒ **the volume test needs the clock beside it; neither is sufficient alone.**
> ★ This desk's own `PREFLIGHT_US.md §G0`, written 09:10 ET the same morning, independently agrees:
> *"Last bar **2026-08-12**, settled."*

| ID | Verdict | Measured | Note |
|---|---|---|---|
| **S63** | ⏸ **NOT SCORED — settle does not exist** | At the **08-12** settle `DUR = −4.009` (XLU −5.394 · XLRE −2.499 · XLF +0.062); anchor −6.197 | **C band, 0.709pp from branch A's −3.3.** ⚠ Its third leg's known defect (C5 — at 252d the leg is STPL, not FIN) is **carried, not resolved**; the row is not re-cut |
| **S64** | 🚫 **VOID — and the VOID is settle-invariant** | **WTI `CL=F` 08-12 settle 83.27**, 08-13 live 81.14, against the row's own base **75.22** | The row VOIDs on *"WTI settled 2026-08-13 ≥ 75.22 ⇒ the discriminating tick never arrived."* Crude would have to fall **−7.3% intraday** to un-VOID it ⇒ **scoreable now.** ★ **`D249` (the row measures XLI while the book's position is defense) is MOOT — the row never scores at all.** Crude **rose 10.7%** over the window the row needed it to fall in. ⚠ Consistent with `R65`: `XLE exc5 +6.140` was best-of-11 for exactly this reason |
| **S67** | ⏸ **NOT SCORED — settle does not exist** | At the **08-12** settle `median{MPC,VLO,PSX} RS20 = +12.656` (MPC +14.059 · VLO +10.488 · PSX +12.656); anchor +5.488 | **C band, 0.904pp below branch B's +13.56** — the *"with us"* branch is within one session's noise. ⚠ **This is the row `SECTOR_ROTATION.md §2b` explicitly deferred the ENRG OW−→OW promotion for.** It settles tonight |
| **S68** | ✅ **FIRED-A** — on the only scoreable leg | **leg (ii): DIS current-year 30-day revision breadth = 1↑ / 7↓ — IDENTICAL to registration** | Branch A is *"leg (i) ≤ +0.29 **OR** leg (ii) still net-negative"*; leg (ii) **is** still net-negative ⇒ **A fires.** **leg (i) stays VOID BY CONSTRUCTION** (`S68-ANNEX`: EA went private 08-04, Form 25-NSE, two zero-volume bars). ⚠ **Read at 11:00 ET, not at the settle — disclosed.** The margin is **6 counts**, so no close can flip it ⇒ **settle-invariant.** ★ The verdict **confirms a withdrawal already made** (ROTATION withdrew the COMM notch on 08-07), so it changes no tilt — but it is the first row this desk has scored on a **count** axis rather than a price axis, and the count axis was the one the promotion did not use |
| **S69** | ⏸ **NOT SCORED — settle does not exist** | At the **08-12** settle `MET RS20 = +2.495` against branch A's line **≤ +2.53** — **0.035pp INSIDE A** | ⚠⚠ **The thinnest margin this desk has carried into a settle.** Companion (C2, quoted not frozen): MET FY 30-day breadth **5↑/9↓ = still net-down**, FY consensus **−0.6%/90d** ⇒ **the revision book is unchanged from registration.** If A fires it fires on a 0.035pp edge and **must be reported with that number attached** |
| **S71** | ⏸ **NOT SCORED — settle does not exist** | 08-12 leg fixed: `XLU` 1-session excess **+0.231**. A needs the 08-13 excess **≥ +1.801**, B needs **≤ −1.459** | ⚠ Registered defect **`D248` carried, band NOT moved**: the +0.231 base makes **A a 6.0% event and B a 10.3% event ⇒ the against-us branch is 1.7× harder.** ★ `S80` (08-19) was registered to replace this row's job on a 4-session window |
| **S73 Leg 1** | ✅ **N — and it is determined by ONE leg** | `hy_oas` **08-12 = 2.71** vs the row's 08-06 anchor **2.71** ⇒ **ΔHY OAS = 0.00** | Branch H needs `ΔHY ≥ +0.10`; branch C needs `ΔHY ≤ −0.05`. **Both are conjunctions and both fail on the HY leg alone ⇒ N, regardless of what `DGS2` prints.** ⚠⚠ **`D212` reproduces for a FIFTH consecutive run and it is why this row looked unsettleable**: `hy_oas` carries **08-12**, `us_2y` stops at **08-11 (4.22)**. ★ **The desk was asking the wrong question** — *"has DGS2 published?"* is not the gate; the row was **already decided by the leg that had published.** ⇒ registered as the general lesson: **on a conjunction bracket, check whether the published leg alone forecloses every branch before waiting on the lagging leg.** |

**Scored 3 (1 VOID · 1 FIRED-A · 1 N) · NOT SCORED 4 (all four blocked by the same missing close).**
⚠ **The four unscored rows settle at tonight's 16:00 ET close and are readable 2026-08-14 morning KST.
They are NOT re-dated** — the observable is anchored, not the calendar (the `S73` treatment).


---

## MASTER scoring log — appended 2026-08-14 by the `industry_kr` run

> ⚠ **이 로그는 시장별로 쪼개지 않는다**(README §2). 아래 첫 행은 **US 소유 행을 KR 런이 채점한 것**이고,
> 그것이 정확히 이 로그를 안 쪼개는 이유다.

| 브래킷 | 등록 | 정산점 | **판정** | 채점 주체 | 관측값 / 근거 |
|---|---|---|---|---|---|
| **S67** (US 소유) | 2026-08-07 `industry_US` PREMORTEM | → **2026-08-13 US 정착 종가** | ✅ **`FIRED-C`** | **2026-08-14 HANDOVER §2-1 (industry_kr)** | **median RS20 vs SPY of {MPC, VLO, PSX} = +11.925** (MPC +12.90 · VLO +10.59 · PSX +11.93; SPY 20일 +3.618%). 밴드 **A ≤−2.20 / B ≥+13.56** ⇒ C 구간, **B까지 1.635pp · A와는 14.1pp**. 08-12 시점 +12.656 → 08-13 +11.925 로 소폭 후퇴. ⇒ **이 데스크의 ENRG 승격은 반증되지도 검증되지도 않았다.** ⚠ **범위(C4)**: 등록문이 *"B 가 발화해도 싸다는 뜻이 아니다"*(컨센이 목표가를 이미 쫓았고 `margin_history` 3종 blank) 라 적었으므로 **C 는 더더욱 아무것도 말하지 않는다.** ⚠ **미실행 점검 명시**: D149 무효화 조건(정유소 특이사건)을 **KR 런은 1차 공시로 확인하지 않았다** — C 판정이라 결론 불변이나 확인하지 않은 것을 확인한 것으로 적지 않는다 |
| **S38** | 2026-07-29 `industry_kr` DEEP-INDU/BET | → 2026-08-12 | ⏸ **`PENDING-DATA` · 3런 연속** | 2026-08-14 HANDOVER §2-2 | 관측값(**2026-08-12 KRX 공매도잔고 %float**)이 오늘도 미인쇄. 08-14 08:37 조회 시 시계열 마지막 행 **2026-08-11**. **T+2 규칙은 3회 독립 측정으로 확정**(08-12→08-07 · 08-13→08-10 · 08-14→08-11)됐고 **틀린 것은 적용 산수**였다 ⇒ **첫 채점 기회 = 2026-08-17(월) 아침.** 현재 거리: **4.89%**, 브랜치 B(≥5.00)까지 **0.11pp**, `building(+0.65)`. **밴드 불변 · 재동결 없음** |
| **S48-KR** | 2026-08-02 `industry_kr` BET/ALPHA | → 2026-08-12 | ⏸ **`PENDING-DATA` · 3런 연속** | 동일 | 006340 최신 관측 **3.62%(08-11)**, 밴드 A ≤2.50 / B ≥5.50 ⇒ C 구간. ⚠ **추세 서술은 창이 정한다**: 10세션 `covering(−0.38)` 이나 **최근 5세션은 3.03→3.62 = +0.59 `building`** — 10세션 창이 07-31 급락(3.91→2.85)을 물고 있다 |
| **S8** (US 소유, 무날짜 `[blank]`) | — | — | 🚨🚨 **정산 불가 · 11번째** | 2026-08-14 HANDOVER §2-3 | **KR 은 판정할 수 없다(P5).** 사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다 |
| — | — | — | ⏸ **US 데스크로 명시 이관 4건** | 동일 | **S63 · S68 · S69 · S71** — 전부 08-13 US 정착에 걸려 있고 관측값이 **US 섹터 ETF·컨센 리비전**(KR preflight 미검사 계기). 날짜 경과 **약 3.5시간**이고 US 런은 오늘 밤 ⇒ **EXPIRED 아님.** 🚨 **오늘 밤 US 런이 이 넷을 안 채점하면 그때부터 EXPIRED 다** — 그 사실을 여기 못박는다 |

**`EXPIRED` = 0 · 조용한 생략 = 0 · 날짜 지난 미채점 = 0**(전부 위 표에 사유와 함께 있다).


## 채점 로그 — appended 2026-08-15 by the `industry_kr` run

> ★ **3런 연속 `PENDING-DATA` 였던 두 행이 오늘 정산됐다.** 08-14 런이 예고한 「첫 채점 기회 = 08-17(월)」보다 **이틀 이르게** 관측면이 인쇄됐다
> (`pykrx get_shorting_balance_by_date` 최종행 = **2026-08-12**, 양 종목 모두).

| 브래킷 | 등록 | 정산점 | **판정** | 채점 주체 | 관측값 / 근거 |
|---|---|---|---|---|---|
| **S38** | 2026-07-29 `industry_kr` DEEP-INDU/BET | → 2026-08-12 | ✅ **`FIRED-B`** | 2026-08-15 HANDOVER §3-1 (`industry_kr`) | 006360 공매도잔고 **5.01% float · `building`** (08-04 4.36 → 08-05 4.42 → 08-06 4.69 → 08-07 4.61 → 08-10 4.71 → 08-11 4.89 → **08-12 5.01**). 브랜치 B = **≥5.00% ∧ still building** ⇒ **두 다리 모두 충족.** ⚠⚠ **레벨 다리 마진 0.01pp — 이 데스크가 정산한 가장 얇은 마진**(직전 최박 S69 0.035pp); `building` 다리는 7세션 중 6세션 상승으로 얇지 않다. **안티시그널 실제로 점검함**: 「국내 주택정책/PF 사건이 전체 건설 버킷을 움직이면 VOID」 — **8·13 부동산대책은 실존하나 관측일(08-12) 다음날**이고, **발표일 08-13 건설 중앙 −0.27% · 양의비율 31% vs 벤치 `^KS11` +3.56% = 초과 −3.84pp (sell-the-news)** 이며, 창 내 움직임은 **12세션 중 10세션 양(+)의 그라인드**로 이벤트 점프가 아니다 ⇒ **미발화, 판정 유효.** 🚨🚨 **그러나 B 에 등록된 의미(*"숏이 이겼다 · 그 🟢 은 깔고 앉은 매집이다"*)는 같은 창의 가격이 반증한다 — 006360 은 07-31→08-12 에 **+50.11%** (벤치 −0.25%). **관측면은 발화했고 인과 서술은 죽었다**(C2). 새 명제 **`M-61`** 이 이를 소유 |
| **S48-KR** | 2026-08-02 `industry_kr` BET/ALPHA | → 2026-08-12 | ✅ **`FIRED-C`** | 동일 | 006340 공매도잔고 **3.53% (`covering −0.38`)** — 밴드 A ≤2.50 / B ≥5.50 ⇒ **C 구간, 정보 없음**(등록문 그대로: *"더 좁은 밴드로 재등록하되 사후에 넓히지 마라"*). **안티시그널 둘 다 실제로 점검함**: ① 구리 `HG=F` 07-31 **6.4360** → 08-12 **6.5970 = +2.50%**(창내 최저→최고 +6.85%) ⇒ **±10% 문턱 미달, 미발화** ② 006340 DART 20일 — 창 **안쪽** 공시는 **반기보고서(08-12)** 뿐, 명시 3클래스(수주·증자·지배권) 해당 없음 ⇒ 미발화. ⚠ **정직하게 남긴다**: 07-31 「최대주주등소유주식변동신고서」+「대량보유상황보고서」가 있으나 **등록 asof(07-31)와 동일자 = 동결 상태의 일부**로 읽었다; 더 엄격한 독법이면 「지배권 이전」에 가깝게 셀 여지가 있는 **판단 호출**이다. ★ **재등록 시 첫 분포 표본**: 이 브래킷이 C5(손 설정)로 선언했던 「2주 변화 분포」의 실측 두 점 = **006340 −0.47pp · 006360 +1.38pp** |
| **S8** (US 소유, 무날짜 `[blank]`) | — | — | 🚨🚨 **정산 불가 · 12번째** | 2026-08-15 HANDOVER §3-3 | **KR 은 판정할 수 없다(P5).** 사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다. **12연속을 프로세스 실패로 명시 기록** |

**`EXPIRED` = 0 · 조용한 생략 = 0 · 날짜 지난 미채점 = 0.**
★ **이 쌍이 만든 것**: 같은 날 정산된 두 크라우디드 숏이 **정반대 공매도 경로**(building +1.38pp / covering −0.47pp)를 걷고 **둘 다 급등**했다(+50.11% / +23.31%, 벤치 −0.25%)
⇒ **공매도 잔고 방향은 이 표본에서 가격에 대해 정보를 갖지 않았다**(n=2, C4). 이는 이 데스크의 **REJECTED 신호 원장(D6)** 의 **첫 KR 자체 실측**이다.


## MASTER INDEX — appended 2026-08-14 by the industry_kr run

> IDs checked at **WRITE time** (D137 3-grep): 기존 최고 **S60-KR(KR) / S83(US)**.

| ID | Market | File | One line |
|---|---|---|---|
| **S61-KR** | KR | SCENARIOS_KR.md | S61-KR — ★★★ 레짐 콜을 처음으로 KR 1차 관측면에 묶는다: 한국은행 **총 수출물가 MoM**(원화 기준), A ≤0.0% / B ≥+3.0% / C 사이, → **~2026-09-14**. 공표 지연 **0 영업일** — D231-KR 이 요구한 칸을 처음 채운 브래킷 |


---

## Scored by the 2026-08-14 `industry_US` run (appended to the MASTER scoring log — the log stays shared and un-split)

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, held.
> Run clock **2026-08-14 22:10–23:3x KST = 09:10–10:3x ET**. Every settlement uses the **2026-08-13
> settled close**; **no 08-14 bar is used anywhere** (D74 — and a live 08-14 bar WAS caught intruding
> mid-run, see `MACRO_REPORT §C`). Prices re-pulled in full at scoring (D140): `yfinance`,
> `auto_adjust=False`, benchmark **`SPY` named inline (C1)**.
> ★ **Method validated before any new number was read**: this pull reproduces the 08-12 anchors
> exactly (XLU −5.394 · XLRE −2.499 · XLF +0.062 · MET +2.495 · PSX +12.656) **and** the KR desk's
> 08-13 numbers exactly (MPC +12.900 · VLO +10.590 · PSX +11.925).
> ★★ **This clears the deadline the 2026-08-14 `industry_kr` run set in this same log**
> (*"🚨 오늘 밤 US 런이 이 넷을 안 채점하면 그때부터 EXPIRED 다"*). **`EXPIRED` = 0.**

| ID | Registered | Event date | Branch fired | Note |
|---|---|---|---|---|
| **S63** | 2026-08-06 (PREMORTEM Lens 2) | → 2026-08-13 | **FIRED-C** | `DUR = (XLU+XLRE)/2 − XLF` RS20 vs SPY: XLU **−6.763** · XLRE **−4.366** · XLF **−0.957** ⇒ **−4.6075**, inside the −9.2 / −3.3 band (**1.308pp from A**, 4.59pp from B). ★ **The PATH is the finding**: the CPI session moved DUR **toward** A (−6.197 → −4.009) and the PPI session moved it **back away** (→ −4.608) ⇒ **the cool CPI began pulling the three tilts together and the split PPI un-did it inside one session** — agreeing independently with `S71`. ⚠ **C4**: C means the question is **not answered**. ⚠ **`D249` carried, NOT re-cut**: at 252 days the measured third leg is **STPL, not FIN**. ✅ Invalidation checked and did not fire; the NEE/Dominion Virginia intervention (`cnbc`+`bloomberg` 08-06) is named as a real in-window event **outside the three specified classes**, and `R40`'s standing note that `D` is a merger-arb security inside `XLU` is re-stated |
| **S69** | 2026-08-07 (PREMORTEM Lens 3) | → 2026-08-13 | ✅ **FIRED-A** | MET RS20 vs SPY **+0.406** against branch A's **≤ +2.53** ⇒ fires, **2.124pp inside**. Companion axis quoted as the row demands (C2): FY consensus **9.79, −0.6%/90d**, FY revision breadth **30d 5↑/9↓** and **7d 0↑/3↓** — **unchanged from registration and still net-down**, so branch A's meaning holds on **both** axes. 🚨 **AND THE QUALIFIER TRAVELS WITH THE FIRE**: RS20 fell **+2.495 → +0.406 = −2.089pp while MET OUTPERFORMED** (MET +0.838% vs SPY +0.698% = **+0.140pp**). The entire move was the **07-16 bar rolling out of the back of the window** (07-15→07-16 was **+1.627% MET / −0.542% SPY = +2.17pp excess**). ⇒ **the observable fired exactly as frozen and no threshold was improvised — but "the flow tag lagged" is measured HERE by a July session leaving the window, not by August weakness.** Registered **`D257`** |
| **S71** | 2026-08-08 (PREMORTEM Lens 2) | → 2026-08-13 | **FIRED-C** | `Δ` = XLU 1-session excess vs SPY on 08-13 (**−0.2415**) minus on 08-12 (**+0.2309**) = **−0.4724pp**, inside the −1.69 / +1.57 band ⇒ **the two prints did not disagree materially.** ✅ **Anti-signal (a)** did not fire — CPI 08-12 and PPI 08-13 08:30 ET both on schedule. ✅ **Anti-signal (b) MEASURED rather than asserted**: the Δ was decomposed across XLU's constituents and **10 of 14 carry a negative Δ** while the two candidate contaminants push the **other** way (`DUK` storm outages **+0.119**, `D` merger-arb **+0.376**); the move is **broad regulated-utility**, driven by `SO −0.808` · `AEP −0.727` · `XEL −1.174` · `PEG −1.246`. ⚠ **`D248` carried, band NOT moved**: the +0.231 base made A a **6.0%** event and B a **10.3%** event ⇒ **C was the heavy favourite before the settle and was graded no-information at registration.** `S80` (08-19) replaces its job |

**Already settled elsewhere and NOT re-scored, named rather than dropped:**
- **S67** ✅ `FIRED-C` — scored by the 2026-08-14 `industry_kr` run; **independently reproduced by this
  run's own pull to the third decimal** (median{MPC,VLO,PSX} RS20 **+11.925**). ⚠ The KR run disclosed
  it did **not** check `S67`'s D149 invalidation at a primary source; **this run checked and it does
  not fire** — no refinery-specific incident filing in-window.
- **S68** ✅ `FIRED-A` (portfolio_US 08-13, settle-invariant at a 6-count margin) · **S64** 🚫 `VOID`
  (settle-invariant; crude **rose 10.7%** over the window the row needed a fall in) ·
  **S73 Leg 1** ✅ `N` (determined by the published leg alone: ΔHY OAS **0.00**).
- **S74** (→08-24) · **S75 · S76 · S77 · S78 · S80** (→08-19) · **S82 · S83** (→08-20) ·
  **S79 · S81** (→08-27) — **ARMED, none past-dated.**
- 🚨🚨 **`S8` remains undated `[blank]` and un-scoreable for a TWELFTH consecutive run by this desk.
  A human must `VOID` it or re-register it with a date (P5). Named again, not dropped.**

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows left unscored = 0.**

## MASTER INDEX — appended 2026-08-14 by the `industry_US` run (PREMORTEM registrations)

| ID | Owner | File | One line |
|---|---|---|---|
| **S84** | US | `SCENARIOS_US.md` | ★★★ **The MANDATORY Hormuz both-sides bracket.** `[XLE exc5] − [EW{XLU,XLRE} exc5]` vs SPY at the **08-21** settle: **A ≤ −3.174 (p15, 15.1%) · B ≥ +5.544 (p95, 5.2%)**. D93 mean +0.634 · sd 3.474. **State +3.880 is ALREADY AT p85**, so B was set at p95 to avoid a zero-information branch. **Branch A falsifies ENRG OW− and four underweights on one tick** |
| **S85** | US | `SCENARIOS_US.md` | ★★★ **The falsifier for the SAME RUN'S IT N→N+ promotion, on the axis the promotion used.** `RSPT − XLK` 5-session, **08-21**: **A ≤ −0.994 · B ≥ +2.046**. **State +1.980 is already above p85 ⇒ the promotion was made at the 85th–95th percentile of its own justifying estimator, DISCLOSED** |
| **S86** | US | `SCENARIOS_US.md` | ★★ **The optical/interconnect layer — 2 of the desk's 6 admissible 🟢, zero exposure, no cycle-registry entry.** `EW{COHR,LITE,CIEN}` exc5 vs SPY, **08-21**: **A ≥ +12.584 · B ≤ −5.948**. **sd 8.998 = the widest estimator on the board, disclosed ⇒ C favoured** |
| **S87** | US | `SCENARIOS_US.md` | ★★ **Are the book's biggest runners EXTENDED-BUT-LIVE or EXHAUSTED?** `EW{DELL,HPE}` exc5 vs SPY, **08-21**: **A ≤ −4.961 · B ≥ +16.143**. State **+12.331**, between p85 and p95 |

**Count: 101 brackets — 75 US-owned · 26 KR-owned.**
⚠⚠ **The shared-counter proposal for a human now stands for a TWENTY-FIRST run.**
★ **Every one of the four states its SETTLEMENT MODE (`TERMINAL` on both branches) — the first
application of `D242`'s remedy on this desk.**

---

## MASTER INDEX — appended 2026-08-15 by the `industry_US` run (PREMORTEM registrations)

> ⚠ Written by **append**, never a whole-file `'w'` rewrite — the **D165** pre-commitment, held.
> ⚠ **ID 3-grep at WRITE time (D137)**: highest existing **S87** (US) / **S61-KR** (KR).

| ID | Owner | File | One line |
|---|---|---|---|
| **S88** | US | `SCENARIOS_US.md` | ★★★ **The falsifier for the SAME RUN'S Energy OW promotion, on the node the promotion trades.** `EW{MPC,VLO,PSX}` 5-session excess vs `SPY`, **08-21**: **A ≤ +0.061 (the 2-year median) · B ≥ +8.144 (p95)**. **State +15.698 = the 100th percentile of two years** ⇒ **B declared NO-INFORMATION at registration** (it tolerates only −7.6pp ≈ 1.7× `MPC`'s ±4.4% implied move); **A is the entire row**, and A is exactly what falsifies a promotion made at the top of its own distribution |
| **S89** | US | `SCENARIOS_US.md` | ★★ **Is Materials' one name exhausted?** `NEM` 5-session excess vs `SPY`, **08-21**: **A ≤ −5.217 · B ≥ +9.658**. State **+3.833 (70th %ile)**. `NEM` carries the board's most extreme exhaustion geometry — **+429% of its 60-day excess earned in the last 20 sessions, days 21–60 = −20.59** — while being the whole of `P59`'s positive case. **sd 6.056 = 2nd-widest estimator this desk has registered ⇒ C is the favourite, disclosed now** |
| **S90** | US | `SCENARIOS_US.md` | ★★ **Is Real Estate's accumulating node early, or 20 sessions old?** `DLR` 5-session excess vs `SPY`, **08-21**: **A ≤ −3.199 · B ≥ +5.223**. State **+2.878 (84th %ile)**. `DLR` leads the 4-of-12 accumulating node that won DEEP Rotating slot 2 — **and its days 21–60 are −9.02 on a +1.64 60-day base**. 🚨 **No implied-move check was pulled for this row and the gap is stated** |
| **S91** | US | `SCENARIOS_US.md` | ★★★ **The consumer binary nobody was bracketing — the week's actual regime event.** `XLY` 5-session excess vs `SPY`, **08-21**: **A ≤ −2.467 (p05) · B ≥ +1.553 (p85)**. State **−1.783 (14th %ile)**. **Branch A was set at p05 rather than the customary p15 because the state already sat below p15** — disclosed at registration. **`sd 1.639` is the narrowest estimator on this desk's board ⇒ both branches reachable ⇒ the most informative row registered today** |

**Count: 105 brackets — 79 US-owned · 26 KR-owned.**
⚠⚠ **The shared-counter proposal for a human now stands for a TWENTY-SECOND run.**
🚨🚨 **`S8` remains undated `[blank]` and un-scoreable for a THIRTEENTH consecutive run by this desk.
A human must `VOID` it or re-register it with a date (P5). Named again, not dropped.**
★ **One candidate binary was considered and DROPPED with its reason** (Navy shipbuilding / foreign-yard
opening) — neither branch would change a conclusion, because the beneficiaries are foreign-listed and
the pure-play `HII` is outside `us_top300`. **Kept as a watch KPI, not minted as a bracket.**


---

## Scored by the 2026-08-16 `industry_kr` run (appended to the MASTER scoring log — the log stays shared and un-split)

| id | event date | verdict | observed | threshold was | effect on the standing view |
|---|---|---|---|---|---|
| — | — | ★ **Condition-check executed on every ARMED row — null result, recorded as a check, not a skip** | **Zero rows past-dated for either desk.** `SCENARIOS_KR.md` opened in full: the nearest is **S51-KR → 2026-08-17 (tomorrow)**, then S52-KR 08-19 · S57-KR 08-20 · S27 ~late-Aug · S58-KR 09-09 · S61-KR ~09-14 · S45 & S54-KR 09-30 · S60-KR 10-12 · S49-KR 10-30 · S34 & S53-KR 10-31 · S59-KR 11-04. `SCENARIOS_US.md` opened: nearest US rows settle **08-19 (S75–S78) · 08-24 (S74) · 08-27 (S79)**. **This run had zero new settled sessions, so no observation window closed.** | — | **`EXPIRED` = 0 · silent skips = 0** |
| **S8** | `[blank]` undated | 🚨🚨 **UNSCOREABLE — 13th consecutive run** | The KR desk cannot rule on it (P5). ⚠ And the observable **moved this week while the bracket stayed undated**: 2026-08-15 「이란, 美호르무즈 소유권 주장에 "과거에도, 앞으로도 우리 땅"」 [asiae, 1 outlet] and 2026-08-14 「'개방도 폐쇄도 아냐'…호르무즈 항로 다층화 '뉴노멀' 형성」 [yonhap, single-source tier]; `CATALYST_WATCH` still carries *Iran 'Strait of Hormuz open' statement* as an **undated 🔀binary** | — | **A human must `VOID` it or re-register it with a date.** Logged as a process failure for the 13th time |
| **M-61 anti-signal ②** (KR, `MACRO_REPORT` proposition, not a SCENARIOS row) | condition-settled | ✅ **NOT FIRED — settled without a new session** | Residual correlation of 006360 × 006340 after removing `^KS11`: **+0.2694** (window 2026-04-15→08-14, **n=83**; betas +0.628 / +1.017) against a threshold of **+0.50** ⇒ branch (a) survives | +0.50 | ⚠ **Both halves recorded (C2/C5)**: restricted to the registration→observation window (07-31→08-12, **n=9**) the same statistic reads **+0.4610 — 0.04 from the line.** The window choice nearly decided the verdict, and short windows manufacture structure (S5) |

## MASTER INDEX — appended 2026-08-16 by the `industry_kr` run

| id | owner desk | file | one-line |
|---|---|---|---|
| **S62-KR** | industry_kr | `SCENARIOS_KR.md` | Transshipment tariffs: the board's fastest narrative finally gets a dated bracket (4 runs overdue) |
| **S63-KR** | industry_kr | `SCENARIOS_KR.md` | Cosmetics: is "ODM vs brand" a real unit or a one-week artifact? |

## Scored by the 2026-08-16 `industry_US` run (appended to the MASTER scoring log ??the log stays shared and un-split)

| id | event date | verdict | observed | threshold was | effect on the standing view |
|---|---|---|---|---|---|
| ??| ??| ??**Condition-check executed on every ARMED row ??null result, recorded as a check, not a skip** | **Zero rows past-dated for either desk.** `SCENARIOS_US.md` opened in full: nearest US settlements **08-19** (`S75`??S78`, `S80`) 쨌 **08-20** (`S82`, `S83`) 쨌 **08-21** (`S84`??S87`) 쨌 08-24 (`S74`) 쨌 08-26/27 (`S79`, `S81`). `SCENARIOS_KR.md` opened (the other market's file is this run's to score if past-dated): nearest **`S51-KR` ??08-17**. ??**The reason is mechanical, not lucky: NO OBSERVATION WINDOW COULD CLOSE, because zero sessions settled.** The KR desk logged the identical null result this morning | ??| **`EXPIRED` = 0 쨌 silent skips = 0** |
| **S8** | `[blank]` undated | ?슚?슚 **UNSCOREABLE ??14th consecutive run** | The US desk cannot rule on it (P5). ??**And its observable moved twice this weekend while the bracket stayed undated**: *"Trump threatens to declare strait of Hormuz 'territory of the United States'"* [`guardian` **08-14**] and ??found by DRIFT after this run's MACRO was written ??***"Iran, Oman home in on Hormuz Strait deal as ship attacks mount"*** [`fortune` **08-15**] with talks **live on 08-16** [`aljazeera`]. `CATALYST_WATCH` still carries it as an **undated ??binary** | ??| **A human must `VOID` it or re-register it with a date.** Logged as a process failure for the 14th time. ??**`S92` was registered this run partly to stop the desk depending on it** |
| **P56 / M653** | condition-settled | ??**PARTIAL RETRACTION ??`R73`** | **Re-measured on the SAME `[FRED]` pull, current window (08-06 ??08-13)**: the spread half **survives and extended** (30y??0y **0.53 ??0.58**), the level half is **refuted** ??**`DGS30` FELL** 5.22 ??5.21, `DGS10` ??bp, **`DGS2` ??0bp (4.25 ??4.15), i.e. NOT "unchanged"** | *"30y??0y widened with `DGS2` unchanged"* | **A BULL steepener, not a term-premium level rise.** `P65` replaces the mechanism and keeps the sign. ??**`S80` (08-19) must be read as a THREE-SECTOR event** ??UTIL/RE/STPL may be one rate bet whose sign just changed. ??Found **on a run with ZERO new sessions**, by re-measuring the window (C1) |
| **P61 쨌 P62 쨌 P63 쨌 P64** | 08-20 / 08-21 | **UNSCOREABLE ??window did not advance** | Every price-anchored KPI settles 08-20 or 08-21 and **no session settled.** Explicitly **not** recorded as "carried favourably" | ??| **Running hit-rate this run: 0 HIT 쨌 0 HALF 쨌 0 MISS 쨌 5 UNSCOREABLE 쨌 1 PARTIAL RETRACTION.** ??**A zero-scored backtest is a finding**: the desk ran a full macro stage and could not move a single scoreboard row |

## MASTER INDEX ??appended 2026-08-16 by the `industry_US` run (PREMORTEM registrations)

| id | owner desk | file | one-line |
|---|---|---|---|
| **S92** | industry_US | `SCENARIOS_US.md` | The mandatory Hormuz bracket ??**widened to a third branch** because B4 showed both Hormuz branches are confirm-only; branch C (a US-brokered halt to Ukrainian strikes on Russian energy infrastructure) is the only one that can falsify the Energy OW |
| **S93** | industry_US | `SCENARIOS_US.md` | The consumer complex: one factor or two? Cross-sectional sign test on `WMT`/`HD`/`TGT` ??registered because the desk's own catalyst instrument carried **zero** of the three prints |
| **S94** | industry_US | `SCENARIOS_US.md` | The cycle registry cannot see the cycles this desk finds ??`cycle_registry.json` has **no entry** for optical/interconnect while `COHR`/`LITE` are IT's only admissible ?윟 and the book holds neither |


---

## Scored by the 2026-08-17 `industry_kr` run (appended to the MASTER scoring log — the log stays shared and un-split)

| id | event date | verdict | observed | threshold was | effect on the standing view |
|---|---|---|---|---|---|
| **S51-KR** | **2026-08-17** | ★ **FIRED-C** (the "missing line" branch) | **The 반기보고서 exists and was filed 2026-08-14** (DART `rcpNo=20260814000827`, inside the registered window "08-14 ± 3 business days", on day one). **Denominator reproduces almost exactly**: segment note 5 gives 1H26 refining OP **1,571,420** and the 1Q 분기보고서 (`20260515000478`) gives **1,039,042** ⇒ **2Q26 = 532,378 백만원** vs the **532,400** the desk scored off a news body — **a 0.0041% difference**. **Numerator does not exist**: the string 「재고관련」 appears **0 times in the entire 3,977,008-character filing**; the nearest filed concept is 재고자산평가손실(환입) **343,126 백만원** (1H26 consolidated, vs 3,355 a year earlier), which is a **lower-of-cost-or-NRV loss charged to COGS — opposite sign, different concept**. | ratio inside [16.4%, 26.4%] = A · outside but <50% = B · **≥50% OR no inventory-gain line = C** | ★ **S47-KR is NOT re-scored (thresholds frozen).** **M-19″'s ratio anchor loses its primary**: the numerator is IR-only and has never been filed. **Anti-signal checked and NOT fired** — 010950 did not change segment basis (정유/윤활/석유화학, identical in 1Q and 1H, no restatement) ⇒ not `VOID`. ★★ **What the bracket actually bought — the measurement it said it wanted**: the dispersion between a KR conference-call figure and its later filing is **not one number, it splits**: **0.0041% where the figure IS filed, and undefined where it is NOT.** ⇒ the operative rule is not "news bodies are unreliable" but **"ask first whether the number exists in the filing at all."** ⚠ **n=1**, one company, one quarter, one figure — not generalizable (C4). ⚠ The 2Q figure is **derived by subtraction from two primaries**, not itself disclosed; both sources are primary but the derivation is stated, not hidden. ⚠ A missing 재고관련이익 line is **not concealment** — it is not a required item of a K-IFRS segment note. |
| **M-69 anti-signal ④** (KR, `MACRO_REPORT` proposition, not a SCENARIOS row) | condition-settled, same run | 🚨 **FIRED — and it killed half of the proposition that registered it, 40 minutes after registration** | Registered condition: *"if another KR refiner's (096770 · GS) half-year segment note shows 2Q QoQ **positive**, branch (b) is retracted."* **Measured**: 096770 SK이노베이션 「에너지 및 화학」 segment OP — 1Q26 **2,368,674** (`rcpNo=20260515001455`) · 1H26 **5,053,621** (`20260814002500`) ⇒ **2Q26 = 2,684,947, QoQ +13.35%.** Against 010950 refining **−48.76%**. | 2Q QoQ > 0 | **Branch (b) — "the −48.8% is refining-margin contraction" — is RETRACTED (→ R74).** Branch (a) — a one-off inventory-valuation effect, consistent with S-Oil's ₩343.1bn 1H26 valuation loss (102× the prior year) — is strengthened. ⚠ **Segment definitions are not like-for-like** (SK이노's "Energy & Chemicals" is wider than S-Oil's "Refining"); the pre-registered wording fired anyway and **was not narrowed after the fact**. ⚠ **The GS half of the anti-signal was unobservable by construction** — GS's half-year segment note has **no refining segment at all** (유통/무역/가스전력/투자및기타; GS칼텍스 is equity-method) → `D272-KR`. |
| — | — | ★ **Condition-check executed on every remaining ARMED row — one row due, one row scored, zero skipped** | **KR past-dated: S51-KR only (above).** Remaining KR ARMED, none past-dated: S52-KR 08-19 · S57-KR 08-20 · S63-KR 08-20 · S27 ~late-Aug · S58-KR 09-09 · S61-KR ~09-14 · S62-KR 09-15 · S45 & S54-KR 09-30 · S60-KR 10-12 · S49-KR 10-30 · S34 & S53-KR 10-31 · S59-KR 11-04. **`SCENARIOS_US.md` opened in full: nearest US rows settle 08-19 (S75–S78) · 08-21 (S93) · 08-24 (S74) · 08-27 (S79) · 08-31 (S92, S94) ⇒ zero US rows past-dated for this desk.** | — | **`EXPIRED` = 0 · silent skips = 0** |
| **S57-KR** | → 2026-08-20 | ⏳ **NOT scored — its observation session did not occur, and today the trigger moved AWAY** | The bracket's frozen observable requires *"the first settled session that knows Hormuz has been reopened."* **Today's event axis carries the opposite**: 「미·이란 '60일 협상시한' 종료…'압박 對 버티기' 경제전 전환」 [yonhap, 4 articles / 2 outlets, 2026-08-17]. Narrative axes cooling with it: `호르무즈` **0.94×** (below 1.0 for the first time) · `국제유가` **0.36× = board low**. | reopening announced | ⚠ **Recorded now so the 08-20 deadline is not met with a surprise: the current trajectory is `EXPIRED-미도래`.** ★ Separately worth carrying: **the two refiners outperformed intraday on a session where the reopening did NOT happen** (010950 +4.76% · 096770 +5.75% vs KOSPI200 front-month +2.34%, **unsettled**) — that is evidence for the bracket's branch-B *direction* but **cannot be used to score it**, because the session does not satisfy the frozen observable. Registered as `M-71`, settling on today's close. |
| **S8** | `[blank]` undated | 🚨🚨 **UNSCOREABLE — 14th consecutive run** | The KR desk cannot rule on it (P5). The undated 🔀binary is still on `CATALYST_WATCH`, and today the axis moved again (the 60-day negotiation deadline expired without a deal). | — | **A human must `VOID` it or re-register it with a date.** Logged as a process failure for the 14th time |

---

## MASTER INDEX additions — registered 2026-08-17 by the `industry_US` run (PREMORTEM)

| ID | Market | File | One line |
|---|---|---|---|
| **S95** | US | `SCENARIOS_US.md` | ★★★ **The MANDATORY D-0 bracket.** The **60-day US–Iran MoU expired 2026-08-17** (5 outlets) and **no existing row was keyed to that date** — `S74`/`S84`/`S92` bracket *Hormuz reopening*, not the expiry, because the date was unknown at their registration; `S8` has carried the same object **undated for fifteen runs**. `BZ=F` at the **08-21** settle: **A ≥ 93.00 · B ≤ 86.50 · C 86.50–93.00 declared NO-INFORMATION at registration and the favourite** (realised 4-session range 87.07–88.98). ★ The row exists because four settled sessions of escalation produced **Brent −0.44%** — the live question is whether the equity complex priced a premium the barrel did not |
| **S96** | US | `SCENARIOS_US.md` | ★★ **The 5th DEEP's own falsifier, registered in the same breath as the promotion.** Three independent instruments picked the optical/interconnect node (`theme_age optical` **1.74×** highest of 13 · `burst` `OPTOELECTRONICS` **z 5.7**, vocabulary-free · a BUILDING Lightmatter thread · the board's **#1/#2 `flow_score`**). `EW{COHR,LITE}` 5-session excess vs `SPY` at **08-21**: **A ≥ +5.0pp with the thread reaching ≥4 outlets · B ≤ −5.0pp**. ⚠ **Both names carry NEGATIVE-to-zero 60-day excess** (`COHR` −13.67 · `LITE` −1.76) — a 20-day phenomenon promoted on a 5-day narrative, and the row says so |
| **S97** | US | `SCENARIOS_US.md` | ★★ **`LHX` succession.** `burst` surfaced `KUBASIK` at a **0% baseline**; the body-read inverted it — **CEO stepped down, insider successor, stock down** (4 outlets, 08-17), on the **only** name negative on both 20d and 60d inside `M704`'s defense EW, whose FINRA short-z was **+1.86 building on 08-14, three days earlier**. 5-session excess vs `SPY` at **08-21**: **A ≤ −4.0pp · B ≥ 0**. ★ Implied move **±3.7% with skew +0.0** — a *neutral* skew on a name that lost its CEO the same day is the row's most interesting input |
| **S98** | US | `SCENARIOS_US.md` | ★★★ **Is the underweight FOUR legs of ONE duration bet, and was its cause already retracted?** The desk is UW Utilities · UW Real Estate · UW− Staples (`S80`) and `S82` asks whether Health Care is a fourth. 🚨 **`R73` withdrew the mechanism underneath all of them** — `DGS2` fell **10bp** while `DGS30` also fell, so it is a **bull steepener**, a tailwind for regulated utilities and long-duration REITs. Sign of the 5-session excess vs `SPY` for `XLU`/`XLRE`/`XLP`/`XLV` at **08-20**: **A all four agree · B they split**. **The highest-information row this run registered** — neither outcome is predictable from anything the desk holds, and A would retire a four-sector tilt |

⚠ **ID allocation, D76 collision class**: greps for `S9[5-8]` were run at WRITE time across
`handoff/*.md`, `llm_outputs/` and `REPORT/` and returned **0 markdown registrations**; highest
existing was **S94 (US) / S63-KR (KR)**.

## MASTER scoring log — entry added by the `industry_US` run of 2026-08-17

| ID | Settle date | Verdict | Observed | Threshold was | Note |
|---|---|---|---|---|---|
| — | — | ★ **Condition-check executed on every ARMED row — one past-dated row found, and it was ALREADY SCORED by the sibling desk** | **`SCENARIOS_KR.md` opened in full**: `S51-KR` was dated **2026-08-17 = today** and this morning's `industry_kr` run had already settled it **`FIRED-C`** ⇒ verified settled, **not assumed**. This is the first non-null result the cross-desk rule has produced in four runs. **`SCENARIOS_US.md` opened in full**: nearest US settlements are **08-19** (`S75`–`S78`, `S80`) · **08-20** (`S82`, `S83`, **`S98` new**) · **08-21** (`S84`–`S91`, `S93`, **`S95`–`S97` new**) · 08-24 (`S74`) · 08-26/27 (`S79`, `S81`) · 08-31 (`S92`, `S94`) ⇒ **zero US rows past-dated.** ★ The reason is mechanical: **zero sessions settled since the prior run** (4th consecutive replay of the 2026-08-14 close) | — | **`EXPIRED` = 0 · silent skips = 0.** 🚨 **`S8` remains undated and un-scoreable for the FIFTEENTH consecutive run** — and its observable moved again today (the 60-day MoU it brackets **expired**), while `CATALYST_WATCH` still carries the Hormuz statement as an **undated** 🔀binary. **A human must `VOID` it or re-register it with a date (P5).** `S95` now brackets the expiry that `S8` could not |

---

## MASTER INDEX additions — registered 2026-08-19 by the `industry_US` run (PREMORTEM, 4-lens fan-out)

| ID | Market | File | One line |
|---|---|---|---|
| **S99** | US | `SCENARIOS_US.md` | ★★★ **Is `ETN` an Industrials position or the book's 5th AI-compute unit?** `ETN`–`ANET` **raw** 60d correlation **+0.722** — higher than `AVGO`–`ANET` (+0.596) and `NVDA`–`AVGO` (+0.495) — while `ETN`–`RTX` raw is **−0.040**. No live row carried `ETN`, and **G4 has failed 10 consecutive runs on exactly this grouping**. `M`=EW{ANET,AVGO,HPE} vs `E`=`ETN`, 5-session excess vs `SPY` at **08-21**: **A** \|M\|≥3.0 ∧ same sign ∧ \|E\|≥1.5 · **B** \|M\|≥3.0 ∧ (opposite sign ∨ \|E\|≤0.5) · **C** \|M\|<3.0 (modal 46.8%, declared). D93: A 29.8/B 17.1/C 46.8. State at registration **M −2.617 · E −3.324, same sign, gate not cleared** |
| **S100** | US | `SCENARIOS_US.md` | ★★★ **Does the STPL UW−→UW promotion survive its own two earnings prints?** `TGT` reports **08-19**, `WMT` **08-20** — both inside the window. The promotion's stated reason ("mega-cap-narrow") is refuted by its own decomposition: `WMT` supplies **+0.129 of the +0.325 Δ at a 28.9% weight** while `TGT` supplies **+0.004 at 1.8%**, so the sector's **best flow name (+0.713)** is invisible to every cap-weighted instrument. EW{TGT,WMT} excess vs `SPY` at **08-21**: **A ≥ +6.5pp · B ≤ −6.5pp** — ★ **thresholds set AT the implied move** (`TGT` ±7.8%, `WMT` ±5.3%, D2) because the proposed ±3.0pp sat inside it |
| **S101** | US | `SCENARIOS_US.md` | ★★★ **Does the `vol_surge` gate cost the desk return? The shortlist tests itself.** `corr(rs60, vol_surge) = **−0.124**` over 299 names; the 9 names clearing the gate average **rs60 −12.7 vs `SPY`** against a universe mean **+2.9**; **18 of the top-20 by `flow_score` are 🟡**; **9 of the 10 strongest erased runners have ZERO mentions in the entire run**. Frozen long-short: EW{10 erased} − EW{8 admitted}, 5-session excess vs `SPY` at **08-26**: **A ≥ +4.45pp · B ≤ −3.88pp** (the measured p85/p15). ★ **D93 mean −0.035 — the first near-zero-centred estimator this desk has registered**, which locates the long-standing bias in the single-leg-vs-`SPY` construction rather than in the estimator |
| **S102** | US | `SCENARIOS_US.md` | ★★★ **Which tenor carries the FOMC minutes?** — a **repair**: `catalyst_calendar` missed the only dated binary in the window, MACRO hand-injected it as `P73`, and **`P73` voided at registration** on its own Warsh anti-signal (§D-1 carries Warsh at 10 articles / 6 outlets). Re-registered with an anti-signal that is reachability-checked and not already fired. `DGS2` + `30y−10y` at **08-21**: **A ≥4.30 · B ≤4.08 ∧ spread ≥0.59 · C** (favourite; realised 9-obs range 4.15–4.25 is entirely inside C). ★ Registered on the measurement that **the four duration-UW legs have NO rate beta** (`XLU` +0.0049 · `XLRE` −0.0072 · `XLP` +0.0224 · `XLV` +0.0185 pp/bp) **while `XLE` has +0.1534** — the desk's only rate-exposed tilt is its overweight |

⚠ **ID allocation, D76 collision class**: `grep` for `S99`–`S103` was run at WRITE time across
`handoff/*.md`, `llm_outputs/` and `REPORT/` and returned **0 markdown registrations**; highest
existing was **S98 (US) / S64-KR (KR)**.

## MASTER scoring log — entries added by the `industry_US` run of 2026-08-19

| ID | Settle date | Verdict | Observed | Threshold was | Note |
|---|---|---|---|---|---|
| — | — | ★ **Condition-check executed on every ARMED row — zero past-dated on the US side, and the reason is a CLOCK, not a frozen tape** | `SCENARIOS_US.md` opened in full: the five rows dated **08-19** (`S75`–`S78`, `S80`) settle on **tonight's** US close, which occurs at 05:00 KST on 08-20 — **after this run ends**. This desk runs pre-market every day, so **a row dated D is always scored by the D+1 run**; written down explicitly so the 08-20 run treats them as **past-due on arrival**. `SCENARIOS_KR.md` opened because it held a past-dated row: **`S52-KR` (08-19)** — **verified already scored** by this morning's `industry_kr` desk as `미결(undecided)` with `S64-KR` reserved as its replacement. | — | **`EXPIRED` = 0 · silent skips = 0** |
| **`S75` `S76` `S77` `S78` `S80`** | 2026-08-19 | ⏳ **PRE-SETTLE readings recorded — the first such readings in six runs, because the tape finally advanced** | At the **08-18** settled close, one session short of settle: **`S75`** `XLE` exc5 vs `SPY` **+4.917** (A ≤−3.60 / B ≥+3.94) — **above B** · **`S76`** leg1 `XLV` **+1.427** (mid-band), **leg2 = 17 of 32** HLTH names on `OBV 매집 ∧ RS20>0` (A ≤10 / B ≥22, anchor 18) · **`S77`** non-`NEM` EW **−3.231 with 10 of 11 negative** (A ≥+2.03 / B ≤−2.04) — **below B, the first NEM-free evidence this UW− has ever had** · **`S78`** median RS20 {JPM,BAC,WFC,BRK-B} **+1.256** (mid-band) · **`S80`** EW{XLU,XLRE,XLP} cum excess **+0.801 raw / −0.387 β-adjusted**, 3 of 4 sessions | frozen at registration, unchanged | ⚠ **Not scores.** ★ `S76` leg 2's supporting measurement: **0 of the 17 accumulating HLTH names clears `vol_surge` 1.2** — `M144`'s 7th replication |
| **`S98`** | → 2026-08-20 | 🚨 **CONSTRUCTION DEFECT recorded BEFORE the settle — branch A is unscoreable** | `S98`'s anti-signal reads *"an **FOMC-dated communication** or a CPI/PPI print inside the window drives all four together ⇒ **VOID**"*, and **FOMC minutes released 2026-08-19, inside its 08-13→08-20 window**. Branch A **is** *"all four carry the same sign."* ⇒ **an A-shaped print satisfies the VOID condition and cannot settle the row.** Only **B** (split) or **C** (3–1) can. | sign agreement, frozen | ⚠ **Thresholds NOT changed** (that would be the improvisation the protocol forbids). ★ **This also refutes this run's own MACRO headline**, which said branch A *"would retire a four-sector tilt"* — it cannot. The **08-20 run must record `VOID` + construction defect on an A-shaped print, not a tilt retirement.** Compounded by `P74`: at the 08-18 close the four legs read **+1.295 / +0.255 / +0.852 / +2.143 raw** (all one sign = A) but **+0.150 / −0.719 / −0.592 / +1.158 β-adjusted** (2-2 split = B) — **the row's own observable cannot distinguish a duration factor from four low-beta sectors in a −1.34% `SPY` tape** |
| **`P73`** (MACRO proposition, not a SCENARIOS row) | 2026-08-21 | 🚨 **VOID AT REGISTRATION — self-inflicted, caught by this run's own PREMORTEM 40 minutes later** | `P73`'s anti-signal named *"a Warsh testimony headline that moves ≥3 outlets"*. **The same report's §D-1 carries "Fed Chair Kevin Warsh testified to Congress" at 10 articles / 6 outlets.** MACRO even wrote *"this anti-signal is already live and is reachability-checked, not decorative"* — **and failed to draw the conclusion that a live anti-signal at registration voids the row.** | ≥3 outlets | **Withdrawn and replaced by `S102`**, whose anti-signal is reachability-checked **and not already fired**. ⚠ Recorded rather than edited away (§4c) |
| **`P65`** (08-16) | → 2026-08-21 | ★ **HALF-BROKEN on new data** | Required `30y−10y` ≥0.58 **AND** `DGS2` ≤4.15. Measured 08-17: **spread 0.59 ✅ · `DGS2` 4.19 ❌.** Over 08-13→08-17 all four tenors ROSE (`DGS30` +10bp · `DGS10` +9 · `DGS5` +6 · `DGS2` +4) — **a BEAR steepener**, not the bull steepener `R73` installed | conjunction, frozen | **Not scored (settle 08-21), but the trajectory inverted.** ⚠ `R73` retracted the term-premium *level* clause on a window ending **08-13**; the two sessions this desk just gained **reverse its refuting half** — `DGS30` 5.21 → **5.31**, above the 5.22 that opened `R73`'s window. **A retraction has an `asof` too** |
| **`P70`** (08-17) | → 2026-08-21 | ⏳ **C — blocked by its own control leg by 0.37pp** | `EW{MPC,PSX,VLO}` exc5 vs `SPY` **+8.886** (4.4× branch A's +2.0 bar) but branch A also requires `BZ=F` 5-session ≤ **+2.0%**, and it printed **+2.37%** | conjunction, frozen | **`P75` registers the replacement discriminator** on the **crack** (`HO=F`×42−`CL=F` **88.41 → 101.96 $/bbl, +13.56**, the **100th percentile of its own trailing 252 sessions**). ⚠ Lens 2 measured the trade-off: `MPC` **+0.2144 pp per $1 of crack / +0.256 pp per 1% Brent** ⇒ **a $6 crack decline costs `MPC` as much as a 5% Brent decline**, so a Hormuz reopening does **not** falsify the refiners unless the crack rolls with it |
| **`P53`** (08-13) | → 2026-08-19 | ★ **SUPPORTED on fresh closes** | *"Materials' broad leg lasted two sessions"* — refuting condition was ex-`NEM` EW exc5 **positive**. Measured **−3.231, 10 of 11 names negative** (was −2.097 on the frozen tape) | positive ⇒ A wrong | Settles tonight with `S77` |
| **`P52`** (08-13) | → 2026-08-19 | ⏳ **A not refuted** | Refuting conjunction was `XLK` exc5 ≤0 **∧** `XLU` exc5 >0. Measured **`XLK` +0.151 ❌ · `XLU` +1.297 ✅** — fails on the `XLK` leg | conjunction, frozen | Settles tonight |
| **`P68`** (08-16) | — | **RETIRED BY CIRCUMSTANCE, not by refutation** | *"Two instruments cannot distinguish no-change from no-observation"* — **cannot recur this run: the tape advanced two settled sessions, 298/299 `flow_score`s moved (median \|Δ\| 0.127, 44 tag changes), and `[FRED]` gained four observations** | — | Recorded so it is not silently dropped |
| **S8** | `[blank]` undated | 🚨🚨 **UNSCOREABLE — 17th consecutive run** | The desk still cannot rule on it (P5). Still carried on `CATALYST_WATCH` as an **undated 🔀binary** — indeed as its **only** row, which is how the FOMC-minutes binary went unbracketed until PREMORTEM caught it | — | **A human must `VOID` it or re-register it with a date.** `S95` brackets the expiry `S8` could not |

**Running hit-rate this run: 0 HIT · 2 HALF (`P65` broken-half, `P70` blocked-half) · 0 MISS ·
4 CARRIED · 1 RETIRED · 1 VOID-at-registration (`P73`) · 1 construction defect (`S98`) ·
5 settling tonight.**
★ **For five runs this table read "UNSCOREABLE — the window did not advance." Today six of nine rows
moved against real data, and the two that moved most both moved AGAINST the proposition that
registered them.**

## MASTER scoring log — second entry added by the `industry_US` run of 2026-08-19 (found by DEEP, after PREMORTEM had closed)

| ID | Settle date | Verdict | Observed | Threshold was | Note |
|---|---|---|---|---|---|
| **`S99`** | → 2026-08-21 | 🚨 **CONSTRUCTION DEFECT recorded ~90 minutes after registration — the premise was a correlation cited without its control** | `S99` was registered on PREMORTEM Lens 2's measurement that **`ETN`–`ANET` raw 60d = +0.722**, "higher than `AVGO`–`ANET` (+0.596) and `NVDA`–`AVGO` (+0.495)", concluding that `ETN` may trade as AI-compute. **Lens 2 never ran the machinery control.** DEEP-INDU ran it and this desk re-measured it independently on the same window: **`ETN`–`CMI` +0.811** and **`ETN`–`CAT` +0.807 — BOTH HIGHER than `ETN`–`ANET` +0.722**, with `ETN`–`EMR` +0.628, `ETN`–`PH` +0.518, `ETN`–`XLI` **+0.764** vs `ETN`–`XLK` +0.731. Joint regression of `ETN` daily returns on `XLI` and `XLK`, 60 sessions to 08-18: **β`XLI` 1.396 (t 6.00) · β`XLK` 0.619 (t 5.12)** — `ETN` loads **2.3× more heavily on Industrials than on Tech**, and both loadings are significant. | \|M\| ≥ 3.0pp ∧ sign(E)=sign(M) ∧ \|E\| ≥ 1.5pp, frozen | ⚠ **Thresholds NOT changed and the row is NOT withdrawn** — it settles 08-21 as registered. What is recorded is that **its branches do not contain the answer**: branch A ("same sign as the AI basket") is satisfied by any common market factor, and `ETN` co-moves with machinery *more* than with AI. ★ **And the inversion is named**: **`RTX`–`XLK` = −0.242** and `RTX`–`ETN` = **−0.040** ⇒ **`RTX`, not `ETN`, is the Industrials position that diversifies the book's AI-compute concentration.** The correct successor test is a **joint-loading** test (β`XLI` vs β`XLK` with standard errors), not a sign-agreement test — to be registered by the desk that settles `S99`. ⚠ This is the **`D48` pattern inside one run at one stage's remove**: PREMORTEM's job is to be the control, and on this row it *was* the uncontrolled claim |
| **`M25`** (STANDING_VIEW anchor, not a SCENARIOS row) | condition-settled, same run | 🚨 **REFUTED on this run's own board → `R81`** | `M25` says *"the US 🟢 tag is a **volume-surge** count, not a flow count — with `velocity` dead, 🟢 requires OBV ∧ RS20>0 ∧ `vol_surge` ≥1.2."* **Measured across all 8 greens: only 3 clear `vol_surge` ≥1.2 (`KKR` 1.32 · `LITE` 1.25 · `CSCO` 1.43). Five (`RTX` 0.83 · `WMT` 0.83 · `ORCL` 0.76 · `MA` 0.84 · `BAC` 0.81) carry `vol_surge` well below the bar and a live `velocity` — the axis G1 revoked.** Cross-check from the other side: 9 names in the universe clear `vol_surge` ≥1.2 and **4 of them are 🟡 and 2 are 🔴** (`COHR` 1.70 🟡 · `MNST` 1.62 🟡 · `SNDK` 1.25 🟡 · `EBAY` 1.20 🟡 · `WEC` 1.45 🔴 · `NKE` 1.40 🔴). | OBV ∧ RS20>0 ∧ `vol_surge` ≥1.2 | 🚨 **`R78` reproduced on the run that claimed to have pre-empted it.** `HANDOVER §1` wrote *"`R78`'s lesson is pre-empted this run: no stage may promote on a tag today"* — and then **SWEEP_READ §1, `SECTOR_ROTATION §2b`/§3 and `EVENT_ALPHA` Card 8 each used the tag.** **Both new-🟢 (`RTX`, `WMT`) are velocity-derived and are withdrawn**; the underlying OBV/RS numbers survive and carry their claims unaided, so **no verdict moves** (STPL's promotion rests on Δ +0.325 and `ex_top1` +0.027, both price-only). Full correction appended to `SWEEP_READ.md`. New dig **`D290`**: `flow_tag` must take the **run-level axis set**, exactly as `flow_score` already does since `D225-KR` — until then the tag and the score disagree about which axes exist |


## Master-index addendum — 2026-08-19 `industry_US` ALPHA stage

| row | owner | registered | settles | where |
|---|---|---|---|---|
| **`S103`** — Does the AI-compute cycle re-accelerate on its own epicenter's print? (`NVDA`, both-sided) | `industry_US` | 2026-08-19 (ALPHA) | **2026-08-29** | [`SCENARIOS_US.md`](SCENARIOS_US.md) |

⚠ **`S103` is registered LOW-RESOLUTION on purpose**: its ±5.0pp bands are **hand-set**, because the
nearest option chain readable at registration expired **08-21**, five sessions before the event. The
obligation to re-derive them from the 08-26-or-later straddle **before the print** is registered as
`D295`. **Scoring it as a measured bracket without that re-derivation would repeat the failure `S100`
fixed inside its own window.**

★ **Process note for the scoring desk**: this row exists because `action_bracket.py` **named the binary
and then reported that there was none** (`D294`). The bracket is hand-written; the script produced no
ticket for it and will not produce one for any single-name earnings binary until its `earnings` axis is
populated. **Do not read an empty `ACTION_TICKETS.md` as "nothing was due."**


---

## MASTER 채점 로그 — 2026-08-20 `industry_kr` 런 (**분할하지 않는 스파인**)

> ⚠ 이 로그는 시장별로 나누지 않는다 — `EXPIRED` 는 어느 쪽에 있든 프로세스 실패이고, 반쪽만 보면 절반이 숨는다.
> ⚠ **오늘 KR 데스크가 US 소유 행 4건을 채점했다.** 소유권은 등록 데스크에 있고 배타성을 주지 않는다(README §3).
> 08-19 KR 런은 *"관측면이 US 정착 종가이고 KST 08~09시엔 아직 오지 않았다"* 로 정당하게 유예했고,
> **US 08-19 정착 종가는 KST 2026-08-20 05:00 에 도착했다 — 유예 사유가 소멸했다.**
> 계산: `yfinance auto_adjust=False`, SPY 마지막 봉 **2026-08-19 769.06** 확인.

| 브래킷 | 소유 | 만기 | 동결 관측값 | 밴드 | **실측** | **판정** |
|---|---|---|---|---|---:|---|
| **S75** | `industry_US` | 2026-08-19 | `XLE` 5세션 초과 vs `SPY` | A ≤ −3.60 · B ≥ +3.94 | **+4.622** | ★ **FIRED-B** — ENRG 승격이 그 축에서 검증됨 |
| **S76** | `industry_US` | 2026-08-19 | leg1 `XLV` 5세션 초과 · leg2 축적 카운트 | A ≤ −2.67 / ≤10 · B ≥ +2.62 / ≥22 | **leg1 +4.742 · leg2 22/32** | ★★ **FIRED-B 양다리** — 가격과 메커니즘이 독립적으로 같은 방향 |
| **S77** | `industry_US` | 2026-08-19 | 非NEM 11종 등가중 5세션 초과 | A ≥ +2.03 · B ≤ −2.04 | **−1.589** | **FIRED-C** — 정보량 없음, 결론 불변 |
| **S78** | `industry_US` | 2026-08-19 | median RS20 {JPM,BAC,WFC,BRK-B} | A ≥ +4.68 · B ≤ −5.65 | **−0.594** | **FIRED-C** — 정보량 없음 |
| **S57-KR** | `industry_kr` | 2026-08-20 | 호르무즈 재개방 첫 정착 세션의 정유 2종 등가중 초과 | A ≤ −6.07 · B ≥ 0.00 | **관측면 미발생** | **`EXPIRED-미도래`** — 브래킷 자기 마감 조항대로 종료 후 **`S65-KR` 로 재등록** |
| **S63-KR** | `industry_kr` | 2026-08-20 | RS60 spread(ODM − 브랜드), **정착 종가** | A ≥ +20 · B ≤ +10 | **D−0 사전관측 +24.2pp** | **정산 미도래**(런이 개장 전). `EXPIRED` 아님 — **다음 런 #1 작업** |
| **S64-KR** | `industry_kr` | (예약) | — | — | — | **미발행 · 사유 기재**(정착 스냅샷 오염 위에 「휴장 흡수 창」을 세울 수 없다) |
| 🚨🚨 **S8** | `industry_US` | **날짜 `[blank]`** | — | — | — | **정산 불가 `17번째 연속`.** 사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다(P5). **17런이면 「대기 중」이 아니라 죽은 행이고, 매 런 같은 줄을 쓰는 것 자체가 비용이다** |

**오늘 만기 도래 총 2건(KR) + 유예 해소 4건(US) = 6건 처리. `EXPIRED` 1건(사유 기재) · 조용한 스킵 `0`.**

### 오늘 이 로그가 남기는 관측 두 개
1. **`S77` 의 −1.589 는 두 이름이 만든다** — STLD **−11.78** · NUE **−8.04**(나머지 9종 중 6종은 ±1.4pp 안).
   **「NEM 을 뺐더니 이번엔 철강 두 개가 지배한다」** ⇒ 소유 데스크(`industry_US`)로 넘기는 관측.
2. **`S76` 의 leg2 는 등록 시점 18/32 → 오늘 22/32** 로 올랐고, **leg1 과 독립적으로** 같은 방향을 가리켰다.
   등록 때 *"leg 2 가 더 높은 정보량"* 이라 적혀 있었고 **그 예측이 맞았다** — 메커니즘 다리를 브래킷한 것이 값을 했다.

### 신규 등록 (2026-08-20 `industry_kr`) — 상세는 `SCENARIOS_KR.md`
- **S65-KR** — `S57-KR` 재등록. **관측면을 「이벤트」에서 「기간」으로 바꿨다**(2026-08-20 ~ 09-19 누적 초과).
  ★ **이벤트 대기형 브래킷은 이벤트가 안 나면 정보량 0 으로 만료된다** — 그 실패를 구성으로 막은 첫 사례.
- **S66-KR** — **오늘 15:30 정착**에 채점되는 2다리 브래킷(지수 수익률 × 유니버스 거래량비 중앙값).
  ★ **임계값이 `1.0/1.2` 같은 둥근 수가 아니라 추정량 자신의 57세션 `p85 = 0.920`** 이다 —
  **이 런이 `R85` 로 반증당한 바로 그 자리에서 나온 교정.**

---

## MASTER INDEX additions — registered 2026-08-20 by the `industry_US` run (PREMORTEM, 4 lenses)

> ⚠ ID 3-grep at WRITE time (`D137`/`D76`): `S104` `S105` `S106` `S107` returned **0 hits** across
> `SCENARIOS*.md` ×3, `STANDING_VIEW*.md` ×3, `RESEARCH.md` and all of `llm_outputs/2026-08-*/`.
> Highest existing was **`S103` (US) / `S66-KR` (KR)**.
> ⚠⚠ **Every straddle readable at registration expired 2026-08-21 (`D1`)** ⇒ implied moves are a
> **floor, not an estimate**, and **no threshold below is claimed to sit outside what is priced**
> (`D295`). ★ Every band is the estimator's own trailing-252 distribution, measured before freezing.

| row | owner | registered | settles | where |
|---|---|---|---|---|
| **`S104`** — July PCE 2026-08-28: does the print move **breakeven** or **real yield**? `T10YIE` 2-obs change 08-27 → 08-31: **A ≥ +3.0bp (against us — the "all real yield" frame is wrong) · B ≤ −3.0bp (frame survives)**. D93: mean −0.07bp, sd 2.60, p10/p90 = ±3.0 ⇒ **A ~10% · B ~10% · C ~80%**. State +2.300. 🚨 anti-signal is **LIVE** (Treasury changed buyback sizes 08-19) | `industry_US` | 2026-08-20 (PREMORTEM L2) | **2026-08-31** | [`SCENARIOS_US.md`](SCENARIOS_US.md) |
| **`S105`** — Google's **$12.2bn / 59m-share warrant to `MRVL`**: structural displacement of a **held** name? `[MRVL exc10] − [AVGO exc10]` vs `SPY`: **A ≤ −10.836 (p15, no displacement) · B ≥ +30.484 (p95, rewrite `AVGO`'s thesis)**. ⚠⚠ **State +25.780 = 93.7th %ile, ALREADY NEAR B — disclosed; A is the adversarial ask.** `MRVL` prints 08-28 **inside** the window, disclosed as a contaminant rather than voided | `industry_US` | 2026-08-20 (PREMORTEM L2) | **2026-09-03** | [`SCENARIOS_US.md`](SCENARIOS_US.md) |
| **`S106`** — Is the **IT underweight** wrong about its own largest reversal? `MSFT` exc10 vs `SPY`: **A ≥ +7.969 (p95, the UW is a sub-node call wearing a sector label) · B ≤ −9.184 (p05)**. State −0.551 = 56.7th %ile, inside C at its own median — **the 20-day shape lives in exc20 not exc10, stated** | `industry_US` | 2026-08-20 (PREMORTEM L1) | **2026-09-03** | [`SCENARIOS_US.md`](SCENARIOS_US.md) |
| **`S107`** — The **`T` orphan** (9.74% of invested, three runs with no bracket) gets its first falsifier. `EW{T,VZ}` exc10 vs `SPY`, **`TMUS` deliberately excluded**: **A ≥ +12.244 (p95) · B ≤ −9.533 (p05, the adversarial ask)**. ⚠ State +7.671 = 92.9th %ile, already above p85 — disclosed | `industry_US` | 2026-08-20 (PREMORTEM L1) | **2026-09-03** | [`SCENARIOS_US.md`](SCENARIOS_US.md) |

### ★ Brackets DECLINED this run, with the reason — so an absence is legible

- **A fourth `NVDA` bracket: DECLINED on information content (B4).** `S79` (the name) · `S81` (the
  readthrough, deliberately excluding `NVDA`) · `S103` (the cycle) already own it, and **no branch of
  a fourth row could change a conclusion those three do not already own.** ⚠ Two obligations restated
  because they are **unmet**: `D295` requires `S103`'s **hand-set ±5.0pp bands to be re-derived from
  an 08-26-or-later straddle before the print** (the readable chain still expires 08-21), and 🚨
  **`catalyst_calendar` / `S79` / `S81` / `S103` / `P79` key the print to 2026-08-26 while `yfinance`
  returns 2026-08-27** — both consistent with an after-close print on 08-26, but **four rows are dated
  against one reading and nothing reconciles them.** Handed to the scoring desk as a check.
- **A fourth duration bracket: DECLINED as a correlated tail.** The pre-mortem's correlated-UW check
  **fired** — `UTIL` and `RE` are bottom-two on `eqflow` (−0.545, −0.252) and **both rallied on price**
  (`XLU` +0.855, `XLRE` +1.568 exc5) — but `S80`/`S82`/`S98` and MACRO `P78` already bracket that
  object. **A fourth row on it would be counting one tail twice.** Routed to DEEP-UTIL instead.

## MASTER scoring log — entries added by the `industry_US` run of 2026-08-20

| ID | Settle | Verdict | Observed | Threshold was | Note |
|---|---|---|---|---|---|
| **`S80`** | 2026-08-19 | **FIRED-C** | `EW{XLU,XLRE,XLP}` **4-session** cumulative excess vs `SPY`, 08-13 → 08-19 = **+1.232pp** (`XLU` −0.045% · `XLRE` −0.288% · `XLP` +0.628% ⇒ EW +0.098%; `SPY` −1.134%) | A ≥ +1.85 · B ≤ −2.29, frozen | ★ **C is not "nothing happened."** The reading moved **+0.43pp toward branch A** from the 08-18 pre-settle (+0.801 raw / −0.387 β-adj) and finished **0.62pp short of falsifying three underweights at once.** The duration complex beat `SPY` by 1.23pp over four sessions **while the desk is short three legs of it.** Recorded, not smoothed |
| **`S82` `S83` `S98`** | 2026-08-20 | ⏳ **DEFERRED — settle has not occurred** | All three settle at the **2026-08-20 settled close**, which arrives **05:00 KST 2026-08-21**, after this pre-market run ends. **Pre-settle readings at the 08-19 close, 4 of 5 sessions in**: `S82` **+4.237pp** (already 1.79pp above branch A's +2.45, and above its own 252d p85 of +2.299) · `S98` **all four legs POSITIVE** (`XLU` +1.089 · `XLRE` +0.846 · `XLP` +1.762 · `XLV` +5.469) = **branch A's shape** · `S83` not computed (pair spread, sd 8.417 = the board's widest estimator; `HPE`'s next print is 2026-09-04, **outside** the window, so its VOID clause does not fire) | frozen at registration | **Not `EXPIRED` — the D→D+1 rule**, written down explicitly by the 08-19 run and applied by the KR desk this morning to `S63-KR`. **Past-due on arrival for the 08-21 run** |
| 🚨 **`S98`** | 2026-08-20 | ⚠ **VOID RECOMMENDED — ruled on the CLAUSE, before the branch** | Its anti-signal: *"an **FOMC-dated communication** or a CPI/PPI print inside the window drives all four together for a reason that is not the duration structure ⇒ **VOID**."* **The FOMC minutes were released 2026-08-19, inside the window 08-13 → 08-20** (this desk's own `S102` opens by calling them *"a dated ≤48h binary"*), and they **read hawkish** — the thread `'Many' Fed officials think higher rates will be needed` peaked at **17 outlets** | — | ★ **Written while the pre-settle points at branch A**, i.e. at the branch that would retire a four-sector tilt. **That is the point of pre-registration**, and the decision is recorded before the observable settles rather than after |
| 🚨 **`S102`** | → 2026-08-21 | ⚠ **VOID RECOMMENDED — and the pattern is the finding** | Its anti-signal: *"an intermeeting Fed policy action or a **Treasury refunding announcement** inside the window."* On **2026-08-19**, inside the window, **Treasury Secretary Bessent announced a doubling of long-dated buyback operations**, and the tape moved on it by name (`Bond Yields Dive After Treasury Increases Buybacks`; `Treasury Yields Fall, Gold Jumps On Bessent Buyback Plan`; MUFG via `fxstreet`: *"the US dollar weakened after… a significant expansion of long-dated Treasury buyback operations"*) | `DGS2` ≥4.30 (A) · ≤4.08 ∧ 30y−10y ≥0.59 (B), frozen | **The clause's LETTER is arguable** (a buyback-size increase is not the quarterly refunding announcement); **its INTENT is met without ambiguity** — the clause exists so a yield move caused by Treasury cannot be scored as caused by the minutes, and that is exactly what happened. 🚨 **`S102` was registered on 08-19 as the repair for `P73`, which self-voided on the identical clause. The repair inherited the defect** ⇒ new dig **`D296`**. **No replacement threshold was improvised on the existing row** (an ambiguous observable is a finding about construction); **`P77` is the successor** |
| **`P52`** (MACRO, 08-13) | 2026-08-19 | ★ **A IS REFUTED — the conjunction holds** | `XLK` exc5 **−2.320** ✅ ≤0 **and** `XLU` exc5 **+0.855** ✅ >0 ⇒ *"the in-line print sent money to growth, not defensives"* is **refuted**; money went to **defensives** | A refuted iff `XLK` exc5 ≤0 ∧ `XLU` exc5 >0 | ⚠ **This FLIPPED between the pre-settle and the settle**: the 08-19 run read `XLK` at **+0.151** and judged the conjunction to fail. One session moved it **2.47pp**. **The whole argument for not scoring on an unsettled bar, in one row** |
| **`P74`** (MACRO, 08-19) | → 2026-08-21 | ⚠ **Direction B tracking = the proposition is WRONG on its own data, AND its own anti-signal fires** | Raw 5-session signs of {`XLU`,`XLRE`,`XLP`,`XLV`} are **4-0 positive**; **β-adjusted (252d) signs are ALSO 4-0 positive** (+0.475 · +1.245 · +1.682 · +4.417) ⇒ raw and adjusted **agree**, which is `P74`'s direction B. Separately its VOID clause — *"`SPY`'s own 5-session return within ±0.5%"* — reads **`SPY` −0.444%, INSIDE the band** | A: raw signs agree ∧ β-adj signs split | ★ **A self-refutation of a proposition this desk registered 24 hours earlier, recorded not edited** (`§4c` / `D48`). **`P78` is the successor and it changes the instrument from a SIGN to a DISPERSION** — the cross-sectional range of the four legs' exc5, because today's 4-0 agreement spans **`XLU` +0.855 to `XLV` +4.742**, a 3.9pp range driven by a drug trial at one end and the board's worst-accumulated sector at the other |
| **`P75`** (MACRO, 08-19) | → 2026-08-21 | 🚨 **CONSTRUCTION DEFECT — ambiguous as written, recorded not resolved** | Branch A requires *"the crack ≥ 95"*. On the **3-2-1** crack the leg **FAILS** (settled 08-19: **67.64**); on the **distillate** crack it **PASSES** (**101.17**). The row's supporting text uses the distillate series (88.41 → 101.96) but its branch says only *"the crack"* | crack ≥95 ∧ EW exc5 ≥+2.0 | **Found by attempting to score it, not by re-reading it.** `P80` replaces it with **both series named explicitly**. The EW leg passes either way (**+5.730**) |
| **`P70`** (MACRO, 08-17) | → 2026-08-21 | ★ **BOTH legs now pass** (not scored — settle is 08-21) | `EW{MPC,PSX,VLO}` exc5 **+5.730** ✅ ≥+2.0 **and** `BZ=F` 5-session **+0.66%** ✅ ≤+2.0% | EW ≥+2.0 ∧ `BZ=F` 5d ≤+2.0% | **The control leg that blocked it by 0.37pp on 08-18 has cleared.** The refiners paid **without** the barrel |
| **`P65`** (MACRO, 08-16) | → 2026-08-21 | **BOTH legs now fail** (was half-broken) | `30y−10y` **0.570** ❌ (<0.58) · `DGS2` **4.190** ❌ (>4.15) | ≥0.58 ∧ ≤4.15 | §A-2 shows why: **both spreads sit BELOW their own 252-obs medians** (2s10s 0.520 vs 0.540; 30y−10y 0.570 vs 0.590) while `DGS30` **5.28** is within 3bp of a one-year high ⇒ **the long end is expensive because the whole curve is high, not because the term-premium wedge is wide** |
| 🚨 **`S8`** | `[blank]` undated | **UNSCOREABLE — 18th consecutive run** | — | — | **A human must `VOID` it or re-register it with a date (P5).** `S95` brackets the expiry `S8` could not. ★ **Eighteen runs of writing the same line is itself the cost**, and this run declines to write more than one line about it |

**Running tally this run: 1 SCORED (`S80` FIRED-C) · 1 SCORED by proposition (`P52`, A refuted) ·
3 DEFERRED with the settle clock stated (`S82` `S83` `S98`) · 2 VOID recommended on their own clauses
(`S98` `S102`) · 1 self-refutation recorded (`P74`) · 1 construction defect recorded (`P75`) ·
1 bracket declined with its reason (a fourth `NVDA` row) · 0 `EXPIRED` · 0 silent skips.**
★ **Four US-owned rows (`S75`–`S78`) were scored this morning by the `industry_kr` desk** — verified
present, not re-scored; ownership confers no exclusivity (README §3).


---

## MASTER scoring log — appended by the 2026-08-21 `industry_kr` run

> Five past-dated rows settled. `EXPIRED` = 0 · silent skips = 0.
> Bench for every KR relative number is **`069500.KS`** — `^KS11` has no 2026-08-20 bar (G0, 3rd consecutive run).

| id | settle date | verdict | observed | frozen threshold | effect on the standing view |
|---|---|---|---|---|---|
| **S66-KR** | 2026-08-20 | **FIRED-A** | leg1 `069500.KS` daily **+6.319%** · leg2 universe volume-ratio median **0.7288** (n=806) | A: leg1 >= +2.0% AND leg2 < 0.920 (the estimator's own 57-session p85) | "Recovery = confidence restored" is **discarded**. `M-80(a)` weakly supported. The by-product is the larger finding: **0.7288 equals the 57-session baseline median 0.730 to the third decimal** — on BOTH the −6.3% and the +6.3% session the median stock's volume was indistinguishable from an ordinary day. That opens the question of whether "no volume response" is an event at all, or the universe's resting state |
| **S63-KR** | 2026-08-20 | **FIRED-A** | VOID clause executed first: **192820 코스맥스 filed 합병등종료보고서(합병) on 2026-08-20** (rcpNo 20260820000434) => removed; 1 name < 2 => not VOID. Spread computed four ways, all above the A line: (a) `^KS11` date-aligned **+24.67pp** · (b) `^KS11` naive **+31.81pp** · (c) proxy `069500.KS` **+31.81pp** · (d) VOID-clause applied, 161890 alone vs brand median **+36.20pp** | A >= **+20pp** · B <= +10pp | **The ODM/brand split is a real unit; "cosmetics" stays retired as a unit** and both sides keep separate theses. The verdict is **robust to the G0 date defect** — four readings, one branch. Price axis only, as registered; the margin leg settles ~2027-03 |
| **S82** *(US-owned)* | 2026-08-20 | **FIRED-A** | `XLV` exc5 **+4.346** minus EW{`XLU` +1.351, `XLRE` +1.876, `XLP` +1.174} = **+2.879** | A >= +2.45 · B <= −1.62 | HLTH decouples upward => **Lens 1/4 right, Lens 2 wrong**; the zero-exposure GAP is real. State-at-registration was **already +3.091, above A** — an A-fire was disclosed in advance, not discovered. The tilt is `industry_US`'s to move (P5) |
| **S83** *(US-owned)* | 2026-08-20 | **FIRED-C** | `ANET` exc5 **−7.794** minus `HPE` exc5 **−9.620** = **+1.826** | A >= +7.16 · B <= −9.68 | No information at this horizon; the theme label grouping ANET+HPE is **not refuted**. Registered with its weakness disclosed (sd **8.417pp**, the board's widest estimator, C the heavy favourite) — and C is what printed. Side observation: the spread is narrow because **both legs fell** (−7.8 / −9.6 vs SPY), not because both held. VOID check: HPE's next print 2026-09-04 is outside the window; M&A / guidance-withdrawal / index-deletion could **not** be re-verified (G1) — read the verdict under that condition |
| **S98** *(US-owned)* | 2026-08-20 | **VOID** — its own anti-signal fired | Anti-signal: *"an FOMC-dated communication or a CPI/PPI print inside the window => VOID."* **The FOMC minutes were released 2026-08-19, inside the 08-13 to 08-20 window.** The evidence is another row of this same ledger, not an inference: `S102` (US, registered 08-19) is built on *"The FOMC minutes released 2026-08-19"*. Observable recorded **for the record only**: all four positive (`XLU` +1.351 · `XLRE` +1.876 · `XLP` +1.174 · `XLV` +4.346) = branch A's shape | A: all four same sign · B: split · C: 3-1 | **Not scored.** The branch-A shape is **not** adopted — reviving a threshold after the fact converts a forecast into a description. Two construction findings handed to `industry_US`: **(1) this anti-signal fires almost surely** — an 8-calendar-day US window essentially always contains an FOMC communication or a CPI/PPI print, so the row was **designed to void**; **(2) the mechanism the anti-signal assumes was already refuted by the same desk** — `S102`'s pre-registration regression (120 settled sessions, Brent-controlled, on d10y in bp) gives `XLU` **+0.0049** · `XLRE` **−0.0072** · `XLP` **+0.0224** · `XLV` **+0.0185** pp/bp, i.e. **the four legs have no measurable rate beta**. A re-registration should key the anti-signal to a measured move (e.g. d10y beyond +/- X bp), not to the existence of a calendar event |

**Still un-scoreable**: **`S8`** (US-owned, date `[blank]`) — **18th consecutive run**. A human must `VOID` it or re-register it with a date (P5). Eighteen runs of writing the same line is itself the cost.

**Deferred with a stated reason (not `EXPIRED`)**: `S64-KR` — the 08-19 run reserved a re-registration; the 08-20 run declined because the settled anchor was contaminated, and **this run declines for the same reason** (G0 failed a 3rd consecutive time; `^KS11` still has no 08-20 bar). **Two consecutive non-issues. If the next run also declines, that is disappearance rather than caution** — at that point either close the bracket or change its observable, in writing.

**Not yet due**: US rows settling at the **2026-08-21** close (`S84`-`S87`, `S95`-`S97`, `S99`, `S100`, `S102`) arrive **05:00 KST 2026-08-22** — the next KR run's to score.


---

## MASTER INDEX — appended 2026-08-21 by the `industry_US` run (PREMORTEM registrations)

| id | owner | file | event / observable | settle | status |
|---|---|---|---|---|---|
| **S108** | `industry_US` | `SCENARIOS_US.md` | Warsh Jackson Hole **D-0 (2026-08-21)** — equity leg: `EW{XLU,XLRE,XLP}` 3-session excess vs `SPY` | **2026-08-25** | ARMED |
| **S109** | `industry_US` | `SCENARIOS_US.md` | `FRO` earnings 2026-08-31 — `FRO` 5-session excess vs `SPY` (the Hormuz axis's freight leg) | **2026-09-02** | ARMED |
| **S110** | `industry_US` | `SCENARIOS_US.md` | [`HPE` exc5] − [`DELL` exc5] vs `SPY` — the pair test `S87` could not perform | **2026-09-03** | ARMED |
| **S111** | `industry_US` | `SCENARIOS_US.md` | `IG OAS` (`BAMLC0A0CM`) level `[FRED]` — the credit instrument `P67` is missing | **first `[FRED]` close covering 2026-08-28** | ARMED |

★ **Registration note**: the implied-move check was **performed and returned unusable** — all four
available straddles (`HPE` ±2.7% · `DELL` ±1.8% · `FRO` ±3.1% · `NEM` ±2.0%) expire **2026-08-21 = D0**
and cover none of the bracketed events (`M47`). All thresholds are `D93` distribution-based and every
row discloses its **state's own percentile** at registration.


---

## MASTER 채점 로그 — appended by the 2026-08-22 `industry_kr` run (**분할하지 않는 스파인**)

> **과거일 10행 처리: 채점 9 · 미도래 1 · `EXPIRED` 0 · 조용한 스킵 0.**
> 08-21 KR 채점 로그가 문자로 위임한 그 행들이다 — *"US rows settling at the 2026-08-21 close … **the next KR run's to score**."*
> 전부 `yfinance auto_adjust=False` **정착 종가**, 벤치 **`SPY`** 인라인(C1), 창 **2026-08-14 종가 → 2026-08-21 종가**. `SPY` 5세션 **−1.368%**.

| id | 정산일 | 평결 | 관측값(실측) | 동결 임계 | 서 있는 뷰에 대한 효과 |
|---|---|---|---|---|---|
| **S84** *(US 소유)* | 2026-08-21 | **FIRED-C** | `XLE` exc5 **+4.162** − EW{`XLU` −2.108, `XLRE` +0.948} **−0.580** = **+4.742** | A ≤ −3.174 · B ≥ +5.544 | 모달. **B 에서 0.80pp 모자랐다** — 등록 시 상태 +3.880 에서 스프레드가 더 벌어졌으나 p95 를 못 넘었다. 「호르무즈 완화가 ENRG 를 압축한다」(A)는 **반대 방향으로 빗나갔다** |
| **S85** *(US)* | 2026-08-21 | **FIRED-C** | `RSPT` 5d −3.322 − `XLK` 5d −3.526 = **+0.204** | A ≤ −0.994 · B ≥ +2.046 | IT N+ 승격의 반증자가 발화하지 않았다. 등록 시 +1.980(p85 위)에서 +0.204 로 급락했으나 A 선에 못 닿아 **「대형주 아티팩트였다」를 부정도 긍정도 못 한다** |
| **S86** *(US)* | 2026-08-21 | **FIRED-B** | EW{`COHR` −9.776, `LITE` −5.049, `CIEN` −6.324} = **−7.050** | A ≥ +12.584 · B ≤ −5.948 | **광학/인터커넥트는 「하락추세 속 반등」이었다.** RS60(−15.1/−5.8/−20.9)이 정직한 창이었다. ⚠ sd 8.998 = 보드 최광폭이라 C 가 압도적 favourite 였는데 **꼬리인 B 가 나왔다** ⇒ 정보량이 크다 |
| **S87** *(US)* | 2026-08-21 | **FIRED-A** | EW{`DELL` −8.561, `HPE` −7.591} = **−8.076** | A ≤ −4.961 · B ≥ +16.143 | **EXHAUSTED.** 등록 시 +12.331 에서 **20.4pp 평균회귀** ⇒ PREMORTEM Lens 3 의 `EXTENDED-BUT-LIVE` 태그가 **틀렸다.** ★ `S83`(08-20 `FIRED-C`)와 모순 없음 — 그 행은 *"두 다리가 다 떨어져서 스프레드가 좁다"* 고 했고 오늘 그 하락이 확인됐다 |
| **S95** *(US)* | 2026-08-21 | **FIRED-A** | `BZ=F` 정착 **93.870** | A ≥ **93.00** · B ≤ 86.50 · C 86.50~93.00(등록 시 favourite) | ★★★ **봉쇄가 결국 배럴을 리프라이싱했다.** 등록 시 88.52~88.91, 실현 4세션 밴드 87.07~88.98(2.2%)에서 **+5.6% 돌파.** 「주식이 원자재가 안 매긴 프리미엄을 매겼나」의 답은 **아니다 — 원자재가 따라왔다.** **안티시그널 검사 실행함**: OPEC+ 쿼터 결정 없음(이라크 증산 요구 기사뿐) · 美 정제소 가동중단 없음(러시아 정제소 피격은 미국 밖) · 허리케인 Lala 는 **하와이**(PADD3 아님) ⇒ **VOID 아님** |
| **S96** *(US)* | 2026-08-21 | **FIRED-B** | EW{`COHR` −9.776, `LITE` −5.049} = **−7.412** | A ≥ +5.0 ∧ 스레드 ≥4매체/일 · B ≤ −5.0 | **5번째 DEEP 승격은 늦었다.** ★ 부가 관측: Lightmatter 스레드는 7일 총 **3건**(digitimes 1 + yahoo_finance 2), **하루 최대 2매체** ⇒ **branch A 는 가격축·매체축 양쪽에서 이중 도달 불가**였다. 안티시그널(NVDA 광학 발표)은 미발화 — NVDA 인쇄는 08-26 |
| **S97** *(US)* | 2026-08-21 | **FIRED-A** | `LHX` exc5 **−7.230** | A ≤ −4.0 · B ≥ 0 | **불연속으로 가격이 매겨졌다** ⇒ `M704` 의 방산 EW 는 **ex-`LHX`** 로 재실행돼야 한다. ★ 확증: 08-20 `LHX` 는 **가이던스를 재확인하고도 −4.6%**(yahoo_finance). 안티시그널(DoD 수주·국방예산 헤드라인) **미발화** — 7일 52건이 전부 CEO 경질·시설 관련 |
| **S99** *(US)* | 2026-08-21 | **FIRED-A** | `M` = EW{`ANET` −3.747, `AVGO` −4.876, `HPE` −7.591} = **−5.405** · `E`(`ETN`) = **−5.788** | A: \|M\|≥3.0 ∧ sign(E)=sign(M) ∧ \|E\|≥1.5 | 🚨 **등록된 규칙대로는 A 다**(세 조건 전부 충족). **그러나 같은 데스크가 같은 주에 이 A 를 위양성이라 사전 선언했다**(`M778`: `ETN` β`XLI` **+1.402**(t +6.12) > β`XLK` +0.620(t +5.14), `ETN`–`CMI` +0.818 · `ETN`–`CAT` +0.800 > `ETN`–`ANET` +0.719). ⇒ **평결은 A 로 기록하고 집중도 가드는 이 A 로 움직이지 않는다.** ★ **이 채점의 진짜 산출물은 「브래킷과 회귀가 정면충돌했고 회귀가 더 많은 정보를 갖고 있다」** 이다 |
| **S100** *(US)* | 2026-08-21 | **FIRED-C** | 창 08-18→08-21: `TGT` **+8.499%** · `WMT` **−9.983%** → EW −0.742% − `SPY` −0.225% = **−0.516pp** | A ≥ +6.5 · B ≤ −6.5 | 결론 변화 없음. ★★ **그러나 C 가 나온 방식이 핵심이다** — 두 발행사가 **18.5pp 벌어진 채 정반대**로 갔는데 등가중이 그걸 **−0.5pp 로 상쇄**했다. **바스켓이 두 개의 반대 이벤트를 서로 지웠다** ⇒ 원래 질문(대형마트 노드를 따로 다뤘어야 하나)은 **답이 안 나온 게 아니라 추정량이 답을 담지 못했다** |

**미도래 1행 (`EXPIRED` 아님)**: **`S102`** *(US)* — 관측면이 *"`[FRED]`, 2026-08-21 을 덮는 첫 종가"* 인데
**FRED 의 `DGS2`/`DGS10`/`DGS30` 마지막 관측이 2026-08-20**이다(2회 독립 조회로 확인; `breakeven_10y` 는 08-21 이 있다).
**08-20 값(`DGS2` 4.19 / `30y−10y` 0.54)을 대입하지 않는다** — 사후에 관측면을 바꾸면 예측이 서술로 바뀐다. **다음 런이 채점한다.**

🚨 **`S8`**(US 소유, 날짜 `[blank]`) — **정산 불가 19번째 연속 런.** 사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다(P5).

### 오늘 이 로그가 남기는 관측 두 개
1. ★ **바스켓 추정량이 정반대 이벤트를 서로 지운다**(`S100`). ⇒ 등가중 바스켓 브래킷은 **다리 간 분산(dispersion)의 사전 임계**를 같이 등록해야 한다. `D305-KR` 의 자매.
2. ★ **`S99` 는 브래킷이 스스로 위양성을 낼 수 있음을 보여준 첫 사례**다 — 같은 데스크의 회귀가 그 A 를 **사전에** 무력화해 뒀고, 브래킷은 그것을 모른 채 A 를 냈다. **평결을 각색하지 않고, 가드를 움직이지 않는 것으로 처리했다.**

### 신규 등록 (2026-08-22 `industry_kr`) — 상세는 `SCENARIOS_KR.md`

| id | 소유 | 파일 | 이벤트 / 관측면 | 정산 | 상태 |
|---|---|---|---|---|---|
| **S64-KR** | `industry_kr` | `SCENARIOS_KR.md` | **`S52-KR` 재등록(3결함 수정)** — 제약이 섹터 명제인가 한 이름 명제인가. O1=068270 정착 종가 밴드 · O2=**24섹터 동시 이항검정의 Bonferroni 통과 여부** | **2026-09-19**(21 정착세션) | **ARMED** |

★ **`S64-KR` 은 3런 연기 끝에 오늘 발행됐다.** 연기 사유는 매번 *"정착 앵커(`^KS11`)가 오염됐다"* 였고,
**오늘 그 문제는 더 나빠졌으나**(08-21 `Close`=NaN) **같은 창에서 `069500.KS` 는 정착봉을 갖고 결측이 0** 이다
⇒ **관측면의 앵커를 `069500.KS` 정착세션으로 바꿔서 발행한다.** 스파인 규칙(*"다음 런도 연기하면 소멸"*)을 소멸이 아니라 **관측면 교체**로 이행했다.


---

# MASTER scoring log + MASTER INDEX — appended by the 2026-08-22 `industry_US` run

> ⚠ Append-only (`'a'` mode, D165). The spine's scoring log and MASTER INDEX are **not split by
> market** — this block updates both for the rows this desk scored and registered on 2026-08-22.

## A · Scored this run — the five US rows the sibling KR desk did NOT take

All are **5-session excess vs `SPY`**, settled closes, window **2026-08-14 → 2026-08-21**,
`yfinance auto_adjust=False`. **`SPY` 5-session return = −1.368%** (776.34 → 765.72) — **independently
computed and identical to the KR desk's figure this morning, which is the cross-check.**

| ID | Observable (measured) | Frozen bands | **Verdict** | Effect on the standing view |
|---|---|---|---|---|
| **`S88`** | `EW{MPC +2.859, VLO +3.472, PSX +5.332}` = **+3.888** | A ≤ +0.061 · B ≥ +8.144 | **FIRED-C** | The ENRG OW promotion is **not falsified**. ⚠ Information content honestly low: **A was the row's entire content** (B was declared NO-INFORMATION at registration) and A needed a **−15.6pp** collapse from a 100th-percentile state ⇒ **C was overwhelmingly the favourite and C is what came.** ★ What it did buy is the `VLO` miss-ledger leg |
| **`S89`** | `NEM` exc5 = **+13.104** | A ≤ −5.217 · B ≥ +9.658 | **FIRED-B** | The gold run is **live, not exhausted**. ⚠ **Anti-signal checked FIRST**, as the 08-21 packet pre-committed: `GC=F` 4380.4 → 4624.1 = **+5.563%**, inside the **±8%** void band ⇒ **NOT fired, the row scores.** ⚠⚠ **But `M779` puts 246.4% of `NEM`'s rs60 in the last 20 sessions** ⇒ **B fired on EXHAUSTION GEOMETRY** (`D306` class). **B is a price fact, not evidence of a base** |
| **`S90`** | `DLR` exc5 = **−3.393** | A ≤ −3.199 · B ≥ +5.223 | **FIRED-A** | **The Real Estate accumulation was LATE** — and this is the registered falsifier of the 08-21 run's own price-only promotion of RE to N−. **ROTATION moved RE N− → UW on it.** ⚠ **Anti-signal examined and NOT fired, on two independent grounds, both recorded**: (1) *strict reading* — the 08-19 **8-K + 424B7** is a **resale registration of shares already issued** in a previously-closed acquisition and the **third in a recurring series** (06-29, 07-01, 08-19); **no acquisition was announced and no guidance issued** (last Item 7.01 8-Ks 06-22/06-29, 10-Q 07-31, all before the window). (2) *the clause's own purpose, tested* — it exists to catch *name event, not node read*, and the peer decomposition **refutes a name event**: `DLR` **−3.393** travels with `EQIX` **−1.963** and `IRM` **−4.357** while `XLRE` **+0.948**, `AMT` **+1.493**, `PLD` **+1.914**, `WELL` **+2.939** go the other way. ⚠ **Disclosure that keeps it honest: branch A is the branch that COSTS this desk** |
| **`S91`** | `XLY` exc5 = **+1.216** (un-voided reading: **C**, 0.337pp from B) | A ≤ −2.467 · B ≥ +1.553 | 🚨 **VOID** | Its anti-signal — *"a September-FOMC-dated headline or an inflation print in window"* — **fired unambiguously**: `investing_en` **08-20** *"Fed's Musalem says he won't prejudge rate call view for **September FOMC**"*; `fool`/`yahoo_finance` **08-14** *"Despite Lower Odds of a **September Fed Rate Hike**…"*; the **FOMC minutes of 08-19**; **219 hits** on `September AND FOMC` over the 8 days; plus the **UMich inflation-expectations release, 08-14**. ⚠ **What is given up**: the narrowest estimator on the board (sd 1.639) landing **a third of a point from an informative branch** |
| **`S93`** | `WMT` **−8.669** · `HD` **+0.409** · `TGT` **+8.463** · `ABNB`−`HD` **+2.719** (un-voided: **C** — A fails on `HD`/`TGT`, B fails on `HD` and on the +2.719 OR-leg) | A = all three negative · B = `TGT`+ while `WMT`,`HD` − , OR spread > +5 | 🚨 **VOID** | Its anti-signal — *"a tariff announcement affecting consumer goods inside the window"* — **fired ON THE BRACKET'S OWN NAMES**: **2026-08-21**, three outlets — `bloomberg` *"Trump to Allow Tariff Relief for Certain Ground Beef Imports"*, `scmp`, `fortune`; and `forbes` 08-21 *"Americans' Top Retailers Are Getting Billions In Tariff Refunds — Including **Walmart, Target**."* |

★★ **The finding that outranks all five verdicts: TWO of them VOIDed on the SAME construction defect,
and it is `D300-KR`, now measured three times in six days** (`S98` VOIDed 08-21 on an FOMC
communication inside an 8-day US window). **An 8-calendar-day US window essentially always contains an
FOMC/CPI/PPI communication, and almost as often a consumer-tariff headline. These anti-signals were
DESIGNED TO VOID.** `S91` and `S93` predate the fix the 08-21 run applied to `S108`–`S111`
(a base-rate check at registration) and **are its cost, paid today.** ⇒ Every clause registered by this
run (`S112`–`S114`, `P85`–`P89`) is keyed to a **magnitude** or a **specific dated action**, never to
"an event occurring" — the `S89` gold-band shape, **which behaved correctly today.**

## B · P-row pre-commitments settled on the true 2026-08-21 close

| ID | Registered test | Measured | Verdict |
|---|---|---|---|
| **`P66`** | The Russia supply-destruction leg survives independently of Hormuz | **CONFIRMED and still being reported inside the window**: `toi` 08-17 *"Russia faces fresh fuel shortages as refinery attacks disrupt supplies"* · `oilprice` 08-17 *"Russia Receives First Gasoline Cargo From India"* · **08-21 *"Ukrainian Drone Attack Hits Lukoil Refinery Deep in Russia"*** | **HOLDS** |
| **`P69`** | Does a Hormuz shutdown reprice crude at all? A ≥ 93.00 · B ≤ 86.50 | `BZ=F` 08-21 settle **94.390** (this desk, 22:2x KST) / **93.870** (KR desk, 09:3x KST) | **FIRED-A on both readings.** The answer to the registered question is **yes — the barrel repriced.** Twin of `S95`-A |
| **`P70`** | `EW{MPC,PSX,VLO}` exc5 ≥ +2.0 **∧** `BZ=F` 5-session ≤ +2.0% | EW **+3.888** ✅ · `BZ=F` 5d **+6.631%** ❌ | **MISS — the conjunction fails on the control leg by 4.63pp.** ⇒ **`R89` is confirmed AT SETTLE, not merely anticipated: this week the desk cannot show the refiners' excess is margin rather than barrel** |
| **`P75`** | *"the crack ≥ 95"* ∧ EW exc5 ≥ +2.0 | 3-2-1 crack **69.61** ❌ · distillate crack **101.72** ✅ · EW **+3.888** ✅ | 🚨 **CLOSED AS UNSCOREABLE-BY-CONSTRUCTION (P5), third consecutive recording** (08-19: 67.64/101.17; 08-20: 66.26/100.34). The branch names *"the crack"* and the two series answer oppositely. **A third deferral would be extinction, not caution** (the `S64-KR` precedent, same morning). **`P80`/`P83` are the successors and name both series explicitly** |

## C · Not yet arrived — `S102`, second consecutive run, and the reason is now STRUCTURAL

**`S102`** — observable *"`[FRED]`, the first close covering 2026-08-21"*: `DGS2` ≥ 4.30 (A) /
`DGS2` ≤ 4.08 ∧ `30y−10y` ≥ 0.59 (B). **FRED's last observation on `DGS2`/`DGS10`/`DGS30` is still
2026-08-20** on a **third independent pull** (the KR desk made two this morning; this is the third,
~14 hours later). Values at 08-20: `DGS2` **4.19**, `30y−10y` **0.54**. **They are NOT substituted** —
changing the observable after the fact converts a prediction into a narrative.
🚨 **Diagnosis registered as `D309`: FRED daily series do not publish on weekends, so a bracket whose
settle date is a FRIDAY cannot be read by a Saturday-or-Sunday desk, by construction.** ⇒ **`S102` is
handed explicitly to the 2026-08-24 run**, and future FRED-observable brackets must settle on **the
first BUSINESS DAY after the release**, with the release lag stated at registration.

## D · MASTER INDEX additions

| ID | Owner | File | Settles | Status |
|---|---|---|---|---|
| **`S112`** | `industry_US` | `SCENARIOS_US.md` | **2026-08-31** | ARMED — the mandatory Jackson Hole (+PCE) bracket; state **49th %ile**, both branches equally reachable |
| **`S113`** | `industry_US` | `SCENARIOS_US.md` | **2026-09-01** | ARMED — `SMH` into `NVDA` 08-26; branch B pre-declared LOW-INFO (state already at the 12th %ile) |
| **`S114`** | `industry_US` | `SCENARIOS_US.md` | **2026-09-03** | ARMED — `EW{NUE,STLD}` tariff test on a HELD name; branch A pre-declared LOW-INFO (state at the 3rd %ile) |

## E · 🚨 `S8` — undated and unscoreable for the **20th** consecutive run

US-owned, date `[blank]`. **A human must `VOID` it or re-register it with a date (P5).**
⚠ **New this run, and it is the clearest argument yet for closing it**: `S95` **fired branch A this
morning** — the very axis `S8` was built for has now produced a scored outcome through a *different*
row. **`S92` (08-31) and `P89` (08-28) cover both sides of it.** `S8` is dead weight, and writing the
same line for a 20th time is itself a cost.

**Run tally 2026-08-22 (`industry_US`): scored 5 (FIRED-A 1 · FIRED-B 1 · FIRED-C 1 · VOID 2) ·
verified-as-scored-by-sibling 9 · P-rows settled 4 · not-yet-arrived 1 (with a registered structural
cause and a named successor run) · newly registered 3 · `EXPIRED` 0 · silent skips 0.**


---

## MASTER 채점 로그 — appended by the 2026-08-23 `industry_kr` run (**분할하지 않는 스파인**)

> **과거일 처리: 채점 0 · 미도래 1 · `EXPIRED` 0 · 조용한 스킵 0.**
> ⚠ **쓰기 방식**: `'a'` 모드 append(`D165`).

### A · 채점 대상 — **전수 확인 결과 0건이다** (「없어서 안 했다」가 아니다)

**KR 소유 브래킷 전수**(`SCENARIOS_KR.md` + 이 스파인의 MASTER INDEX) 중 **정산일이 2026-08-23 이하인 행은 0개**다:

| id | 정산 | id | 정산 |
|---|---|---|---|
| `S67-KR` | 2026-09-04 | `S58-KR` | 2026-09-09 |
| `S61-KR` | ~2026-09-14 | `S62-KR` | 2026-09-15 |
| `S64-KR` | **2026-09-19**(21 정착세션) | `S65-KR` | 2026-09-19 |
| **`S68-KR` (오늘 신규)** | **2026-09-19**(21 정착세션) | `S45` · `S54-KR` | 2026-09-30 |
| `S60-KR` | 2026-10-12 | `S49-KR` | 2026-10-30 |
| `S34` · `S53-KR` | 2026-10-31 | `S59-KR` | 2026-11-04 |

⇒ **가장 이른 KR 정산은 09-04 로 12일 앞이다.** **오늘 KR 채점 대상은 존재하지 않고, 그것을 전수 확인으로 확정했다.**

### B · 미도래 1행 (`EXPIRED` 아님) — **`S102`** *(US 소유)* · **3런 연속**

- 관측면: *"`[FRED]`, 2026-08-21 을 덮는 첫 종가"* · 임계 `DGS2` **≥4.30**(A) / `DGS2` **≤4.08 ∧ 30y−10y ≥0.59**(B), 동결.
- **오늘 실측(`module_macro_us --days 365 --json`, 09:0x — 이 행에 대한 4번째 독립 조회)**:
  **`DGS10`·`DGS2`·`DGS30` 마지막 관측이 전부 2026-08-20.** 값 `DGS2` **4.19** · `DGS30` 5.23 · `DGS10` 4.69 ⇒ `30y−10y` **0.54**.
  (`T10YIE` 는 08-21 존재, `RRPONTSYD` 도 08-21 — **일별 국채 시리즈만 08-20 에 멈춰 있다.**)
- 🚫 **08-20 값을 대입하지 않는다.** 사후에 관측면을 바꾸면 예측이 서술로 바뀐다.
- ⇒ **진단은 이미 `D309` 로 등록돼 있다**(FRED 일별 시리즈는 주말에 게시되지 않는다 ⇒ 정산일이 금요일인 브래킷은 토·일 데스크가 **구조적으로** 읽을 수 없다).
  **08-22 US 런이 이 행을 「2026-08-24 런에 명시적으로 인계」했고, 오늘은 일요일이므로 그 인계를 그대로 유지한다.**
- ★ **이 행이 오늘 남기는 진짜 산출물은 평결이 아니라 표본이다**: **같은 이유의 4번째 조회이고 네 번 다 같은 답이다.**
  `D309` 는 이제 추론이 아니라 **4회 재현된 관측**이다.

### C · 🚨 **`S8`** *(US 소유, 날짜 `[blank]`)* — **정산 불가 21번째 연속 런**
날짜가 없어 어느 클럭으로도 정산할 수 없다. **사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다(P5).**
이 런은 **고치지 않고 카운트만 올린다** — **조용히 넘기지 않았다는 기록이 이 줄의 목적이다.**

### D · 신규 등록 — 상세는 `SCENARIOS_KR.md`

| id | 소유 | 파일 | 이벤트 / 관측면 | 정산 | 상태 |
|---|---|---|---|---|---|
| **`S68-KR`** | `industry_kr` | `SCENARIOS_KR.md` | **KR 밸류 축의 반쪽 다리(마진 백분위)가 초과수익과 관계있는가** — 004370 농심의 **21 정착세션 초과**(벤치 `069500.KS`), **밴드 중심을 0 이 아니라 측정된 −4.773pp 에 두고 ±1σ(14.938pp)** | **2026-09-19** | **ARMED** |

★ **이 등록의 방법론적 특징 세 가지 — 전부 이 데스크 자신의 과거 실패에 대한 대응이다.**
1. **`D93`**: σ 만이 아니라 **중심도 측정했다.** 이 추정량의 2년 평균은 **−4.773pp** 이고 0 이 아니다.
   0 을 중심으로 잡았으면 **branch A 가 4.8pp 쉬워지고 branch B 가 4.8pp 어려워졌을 것이다.**
2. **`D300-KR`**: 안티시그널의 **base-rate 를 등록 시점에 실측했다.** `단일판매·공급계약`·`자기주식`·`유상증자` 는 **90일 창 0건**,
   `기업가치제고계획` 만 **2건/90일 ≈ 0.5건/30일**. ⇒ **「발화하도록 설계된 절」이 아니다.**
3. **`D305-KR`**: **지평을 임계와 같은 줄에 적었다**(21 정착세션, `069500.KS` 기준일 정렬).
   그리고 **정보 등급을 선언했다** — **C 가 favourite(~68%)** 이고 이 행의 값은 A/B 가 나올 때만 크다.

### E · 오늘 이 로그가 남기는 관측 하나
★ **채점 0건이 정보가 되려면 「전수 확인했다」가 같이 적혀야 한다.**
이 데스크는 **`EXPIRED` 를 프로세스 실패로 규정**하는데, **「오늘 정산할 게 없었다」와 「오늘 정산 대상을 확인하지 않았다」는 같은 모양으로 보인다.**
⇒ **§A 의 전수 표가 그 둘을 가르는 유일한 장치다.** 앞으로도 채점 0인 런은 이 표를 붙인다.


---

# MASTER INDEX + scoring log — appended by the 2026-08-23 `industry_US` run

> ⚠ Append-only (`D165`). The spine's scoring log and MASTER INDEX are **not split by market**.

## A · Scored this run — **0, and the exhaustive settle table is the evidence the question was asked**

Every US-owned bracket with a settle date, checked against **2026-08-23**:

| Settle | Rows | Status |
|---|---|---|
| ≤ 2026-08-21 | `S84`–`S101`, `P65`–`P75`, and all earlier | **ALL SCORED** (nine by the KR desk 08-22, five by the US desk 08-22, four P-rows settled) |
| **2026-08-22** | **none** | — |
| **2026-08-23 (today)** | **none** | — |
| 2026-08-24 | `S74` | ARMED |
| 2026-08-25 | `P79` · `S108` | ARMED |
| 2026-08-26 | `S79` · `S101` · `S103` · `P77` · `P78` · `P80` | ARMED |
| **2026-08-27** | **`S115` (new)** · **`S117` (new)** · `S81` · `P83` | ARMED |
| **2026-08-28** | **`S116` (new)** · `P67` · `P81` · `S111` · `P85`–`P89` | ARMED |
| 2026-08-31 | `S92` · `S94` · `S104` · `S112` | ARMED |
| 2026-09-01 → 09-30 | `S113` · `S109` · `S105`–`S107` · `S110` · `P84` · `S114` · `S48` | ARMED |

⇒ **0 scored · 0 `EXPIRED` · 0 silent skips.** The earliest US settle is **2026-08-24**.
KR-owned rows (`SCENARIOS_KR.md`, opened): earliest settle **2026-09-04** — none past-dated.

## B · Not yet arrived — **`S102`**, 4th consecutive US run, diagnosis now **5×-replicated**

Observable *"`[FRED]`, the first close covering 2026-08-21"*. **Today's pull is the fifth independent
one** (two KR-desk 08-22, one US-desk 08-22, one KR-desk 08-23, this one): `DGS2`/`DGS10`/`DGS30` all
still end **2026-08-20** — `DGS2` **4.19**, `DGS30` **5.23**, `DGS10` **4.69** ⇒ `30y−10y` **0.54**.
🚫 08-20 values **not substituted**. `D309` (a FRED-daily bracket settles on a publication, not on a
market close, and FRED does not publish on weekends) has stopped being an inference: **five identical
observations across three desks and three calendar days.** **The 08-22 hand-off to the 08-24 run
stands unchanged; a Sunday could not have changed it.**

## C · 🚨 `S8` — undated and unscoreable for the **22nd** consecutive run
Confirmed present in today's `catalyst_calendar --days 10` as its undated binary. **A human must
`VOID` it or re-register it with a date (P5).** This run increments the count and does not fix it.

## D · MASTER INDEX additions

| id | owner | file | event / observable | implied move at registration | settle | status |
|---|---|---|---|---|---|---|
| **`S115`** | `industry_US` | `SCENARIOS_US.md` | `NVDA` **08-26** print → 1-session return on 08-27; A ≥ +7.0% / B ≤ −7.0% | **±6.11%** (08-28 straddle, ATM IV 0.606) | **2026-08-27** | **ARMED** |
| **`S116`** | `industry_US` | `SCENARIOS_US.md` | `MRVL` **08-27** print (🚨 calendar-invisible) → **`MRVL` − `AVGO` spread** on 08-28; A ≥ +12.0pp / B ≤ −12.0pp | `MRVL` **±11.31%** (ATM IV 1.122) | **2026-08-28** | **ARMED** |
| **`S117`** | `industry_US` | `SCENARIOS_US.md` | `MU` − `NVDA` 1-session excess on 08-27; A ≥ +3.0pp / B ≤ −3.0pp | registration fact: `MU` ATM IV **0.650** > `NVDA` **0.606** on one expiry, with **no `MU` print until 09-24** | **2026-08-27** | **ARMED** |

## E · Two observations this log leaves

1. ★ **`S103` is pre-declared NO-INFORMATION rather than re-banded.** Its hand-set ±5.0pp bands sit
   **inside** the measured ±6.11% implied move. `D242` forbids re-freezing, so it settles as
   registered — but its verdict may not be read as a surprise in either direction, and `S115` is the
   successor written outside the implied move. **`D295` is thereby DISCHARGED after four runs**, and
   the discharge came from reading the option chain directly because `module_flow --positioning`
   returns the 08-24 expiry for an 08-26 event (`D315`, 4th run).
2. ★★ **`S116` exists only because the calendar was audited.** `catalyst_calendar` carries **no row**
   for `MRVL` 08-27, and `MRVL` is the name that took Alphabet custom-silicon share from a **held**
   position on 08-19 while carrying the **highest implied move on the board**. ⚠ **And the same audit
   cleared the calendar on `NVDA`** — `catalyst_calendar` says 08-26, `yfinance` says 08-27, and two
   news bodies say **08-26**. **An audit that can only convict its instrument is not an audit**; this
   one exonerated it on the biggest row and convicted it on a row nobody had looked for.

---

# MASTER scoring log — entry added by the 2026-08-24 `industry_kr` run

> **0 scored · 1 not-yet-arrived · 1 handed to its owner · 0 `EXPIRED` · 0 silent skips.**
> ⚠ 채점 0 인 런은 **전수 표를 붙인다**(2026-08-23 KR 이 도입하고 08-23 US 가 채택한 규칙).

## A · 전수 정산 표 — **「없어서 안 했다」와 「확인 안 했다」를 가르는 유일한 장치**

| Settle | Rows | Status |
|---|---|---|
| ≤ 2026-08-21 | `S84`–`S101`, `P65`–`P75`, 및 그 이전 전부 | **ALL SCORED** (08-22 KR 9건 · 08-22 US 5건 · P행 4건) |
| **2026-08-22 · 08-23** | **none** | — |
| **2026-08-24 (오늘)** | **`S74`** (US 소유) | 🚨 **소유자 인계 — 아래 §C** |
| 2026-08-25 | `P79` · `S108` | ARMED |
| 2026-08-26 | `S79` · `S101` · `S103` · `P77` · `P78` · `P80` | ARMED |
| 2026-08-27 | `S115` · `S117` · `S81` · `P83` | ARMED |
| 2026-08-28 | `S116` · `P67` · `P81` · `S111` · `P85`–`P89` | ARMED |
| 2026-08-31 | `S92` · `S94` · `S104` · `S112` | ARMED |
| 2026-09-01 → 09-30 | `S113` · `S109` · `S105`–`S107` · `S110` · `P84` · `S114` · `S48` | ARMED |

**KR 소유 브래킷(`SCENARIOS_KR.md` 전수 확인)** — 오늘 정산일 도래 **0건**:

| 정산일 | 행 | 정산일 | 행 |
|---|---|---|---|
| 2026-09-04 | `S67-KR` | 2026-09-09 | `S58-KR` |
| ~2026-09-14 | `S61-KR` | 2026-09-15 | `S62-KR` |
| **2026-09-19** | `S64-KR` · `S65-KR` · `S68-KR` | 2026-09-30 | `S45` · `S54-KR` |
| 2026-10-12 | `S60-KR` | 2026-10-30 | `S49-KR` |
| 2026-10-31 | `S34` · `S53-KR` | 2026-11-04 | `S59-KR` |

⇒ **가장 이른 KR 정산은 09-04 로 11일 앞이다.**

## B · 🚨 `S102` — **6번째 미도래, 그리고 오늘 진단이 정정됐다**

관측면 *"`[FRED]`, 2026-08-21 을 덮는 첫 종가"*. 임계 `DGS2` **≥4.30**(A) / `DGS2` **≤4.08 ∧ 30y−10y ≥0.59**(B), 동결.

**오늘 실측 — 두 경로 독립 조회**(모듈 경유 + FRED CSV 엔드포인트 직접):
`DGS2` **4.19** · `DGS10` **4.69** · `DGS30` **5.23** — **전부 마지막 관측이 2026-08-20**, 08-21 행 자체가 없다.
**반면 `T10YIE` 는 `2026-08-21,2.34`, `RRPONTSYD` 는 `2026-08-21,0.200` 으로 존재한다.**

★★★ **`D309` 는 반증이 아니라 좁혀졌다.** 상속된 진단은 *"FRED 는 주말에 게시하지 않으므로 금요일 정산 브래킷을
주말 데스크가 구조적으로 못 읽는다"* 였고, **앞선 5회 관측은 전부 주말이라 두 설명이 구분되지 않았다.**
**오늘은 월요일이고 같은 FRED 에서 두 시리즈가 08-21 을 갖고 있다.**
⇒ **정정판: 시리즈별 게시 래그이고, H.15 계열(`DGS*`·`DFII10`)이 `T10YIE` 보다 최소 1영업일 늦다.**
⇒ **`DGS*` 로 정산하는 브래킷은 정산일 +1영업일 이후에만 읽을 수 있다.**
🚫 **08-20 값을 대입하지 않았다.** ⇒ **미도래 · `EXPIRED` 아님.**
⚠ **그리고 이 행은 08-22 US 런이 이미 「VOID RECOMMENDED」로 표시했다**(안티시그널: 창 안의 재무부 리펀딩 — 08-19 Bessent
장기물 바이백 확대). ⇒ **정산 여부 자체가 소유자(P5 · `industry_US`)의 결정이고, KR 은 관측만 넘긴다.**
⇒ **08-25 가 이 행이 읽힐 수 있는 첫 영업일이다.**

## C · 🚨 `S74` (US 소유) — **정산일이 오늘인데 오늘이 끝나지 않았다. 브랜치별 실측을 붙여 소유자에게 인계한다**

관측면은 **뉴스**다: *"명명된 두 조건(① 미 해군 봉쇄 종료 ② 전쟁 피해 보상)에 관한 날짜 박힌 귀속 가능한 성명·행동,
`--scope foreign` 풀, **본문 2개 매체 이상 교차확인**"*. 브랜치 C = *"08-24 까지 둘 다 아님 = AMBIGUOUS"*.

**2026-08-24 08:5x 실측**(스윕 밖 창 · 임베딩 커서 08-24 07:54 · **`D324` 를 피해 각 텀을 개별 인용부호로**):

| 다리 | 실측 | 판정 |
|---|---|---|
| **A① 미 봉쇄 해제·부분 철회** | 없음. 08-18 `fxstreet` 본문 *"Trump says no Iran talks; naval blockade remains"* · 08-21 `toi` 본문 *"US vows toughest-ever Iran sanctions, presses China to help reopen Hormuz"* | **미발화** |
| **A② 보상 프레임워크 발표** | 없음. `"compensation" AND "Iran"` 6일 **52건** 중 보상 프레임워크 보도 0 | **미발화** |
| **A③ 이란 무조건 재개 성명** | 없음. 08-18 `forbes` 본문 *"Iran Says Hormuz Will Stay Shut Until U.S. Lifts Sanctions And Blockade"* · 08-23 `euronews` 본문 Rezaei *"shut until US changes"* | **미발화** |
| **B① 두 조건에 대한 공식 미국 거부** | **후보 있음, letter 미충족** — 위 세 건은 회담 거부·제재 강화이지 *"명명된 두 조건에 대한 공식 거부"* 문구가 아니다 | **소유자 판단** |
| **B② 통항 중 VLCC 피격** | **후보 있음, 선종 미확정** — 08-18 `upi`·`euronews` 본문 *"Ship hit in Hormuz"*, 사상자 1. **VLCC 여부 본문 미확정** | **소유자 판단** |
| ⚠ **안티시그널 (a)** | 🚨 **후보 발생** — 08-23 `hellenicshipping` 본문 *"Iran grants Iraq limited Hormuz passage to revive oil exports"* / *"Iran lets Iraqi oil tankers pass Hormuz as Trump claims 'total control'"*. **명명된 두 조건 어디에도 연결되지 않은 부분 재개** = S74 자신의 안티시그널 (a)(*"조건 언급 없는 재개가 일어나면 이 행의 프레이밍 전체가 틀렸다"*) 클래스 | **소유자에게 인계** |

⇒ **KR 의 처리: 브랜치 A 미발화 확정 · B 는 letter 미충족(후보 2건 기재) · 안티시그널 (a) 후보 1건 기재 ·
정산은 소유자(`industry_US`)의 08-24 런.**
🚫 **letter 를 intent 로 바꿔 읽지 않았다** — 그것이 `S102` 가 「구성 결함」으로 기록된 바로 그 형태다.
★ **부수 효과**: 미스 원장 `UAL`(08-13, 진입조건 = `S74` 브랜치 A 발화)이 **이 측정으로 `reaffirmed` 됐다.**

## D · 🚨 `S8` — **날짜 없음, 22번째 연속 정산 불가**

오늘 `catalyst_calendar --days 5` 의 `[MACRO]` 블록에 **`undated — Iran 'Strait of Hormuz open' statement (TACO trigger) 🔀binary [news👁]`**
로 그대로 존재한다. **사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다(P5).** 이 런은 **카운트만 올리고 고치지 않는다.**

## E · 이 로그가 남기는 관측 두 줄

1. ★★ **오늘 이 데스크가 만든 두 개의 「양면 명제」는 브래킷이 아니다.** `M-100`~`M-103` 은 MACRO 명제이지
   `SCENARIOS` 행이 아니다. **KR 브래킷 신규 등록 0건** — **`S68-KR`(08-23 등록, 정산 09-19)이 여전히 최신이다.**
   ⚠ **이 런은 PREMORTEM 블록이 없는 프로토콜(`industry_kr` 는 7스테이지 + preflight/handover)이라 브래킷 등록 경로가 구조적으로 좁다.**
2. ★ **정산일이 「오늘」인 행을 개장 중 런이 만나면, 그 행은 채점 대상이 아니라 인계 대상이다.**
   오늘 `S74`(뉴스 관측면, 08-24 종료 미도래)와 `011200 HMM` 의 스코어보드 08-24 관측점(`BZ=F` 08-24 정착 필요)이
   **둘 다 같은 이유로 미도래**였다. ⇒ **후보 규칙: 관측면이 「그 날의 종료」에 걸린 행은 다음 런이 채점한다 — 장중 값으로 채점하지 않는다.**


---

## MASTER scoring log — rows appended 2026-08-24 by `industry_US` (append-only)

> ⚠ This spine section is **deliberately NOT split by market**, so an `EXPIRED` row cannot hide in the
> other market's file. **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` ·
> `REPORT/**`: `S118`–`S123` **0 hit**. Current highest **`S117`**.

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **`S74`** | 2026-08-10 (PREMORTEM) | **2026-08-24** (or on first occurrence) | ★ **FIRED-C** | **2026-08-24 HANDOVER (`industry_US`)** | **Observed**: A's three legs all unfired (US escalated to strictest-ever sanctions; compensation restated as a **demand** not a framework, `euronews` 08-21; the reopening was **explicitly conditional** — Rezaee, *"not a single drop of oil will be exported"*). B's two legs **fail the letter**: no *formal* refusal document, and **no VLCC was struck** — a transiting **bulk carrier** (`MINOAN DIGNITY`, chief engineer killed 08-17→18, UKMTO) and a **products tanker** (`AMARA`, seized 08-17) were, while the VLCCs in the same report **aborted**. ⇒ C. 🚨 **Its registered anti-signal (a) FIRED**: a partial reopening ran through **bilateral exception-granting** (Iraqi permits on *"repeated requests … through various diplomatic channels"*, IRNA/Reuters 08-22) **naming neither condition** — and DRIFT then found a **FOURTH** channel the same night (China+Jordan joint statement, `scmp` 21:48 HKT, `M883`). **No grade moved. `S8` — undated 23 runs — is now again the only general-fleet Hormuz bracket** |
| **`S102`** | 2026-08-19 (PREMORTEM) | "first close covering 2026-08-21" | — | — | **NOT-YET-ARRIVED, 5th consecutive US run · 7th independent pull.** `DGS2`/`DGS10`/`DGS30`/`DFII10`/`DTB3` all end **08-20**; `T10YIE` (2.34) and `SOFR` (3.65) carry **08-21** — two code paths, module and direct FRED API (`M858`). 🚫 **08-20 values NOT substituted.** ★ **The diagnosis was CORRECTED by the `industry_kr` desk, not by us** (`D333-KR`/`M840`, ~10:00 KST the same day): not "FRED doesn't publish on weekends" but **a per-series publication lag, H.15 ≥1 business day behind `T10YIE`**. **Successor run: 2026-08-25** |
| **`S8`** | 2026-07-22 (PREMORTEM) | `[blank]` **undated** | — | — | **UNSCOREABLE, 23rd consecutive run.** Human must `VOID` it or re-register with a date (P5). ★ **Its cost is now open, not merely old**: `S74` — the row written *because* `S8` was unscoreable — has settled and retired, on a day the Strait produced a fatality, a seizure, a partial reopening and a sanctions round |
| **`S118`** | **2026-08-24 (PREMORTEM)** | **2026-08-28** | — | — | **ARMED** — `EW{MU,SNDK,WDC}` 2-session excess vs **`NVDA`**, 08-26→08-28. A ≥ **+6.50pp** (memory carries it) / B ≤ **−6.50pp** (NVDA does) / C between. ★ **Threshold OUTSIDE the implied move**: `NVDA` 08-28 straddle **±6.13%**. Registered because three non-printing memory names carry higher ATM IV than the printer (`SNDK` **0.926** vs `NVDA` 0.692 = **1.34×**) while memory participation is **0.0%** (`M874`) |
| **`S119`** | **2026-08-24 (PREMORTEM)** | **2026-08-27** | — | — | **ARMED** — equal-weight **Energy** 3-session excess vs `SPY`, 08-24→08-27. A ≥ **+2.60pp** / B ≤ **−2.60pp** (≈ ±0.60σ on a 3-session sd of ~3.35) / C between. ★ **Mandatory D-0 bracket** on Bessent's **14:00 ET 08-24** sanctions presser — **a dated binary `catalyst_calendar` does not carry** (`M872`). **B is the falsifying branch and this run's own evidence points at it** |
| **`S120`** | **2026-08-24 (PREMORTEM)** | **2026-08-28** | — | — | **ARMED** — `DGS30` **and** `T10YIE` `[FRED]` at the **first observation where BOTH carry 08-28**. A `DGS30 ≥ 5.31` ∧ `T10YIE ≤ 2.38` / B `DGS30 ≤ 5.10` ∧ `T10YIE` 2.28–2.40 / C between. ⚠ **The observation-lag clause is written INTO the row** (`D333-KR`) — the defect that has left `S102` unsettled for five runs. ⚠ **Shares its observable pair with `P94` (08-27): if both fire the same way that is ONE observation** |
| **`S121`** | **2026-08-24** | — | ⚠ **DROPPED before registration; ID consumed, permanently unused** | 2026-08-24 | **Graded and dropped**: 08-28 already carries **`P67` `P81` `P85`–`P89` `S116`** — seven rows on one print, plus `FRO`. Per the standing rule, an eighth changes no conclusion. ⇒ **`D343`** — date-clustered rows resolving together read as seven confirmations from **n ≈ 1** (`B3`) |
| **`S122`** | **2026-08-24 (PREMORTEM)** | **2026-09-30** | — | — | **ARMED** — a **definitive agreement naming buyer and price** on **Shell's ~$8bn US chemicals sale**, in **≥2 outlet bodies**. A `XOM` is the buyer ⇒ **its 🔴RESOLVED *control* status is falsified** / B non-`XOM` or no agreement / C consortium. Grade **`[news]`**. ★ Surfaced only by the **blind-spot pass** (`burst`: `CHEMICALS` **z 13.2**, 100% market relevance, no chemicals bucket in the term table). 🚨 `LYB`/`DOW` are **outside the universe** (`D341`) |
| **`S123`** | **2026-08-24 (PREMORTEM)** | **2026-09-12** | — | — | **ARMED** — equal-weight **Industrials** 5-session excess vs `SPY`, **09-05→09-12**, a window **straddling Canada's 09-08 effective date**. A ≤ **−3.10pp** (−2.0σ) / B ≥ **+0.44pp** / C between. ★ Exists because **`P92` and `P93` both settle 08-28, ELEVEN DAYS EARLY** (`D342`) — they measure the announcement and can never measure the implementation. ⚠ **Correlated with `P93`: if both A-branches fire that is ONE object measured twice.** ⚠ **The Staples/agricultural leg of the same event remains UNBRACKETED** |

**Run totals, 2026-08-24 `industry_US`: 1 SCORED (`S74` → `FIRED-C`) · 0 `EXPIRED` · 0 silent skips ·
1 not-yet-arrived with a corrected structural diagnosis and a named successor date (`S102` → 08-25) ·
1 undated and named for the 23rd time (`S8`) · 5 REGISTERED (`S118` `S119` `S120` `S122` `S123`, all
both-sided) · 1 GRADED AND DROPPED with its ID consumed (`S121`).**

---

## Scored by the 2026-08-25 `industry_kr` run (appended to the MASTER scoring log — the log stays shared and un-split)

> ⚠ **Append-only.** 이 줄 위의 어떤 행도 재작성하지 않았다.
> ⚠ **소유권은 등록 데스크이고 배타성을 주지 않는다** — 아래 두 행 중 하나(`S102`)는 **US 등록 · KR 정산**이다
> (`S8` US등록/KR정산 · `S33`·`S28` KR등록/US정산 과 같은 선례).

| id | 등록 | 정산일 | 평결 | 정산한 런 | 관측 |
|---|---|---|---|---|---|
| **`S27`** | 2026-07-27 (`industry_kr` MACRO + DEEP-ENRG) | **`~2026-08 late`** (퍼지) | ★ **`FIRED-B`** | **2026-08-25 HANDOVER (`industry_kr`)** | **관측면(동결) = 「9차 지정의 휘발유·경유 상한, 7차 기준 ₩1,784/₩1,773 대비」.** 실측: 산업통상부 **2026-08-21 발표 · 08-22 00:00 시행 · 향후 4주간** ⇒ **휘발유 1,784 · 경유 1,773 · 등유 1,380 = 8차와 동일 = 동결** ⇒ **브랜치 B.** 국내 코퍼스 **8매체 교차**(mt·newsis·chosun·yonhap·einfomax·donga·mk·sedaily), 본문 2건 전문. 원문: *"9차 석유 최고가격을 기존 8차와 동일하게 유지"*(mt) · *"두 차례 연속 같은 수준"*(newsis) · *"최고가격제 4주 더 연장"*(sedaily). ★ **등록 시 명시한 안티시그널이 옳은 방향을 가리켰다** — 대통령 *"오히려 더 강화해야 할 것 같다"*(07-21 국무회의). **브랜치 B 의 의미가 실현됐다**: 브렌트 **93.8**(08-20) · 국제 휘발유 **114달러/배럴**(8월초 105) · 경유 **164**(148) 위에서의 **명목 동결 = 실질 강화** ⇒ **크랙 개선의 국내 전달 차단이 관측으로 확인**됐고 `M157` 의 **22.6×(SK이노)/37.6×(S-Oil) 영업이익 배수 노출**은 살아 있는 드래그다. ★ **교차확인 KPI 가 처음 날짜를 얻었다**: 손실보전 원가자료 **8월 말 접수 마감 → 연말께 규모 확정**(newsis 본문). 🚨 **프로세스 실패 기록**: 관측면은 **08-21 에 인쇄**됐는데 08-22·08-23·08-24 세 런이 전부 **「KR 정산 도래 0건」**으로 넘겼다 — 정산일이 `~2026-08 late` 라는 **퍼지 문자열**이라 **날짜 정렬 열거표에 한 번도 나타나지 않았다**. **`EXPIRED` 는 아니다**(오늘 채점) — **3런 지연은 실패로 기록**하고 처방은 `D347-KR` |
| **`S102`** | 2026-08-19 (`industry_US` PREMORTEM) | **"first close covering 2026-08-21"** | **`FIRED-C`** | **2026-08-25 HANDOVER (`industry_kr`)** | **7번째 독립 조회에서 관측면이 도착했다.** `DGS2` **4.24 (2026-08-21)** ⇒ **A(≥4.30) ❌ · B(≤4.08 ∧ `30y−10y` ≥0.59) ❌** ⇒ **C.** 부수 실측 `DGS10` 4.74 · `DGS30` 5.27 ⇒ `30y−10y` **0.53**. ⚠ **등록 시 스스로 「C 가 공개된 favourite」이라 적었다**(`DGS2` 실현 9관측 범위 4.15–4.25) ⇒ **정보량 낮은 정산이고, A·B 어느 쪽도 반증되지 않았다.** ★ **US `M859` 의 관측 하나가 오늘 뒤집혔다**: *"`DGS2` 가 4.19 를 네 세션 연속 — 프론트엔드는 FOMC 의사록을 관통해 전혀 움직이지 않았다"* → **08-21 에 +5bp 로 4.24.** 커브는 **평행 이동**(2y +5 · 10y +5 · 30y +4bp)이라 **기울기가 아니라 레벨 이야기**다. 🚨 **등록된 VOID 안티시그널(창 내 재무부 리펀딩 발표 — 08-19 Bessent 장기물 바이백 확대)이 살아 있고, 08-22 US 런이 이미 「VOID RECOMMENDED」로 표시**했다 ⇒ **`VOID` 여부의 판정은 소유자(`industry_US`)의 몫이고, 이 런은 letter 대로 `FIRED-C` 만 기록한다.** 🚫 **letter 를 intent 로 바꿔 읽지 않았다.** ★ **`D333-KR` 6번째 재현**: 오늘도 `DGS*` 는 08-21, `T10YIE`·`RRPONTSYD` 는 08-24 ⇒ **H.15 계열이 파생 시리즈보다 1영업일+ 늦다**. **KR 데스크가 만든 이 진단이 US 08-24 런의 「후속 시도일 08-25」 예측을 정확히 맞혔다** |

**정산 불가 행 (계속)**

| id | 상태 | 이 런의 처리 |
|---|---|---|
| **`S8`** | `[blank]` **날짜 없음** | 🚨🚨 **정산 불가 24런 연속.** 어느 클럭으로도 정산할 수 없다. **사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다(P5).** ⚠ **비용은 이제 닫힌 값이 아니라 열린 값이다** — *"`S8` 이 정산 불가라서 쓴 행"* 인 `S74` 는 **08-24 에 `FIRED-C` 로 정산되고 은퇴**했는데, `S8` 은 같은 대상을 여전히 날짜 없이 들고 있다 |

**KR 소유 ARMED 전수표 (2026-08-25 확인) — `S27` 정산 후 남은 것**

| 정산일 | 행 | 정산일 | 행 |
|---|---|---|---|
| **2026-09-04** | `S67-KR` | 2026-09-09 | `S58-KR` |
| ~2026-09-14 | `S61-KR` | 2026-09-15 | `S62-KR` |
| **2026-09-19** | `S64-KR` · `S65-KR` · `S68-KR` | 2026-09-30 | `S45` · `S54-KR` |
| 2026-10-12 | `S60-KR` | 2026-10-30 | `S49-KR` |
| 2026-10-31 | `S34` · `S53-KR` | 2026-11-04 | `S59-KR` |
| 🆕 **날짜 미파싱 행** | **0건** — `S27` 정산으로 비었다. **칸 자체는 `D347-KR` 처방으로 남긴다** | | |

⇒ **가장 이른 KR 정산은 2026-09-04(`S67-KR`)로 10일 앞.**

**Run totals, 2026-08-25 `industry_kr`: 2 SCORED (`S27` → `FIRED-B` · `S102` → `FIRED-C`) ·
0 `EXPIRED` · 0 silent skips · 1 unscoreable-by-construction (`S8`, 24th run) · 0 newly registered brackets.**
⚠ **신규 등록 0건인 이유를 적는다**: 이 런은 **무인 실행이고 사이즈·집행을 만들지 않으므로**, 새 브래킷 등록보다
**이미 등록된 행의 정산과 두 원장 감사**에 예산을 썼다. **후속 등록 후보 2건은 이름으로 남긴다** —
① **`S27` 손실보전 후속**(8월 말 원가자료 접수 → 연말 규모 확정; 정유 두 이름의 22.6×/37.6× 노출이 숫자가 되는 순간)
② **한미약품 HM17321 2상 진입 여부**(오늘 `🔴RESOLVED` 로 드롭한 이름의 다음 촉매).


---

## MASTER INDEX — appended 2026-08-25 by the `industry_US` run (PREMORTEM registrations)

> ⚠ **Append-only.** ID 3-grep at WRITE time across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`:
> `S124`–`S126` **0 hit**. Current highest **`S123`**.

| ID | Market | File | One line |
|---|---|---|---|
| **S124** | US | `SCENARIOS_US.md` | ★★★ **Does IT's breadth repair through its own two prints?** The row that tests this run's ONLY verdict change (`IT` N → UW). Observable = COUNT of the 56 `us_top300` IT names with positive 5-session excess vs `SPY` at the **2026-08-31** close. **A ≥ 30** (252d median) / **B ≤ 13** / C 14–29. D93: mean 29.5, sd 9.0, p05 13, p50 30, p85 39 ⇒ A ≈50% / B ≈6% / C ≈44%. State at registration **13 of 56 = 5.6th percentile**. ★ A **cross-sectional count is priced by no straddle**, so the threshold is outside `NVDA` ±6.13% and `MRVL` ±13.3% (both 08-28 D3) by construction. Deliberately not a 5th reading of the `NVDA` print |
| **S125** | US | `SCENARIOS_US.md` | ★★ **The agricultural half of the trade war** — `D342`'s twice-named gap. `ADM` 5-session excess vs **`XLP`** at the **2026-09-11** close, a window containing Canada's **09-08** effective date. **A ≥ +0.602** (p50) / **B ≤ −6.146** (p05) / C between. State **−6.511 = 4.4th percentile, already inside B** ⇒ **B pre-declared LOW-information, A informative (B4)**. No event-dated straddle exists; stated as unavailable rather than fabricated. Correlated with `S123` (Industrials leg) — one policy event, two sectors |
| **S126** | US | `SCENARIOS_US.md` | ★★ **August payrolls: is `INDU UW−` a tariff call or a cycle call?** `XLI` 5-session excess vs `SPY` at the **2026-09-04** close. **A ≥ −0.087** (p50) / **B ≤ −2.500** (p05) / C between. D93: mean +0.012, sd 1.619. State **−2.738 = 2.8th percentile** ⇒ B low-information, A informative. ★ Exists because **every existing Industrials test settles on the wrong date** — `P92`/`P93` on 08-28, eleven days BEFORE the tariffs take effect (`D342`); `S123` on 09-12, after. **B does not confirm the tariff story, it only rules out the labour one** — asymmetry stated |


---

## MASTER scoring log — entries added by the `industry_US` run of 2026-08-25 (append-only)

> ⚠ This spine section is **deliberately NOT split by market**, so an `EXPIRED` row cannot hide in the
> other market's file. **ID 3-grep at WRITE time**: `S124`–`S126` **0 hit**; current highest **`S123`**.

| ID | Settle date | Verdict | Observed | Threshold was | Note |
|---|---|---|---|---|---|
| **`S102`** | "first close covering 2026-08-21" | ★★★ **OWNER RULING: `FIRED-C` STANDS — NO VOID** | The `industry_kr` desk scored it `FIRED-C` this morning on `DGS2` **4.24 @ 2026-08-21** (A ≥4.30 ❌ · B ≤4.08 ∧ spread ≥0.59 ❌) and correctly deferred the VOID question to the registering desk. **This desk rules the anti-signal did NOT fire.** The clause named *"an **intermeeting Fed policy action** or a **Treasury refunding announcement**"*; the 08-19 event was a **buyback-programme doubling** — 239 matching articles read (`fts search "Treasury buyback" --days 10 --scope foreign`), and **no outlet describes a refunding**: *"Bessent Doubling The Treasury Buyback Program"* [seekingalpha 08-23] · *"Deutsche Bank calls Treasury buyback doubling similar to 'operation twist'"* [investing_en 08-19] | frozen at registration, unchanged | **Three grounds**: (a) the LETTER — a QRA is a distinct named scheduled event and a buyback-schedule change is not one; (b) **the desk's OWN 08-22 PREMORTEM drew the same line three days later**, writing *"an emergency Treasury operation (**not a scheduled buyback**)"* and noting *"the buyback expansion already executed on 08-19"*; (c) widening a frozen clause after the fact converts a forecast into a description. ⚠ **The counter-argument is RECORDED, not suppressed**: a buyback doubling is a deliberate intervention on the long end, which is the leg branch B rests on, and `M870` measured the long end did **not** respond. ⇒ **`D356`** — name the MECHANISM, list instruments as examples |
| **`S8`** | `[blank]` **undated** | 🚨🚨 **UNSCOREABLE, 25th consecutive run** | — | — | **A human must `VOID` it or re-register it with a date (P5).** ⚠ Its cost stays open: `S74` — the row written *because* `S8` was unscoreable — settled and retired on 08-24, and `S8` still holds the same object with no date |
| **`P79`** | **2026-08-25 (tonight's close)** | ⏳ **PRE-SETTLE, not a score** | **−10.852** at the 08-24 settled close — legs `COHR −20.371` · `LITE −13.128` · `HPE −7.801` · `AVGO −7.389` · `ANET −5.573`. **INSIDE branch B**, i.e. a second sub-p05 week | A ≥ **+8.02** (252d p85) · B ≤ **−7.72** (252d p05) | Trajectory: **−12.425** (registration 08-20) → −7.178 (08-21) → −5.609 (08-22) → **−10.852** (08-24). ⚠ **The desk's own draft first read −5.298 on the wrong window** (the partial 08-18→08-24); the row freezes a **trailing** 5-session window. **Both figures are written down** (`D48`/`C1`). ⚠ Branch A retains a live mechanism: `Nasdaq-100` spec at the **4th %ile short with +30,838 weekly covering** `[COT 08-18]`. **PAST-DUE ON ARRIVAL for the 08-26 run** |
| **`S108`** | **2026-08-25 (tonight's close)** | ⏳ **PRE-SETTLE, not a score** | **+0.484** with **2 of 3 sessions elapsed** — legs **`XLP +2.382` · `XLRE +0.440` · `XLU −1.371`** | A ≥ **+1.68** (p85) · B ≤ **−1.76** (p15) · C between (favourite, ≈70%, disclosed at registration) | Inside C and **moving AWAY from A** (state at registration **+1.432 = 78.6th %ile**). ★ **The dispersion is the more informative number: the three legs span 3.75pp and one is NEGATIVE** ⇒ *"the three underweights rip together"* — the row's own premise — **is not what the tape is doing**, and that is visible before its settle. **PAST-DUE ON ARRIVAL for the 08-26 run** |
| **`S124`** | **2026-08-28→31** | — | — | — | **ARMED** — COUNT of the 56 `us_top300` IT names with positive 5-session excess vs `SPY` at the **08-31** close. **A ≥ 30** (252d median) / **B ≤ 13** / C 14–29. D93: mean 29.5, sd 9.0, p05 13, p50 30, p85 39 ⇒ **A ≈50% / B ≈6%**. State **13 of 56 = 5.6th percentile**. ★ **A cross-sectional COUNT is priced by no straddle**, so it sits outside `NVDA` ±6.13% and `MRVL` ±13.3% by construction. **The row that tests this run's ONLY verdict change** |
| **`S125`** | **2026-09-11** | — | — | — | **ARMED** — `ADM` 5-session excess vs **`XLP`** at the 09-11 close, a window containing Canada's **09-08** effective date. **A ≥ +0.602** (p50) / **B ≤ −6.146** (p05). State **−6.511 = 4.4th %ile, ALREADY inside B** ⇒ **B pre-declared LOW-information, A informative** (`B4`). Fills `D342`'s twice-named gap. No event-dated straddle exists ⇒ stated as unavailable, not fabricated |
| **`S126`** | **2026-09-04** | — | — | — | **ARMED** — `XLI` 5-session excess vs `SPY` at the 09-04 close (August NFP). **A ≥ −0.087** (p50) / **B ≤ −2.500** (p05). State **−2.738 = 2.8th %ile** ⇒ B low-information, A informative. ★ Exists because **every existing Industrials test settles on the wrong date** — `P92`/`P93` on 08-28, **eleven days BEFORE** the tariffs take effect (`D342`); `S123` on 09-12, after. **B does not confirm the tariff story, it only rules out the labour one** — asymmetry stated |

**Run totals, 2026-08-25 `industry_US`: 0 newly scored by this desk · 1 OWNER RULING (`S102` no-void,
`FIRED-C` stands) · 2 PRE-SETTLE readings recorded (`P79` inside branch B, `S108` inside C) ·
0 `EXPIRED` · 0 silent skips · 1 undated and named for the 25th time (`S8`) · 3 REGISTERED
(`S124` `S125` `S126`, all both-sided, all `D93`-baselined before freezing).**
⚠ **The zero-newly-scored is a CLOCK fact, not a diligence fact**: this desk runs pre-market, so a row
dated D always settles on D's US close and is scored by the D+1 run. **`P79` and `S108` are dated
TODAY and are named here so the 08-26 run cannot skip them silently.**

---

## MASTER scoring log — entries added by the `industry_kr` run of 2026-08-26 (append-only)

> ⚠ This spine section is **deliberately NOT split by market**, so an `EXPIRED` row cannot hide in the
> other market's file. **ID 3-grep at WRITE time**: no new `S`/`P` ids were registered by this run.
> ★ Both rows below were **explicitly handed to this run by the 2026-08-25 `industry_US` desk**
> (*"`P79` and `S108` are dated TODAY and are named here so the 08-26 run cannot skip them silently"*).

| ID | Settle date | Verdict | Observed | Threshold was | Note |
|---|---|---|---|---|---|
| **`P79`** | **2026-08-25 close** | ★ **`FIRED-C`** | `EW{COHR, LITE, HPE, AVGO, ANET}` trailing 5-session excess vs `SPY`, **08-18 close → 08-25 close** = **−2.977pp**. Legs: `COHR −5.768` · `LITE **+1.604**` · `HPE −3.840` · `AVGO −5.920` · `ANET −0.959`; `SPY` −0.201%. `SPY`'s terminal bar verified **08-25** | A ≥ **+8.02** (252d p85) · B ≤ **−7.72** (252d p05) · C between | ★★ **The information is in the trajectory, not the branch**: **−12.425 (registration 08-20) → −7.178 → −5.609 → −10.852 (08-24) → −2.977 (08-25)** — **+7.9pp in one roll**, because the trailing window dropped 08-17 and took on 08-25. ⇒ **the "second consecutive sub-p05 week" state the 08-25 desk recorded was erased by a single session.** 🚫 Not readable as "the rebound came" — roll-off and new session are mixed and the decomposition is out of this stage's scope. ⚠ The 08-25 desk's own note that its first draft read −5.298 on the wrong window stands; **this row used the registered trailing 5-session window** |
| **`S108`** | **2026-08-25 close** | **`FIRED-C` by the letter** 🚨 **VOID question handed to the owner (`industry_US`)** | `EW{XLU, XLRE, XLP}` 3-session excess vs `SPY`, **08-20 close → 08-25 close** (endpoints verified on the `XLU` bar series) = **−0.108pp**. Legs: **`XLP` +0.972 · `XLRE` +0.187 · `XLU` −1.485**; `SPY` +0.434% | A ≥ **+1.68** (p85) · B ≤ **−1.76** (p15) · C between (the disclosed favourite, ≈70%) | ★ **State at registration was +1.432 = 78.6th percentile, leaning A; it finished at the middle.** ★★ **The 08-25 desk's dispersion point survives to settlement**: the three legs span **2.46pp and one is negative**, so the row's own premise — *"the three underweights rip together"* — **was not observed even in the branch that fired.** 🚨 **Premise-invalidation candidate**: the row froze its window around *"Warsh's Jackson Hole D-0, 2026-08-21"*, and **`R93` (08-22 US) established the speech is 08-27~29** ⇒ **the event never occurred inside the window.** ⚠ **But that reason is NOT in the row's registered anti-signal list** (CPI/PPI/PCE · intermeeting FOMC · Treasury refunding change), **and the owner ruled on `S102` one run earlier that the letter governs and no VOID applies.** ⇒ **This run records the letter and refuses to convert letter into intent.** `industry_US` decides |
| **`S8`** | `[blank]` **undated** | 🚨🚨 **UNSCOREABLE, 26th consecutive run** | — | — | **A human must `VOID` it or re-register it with a date (P5).** Its cost stays open: `S74` — the row written *because* `S8` was unscoreable — settled `FIRED-C` on 08-24 and retired, and `S8` still holds the same object with no date |

**Not-yet-arrived, named so they cannot be skipped silently** — settling at **tonight's US close
(2026-08-26)**: **`S101`** · `S79`(leg settles 08-27) · `S103` · `P77` · `P78` · `P80` · `P90`.
🚨 **`S101` asks from the US side exactly the question `C15` is stuck on — whether the `vol_surge`
gate costs the desk return. The 2026-08-27 run must pick it up.**

**KR-OWNED ARMED ROSTER (verified in full 2026-08-26) — earliest settle is 9 days out**

| Settle | Rows | Settle | Rows |
|---|---|---|---|
| **2026-09-04** | `S67-KR` | 2026-09-09 | `S58-KR` |
| ~2026-09-14 | `S61-KR` | 2026-09-15 | `S62-KR` |
| **2026-09-19** | `S64-KR` · `S65-KR` · `S68-KR` | 2026-09-30 | `S45` · `S54-KR` |
| 2026-10-12 | `S60-KR` | 2026-10-30 | `S49-KR` |
| 2026-10-31 | `S34` · `S53-KR` | 2026-11-04 | `S59-KR` |
| **UNPARSED-DATE ROWS** | **0** — the column is kept per the `D347-KR` prescription; `S27` went unscored for 3 runs precisely because it had no parseable date | | |

**Run totals, 2026-08-26 `industry_kr`: 2 SCORED (`P79` → `FIRED-C` · `S108` → `FIRED-C`, VOID
deferred to owner) · 0 `EXPIRED` · 0 silent skips · 1 unscoreable-by-construction (`S8`, 26th run) ·
0 newly registered brackets.**
⚠ **Why zero registrations, stated rather than left blank**: this run is **unattended and produces no
sizing or execution**, so it prioritised settlement integrity and ledger closure over new brackets.
★ **One registration obligation is nonetheless recorded for the next attended run**: `EVENT_ALPHA`
card 5 (the nuclear-chain money move) and `BET §A-3` (`064350`'s three-legged B2 case) are both
**falsifiable and dated** — `064350`'s 2026Q3 filing (~2026-11-16) is a natural observable, and the
run filed it to `missed_ledger` with that date rather than leaving it unrecorded.

---

## MASTER INDEX — appended 2026-08-26 by the `industry_US` run (PREMORTEM registrations)

> ⚠ **Append-only** (`D165`), staged in a scratchpad first (`D357`).
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`: `S127` `S128`
> → **0 hits** in all three. Highest existing before this append: **`S126`**.
> 🚨 **The same grep caught a collision earlier in this run**: `M927`–`M934` were already allocated by
> this morning's `industry_kr` run, so the US desk's measured rows start at **`M935`**. The `D76`
> class fired and was **prevented for a 3rd time in 3 days**.

| ID | Market | File | One line |
|---|---|---|---|
| **`S127`** | US | `SCENARIOS_US.md` | ★★★ **`AVGO` 2026-09-02 — the held name with the book's worst `rs60` (−24.1) and no row until now.** `AVGO` exc5 vs `SPY`, window 09-01 → **09-08**: **A ≥ +5.928 (p85) · B ≤ −4.922 (p15) · C between (favourite, ~70%)**. State at registration **−5.920 = 9.9th %ile — already inside B's zone**. 🚨 **Thresholds are NOT from the options market**: `module_flow` returns ±1.3% at an **08-26 D0 expiry** for a 09-02 print (`D353`/`M948`), so the row is **MEDIUM-RESOLUTION** with an obligation to re-derive from the 09-04-or-later straddle at the 08-28/08-31 run |
| **`S128`** | US | `SCENARIOS_US.md` | ★★★ **The out-of-sample test of the desk's own strongest cell.** `EW{35 reversal, rs20>0 ∧ rs60<0}` − `EW{117 decay, rs20<0 ∧ rs60>0}`, both frozen from the 2026-08-26 sweep, 5-session, settle **09-09**: **A ≥ +5.433 (p85) · B ≤ −3.158 (p15) · C between**. State **−0.556 = 31.7th %ile**, i.e. currently **against** the ledger's sign. **39.1% of the board is a decayer and 4 of 11 holdings sit there** (`M949`). ⚠ Estimator centre is **+1.268, not zero**, disclosed. **B kills a Bonferroni-passing cell before it becomes doctrine** |

### Rows this run examined and DECLINED to register, with the reason (so "we never looked" stays distinguishable from "we looked and passed")

| Binary | Why no new row |
|---|---|
| **`NVDA` 2026-08-26 (D-0)** | **SEVEN rows already own it** — `P90` · `S79` · `S115` · `S117` · `S118` · `S103` · `S113`. An eighth is `D343` in its purest form. Implied **±6.0% (08-28, D2)** correctly spans the print; P/C 0.5, skew 0.0 ⇒ complacent. **The mandate is met: this is not a one-way tilt** |
| **`MRVL` 2026-08-27** | **`S116`** owns it. Registered implied ±11.31%; today the same 08-28 chain reads **±10.3%**, so the **±12.0pp thresholds still sit OUTSIDE the implied move** ⇒ still information-carrying. **Not re-banded** (`D242`) |
| **July PCE 2026-08-28** | **08-28 carries NINE rows** (`D343`). `S104` · `S111` · `S112` own the print |
| **Jackson Hole 08-27~29** | `S120` (08-28) and `S112` (08-31) own it. `D365` filed on `S108`'s construction defect (its frozen window contained no event) |
| **`FRO` 2026-08-28** | `S109` is armed — but **`FRO` is outside `us_top300`** (`D341`), so the gap is an instrument gap, not a bracket gap |
| **Aug NFP 2026-09-04** | `S126` owns it |
| **Hormuz statement** | 🚨 **`S8`, UNDATED, unscoreable for a 27th consecutive run.** Its object was in the 08-25 head layer (*"Iran, Oman Push Talks for 'Interim' Reopening of Hormuz Strait"*, 9 art / 8 outlets) **and** in `CATALYST_WATCH` as an explicitly undated binary. **A human must `VOID` it or re-register it with a date (P5)** |

---

## MASTER scoring log — appended 2026-08-27 by the `industry_kr` run (the log stays shared and un-split)

> ⚠ **All three rows below are US-owned.** The KR desk scored them because **yesterday both desks
> handed `S101` forward by name**, and because the MASTER INDEX rule says a past-dated row in the
> other market's file is still this run's to open. **Frozen observables were used exactly as
> registered; no threshold was improvised.**
> All measured on **settled US closes, 2026-08-19 → 2026-08-26, benchmark `SPY` inline (5 sessions,
> `SPY` −0.387%)**.

| ID | Owner | Settle | Frozen observable | **Measured** | Thresholds | **Verdict** |
|---|---|---|---|---|---|---|
| **`S101`** | US | 2026-08-26 | `EW{DELL,PANW,SHOP,ABNB,CRWD,DASH,PYPL,TMO,BKNG,AXON}` exc5 **minus** `EW{KKR,RTX,LITE,ORCL,CSCO,MA,BAC,WMT}` exc5 | **erased EW +0.539** · **admitted EW +1.283** ⇒ **spread −0.744pp** | A ≥ +4.45 ❌ · B ≤ −3.88 ❌ | **`FIRED-C`** |
| **`P78`** | US (MACRO) | 2026-08-26 | range of `exc5` vs `SPY` across `{XLU, XLRE, XLP, XLV}` | `XLRE` **+0.610** · `XLP` +0.075 · `XLU` −0.771 · `XLV` **−0.831** ⇒ **range 1.440pp** | A ≥ 4.71 ❌ · **B ≤ 1.69 ✅** | **`FIRED-B`** |
| **`P80`** | US (MACRO) | 2026-08-26 | 3-2-1 crack **and** `EW{MPC,VLO,PSX}` exc5 | **EW +0.690** (`VLO +0.899` · `MPC +0.809` · `PSX +0.363`, all within 0.54pp) · crack **68.134** on the last non-stub bar (08-25) / **57.593** on the 08-26 stub | A: crack ≥65 ✅ ∧ EW ≥ +0.86 ❌(short by 0.17pp) · B: crack ≤58 ∧ EW ≤ −3.74 ❌ | **`FIRED-C`** — **robust to which bar is read** |

**Notes that belong with the scores, not after them:**
- **`S101` — the VOID anti-signal was actively measured, not waved through.** The row voids on
  *"an earnings print at ≥3 of the 10 erased names inside the window"*. Measured: **0 of 10 in-window**
  (`DELL` 09-01 · `PANW` 09-01 · `SHOP` 08-05 · `ABNB` 08-06 · `DASH` 08-05 · `PYPL` 07-28 ·
  `TMO` 07-23 · `BKNG` 08-04 · `CRWD` 06-03; **`AXON` lookup failed ⇒ `unknown`, C3**). Max possible
  1 < 3 ⇒ **not void.**
- **`S101` — `W5`, and it matters here**: the admitted basket's **entire** +1.283 comes from
  **`LITE` +13.852**. Ex-`LITE` the admitted EW is **−0.513** and the spread **flips sign to +1.05**
  (still C). The erased basket spans **13.8pp** internally. **Neither basket is summarisable by its EW.**
- **`S101` — trajectory over branch**: registered at **−0.677**, pre-settle read **+1.616** ("inside C,
  leaning A", 08-26 US HANDOVER), final **−0.744** — **−2.36pp in one session.**
- **`P78` — the largest single-session branch swing this desk has recorded.** Its pre-settle read was
  **4.889pp, ABOVE branch A**, and the owning report wrote *"if it holds one session, the 'duration
  complex is one bet' framing is falsified."* It did not hold; **the opposite branch fired**, and the
  leg ordering inverted (`XLV` best → worst). ⇒ **the four duration-underweight legs measure as ONE
  object on this observable.** 🚫 **Not transferred to KR** (`W1`).
- **`P80` — the crack leg's 08-26 value is an artifact and the verdict survives it anyway.** The
  08-26 futures bars are stubs (`RB=F` **127** contracts, −10.1% in one session; `CL=F` 1,158 ·
  `HO=F` 111 · `BZ=F` 64), and `RB=F` alone drives the crack from 68.134 to 57.593. **B's crack leg
  would have "fired" on 127 contracts**; the EW leg blocked it. Next time it may not.

### Not scored, and why — named so they cannot be skipped silently

| ID | Owner | Status |
|---|---|---|
| **`P77`** | US | ⏸ **DEFERRED — the registered observable has not been published.** `DGS30`'s last `[FRED]` observation is **2026-08-25 = 5.17**; there is no 08-26 bar (`D333`, **9th reproduction**; the joint rate date advanced 08-24 → 08-25). ⚠ **Pre-settle read disclosed now rather than discovered later**: 5.17 sits **inside branch A (≤5.18) by 0.01** — 🚫 **do not inherit that as "A fired."** **Readable 08-28 at the earliest.** |
| **`P90`** | US | ➡ **HANDED TO OWNER.** Its own registration says *"scored jointly with `S115`"* and its observable is the **print's body** (margin expansion vs cost pass-through), not a price. **This run supplies the number the owner needs**: `NVDA` FY27 Q2 adjusted **gross margin 75%, "in line with guidance"**; adj. EPS **$2.22** vs $2.10; revenue **$96.22bn** vs $92.17bn; Q3 guide midpoint **$108.0bn** vs $105.2bn; **stock −2.08% after hours, −1.59% in the regular session** (`einfomax` 08-27). |
| **`S79`** | US | ⏳ Not due — settles at the **08-27** US close. |
| **`S103`** | US | ⏳ Window **08-25 → 08-29** still open; **pre-declared low-information** by its own registration (hand-set ±5.0pp bands inside a ±6.1% implied move). |
| **`S8`** | US | 🚫 **Unscoreable for a 27th consecutive run — the row has no date.** A human must `VOID` it or re-register it with one (P5). |

## MASTER INDEX — appended 2026-08-27 by the `industry_kr` run

**New brackets registered by this desk: 0.** ⚠ **The reason is written rather than left implicit.**
This run froze its observables **before the 09:00 BOK decision** and registered its both-sides
proposition as **`M-111` inside `MACRO_REPORT §F`**, where this desk's `M-1xx` propositions live —
they carry branches, mandatory anti-signals, Track KPIs and dated catalysts, but they are **not
`D93`-banded numeric brackets** and are not filed here. **`M-111` · `M-112` · `M-113` are therefore
findable in `REPORT/industry_KR/MACRO_REPORT.md`, not in this index**, and the next KR run must read
them there. ⇒ **KR-owned ARMED rows are unchanged; the earliest is `S67-KR` on 2026-09-04.**

**KR-owned ARMED roster, re-verified in full this run (no row without a parsed date):**
`S67-KR` 09-04 · `S58-KR` 09-09 · `S61-KR` ~09-14 · `S62-KR` 09-15 ·
`S64-KR`·`S65-KR`·`S68-KR` 09-19 · `S45`·`S54-KR` 09-30 · `S60-KR` 10-12 · `S49-KR` 10-30 ·
`S34`·`S53-KR` 10-31 · `S59-KR` 11-04. **Unparsed-date rows: 0** (the `D347-KR` column is kept even
when empty — it was absent for three runs and `S27` went invisible in exactly that gap).


## MASTER INDEX — appended 2026-08-27 by the `industry_US` run (PREMORTEM registrations)

> ⚠ Append-only (`D165`). ID 3-grep at WRITE time across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`
> (excluding this run's own files): `S129` `S130` → **0 hits**. Highest existing `S128` (2026-08-26 US).

| id | owner desk | file | object | settles | status |
|---|---|---|---|---|---|
| **`S129`** | `industry_US` | `SCENARIOS_US.md` | `ADM` 5-session excess vs `SPY`, 09-02 → 09-09 — the Canadian retaliation's **agricultural** leg, unbracketed for 3 runs (`D342`) | **2026-09-09** | ARMED |
| **`S130`** | `industry_US` | `SCENARIOS_US.md` | `NVDA` / Hugging Face **$12.9bn** — confirmation leg + 10-session excess vs `SPY`, 08-27 → 09-10 | **2026-09-10** | ARMED |

### Scored by the 2026-08-27 `industry_US` run (appended to the MASTER scoring log — the log stays shared and un-split)

| id | owner | verdict | measurement that settled it |
|---|---|---|---|
| **`P90`** | `industry_US` | **FIRED-A** | `NVDA` FQ2 FY2027 (printed 2026-08-26 AMC): gross margin **75.0%** vs **74.9%** the prior quarter (**+10bp ≤ the 50bp tolerance**) and FQ3 guide **~74.0%**, i.e. **−100bp ≤ the reported quarter**. **Both branch-A conjuncts met.** Sources: `yahoo_finance` 08-27 body (*"gross margin rose to 75% in the quarter, compared with 74.9% in the previous quarter and 72.4% a year earlier"*; *"guidance falling from 75% … to about 74%"*) corroborated by `nasdaq`/`fool` 08-26 (*"fiscal third-quarter gross margin guide of 74% is 100 basis points lower than what it just reported"*). Revenue leg cross-checked to **SEC XBRL $96.22bn**. Anti-signal did not fire (the company reported and did guide GM). ⚠ **Construction finding recorded, not improvised around** (`D380`): the row never named GAAP vs non-GAAP and its 50bp tolerance is finer than its likely source's precision — scoreable only because both legs clear by a wide margin |

### Rows NOT scored by this run, named rather than dropped

| id | why not scored |
|---|---|
| `S79` `S81` `S115` `S117` `S119` `P83` `P96` | **Observable is the 2026-08-27 settled close, which had not occurred** — the run fires at 09:1x ET, pre-market (`D355` class). **NOT `EXPIRED`**: the observable has not come and gone, it has not arrived. Seven rows on one date; the next run inherits them explicitly |
| `P77` | **Deferred, 2nd consecutive run** — `DGS30` `[FRED]` has no 2026-08-26 bar (series ends 08-25 at **5.17**); `D333`'s **10th** reproduction. ⚠ 5.17 sits 1bp inside branch A and **that is stated, not scored** |
| `P97` | unreadable — the dollar leg (`DTWEXBGS`) ends **08-21**, seven days behind the joint date the row requires |
| `P86` | **PCE conjunct MET** (July core PCE **+0.2% MoM ≤ +0.20**, printed **08-26** not 08-28 — `M977`/`M978`); rate conjunct unreadable (`DGS2` 4.17, A ≤ 4.10 / B ≥ 4.32). Stays ARMED |
| `S8` | unscoreable for a **28th** consecutive run — named again rather than dropped |
| `S101` `P78` `P80` | taken by the sibling `industry_kr` desk on 2026-08-27; recorded, not re-scored |
| `P90` | ✅ scored above — handed to this desk by the KR run, which correctly declined an unowned row |


---

# ═══ MASTER SCORING LOG — append by `industry_kr`, 2026-08-28 (Fri, pre-open KST) ═══

> ⚠ **Ownership is the REGISTERING desk and confers no exclusivity.** All four rows below are
> **`industry_US`-owned** and were past-dated at this desk's run time with no US run in between;
> each was settled **only against its pre-registered observable and threshold** (`D242` — no
> threshold was improvised, no band re-derived).
> ⚠ **No new bracket was registered by this run.** The KR desk's earliest own settle is `S67-KR`, 09-04.

| id | owner | verdict | evidence |
|---|---|---|---|
| **`S115`** | `industry_US` | ★★★ **`FIRED-A`** | Frozen observable = `NVDA` **1-session return on the first settled close after the print (2026-08-27)**. Measured **08-26 209.66 → 08-27 227.98 = +8.738%**, excess vs `SPY` (+0.655%) = **+8.083pp**. Branch A line **≥ +7.0%** ⇒ **cleared by 1.74pp**, and the move sits **outside the ±6.11% implied move** recorded at registration. Anti-signal (NVDA did not report 08-26 / no full US cash session 08-27) **NOT fired** — both conditions normal |
| **`P90`** | `industry_US` | ✅ **already `FIRED-A` (scored by the US run of 2026-08-27) — joint leg with `S115` NOW CLOSED** | `S115`'s registration declared *"branch A **with** gross-margin expansion falsifies `P90`; branch A **with flat** margin confirms it."* The US run measured **gross margin 75.0% vs 74.9% prior = +10bp ≤ the 50bp tolerance (flat)** with an FQ3 guide of **~74.0%**. ⇒ **A × flat ⇒ `P90` confirmed.** 🚨 **This KR run's HANDOVER §2-d wrongly wrote that `P90` was being handed forward for a 2nd run; the writeback pass reading THIS log refuted it one stage later.** Correction appended (HANDOVER §11), original left standing (`D48`), mechanism registered as **`D393-KR`** |
| **`S117`** | `industry_US` | **`FIRED-B`** — ⚠ **with a construction finding recorded beside the verdict** | Frozen observable = `MU` **1-session excess vs `NVDA`** on 2026-08-27, each vs its own 08-26 close. Measured **`MU` −0.321% − `NVDA` +8.738% = −9.059pp** ≤ branch B's **−3.0pp** ⇒ **B by 6.06pp.** 🚨 **But B's prose reads *"it was `NVDA` beta and `MU` is a levered follower"*, and the realised signs are OPPOSITE** — a levered follower moves further in the SAME direction; `MU` fell while `NVDA` rose 8.7%. **The A/B bands cannot express the third state (downside decoupling).** Recorded as a defect in the row's construction; **the threshold was NOT re-derived** (`D242`). Anti-signal (a `MU`-specific dated announcement inside 08-24→08-27) **judged NOT fired**: the window's top `MU` item is *"Micron's Customers Are Putting Up $22 Billion…"* (`fool`/`nasdaq` **08-24**), the **same secondary-writeup class the registration itself excluded** for the 08-20 item — the ambiguity is recorded rather than resolved |
| **`P77`** | `industry_US` | ★ **`FIRED-A` — by 0.00bp** | Frozen observable = `DGS30` **at the first `[FRED]` close covering 2026-08-26**. That bar **published today** at **5.18**; branch A is **≤ 5.18**, branch B **≥ 5.38** ⇒ **A fires with zero margin — 1bp higher and this is C.** Anti-signal (an intermeeting Fed action **or** a Treasury refunding announcement in the window) **NOT fired**: `intermeeting` 3d **0 hits**; `"quarterly refunding"` 3d **7 hits, all commentary on the 08-19 buyback expansion**, no new refunding announcement. ⚠ **`D333` blocked this row on 08-26 and 08-27 and then released it into a rounding-digit decision** — carry the verdict as *"passed on the thinnest possible margin"*, not as *"measured"* |
| **`S119`** | `industry_US` | ⛔ **PAST-DATED AND DELIBERATELY NOT SCORED — named, not silently skipped** | Frozen observable = *"the equal-weight Energy basket's 3-session excess vs `SPY`, 08-24 close → 08-27 close"*, bands ±2.60pp. 🚨 **The row never enumerates the basket's membership**, and it does not name a file+date that would fix it. Reconstructing it here would make **this desk** choose the observable, which `C5` forbids. ⇒ **NOT `EXPIRED`** — handed to `industry_US` by name, with **`D388-KR`** registered: *"a row whose observable is a basket must enumerate that basket's membership (tickers, or a file name + date that fixes it) at registration."* `S119` is that rule's first specimen |
| `S8` | `industry_US` | ⛔ unscoreable for a **29th** consecutive run — named again rather than dropped (date field still `[blank]`; human item) |
| `S116` `S118` `S120` `S111` `P67` `P81` `P85`–`P89` `FRO` | `industry_US` | ⏳ **NOT YET DUE at this desk's run time** — all settle on the **2026-08-28 US close / a FRED bar covering 08-28**, i.e. after this pre-open KR run. Listed so the absence is a stated fact, not a gap |
| KR-owned rows | `industry_kr` | ⏳ **ZERO due today.** Full forward table: **09-04** `S67-KR` · **09-09** `S58-KR` · **~09-14** `S61-KR` · **09-15** `S62-KR` · **09-19** `S64-KR`·`S65-KR`·`S68-KR` · **09-30** `S45`·`S54-KR` · **10-12** `S60-KR` · **10-30** `S49-KR` · **10-31** `S34`·`S53-KR` · **11-04** `S59-KR`. **Date-unparsed rows: 0** |

### 🆕 A finding about this log itself — `D389-KR`

**Heading text is not a status field.** `SCENARIOS_KR.md` contains **38 headings carrying the token
`ARMED`**, while the true unsettled KR set is **14**. Rows scored in earlier runs (`S10`, `S17`, `S38`,
`S50-KR` …) keep `ARMED` in their headings; only some were rewritten to `SCORED FIRED-x`
(`S27`, `S51-KR`). ⇒ **Authority for "is it due" is THIS master log, never a heading grep** — a heading
grep double-counts by **24 rows**. Registered so the next run does not re-derive the due list from titles.

## Scoring log — entry added by the `industry_kr` run of 2026-08-29 (Sat, KRX closed)

**KR-owned rows settling on or before 2026-08-29: 0.** Nothing due, nothing skipped.

**`S103` (US-owned, registered 08-19, settle date written as 2026-08-29) — NOT SCORED, and NOT `EXPIRED`.**
- **2026-08-29 is a Saturday.** The row observes `NVDA` 5-session excess vs `SPY` on **settled closes**,
  window 2026-08-25 close → 2026-08-29 close. **That terminal close does not exist.**
- The row itself carries the clause *"first settled close on/after 08-29"* ⇒ it settles **2026-08-31**
  and is handed back to `industry_US`.
- **Preview only, explicitly not a score** (`D242`, no improvised threshold): over the 4 sessions that
  DO exist, 08-25 → 08-28, `NVDA` **213.05 → 217.55 = +2.112%** and `SPY` **765.91 → 769.35 = +0.449%**
  ⇒ excess **+1.663pp**. The registered bands are A ≥ +5.0pp / B ≤ −5.0pp / C between.
- **Anti-signal check**: `SPY` 08-25 → 08-28 **+0.449%**, inside the ±3% VOID band ⇒ not voided on the
  4 observable sessions; the 5th session is unobserved.
- ⇒ **`D394-KR` registered**: a settle date must be a trading day, and the weekday is checked at
  registration time.

**Date-unparsed rows named explicitly** (`D347-KR` prescription): **`S3`** (~2026-09/10) ·
**`S4`** (~2026-09) · **`S8`** (`[blank]` undated).
**`S8` is unscoreable for a 30th consecutive run** — a construction failure owned by the registering
desk (US PREMORTEM), recorded here rather than passed over in silence.

**Next KR-relevant settle dates**: **08-31** (MSCI review · `316140` listing of 8.697m new shares ·
`S92`·`S94`·`S104`·`S112`) · **09-01** (`S113`) · **09-02/03** (`AVGO` print · `S109` · `S105`–`S107` ·
`S110` · `P84` · `S114`) · **09-04** (**`S67-KR` settles** · US August NFP) · **09-09** (`S58-KR`) ·
**09-11** (six rejection/miss rechecks · KOSPI200 futures final trading day) ·
**09-14/15** (`S61-KR` / `S62-KR`) · **09-18** (10th oil price-cap designation) ·
**09-19** (`S64-KR`·`S65-KR`·`S66-KR`·`S68-KR`) · **09-24** (`MU` earnings).

**No new bracket was registered this run** — the KR protocol has no PREMORTEM stage, and `M-117`'s
five anti-signals (all keyed on KIS / news / FRED, deliberately **zero** sweep-derived observables)
carry this run's pre-commitment instead. See `llm_outputs/2026-08-29/industry_KR/MACRO_REPORT.md §F`.
⚠ **That "zero sweep-derived observables" choice was made because this run measured the opposite
failing**: of `M-114`'s and `M-115`'s twelve anti-signals, **four could not be evaluated at all**
because they were keyed on sweep outputs (`eqflow`, green/red counts, Δ) and the sweep died.
**An anti-signal written on a dead instrument passes silently, which is indistinguishable from not
firing.**


---

# ═══ MASTER SCORING LOG — append by `industry_US`, 2026-08-29 (Sat 09:1x ET · US session 08-28 SETTLED) ═══

> ⚠ **Append-only** (`D165`); text staged in `llm_outputs/2026-08-29/industry_US/_scoring_block.md`
> first (`D357`), file backed up to `SCENARIOS.md.bak_0829us` before the write.
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`:
> `M1039`–`M1045` · `D400`–`D402` → **0 hits**. IDs issued by
> `module_evidence next-id` (D highest before: `D399`; M highest before: `M1038`), **not hand-grepped**.
> ⚠ **Language: English** — the US desk's documented practice.
> ⚠ **This block is written at HANDOVER time, not at run end.** Deviation from the usual writeback
> point, taken deliberately: **§A below exists because the 2026-08-28 run deferred exactly this write
> and then terminated before reaching it.** Logged as a resolved decision, not a silent change.

## §A · 🚨 RECOVERY — five verdicts the 2026-08-28 `industry_US` run produced and **never landed**

`llm_outputs/2026-08-28/industry_US/HANDOVER.md §2a–§2e` carries full, sourced verdicts for `S79`,
`S81`, `P83`, `P96` and `S119`. **None of them reached this log.** The 08-28 run wrote
`HANDOVER.md`, `MACRO_REPORT.md`, `SECTOR_FLOW_US.json`, `SECTOR_ROTATION.md`, `SWEEP_READ.md` and
`EVENT_ALPHA.md`, then produced **no `BLINDSPOT_PREMORTEM.md`, no `SECTOR_DEEP_*`, no `BET_SHEET.md`**
⇒ it terminated between ROTATION and PREMORTEM and its writeback pass never executed.

**These are NOT re-scored here.** Re-scoring a frozen observable risks writing the same fact with a
different value. Instead the 08-29 run **re-derived each leg's arithmetic independently and checked
it against the 08-28 run's printed figures**; all six legs matched to four decimals (receipts in
`llm_outputs/2026-08-29/industry_US/HANDOVER.md §2a`). The verdicts below are **attributed to the
2026-08-28 run**, which measured them.

| id | owner | verdict | measurement that settled it · (08-29 reproduction) |
|---|---|---|---|
| **`S79` Leg 1** | `industry_US` | **`FIRED-A`** | `NVDA` 1-session excess vs `SPY` on the first settled session after the 08-26 AMC print (**08-27**): `NVDA` 209.66 → 227.98 = **+8.738%**, `SPY` 766.08 → 771.10 = **+0.655%** ⇒ **excess +8.083pp** vs branch A **≥ +5.0pp** ⇒ **A clears by 3.08pp**, outside the ±6.11% implied move recorded at registration. ⚠ **`S115` fired A on the same session against a ≥ +7.0% line — `S79` L1 and `S115` are ONE event read twice** (`D343`), stated so no stage double-counts. *(08-29 reproduction: +8.0828pp ✅)* |
| **`S79` Leg 2** | `industry_US` | ★★★ **`U-MIXED`** | Same session, `AVGO` and `TSM` 1-session excess vs `SPY`: `NVDA` **+8.083pp** (\|·\|≥5.0 ✅) · `AVGO` **+3.830pp** (same sign ✅, \|·\|≥2.0 ✅) · `TSM` **+1.645pp** (same sign ✅, \|·\|≥2.0 **❌ by 0.355pp**). ⇒ neither `U-ONE` nor `U-SPLIT`. ★ The registration called `U-MIXED` *"the most informative outcome, because it retires a framing the desk uses for its concentration guard."* **On the one day the answer was observable, neither the 250d split (ANET/ETN/AVGO/NVDA standalone) nor the 500/750d merge described the tape** ⇒ **PREFLIGHT `G4`'s cross-window disagreement is not resolved by observation either; the desk has no validated grouping for event risk.** ⚠ **Margin disclosed: TSM missed by 0.355pp on a 2.0pp line.** *(08-29 reproduction: AVGO +3.8301pp, TSM +1.6454pp ✅)* |
| **`S81`** | `industry_US` | **`C`, recorded as AMBIGUOUS by its own anti-signal** | `EW{AVGO,ANET,HPE}` 2-session cumulative excess vs `SPY`, 08-25 → 08-27: `AVGO` +4.149 · `ANET` +5.316 · `HPE` +1.815 ⇒ **EW +3.760%**, `SPY` +0.678% ⇒ **excess +3.082pp**. A ≥ +3.66 (**short by 0.578pp**) · B ≤ −2.86 ⇒ inside C. 🚨 **The registered anti-signal fired and is honoured**: *"a separate ≤48h macro binary on 08-26/27 ⇒ AMBIGUOUS."* **July PCE printed 08-26, in-window and hot** (`yahoo_finance` ×2, 08-26). The C-side number is disclosed because suppressing it would hide how near A it came; **the verdict is not upgraded**. *(08-29 reproduction: +3.0822pp ✅)* |
| **`P83`** | `industry_US` (MACRO) | ★★ **`FIRED-B`** | (`HO=F` − `RB=F`) × 42, change from the 08-20 settle of **51.131**, at the 08-27 close. Settled series **51.131 → 48.170 → 41.870 → 41.618 → 39.476 → 37.569** ⇒ **change −13.562**, branch B **≤ −4.0** ⇒ **B by 9.56 points.** ★★ **`P83` was registered 2026-08-21 as the replacement INSTRUMENT after `R89` retracted the refining-separation claim**, chosen because *"a pure crude move cannot widen it."* It did not widen; it collapsed. ⇒ **the successor separator has failed too, and the desk has no surviving instrument that separates the refining excess from the barrel.** The refining *thesis* is not retracted by this row — crack levels and capacity mechanisms are separate evidence — but **separation may not be re-asserted on any instrument.** ⚠ Composition disclosed: two-sided, `HO=F` 4.480 → 4.279 (−4.5%) and `RB=F` 3.263 → 3.384 (+3.7%). *(08-29 reproduction: 51.1308 → 37.5690, −13.5618 ✅)* |
| **`P96`** | `industry_US` (MACRO) | **`FIRED-B`** ★ and the live read had the sign backwards | Settled 3-2-1 crack **5-session change** at the 08-27 close. A ≤ −2.887 · B ≥ +0.468. Reconstruction validated against the registration's own printed values before use (**−2.862 @ 08-24**, **−1.675 @ 08-25** — byte-matching `M936`). Measured at the settled 08-27 close: **+4.874** ⇒ **B, clearing by 4.41.** 🚨 **The 08-27 run's `SECTOR_DEEP_ENRG` wrote *"as printed −8.584 = deep inside A"* off a LIVE INTRADAY 08-27 bar — the settled bar is the opposite branch, 13.5 points away.** `D355` landing on a **registered row**. ✅ `M958`'s withdrawal of the 08-26 live crack figure is vindicated by the settled tape (`RB=F` 3.320 → 3.384, i.e. it **rose**). *(08-29 reproduction: 66.2554 → 71.1294 = +4.8740 ✅)* |
| **`S119`** | `industry_US` | **`FIRED-C`** — ★ and the reason it is scoreable is measured, not asserted | Handed to this desk by name by the KR run of 08-28, which declined it under `C5` (*"the row never enumerates the basket's membership"*, ⇒ `D388-KR`). **The refusal was right; reconstructing one basket would make this desk choose the observable.** What the 08-28 US run did instead: scored it under **every plausible enumeration** and tested whether the branch depends on the choice. Window 08-24 → 08-27, bands **±2.60pp**, untouched (`D242`), `SPY` +0.999%: **(a)** EW of the sweep's own 16 GICS-Energy names (identical membership in the 08-24 and 08-27 snapshots) −0.710% ⇒ **−1.709pp**; **(b)** `RSPG` (S&P 500 equal-weight energy) −0.363% ⇒ **−1.363pp**; **(c)** `XLE` (cap-weighted, robustness read) −1.299% ⇒ **−2.299pp**. ⇒ **C fires on all three. The verdict is invariant to which basket the row meant.** `D388-KR` stands as a rule; what is **not** true is that the row was unscoreable — it was unscoreable by a single arbitrary pick and scoreable by showing the pick does not matter. ⚠ Nearest branch is B at −2.299pp vs −2.60pp (**0.30pp**), disclosed. **Anti-signals probed, neither fired**: the presser held (`fxstreet` 08-24); **no US–Iran direct-talks announcement with a named date** — the window instead contains an **Iran–Oman temporary Strait of Hormuz transit deal (08-26**, `foreignpolicy`/`semafor`/`aljazeera`) and, on the US leg, the opposite (`aljazeera` 08-26 *"not in a hurry"*; `wsj` 08-27 *"Iran Talks Sputter"*). *(08-29 reproduction: XLE −1.299% / RSPG −0.363% / SPY +0.999% ✅)* |

⇒ **`D400` registered**: *a scoring verdict that exists only in a run directory is not scored.*
**Positive form**: the writeback pass verifies `grep "<id>" handoff/SCENARIOS.md` returns ≥1 hit
**for every id the run scored**, before the run is called complete.

## §B · Scored by the 2026-08-29 `industry_US` run

> The **2026-08-28 US session is settled** and this run fires after it — the first US run in four
> to have its own settle date behind it rather than ahead of it.
> ⚠ **Both rows were scored under TWO price surfaces and the branch reported only because it is
> invariant across them** (`C5`). See §C for why that was necessary.

| id | owner | verdict | measurement that settled it |
|---|---|---|---|
| **`S116`** | `industry_US` | **`FIRED-C`** | Frozen observable = `MRVL` − `AVGO` **1-session excess** on the first settled close after the 08-27 print (**08-28**), each vs its own 08-27 close. A ≥ **+12.0pp** · B ≤ **−12.0pp**. Measured: `MRVL` 241.45 → **216.62** = **−10.2837%**, `AVGO` 371.54 → **368.79** = **−0.7402%** ⇒ **spread −9.5435pp** ⇒ **C**. Second surface (`repair=True`): −10.3748% / −0.6513% ⇒ **−9.7235pp** ⇒ **C**. **Invariant.** ⚠ **Margin disclosed and it is the informative part**: the spread is **79% of the way to B** (2.46pp short) on a **beat-and-raise** print — *"Marvell Leads AI Stocks Lower After Earnings That Narrowly Topped Estimates"*, *"Marvell forecasts $18B fiscal 2028 revenue, data center growth >60%"* (`seekingalpha` 08-27). **C is the verdict and the direction is not neutral; saying so is not moving the line.** **Anti-signal** (*"an announced acquisition of, or by, either company inside 08-24→08-28"*) **probed, NOT fired** — argued from a **loud** query, not a zero-hit one (`D94`): `Marvell` returns **482** foreign hits/7d, **380**/4d, and the window's content is the print, not a corporate action. ⇒ **`M1039`** |
| **`S118`** | `industry_US` | **`FIRED-C`** | Frozen observable = `EW{MU,SNDK,WDC}` **2-session excess vs `NVDA`**, 08-26 close → 08-28 close. A ≥ **+6.50pp** (the print is about MEMORY) · B ≤ **−6.50pp** (the print is about NVDA). Measured: `MU` **−0.5904%** · `SNDK` **−0.9597%** · `WDC` **−2.0112%** ⇒ **EW −1.1871%**; `NVDA` 209.66 → **217.55** = **+3.7632%** ⇒ **spread −4.9503pp** ⇒ **C**. Second surface (`repair=True`): EW −1.2267% vs `NVDA` +3.9254% ⇒ **−5.1521pp** ⇒ **C**. **Invariant.** ⚠ Spread is **76% of the way to B** (1.55pp short). **Anti-signal** (*"a memory-maker pre-announcement **or guidance revision** with a named date inside 08-24→08-28"*) **probed, near-miss disclosed, NOT fired**: the window contains ***"Micron Technology to Report Fiscal Fourth Quarter Results on September 30, 2026"*** (`yahoo_finance` 08-26) — **an announcement with a named date**, but an earnings-*calendar* notice, **neither a pre-announcement nor a guidance revision**; also *"Micron Announces Leadership Appointments"* (08-26), likewise non-qualifying. ⇒ **NOT fired on the row's own words**, recorded with sources so a later run can overturn it on evidence. ★ **The same item corrects a carried fact the row's base-rate argument rested on**: registration read *"`MU` does not print until **09-24**"*; it prints **09-30**. The base rate was argued from a wrong date and is **safer** than claimed, not less safe ⇒ **`M1044`**. ⚠ **`S116` and `S118` are NOT independent** — `NVDA`'s +3.76% two-session move is inside both, and `S79` L1 measured the 08-27 leg of that same path (`D343`) |

### Not scored by this run, and why — named rather than dropped

| id | why not scored |
|---|---|
| **`S120`** | Needs *"the first observation where **BOTH** `DGS30` and `T10YIE` carry 2026-08-28."* `T10YIE` **has 08-28 (2.31)**; `DGS30` ends **08-27 (5.19)**. **Not readable ⇒ stays ARMED, NOT `EXPIRED`.** ✅ **The row's own observation-lag clause working as designed** — it was written in at registration so this would be a deferral, not a discovery. That is exactly what `S102` lacked for five runs |
| **`S111`** | `BAMLC0A0CM` (`ig_oas`) ends **08-27 = 0.79**; needs the first close covering 08-28. **Stays ARMED.** ⚠ Pre-settle read disclosed: 0.79 is inside **C** (A ≥ 0.85 / B ≤ 0.77), **2bp above B** — 🚫 not to be inherited as "C fired" |
| **`P67`** | `hy_oas` ends **08-27 = 2.63** vs a **≥ 2.85%** line ⇒ **22bp below**. **Stays ARMED**; disclosed, not scored |
| **`S103`** | Handed here by the KR run of 08-29. Registered to settle **2026-08-29, a Saturday**; its `"first settled close on/after"` clause moves it to **08-31**. **NOT due.** ⚠ The KR run's 4-session preview (**+1.663pp**) was **independently reproduced by this run at +1.6630pp** — used as instrument corroboration (§C), **explicitly not as a score** |
| **`S124`** | 🚨 **Correction to the 08-28 HANDOVER, which listed this as settling 08-28.** It settles **2026-08-31** (cross-sectional count of `us_top300` IT names with positive `exc5` vs `SPY`). **Not due.** ⚠ It is the **only cross-sectional row on 08-31** and it tests this desk's own `IT` underweight — **branch B is the one that vindicates the desk**, stated so C is not read as a win |
| `S92` `S94` `S104` `S112` | settle **08-31**. ⚠ `S104`'s title still carries the `R106` date defect (*"July PCE 2026-08-28"* when PCE printed **08-26**); **its settle is later and no threshold is touched** |
| `P86` | PCE conjunct **met**; rate conjunct unreadable (`DGS2` **4.20** @08-27 vs A ≤ 4.10 / B ≥ 4.32). **Stays ARMED** |
| `P97` | unreadable — `DTWEXBGS` ends **08-21**, eight days behind the joint date the row requires. **`D333`'s 11th reproduction** |
| `S109`(`FRO`) `P81` `P85` `P87`–`P89` `S127` `S128` `S129` `S130` | not yet due (09-02 and later) |
| **`S8`** | ⛔ **unscoreable for a 31st consecutive run** — date field still `[blank]`. **Named again rather than dropped.** A human must `VOID` it or re-register it with a date (P5) |
| KR-owned rows | **zero due**; earliest `S67-KR` **09-04** |

## §C · 🚨 The instrument finding that forced §B's two-surface method — `M1040`–`M1043`

Scoring `S116` required the **2026-08-28 settled close**, and the provider returned **three different
values for it**. Measured 2026-08-29 ~22:2x KST, one provider (`yfinance`), three surfaces:

| surface | NVDA 08-28 | SPY 08-28 | MRVL 08-28 |
|---|---|---|---|
| `yf.download(...)` daily bar | **NaN** | **NaN** | **NaN** |
| `yf.download(..., repair=True)` | 217.89 (`Repaired? True`) | 769.35 | 216.40 |
| `Ticker.fast_info['last_price']` | **217.55** | **769.35** | **216.62** |

- **`M1040`** — the 08-28 row is **present with Volume and with Open/High/Low; only `Close` is NaN.**
  NVDA 08-28: O **227.33** / H **229.26** / L **216.81** / C **NaN** / V **194,036,188**. The session
  happened. Reproduced on all nine tickers probed (`NVDA SPY MRVL AVGO MU SNDK WDC XLE RSPG`) and on
  the three energy futures (`CL=F HO=F RB=F`).
- **`M1041`** — this is the **same defect class the KR desk measured this morning** (`M1026`: a phantom
  08-28 bar for **831 of 833** KR names), **independently re-measured here on US names** — not a
  cross-market transfer — and **the signature differs**: KR lost all of OHLC, **US lost `Close` only**.
- **`M1042`** — ★ **the tie was broken by measurement, not by preference.** The KR run, eleven hours
  earlier and through a different path, quoted `NVDA` 08-28 = **217.55** / `SPY` = **769.35** and
  published a four-session `S103` preview of **+1.663pp**. Recomputing that preview from **this run's**
  `fast_info` values returns **+1.6630pp** — byte-identical. ⇒ **`fast_info.last_price` is the settled
  close; `repair=True`'s 217.89 is a synthetic outlier, flagged as such by its own `Repaired?` column.**
- **`M1043`** — a **fourth** disagreement inside the same instrument: `fast_info['previous_close']`
  returns **226.149** where the daily bar's 08-27 close is **227.98**. Not used; recorded, not diagnosed.
- ⚠ **`D5` (cross-provider) is UNMET.** A second provider was attempted and **failed**: Stooq returned
  **HTTP 404** for every US symbol (`nvda.us` `spy.us` `mrvl.us` `avgo.us` `mu.us` `sndk.us` `wdc.us`),
  retried once with a raw-response diagnostic, same result. The corroboration above is
  **temporal + cross-path within one provider**, which is weaker. **Stated, not glossed.**
- 🚫 **Right removed for the rest of this run**: `repair=True` output may not be used as a settled
  price. Where an 08-28 close is needed it comes from `fast_info.last_price`, and both readings are
  shown wherever a threshold sits within one reading's width of the other.
- ⇒ **`D402` registered**: *`repair=True` fabricates a settled price and flags it only in a column
  nobody reads.* **Positive form**: any settled-price read asserts `Repaired? == False`, or falls back
  to `fast_info.last_price` **and says which it used**.
- ⚠ **Contaminated stretch registered, not cleaned**: the **2026-08-28 daily-close bar** is unreadable
  via `yf.download` for US names. Prior runs' figures are **not** retro-corrected; they carry this note.

## §D · 🚨 A finding about the snapshot files this log's rows are read beside — `M1045` / `D401`

Found while checking PREFLIGHT `G2`, and it **refutes that gate's own summary sentence**, which is
left standing in `PREFLIGHT.md` per `D48` rather than edited.

`SECTOR_FLOW_US.json`'s `asof` is set from **the bench frame's last index date**
(`scripts/sector_flow.py:507-509`) — which a **live intraday** row satisfies. Measured:

| snapshot | its `asof` | its `last` for `NVDA` | that date's **settled** close | gap |
|---|---|---|---|---|
| 08-27 file | 2026-08-27 | **224.17** | **227.98** | **−1.67%** |
| 08-28 file | 2026-08-28 | **227.46** | **217.55** | **+4.56%** |

Both `last` values sit **inside their own date's intraday range** (08-27 H/L 230.47 / 220.90;
08-28 H/L 229.26 / 216.81), which excludes *"it is the prior close"* and *"it is an adjusted value"*.
⇒ **the snapshots' terminal bars are live intraday prints taken minutes after the 09:1x ET open**, and
**a `Δflow` between two snapshots differences two intraday photographs, each labelled with a settled
date.** `G2`'s PASS stands (it measures axis-count continuity, which is continuous); the constraint is
**appended, not substituted**. 🚫 **No stage may describe a `SECTOR_FLOW_US.json` figure as a settled
reading this run.**
⇒ **`D401` registered**: *PREFLIGHT's `asof` gate reads a field, not a bar.* **Positive form**: `G2`
compares the snapshot's `last` for one liquid name against that date's **settled** close and reports
the gap in %.

★ This row belongs in the scoring log rather than only in a run directory for the same reason §A
exists: **`P96` was put on the wrong branch by exactly this defect** — the 08-27 `SECTOR_DEEP_ENRG`
read a live intraday crack of **−8.584** where the settled value was **+4.874**, the opposite branch,
13.5 points away. `D355` and `D401` are the same mechanism at two altitudes.

## §E · Two observations this log leaves

1. **The desk's scoring is now three-for-three on "the pre-settle read pointed the wrong way."**
   `S101` registered −0.677, pre-settle +1.616, final −0.744. `P78` pre-settle **above branch A**,
   final **branch B**. `P96` live **−8.584 (deep in A)**, settled **+4.874 (B)**. ⇒ **a pre-settle
   read is not a weak version of a verdict; on this desk's record it has been an inverted one.**
   Rows `S111`/`P67`/`P86`/`P97` are deferred **with their pre-settle numbers disclosed** precisely so
   the next run inherits the number *and* this warning together.
2. **Nothing was registered by this stage.** New brackets are PREMORTEM's to write (Stage 7); the
   ≤48h obligation handed forward is **MSCI 08-31 (inside 48h, six rows already on that date)** plus
   two **uncovered** dated binaries — **Aug PPI 09-10** and **Aug CPI 09-11, zero rows on either** —
   and the **Hormuz state change**, which `catalyst_calendar` still carries as *undated* although a
   temporary Iran–Oman transit deal was struck **2026-08-26**.


---

## MASTER INDEX — appended 2026-08-29 by the `industry_US` run (PREMORTEM registrations)

> ⚠ Append-only (`D165`). ID 3-grep at WRITE time across `handoff/*.md` · `llm_outputs/**` ·
> `REPORT/**` (excluding this run's own files): `S131` `S132` `S134` → **0 hits**; `S133` → 1 hit
> **inspected and rejected as a false positive** (substring of the FRED series id `MTSDS133FMS`).
> Highest existing **`S130`** (2026-08-27 US). IDs issued by `module_evidence next-id`, not hand-grepped.

| id | owner desk | file | object | settles | status |
|---|---|---|---|---|---|
| **`S131`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **MSCI 08-31 rebalance — `RSP` − `SPY` 1-session excess**, ±1.30pp. ★ **The mandatory ≤48h bracket**: six rows already settle 08-31 and none observes the rebalance itself | **2026-08-31** | ARMED |
| **`S132`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **`AVGO` 09-02 print — 1-session excess vs `SPY`**, ±9.00pp, set **outside** the ±8.11% chain-derived implied move. `D295`'s prescription executed 4 runs late; `S127` stays armed and is pre-declared NO-INFORMATION | **2026-09-03** | ARMED |
| **`S133`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **`EW{REGN,AMGN,TMO,BDX,MRK,VRTX}` 10-session excess vs `XLV`**, ±3.00pp — brackets the `HLTH` `N`→`OW` promotion this run made on `eqflow` against the board's worst `exc5` | **2026-09-14** | ARMED |
| **`S134`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **`XLF` 5-session excess vs `SPY`**, ±2.00pp — the board's only contradiction with no instrument defect available (both flow reads negative, no flipper, tape positive) | **2026-09-04** | ARMED |

### Rows this run examined and DECLINED to register, with the reason (so an absence stays legible)

| candidate | why declined |
|---|---|
| **Aug PPI (09-10) · Aug CPI (09-11)** | 🚫 **Dropped on information grade (`B4`), not overlooked** — MACRO §10 named the zero-row gap and this stage checked it: **no verdict this run reached is conditioned on an inflation print.** Every delta rests on `eqflow`, settled excess returns, or an options-implied move, and **`P108` already owns the credit consequence at 09-11**. Neither branch would change a conclusion ⇒ the bracket was spent on `S131` instead |
| **Aug NFP (09-04)** | Already spanned **twice** — `S126` (five sessions **into** it) and `P114` (five sessions **out of** it). A third row on one event is `D343` |
| **Hormuz "strait open" (undated)** | Already spanned by `P107` (through 09-08) and `P112` (through 09-11). ⚠ Recorded again: the calendar still carries it as **undated** although a temporary **Iran–Oman transit deal was struck 2026-08-26** — an instrument fact, not a bracket gap |
| **`HPE` 09-03 print** | Held, prints inside the window, implied move **±11.39%** (09-04 expiry, K=52.00, straddle 5.96) — **but it is inside the `IT` DEEP mandate this stage just created**, and bracketing a name the same run is about to deep-dive pre-commits the DEEP's conclusion. **Deferred to the DEEP stage by design**, not missed |


## MASTER INDEX — appended 2026-08-30 by the `industry_US` run (PREMORTEM registrations)

> ⚠ Append-only (`D165`). ID 3-grep at WRITE time across `handoff/*.md` · `llm_outputs/**` ·
> `REPORT/**` (excluding this run's own files): `S135` → **0 hits**. Highest existing **`S134`**
> (2026-08-29 US). IDs issued by `module_evidence next-id`, not hand-grepped.

| id | owner desk | file | object | settles | status |
|---|---|---|---|---|---|
| **`S135`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **max pairwise spread among `XLU`·`XLRE`·`XLP` 5-session excess vs `SPY`**, A ≤ 1.50pp / B ≥ 4.00pp — tests whether the desk's three UW verdicts are ONE bet booked as three. Bands = 1σ/2σ of the legs' own 5-session realised sigma | **2026-09-11** | ARMED |

### Rows this run drafted and DECLINED to register, with the reason (so an absence stays legible)

| candidate | why declined |
|---|---|
| **MSCI quarterly review, 2026-08-31 (the ≤48h binary)** | ✅ **Already owned by `S131`** (registered 08-29, ARMED: `RSP` − `SPY` 1-session excess, A ≥ +1.30pp / B ≤ −1.30pp, both outside `RSP`'s ±1.06% implied). **The ≤48h obligation is satisfied by an armed row; issuing a second would re-freeze a live threshold (`D242`).** ⚠ My independent band derivation (±0.41σ of `SPY`'s 20-day daily sigma) lands **tighter** than the armed row's — recorded so the comparison survives |
| **`AVGO` earnings, 2026-09-02** | ✅ **Already owned twice** — `S132` (±9.00pp 1-session excess vs `SPY`, settles 09-03) and `S127` (settles 09-08). A third row on one print is `D343`. ★ **Independent corroboration recorded**: today's chain gives implied **±8.09%** (09-04 expiry, K=367.5, straddle 29.83, OI 645c/354p) against the 08-29 run's **±8.11%** — **2 bp apart on a different day's chain**, which is why `S132`'s threshold is left untouched |
| **`HPE` earnings, 2026-09-03** | 🔁 **Deferral RENEWED, not re-decided.** The 08-29 run declined it in writing because *"it is inside the `IT` DEEP mandate and bracketing a name the same run is about to deep-dive pre-commits the DEEP's conclusion."* **`IT` is a DEEP again this run (PREMORTEM-promoted), so the identical reasoning holds.** ⚠ Today's numbers recorded for the DEEP to inherit: implied **±11.23%** (09-04 expiry, K=52.00, straddle 5.87, **P/C OI 2.19×**) against a **7.21%** 5-session realised sigma; `HPE` reads OBV **+0.096 매집** and `rs20` **+6.2** against `rs60` **−7.2** vs `SPY` |
| **Aug PPI, 2026-09-10** | 🚫 **Dropped on information grade (`B4`), 3rd consecutive run — now BY DECISION, not by omission.** PPI is a **nowcast update to the CPI print one day later**, not an independent binary; neither branch would change a verdict that **`P116`** (HY OAS at the first `[FRED]` close covering 09-18) does not already carry. **The bracket was spent on `S135` instead** |
| **Aug CPI, 2026-09-11** | ✅ **Closed this run by `P116`** (registered in `MACRO_REPORT §C`): HY OAS ≤ 2.62 / ≥ 3.00. **The two-run "zero rows on CPI" gap is closed** — and it is closed on the **credit** leg rather than the equity leg, because `§A-2` measured HY OAS at the **0.0th percentile** of its year while real yields sit at the **89th**, which is where the fault line is |
| **Aug NFP, 2026-09-04** | ✅ Already spanned twice — `S126` (five sessions **into** it) and `P114` (five sessions **out of** it). A third is `D343`. ⚠ `S135`'s window **starts** on 09-04 rather than observing it |
| **Hormuz "strait open" (undated)** | ✅ Spanned **three** ways — `P107` (through 09-08), `P112` (through 09-11), **`P117`** (registered this run, through 09-18, with an explicit cross-provider leg after `BZ=F` and FRED's `DCOILBRENTEU` were measured **2.53 apart on 2026-08-21**, straddling `P107`'s branch-B line of 96.00). A fourth is `D343` |
| **`XLU` 09-11 standalone** | 🚫 Considered and declined: `XLU`'s 09-11 implied is **±2.88%** vs a **1.89%** 5-session realised sigma, so a threshold outside implied would be reachable — **but `S135` already tests `XLU` on the same window through a spread that carries more information** (it tests whether `XLU` is a separate bet at all). One observable, one row |

---

# ═══ MASTER 채점 로그 — appended 2026-08-31 by the `industry_kr` run (분할하지 않는 스파인) ═══

> ⚠ **Append-only** (`D165`). 백업 `SCENARIOS.md.bak_0831kr` 선행.
> ⚠ **ID 3-grep at WRITE time**: `S69-KR` → `handoff/*.md` · `llm_outputs/2026-08-2*` · `REPORT/` **0 hits**.
> 직전 최고 **`S68-KR`**. 발급은 `module_evidence`/전수 grep, 손으로 세지 않았다.

## A · 이번 런이 채점한 것 — **KR 소유 0건, 그리고 그 0 은 grep 으로 증명됐다**

`SCENARIOS_KR.md` 전수 검색: 문자열 **`2026-08-31` / `08-31` 히트 0건.**
직전 런(08-29)의 채점 로그도 *"KR-owned rows settling on or before 2026-08-29: 0"* 로 닫혀 있다.
⇒ **오늘 정산 도래하는 KR 소유 행은 0건이다. 조용히 넘긴 행 0건.**
> `D389-KR` 준수: 제목의 `ARMED` 토큰을 세지 않고 **마스터 채점 로그의 날짜**로 열거했다.

## B · 🚨 US 소유 4행 — **오늘 정산인데 오늘이 안 끝났다.** `EXPIRED` 아님

| 행 | 관측면 | 왜 오늘 채점 못 하나 |
|---|---|---|
| **`S92`** | 필수 호르무즈 브래킷(3갈래) · settle **2026-08-31** | 관측면이 **08-31 정착 종가**. **이 런은 KST 08:17~09:2x 에 돌았고 US 세션은 아직 열리지도 않았다** |
| **`S94`** | 사이클 등록부가 광학/인터커넥트를 못 본다 · settle **2026-08-31** | 동일 |
| **`S103`** | `NVDA` 5세션 초과 vs `SPY`, **on/after 08-29 첫 정착종가 = 08-31** | 동일. ⚠ **`EXPIRED` 아님** — 08-29 는 토요일이었고 `on/after` 절이 오늘로 밀었다 |
| **`S112`** | 필수 잭슨홀 브래킷(창 안에 PCE 인쇄 포함) · settle **2026-08-31** | 동일 |

⇒ **넷 다 「미도래」이지 「미정산」이 아니다.** 소유 데스크(`industry_US`)로 그대로 넘기고,
**정산 가능 시점은 KST 기준 2026-09-01 새벽**이다.
⚠ **`D242` 준수**: 임계값을 즉흥으로 바꿔 미리 판정하지 않았다. 08-29 런이 남긴 `S103` 4세션 프리뷰
(**초과 +1.663pp**)는 **그 런의 프리뷰이고 오늘의 점수가 아니다.**

★ **`D402-KR` 등록 — 이 4행이 드러낸 새 갈래**: **정산일이 같아도 시장이 다르면 어느 데스크가 채점할 수
있는지가 다르다.** `D394-KR`(정산일은 거래일이어야 한다)은 이 경우를 못 덮는다 — **날짜는 거래일이 맞고,
어긋난 것은 시간대다.** ⇒ 등록 시 **정산일 옆에 「관측 가능해지는 KST 시각」**을 적는다.

## C · `D347-KR` 준수 — 날짜 미파싱 행
**`S3`**(~2026-09/10) · **`S4`**(~2026-09) · **`S8`**(undated).
⚠ **`S8` 은 이로써 KR 데스크 기준 31런 연속 정산 불가.** 중립이 아니라 **행 구성 실패**이며 관측면을
주는 것은 소유 데스크(US PREMORTEM)의 몫이다. **오늘도 명시적으로 미정산으로 남긴다.**

## D · MASTER INDEX 추가 — 이번 런이 등록한 브래킷

| id | 소유 | 파일 | 관측면 | 정산일 | 상태 |
|---|---|---|---|---|---|
| **`S69-KR`** | `industry_kr` | `SCENARIOS_KR.md` | ★★★ **보유 이름의 자본구조 이벤트를 처음으로 브래킷에 묶는다** — `316140` 우리금융지주 추가상장(08-31) 이후 **5 정착세션 기관 순매수 누적 부호** + 같은 창의 `069500.KS` 대비 초과 | **2026-09-05**(08-31 포함 5 정착세션의 마지막) | **ARMED** |

★ **이 등록은 오늘 이 런이 스스로 낸 dig `D401-KR` 을 즉시 이행한 것이다** —
*"보유 종목의 날짜 박힌 자본구조 이벤트에는 브래킷을 붙여라. 안 붙이면 어떤 정산 표에도 안 잡힌다."*
**`SCENARIOS_KR.md` 의 08-31 grep 이 0 이었다는 사실 자체가 그 dig 의 실측 근거였고, 여기서 닫는다.**

## E · 이 로그가 남기는 관측 두 줄
1. **KR 데스크는 오늘 정산 도래가 0 인데도 US 소유 4행을 열어 「왜 못 하는지」를 적었다** — `D393-KR` 이행.
   **「없어서 안 했다」와 「확인 안 했다」를 가르는 유일한 장치는 이 표다.**
2. **`M-117` 은 등록 2세션 만에 폐기됐고**(회수 원장 `R113`), **그 사인은 예측 실패가 아니라 관측면 설계 실패였다** —
   **두 관측면(건수 임계값, 「미거래」 절)이 둘 다 자기 창의 성질을 안 셌다.**
   후속 `M-118` 의 안티시그널 5개는 **전부 KIS·FRED·환율 위에 걸었고 건수 임계값을 0개 썼다.**

---

## MASTER INDEX — appended 2026-08-31 by the `industry_US` run (PREMORTEM registrations)

> ⚠ Append-only (`D165`). ID 3-grep at WRITE time across `handoff/*.md` · `REPORT/` ·
> `llm_outputs/2026-08-2*/` (excluding this run's own files): `S136` · `S137` → **0 hits**.
> Highest existing **`S135`** (2026-08-30 US). IDs issued by `module_evidence next-id`, not hand-grepped.

| id | owner desk | file | object | settles | status |
|---|---|---|---|---|---|
| **`S136`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **`EW{SLB,MPC,PSX,VLO,COP}` − `EW{XOM,EOG,FANG}`, 5-session sum**, A ≥ +3.90pp / B ≤ −3.90pp (±1.50σ of the measured 2.598pp 5-session sigma). Tests this run's own headline flow claim — that the money left E&P for services/refining **before** the strikes. **B kills that claim** | **2026-09-09** | ARMED |
| **`S137`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **`EW{LITE,COHR}` − `SMH`, 5-session sum**, A ≥ +9.00pp / B ≤ −9.00pp (±1.04σ of the measured 8.639pp sigma). **`D250`'s 16-run question, bracketed instead of deferred a 17th time**; **B closes the dig as not-a-gap** | **2026-09-09** | ARMED |

### Rows this stage drafted and DECLINED to register, with the reason (so an absence stays legible)

| candidate | why declined |
|---|---|
| **MSCI quarterly review, 2026-08-31 (the mandatory ≤48h binary)** | ✅ **Already owned by `S131`** (ARMED, `RSP` − `SPY` 1-session excess, ±1.30pp, outside `RSP`'s ±1.06% implied at registration). A second row would re-freeze a live threshold (`D242`). ★ **New context recorded instead of a new row (`M1141`)**: the dominant MSCI story today is **India** — *"India's Closing Auction Faces $5 Billion MSCI Reshuffle Test"*, *"Adani Shares Lose $15 Billion"* — so `S131`'s **observable is unaffected but its narrative premise may be an offshore echo**. **Threshold NOT moved** |
| **`AVGO` earnings, 2026-09-02/03** | ✅ **Already owned twice** — `S132` (±9.00pp vs `SPY`, settles 09-03) and `S127` (09-08). A third is `D343`. ★ **Independent corroboration recorded**: today's chain gives implied **±8.08%** (09-04 expiry, K=370.0, straddle 29.82, spot 368.91) against **±8.09%** on 08-30 and **±8.11%** on 08-29 — **three chains, three days, 3 bp apart**, so `S132`'s ±9.00pp remains **outside** implied. ★ **`M1142`: the option book FLIPPED side** — call OI **645 → 5,105** and put OI **354 → 1,892** (2.70× call-heavy) in one day, **while the underlying reads flow −0.717 🔴분산 · OBV −0.147 · `rs60` −25.1 vs `SPY`.** 🚨 **`D420` still unresolved**: the issuer's calendar says 09-03, `catalyst_calendar` says 09-02, and `S132` settles 09-03 on that basis |
| **Aug NFP, 2026-09-04** | ✅ Spanned three ways — `S126` (`XLI` exc5 **into**), `P114` (**out of**), `S134` (Financials, same date) — and `P115` carries it as an **AMBIGUOUS clause** (a ≥100k miss voids rather than scores). A fourth is `D343` |
| **Aug PPI, 2026-09-10** | 🚫 **Dropped on information grade (`B4`), 4th consecutive run — BY DECISION, restated so it does not decay into an omission.** PPI is a nowcast update to the CPI print one day later, not an independent binary; **neither branch would change a verdict `P116` (09-18) and `P120` (09-25) do not already carry** |
| **Aug CPI, 2026-09-11** | ✅ Owned by `P108` (09-11), `P116` (09-18) and `P120` (IG OAS, 09-25, registered today). ⚠ Recorded rather than re-bracketed: the **09-11 option book is one-sided on the branch the desk is already on** — `XLU` put OI **3,594 vs call 22 (163×)**, `NVDA` put **4,602 vs call 379 (12.1×)** |
| **Hormuz "strait open" (undated)** | ✅ Spanned four ways — `P107` (→09-08), `P112` (→09-11), `P117` (→09-18), **`P118`** (`DCOILWTICO` **spot**, →09-11, registered today **because it is roll-immune**, `M1136`). A fifth is `D343`. ⚠ **`S8` remains dateless for a 33rd run — a human must `VOID` it or give it a date (P5)** |
| **A yen/`JPY=X` bracket** | ✅ **Registered by MACRO this run as `P119`** (settled close, any bar 09-01→09-18, A ≥164.00 / B ≤156.00 against 159.32). PREMORTEM declines to duplicate its own run's MACRO stage |
| **A `UTIL`-only row** | 🚫 Declined — **`S135` already tests `XLU` through a spread** (max pairwise among `XLU`/`XLRE`/`XLP`, 5-session excess, settles 09-11) that **carries more information than a level**, because it asks whether the three UW verdicts are one bet. One observable, one row |

---

# ═══ MASTER SCORING LOG — appended 2026-08-31 by the `industry_US` run ═══

> ⚠ **Append-only** (`D165`). Backups `SCENARIOS.md.bak_0831us` · `SCENARIOS_US.md.bak_0831us` taken first.
> ⚠ ID 3-grep at WRITE time: `S136` · `S137` → **0 hits**; highest existing `S135`.

## A · Scored by this run — **ZERO, and the composition is the point**

**0 scored · 7 not-due-by-clock · 5 `[FRED]`-blocked · 1 unscoreable · 0 silent skips.**
`D430` (registered this run) asks exactly for that breakdown, because **a bare zero cannot be told
apart from a skip**.

### A-1 · 🚨 The structural cause, discovered this run — `M1127` ⇒ `D426`

**This desk fires PRE-OPEN.** The scheduled run starts at **KST 22:09 = ET 09:09**, twenty-one
minutes before the NYSE opens. ⇒ **a row whose observable is "date D's settled US close" can NEVER be
scored by the run dated D.** Confirmed against the desk's own record: the 08-29 run described itself
as *"the first US run in four to have its own settle date behind it rather than ahead of it"* and
scored `S116`/`S118` off the **08-28** session, not its own date.
⇒ **`D426`**: *a scenario observing date D's US close is registered to settle **D+1**, with the KST
hour at which it becomes observable written beside it.* This is the **US-side twin of `D402-KR`**,
which the KR desk reached from the other side of the same clock **eight hours earlier the same day**.

### A-2 · The seven rows that settle 2026-08-31 — NOT DUE, not `EXPIRED`

| row | observable | why not scored |
|---|---|---|
| **`S92`** | mandatory Hormuz bracket (3 branches) | needs the **08-31 settled close**; the session had not opened when this stage ran |
| **`S94`** | the cycle registry cannot see the cycles this desk finds | same |
| **`S103`** | `NVDA` 5-session excess vs `SPY`, first settled close on/after 08-29 ⇒ 08-31 | same. ⚠ **Not `EXPIRED`** — 08-29 was a Saturday and the `on/after` clause moved it. Pre-settle read carried and **explicitly not a score**: the 08-29 run reproduced the KR preview at **+1.6630pp** |
| **`S104`** | (title still carries the `R106` date defect) | settle is later; no threshold touched |
| **`S112`** | mandatory Jackson Hole bracket, owns the PCE print in its window | same |
| **`S124`** | cross-sectional count of `us_top300` IT names with positive `exc5` vs `SPY` | same. ⚠ **the only cross-sectional row on this date**, and **branch B is the one that vindicates the desk's own `IT` underweight** — stated so a `C` is not later read as a win |
| **`S131`** | ★ the mandatory 48h bracket — MSCI 08-31, `RSP` − `SPY` 1-session excess, ±1.30pp | the rebalance prints into today's close. **The row is armed and correctly placed; the desk simply cannot observe it yet.** ★ **`M1141` recorded beside it**: the dominant MSCI story today is **India** ($5bn reshuffle, Adani −$15bn), so the observable is unaffected but the **narrative premise may be an offshore echo**. 🚫 Threshold NOT moved |

### A-3 · The five rows blocked on `[FRED]` — re-measured, still unreadable

| row | requirement | today's read | status |
|---|---|---|---|
| **`S120`** | first observation where **both** `DGS30` and `T10YIE` carry 08-28 | `T10YIE` ✅ **08-28** · `DGS30` ❌ **08-27** | **ARMED**, 2nd consecutive run. ✅ its own observation-lag clause working as designed. ★ **`M1128`/`D431`: `T10YIE` = `DGS10` − `DFII10` and is published for a date neither constituent carries** — a derived series outran its inputs, which is what blocks this row |
| **`S111`** | `ig_oas` close covering 08-28 | ends 08-27 = **0.79** | **ARMED**. ⚠ pre-settle disclosed: 0.79 sits in **C**, **2 bp above B** — 🚫 not to be inherited as "C fired" |
| **`P67`** | `hy_oas` ≥ 2.85% | ends 08-27 = **2.63** ⇒ 22 bp below | **ARMED**, disclosed not scored |
| **`P86`** | PCE conjunct met; rate conjunct on `DGS2` | **4.20** @08-27 vs A ≤4.10 / B ≥4.32 | **ARMED** |
| **`P97`** | joint date on `DTWEXBGS` | ends **08-21** = **10 days behind**, widened from 9 | **ARMED**. ★ **`D333`'s 13th reproduction, and the lag is still growing run over run** |

### A-4 · Named again rather than dropped

- **`S8`** — ⛔ **unscoreable for a 33rd consecutive run**; date field still `[blank]`. **A human must
  `VOID` it or re-register it with a date (P5).**
- **`S3`** (~2026-09/10) · **`S4`** (~2026-09 late) — dates unparsed by design; not due.
- **KR-owned rows: zero due** (the KR run proved its own zero by grep this morning; earliest
  `S67-KR` is 09-04).
- **`S130`** — ARMED (09-10) but ⚠ **staleness flag raised**: its attention thread
  (*"Nvidia agrees to acquire Hugging Face for $12.9B"*) is **ENDED**, peak 15 outlets, dead by 08-28.
  **A row may still score with a dead thread; its premise no longer has a live audience.**

## B · What this log leaves for the next run

1. **The next run is the first that can score seven of these rows** — and it inherits both the
   pre-settle numbers **and** the warning that this desk's pre-settle reads have been **inverted
   three-for-three** (`S101` registered −0.677 / pre-settle **+1.616** / final −0.744; `P78`
   pre-settle above A / final **B**; `P96` live **−8.584** deep in A / settled **+4.874** = **B**).
2. **Two ARMED rows are keyed to an instrument that changed underneath them.** `P107` and `P117` both
   observe **`BZ=F` settled closes**, and **the Brent front month rolled on 2026-08-31** — a **−3.30
   level shift, ~48% of `P117`'s lower band** (`M1136`). 🚫 **Neither was re-frozen** (`D242`);
   **`P118` was registered on roll-immune `DCOILWTICO` spot instead**, and if the futures rows and the
   spot row fire different branches, **that disagreement is `D432`'s evidence, not a contradiction to
   resolve.**
3. **`S136` is pointed at this run's own headline claim, and DRIFT already recorded a pre-settle read
   against it** (≈ **−0.44pp**, toward branch **B**, measured 48 minutes into the following session,
   **explicitly not a score**). **A desk that only brackets what it believes has not bracketed
   anything.**

---

## Master scoring log — appended by the 2026-09-01 `industry_kr` run (append-only)

> ★ **Five US-owned rows settled 2026-08-31 and this KR run scored all five.** They were handed
> forward by the 08-31 KR run as "not due yet — the US session had not opened" and by the 08-31 US
> run as `D426` (*"a desk that fires pre-open can never score a row observing that date's US close"*).
> **The KR desk's morning run is the natural scorer for the previous US session** — registered as
> `M1148`. Ownership confers no exclusivity (README §Split rule 3).

| row | owner | settle | verdict | measurement |
|---|---|---|---|---|
| **`S112`** | `industry_US` | 2026-08-31 | **`FIRED-B`** (with us) | `EW{XLU,XLRE,XLP}` 3-session excess vs `SPY`, 08-26 close → 08-31 close = **−2.3301pp** (XLU −2.9418% · XLRE −2.1734% · XLP −1.4953% ⇒ EW −2.2035%; SPY +0.1266%). Branch B threshold **≤ −1.757pp** (252-obs p15). ⇒ the three underweights did **not** rip together; the correlated-UW pattern did not cost this window. Anti-signal (intermeeting FOMC / emergency Treasury operation inside 08-26→08-31): **not observed** ⇒ not VOID. ★ Registered at the **49th percentile, dead centre**, and it produced a **15%-tail** outcome — the most informative starting state this desk had registered actually paid information |
| **`S104`** | `industry_US` | 2026-08-31 | **`FIRED-C`** (no conclusion changes) | `T10YIE` **2.33 (08-27) → 2.31 (08-31) = −2.0bp** `[FRED]` via `module_macro_us --series breakeven_10y`. Branch A ≥ +3.0bp, B ≤ −3.0bp ⇒ **between**. Disclosed at registration as **C ≈ 80%**. Anti-signal (refunding / buyback-size change / intermeeting Fed action inside 08-27→08-31): not observed (the buyback change was 08-19, outside) ⇒ not VOID |
| **`S103`** | `industry_US` | 08-29 → first settled close on/after = 2026-08-31 | **`FIRED-C`** ⚠ **construction defect recorded** | On the row's **explicit window** (2026-08-25 close → 08-31 close): `NVDA` +3.6283% · `SPY` +0.1488% ⇒ **excess +3.4794pp**, inside the hand-set ±5.0pp ⇒ **C**. 🚨 **But the same row also says "5-session excess", which puts the window at 08-24 → 08-31 and gives +5.4309pp = branch A.** The two descriptors in one row select different branches. **Scored on the explicit dated window (the more specific clause); thresholds untouched (`D242`); the disagreement recorded rather than resolved.** VOID check: `SPY` 08-25→08-31 **+0.149%** (inside ±3%), no `NVDA` guidance withdrawal / M&A / export-control action ⇒ not VOID. The row's own **LOW-RESOLUTION** label (hand-set bands, `D295` unmet) stands |
| **`S92`** | `industry_US` | 2026-08-31 | **`FIRED-D`** (none of the above — no information) | **A** (dated US action on the Strait, ≥2 independent foreign outlets, **AND** `CL=F` > 82.40): price leg ✅ **86.37**, **news leg ✗** — every in-window US item is rhetoric, not a dated action (*"Trump vows to make Hormuz US territory 'pretty soon'"* [aljazeera 08-15] · *"Trump claims Hormuz on Truth Social"* [euronews 08-23] · *"Trump: Mines fully removed"* [axios 08-25]). **B** (`CL=F` < 78.00 any session through 08-31): **✗ — window min 82.23 (08-26)**, 12 sessions measured. **C, the falsifier** (US-brokered halt to Ukrainian strikes on Russian energy infrastructure, ≥2 outlets): **refuted** — strikes continued through 08-28 (*"Ukraine Drones Spark Fire at Russian Refinery"* [oilprice 08-28] · *"Ukraine Says It Attacked Major Russian Oil Refinery in Yaroslavl"* [bloomberg 08-28] · [bloomberg 08-26] · [oilprice 08-25]). Anti-signal (OPEC+ **production decision** in window): **not observed** — the only OPEC items are Venezuela weighing exit, a membership story ⇒ **not VOID**. ★ **The only branch that could falsify the Energy OW's mechanism is the one that died, and `P66`'s Russia supply-destruction leg survives** (`M1149`) |
| **`S94`** | `industry_US` | 2026-08-31 | 🚨 **`UNSCOREABLE — construction defect`** (not `EXPIRED`) | Measured cleanly: `EW{COHR, LITE}` 5-session excess vs `SPY` (08-24 close → 08-31 close) = **+5.0505pp** (COHR +0.8494% · LITE +10.1895% ⇒ EW +5.5194%; SPY +0.4689%); `vol_surge` (5d/50d) **COHR 0.88 · LITE 0.78**; registry leg ✅ **`data/cycles/cycle_registry.json` still carries no optical/interconnect entry** (3 cycles: AI-compute floor 12.0 · Energy 8.0 · Missile-defense 0.0). **Branch A requires excess > +3pp AND `vol_surge` ≥ 1.0 on BOTH names — the conjunction breaks. Branch B (< −3pp) fails. Branch C (between ±3pp) fails.** **No branch covers the realized state: the partition is not exhaustive.** `S92` has a *"D = none of the above"*; this row does not. **Thresholds untouched (`D242`); returned to the owning desk** (`M1150`) |

**Not due, explicitly named rather than dropped**: **`S113`** (settle **2026-09-01 US close**; the US
session opens 22:30 KST — pre-settle read carried and **explicitly not a score**: `SMH` 08-25→08-31
excess **−0.0031pp**) · `S109` (09-02) · `S110`·`S114` (09-03) · **`S67-KR`** (09-04) · `S58-KR` (09-09).

**KR-owned rows settling on or before 2026-09-01: 0.** Full `SCENARIOS_KR.md` grep for `2026-09-01`
returned **one hit and it is not a settle date** — it is day 2 of `316140`'s `O1` observation window
(08-31 → 09-04, KIS institutional net-buy cumulative sign). **Zero silent skips.**

**`S8` — 32nd consecutive run unscoreable (KR desk count).** Still `[blank]`-dated. Not a neutral; a
row-construction failure whose observable must come from the owning desk (P5).
★ **And `S94` adds a second type to that class**: `S8` cannot be scored because it has **no date**;
`S94` cannot be scored because its **branches are not exhaustive**. Both are *"the row does not permit
scoring"*, not *"we declined to score"*. The generalized prescription is `D443-KR`.


---

# ═══ MASTER SCORING LOG — appended by `industry_US`, 2026-09-01 (Tue, pre-open KST) ═══

> ⚠ **Every row settled ONLY against its pre-registered observable and threshold** (`D242`) — no
> threshold was improvised, no band re-derived, no row VOIDed to make a call easier.
> ★ **11 rows scored — the largest single-run settlement in this desk's record.** The backlog cleared
> because `M1127`/`D426` (this desk fires pre-open) had left seven rows "due but unreadable" for two
> runs, and the 2026-08-31 close finally sat behind the run.
> **Composition: 3 directional (`S92` A · `S112` B · `P86` B) · 8 `C` · 0 `EXPIRED` · 1 unscoreable
> (`S8`, 34th) · 0 silent skips** (`D430`'s prescription).

| id | verdict | evidence |
|---|---|---|
| **`S124`** | ★★★ **`FIRED-A`** | COUNT of `us_top300` IT names (n=56) with positive 5-session excess vs `SPY` at the **08-31** close = **41**, threshold A ≥ 30. Window 08-24 → 08-31, `SPY` +0.469%, **0 names missing**. 41 sits **above the trailing-252 p85 (39)**; registration state was **13 of 56 = the 5.6th percentile of two years**. Anti-signal checked: no GICS reclassification of ≥3 names, no market-wide halt; MSCI's 08-31 review was pre-declared NOT a voider. ⚠ **`D93` had disclosed A as the ~50% favourite**, so this is a favourite landing — and `IT` had already been walked back from `UW` to `N` on 08-31, so it scores against a **partly-withdrawn** call. **Recorded as a partial hit against a partly-withdrawn verdict, not a clean one** |
| **`S112`** | ★★★ **`FIRED-B`** | `EW{XLU, XLRE, XLP}` 3-session excess vs `SPY`, 08-26 → 08-31 settled: `XLU` −2.942% · `XLRE` −2.173% · `XLP` −1.495% ⇒ EW **−2.204%**; `SPY` **+0.127%** ⇒ excess **−2.331pp** vs a B threshold of **≤ −1.757pp** (252-obs p15), clearing it by 0.57pp. **Registration state was −0.225 = the 49th percentile, dead centre** ⇒ the most balanced start this desk had registered in weeks, which makes this the more informative of the two directional hits. ⇒ **`UTIL UW` · `RE UW` · `STPL N` survive their own registered test**, and **the correlated-UW pattern is now measured rather than hypothesised** |
| **`S92`** | **`FIRED-A`** ⚠ **confirm-only by its own grading** | **B fails**: `CL=F` never closed below 78.00 through 08-31 (window min **82.23**; closes 81.25 · 82.40 · 84.50 · 84.94 · 85.83 · 87.83 · 87.06 · 85.01 · 82.36 · 82.23 · 83.53 · 83.40 · **85.76**). **C (the designated falsifier — a US-brokered halt to Ukrainian strikes on Russian energy) fails**: strikes continued through the window [bloomberg Yaroslavl 08-28 · Volga 08-26 · Samara 08-22 · aljazeera Krasnodar 08-25 · oilprice 08-28] ⇒ **`P66`'s Russia leg SURVIVES**, as pre-registered. **A fires on both legs**: price `CL=F` 08-31 **85.76 > 82.40** ✅; action leg met in **two independent categories, each ≥2 foreign outlets** — **declaration** [upi 08-22 *"Trump says Strait of Hormuz is 'an American territory'"*; forbes 08-18] and **interdiction/clearance** [fxstreet 08-25 *"US Navy has cleared Strait of Hormuz mines"*; axios 08-25; corroborated adversarially by bloomberg 08-26 *"US Allies Cast Doubt"*; hellenicshipping 08-13 *"US Navy fires on Iran-bound container ship"*]. ★ **`M1167`: the state moved AGAINST A's own premise on the settle date** — *"Iran Says Supertanker Hit by Mines in Strait of Hormuz"* [oilprice 08-31] and *"IRGC says ship struck 2 sea mines after U.S. declared Hormuz cleared"* [upi 08-31] falsify the demining declaration that helps satisfy A. **Scored A as written; the contradiction is recorded beside it, not used to re-band** ⇒ `D445` |
| **`P86`** | **`FIRED-B`** ⚠ **with a dissenting KPI** | B = *"core PCE MoM ≥ +0.35% **OR** `DGS2` ≥ 4.32"*. `[FRED]` `DGS2` at the first close covering 08-28 = **4.34 ≥ 4.32** ⇒ **B fires on the OR-leg**. (A required core PCE ≤ +0.20 **AND** `DGS2` ≤ 4.10 — the PCE leg went A's way at +0.2% (`M977`) but A is a conjunction and its rate leg failed.) ★ **`M1166`: B's own registered KPI dissents** — the row says *"branch B should carry `breakeven_10y` above 2.42"*; it reads **2.31** and did not move (2.33 → 2.31). The 08-28 session was **`DGS2` +14bp · `DGS10` +6bp · `DFII10` +8bp with breakevens FLAT** ⇒ **the wedge closed upward on the REAL-rate/policy-path leg, not on inflation compensation.** The branch label ("YoY wins") is **half-earned: the level test fired, the mechanism it named did not** |
| **`S94`** | **`FIRED-C`** ⚠ **the informative kind of C** | `EW{COHR, LITE}` 5-session excess vs `SPY` to the **08-31** settle (window start 08-24): `COHR` **+0.849%** · `LITE` **+10.189%** ⇒ EW **+5.519%**; `SPY` +0.469% ⇒ excess **+5.05pp**, i.e. **A's price leg clears +3pp by 2pp**. **But A is a conjunction and requires `vol_surge ≥ 1.0` on BOTH names**: `COHR` **0.83** · `LITE` **0.76** ⇒ **below 1.0 on both**. ★ The failed conjunct is exactly the one written in to guard against print-reaction volume decay, and it failed **in the direction that says the move is not volume-confirmed**. **A is NOT awarded on the price leg alone** (`D242`) ⇒ `D450` |
| **`S103`** | **`FIRED-C`** ⚠ **from a band pre-declared NO-INFORMATION** | `NVDA` 5-session excess vs `SPY`, 08-25 close → first settled close on/after 08-29 ⇒ **08-31**: `NVDA` 213.05 → 220.78 = **+3.628%**; `SPY` +0.149% ⇒ excess **+3.479pp**, inside ±5.0pp. ⚠ **The 2026-08-23 run had already declared these hand-set ±5.0pp bands inside the implied move (`NVDA` ±6.11%) and therefore NO-INFORMATION** ⇒ **this C is not evidence.** ★ And the pre-settle read (08-29, **+1.663pp**) understated the final by **2.1×** — the 4th consecutive pre-settle read to be wrong in sign or magnitude (`M1182`) |
| **`S104`** | **`FIRED-C`** — 1.0bp short of B | `T10YIE` change from the 08-27 `[FRED]` close to the first `[FRED]` close covering 08-31: **2.33 → 2.31 = −2.0 bp**, against A ≥ +3.0 / B ≤ −3.0. **Direction agrees with the desk's real-yield frame; magnitude does not reach the pre-registered bar. Stated, not rounded into B** |
| **`S111`** | **`FIRED-C`** (the disclosed ~78% favourite) | `ig_oas` `[FRED]` level at the first close covering 08-28 = **0.79**, unmoved from 08-27, against A ≥ 0.85 / B ≤ 0.77. ⇒ **`P67`'s instrument question is UNRESOLVED**: IG neither widened to confirm nor tightened to exonerate |
| **`S120`** | **`FIRED-C`** ★ **and the row's own lag clause worked** | Frozen observable = `DGS30` **and** `T10YIE` at the first observation where BOTH carry 2026-08-28. **The joint date arrived this run**: `DGS30` **5.22** · `T10YIE` **2.31**. A needed `DGS30` ≥ 5.31 ∧ `T10YIE` ≤ 2.38; B needed `DGS30` ≤ 5.10 ∧ `T10YIE` 2.28–2.40 ⇒ **C**. 5.22 sits inside the realised 8-obs range 5.17–5.27. ★ **The observation-lag clause written INTO the row let it wait three runs and settle cleanly — which is exactly what `S102` could not do.** ⚠ `D427` reproduced: `T10YIE` again runs one date ahead (08-31) of the constituents it is computed from (08-28) |
| **`S131`** | **`FIRED-C`** (the mandatory ≤48h MSCI bracket) | `RSP` − `SPY` 1-session excess, 08-28 → 08-31 settled: `RSP` **220.69 → 219.39 = −0.589%**; `SPY` **769.35 → 767.05 = −0.299%** ⇒ excess **−0.290pp**, against A ≥ +1.30 / B ≤ −1.30. ⚠ **`RSP`'s 08-28 close is inside the vendor hole**; 220.69 is the value frozen at registration and the 5m proxy independently gives **220.66** (0.014% apart) ⇒ **the verdict is C on either value.** Labelled |
| **`P97`** | **`FIRED-C`** ★ **readable for the first time — `D333` closed after 13 reproductions** | Frozen observable = broad dollar **and** `DGS10` at the first observation where BOTH carry the same date ≥ 08-28. **`DTWEXBGS` caught up from 08-21 to 08-28**, so the joint date is **08-28**: dollar **118.7479** · `DGS10` **4.73**. A: ≤117.44 ∧ ≥4.75 ❌ · B: ≥118.60 ∧ ≤4.65 — **the dollar leg ALONE clears B (118.75 ≥ 118.60) and `DGS10` misses ≤4.65 by 8bp** ⇒ **C**. ★ **The conjunction saved the row from a false B**, and a run reading only the dollar would have scored it B ⇒ `D450` |

### Rows still ARMED, disclosed and NOT scored
`P67` — `hy_oas` **2.60** at 08-28, **tighter on seven consecutive observations** (2.73 → 2.60) ⇒ **25bp
further from its 2.85% trigger than at registration**. With `S111` at C, the desk now has **two credit
instruments that both decline to confirm** the AI-capex-to-debt claim (`M1175`).
`P111`(09-14) · `P114`/`S126`/`S134`(09-04) · `S132`(09-03, ⚠ **now NO-INFORMATION**, `M1197`) ·
`S135`(09-11) · `S136`/`S137`(09-09) · `S127`–`S130` · `P81` `P85` `P87`–`P89` `P115`–`P117` · `S3`/`S4`.

### Named again rather than dropped
**`S8` — 34th consecutive run unscoreable** (US count); date field still `[blank]`. A human must `VOID`
it or re-register it with a date (P5). **KR-owned rows: zero due** (earliest `S67-KR` is 09-04).

---

# MASTER INDEX — appended 2026-09-01 by the `industry_US` run

| id | title | owner | settles | file |
|---|---|---|---|---|
| **`P121`** | The repricing is the POLICY PATH, not inflation, and not term premium | `industry_US` | **2026-09-04+** | `SCENARIOS_US.md` |
| **`P122`** | The oil bid is a supply event that positioning has not chased | `industry_US` | **2026-09-08** | `SCENARIOS_US.md` |
| **`P123`** | The AI trade's marginal dollar moved from COMPUTE to POWER | `industry_US` | **2026-09-08** | `SCENARIOS_US.md` |
| **`P124`** | Credit and the dollar both say this is a policy event, not a risk event | `industry_US` | **2026-09-18** | `SCENARIOS_US.md` |
| **`S138`** | `AVGO`: a threshold that is actually OUTSIDE the priced move (±11.00pp vs a measured ±9.6%) | `industry_US` | **first settled close after the 09-02/09-03 print** | `SCENARIOS_US.md` |
| **`S139`** | Re-arming the correlated-underweight bracket across the NFP | `industry_US` | **2026-09-04** | `SCENARIOS_US.md` |
| **`S140`** | Does IT's repaired breadth HOLD, or was 41-of-56 one week? | `industry_US` | **2026-09-08** | `SCENARIOS_US.md` |

> ⚠ IDs issued by `module_evidence next-id` (live scan of `handoff/*.md` · `llm_outputs/**` ·
> `REPORT/**`), **not hand-grepped** — highest existing `P120` / `S137` at write time (`D76` class).


# ═══ MASTER SCORING LOG — appended by the 2026-09-02 `industry_kr` run (append-only) ═══

> Run clock KST 08:16 → 10:0x, **before the KRX open**. Last settled session **2026-09-01** (KR and US).
> **Scored 1 · not-due named 7 · `EXPIRED` 0 · silent skips 0 · unscoreable named 1 (`S8`, 33rd on the KR count).**

| id | owner | event date | branch | evidence |
|---|---|---|---|---|
| **`S113`** | `industry_US` | **2026-09-01 US close** | **`FIRED-C`** | `SMH` 5-session excess vs `SPY`, settled closes, window **2026-08-25 close → 2026-09-01 close**: `SMH` **555.82 → 545.22 = −1.9071%**; `SPY` **765.91 → 761.78 = −0.5392%** ⇒ **excess −1.3679pp**, against A ≥ **+4.461pp** (252-obs p85) and B ≤ **−2.627pp** (p15). ★ **The informative part is where it started**: registration state was **−3.293 = the 12th percentile, already inside branch B**, and B was declared LOW-INFORMATION at registration. **The value moved UP and out of B** ⇒ **the semis de-rate did not continue through the catalyst** — but A required a genuine reversal and never came, so **the `IT UW` is neither falsified nor confirmed.** VOID clause (a dated US export-control announcement on advanced semiconductors inside 08-25 → 09-01): **did not fire.** ⚠ **Near-miss recorded rather than glossed**: scmp 08-31 *"US export controls on tungsten, battery black mass"* is a real export-control action on a **different product class**; tomshardware 08-28 reports a **draft** ("could be shared with industry as soon as September"); cna 08-27 is **tariffs, not export controls**. Thresholds untouched (`D242`) |

### Scored by this run because a KST-morning KR run is the natural scorer for the previous US session
`M1148` (registered 2026-09-01) again: the US desk fires pre-open and cannot read the US close dated
the same day (`D426`). `S113` settled on the **09-01 US close**, which sat behind this run.

### Not due — named rather than dropped

| row | settles | KST observable-at | why not today |
|---|---|---|---|
| **`S109`** (`FRO`, the Hormuz axis's one dated binary) | **2026-09-02 US close** | **09-03 05:00** | The observable is **tonight's** close. ⚠ **Reference pre-settle (08-26 → 09-01), explicitly NOT a score** (`D242`): `FRO` **+7.5728%** · `SPY` **−0.5613%** ⇒ **excess +8.134pp**, which sits **0.09pp above branch A's +8.043**. One session remains |
| `S110` · `S114` · `S132` | 2026-09-03 | 09-04 05:00 | not due |
| **`S67-KR`** · `S126` · `S134` · `S139` · `P114` | 2026-09-04 | — | not due |
| **`316140` observation point `O1`** | 2026-09-04 | — | **day 3 of 5** — graded partially in `BET_SHEET §D-1` (cumulative foreign **+14.7만** against the **+30만** threshold: 08-31 −44.7만, 09-01 +59.4만). **No early call** (`D242`) |
| `S127`–`S130` · `P122` · `P123` · `S140` | 2026-09-08 | — | not due |
| `S58-KR` · `S136` · `S137` | 2026-09-09 | — | not due |
| `S138` | first settled close after the 09-02/03 `AVGO` print | — | print has not occurred |

**KR-owned rows settling on or before 2026-09-02: 0.** Full `SCENARIOS_KR.md` search for `2026-09-02`
returns the `316140` observation window only, whose settle is 09-04.

### Named again rather than dropped
**`S8` — 33rd consecutive run unscoreable on the KR count** (34th on the US count); the date field is
still `[blank]`. A human must `VOID` it or re-register it with a date (P5). ★ Today the desk added a
**third** way a row can refuse to be scored, and it is the most expensive one: **`S8` has no date**,
**`S94` has a non-exhaustive branch partition**, and **`S92` is scorer-dependent** — see below.

### 🚨 A finding about the log itself, not about a row: **two desks scored the same rows on the same day and disagreed**

Reading the master log in full surfaced that the 2026-09-01 KR run (08:1x KST) and the 2026-09-01 US
run (23:0x KST) **both scored four rows**, and **two of the four verdicts conflict**:

| row | settle | KR desk verdict | US desk verdict | agree? |
|---|---|---|---|---|
| `S112` | 08-31 | `FIRED-B` | `FIRED-B` | ✅ |
| `S104` | 08-31 | `FIRED-C` | `FIRED-C` | ✅ |
| `S103` | 08-31 | `FIRED-C` | `FIRED-C` | ✅ |
| **`S92`** | **08-31** | **`FIRED-D`** | **`FIRED-A`** | 🚨 **conflict** |
| **`S94`** | **08-31** | **`UNSCOREABLE — construction defect`** | **`FIRED-C`** | 🚨 **conflict** |

**Neither block references the other.** Both stand in the log.

**Today's third measurement settles the evidence question on `S92` without re-scoring it.** The branch
required *"a dated US action on the Strait (declaration / escort regime / interdiction), ≥2 independent
FOREIGN outlets"* plus `CL=F` > 82.40. Re-queried today as `fts search Hormuz strike --days 3 --scope
foreign` (277 matches), the scored window contains **euronews 2026-08-30 *"US forces strike Iranian
rocket launchers in Strait of Hormuz"*** and **dw 2026-08-30 *"US military strikes Iran's Larak
Island"*** (Larak lies inside the Strait) — **two independent foreign outlets, dated 08-30, inside the
window that ended 08-31** — while the price leg was already met (`CL=F` 08-31 **85.76**).
⇒ **The KR desk's `FIRED-D` rested on a query that could not see the action reports** (it searched a
single term over 20 days and reviewed the BM25 top-40, without the `strike` conjunct and without the
`--scope foreign` the branch specified). **The US desk's `FIRED-A` is the verdict this measurement
supports.**

🚫 **This run does NOT re-score `S92` or `S94`.** They are `industry_US`-owned and already carry two
verdicts each; overwriting another desk's row violates `P5` and `D242`. What this run retracts is
**its own prior observation sentence** (`R121`), and what it registers is the process defect
(`D464-KR`): **a later scorer must read the earlier verdict and declare agreement or disagreement in
writing.** ★ **Why this matters more than a single row**: this desk's track record rests on scoring
being *reproducible*. If the same observable yields `A` and `D` from two scorers on the same day,
that row measured the scorer, not the market.

⚠ **A second, smaller reproducibility gap in the same pair**: on `S94` the two desks read different
`vol_surge` values for the same names on the same date — KR **COHR 0.88 / LITE 0.78**, US **0.83 /
0.76**. It changed no verdict (both below 1.0) and is logged rather than resolved.


# MASTER INDEX — appended 2026-09-02 by the `industry_US` run (PREMORTEM registrations)

| id | title | owner | settles | file |
|---|---|---|---|---|
| **`S141`** | Does the `AVGO` print move the SECTOR? (`SMH` exc1 vs `SPY`; the D-0 binary's sector leg) | `industry_US` | **2026-09-03** | `SCENARIOS_US.md` |
| **`S142`** | The against-us branch of the `FIN UW` issued 09-02, priced on the August CPI print (`XLF` exc3 vs `SPY`) | `industry_US` | **2026-09-11** | `SCENARIOS_US.md` |

> IDs issued by `module_evidence next-id` (live scan of `handoff/*.md` · `llm_outputs/**` ·
> `REPORT/**`), **not hand-grepped** — highest existing `S140` at write time (`D76` class).
> ⚠ Both rows are labelled **`implied-move UNCHECKED`**: the only straddles available for `SMH` and
> `XLF` expire **before** their observable windows open (D0), so the standard "threshold outside the
> implied move" warrant could not be issued and is **not** claimed.


# ═══ MASTER SCORING LOG — appended by the 2026-09-02 `industry_US` run (append-only) ═══

> Run clock **KST 22:09 → 23:2x = 09:09 → 10:2x ET**. **The NYSE had not opened when the run began.**
> Last settled US session **2026-09-01**.
> **Scored 1 (`P100`) · due-but-unreadable 1 (`S109`) · `EXPIRED` 0 · silent skips 0 · unscoreable
> named 1 (`S8`, 35th on the US count).**

## ★ The row that was scored — and it was NOT in this index until today

| id | owner | event date | branch | evidence |
|---|---|---|---|---|
| **`P100`** | `industry_US` | **2026-09-01 close** | **`FIRED-A`** | Frozen observable: `EW{MPC, VLO, PSX}` **20-session excess vs `SPY`**, settled closes, `auto_adjust=False`. Window **2026-08-04 → 2026-09-01**: `MPC` **+22.517%** · `VLO` **+17.251%** · `PSX` **+22.405%** ⇒ EW **+20.724%**; `SPY` **−1.238%** ⇒ **excess +21.963pp** against **A ≥ +13.478** (252-obs p85) and B ≤ −4.731 (p15). Registration state was **+11.597 = the 77.4th percentile** (inside C, leaning A); the settle sits at the **~94.9th percentile**, just under the p95 of +22.084. **VOID checked and did not fire**: `fts search OPEC --days 8 --scope foreign` returns **220 hits** with **no OPEC+ emergency production decision and no US SPR action**; the OPEC-adjacent story is *Venezuela weighing an OPEC **exit*** [bloomberg 08-27/28, investing_en 08-28], which is **structural, not a production decision**, and is explicitly **not** a voider; no M&A among the three names. ⚠ **What weakens the win, recorded beside it (`D445`)**: the row was designed as *"was it the margin story or the barrel?"* and its discriminator was a **barrel break** — **the barrel broke and then REVERSED inside the same window** (`CL=F` 82.23 on 08-26 → **90.22** on 09-01), so **A fired and the mechanism it was built to separate did not stay separated.** Thresholds untouched (`D242`); this is the direct reason **`P126`** was registered today |

🚨 **A finding about the LOG, not about the row: `P100` appears NOWHERE in this index or scoring log.**
It was registered by the **2026-08-26 MACRO stage**, lived only in that run's report, and was found
solely because this run opened the old file to build its self-backtest. **It settled on 09-01 and no
desk was going to score it.** ⇒ this is exactly what **`D449`** predicted (*a proposition whose branch
semantics live only in a run report*), and it is now upgraded from an inconvenience to a **missed
settlement**. `P101` (settles 09-04) and `P102` (09-09) are in the same state and are **named here so
they are reachable**.

## Due today, **not readable at this run's clock** — named, not skipped

| row | settle | why | reference pre-settle (**explicitly NOT a score**, `D242`) |
|---|---|---|---|
| **`S109`** (`FRO`, the Hormuz axis's one dated binary) | **2026-09-02 US close** | The observable is **tonight's** close; the desk fires at 09:09 ET. **`D426`, 3rd consecutive run as the binding constraint** | Window 08-26 → **09-01** (one session short): `FRO` **41.20 → 44.32 = +7.5728%**; `SPY` **766.08 → 761.78 = −0.5613%** ⇒ excess **+8.134pp**, **0.091pp above branch A's +8.043**. ⚠ **A is the WEAK-information branch by the row's own registration disclosure** (the state was already at the 89.3rd percentile). One session remains |

## Rows whose section headers still read `ARMED` but which are ALREADY scored — verified, not re-scored
`S92`(A) · `S94`(C) · `S104`(C) · `S112`(B) · `S124`(A) · `S131`(C) settled **08-31**; `S113`(C)
settled 09-01 (scored by the KR run of 09-02); `S103`(C) · `S111`(C) · `S120`(C) · `P86`(B) · `P97`(C)
likewise. **Their headers were never updated** ⇒ **`D472`**: *a scored row's section header carries its
verdict, so `ARMED` in a header means armed.* A `grep ARMED` on `SCENARIOS_US.md` returns **9 rows with
past settle dates, of which 8 are scored** — a reader trusting the headers would re-score eight.

## `D464-KR` honoured — this desk read the earlier verdict and states its agreement in writing
The 2026-09-02 KR run recorded that **two desks scored `S92` and `S94` on the same day and disagreed**
(`FIRED-D` vs `FIRED-A`; `UNSCOREABLE` vs `FIRED-C`), then produced a **third measurement** —
`fts search Hormuz strike --days 3 --scope foreign`, surfacing **euronews 08-30 *"US forces strike
Iranian rocket launchers in Strait of Hormuz"*** and **dw 08-30 *"US military strikes Iran's Larak
Island"***, two independent foreign outlets inside the scored window — that supports this desk's
`FIRED-A`. **This desk reads that and AGREES in writing.** 🚫 **Neither row is re-scored** (P5, `D242`);
the KR desk's own retraction (`R121`) of its observation sentence is accepted.

## Not due — named rather than dropped

| rows | settles |
|---|---|
| **`S141`** (registered today) · `S105` · `S106` · `S107` · `S110` · `S114` · `S132` · `S138` (first settled close after tonight's print) | **2026-09-03** |
| `S126` · `S134` · `S139` · `P114` · `P121` · **`P125`** (registered today) · `S67-KR` · **`P101`** | **2026-09-04** |
| `S127` · `S128` · `S129` · `S140` · `P122` · `P123` · **`P128`** (registered today) | 2026-09-08 |
| `S136` · `S137` · **`P126`** (registered today) · `S58-KR` · **`P102`** | 2026-09-09 |
| `S130` (⚠ dead thread — but its own thread is now **REIGNITED 15→2→4**, a status change recorded, row untouched) · **`P127`** (registered today) | 2026-09-10 |
| `S125` · `S135` · **`S142`** (registered today) | 2026-09-11 |
| `S123` | 2026-09-12 |
| `P111` · `S133` | 2026-09-14 |
| `P124` | 2026-09-18 |
| `S122` | 2026-09-30 |
| `P67` · `P81` · `P85` · `P87`–`P89` · `P115`–`P117` · `S3` · `S4` | open, no date reached |

**KR-owned rows settling on or before 2026-09-02: 0.**

### Named again rather than dropped
**`S8` — 35th consecutive run unscoreable** on the US count; the date field is still `[blank]`.
**A human must `VOID` it or re-register it with a date (P5).**

### ⚠ Both rows registered today carry a warrant this log has not seen before
**`S141`** and **`S142`** are labelled **`implied-move UNCHECKED`**. The stage rule requires a
magnitude threshold to be stated against the options market's implied move; for both rows **the only
straddle available expires BEFORE the observable window opens** (`SMH` **±0.9% at a D0 expiry**, `XLF`
**±0.4% at D0**), so it bounds today's residual move rather than the event. ⇒ **the warrant is
declined rather than faked** (`C3`). `AVGO`'s own **±9.5% (D0)** *was* usable and confirms
**`S138` (±11.00pp) is OUTSIDE** and **`S132` (±9.00pp) is INSIDE ⇒ NO-INFORMATION** (`D451`).

---

## MASTER scoring log — appended 2026-09-05 by the `industry_kr` run (append-only, shared spine)

> Scored against the **pre-registered observable and threshold only**. No threshold was touched (`D242`).
> `D389-KR` honoured: rows were enumerated from the **master log + settle dates**, never from `ARMED` header tokens
> (`D472` reproduces — `grep ARMED SCENARIOS_US.md` still returns already-scored rows).

### A · Scored by this run — **5 rows** (2 KR-owned, 3 US-owned)

| row | owner | observable (as registered) | measured | verdict |
|---|---|---|---|---|
| **`S69-KR`** | `industry_kr` | `O1` = sign of `316140` cumulative KIS **institutional** net-buy over the 5 settled sessions from 08-31; `O2` = `316140` − `069500.KS` return over the same window | `O1` = **+1,985k shares (positive)**, institutions bought in 4 of 5 sessions (+454k / −197k / +63k / +1,006k / +659k). **`VOID ①` FIRED** — `069500.KS` printed **−4.065%** on 09-02, above the row's own ±3.0% clause ⇒ **`O2` excluded, partial scoring on `O1` alone**, exactly as the row instructs | ★ **`FIRED-A` (partial)** |
| **`S67-KR`** | `industry_kr` | leg1 = sign of `000660` foreign 20-day cumulative at the 09-04 settled close; leg2 = did `005930` file a `자기주식취득결정` or a dividend-increase 주요사항보고서 to DART between 08-21 and 09-04 | leg1 **−2,457k = negative**; leg2 **YES** — 2026-08-21, rcpNo 20260821000616, **53,285,968 shares / ₩15.00tn / open-market purchase**. VOID clause (capital raise · major M&A · buyback suspension at `000660`) did not fire: 17 filings in 20 days, **zero** under 자본변동 | **`FIRED-C`** (the legs split ⇒ name-specific, not a sector event) |
| **`S126`** | `industry_US` | `XLI` 5-session excess vs `SPY`, 08-28 → 09-04 close | `XLI` **−1.056%** vs `SPY` **+0.109%** ⇒ **−1.165pp** against A ≥ −0.087 / B ≤ −2.500 | **`FIRED-C`** |
| **`S134`** | `industry_US` | `XLF` 5-session excess vs `SPY`, 08-28 → 09-04 close | `XLF` **+0.000%** vs `SPY` **+0.109%** ⇒ **−0.109pp** against A ≥ +2.00 / B ≤ −2.00 | **`FIRED-C`** |
| **`S139`** | `industry_US` | EW{`XLU`,`XLRE`,`XLP`} 3-session excess vs `SPY`, 09-01 → 09-04 close | `XLU` +1.222 · `XLRE` −0.250 · `XLP` −0.786 ⇒ mean **+0.062%** vs `SPY` **+1.104%** ⇒ **−1.042pp** against A ≥ +1.653 / B ≤ −1.757 | **`FIRED-C`** |

**Thresholds for the three US rows were taken verbatim from the 2026-09-04 `industry_US` HANDOVER §3c**, which
printed them *before* the settle. Nothing was re-derived. Scored here under **`M1148`** (a KST-morning KR run is
the natural scorer for the previous US session).

**What the scored rows change, stated rather than left in the table:**
- 🚨 **`S69-KR` bought almost no information, and it said so at registration.** Its own text declared
  *"`O1` positive is modal and low-information; the information is in `O2`"* — **and its own anti-signal then deleted `O2`.**
  ⇒ `STANDING_VIEW_KR §3b`'s "dilution = downside axis" clause is **NOT retired**: branch A required `O1` **and** `O2`.
  **`M1113` promotion stays on hold.** Reference `O2` (explicitly not a score, `D242`): 08-28→09-04 **−0.703pp**,
  08-31→09-04 **−0.014pp** — both inside band C either way.
  ⚠ **A construction defect, recorded without changing the verdict**: the row asserted *"`D394-KR` confirmed — 2026-09-05
  is a Friday, a KRX trading day."* **It is a Saturday.** The verdict was unaffected only because the observable named
  its five sessions explicitly. ⇒ **`D495-KR`**.
- 🚨 **`S67-KR`'s contagion leg fired on FORM, not on SUBSTANCE.** The registered question asks only *whether* `005930`
  filed; the filing's stated purpose is **employee share compensation**, not cancellation — whereas `000660`'s own
  08-19 filing was *"to enhance shareholder value through cancellation."* The registration's narrative was
  *"the peer followed ⇒ a capital-policy regime"*, and a compensation buyback is not that act. **Threshold untouched;
  the looseness is filed as `D496-KR`.** ★ And the row **left branch B on its registration day** — it was registered
  at 08-21 09:0x on *"zero treasury filings"* and the filing landed later the same day (**`M1264`**).
- 🚨 **Three `FIRED-C` verdicts in one block, on bands of ±1.65–2.00pp over 3–5 sessions, with realized values of
  0.109 / 1.042 / 1.165pp.** If sector-ETF 3–5 session dispersion vs `SPY` is smaller than those bands, **C is the modal
  branch and the rows could not buy information by construction.** ⇒ **`D497-KR`**: short-window sector-ETF excess
  brackets should take their bands from measured dispersion, the `D93` procedure the KR rows (`S64-KR`, `S68-KR`)
  already follow. ⚠ **`C4`: n=3. This says "all three settled today did", not "the US desk's bands are wide."**

### B · 🚨 A finding about the LOG, not about a row — **eight scored verdicts never reached this ledger**

The **2026-09-04 `industry_US` run** scored **eight rows** inside `llm_outputs/2026-09-04/industry_US/HANDOVER.md §3a`
(`S109` `FIRED-A` · `S105` `FIRED-A` · `S106` `FIRED-C` · `S107` `FIRED-C` · `S114` `FIRED-B` · `S132` `FIRED-C` ·
`S138` `FIRED-C` · `S141` `FIRED-C`, plus one VOID), **and none of them is in this log** — that run did not reach its
handoff writeback. **This block does not copy those verdicts** (P5, `D464-KR`: never overwrite another desk's row);
it records **that they exist and where**, so the next US run folds them in rather than re-scoring.
⇒ This is **`D449`'s superset — a proposition living only in a run report was bad; a *scoring* living only in a run
report is worse**, because the row still reads `ARMED` to everyone else. Registered as **`D494-KR`**, and it has
already cost this run once: hand-picked dig IDs `D485`–`D490` collided with numbers those unwritten runs had issued
(`D76` class), caught by `next-id`'s live scan and renumbered to `D494`–`D499`.

### C · Due but **not readable at this run's clock** — named, not skipped

| row | settle condition | why unreadable | reference state (**explicitly NOT a score**, `D242`) |
|---|---|---|---|
| **`P121`** | first `[FRED]` close covering 09-04 | 🚨 **`DGS2` stops at 09-03 (4.34%)**; `T10YIE` does carry 09-04 (2.35%) — the two series did not publish together (**`D427`, 4th reproduction**) | A needs `DGS2` ≥ 4.50 **and** `T10YIE` ≤ 2.36; B needs ≤ 4.18. At the 09-03 state `DGS2` 4.34 is neither, and the `T10YIE` leg alone would satisfy A's second condition |
| **`P114`** | same | same blocker | — |

**Not `EXPIRED`** — the settle condition itself has not arrived.

### D · `D347-KR` compliance — undated / unreachable rows

- **`S8`** — **37th consecutive run unscoreable**; the date field is still `[blank]`. **A human must `VOID` it or
  re-register it with a date (P5).** Writing this line for the 37th time is itself the finding.
- **`S3`** (~2026-09/10) · **`S4`** (~2026-09 late) — dates unparsed, not yet due.
- 🚨 **`P101`** (settled 09-04) · **`P102`** (09-09) — the `D449` class: registered by a 2026-08-26 MACRO stage and
  present in **neither the master index nor this log**. The 09-03 US run named them *"so they are reachable"*.
  **This run did not open the source report** (budget allocation) ⇒ **recorded as unscored with the source unread**,
  not silently passed. Next US run's item.

### E · KR-owned rows still ARMED, with dates — nothing dropped

`S58-KR` **09-09** · `S61-KR` **~09-14** · `S62-KR` **09-15** · `S64-KR`·`S65-KR`·**`S68-KR`** **09-19** ·
`S45`·`S54-KR` **09-30** · `S60-KR` **10-12** · `S49-KR` **10-30** · `S34`·`S53-KR` **10-31** · `S59-KR` **11-04**.
**Date-unparsed KR rows: 0.** ⚠ **`S68-KR`** (004370 농심, 21 settled sessions from 08-21) is at **day 11 of 21** —
no early call (`D242`).

**This run: `EXPIRED` = 0 · silent skips = 0 · brackets newly registered = 0** (the two propositions registered at MACRO,
`M-130` and `M-131`, are macro propositions with anti-signals and horizons, filed in `MACRO_REPORT §E`, **not** bracket rows —
stated here so their absence from the index is deliberate rather than lost).


---

## MASTER INDEX — appended 2026-09-05 by the `industry_US` run (PREMORTEM registrations)

| id | question | owner | settle | file |
|---|---|---|---|---|
| **`S145`** | Does the LOW-`vol_surge` sub-node lead its own sector? (`EW{STX,WDC,AMD}` − `SMH`, 4 settled sessions) — the desk's FIRST US-market read on the axis `C29` is about | `industry_US` | **2026-09-11** | `SCENARIOS_US.md` |
| **`S146`** | Is the AI-power lane one object, or is the book holding its worst name? (`EW{VST,CEG,VRT}` − `ETN`, 5 settled sessions) | `industry_US` | **2026-09-14** | `SCENARIOS_US.md` |
| **`S147`** | The refiner sub-node: EXTENDED-BUT-LIVE, or is `L2`'s peak-margin trap loaded? (`EW{MPC,PSX,VLO}` − `SPY`, 5 settled sessions) | `industry_US` | **2026-09-14** | `SCENARIOS_US.md` |
| **`S142-ANNEX`** | Not a new row — records that `S142`'s premise (`FIN UW`) was INVERTED to `FIN N` inside its own window on 2026-09-05. Thresholds UNTOUCHED (`D242`); branch labels must be read against the 09-02 verdict | `industry_US` | (rides `S142`, **2026-09-11**) | `SCENARIOS_US.md` |

> ⚠ **`S146` uses an asymmetric branch design, declared at registration**: branch A is set at **p95**
> (+7.651), not p85, because the state is already at the **92.9th percentile** — a p85 line would make
> A near-certain and therefore uninformative (`B4`), the same construction `P102` used.
> ⚠ **August PPI (09-10) was deliberately NOT bracketed**: neither branch would change the
> conclusion (`B4`), so the bracket was spent elsewhere. The CPI (09-11) already carries five
> independent both-sides rows (`P137`, `P138`, `S135`, `S142`, `S125`) plus `S145`.
> ★ **`P136` and `S147` are deliberately co-dated to 09-14 on the same theme at different units**
> (16-name sector vs 3-name refiner sub-node). If they fire different branches, the sector verdict
> and the sub-node verdict have separated — the `W5` question this desk keeps re-discovering.

### Dated settle queue, updated by this run
| rows | date |
|---|---|
| `S127` · `S128` · `S129` · `S140` · `P122` · `P123` · `P128` | 2026-09-08 |
| `S136` · `S137` · `P102` · `P126` | 2026-09-09 |
| `S130` · `P127` | 2026-09-10 |
| `S125` · `S135` · `S142` (+`S142-ANNEX`) · **`S145`** · `P137` · `P138` | **2026-09-11** |
| `S123` | 2026-09-12 |
| `P111` · `S133` · **`S146`** · **`S147`** · `P136` | **2026-09-14** |
| `P124` | 2026-09-18 |
| `S122` · `S48` | 2026-09-30 |
| `P121` · `P114` · `P125` | **blocked on `D427`** — settle when `DGS2`/`DFII10` publish 2026-09-04 |


---

## MASTER 채점 로그 — appended 2026-09-06 by the `industry_kr` run (**분할하지 않는 스파인**)

### A · 오늘 정산 도래한 행 = **0건**, 그리고 그것은 달력이 정한 것이다

- **2026-09-05(토)·2026-09-06(일)은 KRX·NYSE 모두 비세션**이다.
- **09-04 정착분은 어제(09-05) 런이 이미 전량 채점했다**: `S69-KR` **`FIRED-A`(부분, `O1` 만)** ·
  `S67-KR` **`FIRED-C`** · US 소유 `S126`·`S134`·`S139` 각 **C**.
- **날짜별 정산 큐**(09-05 US 런이 갱신)의 **다음 칸은 2026-09-08** —
  `S127`·`S128`·`S129`·`S140`·`P122`·`P123`·`P128`. **09-05·09-06 칸은 존재하지 않는다.**

⇒ **채점 0 · `EXPIRED` 0 · 조용한 스킵 0.**
⚠ **이것은 「도래했는데 안 봤다」가 아니라 「도래한 것이 없다」이고, 그 사실을 큐에서 확인한 뒤 적었다.**

### B · 정산 도래했으나 **읽을 수 없음** — 명시적으로 열거(스킵 아님) · **오늘 KR 이 독립 풀로 재측정**

| 행 | 정산 조건 | 오늘 실측 `[FRED]` | 상태 |
|---|---|---|---|
| **`P121`** · **`P114`** · **`P125`** | 2026-09-04 을 덮는 첫 `[FRED]` 종가 | 🚨 **`DGS2` 4.34 · `DGS10` 4.77 · `DGS5` · `DGS30` 5.25 · `DFII10` 2.42 전부 09-03 정지.** **`T10YIE` 만 09-04(2.35)** · `RRPONTSYD` 도 09-04 | **미정산 — `EXPIRED` 아님**(정산 조건 미도래) · **3런 연속 블록** |

★ **오늘 이 블록에 날짜를 붙일 수 있다**: `D507`(09-05 US 런 실측)이 **2026-09-07 = Labor Day** 라고 적었다.
⇒ **H.15 는 09-07 에도 발행되지 않는다.** **이 3행은 최소 2026-09-08 까지 블록이 유지된다**(4런째 예고).
★ **`P125` 의 구성은 여전히 작동 중이다** — 관측면이 **공동(joint) 날짜**를 명시하므로 **오채점이 아니라 미채점**으로 남는다.

### C · `D347-KR` 준수 — 날짜 미파싱 · 도달불가 행 칸

- **`S8`** — **39런 연속 정산 불가**(날짜 필드 `[blank]`). **사람이 `VOID` 하거나 날짜를 붙여야 한다(P5).**
- **`S3`**(~2026-09/10) · **`S4`**(`MU` FQ4 = **2026-09-30 16:00 ET**, `D488` 로 정정) — 미도래.
- ✅ **`P101` 은 닫혔다** — 09-05 KR 런이 「미채점, 원문 미열람」으로 남긴 행을 **09-05 US 런이 `FIRED-C`(−6.511pp)로 채점**했다.
  ⇒ **이 데스크가 이름을 불러서 도달 가능해진 행이 실제로 채점된 첫 사례**이고, `D504` 가 그 경로를 일반화했다.
- 🚨 **`P128`(09-08) · `P102`·`P126`(09-09) · `P127`(09-10)** — 여전히 **`D449`/`D504` 클래스**
  (MACRO 리포트 안에서 등록됐고 마스터 인덱스에 없다). **오늘 KR 런은 원문을 열지 않았다**(시간 배분).
  ⇒ **「미채점, 원문 미열람」으로 적는다.** **`P128` 이 모레 정산이므로 다음 US 런의 1순위.**

### D · KR 소유 · 미도래 전량 (변화 없음)

`S58-KR` **09-09** · `S61-KR` **~09-14** · `S62-KR` **09-15** · `S64-KR`·`S65-KR`·**`S68-KR`** **09-19** ·
`S45`·`S54-KR` **09-30** · `S60-KR` **10-12** · `S49-KR` **10-30** · `S34`·`S53-KR` **10-31** · `S59-KR` **11-04**.
**날짜 미파싱 KR 행: 0.**
⚠ **`S68-KR`**(004370 농심, 08-21 부터 21 정착세션)은 **11일차** — 조기 판정 금지(`D242`).
⚠ **`S58-KR`**(000660 충칭 패키징 지분매각, **회사가 스스로 박은 날짜**) **D-3**.

### E · 이번 런의 신규 브래킷 등록 = **0건**, 그리고 그 이유

**오늘 새 정착세션이 0개**라 **관측면을 새로 정착시킬 수 있는 창이 없었다.**
대신 **매크로 명제 2건**(`M-132`·`M-133`)을 등록했는데, 둘 다 **계기에 관한 명제**라
안티시그널과 지평은 있으나 **가격 관측면이 없어 브래킷 행이 아니다** — `MACRO_REPORT §E` 에 있다.
**이 부재는 누락이 아니라 의도임을 여기 적는다**(`D504` 가 지적한 「리포트 안에서만 사는 명제」를 피하기 위해).

⚠ **다만 다음 런이 브래킷을 걸어야 할 자리는 이미 있다**:
**2026-09-10 = 미 8월 PPI ∧ KOSPI200 선물·옵션 동시만기**(`M1349`) — **한 날에 두 바이너리**이고
**KR STRUCTURAL 캘린더는 이 날을 3런 연속 못 봤다**(`D391-KR`). **KR 은 PREMORTEM 블록이 없으므로
사람 또는 다음 US 런이 걸어야 한다.**


---

# ═══ MASTER SCORING LOG + MASTER INDEX — appended by the 2026-09-06 `industry_US` run (append-only) ═══

> Written **inside the HANDOVER stage**, not deferred to run end — following the 09-05 US run's own
> decision #6, and because `D490`/`D504`/`D529` are three of this run's dig items.
> **Clock**: KST 2026-09-06 22:0x = Sun 09:0x ET. **NYSE closed all weekend; last settled session
> 2026-09-04, and 2026-09-07 is Labor Day, so the next settled close is 2026-09-08.**

## A · Rows settling today = **0** — verified twice, by the queue AND by an exhaustive back-scan

- The dated settle queue (updated by the 09-05 US run) has **no 09-05 and no 09-06 cell**; its next
  cell is **2026-09-08**. The 09-06 KR run verified the same thing independently.
- **This run did not stop there.** `SCENARIOS_US.md` was parsed end-to-end: **152 row-blocks, 105
  with a header settle date on or before 2026-09-06**, each cross-searched for a verdict token in
  this log and in the US file. Section **C** is what that scan found.

⇒ **Newly scored 0 · `EXPIRED` 0 by omission · silent skips 0.**

## B · ★ FOLD-IN — ten verdicts that existed only in run reports are transcribed into this log

**Transcribed, NOT re-scored** (`D242`). Provenance: `llm_outputs/2026-09-04/industry_US/HANDOVER.md`
§3a (eight + one VOID, derived by this desk on 09-04 against the pre-registered observables) and
`llm_outputs/2026-09-05/industry_US/HANDOVER.md` §3c (`P101`). The 09-05 KR run named the eight in
its §B and deliberately did **not** copy them (`D464-KR`); the 09-05 US run folded them into its own
HANDOVER and **its writeback reached three of four handoff files, skipping this log** (`M1352`).
**This block closes that gap.**

| row | registered | settle | verdict | derived by | observable & measurement |
|---|---|---|---|---|---|
| **`S109`** | 2026-08-26 (US PREMORTEM) | 2026-09-02 | ★ **FIRED-A** | 2026-09-04 HANDOVER (industry_US) | `FRO` 5-session excess vs `SPY`, 08-26 → 09-02: 41.20 → 45.42 vs `SPY` 766.08 → 765.16 ⇒ **+10.363pp** against branch A's **≥ +8.043** |
| **`S105`** | 2026-08-28 (US PREMORTEM) | 2026-09-03 | ★★ **FIRED-A** | 2026-09-04 HANDOVER (industry_US) | [`MRVL` exc10] − [`AVGO` exc10] @ 09-03 = −18.190 − (−3.273) ⇒ **−14.917pp** against branch A's **≤ −10.836**. ⇒ the Google→`MRVL` warrant did **not** displace `AVGO`; the spread went the other way, hard |
| **`S106`** | 2026-08-28 (US PREMORTEM) | 2026-09-03 | **FIRED-C** | 2026-09-04 HANDOVER (industry_US) | `MSFT` exc10 vs `SPY` @ 09-03 = **+4.635pp**, inside the band |
| **`S107`** | 2026-08-28 (US PREMORTEM) | 2026-09-03 | **FIRED-C** | 2026-09-04 HANDOVER (industry_US) | `EW{T,VZ}` exc10 vs `SPY` @ 09-03 = **+2.105pp**, inside the band. ⚠ The `T` orphan survives its first and only test **without resolving** — a C on an orphan is not an ownership |
| **`S110`** | 2026-08-30 (US PREMORTEM) | 2026-09-03 | 🚨 **VOID** | 2026-09-04 HANDOVER (industry_US) | [`HPE` exc5] − [`DELL` exc5] @ 09-03 = −9.289pp, **which would have been branch B** — voided because **both names printed inside the window**, the row's own anti-signal. ★ Root cause is `D488` (the earnings-date field every VOID clause reads is wrong) |
| **`S114`** | 2026-08-26 (US PREMORTEM) | 2026-09-03 | ★ **FIRED-B** | 2026-09-04 HANDOVER (industry_US) | `EW{NUE,STLD}` exc5, 08-26 → 09-03 = **+3.134pp** against branch B's **≥ +0.826**. Points at a **held** name (`NUE`) |
| **`S132`** | 2026-09-01 (US PREMORTEM) | first settled close after the `AVGO` print | **FIRED-C** | 2026-09-04 HANDOVER (industry_US) | `AVGO` 1-session excess = **−3.792pp** inside **±9.00** |
| **`S138`** | 2026-09-01 (US PREMORTEM) | same | **FIRED-C** | 2026-09-04 HANDOVER (industry_US) | same observable, band **±11.00** ⇒ **the wider band bought no information the narrower one did not**, which is `D503`'s point measured on this desk's own pair |
| **`S141`** | 2026-09-02 (US PREMORTEM) | 2026-09-03 | **FIRED-C** | 2026-09-04 HANDOVER (industry_US) | `SMH` exc1 vs `SPY`, 09-02 → 09-03 = **−0.662pp** (A +1.802 / B −1.732). ⚠⚠ **Near-miss carried WITH the verdict (`D505`)**: the sector move the row was built to catch printed **+3.00pp excess on 09-04**, **1.7× branch A's line, one bar outside the window.** The verdict stands (`D242`); `S141` is a **timing** miss, not a direction miss |
| **`P101`** | 2026-08-26 (US MACRO §D — **a `D449`/`D504` row, absent from this index until today**) | 2026-09-04 | ★★ **FIRED-C** | 2026-09-05 HANDOVER (industry_US) §3c | `EW{App SW, Systems SW, IT Consulting; n=19}` − `EW{Semis, Semicap, Tech HW/Storage, Electronic Components, Electronic Equip, EMS, Comms Equip; n=37}`, 5-session returns, window 08-28 → 09-04. Legs: SW **−4.458% / 21.1% positive**; HW **+2.053% / 73.0% positive** ⇒ spread **−6.511pp** (A ≥ +3.196 / B ≤ −7.906). ★★ Registration state was **+6.228 = the 89.7th percentile leaning A**; the settle stopped **1.40pp short of branch B** — a **−12.74pp** traverse, with **participation inverting from 91.7%/16.7% to 21.1%/73.0%**. VOID checked and not fired (no GICS reclass moved ≥3 of 56; no halt ≥1 session) |

⚠ **Two carried claims are DATED by this block, not retracted**: `M1251`'s *"IT's weak half is
semicap/test"* (the 5-session drag is **EDA + security software** — `ADSK` −16.40 · `CDNS` −14.01 ·
`SNPS` −11.02 · `PANW` −10.32 · `DDOG` −10.15), and `M1244`'s n=1 rule that a leaning registration
state is better-behaved than a pre-settle read (`P101` is sample 2 and points the other way).

## C · 🚨 A finding about the LOG, not about a row — **five past-dated rows the settle queue cannot see**

The back-scan in §A found five US-owned rows whose settle dates have passed and whose verdicts are
**not in this log**. They fall into three distinct classes and only one of them was already known.

| row | settle | days past | where the verdict is | class |
|---|---|--:|---|---|
| **`S16`** — Meta Q2, the COMM sector-vs-name separation test | **2026-07-29** | **39** | 🚨 **nowhere.** This log's line 28 still carries verdict `—`; the only later mention is a **2026-07-30 interim tracking line** (*"categorical leg recorded, windows open to 08-12 / 09-30"*) | **`EXPIRED-UNSCORED`** |
| **`S24`** — MSFT/META/AMZN capex, the **Utilities** leg | **2026-07-29** | **39** | 🚨 **nowhere.** Master-index row only; same 07-30 tracking line as its last state | **`EXPIRED-UNSCORED`** |
| **`S42`** — the 07-29 run's own INDU verdict, bracketed against itself | **2026-08-12** | **25** | 🚨 **nowhere.** Last state 2026-07-30, *"tracking branch B (with us)"* | **`EXPIRED-UNSCORED`** |
| **`S25`** — RE OW−, `DLR` rs20 vs the {PLD, AMT, WELL} median | 2026-08-08 | 29 | ✅ **scored** — `FIRED (threshold met) — ⚠ ZERO-INFORMATION`, 2026-08-02 HANDOVER — **but the verdict lives in `SCENARIOS_US.md` line 1259 and never reached this shared log** | **logged in the wrong file** |
| **`S110`** | 2026-09-03 | 3 | ✅ **VOID**, derived 09-04, lived only in two run reports — **folded in by §B above.** Its master-index row (line 1091) still reads `ARMED` | **`D494-KR`, now closed** |

★★ **The mechanism behind the three `EXPIRED-UNSCORED` rows, and it is mechanical, not a lapse.**
All three were registered in the **2026-07-23 → 07-29 PREMORTEM cohort**; all three had their last
recorded state written as an **interim "tracking" line on 2026-07-30**; the desk then had a multi-day
gap. **An interim tracking line contains the row id and a branch name, so it matches a later run's
verdict scan** — the row reads settled to a grep and unsettled to a reader. Every subsequent run
inherited the **settle queue** (a forward-looking object built from what someone remembered to
register) rather than re-scanning the file, so none of them could have found these.
⇒ Registered as **`D531`** (*an interim tracking line takes a token no verdict scan will match*) with
**`M1355`** as its measurement.

⚠ **This run does NOT score `S16`/`S24`/`S42`.** Two of the three settle on capex-guide readings and
one on a 20-session peer-median as of 07-29 / 08-12; reconstructing a threshold 25–39 days later is
exactly what `D242` forbids. **`EXPIRED-UNSCORED` with the reason is the honest verdict.** A human
may `VOID` them or re-register them with fresh dates (**P5**).

⚠ **`S25` is NOT re-scored either** — it was scored correctly on 2026-08-02. What is recorded here is
that **this log did not receive it**, which is the same defect class as §B, three weeks earlier.

## D · Due but **not readable at this run's clock** — named, not skipped (`D427`, **7th reproduction**)

`module_macro_us --days 400 --json` re-pulled this run. The split publication reproduces exactly:

| carries **2026-09-04** | stops at **2026-09-03** | stops earlier |
|---|---|---|
| `T10YIE` **2.35** · `RRPONTSYD` 0.675 | `DGS2` **4.34** · `DGS10` 4.77 · `DGS5` 4.52 · `DGS30` 5.25 · **`DFII10` 2.42** · `hy_oas` **2.65** · `ig_oas` 0.81 · `VIXCLS` 14.32 · `SOFR` 3.66 | `WALCL` 09-02 · `DTWEXBGS` **08-28** · `NFCI` 08-28 |

| row | settle condition | reference state (**explicitly NOT a score**, `D242`) | status |
|---|---|---|---|
| **`P121`** | first `[FRED]` close covering 2026-09-04 | A needs `DGS2` ≥ 4.50 **and** `T10YIE` ≤ 2.36; B needs `DGS2` ≤ 4.18. At 09-03 `DGS2` **4.34** is neither; the `T10YIE` leg alone (2.35) would satisfy A's second condition | **blocked, 4th consecutive run** |
| **`P114`** | same | — | **blocked, 4th** |
| **`P125`** | *"the first observation where **BOTH** `T10YIE` and `DFII10` carry 2026-09-04"* | 3-session (Δ`breakeven_10y` − Δ`real_10y`) recomputed from source this run: **−11.0 (08-28) → −11.0 (08-31) → −8.0 (09-01) → −0.0 (09-02) → +6.0 bp (09-03) = the 88.1st percentile of trailing 252** (p05 −11.0 · p15 −6.0 · p50 0.0 · **p85 +5.0** · p95 +9.0). ⚠ **+6.0 is ABOVE branch A's +5.0 line** | **blocked, 4th** |

★ **The block now has a calendar FLOOR, stated in advance rather than discovered.** `2026-09-07` is
**Labor Day** (`D507`, measured by the 09-05 US run); H.15 does not publish on a federal holiday.
⇒ **these three rows are blocked through at least 2026-09-08.**

★★ **And `P125`'s construction is doing exactly what it was written to do, which is worth stating
plainly because it is rare.** The row's observable names the **joint** date rather than a calendar
date, explicitly citing `D427` at registration. **A calendar-dated version of the identical row would
have been scored branch A today, on a `DFII10` value that does not exist.** The row is protecting
itself from a verdict it would have gotten wrong ⇒ **unscoreable rather than mis-scoreable**
(`M1356`). This is the second consecutive run in which `D427`-awareness at registration has paid.

## E · `D347`/`D504` compliance — undated and index-absent rows

- **`S8`** — **40th consecutive run unscoreable.** Date field still `[blank]`. **A human must `VOID`
  it or re-register it with a date (P5).** The 40th writing of this line is the finding.
- **`S3`** (~2026-09/10) · **`S4`** (`MU` FQ4 = **2026-09-30 16:00 ET**, `D488`-corrected) — not due.
- ✅ **`P125`·`P126`·`P127`·`P128` are written into the master index by this run** (section F) —
  closing the `D504` class for the four rows that were in it. **`P128` settles 2026-09-08**, which the
  09-06 KR run named as *"the next US run's #1 priority."* This run is that run and the row is now
  reachable by any desk.
- ⚠ **`P102`·`P111`·`P136`·`P137`·`P138` were checked against the index and ARE present** — the
  `D504` residual after this block is **0 among propositions with a settle date ≤ 2026-09-14**.

## F · MASTER INDEX additions — four `D449`/`D504` propositions, transcribed from their MACRO report

> **Source read verbatim**: `llm_outputs/2026-09-02/industry_US/MACRO_REPORT.md` §D. **No threshold,
> branch line, window, anti-signal or owner is altered** (`D242`). These rows have existed and been
> live since 2026-09-02; only their *index entry* is new.

| id | question | owner | settle | branch A | branch B | file |
|---|---|---|---|---|---|---|
| **`P125`** | Is the repricing's leg flipping from REAL to INFLATION? (`P121`'s own registered falsifier) — [3-session Δ`breakeven_10y`] − [3-session Δ`real_10y`], bp, **at the first observation where BOTH series carry 2026-09-04** | `industry_US` | **joint-date (blocked, ≥09-08)** | **≥ +5.0 bp** (p85) | **≤ −6.0 bp** (p15) | `MACRO_REPORT` 2026-09-02 §D |
| **`P126`** | Is the escalation finally paying the BARREL, or still only the CHAIN? — `EW{XOM,CVX,EOG,FANG}` − `EW{MPC,VLO,PSX}`, 5-session returns, settled closes, `auto_adjust=False` | `industry_US` | **2026-09-09** | **≥ +2.312** (p85) | **≤ −4.443** (p15) | `MACRO_REPORT` 2026-09-02 §D |
| **`P127`** | Did the AI marginal dollar go to POWER, or come back to COMPUTE? — `EW{VST,CEG,TLN,NRG,GEV,ETN,PWR}` − `EW{NVDA,AVGO,ANET}`, 5-session, window **09-03 close → 09-10 close** (start chosen to put the `AVGO` print in the BASE, not inside the window) | `industry_US` | **2026-09-10** | **≥ +4.555** (p85) | **≤ −5.790** (p15) | `MACRO_REPORT` 2026-09-02 §D |
| **`P128`** | Does the global bond selloff reach US CREDIT, or is it a rates-only event? — `hy_oas` `[FRED]` **5-session change in bp**, at the first `[FRED]` close covering 2026-09-08 | `industry_US` | **2026-09-08** | **≥ +10.3 bp** (p85) | **≤ −9.0 bp** (p15) | `MACRO_REPORT` 2026-09-02 §D |

⚠ **`P128` reference state carried at transcription** (explicitly **not** a score): `hy_oas` 5-session
change at 09-03 = **+2 bp**, inside branch C; **level 2.65 = the 2.0th percentile of trailing 252**.
`D3` applies and the row already states it — **the LEVEL is at an extreme while the CHANGE is
mid-pack, and the row is written on the change.** ⚠ Its settle also depends on `hy_oas` publishing,
and `hy_oas` currently stops at **09-03** — so `D427` may reach this row too.

⚠ **`P127`'s window closes 09-10, the same session as US August PPI.** Its anti-signal list does not
name a macro print, so PPI is **not** a voider — recorded now rather than argued at scoring (`D450`).

### Dated settle queue, updated by this run

| rows | date |
|---|---|
| `S127` · `S128`* · `S129`* · `S140` · `P122` · `P123` · **`P128`** | **2026-09-08** *(first session after Labor Day)* |
| `S128` · `S129` · `S136` · `S137` · `P102` · `P126` | 2026-09-09 |
| `S130` · `P127` | **2026-09-10** *(US Aug PPI ∧ KOSPI200 quad witching — **unbracketed**, `D533`)* |
| `S125` · `S135` · `S142` (+`S142-ANNEX`) · `S145` · `P137` · `P138` | **2026-09-11** *(US Aug CPI)* |
| `S123` | 2026-09-12 |
| `P111` · `S133` · `S146` · `S147` · `P136` | 2026-09-14 |
| `P124` | 2026-09-18 |
| `S37` · `S40` · `S48` · `S122` | 2026-09-30 |
| `P121` · `P114` · `P125` | **blocked on `D427`, floor 2026-09-08** (Labor Day 09-07) |

\* `S128`/`S129` are carried in both the 09-08 and 09-09 cells by the 09-05 run's queue and their own
headers; **the header date (09-09) governs** and the discrepancy is recorded rather than silently
resolved.

## G · New bracket registrations by this stage = **0**, and the reason

**No new settled session exists**, so no observable can be frozen against a fresh state, and the
`D93` dispersion that every branch line must come from would be computed on the same distribution the
09-05 run already used. **Registering a row today would produce a bracket that is a copy of
yesterday's with a later date — width without information** (`D503`, `L3`).

⚠ **The place the next bracket belongs is already identified**: **2026-09-10 carries US August PPI
AND the KOSPI200 quadruple witching** — two binaries on one session, on two desks' calendars. The
09-06 KR run named this and stated it cannot bracket it (KR has no PREMORTEM block, `M1349-KR`).
⇒ **assigned to this run's PREMORTEM stage** and registered as **`D533`** so the assignment is
written down rather than assumed.

---

---

## MASTER INDEX — appended 2026-09-06 by the `industry_US` run (PREMORTEM registrations)

> Written **inside** the PREMORTEM stage (the 09-05 run's decision #6), because `D490`/`D504`/`D529`
> are three of this run's dig items. Full registrations in `handoff/SCENARIOS_US.md`.
> ⚠ Windows count **settled** sessions: **2026-09-07 is Labor Day**, so 09-08 · 09-09 · 09-10 ·
> 09-11 · 09-14.

| id | question | owner | settle | branch A | branch B | state at registration | file |
|---|---|---|---|---|---|---|---|
| **`S148`** | Does `P101`'s software/hardware inversion survive the software leg's own two biggest scheduled prints? `EW{SW n=19}` − `EW{HW n=37}`, 5 sessions. **`ORCL` and `ADBE` both report 09-10 16:00 ET and both are IN the SW leg** | `industry_US` | **2026-09-14** | ≥ **+3.927** (p85) | ≤ **−7.906** (p15) | **−6.511 = 21.0th pctile** — 1.40pp from B, 10.4pp from A ⇒ **A is the informative branch** | `SCENARIOS_US.md` |
| **`S149`** | The regime-flip bracket: escalation vs **the US Treasury Secretary's own** $40-crude forecast. `CL=F` 5-session % change | `industry_US` | **2026-09-11** | ≥ **+8.343** (p85) | ≤ **−5.734** (p15) | 🚨 **+9.688% = 87.7th pctile** — the *level* is above A's line but the observable is the NEXT five sessions' change ⇒ **B is the more reachable branch and B is the against-us branch** | `SCENARIOS_US.md` |
| **`S150`** | Defense: a node event, or is the book just holding the worst name? `EW{RTX,LMT,NOC,GD,LHX}` − `SPY`, 5 sessions | `industry_US` | **2026-09-14** | ≥ **+2.902** (p85) | ≤ **−3.611** (p15) | 🚨 **−5.166 = 7.1st pctile, already BELOW B's line** ⇒ **B carries little information; A and C carry it**, disclosed at registration | `SCENARIOS_US.md` |

> ⚠ **`S150` has NO dated catalyst and NO thread — both stated at registration.** It is a positioning
> row on a one-year-extreme starting point, and it is filed ★★ rather than ★★★ for that reason.
> ⚠ **`S149`'s thresholds come from `D93` on the observable itself, not from a straddle** — the only
> Energy straddle (`XLE` ±1.6%) **expires 09-09, before the row settles**, and borrowing a proxy
> straddle that expires early is the scope error `M1305` made and `M1326` corrected.
> ★ **Binaries deliberately NOT bracketed, with reasons** (`B4`): the `ORCL`/`ADBE` **magnitude**
> (no-information — implied ±11.8%/±8.1% against an observable whose p85/p15 vs `SMH` are +3.15/−3.66;
> `S132`/`S138` are the measured precedent, `D503`) · **US PPI 09-10 standalone** (already inside
> `S148`'s and `S149`'s windows) · **FOMC 09-16** (outside every window; deferred to a run with a
> settled tape and the 09-11 COT) · **S&P rebalance 09-18** (structural, not directional; `P124`
> already settles that date) · **KOSPI200 quad witching 09-10** (🚫 out of scope for `--market us`,
> `W1` — the 09-06 KR run's request cannot be discharged by a US-pure desk, so **`D533` stays open**
> and needs a human or a KR protocol change, **P5**).

### Dated settle queue, updated by this run
| rows | date |
|---|---|
| `S127` · `S140` · `P122` · `P123` · **`P128`** | **2026-09-08** *(first session after Labor Day)* |
| `S128` · `S129` · `S136` · `S137` · `P102` · `P126` | 2026-09-09 |
| `S130` · `P127` | **2026-09-10** *(US Aug PPI · `ORCL` · `ADBE` — three binaries, one session)* |
| `S125` · `S135` · `S142` (+ANNEX) · `S145` · **`S149`** · `P137` · `P138` · **`P140`** | **2026-09-11** *(US Aug CPI)* |
| `S123` | 2026-09-12 |
| `P111` · `S133` · `S146` · `S147` · **`S148`** · **`S150`** · `P136` · **`P139`** | **2026-09-14** |
| `P124` | 2026-09-18 |
| `S37` · `S40` · `S48` · `S122` | 2026-09-30 |
| `P121` · `P114` · `P125` | **blocked on `D427`, floor 2026-09-08** (Labor Day 09-07) |

## H · `D472` header hygiene — performed, counted, and its residual reported for the first time

**Scoring and header hygiene are two different writes, and only one of them has ever happened at run
end.** This run did both.

- **9 headers in `SCENARIOS_US.md` were changed from `· ARMED ·` to `· **SETTLED <verdict>** ·`** for
  the rows folded into the log in section B: `S105` FIRED-A · `S106` FIRED-C · `S107` FIRED-C ·
  `S109` FIRED-A · **`S110` VOID** · `S114` FIRED-B · `S132` FIRED-C · `S138` FIRED-C · `S141`
  FIRED-C. Each carries the scoring date and the folding run, so provenance survives the edit.
- 📊 **Residual, measured for the first time: `SCENARIOS_US.md` still carries 47 `ARMED` headers with
  a past settle date** (down from **56** before this pass; the full `ARMED`-token count across all
  block bodies is **63**).
- ⚠ **The 47 are NOT fixed and must not be.** Changing a header to `SETTLED` requires a verdict, and
  a verdict on a 25–39-day-old observable is exactly what `D242` forbids. **`S16`, `S24` and `S42`
  are marked `EXPIRED-UNSCORED` in section C instead**, which is the honest label. A human may
  `VOID` them or re-register them with fresh dates (**P5**).
- ★ **The number is published so the next run can measure whether it falls.** A dig with no counter
  is a dig nobody can tell is being worked.

---

# ═══ MASTER 채점 로그 + MASTER INDEX — appended 2026-09-07 by the `industry_kr` run (분할하지 않는 스파인) ═══

> **HANDOVER 스테이지 안에서 스캔하고 런 종료 시 기록한다.**
> **시계**: KST 2026-09-07 08:17 시작 = 월 개장 43분 전. **마지막 정착 세션 금 2026-09-04**(KR·US 공통).
> **US 는 오늘 Labor Day 휴장** ⇒ **다음 US 정착 종가는 09-08.**
> ⚠ **런 도중 09:00 에 KRX 가 개장했다** — 09-07 KR 정착분은 **15:30 이후**이고 **이 런에는 없다.**

## A · 오늘 정산 도래한 행 = **0건** — 큐로 확인하고, **그 다음 전수 스캔으로 다시 확인했다**

- **날짜별 정산 큐**(09-05 US 런 갱신)의 다음 칸은 **2026-09-08**(`S127`·`S128`·`S129`·`S140`·`P122`·`P123`·`P128`).
  **09-07 칸은 존재하지 않는다.**
- 🚨 **그러나 큐만 보고 멈추지 않았다** — 어제 US 런이 `D531` 로 *"the queue is forward-looking and structurally
  cannot show them"* 을 실측했기 때문이다. **KR 도 같은 스캔을 처음 돌렸다**(§B).

⇒ **채점 0 · `EXPIRED` 0 · 조용한 스킵 0.**

## B · ★★★ **`SCENARIOS_KR.md` 전수 back-scan — KR 데스크 최초**

**헤더에서 39개 행 id 를 파싱 · 정산일이 오늘 이전인 행 23개** 를 마스터 로그와 대조:

| 결과 | 건수 | 목록 |
|---|---:|---|
| **자기 행에 판정이 적혀 있음** | **21** | `S10`·`S11`·`S17`·`S18`·`S22`·`S27`·`S29`·`S33`·`S38`·`S46-KR`·`S47-KR`·`S48-KR`·`S50-KR`·`S51-KR`·`S55-KR`·`S56-KR`·`S57-KR`·`S63-KR`·`S66-KR`·`S67-KR`·`S69-KR` |
| 🚨 **판정은 실재하나 「자기 행」에는 없음** | **2** | **`S28`** · **`S52-KR`** |
| ⛔ **`EXPIRED-UNSCORED`** | ★ **0** | — |

- ★ **`EXPIRED-UNSCORED` = 0.** **US 는 같은 스캔에서 3건**(`S16`·`S24`·`S42`, 25~39일 경과)을 찾았다.
  **KR 에는 그 클래스가 없고, 이제 그것을 「큐가 그렇게 말해서」가 아니라 「스캔했으므로」 말할 수 있다.**
- 🚨 **그러나 완전히 깨끗하지도 않다 — 2행의 판정이 「다른 행의 산문」에만 있다**:
  - **`S28`**(SK이터닉스 임시주총, 07-28) → **`FIRED-A`** 가 **`S22` 행 본문**에 있다
    (*"S28(07-28 임시주총 두 후보 선임 = A)이 예고한 대로 정산"*, `SCENARIOS.md:485`). **자기 마스터 행 없음.**
  - **`S52-KR`**(제약 OW, 08-19) → **`미결(undecided)`** 로 채점되고 **`S64-KR`(09-19)로 재등록**됐는데,
    그 확인이 **US 데스크가 쓴 줄**(`SCENARIOS.md:925`)에 있다. **KR 마스터 로그에 자기 판정 행 없음.**
  ⇒ **판정은 실재하고 소실은 0이다. 없는 것은 색인이다.** **그리고 색인의 부재가 US 3행을 39일 숨긴 기제다.**
  ⇒ **`D550` 등록.**

### B-b · ⚠ 이 스캔 자체가 두 번 거짓 ✅ 를 냈다 (`D48` · 지우지 않고 적는다)
① **id 주변 ±300자** 검색 ⇒ **23/23 ✅**(옆 행의 판정 토큰을 매칭).
② **id 와 판정 토큰의 같은 줄** 동시등장 ⇒ **역시 23/23 ✅** — 히트 다수가
*"Condition-check executed on every ARMED row…"* 같은 **요약 행**이었고, `S11`·`S18`·`S47-KR` 의 히트는
실제로는 **`"NOT EXPIRED"`·`"PENDING"`** 이었다(**부정문이 긍정 판정으로 읽힘**).
③ **테이블 첫 칸이 그 id 인 행만** 보는 세 번째 시도에서야 신호가 깨끗해졌다.
⇒ 🚨 **`D531` 은 US 파일의 특성이 아니라 verdict-grep 자체의 특성이다.** **`D551` 등록.**

## C · 정산 도래했으나 **읽을 수 없음** — 명시적 열거(스킵 아님) · **KR 이 독립 풀로 재측정**

| 행 | 정산 조건 | **오늘 실측 `[FRED]`** | 상태 |
|---|---|---|---|
| **`P121`** · **`P114`** · **`P125`** | 2026-09-04 을 덮는 첫 `[FRED]` 종가 | 🚨 **`DGS2` 4.39 · `DGS5` 4.52 · `DGS10` 4.77 · `DGS30` 5.25 · `DFII10` 2.42 — 전부 09-03 정지.** **`T10YIE` 만 09-04(2.35)** · `RRPONTSYD` 도 09-04(0.7) | **미정산 — `EXPIRED` 아님** · **4런 연속 블록** |

★ **오늘은 예고의 확인이다**: 09-06 두 런이 *"`D507`(09-07 Labor Day)과 곱하면 블록은 최소 09-08 까지"* 라고 적었고
**09-07 다리가 실제로 그렇게 됐다.** ⇒ **`D427` 7번째 재현**(KR 독립 측정 2번째).
★ **`P125` 의 구성은 여전히 작동 중이다** — 관측면이 **공동(joint) 날짜**를 명시하므로 **오채점이 아니라 미채점**으로 남는다.

## D · `D347-KR` 준수 — 날짜 미파싱 · 도달불가 행

- **`S8`** — **40런 연속 정산 불가**(날짜 필드 `[blank]`). **사람이 `VOID` 하거나 날짜를 붙여야 한다(P5).**
- **`S3`**(~2026-09/10) · **`S4`**(`MU` FQ4 = **2026-09-30 16:00 ET**, `D488` 정정) — 미도래.
- **`P128`(09-08) · `P102`·`P126`(09-09) · `P127`(09-10)** — ✅ **어제 US 런이 마스터 인덱스에 써 넣어 `D504` 클래스를
  4행에 대해 닫았다.** **오늘 KR 은 원문을 열지 않았다**(시간 배분) ⇒ **「미채점, 원문 미열람」으로 적는다.**
  **`P128` 이 내일 정산이므로 다음 US 런의 1순위.**

## E · KR 소유 · 미도래 전량 (변화 없음)

`S58-KR` **09-09 (D-2)** · `S61-KR` **~09-14** · `S62-KR` **09-15** · `S64-KR`·`S65-KR`·**`S68-KR`** **09-19** ·
`S45`·`S54-KR` **09-30** · `S60-KR` **10-12** · `S49-KR` **10-30** · `S34`·`S53-KR` **10-31** · `S59-KR` **11-04**.
**날짜 미파싱 KR 행: 0.**
⚠ **`S68-KR`**(004370 농심, 08-21 부터 21 정착세션)은 **11일차 그대로** — 새 세션이 없었다. **조기 판정 금지**(`D242`).
⚠ **`S58-KR`**(000660 충칭 패키징 지분매각, **회사가 스스로 박은 날짜**) **D-2.**
★ **`feedback_bracket_registration_state_stale` 를 여기 미리 박는다**: 다음 런이 D-1 에 「아직 공시 없음」을 보더라도
그것은 **부재의 증거가 아니고**(`D94`), **등록 시 선언한 상태를 정산일에 인용하지 말고 원천을 재조회한다.**

## F · 이번 런의 신규 브래킷 등록 — **1건**

| id | question | owner | settle | file |
|---|---|---|---|---|
| **`S151-KR`** | **2026-09-10 은 KOSPI200 선물·옵션 동시만기 ∧ 미 8월 PPI 다. 그날 KR 가격의 주인은 만기 물량인가 매크로인가?** 관측면 = `069500.KS` 의 ① 09-10 거래량 ÷ 직전 20 정착세션 거래량 중앙 ② 09-10→09-11 되돌림 비율 | **`industry_kr`** | **2026-09-11** | `SCENARIOS_KR.md` |

> ★ **왜 오늘인가**: L2 `schedule` 의 등록 문턱은 **근월 잔존일 ≤5** 인데 **어제 7 이라 안 걸렸고 오늘 4 로 걸렸다**
> (`M1410`). 그리고 `catalyst_calendar` STRUCTURAL 은 `--days 5`·`--days 10` 둘 다 이 날짜를 **못 본다**
> ⇒ **`D391-KR` 4번째 재현 · `D533`(어제 US 등록) 은 이 등록으로 KR 쪽만 닫힌다.**
> ⚠ **KR 프로토콜에는 PREMORTEM 이 없으므로 BET 이 걸었다.** 등록 상세는 `BET_SHEET.md §5`.
> ⚠ **정보량 선언: favourite 없음** — 이 데스크는 KR 만기 세션의 거래량 분포를 **측정한 적이 없다**(`C3`).

### 날짜별 정산 큐 — 이 런이 갱신
| rows | date |
|---|---|
| `S127` · `S128` · `S129` · `S140` · `P122` · `P123` · `P128` | 2026-09-08 |
| `S136` · `S137` · `P102` · `P126` · **`S58-KR`** | 2026-09-09 |
| `S130` · `P127` | 2026-09-10 |
| `S125` · `S135` · `S142`(+ANNEX) · `S145` · `S149` · `P137` · `P138` · `P140` · **`S151-KR`** | **2026-09-11** |
| `S123` | 2026-09-12 |
| `P111` · `S133` · `S146` · `S147` · `S148` · `S150` · `P136` · `P139` · **`S61-KR`** | 2026-09-14 |
| **`S62-KR`** | 2026-09-15 |
| `P124` | 2026-09-18 |
| **`S64-KR`** · **`S65-KR`** · **`S68-KR`** | 2026-09-19 |
| `S122` · `S48` · `S37` · `S40` · **`S45`** · **`S54-KR`** | 2026-09-30 |
| **`S60-KR`** | 2026-10-12 |
| **`S49-KR`** | 2026-10-30 |
| **`S34`** · **`S53-KR`** | 2026-10-31 |
| **`S59-KR`** | 2026-11-04 |
| `P121` · `P114` · `P125` | **`D427` 로 블록** — `DGS2`/`DFII10` 가 2026-09-04 을 발행할 때 정산 |

---

# ═══ MASTER SCORING LOG — appended by the 2026-09-07 `industry_US` run (append-only) ═══

> Written **inside the HANDOVER stage**, not deferred to run end (`M1352`: the scoring log is the
> writeback target that gets dropped, because it is the only one that transcribes another stage's work).
> **Clock**: KST 2026-09-07 22:2x = Mon 09:2x ET. **2026-09-07 is US Labor Day — NYSE closed; last
> settled session 2026-09-04; next settled close 2026-09-08.**

## A · Rows settling today = **0**, verified by the queue AND by an exhaustive re-scan under a NEW method

The dated settle queue has no 09-07 cell. **This run did not stop there**, and it did not repeat the
09-06 method either: the 2026-09-07 `industry_kr` run registered **`D551`** hours earlier —
*verdict-grep is not a verdict-confirmation tool; only a table row whose FIRST cell is that id counts.*

**`D551` was tested against the US file as a controlled comparison, and it reproduces:**

| method | past-dated `ARMED` headers in `SCENARIOS_US.md` | reported verdicted | **missed** |
|---|--:|--:|--:|
| ±200-char proximity grep (the 09-06 method) | 87 | 84 | **6** |
| **first-cell table row only (`D551`)** | 87 | 81 | **0 known** |

⇒ **`M1411`** — `D551` is a property of the *technique*, not of the KR file. The 09-06 run's *"five
past-dated rows it could not see"* was itself an undercount produced by the weaker method.

## B · ★★ SIX rows past settle with no verdict anywhere — and FOUR were scoreable all along

| row | settle | days past | verdict | observable & measurement |
|---|---|--:|---|---|
| **`S19`** | 2026-07-29 decision / numeric legs → **2026-08-05** | 33 | ★ **FIRED-M** | Invalidation checked first: HY OAS > 3.10% on a close ⇒ window **max 2.87%**, not invalidated. **H** (raised, OR held with `DGS2` > 4.45 by 08-05): decision was *held with three dissents for a hike*; `DGS2` **4.22 · 4.23 · 4.28 · 4.25 · 4.20 · 4.18**, max **4.28** ⇒ did not fire. **D** (held dovish AND `DGS2` < 4.15 by 08-05): min **4.18** ⇒ did not fire. **M** (held, 4.15–4.45): **every close inside the band** ⇒ *"no conclusion changes."* ⚠ The row's pre-registered `n≈1` warning (FOMC 07-29 and June PCE 07-30 share one driver, oil) is carried with the verdict |
| **`S9`** | 2026-07-29 *"and running"* — **no terminal date registered** | 40 | ★ **FIRED-B** | `DFII10` over **27 settled observations 07-29 → 09-03: min 2.32 · max 2.47**, with `T10YIE` quoted alongside (the row's own two-series rule). **Zero below 2.20 (A), zero above 2.55 (C)** ⇒ **B on every observation the row could ever have been scored against** — *"term-premium blip; the tilt survives on flow."* ⚠ **B was disclosed at registration as the low-information branch** — this verdict is not a licence to re-argue the duration bet. 🚨 The missing end-date is filed as **`D555`** |
| **`S41`** | 2026-08-12 | 26 | ★★ **FIRED-B** | IG OAS (`BAMLC0A0CM`) on a close, HY quoted alongside. **A** (IG ≥ 0.90 by 08-12): the 11 closes are **0.81 · 0.80 · 0.79 · 0.78 ×6 · 0.79 · 0.79**, **max 0.81 — never reached**. **B** (IG < 0.90 **and** HY < 3.10 through 08-12): HY window max **2.87** ⇒ both legs held. Single-issuer default (invalidation) did not occur. ⇒ **the single-name AI CDS widening (Oracle ~200bp · NVDA ~78bp *"risen sharply"* · Meta ~93bp vs IG index ~53bp) did NOT transmit to the index inside 14 sessions; `S26-A` held.** ⚠ The registration's own counter-evidence (CDS trades are thin, single-digit daily, `[news]`-grade single-wire) is carried intact — this is **not** evidence the channel is useless, only that it did not transmit in this window. **`D97` (no CDS feed) stays open** |
| **`S46`** | 2026-08-13 | 25 | ★★ **FIRED-A — the AGAINST-US branch** | Leg (i) gross-margin guide **flat or down: MET** (already on record from the 08-02 partial; B's *"guided up"* leg therefore permanently false). Leg (ii) `AAPL` RS20 − `QCOM` RS20 (both vs `SPY`, settled closes), registration state **+32.6pp**: **07-31 +16.34 · 08-04 +10.68 · 08-07 +10.63 · 08-11 +5.50 · 08-13 −4.99pp**. A needs **< +15pp** by 08-13 — **crossed 2026-08-04 and never recovered**; window min **−4.99** on the settle date. ⇒ **both legs of A met.** *"The ledger revival was flow-chasing into a binary, and the zero-base reading was right."* ★ The row's stated information content — *"branch A falsifies a decision this run made three stages earlier"* — is realised. ⚠ The separately-registered ±3.3% reaction test (`D28` fix) is **not** folded in to soften it. ⚠ The verdict lands on a **decision class** (a `resolve --outcome revived` taken on a flow pull hours before an unbracketed binary), **n=1** |
| **`S14`** | 2026-08-06 (branch B's invalidation date) | 32 | 🟡 **A-PARTIAL — half published, half named** | {`MA`,`V`,`PYPL`} RS20 vs `SPY` on all five post-print sessions **and** the 08-06 date: `MA` **+5.95 → +7.84** · `V` **+0.80 → +4.15** · `PYPL` **+25.52 → +29.66** — **all three positive throughout** ⇒ **branch B is definitively ruled out** (it requires the RS20 flip) and **A's price leg is MET**. A's fundamental leg (*cross-border volume holds*) could **not** be retrieved 39 days later: `fts search "Mastercard cross-border" --days 60 --scope foreign` returns **0**, and the only 07-30 print article in the pool speaks to **purchase transactions and GDV**, not to the frozen observable. **Widening the observable to GDV to make it scoreable is what `D242` forbids** ⇒ filed as **`D556`** |
| **`S5`** | ~2026-08-11 | 27 | **`EXPIRED-UNSCORED` — reassigned by name** | KR semiconductor customs exports, 1–10 August. Scoring a Korean customs series on a `--market us` desk is a **`W1`** cross-market transfer. ⇒ **assigned to `industry_kr`**, named here so it cannot be carried silently a third time |

⇒ **`M1413`**: *four brackets that had been open 25–40 days were scoreable from already-published data
the entire time. The obstacle was never data availability; it was that nothing looked.*

## C · `D427` — 8th reproduction, and the 09-06 pre-commitment HELD

`module_macro_us --days 400 --json` re-pulled this run:

| carries **2026-09-04** | stops at **2026-09-03** | stops earlier |
|---|---|---|
| `T10YIE` **2.35** · `RRPONTSYD` 0.675 | `DGS2` **4.34** · `DGS10` 4.77 · `DGS5` 4.52 · `DGS30` 5.25 · `DFII10` **2.42** · `hy_oas` **2.65** · `ig_oas` 0.81 · `VIXCLS` 14.32 · `SOFR` 3.66 | `WALCL` 09-02 · `DTWEXBGS` **08-28** · `NFCI` 08-28 |

**Identical split to 09-06.** H.15 does not publish on a federal holiday, so **`P121` · `P114` · `P125`
are blocked for a 5th consecutive run — and the 09-06 run predicted this floor in advance** (`M1412`).
★ `P125`'s joint-date construction continues to make it **unscoreable rather than mis-scoreable**.

## D · `D347`/`D504` compliance

- **`S8`** — **41st consecutive run unscoreable.** Date field still `[blank]`. Human `VOID` or
  re-registration (**P5**). The 41st writing of this line is the finding.
- **`S3`** (~2026-09/10) · **`S4`** (`MU` FQ4 = **2026-09-30 16:00 ET**, `D488`-corrected) — not due.
- `P125`·`P126`·`P127`·`P128` were written into the master index by the 09-06 run; **`D504` residual
  among propositions settling ≤ 2026-09-14 remains 0.**

## E · `D472` header hygiene — performed and counted

**Six headers in `SCENARIOS_US.md` updated** from `· ARMED ·` to `· **SETTLED <verdict>** ·` for the
rows scored above: `S19` FIRED-M · `S9` FIRED-B · `S41` FIRED-B · `S46` FIRED-A · `S14` A-PARTIAL ·
`S5` EXPIRED-UNSCORED(→KR). Each carries the scoring date and this run as the scorer.

📊 **Residual: `SCENARIOS_US.md` past-dated `ARMED` headers 87 → 81** (the 09-06 run reported 47 on a
narrower definition; **this run's 87 counts every header carrying any past date, which is the honest
denominator** and is stated so the two numbers are not confused). **The remainder must NOT be forced
to `SETTLED`** — a verdict on an observable this old is what `D242` forbids, unless (as with the four
above) the observable is fully specified and the data was published at the time.

### Dated settle queue — unchanged by this run (no new session, no new registrations here)

| rows | date |
|---|---|
| `S127` · `S140` · `P122` · `P123` · **`P128`** | **2026-09-08** *(first session after Labor Day)* |
| `S128` · `S129` · `S136` · `S137` · `P102` · `P126` | 2026-09-09 |
| `S130` · `P127` | **2026-09-10** *(US Aug PPI · `ORCL` · `ADBE`)* |
| `S125` · `S135` · `S142` (+ANNEX) · `S145` · `S149` · `P137` · `P138` · `P140` | **2026-09-11** *(US Aug CPI)* |
| `S123` | 2026-09-12 |
| `P111` · `S133` · `S146` · `S147` · `S148` · `S150` · `P136` · `P139` | 2026-09-14 |
| `P124` | 2026-09-18 |
| `S37` · `S40` · `S48` · `S122` | 2026-09-30 |
| `P121` · `P114` · `P125` | **blocked on `D427`, floor 2026-09-08** |
| **`S5`** | **reassigned to `industry_kr`** — `EXPIRED-UNSCORED` on this desk (`W1`) |

## F · New bracket registrations by this stage = **0**, and the reason

Same as 09-06 and for the same measured reason, now on its third run: **no new settled session exists**,
so no observable can be frozen against a fresh state and the `D93` dispersion every branch line comes
from would be computed on the identical distribution the 09-05 run used. **A row registered today would
be yesterday's row with a later date — width without information** (`D503`, `L3`). Registration is
PREMORTEM's job this run, against the **09-10 (US Aug PPI · `ORCL` · `ADBE`)** and **09-11 (US Aug CPI)**
cells.

---

## MASTER INDEX — appended 2026-09-07 by the `industry_US` run (PREMORTEM registrations)

> Written **inside** the PREMORTEM stage (the 09-05 run's decision #6), because `D490`/`D504`/`D529`
> remain on this desk's dig list. Full registration in `handoff/SCENARIOS_US.md`.
> ⚠ Windows count **settled** sessions: **2026-09-07 was Labor Day**, so the next settled closes are
> 09-08 · 09-09 · 09-10 · 09-11 · 09-14.

| id | question | owner | settle | branch A | branch B | state at registration | file |
|---|---|---|---|---|---|---|---|
| **`S152`** | 🚨 **The ECB decision the desk's own calendar does not carry.** Is the long-end move US-domestic (the desk's frame) or EXTERNAL — ECB hike + Japan selling USTs to fund yen intervention + $40tn issuance? `TLT` **3-session % change**, window **09-09 close → 09-14 close** (start chosen so the ECB decision AND the US CPI print are INSIDE the window) | `industry_US` | **2026-09-14** | **≥ +0.913%** (p85) — long end **rallies**; `RE`+`STPL`+`UTIL` lose their driver together | **≤ −1.124%** (p15) — hawkish transmission; the three UWs vindicated on an EXTERNAL cause | ★ **+0.415% = 67.1st pctile — genuinely mid-pack.** The only **balanced** bracket this desk registered today; `P142` registered above its own branch A and `P143` above p95 | `SCENARIOS_US.md` |

> ⚠ **The straddle does NOT cover this row and that is stated rather than papered over**: `TLT`
> 예상변동 **±0.7%, expiry 2026-09-09 — before the window opens** (`M1305`/`M1326`). Thresholds are
> from `D93` on the observable itself.
> ★ **Branches deliberately NOT bracketed, with reasons** (`B4`):
> · **`ORCL` + `ADBE` prints 09-10** — measured no-information: implied **±11.8%** and **±8.1%**
>   against an observable whose `D93` p85/p15 vs `SMH` are **+3.15 / −3.66**; `S132`/`S138` are the
>   precedent (`D503`), and **`S148` already owns the pair's real question**, settling 09-14.
> · **US Aug PPI 09-10 standalone** — already inside `S148`/`S149` windows.
> · **US Aug CPI 09-11 standalone** — bracketed from nine directions already.
> · 🚨 **FOMC + SEP 09-16 — deferred a SECOND time, now WITH A DEADLINE.** Every branch line would
>   come from a `D93` computed on a tape frozen at `asof 2026-09-04` (third consecutive run), and the
>   09-11 COT does not exist yet. **Commitment, filed as `D564`: the row must be registered by the
>   2026-09-11 run at the latest**, because after the CPI prints the pre-print information is in the
>   base. A deferral with a date is a plan; a deferral without one is avoidance.
> · **KOSPI200 quad witching 09-10** — 🚫 out of scope for `--market us` (`W1`); **`D533` stays open**
>   for a 2nd run and needs a human or a KR protocol change (**P5**).
> · **S&P rebalance 09-18** — structural, not directional; `P124` already settles that date.

### Dated settle queue, updated by this run

| rows | date |
|---|---|
| `S127` · `S140` · `P122` · `P123` · **`P128`** | **2026-09-08** *(first settled session after Labor Day)* |
| `S128` · `S129` · `S136` · `S137` · `P102` · `P126` | 2026-09-09 |
| `S130` · `P127` | **2026-09-10** *(US Aug PPI · **ECB decision** · `ORCL` · `ADBE` — four binaries, one session)* |
| `S125` · `S135` · `S142` (+ANNEX) · `S145` · `S149` · `P137` · `P138` · `P140` · **`P142`** | **2026-09-11** *(US Aug CPI)* |
| `S123` | 2026-09-12 |
| `P111` · `S133` · `S146` · `S147` · `S148` · `S150` · **`S152`** · `P136` · `P139` · **`P143`** | **2026-09-14** |
| `P124` | 2026-09-18 |
| `S37` · `S40` · `S48` · `S122` | 2026-09-30 |
| `P121` · `P114` · `P125` | **blocked on `D427`, floor 2026-09-08** |
| `S5` | **reassigned to `industry_kr`** — `EXPIRED-UNSCORED` on this desk (`W1`) |
| `P144` | **instrument row — no price observable, deliberately NOT indexed as a bracket** (recorded in `MACRO_REPORT §D`) |

---

## MASTER INDEX — appended 2026-09-07 by the `industry_US` run (`D449`/`D504` propositions, transcribed from their MACRO report)

> **Source read verbatim**: `llm_outputs/2026-09-07/industry_US/MACRO_REPORT.md` §D. **No threshold,
> branch line, window, anti-signal or owner is altered** (`D242`).
> ★ **Written the SAME DAY the propositions were registered**, rather than three runs later — which
> is what `D504` exists to prevent. The 09-06 run had to transcribe `P125`–`P128` four days late; this
> block closes the class at zero latency.

| id | question | owner | settle | branch A | branch B | state at registration | file |
|---|---|---|---|---|---|---|---|
| **`P142`** | ★★★ **The front end has repriced five sessions running. Is this a HIKE PATH, or a term-premium / supply event?** `DGS2` `[FRED]` **5-session change in basis points**, at the **first `[FRED]` close covering 2026-09-11** (the August CPI session) | `industry_US` | **2026-09-11** | **≥ +10.0 bp** (trailing-252 **p85**) — the repricing extends *through* the CPI print and the **FOMC on 09-16** becomes a live two-sided event for every duration-sensitive tilt | **≤ −7.0 bp** (**p15**) — it was the global bond selloff reaching the US front end and it unwinds once the auction/CPI calendar clears | 🚨 **+14.0 bp = the 92.1st pctile — ALREADY ABOVE branch A's line.** ⇒ **A is the LOW-information branch and B is the informative one**, disclosed at registration | `MACRO_REPORT` 2026-09-07 §D |
| **`P143`** | ★★ **The BoJ / yen carry channel: a global-duration binary NO row on this desk brackets.** `FXY` **5-session % change**, settled closes, `auto_adjust=False`, the 5 settled closes following 2026-09-04 (**09-08 → 09-14**) | `industry_US` | **2026-09-14** | **≥ +0.704%** (**p85**) — the yen extends; US long duration takes a second leg on a driver that is **not** the Fed | **≤ −1.062%** (**p15**) — intervention exhaustion; the channel closes | 🚨 **+2.480% = the 94.8th pctile, above p95.** ⇒ **A is low-information; B is informative AND is the branch that would CLOSE a risk the desk has not been counting** | `MACRO_REPORT` 2026-09-07 §D |

> ⚠ **`P142`'s `D427` exposure is declared at registration**: `DGS2` currently stops at **09-03**. Its
> observable names *the first close covering 09-11* — **deliberately copying `P125`'s construction**,
> the only thing that has protected a row from `D427` so far. If the lag persists the row is
> **blocked, not mis-scored**.
> ⚠ **`P143`'s mechanism was CORRECTED by this run's own EVENT_ALPHA stage, hours after registration,
> and the correction is recorded rather than the row edited** (`D48`): it was registered as *"a BoJ
> hike → carry unwind → US duration"*, and the body read (`[news — CNBC 2026-09-07]`: reserves
> **−6.18% to $1.207tn**, **¥27.1tn** of 2026 intervention, *"Japan likely sold a portion of its U.S.
> Treasury holdings to finance its currency intervention"*) shows the channel actually running is
> **intervention-funded UST SELLING — a SUPPLY channel that operates whether or not the BoJ hikes.**
> **Observable and thresholds UNCHANGED** (`D242`); only the stated mechanism is corrected.
> ⚠ **`P143` has NO dated catalyst in `catalyst_calendar`** — the BoJ's September meeting date is not
> carried by the tool and **this desk did not invent one**; the window is set by the desk's own
> 5-session convention. Stated rather than dressed up.
> ⚠ **`P143`'s two narrative instruments disagree** and that is disclosed, not resolved: the thread
> axis is 🟢 REIGNITED (**2→6** on FX reserves) while `theme-age` reads `yen` ⚪**ECHO 1.24×**. That is
> `D508`'s exact class.
> 🚫 **`P144` is deliberately NOT indexed here.** It is an **instrument** proposition with an
> anti-signal and a falsifier but **no price observable**, so it is not a bracket. It lives in
> `MACRO_REPORT` §D and is named in this writeback — **stating the absence is what keeps `D504` from
> reproducing in the other direction** (indexing a non-bracket would corrupt the settle queue).

## MASTER INDEX — appended by the 2026-09-08 `industry_kr` run

| id | 명제 · 동결 관측면 | 등록 데스크 | 정산일 | 파일 |
|---|---|---|---|---|
| **`S153-KR`** | 🚨 **표적관세는 세율이 붙는 순간 KR 메모리의 진짜손을 뒤집는가?** 09-07 에 `005930`·`000660`·`066570`·`009150` 4/4 가 외국인 ∧ 기관 매수·개인 매도였다. 관측면 = **O1** `005930`·`000660` 의 **외국인 20일 누적 부호**, **O2** 미 행정부의 **세율 또는 국가별 할당량 공표일(D0)**. 판정 창 = **D0 +3 정착세션**. A = 2종 모두 양(+) 유지(관세가 이미 가격에) · B = 1종 이상 음(−) 전환(랠리가 관세를 안 봤다) · C = D0 부재 또는 부호 갈림. **favourite = A ⇒ 값은 B 가 날 때 크다**(B 는 「KIS 실측 = A급」이라는 이 데스크의 최다 사용 근거를 깎는다) | **`industry_kr`** | **2026-09-30** | `SCENARIOS_KR.md` |

### 날짜별 정산 큐 — 이 런이 추가하는 행
| 브래킷 | 정산일 |
|---|---|
| **`S58-KR`** | **2026-09-09 (D−1)** |
| `S151-KR` | 2026-09-11 |
| `S61-KR` | ~2026-09-14 |
| `S62-KR` | 2026-09-15 |
| `S64-KR` · `S65-KR` · `S68-KR` | 2026-09-19 |
| `S45` · `S54-KR` · **`S153-KR`** | **2026-09-30** |


---

# ═══ MASTER SCORING LOG — appended 2026-09-08 by the `industry_US` run (Stage 2 / HANDOVER) ═══

> Written **inside HANDOVER**, not deferred to run end (`M1352`'s measured failure mode).
> Method: `D551` strict first-cell scan, **re-implemented independently this run**, followed by a
> prose read of every candidate (`D576` — the strict rule has a false-positive rate too).

| id | owner | observable, as frozen | measurement | verdict |
|---|---|---|---|---|
| **`S13`** | `industry_US` | Registered 2026-07-23 (PREMORTEM), settle 2026-07-29, measured over the **10 sessions after the print (to ≈2026-08-12)**. THREE legs: (1) capex guide at MSFT and META (raised/held/cut); (2) spenders' NTM P/E change; (3) suppliers' (MU, AMAT, LRCX, KLAC) **median RS20 vs `SPY`** | **Leg 3** — settled closes, `auto_adjust=False`, benchmark `SPY` named (`C1`): 07-29 `MU −33.66 · AMAT −37.32 · LRCX −39.45 · KLAC −41.27`, **median −38.38** → 08-12 `MU −1.57 · AMAT −7.74 · LRCX −5.12 · KLAC −9.58`, **median −6.43**. Rose **+31.95pp** but **never crossed zero; all four still negative on the terminal date** ⇒ *"turns positive"* **NOT MET**. **Leg 2** — `data/estimates/` (`eps_trend['+1y'].current`), both readings **post** the fiscal roll (`D574`): MSFT `464.72/23.085 = 20.13` → `492.43/23.553 = 20.91` (**+3.9%**); META `556.71/34.408 = 16.18` → `578.85/33.948 = 17.05` (**+5.4%**) ⇒ the multiple **EXPANDED**, *"compresses"* **NOT MET**. **Leg 1** — body-read, `--scope foreign`: META *"narrowed its expectations for 2026 capital expenditures"* [barrons via yahoo_finance 2026-07-30] under a headline reading *"CapEx Boost"*; MSFT *"Lower-Than-Expected Q4 Capex"* [yahoo_finance 2026-07-29] = a **consensus** column, not the **guide-direction** column the row froze (`C3`) ⇒ neither a documented raise nor a documented cut | ★ **`A-RULED-OUT · B/C AMBIGUOUS`** — **branch A is dead on the two MEASURED legs alone**, independent of the categorical leg, so the row's high-information claim (*"Info Tech's single N label is wrong on BOTH halves at once; IT must be split"*) **did NOT fire**. B and C are separated only by the unresolvable capex leg; widening *"narrowed"* / *"lower-than-expected"* into *"raised"* / *"cut"* is exactly what `D242` forbids. Recorded in the **`S31` `AMBIGUOUS` class — 3rd instance**, and `D556`'s **2nd** instance (price legs scored cleanly, non-price leg unretrievable). ⚠ **This says nothing about whether IT should be split** — it says the registered test produced no answer on two of three legs. `D566` unaffected. **41 days past settle; found only by the `D551` re-scan** (`M1452`, `M1453`) |

### Rows on today's settle cell that this run did **NOT** score, and the reason is structural

| row | settle | why not scored |
|---|---|---|
| `S127` · `S140` · `P122` · `P123` | **2026-09-08** | 🚨 **the `industry_US` runtime fires at 09:00 ET, BEFORE the US open** ⇒ every one of these terminates on a close that had not happened. Registered as **`D572`**. They are the **09-09 run's** to score |
| `P128` | **2026-09-08** | same, plus FRED has not published 09-08 `hy_oas` |
| `P121` · `P114` · `P125` | *first `[FRED]` close covering 2026-09-04* | **blocked 5 consecutive runs** by `D427` (H.15 split publication + federal holiday). **Today is the first business day after the holiday** ⇒ handed forward to **MACRO in this run** with an obligation to report **either way** |

★ **Bounded, not scored** (`D531` discipline — an interim line that reads like a verdict is the
defect): `P122` branch **B** requires a `CL=F` settled close **≤ 80.00** on or before 09-08. Settled
closes since the registration state: **08-31 85.76 · 09-01 90.22 · 09-02 91.01 · 09-03 91.30 ·
09-04 91.48** (window min **85.76**). B therefore requires a **−12.55% single-session close** on
09-08. **Arithmetically all-but-closed; formally still open.**
★ **`P122` branch A carries a NEW defect form** (`D573`): its `CL=F` price leg settles at the 09-08
close but its `[COT]` positioning leg for 09-08 **does not publish until ~09-11** — a row can be
past-settle and unscoreable at the same time without anything being broken.

### Dated settle queue, updated by this run

| rows | date |
|---|---|
| `S127` · `S140` · `P122`(B decidable; A waits on COT) · `P123` · `P128` | **2026-09-08** — ⚠ **scoreable from the 2026-09-09 run** (`D572`) |
| `S128` · `S129` · `S136` · `S137` · `P102` · `P126` · `S58-KR` | 2026-09-09 |
| `S130` · `P127` | **2026-09-10** *(US Aug PPI ∧ KOSPI200 quad witching — still unbracketed, `D533`)* |
| `P122`-A `[COT]` leg | ~2026-09-11 *(CFTC release for the 09-08 reference date)* |


---

## MASTER INDEX — appended 2026-09-08 by the `industry_US` run (PREMORTEM registrations)

| id | owner desk | file | statement | settle | status |
|---|---|---|---|---|---|
| **`P147`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **US Aug PPI 2026-09-10 — is the repricing INFLATION or REAL?** `TIP` − `IEF` **1-session excess**, settled closes, 09-09 close → 09-10 close. **A >= +0.1514%** (p85, inflation) / **B <= -0.1492%** (p15, real). 🚨 **MANDATORY ≤48h bracket** — and it **overturns this desk's four-run `B4` drop of PPI with a measurement**: MACRO §A-2 finds two-thirds of the 5-session 10y move is REAL (+0.08 `DFII10` vs +0.04 `T10YIE`). State at registration **49.2nd pctile = dead centre** | **2026-09-10** | ARMED |
| **`P148`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **FOMC + SEP 2026-09-16 — does the dot plot move the CURVE or only the level?** `IEF` − `SHY` **2-session excess** (slope proxy), 09-15 close → 09-17 close. **A <= -0.3469%** (p15, hawkish/flatten) / **B >= +0.2856%** (p85, dovish/steepen). 🚨 **Discharges `D564`'s live commitment three days early**; last clean pre-CPI opportunity. **Nothing on the board measured the SLOPE and nothing spanned the FOMC date.** ETF-based by design because `D427` has blocked the `[FRED]` legs six runs (`R147`). State **54.0th pctile** | **2026-09-17** | ARMED |

### Dated settle queue — updated by the 2026-09-08 `industry_US` PREMORTEM

| rows | date |
|---|---|
| `S127` · `S140` · `P122`(B decidable) · `P123` · `P128` | **2026-09-08** — ⚠ **scoreable from the 2026-09-09 run** (`D572`) |
| `S128` · `S129` · `S136` · `S137` · `P102` · `P126` · `S58-KR` | 2026-09-09 |
| **`P147`** · `S130` · `P127` | **2026-09-10** *(US Aug PPI ∧ ECB decision ∧ `ORCL`+`ADBE` prints — three binaries on one day, of which `catalyst_calendar` surfaces one: `D562`, `D560`)* |
| `P142` · `S135` · `S142` · `S145` · `P140` | 2026-09-11 |
| `P122`-A `[COT]` leg | ~2026-09-11 *(CFTC release for the 09-08 reference date, `D573`)* |
| `S133` · `S146` · `S148` · `S150` · `P139` · `P143` · **`P145`** · **`P146`** · the 09-07 `TLT` row | 2026-09-14 |
| **`P148`** | **2026-09-17** |
| `P124` | 2026-09-18 *(S&P quarterly rebalance = quad witching — **the rebalance itself is UNBRACKETED, dropped BY DECISION on `B4`**, `D533` 2nd run)* |


---

# Master scoring log + index — rows added by the 2026-09-09 `industry_kr` run

## Scored / settled this run

| id | event date | verdict | observed (frozen as-is) | threshold was | effect on the standing view |
|---|---|---|---|---|---|
| **S58-KR** | **2026-09-09** | **`PENDING` — settles today 24:00 KST, NOT `EXPIRED`** | Pre-open read (08:5x) of `module_disclosure 000660 --days 35`: **no 충칭-subject re-disclosure has printed.** The window carries two OTHER "미확정" filings, both on different rumours: **08-21** 조회공시 답변 (Japan fab, 재공시예정일 **09-18**) and **09-04** 자발적 해명 (subsidiary stake sale / HK IPO, per a 08-05 한국경제 report, 재공시예정일 **2026-12-03**). Anti-signal (i) did **not** fire — 자본변동(증자·합병·분할) **0건** in 35 days; ⚠ stated honestly, 자기주식취득결정·주식소각결정·자기주식처분 **do** exist and are not the enumerated classes. Anti-signal (ii) **not checked** (`C3`) | A = 확정 공시 · B = another 미확정 · C = nothing ⇒ `AMBIGUOUS` | **Scoring handed to the 2026-09-10 run as its #1 job.** Branch rule frozen unchanged. ★ Side-observation recorded but **NOT used as the verdict** (`C4`): the same company filed two other 미확정 responses in the same window and pushed both re-disclosure dates out — so branch B's meaning ("the report ran ahead of the company") is a repeating pattern at this issuer, not a one-off |

⚠ **Two KR rows remain verdict-bearing only in prose/index and still have no master-log row: `S28`, `S33`.**
Unchanged from 2026-09-08; recorded again so the gap stays visible, not silently inherited.
⚠ **`D472` 13th reproduction** — scored rows keep an `ARMED` header; the verdict lives only here.

## Index rows added

| id | owner desk | file | one-line |
|---|---|---|---|
| **S154-KR** | `industry_kr` | `SCENARIOS_KR.md` | Three events land on **2026-09-10** (KR quad witching + semiconductor ETF rebalancing ₩1.3~1.8조 + US Aug PPI) and `catalyst_calendar` knows only the PPI — does the structural flow hit `005930` and `000660` **differently**? Settles **2026-09-11** |
| **S155-KR** | `industry_kr` | `SCENARIOS_KR.md` | 대우건설's real 60-day driver is **domestic public orders (52% of ₩2.4953조)** whose vocabulary is **🔴FADING (5 articles/90d)**, while the narrative the desk attached (**대미투자, 🟡ACCEL 3.58×, 787 articles**) appears in **zero** contracts — is the desk's narrative-first candidate selection systematically picking the wrong axis? Settles **2026-10-09** |


---

# ═══ MASTER SCORING LOG — appended 2026-09-12 by the `industry_US` run (Stage 2 / HANDOVER, transcribed at run end 23:15 KST) ═══

> ⚠ **Transcribed at run END, not inside HANDOVER** — the 14:52 invocation of this date wrote HANDOVER.md
> claiming the verdicts were transcribed and stopped before writing them (`M1352`'s failure mode,
> reproduced exactly; HANDOVER addendum item 1). This block is the receipt. Method: mechanical header
> scan of `SCENARIOS_US.md` + master-index rows + the 09-06/09-07/09-08 queue cells (**`D589`: the queue
> alone dropped 7 of 25 due rows**), then a prose read of every row. Observables recomputed from settled
> closes (`auto_adjust=False`), `[FRED]`, `[COT 09-08]`, `[EDGAR]`. **Thresholds frozen; none moved.**

| id | owner | settle | observable (frozen) | measured | verdict |
|---|---|---|---|---|---|
| **`S127`** | US | 09-08 | `AVGO` exc5 vs `SPY`, 09-01→09-08 | **−0.852pp** | **`FIRED-C`** (anti-signal: the 09-10 `AVGO` S-4 is a notes *exchange offer*, not M&A — `D590`) |
| **`S140`** | US | 09-08 | count of 56 IT names with positive exc5 vs `SPY` | **30/56** (trailing-252 median) | **`FIRED-C`** |
| **`P122`** | US | 09-08 | `[COT]` WTI spec 1-yr pctile ≥65 ∧ `CL=F` ≥ 88 / B: any close ≤ 80 | pctile **75**, close **93.03**, window min 82.23 | **`FIRED-A`** |
| **`P123`** | US | 09-08 | `EW{SLB,ETN,NEE,VRT}` − `SMH`, 09-01/02→09-08 | +0.334pp / +0.738pp (both bases) | **`FIRED-C`** |
| **`P128`** | US | 09-08 | `hy_oas` 5-obs change (bp) | 2.65 → 2.67 = **+2 bp** | **`FIRED-C`** |
| **`S128`** | US | 09-09 | `EW{35 reversal}` − `EW{117 decay}`, 5 sessions | **+6.763pp** (`SPY` +0.08%, anti-signal not tripped) | **`FIRED-A`** ★★★ |
| **`S129`** | US | 09-09 | `ADM` exc5 vs `SPY` | **+1.731pp** | **`FIRED-C`** |
| **`S136`** | US | 09-08 | `EW{SLB,MPC,PSX,VLO,COP}` − `EW{XOM,EOG,FANG}`, "5-session sum" | **+4.316pp** (09-01 base) / **+3.165pp** (09-02 base) vs A ≥ +3.90 | 🚨 **`AMBIGUOUS`** — window convention (`D588`) |
| **`S137`** | US | 09-08 | `EW{LITE,COHR}` − `SMH` | +6.578 / +8.072pp vs A ≥ +9 | **`FIRED-C`** |
| **`P102`** | US | 09-09 | `EW{FCX,NEM}` − `EW{10 MATR}`, 10 sessions | **−1.431pp** vs B ≤ +2.505 | **`FIRED-B`** ★ |
| **`P126`** | US | 09-09 | `EW{XOM,CVX,EOG,FANG}` − `EW{MPC,VLO,PSX}` | **−5.085pp** vs B ≤ −4.443 | **`FIRED-B`** |
| **`S130`** | US | 09-10 | `NVDA` filing naming Hugging Face ∧ 10-session exc vs `SPY` | leg 1 **no** (`[EDGAR]`) · leg 2 **−2.499pp** | **`FIRED-C`** |
| **`P127`** | US | 09-10 | `EW{VST,CEG,TLN,NRG,GEV,ETN,PWR}` − `EW{NVDA,AVGO,ANET}` | **+2.27pp** vs A ≥ +4.555 | **`FIRED-C`** |
| **`P147`** | US | 09-10 | `TIP` − `IEF` 1-session (PPI) | **+0.343%** vs A ≥ +0.1514 | **`FIRED-A`** ★★★ (inflation-flavoured print) |
| **`S135`** | US | 09-11 | max pairwise spread of `XLU`/`XLRE`/`XLP` exc5 vs `SPY` | **0.441pp** vs A ≤ 1.50 | **`FIRED-A`** ★★ (the UW trio is ONE bet) |
| **`S142`** | US | 09-11 | `XLF` exc3 vs `SPY` (CPI) | **+0.131pp** | **`FIRED-C`** |
| **`S145`** | US | 09-11 | `EW{STX,WDC,AMD}` − `SMH`, 4 sessions | **+0.227pp** | **`FIRED-C`** |
| **`S149`** | US | 09-11 | `CL=F` 5-session %, 09-04→09-11 | **+9.368%** vs A ≥ +8.343 | **`FIRED-A`** ★★★ |
| **`P137`** | US | 09-11 | `SMH` − `SPY`, 4 sessions | **+1.034pp** | **`FIRED-C`** |
| **`P138`** | US | 09-11 | `^TYX − ^FVX` change (bp), 09-04→09-11 | **69.6 → 56.3 = −13.3 bp** vs B ≤ −5.97 | **`FIRED-B`** ★★★ (Fed path owns the curve) |
| **`P140`** | US | 09-11 | distillate crack `HO×42−CL`, 5-session change | **+9.03 → 108.24** vs B ≥ +8.699 | **`FIRED-B`** ★★ (level reasserted; `L1` lens lost) |
| **`P114`** | US | 09-11 | `XLI` exc5 vs `SPY` | **−0.889pp** | **`FIRED-C`** |
| **`P121`** | US | 09-04+ | `DGS2` ∧ `T10YIE` at the first `[FRED]` close covering 09-04 | 4.37 ∧ 2.35 | **`FIRED-C`** (unblocked by the H.15 lift) |
| **`P125`** | US | 09-04+ | Δ`T10YIE` − Δ`DFII10`, 3-obs, 09-01→09-04 | **+1 bp** | **`FIRED-C`** |
| **`S123`** | US | "09-12" | EW Industrials (50) exc5 vs `SPY`, "09-05 close → 09-12 close" — **both dates are Saturdays** | only admissible window 09-04→09-11: EW INDU −1.726% · `SPY` −0.766% ⇒ **−0.960pp** vs A ≤ −3.10 / B ≥ +0.44 | **`FIRED-C`** (`D588` 2nd instance; caught late — HANDOVER addendum item 2) |
| **`S151-KR`** | KR-owned, scored by US | 09-11 | `069500.KS` O1 = 09-10 vol ÷ 20-session median · O2 = 09-11 retracement ratio | O1 **1.187** (<1.5) · O2 **10.06** (≥0.50) — legs split | **`FIRED-C`** |

**Tally: 26 rows accounted — scored 23 (A 5 · B 4 · C 13 · AMBIGUOUS 1) · blocked 1 (`P142`, H.15 split: `DGS2` ends 09-10 while `T10YIE` carries 09-11; bound +19 bp = A side) · unmeasurable 1 (`P141`, G1) · named-not-scored 1 (`S58-KR`, DART observable — the KR run's; the KR 09-12 run also stopped early, so it is now a TWO-run open item for the next KR run).** Silent skips 0.

### Dated settle queue — rebuilt from the registration files (not from the prior cell — `D589`)
| rows | date |
|---|---|
| `S133` · `S146` · `S148` · `S150` · `P139` · `P143` · `P145` · `P146` · the 09-07 `TLT` row | **2026-09-14** (Muscat route-agreement signing also dated 09-14 `[WebSearch]`, DRIFT addendum) |
| **`P151`** (new) | **2026-09-16** (FOMC) |
| **`P148`** | 2026-09-17 |
| **`P149`** · **`P150`** · **`S156`** (new) · `P124` | **2026-09-18** (quad witching / S&P rebalance — inside all four windows, named, not a voider) |
| `P142` | first `[FRED]` close covering 09-11 (H.15 split) |
| `P141` | when the news index returns (G1) |
| `S58-KR` | KR run — two runs overdue |

---

## MASTER INDEX — appended 2026-09-12 by the `industry_US` run (MACRO + PREMORTEM registrations)

| id | owner desk | file | statement | settle | status |
|---|---|---|---|---|---|
| **`P149`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **The barrel cleared $100 and the equity leg did not follow** — `XLE` 5-session return minus `CL=F` 5-session return (pp), 09-11 close → 09-18 close. **A ≥ +4.69** (p85, convergence) / **B ≤ −5.17** (p15, the equity market keeps discounting $100 as transient). Enters at the 7.9th pctile (inside B). Anti-signal: a ≥3-outlet Hormuz **reopening** statement (pre-declared: a Muscat route agreement excluding US/Israeli flags is NOT one) | 2026-09-18 | ARMED |
| **`P150`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **Health Care's 4-of-32 week — persists or reverts?** EW `us_top300` Health Care (32) 5-session excess vs `SPY`, 09-11 → 09-18. **A ≤ −2.594pp** (p15) / **B ≥ +2.422pp** (p85). ⚠ Reading corrected by PREMORTEM (`M1478`): the week was three idiosyncratic breaks (`AMGN` Lp(a) read-through, `BSX`/`SYK` cyber) — A = "the sympathy drawdown persists", not "rotation"; thresholds untouched | 2026-09-18 | ARMED |
| **`P151`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **FOMC 09-16 LEVEL companion** (`P148`'s slope is already inside A at −0.650%): `SHY` 1-session return 09-15 close → 09-16 close. **A ≤ −0.236%** (p05, hawkish beyond consensus) / **B ≥ +0.134%** (p95, dovish surprise) / C = "hike delivered, nothing learned". Thresholds inside `SHY`'s ±0.7% 6-session straddle — pre-declared history-graded, not a trigger | 2026-09-16 | ARMED |
| **`S156`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **The crack after the record**: distillate crack `HO×42−CL` 5-session change, 09-11 (108.24) → 09-18. **A ≤ −4.25 $/bbl** (p15, collapses — the Hormuz against-us branch measured, not voided) / **B ≥ +8.70** (p85, scarcity extends). Enters at the 81st pctile (leaning B) | 2026-09-18 | ARMED |


---

# ═══ MASTER SCORING LOG — appended 2026-09-13 by the `industry_kr` run (Stage 2 / HANDOVER, transcribed at run end) ═══

> Method: mechanical header scan of `SCENARIOS_KR.md` + master-index rows + the 09-12 US queue cell. ⚠ The
> scan **missed `S58-KR`** (the 09-09 PENDING row's threshold cell carried the token `AMBIGUOUS`) — caught by
> reading the 09-12 queue (`D594`, `D582` 3rd form). Thresholds frozen; none moved.

| id | owner | settle | observable (frozen) | measured | verdict |
|---|---|---|---|---|---|
| **`S58-KR`** | KR | 09-09 (**2 runs late** — 09-10 had no KR run, 09-12 stopped after PREFLIGHT; the delay is logged as a process failure) | Type of 000660 follow-up filing printed on DART by the company's own re-disclosure date | **09-09 조회공시요구에대한답변(미확정)**, rcept 20260909800559, subject **충칭 packaging stake sale (₩4조)**, body: *"확정된 사항은 없습니다 … 3개월 이내 재공시"*, 재공시예정일 **2026-12-08**. Anti-signal (i) 자본변동 0/40d ✅ (자기주식·소각 exist, not enumerated classes) · (ii) 수출통제 EO `[unchecked]` (G1) | **`FIRED-B`** — "another 미확정"; per registration **not a kill** (`R63`), meaning = the report ran ahead of the company, **now on a 3-month roll**. No re-registration (`D343`); §3b 000660 re-check 12-08 |
| **`S154-KR`** | KR | 09-11 | O1 = `069500.KS` 09-10 volume ÷ 20-session median · O2 = 005930−000660 09-10 return spread | **O1 1.187×** (< 2.0; 09-09 1.191 · 09-11 1.244) · O2 **−0.02pp** | **`FIRED-C`** — `AMBIGUOUS`, band not widened. Matches `M1473` (US 09-12) by independent recomputation. Anti-signal (i) `[unchecked]` (G1) · (ii) expiry not moved ✅. ★ Registration finding (`D597`): the 1.3~1.8조 rebalance **did occur** (`[WebSearch]`: 삼전닉스 ~1.32조 sold, 소부장 +5~10%) but through **KRX 반도체 index ETFs**, not `069500.KS` — the observable measured the wrong vehicle. Not re-registered on KR; US `P149`/`P150`/`S156` own the 09-18 window |

**Also settled this run (propositions, not brackets):** `M-138` **`VOID`** (anti-signal ③ fired: aligned `wflow` −0.047 vs the registered 0.095±0.05; (b) leg — 7 positive-`eqflow` sectors ≥ 6 — met simultaneously, recorded as side-observation) · `M-137` closed (c) via `S154-KR`. `M-141` (a) endpoint met (run 1/3). `M-143` registered (MACRO §E).

⚠ **Two KR rows remain verdict-bearing only in prose/index and still have no master-log row: `S28`, `S33`.** ⚠ `D472` **15th reproduction** — scored rows keep an `ARMED` header; the verdict lives here.

### Dated settle queue — rebuilt from the registration files (`D589`), KR rows
| rows | date |
|---|---|
| **`S61-KR`** (BoK Aug export-price MoM, 원화) | **~2026-09-14** (pattern date, not ✓) — next KR run's #1 |
| `S62-KR` | 2026-09-15 |
| `S64-KR` · `S65-KR` · `S68-KR` | 2026-09-19 |
| `S45` · `S54-KR` · `S153-KR` | 2026-09-30 |
| `S155-KR` | 2026-10-09 |
| `S60-KR` · `S49-KR` · `S34` · `S53-KR` · `S59-KR` | 10-12 ~ 11-04 |
| event-conditional `S39` · `S43` · `S44` | bench ≤ −3% session — 09-11 was −1.76% (`^KS11`) / −2.11% (`069500.KS`): checked, not fired |

## MASTER INDEX — appended 2026-09-13 by the `industry_kr` run
**New bracket registrations: 0 — deliberately.** `S58-KR`-B's natural follow-on (same observable, 12-08) would be
registration inflation (`D343`); the 09-18 S&P/quad-witching window is already held by three US rows; the KR
09-16 FOMC read is owned by proposition `M-143` (price + KIS observable, MACRO §E), whose thresholds are declared
hand-set (`C5`) because KR has no implied-move instrument.



---

# ═══ MASTER SCORING LOG — appended 2026-09-14 by the `industry_US` run (Stage 2 / HANDOVER; transcribed at run end ~14:5x KST) ═══

> **Rows scored this run: 0.** Run start 13:16 KST Monday = 00:16 ET; the last settled US close is Fri 09-11, which
> the 09-12 run scored in full (26 rows). No US close printed between the two runs ⇒ no past-dated row existed.
> Partial 4-of-5-session readings for `P136`/`P139`/`P145` were recorded as **bounds, not verdicts** (`D531`,
> HANDOVER §3b). Method: mechanical header scan of `SCENARIOS_US.md` + master-index rows + **all** prior queue cells
> (the 09-12 cell had dropped `P111`, `P136`, `S147` — `D589` third reproduction).

| id | owner | settle | status this run |
|---|---|---|---|
| `P142` | US | first `[FRED]` close covering 09-11 | **BLOCKED, unchanged** — `DGS2` ends 09-10 (4.56), `T10YIE` 09-11; bound +19 bp (A side); no unblock forecast (`R147`) |
| `P141` | US | 09-08 falsifier | **UNMEASURABLE** — remote index dead 13:19 → 14:3x; the local 09-13 pull has no base window (not the registered observable); carried, not EXPIRED |
| `S61-KR` | KR | ~09-14 (BoK export price) | named, not scored — KR feed, the in-flight KR run's (`W1`) |

### Dated settle queue — rebuilt from the registration files + every prior cell (`D589`: the union, not the newest cell)
| rows | date |
|---|---|
| **`S133` · `S146` · `S147` · `S148` · `S150` · `S152` · `P111` · `P136` · `P139` · `P143` · `P145` · `P146`** (13 incl. `P148` below; `P111`/`P136`/`S147` were missing from the 09-11/09-12 cells) | **2026-09-14 close** — the next US run scores all thirteen |
| `P151` | 2026-09-16 (FOMC) |
| `P148` | 2026-09-17 |
| `P149` · `P150` · `S156` · `P124` · **`P155`** (new) | 2026-09-18 (quad witching / S&P + Nasdaq-100 rebalance; BoJ decision Fri 09-18 JST inside the US 09-18 session) |
| **`P152` · `P153` · `P154` · `P156`** (new) | 2026-09-21 |
| `S37` · `S40` · `S48` · `S122` | 2026-09-30 |
| `P142` | first `[FRED]` close covering 09-11 |
| `P141` | when the news index returns with a base window |
| `S8` | `[blank]` — 45th run; human VOID/re-registration |

**Ledgers this HANDOVER**: rejection 324 / due 14 / resolved 5 (`XOM` 09-07 **revived**; `FN` `GEV` `PWR` `LLY` reaffirmed); missed 367 / due 26 / resolved 23 (**9 condition-MET rows closed `expired`-with-MET-note — `D605`**: `MSTR` `LITE` `DASH` `SLB` `COP` `XOM` `FANG` `VLO` `CTVA`; 14 reaffirmed). Legacy 0/0, 23rd run.

## MASTER INDEX — appended 2026-09-14 by the `industry_US` run (MACRO §D + PREMORTEM §3 registrations)

| id | owner desk | file | statement | settle | status |
|---|---|---|---|---|---|
| **`P152`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **The second chokepoint → the freight leg**: `EW{FRO,DHT,INSW,STNG,TNK}` 5-session excess vs `SPY`, 09-14 → 09-21. **A ≥ +6.240pp** / **B ≤ −4.308pp**. State 91.7th pctile ⇒ B informative. Anti-signal: ≥3-outlet "East-West reopened AND Bab el-Mandeb transit restored" | 2026-09-21 | ARMED |
| **`P153`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **The yen after the positioning flip**: `FXY` 5-session %, 09-14 → 09-21 (BoJ Fri 09-18 JST inside). **A ≥ +0.855%** / **B ≤ −1.059%**. State 89.3rd pctile ⇒ B informative | 2026-09-21 | ARMED |
| **`P154`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **Carry unwind → US equities?** `QQQ − SPY` 2-session excess, 09-17 → 09-21. **A ≤ −0.632pp** (NDX lags) / **B ≥ +0.772pp**. Pairs with `P153` | 2026-09-21 | ARMED |
| **`P155`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **Nasdaq-100 funding sale for SpaceX**: `EW{NVDA,AVGO} − SPY` 1-session, 09-17 → 09-18 (companion 09-18 → 09-21 reported). **A ≤ −1.932pp** / **B ≥ +1.584pp** | 2026-09-18 | ARMED |
| **`P156`** | `industry_US` | [`SCENARIOS_US.md`](SCENARIOS_US.md) | **The barrel's own sign** (disambiguates `P149`-A): `CL=F` 5-session %, 09-14 → 09-21. **A ≥ +8.764%** / **B ≤ −5.734%** (de-escalation). State +9.58% on the prior window ⇒ B informative | 2026-09-21 | ARMED |


# ═══ MASTER SCORING LOG — appended 2026-09-14 by the `industry_kr` run (Stage 2 / HANDOVER, transcribed at run end 14:3x KST) ═══

> Method: mechanical header scan of `SCENARIOS_KR.md` + `SCENARIOS_US.md` + master index rows (tokens counted in the verdict column only, `D594`) + the 09-12 US transcription table (`D589` cross-check). Observables recomputed from settled closes (`auto_adjust=False`). **Thresholds frozen; none moved.**

| id | owner | settle | observable (frozen) | measured | verdict |
|---|---|---|---|---|---|
| **`S125`** | US (**scored by KR** — missing from the US 09-12 26-row table, header still `ARMED`) | 09-11 | `ADM` 5-session excess vs `XLP`, 09-03 → 09-11 close | ADM +2.773% / XLP −2.205% = **+4.978pp** vs A ≥ +0.602 | **`FIRED-A`** ★ (registration declared A informative; anti-signal US–Canada ag deal / ADM corporate action `[unchecked-thin]`) |
| **`S61-KR`** | KR | ~09-14 (pattern estimate) | BoK Aug export-price MoM (KRW) | **not released by 13:xx 09-14** — 7 domestic hits all previews ("this week") | **pending — not `EXPIRED`** (date was declared an estimate); KR run #1 item until printed |
| `S62-KR` | KR | 09-15 | US primary document naming Korea on transshipment | D-1 state: `불법환적` KR 0/4 (0.00×) · default 0/2 · `환적` default 3/39 (0.54×), KR index 0 (2-char); no document | not due — B's second leg met on today's values (thin denominator noted) |

**Tally**: 1 scored (A) · 1 pending-not-expired · 0 EXPIRED · 0 silent skips. Event-conditional residue = **0** (S39/S43/S44 were closed 08-08 or earlier — the 09-13 HANDOVER carried them as open; corrected here). US rows settling 09-14 (`S133`·`S146`·`S147`·`S148`·`S150`·`P139`·`P143`·`P145`·`P146`) are not due until the US 09-14 close.

## MASTER INDEX — appended 2026-09-14 by the `industry_kr` run

| id | owner | file | question / observable | settle | status |
|---|---|---|---|---|---|
| **`S158-KR`** | `industry_kr` | `SCENARIOS_KR.md` | **Is the 09-14 insurance "hold" a rate-axis rotation or a low-beta artifact of a −2.6% session?** 11-name insurance EW (동양생명 excluded, trading halted since 08-28) 3-settled-session cumulative return − `^KS11`, 09-11 close base. A ≥ +3.0pp ∧ ≥1 bench-up day with positive excess ∧ big-3 (032830·000810·005830) foreign+institution net > 0 / B ≤ −3.0pp or every bench-up day lost / C between | **2026-09-16 close** (scored by the 09-17 run; final 09-19) | ARMED |

**Next due**: `S62-KR` 09-15 · `S61-KR` (BoK print) · `S158-KR` 09-16 · `S64-KR`·`S65-KR`·`S68-KR` 09-19.
