"""module_timefolio CLI — 타임폴리오 대회 어댑터.

  python -X utf8 -m module_timefolio account            # NAV/순위/회전율
  python -X utf8 -m module_timefolio holdings           # 보유 비중
  python -X utf8 -m module_timefolio plan               # 책→콘테스트 미러 계획(드라이런)
  python -X utf8 -m module_timefolio sync               # 계획 집행(드라이런 기본)
  python -X utf8 -m module_timefolio sync --execute     # 실제 제출(+ TIMEFOLIO_EXECUTE=1 필요)
  python -X utf8 -m module_timefolio order 067310 --side buy --weight 3.85   # 단건(드라이런)

★ 실제 '주문 제출'은 --execute 와 환경변수 TIMEFOLIO_EXECUTE=1 이 둘 다 있을 때만.

★ --port (기본 9222 · env TIMEFOLIO_CDP_PORT) — 2026-08-07 추가.
  포트가 고정이라 **다른 크롬이 9222 를 먼저 잡으면 전 서브커맨드가 CDPError 로 죽었다**.
  `start_timefolio_chrome.bat` 은 9222 가 LISTENING 이면 점유자를 확인하지 않고 skip 하므로
  그 상태가 조용히 만들어진다. 타임폴리오 프로필을 다른 포트로 띄웠으면 여기 그 포트를 준다:
    python -X utf8 -m module_timefolio holdings --port 9223
"""
from __future__ import annotations

import argparse
import json
import os

from . import Timefolio
from ._sync import SyncBlocked, build_plan, plan_targets, sync


def _shot_dir() -> str:
    d = os.environ.get("TIMEFOLIO_SHOT_DIR", "").strip()
    return d or os.path.join(os.getcwd(), "llm_outputs", "timefolio")


def cmd_account(args):
    tf = Timefolio.attach(port=args.port)
    a = tf.read_account()
    print(json.dumps(a.__dict__, ensure_ascii=False, indent=2))
    tf.close()


def cmd_holdings(args):
    tf = Timefolio.attach(port=args.port)
    for h in tf.read_holdings():
        print(f"  {h.code} {h.name:12} 비중 {h.weight:5.2f}% 평가 {h.eval_manwon:>8.0f}만 손익 {h.pnl_pct}")
    tf.close()


def cmd_plan(args):
    try:
        targets, exp = plan_targets()
    except SyncBlocked as e:                    # 소리 내어 멈춘다 — 조용한 폴백 금지
        print(f"🚨 계획 불가\n{e}")
        return 1
    tf = Timefolio.attach(port=args.port)
    holdings = tf.read_holdings()
    tf.close()
    if not holdings:
        print("🚨 보유 조회 0건 — 파서 회귀 의심. 스크린샷 대조 전엔 계획을 내지 않는다.")
        return 1
    cash = targets["_cash"]
    print(f"노출 규칙: **{exp['state']}** (asof {exp['asof']} · {exp.get('bar_status','')}) "
          f"⇒ 투자 {exp['invested_target_pct']}% / 현금 {cash['weight']}%")
    for nt in cash.get("cap_notes", []):
        print(f"  🚨 종목상한 적용: {nt}")
    print("타깃:", {k: v["weight"] for k, v in targets.items() if not k.startswith("_")})
    print("현재 보유:", {h.code: h.weight for h in holdings},
          f"(투자 합계 {sum(h.weight for h in holdings):.1f}%)")
    plans = build_plan(targets, holdings, min_drift=args.min_drift)
    if not plans:
        print("→ 드리프트 임계 내, 매매 없음")
    for p in plans:
        print(f"  {p.side.upper():4} {p.code} {p.name:12} 주문비중 {p.order_weight:5.2f}% "
              f"(타깃{p.target_w}→현재{p.current_w}) [{p.reason}]")
    print("\n⚠ 계획일 뿐이다. 제출은 사람이 `--execute` 로 한다"
          " — 그리고 arming(TIMEFOLIO_EXECUTE)이 이미 켜져 있는지 먼저 확인하라.")
    return 0


def cmd_sync(args):
    os.makedirs(_shot_dir(), exist_ok=True)
    tf = Timefolio.attach(port=args.port)
    try:
        out = sync(tf, min_drift=args.min_drift, execute=args.execute, shot_dir=_shot_dir())
    except SyncBlocked as e:
        tf.close()
        print(f"🚨 동기화 불가\n{e}")
        return 1
    tf.close()
    e = out["exposure"]
    print(f"노출 규칙: **{e['state']}** ⇒ 투자 {e['invested_target_pct']}% "
          f"/ 현금 {out['targets']['_cash']['weight']}%")
    for r in out["results"]:
        status = "제출됨" if r.get("submitted") else ("드라이런" if r.get("dryrun") else "실패")
        print(f"  [{status}] {r['side'].upper()} {r['code']} {r.get('name','')} "
              f"주문비중 {r['weight']}% {r.get('note','')}")
    if not out["results"]:
        print("→ 매매 없음(드리프트 임계 내)")
    print(json.dumps({"plans": out["plans"]}, ensure_ascii=False))


def cmd_order(args):
    os.makedirs(_shot_dir(), exist_ok=True)
    tf = Timefolio.attach(port=args.port)
    r = tf.place_order(args.code, args.side, args.weight, prc_ty=args.prc,
                       execute=args.execute, shot=os.path.join(_shot_dir(), f"tf_order_{args.code}.jpg"))
    print(json.dumps(r, ensure_ascii=False, indent=2))
    tf.close()


def build_parser():
    p = argparse.ArgumentParser(prog="module_timefolio")
    # ⚠ 포트는 모든 서브커맨드가 공유한다 — 전용 프로필이 9222 를 못 잡는 상황이 실제로 있었다.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--port", type=int,
                        default=int(os.environ.get("TIMEFOLIO_CDP_PORT", "9222")),
                        help="CDP 원격 디버깅 포트(기본 9222 · env TIMEFOLIO_CDP_PORT)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("account", parents=[common]).set_defaults(func=cmd_account)
    sub.add_parser("holdings", parents=[common]).set_defaults(func=cmd_holdings)
    s = sub.add_parser("plan", parents=[common]); s.add_argument("--min-drift", type=float, default=0.5); s.set_defaults(func=cmd_plan)
    s = sub.add_parser("sync", parents=[common]); s.add_argument("--min-drift", type=float, default=0.5); s.add_argument("--execute", action="store_true"); s.set_defaults(func=cmd_sync)
    s = sub.add_parser("order", parents=[common]); s.add_argument("code"); s.add_argument("--side", choices=["buy", "sell"], required=True); s.add_argument("--weight", type=float, required=True); s.add_argument("--prc", default="Opp"); s.add_argument("--execute", action="store_true"); s.set_defaults(func=cmd_order)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
