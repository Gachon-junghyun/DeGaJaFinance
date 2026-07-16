"""CLI 진입점.  사용:  python -m module_text_chart <ticker>"""
from __future__ import annotations

import sys

from ._make_chart import save_text_chart


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print("usage: python -m module_text_chart <ticker> [--read]   (예: 005930.KS)")
        sys.exit(1)
    if "--read" in flags:
        # CHART_READ 블록만 출력 — 에이전트 브리프 임베드용
        from ._ohlcv import fetch_ohlcv
        from ._metadata import generate_chart_read
        df = fetch_ohlcv(args[0])
        if df.empty:
            print(f"OHLCV 데이터 없음: {args[0]}")
            sys.exit(1)
        try:
            print(generate_chart_read(df))
        except Exception as exc:  # noqa: BLE001
            print(f"(CHART_READ 생성 실패: {exc!r})")
            sys.exit(1)
        return
    saved = save_text_chart(args[0])
    print(f"saved: {saved}")


if __name__ == "__main__":
    main()
