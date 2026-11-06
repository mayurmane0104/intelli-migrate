import { NextRequest, NextResponse } from 'next/server';
import { jobEngine } from '@/lib/store';

export async function POST(request: NextRequest) {
    try {
        const { projectId } = await request.json();
        if (!projectId) return NextResponse.json({ error: 'Missing projectId' }, { status: 400 });

        const count = await jobEngine.retryFailed(projectId);
        return NextResponse.json({ retried: count });
    } catch {
        return NextResponse.json({ error: 'Internal error' }, { status: 500 });
    }
}
