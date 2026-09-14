# L1 · BET_VERDICT — the single-name trading verdict, with the gates that must survive it

> Terminal reasoning phase for the company desk. Turns everything upstream into **one** verdict:
> `ENTER · ADD · HOLD · TRIM · EXIT · PASS`, each with a stop, a horizon, and a dated observation
> point. Distinct from [verdict](verdict.md), which renders the forensic 4-tier *"is it REAL?"* on a
> different axis. Calls L3 for the ledger writes. Output: `COMPANY_VERDICT.md` + a ledger row.

## Belief
A verdict that is not written into a scored ledger is an opinion that will never be graded. Every run
of this stage ends with **exactly one** row appended — to [reject_ledger](../L3_functions/reject_ledger.md)
(we held/declined and it could have paid) or to [missed_ledger](../L3_functions/missed_ledger.md) (we
did not buy and it could have paid). PASS with no row is a **failed run**, not a quiet one.

## L3 called
- L3 [reject_ledger](../L3_functions/reject_ledger.md) — PASS/TRIM/EXIT ⇒ a row with a reason class,
  a **`--revives-if`** condition and a recheck date. Both fields are mechanically required.
- L3 [missed_ledger](../L3_functions/missed_ledger.md) — "looked, did not buy" ⇒ **`--enters-if`** + recheck.
- L3 [exposure_state](../L3_functions/exposure_state.md) — the book's cash/exposure state is size context,
  and it is the **single source of the cash target**; this stage never invents one.

## Gates — a verdict must clear every one, and each is written out with its value
| # | Gate | Rule |
|---|---|---|
| **G1** | above-SMA200 | below ⇒ `ENTER`/`ADD` are unavailable (HOLD/TRIM/EXIT/PASS only) |
| **G2** | confirmation | no OBV-alone conviction. Needs an **A-grade** (RS20/RS60) or, for KR, a **B-grade** (KIS per-investor actual) agreeing. A C-grade may never carry it |
| **G3** | catalyst | a dated catalyst must exist, or the name is a value trap ⇒ PASS |
| **G4** | reward/risk | `upside / |downside| ≥ 1.5` against a **written** stop, not a mental one |
| **G5** | opinion-anchoring | the bear case from FALSIFY is quoted verbatim before the verdict line |
| **G6** ★ | **frame gate** (new) | if DRIVER_TEST **D3 FAILED**, the shared leg is sector beta and **may not appear as name-specific evidence**. Cite it as beta or drop it |
| **G7** ★ | **consensus-exceeded** (new) | if price > consensus mean target, a low forward P/E **may not be cited as cheap** unless the **next-year EPS direction** is printed on the same line |
| **G8** ★ | **position conflict** (new) | if the name is **held in the book** and also sits **unresolved in the reject ledger**, the contradiction is resolved *in this file* before any verdict |

### Why G7 and G8 exist (measured 2026-08-21, PSX)
**G7** — the name traded at **$245.51 against a consensus mean target of $221.68 (−9.7% "upside")** on a
**forward P/E of 11.55**, while consensus **next-year EPS sat 15.4% below this year's**. The low multiple
was the *arithmetic of a peak year*, and "cheap forward P/E" was being written without its denominator.
**G8** — the same name was in the book at **+21.3%** *and* carried an **unresolved 2026-08-02 rejection**
(`B.모멘텀only`). Testing that rejection's own `--revives-if` showed it had **not** revived (leg 1 `days21-60
> 0` ✅, leg 2 `FINRA short-vol z < 0` ❌ at **+0.98 and rising**) — so the ledger said *still rejected*
while the book said *held and winning*, and **nothing in any protocol had ever put those two files side by
side.** G8 is that missing read, made mandatory.

## 🚨 Known instrument defect — read before trusting a US ledger score
`scripts/reject_ledger.py score` prices every row off `llm_outputs/sector_flow/prices_kr_*.pkl` against a
**KR** equal-weight benchmark. The ledger is **201 rows, of which 100 are US**, and those 100 score as
`채점불가` — **silently**. Measured: the PSX rejection above was worth **+18.63pp** against SPY and appears
in no class average; the `B.모멘텀only` class currently reads `n=6, −3.1pp` on KR rows alone.
⇒ **When `--market us`, this stage writes its row and states that the row cannot be scored today.**
Do not quote a US class average from that scorer. (Fix = a US price-cache/benchmark path in
`reject_ledger.py::_prices`/`_bench_universe`; `sector_flow --market us` already produces the cache.)

## ✅ EXIT CHECK
- [ ] One verdict line: action · stop (a number) · horizon · size hand-off to SIZE (or `NEEDS_SIZE`).
- [ ] G1–G8 each printed with the value that cleared or failed it — not a checkmark.
- [ ] Exactly one ledger row appended, with `--revives-if` / `--enters-if` **and** a recheck date.
- [ ] ≥1 dated observation point registered for the next run's SELF_SCORE to grade.
- [ ] If `--market us`: the ledger-scoring defect is stated in the file, not assumed known.
