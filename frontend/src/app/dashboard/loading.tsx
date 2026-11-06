import React from 'react';
import LoadingScreen from '@/components/ui/LoadingScreen';

export default function Loading() {
    return (
        <div className="flex h-screen items-center justify-center bg-gray-50 dark:bg-gray-950">
            <LoadingScreen message="Initializing Experience" subtext="Preparing neural workspace..." />
        </div>
    );
}
