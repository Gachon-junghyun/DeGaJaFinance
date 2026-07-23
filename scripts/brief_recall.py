# -*- coding: utf-8 -*-
"""brief 회수율 감사 — "그날 기사를 정말 다 봤나"를 무작위 표본으로 **재기 가능하게** 만든다.

왜 있나: `brief` 는 "다 읽었다고 말할 수 있게 한다"가 목적인데, 그 주장이 참인지 재는 도구가
없었다. 2026-07-23 처음 재봤을 때 국내기사의 **45.6% 가 브리핑 어디에도 없었다** — 꼬리를
`--body 2` 로 이미 비운 뒤였는데도. 새던 곳은 ①1매체 덩어리(35%) ②비시장 미노출 ③토픽 블롭.
셋 다 수선했고(→ 64.6%), 이 스크립트는 그 수치가 **다른 날에도 유지되는지** 확인하는 회귀 감사다.

방법: 그날 기사의 N%를 무작위로 뽑아, 각 기사가 속한 사건이 브리핑 출력에 실제로 나오는지
대조한다. 표본이므로 오차가 있다 — 20%/300건이면 회수율 표준오차 ±2.7%p 수준.

⚠ 이건 **회수율**(브리핑에 나오나)이지 정확도가 아니다. 사건 제목이 그 기사를 제대로 대표하는지는
   따로 봐야 한다 — 실측으로 「부틸아크릴레이트 반덤핑」이 「美 301조 관세」 사건에 흡수돼
   '회수됨'으로 세어졌으나 실제 브리핑엔 없었다(그래서 `subevents` 가 생겼다).
⚠ 클라이언트 전용(GPU) — `brief` 와 같은 재료를 쓴다.

사용:
    python -X utf8 scripts/brief_recall.py --date 2026-07-23 --scope domestic
    python -X utf8 scripts/brief_recall.py --date 2026-07-23 --frac 0.5 --show-missed 20
"""
from __future__ import annotations

import argparse
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from module_news_data._brief import build                      # noqa: E402
from module_news_data._cluster import cluster_day              # noqa: E402
from module_news_data._config import (FOREIGN_SOURCES, noise_class,  # noqa: E402
                                      utf8_stdout)
from module_news_data._embed import load_vectors               # noqa: E402


def audit(day: str, scope: str, frac: float, seed: int, body_min: int) -> dict:
    b = build(day, scope, body_min=body_min)
    cl = cluster_day(day, scope, with_members=True)

    # 브리핑에 실제로 인쇄되는 제목 = 그 사건이 '보였다'는 뜻
    shown = ({e["title"] for e in b["head"]} | {e["title"] for e in b["body"]}
             | {e["title"] for e in b["tail"]["sample"]}
             | {e["title"] for e in b["excluded_nonmarket"]["sample"]})
    singles_shown = {s["title"] for s in b["single_source"]["sample"]}

    where: dict[str, str] = {}
    for e in cl["events"]:
        tier = "event_shown" if e["title"] in shown else "event_hidden"
        for h in e.get("members", []):
            where[h] = tier
    for s in cl["singles"]:
        where[s["url_hash"]] = ("single_shown" if s["title"] in singles_shown
                                else "single_hidden")

    hashes, meta, _ = load_vectors(day=day)
    pool = [(hashes[i], m) for i, m in enumerate(meta)
            if (scope == "all"
                or ((m["source"] or "") in FOREIGN_SOURCES) == (scope == "foreign"))]
    clean = [(h, m) for h, m in pool if not noise_class(m["title"], m.get("url"))]

    sample = random.Random(seed).sample(clean, max(1, round(len(clean) * frac)))
    tiers, missed = Counter(), []
    for h, m in sample:
        t = where.get(h, "single_hidden")
        tiers[t] += 1
        if t.endswith("hidden"):
            missed.append((t, m["source"], m["title"]))
    vis = tiers["event_shown"] + tiers["single_shown"]
    return {"brief": b, "cl": cl, "n_pool": len(pool), "n_clean": len(clean),
            "n_sample": len(sample), "tiers": tiers, "visible": vis,
            "recall": vis / len(sample), "missed": missed}


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser(description="brief 회수율 감사(무작위 표본 대조)")
    ap.add_argument("--date", required=True)
    ap.add_argument("--scope", choices=["domestic", "foreign", "all"], default="domestic")
    ap.add_argument("--frac", type=float, default=0.20, help="표본 비율(기본 0.20)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--body", type=int, default=2, dest="body_min",
                    help="brief --body 와 같은 값(기본 2 — 파이프라인 규약)")
    ap.add_argument("--show-missed", type=int, default=10, help="못 본 기사 예시 개수")
    a = ap.parse_args()

    r = audit(a.date, a.scope, a.frac, a.seed, a.body_min)
    b, cl = r["brief"], r["cl"]
    d = b["denominator"]

    print(f"\n# brief 회수율 감사 — {a.date} [{a.scope}] --body {a.body_min}")
    print(f"  모집단 {r['n_pool']:,}건 → 뉴스아님 −{r['n_pool']-r['n_clean']:,}"
          f"({', '.join(f'{k} {v}' for k, v in sorted(d['excluded_not_news'].items())) or '없음'})"
          f" → 분모 {r['n_clean']:,}건")
    print(f"  사건 {len(cl['events'])}개(+숨은사건 {cl['n_subevents']}) · "
          f"1매체 덩어리 {cl['n_singles']}개")
    print(f"  브리핑 출력: 머리 {len(b['head'])} · 몸통 {len(b['body'])} · "
          f"꼬리표본 {b['tail']['shown']}/{b['tail']['count']} · "
          f"1매체 {b['single_source']['shown']}/{b['single_source']['count']} · "
          f"비시장경계 {b['excluded_nonmarket']['shown']}/{b['excluded_nonmarket']['count']}")

    print(f"\n  표본 {r['n_sample']:,}건 ({a.frac:.0%}, seed={a.seed}):")
    for t, c in r["tiers"].most_common():
        mark = "✅" if t.endswith("shown") else "❌"
        print(f"    {mark} {t:<15} {c:>5}")
    print(f"\n  회수율 {r['visible']}/{r['n_sample']} = **{r['recall']:.1%}**"
          f"   (2026-07-23 KR 기준선: 수선 전 54.4% → 수선 후 64.6%)")

    if a.show_missed and r["missed"]:
        print(f"\n  못 본 기사 예시 {min(a.show_missed, len(r['missed']))}건 "
              f"— 여기에 매크로 재료가 있으면 `--singles-nb` 를 낮춰라:")
        for t, s, title in r["missed"][:a.show_missed]:
            print(f"    [{t:<13}][{(s or '?')[:10]:<10}] {title[:62]}")
    print(f"\n  ⚠ 회수율이지 정확도가 아니다 — 사건 제목이 그 기사를 대표하는지는 따로 봐야 한다"
          f"(헤더 ⚠).")


if __name__ == "__main__":
    main()
