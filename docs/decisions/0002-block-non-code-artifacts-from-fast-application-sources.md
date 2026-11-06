# ADR 0002: Block Non-Code Artifacts from Fast Application Sources

## Status

Accepted

## Context

The fast migrated-file assembler accepted completed project-file rows and structured LLM file trees as application source without first checking whether the original file was a source artifact that should produce code. That allowed support files such as Postman collections or environment JSON files to become Python files when a per-file migration row contained code-like output.

Relevant locations:

- `mule_parser/services/project_assembler.py:329` emits application source files for the fast export path.
- `mule_parser/services/project_assembler.py:362` consumes structured `===FILE:` output.
- `mule_parser/services/project_assembler.py:404` consumes legacy primary-code-block output.
- `mule_parser/services/project_assembler.py:448` separately preserves all original source files under `source-artifacts/`.

## Decision

Add `_is_code_migration_source` and call it before either structured file-tree output or legacy extracted code can be emitted as application source. Only real flow XML and DataWeave files can produce generated code in this fast assembler path. Known support files such as `pom.xml`, `mule-artifact.json`, `application-types.xml`, Postman collections/environments, and docs are skipped for application source generation but still remain available through reports and source-artifact preservation.

## Consequences

The assembler no longer turns non-code artifacts into `src/` or `application/src/` files. If a completed row for a non-code source has migrated output, the assembler records a warning instead of silently shipping it as runnable code.

## Regression Test

`mule_parser/tests/test_fast_export_assembly.py` now covers both legacy migrated-code extraction and structured file-tree output from non-code source rows.
