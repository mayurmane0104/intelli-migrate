import { NextRequest, NextResponse } from 'next/server';
import { proxyFastify } from '@/lib/server/fastify-proxy';

export async function POST(request: NextRequest) {
    const body = await request.json().catch(() => ({}));
    const projectId = body?.projectId as string | undefined;
    if (!projectId) {
        return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    }
    const payload = { ...body };
    delete payload.projectId;
    return proxyFastify(`/api/projects/${projectId}/workflow/request-reanalysis`, { method: 'POST', body: payload });
}
