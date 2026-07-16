# -*- coding: utf-8 -*-
"""module_paper_book._mirror — 실제 KIS 장부 ↔ paper book ↔ KIS 주문 데스크 동기화.

세 방향:
  1) INGEST  : 실제 KIS 보유(또는 스크린샷 유래 값)를 paper book 에 '이미 보유'로 시드.
               현금 반영 없이 seed (평단은 이미 매수 완료 상태 → 현금은 별도로 셋).
  2) STAGE   : paper 의 추천/결정을 module_order_desk 의 주문 스택(out/order_desk/kis_stack.json)
               에 intent 카드로 올린다 — 사람이 데스크에서 [체결]로 하나씩 발사(자동 아님, P5).
  3) EPISTEMICS: 판단 근거 축적 — module_epistemics.factor_confidence 로 학습된 민감도를 읽고,
               catalyst 발화 후 update_sensitivity 로 되먹인다(닫힌 루프).

이 파일은 '동기화 기계'일 뿐 — 무엇을 사고팔지는 상위(미러링 프로토콜 DECIDE)가 정한다(P4).
주문은 절대 발사하지 않는다: STAGE 는 intent(계획)만 쓴다.
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from ._book import _now, get_positions
from ._config import ccy_of, market_of


@dataclass
class MirrorPosition:
    ticker: str
    qty: float
    avg_cost: float           # 현지통화 평단
    name: Optional[str] = None
    theme: Optional[str] = None
    stop: Optional[float] = None
    source: str = "KIS-mirror"


def seed_position(conn: sqlite3.Connection, mp: MirrorPosition) -> None:
    """보유 포지션 1건을 현금효과 없이 시드(오프닝 밸런스). 미러링 전용."""
    t = mp.ticker.upper()
    now = _now()
    conn.execute(
        "INSERT OR REPLACE INTO positions(ticker,market,currency,name,qty,avg_cost,"
        "stop,theme,thesis,source_report,opened_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
        (t, market_of(t), ccy_of(t), mp.name, mp.qty, mp.avg_cost, mp.stop,
         mp.theme, f"mirrored from {mp.source}", mp.source, now, now),
    )


def apply_mirror(conn: sqlite3.Connection, positions: list[MirrorPosition],
                 cash_krw: Optional[float] = None, cash_usd: Optional[float] = None,
                 reset_positions: bool = True, note: str = "KIS mirror") -> dict:
    """실제 보유를 paper book 에 반영(이미 보유 상태로 수정).

    reset_positions=True 면 기존 포지션을 비우고(미러가 진실의 원본), 현금 슬리브를
    실제값으로 셋한 뒤 각 보유를 seed. 체결원장은 건드리지 않는다(오프닝 밸런스라 미러
    트랜잭션 1줄만 기록).
    """
    if reset_positions:
        conn.execute("DELETE FROM positions")
    if cash_krw is not None:
        conn.execute("INSERT OR REPLACE INTO cash(currency, amount) VALUES('KRW', ?)", (cash_krw,))
    if cash_usd is not None:
        conn.execute("INSERT OR REPLACE INTO cash(currency, amount) VALUES('USD', ?)", (cash_usd,))
    for mp in positions:
        seed_position(conn, mp)
    conn.execute("INSERT OR REPLACE INTO book_meta(k,v) VALUES('last_mirror', ?)", (_now(),))
    conn.execute("INSERT OR REPLACE INTO book_meta(k,v) VALUES('mirror_note', ?)", (note,))
    return {"mirrored": len(positions), "cash_krw": cash_krw, "cash_usd": cash_usd, "note": note}


def stage_to_kis(intents: list[dict], clear_first: bool = False) -> dict:
    """추천/결정을 module_order_desk 주문 스택에 intent 카드로 올린다(재사용, P1).

    intents: [{market, side, code, qty, price, note}] — make_intent 포맷.
    데스크는 로드 시 각 intent 를 드라이런 카드로 만들고, 사람이 [체결]로 발사한다.
    이 함수는 파일만 쓴다 — 주문 발사는 없다.
    """
    try:
        from module_order_desk import stack as _stack
    except Exception as e:
        return {"ok": False, "error": f"module_order_desk import 실패: {e}"}
    if clear_first:
        _stack.clear()
    existing = _stack.load_staged()
    made = []
    for it in intents:
        made.append(_stack.make_intent(
            market=it["market"], side=it["side"], code=it["code"],
            qty=int(it["qty"]), price=it.get("price"), note=it.get("note", ""),
        ))
    _stack.save_staged(existing + made)
    return {"ok": True, "staged": len(made), "total_in_stack": len(existing) + len(made),
            "path": str(_stack.STACK)}


# ── epistemics 연동(판단 근거 축적) ──────────────────────────────────────────
def learned_sensitivity(ticker: str) -> dict:
    """module_epistemics 민감도 원장에서 학습된 factor 신뢰도를 읽는다(있으면).

    미러링 DECIDE 가 '이 종목이 무엇에 민감한지'의 prior 로 참고. 없으면 빈 dict.
    """
    try:
        from module_epistemics import load_sensitivity
        led = load_sensitivity(ticker)
        return led.get("factors", {}) if isinstance(led, dict) else {}
    except Exception:
        return {}


def record_sensitivity(ticker: str, factor: str, direction: str, event: str,
                       conf: float = 0.6) -> bool:
    """오늘 판단의 근거 factor 를 epistemics 원장에 축적(되먹임 시드)."""
    try:
        from module_epistemics import update_sensitivity
        update_sensitivity(ticker, factor, direction, event, conf)
        return True
    except Exception:
        return False
