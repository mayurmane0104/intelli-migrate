const INPUT_PRICE_PER_M = 0.06;
const OUTPUT_PRICE_PER_M = 0.24;

export function calculateNovaCost(inputTokens: number, outputTokens: number): number {
    return (inputTokens / 1_000_000) * INPUT_PRICE_PER_M
        + (outputTokens / 1_000_000) * OUTPUT_PRICE_PER_M;
}
