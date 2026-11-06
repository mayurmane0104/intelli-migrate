import { NextRequest } from 'next/server';
import { proxyFastify } from '@/lib/server/fastify-proxy';

export const dynamic = 'force-dynamic';

export async function GET(
    request: NextRequest,
    { params }: { params: Promise<{ projectId: string }> },
) {
    const { projectId } = await params;
    const qs = request.nextUrl.search;
    return proxyFastify(`/api/projects/${projectId}/files${qs}`);
}
