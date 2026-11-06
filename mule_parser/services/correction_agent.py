"""
services/correction_agent.py — Dedicated post-generation correction agent.

Takes raw LLM-generated handler code and owns the full fix lifecycle:
  1. Runs Flake8 static analysis (undefined names, missing imports).
  2. Runs the pytest sandbox (logic/runtime errors).
  3. If either fails, sends the code + exact error to its own Correction LLM.
  4. Repeats until both pass or max_attempts is reached.
  5. Emits structured real-time progress events via the provided `emit` callable.

The `emit` callable signature matches job_store.emit_event() so events are
written to the ProjectEvent table and visible to any polling UI / log stream.
"""
from __future__ import annotations

import json
import logging
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from typing import Any, Callable

logger = logging.getLogger(__name__)

# ── Type alias for the progress emitter ──────────────────────────────────────
# Compatible with job_store.emit_event signature (keyword-only after event_type)
Emitter = Callable[..., None]


def _noop_emit(*args: Any, **kwargs: Any) -> None:
    """No-op fallback when no emitter is wired."""


# ── Correction Agent System Prompt ───────────────────────────────────────────

_CORRECTION_SYSTEM_PROMPT = """\
You are a Python Correction Agent. Your ONLY job is to receive broken or \
flawed AWS Lambda Python code together with the exact error that was found, \
and output a corrected, complete, production-ready Python source file.

ABSOLUTE RULES:
1. Output ONLY the corrected Python source code. No JSON. No markdown fences. \
   No explanations. No prose.
2. The corrected file MUST be 100% complete — never truncate it.
3. Fix EVERY error listed in the ERRORS section. Do not leave any unfixed.
4. Keep all existing correct logic intact — do not simplify or remove features.
5. All imports must be at the top of the file.
6. All functions must have full Python type hints.
7. All external AWS service calls must be wrapped in try/except.
8. Use aws_lambda_powertools Logger instead of bare print() for logging.
"""

_CORRECTION_USER_TEMPLATE = """\
=== ERRORS FOUND (fix ALL of these) ===
{errors}

=== BROKEN CODE ===
{code}

Output ONLY the corrected Python file now."""


# ── Data model ────────────────────────────────────────────────────────────────

@dataclass
class CorrectionResult:
    """Result returned by CorrectionAgent.correct()."""
    code: str
    test_code: str
    passed_static: bool = False
    passed_sandbox: bool = False
    attempts: int = 0
    issues_fixed: list[str] = field(default_factory=list)
    final_issues: list[str] = field(default_factory=list)


# ── Agent ─────────────────────────────────────────────────────────────────────

class CorrectionAgent:
    """
    Dedicated agent that iteratively fixes generated code until it passes
    Flake8 static analysis and the pytest sandbox, or exhausts max_attempts.
    """

    def __init__(self, client: Any, *, max_attempts: int = 3) -> None:
        self._client = client
        self._max_attempts = max_attempts

    @property
    def enabled(self) -> bool:
        return self._client is not None

    def correct(
        self,
        code: str,
        test_code: str,
        flow_name: str,
        *,
        emit: Emitter = _noop_emit,
        job_id: str = "",
        project_id: str = "",
        job_type: str = "migration",
    ) -> CorrectionResult:
        """
        Run the full correction loop.

        Returns a CorrectionResult with the best version of the code we have,
        whether or not it fully passed — caller decides what to do with it.
        """
        issues_fixed: list[str] = []
        current_code = code
        current_test = test_code

        for attempt in range(1, self._max_attempts + 1):
            # ── Static analysis ───────────────────────────────────────────
            emit(
                project_id,
                "correction:linting",
                job_id=job_id,
                job_type=job_type,
                status="running",
                current_stage=f"correction:linting (attempt {attempt}/{self._max_attempts})",
                payload={"flow": flow_name, "attempt": attempt},
            )
            lint_issues = _run_flake8(current_code)

            if lint_issues:
                emit(
                    project_id,
                    "correction:lint_failed",
                    job_id=job_id,
                    job_type=job_type,
                    status="retrying",
                    current_stage=f"correction:lint_failed (attempt {attempt}/{self._max_attempts})",
                    payload={"flow": flow_name, "attempt": attempt, "issues": lint_issues},
                )
                logger.warning(
                    "CorrectionAgent [%s] attempt %d/%d — Flake8 issues: %s",
                    flow_name, attempt, self._max_attempts, lint_issues,
                )
                fixed = self._llm_fix(current_code, lint_issues, flow_name)
                if fixed:
                    issues_fixed.extend(lint_issues)
                    current_code = fixed
                continue  # Re-run from the top after a fix

            # ── Sandbox tests ────────────────────────────────────────────
            emit(
                project_id,
                "correction:testing",
                job_id=job_id,
                job_type=job_type,
                status="running",
                current_stage=f"correction:testing (attempt {attempt}/{self._max_attempts})",
                payload={"flow": flow_name, "attempt": attempt},
            )
            sandbox_issues = _run_sandbox(current_code, current_test) if current_test else []

            if sandbox_issues:
                emit(
                    project_id,
                    "correction:test_failed",
                    job_id=job_id,
                    job_type=job_type,
                    status="retrying",
                    current_stage=f"correction:test_failed (attempt {attempt}/{self._max_attempts})",
                    payload={"flow": flow_name, "attempt": attempt, "issues": sandbox_issues},
                )
                logger.warning(
                    "CorrectionAgent [%s] attempt %d/%d — Sandbox failures: %s",
                    flow_name, attempt, self._max_attempts, sandbox_issues[:3],
                )
                fixed = self._llm_fix(current_code, sandbox_issues, flow_name)
                if fixed:
                    issues_fixed.extend(sandbox_issues)
                    current_code = fixed
                continue

            # ── Both passed ───────────────────────────────────────────────
            emit(
                project_id,
                "correction:approved",
                job_id=job_id,
                job_type=job_type,
                status="passed",
                current_stage="correction:approved",
                payload={
                    "flow": flow_name,
                    "attempts": attempt,
                    "issues_fixed": len(issues_fixed),
                },
            )
            logger.info(
                "CorrectionAgent [%s] approved after %d attempt(s). Fixed %d issue(s).",
                flow_name, attempt, len(issues_fixed),
            )
            return CorrectionResult(
                code=current_code,
                test_code=current_test,
                passed_static=True,
                passed_sandbox=True,
                attempts=attempt,
                issues_fixed=issues_fixed,
            )

        # Max attempts exhausted — return best effort
        remaining = _run_flake8(current_code)
        emit(
            project_id,
            "correction:exhausted",
            job_id=job_id,
            job_type=job_type,
            status="warning",
            current_stage="correction:exhausted",
            payload={"flow": flow_name, "remaining_issues": remaining},
        )
        logger.warning(
            "CorrectionAgent [%s] exhausted %d attempts. Remaining issues: %s",
            flow_name, self._max_attempts, remaining,
        )
        return CorrectionResult(
            code=current_code,
            test_code=current_test,
            passed_static=not bool(remaining),
            passed_sandbox=False,
            attempts=self._max_attempts,
            issues_fixed=issues_fixed,
            final_issues=remaining,
        )

    def _llm_fix(self, code: str, errors: list[str], flow_name: str) -> str:
        """Call the Correction LLM and return the corrected source, or '' on failure."""
        if not self.enabled:
            return ""
        error_block = "\n".join(f"- {e}" for e in errors)
        user_prompt = _CORRECTION_USER_TEMPLATE.format(errors=error_block, code=code)
        try:
            raw = self._client.complete(system=_CORRECTION_SYSTEM_PROMPT, user=user_prompt)
        except Exception as exc:
            logger.error("CorrectionAgent LLM call failed for '%s': %s", flow_name, exc)
            return ""
        # Strip any accidental markdown fences the model may emit
        cleaned = re.sub(r"^```(?:python)?\s*", "", raw.strip(), flags=re.MULTILINE)
        cleaned = re.sub(r"```\s*$", "", cleaned.strip())
        return cleaned if cleaned.strip() else ""


# ── Helpers ───────────────────────────────────────────────────────────────────

def _run_flake8(code: str) -> list[str]:
    """Run native AST parse for syntax errors, then Flake8 for logic errors."""
    issues: list[str] = []
    
    # 1. Native AST Parse (guarantees syntax errors are caught even without flake8)
    import ast
    try:
        ast.parse(code)
    except SyntaxError as e:
        # Feed the exact line and message to the LLM
        issues.append(f"Line {e.lineno}: SyntaxError - {e.msg}")
        return issues  # Return immediately, flake8 will just report the same syntax error

    # 2. Flake8
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(code)
        tmp = f.name
    try:
        result = subprocess.run(
            [sys.executable, "-m", "flake8", "--select=F,E9", tmp],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            # Check if flake8 is just not installed as a module
            if "No module named flake8" in result.stderr:
                logger.error("CRITICAL: flake8 is not installed. Run 'pip install flake8'. Skipping flake8 checks.")
            else:
                for line in result.stdout.splitlines():
                    parts = line.split(":", 3)
                    if len(parts) >= 4:
                        issues.append(f"Line {parts[1]}:{parts[3].strip()}")
                    else:
                        issues.append(line.strip())
    except FileNotFoundError:
        logger.error("CRITICAL: Python executable not found to run flake8.")
    except Exception as exc:
        logger.warning("Flake8 execution error: %s", exc)
    finally:
        try:
            os.unlink(tmp)
        except Exception:
            pass
    return issues


def _run_sandbox(code: str, test_code: str) -> list[str]:
    """Run pytest in a temp directory and return failure messages."""
    issues: list[str] = []
    with tempfile.TemporaryDirectory() as tmp_dir:
        handler_path = os.path.join(tmp_dir, "handler.py")
        test_path = os.path.join(tmp_dir, "test_handler.py")

        # Stub common dependencies for isolated sandbox execution
        services_dir = os.path.join(tmp_dir, "services")
        os.makedirs(services_dir, exist_ok=True)
        with open(os.path.join(services_dir, "__init__.py"), "w", encoding="utf-8") as f:
            f.write("")
        with open(os.path.join(services_dir, "http_client_service.py"), "w", encoding="utf-8") as f:
            f.write("class HttpClientService:\n    def execute(self, *a, **kw):\n        return {'status': 'ok'}\n")

        exceptions_stub = "class DomainError(Exception): pass\nclass IntegrationError(DomainError): pass\nclass ValidationError(DomainError): pass\n"
        with open(os.path.join(tmp_dir, "exceptions.py"), "w", encoding="utf-8") as f:
            f.write(exceptions_stub)
        os.makedirs(os.path.join(tmp_dir, "src", "domain"), exist_ok=True)
        with open(os.path.join(tmp_dir, "src", "domain", "exceptions.py"), "w", encoding="utf-8") as f:
            f.write(exceptions_stub)

        with open(handler_path, "w", encoding="utf-8") as f:
            f.write(code)
        with open(os.path.join(tmp_dir, "service.py"), "w", encoding="utf-8") as f:
            f.write(code)
        with open(os.path.join(tmp_dir, "src", "service.py"), "w", encoding="utf-8") as f:
            f.write(code)
        with open(test_path, "w", encoding="utf-8") as f:
            if "import handler" not in test_code and "from handler" not in test_code:
                f.write("import handler\n")
            f.write(test_code)
        try:
            env = os.environ.copy()
            env["PYTHONPATH"] = tmp_dir
            result = subprocess.run(
                [sys.executable, "-m", "pytest", test_path, "-v", "--tb=short"],
                capture_output=True, text=True, env=env, timeout=15,
            )
            if result.returncode != 0:
                if "No module named pytest" in result.stderr:
                    logger.error("CRITICAL: pytest is not installed. Run 'pip install pytest'. Skipping sandbox testing.")
                else:
                    out = result.stdout[:2000] if len(result.stdout) > 2000 else result.stdout
                    issues.append(
                        f"Sandbox tests FAILED — fix the code so all tests pass.\n{out}"
                    )
        except subprocess.TimeoutExpired:
            issues.append("Sandbox timed out — possible infinite loop. Fix the code.")
        except FileNotFoundError:
            logger.error("CRITICAL: Python executable not found to run pytest.")
        except Exception as exc:
            issues.append(f"Sandbox error: {exc}")
    return issues
