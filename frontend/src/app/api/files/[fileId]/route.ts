import { NextRequest, NextResponse } from 'next/server';
import { dbFileStore } from '@/lib/db-store';

export const dynamic = 'force-dynamic';

export async function GET(
    _req: NextRequest,
    { params }: { params: Promise<{ fileId: string }> }
) {
    const { fileId } = await params;
    const file = await dbFileStore.findById(fileId);
    if (!file) {
        return NextResponse.json({ error: 'File not found' }, { status: 404 });
    }
    return NextResponse.json({ file });
}

export async function PUT(
    req: NextRequest,
    { params }: { params: Promise<{ fileId: string }> }
) {
    try {
        const { fileId } = await params;
        const updates = await req.json();
        const file = await dbFileStore.update(fileId, updates);
        if (!file) {
            return NextResponse.json({ error: 'File not found' }, { status: 404 });
        }
        return NextResponse.json({ file });
    } catch {
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}
