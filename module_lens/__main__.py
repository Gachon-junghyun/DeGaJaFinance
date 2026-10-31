# -*- coding: utf-8 -*-
"""Question-ledger CLI and the original build/status data commands."""
from __future__ import annotations

import argparse
from importlib import import_module
import json
import sqlite3
import sys

from ._config import PRICE_PERIOD, utf8_stdout
from . import _ledger


class _Parser(argparse.ArgumentParser):
    def error(self, message):
        raise _ledger.LedgerError(message)


def build_parser():
    ap = _Parser(prog="module_lens")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--skip-px", action="store_true")
    b.add_argument("--period", default=PRICE_PERIOD)
    sub.add_parser("status")
    ask = sub.add_parser("ask")
    ask.add_argument("title")
    for name in ("subject", "market", "desk", "settle", "observable"):
        ask.add_argument("--" + name, required=True)
    for name in ("note", "legacy", "asked-at"):
        ask.add_argument("--" + name)
    ev = sub.add_parser("ev")
    ev.add_argument("qid")
    ev.add_argument("method")
    ev.add_argument("reading")
    ev.add_argument("--kind", required=True)
    for name in ("key", "link", "note", "dead"):
        ev.add_argument("--" + name)
    ev.add_argument("--supports", default="")
    ev.add_argument("--weight", type=float, default=0)
    think = sub.add_parser("think")
    think.add_argument("qid")
    think.add_argument("--branch", action="append", required=True)
    think.add_argument("--weights")
    resolve = sub.add_parser("resolve")
    resolve.add_argument("qid")
    resolve.add_argument("fired")
    for name in ("value", "scorer", "note", "link"):
        resolve.add_argument("--" + name)
    sub.add_parser("due").add_argument("--today")
    sub.add_parser("show").add_argument("qid")
    find = sub.add_parser("find")
    find.add_argument("text")
    find.add_argument("--limit", type=int, default=8)
    find.add_argument("--json", action="store_true")
    find.add_argument("--deep", action="store_true", help="의미(임베딩) 검색도 섞는다 — 모델을 올려 몇 초 걸린다")
    sub.add_parser("embed").add_argument("--all", action="store_true")
    sub.add_parser("prior")
    sub.add_parser("export").add_argument("--dir")
    sub.add_parser("import").add_argument("files", nargs="+")
    sub.add_parser("reindex")
    sub.add_parser("hook-prompt")
    sub.add_parser("score").add_argument("--today")
    sub.add_parser("learn")
    sub.add_parser("advise").add_argument("--item", action="append", required=True)
    sub.add_parser("calib")
    return ap


def _dump(value):
    print(json.dumps(value, ensure_ascii=False, indent=1))


def _show(result):
    q = result["question"]
    print(f"{q['id']} legacy={q['legacy'] or '-'} | {q['title']} [{q['status']}]")
    print(f"desk={q['desk']} market={q['market']} subject={q['subject']} asked_at={q['asked_at']}")
    print(f"settle={q['settle']} observable={q['observable']}")
    print("BRANCHES\nk | p (%) | condition | lo | hi")
    for b in q["branches"]:
        print(f"{b['k']} | {b.get('p')} | {b.get('cond', '')} | {b.get('lo')} | {b.get('hi')}")
    print("EVIDENCE\nid | kind | method | reading | supports | weight | dead" +
          (" | cred | beta_mean" if result["has_credit"] else ""))
    for e in result["evidence"]:
        line = f"e{e['id']} | {e['kind']} | {e['method']} | {e['reading']} | {e['supports']} | {e['weight']} | {e['dead']}"
        if result["has_credit"]:
            line += f" | {e['cred']} | {e['beta_mean']}"
        print(line)
    print("OUTCOME")
    _dump(result["outcome"])
    if q["note"]:
        print("NOTE\n" + q["note"])
    if q["link"]:
        print("LINK " + q["link"])


def _optional(cmd):
    module = "._score" if cmd == "score" else "._learn"
    name = "score_due" if cmd == "score" else cmd
    try:
        return getattr(import_module(module, __package__), name)
    except (ImportError, AttributeError):
        print(f"module_lens{module} {name}: not installed")
        return None


def _items(items):
    out = []
    for item in items:
        parts = item.split(":", 2)
        if len(parts) != 3 or ":" not in parts[2]:
            raise _ledger.LedgerError("item must be kind:key:method:supports")
        kind, key, tail = parts
        method, supports = tail.rsplit(":", 1)
        if kind not in _ledger.KINDS or not method.strip():
            raise _ledger.LedgerError("item needs a valid kind and method")
        out.append({"kind": kind, "key": key, "method": method, "supports": supports})
    return out


def _run(a):
    if a.cmd in ("build", "status"):
        from . import _data
        if a.cmd == "build":
            r = _data.build(skip_px=a.skip_px, period=a.period)
            if r.get("prices"):
                miss = r["prices"].pop("missing")
                r["prices"]["missing_n"] = len(miss)
                r["prices"]["missing_head"] = miss[:15]
            _dump(r)
        else:
            _dump(_data.status())
        return 0
    function = None
    if a.cmd in ("score", "learn", "advise", "calib"):
        function = _optional(a.cmd)
        if function is None:
            return 0
    con = _ledger.connect()
    try:
        kw = vars(a).copy()
        kw.pop("cmd")
        if a.cmd in ("ask", "ev", "resolve"):
            _dump(getattr(_ledger, a.cmd)(con, **kw))
        elif a.cmd == "think":
            _dump(_ledger.think(con, a.qid, a.branch, weights=a.weights))
        elif a.cmd == "due":
            for q in _ledger.due(con, a.today):
                print(f"{q['id']} {q['settle']} [{q['form']}] {q['observable']} | {q['title']}")
        elif a.cmd == "show":
            _show(_ledger.show(con, a.qid))
        elif a.cmd == "find":
            from ._search import find, format_find
            vec = None
            if a.deep:
                from ._vec import scores
                vec = scores(con, a.text) or None
            result = find(con, a.text, a.limit, vec_scores=vec)
            _dump(result) if a.json else print(format_find(result))
        elif a.cmd == "export":
            _dump(_ledger.export_jsonl(con, a.dir))
        elif a.cmd == "import":
            _dump(_ledger.import_jsonl(con, a.files))
        elif a.cmd == "embed":
            from ._vec import embed
            _dump(embed(con, all_rows=a.all))
        elif a.cmd == "prior":
            from ._prior import load
            _dump(load(con))
        elif a.cmd == "reindex":
            print(f"reindexed {_ledger.reindex(con)} questions")
        elif a.cmd == "score":
            _dump(function(con, today=a.today))
        elif a.cmd == "advise":
            _dump(function(con, _items(a.item)))
        elif function is not None:
            _dump(function(con))
        con.commit()  # B's score/learn functions deliberately leave commit to callers.
    finally:
        con.close()
    return 0


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args and args[0] == "hook-prompt":
        try:
            utf8_stdout()
            from ._search import hook_prompt
            return hook_prompt(sys.stdin.read())
        except Exception:
            return 0
    utf8_stdout()
    try:
        return _run(build_parser().parse_args(args))
    except (_ledger.LedgerError, ValueError, TypeError, KeyError, OSError, sqlite3.Error) as exc:
        print(" ".join(str(exc).split()), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
