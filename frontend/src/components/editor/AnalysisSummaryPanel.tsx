'use client';

import React, { useState, useMemo, useRef } from 'react';
import { useVirtualizer } from '@tanstack/react-virtual';
import type { AnalysisInventorySummary, StructuredFlow } from '@/lib/types';
import {
    DocumentTextIcon,
    BoltIcon,
    CircleStackIcon,
    CodeBracketIcon,
    KeyIcon,
    ShieldExclamationIcon,
    BeakerIcon,
    ChevronDownIcon,
    ChevronRightIcon,
    FunnelIcon,
    CpuChipIcon,
    ExclamationTriangleIcon,
} from '@heroicons/react/24/outline';

// ─── Helpers ─────────────────────────────────────────────────────────────────
const val = (v: unknown): string => {
    if (v === null || v === undefined) return 'NA';
    const s = String(v).trim();
    return s === '' || s.toLowerCase() === 'na' ? 'NA' : s;
};

// ─── Micro Components ─────────────────────────────────────────────────────────
const Tag: React.FC<{ children: React.ReactNode; color?: string }> = ({
    children, color = 'bg-gray-100 text-gray-700 border-gray-200',
}) => (
    <span className={`inline-flex items-center px-2.5 py-1 text-[9px] font-black uppercase tracking-widest rounded-md border ${color}`}>
        {children}
    </span>
);

const FlowTag = ({ type }: { type: string }) => {
    const cfg: Record<string, string> = {
        'flow':     'bg-violet-50 text-violet-700 border-violet-200',
        'sub-flow': 'bg-sky-50 text-sky-700 border-sky-200',
        'batch':    'bg-amber-50 text-amber-700 border-amber-200',
        'private':  'bg-slate-100 text-slate-700 border-slate-200',
    };
    return <Tag color={cfg[type] || cfg['flow']}>{type}</Tag>;
};

const EmptyState: React.FC<{ icon: React.ElementType; message: string; sub?: string }> = ({
    icon: Icon, message, sub,
}) => (
    <div className="flex flex-col items-center justify-center py-10 gap-3">
        <div className="w-12 h-12 rounded-2xl bg-white/60 border border-white/70 flex items-center justify-center">
            <Icon className="h-6 w-6 text-slate-400" />
        </div>
        <div className="text-center">
            <p className="text-[10px] font-black uppercase tracking-widest text-slate-700">{message}</p>
            {sub && <p className="text-[10px] text-slate-500 mt-1">{sub}</p>}
        </div>
    </div>
);

function VirtualRows<T>({ items, rowHeight, maxHeight, renderRow }: {
    items: T[];
    rowHeight: number;
    maxHeight: number;
    renderRow: (item: T, index: number) => React.ReactNode;
}) {
    const height = Math.min(maxHeight, Math.max(rowHeight * 2, items.length * rowHeight));
    const parentRef = useRef<HTMLDivElement | null>(null);
    const rowVirtualizer = useVirtualizer({
        count: items.length,
        getScrollElement: () => parentRef.current,
        estimateSize: () => rowHeight,
        overscan: 8,
    });
    return (
        <div ref={parentRef} style={{ height, width: '100%', overflowY: 'auto' }}>
            <div style={{ height: `${rowVirtualizer.getTotalSize()}px`, width: '100%', position: 'relative' }}>
                {rowVirtualizer.getVirtualItems().map(virtualRow => (
                    <div
                        key={virtualRow.key}
                        style={{
                            position: 'absolute',
                            top: 0,
                            left: 0,
                            width: '100%',
                            transform: `translateY(${virtualRow.start}px)`,
                        }}
                    >
                        {renderRow(items[virtualRow.index], virtualRow.index)}
                    </div>
                ))}
            </div>
        </div>
    );
}

// ─── Quick Summary Cards (top of panel) ──────────────────────────────────────
const QuickSummaryCards: React.FC<{
    inventory: AnalysisInventorySummary;
    structuredFlows: StructuredFlow[];
}> = ({ inventory, structuredFlows }) => {
    const totalFlows      = inventory.flows?.length ?? 0;
    const totalConnectors = inventory.connectors?.length ?? 0;
    const totalTransforms = inventory.dataweave_transformations?.length ?? 0;
    const totalConfigs    = inventory.mule_configuration_files?.length ?? 0;

    const totalAPIs = (structuredFlows || []).filter(sf =>
        (sf.trigger || sf.source || '').toLowerCase().includes('http')
    ).length;

    const errorItems = inventory.error_handling_and_logging || [];
    const warnings   = errorItems.filter(r =>
        (r as Record<string, unknown>).error_handling === 'NA'
    ).length;

    // Unique files across all inventory sources
    const allFiles = new Set<string>([
        ...(inventory.mule_configuration_files || []),
        ...(inventory.flows || []).map(f => val((f as Record<string, unknown>).file)).filter(v => v !== 'NA'),
        ...(inventory.connectors || []).map(c => val((c as Record<string, unknown>).file)).filter(v => v !== 'NA'),
        ...(inventory.properties_used || []).map(p => val((p as Record<string, unknown>).defined_in_file)).filter(v => v !== 'NA'),
    ]);
    const totalFiles = allFiles.size || totalConfigs;

    const cards = [
        { label: 'Total Files',  value: totalFiles,     color: 'text-sky-800',     bg: 'bg-sky-50/80    border-sky-200/80'      },
        { label: 'Flows',        value: totalFlows,     color: 'text-violet-800',  bg: 'bg-violet-50/80 border-violet-200/80'   },
        { label: 'APIs',         value: totalAPIs,      color: 'text-indigo-800',  bg: 'bg-indigo-50/80 border-indigo-200/80'   },
        { label: 'Connectors',   value: totalConnectors,color: 'text-indigo-800',  bg: 'bg-indigo-50/80 border-indigo-200/80'   },
        { label: 'Configs',      value: totalConfigs,   color: 'text-amber-800',   bg: 'bg-amber-50/80  border-amber-200/80'    },
        { label: 'Transforms',   value: totalTransforms,color: 'text-orange-800',  bg: 'bg-orange-50/80 border-orange-200/80'   },
        {
            label: 'Warnings', value: warnings,
            color: warnings > 0 ? 'text-rose-700' : 'text-slate-600',
            bg:    warnings > 0 ? 'bg-rose-50/80 border-rose-200/80' : 'bg-white/60 border-white/70',
        },
    ];

    return (
        <div className="grid grid-cols-4 sm:grid-cols-7 gap-2">
            {cards.map(c => (
                <div key={c.label} className={`rounded-xl border ${c.bg} px-2 py-2.5 text-center shadow-sm`}>
                    <p className={`text-[8px] font-black uppercase tracking-widest mb-0.5 ${c.color}`}>{c.label}</p>
                    <p className={`text-xl font-black ${c.color}`}>{c.value}</p>
                </div>
            ))}
        </div>
    );
};

// ─── SECTION 1: Config Files — file names + type breakdown ────────────────────
const S1_ConfigFiles: React.FC<{ files: string[] }> = ({ files }) => {
    if (!files?.length) return <EmptyState icon={DocumentTextIcon} message="No configuration files detected" />;

    const grouped = files.reduce<Record<string, string[]>>((acc, f) => {
        const ext = (f.split('.').pop() || 'other').toLowerCase();
        const key = ext === 'xml' ? 'XML' : (ext === 'yaml' || ext === 'yml') ? 'YAML' : ext === 'properties' ? 'Properties' : 'Other';
        (acc[key] = acc[key] || []).push(f);
        return acc;
    }, {});

    return (
        <div className="space-y-4">
            {/* File type breakdown */}
            <div className="flex flex-wrap gap-2">
                {Object.entries(grouped).map(([type, fls]) => (
                    <div key={type} className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-sky-50 border border-sky-100">
                        <span className="text-[9px] font-black uppercase tracking-widest text-sky-700">{type} Files</span>
                        <span className="text-[14px] font-black text-sky-600">{fls.length}</span>
                    </div>
                ))}
            </div>

            {/* Flat clean file list */}
            <VirtualRows
                items={files}
                rowHeight={40}
                maxHeight={320}
                renderRow={(f) => (
                    <div key={f} className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-white/80 border border-white/80 font-mono text-[10px] text-slate-700 shadow-sm hover:border-sky-200 hover:bg-sky-50/70 transition-colors">
                        <DocumentTextIcon className="h-3.5 w-3.5 text-sky-500 shrink-0" />
                        <span className="break-all">{f}</span>
                    </div>
                )}
            />
        </div>
    );
};

// ─── SECTION 2: Flows — compact cards (name, description, trigger, count) ─────
const S2_Flows: React.FC<{
    flows: AnalysisInventorySummary['flows'];
    flowTypeCounts: Record<string, number>;
    structuredFlows: StructuredFlow[];
}> = ({ flows, flowTypeCounts, structuredFlows }) => {
    const [filter, setFilter] = useState<string>('all');

    const structuredByName = useMemo(() => {
        const m: Record<string, StructuredFlow> = {};
        (structuredFlows || []).forEach(sf => { m[sf.flow_name] = sf; });
        return m;
    }, [structuredFlows]);

    if (!flows?.length) return <EmptyState icon={BoltIcon} message="No flows detected" />;

    const filtered = filter === 'all' ? flows : flows.filter(f => (f.type || 'flow') === filter);

    return (
        <div className="space-y-4">
            {/* Flow type filter */}
            <div className="grid grid-cols-3 gap-2">
                {Object.entries(flowTypeCounts || {}).map(([type, count]) => (
                    <button
                        key={type}
                        onClick={() => setFilter(filter === type ? 'all' : type)}
                        className={`rounded-xl border p-2.5 text-center transition-all ${
                            filter === type
                                ? 'border-violet-300 bg-violet-50 shadow-sm'
                                : 'border-white/70 bg-white/60 hover:border-violet-200 hover:bg-violet-50/60'
                        }`}
                    >
                        <p className={`text-[9px] font-black uppercase tracking-widest mb-0.5 ${filter === type ? 'text-violet-700' : 'text-slate-500'}`}>{type}</p>
                        <p className={`text-xl font-black ${filter === type ? 'text-violet-700' : 'text-slate-950'}`}>{count}</p>
                    </button>
                ))}
            </div>

            {filter !== 'all' && (
                <div className="flex items-center gap-2">
                    <FunnelIcon className="h-3 w-3 text-violet-600" />
                    <span className="text-[9px] font-black uppercase tracking-widest text-violet-700">Showing {filter} flows</span>
                    <button onClick={() => setFilter('all')} className="text-[9px] font-semibold text-slate-500 hover:text-slate-900 ml-auto">Show all</button>
                </div>
            )}

            {/* Compact flow list — name, description, trigger, component count only */}
            <VirtualRows
                items={filtered}
                rowHeight={96}
                maxHeight={460}
                renderRow={(flow) => {
                    const sf  = structuredByName[val(flow.name)];
                    const trigger        = val(sf?.trigger || sf?.source);
                    const componentCount = sf?.step_details?.length ?? 0;
                    const description    = val(flow.high_level);

                    return (
                        <div key={val(flow.name)} className="rounded-xl border border-violet-100/80 bg-white/80 px-4 py-3 shadow-sm">
                            <div className="flex items-start gap-3">
                                <div className="shrink-0 pt-0.5">
                                    <FlowTag type={flow.type || 'flow'} />
                                </div>
                                <div className="flex-1 min-w-0">
                                    <p className="text-[11px] font-black text-slate-950 truncate">{val(flow.name)}</p>
                                    {description !== 'NA' && (
                                        <p className="text-[10px] text-slate-600 mt-0.5 leading-relaxed line-clamp-2">{description}</p>
                                    )}
                                    <div className="flex items-center gap-4 mt-1.5 flex-wrap">
                                        {trigger !== 'NA' && (
                                            <span className="text-[9px] font-semibold text-gray-400">
                                                Trigger: <span className="text-gray-700">{trigger}</span>
                                            </span>
                                        )}
                                        {componentCount > 0 && (
                                            <span className="text-[9px] font-semibold text-gray-400">
                                                Components: <span className="text-gray-700">{componentCount}</span>
                                            </span>
                                        )}
                                    </div>
                                </div>
                            </div>
                        </div>
                    );
                }}
            />
        </div>
    );
};

// ─── SECTION 3: Connectors — name + usage count only ─────────────────────────
const S3_Connectors: React.FC<{ connectors: AnalysisInventorySummary['connectors'] }> = ({ connectors }) => {
    if (!connectors?.length) return <EmptyState icon={CircleStackIcon} message="No connectors detected" />;

    const byType = connectors.reduce<Record<string, number>>((acc, c) => {
        const t = val(c.connector_type as unknown);
        acc[t] = (acc[t] || 0) + 1;
        return acc;
    }, {});

    const byName = connectors.reduce<Record<string, { type: string; count: number }>>((acc, c) => {
        const name = val(c.name as unknown);
        const type = val(c.connector_type as unknown);
        if (!acc[name]) acc[name] = { type, count: 0 };
        acc[name].count++;
        return acc;
    }, {});

    return (
        <div className="space-y-4">
            {/* Type pills */}
            <div className="flex flex-wrap gap-2">
                {Object.entries(byType).map(([type, count]) => (
                    <div key={type} className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-indigo-50 border border-indigo-100">
                        <span className="text-[9px] font-black uppercase tracking-widest text-indigo-700">{type}</span>
                        <span className="text-[14px] font-black text-indigo-600">{count}</span>
                    </div>
                ))}
            </div>

            {/* Connector name + usage count — no connection details */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                {Object.entries(byName).map(([name, { type, count }]) => (
                    <div key={name} className="flex items-center justify-between rounded-xl border border-indigo-100 bg-white/80 px-4 py-3 shadow-sm">
                        <div className="flex items-center gap-2.5 min-w-0">
                            <div className="w-6 h-6 rounded-md bg-indigo-50 border border-indigo-200 flex items-center justify-center shrink-0">
                                <CircleStackIcon className="h-3 w-3 text-indigo-600" />
                            </div>
                            <div className="min-w-0">
                                <p className="text-[11px] font-black text-slate-950 truncate">{name}</p>
                                <p className="text-[9px] text-slate-500">{type}</p>
                            </div>
                        </div>
                        <Tag color="bg-indigo-50 text-indigo-700 border-indigo-200">Used {count}×</Tag>
                    </div>
                ))}
            </div>
        </div>
    );
};

// ─── SECTION 4: DataWeave — count + transformation types only ─────────────────
const S4_DataWeave: React.FC<{ items: AnalysisInventorySummary['dataweave_transformations'] }> = ({ items }) => {
    if (!items?.length) return <EmptyState icon={CodeBracketIcon} message="No DataWeave transformations detected" />;

    const uniqueFlows = new Set(
        items.map(item => val((item as Record<string, unknown>).flow)).filter(v => v !== 'NA')
    );

    // Extract human-readable transformation types from expression field
    const typeCounts = items.reduce<Record<string, number>>((acc, item) => {
        const row = item as Record<string, unknown>;
        const expr = val(row.transformation);
        let label  = 'DataWeave Script';

        if (expr !== 'NA') {
            const arrow = expr.match(/(\w[\w\s]*?)\s*[-–—>→]+\s*([\w][\w\s]*)/);
            if (arrow) {
                label = `${arrow[1].trim()} → ${arrow[2].trim()}`;
            } else if (expr.toLowerCase().includes('json'))  label = 'JSON Transform';
            else if (expr.toLowerCase().includes('xml'))     label = 'XML Transform';
            else if (expr.toLowerCase().includes('csv'))     label = 'CSV Transform';
        }
        acc[label] = (acc[label] || 0) + 1;
        return acc;
    }, {});

    return (
        <div className="space-y-4">
            {/* Stats */}
            <div className="grid grid-cols-2 gap-3">
                <div className="rounded-xl border border-amber-200 bg-amber-50 p-4 text-center shadow-sm">
                    <p className="text-[9px] font-black uppercase tracking-widest text-amber-700 mb-1">Total Transformations</p>
                    <p className="text-3xl font-black text-amber-700">{items.length}</p>
                </div>
                <div className="rounded-xl border border-white/80 bg-white/75 p-4 text-center shadow-sm">
                    <p className="text-[9px] font-black uppercase tracking-widest text-slate-500 mb-1">Across Flows</p>
                    <p className="text-3xl font-black text-slate-950">{uniqueFlows.size}</p>
                </div>
            </div>

            {/* Transformation types breakdown — no scripts/expressions */}
            <div>
                <p className="text-[8px] font-black uppercase tracking-widest text-slate-500 mb-2 px-1">Transformation Types</p>
                <div className="flex flex-wrap gap-2">
                    {Object.entries(typeCounts).map(([type, count]) => (
                        <div key={type} className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-amber-50 border border-amber-100">
                            <span className="text-[9px] font-bold text-amber-800">{type}</span>
                            <span className="text-[11px] font-black text-amber-700">{count}</span>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

// ─── SECTION 5: Properties — config file names only (no keys/values/secrets) ──
const S5_Properties: React.FC<{ items: AnalysisInventorySummary['properties_used'] }> = ({ items }) => {
    if (!items?.length) return <EmptyState icon={KeyIcon} message="No properties detected" />;

    const secureCount = items.filter(p => (p as Record<string, unknown>).secure).length;

    const configFiles = [...new Set(
        items
            .map(p => val((p as Record<string, unknown>).defined_in_file))
            .filter(v => v !== 'NA')
    )];

    return (
        <div className="space-y-4">
            {/* Stats */}
            <div className="grid grid-cols-2 gap-3">
                <div className="rounded-xl border border-white/80 bg-white/75 p-4 text-center shadow-sm">
                    <p className="text-[9px] font-black uppercase tracking-widest text-slate-500 mb-1">Total Properties</p>
                    <p className="text-3xl font-black text-slate-950">{items.length}</p>
                </div>
                <div className="rounded-xl border border-rose-200 bg-rose-50 p-4 text-center shadow-sm">
                    <p className="text-[9px] font-black uppercase tracking-widest text-rose-700 mb-1">Secure / Masked</p>
                    <p className="text-3xl font-black text-rose-700">{secureCount}</p>
                </div>
            </div>

            {/* Configuration file names only — no property keys/values */}
            <div>
                <p className="text-[8px] font-black uppercase tracking-widest text-slate-500 mb-2 px-1">Configuration Files</p>
                {configFiles.length > 0 ? (
                    <div className="space-y-1.5">
                        {configFiles.map(f => (
                            <div key={f} className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-white/80 border border-white/80 font-mono text-[10px] text-slate-700 shadow-sm">
                                <KeyIcon className="h-3.5 w-3.5 text-rose-400 shrink-0" />
                                <span className="break-all">{f}</span>
                            </div>
                        ))}
                    </div>
                ) : (
                    <p className="text-[10px] text-gray-400 px-1">No configuration files found.</p>
                )}
            </div>
        </div>
    );
};

// ─── SECTION 6: Error Handling — coverage summary only (no per-flow detail) ───
const S6_ErrorHandling: React.FC<{ items: AnalysisInventorySummary['error_handling_and_logging'] }> = ({ items }) => {
    if (!items?.length) return <EmptyState icon={ShieldExclamationIcon} message="No error handling data detected" />;

    const withHandlers = items.filter(r => (r as Record<string, unknown>).error_handling !== 'NA');
    const withLogging  = items.filter(r => {
        const logs = (r as Record<string, unknown>).logging;
        return Array.isArray(logs) && logs.length > 0;
    });
    const total    = items.length;
    const coverage = total > 0 ? Math.round((withHandlers.length / total) * 100) : 0;
    const missing  = total - withHandlers.length;
    const barColor = coverage >= 80 ? 'bg-indigo-500' : coverage >= 50 ? 'bg-amber-500' : 'bg-rose-500';
    const txtColor = coverage >= 80 ? 'text-indigo-600' : coverage >= 50 ? 'text-amber-600' : 'text-rose-600';

    return (
        <div className="space-y-4">
            {/* Coverage card */}
            <div className="rounded-xl border border-white/80 bg-white/75 p-4 space-y-4 shadow-sm">
                <div className="flex justify-between items-center">
                    <span className="text-[9px] font-black uppercase tracking-widest text-slate-500">Error Handler Coverage</span>
                    <span className={`text-xl font-black ${txtColor}`}>{coverage}%</span>
                </div>
                <div className="h-2 rounded-full bg-gray-100 overflow-hidden">
                    <div className={`h-full ${barColor} rounded-full transition-all`} style={{ width: `${coverage}%` }} />
                </div>
                <div className="grid grid-cols-3 gap-2">
                    {[
                        { label: 'Total Flows',   value: total,               color: 'text-slate-950'   },
                        { label: 'With Handlers', value: withHandlers.length, color: 'text-indigo-600' },
                        { label: 'With Logging',  value: withLogging.length,  color: 'text-sky-600'     },
                    ].map(stat => (
                        <div key={stat.label} className="text-center">
                            <p className={`text-lg font-black ${stat.color}`}>{stat.value}</p>
                            <p className="text-[8px] font-black uppercase tracking-widest text-slate-500">{stat.label}</p>
                        </div>
                    ))}
                </div>
            </div>

            {/* Warning notice */}
            {missing > 0 && (
                <div className="rounded-xl border border-rose-200 bg-rose-50 px-4 py-3 flex items-start gap-3">
                    <ExclamationTriangleIcon className="h-4 w-4 text-rose-500 shrink-0 mt-0.5" />
                    <div>
                        <p className="text-[10px] font-black text-rose-700">
                            {missing} flow{missing !== 1 ? 's' : ''} missing error handlers
                        </p>
                        <p className="text-[9px] text-rose-500 mt-0.5">Consider adding error handling before migration.</p>
                    </div>
                </div>
            )}
        </div>
    );
};

// ─── SECTION 7: MUnit Tests — stat summary + file list ───────────────────────
const S7_MUnit: React.FC<{ tests: AnalysisInventorySummary['munit_test_cases'] }> = ({ tests }) => {
    if (!tests?.length) return (
        <EmptyState
            icon={BeakerIcon}
            message="No MUnit test cases found"
            sub="Consider adding MUnit test suites before migration to validate behavior parity."
        />
    );

    const byFile = tests.reduce<Record<string, number>>((acc, t) => {
        const k = val((t as Record<string, unknown>).file) || 'Unknown File';
        acc[k] = (acc[k] || 0) + 1;
        return acc;
    }, {});

    const totalAssertions = tests.reduce((sum, t) => {
        const r = t as Record<string, unknown>;
        return sum + (Array.isArray(r.assertions) ? r.assertions.length : 0);
    }, 0);

    return (
        <div className="space-y-4">
            {/* Stat summary */}
            <div className="grid grid-cols-3 gap-3">
                {[
                    { label: 'Test Cases', value: tests.length,                color: 'text-sky-700'    },
                    { label: 'Test Files', value: Object.keys(byFile).length,  color: 'text-sky-600'    },
                    { label: 'Assertions', value: totalAssertions,             color: 'text-violet-600' },
                ].map(s => (
                    <div key={s.label} className="rounded-xl border border-white/80 bg-white/75 p-4 text-center shadow-sm">
                        <p className={`text-[9px] font-black uppercase tracking-widest mb-1 ${s.color}`}>{s.label}</p>
                        <p className={`text-2xl font-black ${s.color}`}>{s.value}</p>
                    </div>
                ))}
            </div>

            {/* Test file list with counts — no per-test assertions */}
            <div>
                <p className="text-[8px] font-black uppercase tracking-widest text-slate-500 mb-2 px-1">Test Files</p>
                <div className="space-y-1.5">
                    {Object.entries(byFile).map(([file, count]) => (
                        <div key={file} className="flex items-center justify-between rounded-xl border border-sky-100/80 bg-white/75 px-4 py-3 shadow-sm">
                            <div className="flex items-center gap-2.5 min-w-0">
                                <BeakerIcon className="h-3.5 w-3.5 text-sky-600 shrink-0" />
                                <span className="text-[10px] font-mono text-slate-700 truncate">{file}</span>
                            </div>
                            <Tag color="bg-sky-50 text-sky-700 border-sky-200">
                                {count} test{count !== 1 ? 's' : ''}
                            </Tag>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

// ─── Collapsible Row (kept for future use) ────────────────────────────────────
export const CollapsibleRow: React.FC<{
    title: React.ReactNode;
    children: React.ReactNode;
    defaultOpen?: boolean;
    accent?: string;
}> = ({ title, children, defaultOpen = false, accent = 'border-white/70' }) => {
    const [open, setOpen] = useState(defaultOpen);
    return (
        <div className={`border ${accent} rounded-xl overflow-hidden bg-white/75 shadow-sm backdrop-blur-sm`}>
            <button onClick={() => setOpen(o => !o)} className="w-full flex items-center gap-3 px-4 py-3.5 bg-white/60 hover:bg-white/80 transition-colors text-left">
                <span className="flex-1 flex items-center gap-2.5 min-w-0">{title}</span>
                {open ? <ChevronDownIcon className="h-3.5 w-3.5 text-gray-400 shrink-0" /> : <ChevronRightIcon className="h-3.5 w-3.5 text-gray-400 shrink-0" />}
            </button>
            {open && <div className="px-4 pt-4 pb-5 bg-white/45 border-t border-white/70">{children}</div>}
        </div>
    );
};

// ─── Main Component ───────────────────────────────────────────────────────────
const TABS = [
    { id: 'config',     label: 'Config Files',   icon: DocumentTextIcon,      color: 'text-sky-600',     active: 'border-sky-500 text-sky-700 bg-sky-50'          },
    { id: 'flows',      label: 'Flows',           icon: BoltIcon,              color: 'text-violet-600',  active: 'border-violet-500 text-violet-700 bg-violet-50'  },
    { id: 'connectors', label: 'Connectors',      icon: CircleStackIcon,       color: 'text-indigo-600',  active: 'border-indigo-500 text-indigo-700 bg-indigo-50/85'},
    { id: 'dataweave',  label: 'DataWeave',       icon: CodeBracketIcon,       color: 'text-amber-600',   active: 'border-amber-500 text-amber-700 bg-amber-50'     },
    { id: 'properties', label: 'Properties',      icon: KeyIcon,               color: 'text-rose-600',    active: 'border-rose-500 text-rose-700 bg-rose-50'        },
    { id: 'errors',     label: 'Error & Logging', icon: ShieldExclamationIcon, color: 'text-orange-600',  active: 'border-orange-500 text-orange-700 bg-orange-50'  },
    { id: 'munit',      label: 'MUnit Tests',     icon: BeakerIcon,            color: 'text-sky-600',     active: 'border-sky-500 text-sky-700 bg-sky-50/85'        },
] as const;

type TabId = typeof TABS[number]['id'];

interface Props {
    inventory: AnalysisInventorySummary;
    structuredFlows: StructuredFlow[];
    summary?: unknown;
    warningCount?: number;
}

export default function AnalysisSummaryPanel({ inventory, structuredFlows }: Props) {
    const [tab, setTab] = useState<TabId>('config');

    const counts: Record<TabId, number> = {
        config:     inventory.mule_configuration_files?.length ?? 0,
        flows:      inventory.flows?.length ?? 0,
        connectors: inventory.connectors?.length ?? 0,
        dataweave:  inventory.dataweave_transformations?.length ?? 0,
        properties: inventory.properties_used?.length ?? 0,
        errors:     inventory.error_handling_and_logging?.length ?? 0,
        munit:      inventory.munit_test_cases?.length ?? 0,
    };

    return (
        <div className="flex flex-col rounded-xl border border-white/50 bg-transparent shadow-none overflow-hidden">

            {/* Header + Quick Summary Cards */}
            <div className="px-4 sm:px-5 py-4 border-b border-white/50 space-y-4 shrink-0 bg-white/35 backdrop-blur-md">
                <div className="flex flex-wrap items-center gap-3">
                    <div className="w-9 h-9 rounded-lg bg-white/60 border border-violet-200/80 flex items-center justify-center shadow-sm">
                        <CpuChipIcon className="h-4 w-4 text-violet-600" />
                    </div>
                    <div>
                        <h3 className="text-sm font-black uppercase tracking-[0.15em] text-slate-950">Quick Project Scan</h3>
                        <p className="text-[9px] text-slate-600 uppercase tracking-widest font-bold mt-0.5">MuleSoft project overview</p>
                    </div>
                </div>
                <QuickSummaryCards inventory={inventory} structuredFlows={structuredFlows || []} />
            </div>

            {/* Tab bar */}
            <div className="flex gap-2 border-b border-white/50 overflow-x-auto scrollbar-hide shrink-0 bg-white/25 px-4 py-2.5 backdrop-blur-sm">
                {TABS.map(t => {
                    const Icon    = t.icon;
                    const isActive = tab === t.id;
                    const count   = counts[t.id];
                    return (
                        <button
                            key={t.id}
                            onClick={() => setTab(t.id)}
                            className={`flex items-center gap-2 px-3 py-1.5 text-[9px] font-black uppercase tracking-widest whitespace-nowrap border rounded-lg transition-all shrink-0 ${
                                isActive
                                    ? `${t.active} shadow-sm`
                                    : 'border-white/70 bg-white/55 text-slate-600 hover:text-slate-900 hover:border-indigo-200 hover:bg-white/80'
                            }`}
                        >
                            <Icon className={`h-3.5 w-3.5 ${isActive ? '' : t.color}`} />
                            <span className="hidden sm:inline">{t.label}</span>
                            {count > 0 && (
                                <span className={`px-1.5 py-0.5 rounded text-[8px] font-black ${
                                    isActive ? 'bg-white/70 text-current' : 'bg-white/70 text-slate-600'
                                }`}>
                                    {count}
                                </span>
                            )}
                        </button>
                    );
                })}
            </div>

            {/* Tab content */}
            <div className="flex-1 overflow-y-auto p-4 sm:p-5 max-h-[420px] space-y-4 bg-transparent">
                {tab === 'config'     && <S1_ConfigFiles   files={inventory.mule_configuration_files || []} />}
                {tab === 'flows'      && <S2_Flows          flows={inventory.flows || []} flowTypeCounts={inventory.flow_type_counts || {}} structuredFlows={structuredFlows || []} />}
                {tab === 'connectors' && <S3_Connectors     connectors={inventory.connectors || []} />}
                {tab === 'dataweave'  && <S4_DataWeave      items={inventory.dataweave_transformations || []} />}
                {tab === 'properties' && <S5_Properties     items={inventory.properties_used || []} />}
                {tab === 'errors'     && <S6_ErrorHandling  items={inventory.error_handling_and_logging || []} />}
                {tab === 'munit'      && <S7_MUnit           tests={inventory.munit_test_cases || []} />}
            </div>
        </div>
    );
}









// 'use client';

// import React, { useMemo } from 'react';
// import type { AnalysisInventorySummary, StructuredFlow } from '@/lib/types';
// import {
//     ArrowPathIcon,
//     BeakerIcon,
//     BoltIcon,
//     CircleStackIcon,
//     CodeBracketIcon,
//     CpuChipIcon,
//     DocumentTextIcon,
//     ExclamationTriangleIcon,
//     KeyIcon,
//     ShieldExclamationIcon,
//     SparklesIcon,
//     Squares2X2Icon,
// } from '@heroicons/react/24/outline';

// type SummaryLike = {
//     flows?: number;
//     apis_detected?: number;
//     transformations?: number;
// };

// interface Props {
//     inventory: AnalysisInventorySummary;
//     structuredFlows: StructuredFlow[];
//     summary?: SummaryLike;
//     warningCount?: number;
// }

// const text = (value: unknown): string => {
//     const next = String(value ?? '').trim();
//     return next && next.toLowerCase() !== 'na' ? next : 'NA';
// };

// const asList = (value: unknown): string[] => {
//     if (!Array.isArray(value)) return [];
//     return value.map(text).filter(item => item !== 'NA');
// };

// const fileName = (path: string): string => path.split(/[\\/]/).pop() || path;

// const Pill = ({ children, tone = 'slate' }: { children: React.ReactNode; tone?: 'purple' | 'blue' | 'slate' | 'orange' | 'red' }) => {
//     const tones = {
//         purple: 'bg-violet-50 text-violet-700 border-violet-200',
//         blue: 'bg-sky-50 text-sky-700 border-sky-200',
//         slate: 'bg-slate-50 text-slate-700 border-slate-200',
//         orange: 'bg-orange-50 text-orange-700 border-orange-200',
//         red: 'bg-rose-50 text-rose-700 border-rose-200',
//     };
//     return (
//         <span className={`inline-flex items-center rounded-md border px-2 py-1 text-[9px] font-black uppercase tracking-widest ${tones[tone]}`}>
//             {children}
//         </span>
//     );
// };

// const Section = ({
//     title,
//     icon: Icon,
//     children,
//     action,
// }: {
//     title: string;
//     icon: React.ElementType;
//     children: React.ReactNode;
//     action?: React.ReactNode;
// }) => (
//     <section className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
//         <div className="mb-4 flex items-center justify-between gap-3 border-b border-slate-100 pb-3">
//             <div className="flex items-center gap-2">
//                 <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-violet-50 text-violet-700">
//                     <Icon className="h-4 w-4" />
//                 </span>
//                 <h4 className="text-[12px] font-black uppercase tracking-[0.14em] text-slate-900">{title}</h4>
//             </div>
//             {action}
//         </div>
//         {children}
//     </section>
// );

// const MetricCard = ({ icon: Icon, label, value, tone = 'purple' }: { icon: React.ElementType; label: string; value: number | string; tone?: 'purple' | 'blue' | 'slate' | 'orange' | 'red' }) => {
//     const toneClasses = {
//         purple: 'bg-violet-50 text-violet-700 border-violet-200',
//         blue: 'bg-sky-50 text-sky-700 border-sky-200',
//         slate: 'bg-slate-50 text-slate-700 border-slate-200',
//         orange: 'bg-orange-50 text-orange-700 border-orange-200',
//         red: 'bg-rose-50 text-rose-700 border-rose-200',
//     };
//     return (
//         <div className="flex min-h-[72px] items-center gap-3 rounded-xl border border-slate-200 bg-white px-3 py-3 shadow-sm">
//             <div className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-lg border ${toneClasses[tone]}`}>
//                 <Icon className="h-5 w-5" />
//             </div>
//             <div className="min-w-0">
//                 <p className="text-[9px] font-black uppercase tracking-widest text-slate-500">{label}</p>
//                 <p className="mt-1 text-xl font-black leading-none text-slate-900">{value}</p>
//             </div>
//         </div>
//     );
// };

// const CompactRow = ({ left, right, tone = 'slate' }: { left: React.ReactNode; right?: React.ReactNode; tone?: 'slate' | 'purple' | 'blue' | 'orange' | 'red' }) => (
//     <div className="flex items-center justify-between gap-3 rounded-lg border border-slate-200 bg-white px-3 py-2.5 text-[11px] shadow-sm">
//         <div className="min-w-0 font-semibold text-slate-800">{left}</div>
//         {right !== undefined && <Pill tone={tone}>{right}</Pill>}
//     </div>
// );

// export default function AnalysisSummaryPanel({ inventory, structuredFlows, summary, warningCount = 0 }: Props) {
//     const model = useMemo(() => {
//         const files = inventory.mule_configuration_files || [];
//         const flows = inventory.flows || [];
//         const connectors = inventory.connectors || [];
//         const transforms = inventory.dataweave_transformations || [];
//         const properties = inventory.properties_used || [];
//         const errors = inventory.error_handling_and_logging || [];
//         const munit = inventory.munit_test_cases || [];
//         const configFiles = files.filter(f => /config|artifact|application-types|mule|\.xml$|\.properties$|\.ya?ml$/i.test(fileName(f)));

//         const fileCounts = {
//             xml: files.filter(f => /\.xml$/i.test(f)).length,
//             yaml: files.filter(f => /\.(ya?ml)$/i.test(f)).length,
//             properties: files.filter(f => /\.properties$/i.test(f)).length,
//             java: files.filter(f => /\.java$/i.test(f)).length,
//             dataweave: files.filter(f => /\.(dwl|dw)$/i.test(f)).length + transforms.length,
//             config: configFiles.length,
//             munit: munit.length,
//         };
//         const otherFiles = Math.max(0, files.length - fileCounts.xml - fileCounts.yaml - fileCounts.properties - fileCounts.java);

//         const connectorGroups = connectors.reduce<Record<string, { count: number; flows: Set<string> }>>((acc, connector) => {
//             const name = text(connector.connector_type || connector.name);
//             if (!acc[name]) acc[name] = { count: 0, flows: new Set<string>() };
//             acc[name].count += 1;
//             flows.forEach(flow => {
//                 if (asList(flow.connectors).some(item => item.toLowerCase().includes(name.toLowerCase()))) {
//                     acc[name].flows.add(text(flow.name));
//                 }
//             });
//             return acc;
//         }, {});

//         const propertyFiles = Array.from(new Set(properties.map(p => text((p as Record<string, unknown>).defined_in_file)).filter(item => item !== 'NA')));
//         const envFiles = propertyFiles.filter(item => /(dev|prod|qa|stage|test|local|env)/i.test(item));
//         const secureFiles = propertyFiles.filter(item => /secure|secret|vault/i.test(item));
//         const secureProps = properties.filter(item => Boolean((item as Record<string, unknown>).secure)).length;

//         const errorText = errors.map(row => JSON.stringify(row).toLowerCase()).join(' ');
//         const flowLevelHandlers = errors.filter(row => text((row as Record<string, unknown>).error_handling) !== 'NA').length;
//         const globalHandlers = errors.filter(row => /global/i.test(text((row as Record<string, unknown>).flow))).length;
//         const retryScopes = (errorText.match(/retry/g) || []).length;
//         const onErrorContinue = (errorText.match(/on-error-continue/g) || []).length;
//         const onErrorPropagate = (errorText.match(/on-error-propagate/g) || []).length;

//         const transformText = transforms.map(item => text((item as Record<string, unknown>).transformation)).join(' ').toLowerCase();
//         const transformTypes = [
//             { label: 'DataWeave Scripts', value: transforms.length },
//             { label: 'Object to Object', value: (transformText.match(/object to object/g) || []).length },
//             { label: 'JSON to XML', value: (transformText.match(/json.*xml/g) || []).length },
//             { label: 'CSV to JSON', value: (transformText.match(/csv.*json/g) || []).length },
//             { label: 'XML to JSON', value: (transformText.match(/xml.*json/g) || []).length },
//             { label: 'Other Transformations', value: Math.max(0, transforms.length - (transformText.match(/json.*xml|csv.*json|xml.*json|object to object/g) || []).length) },
//         ];

//         const flowCards = flows.slice(0, 4).map(flow => {
//             const structured = structuredFlows.find(item => item.flow_name === flow.name);
//             const trigger = text(structured?.trigger || structured?.source || 'Unknown');
//             const componentCount = structured?.step_details?.length ?? asList(flow.activities).length;
//             const transformCount = asList(flow.transformations).length || transforms.filter(item => text((item as Record<string, unknown>).flow) === flow.name).length;
//             const description = text(structured?.high_level_summary || flow.high_level || 'Flow behavior summary unavailable.');
//             return {
//                 name: text(flow.name),
//                 description,
//                 trigger,
//                 componentCount,
//                 hasErrorHandling: Boolean(structured?.error_handling?.length),
//                 transformCount,
//             };
//         });

//         const insightItems = [
//             flows.some(flow => /scheduler|scheduled|batch/i.test(`${text(flow.high_level)} ${text(flow.type)}`)) && 'Scheduled integration flows detected.',
//             Object.keys(connectorGroups).some(name => /salesforce/i.test(name)) && 'Salesforce connector usage detected.',
//             munit.length > 0 && 'MUnit coverage artifacts available.',
//             flowLevelHandlers > 0 && 'Flow-level error handling strategy detected.',
//             warningCount > 0 && `${warningCount} warning${warningCount !== 1 ? 's' : ''} found during analysis.`,
//         ].filter(Boolean) as string[];

//         return {
//             files,
//             flows,
//             connectors,
//             transforms,
//             properties,
//             errors,
//             munit,
//             fileCounts,
//             otherFiles,
//             connectorGroups,
//             propertyFiles,
//             envFiles,
//             secureFiles,
//             secureProps,
//             globalHandlers,
//             flowLevelHandlers,
//             retryScopes,
//             onErrorContinue,
//             onErrorPropagate,
//             transformTypes,
//             flowCards,
//             configFiles,
//             insights: insightItems.slice(0, 4),
//         };
//     }, [inventory, structuredFlows, warningCount]);

//     const metricCards = [
//         { label: 'Total Files', value: model.files.length, icon: DocumentTextIcon, tone: 'purple' as const },
//         { label: 'Flows', value: summary?.flows ?? model.flows.length, icon: BoltIcon, tone: 'purple' as const },
//         { label: 'APIs', value: summary?.apis_detected ?? 0, icon: Squares2X2Icon, tone: 'blue' as const },
//         { label: 'Connectors', value: model.connectors.length, icon: CircleStackIcon, tone: 'blue' as const },
//         { label: 'Configurations', value: model.fileCounts.config, icon: CpuChipIcon, tone: 'slate' as const },
//         { label: 'Transformations', value: summary?.transformations ?? model.transforms.length, icon: CodeBracketIcon, tone: 'purple' as const },
//         { label: 'Properties', value: model.properties.length, icon: KeyIcon, tone: 'slate' as const },
//         { label: 'Error Handling', value: model.errors.length, icon: ShieldExclamationIcon, tone: 'orange' as const },
//         { label: 'MUnit Tests', value: model.munit.length, icon: BeakerIcon, tone: 'blue' as const },
//         { label: 'Warnings', value: warningCount, icon: ExclamationTriangleIcon, tone: warningCount > 0 ? 'red' as const : 'slate' as const },
//     ];

//     const fileBreakdown = [
//         ['XML Files', model.fileCounts.xml],
//         ['YAML Files', model.fileCounts.yaml],
//         ['Properties Files', model.fileCounts.properties],
//         ['Java Files', model.fileCounts.java],
//         ['DataWeave Files', model.fileCounts.dataweave],
//         ['Config Files', model.fileCounts.config],
//         ['MUnit Files', model.fileCounts.munit],
//         ['Other Files', model.otherFiles],
//     ];

//     return (
//         <div className="rounded-2xl border border-slate-200 bg-white p-4 shadow-sm sm:p-5">
//             <div className="mb-4 flex flex-wrap items-center justify-between gap-3">
//                 <div className="flex items-center gap-3">
//                     <span className="flex h-10 w-10 items-center justify-center rounded-xl border border-violet-200 bg-violet-50 text-violet-700">
//                         <SparklesIcon className="h-5 w-5" />
//                     </span>
//                     <div>
//                         <h3 className="text-[13px] font-black uppercase tracking-[0.18em] text-slate-950">Project Scan Summary</h3>
//                         <p className="mt-1 text-[11px] font-medium text-slate-500">Enterprise migration scan dashboard</p>
//                     </div>
//                 </div>
//                 <div className="flex items-center gap-2 rounded-xl border border-violet-100 bg-violet-50 px-3 py-2 text-[10px] font-bold text-violet-700">
//                     <ArrowPathIcon className="h-3.5 w-3.5" />
//                     Scan completed
//                 </div>
//             </div>

//             <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-5">
//                 {metricCards.map(card => <MetricCard key={card.label} {...card} />)}
//             </div>

//             <div className="mt-4 grid gap-4 xl:grid-cols-12">
//                 <div className="xl:col-span-4">
//                     <Section title="File Type Breakdown" icon={DocumentTextIcon}>
//                         <div className="space-y-2">
//                             {fileBreakdown.map(([label, count]) => (
//                                 <CompactRow
//                                     key={label}
//                                     left={(
//                                         <span className="flex min-w-0 items-center gap-2">
//                                             <DocumentTextIcon className="h-3.5 w-3.5 shrink-0 text-sky-600" />
//                                             <span className="truncate">{label}</span>
//                                         </span>
//                                     )}
//                                     right={count}
//                                     tone="blue"
//                                 />
//                             ))}
//                         </div>
//                     </Section>
//                 </div>

//                 <div className="xl:col-span-5">
//                     <Section title="Flow Overview" icon={BoltIcon} action={<Pill tone="purple">{model.flowCards.length} shown</Pill>}>
//                         <div className="space-y-3">
//                             {model.flowCards.length ? model.flowCards.map(flow => (
//                                 <article key={flow.name} className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
//                                     <div className="mb-2 flex flex-wrap items-center gap-2">
//                                         <Pill tone="purple">Flow</Pill>
//                                         <h5 className="min-w-0 break-all text-[13px] font-black text-slate-950">{flow.name}</h5>
//                                     </div>
//                                     <p className="text-[12px] leading-relaxed text-slate-600">{flow.description}</p>
//                                     <div className="mt-3 flex flex-wrap gap-2 text-[10px] font-bold text-slate-600">
//                                         <span>Trigger: <b className="text-slate-900">{flow.trigger}</b></span>
//                                         <span>Components: <b className="text-slate-900">{flow.componentCount}</b></span>
//                                         <span>Error Handling: <b className="text-slate-900">{flow.hasErrorHandling ? 'Yes' : 'No'}</b></span>
//                                         <span>Transforms: <b className="text-slate-900">{flow.transformCount}</b></span>
//                                     </div>
//                                 </article>
//                             )) : (
//                                 <CompactRow left="No flows detected" />
//                             )}
//                         </div>
//                     </Section>
//                 </div>

//                 <div className="xl:col-span-3">
//                     <Section title="Connector Summary" icon={CircleStackIcon}>
//                         <div className="space-y-2">
//                             {Object.entries(model.connectorGroups).length ? Object.entries(model.connectorGroups).slice(0, 6).map(([name, data]) => (
//                                 <CompactRow
//                                     key={name}
//                                     left={name}
//                                     right={`${data.count} use${data.count !== 1 ? 's' : ''} / ${Math.max(data.flows.size, data.count)} flow${Math.max(data.flows.size, data.count) !== 1 ? 's' : ''}`}
//                                     tone="blue"
//                                 />
//                             )) : <CompactRow left="No connectors detected" />}
//                         </div>
//                     </Section>
//                 </div>

//                 <div className="xl:col-span-4">
//                     <Section title="Configuration Files" icon={CpuChipIcon} action={<Pill tone="slate">{model.fileCounts.config}</Pill>}>
//                         <div className="space-y-2">
//                             {(model.configFiles.length ? model.configFiles.slice(0, 6) : ['No configuration files detected']).map(file => (
//                                 <CompactRow key={file} left={<span className="break-all font-mono">{fileName(file)}</span>} right={/\./.test(file) ? file.split('.').pop()?.toUpperCase() : 'FILE'} tone="slate" />
//                             ))}
//                         </div>
//                     </Section>
//                 </div>

//                 <div className="xl:col-span-5">
//                     <Section title="Transformation Summary" icon={CodeBracketIcon}>
//                         <div className="space-y-2">
//                             {model.transformTypes.map(item => <CompactRow key={item.label} left={item.label} right={item.value} tone="purple" />)}
//                         </div>
//                     </Section>
//                 </div>

//                 <div className="xl:col-span-3">
//                     <Section title="Analysis Insights" icon={SparklesIcon}>
//                         <div className="space-y-2">
//                             {(model.insights.length ? model.insights : ['No notable insights detected yet.']).map((item, index) => (
//                                 <div key={item} className={`rounded-xl border px-3 py-3 text-[11px] leading-relaxed ${index === model.insights.length - 1 && warningCount > 0 ? 'border-orange-200 bg-orange-50 text-orange-800' : 'border-blue-200 bg-blue-50 text-blue-800'}`}>
//                                     {item}
//                                 </div>
//                             ))}
//                         </div>
//                     </Section>
//                 </div>

//                 <div className="xl:col-span-4">
//                     <Section title="Properties" icon={KeyIcon}>
//                         <div className="grid grid-cols-3 gap-2">
//                             <MetricCard icon={KeyIcon} label="Files" value={model.propertyFiles.length} tone="slate" />
//                             <MetricCard icon={DocumentTextIcon} label="Env Files" value={model.envFiles.length} tone="blue" />
//                             <MetricCard icon={ShieldExclamationIcon} label="Secure" value={model.secureFiles.length || model.secureProps} tone="red" />
//                         </div>
//                         <div className="mt-3 space-y-2">
//                             {(model.propertyFiles.length ? model.propertyFiles.slice(0, 4) : ['No property files detected']).map(file => (
//                                 <CompactRow key={file} left={<span className="break-all font-mono">{fileName(file)}</span>} />
//                             ))}
//                         </div>
//                     </Section>
//                 </div>

//                 <div className="xl:col-span-4">
//                     <Section title="Error Handling" icon={ShieldExclamationIcon}>
//                         <div className="grid grid-cols-2 gap-2">
//                             <CompactRow left="Total Handlers" right={model.errors.length} tone="orange" />
//                             <CompactRow left="Global Handlers" right={model.globalHandlers} tone="orange" />
//                             <CompactRow left="Flow-level" right={model.flowLevelHandlers} tone="orange" />
//                             <CompactRow left="Retry Scopes" right={model.retryScopes} tone="orange" />
//                             <CompactRow left="On Error Continue" right={model.onErrorContinue} tone="orange" />
//                             <CompactRow left="On Error Propagate" right={model.onErrorPropagate} tone="orange" />
//                         </div>
//                     </Section>
//                 </div>

//                 <div className="xl:col-span-4">
//                     <Section title="MUnit Summary" icon={BeakerIcon}>
//                         <div className="grid grid-cols-2 gap-2">
//                             <MetricCard icon={BeakerIcon} label="Suites" value={new Set(model.munit.map(test => text((test as Record<string, unknown>).file))).size} tone="blue" />
//                             <MetricCard icon={BoltIcon} label="Cases" value={model.munit.length} tone="purple" />
//                             <MetricCard icon={DocumentTextIcon} label="Coverage" value="NA" tone="slate" />
//                         </div>
//                     </Section>
//                 </div>
//             </div>
//         </div>
//     );
// }
