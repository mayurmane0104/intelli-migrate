import { NextRequest, NextResponse } from 'next/server';
import { dbFileStore } from '@/lib/db-store';
export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
    const projectId = req.nextUrl.searchParams.get('projectId');
    const page = Number(req.nextUrl.searchParams.get('page') ?? '0');
    const take = Number(req.nextUrl.searchParams.get('take') ?? '50');
    const includeContent = req.nextUrl.searchParams.get('includeContent') === 'true';
    const includeMigrations = req.nextUrl.searchParams.get('includeMigrations') === 'true';
    if (!projectId) {
        return NextResponse.json({ error: 'projectId query parameter is required' }, { status: 400 });
    }
    const files = await dbFileStore.listByProject(projectId, { page, take, includeContent, includeMigrations });
    return NextResponse.json({ files });
}
