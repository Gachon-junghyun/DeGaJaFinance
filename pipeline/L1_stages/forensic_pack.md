# L1 · FORENSIC_PACK — STEP 0 deterministic datapack (stage)

> Phase 0. Freeze every number **before** reasoning, so the write-up cites data, not memory. This is the
> forensic desk's "박제" step: assemble the pack, read it whole, then start the blocks. Calls L2. Output: `DATAPACK.md`.

## Belief
Nothing enters the report that isn't in ① this pack or ② a DART original with its rcept_no. A WebSearch
number gets a `[WebSearch]` tag and is never the spine of a decision. **미확보 is a finding, not a failure.**

## L2 called
- [deepdive](../L2_modules/deepdive.md) — `module_valuation`(현재가·**컨센 목표주가/투자의견**·PER TTM/Fwd·PBR·외인%) ·
  `module_business`(DART 사업보고서 본문: 사업의내용·매출분해·ASP·고객집중) · `module_disclosure --days 120`(공시 digest + red-flags) ·
  `module_chart <code>.KS/.KQ --read` (**풀 그리드 정독** — 요약 tail 말고 `chart_{code}.txt` 본문).
- [money_trail](../L2_modules/money_trail.md) — investor_flow(외/기/개 일별) · insider/treasury/capital(DART) · short%(KRX) · accruals.
- [news](../L2_modules/news.md) — `fts search "<한글명>" --days 30`(velocity 7d/30d + 최근 제목). **검색키=한글 종목명**(티커 0건).
- L3 [filing_diff](../L3_functions/filing_diff.md) — 공시 언어 diff(Lazy Prices), best-effort.

## KR ticker-format trap (violate → 0 data)
| source | format | ex |
|---|---|---|
| KIS·valuation·disclosure·business | 6-digit | `009150` |
| yfinance/chart/flow | `.KS`(코스피)/`.KQ`(코스닥) | `009150.KS` |
| news_fts | 한글 종목명 | `삼성전기` |

## KR data gaps (state explicitly, do not lean on)
No single-stock option flow · insider **trade price 미상**(direction/qty only) · procurement needs `DATA_GO_KR_KEY` ·
per-investor short 미제공. Counter-edge: **per-day foreign/inst net-buy + short balance are KR-only axes — use them.**

## ✅ EXIT CHECK
- [ ] `DATAPACK.md` written; every axis has a status (ok/미확보). Chart full grid read, not just CHART_READ.
- [ ] Consensus target/rating captured (Block C ① seed). Foreign/inst/retail 20d flow captured.
- [ ] prev_research loaded if the ledger has this code (feeds SELF_SCORE). Pack read whole before any block starts.
