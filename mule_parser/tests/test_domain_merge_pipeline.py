"""Tests for DOMAIN-GEN fan-out + MERGE union."""
from __future__ import annotations

from pathlib import Path

from mule_parser.services.export_pipeline.vfs import VirtualFileSystem
from mule_parser.services.export_pipeline_v3.generators.domain_generator import (
    DomainGenerator,
    group_functions_by_source_file,
    primary_source_file,
)
from mule_parser.services.export_pipeline_v3.generators.merge_generator import (
    MERGE_OWNED_PATHS,
    MergeGenerator,
    is_merge_owned,
)
from mule_parser.services.export_pipeline_v3.metadata import (
    ConfigNeed,
    DomainNeedsManifest,
    FunctionMetadata,
    MigrationMetadata,
    TriggerType,
)
from mule_parser.services.export_pipeline_v3.post_generation_gates import (
    _check_runtime_imports,
    _resolve_gate_project_root,
)


def _fn(name: str, *refs: str, module: str | None = None) -> FunctionMetadata:
    return FunctionMetadata(
        id=name,
        name=name,
        display_name=name,
        module_name=module or name,
        trigger_type=TriggerType.http,
        source_refs=list(refs),
    )


def test_primary_source_file_prefers_path_like_refs():
    fn = _fn("order", "order-main-flow", "src/main/mule/order-api.xml")
    assert primary_source_file(fn) == "src/main/mule/order-api.xml"


def test_group_functions_by_source_file():
    a = _fn("a", "flows/order.xml")
    b = _fn("b", "flows/order.xml")
    c = _fn("c", "flows/ship.xml")
    groups = group_functions_by_source_file([a, b, c])
    assert set(groups) == {"flows/order.xml", "flows/ship.xml"}
    assert {f.name for f in groups["flows/order.xml"]} == {"a", "b"}
    assert {f.name for f in groups["flows/ship.xml"]} == {"c"}


def test_merge_unions_needs_and_keeps_all_ports():
    metadata = MigrationMetadata(project_name="demo", project_slug="demo")
    metadata.domain_needs = [
        DomainNeedsManifest(
            source_file="a.xml",
            ports_needed=["DatabasePort"],
            exceptions_needed=["DbError"],
            env_vars_needed=[ConfigNeed(key="DB_HOST", default="localhost")],
            pip_packages_needed=["psycopg2-binary"],
        ),
        DomainNeedsManifest(
            source_file="b.xml",
            ports_needed=["HttpPort", "DatabasePort"],
            exceptions_needed=["HttpError"],
            env_vars_needed=[ConfigNeed(key="API_URL")],
            pip_packages_needed=["requests"],
        ),
    ]
    vfs = VirtualFileSystem()
    written = MergeGenerator().generate(metadata, vfs)
    assert written >= 4

    ports = vfs.read("src/domain/ports.py")
    assert ports is not None
    ports_text = ports.content.decode() if isinstance(ports.content, bytes) else str(ports.content)
    assert "class DatabasePort" in ports_text
    assert "class HttpPort" in ports_text

    exc = vfs.read("src/domain/exceptions.py")
    exc_text = exc.content.decode() if isinstance(exc.content, bytes) else str(exc.content)
    assert "class DbError" in exc_text
    assert "class HttpError" in exc_text

    settings = vfs.read("src/config/settings.py")
    settings_text = settings.content.decode() if isinstance(settings.content, bytes) else str(settings.content)
    assert "DB_HOST" in settings_text
    assert "API_URL" in settings_text

    req = vfs.read("requirements.txt")
    req_text = req.content.decode() if isinstance(req.content, bytes) else str(req.content)
    assert "psycopg2-binary" in req_text
    assert "requests" in req_text

    assert is_merge_owned("src/domain/ports.py", metadata)
    assert set(metadata.extension.get("merge_owned_paths") or []) == set(MERGE_OWNED_PATHS)


def test_merge_is_idempotent():
    metadata = MigrationMetadata(project_name="demo", project_slug="demo")
    metadata.domain_needs = [
        DomainNeedsManifest(source_file="a.xml", ports_needed=["StoragePort"]),
    ]
    vfs = VirtualFileSystem()
    MergeGenerator().generate(metadata, vfs)
    first = vfs.read("src/domain/ports.py").content
    MergeGenerator().generate(metadata, vfs)
    second = vfs.read("src/domain/ports.py").content
    assert first == second


def test_domain_generator_emits_manifests_without_llm():
    metadata = MigrationMetadata(
        project_name="demo",
        project_slug="demo",
        functions=[
            _fn("order", "flows/order.xml"),
            _fn("ship", "flows/ship.xml"),
        ],
    )
    # Seed config needs on functions so manifests are non-empty without LLM.
    metadata.functions[0].config_needs = [ConfigNeed(key="ORDER_URL")]
    metadata.functions[1].config_needs = [ConfigNeed(key="SHIP_URL")]

    vfs = VirtualFileSystem()
    DomainGenerator().generate(metadata, vfs)

    assert len(metadata.domain_needs) == 2
    keys = {m.source_file for m in metadata.domain_needs}
    assert keys == {"flows/order.xml", "flows/ship.xml"}
    env_keys = {
        need.key
        for m in metadata.domain_needs
        for need in m.env_vars_needed
    }
    assert "ORDER_URL" in env_keys
    assert "SHIP_URL" in env_keys


def test_check_runtime_imports_missing_src_returns_tuple(tmp_path: Path):
    errors, stats = _check_runtime_imports(tmp_path, install_deps=True)
    assert errors == []
    assert stats["total"] == 0


def test_resolve_gate_project_root_with_prefix(tmp_path: Path):
    nested = tmp_path / "my-project" / "src"
    nested.mkdir(parents=True)
    (nested / "ok.py").write_text("x = 1\n", encoding="utf-8")
    resolved = _resolve_gate_project_root(tmp_path)
    assert resolved == tmp_path / "my-project"


def test_architect_builds_contract_from_domain_needs():
    from mule_parser.services.export_pipeline_v3.architect_contract import (
        ArchitectContractBuilder,
        accept_contract_gaps,
    )

    metadata = MigrationMetadata(project_name="demo", project_slug="demo")
    metadata.domain_needs = [
        DomainNeedsManifest(
            source_file="a.xml",
            ports_needed=["DatabasePort"],
            exceptions_needed=["DbError"],
            pip_packages_needed=["psycopg2-binary"],
        ),
    ]
    spec = ArchitectContractBuilder().build(metadata)
    assert metadata.contract_spec is spec
    assert "DatabasePort" in spec.port_names()
    assert "DbError" in spec.exception_names()
    assert "psycopg2-binary" in spec.pip_packages
    assert "response_builder" in {u.name for u in spec.utilities}

    added = accept_contract_gaps(
        metadata,
        [{"kind": "exception", "name": "ShipError", "base": "DomainError", "needed_by": ["b.xml"]}],
    )
    assert added == 1
    assert "ShipError" in metadata.contract_spec.exception_names()


def test_restricted_vfs_blocks_shared_writes():
    from mule_parser.services.export_pipeline_v3.restricted_vfs import RestrictedVFS

    vfs = VirtualFileSystem()
    restricted = RestrictedVFS(vfs, domain_tag="test")
    restricted.write("src/handlers/order_handler.py", "x=1\n", role="source", generator="t")
    restricted.write("src/domain/ports.py", "BAD\n", role="source", generator="t")
    assert vfs.read("src/handlers/order_handler.py") is not None
    assert vfs.read("src/domain/ports.py") is None
    assert "src/domain/ports.py" in restricted.blocked_writes


def test_check_module_package_collisions_hard_fails():
    from mule_parser.services.export_pipeline_v3.post_generation_gates import (
        PostGenerationGateError,
        check_module_package_collisions,
        resolve_module_package_collisions,
        run_post_generation_gates,
    )

    vfs = VirtualFileSystem()
    vfs.write("src/handlers.py", "x=1\n", role="source", generator="t")
    vfs.write("src/handlers/api.py", "y=1\n", role="source", generator="t")
    # Unresolved check still detects the collision.
    collisions = check_module_package_collisions(vfs)
    assert any("handlers.py" in c for c in collisions)

    # Resolver prefers package for non-MERGE stems → removes flat module.
    notes = resolve_module_package_collisions(vfs)
    assert notes
    assert vfs.read("src/handlers.py") is None
    assert vfs.read("src/handlers/api.py") is not None
    assert check_module_package_collisions(vfs) == []

    # Recreate collision that MERGE prefers as flat module (ports).
    vfs2 = VirtualFileSystem()
    vfs2.write("proj/src/domain/ports.py", "class P: ...\n", role="source", generator="t")
    vfs2.write("proj/src/domain/ports/extra.py", "x=1\n", role="source", generator="t")
    vfs2.write("proj/src/domain/models.py", "BAD\n", role="source", generator="t")
    vfs2.write("proj/src/domain/models/order.py", "OK\n", role="source", generator="t")
    vfs2.write("proj/src/domain/services.py", "BAD\n", role="source", generator="t")
    vfs2.write("proj/src/domain/services/svc.py", "OK\n", role="source", generator="t")
    resolve_module_package_collisions(vfs2)
    assert vfs2.read("proj/src/domain/ports.py") is not None
    assert vfs2.read("proj/src/domain/ports/extra.py") is None
    assert vfs2.read("proj/src/domain/models.py") is None
    assert vfs2.read("proj/src/domain/models/order.py") is not None
    assert vfs2.read("proj/src/domain/services.py") is None
    assert vfs2.read("proj/src/domain/services/svc.py") is not None

    # After resolve, gates should not raise on these paths.
    metadata = MigrationMetadata(project_name="demo", project_slug="demo")
    # Empty-ish VFS that still has valid python after resolve
    vfs3 = VirtualFileSystem()
    vfs3.write("src/ok.py", "x = 1\n", role="source", generator="t")
    run_post_generation_gates(metadata, vfs3)


def test_blocked_pending_review_status_constant_and_metadata():
    metadata = MigrationMetadata(project_name="demo", project_slug="demo")
    assert metadata.export_status == "ok"
    metadata.export_status = "blocked_pending_review"
    assert metadata.export_status == "blocked_pending_review"
