import { NextRequest, NextResponse } from 'next/server';
import { proxyFastify } from '@/lib/server/fastify-proxy';

export async function GET(request: NextRequest) {
    const projectId = request.nextUrl.searchParams.get('projectId');
    const includeRaw = request.nextUrl.searchParams.get('includeRaw');
    if (!projectId) {
        return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    }

    const qs = includeRaw === 'true' ? '?includeRaw=true' : '';
    return proxyFastify(`/api/projects/${projectId}/analysis/latest${qs}`);
}

