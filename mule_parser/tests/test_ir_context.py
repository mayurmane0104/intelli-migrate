"""
Unit tests for ``services.ir_context`` — the IR slicer that grounds the LLM
on the analysis layer before code generation.

These tests exercise the slicing logic directly (no DB, no HTTP, no FastAPI
TestClient) by handing the service a synthetic IR. The contract under test
is the dict shape returned to the FastAPI ``/internal/migration/stream-file``
endpoint and rendered into the LLM prompt by ``prompt_loader``.
"""

from __future__ import annotations

from mule_parser.ir.models import (
    IntermediateRepresentation,
    ProjectIdentity,
    StructuralLayer,
    SemanticLayer,
    ExecutionLayer,
    QualityLayer,
    GapLayer,
    IRFile,
    IRFlow,
    IRComponent,
    IRConfig,
    IRSemanticFlow,
    IREntryPoint,
    IRPropertyUsage,
    IRTransformation,
    IRRiskFlag,
)
from mule_parser.services.ir_context import (
    build_generation_context,
    _to_env_var,
)


def _build_sample_ir() -> IntermediateRepresentation:
    """
    Build a small but representative IR with two files:

      src/main/mule/customer-flow.xml
        flow `customer-import`
          - http listener / orders
          - flow-ref → `validate-contact-sub` (in the same file)
          - salesforce:create using ${sfdc.user}/${sfdc.password}
        flow `validate-contact-sub` (sub-flow)
          - choice + log

      src/main/mule/order-flow.xml
        flow `order-import`
          - flow-ref → `customer-import` (calls into the file under test)
    """
    return IntermediateRepresentation(
        project_identity=ProjectIdentity(name="customer-sync", source_type="zip", application_archetype="apiled"),
        structural_layer=StructuralLayer(
            files=[
                IRFile(path="src/main/mule/customer-flow.xml", file_type="mule-config"),
                IRFile(path="src/main/mule/order-flow.xml", file_type="mule-config"),
            ],
            flows=[
                IRFlow(name="customer-import", flow_type="flow", file="src/main/mule/customer-flow.xml"),
                IRFlow(name="validate-contact-sub", flow_type="sub-flow", file="src/main/mule/customer-flow.xml"),
                IRFlow(name="order-import", flow_type="flow", file="src/main/mule/order-flow.xml"),
            ],
            components=[
                IRComponent(
                    step_id="customer-import::1",
                    flow_name="customer-import",
                    type="http:listener",
                    name="listener",
                    config_ref="HTTP_Listener_Config",
                    attributes={"path": "/customers"},
                    file="src/main/mule/customer-flow.xml",
                ),
                IRComponent(
                    step_id="customer-import::2",
                    flow_name="customer-import",
                    type="flow-ref",
                    name="validate-contact-sub",
                    attributes={"name": "validate-contact-sub"},
                    file="src/main/mule/customer-flow.xml",
                ),
                IRComponent(
                    step_id="customer-import::3",
                    flow_name="customer-import",
                    type="salesforce:create",
                    name="create-contact",
                    config_ref="Salesforce_Config",
                    attributes={"type": "Contact"},
                    file="src/main/mule/customer-flow.xml",
                    property_refs=["sfdc.user", "sfdc.password"],
                ),
                IRComponent(
                    step_id="order-import::1",
                    flow_name="order-import",
                    type="flow-ref",
                    name="customer-import",
                    attributes={"name": "customer-import"},
                    file="src/main/mule/order-flow.xml",
                ),
            ],
            configs=[
                IRConfig(
                    name="Salesforce_Config",
                    connector_type="salesforce",
                    auth_type="basic",
                    properties={"username": "${sfdc.user}", "password": "${sfdc.password}"},
                    file="src/main/mule/customer-flow.xml",
                ),
                IRConfig(
                    name="HTTP_Listener_Config",
                    connector_type="http",
                    properties={"port": "${http.port}"},
                    file="src/main/mule/customer-flow.xml",
                ),
            ],
        ),
        semantic_layer=SemanticLayer(
            flows=[
                IRSemanticFlow(
                    name="customer-import",
                    purpose="Import customers into Salesforce",
                    business_logic_summary="HTTP-triggered customer import with validation",
                    integration_pattern="api-led",
                    trigger_type="http",
                    confidence=0.9,
                    detected_patterns=["api-led", "validate-then-write"],
                    connectors=["http", "salesforce"],
                ),
            ],
            transformations=[
                IRTransformation(
                    transformation_id="t1",
                    flow_name="customer-import",
                    script_id="map-customer",
                    source_field="firstname",
                    target_field="FirstName",
                    transformation_type="rename",
                    data_type="string",
                    expression="$.firstname",
                    confidence=1.0,
                ),
            ],
            property_usage=[
                IRPropertyUsage(
                    key="sfdc.user",
                    used_in_flows=["customer-import"],
                    is_secure=False,
                    defined_in_file="src/main/resources/application.properties",
                    value_masked="admin@example.com",
                ),
                IRPropertyUsage(
                    key="sfdc.password",
                    used_in_flows=["customer-import"],
                    is_secure=True,
                    defined_in_file="src/main/resources/application.properties",
                    value_masked="***",
                ),
            ],
        ),
        execution_layer=ExecutionLayer(
            entry_points=[
                IREntryPoint(flow_name="customer-import", trigger_type="http", path="/customers"),
            ],
        ),
        quality_layer=QualityLayer(
            risk_flags=[
                IRRiskFlag(
                    severity="MEDIUM",
                    category="missing-error-handler",
                    flow_name="customer-import",
                    description="No on-error-continue handler",
                ),
            ],
        ),
        gap_layer=GapLayer(
            behavior_contracts=[
                {"flow_name": "customer-import", "preconditions": ["payload is JSON"], "postconditions": ["Contact created"]},
            ],
            feasibility_decision={"verdict": "FEASIBLE", "confidence": 0.85, "blockers": [], "warnings": []},
        ),
    )


# ─── Slicing ──────────────────────────────────────────────────────────────────


def test_build_generation_context_slices_by_file_path():
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="src/main/mule/customer-flow.xml",
        ir=ir,
    )

    assert ctx is not None
    assert ctx["available"] is True
    assert ctx["scope"]["file_path"] == "src/main/mule/customer-flow.xml"
    assert ctx["scope"]["total_flows_in_project"] == 3
    assert set(ctx["scope"]["matched_flows"]) == {"customer-import", "validate-contact-sub"}


def test_build_generation_context_returns_none_without_ir_or_project():
    # No ir, no project_id, no analysis_job_id → can't enrich.
    ctx = build_generation_context(
        project_id=None, file_name="x.xml", file_path="x.xml", ir=None
    )
    assert ctx is None


def test_build_generation_context_returns_none_when_file_unknown():
    """
    The file isn't part of the project. We should still return the envelope
    so the LLM gets the project-level context, but matched_flows is empty.
    """
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="unrelated.xml",
        file_path="some/other/dir/unrelated.xml",
        ir=ir,
    )
    assert ctx is not None
    assert ctx["scope"]["matched_flows"] == []
    assert ctx["flows_in_file"] == []
    # Project-level summary is still useful for the LLM:
    assert ctx["project_identity"]["name"] == "customer-sync"


def test_build_generation_context_tolerates_bare_filename():
    """Caller may have only the basename — tail-match should still work."""
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="customer-flow.xml",
        ir=ir,
    )
    assert ctx is not None
    assert "customer-import" in ctx["scope"]["matched_flows"]


# ─── Per-flow context ─────────────────────────────────────────────────────────


def test_flow_in_file_contains_resolved_refs_and_entry_point():
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="src/main/mule/customer-flow.xml",
        ir=ir,
    )
    flow = next(f for f in ctx["flows_in_file"] if f["name"] == "customer-import")

    assert flow["purpose"].startswith("Import customers")
    assert flow["trigger_type"] == "http"
    assert flow["entry_point"]["path"] == "/customers"
    assert flow["flow_refs_resolved"] == ["validate-contact-sub"]
    assert flow["integration_pattern"] == "api-led"
    assert flow["risk_flags"][0]["category"] == "missing-error-handler"
    assert flow["behavior_contract"].get("preconditions") == ["payload is JSON"]


def test_flow_in_file_lists_connectors_with_operations():
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="src/main/mule/customer-flow.xml",
        ir=ir,
    )
    flow = next(f for f in ctx["flows_in_file"] if f["name"] == "customer-import")
    connectors = {c["connector_type"]: c for c in flow["connectors_used"]}

    assert "salesforce" in connectors
    assert "create" in connectors["salesforce"]["operations"]
    assert "http" in connectors
    assert "listener" in connectors["http"]["operations"]


def test_flow_properties_map_to_upper_snake_env_vars():
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="src/main/mule/customer-flow.xml",
        ir=ir,
    )
    flow = next(f for f in ctx["flows_in_file"] if f["name"] == "customer-import")
    by_key = {p["key"]: p for p in flow["properties_used"]}

    assert by_key["sfdc.user"]["env_var"] == "SFDC_USER"
    assert by_key["sfdc.user"]["is_secure"] is False
    assert by_key["sfdc.password"]["env_var"] == "SFDC_PASSWORD"
    assert by_key["sfdc.password"]["is_secure"] is True


def test_flow_transformations_are_structured_field_mappings():
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="src/main/mule/customer-flow.xml",
        ir=ir,
    )
    flow = next(f for f in ctx["flows_in_file"] if f["name"] == "customer-import")
    assert flow["transformations"]
    t = flow["transformations"][0]
    assert t["source_field"] == "firstname"
    assert t["target_field"] == "FirstName"
    assert t["transformation_type"] == "rename"


# ─── Cross-file edges + integration manifest ──────────────────────────────────


def test_cross_flow_inbound_relationships_are_surfaced():
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="src/main/mule/customer-flow.xml",
        ir=ir,
    )
    inbound = ctx["cross_flow_relationships"]["inbound"]
    # order-import (in the OTHER file) calls customer-import.
    assert any(
        edge["caller_flow"] == "order-import" and edge["called_flow"] == "customer-import"
        for edge in inbound
    )


def test_integration_manifest_redacts_secrets_but_lists_refs():
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="src/main/mule/customer-flow.xml",
        ir=ir,
    )
    sf_cfg = next(c for c in ctx["integration_manifest"] if c["connector_type"] == "salesforce")
    assert sf_cfg["auth_type"] == "basic"
    # ``sfdc.password`` is_secure=True, so it should appear in ``secret_refs``.
    assert "sfdc.password" in sf_cfg["secret_refs"]
    # The actual values must not leak into the manifest.
    assert all(not isinstance(v, str) or "${" not in v for v in sf_cfg.values() if not isinstance(v, list))


def test_property_mapping_aggregates_across_flows():
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="src/main/mule/customer-flow.xml",
        ir=ir,
    )
    assert "sfdc.user" in ctx["property_mapping"]
    assert ctx["property_mapping"]["sfdc.password"]["is_secure"] is True


def test_feasibility_summary_is_included():
    ir = _build_sample_ir()
    ctx = build_generation_context(
        project_id="proj-X",
        file_name="customer-flow.xml",
        file_path="src/main/mule/customer-flow.xml",
        ir=ir,
    )
    assert ctx["feasibility"]["verdict"] == "FEASIBLE"
    assert ctx["feasibility"]["confidence"] == 0.85


# ─── env-var slugifier ────────────────────────────────────────────────────────


def test_to_env_var_slugifies_dotted_and_hyphenated_keys():
    assert _to_env_var("sfdc.client.id") == "SFDC_CLIENT_ID"
    assert _to_env_var("api-base-url") == "API_BASE_URL"
    assert _to_env_var("__weird__key") == "WEIRD_KEY"
    assert _to_env_var("alreadyUpper") == "ALREADYUPPER"
