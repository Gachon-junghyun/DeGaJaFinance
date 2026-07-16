# FILE: research_Mvp/module_kis/__main__.py
"""CLI 진입점.

사용:
    python -m module_kis 005930                          # 시세 스냅샷
    python -m module_kis 005930 --ohlcv D --count 120    # 일봉 120개
    python -m module_kis 005930 --ohlcv W --count 60      # 주봉
    python -m module_kis 005930 --investor 20            # 외국인/기관 수급 20일
    python -m module_kis 005930 --all                    # 시세+일봉+수급 한 번에
    python -m module_kis 005930 --all --out llm_outputs/kis_005930.md
    python -m module_kis 005930 --json                   # 시세 JSON dump
    python -m module_kis --balance                        # 계좌 잔고(원화+달러)

    # 주문 — 기본 드라이런(미리보기). 실제 발사는 --execute 를 사람이 직접.
    python -m module_kis 005930 --order buy --qty 1 --price 349000      # 미리보기
    python -m module_kis 005930 --order buy --qty 1 --price 349000 --execute  # 실발사
    python -m module_kis 005930 --order sell --qty 1 --market           # 시장가 매도(미리보기)

KIS_APP_KEY / KIS_APP_SECRET 환경변수 필수(.env 또는 셸). 주문/잔고는 KIS_ACCOUNT_NO 도 필요.
KIS_ENV=vps 면 모의투자 도메인 사용.
의존성: requests (mvp 공용). 추가 설치 불필요.
"""
from __future__ import annotations

import argparse
import io
import json
import os
import sys
from pathlib import Path

from ._auth import KisError
from ._account import fetch_balance
from ._account import to_dict as balance_to_dict
from ._chart import fetch_ohlcv
from ._chart import to_dicts as ohlcv_to_dicts
from ._investor import fetch_investor_trend
from ._investor import to_dicts as investor_to_dicts
from ._order import place_order
from ._order import to_dict as order_to_dict
from ._overseas import fetch_overseas_balance
from ._overseas import to_dict as overseas_to_dict
from ._quote import fetch_quote, to_dict
from ._renderer import (
    render_balance,
    render_investor,
    render_ohlcv,
    render_order,
    render_quote,
    render_wallet,
)


def _utf8_stdout() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("utf"):
        return
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            return
        except Exception:
            pass
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def _maybe_load_dotenv() -> None:
    """프로젝트 루트의 .env 를 단순 파싱해 환경변수 주입(module_macro_us 동일 패턴)."""
    if os.environ.get("KIS_APP_KEY") and os.environ.get("KIS_APP_SECRET"):
        return
    here = Path(__file__).resolve().parent
    # 시크릿 단일 원본 = 이 리포 .env (옛 mvp 리포 링크 없음)
    candidates = [here / ".env", here.parent / ".env", here.parent.parent / ".env"]
    for p in candidates:
        if not p.exists():
            continue
        try:
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                k, _, v = line.partition("=")
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k and v and k not in os.environ:
                    os.environ[k] = v
        except Exception:
            pass
        break


def main() -> int:
    _utf8_stdout()
    _maybe_load_dotenv()

    p = argparse.ArgumentParser(prog="module_kis")
    p.add_argument(
        "code",
        nargs="?",
        default=None,
        help="종목 6자리 코드 (예: 005930). --balance 단독 사용 시 생략 가능.",
    )
    p.add_argument(
        "--ohlcv",
        metavar="PERIOD",
        choices=["D", "W", "M", "Y"],
        help="기간별 OHLCV 조회 (D/W/M/Y)",
    )
    p.add_argument("--count", type=int, default=120, help="OHLCV 봉 개수 (기본 120)")
    p.add_argument(
        "--raw-price",
        action="store_true",
        help="OHLCV 원주가(비수정). 기본은 수정주가.",
    )
    p.add_argument(
        "--investor",
        nargs="?",
        type=int,
        const=20,
        default=None,
        metavar="DAYS",
        help="투자자별 수급 조회 (영업일 수, 기본 20)",
    )
    p.add_argument(
        "--balance",
        action="store_true",
        help="계좌 잔고 조회(예수금+보유종목). KIS_ACCOUNT_NO 필요. 종목코드 불필요.",
    )
    p.add_argument(
        "--order",
        metavar="SIDE",
        choices=["buy", "sell"],
        help="현금 주문 buy/sell. 기본 드라이런(미리보기) — 실제 발사는 --execute 동반.",
    )
    p.add_argument("--qty", type=int, help="주문 수량(--order 와 함께)")
    p.add_argument("--price", type=int, help="지정가 단가(원). 미지정+--market 이면 시장가.")
    p.add_argument("--market", action="store_true", help="시장가 주문(--price 무시)")
    p.add_argument(
        "--execute",
        action="store_true",
        help="⚠️ 실제 주문 전송. 없으면 드라이런. 사람이 직접 당기는 트리거.",
    )
    p.add_argument("--all", action="store_true", help="시세+일봉+수급 모두")
    p.add_argument("--json", action="store_true", help="JSON dump (선택한 항목)")
    p.add_argument("--out", default="", help="markdown 저장 경로 (없으면 stdout)")
    args = p.parse_args()

    # 주문 모드 검증.
    if args.order:
        if not args.code:
            p.error("주문엔 종목코드 필요 (예: --order buy 005930 --qty 1 --price 350000).")
        if not args.qty or args.qty <= 0:
            p.error("--order 엔 --qty (1 이상)가 필요합니다.")
        if not args.market and not args.price:
            p.error("지정가 주문은 --price 가 필요합니다. 시장가면 --market.")

    # 종목 단위 플래그가 있으면 code 필수. --balance/--order 는 별도 처리.
    per_ticker = args.all or args.ohlcv or (args.investor is not None)
    if not args.code and not args.balance and not args.order:
        p.error("종목코드가 필요합니다 (예: 005930). 잔고만 보려면 --balance.")
    if per_ticker and not args.code:
        p.error("종목코드가 필요합니다 (예: 005930).")

    want_order = args.order  # None | 'buy' | 'sell'
    # 주문 모드면 시세 자동조회 끔(주문 sanity 체크가 내부에서 시세를 본다).
    want_quote = bool(args.code) and not want_order and (
        args.all or (args.ohlcv is None and args.investor is None)
    )
    want_ohlcv = args.ohlcv or ("D" if args.all else None)
    want_investor = args.investor if args.investor is not None else (20 if args.all else None)
    want_balance = args.balance

    try:
        return _run(args, want_quote, want_ohlcv, want_investor, want_balance, want_order)
    except KisError as e:
        print(f"[kis] {e}", file=sys.stderr)
        return 1
    except Exception as e:  # noqa: BLE001
        print(f"[kis] unexpected: {type(e).__name__}: {e}", file=sys.stderr)
        return 1


def _run(args, want_quote, want_ohlcv, want_investor, want_balance=False,
         want_order=None) -> int:
    code = args.code
    name: str | None = None

    # 주문 모드는 단독 처리(드라이런/실발사).
    if want_order:
        order = place_order(
            want_order, code, args.qty,
            price=args.price, market=args.market, execute=args.execute,
        )
        if args.json:
            print(json.dumps(order_to_dict(order), ensure_ascii=False, indent=2))
        else:
            print(render_order(order))
        return 0

    q = bars = invs = bal = ovs = None
    if want_quote:
        q = fetch_quote(code)
    if want_ohlcv:
        bars, name = fetch_ohlcv(
            code, want_ohlcv, count=args.count, adjusted=not args.raw_price
        )
        if q is not None and not q.name and name:
            q.name = name
    if want_investor is not None:
        invs = fetch_investor_trend(code, days=want_investor)
    if want_balance:
        bal = fetch_balance()
        # 해외/외화 잔고는 best-effort — 해외거래 미활성·모의계좌면 건너뛴다.
        try:
            ovs = fetch_overseas_balance()
        except KisError as e:
            print(f"[kis] 해외잔고 조회 생략: {e}", file=sys.stderr)
            ovs = None

    if args.json:
        dump: dict = {}
        if code:
            dump["code"] = code
        if q is not None:
            dump["quote"] = to_dict(q)
        if bars is not None:
            dump["ohlcv"] = {"period": want_ohlcv, "name": name, "bars": ohlcv_to_dicts(bars)}
        if invs is not None:
            dump["investor"] = investor_to_dicts(invs)
        if bal is not None:
            dump["balance"] = balance_to_dict(bal)
        if ovs is not None:
            dump["overseas"] = overseas_to_dict(ovs)
        print(json.dumps(dump, ensure_ascii=False, indent=2))
        return 0

    parts: list[str] = []
    if bal is not None or ovs is not None:
        parts.append(render_wallet(bal, ovs, env=os.environ.get("KIS_ENV", "prod")))
    if q is not None:
        parts.append(render_quote(q))
    if bars is not None:
        parts.append(render_ohlcv(bars, name, code, want_ohlcv))
    if invs is not None:
        parts.append(render_investor(invs, code, name))
    parts.append(
        "---\n_source: 한국투자증권(KIS) Open API (조회 전용)_\n"
    )
    out = "\n".join(parts)

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(out, encoding="utf-8")
        print(f"saved: {args.out}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
