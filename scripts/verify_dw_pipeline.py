"""Run DataWeave pipeline integrity check on Testing_batch IR."""
import json
import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from mule_parser.parsers.dw_pipeline_integrity import audit_pipeline
from mule_parser.parsers.dw_preservation import preserve_dataweave, wrap_module_with_provenance
from mule_parser.services.export_pipeline.vfs import VirtualFileSystem

ir_path = ROOT / "frontend/IR_Outputs/Testing_batch/Testing_batch_unknown_20260619_145846_a7bd26.json"
ir = json.loads(ir_path.read_text(encoding="utf-8"))["ir"]
dw = ir["raw_layer"]["original_json"]["dataweave"][0]
text = dw["script_text"]

result = preserve_dataweave(
    text,
    function_name="transform_collection_to_csv_set_payload",
    output_format="application/csv",
)
module = wrap_module_with_provenance(
    impl=result.code,
    description="Testing_batch CSV transform",
    name="transform-collection-to-csv",
    output_format="application/csv",
    parent_flow="businessLogicFlow",
    source_body=text,
    strategy=result.strategy,
    confidence=result.confidence,
)

meta = SimpleNamespace(
    id="transform:testing",
    name="transform-collection-to-csv",
    module_name="transform_collection_to_csv_set_payload",
    function_name="transform_collection_to_csv_set_payload",
    source_body=text,
    output_format="application/csv",
)

vfs = VirtualFileSystem()
vfs.write("src/shared/transformations/transform_collection_to_csv_set_payload.py", module, role="source", generator="verify")

report = audit_pipeline(ir=ir, transformations=[meta], vfs_read=vfs.read)
print("PIPELINE STATUS", report.status)
print("FIDELITY", report.fidelity_pct, "%")
print("IR SCRIPTS", report.total_ir_scripts)
print("GAPS", report.gaps or "(none)")
print("STRATEGY", result.strategy.value, "complete=", result.is_complete)

from mule_parser.parsers.dw_golden_io import audit_export_against_golden

golden = audit_export_against_golden(
    transformations=[meta],
    vfs_read=vfs.read,
    repo_root=ROOT / "mule_parser",
)
print("GOLDEN I/O", golden.get("status"), golden.get("fidelity_pct"), "%")
for check in golden.get("checks") or []:
    print(" ", check)
