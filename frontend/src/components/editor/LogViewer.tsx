'use client';

import React, { useState, useMemo } from 'react';
import { Modal } from '@/components/ui';
import { MigrationJob } from '@/lib/types';
import { 
    CommandLineIcon, 
    DocumentTextIcon, 
    ClockIcon, 
    MagnifyingGlassIcon,
    ChevronRightIcon,
    ChevronDownIcon,
    CodeBracketIcon
} from '@heroicons/react/24/outline';

interface LogViewerProps {
    isOpen: boolean;
    onClose: () => void;
    jobs: MigrationJob[];
    projectId: string;
}

export default function LogViewer({ isOpen, onClose, jobs, projectId }: LogViewerProps) {
    const [search, setSearch] = useState('');
    const [expandedJobs, setExpandedJobs] = useState<Set<string>>(new Set());

    const filteredJobs = useMemo(() => {
        if (!search) return jobs;
        const q = search.toLowerCase();
        return jobs.filter(j => 
            j.fileName?.toLowerCase().includes(q) || 
            j.filePath?.toLowerCase().includes(q) ||
            j.error?.toLowerCase().includes(q)
        );
    }, [jobs, search]);

    const toggleJob = (id: string) => {
        setExpandedJobs(prev => {
            const next = new Set(prev);
            next.has(id) ? next.delete(id) : next.add(id);
            return next;
        });
    };

    return (
        <Modal isOpen={isOpen} onClose={onClose} title="LLM Exchange Logs" size="xl">
            <div className="flex flex-col h-[70vh]">
                {/* Search Bar */}
                <div className="px-4 py-3 border-b border-gray-100 dark:border-gray-800 bg-gray-50/50">
                    <div className="relative">
                        <MagnifyingGlassIcon className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400" />
                        <input 
                            type="text" 
                            value={search} 
                            onChange={e => setSearch(e.target.value)}
                            placeholder="Search by file name or path..."
                            className="w-full pl-10 pr-4 py-2 text-sm bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-lg focus:ring-2 focus:ring-primary-500 outline-none transition-all"
                        />
                    </div>
                </div>

                {/* Log List */}
                <div className="flex-1 overflow-y-auto p-4 space-y-4 scrollbar-thin">
                    {filteredJobs.length === 0 ? (
                        <div className="flex flex-col items-center justify-center h-full text-gray-400">
                            <DocumentTextIcon className="h-12 w-12 mb-2 opacity-20" />
                            <p className="text-sm font-medium">No migration logs found</p>
                        </div>
                    ) : (
                        filteredJobs.map(job => {
                            const isExpanded = expandedJobs.has(job.id);
                            return (
                                <div key={job.id} className="border border-gray-100 dark:border-gray-800 rounded-xl overflow-hidden bg-white dark:bg-gray-950 shadow-sm transition-all hover:shadow-md">
                                    <div 
                                        onClick={() => toggleJob(job.id)}
                                        className="flex items-center gap-3 px-4 py-3 cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-900/50 transition-colors"
                                    >
                                        {isExpanded ? <ChevronDownIcon className="h-4 w-4 text-gray-400" /> : <ChevronRightIcon className="h-4 w-4 text-gray-400" />}
                                        <div className="flex-1 min-w-0">
                                            <div className="flex items-center gap-2">
                                                <span className="text-xs font-bold text-gray-900 dark:text-gray-100 truncate">{job.fileName}</span>
                                                <span className={`text-[10px] px-1.5 py-0.5 rounded font-black uppercase tracking-wider ${
                                                    job.status === 'done' ? 'bg-success-50 text-success-600' : 
                                                    job.status === 'failed' ? 'bg-error-50 text-error-600' : 'bg-primary-50 text-primary-600 animate-pulse'
                                                }`}>
                                                    {job.status}
                                                </span>
                                            </div>
                                            <p className="text-[10px] text-gray-500 truncate mt-0.5 font-mono opacity-60">{job.filePath}</p>
                                        </div>
                                    </div>

                                    {isExpanded && (
                                        <div className="px-4 pb-4 space-y-4 animate-in slide-in-from-top-2 duration-200">
                                            {job.error && (
                                                <div className="p-3 bg-red-50 dark:bg-red-950/20 border border-red-100 dark:border-red-900/30 rounded-lg">
                                                    <span className="text-[10px] font-black text-red-600 uppercase block mb-1">Error Details</span>
                                                    <pre className="text-xs font-mono text-red-700 dark:text-red-400 whitespace-pre-wrap">{job.error}</pre>
                                                </div>
                                            )}

                                            {job.migrations?.map((m, idx) => (
                                                <div key={m.id || idx} className="space-y-3">
                                                    <div className="flex items-center gap-2">
                                                        <div className="h-px flex-1 bg-gray-100 dark:bg-gray-800" />
                                                        <span className="text-[10px] font-black text-gray-400 uppercase tracking-widest">Exchange #{idx + 1}</span>
                                                        <div className="h-px flex-1 bg-gray-100 dark:bg-gray-800" />
                                                    </div>

                                                    <div className="grid grid-cols-1 gap-3">
                                                        <div className="space-y-1.5">
                                                            <div className="flex items-center gap-1.5 px-1">
                                                                <CommandLineIcon className="h-3 w-3 text-primary-500" />
                                                                <span className="text-[10px] font-black text-primary-600 uppercase">System Prompt</span>
                                                            </div>
                                                            <pre className="text-[11px] bg-gray-50 dark:bg-black/40 text-gray-600 dark:text-gray-400 p-4 rounded-xl border border-gray-100 dark:border-gray-800 font-mono overflow-auto max-h-48 scrollbar-thin leading-relaxed shadow-inner">
                                                                {m.systemPrompt || 'N/A'}
                                                            </pre>
                                                        </div>

                                                        <div className="space-y-1.5">
                                                            <div className="flex items-center gap-1.5 px-1">
                                                                <DocumentTextIcon className="h-3 w-3 text-indigo-500" />
                                                                <span className="text-[10px] font-black text-indigo-600 uppercase">User Request (Mule Source)</span>
                                                            </div>
                                                            <pre className="text-[11px] bg-gray-50 dark:bg-black/40 text-gray-600 dark:text-gray-400 p-4 rounded-xl border border-gray-100 dark:border-gray-800 font-mono overflow-auto max-h-48 scrollbar-thin leading-relaxed shadow-inner">
                                                                {m.userPrompt || 'N/A'}
                                                            </pre>
                                                        </div>

                                                        <div className="space-y-1.5">
                                                            <div className="flex items-center gap-1.5 px-1">
                                                                <CodeBracketIcon className="h-3 w-3 text-emerald-500" />
                                                                <span className="text-[10px] font-black text-emerald-600 uppercase">LLM Raw Response</span>
                                                            </div>
                                                            <pre className="text-[11px] bg-emerald-50/30 dark:bg-black/60 text-emerald-700 dark:text-emerald-400 p-4 rounded-xl border border-emerald-100 dark:border-emerald-900/30 font-mono overflow-auto max-h-64 scrollbar-thin leading-relaxed shadow-inner">
                                                                {m.rawResponse || 'Waiting for response...'}
                                                            </pre>
                                                        </div>
                                                    </div>
                                                </div>
                                            ))}

                                            {!job.migrations?.length && !job.error && (
                                                <div className="flex items-center gap-2 justify-center py-4 text-gray-400 text-xs italic">
                                                    <ClockIcon className="h-4 w-4 animate-spin" />
                                                    Waiting for migration telemetry...
                                                </div>
                                            )}
                                        </div>
                                    )}
                                </div>
                            );
                        })
                    )}
                </div>

                {/* Footer Stats */}
                <div className="px-6 py-3 border-t border-gray-100 dark:border-gray-800 bg-gray-50/50 text-[10px] font-bold text-gray-500 flex items-center justify-between">
                    <div className="flex items-center gap-4">
                        <span className="flex items-center gap-1.5 text-primary-600"><div className="w-1.5 h-1.5 bg-primary-600 rounded-full" /> Total Jobs: {jobs.length}</span>
                        <span className="flex items-center gap-1.5 text-success-600"><div className="w-1.5 h-1.5 bg-success-600 rounded-full" /> Completed: {jobs.filter(j => j.status === 'done').length}</span>
                        <span className="flex items-center gap-1.5 text-error-600"><div className="w-1.5 h-1.5 bg-error-600 rounded-full" /> Failed: {jobs.filter(j => j.status === 'failed').length}</span>
                    </div>
                    <span className="uppercase tracking-widest opacity-60">Project Audit Log</span>
                </div>
            </div>
        </Modal>
    );
}
