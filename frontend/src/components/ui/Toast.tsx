'use client';

import React from 'react';
import { useApp } from '../../contexts/AppContext';
import { XMarkIcon, CheckCircleIcon, ExclamationTriangleIcon, InformationCircleIcon, ExclamationCircleIcon } from '@heroicons/react/24/outline';

const iconMap = {
    success: CheckCircleIcon,
    error: ExclamationCircleIcon,
    warning: ExclamationTriangleIcon,
    info: InformationCircleIcon,
};

const colorMap = {
    success: 'bg-success-50 border-success-500 text-success-600',
    error: 'bg-error-50 border-error-500 text-error-600',
    warning: 'bg-warning-50 border-warning-500 text-warning-600',
    info: 'bg-info-50 border-primary-500 text-primary-600',
};

export default function ToastContainer() {
    const { toasts, removeToast } = useApp();

    return (
        <div className="fixed top-4 right-4 z-50 flex flex-col gap-3 w-96">
            {toasts.map(toast => {
                const Icon = iconMap[toast.type];
                return (
                    <div
                        key={toast.id}
                        className={`animate-slide-in flex items-start gap-3 p-4 rounded-lg border shadow-lg ${colorMap[toast.type]}`}
                    >
                        <Icon className="h-5 w-5 shrink-0 mt-0.5" />
                        <div className="flex-1 min-w-0">
                            <p className="font-semibold text-sm">{toast.title}</p>
                            <p className="text-sm opacity-80 mt-0.5">{toast.message}</p>
                        </div>
                        <button onClick={() => removeToast(toast.id)} className="shrink-0 hover:opacity-70">
                            <XMarkIcon className="h-4 w-4" />
                        </button>
                    </div>
                );
            })}
        </div>
    );
}
