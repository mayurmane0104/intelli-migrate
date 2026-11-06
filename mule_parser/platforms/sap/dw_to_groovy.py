"""
mule_parser/platforms/sap/dw_to_groovy.py  –  DataWeave 2.0 to SAP CPI Apache Groovy Translator.

Translates MuleSoft DataWeave expressions and mappings into standard SAP Cloud Integration
Groovy scripts operating on `com.sap.gateway.ip.core.customdev.util.Message`.
"""
from __future__ import annotations

import re
from typing import Any


class DataWeaveToGroovyTranslator:
    """
    Translates DataWeave 2.0 transformations to SAP CPI-compliant Groovy scripts.
    """

    GROOVY_WRAPPER_TEMPLATE = """package src.main.resources.script

import com.sap.gateway.ip.core.customdev.util.Message
import groovy.json.JsonSlurper
import groovy.json.JsonOutput
import groovy.xml.XmlSlurper
import groovy.xml.XmlUtil
import java.util.UUID
import java.text.SimpleDateFormat

/**
 * SAP Cloud Integration script translated from DataWeave transformation: {transform_name}
 */
def Message processData(Message message) {{
    // Access headers and properties
    def headers = message.getHeaders()
    def properties = message.getProperties()
    
    // Parse input body
    def rawBody = message.getBody(String)
    def payload = null
    if (rawBody != null && rawBody.trim().length() > 0) {{
        String trimmed = rawBody.trim()
        if (trimmed.startsWith("<")) {{
            try {{
                payload = new XmlSlurper().parseText(trimmed)
            }} catch (Exception e) {{
                payload = trimmed
            }}
        }} else {{
            try {{
                payload = new JsonSlurper().parseText(trimmed)
            }} catch (Exception e) {{
                payload = trimmed
            }}
        }}
    }}

    // --- Translated Business Logic ---
{translated_body}
    // ---------------------------------

    // Set updated body
    if (result != null) {{
        if (result instanceof groovy.util.slurpersupport.GPathResult || result instanceof groovy.util.Node) {{
            message.setBody(XmlUtil.serialize(result))
            message.setHeader("Content-Type", "application/xml")
        }} else if (result instanceof Map || result instanceof List) {{
            message.setBody(JsonOutput.toJson(result))
            message.setHeader("Content-Type", "application/json")
        }} else {{
            message.setBody(result.toString())
        }}
    }}
    return message
}}
"""

    def __init__(self) -> None:
        pass

    def translate(self, dw_script: str, transform_name: str = "transform") -> str:
        """
        Translates a DataWeave 2.0 script into an executable Groovy script.
        """
        clean_script = self._clean_dw_headers(dw_script)
        groovy_logic = self._convert_expressions(clean_script)
        
        # Indent lines for the template
        indented_lines = ["    " + line for line in groovy_logic.splitlines()]
        translated_body = "\n".join(indented_lines)

        return self.GROOVY_WRAPPER_TEMPLATE.format(
            transform_name=transform_name,
            translated_body=translated_body,
        )

    def _clean_dw_headers(self, script: str) -> str:
        """Strips %dw 2.0 and output directives."""
        if not script:
            return ""
        # Remove directives like %dw 2.0, output application/json, etc.
        lines = []
        body_started = False
        for line in script.splitlines():
            stripped = line.strip()
            if stripped == "---":
                body_started = True
                continue
            if not body_started:
                if stripped.startswith("%dw") or stripped.startswith("output "):
                    continue
                if stripped.startswith("var ") or stripped.startswith("fun "):
                    lines.append(line)
                    continue
            else:
                lines.append(line)
        return "\n".join(lines).strip()

    def _convert_expressions(self, script: str) -> str:
        """Performs lexical and structural translation from DW to Groovy."""
        if not script:
            return "    def result = payload"

        s = script

        # 0. Handle DataWeave if-else expressions: if (cond) val1 else val2 => (cond) ? val1 : val2
        s = re.sub(
            r'\bif\s*\((.*?)\)\s*(.*?)\s+else\s+(.*)',
            r'(\1) ? (\2) : (\3)',
            s,
            flags=re.DOTALL,
        )

        # 0a. Handle startsWith and contains operators
        s = re.sub(
            r'([a-zA-Z0-9_.\?]+)\s+startsWith\s+("[^"]*"|\'[^\']*\')',
            r'\1?.startsWith(\2)',
            s,
        )
        s = re.sub(
            r'([a-zA-Z0-9_.\?]+)\s+contains\s+("[^"]*"|\'[^\']*\')',
            r'\1?.contains(\2)',
            s,
        )

        # 0b. Handle DataWeave string slicing: val[0 to N] => val?.take(N + 1)
        s = re.sub(
            r'([a-zA-Z0-9_.\?]+)\[0\s+to\s+([0-9]+)\]',
            r'(\1 != null && (\1).length() > \2 ? (\1).substring(0, \2 + 1) : \1)',
            s,
        )

        # 0c. Handle context-based filters: filter ($.Code == 'XX') or filter ((x) -> x.Code == 'XX')
        s = re.sub(
            r'\bfilter\s*\(\s*\$\.([a-zA-Z0-9_.]+)\s*==\s*([^\)]+)\)',
            r'.findAll { it?.\1 == \2 }',
            s,
        )
        s = re.sub(
            r'\bfilter\s*\(\s*\(\s*([a-zA-Z0-9_]+)\s*\)\s*->\s*\1\.([a-zA-Z0-9_.]+)\s*==\s*([^\)]+)\)',
            r'.findAll { \1 -> \1?.\2 == \3 }',
            s,
        )

        # 1. Handle map operator
        # payload map ((item, index) -> { ... }) => payload.collect { item, index -> ... }
        s = re.sub(r'payload\s+map\s*\(\s*\(\s*([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)\s*\)\s*->', r'payload?.collect { \1, \2 ->', s)
        s = re.sub(r'payload\s+map\s*\(\s*([a-zA-Z0-9_]+)\s*->', r'payload?.collect { \1 ->', s)
        s = re.sub(r'\bmap\s*\(\s*\(\s*([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)\s*\)\s*->', r'.collect { \1, \2 ->', s)
        s = re.sub(r'\bmap\s*\(\s*([a-zA-Z0-9_]+)\s*->', r'.collect { \1 ->', s)

        # 2. Handle filter operator
        s = re.sub(r'\bfilter\s*\(\s*([a-zA-Z0-9_]+)\s*->', r'.findAll { \1 ->', s)

        # 3. Handle default keyword => Groovy Elvis operator ?:
        s = re.sub(r'\s+default\s+', r' ?: ', s)

        # 4. Handle concatenation ++ => +
        s = s.replace("++", "+")

        # 5. Handle vars.x => properties.get("x")
        s = re.sub(r'\bvars\.([a-zA-Z0-9_]+)\b', r'properties.get("\1")', s)

        # 6. Handle p('property.key') => properties.get("property.key")
        s = re.sub(r'\bp\([\'"]([^\'"]+)[\'"]\)', r'properties.get("\1")', s)

        # 7. Handle sizeOf(x) => x?.size()
        s = re.sub(r'\bsizeOf\(([^)]+)\)', r'(\1)?.size()', s)

        # 8. Handle upper(x), lower(x)
        s = re.sub(r'\bupper\(([^)]+)\)', r'(\1)?.toUpperCase()', s)
        s = re.sub(r'\blower\(([^)]+)\)', r'(\1)?.toLowerCase()', s)

        # 9. Handle now() => new Date()
        s = s.replace("now()", "new Date()")

        # If s looks like an object literal { key: val, ... }, convert to Groovy map [ key: val ]
        trimmed = s.strip()
        if trimmed.startswith("{") and trimmed.endswith("}"):
            # Replace outermost braces with brackets
            inner = trimmed[1:-1]
            s = "[" + inner + "]"

        return f"def result = {s}"
