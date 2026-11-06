from __future__ import annotations

from pathlib import Path

from mule_parser.parsers.observability_extractor import extract_logger_registry


def test_log4j2_parsing_async_rolling_and_sinks(tmp_path: Path):
    log4j = tmp_path / "log4j2.xml"
    log4j.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
  <Appenders>
    <RollingFile name="RollingFile" fileName="logs/app.log" filePattern="logs/app-%d{yyyy-MM-dd}-%i.log.gz">
      <PatternLayout pattern="%d %t %X{correlationId} %msg%n"/>
      <Policies>
        <SizeBasedTriggeringPolicy size="10MB"/>
        <TimeBasedTriggeringPolicy interval="1"/>
      </Policies>
      <DefaultRolloverStrategy max="7"/>
    </RollingFile>
    <Async name="AsyncAppender">
      <AppenderRef ref="RollingFile"/>
    </Async>
    <Socket name="SplunkSocket" host="splunk.local" port="514"/>
  </Appenders>
  <Loggers>
    <AsyncLogger name="com.app" level="INFO" additivity="false">
      <AppenderRef ref="AsyncAppender"/>
    </AsyncLogger>
    <Root level="DEBUG">
      <AppenderRef ref="RollingFile"/>
    </Root>
  </Loggers>
</Configuration>""",
        encoding="utf-8",
    )

    raw = {
        "logging": [{"file": "log4j2.xml"}],
        "file_registry": {
            "files": [
                {
                    "path": str(log4j),
                    "normalized_path": "log4j2.xml",
                    "source": "filesystem",
                    "archive_path": str(tmp_path),
                }
            ]
        },
        "flow_execution_plans": [],
    }
    reg = extract_logger_registry(raw)
    assert reg["appenders"]
    assert any(a["type"] == "RollingFile" for a in reg["appenders"])
    assert reg["async"]["async_enabled"] is True
    assert reg["async"]["async_mode"] in {"AsyncAppender", "AsyncLogger"}
    assert reg["rotation_policies"]
    assert reg["sinks"]
    assert any(l["logger"] == "root" and l["level"].upper() == "DEBUG" for l in reg["loggers"])
    assert reg["observability"]["structured_logging"] is False
    assert reg["observability"]["external_sink"] is True
    assert any(r["type"] == "LOGGING_RISK" for r in reg["risks"])


def test_log4j2_json_layout_and_flow_linkage(tmp_path: Path):
    log4j = tmp_path / "log4j2-test.xml"
    log4j.write_text(
        """<Configuration>
  <Appenders>
    <Console name="Console">
      <JsonLayout complete="false" compact="true"/>
    </Console>
  </Appenders>
  <Loggers>
    <Logger name="com.app.api" level="INFO" additivity="false">
      <AppenderRef ref="Console"/>
    </Logger>
    <Root level="INFO"><AppenderRef ref="Console"/></Root>
  </Loggers>
</Configuration>""",
        encoding="utf-8",
    )
    raw = {
        "logging": [{"file": "log4j2-test.xml"}],
        "file_registry": {
            "files": [
                {
                    "path": str(log4j),
                    "normalized_path": "log4j2-test.xml",
                    "source": "filesystem",
                    "archive_path": str(tmp_path),
                }
            ]
        },
        "flow_execution_plans": [
            {
                "flow_name": "f1",
                "steps": [
                    {"step_id": "s1", "type": "logger", "attributes": {"level": "INFO", "message": "cid=#[vars.correlationId]"}},
                ],
            }
        ],
    }
    reg = extract_logger_registry(raw)
    assert reg["observability"]["structured_logging"] is True
    assert reg["flow_linkage"]["entries"]
    assert reg["flow_linkage"]["flows_with_correlation"] == ["f1"]


def test_log4j2_malformed_xml_warning(tmp_path: Path):
    bad = tmp_path / "log4j2.xml"
    bad.write_text("<Configuration><Appenders><Console></Configuration>", encoding="utf-8")
    raw = {
        "logging": [{"file": "log4j2.xml"}],
        "file_registry": {
            "files": [
                {
                    "path": str(bad),
                    "normalized_path": "log4j2.xml",
                    "source": "filesystem",
                    "archive_path": str(tmp_path),
                }
            ]
        },
        "flow_execution_plans": [],
    }
    reg = extract_logger_registry(raw)
    assert any(w["type"] == "LOG4J_CONFIGURATION" for w in reg["warnings"])
