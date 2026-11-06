'use client';

import React, { useState, useRef } from 'react';
import { CloudArrowUpIcon, DocumentIcon, XMarkIcon, ExclamationCircleIcon } from '@heroicons/react/24/outline';
import { importApi } from '@/lib/api';
import { useApp } from '@/contexts/AppContext';

export default function ZipUpload() {
    const { selectedProject, refreshFiles, addToast } = useApp();
    const [file, setFile] = useState<File | null>(null);
    const [uploading, setUploading] = useState(false);
    const [progress, setProgress] = useState(0);
    const [error, setError] = useState('');
    const [dragOver, setDragOver] = useState(false);
    const inputRef = useRef<HTMLInputElement>(null);

    const validateFile = (f: File) => {
        if (!f.name.endsWith('.zip')) {
            setError('Only .zip files are supported');
            return false;
        }
        if (f.size > 100 * 1024 * 1024) {
            setError('File size must be under 100MB');
            return false;
        }
        return true;
    };

    const handleFile = (f: File) => {
        setError('');
        if (!validateFile(f)) return;
        setFile(f);
        setProgress(0);
    };

    const handleUpload = async () => {
        if (!file) return;
        if (!selectedProject) {
            setError('No project selected. Please open a project first.');
            return;
        }
        setUploading(true);
        setProgress(0);
        try {
            const result = await importApi.zip(file, selectedProject.id);
            await refreshFiles(selectedProject.id, true);
            setProgress(100);
            addToast({ type: 'success', title: 'Upload Complete', message: `${result.filesExtracted} files imported from ${file.name}` });
        } catch (err: any) {
            setError(err?.message || 'Upload failed. Please try again.');
        } finally {
            setUploading(false);
        }
    };

    const handleDrop = (e: React.DragEvent) => {
        e.preventDefault();
        setDragOver(false);
        if (e.dataTransfer.files[0]) handleFile(e.dataTransfer.files[0]);
    };

    return (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 dark:text-gray-200 flex items-center gap-2">
                <CloudArrowUpIcon className="h-5 w-5" /> Upload ZIP
            </h3>

            {/* Drop Zone */}
            <div
                className={`border-2 border-dashed rounded-xl p-8 text-center transition-colors cursor-pointer ${dragOver ? 'border-primary-400 bg-primary-50' : 'border-gray-300 hover:border-primary-300 hover:bg-gray-50'
                    }`}
                onDragOver={e => { e.preventDefault(); setDragOver(true); }}
                onDragLeave={() => setDragOver(false)}
                onDrop={handleDrop}
                onClick={() => inputRef.current?.click()}
            >
                <CloudArrowUpIcon className="h-10 w-10 text-gray-400 mx-auto mb-3" />
                <p className="text-sm text-gray-600 dark:text-gray-400 font-medium">
                    Drag & drop your ZIP file here, or <span className="text-primary-600">browse</span>
                </p>
                <p className="text-xs text-gray-400 mt-1">ZIP files only, up to 100MB</p>
                <input ref={inputRef} type="file" accept=".zip" className="hidden"
                    onChange={e => e.target.files?.[0] && handleFile(e.target.files[0])} />
            </div>

            {error && (
                <div className="flex items-center gap-2 p-3 bg-error-50 border border-error-200 rounded-lg text-sm text-error-600">
                    <ExclamationCircleIcon className="h-4 w-4 shrink-0" /> {error}
                </div>
            )}

            {/* File Info */}
            {file && (
                <div className="bg-gray-50 rounded-lg p-4">
                    <div className="flex items-center gap-3 mb-2">
                        <DocumentIcon className="h-5 w-5 text-gray-500 dark:text-gray-400" />
                        <div className="flex-1">
                            <p className="text-sm font-medium text-gray-800 dark:text-gray-200">{file.name}</p>
                            <p className="text-xs text-gray-400">{(file.size / 1024 / 1024).toFixed(2)} MB</p>
                        </div>
                        <button onClick={() => { setFile(null); setProgress(0); setUploading(false); }}
                            className="p-1 hover:bg-gray-200 rounded"><XMarkIcon className="h-4 w-4 text-gray-400" /></button>
                    </div>
                    {progress < 100 && (
                        <button onClick={handleUpload} disabled={uploading}
                            className="w-full py-2 text-sm font-medium bg-primary-600 hover:bg-primary-700 disabled:bg-gray-300 text-white rounded-lg transition-colors flex items-center justify-center gap-2">
                            {uploading ? (
                                <><span className="h-4 w-4 border-2 border-white border-t-transparent rounded-full animate-spin" />Uploading...</>
                            ) : 'Upload'}
                        </button>
                    )}
                    {/* Progress */}
                    {(uploading || progress >= 100) && (
                    <div className="w-full h-2 bg-gray-200 rounded-full overflow-hidden mt-2">
                        <div className={`h-full rounded-full transition-all ${progress >= 100 ? 'bg-success-500' : 'bg-primary-500'}`}
                            style={{ width: `${Math.min(progress, 100)}%` }} />
                    </div>
                    )}
                    <p className="text-xs text-gray-400 mt-1">
                        {uploading ? 'Uploading...' : progress >= 100 ? '✓ Upload complete' : ''}
                    </p>
                </div>
            )}
        </div>
    );
}
