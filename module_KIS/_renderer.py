# FILE: research_Mvp/module_kis/_renderer.py
"""KisQuote / OHLCV / 투자자동향 / 잔고 → markdown 리포트.

module_macro_us._renderer 와 동일한 _fmt 헬퍼 스타일.
"""
from __future__ import annotations

from typing import Optional

from ._account import Balance
from ._chart import KisBar
from ._investor import InvestorDay, net_summary
from ._order import OrderPreview, OrderResult
from ._overseas import OverseasBalance
from ._quote import _RISK_STATUS, KisQuote


def _won(v: Optional[float]) -> str:
    if v is None:
        return "—"
    return f"{v:,.0f}원"


def _num(v: Optional[float], suffix: str = "") -> str:
    if v is None:
        return "—"
    return f"{v:,.2f}{suffix}"


def _signed(v: Optional[float], suffix: str = "") -> str:
    if v is None:
        return "—"
    sign = "+" if v >= 0 else ""
    return f"{sign}{v:,.0f}{suffix}"


def _eok(v: Optional[float]) -> str:
    """억원 단위 시총을 조/억으로."""
    if v is None:
        return "—"
    if v >= 10_000:
        jo = int(v // 10_000)
        eok = int(v % 10_000)
        return f"{jo}조 {eok:,}억" if eok else f"{jo}조"
    return f"{v:,.0f}억"


def _man(qty: Optional[int]) -> str:
    """순매수 수량을 만주 단위로(가독성)."""
    if qty is None:
        return "—"
    sign = "+" if qty >= 0 else ""
    return f"{sign}{qty / 10_000:,.1f}만주"


def _title(name: Optional[str], code: str) -> str:
    """이름 있으면 '이름 (코드)', 없으면 코드만(코드 중복 방지)."""
    return f"{name} ({code})" if name else code


def render_quote(q: KisQuote) -> str:
    title = _title(q.name, q.code)
    arrow = ""
    if q.change is not None:
        arrow = "▲" if q.change > 0 else ("▼" if q.change < 0 else "―")
    lines = [
        f"# {title} — KIS 시세 스냅샷",
        "",
        f"- 현재가: {_won(q.price)} {arrow} {_signed(q.change)} "
        f"({_num(q.change_pct, '%')}, {q.sign or '—'})",
        f"- 시/고/저: {_won(q.open)} / {_won(q.high)} / {_won(q.low)} "
        f"(전일 {_won(q.prev_close)})",
        f"- 거래량: {q.volume:,}주" if q.volume is not None else "- 거래량: —",
        f"- 시가총액: {_eok(q.market_cap_eok)} / 상장주식수: "
        + (f"{q.listed_shares:,}주" if q.listed_shares is not None else "—"),
        f"- PER {_num(q.per)} · PBR {_num(q.pbr)} · EPS {_won(q.eps)} · BPS {_won(q.bps)}",
        f"- 52주 고/저: {_won(q.week52_high)} / {_won(q.week52_low)}"
        + (f" (고점 대비 {q.pct_from_52w_high():+.1f}%)"
           if q.pct_from_52w_high() is not None else ""),
        f"- 외국인 소진율: {_num(q.foreign_pct, '%')} · 거래량 회전율: {_num(q.turnover_pct, '%')}",
    ]
    if q.sector:
        lines.append(f"- 업종: {q.sector}")
    if q.is_flagged():
        bits = []
        if (q.status_code or "").strip() in _RISK_STATUS:
            bits.append(f"종목상태 {q.status_label() or q.status_code}")
        if (q.warn_code or "").strip() not in ("", "00"):
            bits.append(f"시장경고 {q.warn_label() or q.warn_code}")
        lines.append("- ⚠️ " + " · ".join(bits))
    lines.append("")
    return "\n".join(lines)


def render_ohlcv(bars: list[KisBar], name: Optional[str], code: str, period: str) -> str:
    label = {"D": "일봉", "W": "주봉", "M": "월봉", "Y": "년봉"}.get(period, period)
    title = _title(name, code)
    if not bars:
        return f"## {title} — {label}\n_데이터 없음._\n"
    last = bars[-1]
    first = bars[0]
    hi = max((b.high for b in bars if b.high is not None), default=None)
    lo = min((b.low for b in bars if b.low is not None), default=None)
    chg = None
    if last.close and first.close:
        chg = (last.close / first.close - 1) * 100
    lines = [
        f"## {title} — {label} {len(bars)}봉",
        "",
        f"- 구간: {first.date} ~ {last.date}",
        f"- 종가: {_won(last.close)} (구간 {_num(chg, '%')})",
        f"- 구간 고/저: {_won(hi)} / {_won(lo)}",
        "",
        "| 날짜 | 시 | 고 | 저 | 종 | 거래량 |",
        "|------|----|----|----|----|--------|",
    ]
    for b in bars[-10:]:  # 최근 10봉만 표로(전체는 --json).
        vol = f"{b.volume:,}" if b.volume is not None else "—"
        lines.append(
            f"| {b.date} | {b.open:,.0f} | {b.high:,.0f} | {b.low:,.0f} "
            f"| {b.close:,.0f} | {vol} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_investor(rows: list[InvestorDay], code: str, name: Optional[str] = None) -> str:
    title = _title(name, code)
    if not rows:
        return f"## {title} — 투자자별 매매동향\n_데이터 없음._\n"
    s = net_summary(rows)
    lines = [
        f"## {title} — 투자자별 순매수 ({s['days']}영업일 누적)",
        "",
        f"- 외국인: {_man(s['foreign'])} · 기관: {_man(s['institution'])} "
        f"· 개인: {_man(s['individual'])}",
        "",
        "| 날짜 | 외국인 | 기관 | 개인 | 종가 |",
        "|------|--------|------|------|------|",
    ]
    for r in rows[-10:]:
        close = f"{r.close:,}" if r.close is not None else "—"
        lines.append(
            f"| {r.date} | {_man(r.foreign_qty)} | {_man(r.institution_qty)} "
            f"| {_man(r.individual_qty)} | {close} |"
        )
    lines.append("")
    return "\n".join(lines)


def _won0(v: Optional[int]) -> str:
    return "—" if v is None else f"{v:,}원"


def _frcr(v: Optional[float], cur: str) -> str:
    if v is None:
        return "—"
    sym = {"USD": "$", "HKD": "HK$", "JPY": "¥", "CNY": "¥", "EUR": "€"}.get(cur, "")
    return f"{sym}{v:,.2f}" if sym else f"{v:,.2f} {cur}"


def render_wallet(dom: Optional[Balance], ovs: Optional[OverseasBalance],
                  env: str = "prod") -> str:
    """원화(국내) + 외화(해외) 통합 잔고. 총자산 한 장으로."""
    tag = "모의투자" if env == "vps" else "실전"
    lines = [f"# 계좌 잔고 ({tag})", ""]

    # 총자산: 해외 present-balance 의 tot_asst_amt 가 원화+외화 합산.
    if ovs and ovs.total_asset_krw is not None:
        lines.append(f"- **총자산**: {_won0(ovs.total_asset_krw)}")
        krw = ovs.krw_deposit if ovs.krw_deposit is not None else (dom.deposit if dom else None)
        lines.append(f"  - 원화 예수금: {_won0(krw)}")
        lines.append(f"  - 외화 평가(원화환산): {_won0(ovs.frcr_eval_total_krw)}")
        if ovs.withdrawable_krw is not None:
            lines.append(f"- 출금가능 총액: {_won0(ovs.withdrawable_krw)}")
    elif dom:
        lines.append(f"- **순자산**: {_won0(dom.net_asset)}")
        lines.append(
            f"- 총평가금액: {_won0(dom.total_eval)} "
            f"(예수금 {_won0(dom.deposit)} + 주식평가 {_won0(dom.eval_securities)})"
        )

    # 외화 예수금 통화별.
    if ovs and ovs.foreign_cash:
        lines += [
            "",
            "## 외화 예수금",
            "",
            "| 통화 | 예수금 | 출금가능 | 환율 | 원화환산 |",
            "|------|--------|----------|------|----------|",
        ]
        for fc in ovs.foreign_cash:
            nm = f"{fc.currency} {fc.name}" if fc.name else fc.currency
            rate = f"{fc.exchange_rate:,.2f}원" if fc.exchange_rate is not None else "—"
            lines.append(
                f"| {nm} | {_frcr(fc.deposit, fc.currency)} "
                f"| {_frcr(fc.withdrawable, fc.currency)} | {rate} "
                f"| {_won0(int(fc.eval_krw)) if fc.eval_krw is not None else '—'} |"
            )

    # 보유종목(국내+해외).
    dom_h = dom.holdings if dom else []
    ovs_h = ovs.holdings if ovs else []
    if dom_h or ovs_h:
        lines += ["", f"## 보유종목 (국내 {len(dom_h)} · 해외 {len(ovs_h)})", ""]
        if dom_h:
            lines += [
                "| 종목 | 수량 | 평균가 | 현재가 | 평가금액 | 손익 | 수익률 |",
                "|------|------|--------|--------|----------|------|--------|",
            ]
            for h in dom_h:
                nm = f"{h.name}({h.code})" if h.name else h.code
                qty = f"{h.qty:,}" if h.qty is not None else "—"
                avg = f"{h.avg_price:,.0f}" if h.avg_price is not None else "—"
                cur = f"{h.cur_price:,.0f}" if h.cur_price is not None else "—"
                ev = f"{h.eval_amount:,}" if h.eval_amount is not None else "—"
                pnl = f"{h.pnl_amount:+,}" if h.pnl_amount is not None else "—"
                rt = f"{h.pnl_pct:+.2f}%" if h.pnl_pct is not None else "—"
                lines.append(f"| {nm} | {qty} | {avg} | {cur} | {ev} | {pnl} | {rt} |")
        for h in ovs_h:
            nm = f"{h.name}({h.code})" if h.name else h.code
            qty = f"{h.qty:,.0f}" if h.qty is not None else "—"
            rt = f"{h.pnl_pct:+.2f}%" if h.pnl_pct is not None else "—"
            cval = h.currency or ""
            lines.append(
                f"- 🌐 {nm} {qty}주 · 평가 {_frcr(h.eval_frcr, cval)} ({rt})"
            )
    else:
        lines += ["", "_보유종목 없음 — 국내·해외 모두 현금만._"]

    lines.append("")
    return "\n".join(lines)


def render_balance(bal: Balance, env: str = "prod") -> str:
    tag = "모의투자" if env == "vps" else "실전"
    pnl_pct = bal.total_pnl_pct
    pnl_str = _won0(bal.total_pnl)
    if pnl_pct is not None:
        sign = "+" if (bal.total_pnl or 0) >= 0 else ""
        pnl_str = f"{sign}{bal.total_pnl:,}원 ({sign}{pnl_pct:.2f}%)"
    lines = [
        f"# 계좌 잔고 ({tag})",
        "",
        f"- **순자산**: {_won0(bal.net_asset)}",
        f"- 총평가금액: {_won0(bal.total_eval)} "
        f"(예수금 {_won0(bal.deposit)} + 주식평가 {_won0(bal.eval_securities)})",
        f"- 출금가능(D+2 예수금): {_won0(bal.d2_deposit)}",
        f"- 평가손익: {pnl_str} (매입 {_won0(bal.total_buy)})",
    ]
    if bal.holdings:
        lines += [
            "",
            f"## 보유종목 {len(bal.holdings)}개",
            "",
            "| 종목 | 수량 | 평균가 | 현재가 | 평가금액 | 손익 | 수익률 |",
            "|------|------|--------|--------|----------|------|--------|",
        ]
        for h in bal.holdings:
            nm = f"{h.name}({h.code})" if h.name else h.code
            qty = f"{h.qty:,}" if h.qty is not None else "—"
            avg = f"{h.avg_price:,.0f}" if h.avg_price is not None else "—"
            cur = f"{h.cur_price:,.0f}" if h.cur_price is not None else "—"
            ev = f"{h.eval_amount:,}" if h.eval_amount is not None else "—"
            pnl = f"{h.pnl_amount:+,}" if h.pnl_amount is not None else "—"
            rt = f"{h.pnl_pct:+.2f}%" if h.pnl_pct is not None else "—"
            lines.append(f"| {nm} | {qty} | {avg} | {cur} | {ev} | {pnl} | {rt} |")
    else:
        lines += ["", "_보유종목 없음 (현금만)._"]
    lines.append("")
    return "\n".join(lines)


def render_order(obj) -> str:
    """OrderPreview(드라이런) / OrderResult(체결요청) 둘 다 렌더."""
    side_ko = "매수" if obj.side == "buy" else "매도"
    tag = "모의투자" if obj.env == "vps" else "실전"
    kind = "시장가" if getattr(obj, "market", False) else f"지정가 {obj.price:,}원"

    if isinstance(obj, OrderResult):
        lines = [
            f"# ✅ 주문 전송됨 — {side_ko} ({tag})",
            "",
            f"- 종목: {obj.code} / 수량: {obj.qty:,}주 / {kind}",
            f"- 주문번호: {obj.order_no or '—'} (조직 {obj.org_no or '—'}, {obj.order_time or '—'})",
            f"- 메시지: {obj.message or '—'}",
            "",
            "_주문 접수 ≠ 체결. 체결·미체결은 HTS/앱 또는 잔고조회로 확인하세요._",
        ]
        return "\n".join(lines)

    # OrderPreview (드라이런)
    lines = [
        f"# 🟡 주문 미리보기 (DRY-RUN) — {side_ko} ({tag})",
        "",
        f"- 종목: {obj.code} / 수량: {obj.qty:,}주 / {kind}",
        f"- 예상 체결금액: {('—' if obj.est_value is None else f'{obj.est_value:,}원')}",
        f"- tr_id: {obj.tr_id}",
    ]
    if obj.warnings:
        lines += ["", "## 점검"]
        lines += [f"- {w}" for w in obj.warnings]
    lines += [
        "",
        "> 실제 발사하려면 동일 명령에 **`--execute`** 추가. (이 미리보기는 주문을 전송하지 않음)",
    ]
    return "\n".join(lines)
