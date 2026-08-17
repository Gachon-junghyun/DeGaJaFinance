# FILE: module_order_desk/__main__.py
"""module_order_desk CLI 진입점.

    python -m module_order_desk                 # GUI 주문 데스크
    python -m module_order_desk breakeven ...   # 손익분기(거래비용 원장) — 창 없이 계산만
"""
from __future__ import annotations

import argparse
import json
import sys

from ._desk import main as gui_main  # import 시 .env 로드(단일 원본: _desk._load_dotenv)


def _breakeven(a) -> int:
    from module_KIS import KisError

    from . import _costs as costs

    market = a.market or ("kr" if (a.code or "").isdigit() else "us")
    code = a.code.upper() if market == "us" else a.code
    name, cur, avg, qty = None, None, a.price, a.qty

    if a.scan or avg is None or qty is None:
        # 계좌에서 평단·수량·현재가를 가져온다(조회 전용 — 주문 아님).
        dom = ovs = None
        try:
            from module_KIS import fetch_balance, fetch_overseas_balance
            dom = fetch_balance()
            try:
                ovs = fetch_overseas_balance()
            except KisError:
                ovs = None
        except KisError as e:
            print(f"계좌 조회 실패: {e}")
            if avg is None:
                return 2

        if a.scan:
            leds = costs.holding_ledgers(dom, ovs, settle_krw=a.krw, fx=a.fx,
                                         avg_includes_fee=a.avg_includes_fee)
            if a.json:
                print(json.dumps([costs.to_dict(x) for x in leds],
                                 ensure_ascii=False, indent=2))
            else:
                print(costs.render_scan(leds))
                print(f"\n적용 요율(국내): {costs.rate_summary('kr')}")
                print(f"적용 요율(미국): {costs.rate_summary('us')}")
            return 0

        pool = (ovs.holdings if (market == "us" and ovs) else (dom.holdings if dom else []))
        h = next((x for x in pool if (x.code or "").upper() == code.upper()), None)
        if h:
            name = h.name
            avg = avg if avg is not None else h.avg_price
            qty = qty if qty is not None else h.qty
            cur = h.cur_price

    if avg is None:
        print("매입가를 못 찾았다 — --price 로 직접 넣어라(계좌에 없는 종목이면 평단이 없다).")
        return 2
    if cur is None and not a.no_quote:
        try:
            from module_KIS import fetch_quote, fetch_us_quote
            cur = (fetch_us_quote(code).price if market == "us"
                   else fetch_quote(code).price)
        except Exception:  # noqa: BLE001 — 시세가 없어도 손익분기는 계산된다
            cur = None

    led = costs.breakeven(
        market, avg, qty or 1, code=code, name=name,
        board="etf" if a.etf else (None if market == "kr" else "us"),
        settle_krw=a.krw, fx_buy=a.fx, fx_sell=a.fx_sell, dividend=a.dividend or 0.0,
        cur_price=cur, target_price=a.target, cgt=a.cgt,
        avg_includes_fee=a.avg_includes_fee,
    )
    print(json.dumps(costs.to_dict(led), ensure_ascii=False, indent=2)
          if a.json else costs.render(led))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="python -m module_order_desk",
        description="KIS 주문 데스크 — 인자 없으면 GUI, 서브커맨드는 계산 전용(주문 안 나감).",
    )
    sub = p.add_subparsers(dest="cmd")
    b = sub.add_parser(
        "breakeven", aliases=["be"],
        help="손익분기: 수수료·세금·환전까지 순현금이 0이 되는 매도가",
    )
    b.add_argument("code", nargs="?", default="", help="종목코드(6자리) 또는 미국 티커")
    b.add_argument("--market", choices=["kr", "us"], default=None,
                   help="미지정 시 코드 형태로 자동판별(숫자=국내)")
    b.add_argument("--qty", type=float, default=None, help="수량(미지정 시 계좌 보유수량)")
    b.add_argument("--price", type=float, default=None, help="매입가(미지정 시 계좌 평단)")
    b.add_argument("--target", type=float, default=None, help="목표가 시나리오")
    b.add_argument("--dividend", type=float, default=0.0, help="보유 중 받은 배당 순수령 총액")
    b.add_argument("--etf", action="store_true", help="국내 ETF/ETN(증권거래세 면제)")
    b.add_argument("--krw", action="store_true", help="미국주식을 원화 현금흐름(환전 포함)으로")
    b.add_argument("--fx", type=float, default=None, help="매수 환율(원/$)")
    b.add_argument("--fx-sell", type=float, default=None, help="매도(청산) 환율 — 기본 --fx 와 동일")
    b.add_argument("--cgt", action="store_true", help="미국 양도세 22% 를 시나리오 손익에 반영")
    b.add_argument("--avg-includes-fee", action="store_true",
                   help="계좌 평단에 매수수수료가 이미 포함된 경우(이중계상 방지)")
    b.add_argument("--scan", action="store_true", help="보유 종목 전체 손익분기 표")
    b.add_argument("--no-quote", action="store_true", help="현재가 조회 생략(오프라인 계산)")
    b.add_argument("--json", action="store_true", help="JSON 출력")
    return p


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # Windows cp949 콘솔 크래시 방지
    except Exception:
        pass
    args = build_parser().parse_args()
    if args.cmd in ("breakeven", "be"):
        if not args.code and not args.scan:
            print("종목코드가 필요하다(또는 --scan 으로 보유 전체).")
            raise SystemExit(2)
        raise SystemExit(_breakeven(args))
    gui_main()


if __name__ == "__main__":
    main()
