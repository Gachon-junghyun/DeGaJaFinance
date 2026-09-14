# -*- coding: utf-8 -*-
"""md → 근거 레코드 (결정론 수확). 판단 없음 — 있는 것만 옮긴다 (P4).

두 종류를 뽑는다:
  1. **원장 행** (`handoff/*.md` 의 표) — 이미 `ID | 사실 | 값 | 출처 | asof | run` 스키마다.
  2. **리포트 줄** (`REPORT/**.md`) — 숫자 + (출처토큰 or 신뢰태그)가 같은 줄에 있는 줄.

덤으로 **인용 백링크**(어느 리포트가 `M1032` 를 인용했나)와 **ID 점유**(next-id 발급용)를 모은다.
"""
from __future__ import annotations

import re
from pathlib import Path

from ._config import (DART_VIEWER, HEADER_MAP, RE_ACCESSION, RE_DATE, RE_ID_BARE,
                      RE_ID_DECORATED, RE_KR_CODE, RE_RCEPT, RE_SOURCE, RE_TAG,
                      RE_TICKER_TICK, RE_URL, REPO_ROOT)

_SEP = re.compile(r"^\|[\s:|-]*\|$")
_DECOR = re.compile(r"[*`_~]")


def _rel(path: Path) -> str:
    """리포 루트 기준 상대경로(슬래시 고정). 호출자가 상대경로를 넘겨도 견딘다."""
    try:
        return str(Path(path).resolve().relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def _plain(s: str) -> str:
    return _DECOR.sub("", s).strip()


def _cells(line: str) -> list[str] | None:
    s = line.strip()
    if not s.startswith("|"):
        return None
    return [c.strip() for c in s.strip("|").split("|")]


def _map_header(cells: list[str]) -> dict[int, str]:
    """헤더 셀 → 필드 이름. 표마다 열 이름이 달라 키워드 매칭(실측 20종+ 헤더)."""
    out: dict[int, str] = {}
    taken: set[str] = set()
    for i, c in enumerate(cells):
        low = _plain(c).lower()
        for field, keys in HEADER_MAP.items():
            if field in taken:
                continue
            if any(k in low for k in keys):
                out[i] = field
                taken.add(field)
                break
    return out


def _links(text: str) -> str:
    """원자료 링크 — rcept_no 는 DART 뷰어 URL 로 **구성**한다(원장은 번호만 적는다)."""
    found: list[str] = [DART_VIEWER.format(m) for m in RE_RCEPT.findall(text)]
    found += RE_URL.findall(text)
    found += RE_ACCESSION.findall(text)
    return " ".join(list(dict.fromkeys(found))[:4])


def _sources(text: str) -> list[str]:
    return list(dict.fromkeys(m.group(0) for m in RE_SOURCE.finditer(text)))


def _tickers(text: str, kr_names: dict, us_tickers: dict) -> str:
    hits = [c for c in RE_KR_CODE.findall(text) if c in kr_names]
    hits += [t for t in RE_TICKER_TICK.findall(text) if t in us_tickers]
    return ",".join(sorted(set(hits)))


def _id_of(cell: str) -> tuple[str, str, str] | None:
    """셀 첫머리의 ID → (cid, family, market). 장식형 우선, 없으면 셀 맨 앞 맨몸 ID."""
    m = RE_ID_DECORATED.search(cell)
    if not m:
        m = RE_ID_BARE.match(_plain(cell))
    if not m:
        return None
    fam, num, mkt = m.group(1), m.group(2), (m.group(3) or "")
    return f"{fam}{num}{mkt}", fam, mkt.lstrip("-")


def _file_date(text: str) -> str:
    """파일 앞머리의 날짜 = 그 문서의 asof 폴백."""
    m = RE_DATE.search("\n".join(text.splitlines()[:6]))
    return m.group(1) if m else ""


def _market_of(rel: str) -> str:
    up = rel.upper()
    if "_KR" in up or "INDUSTRY_KR" in up:
        return "KR"
    if "_US" in up or "INDUSTRY_US" in up:
        return "US"
    return ""


def harvest_ledger(path: Path, kr_names: dict, us_tickers: dict) -> list[dict]:
    """표 행 → 레코드. ID 있는 행은 `ledger`, 없는 행(종목별 등록부)은 `registry`."""
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    rel = _rel(path)
    fdate = _file_date(text)
    out: list[dict] = []
    hmap: dict[int, str] = {}
    in_table = False
    for i, line in enumerate(lines):
        cells = _cells(line)
        if cells is None:
            in_table, hmap = False, {}
            continue
        if _SEP.match(line.strip()):
            continue
        if not in_table:
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            in_table = True
            if _SEP.match(nxt):
                hmap = _map_header(cells)
                continue                          # 헤더 행 자체는 레코드가 아니다
        ident = _id_of(cells[0]) if cells else None
        rec = {"claim": "", "evidence": "", "source": "", "asof": "", "run": "", "tag": ""}
        spill: list[str] = []
        for j, c in enumerate(cells):
            if j == 0 and ident:
                continue                          # ID 셀은 따로 다룬다
            field = hmap.get(j)
            if field and not rec[field]:
                rec[field] = c
            elif c:
                spill.append(c)
        if not rec["claim"]:
            # 헤더에 「사실/주장」 열이 없는 표(시나리오 표 등)에선 **가장 긴 셀**이 주장이다.
            # 첫 셀을 집으면 `| S97 | 2026-08-21 | … |` 처럼 날짜가 주장 자리에 앉는다.
            rest = [c for c in spill if c]
            if rest:
                best = max(rest, key=len)
                rec["claim"] = best
                spill = [c for c in rest if c is not best]
            else:
                spill = []
        if spill:
            rec["evidence"] = (rec["evidence"] + " · " + " · ".join(spill)).strip(" ·")
        if not rec["claim"] and not rec["evidence"]:
            continue
        tagm = RE_TAG.search(line)
        srcs = _sources(rec["source"]) or _sources(line)
        datem = RE_DATE.search(rec["asof"]) or RE_DATE.search(line)
        out.append({
            "cid": ident[0] if ident else "",
            "family": ident[1] if ident else "",
            "market": (ident[2] if ident else "") or _market_of(rel),
            "claim": rec["claim"],
            "evidence": rec["evidence"],
            "source": rec["source"] or " ".join(srcs)[:120],
            "asof": (datem.group(1) if datem else "") or fdate,
            "run": rec["run"],
            "tag": rec["tag"] or (tagm.group(1).lower() if tagm else ""),
            "link": _links(line),
            "tickers": _tickers(line, kr_names, us_tickers),
            "file": rel, "line": i + 1,
            "kind": "ledger" if ident else "registry",
            "scope": "line", "section": "",       # 원장 행은 Source 열을 자기가 들고 있다
            "raw": line.strip(),
        })
    return out


_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_ROW_LIKE = re.compile(r"^\s*(\||[-*+•]\s|>\s|\d+[.)]\s)")


def harvest_report(path: Path, kr_names: dict, us_tickers: dict) -> list[dict]:
    """리포트 줄 → 레코드. 게이트: **숫자 AND 출처**, 출처는 두 범위 중 하나.

    - `scope='line'` — 출처토큰/신뢰태그가 **그 줄에** 있다.
    - `scope='section'` — 그 줄 위 가장 가까운 **헤더에** 있다(예: `## §A … (module_valuation
      --peers, 조회 2026-08-29)`). 데스크는 출처를 표 캡션에 한 번 쓰고 그 아래 20행을 채우므로,
      이걸 상속하지 않으면 실제로 출처가 있는 숫자를 「무출처」로 읽는다. **다만 상속은
      상속이라고 표시한다** — 줄에 박힌 출처와 같은 무게로 인용하면 그게 세탁이다.
      상속은 표행·불릿에만 적용한다(산문 문단까지 상속하면 헤더 하나가 페이지를 삼킨다).

    코드펜스 안(CLI 예시)은 건너뛴다 — 명령은 주장이 아니다.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = _rel(path)
    fdate = _file_date(text)
    out: list[dict] = []
    fenced = False
    sec_src, sec_date, sec_title = "", "", ""
    for i, line in enumerate(text.splitlines()):
        s = line.strip()
        if s.startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        head = _HEADING.match(s)
        if head:
            title = head.group(2)
            hs = _sources(title)
            sec_title = _plain(title)[:200]
            if hs:
                dm = RE_DATE.search(title)
                sec_src, sec_date = " ".join(hs)[:120], (dm.group(1) if dm else "")
            else:
                sec_src, sec_date = "", ""       # 출처 없는 헤더는 상속을 **끊는다**
            continue
        if not s or _SEP.match(s):
            continue
        if not any(ch.isdigit() for ch in s):
            continue
        tagm = RE_TAG.search(s)
        srcs = _sources(s)
        scope = "line" if (srcs or tagm) else ""
        if not scope and sec_src and _ROW_LIKE.match(line):
            scope, srcs = "section", [sec_src]
        if not scope:
            continue
        cells = _cells(line)
        claim = _plain(cells[0]) if cells and len(cells) > 1 and _plain(cells[0]) else s
        datem = RE_DATE.search(s)
        out.append({
            "cid": "", "family": "", "market": _market_of(rel),
            "claim": claim[:400],
            "evidence": s if claim != s else "",
            "source": " ".join(srcs)[:120],
            "asof": (datem.group(1) if datem else "") or (sec_date if scope == "section" else "") or fdate,
            "run": "",
            "tag": tagm.group(1).lower() if tagm else "",
            "link": _links(s),
            "tickers": _tickers(s, kr_names, us_tickers),
            "file": rel, "line": i + 1, "kind": "report", "scope": scope,
            "section": sec_title, "raw": s,
        })
    return out


def harvest_refs_and_ids(path: Path) -> tuple[list[dict], list[dict]]:
    """(인용 백링크, ID 점유). 점유는 **장식형 ID 만** — 산문의 P50·M2 오인 차단."""
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = _rel(path)
    refs, ids = [], []
    for i, line in enumerate(text.splitlines()):
        for m in RE_ID_DECORATED.finditer(line):
            cid = f"{m.group(1)}{m.group(2)}{m.group(3) or ''}"
            ids.append({"cid": cid, "family": m.group(1), "num": int(m.group(2)),
                        "file": rel, "line": i + 1})
            refs.append({"cid": cid, "file": rel, "line": i + 1,
                         "context": line.strip()[:300]})
    return refs, ids
