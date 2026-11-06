from __future__ import annotations

import re
from collections import defaultdict
from typing import Any


_OUT_RE = re.compile(r"^\s*output\s+([^\s]+)", re.IGNORECASE | re.MULTILINE)
_PATH_TOKEN_RE = re.compile(
    r"\b(payload|vars|attributes|flowVars|sessionVars)\.([A-Za-z_][\w$]*(?:\.[A-Za-z_][\w$]*)*)"
)
_QPARAM_RE = re.compile(r"\battributes\.queryParams\.([A-Za-z_][\w$]*)")
_UPARAM_RE = re.compile(r"\battributes\.uriParams\.([A-Za-z_][\w$]*)")
_HEADER_RE = re.compile(r"\battributes\.headers\.([A-Za-z_][\w$-]*)")
_ERR_RE = re.compile(r"(?:error|type)\s*[:=]\s*([A-Z]+:[A-Z_]+)")
_PROP_RE = re.compile(r"\$\{([^}]+)\}")
_ENTITY_RE = re.compile(r"\b(customer|account|transaction|payment(?:order)?|invoice|order|contact)\b", re.I)
_DWL_RESOURCE_RE = re.compile(r"resource\s*=\s*\"([^\"]+\.dwl)\"", re.IGNORECASE)


def enrich_dataweave_dependencies(raw: dict) -> None:
    for dw in raw.get("dataweave", []):
        text = dw.get("script_text") or ""
        deps: list[str] = []
        for base, path in _PATH_TOKEN_RE.findall(text):
            deps.append(f"{base}.{path}")
        for name in _QPARAM_RE.findall(text):
            deps.append(f"attributes.queryParams.{name}")
        for name in _UPARAM_RE.findall(text):
            deps.append(f"attributes.uriParams.{name}")
        for name in _HEADER_RE.findall(text):
            deps.append(f"attributes.headers.{name}")
        dw["input_types"] = sorted(set(deps))

        m = _OUT_RE.search(text)
        if m:
            dw["output_type"] = m.group(1).strip()


def resolve_dwl_parent_links(raw: dict) -> None:
    """
    Fill dataweave.parent_flow/parent_step_id by matching external DWL resource names
    referenced by ee:transform step raw_xml blocks.
    """
    by_resource_name: dict[str, list[dict]] = defaultdict(list)
    for dw in raw.get("dataweave", []):
        f = (dw.get("file") or "").replace("\\", "/")
        res_name = f.split("/")[-1]
        if res_name:
            by_resource_name[res_name].append(dw)

    for plan in raw.get("flow_execution_plans", []):
        flow_name = plan.get("flow_name", "")
        for step in plan.get("steps", []):
            raw_xml = step.get("raw_xml", "") or ""
            if "ee:transform" not in (step.get("type", "") or "").lower() and "ee:transform" not in raw_xml.lower():
                continue
            matches = _DWL_RESOURCE_RE.findall(raw_xml)
            for m in matches:
                res_name = m.replace("\\", "/").split("/")[-1]
                for dw in by_resource_name.get(res_name, []):
                    if not dw.get("parent_flow"):
                        dw["parent_flow"] = flow_name
                    if not dw.get("parent_step_id"):
                        dw["parent_step_id"] = step.get("step_id", "")


def infer_flow_schemas(raw: dict, flow_name: str) -> tuple[dict[str, Any], dict[str, Any], str, str]:
    in_tree: dict[str, Any] = {}
    out_tree: dict[str, Any] = {}
    in_mime = ""
    out_mime = ""

    for dw in raw.get("dataweave", []):
        if dw.get("parent_flow") != flow_name:
            continue
        script = dw.get("script_text") or ""
        out_mime = out_mime or (dw.get("output_type") or _extract_output_mime(script))
        for dep in dw.get("input_types", []):
            if dep.startswith("payload."):
                _insert_tree(in_tree, dep.split(".", 1)[1])
        targets = _extract_lhs_fields(script)
        fm = dw.get("field_mappings", {}) or {}
        for k, v in fm.items():
            if isinstance(v, str) and re.match(r"[A-Za-z_][\w.]*$", v):
                targets.append(v)
            if isinstance(k, str) and re.match(r"[A-Za-z_][\w.]*$", k):
                targets.append(k)
        for target in targets:
            _insert_tree(out_tree, target)

    for plan in raw.get("flow_execution_plans", []):
        if plan.get("flow_name") != flow_name:
            continue
        for step in plan.get("steps", []):
            st = (step.get("type") or "").lower()
            attrs = step.get("attributes", {}) or {}
            if "http:listener" in st:
                in_mime = in_mime or attrs.get("outputMimeType", "application/json")
            for p in step.get("payload_reads", []) or []:
                if isinstance(p, str) and p.startswith("payload."):
                    _insert_tree(in_tree, p.split(".", 1)[1])
            for v in step.get("variable_reads", []) or []:
                if isinstance(v, str):
                    _insert_tree(in_tree, f"vars.{v}")
            for p in step.get("payload_writes", []) or []:
                if isinstance(p, str) and p.startswith("payload."):
                    _insert_tree(out_tree, p.split(".", 1)[1])
            if "set-payload" in st:
                expr = attrs.get("value", "")
                for base, path in _PATH_TOKEN_RE.findall(expr):
                    if base == "payload":
                        _insert_tree(out_tree, path)

    in_mime = in_mime or ("application/json" if in_tree else "")
    out_mime = out_mime or ("application/json" if out_tree else "")
    return in_tree, out_tree, in_mime, out_mime


def compute_idempotency(flow_name: str, plan: dict) -> tuple[bool, str]:
    steps = plan.get("steps", [])
    method = ""
    writes: list[str] = []
    for step in steps:
        st = (step.get("type") or "").lower()
        attrs = step.get("attributes", {}) or {}
        if "http:listener" in st and not method:
            method = (attrs.get("method") or "").upper()
        if any(x in st for x in ("create", "insert", "update", "delete", "publish", "write", "upsert", "objectstore:store", "jms:publish", "file:write")):
            writes.append(st)

    if method == "GET" and not writes:
        return True, "GET flow with pure transformations only"
    if method == "PUT" and not writes:
        return True, "PUT flow with no detected external mutation"
    if method == "PATCH" and not writes:
        return True, "PATCH flow appears read/transform only"
    if method == "POST":
        return False, "POST flows are non-idempotent by default"
    if writes:
        return False, f"External side effects detected: {', '.join(sorted(set(writes))[:4])}"
    return method in {"GET", "PUT"}, "Heuristic based on HTTP verb and side effects"


def classify_apikit(plan: dict) -> str | None:
    steps = plan.get("steps", [])
    has_listener = any("http:listener" in (s.get("type") or "").lower() for s in steps)
    has_router = any("apikit:router" in (s.get("type") or "").lower() for s in steps)
    if has_listener and has_router:
        return "APIKIT_DISPATCH"
    return None


_ENV_PRECEDENCE = ["default", "local", "dev", "sit", "qa", "uat", "prod"]
_ENV_RANK = {env: index for index, env in enumerate(_ENV_PRECEDENCE)}


def _collect_property_entries(raw: dict) -> list[dict[str, str | bool]]:
    entries: list[dict[str, str | bool]] = []
    props = raw.get("properties", []) or []

    if isinstance(props, list):
        for item in props:
            if isinstance(item, dict):
                key = str(item.get("key", "")).strip()
                raw_value = str(item.get("value", ""))
                source_file = str(item.get("file", ""))
                environment_scope = str(item.get("environment_scope", "default") or "default")
                is_secure = bool(item.get("is_secure", False))
            elif hasattr(item, "key"):
                key = str(getattr(item, "key", "")).strip()
                raw_value = str(getattr(item, "value", ""))
                source_file = str(getattr(item, "file", ""))
                environment_scope = str(getattr(item, "environment_scope", "default") or "default")
                is_secure = bool(getattr(item, "is_secure", False))
            else:
                continue
            if not key:
                continue
            entries.append({
                "key": key,
                "raw_value": raw_value,
                "source_file": source_file,
                "environment_scope": environment_scope,
                "is_secure": is_secure,
            })
        return entries

    if isinstance(props, dict):
        for key, value in props.items():
            if isinstance(value, dict):
                for env, env_val in value.items():
                    entries.append({
                        "key": str(key).strip(),
                        "raw_value": str(env_val),
                        "source_file": "",
                        "environment_scope": str(env) or "default",
                        "is_secure": False,
                    })
            else:
                entries.append({
                    "key": str(key).strip(),
                    "raw_value": str(value),
                    "source_file": "",
                    "environment_scope": "default",
                    "is_secure": False,
                })
    return entries


def _build_env_layers(entries: list[dict[str, str | bool]]) -> dict[str, dict[str, dict[str, str | bool]]]:
    layers: dict[str, dict[str, dict[str, str | bool]]] = defaultdict(dict)
    for entry in entries:
        env = str(entry.get("environment_scope", "default") or "default")
        layers[env][entry["key"]]= entry
    return layers


def _lookup_property_entry(key: str, env: str, layers: dict[str, dict[str, dict[str, str | bool]]]) -> dict[str, str | bool] | None:
    rank = _ENV_RANK.get(env, 0)
    for current_env in reversed(_ENV_PRECEDENCE[: rank + 1]):
        if key in layers.get(current_env, {}):
            return layers[current_env][key]
    return None


def _resolve_property_value(raw_value: str, env: str, layers: dict[str, dict[str, dict[str, str | bool]]], seen: set[str]) -> str:
    def substitute(match: re.Match) -> str:
        ref_key = match.group(1).strip()
        if ref_key in seen:
            return f"${{{ref_key}}}"
        entry = _lookup_property_entry(ref_key, env, layers)
        if not entry:
            return f"${{{ref_key}}}"
        return _resolve_property_value(str(entry["raw_value"]), str(entry["environment_scope"] or env), layers, seen | {ref_key})

    return _PROP_RE.sub(substitute, raw_value)


def resolve_properties(raw: dict) -> dict[str, dict[str, dict[str, str | bool]]]:
    entries = _collect_property_entries(raw)
    layers = _build_env_layers(entries)

    grouped: dict[str, list[dict[str, str | bool]]] = defaultdict(list)
    for entry in entries:
        grouped[entry["key"]].append(entry)

    resolved: dict[str, dict[str, str | bool]] = {}
    unresolved: dict[str, dict[str, str | bool]] = {}
    sources: dict[str, list[dict[str, str | bool]]] = {}

    for key, candidates in grouped.items():
        chosen = max(candidates, key=lambda entry: _ENV_RANK.get(str(entry.get("environment_scope", "default")), 0))
        resolved_value = _resolve_property_value(
            str(chosen["raw_value"]),
            str(chosen.get("environment_scope", "default") or "default"),
            layers,
            {key},
        )
        entry_info = {
            "resolved_value": resolved_value,
            "raw_value": str(chosen["raw_value"]),
            "source_file": str(chosen.get("source_file", "")),
            "environment_scope": str(chosen.get("environment_scope", "default") or "default"),
            "is_secure": bool(chosen.get("is_secure", False)),
        }

        if _PROP_RE.search(resolved_value):
            unresolved[key] = entry_info
        else:
            resolved[key] = entry_info

        sources[key] = [
            {
                "source_file": str(c.get("source_file", "")),
                "environment_scope": str(c.get("environment_scope", "default") or "default"),
                "raw_value": str(c.get("raw_value", "")),
                "is_secure": bool(c.get("is_secure", False)),
            }
            for c in candidates
        ]

    return {
        "resolved": resolved,
        "unresolved": unresolved,
        "sources": sources,
    }


def derive_risks(raw: dict) -> list[dict[str, Any]]:
    risks: list[dict[str, Any]] = []
    flow_names = {f.get("name", "") for f in raw.get("flows", [])}
    if not raw.get("munit_tests"):
        risks.append(_risk("HIGH", "test", "No MUnit tests detected", 0.95, list(flow_names)))
    if raw.get("property_references"):
        unresolved = [r for r in raw.get("property_references", []) if "${" in str(r)]
        if unresolved:
            risks.append(_risk("MEDIUM", "runtime", "Unresolved property placeholders detected", 0.8, []))
    for dw in raw.get("dataweave", []):
        txt = dw.get("script_text") or ""
        if len(txt.splitlines()) > 120:
            risks.append(_risk("MEDIUM", "maintainability", f"Large DWL script: {dw.get('script_id','')}", 0.85, [dw.get("parent_flow", "")]))
        if "password" in txt.lower() or "secret" in txt.lower():
            risks.append(_risk("HIGH", "security", "Potential plaintext secret in DataWeave", 0.65, [dw.get("parent_flow", "")]))
    return risks


def extract_business_entities(raw: dict) -> dict[str, list[str]]:
    by_flow: dict[str, set[str]] = defaultdict(set)
    for flow in raw.get("flows", []):
        fname = flow.get("name", "")
        for tok in _ENTITY_RE.findall(fname):
            by_flow[fname].add(_norm_entity(tok))
    for dw in raw.get("dataweave", []):
        fname = dw.get("parent_flow", "")
        text = dw.get("script_text", "")
        for tok in _ENTITY_RE.findall(text):
            by_flow[fname].add(_norm_entity(tok))
    return {k: sorted(v) for k, v in by_flow.items() if k}


def map_munit_coverage(raw: dict) -> dict[str, Any]:
    tests = raw.get("munit_tests", [])
    flows = [f.get("name", "") for f in raw.get("flows", []) if f.get("name")]
    coverage: dict[str, list[str]] = {f: [] for f in flows}
    for t in tests:
        name = t.get("name", "")
        target = t.get("target_flow") or _guess_target_flow(name, flows)
        if target:
            coverage.setdefault(target, [])
            coverage[target].append(name)
    untested = sorted([f for f, ts in coverage.items() if not ts])
    density = {t.get("name", ""): len(t.get("assertions", []) or []) for t in tests}
    return {
        "coverage_by_flow": coverage,
        "untested_flows": untested,
        "critical_flow_coverage": {f: bool(ts) for f, ts in coverage.items()},
        "assertion_density": density,
    }


def infer_error_links(raw: dict, flow_name: str) -> dict[str, list[str]]:
    error_types: set[str] = set()
    propagated: set[str] = set()
    retryable: set[str] = set()
    fallbacks: set[str] = set()
    for eh in raw.get("error_handling", []):
        if eh.get("flow_name") != flow_name:
            continue
        et = eh.get("error_type")
        if et:
            error_types.add(et)
        htype = (eh.get("type") or "").lower()
        if "propagate" in htype and et:
            propagated.add(et)
        if any("until-successful" in (p.get("type", "") or "").lower() for p in eh.get("processors", [])):
            if et:
                retryable.add(et)
        for p in eh.get("processors", []):
            if "flow-ref" in (p.get("type", "") or "").lower():
                ref = (p.get("attributes", {}) or {}).get("name")
                if ref:
                    fallbacks.add(ref)

    # Fallback: infer error scopes from execution-plan graph even when
    # flows[].error_handlers and raw.error_handling are empty.
    for plan in raw.get("flow_execution_plans", []):
        if plan.get("flow_name") != flow_name:
            continue
        has_error_scope = False
        for edge in plan.get("error_edges", []):
            if "error" in (edge.get("relationship_type", "") or "").lower():
                has_error_scope = True
                target = edge.get("target", "")
                if ".error-handler@" in target:
                    error_types.add("ANY")
        for scope in plan.get("scope_hierarchy", []):
            stype = (scope.get("type") or "").lower()
            if "error-handler" in stype or "on-error" in stype:
                has_error_scope = True
                error_types.add("ANY")
        if has_error_scope and not propagated:
            # Conservative default when only scope-level evidence exists.
            propagated.add("ANY")
    return {
        "error_types_handled": sorted(error_types),
        "propagated_errors": sorted(propagated),
        "retryable_errors": sorted(retryable),
        "fallback_flows": sorted(fallbacks),
    }


def _extract_output_mime(script: str) -> str:
    m = _OUT_RE.search(script or "")
    return m.group(1) if m else ""


def _extract_lhs_fields(script: str) -> list[str]:
    body = script.split("---", 1)[1] if "---" in script else script
    fields: list[str] = []
    for line in body.splitlines():
        line = line.strip().rstrip(",")
        if ":" not in line:
            continue
        lhs = line.split(":", 1)[0].strip().strip('"').strip("'")
        if lhs and re.match(r"[A-Za-z_][\w.]*$", lhs):
            fields.append(lhs)
    return fields


def _insert_tree(tree: dict[str, Any], path: str) -> None:
    node = tree
    parts = [p for p in path.split(".") if p]
    for i, part in enumerate(parts):
        if part not in node:
            node[part] = {"type": "object", "children": {}}
        if i == len(parts) - 1:
            node[part]["type"] = "scalar"
        node = node[part].setdefault("children", {})


def _risk(severity: str, category: str, description: str, confidence: float, flows: list[str]) -> dict[str, Any]:
    return {
        "severity": severity,
        "category": category,
        "description": description,
        "confidence": confidence,
        "remediation": "Review and harden this area",
        "affected_flows": [f for f in flows if f],
    }


def _norm_entity(tok: str) -> str:
    t = tok.lower()
    if t == "paymentorder":
        return "PaymentOrder"
    return t[:1].upper() + t[1:]


def _guess_target_flow(test_name: str, flows: list[str]) -> str:
    base = test_name.replace("-test", "").replace("_test", "").replace("Test", "")
    for f in flows:
        if f == base or base in f:
            return f
    return ""
