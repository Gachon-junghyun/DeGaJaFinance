# -*- coding: utf-8 -*-
"""Run with python -X utf8 -m module_lens._selftest_ledger (temp DBs only)."""
from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
from datetime import date, timedelta
from io import StringIO
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import time
from types import ModuleType
import unittest
from unittest.mock import patch

from . import _ledger as db, _search as search, __main__ as cli
from ._config import utf8_stdout

BRANCHES = ["A:60:up:0:", "B:40:down::0"]


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="lens-ledger-selftest-")
        self.root = Path(self.temp.name)
        self.path = self.root / "lens_ledger.db"
        self.con = db.connect(self.path)
        self.today = date.today()
        self.future = (self.today + timedelta(days=7)).isoformat()

    def tearDown(self):
        self.con.close()
        self.temp.cleanup()

    def question(self, title="알파벳 capex 가이던스 상향 가능성", **kw):
        return db.ask(self.con, title, **dict({"settle": self.future, "subject": "TEST",
                                             "observable": "text:guidance", "desk": "test", "market": "US"}, **kw))

    def evidence(self, qid, method="count estimate revisions", **kw):
        reading = kw.pop("reading", "1 up : 4 down")
        return db.ev(self.con, qid, method, reading, **dict({"kind": "estimates", "supports": "A"}, **kw))

    def resolve(self, qid, fired="A"):
        # Exercise the no-B path without reading any real price DB.
        with patch.dict(sys.modules, {"module_lens._score": None}):
            return db.resolve(self.con, qid, fired)

    def run_cli(self, *args):
        out, err = StringIO(), StringIO()
        with patch.object(db, "LEDGER_DB", self.path), redirect_stdout(out), redirect_stderr(err):
            rc = cli.main(list(args))
        return rc, out.getvalue(), err.getvalue()

    def rejected(self, reason, *args):
        before = list(self.con.iterdump())
        rc, out, err = self.run_cli(*args)
        self.assertEqual((rc, out), (2, ""))
        self.assertEqual(len(err.splitlines()), 1, err)
        self.assertIn(reason, err)
        self.assertEqual(before, list(self.con.iterdump()), "rejection must be atomic")

    def child(self, args, stdin=None):
        env = dict(os.environ, DEGAJA_DATA_DIR=str(self.root), PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run([sys.executable, "-B", "-S", "-X", "utf8", *args],
                              cwd=Path(__file__).resolve().parent.parent, env=env, input=stdin,
                              encoding="utf-8", capture_output=True, timeout=8)

    def test_01_schema_and_numeric_ids(self):
        names = {r[0] for r in self.con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        self.assertTrue({"questions", "evidence", "outcomes", "q_fts", "q_vec", "credit", "impact"} <= names)
        self.assertEqual(self.con.execute("PRAGMA busy_timeout").fetchone()[0], 5000)
        for name in ("q_vec", "credit", "impact"):
            self.assertEqual(self.con.execute(f"SELECT count(*) FROM {name}").fetchone()[0], 0)
        first = self.question(legacy="S1")
        self.assertEqual(first["id"], "Q1")
        self.con.execute("UPDATE questions SET id='Q9' WHERE id='Q1'")
        self.con.commit()
        self.assertEqual(self.question()["id"], "Q10")
        self.assertEqual(self.question()["id"], "Q11")
        with self.assertRaises(db.LedgerError):
            self.question(legacy="S1")
        self.question(legacy=None)
        self.assertEqual(db.reindex(self.con), 4)
        self.assertEqual(self.con.execute("SELECT count(*) FROM q_fts").fetchone()[0], 4)

    def test_02_all_seven_rejection_rules_exit_2(self):
        q = self.question()["id"]
        a = self.evidence(q)
        dead = self.evidence(q, "unavailable method", dead="not published", supports="")
        other = self.question()["id"]
        foreign = self.evidence(other)
        past = self.question(settle=self.today.isoformat())["id"]
        self.evidence(past)
        self.rejected("now >= settle", "think", past, "--branch", "A:100:up")
        self.rejected("p sum", "think", q, "--branch", "A:60:up", "--branch", "B:20:down")
        self.rejected("alive weights", "think", q, "--branch", "A:100:up", "--weights", f"e{a['id']}=99")
        self.rejected("not from", "think", q, "--branch", "A:100:up", "--weights", f"e{foreign['id']}=100")
        self.rejected("dead evidence", "ev", q, "dead method", "nothing", "--kind", "other", "--dead", "absent", "--weight", "1")
        self.rejected("dead evidence", "think", q, "--branch", "A:100:up", "--weights", f"e{a['id']}=100,e{dead['id']}=1")
        db.think(self.con, q, BRANCHES)
        self.rejected("fired", "resolve", q, "C")
        self.resolve(q)
        self.rejected("already has an outcome", "ev", q, "late method", "late", "--kind", "other")

    def test_03_think_equal_explicit_partial_weights_and_backfill(self):
        q = self.question()["id"]
        rows = [self.evidence(q, f"method {i}") for i in range(3)]
        db.think(self.con, q, BRANCHES)
        self.assertAlmostEqual(sum(e["weight"] for e in db.show(self.con, q)["evidence"]), 100)
        weights = {rows[0]["id"]: 50, rows[1]["id"]: 25, rows[2]["id"]: 25}
        db.think(self.con, q, BRANCHES, weights=weights)
        self.assertEqual([e["weight"] for e in db.show(self.con, q)["evidence"]], [50, 25, 25])
        db.think(self.con, q, ["A:99.5:up"], weights={rows[0]["id"]: 49.5})
        self.assertEqual(sum(e["weight"] for e in db.show(self.con, q)["evidence"]), 99.5)
        old = self.question(settle="2000-01-01", backfilled=1)["id"]
        self.evidence(old)
        db.think(self.con, old, ["A:null:unknown", "B:50:down"])
        self.assertIsNone(db.show(self.con, old)["question"]["branches"][0]["p"])
        self.assertEqual(db.parse_branch("A:100:ratio:some:text")["cond"], "ratio:some:text")

    def test_04_resolve_status_fill_outcome_and_optional_import(self):
        for fired, status in (("A", "scored"), ("VOID", "void"), ("AMBIGUOUS", "ambiguous")):
            q = self.question()["id"]
            self.evidence(q)
            db.think(self.con, q, BRANCHES)
            self.resolve(q, fired)
            self.assertEqual(db.get(self.con, q)["status"], status)
        stub = ModuleType("module_lens._score")
        called = []
        def fill(con, qid, px_con=None):
            called.append(qid)
            con.execute("UPDATE outcomes SET brier=0.32 WHERE question=?", (qid,))
            return {}
        stub.fill_outcome = fill
        with patch.dict(sys.modules, {"module_lens._score": stub}):
            outcome = db.resolve(self.con, q, "B")
        self.assertEqual(called, [q])
        self.assertEqual(outcome["brier"], 0.32)
        self.assertEqual(db.get(self.con, q)["status"], "scored")

    def test_05_due_order_form_default_and_closed_exclusion(self):
        old = self.question(settle="2000-01-01 AMC", observable="px:TEST:3")["id"]
        newer = self.question(settle="2000-01-02 BMO")["id"]
        self.question()
        closed = self.question(settle="1999-01-01")["id"]
        self.resolve(closed, "VOID")
        rows = db.due(self.con, "2000-01-02")
        self.assertEqual([r["id"] for r in rows], [old, newer])
        self.assertEqual([r["form"] for r in rows], ["auto", "text"])
        self.assertEqual(len(db.due(self.con)), 2)
        rc, out, err = self.run_cli("due", "--today", "2000-01-02")
        self.assertEqual((rc, err), (0, ""))
        self.assertIn("[auto] px:TEST:3", out)
        self.assertIn("[text]", out)

    def test_06_find_near_duplicate_ranking_and_semantic_union(self):
        self.question("알파벳 capex 광고 실적과 주가 변동성 점검")
        near = self.question("알파벳 capex 가이던스 상향 가능성은 얼마나 될까", legacy="S77")["id"]
        unrelated = self.question("원유 재고와 유가 하락")['id']
        result = search.find(self.con, "알파벳 capex 가이던스 상향 가능성")
        self.assertEqual(result["hits"][0]["id"], near)
        self.assertEqual(result["hits"][0]["legacy"], "S77")
        lexical = result["hits"][0]["score"]
        mixed = search.find(self.con, "알파벳 capex 가이던스 상향 가능성", vec_scores={near: 0.8, unrelated: 1})
        h = next(h for h in mixed["hits"] if h["id"] == near)
        self.assertAlmostEqual(h["score"], 0.5 * lexical + 0.4)
        self.assertIn(unrelated, [h["id"] for h in mixed["hits"]])
        self.assertEqual(search.find(self.con, '" OR * !')['hits'], [])
        self.assertEqual(search.find(self.con, "알파벳", limit=0)["hits"], [])
        self.assertTrue(all(0 <= h["lexical"] <= 1 for h in mixed["hits"]))
        self.con.execute("DELETE FROM q_fts")
        self.con.commit()
        self.assertEqual(search.find(self.con, "알파벳")["hits"], [])
        db.reindex(self.con)
        self.assertTrue(search.find(self.con, "알파벳")["hits"])

    def test_07_method_summary_eligibility_counts_and_labels(self):
        ids = []
        for fired in ("A", "B", "VOID", "AMBIGUOUS", None):
            q = self.question()["id"]
            ids.append(q)
            self.evidence(q, "count revisions", weight=40, backfilled=1)
            self.evidence(q, "read filing", supports="B", weight=60)
            self.evidence(q, "dead method", dead="missing", supports="A")
            self.evidence(q, "zero method", weight=0)
            self.evidence(q, "context method", supports="", weight=0)
            if fired == "A":
                self.evidence(q, "chase headlines", supports="B", weight=10)
                self.con.execute("UPDATE evidence SET weight=50 WHERE question=? AND method='read filing'", (q,))
                self.con.commit()
            db.think(self.con, q, BRANCHES)
            if fired:
                self.resolve(q, fired)
        q = self.question()["id"]
        ids.append(q)
        self.evidence(q, "count revisions", weight=100)
        db.think(self.con, q, BRANCHES)
        self.resolve(q)
        summary = search.method_summary(self.con, ids)
        methods = {m["method"]: m for m in summary["methods"]}
        self.assertEqual(methods["count revisions"], {"method": "count revisions", "uses": 6, "hits": 2, "misses": 1})
        self.assertEqual((methods["read filing"]["uses"], methods["read filing"]["hits"], methods["read filing"]["misses"]), (5, 1, 1))
        for method in ("dead method", "zero method", "context method"):
            self.assertEqual((methods[method]["hits"], methods[method]["misses"]), (0, 0))
        self.assertEqual(summary["single_method_questions"], 1)
        self.assertEqual(summary["best"][0]["method"], "count revisions")
        self.assertEqual(summary["worst"][0], {"method": "chase headlines", "uses": 1, "hits": 0, "misses": 1})
        text = search.format_find(search.find(self.con, "알파벳 capex"))
        for label in ("METHOD SUMMARY", "잘 맞던 방법", "잘 틀리던 방법", "🎲 방법이 하나뿐인 물음 1건"):
            self.assertIn(label, text)

    def test_08_show_evidence_outcome_and_credit(self):
        q = self.question()["id"]
        e = self.evidence(q)
        db.think(self.con, q, BRANCHES)
        self.resolve(q)
        self.con.execute("INSERT INTO credit(level,name,cred,beta_mean) VALUES('method',?,0.2,0.75)", (e["method"],))
        self.con.commit()
        rc, out, err = self.run_cli("show", q)
        self.assertEqual((rc, err), (0, ""))
        for expected in (q, "BRANCHES", "OUTCOME", f"e{e['id']}", "estimates", "cred | beta_mean", "0.2 | 0.75"):
            self.assertIn(expected, out)

    def test_09_export_import_bytes_and_legacy_backfill(self):
        q = self.question(note="긴 노트\n두 번째 줄", legacy="S1")["id"]
        self.evidence(q, reading="한글 · 42", note="multi\nline", weight=100)
        db.think(self.con, q, BRANCHES)
        self.resolve(q)
        self.question()
        dest = self.root / "export1"
        db.export_jsonl(self.con, dest)
        files = [dest / n for n in ("outcomes.jsonl", "evidence.jsonl", "questions.jsonl")]
        other = db.connect(self.root / "roundtrip.db")
        try:
            db.import_jsonl(other, files)  # intentionally reversed dependency order
            db.export_jsonl(other, self.root / "export2")
            for f in files:
                self.assertEqual(f.read_bytes(), (self.root / "export2" / f.name).read_bytes())
                self.assertFalse(f.read_bytes().startswith(b"\xef\xbb\xbf"))
            db.import_jsonl(other, files)  # exported records are idempotent
        finally:
            other.close()
        legacy = [
            {"type": "outcome", "legacy": "S99", "fired": "A", "scored_at": "2001-01-03", "scorer": "backfill"},
            {"type": "evidence", "legacy": "S99", "method": "historical method", "kind": "filing", "weight": 100, "supports": "A"},
            {"type": "question", "legacy": "S99", "title": "옛 물음", "asked_at": "2001-01-01T12:00:00+09:00",
             "settle": "2001-01-02 AMC", "observable": "text:guide", "backfilled": 1,
             "branches": [{"k": "A", "p": 100, "cond": "up", "lo": None, "hi": None}]}]
        f = self.root / "backfill.jsonl"
        f.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in legacy), encoding="utf-8")
        db.import_jsonl(self.con, [f])
        q = self.con.execute("SELECT id,status FROM questions WHERE legacy='S99'").fetchone()
        self.assertEqual(q["status"], "scored")
        self.assertEqual(db.show(self.con, q["id"])["evidence"][0]["backfilled"], 1)
        before = list(self.con.iterdump())
        bad = self.root / "bad.jsonl"
        bad.write_text(json.dumps({"type": "question", "title": "transient"}) + "\n" +
                       json.dumps({"type": "evidence", "question": "Q404", "method": "bad", "kind": "other"}), encoding="utf-8")
        with self.assertRaises(db.LedgerError):
            db.import_jsonl(self.con, [bad])
        self.assertEqual(before, list(self.con.iterdump()))
        self.con.execute("BEGIN")
        self.con.execute("UPDATE questions SET note='uncommitted' WHERE id=?", (q["id"],))
        db.export_jsonl(self.con, self.root / "snapshot")
        self.assertTrue(self.con.in_transaction)
        self.con.rollback()

    def test_10_cli_success_paths_and_json(self):
        args = ["ask", "CLI capex 물음", "--subject", "TEST", "--market", "US", "--desk", "test",
                "--settle", self.future, "--observable", "text:guidance"]
        rc, out, err = self.run_cli(*args)
        self.assertEqual((rc, err), (0, ""))
        qid = json.loads(out)["id"]
        self.assertEqual(self.run_cli("ev", qid, "read guidance", "up", "--kind", "filing", "--supports", "A")[0], 0)
        self.assertEqual(self.run_cli("think", qid, "--branch", "A:100:up")[0], 0)
        with patch.dict(sys.modules, {"module_lens._score": None}):
            self.assertEqual(self.run_cli("resolve", qid, "A", "--value", "up")[0], 0)
        rc, out, err = self.run_cli("find", "CLI capex", "--json", "--limit", "1")
        self.assertEqual((rc, err), (0, ""))
        self.assertEqual(len(json.loads(out)["hits"]), 1)
        dest = self.root / "cli-export"
        self.assertEqual(self.run_cli("export", "--dir", str(dest))[0], 0)
        self.assertEqual(self.run_cli("import", *map(str, sorted(dest.glob("*.jsonl"))))[0], 0)
        self.assertEqual(self.run_cli("reindex")[0], 0)
        self.rejected("required", "ask")

    def test_11_cli_B_wiring_missing_and_persisted_writes(self):
        cases = (("score", "--today", "2000-01-01"), ("learn",),
                 ("advise", "--item", "news:key:method:with colon:A"), ("calib",))
        for args in cases:
            with patch.dict(sys.modules, {"module_lens._score": None, "module_lens._learn": None}):
                rc, out, err = self.run_cli(*args)
            self.assertEqual((rc, err), (0, ""))
            self.assertIn("not installed", out)
        score, learn = ModuleType("module_lens._score"), ModuleType("module_lens._learn")
        calls = []
        def record(con, name, data=None):
            calls.append((name, data))
            con.execute("INSERT INTO impact(kind,key,mult) VALUES(?,?,1)", ("test", name))
            return [] if name != "calib" else {}
        score.score_due = lambda con, today=None, px_con=None, fetch_fred=None: record(con, "score", today)
        learn.learn = lambda con: record(con, "learn")
        learn.advise = lambda con, items: record(con, "advise", items)
        learn.calib = lambda con: record(con, "calib")
        with patch.dict(sys.modules, {"module_lens._score": score, "module_lens._learn": learn}):
            for args in cases:
                self.assertEqual(self.run_cli(*args)[0], 0)
        self.assertEqual(self.con.execute("SELECT count(*) FROM impact").fetchone()[0], 4)
        self.assertEqual(calls[0], ("score", "2000-01-01"))
        self.assertEqual(calls[2][1], [{"kind": "news", "key": "key", "method": "method:with colon", "supports": "A"}])

    def test_12_build_status_original_dispatch_and_lazy_API(self):
        data = ModuleType("module_lens._data")
        calls = []
        def build(skip_px=False, period="2y"):
            calls.append((skip_px, period))
            return {"prices": {"missing": ["TEST"]}}
        data.build, data.status = build, lambda: {"status": "original"}
        with patch.dict(sys.modules, {"module_lens._data": data}):
            rc, out, err = self.run_cli("build", "--skip-px", "--period", "1y")
            self.assertEqual((rc, err), (0, ""))
            self.assertEqual(json.loads(out), {"prices": {"missing_n": 1, "missing_head": ["TEST"]}})
            self.assertEqual(calls, [(True, "1y")])
            self.assertEqual(json.loads(self.run_cli("status")[1]), {"status": "original"})
        child = self.child(["-c", "import module_lens,sys; assert 'module_lens._data' not in sys.modules; "
                            "from module_lens import ledger_connect,find; import module_lens.__main__; "
                            "assert not any(n in sys.modules for n in ('pandas','numpy','requests','feedparser','bs4')); "
                            "print('stdlib-only lazy import OK')"])
        self.assertEqual(child.returncode, 0, child.stderr)
        self.assertIn("stdlib-only lazy import OK", child.stdout)

    def test_13_hook_empty_missing_bad_json_and_errors_are_silent(self):
        for raw in ('{"prompt":"알파벳 capex 가이던스"}', "bad JSON", "[]", '{"prompt":42}'):
            with patch.object(search, "LEDGER_DB", self.path), redirect_stdout(StringIO()) as out:
                self.assertEqual(search.hook_prompt(raw), 0)
            self.assertEqual(out.getvalue(), "")
        for path in (self.root / "missing.db", self.root / "broken.db"):
            if path.name == "broken.db":
                path.write_bytes(b"not SQLite")
            with patch.object(search, "LEDGER_DB", path), redirect_stdout(StringIO()) as out:
                self.assertEqual(search.hook_prompt('{"prompt":"알파벳 capex 가이던스"}'), 0)
            self.assertEqual(out.getvalue(), "")
        with patch.object(sys, "stdin", StringIO("invalid")):
            self.assertEqual(self.run_cli("hook-prompt")[0], 0)
        self.assertFalse((self.root / "missing.db").exists())

    def test_14_hook_threshold_calibration(self):
        self.question()
        positives = ["알파벳 capex 가이던스 상향 가능성", "알파벳 capex 가이던스가 상향될 가능성",
                     "알파벳 capex 가이던스 상향 가능성을 확인해줘"]
        negatives = ["알파벳 광고 매출과 검색 점유율", "capex unrelated cooking recipe",
                     "원유 재고와 유가 하락을 살펴봐", "오늘 날씨와 주말 여행 계획"]
        scores = []
        for prompt, expected in [(p, True) for p in positives] + [(p, False) for p in negatives]:
            result = search.find(self.con, prompt)
            scores.append((expected, result["hits"][0]["score"] if result["hits"] else 0))
            with patch.object(search, "LEDGER_DB", self.path), redirect_stdout(StringIO()) as out:
                self.assertEqual(search.hook_prompt(json.dumps({"prompt": prompt})), 0)
            self.assertEqual(bool(out.getvalue()), expected, (prompt, scores[-1]))
            self.assertLessEqual(len(out.getvalue().splitlines()), 6)
            self.assertTrue(all(line.startswith("📒 module_lens —") for line in out.getvalue().splitlines()))
        self.assertGreaterEqual(min(s for positive, s in scores if positive), search.HOOK_MIN)
        self.assertLess(max(s for positive, s in scores if not positive), search.HOOK_MIN)

    def test_15_hook_2000_rows_cold_process_under_two_seconds(self):
        now = db._now()
        self.con.executemany("INSERT INTO questions(id,title,asked_at,created,updated) VALUES(?,?,?,?,?)",
                             [(f"Q{i}", f"알파벳 capex 일반 조사 기록 {i}", now, now, now) for i in range(1, 2000)])
        self.con.commit()
        target = self.question()["id"]
        db.reindex(self.con)
        self.assertEqual(self.con.execute("SELECT count(*) FROM questions").fetchone()[0], 2000)
        self.assertEqual(len(search._candidates(self.con, "알파벳 capex")), 300)
        start = time.perf_counter()
        child = self.child(["-m", "module_lens", "hook-prompt"], json.dumps({"prompt": "알파벳 capex 가이던스 상향 가능성"}))
        elapsed = time.perf_counter() - start
        self.assertEqual((child.returncode, child.stderr), (0, ""))
        self.assertIn(target, child.stdout)
        self.assertLessEqual(len(child.stdout.splitlines()), 6)
        self.assertLess(elapsed, 2.0)
        print(f"\nHOOK 2000 rows: {elapsed:.3f}s cold process; 300 candidates; {len(child.stdout.splitlines())} lines", flush=True)
        self.con.execute("BEGIN EXCLUSIVE")
        try:
            start = time.perf_counter()
            locked = self.child(["-m", "module_lens", "hook-prompt"], '{"prompt":"알파벳 capex 가이던스"}')
            self.assertLess(time.perf_counter() - start, 2.0)
            self.assertEqual((locked.returncode, locked.stdout, locked.stderr), (0, "", ""))
        finally:
            self.con.rollback()

    def test_16_installed_B_integration_on_temp_price_DB(self):
        try:
            from . import _score, _learn
        except ImportError:
            self.skipTest("B not installed (guarded CLI paths tested separately)")
        # A tiny in-memory price source, no real ledger or price data touched.
        px = sqlite3.connect(":memory:")
        try:
            px.executescript("CREATE TABLE universe(ticker,market,name,sector); CREATE TABLE px(ticker,date,close);")
            px.executemany("INSERT INTO universe VALUES(?,?,?,?)", [("TEST", "US", "test", "test"), ("PEER", "US", "peer", "test")])
            px.executemany("INSERT INTO px VALUES(?,?,?)", [(ticker, day, value) for ticker in ("TEST", "PEER")
                           for day, value in (("2000-01-03", 100), ("2000-01-04", 110), ("2000-01-05", 120))])
            q = self.question(settle="2000-01-04", observable="px:TEST:1", backfilled=1)["id"]
            self.evidence(q)
            db.think(self.con, q, BRANCHES)
            results = _score.score_due(self.con, today="2000-01-05", px_con=px)
            self.con.commit()
            self.assertTrue(results)
            self.assertEqual(db.show(self.con, q)["outcome"]["fired"], "A")
            self.assertAlmostEqual(db.show(self.con, q)["outcome"]["brier"], 0.32)
            self.assertEqual(self.run_cli("learn")[0], 0)
            self.assertTrue(db.show(self.con, q)["has_credit"])
            rc, out, err = self.run_cli("advise", "--item", "estimates:key:count estimate revisions:A")
            self.assertEqual((rc, err), (0, ""))
            self.assertAlmostEqual(sum(item["weight"] for item in json.loads(out)), 100)
            self.assertIsInstance(json.loads(self.run_cli("calib")[1]), dict)
            with patch.object(_score, "_open_px", return_value=None):
                self.assertEqual(self.run_cli("score", "--today", "2000-01-05")[0], 0)
                self.assertEqual(self.run_cli("resolve", q, "B")[0], 0)
            self.assertAlmostEqual(db.show(self.con, q)["outcome"]["brier"], 0.72)
        finally:
            px.close()


def main():
    utf8_stdout()
    result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(unittest.defaultTestLoader.loadTestsFromTestCase(LedgerTests))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
