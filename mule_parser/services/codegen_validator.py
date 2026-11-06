"""
services/codegen_validator.py — Post-generation validation for LLM-generated code.

Validates that generated handler code:
 1. Contains references to every Mule component in the migration decisions.
 2. Has no forbidden placeholder patterns (TODO, FIXME, stubs, etc.).
 3. Passes a basic syntax check appropriate to the target runtime.
 4. Has a valid Lambda entry point.
 5. Preserves SQL table names.
 6. Uses parallel constructs for scatter-gather.
 7. Has DataWeave conversion constructs.
 8. Obeys mandatory rules (forbidden patterns).

[Layer 8 — IaC Structural Validation]
 9. Lossy mapping compliance: BEHAVIORAL_LOSS comments present for is_lossy components.
10. CloudWatch observability: at least one structured log call present.
11. Environment variable naming: all env refs use SCREAMING_SNAKE_CASE.
12. No hardcoded AWS account IDs / secrets present in generated code.

Returns a ValidationResult that the LLM code generator uses to decide
whether to accept, retry, or fall back to the legacy template engine.
"""
from __future__ import annotations

import ast
import os
import re
import subprocess
import tempfile
from dataclasses import dataclass, field
from typing import Any

# Hardcoded secrets / account ID patterns (Layer 8, Check 12)
_HARDCODED_SECRET_PATTERNS: list[re.Pattern] = [
    re.compile(r"AKIA[0-9A-Z]{16}"),                   # AWS Access Key ID
    re.compile(r"aws_secret_access_key\s*=\s*['\"][^'\"]+['\"]", re.IGNORECASE),
    re.compile(r"\b[0-9]{12}\b"),                       # 12-digit AWS account ID literal
    re.compile(r"password\s*=\s*['\"][^'\"]{8,}['\"]", re.IGNORECASE),
    re.compile(r"secret\s*=\s*['\"][^'\"]{8,}['\"]", re.IGNORECASE),
]

# Environment variable name pattern — must be SCREAMING_SNAKE_CASE (Layer 8, Check 11)
_ENV_VAR_RE = re.compile(
    r'(?:os\.environ\[|process\.env\.)(\w+)',
)
_SCREAMING_SNAKE_RE = re.compile(r'^[A-Z][A-Z0-9_]*$')

# Patterns that indicate placeholder / incomplete code
_PLACEHOLDER_PATTERNS: list[re.Pattern] = [
    re.compile(r"\bTODO\b"),
    re.compile(r"\bFIXME\b"),
    re.compile(r"\bXXX\b"),
    re.compile(r"\bplaceholder\b", re.IGNORECASE),
    re.compile(r"\bstub\b", re.IGNORECASE),
    re.compile(r"\bNotImplementedError\b"),
    re.compile(r"\bNotImplemented\b"),
    re.compile(r"pass\s*#"),           # pass # ... in Python
    re.compile(r"//\s*TODO"),          # // TODO in TypeScript
    re.compile(r"raise\s+NotImplementedError"),
    re.compile(r"throw\s+new\s+Error\(['\"]Not implemented"),
]

# Aliases that map Mule component names to code identifiers the LLM typically uses
_COMPONENT_ALIASES: dict[str, list[str]] = {
    "salesforce":        ["salesforce", "sf", "simple_salesforce", "jsforce", "Salesforce"],
    "db:select":         ["SELECT", "select", "db_select", "query", "execute", "conn.run", "cursor"],
    "db:insert":         ["INSERT", "insert", "db_insert"],
    "db:update":         ["UPDATE", "update", "db_update"],
    "db:delete":         ["DELETE", "delete", "db_delete"],
    "jms:listener":      ["sqs", "SQS", "Records", "receive_message"],
    "jms:publish":       ["send_message", "publish", "sqs"],
    "scatter-gather":    ["gather", "Promise.all", "Promise.allSettled", "asyncio.gather", "ThreadPoolExecutor", "Thread", "Pool", "concurrent.futures", "executor"],
    "scatter_gather":    ["gather", "Promise.all", "Promise.allSettled", "asyncio.gather", "ThreadPoolExecutor", "Thread", "Pool", "concurrent.futures", "executor"],
    "ee:transform":      ["transform", "def transform", "function transform", "map(", ".map(", "csv", "join", "dedup", "sort"],
    "http:listener":     ["handler", "APIGateway", "statusCode", "httpMethod"],
    "scheduler":         ["EventBridge", "scheduler", "detail-type", "scheduled"],
    "email:send":        ["ses", "SES", "send_email", "sendMail", "MIMEMultipart"],
    "s3:put-object":     ["s3", "S3", "put_object", "PutObjectCommand"],
    "s3:get-object":     ["s3", "S3", "get_object", "GetObjectCommand"],
    "flow-ref":          ["def ", "async def ", "function ", "async function ", "invoke", "FunctionName", "lambda", "process", "delegat"],
}


@dataclass
class ValidationResult:
    valid: bool
    issues: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def validate_generated_code(
    code: str,
    ctx: Any,  # GenerationContext (avoiding tight import coupling here)
    target_runtime: str,
    *,
    entry_point: str = "handler",
    test_code: str = "",
) -> ValidationResult:
    """
    Validate LLM-generated handler code.

    Args:
        code:                 The generated handler code string.
        ctx:                  The GenerationContext for this flow.
        target_runtime:       "nodejs" | "python"

    Returns:
        ValidationResult with valid=True if all checks pass.
    """
    issues: list[str] = []
    warnings: list[str] = []
    
    component_decisions = ctx.component_decisions if hasattr(ctx, "component_decisions") else []

    if not code or not code.strip():
        return ValidationResult(valid=False, issues=["Generated code is empty."])

    # ── Check 1: No placeholder patterns ─────────────────────────────────────
    for pattern in _PLACEHOLDER_PATTERNS:
        match = pattern.search(code)
        if match:
            issues.append(f"Forbidden placeholder detected: '{match.group()}' at position {match.start()}")

    # ── Check 2: Component coverage ───────────────────────────────────────────
    for decision in component_decisions:
        source = (decision.get("source") or "").lower()
        if not source:
            continue
        # Skip components that go to ManualReview — they don't need code coverage
        if decision.get("manual_review"):
            continue
        if _should_skip_component_coverage(decision):
            continue
        if not _is_component_referenced(source, code):
            issues.append(
                f"Component '{decision.get('source', source)}' (→ {decision.get('target', '?')}) "
                f"has no corresponding code in the generated handler."
            )

    # ── Check 3: Lambda handler / service entry point ─────────────────────────
    if not _has_handler_entry_point(code, target_runtime, entry_point=entry_point):
        if entry_point == "process":
            issues.append(
                "No service entry point found. "
                "Python canonical service modules must define 'def process(event, context)'."
            )
        else:
            issues.append(
                "No Lambda handler entry point found. "
                "Python: 'def handler(event, context)' or 'def main(event, context)'. "
                "TypeScript: 'export.*handler\\s*=' or 'export.*main\\s*='."
            )

    # ── Check 4: Syntax check & Static Analysis ───────────────────────────────
    syntax_issue = _check_syntax(code, target_runtime)
    if syntax_issue:
        issues.append(syntax_issue)
    
    if target_runtime.lower().startswith("python"):
        static_issues = _run_static_analysis(code, target_runtime)
        if static_issues:
            issues.extend(static_issues)
            
        if test_code:
            sandbox_issues = _run_sandbox_tests(code, test_code)
            if sandbox_issues:
                issues.extend(sandbox_issues)

    # ── Check 5: SQL semantics preservation ───────────────────────────────────
    if hasattr(ctx, "sql_semantics") and ctx.sql_semantics:
        for sql_op in ctx.sql_semantics:
            table = sql_op.get("table")
            if table and table not in code:
                issues.append(f"SQL preservation failure: Table '{table}' from IR is missing from generated code.")

    # ── Check 6: Scatter-Gather Parallelism ───────────────────────────────────
    if hasattr(ctx, "scatter_gather_routes") and ctx.scatter_gather_routes:
        if target_runtime.lower().startswith("python"):
            if "asyncio.gather" not in code and "Thread" not in code and "Pool" not in code:
                issues.append("Scatter-gather failure: Missing asyncio.gather or parallel construct in Python code.")
        else:
            if "Promise.all" not in code:
                issues.append("Scatter-gather failure: Missing Promise.all in TypeScript code.")

    # ── Check 7: DataWeave Completeness ───────────────────────────────────────
    if hasattr(ctx, "dataweave_scripts") and ctx.dataweave_scripts:
        # Rough check: if there are 3 DW scripts, we expect substantial transformation logic.
        # We can't perfectly count lines, but we can verify mapping constructs exist.
        if "map" not in code and "list(" not in code and "{" not in code:
            issues.append("DataWeave failure: Found DW scripts in IR, but no obvious collection mapping or object construction in code.")

    # ── Check 8: Rule Compliance ──────────────────────────────────────────────
    if hasattr(ctx, "mandatory_rules") and ctx.mandatory_rules:
        rules = ctx.mandatory_rules if isinstance(ctx.mandatory_rules, (list, tuple)) else [ctx.mandatory_rules]
        for rule in rules:
            if isinstance(rule, dict):
                if forbidden := rule.get("forbidden", []):
                    for f in forbidden:
                        if f.lower() in code.lower():
                            issues.append(f"Rule violation: Used forbidden service/pattern '{f}'.")

    # ── Check 9 [Layer 8]: Lossy mapping compliance ────────────────────
    # For every component decision marked is_lossy=True, the generated code MUST contain
    # a # BEHAVIORAL_LOSS comment. The LLM system prompt (Rule 13) requires this.
    # This check enforces it deterministically so non-compliant code triggers a retry.
    if hasattr(ctx, "component_decisions"):
        for decision in ctx.component_decisions:
            if decision.get("is_lossy") or decision.get("mapping_rule_used", {}).get("is_lossy"):
                if "BEHAVIORAL_LOSS" not in code:
                    source = decision.get("source", "unknown")
                    issues.append(
                        f"Layer 8/Check 9: Lossy mapping for '{source}' is missing required "
                        "# BEHAVIORAL_LOSS: comment. Add it to document behaviors that cannot be auto-migrated."
                    )
                    break  # One issue is enough to trigger a retry

    # ── Check 10 [Layer 8]: CloudWatch observability ───────────────────
    # Every Lambda handler MUST emit at least one structured log call.
    # This catches the "missing observability" quality gap flagged in the IR.
    _log_patterns = ["logger.", "logging.", "print(", "console.log", "console.error", "CloudWatch"]
    if not any(pat in code for pat in _log_patterns):
        if hasattr(ctx, "missing_practices"):
            if any("log" in p.lower() or "observ" in p.lower() for p in (ctx.missing_practices or [])):
                issues.append(
                    "Layer 8/Check 10: IR quality layer flags missing logging, but generated code "
                    "has no logger/print/console calls. Add CloudWatch-compatible structured logging."
                )
        else:
            warnings.append(
                "Layer 8/Check 10: No logging calls detected in generated handler. "
                "Add structured logging for CloudWatch observability."
            )

    # ── Check 11 [Layer 8]: Environment variable naming ────────────────
    # All env var references must use SCREAMING_SNAKE_CASE.
    # Lowercase env vars are an operational hazard in AWS Lambda.
    for match in _ENV_VAR_RE.finditer(code):
        var_name = match.group(1)
        if not _SCREAMING_SNAKE_RE.match(var_name):
            warnings.append(
                f"Layer 8/Check 11: Environment variable '{var_name}' is not SCREAMING_SNAKE_CASE. "
                "AWS Lambda conventions require uppercase env var names."
            )

    # ── Check 12 [Layer 8]: No hardcoded secrets ─────────────────────
    # Hardcoded AWS credentials or account IDs in generated code are a critical failure.
    for pattern in _HARDCODED_SECRET_PATTERNS:
        match = pattern.search(code)
        if match:
            issues.append(
                f"Layer 8/Check 12 [CRITICAL]: Hardcoded secret/account-ID pattern detected: "
                f"'{match.group()[:20]}...' — use os.environ or AWS Secrets Manager instead."
            )

    # ── Warnings (non-blocking) ─────────────────────────────────────────
    if "os.environ" not in code and "process.env" not in code:
        warnings.append("No environment variable references found — check credentials handling.")

    return ValidationResult(
        valid=len(issues) == 0,
        issues=issues,
        warnings=warnings,
    )


def _should_skip_component_coverage(decision: dict[str, Any]) -> bool:
    """Skip Mule doc-names and flow-ref steps that are not literal code identifiers."""
    source = (decision.get("source") or "").lower()
    target = (decision.get("target") or "")

    if "flow-ref" in source or target in {
        "InternalFunctionCall", "LambdaMethod", "LambdaResponse",
    }:
        return True

    # DataWeave / transform doc names (no Mule namespace prefix) are covered
    # by the DataWeave completeness check, not by literal string matching.
    if ":" not in source and any(
        token in source for token in ("transform", "collection", "csv", "mapping", "aggregate", "flow")
    ):
        return True

    return False


def _is_component_referenced(source: str, code: str) -> bool:
    """Check if a Mule component is meaningfully referenced in the generated code."""
    # Check direct mention of the component name (e.g. "db:select")
    if source.lower() in code.lower():
        return True
    # Check known aliases
    for key, aliases in _COMPONENT_ALIASES.items():
        if key in source:
            if any(alias in code for alias in aliases):
                return True
    # Generic keyword extraction — check if the major noun from the source appears
    parts = re.split(r"[:\-_.]", source)
    main_noun = parts[-1] if parts else source
    if len(main_noun) >= 3 and main_noun.lower() in code.lower():
        return True
    return False


def _has_handler_entry_point(code: str, target_runtime: str, *, entry_point: str = "handler") -> bool:
    if target_runtime.lower().startswith("node"):
        if entry_point == "process":
            return bool(re.search(r"export\s+(async\s+)?function\s+process", code))
        return bool(re.search(
            r"export\s+(async\s+)?(const\s+handler\s*=|function\s+handler|function\s+main)",
            code,
        ))
    if entry_point == "process":
        return bool(re.search(r"def\s+process\s*\(", code))
    return bool(re.search(r"def\s+(handler|main|lambda_handler)\s*\(", code))


def _check_syntax(code: str, target_runtime: str) -> str | None:
    """Returns an error message if syntax is clearly broken, or None."""
    if target_runtime.lower().startswith("python"):
        try:
            ast.parse(code)
        except SyntaxError as exc:
            return f"Python syntax error: {exc}"
    else:
        # TypeScript: basic brace balance check (full TS parser not available)
        opens = code.count("{")
        closes = code.count("}")
        if abs(opens - closes) > 2:
            return f"TypeScript brace imbalance: {{={opens}, }}={closes}"
    return None


def _run_static_analysis(code: str, target_runtime: str) -> list[str]:
    """Run Flake8 to catch undefined variables, missing imports, and severe syntax errors."""
    issues = []
    if not target_runtime.lower().startswith("python"):
        return issues
        
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        temp_path = f.name
        
    try:
        # Run flake8. --select=F,E9 ensures we only catch critical logic/syntax errors
        # F821 = undefined name, F401 = unused import, E9 = syntax error
        result = subprocess.run(
            ['flake8', '--select=F,E9', temp_path],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            for line in result.stdout.splitlines():
                parts = line.split(":", 3)
                if len(parts) >= 4:
                    issues.append(f"Static Analysis Error at line {parts[1]}:{parts[3].strip()}")
                else:
                    issues.append(f"Static Analysis Error: {line.strip()}")
    except FileNotFoundError:
        # flake8 is not installed, fail gracefully but add a warning if we had a warnings list
        pass
    except Exception as e:
        issues.append(f"Linter execution failed: {e}")
    finally:
        try:
            os.unlink(temp_path)
        except Exception:
            pass
            
    return issues


def _run_sandbox_tests(code: str, test_code: str) -> list[str]:
    """Write handler and tests to a temp directory and run pytest."""
    issues = []
    
    with tempfile.TemporaryDirectory() as temp_dir:
        handler_path = os.path.join(temp_dir, "handler.py")
        test_path = os.path.join(temp_dir, "test_handler.py")
        
        # Stub common project modules so isolated sandbox tests can run
        exceptions_stub = (
            "class DomainError(Exception): pass\n"
            "class IntegrationError(DomainError): pass\n"
            "class ValidationError(DomainError): pass\n"
        )
        with open(os.path.join(temp_dir, "exceptions.py"), "w", encoding="utf-8") as f:
            f.write(exceptions_stub)
        os.makedirs(os.path.join(temp_dir, "src", "domain"), exist_ok=True)
        with open(os.path.join(temp_dir, "src", "domain", "exceptions.py"), "w", encoding="utf-8") as f:
            f.write(exceptions_stub)
        with open(os.path.join(temp_dir, "src", "domain", "__init__.py"), "w", encoding="utf-8") as f:
            f.write("")
        with open(os.path.join(temp_dir, "src", "__init__.py"), "w", encoding="utf-8") as f:
            f.write("")

        with open(handler_path, "w", encoding="utf-8") as f:
            f.write(code)

        # Alias as service.py and src/service.py to support service module imports
        with open(os.path.join(temp_dir, "service.py"), "w", encoding="utf-8") as f:
            f.write(code)
        with open(os.path.join(temp_dir, "src", "service.py"), "w", encoding="utf-8") as f:
            f.write(code)
            
        with open(test_path, "w", encoding="utf-8") as f:
            # Ensure the test imports the handler
            if "import handler" not in test_code and "from handler" not in test_code:
                f.write("import handler\n")
            f.write(test_code)
            
        try:
            env = os.environ.copy()
            env["PYTHONPATH"] = temp_dir
            
            import sys
            result = subprocess.run(
                [sys.executable, "-m", "pytest", test_path, "-v", "--tb=short"],
                capture_output=True,
                text=True,
                env=env,
                timeout=15,  # Prevent infinite loops in generated code
            )
            if result.returncode != 0:
                if "No module named pytest" in result.stderr or "No module named pytest" in result.stdout:
                    pass
                else:
                    out = result.stdout[:2000] if len(result.stdout) > 2000 else result.stdout
                    issues.append(f"Sandbox tests failed. The generated code MUST pass these tests.\nTest Output:\n{out}")
        except subprocess.TimeoutExpired:
            issues.append("Sandbox tests timed out (infinite loop or hanging mock). Fix the code.")
        except FileNotFoundError:
            # pytest is not installed, fail gracefully
            pass
        except Exception as e:
            issues.append(f"Test sandbox error: {e}")
            
    return issues
