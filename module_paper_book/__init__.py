# -*- coding: utf-8 -*-
"""module_paper_book — 데스크 리포트를 읽어 굴리는 모의투자(paper) 장부 엔진.

산업/기업 데스크가 만든 리포트(BET_SHEET·ACTION_TICKETS·평결)를 읽어(_intake),
리스크 기반으로 사이징(_risk)하고, 체결을 시뮬레이션해 장부(_book)에 반영하며,
시가평가(_mark)·결정저널/트랙레코드(_journal)를 남긴다.

설계 철학(리포 규약과 동형):
  · 판단은 상위(프로토콜 paper_desk)가, 이 모듈은 결정론 기계만 제공 (P4).
  · 시세·주문 로직은 재사용 (P1): 마크는 module_KIS(KR)/yfinance(US), 리포트 태그는
    module_report_tags. 같은 기능을 다시 구현하지 않는다.
  · 체결은 기본 드라이런 — CLI `--commit` 을 사람이 명시할 때만 장부를 바꾼다 (주문
    계열 안전규약과 동형). 스케줄러 자동발사 코드는 만들지 않는다. 이건 '모의'라
    실제 주문은 없다 — commit 은 장부 시뮬레이션 반영일 뿐.

공개 API:
    from module_paper_book import (
        connect, init_db, get_positions, record_fill, Fill, book_summary,   # _book
        read_actionable, Candidate,                                          # _intake
        size_position, RiskParams, concentration_check,                      # _risk
        mark_book, get_price, position_pnl,                                  # _mark
        log_decision, track_record,                                          # _journal
    )

CLI:
    python -m module_paper_book init [--capital-krw N --capital-usd N --reset]
    python -m module_paper_book intake [--dir REPORT]        # 리포트 → 후보 원장
    python -m module_paper_book status                       # 장부 시가평가
    python -m module_paper_book size AVGO --price 393 --stop 360 [--core]
    python -m module_paper_book fill --ticker AVGO --side buy --qty 3 --price 393 [--commit]
    python -m module_paper_book mark                         # 마크+스탑히트+집중도
    python -m module_paper_book snapshot [--fx 1380 --note "..."]
    python -m module_paper_book journal [--limit 20] | track

랩어카운트(wrap) 계열 — 섹터 만다트로 굴리는 일임 규율 (_allocate):
    python -m module_paper_book mandate --set '{"Information Technology":30}' --market us --band 5
    python -m module_paper_book mandate --map TSM="Information Technology" --target-beta 1.0
    python -m module_paper_book drift                       # 섹터 괴리(pp) + 책 베타
    python -m module_paper_book rebalance                   # 밴드 복원 계획(드라이런)
    python -m module_paper_book rebalance --commit          # 계획을 모의장부에 반영(사람만)
"""
from ._allocate import (
    BENCH,
    book_beta,
    compute_betas,
    get_mandate,
    position_weights,
    rebalance_plan,
    resolve_sector,
    sector_drift,
    set_mandate,
)
from ._book import (
    Fill,
    Position,
    book_summary,
    connect,
    equity_krw,
    get_cash,
    get_position,
    get_positions,
    init_db,
    record_fill,
    snapshot_equity,
)
from ._config import DB_FILENAME, default_db_path, market_of, utf8_stdout
from ._intake import Candidate, read_actionable, summarize
from ._journal import log_decision, recent, track_record
from ._mark import get_price, mark_book, position_pnl, price_move
from ._mirror import (
    MirrorPosition,
    apply_mirror,
    learned_sensitivity,
    record_sensitivity,
    seed_position,
    stage_to_kis,
)
from ._risk import RiskParams, concentration_check, size_position, theme_exposure

__all__ = [
    "Fill", "Position", "book_summary", "connect", "equity_krw", "get_cash", "get_position",
    "get_positions", "init_db", "record_fill", "snapshot_equity",
    "BENCH", "book_beta", "compute_betas", "get_mandate", "position_weights",
    "rebalance_plan", "resolve_sector", "sector_drift", "set_mandate",
    "DB_FILENAME", "default_db_path", "market_of", "utf8_stdout",
    "Candidate", "read_actionable", "summarize",
    "log_decision", "recent", "track_record",
    "get_price", "mark_book", "position_pnl",
    "MirrorPosition", "apply_mirror", "seed_position", "stage_to_kis",
    "learned_sensitivity", "record_sensitivity",
    "RiskParams", "concentration_check", "size_position", "theme_exposure",
]
