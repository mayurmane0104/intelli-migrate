'use client';

import React, { useCallback } from 'react';
import { usePathname, useRouter } from 'next/navigation';
import { useAuth } from '@/contexts/AuthContext';
import { useApp } from '@/contexts/AppContext';
import {
    HomeIcon,
    Cog6ToothIcon,
    ChartPieIcon,
    CommandLineIcon,
    ClockIcon,
    AdjustmentsHorizontalIcon,
    ArrowRightStartOnRectangleIcon,
    ChevronLeftIcon,
    ChevronRightIcon,
    SparklesIcon,
    BuildingOffice2Icon,
    CloudIcon,
} from '@heroicons/react/24/outline';
import {
    HomeIcon as HomeSolid,
    Cog6ToothIcon as CogSolid,
    ChartPieIcon as ChartSolid,
    CommandLineIcon as TerminalSolid,
    ClockIcon as ClockSolid,
    AdjustmentsHorizontalIcon as AdjustSolid,
} from '@heroicons/react/24/solid';

export default function Sidebar() {
    const { user, logout } = useAuth();
    const { selectedOrg, selectedWorkspace, selectedProject, sidebarCollapsed, toggleSidebar } = useApp();
    const router = useRouter();
    const pathname = usePathname();

    const isProjectPath = pathname.includes('/dashboard/projects/');
    const pId = selectedProject?.id;

    const isActive = (href: string, pattern?: RegExp): boolean => {
        if (pattern) return pattern.test(pathname);
        if (href === `/dashboard/projects/${pId}`) {
            return pathname === href || new RegExp(`/dashboard/projects/${pId}$`).test(pathname);
        }
        return pathname.startsWith(href);
    };

    const handleLogout = useCallback(() => {
        logout();
        router.replace('/login');
    }, [logout, router]);

    const projectNavItems = pId ? [
        {
            href: `/dashboard/projects/${pId}`,
            label: 'Overview',
            icon: ChartPieIcon,
            iconActive: ChartSolid,
            pattern: new RegExp(`^/dashboard/projects/${pId}$`),
        },
        {
            href: `/dashboard/projects/${pId}/editor`,
            label: 'Code Editor',
            icon: CommandLineIcon,
            iconActive: TerminalSolid,
            badge: selectedProject?.status === 'in-progress' ? 'Live' : undefined,
        },
        {
            href: `/dashboard/projects/${pId}/history`,
            label: 'History',
            icon: ClockIcon,
            iconActive: ClockSolid,
        },
        {
            href: `/dashboard/projects/${pId}/settings`,
            label: 'Project Setup',
            icon: AdjustmentsHorizontalIcon,
            iconActive: AdjustSolid,
        },
    ] : [];

    const platformNavItems = [
        {
            href: '/dashboard/organizations',
            label: 'Home',
            icon: HomeIcon,
            iconActive: HomeSolid,
        },
        {
            href: '/dashboard/sap-onboarding',
            label: 'SAP Target Setup',
            icon: CloudIcon,
            iconActive: CloudIcon,
        },
        {
            href: '/dashboard/settings',
            label: 'Global Control',
            icon: Cog6ToothIcon,
            iconActive: CogSolid,
        },
    ];

    const initials = user?.name
        ? user.name.trim().split(/\s+/).map((n: string) => n[0]).join('').slice(0, 2).toUpperCase()
        : 'U';

    return (
        <aside className={`flex flex-col h-full bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 transition-all duration-300 ease-in-out shrink-0 ${sidebarCollapsed ? 'w-[68px]' : 'w-[240px]'}`}>

            {/* ── Brand Header ── */}
            <div className={`flex items-center h-16 border-b border-gray-100 dark:border-gray-800 shrink-0 ${sidebarCollapsed ? 'justify-center px-3' : 'justify-between px-4'}`}>
                {!sidebarCollapsed && (
                    <div className="flex items-center gap-2.5 min-w-0">
                        <div className="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center shrink-0 shadow-sm">
                            <SparklesIcon className="h-4 w-4 text-white" />
                        </div>
                        <div className="min-w-0">
                            <span className="text-sm font-bold text-gray-900 dark:text-gray-100 truncate block leading-tight">MigrationStudio</span>
                            <span className="text-[10px] text-gray-400 font-medium">v2.4 PRO</span>
                        </div>
                    </div>
                )}
                {sidebarCollapsed && (
                    <div className="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center shadow-sm">
                        <SparklesIcon className="h-4 w-4 text-white" />
                    </div>
                )}
                {!sidebarCollapsed && (
                    <button onClick={toggleSidebar} className="p-1.5 rounded-lg text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors" title="Collapse sidebar">
                        <ChevronLeftIcon className="h-4 w-4" />
                    </button>
                )}
            </div>

            {/* ── Context Breadcrumb ── */}
            {!sidebarCollapsed && (
                <div className="px-3 py-3 border-b border-gray-100 dark:border-gray-800 bg-gray-50/50 dark:bg-gray-800/30">
                    <div className="flex flex-col gap-1">
                        {selectedOrg ? (
                            <button onClick={() => router.push(`/dashboard/workspaces/${selectedOrg.id}`)} className="flex items-center gap-1.5 text-xs text-gray-500 dark:text-gray-400 hover:text-primary-600 transition-colors truncate text-left">
                                <BuildingOffice2Icon className="h-3 w-3 shrink-0" />
                                <span className="truncate">{selectedOrg.name}</span>
                            </button>
                        ) : selectedProject ? (
                            /* Derivation fallback if org not yet loaded in state */
                            <div className="flex items-center gap-1.5 text-xs text-gray-400 truncate text-left">
                                <BuildingOffice2Icon className="h-3 w-3 shrink-0" />
                                <span className="truncate italic">Syncing Org...</span>
                            </div>
                        ) : (
                            <span className="text-xs text-gray-400 italic">No organization</span>
                        )}
                        
                        {(selectedWorkspace || selectedProject) && (
                            <button 
                                onClick={() => {
                                    const oId = selectedOrg?.id || selectedProject?.orgId;
                                    const wId = selectedWorkspace?.id || selectedProject?.workspaceId;
                                    if (oId && wId) router.push(`/dashboard/workspaces/${oId}/${wId}/projects`);
                                }} 
                                className="flex items-center gap-1.5 text-xs text-gray-500 dark:text-gray-400 hover:text-primary-600 transition-colors truncate ml-1 text-left"
                            >
                                <ChevronRightIcon className="h-2.5 w-2.5 shrink-0" />
                                <span className="truncate">{selectedWorkspace?.name || 'Workspace'}</span>
                                {selectedWorkspace?.environment && (
                                    <span className={`px-1.5 py-0.5 text-[9px] font-semibold rounded-full border ${selectedWorkspace.environment === 'prod' ? 'bg-green-50 text-green-700 border-green-200' : selectedWorkspace.environment === 'test' ? 'bg-amber-50 text-amber-700 border-amber-200' : 'bg-blue-50 text-blue-700 border-blue-200'}`}>
                                        {selectedWorkspace.environment}
                                    </span>
                                )}
                            </button>
                        )}
                        {selectedProject && (
                            <div className="flex items-center gap-1.5 text-xs font-semibold text-gray-800 dark:text-gray-200 ml-2 truncate">
                                <ChevronRightIcon className="h-2.5 w-2.5 shrink-0 text-gray-400" />
                                <span className="truncate">{selectedProject.name}</span>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* Collapsed expand button */}
            {sidebarCollapsed && (
                <button onClick={toggleSidebar} className="mx-auto my-2 p-1.5 rounded-lg text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors" title="Expand sidebar">
                    <ChevronRightIcon className="h-4 w-4" />
                </button>
            )}

            {/* ── Navigation ── */}
            <nav className="flex-1 overflow-y-auto py-2 px-2">
                {/* Project Section */}
                {pId && (
                    <div className="mb-6">
                        {!sidebarCollapsed && (
                            <p className="px-2 py-1 text-[10px] font-semibold text-gray-400 uppercase tracking-widest mb-1">Project Selection</p>
                        )}
                        <ul className="space-y-0.5">
                            {projectNavItems.map((item) => {
                                const active = isActive(item.href, (item as any).pattern);
                                const Icon = active ? item.iconActive : item.icon;
                                return (
                                    <li key={item.href} className="relative">
                                        <a
                                            href={item.href}
                                            title={sidebarCollapsed ? item.label : undefined}
                                            className={`flex items-center gap-3 rounded-lg px-2.5 py-2 text-sm font-medium transition-all ${active ? 'bg-primary-50 dark:bg-primary-900/30 text-primary-700 dark:text-primary-400' : 'text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-800'} ${sidebarCollapsed ? 'justify-center' : ''}`}
                                        >
                                            {sidebarCollapsed && active && (
                                                <span className="absolute left-0 top-1/2 -translate-y-1/2 w-0.5 h-5 bg-primary-600 rounded-r-full" />
                                            )}
                                            <Icon className={`h-5 w-5 shrink-0 ${active ? 'text-primary-600 dark:text-primary-400' : ''}`} />
                                            {!sidebarCollapsed && (
                                                <>
                                                    <span className="flex-1 truncate">{item.label}</span>
                                                    {(item as any).badge && (
                                                        <span className="px-1.5 py-0.5 text-[9px] font-bold rounded-full bg-primary-100 text-primary-700 dark:bg-primary-900/50 dark:text-primary-300 animate-pulse">
                                                            {(item as any).badge}
                                                        </span>
                                                    )}
                                                </>
                                            )}
                                        </a>
                                    </li>
                                );
                            })}
                        </ul>
                    </div>
                )}

                {/* Platform/System Section */}
                <div className="mb-2">
                    {!sidebarCollapsed && (
                        <p className="px-2 py-1 text-[10px] font-semibold text-gray-400 uppercase tracking-widest mb-1">Platform Control</p>
                    )}
                    <ul className="space-y-0.5">
                        {platformNavItems.map((item) => {
                            const active = isActive(item.href, (item as any).pattern);
                            const Icon = active ? item.iconActive : item.icon;
                            return (
                                <li key={item.href} className="relative">
                                    <a
                                        href={item.href}
                                        title={sidebarCollapsed ? item.label : undefined}
                                        className={`flex items-center gap-3 rounded-lg px-2.5 py-2 text-sm font-medium transition-all ${active ? 'bg-primary-50 dark:bg-primary-900/30 text-primary-700 dark:text-primary-400' : 'text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-800'} ${sidebarCollapsed ? 'justify-center' : ''}`}
                                    >
                                        {sidebarCollapsed && active && (
                                            <span className="absolute left-0 top-1/2 -translate-y-1/2 w-0.5 h-5 bg-primary-600 rounded-r-full" />
                                        )}
                                        <Icon className={`h-5 w-5 shrink-0 ${active ? 'text-primary-600 dark:text-primary-400' : ''}`} />
                                        {!sidebarCollapsed && (
                                            <>
                                                <span className="flex-1 truncate">{item.label}</span>
                                            </>
                                        )}
                                    </a>
                                </li>
                            );
                        })}
                    </ul>
                </div>

                {!sidebarCollapsed && isProjectPath && selectedOrg && (
                    <div className="mt-4 pt-4 border-t border-gray-100 dark:border-gray-800">
                        <p className="px-2 py-1 text-[10px] font-semibold text-gray-400 uppercase tracking-widest mb-1">Navigation</p>
                        <button onClick={() => router.push('/dashboard/organizations')} className="flex items-center gap-3 rounded-lg px-2.5 py-2 text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-800 transition-all w-full text-left">
                            <HomeIcon className="h-5 w-5 shrink-0" />
                            <span className="truncate">Organization HUB</span>
                        </button>
                    </div>
                )}
            </nav>

            {/* ── User Footer ── */}
            <div className="border-t border-gray-100 dark:border-gray-800 p-2 shrink-0">
                <div className={`flex items-center gap-2.5 rounded-lg p-2 ${sidebarCollapsed ? 'justify-center' : ''}`}>
                    <div className="w-7 h-7 bg-primary-100 dark:bg-primary-900/50 rounded-full flex items-center justify-center shrink-0">
                        <span className="text-primary-700 dark:text-primary-300 font-bold text-xs">{initials}</span>
                    </div>
                    {!sidebarCollapsed && (
                        <>
                            <div className="flex-1 min-w-0">
                                <p className="text-xs font-semibold text-gray-800 dark:text-gray-200 truncate leading-tight">{user?.name}</p>
                                <p className="text-[10px] text-gray-400 truncate capitalize">{user?.role}</p>
                            </div>
                            <button onClick={handleLogout} className="p-1.5 text-gray-400 hover:text-error-600 hover:bg-error-50 dark:hover:bg-error-900/20 rounded-lg transition-colors" title="Sign out">
                                <ArrowRightStartOnRectangleIcon className="h-4 w-4" />
                            </button>
                        </>
                    )}
                </div>
            </div>
        </aside>
    );
}
