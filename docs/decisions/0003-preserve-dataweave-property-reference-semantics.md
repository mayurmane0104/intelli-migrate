# ADR 0003: Preserve DataWeave Property Reference Semantics

## Status

Accepted

## Context

DataWeave `p('some.property')` reads application configuration. It is not equivalent to `payload.some.property`, `vars.some.property`, or any other request-scoped value. If the DataWeave-to-Python generator maps `p(...)` calls to payload fields, generated business logic can silently use attacker/request-controlled values where deployment configuration was intended.

Relevant locations:

- `mule_parser/services/unified_dw_codegen.py:58` defines the DataWeave LLM system rules.
- `mule_parser/services/unified_dw_codegen.py:80` defines the user prompt sent with the full DataWeave source.
- `mule_parser/services/unified_dw_codegen.py:224` validates generated DataWeave modules before accepting them.

## Decision

Add an explicit `p(...)` rule to the DataWeave codegen prompt and include an application-property contract in each prompt. Add a mechanical post-generation validator that:

- extracts all `p('key')` references from the source DataWeave,
- maps each key to an environment variable name,
- requires the generated code to reference the property key or environment variable, and
- rejects generated code that reads that property from `payload`, `event`, `body`, or `record`.

## Consequences

LLM output that treats deployment config as request payload is rejected before it can replace deterministic transformation output. This makes the gap visible through the existing fallback/manual-review path instead of silently accepting incorrect business logic.

## Regression Test

`mule_parser/tests/test_unified_dw_codegen.py` now verifies property-reference extraction, prompt contract rendering, and rejection of payload-sourced config translations.
