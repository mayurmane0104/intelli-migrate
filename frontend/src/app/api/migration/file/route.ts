import { NextRequest, NextResponse } from 'next/server';
import { sessionStore, llmSettingsStore, jobEngine } from '@/lib/store';
import { dbFileStore, dbLogStore } from '@/lib/db-store';
import type { FileStatus, MigrationLogLevel } from '@/lib/types';

export async function POST(req: NextRequest) {
    try {
        const { fileId } = await req.json();
        if (!fileId) return NextResponse.json({ error: 'Missing fileId' }, { status: 400 });

        const file = await dbFileStore.findById(fileId);
        if (!file || file.type === 'folder') {
            return NextResponse.json({ error: 'File not found or is a folder' }, { status: 404 });
        }

        const startTime = Date.now();

        // Resolve user LLM settings
        const sessionToken = req.cookies.get('ms_session')?.value;
        const userId = sessionToken ? sessionStore.getUserId(sessionToken) : undefined;
        const llmSettings = userId ? await llmSettingsStore.get(userId) : undefined;

        if (!llmSettings || !llmSettings.activeProvider) {
            return NextResponse.json({ error: 'No LLM settings configured.' }, { status: 400 });
        }

        const providerConfig = llmSettings.providers[llmSettings.activeProvider as keyof typeof llmSettings.providers];

        try {
            const fastApiUrl = (process.env.FASTAPI_URL || 'http://localhost:8000').replace(/\/$/, '');
            const backendResponse = await fetch(`${fastApiUrl}/internal/migration/stream-file`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    // ── IR enrichment hook ────────────────────────────────
                    // Pass the projectId so the FastAPI endpoint can query
                    // the latest completed analysis IR and slice it for
                    // this file before invoking the LLM.
                    projectId: file.projectId,
                    fileName: file.name,
                    filePath: file.path,
                    sourceContent: file.content,
                    migrationType: 'mule4-lambda',
                    targetRuntime: 'nodejs',
                    projectStructure: '',
                    activeProvider: llmSettings.activeProvider,
                    providerConfig: providerConfig,
                    instructions: '',
                }),
            });

            if (!backendResponse.ok) {
                const errText = await backendResponse.text();
                throw new Error(`Backend error (${backendResponse.status}): ${errText}`);
            }

            const reader = backendResponse.body?.getReader();
            if (!reader) throw new Error('No response body from backend');

            const decoder = new TextDecoder();
            let migratedContent = '';
            let buffer = '';

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                buffer += decoder.decode(value, { stream: true });
                const lines = buffer.split('\n');
                buffer = lines.pop() || '';

                for (const line of lines) {
                    if (line.startsWith('data: ')) {
                        const data = line.slice(6).trim();
                        if (data === '[DONE]') break;
                        try {
                            const parsed = JSON.parse(data);
                            const text = parsed?.contentBlockDelta?.delta?.text;
                            if (text) migratedContent += text;
                        } catch { /* skip */ }
                    }
                }
            }

            const duration = Date.now() - startTime;
            const migratedCode = jobEngine.extractPrimaryCode(migratedContent);

            await dbFileStore.update(fileId, {
                status: 'completed',
                migratedContent,
                migratedCode,
                activeMigrationId: `mig-${Date.now()}`,
            });

            const log = await dbLogStore.create({
                projectId: file.projectId,
                fileName: file.name,
                status: 'success',
                message: `✓ Migrated ${file.name} (${Math.round(duration)}ms)`,
                duration,
            });

            return NextResponse.json({ status: 'completed', migratedContent, log });
        } catch (err) {
            const duration = Date.now() - startTime;
            const errorMsg = err instanceof Error ? err.message : 'Unknown error';

            await dbFileStore.updateStatus(fileId, 'failed');

            const log = await dbLogStore.create({
                projectId: file.projectId,
                fileName: file.name,
                status: 'error',
                message: `✗ Failed to migrate ${file.name}: ${errorMsg}`,
                duration,
                stackTrace: err instanceof Error ? err.stack : undefined,
            });

            return NextResponse.json({ status: 'failed', migratedContent: '', log });
        }
    } catch {
        return NextResponse.json({ error: 'Internal error' }, { status: 500 });
    }
}
