"""
mule_parser/platforms/sap/validator.py  –  Diagnostic Utility for SAP CPI Packages and Artifacts.

Provides comprehensive validation and comparison for SAP CPI exports:
- Inspects outer ZIP entries and nested artifact archives.
- Verifies required package files and metadata (resources.cnt, contentmetadata.md, hash, ExportInformation.info).
- Validates BPMN2 .iflw XML for well-formedness, complete namespaces, valid sequence flow endpoints,
  and unique element identifiers.
- Checks script and parameter resolution.
- Compares generated packages against known-good reference packages when available.
- Usable via CLI or programmatically.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import Any


def _open_zip(source: str | Path | bytes) -> zipfile.ZipFile:
    if isinstance(source, (str, Path)):
        return zipfile.ZipFile(str(source), mode="r")
    elif isinstance(source, bytes):
        return zipfile.ZipFile(io.BytesIO(source), mode="r")
    raise ValueError(f"Unsupported ZIP source: {type(source)}")


def validate_iflow_xml_content(xml_bytes: bytes, filename: str) -> dict[str, Any]:
    """Validates BPMN2 .iflw XML well-formedness, namespaces, sequence flows, and IDs."""
    result: dict[str, Any] = {
        "filename": filename,
        "is_valid": False,
        "errors": [],
        "warnings": [],
        "declared_namespaces": {},
        "process_elements": [],
        "sequence_flows_count": 0,
        "duplicate_ids": [],
        "unresolved_sequence_endpoints": [],
    }

    try:
        xml_str = xml_bytes.decode("utf-8")
    except UnicodeDecodeError as e:
        result["errors"].append(f"Failed to decode XML as UTF-8: {e}")
        return result

    # 1. Parse XML
    try:
        root = ET.fromstring(xml_str)
        result["is_valid"] = True
    except ET.ParseError as pe:
        result["errors"].append(f"XML parse error: {pe}")
        return result

    # 2. Inspect root tag and envelope
    if not (root.tag.endswith("definitions") or root.tag.endswith("process")):
        result["warnings"].append(f"Unexpected XML root tag '{root.tag}'; standard SAP root is bpmn2:definitions.")

    # 3. Check for deprecated or alien IFL namespace
    if "http://www.sap.com/Integration/IFL" in xml_str:
        result["errors"].append("Found invalid/alien namespace 'http://www.sap.com/Integration/IFL'. Native SAP CPI requires 'http:///com.sap.ifl.model/Ifl.xsd'.")
        result["is_valid"] = False

    # Check for non-compliant serviceTask elements
    service_tasks = [e for e in root.iter() if e.tag.endswith("serviceTask")]
    if service_tasks:
        result["errors"].append(f"Found {len(service_tasks)} non-compliant BPMN2 serviceTask elements. SAP CPI requires callActivity.")
        result["is_valid"] = False

    # Check for illegal direct children inside callActivity
    for ca in root.iter():
        if ca.tag.endswith("callActivity"):
            for child in ca:
                c_tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                if c_tag not in ("extensionElements", "incoming", "outgoing"):
                    result["errors"].append(f"CallActivity '{ca.get('id')}' contains illegal child element '{c_tag}'.")
                    result["is_valid"] = False

    # Check for dangling boundaryEvents
    for be in root.iter():
        if be.tag.endswith("boundaryEvent"):
            if not be.get("attachedToRef"):
                result["errors"].append(f"BoundaryEvent '{be.get('id')}' is missing required 'attachedToRef' attribute.")
                result["is_valid"] = False

    # Check for multiple processes
    procs = [e for e in root if e.tag.endswith("process")]
    if len(procs) > 1:
        result["errors"].append(f"Found {len(procs)} bpmn2:process elements. SAP CPI requires exactly one primary executable process per IFlow.")
        result["is_valid"] = False

    # Check for collaboration and participant definitions
    collab = next((e for e in root if e.tag.endswith("collaboration")), None)
    if collab is None:
        result["errors"].append("Missing required 'bpmn2:collaboration' envelope.")
        result["is_valid"] = False
    else:
        participants = [p for p in collab if p.tag.endswith("participant")]
        ptypes = {p.get("{http:///com.sap.ifl.model/Ifl.xsd}type") or p.get("type") for p in participants}
        if "EndpointSender" not in ptypes:
            result["warnings"].append("Collaboration missing 'EndpointSender' participant.")
        if "IntegrationProcess" not in ptypes:
            result["warnings"].append("Collaboration missing 'IntegrationProcess' participant.")

    # Check for BPMNDiagram
    diagram = next((e for e in root if e.tag.endswith("BPMNDiagram")), None)
    if diagram is None:
        result["warnings"].append("Missing 'bpmndi:BPMNDiagram' visual layout.")

    # 4. Check for undeclared prefixes in raw XML
    known_prefixes = ["bpmn2", "bpmn", "bpmndi", "dc", "di", "ifl", "xsi", "camunda", "if", "ift", "iflw"]
    for pfx in known_prefixes:
        if (f"<{pfx}:" in xml_str or f" {pfx}:" in xml_str) and f"xmlns:{pfx}=" not in xml_str:
            result["errors"].append(f"Undeclared XML prefix '{pfx}' used in elements or attributes.")
            result["is_valid"] = False

    # 5. Check element IDs and duplicate IDs
    element_ids = set()
    dup_ids = set()
    for elem in root.iter():
        elem_id = elem.get("id")
        if elem_id:
            if elem_id in element_ids:
                dup_ids.add(elem_id)
            else:
                element_ids.add(elem_id)
            result["process_elements"].append(elem_id)

    if dup_ids:
        result["duplicate_ids"] = sorted(dup_ids)
        result["errors"].append(f"Duplicate element IDs found: {sorted(dup_ids)}")
        result["is_valid"] = False

    # 6. Check sequence flows
    seq_flows = [e for e in root.iter() if e.tag.endswith("sequenceFlow")]
    result["sequence_flows_count"] = len(seq_flows)

    unresolved_endpoints = []
    for sf in seq_flows:
        sf_id = sf.get("id", "unknown_flow")
        src = sf.get("sourceRef")
        tgt = sf.get("targetRef")
        if not src or src not in element_ids:
            unresolved_endpoints.append(f"{sf_id}: sourceRef '{src}' not found in process elements")
        if not tgt or tgt not in element_ids:
            unresolved_endpoints.append(f"{sf_id}: targetRef '{tgt}' not found in process elements")

    if unresolved_endpoints:
        result["unresolved_sequence_endpoints"] = unresolved_endpoints
        result["errors"].append(f"Unresolved sequence flow endpoints: {unresolved_endpoints}")
        result["is_valid"] = False

    # 7. Check for illegal sequence flows connected to event sub-processes
    event_subproc_ids = {
        e.get("id") for e in root.iter()
        if e.tag.endswith("subProcess") and (
            e.get("triggeredByEvent") == "true" or
            e.get("{http:///com.sap.ifl.model/Ifl.xsd}type") == "ErrorEventSubProcessTemplate"
        )
    }
    for sf in seq_flows:
        if sf.get("sourceRef") in event_subproc_ids or sf.get("targetRef") in event_subproc_ids:
            result["errors"].append(
                f"Illegal sequence flow '{sf.get('id')}' connected to event sub-process "
                f"('{sf.get('sourceRef')}' -> '{sf.get('targetRef')}'). Event sub-processes cannot have incoming or outgoing sequence flows."
            )
            result["is_valid"] = False

    # 8. Check for illegal message flows targeted at timer start events
    timer_start_ids = set()
    for se in root.iter():
        if se.tag.endswith("startEvent"):
            if any(child.tag.endswith("timerEventDefinition") for child in se):
                se_id = se.get("id")
                if se_id:
                    timer_start_ids.add(se_id)
    msg_flows = [e for e in root.iter() if e.tag.endswith("messageFlow")]
    for mf in msg_flows:
        if mf.get("targetRef") in timer_start_ids:
            result["errors"].append(
                f"Illegal message flow '{mf.get('id')}' targeted at timer start event '{mf.get('targetRef')}'. "
                "Timer start events cannot receive message flows."
            )
            result["is_valid"] = False

    return result


def validate_individual_iflow_zip(zf: zipfile.ZipFile, context_name: str = "iFlow") -> dict[str, Any]:
    """Validates an individual Integration Flow archive."""
    report: dict[str, Any] = {
        "type": "individual_iflow",
        "context_name": context_name,
        "is_valid": True,
        "errors": [],
        "warnings": [],
        "entries": sorted(zf.namelist()),
        "iflow_files": [],
        "scripts": [],
        "manifest_info": {},
    }

    namelist = zf.namelist()

    # Required files in individual iflow
    has_manifest = "META-INF/MANIFEST.MF" in namelist
    has_metainfo = "metainfo.prop" in namelist or "project.properties" in namelist

    if not has_manifest:
        report["errors"].append("Missing required 'META-INF/MANIFEST.MF'.")
        report["is_valid"] = False

    # Check for outdated folder
    if any("scenarioflows/integrationscenarioflows/" in n for n in namelist):
        report["errors"].append(
            "Found deprecated directory 'scenarioflows/integrationscenarioflows/'. "
            "Must be 'scenarioflows/integrationflow/'."
        )
        report["is_valid"] = False

    # Check for correct scenarioflows path
    iflow_entries = [n for n in namelist if n.endswith(".iflw")]
    if not iflow_entries:
        report["errors"].append("No .iflw flow models found in archive.")
        report["is_valid"] = False
    else:
        for iflow_path in iflow_entries:
            if not iflow_path.startswith("src/main/resources/scenarioflows/integrationflow/"):
                report["errors"].append(
                    f".iflw file at invalid path: '{iflow_path}'. Expected under 'src/main/resources/scenarioflows/integrationflow/'."
                )
                report["is_valid"] = False

            # Validate XML inside
            xml_bytes = zf.read(iflow_path)
            xml_report = validate_iflow_xml_content(xml_bytes, iflow_path)
            report["iflow_files"].append(xml_report)
            if not xml_report["is_valid"]:
                report["is_valid"] = False
                report["errors"].extend([f"{iflow_path}: {e}" for e in xml_report["errors"]])

    # Collect scripts
    script_entries = [n for n in namelist if n.startswith("src/main/resources/script/")]
    report["scripts"] = script_entries

    # Parse and validate MANIFEST.MF
    if has_manifest:
        mf_raw = zf.read("META-INF/MANIFEST.MF")
        mf_text = mf_raw.decode("utf-8", errors="ignore")

        # 1. Line length check (RFC 2822 / Jar Manifest max 72 bytes per line)
        raw_lines = mf_raw.split(b"\r\n")
        if b"\r\n" not in mf_raw and b"\n" in mf_raw:
            raw_lines = mf_raw.split(b"\n")
            report["warnings"].append("MANIFEST.MF uses LF line endings instead of standard RFC 2822 CRLF.")

        for l_idx, r_line in enumerate(raw_lines, 1):
            if l_idx == len(raw_lines) and r_line == b"":
                continue
            if len(r_line) > 72:
                report["errors"].append(
                    f"MANIFEST.MF line {l_idx} exceeds 72 bytes ({len(r_line)} bytes): {r_line[:40].decode('utf-8', errors='ignore')}..."
                )
                report["is_valid"] = False

        # 2. Header unfolding (continuation lines begin with space/tab)
        unfolded_lines: list[str] = []
        for line in mf_text.splitlines():
            if (line.startswith(" ") or line.startswith("\t")) and unfolded_lines:
                unfolded_lines[-1] += line[1:]
            else:
                unfolded_lines.append(line)

        mf_dict: dict[str, str] = {}
        for line in unfolded_lines:
            if ":" in line:
                k, v = line.split(":", 1)
                mf_dict[k.strip()] = v.strip()
        report["manifest_info"] = mf_dict

        # 3. Required OSGi headers
        for req in ("Manifest-Version", "Bundle-ManifestVersion", "Bundle-Name", "Bundle-SymbolicName", "Import-Package"):
            if req not in mf_dict:
                report["warnings"].append(f"MANIFEST.MF missing recommended OSGi header '{req}'.")

    return report


def validate_package(
    target_source: str | Path | bytes,
    reference_source: str | Path | bytes | None = None,
) -> dict[str, Any]:
    """
    Validates a generated SAP CPI Package against SAP Integration Suite requirements
    and optionally compares it with a reference archive.
    """
    target_zf = _open_zip(target_source)
    namelist = target_zf.namelist()

    report: dict[str, Any] = {
        "status": "PASSED",
        "archive_type": "unknown",
        "errors": [],
        "warnings": [],
        "outer_entries": sorted(namelist),
        "required_files": {},
        "metadata": {},
        "nested_artifacts": {},
        "reference_diff": None,
    }

    # Detect archive type
    is_package = any(n.endswith("_content") or n == "resources.cnt" for n in namelist)
    is_individual = "META-INF/MANIFEST.MF" in namelist and any(n.endswith(".iflw") for n in namelist)

    if not is_package and is_individual:
        report["archive_type"] = "individual_iflow"
        iflow_rep = validate_individual_iflow_zip(target_zf, "target")
        report["nested_artifacts"]["individual_iflow"] = iflow_rep
        if not iflow_rep["is_valid"]:
            report["status"] = "FAILED"
            report["errors"].extend(iflow_rep["errors"])
        report["warnings"].extend(iflow_rep["warnings"])
        report["import_guaranteed"] = (report["status"] == "PASSED")
        report["import_verification"] = "import-verified" if report["import_guaranteed"] else "failed-validation"
        report["delivery_recommendation"] = (
            "Upload into an existing package via Design -> Integrations and APIs -> [Package] -> "
            "Artifacts -> Edit -> Add -> Integration Flow -> Upload, or deploy programmatically via OData API."
        )
        return report

    report["archive_type"] = "content_package"
    report["import_verification"] = "not import-verified"
    report["import_guaranteed"] = False
    report["import_guarantee_message"] = (
        "Package-ZIP output is not import-verified. SAP Integration Suite uses proprietary HashVersion 2.0.0; "
        "import may fail in the UI with 'Select a valid content package'. For reliable delivery, use the OData design-time "
        "API (cpi_api_client.py) or upload individual iFlow archives directly."
    )
    report["delivery_recommendation"] = (
        "Make the OData design-time API (cpi_api_client.py) the primary delivery path, "
        "or upload individual iFlow archives into a package created in the SAP Integration Suite Web UI."
    )

    # Required outer entries
    required_outer = [
        "resources.cnt",
        "contentmetadata.md",
        "hash",
        "ExportInformation.info",
    ]
    for req in required_outer:
        exists = req in namelist
        report["required_files"][req] = "present" if exists else "missing"
        if not exists:
            report["errors"].append(f"Missing mandatory outer package file: '{req}'")
            report["status"] = "FAILED"

    # Verify at least one nested _content ZIP exists
    content_entries = [n for n in namelist if n.endswith("_content")]
    if not content_entries:
        report["errors"].append("No nested artifact ZIPs ('{artifact_id}_content') found in package.")
        report["status"] = "FAILED"
    else:
        report["required_files"]["nested_content_zips"] = f"{len(content_entries)} found"

    # Parse and validate resources.cnt
    if "resources.cnt" in namelist:
        try:
            cnt_raw = target_zf.read("resources.cnt")
            cnt_json = base64.b64decode(cnt_raw).decode("utf-8")
            cnt_data = json.loads(cnt_json)
            report["metadata"]["resources.cnt"] = {
                "parsed_successfully": True,
                "resources_count": len(cnt_data.get("resources", [])),
                "relations_count": len(cnt_data.get("relations", [])),
            }

            # Check for ContentPackage and IFlow resources
            types = {r.get("resourceType") for r in cnt_data.get("resources", [])}
            if "ContentPackage" not in types:
                report["errors"].append("resources.cnt missing resource of type 'ContentPackage'.")
                report["status"] = "FAILED"
            if "IFlow" not in types:
                report["errors"].append("resources.cnt missing resource of type 'IFlow'.")
                report["status"] = "FAILED"

            # Check relations
            relations = cnt_data.get("relations", [])
            if not relations:
                report["warnings"].append("resources.cnt has empty 'relations' list.")

            # Check masterId prefix semantics
            pkg_res = next((r for r in cnt_data.get("resources", []) if r.get("resourceType") == "ContentPackage"), None)
            if pkg_res:
                pkg_id = pkg_res.get("id", "")
                pkg_mid = pkg_res.get("masterId", "")
                mid_prefix = pkg_mid.split(":")[0] if ":" in pkg_mid else ""
                if mid_prefix and mid_prefix == pkg_id:
                    report["warnings"].append(f"ContentPackage masterId prefix '{mid_prefix}' matches package id. Native SAP uses a distinct container prefix.")

                pkg_name = pkg_res.get("name", "")
                if " " in pkg_name or not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", pkg_name):
                    report["errors"].append(
                        f"ContentPackage 'name' must be a valid SAP technical identifier without spaces (alphanumeric/underscore). Found: '{pkg_name}'"
                    )
                    report["status"] = "FAILED"

            # Check uniqueId and name uniqueness across resources
            seen_uids: set[str] = set()
            seen_rnames: set[str] = set()
            for r in cnt_data.get("resources", []):
                uid = r.get("uniqueId")
                if uid:
                    if uid in seen_uids:
                        report["errors"].append(f"Duplicate uniqueId '{uid}' found in resources.cnt.")
                        report["status"] = "FAILED"
                    seen_uids.add(uid)

                rname = r.get("name")
                if rname:
                    if rname in seen_rnames:
                        report["errors"].append(f"Duplicate resource name '{rname}' found in resources.cnt.")
                        report["status"] = "FAILED"
                    seen_rnames.add(rname)

            # Check that non-flow files are not listed as IFlow artifacts
            for r in cnt_data.get("resources", []):
                if r.get("resourceType") == "IFlow":
                    rname = (r.get("name") or "").lower()
                    for bad in ("pom.zip", "log4j2", "application-types", "application_types", "mule-artifact", "global_config.zip"):
                        if bad in rname:
                            report["warnings"].append(f"Non-flow artifact '{r.get('name')}' is classified as an IFlow in resources.cnt.")

            # Check resource schema details and payload existence
            res_ids = {r.get("id") for r in cnt_data.get("resources", [])}
            for r in cnt_data.get("resources", []):
                r_type = r.get("resourceType")
                r_id = r.get("id")

                if r_type == "IFlow":
                    # Check contentType: application/x-zip-compressed expected by SAP
                    ct = r.get("contentType")
                    if ct == "application/octet-stream":
                        report["warnings"].append(
                            f"IFlow '{r_id}' contentType is 'application/octet-stream'. Native SAP Integration Suite prefers 'application/x-zip-compressed'."
                        )

                    # Check that payload entry exists in outer archive
                    payload_name = f"{r_id}_content"
                    if payload_name not in namelist:
                        report["errors"].append(
                            f"IFlow resource '{r_id}' declared in resources.cnt has no corresponding payload '{payload_name}' in outer ZIP."
                        )
                        report["status"] = "FAILED"

                    # Check scope: EXTERNAL expected by SAP on IFlow
                    if r.get("scope") != "EXTERNAL":
                        report["warnings"].append(f"IFlow '{r_id}' missing or non-standard 'scope'. Native SAP Integration Suite uses scope='EXTERNAL'.")

                    # Check isInternal: should be omitted on IFlow
                    if "isInternal" in r:
                        report["warnings"].append(f"IFlow '{r_id}' contains deprecated/extraneous 'isInternal' field.")

                elif r_type == "ContentPackage":
                    # ContentPackage is a container; scope must NOT be EXTERNAL
                    if r.get("scope") == "EXTERNAL":
                        report["errors"].append(
                            "ContentPackage resource declared 'scope: EXTERNAL'. In SAP CPI, ContentPackage must not be marked EXTERNAL or the package import will be rejected with 'Select a valid content package to continue'."
                        )
                        report["status"] = "FAILED"

            # Check relationship closure
            for rel in relations:
                src = rel.get("sourceId")
                tgt = rel.get("targetId")
                if src and src not in res_ids:
                    report["errors"].append(f"Relation references non-existent sourceId '{src}'.")
                    report["status"] = "FAILED"
                if tgt and tgt not in res_ids:
                    report["errors"].append(f"Relation references non-existent targetId '{tgt}'.")
                    report["status"] = "FAILED"

        except Exception as e:
            report["metadata"]["resources.cnt"] = {"parsed_successfully": False, "error": str(e)}
            report["errors"].append(f"Failed to parse resources.cnt: {e}")
            report["status"] = "FAILED"

    # Parse contentmetadata.md
    if "contentmetadata.md" in namelist:
        try:
            md_raw = target_zf.read("contentmetadata.md")
            md_text = base64.b64decode(md_raw).decode("utf-8")
            report["metadata"]["contentmetadata.md"] = {
                "parsed_successfully": True,
                "properties": [line.strip() for line in md_text.splitlines() if line.strip() and not line.startswith("#")],
            }
        except Exception as e:
            report["metadata"]["contentmetadata.md"] = {"parsed_successfully": False, "error": str(e)}
            report["errors"].append(f"Failed to parse contentmetadata.md: {e}")
            report["status"] = "FAILED"

    # Parse hash
    if "hash" in namelist:
        try:
            hash_raw = target_zf.read("hash")
            hash_data = json.loads(hash_raw)
            if not isinstance(hash_data, list) or len(hash_data) == 0:
                report["errors"].append("'hash' file must contain a non-empty JSON list of hashes.")
                report["status"] = "FAILED"
            else:
                is_valid_hex = all(
                    isinstance(h, str) and len(h) == 64 and bool(re.match(r"^[0-9a-fA-F]+$", h))
                    for h in hash_data
                )
                report["metadata"]["hash"] = {
                    "hashes_count": len(hash_data),
                    "valid_hex_format": is_valid_hex,
                    "verified": False,
                    "verification_status": "cannot be verified; SAP algorithm unknown",
                }
                report["warnings"].append(
                    "Package hash cannot be verified; SAP algorithm unknown (HashVersion 2.0.0 uses a proprietary/keyed scheme). "
                    "Package-ZIP output is not import-guaranteed in SAP Integration Suite UI. "
                    "Use the OData design-time API (cpi_api_client.py) or upload individual iFlow archives directly into a UI-created package."
                )
        except Exception as e:
            report["metadata"]["hash"] = {"parsed_successfully": False, "error": str(e)}
            report["errors"].append(f"Failed to parse hash: {e}")
            report["status"] = "FAILED"

    # Parse ExportInformation.info
    if "ExportInformation.info" in namelist:
        try:
            info_raw = target_zf.read("ExportInformation.info").decode("utf-8")
            info_dict = {}
            for line in info_raw.splitlines():
                if "=" in line:
                    k, v = line.split("=", 1)
                    info_dict[k.strip()] = v.strip()
            report["metadata"]["ExportInformation.info"] = info_dict
            if "Name" not in info_dict:
                report["warnings"].append("ExportInformation.info missing 'Name' property.")
        except Exception as e:
            report["metadata"]["ExportInformation.info"] = {"error": str(e)}

    # Validate each nested _content ZIP
    seen_bsns: dict[str, str] = {}
    for content_name in content_entries:
        try:
            inner_bytes = target_zf.read(content_name)
            inner_zf = zipfile.ZipFile(io.BytesIO(inner_bytes), mode="r")
            nested_rep = validate_individual_iflow_zip(inner_zf, context_name=content_name)

            # Check Bundle-SymbolicName uniqueness across inner artifacts
            bsn_raw = nested_rep.get("manifest_info", {}).get("Bundle-SymbolicName", "")
            bsn = bsn_raw.split(";")[0].strip() if bsn_raw else ""
            if bsn:
                if bsn in seen_bsns:
                    report["errors"].append(
                        f"Duplicate OSGi Bundle-SymbolicName '{bsn}' in '{content_name}' (conflicts with '{seen_bsns[bsn]}'). "
                        "Every artifact in a package must have a globally unique Bundle-SymbolicName."
                    )
                    report["status"] = "FAILED"
                else:
                    seen_bsns[bsn] = content_name

            # Check for nested malformed paths (e.g. src/.../src/...)
            inner_names = inner_zf.namelist()
            for iname in inner_names:
                if iname.count("src/main/resources/") > 1 or iname.count("src/") > 1:
                    report["errors"].append(f"Nested/malformed path '{iname}' in inner archive '{content_name}'.")
                    report["status"] = "FAILED"

            # Check for inner bundle pollution (metainfo.prop or project.properties inside content package bundle)
            if "metainfo.prop" in inner_names or "project.properties" in inner_names:
                nested_rep["warnings"].append("Inner bundle contains metainfo.prop / project.properties (native SAP omits these from package content bundles).")

            # Check for script pollution
            iflow_files = [n for n in inner_names if n.endswith(".iflw")]
            scripts = [n for n in inner_names if n.startswith("src/main/resources/script/")]
            if iflow_files and scripts:
                iflow_xml = inner_zf.read(iflow_files[0]).decode("utf-8", errors="ignore")
                for s in scripts:
                    s_name = Path(s).name
                    if s_name not in iflow_xml and not any(part in s_name.lower() for part in Path(iflow_files[0]).stem.lower().split("_")):
                        nested_rep["warnings"].append(f"Script '{s_name}' is packaged in '{content_name}' but not referenced in '{iflow_files[0]}'.")

            report["nested_artifacts"][content_name] = nested_rep
            if not nested_rep["is_valid"]:
                report["status"] = "FAILED"
                report["errors"].extend([f"{content_name} -> {err}" for err in nested_rep["errors"]])
            report["warnings"].extend([f"{content_name} -> {w}" for w in nested_rep["warnings"]])
        except Exception as e:
            report["errors"].append(f"Failed to read nested artifact '{content_name}': {e}")
            report["status"] = "FAILED"

    # Compare with reference archive if provided
    if reference_source is not None:
        try:
            ref_zf = _open_zip(reference_source)
            ref_namelist = sorted(ref_zf.namelist())
            missing_in_target = [entry for entry in ref_namelist if not any(
                entry == e or (entry.endswith("_content") and e.endswith("_content")) for e in namelist
            )]
            extra_in_target = [entry for entry in namelist if not any(
                entry == e or (entry.endswith("_content") and e.endswith("_content")) for e in ref_namelist
            )]

            report["reference_diff"] = {
                "reference_entries": ref_namelist,
                "missing_structural_files": missing_in_target,
                "extra_files": extra_in_target,
                "matches_reference_contract": len(missing_in_target) == 0,
            }
            if missing_in_target:
                report["warnings"].append(f"Structural difference from reference: missing entries {missing_in_target}")
        except Exception as e:
            report["reference_diff"] = {"error": str(e)}

    return report


def compare_packages(
    target_source: str | Path | bytes,
    reference_source: str | Path | bytes,
) -> dict[str, Any]:
    """Compares a target package against a known-good reference package."""
    report = validate_package(target_source, reference_source=reference_source)
    return report.get("reference_diff") or {}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="SAP Integration Suite / CPI Package & Artifact Validation Utility",
    )
    parser.add_argument(
        "--target-package",
        "-t",
        required=True,
        help="Path to generated or downloaded SAP CPI ZIP package",
    )
    parser.add_argument(
        "--reference-package",
        "-r",
        default=None,
        help="Optional path to known-good reference SAP package for comparison",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )

    args = parser.parse_args()

    if not os.path.exists(args.target_package):
        print(f"Error: Target package file not found: {args.target_package}", file=sys.stderr)
        sys.exit(1)

    if args.reference_package and not os.path.exists(args.reference_package):
        print(f"Warning: Reference package file not found: {args.reference_package}", file=sys.stderr)
        args.reference_package = None

    report = validate_package(args.target_package, reference_source=args.reference_package)

    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        print("=================================================================")
        print(f"SAP CPI Package Diagnostic Report: {report['status']}")
        print(f"Archive Type: {report['archive_type']}")
        guarantee_text = "GUARANTEED (No package hash checks on individual uploads)" if report.get("import_guaranteed") else "NOT IMPORT-VERIFIED (Proprietary HashVersion 2.0.0; use OData API or individual upload)"
        print(f"Import Verification: {report.get('import_verification', 'not import-verified').upper()} ({guarantee_text})")
        if report.get("delivery_recommendation"):
            print(f"Recommendation:      {report['delivery_recommendation']}")
        print("=================================================================")
        print("\nOuter Entries:")
        for e in report["outer_entries"]:
            print(f"  - {e}")

        print("\nRequired Files:")
        for k, v in report.get("required_files", {}).items():
            print(f"  - {k}: {v}")

        if report.get("errors"):
            print("\nErrors:")
            for err in report["errors"]:
                print(f"  [ERROR] {err}")

        if report.get("warnings"):
            print("\nWarnings:")
            for w in report["warnings"]:
                print(f"  [WARNING] {w}")

        if report.get("reference_diff"):
            diff = report["reference_diff"]
            print("\nReference Comparison:")
            print(f"  Matches reference contract: {diff.get('matches_reference_contract')}")
            if diff.get("missing_structural_files"):
                print(f"  Missing files compared to reference: {diff.get('missing_structural_files')}")

        print("\nNested Artifacts:")
        for name, art in report.get("nested_artifacts", {}).items():
            print(f"  Artifact '{name}': valid={art.get('is_valid')}")
            for iflow in art.get("iflow_files", []):
                print(f"    Flow '{iflow.get('filename')}': valid={iflow.get('is_valid')}, elements={len(iflow.get('process_elements', []))}, sequence_flows={iflow.get('sequence_flows_count', 0)}")

    if report["status"] != "PASSED":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
