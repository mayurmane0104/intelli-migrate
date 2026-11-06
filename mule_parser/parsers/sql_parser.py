"""
parsers/sql_parser.py  –  Structured semantic extraction from SQL strings.

Supports: SELECT, INSERT, UPDATE, DELETE (+ batch-style multi-statement).
Returns a SqlSemantics dict (compatible with the SqlSemantics Pydantic model)
for embedding into internal_components entries.

Design goals
────────────
• No external SQL-parsing library required (regex + state machine)
• Works on Mule's parameterised SQL with :namedParam tokens
• Handles multi-line SQL, aliases, sub-queries (extracts top-level table)
• Returns None for non-SQL text (fast rejection)
"""

from __future__ import annotations

import re

# ─── Fast rejection ───────────────────────────────────────────────────────────

_SQL_OP_RE = re.compile(
    r"^\s*(SELECT|INSERT|UPDATE|DELETE|MERGE|REPLACE)\b",
    re.IGNORECASE,
)

# ─── Field extraction patterns ────────────────────────────────────────────────

_BIND_PARAM_RE = re.compile(r":([a-zA-Z_]\w*)")       # :paramName
_IDENTIFIER_RE = re.compile(r"[a-zA-Z_]\w*")

# Clause boundary keywords (stop field extraction here)
_CLAUSE_STOP = re.compile(
    r"\b(FROM|WHERE|JOIN|LEFT|RIGHT|INNER|OUTER|FULL|CROSS|ON|GROUP|ORDER|"
    r"HAVING|LIMIT|OFFSET|UNION|RETURNING|SET|VALUES)\b",
    re.IGNORECASE,
)


# ─── Public API ───────────────────────────────────────────────────────────────

def parse_sql(raw: str | None) -> dict | None:
    """
    Parse a SQL string into a structured semantic dict.

    Parameters
    ----------
    raw : raw SQL text (may be None / empty)

    Returns
    -------
    dict with keys: operation, table, fields, where_fields,
                    join_tables, bind_params, raw_sql
    OR None if the text is not recognisable SQL.
    """
    if not raw:
        return None

    sql = _normalise(raw)
    m = _SQL_OP_RE.match(sql)
    if not m:
        return None

    operation = m.group(1).lower()

    try:
        result = {
            "operation":    operation,
            "table":        "",
            "fields":       [],
            "where_fields": [],
            "join_tables":  [],
            "bind_params":  _extract_bind_params(sql),
            "raw_sql":      raw.strip(),
        }

        if operation == "select":
            _parse_select(sql, result)
        elif operation == "insert":
            _parse_insert(sql, result)
        elif operation == "update":
            _parse_update(sql, result)
        elif operation == "delete":
            _parse_delete(sql, result)
        elif operation in ("merge", "replace"):
            _parse_merge(sql, result)

        result["where_fields"] = _extract_where_fields(sql)
        result["join_tables"]  = _extract_join_tables(sql)

        # De-duplicate while preserving order
        result["fields"]       = _dedup(result["fields"])
        result["where_fields"] = _dedup(result["where_fields"])
        result["join_tables"]  = _dedup(result["join_tables"])
        result["bind_params"]  = _dedup(result["bind_params"])

        return result

    except Exception:
        # Never crash the parent parser — return a minimal result
        return {
            "operation":    operation,
            "table":        "",
            "fields":       [],
            "where_fields": [],
            "join_tables":  [],
            "bind_params":  _extract_bind_params(sql),
            "raw_sql":      raw.strip(),
        }


# ─── Per-operation parsers ────────────────────────────────────────────────────

def _parse_select(sql: str, result: dict) -> None:
    # SELECT <fields> FROM <table> …
    m = re.search(r"\bSELECT\s+(.*?)\s+FROM\s+", sql, re.IGNORECASE | re.DOTALL)
    if m:
        result["fields"] = _split_fields(m.group(1))

    m = re.search(r"\bFROM\s+([`\"\w]+)", sql, re.IGNORECASE)
    if m:
        result["table"] = _clean_identifier(m.group(1))


def _parse_insert(sql: str, result: dict) -> None:
    # INSERT INTO <table> (<fields>) VALUES …
    m = re.search(r"\bINTO\s+([`\"\w]+)\s*\(([^)]+)\)", sql, re.IGNORECASE)
    if m:
        result["table"]  = _clean_identifier(m.group(1))
        result["fields"] = _split_fields(m.group(2))
        return

    # INSERT INTO <table> …  (without explicit column list)
    m = re.search(r"\bINTO\s+([`\"\w]+)", sql, re.IGNORECASE)
    if m:
        result["table"] = _clean_identifier(m.group(1))


def _parse_update(sql: str, result: dict) -> None:
    # UPDATE <table> SET col=val, col2=val2 …
    m = re.search(r"\bUPDATE\s+([`\"\w]+)", sql, re.IGNORECASE)
    if m:
        result["table"] = _clean_identifier(m.group(1))

    m = re.search(r"\bSET\s+(.*?)(?:\s+WHERE|\s+ORDER|\s+LIMIT|$)", sql, re.IGNORECASE | re.DOTALL)
    if m:
        set_clause = m.group(1)
        # Extract column names from "col = :val" pairs
        result["fields"] = [
            _clean_identifier(p.group(1))
            for p in re.finditer(r"([`\"\w]+)\s*=\s*", set_clause)
            if not p.group(1).upper().startswith(("AND", "OR"))
        ]


def _parse_delete(sql: str, result: dict) -> None:
    # DELETE FROM <table> …
    m = re.search(r"\bFROM\s+([`\"\w]+)", sql, re.IGNORECASE)
    if m:
        result["table"] = _clean_identifier(m.group(1))


def _parse_merge(sql: str, result: dict) -> None:
    # MERGE INTO <table> …  or  REPLACE INTO <table> …
    m = re.search(r"\bINTO\s+([`\"\w]+)", sql, re.IGNORECASE)
    if m:
        result["table"] = _clean_identifier(m.group(1))


# ─── Clause extractors ────────────────────────────────────────────────────────

def _extract_where_fields(sql: str) -> list[str]:
    """
    Extract column names from the WHERE clause.
    Handles: col = :param, col IS NULL, col IN (...), col > :p
    """
    m = re.search(r"\bWHERE\s+(.*?)(?:\s+(?:ORDER|GROUP|LIMIT|HAVING|UNION)|$)",
                  sql, re.IGNORECASE | re.DOTALL)
    if not m:
        return []
    where = m.group(1)
    # Grab identifiers that appear before comparison operators
    fields = [
        _clean_identifier(f.group(1))
        for f in re.finditer(
            r"([`\"\w]+)\s*(?:=|!=|<>|<|>|<=|>=|\bIS\b|\bLIKE\b|\bIN\b|\bBETWEEN\b)",
            where, re.IGNORECASE
        )
        if f.group(1).upper() not in ("AND", "OR", "NOT", "NULL", "TRUE", "FALSE")
    ]
    return fields


def _extract_join_tables(sql: str) -> list[str]:
    """Extract tables from JOIN clauses."""
    return [
        _clean_identifier(m.group(1))
        for m in re.finditer(
            r"\bJOIN\s+([`\"\w]+)", sql, re.IGNORECASE
        )
    ]


def _extract_bind_params(sql: str) -> list[str]:
    """Extract :paramName tokens."""
    return [m.group(1) for m in _BIND_PARAM_RE.finditer(sql)]


# ─── Utilities ────────────────────────────────────────────────────────────────

def _normalise(sql: str) -> str:
    """Collapse whitespace and strip leading/trailing spaces."""
    return re.sub(r"\s+", " ", sql.strip())


def _split_fields(raw: str) -> list[str]:
    """
    Split a comma-separated field list, stripping aliases and table prefixes.
    e.g. "t.first_name AS fn, last_name" → ["first_name", "last_name"]
    """
    fields = []
    for part in raw.split(","):
        part = part.strip()
        # Remove alias: "col AS alias" → "col"
        part = re.sub(r"\s+AS\s+\w+$", "", part, flags=re.IGNORECASE).strip()
        # Remove table prefix: "tbl.col" → "col"
        if "." in part:
            part = part.split(".")[-1]
        part = _clean_identifier(part)
        if part and part.upper() not in ("*", "NULL"):
            fields.append(part)
    return fields


def _clean_identifier(s: str) -> str:
    """Strip quotes/backticks from a SQL identifier."""
    return s.strip().strip("`\"'")


def _dedup(lst: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in lst:
        low = item.lower()
        if low not in seen:
            seen.add(low)
            result.append(item)
    return result
