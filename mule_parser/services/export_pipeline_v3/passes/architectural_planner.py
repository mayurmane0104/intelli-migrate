"""
Pass 1 - ArchitecturalPlanner.

Walks every ``FunctionMetadata`` and decides the implementation pattern
that a senior architect would pick. Writes an :class:`ArchitecturalDecision`
onto each function so downstream generators consume one source of truth.

The planner is deterministic. It can optionally consult an LLM
(``LLMProvider.critique``) for *rationale* — the chosen pattern itself is
always picked by the deterministic rules below so the output is
reproducible.

Decision rules (in priority order)
----------------------------------
1. ``is_error_handler``                   -> ``error-handler``
2. ``delegates_to`` (sibling Lambda)      -> ``delegation``
3. salesforce + database connectors AND
   a transformation with structured
   join/dedup semantics                   -> ``scatter-gather``
4. salesforce + database connectors AND
   a ``scatter-gather`` step               -> ``scatter-gather``
5. database connector only                -> ``simple-crud``
6. sqs / sns / stream trigger             -> ``event-driven``
7. otherwise                              -> ``passthrough``
"""
from __future__ import annotations

import logging
from typing import Iterable

from ..llm_provider import LLMProvider, NullLLMProvider
from ..metadata import (
    ArchitecturalDecision,
    ConnectorKind,
    FunctionMetadata,
    MigrationMetadata,
    TransformationMetadata,
    TriggerType,
)

logger = logging.getLogger(__name__)


class ArchitecturalPlanner:
    """Stage that decides the pattern for every function in the migration."""

    name = "architectural-planner"

    def __init__(self, llm: LLMProvider | None = None) -> None:
        self._llm = llm or NullLLMProvider()

    def plan(self, metadata: MigrationMetadata) -> None:
        """Mutate ``metadata.functions`` in place, attaching an architecture decision."""
        connector_index = {c.id: c for c in metadata.connectors}
        transform_index = {t.id: t for t in metadata.transformations}

        # The migration-type detector has already run; surface the
        # canonical structure (if any) so the planner can attach the
        # canonical Lambda role to each function and reason about the
        # required Step Functions / SQS pieces.
        spec = self._load_output_spec(metadata)
        canonical_roles = self._canonical_roles(spec)

        for fn in metadata.functions:
            connectors = [connector_index[cid] for cid in fn.connectors if cid in connector_index]
            transforms = [transform_index[tid] for tid in fn.transformations if tid in transform_index]
            decision = self._decide(fn, connectors, transforms)

            # Carry the pattern back onto the function so all downstream
            # generators see one source of truth.
            fn.pattern = decision.pattern
            fn.architecture = decision
            # Auto-populate the function's logical services / repositories
            # so the generator can shape an SOLID-style layered module.
            self._populate_layers(fn, decision, connectors)
            # Attach the canonical Lambda role (batch_trigger / record_processor /
            # batch_completion) when the spec declares discrete roles. Single-
            # Lambda projects (batch_simple / api) leave the field empty.
            self._attach_canonical_role(fn, decision, canonical_roles)

        # When the spec wants Step Functions or SQS, mark the infra contract
        # so the infrastructure generator emits the orchestration files
        # regardless of how many flows the project has.
        if spec is not None:
            try:
                if spec.requires_step_functions:
                    metadata.infrastructure.requires_step_functions = True
                if spec.requires_sqs:
                    metadata.infrastructure.requires_sqs = True
            except AttributeError:
                # Infrastructure model predates these fields — safe to skip.
                pass

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _decide(
        self,
        fn: FunctionMetadata,
        connectors: list,
        transforms: list[TransformationMetadata],
    ) -> ArchitecturalDecision:
        if fn.is_error_handler:
            return self._decision(
                pattern="error-handler",
                confidence=0.95,
                rationale="Function flagged as a global error handler — log + re-raise pattern.",
                alternatives=["dead-letter-handler"],
            )

        if fn.delegates_to:
            return self._decision(
                pattern="delegation",
                confidence=0.9,
                rationale=f"Function only flow-refs to {fn.delegates_to!r}; emit a thin HTTP delegator.",
                alternatives=["simple-crud"],
            )

        kinds = {c.kind for c in connectors}

        has_sfdc = ConnectorKind.salesforce in kinds
        has_db = ConnectorKind.database in kinds
        scatter_step = any(s.kind == "scatter_gather" for s in fn.steps)
        structured_merge = any(
            t.join or t.dedup or t.sort or t.aggregation
            for t in transforms
        )
        if (has_sfdc and has_db) or scatter_step or structured_merge:
            rationale_bits = []
            if has_sfdc and has_db:
                rationale_bits.append("salesforce + database connectors detected")
            if scatter_step:
                rationale_bits.append("source flow has a scatter-gather step")
            if structured_merge:
                rationale_bits.append("DataWeave declared join/dedup/sort semantics")
            return self._decision(
                pattern="scatter-gather",
                confidence=0.85 if structured_merge else 0.7,
                rationale="; ".join(rationale_bits) + ".",
                alternatives=["simple-crud", "event-driven"],
            )

        if fn.trigger_type in (TriggerType.sqs, TriggerType.sns, TriggerType.stream):
            return self._decision(
                pattern="event-driven",
                confidence=0.8,
                rationale=f"Trigger is {fn.trigger_type.value}; emit a streaming handler with batch awareness.",
                alternatives=["simple-crud"],
            )

        if has_db and not (has_sfdc or scatter_step):
            return self._decision(
                pattern="simple-crud",
                confidence=0.7,
                rationale="Only a database connector is present; emit a CRUD-style request handler.",
                alternatives=["passthrough"],
            )

        return self._decision(
            pattern="passthrough",
            confidence=0.6,
            rationale="No external integrations detected; emit a passthrough handler.",
            alternatives=["simple-crud"],
        )

    @staticmethod
    def _decision(
        *,
        pattern: str,
        confidence: float,
        rationale: str,
        alternatives: Iterable[str] = (),
    ) -> ArchitecturalDecision:
        return ArchitecturalDecision(
            pattern=pattern,
            confidence=confidence,
            rationale=rationale,
            alternatives=list(alternatives),
        )

    @staticmethod
    def _populate_layers(
        fn: FunctionMetadata,
        decision: ArchitecturalDecision,
        connectors: list,
    ) -> None:
        """Decide the service / repository names for SOLID-style layering."""
        services: list[str] = []
        repositories: list[str] = []
        for c in connectors:
            kind = c.kind
            if kind == ConnectorKind.database:
                repositories.append(f"{c.module_name}_repository")
            elif kind == ConnectorKind.salesforce:
                services.append("salesforce_service")
            elif kind == ConnectorKind.http:
                services.append(f"{c.module_name}_service")
            elif kind == ConnectorKind.smtp or kind == ConnectorKind.ses:
                services.append("notification_service")
            elif kind == ConnectorKind.s3:
                repositories.append("object_store_repository")
        decision.services = sorted(set(services))
        decision.repositories = sorted(set(repositories))

        # Risk surface notes for the migration report.
        if decision.pattern == "scatter-gather":
            if not decision.services:
                decision.risk_notes.append(
                    "scatter-gather pattern picked but no service layer detected — "
                    "verify upstream connector extraction."
                )
        if decision.pattern == "delegation" and not fn.delegates_to:
            decision.risk_notes.append("delegation pattern picked without a delegates_to id.")

    # ------------------------------------------------------------------
    # Canonical structure integration
    # ------------------------------------------------------------------

    @staticmethod
    def _load_output_spec(metadata: MigrationMetadata):
        """Return the ``OutputStructureSpec`` for this migration (or None)."""
        spec = getattr(metadata, "output_structure", None)
        if spec is not None:
            return spec
        mt = getattr(metadata, "migration_type", "") or ""
        if not mt:
            return None
        try:
            from ..output_structure import get_structure  # local import to avoid cycle

            return get_structure(mt)
        except Exception:  # noqa: BLE001
            return None

    @staticmethod
    def _canonical_roles(spec) -> list[str]:
        """Derive the canonical Lambda role names (if any) from the spec.

        For multi-Lambda layouts (``src/functions/<role>/handler.py``) the role
        is the directory under ``functions``. For single-Lambda layouts
        (``src/app/lambda_handler.py``) the role is the directory under
        ``src`` — so ``app`` becomes the canonical role for batch_simple/api.
        """
        if spec is None:
            return []
        roles: list[str] = []
        for path in getattr(spec, "lambda_functions", []) or []:
            parts = path.split("/")
            if "functions" in parts:
                i = parts.index("functions")
                if i + 1 < len(parts):
                    roles.append(parts[i + 1])
            elif len(parts) >= 2 and parts[0] == "src":
                # ``src/app/lambda_handler.py`` → ``app``
                roles.append(parts[1])
        return roles

    @staticmethod
    def _attach_canonical_role(
        fn: FunctionMetadata,
        decision: ArchitecturalDecision,
        canonical_roles: list[str],
    ) -> None:
        """Pick the canonical role that best matches this function."""
        if not canonical_roles:
            return
        if len(canonical_roles) == 1:
            # Single-Lambda projects route every flow into the same handler.
            decision.canonical_role = canonical_roles[0]
            return
        # Multi-Lambda (batch_complex) — match by function name / module name.
        candidates = {
            fn.name.lower(),
            fn.module_name.lower(),
            (fn.display_name or "").lower(),
        }
        for role in canonical_roles:
            if role in candidates or any(role in c for c in candidates):
                decision.canonical_role = role
                return
        # No match — leave empty; the function generator will emit the
        # canonical handlers separately and the audit report will surface
        # the unmatched flow as a risk.
        decision.risk_notes.append(
            f"function {fn.name!r} did not map to any canonical role "
            f"({', '.join(canonical_roles)}); review the migration-type spec."
        )


__all__ = ["ArchitecturalPlanner"]
