'use client';

import React from 'react';
import Editor from '@monaco-editor/react';
import { ProjectFile } from '@/lib/types';
import MarkdownViewer from './MarkdownViewer';
import {
    ClipboardDocumentIcon, ArrowDownTrayIcon,
    LockClosedIcon, CodeBracketIcon, EyeIcon,
    ClockIcon
} from '@heroicons/react/24/outline';
import MigrationHistory from './MigrationHistory';

const languageMap: Record<string, string> = {
    xml: 'xml', json: 'json', yaml: 'yaml', raml: 'yaml',
    js: 'javascript', ts: 'typescript', md: 'markdown',
    properties: 'ini', dwl: 'javascript', env: 'ini',
    py: 'python',
};

function getLanguage(file: ProjectFile): string {
    const ext = (file.name.split('.').pop() || '').toLowerCase();
    return languageMap[ext] || file.language || 'plaintext';
}

interface CodeEditorProps {
    file: ProjectFile | null;
    mode: 'source' | 'migrated';
    onContentChange?: (content: string) => void;
    readOnly?: boolean;
}

const CodeEditor = React.memo(({ file, mode, onContentChange, readOnly = false }: CodeEditorProps) => {
    const [viewMode, setViewMode] = React.useState<'preview' | 'raw'>('preview');
    const [selectedMigrationId, setSelectedMigrationId] = React.useState<string | null>(null);
    const [showHistory, setShowHistory] = React.useState(false);
    const historyRef = React.useRef<HTMLDivElement>(null);

    // Reset selected migration when file changes
    React.useEffect(() => {
        setSelectedMigrationId(null);
        setShowHistory(false);
    }, [file?.id]);

    // Close history dropdown on outside click
    React.useEffect(() => {
        const handler = (e: MouseEvent) => {
            if (historyRef.current && !historyRef.current.contains(e.target as Node)) {
                setShowHistory(false);
            }
        };
        document.addEventListener('mousedown', handler);
        return () => document.removeEventListener('mousedown', handler);
    }, []);

    if (!file) {
        return (
            <div className="h-full flex items-center justify-center bg-gray-50">
                <div className="text-center select-none">
                    <p className="text-gray-400 text-sm">Select a file to view its code</p>
                    <p className="text-gray-300 text-xs mt-1">Click any file in the source or migrated tree</p>
                </div>
            </div>
        );
    }

    const activeMigration = (file.migrations || []).find(m => m.id === (selectedMigrationId || file.activeMigrationId));

    const content = mode === 'migrated'
        ? (viewMode === 'raw'
            ? (activeMigration?.code || file.migratedCode || activeMigration?.content || file.migratedContent || '// No code extracted yet')
            : (activeMigration?.content || file.migratedContent || '// No migrated content yet'))
        : file.content;

    const lang = getLanguage(file);
    const lineCount = content.split('\n').length;

    const handleCopy = () => navigator.clipboard.writeText(content);

    const handleDownload = () => {
        const ext = mode === 'migrated'
            ? ({ '.xml': '.js', '.dwl': '.js', '.raml': '.yaml', '.properties': '.env' }[file.name.match(/\.\w+$/)?.[0] || ''] || '.txt')
            : (file.name.match(/\.\w+$/)?.[0] || '.txt');
        const newName = mode === 'migrated' ? file.name.replace(/\.\w+$/, ext) : file.name;
        const blob = new Blob([content], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url; a.download = newName;
        document.body.appendChild(a); a.click();
        document.body.removeChild(a); URL.revokeObjectURL(url);
    };

    return (
        <div className="h-full flex flex-col overflow-hidden bg-white dark:bg-gray-950">

            {/* ── Toolbar (Glass Refined) ── */}
            <div className="glass-header flex items-center justify-between px-4 py-2 shrink-0">
                <div className="flex items-center gap-3 text-[11px] min-w-0">
                    <div className="flex items-center gap-2">
                        <div className="p-1.5 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-400">
                            <CodeBracketIcon className="h-3.5 w-3.5" />
                        </div>
                        <span className="font-bold text-gray-800 dark:text-gray-200 truncate max-w-[200px]">{file.name}</span>
                    </div>

                    <span className="text-gray-300 dark:text-gray-700">|</span>

                    <div className="flex items-center gap-3 text-gray-500 dark:text-gray-400 font-semibold tracking-tight">
                        <span className="uppercase tracking-widest text-[9px] text-gray-400">Type</span>
                        <span className="capitalize">{lang}</span>
                        <span className="text-gray-300 dark:text-gray-700">·</span>
                        <span className="tabular-nums">{lineCount} lines</span>
                    </div>

                    {mode === 'migrated' && (
                        <>
                            <span className="text-gray-300 dark:text-gray-700">|</span>
                            <span className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase tracking-widest ${file.status === 'completed' ? 'bg-emerald-50 text-emerald-600 border border-emerald-100/50' :
                                file.status === 'failed' ? 'bg-rose-50 text-rose-600 border border-rose-100/50' :
                                    'bg-gray-100 text-gray-400 border border-gray-200/50'
                                }`}>
                                <div className={`w-1 h-1 rounded-full ${file.status === 'completed' ? 'bg-emerald-500' :
                                    file.status === 'failed' ? 'bg-rose-500' : 'bg-gray-400'
                                    }`} />
                                {file.status === 'completed' ? 'Migrated' : file.status === 'failed' ? 'Failed' : 'Pending'}
                            </span>
                        </>
                    )}

                    {mode === 'migrated' && file.migrations && file.migrations.length > 1 && (
                        <div className="relative" ref={historyRef}>
                            <button
                                onClick={() => setShowHistory(!showHistory)}
                                className={`flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-[10px] font-bold transition-all ${showHistory ? 'bg-primary-50 text-primary-700 border border-primary-100' : 'bg-gray-50 text-gray-500 hover:bg-white hover:shadow-sm border border-transparent hover:border-gray-200'
                                    }`}
                                title="View Migration History"
                            >
                                <ClockIcon className="h-3.5 w-3.5" />
                                {selectedMigrationId ? `V${file.migrations.findIndex(m => m.id === selectedMigrationId) + 1}` : 'Latest'}
                            </button>

                            {showHistory && (
                                <div className="glass-card absolute top-full left-0 mt-2 w-72 z-50 overflow-hidden animate-fade-in translate-y-0">
                                    <div className="px-4 py-3 border-b border-gray-100 dark:border-gray-800/50">
                                        <p className="text-[10px] font-black text-gray-400 uppercase tracking-widest">Version Repository</p>
                                    </div>
                                    <MigrationHistory
                                        migrations={file.migrations}
                                        activeId={selectedMigrationId || file.activeMigrationId}
                                        onSelect={(m) => {
                                            setSelectedMigrationId(m.id);
                                            setShowHistory(false);
                                        }}
                                    />
                                    {selectedMigrationId && (
                                        <div className="p-3 border-t border-gray-100 dark:border-gray-800/50 bg-gray-50/30">
                                            <button
                                                onClick={() => setSelectedMigrationId(null)}
                                                className="w-full py-1.5 text-[10px] text-primary-600 hover:text-primary-700 font-black uppercase tracking-widest"
                                            >
                                                Back to Latest Snapshot
                                            </button>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    )}
                </div>

                <div className="flex items-center gap-2 shrink-0">
                    {mode === 'migrated' && (
                        <div className="flex items-center gap-1 p-1 bg-gray-100 dark:bg-gray-800 rounded-lg">
                            <button onClick={() => setViewMode('preview')}
                                className={`p-1.5 rounded-md transition-all ${viewMode === 'preview' ? 'text-primary-600 bg-white dark:bg-gray-700 shadow-sm' : 'text-gray-400 hover:text-gray-600'}`} title="Preview Report">
                                <EyeIcon className="h-4 w-4" />
                            </button>
                            <button onClick={() => setViewMode('raw')}
                                className={`p-1.5 rounded-md transition-all ${viewMode === 'raw' ? 'text-primary-600 bg-white dark:bg-gray-700 shadow-sm' : 'text-gray-400 hover:text-gray-600'}`} title="Raw Markdown">
                                <CodeBracketIcon className="h-4 w-4" />
                            </button>
                        </div>
                    )}

                    <div className="flex items-center gap-1 border-l border-gray-200 dark:border-gray-800 ml-1 pl-2">
                        <button onClick={handleCopy}
                            className="p-1.5 text-gray-400 hover:text-primary-600 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition-all" title="Copy to clipboard">
                            <ClipboardDocumentIcon className="h-4 w-4" />
                        </button>
                        <button onClick={handleDownload}
                            className="p-1.5 text-gray-400 hover:text-primary-600 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition-all" title="Download file">
                            <ArrowDownTrayIcon className="h-4 w-4" />
                        </button>
                    </div>

                    {(readOnly || mode === 'source') && (
                        <div className="flex items-center gap-1.5 px-2 py-1 bg-amber-50 dark:bg-amber-900/10 rounded-lg border border-amber-100/50 dark:border-amber-900/30 ml-2">
                            <LockClosedIcon className="h-3 w-3 text-amber-600" />
                            <span className="text-[9px] font-black text-amber-600 uppercase tracking-widest">Locked</span>
                        </div>
                    )}
                </div>
            </div>

            {/* ── Visualizer or Monaco Editor ── */}
            <div className="flex-1 overflow-hidden relative border-b border-gray-100 dark:border-gray-800">
                {mode === 'migrated' && viewMode === 'preview' ? (
                    <MarkdownViewer content={content} />
                ) : (
                    <Editor
                        height="100%"
                        language={lang}
                        value={content}
                        onChange={(val) => onContentChange?.(val || '')}
                        theme="vs"
                        options={{
                            readOnly: readOnly || mode === 'source',
                            fontSize: 12,
                            lineNumbers: 'on',
                            roundedSelection: false,
                            scrollBeyondLastLine: false,
                            automaticLayout: true,
                            minimap: { enabled: false },
                            padding: { top: 12, bottom: 12 },
                            folding: true,
                            wordWrap: 'on',
                            fontFamily: "'JetBrains Mono', 'Fira Code', 'Menlo', 'Monaco', 'Courier New', monospace",
                            renderLineHighlight: 'all',
                            overviewRulerBorder: false,
                            scrollbar: {
                                verticalScrollbarSize: 10,
                                horizontalScrollbarSize: 10,
                            }
                        }}
                    />
                )}
            </div>
        </div>
    );
});

CodeEditor.displayName = 'CodeEditor';

export default CodeEditor;
