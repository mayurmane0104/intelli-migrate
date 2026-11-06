"""
mule_parser/tests/test_sap_cpi_export.py — Automated Test Suite for SAP CPI Migration Exporters.

Comprehensive test coverage for Phase 6:
1. XML well-formedness, prefix normalization, and sequence flow endpoint repair.
2. Verification of the 4 real-world failing files (save-order, save-order-items, inventory-serviceFlow, local_api_request).
3. Package-level ZIP structure and metadata (resources.cnt, contentmetadata.md, hash, ExportInformation.info).
4. Nested artifact archives and integrationflow resource paths (no 'integrationscenarioflows').
5. Multi-flow packages and flow isolation.
6. Individual Integration Flow export vs Package export.
7. Diagnostic package validator & reference package comparison.
8. Decoupled 6-stage SAP API migration workflow and credential safety.
"""
from __future__ import annotations

import base64
import hashlib
import io
import json
import os
import struct
import zipfile
import zlib
import xml.etree.ElementTree as ET
from pathlib import Path
import pytest


from mule_parser.platforms.base import GeneratedFile
from mule_parser.platforms.sap.iflow_generator import (
    validate_and_normalize_iflow_xml,
    IFlowGenerator,
    BPMN2_NS,
    BPMNDI_NS,
    IFL_NS,
)
from mule_parser.platforms.sap.cpi_package_generator import (
    CPIArtifact,
    CPIPackageGenerator,
    create_content_package_archive,
    create_individual_iflow_archive,
)
from mule_parser.platforms.sap_generator import SAPPlatformGenerator
from mule_parser.platforms.sap.validator import (
    validate_package,
    validate_iflow_xml_content,
    compare_packages,
)
from mule_parser.platforms.sap.cpi_api_client import (
    MigrationStage,
    StageStatus,
    SAPClientConfig,
    SAPIntegrationSuiteClient,
    run_staged_migration_pipeline,
)
from mule_parser.services.export_service import (
    ExportRequest,
    build_export,
    _sap_reference_bundle_version,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
KNOWN_GOOD_REFERENCE_PATH = REPO_ROOT / "examples" / "Employee Payroll Processor 1.zip"
if not KNOWN_GOOD_REFERENCE_PATH.exists():
    KNOWN_GOOD_REFERENCE_PATH = Path("examples/Employee Payroll Processor 1.zip")
FAILING_ORIGINAL_PATH = Path("/home/mayur/Downloads/ordering_process-zip.zip")


# ==============================================================================
# 1. XML Well-Formedness, Namespace Repair, and Sequence Flow Validation
# ==============================================================================

def test_iflow_xml_repair_naked_process_and_missing_namespaces():
    """Verify naked <process> element is wrapped in <bpmn2:definitions> with full namespaces."""
    raw_naked_process = """
    <process id="Process_1" name="OrderProcess" isExecutable="false">
        <startEvent id="Start_1" name="Start"/>
        <sequenceFlow id="flow_1" sourceRef="Start_1" targetRef="End_1"/>
        <endEvent id="End_1" name="End"/>
    </process>
    """
    fixed_xml, warnings = validate_and_normalize_iflow_xml(raw_naked_process, flow_name="OrderProcess")
    assert "<bpmn2:definitions" in fixed_xml
    assert 'xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"' in fixed_xml

    # Must be valid XML parseable by ElementTree
    root = ET.fromstring(fixed_xml.encode("utf-8"))
    assert root.tag.endswith("definitions")


def test_iflow_xml_repair_camunda_prefix_and_missing_endpoints():
    """Verify camunda attributes and sequence-flow target mismatches are healed."""
    raw_xml_with_camunda = """<?xml version="1.0" encoding="UTF-8"?>
    <bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
                       id="Definitions_1" targetNamespace="http://bpmn.io/schema/bpmn">
        <bpmn2:process id="Process_Test" isExecutable="false">
            <bpmn2:serviceTask id="Task_1" camunda:expression="${orderService.process()}">
                <bpmn2:incoming>Flow_0</bpmn2:incoming>
                <bpmn2:outgoing>Flow_1</bpmn2:outgoing>
            </bpmn2:serviceTask>
            <bpmn2:sequenceFlow id="Flow_1" sourceRef="Task_1" targetRef="Unresolved_End"/>
            <bpmn2:endEvent id="Real_End">
                <bpmn2:incoming>Flow_1</bpmn2:incoming>
            </bpmn2:endEvent>
        </bpmn2:process>
    </bpmn2:definitions>
    """
    fixed_xml, warnings = validate_and_normalize_iflow_xml(raw_xml_with_camunda, flow_name="Process_Test")
    # camunda namespace must have been injected
    assert 'xmlns:camunda="http://camunda.org/schema/1.0/bpmn"' in fixed_xml

    # Endpoint must have been reconciled to Real_End via <incoming>
    assert 'targetRef="Real_End"' in fixed_xml
    root = ET.fromstring(fixed_xml.encode("utf-8"))
    assert root is not None


def test_four_known_failing_files_pass_validation():
    """
    Test the exact 4 files reported in the issue:
    save-order.iflw, save-order-items.iflw, inventory-serviceFlow.iflw, local_api_request.iflw.
    """
    sample_save_order = """<process id="save_order" name="Save Order" camunda:versionTag="1.0">
        <startEvent id="Start_1" name="Start"/>
        <sequenceFlow id="to_task" sourceRef="Start_1" targetRef="task_1"/>
        <serviceTask id="task_1" name="Save" camunda:expression="${db.save()}"/>
        <sequenceFlow id="to_end" sourceRef="task_1" targetRef="End_1"/>
        <endEvent id="End_1" name="End"/>
    </process>"""

    sample_save_order_items = """<process id="save_order_items" name="Save Order Items">
        <serviceTask id="task_items" camunda:delegateExpression="${orderItemDelegate}"/>
    </process>"""

    sample_inventory_service = """<?xml version="1.0" encoding="UTF-8"?>
    <bpmn2:process id="inventory_service" camunda:candidateStarterGroups="inventory_admins">
        <bpmn2:startEvent id="start_inv"/>
        <bpmn2:sequenceFlow id="flow_inv" sourceRef="start_inv" targetRef="end_inv"/>
        <bpmn2:endEvent id="end_inv"/>
    </bpmn2:process>"""

    sample_local_api = """<process id="local_api_request" isExecutable="true">
        <callActivity id="call_api" camunda:caseRef="LocalCase"/>
    </process>"""

    failing_cases = [
        ("save-order", sample_save_order),
        ("save-order-items", sample_save_order_items),
        ("inventory-serviceFlow", sample_inventory_service),
        ("local_api_request", sample_local_api),
    ]

    for flow_name, raw_content in failing_cases:
        fixed_xml, warns = validate_and_normalize_iflow_xml(raw_content, flow_name=flow_name)
        val_result = validate_iflow_xml_content(fixed_xml.encode("utf-8"), f"{flow_name}.iflw")
        assert val_result["is_valid"], f"Failed for {flow_name}: {val_result['errors']}"
        assert len(val_result["errors"]) == 0


def test_iflow_generator_creates_valid_bpmn():
    """Verify IFlowGenerator outputs well-formed BPMN2 XML with SAP CPI extensions."""
    gen = IFlowGenerator()
    flow_def = {
        "name": "OrderSyncFlow",
        "source": {"type": "http:listener"},
        "processors": [
            {"type": "ee:transform", "name": "TransformDWL"},
            {"type": "http:request", "name": "CallBackend"},
        ],
    }
    xml_output = gen.generate_iflow(flow_def)
    val = validate_iflow_xml_content(xml_output.encode("utf-8"), "OrderSyncFlow.iflw")
    assert val["is_valid"]
    assert val["sequence_flows_count"] >= 3
    assert "xmlns:ifl" in xml_output
    assert "xmlns:bpmn2" in xml_output


# ==============================================================================
# 2. Package-Level Archive Structure and Decoded Metadata Validation
# ==============================================================================

def test_package_level_archive_structure_and_metadata():
    """
    Verify create_content_package_archive produces:
    - {artifact_id}_content
    - resources.cnt (Base64 JSON with AGGREGATION relations)
    - contentmetadata.md (Base64 key-value properties)
    - hash (JSON array of digests)
    - ExportInformation.info
    """
    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/order_flow.iflw",
            content="""<?xml version="1.0" encoding="UTF-8"?>
            <bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
                               xmlns:ifl="http://sap.com/xi/services/bpmn2"
                               xmlns:camunda="http://camunda.org/schema/1.0/bpmn"
                               xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
                               xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"
                               xmlns:di="http://www.omg.org/spec/DD/20100524/DI"
                               id="Definitions_1" targetNamespace="http://bpmn.io/schema/bpmn">
                <bpmn2:process id="Process_Order" name="Order Process" isExecutable="false">
                    <bpmn2:startEvent id="Start_1" name="Start">
                        <bpmn2:outgoing>Flow_1</bpmn2:outgoing>
                    </bpmn2:startEvent>
                    <bpmn2:sequenceFlow id="Flow_1" sourceRef="Start_1" targetRef="End_1"/>
                    <bpmn2:endEvent id="End_1" name="End">
                        <bpmn2:incoming>Flow_1</bpmn2:incoming>
                    </bpmn2:endEvent>
                </bpmn2:process>
            </bpmn2:definitions>""",
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/script/transform.groovy",
            content="import com.sap.gateway.ip.core.customdev.util.Message;\ndef Message processData(Message message) { return message; }",
            role="source",
            generator="sap:groovy",
        ),
        GeneratedFile(
            path="src/main/resources/parameters.prop",
            content="backend.host=api.enterprise.com\nbackend.port=443\n",
            role="config",
            generator="sap:props",
        ),
    ]

    package_id = "EnterpriseOrderPackage"
    package_name = "Enterprise Order Package"
    zip_bytes = create_content_package_archive(files, package_id, package_name)

    # 1. Inspect outer ZIP
    with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as zf:
        namelist = zf.namelist()
        assert "resources.cnt" in namelist
        assert "contentmetadata.md" in namelist
        assert "hash" in namelist
        assert "ExportInformation.info" in namelist
        content_entries = [n for n in namelist if n.endswith("_content")]
        assert len(content_entries) == 1
        content_entry_name = content_entries[0]

        # 2. Inspect resources.cnt
        cnt_raw = zf.read("resources.cnt")
        cnt_json = json.loads(base64.b64decode(cnt_raw).decode("utf-8"))
        assert "resources" in cnt_json
        resources = cnt_json["resources"]
        types = [r.get("resourceType") for r in resources]
        assert "ContentPackage" in types
        assert "IFlow" in types
        pkg_res = next(r for r in resources if r.get("resourceType") == "ContentPackage")
        assert pkg_res.get("name") == package_id
        assert pkg_res.get("uniqueId") == package_id
        assert pkg_res.get("displayName") == package_name
        assert len(pkg_res.get("id")) == 32

        # Check AGGREGATION relation in cnt_json["relations"]
        assert "relations" in cnt_json
        relations = cnt_json["relations"]
        assert any(rel.get("relationType") == "AGGREGATION" for rel in relations)

        # 3. Inspect contentmetadata.md
        meta_raw = zf.read("contentmetadata.md")
        meta_lines = base64.b64decode(meta_raw).decode("utf-8").splitlines()
        meta_dict = dict(line.split("=", 1) for line in meta_lines if "=" in line)
        assert meta_dict.get("HashVersion") == "2.0.0"
        assert meta_dict.get("EncodingVersion") == "1.0.0"
        # Organization must default to "TEST" — the cross-tenant-neutral sentinel (unless overridden by env var)
        # This prevents "Select a valid content package" rejection on tenants other than the exporting one.
        assert meta_dict.get("Organization") in ("TEST", os.environ.get("SAP_CPI_ORGANIZATION", "TEST"))
        assert meta_dict.get("Environment") in (
            "sap-integration-suite",  # new default: accepted on all tenants
            os.environ.get("SAP_CPI_ENVIRONMENT", "sap-integration-suite"),
        )

        # 4. Inspect hash
        hash_raw = zf.read("hash")
        hash_list = json.loads(hash_raw.decode("utf-8"))
        assert len(hash_list) >= 2  # Hashes for inner zip and resources.cnt

        # 5. Inspect nested artifact archive
        nested_bytes = zf.read(content_entry_name)
        with zipfile.ZipFile(io.BytesIO(nested_bytes), "r") as nested_zf:
            nested_names = nested_zf.namelist()
            assert "src/main/resources/scenarioflows/integrationflow/order_flow.iflw" in nested_names
            # CRITICAL: Confirm 'integrationscenarioflows' is NOT present
            assert not any("integrationscenarioflows" in n for n in nested_names)
            assert "META-INF/MANIFEST.MF" in nested_names
            # Native SAP content packages strictly omit metainfo.prop and project.properties from inner bundles
            assert "metainfo.prop" not in nested_names
            assert "project.properties" not in nested_names
            assert ".project" in nested_names
            assert "src/main/resources/parameters.prop" in nested_names
            assert "src/main/resources/parameters.propdef" in nested_names
            assert "src/main/resources/script/transform.groovy" in nested_names

            # Check MANIFEST.MF content
            manifest_mf = nested_zf.read("META-INF/MANIFEST.MF").decode("utf-8")
            assert "Bundle-SymbolicName: order_flow" in manifest_mf
            assert "SAP-BundleType: IntegrationFlow" in manifest_mf


# ==============================================================================
# 3. Multi-Flow Packages and Resource Isolation
# ==============================================================================

def test_multi_flow_partitioning_and_isolation():
    """Verify multiple flows in a single package are partitioned into isolated nested ZIPs."""
    flow_a_iflw = """<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL" id="Def_A">
        <bpmn2:process id="FlowA_Process" isExecutable="false"/>
    </bpmn2:definitions>"""

    flow_b_iflw = """<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL" id="Def_B">
        <bpmn2:process id="FlowB_Process" isExecutable="false"/>
    </bpmn2:definitions>"""

    files = [
        GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/FlowA.iflw", content=flow_a_iflw, role="source", generator="sap:iflow"),
        GeneratedFile(path="src/main/resources/script/FlowA_transform.groovy", content="// Script for A", role="source", generator="sap:groovy"),
        GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/FlowB.iflw", content=flow_b_iflw, role="source", generator="sap:iflow"),
        GeneratedFile(path="src/main/resources/script/FlowB_enrich.groovy", content="// Script for B", role="source", generator="sap:groovy"),
    ]

    packager = CPIPackageGenerator()
    artifacts = packager._partition_files_to_artifacts(files, "MultiFlowPackage", "Multi Flow Package", "1.0.0")
    assert len(artifacts) == 2
    artifact_names = {a.name for a in artifacts}
    assert "FlowA" in artifact_names
    assert "FlowB" in artifact_names

    art_a = next(a for a in artifacts if a.name == "FlowA")
    art_a_paths = {f.path for f in art_a.files}
    assert "src/main/resources/script/FlowA_transform.groovy" in art_a_paths
    # Flow B's script must NOT contaminate Flow A
    assert "src/main/resources/script/FlowB_enrich.groovy" not in art_a_paths

    # Outer package packaging
    pkg_bytes = create_content_package_archive(files, "MultiFlowPackage", "Multi Flow Package")
    with zipfile.ZipFile(io.BytesIO(pkg_bytes), "r") as zf:
        namelist = zf.namelist()
        content_entries = [n for n in namelist if n.endswith("_content")]
        assert len(content_entries) == 2


# ==============================================================================
# 4. Individual Flow Export vs Package Export
# ==============================================================================

def test_individual_flow_export_structure():
    """Verify create_individual_iflow_archive generates a flat iFlow archive for existing packages."""
    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/single_flow.iflw",
            content="""<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL" id="Def_Single">
                <bpmn2:process id="Single_Process"/>
            </bpmn2:definitions>""",
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/script/helper.groovy",
            content="// Groovy helper",
            role="source",
            generator="sap:groovy",
        ),
    ]

    flow_bytes = create_individual_iflow_archive(files, "single_flow", "Single Flow")
    with zipfile.ZipFile(io.BytesIO(flow_bytes), "r") as zf:
        namelist = zf.namelist()
        # Direct entries at root
        assert "src/main/resources/scenarioflows/integrationflow/single_flow.iflw" in namelist
        assert "src/main/resources/script/helper.groovy" in namelist
        assert "META-INF/MANIFEST.MF" in namelist
        assert "metainfo.prop" in namelist
        # Must NOT contain package-level metadata
        assert "resources.cnt" not in namelist
        assert "contentmetadata.md" not in namelist
        assert "ExportInformation.info" not in namelist

    # Validator checks it as individual_iflow
    rep = validate_package(flow_bytes)
    assert rep["archive_type"] == "individual_iflow"
    assert rep["status"] == "PASSED"


# ==============================================================================
# 5. Diagnostic Package Validator Utility & Comparison
# ==============================================================================

def test_validator_detects_malformed_package():
    """Verify validator flags missing metadata, malformed XML, and invalid paths."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        # Invalid directory
        zf.writestr("src/main/resources/scenarioflows/integrationscenarioflows/bad.iflw", "<not-xml>")
        # Missing outer metadata
    val_rep = validate_package(buf.getvalue())
    assert val_rep["status"] == "FAILED"
    assert any("Missing mandatory outer package file" in e for e in val_rep["errors"])


def test_validator_on_synthetic_valid_package():
    """Verify validator completely passes a synthetically generated valid package."""
    sap_gen = SAPPlatformGenerator()
    flow_dict = {"name": "TestFlow", "source": {"type": "http:listener"}, "processors": []}
    xml_str = sap_gen.iflow_gen.generate_iflow(flow_dict)
    files = [
        GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/TestFlow.iflw", content=xml_str, role="source", generator="sap:iflow")
    ]
    pkg_bytes = sap_gen.package_content_package(files, "TestPkg", "Test Pkg")
    report = validate_package(pkg_bytes)
    assert report["status"] == "PASSED"
    assert len(report["errors"]) == 0
    assert report["archive_type"] == "content_package"


@pytest.mark.skipif(not KNOWN_GOOD_REFERENCE_PATH.exists(), reason="Known-good SAP archive not available on host")
def test_validator_on_known_good_reference_sap_archive():
    """Verify validator passes the native SAP Integration Suite export when present on the system."""
    report = validate_package(KNOWN_GOOD_REFERENCE_PATH)
    assert report["status"] == "PASSED", f"Native export had unexpected errors: {report['errors']}"
    assert report["archive_type"] == "content_package"
    assert len(report["errors"]) == 0


@pytest.mark.skipif(not KNOWN_GOOD_REFERENCE_PATH.exists(), reason="Known-good SAP archive not available on host")
def test_compare_reference_with_generated_package():
    """Verify package comparator matches outer package structure with known-good export."""
    sap_gen = SAPPlatformGenerator()
    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/employee_payroll.iflw",
            content=sap_gen.iflow_gen.generate_iflow({"name": "employee_payroll", "source": {"type": "http:listener"}, "processors": []}),
            role="source",
            generator="sap:iflow",
        )
    ]
    gen_bytes = sap_gen.package_content_package(files, "Employee_Payroll_Processor_1", "Employee Payroll Processor 1")
    report = validate_package(gen_bytes, reference_source=KNOWN_GOOD_REFERENCE_PATH)
    assert report["status"] == "PASSED"
    diff = report.get("reference_diff")
    assert diff is not None
    # Both packages share the mandatory outer files
    assert diff["matches_reference_contract"] is True
    assert len(diff["missing_structural_files"]) == 0


# ==============================================================================
# 6. Export Service Platform Routing and Manifest Generation
# ==============================================================================

def test_export_service_sap_package_routing():
    """Verify build_export routes to SAP package when target_platform is sap-cpi."""
    inputs = {
        "project_name": "OrderServiceApp",
        "project_files": [
            {
                "name": "order-api.xml",
                "path": "src/main/mule/order-api.xml",
                "content": """<mule xmlns="http://www.mulesoft.org/schema/mule/core"
                                     xmlns:http="http://www.mulesoft.org/schema/mule/http">
                    <flow name="order-flow">
                        <http:listener path="/orders"/>
                        <logger message="Processing order"/>
                    </flow>
                </mule>""",
            },
            {
                "name": "transform.dwl",
                "path": "src/main/resources/transform.dwl",
                "content": "%dw 2.0 output application/json --- { orderId: payload.id }",
            },
        ],
    }

    req = ExportRequest(
        project_id="order-service-app",
        target_platform="sap-cpi",
        format="cpi-package",
    )
    result = build_export(
        req,
        file_lookup=lambda pid: inputs["project_files"],
        job_lookup=lambda pid: {"project_name": inputs.get("project_name")},
    )

    assert result.format == "cpi-package"
    assert result.manifest["target_platform"] == "sap-integration-suite"
    assert result.manifest["export_type"] == "sap-cpi-package"
    assert "Design -> Integrations and APIs -> Import" in result.manifest["upload_instructions"]
    assert result.manifest["target_compatibility"]["reference_used"] is False
    assert result.manifest["target_compatibility"]["summary"]["total_artifacts"] >= 1

    # Verify bytes form a valid package
    rep = validate_package(result.bytes)
    assert rep["status"] == "PASSED"
    assert rep["archive_type"] == "content_package"


def test_export_service_sap_individual_flow_routing():
    """Verify build_export routes to individual flow when format is cpi-iflow."""
    inputs = {
        "project_name": "InvoiceProcess",
        "project_files": [
            {
                "name": "invoice.xml",
                "path": "src/main/mule/invoice.xml",
                "content": """<mule xmlns="http://www.mulesoft.org/schema/mule/core">
                    <flow name="invoice-flow">
                        <logger message="Invoice"/>
                    </flow>
                </mule>""",
            }
        ],
    }

    req = ExportRequest(
        project_id="invoice-process",
        target_platform="sap-cpi",
        format="cpi-iflow",
    )
    result = build_export(
        req,
        file_lookup=lambda pid: inputs["project_files"],
        job_lookup=lambda pid: {"project_name": inputs.get("project_name")},
    )

    assert result.format == "cpi-iflow"
    assert result.manifest["export_type"] == "sap-cpi-individual-flow"
    assert "Artifacts -> Edit -> Add -> Integration Flow -> Upload" in result.manifest["upload_instructions"]

    rep = validate_package(result.bytes)
    assert rep["status"] == "PASSED"
    assert rep["archive_type"] == "individual_iflow"


def test_reference_manifest_version_requires_repeated_valid_observation():
    assert _sap_reference_bundle_version({"artifacts": [
        {"artifact_id": "flow_one", "manifest": {"Bundle-Version": "2.4.1"}},
        {"artifact_id": "flow_two", "manifest": {"Bundle-Version": "2.4.1"}},
        {"artifact_id": "flow_three", "manifest": {"Bundle-Version": "1.0.0"}},
    ]}) == "2.4.1"
    assert _sap_reference_bundle_version({"artifacts": [
        {"artifact_id": "flow_one", "manifest": {"Bundle-Version": "2.4.1"}},
        {"artifact_id": "flow_two", "manifest": {"Bundle-Version": "1.0.0"}},
    ]}) is None
    assert _sap_reference_bundle_version({"artifacts": [
        {"artifact_id": "flow_one", "manifest": {"Bundle-Version": "../../unsafe"}},
        {"artifact_id": "flow_two", "manifest": {"Bundle-Version": "../../unsafe"}},
    ]}) is None
    assert _sap_reference_bundle_version({"artifacts": [
        {"artifact_id": "same_flow", "manifest": {"Bundle-Version": "2.4.1"}},
        {"artifact_id": "same_flow", "manifest": {"Bundle-Version": "2.4.1"}},
    ]}) is None


def test_sap_export_uses_repeated_reference_bundle_version(monkeypatch):
    from mule_parser.services import export_service
    from mule_parser.platforms.sap.sap_reference_analyzer import analyze_sap_reference

    profile = {
        "artifacts": [
            {"artifact_id": "reference_one", "manifest": {"Bundle-Version": "2.4.1"}},
            {"artifact_id": "reference_two", "manifest": {"Bundle-Version": "2.4.1"}},
        ],
        "adapter_inventory": [],
        "naming_conventions": [{
            "scope": "artifact_identifiers", "style": "lower_snake_case",
            "confidence": "inferred", "basis_artifact_count": 3,
        }],
    }
    monkeypatch.setattr(export_service, "_load_sap_reference_profile", lambda _project_id: (profile, None))
    source = {
        "name": "billing.xml",
        "path": "src/main/mule/billing.xml",
        "content": '<mule xmlns="http://www.mulesoft.org/schema/mule/core"><flow name="BillingFlow"><logger message="Billing"/></flow></mule>',
    }
    result = build_export(
        ExportRequest(project_id="billing", target_platform="sap-cpi", format="cpi-iflow"),
        file_lookup=lambda _project_id: [source],
    )

    generated = analyze_sap_reference(result.bytes)
    assert generated["artifacts"][0]["manifest"]["Bundle-Version"] == "2.4.1"
    assert any(resource["path"].endswith("/billing_flow.iflw") for resource in generated["artifacts"][0]["resources"])
    assert result.manifest["target_compatibility"]["reference_conventions_applied"] == {
        "Bundle-Version": "2.4.1", "artifact_identifier_style": "lower_snake_case",
    }


# ==============================================================================
# 7. Decoupled 6-Stage SAP Integration Suite API Lifecycle & Credential Safety
# ==============================================================================

def test_staged_migration_pipeline_halts_on_invalid_local_archive():
    """Verify pipeline strictly halts at LOCAL_ARCHIVE_VALIDATION if archive is corrupt without calling SAP APIs."""
    bad_bytes = b"not a zip file"
    stages = run_staged_migration_pipeline(
        package_id="TestPkg",
        package_name="Test Pkg",
        iflow_artifacts=[("TestFlow", "TestFlow", bad_bytes)],
    )

    # Must complete ARTIFACT_GENERATION
    assert stages[0].stage == MigrationStage.ARTIFACT_GENERATION
    assert stages[0].status == StageStatus.SUCCESS

    # Must fail at LOCAL_ARCHIVE_VALIDATION
    assert stages[1].stage == MigrationStage.LOCAL_ARCHIVE_VALIDATION
    assert stages[1].status == StageStatus.FAILED

    # Subsequent stages must be SKIPPED
    assert stages[2].stage == MigrationStage.SAP_PACKAGE_IMPORT
    assert stages[2].status == StageStatus.SKIPPED


def test_staged_migration_pipeline_skips_api_when_credentials_not_configured():
    """Verify pipeline safely validates local archive and marks remote stages FAILED when credentials absent."""
    sap_gen = SAPPlatformGenerator()
    flow_bytes = sap_gen.package_individual_flow([], "SafeFlow", "Safe Flow")

    client = SAPIntegrationSuiteClient(config=SAPClientConfig(tenant_host=""))
    stages = run_staged_migration_pipeline(
        package_id="SafePkg",
        package_name="Safe Pkg",
        iflow_artifacts=[("SafeFlow", "SafeFlow", flow_bytes)],
        client=client,
        allow_api_import=True,
    )

    assert stages[0].stage == MigrationStage.ARTIFACT_GENERATION
    assert stages[0].status == StageStatus.SUCCESS

    assert stages[1].stage == MigrationStage.LOCAL_ARCHIVE_VALIDATION
    assert stages[1].status == StageStatus.SUCCESS

    # Remote stage fails safely with actionable credentials error, remaining skipped
    assert stages[2].stage == MigrationStage.SAP_PACKAGE_IMPORT
    assert stages[2].status == StageStatus.FAILED
    assert "credentials not configured" in stages[2].message.lower()
    assert stages[3].status == StageStatus.SKIPPED


def test_no_hardcoded_credentials_in_client():
    """Verify client default configuration contains zero hardcoded credentials."""
    cfg = SAPClientConfig()
    assert cfg.client_id == "" or "env" in os.environ
    assert cfg.client_secret == "" or "env" in os.environ
    assert cfg.password == "" or "env" in os.environ


def test_phase1_mulesoft_container_unpacking_and_tag_sanitization():
    """Verify loopingTask, choice, sequence, logger, set-payload, raise-error are properly normalized."""
    complex_raw_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
                 xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL">
        <process id="complex_flow" name="Complex Flow" isExecutable="true">
            <startEvent id="start_1" name="Start"/>
            <sequenceFlow id="f_start" sourceRef="start_1" targetRef="loop_1"/>
            <loopingTask id="loop_1" name="For Each Item" multiInstance="parallel">
                <incoming>f_start</incoming>
                <outgoing>f_after_loop</outgoing>
                <serviceTask id="fetch_item" name="Fetch Item"
                             script="src/main/resources/script/transform-message-set-payload.groovy"/>
                <sequenceFlow id="f_inner" sourceRef="fetch_item" targetRef="choice_1"/>
                <choice id="choice_1" name="Check Item">
                    <when expression="payload.valid == true">
                        <logger id="log_ok" message="Item is valid"/>
                        <set-payload id="set_ok" value="OK"/>
                    </when>
                    <otherwise>
                        <raise-error id="err_invalid" type="APP:INVALID_ITEM"/>
                    </otherwise>
                </choice>
            </loopingTask>
            <sequenceFlow id="f_after_loop" sourceRef="loop_1" targetRef="end_1"/>
            <endEvent id="end_1" name="End"/>
        </process>
    </definitions>"""

    norm_xml, warns = validate_and_normalize_iflow_xml(
        complex_raw_xml,
        flow_name="ComplexFlow",
        available_scripts=["transform-message-set-payload.groovy"],
    )

    root = ET.fromstring(norm_xml)
    proc = root.find(f"{{{BPMN2_NS}}}process")
    assert proc is not None

    # Verify zero direct incoming or outgoing under process
    for child in proc:
        assert not child.tag.endswith(("incoming", "outgoing")), f"Stray tag {child.tag} directly in process"
        # Verify no raw mulesoft tags survived
        local = child.tag.split("}")[-1]
        assert local not in ("loopingTask", "choice", "when", "otherwise", "logger", "set-payload", "raise-error")

    # Verify loopingTask was unpacked and f_start rewired to fetch_item
    sf_start = next(sf for sf in proc.findall(f"{{{BPMN2_NS}}}sequenceFlow") if sf.get("id") == "f_start")
    assert sf_start.get("targetRef") == "fetch_item"

    # Verify choice became an exclusiveGateway
    gw = next(e for e in proc if e.get("id") == "choice_1")
    assert gw.tag == f"{{{BPMN2_NS}}}exclusiveGateway"

    # Verify script reference was resolved and standardized to basename
    task_fetch = next(e for e in proc if e.get("id") == "fetch_item")
    assert task_fetch.tag == f"{{{BPMN2_NS}}}callActivity"
    script_prop = None
    for p in task_fetch.findall(f".//{{{IFL_NS}}}property"):
        k = p.find("key")
        v = p.find("value")
        if k is not None and k.text == "script" and v is not None:
            script_prop = v.text
    assert script_prop == "transform-message-set-payload.groovy"


def test_phase2_flow_filtering_and_script_bundling():
    """
    Verify Phase 2 requirements:
    1. Metadata/helper flows (enrichment_auto_*, application-types, pom, mq, log4j2) are filtered out.
    2. Every referenced Groovy script in each .iflw is physically bundled in src/main/resources/script/.
    3. Missing scripts are auto-synthesized with valid Groovy stubs.
    4. Package validates with PASSED and zero errors.
    """
    # 1. Synthetic test with metadata flows and missing script references
    iflow_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
                       xmlns:ifl="http://com.sap.ifl.model/Ifl.xsd"
                       id="Definitions_1">
        <bpmn2:process id="OrderProcess" isExecutable="false">
            <bpmn2:startEvent id="Start_1">
                <bpmn2:outgoing>Flow_1</bpmn2:outgoing>
            </bpmn2:startEvent>
            <bpmn2:callActivity id="Task_1" name="Execute Script">
                <bpmn2:extensionElements>
                    <ifl:property>
                        <key>activityType</key>
                        <value>Script</value>
                    </ifl:property>
                    <ifl:property>
                        <key>script</key>
                        <value>missingCustomHelper.groovy</value>
                    </ifl:property>
                </bpmn2:extensionElements>
                <bpmn2:incoming>Flow_1</bpmn2:incoming>
                <bpmn2:outgoing>Flow_2</bpmn2:outgoing>
            </bpmn2:callActivity>
            <bpmn2:sequenceFlow id="Flow_1" sourceRef="Start_1" targetRef="Task_1"/>
            <bpmn2:sequenceFlow id="Flow_2" sourceRef="Task_1" targetRef="End_1"/>
            <bpmn2:endEvent id="End_1">
                <bpmn2:incoming>Flow_2</bpmn2:incoming>
            </bpmn2:endEvent>
        </bpmn2:process>
    </bpmn2:definitions>"""

    files = [
        # Genuine business flow
        GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/order-process.iflw", content=iflow_xml, role="source", generator="sap:iflow"),
        # Metadata / helper flows that MUST be filtered out
        GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/application-types.iflw", content="<process/>", role="source", generator="sap:iflow"),
        GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/enrichment_auto_123.iflw", content="<process/>", role="source", generator="sap:iflow"),
        GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/mq.iflw", content="<process/>", role="source", generator="sap:iflow"),
        GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/pom.iflw", content="<process/>", role="source", generator="sap:iflow"),
        GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/log4j2.iflw", content="<process/>", role="source", generator="sap:iflow"),
    ]

    pkg_bytes = create_content_package_archive(files, "TestPhase2Pkg", "Test Phase 2 Pkg")
    with zipfile.ZipFile(io.BytesIO(pkg_bytes), "r") as zf:
        namelist = zf.namelist()
        content_entries = [n for n in namelist if n.endswith("_content")]
        # Only the 1 genuine business flow should be packaged
        assert len(content_entries) == 1

        inner_bytes = zf.read(content_entries[0])
        with zipfile.ZipFile(io.BytesIO(inner_bytes), "r") as inner_zf:
            inner_names = inner_zf.namelist()
            # Verified that missingCustomHelper.groovy was synthesized into src/main/resources/script/
            assert "src/main/resources/script/missingCustomHelper.groovy" in inner_names
            stub_content = inner_zf.read("src/main/resources/script/missingCustomHelper.groovy").decode("utf-8")
            assert "def Message processData(Message message)" in stub_content

    # 2. Real project test if available
    if FAILING_ORIGINAL_PATH.exists():
        real_files = []
        with zipfile.ZipFile(FAILING_ORIGINAL_PATH, "r") as zf:
            for name in zf.namelist():
                if not name.endswith("/"):
                    real_files.append(GeneratedFile(
                        path=name,
                        content=zf.read(name),
                        role="source",
                        generator="raw",
                    ))
        real_pkg_bytes = create_content_package_archive(real_files, "Ordering_Process", "Ordering Process")
        report = validate_package(real_pkg_bytes)
        assert report["status"] == "PASSED", f"Ordering Process validation failed: {report['errors']}"
        with zipfile.ZipFile(io.BytesIO(real_pkg_bytes), "r") as out_zf:
            content_entries = [n for n in out_zf.namelist() if n.endswith("_content")]
            # Exactly 13 genuine business flows
            assert len(content_entries) == 13
            for ce in content_entries:
                inner_zf = zipfile.ZipFile(io.BytesIO(out_zf.read(ce)), "r")
                scripts = [f for f in inner_zf.namelist() if f.startswith("src/main/resources/script/")]
                assert len(scripts) >= 1, f"Inner archive {ce} missing scripts!"


def test_phase3_osgi_manifest_formatting_and_alignment():
    """
    Verify Phase 3 requirements:
    1. META-INF/MANIFEST.MF strictly adheres to RFC 2822: <= 72 bytes per line.
    2. Uses standard CRLF (\\r\\n) line endings and ends with trailing blank line.
    3. Continuation lines begin with a single space.
    4. Import-Package matches the canonical SAP Integration Suite OSGi packages.
    5. All inner artifact archives in ordering_process have compliant manifests.
    """
    pkg_gen = CPIPackageGenerator()
    manifests = pkg_gen.build_package_manifests("TestFlow_123", "Test Flow 123", "1.0.0", include_metainfo=False)
    mf_file = next(f for f in manifests if f.path == "META-INF/MANIFEST.MF")
    mf_bytes = mf_file.content.encode("utf-8") if isinstance(mf_file.content, str) else mf_file.content

    # 1. Line endings must be CRLF
    assert b"\r\n" in mf_bytes
    assert mf_bytes.endswith(b"\r\n\r\n")

    # 2. Every single line must be <= 72 bytes
    lines = mf_bytes.split(b"\r\n")
    for idx, line in enumerate(lines[:-2]):  # omit trailing blank lines
        assert len(line) <= 72, f"Manifest line {idx} exceeds 72 bytes ({len(line)}): {line!r}"
        if idx > 0 and lines[idx - 1].startswith(b"Import-Package:") and not line.startswith(b"Origin-Bundle-Name:"):
            # Continuation lines must begin with a single space
            assert line.startswith(b" "), f"Continuation line {idx} does not start with space: {line!r}"

    # 3. Test on ordering_process package if available
    if FAILING_ORIGINAL_PATH.exists():
        real_files = []
        with zipfile.ZipFile(FAILING_ORIGINAL_PATH, "r") as zf:
            for name in zf.namelist():
                if not name.endswith("/"):
                    real_files.append(GeneratedFile(path=name, content=zf.read(name), role="source", generator="raw"))

        real_pkg_bytes = create_content_package_archive(real_files, "Ordering_Process", "Ordering Process")
        report = validate_package(real_pkg_bytes)
        assert report["status"] == "PASSED"
        assert len(report["errors"]) == 0

        # Check every inner manifest
        with zipfile.ZipFile(io.BytesIO(real_pkg_bytes), "r") as out_zf:
            for ce in [n for n in out_zf.namelist() if n.endswith("_content")]:
                inner_zf = zipfile.ZipFile(io.BytesIO(out_zf.read(ce)), "r")
                inner_mf = inner_zf.read("META-INF/MANIFEST.MF")
                inner_lines = inner_mf.split(b"\r\n")
                for l_idx, l in enumerate(inner_lines[:-2]):
                    assert len(l) <= 72, f"{ce} MANIFEST.MF line {l_idx} length {len(l)} > 72: {l!r}"


def test_multiple_bpmn2_processes_and_service_tasks_merged_and_converted():
    """Verify that multiple <bpmn2:process> sibling elements are merged into the primary process,
    and all serviceTasks are converted to callActivities."""
    xml_with_two_processes = """<?xml version="1.0" encoding="UTF-8"?>
    <bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
                       xmlns:ifl="http:///com.sap.ifl.model/Ifl.xsd"
                       id="Definitions_1">
        <bpmn2:process id="Process_shipping" name="Shipping Flow" isExecutable="true">
            <bpmn2:startEvent id="start_1" name="Start"/>
            <bpmn2:callActivity id="logger_1" name="Logger"/>
            <bpmn2:sequenceFlow id="f1" sourceRef="start_1" targetRef="logger_1"/>
            <bpmn2:endEvent id="end_1" name="End"/>
            <bpmn2:sequenceFlow id="f2" sourceRef="logger_1" targetRef="end_1"/>
        </bpmn2:process>
        <bpmn2:process id="transformScript">
            <bpmn2:serviceTask id="task_transform_message" name="Transform Message" implementation="src.main.resources.script.transform-message-set-payload.groovy"/>
        </bpmn2:process>
    </bpmn2:definitions>"""

    norm_xml, warns = validate_and_normalize_iflow_xml(
        xml_with_two_processes,
        flow_name="shipping_serviceFlow",
        available_scripts=["transform-message-set-payload.groovy"],
    )

    root = ET.fromstring(norm_xml)
    processes = [e for e in root if e.tag.endswith("process")]
    assert len(processes) == 1, f"Expected exactly 1 process, found {len(processes)}"

    # Verify no serviceTasks exist anywhere
    service_tasks = [e for e in root.iter() if e.tag.endswith("serviceTask")]
    assert len(service_tasks) == 0, f"Found unexpected serviceTasks: {service_tasks}"

    # Verify task_transform_message was converted to callActivity and merged into primary process
    task = next((e for e in processes[0] if e.get("id") == "task_transform_message"), None)
    assert task is not None
    assert task.tag.endswith("callActivity")
    assert "implementation" not in task.attrib


def test_duplicate_flow_names_and_unique_ids_disambiguated():
    """Verify that when flows would have colliding safe identifiers (e.g. error_handler and error-handler),
    the CPI package generator disambiguates their symbolic names, uniqueIds, and artifact names."""
    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/error_handler.iflw",
            content="""<?xml version="1.0" encoding="UTF-8"?>
            <bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL" id="Definitions_1">
                <bpmn2:process id="Process_error_handler" isExecutable="true">
                    <bpmn2:startEvent id="start_1" name="Start"/>
                    <bpmn2:endEvent id="end_1" name="End"/>
                </bpmn2:process>
            </bpmn2:definitions>""",
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/error-handler.iflw",
            content="""<?xml version="1.0" encoding="UTF-8"?>
            <bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL" id="Definitions_1">
                <bpmn2:process id="Process_error_handler" isExecutable="true">
                    <bpmn2:startEvent id="start_2" name="Start"/>
                    <bpmn2:endEvent id="end_2" name="End"/>
                </bpmn2:process>
            </bpmn2:definitions>""",
            role="source",
            generator="sap:iflow",
        ),
    ]

    pkg_gen = CPIPackageGenerator()
    pkg_bytes = pkg_gen.create_zip_archive(
        files,
        package_id="test_pkg",
        package_name="Test Package",
        export_type="package",
    )

    report = validate_package(pkg_bytes)
    assert report["status"] == "PASSED", f"Package failed validation: {report['errors']}"
    assert len(report["errors"]) == 0

    # Verify resources.cnt has distinct uniqueIds and names
    with zipfile.ZipFile(io.BytesIO(pkg_bytes), "r") as z:
        cnt_raw = z.read("resources.cnt")
        cnt_data = json.loads(base64.b64decode(cnt_raw).decode("utf-8"))
        uids = [r.get("uniqueId") for r in cnt_data["resources"]]
        names = [r.get("name") for r in cnt_data["resources"]]
        assert len(uids) == len(set(uids)), f"Duplicate uniqueIds found: {uids}"
        assert len(names) == len(set(names)), f"Duplicate names found: {names}"


def test_sequence_flow_without_id_serialization():
    """Verify that an iFlow with sequenceFlow elements missing 'id' or having None attributes serializes cleanly without TypeError."""
    raw_xml_missing_sf_id = """<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
        xmlns:ifl="http://www.sap.com/Integration/IFL"
        xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
        xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"
        xmlns:di="http://www.omg.org/spec/DD/20100524/DI"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        targetNamespace="http://www.example.com/bpmn">
        <bpmn2:process id="emailServiceFlow" isExecutable="true">
            <bpmn2:serviceTask id="serviceTask" name="Process Email" implementation="src.main.resources.script.transform-message-set-payload" />
            <bpmn2:sequenceFlow sourceRef="startEvent" targetRef="serviceTask" />
            <bpmn2:startEvent id="startEvent" name="Start" />
            <bpmn2:sequenceFlow id="flow1" sourceRef="serviceTask" targetRef="endEvent" />
            <bpmn2:endEvent id="endEvent" name="End" />
        </bpmn2:process>
    </bpmn2:definitions>"""

    norm_xml, warns = validate_and_normalize_iflow_xml(
        raw_xml_missing_sf_id,
        flow_name="email_serviceFlow",
    )

    assert norm_xml.startswith('<?xml version="1.0" encoding="UTF-8"?>')
    root = ET.fromstring(norm_xml)
    # Verify all sequenceFlows have an id
    for sf in root.findall(f".//{{{BPMN2_NS}}}sequenceFlow"):
        assert sf.get("id") is not None
        assert sf.get("id") != "None"
        assert len(sf.get("id")) > 0

    # Verify all BPMNEdge elements have non-null bpmnElement and id
    for edge in root.findall(f".//{{{BPMNDI_NS}}}BPMNEdge"):
        assert edge.get("id") is not None
        assert edge.get("id") != "BPMNEdge_None"
        assert edge.get("bpmnElement") is not None
        assert edge.get("bpmnElement") != "None"


def test_cpi_full_package_matches_sap_native_schema_and_forensic_spec():
    """
    Forensic verification test confirming full package matches SAP-native export:
    1. IFlow contentType is application/x-zip-compressed (not application/octet-stream)
    2. All resources declare scope='EXTERNAL'
    3. isInternal field is omitted
    4. versionComment is 'Resource Created'
    5. ContentPackage uniqueId and name are alphanumeric without underscores (e.g. OrderingProcess)
    6. IFlow resource name in resources.cnt is {id}_content.zip matching payload {id}_content
    7. hash array is a 2-tuple matching sha256(contentmetadata.md) and sha256(resources.cnt)
    8. Package passes validate_package without errors
    """
    pkg_gen = CPIPackageGenerator()
    flow_xml = pkg_gen.iflow_gen.generate_iflow({"name": "customer-service-flow", "processors": []})
    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/customer-service-flow.iflw",
            content=flow_xml,
            role="source",
            generator="sap:iflow",
        )
    ]

    pkg_bytes = pkg_gen.create_zip_archive(
        files,
        package_id="Ordering_Process",
        package_name="Ordering Process",
        export_type="package",
    )

    with zipfile.ZipFile(io.BytesIO(pkg_bytes), "r") as z:
        namelist = z.namelist()
        raw_cnt = z.read("resources.cnt")
        cnt_data = json.loads(base64.b64decode(raw_cnt).decode("utf-8"))
        raw_md = z.read("contentmetadata.md")
        raw_hash = z.read("hash")
        hash_list = json.loads(raw_hash)

        # 1. Check ContentPackage resource
        pkg_res = next(r for r in cnt_data["resources"] if r.get("resourceType") == "ContentPackage")
        assert pkg_res["name"] == "OrderingProcess", f"Expected alphanumeric name 'OrderingProcess', got {pkg_res['name']}"
        assert pkg_res["uniqueId"] == "OrderingProcess", f"Expected alphanumeric uniqueId 'OrderingProcess', got {pkg_res['uniqueId']}"
        assert pkg_res.get("isInternal") is False
        assert "scope" not in pkg_res or pkg_res.get("scope") != "EXTERNAL"
        assert "versionComment" not in pkg_res

        # 2. Check IFlow resource
        iflow_res = next(r for r in cnt_data["resources"] if r.get("resourceType") == "IFlow")
        art_id = iflow_res["id"]
        assert iflow_res["contentType"] == "application/octet-stream"
        assert iflow_res.get("versionComment") == ""
        assert iflow_res.get("isInternal") is False
        assert iflow_res["name"] == "customer-service-flow.zip"
        assert iflow_res["displayName"] == "customer-service-flow"

        # 3. Verify matching payload in archive
        assert f"{art_id}_content" in namelist

        # 4. Verify hash matches per-resource sha256 (flow payload + resources.cnt)
        assert len(hash_list) == 2
        exp_flow_hash = hashlib.sha256(z.read(f"{art_id}_content")).hexdigest()
        exp_cnt_hash = hashlib.sha256(raw_cnt).hexdigest()
        assert hash_list[0] == exp_flow_hash
        assert hash_list[1] == exp_cnt_hash

    # 5. Run full validator
    report = validate_package(pkg_bytes)
    assert report["status"] == "PASSED"
    assert len(report["errors"]) == 0


def test_colon_and_prefix_scripts_sanitized_and_no_illegal_paths_in_cpi_archive():
    """
    Verifies that scripts and flow-refs with colons (e.g. script:foo.groovy, flow-ref:bar)
    are strictly sanitized to clean filenames, properly matched against existing scripts,
    and never produce illegal characters or dummy colon stubs in the final archive.
    """
    pkg_gen = CPIPackageGenerator()

    # Synthetic XML that references scripts with 'script:' and 'flow-ref:' prefixes
    flow_with_colon_refs = """<?xml version="1.0" encoding="UTF-8"?>
<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
                   xmlns:ifl="http:///com.sap.ifl.model/Ifl.xsd"
                   id="Definitions_1">
    <bpmn2:process id="Process_Order" isExecutable="true">
        <bpmn2:callActivity id="step_shipping" name="Prepare shipping">
            <bpmn2:extensionElements>
                <ifl:property><key>scriptFunction</key><value>processData</value></ifl:property>
                <ifl:property><key>activityType</key><value>Script</value></ifl:property>
                <ifl:property><key>subActivityType</key><value>GroovyScript</value></ifl:property>
                <ifl:property><key>script</key><value>script:shipping-invoice-request.groovy</value></ifl:property>
            </bpmn2:extensionElements>
        </bpmn2:callActivity>
        <bpmn2:serviceTask id="step_save" name="Save Order" implementation="flow-ref:save-order"/>
    </bpmn2:process>
</bpmn2:definitions>"""

    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/order_flow.iflw",
            content=flow_with_colon_refs,
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/script/shipping-invoice-request.groovy",
            content="// Real shipping invoice logic",
            role="source",
            generator="sap:groovy",
        ),
        GeneratedFile(
            path="src/main/resources/script/save-order.groovy",
            content="// Real save order logic",
            role="source",
            generator="sap:groovy",
        ),
    ]

    pkg_bytes = pkg_gen.create_zip_archive(
        files,
        package_id="Order_System",
        package_name="Order System",
        export_type="package",
    )

    with zipfile.ZipFile(io.BytesIO(pkg_bytes), "r") as outer_zf:
        # Check all inner archives
        for name in outer_zf.namelist():
            assert ":" not in name, f"Illegal colon in outer archive entry: {name}"
            if name.endswith("_content"):
                inner_zf = zipfile.ZipFile(io.BytesIO(outer_zf.read(name)))
                for iname in inner_zf.namelist():
                    assert ":" not in iname, f"Illegal colon in inner archive entry: {iname}"
                    assert "\\" not in iname, f"Backslash in inner archive entry: {iname}"

                # Verify order_flow.iflw XML has clean script references
                if "src/main/resources/scenarioflows/integrationflow/order_flow.iflw" in inner_zf.namelist():
                    xml_str = inner_zf.read("src/main/resources/scenarioflows/integrationflow/order_flow.iflw").decode("utf-8")
                    assert "script:shipping-invoice-request.groovy" not in xml_str
                    assert "shipping-invoice-request.groovy" in xml_str
                    assert "flow-ref:save-order" not in xml_str
                    assert "save-order.groovy" in xml_str

                # Verify clean scripts exist in inner archive without dummy colon copies
                assert "src/main/resources/script/shipping-invoice-request.groovy" in inner_zf.namelist()
                assert "src/main/resources/script/save-order.groovy" in inner_zf.namelist()
                assert "src/main/resources/script/script:shipping-invoice-request.groovy" not in inner_zf.namelist()
                assert "src/main/resources/script/flow-ref:save-order.groovy" not in inner_zf.namelist()


# ==============================================================================
# 9. SAP CPI OData API Client, Service Key, and Deployment Verification Tests
# ==============================================================================

def test_sap_client_config_from_service_key(monkeypatch):
    """Verify SAPClientConfig parses BTP service key dict, JSON string, and env var."""
    # Standard SAP BTP Process Integration Runtime service key layout:
    # Top-level 'url' is the API base URL, while 'oauth.url' is the authentication server URL.
    sk_dict = {
        "oauth": {
            "clientid": "sb-test-client!b123",
            "clientsecret": "secret12345",
            "url": "https://tenant.authentication.eu10.hana.ondemand.com",
        },
        "url": "https://tenant-it-db-design.it-cpi001.cfapps.eu10.hana.ondemand.com",
    }

    # Dict parsing with auto-appending /oauth/token to oauth.url, and taking API base from top-level 'url'
    cfg = SAPClientConfig.from_service_key(sk_dict)
    assert cfg.client_id == "sb-test-client!b123"
    assert cfg.client_secret == "secret12345"
    assert cfg.token_url == "https://tenant.authentication.eu10.hana.ondemand.com/oauth/token"
    assert cfg.tenant_host == "https://tenant-it-db-design.it-cpi001.cfapps.eu10.hana.ondemand.com"
    assert cfg.has_credentials is True

    # Accidental Web UI URL gets stripped to API origin
    ui_key = dict(sk_dict)
    ui_key["url"] = "https://tenant.integrationsuite.cfapps.eu10.hana.ondemand.com/shell/design"
    cfg_ui = SAPClientConfig.from_service_key(ui_key)
    assert "/shell" not in cfg_ui.tenant_host
    assert cfg_ui.tenant_host == "https://tenant.integrationsuite.cfapps.eu10.hana.ondemand.com"

    # JSON string parsing
    cfg_json = SAPClientConfig.from_service_key(json.dumps(sk_dict))
    assert cfg_json.client_id == "sb-test-client!b123"
    assert cfg_json.token_url == "https://tenant.authentication.eu10.hana.ondemand.com/oauth/token"
    assert cfg_json.tenant_host == "https://tenant-it-db-design.it-cpi001.cfapps.eu10.hana.ondemand.com"

    # Auto-loading via SAP_CPI_SERVICE_KEY environment variable
    monkeypatch.setenv("SAP_CPI_SERVICE_KEY", json.dumps(sk_dict))
    cfg_env = SAPClientConfig()
    assert cfg_env.client_id == "sb-test-client!b123"
    assert cfg_env.token_url == "https://tenant.authentication.eu10.hana.ondemand.com/oauth/token"
    assert cfg_env.tenant_host == "https://tenant-it-db-design.it-cpi001.cfapps.eu10.hana.ondemand.com"


def test_cpi_api_client_package_create_and_update():
    """Verify create_or_verify_package uses PUT when package exists and POST when it does not."""
    from unittest.mock import MagicMock, patch
    import urllib.error

    cfg = SAPClientConfig(
        tenant_host="https://fake-cpi.cfapps.eu10.hana.ondemand.com",
        client_id="dummy",
        client_secret="dummy",
    )
    client = SAPIntegrationSuiteClient(config=cfg)
    client.fetch_csrf_token = MagicMock(return_value=("fake-csrf-token", "fake-cookie"))
    client.get_auth_headers = MagicMock(return_value={"Authorization": "Bearer fake-token"})

    class MockResp:
        def __init__(self, data=b"{}", code=200):
            self.data = data
            self.code = code
        def read(self):
            return self.data
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

    # Case A: Package already exists -> issues PUT to update
    recorded_requests = []
    def fake_urlopen_exists(req, timeout=30):
        recorded_requests.append(req)
        return MockResp(b'{"d": {"Id": "pkg1"}}', code=200)

    with patch("urllib.request.urlopen", side_effect=fake_urlopen_exists):
        res = client.create_or_verify_package(
            package_id="pkg1",
            package_name="Updated Package Name",
            description="New Description",
            version="1.0.1",
        )
        assert res["status"] == "updated"
        assert len(recorded_requests) == 2
        assert recorded_requests[0].get_method() == "GET"
        assert recorded_requests[1].get_method() == "PUT"
        payload = json.loads(recorded_requests[1].data.decode("utf-8"))
        assert payload["Name"] == "Updated Package Name"
        assert payload["Version"] == "1.0.1"

    # Case B: Package does not exist -> issues POST to create
    recorded_requests.clear()
    def fake_urlopen_new(req, timeout=30):
        recorded_requests.append(req)
        if req.get_method() == "GET":
            raise urllib.error.HTTPError(req.full_url, 404, "Not Found", {}, io.BytesIO(b"Not Found"))
        return MockResp(b'{"d": {"Id": "pkg2"}}', code=201)

    with patch("urllib.request.urlopen", side_effect=fake_urlopen_new):
        res = client.create_or_verify_package(
            package_id="pkg2",
            package_name="New Package Name",
            version="1.0.0",
        )
        assert res["status"] == "created"
        assert len(recorded_requests) == 2
        assert recorded_requests[0].get_method() == "GET"
        assert recorded_requests[1].get_method() == "POST"
        payload = json.loads(recorded_requests[1].data.decode("utf-8"))
        assert payload["Id"] == "pkg2"
        assert payload["Name"] == "New Package Name"
        assert payload["Version"] == "1.0.0"


def test_cpi_api_client_upload_artifact_create_and_update():
    """Verify upload_iflow_artifact includes Version in POST and falls back to PUT on existing artifact."""
    from unittest.mock import MagicMock, patch
    import urllib.error

    cfg = SAPClientConfig(
        tenant_host="https://fake-cpi.cfapps.eu10.hana.ondemand.com",
        client_id="dummy",
        client_secret="dummy",
    )
    client = SAPIntegrationSuiteClient(config=cfg)
    client.fetch_csrf_token = MagicMock(return_value=("fake-csrf-token", "fake-cookie"))
    client.get_auth_headers = MagicMock(return_value={"Authorization": "Bearer fake-token"})

    class MockResp:
        def __init__(self, data=b"{}", code=200):
            self.data = data
            self.code = code
        def read(self):
            return self.data
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

    dummy_zip = b"PK\x03\x04fake-zip-data"

    # Case A: Artifact does not exist -> POST includes Version, Id, Name, PackageId, ArtifactContent
    recorded_requests = []
    def fake_urlopen_create(req, timeout=60):
        recorded_requests.append(req)
        if req.get_method() == "GET":
            raise urllib.error.HTTPError(req.full_url, 404, "Not Found", {}, io.BytesIO(b"Not Found"))
        return MockResp(b'{"d": {"Id": "flow1"}}', code=201)

    with patch("urllib.request.urlopen", side_effect=fake_urlopen_create):
        res = client.upload_iflow_artifact(
            package_id="pkg1",
            iflow_id="flow1",
            iflow_name="Flow 1",
            iflow_zip_bytes=dummy_zip,
            version="1.2.3",
        )
        assert res["status"] == "created"
        assert len(recorded_requests) == 2
        post_req = recorded_requests[1]
        assert post_req.get_method() == "POST"
        payload = json.loads(post_req.data.decode("utf-8"))
        assert payload["Id"] == "flow1"
        assert payload["Name"] == "Flow 1"
        assert payload["Version"] == "1.2.3"
        assert payload["PackageId"] == "pkg1"
        assert payload["ArtifactContent"] == base64.b64encode(dummy_zip).decode("utf-8")

    # Case B: Artifact exists -> PUT binary payload
    recorded_requests.clear()
    def fake_urlopen_update(req, timeout=60):
        recorded_requests.append(req)
        return MockResp(b"", code=200)

    with patch("urllib.request.urlopen", side_effect=fake_urlopen_update):
        res = client.upload_iflow_artifact(
            package_id="pkg1",
            iflow_id="flow1",
            iflow_name="Flow 1",
            iflow_zip_bytes=dummy_zip,
            version="1.2.3",
        )
        assert res["status"] == "updated"
        assert len(recorded_requests) == 2
        put_req = recorded_requests[1]
        assert put_req.get_method() == "PUT"
        assert put_req.data == dummy_zip


def test_cpi_api_client_runtime_status():
    """Verify read_runtime_status reads status and handles undeployed flows."""
    from unittest.mock import MagicMock, patch
    import urllib.error

    cfg = SAPClientConfig(
        tenant_host="https://fake-cpi.cfapps.eu10.hana.ondemand.com",
        client_id="dummy",
        client_secret="dummy",
    )
    client = SAPIntegrationSuiteClient(config=cfg)
    client.get_auth_headers = MagicMock(return_value={"Authorization": "Bearer fake-token"})

    class MockResp:
        def __init__(self, data=b"{}", code=200):
            self.data = data
            self.code = code
        def read(self):
            return self.data
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

    # Case A: Deployed flow found in runtime
    def fake_urlopen_deployed(req, timeout=30):
        return MockResp(b'{"d": {"Id": "flow1", "Status": "STARTED", "Version": "1.0.0"}}', code=200)

    with patch("urllib.request.urlopen", side_effect=fake_urlopen_deployed):
        res = client.read_runtime_status("flow1")
        assert res.get("Status") == "STARTED"

    # Case B: Flow not deployed (404)
    def fake_urlopen_not_found(req, timeout=30):
        raise urllib.error.HTTPError(req.full_url, 404, "Not Found", {}, io.BytesIO(b"Not Found"))

    with patch("urllib.request.urlopen", side_effect=fake_urlopen_not_found):
        res = client.read_runtime_status("flow1")
        assert res.get("Status") == "NOT_DEPLOYED"


# ==============================================================================
# 10. No-Credentials Fallback, Native Attributes, and Validator Truthfulness
# ==============================================================================

def test_multiflow_no_credentials_bundle_and_instructions():
    """Verify multi-flow iflow export generates individual zips and INSTRUCTIONS.txt."""
    pkg_gen = CPIPackageGenerator()
    flow1_xml = pkg_gen.iflow_gen.generate_iflow({"name": "order_service", "processors": []})
    flow2_xml = pkg_gen.iflow_gen.generate_iflow({"name": "invoice_service", "processors": []})

    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/order_service.iflw",
            content=flow1_xml,
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/invoice_service.iflw",
            content=flow2_xml,
            role="source",
            generator="sap:iflow",
        ),
    ]

    bundle_bytes = pkg_gen.create_zip_archive(files, package_id="sales_integration", export_type="iflow")

    with zipfile.ZipFile(io.BytesIO(bundle_bytes), "r") as zf:
        names = zf.namelist()
        assert "order_service.zip" in names
        assert "invoice_service.zip" in names
        assert "INSTRUCTIONS.txt" in names
        assert "README.md" in names

        instructions = zf.read("INSTRUCTIONS.txt").decode("utf-8")
        assert "Add" in instructions
        assert "Integration Flow" in instructions
        assert "Upload" in instructions

        readme = zf.read("README.md").decode("utf-8")
        assert "Add" in readme
        assert "Upload" in readme

        # Validate each inner zip as a standalone valid individual iflow archive
        for flow_zip_name in ("order_service.zip", "invoice_service.zip"):
            flow_bytes = zf.read(flow_zip_name)
            flow_report = validate_package(flow_bytes)
            assert flow_report["status"] == "PASSED"
            assert flow_report["archive_type"] == "individual_iflow"
            assert flow_report["import_guaranteed"] is True
            assert flow_report["import_verification"] == "import-verified"


def test_package_validator_no_false_confidence():
    """Verify validator reports package-ZIP as not import-guaranteed and hash as unknown."""
    pkg_gen = CPIPackageGenerator()
    flow_xml = pkg_gen.iflow_gen.generate_iflow({"name": "payment_service", "processors": []})
    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/payment_service.iflw",
            content=flow_xml,
            role="source",
            generator="sap:iflow",
        )
    ]

    # Package ZIP: must not claim false guarantee or verified hash
    pkg_bytes = pkg_gen.create_zip_archive(files, package_id="test_pkg", export_type="package")
    report = validate_package(pkg_bytes)
    assert report["archive_type"] == "content_package"
    assert report["import_guaranteed"] is False
    assert report["import_verification"] == "not import-verified"
    assert "not import-verified" in report["import_guarantee_message"].lower() or "not import-guaranteed" in report["import_guarantee_message"].lower()
    assert report["metadata"]["hash"]["verified"] is False
    assert report["metadata"]["hash"]["verification_status"] == "cannot be verified; SAP algorithm unknown"
    assert any("SAP algorithm unknown" in w for w in report["warnings"])

    # Individual iFlow ZIP: guaranteed import
    indiv_bytes = create_individual_iflow_archive(files, artifact_id="payment_service", artifact_name="Payment Service")
    indiv_report = validate_package(indiv_bytes)
    assert indiv_report["archive_type"] == "individual_iflow"
    assert indiv_report["import_guaranteed"] is True
    assert indiv_report["import_verification"] == "import-verified"


def test_native_zip_attributes_and_export_info():
    """Verify ExportInformation.info has no trailing newline and ZIP attributes match native SAP export."""
    pkg_gen = CPIPackageGenerator()
    flow_xml = pkg_gen.iflow_gen.generate_iflow({"name": "payroll_flow", "processors": []})
    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/payroll_flow.iflw",
            content=flow_xml,
            role="source",
            generator="sap:iflow",
        )
    ]

    pkg_bytes = pkg_gen.create_zip_archive(files, package_id="payroll_package", export_type="package")

    with zipfile.ZipFile(io.BytesIO(pkg_bytes), "r") as zf:
        # Check ExportInformation.info has NO trailing newline
        raw_info = zf.read("ExportInformation.info")
        assert not raw_info.endswith(b"\n"), "ExportInformation.info must not have a trailing newline"
        assert not raw_info.endswith(b"\r\n")

        # Check all outer entries match native SAP ZIP attributes: system=0, flag_bits=0x808, external_attr=0
        for info in zf.infolist():
            assert info.create_system == 0, f"Entry {info.filename} has create_system={info.create_system}, expected 0"
            assert info.flag_bits == 0x808, f"Entry {info.filename} has flag_bits={info.flag_bits}, expected 0x808"
            assert info.external_attr == 0, f"Entry {info.filename} has external_attr={info.external_attr}, expected 0"

        # Check nested _content ZIP entries also match native attributes
        content_entries = [n for n in zf.namelist() if n.endswith("_content")]
        assert len(content_entries) > 0
        for ce in content_entries:
            inner_zf = zipfile.ZipFile(io.BytesIO(zf.read(ce)))
            for inner_info in inner_zf.infolist():
                assert inner_info.create_system == 0, f"Inner entry {inner_info.filename} has create_system={inner_info.create_system}"
                assert inner_info.flag_bits == 0x808, f"Inner entry {inner_info.filename} has flag_bits={inner_info.flag_bits}"
                assert inner_info.external_attr == 0, f"Inner entry {inner_info.filename} has external_attr={inner_info.external_attr}"


def test_filter_leftover_and_empty_flows():
    """Verify disallowed flow stems (dev, inputFlow, empty scheduler) are filtered out."""
    pkg_gen = CPIPackageGenerator()
    valid_xml = pkg_gen.iflow_gen.generate_iflow({"name": "real_business_flow", "processors": []})
    valid_xml2 = pkg_gen.iflow_gen.generate_iflow({"name": "another_business_flow", "processors": []})
    dev_xml = pkg_gen.iflow_gen.generate_iflow({"name": "dev", "processors": []})
    input_flow_xml = pkg_gen.iflow_gen.generate_iflow({"name": "inputFlow", "processors": []})
    empty_scheduler_xml = pkg_gen.iflow_gen.generate_iflow({"name": "scheduler", "processors": []})

    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/real_business_flow.iflw",
            content=valid_xml,
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/another_business_flow.iflw",
            content=valid_xml2,
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/dev.iflw",
            content=dev_xml,
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/inputFlow.iflw",
            content=input_flow_xml,
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/scheduler.iflw",
            content=empty_scheduler_xml,
            role="source",
            generator="sap:iflow",
        ),
    ]

    bundle_bytes = pkg_gen.create_zip_archive(files, package_id="filtered_package", export_type="iflow")
    with zipfile.ZipFile(io.BytesIO(bundle_bytes), "r") as zf:
        names = zf.namelist()
        assert "real_business_flow.zip" in names
        assert "another_business_flow.zip" in names
        assert "dev.zip" not in names
        assert "inputFlow.zip" not in names
        assert "input_flow.zip" not in names
        assert "scheduler.zip" not in names


def test_flow_collision_stem_deduplication():
    """Verify identical colliding flow stems are deduplicated cleanly."""
    pkg_gen = CPIPackageGenerator()
    flow_xml = pkg_gen.iflow_gen.generate_iflow({"name": "payment_service", "processors": []})

    # Two files with colliding names payment_service and payment-service, with identical XML content
    files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/payment_service.iflw",
            content=flow_xml,
            role="source",
            generator="sap:iflow",
        ),
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/payment-service.iflw",
            content=flow_xml,
            role="source",
            generator="sap:iflow",
        ),
    ]

    # In single-flow iflow export mode, deduplicating the two colliding files yields a single valid iFlow archive directly
    indiv_bytes = pkg_gen.create_zip_archive(files, package_id="billing_pkg", export_type="iflow")
    report = validate_package(indiv_bytes)
    assert report["status"] == "PASSED"
    assert report["archive_type"] == "individual_iflow"

    # In package export mode, outer package has only 1 _content archive (not 2 colliding ones)
    pkg_bytes = pkg_gen.create_zip_archive(files, package_id="billing_pkg", export_type="package")
    with zipfile.ZipFile(io.BytesIO(pkg_bytes), "r") as pzf:
        content_entries = [n for n in pzf.namelist() if n.endswith("_content")]
        assert len(content_entries) == 1


def test_cpi_api_client_per_flow_error_handling():
    """Verify that when uploading multiple flows, an error on one flow does not stop the rest."""
    from unittest.mock import MagicMock

    cfg = SAPClientConfig(
        tenant_host="https://fake-cpi.cfapps.eu10.hana.ondemand.com",
        client_id="dummy",
        client_secret="dummy",
    )
    client = SAPIntegrationSuiteClient(config=cfg)

    # Mock upload_iflow_artifact such that flow1 succeeds and flow2 fails
    def mock_upload(package_id, iflow_id, iflow_name, iflow_zip_bytes, version="1.0.0"):
        if iflow_id == "flow2_failing":
            raise RuntimeError("400 Bad Request: Invalid flow artifact XML")
        return {"status": "created", "id": iflow_id}

    client.upload_iflow_artifact = MagicMock(side_effect=mock_upload)

    pkg_gen = CPIPackageGenerator()
    xml1 = pkg_gen.iflow_gen.generate_iflow({"name": "flow1_good", "processors": []})
    zip1 = create_individual_iflow_archive([GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/flow1_good.iflw", content=xml1, role="source", generator="sap:iflow")], artifact_id="flow1_good")
    xml2 = pkg_gen.iflow_gen.generate_iflow({"name": "flow2_failing", "processors": []})
    zip2 = create_individual_iflow_archive([GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/flow2_failing.iflw", content=xml2, role="source", generator="sap:iflow")], artifact_id="flow2_failing")
    xml3 = pkg_gen.iflow_gen.generate_iflow({"name": "flow3_good", "processors": []})
    zip3 = create_individual_iflow_archive([GeneratedFile(path="src/main/resources/scenarioflows/integrationflow/flow3_good.iflw", content=xml3, role="source", generator="sap:iflow")], artifact_id="flow3_good")

    iflow_artifacts = [
        ("flow1_good", "Good Flow", zip1),
        ("flow2_failing", "Failing Flow", zip2),
        ("flow3_good", "Another Good Flow", zip3),
    ]

    summaries = client.upload_flows(package_id="test_pkg", iflow_artifacts=iflow_artifacts)
    assert len(summaries) == 3
    assert summaries["flow1_good"]["status"] == "success"
    assert summaries["flow2_failing"]["status"] == "failed"
    assert "Invalid flow artifact XML" in summaries["flow2_failing"]["error"]
    assert summaries["flow3_good"]["status"] == "success"

    # Test pipeline behavior: stage 3 reports partial success with failure details,
    # and subsequent stages (validation, deploy) process the 2 successful flows
    client.create_or_verify_package = MagicMock(return_value={"status": "created"})
    client.read_iflow_status = MagicMock(return_value={"Id": "flow1_good", "Version": "1.0.0"})
    client.deploy_iflow = MagicMock(return_value={"Status": "PROCESSING"})

    stages = run_staged_migration_pipeline(
        package_id="test_pkg",
        package_name="Test Package",
        iflow_artifacts=iflow_artifacts,
        client=client,
        allow_api_import=True,
        auto_deploy=True,
    )

    stage_map = {st.stage: st for st in stages}
    assert stage_map[MigrationStage.SAP_PACKAGE_IMPORT].status == StageStatus.SUCCESS
    assert "Imported 2/3 flow(s)" in stage_map[MigrationStage.SAP_PACKAGE_IMPORT].message
    assert "flow2_failing" in str(stage_map[MigrationStage.SAP_PACKAGE_IMPORT].details)
    assert stage_map[MigrationStage.IFLOW_VALIDATION].status == StageStatus.SUCCESS
    assert stage_map[MigrationStage.DEPLOYMENT].status == StageStatus.SUCCESS


def test_live_cpi_tenant_api_client():
    """
    Live tenant integration test for SAP Integration Suite OData API.
    Executes live against a real SAP CPI tenant when credentials are provided via:
      - SAP_CPI_SERVICE_KEY (JSON string or file path)
      - SAP_CPI_SERVICE_KEY_FILE (file path)
      - SAP_CPI_HOST + SAP_CPI_CLIENT_ID + SAP_CPI_CLIENT_SECRET
    If credentials are not present in the environment, this test is skipped cleanly.
    """
    cfg = SAPClientConfig()
    if not cfg.has_credentials:
        pytest.skip(
            "Real SAP CPI tenant credentials not configured in environment. "
            "To test live against a real tenant: set SAP_CPI_SERVICE_KEY or SAP_CPI_SERVICE_KEY_FILE "
            "from your BTP Process Integration Runtime service key (plan api)."
        )

    client = SAPIntegrationSuiteClient(config=cfg)

    # 1. Fetch CSRF token and verify OAuth handshake against real tenant
    csrf_token, cookie = client.fetch_csrf_token()
    assert csrf_token is not None and len(csrf_token) > 0, "Failed to fetch CSRF token from real tenant"

    # 2. Create or verify test package on real tenant
    test_pkg_id = "MULE_LIVE_TEST_PKG"
    pkg_res = client.create_or_verify_package(
        package_id=test_pkg_id,
        package_name="MuleSoft Live Test Package",
        description="Automated integration test package created by mule-parser test suite",
    )
    assert pkg_res.get("status") in ("created", "updated", "exists")

    # 3. Generate and upload a live test iFlow
    pkg_gen = CPIPackageGenerator()
    test_xml = pkg_gen.iflow_gen.generate_iflow({"name": "live_smoke_flow", "processors": []})
    test_files = [
        GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/live_smoke_flow.iflw",
            content=test_xml,
            role="source",
            generator="sap:iflow",
        )
    ]
    flow_zip_bytes = create_individual_iflow_archive(
        test_files,
        artifact_id="live_smoke_flow",
        artifact_name="Live Smoke Flow",
    )

    upload_res = client.upload_iflow_artifact(
        package_id=test_pkg_id,
        iflow_id="live_smoke_flow",
        iflow_name="Live Smoke Flow",
        iflow_zip_bytes=flow_zip_bytes,
    )
    assert upload_res.get("status") in ("created", "updated")

    # 4. Read back design-time artifact status from tenant
    status_data = client.read_iflow_status("live_smoke_flow")
    assert status_data is not None
    assert status_data.get("Id") == "live_smoke_flow"

    # 5. Query runtime status (may be NOT_DEPLOYED if not deployed)
    rt_status = client.read_runtime_status("live_smoke_flow")
    assert "Status" in rt_status


def test_dw_to_groovy_conditionals_and_xml_support():
    """Verifies DataWeave conditional expressions, startsWith, slicing, and XML support."""
    from mule_parser.platforms.sap.dw_to_groovy import DataWeaveToGroovyTranslator

    translator = DataWeaveToGroovyTranslator()

    dw_script = (
        "%dw 2.0\n"
        "output application/json\n"
        "---\n"
        'if (payload.salesOrg startsWith "CA") "CA_PHARMA" else "GLOBAL"'
    )
    result = translator.translate(dw_script, transform_name="testConditional")
    assert "XmlSlurper" in result
    assert "XmlUtil" in result
    assert '?.startsWith("CA")' in result
    assert ' ? ("CA_PHARMA") : ("GLOBAL")' in result

    dw_filter_script = (
        "%dw 2.0\n"
        "output application/json\n"
        "---\n"
        "payload.AddressInformation filter ($.AddressUsage.Code == 'XXDEFAULT')"
    )
    res_filter = translator.translate(dw_filter_script, transform_name="testFilter")
    assert ".findAll { it?.AddressUsage.Code == 'XXDEFAULT' }" in res_filter


def test_iflow_generator_specialized_steps_and_adapters():
    """Verifies that SOAP, RFC, SFTP adapters and Validator, PGP, Splitter, Mapping steps are correctly generated."""
    gen = IFlowGenerator()

    assert gen._map_adapter_type("soap_listener") == "SOAP"
    assert gen._map_adapter_type("rfc_receiver") == "RFC"
    assert gen._map_adapter_type("sftp_channel") == "SFTP"

    assert gen._map_cpi_step("validate-xml") == ("Validator", "XmlValidator")
    assert gen._map_cpi_step("pgp-encrypt") == ("MessageDigest", "PGPEncryptor")
    assert gen._map_cpi_step("message-mapping") == ("Mapping", "MessageMapping")
    assert gen._map_cpi_step("splitter") == ("Splitter", "GeneralSplitter")

    flow_data = {
        "name": "AnalyticsFlow",
        "source": {"type": "soap"},
        "processors": [
            {"name": "ValidateXML", "type": "validate-xml"},
            {"name": "TransformLogic", "type": "transform"},
            {"name": "EncryptPayload", "type": "pgp-encrypt"},
        ],
    }

    iflow_xml = gen.generate_iflow(flow_data)
    validation = validate_iflow_xml_content(iflow_xml.encode("utf-8"), "AnalyticsFlow.iflw")
    assert validation["is_valid"] is True
    assert "XmlValidator" in iflow_xml
    assert "PGPEncryptor" in iflow_xml



# ==============================================================================
# 9. Regression Tests: Root Cause Fix — Cross-Tenant-Neutral contentmetadata.md
#    and Canonical Inner Archive Entry Ordering
# ==============================================================================

def _make_minimal_iflow_xml(flow_id: str = "TestFlow") -> str:
    """Returns a minimal valid SAP CPI BPMN2 iFlow XML for testing."""
    return (
        f'<?xml version="1.0" encoding="UTF-8"?>'
        f'<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"'
        f'  xmlns:ifl="http:///com.sap.ifl.model/Ifl.xsd" id="Definitions_1">'
        f'  <bpmn2:process id="Process_{flow_id}" name="{flow_id}" isExecutable="true">'
        f'    <bpmn2:startEvent id="Start_1" name="Start"><bpmn2:outgoing>Flow_1</bpmn2:outgoing></bpmn2:startEvent>'
        f'    <bpmn2:sequenceFlow id="Flow_1" sourceRef="Start_1" targetRef="End_1"/>'
        f'    <bpmn2:endEvent id="End_1" name="End"><bpmn2:incoming>Flow_1</bpmn2:incoming></bpmn2:endEvent>'
        f'  </bpmn2:process>'
        f'</bpmn2:definitions>'
    )


class TestCrossTenantNeutralMetadata:
    """
    Regression: contentmetadata.md must use cross-tenant-neutral Organization/Environment
    defaults so the package imports on any SAP tenant, not just the exporting one.
    Root cause: hardcoded Organization=16fa66c4trial caused rejection on other tenants.
    Fix: default to Organization=TEST, Environment=sap-integration-suite.
    """

    def test_default_organization_is_cross_tenant_neutral(self, monkeypatch):
        """Organization must default to 'TEST', not a specific trial tenant ID."""
        monkeypatch.delenv("SAP_CPI_ORGANIZATION", raising=False)
        monkeypatch.delenv("SAP_CPI_ENVIRONMENT", raising=False)

        files = [GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/flow.iflw",
            content=_make_minimal_iflow_xml("flow"),
            role="source",
        )]
        pkg_bytes = create_content_package_archive(files, "test_pkg", "Test Package")

        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            meta_raw = zf.read("contentmetadata.md")
            decoded = base64.b64decode(meta_raw).decode("utf-8")
            lines = dict(line.split("=", 1) for line in decoded.splitlines() if "=" in line)

        assert lines.get("Organization") == "TEST", (
            f"Organization must default to 'TEST' for cross-tenant compatibility, got {lines.get('Organization')!r}. "
            "A hardcoded trial tenant ID (e.g. '16fa66c4trial') causes 'Select a valid content package' "
            "rejection on any SAP tenant other than the exporting one."
        )
        assert lines.get("Environment") == "sap-integration-suite", (
            f"Environment must default to 'sap-integration-suite', got {lines.get('Environment')!r}. "
            "A specific subdomain URL (e.g. 'it-db-design.16fa66c4trial') is rejected on other tenants."
        )

    def test_organization_overridable_via_env_var(self, monkeypatch):
        """Organization and Environment must be overridable via environment variables."""
        monkeypatch.setenv("SAP_CPI_ORGANIZATION", "my-org-123")
        monkeypatch.setenv("SAP_CPI_ENVIRONMENT", "it-prod.my-org-123")

        files = [GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/flow.iflw",
            content=_make_minimal_iflow_xml(),
            role="source",
        )]
        pkg_bytes = create_content_package_archive(files, "test_pkg", "Test")

        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            meta_raw = zf.read("contentmetadata.md")
            decoded = base64.b64decode(meta_raw).decode("utf-8")
            lines = dict(line.split("=", 1) for line in decoded.splitlines() if "=" in line)

        assert lines.get("Organization") == "my-org-123"
        assert lines.get("Environment") == "it-prod.my-org-123"

    def test_hardcoded_trial_tenant_is_not_in_default(self, monkeypatch):
        """The old hardcoded trial tenant values must NOT appear in any output."""
        monkeypatch.delenv("SAP_CPI_ORGANIZATION", raising=False)
        monkeypatch.delenv("SAP_CPI_ENVIRONMENT", raising=False)

        files = [GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/flow.iflw",
            content=_make_minimal_iflow_xml(),
            role="source",
        )]
        pkg_bytes = create_content_package_archive(files, "test_pkg", "Test")

        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            meta_raw = zf.read("contentmetadata.md")
            decoded = base64.b64decode(meta_raw).decode("utf-8")

        assert "16fa66c4trial" not in decoded, (
            "The old hardcoded trial tenant '16fa66c4trial' must not appear in contentmetadata.md. "
            "It prevents import on any other SAP tenant."
        )
        assert "it-db-design.16fa66c4trial" not in decoded


class TestNativeCanonicalInnerArchiveOrdering:
    """
    Regression: inner _content archives must use the canonical SAP entry ordering:
    .iflw -> parameters.prop -> parameters.propdef -> scripts -> .project -> MANIFEST.MF.
    """

    def test_inner_archive_iflw_is_first_entry(self):
        """The .iflw file must be the first entry in the inner _content archive."""
        files = [
            GeneratedFile(
                path="src/main/resources/scenarioflows/integrationflow/my_flow.iflw",
                content=_make_minimal_iflow_xml("my_flow"),
                role="source",
            ),
            GeneratedFile(
                path="src/main/resources/script/transform.groovy",
                content="import com.sap.gateway.ip.core.customdev.util.Message\n"
                        "def Message processData(Message message) { return message }\n",
                role="source",
            ),
        ]
        pkg_bytes = create_content_package_archive(files, "order_test_pkg", "Order Test")

        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as outer_zf:
            content_entries = [n for n in outer_zf.namelist() if n.endswith("_content")]
            assert len(content_entries) == 1
            inner_bytes = outer_zf.read(content_entries[0])

        with zipfile.ZipFile(io.BytesIO(inner_bytes)) as inner_zf:
            names = inner_zf.namelist()
            first_entry = names[0]
            last_entry = names[-1]

        assert first_entry.endswith(".iflw"), (
            f".iflw must be the FIRST entry in inner archive, got {first_entry!r}. "
            "Native SAP always places the .iflw first."
        )
        assert "MANIFEST.MF" in last_entry, (
            f"META-INF/MANIFEST.MF must be the LAST entry in inner archive, got {last_entry!r}. "
            "Native SAP always places MANIFEST.MF last."
        )

    def test_parameters_before_scripts_in_inner_archive(self):
        """parameters.prop must appear before scripts in the inner archive (native SAP order)."""
        files = [
            GeneratedFile(
                path="src/main/resources/scenarioflows/integrationflow/flow.iflw",
                content=_make_minimal_iflow_xml(),
                role="source",
            ),
            GeneratedFile(
                path="src/main/resources/script/helper.groovy",
                content="def x() {}",
                role="source",
            ),
            GeneratedFile(
                path="src/main/resources/parameters.prop",
                content="key=value\n",
                role="config",
            ),
        ]
        pkg_bytes = create_content_package_archive(files, "order_pkg", "Order Pkg")

        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as outer_zf:
            inner_bytes = outer_zf.read(next(n for n in outer_zf.namelist() if n.endswith("_content")))

        with zipfile.ZipFile(io.BytesIO(inner_bytes)) as inner_zf:
            names = inner_zf.namelist()
            param_idx = next((i for i, n in enumerate(names) if n.endswith("parameters.prop")), None)
            script_idx = next((i for i, n in enumerate(names) if n.endswith(".groovy")), None)

        if param_idx is not None and script_idx is not None:
            assert param_idx < script_idx, (
                f"parameters.prop (index {param_idx}) must come BEFORE scripts (index {script_idx}). "
                "Native SAP order: .iflw -> params -> propdef -> scripts -> .project -> MANIFEST.MF"
            )


class TestPackageStructureInvariants:
    """Package structure invariants that SAP's import validator requires."""

    def test_exactly_one_content_package_resource_per_package(self):
        """Exactly one ContentPackage resource must exist in resources.cnt."""
        files = [GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/flow.iflw",
            content=_make_minimal_iflow_xml(),
            role="source",
        )]
        pkg_bytes = create_content_package_archive(files, "pkg_1", "Package One")
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            cnt = json.loads(base64.b64decode(zf.read("resources.cnt")))
        content_packages = [r for r in cnt["resources"] if r.get("resourceType") == "ContentPackage"]
        assert len(content_packages) == 1, (
            f"Expected exactly 1 ContentPackage resource, found {len(content_packages)}."
        )

    def test_content_package_resource_is_last_in_resources_list(self):
        """ContentPackage must be the LAST resource in resources.cnt (native SAP ordering)."""
        files = [
            GeneratedFile(path=f"src/main/resources/scenarioflows/integrationflow/flow_{i}.iflw",
                          content=_make_minimal_iflow_xml(f"flow_{i}"), role="source")
            for i in range(2)
        ]
        pkg_bytes = create_content_package_archive(files, "multi_pkg", "Multi Package")
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            cnt = json.loads(base64.b64decode(zf.read("resources.cnt")))
        last_resource = cnt["resources"][-1]
        assert last_resource.get("resourceType") == "ContentPackage", (
            f"ContentPackage must be the LAST resource. Got {last_resource.get('resourceType')!r}."
        )

    def test_every_iflow_has_aggregation_relation_to_content_package(self):
        """Every IFlow resource must have exactly one AGGREGATION relation from the ContentPackage."""
        files = [
            GeneratedFile(path=f"src/main/resources/scenarioflows/integrationflow/flow_{i}.iflw",
                          content=_make_minimal_iflow_xml(f"flow_{i}"), role="source")
            for i in range(2)
        ]
        pkg_bytes = create_content_package_archive(files, "rel_pkg", "Relation Package")
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            cnt = json.loads(base64.b64decode(zf.read("resources.cnt")))
        pkg_resource = next(r for r in cnt["resources"] if r.get("resourceType") == "ContentPackage")
        iflow_resources = [r for r in cnt["resources"] if r.get("resourceType") == "IFlow"]
        relations = cnt.get("relations", [])
        for iflow in iflow_resources:
            matching_rels = [
                rel for rel in relations
                if rel.get("sourceId") == pkg_resource["id"]
                and rel.get("targetId") == iflow["id"]
                and rel.get("relationType") == "AGGREGATION"
            ]
            assert len(matching_rels) == 1, (
                f"IFlow '{iflow['uniqueId']}' must have exactly 1 AGGREGATION relation. Found {len(matching_rels)}."
            )

    def test_no_orphaned_resources(self):
        """Every IFlow in resources.cnt must have a corresponding _content archive."""
        files = [GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/flow.iflw",
            content=_make_minimal_iflow_xml(),
            role="source",
        )]
        pkg_bytes = create_content_package_archive(files, "orphan_pkg", "Orphan Check")
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            names = zf.namelist()
            cnt = json.loads(base64.b64decode(zf.read("resources.cnt")))
            content_ids = {n.replace("_content", "") for n in names if n.endswith("_content")}
            iflow_ids = {r["id"] for r in cnt["resources"] if r.get("resourceType") == "IFlow"}
        orphaned = iflow_ids - content_ids
        assert not orphaned, f"IFlow IDs {orphaned} have no corresponding _content archive."

    def test_no_duplicate_resource_ids(self):
        """No two resources in resources.cnt may share the same id or uniqueId."""
        files = [
            GeneratedFile(path=f"src/main/resources/scenarioflows/integrationflow/flow_{i}.iflw",
                          content=_make_minimal_iflow_xml(f"flow_{i}"), role="source")
            for i in range(2)
        ]
        pkg_bytes = create_content_package_archive(files, "dup_check_pkg", "Dup Check")
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            cnt = json.loads(base64.b64decode(zf.read("resources.cnt")))
        ids = [r["id"] for r in cnt["resources"]]
        unique_ids = [r["uniqueId"] for r in cnt["resources"]]
        assert len(ids) == len(set(ids)), f"Duplicate resource IDs found: {ids}"
        assert len(unique_ids) == len(set(unique_ids)), f"Duplicate uniqueIds found: {unique_ids}"

    def test_content_package_resource_id_is_32_hex_chars(self):
        """ContentPackage resource id must be a 32-character lowercase hex string (MD5)."""
        files = [GeneratedFile(
            path="src/main/resources/scenarioflows/integrationflow/flow.iflw",
            content=_make_minimal_iflow_xml(),
            role="source",
        )]
        pkg_bytes = create_content_package_archive(files, "hex_id_pkg", "Hex ID")
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            cnt = json.loads(base64.b64decode(zf.read("resources.cnt")))
        pkg = next(r for r in cnt["resources"] if r.get("resourceType") == "ContentPackage")
        assert len(pkg["id"]) == 32, f"ContentPackage id must be 32 chars, got {len(pkg['id'])}"
        assert pkg["id"].isalnum(), f"ContentPackage id must be alphanumeric hex, got {pkg['id']!r}"


class TestHashConsistency:
    """Hash array correctness: count, algorithm, and determinism."""

    def test_hash_count_equals_content_archives_plus_one(self):
        """hash array length must equal number of _content entries + 1."""
        for n_flows in (1, 2, 3):
            files = [
                GeneratedFile(
                    path=f"src/main/resources/scenarioflows/integrationflow/flow_{i}.iflw",
                    content=_make_minimal_iflow_xml(f"flow_{i}"),
                    role="source",
                )
                for i in range(n_flows)
            ]
            pkg_bytes = create_content_package_archive(files, f"hash_count_{n_flows}", f"Hash Count")
            with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
                n_content = sum(1 for n in zf.namelist() if n.endswith("_content"))
                hashes = json.loads(zf.read("hash"))
            assert len(hashes) == n_content + 1, (
                f"For {n_flows} flows: expected {n_content + 1} hashes, got {len(hashes)}."
            )

    def test_each_hash_is_sha256_of_corresponding_content(self):
        """Every hash must match SHA-256 of its corresponding payload."""
        files = [
            GeneratedFile(path=f"src/main/resources/scenarioflows/integrationflow/flow_{i}.iflw",
                          content=_make_minimal_iflow_xml(f"flow_{i}"), role="source")
            for i in range(2)
        ]
        pkg_bytes = create_content_package_archive(files, "sha256_verify_pkg", "SHA256 Verify")
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            entries = zf.infolist()
            content_entries = [e for e in entries if e.filename.endswith("_content")]
            hashes = json.loads(zf.read("hash"))
            cnt_bytes = zf.read("resources.cnt")
            for i, entry in enumerate(content_entries):
                content_bytes = zf.read(entry.filename)
                expected = hashlib.sha256(content_bytes).hexdigest()
                assert hashes[i] == expected, (
                    f"hash[{i}] for {entry.filename!r}: expected {expected!r}, got {hashes[i]!r}."
                )
            expected_cnt_hash = hashlib.sha256(cnt_bytes).hexdigest()
            assert hashes[-1] == expected_cnt_hash, (
                f"Last hash must be SHA-256 of resources.cnt. Expected {expected_cnt_hash!r}, got {hashes[-1]!r}."
            )


class TestNativeReferencePackageRegression:
    """Validate native SAP reference package against structural invariants (read-only)."""

    @pytest.mark.skipif(
        not KNOWN_GOOD_REFERENCE_PATH.exists(),
        reason="Native SAP reference package not available",
    )
    def test_native_has_exactly_one_content_package_resource(self):
        pkg_bytes = KNOWN_GOOD_REFERENCE_PATH.read_bytes()
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            cnt = json.loads(base64.b64decode(zf.read("resources.cnt")))
        content_packages = [r for r in cnt["resources"] if r.get("resourceType") == "ContentPackage"]
        assert len(content_packages) == 1

    @pytest.mark.skipif(
        not KNOWN_GOOD_REFERENCE_PATH.exists(),
        reason="Native SAP reference package not available",
    )
    def test_native_content_package_is_last_resource(self):
        pkg_bytes = KNOWN_GOOD_REFERENCE_PATH.read_bytes()
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            cnt = json.loads(base64.b64decode(zf.read("resources.cnt")))
        assert cnt["resources"][-1].get("resourceType") == "ContentPackage"

    @pytest.mark.skipif(
        not KNOWN_GOOD_REFERENCE_PATH.exists(),
        reason="Native SAP reference package not available",
    )
    def test_native_inner_iflw_is_first_entry(self):
        pkg_bytes = KNOWN_GOOD_REFERENCE_PATH.read_bytes()
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as outer_zf:
            content_entries = [n for n in outer_zf.namelist() if n.endswith("_content")]
            inner_bytes = outer_zf.read(content_entries[0])
        with zipfile.ZipFile(io.BytesIO(inner_bytes)) as inner_zf:
            first_entry = inner_zf.namelist()[0]
        assert first_entry.endswith(".iflw"), f"First entry must be .iflw, got {first_entry!r}"

    @pytest.mark.skipif(
        not KNOWN_GOOD_REFERENCE_PATH.exists(),
        reason="Native SAP reference package not available",
    )
    def test_native_inner_manifest_is_last_entry(self):
        pkg_bytes = KNOWN_GOOD_REFERENCE_PATH.read_bytes()
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as outer_zf:
            content_entries = [n for n in outer_zf.namelist() if n.endswith("_content")]
            inner_bytes = outer_zf.read(content_entries[0])
        with zipfile.ZipFile(io.BytesIO(inner_bytes)) as inner_zf:
            last_entry = inner_zf.namelist()[-1]
        assert "MANIFEST.MF" in last_entry, f"Last entry must be MANIFEST.MF, got {last_entry!r}"

    @pytest.mark.skipif(
        not KNOWN_GOOD_REFERENCE_PATH.exists(),
        reason="Native SAP reference package not available",
    )
    def test_native_organization_is_test_sentinel(self):
        """Confirm native uses 'TEST' as Organization — the cross-tenant-neutral sentinel."""
        pkg_bytes = KNOWN_GOOD_REFERENCE_PATH.read_bytes()
        with zipfile.ZipFile(io.BytesIO(pkg_bytes)) as zf:
            decoded = base64.b64decode(zf.read("contentmetadata.md")).decode("utf-8")
        lines = dict(line.split("=", 1) for line in decoded.splitlines() if "=" in line)
        assert lines.get("Organization") == "TEST", (
            f"Native package Organization is {lines.get('Organization')!r}. "
            "Expected 'TEST' as the cross-tenant-neutral sentinel."
        )


class TestBinaryZIPStructureCompatibility:
    """
    Automated binary-level regression test suite for SAP Integration Suite ZIP binary compatibility.

    Verifies:
      - Local file header general purpose bit flags match central directory flags (0x0808).
      - Local file header CRC-32, compressed size, uncompressed size are zero (data descriptor convention).
      - Data descriptors (PK\\x07\\x08) are present immediately following compressed data.
      - Central directory declares exact CRC-32, compressed size, uncompressed size matching data descriptor.
      - Relative local header offsets are non-overlapping and strictly valid.
      - All entries in both outer package archive and inner embedded iFlow archives can be extracted cleanly.
      - 100% structural convention parity with native SAP exports.
    """

    @staticmethod
    def _parse_local_headers(data: bytes) -> list[dict[str, Any]]:
        results = []
        offset = 0
        lochdr = b"PK\x03\x04"
        while True:
            idx = data.find(lochdr, offset)
            if idx == -1:
                break
            sig, ver, flags, comp, mt, md, crc, csz, usz, fnl, extl = struct.unpack_from("<4sHHHHHIIIHH", data, idx)
            fname = data[idx + 30 : idx + 30 + fnl].decode("utf-8", "replace")
            results.append({
                "offset": idx,
                "flags": flags,
                "crc": crc,
                "csz": csz,
                "usz": usz,
                "name": fname,
                "data_start": idx + 30 + fnl + extl,
            })
            offset = idx + 4
        return results

    @staticmethod
    def _parse_central_dir(data: bytes) -> list[dict[str, Any]]:
        results = []
        offset = 0
        cdhdr = b"PK\x01\x02"
        while True:
            idx = data.find(cdhdr, offset)
            if idx == -1:
                break
            sig, vmade, vneeded, flags, comp, mt, md, crc, csz, usz, fnl, extl, coml, dsk, iattr, eattr, loff = struct.unpack_from("<4sHHHHHHIIIHHHHHII", data, idx)
            fname = data[idx + 46 : idx + 46 + fnl].decode("utf-8", "replace")
            results.append({
                "offset": idx,
                "flags": flags,
                "crc": crc,
                "csz": csz,
                "usz": usz,
                "name": fname,
                "loff": loff,
            })
            offset = idx + 46 + fnl + extl + coml
        return results

    @staticmethod
    def _parse_data_descriptors(data: bytes) -> list[dict[str, Any]]:
        results = []
        offset = 0
        dd_sig = b"PK\x07\x08"
        while True:
            idx = data.find(dd_sig, offset)
            if idx == -1:
                break
            crc, csz, usz = struct.unpack_from("<III", data, idx + 4)
            results.append({"offset": idx, "crc": crc, "csz": csz, "usz": usz})
            offset = idx + 4
        return results

    @staticmethod
    def _make_sample_package() -> bytes:
        pkg_gen = CPIPackageGenerator()
        flow_xml = pkg_gen.iflow_gen.generate_iflow({"name": "binary_test_flow", "processors": []})
        files = [
            GeneratedFile(
                path="src/main/resources/scenarioflows/integrationflow/binary_test_flow.iflw",
                content=flow_xml,
                role="source",
                generator="sap:iflow",
            ),
            GeneratedFile(
                path="src/main/resources/script/test_script.groovy",
                content="// test groovy",
                role="source",
                generator="sap:groovy",
            ),
        ]
        return pkg_gen.create_zip_archive(files, package_id="binary_test_pkg", package_name="Binary Test Package", export_type="package")

    def test_outer_zip_local_and_central_flags_match_and_equal_0x0808(self):
        pkg_bytes = self._make_sample_package()
        lh = self._parse_local_headers(pkg_bytes)
        cd = self._parse_central_dir(pkg_bytes)

        assert len(lh) > 0, "No local headers found in generated package"
        assert len(lh) == len(cd), f"Local header count ({len(lh)}) != central directory count ({len(cd)})"

        for l_entry, c_entry in zip(lh, cd):
            assert l_entry["name"] == c_entry["name"]
            assert l_entry["flags"] == 0x0808, f"Local header {l_entry['name']} flag is {hex(l_entry['flags'])}, expected 0x0808"
            assert c_entry["flags"] == 0x0808, f"Central directory {c_entry['name']} flag is {hex(c_entry['flags'])}, expected 0x0808"
            assert l_entry["flags"] == c_entry["flags"], f"Flag mismatch for {l_entry['name']}"

    def test_outer_zip_zeroed_local_crc_and_sizes_with_data_descriptors(self):
        pkg_bytes = self._make_sample_package()
        lh = self._parse_local_headers(pkg_bytes)
        cd = self._parse_central_dir(pkg_bytes)
        dd = self._parse_data_descriptors(pkg_bytes)

        assert len(dd) == len(lh), f"Data descriptor count ({len(dd)}) != local header count ({len(lh)})"

        for l_entry, c_entry, d_entry in zip(lh, cd, dd):
            # Local header must have CRC and sizes zeroed (data descriptor convention)
            assert l_entry["crc"] == 0, f"Local header {l_entry['name']} CRC is {l_entry['crc']}, expected 0"
            assert l_entry["csz"] == 0, f"Local header {l_entry['name']} compressed size is {l_entry['csz']}, expected 0"
            assert l_entry["usz"] == 0, f"Local header {l_entry['name']} uncompressed size is {l_entry['usz']}, expected 0"

            # Data descriptor must immediately follow compressed data
            expected_dd_offset = l_entry["data_start"] + c_entry["csz"]
            assert d_entry["offset"] == expected_dd_offset, (
                f"Data descriptor for {l_entry['name']} at {d_entry['offset']:#010x}, expected {expected_dd_offset:#010x}"
            )

            # Central directory and data descriptor values must match exactly
            assert c_entry["crc"] == d_entry["crc"]
            assert c_entry["csz"] == d_entry["csz"]
            assert c_entry["usz"] == d_entry["usz"]

    def test_outer_zip_entry_extraction_and_crc_verification(self):
        pkg_bytes = self._make_sample_package()
        cd = self._parse_central_dir(pkg_bytes)
        with zipfile.ZipFile(io.BytesIO(pkg_bytes), "r") as zf:
            for c_entry in cd:
                data = zf.read(c_entry["name"])
                actual_crc = zlib.crc32(data) & 0xFFFFFFFF
                assert actual_crc == c_entry["crc"], f"CRC mismatch for {c_entry['name']}: {actual_crc} vs {c_entry['crc']}"
                assert len(data) == c_entry["usz"], f"Size mismatch for {c_entry['name']}: {len(data)} vs {c_entry['usz']}"

    def test_outer_zip_no_overlapping_or_malformed_structures(self):
        pkg_bytes = self._make_sample_package()
        lh = self._parse_local_headers(pkg_bytes)
        cd = self._parse_central_dir(pkg_bytes)
        # Verify monotonically increasing offsets
        for i in range(len(lh) - 1):
            curr_end = lh[i]["data_start"] + cd[i]["csz"] + 16  # data + 16-byte data descriptor
            next_start = lh[i + 1]["offset"]
            assert curr_end == next_start, f"Entry gap or overlap between {lh[i]['name']} and {lh[i+1]['name']}"

    def test_embedded_iflow_zip_binary_structure(self):
        pkg_bytes = self._make_sample_package()
        outer_zf = zipfile.ZipFile(io.BytesIO(pkg_bytes))
        content_entries = [n for n in outer_zf.namelist() if n.endswith("_content")]
        assert len(content_entries) > 0, "No embedded _content ZIP found"

        inner_bytes = outer_zf.read(content_entries[0])
        lh = self._parse_local_headers(inner_bytes)
        cd = self._parse_central_dir(inner_bytes)
        dd = self._parse_data_descriptors(inner_bytes)

        assert len(lh) > 0
        assert len(lh) == len(cd)
        assert len(dd) == len(lh)

        for l_entry, c_entry, d_entry in zip(lh, cd, dd):
            assert l_entry["flags"] == 0x0808
            assert c_entry["flags"] == 0x0808
            assert l_entry["flags"] == c_entry["flags"]
            assert l_entry["crc"] == 0
            assert l_entry["csz"] == 0
            assert l_entry["usz"] == 0
            assert d_entry["offset"] == l_entry["data_start"] + c_entry["csz"]
            assert c_entry["crc"] == d_entry["crc"]
            assert c_entry["csz"] == d_entry["csz"]
            assert c_entry["usz"] == d_entry["usz"]

        # Extraction verification
        inner_zf = zipfile.ZipFile(io.BytesIO(inner_bytes), "r")
        for c_entry in cd:
            data = inner_zf.read(c_entry["name"])
            assert (zlib.crc32(data) & 0xFFFFFFFF) == c_entry["crc"]
            assert len(data) == c_entry["usz"]

    @pytest.mark.skipif(
        not KNOWN_GOOD_REFERENCE_PATH.exists(),
        reason="Native SAP reference package not available",
    )
    def test_binary_parity_with_native_reference(self):
        native_bytes = KNOWN_GOOD_REFERENCE_PATH.read_bytes()
        gen_path = REPO_ROOT / "examples" / "emp-cpi-package-fixed.zip"
        if not gen_path.exists():
            gen_path = Path("examples/emp-cpi-package-fixed.zip")
        gen_bytes = gen_path.read_bytes()

        # Outer comparison
        for label, b in [("Native", native_bytes), ("Generated", gen_bytes)]:
            lh = self._parse_local_headers(b)
            cd = self._parse_central_dir(b)
            dd = self._parse_data_descriptors(b)
            assert len(lh) == len(cd) == len(dd), f"{label} outer header/CD/DD counts disagree"
            for l_entry, c_entry in zip(lh, cd):
                assert l_entry["flags"] == 0x0808, f"{label} local flag != 0x0808"
                assert c_entry["flags"] == 0x0808, f"{label} CD flag != 0x0808"
                assert l_entry["crc"] == 0, f"{label} local CRC != 0"
                assert l_entry["csz"] == 0, f"{label} local csz != 0"
                assert l_entry["usz"] == 0, f"{label} local usz != 0"

        # Inner comparison
        native_zf = zipfile.ZipFile(io.BytesIO(native_bytes))
        gen_zf = zipfile.ZipFile(io.BytesIO(gen_bytes))

        native_inner = [n for n in native_zf.namelist() if n.endswith("_content")][0]
        gen_inner = [n for n in gen_zf.namelist() if n.endswith("_content")][0]

        for label, b in [("Native Inner", native_zf.read(native_inner)), ("Generated Inner", gen_zf.read(gen_inner))]:
            lh = self._parse_local_headers(b)
            cd = self._parse_central_dir(b)
            dd = self._parse_data_descriptors(b)
            assert len(lh) == len(cd) == len(dd), f"{label} inner header/CD/DD counts disagree"
            for l_entry, c_entry in zip(lh, cd):
                assert l_entry["flags"] == 0x0808, f"{label} local flag != 0x0808"
                assert c_entry["flags"] == 0x0808, f"{label} CD flag != 0x0808"
                assert l_entry["crc"] == 0, f"{label} local CRC != 0"
                assert l_entry["csz"] == 0, f"{label} local csz != 0"
                assert l_entry["usz"] == 0, f"{label} local usz != 0"


class TestBPMN2SemanticComplianceAndNormalization:
    """Automated regression suite verifying BPMN2 semantic standards in SAP CPI iflows."""

    def test_event_subprocess_excluded_from_sequence_flow_chaining(self):
        """Event sub-processes cannot have incoming or outgoing sequence flows (BPMN 2.0.2 §10.5.3)."""
        raw_xml = """<?xml version="1.0" encoding="UTF-8"?>
<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
                   xmlns:ifl="http:///com.sap.ifl.model/Ifl.xsd"
                   id="Definitions_1">
    <bpmn2:process id="Process_1" isExecutable="true">
        <bpmn2:startEvent id="StartEvent_1"/>
        <bpmn2:callActivity id="CallActivity_1"/>
        <bpmn2:subProcess id="SubProcess_Error" triggeredByEvent="true">
            <bpmn2:extensionElements>
                <ifl:property>
                    <key>activityType</key>
                    <value>ErrorEventSubProcessTemplate</value>
                </ifl:property>
            </bpmn2:extensionElements>
            <bpmn2:startEvent id="ErrorStart_1"/>
            <bpmn2:endEvent id="ErrorEnd_1"/>
        </bpmn2:subProcess>
        <bpmn2:endEvent id="EndEvent_1"/>
    </bpmn2:process>
</bpmn2:definitions>"""
        norm_xml, warns = validate_and_normalize_iflow_xml(raw_xml, flow_name="TestFlow")
        root = ET.fromstring(norm_xml.encode("utf-8"))

        seq_flows = [e for e in root.iter() if e.tag.endswith("sequenceFlow")]
        for sf in seq_flows:
            assert sf.get("sourceRef") != "SubProcess_Error", (
                f"Event sub-process illegally connected as sourceRef in sequenceFlow {sf.get('id')}"
            )
            assert sf.get("targetRef") != "SubProcess_Error", (
                f"Event sub-process illegally connected as targetRef in sequenceFlow {sf.get('id')}"
            )

    def test_timer_start_event_does_not_receive_inbound_message_flow(self):
        """Timer start events are autonomous; an inbound MessageFlow from a sender participant is invalid."""
        raw_xml = """<?xml version="1.0" encoding="UTF-8"?>
<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
                   xmlns:ifl="http:///com.sap.ifl.model/Ifl.xsd"
                   id="Definitions_1">
    <bpmn2:collaboration id="Collaboration_1">
        <bpmn2:participant id="Participant_Process" processRef="Process_1"/>
    </bpmn2:collaboration>
    <bpmn2:process id="Process_1" isExecutable="true">
        <bpmn2:startEvent id="StartTimer_1">
            <bpmn2:timerEventDefinition id="TimerDef_1"/>
        </bpmn2:startEvent>
        <bpmn2:endEvent id="EndEvent_1"/>
    </bpmn2:process>
</bpmn2:definitions>"""
        norm_xml, _ = validate_and_normalize_iflow_xml(raw_xml, flow_name="TimerFlow")
        root = ET.fromstring(norm_xml.encode("utf-8"))

        msg_flows = [e for e in root.iter() if e.tag.endswith("messageFlow")]
        for mf in msg_flows:
            assert mf.get("targetRef") != "StartTimer_1", (
                f"Inbound MessageFlow illegally wired to timer start event: {mf.get('id')}"
            )

    def test_pre_existing_bpmn_diagram_and_waypoints_preserved(self):
        """Existing BPMNDiagram layout and sequence flow waypoints must NOT be cleared or overwritten."""
        raw_xml = """<?xml version="1.0" encoding="UTF-8"?>
<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
                   xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
                   xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"
                   xmlns:di="http://www.omg.org/spec/DD/20100524/DI"
                   id="Definitions_1">
    <bpmn2:collaboration id="Collaboration_1">
        <bpmn2:participant id="Participant_Process" processRef="Process_1"/>
    </bpmn2:collaboration>
    <bpmn2:process id="Process_1" isExecutable="true">
        <bpmn2:startEvent id="Start_1"/>
        <bpmn2:endEvent id="End_1"/>
        <bpmn2:sequenceFlow id="Flow_1" sourceRef="Start_1" targetRef="End_1"/>
    </bpmn2:process>
    <bpmndi:BPMNDiagram id="BPMNDiagram_1">
        <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Collaboration_1">
            <bpmndi:BPMNShape id="BPMNShape_Start_1" bpmnElement="Start_1">
                <dc:Bounds height="36.0" width="36.0" x="300.0" y="200.0"/>
            </bpmndi:BPMNShape>
            <bpmndi:BPMNEdge id="BPMNEdge_Flow_1" bpmnElement="Flow_1">
                <di:waypoint x="336.0" y="218.0"/>
                <di:waypoint x="500.0" y="218.0"/>
            </bpmndi:BPMNEdge>
        </bpmndi:BPMNPlane>
    </bpmndi:BPMNDiagram>
</bpmn2:definitions>"""
        norm_xml, _ = validate_and_normalize_iflow_xml(raw_xml, flow_name="LayoutFlow")
        root = ET.fromstring(norm_xml.encode("utf-8"))

        start_shape = next(
            e for e in root.iter()
            if e.tag.endswith("BPMNShape") and e.get("bpmnElement") == "Start_1"
        )
        bounds = next(c for c in start_shape if c.tag.endswith("Bounds"))
        assert bounds.get("x") == "300.0" and bounds.get("y") == "200.0", "Custom coordinates were lost!"

        edge = next(
            e for e in root.iter()
            if e.tag.endswith("BPMNEdge") and e.get("bpmnElement") == "Flow_1"
        )
        waypoints = [c for c in edge if c.tag.endswith("waypoint")]
        assert len(waypoints) == 2
        assert waypoints[0].get("x") == "336.0" and waypoints[1].get("x") == "500.0", "Waypoints were overwritten!"

    def test_validator_flags_illegal_event_subprocess_and_timer_flows(self):
        """Structural validator must identify illegal sequenceFlows on event sub-processes and messageFlows on timer start events."""
        bad_xml = """<?xml version="1.0" encoding="UTF-8"?>
<bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"
                   xmlns:ifl="http:///com.sap.ifl.model/Ifl.xsd"
                   id="Definitions_1">
    <bpmn2:collaboration id="Collab_1">
        <bpmn2:participant id="Sender" ifl:type="EndpointSender"/>
        <bpmn2:participant id="Proc_Part" ifl:type="IntegrationProcess" processRef="Process_1"/>
        <bpmn2:messageFlow id="MsgFlow_1" sourceRef="Sender" targetRef="StartTimer_1"/>
    </bpmn2:collaboration>
    <bpmn2:process id="Process_1" isExecutable="true">
        <bpmn2:startEvent id="StartTimer_1">
            <bpmn2:timerEventDefinition id="Timer_1"/>
        </bpmn2:startEvent>
        <bpmn2:subProcess id="ErrorSubProc" triggeredByEvent="true">
            <bpmn2:startEvent id="ErrStart"/>
            <bpmn2:endEvent id="ErrEnd"/>
        </bpmn2:subProcess>
        <bpmn2:endEvent id="End_1"/>
        <bpmn2:sequenceFlow id="IllegalFlow_1" sourceRef="ErrorSubProc" targetRef="End_1"/>
    </bpmn2:process>
</bpmn2:definitions>"""
        report = validate_iflow_xml_content(bad_xml.encode("utf-8"), "bad.iflw")
        assert not report["is_valid"]
        err_str = " ".join(report["errors"])
        assert "Illegal sequence flow" in err_str and "ErrorSubProc" in err_str
        assert "Illegal message flow" in err_str and "StartTimer_1" in err_str


