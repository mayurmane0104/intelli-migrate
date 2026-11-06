import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { prisma } from '@/lib/prisma';
import { randomUUID } from 'node:crypto';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Authentication required' }, { status: 401 });
    const form = await req.formData();
    const file = form.get('file');
    if (!(file instanceof File)) return NextResponse.json({ error: 'ZIP file is required' }, { status: 400 });
    if (file.size > 50 * 1024 * 1024) return NextResponse.json({ error: 'File exceeds 50 MB' }, { status: 413 });
    const projectIdValue = form.get('projectId');
    const projectId = typeof projectIdValue === 'string' ? projectIdValue : null;
    if (projectId) {
        const project = await prisma.project.findFirst({ where: { id: projectId, userId }, select: { id: true } });
        if (!project) return NextResponse.json({ error: 'Project not found' }, { status: 404 });
    }
    const upstreamForm = new FormData();
    upstreamForm.set('file', file, file.name);
    try {
        const base = (process.env.FASTAPI_URL || 'http://localhost:8000').replace(/\/$/, '');
        const response = await fetch(`${base}/api/v1/sap/reference/upload`, { method: 'POST', headers: { 'X-SAP-API-Key': process.env.SAP_REFERENCE_API_KEY || '' }, body: upstreamForm, signal: AbortSignal.timeout(60_000), cache: 'no-store' });
        const body = await response.json();
        if (!response.ok) return NextResponse.json(body, { status: response.status });
        const now = new Date();
        await prisma.sapReference.deleteMany({ where: { userId, expiresAt: { lt: now } } });
        const reference = await prisma.$transaction(async tx => {
            const saved = await tx.sapReference.create({ data: {
                id: typeof body.reference_id === 'string' ? body.reference_id : randomUUID(),
                userId, projectId, filename: file.name, artifactType: String(body.artifact_type || 'unknown'),
                profile: body, expiresAt: new Date(now.getTime() + 30 * 24 * 60 * 60 * 1000),
            } });
            if (projectId) await tx.project.update({ where: { id: projectId }, data: { sapReferenceMode: 'reference' } });
            return saved;
        });
        return NextResponse.json({ ...body, reference_id: reference.id, persisted: true }, { status: 201 });
    } catch {
        return NextResponse.json({ error: 'Analysis or secure profile persistence failed. No uploaded archive was retained.' }, { status: 503 });
    }
}

export async function PUT(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Authentication required' }, { status: 401 });
    const body = await req.json().catch(() => null) as { projectId?: string; mode?: string } | null;
    if (!body?.projectId || !['standard', 'reference'].includes(body.mode || '')) return NextResponse.json({ error: 'projectId and supported mode are required' }, { status: 400 });
    if (body.mode === 'reference') {
        const reference = await prisma.sapReference.findFirst({ where: { userId, projectId: body.projectId, expiresAt: { gt: new Date() } }, select: { id: true } });
        if (!reference) return NextResponse.json({ error: 'Analyze a reference archive before selecting reference mode.' }, { status: 409 });
    }
    const updated = await prisma.project.updateMany({ where: { id: body.projectId, userId }, data: { sapReferenceMode: body.mode } });
    if (!updated.count) return NextResponse.json({ error: 'Project not found' }, { status: 404 });
    if (body.mode === 'standard') await prisma.sapReference.deleteMany({ where: { userId, projectId: body.projectId } });
    return NextResponse.json({ mode: body.mode });
}

export async function GET(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Authentication required' }, { status: 401 });
    const projectId = req.nextUrl.searchParams.get('projectId');
    await prisma.sapReference.deleteMany({ where: { userId, expiresAt: { lt: new Date() } } });
    const reference = await prisma.sapReference.findFirst({ where: { userId, projectId: projectId || null }, orderBy: { createdAt: 'desc' } });
    return NextResponse.json({ reference: reference ? { reference_id: reference.id, filename: reference.filename, artifact_type: reference.artifactType, created_at: reference.createdAt, expires_at: reference.expiresAt, ...reference.profile as object } : null });
}

export async function DELETE(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Authentication required' }, { status: 401 });
    const referenceId = req.nextUrl.searchParams.get('referenceId');
    if (!referenceId) return NextResponse.json({ error: 'referenceId is required' }, { status: 400 });
    const reference = await prisma.sapReference.findFirst({ where: { id: referenceId, userId }, select: { id: true, projectId: true } });
    if (!reference) return NextResponse.json({ error: 'Reference not found' }, { status: 404 });
    await prisma.$transaction(async tx => {
        await tx.sapReference.delete({ where: { id: reference.id } });
        if (reference.projectId) await tx.project.updateMany({ where: { id: reference.projectId, userId }, data: { sapReferenceMode: 'standard' } });
    });
    return NextResponse.json({ deleted: true });
}
