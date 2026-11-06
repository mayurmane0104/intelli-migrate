'use client';

import React, { useState } from 'react';
import {
    LinkIcon,
    CheckCircleIcon,
    ExclamationCircleIcon,
    ArrowPathIcon,
} from '@heroicons/react/24/outline';

export default function GitImport() {
    const [url, setUrl] = useState('');
    const [branch, setBranch] = useState('main');
    const [token, setToken] = useState('');
    const [showToken, setShowToken] = useState(false);
    const [status, setStatus] = useState<'idle' | 'validating' | 'success' | 'failed'>('idle');
    const [error, setError] = useState('');

    const handleTest = async () => {
        if (!url) { setError('Git URL is required'); return; }
        setStatus('validating');
        setError('');
        await new Promise(r => setTimeout(r, 2000));
        // Simulate success/failure
        if (url.includes('github.com') || url.includes('gitlab.com')) {
            setStatus('success');
        } else {
            setStatus('failed');
            setError('Could not connect to repository. Please check the URL and credentials.');
        }
    };

    return (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 dark:text-gray-200 flex items-center gap-2">
                <LinkIcon className="h-5 w-5" /> Git Import
            </h3>

            <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Repository URL</label>
                <input type="text" value={url} onChange={e => { setUrl(e.target.value); setError(''); setStatus('idle'); }}
                    className="w-full px-4 py-2.5 rounded-lg border border-gray-300 text-sm focus:ring-2 focus:ring-primary-500 outline-none"
                    placeholder="https://github.com/org/repo.git" />
            </div>

            <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Branch</label>
                <input type="text" value={branch} onChange={e => setBranch(e.target.value)}
                    className="w-full px-4 py-2.5 rounded-lg border border-gray-300 text-sm focus:ring-2 focus:ring-primary-500 outline-none"
                    placeholder="main" />
            </div>

            <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">Access Token (optional)</label>
                <div className="relative">
                    <input type={showToken ? 'text' : 'password'} value={token}
                        onChange={e => setToken(e.target.value)}
                        className="w-full px-4 py-2.5 pr-16 rounded-lg border border-gray-300 text-sm focus:ring-2 focus:ring-primary-500 outline-none"
                        placeholder="ghp_xxxxxxxxxxxx" />
                    <button onClick={() => setShowToken(!showToken)}
                        className="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-primary-600 hover:text-primary-700 font-medium">
                        {showToken ? 'Hide' : 'Show'}
                    </button>
                </div>
            </div>

            {error && (
                <div className="flex items-center gap-2 p-3 bg-error-50 border border-error-200 rounded-lg text-sm text-error-600">
                    <ExclamationCircleIcon className="h-4 w-4 shrink-0" />
                    {error}
                </div>
            )}

            {status === 'success' && (
                <div className="flex items-center gap-2 p-3 bg-success-50 border border-success-200 rounded-lg text-sm text-success-600">
                    <CheckCircleIcon className="h-4 w-4 shrink-0" />
                    Connection successful! Repository is accessible.
                </div>
            )}

            <button onClick={handleTest} disabled={status === 'validating'}
                className="flex items-center gap-2 px-4 py-2.5 bg-primary-600 hover:bg-primary-700 disabled:bg-primary-400 text-white text-sm font-medium rounded-lg transition-colors">
                {status === 'validating' ? (
                    <><ArrowPathIcon className="h-4 w-4 animate-spin" /> Validating...</>
                ) : 'Test Connection'}
            </button>
        </div>
    );
}
