import { NextRequest } from 'next/server';
import { proxyFastify } from '@/lib/server/fastify-proxy';

export const dynamic = 'force-dynamic';

export async function POST(
    request: NextRequest,
    { params }: { params: Promise<{ projectId: string }> },
) {
    const { projectId } = await params;
    const body = await request.json().catch(() => ({}));
    return proxyFastify(`/api/projects/${projectId}/retry-file`, { method: 'POST', body });
}
