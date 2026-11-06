/**
 * Simple token estimation utility.
 * Heuristic: 1 token is roughly 4 characters for English/Source code.
 * This provides a consistent, deterministic baseline without external libraries.
 */
export function estimateTokens(text: string | null | undefined): number {
    if (!text) return 0;
    // Heuristic: characters / 4, rounded up.
    return Math.ceil(text.length / 4);
}
