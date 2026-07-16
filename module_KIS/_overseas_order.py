# FILE: research_Mvp/module_kis/_overseas_order.py
"""미국주식 현재가 + 매수/매도 주문 (휴먼 트리거 전용).

시세:  GET  /uapi/overseas-price/v1/quotations/price   tr_id HHDFS00000300
주문:  POST /uapi/overseas-stock/v1/trading/order       tr_id 미국 매수 TTTT1002U /
       매도 TTTT1006U (모의 VTTT1002U / VTTT1001U)

거래소 코드가 시세용(EXCD: NAS/NYS/AMS)과 주문용(OVRS_EXCG_CD: NASD/NYSE/AMEX)이
다르다 — KIS 특유의 비대칭. fetch_us_quote 가 NAS→NYS→AMS 순으로 자동 탐색해
둘 다 채워준다.

⚠️ 국내 _order 와 동일한 안전 설계: place_us_order(..., execute=False) 가 기본 드라이런,
   execute=True(사람이 직접) 일 때만 발사. 미국주문 단가는 USD, 시장가 미지원(지정가만).
   주문 파라미터는 KIS 스펙 기준 — 실발사 전 첫 1건은 사용자가 확인 권장.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Optional

from ._auth import KisConfig, KisError, load_config
from ._client import kis_get, kis_post, make_hashkey
from ._parse import to_float

_PRICE_PATH = "/uapi/overseas-price/v1/quotations/price"
_PRICE_TR = "HHDFS00000300"
_PSAMT_PATH = "/uapi/overseas-stock/v1/trading/inquire-psamount"
_PSAMT_TR = "TTTS3007R"   # 해외주식 매수가능금액조회(실전)
_ORDER_PATH = "/uapi/overseas-stock/v1/trading/order"
_ORDER_TR = {
    ("prod", "buy"): "TTTT1002U", ("prod", "sell"): "TTTT1006U",
    ("vps", "buy"): "VTTT1002U", ("vps", "sell"): "VTTT1001U",
}
# (시세 EXCD, 주문 OVRS_EXCG_CD)
_US_MKTS = [("NAS", "NASD"), ("NYS", "NYSE"), ("AMS", "AMEX")]


@dataclass
class UsQuote:
    symbol: str
    excd: str                      # 시세 거래소코드 (NAS/NYS/AMS)
    exchange: str                  # 주문 거래소코드 (NASD/NYSE/AMEX)
    price: Optional[float] = None  # 현재가 (USD)
    prev_close: Optional[float] = None
    change_pct: Optional[float] = None


def fetch_us_quote(symbol: str, exchange: Optional[str] = None,
                   cfg: Optional[KisConfig] = None) -> UsQuote:
    """미국 종목 현재가(USD). 거래소 미지정 시 NAS→NYS→AMS 자동 탐색."""
    cfg = cfg or load_config()
    sym = symbol.upper().strip()
    mkts = _US_MKTS
    if exchange:
        ex = exchange.upper()
        mkts = [m for m in _US_MKTS if ex in m] or _US_MKTS
    for excd, ordc in mkts:
        body = kis_get(_PRICE_PATH, _PRICE_TR,
                       {"AUTH": "", "EXCD": excd, "SYMB": sym}, cfg=cfg)
        o = body.get("output") or {}
        last = to_float(o.get("last"))
        if last:
            return UsQuote(
                symbol=sym, excd=excd, exchange=ordc, price=last,
                prev_close=to_float(o.get("base")),
                change_pct=to_float(o.get("rate")),
            )
    raise KisError(f"미국 종목 '{sym}' 시세를 못 찾음 (NAS/NYS/AMS 모두 0).")


def fetch_us_buyable(exchange: str, price: float, symbol: str,
                     cfg: Optional[KisConfig] = None) -> dict:
    """미국주식 매수가능금액 조회(통합증거금 반영).

    USD 예수금만 보는 게 아니라 원화 매수증거금까지 합산한 실제 주문가능액을 준다.
    반환: {usd_only, buyable(원화포함), max_qty, exrt}.
    """
    cfg = cfg or load_config()
    cfg.require_account()
    body = kis_get(
        _PSAMT_PATH, _PSAMT_TR,
        {"CANO": cfg.cano, "ACNT_PRDT_CD": cfg.acnt_prdt_cd,
         "OVRS_EXCG_CD": exchange, "OVRS_ORD_UNPR": f"{price:.2f}",
         "ITEM_CD": symbol.upper()},
        cfg=cfg,
    )
    o = body.get("output") or {}
    return {
        "usd_only": to_float(o.get("ord_psbl_frcr_amt")),      # 달러만
        "buyable": to_float(o.get("frcr_ord_psbl_amt1")),      # 원화 포함(통합증거금)
        "max_qty": _to_int(o.get("ovrs_max_ord_psbl_qty")),    # 원화 포함 최대주수
        "max_qty_usd": _to_int(o.get("max_ord_psbl_qty")),     # 달러만 최대주수
        "exrt": to_float(o.get("exrt")),
    }


def _to_int(s):
    v = to_float(s)
    return int(v) if v is not None else None


@dataclass
class UsOrderPreview:
    side: str
    symbol: str
    exchange: str           # 주문 거래소코드
    qty: int
    price: float            # 지정가 (USD)
    env: str
    tr_id: str
    est_value_usd: Optional[float] = None
    cur_price: Optional[float] = None
    body: dict = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    executed: bool = False


@dataclass
class UsOrderResult:
    side: str
    symbol: str
    exchange: str
    qty: int
    price: float
    env: str
    order_no: Optional[str] = None
    order_time: Optional[str] = None
    message: Optional[str] = None
    executed: bool = True


def place_us_order(
    side: str,
    symbol: str,
    qty: int,
    price: Optional[float] = None,
    *,
    exchange: Optional[str] = None,
    execute: bool = False,
    skip_checks: bool = False,
    cfg: Optional[KisConfig] = None,
):
    """미국주식 지정가 주문. 기본 드라이런, execute=True 일 때만 실제 전송.

    price 미지정 시 현재가로 미리보기(실발사는 price 명시 권장).
    Returns: UsOrderPreview(execute=False) 또는 UsOrderResult(execute=True).
    """
    side = side.lower().strip()
    if side not in ("buy", "sell"):
        raise ValueError("side 는 'buy' 또는 'sell'.")
    cfg = cfg or load_config()
    cfg.require_account()
    qty = int(qty)
    if qty <= 0:
        raise ValueError("수량(qty)은 1 이상.")

    q = fetch_us_quote(symbol, exchange=exchange, cfg=cfg)
    if price is None:
        price = q.price  # 미리보기용 기본값(현재가)
    price = round(float(price), 2)
    if price <= 0:
        raise ValueError("지정가(USD)가 필요합니다.")

    tr_id = _ORDER_TR[(cfg.env, side)]
    body = {
        "CANO": cfg.cano,
        "ACNT_PRDT_CD": cfg.acnt_prdt_cd,
        "OVRS_EXCG_CD": q.exchange,
        "PDNO": q.symbol,
        "ORD_QTY": str(qty),
        "OVRS_ORD_UNPR": f"{price:.2f}",
        "ORD_SVR_DVSN_CD": "0",
        "ORD_DVSN": "00",  # 지정가
    }
    est = round(qty * price, 2)

    warns: list[str] = []
    if not skip_checks:
        warns = _us_checks(cfg, side, q, qty, price, est)

    if not execute:
        warns.insert(0, "DRY-RUN: 실제 주문 미전송. 발사하려면 execute=True (--execute).")
        return UsOrderPreview(
            side=side, symbol=q.symbol, exchange=q.exchange, qty=qty, price=price,
            env=cfg.env, tr_id=tr_id, est_value_usd=est, cur_price=q.price,
            body=body, warnings=warns, executed=False,
        )

    hashkey = make_hashkey(body, cfg=cfg)
    resp = kis_post(_ORDER_PATH, tr_id, body, cfg=cfg, hashkey=hashkey)
    out = resp.get("output") or {}
    return UsOrderResult(
        side=side, symbol=q.symbol, exchange=q.exchange, qty=qty, price=price,
        env=cfg.env, order_no=(out.get("ODNO") or "").strip() or None,
        order_time=(out.get("ORD_TMD") or "").strip() or None,
        message=resp.get("msg1"), executed=True,
    )


def _us_checks(cfg, side, q: UsQuote, qty, price, est) -> list[str]:
    warns: list[str] = []
    if cfg.env == "prod":
        warns.append("⚠️ 실전 계좌 — 실제 체결 시 결제됩니다.")
    if q.price:
        gap = (price / q.price - 1) * 100
        if abs(gap) >= 10:
            warns.append(f"지정가 ${price:,.2f}가 현재가 ${q.price:,.2f}와 {gap:+.1f}% 차이 — 오타 점검.")
    if side == "buy":
        try:
            # 통합증거금 반영 실제 매수가능(원화 포함). USD 예수금만 보지 않는다.
            b = fetch_us_buyable(q.exchange, price, q.symbol, cfg=cfg)
            mq = b["max_qty"]
            if mq is not None and qty > mq:
                warns.append(
                    f"매수가능 초과 — 원화 포함 최대 {mq}주(≈${b['buyable']:,.0f}). 수량 줄이거나 입금."
                )
            elif b["usd_only"] is not None and est > b["usd_only"] and mq and qty <= mq:
                warns.append(
                    f"달러 예수금 ${b['usd_only']:,.2f}는 부족하지만 통합증거금(원화)으로 매수가능(최대 {mq}주)."
                )
        except KisError:
            pass
    return warns


def to_dict(obj) -> dict:
    return asdict(obj)
