# aws_lambda_powertools.utilities.data_classes.vpc_lattice API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/vpc_lattice.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/vpc_lattice.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.vpc_lattice`

## Classes

- `class VPCLatticeEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class VPCLatticeEvent(VPCLatticeEventBase): @property def raw_path(self) -> str: """The raw VPC Lattice request path.""" return self["raw_path"] @property def is_base64_encoded(self) -> bool: """A boolean flag to indicate if the applicable request payload is Base64-encode""" return self["is_base64_encoded"] # VPCLattice event has no path field # Added here for consistency with the BaseProxyEvent class @property def path(self) -> str: return self["raw_path"] @property def query_string_parameters(self) -> dict[str, str]: """The request query string parameters.""" return self["query_string_parameters"] @cached_property def resolved_headers_field(self) -> dict[str, Any]: return CaseInsensitiveDict((k, v.split(",") if "," in v else v) for k, v in self.headers.items())`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [VPCLatticeEventBase](#aws_lambda_powertools.utilities.data_classes.vpc_lattice.VPCLatticeEventBase)
- [BaseProxyEvent](common.html#aws_lambda_powertools.utilities.data_classes.common.BaseProxyEvent)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop is_base64_encoded : bool`
- 
## Expand source code`@property def is_base64_encoded(self) -> bool: """A boolean flag to indicate if the applicable request payload is Base64-encode""" return self["is_base64_encoded"]`A boolean flag to indicate if the applicable request payload is Base64-encode 
- `prop path : str`
- 
## Expand source code`@property def path(self) -> str: return self["raw_path"]`
- `prop query_string_parameters : dict[str, str]`
- 
## Expand source code`@property def query_string_parameters(self) -> dict[str, str]: """The request query string parameters.""" return self["query_string_parameters"]`The request query string parameters. 
- `prop raw_path : str`
- 
## Expand source code`@property def raw_path(self) -> str: """The raw VPC Lattice request path.""" return self["raw_path"]`The raw VPC Lattice request path. 
 ### Inherited members
- `class VPCLatticeEventBase (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class VPCLatticeEventBase(BaseProxyEvent): @property def body(self) -> str: """The VPC Lattice body.""" return self["body"] @cached_property def json_body(self) -> Any: """Parses the submitted body as json""" return self._json_deserializer(self.decoded_body) @property def headers(self) -> dict[str, str]: """The VPC Lattice event headers.""" return CaseInsensitiveDict(self["headers"]) @property def decoded_body(self) -> str: """Dynamically base64 decode body as a str""" body: str = self["body"] return base64_decode(body) if self.is_base64_encoded else body @property def method(self) -> str: """The VPC Lattice method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT.""" return self["method"] @property def http_method(self) -> str: """The HTTP method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT.""" return self["method"] def header_serializer(self) -> BaseHeadersSerializer: # When using the VPC Lattice integration, we have multiple HTTP Headers. return HttpApiHeadersSerializer()`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [BaseProxyEvent](common.html#aws_lambda_powertools.utilities.data_classes.common.BaseProxyEvent)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Subclasses### Instance variables- `prop body : str`
- 
## Expand source code`@property def body(self) -> str: """The VPC Lattice body.""" return self["body"]`The VPC Lattice body. 
- `prop decoded_body : str`
- 
## Expand source code`@property def decoded_body(self) -> str: """Dynamically base64 decode body as a str""" body: str = self["body"] return base64_decode(body) if self.is_base64_encoded else body`Dynamically base64 decode body as a str 
- `prop headers : dict[str, str]`
- 
## Expand source code`@property def headers(self) -> dict[str, str]: """The VPC Lattice event headers.""" return CaseInsensitiveDict(self["headers"])`The VPC Lattice event headers. 
- `prop method : str`
- 
## Expand source code`@property def method(self) -> str: """The VPC Lattice method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT.""" return self["method"]`The VPC Lattice method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT. 
 ### Methods- `def header_serializer(self) ‑>`- [BaseHeadersSerializer](../../shared/headers_serializer.html#aws_lambda_powertools.shared.headers_serializer.BaseHeadersSerializer)
- 
## Expand source code`def header_serializer(self) -> BaseHeadersSerializer: # When using the VPC Lattice integration, we have multiple HTTP Headers. return HttpApiHeadersSerializer()`
 ### Inherited members
- `class VPCLatticeEventV2 (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class VPCLatticeEventV2(VPCLatticeEventBase): @property def version(self) -> str: """The VPC Lattice v2 Event version""" return self["version"] @property def is_base64_encoded(self) -> bool | None: """A boolean flag to indicate if the applicable request payload is Base64-encode""" return self.get("isBase64Encoded") @property def path(self) -> str: """The VPC Lattice v2 Event path""" return self["path"] @property def request_context(self) -> vpcLatticeEventV2RequestContext: """The VPC Lattice v2 Event request context.""" return vpcLatticeEventV2RequestContext(self["requestContext"]) @cached_property def query_string_parameters(self) -> dict[str, str]: """The request query string parameters. For VPC Lattice V2, the queryStringParameters will contain a dict[str, list[str]] so to keep compatibility with existing utilities, we merge all the values with a comma. """ params = self.get("queryStringParameters") or {} return {k: ",".join(v) for k, v in params.items()} @property def resolved_headers_field(self) -> dict[str, str]: if self.headers is not None: return {key.lower(): value for key, value in self.headers.items()} return {}`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [VPCLatticeEventBase](#aws_lambda_powertools.utilities.data_classes.vpc_lattice.VPCLatticeEventBase)
- [BaseProxyEvent](common.html#aws_lambda_powertools.utilities.data_classes.common.BaseProxyEvent)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop is_base64_encoded : bool | None`
- 
## Expand source code`@property def is_base64_encoded(self) -> bool | None: """A boolean flag to indicate if the applicable request payload is Base64-encode""" return self.get("isBase64Encoded")`A boolean flag to indicate if the applicable request payload is Base64-encode 
- `prop path : str`
- 
## Expand source code`@property def path(self) -> str: """The VPC Lattice v2 Event path""" return self["path"]`The VPC Lattice v2 Event path 
- `var query_string_parameters : dict[str, str]`
- 
## Expand source code`@cached_property def query_string_parameters(self) -> dict[str, str]: """The request query string parameters. For VPC Lattice V2, the queryStringParameters will contain a dict[str, list[str]] so to keep compatibility with existing utilities, we merge all the values with a comma. """ params = self.get("queryStringParameters") or {} return {k: ",".join(v) for k, v in params.items()}`The request query string parameters. For VPC Lattice V2, the queryStringParameters will contain a dict[str, list[str]] so to keep compatibility with existing utilities, we merge all the values with a comma. 
- `prop request_context :`- [vpcLatticeEventV2RequestContext](#aws_lambda_powertools.utilities.data_classes.vpc_lattice.vpcLatticeEventV2RequestContext)
- 
## Expand source code`@property def request_context(self) -> vpcLatticeEventV2RequestContext: """The VPC Lattice v2 Event request context.""" return vpcLatticeEventV2RequestContext(self["requestContext"])`The VPC Lattice v2 Event request context. 
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: """The VPC Lattice v2 Event version""" return self["version"]`The VPC Lattice v2 Event version 
 ### Inherited members
- `class vpcLatticeEventV2Identity (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class vpcLatticeEventV2Identity(DictWrapper): @property def source_vpc_arn(self) -> str | None: """The VPC Lattice v2 Event requestContext Identity sourceVpcArn""" return self.get("sourceVpcArn") @property def get_type(self) -> str | None: """The VPC Lattice v2 Event requestContext Identity type""" return self.get("type") @property def principal(self) -> str | None: """The VPC Lattice v2 Event requestContext principal""" return self.get("principal") @property def principal_org_id(self) -> str | None: """The VPC Lattice v2 Event requestContext principalOrgID""" return self.get("principalOrgID") @property def session_name(self) -> str | None: """The VPC Lattice v2 Event requestContext sessionName""" return self.get("sessionName") @property def x509_subject_cn(self) -> str | None: """The VPC Lattice v2 Event requestContext X509SubjectCn""" return self.get("X509SubjectCn") @property def x509_issuer_ou(self) -> str | None: """The VPC Lattice v2 Event requestContext X509IssuerOu""" return self.get("X509IssuerOu") @property def x509_san_dns(self) -> str | None: """The VPC Lattice v2 Event requestContext X509SanDns""" return self.get("x509SanDns") @property def x509_san_uri(self) -> str | None: """The VPC Lattice v2 Event requestContext X509SanUri""" return self.get("X509SanUri") @property def x509_san_name_cn(self) -> str | None: """The VPC Lattice v2 Event requestContext X509SanNameCn""" return self.get("X509SanNameCn")`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop get_type : str | None`
- 
## Expand source code`@property def get_type(self) -> str | None: """The VPC Lattice v2 Event requestContext Identity type""" return self.get("type")`The VPC Lattice v2 Event requestContext Identity type 
- `prop principal : str | None`
- 
## Expand source code`@property def principal(self) -> str | None: """The VPC Lattice v2 Event requestContext principal""" return self.get("principal")`The VPC Lattice v2 Event requestContext principal 
- `prop principal_org_id : str | None`
- 
## Expand source code`@property def principal_org_id(self) -> str | None: """The VPC Lattice v2 Event requestContext principalOrgID""" return self.get("principalOrgID")`The VPC Lattice v2 Event requestContext principalOrgID 
- `prop session_name : str | None`
- 
## Expand source code`@property def session_name(self) -> str | None: """The VPC Lattice v2 Event requestContext sessionName""" return self.get("sessionName")`The VPC Lattice v2 Event requestContext sessionName 
- `prop source_vpc_arn : str | None`
- 
## Expand source code`@property def source_vpc_arn(self) -> str | None: """The VPC Lattice v2 Event requestContext Identity sourceVpcArn""" return self.get("sourceVpcArn")`The VPC Lattice v2 Event requestContext Identity sourceVpcArn 
- `prop x509_issuer_ou : str | None`
- 
## Expand source code`@property def x509_issuer_ou(self) -> str | None: """The VPC Lattice v2 Event requestContext X509IssuerOu""" return self.get("X509IssuerOu")`The VPC Lattice v2 Event requestContext X509IssuerOu 
- `prop x509_san_dns : str | None`
- 
## Expand source code`@property def x509_san_dns(self) -> str | None: """The VPC Lattice v2 Event requestContext X509SanDns""" return self.get("x509SanDns")`The VPC Lattice v2 Event requestContext X509SanDns 
- `prop x509_san_name_cn : str | None`
- 
## Expand source code`@property def x509_san_name_cn(self) -> str | None: """The VPC Lattice v2 Event requestContext X509SanNameCn""" return self.get("X509SanNameCn")`The VPC Lattice v2 Event requestContext X509SanNameCn 
- `prop x509_san_uri : str | None`
- 
## Expand source code`@property def x509_san_uri(self) -> str | None: """The VPC Lattice v2 Event requestContext X509SanUri""" return self.get("X509SanUri")`The VPC Lattice v2 Event requestContext X509SanUri 
- `prop x509_subject_cn : str | None`
- 
## Expand source code`@property def x509_subject_cn(self) -> str | None: """The VPC Lattice v2 Event requestContext X509SubjectCn""" return self.get("X509SubjectCn")`The VPC Lattice v2 Event requestContext X509SubjectCn 
 ### Inherited members
- `class vpcLatticeEventV2RequestContext (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class vpcLatticeEventV2RequestContext(DictWrapper): @property def service_network_arn(self) -> str: """The VPC Lattice v2 Event requestContext serviceNetworkArn""" return self["serviceNetworkArn"] @property def service_arn(self) -> str: """The VPC Lattice v2 Event requestContext serviceArn""" return self["serviceArn"] @property def target_group_arn(self) -> str: """The VPC Lattice v2 Event requestContext targetGroupArn""" return self["targetGroupArn"] @property def identity(self) -> vpcLatticeEventV2Identity: """The VPC Lattice v2 Event requestContext identity""" return vpcLatticeEventV2Identity(self["identity"]) @property def region(self) -> str: """The VPC Lattice v2 Event requestContext serviceNetworkArn""" return self["region"] @property def time_epoch(self) -> float: """The VPC Lattice v2 Event requestContext timeEpoch""" return self["timeEpoch"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop identity :`- [vpcLatticeEventV2Identity](#aws_lambda_powertools.utilities.data_classes.vpc_lattice.vpcLatticeEventV2Identity)
- 
## Expand source code`@property def identity(self) -> vpcLatticeEventV2Identity: """The VPC Lattice v2 Event requestContext identity""" return vpcLatticeEventV2Identity(self["identity"])`The VPC Lattice v2 Event requestContext identity 
- `prop region : str`
- 
## Expand source code`@property def region(self) -> str: """The VPC Lattice v2 Event requestContext serviceNetworkArn""" return self["region"]`The VPC Lattice v2 Event requestContext serviceNetworkArn 
- `prop service_arn : str`
- 
## Expand source code`@property def service_arn(self) -> str: """The VPC Lattice v2 Event requestContext serviceArn""" return self["serviceArn"]`The VPC Lattice v2 Event requestContext serviceArn 
- `prop service_network_arn : str`
- 
## Expand source code`@property def service_network_arn(self) -> str: """The VPC Lattice v2 Event requestContext serviceNetworkArn""" return self["serviceNetworkArn"]`The VPC Lattice v2 Event requestContext serviceNetworkArn 
- `prop target_group_arn : str`
- 
## Expand source code`@property def target_group_arn(self) -> str: """The VPC Lattice v2 Event requestContext targetGroupArn""" return self["targetGroupArn"]`The VPC Lattice v2 Event requestContext targetGroupArn 
- `prop time_epoch : float`
- 
## Expand source code`@property def time_epoch(self) -> float: """The VPC Lattice v2 Event requestContext timeEpoch""" return self["timeEpoch"]`The VPC Lattice v2 Event requestContext timeEpoch 
 ### Inherited members