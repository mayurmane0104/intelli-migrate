'use client';

import React, { useMemo } from 'react';
import { ProjectFile } from '@/lib/types';
import {
    ArrowsRightLeftIcon, CheckIcon, XMarkIcon,
    ArrowsPointingInIcon, ArrowsPointingOutIcon,
} from '@heroicons/react/24/outline';

interface DiffViewerProps {
    file: ProjectFile | null;
    onAccept?: () => void;
    onReject?: () => void;
}

type DiffLine = {
    type: 'same' | 'added' | 'removed' | 'header';
    lineNum?: number;
    newLineNum?: number;
    content: string;
};

function computeDiff(original: string, migrated: string): DiffLine[] {
    const origLines = original.split('\n');
    const migLines = migrated.split('\n');
    const lines: DiffLine[] = [];
    let oIdx = 0; let mIdx = 0;

    // Simple LCS-based diff
    while (oIdx < origLines.length || mIdx < migLines.length) {
        if (oIdx < origLines.length && mIdx < migLines.length && origLines[oIdx] === migLines[mIdx]) {
            lines.push({ type: 'same', lineNum: oIdx + 1, newLineNum: mIdx + 1, content: origLines[oIdx] });
            oIdx++; mIdx++;
        } else {
            // Find next matching line within a window
            let foundMatch = false;
            for (let ahead = 1; ahead < 15; ahead++) {
                if (mIdx + ahead < migLines.length && oIdx < origLines.length && origLines[oIdx] === migLines[mIdx + ahead]) {
                    // Added lines before the match
                    for (let a = 0; a < ahead; a++) {
                        lines.push({ type: 'added', newLineNum: mIdx + a + 1, content: migLines[mIdx + a] });
                    }
                    mIdx += ahead;
                    foundMatch = true;
                    break;
                }
                if (oIdx + ahead < origLines.length && mIdx < migLines.length && origLines[oIdx + ahead] === migLines[mIdx]) {
                    // Removed lines before the match
                    for (let r = 0; r < ahead; r++) {
                        lines.push({ type: 'removed', lineNum: oIdx + r + 1, content: origLines[oIdx + r] });
                    }
                    oIdx += ahead;
                    foundMatch = true;
                    break;
                }
            }
            if (!foundMatch) {
                if (oIdx < origLines.length) {
                    lines.push({ type: 'removed', lineNum: oIdx + 1, content: origLines[oIdx] });
                    oIdx++;
                }
                if (mIdx < migLines.length) {
                    lines.push({ type: 'added', newLineNum: mIdx + 1, content: migLines[mIdx] });
                    mIdx++;
                }
            }
        }
    }
    return lines;
}

const DiffViewer = React.memo(({ file, onAccept, onReject }: DiffViewerProps) => {
    const [viewMode, setViewMode] = React.useState<'unified' | 'split'>('split');

    const diff = useMemo(() => {
        if (!file || (!file.migratedContent && !file.migratedCode)) return [];
        const target = file.migratedCode || (file.migratedContent.startsWith('<!--metadata:') ? file.migratedContent.split('-->\n')[1] || file.migratedContent : file.migratedContent);
        return computeDiff(file.content, target);
    }, [file]);

    const stats = useMemo(() => {
        const additions = diff.filter(d => d.type === 'added').length;
        const deletions = diff.filter(d => d.type === 'removed').length;
        return { additions, deletions };
    }, [diff]);

    // Group diff into side-by-side pairs
    const splitLines = useMemo(() => {
        const pairs: { left?: DiffLine; right?: DiffLine }[] = [];
        let i = 0;
        while (i < diff.length) {
            const current = diff[i];
            const next = diff[i + 1];

            if (current.type === 'removed' && next?.type === 'added') {
                pairs.push({ left: current, right: next });
                i += 2;
            } else if (current.type === 'removed') {
                pairs.push({ left: current });
                i++;
            } else if (current.type === 'added') {
                pairs.push({ right: current });
                i++;
            } else {
                pairs.push({ left: current, right: current });
                i++;
            }
        }
        return pairs;
    }, [diff]);

    if (!file) {
        return (
            <div className="h-full flex items-center justify-center bg-gray-50/50 dark:bg-gray-950">
                <p className="text-gray-400 text-sm">Select a file to see the diff view</p>
            </div>
        );
    }

    if (!file.migratedContent && !file.migratedCode) {
        return (
            <div className="h-full flex items-center justify-center bg-gray-50/50 dark:bg-gray-950">
                <div className="text-center">
                    <ArrowsRightLeftIcon className="h-8 w-8 text-gray-300 mx-auto mb-2" />
                    <p className="text-gray-500 dark:text-gray-400 text-sm font-medium">No migrated version available</p>
                    <p className="text-gray-400 text-xs mt-1">Run migration on this file to see the diff</p>
                </div>
            </div>
        );
    }

    return (
        <div className="h-full flex flex-col bg-white dark:bg-gray-950 min-h-0 overflow-hidden">
            {/* Toolbar */}
            <div className="flex items-center justify-between px-4 py-2 bg-gray-50/80 dark:bg-gray-900/80 backdrop-blur-md border-b border-gray-200 dark:border-gray-800">
                <div className="flex items-center gap-4 text-xs">
                    <div className="flex items-center gap-1.5 font-mono text-gray-900 dark:text-gray-100 font-semibold">
                        <ArrowsRightLeftIcon className="h-3.5 w-3.5 text-primary-500" />
                        {file.name}
                    </div>
                    <div className="h-4 w-px bg-gray-200 dark:bg-gray-700" />
                    <div className="flex items-center gap-2">
                        <span className="flex items-center gap-1 text-success-600 dark:text-success-400 font-bold bg-success-50/50 dark:bg-success-900/10 px-1.5 py-0.5 rounded">+{stats.additions}</span>
                        <span className="flex items-center gap-1 text-error-600 dark:text-error-400 font-bold bg-error-50/50 dark:bg-error-900/10 px-1.5 py-0.5 rounded">-{stats.deletions}</span>
                    </div>
                    <div className="h-4 w-px bg-gray-200 dark:bg-gray-700" />
                    <div className="flex bg-gray-200/50 dark:bg-gray-800 p-0.5 rounded-lg">
                        <button onClick={() => setViewMode('unified')}
                            className={`px-2 py-1 rounded-md text-[10px] font-bold transition-all ${viewMode === 'unified' ? 'bg-white dark:bg-gray-950 text-primary-600 shadow-sm' : 'text-gray-500 hover:text-gray-700'}`}>
                            Unified
                        </button>
                        <button onClick={() => setViewMode('split')}
                            className={`px-2 py-1 rounded-md text-[10px] font-bold transition-all ${viewMode === 'split' ? 'bg-white dark:bg-gray-950 text-primary-600 shadow-sm' : 'text-gray-500 hover:text-gray-700'}`}>
                            Split
                        </button>
                    </div>
                </div>

                <div className="flex items-center gap-2">
                    {onAccept && onReject && (
                        <>
                            <button onClick={onReject}
                                className="flex items-center gap-1.5 px-3 py-1.5 text-gray-600 dark:text-gray-400 text-xs font-bold hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors">
                                <XMarkIcon className="h-3.5 w-3.5" /> Reject
                            </button>
                            <button onClick={onAccept}
                                className="flex items-center gap-1.5 px-3 py-1.5 bg-success-600 hover:bg-success-700 text-white text-xs font-bold rounded-lg transition-all shadow-sm shadow-success-100 border border-success-500">
                                <CheckIcon className="h-3.5 w-3.5" /> Accept Changes
                            </button>
                        </>
                    )}
                </div>
            </div>

            {/* Diff content */}
            <div className="flex-1 overflow-hidden flex flex-col font-mono text-[12px] leading-relaxed">
                {viewMode === 'unified' ? (
                    <div className="flex-1 overflow-auto">
                        <div className="min-w-full inline-block">
                            {diff.map((line, i) => {
                                const bg = line.type === 'added' ? 'bg-success-50/40 dark:bg-success-900/10' : line.type === 'removed' ? 'bg-error-50/40 dark:bg-error-900/10' : '';
                                const textColor = line.type === 'added' ? 'text-success-700 dark:text-success-400' : line.type === 'removed' ? 'text-error-700 dark:text-error-400' : 'text-gray-700 dark:text-gray-300';
                                const prefix = line.type === 'added' ? '+' : line.type === 'removed' ? '-' : ' ';

                                return (
                                    <div key={i} className={`flex border-l-4 ${line.type === 'added' ? 'border-success-500' : line.type === 'removed' ? 'border-error-500' : 'border-transparent'} ${bg} hover:brightness-105 transition-all`}>
                                        <div className="w-20 flex bg-gray-50/50 dark:bg-gray-900/50 text-gray-400 select-none text-[10px] shrink-0">
                                            <span className="w-10 text-right pr-2 border-r border-gray-100 dark:border-gray-800">{line.lineNum || ''}</span>
                                            <span className="w-10 text-right pr-2">{line.newLineNum || ''}</span>
                                        </div>
                                        <span className={`w-6 text-center select-none font-bold opacity-50 shrink-0 ${textColor}`}>{prefix}</span>
                                        <span className={`flex-1 px-2 whitespace-pre ${textColor}`}>{line.content}</span>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                ) : (
                    <div className="flex-1 overflow-y-auto overflow-x-hidden">
                        <div className="w-full grid grid-cols-2 divide-x divide-gray-200 dark:divide-gray-800 border-b border-gray-100 dark:border-gray-800">
                            {/* Header */}
                            <div className="sticky top-0 bg-gray-50/50 dark:bg-gray-900/50 backdrop-blur px-4 py-1 text-[10px] font-bold text-gray-400 uppercase tracking-widest border-b border-gray-200 dark:border-gray-800 flex justify-between z-10">
                                <span>MuleSoft Source</span>
                                <ArrowsPointingInIcon className="h-3 w-3" />
                            </div>
                            <div className="sticky top-0 bg-gray-50/50 dark:bg-gray-900/50 backdrop-blur px-4 py-1 text-[10px] font-bold text-primary-500 uppercase tracking-widest border-b border-gray-200 dark:border-gray-800 flex justify-between z-10">
                                <span>AWS Lambda Output</span>
                                <ArrowsPointingOutIcon className="h-3 w-3" />
                            </div>

                            {splitLines.map((pair, i) => (
                                <React.Fragment key={i}>
                                    {/* Left Side (Removed/Same) */}
                                    <div className={`overflow-x-auto scrollbar-none border-l-4 ${pair.left?.type === 'removed' ? 'border-error-500 bg-error-50/20 dark:bg-error-900/10' : pair.left?.type === 'same' ? 'border-transparent' : 'border-transparent bg-gray-50/20 dark:bg-gray-950/20'} transition-all`}>
                                        <div className="flex min-w-full">
                                            <span className="w-10 text-right pr-2 text-gray-400 select-none text-[10px] shrink-0 bg-gray-50/30 dark:bg-gray-900/30">{pair.left?.lineNum || ''}</span>
                                            <span className={`w-5 text-center select-none font-bold text-error-400/50 shrink-0`}>{pair.left?.type === 'removed' ? '-' : ' '}</span>
                                            <span className={`px-2 whitespace-pre ${pair.left?.type === 'removed' ? 'text-error-700 dark:text-error-400' : 'text-gray-700 dark:text-gray-300'}`}>{pair.left?.content || ''}</span>
                                        </div>
                                    </div>
                                    {/* Right Side (Added/Same) */}
                                    <div className={`overflow-x-auto scrollbar-none border-l-4 ${pair.right?.type === 'added' ? 'border-success-500 bg-success-50/20 dark:bg-success-900/10' : pair.right?.type === 'same' ? 'border-transparent' : 'border-transparent bg-gray-50/20 dark:bg-gray-950/20'} transition-all`}>
                                        <div className="flex min-w-full">
                                            <span className="w-10 text-right pr-2 text-gray-400 select-none text-[10px] shrink-0 bg-gray-50/30 dark:bg-gray-900/30">{pair.right?.newLineNum || ''}</span>
                                            <span className={`w-5 text-center select-none font-bold text-success-400/50 shrink-0`}>{pair.right?.type === 'added' ? '+' : ' '}</span>
                                            <span className={`px-2 whitespace-pre ${pair.right?.type === 'added' ? 'text-success-700 dark:text-success-400' : 'text-gray-700 dark:text-gray-300'}`}>{pair.right?.content || ''}</span>
                                        </div>
                                    </div>
                                </React.Fragment>
                            ))}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
});

DiffViewer.displayName = 'DiffViewer';

export default DiffViewer;

