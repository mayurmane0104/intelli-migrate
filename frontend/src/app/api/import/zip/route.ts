import { NextRequest, NextResponse } from 'next/server';
import { promises as fs } from 'fs';
import os from 'os';
import path from 'path';
import JSZip from 'jszip';
import { dbFileStore, dbProjectStore } from '@/lib/db-store';
import type { ProjectFile } from '@/lib/types';
import { callFastify } from '@/lib/server/fastify-proxy';

const MULESOFT_EXTENSIONS = ['.xml', '.dwl', '.raml', '.yaml', '.yml', '.json', '.properties', '.mf', '.groovy', '.java'];
const SKIP_PATH_SEGMENTS = ['.git', 'node_modules', 'target', '.mvn', '.idea', '__MACOSX'];

function detectLanguage(name: string): string {
    const ext = name.includes('.') ? name.substring(name.lastIndexOf('.')).toLowerCase() : '';
    const map: Record<string, string> = {
        '.xml': 'xml', '.dwl': 'dataweave', '.raml': 'yaml',
        '.yaml': 'yaml', '.yml': 'yaml', '.json': 'json',
        '.properties': 'properties', '.java': 'java', '.groovy': 'groovy',
    };
    return map[ext] || 'plaintext';
}

export async function POST(req: NextRequest) {
    try {
        const formData = await req.formData();
        const file = formData.get('file');
        const projectId = formData.get('projectId') as string | null;

        if (!file || !(file instanceof File)) {
            return NextResponse.json({ error: 'No file uploaded' }, { status: 400 });
        }
        if (!projectId) {
            return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
        }
        if (!file.name.endsWith('.zip') && !file.name.endsWith('.jar')) {
            return NextResponse.json({ error: 'Only .zip and .jar files are supported' }, { status: 400 });
        }

        const arrayBuffer = await file.arrayBuffer();
        const sourceArchivePath = path.join(
            os.tmpdir(),
            `migration-studio-${projectId}-${Date.now()}-${Math.random().toString(36).slice(2, 8)}${file.name.endsWith('.jar') ? '.jar' : '.zip'}`
        );
        await fs.writeFile(sourceArchivePath, Buffer.from(arrayBuffer));
        setTimeout(() => {
            fs.unlink(sourceArchivePath).catch(() => {});
        }, 30 * 60 * 1000);

        const zip = await JSZip.loadAsync(arrayBuffer);

        const now = new Date().toISOString();
        const seen = new Set<string>();

        const promises = Object.entries(zip.files).map(async ([relativePath, zipEntry]) => {
            if (zipEntry.dir) return null;

            // Skip paths that should not be imported
            const segments = relativePath.split('/');
            if (segments.some(seg => SKIP_PATH_SEGMENTS.includes(seg))) return null;

            // Skip internal Mule runtime / Maven metadata that are not application source
            if (
                relativePath.startsWith('META-INF/maven/') ||
                relativePath.startsWith('META-INF/mule-artifact/') ||
                relativePath.endsWith('classloader-model.json')
            ) {
                return null;
            }

            // If packaged inside META-INF/mule-src/<app-name>/, unwrap to original source path
            let cleanRelPath = relativePath;
            const muleSrcMatch = cleanRelPath.match(/^META-INF\/mule-src\/[^/]+\/(.*)$/);
            if (muleSrcMatch) {
                cleanRelPath = muleSrcMatch[1];
            }

            const cleanSegments = cleanRelPath.split('/');
            const fileName = cleanSegments[cleanSegments.length - 1];
            if (!fileName || fileName.startsWith('.')) return null;

            const ext = fileName.includes('.') ? fileName.substring(fileName.lastIndexOf('.')).toLowerCase() : '';
            if (!MULESOFT_EXTENSIONS.includes(ext)) return null;

            // De-duplicate paths
            const normalizedPath = `/${cleanRelPath}`;
            if (seen.has(normalizedPath)) return null;
            seen.add(normalizedPath);

            try {
                const content = await zipEntry.async('string');
                const fileId = `file-zip-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
                return {
                    id: fileId,
                    projectId,
                    name: fileName,
                    path: normalizedPath,
                    type: 'file' as const,
                    language: detectLanguage(fileName),
                    status: 'pending' as const,
                    content,
                    migratedContent: '',
                    children: [],
                    size: content.length,
                    lastModified: now,
                } satisfies ProjectFile;
            } catch {
                return null;
            }
        });

        const results = await Promise.all(promises);
        const validFiles = results.filter(Boolean) as ProjectFile[];

        if (validFiles.length === 0) {
            return NextResponse.json(
                { error: 'No MuleSoft files found in the archive. Expected .xml, .dwl, .raml, .yaml, .yml, .json, or .properties files.' },
                { status: 422 }
            );
        }

        await dbFileStore.deleteByProject(projectId);
        await dbFileStore.bulkCreate(validFiles);
        await dbProjectStore.update(projectId, {
            totalFiles: validFiles.length,
            migratedFiles: 0,
            failedFiles: 0,
            status: 'pending',
            sourceType: 'zip',
        });

        let analysisJob: unknown = null;
        let analysisTriggerError: string | null = null;
        try {
            const project = await dbProjectStore.findById(projectId);
            const analysisResult = await callFastify(`/api/projects/${projectId}/analysis/start`, {
                method: 'POST',
                body: {
                    sourcePath: sourceArchivePath,
                    migrationType: project?.migrationType || 'mule4-lambda',
                    targetRuntime: project?.targetRuntime || 'nodejs',
                    requestedBy: 'import:zip',
                    fileManifest: validFiles.map((entry) => ({
                        path: entry.path,
                        name: entry.name,
                        language: entry.language,
                    })),
                },
            });
            if (analysisResult.ok) {
                analysisJob = analysisResult.data;
            } else {
                analysisTriggerError = `analysis_start_failed_${analysisResult.status}`;
            }
        } catch (analysisError: any) {
            analysisTriggerError = analysisError?.message || 'analysis_start_failed';
        }

        return NextResponse.json({
            success: true,
            message: `Imported ${validFiles.length} files from ${file.name}`,
            filesExtracted: validFiles.length,
            importStartedAt: now,
            analysisTriggered: Boolean(analysisJob),
            analysisJob,
            analysisTriggerError,
        });
    } catch (err: any) {
        return NextResponse.json({ error: err?.message || 'Failed to process archive' }, { status: 500 });
    }
}
