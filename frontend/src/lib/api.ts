/**
 * API Client Service Layer
 * Centralized fetch wrapper with typed methods for all backend endpoints.
 */

import axios from 'axios';
import type {
    User, Organization, Workspace, Project, ProjectFile,
    MigrationLog, MigrationType, TargetRuntime, SourceType, Environment,
    LLMSettings, MigrationBatch, IRSummary, StructuredFlow, AnalysisValidation, AnalysisJobView,
    MigrationWorkflow, MappingReviewPayload, ArchitectureReviewPayload,
} from './types';

axios.defaults.withCredentials = true;

/* ─── Helpers ─── */
async function request<T>(url: string, options?: { method?: string; body?: string; headers?: Record<string, string>; signal?: AbortSignal } & Record<string, unknown>): Promise<T> {
    const method = options?.method || 'GET';
    try {
        const response = await axios({
            url,
            method,
            data: options?.body ? JSON.parse(options.body) : undefined,
            headers: options?.headers,
            ...options,
        });

        return response.data as T;
    } catch (err: unknown) {
        if (axios.isAxiosError(err)) {
            const status = err.response?.status;
            const data = err.response?.data as { error?: string; message?: string; requestId?: string } | undefined;
            const requestId = err.response?.headers?.['x-request-id'] || data?.requestId;
            const message = data?.error || data?.message || err.message || 'Request failed';
            const statusLabel = typeof status === 'number' ? String(status) : 'network-error';
            const detailParts = [
                `${method.toUpperCase()} ${url}`,
                `status ${statusLabel}`,
                message,
                requestId ? `request ${requestId}` : null,
            ].filter(Boolean);
            const error = new Error(detailParts.join(' | ')) as Error & { status?: number; data?: unknown; requestId?: string; endpoint?: string };
            error.status = status;
            error.data = data;
            error.requestId = requestId;
            error.endpoint = url;
            throw error;
        }
        if (err instanceof Error) {
            throw new Error(`${method.toUpperCase()} ${url} | network-error | ${err.message || 'Network error occurred. Please check your connection.'}`);
        }
        throw new Error(`${method.toUpperCase()} ${url} | network-error | An unknown error occurred`);
    }
}

function post<T>(url: string, body: unknown): Promise<T> {
    return request<T>(url, { method: 'POST', body: JSON.stringify(body) });
}

function put<T>(url: string, body: unknown): Promise<T> {
    return request<T>(url, { method: 'PUT', body: JSON.stringify(body) });
}

function del<T>(url: string): Promise<T> {
    return request<T>(url, { method: 'DELETE' });
}

/* ══════════════════════════════════════════════
   Auth API
   ══════════════════════════════════════════════ */
export const authApi = {
    async login(email: string, password: string): Promise<{ user: User }> {
        return post('/api/auth/login', { email, password });
    },

    async register(name: string, email: string, password: string): Promise<{ user: User }> {
        return post('/api/auth/register', { name, email, password });
    },

    async logout(): Promise<{ success: boolean }> {
        return post('/api/auth/logout', {});
    },

    async me(): Promise<{ user: User | null }> {
        try {
            return await request('/api/auth/me');
        } catch {
            return { user: null };
        }
    },

    async updateProfile(updates: Partial<User>): Promise<{ user: User }> {
        return put('/api/auth/me', updates);
    },

    async updatePassword(currentPassword: string, newPassword: string): Promise<{ success: boolean }> {
        return put('/api/auth/me/password', { currentPassword, newPassword });
    },
};

/* ══════════════════════════════════════════════
   Organizations API
   ══════════════════════════════════════════════ */
export const orgApi = {
    async list(): Promise<{ organizations: Organization[] }> {
        return request('/api/organizations');
    },

    async create(data: { name: string; description: string; owner: string; logo: string }): Promise<{ organization: Organization }> {
        return post('/api/organizations', data);
    },

    async get(orgId: string): Promise<{ organization: Organization }> {
        return request(`/api/organizations/${orgId}`);
    },
};

/* ══════════════════════════════════════════════
   Workspaces API
   ══════════════════════════════════════════════ */
export const workspaceApi = {
    async list(orgId: string): Promise<{ workspaces: Workspace[] }> {
        return request(`/api/workspaces?orgId=${orgId}`);
    },

    async create(data: { orgId: string; name: string; environment: Environment; memberCount: number }): Promise<{ workspace: Workspace }> {
        return post('/api/workspaces', data);
    },

    async get(wsId: string): Promise<{ workspace: Workspace }> {
        return request(`/api/workspaces/${wsId}`);
    },
};

/* ══════════════════════════════════════════════
   Projects API
   ══════════════════════════════════════════════ */
export const projectApi = {
    async list(workspaceId?: string, options?: { page?: number; take?: number; withStats?: boolean }): Promise<{ projects: Project[] }> {
        const page = options?.page ?? 0;
        const take = options?.take ?? 50;
        const withStats = options?.withStats ? '&withStats=true' : '';
        const query = workspaceId
            ? `?workspaceId=${workspaceId}&page=${page}&take=${take}${withStats}`
            : `?page=${page}&take=${take}${withStats}`;
        return request(`/api/projects${query}`);
    },

    async get(projectId: string): Promise<{ project: Project }> {
        return request(`/api/projects/${projectId}`);
    },

    async create(data: {
        workspaceId: string; orgId: string; name: string; description: string;
        migrationType: MigrationType; targetRuntime: TargetRuntime; sourceType: SourceType;
    }): Promise<{ project: Project }> {
        return post('/api/projects', data);
    },

    async update(projectId: string, updates: Partial<Project>): Promise<{ project: Project }> {
        return put(`/api/projects/${projectId}`, updates);
    },
};

/* ══════════════════════════════════════════════
   Files API
   ══════════════════════════════════════════════ */
export const fileApi = {
    async list(projectId: string, options?: { page?: number; take?: number; includeContent?: boolean; includeMigrations?: boolean }): Promise<{ files: ProjectFile[] }> {
        const page = options?.page ?? 0;
        const take = options?.take ?? 50;
        const includeContent = options?.includeContent ? '&includeContent=true' : '';
        const includeMigrations = options?.includeMigrations ? '&includeMigrations=true' : '';
        return request(`/api/files?projectId=${projectId}&page=${page}&take=${take}${includeContent}${includeMigrations}`);
    },

    async get(fileId: string): Promise<{ file: ProjectFile }> {
        return request(`/api/files/${fileId}`);
    },

    async update(fileId: string, updates: Partial<ProjectFile>): Promise<{ file: ProjectFile }> {
        return put(`/api/files/${fileId}`, updates);
    },
};

/* ══════════════════════════════════════════════
   Migration API
   ══════════════════════════════════════════════ */
export interface MigrationStatus {
    isRunning: boolean;
    currentFile: string | null;
    progress: number;
    totalFiles: number;
    processedFiles: number;
    fileStats: {
        total: number;
        completed: number;
        failed: number;
        pending: number;
        inProgress: number;
    };
    files: ProjectFile[];
}

export const migrationApi = {
    async start(projectId: string): Promise<{ session: unknown }> {
        return post('/api/migration/start', { projectId });
    },

    async stop(projectId: string): Promise<{ success: boolean }> {
        return post('/api/migration/stop', { projectId });
    },

    async status(projectId: string): Promise<MigrationStatus> {
        return request(`/api/migration/status?projectId=${projectId}`);
    },

    async migrateFile(fileId: string): Promise<{ status: string; migratedContent: string; log: MigrationLog }> {
        return post('/api/migration/file', { fileId });
    },

    async retry(projectId: string): Promise<{ retriedCount: number }> {
        return post('/api/migration/retry', { projectId });
    },

    async getLogs(projectId: string): Promise<{ logs: MigrationLog[] }> {
        return request(`/api/migration/logs?projectId=${projectId}`);
    },

    async clearLogs(projectId: string): Promise<{ success: boolean }> {
        return del(`/api/migration/logs?projectId=${projectId}`);
    },

    async getBatches(projectId: string, options?: { page?: number; take?: number }): Promise<{ batches: MigrationBatch[] }> {
        const page = options?.page ?? 0;
        const take = options?.take ?? 50;
        return request(`/api/migration/batches?projectId=${projectId}&page=${page}&take=${take}`);
    },
};

export const workflowApi = {
    async get(projectId: string): Promise<{ projectId: string; workflow: MigrationWorkflow }> {
        return request(`/api/workflow?projectId=${projectId}`);
    },

    async approve(projectId: string, stage: 'ir' | 'mapping' | 'architecture', payload?: { userId?: string; notes?: string; approvedVersion?: string }): Promise<{ projectId: string; workflow: MigrationWorkflow }> {
        return post('/api/workflow/approve', { projectId, stage, ...(payload || {}) });
    },

    async reject(projectId: string, stage: 'ir' | 'mapping' | 'architecture', payload?: { userId?: string; notes?: string }): Promise<{ projectId: string; workflow: MigrationWorkflow }> {
        return post('/api/workflow/reject', { projectId, stage, ...(payload || {}) });
    },

    async requestReanalysis(projectId: string, payload?: { userId?: string; notes?: string }): Promise<{ projectId: string; workflow: MigrationWorkflow }> {
        return post('/api/workflow/request-reanalysis', { projectId, ...(payload || {}) });
    },

    async generateMapping(projectId: string, targetRuntime: string): Promise<{ projectId: string; workflow: MigrationWorkflow; mappingReview: MappingReviewPayload }> {
        return post('/api/workflow/generate-mapping', { projectId, targetRuntime });
    },

    async generateArchitecture(projectId: string, targetRuntime: string): Promise<{ projectId: string; workflow: MigrationWorkflow; architectureReview: ArchitectureReviewPayload }> {
        return post('/api/workflow/generate-architecture', { projectId, targetRuntime });
    },
};

/* ══════════════════════════════════════════════
   Import API
   ══════════════════════════════════════════════ */
export const importApi = {
    async gitTest(params: { repoUrl: string; branch?: string; token?: string }): Promise<{
        name: string; description: string; isPrivate: boolean;
        stars?: number; defaultBranch: string; filesFound: number;
    }> {
        const qs = new URLSearchParams({ repoUrl: params.repoUrl });
        if (params.branch) qs.set('branch', params.branch);
        if (params.token) qs.set('token', params.token);

        try {
            const res = await axios.get(`/api/import/git?${qs}`);
            return res.data;
        } catch (err: unknown) {
            const data = axios.isAxiosError(err) ? err.response?.data : null;
            throw new Error((data as { error?: string })?.error || 'Connection test failed');
        }
    },

    /** Import files — POST /api/import/git */
    async git(data: { repoUrl: string; projectId: string; branch?: string; provider?: string; token?: string; subPath?: string }): Promise<{ success: boolean; message: string; filesImported: number; repoName: string; importStartedAt: string }> {
        return post('/api/import/git', data);
    },

    async zip(file: File, projectId: string): Promise<{ success: boolean; message: string; filesExtracted: number; importStartedAt: string }> {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('projectId', projectId);

        try {
            const res = await axios.post('/api/import/zip', formData);
            return res.data;
        } catch (err: unknown) {
            const data = axios.isAxiosError(err) ? err.response?.data : null;
            throw new Error((data as { error?: string })?.error || 'ZIP import failed');
        }
    },
};

export const analysisApi = {
    async start(projectId: string, payload: {
        sourceRef?: string;
        sourcePath?: string;
        migrationType?: MigrationType;
        targetRuntime?: TargetRuntime;
        requestedBy?: string;
        fileManifest?: Array<{ path: string; name: string; language?: string }>;
    }): Promise<AnalysisJobView> {
        return post('/api/analysis/start', { projectId, ...payload });
    },

    async latest(projectId: string, includeRaw = false, signal?: AbortSignal): Promise<AnalysisJobView> {
        return request(`/api/analysis/latest?projectId=${projectId}${includeRaw ? '&includeRaw=true' : ''}`, { signal });
    },

    async summary(projectId: string): Promise<{ jobId: string; projectId: string; summary: IRSummary }> {
        return request(`/api/analysis/summary?projectId=${projectId}`);
    },

    async flows(projectId: string): Promise<{ jobId: string; projectId: string; structuredFlows: StructuredFlow[] }> {
        return request(`/api/analysis/flows?projectId=${projectId}`);
    },

    async validation(projectId: string): Promise<{ jobId: string; projectId: string; validation: AnalysisValidation }> {
        return request(`/api/analysis/validation?projectId=${projectId}`);
    },

    async raw(projectId: string, jobId?: string, signal?: AbortSignal): Promise<{ jobId: string; projectId: string; rawIr: Record<string, unknown> }> {
        const qs = jobId ? `&jobId=${jobId}` : '';
        return request(`/api/analysis/raw?projectId=${projectId}${qs}`, { signal });
    },

    async events(projectId: string, since = 0): Promise<{ projectId: string; latestSeq: number; events: Array<Record<string, unknown>> }> {
        return request(`/api/analysis/events?projectId=${projectId}&since=${since}`);
    },
};

export const executionMigrationApi = {
    async start(projectId: string, payload: {
        analysisJobId?: string;
        confirmationToken?: string;
        migrationType?: MigrationType;
        targetRuntime?: TargetRuntime;
        requestedBy?: string;
    }): Promise<AnalysisJobView> {
        return post('/api/migrations/start', { projectId, ...payload });
    },
    async latest(projectId: string): Promise<AnalysisJobView> {
        return request(`/api/migrations/latest?projectId=${projectId}`);
    },
};

/* ══════════════════════════════════════════════
   Export API
   ══════════════════════════════════════════════ */
export const exportApi = {
    async download(projectId: string, format: string): Promise<{ success: boolean; message: string; downloadUrl: string }> {
        return post('/api/export/download', { projectId, format });
    },

    async push(data: { projectId: string; target: string; repoUrl?: string; branch?: string }): Promise<{ success: boolean; message: string }> {
        return post('/api/export/push', data);
    },
};

/* ══════════════════════════════════════════════
   LLM Settings API
   ══════════════════════════════════════════════ */
export const llmSettingsApi = {
    async get(): Promise<{ settings: LLMSettings }> {
        return request('/api/settings/llm');
    },

    async getUnmasked(): Promise<{ settings: LLMSettings }> {
        return request('/api/settings/llm?reveal=true');
    },

    async save(settings: Partial<LLMSettings>): Promise<{ settings: LLMSettings; saved: boolean }> {
        return put('/api/settings/llm', { settings });
    },

    async testConnection(data: { provider: string; apiKey?: string; model?: string }): Promise<{ success: boolean; message: string }> {
        return post('/api/settings/llm/test', data);
    },
};
