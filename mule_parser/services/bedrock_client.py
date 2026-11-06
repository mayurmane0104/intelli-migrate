"""
parsers/services/bedrock_client.py — Production Bedrock Claude client.

Implements the LLMClient Protocol defined in llm_inference_layer.py.
All config sourced from Settings — no hardcoded values.

Features:
- Exponential backoff with jitter (3 retries)
- Per-call timeout enforcement
- Structured logging with correlation IDs
- Raises BedrockError (never swallows exceptions silently)
"""

from __future__ import annotations

import json
import logging
import time
import uuid
from typing import Any

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError, EndpointResolutionError

from mule_parser.config.settings import Settings, get_settings

logger = logging.getLogger(__name__)


class BedrockError(RuntimeError):
    """Raised when Bedrock invocation fails after all retries."""


class BedrockClient:
    """
    Production Bedrock client.  Satisfies the LLMClient Protocol.

    Usage:
        client = BedrockClient.from_settings()
        text = client.complete(system="...", user="...")
    """

    _MAX_RETRIES = 3
    _BASE_BACKOFF = 1.0   # seconds
    _JITTER = 0.25

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._client = self._build_boto_client(settings)

    # ── Factory ───────────────────────────────────────────────────────────

    @classmethod
    def from_settings(cls, settings: Settings | None = None) -> "BedrockClient":
        return cls(settings or get_settings())

    # ── LLMClient Protocol ────────────────────────────────────────────────

    def complete(self, system: str, user: str) -> str:
        """
        Send a prompt pair and return raw completion text.
        Retries on throttling/transient errors with exponential backoff.
        Raises BedrockError on permanent failure.
        """
        correlation_id = str(uuid.uuid4())[:8]
        body = self._build_request_body(system, user)

        for attempt in range(1, self._MAX_RETRIES + 1):
            try:
                logger.debug(
                    "[%s] Bedrock invoke attempt %d/%d model=%s",
                    correlation_id, attempt, self._MAX_RETRIES,
                    self._settings.bedrock_model_id,
                )
                t0 = time.monotonic()
                response = self._client.invoke_model(
                    modelId=self._settings.bedrock_model_id,
                    body=json.dumps(body),
                    contentType="application/json",
                    accept="application/json",
                )
                elapsed = round(time.monotonic() - t0, 3)
                text = self._extract_text(response)
                logger.info(
                    "[%s] Bedrock OK attempt=%d elapsed=%.3fs tokens_in≈%d",
                    correlation_id, attempt, elapsed, len(user) // 4,
                )
                return text

            except ClientError as exc:
                code = exc.response["Error"]["Code"]
                if code in ("ThrottlingException", "ServiceUnavailableException"):
                    if attempt < self._MAX_RETRIES:
                        wait = self._backoff(attempt)
                        logger.warning(
                            "[%s] Bedrock throttled (%s), retry in %.1fs",
                            correlation_id, code, wait,
                        )
                        time.sleep(wait)
                        continue
                raise BedrockError(f"[{correlation_id}] Bedrock ClientError: {exc}") from exc

            except (EndpointResolutionError, OSError) as exc:
                raise BedrockError(f"[{correlation_id}] Bedrock network error: {exc}") from exc

        raise BedrockError(f"[{correlation_id}] Bedrock exhausted {self._MAX_RETRIES} retries.")

    # ── Private helpers ───────────────────────────────────────────────────

    def _build_request_body(self, system: str, user: str) -> dict[str, Any]:
        s = self._settings
        return {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": s.bedrock_max_tokens,
            "temperature": s.bedrock_temperature,
            "top_p": s.bedrock_top_p,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }

    @staticmethod
    def _extract_text(response: dict) -> str:
        body = json.loads(response["body"].read())
        content = body.get("content", [])
        if not content:
            raise BedrockError("Bedrock returned empty content list.")
        # Claude messages API returns list of content blocks
        texts = [block["text"] for block in content if block.get("type") == "text"]
        if not texts:
            raise BedrockError("No text block in Bedrock response.")
        return "\n".join(texts)

    @staticmethod
    def _build_boto_client(settings: Settings) -> Any:
        session_kwargs: dict[str, Any] = {
            "region_name": settings.aws_default_region,
        }
        if settings.aws_access_key_id:
            session_kwargs["aws_access_key_id"] = settings.aws_access_key_id
            session_kwargs["aws_secret_access_key"] = settings.aws_secret_access_key

        session = boto3.Session(**session_kwargs)
        return session.client(
            "bedrock-runtime",
            config=Config(
                connect_timeout=settings.bedrock_timeout,
                read_timeout=settings.bedrock_timeout,
                retries={"max_attempts": 1},  # retries managed above
            ),
        )

    def _backoff(self, attempt: int) -> float:
        import random
        return self._BASE_BACKOFF * (2 ** (attempt - 1)) + random.uniform(0, self._JITTER)