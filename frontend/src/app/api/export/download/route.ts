import { NextRequest, NextResponse } from 'next/server';
import {
    fetchExportPreview,
    isValidExportFormat,
    postExportDownload,
} from '@/lib/server/export-plane';

export const dynamic = 'force-dynamic';
export const fetchCache = 'force-no-store';
export const runtime = 'nodejs';

import { prisma } from '@/lib/prisma';

export async function POST(req: NextRequest) {
    let body: { projectId?: string; format?: string; targetRuntime?: string; targetPlatform?: string; projectNameHint?: string; pipeline?: string };
    try {
        body = await req.json();
    } catch {
        return NextResponse.json({ error: 'Invalid JSON body' }, { status: 400 });
    }

    const projectId = (body.projectId || '').trim();
    const rawFormat = (body.format || 'zip').toLowerCase();
    const format = rawFormat === 'iflow' ? 'cpi-iflow' : rawFormat;
    const projectNameHint = body.projectNameHint || '';
    const pipeline = (body.pipeline || 'v3').toLowerCase();

    if (!projectId) {
        return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    }
    if (!isValidExportFormat(format)) {
        return NextResponse.json({ error: `Unsupported format: ${format}` }, { status: 400 });
    }

    const proj = await prisma.project.findUnique({ where: { id: projectId } }).catch(() => null);
    const resolvedPlatform = body.targetPlatform || (proj as any)?.targetPlatform || (
        proj?.migrationType?.includes('cpi') || proj?.migrationType?.includes('sap') ||
        proj?.targetRuntime === 'groovy' || proj?.targetRuntime === 'cpi-xml' || proj?.targetRuntime === 'xslt' ||
        body.targetRuntime === 'groovy' || body.targetRuntime === 'cpi-xml' ||
        format === 'cpi-package' || format === 'cpi-iflow' || format === 'cpi-tenant-push'
            ? 'sap-integration-suite'
            : 'aws'
    );
    const targetRuntime = (body.targetRuntime || (resolvedPlatform === 'sap-integration-suite' ? 'groovy' : 'python')).toLowerCase();

    return postExportDownload(projectId, { format, targetRuntime, targetPlatform: resolvedPlatform, projectNameHint, pipeline });
}

export async function GET(req: NextRequest) {
    const projectId = req.nextUrl.searchParams.get('projectId') || '';
    const rawFormat = (req.nextUrl.searchParams.get('format') || 'zip').toLowerCase();
    const format = rawFormat === 'iflow' ? 'cpi-iflow' : rawFormat;
    const queryPlatform = req.nextUrl.searchParams.get('targetPlatform') || '';
    const pipeline = (req.nextUrl.searchParams.get('pipeline') || 'v3').toLowerCase();

    if (!projectId) {
        return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    }
    if (!isValidExportFormat(format)) {
        return NextResponse.json({ error: `Unsupported format: ${format}` }, { status: 400 });
    }

    const proj = await prisma.project.findUnique({ where: { id: projectId } }).catch(() => null);
    const resolvedPlatform = queryPlatform || (proj as any)?.targetPlatform || (
        proj?.migrationType?.includes('cpi') || proj?.migrationType?.includes('sap') ||
        proj?.targetRuntime === 'groovy' || proj?.targetRuntime === 'cpi-xml' || proj?.targetRuntime === 'xslt' ||
        format === 'cpi-package' || format === 'cpi-iflow' || format === 'cpi-tenant-push'
            ? 'sap-integration-suite'
            : 'aws'
    );
    const targetRuntime = (req.nextUrl.searchParams.get('targetRuntime') || (resolvedPlatform === 'sap-integration-suite' ? 'groovy' : 'python')).toLowerCase();

    const result = await fetchExportPreview(projectId, format, targetRuntime, pipeline, resolvedPlatform);
    const data = result.data ?? { error: 'Empty preview response from export pipeline' };

    if (!result.ok) {
        const payload = typeof data === 'object' && data !== null ? data : { error: String(data) };
        return NextResponse.json(payload, { status: result.status });
    }

    return NextResponse.json(data, { status: 200 });
}
