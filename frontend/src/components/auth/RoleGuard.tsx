'use client';

import React from 'react';
import { Role } from '../../lib/types';
import { useAuth } from '../../contexts/AuthContext';

interface RoleGuardProps {
    allowedRoles: Role[];
    children: React.ReactNode;
    fallback?: React.ReactNode;
}

export default function RoleGuard({ allowedRoles, children, fallback }: RoleGuardProps) {
    const { role } = useAuth();

    if (!allowedRoles.includes(role)) {
        return fallback ? <>{fallback}</> : (
            <div className="text-center py-8 text-gray-400 text-sm">
                <p>You don&apos;t have permission to view this content.</p>
                <p className="text-xs mt-1">Required role: {allowedRoles.join(' or ')}</p>
            </div>
        );
    }

    return <>{children}</>;
}
