def calculate_nova_cost(input_tokens: int, output_tokens: int) -> float:
    INPUT_PRICE_PER_M = 0.06
    OUTPUT_PRICE_PER_M = 0.24
    return (input_tokens / 1_000_000) * INPUT_PRICE_PER_M + (output_tokens / 1_000_000) * OUTPUT_PRICE_PER_M
