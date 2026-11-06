# aws_lambda_powertools.utilities.data_classes.cloudformation_custom_resource_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/cloudformation_custom_resource_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/cloudformation_custom_resource_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.cloudformation_custom_resource_event`

## Classes

- `class CloudFormationCustomResourceEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudFormationCustomResourceEvent(DictWrapper): @property def request_type(self) -> Literal["Create", "Update", "Delete"]: return self["RequestType"] @property def service_token(self) -> str: return self["ServiceToken"] @property def response_url(self) -> str: return self["ResponseURL"] @property def stack_id(self) -> str: return self["StackId"] @property def request_id(self) -> str: return self["RequestId"] @property def logical_resource_id(self) -> str: return self["LogicalResourceId"] @property def physical_resource_id(self) -> str: return self.get("PhysicalResourceId") or "" @property def resource_type(self) -> str: return self["ResourceType"] @property def resource_properties(self) -> dict[str, Any]: return self.get("ResourceProperties") or {} @property def old_resource_properties(self) -> dict[str, Any]: return self.get("OldResourceProperties") or {}`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop logical_resource_id : str`
- 
## Expand source code`@property def logical_resource_id(self) -> str: return self["LogicalResourceId"]`
- `prop old_resource_properties : dict[str, Any]`
- 
## Expand source code`@property def old_resource_properties(self) -> dict[str, Any]: return self.get("OldResourceProperties") or {}`
- `prop physical_resource_id : str`
- 
## Expand source code`@property def physical_resource_id(self) -> str: return self.get("PhysicalResourceId") or ""`
- `prop request_id : str`
- 
## Expand source code`@property def request_id(self) -> str: return self["RequestId"]`
- `prop request_type : Literal['Create', 'Update', 'Delete']`
- 
## Expand source code`@property def request_type(self) -> Literal["Create", "Update", "Delete"]: return self["RequestType"]`
- `prop resource_properties : dict[str, Any]`
- 
## Expand source code`@property def resource_properties(self) -> dict[str, Any]: return self.get("ResourceProperties") or {}`
- `prop resource_type : str`
- 
## Expand source code`@property def resource_type(self) -> str: return self["ResourceType"]`
- `prop response_url : str`
- 
## Expand source code`@property def response_url(self) -> str: return self["ResponseURL"]`
- `prop service_token : str`
- 
## Expand source code`@property def service_token(self) -> str: return self["ServiceToken"]`
- `prop stack_id : str`
- 
## Expand source code`@property def stack_id(self) -> str: return self["StackId"]`
 ### Inherited members