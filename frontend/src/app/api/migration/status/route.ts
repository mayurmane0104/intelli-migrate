import { NextRequest, NextResponse } from 'next/server';
import { jobEngine } from '@/lib/store';
import { dbFileStore } from '@/lib/db-store';

export const dynamic = 'force-dynamic';

export async function GET(request: NextRequest) {
    const projectId = request.nextUrl.searchParams.get('projectId');
    if (!projectId) return NextResponse.json({ error: 'Missing projectId' }, { status: 400 });

    const session = jobEngine.getSession(projectId);
    const allFiles = await dbFileStore.listByProject(projectId);
    const projectFiles = allFiles.filter(f => f.type === 'file');

    const completedFiles = projectFiles.filter(f => f.status === 'completed').length;
    const failedFiles = projectFiles.filter(f => f.status === 'failed').length;
    const pendingFiles = projectFiles.filter(f => f.status === 'pending').length;
    const inProgressFiles = projectFiles.filter(f => f.status === 'in-progress').length;

    return NextResponse.json({
        isRunning: session?.status === 'running',
        progress: session ? Math.round(((session.completedJobs + session.failedJobs) / Math.max(session.totalJobs, 1)) * 100) : 0,
        currentFile: session?.jobs.find(j => j.status === 'running')?.fileName || null,
        session: session || null,
        stats: { total: projectFiles.length, completed: completedFiles, failed: failedFiles, pending: pendingFiles, inProgress: inProgressFiles },
        files: projectFiles,
    });
}
