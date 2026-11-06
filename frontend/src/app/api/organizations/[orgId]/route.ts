import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { prisma } from '@/lib/prisma';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: Promise<{ orgId: string }> }) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    
    const { orgId } = await params;
    
    try {
        const organization = await prisma.organization.findUnique({
            where: { id: orgId },
            include: {
                _count: {
                    select: { workspaces: true }
                }
            }
        });
        
        if (!organization) {
            return NextResponse.json({ error: 'Organization not found' }, { status: 404 });
        }
        
        return NextResponse.json({ organization: {
            ...organization,
            workspaceCount: organization._count.workspaces,
            createdAt: organization.createdAt.toISOString().split('T')[0]
        }});
    } catch (err) {
        console.error('[GET /api/organizations/[orgId]]', err);
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}
