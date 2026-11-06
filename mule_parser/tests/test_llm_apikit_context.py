from __future__ import annotations

from mule_parser.parsers.llm_inference_layer import _apikit_contract_context, _decode_apikit_flow_name, _norm_path


def test_decode_apikit_flow_name_with_raml_suffix():
    method, path = _decode_apikit_flow_name(r"put:\CurrentAccount\IssuedDevice\Request:application\json:fsc-integrations-config")
    assert method == "PUT"
    assert path == "/CurrentAccount/IssuedDevice/Request"


def test_apikit_contract_context_match():
    api_contract = {
        "apis": [{
            "title": "FSC API",
            "endpoints": [{
                "path": "/CurrentAccount/IssuedDevice/Request",
                "display_name": "Issued Device Request",
                "methods": [{
                    "method": "put",
                    "description": "Update issued device request",
                }],
            }],
        }],
    }
    ctx = _apikit_contract_context(
        r"put:\CurrentAccount\IssuedDevice\Request:application\json:fsc-integrations-config",
        api_contract,
    )
    assert ctx["method"] == "PUT"
    assert ctx["path"] == "/CurrentAccount/IssuedDevice/Request"
    assert "issued device request" in ctx["description"].lower()


def test_norm_path():
    assert _norm_path("customers//x/") == "/customers/x"
