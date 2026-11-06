"""
mule_parser/platforms/sap_generator.py  –  SAP Integration Suite Platform Plugin.

Plugs into the unified PlatformGenerator interface, orchestrating:
  - BPMN2 iFlow XML generation (iflow_generator.py)
  - DataWeave to Apache Groovy translation (dw_to_groovy.py)
  - SAP CPI deployable package bundle assembly (cpi_package_generator.py)
"""
from __future__ import annotations

from typing import Any

from .base import (
    BasePlatformGenerator,
    ConnectorMappingRule,
    GeneratedFile,
    TargetPlatformType,
    register_platform,
)
from .sap.cpi_package_generator import CPIArtifact, CPIPackageGenerator
from .sap.dw_to_groovy import DataWeaveToGroovyTranslator
from .sap.iflow_generator import IFlowGenerator, validate_and_normalize_iflow_xml


@register_platform(TargetPlatformType.SAP_INTEGRATION_SUITE)
class SAPPlatformGenerator(BasePlatformGenerator):
    """
    SAP Integration Suite implementation targeting SAP Cloud Integration (CPI)
    iFlows, Groovy transformation scripts, and BTP bundle manifests.
    """

    def __init__(self) -> None:
        self.iflow_gen = IFlowGenerator()
        self.dw_translator = DataWeaveToGroovyTranslator()
        self.packager = CPIPackageGenerator()

    @property
    def platform_type(self) -> TargetPlatformType:
        return TargetPlatformType.SAP_INTEGRATION_SUITE

    @property
    def display_name(self) -> str:
        return "SAP Integration Suite (Cloud Integration / CPI iFlows & Groovy)"

    def get_connector_mappings(self) -> dict[str, ConnectorMappingRule]:
        return {
            "http": ConnectorMappingRule("http", "HTTPS / ProcessDirect Adapter", "channel_https", 0.98),
            "soap": ConnectorMappingRule("soap", "SOAP 1.x / XI 3.0 Adapter", "channel_soap", 0.98),
            "rfc": ConnectorMappingRule("rfc", "SAP RFC / BAPI Adapter", "channel_rfc", 0.95),
            "db": ConnectorMappingRule("db", "SAP JDBC Adapter", "channel_jdbc", 0.95),
            "jms": ConnectorMappingRule("jms", "JMS / SAP Event Mesh Adapter", "channel_jms", 0.95),
            "amqp": ConnectorMappingRule("amqp", "AMQP / Event Mesh Adapter", "channel_amqp", 0.90),
            "sftp": ConnectorMappingRule("sftp", "SFTP Receiver Adapter", "channel_sftp", 0.95),
            "file": ConnectorMappingRule("file", "SFTP / File Adapter", "channel_file", 0.90),
            "salesforce": ConnectorMappingRule("salesforce", "Salesforce OData Adapter", "channel_odata", 0.92),
            "sap": ConnectorMappingRule("sap", "SAP RFC / IDoc Native Adapter", "channel_idoc", 0.99),
            "email": ConnectorMappingRule("email", "Mail Receiver Adapter", "channel_mail", 0.95),
            "vm": ConnectorMappingRule("vm", "ProcessDirect In-Memory Adapter", "channel_processdirect", 0.98),
            "objectstore": ConnectorMappingRule("objectstore", "SAP CPI Data Store Operations", "datastore", 0.90),
        }

    def generate_flow_handler(self, flow_data: dict[str, Any], context: dict[str, Any]) -> list[GeneratedFile]:
        flow_name = flow_data.get("name", "MainFlow")
        safe_name = "".join(c if c.isalnum() else "_" for c in flow_name).strip("_")

        # 1. Generate BPMN2 iFlow XML
        iflow_xml = self.iflow_gen.generate_iflow(flow_data)
        iflow_file = GeneratedFile(
            path=f"src/main/resources/scenarioflows/integrationflow/{safe_name}.iflw",
            content=iflow_xml,
            role="source",
            generator="sap:iflow",
        )

        return [iflow_file]

    def generate_transformation(self, dw_script: str, transform_meta: dict[str, Any]) -> list[GeneratedFile]:
        name = transform_meta.get("name", "transform_script")
        safe_name = "".join(c if c.isalnum() else "_" for c in name).strip("_")

        # 2. Translate DataWeave to Apache Groovy script
        groovy_code = self.dw_translator.translate(dw_script, transform_name=name)
        groovy_file = GeneratedFile(
            path=f"src/main/resources/script/{safe_name}.groovy",
            content=groovy_code,
            role="source",
            generator="sap:groovy",
        )

        return [groovy_file]

    def generate_infrastructure(self, project_metadata: dict[str, Any]) -> list[GeneratedFile]:
        project_id = project_metadata.get("id", "mule_project_cpi")
        project_name = project_metadata.get("name", "MuleSoft CPI Migration")

        # 3. Generate SAP CPI Package manifests
        return self.packager.build_package_manifests(project_id, project_name)

    def package_content_package(
        self,
        files: list[GeneratedFile],
        package_id: str,
        package_name: str,
        version: str = "1.0.0",
    ) -> bytes:
        """Assembles an experimental SAP CPI Content Package archive (experimental, not import-guaranteed in UI)."""
        return self.packager.create_zip_archive(
            files,
            package_id=package_id,
            package_name=package_name,
            export_type="package",
            version=version,
        )

    def package_individual_flow(
        self,
        files: list[GeneratedFile],
        artifact_id: str,
        artifact_name: str,
        version: str = "1.0.0",
    ) -> bytes:
        """Assembles Integration Flow archive(s) for upload into an existing package (primary guaranteed delivery path)."""
        return self.packager.create_zip_archive(
            files,
            package_id=artifact_id,
            package_name=artifact_name,
            export_type="iflow",
            version=version,
        )

    def package_bundle(self, files: list[GeneratedFile], export_type: str = "iflow") -> bytes:
        """Assembles the SAP CPI deployable zip. Defaults to 'iflow' (guaranteed individual flow bundle)."""
        return self.packager.create_zip_archive(files, export_type=export_type)
