'use client';

import React, { createContext, useContext, useState, useCallback, useRef, useEffect, ReactNode } from 'react';
import {
    Organization, Workspace, Project, ProjectFile,
    MigrationLog, FileStatus, Toast, MigrationJob, MigrationSessionState,
    LLMProviderType, LLMSettings, MigrationBatch
} from '../lib/types';
import {
    orgApi, workspaceApi, projectApi, fileApi,
    migrationApi, importApi, exportApi, llmSettingsApi
} from '../lib/api';
import { useAuth } from './AuthContext';

/* ─── Context shape ─── */
interface AppContextType {
    // Organizations
    organizations: Organization[];
    selectedOrg: Organization | null;
    selectOrg: (org: Organization | null) => void;
    addOrganization: (org: Omit<Organization, 'id' | 'createdAt' | 'workspaceCount'>) => Promise<boolean>;
    refreshOrganizations: () => Promise<void>;

    // Projects
    projects: Project[];
    selectedProject: Project | null;
    selectProject: (p: Project | null) => void;
    addProject: (p: Omit<Project, 'id' | 'createdAt' | 'lastActivity' | 'totalFiles' | 'migratedFiles' | 'failedFiles' | 'status' | 'migrationRuns'>) => Promise<Project | null>;
    updateProject: (id: string, updates: Partial<Project>) => void;
    deleteProject: (projectId: string) => Promise<boolean>;
    refreshProjects: (workspaceId?: string, force?: boolean) => Promise<void>;

    // Migration Batches (project-level run bundles)
    migrationBatches: MigrationBatch[];
    refreshBatches: (projectId: string, force?: boolean) => Promise<void>;

    // Workspaces
    workspaces: Workspace[];
    selectedWorkspace: Workspace | null;
    selectWorkspace: (ws: Workspace | null) => void;
    addWorkspace: (ws: Omit<Workspace, 'id' | 'projectCount'>) => void;
    deleteWorkspace: (orgId: string, workspaceId: string) => Promise<boolean>;
    refreshWorkspaces: (orgId: string, force?: boolean) => Promise<void>;

    // Files
    files: ProjectFile[];
    selectedFile: ProjectFile | null;
    selectFile: (f: ProjectFile | null) => void;
    updateFileStatus: (fileId: string, status: FileStatus) => void;
    bulkUpdateFileStatus: (fileIds: string[], status: FileStatus) => void;
    updateFileContent: (fileId: string, content: string) => void;
    updateFileMigratedContent: (fileId: string, content: string) => void;
    syncFileMigrationResult: (fileId: string, migratedContent: string, status?: FileStatus) => void;
    getFileById: (id: string) => ProjectFile | undefined;
    getProjectFiles: (projectId: string) => ProjectFile[];
    refreshFiles: (
        projectId: string,
        force?: boolean,
        options?: { page?: number; take?: number; includeContent?: boolean; includeMigrations?: boolean }
    ) => Promise<void>;

    // Migration engine — job-based SSE
    migrationLogs: MigrationLog[];
    isMigrating: boolean;
    migrationProgress: number;
    currentMigratingFile: string | null;
    migrationJobs: MigrationJob[];
    migrationSession: MigrationSessionState | null;
    startMigration: (reMigrate?: boolean) => void;
    stopMigration: () => void;
    retryFailed: () => void;
    clearLogs: () => void;

    // LLM Provider
    activeLLMProvider: LLMProviderType;
    llmSettings: LLMSettings | null;
    refreshLLMSettings: () => void;
    updateActiveLLMProvider: (provider: LLMProviderType) => void;

    // Toast
    toasts: Toast[];
    addToast: (toast: Omit<Toast, 'id'>) => void;
    removeToast: (id: string) => void;

    // UI
    globalLoading: boolean;
    sidebarCollapsed: boolean;
    toggleSidebar: () => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

/* ─── Provider ─── */
export function AppProvider({ children }: { children: ReactNode }) {
    const [organizations, setOrganizations] = useState<Organization[]>([]);
    const [selectedOrg, setSelectedOrg] = useState<Organization | null>(null);
    const [workspaces, setWorkspaces] = useState<Workspace[]>([]);
    const [selectedWorkspace, setSelectedWorkspace] = useState<Workspace | null>(null);
    const [projects, setProjects] = useState<Project[]>([]);
    const [selectedProject, setSelectedProject] = useState<Project | null>(null);
    const [files, setFiles] = useState<ProjectFile[]>([]);
    const [selectedFile, setSelectedFile] = useState<ProjectFile | null>(null);
    const [migrationLogs, setMigrationLogs] = useState<MigrationLog[]>([]);
    const [isMigrating, setIsMigrating] = useState(false);
    const [migrationProgress, setMigrationProgress] = useState(0);
    const [currentMigratingFile, setCurrentMigratingFile] = useState<string | null>(null);
    const [migrationJobs, setMigrationJobs] = useState<MigrationJob[]>([]);
    const [migrationSession, setMigrationSession] = useState<MigrationSessionState | null>(null);
    const [migrationBatches, setMigrationBatches] = useState<MigrationBatch[]>([]);
    const [toasts, setToasts] = useState<Toast[]>([]);
    const [globalLoading, setGlobalLoading] = useState(false);
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [activeLLMProvider, setActiveLLMProvider] = useState<LLMProviderType>('nova');
    const [llmSettings, setLlmSettings] = useState<LLMSettings | null>(null);

    const { user } = useAuth();
    const eventSourceRef = useRef<EventSource | null>(null);

    // One-shot fetch cache — prevents duplicate requests on re-renders
    const fetchedWorkspaceOrgs = useRef<Set<string>>(new Set());
    const fetchedProjectWorkspaces = useRef<Set<string>>(new Set());
    const fetchedFileProjects = useRef<Set<string>>(new Set());

    /* ─── Initial data load ─── */
    useEffect(() => {
        setGlobalLoading(true);
        orgApi.list()
            .then(({ organizations }) => setOrganizations(organizations))
            .catch(() => { })
            .finally(() => setGlobalLoading(false));
    }, []);

    /* ─── Load LLM Settings (Sync LocalStorage + Backend) ─── */
    useEffect(() => {
        if (!user) {
            setLlmSettings(null);
            setActiveLLMProvider('nova');
            return;
        }

        const localKey = `ms_settings_${user.id}`;
        try {
            const cached = localStorage.getItem(localKey);
            if (cached) {
                const parsed = JSON.parse(cached) as LLMSettings;
                setLlmSettings(parsed);
                setActiveLLMProvider(parsed.activeProvider);
            }
        } catch { }

        // Always fetch from server to guarantee sync
        llmSettingsApi.get()
            .then(({ settings }) => {
                setActiveLLMProvider(settings.activeProvider);
                setLlmSettings(settings);
                localStorage.setItem(localKey, JSON.stringify(settings));
            })
            .catch(() => { });
    }, [user]);

    /* ─── Explicit LLM Settings Persistence Hook ─── */
    useEffect(() => {
        if (!user || !llmSettings) return;
        localStorage.setItem(`ms_settings_${user.id}`, JSON.stringify(llmSettings));
    }, [llmSettings, user]);

    /* ─── Toasts (Moved up to avoid hoisting issues) ─── */
    const addToast = useCallback((toast: Omit<Toast, 'id'>) => {
        const id = typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function'
            ? `toast-${crypto.randomUUID()}`
            : `toast-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
        setToasts(prev => [...prev, { ...toast, id }]);
        setTimeout(() => setToasts(prev => prev.filter(t => t.id !== id)), 5000);
    }, []);

    const removeToast = useCallback((id: string) => {
        setToasts(prev => prev.filter(t => t.id !== id));
    }, []);

    /* ─── Global Error Handler Helper ─── */
    const withErrorHandling = useCallback(async <T,>(
        promise: Promise<T>,
        errorTitle = 'Action Failed'
    ): Promise<T | null> => {
        try {
            return await promise;
        } catch (err: any) {
            addToast({
                type: 'error',
                title: errorTitle,
                message: err.message || 'An unexpected error occurred.',
            });
            return null;
        }
    }, [addToast]);

    /* ─── Refresh helpers (cached — skip server round-trip if already fetched) ─── */
    const refreshOrganizations = useCallback(async () => {
        const res = await withErrorHandling(orgApi.list(), 'Failed to load Organizations');
        if (res) setOrganizations(res.organizations);
    }, [withErrorHandling]);

    const refreshWorkspaces = useCallback(async (orgId: string, force = false) => {
        if (!force && fetchedWorkspaceOrgs.current.has(orgId)) return;
        const res = await withErrorHandling(workspaceApi.list(orgId), 'Failed to load Workspaces');
        if (res) {
            setWorkspaces(res.workspaces);
            fetchedWorkspaceOrgs.current.add(orgId);
        }
    }, [withErrorHandling]);

    const refreshProjects = useCallback(async (workspaceId?: string, force = false) => {
        const key = workspaceId ?? '__all__';
        if (!force && fetchedProjectWorkspaces.current.has(key)) return;
        const res = await withErrorHandling(projectApi.list(workspaceId), 'Failed to load Projects');
        if (res) {
            setProjects(res.projects);
            fetchedProjectWorkspaces.current.add(key);
        }
    }, [withErrorHandling]);

    const refreshFiles = useCallback(async (
        projectId: string,
        force = false,
        options?: { page?: number; take?: number; includeContent?: boolean; includeMigrations?: boolean }
    ) => {
        if (force) fetchedFileProjects.current.delete(projectId);
        if (!force && fetchedFileProjects.current.has(projectId)) return;
        const res = await withErrorHandling(
            fileApi.list(projectId, { includeContent: true, ...options }),
            'Failed to load Project Files'
        );
        if (res) {
            setFiles(prev => [
                ...prev.filter(f => f.projectId !== projectId),
                ...res.files,
            ]);
            fetchedFileProjects.current.add(projectId);
        }
    }, [withErrorHandling]);

    const refreshBatches = useCallback(async (projectId: string, _force = false) => {
        const res = await withErrorHandling(migrationApi.getBatches(projectId), 'Failed to load Migration Batches');
        if (res) {
            setMigrationBatches(prev => [
                ...prev.filter(b => b.projectId !== projectId),
                ...res.batches,
            ]);
        }
    }, [withErrorHandling]);

    /* ─── Organization CRUD ─── */
    const addOrganization = useCallback(async (org: Omit<Organization, 'id' | 'createdAt' | 'workspaceCount'>) => {
        const res = await withErrorHandling(orgApi.create({
            name: org.name, description: org.description, owner: org.owner, logo: org.logo
        }), 'Failed to create Organization');
        if (res) {
            setOrganizations(prev => [...prev, res.organization]);
            return true;
        }
        return false;
    }, [withErrorHandling]);

    /* ─── Workspace CRUD ─── */
    const addWorkspace = useCallback(async (ws: Omit<Workspace, 'id' | 'projectCount'>) => {
        const res = await withErrorHandling(workspaceApi.create({
            orgId: ws.orgId, name: ws.name, environment: ws.environment, memberCount: ws.memberCount
        }), 'Failed to create Workspace');
        if (res) {
            setWorkspaces(prev => [...prev, res.workspace]);
            // Invalidate cache so subsequent navigations fetch full data (e.g. calculated fields)
            fetchedWorkspaceOrgs.current.delete(ws.orgId);
        }
    }, [withErrorHandling]);

    /* ─── Project CRUD ─── */
    const addProject = useCallback(async (p: Omit<Project, 'id' | 'createdAt' | 'lastActivity' | 'totalFiles' | 'migratedFiles' | 'failedFiles' | 'status' | 'migrationRuns'>): Promise<Project | null> => {
        const res = await withErrorHandling(projectApi.create({
            workspaceId: p.workspaceId, orgId: p.orgId, name: p.name,
            description: p.description, migrationType: p.migrationType,
            targetRuntime: p.targetRuntime, sourceType: p.sourceType,
        }), 'Failed to create Project');

        if (res) {
            setProjects(prev => [...prev, res.project]);
            // Invalidate project list cache for this workspace
            fetchedProjectWorkspaces.current.delete(p.workspaceId);
            return res.project;
        }
        return null;
    }, [withErrorHandling]);

    const updateProject = useCallback(async (id: string, updates: Partial<Project>) => {
        const res = await withErrorHandling(projectApi.update(id, updates), 'Failed to update Project');
        if (res) setProjects(prev => prev.map(p => p.id === id ? res.project : p));
    }, [withErrorHandling]);

    const deleteProject = useCallback(async (projectId: string): Promise<boolean> => {
        try {
            const res = await fetch(`/api/projects/${projectId}`, { method: 'DELETE' });
            if (!res.ok) return false;

            const p = projects.find(proj => proj.id === projectId);
            const wsId = p?.workspaceId;
            const orgId = p?.orgId;

            // Refresh project list
            await refreshProjects(wsId, true);

            // CRITICAL: Refresh workspaces so projectCount is updated in UI
            if (orgId) {
                await refreshWorkspaces(orgId, true);
            }

            addToast({ type: 'success', title: 'Project Deleted', message: 'The project has been removed.' });
            return true;
        } catch {
            addToast({ type: 'error', title: 'Delete Failed', message: 'Could not delete the project.' });
            return false;
        }
    }, [projects, refreshProjects, refreshWorkspaces, addToast]);

    const deleteWorkspace = useCallback(async (orgId: string, workspaceId: string): Promise<boolean> => {
        try {
            const res = await fetch(`/api/workspaces?orgId=${orgId}&workspaceId=${workspaceId}`, { method: 'DELETE' });
            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.error || 'Delete failed');
            }

            await refreshWorkspaces(orgId, true);
            // Also refresh organizations to update workspaceCount
            await refreshOrganizations();

            addToast({ type: 'success', title: 'Workspace Deleted', message: 'The workspace has been removed.' });
            return true;
        } catch (err: any) {
            addToast({ type: 'error', title: 'Delete Failed', message: err.message || 'Could not delete the workspace.' });
            return false;
        }
    }, [refreshWorkspaces, refreshOrganizations, addToast]);

    const fetchingParents = useRef<Set<string>>(new Set());

    const selectProject = useCallback(async (p: Project | null) => {
        setSelectedProject(p);
        if (p) {
            // Auto-select parent organization
            setOrganizations(prevOrgs => {
                const org = prevOrgs.find(o => o.id === p.orgId);
                if (org) {
                    setSelectedOrg(org);
                } else if (!fetchingParents.current.has(p.orgId)) {
                    fetchingParents.current.add(p.orgId);
                    orgApi.get(p.orgId).then(({ organization }) => {
                        setSelectedOrg(organization);
                        setOrganizations(prev => {
                            if (prev.some(o => o.id === organization.id)) return prev;
                            return [...prev, organization];
                        });
                    }).catch(() => {}).finally(() => fetchingParents.current.delete(p.orgId));
                }
                return prevOrgs;
            });

            // Auto-select parent workspace
            setWorkspaces(prevWs => {
                const ws = prevWs.find(w => w.id === p.workspaceId);
                if (ws) {
                    setSelectedWorkspace(ws);
                } else if (!fetchingParents.current.has(p.workspaceId)) {
                    fetchingParents.current.add(p.workspaceId);
                    workspaceApi.get(p.workspaceId).then(({ workspace }) => {
                        setSelectedWorkspace(workspace);
                        setWorkspaces(prev => {
                            if (prev.some(w => w.id === workspace.id)) return prev;
                            return [...prev, workspace];
                        });
                    }).catch(() => {}).finally(() => fetchingParents.current.delete(p.workspaceId));
                }
                return prevWs;
            });
        }
    }, []);

    /* ─── File operations ─── */
    const updateFileStatus = useCallback(async (fileId: string, status: FileStatus) => {
        const res = await withErrorHandling(fileApi.update(fileId, { status }), 'Failed to update file status');
        if (res) {
            setFiles(prev => prev.map(f => f.id === fileId ? res.file : f));
            setSelectedFile(prev => prev && prev.id === fileId ? res.file : prev);
        }
    }, [withErrorHandling]);

    const bulkUpdateFileStatus = useCallback((fileIds: string[], status: FileStatus) => {
        const idSet = new Set(fileIds);
        setFiles(prev => prev.map(f => idSet.has(f.id) ? { ...f, status } : f));
        if (selectedFile && idSet.has(selectedFile.id)) {
            setSelectedFile(prev => prev ? { ...prev, status } : null);
        }
    }, [selectedFile]);

    const updateFileContent = useCallback(async (fileId: string, content: string) => {
        const res = await withErrorHandling(fileApi.update(fileId, { content }), 'Failed to save file content');
        if (res) {
            setFiles(prev => prev.map(f => f.id === fileId ? res.file : f));
            setSelectedFile(prev => prev && prev.id === fileId ? res.file : prev);
        }
    }, [withErrorHandling]);

    const updateFileMigratedContent = useCallback(async (fileId: string, migratedContent: string) => {
        const res = await withErrorHandling(fileApi.update(fileId, { migratedContent }), 'Failed to save migrated content');
        if (res) {
            setFiles(prev => prev.map(f => f.id === fileId ? res.file : f));
            setSelectedFile(prev => prev && prev.id === fileId ? res.file : prev);
        }
    }, [withErrorHandling]);

    const syncFileMigrationResult = useCallback((fileId: string, migratedContent: string, status: FileStatus = 'completed') => {
        setFiles(prev => prev.map(f => (
            f.id === fileId
                ? { ...f, status, migratedContent }
                : f
        )));
        setSelectedFile(prev => (
            prev && prev.id === fileId
                ? { ...prev, status, migratedContent }
                : prev
        ));
    }, []);

    const getFileById = useCallback((id: string) => files.find(f => f.id === id), [files]);
    const getProjectFiles = useCallback((projectId: string) => files.filter(f => f.projectId === projectId), [files]);

    /* ══════════════════════════════════════════════
       Migration Engine — SSE / EventSource based
       ══════════════════════════════════════════════ */
    const startMigration = useCallback((reMigrate = false) => {
        const projectId = selectedProject?.id;
        if (!projectId) return;

        // Close any existing connection
        if (eventSourceRef.current) {
            eventSourceRef.current.close();
            eventSourceRef.current = null;
        }

        setIsMigrating(true);
        setMigrationProgress(0);
        setMigrationJobs([]);
        setMigrationLogs([]);

        const es = new EventSource(`/api/migration/stream?projectId=${projectId}&action=start${reMigrate ? '&includeCompleted=true' : ''}`);
        eventSourceRef.current = es;

        /* ── session:start ── */
        es.addEventListener('session:start', (e) => {
            const data = JSON.parse(e.data);
            const session: MigrationSessionState = {
                projectId: data.projectId,
                sessionId: data.sessionId,
                status: 'running',
                jobs: data.jobs.map((j: any) => ({
                    ...j, progress: 0, streamedContent: '', logs: [],
                })),
                totalJobs: data.totalJobs,
                completedJobs: 0,
                failedJobs: 0,
                currentJobId: null,
                startedAt: new Date().toISOString(),
            };
            setMigrationSession(session);
            setMigrationJobs(session.jobs);
        });

        /* ── job:start ── */
        es.addEventListener('job:start', (e) => {
            const data = JSON.parse(e.data);
            setCurrentMigratingFile(data.fileName);
            setMigrationJobs(prev => prev.map(j =>
                j.id === data.jobId ? { ...j, status: 'running' as const, startedAt: new Date().toISOString() } : j
            ));
            setMigrationSession(prev => prev ? { ...prev, currentJobId: data.jobId } : prev);
        });

        /* ── job:token — real-time content streaming ── */
        es.addEventListener('job:token', (e) => {
            const data = JSON.parse(e.data);
            setMigrationJobs(prev => prev.map(j =>
                j.id === data.jobId ? { ...j, streamedContent: j.streamedContent + data.token } : j
            ));
        });

        /* ── job:progress ── */
        es.addEventListener('job:progress', (e) => {
            const data = JSON.parse(e.data);
            setMigrationJobs(prev => prev.map(j =>
                j.id === data.jobId ? { ...j, progress: data.progress } : j
            ));
        });

        /* ── job:log ── */
        es.addEventListener('job:log', (e) => {
            const data = JSON.parse(e.data);
            setMigrationLogs(prev => [data.log, ...prev]);

            if (data.jobId && data.jobId !== 'session') {
                setMigrationJobs(prev => prev.map(j =>
                    j.id === data.jobId ? { ...j, logs: [...j.logs, data.log] } : j
                ));
            }
        });

        /* ── job:done ── */
        es.addEventListener('job:done', (e) => {
            const data = JSON.parse(e.data);
            setMigrationJobs(prev => prev.map(j =>
                j.id === data.jobId ? {
                    ...j, status: 'done' as const, progress: 100,
                    duration: data.duration, completedAt: new Date().toISOString(),
                    streamedContent: data.migratedContent,
                } : j
            ));

            // Update file in files list using fileId directly from SSE to avoid stale closure
            setFiles(prev => prev.map(f => {
                if (f.id === data.fileId) {
                    return { ...f, status: 'completed' as const, migratedContent: data.migratedContent };
                }
                return f;
            }));

            setMigrationSession(prev => {
                if (!prev) return prev;
                const newCompleted = prev.completedJobs + 1;
                const pct = Math.round(((newCompleted + prev.failedJobs) / Math.max(prev.totalJobs, 1)) * 100);
                setMigrationProgress(pct);
                return { ...prev, completedJobs: newCompleted };
            });
        });

        /* ── job:failed ── */
        es.addEventListener('job:failed', (e) => {
            const data = JSON.parse(e.data);
            setMigrationJobs(prev => prev.map(j =>
                j.id === data.jobId ? {
                    ...j, status: 'failed' as const, progress: 100,
                    error: data.error, duration: data.duration,
                    completedAt: new Date().toISOString(),
                } : j
            ));

            setMigrationSession(prev => prev ? {
                ...prev,
                failedJobs: prev.failedJobs + 1,
            } : prev);
        });

        /* ── session:complete ── */
        es.addEventListener('session:complete', (e) => {
            const data = JSON.parse(e.data);
            setIsMigrating(false);
            setCurrentMigratingFile(null);
            setMigrationProgress(100);
            setMigrationSession(prev => prev ? {
                ...prev, status: 'completed',
                completedJobs: data.completedJobs,
                failedJobs: data.failedJobs,
                currentJobId: null,
                completedAt: new Date().toISOString(),
            } : prev);
            refreshFiles(projectId, true); // force so migrated content updates
            refreshBatches(projectId, true); // refresh project-level batch records
            es.close();
            eventSourceRef.current = null;
        });

        /* ── session:stopped ── */
        es.addEventListener('session:stopped', () => {
            setIsMigrating(false);
            setCurrentMigratingFile(null);
            setMigrationSession(prev => prev ? { ...prev, status: 'stopped', currentJobId: null } : prev);
            refreshFiles(projectId, true); // force refresh to sync server state
            refreshBatches(projectId, true); // refresh batches for the stopped run
            es.close();
            eventSourceRef.current = null;
        });

        /* ── Error handling ── */
        es.onerror = () => {
            setIsMigrating(false);
            setCurrentMigratingFile(null);
            es.close();
            eventSourceRef.current = null;
        };
    }, [selectedProject, refreshFiles, refreshBatches]);

    const stopMigration = useCallback(() => {
        const projectId = selectedProject?.id;
        if (!projectId) return;

        // Close EventSource
        if (eventSourceRef.current) {
            eventSourceRef.current.close();
            eventSourceRef.current = null;
        }

        // Tell server to stop
        fetch(`/api/migration/stream?projectId=${projectId}&action=stop`).catch(() => { });

        setIsMigrating(false);
        setCurrentMigratingFile(null);
        setMigrationSession(prev => prev ? { ...prev, status: 'stopped', currentJobId: null } : prev);
        // Eagerly refresh files — session:stopped SSE event may not arrive since EventSource is already closed
        refreshFiles(projectId, true);
    }, [selectedProject, refreshFiles]);

    const retryFailed = useCallback(() => {
        const projectId = selectedProject?.id;
        if (!projectId) return;

        migrationApi.retry(projectId)
            .then(() => {
                refreshFiles(projectId, true);  // force after retry
                setMigrationJobs([]);
                setMigrationSession(null);
                migrationApi.getLogs(projectId).then(({ logs }) => setMigrationLogs(logs));
            })
            .catch(() => { });
    }, [selectedProject, refreshFiles]);

    const clearLogs = useCallback(() => {
        const projectId = selectedProject?.id;
        if (!projectId) return;
        migrationApi.clearLogs(projectId)
            .then(() => setMigrationLogs([]))
            .catch(() => { });
    }, [selectedProject]);

    // Cleanup on unmount
    useEffect(() => {
        return () => {
            if (eventSourceRef.current) {
                eventSourceRef.current.close();
            }
        };
    }, []);

    const toggleSidebar = useCallback(() => setSidebarCollapsed(prev => !prev), []);

    const refreshLLMSettings = useCallback(() => {
        llmSettingsApi.get()
            .then(({ settings }) => {
                setActiveLLMProvider(settings.activeProvider);
                setLlmSettings(settings);
                if (user) {
                    localStorage.setItem(`ms_settings_${user.id}`, JSON.stringify(settings));
                }
            })
            .catch(() => { });
    }, [user]);

    const updateActiveLLMProvider = useCallback(async (provider: LLMProviderType) => {
        setActiveLLMProvider(provider);
        const res = await withErrorHandling(llmSettingsApi.save({ activeProvider: provider }), 'Failed to update default provider');
        if (res) setLlmSettings(res.settings);
    }, [withErrorHandling]);

    return (
        <AppContext.Provider value={{
            organizations, selectedOrg, selectOrg: setSelectedOrg, addOrganization, refreshOrganizations,
            workspaces, selectedWorkspace, selectWorkspace: setSelectedWorkspace, addWorkspace, deleteWorkspace, refreshWorkspaces,
            projects, selectedProject, selectProject, addProject, updateProject, deleteProject, refreshProjects,
            migrationBatches, refreshBatches,
            files, selectedFile, selectFile: setSelectedFile, updateFileStatus, bulkUpdateFileStatus,
            updateFileContent, updateFileMigratedContent, syncFileMigrationResult, getFileById, getProjectFiles, refreshFiles,
            migrationLogs, isMigrating, migrationProgress, currentMigratingFile,
            migrationJobs, migrationSession,
            startMigration, stopMigration, retryFailed, clearLogs,
            activeLLMProvider, llmSettings, refreshLLMSettings, updateActiveLLMProvider,
            toasts, addToast, removeToast,
            globalLoading, sidebarCollapsed, toggleSidebar,
        }}>
            {children}
        </AppContext.Provider>
    );
}

export function useApp() {
    const ctx = useContext(AppContext);
    if (!ctx) throw new Error('useApp must be used within AppProvider');
    return ctx;
}
