# 0008: Fix DataWeave Fidelity Pipeline Regressions

## Context
During synthetic parity testing of generated DataWeave transformations, several errors were discovered:
1. `function not defined in generated code` - Caused by terminology scrubbers mutating the generated source code (replacing "dataweave" with "data_transformer") after the `TransformationMetadata` was already populated. The generated module's function name no longer matched the expected metadata function name.
2. `TypeError` or `AttributeError: 'str' object has no attribute 'get'` - Caused by LLM transformations generating custom function signatures like `def transform_xyz(records: List[Dict])` instead of the required default payload contract `def transform_xyz(payload: dict[str, Any])`.
3. `NoneType object is not callable` - Caused by the deterministic `ast_compile` strategy translating `p('api.name')` to `_ctx.get_path('p')('api.name')`, but the runtime `DWContext` did not implement resolving `p` to application properties.

## Decision
1. **Terminology Scrubbing Scope**: Limit terminology scrubbing in `metadata_builder.py` to the generated `module` and `func_name`, leaving the original `slug` (which controls `TransformationMetadata.id` and `TransformationMetadata.name`) unchanged. This ensures downstream linkage via IDs works correctly while keeping the generated module names consistent with the code.
2. **Explicit LLM Signatures**: Modify the `_USER_TEMPLATE` in `unified_dw_codegen.py` to dictate the exact python function signature required: `def {function_name}(payload: dict[str, Any]) -> dict[str, Any]:`.
3. **AST Runtime Context**: Add a `read_property` helper to `DWContext` (in `dw_runtime.py`) that handles DataWeave `p(...)` calls identically to the LLM generation rules, mapping them to `os.environ.get(...)`.

## Consequences
- DataWeave metadata IDs preserve trace lineage accurately back to Mule flow IDs.
- The VFS generated Python code matches the validation gate assertions identically.
- Deterministic and LLM generated translations conform to expected runtime behaviors and pass parity tests.
