# FILE: module_order_desk/_decisions.py
"""'만약에' 반사실(counterfactual) 결정 추적기 — 최근 매매.

매 체결을 기록하고, 각 결정의 "안 했더라면" 대비 차액을 현재가로 계산한다.
전체 평행 포트폴리오를 시뮬레이션하지 않고 결정별 알파만 본다(가볍고 정확):

  매수 결정: 안 샀으면 현금 보유 → 결정손익 = (현재가 - 매수가) × 수량
  매도 결정: 안 팔았으면 계속 보유 → 결정손익 = (매도가 - 현재가) × 수량

양수면 '잘한 선택', 음수면 '아무것도 안 하느니만 못한 선택'.
저장은 out/order_desk/kis_decisions.json, 최근 MAX_KEEP개만 유지.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG = REPO_ROOT / "out" / "order_desk" / "kis_decisions.json"
# 보관·평가할 최근 결정 수. 50까지 쾌적(현재가는 종목별 1회만 조회 → 고유 종목 수가 실제 비용).
# 너무 옛 거래는 '타이밍 판단'이 아니라 '보유 수익 전체'를 재므로 30 권장.
MAX_KEEP = 30


def load_decisions(path: Path = LOG) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def log_decision(market: str, side: str, code: str, name: Optional[str],
                 qty: int, price: float, currency: str, *,
                 ts: Optional[str] = None, path: Path = LOG) -> None:
    """체결된 결정을 기록하고 최근 MAX_KEEP개로 자른다."""
    rec = {
        "ts": ts or datetime.now().strftime("%Y-%m-%d %H:%M"),
        "market": market,          # "kr" | "us"
        "side": side,              # "buy" | "sell"
        "code": code,
        "name": name or code,
        "qty": int(qty),
        "price": float(price),     # 체결 단가
        "currency": currency,      # "KRW" | "USD"
    }
    recs = load_decisions(path)
    recs.append(rec)
    recs = recs[-MAX_KEEP:]
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(recs, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass


def evaluate(records: list[dict], price_fn) -> dict:
    """각 결정의 반사실 차액을 현재가로 계산.

    price_fn(market, code) -> 현재가(float) 또는 None.
    반환: {"rows": [...최신순...], "summary": {...}}
    """
    # 현재가는 (시장,종목)별 1회만 — 같은 종목 반복 매매해도 조회는 고유 종목 수만큼.
    price_cache: dict = {}

    def cached_price(market, code):
        key = (market, code)
        if key not in price_cache:
            try:
                price_cache[key] = price_fn(market, code)
            except Exception:
                price_cache[key] = None
        return price_cache[key]

    rows: list[dict] = []
    for r in records:
        cur = cached_price(r["market"], r["code"])
        row = dict(r)
        row["cur"] = cur
        if cur and r.get("price"):
            qty, p = r["qty"], r["price"]
            if r["side"] == "buy":
                delta = (cur - p) * qty          # 안 샀으면 현금 보유 대비
                pct = (cur / p - 1) * 100
                row["verdict"] = "잘 삼" if delta >= 0 else "아쉬움"
            else:  # sell
                delta = (p - cur) * qty          # 안 팔았으면 보유 대비
                pct = (p / cur - 1) * 100 if cur else 0
                row["verdict"] = "잘 팖" if delta >= 0 else "아쉬움"
            row["delta"] = round(delta, 2)
            row["pct"] = round(pct, 2)
        else:
            row["delta"] = None
            row["pct"] = None
            row["verdict"] = "시세없음"
        rows.append(row)

    rows.reverse()  # 최신순

    good = sum(1 for r in rows if r["delta"] is not None and r["delta"] >= 0)
    rated = sum(1 for r in rows if r["delta"] is not None)
    krw = sum(r["delta"] for r in rows if r["delta"] is not None and r["currency"] == "KRW")
    usd = sum(r["delta"] for r in rows if r["delta"] is not None and r["currency"] == "USD")
    summary = {
        "n": len(rows), "rated": rated, "good": good,
        "krw_total": round(krw, 0), "usd_total": round(usd, 2),
        "hit_rate": round(good / rated * 100, 0) if rated else None,
    }
    return {"rows": rows, "summary": summary}


def portfolio_branches(rows: list[dict], actual_total_krw: Optional[float],
                       usd_rate: Optional[float] = None) -> dict:
    """매 선택마다 '그 선택을 안 했다면 포트폴리오 전체가 얼마였을까'를 계산.

    포트폴리오 가치는 각 매매에 선형 → 한 선택을 빼면 그 선택이 더한 값(delta)만큼만 변한다.
    그 선택 안 한 분기 = 실제 총자산 − delta(원화환산). 전부 안 한 분기 = 실제 − Σdelta.

    evaluate()의 rows(결정별 delta) + 실제 라이브 총자산 + USD환율을 받아
    분기별 포트폴리오 총액을 만든다(추가 시세조회 없음).
    """
    branches: list[dict] = []
    total_contrib = 0.0
    contrib_known = True
    for r in rows:
        d = r.get("delta")
        if d is None:
            dk = None
        elif r["currency"] == "USD":
            dk = d * usd_rate if usd_rate else None
        else:
            dk = float(d)
        if dk is None:
            contrib_known = False
        else:
            total_contrib += dk
        without = (round(actual_total_krw - dk)
                   if (actual_total_krw is not None and dk is not None) else None)
        branches.append({**r, "delta_krw": (round(dk) if dk is not None else None),
                         "without_total": without})

    no_trade = (round(actual_total_krw - total_contrib)
                if (actual_total_krw is not None and contrib_known) else None)
    return {
        "actual_total": (round(actual_total_krw) if actual_total_krw is not None else None),
        "no_trade_total": no_trade,
        "my_contribution": round(total_contrib) if contrib_known else None,
        "branches": branches,
    }


def rollup_by_ticker(rows: list[dict]) -> dict:
    """evaluate()의 결정별 rows → 종목별 '단타 vs 홀드' 집계.

    핵심: 한 종목의 (단타결과 − 홀드결과) = Σ 매도 qty×(매도가 − 현재가).
    매수비용은 두 시나리오에서 동일해 상쇄 → 매도 행의 delta 합이 곧 단타-홀드 차.
    (sell 행의 delta = (매도가 − 현재가)×수량 이므로 그대로 누적하면 됨)
    """
    groups: dict = {}
    for r in rows:
        key = (r["market"], r["code"])
        g = groups.setdefault(key, {
            "name": r["name"], "currency": r["currency"], "cur": r.get("cur"),
            "n_buy": 0, "n_sell": 0, "buy_qty": 0, "sell_qty": 0,
            "tvh": 0.0, "has_price": r.get("cur") is not None,
        })
        if r.get("cur") is None:
            g["has_price"] = False
        if r["side"] == "buy":
            g["n_buy"] += 1
            g["buy_qty"] += r["qty"]
        else:
            g["n_sell"] += 1
            g["sell_qty"] += r["qty"]
            if r["delta"] is not None:
                g["tvh"] += r["delta"]   # = (매도가 − 현재가)×수량

    out: list[dict] = []
    for (market, code), g in groups.items():
        if g["n_sell"] == 0:
            verdict = "홀드중"           # 매도 없음 → 비교 대상 없음(아직 보유)
            tvh = None
        elif not g["has_price"]:
            verdict, tvh = "시세없음", None
        else:
            tvh = round(g["tvh"], 2)
            verdict = "단타 승" if tvh >= 0 else "홀드 승"
        out.append({
            "market": market, "code": code, "name": g["name"],
            "currency": g["currency"], "cur": g["cur"],
            "n_buy": g["n_buy"], "n_sell": g["n_sell"],
            "buy_qty": g["buy_qty"], "sell_qty": g["sell_qty"],
            "trade_vs_hold": tvh, "verdict": verdict,
        })
    out.sort(key=lambda x: (x["n_sell"] > 0, abs(x["trade_vs_hold"] or 0)), reverse=True)

    krw = sum(r["trade_vs_hold"] for r in out
              if r["trade_vs_hold"] is not None and r["currency"] == "KRW")
    usd = sum(r["trade_vs_hold"] for r in out
              if r["trade_vs_hold"] is not None and r["currency"] == "USD")
    daytrade_wins = sum(1 for r in out if r["verdict"] == "단타 승")
    hold_wins = sum(1 for r in out if r["verdict"] == "홀드 승")
    return {
        "rows": out,
        "summary": {
            "krw_total": round(krw, 0), "usd_total": round(usd, 2),
            "daytrade_wins": daytrade_wins, "hold_wins": hold_wins,
        },
    }
