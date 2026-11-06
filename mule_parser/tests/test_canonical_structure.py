"""Tests for the canonical migration-type / output-structure stack.

Covers:
- ``ir.batch_classifier.classify_batch`` priority rules.
- ``ir.migration_type_detector.detect_migration_type`` for batch / API / scheduler.
- ``services.export_pipeline_v3.output_structure`` registry and helpers.
- ``MigrationMetadata.migration_type / batch_size / output_structure`` end-to-end
  wiring through the v3 ``ExportOrchestrator``.
- Architectural-planner canonical-role attachment for batch_complex.
- Generator output paths:
    * canonical Lambda handler.py files per spec
    * canonical Terraform skeletons for batch_simple/complex
    * Step Functions ASL for batch_complex
    * tests/events/*.json per spec
    * docs/mule-batch-mapping.md for batch projects
    * type-aware GitHub Actions workflow
"""
from __future__ import annotations

import io
import json
import zipfile

import pytest

from mule_parser.ir.batch_classifier import (
    BatchSize,
    BatchClassification,
    classify_batch,
)
from mule_parser.ir.migration_type_detector import detect_migration_type
from mule_parser.services.export_pipeline_v3.orchestrator import ExportOrchestrator
from mule_parser.services.export_pipeline_v3.output_structure import (
    API_STRUCTURE,
    BATCH_COMPLEX_STRUCTURE,
    BATCH_SIMPLE_STRUCTURE,
    MigrationType,
    STRUCTURE_REGISTRY,
    get_structure,
    is_batch,
)


# ---------------------------------------------------------------------------
# 1. Batch classifier
# ---------------------------------------------------------------------------


def test_batch_classifier_simple_when_single_step_low_volume():
    # A flow with non-batch steps and zero record-count → SIMPLE.
    ir = {
        "batch_jobs": [{"name": "smallBatch", "estimated_record_count": 500}],
        "flow_execution_plans": [
            {
                "flow_name": "smallBatch",
                "steps": [{"type": "set-payload"}],
            }
        ],
    }
    result = classify_batch(ir)
    assert isinstance(result, BatchClassification)
    assert result.size == BatchSize.SIMPLE
    assert any("simple" in r.lower() for r in result.reasoning)


def test_batch_classifier_complex_when_chunking_or_recovery():
    ir = {
        "batch_jobs": [{"name": "ordersBatch", "estimated_record_count": 5_000}],
        "error_handling_flows": [{"name": "global-error"}],
        "flow_execution_plans": [
            {
                "flow_name": "ordersBatch",
                "steps": [
                    {"type": "batch:step"},
                    {"type": "scatter-gather"},
                    {"type": "batch:aggregator"},
                ],
            }
        ],
    }
    result = classify_batch(ir)
    assert result.size == BatchSize.COMPLEX


def test_batch_classifier_large_when_volume_or_duration_exceeds_lambda_limits():
    ir = {
        "batch_jobs": [
            {"name": "megaBatch", "estimated_record_count": 5_000_000},
        ],
        "duration_hint": "long-running",
        "flow_execution_plans": [
            {
                "flow_name": "megaBatch",
                "steps": [{"type": "set-payload"}],
            }
        ],
    }
    result = classify_batch(ir)
    assert result.size == BatchSize.LARGE


def test_batch_classifier_handles_empty_ir():
    result = classify_batch({})
    # No batch_jobs → defaults to SIMPLE with low confidence, but never crashes.
    assert isinstance(result, BatchClassification)
    assert result.size == BatchSize.SIMPLE


# ---------------------------------------------------------------------------
# 2. Migration-type detector
# ---------------------------------------------------------------------------


def test_detector_returns_api_for_http_listener():
    ir = {
        "flow_execution_plans": [
            {"flow_name": "ordersApi", "trigger_type": "http:listener", "steps": []}
        ]
    }
    res = detect_migration_type(ir)
    assert res.migration_type == MigrationType.API
    assert res.batch_size is None


def test_detector_returns_api_with_zero_confidence_for_scheduler_only():
    ir = {
        "flow_execution_plans": [
            {"flow_name": "nightlySync", "trigger_type": "scheduler", "steps": []}
        ]
    }
    res = detect_migration_type(ir)
    assert res.migration_type == MigrationType.API
    assert res.confidence == 0.0


def test_detector_returns_batch_complex_when_batch_jobs_with_complexity():
    ir = {
        "batch_jobs": [{"name": "complexBatch"}],
        "flow_execution_plans": [
            {
                "flow_name": "complexBatch",
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
    res = detect_migration_type(ir)
    assert res.migration_type == MigrationType.BATCH_COMPLEX
    assert res.batch_size == "complex"


def test_detector_defaults_to_api_when_no_signals():
    res = detect_migration_type({})
    assert res.migration_type == MigrationType.API
    assert res.confidence < 0.9  # default has low confidence


# ---------------------------------------------------------------------------
# 3. Output-structure registry
# ---------------------------------------------------------------------------


def test_structure_registry_has_all_four_types():
    assert MigrationType.BATCH_SIMPLE in STRUCTURE_REGISTRY
    assert MigrationType.BATCH_COMPLEX in STRUCTURE_REGISTRY
    assert MigrationType.API in STRUCTURE_REGISTRY


def test_batch_complex_structure_declares_three_lambdas_and_step_functions():
    spec = BATCH_COMPLEX_STRUCTURE
    handler_paths = [p for p in spec.lambda_functions if p.endswith("handler.py")]
    assert len(handler_paths) == 3
    assert "src/handlers/batch_trigger_handler.py" in spec.lambda_functions
    assert "src/handlers/record_processor_handler.py" in spec.lambda_functions
    assert "src/handlers/batch_completion_handler.py" in spec.lambda_functions
    assert spec.requires_step_functions is True
    assert spec.requires_sqs is True


def test_batch_simple_structure_declares_one_lambda_no_sqs():
    spec = BATCH_SIMPLE_STRUCTURE
    assert spec.lambda_functions == ["src/handlers/lambda_handler.py"]
    assert spec.requires_step_functions is False
    assert spec.requires_sqs is False


def test_api_structure_declares_one_lambda():
    spec = API_STRUCTURE
    assert spec.lambda_functions == ["src/handlers/api_handler.py"]
    assert spec.requires_step_functions is False
    assert spec.requires_sqs is False


def test_get_structure_accepts_enum_and_string():
    assert get_structure(MigrationType.API) is API_STRUCTURE
    assert get_structure("api") is API_STRUCTURE
    assert get_structure("batch_simple") is BATCH_SIMPLE_STRUCTURE
    with pytest.raises(ValueError):
        get_structure("unknown_type")


def test_is_batch_helper_recognises_batch_types():
    assert is_batch(MigrationType.BATCH_SIMPLE) is True
    assert is_batch("batch_complex") is True
    assert is_batch("api") is False
    assert is_batch(None) is False


# ---------------------------------------------------------------------------
# 4. Orchestrator wiring (batch_simple end-to-end)
# ---------------------------------------------------------------------------


def _packaged_paths(packaged) -> dict[str, bytes]:
    """Return ``{vfs-path: contents-bytes}`` for everything in the packaged zip.

    The packager prepends the project slug as the top-level directory in the
    archive (e.g. ``nightly-sync/src/app/lambda_handler.py``); these tests
    care about the VFS-relative path, so we strip the leading slug segment.
    """
    out: dict[str, bytes] = {}
    with zipfile.ZipFile(io.BytesIO(packaged.bytes)) as zf:
        for info in zf.infolist():
            name = info.filename
            if "/" in name:
                _slug, _, rest = name.partition("/")
                out[rest] = zf.read(name)
            else:
                out[name] = zf.read(name)
    return out


def _vfs_paths(result) -> dict[str, bytes]:
    """Collect VFS file bodies keyed by path (preferred over packaging)."""
    out: dict[str, bytes] = {}
    for path in result.vfs.list_paths():
        vfile = result.vfs.read(path)
        if vfile is None:
            continue
        content = vfile.content if isinstance(vfile.content, bytes) else str(vfile.content).encode()
        out[path] = content
    return out


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


def test_orchestrator_pins_migration_type_for_batch_simple(batch_simple_ir, batch_simple_plan):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="NightlySync",
        target_runtime="python",
        target_format="zip",
        ir=batch_simple_ir,
        migration_plan=batch_simple_plan,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )
    metadata = result.metadata
    assert metadata.migration_type == MigrationType.BATCH_SIMPLE.value
    assert metadata.batch_size == "simple"
    assert metadata.output_structure is BATCH_SIMPLE_STRUCTURE
    # The canonical Lambda handler must be present at the spec path.
    canonical_paths = _vfs_paths(result)
    assert "src/handlers/lambda_handler.py" in canonical_paths
    # The mule-batch-mapping doc must be generated.
    assert "docs/mule-batch-mapping.md" in canonical_paths


# ---------------------------------------------------------------------------
# 5. Generator output paths (synthetic VFS smoke test for batch_complex)
# ---------------------------------------------------------------------------


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


def test_orchestrator_emits_canonical_files_for_batch_complex(
    batch_complex_ir, batch_complex_plan,
):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="ComplexBatch",
        target_runtime="python",
        target_format="zip",
        ir=batch_complex_ir,
        migration_plan=batch_complex_plan,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )
    metadata = result.metadata
    assert metadata.migration_type == MigrationType.BATCH_COMPLEX.value
    assert metadata.batch_size == "complex"
    assert metadata.output_structure is BATCH_COMPLEX_STRUCTURE
    assert metadata.infrastructure.requires_step_functions is True
    assert metadata.infrastructure.requires_sqs is True

    paths = _vfs_paths(result)
    # All three canonical Lambdas must be emitted.
    for required in (
        "src/handlers/batch_trigger_handler.py",
        "src/handlers/record_processor_handler.py",
        "src/handlers/batch_completion_handler.py",
    ):
        assert required in paths, f"missing canonical lambda: {required}"

    # Step Functions ASL must be emitted.
    asl_path = "infrastructure/step-functions/batch_state_machine.asl.json"
    assert asl_path in paths

    # Verify the ASL is valid JSON.
    parsed = json.loads(paths[asl_path].decode("utf-8"))
    assert parsed["StartAt"] == "Trigger"
    assert "States" in parsed

    # mule-batch-mapping.md is mandatory for batch projects.
    assert "docs/mule-batch-mapping.md" in paths


def test_test_event_jsons_are_emitted_per_canonical_spec(
    batch_complex_ir, batch_complex_plan,
):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="ComplexBatch",
        target_runtime="python",
        target_format="zip",
        ir=batch_complex_ir,
        migration_plan=batch_complex_plan,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )
    paths = _vfs_paths(result)
    for required in BATCH_COMPLEX_STRUCTURE.test_event_files:
        assert required in paths, f"missing canonical test event: {required}"


def test_github_actions_workflow_is_type_aware(
    batch_complex_ir, batch_complex_plan,
):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="ComplexBatch",
        target_runtime="python",
        target_format="zip",
        ir=batch_complex_ir,
        migration_plan=batch_complex_plan,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )
    paths = _vfs_paths(result)
    body = paths["deployment/pipelines/github-actions.yml"].decode("utf-8")
    # batch_complex must trigger Terraform validate + ASL syntax check.
    assert "Terraform validate" in body
    assert "Validate Step Functions ASL" in body
    assert "MIGRATION_TYPE: batch_complex" in body


# ---------------------------------------------------------------------------
# 6. Architectural-planner: canonical role attachment
# ---------------------------------------------------------------------------


def test_architectural_planner_attaches_canonical_role_for_single_lambda(
    batch_simple_ir, batch_simple_plan,
):
    orchestrator = ExportOrchestrator()
    result = orchestrator.run(
        project_name="NightlySync",
        target_runtime="python",
        target_format="zip",
        ir=batch_simple_ir,
        migration_plan=batch_simple_plan,
        infra_mode="terraform",
        canonical_layout=True,
        package_export=False,
    )
    # Single-Lambda projects always route every flow to the same canonical role.
    for fn in result.metadata.functions:
        assert fn.architecture is not None
        assert fn.architecture.canonical_role == "handlers"
