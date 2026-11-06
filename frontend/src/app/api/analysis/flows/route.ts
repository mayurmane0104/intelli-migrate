import { NextRequest, NextResponse } from 'next/server';
import { proxyFastify } from '@/lib/server/fastify-proxy';

export async function GET(request: NextRequest) {
    const projectId = request.nextUrl.searchParams.get('projectId');
    if (!projectId) {
        return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    }
    return proxyFastify(`/api/projects/${projectId}/analysis/flows`);
}

