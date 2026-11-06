'use client';

import React from 'react';

export function SkeletonLine({ className = '' }: { className?: string }) {
    return <div className={`h-4 bg-gray-200 rounded animate-pulse ${className}`} />;
}

export function SkeletonCard() {
    return (
        <div className="bg-white dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-xl p-6 space-y-4">
            <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-gray-200 rounded-lg animate-pulse" />
                <div className="flex-1 space-y-2">
                    <SkeletonLine className="w-2/3" />
                    <SkeletonLine className="w-1/3 h-3" />
                </div>
            </div>
            <SkeletonLine className="w-full" />
            <SkeletonLine className="w-4/5" />
            <div className="flex gap-2 pt-2">
                <SkeletonLine className="w-16 h-6 rounded-full" />
                <SkeletonLine className="w-16 h-6 rounded-full" />
            </div>
        </div>
    );
}

export function SkeletonTable({ rows = 5 }: { rows?: number }) {
    return (
        <div className="space-y-3">
            {Array.from({ length: rows }).map((_, i) => (
                <div key={i} className="flex gap-4">
                    <SkeletonLine className="w-1/4" />
                    <SkeletonLine className="w-1/3" />
                    <SkeletonLine className="w-1/6" />
                    <SkeletonLine className="w-1/6" />
                </div>
            ))}
        </div>
    );
}

export function SkeletonEditor() {
    return (
        <div className="flex gap-4 h-full">
            <div className="w-60 space-y-2 p-4">
                {Array.from({ length: 10 }).map((_, i) => (
                    <SkeletonLine key={i} className={`w-${i % 2 ? '3/4' : 'full'}`} />
                ))}
            </div>
            <div className="flex-1 space-y-1 p-4">
                {Array.from({ length: 20 }).map((_, i) => (
                    <SkeletonLine key={i} className={`h-3 w-${['full', '4/5', '3/4', '2/3', '5/6'][i % 5]}`} />
                ))}
            </div>
        </div>
    );
}
