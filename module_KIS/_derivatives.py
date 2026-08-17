# FILE: module_KIS/_derivatives.py
"""국내 선물옵션 시세 — 읽기 전용 (v1: 지수선물).

KIS Open API [국내선물옵션] 기본시세. TR_ID 는 공식 리포에서 확정:
  https://github.com/koreainvestment/open-trading-api (examples_llm/domestic_futureoption)

- 선물 전광판  display-board-futures  tr_id=FHPIF05030200  (F/20503/MKI)
    → KOSPI200 지수선물 근월물 목록: 현재가·등락·거래량·미결제약정·이론가·잔존일수·호가잔량
- 선물옵션 시세 inquire-price          tr_id=FHMIF10000000  (F:지수선물 / O:지수옵션)
    → 계약별 상세(output1) + 기초지수(output2=종합, output3=KOSPI200)
      basis(베이시스)·dprt(괴리율)·미결제약정 증감·최종거래일 포함

⚠ 읽기 전용. 주문/잔고 없음(그 TR 들은 별도, 파생 주문은 삼중차단 필요).
⚠ 옵션(IV/그릭)은 v1 미포함 — display-board-option-list 가 추가 파라미터(FID_MTRT_CNT 등)를
   요구해 v1.1 로 분리한다.
필드명은 라이브 응답(2026-07-24 세션)에서 실측 확인함.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import List, Optional

from ._client import kis_get
from ._auth import KisConfig
from ._parse import to_float, to_int

_PATH_BOARD = "/uapi/domestic-futureoption/v1/quotations/display-board-futures"
_TR_BOARD = "FHPIF05030200"
_PATH_PRICE = "/uapi/domestic-futureoption/v1/quotations/inquire-price"
_TR_PRICE = "FHMIF10000000"

# prdy_vrss_sign: 1 상한 2 상승 3 보합 4 하한 5 하락
_SIGN = {"1": "상한", "2": "상승", "3": "보합", "4": "하한", "5": "하락"}


@dataclass
class FutBoardRow:
    code: str                              # futs_shrn_iscd (예: A05608)
    name: Optional[str] = None             # hts_kor_isnm (예: 미니F 202608)
    price: Optional[float] = None          # futs_prpr
    change: Optional[float] = None         # futs_prdy_vrss
    change_pct: Optional[float] = None     # futs_prdy_ctrt
    sign: Optional[str] = None
    volume: Optional[int] = None           # acml_vol
    open_interest: Optional[int] = None    # hts_otst_stpl_qty (미결제약정)
    theoretical: Optional[float] = None    # hts_thpr (이론가)
    days_left: Optional[int] = None        # hts_rmnn_dynu (잔존일수)
    ask: Optional[float] = None            # futs_askp
    bid: Optional[float] = None            # futs_bidp


@dataclass
class FutOptQuote:
    code: str
    name: Optional[str] = None
    market: str = "F"                      # F 지수선물 / O 지수옵션
    price: Optional[float] = None          # futs_prpr
    change: Optional[float] = None         # futs_prdy_vrss
    change_pct: Optional[float] = None     # futs_prdy_ctrt
    sign: Optional[str] = None
    prev_close: Optional[float] = None     # futs_prdy_clpr
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    upper_limit: Optional[float] = None    # futs_mxpr
    lower_limit: Optional[float] = None    # futs_llam
    volume: Optional[int] = None
    value_traded: Optional[int] = None     # acml_tr_pbmn
    open_interest: Optional[int] = None    # hts_otst_stpl_qty
    oi_change: Optional[int] = None        # otst_stpl_qty_icdc (미결제 증감)
    basis: Optional[float] = None          # basis (선물−현물)
    theoretical: Optional[float] = None    # hts_thpr
    disparity: Optional[float] = None      # dprt (괴리율 %)
    days_left: Optional[int] = None        # hts_rmnn_dynu
    last_trade_date: Optional[str] = None  # futs_last_tr_date (YYYYMMDD)
    # 기초지수 (동시 반환)
    kospi: Optional[float] = None          # output2 종합 bstp_nmix_prpr
    kospi_pct: Optional[float] = None
    kospi200: Optional[float] = None       # output3 KOSPI200 bstp_nmix_prpr
    kospi200_pct: Optional[float] = None


def fetch_futures_board(cfg: Optional[KisConfig] = None) -> List[FutBoardRow]:
    """KOSPI200 지수선물 전광판(근월물 목록)."""
    body = kis_get(
        _PATH_BOARD, _TR_BOARD,
        {"FID_COND_MRKT_DIV_CODE": "F", "FID_COND_SCR_DIV_CODE": "20503",
         "FID_COND_MRKT_CLS_CODE": "MKI"},
        cfg=cfg,
    )
    rows = body.get("output") or []
    out: List[FutBoardRow] = []
    for r in rows:
        out.append(FutBoardRow(
            code=(r.get("futs_shrn_iscd") or "").strip(),
            name=(r.get("hts_kor_isnm") or "").strip() or None,
            price=to_float(r.get("futs_prpr")),
            change=to_float(r.get("futs_prdy_vrss")),
            change_pct=to_float(r.get("futs_prdy_ctrt")),
            sign=_SIGN.get(str(r.get("prdy_vrss_sign", "")).strip()),
            volume=to_int(r.get("acml_vol")),
            open_interest=to_int(r.get("hts_otst_stpl_qty")),
            theoretical=to_float(r.get("hts_thpr")),
            days_left=to_int(r.get("hts_rmnn_dynu")),
            ask=to_float(r.get("futs_askp")),
            bid=to_float(r.get("futs_bidp")),
        ))
    return out


def fetch_futopt_price(code: str, market: str = "F",
                       cfg: Optional[KisConfig] = None) -> FutOptQuote:
    """계약코드(전광판의 futs_shrn_iscd, 예 A05608) → 상세 시세 + 기초지수.

    market: 'F' 지수선물 / 'O' 지수옵션.
    """
    code = (code or "").strip().upper()
    market = (market or "F").strip().upper()
    body = kis_get(
        _PATH_PRICE, _TR_PRICE,
        {"FID_COND_MRKT_DIV_CODE": market, "FID_INPUT_ISCD": code},
        cfg=cfg,
    )
    o1 = body.get("output1") or {}
    o2 = body.get("output2") or {}   # 종합
    o3 = body.get("output3") or {}   # KOSPI200
    return FutOptQuote(
        code=code,
        name=(o1.get("hts_kor_isnm") or "").strip() or None,
        market=market,
        price=to_float(o1.get("futs_prpr")),
        change=to_float(o1.get("futs_prdy_vrss")),
        change_pct=to_float(o1.get("futs_prdy_ctrt")),
        sign=_SIGN.get(str(o1.get("prdy_vrss_sign", "")).strip()),
        prev_close=to_float(o1.get("futs_prdy_clpr")),
        open=to_float(o1.get("futs_oprc")),
        high=to_float(o1.get("futs_hgpr")),
        low=to_float(o1.get("futs_lwpr")),
        upper_limit=to_float(o1.get("futs_mxpr")),
        lower_limit=to_float(o1.get("futs_llam")),
        volume=to_int(o1.get("acml_vol")),
        value_traded=to_int(o1.get("acml_tr_pbmn")),
        open_interest=to_int(o1.get("hts_otst_stpl_qty")),
        oi_change=to_int(o1.get("otst_stpl_qty_icdc")),
        basis=to_float(o1.get("basis")),
        theoretical=to_float(o1.get("hts_thpr")),
        disparity=to_float(o1.get("dprt")),
        days_left=to_int(o1.get("hts_rmnn_dynu")),
        last_trade_date=(o1.get("futs_last_tr_date") or "").strip() or None,
        kospi=to_float(o2.get("bstp_nmix_prpr")),
        kospi_pct=to_float(o2.get("bstp_nmix_prdy_ctrt")),
        kospi200=to_float(o3.get("bstp_nmix_prpr")),
        kospi200_pct=to_float(o3.get("bstp_nmix_prdy_ctrt")),
    )


def board_to_dict(r: FutBoardRow) -> dict:
    return asdict(r)


def quote_to_dict(q: FutOptQuote) -> dict:
    return asdict(q)


def _fmt(v, nd=2):
    if v is None:
        return "-"
    if isinstance(v, float):
        return f"{v:,.{nd}f}"
    return f"{v:,}"


def render_board(rows: List[FutBoardRow]) -> str:
    if not rows:
        return "## KOSPI200 지수선물 전광판\n\n_조회 결과 없음._"
    out = ["## KOSPI200 지수선물 전광판 (근월물)", ""]
    out.append("| 계약 | 코드 | 현재가 | 등락% | 거래량 | 미결제약정 | 이론가 | 잔존일 |")
    out.append("|---|---|---|---|---|---|---|---|")
    for r in rows:
        out.append(
            f"| {r.name or '-'} | {r.code} | {_fmt(r.price)} | {_fmt(r.change_pct)} | "
            f"{_fmt(r.volume,0)} | {_fmt(r.open_interest,0)} | {_fmt(r.theoretical)} | "
            f"{_fmt(r.days_left,0)} |"
        )
    out.append("")
    out.append("_source: 한국투자증권(KIS) Open API · 국내선물옵션 전광판(조회 전용)_")
    return "\n".join(out)


def render_futopt(q: FutOptQuote) -> str:
    mk = "지수선물" if q.market == "F" else ("지수옵션" if q.market == "O" else q.market)
    out = [f"## {q.name or q.code} ({q.code}) — {mk} 시세", ""]
    out.append(f"- 현재가: **{_fmt(q.price)}** ({q.sign or ''} {_fmt(q.change)} · {_fmt(q.change_pct)}%)")
    out.append(f"- 시/고/저: {_fmt(q.open)} / {_fmt(q.high)} / {_fmt(q.low)}  ·  전일: {_fmt(q.prev_close)}")
    out.append(f"- 거래량: {_fmt(q.volume,0)}  ·  거래대금: {_fmt(q.value_traded,0)}")
    out.append(f"- **미결제약정: {_fmt(q.open_interest,0)}** (증감 {_fmt(q.oi_change,0)})")
    out.append(f"- **베이시스: {_fmt(q.basis)}**  ·  이론가: {_fmt(q.theoretical)}  ·  괴리율: {_fmt(q.disparity)}%")
    out.append(f"- 잔존일수: {_fmt(q.days_left,0)}  ·  최종거래일: {q.last_trade_date or '-'}")
    idx = []
    if q.kospi is not None:
        idx.append(f"종합 {_fmt(q.kospi)} ({_fmt(q.kospi_pct)}%)")
    if q.kospi200 is not None:
        idx.append(f"KOSPI200 {_fmt(q.kospi200)} ({_fmt(q.kospi200_pct)}%)")
    if idx:
        out.append(f"- 기초지수: {' · '.join(idx)}")
    out.append("")
    out.append("_source: 한국투자증권(KIS) Open API · 국내선물옵션 시세(조회 전용)_")
    return "\n".join(out)
