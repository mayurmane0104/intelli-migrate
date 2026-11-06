"""Safe, read-only analysis of SAP Integration Suite export archives.

Archives are read in place with strict limits; uploaded scripts and expressions
are never executed and no archive paths are extracted to the filesystem.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import stat
import uuid
import zipfile
from datetime import datetime, timezone
from typing import Any

from lxml import etree

MAX_UPLOAD_BYTES = 50 * 1024 * 1024
MAX_ENTRIES = 2_000
MAX_FILE_BYTES = 20 * 1024 * 1024
MAX_EXPANDED_BYTES = 100 * 1024 * 1024
MAX_COMPRESSION_RATIO = 200
_BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"
_RESOURCE_TYPES = {
    ".groovy": "script", ".js": "script", ".xslt": "xslt", ".xsl": "xslt",
    ".mmap": "message_mapping", ".mappings": "message_mapping", ".iflw": "iflow",
    ".xsd": "schema", ".wsdl": "wsdl", ".json": "json", ".xml": "xml",
    ".prop": "properties", ".propdef": "properties", ".properties": "properties",
    ".zip": "nested_archive", ".cnt": "package_metadata", ".md": "documentation",
}
_SECRET_KEY = re.compile(r"password|passwd|secret|token|credential|private.?key|authorization", re.I)
_INLINE_SECRET = re.compile(r"(?i)(password|passwd|secret|token|client[_-]?secret)\s*([=:])\s*([^\s,;]+)")


def _redact(value: str) -> str:
    return _INLINE_SECRET.sub(lambda match: f"{match.group(1)}{match.group(2)}[REDACTED]", value)


class SAPReferenceError(ValueError):
    """A safe, user-facing reference archive validation error."""


def _validate_entries(zf: zipfile.ZipFile) -> list[zipfile.ZipInfo]:
    infos = zf.infolist()
    if not infos or len(infos) > MAX_ENTRIES:
        raise SAPReferenceError(f"Archive must contain between 1 and {MAX_ENTRIES} entries.")
    total = 0
    seen: set[str] = set()
    for info in infos:
        name = info.filename
        normalized = name.replace("\\", "/")
        parts = normalized.split("/")
        if (not name or normalized.startswith("/") or re.match(r"^[A-Za-z]:", normalized)
                or any(p in ("..", ".") for p in parts) or "\x00" in name):
            raise SAPReferenceError("Archive contains an unsafe path.")
        if normalized in seen:
            raise SAPReferenceError("Archive contains duplicate paths.")
        seen.add(normalized)
        if info.flag_bits & 0x1:
            raise SAPReferenceError("Encrypted archive entries are not supported.")
        if stat.S_ISLNK(info.external_attr >> 16):
            raise SAPReferenceError("Symbolic links are not supported in SAP archives.")
        if info.file_size > MAX_FILE_BYTES:
            raise SAPReferenceError("An archive entry exceeds the uncompressed file size limit.")
        total += info.file_size
        if total > MAX_EXPANDED_BYTES:
            raise SAPReferenceError("Archive expanded size exceeds the configured limit.")
        if info.file_size and (not info.compress_size or info.file_size / info.compress_size > MAX_COMPRESSION_RATIO):
            raise SAPReferenceError("Archive contains a suspicious compression ratio.")
        if not info.is_dir():
            suffix = "." + normalized.rsplit(".", 1)[-1].lower() if "." in normalized.rsplit("/", 1)[-1] else ""
            basename = normalized.rsplit("/", 1)[-1]
            if basename.lower() not in {"manifest.mf", "resources.cnt", "contentmetadata.md", "exportinformation.info", "hash", ".project"} and not basename.endswith("_content") and suffix not in _RESOURCE_TYPES and suffix != ".mf":
                raise SAPReferenceError(f"Unsupported file type in SAP archive: {suffix or '(no extension)'}.")
    return infos


def _manifest(data: bytes) -> tuple[dict[str, str], list[str]]:
    warnings: list[str] = []
    text = data.decode("utf-8-sig", errors="replace")
    if "\ufffd" in text:
        warnings.append("Manifest contained undecodable bytes; replacement decoding was used.")
    unfolded: list[str] = []
    for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if line.startswith(" ") and unfolded:
            unfolded[-1] += line[1:]
        else:
            unfolded.append(line)
    attrs: dict[str, str] = {}
    duplicates: list[str] = []
    for line in unfolded:
        if not line.strip():
            continue
        if ":" not in line:
            warnings.append("Manifest contains a malformed attribute line.")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in attrs:
            duplicates.append(key)
        attrs[key] = "[REDACTED]" if _SECRET_KEY.search(key) else _redact(value)
    if duplicates:
        warnings.append("Duplicate manifest attributes found: " + ", ".join(sorted(set(duplicates))))
    return attrs, warnings


def _parse_bpmn(path: str, data: bytes) -> dict[str, Any]:
    parser = etree.XMLParser(resolve_entities=False, no_network=True, load_dtd=False, recover=False, huge_tree=False)
    try:
        root = etree.fromstring(data, parser=parser)
    except (etree.XMLSyntaxError, ValueError) as exc:
        return {"path": path, "valid_xml": False, "error": f"Invalid BPMN XML: {str(exc).splitlines()[0][:180]}"}
    elements = list(root.iter())
    def local(el: Any) -> str:
        return etree.QName(el).localname
    flows = [el for el in elements if local(el) == "sequenceFlow"]
    ids = {el.get("id") for el in elements if el.get("id")}
    unresolved = [el.get("id", "(unnamed)") for el in flows if el.get("sourceRef") not in ids or el.get("targetRef") not in ids]
    task_counts: dict[str, int] = {}
    adapter_configs = []
    for el in elements:
        name = local(el)
        if name in {"startEvent", "endEvent", "serviceTask", "scriptTask", "callActivity", "exclusiveGateway", "parallelGateway", "inclusiveGateway", "sequenceFlow", "messageFlow", "participant", "collaboration"}:
            task_counts[name] = task_counts.get(name, 0) + 1
        if "adapter" in name.lower() or "channel" in name.lower():
            attributes = {etree.QName(key).localname.lower(): value for key, value in el.attrib.items()}
            adapter_type = next((attributes[k] for k in ("adaptertype", "type", "protocol") if attributes.get(k)), None)
            direction = "sender" if "sender" in name.lower() else "receiver" if "receiver" in name.lower() else None
            adapter_configs.append({"type": _redact(adapter_type) if adapter_type else None, "direction": direction, "channel_name": _redact(attributes["name"]) if attributes.get("name") else None,
                                    "endpoint_configured": any(k in attributes for k in ("address", "endpoint", "url")),
                                    "authentication_configured": any("auth" in k for k in attributes),
                                    "sensitive_values_redacted": True})
    # Event sub-processes cannot have incoming or outgoing sequence flows (BPMN 2.0.2 spec 10.5.3)
    event_subprocs = {
        el.get("id") for el in elements
        if local(el) == "subProcess" and (
            el.get("triggeredByEvent") == "true" or
            el.get("{http:///com.sap.ifl.model/Ifl.xsd}type") == "ErrorEventSubProcessTemplate"
        )
    }
    illegal_subproc_flows = [
        el.get("id", "(unnamed)") for el in flows
        if el.get("sourceRef") in event_subprocs or el.get("targetRef") in event_subprocs
    ]

    # Timer start events cannot receive incoming message flows
    timer_start_ids = {
        el.get("id") for el in elements
        if local(el) == "startEvent" and any(local(c) == "timerEventDefinition" for c in el)
    }
    msg_flows = [el for el in elements if local(el) == "messageFlow"]
    illegal_timer_flows = [
        el.get("id", "(unnamed)") for el in msg_flows
        if el.get("targetRef") in timer_start_ids
    ]

    processes = [el for el in elements if local(el) == "process"]
    return {
        "path": path, "valid_xml": True, "root_namespace": etree.QName(root).namespace,
        "processes": [{"id": p.get("id"), "name": p.get("name")} for p in processes],
        "element_counts": task_counts, "unresolved_sequence_flows": unresolved,
        "illegal_subproc_flows": illegal_subproc_flows,
        "illegal_timer_flows": illegal_timer_flows,
        "adapter_configs": adapter_configs,
        "sap_extension_namespaces": sorted({ns for ns in (root.nsmap or {}).values() if ns and ("sap" in ns.lower() or "ifl" in ns.lower())}),
        "namespace_map": {k or "default": v for k, v in (root.nsmap or {}).items()},
    }


def _iflow(data: bytes, label: str) -> dict[str, Any]:
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            infos = _validate_entries(zf)
            entries = {i.filename: zf.read(i) for i in infos if not i.is_dir()}
    except (zipfile.BadZipFile, OSError) as exc:
        raise SAPReferenceError(f"Invalid nested iFlow archive ({label}).") from exc
    manifest_path = next((n for n in entries if n.lower().endswith("meta-inf/manifest.mf")), None)
    attrs, warnings = _manifest(entries[manifest_path]) if manifest_path else ({}, ["Missing MANIFEST.MF."])
    bsn = attrs.get("Bundle-SymbolicName", "").split(";", 1)[0].strip()
    bpmn_paths = [n for n in entries if n.lower().endswith((".iflw", ".bpmn", ".bpmn2"))]
    if not bpmn_paths:
        raise SAPReferenceError(f"iFlow archive '{label}' has no BPMN integration flow model.")
    bpmn = [_parse_bpmn(n, entries[n]) for n in bpmn_paths]
    resources = []
    adapters = []
    for model in bpmn:
        adapters.extend(model.get("adapter_configs", []))
    for path, content in entries.items():
        base = path.rsplit("/", 1)[-1]
        suffix = "." + base.rsplit(".", 1)[-1].lower() if "." in base else ""
        kind = _RESOURCE_TYPES.get(suffix)
        if kind:
            resources.append({"name": base, "path": path, "type": kind, "size_bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()})
        if "adapter" in path.lower() or "receiver" in path.lower() or "sender" in path.lower():
            adapters.append({"path": path, "type": next((n for n in ("HTTP", "HTTPS", "SOAP", "REST", "SFTP", "FTP", "JDBC", "ODATA", "IDOC", "RFC", "PROCESSDIRECT", "AMQP") if n.lower() in path.lower()), "unknown"), "details": "Adapter-like resource path detected; values not extracted."})
    if not bsn:
        warnings.append("Missing Bundle-SymbolicName; no canonical artifact identifier could be confirmed.")
    scripts = [r for r in resources if r["type"] == "script"]
    mappings = [r for r in resources if r["type"] == "message_mapping"]
    return {"artifact_id": bsn or None, "manifest": attrs, "manifest_warnings": warnings, "bpmn": bpmn, "resources": resources, "adapters": adapters, "expanded_size_bytes": sum(len(value) for value in entries.values()), "script_count": len(scripts), "mapping_count": len(mappings)}


def _infer_identifier_convention(identifiers: list[str]) -> list[dict[str, Any]]:
    """Report a repeated identifier casing style only when at least 3 IDs agree."""
    unique = list(dict.fromkeys(value for value in identifiers if value))
    if len(unique) < 3:
        return []

    def classify(value: str) -> str | None:
        if re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)+", value):
            return "lower_snake_case"
        if re.fullmatch(r"[A-Z0-9]+(?:_[A-Z0-9]+)+", value):
            return "upper_snake_case"
        if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", value):
            return "kebab_case"
        if re.fullmatch(r"[A-Z][a-zA-Z0-9]*", value) and re.search(r"[a-z][A-Z]", value):
            return "pascal_case"
        if re.fullmatch(r"[a-z][a-zA-Z0-9]*", value) and re.search(r"[a-z][A-Z]", value):
            return "camel_case"
        return None

    styles = [classify(value) for value in unique]
    observed = [style for style in styles if style]
    if len(observed) < 3:
        return []
    from collections import Counter
    style, count = Counter(observed).most_common(1)[0]
    if count < 3 or count / len(unique) < 0.8:
        return []
    return [{"scope": "artifact_identifiers", "style": style, "confidence": "inferred",
             "basis": "repeated Bundle-SymbolicName values", "basis_artifact_count": count}]


def analyze_sap_reference(data: bytes, filename: str = "reference.zip") -> dict[str, Any]:
    """Validate and analyze a native SAP iFlow or content package ZIP."""
    if not filename.lower().endswith(".zip"):
        raise SAPReferenceError("SAP reference uploads must use the .zip extension.")
    if not data or len(data) > MAX_UPLOAD_BYTES:
        raise SAPReferenceError(f"Upload must be between 1 byte and {MAX_UPLOAD_BYTES // (1024 * 1024)} MB.")
    if not data.startswith((b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")):
        raise SAPReferenceError("File signature is not a ZIP archive.")
    try:
        zf = zipfile.ZipFile(io.BytesIO(data))
        infos = _validate_entries(zf)
        entries = {i.filename: zf.read(i) for i in infos if not i.is_dir()}
    except SAPReferenceError:
        raise
    except (zipfile.BadZipFile, OSError, RuntimeError) as exc:
        raise SAPReferenceError("The uploaded ZIP is corrupt or cannot be read.") from exc

    outer_names = set(entries)
    warnings: list[str] = []
    package = "resources.cnt" in outer_names and any(n.endswith("_content") for n in outer_names)
    has_iflow_model = any("src/main/resources/scenarioflows/integrationflow/" in n.lower() and n.lower().endswith(".iflw") for n in outer_names)
    iflow_signature = has_iflow_model and (any(n.lower().endswith("meta-inf/manifest.mf") for n in outer_names) or len(outer_names) >= 2)
    if package:
        artifact_type = "content_package"
        candidates = [n for n in entries if n.endswith("_content") and entries[n].startswith(b"PK")]
        if not candidates:
            raise SAPReferenceError("Content package has resources.cnt but no nested iFlow artifacts.")
        if len(candidates) > 100:
            raise SAPReferenceError("Content package contains more than 100 nested iFlow artifacts.")
        flows = [_iflow(entries[n], n) for n in candidates]
        if sum(flow["expanded_size_bytes"] for flow in flows) > MAX_EXPANDED_BYTES:
            raise SAPReferenceError("Nested iFlow expanded size exceeds the configured package limit.")
        try:
            raw = entries["resources.cnt"].decode("utf-8")
            package_resources = json.loads(__import__("base64").b64decode(raw).decode("utf-8"))
        except Exception:
            package_resources = None
        metadata = {"resource_count": len(package_resources.get("resources", [])) if isinstance(package_resources, dict) else None,
                    "resources_manifest_parsed": isinstance(package_resources, dict),
                    "metadata_file_present": "contentmetadata.md" in outer_names,
                    "integrity_file_present": "hash" in outer_names,
                    "export_information_present": "ExportInformation.info" in outer_names}
        if not metadata["resources_manifest_parsed"]:
            warnings.append("resources.cnt was present but its resource index could not be decoded.")
    elif iflow_signature:
        artifact_type = "iflow"
        flows = [_iflow(data, filename)]
        metadata = {}
    else:
        raise SAPReferenceError("Archive does not match a supported native SAP iFlow or content package structure.")
    ids = [f["artifact_id"] for f in flows if f.get("artifact_id")]
    duplicate_ids = sorted({x for x in ids if ids.count(x) > 1})
    warnings.extend(w for flow in flows for w in flow["manifest_warnings"])
    if duplicate_ids:
        warnings.append("Duplicate Bundle-SymbolicName identifiers: " + ", ".join(duplicate_ids))
    if artifact_type == "content_package" and metadata.get("integrity_file_present"):
        warnings.append("Package integrity metadata is present; its SAP proprietary hash has not been verified.")
    return {
        "reference_id": str(uuid.uuid4()), "artifact_type": artifact_type,
        "platform": "SAP_INTEGRATION_SUITE", "analysis_status": "completed",
        "package_metadata": metadata, "artifacts": flows, "artifact_identifiers": ids,
        "adapter_inventory": [a for flow in flows for a in flow["adapters"]],
        "resource_inventory": [r for flow in flows for r in flow["resources"]],
        "script_inventory": [r for flow in flows for r in flow["resources"] if r["type"] == "script"],
        "mapping_inventory": [r for flow in flows for r in flow["resources"] if r["type"] == "message_mapping"],
        "bpmn_metadata": [b for flow in flows for b in flow["bpmn"]],
        "naming_conventions": _infer_identifier_convention(ids), "structural_patterns": [],
        "compatibility_observations": ["Facts are limited to the uploaded archive and do not represent the entire tenant."],
        "validation_warnings": warnings, "created_at": datetime.now(timezone.utc).isoformat(),
    }
