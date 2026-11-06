"""Tests for project-agnostic DataWeave script analysis and codegen."""
from __future__ import annotations

from mule_parser.parsers.dw_script_analyzer import analyze_dataweave_script
from mule_parser.parsers.dw_semantic_codegen import can_generate, generate_from_script


GENERIC_MERGE_SCRIPT = """%dw 2.0
output application/csv
import mergeWith from dw::core::Objects
var crmRows = payload["0"].payload map (row) -> {
    "CustomerId": row.crm_id,
    "Name": row.display_name,
    "SourceA": row.system_a_id
}
var erpRows = payload["1"].payload map (row) -> {
    "CustomerId": row.erp_customer_id,
    "Name": row.legal_name,
    "SourceB": row.system_b_id
}
var merged = (
    crmRows map ((item) -> item mergeWith ((erpRows filter ($.CustomerId == item.CustomerId))[0]
        default {SourceB: ""}
    ))
) distinctBy $.CustomerId
++ (
    erpRows map ((item) -> item mergeWith ((crmRows filter ($.CustomerId == item.CustomerId))[0]
        default {SourceA: ""}
    ))
) distinctBy $.CustomerId
---
merged map (row) -> {
    "CustomerId": row.CustomerId,
    "Name": row.Name,
    "SourceA": row.SourceA,
    "SourceB": row.SourceB
}
"""


def test_analyzer_extracts_generic_routes_and_merge_key():
    analysis = analyze_dataweave_script(GENERIC_MERGE_SCRIPT)
    assert len(analysis.scatter_routes) == 2
    assert analysis.scatter_routes[0].field_map.get("CustomerId") == "crm_id"
    assert analysis.scatter_routes[1].field_map.get("CustomerId") == "erp_customer_id"
    assert analysis.bidirectional_merge is not None
    assert analysis.bidirectional_merge.merge_key == "CustomerId"
    assert "SourceA" in analysis.bidirectional_merge.defaults_when_partner_missing.get("1", {})


def test_codegen_emits_no_sfdc_db_names():
    code = generate_from_script(
        GENERIC_MERGE_SCRIPT,
        function_name="merge_customers",
        output_format="application/csv",
    )
    assert code is not None
    assert "sfdc" not in code.lower()
    assert "db_users" not in code.lower()
    assert "left_rows" in code
    assert "right_rows" in code
    assert "CustomerId" in code
    assert can_generate(GENERIC_MERGE_SCRIPT)


FILTER_SCRIPT = """%dw 2.0
output application/json
---
{
  PaymentOrders:
    if (attributes.queryParams.paymentId?)
      vars.paymentOrders filter ($.PaymentId ~= attributes.queryParams.paymentId)
    else
      vars.paymentOrders
}"""

CONCAT_SCRIPT = """%dw 2.0
output application/json
---
payload.a ++ ' middle ' ++ payload.b"""


def test_analyzer_parses_conditional_filter():
    analysis = analyze_dataweave_script(FILTER_SCRIPT)
    assert analysis.object_build is not None
    cf = analysis.object_build.conditional_filter
    assert cf is not None
    assert cf.output_key == "PaymentOrders"
    assert cf.source_ref == "vars.paymentOrders"
    assert len(cf.branches) == 2


def test_analyzer_parses_string_concat():
    analysis = analyze_dataweave_script(CONCAT_SCRIPT)
    assert analysis.string_concat is not None
    assert len(analysis.string_concat.parts) == 3
    assert can_generate(CONCAT_SCRIPT)
    code = generate_from_script(CONCAT_SCRIPT, function_name="concat_fields")
    assert code is not None
    assert "concat_str" in code
