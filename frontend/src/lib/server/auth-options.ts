import { PrismaAdapter } from '@next-auth/prisma-adapter';
import CredentialsProvider from 'next-auth/providers/credentials';
import GoogleProvider from 'next-auth/providers/google';
import AppleProvider from 'next-auth/providers/apple';
import { prisma } from '@/lib/prisma';
import bcrypt from 'bcryptjs';
import type { NextAuthOptions, Session } from 'next-auth';
import type { JWT } from 'next-auth/jwt';

type AppJwt = JWT & { id?: string; role?: string | null };
type SessionUser = NonNullable<Session['user']> & { id?: string; role?: string };

const oauthProviders = [];

if (process.env.GOOGLE_CLIENT_ID && process.env.GOOGLE_CLIENT_SECRET) {
    oauthProviders.push(GoogleProvider({ clientId: process.env.GOOGLE_CLIENT_ID, clientSecret: process.env.GOOGLE_CLIENT_SECRET }));
}

if (process.env.APPLE_ID && process.env.APPLE_TEAM_ID && process.env.APPLE_KEY_ID && process.env.APPLE_PRIVATE_KEY) {
    oauthProviders.push(AppleProvider({
        clientId: process.env.APPLE_ID,
        clientSecret: {
            teamId: process.env.APPLE_TEAM_ID,
            keyId: process.env.APPLE_KEY_ID,
            privateKey: process.env.APPLE_PRIVATE_KEY.replace(/\\n/g, '\n'),
        } as unknown as string,
    }));
}

export const authOptions: NextAuthOptions = {
    adapter: PrismaAdapter(prisma),
    providers: [
        ...oauthProviders,
        CredentialsProvider({
            name: 'Credentials',
            credentials: {
                email: { label: 'Email', type: 'email' },
                password: { label: 'Password', type: 'password' },
            },
            async authorize(credentials) {
                if (!credentials?.email || !credentials?.password) throw new Error('Missing email or password');
                const user = await prisma.user.findUnique({ where: { email: credentials.email } });
                if (!user || !user.password) throw new Error('No user found with this email');
                if (!(await bcrypt.compare(credentials.password, user.password))) throw new Error('Invalid password');
                return { id: user.id, email: user.email, name: user.name, role: user.role };
            },
        }),
    ],
    callbacks: {
        async jwt({ token, user }: { token: AppJwt; user?: { id?: string; role?: string | null } }) {
            if (user) { token.id = user.id; token.role = user.role; }
            return token;
        },
        async session({ session, token }: { session: Session; token: AppJwt }) {
            if (session.user) {
                const sessionUser = session.user as SessionUser;
                sessionUser.id = typeof token.id === 'string' ? token.id : '';
                sessionUser.role = typeof token.role === 'string' ? token.role : 'developer';
            }
            return session;
        },
    },
    pages: { signIn: '/login' },
    session: { strategy: 'jwt' as const },
    secret: process.env.NEXTAUTH_SECRET,
};
