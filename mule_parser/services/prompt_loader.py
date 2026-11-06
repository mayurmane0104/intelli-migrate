"""
prompt_loader.py — Builds LLM prompts for the per-file migration path.

The system prompt instructs the LLM to produce a **complete, deployable
AWS Lambda project file tree** — not a Markdown migration report.

Output format (strict):
    ===FILE: {relative/path/to/file.py}===
    <complete file content>
    ===END===

The canonical directory structure is driven by the detected project type:
  * batch_simple   → EventBridge → single Lambda → S3/DB/API
  * batch_complex  → EventBridge → Step Functions → SQS → 3 Lambdas
  * api            → API Gateway → Lambda
  * hybrid         → both API + Batch structures
"""
import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

PROMPTS_DIR = Path(__file__).parent.parent / "kb" / "04_prompt_library" / "system_prompts"
SAMPLES_DIR = Path(__file__).parent.parent / "kb" / "03_validation"

CODE_GENERATION_CONTRACT_FILENAME = "code_generation_contract.md"

RUNTIME_META = {
    "python": {
        "label": "Python 3.12",
        "language": "Python",
        "languageVersion": "3.12",
        "sdk": "boto3 1.x / botocore",
        "sdkImport": "import boto3",
        "fileExt": ".py",
        "namingConvention": "snake_case functions and filenames",
        "handlerSignature": "def lambda_handler(event: dict, context: LambdaContext) -> dict",
        "testFramework": "pytest + moto",
        "packageManager": "pip / requirements.txt",
    },
    "groovy": {
        "label": "Apache Groovy 2.4 / 3.0",
        "language": "Groovy",
        "languageVersion": "3.0",
        "sdk": "com.sap.gateway.ip.core.customdev.util",
        "sdkImport": "import com.sap.gateway.ip.core.customdev.util.Message",
        "fileExt": ".groovy",
        "namingConvention": "camelCase functions and scripts",
        "handlerSignature": "def Message processData(Message message)",
        "testFramework": "Spock / JUnit",
        "packageManager": "Maven / Gradle",
    },
    "cpi-xml": {
        "label": "SAP CPI BPMN 2.0 XML",
        "language": "XML",
        "languageVersion": "1.0",
        "sdk": "SAP Cloud Integration BPMN2",
        "sdkImport": 'xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL"',
        "fileExt": ".iflw",
        "namingConvention": "CamelCase",
        "handlerSignature": "<bpmn2:process id=...>",
        "testFramework": "CPI Simulation",
        "packageManager": "CPI Package Bundle",
    },
    "xslt": {
        "label": "XSLT 3.0",
        "language": "XSLT",
        "languageVersion": "3.0",
        "sdk": "W3C XSLT",
        "sdkImport": 'xmlns:xsl="http://www.w3.org/1999/XSL/Transform"',
        "fileExt": ".xsl",
        "namingConvention": "kebab-case",
        "handlerSignature": "<xsl:stylesheet>",
        "testFramework": "CPI Simulation",
        "packageManager": "CPI Package Bundle",
    },
}

_DEFAULT_RUNTIME = "python"
DEFAULT_RUNTIME_KEY = _DEFAULT_RUNTIME
_DEFAULT_MIGRATION_TYPE = "mule4-lambda"

MIGRATION_TYPE_META = {
    "mule3-lambda": {"sourceVersion": "MuleSoft Mule 3.x (ESB)", "targetService": "AWS Lambda + API Gateway", "pattern": "Function-per-flow"},
    "mule4-lambda": {"sourceVersion": "MuleSoft Mule 4.x (Runtime 4.x)", "targetService": "AWS Lambda + API Gateway", "pattern": "Function-per-flow, reactive streams"},
    "apiled-apigateway": {"sourceVersion": "MuleSoft API-Led Connectivity", "targetService": "AWS API Gateway + Lambda", "pattern": "REST proxy + handler"},
    "batch-stepfunction": {"sourceVersion": "MuleSoft Batch Module", "targetService": "AWS Step Functions + Lambda", "pattern": "State machine + map state"},
    "mule-to-cpi-iflow": {"sourceVersion": "MuleSoft Mule 4.x / 3.x", "targetService": "SAP Integration Suite (Cloud Integration / CPI iFlows & Groovy)", "pattern": "iFlow Process with Groovy script steps and Camel mediation"},
    "mule3-to-cpi": {"sourceVersion": "MuleSoft Mule 3.x", "targetService": "SAP Integration Suite (Cloud Integration)", "pattern": "iFlow Process with Groovy script steps"},
    "mule4-to-cpi": {"sourceVersion": "MuleSoft Mule 4.x", "targetService": "SAP Integration Suite (Cloud Integration)", "pattern": "iFlow Process with Groovy script steps"},
}

# ─── Canonical directory structure definitions per project type ───────────────
# These are injected into the system prompt so the LLM knows exactly what
# files to generate and where to place them.

BATCH_SIMPLE_FILE_TREE = """
{project_name}/
├── src/
│   ├── domain/
│   │   ├── ports.py                       ← Protocol interfaces (no I/O)
│   │   ├── models/
│   │   │   ├── batch_context.py           ← Dataclass for batch run context
│   │   │   ├── batch_result.py            ← Dataclass for batch result
│   │   │   └── processing_result.py       ← Dataclass for per-record result
│   │   ├── services/
│   │   │   ├── batch_service.py           ← Core batch orchestration (pure)
│   │   │   ├── record_processor.py        ← Business logic per record (pure)
│   │   │   ├── record_validator.py        ← Validation rules (pure)
│   │   │   ├── record_transformer.py      ← DataWeave→Python transforms (pure)
│   │   │   ├── audit_service.py           ← Audit logic (pure, no I/O)
│   │   │   └── reconciliation_service.py  ← Reconciliation logic (pure)
│   │   └── exceptions/
│   │       └── domain_exceptions.py       ← Custom exception hierarchy
│   ├── adapters/
│   │   ├── s3_adapter.py                  ← boto3 S3 read/write
│   │   ├── db_adapter.py                  ← psycopg2/pymysql/oracledb
│   │   ├── http_adapter.py                ← httpx outbound HTTP
│   │   ├── salesforce_adapter.py          ← simple_salesforce
│   │   ├── secrets_adapter.py             ← boto3 Secrets Manager
│   │   ├── notification_adapter.py        ← boto3 SNS/SES
│   │   └── retry_adapter.py               ← Exponential backoff retry
│   ├── handlers/
│   │   └── lambda_handler.py              ← EventBridge trigger; thin wiring
│   └── config/
│       ├── settings.py                    ← Environment variable config
│       └── logging_config.py              ← Structured JSON logging setup
├── infrastructure/
│   └── terraform/
│       ├── main.tf                        ← Provider + backend config
│       ├── variables.tf                   ← Input variable declarations
│       ├── outputs.tf                     ← Output value declarations
│       ├── lambda.tf                      ← Lambda function resource
│       ├── scheduler.tf                   ← EventBridge scheduler
│       ├── iam.tf                         ← IAM role + policies
│       ├── s3.tf                          ← S3 bucket resources
│       └── secrets.tf                     ← Secrets Manager resources
├── tests/
│   ├── unit/
│   │   ├── domain/
│   │   │   ├── test_batch_service.py
│   │   │   ├── test_record_processor.py
│   │   │   └── test_record_validator.py
│   │   └── adapters/
│   │       ├── test_s3_adapter.py
│   │       └── test_db_adapter.py
│   └── events/
│       └── eventbridge_event.json
├── migration-report/
│   ├── assessment.md
│   └── migration-summary.md
├── requirements.txt
├── .env.example
└── README.md
"""

BATCH_COMPLEX_FILE_TREE = """
{project_name}/
├── src/
│   ├── domain/
│   │   ├── ports.py
│   │   ├── models/
│   │   │   ├── batch_context.py
│   │   │   ├── batch_result.py
│   │   │   └── processing_result.py
│   │   ├── services/
│   │   │   ├── batch_service.py
│   │   │   ├── record_processor.py
│   │   │   ├── record_validator.py
│   │   │   ├── record_transformer.py
│   │   │   ├── chunk_service.py
│   │   │   └── audit_service.py
│   │   └── exceptions/
│   │       └── domain_exceptions.py
│   ├── adapters/
│   │   ├── s3_adapter.py
│   │   ├── db_adapter.py
│   │   ├── http_adapter.py
│   │   ├── salesforce_adapter.py
│   │   ├── secrets_adapter.py
│   │   ├── notification_adapter.py
│   │   └── retry_adapter.py
│   ├── handlers/
│   │   ├── batch_trigger_handler.py       ← Lambda 1: Trigger + Step Functions
│   │   ├── record_processor_handler.py    ← Lambda 2: SQS consumer
│   │   └── batch_completion_handler.py    ← Lambda 3: Aggregation + notification
│   └── config/
│       ├── settings.py
│       └── logging_config.py
├── infrastructure/
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── lambda.tf
│   │   ├── sqs.tf
│   │   ├── stepfunctions.tf
│   │   ├── scheduler.tf
│   │   ├── iam.tf
│   │   ├── s3.tf
│   │   └── secrets.tf
│   └── step-functions/
│       └── batch_state_machine.asl.json
├── tests/
│   ├── unit/
│   │   ├── domain/
│   │   │   ├── test_batch_service.py
│   │   │   ├── test_record_processor.py
│   │   │   └── test_record_validator.py
│   │   └── adapters/
│   │       ├── test_s3_adapter.py
│   │       └── test_db_adapter.py
│   └── events/
│       ├── eventbridge_event.json
│       ├── sqs_event.json
│       └── stepfunction_event.json
├── migration-report/
│   ├── assessment.md
│   └── migration-summary.md
├── requirements.txt
├── .env.example
└── README.md
"""

API_FILE_TREE = """
{project_name}/
├── src/
│   ├── domain/
│   │   ├── ports.py                       ← Protocol interfaces
│   │   ├── models/
│   │   │   ├── request_model.py
│   │   │   ├── response_model.py
│   │   │   └── error_model.py
│   │   ├── services/                      ← One service module per endpoint
│   │   ├── validators/                    ← One validator per endpoint
│   │   └── exceptions/
│   │       └── domain_exceptions.py
│   ├── adapters/
│   │   ├── http_adapter.py                ← httpx outbound
│   │   ├── db_adapter.py                  ← Database connector
│   │   ├── salesforce_adapter.py          ← simple_salesforce
│   │   ├── secrets_adapter.py             ← boto3 Secrets Manager
│   │   └── auth_adapter.py                ← JWT/API key validation
│   ├── handlers/
│   │   ├── api_handler.py                 ← API Gateway trigger; thin routing
│   │   └── response_builder.py            ← Shared HTTP response shaping
│   └── config/
│       ├── settings.py
│       └── logging_config.py
├── infrastructure/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       ├── api_gateway.tf
│       ├── lambda.tf
│       ├── iam.tf
│       ├── s3.tf
│       ├── secrets.tf
│       └── cloudwatch.tf
├── tests/
│   ├── unit/
│   │   ├── domain/
│   │   └── adapters/
│   └── events/
│       ├── api_gateway_get_event.json
│       ├── api_gateway_post_event.json
│       └── api_gateway_error_event.json
├── migration-report/
│   ├── assessment.md
│   └── migration-summary.md
├── requirements.txt
├── .env.example
└── README.md
"""

HYBRID_FILE_TREE = """
{project_name}/
├── src/
│   ├── domain/
│   │   ├── ports.py
│   │   ├── models/
│   │   │   ├── batch_context.py
│   │   │   ├── batch_result.py
│   │   │   ├── request_model.py
│   │   │   └── response_model.py
│   │   ├── services/
│   │   │   ├── batch_service.py
│   │   │   ├── record_processor.py
│   │   │   └── api_service.py
│   │   └── exceptions/
│   │       └── domain_exceptions.py
│   ├── adapters/
│   │   ├── s3_adapter.py
│   │   ├── db_adapter.py
│   │   ├── http_adapter.py
│   │   └── secrets_adapter.py
│   ├── handlers/
│   │   ├── api_handler.py                 ← API Gateway trigger
│   │   └── batch_handler.py               ← EventBridge trigger
│   └── config/
│       ├── settings.py
│       └── logging_config.py
├── infrastructure/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       ├── api_gateway.tf
│       ├── lambda.tf
│       ├── scheduler.tf
│       ├── iam.tf
│       ├── s3.tf
│       └── secrets.tf
├── tests/
│   ├── unit/
│   │   ├── domain/
│   │   └── adapters/
│   └── events/
│       ├── api_gateway_event.json
│       └── eventbridge_event.json
├── migration-report/
│   ├── assessment.md
│   └── migration-summary.md
├── requirements.txt
├── .env.example
└── README.md
"""


def _detect_project_type(config: Dict[str, Any]) -> str:
    """
    Detect whether this is a batch, api, or hybrid project from the analysis context.
    Returns: "batch_simple" | "batch_complex" | "api" | "hybrid"

    Classification priority:
    1. Explicit ``migrationType`` value on the config dict.
    2. Per-file flow triggers from ``analysisContext.flows_in_file``.
    3. Project-level archetype / migration_type from ``analysisContext.project_identity``
       (fallback for support files such as .dwl, pom.xml, .yaml that have no own flows).
    4. ``ValueError`` — caller must handle gracefully (see ``build_system_prompt``).
    """
    migration_type = str(config.get("migrationType") or config.get("migration_type") or "").strip()
    mt_lower = migration_type.lower()
    if mt_lower in {"api", "rest", "http", "mule-api-to-aws-lambda"}:
        return "api"
    if mt_lower in {"batch_simple", "batch-simple", "mule-batch-to-lambda-simple"}:
        return "batch_simple"
    if mt_lower in {"batch_complex", "batch-complex", "mule-batch-to-lambda"}:
        return "batch_complex"
    if mt_lower in {"batch_large", "batch-large", "mule-batch-to-fargate"}:
        return "batch_complex"
    if mt_lower in {"hybrid", "mule-hybrid"}:
        return "hybrid"
    if "batch" in mt_lower and "step" in mt_lower:
        return "batch_complex"
    if "batch" in mt_lower:
        return "batch_simple"

    analysis_context = config.get("analysisContext") or {}
    flows = analysis_context.get("flows_in_file") or []
    project_identity = analysis_context.get("project_identity") or {}
    archetype = str(project_identity.get("archetype") or "").lower()

    has_batch = False
    has_api = False

    for flow in flows:
        trigger = (flow.get("entry_point") or {}).get("trigger_type") or ""
        pattern = str(flow.get("integration_pattern") or "").lower()
        if trigger in ("scheduler", "batch", "jms", "amqp") or "batch" in pattern:
            has_batch = True
        if trigger in ("http", "https") or "api" in pattern:
            has_api = True

    if "batch" in archetype:
        has_batch = True
    if "api" in archetype or "rest" in archetype or "http" in archetype:
        has_api = True

    if has_batch and has_api:
        return "hybrid"
    if has_batch:
        return "batch_simple"
    if has_api:
        return "api"

    # ── Project-level fallback ─────────────────────────────────────────────────
    # Support files (.dwl, pom.xml, .yaml, log4j2.xml, Postman collections, …)
    # have no per-file flow triggers.  Use the project-level migration_type or
    # archetype from the IR's project_identity before giving up.
    proj_mt = str(
        project_identity.get("migration_type")
        or project_identity.get("migrationType")
        or ""
    ).strip().lower()
    if proj_mt in {"api", "rest", "http", "mule-api-to-aws-lambda"}:
        return "api"
    if "batch" in proj_mt and "step" in proj_mt:
        return "batch_complex"
    if "batch" in proj_mt:
        return "batch_simple"
    if "hybrid" in proj_mt:
        return "hybrid"

    # Fallback on raw archetype string when migration_type is absent
    if "api" in archetype or "sapi" in archetype or "papi" in archetype:
        return "api"
    if "batch" in archetype:
        return "batch_simple"

    raise ValueError(
        "Cannot classify project type: no HTTP listener, APIKit router, scheduler, "
        "batch, JMS, or AMQP triggers detected. Human review required."
    )


def _get_file_tree_for_type(project_type: str, project_name: str) -> str:
    """Return the canonical file tree template for the given project type."""
    trees = {
        "batch_simple": BATCH_SIMPLE_FILE_TREE,
        "batch_complex": BATCH_COMPLEX_FILE_TREE,
        "api": API_FILE_TREE,
        "hybrid": HYBRID_FILE_TREE,
    }
    tree = trees.get(project_type)
    if tree is None:
        raise ValueError(
            f"Unknown project_type {project_type!r} — no file-tree template. "
            "Evidence-based classification required before code generation."
        )
    return tree.replace("{project_name}", project_name)


def _resolve_runtime_meta(config: Dict[str, Any]) -> tuple[str, Dict[str, Any]]:
    """Normalize target runtime; only Python is active in RUNTIME_META today."""
    raw = config.get("targetRuntime") or config.get("target_runtime") or _DEFAULT_RUNTIME
    target_runtime = str(raw).strip().lower() or _DEFAULT_RUNTIME
    rt = RUNTIME_META.get(target_runtime)
    if rt is None:
        target_runtime = _DEFAULT_RUNTIME
        rt = RUNTIME_META[_DEFAULT_RUNTIME]
    return target_runtime, rt


def _resolve_migration_type_meta(config: Dict[str, Any]) -> tuple[str, Dict[str, Any]]:
    raw = config.get("migrationType") or config.get("migration_type") or _DEFAULT_MIGRATION_TYPE
    migration_type = str(raw).strip() or _DEFAULT_MIGRATION_TYPE
    mt = MIGRATION_TYPE_META.get(migration_type)
    if mt is None:
        migration_type = _DEFAULT_MIGRATION_TYPE
        mt = MIGRATION_TYPE_META[_DEFAULT_MIGRATION_TYPE]
    return migration_type, mt


def load_migration_instructions() -> str:
    """Loads all markdown files from the prompts directory and concatenates them."""
    instructions = []
    if not PROMPTS_DIR.exists():
        return ""

    for md_file in PROMPTS_DIR.glob("*.md"):
        if md_file.name == CODE_GENERATION_CONTRACT_FILENAME:
            continue
        with open(md_file, "r", encoding="utf-8") as f:
            instructions.append(f.read())

    return "\n\n---\n\n".join(instructions)


def load_knowledge_base_samples() -> str:
    """Loads all markdown and json files from the samples directory."""
    samples = []
    if not SAMPLES_DIR.exists():
        return ""

    for file_path in SAMPLES_DIR.iterdir():
        if not file_path.is_file():
            continue

        ext = file_path.suffix.lower()
        if ext in [".md", ".json"]:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                samples.append(f"### {file_path.name}")
                if ext == ".json":
                    samples.append(f"```json\n{content}\n```")
                else:
                    samples.append(content)
            except Exception:
                pass

    return "\n\n".join(samples)


def load_code_generation_contract() -> str:
    """
    Return the contents of ``prompts/code_generation_contract.md``.

    The contract is the code generator's operating contract — absolute rules
    that override everything else (handler/service split, credential handling,
    DataWeave→Python translation patterns, scatter-gather pattern, mandatory
    quality requirements, …). It is injected as a dedicated fourth section
    into the system prompt by ``build_system_prompt`` so the LLM treats it
    as non-negotiable rather than as part of the variable knowledge base.

    Returns an empty string (with no exception) if the file is missing so
    callers degrade gracefully — useful in tests and partial installs.
    """
    path = PROMPTS_DIR / CODE_GENERATION_CONTRACT_FILENAME
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8").strip()
    except OSError:
        return ""


def _is_sap_target(config: Dict[str, Any]) -> bool:
    tp = str(config.get("targetPlatform") or config.get("target_platform") or "").lower().strip()
    if tp in ("sap-integration-suite", "sap", "cpi"):
        return True
    tr = str(config.get("targetRuntime") or config.get("target_runtime") or "").lower().strip()
    if tr in ("groovy", "cpi-xml", "xslt"):
        return True
    mt = str(config.get("migrationType") or config.get("migration_type") or "").lower().strip()
    if any(k in mt for k in ("cpi", "sap", "iflow")):
        return True
    return False


def _build_sap_system_prompt(config: Dict[str, Any]) -> str:
    target_runtime, rt = _resolve_runtime_meta(config)
    migration_type, mt = _resolve_migration_type_meta(config)
    file_name = config.get("fileName", "Unknown")

    prompt = f"""\
You are an expert Enterprise Integration Engineer specialising in migrating MuleSoft ESB applications to SAP Integration Suite (SAP Cloud Integration / CPI).

## YOUR MISSION
Translate the provided MuleSoft source file to production-ready SAP Cloud Integration (CPI) artifacts.
Do NOT generate AWS Lambda Python, Boto3, or Terraform.

## Migration Context
| Field              | Value |
|--------------------|-------|
| Source Platform    | {mt['sourceVersion']} |
| Target Platform    | SAP Integration Suite (Cloud Integration / CPI) |
| Target Runtime     | {rt['label']} |
| Language           | {rt['language']} {rt['languageVersion']} |
| Source File        | {file_name} |

## OUTPUT FORMAT — STRICT
Output every generated file using this exact delimiter:

===FILE: {{relative/path/from/project/root}}===
{{complete file content — no truncation, no placeholders}}
===END===

## ARTIFACT RULES:
1. DataWeave (`.dwl`) scripts:
   Translate to Apache Groovy script at:
   ===FILE: src/main/resources/script/{{script_name}}.groovy===
   Using the standard SAP CPI Groovy contract:
   package src.main.resources.script

   import com.sap.gateway.ip.core.customdev.util.Message
   import groovy.json.JsonSlurper
   import groovy.json.JsonOutput
   import java.util.UUID
   import java.text.SimpleDateFormat

   def Message processData(Message message) {{
       def headers = message.getHeaders()
       def properties = message.getProperties()
       def rawBody = message.getBody(String)
       def payload = null
       if (rawBody != null && rawBody.trim().length() > 0) {{
           try {{
               payload = new JsonSlurper().parseText(rawBody)
           }} catch (Exception e) {{
               payload = rawBody
           }}
       }}

       // Translated business logic without placeholders or stubs

       if (result != null) {{
           if (result instanceof Map || result instanceof List) {{
               message.setBody(JsonOutput.toJson(result))
               message.setHeader("Content-Type", "application/json")
           }} else {{
               message.setBody(result.toString())
           }}
       }}
       return message
   }}
   ===END===

2. Mule XML Flow files (`.xml`):
   Translate each Mule flow to an SAP CPI BPMN2 iFlow XML at:
   ===FILE: src/main/resources/scenarioflows/integrationflow/{{flow_name}}.iflw===
   Target standard SAP BPMN2 model with bpmn2:process, bpmn2:serviceTask, bpmn2:sequenceFlow, and ifl:property.
   Declare all namespaces on bpmn2:definitions (bpmn2, ifl, bpmndi, dc, di, xsi). Do not use undeclared prefixes.
   And any embedded DataWeave transformations to Groovy scripts under `src/main/resources/script/`.

3. Configuration / Properties (`.yaml`, `.properties`):
   Translate to SAP CPI externalized parameters:
   ===FILE: src/main/resources/parameters/parameters.prop===
   key=value
   ===END===

4. ZERO placeholders, TODO comments, empty stubs, or NotImplementedError.
5. NO AWS Lambda code, NO boto3, NO python syntax.
"""
    instructions = config.get("instructions")
    if instructions:
        prompt += f"\n\n### ADDITIONAL INSTRUCTIONS:\n{instructions}"
    return prompt


def _build_support_file_system_prompt(config: Dict[str, Any]) -> str:
    """
    Compact system prompt for support files that have no classifiable project type
    (e.g. DataWeave scripts, pom.xml, YAML config, log4j2.xml, Postman JSON).

    Instructs the LLM to translate the file to its target equivalent.
    """
    if _is_sap_target(config):
        return _build_sap_system_prompt(config)

    target_runtime, rt = _resolve_runtime_meta(config)
    migration_type, mt = _resolve_migration_type_meta(config)
    file_name = config.get("fileName", "Unknown")

    prompt = f"""\
You are an expert AWS migration engineer specialising in MuleSoft-to-AWS migrations.

## YOUR MISSION
Translate the provided MuleSoft support file to its AWS/Python equivalent.
This file is a **support artefact** (configuration, DataWeave script, schema, build
descriptor, or test resource) — it does not define a Mule flow, so no Lambda handler
or Terraform scaffolding is required unless the file content implies it.

## Migration Context
| Field           | Value |
|-----------------|-------|
| Source Platform | {mt['sourceVersion']} |
| Target Platform | {mt['targetService']} |
| Target Runtime  | {rt['label']} |
| Language        | {rt['language']} {rt['languageVersion']} |
| Source File     | {file_name} |

## OUTPUT FORMAT
If the file produces one or more output files, use:

===FILE: {{relative/path}}===
{{complete file content}}
===END===

If the file is not needed in the AWS project (e.g. a Postman environment file or a
Mule-specific log4j2.xml), output a brief explanation of why it is omitted instead.

## RULES
1. DataWeave (`.dwl`) → idiomatic Python function (no placeholders, complete logic).
2. YAML config → `config.py` or `.env.example` with AWS equivalents.
3. `pom.xml` → `requirements.txt` + brief migration note.
4. Log4j2 XML → Python `logging.config` dict or omit with explanation.
5. Postman collections/environments → omit with a note.
6. RAML/OAS specs → keep as-is under `src/api/` if relevant, or omit.
7. ZERO placeholders, TODO comments, or empty functions.
"""

    contract = load_code_generation_contract()
    if contract:
        prompt += (
            "\n\n---\n\n"
            "# CODE GENERATION CONTRACT (non-negotiable — highest precedence)\n\n"
            "If any other instruction conflicts with this contract, **this contract wins**.\n\n"
            f"{contract}"
        )

    instructions = config.get("instructions")
    if instructions:
        prompt += f"\n\n### ADDITIONAL INSTRUCTIONS:\n{instructions}"

    return prompt


def build_system_prompt(config: Dict[str, Any]) -> str:
    """
    Build the system prompt for per-file migration.

    The prompt instructs the LLM to produce a COMPLETE, DEPLOYABLE project as a set of files using
    the ===FILE: path=== / ===END=== format.
    """
    if _is_sap_target(config):
        return _build_sap_system_prompt(config)

    target_runtime, rt = _resolve_runtime_meta(config)
    migration_type, mt = _resolve_migration_type_meta(config)
    file_name = config.get("fileName", "Unknown")
    project_name = _normalize_project_name(file_name)
    try:
        project_type = _detect_project_type(config)
    except ValueError:
        # Support file with no classifiable trigger (DWL, YAML, JSON, pom.xml, …).
        # Fall back to a compact prompt so the batch does not fail on every support file.
        return _build_support_file_system_prompt(config)
    file_tree = _get_file_tree_for_type(project_type, project_name)

    base_prompt = f"""\
You are an expert AWS migration engineer and Python architect specializing in migrating MuleSoft Enterprise Service Bus applications to production AWS serverless architectures.

## YOUR MISSION
Generate a **complete, deployable AWS Lambda project** from the MuleSoft source code provided.

## Migration Context
| Field              | Value |
|--------------------|-------|
| Source Platform    | {mt['sourceVersion']} |
| Target Platform    | {mt['targetService']} |
| Pattern            | {mt['pattern']} |
| Target Runtime     | {rt['label']} |
| Language           | {rt['language']} {rt['languageVersion']} |
| AWS SDK            | {rt['sdk']} |
| Naming Convention  | {rt['namingConvention']} |
| Test Framework     | {rt['testFramework']} |
| Infrastructure     | Terraform (no SAM, no CDK) |
| Project Type       | {project_type.replace('_', ' ').upper()} |

## OUTPUT FORMAT — STRICT (any deviation = failure)

For EVERY file in the required file tree below, output it using this exact format:

===FILE: {{relative/path/from/project/root}}===
{{complete file content — no truncation, no placeholders}}
===END===

Generate ALL files. If a file is not relevant to the source application, generate it as a working stub with proper imports, docstring, and no-op functions — NEVER leave it empty.

## REQUIRED FILE TREE FOR PROJECT TYPE: {project_type.replace('_', ' ').upper()}
{file_tree}

## ABSOLUTE RULES — VIOLATION = REJECTION

### Code Quality
1. ZERO tolerance for TODO comments, placeholder stubs, `pass` bodies, or `NotImplementedError`
2. EVERY function must have a complete, working implementation with real business logic
3. ALL type hints required on every function signature
4. ALL functions and classes must have docstrings
5. ALL DataWeave transformations must be converted to idiomatic Python (list comprehensions, dict operations)
6. ALL error handling must be explicit (try/except with specific exception types)

### Architecture
7. Lambda handler function MUST be named `lambda_handler(event: dict, context: LambdaContext) -> dict`
8. Use `aws_lambda_powertools` for all structured logging (Logger, Tracer)
9. NO hardcoded credentials, passwords, or API keys — use AWS Secrets Manager or `os.environ`
10. ALL environment variable names MUST be UPPER_SNAKE_CASE
11. ALL connector clients MUST be lazily initialized (not at import time — cold-start safety)
12. Flow-refs become internal Python function calls — NEVER Lambda-to-Lambda calls unless the source is a delegation pattern
13. Scatter-gather / parallel routes MUST use `concurrent.futures.ThreadPoolExecutor` or `asyncio.gather`

### Infrastructure (Terraform)
14. ALL Terraform files must be syntactically valid HCL
15. EVERY Lambda must have: DLQ, X-Ray tracing enabled, CloudWatch log group with 30-day retention
16. NO wildcard `"*"` Resource on write IAM actions
17. ALL secrets referenced via Secrets Manager ARN environment variables

### DataWeave → Python Translation Rules
18. DataWeave `map` → Python list comprehension `[transform(x) for x in items]`
19. DataWeave `filter` → Python `[x for x in items if condition(x)]`
20. DataWeave `distinctBy` → Python deduplication with a `seen` set
21. DataWeave `orderBy` → Python `sorted(items, key=lambda x: x.get("field"), reverse=bool)`
22. DataWeave `reduce` → Python `functools.reduce` or manual accumulator loop
23. DataWeave `++` (concat) → Python list concatenation `list1 + list2`
24. DataWeave `default` → Python `.get("field", default_value)`
25. DataWeave `output application/csv` → Python `csv.DictWriter`
26. DataWeave `output application/json` → Python `json.dumps`

## NAMING CONVENTION
- Files and folders: `snake_case`
- Python classes: `PascalCase`
- Python functions and variables: `snake_case`
- Environment variables: `UPPER_SNAKE_CASE`
- AWS resources: `kebab-case` suffixed with `-${{var.environment}}`
- NO "mule", "esb", "anypoint" in any generated file, folder, variable, or class name

## REQUIREMENTS.TXT GENERATION
Include ALL libraries actually used. Pin major versions. Must include:
- `boto3>=1.34.0`
- `aws-lambda-powertools>=2.30.0`
- `botocore>=1.34.0`
Add others as needed (e.g. `simple-salesforce`, `pymysql`, `psycopg2-binary`, `requests`, `httpx`).

## MIGRATION REPORT FILES
Generate these as real markdown documents (not placeholders):
- `migration-report/assessment.md` — risk assessment, component mapping table, blockers
- `migration-report/migration-summary.md` — what was migrated, architecture decisions, env vars needed

## .ENV.EXAMPLE
List ALL environment variables required by the generated code with descriptive comments.

## README.MD
Include deployment instructions, prerequisites, environment variable table, and testing steps.

## Risks and Recommendations
(Performance, cold starts, SDK differences, security considerations)
"""

    # ── Code Generation Contract (highest precedence) ──────────────────────────
    contract = load_code_generation_contract()
    if contract:
        base_prompt += (
            "\n\n---\n\n"
            "# CODE GENERATION CONTRACT (non-negotiable — highest precedence)\n\n"
            "If any other instruction conflicts with this contract, **this contract wins**.\n\n"
            f"{contract}"
        )

    # ── Architecture guidelines from KB ────────────────────────────────────────
    arch_instructions = load_migration_instructions()
    if arch_instructions:
        base_prompt += (
            "\n\n---\n\n"
            "# ARCHITECTURE GUIDELINES & PATTERNS\n\n"
            f"{arch_instructions}"
        )

    # ── KB samples ─────────────────────────────────────────────────────────────
    samples = load_knowledge_base_samples()
    if samples:
        base_prompt += (
            "\n\n---\n\n"
            "# KNOWLEDGE BASE SAMPLES & RULES\n\n"
            f"{samples}"
        )

    instructions = config.get("instructions")
    if instructions:
        base_prompt += f"\n\n### ADDITIONAL INSTRUCTIONS:\n{instructions}"

    return base_prompt


def build_user_prompt(source_content: str, config: Dict[str, Any]) -> str:
    """
    Build the user prompt containing the source file to be migrated.
    """
    target_runtime, rt = _resolve_runtime_meta(config)
    migration_type, mt = _resolve_migration_type_meta(config)
    file_name = config.get("fileName", "Unknown")
    file_path = config.get("filePath", "Unknown")
    project_name = _normalize_project_name(file_name)
    try:
        project_type = _detect_project_type(config)
    except ValueError:
        # Support file — use a generic label so the user prompt is still informative.
        project_type = "support_file"

    is_sap = _is_sap_target(config)
    infra_line = "**Target Platform:** SAP Integration Suite (Cloud Integration)" if is_sap else "**Infrastructure:** Terraform"

    prompt = f"""\
## MIGRATION TASK

Migrate the {mt['sourceVersion']} source file below to a complete **{mt['targetService']}** project.

**Project Name:** `{project_name}`
**Project Type:** `{project_type.replace('_', ' ').upper()}`
**Source File:** `{file_name}`
**Source Path:** `{file_path}`
**Target Runtime:** {rt['label']}
**Target Language:** {rt['language']} {rt['languageVersion']}
{infra_line}
"""

    project_structure = config.get("projectStructure")
    if project_structure:
        prompt += f"\n## Project Context (File Tree)\n```text\n{project_structure}\n```"

    analysis_context = config.get("analysisContext")
    if analysis_context:
        prompt += "\n\n" + _render_analysis_context(analysis_context)

    ext = "xml" if file_path.endswith('.xml') else "dataweave" if file_path.endswith('.dwl') else "yaml" if file_path.endswith('.raml') else "text"
    prompt += f"\n\n## Source Code to Migrate\n```{ext}\n{source_content}\n```"

    if is_sap:
        prompt += f"""

## RESPONSE REQUIREMENTS (SAP Integration Suite / Cloud Integration)

1. For DataWeave scripts (`.dwl`): Generate complete Apache Groovy script in `===FILE: src/main/resources/script/<script_name>.groovy===`.
   Use `processData(Message message)` standard pattern operating on `com.sap.gateway.ip.core.customdev.util.Message`.
2. For Mule flow XML files (`.xml`): Generate complete SAP CPI BPMN2 iFlow XML in `===FILE: src/main/resources/scenarioflows/integrationflow/<flow_name>.iflw===`.
   Ensure proper standard SAP BPMN2 model with bpmn2:definitions and fully declared namespaces.
3. For configurations (`.yaml`, `.properties`): Generate parameters in `===FILE: src/main/resources/parameters.prop===`.
4. Extract ALL business logic and field mappings completely — do NOT leave any operations as TODOs or empty stubs.
5. STRICT: Never output AWS Lambda Python, Boto3, or Terraform.

Begin generating files now:
"""
    else:
        prompt += f"""

## RESPONSE REQUIREMENTS

1. Generate ALL files listed in the required file tree for project type `{project_type}`.
2. Use the exact `===FILE: path===` / `===END===` format for EVERY file.
3. Start with the handler files in `src/handlers/`, then generate all supporting domain, adapter, and config files.
4. Extract ALL business logic from the source — do NOT leave any operations as TODOs.
5. Convert ALL DataWeave transformations to complete Python implementations.
6. CRITICAL: You MUST generate the `infrastructure/terraform/` and `tests/` directories and their files. Do not stop after generating the python code!
7. The output must be immediately deployable — `terraform init && terraform apply` should work.

Begin generating files now:
"""

    return prompt


def _normalize_project_name(file_name: str) -> str:
    """
    Derive a clean project name from a file name.
    Strips extensions, replaces separators with hyphens, lowercases.
    Removes legacy platform names from the output.
    """
    import re
    name = Path(file_name).stem if file_name else "aws-project"
    # Replace underscores, spaces with hyphens
    name = re.sub(r"[\s_]+", "-", name)
    # Remove non-alphanumeric except hyphens
    name = re.sub(r"[^a-zA-Z0-9-]", "", name)
    # Lowercase
    name = name.lower().strip("-")
    # Remove legacy platform names
    for term in ["mule", "esb", "anypoint", "mulesoft"]:
        name = name.replace(term, "").strip("-")
    # Collapse repeated hyphens
    name = re.sub(r"-{2,}", "-", name).strip("-")
    return name or "aws-project"


def _render_analysis_context(ctx: Dict[str, Any]) -> str:
    """
    Render the per-file IR slice produced by ``services.ir_context`` into a
    deterministic prompt section. The LLM is told to treat this as the
    source of truth (the parser has already resolved flow-refs, properties,
    connectors and DataWeave semantics — the model must not re-derive).

    Compact JSON is preferred over prose so the model can lift values
    verbatim and we keep token usage predictable.
    """
    scope = ctx.get("scope") or {}
    flows = ctx.get("flows_in_file") or []
    integrations = ctx.get("integration_manifest") or []
    properties = ctx.get("property_mapping") or {}
    cross = ctx.get("cross_flow_relationships") or {}
    feasibility = ctx.get("feasibility") or {}
    project_identity = ctx.get("project_identity") or {}

    lines = [
        "## Analysis Context (from the parser layer — authoritative)",
        "",
        "**You MUST use this analysis output as the ground truth.** It was",
        "produced by the deterministic parser stage which has already:",
        "",
        "- resolved every `flow-ref` and `sub-flow`,",
        "- classified each property as secure / non-secure and mapped it to an",
        "  UPPER_SNAKE environment variable,",
        "- enumerated the connectors and HTTP/scheduler entry points,",
        "- structured every DataWeave script into field-level mappings.",
        "",
        "Do not re-derive any of this from the raw XML — read it directly",
        "from the structured context below and translate it into the target",
        "runtime. If you find a discrepancy between the raw XML and the",
        "analysis context, **prefer the analysis context** and surface the",
        "discrepancy in the migration-report/assessment.md.",
        "",
        f"- **Project:** {project_identity.get('name') or 'unknown'} (archetype: {project_identity.get('archetype') or 'unknown'})",
        f"- **Analysis Job:** `{ctx.get('analysis_job_id') or 'n/a'}` · IR v{ctx.get('ir_version') or '?'}",
        f"- **Scope:** file `{scope.get('file_name') or ''}` → flows {scope.get('matched_flows') or []} "
        f"(of {scope.get('total_flows_in_project', 0)} total project flows)",
    ]

    if feasibility.get("verdict"):
        lines.append(
            f"- **Feasibility:** {feasibility.get('verdict')} "
            f"(confidence {feasibility.get('confidence', 0)})"
        )
        if feasibility.get("blockers"):
            lines.append(f"  - Blockers: {feasibility['blockers']}")

    lines.append("")
    lines.append("### Flows in this file (resolved)")
    if not flows:
        lines.append("_No flows from this file were found in the analysis IR._")
    for flow in flows:
        lines.append("")
        lines.append(f"#### `{flow.get('name')}` ({flow.get('flow_type') or 'flow'})")
        if flow.get("purpose"):
            lines.append(f"- **Purpose:** {flow['purpose']}")
        if flow.get("business_logic_summary"):
            lines.append(f"- **Business logic:** {flow['business_logic_summary']}")
        if flow.get("integration_pattern"):
            lines.append(f"- **Pattern:** {flow['integration_pattern']}")

        entry = flow.get("entry_point") or {}
        if entry.get("trigger_type"):
            ep_bits = [f"type=`{entry['trigger_type']}`"]
            if entry.get("path"):
                ep_bits.append(f"path=`{entry['path']}`")
            if entry.get("trigger_config"):
                ep_bits.append(f"config={json.dumps(entry['trigger_config'])}")
            lines.append(f"- **Trigger:** {', '.join(ep_bits)}")

        if flow.get("flow_refs_resolved"):
            lines.append(f"- **Resolved flow-refs:** {flow['flow_refs_resolved']}")

        connectors = flow.get("connectors_used") or []
        if connectors:
            lines.append("- **Connectors used:**")
            for c in connectors:
                ops = ", ".join(c.get("operations") or []) or "—"
                lines.append(
                    f"  - `{c.get('connector_type')}` (config `{c.get('config_name') or 'inline'}`): {ops}"
                )

        props = flow.get("properties_used") or []
        if props:
            lines.append("- **Properties referenced (dotted → env-var):**")
            for p in props:
                marker = " 🔒" if p.get("is_secure") else ""
                lines.append(f"  - `${{{p['key']}}}` → `{p['env_var']}`{marker}")

        transforms = flow.get("transformations") or []
        if transforms:
            lines.append("- **DataWeave field mappings (structured — translate ALL of these):**")
            lines.append("```json")
            lines.append(json.dumps(transforms, indent=2)[:4000])
            lines.append("```")

        if flow.get("error_handling"):
            lines.append(f"- **Error handling:** {json.dumps(flow['error_handling'])[:1000]}")

        risk = flow.get("risk_flags") or []
        if risk:
            lines.append(f"- **Risk flags:** {json.dumps(risk)[:1000]}")

        contract = flow.get("behavior_contract") or {}
        if contract:
            lines.append("- **Behaviour contract:** " + json.dumps(contract)[:1500])

    if integrations:
        lines.append("")
        lines.append("### Integration Manifest (connector clients to wire up)")
        lines.append("```json")
        lines.append(json.dumps(integrations, indent=2)[:4000])
        lines.append("```")

    if properties:
        lines.append("")
        lines.append("### Property → Environment Variable Mapping")
        lines.append("```json")
        lines.append(json.dumps(properties, indent=2)[:4000])
        lines.append("```")

    if cross.get("inbound") or cross.get("outbound"):
        lines.append("")
        lines.append("### Cross-flow Relationships (edges of this slice)")
        if cross.get("inbound"):
            lines.append(f"- **Inbound callers:** {cross['inbound']}")
        if cross.get("outbound"):
            lines.append(f"- **Outbound calls:** {cross['outbound']}")

    return "\n".join(lines)
