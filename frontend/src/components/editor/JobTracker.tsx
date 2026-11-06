'use client';

import React, { useState, useRef, useEffect, useMemo } from 'react';
import { useApp } from '@/contexts/AppContext';
import { useAuth } from '@/contexts/AuthContext';
import { MigrationJob, JobStatus } from '@/lib/types';
import { useMigrationStore } from '@/lib/stores/migration-store';
import {
    CheckCircleIcon, ExclamationCircleIcon,
    ClockIcon, CogIcon, ChevronDownIcon, ChevronRightIcon,
    MagnifyingGlassIcon, RocketLaunchIcon,
    PlayIcon, StopIcon, DocumentMagnifyingGlassIcon, ListBulletIcon,
} from '@heroicons/react/24/outline';
import { LogViewer } from './index';

const statusConfig: Record<JobStatus, { label: string; color: string; bg: string; ring: string }> = {
    queued: { label: 'QUEUED', color: 'text-gray-500 dark:text-gray-400', bg: 'bg-gray-100 dark:bg-gray-800', ring: 'var(--color-gray-300)' },
    running: { label: 'RUNNING', color: 'text-primary-600', bg: 'bg-primary-50 dark:bg-primary-900/20', ring: 'var(--color-primary-500)' },
    done: { label: 'DONE', color: 'text-success-600', bg: 'bg-success-50 dark:bg-success-900/20', ring: 'var(--color-success-500)' },
    failed: { label: 'FAILED', color: 'text-error-600', bg: 'bg-error-50 dark:bg-error-900/20', ring: 'var(--color-error-500)' },
};

const StatusBadge = React.memo(({ status }: { status: JobStatus }) => {
    const cfg = statusConfig[status];
    return (
        <span className={`inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold tracking-wider ${cfg.color} ${cfg.bg} ${status === 'running' ? 'animate-pulse' : ''}`}>
            {cfg.label}
        </span>
    );
});
StatusBadge.displayName = 'StatusBadge';

const ProgressRing = React.memo(({ progress, status, size = 36 }: { progress: number; status: JobStatus; size?: number }) => {
    const strokeWidth = 3;
    const radius = (size - strokeWidth) / 2;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (progress / 100) * circumference;
    const color = statusConfig[status]?.ring || 'var(--color-gray-300)';

    return (
        <svg width={size} height={size} className="shrink-0 -rotate-90">
            <circle cx={size / 2} cy={size / 2} r={radius}
                stroke="#e5e7eb" strokeWidth={strokeWidth} fill="none" />
            <circle cx={size / 2} cy={size / 2} r={radius}
                stroke={color} strokeWidth={strokeWidth} fill="none"
                strokeDasharray={circumference} strokeDashoffset={offset}
                strokeLinecap="round"
                className="transition-all duration-300" />
            <text x={size / 2} y={size / 2}
                textAnchor="middle" dominantBaseline="central"
                className="rotate-90 origin-center"
                style={{ fontSize: '9px', fontWeight: 700, fill: color }}>
                {progress}%
            </text>
        </svg>
    );
});
ProgressRing.displayName = 'ProgressRing';

export default function JobTracker() {
    const { selectedProject, addToast } = useApp();
    const { user } = useAuth();
    const { jobs: jobsMap, isMigrating, retryFile, stopMigration, resumeMigration } = useMigrationStore();

    const [expandedBatches, setExpandedBatches] = useState<Record<string, boolean>>({ 'current': true });

    const handleRetry = async (job: MigrationJob) => {
        if (!selectedProject || !job.batchId) return;
        
        try {
            await retryFile(
                selectedProject.id,
                job.fileId,
                job.batchId,
                {
                    targetPlatform: selectedProject.targetPlatform,
                    migrationType: selectedProject.migrationType,
                    targetRuntime: selectedProject.targetRuntime,
                },
                user?.id
            );
            addToast({
                type: 'success',
                title: 'Retry Started',
                message: `Rescheduling ${job.fileName || 'file'} for transformation.`
            });
        } catch (error: any) {
             addToast({
                type: 'error',
                title: 'Retry Failed',
                message: error.message || 'Could not restart this job.'
            });
        }
    };
    const [expandedJobId, setExpandedJobId] = useState<string | null>(null);
    const [showLogViewer, setShowLogViewer] = useState(false);
    const [logViewerFilter, setLogViewerFilter] = useState<string | null>(null);
    const streamRef = useRef<HTMLPreElement>(null);

    const jobs = useMemo(() => {
        const allJobs = Object.values(jobsMap);
        if (!selectedProject) return allJobs;
        return allJobs.filter(j => j.projectId === selectedProject.id);
    }, [jobsMap, selectedProject]);

    const groupedJobs = useMemo(() => {
        const groups: Record<string, MigrationJob[]> = {};
        jobs.forEach(job => {
            const bid = job.batchId || 'SESSION';
            if (!groups[bid]) groups[bid] = [];
            groups[bid].push(job);
        });

        // Get all batches
        const allBatches = Object.entries(groups).sort((a, b) => {
            const aLatest = Math.max(...a[1].map(j => new Date(j.completedAt || j.startedAt || 0).getTime()));
            const bLatest = Math.max(...b[1].map(j => new Date(j.completedAt || j.startedAt || 0).getTime()));
            return bLatest - aLatest;
        });

        // User requested: "only show the current running Batch Job"
        // We find the first batch that is "active" (has running or queued jobs)
        // or just return the most recent one if all are finished.
        const activeBatch = allBatches.find(([_, batchJobs]) => 
            batchJobs.some(j => j.status === 'running' || j.status === 'queued')
        );

        return activeBatch ? [activeBatch] : (allBatches.length > 0 ? [allBatches[0]] : []);
    }, [jobs]);

    useEffect(() => {
        if (streamRef.current) {
            streamRef.current.scrollTop = streamRef.current.scrollHeight;
        }
    }, [expandedJobId, jobsMap]);

    // Automatically expand failed jobs to show errors
    useEffect(() => {
        if (!expandedJobId) {
            const failedJob = jobs.find(j => j.status === 'failed');
            if (failedJob) setExpandedJobId(failedJob.id);
        }
    }, [jobs, expandedJobId]);

    const toggleBatch = (bid: string) => {
        setExpandedBatches(prev => ({ ...prev, [bid]: !prev[bid] }));
    };

    if (jobs.length === 0) {
        return (
            <div className="flex flex-col items-center justify-center h-full premium-glass border-none text-gray-600 dark:text-gray-800 p-8">
                <ClockIcon className="h-10 w-10 mb-4 opacity-10" />
                <p className="text-[10px] font-black uppercase tracking-widest text-gray-500">System Idle</p>
            </div>
        );
    }

    return (
        <div className="flex flex-col h-full premium-glass border-none overflow-hidden text-gray-900 dark:text-white">
            <div className="flex items-center justify-between px-4 py-3 border-b border-white/5 bg-white/5 shrink-0">
                <div className="flex items-center gap-3">
                    <span className="text-[10px] font-black uppercase tracking-[0.2em] text-gray-400">Current Batch Activity</span>
                    <span className="px-2 py-0.5 bg-primary-100 dark:bg-primary-900/30 text-primary-600 dark:text-primary-400 rounded text-[9px] font-bold">{jobs.length} Active Jobs</span>
                </div>
                <button 
                    onClick={() => {
                        setLogViewerFilter(null);
                        setShowLogViewer(true);
                    }}
                    className="flex items-center gap-1.5 px-2 py-1 bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white rounded text-[9px] font-bold border border-white/10 transition-colors"
                >
                    <ListBulletIcon className="h-3 w-3" />
                    FULL AUDIT LOG
                </button>
            </div>

            <div className="flex-1 overflow-y-auto scrollbar-thin">
                {groupedJobs.map(([batchId, batchJobs]) => {
                    const isBatchExpanded = expandedBatches[batchId] ?? true;
                    const doneCount = batchJobs.filter(j => j.status === 'done').length;
                    const failCount = batchJobs.filter(j => j.status === 'failed').length;
                    const runCount = batchJobs.filter(j => j.status === 'running').length;
                    const batchPct = batchJobs.length > 0 ? Math.round((doneCount / batchJobs.length) * 100) : 0;

                    return (
                        <div key={batchId} className="border-b border-white/5 bg-white/[0.01]">
                            {/* Batch Header */}
                            <div
                                onClick={() => toggleBatch(batchId)}
                                className="w-full flex items-center gap-3 px-4 py-3 hover:bg-white/[0.03] transition-colors group cursor-pointer"
                                role="button"
                                tabIndex={0}
                            >
                                {isBatchExpanded ? <ChevronDownIcon className="h-3.5 w-3.5 text-gray-400" /> : <ChevronRightIcon className="h-3.5 w-3.5 text-gray-300" />}
                                <div className="flex-1 min-w-0">
                                    <div className="flex items-center gap-2 mb-1">
                                        <span className="text-[11px] font-black tracking-wider truncate">
                                            {batchId === 'SESSION' ? 'SESSION' : batchId.toUpperCase()}
                                        </span>
                                        {runCount > 0 && <span className="w-1.5 h-1.5 bg-primary-500 rounded-full animate-ping" />}
                                    </div>
                                    <div className="flex items-center gap-3 text-[10px] font-bold">
                                        <span className="text-emerald-500">{doneCount}/{batchJobs.length} OK</span>
                                        {failCount > 0 && <span className="text-red-500">{failCount} ERR</span>}
                                        <div className="flex-1 h-1 bg-white/5 rounded-full overflow-hidden ml-2">
                                            <div className="h-full bg-gradient-to-r from-primary-500 to-emerald-500" style={{ width: `${batchPct}%` }} />
                                        </div>
                                    </div>
                                </div>
                                <div className="flex flex-col items-end gap-1">
                                    <span className="text-[11px] font-black">{batchPct}%</span>
                                    <div className="flex items-center gap-1">
                                        {runCount > 0 ? (
                                            <button
                                                onClick={(e) => {
                                                    e.stopPropagation();
                                                    if (selectedProject) stopMigration(selectedProject.id, batchId);
                                                }}
                                                className="p-1 px-2 hover:bg-red-50 dark:hover:bg-red-900/40 text-red-500 rounded text-[9px] font-bold border border-red-500/20"
                                            >
                                                STOP BATCH
                                            </button>
                                        ) : (
                                            doneCount < batchJobs.length && (
                                                <button
                                                    onClick={(e) => {
                                                        e.stopPropagation();
                                                        if (selectedProject) resumeMigration(selectedProject.id, batchId, user?.id);
                                                    }}
                                                    className="p-1 px-2 hover:bg-primary-50 dark:hover:bg-primary-900/40 text-primary-500 rounded text-[9px] font-bold border border-primary-500/20"
                                                >
                                                    RESUME BATCH
                                                </button>
                                            )
                                        )}
                                    </div>
                                </div>
                            </div>

                            {/* Batch Jobs */}
                            {isBatchExpanded && (
                                <div className="divide-y divide-white/5 bg-black/5">
                                    {batchJobs.map(job => {
                                        const isExpanded = expandedJobId === job.id;
                                        return (
                                            <div key={job.id} className="transition-colors overflow-hidden">
                                                <div
                                                    onClick={() => setExpandedJobId(isExpanded ? null : job.id)}
                                                    className={`w-full flex items-start gap-4 px-4 py-3 group hover:bg-white/[0.03] cursor-pointer ${job.status === 'failed' ? 'bg-red-500/5' : ''}`}
                                                    role="button"
                                                    tabIndex={0}
                                                >
                                                    <div className="relative shrink-0 mt-1">
                                                        <ProgressRing progress={job.progress} status={job.status} size={32} />
                                                    </div>
                                                    <div className="flex-1 min-w-0">
                                                        <div className="flex flex-col">
                                                            <span className={`text-[11px] font-black truncate ${job.status === 'failed' ? 'text-red-500' : 'text-gray-200'}`}>
                                                                {job.fileName || 'Processing...'}
                                                            </span>
                                                            <span className={`text-[10px] font-black uppercase tracking-widest mt-0.5 ${job.status === 'failed' ? 'text-red-500' : job.status === 'done' ? 'text-emerald-500' : 'text-primary-500'}`}>
                                                                {job.status.toUpperCase()}
                                                            </span>
                                                            <span className="text-[9px] text-gray-500 truncate font-mono mt-1 opacity-60">
                                                                {job.filePath}
                                                            </span>
                                                        </div>
                                                    </div>
                                                    <div className="flex items-center gap-2 self-center">
                                                        {job.status === 'failed' && (
                                                            <button 
                                                                onClick={(e) => {
                                                                    e.stopPropagation();
                                                                    handleRetry(job);
                                                                }}
                                                                className="p-1.5 bg-red-500/10 hover:bg-red-500/20 text-red-500 rounded-md transition-colors border border-red-500/20"
                                                                title="Retry specific file"
                                                            >
                                                                <RocketLaunchIcon className="h-4 w-4" />
                                                            </button>
                                                        )}
                                                        {isExpanded ? <ChevronDownIcon className="h-4 w-4 text-gray-400" /> : <ChevronRightIcon className="h-4 w-4 text-gray-600" />}
                                                    </div>
                                                </div>
                                                {isExpanded && (
                                                    <div className="px-4 pb-4 animate-in slide-in-from-top-2 duration-300">
                                                        <div className="flex flex-col gap-3">
                                                            {job.error && (
                                                                <div className="text-[9px] font-mono leading-relaxed bg-red-950/40 text-red-400 rounded-lg p-3 border border-red-900/50 whitespace-pre-wrap">
                                                                    <span className="font-black text-[10px] block mb-1">RUN-TIME ERROR:</span>
                                                                    {job.error}
                                                                </div>
                                                            )}

                                                            {/* Log Viewer Trigger */}
                                                            {job.migrations && job.migrations.length > 0 && (
                                                                <button 
                                                                    onClick={() => {
                                                                        setLogViewerFilter(job.id);
                                                                        setShowLogViewer(true);
                                                                    }}
                                                                    className="flex items-center justify-center gap-2 w-full py-2 bg-primary-500/5 hover:bg-primary-500/10 text-primary-500 border border-primary-500/10 rounded-lg text-[10px] font-black uppercase tracking-[0.1em] transition-all"
                                                                >
                                                                    <DocumentMagnifyingGlassIcon className="h-4 w-4" />
                                                                    View LLM Exchange Audit ({job.migrations.length})
                                                                </button>
                                                            )}

                                                            {/* Live Telemetry / Migration Report */}
                                                            {!job.error && (job.status === 'running' || job.status === 'done' || job.streamedContent) && (
                                                                <div className="relative group/console">
                                                                    <div className="flex items-center gap-2 mb-1">
                                                                        <span className="text-[8px] font-black text-emerald-500/40 uppercase tracking-widest ml-1">Live Telemetry Report</span>
                                                                    </div>
                                                                    <pre ref={streamRef} className="text-[9px] bg-black/60 text-emerald-400/90 p-4 rounded-xl font-mono overflow-auto max-h-64 scrollbar-thin border border-white/5 leading-relaxed shadow-inner">
                                                                        {job.streamedContent || 'Establishing secure link...'}
                                                                    </pre>
                                                                </div>
                                                            )}
                                                        </div>
                                                    </div>
                                                )}
                                            </div>
                                        );
                                    })}
                                </div>
                            )}
                        </div>
                    );
                })}
            </div>

            {/* Log Viewer Modal */}
            <LogViewer 
                isOpen={showLogViewer}
                onClose={() => setShowLogViewer(false)}
                jobs={logViewerFilter ? jobs.filter(j => j.id === logViewerFilter) : jobs}
                projectId={selectedProject?.id || ''}
            />
        </div>
    );
}
