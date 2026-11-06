import { describe, expect, it } from 'vitest';
import { calculateNovaCost } from '@/lib/utils/costCalculator';

describe('calculateNovaCost', () => {
    it('returns zero when no tokens are used', () => {
        expect(calculateNovaCost(0, 0)).toBe(0);
    });

    it('calculates the combined Nova Lite input and output cost', () => {
        const cost = calculateNovaCost(1_000_000, 500_000);
        expect(cost).toBeCloseTo(0.18, 10);
    });

    it('supports small per-file token totals', () => {
        const cost = calculateNovaCost(12_450, 3_200);
        expect(cost).toBeCloseTo(0.001515, 10);
    });
});
