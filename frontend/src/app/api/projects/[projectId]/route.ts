import { NextRequest, NextResponse } from 'next/server';
import { dbProjectStore } from '@/lib/db-store';

export const dynamic = 'force-dynamic';

export async function GET(
    _req: NextRequest,
    { params }: { params: Promise<{ projectId: string }> }
) {
    const { projectId } = await params;
    await dbProjectStore.syncStats(projectId);
    const project = await dbProjectStore.findById(projectId);
    if (!project) {
        return NextResponse.json({ error: 'Project not found' }, { status: 404 });
    }
    return NextResponse.json({ project });
}

export async function PUT(
    req: NextRequest,
    { params }: { params: Promise<{ projectId: string }> }
) {
    try {
        const { projectId } = await params;
        const updates = await req.json();
        const project = await dbProjectStore.update(projectId, updates);
        if (!project) {
            return NextResponse.json({ error: 'Project not found' }, { status: 404 });
        }
        return NextResponse.json({ project });
    } catch {
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}

export async function DELETE(_req: NextRequest, { params }: { params: Promise<{ projectId: string }> }) {
    const { projectId } = await params;
    const success = await dbProjectStore.delete(projectId);
    if (!success) {
        return NextResponse.json({ error: 'Project not found or could not be deleted' }, { status: 404 });
    }
    return NextResponse.json({ success: true });
}
