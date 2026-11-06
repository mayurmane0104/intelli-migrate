'use client';

import React, { useRef, useEffect } from 'react';
import { ProjectFile } from '@/lib/types';
import { useMigrationStore } from '@/lib/stores/migration-store';
import { SparklesIcon } from '@heroicons/react/24/outline';

interface LiveStreamPanelProps {
    file: ProjectFile;
}

export default function LiveStreamPanel({ file }: LiveStreamPanelProps) {
    const { jobs } = useMigrationStore();
    const preRef = useRef<HTMLPreElement>(null);

    // Find the active job for this file
    const activeJob = Object.values(jobs).find(j => j.fileId === file.id && (j.status === 'running' || j.status === 'queued'));
    const content = activeJob?.streamedContent || 'Initializing migration...';

    useEffect(() => {
        if (preRef.current) {
            preRef.current.scrollTop = preRef.current.scrollHeight;
        }
    }, [content]);

    return (
        <div className="h-full flex flex-col premium-glass overflow-hidden rounded-3xl border-none shadow-2xl">
            <div className="flex items-center justify-between px-6 py-4 border-b border-white/5 bg-white/5 shrink-0">
                <div className="flex items-center gap-3">
                    <div className="relative">
                        <SparklesIcon className="h-4 w-4 text-primary-400 animate-pulse" />
                        <div className="absolute inset-0 bg-primary-400 blur-md opacity-30 animate-pulse" />
                    </div>
                    <span className="font-black text-[10px] tracking-[0.2em] uppercase text-gray-400">
                        Neural Migration Intelligence
                    </span>
                </div>
                <div className="flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.5)] animate-pulse" />
                    <span className="text-[10px] font-black text-gray-400 uppercase tracking-widest">{file.name}</span>
                </div>
            </div>
            <div className="flex-1 p-6 overflow-auto scrollbar-thin scrollbar-thumb-white/10 selection:bg-primary-500/30">
                <pre ref={preRef} className="text-[11px] font-mono leading-relaxed text-emerald-400/80 whitespace-pre-wrap break-all">
                    {content}
                    {activeJob?.status === 'running' && (
                        <span className="inline-block w-2 h-4 bg-primary-500 ml-1 shadow-[0_0_12px_rgba(14,140,233,0.8)] animate-pulse align-middle" />
                    )}
                </pre>
            </div>
            {activeJob?.status === 'running' && (
                <div className="px-6 py-3 bg-primary-500/5 border-t border-white/5">
                    <div className="flex items-center gap-3">
                         <div className="w-1.5 h-1.5 rounded-full bg-primary-500 animate-ping" />
                         <span className="text-[9px] font-black text-primary-400 uppercase tracking-[0.2em]">Synthesizing architectural patterns...</span>
                    </div>
                </div>
            )}
        </div>
    );
}
