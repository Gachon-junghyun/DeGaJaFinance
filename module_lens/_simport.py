# -*- coding: utf-8 -*-
"""Import simulation samples (out/sim/<branch>/*.jsonl) into the ledger, re-scored by the live scorer.

Each outcome is re-measured with `_score._Prices` (price-break filter included) before import, so a
sim built on an older or buggy scorer cannot plant a wrong `fired`. Questions that cannot be measured
are dropped. The ledger is copied to data/lens_ledger.before_sim_<stamp>.db first. Re-importing the
same legacy ids is a no-op (import_jsonl is idempotent on identical rows).
"""
from __future__ import annotations

import datetime
import json
import shutil
from pathlib import Path

from module_lens import _ledger
from module_lens._score import _matches, _open_px, _Prices, fred_series, parse_observable

ROOT = Path(__file__).resolve().parents[1]


def import_sim(branches) -> dict:
    con_px = _open_px()
    prices = _Prices(con_px)
    if con_px is not None:
        con_px.close()
    fred = {}

    def value(q):
        o = parse_observable(q["observable"])
        st = str(q["settle"])[:10]
        if o["kind"] == "fred":
            s = fred.setdefault(o["series_id"], sorted((d, float(v)) for d, v in fred_series(o["series_id"]) if v is not None))
            b = [i for i, (d, _) in enumerate(s) if d < st]
            return s[b[-1] + o["h"]][1] - s[b[-1]][1] if b and b[-1] + o["h"] < len(s) else None
        w = prices.window(o["ticker"], st, o["h"])
        if not w:
            return None
        days, b = w
        f = prices.raw if o["kind"] == "px" else prices.excess
        r = f(o["ticker"], days[b], days[b + o["h"]])
        return None if r is None else r * 100

    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy2(ROOT / "data/lens_ledger.db", ROOT / f"data/lens_ledger.before_sim_{stamp}.db")
    report = {}
    for br in branches:
        d = ROOT / "out/sim" / br
        recs = {k: [json.loads(l) for l in open(d / f"{k}.jsonl", encoding="utf-8") if l.strip()]
                for k in ("questions", "evidence", "outcomes")}
        qmap = {q["legacy"]: q for q in recs["questions"]}
        changed = dropped = 0
        keep = set()
        for o in recs["outcomes"]:
            q = qmap[o["legacy"]]
            v = value(q)
            m = [] if v is None else [b["k"] for b in q["branches"] if _matches(b, v)]
            if len(m) != 1:
                dropped += 1
                continue
            changed += m[0] != o["fired"]
            o["fired"], o["value"] = m[0], str(v)
            keep.add(o["legacy"])
        out = d / "work" / "import"
        out.mkdir(parents=True, exist_ok=True)
        files = []
        for k in ("questions", "evidence", "outcomes"):
            rows = [r for r in recs[k] if r["legacy"] in keep]
            for r in rows:
                r.pop("id", None)
                if k != "questions":
                    r["question"] = None
            p = out / f"{k}.jsonl"
            p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
            files.append(p)
        con = _ledger.connect()
        try:
            n = _ledger.import_jsonl(con, files)
            con.commit()
        finally:
            con.close()
        report[br] = dict(total=len(recs["outcomes"]), kept=len(keep), fired_changed=changed,
                          dropped=dropped, imported=n)
    return report
