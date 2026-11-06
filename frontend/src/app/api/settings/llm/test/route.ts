import { NextRequest, NextResponse } from 'next/server';
import { sessionStore, llmSettingsStore } from '@/lib/store';
import type { LLMProviderType } from '@/lib/types';

export const dynamic = 'force-dynamic';

function getUserIdFromRequest(request: NextRequest): string | null {
    const sessionToken = request.cookies.get('ms_session')?.value;
    if (!sessionToken) return null;
    return sessionStore.getUserId(sessionToken) || null;
}

async function testProviderConnection(
    provider: LLMProviderType,
    apiKey: string,
    model?: string,
): Promise<{ success: boolean; message: string }> {
    if (provider === 'nova') {
        const accessKey = apiKey || process.env.AWS_ACCESS_KEY_ID || '';
        const secretKey = process.env.AWS_SECRET_ACCESS_KEY || '';
        if (!accessKey || !secretKey) {
            return { success: false, message: 'AWS credentials not configured (AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY)' };
        }
        return { success: true, message: 'AWS Bedrock credentials are configured' };
    }

    if (!apiKey?.trim()) {
        return { success: false, message: 'API key is required' };
    }

    if (provider === 'claude') {
        const response = await fetch('https://api.anthropic.com/v1/messages', {
            method: 'POST',
            headers: {
                'x-api-key': apiKey,
                'anthropic-version': '2023-06-01',
                'content-type': 'application/json',
            },
            body: JSON.stringify({
                model: model || 'claude-3-5-haiku-20241022',
                max_tokens: 1,
                messages: [{ role: 'user', content: 'ping' }],
            }),
        });
        if (response.ok) {
            return { success: true, message: 'Connected to Anthropic API' };
        }
        const detail = await response.text();
        return { success: false, message: `Anthropic API error (${response.status}): ${detail.slice(0, 200)}` };
    }

    if (provider === 'openai') {
        const response = await fetch('https://api.openai.com/v1/models', {
            headers: { Authorization: `Bearer ${apiKey}` },
        });
        if (response.ok) {
            return { success: true, message: 'Connected to OpenAI API' };
        }
        const detail = await response.text();
        return { success: false, message: `OpenAI API error (${response.status}): ${detail.slice(0, 200)}` };
    }

    if (provider === 'gemini') {
        const modelId = model || 'gemini-2.0-flash';
        const response = await fetch(
            `https://generativelanguage.googleapis.com/v1beta/models/${modelId}?key=${encodeURIComponent(apiKey)}`,
        );
        if (response.ok) {
            return { success: true, message: 'Connected to Google Gemini API' };
        }
        const detail = await response.text();
        return { success: false, message: `Gemini API error (${response.status}): ${detail.slice(0, 200)}` };
    }

    return { success: false, message: 'Invalid provider' };
}

export async function POST(request: NextRequest) {
    const rawUserId = getUserIdFromRequest(request);
    const userId = rawUserId || 'default-user';

    try {
        const body = await request.json();
        const { provider, apiKey, model } = body;

        if (!provider) {
            return NextResponse.json({ error: 'Missing provider' }, { status: 400 });
        }

        let actualApiKey = apiKey;
        if (apiKey && apiKey.includes('••••')) {
            const settings = await llmSettingsStore.get(userId);
            const providerConfig = settings.providers[provider as LLMProviderType];
            actualApiKey = providerConfig?.apiKey || '';
        }

        const result = await testProviderConnection(provider as LLMProviderType, actualApiKey, model);
        return NextResponse.json(result);
    } catch (err: unknown) {
        return NextResponse.json(
            { success: false, message: err instanceof Error ? err.message : 'Internal error' },
            { status: 500 },
        );
    }
}
