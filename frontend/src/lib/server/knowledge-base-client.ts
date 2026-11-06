interface KBMetadata {
    source?: string;
    kb_type?: string;
    component?: string;
    service?: string;
    category?: string;
    tags?: string[];
}

interface KBSearchResult {
    chunk_id: string;
    document_id: string;
    domain: string;
    score: number;
    text: string;
    metadata: KBMetadata;
}

interface KBSearchResponse {
    query: string;
    top_k: number;
    results: KBSearchResult[];
}

export interface MigrationKnowledgeInput {
    fileName: string;
    filePath: string;
    sourceContent: string;
    migrationType: string;
    targetRuntime: string;
    projectStructure?: string;
}

const DEFAULT_FASTAPI_URL = 'http://localhost:8000';
const MAX_QUERY_CHARS = 6000;
const MAX_CHUNK_CHARS = 1200;

function compactText(value: string, maxLength: number): string {
    const normalized = value.replace(/\s+/g, ' ').trim();
    return normalized.length > maxLength
        ? `${normalized.slice(0, maxLength)}...`
        : normalized;
}

function buildKnowledgeQuery(input: MigrationKnowledgeInput): string {
    return compactText(
        [
            `MuleSoft migration knowledge for ${input.fileName}`,
            `Path: ${input.filePath}`,
            `Migration type: ${input.migrationType}`,
            `Target runtime: ${input.targetRuntime}`,
            input.projectStructure ? `Project structure: ${input.projectStructure}` : '',
            `Source excerpt: ${input.sourceContent}`,
        ].filter(Boolean).join('\n'),
        MAX_QUERY_CHARS
    );
}

function formatResults(results: KBSearchResult[]): string {
    if (results.length === 0) {
        return '';
    }

    const formatted = results.map((result, index) => {
        const metadata = result.metadata || {};
        const labels = [
            metadata.kb_type || result.domain,
            metadata.component ? `component=${metadata.component}` : '',
            metadata.service ? `service=${metadata.service}` : '',
            metadata.source ? `source=${metadata.source}` : '',
        ].filter(Boolean).join('; ');

        return [
            `#### Retrieved KB ${index + 1}`,
            labels ? `Metadata: ${labels}` : '',
            compactText(result.text, MAX_CHUNK_CHARS),
        ].filter(Boolean).join('\n');
    });

    return `\n### RETRIEVED BACKEND KNOWLEDGE BASE CONTEXT\n${formatted.join('\n\n')}\n`;
}

export async function retrieveMigrationKnowledge(input: MigrationKnowledgeInput): Promise<string> {
    const fastApiUrl = process.env.FASTAPI_URL || DEFAULT_FASTAPI_URL;
    const query = buildKnowledgeQuery(input);

    try {
        const response = await fetch(`${fastApiUrl}/kb/search`, {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify({
                query,
                top_k: Number(process.env.MIGRATION_KB_TOP_K || 8),
            }),
        });

        if (!response.ok) {
            console.warn(`[Migration KB] Search failed with status ${response.status}`);
            return '';
        }

        const payload = await response.json() as KBSearchResponse;
        return formatResults(payload.results || []);
    } catch (error) {
        const message = error instanceof Error ? error.message : 'unknown error';
        console.warn(`[Migration KB] Search unavailable: ${message}`);
        return '';
    }
}
