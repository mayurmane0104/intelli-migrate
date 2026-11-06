'use client';

import React from 'react';
import Modal from './Modal';
import { ExclamationTriangleIcon } from '@heroicons/react/24/outline';

interface ConfirmDialogProps {
    isOpen: boolean;
    onClose: () => void;
    onConfirm: () => void;
    title: string;
    message: string;
    confirmLabel?: string;
    destructive?: boolean;
}

export default function ConfirmDialog({
    isOpen, onClose, onConfirm, title, message,
    confirmLabel = 'Confirm', destructive = false,
}: ConfirmDialogProps) {
    return (
        <Modal isOpen={isOpen} onClose={onClose} title={title} size="sm">
            <div className="flex flex-col items-center text-center">
                {destructive && (
                    <div className="w-12 h-12 rounded-full bg-error-50 flex items-center justify-center mb-4">
                        <ExclamationTriangleIcon className="h-6 w-6 text-error-500" />
                    </div>
                )}
                <p className="text-gray-600 dark:text-gray-400 text-sm">{message}</p>
                <div className="flex gap-3 mt-6 w-full">
                    <button
                        onClick={onClose}
                        className="flex-1 px-4 py-2.5 text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-950 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
                    >
                        Cancel
                    </button>
                    <button
                        onClick={() => { onConfirm(); onClose(); }}
                        className={`flex-1 px-4 py-2.5 text-sm font-medium text-white rounded-lg transition-colors ${destructive
                                ? 'bg-error-500 hover:bg-error-600'
                                : 'bg-primary-600 hover:bg-primary-700'
                            }`}
                    >
                        {confirmLabel}
                    </button>
                </div>
            </div>
        </Modal>
    );
}
