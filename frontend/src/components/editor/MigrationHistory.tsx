'use client';

import React from 'react';
import { MigrationRecord, LLMProviderType } from '@/lib/types';
import { PROVIDER_INFO } from '@/lib/llm-provider';
import {
    ClockIcon,
    CheckCircleIcon,
    ChevronRightIcon
} from '@heroicons/react/24/outline';

interface MigrationHistoryProps {
    migrations: MigrationRecord[];
    activeId?: string;
    onSelect: (migration: MigrationRecord) => void;
}

export default function MigrationHistory({ migrations, activeId, onSelect }: MigrationHistoryProps) {
    if (!migrations || migrations.length === 0) return null;

    // Sort migrations by date descending (newest first)
    const sorted = [...migrations].sort((a, b) =>
        new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
    );

    return (
        <div className="flex flex-col gap-1 py-1 max-h-64 overflow-y-auto">
            {sorted.map((m, idx) => {
                const info = PROVIDER_INFO[m.provider as LLMProviderType];
                const date = new Date(m.createdAt).toLocaleString(undefined, {
                    month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
                });
                const isActive = activeId === m.id;

                return (
                    <button
                        key={m.id}
                        onClick={() => onSelect(m)}
                        className={`flex items-center gap-3 px-3 py-2 text-left transition-colors ${isActive
                            ? 'bg-primary-50 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300'
                            : 'hover:bg-gray-50 dark:hover:bg-gray-800/50 text-gray-700 dark:text-gray-300'
                            }`}
                    >
                        <div className="shrink-0 w-8 h-8 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-sm">
                            {info?.icon || '🤖'}
                        </div>
                        <div className="flex-1 min-w-0">
                            <div className="flex items-center justify-between gap-2">
                                <p className="text-[11px] font-bold truncate">
                                    Version {sorted.length - idx}
                                </p>
                                <p className="text-[10px] text-gray-400">
                                    {date}
                                </p>
                            </div>
                            <p className="text-[10px] text-gray-500 truncate italic">
                                {info?.name || m.provider} · {m.model}
                            </p>
                        </div>
                        {isActive && (
                            <CheckCircleIcon className="h-4 w-4 text-primary-500 shrink-0" />
                        )}
                        {!isActive && (
                            <ChevronRightIcon className="h-3 w-3 text-gray-300 shrink-0" />
                        )}
                    </button>
                );
            })}
        </div>
    );
}
