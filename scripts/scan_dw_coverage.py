"""Scan IR outputs for DataWeave preservation coverage."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from mule_parser.parsers.dw_preservation import analyze_operators, preserve_dataweave

IR_ROOT = ROOT / "frontend/IR_Outputs"


def main() -> int:
    seen: set[str] = set()
    rows: list[dict] = []

    for p in sorted(IR_ROOT.rglob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        ir = data.get("ir") or data
        dws = (ir.get("raw_layer") or {}).get("original_json", {}).get("dataweave") or []
        for i, dw in enumerate(dws):
            text = (dw.get("script_text") or "").strip()
            if not text:
                continue
            h = hashlib.sha256(text.encode()).hexdigest()
            if h in seen:
                continue
            seen.add(h)
            ops = analyze_operators(text)
            result = preserve_dataweave(text, function_name="transform_test", output_format="")
            rows.append({
                "project": p.parent.name,
                "ir_file": p.name,
                "index": i,
                "length": len(text),
                "operators": [k for k, v in ops.items() if v],
                "strategy": result.strategy.value,
                "complete": result.is_complete,
                "blocked": "NotImplementedError" in result.code,
                "hash": h[:12],
            })

    complete = sum(1 for r in rows if r["complete"])
    blocked = sum(1 for r in rows if r["blocked"])
    blocked_with_ops = sum(1 for r in rows if r["blocked"] and r["operators"])
    trivial_blocked = sum(1 for r in rows if r["blocked"] and not r["operators"])

    print(f"Unique DataWeave scripts: {len(rows)}")
    print(f"Preservation complete:    {complete} ({round(complete/len(rows)*100,1) if rows else 0}%)")
    print(f"Blocked (NotImplemented): {blocked}")
    print(f"  with operators:         {blocked_with_ops}")
    print(f"  trivial / no operators: {trivial_blocked}")
    print()
    print("By strategy:")
    by_strat: dict[str, int] = {}
    for r in rows:
        by_strat[r["strategy"]] = by_strat.get(r["strategy"], 0) + 1
    for k, v in sorted(by_strat.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    print()
    print("Blocked scripts with operators (priority for golden fixtures + codegen):")
    for r in rows:
        if r["blocked"] and r["operators"]:
            print(f"  [{r['project']}] ops={r['operators']} hash={r['hash']}")
    return 0 if blocked_with_ops == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
