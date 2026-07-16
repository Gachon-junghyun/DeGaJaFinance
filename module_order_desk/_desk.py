# FILE: module_order_desk/_desk.py
"""KIS 주문 데스크 — Tkinter 스택형 주문 GUI.

주문을 '스택(큐)'에 카드로 쌓아두고, 카드마다 [체결] 버튼으로 하나씩 발사한다.
자동매매 아님 — 모든 체결은 사람이 버튼을 눌러야 나간다(+확인 다이얼로그 1회).

실행:
    python -m module_order_desk        (cwd=리포 루트)
    또는 run_kis_desk.bat 더블클릭

의존성: 표준 라이브러리 tkinter 뿐 (별도 설치 없음). 주문 로직은 module_KIS 재사용.
KIS_APP_KEY/SECRET + KIS_ACCOUNT_NO 필요(리포 루트 .env). KIS_ENV=prod 면 실전(실제 돈).
"""
from __future__ import annotations

import os
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _load_dotenv() -> None:
    if os.environ.get("KIS_APP_KEY") and os.environ.get("KIS_ACCOUNT_NO"):
        return
    p = REPO_ROOT / ".env"
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and v and k not in os.environ:
            os.environ[k] = v


_load_dotenv()

from . import _decisions as kd  # noqa: E402
from . import _stack as kstack  # noqa: E402

from module_KIS import (  # noqa: E402
    KisError,
    fetch_balance,
    fetch_fluctuation,
    fetch_ohlcv,
    fetch_overseas_balance,
    fetch_quote,
    fetch_us_quote,
    fetch_volume_rank,
    load_config,
    place_order,
    place_us_order,
)

# ── 색상(HJH 터미널 팔레트와 동일 계열) ───────────────────────────────
C = {
    "bg": "#0e0f11", "panel": "#16181c", "panel2": "#1d2025",
    "border": "#2a2d33", "text": "#d9dbdf", "muted": "#8a8e96",
    "amber": "#f5b452", "buy": "#f05650", "sell": "#4d8df0",
    "ok": "#22c55e", "warn": "#f0c050", "err": "#ef4444",
}
FONT = ("Malgun Gothic", 10)
FONT_B = ("Malgun Gothic", 10, "bold")
FONT_BIG = ("Malgun Gothic", 14, "bold")


def _won(v) -> str:
    return "—" if v is None else f"{int(v):,}원"


# 자산배분 버킷 색상
PF_COL = {
    "원화현금": "#f5b452", "외화현금($)": "#22c55e",
    "국내주식": "#6aa7e8", "해외주식": "#a78bfa",
}


def _usdkrw(ovs) -> float:
    """USD→KRW 환율: 외화예수금 고시환율 → env(USDKRW_FALLBACK) → 기본 1380 순."""
    if ovs:
        for c in ovs.foreign_cash:
            if c.exchange_rate:
                return float(c.exchange_rate)
    try:
        return float(os.environ.get("USDKRW_FALLBACK", "1380") or 1380)
    except (TypeError, ValueError):
        return 1380.0


def _overseas_pnl_krw(ovs, exrt):
    """해외 미실현손익·취득원가를 원화로 합산 → (손익원화, 원가원화).

    KIS가 pnl_frcr(평가손익 외화)를 주면 그대로, 안 주면(null) (현재가-평단)×수량으로 계산.
    """
    pnl_frcr = 0.0
    cost_frcr = 0.0
    for h in (ovs.holdings if ovs else []):
        qty = h.qty or 0
        if h.pnl_frcr is not None:
            pnl_frcr += h.pnl_frcr
        elif h.cur_price is not None and h.avg_price is not None:
            pnl_frcr += (h.cur_price - h.avg_price) * qty
        if h.avg_price is not None:
            cost_frcr += h.avg_price * qty
    return int(pnl_frcr * exrt), int(cost_frcr * exrt)


def portfolio_buckets(dom, ovs):
    """국내+해외 잔고 → 원화환산 4버킷 [(라벨, 값KRW, 색)] + 총액 + 현금비중."""
    krw_cash = (ovs.krw_deposit if ovs and ovs.krw_deposit is not None
                else (dom.deposit if dom else 0)) or 0
    dom_stock = sum((h.eval_amount or 0) for h in (dom.holdings if dom else []))
    frcr_cash_krw = 0
    overseas_stock_krw = 0
    if ovs:
        frcr_cash_krw = sum(int(c.eval_krw or 0) for c in ovs.foreign_cash)
        foreign_total = ovs.frcr_eval_total_krw or 0
        overseas_stock_krw = max(0, foreign_total - frcr_cash_krw)
        # KIS는 외화기준 잔고조회에서 frcr_evlu_tota(외화평가총액)를 0으로 반환한다 →
        # 도넛에서 해외주식이 통째로 사라지는 버그. 보유종목 외화평가×환율(시장가)로 보정.
        if overseas_stock_krw <= 0 and ovs.holdings:
            exrt = _usdkrw(ovs)
            overseas_stock_krw = int(
                sum((h.eval_frcr or 0) for h in ovs.holdings) * exrt)
    buckets = [
        ("원화현금", krw_cash, PF_COL["원화현금"]),
        ("외화현금($)", frcr_cash_krw, PF_COL["외화현금($)"]),
        ("국내주식", dom_stock, PF_COL["국내주식"]),
        ("해외주식", overseas_stock_krw, PF_COL["해외주식"]),
    ]
    total = sum(v for _, v, _ in buckets)
    cash = krw_cash + frcr_cash_krw
    cash_ratio = (cash / total * 100) if total else 0.0
    return buckets, total, cash_ratio


_ERR_LOG = REPO_ROOT / "kis_desk_error.log"


def _log_error(where: str, tb: str) -> None:
    """오류를 파일로 남긴다(콘솔이 닫혀도 원인 추적 가능)."""
    try:
        with open(_ERR_LOG, "a", encoding="utf-8") as f:
            f.write(f"\n===== {where} =====\n{tb}\n")
    except Exception:
        pass
    print(f"[kis_desk] {where} 오류:\n{tb}")


class KisDesk(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("KIS 주문 데스크")
        self.configure(bg=C["bg"])
        self.geometry("760x720")
        self.minsize(640, 560)

        try:
            self.cfg = load_config()
            self.cfg.require_account()
            self.env = self.cfg.env
            self._fatal = None
        except KisError as e:
            self.cfg = None
            self.env = "prod"
            self._fatal = str(e)

        # Tkinter 콜백/스레드 예외를 파일+팝업으로(조용히 죽는 것 방지)
        self.report_callback_exception = self._on_cb_error

        self._cards: list[OrderCard] = []
        self._build()
        if self._fatal:
            # mainloop 시작 후 팝업(생성 도중 모달 방지)
            self.after(300, lambda: messagebox.showerror("설정 오류", self._fatal))
        else:
            # mainloop 시작 후 첫 잔고 조회(스레드 after 레이스 방지)
            self.after(300, self.refresh_balance)
            # 저장된 '계획' 스택 자동 로드(드라이런 카드)
            self.after(900, self._load_staged)

    def _on_cb_error(self, exc, val, tb) -> None:
        import traceback
        text = "".join(traceback.format_exception(exc, val, tb))
        _log_error("콜백", text)
        try:
            messagebox.showerror("KIS 데스크 오류", text[-1500:])
        except Exception:
            pass

    # ── 레이아웃 ──────────────────────────────────────────────────
    def _build(self) -> None:
        is_real = self.env == "prod"
        banner = tk.Frame(self, bg=(C["buy"] if is_real else C["panel2"]))
        banner.pack(fill="x")
        tk.Label(
            banner,
            text=("● 실전 — 실제 돈이 움직입니다" if is_real else "○ 모의투자 (가상)"),
            bg=(C["buy"] if is_real else C["panel2"]),
            fg="#ffffff", font=FONT_B, pady=5,
        ).pack(side="left", padx=12)

        # 잔고 바
        bar = tk.Frame(self, bg=C["panel"]); bar.pack(fill="x")
        self.lbl_balance = tk.Label(
            bar, text="잔고 불러오는 중…", bg=C["panel"], fg=C["text"],
            font=FONT, anchor="w", justify="left", pady=8, padx=12,
        )
        self.lbl_balance.pack(side="left", fill="x", expand=True)
        self._mk_btn(bar, "↻ 새로고침", self.refresh_balance, C["panel2"]).pack(
            side="right", padx=(0, 10)
        )
        self._mk_btn(bar, "📊 포트폴리오", self.open_portfolio, C["amber"], fg="#000").pack(
            side="right", padx=4
        )
        self._mk_btn(bar, "🔥 인기종목", self.open_movers, C["panel2"]).pack(
            side="right", padx=4
        )
        self._mk_btn(bar, "🌊 흐름", self.open_flow, C["panel2"]).pack(
            side="right", padx=4
        )
        self._mk_btn(bar, "🔀 만약에", self.open_whatif, C["panel2"]).pack(
            side="right", padx=4
        )

        # 주문 추가 폼
        form = tk.Frame(self, bg=C["panel2"], padx=12, pady=10)
        form.pack(fill="x")

        # 시장: 국내(KRW) / 미국(USD)
        self.mkt = tk.StringVar(value="kr")
        for txt, val in (("국내", "kr"), ("미국", "us")):
            tk.Radiobutton(
                form, text=txt, variable=self.mkt, value=val, fg=C["amber"], bg=C["panel2"],
                selectcolor=C["bg"], activebackground=C["panel2"], activeforeground=C["amber"],
                font=FONT_B, command=self._on_mkt_change,
            ).pack(side="left", padx=(0, 6))
        tk.Frame(form, width=1, bg=C["border"]).pack(side="left", fill="y", padx=6)

        self.side = tk.StringVar(value="buy")
        for txt, val, col in (("매수", "buy", C["buy"]), ("매도", "sell", C["sell"])):
            tk.Radiobutton(
                form, text=txt, variable=self.side, value=val, fg=col, bg=C["panel2"],
                selectcolor=C["bg"], activebackground=C["panel2"], activeforeground=col,
                font=FONT_B, indicatoron=True,
            ).pack(side="left", padx=(0, 8))

        self.e_code = self._mk_entry(form, "종목코드/티커", 9)
        self.e_qty = self._mk_entry(form, "수량", 6)
        self.e_price, self.lbl_price = self._mk_entry(form, "지정가(원)", 9, ret_label=True)
        self.is_market = tk.BooleanVar(value=False)
        self.chk_market = tk.Checkbutton(
            form, text="시장가", variable=self.is_market, fg=C["text"], bg=C["panel2"],
            selectcolor=C["bg"], activebackground=C["panel2"], font=FONT,
        )
        self.chk_market.pack(side="left", padx=6)
        self._mk_btn(form, "＋ 스택에 추가", self.add_to_stack, C["amber"], fg="#000").pack(
            side="left", padx=8
        )

        # 스택 헤더
        hd = tk.Frame(self, bg=C["bg"]); hd.pack(fill="x", padx=12, pady=(10, 2))
        tk.Label(hd, text="주문 스택  (카드마다 [체결]을 눌러 하나씩 발사)",
                 bg=C["bg"], fg=C["amber"], font=FONT_B).pack(side="left")
        self._mk_btn(hd, "체결완료 정리", self.clear_filled, C["panel"]).pack(side="right")
        self._mk_btn(hd, "💾 계획저장", self.save_stack, C["panel"]).pack(side="right", padx=4)

        # 스크롤 스택
        wrap = tk.Frame(self, bg=C["bg"]); wrap.pack(fill="both", expand=True, padx=12, pady=6)
        self.canvas = tk.Canvas(wrap, bg=C["bg"], highlightthickness=0)
        sb = ttk.Scrollbar(wrap, orient="vertical", command=self.canvas.yview)
        self.stack = tk.Frame(self.canvas, bg=C["bg"])
        self.stack.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self._win = self.canvas.create_window((0, 0), window=self.stack, anchor="nw")
        self.canvas.bind(
            "<Configure>", lambda e: self.canvas.itemconfig(self._win, width=e.width)
        )
        self.canvas.configure(yscrollcommand=sb.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        self.canvas.bind_all(
            "<MouseWheel>",
            lambda e: self.canvas.yview_scroll(int(-e.delta / 120), "units"),
        )

        self.status = tk.Label(self, text="", bg=C["bg"], fg=C["muted"], font=FONT,
                               anchor="w", padx=12, pady=4)
        self.status.pack(fill="x")

    def _on_mkt_change(self) -> None:
        """국내/미국 전환 시 가격 라벨·시장가 가용 갱신."""
        if self.mkt.get() == "us":
            self.lbl_price.config(text="지정가($)")
            self.is_market.set(False)
            self.chk_market.config(state="disabled")  # 미국은 지정가만
        else:
            self.lbl_price.config(text="지정가(원)")
            self.chk_market.config(state="normal")

    def _mk_entry(self, parent, placeholder, width, ret_label=False):
        f = tk.Frame(parent, bg=C["panel2"]); f.pack(side="left", padx=4)
        lbl = tk.Label(f, text=placeholder, bg=C["panel2"], fg=C["muted"],
                       font=("Malgun Gothic", 8))
        lbl.pack(anchor="w")
        e = tk.Entry(f, width=width, bg=C["bg"], fg=C["text"], insertbackground=C["text"],
                     relief="flat", font=FONT)
        e.pack()
        return (e, lbl) if ret_label else e

    def _mk_btn(self, parent, text, cmd, bg, fg=None):
        return tk.Button(
            parent, text=text, command=cmd, bg=bg, fg=(fg or C["text"]),
            activebackground=bg, relief="flat", font=FONT_B, padx=10, pady=4,
            cursor="hand2", bd=0,
        )

    # ── 비동기 헬퍼 ──────────────────────────────────────────────
    def _async(self, fn, on_done) -> None:
        def worker():
            try:
                res, err = fn(), None
            except Exception as e:  # noqa: BLE001
                res, err = None, e
            try:
                self.after(0, lambda: on_done(res, err))
            except RuntimeError:
                pass  # 창이 닫혔거나 mainloop 종료 — 무시
        threading.Thread(target=worker, daemon=True).start()

    def _set_status(self, msg, color=None) -> None:
        self.status.config(text=msg, fg=color or C["muted"])

    # ── 잔고 ────────────────────────────────────────────────────
    def refresh_balance(self) -> None:
        if not self.cfg:
            return
        self._set_status("잔고 조회 중…")

        def fetch():
            dom = fetch_balance(cfg=self.cfg)
            try:
                ovs = fetch_overseas_balance(cfg=self.cfg)
            except KisError:
                ovs = None
            return dom, ovs

        def done(res, err):
            if err:
                self.lbl_balance.config(text=f"잔고 오류: {err}")
                return
            dom, ovs = res
            if ovs and ovs.total_asset_krw is not None:
                usd = next((c for c in ovs.foreign_cash if c.currency == "USD"), None)
                usd_s = f" · USD ${usd.deposit:,.2f}" if usd and usd.deposit else ""
                txt = (f"총자산 {_won(ovs.total_asset_krw)}   |   "
                       f"원화예수금 {_won(ovs.krw_deposit or dom.deposit)}{usd_s}   |   "
                       f"보유 국내 {len(dom.holdings)} · 해외 {len(ovs.holdings)}")
            else:
                txt = f"예수금 {_won(dom.deposit)}   |   보유종목 {len(dom.holdings)}개"
            self.lbl_balance.config(text=txt)
            self._set_status("잔고 갱신 완료", C["ok"])

        self._async(fetch, done)

    def open_portfolio(self) -> None:
        if not self.cfg:
            messagebox.showerror("설정 오류", self._fatal or "설정 없음")
            return
        if getattr(self, "_pf", None) and self._pf.winfo_exists():
            self._pf.lift()
            return
        self._pf = PortfolioWindow(self)

    def open_whatif(self) -> None:
        if not self.cfg:
            messagebox.showerror("설정 오류", self._fatal or "설정 없음")
            return
        if getattr(self, "_wi", None) and self._wi.winfo_exists():
            self._wi.lift()
            return
        self._wi = WhatIfWindow(self)

    def open_movers(self) -> None:
        if not self.cfg:
            messagebox.showerror("설정 오류", self._fatal or "설정 없음")
            return
        if getattr(self, "_mv", None) and self._mv.winfo_exists():
            self._mv.lift()
            return
        self._mv = MoversWindow(self)

    def open_flow(self, code: str | None = None, name: str | None = None) -> None:
        """흐름(flow_read) 창. code 주면 프리필+자동조회 — 인기종목→흐름 엮기."""
        if not self.cfg:
            messagebox.showerror("설정 오류", self._fatal or "설정 없음")
            return
        if getattr(self, "_fl", None) and self._fl.winfo_exists():
            self._fl.lift()
            if code:
                self._fl.query(code, name)
            return
        self._fl = FlowWindow(self, code, name)

    def prefill_order(self, code: str) -> None:
        """주문 폼 종목코드 채우기(국내) — 흐름창→주문데스크 엮기."""
        self.mkt.set("kr")
        self._on_mkt_change()
        self.e_code.delete(0, "end")
        self.e_code.insert(0, code)
        self._set_status(f"주문 폼에 {code} 넣음 — 수량/가격 입력 후 [스택에 추가]", C["amber"])

    # ── 스택 추가 (드라이런 미리보기) ─────────────────────────────
    def add_to_stack(self) -> None:
        if not self.cfg:
            messagebox.showerror("설정 오류", self._fatal or "설정 없음")
            return
        code = self.e_code.get().strip()
        if not code:
            messagebox.showwarning("입력", "종목코드/티커를 입력하세요.")
            return
        try:
            qty = int(self.e_qty.get().strip())
        except ValueError:
            messagebox.showwarning("입력", "수량은 정수여야 합니다.")
            return
        side = self.side.get()
        is_us = self.mkt.get() == "us"
        raw_price = self.e_price.get().strip()
        self._set_status("미리보기 생성 중…")

        if is_us:
            price = float(raw_price) if raw_price else None  # 빈칸 → 현재가
            sym = code.upper()

            def build():
                preview = place_us_order(side, sym, qty, price=price,
                                         execute=False, cfg=self.cfg)
                return preview, sym
        else:
            market = self.is_market.get()
            price = None
            if not market:
                try:
                    price = int(raw_price)
                except ValueError:
                    messagebox.showwarning("입력", "지정가(원)를 넣거나 시장가를 체크하세요.")
                    self._set_status("")
                    return

            def build():
                preview = place_order(side, code, qty, price=price, market=market,
                                      execute=False, cfg=self.cfg)
                name = None
                try:
                    _, name = fetch_ohlcv(code, "D", count=1, cfg=self.cfg)
                except KisError:
                    pass
                return preview, name

        def done(res, err):
            if err:
                self._set_status(f"미리보기 실패: {err}", C["err"])
                messagebox.showerror("미리보기 실패", str(err))
                return
            preview, name = res
            card = OrderCard(self.stack, self, preview, name)
            self._cards.insert(0, card)   # 최신을 맨 앞에
            for c in self._cards:         # 스택 순서대로 다시 쌓기(최신이 위)
                c.pack_forget()
                c.pack(fill="x", pady=4)
            self._set_status("스택에 추가됨 — [체결]로 발사", C["amber"])

        self._async(build, done)

    def stage_intent(self, market, side, code, qty, price=None) -> None:
        """저장된 계획(intent)으로 드라이런 카드 1장 생성(폼 입력 없이). 실주문 아님."""
        is_us = market == "us"
        if is_us:
            sym = (code or "").upper()

            def build():
                pv = place_us_order(side, sym, qty, price=price, execute=False, cfg=self.cfg)
                return pv, sym
        else:
            kr_market = price is None

            def build():
                pv = place_order(side, code, qty, price=price, market=kr_market,
                                 execute=False, cfg=self.cfg)
                name = None
                try:
                    _, name = fetch_ohlcv(code, "D", count=1, cfg=self.cfg)
                except KisError:
                    pass
                return pv, name

        def done(res, err):
            if err:
                self._set_status(f"계획 카드 실패({code}): {err}", C["err"])
                return
            pv, name = res
            card = OrderCard(self.stack, self, pv, name)
            self._cards.insert(0, card)
            for c in self._cards:
                c.pack_forget()
                c.pack(fill="x", pady=4)

        self._async(build, done)

    def _load_staged(self) -> None:
        intents = kstack.load_staged()
        if not intents:
            return
        self._set_status(f"저장된 계획 {len(intents)}건 불러오는 중…", C["amber"])
        for it in intents:
            self.stage_intent(it.get("market", "us"), it.get("side", "buy"),
                              it.get("code", ""), it.get("qty", 1), it.get("price"))

    def save_stack(self) -> None:
        """현재 스택(미체결 카드)을 계획 파일로 저장."""
        intents = []
        for c in reversed(self._cards):   # 추가 순서대로
            if c.filled:
                continue
            p = c.preview
            if c.is_us:
                intents.append(kstack.make_intent("us", p.side, p.symbol, p.qty, p.price))
            else:
                price = None if p.market else p.price
                intents.append(kstack.make_intent("kr", p.side, p.code, p.qty, price))
        kstack.save_staged(intents)
        self._set_status(f"계획 {len(intents)}건 저장됨 (다음 실행 때 자동 로드)", C["ok"])

    def clear_filled(self) -> None:
        for c in list(self._cards):
            if c.filled:
                c.destroy()
                self._cards.remove(c)

    # ── 실제 체결 (카드에서 호출) ────────────────────────────────
    def execute_card(self, card: "OrderCard") -> None:
        p = card.preview
        is_us = card.is_us
        side_ko = "매수" if p.side == "buy" else "매도"
        if is_us:
            tgt = f"{p.symbol} ({p.exchange})  {p.qty:,}주  ${p.price:,.2f} 지정가"
            est = f"예상 ${p.est_value_usd:,.2f}"
        else:
            kind = "시장가" if p.market else f"{p.price:,}원 지정가"
            tgt = f"{p.code}  {p.qty:,}주  {kind}"
            est = f"예상 {_won(p.est_value)}"
        warn = "\n\n⚠️ 실전 계좌 — 실제 체결됩니다." if self.env == "prod" else ""
        ok = messagebox.askyesno(
            "체결 확인",
            f"[{side_ko}] {tgt}\n{est}{warn}\n\n정말 주문을 전송할까요?",
            icon="warning" if self.env == "prod" else "question",
        )
        if not ok:
            return
        card.set_state("전송 중…", C["warn"])
        card.btn_fill.config(state="disabled")

        def fire():
            if is_us:
                return place_us_order(p.side, p.symbol, p.qty, price=p.price,
                                      execute=True, cfg=self.cfg)
            return place_order(p.side, p.code, p.qty, price=p.price,
                               market=p.market, execute=True, cfg=self.cfg)

        def done(res, err):
            if err:
                card.set_state(f"실패: {err}", C["err"])
                card.btn_fill.config(state="normal")
                messagebox.showerror("주문 실패", str(err))
                return
            card.filled = True
            card.set_state(f"✅ 체결요청 #{res.order_no or '—'} ({res.order_time or ''})", C["ok"])
            card.btn_fill.config(text="체결됨", state="disabled")
            # '만약에' 결정 로그(체결된 선택만 기록)
            try:
                if is_us:
                    kd.log_decision("us", p.side, p.symbol, p.symbol, p.qty, p.price, "USD")
                else:
                    kd.log_decision("kr", p.side, p.code, card.name, p.qty, p.price, "KRW")
            except Exception:
                pass
            self._set_status(f"주문 전송됨: {res.order_no}", C["ok"])
            self.refresh_balance()

        self._async(fire, done)


class OrderCard(tk.Frame):
    def __init__(self, parent, app: KisDesk, preview, name) -> None:
        accent = C["buy"] if preview.side == "buy" else C["sell"]
        super().__init__(parent, bg=C["panel"], highlightbackground=accent,
                         highlightthickness=1)
        self.app = app
        self.preview = preview
        self.name = name
        self.filled = False
        self.is_us = hasattr(preview, "est_value_usd")  # US 미리보기 판별

        side_ko = "매수" if preview.side == "buy" else "매도"
        if self.is_us:
            title = f"🇺🇸 {preview.symbol} ({preview.exchange})"
            kind = f"@${preview.price:,.2f}"
            est_txt = f"예상 ${preview.est_value_usd:,.2f}"
        else:
            title = f"{name} ({preview.code})" if name else preview.code
            kind = "시장가" if preview.market else f"@{preview.price:,}원"
            est_txt = f"예상 {_won(preview.est_value)}"

        top = tk.Frame(self, bg=C["panel"]); top.pack(fill="x", padx=10, pady=(8, 2))
        tk.Label(top, text=f"[{side_ko}]", bg=C["panel"], fg=accent,
                 font=FONT_B).pack(side="left")
        tk.Label(top, text=f"  {title}   {preview.qty:,}주  {kind}", bg=C["panel"],
                 fg=C["text"], font=FONT_B).pack(side="left")
        tk.Label(top, text=est_txt, bg=C["panel"],
                 fg=C["muted"], font=FONT).pack(side="right")

        real_warns = [w for w in preview.warnings if not w.startswith("DRY-RUN")]
        if real_warns:
            tk.Label(self, text="⚠ " + "  ·  ".join(real_warns), bg=C["panel"],
                     fg=C["warn"], font=("Malgun Gothic", 8), wraplength=680,
                     justify="left", anchor="w").pack(fill="x", padx=10, pady=(0, 2))

        bot = tk.Frame(self, bg=C["panel"]); bot.pack(fill="x", padx=10, pady=(2, 8))
        self.btn_fill = tk.Button(
            bot, text="체결 ▶", command=lambda: self.app.execute_card(self),
            bg=accent, fg="#fff", activebackground=accent, relief="flat",
            font=FONT_B, padx=14, pady=3, cursor="hand2", bd=0,
        )
        self.btn_fill.pack(side="left")
        tk.Button(bot, text="삭제", command=self._remove, bg=C["panel2"],
                  fg=C["muted"], relief="flat", font=FONT, padx=8, pady=3,
                  cursor="hand2", bd=0).pack(side="left", padx=6)
        self.lbl_state = tk.Label(bot, text="대기", bg=C["panel"], fg=C["muted"], font=FONT)
        self.lbl_state.pack(side="left", padx=8)

    def set_state(self, txt, color) -> None:
        self.lbl_state.config(text=txt, fg=color)

    def _remove(self) -> None:
        if self in self.app._cards:
            self.app._cards.remove(self)
        self.destroy()


class PortfolioWindow(tk.Toplevel):
    """HTS풍 포트폴리오 뷰 — 자산배분 도넛 + 보유종목 + 현금비중/집중도."""

    def __init__(self, app: KisDesk) -> None:
        super().__init__(app, bg=C["bg"])
        self.app = app
        self.cfg = app.cfg
        self.title("포트폴리오")
        self.geometry("720x640")
        self.configure(bg=C["bg"])

        top = tk.Frame(self, bg=C["panel"]); top.pack(fill="x")
        tk.Label(top, text="📊 포트폴리오", bg=C["panel"], fg=C["amber"],
                 font=FONT_BIG, pady=8, padx=12).pack(side="left")
        self.lbl_sum = tk.Label(top, text="불러오는 중…", bg=C["panel"], fg=C["text"],
                                font=FONT, justify="right")
        self.lbl_sum.pack(side="right", padx=12)
        tk.Button(top, text="↻", command=self.load, bg=C["panel2"], fg=C["text"],
                  relief="flat", font=FONT_B, padx=10, cursor="hand2", bd=0).pack(
            side="right", pady=6)

        mid = tk.Frame(self, bg=C["bg"]); mid.pack(fill="x", padx=12, pady=10)
        self.canvas = tk.Canvas(mid, width=260, height=260, bg=C["bg"],
                                highlightthickness=0)
        self.canvas.pack(side="left")
        self.legend = tk.Frame(mid, bg=C["bg"]); self.legend.pack(
            side="left", fill="both", expand=True, padx=16)

        # 현금비중 게이지
        gw = tk.Frame(self, bg=C["bg"]); gw.pack(fill="x", padx=12, pady=(0, 8))
        tk.Label(gw, text="현금비중 (dry powder)", bg=C["bg"], fg=C["muted"],
                 font=("Malgun Gothic", 8)).pack(anchor="w")
        self.gauge = tk.Canvas(gw, height=20, bg=C["panel2"], highlightthickness=0)
        self.gauge.pack(fill="x")

        tk.Label(self, text="보유종목", bg=C["bg"], fg=C["amber"], font=FONT_B,
                 anchor="w").pack(fill="x", padx=12, pady=(6, 0))
        self.holds = tk.Frame(self, bg=C["bg"]); self.holds.pack(
            fill="both", expand=True, padx=12, pady=4)

        self.load()

    def load(self) -> None:
        self.lbl_sum.config(text="불러오는 중…")

        def fetch():
            dom = fetch_balance(cfg=self.cfg)
            try:
                ovs = fetch_overseas_balance(cfg=self.cfg)
            except KisError:
                ovs = None
            return dom, ovs

        def done(res, err):
            if not self.winfo_exists():
                return
            if err:
                self.lbl_sum.config(text=f"오류: {err}")
                return
            self._render(*res)

        self.app._async(fetch, done)

    def _render(self, dom, ovs) -> None:
        buckets, total, cash_ratio = portfolio_buckets(dom, ovs)
        ex = _usdkrw(ovs)
        # 국내 + 해외 미실현손익 합산(해외는 pnl_frcr 없으면 현재가-평단으로 계산)
        dom_pnl = (dom.total_pnl if dom and dom.total_pnl is not None else 0)
        dom_cost = (dom.total_buy if dom and dom.total_buy else 0)
        ov_pnl, ov_cost = _overseas_pnl_krw(ovs, ex)
        tot_pnl = dom_pnl + ov_pnl
        tot_cost = dom_cost + ov_cost
        tot_pct = (tot_pnl / tot_cost * 100) if tot_cost else None
        # 헤드라인은 KIS 순자산(총자산). 통합증거금으로 미국주식을 사면 보유구성(시장가)이
        # 순자산보다 커질 수 있어(원화현금이 담보로 남음) 두 수를 정직하게 병기한다.
        net = ovs.total_asset_krw if (ovs and ovs.total_asset_krw) else total
        lines = [f"총자산(KIS) {_won(net)}"]
        if abs(total - net) > max(net * 0.02, 10000):
            lines.append(f"보유구성(시장가) {_won(total)}")
        lines.append(f"평가손익 {tot_pnl:+,}원"
                     + (f" ({tot_pct:+.2f}%)" if tot_pct is not None else ""))
        self.lbl_sum.config(text="\n".join(lines), justify="right")
        self._draw_donut(buckets, total)
        self._draw_legend(buckets, total)
        self._draw_gauge(cash_ratio)
        self._draw_holdings(dom, ovs, total)

    # ── 도넛 차트 (Canvas create_arc) ────────────────────────────
    def _draw_donut(self, buckets, total) -> None:
        c = self.canvas; c.delete("all")
        cx, cy, r = 130, 130, 110
        nz = [(l, v, col) for l, v, col in buckets if v > 0]
        if not total or not nz:
            c.create_oval(cx - r, cy - r, cx + r, cy + r, outline=C["border"], width=2)
            c.create_text(cx, cy, text="자산 없음", fill=C["muted"], font=FONT)
            return
        if len(nz) == 1:  # 단일 100% — arc 대신 꽉 찬 원
            c.create_oval(cx - r, cy - r, cx + r, cy + r, fill=nz[0][2], outline=C["bg"])
        else:
            start = 90.0
            for _l, v, col in nz:
                ext = -360.0 * v / total
                c.create_arc(cx - r, cy - r, cx + r, cy + r, start=start, extent=ext,
                             fill=col, outline=C["bg"], width=2, style="pieslice")
                start += ext
        hr = r * 0.58  # 가운데 구멍(도넛)
        c.create_oval(cx - hr, cy - hr, cx + hr, cy + hr, fill=C["bg"], outline=C["bg"])
        c.create_text(cx, cy - 8, text="구성합계", fill=C["muted"], font=("Malgun Gothic", 8))
        c.create_text(cx, cy + 10, text=f"{int(total/10000):,}만", fill=C["text"],
                      font=FONT_B)

    def _draw_legend(self, buckets, total) -> None:
        for w in self.legend.winfo_children():
            w.destroy()
        for label, val, col in buckets:
            pct = (val / total * 100) if total else 0
            row = tk.Frame(self.legend, bg=C["bg"]); row.pack(fill="x", pady=3)
            tk.Canvas(row, width=12, height=12, bg=col, highlightthickness=0).pack(
                side="left", padx=(0, 8))
            tk.Label(row, text=label, bg=C["bg"], fg=C["text"], font=FONT,
                     width=10, anchor="w").pack(side="left")
            tk.Label(row, text=f"{pct:4.1f}%", bg=C["bg"],
                     fg=(C["text"] if val else C["muted"]), font=FONT_B).pack(side="left")
            tk.Label(row, text=f"  {_won(val)}", bg=C["bg"], fg=C["muted"],
                     font=("Malgun Gothic", 8)).pack(side="left")

    def _draw_gauge(self, cash_ratio) -> None:
        g = self.gauge; g.delete("all")
        g.update_idletasks()
        w = g.winfo_width() or 600
        fill_w = int(w * min(cash_ratio, 100) / 100)
        # 현금 많으면 amber(놀고있는 돈), 적으면 green(투입됨)
        col = C["amber"] if cash_ratio >= 50 else C["ok"]
        g.create_rectangle(0, 0, fill_w, 20, fill=col, outline=col)
        invested = 100 - cash_ratio
        g.create_text(8, 10, text=f"현금 {cash_ratio:.0f}%  ·  투입 {invested:.0f}%",
                      anchor="w", fill="#0b0c0e", font=FONT_B)

    def _draw_holdings(self, dom, ovs, total) -> None:
        for w in self.holds.winfo_children():
            w.destroy()
        rows = []
        for h in (dom.holdings if dom else []):
            nm = f"{h.name}({h.code})" if h.name else h.code
            rows.append((nm, h.eval_amount or 0, h.pnl_pct, "국내"))
        ex = _usdkrw(ovs)
        for h in (ovs.holdings if ovs else []):
            nm = f"🇺🇸 {h.name or h.code}"
            ev_krw = int((h.eval_frcr or 0) * ex)  # 외화평가×환율 원화환산(시장가)
            rows.append((nm, ev_krw, h.pnl_pct, "해외"))
        if not rows:
            tk.Label(self.holds, text="보유종목 없음 — 전액 현금. (주문 데스크에서 매수하면 채워집니다)",
                     bg=C["bg"], fg=C["muted"], font=FONT).pack(anchor="w", pady=6)
            return
        # 집중도 경고(최대 비중)
        top_w = max((v / total * 100) if total else 0 for _n, v, _p, _m in rows)
        if top_w >= 40:
            tk.Label(self.holds, text=f"⚠ 집중도 높음 — 최대 종목 비중 {top_w:.0f}%",
                     bg=C["bg"], fg=C["warn"], font=("Malgun Gothic", 8)).pack(anchor="w")
        hdr = tk.Frame(self.holds, bg=C["bg"]); hdr.pack(fill="x")
        for t, wd in (("종목", 20), ("평가액", 12), ("비중", 7), ("손익", 8)):
            tk.Label(hdr, text=t, bg=C["bg"], fg=C["muted"], font=("Malgun Gothic", 8),
                     width=wd, anchor="w").pack(side="left")
        for nm, val, pnl_pct, mkt in sorted(rows, key=lambda r: r[1], reverse=True):
            pct = (val / total * 100) if total else 0
            r = tk.Frame(self.holds, bg=C["bg"]); r.pack(fill="x", pady=1)
            tk.Label(r, text=nm, bg=C["bg"], fg=C["text"], font=FONT, width=20,
                     anchor="w").pack(side="left")
            tk.Label(r, text=(_won(val) if val else "—"), bg=C["bg"], fg=C["text"],
                     font=FONT, width=12, anchor="w").pack(side="left")
            tk.Label(r, text=f"{pct:.1f}%", bg=C["bg"], fg=C["text"], font=FONT,
                     width=7, anchor="w").pack(side="left")
            pc = C["muted"] if pnl_pct is None else (C["buy"] if pnl_pct >= 0 else C["sell"])
            tk.Label(r, text=("—" if pnl_pct is None else f"{pnl_pct:+.2f}%"), bg=C["bg"],
                     fg=pc, font=FONT, width=8, anchor="w").pack(side="left")


class WhatIfWindow(tk.Toplevel):
    """'만약에' — 기준 시점 이후 내 매매 vs 그대로 뒀으면(포트폴리오 vs 포트폴리오)."""

    def __init__(self, app: KisDesk) -> None:
        super().__init__(app, bg=C["bg"])
        self.app = app
        self.cfg = app.cfg
        self.anchor_n = None     # None=전체, 정수=최근 N개 매매를 기준 이후로
        self._res = None         # 마지막 fetch 결과(앵커 변경 시 재조회 없이 재렌더)
        self.title("만약에 — 기준 시점 이후 내 매매 vs 그대로 뒀으면")
        self.geometry("700x540")
        self.configure(bg=C["bg"])

        top = tk.Frame(self, bg=C["panel"]); top.pack(fill="x")
        tk.Label(top, text="🔀 만약에 — 내 매매 vs 그대로 뒀으면",
                 bg=C["panel"], fg=C["amber"], font=FONT_BIG, pady=8, padx=12).pack(side="left")
        tk.Button(top, text="↻", command=self.load, bg=C["panel2"], fg=C["text"],
                  relief="flat", font=FONT_B, padx=10, cursor="hand2", bd=0).pack(
            side="right", padx=10, pady=6)

        # 기준(앵커) 선택 — 그 시점 포트폴리오를 고정하고 이후 매매만 비교
        anc = tk.Frame(self, bg=C["bg"]); anc.pack(fill="x", padx=12, pady=(8, 2))
        tk.Label(anc, text="기준:", bg=C["bg"], fg=C["muted"], font=FONT).pack(side="left")
        self._anchor_btns = {}
        for label, n in (("전체", None), ("최근 10", 10), ("최근 5", 5), ("최근 3", 3)):
            b = tk.Button(anc, text=label, command=lambda nn=n: self._set_anchor(nn),
                          bg=C["panel"], fg=C["muted"], relief="flat", font=FONT,
                          padx=10, pady=2, cursor="hand2", bd=0)
            b.pack(side="left", padx=3)
            self._anchor_btns[n] = b

        self.lbl_sum = tk.Label(self, text="불러오는 중…", bg=C["bg"], fg=C["text"],
                                font=FONT, anchor="w", justify="left", padx=12, pady=8)
        self.lbl_sum.pack(fill="x")

        # 스크롤 본문
        wrap = tk.Frame(self, bg=C["bg"]); wrap.pack(fill="both", expand=True, padx=12, pady=4)
        cv = tk.Canvas(wrap, bg=C["bg"], highlightthickness=0)
        sb = ttk.Scrollbar(wrap, orient="vertical", command=cv.yview)
        self.body = tk.Frame(cv, bg=C["bg"])
        self.body.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
        win = cv.create_window((0, 0), window=self.body, anchor="nw")
        cv.bind("<Configure>", lambda e: cv.itemconfig(win, width=e.width))
        cv.configure(yscrollcommand=sb.set)
        cv.pack(side="left", fill="both", expand=True); sb.pack(side="right", fill="y")
        self.bind("<MouseWheel>", lambda e: cv.yview_scroll(int(-e.delta / 120), "units"))
        self.load()

    def load(self) -> None:
        self.lbl_sum.config(text="현재가·잔고 조회 중…")
        records = kd.load_decisions()

        def price_fn(market, code):
            if market == "us":
                return fetch_us_quote(code, cfg=self.cfg).price
            return fetch_quote(code, cfg=self.cfg).price

        def work():
            ev = kd.evaluate(records, price_fn)
            dom = fetch_balance(cfg=self.cfg)
            try:
                ovs = fetch_overseas_balance(cfg=self.cfg)
            except KisError:
                ovs = None
            if ovs and ovs.total_asset_krw is not None:
                actual = ovs.total_asset_krw
                u = next((c for c in ovs.foreign_cash if c.currency == "USD"), None)
                usd_rate = u.exchange_rate if u else None
            else:
                actual = (dom.total_eval if dom else None) or (dom.net_asset if dom else None)
                usd_rate = None
            return {"ev": ev, "actual": actual, "usd_rate": usd_rate}

        def done(res, err):
            if not self.winfo_exists():
                return
            if err:
                self.lbl_sum.config(text=f"오류: {err}")
                return
            self._res = res
            self._render()

        self.app._async(work, done)

    def _set_anchor(self, n) -> None:
        self.anchor_n = n
        if self._res is not None:
            self._render()

    def _render(self) -> None:
        # 앵커 버튼 하이라이트
        for n, b in self._anchor_btns.items():
            on = (n == self.anchor_n)
            b.config(fg=(C["amber"] if on else C["muted"]),
                     bg=(C["panel2"] if on else C["panel"]))
        if self._res is None:
            return
        res = self._res
        for w in self.body.winfo_children():
            w.destroy()
        all_rows = res["ev"]["rows"]                 # 최신순
        rows = all_rows[:self.anchor_n] if self.anchor_n else all_rows  # 기준 이후만
        pb = kd.portfolio_branches(rows, res["actual"], res["usd_rate"])
        branches = pb["branches"]
        if not branches:
            self.lbl_sum.config(
                text="아직 체결된 매매가 없습니다.\n주문 데스크에서 [체결]하면 그 선택마다 "
                     "'안 했으면 포트폴리오가 얼마였을까' 분기가 자동으로 만들어집니다.")
            return

        actual = pb["actual_total"]; nt = pb["no_trade_total"]; contrib = pb["my_contribution"]
        anchor_word = (f"기준 시점(최근 {self.anchor_n}개 매매 전)에 그대로 뒀으면"
                       if self.anchor_n else "전혀 매매 안 했으면")
        head = f"실제 포트폴리오   {_won(actual)}   (기준 이후 매매 {len(branches)}건)"
        if nt is not None and contrib is not None:
            sign = "+" if contrib >= 0 else ""
            head += (f"\n{anchor_word}   {_won(nt)}"
                     f"   →   내 매매가 포트폴리오를 전체 {sign}{contrib:,}원")
        self.lbl_sum.config(text=head, fg=(C["ok"] if (contrib or 0) >= 0 else C["err"]))

        tk.Label(self.body, text="── 분기: 이 선택을 안 했다면 포트폴리오는? (자동, 선택마다) ──",
                 bg=C["bg"], fg=C["amber"], font=FONT_B, anchor="w").pack(fill="x", pady=(2, 4))
        hdr = tk.Frame(self.body, bg=C["bg"]); hdr.pack(fill="x")
        for t, wd in (("시각", 8), ("안 했을 선택", 22), ("체결→현재", 18),
                      ("그 분기 포폴", 15), ("이 선택 효과", 14)):
            tk.Label(hdr, text=t, bg=C["bg"], fg=C["muted"], font=("Malgun Gothic", 8),
                     width=wd, anchor="w").pack(side="left")

        # '전혀 매매 안 함' 분기(헤드)
        if nt is not None:
            f = tk.Frame(self.body, bg=C["panel2"]); f.pack(fill="x", pady=(1, 3))
            tk.Label(f, text="—", bg=C["panel2"], fg=C["muted"], font=("Malgun Gothic", 8),
                     width=8, anchor="w").pack(side="left")
            tk.Label(f, text=("🚫 기준 시점에 멈췄으면" if self.anchor_n else "🚫 전혀 매매 안 함"),
                     bg=C["panel2"], fg=C["text"], font=FONT_B,
                     width=22, anchor="w").pack(side="left")
            tk.Label(f, text="", bg=C["panel2"], width=18).pack(side="left")
            tk.Label(f, text=_won(nt), bg=C["panel2"], fg=C["text"], font=FONT_B,
                     width=15, anchor="w").pack(side="left")
            diff = (actual - nt) if (actual is not None and nt is not None) else 0
            dcol = C["ok"] if diff >= 0 else C["err"]
            tk.Label(f, text=f"{diff:+,}원", bg=C["panel2"], fg=dcol, font=FONT_B,
                     width=14, anchor="w").pack(side="left")

        for b in branches:
            sd = "매수" if b["side"] == "buy" else "매도"
            acc = C["buy"] if b["side"] == "buy" else C["sell"]
            f = tk.Frame(self.body, bg=C["panel"]); f.pack(fill="x", pady=1)
            tk.Label(f, text=b["ts"][-5:], bg=C["panel"], fg=C["muted"],
                     font=("Malgun Gothic", 8), width=8, anchor="w").pack(side="left")
            tk.Label(f, text=f"[{sd}] {b['name']} {b['qty']}", bg=C["panel"], fg=acc,
                     font=FONT, width=22, anchor="w").pack(side="left")
            cur = f"{b['cur']:,.2f}" if b["cur"] else "—"
            tk.Label(f, text=f"{b['price']:,.0f}→{cur}", bg=C["panel"], fg=C["muted"],
                     font=("Malgun Gothic", 8), width=18, anchor="w").pack(side="left")
            wt = _won(b["without_total"]) if b["without_total"] is not None else "—"
            tk.Label(f, text=wt, bg=C["panel"], fg=C["text"], font=FONT,
                     width=15, anchor="w").pack(side="left")
            if b["delta_krw"] is None:
                dtxt, dcol = "환율없음", C["muted"]
            else:
                dcol = C["ok"] if b["delta_krw"] >= 0 else C["err"]
                dtxt = f"{b['delta_krw']:+,}원"
            tk.Label(f, text=dtxt, bg=C["panel"], fg=dcol, font=FONT_B,
                     width=14, anchor="w").pack(side="left")


def _run_flow_read(code6: str, name: str | None = None):
    """module_flow 서브프로세스 실행 → 오늘 JSON 읽어 해당 티커 행 반환.
    KIS 권위 현재가로 올바른 상장시장(.KS/.KQ)을 판별한다(코스닥이 .KS로 잘못
    잡히는 것 방지). (row, tkr) 또는 (None, None)."""
    import json
    import subprocess
    from datetime import date

    ref = None  # KIS 권위 현재가
    try:
        ref = fetch_quote(code6).price
    except Exception:
        ref = None

    out_path = REPO_ROOT / "out" / "flow" / f"{date.today().isoformat()}.json"
    fallback = None
    for suf in (".KS", ".KQ"):
        tkr = code6 + suf
        cmd = [sys.executable, "-X", "utf8", "-m", "module_flow", tkr,
               "--bench", "^KS11", "--no-short"]
        if name:
            cmd += ["--names", name]
        cmd += ["--json"]
        try:
            subprocess.run(cmd, capture_output=True, text=True,
                           cwd=str(REPO_ROOT), timeout=120)
        except Exception:
            continue
        if not out_path.exists():
            continue
        try:
            data = json.load(open(out_path, encoding="utf-8"))
        except Exception:
            continue
        row = next((d for d in data if d.get("ticker") == tkr), None)
        if not row:
            continue
        pr = row.get("price") or {}
        last = pr.get("last")
        if not last or pr.get("error"):
            continue
        # 권위 현재가와 ±3% 이내면 올바른 시장 — 즉시 반환
        if ref and abs(last / ref - 1.0) <= 0.03:
            return row, tkr
        if fallback is None:
            fallback = (row, tkr)
    # 권위가격 매칭 실패 시 첫 유효 후보(ref 없을 때 등)
    return fallback if fallback else (None, None)


class MoversWindow(tk.Toplevel):
    """🔥 인기종목 — 등락률 상승/하락 top5 + 거래량 상위. 행 클릭 → 흐름조회."""

    def __init__(self, app: KisDesk) -> None:
        super().__init__(app, bg=C["bg"])
        self.app = app
        self.cfg = app.cfg
        self.title("인기종목")
        self.geometry("470x640")
        self.configure(bg=C["bg"])

        top = tk.Frame(self, bg=C["panel"]); top.pack(fill="x")
        tk.Label(top, text="🔥 인기종목", bg=C["panel"], fg=C["amber"],
                 font=FONT_BIG, pady=8, padx=12).pack(side="left")
        tk.Button(top, text="↻", command=self.load, bg=C["panel2"], fg=C["text"],
                  relief="flat", font=FONT_B, padx=10, cursor="hand2", bd=0).pack(
            side="right", pady=6, padx=8)
        tk.Label(self, text="행 클릭 → 흐름(수급) 조회로 연결", bg=C["bg"],
                 fg=C["muted"], font=("Malgun Gothic", 8), anchor="w").pack(
            fill="x", padx=12)
        self.body = tk.Frame(self, bg=C["bg"]); self.body.pack(
            fill="both", expand=True, padx=12, pady=6)
        self.load()

    def load(self) -> None:
        for w in self.body.winfo_children():
            w.destroy()
        tk.Label(self.body, text="불러오는 중…", bg=C["bg"], fg=C["muted"],
                 font=FONT).pack(pady=20)

        def fetch():
            return (fetch_fluctuation(True, 5, self.cfg),
                    fetch_fluctuation(False, 5, self.cfg),
                    fetch_volume_rank(5, self.cfg))

        def done(res, err):
            if not self.winfo_exists():
                return
            for w in self.body.winfo_children():
                w.destroy()
            if err:
                tk.Label(self.body, text=f"오류: {err}", bg=C["bg"], fg=C["err"],
                         font=FONT, wraplength=430, justify="left").pack(anchor="w")
                return
            up, down, vol = res
            self._section("📈 상승 top5", up)
            self._section("📉 하락 top5", down)
            self._section("🔊 거래량 상위 (ETF 포함)", vol)

        self.app._async(fetch, done)

    def _section(self, title: str, rows) -> None:
        tk.Label(self.body, text=title, bg=C["bg"], fg=C["amber"], font=FONT_B,
                 anchor="w").pack(fill="x", pady=(8, 2))
        if not rows:
            tk.Label(self.body, text="  (없음)", bg=C["bg"], fg=C["muted"],
                     font=FONT, anchor="w").pack(fill="x")
            return
        for r in rows:
            f = tk.Frame(self.body, bg=C["panel"], cursor="hand2")
            f.pack(fill="x", pady=1)
            chg = f"{r.change_pct:+.2f}%" if r.change_pct is not None else "—"
            ccol = C["ok"] if (r.change_pct or 0) >= 0 else C["err"]
            tk.Label(f, text=r.name, bg=C["panel"], fg=C["text"], font=FONT,
                     width=15, anchor="w").pack(side="left", padx=(8, 2))
            tk.Label(f, text=r.code, bg=C["panel"], fg=C["muted"],
                     font=("Malgun Gothic", 8), width=7).pack(side="left")
            tk.Label(f, text=_won(r.price), bg=C["panel"], fg=C["text"], font=FONT,
                     width=11, anchor="e").pack(side="left")
            tk.Label(f, text=chg, bg=C["panel"], fg=ccol, font=FONT_B,
                     width=8, anchor="e").pack(side="left", padx=(4, 8))
            for w in (f, *f.winfo_children()):
                w.bind("<Button-1>",
                       lambda e, c=r.code, n=r.name: self.app.open_flow(c, n))


class FlowWindow(tk.Toplevel):
    """🌊 흐름(수급) — flow_read 4축 조회(읽기전용). 진입 검증용."""

    def __init__(self, app: KisDesk, code: str | None = None,
                 name: str | None = None) -> None:
        super().__init__(app, bg=C["bg"])
        self.app = app
        self.cfg = app.cfg
        self.title("흐름(수급) 조회")
        self.geometry("540x480")
        self.configure(bg=C["bg"])
        self._cur_code = None

        tk.Label(self, text="🌊 흐름(수급)", bg=C["panel"], fg=C["amber"],
                 font=FONT_BIG, pady=8, padx=12).pack(fill="x")
        form = tk.Frame(self, bg=C["panel2"], padx=12, pady=8); form.pack(fill="x")
        tk.Label(form, text="종목코드", bg=C["panel2"], fg=C["muted"],
                 font=("Malgun Gothic", 8)).pack(side="left")
        self.e = tk.Entry(form, width=10, bg=C["bg"], fg=C["text"],
                          insertbackground=C["text"], relief="flat", font=FONT)
        self.e.pack(side="left", padx=6)
        self.e.bind("<Return>", lambda ev: self.query(self.e.get().strip()))
        tk.Button(form, text="흐름 조회", command=lambda: self.query(self.e.get().strip()),
                  bg=C["amber"], fg="#000", relief="flat", font=FONT_B, padx=10,
                  cursor="hand2", bd=0).pack(side="left", padx=4)
        self.btn_order = tk.Button(form, text="＋ 주문 폼에 넣기", command=self._to_order,
                                   bg=C["panel"], fg=C["text"], relief="flat", font=FONT_B,
                                   padx=10, cursor="hand2", bd=0, state="disabled")
        self.btn_order.pack(side="right")

        self.result = tk.Frame(self, bg=C["bg"]); self.result.pack(
            fill="both", expand=True, padx=12, pady=8)
        tk.Label(self.result,
                 text="종목코드 입력 후 [흐름 조회]\n뉴스속도·OBV매집/분산·RS·거래량서지·투자자별 순매수",
                 bg=C["bg"], fg=C["muted"], font=FONT, justify="left").pack(anchor="w")
        if code:
            self.query(code, name)

    def query(self, code: str, name: str | None = None) -> None:
        code = (code or "").strip().upper().replace(".KS", "").replace(".KQ", "")
        if not code:
            return
        self.e.delete(0, "end"); self.e.insert(0, code)
        self._cur_code = None
        self.btn_order.config(state="disabled")
        for w in self.result.winfo_children():
            w.destroy()
        tk.Label(self.result, text=f"{code} 흐름 조회 중… (수급·yfinance ~10초)",
                 bg=C["bg"], fg=C["muted"], font=FONT).pack(anchor="w")

        def fetch():
            return _run_flow_read(code, name)

        def done(res, err):
            if not self.winfo_exists():
                return
            for w in self.result.winfo_children():
                w.destroy()
            if err or not res or not res[0]:
                tk.Label(self.result,
                         text=f"조회 실패: {err or '데이터 없음(.KS/.KQ 모두)'}",
                         bg=C["bg"], fg=C["err"], font=FONT, wraplength=500,
                         justify="left").pack(anchor="w")
                return
            self._cur_code = code
            self.btn_order.config(state="normal")
            self._render(res[0], res[1], name)

        self.app._async(fetch, done)

    def _render(self, row: dict, tkr: str, name: str | None) -> None:
        tag = row.get("tag", "?")
        pr = row.get("price") or {}
        nw = row.get("news") or {}
        iv = row.get("investor") or {}
        tk.Label(self.result, text=f"{name or ''} {tkr}   {tag}".strip(),
                 bg=C["bg"], fg=C["text"], font=FONT_BIG, anchor="w").pack(fill="x")
        last = pr.get("last")
        tk.Label(self.result, text=(f"현재가 {int(last):,}원" if last else "현재가 —"),
                 bg=C["bg"], fg=C["text"], font=FONT_B, anchor="w").pack(
            fill="x", pady=(2, 6))

        def line(txt, col=None):
            tk.Label(self.result, text=txt, bg=C["bg"], fg=col or C["text"],
                     font=FONT, anchor="w", justify="left").pack(fill="x")

        vel = nw.get("velocity")
        line(f"뉴스속도   {vel}x" + ("   ▲관심 가속" if (vel or 0) > 1.2 else ""))
        line(f"OBV        {pr.get('obv_state', '?')}   (기울기 {pr.get('obv_norm')})")
        line(f"RS20/RS60  {pr.get('rs20')}% / {pr.get('rs60')}%   (벤치대비 +면 이김)")
        vs = pr.get("vol_surge")
        line(f"거래량서지  {vs}x" + ("   ▲돈 유입" if (vs or 0) > 1.3 else ""))
        f20, i20, r20 = iv.get("foreign_20"), iv.get("inst_20"), iv.get("indiv_20")
        if f20 is not None:
            if iv.get("smart_buy"):
                sm, sc = "   ★진짜손(외/기 순매수)", C["ok"]
            elif iv.get("distribution_to_ret"):
                sm, sc = "   ⚠개인 흡수(외국인 이탈)", C["warn"]
            else:
                sm, sc = "", C["muted"]
            line(f"수급20d    외 {f20/10000:+,.0f}만 · 기 {i20/10000:+,.0f}만 · "
                 f"개 {r20/10000:+,.0f}만주{sm}", sc)
        note = {"🟢가속": "돈 들어오는 중·서사 가속 — 단 하드스탑 필수(꼭지위험).",
                "🟡중립": "일부 소진·잔여만 — 확증 대기.",
                "🔴분산": "이미 반영/분산 — 지금 진입 아님(watch)."}.get(tag, "")
        if note:
            tk.Label(self.result, text=note, bg=C["bg"], fg=C["amber"], font=FONT,
                     wraplength=500, justify="left").pack(fill="x", pady=(10, 0))

    def _to_order(self) -> None:
        if self._cur_code:
            self.app.prefill_order(self._cur_code)


def main() -> None:
    try:
        KisDesk().mainloop()
    except Exception:
        import traceback
        tb = traceback.format_exc()
        _log_error("시작", tb)
        try:
            import tkinter.messagebox as mb
            mb.showerror("KIS 데스크 시작 오류", tb[-1500:])
        except Exception:
            pass
        raise


if __name__ == "__main__":
    main()
