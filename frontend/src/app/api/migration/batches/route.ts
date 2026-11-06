import { NextRequest, NextResponse } from 'next/server';
import { dbBatchStore } from '@/lib/db-store';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
    const projectId = req.nextUrl.searchParams.get('projectId');
    const page = Number(req.nextUrl.searchParams.get('page') ?? '0');
    const take = Number(req.nextUrl.searchParams.get('take') ?? '50');
    if (!projectId) {
        return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    }
    const batches = await dbBatchStore.listByProject(projectId, { page, take });
    return NextResponse.json({ batches });
}
