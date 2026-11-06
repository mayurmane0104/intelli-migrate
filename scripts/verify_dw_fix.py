"""Verify DataWeave scatter-gather merge script compiles with full operator fidelity."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from mule_parser.parsers.dataweave_semantics import extract_semantics
from mule_parser.parsers.dw_preservation import preserve_dataweave

p = ROOT / "frontend/IR_Outputs/Testing_batch/Testing_batch_unknown_20260619_145846_a7bd26.json"
ir = json.loads(p.read_text(encoding="utf-8"))["ir"]
dw = ir["raw_layer"]["original_json"]["dataweave"][0]
text = dw["script_text"]

sem = extract_semantics(text)
print("SEMANTICS", {
    "merge_keys": sem.join.key if sem.join else None,
    "join_strategy": sem.join.strategy if sem.join else None,
    "dedup_keys": sem.dedup.key if sem.dedup else None,
    "sort": sem.sort.model_dump() if sem.sort else None,
    "output_format": sem.projection.output_format if sem.projection else None,
})

result = preserve_dataweave(
    text,
    function_name="transform_collection_to_csv_set_payload",
    output_format="application/csv",
    field_mappings=dw.get("field_mappings", {}),
)
code = result.code
checks = {
    "mergeWith": "merge_on_key" in (code or ""),
    "distinctBy": "distinct_by" in (code or ""),
    "sort": "sort_by_field_presence" in (code or "") or ".sort(" in (code or ""),
    "scatter_routes": "route_rows" in (code or ""),
    "csv": "records_to_csv" in (code or ""),
    "NOT_bad_mapper": 'payload.get("Name")' not in (code or ""),
    "no_sfdc_hardcode": "sfdc_users" not in (code or "").lower(),
}
print("COMPILED", checks)
print("ALL_PASS", all(checks.values()))
print("PRESERVATION", {
    "strategy": result.strategy.value,
    "complete": result.is_complete,
    "confidence": result.confidence,
})
