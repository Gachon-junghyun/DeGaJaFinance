# -*- coding: utf-8 -*-
"""module_epistemics CLI — 서브커맨드 (audit / adjudicate / sensitivity / verify)."""
from __future__ import annotations

import argparse

from ._bayes import cli_register as _reg_adjudicate
from ._config import utf8_stdout
from ._registry_audit import cli_register as _reg_audit
from ._sensitivity import cli_register as _reg_sensitivity
from ._verify import cli_register as _reg_verify

REGISTRARS = [_reg_audit, _reg_adjudicate, _reg_sensitivity, _reg_verify]


def main() -> None:
    utf8_stdout()
    ap = argparse.ArgumentParser(
        prog="module_epistemics",
        description="인식 루프 — 베이지안 충돌평가·민감도 학습·verify·registry_audit")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for reg in REGISTRARS:
        reg(sub)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
