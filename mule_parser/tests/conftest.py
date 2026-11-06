import os
import sys

# Force LLM provider to null and disable codegen LLM globally for pytest
os.environ["EXPORT_V3_LLM_PROVIDER"] = "null"
os.environ["CODEGEN_LLM_ENABLED"] = "false"
os.environ["LLM_ENABLED"] = "false"

# Import settings to trigger load_dotenv
import mule_parser.config.settings as settings

# Override settings variables to ensure they are disabled during test execution
settings.LLM_ENABLED = False
settings.CODEGEN_LLM_ENABLED = False
settings.AWS_ACCESS_KEY_ID = None
settings.AWS_SECRET_ACCESS_KEY = None

# Mock Celery send_task globally to prevent connection refused errors in tests
from unittest.mock import MagicMock
from celery import Celery
import pytest

Celery.send_task = MagicMock(return_value=MagicMock(id="mock-task-id", status="PENDING"))


def _flow(name, *, file, source=None, processors=None, error_handlers=None):
    return {
        "name": name,
        "file": file,
        "source": source,
        "processors": processors or [],
        "error_handlers": error_handlers or [],
    }


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
                {"name": "triggerFlow", "source": {"type": "http:listener"}},
                {"name": "mainFlow"},
                {"name": "businessLogicFlow"},
                {"name": "errorHandlingFlow"},
            ],
        },
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


@pytest.fixture
def batch_simple_ir() -> dict:
    """Minimal scheduler-driven IR that classifies as BATCH_SIMPLE."""
    ir = {
        "project_identity": {
            "name": "NightlySync",
            "application_archetype": "scheduled_job",
            "source_type": "mule4",
        },
        "raw_layer": {
            "original_json": {
                "migration_type": "batch_simple",
                "batch_size": "simple",
                "migration_type_confidence": 0.95,
                "flows": [
                    {
                        "name": "nightlySync",
                        "file": "src/main/mule/nightly.xml",
                        "source": {
                            "type": "scheduler",
                            "attributes": {"frequency": "0 0 * * *"},
                        },
                        "processors": [{"type": "db:select", "config_ref": "Database_Config"}],
                    }
                ],
                "connectors": [
                    {"connector_type": "db", "config_id": "Database_Config"},
                ],
            },
        },
        "flow_execution_plans": [
            {"flow_name": "nightlySync", "trigger_type": "scheduler", "steps": []},
        ],
    }
    ir.setdefault("gap_layer", {})["feasibility_decision"] = {
        "verdict": "FEASIBLE",
        "confidence": 0.95,
        "blockers": [],
    }
    from mule_parser.services.export_pipeline_v3.analysis_contract import stamp_analysis_contract
    return stamp_analysis_contract(ir)


@pytest.fixture
def batch_simple_plan() -> dict:
    return {
        "summary": {"service_counts": {"RDS": 1}},
        "flows": [
            {
                "flow_name": "nightlySync",
                "purpose": "Sync nightly data.",
                "component_decisions": [{"source": "db", "target": "RDS"}],
            }
        ],
    }


@pytest.fixture
def batch_complex_ir() -> dict:
    """Minimal IR with batch_jobs + chunking → BATCH_COMPLEX."""
    ir = {
        "project_identity": {
            "name": "ComplexBatch",
            "application_archetype": "batch_job",
            "source_type": "mule4",
        },
        "raw_layer": {
            "original_json": {
                "migration_type": "batch_complex",
                "batch_size": "complex",
                "migration_type_confidence": 0.95,
                "batch_jobs": [{"name": "ordersBatch"}],
                "flows": [
                    {
                        "name": "ordersBatch",
                        "file": "src/main/mule/orders-batch.xml",
                        "source": {
                            "type": "scheduler",
                            "attributes": {"frequency": "0 2 * * *"},
                        },
                        "processors": [
                            {"type": "batch:step"},
                            {"type": "scatter_gather"},
                            {"type": "batch:aggregator"},
                        ],
                        "metadata": {"estimated_records": 50_000},
                        "error_handlers": [{"type": "on-error-continue"}],
                    }
                ],
                "connectors": [
                    {"connector_type": "db", "config_id": "Database_Config"},
                ],
            },
        },
        "batch_jobs": [{"name": "ordersBatch"}],
        "flow_execution_plans": [
            {
                "flow_name": "ordersBatch",
                "trigger_type": "scheduler",
                "metadata": {"estimated_records": 50_000},
                "error_handling": {"kind": "on_error_continue"},
                "steps": [
                    {"type": "batch:step"},
                    {"type": "scatter_gather"},
                    {"type": "batch:aggregator"},
                ],
            }
        ],
    }
    ir.setdefault("gap_layer", {})["feasibility_decision"] = {
        "verdict": "FEASIBLE",
        "confidence": 0.95,
        "blockers": [],
    }
    from mule_parser.services.export_pipeline_v3.analysis_contract import stamp_analysis_contract
    return stamp_analysis_contract(ir)


@pytest.fixture
def batch_complex_plan() -> dict:
    return {
        "summary": {"service_counts": {"RDS": 1, "SQS": 1}},
        "flows": [
            {
                "flow_name": "ordersBatch",
                "purpose": "Process a large daily orders batch.",
                "component_decisions": [
                    {"source": "scheduler", "target": "EventBridge"},
                    {"source": "db", "target": "RDS"},
                ],
            }
        ],
    }

