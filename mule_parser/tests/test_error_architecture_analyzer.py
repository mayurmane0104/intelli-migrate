from __future__ import annotations

from pathlib import Path

from mule_parser.core.orchestrator import parse_mule_project


XML = """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:jms="http://www.mulesoft.org/schema/mule/jms"
      xmlns:sqs="http://www.mulesoft.org/schema/mule/sqs">
  <error-handler name="global-handler">
    <on-error-propagate type="HTTP:BAD_REQUEST" />
  </error-handler>

  <flow name="order-flow">
    <http:listener path="/orders" />
    <try doc:name="outer-try" transactionalAction="ALWAYS_BEGIN">
      <until-successful maxRetries="3" millisBetweenRetries="1000">
        <jms:publish destination="orders.queue" />
      </until-successful>
      <try doc:name="inner-try">
        <raise-error type="APP:ORDER_FAILURE" />
      </try>
      <error-handler>
        <on-error-continue type="ANY" />
      </error-handler>
    </try>
    <error-handler ref="global-handler" />
  </flow>

  <flow name="inventory-flow">
    <sqs:send-message queueUrl="inventory-dlq" />
    <error-handler>
      <on-error-propagate type="APP:INVENTORY_ERROR" />
    </error-handler>
  </flow>
</mule>
"""


def _mk_project(tmp_path: Path) -> Path:
    (tmp_path / "pom.xml").write_text(
        """<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion><artifactId>a</artifactId></project>""",
        encoding="utf-8",
    )
    mule_dir = tmp_path / "src" / "main" / "mule"
    mule_dir.mkdir(parents=True, exist_ok=True)
    (mule_dir / "app.xml").write_text(XML, encoding="utf-8")
    return tmp_path


def test_nested_try_retry_and_error_mapping(tmp_path: Path):
    result = parse_mule_project(str(_mk_project(tmp_path)))
    arch = result.error_architecture

    assert len(arch.try_scopes) >= 2
    assert any(scope.get("parent_try_scope") for scope in arch.try_scopes)
    assert any(p.get("type") == "until-successful" for p in arch.retry_policies)

    mapping = arch.error_propagation.get("flow_coverage", {})
    assert "order-flow" in mapping


def test_continue_vs_propagate_and_global_ref(tmp_path: Path):
    result = parse_mule_project(str(_mk_project(tmp_path)))
    arch = result.error_architecture
    handlers = arch.error_handlers

    assert any(h.get("handler_type") == "on-error-continue" for h in handlers)
    assert any(h.get("handler_type") == "on-error-propagate" for h in handlers)
    assert any(h.get("error_type") == "APP:ORDER_FAILURE" for h in handlers)

    flow_map = arch.model_dump().get("flow_error_mapping", {})
    assert "order-flow" in flow_map
    assert flow_map["order-flow"]["referenced_handlers"] == ["global-handler"]


def test_dlq_and_resilience_and_aws_risk(tmp_path: Path):
    result = parse_mule_project(str(_mk_project(tmp_path)))
    arch = result.error_architecture
    risk = result.aws_migration_risk

    assert arch.dlq_recommendation.target in {"SQS", "JMS", ""}
    assert 0 <= arch.resilience_score <= 100
    assert risk.risk in {"LOW", "MEDIUM", "HIGH"}
