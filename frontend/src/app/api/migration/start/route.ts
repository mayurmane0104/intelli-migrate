import { NextRequest, NextResponse } from 'next/server';
import { jobEngine } from '@/lib/store';

export async function POST(request: NextRequest) {
    try {
        const { projectId } = await request.json();
        if (!projectId) return NextResponse.json({ error: 'Missing projectId' }, { status: 400 });

        const session = await jobEngine.createSession(projectId);
        return NextResponse.json({ session });
    } catch {
        return NextResponse.json({ error: 'Internal error' }, { status: 500 });
    }
}
