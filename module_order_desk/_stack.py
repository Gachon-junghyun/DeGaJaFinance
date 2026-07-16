# FILE: module_order_desk/_stack.py
"""주문 스택 저장/로드 — '계획'을 파일로 두고 데스크가 시작 시 불러온다.

체결이 아니라 '의도(intent)'만 저장: {market, side, code, qty, price, note}.
데스크는 로드 시 각 intent를 드라이런 미리보기 카드로 만든다(실주문 아님).
저장은 out/order_desk/kis_stack.json (커밋 대상 아님 — 개인 계획).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
STACK = REPO_ROOT / "out" / "order_desk" / "kis_stack.json"


def load_staged(path: Path = STACK) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        return []


def save_staged(intents: list[dict], path: Path = STACK) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(intents, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass


def make_intent(market: str, side: str, code: str, qty: int,
                price: Optional[float] = None, note: str = "") -> dict:
    return {"market": market, "side": side, "code": code,
            "qty": int(qty), "price": price, "note": note}


def clear(path: Path = STACK) -> None:
    try:
        path.unlink(missing_ok=True)
    except Exception:
        pass
