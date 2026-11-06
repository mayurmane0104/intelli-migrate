import { NextRequest, NextResponse } from 'next/server';
import { proxyFastify } from '@/lib/server/fastify-proxy';
import { saveIRToFile } from '@/lib/server/save-ir';
import { prisma } from '@/lib/prisma';

export async function GET(request: NextRequest) {
    const projectId = request.nextUrl.searchParams.get('projectId');
    const jobId = request.nextUrl.searchParams.get('jobId');

    if (!projectId) {
        return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    }

    const qs = jobId ? `?jobId=${encodeURIComponent(jobId)}` : '';
    const upstream = await proxyFastify(`/api/projects/${projectId}/analysis/raw${qs}`);

    let payload: Record<string, unknown> | null = null;
    try {
        payload = await upstream.json() as Record<string, unknown>;
    } catch {
        return upstream;
    }

    if (!payload || upstream.status >= 400) {
        return NextResponse.json(payload, { status: upstream.status });
    }

    const rawIr = payload.rawIr ?? payload.raw_ir ?? payload.ir;
    if (!rawIr) {
        return NextResponse.json(payload, { status: upstream.status });
    }

    try {
        const project = await prisma.project.findUnique({
            where: { id: projectId },
            select: { id: true, name: true },
        });
        const sourceFile = String(
            payload.sourceFile ??
            payload.source_file ??
            payload.filePath ??
            payload.file_path ??
            'unknown'
        );
        const result = await saveIRToFile({
            projectId,
            projectName: project?.name || projectId,
            sourceFile,
            irVersion: String(payload.irVersion ?? payload.ir_version ?? 'unknown'),
            ir: rawIr,
        });
        return NextResponse.json({ ...payload, saved: result.saved, path: result.path }, { status: upstream.status });
    } catch {
        return NextResponse.json({ ...payload, saved: false, path: '' }, { status: upstream.status });
    }
}
