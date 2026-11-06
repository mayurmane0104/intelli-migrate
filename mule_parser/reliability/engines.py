class RetryGenerator:
    """
    Wraps execution in exponential backoff patterns.
    """
    def generate_wrapper(self, target_function: str) -> str:
        return f"""
@retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(3))
def {target_function}_with_retry(*args, **kwargs):
    return {target_function}(*args, **kwargs)
"""

class DLQGenerator:
    """
    Connects dead letter queues for failed messages.
    """
    def generate_dlq_binding(self, queue_name: str) -> dict:
        return {
            "Type": "AWS::SQS::Queue",
            "Properties": {
                "QueueName": f"{queue_name}-dlq"
            }
        }

class IdempotencyGenerator:
    """
    Injects idempotency key handling.
    """
    def inject_idempotency_check(self, code_lines: list) -> list:
        # Simplistic injection for demo
        injection = [
            "    # Idempotency Check",
            "    idempotency_key = event.get('headers', {}).get('x-idempotency-key')",
            "    if idempotency_store.exists(idempotency_key):",
            "        return idempotency_store.get(idempotency_key)"
        ]
        
        # Inject after function def
        for i, line in enumerate(code_lines):
            if line.strip().startswith("def "):
                return code_lines[:i+1] + injection + code_lines[i+1:]
        
        return code_lines
