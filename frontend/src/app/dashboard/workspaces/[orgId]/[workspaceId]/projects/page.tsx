'use client';

import React, { useState, useMemo, useCallback } from 'react';
import { useApp } from '@/contexts/AppContext';
import { useRouter } from 'next/navigation';
import { useDebounce } from '@/lib/hooks';
import { PLATFORM_STRATEGIES, getPlatformStrategy } from '@/lib/platforms';
import type { TargetPlatform } from '@/lib/types';
import {
    FolderIcon,
    ChevronRightIcon,
    PlusIcon,
    CheckCircleIcon,
    ClockIcon,
    ExclamationCircleIcon,
    ArrowPathIcon,
    TrashIcon,
    MagnifyingGlassIcon,
    BuildingOffice2Icon,
    Square3Stack3DIcon,
    BoltIcon,
    Squares2X2Icon,
    ListBulletIcon,
    ArrowRightIcon,
} from '@heroicons/react/24/outline';

const statusConfig: Record<string, { color: string; dot: string; icon: React.ElementType; label: string }> = {
    pending: { color: 'bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400', dot: 'bg-gray-400', icon: ClockIcon, label: 'Pending' },
    'in-progress': { color: 'bg-blue-50 text-blue-700 dark:bg-blue-900/30 dark:text-blue-300', dot: 'bg-blue-500', icon: ArrowPathIcon, label: 'In Progress' },
    completed: { color: 'bg-emerald-50 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-300', dot: 'bg-emerald-500', icon: CheckCircleIcon, label: 'Completed' },
    failed: { color: 'bg-red-50 text-red-700 dark:bg-red-900/30 dark:text-red-300', dot: 'bg-red-500', icon: ExclamationCircleIcon, label: 'Failed' },
};

const ITEMS_PER_PAGE = 10;

export default function ProjectsPage({ params }: { params: Promise<{ orgId: string; workspaceId: string }> }) {
    const {
        organizations, workspaces, projects,
        selectWorkspace, selectProject, selectedWorkspace, selectedOrg, selectOrg,
        addProject, addToast, refreshProjects, refreshWorkspaces, deleteProject,
    } = useApp();
    const router = useRouter();
    const [showWizard, setShowWizard] = useState(false);
    const [step, setStep] = useState(1);
    const [viewMode, setViewMode] = useState<'list' | 'grid'>('list');
    const [wizardData, setWizardData] = useState({
        name: '', description: '', targetPlatform: 'aws' as TargetPlatform,
        migrationType: 'mule4-lambda' as any,
        targetRuntime: 'python' as any, sourceType: 'git' as const,
    });
    const [searchQuery, setSearchQuery] = useState('');
    const [currentPage, setCurrentPage] = useState(1);

    const debouncedSearch = useDebounce(searchQuery, 300);

    const resolvedParams = React.use(params);

    // Sync org + workspace selection from URL — not triggered by selectedOrg/selectedWorkspace state changes
    React.useEffect(() => {
        const org = organizations.find(o => o.id === resolvedParams.orgId);
        if (org && (!selectedOrg || selectedOrg.id !== resolvedParams.orgId)) selectOrg(org);
        const ws = workspaces.find(w => w.id === resolvedParams.workspaceId);
        if (ws && (!selectedWorkspace || selectedWorkspace.id !== resolvedParams.workspaceId)) selectWorkspace(ws);
    }, [resolvedParams.orgId, resolvedParams.workspaceId, organizations, workspaces]); // eslint-disable-line react-hooks/exhaustive-deps

    // Fetch data once per workspace — not re-triggered by selection state
    React.useEffect(() => {
        refreshWorkspaces(resolvedParams.orgId);
        refreshProjects(resolvedParams.workspaceId);
    }, [resolvedParams.orgId, resolvedParams.workspaceId]); // eslint-disable-line react-hooks/exhaustive-deps

    const wsProjects = projects.filter(p => p.workspaceId === resolvedParams.workspaceId);
    const org = organizations.find(o => o.id === resolvedParams.orgId);
    const ws = workspaces.find(w => w.id === resolvedParams.workspaceId);

    const filteredProjects = useMemo(() => {
        if (!debouncedSearch.trim()) return wsProjects;
        const q = debouncedSearch.toLowerCase();
        return wsProjects.filter(p =>
            p.name.toLowerCase().includes(q) || p.description.toLowerCase().includes(q)
        );
    }, [wsProjects, debouncedSearch]);

    const totalPages = Math.max(1, Math.ceil(filteredProjects.length / ITEMS_PER_PAGE));
    const paginatedProjects = filteredProjects.slice(
        (currentPage - 1) * ITEMS_PER_PAGE,
        currentPage * ITEMS_PER_PAGE
    );

    const [deleteTarget, setDeleteTarget] = useState<string | null>(null);

    const handleDelete = async () => {
        if (!deleteTarget) return;
        await deleteProject(deleteTarget);
        setDeleteTarget(null);
    };

    const handleCreate = async () => {
        if (!wizardData.name.trim()) return;
        setShowWizard(false);
        const created = await addProject({
            ...wizardData,
            sourceType: 'git',
            workspaceId: resolvedParams.workspaceId,
            orgId: resolvedParams.orgId,
        });
        setStep(1);
        setWizardData({ name: '', description: '', targetPlatform: 'aws', migrationType: 'mule4-lambda', targetRuntime: 'python', sourceType: 'git' });
        if (created) {
            selectProject(created);
            router.push(`/dashboard/projects/${created.id}`);
        } else {
            addToast({ type: 'error', title: 'Create Failed', message: 'Could not create project. Please try again.' });
        }
    };

    const stats = useMemo(() => ({
        total: wsProjects.length,
        inProgress: wsProjects.filter(p => p.status === 'in-progress').length,
        completed: wsProjects.filter(p => p.status === 'completed').length,
        failed: wsProjects.filter(p => p.status === 'failed').length,
        pending: wsProjects.filter(p => p.status === 'pending').length,
    }), [wsProjects]);

    const activeStrategy = getPlatformStrategy(wizardData.targetPlatform);
    const migrationTypes = activeStrategy.supportedMigrationTypes.map(m => ({ value: m.id, label: m.label, desc: m.desc }));
    const runtimes = activeStrategy.supportedRuntimes.map(r => ({ value: r.id, label: r.label }));

    return (
        <div className="animate-fade-in p-6">
            {/* Breadcrumb */}
            <nav className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-6">
                <button onClick={() => router.push('/dashboard/organizations')} className="hover:text-primary-600 transition-colors">Organizations</button>
                <ChevronRightIcon className="h-3.5 w-3.5" />
                <button onClick={() => router.push(`/dashboard/workspaces/${resolvedParams.orgId}`)} className="hover:text-primary-600 transition-colors">{org?.name}</button>
                <ChevronRightIcon className="h-3.5 w-3.5" />
                <span className="text-gray-900 dark:text-gray-100 font-medium">{ws?.name}</span>
            </nav>

            <div className="flex items-center justify-between mb-4">
                <div>
                    <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">Projects</h1>
                    <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
                        {wsProjects.length} project{wsProjects.length !== 1 ? 's' : ''} in <span className="font-medium text-gray-700 dark:text-gray-300">{ws?.name}</span>
                    </p>
                </div>
                <div className="flex items-center gap-3">
                    <div className="relative">
                        <MagnifyingGlassIcon className="h-4 w-4 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
                        <input
                            type="text"
                            placeholder="Search projects..."
                            value={searchQuery}
                            onChange={(e) => { setSearchQuery(e.target.value); setCurrentPage(1); }}
                            className="pl-9 pr-3 py-2 border border-gray-200 dark:border-gray-800 rounded-lg text-sm bg-white dark:bg-gray-950 focus:outline-none focus:ring-2 focus:ring-primary-500 text-gray-900 dark:text-gray-100 w-52"
                        />
                    </div>
                    {/* View toggle */}
                    <div className="flex items-center gap-1 bg-gray-100 dark:bg-gray-800 p-1 rounded-lg">
                        <button
                            onClick={() => setViewMode('list')}
                            className={`p-1.5 rounded transition-colors ${viewMode === 'list' ? 'bg-white dark:bg-gray-950 shadow text-primary-600' : 'text-gray-400 hover:text-gray-600'}`}
                            title="List view"
                        ><ListBulletIcon className="h-4 w-4" /></button>
                        <button
                            onClick={() => setViewMode('grid')}
                            className={`p-1.5 rounded transition-colors ${viewMode === 'grid' ? 'bg-white dark:bg-gray-950 shadow text-primary-600' : 'text-gray-400 hover:text-gray-600'}`}
                            title="Grid view"
                        ><Squares2X2Icon className="h-4 w-4" /></button>
                    </div>
                    <button
                        onClick={() => setShowWizard(true)}
                        className="flex items-center gap-2 px-4 py-2.5 bg-primary-600 hover:bg-primary-700 text-white text-sm font-medium rounded-lg transition-colors shadow-sm"
                    >
                        <PlusIcon className="h-4 w-4" /> New Project
                    </button>
                </div>
            </div>

            {/* Stats bar */}
            {wsProjects.length > 0 && (
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-6">
                    {[
                        { label: 'Total', value: stats.total, color: 'text-gray-700 dark:text-gray-200', bg: 'bg-white dark:bg-gray-950', Icon: Square3Stack3DIcon },
                        { label: 'In Progress', value: stats.inProgress, color: 'text-blue-600 dark:text-blue-400', bg: 'bg-blue-50 dark:bg-blue-900/20', Icon: ArrowPathIcon },
                        { label: 'Completed', value: stats.completed, color: 'text-emerald-600 dark:text-emerald-400', bg: 'bg-emerald-50 dark:bg-emerald-900/20', Icon: CheckCircleIcon },
                        { label: 'Failed', value: stats.failed, color: 'text-red-600 dark:text-red-400', bg: 'bg-red-50 dark:bg-red-900/20', Icon: ExclamationCircleIcon },
                    ].map(({ label, value, color, bg, Icon }) => (
                        <div key={label} className={`${bg} rounded-xl border border-gray-200 dark:border-gray-800 px-4 py-3 flex items-center gap-3`}>
                            <Icon className={`h-5 w-5 ${color} flex-shrink-0`} />
                            <div>
                                <p className={`text-lg font-bold ${color}`}>{value}</p>
                                <p className="text-xs text-gray-400">{label}</p>
                            </div>
                        </div>
                    ))}
                </div>
            )}

            {wsProjects.length === 0 ? (
                <div className="text-center py-20 bg-white dark:bg-gray-950 rounded-xl border border-dashed border-gray-200 dark:border-gray-800">
                    <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-primary-50 dark:bg-primary-900/20 mb-4">
                        <FolderIcon className="h-8 w-8 text-primary-400" />
                    </div>
                    <h3 className="text-gray-700 dark:text-gray-200 font-semibold text-lg mb-2">No projects yet</h3>
                    <p className="text-gray-400 text-sm mb-6">Get started by creating your first migration project</p>
                    <button onClick={() => setShowWizard(true)} className="inline-flex items-center gap-2 px-5 py-2.5 bg-primary-600 hover:bg-primary-700 text-white text-sm font-medium rounded-lg transition-colors shadow-sm">
                        <PlusIcon className="h-4 w-4" /> Create Project
                    </button>
                </div>
            ) : filteredProjects.length === 0 ? (
                <div className="text-center py-16 bg-white dark:bg-gray-950 rounded-xl border border-gray-200 dark:border-gray-800">
                    <MagnifyingGlassIcon className="h-8 w-8 text-gray-300 mx-auto mb-3" />
                    <p className="text-gray-500 dark:text-gray-400 font-medium">No results for &quot;{searchQuery}&quot;</p>
                    <p className="text-gray-400 text-sm mt-1">Try adjusting your search terms</p>
                </div>
            ) : (
                <>
                    {viewMode === 'list' ? (
                    /* ---- List View ---- */
                    <div className="bg-white dark:bg-gray-950 rounded-xl border border-gray-200 dark:border-gray-800 overflow-hidden">
                        <div className="grid grid-cols-[1fr_140px_120px_120px_160px_80px] items-center px-4 py-2.5 border-b border-gray-100 dark:border-gray-800 bg-gray-50 dark:bg-gray-900/60 text-xs font-semibold uppercase tracking-wider text-gray-400">
                            <span>Project</span>
                            <span>Status</span>
                            <span>Type</span>
                            <span>Runtime</span>
                            <span>Progress</span>
                            <span className="text-right">Actions</span>
                        </div>
                        {paginatedProjects.map((project, idx) => {
                            const status = statusConfig[project.status] || statusConfig.pending;
                            const StatusIcon = status.icon;
                            const progressPct = project.totalFiles > 0
                                ? Math.round((project.migratedFiles / project.totalFiles) * 100)
                                : 0;
                            return (
                                <div
                                    key={project.id}
                                    className={`grid grid-cols-[1fr_140px_120px_120px_160px_80px] items-center px-4 py-3.5 hover:bg-primary-50/40 dark:hover:bg-primary-900/10 transition-colors group cursor-pointer ${idx !== paginatedProjects.length - 1 ? 'border-b border-gray-100 dark:border-gray-800' : ''}`}
                                    onClick={() => { selectProject(project); router.push(`/dashboard/projects/${project.id}`); }}
                                >
                                    <div className="min-w-0 pr-4">
                                        <p className="font-semibold text-sm text-gray-900 dark:text-gray-100 group-hover:text-primary-700 truncate">{project.name}</p>
                                        <p className="text-xs text-gray-400 truncate mt-0.5">{project.description}</p>
                                        <p className="text-xs text-gray-300 dark:text-gray-600 mt-0.5">Updated {project.lastActivity}</p>
                                    </div>
                                    <div>
                                        <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-medium rounded-full ${status.color}`}>
                                            <span className={`w-1.5 h-1.5 rounded-full flex-shrink-0 ${status.dot}`} />
                                            {status.label}
                                        </span>
                                    </div>
                                    <div className="text-xs text-gray-500 dark:text-gray-400 truncate capitalize">
                                        {project.migrationType.replace('-', ' → ').replace('-', ' ')}
                                    </div>
                                    <div className="text-xs text-gray-500 dark:text-gray-400 capitalize">
                                        {project.targetRuntime}
                                    </div>
                                    <div className="pr-4">
                                        <div className="flex justify-between text-xs text-gray-400 mb-1">
                                            <span>{project.migratedFiles}/{project.totalFiles} files</span>
                                            <span className="font-medium">{progressPct}%</span>
                                        </div>
                                        <div className="w-full h-1.5 bg-gray-100 dark:bg-gray-800 rounded-full overflow-hidden">
                                            <div
                                                className={`h-full rounded-full transition-all ${project.status === 'completed' ? 'bg-emerald-500' : project.status === 'failed' ? 'bg-red-500' : 'bg-primary-500'}`}
                                                style={{ width: `${progressPct}%` }}
                                            />
                                        </div>
                                        {(project.migrationRuns ?? 0) > 0 && (
                                            <p className="text-xs text-violet-500 mt-1">{project.migrationRuns} run{project.migrationRuns !== 1 ? 's' : ''}</p>
                                        )}
                                    </div>
                                    <div className="flex justify-end">
                                        <button
                                            onClick={(e) => { e.stopPropagation(); setDeleteTarget(project.id); }}
                                            className="p-1.5 text-gray-300 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 rounded transition-colors opacity-0 group-hover:opacity-100"
                                            title="Delete project"
                                        >
                                            <TrashIcon className="h-4 w-4" />
                                        </button>
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                    ) : (
                    /* ---- Grid View ---- */
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                        {paginatedProjects.map((project) => {
                            const status = statusConfig[project.status] || statusConfig.pending;
                            const progressPct = project.totalFiles > 0
                                ? Math.round((project.migratedFiles / project.totalFiles) * 100)
                                : 0;
                            const gradients = [
                                'from-violet-500 to-purple-600',
                                'from-blue-500 to-cyan-500',
                                'from-emerald-500 to-teal-500',
                                'from-orange-500 to-amber-500',
                                'from-pink-500 to-rose-500',
                                'from-indigo-500 to-blue-600',
                            ];
                            const gradient = gradients[project.name.charCodeAt(0) % gradients.length];
                            return (
                                <div
                                    key={project.id}
                                    className="group bg-white dark:bg-gray-950 rounded-xl border border-gray-200 dark:border-gray-800 hover:border-primary-300 dark:hover:border-primary-700 hover:shadow-md transition-all cursor-pointer overflow-hidden"
                                    onClick={() => { selectProject(project); router.push(`/dashboard/projects/${project.id}`); }}
                                >
                                    <div className={`h-1.5 w-full bg-gradient-to-r ${gradient}`} />
                                    <div className="p-5">
                                        <div className="flex items-start justify-between mb-3">
                                            <div className={`w-10 h-10 rounded-xl bg-gradient-to-br ${gradient} flex items-center justify-center flex-shrink-0`}>
                                                <FolderIcon className="h-5 w-5 text-white" />
                                            </div>
                                            <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-medium rounded-full ${status.color}`}>
                                                <span className={`w-1.5 h-1.5 rounded-full flex-shrink-0 ${status.dot}`} />
                                                {status.label}
                                            </span>
                                        </div>
                                        <h3 className="font-semibold text-gray-900 dark:text-gray-100 text-sm mb-1 group-hover:text-primary-600 truncate">{project.name}</h3>
                                        <p className="text-xs text-gray-400 line-clamp-2 mb-4">{project.description || 'No description'}</p>
                                        <div className="mb-3">
                                            <div className="flex justify-between text-xs text-gray-400 mb-1">
                                                <span>{project.migratedFiles}/{project.totalFiles} files</span>
                                                <span className="font-medium">{progressPct}%</span>
                                            </div>
                                            <div className="w-full h-1.5 bg-gray-100 dark:bg-gray-800 rounded-full overflow-hidden">
                                                <div
                                                    className={`h-full rounded-full transition-all ${project.status === 'completed' ? 'bg-emerald-500' : project.status === 'failed' ? 'bg-red-500' : 'bg-primary-500'}`}
                                                    style={{ width: `${progressPct}%` }}
                                                />
                                            </div>
                                            {(project.migrationRuns ?? 0) > 0 && (
                                                <p className="text-xs text-violet-500 mt-1.5">{project.migrationRuns} migration run{project.migrationRuns !== 1 ? 's' : ''}</p>
                                            )}
                                        </div>
                                        <div className="flex items-center justify-between">
                                            <span className="text-xs text-gray-400 capitalize">{project.migrationType.split('-').join(' ')}</span>
                                            <div className="flex items-center gap-2">
                                                <button
                                                    onClick={(e) => { e.stopPropagation(); setDeleteTarget(project.id); }}
                                                    className="p-1 text-gray-300 hover:text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 rounded transition-colors opacity-0 group-hover:opacity-100"
                                                ><TrashIcon className="h-3.5 w-3.5" /></button>
                                                <ArrowRightIcon className="h-4 w-4 text-gray-300 group-hover:text-primary-500 transition-colors" />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                    )}
                    {totalPages > 1 && (
                        <div className="flex justify-between items-center mt-4">
                            <span className="text-sm text-gray-400">
                                Showing {(currentPage - 1) * ITEMS_PER_PAGE + 1}–{Math.min(currentPage * ITEMS_PER_PAGE, filteredProjects.length)} of {filteredProjects.length} projects
                            </span>
                            <div className="flex items-center gap-1">
                                <button onClick={() => setCurrentPage(1)} disabled={currentPage === 1}
                                    className="px-2.5 py-1.5 text-xs bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-lg disabled:opacity-40 hover:bg-gray-50 transition-colors">«</button>
                                <button onClick={() => setCurrentPage(p => Math.max(p - 1, 1))} disabled={currentPage === 1}
                                    className="px-3 py-1.5 text-sm bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-lg disabled:opacity-40 hover:bg-gray-50 transition-colors">‹ Prev</button>
                                {Array.from({ length: totalPages }, (_, i) => i + 1).filter(p => p === 1 || p === totalPages || Math.abs(p - currentPage) <= 1).map((p, idx, arr) => (
                                    <React.Fragment key={p}>
                                        {idx > 0 && arr[idx - 1] !== p - 1 && <span className="px-1 text-gray-300">…</span>}
                                        <button onClick={() => setCurrentPage(p)}
                                            className={`px-3 py-1.5 text-sm rounded-lg border transition-colors ${p === currentPage
                                                ? 'bg-primary-600 text-white border-primary-600'
                                                : 'bg-white dark:bg-gray-950 border-gray-200 dark:border-gray-800 hover:bg-gray-50'
                                                }`}>{p}</button>
                                    </React.Fragment>
                                ))}
                                <button onClick={() => setCurrentPage(p => Math.min(p + 1, totalPages))} disabled={currentPage === totalPages}
                                    className="px-3 py-1.5 text-sm bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-lg disabled:opacity-40 hover:bg-gray-50 transition-colors">Next ›</button>
                                <button onClick={() => setCurrentPage(totalPages)} disabled={currentPage === totalPages}
                                    className="px-2.5 py-1.5 text-xs bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-lg disabled:opacity-40 hover:bg-gray-50 transition-colors">»</button>
                            </div>
                        </div>
                    )}
                </>
            )}

            {/* Delete confirmation modal */}
            {deleteTarget && (
                <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
                    <div className="bg-white dark:bg-gray-950 rounded-xl shadow-2xl w-full max-w-md p-6">
                        <div className="flex items-center gap-3 mb-4">
                            <div className="w-10 h-10 rounded-full bg-red-100 dark:bg-red-900/30 flex items-center justify-center flex-shrink-0">
                                <TrashIcon className="h-5 w-5 text-red-600" />
                            </div>
                            <div>
                                <h3 className="font-semibold text-gray-900 dark:text-gray-100">Delete Project</h3>
                                <p className="text-sm text-gray-500 dark:text-gray-400">This action cannot be undone</p>
                            </div>
                        </div>
                        <p className="text-sm text-gray-600 dark:text-gray-300 mb-6">
                            Are you sure you want to delete <span className="font-semibold">{wsProjects.find(p => p.id === deleteTarget)?.name}</span>? All migration data will be permanently removed.
                        </p>
                        <div className="flex gap-3 justify-end">
                            <button onClick={() => setDeleteTarget(null)} className="px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 rounded-lg transition-colors">Cancel</button>
                            <button onClick={handleDelete} className="px-4 py-2 text-sm font-medium text-white bg-red-600 hover:bg-red-700 rounded-lg transition-colors">Delete Project</button>
                        </div>
                    </div>
                </div>
            )}

            {showWizard && (
                <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
                    <div className="bg-white dark:bg-gray-950 rounded-xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-y-auto">
                        <div className="px-6 py-5 border-b border-gray-100 dark:border-gray-800">
                            <div className="flex items-center justify-between mb-4">
                                <div className="flex items-center gap-3">
                                    <div className="w-8 h-8 rounded-lg bg-primary-100 dark:bg-primary-900/30 flex items-center justify-center">
                                        <BoltIcon className="h-4 w-4 text-primary-600" />
                                    </div>
                                    <div>
                                        <h2 className="text-base font-semibold text-gray-900 dark:text-gray-100">Create New Project</h2>
                                        <p className="text-xs text-gray-400">Step {step} of 4</p>
                                    </div>
                                </div>
                                <button onClick={() => { setShowWizard(false); setStep(1); }} className="p-1.5 text-gray-400 hover:text-gray-600 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors"><BuildingOffice2Icon className="h-4 w-4" /></button>
                            </div>
                            {/* Step indicators */}
                            <div className="flex items-center gap-2">
                                {[{ n: 1, label: 'Info' }, { n: 2, label: 'Migration' }, { n: 3, label: 'Runtime' }, { n: 4, label: 'Review' }].map(({ n, label }, idx, arr) => (
                                    <React.Fragment key={n}>
                                        <div className={`flex items-center gap-1.5 ${n < step ? 'text-emerald-600' : n === step ? 'text-primary-600' : 'text-gray-300'}`}>
                                            <div className={`w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0 ${
                                                n < step ? 'bg-emerald-100 text-emerald-600 dark:bg-emerald-900/30' :
                                                n === step ? 'bg-primary-600 text-white' :
                                                'bg-gray-100 dark:bg-gray-800 text-gray-400'
                                            }`}>{n < step ? '✓' : n}</div>
                                            <span className="text-xs font-medium hidden sm:block">{label}</span>
                                        </div>
                                        {idx < arr.length - 1 && <div className={`flex-1 h-0.5 rounded-full ${n < step ? 'bg-emerald-400' : 'bg-gray-200 dark:bg-gray-700'}`} />}
                                    </React.Fragment>
                                ))}
                            </div>
                        </div>
                        <div className="p-6">
                            {step === 1 && (
                                <div className="space-y-4">
                                    <h3 className="font-semibold text-gray-800 dark:text-gray-200">Basic Information</h3>
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Target Integration Platform</label>
                                        <div className="grid grid-cols-2 gap-3 mb-4">
                                            {Object.values(PLATFORM_STRATEGIES).map(p => (
                                                <div
                                                    key={p.id}
                                                    onClick={() => setWizardData(prev => ({
                                                        ...prev,
                                                        targetPlatform: p.id,
                                                        migrationType: p.supportedMigrationTypes[0].id as any,
                                                        targetRuntime: p.defaultRuntime as any,
                                                    }))}
                                                    className={`p-3 rounded-xl border-2 cursor-pointer transition-all ${wizardData.targetPlatform === p.id ? "border-primary-600 bg-primary-50/50 dark:bg-primary-950/20" : "border-gray-200 dark:border-gray-800 hover:border-gray-300"}`}
                                                >
                                                    <div className="font-semibold text-xs text-gray-900 dark:text-gray-100">{p.displayName}</div>
                                                    <div className="text-[11px] text-gray-500 mt-1 line-clamp-2">{p.description}</div>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Project Name</label>
                                        <input type="text" value={wizardData.name} onChange={e => setWizardData(p => ({ ...p, name: e.target.value }))}
                                            className="w-full px-4 py-2.5 rounded-lg border border-gray-300 text-sm focus:ring-2 focus:ring-primary-500 outline-none" placeholder="e.g. Order Processing API" />
                                    </div>
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Description</label>
                                        <textarea value={wizardData.description} onChange={e => setWizardData(p => ({ ...p, description: e.target.value }))} rows={3}
                                            className="w-full px-4 py-2.5 rounded-lg border border-gray-300 text-sm focus:ring-2 focus:ring-primary-500 outline-none resize-none" placeholder="What does this project migrate?" />
                                    </div>
                                </div>
                            )}
                            {step === 2 && (
                                <div className="space-y-4">
                                    <h3 className="font-semibold text-gray-800 dark:text-gray-200">Migration Type</h3>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">Select the type of migration for this project.</p>
                                    <div className="grid grid-cols-1 gap-3">
                                        {migrationTypes.map(mt => (
                                            <label key={mt.value} className={`flex items-center gap-3 p-4 rounded-lg border cursor-pointer transition-colors ${wizardData.migrationType === mt.value ? 'border-primary-500 bg-primary-50' : 'border-gray-200 dark:border-gray-800 hover:border-primary-200'}`}>
                                                <input type="radio" name="migrationType" value={mt.value} checked={wizardData.migrationType === mt.value}
                                                    onChange={() => setWizardData(p => ({ ...p, migrationType: mt.value as typeof p.migrationType }))} className="text-primary-600 focus:ring-primary-500" />
                                                <span className="font-medium text-sm text-gray-800 dark:text-gray-200">{mt.label}</span>
                                            </label>
                                        ))}
                                    </div>
                                </div>
                            )}
                            {step === 3 && (
                                <div className="space-y-4">
                                    <h3 className="font-semibold text-gray-800 dark:text-gray-200">Target Runtime</h3>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">Choose the AWS Lambda runtime for your migrated functions.</p>
                                    <div className="grid grid-cols-1 gap-3">
                                        {runtimes.map(rt => (
                                            <label key={rt.value} className={`flex items-center gap-3 p-4 rounded-lg border cursor-pointer transition-colors ${wizardData.targetRuntime === rt.value ? 'border-primary-500 bg-primary-50' : 'border-gray-200 dark:border-gray-800 hover:border-primary-200'}`}>
                                                <input type="radio" name="targetRuntime" value={rt.value} checked={wizardData.targetRuntime === rt.value}
                                                    onChange={() => setWizardData(p => ({ ...p, targetRuntime: rt.value as typeof p.targetRuntime }))} className="text-primary-600 focus:ring-primary-500" />
                                                <span className="font-medium text-sm text-gray-800 dark:text-gray-200">{rt.label}</span>
                                            </label>
                                        ))}
                                    </div>
                                </div>
                            )}
                            {step === 4 && (
                                <div className="space-y-4">
                                    <h3 className="font-semibold text-gray-800 dark:text-gray-200">Confirmation</h3>
                                    <p className="text-sm text-gray-500 dark:text-gray-400">Review your project settings before creating.</p>
                                    <div className="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 space-y-3 text-sm">
                                        <div className="flex justify-between"><span className="text-gray-500 dark:text-gray-400">Project Name</span><span className="font-medium">{wizardData.name || '—'}</span></div>
                                        <div className="flex justify-between"><span className="text-gray-500 dark:text-gray-400">Migration Type</span><span className="font-medium capitalize">{wizardData.migrationType.replace(/-/g, ' → ')}</span></div>
                                        <div className="flex justify-between"><span className="text-gray-500 dark:text-gray-400">Target Runtime</span><span className="font-medium capitalize">{wizardData.targetRuntime}</span></div>
                                    </div>
                                    <div className="bg-primary-50 border border-primary-200 rounded-lg p-4 text-sm text-primary-800">
                                        <p className="font-medium mb-1">What happens next?</p>
                                        <ol className="space-y-1 text-primary-700 list-decimal list-inside">
                                            <li>Project is created and you&apos;ll land on the project overview</li>
                                            <li>Import your MuleSoft source code (Git or ZIP)</li>
                                            <li>Run the AI migration</li>
                                            <li>Review &amp; export to AWS Lambda</li>
                                        </ol>
                                    </div>
                                </div>
                            )}
                        </div>
                        <div className="px-6 py-4 border-t border-gray-100 dark:border-gray-800 flex justify-between">
                            <button onClick={() => step > 1 ? setStep(step - 1) : setShowWizard(false)}
                                className="px-4 py-2.5 text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-950 border border-gray-300 dark:border-gray-700 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors">
                                {step === 1 ? 'Cancel' : '← Back'}
                            </button>
                            <button onClick={() => step < 4 ? setStep(step + 1) : handleCreate()} disabled={step === 1 && !wizardData.name.trim()}
                                className="px-6 py-2.5 text-sm font-medium text-white bg-primary-600 hover:bg-primary-700 disabled:opacity-40 disabled:cursor-not-allowed rounded-lg transition-colors inline-flex items-center gap-2">
                                {step === 4 ? <><BoltIcon className="h-4 w-4" /> Create Project</> : <>Next →</>}
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}