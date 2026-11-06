import { NextRequest, NextResponse } from 'next/server';

/** Python execution plane (FastAPI) — primary backend for export. */
export function getFastApiUrl(): string {
    return (process.env.FASTAPI_URL || 'http://127.0.0.1:8000').replace(/\/$/, '');
}

/** Optional Fastify control plane fallback (port 3001). */
export function getFastifyUrl(): string {
    return (process.env.FASTIFY_URL || process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001').replace(/\/$/, '');
}

export const VALID_EXPORT_FORMATS = ['zip', 'sam', 'cloudformation', 'terraform', 'cpi-package', 'cpi-iflow', 'cpi-tenant-push'] as const;
export type ExportFormat = (typeof VALID_EXPORT_FORMATS)[number];

export const PASSTHROUGH_EXPORT_HEADERS = [
    'x-export-format',
    'x-export-file-count',
    'x-export-sha256',
    'x-export-pipeline',
    'x-export-components-total',
    'x-export-components-covered',
    'x-export-archetype',
    'x-export-archetype-confidence',
    'x-export-complexity',
] as const;

export function isValidExportFormat(format: string): format is ExportFormat {
    return (VALID_EXPORT_FORMATS as readonly string[]).includes(format);
}

export function previewUrl(projectId: string, format: string, targetRuntime: string, pipeline: string, targetPlatform?: string): string {
    const base = getFastApiUrl();
    const params = new URLSearchParams({
        format,
        target_runtime: targetRuntime,
        pipeline,
    });
    if (targetPlatform) {
        params.set('target_platform', targetPlatform);
    }
    return `${base}/internal/projects/${encodeURIComponent(projectId)}/export/preview?${params}`;
}

export function exportUrl(projectId: string): string {
    return `${getFastApiUrl()}/internal/projects/${encodeURIComponent(projectId)}/export`;
}

/** Fastify proxy path used when FastAPI is unreachable. */
export function fastifyPreviewUrl(projectId: string, format: string, targetRuntime: string, pipeline: string, targetPlatform?: string): string {
    const params = new URLSearchParams({ format, targetRuntime, pipeline });
    if (targetPlatform) {
        params.set('targetPlatform', targetPlatform);
    }
    return `${getFastifyUrl()}/api/projects/${encodeURIComponent(projectId)}/export/preview?${params}`;
}

export function fastifyExportUrl(projectId: string): string {
    return `${getFastifyUrl()}/api/projects/${encodeURIComponent(projectId)}/export`;
}

async function fetchPreviewFromFastApi(
    projectId: string,
    format: string,
    targetRuntime: string,
    pipeline: string,
    targetPlatform?: string,
): Promise<{ ok: boolean; status: number; data: unknown }> {
    try {
        const upstream = await fetch(previewUrl(projectId, format, targetRuntime, pipeline, targetPlatform), { cache: 'no-store' });
        const text = await upstream.text();
        let data: unknown = null;
        try {
            data = text ? JSON.parse(text) : null;
        } catch {
            data = { error: 'Invalid JSON from export preview', detail: text.slice(0, 500) };
        }
        return { ok: upstream.ok, status: upstream.status, data };
    } catch (error: unknown) {
        const detail = error instanceof Error ? error.message : String(error);
        return { ok: false, status: 502, data: { error: 'Failed to reach export pipeline', detail } };
    }
}

async function fetchPreviewFromFastify(
    projectId: string,
    format: string,
    targetRuntime: string,
    pipeline: string,
    targetPlatform?: string,
): Promise<{ ok: boolean; status: number; data: unknown }> {
    try {
        const upstream = await fetch(fastifyPreviewUrl(projectId, format, targetRuntime, pipeline, targetPlatform), { cache: 'no-store' });
        const text = await upstream.text();
        let data: unknown = null;
        try {
            data = text ? JSON.parse(text) : null;
        } catch {
            data = { error: 'Invalid JSON from Fastify export preview', detail: text.slice(0, 500) };
        }
        return { ok: upstream.ok, status: upstream.status, data };
    } catch {
        return { ok: false, status: 502, data: null };
    }
}

export async function fetchExportPreview(
    projectId: string,
    format: string,
    targetRuntime: string,
    pipeline: string,
    targetPlatform?: string,
): Promise<{ ok: boolean; status: number; data: unknown }> {
    const primary = await fetchPreviewFromFastApi(projectId, format, targetRuntime, pipeline, targetPlatform);
    if (primary.ok && primary.data && typeof primary.data === 'object') {
        const payload = primary.data as Record<string, unknown>;
        const manifest = payload.manifest as Record<string, unknown> | undefined;
        const files = manifest?.files;
        if (Array.isArray(files) && files.length > 0) {
            return primary;
        }
        if (payload.fileCount && Number(payload.fileCount) > 0) {
            return primary;
        }
    }

    const fallback = await fetchPreviewFromFastify(projectId, format, targetRuntime, pipeline, targetPlatform);
    if (fallback.ok && fallback.data) {
        return fallback;
    }

    if (primary.data) {
        return { ok: primary.ok, status: primary.status, data: primary.data };
    }
    return fallback.ok ? fallback : primary;
}

export async function postExportDownload(
    projectId: string,
    body: {
        format: string;
        targetRuntime: string;
        targetPlatform?: string;
        projectNameHint: string;
        pipeline: string;
    },
): Promise<Response> {
    const payload = {
        format: body.format,
        target_runtime: body.targetRuntime,
        targetRuntime: body.targetRuntime,
        target_platform: body.targetPlatform,
        targetPlatform: body.targetPlatform,
        project_name_hint: body.projectNameHint,
        projectNameHint: body.projectNameHint,
        pipeline: body.pipeline,
    };

    let upstream: Response;
    try {
        upstream = await fetch(exportUrl(projectId), {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify(payload),
            cache: 'no-store',
        });
    } catch (error: unknown) {
        const detail = error instanceof Error ? error.message : String(error);
        return NextResponse.json(
            { error: 'Failed to reach export pipeline', detail: `Is FastAPI running at ${getFastApiUrl()}? ${detail}` },
            { status: 502 },
        );
    }

    if (!upstream.ok) {
        const firstError = await upstream.text().catch(() => '');
        try {
            const retry = await fetch(fastifyExportUrl(projectId), {
                method: 'POST',
                headers: { 'content-type': 'application/json' },
                body: JSON.stringify(body),
                cache: 'no-store',
            });
            if (retry.ok) {
                upstream = retry;
            } else {
                const retryError = await retry.text().catch(() => '');
                return new NextResponse(retryError || firstError || JSON.stringify({ error: `Export failed (${retry.status})` }), {
                    status: retry.status,
                    headers: { 'content-type': retry.headers.get('content-type') || 'application/json' },
                });
            }
        } catch {
            return new NextResponse(firstError || JSON.stringify({ error: `Export failed (${upstream.status})` }), {
                status: upstream.status,
                headers: { 'content-type': upstream.headers.get('content-type') || 'application/json' },
            });
        }
    }

    const buffer = await upstream.arrayBuffer();
    const headers = new Headers();
    headers.set('content-type', upstream.headers.get('content-type') || 'application/zip');
    headers.set(
        'content-disposition',
        upstream.headers.get('content-disposition') || `attachment; filename="${projectId}-${body.format}.zip"`,
    );
    for (const key of PASSTHROUGH_EXPORT_HEADERS) {
        const v = upstream.headers.get(key);
        if (v) headers.set(key, v);
    }
    return new NextResponse(buffer, { status: 200, headers });
}
