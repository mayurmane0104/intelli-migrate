'use client';

import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { PrismLight as SyntaxHighlighter } from 'react-syntax-highlighter';
import ts from 'react-syntax-highlighter/dist/cjs/languages/prism/typescript';
import js from 'react-syntax-highlighter/dist/cjs/languages/prism/javascript';
import py from 'react-syntax-highlighter/dist/cjs/languages/prism/python';
import yaml from 'react-syntax-highlighter/dist/cjs/languages/prism/yaml';
import json from 'react-syntax-highlighter/dist/cjs/languages/prism/json';
import xml from 'react-syntax-highlighter/dist/cjs/languages/prism/markup';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/cjs/styles/prism';

SyntaxHighlighter.registerLanguage('typescript', ts);
SyntaxHighlighter.registerLanguage('javascript', js);
SyntaxHighlighter.registerLanguage('python', py);
SyntaxHighlighter.registerLanguage('yaml', yaml);
SyntaxHighlighter.registerLanguage('json', json);
SyntaxHighlighter.registerLanguage('xml', xml);
SyntaxHighlighter.registerLanguage('html', xml);

interface MarkdownViewerProps {
    content: string;
}

export default function MarkdownViewer({ content }: MarkdownViewerProps) {
    return (
        <div className="markdown-body p-6 max-w-4xl mx-auto h-full overflow-y-auto text-sm text-gray-800 dark:text-gray-200">
            <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                components={{
                    h1: ({ node, ...props }) => <h1 className="text-2xl font-bold mb-4 mt-6 text-gray-900 dark:text-white pb-2 border-b border-gray-200 dark:border-gray-800" {...props} />,
                    h2: ({ node, ...props }) => <h2 className="text-xl font-semibold mb-3 mt-5 text-gray-900 dark:text-gray-100" {...props} />,
                    h3: ({ node, ...props }) => <h3 className="text-lg font-medium mb-2 mt-4 text-gray-800 dark:text-gray-200" {...props} />,
                    p: ({ node, ...props }) => <p className="mb-4 leading-relaxed" {...props} />,
                    ul: ({ node, ...props }) => <ul className="list-disc pl-5 mb-4 space-y-1" {...props} />,
                    ol: ({ node, ...props }) => <ol className="list-decimal pl-5 mb-4 space-y-1" {...props} />,
                    li: ({ node, ...props }) => <li className="" {...props} />,
                    a: ({ node, ...props }) => <a className="text-primary-600 hover:underline" {...props} />,
                    table: ({ node, ...props }) => (
                        <div className="overflow-x-auto mb-4">
                            <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-800 border border-gray-200 dark:border-gray-800 rounded-lg" {...props} />
                        </div>
                    ),
                    thead: ({ node, ...props }) => <thead className="bg-gray-50 dark:bg-gray-900/50 block w-full" {...props} />,
                    tbody: ({ node, ...props }) => <tbody className="divide-y divide-gray-200 dark:divide-gray-800 block w-full" {...props} />,
                    tr: ({ node, ...props }) => <tr className="flex w-full" {...props} />,
                    th: ({ node, ...props }) => <th className="px-4 py-2 text-left text-xs font-semibold text-gray-500 dark:text-gray-400 flex-1" {...props} />,
                    td: ({ node, ...props }) => <td className="px-4 py-2 text-sm text-gray-700 dark:text-gray-300 flex-1" {...props} />,
                    code({ node, inline, className, children, ...props }: any) {
                        const match = /language-(\w+)/.exec(className || '');
                        return !inline && match ? (
                            <div className="mb-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-800 shadow-sm">
                                <div className="bg-gray-100 dark:bg-gray-900 flex justify-between items-center px-4 py-1.5 text-xs text-gray-500 dark:text-gray-400 border-b border-gray-200 dark:border-gray-800 uppercase tracking-wider font-semibold">
                                    <span>{match[1]}</span>
                                </div>
                                <SyntaxHighlighter
                                    style={vscDarkPlus as any}
                                    language={match[1]}
                                    PreTag="div"
                                    customStyle={{ margin: 0, borderRadius: 0, fontSize: '12px' }}
                                    {...props}
                                >
                                    {String(children).replace(/\n$/, '')}
                                </SyntaxHighlighter>
                            </div>
                        ) : (
                            <code className="bg-gray-100 dark:bg-gray-800 px-1.5 py-0.5 rounded text-xs text-primary-600 dark:text-primary-400 font-mono" {...props}>
                                {children}
                            </code>
                        );
                    }
                }}
            >
                {content}
            </ReactMarkdown>
        </div>
    );
}
