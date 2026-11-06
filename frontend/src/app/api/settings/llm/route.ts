import { NextRequest, NextResponse } from 'next/server';
import { sessionStore, llmSettingsStore } from '@/lib/store';
import type { LLMSettings, LLMProviderType } from '@/lib/types';

export const dynamic = 'force-dynamic';

function getUserIdFromRequest(request: NextRequest): string | null {
    const sessionToken = request.cookies.get('ms_session')?.value;
    if (!sessionToken) return null;
    return sessionStore.getUserId(sessionToken) || null;
}

function maskApiKey(key: string): string {
    if (!key || key.length < 8) return key ? '••••••••' : '';
    return key.slice(0, 4) + '••••' + key.slice(-4);
}

function normalizeProvider(provider: unknown, fallback: LLMProviderType): LLMProviderType {
    return provider === 'nova' || provider === 'claude' || provider === 'openai' || provider === 'gemini' ? provider : fallback;
}

export async function GET(request: NextRequest) {
    const userId = getUserIdFromRequest(request);
    const reveal = request.nextUrl.searchParams.get('reveal') === 'true';

    // Gracefully return defaults if not authenticated (e.g., dev server restart)
    const settings = userId ? await llmSettingsStore.get(userId) : llmSettingsStore.getDefaults();

    if (reveal) {
        return NextResponse.json({ settings });
    }

    // Return settings with masked API keys
    const masked = {
        ...settings,
        providers: {
            nova: { ...settings.providers.nova, apiKey: maskApiKey(settings.providers.nova?.apiKey || '') },
            claude: { ...settings.providers.claude, apiKey: maskApiKey(settings.providers.claude.apiKey) },
            openai: { ...settings.providers.openai, apiKey: maskApiKey(settings.providers.openai.apiKey) },
            gemini: { ...settings.providers.gemini, apiKey: maskApiKey(settings.providers.gemini.apiKey) },
        },
    };

    return NextResponse.json({ settings: masked });
}

export async function PUT(request: NextRequest) {
    const rawUserId = getUserIdFromRequest(request);
    const userId = rawUserId || 'default-user'; // Fallback for dev mode

    try {
        const body = await request.json();
        const incoming = body.settings as Partial<LLMSettings>;
        if (!incoming) return NextResponse.json({ error: 'Missing settings' }, { status: 400 });

        // Get existing settings to preserve un-changed API keys
        const existing = await llmSettingsStore.get(userId);

        const updatedSettings: LLMSettings = {
            activeProvider: normalizeProvider(incoming.activeProvider, normalizeProvider(existing.activeProvider, 'openai')),
            providers: {
                nova: {
                    apiKey: resolveApiKey(incoming.providers?.nova?.apiKey, existing.providers.nova?.apiKey || ''),
                    model: incoming.providers?.nova?.model || existing.providers.nova?.model || 'amazon.nova-lite-v1:0',
                    enabled: incoming.providers?.nova?.enabled ?? existing.providers.nova?.enabled ?? false,
                },
                claude: {
                    apiKey: resolveApiKey(incoming.providers?.claude?.apiKey, existing.providers.claude.apiKey),
                    model: incoming.providers?.claude?.model || existing.providers.claude.model,
                    enabled: incoming.providers?.claude?.enabled ?? existing.providers.claude.enabled,
                },
                openai: {
                    apiKey: resolveApiKey(incoming.providers?.openai?.apiKey, existing.providers.openai.apiKey),
                    model: incoming.providers?.openai?.model || existing.providers.openai.model,
                    enabled: incoming.providers?.openai?.enabled ?? existing.providers.openai.enabled,
                },
                gemini: {
                    apiKey: resolveApiKey(incoming.providers?.gemini?.apiKey, existing.providers.gemini.apiKey),
                    model: incoming.providers?.gemini?.model || existing.providers.gemini.model,
                    enabled: incoming.providers?.gemini?.enabled ?? existing.providers.gemini.enabled,
                },
            },
            theme: incoming.theme || existing.theme,
            notifications: incoming.notifications ?? existing.notifications,
        };

        const saved = await llmSettingsStore.save(userId, updatedSettings);

        // Return with masked keys
        const masked = {
            ...saved,
            providers: {
                nova: { ...saved.providers.nova, apiKey: maskApiKey(saved.providers.nova?.apiKey || '') },
                claude: { ...saved.providers.claude, apiKey: maskApiKey(saved.providers.claude.apiKey) },
                openai: { ...saved.providers.openai, apiKey: maskApiKey(saved.providers.openai.apiKey) },
                gemini: { ...saved.providers.gemini, apiKey: maskApiKey(saved.providers.gemini.apiKey) },
            },
        };

        return NextResponse.json({ settings: masked, saved: true });
    } catch (error: any) {
        return NextResponse.json({ error: error.message || 'Internal error' }, { status: 500 });
    }
}

/**
 * If the incoming key contains '••••' (masked), keep the existing key.
 * Otherwise, use the new key.
 */
function resolveApiKey(incoming: string | undefined, existing: string): string {
    if (!incoming) return existing;
    if (incoming.includes('••••')) return existing;
    return incoming;
}
