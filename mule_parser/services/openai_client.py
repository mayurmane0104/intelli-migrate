"""
services/openai_client.py — Scratch & Independent OpenAI LLM Client.

Provides a dedicated OpenAICodegenClient that handles:
  1. Completion API requests (UnifiedFlowCodeGenerator & CorrectionAgent)
  2. Critique API requests (GroundedLLMClient & ReviewPass)

Completely independent of AWS Bedrock.
"""
from __future__ import annotations

import logging
import os
from typing import Any

logger = logging.getLogger(__name__)


class OpenAICodegenClient:
    """
    Independent OpenAI client wrapper for code generation, review, and self-correction.
    Uses the official `openai` SDK or direct httpx requests.
    """

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        max_tokens: int | None = None,
        temperature: float | None = None,
        timeout: int | None = None,
    ) -> None:
        from mule_parser.config.settings import (
            OPENAI_API_KEY,
            OPENAI_MODEL,
            OPENAI_MAX_TOKENS,
            OPENAI_TEMPERATURE,
            OPENAI_TIMEOUT,
        )

        self.api_key = api_key or OPENAI_API_KEY or os.getenv("OPENAI_API_KEY", "")
        self.model = model or OPENAI_MODEL or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self._max_tokens = max_tokens or OPENAI_MAX_TOKENS or 8192
        self._temperature = temperature if temperature is not None else OPENAI_TEMPERATURE
        self._timeout = timeout or OPENAI_TIMEOUT or 60

        self._client = None
        if self.api_key and self.api_key.strip() and self.api_key != "your_openai_api_key_here":
            try:
                from openai import OpenAI
                self._client = OpenAI(api_key=self.api_key.strip(), timeout=self._timeout)
            except Exception as exc:
                logger.error("Failed to initialize OpenAI SDK client: %s", exc)

    @property
    def enabled(self) -> bool:
        return self._client is not None

    def complete(self, system: str, user: str, max_tokens: int | None = None) -> str:
        """
        Synchronous completion call for UnifiedFlowCodeGenerator and CorrectionAgent.
        """
        if not self._client:
            raise RuntimeError("OpenAI client is not configured. Provide OPENAI_API_KEY in .env.")

        tokens = max_tokens or self._max_tokens
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]

        logger.info("OpenAICodegenClient calling model %s (max_tokens=%d)...", self.model, tokens)
        try:
            kwargs: dict[str, Any] = {
                "model": self.model,
                "messages": messages,
            }
            # Reasoning / newer models (gpt-4o, gpt-4o-mini, o1, o3) use max_completion_tokens
            if any(m in self.model.lower() for m in ("gpt-4o", "o1", "o3")):
                kwargs["max_completion_tokens"] = tokens
            else:
                kwargs["max_tokens"] = tokens
                kwargs["temperature"] = self._temperature

            response = self._client.chat.completions.create(**kwargs)
            content = response.choices[0].message.content or ""
            return content.strip()
        except Exception as exc:
            logger.error("OpenAI completion request failed: %s", exc)
            raise

    def critique(
        self,
        role: str,
        system: str,
        user: str,
        max_tokens: int = 2048,
        use_complex_model: bool = False,
    ) -> str:
        """
        Synchronous critique call for GroundedLLMClient and ValidationPipeline Layer 6.
        """
        return self.complete(system=system, user=user, max_tokens=max_tokens)


def build_openai_codegen_client() -> OpenAICodegenClient | None:
    """
    Factory function to build an OpenAICodegenClient if configured.
    """
    from mule_parser.config.settings import openai_configured
    if not openai_configured():
        return None
    try:
        client = OpenAICodegenClient()
        return client if client.enabled else None
    except Exception as exc:
        logger.warning("Could not build OpenAICodegenClient: %s", exc)
        return None
