"""Local structural checks for generated SAP iFlow archives."""
from __future__ import annotations

from typing import Any

from mule_parser.platforms.sap.sap_reference_analyzer import (
    SAPReferenceError, analyze_sap_reference,
)


def validate_sap_artifacts(artifacts: list[tuple[str, bytes]], profile: dict[str, Any] | None = None) -> dict[str, Any]:
    results = []
    seen: set[str] = set()
    for artifact_id, payload in artifacts:
        errors: list[str] = []
        warnings: list[str] = []
        if not artifact_id or not artifact_id.strip():
            errors.append("Artifact identifier is missing.")
        elif artifact_id in seen:
            errors.append("Duplicate artifact identifier.")
        seen.add(artifact_id)
        try:
            parsed = analyze_sap_reference(payload, f"{artifact_id or 'artifact'}.zip")
            flow = parsed["artifacts"][0]
            if flow.get("artifact_id") and flow["artifact_id"] != artifact_id:
                warnings.append("Request artifact identifier differs from MANIFEST Bundle-SymbolicName.")
            for bpmn in flow["bpmn"]:
                if not bpmn["valid_xml"]:
                    errors.append(bpmn["error"])
                if bpmn.get("unresolved_sequence_flows"):
                    errors.append("Sequence flow references an unknown BPMN element.")
                if bpmn.get("illegal_subproc_flows"):
                    errors.append("Sequence flow illegally connected to event sub-process.")
                if bpmn.get("illegal_timer_flows"):
                    errors.append("Message flow illegally connected to timer start event.")
            if not flow.get("artifact_id"):
                errors.append("MANIFEST Bundle-SymbolicName is missing.")
            warnings.extend(flow["manifest_warnings"])
            if not flow["adapters"]:
                warnings.append("No adapter configuration was confidently identified.")
        except SAPReferenceError as exc:
            errors.append(str(exc))
        if profile:
            reference_adapters = {a.get("type") for a in profile.get("adapter_inventory", []) if a.get("type")}
            if reference_adapters:
                warnings.append("Reference adapter types available for comparison: " + ", ".join(sorted(reference_adapters)))
        status = "ERROR" if errors else "WARNING" if warnings else "PASS"
        results.append({"artifact_id": artifact_id, "status": status, "errors": errors, "warnings": warnings,
                        "validation_scope": "local_structural_only"})
    counts = {s: sum(1 for result in results if result["status"] == s) for s in ("PASS", "WARNING", "ERROR")}
    overall = "error" if counts["ERROR"] else "warning" if counts["WARNING"] else "passed"
    return {"validation_status": overall, "reference_used": profile is not None,
            "summary": {"total_artifacts": len(results), "passed": counts["PASS"], "warnings": counts["WARNING"], "failed": counts["ERROR"]},
            "artifacts": results,
            "disclaimer": "Local structural validation does not confirm SAP import, tenant permissions, deployment, or runtime compatibility."}
