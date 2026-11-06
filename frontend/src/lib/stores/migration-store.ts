import { create } from 'zustand';
import { createJSONStorage, persist } from 'zustand/middleware';
import type { MigrationConfig, MigrationJob, MigrationRecord, LLMSettings } from '../types';
import io, { type Socket } from 'socket.io-client';
import axios from 'axios';
import { Buffer } from 'buffer';

const b64dec = (value: string): string => {
    if (typeof value === 'string' && value.startsWith('b64:')) {
        try {
            return Buffer.from(value.slice(4), 'base64').toString('utf8');
        } catch {
            return value;
        }
    }
    return value;
};

interface ProjectTiming {
    projectStartedAt: string;
    projectCompletedAt: string | null;
}

interface ExecutionRunTiming {
    migrationId: string;
    projectId: string;
    executionStartedAt: string;
    executionCompletedAt: string | null;
}

interface SyncMigrationRecord extends Omit<MigrationRecord, 'content'> {
    content: string;
}

interface SyncFileResponse {
    id: string;
    name: string;
    path: string;
    status: 'pending' | 'in-progress' | 'completed' | 'failed';
    activeMigrationId?: string | null;
    migratedContent?: string | null;
    migrations?: SyncMigrationRecord[];
}

interface ActiveBatchResponse {
    id: string;
}

interface StartMigrationResponse {
    success: boolean;
    migrationId: string;
    jobs: Array<{
        id: string;
        fileId: string;
        fileName: string;
        filePath: string;
    }>;
}

interface ResumeMigrationResponse {
    success: boolean;
    jobs: Array<{
        id: string;
        fileId: string;
    }>;
}

interface RetryFileResponse {
    success: boolean;
    jobId: string;
}

interface ProjectFilesResponse {
    success: boolean;
    files: SyncFileResponse[];
}

interface ActiveBatchApiResponse {
    success: boolean;
    batch: ActiveBatchResponse | null;
}

interface MigrationState {
    jobs: Record<string, MigrationJob>;
    isMigrating: boolean;
    currentProjectId: string | null;
    projectTimings: Record<string, ProjectTiming>;
    executionRuns: Record<string, ExecutionRunTiming>;
    latestExecutionRunByProject: Record<string, string>;
    initSocket: (projectId: string) => void;
    markProjectLoaded: (projectId: string) => void;
    setProjectStartedAt: (projectId: string, startedAt: string) => void;
    resetProjectTiming: (projectId: string, startedAt: string) => void;
    markProjectCompleted: (projectId: string) => void;
    startExecutionRun: (projectId: string, migrationId: string) => void;
    completeExecutionRun: (projectId: string, migrationId?: string) => void;
    startBatchMigration: (
        projectId: string,
        fileIds: string[],
        config: MigrationConfig,
        migrationId?: string,
        userId?: string,
        llmSettings?: LLMSettings,
    ) => Promise<void>;
    stopMigration: (projectId: string, migrationId?: string) => Promise<void>;
    resumeMigration: (projectId: string, migrationId: string, userId?: string) => Promise<void>;
    syncJobs: (projectId: string) => Promise<void>;
    retryFile: (
        projectId: string,
        fileId: string,
        migrationId: string,
        config: MigrationConfig,
        userId?: string
    ) => Promise<void>;
    updateJob: (jobId: string, updates: Partial<MigrationJob>) => void;
    setJobs: (jobs: MigrationJob[]) => void;
}

function mapFileStatusToJobStatus(status: SyncFileResponse['status']): MigrationJob['status'] {
    switch (status) {
        case 'completed':
            return 'done';
        case 'failed':
            return 'failed';
        case 'in-progress':
            return 'running';
        default:
            return 'queued';
    }
}

function buildJobFromFile(
    file: SyncFileResponse,
    projectId: string,
    batchId: string
): MigrationJob {
    const jobId = `py-${batchId}-${file.id}`;
    return {
        id: jobId,
        projectId,
        fileId: file.id,
        batchId,
        fileName: file.name,
        filePath: file.path,
        status: mapFileStatusToJobStatus(file.status),
        progress:
            file.status === 'completed' ? 100 : file.status === 'in-progress' ? 50 : 0,
        logs: [],
        streamedContent: file.migratedContent ? b64dec(file.migratedContent) : '',
        tokens: 0,
        migrations: decodeMigrations(file.migrations),
    };
}

function decodeMigrations(records: SyncMigrationRecord[] | undefined): MigrationRecord[] | undefined {
    if (!records) return undefined;

    return records.map((record) => ({
        ...record,
        systemPrompt: record.systemPrompt ? b64dec(record.systemPrompt) : undefined,
        userPrompt: record.userPrompt ? b64dec(record.userPrompt) : undefined,
        rawResponse: record.rawResponse ? b64dec(record.rawResponse) : undefined,
        content: record.content ? b64dec(record.content) : '',
    }));
}

function mergeProjectJobs(
    projectId: string,
    incoming: Record<string, MigrationJob>,
    existingJobs: Record<string, MigrationJob>,
    preserveStatuses: MigrationJob['status'][] = ['queued', 'running'],
): Record<string, MigrationJob> {
    const merged = { ...incoming };
    Object.values(existingJobs).forEach((job) => {
        if (job.projectId !== projectId) return;
        if (!preserveStatuses.includes(job.status)) return;
        const current = merged[job.id];
        if (!current || preserveStatuses.includes(current.status)) {
            merged[job.id] = current ? { ...current, ...job } : job;
        }
    });
    return merged;
}

export const useMigrationStore = create<MigrationState>()(
    persist(
        (set, get) => {
            let socket: Socket | null = null;
            const apiBase =
                typeof window !== 'undefined'
                    ? window.location.origin
                    : (process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001');

            const syncMigrationRunningState = () => {
                const hasActiveJobs = Object.values(get().jobs).some(
                    (job) => job.status === 'queued' || job.status === 'running'
                );
                set({ isMigrating: hasActiveJobs });
            };

            const completeLatestRunForProject = (projectId: string) => {
                const latestRunId = get().latestExecutionRunByProject[projectId];
                if (!latestRunId) return;
                const existingRun = get().executionRuns[latestRunId];
                if (!existingRun || existingRun.executionCompletedAt) return;

                set((state) => ({
                    executionRuns: {
                        ...state.executionRuns,
                        [latestRunId]: {
                            ...existingRun,
                            executionCompletedAt: new Date().toISOString(),
                        },
                    },
                }));
            };

            return {
                jobs: {},
                isMigrating: false,
                currentProjectId: null,
                projectTimings: {},
                executionRuns: {},
                latestExecutionRunByProject: {},

                initSocket: (projectId) => {
                    if (socket && get().currentProjectId === projectId) return;
                    if (socket) {
                        socket.removeAllListeners();
                        socket.disconnect();
                    }

                    const socketUrl = process.env.NEXT_PUBLIC_SOCKET_URL || apiBase;
                    socket = io(socketUrl, {
                        transports: ['websocket', 'polling'],
                        reconnection: true,
                        reconnectionAttempts: 10,
                        timeout: 10000,
                    });

                    socket.on('connect', () => {
                        socket?.emit('join:project', projectId);
                    });

                    socket.on('job:progress', ({ jobId, progress }: { jobId: string; progress: number }) => {
                        get().updateJob(jobId, { status: 'running', progress });
                        syncMigrationRunningState();
                    });

                    socket.on('job:token', ({ jobId, token }: { jobId: string; token: string }) => {
                        const currentJob = get().jobs[jobId];
                        const newContent = (currentJob?.streamedContent || '') + token;
                        get().updateJob(jobId, {
                            status: 'running',
                            streamedContent: newContent,
                        });
                        syncMigrationRunningState();
                    });

                    socket.on(
                        'job:completed',
                        ({ jobId, fileId }: { jobId: string; fileId?: string; result: unknown }) => {
                            get().updateJob(jobId, {
                                status: 'done',
                                progress: 100,
                                completedAt: new Date().toISOString(),
                            });
                            syncMigrationRunningState();
                            const activeProjectId = get().currentProjectId;
                            if (activeProjectId) {
                                void get().syncJobs(activeProjectId);
                            }
                        }
                    );

                    socket.on('job:failed', ({ jobId }: { jobId: string; error: string }) => {
                        get().updateJob(jobId, { status: 'failed', progress: 100 });
                        syncMigrationRunningState();
                        const activeProjectId = get().currentProjectId;
                        if (activeProjectId) {
                            void get().syncJobs(activeProjectId);
                        }
                    });

                    socket.on(
                        'migration:batch-complete',
                        ({
                            projectId: completedProjectId,
                            migrationId,
                            status,
                        }: {
                            projectId: string;
                            migrationId?: string;
                            status?: 'completed' | 'partial' | 'failed' | 'stopped';
                        }) => {
                            if (get().currentProjectId === completedProjectId) {
                                set({ isMigrating: false });
                            }
                            get().completeExecutionRun(completedProjectId, migrationId);
                            if (status === 'completed') {
                                get().markProjectCompleted(completedProjectId);
                            }
                            void get().syncJobs(completedProjectId);
                        }
                    );

                    socket.on(
                        'migration:stopped',
                        ({ projectId: stoppedProjectId, migrationId }: { projectId: string; migrationId?: string }) => {
                            set({ isMigrating: false });
                            get().completeExecutionRun(stoppedProjectId, migrationId);
                        }
                    );

                    set({ currentProjectId: projectId });
                },

                markProjectLoaded: (projectId) => {
                    set((state) => {
                        if (state.projectTimings[projectId]?.projectStartedAt) {
                            return state;
                        }

                        return {
                            projectTimings: {
                                ...state.projectTimings,
                                [projectId]: {
                                    projectStartedAt: new Date().toISOString(),
                                    projectCompletedAt: null,
                                },
                            },
                        };
                    });
                },

                setProjectStartedAt: (projectId, startedAt) => {
                    set((state) => {
                        const existing = state.projectTimings[projectId];
                        if (existing && new Date(existing.projectStartedAt).getTime() <= new Date(startedAt).getTime()) {
                            return state;
                        }

                        return {
                            projectTimings: {
                                ...state.projectTimings,
                                [projectId]: {
                                    projectStartedAt: startedAt,
                                    projectCompletedAt: existing?.projectCompletedAt ?? null,
                                },
                            },
                        };
                    });
                },

                resetProjectTiming: (projectId, startedAt) => {
                    set((state) => ({
                        projectTimings: {
                            ...state.projectTimings,
                            [projectId]: {
                                projectStartedAt: startedAt,
                                projectCompletedAt: null,
                            },
                        },
                    }));
                },

                markProjectCompleted: (projectId) => {
                    get().markProjectLoaded(projectId);
                    set((state) => {
                        const existing = state.projectTimings[projectId];
                        if (!existing || existing.projectCompletedAt) {
                            return state;
                        }

                        return {
                            projectTimings: {
                                ...state.projectTimings,
                                [projectId]: {
                                    ...existing,
                                    projectCompletedAt: new Date().toISOString(),
                                },
                            },
                        };
                    });
                },

                startExecutionRun: (projectId, migrationId) => {
                    get().markProjectLoaded(projectId);
                    const now = new Date().toISOString();
                    set((state) => ({
                        executionRuns: {
                            ...state.executionRuns,
                            [migrationId]: {
                                migrationId,
                                projectId,
                                executionStartedAt: now,
                                executionCompletedAt: null,
                            },
                        },
                        latestExecutionRunByProject: {
                            ...state.latestExecutionRunByProject,
                            [projectId]: migrationId,
                        },
                    }));
                },

                completeExecutionRun: (projectId, migrationId) => {
                    const resolvedMigrationId = migrationId || get().latestExecutionRunByProject[projectId];
                    if (!resolvedMigrationId) return;

                    const existingRun = get().executionRuns[resolvedMigrationId];
                    if (!existingRun || existingRun.executionCompletedAt) return;

                    set((state) => ({
                        executionRuns: {
                            ...state.executionRuns,
                            [resolvedMigrationId]: {
                                ...existingRun,
                                executionCompletedAt: new Date().toISOString(),
                            },
                        },
                    }));
                },

                startBatchMigration: async (projectId, fileIds, config, migrationId, userId, llmSettings) => {
                    set({ isMigrating: true, currentProjectId: projectId });
                    get().markProjectLoaded(projectId);
                    if (migrationId) {
                        get().startExecutionRun(projectId, migrationId);
                    }

                    try {
                        const response = await axios.post<StartMigrationResponse>(
                            `${apiBase}/api/projects/${projectId}/migrate`,
                            {
                                fileIds,
                                config,
                                migrationId,
                                userId,
                                llmSettings,
                            }
                        );

                        const data = response.data;
                        if (data.success) {
                            const effectiveMigrationId = data.migrationId || migrationId;
                            if (effectiveMigrationId) {
                                get().startExecutionRun(projectId, effectiveMigrationId);
                            }

                            const newJobs: Record<string, MigrationJob> = { ...get().jobs };
                            data.jobs.forEach((job) => {
                                newJobs[job.id] = {
                                    id: job.id,
                                    projectId,
                                    fileId: job.fileId,
                                    batchId: effectiveMigrationId,
                                    fileName: job.fileName,
                                    filePath: job.filePath,
                                    status: 'queued',
                                    progress: 0,
                                    logs: [],
                                    streamedContent: '',
                                    tokens: 0,
                                };
                            });
                            set({ jobs: newJobs });
                            syncMigrationRunningState();
                            // Delay first sync so the running batch row exists before we poll.
                            window.setTimeout(() => {
                                void get().syncJobs(projectId);
                            }, 1500);
                        }
                    } catch (error: unknown) {
                        if (axios.isAxiosError(error) && error.response?.status === 409) {
                            set({ isMigrating: false });
                            throw new Error(error.response.data.message || 'CONCURRENCY_LOCK');
                        }
                        set({ isMigrating: false });
                        throw error;
                    }
                },

                stopMigration: async (projectId, migrationId) => {
                    try {
                        await axios.post(`${apiBase}/api/projects/${projectId}/stop`, { migrationId });
                        if (!migrationId) {
                            set({ isMigrating: false });
                        }
                    } catch (error) {
                        console.error('Failed to stop migration:', error);
                    }
                },

                resumeMigration: async (projectId, migrationId, userId) => {
                    get().markProjectLoaded(projectId);
                    get().startExecutionRun(projectId, migrationId);

                    try {
                        const response = await axios.post<ResumeMigrationResponse>(
                            `${apiBase}/api/projects/${projectId}/resume`,
                            {
                                migrationId,
                                userId,
                            }
                        );

                        if (response.data.success) {
                            await get().syncJobs(projectId);
                            set({ isMigrating: true, currentProjectId: projectId });
                        }
                    } catch (error) {
                        console.error('Failed to resume migration:', error);
                    }
                },

                syncJobs: async (projectId) => {
                    try {
                        const fetchAllProjectFiles = async (): Promise<SyncFileResponse[]> => {
                            const allFiles: SyncFileResponse[] = [];
                            let page = 0;
                            const take = 100;
                            while (true) {
                                const res = await axios.get<ProjectFilesResponse>(
                                    `${apiBase}/api/projects/${projectId}/files?page=${page}&take=${take}`
                                );
                                if (!res.data.success || !res.data.files || res.data.files.length === 0) {
                                    break;
                                }
                                allFiles.push(...res.data.files);
                                if (res.data.files.length < take) {
                                    break;
                                }
                                page += 1;
                            }
                            return allFiles;
                        };

                        const [allFiles, activeBatchRes] = await Promise.all([
                            fetchAllProjectFiles(),
                            axios.get<ActiveBatchApiResponse>(`${apiBase}/api/projects/${projectId}/active-batch`),
                        ]);

                        const existingJobs = get().jobs;

                        if (activeBatchRes.data.success && activeBatchRes.data.batch) {
                            const activeBatchId = activeBatchRes.data.batch.id;
                            const jobsMap: Record<string, MigrationJob> = {};

                            allFiles.forEach((file) => {
                                if (file.activeMigrationId === activeBatchId) {
                                        jobsMap[`py-${activeBatchId}-${file.id}`] = buildJobFromFile(
                                            file,
                                            projectId,
                                            activeBatchId
                                        );
                                    }
                                });

                            const mergedJobs = mergeProjectJobs(projectId, jobsMap, existingJobs);
                            set({
                                jobs: mergedJobs,
                                currentProjectId: projectId,
                            });
                            syncMigrationRunningState();
                        } else {
                            const jobsMap: Record<string, MigrationJob> = {};

                            allFiles.forEach((file) => {
                                if (file.activeMigrationId && file.status !== 'pending') {
                                    jobsMap[`py-${file.activeMigrationId}-${file.id}`] = buildJobFromFile(
                                        file,
                                        projectId,
                                        file.activeMigrationId
                                    );
                                }
                            });

                            const mergedJobs = mergeProjectJobs(projectId, jobsMap, existingJobs);
                            const hasActiveJobs = Object.values(mergedJobs).some(
                                (job) => job.projectId === projectId && (job.status === 'queued' || job.status === 'running')
                            );

                            set({
                                jobs: hasActiveJobs ? mergedJobs : jobsMap,
                                isMigrating: hasActiveJobs,
                                currentProjectId: projectId,
                            });

                            if (!hasActiveJobs) {
                                completeLatestRunForProject(projectId);

                                if (
                                    allFiles.length > 0 &&
                                    allFiles.every((file: SyncFileResponse) => file.status === 'completed')
                                ) {
                                    get().markProjectCompleted(projectId);
                                }
                            }
                        }
                    } catch (error) {
                        console.error('Failed to sync jobs:', error);
                    }
                },

                retryFile: async (projectId, fileId, migrationId, config, userId) => {
                    try {
                        const response = await axios.post<RetryFileResponse>(
                            `${apiBase}/api/projects/${projectId}/retry-file`,
                            {
                                fileId,
                                migrationId,
                                config,
                                userId,
                            }
                        );

                        if (response.data.success) {
                            const jobId = response.data.jobId;
                            get().updateJob(jobId, {
                                id: jobId,
                                projectId,
                                fileId,
                                batchId: migrationId,
                                fileName: get().jobs[jobId]?.fileName || '',
                                filePath: get().jobs[jobId]?.filePath || '',
                                status: 'queued',
                                progress: 0,
                                streamedContent: '',
                                logs: [],
                                tokens: 0,
                            });
                        }
                    } catch (error: unknown) {
                        if (axios.isAxiosError(error) && error.response?.status === 409) {
                            throw new Error(error.response.data.message || 'A migration is already in progress.');
                        }
                        console.error('Failed to retry file migration:', error);
                        throw error;
                    }
                },

                updateJob: (jobId, updates) => {
                    set((state) => ({
                        jobs: {
                            ...state.jobs,
                            [jobId]: { ...state.jobs[jobId], ...updates },
                        },
                    }));
                },

                setJobs: (jobs) => {
                    const jobsMap: Record<string, MigrationJob> = {};
                    jobs.forEach((job) => {
                        jobsMap[job.id] = job;
                    });
                    set({ jobs: jobsMap });
                },
            };
        },
        {
            name: 'migration-store',
            storage: createJSONStorage(() => localStorage),
            partialize: (state) => ({
                currentProjectId: state.currentProjectId,
                projectTimings: state.projectTimings,
                executionRuns: state.executionRuns,
                latestExecutionRunByProject: state.latestExecutionRunByProject,
            }),
        }
    )
);
