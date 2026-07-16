# FILE: research_Mvp/module_kis/_account.py
"""국내주식 계좌 잔고 조회 (예수금 + 보유종목 + 평가손익).

엔드포인트: GET /uapi/domestic-stock/v1/trading/inquire-balance
tr_id:      TTTC8434R(실전) / VTTC8434R(모의)

⚠️ **읽기 전용 잔고조회만.** 주문/체결/이체 함수는 이 모듈에 없다(의도적).
   잔고조회는 '조회(read)'라 프로젝트 읽기전용 원칙에 부합하지만,
   계좌번호(KIS_ACCOUNT_NO)와 계좌 권한이 필요하다.

보유종목 50개 초과 시 tr_cont(연속조회) 헤더로 페이지네이션.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Optional

from ._auth import KisConfig, load_config
from ._client import kis_get
from ._parse import to_float, to_int

_PATH = "/uapi/domestic-stock/v1/trading/inquire-balance"
_TR_ID = {"prod": "TTTC8434R", "vps": "VTTC8434R"}
_MAX_PAGES = 10


@dataclass
class Holding:
    code: str                       # pdno 종목코드
    name: Optional[str] = None      # prdt_name 종목명
    qty: Optional[int] = None       # hldg_qty 보유수량
    avg_price: Optional[float] = None   # pchs_avg_pric 매입평균가
    cur_price: Optional[float] = None   # prpr 현재가
    buy_amount: Optional[int] = None    # pchs_amt 매입금액
    eval_amount: Optional[int] = None   # evlu_amt 평가금액
    pnl_amount: Optional[int] = None    # evlu_pfls_amt 평가손익금액
    pnl_pct: Optional[float] = None     # evlu_pfls_rt 평가손익율(%)


@dataclass
class Balance:
    deposit: Optional[int] = None         # dnca_tot_amt 예수금 총액
    d2_deposit: Optional[int] = None      # prvs_rcdl_excc_amt 예수금(D+2 출금가능)
    eval_securities: Optional[int] = None  # scts_evlu_amt 유가증권 평가액
    total_eval: Optional[int] = None      # tot_evlu_amt 총평가금액(예수금+유가)
    net_asset: Optional[int] = None       # nass_amt 순자산금액
    total_buy: Optional[int] = None       # pchs_amt_smtl_amt 매입금액 합계
    total_pnl: Optional[int] = None       # evlu_pfls_smtl_amt 평가손익 합계
    holdings: list[Holding] = field(default_factory=list)

    @property
    def total_pnl_pct(self) -> Optional[float]:
        if self.total_buy and self.total_pnl is not None and self.total_buy != 0:
            return round(self.total_pnl / self.total_buy * 100, 2)
        return None


def _parse_holdings(output1: list) -> list[Holding]:
    out: list[Holding] = []
    for r in output1 or []:
        qty = to_int(r.get("hldg_qty"))
        if not qty:  # 보유수량 0 행은 스킵(KIS가 0짜리 행을 끼워 주기도 함).
            continue
        out.append(
            Holding(
                code=(r.get("pdno") or "").strip(),
                name=(r.get("prdt_name") or "").strip() or None,
                qty=qty,
                avg_price=to_float(r.get("pchs_avg_pric")),
                cur_price=to_float(r.get("prpr")),
                buy_amount=to_int(r.get("pchs_amt")),
                eval_amount=to_int(r.get("evlu_amt")),
                pnl_amount=to_int(r.get("evlu_pfls_amt")),
                pnl_pct=to_float(r.get("evlu_pfls_rt")),
            )
        )
    return out


def fetch_balance(cfg: Optional[KisConfig] = None) -> Balance:
    """계좌 잔고(예수금 + 보유종목 + 평가손익)를 조회.

    Raises:
        KisError: 계좌번호 미설정 또는 조회 권한/네트워크 실패.
    """
    cfg = cfg or load_config()
    cfg.require_account()
    tr_id = _TR_ID["vps" if cfg.is_paper else "prod"]

    base_params = {
        "CANO": cfg.cano,
        "ACNT_PRDT_CD": cfg.acnt_prdt_cd,
        "AFHR_FLPR_YN": "N",        # 시간외단일가 여부
        "OFL_YN": "",               # 오프라인 여부
        "INQR_DVSN": "02",          # 조회구분 02=종목별
        "UNPR_DVSN": "01",          # 단가구분
        "FUND_STTL_ICLD_YN": "N",   # 펀드결제분 포함여부
        "FNCG_AMT_AUTO_RDPT_YN": "N",  # 융자금액 자동상환 여부
        "PRCS_DVSN": "00",          # 00=전일매매 포함
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": "",
    }

    bal = Balance()
    summary_set = False
    tr_cont = ""

    for _ in range(_MAX_PAGES):
        body, headers = kis_get(
            _PATH, tr_id, base_params, cfg=cfg,
            extra_headers={"tr_cont": tr_cont} if tr_cont else None,
            return_headers=True,
        )
        bal.holdings.extend(_parse_holdings(body.get("output1") or []))

        if not summary_set:
            o2 = (body.get("output2") or [{}])[0]
            bal.deposit = to_int(o2.get("dnca_tot_amt"))
            bal.d2_deposit = to_int(o2.get("prvs_rcdl_excc_amt"))
            bal.eval_securities = to_int(o2.get("scts_evlu_amt"))
            bal.total_eval = to_int(o2.get("tot_evlu_amt"))
            bal.net_asset = to_int(o2.get("nass_amt"))
            bal.total_buy = to_int(o2.get("pchs_amt_smtl_amt"))
            bal.total_pnl = to_int(o2.get("evlu_pfls_smtl_amt"))
            summary_set = True

        # 연속조회: 응답헤더 tr_cont 가 F/M 이면 다음 페이지 존재.
        cont = (headers.get("tr_cont") or "").strip().upper()
        if cont in ("F", "M"):
            tr_cont = "N"
            base_params["CTX_AREA_FK100"] = body.get("ctx_area_fk100", "") or ""
            base_params["CTX_AREA_NK100"] = body.get("ctx_area_nk100", "") or ""
        else:
            break

    bal.holdings.sort(key=lambda h: h.eval_amount or 0, reverse=True)
    return bal


def to_dict(bal: Balance) -> dict:
    d = asdict(bal)
    d["total_pnl_pct"] = bal.total_pnl_pct
    return d
