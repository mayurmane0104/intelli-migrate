'use client';

import React, { useRef, useState, useCallback, useEffect } from 'react';

export interface PanelConfig {
    id: string;
    defaultWidth: number;   // in px (or -1 for flex-grow center)
    minWidth: number;
    maxWidth: number;
    grow?: boolean;         // if true, this panel fills remaining space
    content: React.ReactNode;
}

interface ResizablePanelsProps {
    panels: PanelConfig[];
    className?: string;
}

export default function ResizablePanels({ panels, className = '' }: ResizablePanelsProps) {
    // Widths stored in px for fixed panels; grow panels have no stored width
    const [widths, setWidths] = useState<Record<string, number>>(() => {
        const w: Record<string, number> = {};
        panels.forEach(p => { if (!p.grow) w[p.id] = p.defaultWidth; });
        return w;
    });

    const containerRef = useRef<HTMLDivElement>(null);
    const dragging = useRef<{ dividerId: number; startX: number; leftId: string; rightId: string; leftW: number; rightW: number } | null>(null);

    const onMouseDown = useCallback((e: React.MouseEvent, dividerId: number) => {
        e.preventDefault();
        // Find fixed panels on either side of the divider
        const fixedPanels = panels.filter(p => !p.grow);
        const leftPanel = fixedPanels[dividerId - 1] ?? panels[dividerId - 1];
        const rightPanel = fixedPanels[dividerId] ?? panels[dividerId];

        if (!leftPanel || !rightPanel) return;

        dragging.current = {
            dividerId,
            startX: e.clientX,
            leftId: leftPanel.id,
            rightId: rightPanel.id,
            leftW: widths[leftPanel.id] ?? leftPanel.defaultWidth,
            rightW: widths[rightPanel.id] ?? rightPanel.defaultWidth,
        };

        document.body.style.cursor = 'col-resize';
        document.body.style.userSelect = 'none';
    }, [panels, widths]);

    useEffect(() => {
        const onMouseMove = (e: MouseEvent) => {
            if (!dragging.current) return;
            const { startX, leftId, rightId, leftW, rightW } = dragging.current;
            const dx = e.clientX - startX;

            const lp = panels.find(p => p.id === leftId)!;
            const rp = panels.find(p => p.id === rightId)!;

            const newLeft = Math.max(lp.minWidth, Math.min(lp.maxWidth, leftW + dx));
            const newRight = Math.max(rp.minWidth, Math.min(rp.maxWidth, rightW - dx));

            setWidths(prev => ({ ...prev, [leftId]: newLeft, [rightId]: newRight }));
        };

        const onMouseUp = () => {
            dragging.current = null;
            document.body.style.cursor = '';
            document.body.style.userSelect = '';
        };

        window.addEventListener('mousemove', onMouseMove);
        window.addEventListener('mouseup', onMouseUp);
        return () => {
            window.removeEventListener('mousemove', onMouseMove);
            window.removeEventListener('mouseup', onMouseUp);
        };
    }, [panels]);

    // Build divider indices: dividers appear between panels that can resize between each other
    // We put a divider after every non-last panel
    const items: React.ReactNode[] = [];
    let dividerIdx = 0;

    panels.forEach((panel, i) => {
        const w = panel.grow ? undefined : widths[panel.id];
        items.push(
            <div
                key={panel.id}
                className="flex flex-col min-h-0 overflow-hidden"
                style={panel.grow ? { flex: 1, minWidth: panel.minWidth, maxWidth: panel.maxWidth } : { width: w, flexShrink: 0 }}
            >
                {panel.content}
            </div>
        );

        if (i < panels.length - 1) {
            const currentDivider = dividerIdx;
            dividerIdx++;
            items.push(
                <div
                    key={`divider-${currentDivider}`}
                    onMouseDown={e => onMouseDown(e, currentDivider + 1)}
                    className="w-1 shrink-0 bg-gray-200 hover:bg-primary-400 cursor-col-resize transition-colors group relative z-10"
                    title="Drag to resize"
                >
                    {/* Visual grip dots */}
                    <div className="absolute inset-y-0 left-0 right-0 flex flex-col items-center justify-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                        {[0, 1, 2].map(d => (
                            <div key={d} className="w-1 h-1 rounded-full bg-primary-500" />
                        ))}
                    </div>
                </div>
            );
        }
    });

    return (
        <div ref={containerRef} className={`flex min-h-0 overflow-hidden ${className}`}>
            {items}
        </div>
    );
}
