'use client';

import React, { Fragment, useState, useEffect, useCallback } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { useApp } from '@/contexts/AppContext';
import { useRouter } from 'next/navigation';
import { Menu, MenuButton, MenuItems, MenuItem, Transition } from '@headlessui/react';
import {
    Bars3Icon,
    BellIcon,
    ChevronDownIcon,
    ChevronRightIcon,
    ArrowRightStartOnRectangleIcon,
    Cog6ToothIcon,
    UserCircleIcon,
    QuestionMarkCircleIcon,
    XMarkIcon,
    CheckCircleIcon,
    ExclamationTriangleIcon,
    InformationCircleIcon,
    HomeIcon,
} from '@heroicons/react/24/outline';
import UserButton from '../ui/UserButton';

interface Notification {
    id: string;
    title: string;
    message: string;
    type: 'success' | 'warning' | 'info';
    time: string;
    read: boolean;
}

const initialNotifications: Notification[] = [
    { id: 'n1', title: 'Migration Complete', message: 'Customer Data Sync project migration finished successfully.', type: 'success', time: '2 hours ago', read: false },
    { id: 'n2', title: 'New Team Member', message: 'Sarah Chen joined the Acme Corporation organization.', type: 'info', time: '5 hours ago', read: false },
    { id: 'n3', title: 'Migration Warning', message: 'Payment Gateway has 3 files with unsupported constructs.', type: 'warning', time: '1 day ago', read: true },
    { id: 'n4', title: 'System Update', message: 'MigrationStudio v2.4 is now available with improved DWL support.', type: 'info', time: '2 days ago', read: true },
];

const notifIcons: Record<string, React.ElementType> = {
    success: CheckCircleIcon,
    warning: ExclamationTriangleIcon,
    info: InformationCircleIcon,
};
const notifColors: Record<string, string> = {
    success: 'text-success-500',
    warning: 'text-warning-500',
    info: 'text-primary-500',
};

export default function Topbar() {
    const { user, logout } = useAuth();
    const { selectedOrg, selectedWorkspace, selectedProject, toggleSidebar } = useApp();

    const router = useRouter();
    const [mounted, setMounted] = useState(false);
    const [showNotifications, setShowNotifications] = useState(false);
    const [notifications, setNotifications] = useState<Notification[]>(initialNotifications);
    useEffect(() => setMounted(true), []);

    const unreadCount = notifications.filter(n => !n.read).length;

    const markAllRead = useCallback(() => {
        setNotifications(prev => prev.map(n => ({ ...n, read: true })));
    }, []);

    const markRead = useCallback((id: string) => {
        setNotifications(prev => prev.map(n => n.id === id ? { ...n, read: true } : n));
    }, []);

    const handleLogout = useCallback(() => {
        logout();
        router.replace('/login');
    }, [logout, router]);

    const handleProfile = useCallback(() => {
        router.push('/dashboard/profile');
    }, [router]);

    const handleSettings = useCallback(() => {
        router.push('/dashboard/settings');
    }, [router]);

    return (
        <header className="h-16 bg-white dark:bg-gray-950 border-b border-gray-200 dark:border-gray-800 flex items-center justify-between px-4 lg:px-6 shrink-0 z-30">
            {/* Left */}
            <div className="flex items-center gap-4">
                <button onClick={toggleSidebar}
                    className="p-2 rounded-lg hover:bg-gray-100 transition-colors lg:hidden"
                    aria-label="Toggle sidebar">
                    <Bars3Icon className="h-5 w-5 text-gray-600 dark:text-gray-400" />
                </button>


                {/* Breadcrumb */}
                <nav className="hidden sm:flex items-center gap-1.5 ml-4 text-sm" aria-label="Breadcrumb">
                    <button onClick={() => router.push('/dashboard/organizations')}
                        className="flex items-center gap-1 text-gray-400 hover:text-primary-600 transition-colors"
                        title="Organizations">
                        <HomeIcon className="h-4 w-4" />
                    </button>
                    {selectedOrg && (
                        <>
                            <ChevronRightIcon className="h-3.5 w-3.5 text-gray-300" />
                            <button onClick={() => router.push(`/dashboard/workspaces/${selectedOrg.id}`)}
                                className="text-gray-500 dark:text-gray-400 hover:text-primary-600 transition-colors max-w-[140px] truncate">
                                {selectedOrg.name}
                            </button>
                        </>
                    )}
                    {selectedWorkspace && selectedOrg && (
                        <>
                            <ChevronRightIcon className="h-3.5 w-3.5 text-gray-300" />
                            <button onClick={() => router.push(`/dashboard/workspaces/${selectedOrg.id}/${selectedWorkspace.id}/projects`)}
                                className="text-gray-500 dark:text-gray-400 hover:text-primary-600 transition-colors max-w-[120px] truncate">
                                {selectedWorkspace.name}
                            </button>
                        </>
                    )}
                    {selectedProject && (
                        <>
                            <ChevronRightIcon className="h-3.5 w-3.5 text-gray-300" />
                            <span className="text-gray-800 dark:text-gray-200 font-medium max-w-[160px] truncate">
                                {selectedProject.name}
                            </span>
                        </>
                    )}
                </nav>
            </div>

            {/* Right */}
            <div className="flex items-center gap-2">
                {/* Notification Bell */}
                <div className="flex items-center gap-3">
                    <a
                        href="/dashboard/help"
                        className="p-2 text-gray-400 hover:text-primary-600 hover:bg-gray-100 rounded-lg transition-all group relative"
                        title="Help Documentation"
                    >
                        <QuestionMarkCircleIcon className="h-6 w-6" />
                        <span className="absolute -top-1 -right-1 w-2 h-2 bg-primary-500 rounded-full border-2 border-white scale-0 group-hover:scale-100 transition-transform shadow-sm"></span>
                    </a>

                    <div className="relative">
                        <button
                            onClick={() => setShowNotifications(!showNotifications)}
                            className="p-2 text-gray-400 hover:text-primary-600 hover:bg-gray-100 rounded-lg transition-all relative"
                        >
                            <BellIcon className="h-5 w-5" />
                            {unreadCount > 0 && (
                                <span className="absolute top-1 right-1 w-4 h-4 bg-error-500 rounded-full text-[9px] font-bold text-white flex items-center justify-center">
                                    {unreadCount}
                                </span>
                            )}
                        </button>

                        {/* Notification Dropdown */}
                        {showNotifications && (
                            <>
                                <div className="fixed inset-0 z-40" onClick={() => setShowNotifications(false)} />
                                <div className="absolute right-0 top-full mt-2 w-80 bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-xl shadow-xl z-50 overflow-hidden">
                                    <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100 dark:border-gray-800 bg-gray-50/50">
                                        <h3 className="text-sm font-semibold text-gray-900 dark:text-gray-100">Notifications</h3>
                                        <div className="flex items-center gap-2">
                                            {unreadCount > 0 && (
                                                <button onClick={markAllRead}
                                                    className="text-[11px] text-primary-600 hover:text-primary-700 font-medium">
                                                    Mark all read
                                                </button>
                                            )}
                                            <button onClick={() => setShowNotifications(false)}
                                                className="p-0.5 rounded hover:bg-gray-200 transition-colors">
                                                <XMarkIcon className="h-4 w-4 text-gray-400" />
                                            </button>
                                        </div>
                                    </div>
                                    <div className="max-h-80 overflow-y-auto">
                                        {notifications.length === 0 ? (
                                            <div className="py-8 text-center text-gray-400 text-sm">No notifications</div>
                                        ) : (
                                            notifications.map(n => {
                                                const Icon = notifIcons[n.type];
                                                return (
                                                    <div key={n.id}
                                                        onClick={() => markRead(n.id)}
                                                        className={`flex gap-3 px-4 py-3 border-b border-gray-50 cursor-pointer hover:bg-gray-50 transition-colors ${!n.read ? 'bg-primary-50/30' : ''}`}>
                                                        <Icon className={`h-5 w-5 shrink-0 mt-0.5 ${notifColors[n.type]}`} />
                                                        <div className="flex-1 min-w-0">
                                                            <div className="flex items-center gap-2">
                                                                <span className={`text-sm ${!n.read ? 'font-semibold text-gray-900 dark:text-gray-100' : 'font-medium text-gray-700 dark:text-gray-300'}`}>{n.title}</span>
                                                                {!n.read && <span className="w-2 h-2 bg-primary-500 rounded-full shrink-0" />}
                                                            </div>
                                                            <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5 line-clamp-2">{n.message}</p>
                                                            <span className="text-[10px] text-gray-400 mt-1 block">{n.time}</span>
                                                        </div>
                                                    </div>
                                                );
                                            })
                                        )}
                                    </div>
                                </div>
                            </>
                        )}
                    </div>
                </div>

                {/* User Menu */}
                <UserButton />
            </div>
        </header>
    );
}
