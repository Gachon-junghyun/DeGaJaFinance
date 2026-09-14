"""docx -> pdf 변환기 (Windows · Word COM).

이 리포의 보고서 조판기(`build_*_docx.py`)는 .docx 만 만든다. PDF 가 필요할 때
매번 COM 호출을 다시 짜지 않도록 여기 한 곳에 둔다 (P1 단일 원본).

    python scripts/docx_to_pdf.py REPORT/company_034020/두산에너빌리티_기업분석_20260828.docx
    python scripts/docx_to_pdf.py in.docx out.pdf

전제: Windows + Microsoft Word 설치 + pywin32. 셋 중 하나라도 없으면 그 사실을
그대로 알리고 종료한다 (조용히 빈 파일을 남기지 않는다).

⚠ Word 를 띄우므로 서버 PC(P6)에서는 쓰지 않는다 — 클라이언트 전용.
"""
from __future__ import annotations

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WD_FORMAT_PDF = 17


def convert(src: Path, dest: Path | None = None) -> Path:
    src = src.resolve()
    if not src.is_file():
        raise FileNotFoundError(f"원본이 없다: {src}")
    dest = (dest or src.with_suffix(".pdf")).resolve()
    dest.parent.mkdir(parents=True, exist_ok=True)

    try:
        import win32com.client  # noqa: PLC0415  (COM 은 실제 변환 시점에만)
    except ImportError as e:  # pragma: no cover
        raise RuntimeError("pywin32 가 없다. pip install pywin32") from e

    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = None
    try:
        doc = word.Documents.Open(str(src), ReadOnly=True, AddToRecentFiles=False)
        # 목차(TOC) 필드는 열자마자 갱신해야 PDF 에 쪽번호가 박힌다.
        try:
            doc.Fields.Update()
            for toc in doc.TablesOfContents:
                toc.Update()
        except Exception:
            pass  # 목차가 없는 문서도 있다
        doc.SaveAs2(str(dest), FileFormat=WD_FORMAT_PDF)
    finally:
        if doc is not None:
            doc.Close(SaveChanges=0)
        word.Quit()
    return dest


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    out = convert(src, dest)
    print(f"[ok] {out}  ({out.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
