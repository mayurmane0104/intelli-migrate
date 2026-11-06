'use client';

import React, { createContext, useContext, useState, useCallback, ReactNode, useEffect } from 'react';
import { User, Role } from '../lib/types';
import { authApi } from '../lib/api';
import { useSession, signIn, signOut } from 'next-auth/react';

interface AuthContextType {
    user: User | null;
    isAuthenticated: boolean;
    isLoading: boolean;
    login: (email: string, password: string) => Promise<boolean>;
    register: (name: string, email: string, password: string) => Promise<boolean>;
    logout: () => void;
    updateProfile: (updates: Partial<User>) => Promise<boolean>;
    updatePassword: (current: string, next: string) => Promise<boolean>;
    role: Role;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
    const { data: session, status } = useSession();
    const [user, setUser] = useState<User | null>(null);
    const [isLoading, setIsLoading] = useState(false);

    // Sync with NextAuth session
    useEffect(() => {
        if (status === 'authenticated' && session?.user) {
            const sessionUser = session.user as { id?: string; name?: string; email?: string; role?: string; image?: string };
            const newUser: User = {
                id: sessionUser.id || '',
                name: sessionUser.name || '',
                email: sessionUser.email || '',
                role: (sessionUser.role as Role) || 'developer',
                avatar: sessionUser.image || ''
            };

            // Only set if user has changed to avoid cascading renders
            setUser(prev => {
                if (JSON.stringify(prev) === JSON.stringify(newUser)) return prev;
                return newUser;
            });
        } else if (status === 'unauthenticated') {
            setUser(prev => prev === null ? null : null);
        }
    }, [session, status]);

    const login = useCallback(async (email: string, password: string) => {
        setIsLoading(true);
        const result = await signIn('credentials', {
            redirect: false,
            email,
            password
        });
        setIsLoading(false);
        return !result?.error;
    }, []);

    const register = useCallback(async (name: string, email: string, password: string) => {
        setIsLoading(true);
        try {
            await authApi.register(name, email, password);
            // After registration, log them in
            await login(email, password);
            setIsLoading(false);
            return true;
        } catch {
            setIsLoading(false);
            return false;
        }
    }, [login]);

    const updateProfile = useCallback(async (updates: Partial<User>) => {
        if (!user) return false;
        setIsLoading(true);
        try {
            const { user: updated } = await authApi.updateProfile(updates);
            setUser(updated);
            setIsLoading(false);
            return true;
        } catch {
            setIsLoading(false);
            return false;
        }
    }, [user]);

    const updatePassword = useCallback(async (current: string, next: string) => {
        if (!user) return false;
        setIsLoading(true);
        try {
            await authApi.updatePassword(current, next);
            setIsLoading(false);
            return true;
        } catch {
            setIsLoading(false);
            return false;
        }
    }, [user]);

    const logout = useCallback(async () => {
        setUser(null);
        // Sign out without built-in redirect so we can replace the history
        // entry ourselves.  Using `replace` (not `push`) means the browser's
        // back button can never navigate back to the now-invalidated session.
        await signOut({ redirect: false });
        window.location.replace('/login');
    }, []);

    if (status === 'loading') return null;

    return (
        <AuthContext.Provider value={{
            user,
            isAuthenticated: !!user,
            isLoading,
            login,
            register,
            logout,
            updateProfile,
            updatePassword,
            role: user?.role || 'viewer',
        }}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);
    if (!context) throw new Error('useAuth must be used within AuthProvider');
    return context;
}
