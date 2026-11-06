import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { prisma } from '@/lib/prisma';

export async function POST(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Authentication required' }, { status: 401 });
    const body = await req.json();
    const projectId = typeof body.projectId === 'string' ? body.projectId : null;
    if (projectId) {
        const project = await prisma.project.findFirst({ where: { id: projectId, userId }, select: { id: true } });
        if (!project) return NextResponse.json({ error: 'Project not found' }, { status: 404 });
    }
    const base = (process.env.FASTAPI_URL || 'http://localhost:8000').replace(/\/$/, '');
    try {
        const response = await fetch(`${base}/api/v1/sap/tenant/test-connection`, {
            method: 'POST', headers: { 'content-type': 'application/json', 'X-SAP-API-Key': process.env.SAP_REFERENCE_API_KEY || '' }, body: JSON.stringify(body),
            signal: AbortSignal.timeout(45_000), cache: 'no-store',
        });
        const result = await response.json();
        if (response.ok && projectId) await prisma.project.update({ where: { id: projectId }, data: { sapConnection: result, sapConnectionAt: new Date() } });
        return NextResponse.json(result, { status: response.status });
    } catch {
        return NextResponse.json({ error: 'SAP connection check is unavailable' }, { status: 502 });
    }
}
