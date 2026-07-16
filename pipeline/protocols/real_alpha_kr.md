# PROTOCOL — real_alpha_kr (리얼알파 컴퍼니 리서치 · 한국판)

> A protocol = an ordered composition of L1 blocks. **Order is owned by this file.** L1s are referenced only.
> Purpose: for **one KR company**, ask not "should I bet on it?" but **"is this company REAL?"** — forensic
> research where news/narrative is the defendant's statement and verification comes only from primary
> sources (**DART**) and the real movement of money (**투자자수급·KRX 공매도·컨센**). Port of the mvp
> `REAL_ALPHA_COMPANY_RESEARCH_KR.md` v1.1 into this repo's pipeline, reusing existing units (P1).
> Output root `llm_outputs/{YYYY-MM-DD}/real_alpha_kr/{code}/`.

## What this desk is (and is NOT)
- **IS**: a forensic auditor of a single name — product reality + money authenticity + pre-priced set
  difference → a 4-tier verdict with dated, falsifiable observation points that a later run re-grades.
- **IS NOT**: a sizing engine. **참고-only / binding:false** — the verdict informs judgment, it never sizes
  the book. **READ-ONLY**: no order, no stage, no telegram; the only output is files. Not licensed advice.
- **Judgment basis**: numbers come only from ① the STEP-0 datapack or ② a DART original (rcept_no). A
  WebSearch figure is `[WebSearch]`-tagged and never the spine of a decision. **미확보 is a finding.**

## What is REUSED vs NEW (this port added only the missing forensic layer)
> Prose below names stages in plain text on purpose — **only the composition table's links set the run
> order** (the compiler orders L1 by first link appearance).
- **Reused (already in pipeline)**: the deepdive/competitors L2·L3 machinery (valuation/business/disclosure/
  chart/industry_map) is reused inside the new stages; most STEP-0 data ≈ deepdive's calls.
- **New (inserted by this port)**: FORENSIC_PACK · SELF_SCORE · **CHAIN_ALPHA** (analyst-grade value-chain &
  contract alpha — Block A+, replaces the sector-level DEEP for a single name) · MONEY_FORENSIC(+money_trail,
  accruals_check) · SET_DIFF(+set_difference) · FALSIFY · VERDICT · filing_diff · contract_alpha.

## Composition (L1 order)

| # | L1 block | Output |
|---|---|---|
| 0 | [PULSE](../L1_stages/pulse.md) ☆optional-lead | same-day tape sanity if the name is moving hard today |
| 1 | [FORENSIC_PACK](../L1_stages/forensic_pack.md) ★new | `DATAPACK.md` — every number frozen before reasoning (valuation·DART·flow·chart·filing_diff) |
| 2 | [SELF_SCORE](../L1_stages/self_score.md) ★new | prior observation_points graded 적중/기각/미도래 (skip if first research) |
| 3 | [CHAIN_ALPHA](../L1_stages/chain_alpha.md) ★new (Block A+) | analyst-grade value-chain: 마진포착 노드지도·세그먼트 단위이코노믹스·계약 book-to-bill·고객/공급 의존그래프·경쟁 스펙표·미스프라이싱 노드 |
| 4 | [MONEY_FORENSIC](../L1_stages/money_forensic.md) ★new (Block B) | is the money real: accruals(NI↔OCF)·재고/채권·말vs행동 괴리표 |
| 5 | [SET_DIFF](../L1_stages/set_diff.md) ★new (Block C) | ①선반영 vs ②실측 → alpha_delta / risk_unseen |
| 6 | [FALSIFY](../L1_stages/falsify.md) ★new | strongest bear case first → reject/uphold with A/B evidence |
| 7 | [VERDICT](../L1_stages/verdict.md) ★new | REAL / REAL-but-PRICED / INFLATED / BROKEN + delta line + 관측점 + ledger |

## Runtime deltas (vs the reused industry/paper desks)
- **Unit of work = one company, not a sector or a book.** CHAIN_ALPHA (not the sector-level DEEP) maps a
  *single* name's value-chain position, contract backlog, and competitive spec tables at analyst depth.
- **The verdict is forensic, not directional.** Not buy/sell — REAL/PRICED/INFLATED/BROKEN. Sizing is out of scope.
- **The ledger is the point.** VERDICT's dated observation_points are graded by the *next* SELF_SCORE — the
  desk earns trust only through its hit/miss track record (§0 참고-only → binding is a human call after 30d).
- **KR ticker-format trap**: 6-digit for KIS/DART, `.KS/.KQ` for chart/flow, 한글 종목명 for news. Violate → 0 data.

**Start → read [FORENSIC_PACK](../L1_stages/forensic_pack.md) and execute.** Advance only after each EXIT
CHECK passes. Finish at VERDICT (ledger merged) — no downstream stage; this desk ends in files.
