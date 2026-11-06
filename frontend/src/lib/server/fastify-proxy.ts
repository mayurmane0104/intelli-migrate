import { NextResponse } from 'next/server';

export const FASTIFY_URL = process.env.FASTIFY_URL || process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001';

type ProxyOptions = {
    method?: 'GET' | 'POST';
    body?: unknown;
};

export async function proxyFastify(path: string, options: ProxyOptions = {}): Promise<NextResponse> {
    const method = options.method || 'GET';
    const init: RequestInit = {
        method,
        headers: {
            'content-type': 'application/json',
        },
        cache: 'no-store',
    };

    if (options.body !== undefined) {
        init.body = JSON.stringify(options.body);
    }

    try {
        const response = await fetch(`${FASTIFY_URL}${path}`, init);
        const text = await response.text();
        let data: unknown = null;

        try {
            data = text ? JSON.parse(text) : null;
        } catch {
            data = { message: text };
        }

        return NextResponse.json(data, { status: response.status });
    } catch (error: any) {
        return NextResponse.json(
            {
                error: 'Failed to reach control plane',
                detail: error?.message || 'Unknown proxy error',
            },
            { status: 502 },
        );
    }
}

export async function callFastify(path: string, options: ProxyOptions = {}): Promise<{
    ok: boolean;
    status: number;
    data: unknown;
}> {
    const method = options.method || 'GET';
    const init: RequestInit = {
        method,
        headers: {
            'content-type': 'application/json',
        },
        cache: 'no-store',
    };

    if (options.body !== undefined) {
        init.body = JSON.stringify(options.body);
    }

    const response = await fetch(`${FASTIFY_URL}${path}`, init);
    const text = await response.text();
    let data: unknown = null;
    try {
        data = text ? JSON.parse(text) : null;
    } catch {
        data = { message: text };
    }
    return { ok: response.ok, status: response.status, data };
}
