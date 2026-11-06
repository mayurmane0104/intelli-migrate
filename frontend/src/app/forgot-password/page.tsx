'use client';

import React, { useState } from 'react';

export default function ForgotPasswordPage() {
    const [email, setEmail] = useState('');
    const [sent, setSent] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!email || !/\S+@\S+\.\S+/.test(email)) {
            setError('Please enter a valid email address');
            return;
        }
        setIsLoading(true);
        await new Promise(r => setTimeout(r, 1500));
        setSent(true);
        setIsLoading(false);
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 p-4">
            <div className="w-full max-w-md">
                <div className="flex items-center gap-2 mb-8 justify-center">
                    <div className="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center">
                        <span className="text-white font-bold text-sm">M</span>
                    </div>
                    <span className="font-bold text-lg text-gray-900 dark:text-gray-100">MigrationStudio</span>
                </div>

                {sent ? (
                    <div className="bg-white dark:bg-gray-950 rounded-xl shadow-sm border border-gray-200 dark:border-gray-800 p-8 text-center">
                        <div className="w-16 h-16 bg-success-50 rounded-full flex items-center justify-center mx-auto mb-4">
                            <svg className="h-8 w-8 text-success-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
                        </div>
                        <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">Check your email</h2>
                        <p className="text-gray-500 dark:text-gray-400 text-sm mb-6">
                            We&apos;ve sent a password reset link to <strong>{email}</strong>
                        </p>
                        <a href="/login" className="text-primary-600 hover:text-primary-700 font-medium text-sm">
                            ← Back to Sign In
                        </a>
                    </div>
                ) : (
                    <div className="bg-white dark:bg-gray-950 rounded-xl shadow-sm border border-gray-200 dark:border-gray-800 p-8">
                        <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-1">Forgot your password?</h2>
                        <p className="text-gray-500 dark:text-gray-400 text-sm mb-6">Enter your email and we&apos;ll send you a reset link.</p>
                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Email address</label>
                                <input type="email" value={email}
                                    onChange={e => { setEmail(e.target.value); setError(''); }}
                                    className={`w-full px-4 py-2.5 rounded-lg border ${error ? 'border-error-500' : 'border-gray-300'} text-sm focus:ring-2 focus:ring-primary-500 focus:border-primary-500 outline-none`}
                                    placeholder="you@company.com" />
                                {error && <p className="text-error-500 text-xs mt-1">{error}</p>}
                            </div>
                            <button type="submit" disabled={isLoading}
                                className="w-full py-2.5 bg-primary-600 hover:bg-primary-700 disabled:bg-primary-400 text-white font-medium text-sm rounded-lg transition-colors flex items-center justify-center gap-2">
                                {isLoading ? 'Sending...' : 'Send Reset Link'}
                            </button>
                        </form>
                        <p className="text-center text-sm text-gray-500 dark:text-gray-400 mt-6">
                            <a href="/login" className="font-medium text-primary-600 hover:text-primary-700">← Back to Sign In</a>
                        </p>
                    </div>
                )}
            </div>
        </div>
    );
}
