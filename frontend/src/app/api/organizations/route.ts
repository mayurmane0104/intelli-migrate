import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { dbOrgStore } from '@/lib/db-store';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    const organizations = await dbOrgStore.list(userId);
    return NextResponse.json({ organizations });
}

export async function POST(req: NextRequest) {
    try {
        const userId = await getAuthUserId(req);
        if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

        const body = await req.json();
        const { name, description, owner, logo } = body;

        if (!name) {
            return NextResponse.json({ error: 'Organization name is required' }, { status: 400 });
        }

        if (await dbOrgStore.nameExists(name)) {
            return NextResponse.json({ error: 'An organization with this name already exists' }, { status: 409 });
        }

        const org = await dbOrgStore.create(userId, {
            name,
            description: description || '',
            owner:       owner || 'Current User',
            logo:        logo  || '',
        });
        return NextResponse.json({ organization: org }, { status: 201 });
    } catch (err) {
        console.error('[POST /api/organizations]', err);
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}

export async function DELETE(req: NextRequest) {
    const id = req.nextUrl.searchParams.get('id');
    if (!id) return NextResponse.json({ error: 'id query parameter is required' }, { status: 400 });
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    const success = await dbOrgStore.delete(id);
    if (!success) return NextResponse.json({ error: 'Organization not found' }, { status: 404 });
    return NextResponse.json({ success: true });
}
