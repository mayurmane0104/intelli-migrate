# 0007. Fix Pipeline Test Regressions and Gate Logic

## Context

Recent changes to the `migration-studio` export pipeline (v3) surfaced four distinct failures across the regression test suite. These failures were blocking `ExportOrchestrator` runs, failing post-generation gates, and breaking the fast export canonical packaging test.

The four specific defects were:
1. **`test_dataweave_property_refs_are_config_contract` (DataWeave Validation)**: The test contained a mismatched string assertion. It looked for `"never payload"` instead of the actual `UnifiedDataWeaveCodeGenerator` rejection text (`"never implement these"`).
2. **`test_fast_export_zip_uses_canonical_layout` (Assembler / Layout)**: The test's `migratedCode` mock was being rejected silently by `_is_code_migration_source` because it passed a barren `<mule/>` XML root without any `<flow>` elements, resulting in a zero-handler zip output. The test was also asserting the presence of `_controller.py`, which is correct for `api` classification, but wasn't emitting due to the drop.
3. **`test_fresh_batch_simple_export_passes_gate_runner` (NameError)**: The canonical `function_generator.py` handler template logic referenced `CONNECTOR_KIND_TO_PORT` without importing it, causing a crash during `_render_default_handler`.
4. **`test_fresh_sfdc_export_passes_gate_runner` (API Route Gate)**: The post-generation gate `api_route_mapping` failed to detect the generated route `GET /generatereport -> trigger-flow` in the `_ROUTES` dictionary of the API handler. The AST parsing logic only extracted routes from standard assignments (`ast.Assign`) but failed to support annotated assignments (`ast.AnnAssign`), which the generator actually outputs (`_ROUTES: dict[...] = {...}`).

## Decision

We root-caused and fixed each issue directly at the pipeline layer, ensuring test validity without compromising real execution paths.

1. **Test Assertion Correction**: Updated the DW config contract test to match the true system string.
2. **Fast Export Fixture**: Updated the XML mock payload in `test_fast_export_zip_uses_canonical_layout` to `<mule><flow name='test'/></mule>` to satisfy the code-migration rules (`_is_code_migration_source`), restoring valid layout generation.
3. **Constant Import**: Explicitly imported `CONNECTOR_KIND_TO_PORT` from `..port_registry` inside `_render_default_handler`.
4. **AST Parsing Enrichment**: Enriched `_extract_api_routes()` in `post_generation_gates.py` to recursively match and process `ast.AnnAssign` nodes targeting `_ROUTES`, restoring the gate's ability to validate typed dictionaries.

## Consequences

- All pipeline regression tests are now green (`24 passed`).
- Code validity gates accurately parse standard typed outputs for Python 3.12 without falsely blocking valid generated handlers.
- The pipeline remains strictly deterministic and safe against missing lazy imports.
