import { NextRequest, NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';
import bcrypt from 'bcryptjs';

export async function POST(req: NextRequest) {
    try {
        const { name, email, password } = await req.json();

        if (!name || !email || !password) {
            return NextResponse.json({ error: 'Name, email, and password are required' }, { status: 400 });
        }

        if (password.length < 6) {
            return NextResponse.json({ error: 'Password must be at least 6 characters' }, { status: 400 });
        }

        const existing = await prisma.user.findUnique({
            where: { email }
        });

        if (existing) {
            return NextResponse.json({ error: 'A user with this email already exists' }, { status: 409 });
        }

        const hashedPassword = await bcrypt.hash(password, 10);

        const user = await prisma.user.create({
            data: {
                name,
                email,
                password: hashedPassword,
                role: 'developer',
                settings: {
                    create: {
                        activeProvider: 'claude',
                        llmSettings: {},
                        editorSettings: {}
                    }
                }
            }
        });

        // Omit password from response
        const { password: _password, ...safeUser } = user;

        return NextResponse.json({ user: safeUser });
    } catch (err: unknown) {
        console.error('Registration error:', err);
        return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
    }
}
