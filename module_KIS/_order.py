# FILE: research_Mvp/module_kis/_order.py
"""국내주식 현금 매수/매도 주문 (휴먼 트리거 전용).

엔드포인트: POST /uapi/domestic-stock/v1/trading/order-cash
tr_id:      매수 TTTC0802U / 매도 TTTC0801U (모의 VTTC0802U / VTTC0801U)

⚠️ **안전 설계 — 자동매매 아님.**
   - `place_order(..., execute=False)` 가 기본 = 드라이런(미리보기). 네트워크로 주문 안 나감.
   - 실제 발사는 호출부가 명시적으로 `execute=True` 를 줄 때만. CLI 는 `--execute` 플래그.
   - 즉 '트리거'는 항상 사람이 당긴다. 이 모듈은 어떤 스케줄러/루프에서도 자동 호출되지 않도록
     기본값을 막아둔 도구일 뿐이다.
   - 주문 전 수량/단가/잔고 sanity 체크. 정정/취소/예약주문은 의도적으로 미포함.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Optional

from ._account import fetch_balance
from ._auth import KisConfig, KisError, load_config
from ._client import kis_post, make_hashkey
from ._parse import norm_code
from ._quote import fetch_quote

_PATH = "/uapi/domestic-stock/v1/trading/order-cash"
# (env, side) → tr_id
_TR_ID = {
    ("prod", "buy"): "TTTC0802U",
    ("prod", "sell"): "TTTC0801U",
    ("vps", "buy"): "VTTC0802U",
    ("vps", "sell"): "VTTC0801U",
}


@dataclass
class OrderPreview:
    side: str             # buy | sell
    code: str
    qty: int
    price: int            # 지정가(시장가면 0)
    market: bool
    env: str
    tr_id: str
    est_value: Optional[int] = None   # 예상 체결금액(지정가 기준)
    body: dict = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    executed: bool = False            # 드라이런이면 False


@dataclass
class OrderResult:
    side: str
    code: str
    qty: int
    price: int
    env: str
    order_no: Optional[str] = None    # ODNO 주문번호
    org_no: Optional[str] = None      # KRX_FWDG_ORD_ORGNO
    order_time: Optional[str] = None  # ORD_TMD
    message: Optional[str] = None
    executed: bool = True


def _build_body(cfg: KisConfig, side: str, code: str, qty: int,
                price: int, market: bool) -> dict:
    return {
        "CANO": cfg.cano,
        "ACNT_PRDT_CD": cfg.acnt_prdt_cd,
        "PDNO": code,
        "ORD_DVSN": "01" if market else "00",  # 01 시장가 / 00 지정가
        "ORD_QTY": str(int(qty)),
        "ORD_UNPR": "0" if market else str(int(price)),
    }


def place_order(
    side: str,
    code: str,
    qty: int,
    price: Optional[int] = None,
    *,
    market: bool = False,
    execute: bool = False,
    skip_checks: bool = False,
    cfg: Optional[KisConfig] = None,
):
    """현금 주문. 기본은 드라이런(미리보기). execute=True 일 때만 실제 발사.

    Args:
        side: "buy" | "sell".
        code: 6자리 종목코드.
        qty: 주문 수량(>0).
        price: 지정가(원). market=True 면 무시.
        market: True 면 시장가.
        execute: True 라야 실제 주문 전송. 기본 False(드라이런).
        skip_checks: 잔고/시세 sanity 체크 생략(빠른 발사용).

    Returns:
        OrderPreview(execute=False) 또는 OrderResult(execute=True).

    Raises:
        KisError / ValueError: 검증 실패 또는 주문 전송 실패.
    """
    side = side.lower().strip()
    if side not in ("buy", "sell"):
        raise ValueError("side 는 'buy' 또는 'sell' 이어야 합니다.")
    cfg = cfg or load_config()
    cfg.require_account()
    code = norm_code(code)
    qty = int(qty)
    if qty <= 0:
        raise ValueError("주문 수량(qty)은 1 이상이어야 합니다.")
    if not market:
        if price is None or int(price) <= 0:
            raise ValueError("지정가 주문은 price(>0)가 필요합니다. 시장가는 --market.")
        price = int(price)
    else:
        price = 0

    tr_id = _TR_ID[(cfg.env, side)]
    body = _build_body(cfg, side, code, qty, price, market)
    est_value = (qty * price) if (not market and price) else None

    warnings: list[str] = []
    if not skip_checks:
        warnings = _sanity_checks(cfg, side, code, qty, price, market, est_value)

    if not execute:
        # 드라이런 — 주문 전송 없음.
        warnings.insert(0, "DRY-RUN: 실제 주문이 전송되지 않았습니다. 발사하려면 execute=True (CLI --execute).")
        return OrderPreview(
            side=side, code=code, qty=qty, price=price, market=market,
            env=cfg.env, tr_id=tr_id, est_value=est_value, body=body,
            warnings=warnings, executed=False,
        )

    # ── 실제 발사 (호출부가 execute=True 를 명시했을 때만 도달) ──
    hashkey = make_hashkey(body, cfg=cfg)
    resp = kis_post(_PATH, tr_id, body, cfg=cfg, hashkey=hashkey)
    out = resp.get("output") or {}
    return OrderResult(
        side=side, code=code, qty=qty, price=price, env=cfg.env,
        order_no=(out.get("ODNO") or "").strip() or None,
        org_no=(out.get("KRX_FWDG_ORD_ORGNO") or "").strip() or None,
        order_time=(out.get("ORD_TMD") or "").strip() or None,
        message=resp.get("msg1"),
        executed=True,
    )


def _sanity_checks(cfg, side, code, qty, price, market, est_value) -> list[str]:
    """주문 전 가벼운 정합성 점검(실패해도 차단하진 않고 경고만)."""
    warns: list[str] = []
    if cfg.env == "prod":
        warns.append("⚠️ 실전(prod) 계좌 — 실제 체결 시 실제 손익이 발생합니다.")
    try:
        q = fetch_quote(code, cfg=cfg)
        if q.price:
            if not market and price:
                gap = (price / q.price - 1) * 100
                if abs(gap) >= 10:
                    warns.append(
                        f"지정가 {price:,}원이 현재가 {q.price:,.0f}원과 {gap:+.1f}% 차이 — 오타 점검."
                    )
            if q.upper_limit and price and price > q.upper_limit:
                warns.append(f"지정가가 상한가({q.upper_limit:,.0f}) 초과 — 거부될 수 있음.")
            if q.lower_limit and price and 0 < price < q.lower_limit:
                warns.append(f"지정가가 하한가({q.lower_limit:,.0f}) 미만 — 거부될 수 있음.")
        if q.status_code and q.status_code != "55":
            lbl = q.status_label() or q.status_code
            warns.append(f"종목상태 '{lbl}' — 거래 제약 가능.")
    except KisError:
        warns.append("시세 조회 실패 — 단가 sanity 점검 생략.")

    if side == "buy" and est_value:
        try:
            bal = fetch_balance(cfg=cfg)
            if bal.deposit is not None and est_value > bal.deposit:
                warns.append(
                    f"예상 체결금액 {est_value:,}원 > 예수금 {bal.deposit:,}원 — 잔고 부족 가능."
                )
        except KisError:
            pass
    return warns


def to_dict(obj) -> dict:
    return asdict(obj)
