'use client';

import React, { useState } from 'react';
import { EyeIcon, EyeSlashIcon } from '@heroicons/react/24/outline';

export default function ResetPasswordPage() {
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [done, setDone] = useState(false);
    const [errors, setErrors] = useState<Record<string, string>>({});

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const errs: Record<string, string> = {};
        if (!password) errs.password = 'Password is required';
        else if (password.length < 8) errs.password = 'Minimum 8 characters';
        if (password !== confirmPassword) errs.confirm = 'Passwords do not match';
        setErrors(errs);
        if (Object.keys(errs).length) return;
        setIsLoading(true);
        await new Promise(r => setTimeout(r, 1500));
        setDone(true);
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

                {done ? (
                    <div className="bg-white dark:bg-gray-950 rounded-xl shadow-sm border border-gray-200 dark:border-gray-800 p-8 text-center">
                        <div className="w-16 h-16 bg-success-50 rounded-full flex items-center justify-center mx-auto mb-4">
                            <svg className="h-8 w-8 text-success-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" /></svg>
                        </div>
                        <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">Password reset</h2>
                        <p className="text-gray-500 dark:text-gray-400 text-sm mb-6">Your password has been successfully reset.</p>
                        <a href="/login" className="inline-block px-6 py-2.5 bg-primary-600 hover:bg-primary-700 text-white font-medium text-sm rounded-lg transition-colors">
                            Sign In
                        </a>
                    </div>
                ) : (
                    <div className="bg-white dark:bg-gray-950 rounded-xl shadow-sm border border-gray-200 dark:border-gray-800 p-8">
                        <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-1">Reset your password</h2>
                        <p className="text-gray-500 dark:text-gray-400 text-sm mb-6">Enter your new password below.</p>
                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">New password</label>
                                <div className="relative">
                                    <input type={showPassword ? 'text' : 'password'} value={password}
                                        onChange={e => { setPassword(e.target.value); setErrors(p => ({ ...p, password: '' })); }}
                                        className={`w-full px-4 py-2.5 pr-10 rounded-lg border ${errors.password ? 'border-error-500' : 'border-gray-300'} text-sm focus:ring-2 focus:ring-primary-500 focus:border-primary-500 outline-none`}
                                        placeholder="Min 8 characters" />
                                    <button type="button" onClick={() => setShowPassword(!showPassword)} className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400">
                                        {showPassword ? <EyeSlashIcon className="h-4 w-4" /> : <EyeIcon className="h-4 w-4" />}
                                    </button>
                                </div>
                                {errors.password && <p className="text-error-500 text-xs mt-1">{errors.password}</p>}
                            </div>
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Confirm password</label>
                                <input type="password" value={confirmPassword}
                                    onChange={e => { setConfirmPassword(e.target.value); setErrors(p => ({ ...p, confirm: '' })); }}
                                    className={`w-full px-4 py-2.5 rounded-lg border ${errors.confirm ? 'border-error-500' : 'border-gray-300'} text-sm focus:ring-2 focus:ring-primary-500 focus:border-primary-500 outline-none`}
                                    placeholder="••••••••" />
                                {errors.confirm && <p className="text-error-500 text-xs mt-1">{errors.confirm}</p>}
                            </div>
                            <button type="submit" disabled={isLoading}
                                className="w-full py-2.5 bg-primary-600 hover:bg-primary-700 disabled:bg-primary-400 text-white font-medium text-sm rounded-lg transition-colors">
                                {isLoading ? 'Resetting...' : 'Reset Password'}
                            </button>
                        </form>
                    </div>
                )}
            </div>
        </div>
    );
}
