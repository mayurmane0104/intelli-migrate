# ADR 0005: Enforce HTTP Flow to API Route Mapping

## Context

Canonical API exports generate one Lambda handler at `src/handlers/api_handler.py`.
That handler is responsible for mapping every source HTTP listener captured in
`FunctionMetadata` to the correct generated domain service. A simple handler
count gate can still pass if the single API handler exists but one source
endpoint is absent from `_ROUTES` or points to the wrong service.

## Decision

Add a post-generation gate that, for canonical API exports, derives expected
routes from each non-error HTTP `FunctionMetadata` entry:

- `http_path` becomes the route path, defaulting to `/<function-name>`.
- `http_methods` become the route methods, defaulting to `ANY`.
- `module_name` determines the required service target:
  `<module_name>_service.process`.

The gate parses the generated canonical API handler, extracts the `_ROUTES`
dictionary, and fails the export if any expected `(method, path)` tuple is
missing or wired to a different service.

## Consequences

- Endpoint completeness is now checked against generated code, not a planned
  file count.
- Single-handler API exports can no longer pass while silently dropping a
  listener route.
- The gate remains layout-specific and skips non-API exports.
