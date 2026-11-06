'use client';

import React, { ReactNode, useMemo } from 'react';
import Sidebar from './Sidebar';
import Topbar from './Topbar';
import ToastContainer from '../ui/Toast';
import TransitionWrapper from './TransitionWrapper';
import LoadingScreen from '../ui/LoadingScreen';
import { usePathname } from 'next/navigation';
import { useApp } from '@/contexts/AppContext';
import { motion, AnimatePresence } from 'framer-motion';

export default function AppShell({ children }: { children: ReactNode }) {
    const pathname = usePathname();
    const { selectedProject, globalLoading } = useApp();

    // Data Guard: Detect if we are on a project-specific route and wait for data
    const isProjectRoute = pathname.includes('/dashboard/projects/');
    const routeProjectId = useMemo(() => {
        const match = pathname.match(/\/dashboard\/projects\/([^/]+)/);
        return match ? match[1] : null;
    }, [pathname]);

    const isDataMissing = isProjectRoute && routeProjectId && (!selectedProject || selectedProject.id !== routeProjectId);
    const isLoading = globalLoading || isDataMissing;

    return (
        <div className="flex h-screen overflow-hidden bg-gray-50 dark:bg-gray-950">
            {/* Top Navigation Progress Bar (Premium Touch) */}
            <AnimatePresence>
                {isLoading && (
                    <motion.div 
                        initial={{ scaleX: 0 }}
                        animate={{ scaleX: 1 }}
                        exit={{ opacity: 0 }}
                        transition={{ duration: 1.5, ease: "easeInOut" }}
                        className="fixed top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-primary-600 via-indigo-500 to-primary-400 z-[100] origin-left"
                    />
                )}
            </AnimatePresence>

            {/* Sidebar */}
            <Sidebar />

            {/* Main area: topbar + scrollable content */}
            <div className="flex flex-col flex-1 min-w-0 overflow-hidden">
                <Topbar />
                <main className="flex-1 overflow-y-auto bg-gray-50 dark:bg-gray-950 relative">
                    <AnimatePresence mode="wait">
                        {isLoading && (
                            <motion.div 
                                key="loading-overlay"
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                exit={{ opacity: 0 }}
                                className="absolute inset-0 z-[60] bg-gray-50 dark:bg-gray-950 flex items-center justify-center p-8"
                            >
                                <LoadingScreen />
                            </motion.div>
                        )}
                    </AnimatePresence>

                    <div className={isLoading ? 'opacity-0 pointer-events-none' : 'opacity-100 transition-opacity duration-300 h-full'}>
                        <TransitionWrapper>
                            {children}
                        </TransitionWrapper>
                    </div>
                </main>
            </div>

            {/* Global toast notifications */}
            <ToastContainer />
        </div>
    );
}
