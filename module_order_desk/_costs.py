# FILE: module_order_desk/_costs.py
"""거래비용 원장 · 손익분기가 — "수수료·세금까지 전부 0이 되는 가격".

주문 데스크가 쓰는 **거래비용의 단일 원본(P1)**. 수수료율·세율을 다른 파일에 다시 적지 않는다.

무엇을 세나 (현금흐름 그대로, 대차대조표처럼 좌/우):
    진입 = 현금유출   매수대금 · 위탁수수료 · (미국·원화정산이면) 환전 스프레드
    청산 = 현금유입   매도대금 · 위탁수수료 · 증권거래세(국내) · SEC fee·FINRA TAF(미국)
                     · 환전 스프레드 · 보유 중 받은 배당(현금유입)
    **손익분기가 = 유입 합계가 유출 합계와 정확히 같아지는 매도가**(이분법으로 푼다).
    최소수수료·주당 TAF 처럼 비선형 항이 있어 닫힌식 대신 수치해를 쓴다 — 어떤 요율 조합이 와도 0이 맞는다.

⚠️ **요율은 계좌마다 다르다.** 기본값은 '한국투자 온라인 일반' 가정이고, 세율은 아래 날짜 기준이다.
   실제 요율은 리포 루트 `.env` 에서 덮어쓴다(요율이 틀리면 손익분기가도 틀린다 — P4).

    KIS_FEE_KR_PCT=0.0140527    국내 위탁수수료(편도, %, 유관기관 제비용 포함)
    KIS_FEE_KR_MIN=0            국내 최소수수료(원)
    KIS_TAX_KOSPI_PCT=0.15      국내 매도 증권거래세+농특세(%) — 코스피
    KIS_TAX_KOSDAQ_PCT=0.15     코스닥
    KIS_TAX_KONEX_PCT=0.10      코넥스
    KIS_TAX_ETF_PCT=0           국내 상장 ETF/ETN(거래세 면제)
    KIS_FEE_US_PCT=0.25         미국 온라인 위탁수수료(편도, %)
    KIS_FEE_US_MIN=0.01         미국 최소수수료(USD)
    KIS_SEC_FEE_PCT=0.00278     SEC fee(매도만, %) — 미국 규제기관이 해마다 고친다
    KIS_TAF_PER_SHARE=0.000166  FINRA TAF(매도만, 주당 USD)
    KIS_TAF_MAX=8.30            TAF 건당 상한(USD)
    KIS_FX_SPREAD_PCT=0         환전 스프레드(편도, %, 매매기준율 대비 — 우대율 반영해 직접 설정)

세율 기준일: 2025-01(국내 거래세 0.15%) · 2025 요율표(SEC/TAF). 그 뒤 개정됐다면 .env 로 덮어쓴다.
"""
from __future__ import annotations

import math
import os
import unicodedata
from dataclasses import asdict, dataclass, field
from typing import Callable, Optional

# ── 기본 요율 (%, 또는 통화단위) ─────────────────────────────────────
DEFAULTS: dict[str, float] = {
    "KIS_FEE_KR_PCT": 0.0140527,
    "KIS_FEE_KR_MIN": 0.0,
    "KIS_TAX_KOSPI_PCT": 0.15,
    "KIS_TAX_KOSDAQ_PCT": 0.15,
    "KIS_TAX_KONEX_PCT": 0.10,
    "KIS_TAX_ETF_PCT": 0.0,
    "KIS_FEE_US_PCT": 0.25,
    "KIS_FEE_US_MIN": 0.01,
    "KIS_SEC_FEE_PCT": 0.00278,
    "KIS_TAF_PER_SHARE": 0.000166,
    "KIS_TAF_MAX": 8.30,
    "KIS_FX_SPREAD_PCT": 0.0,
}

# 미국주식 양도소득세(선택 계산용) — 손익분기 자체는 못 움직인다(이익 0이면 세금 0).
US_CGT_RATE = 0.22            # 20% + 지방소득세 2%
US_CGT_DEDUCTION = 2_500_000  # 연 기본공제(원)


def _num(key: str) -> float:
    """환경변수 우선, 없으면 DEFAULTS. 파싱 실패 시 기본값(조용히 죽지 않게)."""
    raw = os.environ.get(key, "").strip()
    if not raw:
        return DEFAULTS[key]
    try:
        return float(raw)
    except ValueError:
        return DEFAULTS[key]


def _rate(key: str) -> float:
    """퍼센트로 적힌 환경변수를 비율(0.0015)로."""
    return _num(key) / 100.0


# ── 요율표 ──────────────────────────────────────────────────────────
@dataclass
class FeeSchedule:
    market: str            # kr | us
    board: str             # kospi | kosdaq | konex | etf | us
    currency: str          # 종목 거래통화 (KRW | USD)
    settle_currency: str   # 정산통화 (원화결제면 KRW)
    buy_fee_rate: float
    sell_fee_rate: float
    min_fee: float
    sell_tax_rate: float = 0.0
    sec_fee_rate: float = 0.0
    taf_per_share: float = 0.0
    taf_max: float = 0.0
    fx_spread_rate: float = 0.0

    @property
    def fx(self) -> bool:
        """정산통화가 거래통화와 다른가(=환전이 끼는가)."""
        return self.settle_currency != self.currency


_KR_TAX_KEY = {
    "kospi": "KIS_TAX_KOSPI_PCT",
    "kosdaq": "KIS_TAX_KOSDAQ_PCT",
    "konex": "KIS_TAX_KONEX_PCT",
    "etf": "KIS_TAX_ETF_PCT",
}

# 국내 상장 ETF/ETN 브랜드 접두어(거래세 면제 자동판정용). 확신 못하면 kospi 로 둔다.
_ETF_BRANDS = (
    "KODEX", "TIGER", "KBSTAR", "ARIRANG", "HANARO", "KOSEF", "ACE", "SOL",
    "RISE", "PLUS", "TIMEFOLIO", "KIWOOM", "히어로즈", "TREX", "마이다스",
    "1Q", "BNK", "WOORI", "파워", "네비게이터", "VITA", "ITF", "FOCUS", "UNICORN",
)


def guess_board(name: Optional[str] = None, code: Optional[str] = None) -> str:
    """종목명으로 ETF/ETN 여부만 판정(거래세 면제). 그 외는 'kospi'(코스닥과 세율 동일)."""
    n = (name or "").upper().replace(" ", "")
    if not n:
        return "kospi"
    if "ETN" in n or n.startswith(_ETF_BRANDS):
        return "etf"
    return "kospi"


def schedule(market: str, board: Optional[str] = None, *,
             settle_krw: bool = False) -> FeeSchedule:
    """시장·보드별 요율표. settle_krw=True 면 미국주식을 원화 현금흐름으로 정산(환전 포함)."""
    market = (market or "kr").lower()
    if market == "us":
        return FeeSchedule(
            market="us", board="us", currency="USD",
            settle_currency="KRW" if settle_krw else "USD",
            buy_fee_rate=_rate("KIS_FEE_US_PCT"),
            sell_fee_rate=_rate("KIS_FEE_US_PCT"),
            min_fee=_num("KIS_FEE_US_MIN"),
            sec_fee_rate=_rate("KIS_SEC_FEE_PCT"),
            taf_per_share=_num("KIS_TAF_PER_SHARE"),
            taf_max=_num("KIS_TAF_MAX"),
            fx_spread_rate=_rate("KIS_FX_SPREAD_PCT") if settle_krw else 0.0,
        )
    board = (board or "kospi").lower()
    return FeeSchedule(
        market="kr", board=board if board in _KR_TAX_KEY else "kospi",
        currency="KRW", settle_currency="KRW",
        buy_fee_rate=_rate("KIS_FEE_KR_PCT"),
        sell_fee_rate=_rate("KIS_FEE_KR_PCT"),
        min_fee=_num("KIS_FEE_KR_MIN"),
        sell_tax_rate=_rate(_KR_TAX_KEY.get(board, "KIS_TAX_KOSPI_PCT")),
    )


# ── 현금흐름 한 줄 ──────────────────────────────────────────────────
@dataclass
class Line:
    label: str
    amount: float       # 부호 그대로: 유출 음수 · 유입 양수 (정산통화)
    note: str = ""


def _fee(gross: float, rate: float, min_fee: float) -> float:
    if gross <= 0:
        return 0.0
    return max(gross * rate, min_fee)


def buy_flow(sch: FeeSchedule, price: float, qty: float,
             fx_rate: float = 1.0) -> tuple[float, list[Line]]:
    """진입 현금유출 (정산통화, 양수 = 나간 돈)."""
    gross = price * qty
    fee = _fee(gross, sch.buy_fee_rate, sch.min_fee)
    conv = fx_rate if sch.fx else 1.0
    note = f"{price:,.4g} × {qty:,.6g}" + (f" × {fx_rate:,.2f}원" if sch.fx else "")
    lines = [
        Line("매수대금", -gross * conv, note),
        Line("위탁수수료", -fee * conv, f"{sch.buy_fee_rate * 100:.6g}%"
             + (f", 최소 {sch.min_fee:,.6g}" if sch.min_fee else "")),
    ]
    total = (gross + fee) * conv
    if sch.fx and sch.fx_spread_rate:
        spread = total * sch.fx_spread_rate
        lines.append(Line("환전 스프레드", -spread, f"편도 {sch.fx_spread_rate * 100:.6g}%"))
        total += spread
    return total, lines


def sell_flow(sch: FeeSchedule, price: float, qty: float,
              fx_rate: float = 1.0) -> tuple[float, list[Line]]:
    """청산 현금유입 (정산통화, 양수 = 들어온 돈). 수수료·세금·환전 다 뺀 뒤의 실수령."""
    gross = price * qty
    fee = _fee(gross, sch.sell_fee_rate, sch.min_fee)
    tax = gross * sch.sell_tax_rate
    sec = gross * sch.sec_fee_rate
    taf = min(qty * sch.taf_per_share, sch.taf_max) if sch.taf_per_share else 0.0
    conv = fx_rate if sch.fx else 1.0

    lines = [Line("매도대금", gross * conv,
                  f"{price:,.4g} × {qty:,.6g}" + (f" × {fx_rate:,.2f}원" if sch.fx else "")),
             Line("위탁수수료", -fee * conv, f"{sch.sell_fee_rate * 100:.6g}%")]
    if sch.sell_tax_rate:
        lines.append(Line("증권거래세", -tax * conv, f"{sch.sell_tax_rate * 100:.6g}%"
                          + (" · ETF/ETN 면제" if sch.board == "etf" else "")))
    elif sch.market == "kr":
        lines.append(Line("증권거래세", 0.0, "ETF/ETN 면제"))
    if sch.sec_fee_rate:
        lines.append(Line("SEC fee", -sec * conv, f"{sch.sec_fee_rate * 100:.6g}%"))
    if taf:
        lines.append(Line("FINRA TAF", -taf * conv,
                          f"주당 ${sch.taf_per_share:g}, 상한 ${sch.taf_max:g}"))

    net = (gross - fee - tax - sec - taf) * conv
    if sch.fx and sch.fx_spread_rate:
        spread = net * sch.fx_spread_rate
        lines.append(Line("환전 스프레드", -spread, f"편도 {sch.fx_spread_rate * 100:.6g}%"))
        net -= spread
    return net, lines


def _bisect(f: Callable[[float], float], lo: float, hi: float) -> float:
    """f(lo)<0<f(hi) 를 만족하는 구간에서 f(x)=0 을 이분법으로. 200회면 배정도 한계까지 수렴."""
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def tick_up(market: str, price: float) -> float:
    """실제로 걸 수 있는 최소 호가로 올림(국내 2023-01 호가단위 개편 기준, 미국 $0.01)."""
    if price <= 0:
        return 0.0
    if (market or "kr").lower() == "us":
        return math.ceil(price * 100 - 1e-9) / 100
    for lim, t in ((2_000, 1), (5_000, 5), (20_000, 10), (50_000, 50),
                   (200_000, 100), (500_000, 500)):
        if price < lim:
            return math.ceil(price / t - 1e-9) * t
    return math.ceil(price / 1_000 - 1e-9) * 1_000


# ── 원장 ────────────────────────────────────────────────────────────
@dataclass
class Ledger:
    market: str
    board: str
    code: str
    name: Optional[str]
    qty: float
    buy_price: float
    currency: str
    settle_currency: str
    fx_buy: Optional[float]
    fx_sell: Optional[float]
    dividend: float                 # 보유 중 받은 배당(정산통화 순수령액)
    outflow: list[Line] = field(default_factory=list)
    inflow: list[Line] = field(default_factory=list)
    cash_out: float = 0.0
    cash_in: float = 0.0
    breakeven_price: float = 0.0    # 정확해(모든 항 합계 = 0)
    breakeven_tick: float = 0.0     # 호가 올림(실제 주문 가능한 최소 지정가)
    breakeven_pct: float = 0.0      # 매입가 대비 필요 상승률(%)
    roundtrip_cost: float = 0.0     # 왕복 총비용(정산통화) — 수수료·세금·스프레드 합
    roundtrip_pct: float = 0.0      # 매수대금 대비(%)
    fx_effect_pct: float = 0.0      # 환율차가 손익분기가를 움직인 폭(%p) — 원화정산일 때만
    now: Optional[dict] = None      # 현재가 기준 '지금 팔면'
    target: Optional[dict] = None   # 목표가 시나리오
    warnings: list[str] = field(default_factory=list)


def _scenario(sch: FeeSchedule, price: float, qty: float, fx_sell: float,
              cash_out: float, dividend: float, buy_price: float,
              cgt: bool = False, cgt_deduction: float = US_CGT_DEDUCTION,
              fx_buy: float = 1.0) -> dict:
    """어떤 매도가에서의 실현 현금손익(정산통화). 미국 양도세는 선택(이익 있을 때만 붙는다)."""
    net, lines = sell_flow(sch, price, qty, fx_sell)
    pnl = net + dividend - cash_out
    tax_krw = 0.0
    if cgt and sch.market == "us":
        # 양도소득세는 원화 기준 취득/양도가액으로 계산한다(환율 반영).
        gain_krw = pnl if sch.fx else pnl * (fx_sell or 1.0)
        taxable = max(0.0, gain_krw - max(0.0, cgt_deduction))
        tax_krw = taxable * US_CGT_RATE
        if tax_krw:
            tax_local = tax_krw if sch.fx else tax_krw / (fx_sell or 1.0)
            lines.append(Line("양도소득세(22%)", -tax_local,
                              f"기본공제 {cgt_deduction:,.0f}원 차감 후"))
            pnl -= tax_local
    return {
        "price": price,
        "proceeds": net,
        "pnl": pnl,
        "pnl_pct": (pnl / cash_out * 100) if cash_out else 0.0,
        "cgt_krw": tax_krw,
        "lines": lines,
    }


def breakeven(
    market: str,
    buy_price: float,
    qty: float,
    *,
    code: str = "",
    name: Optional[str] = None,
    board: Optional[str] = None,
    settle_krw: bool = False,
    fx_buy: Optional[float] = None,
    fx_sell: Optional[float] = None,
    dividend: float = 0.0,
    cur_price: Optional[float] = None,
    target_price: Optional[float] = None,
    cgt: bool = False,
    cgt_deduction: float = US_CGT_DEDUCTION,
    avg_includes_fee: bool = False,
) -> Ledger:
    """매입가·수량 → 모든 비용이 0으로 상쇄되는 매도가 원장.

    Args:
        market: "kr" | "us".
        buy_price: 매입 단가(거래통화). 계좌 평단을 그대로 넣어도 된다.
        qty: 수량.
        board: 국내 보드(kospi/kosdaq/konex/etf). None 이면 종목명으로 ETF 만 자동판정.
        settle_krw: 미국주식을 원화 현금흐름(환전 포함)으로 볼지.
        fx_buy/fx_sell: 매수·매도 시점 환율(원/USD). settle_krw 일 때만 쓰인다.
        dividend: 보유 중 받은 배당 **순수령 총액**(정산통화). 손익분기를 낮춘다.
        cur_price: 현재가 → '지금 팔면' 실현 현금손익.
        target_price: 목표가 → 그 가격의 실현 현금손익.
        cgt: 미국 양도소득세(22%)를 시나리오 손익에 반영할지. 손익분기가는 안 움직인다.
        avg_includes_fee: 계좌 평단에 매수수수료가 이미 포함돼 있으면 True(수수료 이중계상 방지).

    Returns:
        Ledger — 유출/유입 라인 + 손익분기가(정확해·호가 올림) + 시나리오.
    """
    market = (market or "kr").lower()
    if buy_price is None or buy_price <= 0 or not qty:
        raise ValueError("매입가(>0)와 수량이 필요합니다.")
    if board is None:
        board = guess_board(name, code) if market == "kr" else "us"
    sch = schedule(market, board, settle_krw=settle_krw and market == "us")

    fxb = float(fx_buy or 0) or 1.0
    fxs = float(fx_sell or fx_buy or 0) or fxb
    if not sch.fx:
        fxb = fxs = 1.0

    cash_out, out_lines = buy_flow(sch, buy_price, qty, fxb)
    warns: list[str] = []
    if avg_includes_fee:
        # 평단에 수수료가 이미 녹아 있으면 매수수수료 줄을 0으로 접는다.
        fee_line = out_lines[1]
        cash_out -= abs(fee_line.amount)
        fee_line.amount = 0.0
        fee_line.note = "평단에 포함된 것으로 간주"

    def net_at(p: float) -> float:
        return sell_flow(sch, p, qty, fxs)[0] + dividend - cash_out

    hi = max(buy_price * 10, buy_price + 1)
    while net_at(hi) < 0 and hi < buy_price * 1e6:
        hi *= 10
    be = _bisect(net_at, 0.0, hi)
    cash_in, in_lines = sell_flow(sch, be, qty, fxs)
    be_tick = tick_up(market, be)

    # 왕복 총비용 = 매수/매도 대금 줄을 뺀 나머지(수수료·세금·환전스프레드)의 절대합.
    gross_out = abs(out_lines[0].amount)
    roundtrip = sum(abs(x.amount) for x in out_lines[1:]) + sum(abs(x.amount) for x in in_lines[1:])

    # 환율효과: 매도환율=매수환율 이라고 두고 다시 풀어, 그 차이만큼을 따로 보고한다.
    fx_effect = 0.0
    if sch.fx and abs(fxs - fxb) > 1e-9:
        be_neutral = _bisect(
            lambda p: sell_flow(sch, p, qty, fxb)[0] + dividend - cash_out, 0.0, hi)
        if be_neutral:
            fx_effect = (be - be_neutral) / buy_price * 100

    led = Ledger(
        market=market, board=sch.board, code=code, name=name, qty=qty,
        buy_price=buy_price, currency=sch.currency, settle_currency=sch.settle_currency,
        fx_buy=(fxb if sch.fx else None), fx_sell=(fxs if sch.fx else None),
        dividend=dividend, outflow=out_lines, inflow=in_lines,
        cash_out=cash_out, cash_in=cash_in + dividend,
        breakeven_price=be, breakeven_tick=be_tick,
        breakeven_pct=(be / buy_price - 1) * 100,
        roundtrip_cost=roundtrip,
        roundtrip_pct=(roundtrip / gross_out * 100) if gross_out else 0.0,
        fx_effect_pct=fx_effect,
        warnings=warns,
    )
    if dividend:
        led.inflow.append(Line("배당(보유 중 수령)", dividend, "손익분기를 낮춘다"))
    if cur_price:
        led.now = _scenario(sch, cur_price, qty, fxs, cash_out, dividend, buy_price,
                            cgt, cgt_deduction, fxb)
    if target_price:
        led.target = _scenario(sch, target_price, qty, fxs, cash_out, dividend, buy_price,
                               cgt, cgt_deduction, fxb)
    if sch.market == "us" and settle_krw and not fx_buy:
        warns.append("환율 미지정 — 원화 정산 라인은 환율 1.00 가정(무의미). --fx 로 넣어라.")
    if sch.market == "us" and not settle_krw:
        warns.append("USD 기준 손익분기 — 환전 스프레드·환율 변동은 빠져 있다(원화로 보려면 환전 포함).")
    if sch.market == "kr" and sch.board != "etf":
        warns.append(f"거래세 {sch.sell_tax_rate * 100:.6g}% 가정 — 요율 개정 시 .env 로 덮어써라.")
    return led


# ── 잔고 전체 스캔 ──────────────────────────────────────────────────
def holding_ledgers(dom=None, ovs=None, *, settle_krw: bool = False,
                    fx: Optional[float] = None, avg_includes_fee: bool = False,
                    dividends: Optional[dict] = None) -> list[Ledger]:
    """계좌 잔고(국내 Balance · 해외 OverseasBalance) → 종목별 손익분기 원장.

    module_KIS 의 잔고 조회 결과를 그대로 받는다(여기서 API 를 다시 부르지 않는다 — P1).
    """
    divs = dividends or {}
    out: list[Ledger] = []
    for h in (dom.holdings if dom else []):
        if not h.avg_price or not h.qty:
            continue
        try:
            out.append(breakeven(
                "kr", h.avg_price, h.qty, code=h.code, name=h.name,
                cur_price=h.cur_price, dividend=float(divs.get(h.code, 0) or 0),
                avg_includes_fee=avg_includes_fee,
            ))
        except ValueError:
            continue
    for h in (ovs.holdings if ovs else []):
        if not h.avg_price or not h.qty:
            continue
        try:
            out.append(breakeven(
                "us", h.avg_price, h.qty, code=h.code, name=h.name,
                cur_price=h.cur_price, settle_krw=settle_krw, fx_buy=fx,
                dividend=float(divs.get(h.code, 0) or 0),
                avg_includes_fee=avg_includes_fee,
            ))
        except ValueError:
            continue
    return out


# ── 렌더 (CLI·GUI 공용 — 표는 여기 한 곳에서만 그린다) ───────────────
def _w(s: str) -> int:
    return sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in s)


def _clip(s: str, width: int) -> str:
    """표시폭 기준 자르기(한글 2폭). 글자수로 자르면 한글 이름에서 열이 밀린다."""
    if _w(s) <= width:
        return s
    out = ""
    for ch in s:
        if _w(out + ch) > width - 1:
            return out + "…"
        out += ch
    return out


def _pad(s: str, width: int, right: bool = False) -> str:
    gap = max(0, width - _w(s))
    return (" " * gap + s) if right else (s + " " * gap)


def _amt(v: float, cur: str) -> str:
    if cur == "KRW":
        return "0원" if abs(v) < 0.5 else f"{v:+,.0f}원"
    return "$0.00" if abs(v) < 0.005 else f"{v:+,.2f}$"


def _price(v: float, cur: str) -> str:
    if cur == "KRW":
        return f"{v:,.0f}원" if abs(v - round(v)) < 1e-6 else f"{v:,.1f}원"
    return f"${v:,.2f}" if abs(v - round(v, 2)) < 1e-9 else f"${v:,.4f}"


_COL = 40


def render(led: Ledger, *, rates: bool = True) -> str:
    """원장을 대차대조표 모양 텍스트로. GUI 도 이 문자열을 그대로 쓴다."""
    cur = led.settle_currency
    who = f"{led.name} ({led.code})" if led.name and led.code else (led.name or led.code or "—")
    head = f"━━ 손익분기 원장 · {who} · {led.qty:,.6g}주 ━━"
    L = [head, ""]
    fxtxt = ""
    if led.fx_buy:
        fxtxt = f" · 환율 매수 {led.fx_buy:,.2f} / 매도 {led.fx_sell:,.2f}"
    L.append(f"매입가 {_price(led.buy_price, led.currency)} · 정산통화 {cur}"
             f" · 보드 {led.board}{fxtxt}")
    L.append("")

    left = [("진입 — 현금유출", None)] + [(x.label, x) for x in led.outflow]
    right = [("청산 — 현금유입 (@ 손익분기)", None)] + [(x.label, x) for x in led.inflow]
    rows = max(len(left), len(right))
    L.append(_pad("  진입 — 현금유출", _COL) + "  청산 — 현금유입 (@ 손익분기)")
    L.append(_pad("  " + "─" * 34, _COL) + "  " + "─" * 34)
    for i in range(1, rows):
        lc = ""
        if i < len(left):
            ln = left[i][1]
            lc = f"  {_pad(ln.label, 14)}{_pad(_amt(ln.amount, cur), 18, right=True)}"
        rc = ""
        if i < len(right):
            rn = right[i][1]
            rc = f"  {_pad(rn.label, 14)}{_pad(_amt(rn.amount, cur), 18, right=True)}"
        L.append(_pad(lc, _COL) + rc)
    L.append(_pad("  " + "─" * 34, _COL) + "  " + "─" * 34)
    L.append(_pad(f"  {_pad('유출 합계', 14)}{_pad(_amt(-led.cash_out, cur), 18, right=True)}", _COL)
             + f"  {_pad('유입 합계', 14)}{_pad(_amt(led.cash_in, cur), 18, right=True)}")
    L.append(_pad("", _COL) + f"  {_pad('⇒ 순현금', 14)}"
             + _pad(_amt(led.cash_in - led.cash_out, cur), 18, right=True))
    L.append("")
    L.append(f"● 손익분기가  {_price(led.breakeven_price, led.currency)}"
             f"  → 실제 호가 {_price(led.breakeven_tick, led.currency)}"
             f"  (매입가 대비 {led.breakeven_pct:+.3f}%)")
    L.append(f"● 왕복 총비용  {_amt(led.roundtrip_cost, cur).lstrip('+')}"
             f"  (매수대금의 {led.roundtrip_pct:.3f}%)")
    if led.fx_effect_pct:
        way = "낮춰" if led.fx_effect_pct < 0 else "높여"
        L.append(f"● 환율효과  매도 {led.fx_sell:,.2f} vs 매수 {led.fx_buy:,.2f}"
                 f" → 손익분기가를 {abs(led.fx_effect_pct):.3f}%p {way}줬다"
                 " (환율이 되돌면 그만큼 되돌아온다)")
    if led.dividend:
        L.append(f"● 배당 {_amt(led.dividend, cur)} 반영 — 그만큼 손익분기가 내려갔다")
    if led.now:
        n = led.now
        L.append(f"● 지금 팔면({_price(n['price'], led.currency)}): 순현금 "
                 f"{_amt(n['pnl'], cur)} ({n['pnl_pct']:+.2f}%)"
                 + (f" · 양도세 {n['cgt_krw']:,.0f}원 반영" if n["cgt_krw"] else ""))
    if led.target:
        t = led.target
        L.append(f"● 목표가({_price(t['price'], led.currency)}): 순현금 "
                 f"{_amt(t['pnl'], cur)} ({t['pnl_pct']:+.2f}%)"
                 + (f" · 양도세 {t['cgt_krw']:,.0f}원 반영" if t["cgt_krw"] else ""))
    if rates:
        L.append("")
        L.append("적용 요율: " + rate_summary(led.market))
    for w in led.warnings:
        L.append(f"⚠ {w}")
    return "\n".join(L)


def rate_summary(market: str) -> str:
    """지금 적용 중인 요율 한 줄(어디서 왔는지 사람이 검증할 수 있게)."""
    if (market or "kr").lower() == "us":
        return (f"위탁 {_num('KIS_FEE_US_PCT'):g}%(최소 ${_num('KIS_FEE_US_MIN'):g}) · "
                f"SEC {_num('KIS_SEC_FEE_PCT'):g}% · TAF ${_num('KIS_TAF_PER_SHARE'):g}/주"
                f"(≤${_num('KIS_TAF_MAX'):g}) · 환전스프레드 {_num('KIS_FX_SPREAD_PCT'):g}%")
    return (f"위탁 {_num('KIS_FEE_KR_PCT'):g}%"
            + (f"(최소 {_num('KIS_FEE_KR_MIN'):,.0f}원)" if _num("KIS_FEE_KR_MIN") else "")
            + f" · 거래세 코스피 {_num('KIS_TAX_KOSPI_PCT'):g}% / 코스닥 "
              f"{_num('KIS_TAX_KOSDAQ_PCT'):g}% / ETF {_num('KIS_TAX_ETF_PCT'):g}%")


def render_scan(leds: list[Ledger]) -> str:
    """잔고 전체 — 종목별 손익분기 vs 현재가 갭 표."""
    if not leds:
        return "보유 종목이 없다(또는 평단·수량 미확인)."
    L = [_pad("종목", 22) + _pad("수량", 8, right=True) + _pad("평단", 14, right=True)
         + _pad("손익분기", 14, right=True) + _pad("현재가", 14, right=True)
         + _pad("갭", 10, right=True) + "  상태",
         "─" * 92]
    for x in leds:
        who = _clip(x.name or x.code or "—", 21)
        curp = (x.now or {}).get("price")
        # 갭은 '실제로 걸 수 있는 호가' 기준 — 표에 찍힌 값과 손으로 계산해도 맞게.
        gap = ((curp / x.breakeven_tick - 1) * 100) if (curp and x.breakeven_tick) else None
        state = "—"
        if gap is not None:
            state = "✅ 비용 넘김" if gap >= 0 else "…비용 미달"
        L.append(
            _pad(who, 22)
            + _pad(f"{x.qty:,.6g}", 8, right=True)
            + _pad(_price(x.buy_price, x.currency), 14, right=True)
            + _pad(_price(x.breakeven_tick, x.currency), 14, right=True)
            + _pad(_price(curp, x.currency) if curp else "—", 14, right=True)
            + _pad(f"{gap:+.2f}%" if gap is not None else "—", 10, right=True)
            + "  " + state
        )
    return "\n".join(L)


def to_dict(led: Ledger) -> dict:
    return asdict(led)


# 표시 헬퍼 공개판(GUI/CLI 가 숫자 포맷을 다시 짜지 않게).
fmt_price = _price
fmt_amount = _amt
