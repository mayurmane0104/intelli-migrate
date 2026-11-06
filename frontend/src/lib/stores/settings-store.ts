import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { LLMSettings, LLMProviderType } from '../types';

interface SettingsState {
    llm: LLMSettings;
    editor: {
        fontSize: number;
        theme: 'light' | 'dark' | 'vs-dark';
        lastUsedModel: string;
        showMinimap: boolean;
    };

    // Actions
    updateLLMSettings: (settings: Partial<LLMSettings>) => void;
    updateProviderKey: (provider: LLMProviderType, key: string) => void;
    updateProviderModel: (provider: LLMProviderType, model: string) => void;
    setEditorPreference: (key: string, value: any) => void;
}

const DEFAULT_LLM_SETTINGS: LLMSettings = {
    activeProvider: 'openai',
    providers: {
        nova: { enabled: false, apiKey: '', model: 'amazon.nova-lite-v1:0' },
        claude: { enabled: false, apiKey: '', model: 'claude-3-5-sonnet-20241022' },
        openai: { enabled: true, apiKey: '', model: 'gpt-4o-mini' },
        gemini: { enabled: false, apiKey: '', model: 'gemini-2.5-flash' },
    },
    theme: 'system',
    notifications: true,
};

export const useSettingsStore = create<SettingsState>()(
    persist(
        (set) => ({
            llm: DEFAULT_LLM_SETTINGS,
            editor: {
                fontSize: 12,
                theme: 'vs-dark',
                lastUsedModel: 'claude-3-5-sonnet-20240620',
                showMinimap: false,
            },

            updateLLMSettings: (updates) =>
                set((state) => ({
                    llm: { ...state.llm, ...updates }
                })),

            updateProviderKey: (provider, apiKey) =>
                set((state) => {
                    const p = provider as 'nova' | 'claude' | 'openai' | 'gemini';
                    return {
                        llm: {
                            ...state.llm,
                            providers: {
                                ...state.llm.providers,
                                [p]: { ...state.llm.providers[p], apiKey }
                            }
                        }
                    };
                }),

            updateProviderModel: (provider, model) =>
                set((state) => {
                    const p = provider as 'nova' | 'claude' | 'openai' | 'gemini';
                    return {
                        llm: {
                            ...state.llm,
                            providers: {
                                ...state.llm.providers,
                                [p]: { ...state.llm.providers[p], model }
                            }
                        }
                    };
                }),

            setEditorPreference: (key, value) =>
                set((state) => ({
                    editor: { ...state.editor, [key]: value }
                })),
        }),
        {
            name: 'ms-settings-storage', // Key in localStorage
            storage: createJSONStorage(() => localStorage),
        }
    )
);
