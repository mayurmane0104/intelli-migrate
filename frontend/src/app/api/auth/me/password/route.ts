import { NextRequest, NextResponse } from 'next/server';
import { userStore, sessionStore } from '@/lib/store';

export async function PUT(req: NextRequest) {
    const token = req.cookies.get('ms_session')?.value;
    if (!token) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

    const userId = sessionStore.getUserId(token);
    if (!userId) return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });

    try {
        const { currentPassword, newPassword } = await req.json();

        if (!currentPassword || !newPassword) {
            return NextResponse.json({ error: 'Current and new passwords are required' }, { status: 400 });
        }

        if (newPassword.length < 6) {
            return NextResponse.json({ error: 'New password must be at least 6 characters' }, { status: 400 });
        }

        const success = userStore.updatePassword(userId, currentPassword, newPassword);
        if (!success) {
            return NextResponse.json({ error: 'Current password is incorrect' }, { status: 400 });
        }

        return NextResponse.json({ success: true });
    } catch {
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}
