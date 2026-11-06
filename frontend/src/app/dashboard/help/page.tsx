'use client';

import React from 'react';
import {
    QuestionMarkCircleIcon,
    KeyIcon,
    BuildingOffice2Icon,
    Square3Stack3DIcon,
    FolderIcon,
    CodeBracketIcon,
    UserCircleIcon
} from '@heroicons/react/24/outline';

export default function HelpPage() {
    return (
        <div className="max-w-5xl mx-auto py-10 px-6">
            <div className="mb-12">
                <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-4 flex items-center gap-3">
                    <QuestionMarkCircleIcon className="h-8 w-8 text-primary-600" />
                    MigrationStudio: Comprehensive User Guide
                </h1>
                <p className="text-lg text-gray-600 dark:text-gray-400 leading-relaxed">
                    Welcome to <span className="font-semibold text-primary-700">MigrationStudio</span>, the premier platform for migrating MuleSoft integrations to modern AWS Lambda architectures. This guide provides a detailed walkthrough of the application's core functionality and user flow.
                </p>
            </div>

            <div className="space-y-16">
                {/* 1. Authentication */}
                <section id="auth" className="scroll-mt-20">
                    <div className="flex items-center gap-2 mb-6">
                        <div className="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center">
                            <KeyIcon className="h-6 w-6 text-blue-600" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200">1. Authentication</h2>
                    </div>
                    <p className="text-gray-600 dark:text-gray-400 mb-6">
                        Access the platform via the secure login portal. Enter your credentials to reach your personalized dashboard.
                    </p>
                    <div className="rounded-xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm transition-hover hover:shadow-md">
                        <img src="/docs/login.png" alt="Login Page" className="w-full object-cover" />
                    </div>
                </section>

                {/* 2. Organizations */}
                <section id="orgs" className="scroll-mt-20">
                    <div className="flex items-center gap-2 mb-6">
                        <div className="w-10 h-10 rounded-full bg-emerald-100 flex items-center justify-center">
                            <BuildingOffice2Icon className="h-6 w-6 text-emerald-600" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200">2. Organization Management</h2>
                    </div>
                    <p className="text-gray-600 dark:text-gray-400 mb-6">
                        Upon logging in, you'll see your <span className="font-semibold text-gray-900 dark:text-gray-100">Organizations</span>. Organizations are top-level containers for all your migration work, typical for enterprise departments or client portfolios.
                    </p>
                    <div className="rounded-xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm transition-hover hover:shadow-md">
                        <img src="/docs/organizations.png" alt="Organizations Dashboard" className="w-full object-cover" />
                    </div>
                </section>

                {/* 3. Workspaces */}
                <section id="workspaces" className="scroll-mt-20">
                    <div className="flex items-center gap-2 mb-6">
                        <div className="w-10 h-10 rounded-full bg-indigo-100 flex items-center justify-center">
                            <Square3Stack3DIcon className="h-6 w-6 text-indigo-600" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200">3. Workspaces</h2>
                    </div>
                    <p className="text-gray-600 dark:text-gray-400 mb-6">
                        Each Organization contains multiple <span className="font-semibold text-gray-900 dark:text-gray-100">Workspaces</span>. Workspaces allow you to segregate work by environment (e.g., Development, Staging, Production) or sub-teams.
                    </p>
                    <div className="rounded-xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm transition-hover hover:shadow-md">
                        <img src="/docs/workspaces.png" alt="Workspaces View" className="w-full object-cover" />
                    </div>
                </section>

                {/* 4. Projects */}
                <section id="projects" className="scroll-mt-20">
                    <div className="flex items-center gap-2 mb-6">
                        <div className="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center">
                            <FolderIcon className="h-6 w-6 text-amber-600" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200">4. Projects</h2>
                    </div>
                    <p className="text-gray-600 dark:text-gray-400 mb-6">
                        Inside a Workspace, you manage your migration <span className="font-semibold text-gray-900 dark:text-gray-100">Projects</span>. Each project represents a specific integration or set of APIs being moved to AWS. You can track migration progress and status (Pending, In Progress, Completed) at a glance.
                    </p>
                    <div className="rounded-xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm transition-hover hover:shadow-md">
                        <img src="/docs/projects.png" alt="Projects List" className="w-full object-cover" />
                    </div>
                </section>

                {/* 5. Code Editor */}
                <section id="editor" className="scroll-mt-20">
                    <div className="flex items-center gap-2 mb-6">
                        <div className="w-10 h-10 rounded-full bg-primary-100 flex items-center justify-center">
                            <CodeBracketIcon className="h-6 w-6 text-primary-600" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200">5. Code Editor & Migration Engine</h2>
                    </div>
                    <div className="prose prose-primary max-w-none text-gray-600 dark:text-gray-400 mb-6">
                        <p>The heart of MigrationStudio is the <strong>Code Editor</strong>. Here, you can:</p>
                        <ul className="list-disc pl-5 space-y-2">
                            <li><strong>View Source:</strong> Browse the original MuleSoft project structure.</li>
                            <li><strong>Run Migration:</strong> Execute our proprietary AI-driven migration engine.</li>
                            <li><strong>Side-by-Side Review:</strong> Compare original MuleSoft XML with generated AWS Lambda code.</li>
                            <li><strong>Track Logs:</strong> Monitor detailed migration logs and progress.</li>
                        </ul>
                    </div>
                    <div className="rounded-xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm transition-hover hover:shadow-md">
                        <img src="/docs/editor.png" alt="Code Editor & Migration" className="w-full object-cover" />
                    </div>
                </section>

                {/* 6. Profile */}
                <section id="profile" className="scroll-mt-20 pb-10">
                    <div className="flex items-center gap-2 mb-6">
                        <div className="w-10 h-10 rounded-full bg-rose-100 flex items-center justify-center">
                            <UserCircleIcon className="h-6 w-6 text-rose-600" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200">6. User Profile & Settings</h2>
                    </div>
                    <p className="text-gray-600 dark:text-gray-400 mb-6">
                        Manage your personal account details, appearance preferences (Theme), and security settings from the <span className="font-semibold text-gray-900 dark:text-gray-100">Profile</span> page.
                    </p>
                    <div className="rounded-xl overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm transition-hover hover:shadow-md">
                        <img src="/docs/profile.png" alt="Account Settings" className="w-full object-cover" />
                    </div>
                </section>
            </div>

            {/* Summary Flow */}
            <div className="mt-12 p-8 bg-gray-50 rounded-2xl border border-gray-200 dark:border-gray-800">
                <h3 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-6">Quick App Flow Summary</h3>
                <div className="flex flex-wrap items-center gap-3 text-sm font-medium text-gray-600 dark:text-gray-400">
                    <span className="px-3 py-1.5 bg-white dark:bg-gray-950 rounded-lg border border-gray-200 dark:border-gray-800">Login</span>
                    <span className="text-gray-300">→</span>
                    <span className="px-3 py-1.5 bg-white dark:bg-gray-950 rounded-lg border border-gray-200 dark:border-gray-800">Select Organization</span>
                    <span className="text-gray-300">→</span>
                    <span className="px-3 py-1.5 bg-white dark:bg-gray-950 rounded-lg border border-gray-200 dark:border-gray-800">Select Workspace</span>
                    <span className="text-gray-300">→</span>
                    <span className="px-3 py-1.5 bg-white dark:bg-gray-950 rounded-lg border border-gray-200 dark:border-gray-800">Select Project</span>
                    <span className="text-gray-300">→</span>
                    <span className="px-3 py-1.5 bg-white dark:bg-gray-950 rounded-lg border border-gray-200 dark:border-gray-800">Code Editor</span>
                    <span className="text-gray-300">→</span>
                    <span className="px-3 py-1.5 bg-white dark:bg-gray-950 rounded-lg border border-gray-200 dark:border-gray-800">Migration</span>
                    <span className="text-gray-300">→</span>
                    <span className="px-3 py-1.5 bg-primary-600 text-white rounded-lg border border-primary-600 shadow-sm">Review & Export</span>
                </div>
            </div>
        </div>
    );
}
