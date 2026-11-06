import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { dbWorkspaceStore } from '@/lib/db-store';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
    const orgId = req.nextUrl.searchParams.get('orgId');
    if (!orgId) {
        return NextResponse.json({ error: 'orgId query parameter is required' }, { status: 400 });
    }
    const workspaces = await dbWorkspaceStore.listByOrg(orgId);
    return NextResponse.json({ workspaces });
}

export async function POST(req: NextRequest) {
    try {
        const userId = await getAuthUserId(req);
        if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const body = await req.json();
        const { orgId, name, environment, memberCount } = body;

        if (!orgId || !name) {
            return NextResponse.json({ error: 'orgId and name are required' }, { status: 400 });
        }

        if (await dbWorkspaceStore.nameExistsInOrg(orgId, name)) {
            return NextResponse.json({ error: 'A workspace with this name already exists' }, { status: 409 });
        }

        const workspace = await dbWorkspaceStore.create(userId, {
            orgId,
            name,
            environment: environment || 'dev',
            memberCount: memberCount  || 1,
        });
        return NextResponse.json({ workspace }, { status: 201 });
    } catch (err) {
        console.error('[POST /api/workspaces]', err);
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}

export async function DELETE(req: NextRequest) {
    const workspaceId = req.nextUrl.searchParams.get('workspaceId');
    if (!workspaceId) {
        return NextResponse.json({ error: 'workspaceId query parameter is required' }, { status: 400 });
    }
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    const success = await dbWorkspaceStore.delete(workspaceId);
    if (!success) {
        return NextResponse.json({ error: 'Workspace not found or could not be deleted (may contain projects)' }, { status: 404 });
    }
    return NextResponse.json({ success: true });
}
