/**
 * Utility for generating random alphanumeric strings for identifiers.
 */
export function generateAlphanumericId(length: number = 10): string {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let result = '';
    const bytes = new Uint8Array(length);
    
    // Use crypto.getRandomValues if available (browser), otherwise fallback
    if (typeof crypto !== 'undefined' && crypto.getRandomValues) {
        crypto.getRandomValues(bytes);
        for (let i = 0; i < length; i++) {
            result += chars[bytes[i] % chars.length];
        }
    } else {
        // Fallback for environments without crypto (like some custom server setups)
        for (let i = 0; i < length; i++) {
            result += chars.charAt(Math.floor(Math.random() * chars.length));
        }
    }
    return result;
}
