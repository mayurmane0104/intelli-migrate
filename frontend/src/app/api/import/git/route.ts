import { NextRequest, NextResponse } from 'next/server';
import { dbFileStore, dbProjectStore } from '@/lib/db-store';
import { ProjectFile } from '@/lib/types';
import { callFastify } from '@/lib/server/fastify-proxy';

export const dynamic = 'force-dynamic';

/* ─── Constants ─── */
const MULESOFT_EXTENSIONS = new Set([
    '.xml', '.dwl', '.raml', '.yaml', '.yml',
    '.json', '.properties', '.groovy', '.wsdl', '.xsd',
]);
const MAX_FILES = 60;

/* ─── URL parsers ─── */
function parseGitHubUrl(url: string): { owner: string; repo: string } | null {
    try {
        const u = new URL(url);
        if (!u.hostname.includes('github.com')) return null;
        const parts = u.pathname.replace(/\.git$/, '').split('/').filter(Boolean);
        if (parts.length < 2) return null;
        return { owner: parts[0], repo: parts[1] };
    } catch { return null; }
}

function parseGitLabUrl(url: string): { projectPath: string; host: string } | null {
    try {
        const u = new URL(url);
        if (!u.hostname.includes('gitlab')) return null;
        const path = u.pathname.replace(/\.git$/, '').replace(/^\//, '');
        if (!path || path.split('/').length < 2) return null;
        return { projectPath: path, host: u.origin };
    } catch { return null; }
}

function isMuleSoftFile(filePath: string): boolean {
    if (
        filePath.startsWith('META-INF/maven/') ||
        filePath.startsWith('META-INF/mule-artifact/') ||
        filePath.endsWith('classloader-model.json')
    ) {
        return false;
    }
    const ext = '.' + (filePath.split('.').pop()?.toLowerCase() ?? '');
    return MULESOFT_EXTENSIONS.has(ext);
}

function detectLanguage(filename: string): string {
    const ext = filename.split('.').pop()?.toLowerCase() ?? '';
    const map: Record<string, string> = {
        xml: 'xml', dwl: 'dataweave', raml: 'raml',
        yaml: 'yaml', yml: 'yaml', json: 'json',
        properties: 'properties', groovy: 'groovy',
        wsdl: 'xml', xsd: 'xml',
    };
    return map[ext] ?? 'text';
}

function makeId(prefix: string): string {
    return `${prefix}-${Date.now()}-${Math.random().toString(36).slice(2, 9)}`;
}

async function triggerAnalysis(projectId: string, sourceRef: string, files: ProjectFile[]) {
    try {
        const response = await callFastify(`/api/projects/${projectId}/analysis/start`, {
            method: 'POST',
            body: {
                sourceRef,
                migrationType: 'mule4-lambda',
                targetRuntime: 'nodejs',
                requestedBy: 'import:git',
                fileManifest: files.map((entry) => ({
                    path: entry.path,
                    name: entry.name,
                    language: entry.language,
                })),
            },
        });
        return {
            analysisTriggered: response.ok,
            analysisJob: response.ok ? response.data : null,
            analysisTriggerError: response.ok ? null : `analysis_start_failed_${response.status}`,
        };
    } catch (error: any) {
        return {
            analysisTriggered: false,
            analysisJob: null,
            analysisTriggerError: error?.message || 'analysis_start_failed',
        };
    }
}

/* ─── GitHub helpers ─── */
function ghHeaders(token?: string): Record<string, string> {
    const h: Record<string, string> = {
        Accept: 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
    };
    if (token) h['Authorization'] = `Bearer ${token}`;
    return h;
}

async function ghFetchRepoMeta(owner: string, repo: string, token?: string) {
    const res = await fetch(`https://api.github.com/repos/${owner}/${repo}`, { headers: ghHeaders(token) });
    if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        const err = new Error(body.message || 'Repository not found') as any;
        err.status = res.status;
        throw err;
    }
    return res.json();
}

async function ghFetchTree(owner: string, repo: string, branch: string, token?: string) {
    const res = await fetch(
        `https://api.github.com/repos/${owner}/${repo}/git/trees/${branch}?recursive=1`,
        { headers: ghHeaders(token) }
    );
    if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        const err = new Error(body.message || 'Failed to fetch tree') as any;
        err.status = res.status;
        throw err;
    }
    return res.json();
}

/* ─── GitLab helpers ─── */
async function glFetchRepoMeta(host: string, projectPath: string, token?: string) {
    const headers: Record<string, string> = {};
    if (token) headers['PRIVATE-TOKEN'] = token;
    const res = await fetch(`${host}/api/v4/projects/${encodeURIComponent(projectPath)}`, { headers });
    if (!res.ok) {
        const err = new Error('GitLab repository not found or access denied') as any;
        err.status = res.status;
        throw err;
    }
    return res.json();
}

async function glFetchTree(host: string, projectPath: string, branch: string, token?: string): Promise<Array<{ type: string; path: string; name: string }>> {
    const headers: Record<string, string> = {};
    if (token) headers['PRIVATE-TOKEN'] = token;
    const res = await fetch(
        `${host}/api/v4/projects/${encodeURIComponent(projectPath)}/repository/tree?recursive=true&per_page=100&ref=${encodeURIComponent(branch)}`,
        { headers }
    );
    if (!res.ok) {
        const err = new Error('GitLab tree fetch failed') as any;
        err.status = res.status;
        throw err;
    }
    return res.json();
}

/* ════════════════════════════
   GET — Test connection
   ?repoUrl=...&branch=...&token=...
   ════════════════════════════ */
export async function GET(req: NextRequest) {
    const repoUrl = req.nextUrl.searchParams.get('repoUrl') ?? '';
    const branch = req.nextUrl.searchParams.get('branch') || 'main';
    const token = req.nextUrl.searchParams.get('token') || undefined;

    if (!repoUrl) return NextResponse.json({ error: 'repoUrl is required' }, { status: 400 });

    const gh = parseGitHubUrl(repoUrl);
    if (gh) {
        try {
            const [meta, treeData] = await Promise.all([
                ghFetchRepoMeta(gh.owner, gh.repo, token),
                ghFetchTree(gh.owner, gh.repo, branch, token).catch(() => null),
            ]);
            const filesFound = treeData
                ? (treeData.tree as Array<{ type: string; path: string }>)
                    .filter(i => i.type === 'blob' && isMuleSoftFile(i.path)).length
                : 0;
            return NextResponse.json({
                name: meta.full_name as string,
                description: (meta.description ?? '') as string,
                isPrivate: meta.private as boolean,
                stars: meta.stargazers_count as number,
                defaultBranch: meta.default_branch as string,
                filesFound,
            });
        } catch (err: any) {
            const status = err.status ?? 500;
            if (status === 401 || status === 403) {
                return NextResponse.json({ error: 'Access denied — add a personal access token for private repositories.' }, { status: 403 });
            }
            return NextResponse.json({ error: err.message || 'Could not reach GitHub' }, { status });
        }
    }

    const gl = parseGitLabUrl(repoUrl);
    if (gl) {
        try {
            const [meta, tree] = await Promise.all([
                glFetchRepoMeta(gl.host, gl.projectPath, token),
                glFetchTree(gl.host, gl.projectPath, branch, token).catch(() => [] as any[]),
            ]);
            const filesFound = (tree as Array<{ type: string; path: string }>)
                .filter(i => i.type === 'blob' && isMuleSoftFile(i.path)).length;
            return NextResponse.json({
                name: meta.path_with_namespace as string,
                description: (meta.description ?? '') as string,
                isPrivate: meta.visibility !== 'public',
                defaultBranch: meta.default_branch as string,
                filesFound,
            });
        } catch (err: any) {
            return NextResponse.json({ error: err.message || 'Could not reach GitLab' }, { status: err.status ?? 500 });
        }
    }

    return NextResponse.json({ error: 'Only GitHub and GitLab URLs are supported' }, { status: 400 });
}

/* ════════════════════════════
   POST — Import files
   { repoUrl, projectId, branch?, token?, subPath? }
   ════════════════════════════ */
export async function POST(req: NextRequest) {
    try {
        const importStartedAt = new Date().toISOString();
        const { repoUrl, projectId, branch = 'main', token, subPath } = await req.json() as {
            repoUrl: string; projectId?: string; branch?: string; token?: string; subPath?: string; provider?: string;
        };

        if (!repoUrl) return NextResponse.json({ error: 'Repository URL is required' }, { status: 400 });
        if (!projectId) return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
        if (!await dbProjectStore.findById(projectId)) return NextResponse.json({ error: 'Project not found' }, { status: 404 });

        const normalizedSubPath = subPath?.replace(/^\//, '').replace(/\/$/, '');

        /* ── GitHub ── */
        const gh = parseGitHubUrl(repoUrl);
        if (gh) {
            let treeData: any;
            try {
                treeData = await ghFetchTree(gh.owner, gh.repo, branch, token);
            } catch (err: any) {
                const s = err.status ?? 500;
                if (s === 401 || s === 403) return NextResponse.json({ error: 'Access denied. Add a personal access token for private repositories.' }, { status: 403 });
                if (s === 404) return NextResponse.json({ error: `Branch "${branch}" not found. Check the branch name and try again.` }, { status: 404 });
                return NextResponse.json({ error: err.message || 'Failed to fetch repository tree' }, { status: s });
            }

            const rawTree: Array<{ path: string; type: string }> = treeData.tree ?? [];
            const relevantItems = rawTree
                .filter(item => {
                    if (item.type !== 'blob') return false;
                    if (normalizedSubPath && !item.path.startsWith(normalizedSubPath + '/')) return false;
                    return isMuleSoftFile(item.path);
                })
                .slice(0, MAX_FILES);

            if (relevantItems.length === 0) {
                return NextResponse.json({
                    error: 'No MuleSoft source files found. Expected .xml, .dwl, .raml, .yaml, .json or .properties files.',
                }, { status: 404 });
            }

            // Fetch contents in batches of 10
            const fileResults: ProjectFile[] = [];
            for (let i = 0; i < relevantItems.length; i += 10) {
                const batch = relevantItems.slice(i, i + 10);
                const results = await Promise.all(batch.map(async item => {
                    try {
                        const rawUrl = `https://raw.githubusercontent.com/${gh.owner}/${gh.repo}/${branch}/${item.path}`;
                        const fetchHeaders: Record<string, string> = {};
                        if (token) fetchHeaders['Authorization'] = `Bearer ${token}`;
                        const res = await fetch(rawUrl, { headers: fetchHeaders });
                        if (!res.ok) return null;
                        const content = await res.text();
                        const filename = item.path.split('/').pop() ?? item.path;
                        return {
                            id: makeId('file'),
                            projectId,
                            name: filename,
                            path: item.path,
                            type: 'file' as const,
                            language: detectLanguage(filename),
                            status: 'pending' as const,
                            content,
                            migratedContent: '',
                            children: [],
                            size: content.length,
                            lastModified: new Date().toISOString(),
                        } satisfies ProjectFile;
                    } catch { return null; }
                }));
                fileResults.push(...(results.filter(Boolean) as ProjectFile[]));
            }

            if (fileResults.length === 0) {
                return NextResponse.json({ error: 'Could not retrieve file contents from repository.' }, { status: 500 });
            }

            // buildFileTree is no longer needed — the DB layer reconstructs
            // folder hierarchy from paths at read time.
            await dbFileStore.deleteByProject(projectId);
            await dbFileStore.bulkCreate(fileResults);
            await dbProjectStore.update(projectId, {
                totalFiles: fileResults.length,
                migratedFiles: 0,
                failedFiles: 0,
                status: 'pending',
                sourceType: 'git',
            });

            const analysis = await triggerAnalysis(projectId, repoUrl, fileResults);

            return NextResponse.json({
                success: true,
                message: `Imported ${fileResults.length} files from ${gh.owner}/${gh.repo}`,
                filesImported: fileResults.length,
                repoName: `${gh.owner}/${gh.repo}`,
                importStartedAt,
                ...analysis,
            });
        }

        /* ── GitLab ── */
        const gl = parseGitLabUrl(repoUrl);
        if (gl) {
            let tree: Array<{ type: string; path: string; name: string }>;
            try {
                tree = await glFetchTree(gl.host, gl.projectPath, branch, token);
            } catch (err: any) {
                return NextResponse.json({ error: err.message || 'Failed to fetch GitLab tree' }, { status: err.status ?? 500 });
            }

            const relevantItems = tree
                .filter(item => {
                    if (item.type !== 'blob') return false;
                    if (normalizedSubPath && !item.path.startsWith(normalizedSubPath + '/')) return false;
                    return isMuleSoftFile(item.path);
                })
                .slice(0, MAX_FILES);

            if (relevantItems.length === 0) {
                return NextResponse.json({ error: 'No MuleSoft source files found in this GitLab repository.' }, { status: 404 });
            }

            const glHeaders: Record<string, string> = {};
            if (token) glHeaders['PRIVATE-TOKEN'] = token;

            const fileResults: ProjectFile[] = [];
            for (let i = 0; i < relevantItems.length; i += 10) {
                const batch = relevantItems.slice(i, i + 10);
                const results = await Promise.all(batch.map(async item => {
                    try {
                        const encodedFilePath = encodeURIComponent(item.path);
                        const res = await fetch(
                            `${gl.host}/api/v4/projects/${encodeURIComponent(gl.projectPath)}/repository/files/${encodedFilePath}/raw?ref=${encodeURIComponent(branch)}`,
                            { headers: glHeaders }
                        );
                        if (!res.ok) return null;
                        const content = await res.text();
                        const filename = item.path.split('/').pop() ?? item.path;
                        return {
                            id: makeId('file'),
                            projectId,
                            name: filename,
                            path: item.path,
                            type: 'file' as const,
                            language: detectLanguage(filename),
                            status: 'pending' as const,
                            content,
                            migratedContent: '',
                            children: [],
                            size: content.length,
                            lastModified: new Date().toISOString(),
                        } satisfies ProjectFile;
                    } catch { return null; }
                }));
                fileResults.push(...(results.filter(Boolean) as ProjectFile[]));
            }

            if (fileResults.length === 0) {
                return NextResponse.json({ error: 'Could not retrieve file contents from GitLab.' }, { status: 500 });
            }

            // Folder hierarchy is reconstructed from paths at read time.
            await dbFileStore.deleteByProject(projectId);
            await dbFileStore.bulkCreate(fileResults);
            await dbProjectStore.update(projectId, {
                totalFiles: fileResults.length, migratedFiles: 0, failedFiles: 0,
                status: 'pending', sourceType: 'git',
            });

            const analysis = await triggerAnalysis(projectId, repoUrl, fileResults);

            return NextResponse.json({
                success: true,
                message: `Imported ${fileResults.length} files from ${gl.projectPath}`,
                filesImported: fileResults.length,
                repoName: gl.projectPath,
                importStartedAt,
                ...analysis,
            });
        }

        return NextResponse.json({ error: 'Only GitHub and GitLab URLs are currently supported.' }, { status: 400 });

    } catch (err) {
        console.error('[git import] unexpected error:', err);
        return NextResponse.json({ error: 'Unexpected error during import' }, { status: 500 });
    }
}
