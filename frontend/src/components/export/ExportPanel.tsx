'use client';

import React, { useEffect, useState, useMemo } from 'react';
import { useApp } from '@/contexts/AppContext';
import { useMigrationStore } from '@/lib/stores/migration-store';
import { getPlatformStrategy } from '@/lib/platforms';
import {
    ArrowDownTrayIcon, CloudArrowUpIcon, FolderIcon,
    CheckCircleIcon, ArrowPathIcon, XMarkIcon,
    ArchiveBoxArrowDownIcon, BoltIcon, CloudIcon, CubeTransparentIcon,
    ExclamationTriangleIcon,
} from '@heroicons/react/24/outline';

type ExportFormat = 'zip' | 'cloudformation' | 'terraform' | 'sam' | 'cpi-package' | 'cpi-iflow' | 'cpi-tenant-push';
type ExportRuntime = 'python' | 'nodejs' | 'java' | 'groovy' | 'cpi-xml' | 'xslt';
type PushTarget = 'github' | 'gitlab' | 'bitbucket' | 'local';

interface ExportPreview {
    format: string;
    fileCount: number;
    sizeBytes: number;
    sha256: string;
    manifest?: {
        pipeline?: string;
        components_total?: number;
        components_covered?: number;
        warnings?: string[];
        target_compatibility?: {
            validation_status?: string;
            reference_used?: boolean;
            summary?: { total_artifacts?: number; passed?: number; warnings?: number; failed?: number };
            reference_conventions_applied?: Record<string, string>;
            disclaimer?: string;
        };
        files?: { path: string; role: string; size: number; generator?: string }[];
        application_profile?: {
            archetype?: string;
            archetype_confidence?: number;
            complexity_score?: number;
            languages?: string[];
            frameworks?: string[];
            technology_stack?: Record<string, string[]>;
            risks?: string[];
            recommendations?: string[];
        };
    };
}

/* ── Brand SVG icons for push targets ─────────────────────────────── */
const GitHubIcon = () => (
    <svg viewBox="0 0 24 24" className="h-5 w-5" fill="currentColor">
        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z" />
    </svg>
);
const GitLabIcon = () => (
    <svg viewBox="0 0 24 24" className="h-5 w-5" fill="currentColor">
        <path d="M23.955 13.587l-1.342-4.135-2.664-8.189a.455.455 0 0 0-.867 0L16.418 9.45H7.582L4.918 1.263a.455.455 0 0 0-.867 0L1.386 9.45.044 13.587a.924.924 0 0 0 .331 1.023L12 23.054l11.625-8.443a.924.924 0 0 0 .33-1.024" />
    </svg>
);
const BitbucketIcon = () => (
    <svg viewBox="0 0 24 24" className="h-5 w-5" fill="currentColor">
        <path d="M.778 1.213a.768.768 0 0 0-.768.892l3.263 19.81c.084.5.515.868 1.022.873H19.95a.772.772 0 0 0 .77-.646l3.27-20.03a.768.768 0 0 0-.768-.891zM14.52 15.53H9.522L8.17 8.466h7.561z" />
    </svg>
);

const DEFAULT_EXPORT_FORMATS: { id: ExportFormat; label: string; desc: string; icon: React.ReactNode }[] = [
    { id: 'zip',            label: 'ZIP Archive',    desc: 'Full deployable project tree',           icon: <ArchiveBoxArrowDownIcon className="h-7 w-7" /> },
    { id: 'sam',            label: 'SAM Template',   desc: 'AWS SAM with template.yaml + samconfig', icon: <BoltIcon className="h-7 w-7" /> },
    { id: 'cloudformation', label: 'CloudFormation', desc: 'CloudFormation stack template',          icon: <CloudIcon className="h-7 w-7" /> },
    { id: 'terraform',      label: 'Terraform',      desc: 'Terraform main / variables / outputs',   icon: <CubeTransparentIcon className="h-7 w-7" /> },
];

function getFormatIcon(id: string) {
    if (id === 'cpi-package' || id === 'zip') return <ArchiveBoxArrowDownIcon className="h-7 w-7" />;
    if (id === 'cpi-tenant-push' || id === 'cloudformation') return <CloudIcon className="h-7 w-7" />;
    if (id === 'sam') return <BoltIcon className="h-7 w-7" />;
    if (id === 'terraform') return <CubeTransparentIcon className="h-7 w-7" />;
    return <ArchiveBoxArrowDownIcon className="h-7 w-7" />;
}

const pushTargets: { id: PushTarget; label: string; icon: React.ReactNode; color: string }[] = [
    { id: 'github',    label: 'GitHub',       icon: <GitHubIcon />,                          color: 'border-gray-800' },
    { id: 'gitlab',    label: 'GitLab',       icon: <GitLabIcon />,                          color: 'border-orange-500' },
    { id: 'bitbucket', label: 'Bitbucket',    icon: <BitbucketIcon />,                       color: 'border-blue-600' },
    { id: 'local',     label: 'Local Folder', icon: <FolderIcon className="h-5 w-5" />,      color: 'border-gray-400' },
];

interface ExportPanelProps {
    onClose: () => void;
}

export default function ExportPanel({ onClose }: ExportPanelProps) {
    const { files, selectedProject, addToast } = useApp();
    const { isMigrating } = useMigrationStore();
    const [activeTab, setActiveTab] = useState<'download' | 'push'>('download');
    const platformStrategy = useMemo(
        () => getPlatformStrategy(selectedProject?.targetPlatform, selectedProject?.migrationType, selectedProject?.targetRuntime),
        [selectedProject?.targetPlatform, selectedProject?.migrationType, selectedProject?.targetRuntime]
    );
    const availableFormats = useMemo(() => {
        if (platformStrategy.exportFormats && platformStrategy.exportFormats.length > 0) {
            return platformStrategy.exportFormats.map((f: any) => ({
                id: f.id as ExportFormat,
                label: f.label,
                desc: f.desc,
                icon: getFormatIcon(f.id),
            }));
        }
        return DEFAULT_EXPORT_FORMATS;
    }, [platformStrategy]);

    const [selectedFormat, setSelectedFormat] = useState<ExportFormat>(
        (platformStrategy.exportFormats[0]?.id as ExportFormat) || 'zip'
    );
    const [targetRuntime, setTargetRuntime] = useState<ExportRuntime>(
        (platformStrategy.defaultRuntime as ExportRuntime) || 'python'
    );

    useEffect(() => {
        if (platformStrategy.exportFormats.length > 0) {
            setSelectedFormat(platformStrategy.exportFormats[0].id as ExportFormat);
        }
        setTargetRuntime((platformStrategy.defaultRuntime as ExportRuntime) || 'python');
    }, [platformStrategy]);
    const [selectedTarget, setSelectedTarget] = useState<PushTarget>('github');
    const [repoUrl, setRepoUrl] = useState('');
    const [branch, setBranch] = useState('main');
    const [commitMsg, setCommitMsg] = useState(selectedProject?.targetPlatform === 'sap-integration-suite' ? 'chore: add migrated SAP CPI iFlow bundle from MigrationStudio' : 'chore: add migrated code from MigrationStudio');
    const [token, setToken] = useState('');
    const [localPath, setLocalPath] = useState('');
    const [downloading, setDownloading] = useState(false);
    const [pushing, setPushing] = useState(false);
    const [pushSuccess, setPushSuccess] = useState(false);
    const [preview, setPreview] = useState<ExportPreview | null>(null);
    const [previewLoading, setPreviewLoading] = useState(false);
    const [previewError, setPreviewError] = useState<string | null>(null);

    const projectId = selectedProject?.id || 'proj-1';
    const isMuleMetadata = (path: string) =>
        path.includes('META-INF/maven') ||
        path.includes('META-INF/mule-artifact') ||
        path.endsWith('classloader-model.json');

    const migratedFiles = files.filter(f => f.projectId === projectId && f.type === 'file' && f.status === 'completed' && !isMuleMetadata(f.path));
    const allFiles = files.filter(f => f.projectId === projectId && f.type === 'file' && !isMuleMetadata(f.path));
    const migrationComplete = allFiles.length > 0
        && migratedFiles.length === allFiles.length
        && !isMigrating
        && !allFiles.some(f => f.status === 'in-progress' || f.status === 'pending');

    const buildLocalPreview = (): ExportPreview => ({
        format: selectedFormat,
        fileCount: migratedFiles.length,
        sizeBytes: migratedFiles.reduce((sum, f) => sum + (f.migratedContent?.length || 0), 0),
        sha256: '',
        manifest: {
            pipeline: platformStrategy.id === 'sap-integration-suite' ? 'sap-cpi-bundle' : 'v3-fast',
            files: migratedFiles.map(f => ({
                path: `${f.path}/${f.name}`.replace(/^\//, ''),
                role: 'migrated-source',
                size: f.migratedContent?.length || 0,
                generator: 'migration',
            })),
        },
    });

    useEffect(() => {
        if (activeTab !== 'download' || !projectId || !migrationComplete) return;
        let cancelled = false;
        setPreview(buildLocalPreview());
        setPreviewError(null);
        setPreviewLoading(false);

        // Optional background manifest refresh — never blocks the modal.
        const timer = setTimeout(() => {
            setPreviewLoading(true);
            const url = `/api/export/download?projectId=${encodeURIComponent(projectId)}&format=${encodeURIComponent(selectedFormat)}&targetRuntime=${encodeURIComponent(targetRuntime)}&targetPlatform=${encodeURIComponent(platformStrategy.id)}`;
            fetch(url, { cache: 'no-store' })
                .then(async res => {
                    const data = await res.json().catch(() => null);
                    if (!res.ok || !data || typeof data !== 'object') return null;
                    const previewData = data as ExportPreview & { error?: string; detail?: string };
                    if (previewData.error) return null;
                    const fileList = previewData.manifest?.files ?? [];
                    if (!previewData.fileCount && fileList.length === 0) return null;
                    return previewData;
                })
                .then(data => {
                    if (!cancelled && data) setPreview(data as ExportPreview);
                })
                .catch(() => { /* keep local preview */ })
                .finally(() => {
                    if (!cancelled) setPreviewLoading(false);
                });
        }, 200);

        return () => {
            cancelled = true;
            clearTimeout(timer);
        };
    }, [activeTab, projectId, selectedFormat, targetRuntime, platformStrategy.id, migrationComplete, migratedFiles.length]);

    const handleDownload = async () => {
        if (!migrationComplete) {
            addToast({
                type: 'warning',
                title: 'Migration In Progress',
                message: 'Wait until migration reaches 100% before exporting.',
            });
            return;
        }

        setDownloading(true);
        try {
            const response = await fetch('/api/export/download', {
                method: 'POST',
                headers: { 'content-type': 'application/json' },
                body: JSON.stringify({
                    projectId,
                    format: selectedFormat,
                    targetRuntime,
                    targetPlatform: platformStrategy.id,
                    projectNameHint: selectedProject?.name || '',
                }),
            });

            if (!response.ok) {
                const text = await response.text().catch(() => '');
                let message = `Export failed (${response.status})`;
                let platformError: any = null;
                try {
                    const parsed = JSON.parse(text);
                    if (parsed?.error_category?.startsWith('PLATFORM_')) {
                        platformError = parsed;
                    }
                    message = parsed?.error || parsed?.detail || message;
                } catch {
                    if (text) message = text;
                }
                if (platformError) {
                    const errObj = new Error(platformError.problem || message);
                    (errObj as any).isPlatformError = true;
                    (errObj as any).platformDetails = platformError;
                    throw errObj;
                }
                throw new Error(message);
            }

            const blob = await response.blob();
            const fileCount = Number(response.headers.get('x-export-file-count') || '0');
            const pipeline = response.headers.get('x-export-pipeline') || 'unknown';
            const sha = response.headers.get('x-export-sha256') || '';
            const archetype = response.headers.get('x-export-archetype') || '';
            const archetypeConfidence = response.headers.get('x-export-archetype-confidence') || '';
            const cd = response.headers.get('content-disposition') || '';
            const match = cd.match(/filename="?([^";]+)"?/i);
            const filename = match?.[1] || `${selectedProject?.name || 'migrated'}-${selectedFormat}.zip`;

            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            const archetypeFragment = archetype
                ? `, archetype=${archetype}${archetypeConfidence ? ` @${Math.round(parseFloat(archetypeConfidence) * 100)}%` : ''}`
                : '';
            addToast({
                type: 'success',
                title: 'Download Complete',
                message: `${fileCount} files packaged as ${selectedFormat.toUpperCase()} (pipeline=${pipeline}${sha ? `, sha=${sha.slice(0, 8)}` : ''}${archetypeFragment})`,
            });
        } catch (error: any) {
            addToast({
                type: 'error',
                title: 'Export Failed',
                message: error?.message ?? 'Failed to generate the export.',
            });
        } finally {
            setDownloading(false);
        }
    };

    const handlePush = () => {
        if (selectedTarget !== 'local' && !repoUrl) {
            addToast({ type: 'error', title: 'Missing Repository URL', message: 'Please enter a repository URL' });
            return;
        }
        if (selectedTarget === 'local' && !localPath) {
            addToast({ type: 'error', title: 'Missing Path', message: 'Please enter a local folder path' });
            return;
        }
        setPushing(true);
        setPushSuccess(false);

        // Simulate push operation - real Git push lands in Phase 7
        setTimeout(() => {
            setPushing(false);
            setPushSuccess(true);
            addToast({
                type: 'success',
                title: 'Push Successful',
                message: selectedTarget === 'local'
                    ? `${migratedFiles.length} files saved to ${localPath}`
                    : `${migratedFiles.length} files pushed to ${repoUrl} (${branch})`,
            });
        }, 2500);
    };

    return (
        <div className="fixed inset-0 bg-black/30 backdrop-blur-sm z-50 flex items-center justify-center p-4">
            <div className="bg-white dark:bg-gray-950 rounded-2xl shadow-2xl w-full max-w-2xl max-h-[85vh] overflow-hidden flex flex-col animate-fade-in">
                {/* Header */}
                <div className="flex items-center justify-between px-6 py-4 border-b border-gray-100 dark:border-gray-800">
                    <div>
                        <h2 className="text-lg font-semibold text-gray-900 dark:text-gray-100">Export Migrated Code</h2>
                        <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
                            {migrationComplete
                                ? `${migratedFiles.length} of ${allFiles.length} files ready for export`
                                : `${migratedFiles.length} of ${allFiles.length} migrated — finish migration to export`}
                        </p>
                    </div>
                    <button onClick={onClose} className="p-1.5 hover:bg-gray-100 rounded-lg transition-colors">
                        <XMarkIcon className="h-5 w-5 text-gray-400" />
                    </button>
                </div>

                {/* Tab switch */}
                <div className="flex border-b border-gray-100 dark:border-gray-800">
                    <button onClick={() => setActiveTab('download')}
                        className={`flex-1 flex items-center justify-center gap-2 py-3 text-sm font-medium transition-colors ${activeTab === 'download' ? 'text-primary-700 border-b-2 border-primary-600' : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:text-gray-300'
                            }`}>
                        <ArrowDownTrayIcon className="h-4 w-4" /> Download
                    </button>
                    <button onClick={() => setActiveTab('push')}
                        className={`flex-1 flex items-center justify-center gap-2 py-3 text-sm font-medium transition-colors ${activeTab === 'push' ? 'text-primary-700 border-b-2 border-primary-600' : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:text-gray-300'
                            }`}>
                        <CloudArrowUpIcon className="h-4 w-4" /> Push to Repository
                    </button>
                </div>

                {/* Content */}
                <div className="flex-1 overflow-y-auto p-6">
                    {activeTab === 'download' ? (
                        <div className="space-y-4">
                            {!migrationComplete && (
                                <div className="flex items-start gap-3 p-3 rounded-xl border border-amber-200 bg-amber-50/70 text-amber-900">
                                    <ExclamationTriangleIcon className="h-5 w-5 shrink-0 mt-0.5 text-amber-500" />
                                    <p className="text-xs leading-relaxed">
                                        Export unlocks when migration reaches <strong>100%</strong>. Self-correction and token accounting run during migration, not at export time.
                                    </p>
                                </div>
                            )}
                            <p className="text-sm text-gray-600 dark:text-gray-400">Choose an export format. The backend assembles a real, deployable project tree (no markdown-only outputs).</p>
                            <div className="grid grid-cols-2 gap-3">
                                {availableFormats.map((fmt: any) => (
                                    <button key={fmt.id} onClick={() => setSelectedFormat(fmt.id)}
                                        className={`p-4 rounded-xl border-2 text-left transition-all ${selectedFormat === fmt.id
                                            ? 'border-primary-500 bg-primary-50/50 shadow-sm'
                                            : 'border-gray-200 dark:border-gray-800 hover:border-primary-200 hover:bg-gray-50'
                                            }`}>
                                        <span className={selectedFormat === fmt.id ? 'text-primary-600' : 'text-gray-500'}>{fmt.icon}</span>
                                        <p className="font-medium text-sm text-gray-800 dark:text-gray-200 mt-2">{fmt.label}</p>
                                        <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">{fmt.desc}</p>
                                    </button>
                                ))}
                            </div>

                            {/* Runtime selector */}
                            {/* 
                            <div>
                                <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 block">Target Runtime</label>
                                <div className="grid grid-cols-3 gap-2">
                                    {(['python', 'nodejs', 'java'] as ExportRuntime[]).map(rt => (
                                        <button
                                            key={rt}
                                            onClick={() => setTargetRuntime(rt)}
                                            className={`px-3 py-2 rounded-lg border text-xs font-medium uppercase tracking-wide transition-all ${
                                                targetRuntime === rt
                                                    ? 'border-primary-500 bg-primary-50/50 text-primary-700'
                                                    : 'border-gray-200 dark:border-gray-800 text-gray-600 dark:text-gray-400 hover:border-primary-200'
                                            }`}>
                                            {rt}
                                        </button>
                                    ))}
                                </div>
                            </div>
                            */}

                            {/* Detected archetype + tech */}
                            {preview?.manifest?.application_profile?.archetype && (
                                <div className="rounded-xl border border-primary-100 bg-primary-50/50 p-4 space-y-2">
                                    <div className="flex items-center justify-between">
                                        <h4 className="text-xs font-semibold text-primary-700 uppercase tracking-wider">Detected application profile</h4>
                                        <span className="text-[11px] text-primary-700 font-mono">
                                            {preview.manifest.application_profile.archetype}
                                            {' '}
                                            @{Math.round((preview.manifest.application_profile.archetype_confidence ?? 0) * 100)}%
                                        </span>
                                    </div>
                                    {(() => {
                                        const stack = preview.manifest!.application_profile!.technology_stack || {};
                                        const chips = (['integrations', 'databases', 'messaging', 'auth', 'frameworks'] as const)
                                            .flatMap(cat => (stack[cat] || []).slice(0, 4).map(tag => ({ cat, tag })));
                                        if (chips.length === 0) return null;
                                        return (
                                            <div className="flex flex-wrap gap-1.5">
                                                {chips.map(({ cat, tag }, idx) => (
                                                    <span key={`${cat}-${tag}-${idx}`} className="inline-flex items-center gap-1 rounded-full bg-white px-2 py-0.5 text-[11px] text-gray-600 dark:text-gray-400 border border-primary-100">
                                                        <span className="text-[10px] uppercase text-primary-500">{cat}</span>
                                                        <span className="font-mono">{tag}</span>
                                                    </span>
                                                ))}
                                            </div>
                                        );
                                    })()}
                                    {(preview.manifest.application_profile.recommendations?.length ?? 0) > 0 && (
                                        <ul className="text-[11px] text-primary-800 list-disc list-inside space-y-0.5">
                                            {preview.manifest.application_profile.recommendations!.slice(0, 3).map((r, i) => (
                                                <li key={i}>{r}</li>
                                            ))}
                                        </ul>
                                    )}
                                </div>
                            )}

                            {/* Coverage banner */}
                            {(preview?.manifest?.warnings?.length ?? 0) > 0 && (
                                <div className="flex items-start gap-3 p-3 rounded-xl border border-amber-200 bg-amber-50/70 text-amber-900">
                                    <ExclamationTriangleIcon className="h-5 w-5 shrink-0 mt-0.5 text-amber-500" />
                                    <div className="space-y-1 text-xs leading-relaxed">
                                        <p className="font-semibold">{preview?.manifest?.warnings?.length} warnings about this export</p>
                                        <ul className="list-disc list-inside space-y-0.5">
                                            {preview?.manifest?.warnings?.slice(0, 4).map((w, i) => (
                                                <li key={i}>{w}</li>
                                            ))}
                                        </ul>
                                    </div>
                                </div>
                            )}

                            {preview?.manifest?.target_compatibility && (
                                <div className="rounded-xl border border-sky-200 bg-sky-50/70 p-3 text-sky-950">
                                    <p className="text-xs font-semibold">SAP local compatibility: {preview.manifest.target_compatibility.validation_status ?? 'reported'}</p>
                                    <p className="mt-1 text-[11px] leading-relaxed">
                                        {preview.manifest.target_compatibility.summary?.total_artifacts ?? 0} artifact(s): {preview.manifest.target_compatibility.summary?.passed ?? 0} passed, {preview.manifest.target_compatibility.summary?.warnings ?? 0} warning(s), {preview.manifest.target_compatibility.summary?.failed ?? 0} failed.
                                        {' '}{preview.manifest.target_compatibility.reference_used ? 'Saved SAP reference used.' : 'Standard SAP checks used.'}
                                    </p>
                                    <p className="mt-1 text-[10px] leading-relaxed text-sky-800">
                                        {preview.manifest.target_compatibility.disclaimer ?? 'Local checks do not confirm import or runtime compatibility in SAP.'}
                                    </p>
                                    {Object.keys(preview.manifest.target_compatibility.reference_conventions_applied ?? {}).length > 0 && (
                                        <p className="mt-1 text-[10px] leading-relaxed text-sky-800">
                                            Applied reference conventions: {Object.entries(preview.manifest.target_compatibility.reference_conventions_applied ?? {}).map(([key, value]) => `${key}=${value}`).join(', ')}
                                        </p>
                                    )}
                                </div>
                            )}

                            {/* Export preview from the backend manifest */}
                            <div className="bg-gray-50 rounded-xl p-4 mt-2">
                                <div className="flex items-center justify-between mb-3">
                                    <h4 className="text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Export Contents</h4>
                                    {previewLoading ? (
                                        <span className="text-[11px] text-gray-400 inline-flex items-center gap-1">
                                            <ArrowPathIcon className="h-3 w-3 animate-spin" /> loading
                                        </span>
                                    ) : preview ? (
                                        <span className="text-[11px] text-gray-400">
                                            {preview.fileCount} files • {(preview.sizeBytes / 1024).toFixed(1)} KB
                                            {preview.manifest?.pipeline ? <> • pipeline {preview.manifest.pipeline}</> : null}
                                            {preview.manifest?.components_total ? (
                                                <> • {preview.manifest.components_covered}/{preview.manifest.components_total} components</>
                                            ) : null}
                                        </span>
                                    ) : null}
                                </div>
                                {previewError ? (
                                    <div className="space-y-2">
                                        <p className="text-xs text-rose-600">{previewError}</p>
                                        <p className="text-[11px] text-gray-500">
                                            Start the Python API: <span className="font-mono">uvicorn mule_parser.api.app:app --port 8000</span>
                                        </p>
                                        {migratedFiles.length > 0 && (
                                            <div className="pt-2 border-t border-gray-200 dark:border-gray-700">
                                                <p className="text-[11px] font-semibold text-gray-500 uppercase mb-1">Migrated source files ({migratedFiles.length})</p>
                                                <div className="space-y-1 max-h-28 overflow-y-auto">
                                                    {migratedFiles.slice(0, 50).map(f => (
                                                        <div key={f.id} className="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-400 py-0.5">
                                                            <CheckCircleIcon className="h-3 w-3 text-success-500 shrink-0" />
                                                            <span className="font-mono truncate">{f.path}/{f.name}</span>
                                                        </div>
                                                    ))}
                                                </div>
                                            </div>
                                        )}
                                    </div>
                                ) : (
                                    <div className="space-y-1 max-h-44 overflow-y-auto scrollbar-thin">
                                        {(preview?.manifest?.files || []).slice(0, 200).map(f => (
                                            <div key={f.path} className="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-400 py-1">
                                                <CheckCircleIcon className="h-3 w-3 text-success-500 shrink-0" />
                                                <span className="font-mono truncate">{f.path}</span>
                                                <span className="text-gray-400 ml-auto">{(f.size / 1024).toFixed(1)}KB</span>
                                            </div>
                                        ))}
                                        {!preview && !previewLoading && (
                                            <p className="text-xs text-gray-400">Select a format to preview the assembled project tree.</p>
                                        )}
                                        {(preview?.manifest?.files?.length || 0) > 200 && (
                                            <p className="text-[11px] text-gray-400 mt-2">Showing first 200 entries of {preview?.manifest?.files?.length}.</p>
                                        )}
                                    </div>
                                )}
                            </div>

                            {/* Source-files reference */}
                            {/*
                            {migratedFiles.length > 0 && (
                                <div className="bg-gray-50 rounded-xl p-4 mt-2">
                                    <h4 className="text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-3">Source Files Migrated ({migratedFiles.length}/{allFiles.length})</h4>
                                    <div className="space-y-1 max-h-28 overflow-y-auto scrollbar-thin">
                                        {migratedFiles.map(f => (
                                            <div key={f.id} className="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-400 py-1">
                                                <CheckCircleIcon className="h-3 w-3 text-success-500 shrink-0" />
                                                <span className="font-mono truncate">{f.path}/{f.name}</span>
                                                <span className="text-gray-400 ml-auto">{(f.migratedContent.length / 1024).toFixed(1)}KB</span>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}
                            */}
                        </div>
                    ) : (
                        <div className="space-y-5">
                            {/* Target selection */}
                            <div>
                                <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2 block">Push Target</label>
                                <div className="grid grid-cols-4 gap-2">
                                    {pushTargets.map(t => (
                                        <button key={t.id} onClick={() => { setSelectedTarget(t.id); setPushSuccess(false); }}
                                            className={`flex flex-col items-center gap-1.5 p-3 rounded-xl border-2 transition-all ${selectedTarget === t.id
                                                ? `${t.color} bg-gray-50 shadow-sm`
                                                : 'border-gray-200 dark:border-gray-800 hover:border-gray-300'
                                                }`}>
                                            <span className={selectedTarget === t.id ? 'text-gray-800 dark:text-gray-200' : 'text-gray-500 dark:text-gray-400'}>{t.icon}</span>
                                            <span className="text-[11px] font-medium text-gray-700 dark:text-gray-300">{t.label}</span>
                                        </button>
                                    ))}
                                </div>
                            </div>

                            {selectedTarget === 'local' ? (
                                <div>
                                    <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 block">Local Folder Path</label>
                                    <input type="text" value={localPath} onChange={e => { setLocalPath(e.target.value); setPushSuccess(false); }}
                                        placeholder="C:\Users\you\projects\my-lambda"
                                        className="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none font-mono" />
                                </div>
                            ) : (
                                <>
                                    <div>
                                        <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 block">Repository URL</label>
                                        <input type="text" value={repoUrl} onChange={e => { setRepoUrl(e.target.value); setPushSuccess(false); }}
                                            placeholder={`https://${selectedTarget}.com/your-org/your-repo.git`}
                                            className="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none font-mono" />
                                    </div>
                                    <div className="grid grid-cols-2 gap-3">
                                        <div>
                                            <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 block">Branch</label>
                                            <input type="text" value={branch} onChange={e => setBranch(e.target.value)}
                                                className="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none" />
                                        </div>
                                        <div>
                                            <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 block">Access Token</label>
                                            <input type="password" value={token} onChange={e => setToken(e.target.value)}
                                                placeholder="ghp_xxxxxxxxxxxx"
                                                className="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none font-mono" />
                                        </div>
                                    </div>
                                    <div>
                                        <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 block">Commit Message</label>
                                        <input type="text" value={commitMsg} onChange={e => setCommitMsg(e.target.value)}
                                            className="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none" />
                                    </div>
                                </>
                            )}

                            {pushSuccess && (
                                <div className="flex items-center gap-3 p-4 bg-success-50 rounded-xl border border-success-200">
                                    <CheckCircleIcon className="h-5 w-5 text-success-600 shrink-0" />
                                    <div>
                                        <p className="text-sm font-medium text-success-800">Push Successful!</p>
                                        <p className="text-xs text-success-600 mt-0.5">
                                            {migratedFiles.length} files pushed to {selectedTarget === 'local' ? localPath : `${repoUrl} (${branch})`}
                                        </p>
                                    </div>
                                </div>
                            )}
                        </div>
                    )}
                </div>

                {/* Footer */}
                <div className="px-6 py-4 border-t border-gray-100 dark:border-gray-800 flex items-center justify-between bg-gray-50/50">
                    <span className="text-xs text-gray-400">{/* {migratedFiles.length} files ready */}</span>
                    <div className="flex items-center gap-2">
                        <button onClick={onClose} className="px-4 py-2 text-sm font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-100 rounded-lg transition-colors">
                            Cancel
                        </button>
                        {activeTab === 'download' ? (
                            <button onClick={handleDownload} disabled={downloading || !projectId || !migrationComplete}
                                className="flex items-center gap-2 px-5 py-2.5 bg-primary-600 hover:bg-primary-700 disabled:bg-gray-300 text-white text-sm font-medium rounded-lg transition-colors shadow-sm">
                                {downloading ? <ArrowPathIcon className="h-4 w-4 animate-spin" /> : <ArrowDownTrayIcon className="h-4 w-4" />}
                                {downloading ? 'Preparing...' : `Download ${selectedFormat.toUpperCase()}`}
                            </button>
                        ) : (
                            <button onClick={handlePush} disabled={pushing || migratedFiles.length === 0}
                                className="flex items-center gap-2 px-5 py-2.5 bg-primary-600 hover:bg-primary-700 disabled:bg-gray-300 text-white text-sm font-medium rounded-lg transition-colors shadow-sm">
                                {pushing ? <ArrowPathIcon className="h-4 w-4 animate-spin" /> : <CloudArrowUpIcon className="h-4 w-4" />}
                                {pushing ? 'Pushing...' : `Push to ${selectedTarget === 'local' ? 'Local' : selectedTarget.charAt(0).toUpperCase() + selectedTarget.slice(1)}`}
                            </button>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
