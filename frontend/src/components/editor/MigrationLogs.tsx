'use client';

import React, { useState, useMemo, useRef, useEffect } from 'react';
import { useApp } from '@/contexts/AppContext';
import {
    MagnifyingGlassIcon, ArrowDownTrayIcon,
    ChevronDownIcon, ChevronRightIcon,
    CheckCircleIcon, ExclamationCircleIcon,
    ExclamationTriangleIcon, InformationCircleIcon,
    ArrowPathIcon, FunnelIcon, TrashIcon,
} from '@heroicons/react/24/outline';

const logStyles: Record<string, { icon: React.ElementType; color: string; bg: string }> = {
    success: { icon: CheckCircleIcon, color: 'text-success-600', bg: 'bg-success-50/40' },
    error: { icon: ExclamationCircleIcon, color: 'text-error-600', bg: 'bg-error-50/40' },
    warning: { icon: ExclamationTriangleIcon, color: 'text-warning-600', bg: 'bg-warning-50/40' },
    info: { icon: InformationCircleIcon, color: 'text-primary-600', bg: 'bg-primary-50/40' },
};

export default function MigrationLogs() {
    const { migrationLogs, clearLogs } = useApp();
    const [search, setSearch] = useState('');
    const [filter, setFilter] = useState<string>('all');
    const [expandedLogs, setExpandedLogs] = useState<Set<string>>(new Set());
    const logEndRef = useRef<HTMLDivElement>(null);

    // Auto-scroll when new logs arrive
    useEffect(() => {
        logEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [migrationLogs.length]);

    const filtered = useMemo(() => {
        return migrationLogs.filter(log => {
            if (filter !== 'all' && log.status !== filter) return false;
            if (search) {
                const q = search.toLowerCase();
                if (!log.fileName.toLowerCase().includes(q) && !log.message.toLowerCase().includes(q)) return false;
            }
            return true;
        });
    }, [migrationLogs, search, filter]);

    const counts = useMemo(() => ({
        all: migrationLogs.length,
        success: migrationLogs.filter(l => l.status === 'success').length,
        error: migrationLogs.filter(l => l.status === 'error').length,
        warning: migrationLogs.filter(l => l.status === 'warning').length,
        info: migrationLogs.filter(l => l.status === 'info').length,
    }), [migrationLogs]);

    return (
        <div className="flex flex-col h-full bg-white dark:bg-gray-950 border-t border-gray-200 dark:border-gray-800">
            {/* Toolbar */}
            <div className="flex items-center gap-3 px-4 py-2 border-b border-gray-100 dark:border-gray-800 bg-gray-50/50">
                <div className="relative flex-1 max-w-xs">
                    <MagnifyingGlassIcon className="absolute left-2 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-gray-400" />
                    <input type="text" value={search} onChange={e => setSearch(e.target.value)}
                        placeholder="Search logs..."
                        className="w-full pl-7 pr-3 py-1.5 text-xs bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-md focus:ring-1 focus:ring-primary-500 outline-none" />
                </div>
                <div className="flex items-center gap-1">
                    <FunnelIcon className="h-3.5 w-3.5 text-gray-400" />
                    {(['all', 'error', 'warning', 'success', 'info'] as const).map(f => (
                        <button key={f} onClick={() => setFilter(f)}
                            className={`px-2 py-1 text-[11px] font-medium rounded transition-colors capitalize ${filter === f ? 'bg-primary-100 text-primary-700' : 'text-gray-500 dark:text-gray-400 hover:bg-gray-100'
                                }`}>
                            {f} {f !== 'all' && <span className="text-gray-400">({counts[f]})</span>}
                        </button>
                    ))}
                </div>
                <div className="flex items-center gap-1 ml-auto">
                    <button onClick={clearLogs}
                        className="flex items-center gap-1 px-2 py-1 text-xs text-gray-500 dark:text-gray-400 hover:text-error-600 hover:bg-error-50 rounded transition-colors">
                        <TrashIcon className="h-3 w-3" /> Clear
                    </button>
                    <button className="flex items-center gap-1 px-2 py-1 text-xs text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:text-gray-300 hover:bg-gray-100 rounded transition-colors">
                        <ArrowDownTrayIcon className="h-3 w-3" /> Export
                    </button>
                </div>
            </div>

            {/* Logs */}
            <div className="flex-1 overflow-y-auto scrollbar-thin">
                {filtered.length === 0 ? (
                    <div className="text-center py-8 text-gray-400 text-xs">
                        {migrationLogs.length === 0 ? 'No logs yet — start a migration to see output here' : 'No logs match the current filter'}
                    </div>
                ) : (
                    <div>
                        {filtered.map(log => {
                            const style = logStyles[log.status];
                            const Icon = style.icon;
                            const isExpanded = expandedLogs.has(log.id);
                            return (
                                <div key={log.id} className={`border-b border-gray-50 ${style.bg}`}>
                                    <div
                                        className="flex items-center gap-3 px-4 py-2 cursor-pointer hover:bg-white dark:bg-gray-950/50 transition-colors"
                                        onClick={() => log.stackTrace && setExpandedLogs(prev => {
                                            const next = new Set(prev);
                                            next.has(log.id) ? next.delete(log.id) : next.add(log.id);
                                            return next;
                                        })}
                                    >
                                        <Icon className={`h-4 w-4 shrink-0 ${style.color}`} />
                                        <span className="text-[11px] font-mono font-medium text-gray-700 dark:text-gray-300 w-40 truncate">{log.fileName}</span>
                                        <span className="text-xs text-gray-600 dark:text-gray-400 flex-1">{log.message}</span>
                                        {log.duration ? (
                                            <span className="text-[10px] text-gray-400 tabular-nums shrink-0">{Math.round(log.duration)}ms</span>
                                        ) : null}
                                        <span className="text-[10px] text-gray-400 shrink-0 tabular-nums w-16 text-right">
                                            {new Date(log.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })}
                                        </span>
                                        {log.stackTrace && (
                                            isExpanded ? <ChevronDownIcon className="h-3 w-3 text-gray-400" /> : <ChevronRightIcon className="h-3 w-3 text-gray-400" />
                                        )}
                                    </div>
                                    {isExpanded && log.stackTrace && (
                                        <div className="px-4 pb-3">
                                            <pre className="text-[11px] bg-gray-900 text-gray-300 rounded-lg p-3 overflow-x-auto font-mono whitespace-pre-wrap leading-relaxed">
                                                {log.stackTrace}
                                            </pre>
                                        </div>
                                    )}
                                </div>
                            );
                        })}
                        <div ref={logEndRef} />
                    </div>
                )}
            </div>
        </div>
    );
}
