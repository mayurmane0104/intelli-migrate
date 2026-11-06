'use client';

import React from 'react';
import type { ArchitectureReviewPayload } from '@/lib/types';
import ApprovalActions from './ApprovalActions';

type ArchitectureReviewProps = {
    architecture?: ArchitectureReviewPayload;
    disabled?: boolean;
    onApprove: () => void;
    onReject: () => void;
    onReturnToMapping: () => void;
};

export default function ArchitectureReview({ architecture, disabled, onApprove, onReject, onReturnToMapping }: ArchitectureReviewProps) {
    const rows = architecture?.architecture || [];
    return (
        <section className="space-y-4">
            <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                    <h2 className="text-sm font-semibold text-gray-950">Architecture Review</h2>
                    <p className="mt-1 text-xs text-gray-500">{rows.length} AWS service groups</p>
                </div>
                <ApprovalActions
                    approveLabel="Approve Architecture"
                    rejectLabel="Reject Architecture"
                    secondaryLabel="Return To Mapping"
                    secondaryKind="return"
                    disabled={disabled || rows.length === 0}
                    onApprove={onApprove}
                    onReject={onReject}
                    onSecondary={onReturnToMapping}
                />
            </div>

            <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
                {rows.map(row => (
                    <div key={row.generatedResourceName} className="rounded-md border border-gray-200 bg-white p-3">
                        <div className="flex items-start justify-between gap-3">
                            <div>
                                <h3 className="text-sm font-semibold text-gray-950">{row.awsService}</h3>
                                <p className="mt-1 text-xs text-gray-500">{row.purpose}</p>
                            </div>
                            <span className="rounded border border-gray-200 px-2 py-1 text-[11px] font-medium text-gray-600">
                                {row.estimatedCostCategory}
                            </span>
                        </div>
                        <div className="mt-3 text-[11px] text-gray-500">{row.generatedResourceName}</div>
                    </div>
                ))}
            </div>
        </section>
    );
}
