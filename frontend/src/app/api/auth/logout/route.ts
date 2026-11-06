import { NextRequest, NextResponse } from 'next/server';
import { sessionStore } from '@/lib/store';

export async function POST(req: NextRequest) {
    const token = req.cookies.get('ms_session')?.value;
    if (token) {
        sessionStore.destroy(token);
    }

    const response = NextResponse.json({ success: true });
    response.cookies.delete('ms_session');
    return response;
}
