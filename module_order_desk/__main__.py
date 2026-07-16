# FILE: module_order_desk/__main__.py
"""module_order_desk CLI 진입점 — GUI 주문 데스크를 연다.

    python -m module_order_desk
"""
from __future__ import annotations

import sys

from ._desk import main

if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # Windows cp949 콘솔 크래시 방지
    except Exception:
        pass
    main()
