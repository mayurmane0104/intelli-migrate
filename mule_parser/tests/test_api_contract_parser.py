from __future__ import annotations

from pathlib import Path

from mule_parser.models.schemas import Flow
from mule_parser.parsers.api_contract_parser import parse_api_contract


def _write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_includes_libraries_traits_resource_types_and_security(tmp_path: Path):
    xml = _write(
        tmp_path / "src" / "main" / "mule" / "api.xml",
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:apikit="http://www.mulesoft.org/schema/mule/apikit"
      xmlns="http://www.mulesoft.org/schema/mule/core">
  <apikit:config name="api" raml="api/fsc-integrations.raml" />
  <flow name="get:/customers"/>
</mule>""",
    )
    _write(
        tmp_path / "api" / "libraries" / "common.raml",
        """#%RAML 1.0 Library
traits:
  paged:
    queryParameters:
      limit:
        type: integer
resourceTypes:
  collection:
    get:
      is: [ paged ]
securitySchemes:
  oauth_2_0:
    type: OAuth 2.0
types:
  Customer:
    type: object
    properties:
      id: string
      name?: string
""",
    )
    _write(
        tmp_path / "api" / "fsc-integrations.raml",
        """#%RAML 1.0
title: FSC API
version: v1
baseUri: /api/v1
mediaType: [ application/json ]
uses:
  common: libraries/common.raml
/customers:
  get:
    is: [ common.paged ]
    securedBy: [ common.oauth_2_0 ]
    responses:
      200:
        body:
          application/json:
            type: common.Customer[]
""",
    )
    flows = [Flow(name="get:/customers", file=str(xml))]
    api = parse_api_contract(tmp_path, [xml], flows)
    assert api["apis"][0]["title"] == "FSC API"
    assert api["stats"]["apis"] == 1
    assert api["traits"]
    assert api["resource_types"]
    assert api["security_schemes"]


def test_params_responses_unions_arrays_and_mapping(tmp_path: Path):
    xml = _write(
        tmp_path / "src" / "main" / "mule" / "api.xml",
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:apikit="http://www.mulesoft.org/schema/mule/apikit"
      xmlns="http://www.mulesoft.org/schema/mule/core">
  <apikit:config name="api" raml="api/api.raml" />
  <flow name="post:/orders"/>
</mule>""",
    )
    _write(
        tmp_path / "api" / "api.raml",
        """#%RAML 1.0
title: Orders API
types:
  OrderItem:
    type: object
    properties:
      sku: string
  Order:
    type: OrderItem[] | string
/orders/{id}:
  post:
    uriParameters:
      id:
        type: string
        required: true
    queryParameters:
      dryRun:
        type: boolean
        default: false
    responses:
      400:
        body:
          application/json:
            type: string
""",
    )
    flows = [Flow(name="post:/orders/{id}", file=str(xml))]
    api = parse_api_contract(tmp_path, [xml], flows)
    ep = api["apis"][0]["endpoints"][0]
    meth = ep["methods"][0]
    assert meth["uri_params"][0]["name"] == "id"
    assert meth["query_params"][0]["name"] == "dryRun"
    assert "400" in meth["responses"]
    assert any(s["kind"] == "union" for s in api["schemas"])
    assert api["flow_links"]


def test_apikit_flow_name_with_config_suffix_is_linked(tmp_path: Path):
    xml = _write(
        tmp_path / "src" / "main" / "mule" / "api.xml",
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:apikit="http://www.mulesoft.org/schema/mule/apikit"
      xmlns="http://www.mulesoft.org/schema/mule/core">
  <apikit:config name="fsc-integrations-config" api="api/fsc-integrations.raml" />
  <flow name="put:\\CurrentAccount\\IssuedDevice\\Request:application\\json:fsc-integrations-config"/>
</mule>""",
    )
    _write(
        tmp_path / "api" / "fsc-integrations.raml",
        """#%RAML 1.0
title: FSC API
/CurrentAccount/IssuedDevice/Request:
  put:
    responses:
      200:
        body:
          application/json:
            type: string
""",
    )
    flows = [Flow(name=r"put:\CurrentAccount\IssuedDevice\Request:application\json:fsc-integrations-config", file=str(xml))]
    api = parse_api_contract(tmp_path, [xml], flows)
    assert api["flow_links"]
    assert api["flow_links"][0]["path"] == "/CurrentAccount/IssuedDevice/Request"
    assert api["flow_links"][0]["method"] == "PUT"


def test_broken_include_and_unmapped_routes(tmp_path: Path):
    xml = _write(
        tmp_path / "src" / "main" / "mule" / "api.xml",
        """<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:apikit="http://www.mulesoft.org/schema/mule/apikit"
      xmlns="http://www.mulesoft.org/schema/mule/core">
  <apikit:config name="api" raml="api/api.raml" />
  <flow name="get:/not-in-raml"/>
</mule>""",
    )
    _write(
        tmp_path / "api" / "api.raml",
        """#%RAML 1.0
title: Broken
uses:
  bad: libraries/missing.raml
/ok:
  get:
    responses:
      200:
        body:
          application/json:
            type: UnknownType
""",
    )
    flows = [Flow(name="get:/not-in-raml", file=str(xml))]
    api = parse_api_contract(tmp_path, [xml], flows)
    assert api["unresolved_includes"]
    assert api["unresolved_types"]
    assert api["orphan_flows"]
    assert api["unmapped_routes"]
