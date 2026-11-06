# ADR 0001: Ground Fast Export Validation in Assembled Files

## Status

Accepted

## Context

The fast migrated-file export path packages already completed generated files through `project_assembler.assemble_project`. Its markdown migration summary already counts the assembled file list, but `migration-report/export-validation.json` used `_coverage_matrix`, which derived totals from migration-plan decisions, orchestration artifacts, and migrated database rows. When those intermediate structures were stale or empty, the report could show `0/0` style coverage even though the export contained real Python and Terraform files.

Relevant locations:

- `mule_parser/services/export_service.py:224` routes completed migrated files to the fast assembled export path.
- `mule_parser/services/export_service.py:449` calls `assemble_project`.
- `mule_parser/services/project_assembler.py:161` emits the fast-path validation summary.
- `mule_parser/services/project_assembler.py:685` contains the old intermediate-state coverage matrix.
- `mule_parser/services/project_assembler.py:731` already derives disk-equivalent counts from assembled files.

## Decision

Add `_real_output_coverage` in `mule_parser/services/project_assembler.py` and use it when emitting `migration-report/export-validation.json`. The helper still preserves plan-derived per-flow detail when available, but its totals are grounded in the actual assembled files:

- real handler file count
- real Python file count
- real Terraform/IaC file count
- real component coverage derived from generated handler and transformation modules

## Consequences

The fast export validation JSON can no longer report zero covered/generated components when the assembled output contains deployable source files. This does not satisfy the full Phase 8 requirement because three structurally different real MuleSoft sample projects were not available and were not run end-to-end in this change.

## Regression Test

`mule_parser/tests/test_project_assembler_counts.py` now verifies that validation coverage is derived from assembled files even when plan/artifact inputs are empty.
