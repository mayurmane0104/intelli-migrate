from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Any

from mule_parser.config.settings import (
    AWS_ACCESS_KEY_ID,
    BEDROCK_MODEL_ID,
    LLM_ENABLED,
    bedrock_configured,
)
from mule_parser.services.accuracy_scorer import (
    ACCURACY_THRESHOLD,
    MAX_ACCURACY_RETRY_ATTEMPTS,
    format_deficiency_retry_prompt,
    score_migration_accuracy,
)
from mule_parser.services.llm_providers import create_llm_provider
from mule_parser.services.prompt_loader import build_system_prompt, build_user_prompt

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class FileMigrationResult:
    content: str
    system_prompt: str
    user_prompt: str
    provider: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    accuracy_score: int = 0
    accuracy_deficiencies: tuple[str, ...] = ()
    accuracy_attempts: int = 1
    needs_manual_review: bool = False


def _estimate_tokens(text: str) -> int:
    return max(1, len(text or "") // 4)


def _default_provider_config(provider_name: str) -> dict[str, Any]:
    """Server-side provider config — defaults to OpenAI when configured."""
    from mule_parser.config.settings import (
        ACTIVE_LLM_PROVIDER,
        OPENAI_API_KEY,
        OPENAI_MODEL,
        openai_configured,
        bedrock_configured,
        AWS_ACCESS_KEY_ID,
        BEDROCK_MODEL_ID,
    )
    from mule_parser.services.llm_providers import _is_masked_or_placeholder_api_key

    if provider_name == "openai" or (ACTIVE_LLM_PROVIDER == "openai" and openai_configured()):
        return {
            "enabled": True,
            "apiKey": OPENAI_API_KEY or "",
            "model": OPENAI_MODEL or "gpt-4o-mini",
        }
    access_key = AWS_ACCESS_KEY_ID if not _is_masked_or_placeholder_api_key(AWS_ACCESS_KEY_ID) else ""
    return {
        "enabled": bedrock_configured(),
        "apiKey": access_key or "",
        "model": BEDROCK_MODEL_ID,
    }


def _resolve_provider(
    active_provider: str | None,
    provider_config: dict[str, Any] | None,
) -> tuple[str, dict[str, Any]]:
    from mule_parser.config.settings import ACTIVE_LLM_PROVIDER, openai_configured, bedrock_configured

    default_prov = ACTIVE_LLM_PROVIDER if (ACTIVE_LLM_PROVIDER and openai_configured()) else "openai" if openai_configured() else "nova"
    provider = (active_provider or default_prov).strip().lower()

    # Fallback to OpenAI if Nova was requested but Bedrock credentials are unavailable
    if provider == "nova" and not bedrock_configured() and openai_configured():
        provider = "openai"

    config = dict(provider_config or _default_provider_config(provider))
    if provider == "openai":
        if not config.get("apiKey"):
            from mule_parser.config.settings import OPENAI_API_KEY
            config["apiKey"] = OPENAI_API_KEY or ""
        config["enabled"] = openai_configured()
    elif provider == "nova" and not config.get("enabled") and bedrock_configured():
        config["enabled"] = True

    if not config.get("enabled"):
        raise RuntimeError(
            f"LLM provider '{provider}' is not enabled. Configure API keys in Settings "
            "or set OPENAI_API_KEY in environment."
        )
    return provider, config


async def _collect_streamed_migration(
    provider: Any,
    source_content: str,
    config: dict[str, Any],
) -> str:
    chunks: list[str] = []
    async for token in provider.stream_migration(source_content, config):
        if token:
            chunks.append(token)
    content = "".join(chunks).strip()
    if not content:
        raise RuntimeError("LLM returned an empty migration response")
    return content


async def _run_accuracy_retry_loop(
    llm: Any,
    *,
    source_content: str,
    base_config: dict[str, Any],
    file_name: str,
    file_path: str,
    system_prompt: str,
    user_prompt: str,
) -> tuple[str, int, tuple[str, ...], int, bool]:
    """Generate migration output with bounded accuracy retries."""
    base_instructions = base_config.get("instructions") or ""
    retry_appendix = ""
    best_content = ""
    best_score = -1
    best_deficiencies: tuple[str, ...] = ()
    attempts = 0

    for attempt in range(1, MAX_ACCURACY_RETRY_ATTEMPTS + 1):
        attempts = attempt
        config = dict(base_config)
        config["instructions"] = base_instructions + retry_appendix

        try:
            content = await _collect_streamed_migration(llm, source_content, config)
        except Exception as exc:
            if attempt >= MAX_ACCURACY_RETRY_ATTEMPTS:
                raise
            logger.warning(
                "LLM attempt %d/%d failed for %s: %s",
                attempt,
                MAX_ACCURACY_RETRY_ATTEMPTS,
                file_path,
                exc,
            )
            continue

        # ── In-Flight Self-Healing during Migration ──────────────────────
        target_rt = (base_config.get("targetRuntime") or "python").lower()
        target_plat = (base_config.get("targetPlatform") or "aws").lower()
        is_sap = (
            target_plat in ("sap-integration-suite", "sap", "cpi")
            or target_rt in ("groovy", "cpi-xml", "xslt")
            or "cpi" in str(base_config.get("migrationType", "")).lower()
        )
        if not is_sap and ("python" in target_rt or file_name.endswith(".py")):
            from mule_parser.services.python_syntax import is_valid_python, auto_repair_python_syntax
            from mule_parser.services.migration_db import extract_primary_code

            code_to_check = extract_primary_code(content) or content
            if code_to_check.strip() and not is_valid_python(code_to_check):
                try:
                    repaired_code = auto_repair_python_syntax(code_to_check)
                    if is_valid_python(repaired_code) and repaired_code != code_to_check:
                        if code_to_check in content:
                            content = content.replace(code_to_check, repaired_code)
                        else:
                            content = repaired_code
                        logger.info(
                            "In-flight self-healing successfully repaired Python syntax for %s (attempt %d)",
                            file_path,
                            attempt,
                        )
                except Exception as repair_err:
                    logger.debug("In-flight self-healing attempted but encountered: %s", repair_err)
        elif is_sap and (file_name.endswith(".dwl") or target_rt == "groovy"):
            if "processData" not in content and "Message" not in content:
                from mule_parser.platforms.sap.dw_to_groovy import DataWeaveToGroovyTranslator
                from pathlib import Path
                content = DataWeaveToGroovyTranslator().translate(source_content, transform_name=Path(file_name).stem)
                logger.info("In-flight self-healing generated SAP CPI Groovy wrapper for %s", file_path)

        accuracy = score_migration_accuracy(
            source_content,
            content,
            file_name=file_name,
            file_path=file_path,
            target_runtime=target_rt,
            target_platform=target_plat,
        )
        if accuracy.score > best_score:
            best_score = accuracy.score
            best_content = content
            best_deficiencies = tuple(accuracy.deficiencies)

        if accuracy.passed:
            return content, accuracy.score, tuple(accuracy.deficiencies), attempts, False

        if attempt < MAX_ACCURACY_RETRY_ATTEMPTS:
            retry_appendix = format_deficiency_retry_prompt(accuracy.deficiencies)
            logger.info(
                "Accuracy retry %d/%d for %s score=%d deficiencies=%d",
                attempt,
                MAX_ACCURACY_RETRY_ATTEMPTS,
                file_path,
                accuracy.score,
                len(accuracy.deficiencies),
            )

    needs_review = best_score < ACCURACY_THRESHOLD
    if needs_review:
        logger.warning(
            "Migration for %s needs manual review after %d attempts (best score=%d)",
            file_path,
            attempts,
            best_score,
        )
    return best_content, max(best_score, 0), best_deficiencies, attempts, needs_review


def generate_file_migration(
    *,
    file_name: str,
    file_path: str,
    source_content: str,
    migration_type: str,
    target_runtime: str,
    target_platform: str | None = None,
    project_structure: str = "",
    project_id: str | None = None,
    active_provider: str | None = None,
    provider_config: dict[str, Any] | None = None,
    instructions: str = "",
    top_k: int = 8,  # noqa: ARG001 — retained for API compatibility
) -> FileMigrationResult:
    """
    Run per-file migration using the same enriched prompt path as
    ``/migration/stream-file``: IR slice + industry prompt library + streaming LLM.
    """
    resolved_platform = (
        (target_platform or "").strip().lower()
        or ("sap-integration-suite" if ("cpi" in migration_type.lower() or (target_runtime or "").lower() in ("groovy", "cpi-xml", "xslt")) else "aws")
    )
    is_sap = (
        resolved_platform in ("sap-integration-suite", "sap", "cpi")
        or (target_runtime or "").strip().lower() in ("groovy", "cpi-xml", "xslt")
        or "cpi" in migration_type.lower()
        or "sap" in migration_type.lower()
    )

    def _generate_sap_deterministic() -> str:
        from pathlib import Path
        clean_name = Path(file_name).stem
        if file_name.endswith(".dwl") or target_runtime == "groovy":
            from mule_parser.platforms.sap.dw_to_groovy import DataWeaveToGroovyTranslator
            return DataWeaveToGroovyTranslator().translate(source_content, transform_name=clean_name)
        elif file_name.endswith(".xml") and ("mule" in source_content.lower() or "<flow" in source_content.lower()):
            from lxml import etree
            from mule_parser.core.xml_engine import MuleXMLDocument
            from mule_parser.parsers.flow_parser import parse_flows
            from mule_parser.platforms.sap_generator import SAPPlatformGenerator
            try:
                raw = source_content.encode('utf-8')
                parser = etree.XMLParser(recover=True, remove_comments=True, remove_pis=False, huge_tree=True)
                tree = etree.fromstring(raw, parser=parser)
                doc = MuleXMLDocument(Path(file_name), tree.getroottree(), source_content)
                flows = parse_flows(doc)
                if flows:
                    sap = SAPPlatformGenerator()
                    flow_dict = {
                        'name': flows[0].name,
                        'source': {'type': flows[0].source.type if flows[0].source else 'http:listener'},
                        'processors': [{'type': p.type, 'name': p.name or p.type} for p in flows[0].processors]
                    }
                    gen_files = sap.generate_flow_handler(flow_dict, {})
                    return gen_files[0].content
            except Exception as e:
                logger.warning("Deterministic SAP iFlow generation fallback failed for %s: %s", file_path, e)
        return source_content

    if not LLM_ENABLED:
        if is_sap:
            content = _generate_sap_deterministic()
            accuracy = score_migration_accuracy(
                source_content,
                content,
                file_name=file_name,
                file_path=file_path,
                target_runtime=target_runtime,
                target_platform=resolved_platform,
            )
            return FileMigrationResult(
                content=content,
                system_prompt="SAP Native Deterministic Translator",
                user_prompt="Deterministic conversion",
                provider="sap-native",
                model="deterministic",
                input_tokens=_estimate_tokens(source_content),
                output_tokens=_estimate_tokens(content),
                accuracy_score=accuracy.score,
                accuracy_deficiencies=tuple(accuracy.deficiencies),
                accuracy_attempts=1,
                needs_manual_review=not accuracy.passed,
            )
        raise RuntimeError(
            "LLM migration is disabled (LLM_ENABLED=false). "
            "Set LLM_ENABLED=true and configure your provider in Settings."
        )

    provider_name, resolved_config = _resolve_provider(active_provider, provider_config)
    llm = create_llm_provider(provider_name, resolved_config)

    analysis_context: dict[str, Any] | None = None
    if project_id:
        try:
            from mule_parser.services.ir_context import build_generation_context

            analysis_context = build_generation_context(
                project_id=project_id,
                file_name=file_name,
                file_path=file_path,
            )
            if analysis_context:
                logger.info(
                    "migration IR context project=%s file=%s flows=%d connectors=%d",
                    project_id,
                    file_path,
                    len(analysis_context.get("flows_in_file") or []),
                    len(analysis_context.get("integration_manifest") or []),
                )
        except Exception:
            logger.exception(
                "IR enrichment failed for project=%s file=%s — falling back to raw source",
                project_id,
                file_path,
            )

    config: dict[str, Any] = {
        "migrationType": migration_type,
        "targetRuntime": (target_runtime or ("groovy" if is_sap else "python")).strip().lower(),
        "targetPlatform": resolved_platform,
        "fileName": file_name,
        "filePath": file_path,
        "projectStructure": project_structure,
        "instructions": instructions,
        "analysisContext": analysis_context,
    }

    system_prompt = build_system_prompt(config)
    user_prompt = build_user_prompt(source_content, config)

    try:
        (
            content,
            accuracy_score,
            accuracy_deficiencies,
            accuracy_attempts,
            needs_manual_review,
        ) = asyncio.run(
            _run_accuracy_retry_loop(
                llm,
                source_content=source_content,
                base_config=config,
                file_name=file_name,
                file_path=file_path,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
            )
        )
    except Exception as exc:
        if is_sap:
            logger.warning("LLM migration failed for SAP target %s; using deterministic generator: %s", file_path, exc)
            content = _generate_sap_deterministic()
            accuracy = score_migration_accuracy(
                source_content,
                content,
                file_name=file_name,
                file_path=file_path,
                target_runtime=target_runtime,
                target_platform=resolved_platform,
            )
            accuracy_score = accuracy.score
            accuracy_deficiencies = tuple(accuracy.deficiencies)
            accuracy_attempts = 1
            needs_manual_review = not accuracy.passed
        else:
            logger.exception("LLM migration failed for %s", file_path)
            raise RuntimeError(f"LLM migration failed for {file_path}: {exc}") from exc

    if needs_manual_review:
        logger.warning(
            "Migration for %s needs manual review "
            "(accuracy=%d%%, threshold=%d%%, attempts=%d). "
            "Deficiencies: %s - saving code anyway.",
            file_path,
            accuracy_score,
            ACCURACY_THRESHOLD,
            accuracy_attempts,
            "; ".join(accuracy_deficiencies[:5]),
        )

    input_tokens = _estimate_tokens(system_prompt) + _estimate_tokens(user_prompt)
    output_tokens = _estimate_tokens(content)

    return FileMigrationResult(
        content=content,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        provider=provider_name,
        model=getattr(llm, "model", resolved_config.get("model", "unknown")),
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        accuracy_score=accuracy_score,
        accuracy_deficiencies=accuracy_deficiencies,
        accuracy_attempts=accuracy_attempts,
        needs_manual_review=needs_manual_review,
    )
