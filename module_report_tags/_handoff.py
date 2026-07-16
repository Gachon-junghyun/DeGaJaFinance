# -*- coding: utf-8 -*-
"""인수인계 원장 — REPORT/ 증분 스캔 → 태그 추출 → HANDOFF.md + _tags.json 갱신.

핵심(인수인계 업데이트 방식): 매번 전부 재처리하지 않는다. 파일 mtime을 기억해
새/변경된 리포트만 다시 추출하고, 나머지는 이전 결과를 승계한다. 다운스트림은
매번 재검색·재리포트하지 말고 이 원장(HANDOFF.md)을 읽어 '누가 뭘 말했나'를 인수받는다.
"""
from __future__ import annotations

import json
from datetime import datetime

from ._config import HANDOFF_MD, REPORT_DIR, TAGS_JSON, load_kr_names, load_us_tickers
from ._extract import extract_tags


def _load_ledger() -> dict:
    if TAGS_JSON.exists():
        try:
            return json.loads(TAGS_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"reports": {}, "updated_at": None}


def _desk_of(relpath: str) -> str:
    """리포트 경로 → 데스크 라벨(부모 폴더). 없으면 'root'."""
    parts = relpath.replace("\\", "/").split("/")
    return parts[-2] if len(parts) >= 2 else "root"


def update() -> dict:
    """증분 스캔. 새/변경 리포트만 재추출, 사라진 리포트는 원장에서 제거. 요약 반환."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ledger = _load_ledger()
    reports = ledger.get("reports", {})
    us_tickers = load_us_tickers()
    kr_names = load_kr_names()

    present = {}
    for p in REPORT_DIR.rglob("*.md"):
        if p.name in ("HANDOFF.md",):
            continue
        rel = str(p.relative_to(REPORT_DIR)).replace("\\", "/")
        present[rel] = p
    n_new = n_changed = n_kept = 0

    # 사라진 리포트 제거
    for rel in list(reports.keys()):
        if rel not in present:
            del reports[rel]

    for rel, p in present.items():
        mtime = p.stat().st_mtime
        prev = reports.get(rel)
        if prev and abs(prev.get("mtime", 0) - mtime) < 1e-6:
            n_kept += 1
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        tags = extract_tags(text, us_tickers, kr_names)
        reports[rel] = {"mtime": mtime, "desk": _desk_of(rel), **tags}
        if prev:
            n_changed += 1
        else:
            n_new += 1

    ledger["reports"] = reports
    ledger["updated_at"] = datetime.now().isoformat(timespec="seconds")
    TAGS_JSON.write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding="utf-8")
    _render(ledger)
    return {"new": n_new, "changed": n_changed, "kept": n_kept, "total": len(reports)}


def _render(ledger: dict) -> None:
    """_tags.json → HANDOFF.md (역인덱스: 종목/섹터별 '누가 뭘 말했나')."""
    reports = ledger.get("reports", {})
    # 역인덱스 구성
    by_ticker: dict[str, list] = {}
    by_sector: dict[str, list] = {}
    for rel, r in reports.items():
        for t in r.get("us_tickers", []):
            by_ticker.setdefault(f"{t['ticker']} ({t['name']})", []).append((rel, r))
        for t in r.get("kr_tickers", []):
            by_ticker.setdefault(f"{t['code']} {t['name']}", []).append((rel, r))
        for s in r.get("sectors", []):
            by_sector.setdefault(s, []).append(rel)

    L = ["# REPORT 인수인계 (HANDOFF)", ""]
    L.append(f"_갱신: {ledger.get('updated_at')} · 리포트 {len(reports)}건 · "
             f"종목 {len(by_ticker)} · 섹터 {len(by_sector)}_")
    L.append("")
    L.append("> 다운스트림은 매번 재검색하지 말고 이 표를 읽어라. 각 항목은 '어느 리포트가 "
             "무슨 평결로 이 종목/섹터를 다뤘나'의 인수인계다. 원문은 REPORT/ 해당 경로.")
    L.append("")

    # ── 종목별 (언급 리포트 많은 순) ─────────────────────────────────────
    L.append("## 종목별")
    L.append("")
    L.append("| 종목 | 리포트 수 | 평결 | 최근 리포트 |")
    L.append("|---|---|---|---|")
    for key, entries in sorted(by_ticker.items(), key=lambda x: -len(x[1])):
        verds = sorted({v for _, r in entries for v in r.get("verdicts", [])})
        recent = sorted(entries, key=lambda x: -x[1].get("mtime", 0))[0][0]
        vtxt = " ".join(verds[:5]) if verds else "—"
        L.append(f"| {key} | {len(entries)} | {vtxt} | `{recent}` |")
    L.append("")

    # ── 섹터별 ───────────────────────────────────────────────────────────
    L.append("## 섹터별")
    L.append("")
    for s, rels in sorted(by_sector.items(), key=lambda x: -len(x[1])):
        L.append(f"- **{s}** ({len(rels)}건): " + ", ".join(f"`{r}`" for r in rels[:6]))
    L.append("")

    # ── 리포트 목록 ──────────────────────────────────────────────────────
    L.append("## 리포트 목록 (데스크별)")
    L.append("")
    by_desk: dict[str, list] = {}
    for rel, r in reports.items():
        by_desk.setdefault(r.get("desk", "root"), []).append((rel, r))
    for desk, items in sorted(by_desk.items()):
        L.append(f"### {desk}")
        for rel, r in sorted(items):
            themes = " · ".join(r.get("themes", [])[:2])
            L.append(f"- `{rel}` — {themes}")
        L.append("")

    HANDOFF_MD.write_text("\n".join(L), encoding="utf-8")


def query_ticker(token: str) -> list:
    """종목 토큰(티커/6자리) → 그 종목을 다룬 리포트 목록."""
    ledger = _load_ledger()
    token_u = token.upper()
    out = []
    for rel, r in ledger.get("reports", {}).items():
        hit = any(t["ticker"] == token_u for t in r.get("us_tickers", [])) or \
              any(t["code"] == token for t in r.get("kr_tickers", []))
        if hit:
            out.append({"report": rel, "desk": r.get("desk"),
                        "verdicts": r.get("verdicts", []), "themes": r.get("themes", [])[:3]})
    return out
