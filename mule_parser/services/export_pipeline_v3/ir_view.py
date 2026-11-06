"""
IRView — the read-only contract every v3 generator consumes.

The Enterprise Migration Directive mandates that the **generation layer
must become a pure consumer of the analysis layer**. There is exactly
one input stream into generation: the parser's IR (Intermediate
Representation). The IRView is the only object that exposes the IR to
downstream code.

Design rules
------------
* The IRView is **read-only**. Generators may not mutate the underlying
  IR. Every accessor returns a plain dict / list / value, never the
  internal storage.
* All access goes through typed iterators (``iter_flows``, ``iter_connectors``,
  ``iter_properties``, ``iter_files``, ``iter_entry_points``,
  ``iter_dataweave``). Generators MUST NOT reach into ``ir["raw_layer"]``
  directly.
* Required IR sections are validated at construction time. If the IR
  is missing a section that generation depends on, the view raises
  :class:`IRContractError` so the caller can write a structured
  failure report instead of producing a half-baked export.
* The view is the bridge between the IR-shape the parser produces today
  and the canonical contract the directive prescribes. Sections the
  parser doesn't natively emit yet (``file_inventory``,
  ``property_registry``, ``integration_manifest``) are derived from
  existing IR data so the migration to a fully native IR can happen
  parser-side without breaking the generators.

Usage:

    view = IRView.from_ir(ir_dict)
    for flow in view.iter_flows():
        ...
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Iterable, Iterator

logger = logging.getLogger(__name__)


# ─── Errors ───────────────────────────────────────────────────────────────────


class IRContractError(ValueError):
    """Raised when the IR is missing a section the generation layer requires.

    The exporter catches this and produces a structured failure report
    (``docs/export-failure.md``) instead of trying to fall back to raw
    file inspection.
    """


# ─── Light dataclasses for typed iteration ────────────────────────────────────


@dataclass(frozen=True)
class FlowView:
    """One flow exposed by the view."""

    name: str
    flow_type: str           # flow | sub-flow | batch
    file: str
    source: dict[str, Any]   # the trigger (http:listener / scheduler / jms / ...)
    processors: list[dict[str, Any]]
    error_handlers: list[dict[str, Any]]
    raw: dict[str, Any]      # backing dict for callers that need full access


@dataclass(frozen=True)
class ConnectorView:
    """One global connector configuration."""

    config_id: str
    connector_type: str       # http | db | salesforce | email | ...
    host: str
    port: str
    nested_configs: list[dict[str, Any]]
    properties: dict[str, Any]
    raw: dict[str, Any]


@dataclass(frozen=True)
class PropertyView:
    """One property in the project's property registry."""

    key: str                  # original key, e.g. "sfdc.password"
    value: str                # raw value (may be masked)
    is_secure: bool
    file: str
    env_var: str = ""         # normalised UPPER_SNAKE_CASE form for Lambda


@dataclass(frozen=True)
class FileView:
    """One file in the project, with content available for verbatim preservation."""

    path: str
    file_type: str            # mule-config | property | dwl | pom | log4j | json | other
    content: str              # decoded text content, may be empty if binary
    size_bytes: int = 0
    is_flow_file: bool = False


@dataclass(frozen=True)
class EntryPointView:
    """One execution entry point (HTTP listener, scheduler, queue consumer, ...)."""

    flow_name: str
    trigger_type: str         # http | scheduler | jms | kafka | ...
    path: str                 # HTTP path or queue name
    methods: list[str]
    trigger_config: dict[str, Any]


@dataclass(frozen=True)
class DataWeaveView:
    """One DataWeave script preserved verbatim plus its enriched metadata."""

    script_id: str
    body: str
    file: str
    parent_flow: str
    parent_step: str
    output_format: str
    field_mappings: dict[str, str]
    purpose: str
    semantics: dict[str, Any]  # structured semantics from the deep parser
    raw: dict[str, Any]


@dataclass(frozen=True)
class IntegrationView:
    """One outbound integration touched by at least one flow."""

    name: str                  # e.g. "Salesforce_Sfdc_config"
    kind: str                  # salesforce | database | smtp | sqs | http | ...
    subkind: str               # mysql | postgres | gmail | sendgrid | ...
    used_by_flows: list[str]
    env_vars: list[str]


# ─── The view itself ──────────────────────────────────────────────────────────


REQUIRED_IR_TOP_LEVEL_KEYS = ("raw_layer",)


@dataclass
class IRView:
    """Read-only structured view over the parser IR.

    Construct via :meth:`from_ir`. Direct ``__init__`` use is reserved
    for testing.
    """

    _ir: dict[str, Any] = field(default_factory=dict)

    # Cached projections (lazy).
    _flows_cache: tuple[FlowView, ...] | None = field(default=None, repr=False)
    _connectors_cache: tuple[ConnectorView, ...] | None = field(default=None, repr=False)
    _properties_cache: tuple[PropertyView, ...] | None = field(default=None, repr=False)
    _files_cache: tuple[FileView, ...] | None = field(default=None, repr=False)
    _entry_points_cache: tuple[EntryPointView, ...] | None = field(default=None, repr=False)
    _dataweave_cache: tuple[DataWeaveView, ...] | None = field(default=None, repr=False)
    _integrations_cache: tuple[IntegrationView, ...] | None = field(default=None, repr=False)

    # ------------------------------------------------------------------
    # Factory + validation
    # ------------------------------------------------------------------

    @classmethod
    def from_ir(cls, ir: Any) -> "IRView":
        """Coerce, validate, and return an IRView over the given IR.

        Accepts either:
            * a dict (the canonical IR shape), or
            * a pydantic IntermediateRepresentation (or anything with
              ``model_dump`` / ``dict``).

        Raises :class:`IRContractError` if the IR is missing sections
        the generation layer absolutely requires.
        """
        ir_dict = _coerce_ir(ir)
        cls._validate(ir_dict)
        return cls(_ir=ir_dict)

    @staticmethod
    def _validate(ir: dict[str, Any]) -> None:
        for key in REQUIRED_IR_TOP_LEVEL_KEYS:
            if key not in ir or ir.get(key) is None:
                raise IRContractError(f"Missing required top-level IR key: {key}")
        raw = ir.get("raw_layer")
        if not isinstance(raw, dict):
            raise IRContractError("IR.raw_layer must be a dict.")
        # raw_layer.original_json may be absent in degenerate IRs but the
        # rest of the codebase expects an empty dict in that case.
        if "original_json" in raw and not isinstance(raw["original_json"], dict):
            raise IRContractError(
                "IR.raw_layer.original_json must be a dict when present."
            )

    # ------------------------------------------------------------------
    # Top-level accessors
    # ------------------------------------------------------------------

    @property
    def raw(self) -> dict[str, Any]:
        """The unmodified backing IR. Use sparingly — generators should
        prefer the typed iterators below."""
        return self._ir

    @property
    def project_identity(self) -> dict[str, Any]:
        return dict(self._ir.get("project_identity") or {})

    @property
    def semantic_layer(self) -> dict[str, Any]:
        return dict(self._ir.get("semantic_layer") or {})

    @property
    def execution_layer(self) -> dict[str, Any]:
        return dict(self._ir.get("execution_layer") or {})

    @property
    def structural_layer(self) -> dict[str, Any]:
        return dict(self._ir.get("structural_layer") or {})

    @property
    def migration_plan(self) -> dict[str, Any]:
        """Enriched section: the migration plan attached to the IR."""
        return dict(self._ir.get("migration_plan") or {})

    @property
    def audit_report(self) -> dict[str, Any]:
        """Enriched section: the audit trail attached to the IR."""
        return dict(self._ir.get("audit_report") or {})

    @property
    def validation_report(self) -> dict[str, Any]:
        """Enriched section: the upstream validation report attached to the IR."""
        return dict(self._ir.get("validation_report") or {})

    @property
    def raw_layer(self) -> dict[str, Any]:
        raw = self._ir.get("raw_layer") or {}
        return dict(raw.get("original_json") or {})

    # ------------------------------------------------------------------
    # Typed iterators (the only API generators should use)
    # ------------------------------------------------------------------

    def iter_flows(self) -> Iterator[FlowView]:
        if self._flows_cache is None:
            self._flows_cache = tuple(self._build_flows())
        return iter(self._flows_cache)

    def iter_connectors(self) -> Iterator[ConnectorView]:
        if self._connectors_cache is None:
            self._connectors_cache = tuple(self._build_connectors())
        return iter(self._connectors_cache)

    def iter_properties(self) -> Iterator[PropertyView]:
        if self._properties_cache is None:
            self._properties_cache = tuple(self._build_properties())
        return iter(self._properties_cache)

    def iter_files(self) -> Iterator[FileView]:
        if self._files_cache is None:
            self._files_cache = tuple(self._build_files())
        return iter(self._files_cache)

    def iter_entry_points(self) -> Iterator[EntryPointView]:
        if self._entry_points_cache is None:
            self._entry_points_cache = tuple(self._build_entry_points())
        return iter(self._entry_points_cache)

    def iter_dataweave(self) -> Iterator[DataWeaveView]:
        if self._dataweave_cache is None:
            self._dataweave_cache = tuple(self._build_dataweave())
        return iter(self._dataweave_cache)

    def iter_integrations(self) -> Iterator[IntegrationView]:
        if self._integrations_cache is None:
            self._integrations_cache = tuple(self._build_integrations())
        return iter(self._integrations_cache)

    # ------------------------------------------------------------------
    # Convenience lookups
    # ------------------------------------------------------------------

    def get_file(self, path: str) -> FileView | None:
        """Return the FileView for ``path`` if present in the inventory."""
        normalised = path.replace("\\", "/").strip().lstrip("./")
        for entry in self.iter_files():
            if entry.path == path or entry.path == normalised:
                return entry
        return None

    def is_flow_file(self, path: str) -> bool:
        """Return True iff the IR considers ``path`` a Mule flow XML file."""
        entry = self.get_file(path)
        if entry is not None:
            return entry.is_flow_file
        # Fallback: derive by checking whether any flow references the path.
        for flow in self.iter_flows():
            if flow.file == path:
                return True
        return False

    def semantic_flow_index(self) -> dict[str, dict[str, Any]]:
        """Return {flow_name: semantic_flow_dict} for fast lookups."""
        index: dict[str, dict[str, Any]] = {}
        for sf in (self.semantic_layer.get("flows") or []):
            if isinstance(sf, dict):
                name = str(sf.get("name") or "").strip()
                if name:
                    index[name] = sf
        return index

    def plan_flow_index(self) -> dict[str, dict[str, Any]]:
        """Return {flow_name: plan_flow_dict} for fast lookups."""
        index: dict[str, dict[str, Any]] = {}
        for pf in (self.migration_plan.get("flows") or []):
            if not isinstance(pf, dict):
                continue
            name = str(pf.get("flow_name") or pf.get("name") or "").strip()
            if name:
                index[name] = pf
        return index

    # ------------------------------------------------------------------
    # Private builders
    # ------------------------------------------------------------------

    def _build_flows(self) -> Iterable[FlowView]:
        for raw_flow in self.raw_layer.get("flows") or []:
            if not isinstance(raw_flow, dict):
                continue
            yield FlowView(
                name=str(raw_flow.get("name") or "").strip(),
                flow_type=str(raw_flow.get("flow_type") or "flow"),
                file=str(raw_flow.get("file") or ""),
                source=dict(raw_flow.get("source") or {}) if isinstance(raw_flow.get("source"), dict) else {},
                processors=list(raw_flow.get("processors") or []),
                error_handlers=list(raw_flow.get("error_handlers") or []),
                raw=dict(raw_flow),
            )

    def _build_connectors(self) -> Iterable[ConnectorView]:
        for raw_conn in self.raw_layer.get("connectors") or []:
            if not isinstance(raw_conn, dict):
                continue
            yield ConnectorView(
                config_id=str(raw_conn.get("config_id") or raw_conn.get("name") or "").strip(),
                connector_type=str(raw_conn.get("connector_type") or "").strip(),
                host=str(raw_conn.get("host") or ""),
                port=str(raw_conn.get("port") or ""),
                nested_configs=list(raw_conn.get("nested_configs") or []),
                properties=dict(raw_conn.get("properties") or {}),
                raw=dict(raw_conn),
            )

    def _build_properties(self) -> Iterable[PropertyView]:
        # Prefer an explicit ``property_registry`` section if the parser
        # populated one. Fall back to the raw ``properties`` list.
        registry = self._ir.get("property_registry")
        seen: set[str] = set()
        if isinstance(registry, list):
            for entry in registry:
                if not isinstance(entry, dict):
                    continue
                key = str(entry.get("key") or "").strip()
                if not key or key in seen:
                    continue
                seen.add(key)
                yield PropertyView(
                    key=key,
                    value=str(entry.get("value") or ""),
                    is_secure=bool(entry.get("is_secure") or entry.get("is_secret") or False),
                    file=str(entry.get("file") or entry.get("source_file") or ""),
                    env_var=str(entry.get("env_var") or ""),
                )
        for raw_prop in self.raw_layer.get("properties") or []:
            if not isinstance(raw_prop, dict):
                continue
            key = str(raw_prop.get("key") or "").strip()
            if not key or key in seen:
                continue
            seen.add(key)
            yield PropertyView(
                key=key,
                value=str(raw_prop.get("value") or ""),
                is_secure=bool(raw_prop.get("is_secure") or False),
                file=str(raw_prop.get("file") or ""),
            )

    def _build_files(self) -> Iterable[FileView]:
        # Three sources, in priority order:
        #   1. ``ir.file_inventory[]``    — canonical (when parser populates it)
        #   2. ``structural_layer.files`` — existing IR shape (no content)
        #   3. Synthesised from raw_layer.flows[] / properties[] / etc.
        seen_paths: set[str] = set()
        flow_paths = {flow.file for flow in self.iter_flows() if flow.file}

        inventory = self._ir.get("file_inventory")
        if isinstance(inventory, list):
            for entry in inventory:
                if not isinstance(entry, dict):
                    continue
                path = str(entry.get("path") or entry.get("name") or "").strip()
                if not path or path in seen_paths:
                    continue
                seen_paths.add(path)
                content = entry.get("content") or ""
                if isinstance(content, bytes):
                    try:
                        content = content.decode("utf-8")
                    except UnicodeDecodeError:
                        content = ""
                yield FileView(
                    path=path,
                    file_type=str(entry.get("file_type") or _classify_file(path)),
                    content=str(content),
                    size_bytes=int(entry.get("size_bytes") or 0),
                    is_flow_file=bool(entry.get("is_flow_file"))
                        or (path in flow_paths)
                        or _looks_like_flow_path(path),
                )

        structural_files = self.structural_layer.get("files") or []
        for entry in structural_files:
            if not isinstance(entry, dict):
                continue
            path = str(entry.get("path") or "").strip()
            if not path or path in seen_paths:
                continue
            seen_paths.add(path)
            yield FileView(
                path=path,
                file_type=str(entry.get("file_type") or _classify_file(path)),
                content=str(entry.get("content") or ""),
                size_bytes=int(entry.get("size_bytes") or 0),
                is_flow_file=path in flow_paths or _looks_like_flow_path(path),
            )

        # Synthesise from raw_layer.flows[] / dataweave[] / properties[]
        # so we don't lose track of files the parser referenced but didn't
        # list explicitly.
        for flow in self.iter_flows():
            if flow.file and flow.file not in seen_paths:
                seen_paths.add(flow.file)
                yield FileView(
                    path=flow.file,
                    file_type="mule-config",
                    content="",
                    is_flow_file=True,
                )
        for dw in self.iter_dataweave():
            if dw.file and dw.file not in seen_paths:
                seen_paths.add(dw.file)
                yield FileView(
                    path=dw.file,
                    file_type="dwl" if dw.file.lower().endswith(".dwl") else "mule-config",
                    content=dw.body,
                )

    def _build_entry_points(self) -> Iterable[EntryPointView]:
        for ep in self.execution_layer.get("entry_points") or []:
            if not isinstance(ep, dict):
                continue
            yield EntryPointView(
                flow_name=str(ep.get("flow_name") or "").strip(),
                trigger_type=str(ep.get("trigger_type") or ep.get("type") or "http").strip().lower(),
                path=str(ep.get("path") or "").strip(),
                methods=[m.upper() for m in (ep.get("methods") or []) if isinstance(m, str)],
                trigger_config=dict(ep.get("trigger_config") or {}),
            )

    def _build_dataweave(self) -> Iterable[DataWeaveView]:
        for dw in self.raw_layer.get("dataweave") or []:
            if not isinstance(dw, dict):
                continue
            yield DataWeaveView(
                script_id=str(dw.get("script_id") or "").strip(),
                body=str(dw.get("script_text") or dw.get("body") or dw.get("content") or ""),
                file=str(dw.get("file") or dw.get("path") or ""),
                parent_flow=str(dw.get("parent_flow") or "").strip(),
                parent_step=str(dw.get("parent_step_id") or "").strip(),
                output_format=str(dw.get("output_type") or ""),
                field_mappings=dict(dw.get("field_mappings") or {}),
                purpose=str(dw.get("purpose") or ""),
                semantics=dict(dw.get("semantics") or {}),
                raw=dict(dw),
            )

    def _build_integrations(self) -> Iterable[IntegrationView]:
        # Prefer an explicit ``integration_manifest`` section. Otherwise
        # derive a coarse one from the connector list.
        manifest = self._ir.get("integration_manifest")
        if isinstance(manifest, list):
            for entry in manifest:
                if not isinstance(entry, dict):
                    continue
                yield IntegrationView(
                    name=str(entry.get("name") or "").strip(),
                    kind=str(entry.get("kind") or "").strip(),
                    subkind=str(entry.get("subkind") or "").strip(),
                    used_by_flows=list(entry.get("used_by_flows") or []),
                    env_vars=list(entry.get("env_vars") or []),
                )
            return
        # Derived view from the connectors list.
        for c in self.iter_connectors():
            kind = c.connector_type
            subkind = ""
            for nested in c.nested_configs:
                if isinstance(nested, dict) and "type" in nested:
                    subkind = str(nested["type"]).split(":")[-1]
                    break
            yield IntegrationView(
                name=c.config_id or c.connector_type or "(unnamed)",
                kind=kind,
                subkind=subkind,
                used_by_flows=[],
                env_vars=[],
            )


# ─── Helpers ──────────────────────────────────────────────────────────────────


_FLOW_PATH_HINTS = ("src/main/mule/", "src/main/resources/mule/", "src/main/app/")


def _looks_like_flow_path(path: str) -> bool:
    lower = (path or "").lower()
    return lower.endswith(".xml") and any(hint in lower for hint in _FLOW_PATH_HINTS)


def _classify_file(path: str) -> str:
    """Best-effort file_type classification when the parser didn't set one."""
    lower = (path or "").lower()
    if lower.endswith(".xml"):
        if any(hint in lower for hint in _FLOW_PATH_HINTS):
            return "mule-config"
        return "xml"
    if lower.endswith(".dwl"):
        return "dwl"
    if lower.endswith(".properties"):
        return "property"
    if lower.endswith(".json"):
        return "json"
    if "pom.xml" in lower:
        return "pom"
    if lower.endswith((".yaml", ".yml")):
        return "yaml"
    return "other"


def _coerce_ir(ir: Any) -> dict[str, Any]:
    """Return a plain dict from any IR-shaped input."""
    if ir is None:
        return {}
    if isinstance(ir, dict):
        return ir
    # Pydantic model? Try model_dump (v2) then dict (v1).
    dump = getattr(ir, "model_dump", None)
    if callable(dump):
        try:
            return dump()
        except Exception:  # noqa: BLE001
            pass
    legacy_dict = getattr(ir, "dict", None)
    if callable(legacy_dict):
        try:
            return legacy_dict()
        except Exception:  # noqa: BLE001
            pass
    if hasattr(ir, "__dict__"):
        return dict(ir.__dict__)
    return {}


__all__ = [
    "ConnectorView",
    "DataWeaveView",
    "EntryPointView",
    "FileView",
    "FlowView",
    "IRContractError",
    "IRView",
    "IntegrationView",
    "PropertyView",
]
