import { Queue, Worker, Job } from 'bullmq';
import type { ConnectionOptions } from 'bullmq';
import { MigrationConfig, LLMSettings } from '../types';
import { PrismaClient } from '@prisma/client';
import { jobEvents } from './events';
import { estimateTokens } from '../utils/tokens';
import { generatePhysicalProject } from '../server/project-generator';
import { retrieveMigrationKnowledge } from '../server/knowledge-base-client';
import { generateWithBackendMigrationEngine } from '../server/backend-migration-client';

const prisma = new PrismaClient();
const stopRequestedMigrationIds = new Set<string>();

/* ─── Base64 codec (must match db-store.ts) ─── */
const b64enc = (s: string): string =>
    'b64:' + Buffer.from(s ?? '', 'utf8').toString('base64');

const b64dec = (s: string): string => {
    if (typeof s === 'string' && s.startsWith('b64:')) {
        try { return Buffer.from(s.slice(4), 'base64').toString('utf8'); }
        catch { return s; }
    }
    return s;
};

/** Extract the primary code block from a Markdown migration report. */
function extractPrimaryCode(content: string): string {
    const startMarker = '[PRIMARY_CODE_BLOCK]';
    const endMarker = '[/PRIMARY_CODE_BLOCK]';
    const startIdx = content.indexOf(startMarker);
    const endIdx = content.indexOf(endMarker);

    if (startIdx !== -1 && endIdx !== -1 && endIdx > startIdx) {
        const block = content.slice(startIdx + startMarker.length, endIdx);
        const m = block.match(/```(?:\w+)?\n([\s\S]*?)```/);
        if (m) return m[1].trim();
        return block.trim(); // Fallback if no fence but marker present
    }

    // Legacy fallback extraction
    const blocks = Array.from(content.matchAll(/```(?:\w+)?\n([\s\S]*?)```/g), x => x[1].trim());
    if (!blocks.length) return '';
    return blocks.reduce((a, b) => (a.length > b.length ? a : b));
}

function getRedisConnection(): ConnectionOptions {
    const url = process.env.REDIS_URL || 'redis://localhost:6379';
    try {
        const parsed = new URL(url);
        return {
            host: parsed.hostname || 'localhost',
            port: parsed.port ? Number(parsed.port) : 6379,
            password: parsed.password || undefined,
            username: parsed.username || undefined,
            maxRetriesPerRequest: null,
        };
    } catch {
        return { host: 'localhost', port: 6379, maxRetriesPerRequest: null };
    }
}

const connection = getRedisConnection();

export const migrationQueue = new Queue('migration-queue', { connection });

export function requestMigrationStop(migrationId?: string | null): void {
    if (migrationId) {
        stopRequestedMigrationIds.add(migrationId);
    }
}

export function clearMigrationStopRequest(migrationId?: string | null): void {
    if (migrationId) {
        stopRequestedMigrationIds.delete(migrationId);
    }
}

function isMigrationStopRequested(migrationId?: string | null): boolean {
    return !!migrationId && stopRequestedMigrationIds.has(migrationId);
}

export const migrationWorker = new Worker(
    'migration-queue',
    async (job: Job) => {
        const { fileId, config, llmSettings } = job.data as {
            fileId: string;
            config: MigrationConfig;
            llmSettings: LLMSettings;
        };

        // Fetch file content from Prisma
        const file = await prisma.projectFile.findUnique({
            where: { id: fileId }
        });

        if (!file) throw new Error(`File ${fileId} not found`);

        const sourceContent = b64dec(file.content);

        // Fetch project structure for context
        const projectFiles = await prisma.projectFile.findMany({
            where: { projectId: config.projectId },
            select: { path: true, name: true, type: true },
            orderBy: { path: 'asc' }
        });
        const projectStructure = projectFiles
            .map(f => `${f.type === 'folder' ? '[DIR] ' : '      '}${f.path}`)
            .join('\n');

        let migrationRecord: Awaited<ReturnType<typeof prisma.migrationRecord.create>> | null = null;
        let migratedContent = '';
        const sessionId = job.data.migrationId || `mig-batch-${Date.now()}`;
        let providerName = 'unknown';
        let providerModel = 'unknown';
        let systemPrompt = '';
        let userPrompt = '';
        let inputTokens = 0;
        let outputTokens = 0;
        let tokens = 0;

        try {
            console.log(`[Worker] Starting transformation for file: ${file.path}`);

            if (isMigrationStopRequested(sessionId)) {
                throw new Error('MIGRATION_STOP_REQUESTED');
            }

            // Explicitly mark as in-progress
            await prisma.projectFile.update({
                where: { id: fileId },
                data: { status: 'in-progress', activeMigrationId: job.data.migrationId }
            });

            await job.log('MILESTONE: CONTEXT_LOADED');

            const backendResult = await generateWithBackendMigrationEngine({
                fileName: file.name,
                filePath: file.path,
                sourceContent,
                migrationType: config.migrationType,
                targetRuntime: config.targetRuntime,
                projectStructure,
            }, config);

            if (backendResult) {
                providerName = backendResult.provider;
                providerModel = backendResult.model;
                systemPrompt = backendResult.systemPrompt;
                userPrompt = backendResult.userPrompt;
                inputTokens = backendResult.usage?.inputTokens ?? 0;
                outputTokens = backendResult.usage?.outputTokens ?? 0;
                migratedContent = backendResult.content;

                migrationRecord = await prisma.migrationRecord.create({
                    data: {
                        fileId,
                        provider: providerName as any,
                        model: providerModel,
                        content: '',
                        systemPrompt: b64enc(systemPrompt),
                        userPrompt: b64enc(userPrompt),
                        tokens: 0,
                    }
                });

                jobEvents.emit('token', {
                    jobId: job.id,
                    projectId: config.projectId,
                    token: migratedContent
                });
                await job.log(JSON.stringify({ type: 'token', token: migratedContent }));
                await job.updateProgress(95);
            } else {
                throw new Error("Backend migration engine failed to return a result.");
            }

            await job.log('MILESTONE: CODE_EXTRACTED');
            const migratedCode = extractPrimaryCode(migratedContent);
            tokens = inputTokens || outputTokens ? inputTokens + outputTokens : estimateTokens(migratedContent);
            // Analytics is now tracked in Python backend DB
            let batchCompleted = false;
            let batchStatus: 'running' | 'completed' | 'partial' = 'running';

            // Final updates to file and migration record
            await prisma.$transaction(async (tx) => {
                await tx.projectFile.update({
                    where: { id: fileId },
                    data: {
                        status: 'completed',
                        migratedContent: b64enc(migratedContent),
                        migratedCode: migratedCode ? b64enc(migratedCode) : null,
                        activeMigrationId: sessionId,
                    },
                });

                if (migrationRecord) {
                    await tx.migrationRecord.update({
                        where: { id: migrationRecord.id },
                        data: {
                            rawResponse: b64enc(migratedContent),
                            content: b64enc(migratedContent),
                            tokens: tokens,
                        }
                    });
                }

                const batch = await tx.migrationBatch.findUnique({ where: { id: sessionId } });
                if (batch) {
                    const currentResults = Array.isArray(batch.fileResults) ? batch.fileResults : [];
                    const newResult = {
                        fileId,
                        fileName: job.data.fileName,
                        filePath: job.data.filePath,
                        status: 'completed' as const
                    };

                    await tx.migrationBatch.update({
                        where: { id: sessionId },
                        data: {
                            completedFiles: { increment: 1 },
                            totalTokens: { increment: tokens },
                            fileResults: [...currentResults, newResult],
                            status: (batch.completedFiles + batch.failedFiles + 1) >= batch.totalFiles ? 'completed' : 'running',
                            completedAt: (batch.completedFiles + batch.failedFiles + 1) >= batch.totalFiles ? new Date() : batch.completedAt
                        }
                    });
                    batchCompleted = (batch.completedFiles + batch.failedFiles + 1) >= batch.totalFiles;
                    batchStatus = batchCompleted ? 'completed' : 'running';
                }
            });
            if (batchCompleted) {
                clearMigrationStopRequest(sessionId);
                try {
                    await generatePhysicalProject(config.projectId ?? file.projectId);
                } catch (err) {
                    console.error('[Worker] Failed to generate physical project:', err);
                }
            }

            await job.log('MILESTONE: PUBLISHED');

            return {
                status: 'completed',
                migratedContent,
                migratedCode,
                tokens,
                duration: Date.now() - (job.timestamp || Date.now()),
                migrationId: sessionId,
                batchCompleted,
                batchStatus,
            };

        } catch (error: unknown) {
            console.error(`Migration job failed for file ${fileId}:`, error);
            const errorMessage = error instanceof Error ? error.message : 'Unknown error';
            const isStopRequested = errorMessage === 'MIGRATION_STOP_REQUESTED';

            // Update individual file status to failed
            await prisma.projectFile.update({
                where: { id: fileId },
                data: { status: isStopRequested ? 'pending' : 'failed' }
            }).catch(() => null);

            // Update record if it exists even on failure
            if (migrationRecord) {
                await prisma.migrationRecord.update({
                    where: { id: migrationRecord.id },
                    data: {
                        rawResponse: b64enc(migratedContent),
                        content: b64enc(migratedContent),
                        tokens: estimateTokens(migratedContent),
                    }
                }).catch(() => null);
            }

            // Update Batch statistics for failure
            if (sessionId) {
                const batch = await prisma.migrationBatch.findUnique({ where: { id: sessionId } });
                if (batch) {
                    const currentResults = Array.isArray(batch.fileResults) ? batch.fileResults : [];
                    const newResult = {
                        fileId,
                        fileName: job.data.fileName,
                        filePath: job.data.filePath,
                        status: isStopRequested ? 'stopped' as const : 'failed' as const,
                        error: errorMessage
                    };

                    const updatedBatch = await prisma.migrationBatch.update({
                        where: { id: sessionId },
                        data: {
                            failedFiles: isStopRequested ? batch.failedFiles : { increment: 1 },
                            fileResults: [...currentResults, newResult],
                            status: isStopRequested
                                ? 'stopped'
                                : ((batch.completedFiles + batch.failedFiles + 1) >= batch.totalFiles ? 'partial' : 'running'),
                            completedAt: isStopRequested ? new Date() : batch.completedAt
                        }
                    }).catch(() => null);

                    if (!isStopRequested && updatedBatch && updatedBatch.completedFiles + updatedBatch.failedFiles >= updatedBatch.totalFiles) {
                        await prisma.migrationBatch.update({
                            where: { id: sessionId },
                            data: { status: 'partial', completedAt: new Date() }
                        });
                    }

                    if (isStopRequested) {
                        clearMigrationStopRequest(sessionId);
                    }
                }
            }
            throw error;
        }
    },
    {
        connection,
        concurrency: 1, // Enforce one-by-one processing
        removeOnComplete: { count: 1000 },
        removeOnFail: { count: 5000 },
        settings: {
            backoffStrategy: (attemptsMade: number) => {
                return Math.pow(2, attemptsMade) * 1000;
            }
        }
    }
);

migrationWorker.on('completed', (job) => {
    console.log(`[Worker] Job ${job.id} completed successfully`);
});

migrationWorker.on('failed', (job, err) => {
    console.error(`[Worker] Job ${job?.id} failed: ${err.message}`);
});

migrationWorker.on('error', (err) => {
    console.error(`[Worker] Global Error:`, err);
});
