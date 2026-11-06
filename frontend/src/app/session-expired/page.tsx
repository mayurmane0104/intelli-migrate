'use client';

import React from 'react';

export default function SessionExpiredPage() {
    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 p-4">
            <div className="w-full max-w-md text-center">
                <div className="bg-white dark:bg-gray-950 rounded-xl shadow-sm border border-gray-200 dark:border-gray-800 p-8">
                    <div className="w-16 h-16 bg-warning-50 rounded-full flex items-center justify-center mx-auto mb-4">
                        <svg className="h-8 w-8 text-warning-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                    </div>
                    <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">Session Expired</h2>
                    <p className="text-gray-500 dark:text-gray-400 text-sm mb-6">
                        Your session has expired for security reasons. Please sign in again to continue.
                    </p>
                    <a href="/login"
                        className="inline-block px-6 py-2.5 bg-primary-600 hover:bg-primary-700 text-white font-medium text-sm rounded-lg transition-colors">
                        Sign In Again
                    </a>
                </div>
            </div>
        </div>
    );
}
