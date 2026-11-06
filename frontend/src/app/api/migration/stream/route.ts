/**
 * SSE Streaming Migration Endpoint
 * GET /api/migration/stream?projectId=xxx&action=start
 *
 * Returns a text/event-stream response with real-time migration events.
 * Uses per-user LLM settings for provider selection.
 */
import { NextRequest } from 'next/server';
import { jobEngine, sessionStore, llmSettingsStore, userStore } from '@/lib/store';

export const dynamic = 'force-dynamic';

export async function GET(request: NextRequest) {
    const projectId = request.nextUrl.searchParams.get('projectId');
    const action = request.nextUrl.searchParams.get('action') || 'start';

    if (!projectId) {
        return new Response(JSON.stringify({ error: 'Missing projectId' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    if (action === 'status') {
        const session = jobEngine.getSession(projectId);
        return new Response(JSON.stringify({ session: session || null }), {
            headers: { 'Content-Type': 'application/json' },
        });
    }

    if (action === 'stop') {
        jobEngine.stopSession(projectId);
        return new Response(JSON.stringify({ stopped: true }), {
            headers: { 'Content-Type': 'application/json' },
        });
    }

    // action === 'start'
    // Guard: reject if a session is already actively running for this project
    const existingSession = jobEngine.getSession(projectId);
    if (existingSession?.status === 'running') {
        return new Response(JSON.stringify({ error: 'Migration already in progress for this project' }), {
            status: 409,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    const includeCompleted = request.nextUrl.searchParams.get('includeCompleted') === 'true';
    const session = await jobEngine.createSession(projectId, includeCompleted);

    if (session.totalJobs === 0) {
        return new Response(JSON.stringify({ error: 'No files to migrate' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' },
        });
    }

    // Get user's LLM settings from their session
    const sessionToken = request.cookies.get('ms_session')?.value;
    const userId = sessionToken ? sessionStore.getUserId(sessionToken) : undefined;

    // Resolve user info for triggeredBy metadata
    const resolvedUser = userId ? userStore.findById(userId) : undefined;
    const triggeredBy = resolvedUser
        ? { userId: resolvedUser.id, userName: resolvedUser.name }
        : { userId: 'system', userName: 'System' };

    // Note: The in-memory userMigrationGuard has been removed.
    // Concurrency locking is now handled centrally by the Fastify background processor and Prisma.

    const llmSettings = userId ? await llmSettingsStore.get(userId) : undefined;

    // We pass the llmSettings directly. The backend will load instructions.
    const stream = new TransformStream<Uint8Array, Uint8Array>();
    const writer = stream.writable.getWriter();

    // Send 2KB padding to beat Caddy/nginx/Next.js buffering layers immediately
    const encoder = new TextEncoder();
    writer.write(encoder.encode(': ' + ' '.repeat(2048) + '\n\n')).catch(() => {});

    jobEngine.processJobsWithStream(projectId, writer, llmSettings, triggeredBy).catch(async (err) => {
        const encoder = new TextEncoder();
        try {
            await writer.write(encoder.encode(
                `event: error\ndata: ${JSON.stringify({ error: err?.message || 'Internal error' })}\n\n`
            ));
            await writer.close();
        } catch { /* Writer may already be closed */ }
    });

    request.signal.addEventListener('abort', () => {
        // User disconnected early (e.g. closed browser)
        writer.close().catch(() => { });
    });

    return new Response(stream.readable, {
        headers: {
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache, no-transform',
            'Connection': 'keep-alive',
            'X-Accel-Buffering': 'no',
        },
    });
}
