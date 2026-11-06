/**
 * Database-Backed Store
 * Replaces the in-memory store for Organizations, Workspaces, Projects,
 * ProjectFiles, MigrationLogs, and MigrationBatches.
 * All operations are async and backed by Prisma + PostgreSQL.
 *
 * The in-memory jobEngine, userMigrationGuard, llmSettingsStore, and
 * sessionStore remain in store.ts — they are ephemeral by nature.
 */

import { prisma } from '@/lib/prisma';
import type {
    Organization, Workspace, Project, ProjectFile,
    MigrationLog, MigrationBatch, MigrationRecord,
    FileStatus, MigrationLogLevel, ProjectStatus,
} from '@/lib/types';
import type { Prisma } from '@prisma/client';

/* ═══════════════════════════════════════════════════════════
   Base64 codec — backwards-compatible (prefix 'b64:')
   Existing rows without the prefix are passed through as-is.
   ═══════════════════════════════════════════════════════════ */
export const b64enc = (s: string): string =>
    'b64:' + Buffer.from(s ?? '', 'utf8').toString('base64');

export const b64dec = (s: string): string => {
    if (typeof s === 'string' && s.startsWith('b64:')) {
        try { return Buffer.from(s.slice(4), 'base64').toString('utf8'); }
        catch { return s; }
    }
    return s; // legacy un-encoded value — pass through unchanged
};

/* ═══════════════════════════════════════════════════════════
   Virtual folder tree reconstruction
   Rebuilds folders + parent-child links purely from file paths
   so we never have to rely on stored folder rows or children arrays.
   ═══════════════════════════════════════════════════════════ */
function buildVirtualTree(files: ProjectFile[], projectId: string): ProjectFile[] {
    const dirMap = new Map<string, ProjectFile>();

    const stableId = (dirPath: string) =>
        `folder-${projectId}-${dirPath.replace(/[^a-zA-Z0-9]/g, '-')}`;

    // Normalise file paths (strip any accidental leading slash)
    const normalised = files.map(f => ({
        ...f,
        path: f.path.replace(/^\/+/, ''),
    }));

    // Create one virtual folder node per unique directory prefix
    normalised.forEach(f => {
        const parts = f.path.split('/').filter(Boolean);
        for (let i = 1; i < parts.length; i++) {
            const dirPath = parts.slice(0, i).join('/');
            if (!dirMap.has(dirPath)) {
                dirMap.set(dirPath, {
                    id: stableId(dirPath),
                    projectId,
                    name: parts[i - 1],
                    path: dirPath,
                    type: 'folder',
                    language: '',
                    status: 'pending',
                    content: '',
                    migratedContent: '',
                    migratedCode: undefined,
                    activeMigrationId: undefined,
                    migrations: [],
                    children: [],
                    size: 0,
                    lastModified: new Date().toISOString(),
                });
            }
        }
    });

    const folders = Array.from(dirMap.values());
    const allItems: ProjectFile[] = [...folders, ...normalised];

    // Wire parent → child links
    allItems.forEach(item => {
        const lastSlash = item.path.lastIndexOf('/');
        if (lastSlash === -1) return; // root-level item — no parent
        const parentPath = item.path.substring(0, lastSlash);
        const parent = dirMap.get(parentPath);
        if (parent && !parent.children.includes(item.id)) {
            parent.children.push(item.id);
        }
    });

    return allItems;
}

/* ═══════════════════════════════════════════════════════════
   Domain-type mappers (Prisma row → app interface)
   ═══════════════════════════════════════════════════════════ */

type PrismaOrg = Prisma.OrganizationGetPayload<{ include: { _count: { select: { workspaces: true } } } }>;
type PrismaWs = Prisma.WorkspaceGetPayload<{ include: { _count: { select: { projects: true } } } }>;
type PrismaProject = Prisma.ProjectGetPayload<Record<string, never>>;
type PrismaFile = Prisma.ProjectFileGetPayload<{
    include: { migrations: true }
}>;
type PrismaLog = Prisma.MigrationLogGetPayload<Record<string, never>>;
type PrismaBatch = Prisma.MigrationBatchGetPayload<Record<string, never>>;

function mapOrg(row: PrismaOrg): Organization {
    return {
        id: row.id,
        name: row.name,
        description: row.description,
        owner: row.owner,
        logo: row.logo,
        createdAt: row.createdAt.toISOString().split('T')[0],
        workspaceCount: row._count.workspaces,
    };
}

function mapWorkspace(row: PrismaWs): Workspace {
    return {
        id: row.id,
        orgId: row.orgId,
        name: row.name,
        environment: row.environment as Workspace['environment'],
        memberCount: row.memberCount,
        projectCount: row._count.projects,
    };
}

function mapProject(row: PrismaProject): Project {
    const rawPlatform = (row as any).targetPlatform;
    const inferredPlatform = rawPlatform || (
        row.migrationType?.includes('cpi') || row.migrationType?.includes('sap') ||
        row.targetRuntime === 'groovy' || row.targetRuntime === 'cpi-xml' || row.targetRuntime === 'xslt'
            ? 'sap-integration-suite'
            : 'aws'
    );
    return {
        id: row.id,
        workspaceId: row.workspaceId,
        orgId: row.orgId,
        name: row.name,
        description: row.description ?? '',
        targetPlatform: inferredPlatform,
        migrationType: row.migrationType as Project['migrationType'],
        targetRuntime: row.targetRuntime as Project['targetRuntime'],
        sourceType: row.sourceType as Project['sourceType'],
        status: row.status as ProjectStatus,
        totalFiles: row.totalFiles,
        migratedFiles: row.migratedFiles,
        failedFiles: row.failedFiles,
        migrationRuns: row.migrationRuns,
        createdAt: row.createdAt.toISOString().split('T')[0],
        lastActivity: row.lastActivity.toISOString().split('T')[0],
    };
}

function mapFile(row: PrismaFile): ProjectFile {
    const migrationsSource = Array.isArray(row.migrations) ? row.migrations : [];
    const migrations: MigrationRecord[] = migrationsSource.map(m => ({
        id: m.id,
        provider: m.provider as MigrationRecord['provider'],
        model: m.model,
        content: b64dec(m.content),  // decode for display
        code: m.code ? b64dec(m.code) : undefined,
        tokens: m.tokens,
        createdAt: m.createdAt.toISOString(),
    }));

    return {
        id: row.id,
        projectId: row.projectId,
        name: row.name,
        path: row.path,
        type: row.type as 'file' | 'folder',
        language: row.language ?? 'plaintext',
        status: row.status as FileStatus,
        content: b64dec(row.content),           // decode for editor
        migratedContent: row.migratedContent ? b64dec(row.migratedContent) : '',
        migratedCode: row.migratedCode ? b64dec(row.migratedCode) : undefined,
        activeMigrationId: row.activeMigrationId ?? undefined,
        migrations,
        children: [],
        size: row.size,
        lastModified: row.lastModified.toISOString(),
    };
}

function mapLog(row: PrismaLog): MigrationLog {
    return {
        id: row.id,
        projectId: row.projectId,
        fileName: row.fileName,
        timestamp: row.timestamp.toISOString(),
        status: row.status as MigrationLogLevel,
        message: row.message,
        stackTrace: row.stackTrace ?? undefined,
        duration: row.duration ?? undefined,
    };
}

function mapBatch(row: PrismaBatch): MigrationBatch {
    const fileResults = Array.isArray(row.fileResults)
        ? (row.fileResults as MigrationBatch['fileResults'])
        : [];

    return {
        id: row.id,
        projectId: row.projectId,
        provider: row.provider,
        model: row.model,
        status: row.status as MigrationBatch['status'],
        startedAt: row.startedAt.toISOString(),
        completedAt: row.completedAt?.toISOString() ?? new Date().toISOString(),
        triggeredBy: {
            userId: row.triggeredById,
            userName: row.triggeredByName,
        },
        fileResults,
        totalFiles: row.totalFiles,
        completedFiles: row.completedFiles,
        failedFiles: row.failedFiles,
        totalTokens: row.totalTokens,
    };
}

async function ensureUser(userId: string): Promise<void> {
    if (!userId) return;
    try {
        await prisma.user.upsert({
            where: { id: userId },
            update: {},
            create: {
                id: userId,
                email: userId.includes('@') ? userId : `${userId}@local.internal`,
                name: 'Developer',
                role: 'developer',
            },
        });
    } catch {
        // Ignore duplicate concurrent upsert errors
    }
}

/* ═══════════════════════════════════════════════════════════
   Organizations
   ═══════════════════════════════════════════════════════════ */
export const dbOrgStore = {
    async list(userId: string): Promise<Organization[]> {
        const rows = await prisma.organization.findMany({
            where: { userId },
            include: { _count: { select: { workspaces: true } } },
            orderBy: { createdAt: 'asc' },
        });
        return rows.map(mapOrg);
    },

    async findById(id: string): Promise<Organization | null> {
        const row = await (prisma as any).organization.findUnique({
            where: { id },
            include: { _count: { select: { workspaces: true } } },
        });
        return row ? mapOrg(row) : null;
    },

    async create(
        userId: string,
        data: Omit<Organization, 'id' | 'createdAt' | 'workspaceCount'>
    ): Promise<Organization> {
        await ensureUser(userId);
        const row = await prisma.organization.create({
            data: {
                userId,
                name: data.name,
                description: data.description ?? '',
                owner: data.owner ?? '',
                logo: data.logo ?? '',
            },
            include: { _count: { select: { workspaces: true } } },
        });
        return mapOrg(row);
    },

    async delete(id: string): Promise<boolean> {
        try {
            await prisma.organization.delete({ where: { id } });
            return true;
        } catch {
            return false;
        }
    },

    async nameExists(name: string, excludeId?: string): Promise<boolean> {
        const row = await prisma.organization.findFirst({
            where: { name: { equals: name, mode: 'insensitive' }, NOT: excludeId ? { id: excludeId } : undefined },
        });
        return row !== null;
    },
};

/* ═══════════════════════════════════════════════════════════
   Workspaces
   ═══════════════════════════════════════════════════════════ */
export const dbWorkspaceStore = {
    async listByOrg(orgId: string): Promise<Workspace[]> {
        const rows = await prisma.workspace.findMany({
            where: { orgId },
            include: { _count: { select: { projects: true } } },
            orderBy: { name: 'asc' },
        });
        return rows.map(mapWorkspace);
    },

    async findById(id: string): Promise<Workspace | null> {
        const row = await prisma.workspace.findUnique({
            where: { id },
            include: { _count: { select: { projects: true } } },
        });
        return row ? mapWorkspace(row) : null;
    },

    async create(
        userId: string,
        data: Omit<Workspace, 'id' | 'projectCount'>
    ): Promise<Workspace> {
        await ensureUser(userId);
        const row = await prisma.workspace.create({
            data: {
                userId,
                orgId: data.orgId,
                name: data.name,
                environment: data.environment ?? 'dev',
                memberCount: data.memberCount ?? 1,
            },
            include: { _count: { select: { projects: true } } },
        });
        return mapWorkspace(row);
    },

    /** Delete only if no projects exist in this workspace. */
    async delete(workspaceId: string): Promise<boolean> {
        const projectCount = await prisma.project.count({ where: { workspaceId } });
        if (projectCount > 0) return false;
        try {
            await prisma.workspace.delete({ where: { id: workspaceId } });
            return true;
        } catch {
            return false;
        }
    },

    async nameExistsInOrg(orgId: string, name: string, excludeId?: string): Promise<boolean> {
        const row = await prisma.workspace.findFirst({
            where: {
                orgId,
                name: { equals: name, mode: 'insensitive' },
                NOT: excludeId ? { id: excludeId } : undefined,
            },
        });
        return row !== null;
    },
};

/* ═══════════════════════════════════════════════════════════
   Projects
   ═══════════════════════════════════════════════════════════ */
export const dbProjectStore = {
    async listByWorkspace(workspaceId: string): Promise<Project[]> {
        const rows = await prisma.project.findMany({
            where: { workspaceId },
            orderBy: { lastActivity: 'desc' },
        });
        return rows.map(mapProject);
    },

    async listByUser(userId: string): Promise<Project[]> {
        const rows = await prisma.project.findMany({
            where: { userId },
            orderBy: { lastActivity: 'desc' },
        });
        return rows.map(mapProject);
    },

    async findById(id: string): Promise<Project | null> {
        const row = await prisma.project.findUnique({ where: { id } });
        return row ? mapProject(row) : null;
    },

    async create(
        userId: string,
        data: Omit<Project, 'id' | 'createdAt' | 'lastActivity' | 'totalFiles' | 'migratedFiles' | 'failedFiles' | 'status' | 'migrationRuns'>
    ): Promise<Project> {
        await ensureUser(userId);
        const rawPlatform = (data as any).targetPlatform;
        const targetPlatform = rawPlatform || (
            data.migrationType?.includes('cpi') || data.migrationType?.includes('sap') ||
            data.targetRuntime === 'groovy' || data.targetRuntime === 'cpi-xml' || data.targetRuntime === 'xslt'
                ? 'sap-integration-suite'
                : 'aws'
        );
        const row = await prisma.project.create({
            data: {
                userId,
                workspaceId: data.workspaceId,
                orgId: data.orgId,
                name: data.name,
                description: data.description ?? '',
                targetPlatform,
                migrationType: data.migrationType,
                targetRuntime: data.targetRuntime,
                sourceType: data.sourceType,
            },
        });
        return mapProject(row);
    },

    async update(id: string, updates: Partial<Project>): Promise<Project | null> {
        try {
            const row = await prisma.project.update({
                where: { id },
                data: {
                    ...(updates.name !== undefined && { name: updates.name }),
                    ...(updates.description !== undefined && { description: updates.description }),
                    ...(updates.targetPlatform !== undefined && { targetPlatform: updates.targetPlatform }),
                    ...(updates.migrationType !== undefined && { migrationType: updates.migrationType }),
                    ...(updates.targetRuntime !== undefined && { targetRuntime: updates.targetRuntime }),
                    ...(updates.status !== undefined && { status: updates.status }),
                    ...(updates.totalFiles !== undefined && { totalFiles: updates.totalFiles }),
                    ...(updates.migratedFiles !== undefined && { migratedFiles: updates.migratedFiles }),
                    ...(updates.failedFiles !== undefined && { failedFiles: updates.failedFiles }),
                    ...(updates.migrationRuns !== undefined && { migrationRuns: updates.migrationRuns }),
                },
            });
            return mapProject(row);
        } catch {
            return null;
        }
    },

    async delete(projectId: string): Promise<boolean> {
        try {
            await prisma.project.delete({ where: { id: projectId } });
            return true;
        } catch {
            return false;
        }
    },

    /** Recalculate and persist stats derived from file records. */
    async syncStats(projectId: string): Promise<void> {
        const files = await prisma.projectFile.findMany({
            where: { projectId, type: 'file' },
            select: { status: true, migrations: { select: { id: true } } },
        });

        const total = files.length;
        const migrated = files.filter(f => f.status === 'completed').length;
        const failed = files.filter(f => f.status === 'failed').length;

        // Count distinct batch IDs across all file migration records
        const batchIds = new Set<string>();
        files.forEach(f => f.migrations.forEach(m => batchIds.add(m.id)));
        const runs = batchIds.size;

        let status: ProjectStatus = 'pending';
        if (total > 0) {
            const inProgress = files.filter(f => f.status === 'in-progress').length;
            if (inProgress > 0) {
                status = 'in-progress';
            } else if (migrated + failed === total) {
                status = failed > 0 ? 'failed' : 'completed';
            } else if (migrated > 0 || failed > 0) {
                status = 'in-progress';
            }
        }

        await prisma.project.update({
            where: { id: projectId },
            data: {
                totalFiles: total,
                migratedFiles: migrated,
                failedFiles: failed,
                migrationRuns: runs,
                status,
            },
        });
    },
};

/* ═══════════════════════════════════════════════════════════
   Project Files
   ═══════════════════════════════════════════════════════════ */

/** Extracts the largest or [PRIMARY_CODE_BLOCK]-marked code block from markdown. */
function extractPrimaryCode(content: string): string {
    const marker = '[PRIMARY_CODE_BLOCK]';
    const markerIdx = content.indexOf(marker);
    if (markerIdx !== -1) {
        const after = content.slice(markerIdx + marker.length);
        const m = after.match(/```(?:\w+)?\n([\s\S]*?)```/);
        if (m) return m[1].trim();
    }
    const blocks = Array.from(content.matchAll(/```(?:\w+)?\n([\s\S]*?)```/g), x => x[1].trim());
    if (blocks.length === 0) return '';
    return blocks.reduce((a, b) => (a.length > b.length ? a : b));
}

export const dbFileStore = {
    async listByProject(
        projectId: string,
        options?: { page?: number; take?: number; includeContent?: boolean; includeMigrations?: boolean }
    ): Promise<ProjectFile[]> {
        const page = Math.max(0, options?.page ?? 0);
        const take = Math.min(200, Math.max(1, options?.take ?? 50));
        const includeContent = options?.includeContent ?? false;
        const includeMigrations = options?.includeMigrations ?? false;
        // Fetch only actual files — folder nodes are virtual, built from paths.
        const rows = await prisma.projectFile.findMany({
            where: { projectId, type: 'file' },
            include: {
                migrations: includeMigrations
                    ? { orderBy: { createdAt: 'desc' }, take: 10 }
                    : false,
            },
            skip: page * take,
            take,
            orderBy: { path: 'asc' },
        });
        const files = rows.map(row => mapFile({
            ...row,
            content: includeContent ? row.content : b64enc(''),
            migratedContent: includeContent ? row.migratedContent : '',
            migratedCode: includeContent ? row.migratedCode : null,
        } as PrismaFile));
        // Reconstruct the full folder hierarchy from file paths.
        return buildVirtualTree(files, projectId);
    },

    async findById(id: string): Promise<ProjectFile | null> {
        const row = await prisma.projectFile.findUnique({
            where: { id },
            include: { migrations: { orderBy: { createdAt: 'asc' } } },
        });
        return row ? mapFile(row) : null;
    },

    async bulkCreate(files: Omit<ProjectFile, 'migrations'>[]): Promise<ProjectFile[]> {
        // Only persist actual files — folder nodes are reconstructed at read time.
        // Normalise paths: strip any accidental leading slash.
        const realFiles = files
            .filter(f => f.type === 'file')
            .map(f => ({ ...f, path: f.path.replace(/^\/+/, '') }));

        await prisma.projectFile.createMany({
            data: realFiles.map(f => ({
                id: f.id,
                projectId: f.projectId,
                name: f.name,
                path: f.path,
                type: f.type,
                language: f.language || 'plaintext',
                status: f.status || 'pending',
                content: b64enc(f.content),
                migratedContent: f.migratedContent ? b64enc(f.migratedContent) : '',
                migratedCode: f.migratedCode ? b64enc(f.migratedCode) : null,
                activeMigrationId: f.activeMigrationId ?? null,
                size: f.size,
                lastModified: f.lastModified ? new Date(f.lastModified) : new Date(),
            })),
            skipDuplicates: true,
        });

        const rows = await prisma.projectFile.findMany({
            where: { id: { in: files.map(f => f.id) } },
            include: { migrations: true },
        });
        return rows.map(mapFile);
    },

    async updateStatus(id: string, status: FileStatus): Promise<ProjectFile | null> {
        try {
            const row = await prisma.projectFile.update({
                where: { id },
                data: { status },
                include: { migrations: { orderBy: { createdAt: 'asc' } } },
            });
            return mapFile(row);
        } catch {
            return null;
        }
    },

    async updateContent(id: string, content: string): Promise<ProjectFile | null> {
        try {
            const row = await prisma.projectFile.update({
                where: { id },
                data: { content: b64enc(content) },  // encode for storage
                include: { migrations: { orderBy: { createdAt: 'asc' } } },
            });
            return mapFile(row);
        } catch {
            return null;
        }
    },

    /**
     * Full update — mirrors fileStore.update() in store.ts.
     * When activeMigrationId is provided, also creates a MigrationRecord.
     */
    async update(id: string, updates: Partial<ProjectFile>): Promise<ProjectFile | null> {
        try {
            // Determine whether we should append a MigrationRecord
            const shouldAppend =
                updates.migratedContent &&
                updates.activeMigrationId !== undefined;

            let cleanContent = updates.migratedContent ?? undefined;
            if (cleanContent?.startsWith('<!--metadata:')) {
                cleanContent = cleanContent.split('-->\n')[1] || cleanContent;
            }

            // Extract provider/model from metadata comment
            const rawContent = updates.migratedContent ?? '';
            const providerMatch = rawContent.match(/provider:([^;]+);/);
            const modelMatch = rawContent.match(/model:([^;]+);/);
            const provider = providerMatch?.[1] ?? 'claude';
            const model = modelMatch?.[1] ?? 'unknown';
            const code = updates.migratedCode ?? (cleanContent ? extractPrimaryCode(cleanContent) : undefined);

            // Encode values for DB storage (decoded on read in mapFile)
            const dbMigratedContent = cleanContent ? b64enc(cleanContent) : undefined;
            const dbMigratedCode = code ? b64enc(code) : undefined;
            const dbSourceContent = updates.content ? b64enc(updates.content) : undefined;

            const row = await prisma.projectFile.update({
                where: { id },
                data: {
                    ...(updates.status !== undefined && { status: updates.status }),
                    ...(dbMigratedContent !== undefined && { migratedContent: dbMigratedContent }),
                    ...(dbMigratedCode !== undefined && { migratedCode: dbMigratedCode }),
                    ...(updates.activeMigrationId !== undefined && { activeMigrationId: updates.activeMigrationId }),
                    ...(dbSourceContent !== undefined && { content: dbSourceContent }),
                    // Append migration record via nested create
                    ...(shouldAppend && updates.activeMigrationId && {
                        migrations: {
                            create: {
                                id: `${updates.activeMigrationId}-${id}`, // Unique per file in batch
                                provider,
                                model,
                                content: b64enc(cleanContent!),  // encode for storage
                                code: code ? b64enc(code) : null,
                                tokens: updates.tokens ?? 0,
                            },
                        },
                    }),
                },
                include: { migrations: { orderBy: { createdAt: 'asc' } } },
            });
            return mapFile(row);
        } catch {
            return null;
        }
    },

    async deleteByProject(projectId: string): Promise<number> {
        const result = await prisma.projectFile.deleteMany({ where: { projectId } });
        return result.count;
    },
};

/* ═══════════════════════════════════════════════════════════
   Migration Logs
   ═══════════════════════════════════════════════════════════ */
export const dbLogStore = {
    async listByProject(projectId: string): Promise<MigrationLog[]> {
        const rows = await prisma.migrationLog.findMany({
            where: { projectId },
            orderBy: { timestamp: 'desc' },
        });
        return rows.map(mapLog);
    },

    async create(log: Omit<MigrationLog, 'id' | 'timestamp'>): Promise<MigrationLog> {
        const row = await prisma.migrationLog.create({
            data: {
                projectId: log.projectId,
                fileName: log.fileName,
                status: log.status,
                message: log.message,
                stackTrace: log.stackTrace ?? null,
                duration: log.duration ?? null,
            },
        });
        return mapLog(row);
    },

    async clearByProject(projectId: string): Promise<void> {
        await prisma.migrationLog.deleteMany({ where: { projectId } });
    },
};

/* ═══════════════════════════════════════════════════════════
   Migration Batches
   ═══════════════════════════════════════════════════════════ */
export const dbBatchStore = {
    async listByProject(projectId: string, options?: { page?: number; take?: number }): Promise<MigrationBatch[]> {
        const page = Math.max(0, options?.page ?? 0);
        const take = Math.min(200, Math.max(1, options?.take ?? 50));
        const rows = await prisma.migrationBatch.findMany({
            where: { projectId },
            skip: page * take,
            take,
            orderBy: { startedAt: 'desc' },
        });
        return rows.map(mapBatch);
    },

    async findById(id: string): Promise<MigrationBatch | null> {
        const row = await prisma.migrationBatch.findUnique({ where: { id } });
        return row ? mapBatch(row) : null;
    },

    /** Upsert — mirrors batchStore.create() idempotency in store.ts. */
    async upsert(batch: MigrationBatch): Promise<MigrationBatch> {
        const data = {
            projectId: batch.projectId,
            provider: batch.provider,
            model: batch.model,
            status: batch.status,
            startedAt: new Date(batch.startedAt),
            completedAt: batch.completedAt ? new Date(batch.completedAt) : null,
            triggeredById: batch.triggeredBy.userId,
            triggeredByName: batch.triggeredBy.userName,
            fileResults: batch.fileResults as Prisma.InputJsonValue,
            totalFiles: batch.totalFiles,
            completedFiles: batch.completedFiles,
            failedFiles: batch.failedFiles,
            totalTokens: batch.totalTokens,
        };

        const row = await prisma.migrationBatch.upsert({
            where: { id: batch.id },
            create: { id: batch.id, ...data },
            update: data,
        });
        return mapBatch(row);
    },
};

/* ═══════════════════════════════════════════════════════════
   Convenience re-export — syncProjectStats alias
   ═══════════════════════════════════════════════════════════ */
export const syncProjectStatsDB = dbProjectStore.syncStats;
