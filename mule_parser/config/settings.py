"""
mule_parser/config/settings.py  –  Single source of truth for all config.

Design principles:
- One system only: module-level constants loaded via dotenv at import.
  No Pydantic Settings class — that class was never actually used anywhere.
- AWS_DEFAULT_REGION (not AWS_REGION) — matches the .env key.
- bedrock_configured() reads the SAME vars as everything else — no split.
- No lru_cache — module-level vars are already singletons at import time.
- .env path resolves from <project_root>/.env (2 levels up from this file).
"""

from __future__ import annotations

import os
from pathlib import Path

# ─── Load .env  ──────────────────────────────────────────────────────────────
# Docker: mount host .env → /app/.env (see deploy/docker/docker-compose*.yml).
# Local dev without Docker: mule_parser/../.env or mule_parser/.env.
_APP_ROOT = Path(__file__).resolve().parents[2]
_ENV_CANDIDATES = (
    Path(os.getenv("APP_ENV_FILE", "/app/.env")),
    _APP_ROOT / ".env",
    Path(__file__).resolve().parents[1] / ".env",
)
_env_path = _APP_ROOT / ".env"

try:
    from dotenv import load_dotenv as _load_dotenv

    for _candidate in _ENV_CANDIDATES:
        if _candidate.is_file():
            _load_dotenv(_candidate, override=False)
            _env_path = _candidate
            break
except ImportError:
    pass

# ─── AWS credentials  ────────────────────────────────────────────────────────
AWS_ACCESS_KEY_ID:     str | None = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY: str | None = os.getenv("AWS_SECRET_ACCESS_KEY")

# Coerce empty strings to None so boto3 can fall back to IAM Roles
if AWS_ACCESS_KEY_ID is not None and AWS_ACCESS_KEY_ID.strip() == "":
    AWS_ACCESS_KEY_ID = None
if AWS_SECRET_ACCESS_KEY is not None and AWS_SECRET_ACCESS_KEY.strip() == "":
    AWS_SECRET_ACCESS_KEY = None

# BUG FIXED: was os.getenv("AWS_REGION", "us-east-2")
# .env uses AWS_DEFAULT_REGION; default corrected to us-east-2
AWS_REGION: str = (
    os.getenv("AWS_DEFAULT_REGION")
    or os.getenv("AWS_REGION")
    or "us-east-2"
)


# ─── Bedrock (AWS Bedrock settings - disabled when provider is openai) ───────
BEDROCK_MODEL_ID:    str   = os.getenv("BEDROCK_MODEL_ID",    "us.amazon.nova-pro-v1:0")
BEDROCK_COMPLEX_MODEL_ID: str = os.getenv("BEDROCK_COMPLEX_MODEL_ID", "us.amazon.nova-pro-v1:0")
BEDROCK_MAX_TOKENS:  int   = int(os.getenv("BEDROCK_MAX_TOKENS",  "8192"))
BEDROCK_TEMPERATURE: float = float(os.getenv("BEDROCK_TEMPERATURE", "0"))
BEDROCK_TIMEOUT:     int   = int(os.getenv("BEDROCK_TIMEOUT",     "30"))

# ─── OpenAI Configuration (Independent & Scratch) ───────────────────────────
ACTIVE_LLM_PROVIDER: str   = os.getenv("ACTIVE_LLM_PROVIDER", "openai").strip().lower()
OPENAI_API_KEY:      str | None = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL:        str   = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_MAX_TOKENS:   int   = int(os.getenv("OPENAI_MAX_TOKENS", "8192"))
OPENAI_TEMPERATURE:  float = float(os.getenv("OPENAI_TEMPERATURE", "0.0"))
OPENAI_TIMEOUT:      int   = int(os.getenv("OPENAI_TIMEOUT", "60"))

def openai_configured() -> bool:
    """True when LLM_ENABLED=true and OPENAI_API_KEY is present."""
    return bool(LLM_ENABLED and OPENAI_API_KEY and OPENAI_API_KEY.strip() and OPENAI_API_KEY != "your_openai_api_key_here")


# ─── LLM enrichment control  ─────────────────────────────────────────────────
LLM_ENABLED: bool = os.getenv("LLM_ENABLED", "true").strip().lower() != "false"

# BUG FIXED: was 0.65 — rule-based scoring hits 0.86 so ALL flows were skipped.
# 0.0 = LLM runs on every flow unconditionally.
# Override in .env if you want to restrict: LLM_CONFIDENCE_THRESHOLD=0.5
LLM_CONFIDENCE_THRESHOLD: float = float(os.getenv("LLM_CONFIDENCE_THRESHOLD", "0.7"))

# Performance controls for LLM enrichment.
# 0 = no fuzzy retry (fastest). 1 = current behavior (retry once).
LLM_MAX_FUZZY_RETRIES: int = int(os.getenv("LLM_MAX_FUZZY_RETRIES", "0"))
# Cap number of flows sent to LLM per analysis (0 = unlimited).
LLM_MAX_ENRICH_FLOWS: int = int(os.getenv("LLM_MAX_ENRICH_FLOWS", "40"))

# ─── Code Generation LLM settings  ──────────────────────────────────────────
# These govern the LLM-driven code generation stage (llm_code_generator.py)
# and are separate from the enrichment LLM settings above.

# Set to "false" to force the legacy template engine for all projects.
CODEGEN_LLM_ENABLED: bool = os.getenv("CODEGEN_LLM_ENABLED", "true").strip().lower() != "false"

# Token budget for code generation — larger than enrichment because we generate
# full function bodies, not just metadata fields.
CODEGEN_MAX_TOKENS: int = int(os.getenv("CODEGEN_MAX_TOKENS", "4096"))

# Cap on flows processed by the LLM code generator per migration run.
# 0 = unlimited; use a positive integer to control cost in large projects.
CODEGEN_MAX_FLOWS: int = int(os.getenv("CODEGEN_MAX_FLOWS", "0"))

# Emits a separate handler file per flow rather than merging them into a single api/lambda handler
LAMBDA_PER_FLOW: bool = os.getenv("LAMBDA_PER_FLOW", "false").strip().lower() == "true"

# ─── Knowledge Growth settings ────────────────────────────────────────────────
# When true, successful validated migrations are persisted to the KB as examples.
# Disabled by default — enable after reviewing generated output quality.
KNOWLEDGE_GROWTH_ENABLED: bool = os.getenv("KNOWLEDGE_GROWTH_ENABLED", "false").strip().lower() == "true"

# Directory where growth examples are written (relative to project root or absolute)
KNOWLEDGE_GROWTH_DIR: str = os.getenv(
    "KNOWLEDGE_GROWTH_DIR",
    str(Path(__file__).resolve().parent.parent / "knowledge_base" / "corpus" / "examples" / "approved"),
)

# ─── Enterprise AI Pipeline settings ─────────────────────────────────────────
# Minimum quality score required for export (0-100). Exports with score < this
# value are blocked regardless of individual findings.
MIN_QUALITY_SCORE: int = int(os.getenv("MIN_QUALITY_SCORE", "95"))

# Minimum feasibility confidence required before code generation proceeds.
# Projects self-reporting BLOCKED or confidence below this threshold are halted.
CODEGEN_FEASIBILITY_CONFIDENCE_THRESHOLD: float = float(
    os.getenv("CODEGEN_FEASIBILITY_CONFIDENCE_THRESHOLD", "0.83")
)

# Pipeline version: "v3" = deterministic-first (existing), "v4" = AI-first (new)
PIPELINE_VERSION: str = os.getenv("PIPELINE_VERSION", "v4")

# Maximum self-improvement loop iterations (v4 pipeline)
SELF_IMPROVEMENT_MAX_ITERATIONS: int = int(os.getenv("SELF_IMPROVEMENT_MAX_ITERATIONS", "5"))

# Model routing: Architect + Principal agents use the complex model;
# Senior Dev, Security, DevOps, QA use the standard model.
# Set AGENT_USE_COMPLEX_MODEL=false to use standard model for all agents.
AGENT_USE_COMPLEX_MODEL: bool = os.getenv("AGENT_USE_COMPLEX_MODEL", "true").strip().lower() != "false"

# Per-agent max tokens budget
AGENT_MAX_TOKENS: int = int(os.getenv("AGENT_MAX_TOKENS", "2048"))

# Hallucination guard: block export if generated artifacts reference
# APIs/connectors/fields not present in the IR metadata.
HALLUCINATION_GUARD_ENABLED: bool = os.getenv("HALLUCINATION_GUARD_ENABLED", "true").strip().lower() != "false"

# Export gate: "strict" runs agents + self-correction and blocks on quality findings.
# "codegen_only" generates code once via LLM and blocks only on Python syntax errors.
EXPORT_VALIDATION_MODE: str = os.getenv("EXPORT_VALIDATION_MODE", "strict").strip().lower()


def bedrock_configured() -> bool:
    """
    True when AWS Bedrock is the active provider AND minimum credentials exist.
    Returns False when ACTIVE_LLM_PROVIDER is 'openai'.
    """
    if ACTIVE_LLM_PROVIDER == "openai":
        return False
    return bool(LLM_ENABLED and (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY))



def dump_config() -> dict:
    """Return a safe config snapshot for debugging (no secret values)."""
    return {
        "aws_access_key_id_set":     bool(AWS_ACCESS_KEY_ID),
        "aws_secret_access_key_set": bool(AWS_SECRET_ACCESS_KEY),
        "aws_region":                AWS_REGION,
        "bedrock_model_id":          BEDROCK_MODEL_ID,
        "bedrock_complex_model_id":  BEDROCK_COMPLEX_MODEL_ID,
        "bedrock_max_tokens":        BEDROCK_MAX_TOKENS,
        "bedrock_temperature":       BEDROCK_TEMPERATURE,
        "bedrock_timeout":           BEDROCK_TIMEOUT,
        "llm_enabled":               LLM_ENABLED,
        "llm_confidence_threshold":  LLM_CONFIDENCE_THRESHOLD,
        "llm_max_fuzzy_retries":     LLM_MAX_FUZZY_RETRIES,
        "llm_max_enrich_flows":      LLM_MAX_ENRICH_FLOWS,
        "bedrock_configured":        bedrock_configured(),
        "env_file_path":             str(_env_path),
        "env_file_exists":           _env_path.exists(),
        "min_quality_score":          MIN_QUALITY_SCORE,
        "pipeline_version":           PIPELINE_VERSION,
        "self_improvement_max_iters": SELF_IMPROVEMENT_MAX_ITERATIONS,
        "agent_use_complex_model":    AGENT_USE_COMPLEX_MODEL,
        "hallucination_guard":        HALLUCINATION_GUARD_ENABLED,
        "export_validation_mode":     EXPORT_VALIDATION_MODE,
    }




