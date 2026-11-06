import { NextRequest, NextResponse } from 'next/server';
import { getToken } from 'next-auth/jwt';

const PROTECTED_PREFIX = '/dashboard';
const AUTH_PAGES = ['/login', '/register', '/forgot-password', '/reset-password'];

export async function middleware(req: NextRequest) {
    const { pathname } = req.nextUrl;

    const token = await getToken({
        req,
        secret: process.env.NEXTAUTH_SECRET,
    });

    const isProtected = pathname.startsWith(PROTECTED_PREFIX);
    const isAuthPage = AUTH_PAGES.some(p => pathname.startsWith(p));

    // ── Unauthenticated user hitting a protected route ─────────────────────
    if (isProtected && !token) {
        const loginUrl = req.nextUrl.clone();
        loginUrl.pathname = '/login';
        loginUrl.searchParams.set('callbackUrl', pathname);
        return NextResponse.redirect(loginUrl);
    }

    // ── Authenticated user hitting a login/register page ──────────────────
    // Prevents back-button landing on login after logout is reversed by forward
    if (isAuthPage && token) {
        const homeUrl = req.nextUrl.clone();
        homeUrl.pathname = '/dashboard/organizations';
        homeUrl.search = '';
        return NextResponse.redirect(homeUrl);
    }

    const response = NextResponse.next();

    // ── No-store headers on every protected page ───────────────────────────
    // Browser will never serve a stale cached copy; back-button always
    // re-validates with the server, which will 401 → redirect if logged out.
    if (isProtected) {
        response.headers.set('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
        response.headers.set('Pragma', 'no-cache');
        response.headers.set('Expires', '0');
    }

    return response;
}

export const config = {
    matcher: [
        // Only run auth middleware on page routes.
        // This keeps all /api requests (especially large multipart uploads)
        // out of Next proxy body buffering.
        '/dashboard/:path*',
        '/login',
        '/register',
        '/forgot-password',
        '/reset-password',
    ],
};
