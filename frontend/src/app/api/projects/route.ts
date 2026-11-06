import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { dbProjectStore } from '@/lib/db-store';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
    const workspaceId = req.nextUrl.searchParams.get('workspaceId');
    const page = Number(req.nextUrl.searchParams.get('page') ?? '0');
    const take = Number(req.nextUrl.searchParams.get('take') ?? '50');
    const withStats = req.nextUrl.searchParams.get('withStats') === 'true';
    if (workspaceId) {
        const projects = await dbProjectStore.listByWorkspace(workspaceId);
        if (withStats) {
            await Promise.all(projects.slice(page * take, page * take + take).map(p => dbProjectStore.syncStats(p.id)));
        }
        return NextResponse.json({ projects: projects.slice(page * take, page * take + take) });
    }
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    const projects = await dbProjectStore.listByUser(userId);
    return NextResponse.json({ projects: projects.slice(page * take, page * take + take) });
}

export async function POST(req: NextRequest) {
    try {
        const userId = await getAuthUserId(req);
        if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const body = await req.json();
        const { workspaceId, orgId, name, description, migrationType, targetRuntime, sourceType } = body;

        if (!workspaceId || !orgId || !name) {
            return NextResponse.json({ error: 'workspaceId, orgId, and name are required' }, { status: 400 });
        }

        const project = await dbProjectStore.create(userId, {
            workspaceId,
            orgId,
            name,
            description:   description   || '',
            migrationType: migrationType || 'mule4-lambda',
            targetRuntime: targetRuntime || 'nodejs',
            sourceType:    sourceType    || 'git',
        });
        return NextResponse.json({ project }, { status: 201 });
    } catch (err) {
        console.error('[POST /api/projects]', err);
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}
