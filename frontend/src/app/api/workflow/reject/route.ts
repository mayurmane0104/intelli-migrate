import { NextRequest, NextResponse } from 'next/server';
import { proxyFastify } from '@/lib/server/fastify-proxy';

export async function POST(request: NextRequest) {
    const body = await request.json().catch(() => ({}));
    const projectId = body?.projectId as string | undefined;
    const stage = body?.stage || 'ir';
    if (!projectId) {
        return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    }
    const payload = { ...body };
    delete payload.projectId;
    delete payload.stage;
    return proxyFastify(`/api/projects/${projectId}/workflow/reject?stage=${encodeURIComponent(stage)}`, { method: 'POST', body: payload });
}
