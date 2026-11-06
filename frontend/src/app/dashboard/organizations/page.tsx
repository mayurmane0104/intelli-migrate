'use client';

import React, { useState, useMemo, useCallback } from 'react';
import { useApp } from '@/contexts/AppContext';
import { useRouter } from 'next/navigation';
import Modal from '@/components/ui/Modal';
import { useDebounce } from '@/lib/hooks';
import {
    MagnifyingGlassIcon,
    PlusIcon,
    BuildingOffice2Icon,
    UserIcon,
    CalendarIcon,
    Square3Stack3DIcon,
    ArrowRightIcon,
    Squares2X2Icon,
    ListBulletIcon,
} from '@heroicons/react/24/outline';

const ORG_COLORS = [
    'from-violet-500 to-purple-700',
    'from-blue-500 to-indigo-700',
    'from-emerald-500 to-teal-700',
    'from-orange-500 to-red-600',
    'from-pink-500 to-rose-600',
    'from-cyan-500 to-blue-600',
];

function getOrgColor(name: string) {
    const idx = name.charCodeAt(0) % ORG_COLORS.length;
    return ORG_COLORS[idx];
}

function getInitials(name: string) {
    return name.trim().split(/\s+/).map(w => w[0]).join('').slice(0, 2).toUpperCase();
}

export default function OrganizationsPage() {
    const { organizations, selectOrg, addOrganization, addToast } = useApp();
    const router = useRouter();
    const [search, setSearch] = useState('');
    const [sortBy, setSortBy] = useState<'name' | 'date'>('name');
    const [viewMode, setViewMode] = useState<'grid' | 'list'>('grid');
    const [showCreate, setShowCreate] = useState(false);
    const [newOrg, setNewOrg] = useState({ name: '', description: '', owner: '', logo: '' });
    const [createError, setCreateError] = useState('');

    const debouncedSearch = useDebounce(search, 300);

    const filtered = useMemo(() => {
        let items = organizations.filter(o =>
            o.name.toLowerCase().includes(debouncedSearch.toLowerCase()) ||
            o.description.toLowerCase().includes(debouncedSearch.toLowerCase())
        );
        items.sort((a, b) => sortBy === 'name'
            ? a.name.localeCompare(b.name)
            : b.createdAt.localeCompare(a.createdAt)
        );
        return items;
    }, [organizations, debouncedSearch, sortBy]);

    const totalWorkspaces = useMemo(
        () => organizations.reduce((s, o) => s + o.workspaceCount, 0),
        [organizations]
    );

    const handleCreate = useCallback(async () => {
        if (!newOrg.name.trim()) { setCreateError('Organization name is required'); return; }
        if (organizations.some(o => o.name.toLowerCase() === newOrg.name.toLowerCase())) {
            setCreateError('An organization with this name already exists'); return;
        }
        const created = await addOrganization({ ...newOrg, owner: 'Current User' });
        if (!created) return;
        addToast({ type: 'success', title: 'Organization Created', message: `${newOrg.name} has been created successfully.` });
        setShowCreate(false);
        setNewOrg({ name: '', description: '', owner: '', logo: '' });
        setCreateError('');
    }, [newOrg, organizations, addOrganization, addToast]);

    const handleOrgClick = useCallback((org: typeof organizations[0]) => {
        selectOrg(org);
        router.push(`/dashboard/workspaces/${org.id}`);
    }, [selectOrg, router]);

    return (
        <div className="min-h-full bg-gray-50/50 dark:bg-gray-950">
            {/* ── Hero Header ── */}
            <div className="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 px-6 py-6">
                <div className="flex items-start justify-between gap-4">
                    <div>
                        <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">Organizations</h1>
                        <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">Manage your organizations and migration workspaces</p>
                    </div>
                    <button
                        onClick={() => setShowCreate(true)}
                        className="flex items-center gap-2 px-4 py-2.5 bg-primary-600 hover:bg-primary-700 text-white text-sm font-semibold rounded-xl transition-colors shadow-sm shadow-primary-500/30 shrink-0">
                        <PlusIcon className="h-4 w-4" />
                        New Organization
                    </button>
                </div>

                {/* Stats Row */}
                <div className="flex items-center gap-6 mt-5 pt-4 border-t border-gray-100 dark:border-gray-800">
                    <div className="flex items-center gap-2">
                        <div className="w-8 h-8 bg-primary-50 dark:bg-primary-900/30 rounded-lg flex items-center justify-center">
                            <BuildingOffice2Icon className="h-4 w-4 text-primary-600" />
                        </div>
                        <div>
                            <p className="text-lg font-bold text-gray-900 dark:text-gray-100 leading-tight">{organizations.length}</p>
                            <p className="text-xs text-gray-400">Organizations</p>
                        </div>
                    </div>
                    <div className="w-px h-8 bg-gray-200 dark:bg-gray-800" />
                    <div className="flex items-center gap-2">
                        <div className="w-8 h-8 bg-emerald-50 dark:bg-emerald-900/20 rounded-lg flex items-center justify-center">
                            <Square3Stack3DIcon className="h-4 w-4 text-emerald-600" />
                        </div>
                        <div>
                            <p className="text-lg font-bold text-gray-900 dark:text-gray-100 leading-tight">{totalWorkspaces}</p>
                            <p className="text-xs text-gray-400">Total Workspaces</p>
                        </div>
                    </div>
                </div>
            </div>

            <div className="p-6">
                {/* Filter Bar */}
                <div className="flex items-center gap-3 mb-6">
                    <div className="relative flex-1 max-w-sm">
                        <MagnifyingGlassIcon className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400" />
                        <input
                            type="text"
                            value={search}
                            onChange={e => setSearch(e.target.value)}
                            placeholder="Search organizations..."
                            className="w-full pl-9 pr-4 py-2.5 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-xl text-sm text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary-500 focus:border-primary-500 outline-none"
                        />
                    </div>
                    <select
                        value={sortBy}
                        onChange={e => setSortBy(e.target.value as 'name' | 'date')}
                        className="px-3 py-2.5 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-xl text-sm text-gray-700 dark:text-gray-300 focus:ring-2 focus:ring-primary-500 outline-none cursor-pointer">
                        <option value="name">Sort by Name</option>
                        <option value="date">Sort by Date</option>
                    </select>
                    <div className="flex items-center gap-1 p-1 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-xl">
                        <button
                            onClick={() => setViewMode('grid')}
                            className={`p-1.5 rounded-lg transition-colors ${viewMode === 'grid' ? 'bg-primary-100 text-primary-700 dark:bg-primary-900/50 dark:text-primary-300' : 'text-gray-400 hover:text-gray-600'}`}>
                            <Squares2X2Icon className="h-4 w-4" />
                        </button>
                        <button
                            onClick={() => setViewMode('list')}
                            className={`p-1.5 rounded-lg transition-colors ${viewMode === 'list' ? 'bg-primary-100 text-primary-700 dark:bg-primary-900/50 dark:text-primary-300' : 'text-gray-400 hover:text-gray-600'}`}>
                            <ListBulletIcon className="h-4 w-4" />
                        </button>
                    </div>
                    {search && (
                        <p className="text-sm text-gray-400 shrink-0">
                            {filtered.length} result{filtered.length !== 1 ? 's' : ''}
                        </p>
                    )}
                </div>

                {/* Empty State */}
                {filtered.length === 0 && (
                    <div className="flex flex-col items-center justify-center py-20 bg-white dark:bg-gray-900 rounded-2xl border border-dashed border-gray-300 dark:border-gray-700">
                        <div className="w-16 h-16 bg-gray-100 dark:bg-gray-800 rounded-2xl flex items-center justify-center mb-4">
                            <BuildingOffice2Icon className="h-8 w-8 text-gray-300 dark:text-gray-600" />
                        </div>
                        <p className="text-base font-semibold text-gray-700 dark:text-gray-300 mb-1">
                            {search ? 'No organizations found' : 'No organizations yet'}
                        </p>
                        <p className="text-sm text-gray-400 mb-6">
                            {search ? `Nothing matches "${search}"` : 'Create your first organization to get started'}
                        </p>
                        {!search && (
                            <button
                                onClick={() => setShowCreate(true)}
                                className="flex items-center gap-2 px-5 py-2.5 bg-primary-600 hover:bg-primary-700 text-white text-sm font-semibold rounded-xl transition-colors">
                                <PlusIcon className="h-4 w-4" />
                                Create Organization
                            </button>
                        )}
                    </div>
                )}

                {/* Grid View */}
                {filtered.length > 0 && viewMode === 'grid' && (
                    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
                        {filtered.map(org => {
                            const gradient = getOrgColor(org.name);
                            const initials = getInitials(org.name);
                            return (
                                <div
                                    key={org.id}
                                    onClick={() => handleOrgClick(org)}
                                    className="group bg-white dark:bg-gray-900 rounded-2xl border border-gray-200 dark:border-gray-800 p-5 hover:shadow-lg hover:shadow-gray-200/60 dark:hover:shadow-gray-900/60 hover:border-primary-200 dark:hover:border-primary-800 transition-all cursor-pointer">
                                    {/* Card top */}
                                    <div className="flex items-start gap-4 mb-4">
                                        <div className={`w-12 h-12 bg-gradient-to-br ${gradient} rounded-xl flex items-center justify-center shrink-0 shadow-sm`}>
                                            <span className="text-white font-bold text-sm">{initials}</span>
                                        </div>
                                        <div className="flex-1 min-w-0">
                                            <h3 className="font-bold text-gray-900 dark:text-gray-100 group-hover:text-primary-700 dark:group-hover:text-primary-400 transition-colors truncate text-base">
                                                {org.name}
                                            </h3>
                                            <p className="text-xs text-gray-400 truncate mt-0.5 leading-relaxed">
                                                {org.description || 'No description'}
                                            </p>
                                        </div>
                                    </div>

                                    {/* Stats row */}
                                    <div className="flex items-center gap-4 text-xs text-gray-500 dark:text-gray-400 py-3 border-t border-gray-100 dark:border-gray-800">
                                        <span className="flex items-center gap-1.5">
                                            <UserIcon className="h-3.5 w-3.5" />
                                            {org.owner}
                                        </span>
                                        <span className="flex items-center gap-1.5">
                                            <Square3Stack3DIcon className="h-3.5 w-3.5" />
                                            {org.workspaceCount} workspace{org.workspaceCount !== 1 ? 's' : ''}
                                        </span>
                                        <span className="flex items-center gap-1.5 ml-auto">
                                            <CalendarIcon className="h-3.5 w-3.5" />
                                            {org.createdAt}
                                        </span>
                                    </div>

                                    {/* CTA */}
                                    <div className="flex items-center justify-between mt-3">
                                        <div className="flex gap-1">
                                            {Array.from({ length: Math.min(org.workspaceCount, 4) }).map((_, i) => (
                                                <div key={i} className="w-5 h-5 rounded-full bg-gray-200 dark:bg-gray-700 border-2 border-white dark:border-gray-900 flex items-center justify-center text-[8px] text-gray-500">
                                                    {i + 1}
                                                </div>
                                            ))}
                                            {org.workspaceCount > 4 && (
                                                <div className="w-5 h-5 rounded-full bg-primary-100 dark:bg-primary-900/40 border-2 border-white dark:border-gray-900 flex items-center justify-center text-[8px] text-primary-600">
                                                    +{org.workspaceCount - 4}
                                                </div>
                                            )}
                                        </div>
                                        <span className="flex items-center gap-1 text-xs font-semibold text-primary-600 dark:text-primary-400 opacity-0 group-hover:opacity-100 transition-opacity">
                                            View workspaces <ArrowRightIcon className="h-3.5 w-3.5" />
                                        </span>
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                )}

                {/* List View */}
                {filtered.length > 0 && viewMode === 'list' && (
                    <div className="bg-white dark:bg-gray-900 rounded-2xl border border-gray-200 dark:border-gray-800 overflow-hidden">
                        <div className="grid grid-cols-[auto_1fr_160px_140px_120px_40px] items-center px-5 py-3 border-b border-gray-100 dark:border-gray-800 bg-gray-50 dark:bg-gray-800/50">
                            <div className="w-10" />
                            <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider pl-3">Organization</span>
                            <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Owner</span>
                            <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Workspaces</span>
                            <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Created</span>
                            <span />
                        </div>
                        {filtered.map((org, idx) => {
                            const gradient = getOrgColor(org.name);
                            const initials = getInitials(org.name);
                            return (
                                <div
                                    key={org.id}
                                    onClick={() => handleOrgClick(org)}
                                    className={`grid grid-cols-[auto_1fr_160px_140px_120px_40px] items-center px-5 py-3.5 hover:bg-primary-50/40 dark:hover:bg-primary-900/10 transition-colors cursor-pointer group ${idx < filtered.length - 1 ? 'border-b border-gray-100 dark:border-gray-800' : ''}`}>
                                    <div className={`w-9 h-9 bg-gradient-to-br ${gradient} rounded-lg flex items-center justify-center shrink-0`}>
                                        <span className="text-white font-bold text-xs">{initials}</span>
                                    </div>
                                    <div className="pl-3 min-w-0">
                                        <p className="text-sm font-semibold text-gray-900 dark:text-gray-100 group-hover:text-primary-700 truncate transition-colors">{org.name}</p>
                                        <p className="text-xs text-gray-400 truncate mt-0.5">{org.description}</p>
                                    </div>
                                    <div className="text-sm text-gray-500 dark:text-gray-400 flex items-center gap-1.5">
                                        <UserIcon className="h-3.5 w-3.5 shrink-0" />
                                        <span className="truncate">{org.owner}</span>
                                    </div>
                                    <div className="text-sm text-gray-500 dark:text-gray-400 flex items-center gap-1.5">
                                        <Square3Stack3DIcon className="h-3.5 w-3.5 shrink-0" />
                                        {org.workspaceCount}
                                    </div>
                                    <div className="text-sm text-gray-400 flex items-center gap-1.5">
                                        <CalendarIcon className="h-3.5 w-3.5 shrink-0" />
                                        {org.createdAt}
                                    </div>
                                    <ArrowRightIcon className="h-4 w-4 text-gray-300 group-hover:text-primary-500 transition-colors" />
                                </div>
                            );
                        })}
                    </div>
                )}
            </div>

            {/* Create Organization Modal */}
            <Modal
                isOpen={showCreate}
                onClose={() => { setShowCreate(false); setCreateError(''); setNewOrg({ name: '', description: '', owner: '', logo: '' }); }}
                title="Create Organization"
                size="md">
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-1.5">
                            Organization Name <span className="text-red-500">*</span>
                        </label>
                        <input
                            type="text"
                            value={newOrg.name}
                            onChange={e => { setNewOrg(p => ({ ...p, name: e.target.value })); setCreateError(''); }}
                            onKeyDown={e => e.key === 'Enter' && handleCreate()}
                            autoFocus
                            className={`w-full px-4 py-2.5 rounded-xl border ${createError ? 'border-red-400 focus:ring-red-400' : 'border-gray-300 dark:border-gray-700'} text-sm bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary-500 focus:border-primary-500 outline-none transition-colors`}
                            placeholder="e.g. Acme Corporation"
                        />
                        {createError && <p className="text-red-500 text-xs mt-1.5 flex items-center gap-1">⚠ {createError}</p>}
                    </div>
                    <div>
                        <label className="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-1.5">Description</label>
                        <textarea
                            value={newOrg.description}
                            onChange={e => setNewOrg(p => ({ ...p, description: e.target.value }))}
                            rows={3}
                            className="w-full px-4 py-2.5 rounded-xl border border-gray-300 dark:border-gray-700 text-sm bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary-500 outline-none resize-none"
                            placeholder="What is this organization for?"
                        />
                    </div>
                    {newOrg.name && (
                        <div className="flex items-center gap-3 p-3 bg-gray-50 dark:bg-gray-800 rounded-xl">
                            <div className={`w-10 h-10 bg-gradient-to-br ${getOrgColor(newOrg.name)} rounded-lg flex items-center justify-center`}>
                                <span className="text-white font-bold text-sm">{getInitials(newOrg.name)}</span>
                            </div>
                            <div>
                                <p className="text-sm font-semibold text-gray-900 dark:text-gray-100">{newOrg.name}</p>
                                <p className="text-xs text-gray-400">Preview</p>
                            </div>
                        </div>
                    )}
                    <div className="flex gap-3 pt-1">
                        <button
                            onClick={() => { setShowCreate(false); setCreateError(''); }}
                            className="flex-1 px-4 py-2.5 text-sm font-semibold text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-900 border border-gray-300 dark:border-gray-700 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors">
                            Cancel
                        </button>
                        <button
                            onClick={handleCreate}
                            disabled={!newOrg.name.trim()}
                            className="flex-1 px-4 py-2.5 text-sm font-semibold text-white bg-primary-600 hover:bg-primary-700 disabled:opacity-40 disabled:cursor-not-allowed rounded-xl transition-colors shadow-sm">
                            Create Organization
                        </button>
                    </div>
                </div>
            </Modal>
        </div>
    );
}
