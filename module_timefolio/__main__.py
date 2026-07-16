"""module_timefolio CLI — 타임폴리오 대회 어댑터.

  python -X utf8 -m module_timefolio account            # NAV/순위/회전율
  python -X utf8 -m module_timefolio holdings           # 보유 비중
  python -X utf8 -m module_timefolio plan               # 책→콘테스트 미러 계획(드라이런)
  python -X utf8 -m module_timefolio sync               # 계획 집행(드라이런 기본)
  python -X utf8 -m module_timefolio sync --execute     # 실제 제출(+ TIMEFOLIO_EXECUTE=1 필요)
  python -X utf8 -m module_timefolio order 067310 --side buy --weight 3.85   # 단건(드라이런)

★ 실제 '주문 제출'은 --execute 와 환경변수 TIMEFOLIO_EXECUTE=1 이 둘 다 있을 때만.
"""
from __future__ import annotations

import argparse
import json
import os

from . import Timefolio
from ._sync import book_targets, build_plan, sync


def _shot_dir() -> str:
    d = os.environ.get("TIMEFOLIO_SHOT_DIR", "").strip()
    return d or os.path.join(os.getcwd(), "llm_outputs", "timefolio")


def cmd_account(args):
    tf = Timefolio.attach()
    a = tf.read_account()
    print(json.dumps(a.__dict__, ensure_ascii=False, indent=2))
    tf.close()


def cmd_holdings(args):
    tf = Timefolio.attach()
    for h in tf.read_holdings():
        print(f"  {h.code} {h.name:12} 비중 {h.weight:5.2f}% 평가 {h.eval_manwon:>8.0f}만 손익 {h.pnl_pct}")
    tf.close()


def cmd_plan(args):
    tf = Timefolio.attach()
    targets = book_targets()
    holdings = tf.read_holdings()
    plans = build_plan(targets, holdings, min_drift=args.min_drift)
    print("책 타깃:", {k: v["weight"] for k, v in targets.items()})
    print("현재 보유:", {h.code: h.weight for h in holdings})
    if not plans:
        print("→ 드리프트 임계 내, 매매 없음")
    for p in plans:
        print(f"  {p.side.upper():4} {p.code} {p.name:12} 주문비중 {p.order_weight:5.2f}% "
              f"(타깃{p.target_w}→현재{p.current_w}) [{p.reason}]")
    tf.close()


def cmd_sync(args):
    os.makedirs(_shot_dir(), exist_ok=True)
    tf = Timefolio.attach()
    out = sync(tf, min_drift=args.min_drift, execute=args.execute, shot_dir=_shot_dir())
    tf.close()
    for r in out["results"]:
        status = "제출됨" if r.get("submitted") else ("드라이런" if r.get("dryrun") else "실패")
        print(f"  [{status}] {r['side'].upper()} {r['code']} {r.get('name','')} "
              f"주문비중 {r['weight']}% {r.get('note','')}")
    if not out["results"]:
        print("→ 매매 없음(드리프트 임계 내)")
    print(json.dumps({"plans": out["plans"]}, ensure_ascii=False))


def cmd_order(args):
    os.makedirs(_shot_dir(), exist_ok=True)
    tf = Timefolio.attach()
    r = tf.place_order(args.code, args.side, args.weight, prc_ty=args.prc,
                       execute=args.execute, shot=os.path.join(_shot_dir(), f"tf_order_{args.code}.jpg"))
    print(json.dumps(r, ensure_ascii=False, indent=2))
    tf.close()


def build_parser():
    p = argparse.ArgumentParser(prog="module_timefolio")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("account").set_defaults(func=cmd_account)
    sub.add_parser("holdings").set_defaults(func=cmd_holdings)
    s = sub.add_parser("plan"); s.add_argument("--min-drift", type=float, default=0.5); s.set_defaults(func=cmd_plan)
    s = sub.add_parser("sync"); s.add_argument("--min-drift", type=float, default=0.5); s.add_argument("--execute", action="store_true"); s.set_defaults(func=cmd_sync)
    s = sub.add_parser("order"); s.add_argument("code"); s.add_argument("--side", choices=["buy", "sell"], required=True); s.add_argument("--weight", type=float, required=True); s.add_argument("--prc", default="Opp"); s.add_argument("--execute", action="store_true"); s.set_defaults(func=cmd_order)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
