from typing import Any, Dict, Optional
import yaml
from pathlib import Path
from pydantic import BaseModel, Field

class CanonicalDecision(BaseModel):
    target: str = "ManualReview"
    canonical_service: str = ""
    migration_template: str = ""
    pattern: str = ""
    manual_review: bool = True
    normalized_source: str = ""
    confidence: float = 0.0
    complexity: str = "complex"
    complexity_score: int = 10
    match_type: str = "manual-review"
    tags: list[str] = Field(default_factory=list)
    raw_rule: dict[str, Any] = Field(default_factory=dict)

# Load YAML configs
KB_DIR = Path(__file__).parent
COMP_REGISTRY_PATH = KB_DIR / "01_ir_rules" / "component_registry.yaml"

def _load_registry() -> Dict[str, Any]:
    if not COMP_REGISTRY_PATH.exists():
        return {}
    with open(COMP_REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

_registry_cache = None

def get_registry_data():
    global _registry_cache
    if _registry_cache is None:
        _registry_cache = _load_registry()
    return _registry_cache

def resolve_component_target(detected: str, flow_type: Optional[str] = None) -> CanonicalDecision:
    reg = get_registry_data()
    mapping = reg.get("registry", {})
    metadata = reg.get("capability_metadata", {})
    
    capability_key = mapping.get(detected)
    if not capability_key:
        # Fallback to manual review
        return CanonicalDecision(
            target="ManualReview",
            normalized_source=detected,
            manual_review=True,
            confidence=0.0
        )
        
    meta = metadata.get(capability_key, {})
    aws_target = meta.get("aws_primary", "Lambda")
    score = meta.get("complexity_weight", 5)
    
    # Infer complexity string from score
    if score <= 2:
        complexity = "simple"
    elif score <= 4:
        complexity = "medium"
    else:
        complexity = "complex"
        
    return CanonicalDecision(
        target=aws_target,
        canonical_service=aws_target,
        migration_template=aws_target,
        pattern=capability_key,
        manual_review=False,
        normalized_source=capability_key,
        confidence=0.9,
        complexity=complexity,
        complexity_score=score,
        match_type="deterministic",
        raw_rule=meta
    )

def resolve_flow_target(flow_type: str, flow_name: str = "") -> CanonicalDecision:
    # Most flows just become Lambda functions
    return resolve_component_target("flow", flow_type)

def canonical_service_model() -> Dict[str, str]:
    # Returns a hardcoded default service mapping model 
    # to avoid needing the old OpenSearch models
    return {
        "compute": "AWS Lambda",
        "storage": "Amazon S3",
        "messaging": "Amazon SQS",
        "api": "Amazon API Gateway",
        "event": "Amazon EventBridge"
    }

def migration_template_for_target(target: str) -> Dict[str, Any]:
    # Simplified mock of the template dictionary
    target = target.lower()
    if "step_functions" in target:
        return {"template_id": "step_functions", "artifact_type": "statemachine", "file_extension": ".asl.json"}
    elif "api_gateway" in target:
        return {"template_id": "api_gateway", "artifact_type": "api", "file_extension": ".yaml"}
    return {"template_id": "lambda_handler", "artifact_type": "handler", "file_extension": ".py"}
