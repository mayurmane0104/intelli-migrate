"""
parsers/dataweave_parser.py  –  Extract DataWeave scripts (inline + external).

Detection covers three distinct forms:
  1. Full %dw scripts inside <ee:transform> / <set-payload> / <set-variable>
  2. Inline #[output ... --- {...}] in salesforce:parameters, db:input-parameters,
     batch step attributes, or any text node
  3. Short #[{...}] parameter-binding maps (no %dw header, no output directive)

All three now produce DataWeaveScript entries in the output.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path, PurePosixPath
from zipfile import ZipFile, is_zipfile

from mule_parser.core.file_registry import FileRegistryResolver, normalize_path
from mule_parser.core.xml_engine import MuleXMLDocument
from mule_parser.models.schemas import DataWeaveScript

from . import dw_lexutils as _lex

logger = logging.getLogger(__name__)

# ─── Detection patterns ───────────────────────────────────────────────────────

# Full %dw header — classic transform block
_DW_HEADER_RE   = re.compile(r"%dw\s+[\d.]+", re.IGNORECASE)

# Short-form inline expression wrapper: #[  ...content...  ]
# We capture everything inside the brackets (lazy, handles nesting via depth)
_INLINE_OPEN_RE = re.compile(r"#\[")

# DataWeave fingerprints inside an inline expression (any one is sufficient)
_DW_FINGERPRINTS = [
    re.compile(r"\boutput\s+\w+/\w+", re.IGNORECASE),   # output application/java
    re.compile(r"\bpayload\.[A-Z]", re.IGNORECASE),       # payload.Field
    re.compile(r"---\s*\{"),                               # --- {
    re.compile(r"\bvars\.\w+", re.IGNORECASE),
    re.compile(r"\battributes\.\w+", re.IGNORECASE),
    re.compile(r"\breadUrl\s*\(", re.IGNORECASE),        # readUrl(...)
    re.compile(r"\bread\s*\(\s*['\"]classpath://", re.IGNORECASE),  # read('classpath://...')
    re.compile(r'"[a-zA-Z_]\w*"\s*:'),                    # "key": value
    re.compile(r"'\w+'\s*:"),                              # 'key': value
]

# Parameter-binding maps: {'key': payload.Field}
_PARAM_MAP_RE = re.compile(r"^\s*\{.+:.+\}\s*$", re.DOTALL)

_OUTPUT_RE    = re.compile(r"output\s+([\w/+\-]+)", re.IGNORECASE)
_INPUT_RE     = re.compile(r"input\s+\$?\w+\s+([\w/+\-]+)", re.IGNORECASE)
_MAPPING_RE   = re.compile(r"""(?:"([^"]+)"|'([^']+)'|([a-zA-Z_]\w*))\s*:\s*(.+)""")
_DW_RESOURCE_RE = re.compile(r"resource\s*=\s*\"([^\"]+\.dwl)\"", re.IGNORECASE)
_DW_IMPORT_EXTRACT_RE = re.compile(r"^\s*import\s+([^\n]+)$", re.IGNORECASE | re.MULTILINE)
_DW_VAR_DECL_RE = re.compile(r"^\s*var\s+([A-Za-z_]\w*)\b", re.MULTILINE)
_DW_FUN_RE = re.compile(r"\bfun\s+([A-Za-z_]\w*)\s*\(")
_DW_TOP_KEY_RE = re.compile(r'^\s*\{?\s*(?:"([^"]+)"|\'([^\']+)\'|([A-Za-z_]\w*))\s*:', re.MULTILINE)
_DW_REF_RE = re.compile(r"\b(payload|vars|attributes)(?:\.[A-Za-z_][\w$]*)*")
_DW_CONDITION_RE = re.compile(r"\bif\b|\bwhen\b|\bmatch\b", re.IGNORECASE)
_DW_ITERATION_RE = re.compile(r"\bmap\b|\bflatMap\b|\bfilter\b|\breduce\b", re.IGNORECASE)
_DW_CALL_RE = re.compile(r"\b([A-Za-z_]\w*)\s*\(")
_DW_BUILTINS = {"if", "when", "match", "map", "flatMap", "filter", "reduce", "fun", "var", "output", "input", "import"}

# Elements whose TEXT content is a DataWeave expression
_DW_TEXT_CONTEXTS = {
    "salesforce:parameters",
    "salesforce-parameters",
    "db:input-parameters",
    "db-input-parameters",
    "input-parameters",
    "ee:set-payload",
    "ee:set-variable",
    "ee:message",
    "ee:variables",
}

# Elements whose ATTRIBUTE values may contain %dw
_TRANSFORM_LOCAL_NAMES = {"transform", "transform-message", "set-payload", "set-variable"}


# ─── Public API ───────────────────────────────────────────────────────────────

def parse_inline_dataweave(doc: MuleXMLDocument, flow_name: str = "") -> list[DataWeaveScript]:
    scripts: list[DataWeaveScript] = []
    seen: set[tuple[int | None, str]] = set()

    for elem in doc.root.iter():
        if not isinstance(elem.tag, str):
            continue
        for script in extract_dataweave_from_element(doc, elem, flow_name=flow_name):
            seen_key = (script.line, script.script_text[:120])
            if seen_key in seen:
                continue
            seen.add(seen_key)
            scripts.append(script)

    return scripts


def parse_external_dwl(dwl_path: Path) -> DataWeaveScript:
    try:
        text = dwl_path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        logger.error("Cannot read DWL file %s: %s", dwl_path, exc)
        text = ""

    return _build_script(
        script_id  = dwl_path.stem,
        text       = text,
        source     = "external",
        context    = "external-dwl",
        purpose    = _infer_purpose(text, "external"),
        file       = str(dwl_path),
        line       = 1,
        flow_name  = "",
    )


def extract_dataweave_from_element(
    doc: MuleXMLDocument,
    elem,
    flow_name: str = "",
    parent_step_id: str = "",
    input_format: str = "",
) -> list[DataWeaveScript]:
    """
    Extract all DataWeave scripts from a single XML element.

    Handles three source forms:
      A) <ee:transform> child text with %dw header
      B) Text node of known DW-container elements (#[output...] or #[{...}])
      C) Attribute values containing a %dw header (fallback)
    """
    scripts: list[DataWeaveScript] = []
    tag     = doc.tag_name(elem)
    local   = tag.split(":")[-1].lower() if ":" in tag else tag.lower()
    full_tag_lower = tag.lower()

    # ── A: Full %dw transform inside <ee:transform> ──────────────────────────
    if local in ("transform", "transform-message"):
        for child in elem.iter():
            if not isinstance(child.tag, str):
                continue
            text = (child.text or "").strip()
            if text and _DW_HEADER_RE.search(text):
                scripts.append(_build_script(
                    script_id      = _script_label(doc, child),
                    text           = text,
                    source         = "inline",
                    context        = tag,
                    purpose        = "transformation",
                    file           = str(doc.path),
                    line           = doc.line_number(child),
                    flow_name      = flow_name or _nearest_flow_name(doc, child),
                    parent_step_id = parent_step_id,
                    input_format   = input_format,
                ))
        return scripts

    # ── B: Text node of known DW-container elements ──────────────────────────
    is_dw_text_context = full_tag_lower in _DW_TEXT_CONTEXTS or local in {
        t.split(":")[-1] for t in _DW_TEXT_CONTEXTS
    }
    if is_dw_text_context:
        raw_text = (elem.text or "").strip()
        if raw_text:
            inner = _unwrap_inline(raw_text)          # strip outer #[ ]
            if inner is not None and _is_dw_content(inner):
                scripts.append(_build_script(
                    script_id      = _script_label(doc, elem),
                    text           = inner,
                    source         = "inline-expression",
                    context        = tag,
                    purpose        = _infer_purpose(inner, local),
                    file           = str(doc.path),
                    line           = doc.line_number(elem),
                    flow_name      = flow_name or _nearest_flow_name(doc, elem),
                    parent_step_id = parent_step_id,
                    input_format   = input_format,
                ))
            elif raw_text and _DW_HEADER_RE.search(raw_text):
                # text without #[ ] wrapper but with %dw header
                scripts.append(_build_script(
                    script_id      = _script_label(doc, elem),
                    text           = raw_text,
                    source         = "inline",
                    context        = tag,
                    purpose        = "transformation",
                    file           = str(doc.path),
                    line           = doc.line_number(elem),
                    flow_name      = flow_name or _nearest_flow_name(doc, elem),
                    parent_step_id = parent_step_id,
                    input_format   = input_format,
                ))
            elif raw_text and _is_dw_content(raw_text):
                # raw DW expression without wrapper or header, such as readUrl(...) in set-variable
                scripts.append(_build_script(
                    script_id      = _script_label(doc, elem),
                    text           = raw_text,
                    source         = "inline-expression",
                    context        = tag,
                    purpose        = _infer_purpose(raw_text, local),
                    file           = str(doc.path),
                    line           = doc.line_number(elem),
                    flow_name      = flow_name or _nearest_flow_name(doc, elem),
                    parent_step_id = parent_step_id,
                    input_format   = input_format,
                ))

    # ── Also scan text of ANY element that contains a %dw script ─────────────
    if not is_dw_text_context:
        raw_text = (elem.text or "").strip()
        if raw_text:
            inner = _unwrap_inline(raw_text)
            if inner is not None and _DW_HEADER_RE.search(inner):
                scripts.append(_build_script(
                    script_id      = _script_label(doc, elem),
                    text           = inner,
                    source         = "inline-expression",
                    context        = tag,
                    purpose        = _infer_purpose(inner, local),
                    file           = str(doc.path),
                    line           = doc.line_number(elem),
                    flow_name      = flow_name or _nearest_flow_name(doc, elem),
                    parent_step_id = parent_step_id,
                    input_format   = input_format,
                ))
    raw_text = (elem.text or "").strip()
    if raw_text:
        inner = _unwrap_inline(raw_text)
        if inner is not None and _DW_HEADER_RE.search(inner):
            scripts.append(_build_script(
                script_id      = _script_label(doc, elem),
                text           = inner,
                source         = "inline-expression",
                context        = tag,
                purpose        = _infer_purpose(inner, local),
                file           = str(doc.path),
                line           = doc.line_number(elem),
                flow_name      = flow_name or _nearest_flow_name(doc, elem),
                parent_step_id = parent_step_id,
                input_format   = input_format,
            ))

    # ── C: Attribute values containing %dw or inline #[...] expressions ─────
    attrs = doc.attrs(elem)
    for attr_name, attr_val in attrs.items():
        if not attr_val:
            continue

        # Case 1: attribute contains a full %dw header (classic inline DW in attr)
        if _DW_HEADER_RE.search(attr_val):
            scripts.append(_build_script(
                script_id      = _script_label(doc, elem),
                text           = attr_val,
                source         = "inline",
                context        = tag,
                purpose        = "transformation",
                file           = str(doc.path),
                line           = doc.line_number(elem),
                flow_name      = flow_name or _nearest_flow_name(doc, elem),
                parent_step_id = parent_step_id,
                input_format   = input_format,
            ))

        # Case 2: attribute holds a short inline expression wrapped in #[...]
        inner = _unwrap_inline(attr_val)
        if inner is not None and _is_dw_content(inner):
            scripts.append(_build_script(
                script_id      = f"{_script_label(doc, elem)}:{attr_name}",
                text           = inner,
                source         = "inline-expression",
                context        = f"{tag}.@{attr_name}",
                purpose        = _infer_purpose(inner, local),
                file           = str(doc.path),
                line           = doc.line_number(elem),
                flow_name      = flow_name or _nearest_flow_name(doc, elem),
                parent_step_id = parent_step_id,
                input_format   = input_format,
            ))
        elif attr_val and _is_dw_content(attr_val):
            scripts.append(_build_script(
                script_id      = f"{_script_label(doc, elem)}:{attr_name}",
                text           = attr_val,
                source         = "inline-expression",
                context        = f"{tag}.@{attr_name}",
                purpose        = _infer_purpose(attr_val, local),
                file           = str(doc.path),
                line           = doc.line_number(elem),
                flow_name      = flow_name or _nearest_flow_name(doc, elem),
                parent_step_id = parent_step_id,
                input_format   = input_format,
            ))

    return scripts


def extract_external_dataweave_refs(
    doc: MuleXMLDocument,
    elem,
    flow_name: str,
    parent_step_id: str,
    processor_index: int,
    *,
    resolution_cache: dict[str, tuple[str, list[str], str]] | None = None,
    file_resolver: FileRegistryResolver | None = None,
) -> list[DataWeaveScript]:
    attrs = doc.attrs(elem)
    resource = attrs.get("resource", "")
    if not resource or not resource.lower().endswith(".dwl"):
        return []
    script = _build_external_ref_script(
        doc=doc,
        elem=elem,
        flow_name=flow_name,
        parent_step_id=parent_step_id,
        processor_index=processor_index,
        resource=resource,
        resolution_cache=resolution_cache,
        file_resolver=file_resolver,
    )
    return [script]


def _build_external_ref_script(
    *,
    doc: MuleXMLDocument,
    elem,
    flow_name: str,
    parent_step_id: str,
    processor_index: int,
    resource: str,
    resolution_cache: dict[str, tuple[str, list[str], str]] | None,
    file_resolver: FileRegistryResolver | None,
) -> DataWeaveScript:
    resource_norm = _normalize_resource_path(resource)
    cache_key = f"{doc.path}|{resource_norm}"
    cached = resolution_cache.get(cache_key) if resolution_cache is not None else None
    if cached:
        source_text, attempts, error = cached
        resolved_path = resource_norm
    else:
        source_text, resolved_path, attempts, error = _resolve_dwl_resource(doc.path, resource_norm, file_resolver=file_resolver)
        if resolution_cache is not None:
            resolution_cache[cache_key] = (source_text, attempts, error)

    script = _build_script(
        script_id=f"{_slug(flow_name or doc.path.stem)}-{_slug(resource_norm)}",
        text=source_text,
        source="external-resource",
        context=doc.tag_name(elem),
        purpose="transformation",
        file=resolved_path or resource_norm,
        line=doc.line_number(elem),
        flow_name=flow_name,
        parent_step_id=parent_step_id,
    )
    script.parent_xml_file = str(doc.path)
    script.transform_step = parent_step_id
    script.processor_index = processor_index
    script.resource_path = resource_norm
    script.resolution_attempts = attempts
    script.extraction_error = error
    script.metadata = _extract_dw_metadata(source_text)
    return script


# ─── Inline expression helpers ────────────────────────────────────────────────

def _unwrap_inline(text: str) -> str | None:
    """
    If text is wrapped in #[...], return the inner content.
    Handles nested brackets correctly via depth counting.
    Returns None if not a #[...] expression.
    """
    text = text.strip()
    if not text.startswith("#["):
        return None
    depth = 0
    start = -1
    for i, ch in enumerate(text):
        if ch == "[":
            depth += 1
            if depth == 1:
                start = i + 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return text[start:i].strip()
    return None  # unclosed bracket


def _is_dw_content(inner: str) -> bool:
    """Return True if the extracted inner text looks like DataWeave."""
    return any(pattern.search(inner) for pattern in _DW_FINGERPRINTS)


def _infer_purpose(text: str, context_local: str) -> str:
    """Classify the DataWeave script's functional purpose."""
    ctx = context_local.lower()
    if "parameter" in ctx or "input-param" in ctx:
        return "parameter-binding"
    if "transform" in ctx or "message" in ctx:
        return "transformation"
    if "filter" in ctx or "when" in ctx:
        return "filter"
    if _PARAM_MAP_RE.match(text) and "---" not in text:
        return "parameter-binding"
    if "---" in text and "output" in text.lower():
        return "mapping"
    return "transformation"


# ─── Script builder ───────────────────────────────────────────────────────────

def _build_script(
    script_id: str,
    text: str,
    source: str,
    context: str,
    purpose: str,
    file: str,
    line: int | None,
    flow_name: str,
    parent_step_id: str = "",
    input_format: str = "",
) -> DataWeaveScript:
    output_type  = ""
    input_types: list[str] = []

    m = _OUTPUT_RE.search(text)
    if m:
        output_type = m.group(1).strip()

    for m in _INPUT_RE.finditer(text):
        input_types.append(m.group(1).strip())

    return DataWeaveScript(
        script_id      = script_id,
        source         = source,
        context        = context,
        purpose        = purpose,
        file           = file,
        line           = line,
        script_text    = text,
        input_source   = _detect_input_source(text),
        input_format   = input_format or (input_types[0] if input_types else ""),
        input_types    = input_types,
        output_type    = output_type,
        field_mappings = _extract_field_mappings(text),
        parent_flow    = flow_name,
        parent_step_id = parent_step_id,
        metadata       = _extract_dw_metadata(text),
    )


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _nearest_flow_name(doc: MuleXMLDocument, elem) -> str:
    for ancestor in elem.iterancestors():
        tag = doc.tag_name(ancestor)
        local = tag.split(":")[-1].lower() if ":" in tag else tag.lower()
        if local in ("flow", "sub-flow", "subflow"):
            return doc.attrs(ancestor).get("name", "")
    return ""


def _script_label(doc: MuleXMLDocument, elem) -> str:
    tag   = doc.tag_name(elem)
    local = tag.split(":")[-1] if ":" in tag else tag
    # Walk up to find a named ancestor (transform / batch-step / flow)
    for ancestor in elem.iterancestors():
        attrs = doc.attrs(ancestor)
        label = attrs.get("doc:name") or attrs.get("name")
        if label:
            return _slug(f"{label}_{local}")
    return _slug(local) or f"{doc.path.stem}_dw"


def _slug(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.strip().lower())
    return slug.strip("-") or "dw"


def _detect_input_source(text: str) -> str:
    if re.search(r"\bvars\.", text):
        return "vars"
    if re.search(r"\battributes\.", text):
        return "attributes"
    if re.search(r"\bpayload\b|\$\.", text):
        return "payload"
    return ""


def _extract_field_mappings(text: str) -> dict[str, str]:
    """Extract source-field -> target-field mappings from a DataWeave body.

    Two passes:
      1. Bracket-aware: locate the actual outermost record literal that is
         returned (handles nested `default {...}`, multi-arg calls, etc.
         without corrupting them) and resolve each entry's source. If the
         literal sits directly inside a `map (x) -> {...}` / `filter`/
         `flatMap` lambda, `x.Field` is recognised as a real source field
         (previously only `payload.`/`vars.`/`attributes.`/`$.` prefixed
         expressions were recognised, which silently dropped almost every
         mapping in scripts using the extremely common `collection map
         (item) -> {...}` idiom).
      2. Fallback: the original comma/newline heuristic, kept only as a
         last resort for shapes the bracket scan can't find (e.g. no `{`
         at all in the body).
    """
    body = text.split("---", 1)[1] if "---" in text else text
    mappings: dict[str, str] = {}

    obj_span = None
    spans = _lex.find_all_top_level_braces(body)
    if spans:
        obj_span = spans[-1]

    if obj_span is not None:
        start, end = obj_span
        lambda_param = _lex.find_enclosing_lambda_param(body[:start])
        inner = body[start + 1:end]
        for entry in _lex.split_top_level(inner, ","):
            m = _MAPPING_RE.match(entry.strip())
            if not m:
                continue
            target_field = (m.group(1) or m.group(2) or m.group(3) or "").strip()
            expression = re.sub(r"\s*//.*$", "", (m.group(4) or "")).strip()
            if not target_field or not expression:
                continue
            input_field = _normalize_input_field(expression, lambda_param=lambda_param)
            if input_field and target_field:
                mappings[input_field] = target_field

    if mappings:
        return mappings

    # ── Fallback: legacy line-based heuristic (no brace literal found) ──
    flat = re.sub(r",\s*(?=\"|'|[a-zA-Z_])", "\n", body)
    for raw_line in flat.splitlines():
        line = raw_line.strip().rstrip(",").strip()
        if not line or line in ("{", "}", "{}"):
            continue
        m = _MAPPING_RE.match(line)
        if not m:
            continue
        target_field = (m.group(1) or m.group(2) or m.group(3) or "").strip()
        expression   = re.sub(r"\s*//.*$", "", (m.group(4) or "")).strip().rstrip(", {}")
        if not target_field or not expression:
            continue
        input_field = _normalize_input_field(expression)
        if input_field and target_field:
            mappings[input_field] = target_field

    return mappings


def _normalize_input_field(expression: str, lambda_param: str | None = None) -> str:
    expr = expression.strip()
    for prefix in ("payload.", "vars.", "attributes."):
        if expr.startswith(prefix):
            return expr[len(prefix):]
    if lambda_param and expr.startswith(f"{lambda_param}."):
        return expr[len(lambda_param) + 1:]
    if expr.startswith("$."):
        return expr[2:]
    if expr == "payload":
        return "payload"
    if lambda_param and expr == lambda_param:
        return lambda_param
    m = re.match(r"^(\w+)$", expr)
    if m:
        return m.group(1)
    return ""


def _extract_dw_metadata(text: str) -> dict[str, object]:
    out_match = _OUTPUT_RE.search(text)
    refs = sorted(set(m.group(0) for m in _DW_REF_RE.finditer(text)))
    function_calls = sorted(
        {
            name for name in _DW_CALL_RE.findall(text)
            if name not in _DW_BUILTINS and not name.startswith("$")
        }
    )
    reads = sorted({ref for ref in refs if ref.startswith("vars.") or ref.startswith("payload.") or ref.startswith("attributes.")})

    # Top-level keys: only the keys of the record literal actually returned
    # by the final body expression (after the last `---`), not keys
    # belonging to intermediate `var`/`fun` declarations elsewhere in the
    # script. Falls back to whole-text scanning only if the body itself has
    # no object literal to inspect (e.g. a bare scalar/selector body).
    body = text.split("---", 1)[1] if "---" in text else text
    top_level_keys: set[str] = set()
    spans = _lex.find_all_top_level_braces(body)
    if spans:
        start, end = spans[-1]
        for entry in _lex.split_top_level(body[start + 1:end], ","):
            m = _MAPPING_RE.match(entry.strip())
            if m:
                key = (m.group(1) or m.group(2) or m.group(3) or "").strip()
                if key:
                    top_level_keys.add(key)
    if not top_level_keys:
        top_level_keys = set(k for g in _DW_TOP_KEY_RE.findall(text) for k in g if k)

    # Drop any keys explicitly excluded via DataWeave's `map $ -"field"` /
    # `- "field"` projection-removal idiom anywhere in the script — those
    # never reach the actual output even though they're declared upstream.
    excluded = set(re.findall(r'-\s*"([^"]+)"', text)) | set(re.findall(r"-\s*'([^']+)'", text))
    top_level_keys -= excluded

    return {
        "imports": [m.strip() for m in _DW_IMPORT_EXTRACT_RE.findall(text)],
        "vars": sorted(set(_DW_VAR_DECL_RE.findall(text))),
        "functions": sorted(set(_DW_FUN_RE.findall(text))),
        "output": (out_match.group(1).strip() if out_match else ""),
        "top_level_keys": sorted(top_level_keys),
        "references": refs,
        "reads": reads,
        "has_conditions": bool(_DW_CONDITION_RE.search(text)),
        "has_iteration": bool(_DW_ITERATION_RE.search(text)),
        "function_calls": function_calls,
    }


def _normalize_resource_path(resource: str) -> str:
    return str(PurePosixPath(normalize_path(resource)))


def _resolve_dwl_resource(
    xml_path: Path,
    resource: str,
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> tuple[str, str, list[str], str]:
    attempts: list[str] = []
    errors: list[str] = []
    if file_resolver is not None:
        text, rec, at, err = file_resolver.read_text(resource, relative_to=str(xml_path))
        attempts.extend(at)
        if rec is not None:
            return text, rec.normalized_path, attempts, ""
        if err:
            errors.append(err)

    abs_candidate = Path(resource)
    attempts.append(f"absolute:{abs_candidate}")
    if abs_candidate.is_file():
        try:
            return abs_candidate.read_text(encoding="utf-8", errors="replace"), str(abs_candidate), attempts, ""
        except Exception as exc:
            errors.append(f"absolute read failed: {exc}")

    project_root = _find_project_root_from_xml(xml_path)
    rel_candidates = [
        project_root / resource,
        project_root / "src" / "main" / "resources" / resource,
        project_root / "src" / "main" / "mule" / resource,
        xml_path.parent / resource,
    ]
    norm_res = resource.replace("\\", "/")
    is_win_abs = bool(re.match(r"^[a-zA-Z]:/", norm_res))
    if abs_candidate.is_absolute() or is_win_abs:
        try:
            if is_win_abs:
                parts = [p for p in norm_res.split("/")[1:] if p]
                tail = Path(*parts)
            else:
                tail = abs_candidate.relative_to(abs_candidate.anchor)
        except Exception:
            tail = abs_candidate
        for depth in range(1, len(tail.parts) + 1):
            rel_tail = Path(*tail.parts[-depth:])
            rel_candidates.extend([
                project_root / rel_tail,
                project_root / "src" / "main" / "resources" / rel_tail,
                project_root / "src" / "main" / "mule" / rel_tail,
                xml_path.parent / rel_tail,
            ])

    seen = set()
    for rel in rel_candidates:
        if rel in seen:
            continue
        seen.add(rel)
        attempts.append(f"relative:{rel}")
        if rel.is_file():
            try:
                return rel.read_text(encoding="utf-8", errors="replace"), str(rel), attempts, ""
            except Exception as exc:
                errors.append(f"relative read failed ({rel}): {exc}")

    attempts.append("jar-classpath-scan")
    for jar in _discover_possible_jars(project_root):
        try:
            with ZipFile(jar, "r") as zf:
                for entry in _candidate_zip_entries(resource):
                    if entry in zf.namelist():
                        return zf.read(entry).decode("utf-8", errors="replace"), f"{jar}!/{entry}", attempts, ""
        except Exception as exc:
            errors.append(f"jar classpath lookup failed ({jar}): {exc}")

    attempts.append("jar-zip-entry-fuzzy")
    for jar in _discover_possible_jars(project_root):
        try:
            with ZipFile(jar, "r") as zf:
                target = resource.lower()
                for name in zf.namelist():
                    norm = name.replace("\\", "/").lower()
                    if norm.endswith(target) or norm.endswith("/" + target):
                        return zf.read(name).decode("utf-8", errors="replace"), f"{jar}!/{name}", attempts, ""
        except Exception as exc:
            errors.append(f"jar zip lookup failed ({jar}): {exc}")

    return "", resource, attempts, "; ".join(errors) if errors else "DWL not found"


def resolve_external_dwl_resource(
    xml_path: Path,
    resource: str,
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> tuple[str, str, list[str], str]:
    """Public wrapper used by other parsers (error handlers, etc.)."""
    return _resolve_dwl_resource(xml_path, _normalize_resource_path(resource), file_resolver=file_resolver)


def _find_project_root_from_xml(xml_path: Path) -> Path:
    parts = [p.lower() for p in xml_path.parts]
    for marker in ("src", "main", "mule"):
        if marker not in parts:
            break
    if "src" in parts:
        idx = parts.index("src")
        return Path(*xml_path.parts[:idx])
    return xml_path.parent


def _discover_possible_jars(project_root: Path) -> list[Path]:
    jars: list[Path] = []
    for path in project_root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".jar", ".zip"} and is_zipfile(path):
            jars.append(path)
    return jars


def _candidate_zip_entries(resource: str) -> list[str]:
    res = resource.lstrip("/").replace("\\", "/")
    return [
        res,
        f"src/main/resources/{res}",
        f"META-INF/mule-src/{res}",
    ]


