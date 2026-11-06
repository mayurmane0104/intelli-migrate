import { NextRequest } from 'next/server';
import { proxyFastify } from '@/lib/server/fastify-proxy';

export const dynamic = 'force-dynamic';

export async function GET(
    _request: NextRequest,
    { params }: { params: Promise<{ projectId: string }> },
) {
    const { projectId } = await params;
    return proxyFastify(`/api/projects/${projectId}/active-batch`);
}
