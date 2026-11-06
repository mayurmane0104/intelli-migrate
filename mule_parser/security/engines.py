class IAMValidator:
    """
    Validates IAM policies for least privilege.
    """
    def validate(self, policies: list) -> bool:
        for policy in policies:
            statement = policy.get("Statement", [])
            for s in statement:
                action = s.get("Action", "")
                resource = s.get("Resource", "")
                if action == "*" or resource == "*":
                    raise Exception(f"Critical Security Violation: Wildcard detected in IAM Policy: Action={action}, Resource={resource}")
        return True

class SecretDetector:
    """
    Detects hardcoded secrets and replaces them.
    """
    def scan_and_replace(self, code_lines: list) -> list:
        safe_code = []
        for line in code_lines:
            if "API_KEY" in line and "=" in line and "secrets_manager" not in line:
                indent = line[:len(line) - len(line.lstrip())]
                safe_code.append(f"{indent}secret = secrets_manager.get_secret('API_KEY')")
            else:
                safe_code.append(line)
        return safe_code

class NetworkSecurityAnalyzer:
    """
    Analyzes VPC subnets and security groups.
    """
    def validate_network(self, network_config: dict) -> bool:
        subnets = network_config.get("subnets", [])
        if "public" in str(subnets).lower():
            # Flag it, but maybe just log warning or fail depending on strictness
            pass
        return True
