"""
mule_parser/platforms/sap/cpi_package_generator.py  –  SAP Cloud Integration Package & Artifact Bundler.

Supports two distinct SAP Cloud Integration export workflows:
1. SAP CPI Content Package (package-level ZIP):
   Exported for UI import at "Design -> Integrations and APIs -> Import".
   Contains outer metadata descriptors and nested artifact archives:
     - {artifact_id}_content (nested ZIP archive for each Integration Flow, strictly isolating referenced scripts)
     - resources.cnt (Base64-encoded JSON manifest of ContentPackage and IFlow resources and relationships)
     - contentmetadata.md (Base64-encoded metadata properties: HashVersion, EncodingVersion, etc.)
     - hash (JSON array of SHA-256 hashes matching resource order)
     - ExportInformation.info (Key-value text metadata with Name and Date)

2. Individual Integration Flow ZIP (artifact-level ZIP):
   Exported for uploading into an existing package via "Add -> Integration Flow -> Upload" or OData API.
   Contains the single flow project structure:
     - src/main/resources/scenarioflows/integrationflow/<flow>.iflw
     - src/main/resources/script/<script>.groovy
     - src/main/resources/parameters.prop
     - src/main/resources/parameters.propdef
     - META-INF/MANIFEST.MF
     - metainfo.prop
     - project.properties
     - .project
"""
from __future__ import annotations

import base64
import datetime
import hashlib
import io
import json
import logging
import os
import re
import struct
import uuid
import zipfile
import zlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..base import GeneratedFile
from .iflow_generator import (
    IFlowGenerator,
    validate_and_normalize_iflow_xml,
    clean_script_filename,
    clean_iflow_filename,
)

logger = logging.getLogger(__name__)


def _build_sap_native_zip(
    entries: list[tuple[str, bytes]],
    timestamp: datetime.datetime | None = None,
) -> bytes:
    """
    Build a SAP Integration Suite-compatible ZIP archive from raw (name, data) pairs.

    SAP's native export format requires a specific binary convention that Python's
    standard ``zipfile`` module cannot produce: local file headers must carry
    ``flags=0x0808`` (bit 3: data-descriptor deferred + bit 11: UTF-8 filename)
    with CRC, compressed-size, and uncompressed-size all zero in the local header,
    followed by a ``PK\\x07\\x08`` data-descriptor record after the compressed payload
    that carries the real values.  Python's ``zipfile.writestr()`` / ``ZipFile.open('w')``
    always writes CRC and sizes into the local header immediately (non-streaming),
    resulting in ``flags=0x0000`` in local headers — a mismatch that SAP Integration
    Suite's importer rejects with "The file cannot be imported. Select a valid content
    package to continue."

    This function builds the archive entirely with ``struct.pack`` so every field is
    under explicit control:

    Per entry layout::

        [Local file header]  flags=0x0808, crc=0, csz=0, usz=0
        [Compressed data]    raw DEFLATE (wbits=-15, no zlib wrapper)
        [Data descriptor]    PK\\x07\\x08 + crc32 + compressed_size + uncompressed_size

    Central directory follows all entries, then the end-of-central-directory record.

    Args:
        entries:   Ordered list of ``(filename, uncompressed_data)`` tuples.
        timestamp: UTC datetime for all entries (defaults to now).

    Returns:
        Raw bytes of the complete, standards-compliant ZIP archive.
    """
    if timestamp is None:
        timestamp = datetime.datetime.now(datetime.timezone.utc)

    # DOS time fields (2-second granularity)
    mod_time = (
        (timestamp.second // 2)
        | (timestamp.minute << 5)
        | (timestamp.hour << 11)
    )
    mod_date = (
        timestamp.day
        | (timestamp.month << 5)
        | ((timestamp.year - 1980) << 9)
    )

    buf = io.BytesIO()
    cd_records: list[bytes] = []   # accumulated central-directory bytes
    cd_offsets: list[int] = []     # local-header offset for each entry

    for filename, raw_data in entries:
        raw_bytes = raw_data.encode("utf-8") if isinstance(raw_data, str) else raw_data
        fname_bytes = filename.encode("utf-8")

        # Compress with raw DEFLATE (no zlib header/trailer — matches zipfile default)
        compressor = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
        compressed = compressor.compress(raw_bytes) + compressor.flush()

        crc32 = zlib.crc32(raw_bytes) & 0xFFFFFFFF
        csz   = len(compressed)
        usz   = len(raw_bytes)

        local_offset = buf.tell()
        cd_offsets.append(local_offset)

        # Local file header — flags=0x0808, crc/csz/usz all zero
        buf.write(struct.pack(
            "<4sHHHHHIIIHH",
            b"PK\x03\x04",   # signature
            20,               # version needed to extract (2.0)
            0x0808,           # flags: bit3 (data descriptor) + bit11 (UTF-8)
            8,                # compression method: DEFLATE
            mod_time,
            mod_date,
            0,                # crc-32 (deferred to data descriptor)
            0,                # compressed size (deferred)
            0,                # uncompressed size (deferred)
            len(fname_bytes),
            0,                # extra field length
        ))
        buf.write(fname_bytes)
        buf.write(compressed)

        # Data descriptor — provides real CRC and sizes after compressed payload
        buf.write(struct.pack("<4sIII", b"PK\x07\x08", crc32, csz, usz))

        # Central directory record for this entry
        cd_records.append(struct.pack(
            "<4sHHHHHHIIIHHHHHII",
            b"PK\x01\x02",   # signature
            20,               # version made by (MS-DOS 2.0)
            20,               # version needed
            0x0808,           # flags (same as local header)
            8,                # compression: DEFLATE
            mod_time,
            mod_date,
            crc32,            # real CRC in central directory
            csz,              # real compressed size
            usz,              # real uncompressed size
            len(fname_bytes),
            0,                # extra field length
            0,                # file comment length
            0,                # disk number start
            0,                # internal file attributes
            0,                # external file attributes (zero — no Unix perms)
            local_offset,     # relative offset of local header
        ) + fname_bytes)

    cd_offset = buf.tell()
    for cdr in cd_records:
        buf.write(cdr)
    cd_size = buf.tell() - cd_offset
    n = len(entries)

    # End of central directory record
    buf.write(struct.pack(
        "<4sHHHHIIH",
        b"PK\x05\x06",   # signature
        0,               # disk number
        0,               # disk with start of central directory
        n,               # entries on this disk
        n,               # total entries
        cd_size,
        cd_offset,
        0,               # ZIP file comment length
    ))

    return buf.getvalue()


def _finalize_native_zip(zf: zipfile.ZipFile) -> None:
    """
    Standardizes all central directory entries in a standard zipfile.ZipFile archive
    (e.g., individual iFlow upload ZIPs, multi-flow bundles):
      - create_system = 0 (FAT / MS-DOS)
      - flag_bits = 0x808 (bit 3 data descriptor + bit 11 UTF-8 filename)
      - external_attr = 0 (zero permissions)
    """
    for zinfo in zf.filelist:
        zinfo.create_system = 0
        zinfo.flag_bits = 0x808
        zinfo.external_attr = 0





DISALLOWED_FLOW_STEMS = {
    "pom", "pom_xml", "log4j2", "log4j2_config", "log4j2_test", "log4j2-test",
    "application_types", "application-types", "applicationtypesflow", "application_types_flow",
    "mule_artifact", "mule-artifact", "global_config", "global-config", "mq",
    "readme", "license", "changelog", "notice", "package_json",
    "dev", "dev_config", "dev-config",
    "inputflow", "input_flow", "input-flow",
}


def _is_valid_flow_stem(stem: str) -> bool:
    """Returns True if the stem represents an executable business Integration Flow."""
    s = stem.lower().replace("-", "_").strip()
    if s in DISALLOWED_FLOW_STEMS:
        return False
    if s.startswith(("enrichment_auto_", "enrichment_", "auto_")):
        return False
    if s.startswith(("munit_", "test_")):
        return False
    if any(s.startswith(p) for p in ("readme", "log4j2", "application_types", "applicationtypes")):
        return False
    return True


OSGI_IMPORT_PACKAGES = (
    "com.sap.esb.application.services.cxf.interceptor,"
    "com.sap.esb.security,"
    "com.sap.it.op.agent.api,"
    "com.sap.it.op.agent.collector.camel,"
    "com.sap.it.op.agent.collector.cxf,"
    "com.sap.it.op.agent.mpl,"
    "javax.jms,"
    "javax.jws,"
    "javax.wsdl,"
    "javax.xml.bind.annotation,"
    "javax.xml.namespace,"
    "javax.xml.ws,"
    "org.apache.camel,"
    "org.apache.camel.builder,"
    "org.apache.camel.component.cxf,"
    "org.apache.camel.model,"
    "org.apache.camel.processor,"
    "org.apache.camel.processor.aggregate,"
    "org.apache.camel.spring.spi,"
    "org.apache.commons.logging,"
    "org.apache.cxf.binding,"
    "org.apache.cxf.binding.soap,"
    "org.apache.cxf.binding.soap.spring,"
    "org.apache.cxf.bus,"
    "org.apache.cxf.bus.resource,"
    "org.apache.cxf.bus.spring,"
    "org.apache.cxf.buslifecycle,"
    "org.apache.cxf.catalog,"
    "org.apache.cxf.configuration.jsse,"
    "org.apache.cxf.configuration.spring,"
    "org.apache.cxf.endpoint,"
    "org.apache.cxf.headers,"
    "org.apache.cxf.interceptor,"
    "org.apache.cxf.management.counters,"
    "org.apache.cxf.message,"
    "org.apache.cxf.phase,"
    "org.apache.cxf.resource,"
    "org.apache.cxf.service.factory,"
    "org.apache.cxf.service.model,"
    "org.apache.cxf.transport,"
    "org.apache.cxf.transport.common.gzip,"
    "org.apache.cxf.transport.http,"
    "org.apache.cxf.transport.http.policy,"
    "org.apache.cxf.workqueue,"
    "org.apache.cxf.ws.rm.persistence,"
    "org.apache.cxf.wsdl11,"
    "org.osgi.framework,"
    "org.slf4j,"
    "org.springframework.beans.factory.config,"
    "com.sap.esb.camel.security.cms,"
    "org.apache.camel.spi,"
    "com.sap.esb.webservice.audit.log,"
    "com.sap.esb.camel.endpoint.configurator.api,"
    "com.sap.esb.camel.jdbc.idempotency.reorg,"
    "javax.sql,"
    "org.apache.camel.processor.idempotent.jdbc,"
    "org.osgi.service.blueprint"
)


def format_osgi_manifest(headers: list[tuple[str, str]]) -> str:
    """
    Formats OSGi headers into a standard JAR Manifest compliant with RFC 2822:
    - Maximum 72 bytes per line (UTF-8 encoded).
    - Long lines are wrapped with CRLF followed by a single continuation space ('\\r\\n ').
    - Preserves multi-byte UTF-8 character boundaries.
    - Ends with CRLF and an extra trailing blank line.
    """
    def find_split_point(b_slice: bytes, limit: int) -> int:
        if len(b_slice) <= limit:
            return len(b_slice)
        split = limit
        while split > 0 and (b_slice[split] & 0xC0) == 0x80:
            split -= 1
        return split

    lines_out: list[bytes] = []
    for name, value in headers:
        header_bytes = f"{name}: {value}".encode("utf-8")
        if len(header_bytes) <= 72:
            lines_out.append(header_bytes)
        else:
            split1 = find_split_point(header_bytes, 72)
            lines_out.append(header_bytes[:split1])
            rem = header_bytes[split1:]
            while rem:
                split_cont = find_split_point(rem, 71)
                lines_out.append(b" " + rem[:split_cont])
                rem = rem[split_cont:]

    # Manifest must end with CRLF after all headers plus an extra empty line with CRLF
    return (b"\r\n".join(lines_out) + b"\r\n\r\n").decode("utf-8")


@dataclass
class CPIArtifact:
    """Represents a discrete Integration Flow artifact within a package."""
    artifact_id: str
    name: str
    symbolic_name: str
    version: str = "1.0.0"
    description: str = ""
    files: list[GeneratedFile] = field(default_factory=list)


class CPIPackageGenerator:
    """
    Assembles deployable SAP Cloud Integration (CPI) package bundles and individual iFlow archives.
    """

    MANIFEST_MF_TEMPLATE = """Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: {bundle_name}
Bundle-SymbolicName: {bundle_id}; singleton:=true
Bundle-Version: {bundle_version}
SAP-BundleType: IntegrationFlow
SAP-NodeType: IFLMAP
SAP-RuntimeProfile: iflmap
Import-Package: {import_packages}
Origin-Bundle-Name: {bundle_name}
Origin-Bundle-SymbolicName: {bundle_id}
"""

    METAINFO_PROP_TEMPLATE = """#Product profile
ProductProfile=iflmap
#Artifact type
ArtifactType=IntegrationFlow
#Bundle symbolic name
Bundle-SymbolicName={bundle_id}
#Bundle name
Bundle-Name={bundle_name}
#Bundle version
Bundle-Version={bundle_version}
#Origin description
Origin=Migrated from MuleSoft via Tissa Intelli-Migrate
"""

    PROJECT_PROPERTIES_TEMPLATE = """#Project properties
project.type=iflow
source.mulesoft.migrated=true
project.version={bundle_version}
"""

    DOT_PROJECT_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?><projectDescription>
   <name>{bundle_id}</name>
   <comment/>
   <projects/>
   <buildSpec>
      <buildCommand>
         <name>org.eclipse.jdt.core.javabuilder</name>
         <arguments/>
      </buildCommand>
   </buildSpec>
   <natures>
      <nature>org.eclipse.jdt.core.javanature</nature>
      <nature>com.sap.ide.ifl.project.support.project.nature</nature>
      <nature>com.sap.ide.ifl.bsn</nature>
   </natures>
</projectDescription>
"""

    PARAMETERS_PROPDEF_TEMPLATE = """<?xml version="1.0" encoding="UTF-8" standalone="no"?><parameters><param_references/></parameters>"""

    def __init__(self) -> None:
        self.iflow_gen = IFlowGenerator()

    def build_package_manifests(
        self,
        project_id: str,
        project_name: str,
        version: str = "1.0.0",
        include_metainfo: bool = True,
    ) -> list[GeneratedFile]:
        """
        Creates mandatory manifest and metadata descriptor files for SAP CPI artifact project.
        Uses format_osgi_manifest to enforce 72-byte line wrapping and CRLF line endings.
        """
        clean_id = self._safe_identifier(project_id) or "MuleMigratedFlow"
        clean_name = project_name or clean_id

        manifest_headers = [
            ("Manifest-Version", "1.0"),
            ("Bundle-ManifestVersion", "2"),
            ("Bundle-Name", clean_name),
            ("Bundle-SymbolicName", f"{clean_id}; singleton:=true"),
            ("Bundle-Version", version),
            ("SAP-BundleType", "IntegrationFlow"),
            ("SAP-NodeType", "IFLMAP"),
            ("SAP-RuntimeProfile", "iflmap"),
            ("Import-Package", OSGI_IMPORT_PACKAGES),
            ("Origin-Bundle-Name", clean_name),
            ("Origin-Bundle-SymbolicName", clean_id),
        ]
        manifest_content = format_osgi_manifest(manifest_headers)
        dot_project_content = self.DOT_PROJECT_TEMPLATE.format(
            bundle_id=clean_id,
        )

        res = [
            GeneratedFile(
                path="META-INF/MANIFEST.MF",
                content=manifest_content,
                role="config",
            ),
            GeneratedFile(
                path=".project",
                content=dot_project_content,
                role="config",
            ),
            GeneratedFile(
                path="src/main/resources/parameters.prop",
                content="# SAP Cloud Integration Externalized Parameters\n# Generated by Tissa Intelli-Migrate\n",
                role="config",
            ),
            GeneratedFile(
                path="src/main/resources/parameters.propdef",
                content=self.PARAMETERS_PROPDEF_TEMPLATE,
                role="config",
            ),
        ]

        if include_metainfo:
            metainfo_content = self.METAINFO_PROP_TEMPLATE.format(
                bundle_name=clean_name,
                bundle_id=clean_id,
                bundle_version=version,
            )
            project_prop_content = self.PROJECT_PROPERTIES_TEMPLATE.format(
                bundle_version=version,
            )
            res.extend([
                GeneratedFile(
                    path="metainfo.prop",
                    content=metainfo_content,
                    role="config",
                ),
                GeneratedFile(
                    path="project.properties",
                    content=project_prop_content,
                    role="config",
                ),
            ])

        return res

    def create_content_package_inner_archive(self, artifact: CPIArtifact) -> bytes:
        """
        Packs a single flow project for inclusion as `{artifact_id}_content` inside
        a Content Package ZIP. In native SAP CPI, content bundles strictly contain:
        - src/main/resources/scenarioflows/integrationflow/<flow>.iflw
        - src/main/resources/parameters.prop
        - src/main/resources/parameters.propdef
        - src/main/resources/script/<referenced_scripts_only>.groovy
        - .project
        - META-INF/MANIFEST.MF
        (Excludes metainfo.prop and project.properties, which only belong to standalone iFlow uploads)
        """
        descriptors = self.build_package_manifests(
            artifact.symbolic_name,
            artifact.name,
            version=artifact.version,
            include_metainfo=False,
        )

        files_to_pack = list(artifact.files)
        existing_paths = {f.path for f in files_to_pack}
        for desc in descriptors:
            if desc.path not in existing_paths:
                files_to_pack.append(desc)

        deduped_files: dict[str, GeneratedFile] = {}
        for f in files_to_pack:
            clean_path = self._normalize_resource_path(f.path)
            # Never include metainfo.prop or project.properties in native content package bundles
            if clean_path in ("metainfo.prop", "project.properties", "src/main/resources/parameters/parameters.prop"):
                continue
            deduped_files[clean_path] = f

        inner_script_names = [Path(p).name for p in deduped_files if p.endswith(".groovy")]
        now_dt = datetime.datetime.now(datetime.timezone.utc)

        extra_scripts: dict[str, str] = {}
        # Pre-pass: process .iflw content first to discover all extra_scripts needed
        for clean_path in list(deduped_files.keys()):
            f = deduped_files[clean_path]
            content = f.content
            if clean_path.endswith(".iflw") and isinstance(content, str):
                target_iflw_path = f"src/main/resources/scenarioflows/integrationflow/{artifact.name}.iflw"
                content, _ = validate_and_normalize_iflow_xml(
                    content,
                    flow_name=artifact.name,
                    available_scripts=inner_script_names,
                )
                # Normalize any <key>script</key><value>...</value> to clean filename
                def _clean_inner_script_val(m: re.Match) -> str:
                    cname = clean_script_filename(m.group(1).strip())
                    for sn in inner_script_names:
                        if sn.lower() == cname.lower() or sn[:-7].lower().replace("-", "_") == cname[:-7].lower().replace("-", "_"):
                            return f"<key>script</key><value>{sn}</value>"
                    return f"<key>script</key><value>{cname}</value>"

                content = re.sub(
                    r"<key>script</key>\s*<value>([^<]+)</value>",
                    _clean_inner_script_val,
                    content,
                )
                for ref in re.findall(r"<key>script</key>\s*<value>([^<]+)</value>", content):
                    ref_clean = clean_script_filename(ref.strip())
                    ref_path = f"src/main/resources/script/{ref_clean}"
                    if ref_path not in deduped_files and ref_path not in extra_scripts:
                        extra_scripts[ref_path] = (
                            "import com.sap.gateway.ip.core.customdev.util.Message\n\n"
                            "def Message processData(Message message) {\n"
                            f"    // Auto-generated stub for {ref_clean}\n"
                            "    return message\n"
                            "}\n"
                        )
                if clean_path != target_iflw_path:
                    del deduped_files[clean_path]
                deduped_files[target_iflw_path] = GeneratedFile(
                    path=target_iflw_path,
                    content=content,
                    role=f.role,
                    generator=f.generator,
                )

        # Merge extra stubs into deduped_files before ordering
        for sp_path, sp_content in extra_scripts.items():
            if sp_path not in deduped_files:
                deduped_files[sp_path] = GeneratedFile(
                    path=sp_path, content=sp_content, role="source",
                )

        # Native SAP canonical entry ordering:
        # 1. .iflw files  (src/main/resources/scenarioflows/integrationflow/*.iflw)
        # 2. parameters.prop
        # 3. parameters.propdef
        # 4. scripts       (src/main/resources/script/*.groovy)
        # 5. .project
        # 6. META-INF/MANIFEST.MF  (always last)
        def _entry_sort_key(path: str) -> tuple:
            if path.endswith(".iflw"):
                return (0, path)
            if path == "src/main/resources/parameters.prop":
                return (1, path)
            if path == "src/main/resources/parameters.propdef":
                return (2, path)
            if path.endswith(".groovy") or path.endswith(".gvy"):
                return (3, path)
            if path == ".project":
                return (4, path)
            if "MANIFEST.MF" in path:
                return (6, path)
            return (5, path)

        ordered_paths = sorted(deduped_files.keys(), key=_entry_sort_key)
        inner_entries: list[tuple[str, bytes]] = []
        for clean_path in ordered_paths:
            f = deduped_files[clean_path]
            content_bytes = f.content.encode("utf-8") if isinstance(f.content, str) else f.content
            inner_entries.append((clean_path, content_bytes))

        return _build_sap_native_zip(inner_entries, now_dt)



    def create_individual_iflow_archive(self, artifact: CPIArtifact) -> bytes:
        """
        Packs a single Integration Flow into a deployable artifact ZIP suitable for
        individual upload inside an existing package (includes metainfo.prop & project.properties).
        """
        buffer = io.BytesIO()
        descriptors = self.build_package_manifests(
            artifact.symbolic_name,
            artifact.name,
            version=artifact.version,
            include_metainfo=True,
        )

        files_to_pack = list(artifact.files)
        existing_paths = {f.path for f in files_to_pack}
        for desc in descriptors:
            if desc.path not in existing_paths:
                files_to_pack.append(desc)

        deduped_files: dict[str, GeneratedFile] = {}
        for f in files_to_pack:
            clean_path = self._normalize_resource_path(f.path)
            if clean_path == "src/main/resources/parameters/parameters.prop":
                continue
            deduped_files[clean_path] = f

        inner_script_names = [clean_script_filename(Path(p).name) for p in deduped_files if p.endswith(".groovy")]

        with zipfile.ZipFile(buffer, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
            extra_scripts: dict[str, str] = {}
            for clean_path, f in deduped_files.items():
                content = f.content
                if clean_path.endswith(".iflw") and isinstance(content, str):
                    content, _ = validate_and_normalize_iflow_xml(
                        content,
                        flow_name=artifact.name,
                        available_scripts=inner_script_names,
                    )
                    def _clean_indiv_script_val(m: re.Match) -> str:
                        cname = clean_script_filename(m.group(1).strip())
                        for sn in inner_script_names:
                            if sn.lower() == cname.lower() or sn[:-7].lower().replace("-", "_") == cname[:-7].lower().replace("-", "_"):
                                return f"<key>script</key><value>{sn}</value>"
                        return f"<key>script</key><value>{cname}</value>"

                    content = re.sub(
                        r"<key>script</key>\s*<value>([^<]+)</value>",
                        _clean_indiv_script_val,
                        content,
                    )
                    for ref in re.findall(r"<key>script</key>\s*<value>([^<]+)</value>", content):
                        ref_clean = clean_script_filename(ref.strip())
                        ref_path = f"src/main/resources/script/{ref_clean}"
                        if ref_path not in deduped_files and ref_path not in extra_scripts:
                            extra_scripts[ref_path] = (
                                "import com.sap.gateway.ip.core.customdev.util.Message\n\n"
                                "def Message processData(Message message) {\n"
                                f"    // Auto-generated stub for {ref_clean}\n"
                                "    return message\n"
                                "}\n"
                            )
                content_bytes = content.encode("utf-8") if isinstance(content, str) else content
                zf.writestr(clean_path, content_bytes)

            for sp_path, sp_content in extra_scripts.items():
                zf.writestr(sp_path, sp_content.encode("utf-8"))

            _finalize_native_zip(zf)
        return buffer.getvalue()

    def create_content_package_archive(
        self,
        package_id: str,
        package_name: str,
        artifacts: list[CPIArtifact],
        version: str = "1.0.0",
        description: str = "Migrated from MuleSoft via Tissa Intelli-Migrate",
        short_text: str = "MuleSoft migrated integration package",
    ) -> bytes:
        """
        Assembles an SAP CPI Content Package ZIP for import via Design → Integrations and APIs → Import.
        Produces a ZIP with cross-tenant-neutral contentmetadata.md (Organization=TEST by default),
        canonical inner-archive entry ordering that matches native SAP exports, and consistent
        SHA-256 hashes per resource. Organization and Environment are configurable via environment
        variables SAP_CPI_ORGANIZATION and SAP_CPI_ENVIRONMENT for tenant-specific exports.
        For fully automated headless delivery, the OData design-time API (cpi_api_client.py) is preferred.
        """
        logger.info(
            "Generating SAP CPI Content Package ZIP. "
            "Organization and Environment use cross-tenant-neutral defaults (overridable via "
            "SAP_CPI_ORGANIZATION / SAP_CPI_ENVIRONMENT env vars). "
            "For fully automated delivery, use the OData API client (cpi_api_client.py)."
        )
        clean_package_id = self._safe_32hex_id(package_id)
        base_pkg_uid = self._safe_package_unique_id(package_id)
        package_unique_id = base_pkg_uid
        # display_package_name: human-readable with spaces, used in ExportInformation.info and displayName.
        # If package_name already contains spaces (e.g. "Employee Payroll Processor"), use it directly.
        # Otherwise normalise underscores/hyphens to spaces and title-case each word.
        raw_name = package_name or package_unique_id
        clean_package_name = raw_name.replace("_", " ").replace("-", " ").strip()
        clean_package_name = " ".join(w[:1].upper() + w[1:] for w in clean_package_name.split()) or package_unique_id


        # Distinct container prefix for masterId semantics
        master_container_prefix = self._safe_32hex_id(f"container_{clean_package_id}")

        now_dt = datetime.datetime.now(datetime.timezone.utc)
        now_millis = int(now_dt.timestamp() * 1000)
        now_micros = int(now_dt.timestamp() * 1000000)
        date_formatted = now_dt.strftime("%a %b %d %H:%M:%S UTC %Y")

        outer_entries: list[tuple[str, bytes]] = []
        resources_list: list[dict[str, Any]] = []
        relations_list: list[dict[str, Any]] = []
        artifact_hashes: list[str] = []

        # 1. Package nested artifacts
        seen_unique_ids: set[str] = set()
        seen_art_names: set[str] = set()
        for artifact in artifacts:
            art_id = self._safe_32hex_id(artifact.artifact_id)
            inner_zip_bytes = self.create_content_package_inner_archive(artifact)
            inner_entry_name = f"{art_id}_content"
            outer_entries.append((inner_entry_name, inner_zip_bytes))
            artifact_hashes.append(hashlib.sha256(inner_zip_bytes).hexdigest())

            # Add to resources.cnt with uniqueness safeguards
            base_symbolic = self._safe_identifier(artifact.symbolic_name or artifact.name) or "flow"
            flow_symbolic = base_symbolic
            counter = 2
            while flow_symbolic in seen_unique_ids:
                flow_symbolic = f"{base_symbolic}_{counter}"
                counter += 1
            seen_unique_ids.add(flow_symbolic)

            art_name = artifact.name
            counter = 2
            while art_name in seen_art_names:
                art_name = f"{artifact.name}_{counter}"
                counter += 1
            seen_art_names.add(art_name)

            resources_list.append({
                "version": 1,
                "revision": 0,
                "masterId": f"{master_container_prefix}:{art_id}:1",
                "versionComment": "",
                "globalModifiedDate": now_micros,
                "isValidHash": 0,
                "id": art_id,
                "name": f"{art_name}.zip",
                "createdBy": "MigrationStudio",
                "createdAt": now_millis,
                "uniqueId": flow_symbolic,
                "modifiedBy": "MigrationStudio",
                "modifiedAt": now_millis,
                "additionalAttributes": {
                    "Description": {
                        "isExtendedLargeAttribute": True,
                        "attributeValues": [artifact.description or f"MuleSoft migrated flow: {art_name}"],
                    },
                    "OriginBundleSymbolicName": {
                        "isExtendedLargeAttribute": False,
                        "attributeValues": [flow_symbolic],
                    },
                    "nodeType": {
                        "isExtendedLargeAttribute": False,
                        "attributeValues": ["IFLMAP"],
                    },
                    "OriginBundleName": {
                        "isExtendedLargeAttribute": False,
                        "attributeValues": [art_name],
                    },
                    "productProfile": {
                        "isExtendedLargeAttribute": False,
                        "attributeValues": ["iflmap"],
                    },
                },
                "resourceType": "IFlow",
                "contentType": "application/octet-stream",
                "displayName": art_name,
                "semanticVersion": artifact.version or version,
                "privilegeState": "EDIT_ALLOWED",
                "isRestricted": False,
                "isInternal": False,
                "isGroupDefault": False,
                "resourceReferences": [],
            })

            relations_list.append({
                "sourceId": clean_package_id,
                "targetId": art_id,
                "relationType": "AGGREGATION",
                "RelationName": "Default",
            })

        # 2. Add ContentPackage resource (strictly matching native SAP export)
        counter = 2
        while package_unique_id in seen_unique_ids:
            package_unique_id = f"{base_pkg_uid}{counter}"
            counter += 1
        seen_unique_ids.add(package_unique_id)
        resources_list.append({
            "version": 1,
            "revision": 0,
            "masterId": f"{master_container_prefix}:{clean_package_id}:1",
            "globalModifiedDate": now_micros,
            "isValidHash": 0,
            "id": clean_package_id,
            "name": package_unique_id,
            "createdBy": "MigrationStudio",
            "createdAt": now_millis,
            "uniqueId": package_unique_id,
            "modifiedBy": "MigrationStudio",
            "modifiedAt": now_millis,
            "additionalAttributes": {
                "Industries": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": [""],
                },
                "Description": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": [f"<p>{description}</p>"],
                },
                "Keyword": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": [""],
                },
                "Version": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": [version],
                },
                "shortText": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": [short_text],
                },
                "Product": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": [""],
                },
                "LineOfBusiness": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": [""],
                },
                "Country": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": [""],
                },
                "category": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": ["Integration"],
                },
                "SupportedPlatform": {
                    "isExtendedLargeAttribute": False,
                    "attributeValues": ["SAP HANA Cloud Integration"],
                },
            },
            "auxilaryProperties": {},
            "resourceType": "ContentPackage",
            "displayName": clean_package_name,
            "semanticVersion": version,
            "privilegeState": "EDIT_ALLOWED",
            "isRestricted": False,
            "isInternal": False,
            "isGroupDefault": False,
            "resourceReferences": [],
        })

        # 3. Serialize resources.cnt (Base64 JSON)
        cnt_data = {"resources": resources_list, "relations": relations_list}
        cnt_json = json.dumps(cnt_data, separators=(",", ":"))
        cnt_b64 = base64.b64encode(cnt_json.encode("utf-8")).decode("utf-8")
        cnt_bytes = cnt_b64.encode("utf-8")
        outer_entries.append(("resources.cnt", cnt_bytes))

        # 4. Serialize contentmetadata.md (Base64 properties)
        # Organization defaults to "TEST" — the cross-tenant-neutral sentinel used by SAP's
        # own native exports (observed in reference package: Organization=TEST).
        # Using a specific trial tenant ID (e.g. "16fa66c4trial") causes rejection on any
        # other tenant because SAP validates the Organization against the importing tenant.
        # Environment defaults to "sap-integration-suite" — the generic environment name
        # that is accepted by all SAP Integration Suite tenants regardless of subdomain.
        # Both can be overridden via environment variables for tenant-specific exports.
        org = os.environ.get("SAP_CPI_ORGANIZATION", "TEST")
        env = os.environ.get("SAP_CPI_ENVIRONMENT", "sap-integration-suite")
        metadata_props = (
            "-- listing properties --\n"
            "HashVersion=2.0.0\n"
            "EncodingVersion=1.0.0\n"
            f"Organization={org}\n"
            f"Environment={env}\n"
            "RelationClassVersion=1.0.0\n"
            "ResourceClassVersion=1.2.0\n"
            "ExportModelVersion=1.0.0\n"
        )
        md_b64 = base64.b64encode(metadata_props.encode("utf-8")).decode("utf-8")
        md_bytes = md_b64.encode("utf-8")
        outer_entries.append(("contentmetadata.md", md_bytes))

        # 5. Serialize hash (One SHA-256 hash per resource in resources.cnt)
        # NOTE: SAP HashVersion 2.0.0 is proprietary and does not match plain SHA-256.
        # This output is provided for structure matching only.
        cnt_sha256 = hashlib.sha256(cnt_bytes).hexdigest()
        hashes_list = artifact_hashes + [cnt_sha256]
        hash_bytes = json.dumps(hashes_list, separators=(",", ":")).encode("utf-8")
        outer_entries.append(("hash", hash_bytes))

        # 6. Serialize ExportInformation.info (matching native SAP CPI export without trailing newline)
        export_info = f"Name= {clean_package_name}\nDate= {date_formatted}"
        outer_entries.append(("ExportInformation.info", export_info.encode("utf-8")))

        return _build_sap_native_zip(outer_entries, now_dt)


    def create_zip_archive(
        self,
        files: list[GeneratedFile],
        package_id: str = "mule_cpi_pkg",
        package_name: str = "MuleSoft CPI Migration",
        export_type: str = "iflow",
        version: str = "1.0.0",
    ) -> bytes:
        """
        Unified packaging interface. Automatically partitions flat GeneratedFiles into
        isolated CPIArtifacts with normalized paths and XML, then builds either:
        - Individual Flow ZIP or multi-flow bundle (export_type='iflow' or 'cpi-iflow') [RECOMMENDED / PRIMARY]
        - Full Content Package ZIP (export_type='package' or 'cpi-package') [EXPERIMENTAL]
        """
        artifacts = self._partition_files_to_artifacts(files, package_id, package_name, version)

        if export_type in ("iflow", "cpi-iflow", "individual_iflow", "bundle"):
            if not artifacts:
                default_artifact = CPIArtifact(
                    artifact_id=self._safe_32hex_id(package_id),
                    name=package_name,
                    symbolic_name=self._safe_identifier(package_id),
                    version=version,
                    files=files,
                )
                return self.create_individual_iflow_archive(default_artifact)
            if len(artifacts) == 1:
                return self.create_individual_iflow_archive(artifacts[0])

            # Multi-flow bundle (No-credentials fallback): package each flow into its own self-contained .zip inside a parent bundle
            bundle_buffer = io.BytesIO()
            with zipfile.ZipFile(bundle_buffer, mode="w", compression=zipfile.ZIP_DEFLATED) as bzf:
                for art in artifacts:
                    flow_zip_bytes = self.create_individual_iflow_archive(art)
                    bzf.writestr(f"{art.name}.zip", flow_zip_bytes)

                instructions = (
                    "================================================================================\n"
                    "SAP Integration Suite (Cloud Integration) Migration Bundle\n"
                    "No-Credentials / Individual Flow UI Upload Fallback\n"
                    "================================================================================\n"
                    f"Package Name: {package_name}\n"
                    f"Package ID:   {package_id}\n"
                    f"Total Flows:  {len(artifacts)}\n\n"
                    "WHY THIS ROUTE:\n"
                    "SAP Integration Suite UI imports of hand-built package ZIPs fail with\n"
                    "'Select a valid content package' due to SAP's proprietary HashVersion 2.0.0.\n"
                    "Uploading individual iFlow archives directly into a package created in the UI\n"
                    "completely bypasses the package hash check and guarantees successful import.\n\n"
                    "STEP-BY-STEP UPLOAD INSTRUCTIONS:\n"
                    "1. Log in to SAP Integration Suite Web UI.\n"
                    "2. Navigate to: Design -> Integrations and APIs.\n"
                    "3. Click 'Create' to create a package (or open an existing package).\n"
                    f"   - Name: {package_name}\n"
                    f"   - Technical ID: {package_id}\n"
                    f"   - Short Text: MuleSoft migrated flows for {package_name}\n"
                    "4. Open the package and click 'Edit' in the top-right corner.\n"
                    "5. Switch to the 'Artifacts' tab.\n"
                    "6. Click 'Add' -> 'Integration Flow' -> 'Upload'.\n"
                    "7. Upload each .zip file from this bundle folder one by one.\n"
                    "8. Click 'Save' and then 'Deploy' on each Integration Flow.\n\n"
                    "ALTERNATIVE (RECOMMENDED FOR AUTOMATION):\n"
                    "Use the OData Design-Time API Client (`cpi_api_client.py` or `mule-parser cpi-push`)\n"
                    "to push the package and all flows directly to your tenant without manual UI uploads.\n"
                    "================================================================================\n"
                )
                bzf.writestr("INSTRUCTIONS.txt", instructions.encode("utf-8"))

                readme_md = (
                    f"# SAP Integration Suite Migration Bundle: {package_name}\n\n"
                    "## Individual Integration Flow Upload Guide (No-Credentials Fallback)\n\n"
                    f"- **Package Name**: `{package_name}`\n"
                    f"- **Package ID**: `{package_id}`\n"
                    f"- **Total Flows**: {len(artifacts)}\n\n"
                    "### Why this route?\n"
                    "SAP Integration Suite UI imports of hand-built package ZIPs fail with generic\n"
                    "`'Select a valid content package'` due to SAP's proprietary `HashVersion 2.0.0`.\n"
                    "Uploading individual iFlow archives directly into a package created in the UI\n"
                    "completely bypasses the package hash check and guarantees successful import.\n\n"
                    "### Step-by-Step Instructions\n"
                    "1. Log in to your SAP Integration Suite tenant Web UI.\n"
                    "2. Navigate to: **Design** → **Integrations and APIs**.\n"
                    f"3. Click **Create** to create a package:\n"
                    f"   - **Name**: `{package_name}`\n"
                    f"   - **Technical ID**: `{package_id}`\n"
                    f"   - **Short Text**: `MuleSoft migrated flows for {package_name}`\n"
                    "4. Open the package and click **Edit** (top-right corner).\n"
                    "5. Switch to the **Artifacts** tab.\n"
                    "6. Click **Add** → **Integration Flow** → **Upload**.\n"
                    "7. Upload each `<flow>.zip` file from this folder one by one.\n"
                    "8. Click **Save** and then **Deploy** on each Integration Flow.\n\n"
                    "### Headless Automated Delivery (Recommended)\n"
                    "To import directly via the SAP OData design-time API without manual UI uploads:\n"
                    "```bash\n"
                    f"mule-parser cpi-push --package-id {package_id} --service-key <service_key.json> --flows-dir <extracted_folder> --deploy\n"
                    "```\n"
                )
                bzf.writestr("README.md", readme_md.encode("utf-8"))
                _finalize_native_zip(bzf)
            return bundle_buffer.getvalue()

        return self.create_content_package_archive(
            package_id=package_id,
            package_name=package_name,
            artifacts=artifacts,
            version=version,
        )

    def _partition_files_to_artifacts(
        self,
        files: list[GeneratedFile],
        package_id: str,
        package_name: str,
        version: str,
    ) -> list[CPIArtifact]:
        """Partitions input files into discrete CPIArtifacts per verified iFlow."""
        # Pre-normalize resource paths and identify all scripts
        script_files: list[GeneratedFile] = []
        for f in files:
            clean_path = self._normalize_resource_path(f.path)
            if clean_path.endswith((".groovy", ".gvy")):
                cname = clean_script_filename(clean_path.split("/")[-1])
                script_files.append(GeneratedFile(
                    path=f"src/main/resources/script/{cname}",
                    content=f.content,
                    role="source",
                    generator=f.generator,
                ))

        available_script_names = [clean_script_filename(Path(s.path).name) for s in script_files]
        scripts_by_name = {clean_script_filename(Path(s.path).name).lower(): s for s in script_files}

        normalized_files: list[GeneratedFile] = []
        for f in files:
            clean_path = self._normalize_resource_path(f.path)
            content = f.content
            if clean_path.endswith(".iflw"):
                content, _ = validate_and_normalize_iflow_xml(
                    content,
                    flow_name=clean_path,
                    available_scripts=available_script_names,
                )
            normalized_files.append(GeneratedFile(
                path=clean_path,
                content=content,
                role=f.role,
                generator=f.generator,
            ))

        # Separate files by role
        all_iflow_files = [f for f in normalized_files if f.path.endswith(".iflw")]
        param_files = [f for f in normalized_files if f.path in ("src/main/resources/parameters.prop", "src/main/resources/parameters.propdef")]

        # Filter out non-flow files (pom, log4j2, application_types, enrichment_auto_*, dev, inputflow, etc.)
        raw_iflow_files: list[GeneratedFile] = []
        for iflow_file in all_iflow_files:
            stem = Path(iflow_file.path).stem
            if not self._is_valid_flow_stem(stem):
                logger.debug("Skipping non-flow artifact: %s", iflow_file.path)
                continue
            txt = iflow_file.content.decode("utf-8", "ignore") if isinstance(iflow_file.content, bytes) else str(iflow_file.content or "")
            if "<bpmn2:definitions" not in txt or "# No flows" in txt:
                logger.debug("Skipping invalid BPMN2 XML artifact: %s", iflow_file.path)
                continue
            # Also check if it's an empty scheduler leftover flow (scheduler with no tasks or scripts)
            if stem.lower().replace("-", "_") in ("scheduler", "schedulerflow", "scheduler_flow"):
                has_logic = any(tok in txt for tok in ("callActivity", "serviceTask", "scriptTask", "<key>script</key>", ".groovy"))
                if not has_logic:
                    logger.debug("Skipping empty leftover scheduler artifact: %s", iflow_file.path)
                    continue
            raw_iflow_files.append(iflow_file)

        # Deduplicate flows where normalized stems collide and content is duplicate
        valid_iflow_files: list[GeneratedFile] = []
        seen_normalized: dict[str, GeneratedFile] = {}
        for iflow_file in raw_iflow_files:
            stem = Path(iflow_file.path).stem
            norm_key = stem.lower().replace("-", "_").strip()
            txt = iflow_file.content.decode("utf-8", "ignore") if isinstance(iflow_file.content, bytes) else str(iflow_file.content or "")
            if norm_key in seen_normalized:
                prev = seen_normalized[norm_key]
                prev_txt = prev.content.decode("utf-8", "ignore") if isinstance(prev.content, bytes) else str(prev.content or "")
                # If XML content is identical or one is an empty stub, eliminate the duplicate collision
                if txt.strip() == prev_txt.strip() or len(txt.strip()) < 80:
                    logger.info("Dropping duplicate flow '%s' (matches '%s')", stem, Path(prev.path).stem)
                    continue
                elif len(prev_txt.strip()) < 80:
                    valid_iflow_files.remove(prev)
                    valid_iflow_files.append(iflow_file)
                    seen_normalized[norm_key] = iflow_file
                    continue
                else:
                    logger.warning("Distinct flows collide on normalized identifier '%s' ('%s' vs '%s'); preserving both with disambiguated suffix.", norm_key, Path(prev.path).stem, stem)
            seen_normalized[norm_key] = iflow_file
            valid_iflow_files.append(iflow_file)

        if not valid_iflow_files:
            # Create a single default flow if project had no flows
            default_stem = self._safe_identifier(package_name) or "MainFlow"
            default_xml = self.iflow_gen.generate_iflow({"name": default_stem}, available_scripts=available_script_names)
            valid_iflow_files.append(GeneratedFile(
                path=f"src/main/resources/scenarioflows/integrationflow/{default_stem}.iflw",
                content=default_xml,
                role="source",
                generator="sap:default",
            ))

        artifacts: list[CPIArtifact] = []
        seen_sym_names: set[str] = set()
        seen_names: set[str] = set()
        for iflow_file in valid_iflow_files:
            stem = Path(iflow_file.path).stem
            base_sym_name = self._safe_identifier(stem) or "flow"
            sym_name = base_sym_name
            counter = 2
            while sym_name in seen_sym_names:
                sym_name = f"{base_sym_name}_{counter}"
                counter += 1
            seen_sym_names.add(sym_name)

            art_name = stem
            counter = 2
            while art_name in seen_names:
                art_name = f"{stem}_{counter}"
                counter += 1
            seen_names.add(art_name)

            art_id = self._safe_32hex_id(f"{package_id}_{sym_name}")

            # Discover referenced scripts specifically for THIS flow
            xml_str = iflow_file.content if isinstance(iflow_file.content, str) else ""
            referenced_script_names: set[str] = set()

            # 1. Match from <key>script</key><value>XYZ.groovy</value>
            for match in re.findall(r"<key>script</key>\s*<value>([^<]+)</value>", xml_str):
                m = clean_script_filename(match.strip())
                if m:
                    referenced_script_names.add(m)

            # 2. Match any *.groovy referenced in attributes or body
            for match in re.findall(r"([a-zA-Z0-9_\-:]+\.groovy)", xml_str):
                m = clean_script_filename(match.strip())
                if m:
                    referenced_script_names.add(m)

            # 3. Match scripts by flow stem prefix (longest match among all flows)
            clean_stem = stem.lower().replace("-", "").replace("_", "")
            for s in script_files:
                s_name = Path(s.path).name
                clean_sname = s_name.lower().replace(".groovy", "").replace("-", "").replace("_", "")
                matching_stems = [
                    Path(f.path).stem.lower().replace("-", "").replace("_", "")
                    for f in valid_iflow_files
                    if clean_sname.startswith(Path(f.path).stem.lower().replace("-", "").replace("_", ""))
                ]
                if matching_stems:
                    best_match = max(matching_stems, key=len)
                    if best_match == clean_stem:
                        referenced_script_names.add(s_name)

            art_files: list[GeneratedFile] = [iflow_file]
            matched_scripts: set[str] = set()

            for ref in referenced_script_names:
                bare_ref = clean_script_filename(ref)
                ref_lower = bare_ref.lower()
                matched_s = None
                if ref_lower in scripts_by_name:
                    matched_s = scripts_by_name[ref_lower]
                else:
                    ref_norm = bare_ref[:-7].lower().replace("-", "_")
                    for s_lower, s_file in scripts_by_name.items():
                        s_norm = s_lower[:-7].replace("-", "_")
                        if s_norm == ref_norm:
                            matched_s = s_file
                            bare_ref = Path(s_file.path).name
                            break

                if matched_s:
                    dest_path = f"src/main/resources/script/{bare_ref}"
                    art_files.append(GeneratedFile(
                        path=dest_path,
                        content=matched_s.content,
                        role="source",
                    ))
                    matched_scripts.add(ref_lower)
                else:
                    # Synthesize valid Groovy stub for any referenced script missing from input
                    stub_content = (
                        "import com.sap.gateway.ip.core.customdev.util.Message\n\n"
                        "def Message processData(Message message) {\n"
                        f"    // Auto-generated stub for {bare_ref}\n"
                        "    return message\n"
                        "}\n"
                    )
                    art_files.append(GeneratedFile(
                        path=f"src/main/resources/script/{bare_ref}",
                        content=stub_content,
                        role="source",
                    ))
                    matched_scripts.add(ref_lower)

            # If this is the only iflow artifact and no script was explicitly matched, attach all script files
            if len(valid_iflow_files) == 1 and not matched_scripts and script_files:
                for s in script_files:
                    art_files.append(s)

            # Attach parameters
            if param_files:
                art_files.extend(param_files)
            else:
                art_files.append(GeneratedFile(
                    path="src/main/resources/parameters.prop",
                    content="# SAP Cloud Integration Externalized Parameters\n",
                    role="config",
                ))
                art_files.append(GeneratedFile(
                    path="src/main/resources/parameters.propdef",
                    content=self.PARAMETERS_PROPDEF_TEMPLATE,
                    role="config",
                ))

            artifacts.append(CPIArtifact(
                artifact_id=art_id,
                name=art_name,
                symbolic_name=sym_name,
                version=version,
                description=f"MuleSoft migrated flow: {art_name}",
                files=art_files,
            ))

        return artifacts

    def _normalize_resource_path(self, path: str) -> str:
        """Corrects integrationscenarioflows to integrationflow, strips colons and standardizes slashes."""
        p = path.replace("\\", "/")
        if "scenarioflows/integrationscenarioflows/" in p:
            p = p.replace("scenarioflows/integrationscenarioflows/", "scenarioflows/integrationflow/")
        if p.endswith((".groovy", ".gvy")):
            stem = p.split("/")[-1]
            safe_stem = clean_script_filename(stem)
            p = f"src/main/resources/script/{safe_stem}"
        elif p.endswith(".iflw"):
            stem = p.split("/")[-1]
            safe_stem = clean_iflow_filename(stem)
            p = f"src/main/resources/scenarioflows/integrationflow/{safe_stem}"
        return p

    def _is_valid_flow_stem(self, stem: str) -> bool:
        return _is_valid_flow_stem(stem)

    def _safe_identifier(self, value: str) -> str:
        clean = "".join(c if c.isalnum() else "_" for c in (value or "")).strip("_")
        return clean or "Artifact"

    def _safe_package_unique_id(self, value: str) -> str:
        """Converts package identifier to a valid alphanumeric PascalCase SAP CPI uniqueId without underscores."""
        raw = value or "MuleContentPackage"
        parts = re.split(r"[^a-zA-Z0-9]+", raw)
        clean = "".join(p if p.isupper() else (p[:1].upper() + p[1:]) for p in parts if p)
        if not clean:
            clean = "MuleContentPackage"
        if not clean[0].isalpha():
            clean = f"Pkg{clean}"
        clean = clean[:1].upper() + clean[1:]
        return clean

    def _safe_32hex_id(self, value: str) -> str:
        """Returns a stable 32-character hex ID."""
        return hashlib.md5(value.encode("utf-8")).hexdigest()


def create_content_package_archive(
    files: list[GeneratedFile],
    package_id: str = "mule_cpi_pkg",
    package_name: str = "MuleSoft CPI Migration",
    version: str = "1.0.0",
    description: str = "Migrated from MuleSoft via Tissa Intelli-Migrate",
    short_text: str = "MuleSoft migrated integration package",
) -> bytes:
    """Convenience function to generate a full SAP CPI Content Package ZIP."""
    generator = CPIPackageGenerator()
    return generator.create_zip_archive(
        files=files,
        package_id=package_id,
        package_name=package_name,
        export_type="package",
        version=version,
    )


def create_individual_iflow_archive(
    files: list[GeneratedFile],
    artifact_id: str = "mule_cpi_flow",
    artifact_name: str = "MuleSoft CPI Flow",
    version: str = "1.0.0",
) -> bytes:
    """Convenience function to generate a single Integration Flow ZIP."""
    generator = CPIPackageGenerator()
    return generator.create_zip_archive(
        files=files,
        package_id=artifact_id,
        package_name=artifact_name,
        export_type="iflow",
        version=version,
    )
