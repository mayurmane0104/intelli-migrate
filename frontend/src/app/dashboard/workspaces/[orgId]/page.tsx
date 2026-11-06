'use client';

import React, { useState } from 'react';
import { useApp } from '@/contexts/AppContext';
import { useRouter } from 'next/navigation';
import Modal from '@/components/ui/Modal';
import {
    Square3Stack3DIcon,
    UserGroupIcon,
    FolderIcon,
    ChevronRightIcon,
    PlusIcon,
    TrashIcon,
    ExclamationTriangleIcon,
    BuildingOffice2Icon,
    ArrowRightIcon,
    ServerStackIcon,
    BeakerIcon,
    RocketLaunchIcon,
} from '@heroicons/react/24/outline';

const ENV_CONFIG: Record<string, {
    label: string;
    badge: string;
    icon: React.ElementType;
    gradient: string;
    ring: string;
}> = {
    dev: {
        label: 'Development',
        badge: 'bg-blue-50 text-blue-700 border border-blue-200 dark:bg-blue-900/30 dark:text-blue-300 dark:border-blue-800',
        icon: BeakerIcon,
        gradient: 'from-blue-500 to-indigo-600',
        ring: 'hover:border-blue-300 dark:hover:border-blue-700',
    },
    test: {
        label: 'Testing',
        badge: 'bg-amber-50 text-amber-700 border border-amber-200 dark:bg-amber-900/30 dark:text-amber-300 dark:border-amber-800',
        icon: ServerStackIcon,
        gradient: 'from-amber-500 to-orange-600',
        ring: 'hover:border-amber-300 dark:hover:border-amber-700',
    },
    prod: {
        label: 'Production',
        badge: 'bg-emerald-50 text-emerald-700 border border-emerald-200 dark:bg-emerald-900/30 dark:text-emerald-300 dark:border-emerald-800',
        icon: RocketLaunchIcon,
        gradient: 'from-emerald-500 to-teal-600',
        ring: 'hover:border-emerald-300 dark:hover:border-emerald-700',
    },
};

export default function WorkspacesPage({ params }: { params: Promise<{ orgId: string }> }) {
    const { organizations, workspaces, selectOrg, selectWorkspace, selectedOrg, addWorkspace, addToast, refreshWorkspaces, deleteWorkspace } = useApp();
    const router = useRouter();
    const [showCreate, setShowCreate] = useState(false);
    const [newWs, setNewWs] = useState({ name: '', environment: 'dev' as 'dev' | 'test' | 'prod', memberCount: 1 });
    const [createError, setCreateError] = useState('');
    const [deleteTarget, setDeleteTarget] = useState<{ id: string; name: string } | null>(null);

    const resolvedParams = React.use(params);

    React.useEffect(() => {
        const org = organizations.find(o => o.id === resolvedParams.orgId);
        if (org && (!selectedOrg || selectedOrg.id !== resolvedParams.orgId)) selectOrg(org);
    }, [resolvedParams.orgId, organizations]); // eslint-disable-line react-hooks/exhaustive-deps

    React.useEffect(() => {
        refreshWorkspaces(resolvedParams.orgId);
    }, [resolvedParams.orgId]); // eslint-disable-line react-hooks/exhaustive-deps

    const orgWorkspaces = workspaces.filter(w => w.orgId === resolvedParams.orgId);
    const org = organizations.find(o => o.id === resolvedParams.orgId);
    const totalProjects = orgWorkspaces.reduce((s, w) => s + w.projectCount, 0);
    const totalMembers = orgWorkspaces.reduce((s, w) => s + w.memberCount, 0);

    const handleDeleteClick = (e: React.MouseEvent, wsId: string, wsName: string, projectCount: number) => {
        e.stopPropagation();
        if (projectCount > 0) {
            addToast({
                type: 'error',
                title: 'Cannot Delete Workspace',
                message: `"${wsName}" has ${projectCount} project${projectCount !== 1 ? 's' : ''}. Delete all projects first.`,
            });
            return;
        }
        setDeleteTarget({ id: wsId, name: wsName });
    };

    const handleConfirmDelete = async () => {
        if (!deleteTarget) return;
        await deleteWorkspace(resolvedParams.orgId, deleteTarget.id);
        addToast({ type: 'success', title: 'Workspace Deleted', message: `"${deleteTarget.name}" has been removed.` });
        setDeleteTarget(null);
    };

    const handleCreate = () => {
        if (!newWs.name.trim()) { setCreateError('Workspace name is required'); return; }
        if (orgWorkspaces.some(w => w.name.toLowerCase() === newWs.name.toLowerCase())) {
            setCreateError('A workspace with this name already exists'); return;
        }
        addWorkspace({ orgId: resolvedParams.orgId, name: newWs.name.trim(), environment: newWs.environment, memberCount: newWs.memberCount });
        addToast({ type: 'success', title: 'Workspace Created', message: `${newWs.name} is ready.` });
        setShowCreate(false);
        setNewWs({ name: '', environment: 'dev', memberCount: 1 });
        setCreateError('');
    };

    return (
        <div className="min-h-full bg-gray-50/50 dark:bg-gray-950">
            {/* ── Header ── */}
            <div className="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 px-6 py-5">
                <nav className="flex items-center gap-2 text-xs text-gray-400 mb-3">
                    <button onClick={() => router.push('/dashboard/organizations')} className="hover:text-primary-600 transition-colors flex items-center gap-1">
                        <BuildingOffice2Icon className="h-3.5 w-3.5" />
                        Organizations
                    </button>
                    <ChevronRightIcon className="h-3 w-3" />
                    <span className="text-gray-700 dark:text-gray-300 font-medium">{org?.name}</span>
                </nav>

                <div className="flex items-start justify-between gap-4">
                    <div>
                        <h1 className="text-xl font-bold text-gray-900 dark:text-gray-100">Workspaces</h1>
                        <p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5">
                            {org?.name} — organize projects by environment
                        </p>
                    </div>
                    <button
                        onClick={() => setShowCreate(true)}
                        className="flex items-center gap-2 px-4 py-2.5 bg-primary-600 hover:bg-primary-700 text-white text-sm font-semibold rounded-xl transition-colors shadow-sm shrink-0">
                        <PlusIcon className="h-4 w-4" /> New Workspace
                    </button>
                </div>

                {/* Stats */}
                {orgWorkspaces.length > 0 && (
                    <div className="flex items-center gap-6 mt-4 pt-4 border-t border-gray-100 dark:border-gray-800">
                        <div className="flex items-center gap-2 text-sm">
                            <Square3Stack3DIcon className="h-4 w-4 text-gray-400" />
                            <span className="font-bold text-gray-900 dark:text-gray-100">{orgWorkspaces.length}</span>
                            <span className="text-gray-400">workspaces</span>
                        </div>
                        <div className="flex items-center gap-2 text-sm">
                            <FolderIcon className="h-4 w-4 text-gray-400" />
                            <span className="font-bold text-gray-900 dark:text-gray-100">{totalProjects}</span>
                            <span className="text-gray-400">projects</span>
                        </div>
                        <div className="flex items-center gap-2 text-sm">
                            <UserGroupIcon className="h-4 w-4 text-gray-400" />
                            <span className="font-bold text-gray-900 dark:text-gray-100">{totalMembers}</span>
                            <span className="text-gray-400">members</span>
                        </div>
                    </div>
                )}
            </div>

            <div className="p-6">
                {/* Empty State */}
                {orgWorkspaces.length === 0 && (
                    <div className="flex flex-col items-center justify-center py-20 bg-white dark:bg-gray-900 rounded-2xl border border-dashed border-gray-300 dark:border-gray-700">
                        <div className="w-16 h-16 bg-gray-100 dark:bg-gray-800 rounded-2xl flex items-center justify-center mb-4">
                            <Square3Stack3DIcon className="h-8 w-8 text-gray-300 dark:text-gray-600" />
                        </div>
                        <p className="text-base font-semibold text-gray-700 dark:text-gray-300 mb-1">No workspaces yet</p>
                        <p className="text-sm text-gray-400 mb-6">Create your first workspace to start organizing projects</p>
                        <button
                            onClick={() => setShowCreate(true)}
                            className="flex items-center gap-2 px-5 py-2.5 bg-primary-600 hover:bg-primary-700 text-white text-sm font-semibold rounded-xl transition-colors">
                            <PlusIcon className="h-4 w-4" /> Create Workspace
                        </button>
                    </div>
                )}

                {/* Workspace Cards */}
                {orgWorkspaces.length > 0 && (
                    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
                        {orgWorkspaces.map(ws => {
                            const env = ENV_CONFIG[ws.environment] || ENV_CONFIG.dev;
                            const EnvIcon = env.icon;
                            return (
                                <div
                                    key={ws.id}
                                    onClick={() => { selectWorkspace(ws); router.push(`/dashboard/workspaces/${resolvedParams.orgId}/${ws.id}/projects`); }}
                                    className={`group bg-white dark:bg-gray-900 rounded-2xl border border-gray-200 dark:border-gray-800 ${env.ring} hover:shadow-lg hover:shadow-gray-200/50 dark:hover:shadow-gray-900/50 transition-all cursor-pointer overflow-hidden`}>
                                    {/* Color bar */}
                                    <div className={`h-1 bg-gradient-to-r ${env.gradient}`} />

                                    <div className="p-5">
                                        {/* Header */}
                                        <div className="flex items-start justify-between mb-4">
                                            <div className="flex items-center gap-3 flex-1 min-w-0">
                                                <div className={`w-11 h-11 bg-gradient-to-br ${env.gradient} rounded-xl flex items-center justify-center shrink-0 shadow-sm`}>
                                                    <EnvIcon className="h-5 w-5 text-white" />
                                                </div>
                                                <div className="min-w-0">
                                                    <h3 className="font-bold text-gray-900 dark:text-gray-100 group-hover:text-primary-700 dark:group-hover:text-primary-400 truncate transition-colors">
                                                        {ws.name}
                                                    </h3>
                                                    <span className={`inline-flex items-center mt-1 px-2 py-0.5 text-xs font-semibold rounded-full ${env.badge}`}>
                                                        {env.label}
                                                    </span>
                                                </div>
                                            </div>
                                            <button
                                                onClick={e => handleDeleteClick(e, ws.id, ws.name, ws.projectCount)}
                                                title={ws.projectCount > 0 ? `Delete all ${ws.projectCount} project(s) first` : 'Delete workspace'}
                                                className={`ml-2 p-1.5 rounded-lg transition-all opacity-0 group-hover:opacity-100 shrink-0 ${ws.projectCount > 0 ? 'text-gray-300 dark:text-gray-600 cursor-not-allowed' : 'text-gray-400 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20'}`}>
                                                {ws.projectCount > 0
                                                    ? <ExclamationTriangleIcon className="h-4 w-4" />
                                                    : <TrashIcon className="h-4 w-4" />}
                                            </button>
                                        </div>

                                        {/* Stats */}
                                        <div className="grid grid-cols-2 gap-3">
                                            <div className="bg-gray-50 dark:bg-gray-800/50 rounded-xl p-3 text-center">
                                                <p className="text-xl font-bold text-gray-900 dark:text-gray-100">{ws.projectCount}</p>
                                                <p className="text-xs text-gray-400 flex items-center justify-center gap-1">
                                                    <FolderIcon className="h-3 w-3" /> Projects
                                                </p>
                                            </div>
                                            <div className="bg-gray-50 dark:bg-gray-800/50 rounded-xl p-3 text-center">
                                                <p className="text-xl font-bold text-gray-900 dark:text-gray-100">{ws.memberCount}</p>
                                                <p className="text-xs text-gray-400 flex items-center justify-center gap-1">
                                                    <UserGroupIcon className="h-3 w-3" /> Members
                                                </p>
                                            </div>
                                        </div>

                                        {/* CTA */}
                                        <div className="mt-4 flex items-center justify-between">
                                            {ws.projectCount > 0 && (
                                                <p className="text-xs text-amber-600 dark:text-amber-400 flex items-center gap-1">
                                                    <ExclamationTriangleIcon className="h-3.5 w-3.5" />
                                                    Remove projects to delete
                                                </p>
                                            )}
                                            <span className="ml-auto flex items-center gap-1 text-xs font-semibold text-primary-600 dark:text-primary-400 opacity-0 group-hover:opacity-100 transition-opacity">
                                                Open <ArrowRightIcon className="h-3.5 w-3.5" />
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                )}
            </div>

            {/* Create Workspace Modal */}
            <Modal
                isOpen={showCreate}
                onClose={() => { setShowCreate(false); setCreateError(''); setNewWs({ name: '', environment: 'dev', memberCount: 1 }); }}
                title="Create Workspace"
                size="md">
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-1.5">
                            Workspace Name <span className="text-red-500">*</span>
                        </label>
                        <input
                            type="text"
                            value={newWs.name}
                            autoFocus
                            onChange={e => { setNewWs(p => ({ ...p, name: e.target.value })); setCreateError(''); }}
                            onKeyDown={e => e.key === 'Enter' && handleCreate()}
                            className={`w-full px-4 py-2.5 rounded-xl border ${createError ? 'border-red-400' : 'border-gray-300 dark:border-gray-700'} text-sm bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary-500 outline-none`}
                            placeholder="e.g. Development"
                        />
                        {createError && <p className="text-red-500 text-xs mt-1.5">⚠ {createError}</p>}
                    </div>

                    <div>
                        <label className="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">Environment</label>
                        <div className="grid grid-cols-3 gap-3">
                            {(['dev', 'test', 'prod'] as const).map(env => {
                                const cfg = ENV_CONFIG[env];
                                const EnvIcon = cfg.icon;
                                return (
                                    <label key={env} className={`flex flex-col items-center gap-1.5 p-3 rounded-xl border-2 cursor-pointer transition-all ${newWs.environment === env ? 'border-primary-500 bg-primary-50 dark:bg-primary-900/20' : 'border-gray-200 dark:border-gray-700 hover:border-primary-300'}`}>
                                        <input type="radio" name="environment" value={env} checked={newWs.environment === env}
                                            onChange={() => setNewWs(p => ({ ...p, environment: env }))} className="hidden" />
                                        <div className={`w-8 h-8 bg-gradient-to-br ${cfg.gradient} rounded-lg flex items-center justify-center`}>
                                            <EnvIcon className="h-4 w-4 text-white" />
                                        </div>
                                        <span className="text-xs font-semibold text-gray-700 dark:text-gray-300">{cfg.label}</span>
                                    </label>
                                );
                            })}
                        </div>
                    </div>

                    <div>
                        <label className="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-1.5">Initial Members</label>
                        <input
                            type="number"
                            value={newWs.memberCount}
                            min={1}
                            max={50}
                            onChange={e => setNewWs(p => ({ ...p, memberCount: parseInt(e.target.value) || 1 }))}
                            className="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-700 text-sm bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary-500 outline-none"
                        />
                    </div>

                    <div className="flex gap-3 pt-1">
                        <button
                            onClick={() => { setShowCreate(false); setCreateError(''); }}
                            className="flex-1 px-4 py-2.5 text-sm font-semibold text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-900 border border-gray-300 dark:border-gray-700 rounded-xl hover:bg-gray-50 transition-colors">
                            Cancel
                        </button>
                        <button
                            onClick={handleCreate}
                            disabled={!newWs.name.trim()}
                            className="flex-1 px-4 py-2.5 text-sm font-semibold text-white bg-primary-600 hover:bg-primary-700 disabled:bg-primary-300 disabled:cursor-not-allowed rounded-xl transition-colors">
                            Create Workspace
                        </button>
                    </div>
                </div>
            </Modal>

            {/* Delete Confirmation Modal */}
            <Modal
                isOpen={!!deleteTarget}
                onClose={() => setDeleteTarget(null)}
                title="Delete Workspace"
                size="sm">
                <div className="space-y-4">
                    <div className="flex items-start gap-3 p-4 bg-red-50 dark:bg-red-900/20 rounded-xl border border-red-200 dark:border-red-800">
                        <ExclamationTriangleIcon className="h-5 w-5 text-red-500 shrink-0 mt-0.5" />
                        <p className="text-sm text-red-700 dark:text-red-300">
                            Are you sure you want to delete <strong>&quot;{deleteTarget?.name}&quot;</strong>? This action cannot be undone.
                        </p>
                    </div>
                    <div className="flex gap-3">
                        <button
                            onClick={() => setDeleteTarget(null)}
                            className="flex-1 px-4 py-2.5 text-sm font-semibold text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-900 border border-gray-300 dark:border-gray-700 rounded-xl hover:bg-gray-50 transition-colors">
                            Cancel
                        </button>
                        <button
                            onClick={handleConfirmDelete}
                            className="flex-1 px-4 py-2.5 text-sm font-semibold text-white bg-red-600 hover:bg-red-700 rounded-xl transition-colors">
                            Delete Workspace
                        </button>
                    </div>
                </div>
            </Modal>
        </div>
    );
}