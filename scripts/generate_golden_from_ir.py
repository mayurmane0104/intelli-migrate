"""Bootstrap golden fixtures from IR scripts with complete preservation."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from mule_parser.parsers.dw_golden_io import DEFAULT_FIXTURES_ROOT, run_golden_fixture, load_fixture
from mule_parser.parsers.dw_preservation import preserve_dataweave

IR_ROOT = ROOT / "frontend/IR_Outputs"
OUT_ROOT = ROOT / "mule_parser/tests/fixtures/dataweave"


def _slug(text: str) -> str:
    h = hashlib.sha256(text.encode()).hexdigest()[:10]
    return f"auto_{h}"


def main() -> int:
    existing_hashes: set[str] = set()
    for d in OUT_ROOT.iterdir():
        if not d.is_dir():
            continue
        try:
            fx = load_fixture(d, repo_root=ROOT / "mule_parser")
            if fx.script.strip():
                existing_hashes.add(hashlib.sha256(fx.script.encode()).hexdigest())
        except (OSError, ValueError, KeyError, json.JSONDecodeError):
            continue

    created = 0
    for p in sorted(IR_ROOT.rglob("*.json")):
        try:
            ir = json.loads(p.read_text(encoding="utf-8")).get("ir") or json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        dws = (ir.get("raw_layer") or {}).get("original_json", {}).get("dataweave") or []
        for idx, dw in enumerate(dws):
            script = (dw.get("script_text") or "").strip()
            if not script:
                continue
            h = hashlib.sha256(script.encode()).hexdigest()
            if h in existing_hashes:
                continue
            result = preserve_dataweave(script, function_name="transform_auto", output_format="")
            if not result.is_complete or "NotImplementedError" in result.code:
                continue
            # Only register catalogue entry — operator must add input/expected manually
            # unless script matches a known pattern with existing fixture.
            rel = p.relative_to(ROOT / "mule_parser").as_posix()
            slug = _slug(script)
            out_dir = OUT_ROOT / slug
            if out_dir.exists():
                existing_hashes.add(h)
                continue
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "fixture.json").write_text(
                json.dumps(
                    {
                        "id": slug,
                        "description": f"Auto-catalogued from {p.parent.name} (needs input/expected)",
                        "function_name": "transform_auto",
                        "output_format": "",
                        "ir_relative": rel,
                        "ir_dataweave_index": idx,
                        "compare": {"records": True, "record_order": False, "body": False},
                        "status": "catalogue_only",
                    },
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            existing_hashes.add(h)
            created += 1
            print(f"catalogued: {slug} from {p.parent.name}")

    print(f"Created {created} catalogue entries under {OUT_ROOT}")
    print("Add input.json and expected.json to enable golden I/O for each.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
