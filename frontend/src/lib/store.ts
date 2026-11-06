/**
 * Server-Side In-Memory Data Store
 * Initialized from mockData — provides typed CRUD operations.
 * Includes job-based migration engine with SSE streaming support.
 */

import {
    Organization, Workspace, Project, ProjectFile,
    MigrationLog, User, FileStatus, MigrationLogLevel,
    MigrationJob, MigrationSessionState, SSEEventType,
    LLMSettings, LLMProviderType, ProjectStatus, MigrationBatch,
    MigrationRecord
} from './types';
import {
    mockOrganizations, mockWorkspaces, mockProjects,
    mockFiles, mockUser, mockMigrationBatches,
} from './mockData';
import type { MigrationConfig } from './llm-provider';
import {
    dbFileStore, dbLogStore, dbBatchStore, dbProjectStore,
} from './db-store';
import { prisma } from './prisma';

/* ─── User type with password ─── */
interface StoredUser extends User {
    password: string;
}

const g = globalThis as any;

const migrationSessionsMap: Map<string, MigrationSessionState> = g.__ms_migrationSessionsMap || (g.__ms_migrationSessionsMap = new Map());
/* ─── In-memory collections (bound to globalThis for Next.js API route sharing) ─── */
if (!g.__ms_users) {
    // Initialize users
    g.__ms_users = [
        { ...mockUser, password: 'password123' },
    ];

    // Clean up any stale migration sessions left from previous runs
    // This ensures that workspace load does not see phantom active migrations.
    // Iterate over any existing sessions and mark them as stopped, update related files.
    const cleanupStaleMigrations = async () => {
        // For each stored session, mark jobs as failed and clear activeMigrationId on files.
        for (const [projectId, session] of migrationSessionsMap.entries()) {
            // Mark session as stopped
            session.status = 'stopped';
            // Update each job status if still queued or running
            session.jobs.forEach(job => {
                if (job.status === 'queued' || job.status === 'running') {
                    job.status = 'failed';
                }
            });
            // Clear activeMigrationId on files belonging to this project
            const projectFiles = getFiles().filter(f => f.projectId === projectId);
            projectFiles.forEach(f => {
                if (f.activeMigrationId) {
                    f.activeMigrationId = undefined;
                }
                // Reset any in‑progress status to pending so UI shows correct counts
                if (f.status === 'in-progress') {
                    f.status = 'pending';
                }
            });
            // Remove session from map
            migrationSessionsMap.delete(projectId);
        }
    };
    // Run cleanup immediately (fire‑and‑forget). Errors are logged but do not block startup.
    cleanupStaleMigrations().catch(err => console.error('Failed cleanup of stale migrations:', err));
    } 
// Initialize other global stores if not present
if (!g.__ms_organizations) g.__ms_organizations = [...mockOrganizations];
if (!g.__ms_workspaces) g.__ms_workspaces = [...mockWorkspaces];
if (!g.__ms_projects) g.__ms_projects = [...mockProjects];
if (!g.__ms_files) g.__ms_files = [...mockFiles];
if (!g.__ms_migrationLogs) g.__ms_migrationLogs = [];

// Lazy-init fields that may be missing on a warm server after a hot-reload or incremental deploy
if (!g.__ms_migration_batches) g.__ms_migration_batches = [...mockMigrationBatches];
if (!g.__ms_user_active_migration) g.__ms_user_active_migration = new Map<string, string>();
// FIX P0-2A: these maps were never initialized, causing llmSettingsMap.set() to throw → PUT /api/settings/llm 500
if (!g.__ms_llmSettingsMap) g.__ms_llmSettingsMap = new Map<string, LLMSettings>();
if (!g.__ms_sessionTokens) g.__ms_sessionTokens = new Map<string, string>();

// Direct access to global collections to ensure consistency across API route executions
const getUsers = (): StoredUser[] => g.__ms_users;
const getOrgs = (): Organization[] => g.__ms_organizations;
const getWorkspaces = (): Workspace[] => g.__ms_workspaces;
const getProjects = (): Project[] => g.__ms_projects;
const getFiles = (): ProjectFile[] => g.__ms_files;
const getLogs = (): MigrationLog[] => g.__ms_migrationLogs;

// FIX P0-2B: __ms_user_active_migration was initialized on globalThis but never bound to a local const,
// so every call to userMigrationGuard.claim/release crashed with "Cannot read properties of undefined".
const __ms_user_active_migration: Map<string, string> = g.__ms_user_active_migration;

// const migrationSessionsMap: Map<string, MigrationSessionState> = g.__ms_migrationSessionsMap; // moved earlier
const llmSettingsMap: Map<string, LLMSettings> = g.__ms_llmSettingsMap;
const sessionTokens: Map<string, string> = g.__ms_sessionTokens;

// Sync project stats from actual file data once on cold-boot
if (!g.__ms_stats_synced) {
    g.__ms_stats_synced = true;
    getProjects().forEach((p: Project) => syncProjectStats(p.id));
}

/* ══════════════════════════════════════════════
   Users
   ══════════════════════════════════════════════ */
export const userStore = {
    findByEmail(email: string): StoredUser | undefined {
        return getUsers().find(u => u.email.toLowerCase() === email.toLowerCase());
    },

    findById(id: string): StoredUser | undefined {
        return getUsers().find(u => u.id === id);
    },

    create(name: string, email: string, password: string): User {
        const newUser: StoredUser = {
            id: `user-${Date.now()}`,
            name,
            email,
            password,
            role: 'developer',
            avatar: '',
        };
        getUsers().push(newUser);
        const { password: _, ...safe } = newUser;
        return safe;
    },

    updateProfile(id: string, updates: Partial<User>): User | null {
        const uItems = getUsers();
        const idx = uItems.findIndex(u => u.id === id);
        if (idx === -1) return null;
        uItems[idx] = { ...uItems[idx], ...updates };
        const { password: _, ...safe } = uItems[idx];
        return safe;
    },

    updatePassword(id: string, currentPwd: string, newPwd: string): boolean {
        const uItems = getUsers();
        const idx = uItems.findIndex(u => u.id === id);
        if (idx === -1 || uItems[idx].password !== currentPwd) return false;
        uItems[idx].password = newPwd;
        return true;
    },

    toSafe(user: StoredUser): User {
        const { password: _, ...safe } = user;
        return safe;
    },
};

/* ══════════════════════════════════════════════
   Organizations
   ══════════════════════════════════════════════ */
export const orgStore = {
    list(): Organization[] {
        return getOrgs();
    },

    findById(id: string): Organization | undefined {
        return getOrgs().find(o => o.id === id);
    },

    create(org: Omit<Organization, 'id' | 'createdAt' | 'workspaceCount'>): Organization {
        const newOrg: Organization = {
            ...org,
            id: `org-${Date.now()}`,
            createdAt: new Date().toISOString().split('T')[0],
            workspaceCount: 0,
        };
        getOrgs().push(newOrg);
        return newOrg;
    },
};

/* ══════════════════════════════════════════════
   Workspaces
   ══════════════════════════════════════════════ */
export const workspaceStore = {
    listByOrg(orgId: string): Workspace[] {
        return getWorkspaces().filter(w => w.orgId === orgId);
    },

    findById(id: string): Workspace | undefined {
        return getWorkspaces().find(w => w.id === id);
    },

    create(ws: Omit<Workspace, 'id' | 'projectCount'>): Workspace {
        const newWs: Workspace = {
            ...ws,
            id: `ws-${Date.now()}`,
            projectCount: 0,
        };
        getWorkspaces().push(newWs);
        // Increment workspaceCount in the org
        const org = getOrgs().find(o => o.id === ws.orgId);
        if (org) org.workspaceCount++;
        return newWs;
    },
    // Delete a workspace only if it has no projects
    delete(workspaceId: string): boolean {
        const wsList = getWorkspaces();
        const wsIdx = wsList.findIndex(w => w.id === workspaceId);
        if (wsIdx === -1) return false;

        const ws = wsList[wsIdx];
        const hasProjects = getProjects().some(p => p.workspaceId === workspaceId);
        if (hasProjects) return false;

        // Decrement workspaceCount in the org
        const org = getOrgs().find(o => o.id === ws.orgId);
        if (org) org.workspaceCount = Math.max(0, org.workspaceCount - 1);

        g.__ms_workspaces = getWorkspaces().filter(w => w.id !== workspaceId);
        return true;
    },
};

/* ══════════════════════════════════════════════
   Projects
   ══════════════════════════════════════════════ */
/* ══════════════════════════════════════════════
   Project Stats Sync
   Derives totalFiles, migratedFiles, failedFiles,
   migrationRuns and status from actual file data.
   ══════════════════════════════════════════════ */
export function syncProjectStats(projectId: string): void {
    const projectFiles = getFiles().filter(f => f.projectId === projectId && f.type === 'file');
    const totalFiles = projectFiles.length;
    const migratedFiles = projectFiles.filter(f => f.status === 'completed').length;
    const failedFiles = projectFiles.filter(f => f.status === 'failed').length;

    // Count unique batch runs across all file.migrations arrays
    const batchIds = new Set<string>();
    projectFiles.forEach(f => f.migrations?.forEach(m => batchIds.add(m.id)));
    const migrationRuns = batchIds.size;

    // Derive status from file states
    let status: ProjectStatus = 'pending';
    if (totalFiles > 0) {
        const inProgressCount = projectFiles.filter(f => f.status === 'in-progress').length;
        if (inProgressCount > 0) {
            status = 'in-progress';
        } else if (migratedFiles + failedFiles === totalFiles) {
            status = failedFiles > 0 ? 'failed' : 'completed';
        } else if (migratedFiles > 0 || failedFiles > 0) {
            status = 'in-progress';
        }
    }

    const projectList = getProjects();
    const idx = projectList.findIndex(p => p.id === projectId);
    if (idx !== -1) {
        projectList[idx] = {
            ...projectList[idx],
            totalFiles,
            migratedFiles,
            failedFiles,
            migrationRuns,
            status,
            lastActivity: new Date().toISOString().split('T')[0],
        };
    }
}

export const projectStore = {
    listByWorkspace(workspaceId: string): Project[] {
        return getProjects().filter(p => p.workspaceId === workspaceId);
    },

    list(): Project[] {
        return getProjects();
    },

    findById(id: string): Project | undefined {
        return getProjects().find(p => p.id === id);
    },

    create(p: Omit<Project, 'id' | 'createdAt' | 'lastActivity' | 'totalFiles' | 'migratedFiles' | 'failedFiles' | 'status' | 'migrationRuns'>): Project {
        const newProject: Project = {
            ...p,
            id: `proj-${Date.now()}`,
            createdAt: new Date().toISOString().split('T')[0],
            lastActivity: new Date().toISOString().split('T')[0],
            totalFiles: 0,
            migratedFiles: 0,
            failedFiles: 0,
            migrationRuns: 0,
            status: 'pending',
        };
        getProjects().push(newProject);
        // Increment projectCount in the workspace
        const ws = getWorkspaces().find(w => w.id === p.workspaceId);
        if (ws) ws.projectCount++;
        return newProject;
    },

    update(id: string, updates: Partial<Project>): Project | null {
        const projectList = getProjects();
        const idx = projectList.findIndex(p => p.id === id);
        if (idx === -1) return null;
        projectList[idx] = { ...projectList[idx], ...updates };
        return projectList[idx];
    },
    // Delete a project and its associated files and logs
    delete(projectId: string): boolean {
        const projectList = getProjects();
        const projIdx = projectList.findIndex(p => p.id === projectId);
        if (projIdx === -1) return false;
        // Remove associated files
        g.__ms_files = getFiles().filter(f => f.projectId !== projectId);

        // Remove associated logs
        g.__ms_migrationLogs = getLogs().filter(l => l.projectId !== projectId);

        // Remove the project itself
        const deletedProj = projectList[projIdx];
        projectList.splice(projIdx, 1);
        g.__ms_projects = projectList;

        // Decrement projectCount in the workspace
        const ws = getWorkspaces().find(w => w.id === deletedProj.workspaceId);
        if (ws) ws.projectCount = Math.max(0, ws.projectCount - 1);

        return true;
    },
};

/* ══════════════════════════════════════════════
   Files
   ══════════════════════════════════════════════ */
export const fileStore = {
    listByProject(projectId: string): ProjectFile[] {
        return getFiles().filter(f => f.projectId === projectId);
    },

    findById(id: string): ProjectFile | undefined {
        return getFiles().find(f => f.id === id);
    },

    deleteByProject(projectId: string): number {
        const currentFiles = getFiles();
        const before = currentFiles.length;
        const remaining = currentFiles.filter(f => f.projectId !== projectId);
        const removed = before - remaining.length;
        g.__ms_files = remaining;
        return removed;
    },

    bulkCreate(newFiles: ProjectFile[]): ProjectFile[] {
        getFiles().push(...newFiles);
        return newFiles;
    },

    updateStatus(id: string, status: FileStatus): ProjectFile | null {
        const fileList = getFiles();
        const idx = fileList.findIndex(f => f.id === id);
        if (idx === -1) return null;
        fileList[idx] = { ...fileList[idx], status };
        return fileList[idx];
    },

    updateContent(id: string, content: string): ProjectFile | null {
        const fileList = getFiles();
        const idx = fileList.findIndex(f => f.id === id);
        if (idx === -1) return null;
        fileList[idx] = { ...fileList[idx], content };
        return fileList[idx];
    },

    updateMigratedContent(id: string, migratedContent: string): ProjectFile | null {
        const fileList = getFiles();
        const idx = fileList.findIndex(f => f.id === id);
        if (idx === -1) return null;
        fileList[idx] = { ...fileList[idx], migratedContent };
        return fileList[idx];
    },

    update(id: string, updates: Partial<ProjectFile>): ProjectFile | null {
        const fileList = getFiles();
        const idx = fileList.findIndex(f => f.id === id);
        if (idx === -1) return null;

        const currentFile = fileList[idx];

        // Handle Migration History Appending
        if (updates.migratedContent && updates.activeMigrationId !== undefined) {
            const provider = updates.migratedContent.includes('provider:') ? updates.migratedContent.split('provider:')[1].split(';')[0] : 'claude';
            const model = updates.migratedContent.includes('model:') ? updates.migratedContent.split('model:')[1].split(';')[0] : 'unknown';

            // Clean arbitrary prepended metadata markers from standard generation loop
            let cleanContent = updates.migratedContent;
            if (cleanContent.startsWith('<!--metadata:')) {
                cleanContent = cleanContent.split('-->\n')[1] || cleanContent;
            }

            const record: MigrationRecord = {
                id: updates.activeMigrationId,
                provider: provider as LLMProviderType,
                model: model,
                content: cleanContent,
                code: updates.migratedCode || jobEngine.extractPrimaryCode(cleanContent),
                tokens: updates.tokens ?? 0,
                createdAt: new Date().toISOString(),
            };

            const existingMigrations = currentFile.migrations || [];
            fileList[idx] = {
                ...currentFile,
                ...updates,
                migratedContent: cleanContent,
                migratedCode: updates.migratedCode || record.code,
                migrations: [...existingMigrations, record],
            };
        } else {
            fileList[idx] = { ...currentFile, ...updates };
        }

        return fileList[idx];
    },
};

/* ══════════════════════════════════════════════
   Migration Logs
   ══════════════════════════════════════════════ */
export const logStore = {
    listByProject(projectId: string): MigrationLog[] {
        return getLogs().filter(l => l.projectId === projectId);
    },

    create(log: Omit<MigrationLog, 'id' | 'timestamp'>): MigrationLog {
        const newLog: MigrationLog = {
            ...log,
            id: `log-${Date.now()}-${Math.random().toString(36).substr(2, 5)}`,
            timestamp: new Date().toISOString(),
        };
        getLogs().unshift(newLog);
        return newLog;
    },

    clearByProject(projectId: string): void {
        g.__ms_migrationLogs = getLogs().filter(l => l.projectId !== projectId);
    },
};

/* ══════════════════════════════════════════════
   Migration Batch Store — project-level bundles
   One batch record per migration run; all files in
   a run share the same batch id (session.sessionId).
   ══════════════════════════════════════════════ */
const getBatches = (): MigrationBatch[] => g.__ms_migration_batches;

export const batchStore = {
    listByProject(projectId: string): MigrationBatch[] {
        return getBatches()
            .filter(b => b.projectId === projectId)
            .sort((a, b) => new Date(b.startedAt).getTime() - new Date(a.startedAt).getTime());
    },

    findById(id: string): MigrationBatch | undefined {
        return getBatches().find(b => b.id === id);
    },

    create(batch: MigrationBatch): MigrationBatch {
        // Replace if same id already exists (idempotent upsert)
        const existing = getBatches().findIndex(b => b.id === batch.id);
        if (existing !== -1) {
            getBatches()[existing] = batch;
            return batch;
        }
        getBatches().unshift(batch);
        return batch;
    },
};

/* ══════════════════════════════════════════════
   Per-User Migration Guard
   Ensures only one active migration per user.
   ══════════════════════════════════════════════ */
export const userMigrationGuard = {
    getActiveProject(userId: string): string | undefined {
        // Returns the projectId of the currently active migration for the user, if any.
        return __ms_user_active_migration.get(userId);
    },
    claim(userId: string, projectId: string): boolean {
        // Attempt to claim a migration for the user. If the user already has an active migration
        // (different projectId), the claim fails and returns false. Otherwise, store the claim and return true.
        const existing = __ms_user_active_migration.get(userId);
        if (existing && existing !== projectId) {
            return false; // another migration in progress for this user
        }
        __ms_user_active_migration.set(userId, projectId);
        return true;
    },
    release(userId: string): void {
        // Release any active migration claim for the user.
        __ms_user_active_migration.delete(userId);
    },
};

/* ══════════════════════════════════════════════
   SSE Helper — sends an event through a writer
   ══════════════════════════════════════════════ */
function sseEvent(encoder: TextEncoder, event: SSEEventType, data: unknown): Uint8Array {
    return encoder.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`);
}

/* ══════════════════════════════════════════════
   Job Engine — server-side job queue with SSE streaming
   ══════════════════════════════════════════════ */
export const jobEngine = {
    getSession(projectId: string): MigrationSessionState | undefined {
        return migrationSessionsMap.get(projectId);
    },

    async createSession(projectId: string, includeCompleted = false): Promise<MigrationSessionState> {
        const allFiles = await dbFileStore.listByProject(projectId);
        const migratableFiles = allFiles.filter(
            f => f.type === 'file' && (includeCompleted || f.status !== 'completed')
        );

        const jobs: MigrationJob[] = migratableFiles.map((file, idx) => ({
            id: `job-${projectId}-${idx}-${Date.now()}`,
            projectId,
            fileId: file.id,
            fileName: file.name,
            filePath: file.path,
            status: 'queued' as const,
            progress: 0,
            streamedContent: '',
            tokens: 0,
            logs: [],
        }));

        const session: MigrationSessionState = {
            projectId,
            sessionId: `mig-batch-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
            status: 'running',
            jobs,
            totalJobs: jobs.length,
            completedJobs: 0,
            failedJobs: 0,
            currentJobId: null,
            startedAt: new Date().toISOString(),
        };

        migrationSessionsMap.set(projectId, session);
        return session;
    },

    stopSession(projectId: string): void {
        const session = migrationSessionsMap.get(projectId);
        if (session) {
            session.status = 'stopped';
            session.currentJobId = null;
            session.jobs.forEach(j => {
                if (j.status === 'running') j.status = 'failed';
                if (j.status === 'queued') j.status = 'failed';
            });
        }
    },

    async retryFailed(projectId: string): Promise<number> {
        const allFiles = await dbFileStore.listByProject(projectId);
        const failedFiles = allFiles.filter(f => f.status === 'failed');
        await Promise.all(failedFiles.map(f => dbFileStore.updateStatus(f.id, 'pending')));

        await dbLogStore.create({
            projectId,
            fileName: 'Migration Engine',
            status: 'info',
            message: `Resetting ${failedFiles.length} failed files for retry`,
            duration: 0,
        });

        migrationSessionsMap.delete(projectId);
        return failedFiles.length;
    },

    /**
     * Extracts the primary code block from a Markdown report.
     * Looks for [PRIMARY_CODE_BLOCK] marker or the largest code block.
     */
    extractPrimaryCode(content: string): string {
        // First try the explicit marker
        const marker = '[PRIMARY_CODE_BLOCK]';
        const markerIndex = content.indexOf(marker);
        if (markerIndex !== -1) {
            const afterMarker = content.slice(markerIndex + marker.length);
            const codeBlockMatch = afterMarker.match(/```(?:\w+)?\n([\s\S]*?)```/);
            if (codeBlockMatch) return codeBlockMatch[1].trim();
        }

        // Fallback: extract all code blocks and pick the largest one (likely the handler)
        const codeBlocks = Array.from(content.matchAll(/```(?:\w+)?\n([\s\S]*?)```/g), m => m[1].trim());
        if (codeBlocks.length === 0) return '';

        return codeBlocks.reduce((a, b) => a.length > b.length ? a : b);
    },

    /**
     * Process all jobs via SSE streaming.
     * Called from SSE endpoint — writes events directly to the response stream.
     */
    async processJobsWithStream(
        projectId: string,
        writer: WritableStreamDefaultWriter<Uint8Array>,
        settings: any,
        triggeredBy: { userId: string; userName: string } = { userId: 'system', userName: 'System' },
        instructions?: string
    ): Promise<void> {
        const session = migrationSessionsMap.get(projectId);
        if (!session) return;

        const encoder = new TextEncoder();

        // ─── CRITICAL: Send session:start IMMEDIATELY from in-memory data ───
        // Do NOT await any DB calls before this. The browser needs to receive
        // these events instantly so the UI shows progress without a page refresh.
        const jobSummaries = session.jobs.map(j => ({
            id: j.id, fileId: j.fileId, fileName: j.fileName, filePath: j.filePath, status: j.status,
        }));
        await writer.write(sseEvent(encoder, 'session:start', {
            projectId, sessionId: session.sessionId, totalJobs: session.totalJobs, jobs: jobSummaries,
        }));

        // Send all jobs as queued immediately so the UI populates the list
        for (const job of session.jobs) {
            await writer.write(sseEvent(encoder, 'job:queued', {
                jobId: job.id, fileName: job.fileName, filePath: job.filePath,
            }));
        }

        // ─── NOW do the DB lookup for migration config (after UI is updated) ───
        const project = await dbProjectStore.findById(projectId);
        const migrationConfig: Partial<MigrationConfig> = {
            migrationType: project?.migrationType || 'mule4-lambda',
            targetRuntime: project?.targetRuntime || 'nodejs',
        };
        // Process jobs sequentially
        let sessionTotalTokens = 0;
        const batchFileResults: MigrationBatch['fileResults'] = [];
        for (let i = 0; i < session.jobs.length; i++) {
            if ((session as MigrationSessionState).status === 'stopped') break;

            const job = session.jobs[i];
            session.currentJobId = job.id;
            job.status = 'running';
            job.startedAt = new Date().toISOString();
            job.progress = 0;

            await dbFileStore.updateStatus(job.fileId, 'in-progress');

            await writer.write(sseEvent(encoder, 'job:start', {
                jobId: job.id, fileName: job.fileName, index: i, total: session.totalJobs,
            }));

            const startLog = await dbLogStore.create({
                projectId,
                fileName: job.fileName,
                status: 'info',
                message: `Processing ${job.fileName}... (${i + 1}/${session.totalJobs})`,
                duration: 0,
            });
            job.logs.push(startLog);
            await writer.write(sseEvent(encoder, 'job:log', { jobId: job.id, log: startLog }));

            const startTime = Date.now();

            try {
                const file = await dbFileStore.findById(job.fileId);
                if (!file) throw new Error(`File ${job.fileId} not found`);

                const config: MigrationConfig = {
                    ...(migrationConfig as MigrationConfig),
                    fileName: job.fileName,
                    filePath: job.filePath,
                    instructions,
                };

                let streamedContent = '';
                let tokenCount = 0;

                const fastApiUrl = (process.env.FASTAPI_URL || 'http://localhost:8000').replace(/\/$/, '');
                const activeProvider = settings?.activeProvider || 'nova';
                const providerConfig = settings?.providers?.[activeProvider] || {};

                const backendResponse = await fetch(`${fastApiUrl}/internal/migration/stream-file`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        // ── IR enrichment hook ────────────────────────────────
                        // Pass the projectId so the FastAPI endpoint can query
                        // the latest completed analysis IR and slice it for
                        // this file before invoking the LLM.
                        projectId: file.projectId,
                        fileName: job.fileName,
                        filePath: job.filePath,
                        sourceContent: file.content,
                        migrationType: config.migrationType,
                        targetRuntime: config.targetRuntime,
                        projectStructure: '',
                        activeProvider: activeProvider,
                        providerConfig: providerConfig,
                        instructions: instructions || '',
                    }),
                });

                if (!backendResponse.ok) {
                    throw new Error(`Backend error (${backendResponse.status}): ${await backendResponse.text()}`);
                }

                const reader = backendResponse.body?.getReader();
                if (!reader) throw new Error('No response body from backend');

                const decoder = new TextDecoder();
                let buffer = '';

                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;

                    if ((session as MigrationSessionState).status === 'stopped') {
                        job.status = 'failed';
                        job.error = 'Stopped by user';
                        break;
                    }

                    buffer += decoder.decode(value, { stream: true });
                    const lines = buffer.split('\n');
                    buffer = lines.pop() || '';

                    for (const line of lines) {
                        if (line.startsWith('data: ')) {
                            const data = line.slice(6).trim();
                            if (data === '[DONE]') continue;
                            try {
                                const parsed = JSON.parse(data);
                                const token = parsed?.contentBlockDelta?.delta?.text;
                                if (token) {
                                    streamedContent += token;
                                    tokenCount++;
                                    job.streamedContent = streamedContent;
                                    job.tokens = tokenCount;

                                    await writer.write(sseEvent(encoder, 'job:token', {
                                        jobId: job.id, token, tokenIndex: tokenCount,
                                    }));

                                    if (tokenCount % 10 === 0) {
                                        job.progress = Math.min(95, Math.round(50 + 45 * (1 - Math.exp(-tokenCount / 100))));
                                        await writer.write(sseEvent(encoder, 'job:progress', {
                                            jobId: job.id, progress: job.progress,
                                        }));
                                    }
                                }
                            } catch { /* skip */ }
                        }
                    }
                }

                if ((session as MigrationSessionState).status === 'stopped') break;

                const duration = Date.now() - startTime;
                job.status = 'done';
                job.progress = 100;
                job.completedAt = new Date().toISOString();
                job.duration = duration;
                session.completedJobs++;

                const providerModel = settings.providers[settings.activeProvider as keyof typeof settings.providers]?.model || 'unknown';
                const metadataString = `<!--metadata:provider:${settings.activeProvider};model:${providerModel};-->\n`;
                const finalContent = metadataString + streamedContent;

                const migratedCode = this.extractPrimaryCode(streamedContent);

                await dbFileStore.update(job.fileId, {
                    status: 'completed',
                    migratedContent: finalContent,
                    migratedCode: migratedCode,
                    activeMigrationId: session.sessionId,
                    tokens: tokenCount,
                });

                sessionTotalTokens += tokenCount;

                const doneLog = await dbLogStore.create({
                    projectId,
                    fileName: job.fileName,
                    status: 'success',
                    message: `✓ Migrated ${job.fileName} (${Math.round(duration)}ms, ${tokenCount} tokens)`,
                    duration,
                });
                job.logs.push(doneLog);
                batchFileResults.push({ fileId: job.fileId, fileName: job.fileName, filePath: job.filePath, status: 'completed' });

                await writer.write(sseEvent(encoder, 'job:done', {
                    jobId: job.id, fileId: job.fileId, fileName: job.fileName,
                    duration, tokenCount, migratedContent: streamedContent,
                }));
                await writer.write(sseEvent(encoder, 'job:log', { jobId: job.id, log: doneLog }));

            } catch (err) {
                const duration = Date.now() - startTime;
                const errorMsg = err instanceof Error ? err.message : 'Unknown error';

                job.status = 'failed';
                job.error = errorMsg;
                job.completedAt = new Date().toISOString();
                job.duration = duration;
                job.progress = 100;
                session.failedJobs++;

                await dbFileStore.updateStatus(job.fileId, 'failed');
                batchFileResults.push({ fileId: job.fileId, fileName: job.fileName, filePath: job.filePath, status: 'failed' });

                const errorLog = await dbLogStore.create({
                    projectId,
                    fileName: job.fileName,
                    status: 'error',
                    message: `✗ Failed to migrate ${job.fileName}: ${errorMsg}`,
                    duration,
                    stackTrace: err instanceof Error ? err.stack : undefined,
                });
                job.logs.push(errorLog);

                await writer.write(sseEvent(encoder, 'job:failed', {
                    jobId: job.id, fileName: job.fileName, error: errorMsg, duration,
                }));
                await writer.write(sseEvent(encoder, 'job:log', { jobId: job.id, log: errorLog }));
            }
        }

        // Session complete
        session.currentJobId = null;
        if ((session as MigrationSessionState).status !== 'stopped') {
            session.status = 'completed';
            session.completedAt = new Date().toISOString();

            // Sync project stats (totalFiles, migratedFiles, failedFiles, status, migrationRuns)
            await dbProjectStore.syncStats(projectId);

            // Save bundle as a project-level MigrationBatch record
            const batchStatus = session.failedJobs > 0 ? 'partial' : 'completed';
            const providerModel = settings.providers[settings.activeProvider as keyof typeof settings.providers]?.model || 'unknown';
            await dbBatchStore.upsert({
                id: session.sessionId,
                projectId,
                provider: settings.activeProvider,
                model: providerModel,
                status: batchStatus,
                startedAt: session.startedAt ?? new Date().toISOString(),
                completedAt: session.completedAt!,
                triggeredBy,
                fileResults: batchFileResults,
                totalFiles: session.totalJobs,
                completedFiles: session.completedJobs,
                failedFiles: session.failedJobs,
                totalTokens: sessionTotalTokens,
            });
            // Clear activeMigrationId on all files of this project now that migration is finished
            const projFiles = await dbFileStore.listByProject(projectId);
            await Promise.all(projFiles.map(f => 
                dbFileStore.update(f.id, { activeMigrationId: undefined })
            ));


            const completeLog = await dbLogStore.create({
                projectId,
                fileName: 'Migration Engine',
                status: 'success',
                message: `Migration complete — ${session.completedJobs} done, ${session.failedJobs} failed`,
                duration: 0,
            });

            await writer.write(sseEvent(encoder, 'session:complete', {
                totalJobs: session.totalJobs,
                completedJobs: session.completedJobs,
                failedJobs: session.failedJobs,
            }));
            await writer.write(sseEvent(encoder, 'job:log', { jobId: 'session', log: completeLog }));
        } else {
            await dbProjectStore.syncStats(projectId);
            // Save partial batch for stopped session
            const providerModel = settings.providers[settings.activeProvider as keyof typeof settings.providers]?.model || 'unknown';
            await dbBatchStore.upsert({
                id: session.sessionId,
                projectId,
                provider: settings.activeProvider,
                model: providerModel,
                status: 'stopped',
                startedAt: session.startedAt ?? new Date().toISOString(),
                completedAt: new Date().toISOString(),
                triggeredBy,
                fileResults: batchFileResults,
                totalFiles: session.totalJobs,
                completedFiles: session.completedJobs,
                failedFiles: session.failedJobs,
                totalTokens: sessionTotalTokens,
            });
            userMigrationGuard.release(triggeredBy.userId);
            await writer.write(sseEvent(encoder, 'session:stopped', {}));
        }

        await writer.close();
    },
};

/* ══════════════════════════════════════════════
   LLM Settings Store (per-user)
   ══════════════════════════════════════════════ */
const DEFAULT_LLM_SETTINGS: LLMSettings = {
    activeProvider: (process.env.ACTIVE_LLM_PROVIDER as LLMProviderType) || (process.env.DEFAULT_LLM_PROVIDER as LLMProviderType) || 'openai',
    providers: {
        nova: {
            apiKey: process.env.AWS_ACCESS_KEY_ID || '',
            model: process.env.BEDROCK_MODEL_ID || 'amazon.nova-lite-v1:0',
            enabled: !!process.env.AWS_ACCESS_KEY_ID,
        },
        claude: {
            apiKey: process.env.ANTHROPIC_API_KEY || '',
            model: 'claude-3-5-sonnet-20241022',
            enabled: !!process.env.ANTHROPIC_API_KEY
        },
        openai: {
            apiKey: process.env.OPENAI_API_KEY || '',
            model: process.env.OPENAI_MODEL || 'gpt-4o-mini',
            enabled: true
        },
        gemini: {
            apiKey: process.env.GEMINI_API_KEY || '',
            model: 'gemini-2.5-flash',
            enabled: !!process.env.GEMINI_API_KEY
        },
    },
    theme: 'system',
    notifications: true,
};

export const llmSettingsStore = {
    async get(userId: string): Promise<LLMSettings> {
        // Try DB first
        try {
            const settings = await prisma.userSettings.findUnique({
                where: { userId }
            });

            if (settings) {
                // NOTE: the DB `llmSettings` column stores settings.providers (not the full settings object).
                // We merge per-provider so individual missing keys fall back to defaults.
                const storedProviders = (settings.llmSettings as any) || {};
                return {
                    activeProvider: settings.activeProvider as LLMProviderType,
                    providers: {
                        nova:   { ...DEFAULT_LLM_SETTINGS.providers.nova,   ...(storedProviders.nova   || {}) },
                        claude: { ...DEFAULT_LLM_SETTINGS.providers.claude, ...(storedProviders.claude || {}) },
                        openai: { ...DEFAULT_LLM_SETTINGS.providers.openai, ...(storedProviders.openai || {}) },
                        gemini: { ...DEFAULT_LLM_SETTINGS.providers.gemini, ...(storedProviders.gemini || {}) },
                    },
                    theme: (settings.editorSettings as any)?.theme || DEFAULT_LLM_SETTINGS.theme,
                    notifications: (settings.editorSettings as any)?.notifications ?? DEFAULT_LLM_SETTINGS.notifications,
                };
            }
        } catch (error) {
            console.error('Failed to get LLM settings from DB:', error);
        }

        // Fallback to memory map then defaults
        return llmSettingsMap.get(userId) || { ...DEFAULT_LLM_SETTINGS };
    },

    async save(userId: string, settings: LLMSettings): Promise<LLMSettings> {
        // Save to memory map for fast access
        llmSettingsMap.set(userId, settings);

        // Verify user exists, create if required
        let user = await prisma.user.findUnique({ where: { id: userId } });
        if (!user) {
            user = await prisma.user.create({
                data: {
                    id: userId,
                    name: 'Developer',
                    role: 'developer'
                }
            });
        }

        // Save to DB (Throw errors to frontend instead of silently swallowing)
        await prisma.userSettings.upsert({
            where: { userId },
            update: {
                activeProvider: settings.activeProvider,
                llmSettings: settings.providers as any,
                editorSettings: {
                    theme: settings.theme,
                    notifications: settings.notifications
                } as any,
            },
            create: {
                userId,
                activeProvider: settings.activeProvider,
                llmSettings: settings.providers as any,
                editorSettings: {
                    theme: settings.theme,
                    notifications: settings.notifications
                } as any,
            }
        });

        return settings;
    },

    getDefaults(): LLMSettings {
        return { ...DEFAULT_LLM_SETTINGS };
    },
};

/* ══════════════════════════════════════════════
   Session management (cookie-based user tracking)
   ══════════════════════════════════════════════ */
const activeSessions: Map<string, string> = new Map();

export const sessionStore = {
    create(userId: string): string {
        const token = `sess-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
        activeSessions.set(token, userId);
        return token;
    },

    getUserId(token: string): string | undefined {
        return activeSessions.get(token);
    },

    destroy(token: string): void {
        activeSessions.delete(token);
    },
};








// /**
//  * Server-Side In-Memory Data Store
//  * Initialized from mockData — provides typed CRUD operations.
//  * Includes job-based migration engine with SSE streaming support.
//  */

// import {
//     Organization, Workspace, Project, ProjectFile,
//     MigrationLog, User, FileStatus, MigrationLogLevel,
//     MigrationJob, MigrationSessionState, SSEEventType,
//     LLMSettings, LLMProviderType, ProjectStatus, MigrationBatch,
//     MigrationRecord
// } from './types';
// import {
//     mockOrganizations, mockWorkspaces, mockProjects,
//     mockFiles, mockUser, mockMigrationBatches,
// } from './mockData';
// import type { LLMProvider, MigrationConfig } from './llm-provider';
// import {
//     dbFileStore, dbLogStore, dbBatchStore, dbProjectStore,
// } from './db-store';
// import { prisma } from './prisma';

// /* ─── User type with password ─── */
// interface StoredUser extends User {
//     password: string;
// }

// const g = globalThis as any;

// const migrationSessionsMap: Map<string, MigrationSessionState> = g.__ms_migrationSessionsMap || (g.__ms_migrationSessionsMap = new Map());
// /* ─── In-memory collections (bound to globalThis for Next.js API route sharing) ─── */
// if (!g.__ms_users) {
//     // Initialize users
//     g.__ms_users = [
//         { ...mockUser, password: 'password123' },
//     ];

//     // Clean up any stale migration sessions left from previous runs
//     // This ensures that workspace load does not see phantom active migrations.
//     // Iterate over any existing sessions and mark them as stopped, update related files.
//     const cleanupStaleMigrations = async () => {
//         // For each stored session, mark jobs as failed and clear activeMigrationId on files.
//         for (const [projectId, session] of migrationSessionsMap.entries()) {
//             // Mark session as stopped
//             session.status = 'stopped';
//             // Update each job status if still queued or running
//             session.jobs.forEach(job => {
//                 if (job.status === 'queued' || job.status === 'running') {
//                     job.status = 'failed';
//                 }
//             });
//             // Clear activeMigrationId on files belonging to this project
//             const projectFiles = getFiles().filter(f => f.projectId === projectId);
//             projectFiles.forEach(f => {
//                 if (f.activeMigrationId) {
//                     f.activeMigrationId = undefined;
//                 }
//                 // Reset any in‑progress status to pending so UI shows correct counts
//                 if (f.status === 'in-progress') {
//                     f.status = 'pending';
//                 }
//             });
//             // Remove session from map
//             migrationSessionsMap.delete(projectId);
//         }
//     };
//     // Run cleanup immediately (fire‑and‑forget). Errors are logged but do not block startup.
//     cleanupStaleMigrations().catch(err => console.error('Failed cleanup of stale migrations:', err));
//     } 
// // Initialize other global stores if not present
// if (!g.__ms_organizations) g.__ms_organizations = [...mockOrganizations];
// if (!g.__ms_workspaces) g.__ms_workspaces = [...mockWorkspaces];
// if (!g.__ms_projects) g.__ms_projects = [...mockProjects];
// if (!g.__ms_files) g.__ms_files = [...mockFiles];
// if (!g.__ms_migrationLogs) g.__ms_migrationLogs = [];

// // Lazy-init fields that may be missing on a warm server after a hot-reload or incremental deploy
// if (!g.__ms_migration_batches) g.__ms_migration_batches = [...mockMigrationBatches];
// if (!g.__ms_user_active_migration) g.__ms_user_active_migration = new Map<string, string>();

// // Direct access to global collections to ensure consistency across API route executions
// const getUsers = (): StoredUser[] => g.__ms_users;
// const getOrgs = (): Organization[] => g.__ms_organizations;
// const getWorkspaces = (): Workspace[] => g.__ms_workspaces;
// const getProjects = (): Project[] => g.__ms_projects;
// const getFiles = (): ProjectFile[] => g.__ms_files;
// const getLogs = (): MigrationLog[] => g.__ms_migrationLogs;

// // const migrationSessionsMap: Map<string, MigrationSessionState> = g.__ms_migrationSessionsMap; // moved earlier
// const llmSettingsMap: Map<string, LLMSettings> = g.__ms_llmSettingsMap;
// const sessionTokens: Map<string, string> = g.__ms_sessionTokens;

// // Sync project stats from actual file data once on cold-boot
// if (!g.__ms_stats_synced) {
//     g.__ms_stats_synced = true;
//     getProjects().forEach((p: Project) => syncProjectStats(p.id));
// }

// /* ══════════════════════════════════════════════
//    Users
//    ══════════════════════════════════════════════ */
// export const userStore = {
//     findByEmail(email: string): StoredUser | undefined {
//         return getUsers().find(u => u.email.toLowerCase() === email.toLowerCase());
//     },

//     findById(id: string): StoredUser | undefined {
//         return getUsers().find(u => u.id === id);
//     },

//     create(name: string, email: string, password: string): User {
//         const newUser: StoredUser = {
//             id: `user-${Date.now()}`,
//             name,
//             email,
//             password,
//             role: 'developer',
//             avatar: '',
//         };
//         getUsers().push(newUser);
//         const { password: _, ...safe } = newUser;
//         return safe;
//     },

//     updateProfile(id: string, updates: Partial<User>): User | null {
//         const uItems = getUsers();
//         const idx = uItems.findIndex(u => u.id === id);
//         if (idx === -1) return null;
//         uItems[idx] = { ...uItems[idx], ...updates };
//         const { password: _, ...safe } = uItems[idx];
//         return safe;
//     },

//     updatePassword(id: string, currentPwd: string, newPwd: string): boolean {
//         const uItems = getUsers();
//         const idx = uItems.findIndex(u => u.id === id);
//         if (idx === -1 || uItems[idx].password !== currentPwd) return false;
//         uItems[idx].password = newPwd;
//         return true;
//     },

//     toSafe(user: StoredUser): User {
//         const { password: _, ...safe } = user;
//         return safe;
//     },
// };

// /* ══════════════════════════════════════════════
//    Organizations
//    ══════════════════════════════════════════════ */
// export const orgStore = {
//     list(): Organization[] {
//         return getOrgs();
//     },

//     findById(id: string): Organization | undefined {
//         return getOrgs().find(o => o.id === id);
//     },

//     create(org: Omit<Organization, 'id' | 'createdAt' | 'workspaceCount'>): Organization {
//         const newOrg: Organization = {
//             ...org,
//             id: `org-${Date.now()}`,
//             createdAt: new Date().toISOString().split('T')[0],
//             workspaceCount: 0,
//         };
//         getOrgs().push(newOrg);
//         return newOrg;
//     },
// };

// /* ══════════════════════════════════════════════
//    Workspaces
//    ══════════════════════════════════════════════ */
// export const workspaceStore = {
//     listByOrg(orgId: string): Workspace[] {
//         return getWorkspaces().filter(w => w.orgId === orgId);
//     },

//     findById(id: string): Workspace | undefined {
//         return getWorkspaces().find(w => w.id === id);
//     },

//     create(ws: Omit<Workspace, 'id' | 'projectCount'>): Workspace {
//         const newWs: Workspace = {
//             ...ws,
//             id: `ws-${Date.now()}`,
//             projectCount: 0,
//         };
//         getWorkspaces().push(newWs);
//         // Increment workspaceCount in the org
//         const org = getOrgs().find(o => o.id === ws.orgId);
//         if (org) org.workspaceCount++;
//         return newWs;
//     },
//     // Delete a workspace only if it has no projects
//     delete(workspaceId: string): boolean {
//         const wsList = getWorkspaces();
//         const wsIdx = wsList.findIndex(w => w.id === workspaceId);
//         if (wsIdx === -1) return false;

//         const ws = wsList[wsIdx];
//         const hasProjects = getProjects().some(p => p.workspaceId === workspaceId);
//         if (hasProjects) return false;

//         // Decrement workspaceCount in the org
//         const org = getOrgs().find(o => o.id === ws.orgId);
//         if (org) org.workspaceCount = Math.max(0, org.workspaceCount - 1);

//         g.__ms_workspaces = getWorkspaces().filter(w => w.id !== workspaceId);
//         return true;
//     },
// };

// /* ══════════════════════════════════════════════
//    Projects
//    ══════════════════════════════════════════════ */
// /* ══════════════════════════════════════════════
//    Project Stats Sync
//    Derives totalFiles, migratedFiles, failedFiles,
//    migrationRuns and status from actual file data.
//    ══════════════════════════════════════════════ */
// export function syncProjectStats(projectId: string): void {
//     const projectFiles = getFiles().filter(f => f.projectId === projectId && f.type === 'file');
//     const totalFiles = projectFiles.length;
//     const migratedFiles = projectFiles.filter(f => f.status === 'completed').length;
//     const failedFiles = projectFiles.filter(f => f.status === 'failed').length;

//     // Count unique batch runs across all file.migrations arrays
//     const batchIds = new Set<string>();
//     projectFiles.forEach(f => f.migrations?.forEach(m => batchIds.add(m.id)));
//     const migrationRuns = batchIds.size;

//     // Derive status from file states
//     let status: ProjectStatus = 'pending';
//     if (totalFiles > 0) {
//         const inProgressCount = projectFiles.filter(f => f.status === 'in-progress').length;
//         if (inProgressCount > 0) {
//             status = 'in-progress';
//         } else if (migratedFiles + failedFiles === totalFiles) {
//             status = failedFiles > 0 ? 'failed' : 'completed';
//         } else if (migratedFiles > 0 || failedFiles > 0) {
//             status = 'in-progress';
//         }
//     }

//     const projectList = getProjects();
//     const idx = projectList.findIndex(p => p.id === projectId);
//     if (idx !== -1) {
//         projectList[idx] = {
//             ...projectList[idx],
//             totalFiles,
//             migratedFiles,
//             failedFiles,
//             migrationRuns,
//             status,
//             lastActivity: new Date().toISOString().split('T')[0],
//         };
//     }
// }

// export const projectStore = {
//     listByWorkspace(workspaceId: string): Project[] {
//         return getProjects().filter(p => p.workspaceId === workspaceId);
//     },

//     list(): Project[] {
//         return getProjects();
//     },

//     findById(id: string): Project | undefined {
//         return getProjects().find(p => p.id === id);
//     },

//     create(p: Omit<Project, 'id' | 'createdAt' | 'lastActivity' | 'totalFiles' | 'migratedFiles' | 'failedFiles' | 'status' | 'migrationRuns'>): Project {
//         const newProject: Project = {
//             ...p,
//             id: `proj-${Date.now()}`,
//             createdAt: new Date().toISOString().split('T')[0],
//             lastActivity: new Date().toISOString().split('T')[0],
//             totalFiles: 0,
//             migratedFiles: 0,
//             failedFiles: 0,
//             migrationRuns: 0,
//             status: 'pending',
//         };
//         getProjects().push(newProject);
//         // Increment projectCount in the workspace
//         const ws = getWorkspaces().find(w => w.id === p.workspaceId);
//         if (ws) ws.projectCount++;
//         return newProject;
//     },

//     update(id: string, updates: Partial<Project>): Project | null {
//         const projectList = getProjects();
//         const idx = projectList.findIndex(p => p.id === id);
//         if (idx === -1) return null;
//         projectList[idx] = { ...projectList[idx], ...updates };
//         return projectList[idx];
//     },
//     // Delete a project and its associated files and logs
//     delete(projectId: string): boolean {
//         const projectList = getProjects();
//         const projIdx = projectList.findIndex(p => p.id === projectId);
//         if (projIdx === -1) return false;
//         // Remove associated files
//         g.__ms_files = getFiles().filter(f => f.projectId !== projectId);

//         // Remove associated logs
//         g.__ms_migrationLogs = getLogs().filter(l => l.projectId !== projectId);

//         // Remove the project itself
//         const deletedProj = projectList[projIdx];
//         projectList.splice(projIdx, 1);
//         g.__ms_projects = projectList;

//         // Decrement projectCount in the workspace
//         const ws = getWorkspaces().find(w => w.id === deletedProj.workspaceId);
//         if (ws) ws.projectCount = Math.max(0, ws.projectCount - 1);

//         return true;
//     },
// };

// /* ══════════════════════════════════════════════
//    Files
//    ══════════════════════════════════════════════ */
// export const fileStore = {
//     listByProject(projectId: string): ProjectFile[] {
//         return getFiles().filter(f => f.projectId === projectId);
//     },

//     findById(id: string): ProjectFile | undefined {
//         return getFiles().find(f => f.id === id);
//     },

//     deleteByProject(projectId: string): number {
//         const currentFiles = getFiles();
//         const before = currentFiles.length;
//         const remaining = currentFiles.filter(f => f.projectId !== projectId);
//         const removed = before - remaining.length;
//         g.__ms_files = remaining;
//         return removed;
//     },

//     bulkCreate(newFiles: ProjectFile[]): ProjectFile[] {
//         getFiles().push(...newFiles);
//         return newFiles;
//     },

//     updateStatus(id: string, status: FileStatus): ProjectFile | null {
//         const fileList = getFiles();
//         const idx = fileList.findIndex(f => f.id === id);
//         if (idx === -1) return null;
//         fileList[idx] = { ...fileList[idx], status };
//         return fileList[idx];
//     },

//     updateContent(id: string, content: string): ProjectFile | null {
//         const fileList = getFiles();
//         const idx = fileList.findIndex(f => f.id === id);
//         if (idx === -1) return null;
//         fileList[idx] = { ...fileList[idx], content };
//         return fileList[idx];
//     },

//     updateMigratedContent(id: string, migratedContent: string): ProjectFile | null {
//         const fileList = getFiles();
//         const idx = fileList.findIndex(f => f.id === id);
//         if (idx === -1) return null;
//         fileList[idx] = { ...fileList[idx], migratedContent };
//         return fileList[idx];
//     },

//     update(id: string, updates: Partial<ProjectFile>): ProjectFile | null {
//         const fileList = getFiles();
//         const idx = fileList.findIndex(f => f.id === id);
//         if (idx === -1) return null;

//         const currentFile = fileList[idx];

//         // Handle Migration History Appending
//         if (updates.migratedContent && updates.activeMigrationId !== undefined) {
//             const provider = updates.migratedContent.includes('provider:') ? updates.migratedContent.split('provider:')[1].split(';')[0] : 'claude';
//             const model = updates.migratedContent.includes('model:') ? updates.migratedContent.split('model:')[1].split(';')[0] : 'unknown';

//             // Clean arbitrary prepended metadata markers from standard generation loop
//             let cleanContent = updates.migratedContent;
//             if (cleanContent.startsWith('<!--metadata:')) {
//                 cleanContent = cleanContent.split('-->\n')[1] || cleanContent;
//             }

//             const record: MigrationRecord = {
//                 id: updates.activeMigrationId,
//                 provider: provider as LLMProviderType,
//                 model: model,
//                 content: cleanContent,
//                 code: updates.migratedCode || jobEngine.extractPrimaryCode(cleanContent),
//                 tokens: updates.tokens ?? 0,
//                 createdAt: new Date().toISOString(),
//             };

//             const existingMigrations = currentFile.migrations || [];
//             fileList[idx] = {
//                 ...currentFile,
//                 ...updates,
//                 migratedContent: cleanContent,
//                 migratedCode: updates.migratedCode || record.code,
//                 migrations: [...existingMigrations, record],
//             };
//         } else {
//             fileList[idx] = { ...currentFile, ...updates };
//         }

//         return fileList[idx];
//     },
// };

// /* ══════════════════════════════════════════════
//    Migration Logs
//    ══════════════════════════════════════════════ */
// export const logStore = {
//     listByProject(projectId: string): MigrationLog[] {
//         return getLogs().filter(l => l.projectId === projectId);
//     },

//     create(log: Omit<MigrationLog, 'id' | 'timestamp'>): MigrationLog {
//         const newLog: MigrationLog = {
//             ...log,
//             id: `log-${Date.now()}-${Math.random().toString(36).substr(2, 5)}`,
//             timestamp: new Date().toISOString(),
//         };
//         getLogs().unshift(newLog);
//         return newLog;
//     },

//     clearByProject(projectId: string): void {
//         g.__ms_migrationLogs = getLogs().filter(l => l.projectId !== projectId);
//     },
// };

// /* ══════════════════════════════════════════════
//    Migration Batch Store — project-level bundles
//    One batch record per migration run; all files in
//    a run share the same batch id (session.sessionId).
//    ══════════════════════════════════════════════ */
// const getBatches = (): MigrationBatch[] => g.__ms_migration_batches;

// export const batchStore = {
//     listByProject(projectId: string): MigrationBatch[] {
//         return getBatches()
//             .filter(b => b.projectId === projectId)
//             .sort((a, b) => new Date(b.startedAt).getTime() - new Date(a.startedAt).getTime());
//     },

//     findById(id: string): MigrationBatch | undefined {
//         return getBatches().find(b => b.id === id);
//     },

//     create(batch: MigrationBatch): MigrationBatch {
//         // Replace if same id already exists (idempotent upsert)
//         const existing = getBatches().findIndex(b => b.id === batch.id);
//         if (existing !== -1) {
//             getBatches()[existing] = batch;
//             return batch;
//         }
//         getBatches().unshift(batch);
//         return batch;
//     },
// };

// /* ══════════════════════════════════════════════
//    Per-User Migration Guard
//    Ensures only one active migration per user.
//    ══════════════════════════════════════════════ */
// export const userMigrationGuard = {
//     getActiveProject(userId: string): string | undefined {
//         // Returns the projectId of the currently active migration for the user, if any.
//         return __ms_user_active_migration.get(userId);
//     },
//     claim(userId: string, projectId: string): boolean {
//         // Attempt to claim a migration for the user. If the user already has an active migration
//         // (different projectId), the claim fails and returns false. Otherwise, store the claim and return true.
//         const existing = __ms_user_active_migration.get(userId);
//         if (existing && existing !== projectId) {
//             return false; // another migration in progress for this user
//         }
//         __ms_user_active_migration.set(userId, projectId);
//         return true;
//     },
//     release(userId: string): void {
//         // Release any active migration claim for the user.
//         __ms_user_active_migration.delete(userId);
//     },
// };

// /* ══════════════════════════════════════════════
//    SSE Helper — sends an event through a writer
//    ══════════════════════════════════════════════ */
// function sseEvent(encoder: TextEncoder, event: SSEEventType, data: unknown): Uint8Array {
//     return encoder.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`);
// }

// /* ══════════════════════════════════════════════
//    Job Engine — server-side job queue with SSE streaming
//    ══════════════════════════════════════════════ */
// export const jobEngine = {
//     getSession(projectId: string): MigrationSessionState | undefined {
//         return migrationSessionsMap.get(projectId);
//     },

//     async createSession(projectId: string, includeCompleted = false): Promise<MigrationSessionState> {
//         const allFiles = await dbFileStore.listByProject(projectId);
//         const migratableFiles = allFiles.filter(
//             f => f.type === 'file' && (includeCompleted || f.status !== 'completed')
//         );

//         const jobs: MigrationJob[] = migratableFiles.map((file, idx) => ({
//             id: `job-${projectId}-${idx}-${Date.now()}`,
//             projectId,
//             fileId: file.id,
//             fileName: file.name,
//             filePath: file.path,
//             status: 'queued' as const,
//             progress: 0,
//             streamedContent: '',
//             tokens: 0,
//             logs: [],
//         }));

//         const session: MigrationSessionState = {
//             projectId,
//             sessionId: `mig-batch-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
//             status: 'running',
//             jobs,
//             totalJobs: jobs.length,
//             completedJobs: 0,
//             failedJobs: 0,
//             currentJobId: null,
//             startedAt: new Date().toISOString(),
//         };

//         migrationSessionsMap.set(projectId, session);
//         return session;
//     },

//     stopSession(projectId: string): void {
//         const session = migrationSessionsMap.get(projectId);
//         if (session) {
//             session.status = 'stopped';
//             session.currentJobId = null;
//             session.jobs.forEach(j => {
//                 if (j.status === 'running') j.status = 'failed';
//                 if (j.status === 'queued') j.status = 'failed';
//             });
//         }
//     },

//     async retryFailed(projectId: string): Promise<number> {
//         const allFiles = await dbFileStore.listByProject(projectId);
//         const failedFiles = allFiles.filter(f => f.status === 'failed');
//         await Promise.all(failedFiles.map(f => dbFileStore.updateStatus(f.id, 'pending')));

//         await dbLogStore.create({
//             projectId,
//             fileName: 'Migration Engine',
//             status: 'info',
//             message: `Resetting ${failedFiles.length} failed files for retry`,
//             duration: 0,
//         });

//         migrationSessionsMap.delete(projectId);
//         return failedFiles.length;
//     },

//     /**
//      * Extracts the primary code block from a Markdown report.
//      * Looks for [PRIMARY_CODE_BLOCK] marker or the largest code block.
//      */
//     extractPrimaryCode(content: string): string {
//         // First try the explicit marker
//         const marker = '[PRIMARY_CODE_BLOCK]';
//         const markerIndex = content.indexOf(marker);
//         if (markerIndex !== -1) {
//             const afterMarker = content.slice(markerIndex + marker.length);
//             const codeBlockMatch = afterMarker.match(/```(?:\w+)?\n([\s\S]*?)```/);
//             if (codeBlockMatch) return codeBlockMatch[1].trim();
//         }

//         // Fallback: extract all code blocks and pick the largest one (likely the handler)
//         const codeBlocks = Array.from(content.matchAll(/```(?:\w+)?\n([\s\S]*?)```/g), m => m[1].trim());
//         if (codeBlocks.length === 0) return '';

//         return codeBlocks.reduce((a, b) => a.length > b.length ? a : b);
//     },

//     /**
//      * Process all jobs via SSE streaming.
//      * Called from SSE endpoint — writes events directly to the response stream.
//      */
//     async processJobsWithStream(
//         projectId: string,
//         writer: WritableStreamDefaultWriter<Uint8Array>,
//         llmProvider: LLMProvider,
//         triggeredBy: { userId: string; userName: string } = { userId: 'system', userName: 'System' },
//         instructions?: string
//     ): Promise<void> {
//         const session = migrationSessionsMap.get(projectId);
//         if (!session) return;

//         const encoder = new TextEncoder();
//         const project = await dbProjectStore.findById(projectId);
//         const migrationConfig: Partial<MigrationConfig> = {
//             migrationType: project?.migrationType || 'mule4-lambda',
//             targetRuntime: project?.targetRuntime || 'nodejs',
//         };

//         // Send session:start
//         const jobSummaries = session.jobs.map(j => ({
//             id: j.id, fileId: j.fileId, fileName: j.fileName, filePath: j.filePath, status: j.status,
//         }));
//         await writer.write(sseEvent(encoder, 'session:start', {
//             projectId, sessionId: session.sessionId, totalJobs: session.totalJobs, jobs: jobSummaries,
//         }));

//         // Send all jobs as queued
//         for (const job of session.jobs) {
//             await writer.write(sseEvent(encoder, 'job:queued', {
//                 jobId: job.id, fileName: job.fileName, filePath: job.filePath,
//             }));
//         }

//         // Process jobs sequentially
//         let sessionTotalTokens = 0;
//         const batchFileResults: MigrationBatch['fileResults'] = [];
//         for (let i = 0; i < session.jobs.length; i++) {
//             if ((session as MigrationSessionState).status === 'stopped') break;

//             const job = session.jobs[i];
//             session.currentJobId = job.id;
//             job.status = 'running';
//             job.startedAt = new Date().toISOString();
//             job.progress = 0;

//             await dbFileStore.updateStatus(job.fileId, 'in-progress');

//             await writer.write(sseEvent(encoder, 'job:start', {
//                 jobId: job.id, fileName: job.fileName, index: i, total: session.totalJobs,
//             }));

//             const startLog = await dbLogStore.create({
//                 projectId,
//                 fileName: job.fileName,
//                 status: 'info',
//                 message: `Processing ${job.fileName}... (${i + 1}/${session.totalJobs})`,
//                 duration: 0,
//             });
//             job.logs.push(startLog);
//             await writer.write(sseEvent(encoder, 'job:log', { jobId: job.id, log: startLog }));

//             const startTime = Date.now();

//             try {
//                 const file = await dbFileStore.findById(job.fileId);
//                 if (!file) throw new Error(`File ${job.fileId} not found`);

//                 const config: MigrationConfig = {
//                     ...(migrationConfig as MigrationConfig),
//                     fileName: job.fileName,
//                     filePath: job.filePath,
//                     instructions,
//                 };

//                 let streamedContent = '';
//                 let tokenCount = 0;
//                 const generator = llmProvider.streamMigration(file.content, config);

//                 for await (const token of generator) {
//                     if ((session as MigrationSessionState).status === 'stopped') {
//                         job.status = 'failed';
//                         job.error = 'Stopped by user';
//                         break;
//                     }

//                     streamedContent += token;
//                     tokenCount++;
//                     job.streamedContent = streamedContent;
//                     job.tokens = tokenCount;

//                     await writer.write(sseEvent(encoder, 'job:token', {
//                         jobId: job.id, token, tokenIndex: tokenCount,
//                     }));

//                     if (tokenCount % 10 === 0) {
//                         job.progress = Math.min(95, Math.round(50 + 45 * (1 - Math.exp(-tokenCount / 100))));
//                         await writer.write(sseEvent(encoder, 'job:progress', {
//                             jobId: job.id, progress: job.progress,
//                         }));
//                     }
//                 }

//                 if ((session as MigrationSessionState).status === 'stopped') break;

//                 const duration = Date.now() - startTime;
//                 job.status = 'done';
//                 job.progress = 100;
//                 job.completedAt = new Date().toISOString();
//                 job.duration = duration;
//                 session.completedJobs++;

//                 const metadataString = `<!--metadata:provider:${llmProvider.name};model:${llmProvider.model || 'unknown'};-->\n`;
//                 const finalContent = metadataString + streamedContent;

//                 const migratedCode = this.extractPrimaryCode(streamedContent);

//                 await dbFileStore.update(job.fileId, {
//                     status: 'completed',
//                     migratedContent: finalContent,
//                     migratedCode: migratedCode,
//                     activeMigrationId: session.sessionId,
//                     tokens: tokenCount,
//                 });

//                 sessionTotalTokens += tokenCount;

//                 const doneLog = await dbLogStore.create({
//                     projectId,
//                     fileName: job.fileName,
//                     status: 'success',
//                     message: `✓ Migrated ${job.fileName} (${Math.round(duration)}ms, ${tokenCount} tokens)`,
//                     duration,
//                 });
//                 job.logs.push(doneLog);
//                 batchFileResults.push({ fileId: job.fileId, fileName: job.fileName, filePath: job.filePath, status: 'completed' });

//                 await writer.write(sseEvent(encoder, 'job:done', {
//                     jobId: job.id, fileId: job.fileId, fileName: job.fileName,
//                     duration, tokenCount, migratedContent: streamedContent,
//                 }));
//                 await writer.write(sseEvent(encoder, 'job:log', { jobId: job.id, log: doneLog }));

//             } catch (err) {
//                 const duration = Date.now() - startTime;
//                 const errorMsg = err instanceof Error ? err.message : 'Unknown error';

//                 job.status = 'failed';
//                 job.error = errorMsg;
//                 job.completedAt = new Date().toISOString();
//                 job.duration = duration;
//                 job.progress = 100;
//                 session.failedJobs++;

//                 await dbFileStore.updateStatus(job.fileId, 'failed');
//                 batchFileResults.push({ fileId: job.fileId, fileName: job.fileName, filePath: job.filePath, status: 'failed' });

//                 const errorLog = await dbLogStore.create({
//                     projectId,
//                     fileName: job.fileName,
//                     status: 'error',
//                     message: `✗ Failed to migrate ${job.fileName}: ${errorMsg}`,
//                     duration,
//                     stackTrace: err instanceof Error ? err.stack : undefined,
//                 });
//                 job.logs.push(errorLog);

//                 await writer.write(sseEvent(encoder, 'job:failed', {
//                     jobId: job.id, fileName: job.fileName, error: errorMsg, duration,
//                 }));
//                 await writer.write(sseEvent(encoder, 'job:log', { jobId: job.id, log: errorLog }));
//             }
//         }

//         // Session complete
//         session.currentJobId = null;
//         if ((session as MigrationSessionState).status !== 'stopped') {
//             session.status = 'completed';
//             session.completedAt = new Date().toISOString();

//             // Sync project stats (totalFiles, migratedFiles, failedFiles, status, migrationRuns)
//             await dbProjectStore.syncStats(projectId);

//             // Save bundle as a project-level MigrationBatch record
//             const batchStatus = session.failedJobs > 0 ? 'partial' : 'completed';
//             await dbBatchStore.upsert({
//                 id: session.sessionId,
//                 projectId,
//                 provider: llmProvider.name,
//                 model: llmProvider.model || 'unknown',
//                 status: batchStatus,
//                 startedAt: session.startedAt ?? new Date().toISOString(),
//                 completedAt: session.completedAt!,
//                 triggeredBy,
//                 fileResults: batchFileResults,
//                 totalFiles: session.totalJobs,
//                 completedFiles: session.completedJobs,
//                 failedFiles: session.failedJobs,
//                 totalTokens: sessionTotalTokens,
//             });
//             // Clear activeMigrationId on all files of this project now that migration is finished
//             const projFiles = await dbFileStore.listByProject(projectId);
//             await Promise.all(projFiles.map(f => 
//                 dbFileStore.update(f.id, { activeMigrationId: undefined })
//             ));


//             const completeLog = await dbLogStore.create({
//                 projectId,
//                 fileName: 'Migration Engine',
//                 status: 'success',
//                 message: `Migration complete — ${session.completedJobs} done, ${session.failedJobs} failed`,
//                 duration: 0,
//             });

//             await writer.write(sseEvent(encoder, 'session:complete', {
//                 totalJobs: session.totalJobs,
//                 completedJobs: session.completedJobs,
//                 failedJobs: session.failedJobs,
//             }));
//             await writer.write(sseEvent(encoder, 'job:log', { jobId: 'session', log: completeLog }));
//         } else {
//             await dbProjectStore.syncStats(projectId);
//             // Save partial batch for stopped session
//             await dbBatchStore.upsert({
//                 id: session.sessionId,
//                 projectId,
//                 provider: llmProvider.name,
//                 model: llmProvider.model || 'unknown',
//                 status: 'stopped',
//                 startedAt: session.startedAt ?? new Date().toISOString(),
//                 completedAt: new Date().toISOString(),
//                 triggeredBy,
//                 fileResults: batchFileResults,
//                 totalFiles: session.totalJobs,
//                 completedFiles: session.completedJobs,
//                 failedFiles: session.failedJobs,
//                 totalTokens: sessionTotalTokens,
//             });
//             userMigrationGuard.release(triggeredBy.userId);
//             await writer.write(sseEvent(encoder, 'session:stopped', {}));
//         }

//         await writer.close();
//     },
// };

// /* ══════════════════════════════════════════════
//    LLM Settings Store (per-user)
//    ══════════════════════════════════════════════ */
// const DEFAULT_LLM_SETTINGS: LLMSettings = {
//     // Nova Lite is the default/primary provider. Falls back to DEFAULT_LLM_PROVIDER env var.
//     activeProvider: (process.env.DEFAULT_LLM_PROVIDER as LLMProviderType) || 'nova',
//     providers: {
//         // Amazon Nova Lite (AWS Bedrock) — primary configured provider
//         // apiKey stores AWS_ACCESS_KEY_ID; AWS_SECRET_ACCESS_KEY is read server-side.
//         nova: {
//             apiKey: process.env.AWS_ACCESS_KEY_ID || '',
//             model: process.env.BEDROCK_MODEL_ID || 'amazon.nova-lite-v1:0',
//             enabled: !!process.env.AWS_ACCESS_KEY_ID,
//         },
//         claude: {
//             apiKey: process.env.ANTHROPIC_API_KEY || '',
//             model: 'claude-sonnet-4-20250514',
//             enabled: !!process.env.ANTHROPIC_API_KEY
//         },
//         openai: {
//             apiKey: process.env.OPENAI_API_KEY || '',
//             model: 'gpt-4o',
//             enabled: !!process.env.OPENAI_API_KEY
//         },
//         gemini: {
//             apiKey: process.env.GEMINI_API_KEY || '',
//             model: 'gemini-2.5-flash',
//             enabled: !!process.env.GEMINI_API_KEY
//         },
//     },
//     theme: 'system',
//     notifications: true,
// };

// export const llmSettingsStore = {
//     async get(userId: string): Promise<LLMSettings> {
//         // Try DB first
//         try {
//             const settings = await prisma.userSettings.findUnique({
//                 where: { userId }
//             });

//             if (settings) {
//                 return {
//                     activeProvider: settings.activeProvider as LLMProviderType,
//                     // Use logical merge with defaults to ensure all fields exist
//                     providers: {
//                         ...DEFAULT_LLM_SETTINGS.providers,
//                         ...(settings.llmSettings as any || {})
//                     },
//                     theme: (settings.editorSettings as any)?.theme || DEFAULT_LLM_SETTINGS.theme,
//                     notifications: (settings.editorSettings as any)?.notifications ?? DEFAULT_LLM_SETTINGS.notifications,
//                 };
//             }
//         } catch (error) {
//             console.error('Failed to get LLM settings from DB:', error);
//         }

//         // Fallback to memory map then defaults
//         return llmSettingsMap.get(userId) || { ...DEFAULT_LLM_SETTINGS };
//     },

//     async save(userId: string, settings: LLMSettings): Promise<LLMSettings> {
//         // Save to memory map for fast access
//         llmSettingsMap.set(userId, settings);

//         // Verify user exists, create if required
//         let user = await prisma.user.findUnique({ where: { id: userId } });
//         if (!user) {
//             user = await prisma.user.create({
//                 data: {
//                     id: userId,
//                     name: 'Developer',
//                     role: 'developer'
//                 }
//             });
//         }

//         // Save to DB (Throw errors to frontend instead of silently swallowing)
//         await prisma.userSettings.upsert({
//             where: { userId },
//             update: {
//                 activeProvider: settings.activeProvider,
//                 llmSettings: settings.providers as any,
//                 editorSettings: {
//                     theme: settings.theme,
//                     notifications: settings.notifications
//                 } as any,
//             },
//             create: {
//                 userId,
//                 activeProvider: settings.activeProvider,
//                 llmSettings: settings.providers as any,
//                 editorSettings: {
//                     theme: settings.theme,
//                     notifications: settings.notifications
//                 } as any,
//             }
//         });

//         return settings;
//     },

//     getDefaults(): LLMSettings {
//         return { ...DEFAULT_LLM_SETTINGS };
//     },
// };

// /* ══════════════════════════════════════════════
//    Session management (cookie-based user tracking)
//    ══════════════════════════════════════════════ */
// const activeSessions: Map<string, string> = new Map();

// export const sessionStore = {
//     create(userId: string): string {
//         const token = `sess-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
//         activeSessions.set(token, userId);
//         return token;
//     },

//     getUserId(token: string): string | undefined {
//         return activeSessions.get(token);
//     },

//     destroy(token: string): void {
//         activeSessions.delete(token);
//     },
// };
