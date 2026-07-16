"""책(한국모의) → 타임폴리오 콘테스트 미러 동기화.

strategy-kr 데스크가 한국모의(book id=6)에 기록한 결정을 콘테스트에 집행한다.
타깃 비중 = 한국모의 포지션의 현재 시가비중(= shares*price / 책 equity).
현재 비중 = 타임폴리오 보유. diff(drift)만큼 매수/매도(주문 비중% = |drift|).

★ 이 계층은 '무엇을'만 결정. 실제 제출 arming(TIMEFOLIO_EXECUTE=1)은 상위에서.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from module_webctl._env import load_dotenv


def _uid() -> int:
    load_dotenv()
    raw = os.environ.get("ADMIN_USER_ID", "").strip()
    if not raw:
        raise RuntimeError(".env 에 ADMIN_USER_ID 필요")
    return int(raw)


def code6(ticker: str) -> str:
    """'067310.KQ' → '067310'."""
    return ticker.split(".")[0].strip().zfill(6)


@dataclass
class TradePlan:
    code: str
    name: str
    side: str          # buy | sell
    order_weight: float  # 주문 비중(%) = |target-current|
    target_w: float
    current_w: float
    reason: str = ""


def book_targets(book_id: int = 6, seed: float = 10_000_000.0) -> dict[str, dict]:
    """한국모의 포지션 → {code6: {name, weight, ticker, value}}. 비중 = value/equity."""
    from alert_bot import alert_db as db
    from alert_bot import price as pr

    uid = _uid()
    rows = db.list_positions(uid, portfolio_id=book_id)
    enriched = []
    unreal = 0.0
    for r in rows:
        tk = r["ticker"]
        try:
            cur = pr.get_price(tk)
        except Exception:
            cur = None
        if cur is None:
            cur = r["avg_price"]
        val = cur * r["shares"]
        unreal += val - r["avg_price"] * r["shares"]
        enriched.append({"ticker": tk, "name": r.get("ticker_name") or tk,
                         "shares": r["shares"], "value": val})
    equity = seed + unreal            # cash + 시가 = seed + 미실현손익
    out = {}
    for e in enriched:
        w = (e["value"] / equity * 100) if equity else 0.0
        out[code6(e["ticker"])] = {"name": e["name"], "weight": round(w, 2),
                                   "ticker": e["ticker"], "value": e["value"]}
    return out


def build_plan(targets: dict[str, dict], holdings: list, *, min_drift: float = 0.5) -> list[TradePlan]:
    """타깃(책) vs 현재(타임폴리오 보유) diff → 매매 계획."""
    current = {h.code: h.weight for h in holdings}
    names = {h.code: h.name for h in holdings}
    plans: list[TradePlan] = []
    for code in sorted(set(targets) | set(current)):
        tgt = targets.get(code, {}).get("weight", 0.0)
        cur = current.get(code, 0.0)
        drift = round(tgt - cur, 2)
        if abs(drift) < min_drift:
            continue
        name = targets.get(code, {}).get("name") or names.get(code, code)
        plans.append(TradePlan(
            code=code, name=name,
            side="buy" if drift > 0 else "sell",
            order_weight=abs(drift), target_w=tgt, current_w=cur,
            reason=("신규/증량" if drift > 0 and cur == 0 else
                    "증량" if drift > 0 else
                    "청산" if tgt == 0 else "감량"),
        ))
    return plans


def sync(tf, *, min_drift: float = 0.5, execute: bool = False,
         shot_dir: Optional[str] = None, book_id: int = 6) -> dict:
    """미러 동기화 실행. tf=Timefolio. execute+arming 없으면 드라이런."""
    targets = book_targets(book_id=book_id)
    holdings = tf.read_holdings()
    plans = build_plan(targets, holdings, min_drift=min_drift)
    results = []
    for i, p in enumerate(plans):
        shot = f"{shot_dir}/tf_order_{p.code}.jpg" if shot_dir else None
        r = tf.place_order(p.code, p.side, p.order_weight, prc_ty="Opp",
                           execute=execute, shot=shot)
        r["reason"] = p.reason; r["target_w"] = p.target_w; r["current_w"] = p.current_w
        r["name"] = p.name
        results.append(r)
    return {"targets": targets, "holdings": [h.__dict__ for h in holdings],
            "plans": [p.__dict__ for p in plans], "results": results}
