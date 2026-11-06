'use client';

import React, { useState, useEffect, useMemo, useRef, useCallback } from 'react';
import dynamic from 'next/dynamic';
import { useRouter } from 'next/navigation';
import { useApp } from '@/contexts/AppContext';
import { getPlatformStrategy } from '@/lib/platforms';
import { useAuth } from '@/contexts/AuthContext';
import { useMigrationStore } from '@/lib/stores/migration-store';
import { useSettingsStore } from '@/lib/stores/settings-store';
import { analysisApi, llmSettingsApi } from '@/lib/api';
import { generateAlphanumericId } from '@/lib/id-utils';
import { ErrorBoundary } from '@/components';
import { Modal } from '@/components/ui';
import { ProjectFile } from '@/lib/types';
import {
    ChevronRightIcon, CodeBracketIcon,
    ArrowsRightLeftIcon, ArrowDownTrayIcon,
    ArrowUpTrayIcon, EyeIcon, RocketLaunchIcon,
    SparklesIcon, CheckCircleIcon, CommandLineIcon,
    DocumentTextIcon, ArrowPathIcon
} from '@heroicons/react/24/outline';

// Dynamic imports for performance
const FileTree = dynamic(() => import('@/components/editor/FileTree'), { ssr: false, loading: () => <div className="h-full bg-gray-50/50 animate-pulse" /> }) as any;
const CodeEditor = dynamic(() => import('@/components/editor/CodeEditor'), { ssr: false }) as any;
const DiffViewer = dynamic(() => import('@/components/editor/DiffViewer'), { ssr: false }) as any;
const LiveStreamPanel = dynamic(() => import('@/components/editor/LiveStreamPanel'), { ssr: false }) as any;
const MigrationPanel = dynamic(() => import('@/components/editor/MigrationPanel'), { ssr: false }) as any;
const JobTracker = dynamic(() => import('@/components/editor/JobTracker'), { ssr: false }) as any;
const ExportPanel = dynamic(() => import('@/components/export/ExportPanel'), { ssr: false }) as any;
const ImportPanel = dynamic(() => import('@/components/import/ImportPanel'), { ssr: false }) as any;
const ResizablePanels = dynamic(() => import('@/components/layout/ResizablePanels'), { ssr: false }) as any;

type CenterView = 'diff' | 'source' | 'migrated';

export default function EditorPage({ params }: { params: Promise<{ projectId: string }> }) {
    const {
        projects, selectedProject, selectProject, selectedFile, selectFile, files, addToast,
        refreshFiles,
        migrationJobs, migrationSession, migrationLogs,
    } = useApp();
    const { user } = useAuth();
    const { llm: llmSettings, updateLLMSettings } = useSettingsStore();
    const {
        isMigrating,
        startBatchMigration,
        initSocket,
        markProjectLoaded,
        resetProjectTiming,
    } = useMigrationStore();
    const router = useRouter();
    const projectReqRef = useRef<AbortController | null>(null);
    const fetchedProjectRef = useRef<string | null>(null);
    const [resolvedProjectId, setResolvedProjectId] = useState<string | null>(null);
    const [centerView, setCenterView] = useState<CenterView>('source');
    const [showJobTracker, setShowJobTracker] = useState(false);
    const [showExport, setShowExport] = useState(false);
    const [showImport, setShowImport] = useState(false);
    const [showCompletionModal, setShowCompletionModal] = useState(false);
    const migrationStartedRef = useRef(false);

    useEffect(() => { params.then(p => setResolvedProjectId(p.projectId)); }, [params]);

    // Sync project selection — remove selectedProject from deps to avoid re-trigger loop
    useEffect(() => {
        if (!resolvedProjectId) return;
        if (selectedProject?.id === resolvedProjectId) return;
        const proj = projects.find(p => p.id === resolvedProjectId);
        if (proj) {
            selectProject(proj);
        } else {
            if (fetchedProjectRef.current === resolvedProjectId) return;
            fetchedProjectRef.current = resolvedProjectId;
            projectReqRef.current?.abort();
            const controller = new AbortController();
            projectReqRef.current = controller;
            fetch(`/api/projects/${resolvedProjectId}`, { signal: controller.signal })
                .then(r => r.json())
                .then(data => { if (data.project) selectProject(data.project); })
                .catch(() => { });
        }
    }, [resolvedProjectId, projects]); // eslint-disable-line react-hooks/exhaustive-deps

    // Fetch files once per project ID — not re-triggered by selection changes
    useEffect(() => {
        if (!resolvedProjectId) return;
        refreshFiles(resolvedProjectId);
    }, [resolvedProjectId]); // eslint-disable-line react-hooks/exhaustive-deps
    useEffect(() => () => projectReqRef.current?.abort(), []);

    const project = selectedProject;

    // Auto-show job tracker when migration starts
    useEffect(() => {
        if (isMigrating && !showJobTracker) {
            setShowJobTracker(true);
        }
    }, [isMigrating]); // eslint-disable-line react-hooks/exhaustive-deps

    // Auto-select the most recently migrated file so the diff pops up immediately
    const prevCompletedRef = useRef(0);
    useEffect(() => {
        const donJobs = migrationJobs.filter(j => j.status === 'done');
        if (donJobs.length > prevCompletedRef.current) {
            prevCompletedRef.current = donJobs.length;
            const latestJob = donJobs[donJobs.length - 1];
            const migratedFile = files.find(f => f.id === latestJob?.fileId);
            if (migratedFile?.migratedContent) {
                selectFile(migratedFile);
                setCenterView('diff');
            }
        }
    }, [migrationJobs]); // eslint-disable-line react-hooks/exhaustive-deps

    // Attach socket + restore any in-flight batch when opening the editor.
    useEffect(() => {
        if (!resolvedProjectId) return;
        markProjectLoaded(resolvedProjectId);
        initSocket(resolvedProjectId);
        void useMigrationStore.getState().syncJobs(resolvedProjectId);
    }, [resolvedProjectId, initSocket, markProjectLoaded]);

    const projectFiles = useMemo(() => {
        if (!project) return [];
        return files.filter(f => f.projectId === project.id && f.type === 'file');
    }, [project, files]);

    const migrationState = useMemo(() => {
        if (!project) return { totalFiles: 0, completedFiles: 0, hasMigrated: false, hasStarted: false, isFullyComplete: false };
        const completedFiles = projectFiles.filter(f => f.status === 'completed').length;
        const inProgressFiles = projectFiles.filter(f => f.status === 'in-progress').length;
        const failedFiles = projectFiles.filter(f => f.status === 'failed').length;
        const pendingFiles = projectFiles.filter(f => f.status === 'pending').length;
        const isFullyComplete = projectFiles.length > 0
            && completedFiles === projectFiles.length
            && inProgressFiles === 0
            && pendingFiles === 0
            && !isMigrating;
        return {
            totalFiles: projectFiles.length,
            completedFiles,
            hasMigrated: completedFiles > 0,
            hasStarted: isMigrating || completedFiles > 0 || failedFiles > 0 || inProgressFiles > 0 || pendingFiles > 0,
            isFullyComplete,
        };
    }, [project, projectFiles, isMigrating]);


    // Real-time streaming: show the token stream from the active job in center panel
    const liveStreamFile = useMemo(() => {
        if (!isMigrating) return null;
        const runningJob = migrationJobs.find(j => j.status === 'running');
        if (!runningJob || !runningJob.streamedContent) return null;
        const baseFile = files.find(f => f.id === runningJob.fileId);
        if (!baseFile) return null;
        return { ...baseFile, migratedContent: runningJob.streamedContent, status: 'in-progress' as const };
    }, [isMigrating, migrationJobs, files]);

    const handleSourceFileSelect = useCallback((file: ProjectFile) => {
        selectFile(file);
        setCenterView(file.migratedContent && file.status === 'completed' ? 'diff' : 'source');
    }, [selectFile]);

    const handleMigratedFileSelect = useCallback((file: ProjectFile) => {
        selectFile(file);
        setCenterView(file.migratedContent && file.status === 'completed' ? 'diff' : 'migrated');
    }, [selectFile]);

    const handleAccept = useCallback(() => {
        if (selectedFile) addToast({ type: 'success', title: 'Accepted', message: `Accepted migrated ${selectedFile.name}` });
    }, [selectedFile, addToast]);

    const handleReject = useCallback(() => {
        if (selectedFile) {
            addToast({ type: 'warning', title: 'Rejected', message: `Reverted ${selectedFile.name}` });
            setCenterView('source');
        }
    }, [selectedFile, addToast]);

    const handleStartMigration = useCallback(async () => {
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

        const projectFiles = files.filter(f => f.projectId === project.id && f.type === 'file');
        const fileIds = projectFiles.map(f => f.id);
        const existingMigrationId = projectFiles.find(f => f.activeMigrationId)?.activeMigrationId;
        const migrationId = existingMigrationId || generateAlphanumericId(10);

        try {
            const { settings: savedSettings } = await llmSettingsApi.save({
                activeProvider: llmSettings.activeProvider,
            });
            updateLLMSettings(savedSettings);
            resetProjectTiming(project.id, new Date().toISOString());

            addToast({
                type: 'info',
                title: 'Migration Started',
                message: `Publishing ${fileIds.length} files to the migration queue...`,
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
            setShowJobTracker(true);
        } catch (error: unknown) {
            addToast({
                type: 'error',
                title: 'Migration Blocked',
                message: error instanceof Error ? error.message : 'Failed to start migration.',
            });
            refreshFiles(project.id, true);
        }
    }, [project, files, addToast, llmSettings.activeProvider, updateLLMSettings, resetProjectTiming, startBatchMigration, user?.id, refreshFiles]);

    useEffect(() => {
        if (isMigrating) {
            migrationStartedRef.current = true;
        }
    }, [isMigrating]);

    useEffect(() => {
        if (migrationStartedRef.current && migrationState.isFullyComplete) {
            migrationStartedRef.current = false;
            setShowCompletionModal(true);
        }
    }, [migrationState.isFullyComplete]);

    if (!project) {
        return (
            <div className="h-full flex items-center justify-center bg-gray-50 dark:bg-gray-950">
                <CodeBracketIcon className="h-12 w-12 text-gray-300 mx-auto" />
            </div>
        );
    }

    return (
        <ErrorBoundary>
            <div className="flex flex-col bg-gray-100" style={{ height: 'calc(100vh - 64px)' }}>

                {/* ── Top Bar ── */}
                <div className="flex items-center justify-between px-4 py-2 bg-white dark:bg-gray-950 border-b border-gray-200 dark:border-gray-800 shrink-0">
                    <nav className="flex items-center gap-1.5 text-[11px] font-medium" aria-label="Breadcrumb">
                        <button onClick={() => router.push('/dashboard/organizations')}
                            className="flex items-center gap-1 text-gray-400 hover:text-primary-600 transition-colors">
                            <CodeBracketIcon className="h-3.5 w-3.5" />
                        </button>
                        <ChevronRightIcon className="h-3 w-3 text-gray-300" />
                        <button onClick={() => router.push(`/dashboard/projects/${project.id}`)}
                            className="text-gray-500 dark:text-gray-400 hover:text-primary-600 transition-colors truncate max-w-[120px]">
                            {project.name}
                        </button>
                        <ChevronRightIcon className="h-3 w-3 text-gray-300" />
                        <span className="text-primary-600 font-bold tracking-tight">Editor</span>
                    </nav>

                    <div className="flex items-center gap-2">
                        {migrationState.hasStarted && (
                            <div className="flex items-center gap-0.5 bg-gray-100 rounded-lg p-0.5">
                                {([
                                    { key: 'source' as CenterView, label: 'Source', icon: CodeBracketIcon },
                                    { key: 'diff' as CenterView, label: 'Diff', icon: ArrowsRightLeftIcon },
                                    { key: 'migrated' as CenterView, label: 'Migrated', icon: EyeIcon },
                                ]).map(tab => (
                                    <button key={tab.key} onClick={() => setCenterView(tab.key)}
                                        className={`flex items-center gap-1 px-2.5 py-1.5 text-[11px] font-medium rounded-md transition-all ${centerView === tab.key ? 'bg-white dark:bg-gray-950 text-primary-700 shadow-sm' : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:text-gray-300'
                                            }`}>
                                        <tab.icon className="h-3.5 w-3.5" /> {tab.label}
                                    </button>
                                ))}
                            </div>
                        )}

                        <div className="h-5 w-px bg-gray-200" />

                        <button onClick={() => setShowImport(true)}
                            className="flex items-center gap-1 px-2.5 py-1.5 text-[11px] font-medium text-gray-600 dark:text-gray-400 bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-lg hover:bg-gray-50 transition-colors">
                            <ArrowUpTrayIcon className="h-3.5 w-3.5" /> Import
                        </button>
                        <button onClick={() => setShowExport(true)}
                            disabled={!migrationState.isFullyComplete}
                            title={migrationState.isFullyComplete ? 'Export migrated code' : 'Complete migration before exporting'}
                            className="flex items-center gap-1 px-2.5 py-1.5 text-[11px] font-medium text-white bg-primary-600 hover:bg-primary-700 disabled:bg-gray-300 disabled:cursor-not-allowed rounded-lg transition-colors shadow-sm">
                            <ArrowDownTrayIcon className="h-3.5 w-3.5" /> Export
                        </button>
                    </div>
                </div>

                {/* ── Main Content Area ── */}
                <div className="flex-1 min-h-0">
                    {isMigrating ? (
                        /* ── Active Migration View with Transfer Animation ── */
                        <ActiveMigrationView projectFiles={projectFiles} />
                    ) : !migrationState.hasStarted ? (
                        /* ── Pre-Migration: Source Tree + CTA ── */
                        <div className="h-full flex">
                            <div className="w-[280px] shrink-0 border-r border-gray-200 dark:border-gray-800">
                                <FileTree
                                    onSelectFile={handleSourceFileSelect}
                                    selectedFileId={selectedFile?.id || null}
                                    projectId={project.id}
                                    mode="source"
                                    title="MuleSoft Source"
                                    accent="primary"
                                />
                            </div>

                            <div className="flex-1 flex flex-col min-w-0 min-h-0">
                                {selectedFile ? (
                                    <CodeEditor file={selectedFile} mode="source" readOnly />
                                ) : migrationState.totalFiles === 0 ? (
                                    /* ── No files imported yet ── */
                                    <div className="h-full flex items-center justify-center bg-white dark:bg-gray-950">
                                        <div className="text-center max-w-sm px-8 py-12 bg-gray-50/50 dark:bg-gray-900/30 rounded-3xl border border-gray-100 dark:border-gray-800 shadow-sm">
                                            <div className="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-amber-400 to-orange-500 rounded-2xl flex items-center justify-center shadow-lg shadow-orange-500/20">
                                                <ArrowUpTrayIcon className="h-8 w-8 text-white" />
                                            </div>
                                            <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">No Files Yet</h2>
                                            <p className="text-gray-500 dark:text-gray-400 text-xs mb-8 leading-relaxed">
                                                Import your MuleSoft project from a Git repository or ZIP file to begin the transformation.
                                            </p>
                                            <button
                                                onClick={() => setShowImport(true)}
                                                className="inline-flex items-center gap-2 px-6 py-2.5 bg-gray-900 dark:bg-primary-600 hover:bg-black dark:hover:bg-primary-700 text-white font-semibold text-xs rounded-xl transition-all shadow-md active:scale-95"
                                            >
                                                <ArrowUpTrayIcon className="h-4 w-4" />
                                                Import Source
                                            </button>
                                            <p className="text-[10px] text-gray-400 mt-4 font-medium uppercase tracking-wider">GitHub · GitLab · ZIP · JAR</p>
                                        </div>
                                    </div>
                                ) : (
                                    /* ── Files imported, ready to migrate ── */
                                    <div className="h-full flex items-center justify-center bg-white dark:bg-gray-950">
                                        <div className="text-center max-w-sm px-8 py-12 bg-primary-50/30 dark:bg-primary-900/10 rounded-3xl border border-primary-100/50 dark:border-primary-800/30 shadow-sm relative overflow-hidden">
                                            <div className="absolute top-0 right-0 p-4 opacity-5">
                                                <SparklesIcon className="h-24 w-24 text-primary-600" />
                                            </div>
                                            <div className="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-primary-500 to-primary-700 rounded-2xl flex items-center justify-center shadow-lg shadow-primary-500/20">
                                                <RocketLaunchIcon className="h-8 w-8 text-white" />
                                            </div>
                                            <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">Ready to Migrate</h2>
                                            <p className="text-gray-500 dark:text-gray-400 text-xs mb-8 leading-relaxed">
                                                Your project is ready. <span className="text-primary-600 font-semibold">{migrationState.totalFiles} files</span> detected.
                                                Each file will be processed as an independent job with live synthesis.
                                            </p>
                                            <button
                                                onClick={handleStartMigration}
                                                disabled={isMigrating}
                                                className={`inline-flex items-center gap-2 px-8 py-3 font-bold text-xs rounded-xl transition-all shadow-lg active:scale-95 ${
                                                    isMigrating
                                                        ? 'bg-gray-400 cursor-not-allowed text-white shadow-none'
                                                        : 'bg-primary-600 hover:bg-primary-700 text-white shadow-primary-500/25'
                                                }`}
                                            >
                                                {isMigrating ? (
                                                    <>
                                                        <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                                                            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                                            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
                                                        </svg>
                                                        Migration Running...
                                                    </>
                                                ) : (
                                                    <>
                                                        <SparklesIcon className="h-4 w-4" />
                                                        Begin Migration
                                                    </>
                                                )}
                                            </button>

                                            <div className="mt-8 grid grid-cols-3 gap-3">
                                                {[
                                                    { label: 'XML → TS', color: 'primary' },
                                                    { label: 'DWL → JS', color: 'emerald' },
                                                    { label: 'DWL → DWL', color: 'amber' },
                                                ].map(feat => (
                                                    <div key={feat.label} className="bg-white/80 dark:bg-gray-950/80 rounded-lg py-1.5 border border-primary-50 dark:border-primary-900/50">
                                                        <div className="text-[9px] font-bold text-gray-400 uppercase">{feat.label}</div>
                                                    </div>
                                                ))}
                                            </div>
                                        </div>
                                    </div>
                                )}
                            </div>
                        </div>
                    ) : (
                        /* ── Post-Migration: Source | Center | Migrated ── */
                        <ResizablePanels
                            className="h-full"
                            panels={[
                                {
                                    id: 'source-tree',
                                    defaultWidth: 240,
                                    minWidth: 160,
                                    maxWidth: 480,
                                    content: (
                                        <div className="h-full border-r border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950">
                                            <FileTree
                                                onSelectFile={handleSourceFileSelect}
                                                selectedFileId={selectedFile?.id || null}
                                                projectId={project.id}
                                                mode="source"
                                                title="MuleSoft Source"
                                                accent="primary"
                                            />
                                        </div>
                                    ),
                                },
                                {
                                    id: 'center',
                                    defaultWidth: 0,
                                    minWidth: 300,
                                    maxWidth: 99999,
                                    grow: true,
                                    content: (
                                        <div className="h-full flex flex-col">
                                            {liveStreamFile ? (
                                                /* Live streaming view — raw pre tag avoids Monaco cursor-jump on each token */
                                                <LiveStreamPanel file={liveStreamFile} />
                                            ) : centerView === 'diff' ? (
                                                <DiffViewer file={selectedFile} onAccept={handleAccept} onReject={handleReject} />
                                            ) : centerView === 'migrated' ? (
                                                <CodeEditor file={selectedFile} mode="migrated" readOnly />
                                            ) : (
                                                <CodeEditor file={selectedFile} mode="source" readOnly />
                                            )}
                                        </div>
                                    ),
                                },
                                {
                                    id: 'migrated-tree',
                                    defaultWidth: 240,
                                    minWidth: 160,
                                    maxWidth: 480,
                                    content: (
                                        <div className="h-full border-l border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950">
                                            <FileTree
                                                onSelectFile={handleMigratedFileSelect}
                                                selectedFileId={selectedFile?.id || null}
                                                projectId={project.id}
                                                mode="migrated"
                                                title={getPlatformStrategy(selectedProject?.targetPlatform, selectedProject?.migrationType, selectedProject?.targetRuntime).outputPaneTitle}
                                                accent="emerald"
                                            />
                                        </div>
                                    ),
                                },
                            ]}
                        />
                    )}
                </div>

                {/* ── Migration Panel (controls) ── */}
                <div className="shrink-0">
                    <MigrationPanel
                        onToggleJobTracker={() => setShowJobTracker(p => !p)}
                        showJobTracker={showJobTracker}
                    />
                </div>

                {/* ── Job Tracker ── */}
                {showJobTracker && (
                    <div className="shrink-0" style={{ height: 320 }}>
                        <JobTracker />
                    </div>
                )}

                {/* ── Modals ── */}
                {showExport && <ExportPanel onClose={() => setShowExport(false)} />}
                {showImport && (
                    <ImportPanel
                        onClose={() => {
                            setShowImport(false);
                            if (project) refreshFiles(project.id, true);
                        }}
                    />
                )}
                <Modal
                    isOpen={showCompletionModal}
                    onClose={() => setShowCompletionModal(false)}
                    title="Migration Completed"
                    size="md"
                >
                    <div className="flex flex-col items-center justify-center py-6 text-center">
                        <div className="h-16 w-16 bg-green-100 dark:bg-green-900/30 rounded-full flex items-center justify-center mb-4">
                            <CheckCircleIcon className="h-10 w-10 text-green-600 dark:text-green-400" />
                        </div>
                        <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">Migration Successful</h3>
                        <p className="text-sm text-gray-500 dark:text-gray-400 mb-6 px-4">
                            Successfully converted <span className="font-semibold text-gray-900 dark:text-white">{migrationState.completedFiles}</span> files to modern AWS microservices.
                            You can now review the diffs, modify the output, or export the full package.
                        </p>
                        <div className="flex gap-3 w-full max-w-[200px]">
                            <button
                                onClick={() => setShowCompletionModal(false)}
                                className="flex-1 py-2 px-4 bg-gray-100 hover:bg-gray-200 dark:bg-gray-800 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-200 font-medium rounded-lg transition-colors text-sm"
                            >
                                Review Code
                            </button>
                            <button
                                onClick={() => {
                                    setShowCompletionModal(false);
                                    setShowExport(true);
                                }}
                                className="flex-1 py-2 px-4 bg-primary-600 hover:bg-primary-700 text-white font-medium rounded-lg transition-colors text-sm"
                            >
                                Export
                            </button>
                        </div>
                    </div>
                </Modal>
            </div>
        </ErrorBoundary >
    );
}

function ActiveMigrationView({ projectFiles }: { projectFiles: any[] }) {
    const { selectedProject } = useApp();
    const completedCount = projectFiles.filter(f => f.status === 'completed').length;
    const totalCount = projectFiles.length;
    let pct = totalCount > 0 ? Math.round((completedCount / totalCount) * 100) : 0;
    if (pct >= 100) {
        pct = 95;
    }

    return (
        <div className="h-full flex bg-gray-50 dark:bg-gray-950 overflow-hidden">
            {/* Left Pane: Source files */}
            <div className="w-[280px] shrink-0 border-r border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 flex flex-col">
                <div className="p-4 border-b border-gray-100 dark:border-gray-900 bg-gray-50/50 dark:bg-gray-900/30">
                    <h3 className="text-xs font-black uppercase tracking-[0.2em] text-gray-700 dark:text-gray-300">MuleSoft Source</h3>
                    <p className="text-[10px] font-medium text-gray-400 mt-0.5">{totalCount} files converting</p>
                </div>
                <div className="flex-1 overflow-y-auto p-4 space-y-2">
                    {projectFiles.map(file => (
                        <div key={file.id} className={`flex items-center gap-2.5 p-2.5 rounded-xl border transition-all ${
                            file.status === 'completed'
                                ? 'border-emerald-500/20 bg-emerald-500/[0.02]'
                                : file.status === 'in-progress'
                                    ? 'border-primary-500/20 bg-primary-500/[0.02] shadow-sm'
                                    : 'border-gray-100 dark:border-gray-900 bg-white dark:bg-white/[0.02]'
                        }`}>
                            <span className="p-1 rounded-lg bg-gray-50 dark:bg-gray-900">
                                <DocumentTextIcon className={`h-4 w-4 ${file.status === 'completed' ? 'text-emerald-500' : 'text-primary-500'}`} />
                            </span>
                            <div className="min-w-0 flex-1">
                                <p className="text-xs font-bold text-gray-700 dark:text-gray-300 truncate">{file.name}</p>
                                <p className="text-[9px] text-gray-400 font-medium truncate">{file.path}</p>
                            </div>
                            {file.status === 'completed' && (
                                <span className="text-xs font-black text-emerald-500 bg-emerald-500/10 h-5 w-5 rounded-full flex items-center justify-center border border-emerald-500/20">✓</span>
                            )}
                            {file.status === 'in-progress' && (
                                <span className="flex h-2 w-2 relative">
                                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary-400 opacity-75"></span>
                                    <span className="relative inline-flex rounded-full h-2 w-2 bg-primary-500"></span>
                                </span>
                            )}
                        </div>
                    ))}
                </div>
            </div>

            {/* Center Pane: Animation */}
            <div className="flex-1 flex flex-col items-center justify-center p-8 bg-gray-50/50 dark:bg-gray-900/10 relative overflow-hidden">
                <style dangerouslySetInnerHTML={{__html: `
                    @keyframes particleFlow {
                        0% { transform: translate(-100px, 0) scale(0.8); opacity: 0; }
                        20% { opacity: 1; }
                        80% { opacity: 1; }
                        100% { transform: translate(100px, 0) scale(0.8); opacity: 0; }
                    }
                    .particle-1 { animation: particleFlow 4s infinite linear; }
                    .particle-2 { animation: particleFlow 4s infinite linear 1.3s; }
                    .particle-3 { animation: particleFlow 4s infinite linear 2.6s; }
                `}} />

                {/* Flow particles */}
                <div className="absolute inset-0 flex items-center justify-center pointer-events-none opacity-40">
                    <div className="w-[300px] h-[100px] relative">
                        <div className="particle-1 absolute left-1/2 top-1/4 -translate-y-1/2 bg-gradient-to-r from-primary-500 to-emerald-500 rounded-full blur-[2px] p-2 flex items-center justify-center text-white">
                            <DocumentTextIcon className="h-5 w-5" />
                        </div>
                        <div className="particle-2 absolute left-1/2 top-1/2 -translate-y-1/2 bg-gradient-to-r from-violet-500 to-indigo-500 rounded-full blur-[2px] p-2 flex items-center justify-center text-white">
                            <CodeBracketIcon className="h-5 w-5" />
                        </div>
                        <div className="particle-3 absolute left-1/2 top-3/4 -translate-y-1/2 bg-gradient-to-r from-emerald-500 to-teal-500 rounded-full blur-[2px] p-2 flex items-center justify-center text-white">
                            <CommandLineIcon className="h-5 w-5" />
                        </div>
                    </div>
                </div>

                {/* Central Brain/Rotating Node */}
                <div className="relative mb-8 z-10">
                    {/* Pulsing ring outer */}
                    <div className="absolute inset-0 rounded-full bg-primary-500/10 animate-ping duration-2000" />
                    {/* Rotating dashed ring */}
                    <div className="w-32 h-32 rounded-full border-2 border-dashed border-primary-500/30 animate-spin [animation-duration:20s] flex items-center justify-center" />
                    {/* Inner glowing icon */}
                    <div className="absolute inset-4 rounded-full bg-gradient-to-br from-primary-500 to-primary-700 shadow-xl shadow-primary-500/20 flex items-center justify-center text-white">
                        <ArrowPathIcon className="h-10 w-10 animate-spin" />
                    </div>
                </div>

                {/* Status Texts */}
                <div className="text-center z-10 max-w-md">
                    <h2 className="text-2xl font-black text-primary-600 dark:text-primary-400 mb-6">
                        Your migration is in progress
                    </h2>

                    {/* Progress details */}
                    <div className="bg-white dark:bg-gray-950 p-6 rounded-2xl border border-gray-100 dark:border-gray-900 shadow-xl shadow-gray-200/5 dark:shadow-none space-y-4">
                        <div className="flex justify-between items-center text-xs">
                            <span className="font-bold text-gray-400 uppercase tracking-widest">Progress</span>
                            <span className="font-black text-primary-600 dark:text-primary-400 tabular-nums">{completedCount} / {totalCount} Files ({pct}%)</span>
                        </div>
                        <div className="h-2 w-full bg-gray-100 dark:bg-gray-900 rounded-full overflow-hidden">
                            <div className="h-full bg-gradient-to-r from-primary-500 to-emerald-500 rounded-full transition-all duration-500 ease-out" style={{ width: `${pct}%` }} />
                        </div>
                        <div className="flex items-center gap-2 text-[10px] text-gray-400 font-medium justify-center uppercase tracking-widest animate-pulse">
                            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                            Neural codegen & self-correction active
                        </div>
                    </div>
                </div>
            </div>

            {/* Right Pane: Target files */}
            <div className="w-[280px] shrink-0 border-l border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 flex flex-col">
                <div className="p-4 border-b border-gray-100 dark:border-gray-900 bg-gray-50/50 dark:bg-gray-900/30">
                    <h3 className="text-xs font-black uppercase tracking-[0.2em] text-gray-700 dark:text-gray-300">
                        {getPlatformStrategy(selectedProject?.targetPlatform, selectedProject?.migrationType, selectedProject?.targetRuntime).outputPaneTitle}
                    </h3>
                    <p className="text-[10px] font-medium text-gray-400 mt-0.5">{completedCount} files generated</p>
                </div>
                <div className="flex-1 overflow-y-auto p-4 space-y-2">
                    {projectFiles.map(file => {
                        const strat = getPlatformStrategy(selectedProject?.targetPlatform, selectedProject?.migrationType, selectedProject?.targetRuntime);
                        const ext = file.name.split('.').pop() || '';
                        const targetExt = strat.fileExtensionMap[ext] || 'py';
                        const targetName = file.name.replace(new RegExp(`\\.${ext}$`), `.${targetExt}`);
                        const targetPath = file.path.replace("application/src/", "src/app/").replace("src/main/mule/", "src/app/flows/");
                        return (
                            <div key={file.id} className={`flex items-center gap-2.5 p-2.5 rounded-xl border transition-all ${
                                file.status === 'completed'
                                    ? 'border-emerald-500/20 bg-emerald-500/[0.02]'
                                    : file.status === 'in-progress'
                                        ? 'border-primary-500/20 bg-primary-500/[0.02] shadow-sm'
                                        : 'opacity-40 border-gray-100 dark:border-gray-900 bg-white dark:bg-white/[0.02]'
                            }`}>
                                <span className="p-1 rounded-lg bg-gray-50 dark:bg-gray-900">
                                    <CommandLineIcon className={`h-4 w-4 ${file.status === 'completed' ? 'text-emerald-500' : 'text-gray-400'}`} />
                                </span>
                                <div className="min-w-0 flex-1">
                                    <p className="text-xs font-bold text-gray-700 dark:text-gray-300 truncate">{targetName}</p>
                                    <p className="text-[9px] text-gray-400 font-medium truncate">{targetPath}</p>
                                </div>
                                {file.status === 'completed' && (
                                    <span className="text-xs font-black text-emerald-500 bg-emerald-500/10 h-5 w-5 rounded-full flex items-center justify-center border border-emerald-500/20">✓</span>
                                )}
                                {file.status === 'in-progress' && (
                                    <span className="flex h-2 w-2 relative">
                                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary-400 opacity-75"></span>
                                        <span className="relative inline-flex rounded-full h-2 w-2 bg-primary-500"></span>
                                    </span>
                                )}
                            </div>
                        );
                    })}
                </div>
            </div>
        </div>
    );
}
