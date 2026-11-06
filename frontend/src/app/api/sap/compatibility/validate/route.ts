import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { prisma } from '@/lib/prisma';

export async function POST(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Authentication required' }, { status: 401 });
    const incoming = await req.formData();
    const projectId = String(incoming.get('projectId') || '');
    if (!projectId) return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    const project = await prisma.project.findFirst({ where: { id: projectId, userId }, select: { id: true } });
    if (!project) return NextResponse.json({ error: 'Project not found' }, { status: 404 });
    const files = incoming.getAll('files').filter((entry): entry is File => entry instanceof File);
    if (!files.length || files.length > 20) return NextResponse.json({ error: 'Upload between 1 and 20 generated iFlow ZIP files' }, { status: 400 });
    if (files.some(file => file.size > 50 * 1024 * 1024 || !file.name.toLowerCase().endsWith('.zip'))) return NextResponse.json({ error: 'Each generated artifact must be a ZIP under 50 MB' }, { status: 413 });
    if (files.reduce((total, file) => total + file.size, 0) > 100 * 1024 * 1024) return NextResponse.json({ error: 'Combined artifact size exceeds 100 MB' }, { status: 413 });
    const reference = await prisma.sapReference.findFirst({ where: { userId, projectId, expiresAt: { gt: new Date() } }, orderBy: { createdAt: 'desc' } });
    const upstream = new FormData();
    files.forEach(file => upstream.append('files', file, file.name));
    if (reference) {
        const serialized = JSON.stringify(reference.profile);
        if (serialized.length > 1_000_000) return NextResponse.json({ error: 'Saved SAP profile exceeds the compatibility request limit.' }, { status: 413 });
        upstream.set('reference_profile', serialized);
    }
    try {
        const base = (process.env.FASTAPI_URL || 'http://localhost:8000').replace(/\/$/, '');
        const response = await fetch(`${base}/api/v1/sap/compatibility/validate`, { method: 'POST', headers: { 'X-SAP-API-Key': process.env.SAP_REFERENCE_API_KEY || '' }, body: upstream, signal: AbortSignal.timeout(90_000), cache: 'no-store' });
        const result = await response.json();
        if (response.ok) await prisma.project.update({ where: { id: projectId }, data: { sapValidation: result, sapValidationAt: new Date() } });
        return NextResponse.json(result, { status: response.status });
    } catch {
        return NextResponse.json({ error: 'SAP compatibility validator is unavailable' }, { status: 502 });
    }
}
