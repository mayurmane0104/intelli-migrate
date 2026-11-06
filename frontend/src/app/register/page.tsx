'use client';

import React, { useState, useCallback } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useRouter } from 'next/navigation';
import { EyeIcon, EyeSlashIcon, CheckCircleIcon } from '@heroicons/react/24/outline';
import { signIn } from 'next-auth/react';

export default function RegisterPage() {
    const { register, isLoading } = useAuth();
    const router = useRouter();
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [errors, setErrors] = useState<{ name?: string; email?: string; password?: string; confirm?: string; general?: string }>({});

    const validate = useCallback(() => {
        const errs: { name?: string; email?: string; password?: string; confirm?: string; general?: string } = {};
        if (!name) errs.name = 'Full name is required';
        if (!email) errs.email = 'Email is required';
        else if (!/\S+@\S+\.\S+/.test(email)) errs.email = 'Invalid email address';
        if (!password) errs.password = 'Password is required';
        else if (password.length < 6) errs.password = 'Password must be at least 6 characters';
        if (password !== confirmPassword) errs.confirm = 'Passwords do not match';
        setErrors(errs);
        return Object.keys(errs).length === 0;
    }, [name, email, password, confirmPassword]);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!validate()) return;
        const success = await register(name, email, password);
        if (success) {
            router.replace('/dashboard/organizations');
        } else {
            setErrors({ general: 'An account with this email already exists.' });
        }
    };

    return (
        <div className="min-h-screen flex bg-gray-50">
            {/* Left Panel - Branding */}
            <div className="hidden lg:flex lg:w-1/2 bg-gradient-to-br from-primary-600 via-primary-700 to-primary-900 p-12 flex-col justify-between relative overflow-hidden">
                <div className="absolute inset-0 opacity-10">
                    <div className="absolute top-20 left-20 w-72 h-72 bg-white dark:bg-gray-950 rounded-full blur-3xl" />
                    <div className="absolute bottom-20 right-20 w-96 h-96 bg-primary-300 rounded-full blur-3xl" />
                </div>
                <div className="relative z-10">
                    <div className="flex items-center gap-3 mb-2">
                        <div className="w-10 h-10 bg-white dark:bg-gray-950/20 backdrop-blur rounded-xl flex items-center justify-center">
                            <span className="text-white font-bold text-lg">M</span>
                        </div>
                        <span className="text-white font-bold text-2xl">MigrationStudio</span>
                    </div>
                </div>
                <div className="relative z-10">
                    <h1 className="text-4xl font-bold text-white leading-tight mb-6">
                        Join the future of<br />Application Migration
                    </h1>
                    <ul className="space-y-4 text-primary-100 italic">
                        <li className="flex items-start gap-2">
                            <CheckCircleIcon className="h-5 w-5 text-primary-300 mt-0.5" />
                            <span>Transform legacy Mule flows to serverless AWS Lambda</span>
                        </li>
                        <li className="flex items-start gap-2">
                            <CheckCircleIcon className="h-5 w-5 text-primary-300 mt-0.5" />
                            <span>Automated code conversion with AI-driven intelligence</span>
                        </li>
                        <li className="flex items-start gap-2">
                            <CheckCircleIcon className="h-5 w-5 text-primary-300 mt-0.5" />
                            <span>End-to-end workspace and project lifecycle management</span>
                        </li>
                    </ul>
                </div>
                <div className="relative z-10 flex items-center gap-8 text-primary-200 text-sm">
                    <p>© 2026 MigrationStudio. All rights reserved.</p>
                </div>
            </div>

            {/* Right Panel - Form */}
            <div className="flex-1 flex items-center justify-center p-8">
                <div className="w-full max-w-md animate-fade-in-up">
                    <div className="lg:hidden flex items-center gap-2 mb-8">
                        <div className="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center">
                            <span className="text-white font-bold text-sm">M</span>
                        </div>
                        <span className="font-bold text-lg text-gray-900 dark:text-gray-100">MigrationStudio</span>
                    </div>

                    <h2 className="text-3xl font-extrabold text-gray-900 dark:text-gray-100 tracking-tight">Create your account</h2>
                    <p className="text-gray-500 dark:text-gray-400 mt-2 mb-8">Start your migration journey today</p>

                    {errors.general && (
                        <div className="mb-6 p-4 bg-error-50 border border-error-100 rounded-xl flex items-center gap-3 text-error-700 text-sm slide-in">
                            <span className="font-medium">{errors.general}</span>
                        </div>
                    )}

                    <form onSubmit={handleSubmit} className="space-y-4">
                        <div className="grid grid-cols-2 gap-4 mb-6">
                            <button
                                type="button"
                                onClick={() => signIn('google')}
                                className="flex items-center justify-center gap-2 px-4 py-2.5 border border-gray-300 rounded-xl text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-all shadow-sm active:scale-[0.98]"
                            >
                                <svg className="w-4 h-4" viewBox="0 0 24 24">
                                    <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
                                    <path d="M12 23c2.97 0 5.46-.98 7.28-2.64l-3.57-2.77c-1.01.69-2.31 1.12-3.71 1.12-2.85 0-5.27-1.92-6.13-4.51H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
                                    <path d="M5.87 14.2c-.22-.69-.35-1.45-.35-2.2s.13-1.51.35-2.2V7.04H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.96l3.69-2.84z" fill="#FBBC05" />
                                    <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.04l3.69 2.84c.86-2.59 3.28-4.51 6.13-4.51z" fill="#EA4335" />
                                </svg>
                                Google
                            </button>
                            <button
                                type="button"
                                onClick={() => signIn('apple')}
                                className="flex items-center justify-center gap-2 px-4 py-2.5 border border-gray-300 rounded-xl text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 transition-all shadow-sm active:scale-[0.98]"
                            >
                                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M17.05 20.28c-.96.95-2.04 1.87-3.21 1.9-1.15.02-1.58-.69-2.91-.69-1.31 0-1.8.67-2.91.71-1.15.03-2.35-.97-3.32-1.92-1.98-1.96-3.41-5.59-1.39-9.1.99-1.74 2.8-2.85 4.76-2.88 1.49-.02 2.65.88 3.51.88.85 0 2.29-1.11 4.07-.93 1.1.04 2.11.41 2.89 1.14-.14.1-.14.11-1.3.83-1.13.73-1.63 2.09-1.22 3.38.35 1.11 1.34 1.83 2.51 1.76.1-.21.21-.42.27-.64-1.29 2.14-1.19 3.86-1.96 5.56M13.25 3.5c.82-.99.57-2.61.35-3.5 1.43.14 2.76 1.45 2.27 3.5-.95-.08-2.2-.42-2.62-1.18z" />
                                </svg>
                                Apple
                            </button>
                        </div>

                        <div className="relative mb-6">
                            <div className="absolute inset-0 flex items-center">
                                <div className="w-full border-t border-gray-200"></div>
                            </div>
                            <div className="relative flex justify-center text-sm">
                                <span className="px-2 bg-white text-gray-500">Or use email</span>
                            </div>
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 font-semibold">Full Name</label>
                            <input
                                type="text"
                                value={name}
                                onChange={e => { setName(e.target.value); setErrors(p => ({ ...p, name: undefined })); }}
                                className={`w-full px-4 py-3 rounded-xl border ${errors.name ? 'border-error-500 bg-error-50' : 'border-gray-300'} text-sm focus:ring-4 focus:ring-primary-500/10 focus:border-primary-500 outline-none transition-all shadow-sm`}
                                placeholder="Enter your full name"
                            />
                            {errors.name && <p className="text-error-500 text-xs mt-1.5 ml-1">{errors.name}</p>}
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 font-semibold">Email address</label>
                            <input
                                type="email"
                                value={email}
                                onChange={e => { setEmail(e.target.value); setErrors(p => ({ ...p, email: undefined })); }}
                                className={`w-full px-4 py-3 rounded-xl border ${errors.email ? 'border-error-500 bg-error-50' : 'border-gray-300'} text-sm focus:ring-4 focus:ring-primary-500/10 focus:border-primary-500 outline-none transition-all shadow-sm`}
                                placeholder="you@company.com"
                            />
                            {errors.email && <p className="text-error-500 text-xs mt-1.5 ml-1">{errors.email}</p>}
                        </div>

                        <div className="grid grid-cols-2 gap-4">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 font-semibold">Password</label>
                                <div className="relative">
                                    <input
                                        type={showPassword ? 'text' : 'password'}
                                        value={password}
                                        onChange={e => { setPassword(e.target.value); setErrors(p => ({ ...p, password: undefined })); }}
                                        className={`w-full px-4 py-3 pr-10 rounded-xl border ${errors.password ? 'border-error-500 bg-error-50' : 'border-gray-300'} text-sm focus:ring-4 focus:ring-primary-500/10 focus:border-primary-500 outline-none transition-all shadow-sm`}
                                        placeholder="••••••••"
                                    />
                                    <button
                                        type="button"
                                        onClick={() => setShowPassword(!showPassword)}
                                        className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 dark:text-gray-400 transition-colors"
                                    >
                                        {showPassword ? <EyeSlashIcon className="h-4 w-4" /> : <EyeIcon className="h-4 w-4" />}
                                    </button>
                                </div>
                                {errors.password && <p className="text-error-500 text-xs mt-1.5 ml-1">{errors.password}</p>}
                            </div>
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 font-semibold">Confirm</label>
                                <input
                                    type="password"
                                    value={confirmPassword}
                                    onChange={e => { setConfirmPassword(e.target.value); setErrors(p => ({ ...p, confirm: undefined })); }}
                                    className={`w-full px-4 py-3 rounded-xl border ${errors.confirm ? 'border-error-500 bg-error-50' : 'border-gray-300'} text-sm focus:ring-4 focus:ring-primary-500/10 focus:border-primary-500 outline-none transition-all shadow-sm`}
                                    placeholder="••••••••"
                                />
                                {errors.confirm && <p className="text-error-500 text-xs mt-1.5 ml-1">{errors.confirm}</p>}
                            </div>
                        </div>

                        <button
                            type="submit"
                            disabled={isLoading}
                            className="w-full mt-4 py-3.5 bg-primary-600 hover:bg-primary-700 disabled:bg-primary-400 text-white font-bold text-sm rounded-xl transition-all flex items-center justify-center gap-2 shadow-lg shadow-primary-500/20 active:scale-[0.98]"
                        >
                            {isLoading ? (
                                <>
                                    <svg className="animate-spin h-5 w-5 text-white" fill="none" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" /><path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" /></svg>
                                    Creating account...
                                </>
                            ) : 'Create free account'}
                        </button>
                    </form>

                    <p className="text-center text-sm text-gray-500 dark:text-gray-400 mt-8">
                        Already have an account?{' '}
                        <a href="/login" className="font-bold text-primary-600 hover:text-primary-700 transition-colors">Sign In</a>
                    </p>
                </div>
            </div>
        </div>
    );
}
