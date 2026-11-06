import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { prisma } from '@/lib/prisma';

export async function POST(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Authentication required' }, { status: 401 });
    const body = await req.json().catch(() => null) as Record<string, unknown> | null;
    const projectId = typeof body?.projectId === 'string' ? body.projectId : '';
    if (!projectId) return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    const project = await prisma.project.findFirst({ where: { id: projectId, userId }, select: { id: true, targetPlatform: true } });
    if (!project) return NextResponse.json({ error: 'Project not found' }, { status: 404 });
    if (project.targetPlatform !== 'sap-integration-suite') return NextResponse.json({ error: 'Select SAP Integration Suite as the project target first.' }, { status: 409 });
    const base = (process.env.FASTAPI_URL || 'http://localhost:8000').replace(/\/$/, '');
    try {
        console.info('SAP test deployment approved', { userId, projectId, at: new Date().toISOString() });
        const response = await fetch(`${base}/api/v1/sap/tenant/test-deployment`, {
            method: 'POST', headers: { 'content-type': 'application/json', 'X-SAP-API-Key': process.env.SAP_REFERENCE_API_KEY || '', 'X-SAP-Actor': userId },
            body: JSON.stringify(body), signal: AbortSignal.timeout(120_000), cache: 'no-store',
        });
        const result = await response.json();
        if (response.ok) await prisma.project.update({ where: { id: projectId }, data: { sapTestDeployment: result, sapTestDeploymentAt: new Date() } });
        return NextResponse.json(result, { status: response.status });
    } catch {
        return NextResponse.json({ error: 'SAP test deployment could not be completed' }, { status: 502 });
    }
}
