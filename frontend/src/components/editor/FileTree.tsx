'use client';

import React, { useState, useMemo, useCallback, useRef, useEffect } from 'react';
import { useVirtualizer } from '@tanstack/react-virtual';
import { useApp } from '@/contexts/AppContext';
import { ProjectFile, TargetRuntime } from '@/lib/types';
import { useDebounce } from '@/lib/hooks';
import {
    FolderIcon, FolderOpenIcon,
    MagnifyingGlassIcon, ChevronRightIcon, ChevronDownIcon,
    CheckCircleIcon, ExclamationCircleIcon, ClockIcon,
    DocumentIcon, DocumentTextIcon, CodeBracketIcon,
    CommandLineIcon, DocumentDuplicateIcon,
} from '@heroicons/react/24/outline';

const statusIcons: Record<string, { icon: React.ElementType; color: string }> = {
    pending: { icon: ClockIcon, color: 'text-gray-400' },
    'in-progress': { icon: () => <div className="w-3 h-3 border-2 border-primary-500 border-t-transparent rounded-full animate-spin" />, color: 'text-primary-500' },
    completed: { icon: CheckCircleIcon, color: 'text-success-500' },
    failed: { icon: ExclamationCircleIcon, color: 'text-error-500' },
};

const sourceLangIcons: Record<string, React.ElementType> = {
    xml: DocumentIcon,
    json: DocumentTextIcon,
    yaml: CodeBracketIcon,
    plaintext: DocumentTextIcon,
    raml: CommandLineIcon,
    dwl: DocumentDuplicateIcon,
};

/* ─── Target-runtime naming conventions ───────────────────────────────────
   Extension and folder name maps keyed by TargetRuntime.
   Filenames are transformed to the canonical casing for each runtime.
   ──────────────────────────────────────────────────────────────────────── */
const EXT_MAP: Record<TargetRuntime, Record<string, string>> = {
    nodejs:    { '.xml': '.js',   '.dwl': '.js',     '.raml': '.yaml', '.properties': '.env',        '.json': '.json' },
    python:    { '.xml': '.py',   '.dwl': '.py',     '.raml': '.yaml', '.properties': '.env',        '.json': '.json' },
    java:      { '.xml': '.java', '.dwl': '.java',   '.raml': '.yaml', '.properties': '.properties', '.json': '.json' },
    groovy:    { '.xml': '.iflw', '.dwl': '.groovy', '.raml': '.edmx', '.properties': '.prop',       '.json': '.json' },
    "cpi-xml": { '.xml': '.iflw', '.dwl': '.xml',    '.raml': '.edmx', '.properties': '.prop',       '.json': '.json' },
    xslt:      { '.xml': '.iflw', '.dwl': '.xsl',    '.raml': '.edmx', '.properties': '.prop',       '.json': '.json' },
};

const FOLDER_MAP: Record<TargetRuntime, Record<string, string>> = {
    nodejs:    { mule: 'handlers',  dwl: 'transforms', flows: 'routes',    api: 'api',         resources: 'config' },
    python:    { mule: 'lambdas',   dwl: 'transforms', flows: 'functions', api: 'api',         resources: 'config' },
    java:      { mule: 'services',  dwl: 'processors', flows: 'flows',     api: 'controllers', resources: 'config' },
    groovy:    { mule: 'src/main/resources/scenarioflows/integrationflow', dwl: 'src/main/resources/script', flows: 'src/main/resources/scenarioflows/integrationflow', api: 'src/main/resources/edmx', resources: 'src/main/resources/parameters' },
    "cpi-xml": { mule: 'src/main/resources/scenarioflows/integrationflow', dwl: 'src/main/resources/mapping', flows: 'src/main/resources/scenarioflows/integrationflow', api: 'src/main/resources/edmx', resources: 'src/main/resources/parameters' },
    xslt:      { mule: 'src/main/resources/scenarioflows/integrationflow', dwl: 'src/main/resources/mapping', flows: 'src/main/resources/scenarioflows/integrationflow', api: 'src/main/resources/edmx', resources: 'src/main/resources/parameters' },
};

/** Convert a stem to the canonical naming style for the target runtime. */
function applyNamingConvention(stem: string, runtime: TargetRuntime): string {
    // Normalise: split on -, _, spaces, dots and camel-case boundaries
    const words = stem
        .replace(/([a-z])([A-Z])/g, '$1 $2')   // camelCase → words
        .split(/[\s\-_.]+/)
        .filter(Boolean)
        .map(w => w.toLowerCase());

    if (!words.length) return stem;

    if (runtime === 'java' || runtime === 'groovy') {
        // PascalCase
        return words.map(w => w[0].toUpperCase() + w.slice(1)).join('');
    }
    if (runtime === 'python') {
        // snake_case
        return words.join('_');
    }
    // nodejs, cpi-xml, xslt → kebab-case
    return words.join('-');
}

interface FileTreeProps {
    onSelectFile: (file: ProjectFile) => void;
    selectedFileId: string | null;
    projectId: string;
    mode: 'source' | 'migrated';
    title: string;
    accent?: string;
}

const FileTree = React.memo(({ onSelectFile, selectedFileId, projectId, mode, title, accent = 'primary' }: FileTreeProps) => {
    const { files, projects } = useApp();
    const [expandedFolders, setExpandedFolders] = useState<Set<string>>(new Set());
    const [search, setSearch] = useState('');
    const debouncedSearch = useDebounce(search, 180);
    const treeRef = useRef<HTMLDivElement | null>(null);

    // Resolve the project once; fall back to nodejs if not found
    const targetRuntime: TargetRuntime =
        (projects.find(p => p.id === projectId)?.targetRuntime as TargetRuntime) ?? 'nodejs';

    const toggleFolder = useCallback((id: string) => {
        setExpandedFolders(prev => {
            const next = new Set(prev);
            next.has(id) ? next.delete(id) : next.add(id);
            return next;
        });
    }, []);

    const projectFiles = useMemo(() => files.filter(f => f.projectId === projectId), [files, projectId]);

    // Auto-expand every folder as soon as files are loaded so the tree matches
    // the source repo structure out-of-the-box. Users can collapse manually.
    const folderIds = useMemo(
        () => new Set(projectFiles.filter(f => f.type === 'folder').map(f => f.id)),
        [projectFiles]
    );
    React.useEffect(() => {
        if (folderIds.size === 0) return;
        setExpandedFolders(prev => {
            const next = new Set(prev);
            folderIds.forEach(id => next.add(id));
            return next;
        });
    }, [folderIds]);

    const rootNodes = useMemo(() => {
        const childIds = new Set(projectFiles.flatMap(f => f.children));
        // Preserve the original path-based insertion order from the git tree traversal;
        // do NOT re-sort here — sorting happens to match the source repo structure.
        return projectFiles.filter(f => !childIds.has(f.id));
    }, [projectFiles]);

    const matchesSearch = (file: ProjectFile): boolean => {
        if (!debouncedSearch) return true;
        const q = debouncedSearch.toLowerCase();
        if (file.name.toLowerCase().includes(q)) return true;
        if (file.type === 'folder') {
            return projectFiles.filter(f => file.children.includes(f.id)).some(matchesSearch);
        }
        return false;
    };

    const getFileCount = (folder: ProjectFile): { total: number; completed: number } => {
        let total = 0, completed = 0;
        const walk = (f: ProjectFile) => {
            if (f.type === 'file') { total++; if (f.status === 'completed') completed++; }
            f.children.forEach(cid => { const c = projectFiles.find(x => x.id === cid); if (c) walk(c); });
        };
        walk(folder);
        return { total, completed };
    };

    const getDisplayName = (file: ProjectFile): string => {
        if (mode === 'source') return file.name;

        if (file.type === 'folder') {
            return FOLDER_MAP[targetRuntime][file.name.toLowerCase()] ?? file.name;
        }

        // Only rename once migration is done
        if (file.status !== 'completed') return file.name;

        const dotIdx = file.name.lastIndexOf('.');
        if (dotIdx === -1) return file.name;

        const stem = file.name.substring(0, dotIdx);
        const ext  = file.name.substring(dotIdx);
        const newExt = EXT_MAP[targetRuntime][ext];
        if (!newExt) return file.name;

        const newStem = applyNamingConvention(stem, targetRuntime);
        return `${newStem}${newExt}`;
    };

    const getFileIcon = (file: ProjectFile): React.ReactNode => {
        if (mode === 'migrated') {
            const isDone = file.status === 'completed';
            return <CodeBracketIcon className={`h-3.5 w-3.5 shrink-0 ${isDone ? 'text-emerald-500' : 'text-gray-300 dark:text-gray-700 opacity-50'}`} />;
        }
        const Icon = sourceLangIcons[file.language] || DocumentIcon;
        return <Icon className="h-3.5 w-3.5 shrink-0 text-gray-400 group-hover:text-primary-500 transition-colors" />;
    };

    const shouldShow = (file: ProjectFile): boolean => {
        // Show everything for both source and migrated trees to provide a consistent "professional" view
        return true;
    };

    const visibleNodes = useMemo(() => {
        const rows: Array<{ file: ProjectFile; depth: number }> = [];
        const walk = (file: ProjectFile, depth = 0) => {
            if (!matchesSearch(file) || !shouldShow(file)) return;
            rows.push({ file, depth });
            if (file.type !== 'folder' || !expandedFolders.has(file.id)) return;
            file.children
                .map(cid => projectFiles.find(x => x.id === cid))
                .filter((x): x is ProjectFile => !!x)
                .forEach(child => walk(child, depth + 1));
        };
        rootNodes.forEach(node => walk(node));
        return rows;
    }, [rootNodes, expandedFolders, projectFiles, debouncedSearch]);

    const rowVirtualizer = useVirtualizer({
        count: visibleNodes.length,
        getScrollElement: () => treeRef.current,
        estimateSize: () => 30,
        overscan: 12,
    });

    const Row = (index: number) => {
        const { file, depth } = visibleNodes[index];
        const isFolder = file.type === 'folder';
        const isExpanded = expandedFolders.has(file.id);
        const isSelected = file.id === selectedFileId;
        const isPendingMigrated = mode === 'migrated' && file.status !== 'completed' && file.type === 'file';
        const accentBg = isSelected
            ? (accent === 'primary' ? 'bg-primary-50 text-primary-700' : 'bg-emerald-50 text-emerald-700')
            : `${isPendingMigrated ? 'text-gray-400 dark:text-gray-600 italic opacity-70' : 'text-gray-700 dark:text-gray-300'} hover:bg-gray-50`;

        return (
            <div className="px-1">
                <div
                    className={`flex items-center gap-1.5 px-2 py-[5px] rounded-md cursor-pointer text-[12px] transition-colors group ${accentBg} ${isSelected ? 'font-medium' : ''}`}
                    style={{ paddingLeft: `${depth * 12 + 6}px` }}
                    onClick={() => isFolder ? toggleFolder(file.id) : onSelectFile(file)}
                >
                    {isFolder ? (
                        <button className="p-0.5" onClick={e => { e.stopPropagation(); toggleFolder(file.id); }}>
                            {isExpanded ? <ChevronDownIcon className="h-3 w-3 text-gray-400" /> : <ChevronRightIcon className="h-3 w-3 text-gray-400" />}
                        </button>
                    ) : <span className="w-4" />}
                    {isFolder ? (isExpanded ? <FolderOpenIcon className="h-3.5 w-3.5 shrink-0 text-amber-500" /> : <FolderIcon className="h-3.5 w-3.5 shrink-0 text-amber-400" />) : getFileIcon(file)}
                    <span className="flex-1 truncate">{getDisplayName(file)}</span>
                    {!isFolder && (() => {
                        const st = statusIcons[file.status]; const Icon = st.icon;
                        return <Icon className={`h-3 w-3 shrink-0 ${st.color}`} />;
                    })()}
                    {isFolder && (() => {
                        const c = getFileCount(file);
                        return c.total > 0 ? <span className="text-[9px] text-gray-400 shrink-0">{c.completed}/{c.total}</span> : null;
                    })()}
                </div>
            </div>
        );
    };

    const fileOnly = projectFiles.filter(f => f.type === 'file');
    const counts = {
        total: fileOnly.length,
        completed: fileOnly.filter(f => f.status === 'completed').length,
        failed: fileOnly.filter(f => f.status === 'failed').length,
        pending: fileOnly.filter(f => f.status === 'pending').length,
    };

    return (
        <div className="flex flex-col h-full bg-white dark:bg-gray-950">
            {/* Header */}
            <div className={`px-3 py-2 border-b border-gray-100 dark:border-gray-800 ${accent === 'primary' ? 'bg-primary-50/30' : 'bg-emerald-50/30'}`}>
                <div className="flex items-center justify-between">
                    <span className={`text-[10px] font-bold uppercase tracking-wider ${accent === 'primary' ? 'text-primary-600' : 'text-emerald-600'}`}>
                        {title}
                    </span>
                    <span className="text-[10px] text-gray-400">
                        {mode === 'source' ? `${counts.total} files` : `${counts.completed} files`}
                    </span>
                </div>
            </div>

            {/* Search */}
            <div className="px-2 py-1.5 border-b border-gray-100 dark:border-gray-800">
                <div className="relative">
                    <MagnifyingGlassIcon className="absolute left-2 top-1/2 -translate-y-1/2 h-3 w-3 text-gray-400" />
                    <input type="text" value={search} onChange={e => setSearch(e.target.value)}
                        placeholder="Search..."
                        className="w-full pl-6 pr-2 py-1 text-[11px] bg-gray-50 border border-gray-200 dark:border-gray-800 rounded focus:ring-1 focus:ring-primary-400 outline-none" />
                </div>
            </div>

            {/* Tree */}
            <div ref={treeRef} className="flex-1 overflow-y-auto scrollbar-thin py-1">
                <div style={{ height: `${rowVirtualizer.getTotalSize()}px`, width: '100%', position: 'relative' }}>
                    {rowVirtualizer.getVirtualItems().map((virtualRow) => (
                        <div
                            key={virtualRow.key}
                            style={{
                                position: 'absolute',
                                top: 0,
                                left: 0,
                                width: '100%',
                                height: `${virtualRow.size}px`,
                                transform: `translateY(${virtualRow.start}px)`,
                            }}
                        >
                            {Row(virtualRow.index)}
                        </div>
                    ))}
                </div>
            </div>

            {/* Stats */}
            <div className="px-2 py-1.5 border-t border-gray-100 dark:border-gray-800 bg-gray-50/50 flex items-center gap-2 text-[9px]">
                <span className="flex items-center gap-0.5 text-success-600"><CheckCircleIcon className="h-2.5 w-2.5" />{counts.completed}</span>
                <span className="flex items-center gap-0.5 text-error-500"><ExclamationCircleIcon className="h-2.5 w-2.5" />{counts.failed}</span>
                <span className="flex items-center gap-0.5 text-gray-400"><ClockIcon className="h-2.5 w-2.5" />{counts.pending}</span>
                <span className="ml-auto text-gray-400">{Math.round((counts.completed / Math.max(counts.total, 1)) * 100)}%</span>
            </div>
        </div>
    );
});
FileTree.displayName = 'FileTree';
export default FileTree;
