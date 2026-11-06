'use client';

import React, { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '../contexts/AuthContext';

export default function Home() {
  const { isAuthenticated } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (isAuthenticated) {
      router.replace('/dashboard/organizations');
    } else {
      router.replace('/login');
    }
  }, [isAuthenticated, router]);

  return (
    <div className="h-screen flex items-center justify-center bg-white dark:bg-gray-950 ">
      <div className="flex flex-col items-center gap-4">
        <div className="w-12 h-12 bg-primary-600 rounded-xl flex items-center justify-center animate-pulse">
          <span className="text-white font-bold text-xl">M</span>
        </div>
        <p className="text-gray-400 text-sm">Loading MigrationStudio...</p>
      </div>
    </div>
  );
}
