'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { useApp } from '@/contexts/AppContext';
import { useRouter } from 'next/navigation';
import { MigrationType, TargetRuntime, TargetPlatform } from '@/lib/types';
import { getPlatformStrategy, PLATFORM_STRATEGIES } from '@/lib/platforms';
import ConfirmDialog from '@/components/ui/ConfirmDialog';
import {
    ChevronRightIcon,
    Cog6ToothIcon,
    TrashIcon,
    ClockIcon,
} from '@heroicons/react/24/outline';

export default function ProjectSettingsPage({ params }: { params: Promise<{ projectId: string }> }) {
    const { projects, selectedProject, selectProject, updateProject, addToast } = useApp();
    const router = useRouter();
    const [resolvedProjectId, setResolvedProjectId] = useState<string | null>(null);
    const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);

    // Form state
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [targetPlatform, setTargetPlatform] = useState<TargetPlatform>('aws');
    const [migrationType, setMigrationType] = useState<MigrationType | ''>('');
    const [targetRuntime, setTargetRuntime] = useState<TargetRuntime | ''>('');
    const [hasChanges, setHasChanges] = useState(false);
    const projectReqRef = React.useRef<AbortController | null>(null);
    const fetchedProjectRef = React.useRef<string | null>(null);

    useEffect(() => { params.then(p => setResolvedProjectId(p.projectId)); }, [params]);

    useEffect(() => {
        if (!resolvedProjectId) return;
        
        const existing = projects.find(p => p.id === resolvedProjectId);
        if (existing) {
            selectProject(existing);
        } else {
            if (fetchedProjectRef.current === resolvedProjectId) return;
            fetchedProjectRef.current = resolvedProjectId;
            // Fetch fallback for direct navigation
            projectReqRef.current?.abort();
            const controller = new AbortController();
            projectReqRef.current = controller;
            fetch(`/api/projects/${resolvedProjectId}`, { signal: controller.signal })
                .then(r => r.json())
                .then(data => {
                    if (data.project) selectProject(data.project);
                })
                .catch(() => {});
        }
    }, [resolvedProjectId, projects, selectProject]);
    useEffect(() => () => projectReqRef.current?.abort(), []);

    // Populate form from selected project
    useEffect(() => {
        if (selectedProject) {
            setName(selectedProject.name);
            setDescription(selectedProject.description);
            const strategy = getPlatformStrategy(selectedProject.targetPlatform, selectedProject.migrationType, selectedProject.targetRuntime);
            setTargetPlatform(strategy.id);
            setMigrationType(selectedProject.migrationType);
            setTargetRuntime(selectedProject.targetRuntime);
            setHasChanges(false);
        }
    }, [selectedProject]);

    const activeStrategy = PLATFORM_STRATEGIES[targetPlatform] || PLATFORM_STRATEGIES.aws;

    const handlePlatformChange = useCallback((newPlatform: TargetPlatform) => {
        setTargetPlatform(newPlatform);
        const strat = PLATFORM_STRATEGIES[newPlatform];
        setMigrationType(strat.supportedMigrationTypes[0].id);
        setTargetRuntime(strat.defaultRuntime);
        setHasChanges(true);
    }, []);

    // Hoist callbacks before early return to satisfy Rules of Hooks
    const handleSave = useCallback(() => {
        if (!selectedProject) return;
        updateProject(selectedProject.id, {
            name,
            description,
            targetPlatform,
            migrationType: migrationType as MigrationType,
            targetRuntime: targetRuntime as TargetRuntime
        });
        addToast({ type: 'success', title: 'Settings Saved', message: `Project settings updated to ${activeStrategy.displayName}.` });
        setHasChanges(false);
    }, [selectedProject, name, description, targetPlatform, migrationType, targetRuntime, activeStrategy.displayName, updateProject, addToast]);

    const handleDelete = useCallback(() => {
        if (!selectedProject) return;
        updateProject(selectedProject.id, { status: 'pending' });
        addToast({ type: 'success', title: 'Project Deleted', message: `${selectedProject.name} has been removed.` });
        setShowDeleteConfirm(false);
        router.replace('/dashboard/organizations');
    }, [selectedProject, updateProject, addToast, router]);

    const handleFieldChange = useCallback(<T,>(setter: (v: T) => void, value: T) => {
        setter(value);
        setHasChanges(true);
    }, []);

    const project = selectedProject;
    if (!project) return null;

    // Audit log entries
    const auditLog = [
        { action: 'Project created', user: 'Mayur Mane', time: project.createdAt, icon: '🆕' },
        { action: 'Migration started', user: 'Mayur Mane', time: project.lastActivity, icon: '🚀' },
        { action: 'Settings updated', user: 'Mayur Mane', time: new Date().toISOString().split('T')[0], icon: '⚙️' },
    ];

    return (
        <div className="animate-fade-in p-6 max-w-3xl mx-auto">
            {/* Breadcrumb */}
            <nav className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-6">
                <button onClick={() => router.push('/dashboard/organizations')} className="hover:text-primary-600 transition-colors">Organizations</button>
                <ChevronRightIcon className="h-3.5 w-3.5" />
                <button onClick={() => router.push(`/dashboard/projects/${project.id}`)} className="hover:text-primary-600 transition-colors">{project.name}</button>
                <ChevronRightIcon className="h-3.5 w-3.5" />
                <span className="text-gray-900 dark:text-gray-100 font-medium">Settings</span>
            </nav>

            <div className="flex items-center gap-3 mb-8">
                <div className="w-10 h-10 bg-gray-100 dark:bg-gray-800 rounded-lg flex items-center justify-center">
                    <Cog6ToothIcon className="h-5 w-5 text-gray-500 dark:text-gray-400" />
                </div>
                <div>
                    <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">Project Setup</h1>
                    <p className="text-sm text-gray-500 dark:text-gray-400">{project.name} &bull; <span className="font-semibold text-primary-600 dark:text-primary-400">{activeStrategy.displayName}</span></p>
                </div>
            </div>

            {/* General Settings */}
            <section className="bg-white dark:bg-gray-950 rounded-xl border border-gray-200 dark:border-gray-800 p-6 mb-6">
                <h2 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-4">General</h2>
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Project Name</label>
                        <input type="text" value={name}
                            onChange={e => handleFieldChange(setName, e.target.value)}
                            className="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-700 text-sm focus:ring-2 focus:ring-primary-500 outline-none dark:bg-gray-900" />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Description</label>
                        <textarea value={description}
                            onChange={e => handleFieldChange(setDescription, e.target.value)}
                            rows={3}
                            className="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-700 text-sm focus:ring-2 focus:ring-primary-500 outline-none resize-none dark:bg-gray-900" />
                    </div>

                    {/* Target Platform Selector */}
                    <div>
                        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Target Cloud Platform</label>
                        <div className="grid grid-cols-2 gap-4">
                            <button
                                type="button"
                                onClick={() => handlePlatformChange('aws')}
                                className={`p-4 rounded-xl border-2 text-left transition-all ${
                                    targetPlatform === 'aws'
                                        ? 'border-primary-600 bg-primary-50/40 dark:bg-primary-950/20'
                                        : 'border-gray-200 dark:border-gray-800 hover:border-gray-300'
                                }`}
                            >
                                <div className="flex items-center justify-between mb-1">
                                    <span className="font-semibold text-sm text-gray-900 dark:text-gray-100">AWS Serverless</span>
                                    {targetPlatform === 'aws' && <span className="text-xs bg-primary-600 text-white px-2 py-0.5 rounded-full font-bold">Active</span>}
                                </div>
                                <p className="text-xs text-gray-500 dark:text-gray-400">AWS Lambda, API Gateway, SQS, Step Functions &amp; Terraform</p>
                            </button>

                            <button
                                type="button"
                                onClick={() => handlePlatformChange('sap-integration-suite')}
                                className={`p-4 rounded-xl border-2 text-left transition-all ${
                                    targetPlatform === 'sap-integration-suite'
                                        ? 'border-emerald-600 bg-emerald-50/40 dark:bg-emerald-950/20'
                                        : 'border-gray-200 dark:border-gray-800 hover:border-gray-300'
                                }`}
                            >
                                <div className="flex items-center justify-between mb-1">
                                    <span className="font-semibold text-sm text-gray-900 dark:text-gray-100">SAP Integration Suite</span>
                                    {targetPlatform === 'sap-integration-suite' && <span className="text-xs bg-emerald-600 text-white px-2 py-0.5 rounded-full font-bold">Active</span>}
                                </div>
                                <p className="text-xs text-gray-500 dark:text-gray-400">SAP Cloud Integration (CPI) BPMN2 iFlows, Apache Groovy &amp; BTP Packages</p>
                            </button>
                        </div>
                    </div>

                    <div className="grid grid-cols-2 gap-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Migration Type</label>
                            <select value={migrationType}
                                onChange={e => handleFieldChange<MigrationType | ''>(setMigrationType, e.target.value as MigrationType)}
                                className="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-700 text-sm focus:ring-2 focus:ring-primary-500 outline-none bg-white dark:bg-gray-900">
                                {activeStrategy.supportedMigrationTypes.map((m: any) => (
                                    <option key={m.id} value={m.id}>{m.label}</option>
                                ))}
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Target Runtime</label>
                            <select value={targetRuntime}
                                onChange={e => handleFieldChange<TargetRuntime | ''>(setTargetRuntime, e.target.value as TargetRuntime)}
                                className="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-700 text-sm focus:ring-2 focus:ring-primary-500 outline-none bg-white dark:bg-gray-900">
                                {activeStrategy.supportedRuntimes.map((r: any) => (
                                    <option key={r.id} value={r.id}>{r.label}</option>
                                ))}
                            </select>
                        </div>
                    </div>
                    <div className="flex justify-end pt-2">
                        <button onClick={handleSave} disabled={!hasChanges}
                            className="px-6 py-2.5 bg-primary-600 hover:bg-primary-700 disabled:bg-gray-300 disabled:cursor-not-allowed text-white text-sm font-medium rounded-lg transition-colors shadow-sm">
                            Save Changes
                        </button>
                    </div>
                </div>
            </section>

            {/* Audit Log */}
            <section className="bg-white dark:bg-gray-950 rounded-xl border border-gray-200 dark:border-gray-800 p-6 mb-6">
                <div className="flex items-center gap-2 mb-4">
                    <ClockIcon className="h-5 w-5 text-gray-400" />
                    <h2 className="text-lg font-semibold text-gray-900 dark:text-gray-100">Activity Log</h2>
                </div>
                <div className="space-y-3">
                    {auditLog.map((entry, i) => (
                        <div key={i} className="flex items-center gap-3 py-2 border-b border-gray-50 last:border-0">
                            <span className="text-lg">{entry.icon}</span>
                            <div className="flex-1">
                                <span className="text-sm text-gray-900 dark:text-gray-100 font-medium">{entry.action}</span>
                                <span className="text-xs text-gray-400 ml-2">by {entry.user}</span>
                            </div>
                            <span className="text-xs text-gray-400">{entry.time}</span>
                        </div>
                    ))}
                </div>
            </section>

            {/* Danger Zone */}
            <section className="bg-white dark:bg-gray-950 rounded-xl border-2 border-error-200 p-6">
                <h2 className="text-lg font-semibold text-error-700 mb-4">Danger Zone</h2>
                <div className="flex items-center justify-between py-3">
                    <div>
                        <p className="text-sm font-medium text-gray-900 dark:text-gray-100">Delete Project</p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">Permanently delete this project and all data.</p>
                    </div>
                    <button onClick={() => setShowDeleteConfirm(true)}
                        className="flex items-center gap-1.5 px-4 py-2 text-sm font-medium text-white bg-error-500 hover:bg-error-600 rounded-lg transition-colors">
                        <TrashIcon className="h-4 w-4" /> Delete
                    </button>
                </div>
            </section>

            {/* Confirm Dialogs */}
            <ConfirmDialog isOpen={showDeleteConfirm} onClose={() => setShowDeleteConfirm(false)} onConfirm={handleDelete}
                title="Delete Project" message={`Are you sure you want to delete "${project.name}"? This action cannot be undone and all migration data will be permanently lost.`}
                confirmLabel="Delete" destructive={true} />
        </div>
    );
}
