from __future__ import annotations

import base64
import json
import os
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator
from uuid import uuid4


def b64enc(value: str) -> str:
    return "b64:" + base64.b64encode((value or "").encode("utf-8")).decode("ascii")


def b64dec(value: str) -> str:
    if isinstance(value, str) and value.startswith("b64:"):
        try:
            return base64.b64decode(value[4:]).decode("utf-8")
        except Exception:
            return value
    return value or ""


def extract_primary_code(content: str) -> str:
    start = content.find("[PRIMARY_CODE_BLOCK]")
    end = content.find("[/PRIMARY_CODE_BLOCK]")
    if start >= 0 and end > start:
        block = content[start + len("[PRIMARY_CODE_BLOCK]"):end]
        match = re.search(r"```(?:\w+)?\n([\s\S]*?)```", block)
        return (match.group(1) if match else block).strip()
    matches = re.findall(r"```(?:\w+)?\n([\s\S]*?)```", content or "")
    return max((m.strip() for m in matches), key=len, default="")


@contextmanager
def db() -> Iterator[Any]:
    try:
        import psycopg
        from psycopg.rows import dict_row
    except Exception as exc:
        raise RuntimeError("Python backend DB migration requires psycopg[binary]. Install it in the FastAPI environment.") from exc

    conn = psycopg.connect(_database_url(), row_factory=dict_row)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def fetch_files(project_id: str, file_ids: list[str] | None = None, statuses: list[str] | None = None) -> list[dict[str, Any]]:
    where = ['"projectId" = %s', '"type" = %s']
    params: list[Any] = [project_id, "file"]
    if file_ids:
        where.append("id = ANY(%s)")
        params.append(file_ids)
    if statuses:
        where.append("status = ANY(%s)")
        params.append(statuses)

    with db() as conn:
        rows = conn.execute(
            f'''
            SELECT id, "projectId", name, path, type, language, status,
                   content, "migratedCode", "migratedContent"
            FROM "ProjectFile"
            WHERE {" AND ".join(where)}
            ORDER BY path ASC
            ''',
            params,
        ).fetchall()
    return list(rows)


def fetch_project_structure(project_id: str) -> str:
    with db() as conn:
        rows = conn.execute(
            '''
            SELECT path, name, type
            FROM "ProjectFile"
            WHERE "projectId" = %s
            ORDER BY path ASC
            ''',
            [project_id],
        ).fetchall()
    return "\n".join(f"{'[DIR] ' if row['type'] == 'folder' else '      '}{row['path']}" for row in rows)


def upsert_batch(
    *,
    migration_id: str,
    project_id: str,
    provider: str,
    model: str,
    total_files: int,
    user_id: str,
    user_name: str = "Developer",
) -> None:
    with db() as conn:
        conn.execute(
            '''
            INSERT INTO "MigrationBatch"
                (id, "projectId", provider, model, status, "triggeredById", "triggeredByName",
                 "fileResults", "totalFiles", "completedFiles", "failedFiles", "totalTokens")
            VALUES (%s, %s, %s, %s, 'running', %s, %s, '[]'::jsonb, %s, 0, 0, 0)
            ON CONFLICT (id) DO UPDATE SET status = 'running'
            ''',
            [migration_id, project_id, provider, model, user_id, user_name, total_files],
        )


def mark_files_pending(file_ids: list[str], migration_id: str | None = None) -> None:
    if not file_ids:
        return
    with db() as conn:
        if migration_id:
            conn.execute(
                '''
                UPDATE "ProjectFile"
                SET status = %s,
                    "activeMigrationId" = %s,
                    "migratedContent" = NULL,
                    "migratedCode" = NULL
                WHERE id = ANY(%s)
                ''',
                ["pending", migration_id, file_ids],
            )
        else:
            conn.execute(
                '''
                UPDATE "ProjectFile"
                SET status = %s,
                    "migratedContent" = NULL,
                    "migratedCode" = NULL
                WHERE id = ANY(%s)
                ''',
                ["pending", file_ids],
            )


def mark_file_in_progress(file_id: str, migration_id: str) -> None:
    with db() as conn:
        conn.execute(
            'UPDATE "ProjectFile" SET status = %s, "activeMigrationId" = %s WHERE id = %s',
            ["in-progress", migration_id, file_id],
        )


def complete_file(
    *,
    file_id: str,
    migration_id: str,
    provider: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    content: str,
    tokens: int,
    input_tokens: int = 0,
    output_tokens: int = 0,
) -> None:
    code = extract_primary_code(content)
    with db() as conn:
        conn.execute(
            '''
            UPDATE "ProjectFile"
            SET status = 'completed',
                "migratedContent" = %s,
                "migratedCode" = %s,
                "activeMigrationId" = %s
            WHERE id = %s
            ''',
            [b64enc(content), b64enc(code) if code else None, migration_id, file_id],
        )
        conn.execute(
            '''
            INSERT INTO "MigrationRecord"
                (id, "fileId", provider, model, content, code, "systemPrompt", "userPrompt", "rawResponse", tokens)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''',
            [
                f"migrec-{uuid4().hex}",
                file_id,
                provider,
                model,
                b64enc(content),
                b64enc(code) if code else None,
                b64enc(system_prompt),
                b64enc(user_prompt),
                b64enc(content),
                tokens,
            ],
        )


def fail_file(file_id: str, status: str = "failed") -> None:
    with db() as conn:
        conn.execute('UPDATE "ProjectFile" SET status = %s WHERE id = %s', [status, file_id])


def append_batch_result(
    *,
    migration_id: str,
    file_id: str,
    file_name: str,
    file_path: str,
    status: str,
    tokens: int = 0,
    error: str | None = None,
    accuracy_score: int | None = None,
    accuracy_deficiencies: list[str] | None = None,
    accuracy_attempts: int | None = None,
) -> dict[str, Any] | None:
    with db() as conn:
        batch = conn.execute('SELECT * FROM "MigrationBatch" WHERE id = %s FOR UPDATE', [migration_id]).fetchone()
        if not batch:
            return None
        current = batch.get("fileResults") or []
        if isinstance(current, str):
            current = json.loads(current)
        result: dict[str, Any] = {
            "fileId": file_id,
            "fileName": file_name,
            "filePath": file_path,
            "status": status,
        }
        if error:
            result["error"] = error
        if accuracy_score is not None:
            result["accuracyScore"] = accuracy_score
        if accuracy_deficiencies:
            result["accuracyDeficiencies"] = accuracy_deficiencies
        if accuracy_attempts is not None:
            result["accuracyAttempts"] = accuracy_attempts
        current.append(result)

        completed = int(batch["completedFiles"]) + (1 if status == "completed" else 0)
        failed = int(batch["failedFiles"]) + (1 if status in {"failed", "stopped"} else 0)
        total = int(batch["totalFiles"])
        batch_status = "running"
        conn.execute(
            '''
            UPDATE "MigrationBatch"
            SET "completedFiles" = %s,
                "failedFiles" = %s,
                "totalTokens" = "totalTokens" + %s,
                "fileResults" = %s::jsonb,
                status = %s
            WHERE id = %s
            ''',
            [completed, failed, tokens, json.dumps(current), batch_status, migration_id],
        )
        return {"status": batch_status, "completedFiles": completed, "failedFiles": failed, "totalFiles": total}


def complete_batch(migration_id: str) -> None:
    with db() as conn:
        batch = conn.execute('SELECT * FROM "MigrationBatch" WHERE id = %s FOR UPDATE', [migration_id]).fetchone()
        if not batch:
            return
        failed = int(batch.get("failedFiles") or 0)
        batch_status = "completed" if failed == 0 else "partial"
        conn.execute(
            '''
            UPDATE "MigrationBatch"
            SET status = %s,
                "completedAt" = now()
            WHERE id = %s
            ''',
            [batch_status, migration_id],
        )


def stop_batch(migration_id: str) -> None:
    with db() as conn:
        conn.execute(
            'UPDATE "MigrationBatch" SET status = %s, "completedAt" = now() WHERE id = %s',
            ["stopped", migration_id],
        )
        conn.execute(
            'UPDATE "ProjectFile" SET status = %s WHERE "activeMigrationId" = %s AND status = %s',
            ["pending", migration_id, "in-progress"],
        )


def _database_url() -> str:
    url = ""
    value = os.environ.get("DATABASE_URL")
    if value:
        url = value.strip('"')
    else:
        root_dir = Path(__file__).resolve().parent.parent
        for env_path in [root_dir / ".env"]:
            if not env_path.exists():
                continue
            for line in env_path.read_text(encoding="utf-8", errors="ignore").splitlines():
                if line.startswith("DATABASE_URL="):
                    url = line.split("=", 1)[1].strip().strip('"')
                    break
            if url:
                break
    
    if not url:
        raise RuntimeError("DATABASE_URL is not configured for Python backend migration")

    # Do NOT strip query params — ?sslmode=require is needed for Neon / managed Postgres.
    # psycopg3 accepts the full connection string including SSL parameters.
    return url


def fetch_migration_analytics() -> dict[str, Any]:
    with db() as conn:
        batches = conn.execute(
            '''
            SELECT id, "projectId", "startedAt", "completedAt", "fileResults"
            FROM "MigrationBatch"
            '''
        ).fetchall()
        
        records = conn.execute(
            '''
            SELECT "fileId", "content", tokens
            FROM "MigrationRecord"
            '''
        ).fetchall()
        
    file_records = {}
    for rec in records:
        fid = rec["fileId"]
        if fid not in file_records:
            file_records[fid] = []
        file_records[fid].append(rec)
        
    INPUT_PRICE_PER_M = 0.06
    OUTPUT_PRICE_PER_M = 0.24
    
    runs = {}
    for batch in batches:
        migration_id = batch["id"]
        project_id = batch["projectId"]
        file_results = batch.get("fileResults") or []
        if isinstance(file_results, str):
            try:
                file_results = json.loads(file_results)
            except Exception:
                file_results = []
                
        run_data = {
            "projectId": project_id,
            "migrationId": migration_id,
            "tokenUsage": {
                "totalInputTokens": 0,
                "totalOutputTokens": 0,
                "perFile": {}
            },
            "costBreakdown": {
                "totalCost": 0.0,
                "perFile": {}
            },
            "files": {},
            "updatedAt": batch["completedAt"].isoformat() if batch.get("completedAt") else batch["startedAt"].isoformat() if batch.get("startedAt") else ""
        }
        
        total_in = 0
        total_out = 0
        total_cost = 0.0
        
        for f in file_results:
            fid = f.get("fileId")
            if not fid: continue
            
            recs = file_records.get(fid, [])
            file_total_tokens = sum((r.get("tokens") or 0) for r in recs)

            est_input = int(file_total_tokens * 0.7)
            est_output = file_total_tokens - est_input
            
            # Calculate cost
            file_cost = (est_input / 1_000_000) * INPUT_PRICE_PER_M + (est_output / 1_000_000) * OUTPUT_PRICE_PER_M
            
            file_key = f.get("filePath") or fid
            
            run_data["tokenUsage"]["perFile"][file_key] = {
                "inputTokens": est_input,
                "outputTokens": est_output
            }
            run_data["costBreakdown"]["perFile"][file_key] = file_cost
            run_data["files"][file_key] = {
                "fileId": fid,
                "fileName": f.get("fileName", ""),
                "filePath": f.get("filePath", ""),
                "inputTokens": est_input,
                "outputTokens": est_output,
                "cost": file_cost
            }
            
            total_in += est_input
            total_out += est_output
            total_cost += file_cost
            
        run_data["tokenUsage"]["totalInputTokens"] = total_in
        run_data["tokenUsage"]["totalOutputTokens"] = total_out
        run_data["costBreakdown"]["totalCost"] = total_cost
        
        runs[migration_id] = run_data
        
    return {"runs": runs}
