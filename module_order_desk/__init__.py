# FILE: module_order_desk/__init__.py
"""module_order_desk — KIS 주문 데스크(Tkinter GUI) + 반사실 결정 추적/계획 스택.

주문을 '스택'에 카드로 쌓아 카드마다 [체결]로 하나씩 사람이 발사한다(자동매매 아님,
확인 다이얼로그 1회). 시세·잔고·주문 로직은 module_KIS 재사용(복제 없음, P1). 흐름창은
`python -m module_flow` 서브프로세스로 수급을 조회한다.

거래비용(수수료·세금·환전)의 단일 원본은 `_costs` — '순현금 0'이 되는 매도가를 여기서만 푼다.

실행:
    python -m module_order_desk      # GUI 실행 (cwd=리포 루트)
    python -m module_order_desk breakeven 005930 --qty 10 --price 70000   # 손익분기 원장
    또는 run_kis_desk.bat 더블클릭

요구: 리포 루트 .env 에 KIS_APP_KEY/SECRET + KIS_ACCOUNT_NO. KIS_ENV=prod=실전(실제 돈).
공개 API:
    from module_order_desk import KisDesk, main
"""
from ._desk import KisDesk, main
from . import _costs as costs
from . import _decisions as decisions
from . import _stack as stack
from ._costs import FeeSchedule, Ledger, breakeven, holding_ledgers, render, render_scan

__all__ = [
    "KisDesk", "main", "decisions", "stack",
    # 거래비용·손익분기 (P1 단일 원본)
    "costs", "breakeven", "holding_ledgers", "render", "render_scan",
    "Ledger", "FeeSchedule",
]
