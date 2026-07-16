"""module_timefolio — 타임폴리오 투자대회(RFM) 웹 자동매매 어댑터.

module_webctl(CDP) 위에 얹혀 로그인·계좌조회·보유조회·주문(비중% 기반)을 수행.
대회는 '타깃 비중(%)' 모델 → 데스크의 % 사이징과 1:1 매핑.

★ 안전: place_order 는 기본 드라이런(모달 채우고 스크린샷만, 제출 안 함).
   실제 '주문 제출'은 execute=True + 환경 arming(TIMEFOLIO_EXECUTE=1)일 때만.
   Claude 임의 발사 없음 — 상위 스케줄러/사용자가 arming.
"""
from __future__ import annotations

import os
import re
import time
from dataclasses import dataclass, field
from typing import Optional

from module_webctl import WebController
from module_webctl._env import timefolio_creds

__all__ = ["Timefolio", "Holding", "Account"]

PRC_TYPES = {"Opp", "My", "Limit", "Stop"}  # 상대호가/자기호가/지정가/STOP


@dataclass
class Holding:
    code: str
    name: str
    weight: float          # 보유 비중 %
    eval_manwon: float     # 평가액(만원)
    pnl_pct: Optional[float] = None


@dataclass
class Account:
    nav: Optional[float] = None
    ret_pct: Optional[float] = None
    rank: Optional[int] = None
    total: Optional[int] = None
    turnover_week: Optional[float] = None      # 금주 회전율 %
    violations_cum: Optional[int] = None        # 누적 위반 횟수
    raw_nav_text: str = ""


def _num(s: str) -> Optional[float]:
    if s is None:
        return None
    m = re.search(r"-?\d[\d,]*\.?\d*", s.replace("−", "-"))
    return float(m.group().replace(",", "")) if m else None


class Timefolio:
    ORDER_URL = "https://contest.timefolio.net/"

    def __init__(self, w: WebController):
        self.w = w

    @classmethod
    def attach(cls, *, port: int = 9222, ensure_login: bool = True) -> "Timefolio":
        w = WebController.attach(match_url="timefolio", port=port)
        tf = cls(w)
        if ensure_login:
            tf.ensure_login()
        return tf

    # ── 로그인 ────────────────────────────────────────────────────
    def logged_in(self) -> bool:
        return not self.w.exists("#password") and self.w.exists("input")

    def ensure_login(self, *, timeout: float = 15.0) -> bool:
        if not self.w.exists("#password"):
            return True
        email, pw = timefolio_creds()
        self.w.fill("#email", email)
        self.w.fill("#password", pw)
        self.w.click(".btn-primary") or self.w.click_text("Submit")
        ok = self.w.wait_gone("#password", timeout=timeout)
        time.sleep(1.5)
        return ok

    def go_order(self) -> None:
        """주문 탭으로 이동(SPA)."""
        if not self.w.exists("#매수도_true"):
            self.w.click_text("주문", tag="a", exact=True) or self.w.click_text("주문")
            time.sleep(1.2)

    # ── 계좌 읽기 ──────────────────────────────────────────────────
    def read_account(self) -> Account:
        self.go_order()
        nav_text = self.w.eval(r"""(()=>{
          const b=Array.from(document.querySelectorAll('*')).find(e=>/NAV/.test(e.innerText||'')&&(e.innerText||'').length<60);
          return b? b.parentElement.innerText.replace(/\n/g,' ') : '';
        })()""") or ""
        acc = Account(raw_nav_text=nav_text[:120])
        m = re.search(r"NAV\s*([\d,]+\.?\d*).*?\(([-\d.]+)%\)\s*([\d,]+)\s*위\s*/\s*([\d,]+)", nav_text)
        if m:
            acc.nav = _num(m.group(1)); acc.ret_pct = _num(m.group(2))
            acc.rank = int(_num(m.group(3))); acc.total = int(_num(m.group(4)))
        # 주간 회전율 (가이드라인 표 '금주 X%')
        tv = self.w.eval(r"""(()=>{
          const m=(document.body.innerText||'').match(/금주\s*([\d.]+)\s*%/); return m? m[1]:null;})()""")
        acc.turnover_week = _num(tv) if tv else None
        # 누적 위반 (가이드라인 표 '누적N번 위반')
        cv = self.w.eval(r"""(()=>{
          const m=(document.body.innerText||'').match(/누적\s*(\d+)\s*번\s*위반/); return m? m[1]:null;})()""")
        acc.violations_cum = int(_num(cv)) if cv else None
        return acc

    # ── 보유 읽기 ──────────────────────────────────────────────────
    def _table_rows_by_header(self, *keywords: str) -> list[list[str]]:
        """헤더에 keywords 전부 포함하는 table 의 데이터 셀 행 반환."""
        js = r"""(kw=>{
          const tbls=Array.from(document.querySelectorAll('table'));
          const t=tbls.find(t=>{const h=(t.innerText||'').slice(0,200); return kw.every(k=>h.includes(k));});
          if(!t) return [];
          return Array.from(t.rows).map(r=>Array.from(r.cells).map(c=>(c.innerText||'').replace(/\s+/g,' ').trim()));
        })(%s)""" % (list(keywords),)
        return self.w.eval(js) or []

    def read_holdings(self) -> list[Holding]:
        self.go_order()
        rows = self._table_rows_by_header("잔고", "평단가")
        out: list[Holding] = []
        for r in rows:
            if not r:
                continue
            code = r[0].strip()
            m = re.fullmatch(r"A?(\d{6})", code)   # KRX UI는 'A012450' 접두 → 6자리 정규화
            if not m:                               # 데이터행(종목코드)만, 헤더/Totals 스킵
                continue
            code = m.group(1)                       # 책 code6 키와 매칭되도록 'A' 제거
            # 컬럼: 코드|종목명|현재가|당일%|잔고|비중%|평가액만원|평단가|손익%|손익만원
            def g(i): return r[i] if i < len(r) else ""
            out.append(Holding(
                code=code, name=g(1),
                weight=_num(g(5)) or 0.0,
                eval_manwon=_num(g(6)) or 0.0,
                pnl_pct=_num(g(8)),
            ))
        return out

    # ── 주문 (비중% 기반) ─────────────────────────────────────────
    def _open_modal(self) -> bool:
        self.go_order()
        if self.w.exists("#매수도_true"):   # 이미 열림
            return True
        self.w.click_text("신규 주문")
        return self.w.wait_for("#매수도_true", timeout=6)

    def close_modal(self) -> None:
        if self.w.exists("#매수도_true"):
            self.w.click_text("닫기", tag="button", exact=True)
            time.sleep(0.4)

    def _pick_stock(self, code: str, *, timeout: float = 6.0) -> bool:
        """종목 선택 검색창에 코드 입력 → 드롭다운 첫 항목 선택."""
        sel = "input[placeholder='종목 선택']"
        if not self.w.exists(sel):
            return False
        self.w.focus(sel)
        self.w.fill(sel, code)
        # react-select/autocomplete 드롭다운 대기 후 코드 포함 옵션 클릭
        deadline = time.time() + timeout
        while time.time() < deadline:
            picked = self.w.eval(f"""(()=>{{
              const opts=Array.from(document.querySelectorAll('[role=option],li,.option,[class*=option]'))
                .filter(e=>e.offsetParent!==null && (e.innerText||'').includes('{code}'));
              if(opts.length){{opts[0].click(); return true;}} return false;}})()""")
            if picked:
                time.sleep(0.4)
                return True
            time.sleep(0.3)
        # 폴백: Enter
        self.w.focus(sel); self.w.press_key("Enter"); time.sleep(0.4)
        return self.w.eval(r"""(()=>!/종목 미선택/.test(document.body.innerText))()""")

    def place_order(
        self,
        code: str,
        side: str,                 # 'buy' | 'sell'
        weight_pct: float,
        *,
        prc_ty: str = "Opp",
        immediate: bool = True,
        execute: bool = False,
        shot: Optional[str] = None,
    ) -> dict:
        """비중% 주문. 기본 드라이런(제출 안 함). execute=True + TIMEFOLIO_EXECUTE=1 이면 제출."""
        assert side in ("buy", "sell")
        assert prc_ty in PRC_TYPES
        armed = os.environ.get("TIMEFOLIO_EXECUTE", "").strip() == "1"
        result = {"code": code, "side": side, "weight": weight_pct, "prc_ty": prc_ty,
                  "execute_requested": execute, "armed": armed, "submitted": False, "dryrun": True}

        if not self._open_modal():
            result["error"] = "모달 열기 실패"
            return result
        # 매수/매도
        self.w.click("#매수도_true" if side == "buy" else "#매수도_false")
        # 종목
        if not self._pick_stock(code):
            result["error"] = f"종목 선택 실패({code})"
            self.close_modal(); return result
        # 주문 비중(%)
        filled = self.w.eval(f"""(()=>{{
          const ins=Array.from(document.querySelectorAll('input[type=number]'));
          const el=ins.find(e=>e.offsetParent!==null);  // 첫 가시 number = 주문 비중(%)
          if(!el) return false;
          const p=window.HTMLInputElement.prototype;
          Object.getOwnPropertyDescriptor(p,'value').set.call(el,'{weight_pct}');
          el.dispatchEvent(new Event('input',{{bubbles:true}}));
          el.dispatchEvent(new Event('change',{{bubbles:true}})); return true;}})()""")
        result["weight_filled"] = bool(filled)
        # 가격유형 + 즉시실행
        self.w.click(f"#prcTy_{prc_ty}")
        self.w.click("#isSlice_false" if immediate else "#isSlice_true")
        time.sleep(0.3)
        if shot:
            self.w.screenshot(shot); result["shot"] = shot

        if execute and armed:
            ok = self.w.click_text("주문 제출", tag="button", exact=True)
            time.sleep(1.2)
            gone = self.w.wait_gone("#매수도_true", timeout=6)
            result.update(submitted=bool(ok), dryrun=False, modal_closed=gone)
        else:
            self.close_modal()
            result["note"] = ("execute 요청됐으나 TIMEFOLIO_EXECUTE=1 arming 없음 → 드라이런"
                              if execute and not armed else "드라이런(제출 안 함)")
        return result

    def close(self) -> None:
        self.w.close()
