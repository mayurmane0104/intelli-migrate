import { NextRequest, NextResponse } from 'next/server';
import { userStore, sessionStore } from '@/lib/store';

export async function POST(req: NextRequest) {
    try {
        const { email, password } = await req.json();

        if (!email || !password) {
            return NextResponse.json({ error: 'Email and password are required' }, { status: 400 });
        }

        const user = userStore.findByEmail(email);
        if (!user || user.password !== password) {
            return NextResponse.json({ error: 'Invalid email or password' }, { status: 401 });
        }

        const token = sessionStore.create(user.id);
        const safeUser = userStore.toSafe(user);

        const response = NextResponse.json({ user: safeUser });
        response.cookies.set('ms_session', token, {
            httpOnly: true,
            path: '/',
            sameSite: 'lax',
            maxAge: 60 * 60 * 24 * 7, // 7 days
        });

        return response;
    } catch {
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}
