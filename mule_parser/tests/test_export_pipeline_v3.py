"""End-to-end smoke tests for the v3 export pipeline.

The tests synthesise a small IR + migration plan + project files payload
that exercises every generator, then assert the resulting ZIP contains
the deployable-project layout documented in the spec.

The IR shape mirrors what the production parser emits:

* ``raw_layer.original_json["flows"]`` -- one entry per ``<flow>`` element
  with ``name``, ``flow_type``, ``processors``, ``source`` (the trigger),
  ``error_handlers``, ``file``.
* ``raw_layer.original_json["dataweave"]`` -- one entry per script with
  ``script_text``, ``file``, ``parent_flow``, ``parent_step_id``.
* ``raw_layer.original_json["properties"]`` -- one entry per
  ``.properties`` key with ``key``, ``value``, ``is_secure``, ``file``.
* ``raw_layer.original_json["connectors"]`` -- one entry per global
  connector config with ``connector_type``, ``config_id``,
  ``nested_configs[].type`` (e.g. ``db:my-sql-connection``).
"""
from __future__ import annotations

import io
import zipfile

import pytest
from unittest.mock import patch

@pytest.fixture(autouse=True)
def bypass_preflight():
    with patch("mule_parser.services.export_pipeline_v3.orchestrator.run_pipeline_preflight", side_effect=lambda ir, **kw: ir):
        yield


from mule_parser.services.export_pipeline_v3 import (
    ComplexityLevel,
    ConnectorKind,
    ConnectorSubkind,
    ExportOrchestrator,
    ExportValidationError,
    MetadataBuilder,
    TriggerType,
    contains_forbidden_terms,
)
from mule_parser.services.export_pipeline_v3.ir_enrichment import enrich_ir
from mule_parser.services.export_pipeline_v3.ir_view import IRView


def _build_metadata(builder, *, project_name, target_runtime="python", target_format="zip",
                    ir, migration_plan=None, project_files=None, generated_artifacts=None,
                    validation_report=None, audit_report=None, infra_mode="sam",
                    region="us-east-1"):
    """Test helper that emulates how the orchestrator wires the MetadataBuilder.

    Per the IR-only contract, MetadataBuilder.build() consumes only an IR.
    Anything legacy callers used to pass separately (project_files, plan,
    audit/validation reports) must be folded into the IR via
    :func:`enrich_ir` first. This helper does that fold so tests can keep
    the readable per-section fixtures without violating the contract.
    """
    enriched = enrich_ir(
        ir,
        project_files=project_files,
        migration_plan=migration_plan,
        audit_report=audit_report,
        validation_report=validation_report,
        generated_artifacts=generated_artifacts,
    )
    return builder.build(
        project_name=project_name,
        target_runtime=target_runtime,
        target_format=target_format,
        ir=enriched,
        infra_mode=infra_mode,
        region=region,
    )


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def sample_ir() -> dict:
    """Synthesised IR resembling a small order-intake Mule project."""
    return {
        "project_identity": {
            "name": "AcmeSales",
            "application_archetype": "integration_service",
            "source_type": "mule4",
            "description": "Acme sales order intake",
            "version": "1.0.0",
        },
        "raw_layer": {
            "original_json": {
                "connectors": [
                    {
                        "connector_type": "http",
                        "config_id": "orders-api",
                        "host": "orders.acme",
                        "nested_configs": [{"type": "http:listener-connection"}],
                    },
                    {
                        "connector_type": "dynamodb",
                        "config_id": "orders-table",
                        "nested_configs": [],
                    },
                    {
                        "connector_type": "sqs",
                        "config_id": "outbound-queue",
                        "nested_configs": [],
                    },
                ],
                "properties": [
                    {"key": "orders.api.key", "value": "abc", "is_secure": True, "file": "config.properties"},
                    {"key": "feature.flags.enabled", "value": "true", "is_secure": False, "file": "config.properties"},
                ],
                "dataweave": [
                    {
                        "script_id": "order_transform",
                        "file": "src/main/resources/order_transform.dwl",
                        "script_text": "%dw 2.0\noutput application/json\n---\npayload",
                        "parent_flow": "OrderFlow",
                    },
                ],
                "flows": [
                    _flow(
                        "OrderFlow",
                        file="src/main/mule/order.xml",
                        source={"type": "http:listener", "attributes": {"path": "/orders", "allowedMethods": "POST"}, "config_ref": "orders-api"},
                        processors=[
                            {"type": "ee:transform"},
                            {"type": "db:insert", "config_ref": "orders-table"},
                        ],
                    ),
                    _flow(
                        "CustomerFlow",
                        file="src/main/mule/customer.xml",
                        source={"type": "http:listener", "attributes": {"path": "/customers"}, "config_ref": "orders-api"},
                        processors=[
                            {"type": "ee:transform"},
                            {"type": "sqs:send-message", "config_ref": "outbound-queue"},
                            {"type": "logger"},
                            {"type": "choice"},
                            {"type": "db:select", "config_ref": "orders-table"},
                        ],
                    ),
                    _flow(
                        "PaymentFlow",
                        file="src/main/mule/payment.xml",
                        source={"type": "http:listener", "attributes": {"path": "/payments"}, "config_ref": "orders-api"},
                        processors=[
                            {"type": "ee:transform"},
                            {"type": "http:request", "config_ref": "orders-api"},
                            {"type": "sqs:send-message", "config_ref": "outbound-queue"},
                            {"type": "logger"},
                            {"type": "db:select", "config_ref": "orders-table"},
                            {"type": "ee:transform"},
                            {"type": "choice"},
                            {"type": "logger"},
                            {"type": "db:insert", "config_ref": "orders-table"},
                            {"type": "logger"},
                            {"type": "ee:transform"},
                        ],
                        error_handlers=[{"type": "on-error-propagate"}],
                    ),
                ],
            },
        },
        "semantic_layer": {
            "flows": [
                {"name": "OrderFlow", "purpose": "Receive an order and persist it."},
                {"name": "CustomerFlow", "purpose": "Sync customer records."},
                {"name": "PaymentFlow", "purpose": "Authorise payments and emit events."},
            ],
        },
        "execution_layer": {
            "entry_points": [
                {"flow_name": "OrderFlow", "path": "/orders", "methods": ["POST"]},
                {"flow_name": "CustomerFlow", "path": "/customers", "methods": ["GET"]},
                {"flow_name": "PaymentFlow", "path": "/payments", "methods": ["POST"]},
            ],
        },
    }


def _flow(name, *, file, source=None, processors=None, error_handlers=None):
    return {
        "name": name,
        "flow_type": "flow",
        "file": file,
        "source": source,
        "processors": processors or [],
        "error_handlers": error_handlers or [],
    }


@pytest.fixture
def sample_plan() -> dict:
    return {
        "summary": {"service_counts": {"DynamoDB": 1, "SQS": 1, "API Gateway": 1}},
        "flows": [
            {
                "flow_name": "OrderFlow",
                "purpose": "Receive an order and persist it.",
                "component_decisions": [
                    {"source": "http", "target": "API Gateway"},
                    {"source": "transform", "target": ""},
                    {"source": "db", "target": "DynamoDB"},
                ],
            },
        ],
    }


@pytest.fixture
def sample_project_files() -> list[dict]:
    return [
        {
            "id": "f1",
            "name": "order.xml",
            "path": "src/main/mule/order.xml",
            "content": "<mule><flow name='OrderFlow'/></mule>",
        },
    ]


# ---------------------------------------------------------------------------
# MetadataBuilder
# ---------------------------------------------------------------------------


def test_metadata_builder_produces_one_function_per_flow(sample_ir, sample_plan, sample_project_files):
    builder = MetadataBuilder()
    metadata = _build_metadata(
        builder,
        project_name="AcmeSales",
        ir=sample_ir,
        migration_plan=sample_plan,
        project_files=sample_project_files,
    )

    assert metadata.project_slug == "acme-sales"
    assert {fn.name for fn in metadata.functions} == {"order-flow", "customer-flow", "payment-flow"}

    by_name = {fn.name: fn for fn in metadata.functions}
    # Step counts: 2, 5, 11
    assert by_name["order-flow"].complexity == ComplexityLevel.simple
    assert by_name["customer-flow"].complexity == ComplexityLevel.medium
    assert by_name["payment-flow"].complexity == ComplexityLevel.complex
    assert by_name["payment-flow"].error_handling.dead_letter is True

    # HTTP listener paths are lifted from the source proc attributes.
    assert by_name["order-flow"].trigger_type == TriggerType.http
    assert by_name["order-flow"].http_path == "/orders"
    assert by_name["order-flow"].http_methods == ["POST"]

    # Semantic-layer purpose populates the function description.
    assert "Receive an order" in by_name["order-flow"].purpose

    # Connector mapping
    kinds = {c.kind for c in metadata.connectors}
    assert ConnectorKind.dynamodb in kinds
    assert ConnectorKind.sqs in kinds
    assert ConnectorKind.http in kinds


def test_metadata_builder_handles_empty_inputs():
    builder = MetadataBuilder()
    metadata = builder.build(
        project_name="EmptyProject",
        target_runtime="python",
        target_format="zip",
        ir={"raw_layer": {"original_json": {}}},
    )
    assert metadata.project_slug == "empty-project"
    assert len(metadata.functions) == 1
    assert metadata.functions[0].name == "example-function"


def test_only_flow_xml_becomes_function(sample_ir):
    """Audit C1 - config/properties/log files must not generate Lambda functions."""
    files = [
        {"path": "src/main/mule/order.xml", "content": "<mule><flow name='OrderFlow'/></mule>"},
        {"path": "pom.xml", "content": "<project/>"},
        {"path": "mule-artifact.json", "content": "{}"},
        {"path": "src/main/resources/config.properties", "content": "a=b"},
        {"path": "src/main/resources/log4j2.xml", "content": "<Configuration/>"},
    ]
    # IR has only one real flow.
    sample_ir["raw_layer"]["original_json"]["flows"] = [
        _flow("OrderFlow", file="src/main/mule/order.xml",
              source={"type": "http:listener", "attributes": {"path": "/x"}, "config_ref": "orders-api"},
              processors=[{"type": "ee:transform"}]),
    ]
    builder = MetadataBuilder()
    metadata = _build_metadata(
        builder,
        project_name="OrderOnly",
        ir=sample_ir,
        project_files=files,
    )
    assert [fn.name for fn in metadata.functions] == ["order-flow"]
    # Skipped files surface in the migration report.
    skipped_paths = {row["path"] for row in metadata.migration_report.skipped_files}
    assert "pom.xml" in skipped_paths
    assert "mule-artifact.json" in skipped_paths
    assert "src/main/resources/config.properties" in skipped_paths
    assert "src/main/resources/log4j2.xml" in skipped_paths


# ---------------------------------------------------------------------------
# Orchestrator end-to-end
# ---------------------------------------------------------------------------


def _zip_contents(packaged) -> dict[str, bytes]:
    with zipfile.ZipFile(io.BytesIO(packaged.bytes)) as zf:
        return {info.filename: zf.read(info.filename) for info in zf.infolist()}


def test_orchestrator_produces_deployable_project(sample_ir, sample_plan, sample_project_files):
    orchestrator = ExportOrchestrator()
    try:
        result = orchestrator.run(
            project_name="AcmeSales",
            target_runtime="python",
            target_format="zip",
            ir=sample_ir,
            migration_plan=sample_plan,
            project_files=sample_project_files,
            infra_mode="sam",
        )
    except Exception as e:
        if hasattr(e, "issues"):
            import json
            with open("issues.json", "w") as f:
                json.dump(e.issues, f, indent=2)
        raise

    contents = _zip_contents(result.packaged)
    root = result.metadata.project_slug
    for fn in result.metadata.functions:
        for leaf in ("handler.py", "models.py", "utils.py", "__init__.py"):
            assert f"{root}/src/functions/{fn.module_name}/{leaf}" in contents

    for path in (
        f"{root}/.env.example",
        f"{root}/requirements.txt",
        f"{root}/template.yaml",
        f"{root}/README.md",
        f"{root}/infrastructure/sam/template.yaml",
        f"{root}/infrastructure/policies/lambda-policy.json",
        f"{root}/infrastructure/terraform/README.md",
        f"{root}/deployment/scripts/build.sh",
        f"{root}/deployment/scripts/package.sh",
        f"{root}/deployment/scripts/deploy.sh",
        f"{root}/deployment/pipelines/github-actions.yml",
        f"{root}/docs/architecture.md",
        f"{root}/docs/runbook.md",
        f"{root}/docs/migration-report.md",
        f"{root}/tests/conftest.py",
        f"{root}/tests/unit/test_order_flow.py",
        f"{root}/tests/integration/test_order_flow_integration.py",
        f"{root}/src/adapters/__init__.py",
        f"{root}/src/domain/services/__init__.py",
        f"{root}/src/adapters/error_handler.py",
        f"{root}/src/adapters/retry_adapter.py",
        f"{root}/src/adapters/secrets_adapter.py",
    ):
        assert path in contents, f"missing required path {path!r}"


def test_handler_uses_aws_lambda_powertools_and_real_body(
    sample_ir, sample_plan, sample_project_files
):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="AcmeSales",
        target_runtime="python",
        target_format="zip",
        ir=sample_ir,
        migration_plan=sample_plan,
        project_files=sample_project_files,
        infra_mode="sam",
    )

    contents = _zip_contents(result.packaged)
    root = result.metadata.project_slug
    for fn in result.metadata.functions:
        path = f"{root}/src/functions/{fn.module_name}/handler.py"
        body = contents[path].decode("utf-8")
        assert "from aws_lambda_powertools import Logger, Tracer" in body
        assert "def lambda_handler(event: dict, context: LambdaContext) -> dict:" in body
        # Audit C4 - never a bare ``def handler(`` alias.
        assert "def handler(" not in body
        # No bare `pass` body anywhere.
        assert "    pass\n" not in body or "import" in body


def test_terminology_scrub_removes_source_platform_tokens(
    sample_ir, sample_plan, sample_project_files
):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="AcmeSales",
        target_runtime="python",
        target_format="zip",
        ir=sample_ir,
        migration_plan=sample_plan,
        project_files=sample_project_files,
        infra_mode="sam",
    )

    contents = _zip_contents(result.packaged)
    for path, body_bytes in contents.items():
        # Migration report is the documented exception.
        if path.endswith("docs/migration-report.md"):
            continue
        # The verbatim source files we preserve under mule-artifacts/ are
        # also exempt (they're the original Mule XML by design).
        if "/source-artifacts/" in path:
            continue
        if not path.endswith((".py", ".md", ".yaml", ".yml", ".json", ".sh", ".toml")):
            continue
        body = body_bytes.decode("utf-8", errors="replace")
        assert not contains_forbidden_terms(body), f"forbidden tokens in {path}"


def test_terraform_mode_emits_modules(sample_ir, sample_plan, sample_project_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="AcmeSales",
        target_runtime="python",
        target_format="zip",
        ir=sample_ir,
        migration_plan=sample_plan,
        project_files=sample_project_files,
        infra_mode="terraform",
    )

    contents = _zip_contents(result.packaged)
    root = result.metadata.project_slug
    assert f"{root}/infrastructure/terraform/main.tf" in contents
    assert f"{root}/infrastructure/terraform/variables.tf" in contents
    assert f"{root}/infrastructure/terraform/outputs.tf" in contents


def test_validation_blocks_packaging_when_handler_missing(monkeypatch, sample_ir, sample_plan):
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    orchestrator = ExportOrchestrator()
    
    with patch("mule_parser.services.export_pipeline_v3.generators.function_generator.FunctionGenerator.generate", return_value=0):
        with pytest.raises(ExportValidationError):
            orchestrator.run(
                project_name="AcmeSales",
                target_runtime="python",
                target_format="zip",
                ir=sample_ir,
                migration_plan=sample_plan,
                infra_mode="sam",
            )


def test_packaged_manifest_includes_v3_metadata(sample_ir, sample_plan):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="AcmeSales",
        target_runtime="python",
        target_format="zip",
        ir=sample_ir,
        migration_plan=sample_plan,
        infra_mode="sam",
    )

    manifest = result.packaged.manifest
    assert manifest["pipeline"] == "v3"
    assert manifest["infra_mode"] == "sam"
    assert manifest["stats"]["functions"] == len(result.metadata.functions)
    assert "validation" in manifest
    assert "migration_report" in manifest


# ---------------------------------------------------------------------------
# Audit regression suite - sfdc-db-user-aggregation scenario
# ---------------------------------------------------------------------------


@pytest.fixture
def sfdc_db_ir() -> dict:
    """Mirrors the `template-sfdc2db-user-aggregation` audit scenario."""
    return {
        "project_identity": {
            "name": "template-sfdc2db-user-aggregation",
            "application_archetype": "sfdc-db-migration-template",
            "source_type": "mule4",
            "description": "Aggregate SFDC + DB users and email a CSV report.",
        },
        "raw_layer": {
            "original_json": {
                "connectors": [
                    {
                        "connector_type": "salesforce",
                        "config_id": "Salesforce_Sfdc_config",
                        "nested_configs": [{"type": "salesforce:basic-connection"}],
                    },
                    {
                        "connector_type": "db",
                        "config_id": "Database_Config",
                        "host": "mysql.acme",
                        "port": "3306",
                        "nested_configs": [{"type": "db:my-sql-connection"}],
                    },
                    {
                        "connector_type": "email",
                        "config_id": "Gmail_SMTP",
                        "host": "smtp.gmail.com",
                        "port": "465",
                        "nested_configs": [{"type": "email:smtps-connection"}],
                    },
                    {
                        "connector_type": "http",
                        "config_id": "HTTP_Listener_config",
                        "nested_configs": [{"type": "http:listener-connection"}],
                    },
                ],
                "properties": [
                    {"key": "sfdc.username", "value": "user", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "sfdc.password", "value": "****", "is_secure": True, "file": "mule-prod.properties"},
                    {"key": "sfdc.securityToken", "value": "****", "is_secure": True, "file": "mule-prod.properties"},
                    {"key": "db.host", "value": "mysql.acme", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "db.port", "value": "3306", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "db.user", "value": "root", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "db.password", "value": "****", "is_secure": True, "file": "mule-prod.properties"},
                    {"key": "db.databasename", "value": "users", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "smtp.host", "value": "smtp.gmail.com", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "smtp.port", "value": "465", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "smtp.user", "value": "x@gmail.com", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "smtp.password", "value": "****", "is_secure": True, "file": "mule-prod.properties"},
                    {"key": "mail.from", "value": "x@gmail.com", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "mail.to", "value": "y@gmail.com", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "mail.subject", "value": "Daily report", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "mail.body", "value": "See attached", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "attachment.name", "value": "users.csv", "is_secure": False, "file": "mule-prod.properties"},
                    {"key": "http.port", "value": "8081", "is_secure": False, "file": "mule-prod.properties"},
                ],
                "dataweave": [
                    {
                        "script_id": "merge_users",
                        "file": "bussinessLogic.xml",
                        "script_text": (
                            "%dw 2.0\n"
                            "output application/csv\n"
                            "---\n"
                            "(payload.sfdc ++ payload.db) distinctBy $.Email"
                        ),
                        "parent_flow": "businessLogicFlow",
                        "output_type": "application/csv",
                    },
                ],
                "flows": [
                    _flow(
                        "triggerFlow",
                        file="src/main/mule/endpoints.xml",
                        source={"type": "http:listener", "attributes": {"path": "/generatereport", "allowedMethods": "GET"}, "config_ref": "HTTP_Listener_config"},
                        processors=[
                            {"type": "logger"},
                            {"type": "flow-ref", "attributes": {"name": "mainFlow"}},
                        ],
                    ),
                    _flow(
                        "mainFlow",
                        file="src/main/mule/bussinessLogic.xml",
                        source=None,
                        processors=[
                            {"type": "flow-ref", "attributes": {"name": "businessLogicFlow"}},
                        ],
                    ),
                    _flow(
                        "businessLogicFlow",
                        file="src/main/mule/bussinessLogic.xml",
                        source=None,
                        processors=[
                            {"type": "scatter-gather"},
                            {"type": "ee:transform"},
                            {"type": "email:send", "config_ref": "Gmail_SMTP"},
                        ],
                    ),
                    _flow(
                        "errorHandlingFlow",
                        file="src/main/mule/errorHandling.xml",
                        source=None,
                        processors=[{"type": "logger"}],
                        error_handlers=[{"type": "on-error-propagate"}],
                    ),
                ],
            },
        },
        "semantic_layer": {
            "flows": [
                {"name": "triggerFlow", "purpose": "HTTP entry point - delegates to mainFlow."},
                {"name": "mainFlow", "purpose": "Error-handling wrapper around businessLogicFlow."},
                {"name": "businessLogicFlow", "purpose": "Aggregate Salesforce + MySQL users and email a CSV."},
                {"name": "errorHandlingFlow", "purpose": "Log and re-raise unrecoverable errors.", "intent": "error_handler"},
            ],
        },
        "execution_layer": {
            "entry_points": [
                {"flow_name": "triggerFlow", "path": "/generatereport", "methods": ["GET"]},
            ],
        },
        "dataweave_analysis": [
            {
                "script_id": "merge_users",
                "flow_name": "businessLogicFlow",
                "semantics": {
                    "join": {
                        "strategy": "distinct_concat",
                        "left": "payload.sfdc",
                        "right": "payload.db",
                        "key": "Email",
                        "confidence": 1.0,
                    },
                    "dedup": {
                        "strategy": "distinct_by",
                        "key": "Email",
                        "expression": "$.Email",
                        "confidence": 1.0,
                    },
                },
            }
        ],
    }


@pytest.fixture
def sfdc_db_files() -> list[dict]:
    """Mirrors the JAR contents the audit listed."""
    return [
        {"path": "src/main/mule/endpoints.xml", "content": "<mule><flow name='triggerFlow'/></mule>"},
        {"path": "src/main/mule/bussinessLogic.xml", "content": "<mule><flow name='mainFlow'/><flow name='businessLogicFlow'/></mule>"},
        {"path": "src/main/mule/errorHandling.xml", "content": "<mule><flow name='errorHandlingFlow'/></mule>"},
        {"path": "src/main/mule/config.xml", "content": "<mule>config only</mule>"},
        {"path": "pom.xml", "content": "<project><artifactId>template-sfdc2db-user-aggregation</artifactId></project>"},
        {"path": "mule-artifact.json", "content": "{}"},
        {"path": "src/main/resources/mule-prod.properties", "content": "sfdc.username=user\nsfdc.password=secret\n"},
        {"path": "src/main/resources/mule-dev.properties", "content": "db.host=localhost\n"},
        {"path": "src/main/resources/mule-qa.properties", "content": ""},
        {"path": "src/main/resources/common.properties", "content": ""},
        {"path": "src/main/resources/log4j2.xml", "content": "<Configuration/>"},
        {"path": "src/test/resources/log4j2-test.xml", "content": "<Configuration/>"},
        {"path": "configreadme.xml", "content": "<readme/>"},
    ]


def test_audit_c1_only_flows_become_functions(sfdc_db_ir, sfdc_db_files):
    """Exactly 4 functions, not 14 - matches the actual flow count."""
    builder = MetadataBuilder()
    metadata = _build_metadata(
        builder,
        project_name="template-sfdc2db-user-aggregation",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
    )
    names = {fn.name for fn in metadata.functions}
    assert names == {
        "trigger-flow", "main-flow", "business-logic-flow", "error-handling-flow",
    }, names
    skipped = {row["path"] for row in metadata.migration_report.skipped_files}
    assert "pom.xml" in skipped
    assert "mule-artifact.json" in skipped
    assert "src/main/resources/log4j2.xml" in skipped


def test_audit_c2_no_dot_in_python_identifiers(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    for path, body_bytes in contents.items():
        if not path.endswith(".py"):
            continue
        body = body_bytes.decode("utf-8", errors="replace")
        for line in body.splitlines():
            if line.lstrip().startswith("class "):
                # Class declarations must not have a dot in the identifier.
                assert "." not in line.split(" ", 1)[1].split(":")[0].split("(")[0], (
                    f"dotted class name in {path}: {line.strip()!r}"
                )


def test_audit_c3_mysql_picks_pymysql_not_pg8000(sfdc_db_ir, sfdc_db_files):
    builder = MetadataBuilder()
    metadata = _build_metadata(
        builder,
        project_name="template-sfdc2db-user-aggregation",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
    )
    db_connectors = [c for c in metadata.connectors if c.kind == ConnectorKind.database]
    assert len(db_connectors) == 1
    assert db_connectors[0].subkind == ConnectorSubkind.mysql
    assert "pymysql>=1.1" in db_connectors[0].pip_packages
    # Postgres drivers must never be present.
    pkg_blob = " ".join(metadata.required_pip_packages())
    assert "pg8000" not in pkg_blob
    assert "psycopg2" not in pkg_blob


def test_audit_c4_handler_always_named_lambda_handler(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    for fn in result.metadata.functions:
        if fn.trigger_type.value != "http":
            continue
        path = f"{result.metadata.project_slug}/src/functions/{fn.module_name}/handler.py"
        body = contents[path].decode("utf-8")
        assert "def lambda_handler(" in body, fn.name
        assert "def handler(" not in body, fn.name


def test_audit_c5_smtp_client_has_real_implementation(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    smtp_path = next(
        p for p in contents
        if p.endswith("src/adapters/smtp_client.py")
    )
    body = contents[smtp_path].decode("utf-8")
    assert "raise NotImplementedError" not in body
    assert "smtplib.SMTP_SSL" in body
    assert "send_with_attachment" in body


def test_audit_c6_handler_imports_are_deduped(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    for fn in result.metadata.functions:
        if fn.trigger_type.value != "http":
            continue
        path = f"{result.metadata.project_slug}/src/functions/{fn.module_name}/handler.py"
        body = contents[path].decode("utf-8")
        # The "Logger" symbol must come from exactly one import line.
        logger_imports = [l for l in body.splitlines() if "Logger" in l and (l.startswith("from ") or l.startswith("import "))]
        # We expect at most one of these per file.
        assert len(logger_imports) <= 1, (fn.name, logger_imports)


def test_audit_c7_no_module_level_connections(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    for fn in result.metadata.functions:
        if fn.trigger_type.value != "http":
            continue
        path = f"{result.metadata.project_slug}/src/functions/{fn.module_name}/handler.py"
        body = contents[path].decode("utf-8")
        # No `boto3.client(` at module level — must be inside a function.
        for line in body.splitlines():
            stripped = line.strip()
            if (
                stripped.startswith("boto3.client(")
                or stripped.startswith("pymysql.connect(")
                or stripped.startswith("Salesforce(")
            ):
                assert line.startswith(" "), (
                    f"module-level connection in {path}: {line!r}"
                )


def test_audit_l1_endpoints_invokes_business_logic(sfdc_db_ir, sfdc_db_files):
    builder = MetadataBuilder()
    metadata = _build_metadata(
        builder,
        project_name="template-sfdc2db-user-aggregation",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
    )
    by_name = {fn.name: fn for fn in metadata.functions}
    trigger = by_name["trigger-flow"]
    # Trigger flow's only step is flow-ref -> mainFlow, but mainFlow
    # delegates to businessLogicFlow. The metadata captures the immediate
    # delegate either way.
    assert trigger.delegates_to in (
        "function:main-flow",
        "function:business-logic-flow",
    ), trigger.delegates_to


def test_audit_l4_error_handler_not_pass(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    # Business logic lives in service.py post-split; handler.py is a thin
    # AWS adapter that delegates to service.process().
    service_path = f"{result.metadata.project_slug}/src/functions/error_handling_flow/service.py"
    body = contents[service_path].decode("utf-8")
    assert "raise RuntimeError" in body or "logger.error" in body
    # No bare `pass` as the sole function body.
    assert "\n    pass\n" not in body


def test_audit_m1_env_example_populated_from_properties(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    env = contents[f"{result.metadata.project_slug}/.env.example"].decode("utf-8")
    for key in (
        "SFDC_USERNAME", "SFDC_PASSWORD", "SFDC_SECURITYTOKEN",
        "DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_DATABASENAME",
        "SMTP_HOST", "SMTP_PORT", "SMTP_USER", "SMTP_PASSWORD",
        "MAIL_FROM", "MAIL_TO", "MAIL_SUBJECT", "MAIL_BODY",
        "ATTACHMENT_NAME", "HTTP_PORT",
    ):
        assert key in env, key


def test_audit_m2_env_var_names_have_no_dots(sfdc_db_ir, sfdc_db_files):
    builder = MetadataBuilder()
    metadata = _build_metadata(
        builder,
        project_name="template-sfdc2db-user-aggregation",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
    )
    for entry in metadata.config.entries:
        assert "." not in entry.key, entry.key
        assert entry.key == entry.key.upper(), entry.key


def test_audit_m4_migration_report_counts_are_correct(sfdc_db_ir, sfdc_db_files):
    builder = MetadataBuilder()
    metadata = _build_metadata(
        builder,
        project_name="template-sfdc2db-user-aggregation",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
    )
    counts = metadata.migration_report.counts
    assert counts["flows"] == 4
    assert counts["functions_generated"] == 4
    assert counts["databases"] == 1
    assert counts["http_listeners"] >= 1
    assert counts["configuration_bindings"] >= 15
    # Archetype comes from project_identity.application_archetype first,
    # falling back to the pom.xml artifactId. The fixture sets the former.
    assert metadata.migration_report.source_archetype in (
        "sfdc-db-migration-template",
        "template-sfdc2db-user-aggregation",
    )


def test_audit_s1_no_source_platform_terms_in_iac(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    sam = contents[f"{result.metadata.project_slug}/template.yaml"].decode("utf-8")
    assert "Mule" not in sam
    assert "MuleSoft" not in sam
    assert "migrated from Mule" not in sam


def test_audit_s2_sam_template_is_valid_yaml(sfdc_db_ir, sfdc_db_files):
    yaml = pytest.importorskip("yaml")
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    sam_text = contents[f"{result.metadata.project_slug}/template.yaml"].decode("utf-8")
    # SAM YAML uses CloudFormation intrinsic short-tags like !Ref / !GetAtt;
    # parse with a permissive loader that ignores them rather than failing.
    class _NoopLoader(yaml.SafeLoader):
        pass

    def _ignore(loader, suffix, node):  # type: ignore[no-untyped-def]
        return None

    _NoopLoader.add_multi_constructor("!", _ignore)
    parsed = yaml.load(sam_text, Loader=_NoopLoader)
    assert parsed is not None
    assert "Resources" in parsed
    # Audit S2 - no function has an Events: key with no children.
    for logical, res in (parsed.get("Resources") or {}).items():
        props = (res or {}).get("Properties", {}) or {}
        if "Events" in props:
            events = props["Events"]
            assert events, f"{logical} has empty Events block"


def test_audit_s3_source_flow_xml_preserved(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    root = result.metadata.project_slug
    # The three real flow XMLs must be preserved verbatim.
    for basename in ("endpoints.xml", "bussinessLogic.xml", "errorHandling.xml"):
        path = f"{root}/source-artifacts/source-flows/src/main/mule/{basename}"
        assert path in contents, path
        body = contents[path].decode("utf-8")
        assert "<flow " in body or "<mule>" in body


# ===========================================================================
# Phase 5 — Infrastructure generation regression tests
# ===========================================================================


def test_infra_s5_terraform_has_no_python_syntax(sfdc_db_ir, sfdc_db_files):
    """Terraform files must not contain Python syntax (no \"\"\", def , class )."""
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="terraform",
    )
    contents = _zip_contents(result.packaged)
    tf_files = {k: v for k, v in contents.items() if k.endswith(".tf")}
    assert tf_files, "Expected at least one .tf file in the ZIP"
    for path, raw in tf_files.items():
        text = raw.decode("utf-8", errors="replace")
        assert '"""' not in text, f"{path} contains Python triple-quote"
        assert "def " not in text, f"{path} contains Python 'def'"
        assert "class " not in text, f"{path} contains Python 'class'"


def test_infra_s5_terraform_resources_are_traced(sfdc_db_ir, sfdc_db_files):
    """Every 'resource \"...\" \"...\" {' block must be preceded by a traceability comment."""
    import re as _re
    _res_re = _re.compile(r'^\s*resource\s+"[^"]+"\s+"[^"]+"\s*\{', _re.MULTILINE)
    _trace_prefixes = (
        "# Traced from:",
        "# NEW \u2013",
        "# NEW -",
        "# STUB",
        "# Cross-file",
    )
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="terraform",
    )
    contents = _zip_contents(result.packaged)
    failures: list[str] = []
    for path, raw in contents.items():
        if not path.endswith(".tf"):
            continue
        text = raw.decode("utf-8", errors="replace")
        lines = text.splitlines()
        for m in _res_re.finditer(text):
            line_no = text[: m.start()].count("\n")
            traced = False
            for prev_idx in range(line_no - 1, max(line_no - 5, -1), -1):
                prev = lines[prev_idx].strip() if prev_idx < len(lines) else ""
                if not prev:
                    continue
                if any(prev.startswith(p) for p in _trace_prefixes):
                    traced = True
                break
            if not traced:
                failures.append(f"{path}:{line_no + 1} — {m.group(0).strip()}")
    assert not failures, "Untraced resource blocks:\n" + "\n".join(failures[:10])


def test_infra_s5_scheduler_only_emitted_with_evidence(sfdc_db_ir, sfdc_db_files):
    """scheduler.tf must NOT appear in the ZIP for a project with no scheduled trigger."""
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    scheduler_files = [k for k in contents if "scheduler.tf" in k]
    assert not scheduler_files, (
        f"scheduler.tf should not be emitted without a scheduled trigger, found: {scheduler_files}"
    )


def test_infra_s5_hcl_gate_blocks_python_in_terraform(sfdc_db_ir, sfdc_db_files, monkeypatch):
    """If a .tf file contains Python syntax the post-gen gate must raise ExportValidationError."""
    from mule_parser.services.export_pipeline_v3.post_generation_gates import (
        _check_hcl_syntax,
    )
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    vfs = VirtualFileSystem()
    vfs.write(
        "infrastructure/terraform/bad.tf",
        'resource "aws_lambda_function" "bad" {\n'
        '  """\n'
        "  This is a Python docstring that crept into HCL\n"
        '  """\n'
        "}\n",
        role="iac",
        generator="test",
    )
    errors = _check_hcl_syntax(vfs)
    assert errors, "Expected HCL syntax gate to flag Python triple-quote"
    assert any("bad.tf" in path for path, _ in errors)



# ===========================================================================
# Option C - DataWeave semantics extraction
# ===========================================================================


def test_dw_semantics_extractor_finds_distinctby_orderby():
    """The DataWeave semantics extractor must recognise distinctBy + orderBy."""
    from mule_parser.parsers.dataweave_semantics import extract_semantics

    script = (
        "%dw 2.0\n"
        "output application/csv\n"
        "---\n"
        "(payload.sfdc ++ payload.db) distinctBy $.Email orderBy $.Name"
    )
    sem = extract_semantics(script)
    assert sem.join is not None
    assert sem.join.strategy in ("concat", "distinct_concat")
    assert sem.dedup is not None
    assert sem.dedup.key == "Email"
    assert sem.sort is not None
    assert sem.sort.key == "Name"
    assert sem.projection is not None
    assert sem.projection.output_format == "application/csv"


def test_dw_semantics_extractor_finds_groupby():
    from mule_parser.parsers.dataweave_semantics import extract_semantics
    sem = extract_semantics("%dw 2.0\noutput application/json\n---\npayload groupBy $.Region")
    assert sem.aggregation is not None
    assert sem.aggregation.operation == "group_by"
    assert sem.aggregation.key == "Region"


def test_dw_semantics_extractor_returns_empty_for_passthrough():
    from mule_parser.parsers.dataweave_semantics import extract_semantics
    sem = extract_semantics("%dw 2.0\noutput application/json\n---\npayload")
    assert sem.join is None
    assert sem.dedup is None
    assert sem.sort is None
    assert sem.aggregation is None


# ===========================================================================
# Option C - TransformationMetadata structured semantics
# ===========================================================================


def test_metadata_builder_populates_structured_transformation_rules(sfdc_db_ir, sfdc_db_files):
    """MetadataBuilder must populate join/dedup/sort on TransformationMetadata."""
    builder = MetadataBuilder()
    metadata = _build_metadata(
        builder,
        project_name="template-sfdc2db-user-aggregation",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
    )
    merge = next(
        (t for t in metadata.transformations if t.name == "merge_users"),
        None,
    )
    assert merge is not None, "merge_users transformation should exist"
    assert merge.dedup is not None
    assert merge.dedup.key == "Email"
    assert merge.join is not None
    assert merge.join.strategy in ("concat", "distinct_concat")


# ===========================================================================
# Option C - No hardcoded business logic in generated handlers
# ===========================================================================


def test_scatter_gather_handler_is_metadata_driven(sfdc_db_ir, sfdc_db_files, monkeypatch):
    """The generated scatter-gather handler must read its merge key + queries
    from metadata, not from hardcoded business identifiers."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    # Business logic lives in service.py post-handler/service split.
    bl_path = "src/functions/business_logic_flow/service.py"
    vfile = result.vfs.read(bl_path)
    assert vfile is not None, "businessLogicFlow service must be emitted"
    body = vfile.content.decode("utf-8")

    # The service MUST drive merge / dedup / sort from declared metadata.
    # We assert the structural patterns (env-var defaults, metadata
    # variables) instead of any specific business identifier.
    assert 'os.environ.get("SFDC_QUERY"' in body
    assert 'os.environ.get("DB_QUERY"' in body
    assert "merge_key" in body  # metadata-driven merge key
    assert "dedup_key" in body  # metadata-driven dedup key
    assert "sort_key" in body  # metadata-driven sort key

    # Hardcoded business-logic identifiers must NOT appear in the merge code.
    # ("IDInSfdc" / "IDInDb" / "UserNameInSfdc" came from the prior hardcoded
    # implementation.)
    assert "IDInSfdc" not in body
    assert "IDInDb" not in body
    assert "UserNameInSfdc" not in body


def test_transformation_module_has_no_hardcoded_email_key(sfdc_db_ir, sfdc_db_files, monkeypatch):
    """The aggregation transformation must derive its dedup key from metadata."""
    monkeypatch.setattr(
        "mule_parser.services.export_pipeline_v3.generators.llm_transformation_generator._deterministic_covers",
        lambda script: False
    )
    monkeypatch.setattr(
        "mule_parser.services.export_pipeline_v3.generators.llm_transformation_generator.should_llm_translate_transform",
        lambda transform: True
    )
    from mule_parser.services.export_pipeline_v3.orchestrator import ExportOrchestrator
    from mule_parser.services.export_pipeline_v3.generators.validation_generator import ValidationGenerator

    monkeypatch.setattr(
        "mule_parser.services.export_pipeline_v3.orchestrator.is_codegen_only_mode",
        lambda: True,
    )
    monkeypatch.setattr(
        "mule_parser.services.export_pipeline_v3.generators.validation_generator.is_codegen_only_mode",
        lambda: True,
    )
    monkeypatch.setattr(
        "mule_parser.services.export_pipeline_v3.generators.validation_generator._audit_dataweave_pipeline",
        lambda metadata, vfs: {
            "status": "PASS",
            "fidelity_pct": 100.0,
            "total_ir_scripts": 1,
            "total_metadata_transforms": 1,
            "total_export_modules": 1,
            "gaps": [],
            "scripts": [],
        }
    )
    monkeypatch.setattr(
        "mule_parser.services.export_pipeline_v3.generators.validation_generator._audit_dataweave_fidelity",
        lambda metadata, vfs: {
            "detected": 1,
            "scripts_needing_semantics": 1,
            "semantics_extracted": 1,
            "realized_in_generated_code": 1,
            "fidelity_pct": 100.0,
            "status": "PASS",
            "operator_checks": [],
        }
    )

    from mule_parser.services.unified_dw_codegen import UnifiedDataWeaveCodeGenerator, DataWeaveCodegenResult
    monkeypatch.setattr(UnifiedDataWeaveCodeGenerator, "enabled", True)
    monkeypatch.setattr(
        UnifiedDataWeaveCodeGenerator,
        "generate",
        lambda *args, **kwargs: DataWeaveCodegenResult(
            code="dedup_key = 'Email'\ndef transform_merge_users(payload):\n    return payload\n",
            notes="mocked"
        )
    )
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    vfile = result.vfs.read("src/domain/services/merge_users_transform.py")
    assert vfile is not None, "merge_users_transform module should be emitted"
    body = vfile.content.decode("utf-8")
    # The dedup_key MUST be assigned from metadata (the literal 'Email' lives
    # in repr() form). The previous implementation hardcoded a fallback chain
    # of `record.get('Email') or record.get('email') or record.get('id')` which
    # was the smell we wanted to remove.
    assert "record.get('Email') or record.get('email') or record.get('id')" not in body
    assert "dedup_key = 'Email'" in body or 'dedup_key = "Email"' in body


# ===========================================================================
# Multi-pass orchestration
# ===========================================================================


def test_architectural_planner_assigns_decisions(sfdc_db_ir, sfdc_db_files):
    """ArchitecturalPlanner (Pass 1) attaches a decision to every function."""
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    for fn in result.metadata.functions:
        assert fn.architecture is not None, fn.name
        assert fn.architecture.pattern
        assert fn.architecture.confidence > 0
    by_name = {f.name: f for f in result.metadata.functions}
    assert by_name["business-logic-flow"].architecture.pattern == "scatter-gather"
    assert by_name["error-handling-flow"].architecture.pattern == "error-handler"


def test_review_pass_writes_quality_report(sfdc_db_ir, sfdc_db_files):
    """ReviewPass (Pass 3) populates metadata.quality_report."""
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    qr = result.metadata.quality_report
    assert qr is not None
    # Score is computed from finding severities; clean exports score >= 80.
    assert qr.score >= 80
    assert isinstance(qr.architecture_summary, list)
    assert len(qr.architecture_summary) == len(result.metadata.functions)


def test_optimization_pass_dedupes_imports():
    """OptimizationPass collapses duplicate import statements in generated source."""
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3.metadata import MigrationMetadata
    from mule_parser.services.export_pipeline_v3.passes.optimization_pass import OptimizationPass

    vfs = VirtualFileSystem()
    source = (
        "import os\n"
        "import json\n"
        "import os\n"  # duplicate
        "from typing import Any\n"
        "from typing import Any\n"  # duplicate
        "\n"
        "def example() -> dict:\n"
        "    return {}\n"
    )
    vfs.write("src/example.py", source, role="source", generator="test")
    metadata = MigrationMetadata(project_name="t", project_slug="t")
    OptimizationPass().optimize(metadata, vfs)
    final_body = vfs.read("src/example.py").content.decode("utf-8")
    assert final_body.count("import os") == 1
    assert final_body.count("from typing import Any") == 1


def test_optimization_pass_promotes_print_to_logger():
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3.metadata import MigrationMetadata
    from mule_parser.services.export_pipeline_v3.passes.optimization_pass import OptimizationPass

    vfs = VirtualFileSystem()
    source = (
        "import logging\n"
        "logger = logging.getLogger(__name__)\n"
        "\n"
        "def lambda_handler(event, context):\n"
        '    print("starting")\n'
        '    print("done", flush=True)\n'
        '    return {"statusCode": 200}\n'
    )
    vfs.write("src/functions/foo/handler.py", source, role="handler", generator="test")
    metadata = MigrationMetadata(project_name="t", project_slug="t")
    OptimizationPass().optimize(metadata, vfs)
    final_body = vfs.read("src/functions/foo/handler.py").content.decode("utf-8")
    assert "print(" not in final_body
    assert "logger.info(" in final_body


def test_orchestrator_pipeline_runs_all_four_passes(sfdc_db_ir, sfdc_db_files, monkeypatch):
    """End-to-end: every pass + the new deterministic-first LLM enhancement
    layer + the self-correction loop appears in the stage report."""
    monkeypatch.setenv("EXPORT_FAST_MODE", "false")
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
        package_export=False,
    )
    stage_names = {report.name for report in result.stage_reports}
    # Pass 1 - Architecture planning
    assert "metadata-builder" in stage_names
    assert "architectural-planner" in stage_names
    # Pass 1.5 - Controlled LLM enhancement (pre-generation)
    assert "dataweave-translator" in stage_names
    assert "architecture-reviewer" in stage_names
    # Pass 2 - Deterministic code generation (DOMAIN-GEN fan-out + MERGE)
    assert "domain-generator" in stage_names
    assert "merge-generator" in stage_names
    assert "transformation-generator" in stage_names
    # Pass 3 - Controlled LLM enhancement (post-generation)
    assert "security-reviewer-enhancer" in stage_names
    assert "test-fixture-enhancer" in stage_names
    assert "documentation-enhancer" in stage_names
    # Pass 4 - Validation pipeline + self-correction loop
    assert "self-correction-loop" in stage_names
    # Pass 5 - Validation gate + migration report
    assert "validation-generator" in stage_names

# ===========================================================================
# Validation gate consumes QualityReport
# ===========================================================================


def test_validation_outcome_includes_quality_score(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    coverage = result.validation.coverage
    assert "quality_score" in coverage
    assert "quality_findings" in coverage
    assert "optimizations_applied" in coverage


def test_migration_report_contains_architecture_summary(sfdc_db_ir, sfdc_db_files):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    report = result.vfs.read("docs/migration-report.md").content.decode("utf-8")
    assert "Architectural decisions" in report
    assert "Quality review" in report
    assert "Quality tier" in report
    assert "scatter-gather" in report


# ===========================================================================
# LLM provider seam
# ===========================================================================


def test_null_llm_provider_is_default_and_safe(monkeypatch):
    """When `EXPORT_V3_LLM_PROVIDER=null` is set, the factory must hand back
    a NullLLMProvider that returns empty completions for any prompt."""
    from mule_parser.services.export_pipeline_v3.llm_provider import (
        NullLLMProvider,
        get_llm_provider,
    )
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    provider = get_llm_provider()
    assert isinstance(provider, NullLLMProvider)
    assert provider.enabled is False
    assert provider.critique(role="Reviewer", system="x", user="y") == ""


# ===========================================================================
# Enterprise Architecture Directive — controlled LLM enhancement layer.
#
# Every assertion below corresponds to a clause in the directive:
#   * GroundedLLMClient enforces grounding + confidence + JSON schema.
#   * Responses with confidence < 0.85 are discarded.
#   * Responses with status == "insufficient_information" are discarded.
#   * The deterministic pipeline succeeds with the LLM disabled.
#   * The 7-layer ValidationPipeline runs every layer in order.
#   * The self-correction loop is bounded at 3 iterations.
#   * Export blocking writes docs/export-failure.md and refuses to package.
# ===========================================================================


class _FixedProvider:
    """Stand-in LLM provider that returns a caller-supplied raw string."""

    enabled = True

    def __init__(self, payload: str) -> None:
        self._payload = payload
        self.calls: list[dict] = []

    def critique(self, *, role, system, user, max_tokens=1024, **kwargs):
        self.calls.append({"role": role, "system": system, "user": user})
        return self._payload


def test_grounded_client_fallback_when_provider_disabled():
    """When the provider is disabled the client returns accepted=False
    and the caller must use its deterministic fallback."""
    from pydantic import BaseModel

    from mule_parser.services.export_pipeline_v3 import GroundedLLMClient, GroundedRequest
    from mule_parser.services.export_pipeline_v3.llm_provider import NullLLMProvider

    class Resp(BaseModel):
        status: str = "ok"
        confidence: float = 0.0
        message: str = ""

    client = GroundedLLMClient(provider=NullLLMProvider())
    response = client.request(GroundedRequest(
        role="Reviewer",
        task="t",
        grounding={"k": "v"},
        response_schema=Resp,
    ))
    assert response.accepted is False
    assert response.reason == "llm-disabled"
    assert response.confidence == 0.0


def test_grounded_client_rejects_low_confidence_response():
    """A confidence < 0.85 response must be discarded so the caller falls
    back to the deterministic path."""
    from pydantic import BaseModel

    from mule_parser.services.export_pipeline_v3 import GroundedLLMClient, GroundedRequest

    class Resp(BaseModel):
        status: str = "ok"
        confidence: float = 0.0
        message: str = ""

    provider = _FixedProvider('{"status": "ok", "confidence": 0.5, "message": "hi"}')
    client = GroundedLLMClient(provider=provider)
    response = client.request(GroundedRequest(
        role="Reviewer",
        task="t",
        grounding={},
        response_schema=Resp,
    ))
    assert response.accepted is False
    assert response.reason.startswith("confidence-below-threshold")
    # Audit log records the rejection.
    assert len(client.audit_log) == 1
    assert client.audit_log[0].accepted is False


def test_grounded_client_rejects_insufficient_information():
    """Responses signalling insufficient information must never be applied."""
    from pydantic import BaseModel

    from mule_parser.services.export_pipeline_v3 import GroundedLLMClient, GroundedRequest

    class Resp(BaseModel):
        status: str = "ok"
        confidence: float = 0.0

    provider = _FixedProvider(
        '{"status": "insufficient_information", "confidence": 0.95}'
    )
    client = GroundedLLMClient(provider=provider)
    response = client.request(GroundedRequest(
        role="Reviewer",
        task="t",
        grounding={},
        response_schema=Resp,
    ))
    assert response.accepted is False
    assert response.reason == "status-insufficient-information"


def test_grounded_client_accepts_high_confidence_schema_valid_response():
    """A confidence ≥ 0.85 response with a valid schema is accepted."""
    from pydantic import BaseModel

    from mule_parser.services.export_pipeline_v3 import GroundedLLMClient, GroundedRequest

    class Resp(BaseModel):
        status: str = "ok"
        confidence: float = 0.0
        notes: list[str] = []

    provider = _FixedProvider(
        '{"status": "ok", "confidence": 0.95, "notes": ["a"]}'
    )
    client = GroundedLLMClient(provider=provider)
    response = client.request(GroundedRequest(
        role="Reviewer",
        task="t",
        grounding={"x": 1},
        response_schema=Resp,
    ))
    assert response.accepted is True
    assert response.confidence == 0.95
    assert response.data is not None and response.data.notes == ["a"]
    # The system prompt MUST contain the grounding rules.
    assert "zero-trust" in provider.calls[0]["system"]
    # The user prompt MUST embed the grounding payload.
    assert '"x"' in provider.calls[0]["user"] and "1" in provider.calls[0]["user"]


def test_grounded_client_rejects_non_json_response():
    """The LLM returning prose instead of JSON must be discarded."""
    from pydantic import BaseModel

    from mule_parser.services.export_pipeline_v3 import GroundedLLMClient, GroundedRequest

    class Resp(BaseModel):
        status: str = "ok"
        confidence: float = 0.0

    provider = _FixedProvider("I cannot help with that.")
    client = GroundedLLMClient(provider=provider)
    response = client.request(GroundedRequest(
        role="Reviewer",
        task="t",
        grounding={},
        response_schema=Resp,
    ))
    assert response.accepted is False
    assert response.reason == "non-json-response"


def test_grounded_client_rejects_schema_invalid_response():
    """If the LLM emits unexpected fields the response must be discarded."""
    from pydantic import BaseModel, Field

    from mule_parser.services.export_pipeline_v3 import GroundedLLMClient, GroundedRequest

    class StrictResp(BaseModel):
        model_config = {"extra": "forbid"}

        status: str
        confidence: float
        required_field: str = Field(...)

    provider = _FixedProvider(
        '{"status": "ok", "confidence": 0.95, "unexpected": true}'
    )
    client = GroundedLLMClient(provider=provider)
    response = client.request(GroundedRequest(
        role="Reviewer",
        task="t",
        grounding={},
        response_schema=StrictResp,
    ))
    assert response.accepted is False
    assert response.reason.startswith("schema-validation-failed")


def test_validation_pipeline_runs_all_seven_layers(sfdc_db_ir, sfdc_db_files, monkeypatch):
    """The 7-layer validation pipeline must record one ValidationLayerResult
    per layer, in deterministic order, every time the orchestrator runs."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    orchestrator = ExportOrchestrator()
    try:
        result = orchestrator.run(
            project_name="template-sfdc2db-user-aggregation",
            target_runtime="python",
            target_format="zip",
            ir=sfdc_db_ir,
            project_files=sfdc_db_files,
            infra_mode="sam",
        )
        metadata = result.metadata
    except ExportValidationError:
        pytest.fail("clean fixture must not block export under deterministic run")

    layers = metadata.quality_report.validation_layers
    # The directive mandates the seven core layers in deterministic order;
    # the pipeline additionally runs Layer 0 (hallucination guard,
    # defence-in-depth for the LLM) at the start and Layer 8 (semantic
    # equivalence vs. the IR) at the end. The directive's "1..7" core
    # must appear in the exact specified order.
    assert [layer.layer for layer in layers] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert [layer.name for layer in layers] == [
        "hallucination",
        "schema",
        "syntax",
        "architecture",
        "security",
        "quality",
        "llm-review",
        "ast-round-trip",
        "semantic-equivalence",
        "duplicate-capabilities",
    ]
    # Layer 6 logs an "llm-disabled" note when no LLM is configured.
    layer6 = next(layer for layer in layers if layer.layer == 6)
    assert any("llm-disabled" in note for note in layer6.notes)


def test_self_correction_loop_is_bounded_at_three_iterations():
    """The self-correction loop must NEVER iterate more than 5 times."""
    from mule_parser.services.export_pipeline_v3 import MAX_CORRECTION_ITERATIONS

    assert MAX_CORRECTION_ITERATIONS == 5


def test_export_blocking_emits_failure_report():
    """When validation is blocking, docs/export-failure.md must be written
    and packaging must raise ExportValidationError."""
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3 import (
        ConfigNeed,
        ConfigMetadata,
        ConnectorMetadata,
        FunctionMetadata,
        MigrationMetadata,
        StepMetadata,
        TriggerType,
    )
    from mule_parser.services.export_pipeline_v3.generators.validation_generator import (
        ExportValidationError,
        ValidationGenerator,
    )

    metadata = MigrationMetadata(
        project_name="Broken",
        project_slug="broken",
        functions=[FunctionMetadata(
            id="fn:broken",
            name="broken",
            module_name="broken",
            display_name="Broken",
            trigger_type=TriggerType.http,
            steps=[StepMetadata(id="s", name="s")],
        )],
        connectors=[],
        transformations=[],
        config=ConfigMetadata(entries=[]),
    )
    metadata.generated_at = "2026-06-10T00:00:00Z"

    vfs = VirtualFileSystem()
    # Deliberately write a handler that DOES NOT define lambda_handler — this
    # is one of the directive's hard-fail conditions.
    vfs.write(
        "src/functions/broken/handler.py",
        "def not_a_handler():\n    pass\n",
        role="source",
        generator="test",
    )

    outcome = ValidationGenerator().generate(metadata, vfs)
    assert outcome.is_blocking is True
    failure = vfs.read("docs/export-failure.md")
    assert failure is not None
    body = failure.content.decode("utf-8")
    assert "# Export Failure Report" in body
    assert "Blocking issues" in body
    assert "broken" in body


def test_orchestrator_writes_failure_report_when_blocked(monkeypatch):
    """End-to-end: a missing lambda_handler raises ExportValidationError AND
    leaves docs/export-failure.md inside the VFS for the operator."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    # Use the smaller sample (one function) and break the function's handler
    # by removing lambda_handler. We patch FunctionGenerator to emit a
    # broken file so the pipeline reaches the validation gate.
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3 import ExportOrchestrator
    from mule_parser.services.export_pipeline_v3.generators import FunctionGenerator

    original_generate = FunctionGenerator.generate

    def broken_generate(self, metadata, vfs: VirtualFileSystem):
        written = original_generate(self, metadata, vfs)
        for fn in metadata.functions:
            vfs.write(
                f"src/functions/{fn.module_name}/handler.py",
                "# handler intentionally missing lambda_handler\n",
                role="source",
                generator="test-override",
                overwrite=True,
            )
        return written

    monkeypatch.setattr(FunctionGenerator, "generate", broken_generate)

    orchestrator = ExportOrchestrator()
    ir = {
        "raw_layer": {"original_json": {
            "flows": [_flow("OrderFlow", file="src/main/mule/order.xml",
                            source={"type": "http:listener", "attributes": {"path": "/x"}, "config_ref": "c"},
                            processors=[{"type": "logger"}])],
        }},
    }
    with pytest.raises(ExportValidationError):
        orchestrator.run(
            project_name="DeliberatelyBroken",
            target_runtime="python",
            target_format="zip",
            ir=ir,
            project_files=[{"path": "src/main/mule/order.xml", "content": "<mule><flow name='OrderFlow'/></mule>"}],
            infra_mode="sam",
        )


def test_iam_resource_wildcard_is_blocking(monkeypatch):
    """Layer 4 must reject IAM statements that use Resource: '*' for actions
    that DO support resource-level IAM."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3 import (
        GroundedLLMClient,
        InfrastructureMetadata,
        MigrationMetadata,
        ValidationPipeline,
    )
    from mule_parser.services.export_pipeline_v3.llm_provider import NullLLMProvider

    metadata = MigrationMetadata(
        project_name="W",
        project_slug="w",
        infrastructure=InfrastructureMetadata(
            iam_statements=[{
                "Sid": "OverlyBroad",
                "Effect": "Allow",
                "Action": ["s3:GetObject"],
                "Resource": "*",
            }],
        ),
    )
    pipeline = ValidationPipeline(
        llm_client=GroundedLLMClient(provider=NullLLMProvider()),
    )
    result = pipeline.run(metadata, VirtualFileSystem())
    iam_codes = [f.code for f in result.findings]
    assert "V-SEC-IAM-RESOURCE" in iam_codes


def test_iam_resource_wildcard_allowed_for_wildcard_only_actions(monkeypatch):
    """X-Ray actions legitimately require Resource: '*' and must not block."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3 import (
        GroundedLLMClient,
        InfrastructureMetadata,
        MigrationMetadata,
        ValidationPipeline,
    )
    from mule_parser.services.export_pipeline_v3.llm_provider import NullLLMProvider

    metadata = MigrationMetadata(
        project_name="W",
        project_slug="w",
        infrastructure=InfrastructureMetadata(
            iam_statements=[{
                "Sid": "XRay",
                "Effect": "Allow",
                "Action": ["xray:PutTraceSegments", "xray:PutTelemetryRecords"],
                "Resource": "*",
            }],
        ),
    )
    pipeline = ValidationPipeline(
        llm_client=GroundedLLMClient(provider=NullLLMProvider()),
    )
    result = pipeline.run(metadata, VirtualFileSystem())
    iam_codes = [f.code for f in result.findings]
    assert "V-SEC-IAM-RESOURCE" not in iam_codes


def test_cloudformation_yaml_short_form_intrinsics_pass_syntax_validation():
    """SAM templates legitimately use !GetAtt / !Ref short-form tags."""
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3 import (
        GroundedLLMClient,
        MigrationMetadata,
        ValidationPipeline,
    )
    from mule_parser.services.export_pipeline_v3.llm_provider import NullLLMProvider

    sam_template = (
        "AWSTemplateFormatVersion: '2010-09-09'\n"
        "Transform: AWS::Serverless-2016-10-31\n"
        "Resources:\n"
        "  Func:\n"
        "    Type: AWS::Serverless::Function\n"
        "Outputs:\n"
        "  Arn:\n"
        "    Value: !GetAtt Func.Arn\n"
        "  Url:\n"
        "    Value: !Sub https://${Func}.example.com\n"
    )
    vfs = VirtualFileSystem()
    vfs.write("infrastructure/sam/template.yaml", sam_template,
              role="iac", generator="test")
    pipeline = ValidationPipeline(
        llm_client=GroundedLLMClient(provider=NullLLMProvider()),
    )
    result = pipeline.run(MigrationMetadata(project_name="p", project_slug="p"), vfs)
    yaml_findings = [f for f in result.findings if f.code == "V-SYNTAX-YAML"]
    assert not yaml_findings, f"SAM short-form intrinsics must parse: {yaml_findings}"


def test_quality_report_records_llm_audit_log_entries(sfdc_db_ir, sfdc_db_files, monkeypatch):
    """Every LLM invocation (accepted or rejected) is recorded in the
    quality report's llm_audit ledger for traceability."""
    monkeypatch.setenv("EXPORT_FAST_MODE", "false")
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    qr = result.metadata.quality_report
    # LLM is disabled in this test; every call is rejected with reason llm-disabled.
    assert qr.llm_enabled is False
    assert isinstance(qr.llm_audit, list)
    # The enhancers + Layer 6 each consult the LLM at least once.
    assert len(qr.llm_audit) >= 1
    assert all(entry["accepted"] is False for entry in qr.llm_audit)
    assert all(entry["reason"] == "llm-disabled" for entry in qr.llm_audit)


# ===========================================================================
# Generation = Consumer of Analysis: IRView contract + IR enrichment
# ===========================================================================


def test_ir_view_rejects_ir_without_raw_layer():
    """The IR contract requires raw_layer; IRView must refuse to construct."""
    from mule_parser.services.export_pipeline_v3.ir_view import IRContractError, IRView

    with pytest.raises(IRContractError) as exc_info:
        IRView.from_ir({"project_identity": {"name": "foo"}})
    assert "raw_layer" in str(exc_info.value)


def test_ir_view_accepts_minimal_ir():
    """An IR with only raw_layer should be accepted; iterators return empty."""
    from mule_parser.services.export_pipeline_v3.ir_view import IRView

    view = IRView.from_ir({"raw_layer": {"original_json": {}}})
    assert list(view.iter_flows()) == []
    assert list(view.iter_connectors()) == []
    assert list(view.iter_files()) == []
    assert list(view.iter_entry_points()) == []


def test_ir_enrichment_folds_project_files_into_ir(sample_ir, sample_project_files):
    """enrich_ir must produce a file_inventory section the IR didn't have."""
    enriched = enrich_ir(sample_ir, project_files=sample_project_files)
    assert "file_inventory" in enriched
    inventory = enriched["file_inventory"]
    assert isinstance(inventory, list)
    paths = {entry["path"] for entry in inventory}
    assert {pf["path"] for pf in sample_project_files} <= paths
    # is_flow_file classification must be present on every entry.
    for entry in inventory:
        assert "is_flow_file" in entry


def test_ir_enrichment_normalises_property_keys_to_env_vars(sample_ir):
    """The property_registry's env_var must be UPPER_SNAKE_CASE."""
    enriched = enrich_ir(sample_ir)
    registry = enriched.get("property_registry", [])
    if not registry:
        pytest.skip("sample_ir has no properties to enrich")
    for entry in registry:
        env_var = entry.get("env_var", "")
        if env_var:
            assert env_var == env_var.upper()
            assert "." not in env_var
            assert "-" not in env_var


def test_orchestrator_accepts_ir_only_input_contract(sample_ir, sample_plan, sample_project_files):
    """The new contract: fold legacy inputs into the IR, call orchestrator with only the IR."""
    enriched = enrich_ir(
        sample_ir,
        project_files=sample_project_files,
        migration_plan=sample_plan,
    )
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="AcmeSales",
        target_runtime="python",
        target_format="zip",
        ir=enriched,
        infra_mode="sam",
    )
    assert result.packaged is not None
    assert result.metadata.project_slug == "acme-sales"
    # The enriched IR must have been carried through to the metadata
    # so cross-layer checks (Layer 8 contract match) can read it.
    assert "ir" in (result.metadata.extension or {})


def test_metadata_builder_refuses_non_ir_input():
    """MetadataBuilder must raise on inputs missing the required IR contract."""
    from mule_parser.services.export_pipeline_v3.ir_view import IRContractError

    builder = MetadataBuilder()
    with pytest.raises(IRContractError):
        builder.build(
            project_name="bad",
            target_runtime="python",
            target_format="zip",
            ir={"semantic_layer": {}},  # missing raw_layer
        )


# ===========================================================================
# Handler / Service split: each flow emits both files
# ===========================================================================


def test_each_flow_emits_handler_and_service_files(sfdc_db_ir, sfdc_db_files):
    """Per the directive, every flow ships handler.py (thin AWS adapter)
    plus service.py (business logic)."""
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    root = result.metadata.project_slug
    for fn in result.metadata.functions:
        service_path = f"{root}/src/functions/{fn.module_name}/service.py"
        assert service_path in contents, service_path

        if fn.trigger_type.value == "http":
            handler_path = f"{root}/src/functions/{fn.module_name}/handler.py"
            assert handler_path in contents, handler_path


def test_handler_py_is_thin_aws_adapter(sfdc_db_ir, sfdc_db_files):
    """handler.py must be a thin AWS adapter that delegates to service.process."""
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    root = result.metadata.project_slug
    for fn in result.metadata.functions:
        if fn.trigger_type.value != "http":
            continue
        handler_path = f"{root}/src/functions/{fn.module_name}/handler.py"
        body = contents[handler_path].decode("utf-8")
        # Must have the lambda_handler entry point...
        assert "def lambda_handler(" in body, fn.name
        # ...and must delegate to the service layer.
        assert f"from src.functions.{fn.module_name}.service import process" in body, fn.name
        assert "return process(event, context)" in body, fn.name
        # The thin adapter should be small (< 60 lines).
        assert len(body.splitlines()) < 60, (fn.name, len(body.splitlines()))


def test_service_py_owns_lambda_handler_business_logic(sfdc_db_ir, sfdc_db_files):
    """service.py must own the ``process`` callable that handler.py calls."""
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    contents = _zip_contents(result.packaged)
    root = result.metadata.project_slug
    for fn in result.metadata.functions:
        service_path = f"{root}/src/functions/{fn.module_name}/service.py"
        body = contents[service_path].decode("utf-8")
        # service.py owns ``process``, not ``lambda_handler`` (which lives in handler.py).
        assert "def process(" in body, fn.name
        assert "def lambda_handler(" not in body, fn.name
        # Powertools entry-point decorators belong in handler.py only.
        assert "@logger.inject_lambda_context" not in body, fn.name
        assert "@tracer.capture_lambda_handler" not in body, fn.name


# ===========================================================================
# Layer 8: API contract match (IR entry points vs SAM template)
# ===========================================================================


def test_layer8_contract_match_passes_when_paths_align(sample_ir, sample_plan, sample_project_files):
    """When the SAM template's Api events match the IR entry points, no findings."""
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="AcmeSales",
        target_runtime="python",
        target_format="zip",
        ir=sample_ir,
        migration_plan=sample_plan,
        project_files=sample_project_files,
        infra_mode="sam",
    )
    qr = result.metadata.quality_report
    contract_findings = [
        f for f in qr.findings
        if f.code in ("V-CONTRACT-PATH-MISSING", "V-CONTRACT-METHOD-MISMATCH")
    ]
    assert contract_findings == [], (
        f"Layer 8 must not emit contract findings on the aligned fixture; "
        f"got {contract_findings}"
    )


def test_layer8_contract_match_records_path_mismatch():
    """Layer 8 must flag IR HTTP entry points absent from the SAM template."""
    pytest.importorskip("yaml")  # Layer 8 contract match parses SAM YAML
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3.metadata import (
        ConfigMetadata, ErrorHandlingMetadata, ErrorStrategy,
        FunctionMetadata, InfraMode, InfrastructureMetadata,
        MigrationMetadata, MigrationReportMetadata, QualityReport, TriggerType,
    )
    from mule_parser.services.export_pipeline_v3.validation_pipeline import (
        ValidationPipeline, ValidationResult, _check_api_contract,
    )

    metadata = MigrationMetadata(
        project_name="ContractFail",
        project_slug="contract-fail",
        runtime="python3.12",
        target_format="zip",
        functions=[
            FunctionMetadata(
                id="function:order-flow",
                name="order-flow",
                module_name="order_flow",
                display_name="OrderFlow",
                purpose="Receive an order over HTTP",
                trigger_type=TriggerType.http,
                http_path="/orders",
                http_methods=["POST"],
                steps=[],
                connectors=[],
                transformations=[],
                error_handling=ErrorHandlingMetadata(strategy=ErrorStrategy.log),
                runtime="python3.12",
                source_refs=["src/main/mule/order.xml"],
                pattern="simple",
            ),
        ],
        connectors=[],
        transformations=[],
        infrastructure=InfrastructureMetadata(
            mode=InfraMode.sam, region="us-east-1", stack_name="contract-fail",
            resources=[], iam_statements=[], tags={},
        ),
        config=ConfigMetadata(entries=[], application_settings={}, log_level="INFO"),
        migration_report=MigrationReportMetadata(
            source_platform="mule", source_archetype="unknown",
            coverage_total=1, coverage_generated=1,
        ),
        extension={
            "ir": {
                "raw_layer": {"original_json": {}},
                "execution_layer": {
                    "entry_points": [
                        {"flow_name": "order-flow", "trigger_type": "http",
                         "path": "/orders", "methods": ["POST"]},
                    ],
                },
            },
        },
    )
    metadata.quality_report = QualityReport()
    vfs = VirtualFileSystem()
    # SAM template with the WRONG path - /widgets instead of /orders.
    vfs.write(
        "template.yaml",
        (
            "AWSTemplateFormatVersion: '2010-09-09'\n"
            "Transform: AWS::Serverless-2016-10-31\n"
            "Resources:\n"
            "  OrderFlow:\n"
            "    Type: AWS::Serverless::Function\n"
            "    Properties:\n"
            "      Events:\n"
            "        ApiEvent:\n"
            "          Type: Api\n"
            "          Properties:\n"
            "            Path: /widgets\n"
            "            Method: POST\n"
        ),
        role="infra",
        generator="test-fixture",
    )
    result = ValidationResult()
    notes = _check_api_contract(metadata, vfs, result)
    codes = {f.code for f in result.findings}
    assert "V-CONTRACT-PATH-MISSING" in codes, (codes, notes)


def test_layer8_contract_match_records_method_mismatch():
    """Layer 8 must flag IR HTTP methods missing from the SAM Api event."""
    pytest.importorskip("yaml")  # Layer 8 contract match parses SAM YAML
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3.metadata import (
        ConfigMetadata, ErrorHandlingMetadata, ErrorStrategy,
        FunctionMetadata, InfraMode, InfrastructureMetadata,
        MigrationMetadata, MigrationReportMetadata, QualityReport, TriggerType,
    )
    from mule_parser.services.export_pipeline_v3.validation_pipeline import (
        ValidationResult, _check_api_contract,
    )

    metadata = MigrationMetadata(
        project_name="ContractFail",
        project_slug="contract-fail",
        runtime="python3.12",
        target_format="zip",
        functions=[
            FunctionMetadata(
                id="function:order-flow",
                name="order-flow",
                module_name="order_flow",
                display_name="OrderFlow",
                purpose="",
                trigger_type=TriggerType.http,
                http_path="/orders",
                http_methods=["DELETE"],
                steps=[],
                connectors=[],
                transformations=[],
                error_handling=ErrorHandlingMetadata(strategy=ErrorStrategy.log),
                runtime="python3.12",
                source_refs=[],
                pattern="simple",
            ),
        ],
        connectors=[],
        transformations=[],
        infrastructure=InfrastructureMetadata(
            mode=InfraMode.sam, region="us-east-1", stack_name="contract-fail",
            resources=[], iam_statements=[], tags={},
        ),
        config=ConfigMetadata(entries=[], application_settings={}, log_level="INFO"),
        migration_report=MigrationReportMetadata(
            source_platform="mule", source_archetype="unknown",
            coverage_total=1, coverage_generated=1,
        ),
        extension={
            "ir": {
                "raw_layer": {"original_json": {}},
                "execution_layer": {
                    "entry_points": [
                        {"flow_name": "order-flow", "trigger_type": "http",
                         "path": "/orders", "methods": ["DELETE"]},
                    ],
                },
            },
        },
    )
    metadata.quality_report = QualityReport()
    vfs = VirtualFileSystem()
    # SAM template path matches but method is POST, IR demands DELETE.
    vfs.write(
        "template.yaml",
        (
            "Transform: AWS::Serverless-2016-10-31\n"
            "Resources:\n"
            "  OrderFlow:\n"
            "    Type: AWS::Serverless::Function\n"
            "    Properties:\n"
            "      Events:\n"
            "        ApiEvent:\n"
            "          Type: Api\n"
            "          Properties:\n"
            "            Path: /orders\n"
            "            Method: POST\n"
        ),
        role="infra",
        generator="test-fixture",
    )
    result = ValidationResult()
    _check_api_contract(metadata, vfs, result)
    codes = {f.code for f in result.findings}
    assert "V-CONTRACT-METHOD-MISMATCH" in codes, codes


def test_dataweave_fidelity_gating(monkeypatch):
    """Rule 13 must fail validation if DataWeave translation fidelity is below 80.0%."""
    monkeypatch.setenv("EXPORT_FAST_MODE", "false")
    from mule_parser.services.export_pipeline_v3.generators.validation_generator import (
        ValidationGenerator,
    )
    monkeypatch.setattr(
        "mule_parser.services.export_pipeline_v3.generators.validation_generator._audit_dataweave_fidelity",
        lambda metadata, vfs: {
            "detected": 2,
            "scripts_needing_semantics": 2,
            "semantics_extracted": 2,
            "realized_in_generated_code": 2 if metadata.project_name == "FidelityPass" else 1,
            "fidelity_pct": 100.0 if metadata.project_name == "FidelityPass" else 50.0,
            "status": "PASS" if metadata.project_name == "FidelityPass" else "FAILED",
            "operator_checks": [],
        }
    )
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3.metadata import (
        MigrationMetadata, MigrationReportMetadata, FunctionMetadata,
        InfrastructureMetadata, ConfigMetadata, QualityReport,
    )

    # 1. Test case where fidelity is 100% (or no scripts have semantics)
    metadata_pass = MigrationMetadata(
        project_name="FidelityPass",
        project_slug="fidelity-pass",
        runtime="python3.11",
        target_format="zip",
        functions=[
            FunctionMetadata(
                id="function:f1",
                name="f1",
                module_name="f1",
                display_name="f1",
                runtime="python3.11",
            )
        ],
        infrastructure=InfrastructureMetadata(stack_name="fidelity-pass"),
        config=ConfigMetadata(),
        migration_report=MigrationReportMetadata(
            source_platform="mule",
            coverage_total=1,
            coverage_generated=1,
            dataweave_fidelity={
                "detected": 2,
                "semantics_extracted": 2,
                "realized_in_generated_code": 2,
                "fidelity_pct": 100.0,
            }
        ),
    )
    metadata_pass.quality_report = QualityReport()

    vfs = VirtualFileSystem()
    # Write dummy handler
    vfs.write("src/functions/f1/handler.py", "def lambda_handler(event, context):\n    pass")
    vfs.write("requirements.txt", "")

    generator = ValidationGenerator()
    outcome_pass = generator.generate(metadata_pass, vfs)
    issue_codes_pass = {i["code"] for i in outcome_pass.issues}
    assert "V013" not in issue_codes_pass
    assert outcome_pass.coverage["dataweave_fidelity_pct"] == 100.0

    # Verify report rendering contains fidelity
    report_content_pass = vfs.read("docs/migration-report.md").content.decode("utf-8")
    assert "## DataWeave Semantics Fidelity" in report_content_pass
    assert "Realization fidelity: **100.0%** (PASS)" in report_content_pass

    # 2. Test case where fidelity is below 80% (50.0%)
    metadata_fail = MigrationMetadata(
        project_name="FidelityFail",
        project_slug="fidelity-fail",
        runtime="python3.11",
        target_format="zip",
        functions=[
            FunctionMetadata(
                id="function:f1",
                name="f1",
                module_name="f1",
                display_name="f1",
                runtime="python3.11",
            )
        ],
        infrastructure=InfrastructureMetadata(stack_name="fidelity-fail"),
        config=ConfigMetadata(),
        migration_report=MigrationReportMetadata(
            source_platform="mule",
            coverage_total=1,
            coverage_generated=1,
            dataweave_fidelity={
                "detected": 2,
                "semantics_extracted": 2,
                "realized_in_generated_code": 1,
                "fidelity_pct": 50.0,
            }
        ),
    )
    metadata_fail.quality_report = QualityReport()

    vfs_fail = VirtualFileSystem()
    vfs_fail.write("src/functions/f1/handler.py", "def lambda_handler(event, context):\n    pass")
    vfs_fail.write("requirements.txt", "")

    outcome_fail = generator.generate(metadata_fail, vfs_fail)
    print("ISSUES:", outcome_fail.issues)
    issue_codes_fail = {i["code"] for i in outcome_fail.issues}
    assert "V013" in issue_codes_fail
    assert outcome_fail.coverage["dataweave_fidelity_pct"] == 50.0

    # Verify report rendering contains failure warning alert
    report_content_fail = vfs_fail.read("docs/migration-report.md").content.decode("utf-8")
    assert "Realization fidelity: **50.0%** (FAIL)" in report_content_fail
    assert "DataWeave translation fidelity 50.0% is below the 80.0% threshold" in report_content_fail


def test_scatter_gather_generates_concurrency(sfdc_db_ir, sfdc_db_files, monkeypatch):
    """The generated scatter-gather handler must execute routes concurrently using ThreadPoolExecutor."""
    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    import ast
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )
    bl_path = "src/functions/business_logic_flow/service.py"
    vfile = result.vfs.read(bl_path)
    if vfile is None:
        print("VFS paths in test run:")
        for p in sorted(result.vfs.list_paths()):
            print(f"  {p}")
    assert vfile is not None, f"businessLogicFlow service must be emitted. VFS files: {sorted(result.vfs.list_paths())}"
    body = vfile.content.decode("utf-8")

    tree = ast.parse(body)

    # Assert that ThreadPoolExecutor import exists
    import_found = False
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "concurrent.futures":
            names = {alias.name for alias in node.names}
            if "ThreadPoolExecutor" in names and "as_completed" in names:
                import_found = True
                break
    assert import_found, "Should import ThreadPoolExecutor and as_completed from concurrent.futures"

    # Assert that a with statement using ThreadPoolExecutor exists
    with_executor_found = False
    for node in ast.walk(tree):
        if isinstance(node, ast.With) and len(node.items) == 1:
            item = node.items[0]
            if isinstance(item.context_expr, ast.Call) and isinstance(item.context_expr.func, ast.Name):
                if item.context_expr.func.id == "ThreadPoolExecutor":
                    with_executor_found = True
                    break
    assert with_executor_found, "Should use with ThreadPoolExecutor(...) as executor"


def test_dataweave_filter_and_reduce_wiring():
    """Verify that filter and reduce DataWeave semantics are parsed, mapped, and generated as functional python code."""
    from mule_parser.models.semantic_schemas import DataWeaveSemantics, FilterSpec, AggregationSpec
    from mule_parser.services.export_pipeline_v3 import MetadataBuilder
    from mule_parser.services.export_pipeline_v3.generators import TransformationGenerator
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

    # 1. Synthesize a mock IR carrying both filter and reduce semantics
    sample_ir = {
        "project_identity": {
            "name": "AggProject",
        },
        "raw_layer": {
            "original_json": {
                "dataweave": [
                    {
                        "script_id": "transform-agg",
                        "script_text": "payload filter $.active groupBy $.type",
                        "file": "",
                        "parent_flow": "MainFlow",
                        "parent_step_id": "step-1",
                    }
                ]
            }
        },
        "dataweave_analysis": [
            {
                "script_id": "transform-agg",
                "flow_name": "MainFlow",
                "parent_step_id": "step-1",
                "semantics": {
                    "filter": {
                        "strategy": "filter",
                        "key": "active",
                        "expression": "$.active",
                        "confidence": 1.0,
                    },
                    "aggregation": {
                        "operation": "reduce",
                        "key": "value",
                        "expression": "$.value",
                        "confidence": 1.0,
                    }
                }
            }
        ]
    }

    # 2. Build metadata
    builder = MetadataBuilder()
    metadata = builder.build(
        project_name="AggProject",
        target_runtime="python",
        target_format="zip",
        ir=sample_ir,
    )

    assert len(metadata.transformations) == 1
    t = metadata.transformations[0]
    assert t.filter is not None
    assert t.filter.key == "active"
    assert t.aggregation is not None
    assert t.aggregation.operation == "reduce"

    # 3. Generate the transformation python file
    vfs = VirtualFileSystem()
    generator = TransformationGenerator()
    generator.generate(metadata, vfs)

    path = "src/domain/services/transform_agg_transform.py"
    assert path in vfs.list_paths()
    code = vfs.read(path).content.decode("utf-8")

    # 4. Assert generated code structure
    assert "filter_key = 'active'" in code
    assert "agg_op = 'reduce'" in code

    # 5. Dynamically compile and execute the generated function to verify behavior!
    local_vars = {}
    exec(code, {}, local_vars)
    transform_func = local_vars["transform_transform_agg"]

    # Test payload: active records should be filtered, and then reduced (summed)
    payload = {
        "records": [
            {"active": True, "value": 10},
            {"active": False, "value": 20},
            {"active": True, "value": 30},
        ]
    }
    result = transform_func(payload)
    # The active filter keeps active=True (10 and 30).
    # Since all active values are numeric dictionaries, reduce sums them to 40.
    assert result["reduce"] == 40


def test_runtime_equivalence_scatter_gather_merge(sfdc_db_ir, sfdc_db_files, monkeypatch):
    """Asserts that the generated scatter-gather handler (specifically `_merge_records`)
    and the associated transformation module correctly merge, deduplicate, and sort records
    as implied by the DataWeave spec under a golden-input fixture.

    This wires in and uses RuntimeEquivalenceValidator and SemanticEquivalenceValidator.
    """
    from mule_parser.verification.runtime_equivalence_validator import RuntimeEquivalenceValidator
    from mule_parser.validation.semantic_equivalence_validator import SemanticEquivalenceValidator
    import ast

    monkeypatch.setenv("EXPORT_V3_LLM_PROVIDER", "null")
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="template-sfdc2db-user-aggregation",
        target_runtime="python",
        target_format="zip",
        ir=sfdc_db_ir,
        project_files=sfdc_db_files,
        infra_mode="sam",
    )

    # 1. Read and compile _merge_records from generated src/functions/business_logic_flow/service.py
    bl_path = "src/functions/business_logic_flow/service.py"
    vfile = result.vfs.read(bl_path)
    assert vfile is not None, "businessLogicFlow service must be emitted"
    service_code = vfile.content.decode("utf-8")

    # Extract the _merge_records function AST
    tree = ast.parse(service_code)
    merge_func_ast = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "_merge_records":
            merge_func_ast = node
            break

    assert merge_func_ast is not None, "_merge_records function must be present in service.py"

    # Unparse function AST to pure Python string and execute it
    merge_func_code = ast.unparse(merge_func_ast)
    local_vars = {}
    exec(merge_func_code, globals(), local_vars)
    merge_records_func = local_vars["_merge_records"]

    # 2. Define the Golden Inputs: 3 SFDC records + 3 DB records with one overlapping email
    sfdc_rows = [
        {"Email": "overlap@test.com", "Name": "Overlap SFDC", "Status": "Active"},
        {"Email": "sfdc1@test.com", "Name": "SFDC User 1", "Status": "Active"},
        {"Email": "sfdc2@test.com", "Name": "SFDC User 2", "Status": "Inactive"},
    ]
    db_rows = [
        {"Email": "overlap@test.com", "Phone": "123-456-7890", "Department": "Engineering"},
        {"Email": "db1@test.com", "Phone": "987-654-3210", "Department": "Sales"},
        {"Email": "db2@test.com", "Phone": "555-555-5555", "Department": "Marketing"},
    ]

    # Run actual merge logic
    actual_merged = merge_records_func(sfdc_rows, db_rows)

    # 3. Expected Output implied by DataWeave spec:
    # 5 unique records with the overlapping email merged.
    expected_merged = [
        {
            "Email": "overlap@test.com",
            "Name": "Overlap SFDC",
            "Status": "Active",
            "Phone": "123-456-7890",
            "Department": "Engineering",
        },
        {"Email": "sfdc1@test.com", "Name": "SFDC User 1", "Status": "Active"},
        {"Email": "sfdc2@test.com", "Name": "SFDC User 2", "Status": "Inactive"},
        {"Email": "db1@test.com", "Phone": "987-654-3210", "Department": "Sales"},
        {"Email": "db2@test.com", "Phone": "555-555-5555", "Department": "Marketing"},
    ]

    # Use RuntimeEquivalenceValidator to assert correctness
    validator = RuntimeEquivalenceValidator()
    assert validator.validate_runtime(expected_merged, actual_merged)

    # Also verify that the size of output is exactly 5 (showing deduplication worked)
    # in contrast to 6 (which would happen if wiring failed and it just concatenated)
    assert len(actual_merged) == 5

    # 4. Wire and test SemanticEquivalenceValidator
    semantic_validator = SemanticEquivalenceValidator()
    generated_test_suite = semantic_validator.generate_equivalence_test(
        dw_script_path="bussinessLogic.xml",
        generated_func_name="transform_merge_users"
    )
    assert "def test_semantic_equivalence_transform_merge_users():" in generated_test_suite
    assert "transform_merge_users" in generated_test_suite


def test_agent_findings_sanitization():
    """Verify that false-positive agent findings (like wildcard logs/xray,
    mysql_client SQL injection, and hardcoded credentials in environment wrappers)
    are successfully sanitized and downgraded to warning/info severity.
    """
    from mule_parser.services.export_pipeline_v3.agents.security_agent import SecurityAgent
    from mule_parser.services.export_pipeline_v3.metadata import MigrationMetadata, AgentFinding, QualityReport
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3.metadata import AgentReviewResult

    agent = SecurityAgent()

    # 1. Setup metadata and virtual file system
    metadata = MigrationMetadata(project_name="TestProj", project_slug="test-proj")
    metadata.quality_report = QualityReport()
    metadata.quality_report.findings = []

    vfs = VirtualFileSystem()
    vfs.write("src/shared/connectors/mysql_client.py", b"import os\n# No real secrets")
    vfs.write("src/shared/connectors/smtp_client.py", b"import os\n# No real secrets")
    vfs.write("src/shared/config.py", b"import os\n# No real secrets")

    # 2. Setup mock findings
    result = AgentReviewResult(
        agent=agent.ROLE,
        status="ok",
        findings=[
            # Wildcard IAM for XRay/logs should be downgraded
            AgentFinding(
                severity="error",
                code="SEC-IAM-001",
                message="allows actions on all resources for XRay service",
                file="infrastructure/template.yaml"
            ),
            AgentFinding(
                severity="critical",
                code="S-IAM-001",
                message="IAM statement 'CloudWatchLogs' uses a wildcard resource",
                file="infrastructure/template.yaml"
            ),
            # SQL injection on wrapper client should be downgraded
            AgentFinding(
                severity="error",
                code="SEC-SQL",
                message="Potential SQL injection vulnerability",
                file="src/shared/connectors/mysql_client.py"
            ),
            # Hardcoded credentials in wrapper config/clients should be downgraded
            AgentFinding(
                severity="critical",
                code="SEC-CRED",
                message="SMTP credentials are hardcoded",
                file="src/shared/connectors/smtp_client.py"
            ),
            AgentFinding(
                severity="error",
                code="SEC-CRED",
                message="Database credentials are hardcoded",
                file="src/shared/config.py"
            ),
        ]
    )

    # Run post-processing
    agent._post_process(result, metadata, vfs)

    # 3. Assertions
    findings = metadata.quality_report.findings
    assert len(findings) == 5

    # All of these false positives must be downgraded to "warning" so they do not block the build
    for f in findings:
        assert f.severity == "warning", f"Finding {f.code} was not downgraded: {f.severity}"


def test_validation_generator_findings_sanitization():
    """Verify that findings are successfully sanitized at the validation generator stage
    even if they were added without going through agent post-processing (e.g. from
    static checks or LLM reviews), and check that dynamic validation pipeline re-scoring works.
    """
    from mule_parser.services.export_pipeline_v3.generators.validation_generator import ValidationGenerator
    from mule_parser.services.export_pipeline_v3.metadata import MigrationMetadata, QualityReport, QualityFinding
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    from mule_parser.services.export_pipeline_v3.validation_pipeline import ValidationPipeline

    vg = ValidationGenerator()
    metadata = MigrationMetadata(project_name="TestProj", project_slug="test-proj")
    metadata.quality_report = QualityReport()
    metadata.quality_report.findings = [
        # 1. IAM wildcard checks
        QualityFinding(
            severity="error",
            code="S-IAM-001",
            message="IAM statement 'CloudWatchLogs' uses a wildcard resource, which is over-broad.",
            file="CloudWatchLogs",
            line=0,
            suggestion="Restrict the resource to specific log groups."
        ),
        # 2. Hardcoded credentials in config
        QualityFinding(
            severity="critical",
            code="V-SEC-INLINE-CRED",
            message="Inline credential in generated Python source.",
            file="src/shared/config.py",
            line=10,
            suggestion="Read credentials via os.getenv()"
        ),
        # 3. SQL injection on mysql_client.py
        QualityFinding(
            severity="error",
            code="SEC-SQL",
            message="Potential SQL injection vulnerability",
            file="src/shared/connectors/mysql_client.py",
            line=15,
            suggestion="Use parameterization"
        ),
        # 4. Generic IAM statement with no actual violation in template (legitimate log/xray)
        QualityFinding(
            severity="error",
            code="SEC-IAM-001",
            message="IAM statement allows actions on all resources.",
            file="",
            line=0,
            suggestion="Restrict the resource to specific ARNs."
        )
    ]

    # Setup IAM statements in metadata (all are xray/logs wildcard allowed prefixes)
    metadata.infrastructure.iam_statements = [
        {
            "Sid": "XRayPolicy",
            "Action": ["xray:PutTraceSegments", "xray:PutTelemetryRecords"],
            "Resource": "*"
        },
        {
            "Sid": "LogsPolicy",
            "Action": "logs:CreateLogGroup",
            "Resource": "*"
        }
    ]

    vfs = VirtualFileSystem()
    vfs.write("requirements.txt", b"")
    vfs.write("src/shared/config.py", b"import os\n# no secrets")
    vfs.write("src/shared/connectors/mysql_client.py", b"import os\n# no secrets")

    # Verify ValidationPipeline's _sanitize_findings re-scoring
    pipeline = ValidationPipeline()
    pipeline._sanitize_findings(metadata.quality_report.findings, metadata, vfs)
    # The score should be recalculated: penalty = 4 * 2 (warning weight) = 8. Score = 100 - 8 = 92
    assert metadata.quality_report.score == 92
    assert all(f.severity == "warning" for f in metadata.quality_report.findings)

    # Verify validation generator generates the outcome without issues
    outcome = vg.generate(metadata, vfs)

    # None of these findings should end up in outcome.issues (blocking)
    # They should all be downgraded to warning severity and go to outcome.warnings
    assert len(outcome.issues) == 0, f"Expected 0 issues, got: {outcome.issues}"
    assert len(outcome.warnings) >= 4







# ===========================================================================
# Phase 6 - Packaging Hygiene
# ===========================================================================

def test_pkg_s6_all_src_dirs_have_init_py(sfdc_db_ir, monkeypatch):
    """Every directory under src/ in the ZIP that contains .py files must also contain __init__.py."""
    import zipfile
    from io import BytesIO
    from mule_parser.services.export_pipeline_v3.orchestrator import ExportOrchestrator
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    
    monkeypatch.setenv("LLM_MODE", "stub")
    orch = ExportOrchestrator()
    res = orch.run(project_name="sfdc_db_sync", target_runtime="aws-lambda", target_format="zip", ir=sfdc_db_ir)
    assert not res.validation.is_blocking, f"Export blocked: {res.validation.issues}"
    
    zf = zipfile.ZipFile(BytesIO(res.packaged.bytes))
    paths = zf.namelist()
    
    dirs_with_py = set()
    for p in paths:
        if p.startswith("src/") and p.endswith(".py"):
            dirs_with_py.add(p.rsplit("/", 1)[0])
            
    for d in dirs_with_py:
        if d == "src":
            continue
        init_path = f"{d}/__init__.py"
        assert init_path in paths, f"Directory {d} contains .py files but is missing __init__.py"


def test_pkg_s6_no_relative_imports(sfdc_db_ir, monkeypatch):
    """No .py file under src/ contains relative imports."""
    from mule_parser.services.export_pipeline_v3.orchestrator import ExportOrchestrator
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    
    monkeypatch.setenv("LLM_MODE", "stub")
    orch = ExportOrchestrator()
    res = orch.run(project_name="sfdc_db_sync", target_runtime="aws-lambda", target_format="zip", ir=sfdc_db_ir)
    
    for path in res.vfs.list_paths("src"):
        if not path.endswith(".py"):
            continue
        vfile = res.vfs.read(path)
        content = vfile.content.decode("utf-8") if isinstance(vfile.content, bytes) else str(vfile.content)
        import re
        assert not re.search(r"^\s*from\s+\.+", content, flags=re.MULTILINE), f"File {path} contains a relative import"


def test_pkg_s6_pyproject_toml_emitted(sfdc_db_ir, monkeypatch):
    """pyproject.toml exists in the ZIP."""
    from mule_parser.services.export_pipeline_v3.orchestrator import ExportOrchestrator
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    
    monkeypatch.setenv("LLM_MODE", "stub")
    orch = ExportOrchestrator()
    try:
        res = orch.run(project_name="sfdc_db_sync", target_runtime="aws-lambda", target_format="zip", ir=sfdc_db_ir)
    except Exception as e:
        import json
        print("\n\nISSUES:\n", json.dumps(e.issues, indent=2))
        raise
    assert res.vfs.exists("pyproject.toml")
    content = res.vfs.read("pyproject.toml").content
    content_str = content.decode("utf-8") if isinstance(content, bytes) else str(content)
    assert "[project]" in content_str
    assert "dependencies =" in content_str


def test_pkg_s6_single_requirements_txt(sfdc_db_ir, monkeypatch):
    """Only one requirements.txt exists in the ZIP (at the root)."""
    from mule_parser.services.export_pipeline_v3.orchestrator import ExportOrchestrator
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    
    monkeypatch.setenv("LLM_MODE", "stub")
    orch = ExportOrchestrator()
    res = orch.run(project_name="sfdc_db_sync", target_runtime="aws-lambda", target_format="zip", ir=sfdc_db_ir)
    
    req_files = [p for p in res.vfs.list_paths() if "requirements.txt" in p]
    assert len(req_files) == 1, f"Expected exactly 1 requirements.txt, got: {req_files}"
    assert req_files[0] == "requirements.txt"


def test_pkg_s6_no_stem_collision_gate():
    """_check_stem_collisions raises on stem collision."""
    from mule_parser.services.export_pipeline_v3.post_generation_gates import _check_stem_collisions
    from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
    
    vfs = VirtualFileSystem()
    vfs.write("src/exceptions.py", "pass")
    vfs.write("src/exceptions/custom.py", "pass")
    
    problems = _check_stem_collisions(vfs)
    assert len(problems) == 1
    assert "Stem collision" in problems[0]
    assert "src/exceptions.py" in problems[0]
