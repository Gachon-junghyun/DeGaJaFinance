# FILE: research_Mvp/module_kis/_overseas.py
"""해외주식 체결기준 현재잔고 — 외화예수금(달러 등) + 해외 보유종목 + 총자산.

엔드포인트: GET /uapi/overseas-stock/v1/trading/inquire-present-balance
tr_id:      CTRP6504R(실전)

국내잔고(_account.inquire-balance)는 원화만 잡는다. 달러 등 외화예수금과 해외주식은
이 엔드포인트가 통화별로 돌려준다. output3 의 tot_asst_amt 가 원화+외화 합산 총자산.

⚠️ 읽기 전용. 계좌에 해외주식 거래가 활성화돼 있어야 조회된다(없으면 KisError).
필드명은 2026-06-26 실제 응답으로 검증(외화 cash/총자산). 해외 보유종목 필드는
보유분이 있을 때 추가 검증 필요(현재 계좌는 보유 0이라 best-effort 매핑).
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Optional

from ._auth import KisConfig, load_config
from ._client import kis_get
from ._parse import to_float, to_int

_PATH = "/uapi/overseas-stock/v1/trading/inquire-present-balance"
_TR_ID = "CTRP6504R"  # 실전. (모의 미지원 — 모의계좌면 KisError)


@dataclass
class ForeignCash:
    currency: str                      # crcy_cd (USD/HKD/JPY...)
    name: Optional[str] = None         # crcy_cd_name
    deposit: Optional[float] = None    # frcr_dncl_amt_2 외화예수금
    withdrawable: Optional[float] = None  # frcr_drwg_psbl_amt_1 외화출금가능
    exchange_rate: Optional[float] = None  # frst_bltn_exrt 최초고시환율
    eval_krw: Optional[float] = None   # frcr_evlu_amt2 원화환산 평가액


@dataclass
class OverseasHolding:
    code: str                          # ovrs_pdno
    name: Optional[str] = None         # ovrs_item_name / prdt_name
    qty: Optional[float] = None        # ccld_qty_smtl1 / ovrs_cblc_qty
    avg_price: Optional[float] = None  # pchs_avg_pric
    cur_price: Optional[float] = None  # ovrs_now_pric1 / now_pric2
    eval_frcr: Optional[float] = None  # ovrs_stck_evlu_amt1 평가금액(외화)
    pnl_frcr: Optional[float] = None   # evlu_pfls_amt_smtl 평가손익(외화)
    pnl_pct: Optional[float] = None    # evlu_pfls_rt1
    currency: Optional[str] = None     # crcy_cd
    exchange: Optional[str] = None     # ovrs_excg_cd


@dataclass
class OverseasBalance:
    foreign_cash: list[ForeignCash] = field(default_factory=list)
    holdings: list[OverseasHolding] = field(default_factory=list)
    total_asset_krw: Optional[int] = None     # tot_asst_amt 총자산(원화+외화)
    krw_deposit: Optional[int] = None         # tot_dncl_amt 원화 예수금 총액
    frcr_eval_total_krw: Optional[int] = None  # frcr_evlu_tota 외화평가 총액(원화)
    withdrawable_krw: Optional[int] = None    # wdrw_psbl_tot_amt 출금가능 총액


def _first(d: dict, *keys: str):
    """후보 키들 중 처음 존재하는 값(해외 보유종목 필드명 변형 대응)."""
    for k in keys:
        if k in d and d[k] not in ("", None):
            return d[k]
    return None


def _parse_cash(output2: list) -> list[ForeignCash]:
    out: list[ForeignCash] = []
    for r in output2 or []:
        dep = to_float(r.get("frcr_dncl_amt_2"))
        cur = (r.get("crcy_cd") or "").strip()
        if not cur:
            continue
        # 예수금·평가 모두 0인 통화 행은 스킵(노이즈).
        if not dep and not to_float(r.get("frcr_evlu_amt2")):
            continue
        out.append(
            ForeignCash(
                currency=cur,
                name=(r.get("crcy_cd_name") or "").strip() or None,
                deposit=dep,
                withdrawable=to_float(r.get("frcr_drwg_psbl_amt_1")),
                exchange_rate=to_float(r.get("frst_bltn_exrt")),
                eval_krw=to_float(r.get("frcr_evlu_amt2")),
            )
        )
    return out


def _parse_holdings(output1: list) -> list[OverseasHolding]:
    out: list[OverseasHolding] = []
    for r in output1 or []:
        qty = to_float(_first(r, "ccld_qty_smtl1", "ovrs_cblc_qty", "cblc_qty13"))
        if not qty:
            continue
        out.append(
            OverseasHolding(
                code=(_first(r, "ovrs_pdno", "pdno") or "").strip(),
                name=(_first(r, "ovrs_item_name", "prdt_name") or "").strip() or None,
                qty=qty,
                avg_price=to_float(_first(r, "pchs_avg_pric", "avg_unpr3")),
                cur_price=to_float(_first(r, "ovrs_now_pric1", "now_pric2")),
                eval_frcr=to_float(_first(r, "ovrs_stck_evlu_amt1", "frcr_evlu_amt2")),
                pnl_frcr=to_float(_first(r, "evlu_pfls_amt_smtl", "frcr_evlu_pfls_amt")),
                pnl_pct=to_float(_first(r, "evlu_pfls_rt1", "evlu_pfls_rt")),
                currency=(_first(r, "crcy_cd") or "").strip() or None,
                exchange=(_first(r, "ovrs_excg_cd") or "").strip() or None,
            )
        )
    return out


def fetch_overseas_balance(cfg: Optional[KisConfig] = None) -> OverseasBalance:
    """해외주식 체결기준 현재잔고(외화예수금+해외보유종목+총자산) 조회.

    Raises:
        KisError: 계좌번호 미설정, 해외거래 미활성, 모의계좌 등.
    """
    cfg = cfg or load_config()
    cfg.require_account()

    body = kis_get(
        _PATH, _TR_ID,
        {
            "CANO": cfg.cano,
            "ACNT_PRDT_CD": cfg.acnt_prdt_cd,
            "WCRC_FRCR_DVSN_CD": "02",  # 02=외화 기준
            "NATN_CD": "000",           # 000=전체 국가
            "TR_MKET_CD": "00",         # 00=전체 시장
            "INQR_DVSN_CD": "00",
        },
        cfg=cfg,
    )
    ob = OverseasBalance(
        foreign_cash=_parse_cash(body.get("output2") or []),
        holdings=_parse_holdings(body.get("output1") or []),
    )
    o3 = body.get("output3") or {}
    ob.total_asset_krw = to_int(o3.get("tot_asst_amt"))
    ob.krw_deposit = to_int(o3.get("tot_dncl_amt"))
    ob.frcr_eval_total_krw = to_int(o3.get("frcr_evlu_tota"))
    ob.withdrawable_krw = to_int(o3.get("wdrw_psbl_tot_amt"))
    return ob


def to_dict(ob: OverseasBalance) -> dict:
    return asdict(ob)
