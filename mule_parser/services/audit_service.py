from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from mule_parser.ir.models import IntermediateRepresentation


AGENT_VERSION = "deterministic-mule-aws-v1"


class AuditDecisionRecord(BaseModel):
    ir_hash: str
    timestamp: str
    flow_name: str = ""
    component: str = ""
    target: str = ""
    confidence: float = 0.0
    mapping_rule_used: dict[str, Any] = Field(default_factory=dict)
    kb_chunks_used: list[str] = Field(default_factory=list)
    explanation: str = ""
    agent_version: str = AGENT_VERSION


class AuditReport(BaseModel):
    ir_hash: str
    timestamp: str
    agent_version: str = AGENT_VERSION
    decisions: list[AuditDecisionRecord] = Field(default_factory=list)


def compute_ir_hash(ir: IntermediateRepresentation | dict[str, Any]) -> str:
    payload = ir.model_dump() if isinstance(ir, IntermediateRepresentation) else ir
    encoded = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_audit_report(
    ir: IntermediateRepresentation | dict[str, Any],
    migration_plan: Any,
    *,
    agent_version: str = AGENT_VERSION,
) -> AuditReport:
    ir_hash = compute_ir_hash(ir)
    now = datetime.now(timezone.utc).isoformat()
    decisions: list[AuditDecisionRecord] = []
    plan = migration_plan.model_dump() if hasattr(migration_plan, "model_dump") else migration_plan

    for flow in plan.get("flows", []):
        flow_rule = {
            "mule_component": flow.get("flow_type", "Mule Flow"),
            "aws_target": flow.get("source_target", ""),
            "migration_template": flow.get("migration_template", ""),
        }
        decisions.append(
            AuditDecisionRecord(
                ir_hash=ir_hash,
                timestamp=now,
                flow_name=flow.get("flow_name", ""),
                component=flow.get("flow_type", "Mule Flow"),
                target=flow.get("source_target", ""),
                confidence=float(flow.get("confidence", 0.0) or 0.0),
                mapping_rule_used=flow.get("mapping_rule_used") or flow_rule,
                kb_chunks_used=_chunk_ids(flow.get("kb_chunks_used", [])),
                explanation=flow.get("explanation", ""),
                agent_version=agent_version,
            )
        )
        for item in flow.get("component_decisions", []):
            decisions.append(
                AuditDecisionRecord(
                    ir_hash=ir_hash,
                    timestamp=now,
                    flow_name=item.get("flow_name", flow.get("flow_name", "")),
                    component=item.get("source", ""),
                    target=item.get("target", ""),
                    confidence=float(item.get("confidence", 0.0) or 0.0),
                    mapping_rule_used=item.get("mapping_rule_used", {}),
                    kb_chunks_used=_chunk_ids(item.get("kb_chunks_used", [])),
                    explanation=item.get("explanation", ""),
                    agent_version=agent_version,
                )
            )

    return AuditReport(ir_hash=ir_hash, timestamp=now, agent_version=agent_version, decisions=decisions)


def write_audit_report(report: AuditReport, path: str | Path) -> Path:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report.model_dump_json(indent=2), encoding="utf-8")
    return output_path


def _chunk_ids(chunks: list[Any]) -> list[str]:
    ids: list[str] = []
    for chunk in chunks:
        if isinstance(chunk, str):
            ids.append(chunk)
        elif isinstance(chunk, dict) and chunk.get("chunk_id"):
            ids.append(str(chunk["chunk_id"]))
    return ids
