from __future__ import annotations

import re
import urllib.parse
from pathlib import Path
from typing import Any
from zipfile import ZipFile, is_zipfile

from mule_parser.core.file_registry import FileRegistryResolver
from mule_parser.core.xml_engine import parse_xml_file
from mule_parser.parsers.dataweave_parser import resolve_external_dwl_resource

_DW_OUT_RE = re.compile(r"output\s+([\w/+\-]+)", re.IGNORECASE)
_DW_TOP_KEY_RE = re.compile(r'\s*(?:"([^"]+)"|\'([^\']+)\'|([A-Za-z_]\w*))\s*:', re.MULTILINE)
_DW_REF_RE = re.compile(r"\b(payload|vars|attributes)(?:\.[A-Za-z_][\w$]*)*")
_CP_RE = re.compile(r"classpath://([A-Za-z0-9_./\\-]+)")
_ASSERT_RE = re.compile(r"(status|httpStatus|code|message|details)", re.IGNORECASE)


def enrich_munit_fixtures(
    project_root: Path,
    munit_tests: list[Any],
    flows: list[Any],
    flow_execution_plans: list[Any],
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> tuple[list[Any], dict[str, Any]]:
    resources = _discover_test_resources(project_root, file_resolver=file_resolver)
    grouped = _group_by_test_dir(resources)
    flow_names = sorted({(f.name if hasattr(f, "name") else f.get("name", "")) for f in flows if (f.name if hasattr(f, "name") else f.get("name", ""))})
    endpoint_by_flow = {fn: _endpoint_from_flow(fn) for fn in flow_names}
    unresolved = {
        "missing_fixture_files": [],
        "orphan_tests": [],
        "unresolved_flow_refs": [],
        "empty_assertions": [],
        "malformed_dwl": [],
    }
    registry = {"tests": [], "fixtures": [], "coverage": {}, "unresolved": unresolved}

    tests_out = []
    used_groups: set[str] = set()
    for test in munit_tests:
        t = test if isinstance(test, dict) else test.model_dump()
        name = t.get("name", "")

        # Use the flow_ref already extracted by munit_parser (from the
        # explicit <flow-ref name="..."> in <munit:execution>).  Only fall
        # back to the heuristic inferrer when the field is empty, which
        # happens for tests parsed from XML files other than the MUnit suite
        # (e.g. inline tests embedded in a flow config).
        flow_ref = t.get("flow_ref") or _infer_flow_ref(name, t.get("file", ""), flow_names)

        endpoint = endpoint_by_flow.get(flow_ref, "")

        # Use the fixture_group already extracted by munit_parser (the exact
        # classpath directory component from the <munit:set-event> payload/
        # attributes/variables readUrl calls).  Only fall back to substring
        # matching when the field was not pre-populated.
        fixture_group = t.get("fixture_group") or _find_group_for_test(name, grouped.keys())

        used_groups.add(fixture_group) if fixture_group else None
        fixtures = _classify_and_extract(grouped.get(fixture_group, []), flow_ref, unresolved, project_root, file_resolver=file_resolver)
        assertions = _extract_assertions(t, fixtures)
        derived = _derive_contract(fixtures, assertions)

        t["flow_ref"] = flow_ref
        t["endpoint"] = endpoint
        t["fixture_group"] = fixture_group
        t["fixtures"] = fixtures
        t["assertions"] = assertions
        t["derived_contract"] = derived
        tests_out.append(t)

        registry["tests"].append({
            "test_name": name,
            "flow_ref": flow_ref,
            "endpoint": endpoint,
            "fixtures": fixtures,
            "assertions": assertions,
            "derived_contract": derived,
        })
        for role, fx in fixtures.items():
            if isinstance(fx, dict) and fx.get("path"):
                registry["fixtures"].append({"test_name": name, "role": role, **fx})

    orphan_tests = [g for g in grouped.keys() if g and g not in used_groups]
    unresolved_flow_refs = [t["name"] for t in tests_out if not t.get("flow_ref")]
    empty_assertions = [t["name"] for t in tests_out if not t.get("assertions")]
    registry["coverage"] = _coverage(flow_names, tests_out, flow_execution_plans)
    unresolved["orphan_tests"].extend(orphan_tests)
    unresolved["unresolved_flow_refs"].extend(unresolved_flow_refs)
    unresolved["empty_assertions"].extend(empty_assertions)
    return tests_out, registry


def _discover_test_resources(project_root: Path, *, file_resolver: FileRegistryResolver | None = None) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    exts = {".dwl", ".json", ".xml", ".yaml", ".yml"}
    if file_resolver is not None:
        for f in file_resolver.files:
            norm = f.normalized_path
            if "/src/test/resources/" not in ("/" + norm).lower():
                continue
            if Path(norm).suffix.lower() not in exts:
                continue
            txt, rec, _, _ = file_resolver.read_text(norm)
            if rec is not None:
                found.append({"path": rec.normalized_path, "name": Path(norm).name, "text": txt})
        if found:
            return found
    for p in project_root.rglob("*"):
        if p.is_file() and p.suffix.lower() in exts and "src/test/resources" in str(p).replace("\\", "/"):
            found.append({"path": str(p), "name": p.name, "text": p.read_text(encoding="utf-8", errors="replace")})
    if found:
        return found
    for jar in project_root.rglob("*"):
        if not (jar.is_file() and jar.suffix.lower() in {".jar", ".zip"} and is_zipfile(jar)):
            continue
        with ZipFile(jar, "r") as zf:
            for name in zf.namelist():
                norm = name.replace("\\", "/")
                if "/src/test/resources/" not in norm:
                    continue
                if Path(norm).suffix.lower() not in exts:
                    continue
                found.append({"path": f"{jar}!/{norm}", "name": Path(norm).name, "text": zf.read(name).decode("utf-8", errors="replace")})
    return found


def _group_by_test_dir(resources: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for r in resources:
        norm = r["path"].replace("\\", "/")
        marker = "/src/test/resources/"
        idx = norm.lower().find(marker)
        group = ""
        if idx >= 0:
            sub = norm[idx + len(marker):]
            parts = sub.split("/")
            group = urllib.parse.unquote(parts[0]) if parts else ""
        grouped.setdefault(group, []).append(r)
    return grouped


def _find_group_for_test(test_name: str, groups: Any) -> str:
    tn = (test_name or "").lower()
    for g in groups:
        gl = (g or "").lower()
        if gl and (gl in tn or tn in gl):
            return g
    return ""


def _classify_and_extract(
    resources: list[dict[str, Any]],
    flow_ref: str,
    unresolved: dict[str, list[Any]],
    project_root: Path,
    *,
    file_resolver: FileRegistryResolver | None = None,
) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for r in resources:
        role = _role_from_name(r["name"])
        if not role:
            continue
        payload = {"path": r["path"], "name": r["name"], "kind": Path(r["name"]).suffix.lower().lstrip(".")}
        if r["name"].lower().endswith(".dwl"):
            meta = _extract_dwl_meta(r["text"], flow_ref)
            payload.update(meta)
            if not meta.get("source", "").strip():
                unresolved["malformed_dwl"].append(r["path"])
            for cp in meta.get("referenced_resources", []):
                if file_resolver is not None:
                    rec, _, err = file_resolver.resolve(cp)
                    resolved = rec.normalized_path if rec else ""
                else:
                    resolved, _, _, err = resolve_external_dwl_resource(project_root / "src" / "test" / "resources" / "fixture.xml", f"classpath://{cp}")
                if not resolved:
                    unresolved["missing_fixture_files"].append({"path": cp, "error": err})
        out[role] = payload
    return out


def _role_from_name(name: str) -> str:
    n = name.lower()
    if "attributes" in n:
        return "input_attributes"
    if "variables" in n:
        return "input_variables"
    if "assert" in n and "expression" in n:
        return "assertion_expression"
    if "expected" in n and "schema" in n:
        return "expected_schema"
    if "expected" in n and "payload" in n:
        return "expected_payload"
    if "payload" in n:
        return "input_payload"
    return ""


def _extract_dwl_meta(text: str, flow_ref: str) -> dict[str, Any]:
    out = _DW_OUT_RE.search(text)
    keys = sorted(set(k for g in _DW_TOP_KEY_RE.findall(text.split("---", 1)[-1]) for k in g if k))
    refs = sorted(set(m.group(0) for m in _DW_REF_RE.finditer(text)))
    cp = sorted(set(m.group(1).replace("\\", "/") for m in _CP_RE.finditer(text)))
    return {
        "source": text,
        "output_mime": out.group(1) if out else "",
        "top_level_keys": keys,
        "references": refs,
        "vars_usage": sorted({r for r in refs if r.startswith("vars.")}),
        "payload_references": sorted({r for r in refs if r.startswith("payload")}),
        "referenced_resources": cp,
        "flow_ref": flow_ref,
    }


def _extract_assertions(test: dict[str, Any], fixtures: dict[str, Any]) -> list[dict[str, Any]]:
    assertions = list(test.get("assertions", []) or [])
    fx = fixtures.get("assertion_expression")
    if isinstance(fx, dict):
        src = fx.get("source", "")
        expected_fields = sorted(set(_ASSERT_RE.findall(src)))
        assertions.append({"type": "fixture-assertion-expression", "expected_fields": expected_fields, "source": src[:4000]})
    return assertions


def _derive_contract(fixtures: dict[str, Any], assertions: list[dict[str, Any]]) -> dict[str, Any]:
    inp = fixtures.get("input_payload", {}) if isinstance(fixtures.get("input_payload"), dict) else {}
    attrs = fixtures.get("input_attributes", {}) if isinstance(fixtures.get("input_attributes"), dict) else {}
    expected = fixtures.get("expected_payload", {}) if isinstance(fixtures.get("expected_payload"), dict) else {}
    return {
        "required_inputs": sorted(set(inp.get("top_level_keys", []) + attrs.get("top_level_keys", []))),
        "expected_outputs": sorted(set(expected.get("top_level_keys", []))),
        "status_expectations": sorted(set(str(a.get("expectedStatus", "")) for a in assertions if a.get("expectedStatus"))),
        "payload_structure": expected.get("top_level_keys", []) or inp.get("top_level_keys", []),
    }


def _infer_flow_ref(test_name: str, test_file: str, flow_names: list[str]) -> str:
    doc = parse_xml_file(Path(test_file)) if test_file and Path(test_file).is_file() else None
    if doc:
        # Prefer explicit mappings declared in suite XML: <munit:test ...>
        for e in doc.root.iter():
            if not isinstance(e.tag, str):
                continue
            tag = doc.tag_name(e).lower()
            # When the element is a test definition, check its attributes and children
            if tag.endswith("test"):
                attrs = doc.attrs(e)
                tname = attrs.get("name", "")
                if tname and (tname == test_name or (test_name and (tname.lower() == test_name.lower()))):
                    # 1) check for a doc:name attribute on the test element (often used to reference the flow)
                    docname = attrs.get("doc:name", "") or attrs.get("docname", "")
                    if docname:
                        # try to match the doc:name value against known flows
                        for f in flow_names:
                            if docname.lower() in f.lower() or f.lower() in docname.lower():
                                return f
                        # if docname itself looks like a flow name, return it
                        if ":" in docname or "/" in docname:
                            return docname
                    # 2) look for explicit <flow-ref> children inside this test element
                    for child in e.iter():
                        if not isinstance(child.tag, str):
                            continue
                        if doc.tag_name(child).lower().endswith("flow-ref"):
                            ref = doc.attrs(child).get("name", "")
                            if ref:
                                return ref
                    # 3) look for any child element with a doc:name that matches a flow
                    for child in e.iter():
                        if not isinstance(child.tag, str):
                            continue
                        cattrs = doc.attrs(child)
                        cdocname = cattrs.get("doc:name", "") or cattrs.get("docname", "")
                        if cdocname:
                            for f in flow_names:
                                if cdocname.lower() in f.lower() or f.lower() in cdocname.lower():
                                    return f
        # If no explicit mapping found, fall back to scanning for any flow-ref in the file
        for e in doc.root.iter():
            if not isinstance(e.tag, str):
                continue
            if doc.tag_name(e).lower().endswith("flow-ref"):
                ref = doc.attrs(e).get("name", "")
                if ref:
                    return ref
    name = test_name or ""
    for suffix in ("-test", "_test", "Test"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    for f in flow_names:
        if name.lower() in f.lower() or f.lower() in name.lower():
            return f
    return ""


def _endpoint_from_flow(flow: str) -> str:
    m = re.match(r"^(get|post|put|patch|delete|head|options)\s*:\s*(.+)$", flow or "", re.IGNORECASE)
    if not m:
        return ""
    return f"{m.group(1).upper()} {m.group(2)}"


def _coverage(flow_names: list[str], tests_out: list[dict[str, Any]], flow_execution_plans: list[Any]) -> dict[str, Any]:
    by_flow: dict[str, list[str]] = {}
    for t in tests_out:
        fr = t.get("flow_ref", "")
        if fr:
            by_flow.setdefault(fr, []).append(t.get("name", ""))
    flows_with = sorted(by_flow.keys())
    flows_without = sorted(f for f in flow_names if f not in by_flow)
    endpoint_cov = {(_endpoint_from_flow(f) or f): len(by_flow.get(f, [])) for f in flow_names}
    transform_cov = {}
    for p in flow_execution_plans:
        pd = p if isinstance(p, dict) else p.model_dump()
        fn = pd.get("flow_name", "")
        dw_steps = [s for s in pd.get("steps", []) if s.get("attributes", {}).get("dataweave_script_ids")]
        transform_cov[fn] = {"dw_steps": len(dw_steps), "has_test": fn in by_flow}
    return {
        "flows_with_tests": flows_with,
        "flows_without_tests": flows_without,
        "endpoint_coverage": endpoint_cov,
        "transform_coverage": transform_cov,
    }








# from __future__ import annotations

# import re
# import urllib.parse
# from pathlib import Path
# from typing import Any
# from zipfile import ZipFile, is_zipfile

# from mule_parser.core.file_registry import FileRegistryResolver
# from mule_parser.core.xml_engine import parse_xml_file
# from mule_parser.parsers.dataweave_parser import resolve_external_dwl_resource

# _DW_OUT_RE = re.compile(r"output\s+([\w/+\-]+)", re.IGNORECASE)
# _DW_TOP_KEY_RE = re.compile(r'\s*(?:"([^"]+)"|\'([^\']+)\'|([A-Za-z_]\w*))\s*:', re.MULTILINE)
# _DW_REF_RE = re.compile(r"\b(payload|vars|attributes)(?:\.[A-Za-z_][\w$]*)*")
# _CP_RE = re.compile(r"classpath://([A-Za-z0-9_./\\-]+)")
# _ASSERT_RE = re.compile(r"(status|httpStatus|code|message|details)", re.IGNORECASE)


# def enrich_munit_fixtures(
#     project_root: Path,
#     munit_tests: list[Any],
#     flows: list[Any],
#     flow_execution_plans: list[Any],
#     *,
#     file_resolver: FileRegistryResolver | None = None,
# ) -> tuple[list[Any], dict[str, Any]]:
#     resources = _discover_test_resources(project_root, file_resolver=file_resolver)
#     grouped = _group_by_test_dir(resources)
#     flow_names = sorted({(f.name if hasattr(f, "name") else f.get("name", "")) for f in flows if (f.name if hasattr(f, "name") else f.get("name", ""))})
#     endpoint_by_flow = {fn: _endpoint_from_flow(fn) for fn in flow_names}
#     unresolved = {
#         "missing_fixture_files": [],
#         "orphan_tests": [],
#         "unresolved_flow_refs": [],
#         "empty_assertions": [],
#         "malformed_dwl": [],
#     }
#     registry = {"tests": [], "fixtures": [], "coverage": {}, "unresolved": unresolved}

#     tests_out = []
#     used_groups: set[str] = set()
#     for test in munit_tests:
#         t = test if isinstance(test, dict) else test.model_dump()
#         name = t.get("name", "")
#         flow_ref = _infer_flow_ref(name, t.get("file", ""), flow_names)
#         endpoint = endpoint_by_flow.get(flow_ref, "")
#         fixture_group = _find_group_for_test(name, grouped.keys())
#         used_groups.add(fixture_group) if fixture_group else None
#         fixtures = _classify_and_extract(grouped.get(fixture_group, []), flow_ref, unresolved, project_root, file_resolver=file_resolver)
#         assertions = _extract_assertions(t, fixtures)
#         derived = _derive_contract(fixtures, assertions)

#         t["flow_ref"] = flow_ref
#         t["endpoint"] = endpoint
#         t["fixture_group"] = fixture_group
#         t["fixtures"] = fixtures
#         t["assertions"] = assertions
#         t["derived_contract"] = derived
#         tests_out.append(t)

#         registry["tests"].append({
#             "test_name": name,
#             "flow_ref": flow_ref,
#             "endpoint": endpoint,
#             "fixtures": fixtures,
#             "assertions": assertions,
#             "derived_contract": derived,
#         })
#         for role, fx in fixtures.items():
#             if isinstance(fx, dict) and fx.get("path"):
#                 registry["fixtures"].append({"test_name": name, "role": role, **fx})

#     orphan_tests = [g for g in grouped.keys() if g and g not in used_groups]
#     unresolved_flow_refs = [t["name"] for t in tests_out if not t.get("flow_ref")]
#     empty_assertions = [t["name"] for t in tests_out if not t.get("assertions")]
#     registry["coverage"] = _coverage(flow_names, tests_out, flow_execution_plans)
#     unresolved["orphan_tests"].extend(orphan_tests)
#     unresolved["unresolved_flow_refs"].extend(unresolved_flow_refs)
#     unresolved["empty_assertions"].extend(empty_assertions)
#     return tests_out, registry


# def _discover_test_resources(project_root: Path, *, file_resolver: FileRegistryResolver | None = None) -> list[dict[str, Any]]:
#     found: list[dict[str, Any]] = []
#     exts = {".dwl", ".json", ".xml", ".yaml", ".yml"}
#     if file_resolver is not None:
#         for f in file_resolver.files:
#             norm = f.normalized_path
#             if "/src/test/resources/" not in ("/" + norm).lower():
#                 continue
#             if Path(norm).suffix.lower() not in exts:
#                 continue
#             txt, rec, _, _ = file_resolver.read_text(norm)
#             if rec is not None:
#                 found.append({"path": rec.normalized_path, "name": Path(norm).name, "text": txt})
#         if found:
#             return found
#     for p in project_root.rglob("*"):
#         if p.is_file() and p.suffix.lower() in exts and "src/test/resources" in str(p).replace("\\", "/"):
#             found.append({"path": str(p), "name": p.name, "text": p.read_text(encoding="utf-8", errors="replace")})
#     if found:
#         return found
#     for jar in project_root.rglob("*"):
#         if not (jar.is_file() and jar.suffix.lower() in {".jar", ".zip"} and is_zipfile(jar)):
#             continue
#         with ZipFile(jar, "r") as zf:
#             for name in zf.namelist():
#                 norm = name.replace("\\", "/")
#                 if "/src/test/resources/" not in norm:
#                     continue
#                 if Path(norm).suffix.lower() not in exts:
#                     continue
#                 found.append({"path": f"{jar}!/{norm}", "name": Path(norm).name, "text": zf.read(name).decode("utf-8", errors="replace")})
#     return found


# def _group_by_test_dir(resources: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
#     grouped: dict[str, list[dict[str, Any]]] = {}
#     for r in resources:
#         norm = r["path"].replace("\\", "/")
#         marker = "/src/test/resources/"
#         idx = norm.lower().find(marker)
#         group = ""
#         if idx >= 0:
#             sub = norm[idx + len(marker):]
#             parts = sub.split("/")
#             group = urllib.parse.unquote(parts[0]) if parts else ""
#         grouped.setdefault(group, []).append(r)
#     return grouped


# def _find_group_for_test(test_name: str, groups: Any) -> str:
#     tn = (test_name or "").lower()
#     for g in groups:
#         gl = (g or "").lower()
#         if gl and (gl in tn or tn in gl):
#             return g
#     return ""


# def _classify_and_extract(
#     resources: list[dict[str, Any]],
#     flow_ref: str,
#     unresolved: dict[str, list[Any]],
#     project_root: Path,
#     *,
#     file_resolver: FileRegistryResolver | None = None,
# ) -> dict[str, Any]:
#     out: dict[str, Any] = {}
#     for r in resources:
#         role = _role_from_name(r["name"])
#         if not role:
#             continue
#         payload = {"path": r["path"], "name": r["name"], "kind": Path(r["name"]).suffix.lower().lstrip(".")}
#         if r["name"].lower().endswith(".dwl"):
#             meta = _extract_dwl_meta(r["text"], flow_ref)
#             payload.update(meta)
#             if not meta.get("source", "").strip():
#                 unresolved["malformed_dwl"].append(r["path"])
#             for cp in meta.get("referenced_resources", []):
#                 if file_resolver is not None:
#                     rec, _, err = file_resolver.resolve(cp)
#                     resolved = rec.normalized_path if rec else ""
#                 else:
#                     resolved, _, _, err = resolve_external_dwl_resource(project_root / "src" / "test" / "resources" / "fixture.xml", f"classpath://{cp}")
#                 if not resolved:
#                     unresolved["missing_fixture_files"].append({"path": cp, "error": err})
#         out[role] = payload
#     return out


# def _role_from_name(name: str) -> str:
#     n = name.lower()
#     if "attributes" in n:
#         return "input_attributes"
#     if "variables" in n:
#         return "input_variables"
#     if "assert" in n and "expression" in n:
#         return "assertion_expression"
#     if "expected" in n and "schema" in n:
#         return "expected_schema"
#     if "expected" in n and "payload" in n:
#         return "expected_payload"
#     if "payload" in n:
#         return "input_payload"
#     return ""


# def _extract_dwl_meta(text: str, flow_ref: str) -> dict[str, Any]:
#     out = _DW_OUT_RE.search(text)
#     keys = sorted(set(k for g in _DW_TOP_KEY_RE.findall(text.split("---", 1)[-1]) for k in g if k))
#     refs = sorted(set(m.group(0) for m in _DW_REF_RE.finditer(text)))
#     cp = sorted(set(m.group(1).replace("\\", "/") for m in _CP_RE.finditer(text)))
#     return {
#         "source": text,
#         "output_mime": out.group(1) if out else "",
#         "top_level_keys": keys,
#         "references": refs,
#         "vars_usage": sorted({r for r in refs if r.startswith("vars.")}),
#         "payload_references": sorted({r for r in refs if r.startswith("payload")}),
#         "referenced_resources": cp,
#         "flow_ref": flow_ref,
#     }


# def _extract_assertions(test: dict[str, Any], fixtures: dict[str, Any]) -> list[dict[str, Any]]:
#     assertions = list(test.get("assertions", []) or [])
#     fx = fixtures.get("assertion_expression")
#     if isinstance(fx, dict):
#         src = fx.get("source", "")
#         expected_fields = sorted(set(_ASSERT_RE.findall(src)))
#         assertions.append({"type": "fixture-assertion-expression", "expected_fields": expected_fields, "source": src[:4000]})
#     return assertions


# def _derive_contract(fixtures: dict[str, Any], assertions: list[dict[str, Any]]) -> dict[str, Any]:
#     inp = fixtures.get("input_payload", {}) if isinstance(fixtures.get("input_payload"), dict) else {}
#     attrs = fixtures.get("input_attributes", {}) if isinstance(fixtures.get("input_attributes"), dict) else {}
#     expected = fixtures.get("expected_payload", {}) if isinstance(fixtures.get("expected_payload"), dict) else {}
#     return {
#         "required_inputs": sorted(set(inp.get("top_level_keys", []) + attrs.get("top_level_keys", []))),
#         "expected_outputs": sorted(set(expected.get("top_level_keys", []))),
#         "status_expectations": sorted(set(str(a.get("expectedStatus", "")) for a in assertions if a.get("expectedStatus"))),
#         "payload_structure": expected.get("top_level_keys", []) or inp.get("top_level_keys", []),
#     }


# def _infer_flow_ref(test_name: str, test_file: str, flow_names: list[str]) -> str:
#     doc = parse_xml_file(Path(test_file)) if test_file and Path(test_file).is_file() else None
#     if doc:
#         # Prefer explicit mappings declared in suite XML: <munit:test ...>
#         for e in doc.root.iter():
#             if not isinstance(e.tag, str):
#                 continue
#             tag = doc.tag_name(e).lower()
#             # When the element is a test definition, check its attributes and children
#             if tag.endswith("test"):
#                 attrs = doc.attrs(e)
#                 tname = attrs.get("name", "")
#                 if tname and (tname == test_name or (test_name and (tname.lower() == test_name.lower()))):
#                     # 1) check for a doc:name attribute on the test element (often used to reference the flow)
#                     docname = attrs.get("doc:name", "") or attrs.get("docname", "")
#                     if docname:
#                         # try to match the doc:name value against known flows
#                         for f in flow_names:
#                             if docname.lower() in f.lower() or f.lower() in docname.lower():
#                                 return f
#                         # if docname itself looks like a flow name, return it
#                         if ":" in docname or "/" in docname:
#                             return docname
#                     # 2) look for explicit <flow-ref> children inside this test element
#                     for child in e.iter():
#                         if not isinstance(child.tag, str):
#                             continue
#                         if doc.tag_name(child).lower().endswith("flow-ref"):
#                             ref = doc.attrs(child).get("name", "")
#                             if ref:
#                                 return ref
#                     # 3) look for any child element with a doc:name that matches a flow
#                     for child in e.iter():
#                         if not isinstance(child.tag, str):
#                             continue
#                         cattrs = doc.attrs(child)
#                         cdocname = cattrs.get("doc:name", "") or cattrs.get("docname", "")
#                         if cdocname:
#                             for f in flow_names:
#                                 if cdocname.lower() in f.lower() or f.lower() in cdocname.lower():
#                                     return f
#         # If no explicit mapping found, fall back to scanning for any flow-ref in the file
#         for e in doc.root.iter():
#             if not isinstance(e.tag, str):
#                 continue
#             if doc.tag_name(e).lower().endswith("flow-ref"):
#                 ref = doc.attrs(e).get("name", "")
#                 if ref:
#                     return ref
#     name = test_name or ""
#     for suffix in ("-test", "_test", "Test"):
#         if name.endswith(suffix):
#             name = name[: -len(suffix)]
#             break
#     for f in flow_names:
#         if name.lower() in f.lower() or f.lower() in name.lower():
#             return f
#     return ""


# def _endpoint_from_flow(flow: str) -> str:
#     m = re.match(r"^(get|post|put|patch|delete|head|options)\s*:\s*(.+)$", flow or "", re.IGNORECASE)
#     if not m:
#         return ""
#     return f"{m.group(1).upper()} {m.group(2)}"


# def _coverage(flow_names: list[str], tests_out: list[dict[str, Any]], flow_execution_plans: list[Any]) -> dict[str, Any]:
#     by_flow: dict[str, list[str]] = {}
#     for t in tests_out:
#         fr = t.get("flow_ref", "")
#         if fr:
#             by_flow.setdefault(fr, []).append(t.get("name", ""))
#     flows_with = sorted(by_flow.keys())
#     flows_without = sorted(f for f in flow_names if f not in by_flow)
#     endpoint_cov = {(_endpoint_from_flow(f) or f): len(by_flow.get(f, [])) for f in flow_names}
#     transform_cov = {}
#     for p in flow_execution_plans:
#         pd = p if isinstance(p, dict) else p.model_dump()
#         fn = pd.get("flow_name", "")
#         dw_steps = [s for s in pd.get("steps", []) if s.get("attributes", {}).get("dataweave_script_ids")]
#         transform_cov[fn] = {"dw_steps": len(dw_steps), "has_test": fn in by_flow}
#     return {
#         "flows_with_tests": flows_with,
#         "flows_without_tests": flows_without,
#         "endpoint_coverage": endpoint_cov,
#         "transform_coverage": transform_cov,
#     }
