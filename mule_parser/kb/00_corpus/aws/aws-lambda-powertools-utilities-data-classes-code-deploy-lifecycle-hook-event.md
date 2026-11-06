# aws_lambda_powertools.utilities.data_classes.code_deploy_lifecycle_hook_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/code_deploy_lifecycle_hook_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/code_deploy_lifecycle_hook_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.code_deploy_lifecycle_hook_event`

## Classes

- `class CodeDeployLifecycleHookEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CodeDeployLifecycleHookEvent(DictWrapper): @property def deployment_id(self) -> str: """The unique ID of the calling CodeDeploy Deployment.""" return self["DeploymentId"] @property def lifecycle_event_hook_execution_id(self) -> str: """The unique ID of a deployments lifecycle hook.""" return self["LifecycleEventHookExecutionId"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop deployment_id : str`
- 
## Expand source code`@property def deployment_id(self) -> str: """The unique ID of the calling CodeDeploy Deployment.""" return self["DeploymentId"]`The unique ID of the calling CodeDeploy Deployment. 
- `prop lifecycle_event_hook_execution_id : str`
- 
## Expand source code`@property def lifecycle_event_hook_execution_id(self) -> str: """The unique ID of a deployments lifecycle hook.""" return self["LifecycleEventHookExecutionId"]`The unique ID of a deployments lifecycle hook. 
 ### Inherited members