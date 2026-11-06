from __future__ import annotations

from mule_parser.parsers.connector_capability_intel import build_connector_capability_intelligence


def test_connector_detection_and_normalization():
    raw = {
        "connectors": [{"connector_type": "http"}, {"connector_type": "database"}],
        "flow_execution_plans": [{
            "flow_name": "get:/users",
            "steps": [
                {"step_id": "s1", "type": "http:listener", "config_ref": "http_cfg"},
                {"step_id": "s2", "type": "db:select", "config_ref": "db_cfg"},
                {"step_id": "s3", "type": "ee:transform", "config_ref": ""},
            ],
        }],
    }
    out = build_connector_capability_intelligence(raw)
    names = {c["connector"] for c in out["catalog"]}
    assert "http:listener" in names
    assert "db:select" in names
    assert "ee:transform" in names
    assert out["usages"]


def test_migration_matrix_generation_and_linkage():
    raw = {
        "connectors": [{"connector_type": "http"}],
        "flow_execution_plans": [{
            "flow_name": "post:/orders",
            "steps": [{"step_id": "x1", "type": "http:request", "config_ref": "http_req_cfg"}],
        }],
    }
    out = build_connector_capability_intelligence(raw)
    assert out["migration_matrix"]
    usage = out["usages"][0]
    assert usage["flow"] == "post:/orders"
    assert usage["processor_id"] == "x1"
    assert usage["connector_capability_ref"]
    assert usage["endpoint"] == "POST /orders"


def test_unknown_connectors_and_fallback_profile():
    raw = {
        "connectors": [{"connector_type": "mycustom"}],
        "flow_execution_plans": [{
            "flow_name": "x",
            "steps": [{"step_id": "u1", "type": "foo:bar", "config_ref": ""}],
        }],
    }
    out = build_connector_capability_intelligence(raw)
    assert out["unknown_connectors"]
    unknown_profiles = [c for c in out["catalog"] if c.get("unknown")]
    assert unknown_profiles
    assert out["stats"]["unknown_connector_types"] >= 1


def test_version_and_namespace_presence():
    raw = {
        "connectors": [{"connector_type": "jms"}],
        "flow_execution_plans": [{"flow_name": "a", "steps": [{"step_id": "j1", "type": "jms:listener", "config_ref": "j"}]}],
    }
    out = build_connector_capability_intelligence(raw)
    cap = next(c for c in out["catalog"] if c["connector"] == "jms:listener")
    assert "3" in cap["supported_mule_versions"]
    assert "4" in cap["supported_mule_versions"]
    assert cap["namespace"] == "jms"
