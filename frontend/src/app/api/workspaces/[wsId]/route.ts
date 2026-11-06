import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { prisma } from '@/lib/prisma';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest, { params }: { params: Promise<{ wsId: string }> }) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    
    const { wsId } = await params;
    
    try {
        const workspace = await prisma.workspace.findUnique({
            where: { id: wsId },
            include: {
                _count: {
                    select: { projects: true }
                }
            }
        });
        
        if (!workspace) {
            return NextResponse.json({ error: 'Workspace not found' }, { status: 404 });
        }
        
        return NextResponse.json({ workspace: {
            ...workspace,
            projectCount: workspace._count.projects,
            createdAt: (workspace as { createdAt?: Date }).createdAt?.toISOString?.().split('T')[0] || new Date().toISOString().split('T')[0]
        }});
    } catch (err) {
        console.error('[GET /api/workspaces/[wsId]]', err);
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}
