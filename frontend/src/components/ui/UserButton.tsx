'use client';

import React, { Fragment } from 'react';
import { Menu, MenuButton, MenuItems, MenuItem, Transition } from '@headlessui/react';
import { useAuth } from '@/contexts/AuthContext';
import {
    UserCircleIcon,
    Cog6ToothIcon,
    ArrowRightStartOnRectangleIcon,
    ChevronDownIcon
} from '@heroicons/react/24/outline';
import { useRouter } from 'next/navigation';

export default function UserButton() {
    const { user, logout } = useAuth();
    const router = useRouter();

    if (!user) return null;

    const initials = user.name
        ? user.name.split(' ').map(n => n[0]).join('').toUpperCase()
        : 'U';

    return (
        <Menu as="div" className="relative">
            <MenuButton className="flex items-center gap-2 p-1.5 rounded-lg hover:bg-gray-100 transition-colors">
                <div className="w-8 h-8 bg-primary-100 dark:bg-primary-900/30 rounded-full flex items-center justify-center">
                    {user.avatar ? (
                        <img src={user.avatar} alt={user.name} className="w-full h-full rounded-full object-cover" />
                    ) : (
                        <span className="text-primary-700 dark:text-primary-400 font-semibold text-sm">
                            {initials}
                        </span>
                    )}
                </div>
                <span className="text-sm font-medium text-gray-700 dark:text-gray-300 hidden md:block">
                    {user.name}
                </span>
                <ChevronDownIcon className="h-4 w-4 text-gray-400 hidden md:block" />
            </MenuButton>

            <Transition
                as={Fragment}
                enter="transition ease-out duration-100"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="transition ease-in duration-75"
                leaveFrom="opacity-100 scale-100"
                leaveTo="opacity-0 scale-95"
            >
                <MenuItems className="absolute right-0 mt-2 w-56 bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-xl shadow-lg py-1 z-50">
                    <div className="px-4 py-3 border-b border-gray-100 dark:border-gray-800">
                        <p className="text-sm font-semibold text-gray-900 dark:text-gray-100">{user.name}</p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">{user.email}</p>
                        <span className="inline-block mt-1 px-2 py-0.5 text-xs font-medium bg-primary-50 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300 rounded-full capitalize">
                            {user.role}
                        </span>
                    </div>

                    <MenuItem>
                        {({ active }) => (
                            <button
                                onClick={() => router.push('/dashboard/profile')}
                                className={`flex items-center gap-2 w-full px-4 py-2.5 text-sm ${active ? 'bg-gray-50 dark:bg-gray-900' : ''
                                    } text-gray-700 dark:text-gray-300`}
                            >
                                <UserCircleIcon className="h-4 w-4" /> Profile
                            </button>
                        )}
                    </MenuItem>

                    <MenuItem>
                        {({ active }) => (
                            <button
                                onClick={() => router.push('/dashboard/settings')}
                                className={`flex items-center gap-2 w-full px-4 py-2.5 text-sm ${active ? 'bg-gray-50 dark:bg-gray-900' : ''
                                    } text-gray-700 dark:text-gray-300`}
                            >
                                <Cog6ToothIcon className="h-4 w-4" /> Settings
                            </button>
                        )}
                    </MenuItem>

                    <div className="border-t border-gray-100 dark:border-gray-800 mt-1">
                        <MenuItem>
                            {({ active }) => (
                                <button
                                    onClick={logout}
                                    className={`flex items-center gap-2 w-full px-4 py-2.5 text-sm ${active ? 'bg-error-50 dark:bg-error-900/20' : ''
                                        } text-error-600 dark:text-error-400`}
                                >
                                    <ArrowRightStartOnRectangleIcon className="h-4 w-4" /> Sign Out
                                </button>
                            )}
                        </MenuItem>
                    </div>
                </MenuItems>
            </Transition>
        </Menu>
    );
}
