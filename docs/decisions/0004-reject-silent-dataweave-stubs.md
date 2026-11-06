# ADR 0004: Reject Silent DataWeave Stubs

## Status

Accepted

## Context

The deterministic DataWeave preservation layer already avoids silently accepting complex pass-through output by returning an explicit preservation-required result. The LLM DataWeave codegen path, however, accepted any syntactically valid module with the expected function name. That left room for pass-through code such as `return payload` or `return dict(payload)` to be accepted as a successful translation.

Relevant locations:

- `mule_parser/services/unified_dw_codegen.py:224` validates generated DataWeave modules before accepting them.
- `mule_parser/services/export_pipeline_v3/generators/transformation_generator.py:120` uses the preservation layer for deterministic transformation output.
- `mule_parser/parsers/dw_preservation.py:236` blocks silent deterministic pass-through for complex scripts.

## Decision

Add `_validate_no_silent_stub` to the unified DataWeave codegen acceptance checks. For non-empty DataWeave scripts, the validator rejects generated modules that:

- contain placeholder markers such as `TODO`, `FIXME`, `NotImplementedError`, or “default implementation” text,
- define no meaningful return statements, or
- return only input payload/event/body/record values, including `dict(payload)` or `{"records": payload}` style wrappers.

## Consequences

LLM DataWeave translations now need to perform a real transformation before replacing deterministic output. If the LLM cannot produce one, the pipeline keeps the deterministic/manual-review path rather than silently shipping a stub.

## Regression Test

`mule_parser/tests/test_unified_dw_codegen.py` now verifies that pass-through stubs are rejected and a simple field-mapping implementation is accepted.
