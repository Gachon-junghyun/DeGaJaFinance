# FILE: research_Mvp/module_kis/_quote.py
"""국내주식 현재가 시세 + 밸류에이션 스냅샷.

엔드포인트: GET /uapi/domestic-stock/v1/quotations/inquire-price
tr_id:      FHKST01010100 (실전/모의 동일)

네이버 스크랩(module_valuation)의 무인증 대안 — KIS 공식 실시간 시세로
현재가·등락·거래량·시총·PER/PBR/EPS/BPS·52주 고저·외국인 소진율을 한 번에.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Optional

from ._client import kis_get
from ._auth import KisConfig
from ._parse import norm_code, to_float, to_int

_PATH = "/uapi/domestic-stock/v1/quotations/inquire-price"
_TR_ID = "FHKST01010100"

# prdy_vrss_sign: 1 상한 2 상승 3 보합 4 하한 5 하락
_SIGN_LABEL = {"1": "상한", "2": "상승", "3": "보합", "4": "하한", "5": "하락"}

# iscd_stat_cls_code(종목상태 구분). 55=신용가능(정상)이라 '00 외 전부 경고'는 오판 —
# 삼성전자도 55로 나온다. 실제 리스크 코드(_RISK_STATUS)만 경고로 취급한다.
_STATUS_LABEL = {
    "00": "구분없음",
    "51": "관리종목",
    "52": "투자위험",
    "53": "투자경고",
    "54": "투자주의",
    "55": "정상(신용가능)",
    "57": "증거금100%",
    "58": "거래정지",
    "59": "단기과열",
}
_RISK_STATUS = {"51", "52", "53", "54", "58", "59"}

# mrkt_warn_cls_code(시장경고): 00 없음 / 01 투자주의 / 02 투자경고 / 03 투자위험
_WARN_LABEL = {"00": "없음", "01": "투자주의", "02": "투자경고", "03": "투자위험"}


@dataclass
class KisQuote:
    code: str
    name: Optional[str] = None              # 종목명(업종 한글명이 아닌 HTS 종목명)
    sector: Optional[str] = None            # 업종 한글명 (bstp_kor_isnm)
    price: Optional[float] = None           # 현재가 (원)
    change: Optional[float] = None          # 전일 대비 (원)
    change_pct: Optional[float] = None      # 전일 대비율 (%)
    sign: Optional[str] = None              # 등락 부호 라벨
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    prev_close: Optional[float] = None      # 기준가(전일 종가)
    upper_limit: Optional[float] = None     # 상한가
    lower_limit: Optional[float] = None     # 하한가
    volume: Optional[int] = None            # 누적 거래량 (주)
    value_traded: Optional[int] = None      # 누적 거래대금 (원)
    market_cap_eok: Optional[float] = None  # 시가총액 (억원)
    listed_shares: Optional[int] = None     # 상장 주수
    per: Optional[float] = None
    pbr: Optional[float] = None
    eps: Optional[float] = None
    bps: Optional[float] = None
    week52_high: Optional[float] = None
    week52_low: Optional[float] = None
    foreign_pct: Optional[float] = None     # 외국인 소진율 (%)
    turnover_pct: Optional[float] = None    # 거래량 회전율 (%)
    status_code: Optional[str] = None       # iscd_stat_cls_code (55=정상, 51~59 risk)
    warn_code: Optional[str] = None         # mrkt_warn_cls_code (00 없음)

    def pct_from_52w_high(self) -> Optional[float]:
        if self.week52_high and self.price:
            return round((self.price / self.week52_high - 1) * 100, 2)
        return None

    def status_label(self) -> Optional[str]:
        return _STATUS_LABEL.get((self.status_code or "").strip())

    def warn_label(self) -> Optional[str]:
        return _WARN_LABEL.get((self.warn_code or "").strip())

    def is_flagged(self) -> bool:
        """관리/위험/경고/주의/정지/과열 등 실제 리스크 상태인지."""
        return (self.status_code or "").strip() in _RISK_STATUS or (
            (self.warn_code or "").strip() not in ("", "00")
        )


def fetch_quote(code: str, cfg: Optional[KisConfig] = None) -> KisQuote:
    """6자리 종목코드 → 현재가/밸류에이션 스냅샷."""
    code = norm_code(code)
    body = kis_get(
        _PATH,
        _TR_ID,
        {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": code},
        cfg=cfg,
    )
    o = body.get("output") or {}
    return KisQuote(
        code=code,
        # inquire-price 는 한글 종목명을 안 준다(코드+업종명만). 이름은 _chart 의
        # output1.hts_kor_isnm 이나 watchlist.db 매핑으로 호출부에서 보강한다.
        name=None,
        sector=o.get("bstp_kor_isnm") or None,
        price=to_float(o.get("stck_prpr")),
        change=to_float(o.get("prdy_vrss")),
        change_pct=to_float(o.get("prdy_ctrt")),
        sign=_SIGN_LABEL.get(str(o.get("prdy_vrss_sign", "")).strip()),
        open=to_float(o.get("stck_oprc")),
        high=to_float(o.get("stck_hgpr")),
        low=to_float(o.get("stck_lwpr")),
        prev_close=to_float(o.get("stck_sdpr")),
        upper_limit=to_float(o.get("stck_mxpr")),
        lower_limit=to_float(o.get("stck_llam")),
        volume=to_int(o.get("acml_vol")),
        value_traded=to_int(o.get("acml_tr_pbmn")),
        market_cap_eok=to_float(o.get("hts_avls")),
        listed_shares=to_int(o.get("lstn_stcn")),
        per=to_float(o.get("per")),
        pbr=to_float(o.get("pbr")),
        eps=to_float(o.get("eps")),
        bps=to_float(o.get("bps")),
        week52_high=to_float(o.get("w52_hgpr")),
        week52_low=to_float(o.get("w52_lwpr")),
        foreign_pct=to_float(o.get("hts_frgn_ehrt")),
        turnover_pct=to_float(o.get("vol_tnrt")),
        status_code=(o.get("iscd_stat_cls_code") or None),
        warn_code=(o.get("mrkt_warn_cls_code") or None),
    )


def to_dict(q: KisQuote) -> dict:
    d = asdict(q)
    d["pct_from_52w_high"] = q.pct_from_52w_high()
    return d
