'use client';

import React, { useState, useRef } from 'react';
import { useApp } from '@/contexts/AppContext';
import { importApi } from '@/lib/api';
import { useMigrationStore } from '@/lib/stores/migration-store';
import {
    XMarkIcon, ArrowPathIcon, CheckCircleIcon,
    ExclamationTriangleIcon, LinkIcon,
    FolderIcon, DocumentArrowUpIcon, LockClosedIcon,
    GlobeAltIcon, CodeBracketIcon, DocumentTextIcon,
    CogIcon, BeakerIcon, ServerStackIcon, WrenchScrewdriverIcon,
    StarIcon,
} from '@heroicons/react/24/outline';

/* ── Supported format entries (ASCII-safe, no emoji) ─────────────────── */
const SUPPORTED_FORMATS = [
    { icon: <CodeBracketIcon className="h-4 w-4 text-blue-500" />,       label: 'MuleSoft 3/4 XML flows' },
    { icon: <DocumentTextIcon className="h-4 w-4 text-purple-500" />,   label: 'RAML API specifications' },
    { icon: <WrenchScrewdriverIcon className="h-4 w-4 text-green-500" />, label: 'DataWeave transforms' },
    { icon: <ServerStackIcon className="h-4 w-4 text-orange-500" />,    label: 'Maven POM / Mule artifacts' },
    { icon: <BeakerIcon className="h-4 w-4 text-pink-500" />,           label: 'MUnit test suites' },
    { icon: <CogIcon className="h-4 w-4 text-gray-500" />,              label: 'Property / config files' },
];

type Provider = 'github' | 'gitlab' | 'bitbucket' | 'azure' | 'custom';

/* ── SVG brand icons ─────────────────────────────────────────────────── */
const GitHubIcon = () => (
    <svg viewBox="0 0 24 24" className="h-6 w-6" fill="currentColor">
        <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z" />
    </svg>
);

const GitLabIcon = () => (
    <svg viewBox="0 0 24 24" className="h-6 w-6" fill="currentColor">
        <path d="M23.955 13.587l-1.342-4.135-2.664-8.189a.455.455 0 0 0-.867 0L16.418 9.45H7.582L4.918 1.263a.455.455 0 0 0-.867 0L1.386 9.45.044 13.587a.924.924 0 0 0 .331 1.023L12 23.054l11.625-8.443a.924.924 0 0 0 .33-1.024" />
    </svg>
);

const BitbucketIcon = () => (
    <svg viewBox="0 0 24 24" className="h-6 w-6" fill="currentColor">
        <path d="M.778 1.213a.768.768 0 0 0-.768.892l3.263 19.81c.084.5.515.868 1.022.873H19.95a.772.772 0 0 0 .77-.646l3.27-20.03a.768.768 0 0 0-.768-.891zM14.52 15.53H9.522L8.17 8.466h7.561z" />
    </svg>
);

const AzureDevOpsIcon = () => (
    <svg viewBox="0 0 24 24" className="h-6 w-6" fill="currentColor">
        <path d="M0 5.008l4.456-3.82L18.204 6.78V.968l5.796 5.58-5.796 2.494v9.684l-5.84 4.306zM0 17.64l3.52-4.574 8.84 2.68L18.2 11.1v8.682L3.27 23.03z" />
    </svg>
);

const providers: { id: Provider; label: string; icon: React.ReactNode; placeholder: string }[] = [
    { id: 'github',    label: 'GitHub',       icon: <GitHubIcon />,                        placeholder: 'https://github.com/org/repo' },
    { id: 'gitlab',    label: 'GitLab',       icon: <GitLabIcon />,                        placeholder: 'https://gitlab.com/org/repo' },
    { id: 'bitbucket', label: 'Bitbucket',    icon: <BitbucketIcon />,                     placeholder: 'https://bitbucket.org/org/repo.git' },
    { id: 'azure',     label: 'Azure DevOps', icon: <AzureDevOpsIcon />,                   placeholder: 'https://dev.azure.com/org/project/_git/repo' },
    { id: 'custom',    label: 'Custom URL',   icon: <LinkIcon className="h-6 w-6" />,      placeholder: 'https://your-git-server.com/repo.git' },
];

type TestState = 'idle' | 'testing' | 'ok' | 'error';

interface RepoInfo {
    name: string;
    description: string;
    isPrivate: boolean;
    stars?: number;
    defaultBranch: string;
    filesFound: number;
}

interface ImportPanelProps {
    onClose: (imported?: boolean) => void;
}

export default function ImportPanel({ onClose }: ImportPanelProps) {
    const { addToast, selectedProject, refreshFiles } = useApp();
    const resetProjectTiming = useMigrationStore((state) => state.resetProjectTiming);
    const [activeTab, setActiveTab]     = useState<'git' | 'upload'>('git');
    const [provider, setProvider]       = useState<Provider>('github');
    const [repoUrl, setRepoUrl]         = useState('');
    const [branch, setBranch]           = useState('main');
    const [token, setToken]             = useState('');
    const [subPath, setSubPath]         = useState('');
    const [testState, setTestState]     = useState<TestState>('idle');
    const [testError, setTestError]     = useState('');
    const [repoInfo, setRepoInfo]       = useState<RepoInfo | null>(null);
    const [importing, setImporting]     = useState(false);
    const [importResult, setImportResult] = useState<{ filesImported: number; repoName: string } | null>(null);

    // ZIP upload
    const [dragOver, setDragOver]           = useState(false);
    const [selectedZip, setSelectedZip]     = useState<File | null>(null);
    const [uploading, setUploading]         = useState(false);
    const [uploadProgress, setUploadProgress] = useState(0);
    const fileInputRef = useRef<HTMLInputElement>(null);

    const selectedProvider = providers.find(p => p.id === provider)!;
    const canImport = !!repoUrl.trim() && !importing;

    const handleProviderChange = (p: Provider) => {
        setProvider(p);
        setTestState('idle');
        setTestError('');
        setRepoInfo(null);
        setImportResult(null);
    };

    const handleUrlChange = (v: string) => {
        setRepoUrl(v);
        setTestState('idle');
        setTestError('');
        setRepoInfo(null);
        setImportResult(null);
    };

    const handleTestConnection = async () => {
        if (!repoUrl.trim()) return;
        setTestState('testing');
        setTestError('');
        setRepoInfo(null);
        try {
            const info = await importApi.gitTest({
                repoUrl: repoUrl.trim(),
                branch: branch || 'main',
                token: token || undefined,
            });
            setRepoInfo(info);
            // Auto-fill default branch if user left it as 'main' and repo differs
            if (branch === 'main' && info.defaultBranch && info.defaultBranch !== 'main') {
                setBranch(info.defaultBranch);
            }
            setTestState('ok');
        } catch (err: any) {
            setTestState('error');
            setTestError(err.message || 'Connection test failed');
        }
    };

    const handleImport = async () => {
        if (!canImport) return;
        if (!selectedProject) {
            addToast({ type: 'error', title: 'No Project', message: 'Open a project before importing.' });
            return;
        }
        setImporting(true);
        setImportResult(null);
        try {
            const result = await importApi.git({
                repoUrl: repoUrl.trim(),
                projectId: selectedProject.id,
                branch: branch || 'main',
                provider,
                token: token || undefined,
                subPath: subPath || undefined,
            });
            resetProjectTiming(selectedProject.id, result.importStartedAt);
            await refreshFiles(selectedProject.id, true);
            setImportResult({ filesImported: result.filesImported, repoName: result.repoName });
            addToast({
                type: 'success',
                title: 'Import Complete',
                message: `${result.filesImported} files imported from ${result.repoName}`,
            });
            setTimeout(() => onClose(true), 1200);
        } catch (err: any) {
            addToast({ type: 'error', title: 'Import Failed', message: err.message || 'Could not import repository.' });
        } finally {
            setImporting(false);
        }
    };

    const handleDrop = (e: React.DragEvent) => {
        e.preventDefault();
        setDragOver(false);
        const file = e.dataTransfer.files[0];
        if (file && (file.name.endsWith('.zip') || file.name.endsWith('.jar'))) {
            setSelectedZip(file);
            setUploadProgress(0);
        } else {
            addToast({ type: 'error', title: 'Invalid File', message: 'Please upload a .zip or .jar file' });
        }
    };

    /**
     * Upload with XHR to get real onprogress events instead of blocking axios.
     * Upload phase 0-80%, server extraction simulation 80-95%, complete 100%.
     */
    const handleUpload = async () => {
        if (!selectedZip) return;
        if (!selectedProject) {
            addToast({ type: 'error', title: 'No Project', message: 'Open a project before importing.' });
            return;
        }
        setUploading(true);
        setUploadProgress(0);

        try {
            const result = await new Promise<{ filesExtracted: number; importStartedAt: string }>((resolve, reject) => {
                const xhr = new XMLHttpRequest();
                const formData = new FormData();
                formData.append('file', selectedZip);
                formData.append('projectId', selectedProject.id);

                // Real upload progress: 0-80%
                xhr.upload.addEventListener('progress', (e) => {
                    if (e.lengthComputable) {
                        setUploadProgress(Math.round((e.loaded / e.total) * 80));
                    }
                });

                // Simulate server-side extraction: 80% -> 95%
                let extractionPct = 80;
                const extractionTimer = setInterval(() => {
                    extractionPct = Math.min(95, extractionPct + 3);
                    setUploadProgress(extractionPct);
                }, 400);

                xhr.addEventListener('load', () => {
                    clearInterval(extractionTimer);
                    if (xhr.status >= 200 && xhr.status < 300) {
                        setUploadProgress(100);
                        try { resolve(JSON.parse(xhr.responseText)); }
                        catch { reject(new Error('Invalid response from server')); }
                    } else {
                        try {
                            const data = JSON.parse(xhr.responseText);
                            reject(new Error(data?.error || `Upload failed (${xhr.status})`));
                        } catch {
                            reject(new Error(`Upload failed (${xhr.status})`));
                        }
                    }
                });

                xhr.addEventListener('error', () => { clearInterval(extractionTimer); reject(new Error('Network error during upload')); });
                xhr.addEventListener('timeout', () => { clearInterval(extractionTimer); reject(new Error('Upload timed out')); });

                xhr.open('POST', '/api/import/zip');
                xhr.timeout = 120_000; // 2 min for large archives
                xhr.send(formData);
            });

            resetProjectTiming(selectedProject.id, result.importStartedAt);
            await refreshFiles(selectedProject.id, true);
            addToast({ type: 'success', title: 'Upload Complete', message: `Imported ${result.filesExtracted} files from ${selectedZip.name}` });
            onClose(true);
        } catch (err: any) {
            addToast({ type: 'error', title: 'Upload Failed', message: err.message || 'Could not process the ZIP file.' });
            setUploadProgress(0);
        } finally {
            setUploading(false);
        }
    };

    return (
        <div className="fixed inset-0 bg-black/30 backdrop-blur-sm z-50 flex items-center justify-center p-4">
            <div className="bg-white dark:bg-gray-950 rounded-2xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col animate-fade-in">
                {/* Header */}
                <div className="flex items-center justify-between px-6 py-4 border-b border-gray-100 dark:border-gray-800">
                    <div>
                        <h2 className="text-lg font-semibold text-gray-900 dark:text-gray-100">Import Source Code</h2>
                        <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">Import MuleSoft project from a Git repository or ZIP file</p>
                    </div>
                    <button onClick={() => onClose()} className="p-1.5 hover:bg-gray-100 rounded-lg transition-colors">
                        <XMarkIcon className="h-5 w-5 text-gray-400" />
                    </button>
                </div>

                {/* Tabs */}
                <div className="flex border-b border-gray-100 dark:border-gray-800">
                    <button onClick={() => setActiveTab('git')}
                        className={`flex-1 flex items-center justify-center gap-2 py-3 text-sm font-medium transition-colors ${activeTab === 'git' ? 'text-primary-700 border-b-2 border-primary-600' : 'text-gray-500 dark:text-gray-400 hover:text-gray-700'}`}>
                        <LinkIcon className="h-4 w-4" /> Git Repository
                    </button>
                    <button onClick={() => setActiveTab('upload')}
                        className={`flex-1 flex items-center justify-center gap-2 py-3 text-sm font-medium transition-colors ${activeTab === 'upload' ? 'text-primary-700 border-b-2 border-primary-600' : 'text-gray-500 dark:text-gray-400 hover:text-gray-700'}`}>
                        <DocumentArrowUpIcon className="h-4 w-4" /> Upload ZIP / JAR
                    </button>
                </div>

                {/* Content */}
                <div className="flex-1 overflow-y-auto p-6">
                    {activeTab === 'git' ? (
                        <div className="space-y-5">
                            {/* Provider */}
                            <div>
                                <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2 block">Source Provider</label>
                                <div className="grid grid-cols-5 gap-2">
                                    {providers.map(p => (
                                        <button key={p.id}
                                            onClick={() => handleProviderChange(p.id)}
                                            className={`flex flex-col items-center gap-1 p-2.5 rounded-xl border-2 transition-all ${
                                                provider === p.id
                                                    ? 'border-primary-500 bg-primary-50'
                                                    : 'border-gray-200 dark:border-gray-800 hover:border-gray-300'
                                            }`}>
                                            <span className={provider === p.id ? 'text-primary-600 dark:text-primary-400' : 'text-gray-500 dark:text-gray-400'}>{p.icon}</span>
                                            <span className="text-[10px] font-medium text-gray-700 dark:text-gray-300">{p.label}</span>
                                        </button>
                                    ))}
                                </div>
                            </div>

                            {/* URL + Test */}
                            <div>
                                <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 block">Repository URL</label>
                                <div className="relative">
                                    <input
                                        type="text"
                                        value={repoUrl}
                                        onChange={e => handleUrlChange(e.target.value)}
                                        placeholder={selectedProvider.placeholder}
                                        className="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none font-mono pr-16"
                                    />
                                    <button
                                        onClick={handleTestConnection}
                                        disabled={!repoUrl.trim() || testState === 'testing'}
                                        className="absolute right-1.5 top-1.5 px-3 py-1 text-xs font-medium bg-gray-100 hover:bg-gray-200 text-gray-600 rounded-md transition-colors disabled:opacity-40"
                                    >
                                        {testState === 'testing'
                                            ? <ArrowPathIcon className="h-3.5 w-3.5 animate-spin" />
                                            : 'Test'}
                                    </button>
                                </div>

                                {/* Test result */}
                                {testState === 'ok' && repoInfo && (
                                    <div className="mt-2 p-3 bg-success-50 rounded-lg border border-success-200 text-xs space-y-1">
                                        <div className="flex items-center gap-2">
                                            <CheckCircleIcon className="h-4 w-4 text-success-600 shrink-0" />
                                            <span className="font-semibold text-success-800">{repoInfo.name}</span>
                                            {repoInfo.isPrivate
                                                ? <span className="flex items-center gap-0.5 text-gray-500"><LockClosedIcon className="h-3 w-3" /> Private</span>
                                                : <span className="flex items-center gap-0.5 text-success-600"><GlobeAltIcon className="h-3 w-3" /> Public</span>}
                                        </div>
                                        <div className="flex items-center gap-4 text-gray-500 pl-6">
                                            <span>Branch: <strong className="text-gray-700">{repoInfo.defaultBranch}</strong></span>
                                            <span>MuleSoft files found: <strong className="text-gray-700">{repoInfo.filesFound}</strong></span>
                                            {repoInfo.stars !== undefined && (
                                                <span className="flex items-center gap-1">
                                                    <StarIcon className="h-3 w-3" /> {repoInfo.stars}
                                                </span>
                                            )}
                                        </div>
                                        {repoInfo.description && (
                                            <p className="pl-6 text-gray-500 truncate">{repoInfo.description}</p>
                                        )}
                                    </div>
                                )}
                                {testState === 'error' && (
                                    <div className="mt-2 flex items-start gap-2 p-2.5 bg-error-50 rounded-lg border border-error-200 text-xs">
                                        <ExclamationTriangleIcon className="h-4 w-4 text-error-600 shrink-0 mt-0.5" />
                                        <span className="text-error-700">{testError}</span>
                                    </div>
                                )}
                            </div>

                            {/* Branch + Token */}
                            <div className="grid grid-cols-2 gap-3">
                                <div>
                                    <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 block">Branch</label>
                                    <input
                                        type="text"
                                        value={branch}
                                        onChange={e => setBranch(e.target.value)}
                                        className="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none"
                                    />
                                </div>
                                <div>
                                    <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 flex items-center gap-1.5">
                                        <LockClosedIcon className="h-3 w-3" /> Access Token
                                        <span className="ml-auto text-[10px] font-normal text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded">Optional &mdash; public repos only</span>
                                    </label>
                                    <input
                                        type="password"
                                        value={token}
                                        onChange={e => setToken(e.target.value)}
                                        placeholder="ghp_xxxx  (leave blank for public repos)"
                                        className="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none font-mono"
                                    />
                                </div>
                            </div>

                            {/* Sub-path */}
                            <div>
                                <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5 block">Sub-path <span className="font-normal text-gray-400">(optional)</span></label>
                                <input
                                    type="text"
                                    value={subPath}
                                    onChange={e => setSubPath(e.target.value)}
                                    placeholder="e.g. src/main/mule  (leave blank for entire repo)"
                                    className="w-full px-4 py-2.5 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none font-mono"
                                />
                            </div>

                            {/* Import status */}
                            {importing && (
                                <div className="flex items-center gap-2 text-sm text-primary-600">
                                    <ArrowPathIcon className="h-4 w-4 animate-spin" />
                                    Fetching repository tree and downloading files...
                                </div>
                            )}
                            {importResult && (
                                <div className="flex items-center gap-2 p-3 bg-success-50 rounded-lg border border-success-200 text-sm text-success-700">
                                    <CheckCircleIcon className="h-5 w-5 shrink-0" />
                                    <span>Imported <strong>{importResult.filesImported}</strong> files from <strong>{importResult.repoName}</strong></span>
                                </div>
                            )}
                        </div>
                    ) : (
                        <div className="space-y-5">
                            {/* Drop Zone */}
                            <div
                                onDragOver={e => { e.preventDefault(); setDragOver(true); }}
                                onDragLeave={() => setDragOver(false)}
                                onDrop={handleDrop}
                                onClick={() => !selectedZip && !uploading && fileInputRef.current?.click()}
                                className={`border-2 border-dashed rounded-xl p-10 text-center transition-colors ${
                                    dragOver
                                        ? 'border-primary-400 bg-primary-50'
                                        : selectedZip
                                            ? 'border-success-300 bg-success-50'
                                            : 'border-gray-300 hover:border-primary-300 cursor-pointer'
                                }`}>
                                {selectedZip ? (
                                    <div className="space-y-2">
                                        <CheckCircleIcon className="h-10 w-10 text-success-500 mx-auto" />
                                        <p className="font-medium text-gray-800 dark:text-gray-200">{selectedZip.name}</p>
                                        <p className="text-xs text-gray-500">{(selectedZip.size / (1024 * 1024)).toFixed(2)} MB</p>
                                        {!uploading && (
                                            <button
                                                onClick={e => { e.stopPropagation(); setSelectedZip(null); setUploadProgress(0); }}
                                                className="text-xs text-error-500 hover:text-error-600 transition-colors">
                                                Remove
                                            </button>
                                        )}
                                    </div>
                                ) : (
                                    <div className="space-y-3">
                                        <DocumentArrowUpIcon className="h-10 w-10 text-gray-300 mx-auto" />
                                        <p className="text-sm text-gray-600 font-medium">Drop your MuleSoft project here</p>
                                        <p className="text-xs text-gray-400">Supports .zip and .jar files up to 100 MB</p>
                                        <label
                                            onClick={e => e.stopPropagation()}
                                            className="inline-flex items-center gap-2 px-4 py-2 bg-primary-600 hover:bg-primary-700 text-white text-sm font-medium rounded-lg cursor-pointer transition-colors"
                                        >
                                            Browse Files
                                            <input
                                                ref={fileInputRef}
                                                type="file"
                                                accept=".zip,.jar"
                                                className="hidden"
                                                onChange={e => {
                                                    const f = e.target.files?.[0];
                                                    if (f) { setSelectedZip(f); setUploadProgress(0); }
                                                }}
                                            />
                                        </label>
                                    </div>
                                )}
                            </div>

                            {/* Real-time upload progress bar */}
                            {uploading && (
                                <div className="space-y-2">
                                    <div className="flex items-center justify-between text-xs text-gray-500">
                                        <span className="flex items-center gap-1.5">
                                            <ArrowPathIcon className="h-3.5 w-3.5 animate-spin" />
                                            {uploadProgress < 80 ? 'Uploading file...' : 'Extracting files...'}
                                        </span>
                                        <span className="font-medium tabular-nums text-gray-700">{uploadProgress}%</span>
                                    </div>
                                    <div className="w-full h-2 bg-gray-200 rounded-full overflow-hidden">
                                        <div
                                            className="h-full bg-primary-500 rounded-full transition-all duration-300 ease-out"
                                            style={{ width: `${uploadProgress}%` }}
                                        />
                                    </div>
                                </div>
                            )}

                            {/* Supported Formats — using SVG icons, no emoji */}
                            <div className="bg-gray-50 dark:bg-gray-900 rounded-xl p-4">
                                <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">Supported Formats</h4>
                                <div className="grid grid-cols-2 gap-2">
                                    {SUPPORTED_FORMATS.map(({ icon, label }) => (
                                        <div key={label} className="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-400">
                                            {icon}
                                            <span>{label}</span>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    )}
                </div>

                {/* Footer */}
                <div className="px-6 py-4 border-t border-gray-100 dark:border-gray-800 flex items-center justify-between gap-2 bg-gray-50/50">
                    <p className="text-xs text-gray-400">
                        {activeTab === 'git'
                            ? 'No token needed for public repositories'
                            : 'ZIP and JAR files are extracted server-side'}
                    </p>
                    <div className="flex items-center gap-2">
                        <button onClick={() => onClose()} className="px-4 py-2 text-sm font-medium text-gray-600 hover:bg-gray-100 rounded-lg transition-colors">
                            Cancel
                        </button>
                        {activeTab === 'git' ? (
                            <button
                                onClick={handleImport}
                                disabled={!canImport}
                                className="flex items-center gap-2 px-5 py-2.5 bg-primary-600 hover:bg-primary-700 disabled:bg-gray-300 text-white text-sm font-medium rounded-lg transition-colors shadow-sm"
                            >
                                {importing
                                    ? <><ArrowPathIcon className="h-4 w-4 animate-spin" /> Importing...</>
                                    : <><FolderIcon className="h-4 w-4" /> Import Repository</>}
                            </button>
                        ) : (
                            <button
                                onClick={handleUpload}
                                disabled={uploading || !selectedZip}
                                className="flex items-center gap-2 px-5 py-2.5 bg-primary-600 hover:bg-primary-700 disabled:bg-gray-300 text-white text-sm font-medium rounded-lg transition-colors shadow-sm"
                            >
                                {uploading
                                    ? <><ArrowPathIcon className="h-4 w-4 animate-spin" /> Processing...</>
                                    : <><DocumentArrowUpIcon className="h-4 w-4" /> Upload &amp; Import</>}
                            </button>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
