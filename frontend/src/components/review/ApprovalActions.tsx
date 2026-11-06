'use client';

import React from 'react';
import {
    CheckCircleIcon,
    XCircleIcon,
    ArrowPathIcon,
    PencilSquareIcon,
    ArrowUturnLeftIcon,
} from '@heroicons/react/24/outline';

type ApprovalActionsProps = {
    approveLabel: string;
    rejectLabel: string;
    secondaryLabel?: string;
    secondaryKind?: 'reanalysis' | 'modify' | 'return';
    disabled?: boolean;
    onApprove: () => void;
    onReject: () => void;
    onSecondary?: () => void;
};

export default function ApprovalActions({
    approveLabel,
    rejectLabel,
    secondaryLabel,
    secondaryKind = 'modify',
    disabled,
    onApprove,
    onReject,
    onSecondary,
}: ApprovalActionsProps) {
    const SecondaryIcon = secondaryKind === 'reanalysis'
        ? ArrowPathIcon
        : secondaryKind === 'return'
            ? ArrowUturnLeftIcon
            : PencilSquareIcon;

    return (
        <div className="flex flex-wrap items-center gap-2">
            <button
                type="button"
                disabled={disabled}
                onClick={onApprove}
                className="inline-flex items-center gap-2 rounded-md bg-emerald-600 px-3 py-2 text-xs font-semibold text-white shadow-sm transition hover:bg-emerald-700 disabled:cursor-not-allowed disabled:bg-gray-300"
            >
                <CheckCircleIcon className="h-4 w-4" />
                {approveLabel}
            </button>
            <button
                type="button"
                disabled={disabled}
                onClick={onReject}
                className="inline-flex items-center gap-2 rounded-md border border-red-200 bg-white px-3 py-2 text-xs font-semibold text-red-700 transition hover:bg-red-50 disabled:cursor-not-allowed disabled:text-gray-400"
            >
                <XCircleIcon className="h-4 w-4" />
                {rejectLabel}
            </button>
            {secondaryLabel && onSecondary && (
                <button
                    type="button"
                    disabled={disabled}
                    onClick={onSecondary}
                    className="inline-flex items-center gap-2 rounded-md border border-gray-200 bg-white px-3 py-2 text-xs font-semibold text-gray-700 transition hover:bg-gray-50 disabled:cursor-not-allowed disabled:text-gray-400"
                >
                    <SecondaryIcon className="h-4 w-4" />
                    {secondaryLabel}
                </button>
            )}
        </div>
    );
}
