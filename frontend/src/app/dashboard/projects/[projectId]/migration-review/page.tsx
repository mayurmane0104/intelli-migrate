'use client';

import React, { useEffect } from 'react';
import { useRouter } from 'next/navigation';

type PageProps = {
    params: Promise<{ projectId: string }>;
};

export default function MigrationReviewPage({ params }: PageProps) {
    const router = useRouter();

    useEffect(() => {
        params.then(value => router.replace(`/dashboard/projects/${value.projectId}/editor`));
    }, [params, router]);

    return <div className="p-6 text-sm text-gray-500">Opening migration workspace...</div>;
}
