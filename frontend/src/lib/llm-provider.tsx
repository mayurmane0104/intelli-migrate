/**
 * LLM Provider Metadata (Stripped version for UI)
 * The actual provider implementations and prompts have been moved to the Python backend.
 */

import type { LLMSettings, LLMProviderType } from './types';
import React from 'react';

/* ─── Types ─── */
export interface MigrationConfig {
    targetPlatform?: string;
    migrationType: string;
    targetRuntime: string;
    fileName: string;
    filePath: string;
    instructions?: string;
    projectStructure?: string;
}

export interface LLMUsage {
    inputTokens: number;
    outputTokens: number;
}

/* ─── Runtime & migration-type metadata ───────────────────────────────────── */
export const RUNTIME_META: Record<string, {
    label: string;
    language: string;
    languageVersion: string;
    sdk: string;
    sdkImport: string;
    fileExt: string;
    namingConvention: string;
    handlerSignature: string;
    testFramework: string;
    packageManager: string;
}> = {
    nodejs: {
        label: 'Node.js 20.x LTS',
        language: 'TypeScript',
        languageVersion: '5.x / ES2022',
        sdk: 'AWS SDK for JavaScript v3 (modular)',
        sdkImport: '@aws-sdk/<service-client>',
        fileExt: '.ts',
        namingConvention: 'camelCase functions, kebab-case filenames',
        handlerSignature: 'export const handler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult>',
        testFramework: 'Jest + @types/jest',
        packageManager: 'npm / package.json',
    },
    python: {
        label: 'Python 3.12',
        language: 'Python',
        languageVersion: '3.12',
        sdk: 'boto3 1.x / botocore',
        sdkImport: 'import boto3',
        fileExt: '.py',
        namingConvention: 'snake_case functions and filenames',
        handlerSignature: 'def lambda_handler(event: dict, context: LambdaContext) -> dict',
        testFramework: 'pytest + moto',
        packageManager: 'pip / requirements.txt',
    },
    java: {
        label: 'Java 21 (Amazon Corretto 21)',
        language: 'Java',
        languageVersion: '21 (LTS) — records, sealed classes, pattern matching',
        sdk: 'AWS SDK for Java v2',
        sdkImport: 'software.amazon.awssdk.*',
        fileExt: '.java',
        namingConvention: 'PascalCase class names, camelCase methods',
        handlerSignature: 'public class Handler implements RequestHandler<Map<String,Object>, Map<String,Object>>',
        testFramework: 'JUnit 5 + Mockito',
        packageManager: 'Maven (pom.xml) or Gradle',
    },
};

export const MIGRATION_TYPE_META: Record<string, { sourceVersion: string; targetService: string; pattern: string }> = {
    'mule3-lambda': { sourceVersion: 'MuleSoft Mule 3.x (ESB)', targetService: 'AWS Lambda + API Gateway', pattern: 'Function-per-flow' },
    'mule4-lambda': { sourceVersion: 'MuleSoft Mule 4.x (Runtime 4.x)', targetService: 'AWS Lambda + API Gateway', pattern: 'Function-per-flow, reactive streams' },
    'apiled-apigateway': { sourceVersion: 'MuleSoft API-Led Connectivity', targetService: 'AWS API Gateway + Lambda', pattern: 'REST proxy + handler' },
    'batch-stepfunction': { sourceVersion: 'MuleSoft Batch Module', targetService: 'AWS Step Functions + Lambda', pattern: 'State machine + map state' },
};

/* ══════════════════════════════════════════════
   Model Catalog
   ══════════════════════════════════════════════ */
export const MODEL_CATALOG = {
    nova: [
        { id: 'amazon.nova-lite-v1:0', name: 'Amazon Nova Lite', description: 'Fast, cost-effective (default)' },
        { id: 'amazon.nova-micro-v1:0', name: 'Amazon Nova Micro', description: 'Smallest, fastest Nova model' },
        { id: 'amazon.nova-pro-v1:0', name: 'Amazon Nova Pro', description: 'Most capable Nova model' },
    ],
    claude: [
        { id: 'claude-3-5-sonnet-20241022', name: 'Claude 3.5 Sonnet', description: 'Most balanced & intelligent' },
        { id: 'claude-3-5-haiku-20241022', name: 'Claude 3.5 Haiku', description: 'Fastest for simple tasks' },
        { id: 'claude-3-opus-20240229', name: 'Claude 3 Opus', description: 'Best for complex logic' },
    ],
    openai: [
        { id: 'gpt-4o', name: 'GPT-4o', description: 'Most capable' },
        { id: 'gpt-4o-mini', name: 'GPT-4o Mini', description: 'Fast & affordable' },
        { id: 'o3-mini', name: 'o3-mini', description: 'Reasoning model' },
    ],
    gemini: [
        { id: 'gemini-2.5-flash', name: 'Gemini 2.5 Flash', description: 'Latest, fast' },
        { id: 'gemini-2.5-pro', name: 'Gemini 2.5 Pro', description: 'Most capable' },
        { id: 'gemini-2.0-flash', name: 'Gemini 2.0 Flash', description: 'Previous gen' },
    ],
} as const;

export const PROVIDER_INFO: Record<LLMProviderType, { name: string; description: string; icon: React.ReactNode }> = {
    nova: {
        name: 'Amazon Nova Lite',
        description: 'AWS Bedrock — fast, cost-effective, default provider',
        icon: (
            <svg viewBox="0 0 24 24" className="w-5 h-5 fill-current text-orange-500">
                <path d="M18.75 10.5h-2.25v-3a.75.75 0 0 0-.75-.75H8.25a.75.75 0 0 0-.75.75v3H5.25A2.25 2.25 0 0 0 3 12.75v4.5A2.25 2.25 0 0 0 5.25 19.5h13.5A2.25 2.25 0 0 0 21 17.25v-4.5a2.25 2.25 0 0 0-2.25-2.25Zm-9.75-2.25h6v2.25h-6V8.25Zm9 9H6v-4.5h12v4.5Z"/>
            </svg>
        ),
    },
    claude: {
        name: 'Anthropic Claude',
        description: 'Advanced reasoning, best for complex Mule flows',
        icon: (
            <svg viewBox="0 0 24 24" className="w-5 h-5 fill-current text-orange-600" >
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.5 14H8c-1.66 0-3-1.34-3-3s1.34-3 3-3h.5V8.5C8.5 6.57 10.07 5 12 5s3.5 1.57 3.5 3.5V10h1C18.16 10 19.5 11.34 19.5 13s-1.34 3-3 3zM12 7c-1.1 0-2 .9-2 2h4c0-1.1-.9-2-2-2z" />
            </svg>
        ),
    },
    openai: {
        name: 'OpenAI GPT-4o',
        description: 'High performance general purpose migration',
        icon: (
            <svg viewBox="0 0 24 24" className="w-5 h-5 fill-current text-green-600" >
                <path d="M22.28 11.83a8.9 8.9 0 0 0-.27-2.9 8.65 8.65 0 0 0-4.88-5.32A8.69 8.69 0 0 0 11.83 1.7a8.9 8.9 0 0 0-2.9.27 8.65 8.65 0 0 0-5.32 4.88A8.69 8.69 0 0 0 1.7 12.17a8.9 8.9 0 0 0 .27 2.9 8.65 8.65 0 0 0 4.88 5.32 8.69 8.69 0 0 0 5.32 1.91 8.9 8.9 0 0 0 2.9-.27 8.65 8.65 0 0 0 5.32-4.88 8.69 8.69 0 0 0 1.9-5.32Zm-4.89-6.3a6.83 6.83 0 0 1 2.37 2.06c-1.1.6-1.9 1-2.9 1.6-1-1.6-2.6-2.5-4.5-2.8a6.52 6.52 0 0 1 5.03-.86Zm-8.47 16a6.83 6.83 0 0 1-2.37-2.06c1.1-.6 1.9-1 2.9-1.6 1 1.6 2.6 2.5 4.5 2.8a6.52 6.52 0 0 1-5.03.86Zm8.81-4.72a6.87 6.87 0 0 1-3.23.63c-.1-1.3-.2-2.2-.4-3.3 1.8-.6 3.4-1.6 4.6-3a6.62 6.62 0 0 1-.97 5.67ZM4.26 13.9a6.87 6.87 0 0 1-2.08-2.58c1.2-.6 2.1-1.1 3.2-1.7 0 1.9.4 3.7 1.2 5.3A6.62 6.62 0 0 1 4.26 13.9Zm3.02-9.67c1.1.2 2 .4 3 .7.1 1.3.2 2.2.4 3.2-1.8.6-3.4 1.6-4.6 3a6.87 6.87 0 0 1 1.2-6.9Zm12.12 3a6.87 6.87 0 0 1 2.08 2.58c-1.2.6-2.1 1.1-3.2 1.7 0-1.9-.4-3.7-1.2-5.3A6.62 6.62 0 0 1 19.4 7.23Zm-7.4 8.7a3.83 3.83 0 0 1-.7-3.8 3.86 3.86 0 0 1 4.5-2.2 3.83 3.83 0 0 1 .7 3.8 3.86 3.86 0 0 1-4.5 2.2Z" />
            </svg>
        ),
    },
    gemini: {
        name: 'Google Gemini',
        description: 'Fast multimodal conversion analysis',
        icon: (
            <svg viewBox="0 0 24 24" className="w-5 h-5 fill-current text-blue-500" >
                <path d="M12.01 0c.26 6.3 5.4 11.4 11.75 11.59-6.35.19-11.49 5.3-11.75 11.59C11.76 16.88 6.61 11.78.26 11.59 6.61 11.4 11.76 6.3 12.01 0Z" />
            </svg>
        ),
    },
};
