import { NextRequest } from 'next/server';
import { getToken } from 'next-auth/jwt';
import { getServerSession } from 'next-auth/next';
import { authOptions } from '@/lib/server/auth-options';
import { prisma } from '@/lib/prisma';

/**
 * Resolve the authenticated user's DB id for API route handlers.
 *
 * Prefer JWT from the incoming request (same mechanism as middleware).
 * ``getServerSession`` alone can miss cookies behind reverse proxies.
 */
export async function getAuthUserId(req?: NextRequest): Promise<string | null> {
    const secret = process.env.NEXTAUTH_SECRET;

    if (req && secret) {
        const token = await getToken({ req, secret });
        if (typeof token?.id === 'string' && token.id) {
            return token.id;
        }
        const email = typeof token?.email === 'string' ? token.email : null;
        if (email) {
            const user = await prisma.user.findUnique({ where: { email }, select: { id: true } });
            return user?.id ?? null;
        }
    }

    const session = await getServerSession(authOptions);
    const sessionUser = session?.user as { id?: string; email?: string } | undefined;
    if (typeof sessionUser?.id === 'string' && sessionUser.id) {
        return sessionUser.id;
    }
    if (sessionUser?.email) {
        const user = await prisma.user.findUnique({
            where: { email: sessionUser.email },
            select: { id: true },
        });
        return user?.id ?? null;
    }

    return null;
}
