'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/contexts/AuthContext';
import { useApp } from '@/contexts/AppContext';
import { llmSettingsApi } from '@/lib/api';
import { MODEL_CATALOG, PROVIDER_INFO } from '@/lib/llm-provider';
import type { LLMSettings, LLMProviderType } from '@/lib/types';
import {
    BellIcon,
    MoonIcon,
    SunIcon,
    KeyIcon,
    SparklesIcon,
    EyeIcon,
    EyeSlashIcon,
    CheckCircleIcon,
    ExclamationCircleIcon,
    Cog6ToothIcon,
    ArrowPathIcon
} from '@heroicons/react/24/outline';
import { useTheme } from 'next-themes';

const CONFIGURABLE_PROVIDERS: (LLMProviderType)[] = ['nova', 'claude', 'openai', 'gemini'];
const DEFAULT_PROVIDER: LLMProviderType = 'nova';

export default function SettingsPage() {
    const { user } = useAuth();
    const { addToast, refreshLLMSettings, updateActiveLLMProvider } = useApp();

    const { theme, setTheme } = useTheme();
    const [mounted, setMounted] = useState(false);
    useEffect(() => setMounted(true), []);
    const [notifications, setNotifications] = useState(true);

    // LLM settings state
    const [llmSettings, setLlmSettings] = useState<LLMSettings | null>(null);
    const [llmLoading, setLlmLoading] = useState(true);
    const [llmSaving, setLlmSaving] = useState(false);
    const [editingProvider, setEditingProvider] = useState<LLMProviderType>('claude');
    const [showApiKey, setShowApiKey] = useState<Record<string, boolean>>({});
    const [apiKeyInputs, setApiKeyInputs] = useState<Record<string, string>>({});
    const [connectionStatus, setConnectionStatus] = useState<Record<string, { loading: boolean; success?: boolean; message?: string }>>({});

    // Load LLM settings
    useEffect(() => {
        llmSettingsApi.get()
            .then(({ settings }) => {
                setLlmSettings(settings);
                setNotifications(settings.notifications ?? true);
                if (settings.theme !== 'system' && settings.theme !== theme) {
                    setTheme(settings.theme);
                }
                setApiKeyInputs({
                    nova: settings.providers.nova.apiKey,
                    claude: settings.providers.claude.apiKey,
                    openai: settings.providers.openai.apiKey,
                    gemini: settings.providers.gemini.apiKey,
                });
            })
            .catch(() => { })
            .finally(() => setLlmLoading(false));
    }, [setTheme]);

    const handleSaveLLMSettings = async () => {
        if (!llmSettings) return;
        setLlmSaving(true);

        try {
            const settingsToSave: Partial<LLMSettings> = {
                activeProvider: llmSettings.activeProvider,
                theme: llmSettings.theme || theme || 'system',
                notifications: notifications,
                providers: {
                    nova: {
                        apiKey: apiKeyInputs.nova || '',
                        model: llmSettings.providers.nova.model,
                        enabled: llmSettings.providers.nova.enabled,
                    },
                    claude: {
                        apiKey: apiKeyInputs.claude || '',
                        model: llmSettings.providers.claude.model,
                        enabled: llmSettings.providers.claude.enabled,
                    },
                    openai: {
                        apiKey: apiKeyInputs.openai || '',
                        model: llmSettings.providers.openai.model,
                        enabled: llmSettings.providers.openai.enabled,
                    },
                    gemini: {
                        apiKey: apiKeyInputs.gemini || '',
                        model: llmSettings.providers.gemini.model,
                        enabled: llmSettings.providers.gemini.enabled,
                    },
                },
            };

            const { settings: saved } = await llmSettingsApi.save(settingsToSave);
            setLlmSettings(saved);
            setApiKeyInputs({
                claude: saved.providers.claude.apiKey,
                openai: saved.providers.openai.apiKey,
                gemini: saved.providers.gemini.apiKey,
            });
            addToast({ type: 'success', title: 'AI Settings Saved', message: 'Neural configuration updated successfully.' });
            refreshLLMSettings();
        } catch {
            addToast({ type: 'error', title: 'Error', message: 'Failed to preserve neural settings.' });
        }
        setLlmSaving(false);
    };

    const handleTestConnection = async (provider: LLMProviderType) => {
        if (!llmSettings) return;
        setConnectionStatus(prev => ({ ...prev, [provider]: { loading: true } }));

        try {
            const result = await llmSettingsApi.testConnection({
                provider,
                apiKey: apiKeyInputs[provider],
                model: llmSettings.providers[provider].model,
            });

            setConnectionStatus(prev => ({
                ...prev,
                [provider]: {
                    loading: false,
                    success: result.success,
                    message: result.message
                }
            }));

            if (result.success) {
                addToast({ type: 'success', title: 'Connection Successful', message: `Successfully connected to ${PROVIDER_INFO[provider].name}` });
            } else {
                addToast({ type: 'error', title: 'Connection Failed', message: result.message });
            }
        } catch (err: any) {
            setConnectionStatus(prev => ({
                ...prev,
                [provider]: {
                    loading: false,
                    success: false,
                    message: err.message || 'Connection test failed'
                }
            }));
            addToast({ type: 'error', title: 'Error', message: 'Failed to test connection.' });
        }
    };

    const toggleProviderEnabled = async (provider: LLMProviderType) => {
        if (!llmSettings) return;
        const isCurrentlyActive = llmSettings.activeProvider === provider;
        const willBeEnabled = !llmSettings.providers[provider].enabled;

        const fallbackProvider = CONFIGURABLE_PROVIDERS.find(item => item !== provider && llmSettings.providers[item].enabled) || DEFAULT_PROVIDER;
        const updated = {
            ...llmSettings,
            activeProvider: (isCurrentlyActive && !willBeEnabled) ? fallbackProvider : llmSettings.activeProvider,
            providers: {
                ...llmSettings.providers,
                [provider]: { ...llmSettings.providers[provider], enabled: willBeEnabled },
            },
        };
        setLlmSettings(updated);
        try {
            await llmSettingsApi.save(updated);
            refreshLLMSettings();
            if (isCurrentlyActive && !willBeEnabled) {
                updateActiveLLMProvider(fallbackProvider);
            }
        } catch { }
    };



    const setProviderModel = async (provider: LLMProviderType, model: string) => {
        if (!llmSettings) return;
        const updated = {
            ...llmSettings,
            providers: {
                ...llmSettings.providers,
                [provider]: { ...llmSettings.providers[provider], model },
            },
        };
        setLlmSettings(updated);
        try {
            await llmSettingsApi.save(updated);
            refreshLLMSettings();
        } catch { }
    };

    const handleThemeChange = async (newTheme: 'light' | 'dark' | 'system') => {
        setTheme(newTheme);
        if (!llmSettings) return;
        const updated = { ...llmSettings, theme: newTheme };
        setLlmSettings(updated);
        try {
            await llmSettingsApi.save(updated);
            refreshLLMSettings();
        } catch { }
    };

    const handleNotificationsChange = async (enabled: boolean) => {
        setNotifications(enabled);
        if (!llmSettings) return;
        const updated = { ...llmSettings, notifications: enabled };
        setLlmSettings(updated);
        try {
            await llmSettingsApi.save(updated);
            refreshLLMSettings();
        } catch { }
    };

    const initials = user?.name ? user.name.split(' ').map(n => n[0]).join('').toUpperCase() : 'U';

    return (
        <div className="alignment-grid animate-fade-in">
            <div className="mb-2 flex items-center gap-3">
                <div className="p-2.5 bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-400 rounded-2xl shadow-inner">
                    <Cog6ToothIcon className="h-7 w-7" />
                </div>
                <div>
                    <h1 className="text-3xl font-black text-gray-900 dark:text-gray-100 tracking-tight">Global Control</h1>
                    <p className="text-gray-500 dark:text-gray-400 text-xs font-semibold mt-1 uppercase tracking-widest">Neural Configuration & Environment Tuning</p>
                </div>
            </div>

            <div className="space-y-8 mt-4">
                {/* ══════════════════════════════════════
                   AI Provider Settings
                   ────────────────────────────────────── */}
                <section className="glass-card rounded-3xl overflow-hidden">
                    <div className="px-6 py-5 border-b border-gray-100/50 dark:border-gray-800/50 bg-gradient-to-r from-violet-50/50 to-blue-50/50 dark:from-violet-900/10 dark:to-blue-900/10">
                        <div className="flex items-center gap-3">
                            <SparklesIcon className="h-6 w-6 text-violet-600" />
                            <h3 className="text-lg font-black text-gray-900 dark:text-gray-100 tracking-tight">Intelligence Arrays</h3>
                        </div>
                        <p className="text-xs font-semibold text-gray-400 uppercase tracking-widest mt-1.5 ml-9">Configure and enable active LLM modules</p>
                    </div>

                    {llmLoading ? (
                        <div className="p-12 text-center text-gray-400 text-xs font-black uppercase tracking-widest animate-pulse">Syncing neural state...</div>
                    ) : llmSettings ? (
                        <div className="p-8 space-y-8">
                            {/* Information Box (Refined) */}
                            <div className="bg-primary-50/30 dark:bg-primary-900/10 border border-primary-100/50 dark:border-primary-800/30 rounded-2xl p-5 flex items-start gap-4">
                                <div className="p-2 bg-primary-100 dark:bg-primary-900/50 rounded-xl text-primary-600 shrink-0">
                                    <ExclamationCircleIcon className="h-5 w-5" />
                                </div>
                                <div>
                                    <h4 className="text-xs font-black text-primary-700 dark:text-primary-300 uppercase tracking-widest mb-1">Architecture Note</h4>
                                    <p className="text-xs text-gray-500 dark:text-gray-400 font-medium leading-relaxed">
                                        Enable the providers you wish to utilize. Once verified, these models will be dynamically accessible within the
                                        <span className="text-primary-600 font-bold px-1.5 py-0.5 mx-1 bg-primary-50 dark:bg-primary-900/20 rounded">Inference Editor</span>
                                        during active migration sessions.
                                    </p>
                                </div>
                            </div>

                            {/* Provider Configuration Tabs */}
                            <div>
                                <div className="flex items-center gap-1.5 bg-gray-100 dark:bg-gray-800/50 border border-gray-200/50 dark:border-gray-700/50 rounded-2xl p-1.5 mb-8">
                                    {CONFIGURABLE_PROVIDERS.map(provider => {
                                        const isEnabled = llmSettings.providers[provider].enabled;
                                        const isActive = editingProvider === provider;
                                        return (
                                            <button key={provider} onClick={() => setEditingProvider(provider)}
                                                className={`flex-1 flex items-center justify-center gap-2.5 px-4 py-3 text-[10px] font-black uppercase tracking-widest rounded-xl transition-all relative ${isActive
                                                    ? 'bg-white dark:bg-gray-900 text-primary-600 shadow-xl shadow-primary-500/10 border border-primary-100/50 dark:border-primary-900/30'
                                                    : 'text-gray-400 hover:text-gray-600 dark:hover:text-gray-300'
                                                    }`}>
                                                <span className="grayscale-0 scale-125">{PROVIDER_INFO[provider].icon}</span>
                                                {PROVIDER_INFO[provider].name}
                                                {isEnabled && (
                                                    <span className="absolute top-2 right-2 w-2 h-2 bg-emerald-500 rounded-full shadow-[0_0_8px_rgba(16,185,129,0.8)] animate-pulse" />
                                                )}
                                            </button>
                                        );
                                    })}
                                </div>

                                {/* Provider Config Card (Refined) */}
                                {(() => {
                                    const provider = editingProvider;
                                    const config = llmSettings.providers[provider];
                                    const info = PROVIDER_INFO[provider];
                                    const models = MODEL_CATALOG[provider];

                                    return (
                                        <div className="space-y-8 animate-fade-in translate-y-0">
                                            {/* Header + Enable Toggle */}
                                            <div className="flex items-center justify-between pb-6 border-b border-gray-100 dark:border-gray-800/50">
                                                <div className="flex items-center gap-4">
                                                    <div className="w-14 h-14 rounded-2xl bg-white dark:bg-gray-900 flex items-center justify-center text-3xl shadow-sm border border-gray-100 dark:border-gray-800">
                                                        {info.icon}
                                                    </div>
                                                    <div>
                                                        <h4 className="text-xl font-black text-gray-900 dark:text-gray-100 tracking-tight">
                                                            {info.name} Integration
                                                        </h4>
                                                        <p className="text-xs font-semibold text-gray-400 mt-1">{info.description}</p>
                                                    </div>
                                                </div>
                                                <div className="flex items-center gap-4">
                                                    <span className={`text-[10px] font-black uppercase tracking-widest ${config.enabled ? 'text-emerald-600' : 'text-gray-400'}`}>
                                                        {config.enabled ? 'Online' : 'Disabled'}
                                                    </span>
                                                    <button onClick={() => toggleProviderEnabled(provider)}
                                                        className={`relative inline-flex h-7 w-12 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-all duration-300 ${config.enabled ? 'bg-emerald-500' : 'bg-gray-200 dark:bg-gray-700'}`}>
                                                        <span className={`pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white dark:bg-gray-950 shadow-lg ring-0 transition duration-300 ease-in-out ${config.enabled ? 'translate-x-5' : 'translate-x-0'}`} />
                                                    </button>
                                                </div>
                                            </div>

                                            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                                                {/* API Key Section */}
                                                <div className="space-y-4">
                                                    <div className="flex items-center justify-between">
                                                        <label className="text-[10px] font-black text-gray-400 uppercase tracking-widest">Secret Endpoint Token</label>
                                                        {config.enabled && (
                                                            <button
                                                                onClick={() => handleTestConnection(provider)}
                                                                disabled={connectionStatus[provider]?.loading}
                                                                className="text-[9px] font-black uppercase tracking-widest text-primary-600 hover:text-primary-700 flex items-center gap-1.5 px-3 py-1 bg-primary-50 dark:bg-primary-900/20 rounded-lg border border-primary-100/50 transition-all"
                                                            >
                                                                {connectionStatus[provider]?.loading ? 'Pinging...' : 'Verify Socket'}
                                                            </button>
                                                        )}
                                                    </div>
                                                    <div className="relative group">
                                                        <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                                            <KeyIcon className="h-4 w-4 text-gray-400 group-focus-within:text-primary-500 transition-colors" />
                                                        </div>
                                                        <input
                                                            type={showApiKey[provider] ? 'text' : 'password'}
                                                            value={apiKeyInputs[provider] || ''}
                                                            onChange={e => setApiKeyInputs(prev => ({ ...prev, [provider]: e.target.value }))}
                                                            placeholder={provider === 'claude' ? 'sk-ant-...' : provider === 'openai' ? 'sk-...' : 'AIza...'}
                                                            className="block w-full pl-11 pr-12 py-3 border-2 border-gray-100 dark:border-gray-800 bg-white dark:bg-gray-950 rounded-2xl text-sm font-mono focus:border-primary-500 focus:ring-0 transition-all disabled:opacity-50"
                                                            disabled={!config.enabled}
                                                        />
                                                        <button
                                                            type="button"
                                                            onClick={async () => {
                                                                const isCurrentlyShowing = showApiKey[provider];
                                                                if (!isCurrentlyShowing) {
                                                                    // Fetch unmasked for this session if revealing
                                                                    try {
                                                                        const { settings } = await llmSettingsApi.getUnmasked();
                                                                        setApiKeyInputs(prev => ({
                                                                            ...prev,
                                                                            claude: settings.providers.claude.apiKey,
                                                                            openai: settings.providers.openai.apiKey,
                                                                            gemini: settings.providers.gemini.apiKey,
                                                                        }));
                                                                    } catch (e) {
                                                                        console.error('Failed to reveal keys', e);
                                                                    }
                                                                }
                                                                setShowApiKey(prev => ({ ...prev, [provider]: !prev[provider] }));
                                                            }}
                                                            className="absolute inset-y-0 right-0 pr-4 flex items-center text-gray-400 hover:text-gray-600 transition-colors"
                                                        >
                                                            {showApiKey[provider] ? <EyeSlashIcon className="h-5 w-5" /> : <EyeIcon className="h-5 w-5" />}
                                                        </button>
                                                    </div>
                                                    {connectionStatus[provider]?.message && (
                                                        <div className={`p-3 rounded-xl border flex items-center gap-3 animate-fade-in ${connectionStatus[provider]?.success ? 'bg-emerald-50/50 border-emerald-100 text-emerald-700' : 'bg-rose-50/50 border-rose-100 text-rose-700'}`}>
                                                            {connectionStatus[provider]?.success ? <CheckCircleIcon className="h-4 w-4" /> : <ExclamationCircleIcon className="h-4 w-4" />}
                                                            <p className="text-[11px] font-bold">{connectionStatus[provider]?.message}</p>
                                                        </div>
                                                    )}
                                                </div>

                                                {/* Model Selection grid */}
                                                <div className="space-y-4">
                                                    <label className="text-[10px] font-black text-gray-400 uppercase tracking-widest">Model Precision</label>
                                                    <div className="grid grid-cols-1 gap-2.5">
                                                        {models.map(model => (
                                                            <button key={model.id}
                                                                onClick={() => setProviderModel(provider, model.id)}
                                                                disabled={!config.enabled}
                                                                className={`group/model flex items-center justify-between p-4 rounded-2xl border-2 transition-all ${config.model === model.id
                                                                    ? 'border-primary-500 bg-primary-50/50 dark:bg-primary-900/10'
                                                                    : 'border-gray-100 dark:border-gray-800 bg-white dark:bg-gray-950 hover:border-gray-200 dark:hover:border-gray-700'
                                                                    } disabled:opacity-30`}>
                                                                <div>
                                                                    <p className="text-sm font-bold text-gray-800 dark:text-gray-200 tracking-tight">{model.name}</p>
                                                                    <p className="text-[10px] font-semibold text-gray-500 dark:text-gray-400 mt-0.5">{model.description}</p>
                                                                </div>
                                                                <div className={`w-5 h-5 rounded-full border-2 flex items-center justify-center transition-all ${config.model === model.id ? 'border-primary-500 bg-primary-500 shadow-lg shadow-primary-500/30' : 'border-gray-200'}`}>
                                                                    {config.model === model.id && <CheckCircleIcon className="h-4 w-4 text-white" />}
                                                                </div>
                                                            </button>
                                                        ))}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    );
                                })()}
                            </div>

                            {/* Save Action */}
                            <div className="flex items-center justify-between pt-8 border-t border-gray-100/50 dark:border-gray-800/50">
                                <span className="text-[10px] font-black text-gray-400 uppercase tracking-widest italic flex items-center gap-2">
                                    <span className="w-1.5 h-1.5 rounded-full bg-primary-500 inline-block" />
                                    Neural persistence activated
                                </span>
                                <button onClick={handleSaveLLMSettings} disabled={llmSaving}
                                    className="px-8 py-3 bg-gray-900 dark:bg-primary-600 hover:bg-gray-800 dark:hover:bg-primary-700 disabled:opacity-50 text-white text-[10px] font-black uppercase tracking-widest rounded-2xl transition-all shadow-xl shadow-gray-200 dark:shadow-none flex items-center gap-3">
                                    {llmSaving ? (
                                        <>
                                            <ArrowPathIcon className="h-4 w-4 animate-spin text-primary-400" />
                                            Synchronizing...
                                        </>
                                    ) : (
                                        <>
                                            <CheckCircleIcon className="h-4 w-4 text-primary-400" />
                                            Preserve Evolution
                                        </>
                                    )}
                                </button>
                            </div>
                        </div>
                    ) : (
                        <div className="p-16 text-center">
                            <div className="w-16 h-16 bg-rose-50 dark:bg-rose-900/10 rounded-2xl flex items-center justify-center mx-auto mb-4 border border-rose-100">
                                <ExclamationCircleIcon className="h-8 w-8 text-rose-500" />
                            </div>
                            <h3 className="text-lg font-black text-gray-900 dark:text-gray-100 tracking-tight">Cerebro Link Failed</h3>
                            <p className="text-xs font-semibold text-gray-500 mt-1 uppercase tracking-widest">Unable to synchronize global settings</p>
                        </div>
                    )}
                </section>

                {/* ══════════════════════════════════════
                   Preferences Settings
                   ────────────────────────────────────── */}
                <section className="glass-card rounded-3xl overflow-hidden mb-12">
                    <div className="px-6 py-5 border-b border-gray-100/50 dark:border-gray-800/50 bg-gray-50/50 dark:bg-gray-800/20">
                        <div className="flex items-center gap-3">
                            <Cog6ToothIcon className="h-6 w-6 text-gray-400" />
                            <h3 className="text-lg font-black text-gray-900 dark:text-gray-100 tracking-tight">System Environment</h3>
                        </div>
                        <p className="text-xs font-semibold text-gray-400 uppercase tracking-widest mt-1.5 ml-9">UI Aesthetics & Global Behaviors</p>
                    </div>

                    <div className="p-8 grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div className="flex items-center justify-between p-6 bg-white/40 dark:bg-gray-900/20 rounded-2xl border border-gray-100 dark:border-gray-800">
                            <div className="flex items-center gap-4">
                                <div className="p-3 bg-amber-100/50 dark:bg-amber-900/10 rounded-2xl">
                                    {mounted && theme === 'light' ? <SunIcon className="h-6 w-6 text-amber-600" /> : <MoonIcon className="h-6 w-6 text-gray-400" />}
                                </div>
                                <div>
                                    <p className="text-sm font-black text-gray-900 dark:text-gray-100 tracking-tight">Chromatic Interface</p>
                                    <p className="text-[10px] font-semibold text-gray-400 uppercase tracking-widest mt-0.5">Global Theme Toggle</p>
                                </div>
                            </div>
                            <div className="flex bg-gray-100 dark:bg-gray-800 p-1.5 rounded-xl border border-gray-200/50 dark:border-gray-700/50">
                                <button onClick={() => handleThemeChange('light')}
                                    className={`px-4 py-2 text-[10px] font-black uppercase tracking-widest rounded-lg transition-all ${mounted && theme === 'light' ? 'bg-white dark:bg-gray-900 shadow-xl text-primary-600' : 'text-gray-400 hover:text-gray-600'}`}>
                                    Lumen
                                </button>
                                <button onClick={() => handleThemeChange('dark')}
                                    className={`px-4 py-2 text-[10px] font-black uppercase tracking-widest rounded-lg transition-all ${mounted && theme === 'dark' ? 'bg-white dark:bg-gray-900 shadow-xl text-primary-600' : 'text-gray-400 hover:text-gray-600'}`}>
                                    Nox
                                </button>
                            </div>
                        </div>

                        <div className="flex items-center justify-between p-6 bg-white/40 dark:bg-gray-900/20 rounded-2xl border border-gray-100 dark:border-gray-800">
                            <div className="flex items-center gap-4">
                                <div className="p-3 bg-primary-100/50 dark:bg-primary-900/10 rounded-2xl">
                                    <BellIcon className="h-6 w-6 text-primary-600" />
                                </div>
                                <div>
                                    <p className="text-sm font-black text-gray-900 dark:text-gray-100 tracking-tight">Telemetry Stream</p>
                                    <p className="text-[10px] font-semibold text-gray-400 uppercase tracking-widest mt-0.5">Email Notifications</p>
                                </div>
                            </div>
                            <button onClick={() => handleNotificationsChange(!notifications)}
                                className={`relative inline-flex h-7 w-12 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-all duration-300 ${notifications ? 'bg-primary-500' : 'bg-gray-200 dark:bg-gray-700'}`}>
                                <span className={`pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow ring-0 transition duration-300 ${notifications ? 'translate-x-5' : 'translate-x-0'}`} />
                            </button>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    );
}
