'use client';

import React from 'react';
import type { ProjectAnalysisPayload, Project } from '@/lib/types';
import ApprovalActions from './ApprovalActions';

type IRReviewProps = {
    project: Project;
    analysis?: ProjectAnalysisPayload;
    disabled?: boolean;
    onApprove: () => void;
    onReject: () => void;
    onReanalysis: () => void;
};

export default function IRReview({ project, analysis, disabled, onApprove, onReject, onReanalysis }: IRReviewProps) {
    const flows = analysis?.structured_flows || [];
    const inventory = analysis?.inventory_summary;
    const connectors = inventory?.connectors || [];
    const transformations = inventory?.dataweave_transformations || [];
    const properties = inventory?.properties_used || [];
    const errors = inventory?.error_handling_and_logging || [];

    return (
        <section className="space-y-4">
            <div className="flex flex-wrap items-start justify-between gap-3">
                <div>
                    <h2 className="text-sm font-semibold text-gray-950">IR Review</h2>
                    <p className="mt-1 text-xs text-gray-500">{project.name}</p>
                </div>
                <ApprovalActions
                    approveLabel="Approve IR"
                    rejectLabel="Reject IR"
                    secondaryLabel="Request Re-Analysis"
                    secondaryKind="reanalysis"
                    disabled={disabled || !analysis}
                    onApprove={onApprove}
                    onReject={onReject}
                    onSecondary={onReanalysis}
                />
            </div>

            <div className="grid grid-cols-2 gap-3 md:grid-cols-4">
                <Metric label="Complexity" value={analysis?.summary?.complexity_score || 'NA'} />
                <Metric label="Confidence" value={`${Math.round((analysis?.summary?.confidence_score || 0) * 100)}%`} />
                <Metric label="Status" value={analysis?.validation?.status || 'UNKNOWN'} />
                <Metric label="Flows" value={String(flows.length)} />
            </div>

            <div className="overflow-hidden rounded-md border border-gray-200 bg-white">
                <table className="min-w-full divide-y divide-gray-200 text-xs">
                    <thead className="bg-gray-50 text-left font-semibold text-gray-600">
                        <tr>
                            <th className="px-3 py-2">Flow Name</th>
                            <th className="px-3 py-2">Type</th>
                            <th className="px-3 py-2">Trigger</th>
                            <th className="px-3 py-2">Confidence</th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100">
                        {flows.map(flow => (
                            <tr key={flow.flow_name}>
                                <td className="px-3 py-2 font-medium text-gray-900">{flow.flow_name}</td>
                                <td className="px-3 py-2 text-gray-600">{flow.flow_type}</td>
                                <td className="px-3 py-2 text-gray-600">{flow.trigger}</td>
                                <td className="px-3 py-2 text-gray-600">{Math.round((flow.confidence || 0) * 100)}%</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <div className="grid gap-3 lg:grid-cols-3">
                <ListPanel title="Connectors" items={connectors.map(item => String(item.connector_type || item.name || 'Connector'))} />
                <ListPanel title="Transformations" items={transformations.map(item => String(item.name || item.script_id || item.transformation_id || 'DataWeave'))} />
                <ListPanel title="Security & Errors" items={[...properties.map(item => String(item.key || item.name || 'Property')), ...errors.map(item => String(item.type || item.name || 'Handler'))]} />
            </div>
        </section>
    );
}

function Metric({ label, value }: { label: string; value: string }) {
    return (
        <div className="rounded-md border border-gray-200 bg-white px-3 py-2">
            <div className="text-[11px] font-medium text-gray-500">{label}</div>
            <div className="mt-1 text-sm font-semibold text-gray-950">{value}</div>
        </div>
    );
}

function ListPanel({ title, items }: { title: string; items: string[] }) {
    return (
        <div className="rounded-md border border-gray-200 bg-white p-3">
            <h3 className="text-xs font-semibold text-gray-900">{title}</h3>
            <div className="mt-2 flex flex-wrap gap-1.5">
                {(items.length ? items : ['NA']).slice(0, 12).map((item, index) => (
                    <span key={`${item}-${index}`} className="rounded border border-gray-200 px-2 py-1 text-[11px] text-gray-600">
                        {item}
                    </span>
                ))}
            </div>
        </div>
    );
}
