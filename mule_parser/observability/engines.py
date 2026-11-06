class LoggingGenerator:
    """
    Transforms print statements into structured JSON logging.
    """
    def convert(self, code_lines: list) -> list:
        # Simplistic conversion for demo
        safe_code = ["import logging", "logger = logging.getLogger()", "logger.setLevel(logging.INFO)"]
        for line in code_lines:
            if "print(" in line:
                indent = line[:len(line) - len(line.lstrip())]
                msg = line.split("print(")[1].rstrip(")")
                safe_code.append(f"{indent}logger.info({{'flow': 'test', 'message': {msg}}})")
            else:
                safe_code.append(line)
        return safe_code

class MetricsGenerator:
    """
    Injects CloudWatch custom metrics.
    """
    def inject_metrics(self, code_lines: list) -> list:
        return code_lines # Mock logic

class TracingGenerator:
    """
    Injects OpenTelemetry / X-Ray tracing.
    """
    def inject_tracing(self, code_lines: list) -> list:
        return code_lines # Mock logic
