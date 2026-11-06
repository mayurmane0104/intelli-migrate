'use client';

import React, { useState, useRef, useEffect, useMemo } from 'react';
import { useApp } from '@/contexts/AppContext';
import { useAuth } from '@/contexts/AuthContext';  // FIX P1-2: need authenticated userId
import { PROVIDER_INFO } from '@/lib/llm-provider';
import type { LLMProviderType, ProjectFile, MigrationJob } from '@/lib/types';
import { analysisApi } from '@/lib/api';
import { useSettingsStore } from '@/lib/stores/settings-store';
import { useMigrationStore } from '@/lib/stores/migration-store';
import { formatDuration } from '@/lib/utils/duration';
import {
    StopIcon,
    QueueListIcon, CogIcon, ChevronDownIcon,
    RocketLaunchIcon,
} from '@heroicons/react/24/outline';
import { generateAlphanumericId } from '@/lib/id-utils';
import { llmSettingsApi } from '@/lib/api';

interface MigrationPanelProps {
    onToggleJobTracker: () => void;
    showJobTracker: boolean;
}

// All known providers — filtered at render time to only show configured ones.
// Nova Lite is listed first as it is the primary/default configured provider.
const ALL_PROVIDERS: LLMProviderType[] = ['nova', 'claude', 'openai', 'gemini'];

export default function MigrationPanel({ onToggleJobTracker, showJobTracker }: MigrationPanelProps) {
    const {
        selectedProject, addToast, files, syncFileMigrationResult, bulkUpdateFileStatus, refreshFiles
    } = useApp();

    const { user } = useAuth();  // FIX P1-2: get the authenticated user for userId propagation

    const { llm: llmSettings, updateLLMSettings } = useSettingsStore();
    const {
        isMigrating,
        jobs,
        startBatchMigration,
        stopMigration,
        initSocket,
        markProjectLoaded,
        setProjectStartedAt,
        resetProjectTiming,
        markProjectCompleted,
        projectTimings,
        executionRuns,
        latestExecutionRunByProject,
    } = useMigrationStore();

    const [showProviderDropdown, setShowProviderDropdown] = useState(false);
    const [showAnalytics, setShowAnalytics] = useState(true);
    const [currentTime, setCurrentTime] = useState(() => Date.now());
    const dropdownRef = useRef<HTMLDivElement>(null);

    // Re-attach socket to active session once per project change.
    useEffect(() => {
        if (!selectedProject?.id) return;
        markProjectLoaded(selectedProject.id);
        initSocket(selectedProject.id);
        useMigrationStore.getState().syncJobs(selectedProject.id);
    }, [selectedProject?.id, initSocket, markProjectLoaded]);

    useEffect(() => {
        let cancelled = false;
        llmSettingsApi.get()
            .then(({ settings }) => {
                if (!cancelled) updateLLMSettings(settings);
            })
            .catch(() => { });
        return () => {
            cancelled = true;
        };
    }, [updateLLMSettings]);

    // Sync completed jobs to AppContext files for treeview reactivity
    useEffect(() => {
        Object.values(jobs).forEach(job => {
            if (job.status === 'done' && job.streamedContent) {
                const file = files.find(f => f.id === job.fileId);
                // The backend already persists completed migrations; keep local UI state in sync
                // without re-POSTing the same payload on every render.
                if (file && (file.status !== 'completed' || !file.migratedContent)) {
                    syncFileMigrationResult(job.fileId, job.streamedContent, 'completed');
                }
            }
        });
    }, [jobs, files, syncFileMigrationResult]);

    // Close dropdown on outside click
    useEffect(() => {
        const handler = (e: MouseEvent) => {
            if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
                setShowProviderDropdown(false);
            }
        };
        document.addEventListener('mousedown', handler);
        return () => document.removeEventListener('mousedown', handler);
    }, []);

    const project = selectedProject;
    const projectId = project?.id;

    // Refresh AppContext file tree when migration finishes so counts/status match the DB.
    useEffect(() => {
        if (!projectId || isMigrating) return;
        refreshFiles(projectId, true);
    }, [projectId, isMigrating, refreshFiles]);
    
    // Project files from AppContext (database state)
    const projectFiles = useMemo(() => 
        files.filter((f: ProjectFile) => f.projectId === projectId && f.type === 'file'),
    [files, projectId]);

    // Active jobs from MigrationStore (real-time state)
    const activeJobs = useMemo(() => {
        const allJobs = Object.values(jobs).filter(j => j.projectId === projectId);
        
        // Find the active or most recent batch to stay in sync with JobTracker
        const groups: Record<string, typeof allJobs> = {};
        allJobs.forEach(job => {
            const bid = job.batchId || 'SESSION';
            if (!groups[bid]) groups[bid] = [];
            groups[bid].push(job);
        });

        const allBatches = Object.entries(groups).sort((a, b) => {
            const aLatest = Math.max(...a[1].map(j => new Date(j.completedAt || j.startedAt || 0).getTime()));
            const bLatest = Math.max(...b[1].map(j => new Date(j.completedAt || j.startedAt || 0).getTime()));
            return bLatest - aLatest;
        });

        const activeBatch = allBatches.find(([, batchJobs]) => 
            batchJobs.some(j => j.status === 'running' || j.status === 'queued')
        );

        return activeBatch ? activeBatch[1] : (allBatches.length > 0 ? allBatches[0][1] : []);
    }, [jobs, projectId]);

    const completedCount = isMigrating || activeJobs.length > 0 
        ? activeJobs.filter((j: MigrationJob) => j.status === 'done').length 
        : projectFiles.filter((f: ProjectFile) => f.status === 'completed').length;

    const failedCount = isMigrating || activeJobs.length > 0 
        ? activeJobs.filter((j: MigrationJob) => j.status === 'failed').length 
        : projectFiles.filter((f: ProjectFile) => f.status === 'failed').length;

    const totalCount = isMigrating || activeJobs.length > 0 
        ? activeJobs.length 
        : projectFiles.length;

    const hasLiveJobs = useMemo(
        () => activeJobs.some((j: MigrationJob) => j.status === 'queued' || j.status === 'running'),
        [activeJobs],
    );

    // Poll backend file status while a migration is active (covers missed socket events).
    useEffect(() => {
        if (!projectId || (!isMigrating && !hasLiveJobs)) return;

        void useMigrationStore.getState().syncJobs(projectId);

        const interval = setInterval(() => {
            void useMigrationStore.getState().syncJobs(projectId);
            if (!useMigrationStore.getState().isMigrating) {
                refreshFiles(projectId, true);
            }
        }, 12000);

        return () => clearInterval(interval);
    }, [projectId, isMigrating, hasLiveJobs, refreshFiles]);

    useEffect(() => {
        if (!projectId || projectFiles.length === 0) return;
        const earliestImportedAt = projectFiles.reduce<string | null>((earliest, file) => {
            if (!file.lastModified) return earliest;
            if (!earliest) return file.lastModified;
            return new Date(file.lastModified).getTime() < new Date(earliest).getTime()
                ? file.lastModified
                : earliest;
        }, null);

        if (earliestImportedAt) {
            setProjectStartedAt(projectId, earliestImportedAt);
        }

        if (projectFiles.every((file) => file.status === 'completed')) {
            markProjectCompleted(projectId);
        }
    }, [markProjectCompleted, projectFiles, projectId, setProjectStartedAt]);

    // Progress bar percent: count Done + Fail as "processed"
    let progressPct = totalCount > 0 ? Math.round(((completedCount + failedCount) / totalCount) * 100) : 0;
    if (isMigrating && progressPct >= 100) {
        progressPct = 95;
    }

    const activeLLMProvider = llmSettings.activeProvider;
    const activeInfo = PROVIDER_INFO[activeLLMProvider] || PROVIDER_INFO.claude;
    const projectTiming = projectId ? projectTimings[projectId] : undefined;
    const latestExecutionRunId = projectId ? latestExecutionRunByProject[projectId] : undefined;
    const currentExecutionRun = latestExecutionRunId ? executionRuns[latestExecutionRunId] : undefined;
    const projectDurationMs = projectTiming?.projectStartedAt
        ? new Date(projectTiming.projectCompletedAt ?? currentTime).getTime() - new Date(projectTiming.projectStartedAt).getTime()
        : null;
    const executionDurationMs = currentExecutionRun?.executionStartedAt
        ? new Date(currentExecutionRun.executionCompletedAt ?? currentTime).getTime() - new Date(currentExecutionRun.executionStartedAt).getTime()
        : null;
    const projectDurationLabel = projectDurationMs !== null ? formatDuration(projectDurationMs) : 'Not started';
    const executionDurationLabel = executionDurationMs !== null ? formatDuration(executionDurationMs) : 'Not started';
    const shouldTickClock = Boolean(
        (projectTiming?.projectStartedAt && !projectTiming.projectCompletedAt)
        || (currentExecutionRun?.executionStartedAt && !currentExecutionRun.executionCompletedAt)
    );

    useEffect(() => {
        if (!shouldTickClock) return;

        const interval = window.setInterval(() => {
            setCurrentTime(Date.now());
        }, 1000);

        return () => window.clearInterval(interval);
    }, [shouldTickClock]);

    const handleStartMigration = async () => {
        if (!project) return;

        try {
            const analysis = await analysisApi.latest(project.id);
            const validation = analysis?.analysis?.validation;
            const blocked = Boolean(validation?.blockers?.length);
            if (analysis.status !== 'completed' || !analysis.analysis) {
                addToast({
                    type: 'warning',
                    title: 'Analysis Required',
                    message: 'Project analysis is still running or missing. Complete analysis before migration.',
                });
                return;
            }
            if (blocked) {
                addToast({
                    type: 'error',
                    title: 'Migration Blocked',
                    message: 'Analysis found blockers. Resolve connector/validation blockers before migration.',
                });
                return;
            }
        } catch {
            addToast({
                type: 'warning',
                title: 'Analysis Check Failed',
                message: 'Could not verify analysis status. Refresh analysis and retry.',
            });
            return;
        }

        // For a professional Project-wide Sync, we include all files.
        // Files that are already completed will be re-processed or refreshed.
        const fileIds = projectFiles.map((f: ProjectFile) => f.id);

        // Find if there's an existing migration run to resume
        const existingMigrationId = projectFiles.find((f: ProjectFile) => f.activeMigrationId)?.activeMigrationId;
        const migrationId = existingMigrationId || generateAlphanumericId(10);

        try {
            // Persist only the user's provider choice. The backend resolves full
            // provider settings and secrets when it queues the migration.
            const { settings: savedSettings } = await llmSettingsApi.save({
                activeProvider: llmSettings.activeProvider,
            });
            updateLLMSettings(savedSettings);
            resetProjectTiming(project.id, new Date().toISOString());

            // Optimistically update local UI state so progress bars reset to 0 immediately
            bulkUpdateFileStatus(fileIds, 'pending');

            addToast({
                type: 'info',
                title: completedCount > 0 ? 'Syncing Transformation' : 'Sync Started',
                message: `Publishing ${fileIds.length} files to the migration queue...`
            });

            await startBatchMigration(
                project.id,
                fileIds,
                {
                    targetPlatform: project.targetPlatform,
                    migrationType: project.migrationType,
                    targetRuntime: project.targetRuntime,
                },
                migrationId,
                user?.id,
                llmSettings,
            );
        } catch (error: unknown) {
            // Revert state if possible or just show error
            addToast({
                type: 'error',
                title: 'Migration Blocked',
                message: error instanceof Error ? error.message : 'An unexpected error occurred while starting the migration.'
            });
            // Force refresh files to get back actual DB state
            refreshFiles(project.id, true);
        }
    };

    const handleStopMigration = async () => {
        if (!project) return;

        await stopMigration(project.id);
        addToast({
            type: 'warning',
            title: 'Migration Stopped',
            message: 'Stopping active migration jobs...'
        });
    };

    if (!project) return null;

    return (
        <div className="bg-white dark:bg-gray-950 border-t border-gray-200 dark:border-gray-800 px-4 py-3">
            <div className="flex items-center gap-4 flex-wrap">
                {/* Actions */}
                <div className="flex items-center gap-2">
                    {!isMigrating ? (
                        <button onClick={handleStartMigration}
                            className="flex items-center gap-1.5 px-3 py-1.5 bg-primary-600 hover:bg-primary-700 disabled:bg-gray-300 text-white text-xs font-medium rounded-lg transition-all shadow-md active:scale-95 group">
                            <RocketLaunchIcon className="h-3.5 w-3.5 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
                            Begin Migration
                        </button>
                    ) : (
                        <div className="flex items-center gap-2">
                            <div className="flex items-center gap-2 px-3 py-1.5 bg-gray-100 dark:bg-gray-800 rounded-lg text-xs font-medium text-gray-500">
                                <CogIcon className="h-3.5 w-3.5 animate-spin text-primary-600" />
                                Migrating...
                            </div>
                            <button onClick={handleStopMigration}
                                className="flex items-center gap-1.5 px-3 py-1.5 bg-red-50 hover:bg-red-100 text-red-600 text-xs font-medium rounded-lg transition-colors border border-red-100">
                                <StopIcon className="h-3.5 w-3.5" />
                                Stop
                            </button>
                        </div>
                    )}
                </div>

                <div className="h-6 w-px bg-gray-200" />

                {/* Provider Badge */}
                <div className="relative" ref={dropdownRef}>
                    <button
                        onClick={() => setShowProviderDropdown(p => !p)}
                        className="flex items-center gap-1.5 px-3 py-1.5 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-lg text-[11px] font-bold text-gray-700 dark:text-gray-300 hover:bg-gray-100 transition-all shadow-sm group"
                    >
                        <span className="text-sm group-hover:scale-110 transition-transform">{activeInfo.icon}</span>
                        <span className="tracking-tight">{activeInfo.name}</span>
                        <ChevronDownIcon className="h-3 w-3 text-gray-400 group-hover:text-gray-600" />
                    </button>

                    {showProviderDropdown && (() => {
                        // Only show providers that have an API key configured and are enabled.
                        // This prevents mock/placeholder/unconfigured entries from appearing in the UI.
                        const configuredProviders = ALL_PROVIDERS.filter(p => {
                            const cfg = llmSettings.providers[p as keyof typeof llmSettings.providers];
                            return cfg && cfg.enabled && cfg.apiKey && cfg.apiKey.trim().length > 0;
                        });
                        // Always include the active provider even if somehow not in configured list
                        const visibleProviders = configuredProviders.includes(activeLLMProvider as LLMProviderType)
                            ? configuredProviders
                            : [activeLLMProvider as LLMProviderType, ...configuredProviders];
                        return (
                            <div className="absolute bottom-full left-0 mb-2 w-56 bg-white dark:bg-gray-950 rounded-xl border border-gray-200 dark:border-gray-800 shadow-xl py-1 z-50">
                                {visibleProviders.map(provider => {
                                    const info = PROVIDER_INFO[provider];
                                    const isActive = activeLLMProvider === provider;
                                    return (
                                        <div key={provider}
                                            onClick={() => updateLLMSettings({ activeProvider: provider as LLMProviderType })}
                                            className={`flex items-center gap-3 px-3 py-2.5 cursor-pointer ${isActive ? 'bg-primary-50 dark:bg-primary-900/30' : 'hover:bg-gray-50 dark:hover:bg-gray-800/50'} transition-colors`}>
                                            <span className={`text-base ${isActive ? 'text-primary-600 dark:text-primary-400' : 'text-gray-500 dark:text-gray-400'}`}>{info.icon}</span>
                                            <div className="flex-1 min-w-0">
                                                <p className={`text-xs font-medium ${isActive ? 'text-primary-700 dark:text-primary-400' : 'text-gray-800 dark:text-gray-200'}`}>{info.name}</p>
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        );
                    })()}
                </div>

                {/* Progress */}
                <div className="flex items-center gap-3 flex-1 min-w-[200px]">
                    <div className="flex-1">
                        <div className="flex justify-between text-xs text-gray-500 dark:text-gray-400 mb-1">
                            <span>{completedCount} / {totalCount} migrated</span>
                            <span className="font-medium">{progressPct}%</span>
                        </div>
                        <div className="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                            <div className="h-full bg-primary-600 transition-all duration-700"
                                style={{ width: `${progressPct}%` }} />
                        </div>
                    </div>
                </div>

                <div className="h-6 w-px bg-gray-200" />

                {/* Job Tracker toggle */}
                <button onClick={onToggleJobTracker}
                    className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-lg transition-colors ${showJobTracker ? 'bg-primary-50 text-primary-700 border border-primary-200' : 'bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-50'
                        }`}>
                    <QueueListIcon className="h-3.5 w-3.5" /> Job Tracker
                    {Object.keys(jobs).length > 0 && (
                        <span className={`ml-1 px-1.5 py-0.5 text-[10px] font-bold rounded-full ${isMigrating ? 'bg-blue-100 text-blue-700 animate-pulse' : 'bg-gray-100 text-gray-600 dark:text-gray-400'}`}>
                            {Object.keys(jobs).length}
                        </span>
                    )}
                </button>
            </div>

            <div className="mt-4 border border-gray-200 dark:border-gray-800 rounded-xl overflow-hidden">
                <button
                    type="button"
                    onClick={() => setShowAnalytics((value) => !value)}
                    className="w-full flex items-center justify-between px-4 py-3 bg-gray-50 dark:bg-gray-900/60 text-left"
                >
                    <span className="text-sm font-semibold text-gray-900 dark:text-gray-100">
                        Migration Analytics
                    </span>
                    <ChevronDownIcon
                        className={`h-4 w-4 text-gray-500 transition-transform ${showAnalytics ? 'rotate-180' : ''}`}
                    />
                </button>

                {showAnalytics && (
                    <div className="grid gap-3 px-4 py-4 sm:grid-cols-2">
                        <div className="rounded-lg border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 px-4 py-3">
                            <p className="text-xs font-medium uppercase tracking-wide text-gray-500 dark:text-gray-400">
                                Project Duration
                            </p>
                            <p className="mt-1 text-sm font-semibold text-gray-900 dark:text-gray-100">
                                {projectDurationLabel}
                            </p>
                        </div>
                        <div className="rounded-lg border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 px-4 py-3">
                            <p className="text-xs font-medium uppercase tracking-wide text-gray-500 dark:text-gray-400">
                                Execution Time
                            </p>
                            <p className="mt-1 text-sm font-semibold text-gray-900 dark:text-gray-100">
                                {executionDurationLabel}
                                {isMigrating && currentExecutionRun && !currentExecutionRun.executionCompletedAt ? ' (live)' : ''}
                            </p>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}









