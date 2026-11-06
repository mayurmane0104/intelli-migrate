# ADR 0000: Pipeline Architecture Map

## Status

Accepted

## Context

The migration generator must be remediated at the pipeline level, not by patching one generated output. This map records the current code path from parsed MuleSoft input to generated Python/Terraform output and identifies where validation reports are derived.

## Active Export Entry Points

- `mule_parser/services/export_service.py:107` exposes `build_export`.
- `mule_parser/services/export_service.py:122` defaults the export pipeline to `v3`.
- `mule_parser/services/export_service.py:203` starts `build_export_v3`.
- `mule_parser/services/export_service.py:224` routes projects with completed migrated file rows to the fast assembled export path.
- `mule_parser/services/export_service.py:260` routes projects without completed migrated files to the deterministic v3 `ExportOrchestrator`.
- `mule_parser/services/export_service.py:432` packages completed migrated files through `project_assembler.assemble_project`.

## Ordered Generation Stages

1. Ingestion and parsing
   - `mule_parser/core/orchestrator.py:36` loads ZIP/JAR/folder/Git sources and builds the raw parser model.
   - `mule_parser/core/orchestrator.py:74` discovers Mule XML, DataWeave, and property files.
   - `mule_parser/core/orchestrator.py:91` parses XML files into flows, connectors, execution plans, relationships, DataWeave scripts, and MUnit tests.
   - `mule_parser/core/semantic_orchestrator.py:41` runs semantic enrichment over the raw parse result.
   - `mule_parser/ir/builder.py:137` builds the multi-layer IR used by export.

2. Export request selection
   - `mule_parser/services/export_service.py:217` collects export inputs and chooses infrastructure mode.
   - `mule_parser/services/export_service.py:224` checks whether per-file migrated content already exists.
   - If completed migrated files exist, the project goes to `project_assembler`; otherwise it goes to `ExportOrchestrator`.

3. IR enrichment and preflight
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:245` folds legacy adapter inputs into the IR.
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:254` runs pipeline preflight before generation.
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:267` creates an `IRView`.

4. Metadata and architecture planning
   - `mule_parser/services/export_pipeline_v3/generators/metadata_builder.py:1` declares metadata as the source consumed by downstream generators.
   - `mule_parser/services/export_pipeline_v3/generators/metadata_builder.py:8` documents that only real flow elements become functions.
   - `mule_parser/services/export_pipeline_v3/generators/metadata_builder.py:524` includes standalone `.dwl` files from the IR file inventory as transformations.
   - `mule_parser/services/export_pipeline_v3/generators/metadata_builder.py:600` builds functions strictly from parsed flow elements.
   - `mule_parser/services/export_pipeline_v3/generators/metadata_builder.py:877` derives infrastructure resources from parsed functions and connectors.
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:287` runs metadata building.
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:317` applies migration type detection.
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:322` runs architectural planning.

5. Optional controlled LLM enhancement
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:332` runs the architect agent when fast export is disabled.
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:339` runs DataWeave and architecture enhancers when fast export is disabled.
   - `mule_parser/services/export_pipeline_v3/grounded_llm.py` gates LLM responses by grounding, JSON schema, and confidence.

6. Code generation
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:350` starts code generation.
   - `mule_parser/services/export_pipeline_v3/generators/llm_function_generator.py` generates Lambda/function code on the normal v3 path.
   - `mule_parser/services/export_pipeline_v3/generators/function_generator.py` is used on fast mode for deterministic function generation.
   - `mule_parser/services/export_pipeline_v3/generators/integration_generator.py` generates adapters/integrations.
   - `mule_parser/services/export_pipeline_v3/generators/llm_transformation_generator.py:56` writes deterministic transformation output first, then upgrades low-confidence/complex transforms with unified DataWeave codegen when enabled.
   - `mule_parser/services/export_pipeline_v3/generators/transformation_generator.py:36` emits one Python module per `TransformationMetadata` and preserves source DataWeave provenance.
   - `mule_parser/services/export_pipeline_v3/generators/config_generator.py` writes config artifacts.
   - `mule_parser/services/export_pipeline_v3/generators/infrastructure_generator.py` writes SAM/Terraform infrastructure.
   - `mule_parser/services/export_pipeline_v3/generators/test_generator.py` writes test scaffolding.
   - `mule_parser/services/export_pipeline_v3/generators/documentation_generator.py` writes README, requirements, CI, and docs.

7. Review, validation, and self-correction
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:388` runs agent review stages when not in fast/codegen-only mode.
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:427` runs the validation pipeline and optional self-correction.
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:480` runs the validation report generator.
   - `mule_parser/services/export_pipeline_v3/orchestrator.py:486` runs hard post-generation gates before packaging.

8. Packaging
   - `mule_parser/services/export_pipeline_v3/generators/packaging_generator.py` packages the v3 VFS.
   - `mule_parser/services/project_assembler.py:103` assembles the fast migrated-file export path.
   - `mule_parser/services/project_assembler.py:134` emits application sources from orchestration artifacts and project file rows.
   - `mule_parser/services/project_assembler.py:140` emits infrastructure from artifacts.
   - `mule_parser/services/project_assembler.py:149` emits migration reports after artifact files so the markdown summary can count assembled files.
   - `mule_parser/services/project_assembler.py:161` emits `migration-report/export-validation.json`.

## Prompt and Template Locations

- Global prompt loader and static prompt text live in `mule_parser/services/prompt_loader.py`.
- Markdown prompt library files live under `mule_parser/kb/04_prompt_library/system_prompts/`.
- AWS template skeletons live under `mule_parser/templates/*/template.yaml`, `template.cdk.ts`, and `validation_rules.json`.
- Unified DataWeave and flow codegen prompt text is embedded in:
  - `mule_parser/services/unified_dw_codegen.py`
  - `mule_parser/services/unified_flow_codegen.py`
- v3 agent prompts are embedded in `mule_parser/services/export_pipeline_v3/agents/*.py`.

## Single vs Multiple LLM Passes

The normal v3 path is a metadata-driven, multi-pass pipeline. LLM calls are not a single monolithic generation call. They happen in controlled enhancers, function/transformation generators, and review agents. The orchestrator reconciles these through shared `MigrationMetadata`, VFS validation, and post-generation gates. The fast assembled path is different: it packages already completed per-file migrated content and generated artifacts through `project_assembler`, so it can inherit inconsistencies already present in those migrated rows unless the assembler validates the actual file list.

## Validation Report Sources

There are two report systems:

- Normal v3:
  - `mule_parser/services/export_pipeline_v3/generators/validation_generator.py:176` runs validation.
  - `mule_parser/services/export_pipeline_v3/generators/validation_generator.py:179` writes `docs/export-validation.json`.
  - `mule_parser/services/export_pipeline_v3/generators/validation_generator.py:669` syncs report counts from actual VFS paths.
  - `mule_parser/services/export_pipeline_v3/post_generation_gates.py:181` counts artifacts from actual VFS paths.

- Fast assembled export:
  - `mule_parser/services/project_assembler.py:161` builds coverage for `migration-report/export-validation.json`.
  - `mule_parser/services/project_assembler.py:685` currently derives coverage totals from migration plan decisions, orchestration artifacts, and migrated rows.
  - `mule_parser/services/project_assembler.py:731` can derive disk-equivalent counts from the assembled file list.
  - `mule_parser/services/project_assembler.py:753` already uses assembled-file counts for the markdown migration summary.

The fast assembled path is the likely root of stale `0/0` validation totals when real files exist, because its JSON validation summary can be sourced from intermediate plan/artifact counters instead of the assembled file list.

## Existing End-to-End Coverage

- Python tests cover parser, IR, DataWeave, export, gates, and workflow under `mule_parser/tests`.
- Export-focused tests include `mule_parser/tests/test_export_pipeline_v3.py`, `mule_parser/tests/test_fresh_export_gates.py`, `mule_parser/tests/test_infra_evidence_allowlist.py`, and `mule_parser/tests/test_project_assembler_counts.py`.
- The Studio UI has Vitest and Playwright tests under `frontend/src/test`.
- I did not find a test suite that runs the full migration pipeline against three structurally different real MuleSoft sample projects in this workspace. That means the final Phase 8 exit criteria cannot honestly be claimed without additional sample projects and a longer end-to-end run.

## Decision

Use this map as the remediation anchor. Fixes must target one of the stages above and must add regression coverage at the pipeline/report boundary, not only isolated helpers.
