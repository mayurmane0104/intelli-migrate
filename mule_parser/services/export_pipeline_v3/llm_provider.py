"""
LLM provider seam for the v3 export pipeline.

This module defines the contract every architecture/review/optimization
pass uses when it wants to consult an LLM. The default implementation is
deterministic and offline (``NullLLMProvider``); when AWS Bedrock is
configured the factory swaps in a Bedrock-backed provider.

Design rules
------------
* The pipeline must remain fully deterministic when no LLM is configured.
* No pass blocks on an LLM call. If the provider raises or returns empty,
  the deterministic path is used.
* Providers are stateless. Each ``critique`` / ``suggest`` call is
  self-contained — the caller threads state through the prompts.
* Every prompt names the role the LLM should play (Principal Architect,
  Code Reviewer, Optimisation Engineer) so the same model instance can
  serve all four passes.
"""
from __future__ import annotations

import logging
import os
from typing import Protocol


logger = logging.getLogger(__name__)


class LLMProvider(Protocol):
    """Protocol implemented by every LLM provider for the v3 pipeline."""

    enabled: bool

    def critique(
        self,
        *,
        role: str,
        system: str,
        user: str,
        max_tokens: int = 1024,
        use_complex_model: bool = False,
    ) -> str:
        """Send a single prompt and return the completion text.

        Implementations MUST:
        * Return an empty string when ``self.enabled`` is False.
        * Catch transport errors and return an empty string after logging.
        * Never raise — callers fall back to the deterministic path on
          empty responses, so silent failure is the safer default.
        """
        ...


# ─── Null provider (default) ──────────────────────────────────────────────────


class NullLLMProvider:
    """Deterministic provider. Always returns empty so callers use fallbacks.

    This is the default for the v3 pipeline. The pipeline produces fully
    valid code without ever consulting an LLM — the optional provider only
    adds rationale/critique annotations on top.
    """

    enabled: bool = False

    def critique(
        self,
        *,
        role: str,
        system: str,
        user: str,
        max_tokens: int = 1024,
        use_complex_model: bool = False,
    ) -> str:
        return ""


# ─── Bedrock provider ─────────────────────────────────────────────────────────


class BedrockLLMProvider:
    """Wraps the existing Bedrock-backed ``LLMClient`` for use by the v3 passes.

    Activation is gated on ``LLM_ENABLED`` + ``CODEGEN_LLM_ENABLED`` so
    operators have a single switch to disable LLM activity wholesale.
    Failures from the underlying Bedrock client are swallowed (logged at
    WARNING) so the v3 pipeline always completes.
    """

    enabled: bool

    def __init__(self) -> None:
        self._client = None
        self._complex_client = None
        self.enabled = False
        try:
            from mule_parser.config.settings import bedrock_configured, CODEGEN_LLM_ENABLED, BEDROCK_MODEL_ID, BEDROCK_COMPLEX_MODEL_ID  # type: ignore
            if not CODEGEN_LLM_ENABLED:
                return
            if not bedrock_configured():
                return
            from mule_parser.parsers.llm_inference_layer import build_bedrock_client, build_bedrock_client_for_model
            client = build_bedrock_client()
            if client is None:
                return
            self._client = client
            
            # Instantiate complex client if configured
            if BEDROCK_COMPLEX_MODEL_ID and BEDROCK_COMPLEX_MODEL_ID != BEDROCK_MODEL_ID:
                self._complex_client = build_bedrock_client_for_model(BEDROCK_COMPLEX_MODEL_ID)
            
            self.enabled = True
        except Exception as exc:  # noqa: BLE001 - never bring down the pipeline
            logger.debug("bedrock_provider_unavailable: %s", exc)
            self.enabled = False

    def critique(
        self,
        *,
        role: str,
        system: str,
        user: str,
        max_tokens: int = 1024,
        use_complex_model: bool = False,
    ) -> str:
        if not self.enabled or self._client is None:
            return ""
        
        active_client = self._complex_client if use_complex_model and self._complex_client else self._client
            
        try:
            system_with_role = f"You are acting as a {role}. {system}"
            return active_client.complete(system=system_with_role, user=user) or ""
        except Exception as exc:  # noqa: BLE001
            logger.warning("llm_critique_failed: %s", exc)
            return ""


# ─── Factory ──────────────────────────────────────────────────────────────────


def get_llm_provider() -> LLMProvider:
    """Return the active LLM provider.

    Selection logic:
        1. ``EXPORT_V3_LLM_PROVIDER=null`` forces the deterministic provider.
        2. Otherwise try Bedrock. If unavailable, fall back to Null.
    """
    forced = (os.environ.get("EXPORT_V3_LLM_PROVIDER") or "").strip().lower()
    if forced == "null":
        return NullLLMProvider()
    provider = BedrockLLMProvider()
    if provider.enabled:
        logger.info("export_v3 LLM provider: Bedrock")
        return provider
    logger.info("export_v3 LLM provider: Null (deterministic)")
    return NullLLMProvider()


__all__ = [
    "LLMProvider",
    "NullLLMProvider",
    "BedrockLLMProvider",
    "get_llm_provider",
]
