'use client';

import React, { useState, useEffect, useMemo, useCallback, useRef } from 'react';
import { useRouter } from 'next/navigation';
import dynamic from 'next/dynamic';
import { useApp } from '@/contexts/AppContext';
import { analysisApi, workflowApi } from '@/lib/api';
import type { AnalysisJobView, MigrationWorkflow } from '@/lib/types';
import ImportPanel from '@/components/import/ImportPanel';
import {
    ChevronRightIcon, ArrowUpTrayIcon, CommandLineIcon,
    CheckCircleIcon, XCircleIcon, ClockIcon, ArrowPathIcon,
    CpuChipIcon, SparklesIcon, RocketLaunchIcon, CloudArrowUpIcon,
    DocumentTextIcon, BoltIcon, FolderIcon, CalendarDaysIcon,
    EyeIcon, EyeSlashIcon,
} from '@heroicons/react/24/outline';
import { CheckCircleIcon as CheckSolid, XCircleIcon as XSolid } from '@heroicons/react/24/solid';
import { BarChart, Bar, XAxis, YAxis, Tooltip as RechartsTooltip, ResponsiveContainer } from 'recharts';

const AnalysisSummaryPanel = dynamic(() => import('@/components/editor/AnalysisSummaryPanel'), {
    ssr: false,
    loading: () => <div className="h-64 animate-pulse rounded-xl bg-slate-100" />,
});
const RawIRViewer = dynamic(() => import('@/components/editor/RawIRViewer'), {
    ssr: false,
    loading: () => <div className="h-40 animate-pulse rounded-xl bg-slate-100" />,
});

const STATUS: Record<string, { label: string; classes: string }> = {
    pending:       { label: 'Pending',     classes: 'bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400' },
    'in-progress': { label: 'In Progress', classes: 'bg-blue-50 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400' },
    completed:     { label: 'Completed',   classes: 'bg-emerald-50 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400' },
    failed:        { label: 'Failed',      classes: 'bg-red-50 text-red-700 dark:bg-red-900/30 dark:text-red-400' },
};

type WorkflowStep = {
    label: string;
    done: boolean;
    current?: boolean;
};



/*
function ConfMeter({ label, score, level }: { label: string; score: number; level: string }) {
    const pct = Math.round(score * 100);
    const g = pct >= 80 ? 'from-emerald-500 to-emerald-400' : pct >= 60 ? 'from-amber-500 to-amber-400' : 'from-rose-500 to-rose-400';
    const t = pct >= 80 ? 'text-emerald-400' : pct >= 60 ? 'text-amber-400' : 'text-rose-400';
    return (
        <div className="space-y-1.5">
            <div className="flex justify-between items-center">
                <p className="text-[9px] font-black uppercase tracking-widest text-gray-500">{label}</p>
                <div className="flex items-center gap-1.5">
                    <span className={`text-[9px] font-black uppercase ${t}`}>{level}</span>
                    <span className={`text-sm font-black tabular-nums ${t}`}>{pct}%</span>
                </div>
            </div>
            <div className="h-1.5 rounded-full bg-white/5 overflow-hidden">
                <div className={`h-full bg-gradient-to-r ${g} rounded-full transition-all duration-700`} style={{ width: `${pct}%` }} />
            </div>
        </div>
    );
}

function ReadinessBanner({ r }: { r: NonNullable<AnalysisJobView['analysis']>['migration_readiness_summary'] }) {
    const pct = Math.round((r.confidence_score || 0) * 100);
    const col = pct >= 80 ? 'border-emerald-500/30 bg-emerald-500/5' : pct >= 60 ? 'border-amber-500/30 bg-amber-500/5' : 'border-rose-500/30 bg-rose-500/5';
    const acc = pct >= 80 ? 'text-emerald-400' : pct >= 60 ? 'text-amber-400' : 'text-rose-400';
    const badgeCol = pct >= 80 ? 'bg-emerald-500/10 text-emerald-300 border-emerald-500/20' : pct >= 60 ? 'bg-amber-500/10 text-amber-300 border-amber-500/20' : 'bg-rose-500/10 text-rose-300 border-rose-500/20';
    return (
        <div className={`rounded-xl border ${col} p-4`}>
            <div className="flex items-center justify-between gap-4 mb-4">
                <div className="flex items-center gap-2">
                    <ShieldCheckIcon className={`h-4 w-4 ${acc}`} />
                    <p className="text-[10px] font-black uppercase tracking-widest text-gray-300">Migration Readiness</p>
                </div>
                <div className="flex items-center gap-2">
                    <span className={`text-lg font-black ${acc}`}>{pct}%</span>
                    <span className={`px-2 py-0.5 rounded text-[9px] font-black uppercase tracking-widest border ${badgeCol}`}>{r.migration_readiness_label || r.migration_readiness || 'NA'}</span>
                </div>
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                {[
                    { label: 'Flows Analyzed',    value: String(r.flows_analyzed ?? 'NA') },
                    { label: 'Complex Transforms', value: String(r.complex_transformations ?? 'NA') },
                    { label: 'Custom Components',  value: String(r.unsupported_components ?? 'NA') },
                    { label: 'Error Handling',     value: r.error_handling_present ? 'Present' : 'NA' },
                    { label: 'Connectors',         value: listOrNA(r.connectors_detected).join(', ') },
                ].map(item => (
                    <div key={item.label} className="rounded-lg bg-white/[0.03] border border-white/[0.04] px-3 py-2">
                        <p className="text-[8px] font-black uppercase tracking-widest text-gray-600 mb-0.5">{item.label}</p>
                        <p className="text-[11px] font-semibold text-gray-300 truncate">{item.value}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

function GenPreview({ p }: { p: NonNullable<AnalysisJobView['analysis']>['generation_preview'] }) {
    return (
        <div className="rounded-xl border border-white/5 bg-white/[0.02] p-4 space-y-3">
            <p className="text-[9px] font-black uppercase tracking-widest text-gray-500">What Will Be Generated</p>
            <div className="grid grid-cols-2 gap-2">
                {[
                    { label: 'Lambda Functions', value: p.lambda_functions, icon: BoltIcon,        color: 'text-violet-400' },
                    { label: 'Step Functions',   value: p.step_functions,   icon: ChartBarIcon,    color: 'text-sky-400' },
                    { label: 'API Gateways',     value: p.api_gateways,     icon: CloudArrowUpIcon, color: 'text-emerald-400' },
                    { label: 'IAM Policies',     value: p.iam_roles_policies ? 'Yes' : 'NA', icon: ShieldCheckIcon, color: 'text-amber-400' },
                ].map(item => {
                    const Icon = item.icon;
                    return (
                        <div key={item.label} className="flex items-center gap-2 rounded-lg bg-white/[0.03] border border-white/[0.04] px-3 py-2">
                            <Icon className={`h-4 w-4 ${item.color} shrink-0`} />
                            <div className="min-w-0">
                                <p className="text-[8px] font-black uppercase tracking-widest text-gray-600">{item.label}</p>
                                <p className={`text-sm font-black ${item.color}`}>{item.value}</p>
                            </div>
                        </div>
                    );
                })}
            </div>
            {(p.artifacts || []).length > 0 && (
                <div className="space-y-1 pt-1 border-t border-white/5">
                    {(p.artifacts || []).map((a: string, i: number) => (
                        <div key={i} className="flex items-center gap-2 text-[10px] text-gray-500">
                            <span className="text-gray-700">→</span>{a}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}
*/

export default function ProjectDashboard({ params }: { params: Promise<{ projectId: string }> }) {
    const { projects, selectedProject, selectProject, files, migrationLogs, refreshFiles, refreshProjects, isMigrating, migrationSession, activeLLMProvider } = useApp();
    const router = useRouter();
    const [resolvedId, setResolvedId] = useState('');
    const [showImport, setShowImport] = useState(false);
    const [analysisState, setAnalysisState] = useState<AnalysisJobView | null>(null);
    const [analysisError, setAnalysisError] = useState<string | null>(null);
    const [analysisLoading, setAnalysisLoading] = useState(false);
    const [workflow, setWorkflow] = useState<MigrationWorkflow | null>(null);
    const [showRawIr, setShowRawIr] = useState(false);
    const [rawIr, setRawIr] = useState<unknown>(null);
    const [rawIrError, setRawIrError] = useState<string | null>(null);
    const analysisReq = useRef<AbortController | null>(null);
    const rawIrReq = useRef<AbortController | null>(null);
    const projectReq = useRef<AbortController | null>(null);
    const fetchedProjectRef = useRef<string | null>(null);
    const justImported = useRef(false);

    useEffect(() => { params.then(p => setResolvedId(p.projectId)); }, [params]);
    useEffect(() => {
        if (!resolvedId) return;
        if (selectedProject?.id === resolvedId) return;
        const proj = projects.find(p => p.id === resolvedId);
        if (proj) { selectProject(proj); }
        else {
            if (fetchedProjectRef.current === resolvedId) return;
            fetchedProjectRef.current = resolvedId;
            projectReq.current?.abort();
            const controller = new AbortController();
            projectReq.current = controller;
            fetch(`/api/projects/${resolvedId}`, { signal: controller.signal }).then(r => r.json()).then(d => { if (d.project) selectProject(d.project); }).catch(() => {});
        }
    }, [resolvedId, projects, selectedProject, selectProject]);
    useEffect(() => {
        if (!resolvedId) return;
        refreshFiles(resolvedId, false, { includeContent: false, includeMigrations: false, take: 50, page: 0 });
    }, [resolvedId, refreshFiles]);

    const project = selectedProject;
    const projectFiles = useMemo(() => files.filter(f => f.projectId === (project?.id || resolvedId) && f.type === 'file'), [files, project, resolvedId]);
    const projectLogs  = useMemo(() => migrationLogs.filter(l => l.projectId === (project?.id || resolvedId)), [migrationLogs, project, resolvedId]);

    const stats = useMemo(() => {
        const total = projectFiles.length, completed = projectFiles.filter(f => f.status === 'completed').length;
        const failed = projectFiles.filter(f => f.status === 'failed').length, pending = projectFiles.filter(f => f.status === 'pending').length;
        const inProgress = projectFiles.filter(f => f.status === 'in-progress').length;
        return { total, completed, failed, pending, inProgress, pct: total > 0 ? Math.round((completed / total) * 100) : 0 };
    }, [projectFiles]);

    const loadLatestAnalysis = useCallback(async (autoStartIfNotFound = false) => {
        const pid = project?.id || resolvedId; if (!pid) return;
        analysisReq.current?.abort();
        const controller = new AbortController();
        analysisReq.current = controller;
        setAnalysisLoading(true);
        try { setAnalysisState(await analysisApi.latest(pid, false, controller.signal)); setAnalysisError(null); }
        catch (err: unknown) {
            const e = err as { status?: number; message?: string } | null;
            if ((err as { name?: string }).name === 'CanceledError') return;
            if (e?.status === 404) { 
                if (autoStartIfNotFound) {
                    try {
                        const startedJob = await analysisApi.start(pid, {});
                        setAnalysisState(startedJob);
                        setAnalysisError(null);
                    } catch (startErr: unknown) {
                        setAnalysisState(null);
                        setAnalysisError((startErr as { message?: string })?.message || 'Could not auto-start analysis');
                    }
                } else {
                    setAnalysisState(null); setAnalysisError(null); 
                }
            }
            else setAnalysisError(e?.message || 'Could not fetch analysis status');
        } finally { setAnalysisLoading(false); }
    }, [project?.id, resolvedId]);

    const loadWorkflow = useCallback(async () => {
        const pid = project?.id || resolvedId; if (!pid) return;
        try {
            const res = await workflowApi.get(pid);
            setWorkflow(res.workflow);
        } catch {
            setWorkflow(null);
        }
    }, [project?.id, resolvedId]);

    useEffect(() => {
        if (!project || stats.total === 0) { setAnalysisState(null); setAnalysisError(null); return; }
        if (justImported.current) return;
        loadLatestAnalysis(true);
    }, [project, stats.total, loadLatestAnalysis]);

    useEffect(() => {
        loadWorkflow();
    }, [loadWorkflow]);

    useEffect(() => {
        if (!analysisState || (analysisState.status !== 'queued' && analysisState.status !== 'running')) return;
        const t = setTimeout(() => loadLatestAnalysis(), 5000);
        return () => clearTimeout(t);
    }, [analysisState, loadLatestAnalysis]);

    useEffect(() => { setShowRawIr(false); setRawIr(null); setRawIrError(null); loadWorkflow(); }, [analysisState?.jobId, loadWorkflow]);
    useEffect(() => () => {
        analysisReq.current?.abort();
        rawIrReq.current?.abort();
        projectReq.current?.abort();
    }, []);

    const toggleRawIr = useCallback(async () => {
        if (!project || !analysisState?.jobId) return;
        const next = !showRawIr; setShowRawIr(next);
        if (!next || rawIr) return;
        rawIrReq.current?.abort();
        const controller = new AbortController();
        rawIrReq.current = controller;
        try { const r = await analysisApi.raw(project.id, analysisState.jobId, controller.signal); setRawIr(r.rawIr); setRawIrError(null); }
        catch (err: unknown) { setRawIrError((err as { message?: string } | null)?.message || 'Could not load raw IR'); }
    }, [project, analysisState?.jobId, showRawIr, rawIr]);

    const barData = useMemo(() => {
        const g: Record<string, { completed: number; failed: number; pending: number }> = {};
        projectFiles.forEach(f => {
            const folder = f.path.split('/').slice(0, -1).join('/') || '/';
            if (!g[folder]) g[folder] = { completed: 0, failed: 0, pending: 0 };
            if (f.status === 'completed') g[folder].completed++; else if (f.status === 'failed') g[folder].failed++; else g[folder].pending++;
        });
        return Object.entries(g).map(([name, c]) => ({ name: name.split('/').pop() || '/', ...c }));
    }, [projectFiles]);

    const recentLogs = useMemo(() => projectLogs.slice(0, 8), [projectLogs]);

    if (!project) return (
        <div className="p-6 space-y-6 animate-pulse">
            <div className="h-5 bg-gray-200 dark:bg-gray-800 rounded w-56 mb-8" />
            <div className="grid grid-cols-4 gap-4">{Array.from({ length: 4 }).map((_, i) => <div key={i} className="h-24 bg-gray-100 dark:bg-gray-800 rounded-xl" />)}</div>
        </div>
    );

    const projStatus        = STATUS[project.status as keyof typeof STATUS] || STATUS.pending;
    const showSetupPipeline = !isMigrating && !migrationSession && (stats.total === 0 || (stats.completed === 0 && stats.failed === 0 && stats.inProgress === 0));
    const analysisSummary   = analysisState?.analysis?.summary;
    const analysisValidation= analysisState?.analysis?.validation;
    const analysisInventory = analysisState?.analysis?.inventory_summary;
    const analysisFlows     = analysisState?.analysis?.structured_flows || [];
    const analysisWarningCount = (analysisValidation?.warnings?.length ?? 0) + (analysisValidation?.blockers?.length ?? 0);
    const analysisCompleted = analysisState?.status === 'completed' && Boolean(analysisState?.analysis);
    const analysisInFlight  = analysisState?.status === 'queued' || analysisState?.status === 'running';
    const analysisBlocked   = Boolean(analysisValidation?.blockers?.length);
    const canOpenApprovalReview = stats.total > 0 && analysisCompleted && !analysisBlocked;
    const workflowState = workflow?.state;
    const workflowRank: Record<string, number> = {
        UPLOAD_COMPLETE: 1,
        PARSER_COMPLETE: 2,
        IR_GENERATED: 3,
        IR_APPROVED: 4,
        MAPPING_GENERATED: 5,
        MAPPING_APPROVED: 6,
        ARCHITECTURE_GENERATED: 7,
        ARCHITECTURE_APPROVED: 8,
        CODE_GENERATED: 9,
        EXPORT_READY: 10,
    };
    const currentWorkflowRank = workflowState ? workflowRank[workflowState] ?? 0 : 0;


    // ── SETUP PIPELINE ────────────────────────────────────────────────────────
    if (showSetupPipeline) {
        return (
            <div className="min-h-full p-6 max-w-4xl mx-auto">
                <nav className="flex items-center gap-2 text-sm text-gray-400 mb-8">
                    <button onClick={() => router.push('/dashboard/organizations')} className="hover:text-primary-600 transition-colors">Organizations</button>
                    <ChevronRightIcon className="h-3.5 w-3.5" />
                    <span className="text-gray-900 dark:text-gray-100 font-medium">{project.name}</span>
                </nav>

                <div className="flex items-start gap-4 mb-10">
                    <div className="w-14 h-14 bg-gradient-to-br from-primary-500 to-primary-700 rounded-2xl flex items-center justify-center shadow-lg shrink-0">
                        <SparklesIcon className="h-7 w-7 text-white" />
                    </div>
                    <div>
                        <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">{project.name}</h1>
                        <p className="text-gray-500 dark:text-gray-400 mt-1 text-sm">{project.description}</p>
                        <div className="flex items-center gap-3 mt-2">
                            <span className={`px-2.5 py-1 text-xs font-semibold rounded-full ${projStatus.classes}`}>{projStatus.label}</span>
                            <span className="text-xs text-gray-400 flex items-center gap-1"><CalendarDaysIcon className="h-3.5 w-3.5" /> Created {project.createdAt}</span>
                        </div>
                    </div>
                </div>

                {/* Horizontal Progress Bar */}
                <div className="mb-14 px-4 sm:px-8">
                    <div className="relative flex items-center justify-between">
                        <div className="absolute left-0 top-1/2 -translate-y-1/2 w-full h-1.5 bg-gray-200 dark:bg-gray-800 rounded-full z-0" />
                        <div 
                            className="absolute left-0 top-1/2 -translate-y-1/2 h-1.5 bg-primary-500 rounded-full z-0 transition-all duration-700 ease-in-out shadow-[0_0_10px_rgba(var(--color-primary-500),0.5)]"
                            style={{ width: stats.total === 0 ? '0%' : !canOpenApprovalReview ? '50%' : '100%' }} 
                        />
                        
                        {[
                            { step: 1, label: 'Upload' },
                            { step: 2, label: 'Analysis' },
                            { step: 3, label: 'Workspace' }
                        ].map((s) => {
                            const activeStep = stats.total === 0 ? 1 : !canOpenApprovalReview ? 2 : 3;
                            const isCompleted = activeStep > s.step;
                            const isCurrent = activeStep === s.step;
                            return (
                                <div key={s.step} className="relative z-10 flex flex-col items-center">
                                    <div className={`w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold transition-all duration-500 ${
                                        isCompleted ? 'bg-primary-500 text-white shadow-lg shadow-primary-500/40' :
                                        isCurrent ? 'bg-primary-600 text-white ring-4 ring-primary-500/30 shadow-lg shadow-primary-500/50 animate-pulse' :
                                        'bg-gray-200 dark:bg-gray-800 text-gray-500 border-2 border-gray-100 dark:border-gray-900'
                                    }`}>
                                        {isCompleted ? <CheckSolid className="w-5 h-5" /> : s.step}
                                    </div>
                                    <span className={`text-[10px] font-black uppercase tracking-widest absolute top-10 whitespace-nowrap transition-colors duration-500 ${
                                        isCurrent ? 'text-primary-600 dark:text-primary-400' :
                                        isCompleted ? 'text-gray-900 dark:text-gray-100' :
                                        'text-gray-400'
                                    }`}>
                                        {s.label}
                                    </span>
                                </div>
                            );
                        })}
                    </div>
                </div>

                <div className="relative">
                    <div className="absolute left-7 top-7 bottom-7 w-0.5 bg-gradient-to-b from-emerald-500/20 via-primary-500/20 to-gray-500/20 z-0" />
                    <div className="space-y-6 relative z-10">

                        {/* Step 1 */}
                        <div className={`premium-card border-none ${stats.total > 0 ? 'bg-emerald-500/[0.03] border-emerald-500/20' : 'glow-border'}`}>
                            <div className="flex flex-col sm:flex-row gap-5 sm:gap-6">
                                <div className={`w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 shadow-lg ${stats.total > 0 ? 'bg-emerald-500 text-white' : 'bg-primary-500 text-white'}`}>
                                    {stats.total > 0 ? <CheckCircleIcon className="h-8 w-8" /> : <CloudArrowUpIcon className="h-8 w-8" />}
                                </div>
                                <div className="flex-1 min-w-0">
                                    <div className="flex flex-wrap items-center gap-3 mb-2">
                                        <h3 className="text-lg font-black tracking-tighter text-gray-900 dark:text-gray-100 uppercase">Step 1: Upload Project</h3>
                                        {stats.total > 0 && <span className="px-3 py-1 text-[10px] font-black uppercase tracking-widest bg-emerald-500/10 text-emerald-500 rounded-full border border-emerald-500/20">Verified: {stats.total} Nodes</span>}
                                    </div>
                                    <p className="text-sm text-gray-500 mb-6 font-medium leading-relaxed">Connect your Git architecture or upload MuleSoft XML/RAML archives for neural processing.</p>
                                    <button onClick={() => setShowImport(true)}
                                        className={`inline-flex items-center gap-2 px-5 py-2.5 text-[10px] font-black uppercase tracking-[0.2em] rounded-xl transition-all ${stats.total > 0 ? 'bg-gray-100 dark:bg-white/5 text-gray-700 dark:text-gray-300 hover:bg-white' : 'bg-primary-600 hover:bg-primary-700 text-white shadow-xl shadow-primary-500/20'}`}>
                                        <ArrowUpTrayIcon className="h-3.5 w-3.5" />{stats.total > 0 ? 'Re-index Architecture' : 'Begin Import'}
                                    </button>
                                </div>
                            </div>
                        </div>

                        {/* Step 2 */}
                        <div className={`premium-card !p-5 sm:!p-6 border-none ${stats.total === 0 ? 'opacity-40 grayscale pointer-events-none' : 'glow-border'}`}>
                            <div className="space-y-4">
                                <div className="flex flex-col sm:flex-row gap-5 sm:gap-6">
                                    <div className={`w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 shadow-lg ${stats.total === 0 ? 'bg-gray-200 dark:bg-white/5' : 'bg-violet-600 text-white shadow-violet-500/20'}`}>
                                        <CpuChipIcon className={`h-8 w-8 ${stats.total === 0 ? 'text-gray-400' : 'text-white'}`} />
                                    </div>
                                    <div className="flex-1 min-w-0">
                                    <div className="flex flex-wrap items-center gap-3 mb-2">
                                        <h3 className="text-lg font-black tracking-tighter text-gray-900 dark:text-gray-100 uppercase">Step 2: Parse + IR Analysis</h3>
                                        <span className="px-3 py-1 text-[10px] font-black uppercase tracking-widest bg-violet-500/10 text-violet-400 rounded-full border border-violet-500/20">Engine: {activeLLMProvider.toUpperCase()}</span>
                                    </div>
                                    <p className="text-sm text-gray-500 font-medium leading-relaxed">Parse source automatically, generate IR, review connector mappings, then confirm the analysis output.</p>
                                    </div>
                                </div>

                                    {analysisInFlight && (
                                        <div className="flex items-center gap-3 p-3 rounded-xl bg-primary-500/5 border border-primary-500/15">
                                            <div className="w-2 h-2 rounded-full bg-primary-500 animate-pulse shrink-0" />
                                            <div>
                                                <p className="text-[10px] font-black text-primary-400 uppercase tracking-widest">Analysis Running</p>
                                                <p className="text-[10px] text-gray-500 mt-0.5">{analysisState?.progressPct || 0}% — {analysisState?.currentStage || 'analyzing…'}</p>
                                            </div>
                                        </div>
                                    )}

                                    {/* Migration Readiness and Confidence Breakdown sections intentionally hidden per dashboard cleanup request. */}

                                    {/* ══════ 7-SECTION ANALYSIS PANEL ══════ */}
                                    {analysisInventory && analysisCompleted && (
                                        <div className="w-full">
                                            <AnalysisSummaryPanel
                                                inventory={analysisInventory}
                                                structuredFlows={analysisFlows}
                                                summary={analysisSummary}
                                                warningCount={analysisWarningCount}
                                            />
                                        </div>
                                    )}

                                    {/* What Will Be Generated section intentionally hidden per dashboard cleanup request. */}

                                    {/* Summary metric strip hidden because the refreshed analysis panel now owns the scan summary. */}

                                    {/* Migration Readiness Suggestions section intentionally hidden per dashboard cleanup request.
                                    {analysisRisks.length > 0 && (
                                        <div className="rounded-xl border border-sky-500/15 bg-sky-500/5 p-4 mb-4 space-y-2">
                                            <p className="text-[9px] font-black uppercase tracking-widest text-sky-400">Readiness Suggestions</p>
                                            {analysisRisks.map((risk: string, i: number) => (
                                                <div key={i} className="flex items-start gap-2 text-[11px] text-gray-300">
                                                    <span className="text-sky-500 font-black text-[9px] shrink-0 mt-0.5">{String(i + 1).padStart(2, '0')}</span>
                                                    <span>{risk}</span>
                                                </div>
                                            ))}
                                        </div>
                                    )}
                                    */}

                                    {analysisError && <p className="text-xs text-rose-500 mb-3">{analysisError}</p>}

                                    {stats.total > 0 && (
                                        <div className="flex flex-wrap items-center gap-3 pt-1">
                                            <button onClick={() => loadLatestAnalysis()} disabled={analysisLoading}
                                                className="inline-flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-[10px] font-black uppercase tracking-[0.18em] text-slate-700 shadow-sm transition-all hover:border-violet-200 hover:bg-violet-50 hover:text-violet-700 disabled:opacity-50">
                                                <ArrowPathIcon className={`h-3.5 w-3.5 ${analysisLoading ? 'animate-spin' : ''}`} />
                                                {analysisLoading ? 'Checking...' : 'Refresh'}
                                            </button>
                                            {analysisCompleted && (
                                                <button onClick={toggleRawIr}
                                                    className="inline-flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-[10px] font-black uppercase tracking-[0.18em] text-slate-700 shadow-sm transition-all hover:border-sky-200 hover:bg-sky-50 hover:text-sky-700">
                                                    {showRawIr ? <EyeSlashIcon className="h-3.5 w-3.5" /> : <EyeIcon className="h-3.5 w-3.5" />}
                                                    {showRawIr ? 'Hide Raw IR' : 'Raw IR'}
                                                </button>
                                            )}
                                        </div>
                                    )}
                                    {showRawIr && (
                                        <div className="mt-3 max-h-64 overflow-auto rounded-xl border border-slate-200 bg-white p-3 shadow-sm">
                                            <RawIRViewer rawIr={rawIr} rawIrError={rawIrError} />
                                        </div>
                                    )}
                            </div>
                        </div>

                        {/* Step 3 */}
                        <div className={`premium-card border-none ${stats.total === 0 ? 'opacity-40 grayscale pointer-events-none' : 'glow-border'}`}>
                            <div className="flex flex-col sm:flex-row gap-5 sm:gap-6">
                                <div className={`w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 shadow-lg ${canOpenApprovalReview ? 'bg-violet-600 text-white shadow-violet-500/20' : 'bg-gray-200 dark:bg-white/5'}`}>
                                    <RocketLaunchIcon className={`h-8 w-8 ${canOpenApprovalReview ? 'text-white' : 'text-gray-400'}`} />
                                </div>
                                <div className="flex-1 min-w-0">
                                    <h3 className="text-lg font-black tracking-tighter text-gray-900 dark:text-gray-100 uppercase mb-2">Step 3: Migration Workspace</h3>
                                    <p className="text-sm text-gray-500 font-medium mb-4">Continue after reviewing the IR analysis above. Mapping and architecture resolution will run automatically during migration.</p>
                                    <button onClick={() => router.push(`/dashboard/projects/${project.id}/editor`)} disabled={!canOpenApprovalReview}
                                        className="inline-flex items-center gap-2 px-6 py-3 text-[10px] font-black uppercase tracking-[0.2em] bg-violet-600 hover:bg-violet-700 disabled:bg-gray-300 disabled:text-gray-500 dark:disabled:bg-white/5 dark:disabled:text-gray-600 text-white rounded-xl shadow-xl shadow-violet-500/20 transition-all">
                                        <BoltIcon className="h-4 w-4" /> Start Migration
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="mt-8 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-5">
                    <h3 className="text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-widest mb-4">Project Configuration</h3>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-5">
                        {[
                            { label: 'Migration', value: project.migrationType.replace(/-/g, ' → ') },
                            { label: 'Target',    value: project.targetRuntime, capitalize: true },
                            { label: 'Source',    value: project.sourceType,    upper: true },
                            { label: 'AI Engine', value: activeLLMProvider,     upper: true },
                        ].map(item => (
                            <div key={item.label}>
                                <p className="text-xs text-gray-400 mb-1">{item.label}</p>
                                <p className={`text-sm font-semibold text-gray-800 dark:text-gray-200 ${item.capitalize ? 'capitalize' : ''} ${item.upper ? 'uppercase' : ''}`}>{item.value}</p>
                            </div>
                        ))}
                    </div>
                </div>

                {showImport && <ImportPanel onClose={(imported) => {
                    setShowImport(false);
                    if (imported) {
                        justImported.current = true;
                        refreshFiles(project.id, true);
                        refreshProjects(project.workspaceId, true);
                        setTimeout(() => {
                            justImported.current = false;
                            loadLatestAnalysis(true);
                        }, 1500);
                        setTimeout(loadWorkflow, 1500);
                    }
                }} />}
            </div>
        );
    }

    // ── ACTIVE DASHBOARD ──────────────────────────────────────────────────────
    const statCards = [
        { label: 'Total Files', value: stats.total, sub: `${stats.pending} pending`, icon: DocumentTextIcon, iconColor: 'text-gray-500', iconBg: 'bg-gray-100 dark:bg-gray-800/50', valueColor: 'text-gray-900 dark:text-gray-100' },
        { label: 'Migrated', value: stats.completed, sub: `${stats.pct}% complete`, icon: CheckCircleIcon, iconColor: 'text-emerald-500', iconBg: 'bg-emerald-500/10', valueColor: 'text-emerald-500' },
        { label: 'Failed', value: stats.failed, sub: stats.failed > 0 ? 'needs attention' : 'all clear', icon: XCircleIcon, iconColor: stats.failed > 0 ? 'text-rose-500' : 'text-gray-300', iconBg: stats.failed > 0 ? 'bg-rose-500/10' : 'bg-gray-50 dark:bg-gray-800/50', valueColor: stats.failed > 0 ? 'text-rose-500' : 'text-gray-400' },
        { label: stats.inProgress > 0 ? 'In Progress' : 'Pending', value: stats.inProgress > 0 ? stats.inProgress : stats.pending, sub: stats.inProgress > 0 ? 'actively running' : 'not started', icon: stats.inProgress > 0 ? ArrowPathIcon : ClockIcon, iconColor: stats.inProgress > 0 ? 'text-primary-500' : 'text-gray-400', iconBg: stats.inProgress > 0 ? 'bg-primary-500/10' : 'bg-gray-50 dark:bg-gray-800/50', valueColor: stats.inProgress > 0 ? 'text-primary-500' : 'text-gray-500' },
        { label: 'Batch Runs', value: project.migrationRuns ?? 0, sub: `${project.migrationRuns ?? 0} run${(project.migrationRuns ?? 0) !== 1 ? 's' : ''}`, icon: BoltIcon, iconColor: 'text-violet-500', iconBg: 'bg-violet-500/10', valueColor: 'text-violet-500' },
    ];

    return (
        <div className="flex flex-col min-h-full overflow-y-auto bg-gray-50/30 dark:bg-black">
            <div className="glass-header px-8 py-5 shrink-0 z-50">
                <nav className="flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.15em] text-gray-400 mb-2.5">
                    <button onClick={() => router.push('/dashboard/organizations')} className="hover:text-primary-600 transition-colors">Organizations</button>
                    <ChevronRightIcon className="h-3 w-3 text-gray-300" />
                    <span className="text-gray-600 dark:text-gray-500">{project.name}</span>
                    <ChevronRightIcon className="h-3 w-3 text-gray-300" />
                    <span className="text-gray-900 dark:text-gray-100">Control Center</span>
                </nav>
                <div className="flex items-center justify-between gap-6">
                    <div className="flex items-center gap-4 min-w-0">
                        <div className="w-12 h-12 premium-gradient rounded-2xl flex items-center justify-center shadow-2xl shadow-primary-500/20 shrink-0">
                            <SparklesIcon className="h-6 w-6 text-white" />
                        </div>
                        <div className="min-w-0">
                            <div className="flex items-center gap-3 flex-wrap">
                                <h1 className="text-2xl font-black tracking-tighter text-gray-900 dark:text-gray-100 truncate">{project.name}</h1>
                                <span className={`px-2.5 py-1 text-[10px] font-black uppercase tracking-wider rounded-full shrink-0 ${projStatus.classes}`}>{projStatus.label}</span>
                                {isMigrating && <span className="flex items-center gap-1.5 px-3 py-1 text-[10px] font-black uppercase tracking-widest rounded-full bg-primary-500/10 text-primary-500 animate-pulse shrink-0 border border-primary-500/20"><span className="w-2 h-2 bg-primary-500 rounded-full" /> Live Engine</span>}
                            </div>
                            <p className="text-sm text-gray-500 dark:text-gray-400 truncate mt-1">Refactoring MuleSoft ESB to Cloud-Native AWS Architecture</p>
                        </div>
                    </div>
                    <div className="flex items-center gap-3 shrink-0">
                        <button onClick={() => setShowImport(true)} className="flex items-center gap-2 px-4 py-2.5 text-xs font-black uppercase tracking-widest text-gray-700 dark:text-gray-300 bg-white/50 dark:bg-white/5 border border-gray-200 dark:border-white/10 rounded-xl hover:bg-white dark:hover:bg-white/10 transition-all">
                            <ArrowUpTrayIcon className="h-4 w-4" /><span className="hidden sm:inline">Import</span>
                        </button>
                        <button onClick={() => router.push(`/dashboard/projects/${project.id}/editor`)} className="flex items-center gap-2 px-5 py-2.5 text-xs font-black uppercase tracking-widest text-white premium-gradient rounded-xl shadow-lg shadow-primary-500/10 hover:shadow-primary-500/20 transition-all">
                            <CommandLineIcon className="h-4 w-4" /><span className="hidden sm:inline">Code Lab</span>
                        </button>
                    </div>
                </div>
            </div>

            <div className="flex-1 p-8 space-y-8 max-w-[1600px] mx-auto w-full">
                <div className="grid grid-cols-2 xl:grid-cols-5 gap-5">
                    {statCards.map(card => { const Icon = card.icon; return (
                        <div key={card.label} className="premium-card flex flex-col justify-between group">
                            <div className="flex items-start justify-between mb-6">
                                <p className="text-[10px] font-black text-gray-400 uppercase tracking-[0.2em]">{card.label}</p>
                                <div className={`w-10 h-10 rounded-xl flex items-center justify-center shrink-0 transition-transform group-hover:scale-110 ${card.iconBg}`}><Icon className={`h-5 w-5 ${card.iconColor}`} /></div>
                            </div>
                            <div>
                                <p className={`text-4xl font-black tracking-tighter mb-1.5 ${card.valueColor}`}>{card.value}</p>
                                <p className="text-[10px] font-bold text-gray-400 uppercase tracking-widest">{card.sub}</p>
                            </div>
                        </div>
                    ); })}
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <div className="lg:col-span-2 space-y-8">
                        <div className="premium-card relative overflow-hidden">
                            <div className="absolute top-0 right-0 w-64 h-64 bg-primary-500/5 blur-[100px] rounded-full -mr-20 -mt-20" />
                            <div className="flex items-start justify-between mb-8 relative z-10">
                                <div>
                                    <h3 className="text-xl font-black tracking-tighter text-gray-800 dark:text-gray-100">Global Migration Velocity</h3>
                                    <p className="text-xs font-bold text-gray-400 uppercase tracking-widest mt-1">{stats.completed} of {stats.total} total nodes refactored</p>
                                </div>
                                <div className="text-right">
                                    <span className="text-5xl font-black tracking-tighter text-gradient">{stats.pct}</span>
                                    <span className="text-lg font-black text-gray-300 ml-1">%</span>
                                </div>
                            </div>
                            <div className="relative h-4 bg-gray-100 dark:bg-white/5 rounded-full overflow-hidden shadow-inner mb-6">
                                {stats.total > 0 && (<>
                                    <div className="absolute left-0 top-0 h-full bg-gradient-to-r from-emerald-500 to-emerald-400 transition-all duration-1000 rounded-full" style={{ width: `${(stats.completed / stats.total) * 100}%` }} />
                                    {stats.inProgress > 0 && <div className="absolute top-0 h-full bg-primary-400 animate-pulse" style={{ left: `${(stats.completed / stats.total) * 100}%`, width: `${(stats.inProgress / stats.total) * 100}%` }} />}
                                    {stats.failed > 0 && <div className="absolute top-0 h-full bg-rose-500" style={{ left: `${((stats.completed + stats.inProgress) / stats.total) * 100}%`, width: `${(stats.failed / stats.total) * 100}%` }} />}
                                </>)}
                            </div>
                            <div className="flex flex-wrap items-center gap-6 relative z-10">
                                <span className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-gray-500"><span className="w-2.5 h-2.5 bg-emerald-500 rounded-full" />{stats.completed} Success</span>
                                {stats.inProgress > 0 && <span className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-gray-500"><span className="w-2.5 h-2.5 bg-primary-500 rounded-full animate-pulse" />{stats.inProgress} Active</span>}
                                {stats.failed > 0 && <span className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-gray-500"><span className="w-2.5 h-2.5 bg-rose-500 rounded-full" />{stats.failed} Failed</span>}
                                <span className="ml-auto flex items-center gap-2 px-3 py-1.5 bg-violet-500/5 border border-violet-500/10 rounded-lg">
                                    <BoltIcon className="w-3.5 h-3.5 text-violet-500" />
                                    <span className="text-[10px] font-black uppercase tracking-widest text-violet-500">{project.migrationRuns ?? 0} Cycle{(project.migrationRuns ?? 0) !== 1 ? 's' : ''}</span>
                                </span>
                            </div>
                        </div>

                        <div className="premium-card">
                            <div className="flex items-center justify-between mb-8">
                                <div>
                                    <h3 className="text-lg font-black tracking-tighter text-gray-800 dark:text-gray-100">Functional Distribution</h3>
                                    <p className="text-[10px] font-bold text-gray-400 uppercase tracking-widest mt-1">Refactoring status per source domain</p>
                                </div>
                            </div>
                            {barData.length > 0 ? (
                                <ResponsiveContainer width="100%" height={260}>
                                    <BarChart data={barData} barGap={4} barCategoryGap="25%">
                                        <XAxis dataKey="name" tick={{ fontSize: 10, fontWeight: 800, fill: '#9ca3af' }} axisLine={false} tickLine={false} />
                                        <YAxis tick={{ fontSize: 10, fontWeight: 800, fill: '#9ca3af' }} axisLine={false} tickLine={false} width={25} />
                                        <RechartsTooltip contentStyle={{ background: 'rgba(15,23,42,0.9)', border: 'none', borderRadius: '12px' }} itemStyle={{ fontSize: '10px', fontWeight: 900, textTransform: 'uppercase' }} />
                                        <Bar dataKey="completed" name="Refactored" fill="#10b981" radius={[6, 6, 0, 0]} />
                                        <Bar dataKey="failed"    name="Issues"    fill="#f43f5e" radius={[6, 6, 0, 0]} />
                                        <Bar dataKey="pending"   name="Backlog"   fill="rgba(156,163,175,0.1)" radius={[6, 6, 0, 0]} />
                                    </BarChart>
                                </ResponsiveContainer>
                            ) : (
                                <div className="h-52 flex flex-col items-center justify-center text-gray-300 dark:text-gray-700">
                                    <FolderIcon className="h-10 w-10 mb-4 opacity-20" />
                                    <p className="text-[10px] font-black uppercase tracking-widest">No Domain Data</p>
                                </div>
                            )}
                        </div>
                    </div>

                    <div className="space-y-8">
                        <div className="premium-card bg-gradient-to-br from-gray-900 to-black text-white border-none shadow-2xl shadow-primary-500/10 overflow-hidden relative">
                            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-primary-500 via-violet-500 to-rose-500" />
                            <div className="flex items-center gap-3 mb-8">
                                <div className="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center border border-white/10"><CpuChipIcon className="h-5 w-5 text-primary-400" /></div>
                                <div>
                                    <h3 className="text-sm font-black uppercase tracking-[0.2em] text-white">Intelligence Hub</h3>
                                    <p className="text-[9px] font-bold text-gray-500 uppercase tracking-widest">Neural Migration Mapping</p>
                                </div>
                            </div>
                            <div className="space-y-5">
                                {[
                                    { label: 'Core Engine',    value: activeLLMProvider.toUpperCase(), color: 'text-primary-400' },
                                    { label: 'Architecture',   value: project.migrationType.replace(/-/g, ' → '), color: 'text-white' },
                                    { label: 'Runtime Target', value: project.targetRuntime, capitalize: true, color: 'text-white' },
                                    { label: 'Source Origin',  value: project.sourceType, upper: true, color: 'text-white' },
                                ].map(item => (
                                    <div key={item.label}>
                                        <p className="text-[9px] font-black text-gray-500 uppercase tracking-widest mb-1.5">{item.label}</p>
                                        <p className={`text-xs font-black ${item.color} ${item.capitalize ? 'capitalize' : ''} ${item.upper ? 'uppercase' : ''} tracking-wider`}>{item.value}</p>
                                    </div>
                                ))}
                            </div>
                            <div className="mt-8 pt-6 border-t border-white/5 grid grid-cols-2 gap-3">
                                <button onClick={() => router.push(`/dashboard/projects/${project.id}/editor`)} className="flex items-center justify-center gap-2 px-3 py-2.5 bg-white/5 hover:bg-white/10 text-[9px] font-black uppercase tracking-[0.2em] rounded-xl transition-all border border-white/5"><CommandLineIcon className="h-3.5 w-3.5" /> Lab</button>
                                <button onClick={() => router.push(`/dashboard/projects/${project.id}/history`)} className="flex items-center justify-center gap-2 px-3 py-2.5 bg-white/5 hover:bg-white/10 text-[9px] font-black uppercase tracking-[0.2em] rounded-xl transition-all border border-white/5"><ClockIcon className="h-3.5 w-3.5" /> Logs</button>
                            </div>
                        </div>

                        <div className="premium-card">
                            <div className="flex items-center justify-between mb-8">
                                <h3 className="text-xs font-black uppercase tracking-[0.2em] text-gray-800 dark:text-gray-200">Activity Pulse</h3>
                                {recentLogs.length > 0 && <button onClick={() => router.push(`/dashboard/projects/${project.id}/history`)} className="text-[10px] font-black uppercase tracking-widest text-primary-500 hover:text-primary-600">History →</button>}
                            </div>
                            {recentLogs.length === 0 ? (
                                <div className="py-12 text-center">
                                    <ClockIcon className="h-10 w-10 text-gray-100 dark:text-gray-800 mx-auto mb-4" />
                                    <p className="text-[10px] font-black uppercase tracking-widest text-gray-400">System Idle</p>
                                    <p className="text-[9px] font-bold text-gray-300 dark:text-gray-700 mt-1 uppercase">Awaiting migration sequence</p>
                                </div>
                            ) : (
                                <div className="space-y-6">
                                    {recentLogs.map((log, i) => (
                                        <div key={log.id} className="relative flex gap-4">
                                            {i < recentLogs.length - 1 && <div className="absolute left-[11px] top-8 bottom-[-24px] w-px bg-gray-100 dark:bg-white/5" />}
                                            <div className={`w-6 h-6 rounded-lg flex items-center justify-center shrink-0 z-10 ${log.status === 'success' ? 'bg-emerald-500/10 border border-emerald-500/20' : log.status === 'error' ? 'bg-rose-500/10 border border-rose-500/20' : 'bg-gray-100 dark:bg-white/10'}`}>
                                                {log.status === 'success' ? <CheckSolid className="h-3 w-3 text-emerald-500" /> : log.status === 'error' ? <XSolid className="h-3 w-3 text-rose-500" /> : <ClockIcon className="h-3 w-3 text-gray-400" />}
                                            </div>
                                            <div className="flex-1 min-w-0">
                                                <p className="text-[10px] font-black text-gray-800 dark:text-gray-200 uppercase tracking-widest truncate">{log.fileName}</p>
                                                <p className="text-[9px] font-bold text-gray-500 uppercase tracking-tighter mt-1 line-clamp-1">{log.message}</p>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>

            {showImport && <ImportPanel onClose={(imported) => {
                setShowImport(false);
                if (imported) {
                    justImported.current = true;
                    refreshFiles(project.id, true);
                    refreshProjects(project.workspaceId, true);
                    setTimeout(() => {
                        justImported.current = false;
                        loadLatestAnalysis(true);
                    }, 1500);
                    setTimeout(loadWorkflow, 1500);
                }
            }} />}
        </div>
    );
}









// 'use client';

// import React, { useState, useEffect, useMemo, useCallback } from 'react';
// import { useRouter } from 'next/navigation';
// import { useApp } from '@/contexts/AppContext';
// import { analysisApi } from '@/lib/api';
// import type { AnalysisInventorySummary, AnalysisJobView, StructuredFlow } from '@/lib/types';
// import ImportPanel from '@/components/import/ImportPanel';
// import {
//     ChevronRightIcon,
//     ArrowUpTrayIcon,
//     CommandLineIcon,
//     CheckCircleIcon,
//     XCircleIcon,
//     ClockIcon,
//     ArrowPathIcon,
//     CpuChipIcon,
//     SparklesIcon,
//     RocketLaunchIcon,
//     CloudArrowUpIcon,
//     DocumentTextIcon,
//     BoltIcon,
//     FolderIcon,
//     CalendarDaysIcon,
// } from '@heroicons/react/24/outline';
// import { CheckCircleIcon as CheckSolid, XCircleIcon as XSolid } from '@heroicons/react/24/solid';
// import { BarChart, Bar, XAxis, YAxis, Tooltip as RechartsTooltip, ResponsiveContainer } from 'recharts';

// const textOrNA = (value: unknown) => {
//     if (value === null || value === undefined) return 'NA';
//     const text = String(value).trim();
//     return text.length ? text : 'NA';
// };

// const listOrNA = (values?: unknown[]) => {
//     if (!Array.isArray(values) || values.length === 0) return ['NA'];
//     const cleaned = values.map(textOrNA).filter(value => value !== 'NA');
//     return cleaned.length ? cleaned : ['NA'];
// };

// const recordText = (row: Record<string, unknown>, key: string) => textOrNA(row[key]);

// const statusConfig: Record<string, { label: string; classes: string }> = {
//     pending: { label: 'Pending', classes: 'bg-gray-100 text-gray-600 dark:bg-gray-800 dark:text-gray-400' },
//     'in-progress': { label: 'In Progress', classes: 'bg-blue-50 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400' },
//     completed: { label: 'Completed', classes: 'bg-emerald-50 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400' },
//     failed: { label: 'Failed', classes: 'bg-red-50 text-red-700 dark:bg-red-900/30 dark:text-red-400' },
// };

// function InventorySummary({ inventory }: { inventory: AnalysisInventorySummary }) {
//     return (
//         <div className="rounded-lg border border-gray-200 dark:border-gray-700 p-3 mb-3 text-xs space-y-3">
//             <p className="font-semibold text-gray-700 dark:text-gray-200">Complete Project Summary</p>
//             <SummarySection title="1. Mule Configuration Files">
//                 {listOrNA(inventory.mule_configuration_files).map((file, index) => (
//                     <div key={`mule-file-${index}`}>{file}</div>
//                 ))}
//             </SummarySection>
//             <SummarySection title="2. Flows and what it doing highlevel plus activities">
//                 <div>Flow type counts: {Object.keys(inventory.flow_type_counts || {}).length ? Object.entries(inventory.flow_type_counts).map(([type, count]) => `${type}: ${count}`).join(', ') : 'NA'}</div>
//                 {(inventory.flows || []).length ? inventory.flows.map((flow) => (
//                     <div key={`${flow.type}-${flow.name}`} className="rounded-md border border-gray-100 dark:border-gray-800 p-2 space-y-1">
//                         <div><span className="font-semibold">{textOrNA(flow.type)}:</span> {textOrNA(flow.name)}</div>
//                         <div>High level: {textOrNA(flow.high_level)}</div>
//                         <div>Activities: {listOrNA(flow.activities).join('; ')}</div>
//                     </div>
//                 )) : <div>NA</div>}
//             </SummarySection>
//             <SummarySection title="3. Connectors and its connection details">
//                 {(inventory.connectors || []).length ? inventory.connectors.map((connector, index) => (
//                     <div key={`connector-${index}`} className="rounded-md border border-gray-100 dark:border-gray-800 p-2">
//                         <span className="font-semibold">{textOrNA(connector.connector_type)}</span> [{textOrNA(connector.name)}]: {listOrNA(connector.connection_details).join(', ')}
//                     </div>
//                 )) : <div>NA</div>}
//             </SummarySection>
//             <SummarySection title="4. DataWeave / Transformations">
//                 {(inventory.dataweave_transformations || []).length ? inventory.dataweave_transformations.map((row, index) => (
//                     <div key={`dw-${index}`}>{recordText(row, 'id')} | Flow: {recordText(row, 'flow')} | {recordText(row, 'source_field')} to {recordText(row, 'target_field')} | {recordText(row, 'transformation')}</div>
//                 )) : <div>NA</div>}
//             </SummarySection>
//             <SummarySection title="5. Properties Used">
//                 {(inventory.properties_used || []).length ? inventory.properties_used.map((row, index) => (
//                     <div key={`prop-${index}`}>{recordText(row, 'key')} | File: {recordText(row, 'defined_in_file')} | Flows: {listOrNA(row['used_in_flows'] as unknown[]).join(', ')}</div>
//                 )) : <div>NA</div>}
//             </SummarySection>
//             <SummarySection title="6. Error handling and logging">
//                 {(inventory.error_handling_and_logging || []).length ? inventory.error_handling_and_logging.map((row, index) => (
//                     <div key={`error-log-${index}`}>Flow: {recordText(row, 'flow')} | Error handling: {recordText(row, 'error_handling')} | Logging: {listOrNA(row['logging'] as unknown[]).join(', ')}</div>
//                 )) : <div>NA</div>}
//             </SummarySection>
//             <SummarySection title="7. Munit Test Cases">
//                 {(inventory.munit_test_cases || []).length ? inventory.munit_test_cases.map((row, index) => (
//                     <div key={`munit-${index}`}>{recordText(row, 'name')} | File: {recordText(row, 'file')} | Target flow: {recordText(row, 'target_flow')}</div>
//                 )) : <div>NA</div>}
//             </SummarySection>
//             <SummarySection title="Readiness Suggestions">
//                 {listOrNA(inventory.readiness_suggestions).map((suggestion, index) => (
//                     <div key={`suggestion-${index}`}>- {suggestion}</div>
//                 ))}
//             </SummarySection>
//         </div>
//     );
// }

// function SummarySection({ title, children }: { title: string; children: React.ReactNode }) {
//     return (
//         <div className="space-y-1">
//             <p className="font-semibold text-gray-500 dark:text-gray-400">{title}</p>
//             <div className="space-y-1 text-gray-700 dark:text-gray-300">{children}</div>
//         </div>
//     );
// }

// function StructuredFlowSummary({ flows }: { flows: StructuredFlow[] }) {
//     return (
//         <div className="rounded-lg border border-gray-200 dark:border-gray-700 p-3 mb-3 space-y-3">
//             <p className="text-xs font-semibold text-gray-500">Structured Flow View</p>
//             {flows.map((flow: StructuredFlow) => (
//                 <div key={flow.flow_name} className="text-xs border border-gray-100 dark:border-gray-800 rounded-lg p-2 space-y-2">
//                     <div><span className="font-semibold">{textOrNA(flow.flow_type)}:</span> {textOrNA(flow.flow_name)}</div>
//                     <div><span className="font-semibold">High Level:</span> {textOrNA(flow.high_level_summary)}</div>
//                     <div><span className="font-semibold">Trigger:</span> {textOrNA(flow.trigger || flow.source)}</div>
//                     <div>
//                         <span className="font-semibold">Steps:</span>
//                         <div className="mt-1 space-y-1">
//                             {(flow.step_details || []).length ? flow.step_details.map((step: StructuredFlow['step_details'][number]) => (
//                                 <div key={`${flow.flow_name}-${step.index}`} className="text-gray-600 dark:text-gray-300">
//                                     {step.index}. {textOrNA(step.title)}{step.mapping ? ` (${step.mapping})` : ''}{step.condition ? ` - ${step.condition}` : ''}
//                                 </div>
//                             )) : <div>NA</div>}
//                         </div>
//                     </div>
//                     <div><span className="font-semibold">Error Handling:</span> {listOrNA(flow.error_handling).join('; ')}</div>
//                     <div><span className="font-semibold">Dependencies:</span> {listOrNA(flow.dependencies).join(', ')}</div>
//                     <div><span className="font-semibold">Decision Logic:</span> {listOrNA(flow.decision_logic).join(' | ')}</div>
//                 </div>
//             ))}
//         </div>
//     );
// }

// export default function ProjectDashboard({ params }: { params: Promise<{ projectId: string }> }) {
//     const {
//         projects, selectedProject, selectProject, files, migrationLogs,
//         refreshFiles, refreshProjects, isMigrating, migrationSession, activeLLMProvider,
//     } = useApp();
//     const router = useRouter();
//     const [resolvedId, setResolvedId] = useState('');
//     const [showImport, setShowImport] = useState(false);
//     const [analysisState, setAnalysisState] = useState<AnalysisJobView | null>(null);
//     const [analysisError, setAnalysisError] = useState<string | null>(null);
//     const [analysisLoading, setAnalysisLoading] = useState(false);
//     const [analysisConfirmed, setAnalysisConfirmed] = useState(false);
//     const [showRawIr, setShowRawIr] = useState(false);
//     const [rawIr, setRawIr] = useState<unknown>(null);
//     const [rawIrError, setRawIrError] = useState<string | null>(null);

//     useEffect(() => { params.then(p => setResolvedId(p.projectId)); }, [params]);

//     useEffect(() => {
//         if (!resolvedId) return;
//         if (selectedProject?.id === resolvedId) return;
//         const proj = projects.find(p => p.id === resolvedId);
//         if (proj) {
//             selectProject(proj);
//         } else {
//             fetch(`/api/projects/${resolvedId}`)
//                 .then(r => r.json())
//                 .then(data => { if (data.project) selectProject(data.project); })
//                 .catch(() => { });
//         }
//     }, [resolvedId, projects, selectedProject, selectProject]);

//     useEffect(() => {
//         if (!resolvedId) return;
//         refreshFiles(resolvedId);
//     }, [resolvedId, refreshFiles]);

//     const project = selectedProject;
//     const projectFiles = useMemo(
//         () => files.filter(f => f.projectId === (project?.id || resolvedId) && f.type === 'file'),
//         [files, project, resolvedId]
//     );
//     const projectLogs = useMemo(
//         () => migrationLogs.filter(l => l.projectId === (project?.id || resolvedId)),
//         [migrationLogs, project, resolvedId]
//     );

//     const stats = useMemo(() => {
//         const total = projectFiles.length;
//         const completed = projectFiles.filter(f => f.status === 'completed').length;
//         const failed = projectFiles.filter(f => f.status === 'failed').length;
//         const pending = projectFiles.filter(f => f.status === 'pending').length;
//         const inProgress = projectFiles.filter(f => f.status === 'in-progress').length;
//         const pct = total > 0 ? Math.round((completed / total) * 100) : 0;
//         return { total, completed, failed, pending, inProgress, pct };
//     }, [projectFiles]);

//     const loadLatestAnalysis = useCallback(async () => {
//         const projectId = project?.id || resolvedId;
//         if (!projectId) return;

//         setAnalysisLoading(true);
//         try {
//             const latest = await analysisApi.latest(projectId);
//             setAnalysisState(latest);
//             setAnalysisError(null);
//         } catch (err: unknown) {
//             const error = err as { status?: number; message?: string } | null;
//             if (error?.status === 404) {
//                 setAnalysisState(null);
//                 setAnalysisError(null);
//             } else {
//                 setAnalysisError(error?.message || 'Could not fetch analysis status');
//             }
//         } finally {
//             setAnalysisLoading(false);
//         }
//     }, [project?.id, resolvedId]);

//     useEffect(() => {
//         if (!project || stats.total === 0) {
//             setAnalysisState(null);
//             setAnalysisError(null);
//             setAnalysisConfirmed(false);
//             return;
//         }
//         loadLatestAnalysis();
//     }, [project, stats.total, loadLatestAnalysis]);

//     useEffect(() => {
//         if (!analysisState || (analysisState.status !== 'queued' && analysisState.status !== 'running')) return;
//         const timer = setInterval(() => { loadLatestAnalysis(); }, 2000);
//         return () => clearInterval(timer);
//     }, [analysisState, loadLatestAnalysis]);

//     useEffect(() => {
//         setAnalysisConfirmed(false);
//         setShowRawIr(false);
//         setRawIr(null);
//         setRawIrError(null);
//     }, [analysisState?.jobId]);

//     const toggleRawIr = useCallback(async () => {
//         if (!project || !analysisState?.jobId) return;
//         const nextState = !showRawIr;
//         setShowRawIr(nextState);
//         if (!nextState || rawIr) return;
//         try {
//             const response = await analysisApi.raw(project.id, analysisState.jobId);
//             setRawIr(response.rawIr);
//             setRawIrError(null);
//         } catch (err: unknown) {
//             const error = err as { message?: string } | null;
//             setRawIrError(error?.message || 'Could not load raw IR');
//         }
//     }, [project, analysisState?.jobId, showRawIr, rawIr]);

//     const barData = useMemo(() => {
//         const groups: Record<string, { completed: number; failed: number; pending: number }> = {};
//         projectFiles.forEach(f => {
//             const folder = f.path.split('/').slice(0, -1).join('/') || '/';
//             if (!groups[folder]) groups[folder] = { completed: 0, failed: 0, pending: 0 };
//             if (f.status === 'completed') groups[folder].completed++;
//             else if (f.status === 'failed') groups[folder].failed++;
//             else groups[folder].pending++;
//         });
//         return Object.entries(groups).map(([name, counts]) => ({
//             name: name.split('/').pop() || '/',
//             ...counts,
//         }));
//     }, [projectFiles]);

//     const recentLogs = useMemo(() => projectLogs.slice(0, 8), [projectLogs]);

//     // ── Loading State ────────────────────────────────────────────────
//     if (!project) {
//         return (
//             <div className="p-6 space-y-6 animate-pulse">
//                 <div className="h-5 bg-gray-200 dark:bg-gray-800 rounded w-56 mb-8" />
//                 <div className="grid grid-cols-4 gap-4">
//                     {Array.from({ length: 4 }).map((_, i) => (
//                         <div key={i} className="h-24 bg-gray-100 dark:bg-gray-800 rounded-xl" />
//                     ))}
//                 </div>
//                 <div className="h-3 bg-gray-100 dark:bg-gray-800 rounded-full" />
//                 <div className="grid grid-cols-3 gap-6">
//                     <div className="col-span-2 h-64 bg-gray-100 dark:bg-gray-800 rounded-xl" />
//                     <div className="h-64 bg-gray-100 dark:bg-gray-800 rounded-xl" />
//                 </div>
//             </div>
//         );
//     }

//     const projStatus = statusConfig[project.status as keyof typeof statusConfig] || statusConfig.pending;
//     const showSetupPipeline = !isMigrating && !migrationSession &&
//         (stats.total === 0 || (stats.completed === 0 && stats.failed === 0 && stats.inProgress === 0));
//     const analysisSummary = analysisState?.analysis?.summary;
//     const analysisValidation = analysisState?.analysis?.validation;
//     const analysisReadiness = analysisState?.analysis?.migration_readiness_summary;
//     const analysisInventory = analysisState?.analysis?.inventory_summary;
//     const analysisConfidence = analysisState?.analysis?.confidence_breakdown;
//     const analysisGeneration = analysisState?.analysis?.generation_preview;
//     const analysisRisks = analysisState?.analysis?.risk_warnings || [];
//     const analysisFlows = analysisState?.analysis?.structured_flows || [];
//     const analysisCompleted = analysisState?.status === 'completed' && Boolean(analysisState?.analysis);
//     const analysisInFlight = analysisState?.status === 'queued' || analysisState?.status === 'running';
//     const analysisBlocked = Boolean(analysisValidation?.blockers?.length);
//     const canStartMigration = stats.total > 0 && analysisCompleted && !analysisBlocked && analysisConfirmed;

//     // ── SETUP PIPELINE ───────────────────────────────────────────────
//     if (showSetupPipeline) {
//         return (
//             <div className="min-h-full p-6 max-w-3xl mx-auto">
//                 {/* Breadcrumb */}
//                 <nav className="flex items-center gap-2 text-sm text-gray-400 mb-8">
//                     <button onClick={() => router.push('/dashboard/organizations')} className="hover:text-primary-600 transition-colors">Organizations</button>
//                     <ChevronRightIcon className="h-3.5 w-3.5" />
//                     <span className="text-gray-900 dark:text-gray-100 font-medium">{project.name}</span>
//                 </nav>

//                 {/* Project Header */}
//                 <div className="flex items-start gap-4 mb-10">
//                     <div className="w-14 h-14 bg-gradient-to-br from-primary-500 to-primary-700 rounded-2xl flex items-center justify-center shadow-lg shrink-0">
//                         <SparklesIcon className="h-7 w-7 text-white" />
//                     </div>
//                     <div>
//                         <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">{project.name}</h1>
//                         <p className="text-gray-500 dark:text-gray-400 mt-1 text-sm">{project.description}</p>
//                         <div className="flex items-center gap-3 mt-2">
//                             <span className={`px-2.5 py-1 text-xs font-semibold rounded-full ${projStatus.classes}`}>
//                                 {projStatus.label}
//                             </span>
//                             <span className="text-xs text-gray-400 flex items-center gap-1">
//                                 <CalendarDaysIcon className="h-3.5 w-3.5" /> Created {project.createdAt}
//                             </span>
//                         </div>
//                     </div>
//                 </div>

//                 {/* Pipeline Steps */}
//                 <div className="relative">
//                     <div className="absolute left-7 top-14 bottom-14 w-0.5 bg-gradient-to-b from-emerald-500/20 via-primary-500/20 to-gray-500/20 z-0" />
//                     <div className="space-y-6 relative z-10">
//                         {/* Step 1 – Import */}
//                         <div className={`premium-card border-none ${stats.total > 0 ? 'bg-emerald-500/[0.03] border-emerald-500/20' : 'glow-border'}`}>
//                             <div className="flex gap-6">
//                                 <div className={`w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 shadow-lg ${stats.total > 0 ? 'bg-emerald-500 text-white' : 'bg-primary-500 text-white'}`}>
//                                     {stats.total > 0
//                                         ? <CheckCircleIcon className="h-8 w-8" />
//                                         : <CloudArrowUpIcon className="h-8 w-8" />}
//                                 </div>
//                                 <div className="flex-1 min-w-0">
//                                     <div className="flex flex-wrap items-center gap-3 mb-2">
//                                         <h3 className="text-lg font-black tracking-tighter text-gray-900 dark:text-gray-100 uppercase">Step 1: Upload Project</h3>
//                                         {stats.total > 0 && (
//                                             <span className="px-3 py-1 text-[10px] font-black uppercase tracking-widest bg-emerald-500/10 text-emerald-500 rounded-full border border-emerald-500/20">
//                                                 Verified: {stats.total} Nodes
//                                             </span>
//                                         )}
//                                     </div>
//                                     <p className="text-sm text-gray-500 dark:text-gray-500 mb-6 font-medium leading-relaxed">
//                                         Connect your Git architecture or upload MuleSoft XML/RAML archives for neural processing.
//                                     </p>
//                                     <button
//                                         onClick={() => setShowImport(true)}
//                                         className={`inline-flex items-center gap-2 px-5 py-2.5 text-[10px] font-black uppercase tracking-[0.2em] rounded-xl transition-all ${stats.total > 0
//                                             ? 'bg-gray-100 dark:bg-white/5 text-gray-700 dark:text-gray-300 hover:bg-white'
//                                             : 'bg-primary-600 hover:bg-primary-700 text-white shadow-xl shadow-primary-500/20'}`}>
//                                         <ArrowUpTrayIcon className="h-3.5 w-3.5" />
//                                         {stats.total > 0 ? 'Re-index Architecture' : 'Begin Import'}
//                                     </button>
//                                 </div>
//                             </div>
//                         </div>

//                         {/* Step 2 – Migrate */}
//                         <div className={`premium-card border-none ${stats.total === 0
//                             ? 'opacity-40 grayscale pointer-events-none'
//                             : 'glow-border'}`}>
//                             <div className="flex gap-6">
//                                 <div className={`w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 shadow-lg ${stats.total === 0 ? 'bg-gray-200 dark:bg-white/5' : 'bg-violet-600 text-white shadow-violet-500/20'}`}>
//                                     <RocketLaunchIcon className={`h-8 w-8 ${stats.total === 0 ? 'text-gray-400' : 'text-white'}`} />
//                                 </div>
//                                 <div className="flex-1 min-w-0">
//                                     <div className="flex flex-wrap items-center gap-3 mb-2">
//                                         <h3 className="text-lg font-black tracking-tighter text-gray-900 dark:text-gray-100 uppercase">Step 2: Parse + IR Analysis</h3>
//                                         <span className="px-3 py-1 text-[10px] font-black uppercase tracking-widest bg-violet-500/10 text-violet-400 rounded-full border border-violet-500/20">
//                                             Engine: {activeLLMProvider.toUpperCase()}
//                                         </span>
//                                     </div>
//                                     <p className="text-sm text-gray-500 dark:text-gray-500 mb-4 font-medium leading-relaxed">
//                                         Parse source automatically, generate IR, review connector mappings, then confirm the analysis output.
//                                     </p>
//                                     {analysisInFlight && (
//                                         <p className="text-xs font-semibold text-primary-600 dark:text-primary-400 mb-2">
//                                             Parsing in progress ({analysisState?.progressPct || 0}%): {analysisState?.currentStage || 'analyzing'}
//                                         </p>
//                                     )}
//                                     {analysisReadiness && (
//                                         <div className="rounded-lg border border-emerald-300/40 bg-emerald-50/40 dark:bg-emerald-900/10 p-3 mb-3 text-xs space-y-2">
//                                             <p className="font-semibold text-emerald-700 dark:text-emerald-300">Migration Readiness Summary</p>
//                                             <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
//                                                 <div>Flows analyzed: <span className="font-semibold">{analysisReadiness.flows_analyzed}</span></div>
//                                                 <div>Connectors detected: <span className="font-semibold">{listOrNA(analysisReadiness.connectors_detected).join(', ')}</span></div>
//                                                 <div>Complex transformations: <span className="font-semibold">{analysisReadiness.complex_transformations}</span></div>
//                                                 <div>Error handling: <span className="font-semibold">{analysisReadiness.error_handling_present ? 'Present' : 'NA'}</span></div>
//                                                 <div>Custom mapping items: <span className="font-semibold">{analysisReadiness.unsupported_components || 'NA'}</span></div>
//                                                 <div>Confidence: <span className="font-semibold">{Math.round((analysisReadiness.confidence_score || 0) * 100)}%</span></div>
//                                             </div>
//                                             <div className="font-semibold">
//                                                 Migration Readiness: {analysisReadiness.migration_readiness_label}
//                                             </div>
//                                         </div>
//                                     )}
//                                     {analysisInventory && (
//                                         <InventorySummary inventory={analysisInventory} />
//                                     )}
//                                     {analysisConfidence && (
//                                         <div className="rounded-lg border border-gray-200 dark:border-gray-700 p-3 mb-3 text-xs">
//                                             <p className="text-xs font-semibold text-gray-500 mb-2">Confidence</p>
//                                             <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
//                                                 <div>Parsing: <span className="font-semibold">{analysisConfidence.parsing_level} ({Math.round((analysisConfidence.parsing_confidence || 0) * 100)}%)</span></div>
//                                                 <div>Transformation: <span className="font-semibold">{analysisConfidence.transformation_level} ({Math.round((analysisConfidence.transformation_understanding || 0) * 100)}%)</span></div>
//                                                 <div>Overall: <span className="font-semibold">{analysisConfidence.overall_level} ({Math.round((analysisConfidence.overall_confidence || 0) * 100)}%)</span></div>
//                                             </div>
//                                         </div>
//                                     )}
//                                     {analysisFlows.length > 0 && (
//                                         <StructuredFlowSummary flows={analysisFlows} />
//                                     )}
//                                     {(analysisRisks.length > 0 || analysisValidation) && (
//                                         <div className="rounded-lg border border-amber-300/40 bg-amber-50/30 dark:bg-amber-900/10 p-3 mb-3 text-xs">
//                                             <p className="font-semibold text-amber-700 dark:text-amber-300 mb-1">Readiness Suggestions</p>
//                                             <div className="space-y-1 text-gray-700 dark:text-gray-300">
//                                                 {(analysisRisks.length ? analysisRisks : ['Use the inventory as the migration checklist.']).map((risk: string, index: number) => (
//                                                     <div key={`risk-${index}`}>- {risk}</div>
//                                                 ))}
//                                             </div>
//                                         </div>
//                                     )}
//                                     {analysisGeneration && (
//                                         <div className="rounded-lg border border-gray-200 dark:border-gray-700 p-3 mb-3 text-xs">
//                                             <p className="text-xs font-semibold text-gray-500 mb-2">What Will Be Generated</p>
//                                             <div className="space-y-1">
//                                                 {(analysisGeneration.artifacts || []).map((artifact: string, index: number) => (
//                                                     <div key={`artifact-${index}`}>- {artifact}</div>
//                                                 ))}
//                                             </div>
//                                         </div>
//                                     )}
//                                     {analysisSummary && (
//                                         <div className="grid grid-cols-2 gap-2 mb-3 text-xs">
//                                             <div className="rounded-lg border border-gray-200 dark:border-gray-700 p-2">Flows: <span className="font-semibold">{analysisSummary.flows}</span></div>
//                                             <div className="rounded-lg border border-gray-200 dark:border-gray-700 p-2">APIs: <span className="font-semibold">{analysisSummary.apis_detected}</span></div>
//                                             <div className="rounded-lg border border-gray-200 dark:border-gray-700 p-2">Complexity: <span className="font-semibold">{analysisSummary.complexity_score}</span></div>
//                                             <div className="rounded-lg border border-gray-200 dark:border-gray-700 p-2">Estimate: <span className="font-semibold">{analysisSummary.estimated_migration_time}</span></div>
//                                         </div>
//                                     )}
//                                     {analysisValidation?.blockers?.length ? (
//                                         <p className="text-xs text-amber-700 dark:text-amber-300 mb-3">
//                                             Migration action plan: complete the readiness suggestions before launch.
//                                         </p>
//                                     ) : null}
//                                     {analysisError && (
//                                         <p className="text-xs text-rose-600 dark:text-rose-400 mb-3">{analysisError}</p>
//                                     )}
//                                     {stats.total > 0 && (
//                                         <div className="flex flex-wrap items-center gap-3">
//                                             <button
//                                                 onClick={loadLatestAnalysis}
//                                                 disabled={analysisLoading}
//                                                 className="inline-flex items-center gap-2 px-4 py-2 text-[10px] font-black uppercase tracking-[0.2em] bg-gray-100 dark:bg-white/5 text-gray-700 dark:text-gray-300 rounded-xl hover:bg-white disabled:opacity-50"
//                                             >
//                                                 <ArrowPathIcon className="h-3.5 w-3.5" />
//                                                 {analysisLoading ? 'Checking...' : 'Refresh Analysis'}
//                                             </button>
//                                             {analysisCompleted && (
//                                                 <button
//                                                     onClick={toggleRawIr}
//                                                     className="inline-flex items-center gap-2 px-4 py-2 text-[10px] font-black uppercase tracking-[0.2em] bg-gray-100 dark:bg-white/5 text-gray-700 dark:text-gray-300 rounded-xl hover:bg-white"
//                                                 >
//                                                     <FolderIcon className="h-3.5 w-3.5" />
//                                                     {showRawIr ? 'Hide Raw IR' : 'Raw IR'}
//                                                 </button>
//                                             )}
//                                         </div>
//                                     )}
//                                     {showRawIr && (
//                                         <div className="rounded-lg border border-gray-200 dark:border-gray-700 bg-gray-900 text-gray-100 p-3 mt-3 max-h-56 overflow-auto">
//                                             <pre className="text-[11px] whitespace-pre-wrap break-all">{rawIrError ? rawIrError : JSON.stringify(rawIr, null, 2)}</pre>
//                                         </div>
//                                     )}
//                                 </div>
//                             </div>
//                         </div>

//                         {/* Step 3 – Export */}
//                         <div className={`premium-card border-none ${stats.total === 0 ? 'opacity-40 grayscale pointer-events-none' : 'glow-border'}`}>
//                             <div className="flex gap-6">
//                                 <div className={`w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 shadow-lg ${canStartMigration ? 'bg-violet-600 text-white shadow-violet-500/20' : 'bg-gray-200 dark:bg-white/5'}`}>
//                                     <RocketLaunchIcon className={`h-8 w-8 ${canStartMigration ? 'text-white' : 'text-gray-400'}`} />
//                                 </div>
//                                 <div className="flex-1 min-w-0">
//                                     <h3 className="text-lg font-black tracking-tighter text-gray-900 dark:text-gray-100 uppercase mb-2">Step 3: Neural Refactoring</h3>
//                                     <p className="text-sm text-gray-500 dark:text-gray-500 font-medium mb-4">
//                                         Confirm the analysis output, then launch migration.
//                                     </p>
//                                     <label className="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-300 mb-4">
//                                         <input
//                                             type="checkbox"
//                                             disabled={!analysisCompleted || analysisBlocked}
//                                             checked={analysisConfirmed}
//                                             onChange={(e) => setAnalysisConfirmed(e.target.checked)}
//                                         />
//                                         I reviewed the analysis and want to proceed.
//                                     </label>
//                                     <button
//                                         disabled={!canStartMigration}
//                                         className="inline-flex items-center gap-2 px-6 py-3 text-[10px] font-black uppercase tracking-[0.2em] bg-violet-600 hover:bg-violet-700 disabled:bg-gray-300 disabled:text-gray-500 text-white rounded-xl shadow-xl shadow-violet-500/20 transition-all"
//                                     >
//                                         <BoltIcon className="h-4 w-4" />
//                                         Execute Migration
//                                     </button>
//                                 </div>
//                             </div>
//                         </div>
//                     </div>
//                 </div>

//                 {/* Project Config Card */}
//                 <div className="mt-8 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-5">
//                     <h3 className="text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-widest mb-4">Project Configuration</h3>
//                     <div className="grid grid-cols-2 md:grid-cols-4 gap-5">
//                         {[
//                             { label: 'Migration', value: project.migrationType.replace(/-/g, ' → ') },
//                             { label: 'Target', value: project.targetRuntime, capitalize: true },
//                             { label: 'Source', value: project.sourceType, upper: true },
//                             { label: 'AI Engine', value: activeLLMProvider, upper: true },
//                         ].map(item => (
//                             <div key={item.label}>
//                                 <p className="text-xs text-gray-400 mb-1">{item.label}</p>
//                                 <p className={`text-sm font-semibold text-gray-800 dark:text-gray-200 ${item.capitalize ? 'capitalize' : ''} ${item.upper ? 'uppercase' : ''}`}>
//                                     {item.value}
//                                 </p>
//                             </div>
//                         ))}
//                     </div>
//                 </div>

//                 {showImport && (
//                     <ImportPanel onClose={(imported) => {
//                         setShowImport(false);
//                         if (imported) {
//                             refreshFiles(project.id, true);
//                             refreshProjects(project.workspaceId, true);
//                             setTimeout(() => { loadLatestAnalysis(); }, 400);
//                         }
//                     }} />
//                 )}
//             </div>
//         );
//     }

//     // ── ACTIVE DASHBOARD ─────────────────────────────────────────────
//     const statCards = [
//         {
//             label: 'Total Files',
//             value: stats.total,
//             sub: `${stats.pending} pending`,
//             icon: DocumentTextIcon,
//             iconColor: 'text-gray-500',
//             iconBg: 'bg-gray-100 dark:bg-gray-800/50',
//             valueColor: 'text-gray-900 dark:text-gray-100',
//         },
//         {
//             label: 'Migrated',
//             value: stats.completed,
//             sub: `${stats.pct}% complete`,
//             icon: CheckCircleIcon,
//             iconColor: 'text-emerald-500',
//             iconBg: 'bg-emerald-500/10',
//             valueColor: 'text-emerald-500',
//         },
//         {
//             label: 'Failed',
//             value: stats.failed,
//             sub: stats.failed > 0 ? 'needs attention' : 'all clear',
//             icon: XCircleIcon,
//             iconColor: stats.failed > 0 ? 'text-rose-500' : 'text-gray-300',
//             iconBg: stats.failed > 0 ? 'bg-rose-500/10' : 'bg-gray-50 dark:bg-gray-800/50',
//             valueColor: stats.failed > 0 ? 'text-rose-500' : 'text-gray-400',
//         },
//         {
//             label: stats.inProgress > 0 ? 'In Progress' : 'Pending',
//             value: stats.inProgress > 0 ? stats.inProgress : stats.pending,
//             sub: stats.inProgress > 0 ? 'actively running' : 'not started',
//             icon: stats.inProgress > 0 ? ArrowPathIcon : ClockIcon,
//             iconColor: stats.inProgress > 0 ? 'text-primary-500' : 'text-gray-400',
//             iconBg: stats.inProgress > 0 ? 'bg-primary-500/10' : 'bg-gray-50 dark:bg-gray-800/50',
//             valueColor: stats.inProgress > 0 ? 'text-primary-500' : 'text-gray-500',
//         },
//         {
//             label: 'Batch Runs',
//             value: project.migrationRuns ?? 0,
//             sub: (project.migrationRuns ?? 0) === 0 ? 'never run' : (project.migrationRuns ?? 0) === 1 ? '1 batch run' : `${project.migrationRuns} batch runs`,
//             icon: BoltIcon,
//             iconColor: 'text-violet-500',
//             iconBg: 'bg-violet-500/10',
//             valueColor: 'text-violet-500',
//         },
//     ];

//     return (
//         <div className="flex flex-col min-h-full overflow-y-auto bg-gray-50/30 dark:bg-black">
//             {/* ── Page Header ── */}
//             <div className="glass-header px-8 py-5 shrink-0 z-50">
//                 <nav className="flex items-center gap-2 text-[10px] font-black uppercase tracking-[0.15em] text-gray-400 mb-2.5">
//                     <button onClick={() => router.push('/dashboard/organizations')} className="hover:text-primary-600 transition-colors">Organizations</button>
//                     <ChevronRightIcon className="h-3 w-3 text-gray-300" />
//                     <span className="text-gray-600 dark:text-gray-500">{project.name}</span>
//                     <ChevronRightIcon className="h-3 w-3 text-gray-300" />
//                     <span className="text-gray-900 dark:text-gray-100">Control Center</span>
//                 </nav>
//                 <div className="flex items-center justify-between gap-6">
//                     <div className="flex items-center gap-4 min-w-0">
//                         <div className="w-12 h-12 premium-gradient rounded-2xl flex items-center justify-center shadow-2xl shadow-primary-500/20 shrink-0">
//                             <SparklesIcon className="h-6 w-6 text-white" />
//                         </div>
//                         <div className="min-w-0">
//                             <div className="flex items-center gap-3 flex-wrap">
//                                 <h1 className="text-2xl font-black tracking-tighter text-gray-900 dark:text-gray-100 truncate">{project.name}</h1>
//                                 <span className={`px-2.5 py-1 text-[10px] font-black uppercase tracking-wider rounded-full shrink-0 ${projStatus.classes}`}>
//                                     {projStatus.label}
//                                 </span>
//                                 {isMigrating && (
//                                     <span className="flex items-center gap-1.5 px-3 py-1 text-[10px] font-black uppercase tracking-widest rounded-full bg-primary-500/10 text-primary-500 animate-pulse shrink-0 border border-primary-500/20">
//                                         <span className="w-2 h-2 bg-primary-500 rounded-full" /> Live Engine
//                                     </span>
//                                 )}
//                             </div>
//                             <p className="text-sm text-gray-500 dark:text-gray-400 truncate mt-1">Refactoring MuleSoft ESB to Cloud-Native AWS Architecture</p>
//                         </div>
//                     </div>
//                     <div className="flex items-center gap-3 shrink-0">
//                         <button
//                             onClick={() => setShowImport(true)}
//                             className="flex items-center gap-2 px-4 py-2.5 text-xs font-black uppercase tracking-widest text-gray-700 dark:text-gray-300 bg-white/50 dark:bg-white/5 border border-gray-200 dark:border-white/10 rounded-xl hover:bg-white dark:hover:bg-white/10 transition-all">
//                             <ArrowUpTrayIcon className="h-4 w-4" />
//                             <span className="hidden sm:inline">Import</span>
//                         </button>
//                         <button
//                             onClick={() => router.push(`/dashboard/projects/${project.id}/editor`)}
//                             className="flex items-center gap-2 px-5 py-2.5 text-xs font-black uppercase tracking-widest text-white premium-gradient rounded-xl shadow-lg shadow-primary-500/10 hover:shadow-primary-500/20 transition-all">
//                             <CommandLineIcon className="h-4 w-4" />
//                             <span className="hidden sm:inline">Code Lab</span>
//                         </button>
//                     </div>
//                 </div>
//             </div>

//             {/* ── Body ── */}
//             <div className="flex-1 p-8 space-y-8 max-w-[1600px] mx-auto w-full">
//                 {/* Stat Cards */}
//                 <div className="grid grid-cols-2 xl:grid-cols-5 gap-5">
//                     {statCards.map(card => {
//                         const Icon = card.icon;
//                         return (
//                             <div key={card.label} className="premium-card flex flex-col justify-between group">
//                                 <div className="flex items-start justify-between mb-6">
//                                     <p className="text-[10px] font-black text-gray-400 uppercase tracking-[0.2em]">{card.label}</p>
//                                     <div className={`w-10 h-10 rounded-xl flex items-center justify-center shrink-0 transition-transform group-hover:scale-110 ${card.iconBg}`}>
//                                         <Icon className={`h-5 w-5 ${card.iconColor}`} />
//                                     </div>
//                                 </div>
//                                 <div>
//                                     <p className={`text-4xl font-black tracking-tighter mb-1.5 ${card.valueColor}`}>{card.value}</p>
//                                     <p className="text-[10px] font-bold text-gray-400 uppercase tracking-widest">{card.sub}</p>
//                                 </div>
//                             </div>
//                         );
//                     })}
//                 </div>

//                 {/* Main Content Grid */}
//                 <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
//                     {/* Left Column: Progress & Charts */}
//                     <div className="lg:col-span-2 space-y-8">
//                         {/* Progress Panel */}
//                         <div className="premium-card relative overflow-hidden">
//                             <div className="absolute top-0 right-0 w-64 h-64 bg-primary-500/5 blur-[100px] rounded-full -mr-20 -mt-20" />
//                             <div className="flex items-start justify-between mb-8 relative z-10">
//                                 <div>
//                                     <h3 className="text-xl font-black tracking-tighter text-gray-800 dark:text-gray-100">Global Migration Velocity</h3>
//                                     <p className="text-xs font-bold text-gray-400 uppercase tracking-widest mt-1">{stats.completed} of {stats.total} total nodes refactored</p>
//                                 </div>
//                                 <div className="text-right">
//                                     <span className="text-5xl font-black tracking-tighter text-gradient">{stats.pct}</span>
//                                     <span className="text-lg font-black text-gray-300 ml-1">%</span>
//                                 </div>
//                             </div>
//                             <div className="relative h-4 bg-gray-100 dark:bg-white/5 rounded-full overflow-hidden shadow-inner mb-6">
//                                 {stats.total > 0 && (
//                                     <>
//                                         <div className="absolute left-0 top-0 h-full bg-gradient-to-r from-emerald-500 to-emerald-400 transition-all duration-1000 ease-out rounded-full shadow-[0_0_15px_rgba(16,185,129,0.3)]" style={{ width: `${(stats.completed / stats.total) * 100}%` }} />
//                                         {stats.inProgress > 0 && (
//                                             <div className="absolute top-0 h-full bg-primary-400 animate-pulse transition-all duration-1000 ease-out" style={{ left: `${(stats.completed / stats.total) * 100}%`, width: `${(stats.inProgress / stats.total) * 100}%` }} />
//                                         )}
//                                         {stats.failed > 0 && (
//                                             <div className="absolute top-0 h-full bg-rose-500 transition-all duration-1000 ease-out" style={{ left: `${((stats.completed + stats.inProgress) / stats.total) * 100}%`, width: `${(stats.failed / stats.total) * 100}%` }} />
//                                         )}
//                                     </>
//                                 )}
//                             </div>
//                             <div className="flex flex-wrap items-center gap-6 relative z-10">
//                                 <span className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-gray-500">
//                                     <span className="w-2.5 h-2.5 bg-emerald-500 rounded-full shadow-[0_0_8px_rgba(16,185,129,0.5)]" />
//                                     {stats.completed} Success
//                                 </span>
//                                 {stats.inProgress > 0 && (
//                                     <span className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-gray-500">
//                                         <span className="w-2.5 h-2.5 bg-primary-500 rounded-full animate-pulse shadow-[0_0_8px_rgba(14,140,233,0.5)]" />
//                                         {stats.inProgress} Active
//                                     </span>
//                                 )}
//                                 {stats.failed > 0 && (
//                                     <span className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-gray-500">
//                                         <span className="w-2.5 h-2.5 bg-rose-500 rounded-full" />
//                                         {stats.failed} Failed
//                                     </span>
//                                 )}
//                                 <span className="ml-auto flex items-center gap-2 px-3 py-1.5 bg-violet-500/5 border border-violet-500/10 rounded-lg">
//                                     <BoltIcon className="w-3.5 h-3.5 text-violet-500" />
//                                     <span className="text-[10px] font-black uppercase tracking-widest text-violet-500">{project.migrationRuns ?? 0} Cycle{(project.migrationRuns ?? 0) !== 1 ? 's' : ''}</span>
//                                 </span>
//                             </div>
//                         </div>

//                         {/* Distribution Chart */}
//                         <div className="premium-card">
//                             <div className="flex items-center justify-between mb-8">
//                                 <div>
//                                     <h3 className="text-lg font-black tracking-tighter text-gray-800 dark:text-gray-100">Functional Distribution</h3>
//                                     <p className="text-[10px] font-bold text-gray-400 uppercase tracking-widest mt-1">Refactoring status per source domain</p>
//                                 </div>
//                             </div>
//                             {barData.length > 0 ? (
//                                 <ResponsiveContainer width="100%" height={260}>
//                                     <BarChart data={barData} barGap={4} barCategoryGap="25%">
//                                         <defs>
//                                             <linearGradient id="barGradient" x1="0" y1="0" x2="0" y2="1">
//                                                 <stop offset="0%" stopColor="var(--color-primary-400)" />
//                                                 <stop offset="100%" stopColor="var(--color-primary-600)" />
//                                             </linearGradient>
//                                         </defs>
//                                         <XAxis dataKey="name" tick={{ fontSize: 10, fontWeight: 800, fill: '#9ca3af' }} axisLine={false} tickLine={false} />
//                                         <YAxis tick={{ fontSize: 10, fontWeight: 800, fill: '#9ca3af' }} axisLine={false} tickLine={false} width={25} />
//                                         <RechartsTooltip
//                                             contentStyle={{ background: 'rgba(15, 23, 42, 0.9)', border: 'none', borderRadius: '12px', backdropFilter: 'blur(8px)', boxShadow: '0 20px 25px -5px rgba(0,0,0,0.2)' }}
//                                             itemStyle={{ fontSize: '10px', fontWeight: 900, textTransform: 'uppercase', letterSpacing: '0.05em' }}
//                                         />
//                                         <Bar dataKey="completed" name="Refactored" fill="#10b981" radius={[6, 6, 0, 0]} />
//                                         <Bar dataKey="failed" name="Issues" fill="#f43f5e" radius={[6, 6, 0, 0]} />
//                                         <Bar dataKey="pending" name="Backlog" fill="rgba(156, 163, 175, 0.1)" radius={[6, 6, 0, 0]} />
//                                     </BarChart>
//                                 </ResponsiveContainer>
//                             ) : (
//                                 <div className="h-52 flex flex-col items-center justify-center text-gray-300 dark:text-gray-700">
//                                     <FolderIcon className="h-10 w-10 mb-4 opacity-20" />
//                                     <p className="text-[10px] font-black uppercase tracking-widest">No Domain Data</p>
//                                 </div>
//                             )}
//                         </div>
//                     </div>

//                     {/* Right Column: AI & Activity */}
//                     <div className="space-y-8">
//                         {/* Intelligence Hub */}
//                         <div className="premium-card bg-gradient-to-br from-gray-900 to-black text-white border-none shadow-2xl shadow-primary-500/10 overflow-hidden relative">
//                              <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-primary-500 via-violet-500 to-rose-500" />
//                             <div className="flex items-center gap-3 mb-8">
//                                 <div className="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center border border-white/10">
//                                     <CpuChipIcon className="h-5 w-5 text-primary-400" />
//                                 </div>
//                                 <div>
//                                     <h3 className="text-sm font-black uppercase tracking-[0.2em] text-white">Intelligence Hub</h3>
//                                     <p className="text-[9px] font-bold text-gray-500 uppercase tracking-widest">Neural Migration Mapping</p>
//                                 </div>
//                             </div>
//                             <div className="space-y-5">
//                                 {[
//                                     { label: 'Core Engine', value: activeLLMProvider.toUpperCase(), color: 'text-primary-400' },
//                                     { label: 'Architecture', value: project.migrationType.replace(/-/g, ' → '), color: 'text-white' },
//                                     { label: 'Runtime Target', value: project.targetRuntime, capitalize: true, color: 'text-white' },
//                                     { label: 'Source Origin', value: project.sourceType, upper: true, color: 'text-white' },
//                                 ].map(item => (
//                                     <div key={item.label} className="group">
//                                         <p className="text-[9px] font-black text-gray-500 uppercase tracking-widest mb-1.5">{item.label}</p>
//                                         <p className={`text-xs font-black ${item.color} ${item.capitalize ? 'capitalize' : ''} ${item.upper ? 'uppercase' : ''} tracking-wider`}>
//                                             {item.value}
//                                         </p>
//                                     </div>
//                                 ))}
//                             </div>
//                             <div className="mt-8 pt-6 border-t border-white/5 grid grid-cols-2 gap-3">
//                                 <button onClick={() => router.push(`/dashboard/projects/${project.id}/editor`)}
//                                     className="flex items-center justify-center gap-2 px-3 py-2.5 bg-white/5 hover:bg-white/10 text-[9px] font-black uppercase tracking-[0.2em] rounded-xl transition-all border border-white/5">
//                                     <CommandLineIcon className="h-3.5 w-3.5" /> Lab
//                                 </button>
//                                 <button onClick={() => router.push(`/dashboard/projects/${project.id}/history`)}
//                                     className="flex items-center justify-center gap-2 px-3 py-2.5 bg-white/5 hover:bg-white/10 text-[9px] font-black uppercase tracking-[0.2em] rounded-xl transition-all border border-white/5">
//                                     <ClockIcon className="h-3.5 w-3.5" /> Logs
//                                 </button>
//                             </div>
//                         </div>

//                         {/* Activity Feed */}
//                         <div className="premium-card">
//                             <div className="flex items-center justify-between mb-8">
//                                 <h3 className="text-xs font-black uppercase tracking-[0.2em] text-gray-800 dark:text-gray-200">Activity Pulse</h3>
//                                 {recentLogs.length > 0 && (
//                                     <button onClick={() => router.push(`/dashboard/projects/${project.id}/history`)}
//                                         className="text-[10px] font-black uppercase tracking-widest text-primary-500 hover:text-primary-600">
//                                         History →
//                                     </button>
//                                 )}
//                             </div>
//                             {recentLogs.length === 0 ? (
//                                 <div className="py-12 text-center">
//                                     <div className="relative mb-4">
//                                         <ClockIcon className="h-10 w-10 text-gray-100 dark:text-gray-800 mx-auto" />
//                                         <div className="absolute inset-0 bg-primary-500/5 blur-2xl rounded-full" />
//                                     </div>
//                                     <p className="text-[10px] font-black uppercase tracking-widest text-gray-400">System Idle</p>
//                                     <p className="text-[9px] font-bold text-gray-300 dark:text-gray-700 mt-1 uppercase">Awaiting migration sequence</p>
//                                 </div>
//                             ) : (
//                                 <div className="space-y-6">
//                                     {recentLogs.map((log, i) => (
//                                         <div key={log.id} className="relative flex gap-4">
//                                             {i < recentLogs.length - 1 && (
//                                                 <div className="absolute left-[11px] top-8 bottom-[-24px] w-px bg-gray-100 dark:bg-white/5" />
//                                             )}
//                                             <div className={`w-6 h-6 rounded-lg flex items-center justify-center shrink-0 z-10 ${
//                                                 log.status === 'success' ? 'bg-emerald-500/10 border border-emerald-500/20' :
//                                                 log.status === 'error' ? 'bg-rose-500/10 border border-rose-500/20' :
//                                                 'bg-gray-100 dark:bg-white/10'
//                                             }`}>
//                                                 {log.status === 'success' ? <CheckSolid className="h-3 w-3 text-emerald-500" />
//                                                     : log.status === 'error' ? <XSolid className="h-3 w-3 text-rose-500" />
//                                                     : <ClockIcon className="h-3 w-3 text-gray-400" />}
//                                             </div>
//                                             <div className="flex-1 min-w-0">
//                                                 <p className="text-[10px] font-black text-gray-800 dark:text-gray-200 uppercase tracking-widest truncate">{log.fileName}</p>
//                                                 <p className="text-[9px] font-bold text-gray-500 uppercase tracking-tighter mt-1 line-clamp-1">{log.message}</p>
//                                             </div>
//                                         </div>
//                                     ))}
//                                 </div>
//                             )}
//                         </div>
//                     </div>
//                 </div>
//             </div>

//             {showImport && (
//                 <ImportPanel onClose={(imported) => {
//                     setShowImport(false);
//                     if (imported) {
//                         refreshFiles(project.id, true);
//                         refreshProjects(project.workspaceId, true);
//                     }
//                 }} />
//             )}
//         </div>
//     );
// }
