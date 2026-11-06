"""
Shared DataWeave-equivalent runtime helpers.

Emitted once per export as ``src/shared/transformations/dw_runtime.py``.
Generated transformation modules import from here so merge/dedup/sort/CSV
logic is DRY, typed, and unit-testable.
"""
from __future__ import annotations

import csv
import io
from typing import Any, Iterable


def route_rows(payload: dict[str, Any], index: str) -> list[dict[str, Any]]:
    """Extract rows from scatter-gather indexed payload branch."""
    branch = payload.get(index) or payload.get(str(index)) or {}
    if isinstance(branch, dict):
        rows = branch.get("payload") or branch.get("records") or []
    else:
        rows = branch
    if not isinstance(rows, list):
        return [rows] if isinstance(rows, dict) else []
    return [r for r in rows if isinstance(r, dict)]


def map_fields(row: dict[str, Any], mapping: dict[str, str]) -> dict[str, Any]:
    return {target: row.get(source) for target, source in mapping.items()}


def merge_on_key(
    primary: list[dict[str, Any]],
    secondary: list[dict[str, Any]],
    key: str,
    defaults: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Left-join ``primary`` rows with ``secondary`` index on ``key`` (DataWeave mergeWith)."""
    defaults = defaults or {}
    index: dict[Any, dict[str, Any]] = {}
    for row in secondary:
        k = row.get(key)
        if k is not None:
            index[k] = row
    out: list[dict[str, Any]] = []
    for item in primary:
        k = item.get(key)
        match = index.get(k, {}) if k is not None else {}
        out.append({**defaults, **match, **item})
    return out


def distinct_by(rows: Iterable[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    seen: set[Any] = set()
    out: list[dict[str, Any]] = []
    for row in rows:
        value = row.get(key)
        if value in seen:
            continue
        if value is not None:
            seen.add(value)
        out.append(row)
    return out


def sort_by_field_presence(
    rows: list[dict[str, Any]],
    *,
    rules: list[tuple[str, str, int]],
    default_rank: int = 99,
) -> list[dict[str, Any]]:
    """Sort rows by field-presence rules parsed from a custom DataWeave ``fun``."""

    def _rank(row: dict[str, Any]) -> int:
        for present, absent, rank in rules:
            has_present = bool(str(row.get(present) or "").strip())
            has_absent = bool(str(row.get(absent) or "").strip())
            if has_present and not has_absent:
                return rank
        return default_rank

    return sorted(rows, key=_rank)


def sort_by_source_existence(
    users: list[dict[str, Any]],
    *,
    sfdc_field: str = "IDInSfdc",
    db_field: str = "IDInDb",
) -> list[dict[str, Any]]:
    """Backward-compatible alias — prefer ``sort_by_field_presence``."""
    return sort_by_field_presence(
        users,
        rules=[(sfdc_field, db_field, 1), (db_field, sfdc_field, 2)],
        default_rank=3,
    )


def project_fields(rows: list[dict[str, Any]], fields: list[str]) -> list[dict[str, Any]]:
    return [{f: row.get(f) for f in fields} for row in rows]


def records_to_csv(rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> str:
    """Serialize rows to CSV using the standard library (DataWeave application/csv)."""
    names = fieldnames or (list(rows[0].keys()) if rows else [])
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=names, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def as_records(payload: dict[str, Any] | list[Any] | None) -> list[dict[str, Any]]:
    if isinstance(payload, dict) and isinstance(payload.get("records"), list):
        return [r for r in payload["records"] if isinstance(r, dict)]
    if isinstance(payload, list):
        return [r for r in payload if isinstance(r, dict)]
    return []


def ctx_get(payload: dict[str, Any] | list[Any], ref: str, default: Any = None) -> Any:
    """Resolve ``payload.*``, ``vars.*``, or ``attributes.*`` references from a payload envelope."""
    ref = (ref or "").strip()
    if not ref:
        return default
    if ref == "payload":
        return payload
    if ref.startswith("payload."):
        base = payload if isinstance(payload, dict) else {}
        return nested_get(base, ref[len("payload.") :], default)
    if ref.startswith("vars."):
        vars_ = payload.get("vars") if isinstance(payload, dict) else {}
        if not isinstance(vars_, dict):
            vars_ = {}
        return nested_get(vars_, ref[len("vars.") :], default)
    if ref.startswith("attributes."):
        attrs = payload.get("attributes") if isinstance(payload, dict) else {}
        if not isinstance(attrs, dict):
            attrs = {}
        return nested_get(attrs, ref[len("attributes.") :], default)
    return default


def nested_get(obj: Any, path: str, default: Any = None) -> Any:
    """Walk a dotted path (``Payments.PayeeReference.PayeeName``)."""
    cur = obj
    for part in path.split("."):
        if not part:
            continue
        if isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return default
        if cur is None:
            return default
    return cur


def loose_eq(left: Any, right: Any) -> bool:
    """DataWeave ``~=`` — string-coerce both sides for comparison."""
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return str(left) == str(right)


def concat_str(*parts: Any) -> str:
    """DataWeave ``++`` for strings — ``None`` becomes empty string."""
    return "".join("" if p is None else str(p) for p in parts)


def filter_rows(
    rows: Iterable[dict[str, Any]],
    predicate: Any,
) -> list[dict[str, Any]]:
    """Filter record rows with a callable ``predicate(row) -> bool``."""
    return [row for row in rows if predicate(row)]


def dw_write(value: Any, *, indent: bool = False) -> str:
    """Approximate DataWeave ``write(value, 'application/json', ...)``."""
    import json

    return json.dumps(value, indent=2 if indent else None, default=str)


class DWContext:
    """Runtime envelope for dynamically compiled DataWeave transforms."""

    __slots__ = ("raw", "payload", "vars", "attributes")

    def __init__(self, raw: Any):
        if isinstance(raw, dict):
            self.raw = raw
            inner = raw.get("payload", raw)
            self.payload = inner if inner is not None else raw
            self.vars = dict(raw.get("vars") or {})
            self.attributes = dict(raw.get("attributes") or {})
        else:
            self.raw = raw
            self.payload = raw
            self.vars = {}
            self.attributes = {}

    def resolve_root(self, name: str) -> Any:
        if name == "payload":
            return self.payload
        if name == "vars":
            return self.vars
        if name == "attributes":
            return self.attributes
        return None

    def get_path(self, ref: str, default: Any = None) -> Any:
        ref = (ref or "").strip()
        if not ref:
            return default
        if ref == "payload":
            return self.payload
        if ref.startswith("payload."):
            return nested_get(self.payload if isinstance(self.payload, dict) else {}, ref[8:], default)
        if ref == "vars":
            return self.vars
        if ref.startswith("vars."):
            return nested_get(self.vars, ref[5:], default)
        if ref == "attributes":
            return self.attributes
        if ref.startswith("attributes."):
            return nested_get(self.attributes, ref[11:], default)
        if ref == "p":
            return self.read_property
        return default

    def read_property(self, key: str) -> str | None:
        import os
        import re
        env = re.sub(r"[^A-Za-z0-9]+", "_", key or "").strip("_").upper()
        return os.environ.get(env or "APPLICATION_PROPERTY")

    def is_present(self, value: Any) -> bool:
        return value is not None


def dw_property(key: str, default: str = "") -> str:
    """DataWeave p('property.key') helper mapping to environment configuration."""
    import os
    import re
    if not key:
        return default
    env_name = re.sub(r"[^A-Za-z0-9]+", "_", key).strip("_").upper()
    return os.environ.get(env_name, os.environ.get(key, default))



def as_list(value: Any) -> list[Any]:
    """Coerce DW collection values to a list for iteration."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        records = value.get("records")
        if isinstance(records, list):
            return records
        return [value]
    return [value]


def merge_objects(left: Any, right: Any) -> dict[str, Any]:
    """DataWeave ``mergeWith`` — second object wins on key conflicts."""
    l = left if isinstance(left, dict) else {}
    r = right if isinstance(right, dict) else {}
    return {**l, **r}


def join_values(items: Any, separator: str = "") -> str:
    """DataWeave ``joinBy`` for arrays."""
    seq = as_list(items)
    return separator.join("" if x is None else str(x) for x in seq)


def distinct_by_selector(rows: Any, selector: Any) -> list[Any]:
    """``distinctBy`` when selector is ``$.field`` or a lambda."""
    seq = [r for r in as_list(rows) if isinstance(r, dict)]
    if isinstance(selector, str):
        return distinct_by(seq, selector)
    seen: set[Any] = set()
    out: list[Any] = []
    for row in seq:
        key = selector(row) if callable(selector) else row
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def sort_by_selector(rows: Any, selector: Any, *, descending: bool = False) -> list[Any]:
    seq = as_list(rows)
    if callable(selector):
        return sorted(seq, key=selector, reverse=descending)
    if isinstance(selector, str):
        return sorted(
            seq,
            key=lambda r: (r.get(selector) is None, r.get(selector)) if isinstance(r, dict) else r,
            reverse=descending,
        )
    return list(seq)


def group_by_selector(rows: Any, selector: Any) -> dict[Any, list[Any]]:
    grouped: dict[Any, list[Any]] = {}
    for row in as_list(rows):
        if isinstance(row, dict):
            key = selector(row) if callable(selector) else row.get(selector)
        else:
            key = selector(row) if callable(selector) else row
        grouped.setdefault(key, []).append(row)
    return grouped


def dw_now() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).isoformat()


def index_get(base: Any, key: Any, default: Any = None) -> Any:
    """Index dict/list/string with DataWeave-style keys."""
    if base is None:
        return default
    if isinstance(base, str):
        try:
            idx = int(key)
            return base[idx]
        except (IndexError, TypeError, ValueError):
            return default
    if isinstance(base, dict):
        sk = str(key) if key is not None else key
        if sk in base:
            return base[sk]
        if isinstance(key, int) and str(key) in base:
            return base[str(key)]
        return default
    if isinstance(base, (list, tuple)):
        idx = int(key) if isinstance(key, (int, float)) else key
        try:
            return base[idx]
        except (IndexError, KeyError, TypeError, ValueError):
            return default
    return default


def first_or(value: Any, default: Any) -> Any:
    """``(items filter ...)[0] default {...}`` — safe first element."""
    if isinstance(value, list):
        return value[0] if value else default
    if value in (None, ""):
        return default
    return value


def dw_plus(left: Any, right: Any) -> Any:
    """DataWeave ``++`` for objects/strings (non-list operands)."""
    if isinstance(left, dict) or isinstance(right, dict):
        l = left if isinstance(left, dict) else {}
        r = right if isinstance(right, dict) else {}
        return merge_objects(l, r)
    return concat_str(left, right)


def dw_concat(left: Any, right: Any) -> Any:
    """DataWeave ``++`` — list concat or object/string merge."""
    if isinstance(left, list) or isinstance(right, list):
        return as_list(left) + as_list(right)
    return dw_plus(left, right)


def remove_field(row: Any, field: str) -> Any:
    """DataWeave ``$ - \"field\"`` — copy object without one key."""
    if not isinstance(row, dict):
        return row
    out = dict(row)
    out.pop(field, None)
    return out


def dw_range(start: Any, end: Any) -> list[int]:
    """DataWeave ``start to end`` inclusive range."""
    try:
        lo = int(start)
        hi = int(end)
    except (TypeError, ValueError):
        return []
    if lo <= hi:
        return list(range(lo, hi + 1))
    return list(range(lo, hi - 1, -1))


def dw_lower(value: Any) -> str:
    return "" if value is None else str(value).lower()


def dw_upper(value: Any) -> str:
    return "" if value is None else str(value).upper()


def dw_size(value: Any) -> int:
    if value is None:
        return 0
    if isinstance(value, (str, list, dict, tuple)):
        return len(value)
    return 0


def dw_random_int(max_inclusive: Any) -> int:
    import random

    try:
        upper = int(max_inclusive)
    except (TypeError, ValueError):
        return 0
    return random.randint(0, upper)


def dw_slice(items: Any, start: Any, end: Any | None = None) -> list[Any]:
    seq = as_list(items)
    try:
        s = int(start)
        e = int(end) if end is not None else len(seq)
    except (TypeError, ValueError):
        return seq
    return seq[s:e]


def dw_index_of(items: Any, value: Any) -> int:
    seq = as_list(items)
    try:
        return seq.index(value)
    except ValueError:
        return -1


def str_contains(haystack: Any, needle: Any) -> bool:
    if haystack is None or needle is None:
        return False
    return str(needle) in str(haystack)


def str_starts_with(value: Any, prefix: Any) -> bool:
    if value is None or prefix is None:
        return False
    return str(value).startswith(str(prefix))


def str_ends_with(value: Any, suffix: Any) -> bool:
    if value is None or suffix is None:
        return False
    return str(value).endswith(str(suffix))


def str_substring_after(value: Any, marker: Any) -> str:
    text = "" if value is None else str(value)
    mark = "" if marker is None else str(marker)
    idx = text.find(mark)
    return text[idx + len(mark) :] if idx >= 0 else text


def str_substring_before(value: Any, marker: Any) -> str:
    text = "" if value is None else str(value)
    mark = "" if marker is None else str(marker)
    idx = text.find(mark)
    return text[:idx] if idx >= 0 else text


def as_datetime(value: Any) -> Any:
    from datetime import datetime

    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    text = str(value)
    for fmt in (
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d",
    ):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return value


def as_number(value: Any) -> float | int | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return value
    try:
        text = str(value)
        return int(text) if "." not in text else float(text)
    except ValueError:
        return None


# Template copied verbatim into export ZIP (see TransformationGenerator).
DW_RUNTIME_MODULE = __name__.split(".")[-1]  # "dw_runtime"
