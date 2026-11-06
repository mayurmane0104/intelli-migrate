import { NextRequest, NextResponse } from 'next/server';
import { sessionStore, llmSettingsStore, jobEngine } from '@/lib/store';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
    try {
        const { sourceCode, fileName, migrationType = 'mule4-lambda', targetRuntime = 'nodejs' } = await req.json();

        if (!sourceCode) return NextResponse.json({ error: 'Missing sourceCode' }, { status: 400 });
        if (!fileName) return NextResponse.json({ error: 'Missing fileName' }, { status: 400 });

        const sessionToken = req.cookies.get('ms_session')?.value;
        const userId = sessionToken ? sessionStore.getUserId(sessionToken) : undefined;
        const settings = userId ? await llmSettingsStore.get(userId) : undefined;

        if (!settings || !settings.activeProvider) {
            return NextResponse.json({ error: 'No LLM settings configured.' }, { status: 400 });
        }

        const providerConfig = settings.providers[settings.activeProvider as keyof typeof settings.providers];
        const startTime = Date.now();

        try {
            const fastApiUrl = (process.env.FASTAPI_URL || 'http://localhost:8000').replace(/\/$/, '');
            const backendResponse = await fetch(`${fastApiUrl}/internal/migration/stream-file`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    fileName,
                    filePath: `direct/${fileName}`,
                    sourceContent: sourceCode,
                    migrationType,
                    targetRuntime,
                    projectStructure: '',
                    activeProvider: settings.activeProvider,
                    providerConfig: providerConfig,
                    instructions: '',
                    // The ad-hoc /direct endpoint has no project context, so
                    // skip the IR lookup explicitly (the parser layer never
                    // ran on this snippet).
                    forceNoIr: true,
                }),
            });

            if (!backendResponse.ok) {
                const errText = await backendResponse.text();
                throw new Error(`Backend error (${backendResponse.status}): ${errText}`);
            }

            // The backend returns an SSE stream. We will consume it to build the full text.
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

            return NextResponse.json({
                success: true,
                migratedContent,
                migratedCode,
                provider: settings.activeProvider,
                model: providerConfig.model || 'default',
                duration,
            });
        } catch (err: any) {
            return NextResponse.json({
                success: false,
                error: err.message || 'AI Generation failed',
            }, { status: 500 });
        }
    } catch (err) {
        return NextResponse.json({ error: 'Invalid request' }, { status: 400 });
    }
}
