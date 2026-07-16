"""CLI: python -m module_industry_map "{seed1}" "{seed2}" [--clusters 6] [--top-n 30] [--out FILE]"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import extract, render_markdown


def main() -> int:
    parser = argparse.ArgumentParser(prog="module_industry_map")
    parser.add_argument("seeds", nargs="+", help="thesis 시드 키워드 (1개 이상)")
    parser.add_argument("--top-n", type=int, default=30, help="corp pool 상위 N (default 30)")
    parser.add_argument("--clusters", type=int, default=6, help="가치사슬 cluster 개수 (default 6)")
    parser.add_argument("--expand-top-k", type=int, default=25, help="자동 확장 키워드 top-K (default 25)")
    parser.add_argument("--out", type=str, help="출력 파일 경로. 미지정 시 stdout.")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    extracted = extract(
        args.seeds,
        top_n=args.top_n,
        n_clusters=args.clusters,
        expand_top_k=args.expand_top_k,
    )
    md = render_markdown(extracted)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        print(f"[module_industry_map] wrote {out_path}", file=sys.stderr)
    else:
        sys.stdout.write(md)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
