import base64
import io
import json
import zipfile

import pytest

from mule_parser.platforms.sap.sap_compatibility_validator import validate_sap_artifacts
from mule_parser.platforms.sap.sap_reference_analyzer import SAPReferenceError, analyze_sap_reference, _infer_identifier_convention


BPMN = b'''<?xml version="1.0"?><bpmn2:definitions xmlns:bpmn2="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:ifl="http:///com.sap.ifl.model/Ifl.xsd"><bpmn2:process id="p1" name="Payroll"><bpmn2:startEvent id="s"/><bpmn2:scriptTask id="t"/><bpmn2:endEvent id="e"/><bpmn2:sequenceFlow id="f1" sourceRef="s" targetRef="t"/><bpmn2:sequenceFlow id="f2" sourceRef="t" targetRef="e"/></bpmn2:process></bpmn2:definitions>'''


def iflow_zip(symbolic="payroll_flow", bpmn=BPMN):
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("META-INF/MANIFEST.MF", f"Manifest-Version: 1.0\r\nBundle-SymbolicName: {symbolic}; singleton:=true\r\nBundle-Version: 1.2.0\r\n\r\n")
        z.writestr("src/main/resources/scenarioflows/integrationflow/payroll.iflw", bpmn)
        z.writestr("src/main/resources/script/process.groovy", b"return 'inert'")
        z.writestr("src/main/resources/parameters.prop", b"user.password=secret")
    return data.getvalue()


def package_zip(*artifacts):
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w", zipfile.ZIP_DEFLATED) as z:
        rows = []
        for i, artifact in enumerate(artifacts):
            name = f"{i:032x}_content"
            z.writestr(name, artifact)
            rows.append({"id": name[:32], "name": name[:-8], "resourceType": "IFlow"})
        z.writestr("resources.cnt", base64.b64encode(json.dumps({"resources": rows}).encode()))
        z.writestr("contentmetadata.md", "package")
        z.writestr("hash", "HashVersion=2.0.0")
    return data.getvalue()


def test_analyzes_individual_iflow_and_redacts_secrets():
    profile = analyze_sap_reference(iflow_zip(), "native.zip")
    assert profile["artifact_type"] == "iflow"
    assert profile["artifact_identifiers"] == ["payroll_flow"]
    assert profile["script_inventory"][0]["type"] == "script"
    assert "secret" not in str(profile)
    assert profile["bpmn_metadata"][0]["processes"][0]["name"] == "Payroll"


def test_analyzes_native_content_package_with_multiple_iflows():
    profile = analyze_sap_reference(package_zip(iflow_zip("flow_one"), iflow_zip("flow_two")), "package.zip")
    assert profile["artifact_type"] == "content_package"
    assert profile["artifact_identifiers"] == ["flow_one", "flow_two"]
    assert profile["package_metadata"]["integrity_file_present"] is True
    assert any("proprietary hash" in warning for warning in profile["validation_warnings"])


def test_reference_profile_is_used_as_a_comparison_context():
    profile = analyze_sap_reference(iflow_zip(), "reference.zip")
    profile["adapter_inventory"] = [{"type": "HTTP"}]
    report = validate_sap_artifacts([("payroll_flow", iflow_zip())], profile)
    assert report["reference_used"] is True
    assert "Reference adapter types available" in " ".join(report["artifacts"][0]["warnings"])


def test_identifier_style_is_inferred_only_from_repeated_artifact_ids():
    assert _infer_identifier_convention(["order_flow", "invoice_flow", "billing_flow"]) == [{
        "scope": "artifact_identifiers", "style": "lower_snake_case", "confidence": "inferred",
        "basis": "repeated Bundle-SymbolicName values", "basis_artifact_count": 3,
    }]
    assert _infer_identifier_convention(["order_flow", "invoice_flow"]) == []
    assert _infer_identifier_convention(["order_flow", "InvoiceFlow", "billing_flow"]) == []

    profile = analyze_sap_reference(package_zip(
        iflow_zip("order_flow"), iflow_zip("invoice_flow"), iflow_zip("billing_flow"),
    ))
    assert profile["naming_conventions"][0]["style"] == "lower_snake_case"


@pytest.mark.parametrize("data,name", [(b"not zip", "x.zip"), (iflow_zip(), "x.tar")])
def test_rejects_invalid_signature_and_extension(data, name):
    with pytest.raises(SAPReferenceError):
        analyze_sap_reference(data, name)


def test_rejects_zip_slip_entry():
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as z:
        z.writestr("../outside.txt", "bad")
    with pytest.raises(SAPReferenceError, match="unsafe path"):
        analyze_sap_reference(data.getvalue())


def test_rejects_symlink_and_unsupported_file_entries():
    symlink = io.BytesIO()
    with zipfile.ZipFile(symlink, "w") as z:
        info = zipfile.ZipInfo("link")
        info.create_system = 3
        info.external_attr = (0o120777 << 16)
        z.writestr(info, "../target")
    with pytest.raises(SAPReferenceError, match="Symbolic links"):
        analyze_sap_reference(symlink.getvalue())
    unsupported = io.BytesIO()
    with zipfile.ZipFile(unsupported, "w") as z:
        z.writestr("payload.exe", b"binary")
    with pytest.raises(SAPReferenceError, match="Unsupported file type"):
        analyze_sap_reference(unsupported.getvalue())


def test_unknown_archive_is_not_misclassified():
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as z:
        z.writestr("readme.md", "not an SAP export")
    with pytest.raises(SAPReferenceError, match="does not match"):
        analyze_sap_reference(data.getvalue())


def test_missing_manifest_identifier_and_invalid_bpmn_are_reported_without_claiming_validity():
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w") as z:
        z.writestr("META-INF/MANIFEST.MF", "Manifest-Version: 1.0\n")
        z.writestr("src/main/resources/scenarioflows/integrationflow/flow.iflw", b"<broken")
    result = analyze_sap_reference(data.getvalue())
    assert result["artifact_identifiers"] == []
    assert result["bpmn_metadata"][0]["valid_xml"] is False
    assert any("Bundle-SymbolicName" in warning for warning in result["validation_warnings"])


def test_compatibility_validator_checks_flow_endpoints_and_supports_standard_mode():
    valid = validate_sap_artifacts([("payroll_flow", iflow_zip())])
    assert valid["validation_status"] == "warning"
    assert valid["reference_used"] is False
    invalid_bpmn = BPMN.replace(b"targetRef=\"e\"", b"targetRef=\"missing\"")
    result = validate_sap_artifacts([("bad_flow", iflow_zip("bad_flow", invalid_bpmn))])
    assert result["validation_status"] == "error"
    assert result["summary"]["failed"] == 1

