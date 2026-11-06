import type { MigrationConfig } from '../types';

interface BackendMigrationInput {
    fileName: string;
    filePath: string;
    sourceContent: string;
    migrationType: string;
    targetRuntime: string;
    projectStructure: string;
}

interface BackendMigrationResult {
    content: string;
    systemPrompt: string;
    userPrompt: string;
    provider: string;
    model: string;
    usage?: {
        inputTokens?: number;
        outputTokens?: number;
    };
}

const fastApiBase = (process.env.FASTAPI_URL || 'http://localhost:8000').replace(/\/$/, '');

export function backendMigrationEnabled(): boolean {
    return process.env.BACKEND_MIGRATION_ENGINE !== 'false';
}

export async function generateWithBackendMigrationEngine(
    input: BackendMigrationInput,
    config: MigrationConfig,
): Promise<BackendMigrationResult | null> {
    if (!backendMigrationEnabled()) {
        return null;
    }

    try {
        const response = await fetch(`${fastApiBase}/internal/migration/generate-file`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                fileName: input.fileName,
                filePath: input.filePath,
                sourceContent: input.sourceContent,
                migrationType: input.migrationType || config.migrationType,
                targetRuntime: input.targetRuntime || config.targetRuntime,
                projectStructure: input.projectStructure,
                topK: Number(process.env.MIGRATION_KB_TOP_K || 8),
            }),
        });

        if (!response.ok) {
            const detail = await response.text().catch(() => '');
            console.warn(`[Backend Migration] Python engine returned ${response.status}: ${detail.slice(0, 500)}`);
            return null;
        }

        const payload = await response.json() as {
            success?: boolean;
            content?: string;
            systemPrompt?: string;
            userPrompt?: string;
            provider?: string;
            model?: string;
            usage?: BackendMigrationResult['usage'];
        };

        if (!payload.success || !payload.content) {
            console.warn('[Backend Migration] Python engine returned an empty migration result');
            return null;
        }

        return {
            content: payload.content,
            systemPrompt: payload.systemPrompt || '',
            userPrompt: payload.userPrompt || '',
            provider: payload.provider || 'python-backend',
            model: payload.model || 'unknown',
            usage: payload.usage,
        };
    } catch (error) {
        console.warn('[Backend Migration] Python engine unavailable, falling back to Node worker:', error);
        return null;
    }
}
