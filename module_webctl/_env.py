"""프로젝트 루트 .env 를 무의존 파싱해 환경변수 주입(module_kis 동일 패턴).

python-dotenv 없이도 동작. 자격증명은 코드가 아니라 .env 에만 둔다(.gitignore 처리됨).
"""
from __future__ import annotations

import os
from pathlib import Path


def load_dotenv() -> None:
    here = Path(__file__).resolve().parent
    for p in [here / ".env", here.parent / ".env", here.parent.parent / ".env"]:
        if not p.exists():
            continue
        try:
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                k, _, v = line.partition("=")
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k and v and k not in os.environ:
                    os.environ[k] = v
        except Exception:
            pass
        break


def timefolio_creds() -> tuple[str, str]:
    """(email, password). 없으면 명확한 에러 — 어디에 뭘 넣을지 안내."""
    load_dotenv()
    email = os.environ.get("TIMEFOLIO_EMAIL", "").strip()
    pw = os.environ.get("TIMEFOLIO_PASSWORD", "").strip()
    if not email or not pw:
        raise RuntimeError(
            "타임폴리오 자격증명 부재 — 프로젝트 루트 .env 에 다음 2줄을 추가하세요:\n"
            "  TIMEFOLIO_EMAIL=your@email.com\n"
            "  TIMEFOLIO_PASSWORD=yourpassword\n"
            "(.env 는 .gitignore 처리되어 커밋되지 않음)"
        )
    return email, pw
