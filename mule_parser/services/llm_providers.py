import os
import json
import logging
import httpx
import boto3
from typing import AsyncGenerator, Dict, Any, Optional

from mule_parser.services.prompt_loader import build_system_prompt, build_user_prompt

logger = logging.getLogger(__name__)

_MASKED_KEY_MARKERS = ("••••", "****", "xxxx")


def _is_masked_or_placeholder_api_key(value: str | None) -> bool:
    """True when the UI or .env sent a redacted/placeholder key instead of a real secret."""
    if not value or not str(value).strip():
        return True
    text = str(value).strip()
    if any(marker in text for marker in _MASKED_KEY_MARKERS):
        return True
    if text.lower() in {"changeme", "your-key-here", "placeholder", "none", "null"}:
        return True
    return False


def _resolve_nova_credentials(provider_config: Dict[str, Any]) -> tuple[str, str, str | None]:
    """
    Resolve Bedrock credentials for Nova.

    Priority:
      1. Valid explicit keys from provider_config or settings
      2. IAM role / instance profile (empty keys → boto3 default chain)
    Never use masked UI placeholders as AWS access keys.
    """
    from mule_parser.config.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

    access_key_id = ""
    secret_access_key = ""
    session_token: str | None = None

    api_key = str(provider_config.get("apiKey") or "").strip()
    if api_key and not _is_masked_or_placeholder_api_key(api_key):
        try:
            parsed = json.loads(api_key)
            if isinstance(parsed, dict) and parsed.get("accessKeyId"):
                access_key_id = str(parsed["accessKeyId"]).strip()
                secret_access_key = str(parsed.get("secretAccessKey") or "").strip()
                session_token = parsed.get("sessionToken")
            else:
                access_key_id = api_key
        except (json.JSONDecodeError, TypeError):
            access_key_id = api_key

    if _is_masked_or_placeholder_api_key(access_key_id):
        access_key_id = ""
    if not secret_access_key and not _is_masked_or_placeholder_api_key(AWS_SECRET_ACCESS_KEY or ""):
        secret_access_key = (AWS_SECRET_ACCESS_KEY or "").strip()
    if not access_key_id and not _is_masked_or_placeholder_api_key(AWS_ACCESS_KEY_ID or ""):
        access_key_id = (AWS_ACCESS_KEY_ID or "").strip()

    if _is_masked_or_placeholder_api_key(access_key_id):
        access_key_id = ""
    if _is_masked_or_placeholder_api_key(secret_access_key):
        secret_access_key = ""

    return access_key_id, secret_access_key, session_token

class LLMProvider:
    name: str
    model: str

    async def stream_migration(
        self, source_content: str, config: Dict[str, Any]
    ) -> AsyncGenerator[str, None]:
        raise NotImplementedError

class NovaLiteLLMProvider(LLMProvider):
    def __init__(
        self,
        access_key_id: str,
        secret_access_key: str,
        model: str = "amazon.nova-lite-v1:0",
        region: str = "us-east-2",
        session_token: Optional[str] = None,
    ):
        self.name = "nova"
        self.model = model
        self.region = region
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.session_token = session_token

    def _get_client(self):
        # Coerce empty strings to None so boto3 uses IAM Role credentials
        ak = self.access_key_id if self.access_key_id and self.access_key_id.strip() else None
        sk = self.secret_access_key if self.secret_access_key and self.secret_access_key.strip() else None
        st = self.session_token if self.session_token and self.session_token.strip() else None
        return boto3.client(
            "bedrock-runtime",
            region_name=self.region,
            aws_access_key_id=ak,
            aws_secret_access_key=sk,
            aws_session_token=st,
        )


    async def stream_migration(
        self, source_content: str, config: Dict[str, Any]
    ) -> AsyncGenerator[str, None]:
        client = self._get_client()
        model_id = os.environ.get("BEDROCK_INFERENCE_PROFILE_ID", self.model)
        
        system_text = build_system_prompt(config)
        user_text = build_user_prompt(source_content, config)
        
        # Bedrock's converse_stream is synchronous generator natively in boto3,
        # but since we are in an async context, we yield from it (it will block the thread slightly,
        # in production we might use aioboto3 but this mimics the direct usage).
        try:
            response = client.converse_stream(
                modelId=model_id,
                system=[{"text": system_text}],
                messages=[{"role": "user", "content": [{"text": user_text}]}],
                inferenceConfig={"maxTokens": 8192},
            )
            for event in response.get("stream", []):
                if "contentBlockDelta" in event:
                    text = event["contentBlockDelta"]["delta"].get("text", "")
                    if text:
                        yield text
        except Exception as e:
            logger.error("Bedrock streaming error: %s", e)
            if "UnrecognizedClientException" in str(e) or "InvalidClientTokenId" in str(e):
                raise RuntimeError(
                    "AWS Bedrock authentication failed (invalid security token). "
                    "On EC2: attach an IAM role with bedrock:InvokeModel, OR set valid "
                    "AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY in the container .env. "
                    "Do not pass masked UI api keys (••••) as credentials."
                ) from e
            raise


class ClaudeLLMProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "claude-3-5-sonnet-20241022"):
        self.name = "claude"
        self.api_key = api_key
        self.model = model

    async def stream_migration(
        self, source_content: str, config: Dict[str, Any]
    ) -> AsyncGenerator[str, None]:
        system_text = build_system_prompt(config)
        user_text = build_user_prompt(source_content, config)
        
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
        }
        payload = {
            "model": self.model,
            "max_tokens": 8192,
            "stream": True,
            "system": system_text,
            "messages": [{"role": "user", "content": user_text}],
        }
        
        async with httpx.AsyncClient() as client:
            async with client.stream("POST", url, headers=headers, json=payload, timeout=60.0) as response:
                if response.status_code != 200:
                    text = await response.aread()
                    raise Exception(f"Claude API error ({response.status_code}): {text.decode('utf-8')}")
                
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        data = line[6:]
                        if data == "[DONE]":
                            break
                        try:
                            parsed = json.loads(data)
                            if parsed.get("type") == "content_block_delta":
                                text = parsed.get("delta", {}).get("text", "")
                                if text:
                                    yield text
                        except json.JSONDecodeError:
                            pass


class OpenAILLMProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gpt-4o"):
        self.name = "openai"
        self.api_key = api_key
        self.model = model

    async def stream_migration(
        self, source_content: str, config: Dict[str, Any]
    ) -> AsyncGenerator[str, None]:
        system_text = build_system_prompt(config)
        user_text = build_user_prompt(source_content, config)
        
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        payload = {
            "model": self.model,
            "max_completion_tokens": 8192,
            "stream": True,
            "messages": [
                {"role": "system", "content": system_text},
                {"role": "user", "content": user_text},
            ],
        }
        
        async with httpx.AsyncClient() as client:
            async with client.stream("POST", url, headers=headers, json=payload, timeout=60.0) as response:
                if response.status_code != 200:
                    text = await response.aread()
                    raise Exception(f"OpenAI API error ({response.status_code}): {text.decode('utf-8')}")
                
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        data = line[6:].strip()
                        if data == "[DONE]":
                            break
                        try:
                            parsed = json.loads(data)
                            choices = parsed.get("choices", [])
                            if choices:
                                content = choices[0].get("delta", {}).get("content", "")
                                if content:
                                    yield content
                        except json.JSONDecodeError:
                            pass


class GeminiLLMProvider(LLMProvider):
    def __init__(self, api_key: str, model: str = "gemini-2.5-flash"):
        self.name = "gemini"
        self.api_key = api_key
        self.model = model

    async def stream_migration(
        self, source_content: str, config: Dict[str, Any]
    ) -> AsyncGenerator[str, None]:
        system_text = build_system_prompt(config)
        user_text = build_user_prompt(source_content, config)
        full_text = f"{system_text}\n\n{user_text}"
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:streamGenerateContent?key={self.api_key}&alt=sse"
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            "contents": [{"parts": [{"text": full_text}]}],
            "generationConfig": {"maxOutputTokens": 8192},
        }
        
        async with httpx.AsyncClient() as client:
            async with client.stream("POST", url, headers=headers, json=payload, timeout=60.0) as response:
                if response.status_code != 200:
                    text = await response.aread()
                    raise Exception(f"Gemini API error ({response.status_code}): {text.decode('utf-8')}")
                
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        data = line[6:].strip()
                        try:
                            parsed = json.loads(data)
                            candidates = parsed.get("candidates", [])
                            if candidates:
                                parts = candidates[0].get("content", {}).get("parts", [])
                                if parts:
                                    text = parts[0].get("text", "")
                                    if text:
                                        yield text
                        except json.JSONDecodeError:
                            pass


def create_llm_provider(active_provider: str, provider_config: Dict[str, Any]) -> LLMProvider:
    from mule_parser.config.settings import bedrock_configured, openai_configured, OPENAI_API_KEY, OPENAI_MODEL

    config = dict(provider_config or {})
    if active_provider == "nova" and not bedrock_configured() and openai_configured():
        active_provider = "openai"
        config["enabled"] = True
        if not config.get("apiKey"):
            config["apiKey"] = OPENAI_API_KEY or ""
        if not config.get("model"):
            config["model"] = OPENAI_MODEL or "gpt-4o-mini"
    elif active_provider == "nova" and not config.get("enabled") and bedrock_configured():
        config["enabled"] = True
    elif active_provider == "openai" and openai_configured():
        config["enabled"] = True
        if not config.get("apiKey"):
            config["apiKey"] = OPENAI_API_KEY or ""
        if not config.get("model"):
            config["model"] = OPENAI_MODEL or "gpt-4o-mini"

    if not config or not config.get("enabled"):
        raise ValueError(f"Provider {active_provider} is not configured or enabled.")
    
    api_key = config.get("apiKey", "")
    # For nova, apiKey might be empty when using IAM roles. We allow this.
    if not api_key and active_provider != "nova":
        raise ValueError(f"Provider {active_provider} is missing apiKey.")

    model = config.get("model")
    
    if active_provider == "nova":
        access_key_id, secret_access_key, session_token = _resolve_nova_credentials(config)
        from mule_parser.config.settings import AWS_REGION

        return NovaLiteLLMProvider(
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            model=model or os.environ.get("BEDROCK_MODEL_ID", "us.amazon.nova-lite-v1:0"),
            region=AWS_REGION,
            session_token=session_token,
        )
    elif active_provider == "claude":
        return ClaudeLLMProvider(api_key, model=model)
    elif active_provider == "openai":
        return OpenAILLMProvider(api_key, model=model or "gpt-4o-mini")
    elif active_provider == "gemini":
        return GeminiLLMProvider(api_key, model=model)
    else:
        raise ValueError(f"Unsupported LLM provider: {active_provider}")
