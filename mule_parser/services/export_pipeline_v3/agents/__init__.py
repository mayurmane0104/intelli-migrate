"""
services/export_pipeline_v3/agents/__init__.py

The six named reasoning agents that implement the Enterprise AI-First pipeline.

Stage mapping:
    Stage 1  ArchitectAgent    — system design, module structure, dependency graph
    Stage 2  SeniorDevAgent    — business logic review, implementation quality
    Stage 3  SecurityAgent     — IAM, secrets, compliance review
    Stage 4  DevOpsAgent       — deployment, CI/CD, infrastructure review
    Stage 5  QAAgent           — test coverage, edge cases, fixture generation
    Stage 6  PrincipalAgent    — overall architecture, scalability, performance

Each agent uses the GroundedLLMClient with a role-specific system prompt.
Every agent has a deterministic fallback that runs when the LLM is disabled
or returns an insufficient_information response.
"""
from __future__ import annotations

from .agent_base import AgentBase, AgentError, ArchitecturePlanningError
from .architect_agent import ArchitectAgent
from .devops_agent import DevOpsAgent
from .principal_agent import PrincipalAgent
from .qa_agent import QAAgent
from .security_agent import SecurityAgent
from .senior_dev_agent import SeniorDevAgent

__all__ = [
    "AgentBase",
    "AgentError",
    "ArchitectAgent",
    "ArchitecturePlanningError",
    "DevOpsAgent",
    "PrincipalAgent",
    "QAAgent",
    "SecurityAgent",
    "SeniorDevAgent",
]
