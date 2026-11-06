'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { useApp } from '@/contexts/AppContext';
import {
    UserIcon,
    ShieldCheckIcon,
    KeyIcon,
    EnvelopeIcon,
} from '@heroicons/react/24/outline';

export default function ProfilePage() {
    const { user, updateProfile, updatePassword } = useAuth();
    const { addToast } = useApp();

    // Profile state
    const [displayName, setDisplayName] = useState(user?.name || '');
    const [email] = useState(user?.email || '');
    const [isSaving, setIsSaving] = useState(false);

    const [currentPassword, setCurrentPassword] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    // Sync user data when it loads async
    useEffect(() => {
        if (user) {
            setDisplayName(user.name || '');
        }
    }, [user]);

    const handleSaveProfile = async (e: React.FormEvent) => {
        e.preventDefault();
        setIsSaving(true);
        const success = await updateProfile({ name: displayName });
        setIsSaving(false);
        addToast(success
            ? { type: 'success', title: 'Profile Updated', message: 'Your profile settings have been saved successfully.' }
            : { type: 'error', title: 'Error', message: 'Failed to update profile.' }
        );
    };

    const handleChangePassword = async (e: React.FormEvent) => {
        e.preventDefault();
        if (newPassword !== confirmPassword) {
            addToast({ type: 'error', title: 'Error', message: 'Passwords do not match.' });
            return;
        }
        const success = await updatePassword(currentPassword, newPassword);
        if (success) {
            addToast({ type: 'success', title: 'Password Changed', message: 'Your password has been updated.' });
            setCurrentPassword(''); setNewPassword(''); setConfirmPassword('');
        } else {
            addToast({ type: 'error', title: 'Error', message: 'Current password is incorrect.' });
        }
    };

    const initials = user?.name ? user.name.split(' ').map(n => n[0]).join('').toUpperCase() : 'U';

    return (
        <div className="animate-fade-in p-6 max-w-4xl mx-auto">
            <div className="mb-8">
                <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">Account Settings</h1>
                <p className="text-gray-500 dark:text-gray-400 text-sm">Manage your profile, preferences, and AI provider settings.</p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Left: Summary & Avatar */}
                <div className="space-y-6">
                    <section className="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 p-6 flex flex-col items-center text-center">
                        <div className="w-24 h-24 bg-primary-100 rounded-full flex items-center justify-center mb-4 text-primary-700 text-3xl font-bold">
                            {initials}
                        </div>
                        <h2 className="text-lg font-bold text-gray-900 dark:text-gray-100">{user?.name}</h2>
                        <p className="text-sm text-gray-500 dark:text-gray-400 mb-4">{user?.email}</p>
                        <span className="px-3 py-1 bg-primary-50 text-primary-700 text-xs font-semibold rounded-full capitalize">
                            {user?.role}
                        </span>
                    </section>

                    <nav className="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 overflow-hidden">
                        <button className="w-full flex items-center gap-3 px-4 py-3 text-sm font-medium text-primary-600 bg-primary-50 dark:bg-primary-900/30 border-l-4 border-primary-600">
                            <UserIcon className="h-5 w-5" /> Profile Details
                        </button>
                        <button className="w-full flex items-center gap-3 px-4 py-3 text-sm font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-900 border-l-4 border-transparent transition-colors">
                            <ShieldCheckIcon className="h-5 w-5" /> Security
                        </button>
                    </nav>
                </div>

                {/* Right: Forms */}
                <div className="lg:col-span-2 space-y-8">
                    {/* Profile Details */}
                    <section className="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 overflow-hidden">
                        <div className="px-6 py-4 border-b border-gray-100 dark:border-gray-800 bg-gray-50/50">
                            <h3 className="font-semibold text-gray-900 dark:text-gray-100">Profile Information</h3>
                        </div>
                        <form onSubmit={handleSaveProfile} className="p-6 space-y-4">
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Full Name</label>
                                    <div className="relative">
                                        <UserIcon className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400" />
                                        <input type="text" value={displayName} onChange={e => setDisplayName(e.target.value)}
                                            className="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 text-sm focus:ring-2 focus:ring-primary-500 outline-none" />
                                    </div>
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Email Address</label>
                                    <div className="relative">
                                        <EnvelopeIcon className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400" />
                                        <input type="email" disabled value={email}
                                            className="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-200 dark:border-gray-800 bg-gray-50 text-sm text-gray-500 dark:text-gray-400 outline-none cursor-not-allowed" />
                                    </div>
                                </div>
                            </div>
                            <div className="pt-4 border-t border-gray-100 dark:border-gray-800 flex justify-end">
                                <button type="submit" disabled={isSaving}
                                    className="px-6 py-2 bg-primary-600 hover:bg-primary-700 disabled:bg-primary-400 text-white text-sm font-medium rounded-lg transition-colors">
                                    {isSaving ? 'Saving...' : 'Save Changes'}
                                </button>
                            </div>
                        </form>
                    </section>

                    {/* Security */}
                    <section className="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 overflow-hidden">
                        <div className="px-6 py-4 border-b border-gray-100 dark:border-gray-800 bg-gray-50/50">
                            <h3 className="font-semibold text-gray-900 dark:text-gray-100">Security</h3>
                        </div>
                        <form onSubmit={handleChangePassword} className="p-6 space-y-4">
                            <div>
                                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Current Password</label>
                                <div className="relative">
                                    <KeyIcon className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400" />
                                    <input type="password" value={currentPassword} onChange={e => setCurrentPassword(e.target.value)}
                                        placeholder="••••••••"
                                        className="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 text-sm focus:ring-2 focus:ring-primary-500 outline-none" />
                                </div>
                            </div>
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">New Password</label>
                                    <input type="password" value={newPassword} onChange={e => setNewPassword(e.target.value)}
                                        placeholder="Min. 8 characters"
                                        className="w-full px-4 py-2 rounded-lg border border-gray-300 text-sm focus:ring-2 focus:ring-primary-500 outline-none" />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Confirm New Password</label>
                                    <input type="password" value={confirmPassword} onChange={e => setConfirmPassword(e.target.value)}
                                        placeholder="Repeat new password"
                                        className="w-full px-4 py-2 rounded-lg border border-gray-300 text-sm focus:ring-2 focus:ring-primary-500 outline-none" />
                                </div>
                            </div>
                            <div className="pt-4 flex justify-end">
                                <button type="submit"
                                    className="px-6 py-2 bg-gray-900 hover:bg-black text-white text-sm font-medium rounded-lg transition-colors">
                                    Update Password
                                </button>
                            </div>
                        </form>
                    </section>
                </div>
            </div>
        </div>
    );
}
