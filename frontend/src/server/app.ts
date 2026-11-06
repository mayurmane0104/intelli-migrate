import dotenv from 'dotenv';
import path from 'path';
import fs from 'fs';

// Static .env mounted at /app/.env in Docker (EC2). Fall back to mule_parser/.env locally.
const envCandidates = [
    process.env.APP_ENV_FILE,
    '/app/.env',
    path.resolve(__dirname, '../../../.env'),
    path.resolve(__dirname, '../../../../.env'),
].filter((p): p is string => Boolean(p));

for (const envPath of envCandidates) {
    if (fs.existsSync(envPath)) {
        // Do not override vars already set by start-fastify.sh (PORT=3001).
        dotenv.config({ path: envPath, override: false });
    }
}
dotenv.config({ override: false });

// Startup diagnostics (mask secrets)
const loadedProviders = process.env.LLM_PROVIDERS ? process.env.LLM_PROVIDERS.split(',') : [];
console.log('Loaded LLM Providers:', loadedProviders.length > 0 ? loadedProviders : 'none');
console.log('Loaded Bedrock Model ID:', process.env.BEDROCK_MODEL_ID ? 'present' : 'missing');
console.log('Loaded AWS Region:', process.env.AWS_DEFAULT_REGION || process.env.AWS_REGION || 'missing');
console.log('Nova Enabled:', process.env.BEDROCK_MODEL_ID && process.env.AWS_ACCESS_KEY_ID && process.env.AWS_SECRET_ACCESS_KEY ? 'yes' : 'no');
import fastify, { FastifyRequest, FastifyReply } from 'fastify';
import cors from '@fastify/cors';
import jwt from 'jsonwebtoken';
import { Server } from 'socket.io';
import { MigrationConfig } from '../lib/types';
import { userMigrationGuard } from '@/lib/store';
import { jobEvents } from '../lib/lib/events';
import { saveIRToFile } from '../lib/server/save-ir';
import { Readable } from 'stream';

const app = fastify({ logger: true });

// CORS setup — allow requests from the frontend app only
const frontendUrl = process.env.FRONTEND_URL || 'http://localhost:3000';
app.register(cors, {
    origin: frontendUrl,
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
});

// Socket.io setup
const io = new Server(app.server as any, {
    cors: {
        origin: frontendUrl,
    },
});

io.on('connection', (socket) => {
    console.log('Client connected:', socket.id);

    // Allow clients to join rooms for specific projects or jobs
    socket.on('join:project', (projectId) => {
        socket.join(`project:${projectId}`);
        console.log(`Socket ${socket.id} joined project:${projectId}`);
    });
});

// Bridge Logs (Tokens) for live synthesis
jobEvents.on('token', ({ jobId, projectId, token }) => {
    io.to(`project:${projectId}`).emit('job:token', { jobId, token });
});

import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();
const fastApiUrl = process.env.FASTAPI_URL || 'http://localhost:8000';
const persistedIrJobIds = new Set<string>();
const emittedTerminalBatchIds = new Set<string>();
const backendEventMirrors = new Map<string, NodeJS.Timeout>();


async function emitBatchLifecycleIfTerminal(projectId: string, migrationId?: string): Promise<void> {
    if (!migrationId) return;

    const batch = await prisma.migrationBatch.findUnique({
        where: { id: migrationId },
        select: {
            id: true,
            projectId: true,
            status: true,
            triggeredById: true,
            totalFiles: true,
            completedFiles: true,
            failedFiles: true,
        }
    });

    if (!batch) return;

    const isTerminal = ['completed', 'partial', 'failed', 'stopped'].includes(batch.status);
    const isFullyProcessed = (batch.completedFiles + batch.failedFiles) >= batch.totalFiles || batch.status === 'stopped';
    if (!isTerminal || !isFullyProcessed) return;
    if (emittedTerminalBatchIds.has(batch.id)) return;

    if (batch.triggeredById) {
        userMigrationGuard.release(batch.triggeredById);
    }
    emittedTerminalBatchIds.add(batch.id);

    io.to(`project:${projectId}`).emit('migration:batch-complete', {
        projectId,
        migrationId: batch.id,
        status: batch.status,
        totalFiles: batch.totalFiles,
        completedFiles: batch.completedFiles,
        failedFiles: batch.failedFiles,
    });
}

type ProxyResponse = {
    status: number;
    body: unknown;
};

// P0-A: Maximum time we will wait for the execution plane before returning 504.
// Prevents a slow FastAPI from hanging the Fastify process indefinitely.
const EXECUTION_PLANE_TIMEOUT_MS = 30_000;

async function proxyExecutionPlane(path: string, init?: RequestInit): Promise<ProxyResponse> {
    const url = `${fastApiUrl}${path}`;

    // Merge caller-supplied signal with our hard timeout so BOTH can cancel the request.
    const timeoutController = new AbortController();
    const timeoutId = setTimeout(() => timeoutController.abort(new Error('execution-plane-timeout')), EXECUTION_PLANE_TIMEOUT_MS);

    let response: Response;
    try {
        response = await fetch(url, {
            ...init,
            signal: timeoutController.signal,
        });
    } catch (err: any) {
        clearTimeout(timeoutId);
        const isTimeout = err?.name === 'AbortError' || String(err?.message).includes('execution-plane-timeout');
        return {
            status: isTimeout ? 504 : 502,
            body: {
                message: isTimeout
                    ? `Execution plane timed out after ${EXECUTION_PLANE_TIMEOUT_MS}ms`
                    : `Execution plane unreachable: ${err?.message ?? err}`,
            },
        };
    } finally {
        clearTimeout(timeoutId);
    }

    // Read the body exactly once — undici Response bodies are single-shot, so
    // a failed json() call burns the buffer and a follow-up text() throws
    // "Body is unusable: Body has already been read".
    let raw = '';
    try {
        raw = await response.text();
    } catch (err) {
        return {
            status: response.status,
            body: { message: `Failed to read response body: ${(err as Error)?.message ?? err}` },
        };
    }

    let payload: unknown = null;
    if (raw) {
        try {
            payload = JSON.parse(raw);
        } catch {
            payload = { message: raw };
        }
    } else {
        payload = null;
    }

    return {
        status: response.status,
        body: payload,
    };
}

function startBackendEventMirror(projectId: string, migrationId: string): void {
    const key = `${projectId}:${migrationId}`;
    if (backendEventMirrors.has(key)) return;

    let since = 0;
    const timer = setInterval(async () => {
        try {
            const upstream = await proxyExecutionPlane(`/internal/projects/${projectId}/events?since=${since}`);
            if (upstream.status >= 400) return;
            const body = upstream.body as { events?: Array<Record<string, any>>; latestSeq?: number };
            const events = body.events || [];
            since = body.latestSeq ?? since;

            for (const event of events) {
                if (event.migrationId && event.migrationId !== migrationId) continue;
                const jobId = String(event.jobId || '');
                const fileId = String(event.fileId || '');
                if (event.eventType === 'job.started') {
                    io.to(`project:${projectId}`).emit('job:progress', {
                        jobId,
                        fileId,
                        progress: 5,
                    });
                }
                if (event.eventType === 'job.progress') {
                    io.to(`project:${projectId}`).emit('job:progress', {
                        jobId,
                        fileId,
                        progress: Number(event.progress || 10),
                    });
                }
                if (event.eventType === 'job.token') {
                    io.to(`project:${projectId}`).emit('job:token', {
                        jobId,
                        token: String(event.token || ''),
                    });
                }
                if (event.eventType === 'job.completed') {
                    io.to(`project:${projectId}`).emit('job:completed', {
                        jobId,
                        fileId,
                        result: {
                            status: 'completed',
                            tokens: Number(event.tokens || 0),
                            migrationId,
                            batchCompleted: ['completed', 'partial'].includes(event.batch?.status),
                            batchStatus: event.batch?.status || 'running',
                        },
                    });
                    void emitBatchLifecycleIfTerminal(projectId, migrationId);
                }
                if (event.eventType === 'job.failed') {
                    io.to(`project:${projectId}`).emit('job:failed', {
                        jobId,
                        fileId,
                        error: String(event.error || 'Backend migration failed'),
                    });
                    void emitBatchLifecycleIfTerminal(projectId, migrationId);
                }
                if (event.eventType === 'migration.stopped') {
                    io.to(`project:${projectId}`).emit('migration:stopped', { projectId, migrationId });
                    clearInterval(timer);
                    backendEventMirrors.delete(key);
                }
            }

            const batch = await prisma.migrationBatch.findUnique({ where: { id: migrationId } }).catch(() => null);
            if (batch && ['completed', 'partial', 'failed', 'stopped'].includes(batch.status)) {
                void emitBatchLifecycleIfTerminal(projectId, migrationId);
                clearInterval(timer);
                backendEventMirrors.delete(key);
            }
        } catch (error) {
            app.log.warn(error, 'Backend migration event mirror failed');
        }
    }, 1000);

    backendEventMirrors.set(key, timer);
}

async function persistIRForCompletedJob(projectId: string, jobId: string): Promise<void> {
    if (!jobId || persistedIrJobIds.has(jobId)) return;
    try {
        const rawUpstream = await proxyExecutionPlane(`/internal/analysis/${jobId}/raw`);
        if (rawUpstream.status >= 400) return;
        const rawBody = rawUpstream.body as Record<string, unknown> | null;
        const rawCandidate = (rawBody?.raw_ir ?? rawBody?.rawIr ?? rawBody?.ir ?? rawBody) as unknown;

        const project = await prisma.project.findUnique({
            where: { id: projectId },
            select: { id: true, name: true },
        });
        const sourceFile = String(
            rawBody?.source_file ??
            rawBody?.sourceFile ??
            rawBody?.file_path ??
            rawBody?.filePath ??
            'unknown'
        );

        await saveIRToFile({
            projectId,
            projectName: project?.name || projectId,
            sourceFile,
            irVersion: String(rawBody?.ir_version ?? rawBody?.irVersion ?? 'unknown'),
            ir: rawCandidate,
        });

        persistedIrJobIds.add(jobId);
    } catch (error) {
        app.log.warn(error, 'Auto-persist IR failed');
    }
}

// API Routes
app.post('/api/projects/:id/analysis/start', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const body = (request.body || {}) as Record<string, unknown>;

    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/analysis`, {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify(body),
        });
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to start analysis');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.get('/api/projects/:id/analysis/latest', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const { includeRaw } = (request.query || {}) as { includeRaw?: string | boolean };
    const includeRawFlag = includeRaw === true || includeRaw === 'true';
    const query = includeRawFlag ? '?include_raw=true' : '';

    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/analysis/latest${query}`);
        if (upstream.status < 400) {
            const payload = upstream.body as { jobId?: string; status?: string } | null;
            const completedJobId = payload?.status === 'completed' ? payload?.jobId : undefined;
            if (completedJobId) {
                void persistIRForCompletedJob(id, completedJobId);
            }
        }
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to fetch latest analysis');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.get('/api/projects/:id/analysis/summary', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/analysis/latest/summary`);
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to fetch analysis summary');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.get('/api/projects/:id/analysis/flows', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/analysis/latest/structured-flows`);
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to fetch structured flow analysis');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.get('/api/projects/:id/analysis/validation', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/analysis/latest/validation`);
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to fetch analysis validation');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.get('/api/projects/:id/analysis/raw', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const { jobId } = (request.query || {}) as { jobId?: string };

    try {
        let resolvedJobId = jobId;

        if (!resolvedJobId) {
            const latest = await proxyExecutionPlane(`/internal/projects/${id}/analysis/latest`);
            if (latest.status >= 400) {
                return reply.code(latest.status).send(latest.body);
            }
            const latestPayload = latest.body as { jobId?: string };
            resolvedJobId = latestPayload.jobId;
        }

        if (!resolvedJobId) {
            return reply.code(404).send({ error: 'No analysis job found for project' });
        }

        const upstream = await proxyExecutionPlane(`/internal/analysis/${resolvedJobId}/raw`);
        if (upstream.status >= 400) {
            return reply.code(upstream.status).send(upstream.body);
        }

        const body = upstream.body as Record<string, unknown> | null;
        const rawCandidate = (body?.raw_ir ?? body?.rawIr ?? body?.ir ?? body) as unknown;
        const rawText = JSON.stringify(rawCandidate ?? {});
        const project = await prisma.project.findUnique({
            where: { id },
            select: { id: true, name: true },
        });
        const sourceFile =
            String(body?.source_file ?? body?.sourceFile ?? body?.file_path ?? body?.filePath ?? 'unknown');
        let saveResult: { saved: boolean; path: string } = { saved: false, path: '' };
        try {
            saveResult = await saveIRToFile({
                projectId: id,
                projectName: project?.name || id,
                sourceFile,
                irVersion: String(body?.ir_version ?? body?.irVersion ?? 'unknown'),
                ir: rawCandidate,
            });
        } catch (saveError) {
            request.log.warn(saveError, 'Failed to persist IR output file');
        }
        const metadata = {
            sizeBytes: rawText.length,
            tooLarge: rawText.length > 2 * 1024 * 1024,
            truncated: false,
        };

        return reply.code(200).send({
            id: resolvedJobId,
            projectId: id,
            rawIr: rawCandidate,
            metadata,
            saved: saveResult.saved,
            path: saveResult.path,
        });
    } catch (error: any) {
        request.log.error(error, 'Failed to fetch raw analysis IR');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.post('/api/projects/:id/migrations/start', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const body = (request.body || {}) as Record<string, unknown>;
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/migrations`, {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify(body),
        });
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to start migration from analysis');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.get('/api/projects/:id/migrations/latest', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/migrations/latest`);
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to fetch migration status from execution plane');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.get('/api/projects/:id/workflow', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/workflow`);
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to fetch migration workflow');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.post('/api/projects/:id/workflow/approve', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/workflow/approve`, {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify(request.body || {}),
        });
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to approve migration workflow');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.post('/api/projects/:id/workflow/reject', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const { stage } = (request.query || {}) as { stage?: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/workflow/reject?stage=${encodeURIComponent(stage || 'ir')}`, {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify(request.body || {}),
        });
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to reject migration workflow');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.post('/api/projects/:id/workflow/request-reanalysis', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/workflow/request-reanalysis`, {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify(request.body || {}),
        });
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to request re-analysis');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.post('/api/projects/:id/workflow/generate-mapping', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/workflow/generate-mapping`, {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify(request.body || {}),
        });
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to generate mapping review');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.post('/api/projects/:id/workflow/generate-architecture', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    try {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/workflow/generate-architecture`, {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify(request.body || {}),
        });
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to generate architecture review');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

app.get('/api/projects/:id/events', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    
    // Switch from simple polling GET to SSE
    reply.raw.setHeader('Content-Type', 'text/event-stream');
    reply.raw.setHeader('Cache-Control', 'no-cache');
    reply.raw.setHeader('Connection', 'keep-alive');
    
    // Send initial connection establish
    reply.raw.write(': connected\n\n');

    let since = 0;
    const interval = setInterval(async () => {
        try {
            const upstream = await proxyExecutionPlane(`/internal/projects/${id}/events?since=${since}`);
            const data = typeof upstream.body === 'string' ? JSON.parse(upstream.body) : upstream.body;
            
            if (data.events && data.events.length > 0) {
                for (const event of data.events) {
                    reply.raw.write(`data: ${JSON.stringify(event)}\n\n`);
                }
                since = data.latestSeq || since;
            }
        } catch (error) {
            request.log.error(error, 'SSE proxy error to execution plane');
        }
    }, 1000);

    // Stop polling upstream when client disconnects
    request.raw.on('close', () => {
        clearInterval(interval);
    });
});

app.get('/api/internal/migration-analytics', async (request: FastifyRequest, reply: FastifyReply) => {
    try {
        const secret = request.headers['x-internal-secret'];
        const upstream = await proxyExecutionPlane('/internal/migration-analytics', {
            headers: secret ? { 'x-internal-secret': String(secret) } : undefined
        });
        return reply.code(upstream.status).send(upstream.body);
    } catch (error: any) {
        request.log.error(error, 'Failed to fetch migration analytics');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    }
});

function isMaskedApiKey(apiKey: string | undefined): boolean {
    if (!apiKey?.trim()) return true;
    return apiKey.includes('••••') || apiKey.includes('****');
}

/** Never forward masked UI keys to Python — backend reads env / IAM role instead. */
function resolveBackendProviderConfig(
    activeProvider: string,
    incoming?: { apiKey?: string; model?: string; enabled?: boolean },
) {
    const model =
        incoming?.model ||
        process.env.BEDROCK_MODEL_ID ||
        'us.amazon.nova-lite-v1:0';

    if (activeProvider === 'nova') {
        const apiKey = incoming?.apiKey?.trim() || '';
        if (!isMaskedApiKey(apiKey) && apiKey) {
            return { enabled: true, apiKey, model };
        }
        return {
            enabled: process.env.LLM_ENABLED !== 'false',
            model,
        };
    }

    return {
        enabled: incoming?.enabled ?? false,
        apiKey: isMaskedApiKey(incoming?.apiKey) ? '' : (incoming?.apiKey || ''),
        model: incoming?.model || model,
    };
}

app.post('/api/projects/:id/migrate', async (request: FastifyRequest, _reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const { fileIds, config, migrationId, userId: bodyUserId, llmSettings } = request.body as {
        fileIds: string[];
        config: MigrationConfig;
        migrationId?: string;
        userId?: string;
        llmSettings?: {
            activeProvider?: string;
            providers?: Record<string, { apiKey?: string; model?: string; enabled?: boolean }>;
        };
    };

    const generateId = (len = 10) => {
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        return Array.from({length: len}, () => chars[Math.floor(Math.random() * chars.length)]).join('');
    };

    const runId = migrationId || generateId();
    emittedTerminalBatchIds.delete(runId);

    // P0-B: Extract userId from server-side sources first (header injected by auth middleware
    // or API gateway) to prevent client impersonation of arbitrary user IDs.
    // Priority: X-User-Id header > Authorization JWT sub > body field (dev-only fallback).
    const headerUserId = (request.headers['x-user-id'] as string | undefined)?.trim();
    const authHeader = (request.headers['authorization'] as string | undefined) || '';
    const jwtPayloadUserId = _extractSubFromJwt(authHeader);
    const userId = headerUserId || jwtPayloadUserId || bodyUserId || 'default-user';

    if (!headerUserId && !jwtPayloadUserId) {
        // Loud warning so this is visible in production log aggregators.
        // In a fully-authenticated deployment this path should never be reached.
        request.log.warn(
            { bodyUserId, ip: request.ip, projectId: id },
            'P0-SECURITY: userId resolved from request body — no trusted header/JWT present. ' +
            'Configure auth middleware to inject X-User-Id or Authorization header.'
        );
    }

    // CONCURRENCY LOCK: Check if this user already has a truly RUNNING migration.
    // Use per‑user migration guard to claim this project.
    if (!userMigrationGuard.claim(userId, id)) {
        return _reply.code(409).send({
            success: false,
            error: 'CONCURRENCY_LOCK',
            message: 'User already has an active migration for another project.',
            activeProjectId: userMigrationGuard.getActiveProject(userId),
        });
    }

    // Existing check for any running batch for this project.
    const activeUserBatch = await prisma.migrationBatch.findFirst({
        where: {
            projectId: id,
            status: 'running'  // Only block on genuinely running batches
        }
    });

    if (activeUserBatch && activeUserBatch.id !== runId) {
        // Double-check: verify there are actually in-progress files for this batch.
        // If no files are in-progress, the 'running' status is stale — auto-fix it.
        const inProgressCount = await prisma.projectFile.count({
            where: { projectId: id, status: 'in-progress' }
        });

        if (inProgressCount === 0) {
            // Stale lock: batch says 'running' but no files are in-progress. Auto-release.
            await prisma.migrationBatch.update({
                where: { id: activeUserBatch.id },
                data: { status: 'completed', completedAt: new Date() }
            }).catch(() => {});
            // Allow migration to proceed
        } else {
            return _reply.code(409).send({
                success: false,
                error: 'CONCURRENCY_LOCK',
                message: 'A migration is currently running for this project. Please wait for it to finish or stop it before starting a new one.',
                activeMigrationId: activeUserBatch.id
            });
        }
    }

    const activeProvider = llmSettings?.activeProvider || process.env.ACTIVE_LLM_PROVIDER || 'openai';
    const providerConfig = resolveBackendProviderConfig(
        activeProvider,
        llmSettings?.providers?.[activeProvider],
    );

    const proj = await prisma.project.findUnique({ where: { id } }).catch(() => null);
    const resolvedPlatform = (config as any)?.targetPlatform || (proj as any)?.targetPlatform || (
        config?.migrationType?.includes('cpi') || config?.migrationType?.includes('sap') ||
        config?.targetRuntime === 'groovy' || config?.targetRuntime === 'cpi-xml' || config?.targetRuntime === 'xslt'
            ? 'sap-integration-suite'
            : 'aws'
    );

    const upstream = await proxyExecutionPlane(`/internal/projects/${id}/backend-migrations`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            fileIds,
            migrationId: runId,
            targetPlatform: resolvedPlatform,
            migrationType: config.migrationType,
            targetRuntime: config.targetRuntime,
            userId,
            activeProvider,
            providerConfig,
            instructions: config.instructions || '',
        }),
    });

    if (upstream.status >= 400) {
        userMigrationGuard.release(userId);
        return _reply.code(upstream.status).send(upstream.body);
    }

    startBackendEventMirror(id, runId);
    return upstream.body;
});

app.get('/api/projects/:id/files', async (request: FastifyRequest, _reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const { page, take } = (request.query || {}) as { page?: string; take?: string };
    const pageNum = Math.max(0, Number(page ?? '0') || 0);
    const takeNum = Math.min(200, Math.max(1, Number(take ?? '50') || 50));
    try {
        const files = await prisma.projectFile.findMany({
            where: { projectId: id },
            skip: pageNum * takeNum,
            take: takeNum,
            orderBy: { path: 'asc' },
            select: {
                id: true,
                projectId: true,
                name: true,
                path: true,
                status: true,
                type: true,
                language: true,
                activeMigrationId: true,
                migratedContent: true,
                migrations: {
                    orderBy: { createdAt: 'desc' },
                    take: 5,
                    select: {
                        id: true,
                        provider: true,
                        model: true,
                        content: true,
                        code: true,
                        tokens: true,
                        createdAt: true,
                    },
                },
            },
        });
        return { success: true, files };
    } catch (error) {
        console.error('Failed to fetch project files:', error);
        return { success: false, error: 'Failed to fetch project files' };
    }
});

app.post('/api/projects/:id/stop', async (request: FastifyRequest, _reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const { migrationId } = (request.body as { migrationId?: string }) || {};

    if (migrationId) {
        const upstream = await proxyExecutionPlane(`/internal/projects/${id}/backend-migrations/stop`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ migrationId }),
        });
        if (upstream.status < 400) {
            const key = `${id}:${migrationId}`;
            const timer = backendEventMirrors.get(key);
            if (timer) {
                clearInterval(timer);
                backendEventMirrors.delete(key);
            }
            const batch = await prisma.migrationBatch.findUnique({ where: { id: migrationId } });
            if (batch?.triggeredById) {
                userMigrationGuard.release(batch.triggeredById);
            }
            io.to(`project:${id}`).emit('migration:stopped', { projectId: id, migrationId });
            return { success: true, stoppedCount: 0 };
        }
    }

    return _reply.code(400).send({
        success: false,
        message: 'migrationId is required to stop a Python backend migration',
    });
});

app.post('/api/projects/:id/resume', async (request: FastifyRequest, _reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const { migrationId, userId: bodyUserId } = request.body as {
        migrationId: string;
        userId?: string;
    };

    // Find the batch and its associated files from the fileResults
    const batch = await prisma.migrationBatch.findUnique({
        where: { id: migrationId },
    });

    if (!batch) {
        return _reply.code(404).send({ success: false, message: 'Batch not found' });
    }

    const userId = bodyUserId || batch.triggeredById || 'default-user';
    emittedTerminalBatchIds.delete(migrationId);
    const project = await prisma.project.findUnique({ where: { id } });
    const upstream = await proxyExecutionPlane(`/internal/projects/${id}/backend-migrations/resume`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            migrationId,
            migrationType: project?.migrationType || 'mule4-lambda',
            targetRuntime: project?.targetRuntime || 'python',
            targetPlatform: (project as any)?.targetPlatform || 'aws',
            userId,
        }),
    });
    if (upstream.status >= 400) {
        return _reply.code(upstream.status).send(upstream.body);
    }
    startBackendEventMirror(id, migrationId);
    return upstream.body;
});

app.post('/api/projects/:id/retry-file', async (request: FastifyRequest, _reply: FastifyReply) => {
    const { id: projectId } = request.params as { id: string };
    const { fileId, migrationId, config, userId: bodyUserId } = request.body as {
        fileId: string;
        migrationId: string;
        config: MigrationConfig;
        userId?: string;
    };

    // FIX P1-2: use the userId supplied by the authenticated frontend.
    const userId = bodyUserId || 'default-user';

    // CONCURRENCY LOCK: Block only on a genuinely RUNNING batch for this project.
    // 'partial' is NOT a running state; it means some files finished and others failed.
    const activeUserBatch = await prisma.migrationBatch.findFirst({
        where: {
            projectId,
            status: 'running'
        }
    });

    if (activeUserBatch && activeUserBatch.id !== migrationId) {
        // Verify there are actually in-progress files; if not, the lock is stale.
        const inProgressCount = await prisma.projectFile.count({
            where: { projectId, status: 'in-progress' }
        });

        if (inProgressCount === 0) {
            // Stale lock — auto-heal it
            await prisma.migrationBatch.update({
                where: { id: activeUserBatch.id },
                data: { status: 'completed', completedAt: new Date() }
            }).catch(() => {});
        } else {
            return _reply.code(409).send({
                success: false,
                error: 'CONCURRENCY_LOCK',
                message: 'A migration is currently running. Please wait until it completes or stop it before retrying individual files.',
                activeMigrationId: activeUserBatch.id
            });
        }
    }

    const upstream = await proxyExecutionPlane(`/internal/projects/${projectId}/backend-migrations/retry-file`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            fileId,
            migrationId,
            migrationType: config.migrationType,
            targetRuntime: config.targetRuntime,
            targetPlatform: (config as any)?.targetPlatform || 'aws',
            userId,
        }),
    });

    if (upstream.status >= 400) {
        return _reply.code(upstream.status).send(upstream.body);
    }
    startBackendEventMirror(projectId, migrationId);
    return upstream.body;
});

app.get('/api/projects/:id/active-batch', async (request: FastifyRequest, _reply: FastifyReply) => {
    const { id: projectId } = request.params as { id: string };

    try {
        // Prefer the latest running batch record — files may still be 'pending'
        // before the worker marks the first file 'in-progress'.
        const runningBatch = await prisma.migrationBatch.findFirst({
            where: { projectId, status: 'running' },
            orderBy: { startedAt: 'desc' },
        });

        if (runningBatch) {
            const processed = runningBatch.completedFiles + runningBatch.failedFiles;
            if (processed < runningBatch.totalFiles) {
                return { success: true, batch: runningBatch };
            }

            // All files accounted for but batch still marked running — heal it.
            const healed = await prisma.migrationBatch.update({
                where: { id: runningBatch.id },
                data: { status: 'completed', completedAt: new Date() },
            }).catch(() => runningBatch);
            return { success: true, batch: healed };
        }

        // Fallback: in-progress files without a running batch row (legacy / crash recovery).
        const inProgressFile = await prisma.projectFile.findFirst({
            where: { projectId, status: 'in-progress' },
            select: { activeMigrationId: true },
        });

        if (!inProgressFile) {
            return { success: true, batch: null };
        }

        const activeBatch = inProgressFile.activeMigrationId
            ? await prisma.migrationBatch.findUnique({
                where: { id: inProgressFile.activeMigrationId },
              })
            : null;

        return { success: true, batch: activeBatch };
    } catch (error) {
        console.error('Failed to fetch active batch:', error);
        return { success: false, error: 'Failed to fetch active batch' };
    }
});

/* ── Export pipeline (Phase 1+2) ────────────────────────────────────────── */

type ExportFormat = 'zip' | 'sam' | 'cloudformation' | 'terraform' | 'cpi-package' | 'cpi-iflow' | 'cpi-tenant-push';
type ExportRuntime = 'python' | 'nodejs' | 'java' | 'groovy' | 'cpi-xml' | 'xslt';

const EXPORT_FORMATS: ExportFormat[] = ['zip', 'sam', 'cloudformation', 'terraform', 'cpi-package', 'cpi-iflow', 'cpi-tenant-push'];
const EXPORT_PASSTHROUGH = [
    'content-disposition',
    'x-export-format',
    'x-export-file-count',
    'x-export-sha256',
    'x-export-pipeline',
    'x-export-components-total',
    'x-export-components-covered',
    'x-export-archetype',
    'x-export-archetype-confidence',
    'x-export-complexity',
];

function normaliseExportBody(body: unknown) {
    const raw = (body || {}) as Record<string, unknown>;
    const format = ((raw.format as string | undefined) ?? 'zip').toLowerCase();
    const targetRuntime = ((raw.targetRuntime as string | undefined) ?? 'python').toLowerCase();
    const projectNameHint = (raw.projectNameHint as string | undefined) ?? '';
    const pipeline = ((raw.pipeline as string | undefined) ?? 'v3').toLowerCase();
    const infraMode = ((raw.infraMode as string | undefined) ?? '').toLowerCase();
    const region = ((raw.region as string | undefined) ?? 'us-east-1');
    if (!EXPORT_FORMATS.includes(format as ExportFormat)) {
        throw new Error(`Unsupported export format: ${format}`);
    }
    return {
        format: format as ExportFormat,
        targetRuntime: targetRuntime as ExportRuntime,
        projectNameHint,
        pipeline,
        infraMode,
        region,
    };
}

app.get('/api/projects/:id/export/preview', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    const { format, targetRuntime, pipeline, infraMode, region, targetPlatform } = (request.query || {}) as {
        format?: string;
        targetRuntime?: string;
        pipeline?: string;
        infraMode?: string;
        region?: string;
        targetPlatform?: string;
    };
    const proj = await prisma.project.findUnique({ where: { id } }).catch(() => null);
    const resolvedPlatform = targetPlatform || (proj as any)?.targetPlatform || (
        proj?.migrationType?.includes('cpi') || proj?.migrationType?.includes('sap') ||
        proj?.targetRuntime === 'groovy' || proj?.targetRuntime === 'cpi-xml' || proj?.targetRuntime === 'xslt' ||
        targetRuntime === 'groovy' || targetRuntime === 'cpi-xml' ||
        format === 'cpi-package' || format === 'cpi-tenant-push'
            ? 'sap-integration-suite'
            : 'aws'
    );
    const fmt = (format || 'zip').toLowerCase();
    const rt = (targetRuntime || (resolvedPlatform === 'sap-integration-suite' ? 'groovy' : 'python')).toLowerCase();
    const pl = (pipeline || 'v3').toLowerCase();
    const im = (infraMode || '').toLowerCase();
    const rg = region || 'us-east-1';
    if (!EXPORT_FORMATS.includes(fmt as ExportFormat)) {
        return reply.code(400).send({ error: `Unsupported export format: ${fmt}` });
    }
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 120000);
    try {
        const url =
            `${fastApiUrl}/internal/projects/${encodeURIComponent(id)}/export/preview` +
            `?format=${encodeURIComponent(fmt)}` +
            `&target_runtime=${encodeURIComponent(rt)}` +
            `&target_platform=${encodeURIComponent(resolvedPlatform)}` +
            `&pipeline=${encodeURIComponent(pl)}` +
            `&infra_mode=${encodeURIComponent(im)}` +
            `&region=${encodeURIComponent(rg)}`;
        const upstream = await fetch(url, { signal: controller.signal });
        const payload = await upstream.json().catch(() => ({}));
        return reply.code(upstream.status).send(payload);
    } catch (error: any) {
        if (error.name === 'AbortError') {
            request.log.error('Export preview request timed out after 120 seconds');
            return reply.code(504).send({ error: 'Export preview timed out after 120 seconds' });
        }
        request.log.error(error, 'Failed to preview export');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    } finally {
        clearTimeout(timeoutId);
    }
});

app.post('/api/projects/:id/export', async (request: FastifyRequest, reply: FastifyReply) => {
    const { id } = request.params as { id: string };
    let body;
    try {
        body = normaliseExportBody(request.body);
    } catch (err: any) {
        return reply.code(400).send({ error: err?.message ?? 'Invalid export request' });
    }

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 120000);

    try {
        const proj = await prisma.project.findUnique({ where: { id } }).catch(() => null);
        const resolvedPlatform = (body as any)?.targetPlatform || (proj as any)?.targetPlatform || (
            proj?.migrationType?.includes('cpi') || proj?.migrationType?.includes('sap') ||
            proj?.targetRuntime === 'groovy' || proj?.targetRuntime === 'cpi-xml' || proj?.targetRuntime === 'xslt' ||
            (body.targetRuntime as string) === 'groovy' || (body.targetRuntime as string) === 'cpi-xml' ||
            (body.format as string) === 'cpi-package' || (body.format as string) === 'cpi-tenant-push'
                ? 'sap-integration-suite'
                : 'aws'
        );

        const upstream = await fetch(
            `${fastApiUrl}/internal/projects/${encodeURIComponent(id)}/export`,
            {
                method: 'POST',
                headers: { 'content-type': 'application/json' },
                body: JSON.stringify({
                    format: body.format,
                    targetRuntime: body.targetRuntime || (resolvedPlatform === 'sap-integration-suite' ? 'groovy' : 'python'),
                    targetPlatform: resolvedPlatform,
                    projectNameHint: body.projectNameHint,
                    pipeline: body.pipeline,
                    infraMode: body.infraMode,
                    region: body.region,
                }),
                signal: controller.signal,
            },
        );

        if (!upstream.ok) {
            const text = await upstream.text().catch(() => '');
            return reply
                .code(upstream.status)
                .header('content-type', upstream.headers.get('content-type') || 'application/json')
                .send(text || JSON.stringify({ error: `Export failed (${upstream.status})` }));
        }

        for (const key of EXPORT_PASSTHROUGH) {
            const v = upstream.headers.get(key);
            if (v) reply.header(key, v);
        }
        reply.header('content-type', upstream.headers.get('content-type') || 'application/zip');

        if (!upstream.body) {
            return reply.code(500).send({ error: 'No response body received from execution plane' });
        }

        return reply.send(Readable.fromWeb(upstream.body as any));
    } catch (error: any) {
        if (error.name === 'AbortError') {
            request.log.error('Export download request timed out after 120 seconds');
            return reply.code(504).send({ error: 'Export execution plane timed out after 120 seconds' });
        }
        request.log.error(error, 'Failed to build export');
        return reply.code(502).send({ error: 'Failed to reach execution plane', detail: error?.message });
    } finally {
        clearTimeout(timeoutId);
    }
});

// Process-level safety net so a single rogue async callback (socket.io
// handler, backend event mirror, prisma query, etc.) cannot silently kill
// the dev server. Logs stack + keeps the process alive so the failure mode
// is observable in the terminal instead of a mysterious exit_code=1.
process.on('unhandledRejection', (reason: unknown) => {
    const err = reason instanceof Error ? reason : new Error(String(reason));
    app.log.error({ err, where: 'unhandledRejection' }, 'unhandledRejection (kept alive)');
    console.error('[unhandledRejection]', err.stack || err.message);
});

process.on('uncaughtException', (err: Error) => {
    app.log.error({ err, where: 'uncaughtException' }, 'uncaughtException (kept alive)');
    console.error('[uncaughtException]', err.stack || err.message);
});

const start = async () => {
    try {
        console.log('Running startup cleanup...');
        const inProgressFiles = await prisma.projectFile.findMany({
            where: { status: 'in-progress' }
        });
        
        if (inProgressFiles.length > 0) {
            console.log(`Cleaning up ${inProgressFiles.length} orphaned files...`);
            await prisma.projectFile.updateMany({
                where: { id: { in: inProgressFiles.map(f => f.id) } },
                data: { status: 'failed', activeMigrationId: null }
            });
        }
        
        const runningBatches = await prisma.migrationBatch.findMany({
            where: { status: 'running' }
        });
        
        if (runningBatches.length > 0) {
            console.log(`Cleaning up ${runningBatches.length} stale batches...`);
            await prisma.migrationBatch.updateMany({
                where: { id: { in: runningBatches.map(b => b.id) } },
                data: { status: 'failed', completedAt: new Date() }
            });
        }

        const port = Number(process.env.FASTIFY_PORT || process.env.PORT) || 3001;
        await app.listen({ port, host: '127.0.0.1' });
        console.log(`Fastify server running on http://127.0.0.1:${port}`);
    } catch (err) {
        app.log.error(err);
        process.exit(1);
    }
};

start();

// ─── P0-B: JWT sub extraction helper ──────────────────────────────────────────
// Extracts the `sub` claim from a Bearer JWT for server-side userId resolution.
// Cryptographically verifies the token using JWT_SECRET if present in env, enforcing
// stateless security (RC-7).
function _extractSubFromJwt(authHeader: string): string | undefined {
    if (!authHeader.startsWith('Bearer ')) return undefined;
    const token = authHeader.slice(7).trim();
    const secret = process.env.JWT_SECRET || process.env.NEXTAUTH_SECRET;
    
    try {
        if (secret) {
            // Secure mode: cryptographically verify token
            const payload = jwt.verify(token, secret) as Record<string, unknown>;
            const sub = payload['sub'] ?? payload['userId'] ?? payload['user_id'];
            return typeof sub === 'string' && sub.trim() ? sub.trim() : undefined;
        } else {
            // Fallback (dev-only): just decode payload without signature check
            const parts = token.split('.');
            if (parts.length !== 3) return undefined;
            const payloadJson = Buffer.from(parts[1], 'base64url').toString('utf8');
            const payload = JSON.parse(payloadJson) as Record<string, unknown>;
            const sub = payload['sub'] ?? payload['userId'] ?? payload['user_id'];
            return typeof sub === 'string' && sub.trim() ? sub.trim() : undefined;
        }
    } catch (err) {
        return undefined; // Invalid signature or expired
    }
}

