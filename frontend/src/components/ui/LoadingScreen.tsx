'use client';

import React from 'react';
import { motion } from 'framer-motion';
import { SparklesIcon } from '@heroicons/react/24/outline';

interface LoadingScreenProps {
    message?: string;
    subtext?: string;
}

export default function LoadingScreen({ 
    message = "Synchronizing Neural State", 
    subtext = "Fetching environment context..." 
}: LoadingScreenProps) {
    return (
        <div className="flex flex-col items-center justify-center min-h-[60vh] p-8">
            <div className="relative mb-8">
                {/* Outer Glow */}
                <motion.div 
                    className="absolute inset-0 bg-primary-500/20 blur-2xl rounded-full"
                    animate={{ 
                        scale: [1, 1.5, 1],
                        opacity: [0.3, 0.6, 0.3]
                    }}
                    transition={{ 
                        duration: 3, 
                        repeat: Infinity, 
                        ease: "easeInOut" 
                    }}
                />
                
                {/* Main Icon */}
                <div className="relative z-10 w-20 h-20 bg-white dark:bg-gray-900 rounded-3xl shadow-2xl border border-gray-100 dark:border-gray-800 flex items-center justify-center">
                    <SparklesIcon className="w-10 h-10 text-primary-600 animate-pulse" />
                </div>
                
                {/* Rotating Ring */}
                <svg className="absolute -inset-4 w-[112px] h-[112px] rotate-[-90deg]">
                    <motion.circle
                        cx="56"
                        cy="56"
                        r="52"
                        stroke="currentColor"
                        strokeWidth="2"
                        fill="transparent"
                        className="text-primary-500/10"
                    />
                    <motion.circle
                        cx="56"
                        cy="56"
                        r="52"
                        stroke="currentColor"
                        strokeWidth="3"
                        strokeDasharray="326.7" // 2 * PI * 52
                        fill="transparent"
                        className="text-primary-500"
                        animate={{ strokeDashoffset: [326.7, -326.7] }}
                        transition={{ 
                            duration: 2, 
                            repeat: Infinity, 
                            ease: "easeInOut" 
                        }}
                    />
                </svg>
            </div>
            
            <motion.h2 
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="text-xl font-black text-gray-900 dark:text-gray-100 tracking-tight text-center"
            >
                {message}
            </motion.h2>
            
            <motion.p 
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.2 }}
                className="text-[11px] font-bold text-gray-400 uppercase tracking-[0.2em] mt-3 text-center"
            >
                {subtext}
            </motion.p>
            
            {/* Minimal Progress Bar */}
            <div className="w-48 h-1 bg-gray-100 dark:bg-gray-800 rounded-full mt-10 overflow-hidden relative">
                <motion.div 
                    className="absolute top-0 left-0 h-full bg-gradient-to-r from-primary-600 to-indigo-600"
                    animate={{ x: ["-100%", "100%"] }}
                    transition={{ 
                        duration: 1.5, 
                        repeat: Infinity, 
                        ease: "easeInOut" 
                    }}
                    style={{ width: "60%" }}
                />
            </div>
        </div>
    );
}
