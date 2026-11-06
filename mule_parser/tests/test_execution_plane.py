from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Any, AsyncGenerator

from fastapi import BackgroundTasks
from fastapi import HTTPException

from mule_parser.api import execution


RUNTIME_FLOW_XML = """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:salesforce="http://www.mulesoft.org/schema/mule/salesforce"
      xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      xmlns:file="http://www.mulesoft.org/schema/mule/file"
      xmlns="http://www.mulesoft.org/schema/mule/core">
  <file:config name="File_Config">
    <file:connection workingDir="src/main/resources" />
  </file:config>
  <salesforce:sfdc-config name="Salesforce">
    <salesforce:basic-connection username="${sfdc.user}" password="${sfdc.password}" securityToken="${sfdc.securityToken}" />
  </salesforce:sfdc-config>
  <flow name="import-contacts-into-salesforceFlow">
    <scheduler>
      <scheduling-strategy>
        <fixed-frequency frequency="10000"/>
      </scheduling-strategy>
    </scheduler>
    <file:read config-ref="File_Config" path="contacts.csv" />
    <ee:transform>
      <ee:message>
        <ee:set-payload><![CDATA[%dw 2.0
output application/java
---
payload map { FirstName: $.firstname }]]></ee:set-payload>
      </ee:message>
    </ee:transform>
    <salesforce:create config-ref="Salesforce" type="Contact" />
  </flow>
</mule>
"""


def _build_project_source(tmp_path: Path) -> str:
    mule_dir = tmp_path / "src" / "main" / "mule"
    mule_dir.mkdir(parents=True)
    (mule_dir / "runtime.xml").write_text(RUNTIME_FLOW_XML, encoding="utf-8")
    return str(tmp_path)


def test_analysis_sections_and_raw_gate(tmp_path):
    project_source = _build_project_source(tmp_path)
    req = execution.AnalysisRequest(sourcePath=project_source, requestedBy="unit-test")
    start_resp = execution.start_analysis("proj-A", req, BackgroundTasks())

    # Execute background task inline for deterministic testing.
    execution._run_analysis_job(start_resp.job_id, project_source)

    latest = execution.get_latest_analysis("proj-A")
    assert latest["status"] == "completed"
    assert "analysis" in latest
    assert latest["analysis"]["raw_ir"] is None

    summary = execution.get_latest_analysis_summary("proj-A")
    assert summary["summary"]["flows"] == 1

    flows = execution.get_latest_analysis_structured_flows("proj-A")
    assert flows["structuredFlows"][0]["flow_name"] == "import-contacts-into-salesforceFlow"

    validation = execution.get_latest_analysis_validation("proj-A")
    assert validation["validation"]["status"] in {"VALID", "WARNINGS", "ERRORS"}

    raw = execution.get_raw_ir(start_resp.job_id)
    assert "rawIr" in raw

    events = execution.get_project_events("proj-A")
    assert events["events"]
    assert any(item["eventType"] == "analysis.completed" for item in events["events"])


def test_migration_requires_completed_analysis_and_returns_outputs(tmp_path):
    project_source = _build_project_source(tmp_path)
    analysis_req = execution.AnalysisRequest(sourcePath=project_source, requestedBy="unit-test")
    analysis_resp = execution.start_analysis("proj-B", analysis_req, BackgroundTasks())
    execution._run_analysis_job(analysis_resp.job_id, project_source)

    migration_req = execution.MigrationRequest(
        analysisJobId=analysis_resp.job_id,
        targetRuntime="python",
        migrationType="mule4-lambda",
    )
    try:
        execution.start_migration("proj-B", migration_req, BackgroundTasks())
        raise AssertionError("migration should require approval gates")
    except HTTPException as exc:
        assert exc.status_code == 409

    execution.approve_project_workflow(
        "proj-B",
        execution.ApprovalRequest(stage="ir", userId="unit-test"),
    )
    execution.generate_project_mapping_review(
        "proj-B",
        execution.WorkflowActionRequest(userId="unit-test", targetRuntime="python"),
    )
    execution.approve_project_workflow(
        "proj-B",
        execution.ApprovalRequest(stage="mapping", userId="unit-test"),
    )
    execution.generate_project_architecture_review(
        "proj-B",
        execution.WorkflowActionRequest(userId="unit-test", targetRuntime="python"),
    )
    execution.approve_project_workflow(
        "proj-B",
        execution.ApprovalRequest(stage="architecture", userId="unit-test"),
    )

    migration_resp = execution.start_migration("proj-B", migration_req, BackgroundTasks())
    analysis_job = execution._get_job(analysis_resp.job_id)
    execution._run_migration_job(migration_resp.job_id, analysis_job)

    latest_migration = execution.get_latest_migration("proj-B")
    assert latest_migration["status"] == "completed"
    assert latest_migration["result"]["generatedOutputs"]
    assert latest_migration["result"]["workflow"]["state"] == "CODE_GENERATED"
    assert latest_migration["result"]["generatedCode"]
    assert latest_migration["result"]["generatedOutputs"][0]["runtime"] == "python"

    events = execution.get_project_events("proj-B")
    assert any(item["eventType"] == "migration.completed" for item in events["events"])


# ─── /internal/migration/stream-file — IR enrichment integration ─────────────


class _RecordingProvider:
    """
    Captures the config the endpoint hands to the LLM so the test can
    assert the analysis IR slice was injected before any tokens were
    yielded.
    """
    name = "recording"
    model = "fake"

    def __init__(self) -> None:
        self.captured_config: dict[str, Any] | None = None
        self.captured_source: str | None = None

    async def stream_migration(
        self, source_content: str, config: dict[str, Any]
    ) -> AsyncGenerator[str, None]:
        self.captured_config = config
        self.captured_source = source_content
        # Yield a single chunk so the SSE generator completes naturally.
        yield "ok"


def _run_async(coro):
    """Run an async coroutine in a fresh event loop, blocking until done."""
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


async def _drain_sse(response) -> list[str]:
    """Collect every chunk yielded by a StreamingResponse body."""
    chunks: list[str] = []
    async for piece in response.body_iterator:
        chunks.append(piece if isinstance(piece, str) else piece.decode())
    return chunks


def test_stream_file_endpoint_enriches_llm_payload_with_ir(tmp_path, monkeypatch):
    """
    End-to-end check of the architectural principle:

      Generation Layer Must Become a Consumer of the Analysis Layer

    1. Run the analysis pipeline so the IR is stored on the AnalysisJob.
    2. POST to /internal/migration/stream-file with the project_id.
    3. Capture the config handed to the LLM provider.
    4. Assert ``analysisContext`` is populated with the per-file IR slice
       (flows, connectors, entry points, properties) — i.e. the LLM is no
       longer running blind on raw XML.
    """
    project_source = _build_project_source(tmp_path)
    analysis_req = execution.AnalysisRequest(sourcePath=project_source, requestedBy="unit-test")
    analysis_resp = execution.start_analysis("proj-IR-1", analysis_req, BackgroundTasks())
    execution._run_analysis_job(analysis_resp.job_id, project_source)

    recorder = _RecordingProvider()
    monkeypatch.setattr(
        "mule_parser.services.llm_providers.create_llm_provider",
        lambda *_args, **_kwargs: recorder,
    )

    req = execution.StreamMigrationRequest(
        projectId="proj-IR-1",
        fileName="runtime.xml",
        filePath="src/main/mule/runtime.xml",
        sourceContent=RUNTIME_FLOW_XML,
        migrationType="mule4-lambda",
        targetRuntime="python",
        projectStructure="",
        activeProvider="recording",
        providerConfig={"apiKey": "x", "enabled": True},
        instructions="",
    )

    response = _run_async(execution.generate_stream_migration(req))
    _run_async(_drain_sse(response))

    assert recorder.captured_config is not None, "endpoint never invoked the LLM provider"
    ctx = recorder.captured_config.get("analysisContext")
    assert ctx is not None, "endpoint must enrich the LLM payload with analysisContext"
    assert ctx["available"] is True
    assert ctx["scope"]["file_name"] == "runtime.xml"
    # The sample flow from the fixture must show up in the slice.
    assert "import-contacts-into-salesforceFlow" in ctx["scope"]["matched_flows"]
    # The slice must carry the trigger / connector knowledge the LLM needs.
    flow = next(
        f for f in ctx["flows_in_file"]
        if f["name"] == "import-contacts-into-salesforceFlow"
    )
    assert flow["trigger_type"] in {"scheduler", "scheduled"} or flow["entry_point"].get("trigger_type")
    connector_types = {c["connector_type"] for c in flow["connectors_used"]}
    assert "salesforce" in connector_types


def test_stream_file_endpoint_skips_ir_when_force_no_ir(tmp_path, monkeypatch):
    """
    The ad-hoc /api/migration/direct route sets ``forceNoIr: true`` because
    there's no project IR. The endpoint must respect that and call the LLM
    with ``analysisContext: None`` instead of probing the job store.
    """
    project_source = _build_project_source(tmp_path)
    analysis_req = execution.AnalysisRequest(sourcePath=project_source, requestedBy="unit-test")
    analysis_resp = execution.start_analysis("proj-IR-2", analysis_req, BackgroundTasks())
    execution._run_analysis_job(analysis_resp.job_id, project_source)

    recorder = _RecordingProvider()
    monkeypatch.setattr(
        "mule_parser.services.llm_providers.create_llm_provider",
        lambda *_args, **_kwargs: recorder,
    )

    req = execution.StreamMigrationRequest(
        projectId="proj-IR-2",
        forceNoIr=True,
        fileName="runtime.xml",
        filePath="src/main/mule/runtime.xml",
        sourceContent=RUNTIME_FLOW_XML,
        activeProvider="recording",
        providerConfig={"apiKey": "x", "enabled": True},
    )

    response = _run_async(execution.generate_stream_migration(req))
    _run_async(_drain_sse(response))

    assert recorder.captured_config is not None
    assert recorder.captured_config.get("analysisContext") is None


def test_stream_file_endpoint_handles_missing_project_id(tmp_path, monkeypatch):
    """Without projectId/analysisJobId the endpoint must not error — it should
    just degrade to a raw-only prompt (analysisContext is None)."""
    recorder = _RecordingProvider()
    monkeypatch.setattr(
        "mule_parser.services.llm_providers.create_llm_provider",
        lambda *_args, **_kwargs: recorder,
    )

    req = execution.StreamMigrationRequest(
        fileName="snippet.xml",
        filePath="snippet.xml",
        sourceContent=RUNTIME_FLOW_XML,
        activeProvider="recording",
        providerConfig={"apiKey": "x", "enabled": True},
    )

    response = _run_async(execution.generate_stream_migration(req))
    _run_async(_drain_sse(response))

    assert recorder.captured_config is not None
    assert recorder.captured_config.get("analysisContext") is None
