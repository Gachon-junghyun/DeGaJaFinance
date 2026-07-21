# ACTION_BRACKET — 2026-07-18  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 10,920,817원 · fx 1380 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** SCHW earnings (D-3, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*

---
---

# ⚠ STAGED DRY-RUN TICKET (hand-assembled 2026-07-18) — what the tool couldn't emit

> Above = `action_bracket.py` verbatim (zero tickets). Below = hand-assembled, clearly marked.
> **No order transmitted. `execute=True` appears nowhere.** Sizing = the risk model + the user's own
> `core_pick` decision, not a recommendation. The trigger is the human's.

## Why the deterministic tool emitted zero (unchanged from 07-17)
1. **CORE-STARTER suppressed** — rank-2 Energy cycle is an unconfigured stub: `min_epicenter_pct = 0.0`
   (→ `epi_pct < 0.0` unsatisfiable, GAP can never fire) **and** `core_pick = None`. The user decided
   **PSX / floor 8%** in this session, but that edit was interrupted before it reached
   `data/cycles/cycle_registry.json`, so the tool still reads the stub.
2. **EARNINGS brackets empty** — nearest binary is SCHW (axis=earnings); `branch_map.json` earnings axis
   is a deliberate placeholder (`confirm-then-enter, no front-run of a single-name binary`). Correct by design.
3. **Oil/Hormuz undated** → the `dated` filter drops it (only fully-populated axis, but open-ended).

## ★ Staged ticket — Energy epicenter core-starter (LIVE `place_us_order(execute=False)` preview)
Produced by calling `module_KIS.place_us_order("buy", "PSX", …, execute=False)` — the same dry-run path
the CLI uses; verified in source that `execute=False` returns the preview **before** `kis_post`, so
**nothing is transmitted**.

| Field | Value | Basis |
|---|---|---|
| Ticker | **PSX** (Phillips 66, NYSE) | ★ user-decided rank-2 `core_pick` this session |
| Quote | **$203.67** | KIS live |
| **Size** | **3 shares** | risk-model raw 4 → **capped to 3 by `buyable`** |
| Notional | **$611.01** | 3 × 203.67 |
| Risk | **$63.32 = 0.8% of book** | core-risk 0.8% / stop 7% (`_size` formula) |
| Stop | **$189.41 (−7%)** | rule |
| tr_id | TTTT1002U (US buy) | — |
| **executed** | **False — not transmitted** | `place_us_order(execute=False)` |
| KIS warnings | `DRY-RUN: 실제 주문 미전송…` · `실전 계좌` · `달러 예수금 $0 → 통합증거금(원화)으로 최대 3주` | from the desk itself |

⚠ **Binding constraint = `buyable` (3 shares), not the risk model (4).** USD cash is $0; US buying power
comes from integrated KRW margin, which tops out at 3 PSX shares right now. Cash is 50% of book, but
**immediate US buying power is the ceiling**, not capital.
⚠ **This US core-starter cannot route through the `--order` CLI** — that CLI is domestic-only
(`domestic-stock/order-cash`, KRW). US goes via `_overseas_order` (`overseas-stock/order`), which is
**not wired into the CLI** — previewed by direct function call.

## Boundary (explicit)
- **No `--execute` / `execute=True` anywhere.** Trade execution is the human's act, per repo convention and my own limits.
- **The 3 shares are not "buy this"** — the risk model's mechanical output on the user's own `core_pick`. Not licensed advice.
- **No sell ticket** — the 07-17 stop-hits (TSM/VST) recovered on 07-17, so the de-risk trigger is no longer firing; and I do not make sell judgments on the user's behalf.

*Hand-assembled analytical artifact. Zero buy/sell advice. Nothing in this file transmits an order.*