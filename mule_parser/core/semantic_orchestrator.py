"""
core/semantic_orchestrator.py  –  Enriched parse pipeline.

This is the new top-level entry point.  It:
  1. Calls the ORIGINAL parse_mule_project() (backward-compatible, unchanged)
  2. Serialises the raw output to plain dicts
  3. Runs all semantic enrichment modules in order
  4. Returns a three-layer EnrichedOutput

Usage
-----
    from mule_parser.core.semantic_orchestrator import parse_enriched
    result = parse_enriched("path/to/project.zip")

    # Layer 1 – raw (identical to original output)
    print(result.raw)

    # Layer 2 – semantic
    for sf in result.semantic_flows:
        print(sf.flow_name, sf.business_purpose, sf.integration_pattern)

    # Layer 3 – abstract
    for af in result.abstract_flows:
        for step in af.abstract_steps:
            print(step.order, step.label)
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from mule_parser.core.orchestrator import parse_mule_project
from mule_parser.models.semantic_schemas import EnrichedOutput
from mule_parser.ir.builder import build_ir
from mule_parser.ir.storage import save_json_output
from mule_parser.ir.models import IROutput

from mule_parser.parsers.semantic_analyzer import analyze_flows
from mule_parser.parsers.pattern_detector import detect_patterns
from mule_parser.parsers.dataweave_deep_parser import deep_parse_dataweave
from mule_parser.parsers.intent_layer import build_intents
from mule_parser.parsers.error_observability import analyse_observability
from mule_parser.parsers.abstraction_layer import build_abstract_flows
from mule_parser.parsers.validation_firewall import validate as run_firewall  # NEW
from mule_parser.parsers.llm_inference_layer import (          # NEW
    build_bedrock_client,
    build_bedrock_client_for_model,
    enrich_with_llm,
)
from mule_parser.parsers.step_enricher import enrich_steps     # NEW

logger = logging.getLogger(__name__)


def parse_enriched(source: str, max_workers: int = 4) -> EnrichedOutput:
    """
    Full enriched parse.  Returns an EnrichedOutput with three layers.

    Parameters
    ----------
    source      : ZIP path, folder path, or Git URL (same as parse_mule_project)
    max_workers : thread-pool size for XML parsing (forwarded to base parser)

    Returns
    -------
    EnrichedOutput
    """
    # ── Layer 1: Run existing (raw) parser ────────────────────────────────
    logger.info("Phase 1/6  Running base parser …")
    raw_output = parse_mule_project(source, max_workers=max_workers)
    return enrich_parsed_output(raw_output)


def enrich_parsed_output(raw_output: Any) -> EnrichedOutput:
    """
    Run semantic enrichment over an already parsed MuleProjectOutput.

    This keeps the public parse_enriched() behavior intact while allowing the
    production IR pipeline to parse source code once, then reuse the raw output
    for enrichment and IR construction.
    """
    # Serialise to plain dict for downstream consumers
    raw_dict = _to_serialisable_dict(raw_output)

    enriched = EnrichedOutput(raw=raw_dict)

    # Extract lists we'll pass to enrichment modules
    flow_plans    = _get_flow_plans(raw_dict)
    connectors    = _get_connectors(raw_dict)
    dw_scripts    = _get_dataweave(raw_dict)
    error_handles = _get_error_handling(raw_dict)

    if not flow_plans:
        enriched.warnings.append("No flow execution plans found; semantic enrichment skipped.")
        return enriched

    # ── Layer 2a: Semantic analysis ───────────────────────────────────────
    logger.info("Phase 2/6  Semantic analysis …")
    try:
        enriched.semantic_flows = analyze_flows(flow_plans, connectors)
    except Exception as exc:
        _warn(enriched, f"semantic_analyzer failed: {exc}")
        logger.exception("semantic_analyzer error")

    # ── Layer 2a-LLM: Bedrock enrichment (flow + step level) ─────────────
    # Initialise diagnostics so the caller can always inspect them.
    enriched.llm_diagnostics = {
        "was_bedrock_called":          False,
        "flow_enrichment_completed":   False,
        "step_enrichment_completed":   False,
        "flows_enriched_by_llm":       0,
        "flows_on_fallback":           0,
        "steps_enriched_by_llm":       0,
        "steps_on_fallback":           0,
        "bedrock_model":               None,
        "confidence_threshold":        None,
    }

    try:
        try:
            from mule_parser.config.settings import (
                BEDROCK_MODEL_ID, LLM_CONFIDENCE_THRESHOLD, bedrock_configured,
            )
        except ImportError:
            from mule_parser.core.config import (
                BEDROCK_MODEL_ID, LLM_CONFIDENCE_THRESHOLD, bedrock_configured,
            )
        enriched.llm_diagnostics["bedrock_model"]         = BEDROCK_MODEL_ID
        enriched.llm_diagnostics["confidence_threshold"]  = LLM_CONFIDENCE_THRESHOLD

        _llm_client = build_bedrock_client()
        _complex_client = None
        try:
            from mule_parser.config.settings import BEDROCK_COMPLEX_MODEL_ID
            if BEDROCK_COMPLEX_MODEL_ID and BEDROCK_COMPLEX_MODEL_ID != BEDROCK_MODEL_ID:
                _complex_client = build_bedrock_client_for_model(BEDROCK_COMPLEX_MODEL_ID)
        except Exception:
            _complex_client = None

        if _llm_client is not None:
            enriched.llm_diagnostics["was_bedrock_called"] = True
            logger.info("Phase 2-LLM  Bedrock FLOW enrichment …")

            # Phase A: flow-level enrichment (business_purpose, summary, pattern)
            prev_confs = [_attr(sf, "confidence") for sf in enriched.semantic_flows]
            enriched.semantic_flows = enrich_with_llm(
                enriched.semantic_flows,
                flow_plans,
                client=_llm_client,
                complex_client=_complex_client,
                api_contract=(raw_dict.get("api_contract") or {}),
                confidence_threshold=LLM_CONFIDENCE_THRESHOLD,
            )
            enriched.llm_diagnostics["flow_enrichment_completed"] = True

            # Count flows that were actually LLM-enriched (confidence changed)
            llm_count = sum(
                1 for sf, prev_c in zip(enriched.semantic_flows, prev_confs)
                if _attr(sf, "inference_method") == "llm"
            )
            enriched.llm_diagnostics["flows_enriched_by_llm"] = llm_count
            enriched.llm_diagnostics["flows_on_fallback"]     = len(enriched.semantic_flows) - llm_count

            logger.info("Phase 2-LLM  Bedrock STEP enrichment …")

            # Phase B: step-level enrichment (display_name, business_description per step)
            step_index = enrich_steps(
                flow_plans,
                client=_llm_client,
                semantic_flows=enriched.semantic_flows,
            )
            enriched.enriched_steps = {
                k: {
                    "display_name":          v.display_name,
                    "business_description":  v.business_description,
                    "confidence":            v.confidence,
                    "was_llm":               v.was_llm,
                    "fallback_used":         v.fallback_used,
                    "fallback_reason":       v.fallback_reason,
                }
                for k, v in step_index.items()
            }
            enriched.llm_diagnostics["step_enrichment_completed"] = True
            enriched.llm_diagnostics["steps_enriched_by_llm"]    = sum(1 for v in step_index.values() if v.was_llm)
            enriched.llm_diagnostics["steps_on_fallback"]         = sum(1 for v in step_index.values() if v.fallback_used)

            logger.info(
                "Bedrock enrichment complete | flows_llm=%d steps_llm=%d steps_fallback=%d",
                llm_count,
                enriched.llm_diagnostics["steps_enriched_by_llm"],
                enriched.llm_diagnostics["steps_on_fallback"],
            )
        else:
            # Bedrock not configured — run rule-based step normalization (no LLM)
            logger.info("Phase 2-LLM  Bedrock not configured — running rule-based step normalization.")
            step_index = enrich_steps(flow_plans, client=None)
            enriched.enriched_steps = {
                k: {
                    "display_name":          v.display_name,
                    "business_description":  v.business_description,
                    "confidence":            v.confidence,
                    "was_llm":               False,
                    "fallback_used":         v.fallback_used,
                    "fallback_reason":       v.fallback_reason,
                }
                for k, v in step_index.items()
            }
            enriched.llm_diagnostics["steps_on_fallback"] = len(step_index)

    except Exception as exc:
        _warn(enriched, f"llm_inference_layer failed: {exc}")
        logger.exception("llm_inference_layer error")

    # ── Layer 2b: Pattern detection ───────────────────────────────────────
    logger.info("Phase 3/6  Pattern detection …")
    try:
        enriched.detected_patterns = detect_patterns(flow_plans)
    except Exception as exc:
        _warn(enriched, f"pattern_detector failed: {exc}")
        logger.exception("pattern_detector error")

    # ── Layer 2c: DataWeave deep parse ────────────────────────────────────
    logger.info("Phase 4/6  DataWeave deep parse …")
    try:
        enriched.dataweave_analysis = deep_parse_dataweave(dw_scripts, flow_plans)
        
        try:
            from mule_parser.parsers.dw_transformer import translate
            from mule_parser.models.semantic_schemas import PythonCodeFragment
            for dw_analysis in enriched.dataweave_analysis:
                if dw_analysis.semantics:
                    try:
                        fragments = translate(dw_analysis.semantics)
                        dw_analysis.generated_python = [
                            PythonCodeFragment(
                                label=f.label,
                                python_code=f.python_code,
                                imports=f.imports,
                                helpers=f.helpers,
                                confidence=f.confidence
                            )
                            for f in fragments
                        ]
                    except Exception as ex:
                        logger.warning("dw_transformer failed for %s: %s", dw_analysis.script_id, ex)
        except Exception as exc:
            _warn(enriched, f"dw_transformer pipeline failed: {exc}")
            logger.exception("dw_transformer pipeline error")

        enriched.data_lineage = _flatten_data_lineage(enriched.dataweave_analysis)
    except Exception as exc:
        _warn(enriched, f"dataweave_deep_parser failed: {exc}")
        logger.exception("dataweave_deep_parser error")

    # ── Layer 2d: Error handling & observability ──────────────────────────
    logger.info("Phase 5/6  Observability analysis …")
    logger.info("Phase 5/7  Intent inference ...")
    try:
        enriched.intents = build_intents(
            flow_plans,
            enriched.semantic_flows,
            enriched.dataweave_analysis,
        )
    except Exception as exc:
        _warn(enriched, f"intent_layer failed: {exc}")
        logger.exception("intent_layer error")

    try:
        enriched.observability = analyse_observability(flow_plans, error_handles)
    except Exception as exc:
        _warn(enriched, f"error_observability failed: {exc}")
        logger.exception("error_observability error")

    # ── Layer 3: Abstraction ──────────────────────────────────────────────
    logger.info("Phase 6/6  Building abstraction layer …")
    try:
        enriched.abstract_flows = build_abstract_flows(
            flow_plans, enriched.semantic_flows
        )
    except Exception as exc:
        _warn(enriched, f"abstraction_layer failed: {exc}")
        logger.exception("abstraction_layer error")

    # ── Validation firewall (NEW) ─────────────────────────────────────────
    # Runs AFTER enrichment so it can compare extracted vs inferred values.
    logger.info("Validation firewall running …")
    try:
        enriched.validation_report = run_firewall(flow_plans, enriched.semantic_flows)
        # Stamp each semantic flow with its per-flow validation result
        _stamp_validation_status(enriched)
    except Exception as exc:
        _warn(enriched, f"validation_firewall failed: {exc}")
        logger.exception("validation_firewall error")

    logger.info(
        "Enriched parse complete. Flows: %d, Patterns: %d, DW: %d, Warnings: %d",
        len(enriched.semantic_flows),
        len(enriched.detected_patterns),
        len(enriched.dataweave_analysis),
        len(enriched.warnings),
    )
    return enriched


# ─── Serialisation helpers ────────────────────────────────────────────────────

def _to_serialisable_dict(raw_output) -> dict[str, Any]:
    """Convert a Pydantic MuleProjectOutput to a plain dict via JSON round-trip."""
    try:
        return json.loads(raw_output.model_dump_json())
    except Exception:
        # Pydantic v1 fallback
        return json.loads(raw_output.json())


def _get_flow_plans(raw: dict) -> list[dict]:
    """
    Try the enriched flat format used by the formatted JSON output
    (flow_execution_plans) or fall back to the nested format.
    """
    plans = raw.get("flow_execution_plans") or []
    return plans


def _get_connectors(raw: dict) -> list[dict]:
    return raw.get("connectors") or []


def _get_dataweave(raw: dict) -> list[dict]:
    return raw.get("dataweave") or []


def _get_error_handling(raw: dict) -> list[dict]:
    handlers = list(raw.get("error_handling") or [])
    for flow in raw.get("flows", []) or []:
        flow_name = flow.get("name", "")
        for handler in flow.get("error_handlers", []) or []:
            entry = dict(handler)
            entry["flow_name"] = flow_name
            handlers.append(entry)
    return handlers


def _flatten_data_lineage(dataweave_analysis: list) -> list:
    lineage = []
    for analysis in dataweave_analysis:
        edges = getattr(analysis, "lineage_edges", None)
        if edges is None and isinstance(analysis, dict):
            edges = analysis.get("lineage_edges", [])
        lineage.extend(edges or [])
    return lineage


def _attr(obj: Any, key: str) -> Any:
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)


def _stamp_validation_status(enriched: "EnrichedOutput") -> None:
    """
    Mark each SemanticFlowAnalysis.is_validated based on whether the
    validation firewall produced any ERROR violations for that flow.
    """
    report = enriched.validation_report
    if report is None:
        return

    error_flows: set[str] = set()
    for v in report.violations:
        # field_path format: "semantic_flows[flow=<name>]..."
        import re
        m = re.search(r"\[flow=([^\]]+)\]", v.field_path)
        if m and v.severity == "error":
            error_flows.add(m.group(1))

    for sf in enriched.semantic_flows:
        sf.is_validated = sf.flow_name not in error_flows


def _warn(enriched: "EnrichedOutput", message: str) -> None:
    enriched.warnings.append(message)
    logger.warning(message)


# ─── IR pipeline ─────────────────────────────────────────────────────────────

def generate_ir(
    source: str,
    max_workers: int = 4,
    save: bool = True,
    base_dir: "str | Path | None" = None,
) -> "IROutput":
    """
    Full parse → enrich → IR pipeline.

    Steps
    ─────
    1. parse_mule_project()   – raw XML extraction
    2. parse_enriched()       – semantic enrichment on top of raw
    3. build_ir()             – lossless IR across all layers
    4. save_json_output()     – persist to json_outputs/<project>/output.json

    Parameters
    ----------
    source      : ZIP, folder, or Git URL
    max_workers : thread-pool size for XML parsing
    save        : whether to persist the IR JSON to disk
    base_dir    : override default ``json_outputs`` root directory

    Returns
    -------
    IROutput  –  { status, saved_path, ir }
    """
    logger.info("IR pipeline Phase 1/3  Raw parse …")
    raw_output = parse_mule_project(source, max_workers=max_workers)

    logger.info("IR pipeline Phase 2/3  Semantic enrichment …")
    enriched_output = enrich_parsed_output(raw_output)

    logger.info("IR pipeline Phase 3/3  Building IR …")
    ir_output = build_ir(raw_output, enriched_output, source)

    if save:
        project_name = ir_output.ir.project_identity.name or "unnamed_project"
        try:
            payload    = ir_output.model_dump()
            saved_path = save_json_output(payload, project_name, base_dir=base_dir)
            ir_output.saved_path = saved_path
            logger.info("IR saved → %s", saved_path)
        except Exception as exc:
            logger.error("Failed to save IR output: %s", exc)
            ir_output.status = "save_failed"

    return ir_output


# ─── Convenience: export formatted output ─────────────────────────────────────

def export_enriched(enriched: EnrichedOutput, output_path: str | Path) -> None:
    """
    Save the full EnrichedOutput (all three layers) to a JSON file.

    Parameters
    ----------
    enriched    : EnrichedOutput returned by parse_enriched()
    output_path : destination file path (will be created/overwritten)
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        json_str = enriched.model_dump_json(indent=2)
    except Exception:
        json_str = enriched.json(indent=2)          # Pydantic v1
    path.write_text(json_str, encoding="utf-8")
    logger.info("Enriched output written to %s", path)
