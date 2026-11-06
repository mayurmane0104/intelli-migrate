'use client';

import React, { memo, useEffect, useMemo, useRef, useState } from 'react';
import { useVirtualizer } from '@tanstack/react-virtual';

function RawIRViewer({ rawIr, rawIrError }: { rawIr: unknown; rawIrError: string | null }) {
    const containerRef = useRef<HTMLDivElement | null>(null);
    const [content, setContent] = useState('');
    const [ready, setReady] = useState(false);
    const [visibleLines, setVisibleLines] = useState(200);

    useEffect(() => {
        let cancelled = false;
        setReady(false);
        setVisibleLines(200);

        const format = () => {
            if (cancelled) return;
            try {
                const next = rawIrError ? rawIrError : JSON.stringify(rawIr, null, 2);
                if (!cancelled) {
                    setContent(next);
                    setReady(true);
                }
            } catch {
                if (!cancelled) {
                    setContent('Could not format raw IR.');
                    setReady(true);
                }
            }
        };

        if (typeof window !== 'undefined' && 'requestIdleCallback' in window) {
            const id = (window as Window & { requestIdleCallback: (cb: () => void) => number }).requestIdleCallback(format);
            return () => {
                cancelled = true;
                if ('cancelIdleCallback' in window) {
                    (window as Window & { cancelIdleCallback: (id: number) => void }).cancelIdleCallback(id);
                }
            };
        }

        const t = setTimeout(format, 0);
        return () => {
            cancelled = true;
            clearTimeout(t);
        };
    }, [rawIr, rawIrError]);

    const lines = useMemo(() => content.split('\n'), [content]);
    const initialBySize = useMemo(() => {
        let bytes = 0;
        let count = 0;
        for (const line of lines) {
            bytes += line.length + 1;
            if (bytes > 20 * 1024 || count >= 200) break;
            count++;
        }
        return Math.max(1, count);
    }, [lines]);

    const sliceCount = Math.min(lines.length, Math.max(visibleLines, initialBySize));
    const viewLines = useMemo(() => lines.slice(0, sliceCount), [lines, sliceCount]);
    const isHuge = content.length > 2 * 1024 * 1024;
    const hasMore = sliceCount < lines.length;

    const rowVirtualizer = useVirtualizer({
        count: viewLines.length,
        getScrollElement: () => containerRef.current,
        estimateSize: () => 18,
        overscan: 12,
    });

    return (
        <div className="space-y-2">
            {isHuge && (
                <div className="rounded-md border border-amber-200 bg-amber-50 px-2 py-1 text-[10px] text-amber-700">
                    Large IR detected ({Math.round(content.length / 1024)} KB). Rendering chunked preview.
                </div>
            )}
            {!ready ? (
                <div className="h-24 animate-pulse rounded bg-slate-100" />
            ) : (
                <>
                    <div ref={containerRef} className="max-h-[420px] overflow-auto rounded border border-slate-200 bg-white">
                        <div style={{ height: `${rowVirtualizer.getTotalSize()}px`, width: '100%', position: 'relative' }}>
                            {rowVirtualizer.getVirtualItems().map((virtualRow) => (
                                <div
                                    key={virtualRow.key}
                                    style={{
                                        position: 'absolute',
                                        top: 0,
                                        left: 0,
                                        width: '100%',
                                        transform: `translateY(${virtualRow.start}px)`,
                                    }}
                                    className="font-mono text-[10px] leading-[18px] text-slate-600 px-2 whitespace-pre"
                                >
                                    {viewLines[virtualRow.index]}
                                </div>
                            ))}
                        </div>
                    </div>
                    {hasMore && (
                        <button
                            onClick={() => setVisibleLines((n) => n + 200)}
                            className="rounded border border-slate-300 bg-white px-2 py-1 text-[10px] font-semibold text-slate-700 hover:bg-slate-50"
                        >
                            Load More
                        </button>
                    )}
                </>
            )}
        </div>
    );
}

export default memo(RawIRViewer);
