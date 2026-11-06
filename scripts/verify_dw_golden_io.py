"""Run all DataWeave golden I/O fixtures against preserve_dataweave."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from mule_parser.parsers.dw_golden_io import run_all_golden_fixtures, DEFAULT_FIXTURES_ROOT

results = run_all_golden_fixtures(DEFAULT_FIXTURES_ROOT, repo_root=ROOT / "mule_parser")
passed = sum(1 for r in results if r.passed)
print(f"GOLDEN I/O: {passed}/{len(results)} passed")
for r in results:
    status = "PASS" if r.passed else "FAIL"
    print(f"  [{status}] {r.fixture_id} strategy={r.strategy}")
    if r.diffs:
        print(f"         diffs: {r.diffs}")
    if r.error:
        print(f"         error: {r.error}")

if passed != len(results):
    raise SystemExit(1)
