'use client';

import React, { ReactNode } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { usePathname } from 'next/navigation';

interface TransitionWrapperProps {
    children: ReactNode;
}

export default function TransitionWrapper({ children }: TransitionWrapperProps) {
    const pathname = usePathname();

    return (
        <AnimatePresence mode="wait">
            <motion.div
                key={pathname}
                initial={{ opacity: 0, y: 8, scale: 0.99 }}
                animate={{ opacity: 1, y: 0, scale: 1 }}
                exit={{ opacity: 0, y: -8, scale: 1.01 }}
                transition={{ 
                    duration: 0.3, 
                    ease: [0.22, 1, 0.36, 1] // Custom quintic-like ease for premium feel
                }}
                className="h-full w-full"
            >
                {children}
            </motion.div>
        </AnimatePresence>
    );
}
