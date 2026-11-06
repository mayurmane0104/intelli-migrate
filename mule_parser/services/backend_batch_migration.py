from __future__ import annotations

import concurrent.futures
import logging
from dataclasses import dataclass
from typing import Any, Callable

from mule_parser.services.backend_file_migration import generate_file_migration
from mule_parser.services.migration_db import (
    append_batch_result,
    b64dec,
    complete_file,
    fail_file,
    fetch_files,
    fetch_migration_analytics,
    fetch_project_structure,
    mark_file_in_progress,
    mark_files_pending,
    stop_batch,
    upsert_batch,
)

logger = logging.getLogger(__name__)

EventEmitter = Callable[[str, dict[str, Any]], None]


@dataclass(frozen=True)
class BackendJob:
    id: str
    file_id: str
    file_name: str
    file_path: str
    migration_id: str

    def as_response(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "fileId": self.file_id,
            "fileName": self.file_name,
            "filePath": self.file_path,
            "migrationId": self.migration_id,
        }


def start_backend_batch(
    *,
    project_id: str,
    file_ids: list[str],
    migration_id: str,
    migration_type: str,
    target_runtime: str,
    target_platform: str | None = None,
    user_id: str,
    emit: EventEmitter,
    active_provider: str | None = None,
    provider_config: dict[str, Any] | None = None,
    instructions: str = "",
) -> list[BackendJob]:
    files = fetch_files(project_id, file_ids=file_ids)
    mark_files_pending([f["id"] for f in files], migration_id=migration_id)
    provider_label = (active_provider or "nova").strip().lower()
    upsert_batch(
        migration_id=migration_id,
        project_id=project_id,
        provider=f"python-backend-{provider_label}",
        model=provider_config.get("model", "bedrock") if provider_config else "bedrock",
        total_files=len(files),
        user_id=user_id,
    )
    jobs = [_job_from_file(file, migration_id) for file in files]
    emit("migration.started", {"migrationId": migration_id, "totalFiles": len(files)})
    _run_files(
        project_id=project_id,
        migration_id=migration_id,
        migration_type=migration_type,
        target_runtime=target_runtime,
        target_platform=target_platform,
        files=files,
        emit=emit,
        active_provider=active_provider,
        provider_config=provider_config,
        instructions=instructions,
    )
    return jobs


def resume_backend_batch(
    *,
    project_id: str,
    migration_id: str,
    migration_type: str,
    target_runtime: str,
    target_platform: str | None = None,
    emit: EventEmitter,
    active_provider: str | None = None,
    provider_config: dict[str, Any] | None = None,
    instructions: str = "",
) -> list[BackendJob]:
    files = fetch_files(project_id, statuses=["pending", "failed", "stopped"])
    mark_files_pending([f["id"] for f in files], migration_id=migration_id)
    jobs = [_job_from_file(file, migration_id) for file in files]
    emit("migration.resumed", {"migrationId": migration_id, "totalFiles": len(files)})
    _run_files(
        project_id=project_id,
        migration_id=migration_id,
        migration_type=migration_type,
        target_runtime=target_runtime,
        target_platform=target_platform,
        files=files,
        emit=emit,
        active_provider=active_provider,
        provider_config=provider_config,
        instructions=instructions,
    )
    return jobs


def retry_backend_file(
    *,
    project_id: str,
    file_id: str,
    migration_id: str,
    migration_type: str,
    target_runtime: str,
    target_platform: str | None = None,
    emit: EventEmitter,
    active_provider: str | None = None,
    provider_config: dict[str, Any] | None = None,
    instructions: str = "",
) -> BackendJob:
    files = fetch_files(project_id, file_ids=[file_id])
    if not files:
        raise ValueError(f"File not found: {file_id}")
    mark_files_pending([file_id], migration_id=migration_id)
    job = _job_from_file(files[0], migration_id)
    emit("migration.retry_started", {"migrationId": migration_id, "fileId": file_id})
    _run_files(
        project_id=project_id,
        migration_id=migration_id,
        migration_type=migration_type,
        target_runtime=target_runtime,
        target_platform=target_platform,
        files=files,
        emit=emit,
        active_provider=active_provider,
        provider_config=provider_config,
        instructions=instructions,
    )
    return job


def stop_backend_batch(migration_id: str, emit: EventEmitter) -> None:
    stop_batch(migration_id)
    emit("migration.stopped", {"migrationId": migration_id})


def _run_files(
    *,
    project_id: str,
    migration_id: str,
    migration_type: str,
    target_runtime: str,
    target_platform: str | None = None,
    files: list[dict[str, Any]],
    emit: EventEmitter,
    active_provider: str | None = None,
    provider_config: dict[str, Any] | None = None,
    instructions: str = "",
) -> None:
    project_structure = fetch_project_structure(project_id)
    def _process_file(file: dict[str, Any]) -> None:
        job = _job_from_file(file, migration_id)
        emit("job.started", {"jobId": job.id, "fileId": job.file_id, "fileName": job.file_name})
        try:
            mark_file_in_progress(job.file_id, migration_id)
            emit("job.progress", {"jobId": job.id, "fileId": job.file_id, "progress": 10})
            result = generate_file_migration(
                file_name=job.file_name,
                file_path=job.file_path,
                source_content=b64dec(file["content"]),
                migration_type=migration_type,
                target_runtime=target_runtime,
                target_platform=target_platform,
                project_structure=project_structure,
                project_id=project_id,
                active_provider=active_provider,
                provider_config=provider_config,
                instructions=instructions,
            )
            content = result.content
            tokens = result.input_tokens + result.output_tokens
            complete_file(
                file_id=job.file_id,
                migration_id=migration_id,
                provider=result.provider,
                model=result.model,
                system_prompt=result.system_prompt,
                user_prompt=result.user_prompt,
                content=content,
                tokens=tokens,
                input_tokens=result.input_tokens,
                output_tokens=result.output_tokens,
            )
            batch = append_batch_result(
                migration_id=migration_id,
                file_id=job.file_id,
                file_name=job.file_name,
                file_path=job.file_path,
                status="completed",
                tokens=tokens,
                accuracy_score=result.accuracy_score,
                accuracy_deficiencies=list(result.accuracy_deficiencies),
                accuracy_attempts=result.accuracy_attempts,
            )
            emit("job.token", {"jobId": job.id, "fileId": job.file_id, "token": content})
            emit(
                "job.completed",
                {
                    "jobId": job.id,
                    "fileId": job.file_id,
                    "migrationId": migration_id,
                    "tokens": tokens,
                    "batch": batch,
                },
            )
        except Exception as exc:
            logger.exception("Backend migration failed for %s", job.file_path)
            fail_file(job.file_id)
            batch = append_batch_result(
                migration_id=migration_id,
                file_id=job.file_id,
                file_name=job.file_name,
                file_path=job.file_path,
                status="failed",
                error=str(exc),
            )
            emit(
                "job.failed",
                {
                    "jobId": job.id,
                    "fileId": job.file_id,
                    "migrationId": migration_id,
                    "error": str(exc),
                    "batch": batch,
                },
            )

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(_process_file, f) for f in files]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    # Precompute export artifact in background — download should not wait on zip.
    import threading

    threading.Thread(
        target=_prewarm_export,
        args=(project_id, target_runtime, target_platform, migration_id),
        daemon=True,
        name=f"export-prewarm-{migration_id}",
    ).start()

    _log_analytics(migration_id)


def _prewarm_export(project_id: str, target_runtime: str, target_platform: str | None, migration_id: str) -> None:
    from mule_parser.services.migration_db import complete_batch
    try:
        from mule_parser.services.export_service import prewarm_export_cache

        prewarm_export_cache(
            project_id,
            target_runtime=(target_runtime or "python"),
            target_platform=target_platform,
        )
    except Exception:
        logger.warning("Export prewarm failed for project=%s", project_id, exc_info=True)
    finally:
        try:
            complete_batch(migration_id)
        except Exception:
            logger.exception("Failed to mark batch %s as complete", migration_id)


def _log_analytics(migration_id: str) -> None:
    try:
        analytics = fetch_migration_analytics().get("runs", {}).get(migration_id)
    except Exception as exc:
        logger.warning("Migration analytics logging skipped: %s", exc)
        return

    if not analytics:
        return
        
    for file_key, file_data in analytics["files"].items():
        print(f"[MIGRATION ANALYTICS - INTERNAL]")
        print(f"File: {file_data.get('fileName') or file_key}")
        print(f"Input Tokens  : {file_data.get('inputTokens', 0):,}")
        print(f"Output Tokens : {file_data.get('outputTokens', 0):,}")
        print(f"File Cost     : ${file_data.get('cost', 0):.4f}")
        
    print(f"[MIGRATION ANALYTICS - INTERNAL]")
    print(f"Project Totals:")
    print(f"Total Input Tokens  : {analytics['tokenUsage']['totalInputTokens']:,}")
    print(f"Total Output Tokens : {analytics['tokenUsage']['totalOutputTokens']:,}")
    print(f"Total LLM Cost      : ${analytics['costBreakdown']['totalCost']:.4f}")


def _job_from_file(file: dict[str, Any], migration_id: str) -> BackendJob:
    file_id = file["id"]
    return BackendJob(
        id=f"py-{migration_id}-{file_id}",
        file_id=file_id,
        file_name=file.get("name") or "Unknown",
        file_path=file.get("path") or "Unknown",
        migration_id=migration_id,
    )
