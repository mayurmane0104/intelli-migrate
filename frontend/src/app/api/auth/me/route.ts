import { NextRequest, NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';
import { getAuthUserId } from '@/lib/server/auth';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) {
        return NextResponse.json({ user: null }, { status: 401 });
    }

    const user = await prisma.user.findUnique({
        where: { id: userId },
    });

    if (!user) {
        return NextResponse.json({ user: null }, { status: 401 });
    }

    const { password: _password, ...safeUser } = user;
    return NextResponse.json({ user: safeUser });
}

export async function PUT(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) {
        return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    try {
        const updates = await req.json();
        const updated = await prisma.user.update({
            where: { id: userId },
            data: updates
        });

        const { password: _passwordUpdate, ...safeUser } = updated;
        return NextResponse.json({ user: safeUser });
    } catch (err: unknown) {
        console.error('Profile update error:', err);
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}
