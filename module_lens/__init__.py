# -*- coding: utf-8 -*-
"""Question ledger and price data APIs; dependencies load only when used."""
from importlib import import_module

_DATA = {"build", "status", "connect", "panels", "article_frame", "vectors"}
_LEDGER = {"ask", "ev", "think", "resolve", "due", "show", "reindex",
           "export_jsonl", "import_jsonl", "LedgerError", "KINDS"}
__all__ = sorted(_DATA | _LEDGER | {"ledger_connect", "find", "hook_prompt"})


def __getattr__(name):
    """Keep the original price API; ledger_connect opens the separate ledger."""
    if name == "ledger_connect":
        value = import_module("._ledger", __name__).connect
    elif name in _DATA:
        value = getattr(import_module("._data", __name__), name)
    elif name in _LEDGER:
        value = getattr(import_module("._ledger", __name__), name)
    elif name in {"find", "hook_prompt"}:
        value = getattr(import_module("._search", __name__), name)
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(globals()) | set(__all__))

