# aws_lambda_powertools.utilities.data_classes.aws_config_rule_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/aws_config_rule_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/aws_config_rule_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.aws_config_rule_event`

## Functions

- `def get_invoke_event(invoking_event: dict) ‑>`- [AWSConfigConfigurationChanged](#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigConfigurationChanged)|- [AWSConfigScheduledNotification](#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigScheduledNotification)|- [AWSConfigOversizedConfiguration](#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigOversizedConfiguration)
- 
## Expand source code`def get_invoke_event( invoking_event: dict, ) -> AWSConfigConfigurationChanged | AWSConfigScheduledNotification | AWSConfigOversizedConfiguration: """ Returns the corresponding event object based on the messageType in the invoking event. Parameters ---------- invoking_event: dict The invoking event received. Returns ------- AWSConfigConfigurationChanged | AWSConfigScheduledNotification | AWSConfigOversizedConfiguration: The event object based on the messageType in the invoking event. """ message_type = invoking_event.get("messageType") if message_type == "ScheduledNotification": return AWSConfigScheduledNotification(invoking_event) if message_type == "OversizedConfigurationItemChangeNotification": return AWSConfigOversizedConfiguration(invoking_event) # Default return is AWSConfigConfigurationChanged event return AWSConfigConfigurationChanged(invoking_event)`Returns the corresponding event object based on the messageType in the invoking event. ## Parameters- `invoking_event`- `dict`
- The invoking event received.
 ## Returns- `AWSConfigConfigurationChanged | AWSConfigScheduledNotification | AWSConfigOversizedConfiguration:`
- The event object based on the messageType in the invoking event.
 

## Classes

- `class AWSConfigConfigurationChanged (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class AWSConfigConfigurationChanged(DictWrapper): @property def configuration_item_diff(self) -> dict: """The configuration item diff of the ConfigurationItemChangeNotification event.""" return self["configurationItemDiff"] @property def configuration_item(self) -> AWSConfigConfigurationItemChanged: """The configuration item of the ConfigurationItemChangeNotification event.""" return AWSConfigConfigurationItemChanged(self["configurationItem"]) @property def raw_configuration_item(self) -> dict: """The raw configuration item of the ConfigurationItemChangeNotification event.""" return self["configurationItem"] @property def record_version(self) -> str: """The record version of the ConfigurationItemChangeNotification event.""" return self["recordVersion"] @property def message_type(self) -> str: """The message type of the ConfigurationItemChangeNotification event.""" return self["messageType"] @property def notification_creation_time(self) -> str: """The notification creation time of the ConfigurationItemChangeNotification event.""" return self["notificationCreationTime"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop configuration_item :`- [AWSConfigConfigurationItemChanged](#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigConfigurationItemChanged)
- 
## Expand source code`@property def configuration_item(self) -> AWSConfigConfigurationItemChanged: """The configuration item of the ConfigurationItemChangeNotification event.""" return AWSConfigConfigurationItemChanged(self["configurationItem"])`The configuration item of the ConfigurationItemChangeNotification event. 
- `prop configuration_item_diff : dict`
- 
## Expand source code`@property def configuration_item_diff(self) -> dict: """The configuration item diff of the ConfigurationItemChangeNotification event.""" return self["configurationItemDiff"]`The configuration item diff of the ConfigurationItemChangeNotification event. 
- `prop message_type : str`
- 
## Expand source code`@property def message_type(self) -> str: """The message type of the ConfigurationItemChangeNotification event.""" return self["messageType"]`The message type of the ConfigurationItemChangeNotification event. 
- `prop notification_creation_time : str`
- 
## Expand source code`@property def notification_creation_time(self) -> str: """The notification creation time of the ConfigurationItemChangeNotification event.""" return self["notificationCreationTime"]`The notification creation time of the ConfigurationItemChangeNotification event. 
- `prop raw_configuration_item : dict`
- 
## Expand source code`@property def raw_configuration_item(self) -> dict: """The raw configuration item of the ConfigurationItemChangeNotification event.""" return self["configurationItem"]`The raw configuration item of the ConfigurationItemChangeNotification event. 
- `prop record_version : str`
- 
## Expand source code`@property def record_version(self) -> str: """The record version of the ConfigurationItemChangeNotification event.""" return self["recordVersion"]`The record version of the ConfigurationItemChangeNotification event. 
 ### Inherited members
- `class AWSConfigConfigurationItemChanged (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class AWSConfigConfigurationItemChanged(DictWrapper): @property def related_events(self) -> list: """The related events of the ConfigurationItemChangeNotification event.""" return self["relatedEvents"] @property def relationships(self) -> list: """The relationships of the ConfigurationItemChangeNotification event.""" return self["relationships"] @property def configuration(self) -> dict: """The configuration of the ConfigurationItemChangeNotification event.""" return self["configuration"] @property def supplementary_configuration(self) -> dict: """The supplementary configuration of the ConfigurationItemChangeNotification event.""" return self["supplementaryConfiguration"] @property def tags(self) -> dict: """The tags of the ConfigurationItemChangeNotification event.""" return self["tags"] @property def configuration_item_version(self) -> str: """The configuration item version of the ConfigurationItemChangeNotification event.""" return self["configurationItemVersion"] @property def configuration_item_capture_time(self) -> str: """The configuration item capture time of the ConfigurationItemChangeNotification event.""" return self["configurationItemCaptureTime"] @property def configuration_state_id(self) -> str: """The configuration state id of the ConfigurationItemChangeNotification event.""" return self["configurationStateId"] @property def accountid(self) -> str: """The accountid of the ConfigurationItemChangeNotification event.""" return self["awsAccountId"] @property def configuration_item_status(self) -> str: """The configuration item status of the ConfigurationItemChangeNotification event.""" return self["configurationItemStatus"] @property def resource_type(self) -> str: """The resource type of the ConfigurationItemChangeNotification event.""" return self["resourceType"] @property def resource_id(self) -> str: """The resource id of the ConfigurationItemChangeNotification event.""" return self["resourceId"] @property def resource_name(self) -> str: """The resource name of the ConfigurationItemChangeNotification event.""" return self["resourceName"] @property def resource_arn(self) -> str: """The resource arn of the ConfigurationItemChangeNotification event.""" return self["ARN"] @property def region(self) -> str: """The region of the ConfigurationItemChangeNotification event.""" return self["awsRegion"] @property def availability_zone(self) -> str: """The availability zone of the ConfigurationItemChangeNotification event.""" return self["availabilityZone"] @property def configuration_state_md5_hash(self) -> str: """The md5 hash of the state of the ConfigurationItemChangeNotification event.""" return self["configurationStateMd5Hash"] @property def resource_creation_time(self) -> str: """The resource creation time of the ConfigurationItemChangeNotification event.""" return self["resourceCreationTime"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop accountid : str`
- 
## Expand source code`@property def accountid(self) -> str: """The accountid of the ConfigurationItemChangeNotification event.""" return self["awsAccountId"]`The accountid of the ConfigurationItemChangeNotification event. 
- `prop availability_zone : str`
- 
## Expand source code`@property def availability_zone(self) -> str: """The availability zone of the ConfigurationItemChangeNotification event.""" return self["availabilityZone"]`The availability zone of the ConfigurationItemChangeNotification event. 
- `prop configuration : dict`
- 
## Expand source code`@property def configuration(self) -> dict: """The configuration of the ConfigurationItemChangeNotification event.""" return self["configuration"]`The configuration of the ConfigurationItemChangeNotification event. 
- `prop configuration_item_capture_time : str`
- 
## Expand source code`@property def configuration_item_capture_time(self) -> str: """The configuration item capture time of the ConfigurationItemChangeNotification event.""" return self["configurationItemCaptureTime"]`The configuration item capture time of the ConfigurationItemChangeNotification event. 
- `prop configuration_item_status : str`
- 
## Expand source code`@property def configuration_item_status(self) -> str: """The configuration item status of the ConfigurationItemChangeNotification event.""" return self["configurationItemStatus"]`The configuration item status of the ConfigurationItemChangeNotification event. 
- `prop configuration_item_version : str`
- 
## Expand source code`@property def configuration_item_version(self) -> str: """The configuration item version of the ConfigurationItemChangeNotification event.""" return self["configurationItemVersion"]`The configuration item version of the ConfigurationItemChangeNotification event. 
- `prop configuration_state_id : str`
- 
## Expand source code`@property def configuration_state_id(self) -> str: """The configuration state id of the ConfigurationItemChangeNotification event.""" return self["configurationStateId"]`The configuration state id of the ConfigurationItemChangeNotification event. 
- `prop configuration_state_md5_hash : str`
- 
## Expand source code`@property def configuration_state_md5_hash(self) -> str: """The md5 hash of the state of the ConfigurationItemChangeNotification event.""" return self["configurationStateMd5Hash"]`The md5 hash of the state of the ConfigurationItemChangeNotification event. 
- `prop region : str`
- 
## Expand source code`@property def region(self) -> str: """The region of the ConfigurationItemChangeNotification event.""" return self["awsRegion"]`The region of the ConfigurationItemChangeNotification event. 
- 
## Expand source code`@property def related_events(self) -> list: """The related events of the ConfigurationItemChangeNotification event.""" return self["relatedEvents"]`The related events of the ConfigurationItemChangeNotification event. 
- `prop relationships : list`
- 
## Expand source code`@property def relationships(self) -> list: """The relationships of the ConfigurationItemChangeNotification event.""" return self["relationships"]`The relationships of the ConfigurationItemChangeNotification event. 
- `prop resource_arn : str`
- 
## Expand source code`@property def resource_arn(self) -> str: """The resource arn of the ConfigurationItemChangeNotification event.""" return self["ARN"]`The resource arn of the ConfigurationItemChangeNotification event. 
- `prop resource_creation_time : str`
- 
## Expand source code`@property def resource_creation_time(self) -> str: """The resource creation time of the ConfigurationItemChangeNotification event.""" return self["resourceCreationTime"]`The resource creation time of the ConfigurationItemChangeNotification event. 
- `prop resource_id : str`
- 
## Expand source code`@property def resource_id(self) -> str: """The resource id of the ConfigurationItemChangeNotification event.""" return self["resourceId"]`The resource id of the ConfigurationItemChangeNotification event. 
- `prop resource_name : str`
- 
## Expand source code`@property def resource_name(self) -> str: """The resource name of the ConfigurationItemChangeNotification event.""" return self["resourceName"]`The resource name of the ConfigurationItemChangeNotification event. 
- `prop resource_type : str`
- 
## Expand source code`@property def resource_type(self) -> str: """The resource type of the ConfigurationItemChangeNotification event.""" return self["resourceType"]`The resource type of the ConfigurationItemChangeNotification event. 
- `prop supplementary_configuration : dict`
- 
## Expand source code`@property def supplementary_configuration(self) -> dict: """The supplementary configuration of the ConfigurationItemChangeNotification event.""" return self["supplementaryConfiguration"]`The supplementary configuration of the ConfigurationItemChangeNotification event. 
- 
## Expand source code`@property def tags(self) -> dict: """The tags of the ConfigurationItemChangeNotification event.""" return self["tags"]`The tags of the ConfigurationItemChangeNotification event. 
 ### Inherited members
- `class AWSConfigOversizedConfiguration (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class AWSConfigOversizedConfiguration(DictWrapper): @property def configuration_item_summary(self) -> AWSConfigOversizedConfigurationItemSummary: """The configuration item summary of the OversizedConfiguration event.""" return AWSConfigOversizedConfigurationItemSummary(self["configurationItemSummary"]) @property def raw_configuration_item_summary(self) -> str: """The raw configuration item summary of the OversizedConfiguration event.""" return self["configurationItemSummary"] @property def message_type(self) -> str: """The message type of the OversizedConfiguration event.""" return self["messageType"] @property def notification_creation_time(self) -> str: """The notification creation time of the OversizedConfiguration event.""" return self["notificationCreationTime"] @property def record_version(self) -> str: """The record version of the OversizedConfiguration event.""" return self["recordVersion"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop configuration_item_summary :`- [AWSConfigOversizedConfigurationItemSummary](#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigOversizedConfigurationItemSummary)
- 
## Expand source code`@property def configuration_item_summary(self) -> AWSConfigOversizedConfigurationItemSummary: """The configuration item summary of the OversizedConfiguration event.""" return AWSConfigOversizedConfigurationItemSummary(self["configurationItemSummary"])`The configuration item summary of the OversizedConfiguration event. 
- `prop message_type : str`
- 
## Expand source code`@property def message_type(self) -> str: """The message type of the OversizedConfiguration event.""" return self["messageType"]`The message type of the OversizedConfiguration event. 
- `prop notification_creation_time : str`
- 
## Expand source code`@property def notification_creation_time(self) -> str: """The notification creation time of the OversizedConfiguration event.""" return self["notificationCreationTime"]`The notification creation time of the OversizedConfiguration event. 
- `prop raw_configuration_item_summary : str`
- 
## Expand source code`@property def raw_configuration_item_summary(self) -> str: """The raw configuration item summary of the OversizedConfiguration event.""" return self["configurationItemSummary"]`The raw configuration item summary of the OversizedConfiguration event. 
- `prop record_version : str`
- 
## Expand source code`@property def record_version(self) -> str: """The record version of the OversizedConfiguration event.""" return self["recordVersion"]`The record version of the OversizedConfiguration event. 
 ### Inherited members
- `class AWSConfigOversizedConfigurationItemSummary (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class AWSConfigOversizedConfigurationItemSummary(DictWrapper): @property def change_type(self) -> str: """The change type of the OversizedConfiguration event.""" return self["changeType"] @property def configuration_item_version(self) -> str: """The configuration item version of the OversizedConfiguration event.""" return self["configurationItemVersion"] @property def configuration_item_capture_time(self) -> str: """The configuration item capture time of the OversizedConfiguration event.""" return self["configurationItemCaptureTime"] @property def configuration_state_id(self) -> str: """The configuration state id of the OversizedConfiguration event.""" return self["configurationStateId"] @property def accountid(self) -> str: """The accountid of the OversizedConfiguration event.""" return self["awsAccountId"] @property def configuration_item_status(self) -> str: """The configuration item status of the OversizedConfiguration event.""" return self["configurationItemStatus"] @property def resource_type(self) -> str: """The resource type of the OversizedConfiguration event.""" return self["resourceType"] @property def resource_id(self) -> str: """The resource id of the OversizedConfiguration event.""" return self["resourceId"] @property def resource_name(self) -> str: """The resource name of the OversizedConfiguration event.""" return self["resourceName"] @property def resource_arn(self) -> str: """The resource arn of the OversizedConfiguration event.""" return self["ARN"] @property def region(self) -> str: """The region of the OversizedConfiguration event.""" return self["awsRegion"] @property def availability_zone(self) -> str: """The availability zone of the OversizedConfiguration event.""" return self["availabilityZone"] @property def configuration_state_md5_hash(self) -> str: """The state md5 hash of the OversizedConfiguration event.""" return self["configurationStateMd5Hash"] @property def resource_creation_time(self) -> str: """The resource creation time of the OversizedConfiguration event.""" return self["resourceCreationTime"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop accountid : str`
- 
## Expand source code`@property def accountid(self) -> str: """The accountid of the OversizedConfiguration event.""" return self["awsAccountId"]`The accountid of the OversizedConfiguration event. 
- `prop availability_zone : str`
- 
## Expand source code`@property def availability_zone(self) -> str: """The availability zone of the OversizedConfiguration event.""" return self["availabilityZone"]`The availability zone of the OversizedConfiguration event. 
- `prop change_type : str`
- 
## Expand source code`@property def change_type(self) -> str: """The change type of the OversizedConfiguration event.""" return self["changeType"]`The change type of the OversizedConfiguration event. 
- `prop configuration_item_capture_time : str`
- 
## Expand source code`@property def configuration_item_capture_time(self) -> str: """The configuration item capture time of the OversizedConfiguration event.""" return self["configurationItemCaptureTime"]`The configuration item capture time of the OversizedConfiguration event. 
- `prop configuration_item_status : str`
- 
## Expand source code`@property def configuration_item_status(self) -> str: """The configuration item status of the OversizedConfiguration event.""" return self["configurationItemStatus"]`The configuration item status of the OversizedConfiguration event. 
- `prop configuration_item_version : str`
- 
## Expand source code`@property def configuration_item_version(self) -> str: """The configuration item version of the OversizedConfiguration event.""" return self["configurationItemVersion"]`The configuration item version of the OversizedConfiguration event. 
- `prop configuration_state_id : str`
- 
## Expand source code`@property def configuration_state_id(self) -> str: """The configuration state id of the OversizedConfiguration event.""" return self["configurationStateId"]`The configuration state id of the OversizedConfiguration event. 
- `prop configuration_state_md5_hash : str`
- 
## Expand source code`@property def configuration_state_md5_hash(self) -> str: """The state md5 hash of the OversizedConfiguration event.""" return self["configurationStateMd5Hash"]`The state md5 hash of the OversizedConfiguration event. 
- `prop region : str`
- 
## Expand source code`@property def region(self) -> str: """The region of the OversizedConfiguration event.""" return self["awsRegion"]`The region of the OversizedConfiguration event. 
- `prop resource_arn : str`
- 
## Expand source code`@property def resource_arn(self) -> str: """The resource arn of the OversizedConfiguration event.""" return self["ARN"]`The resource arn of the OversizedConfiguration event. 
- `prop resource_creation_time : str`
- 
## Expand source code`@property def resource_creation_time(self) -> str: """The resource creation time of the OversizedConfiguration event.""" return self["resourceCreationTime"]`The resource creation time of the OversizedConfiguration event. 
- `prop resource_id : str`
- 
## Expand source code`@property def resource_id(self) -> str: """The resource id of the OversizedConfiguration event.""" return self["resourceId"]`The resource id of the OversizedConfiguration event. 
- `prop resource_name : str`
- 
## Expand source code`@property def resource_name(self) -> str: """The resource name of the OversizedConfiguration event.""" return self["resourceName"]`The resource name of the OversizedConfiguration event. 
- `prop resource_type : str`
- 
## Expand source code`@property def resource_type(self) -> str: """The resource type of the OversizedConfiguration event.""" return self["resourceType"]`The resource type of the OversizedConfiguration event. 
 ### Inherited members
- `class AWSConfigRuleEvent (data: dict[str, Any])`
- 
## Expand source code`class AWSConfigRuleEvent(DictWrapper): """Events for AWS Config Rules Documentation: -------------- - https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_lambda-functions.html """ def __init__(self, data: dict[str, Any]): super().__init__(data) self._invoking_event: Any | None = None self._rule_parameters: Any | None = None @property def version(self) -> str: """The version of the event.""" return self["version"] @property def invoking_event( self, ) -> AWSConfigConfigurationChanged | AWSConfigScheduledNotification | AWSConfigOversizedConfiguration: """The invoking payload of the event.""" if self._invoking_event is None: self._invoking_event = self._json_deserializer(self["invokingEvent"]) return get_invoke_event(self._invoking_event) @property def raw_invoking_event(self) -> str: """The raw invoking payload of the event.""" return self["invokingEvent"] @property def rule_parameters(self) -> dict: """The parameters of the event.""" if self._rule_parameters is None: self._rule_parameters = self._json_deserializer(self["ruleParameters"]) return self._rule_parameters @property def result_token(self) -> str: """The result token of the event.""" return self["resultToken"] @property def event_left_scope(self) -> bool: """The left scope of the event.""" return self["eventLeftScope"] @property def execution_role_arn(self) -> str: """The execution role arn of the event.""" return self["executionRoleArn"] @property def config_rule_arn(self) -> str: """The arn of the rule of the event.""" return self["configRuleArn"] @property def config_rule_name(self) -> str: """The name of the rule of the event.""" return self["configRuleName"] @property def config_rule_id(self) -> str: """The id of the rule of the event.""" return self["configRuleId"] @property def accountid(self) -> str: """The accountid of the event.""" return self["accountId"] @property def evalution_mode(self) -> str | None: """The evalution mode of the event.""" return self.get("evaluationMode")`Events for AWS Config Rules Documentation: 
 ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop accountid : str`
- 
## Expand source code`@property def accountid(self) -> str: """The accountid of the event.""" return self["accountId"]`The accountid of the event. 
- `prop config_rule_arn : str`
- 
## Expand source code`@property def config_rule_arn(self) -> str: """The arn of the rule of the event.""" return self["configRuleArn"]`The arn of the rule of the event. 
- `prop config_rule_id : str`
- 
## Expand source code`@property def config_rule_id(self) -> str: """The id of the rule of the event.""" return self["configRuleId"]`The id of the rule of the event. 
- `prop config_rule_name : str`
- 
## Expand source code`@property def config_rule_name(self) -> str: """The name of the rule of the event.""" return self["configRuleName"]`The name of the rule of the event. 
- `prop evalution_mode : str | None`
- 
## Expand source code`@property def evalution_mode(self) -> str | None: """The evalution mode of the event.""" return self.get("evaluationMode")`The evalution mode of the event. 
- `prop event_left_scope : bool`
- 
## Expand source code`@property def event_left_scope(self) -> bool: """The left scope of the event.""" return self["eventLeftScope"]`The left scope of the event. 
- `prop execution_role_arn : str`
- 
## Expand source code`@property def execution_role_arn(self) -> str: """The execution role arn of the event.""" return self["executionRoleArn"]`The execution role arn of the event. 
- `prop invoking_event :`- [AWSConfigConfigurationChanged](#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigConfigurationChanged)|- [AWSConfigScheduledNotification](#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigScheduledNotification)|- [AWSConfigOversizedConfiguration](#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigOversizedConfiguration)
- 
## Expand source code`@property def invoking_event( self, ) -> AWSConfigConfigurationChanged | AWSConfigScheduledNotification | AWSConfigOversizedConfiguration: """The invoking payload of the event.""" if self._invoking_event is None: self._invoking_event = self._json_deserializer(self["invokingEvent"]) return get_invoke_event(self._invoking_event)`The invoking payload of the event. 
- `prop raw_invoking_event : str`
- 
## Expand source code`@property def raw_invoking_event(self) -> str: """The raw invoking payload of the event.""" return self["invokingEvent"]`The raw invoking payload of the event. 
- `prop result_token : str`
- 
## Expand source code`@property def result_token(self) -> str: """The result token of the event.""" return self["resultToken"]`The result token of the event. 
- `prop rule_parameters : dict`
- 
## Expand source code`@property def rule_parameters(self) -> dict: """The parameters of the event.""" if self._rule_parameters is None: self._rule_parameters = self._json_deserializer(self["ruleParameters"]) return self._rule_parameters`The parameters of the event. 
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: """The version of the event.""" return self["version"]`The version of the event. 
 ### Inherited members
- `class AWSConfigScheduledNotification (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class AWSConfigScheduledNotification(DictWrapper): @property def accountid(self) -> str: """The accountid of the ScheduledNotification event.""" return self["awsAccountId"] @property def notification_creation_time(self) -> str: """The notification creation time of the ScheduledNotification event.""" return self["notificationCreationTime"] @property def record_version(self) -> str: """The record version of the ScheduledNotification event.""" return self["recordVersion"] @property def message_type(self) -> str: """The message type of the ScheduledNotification event.""" return self["messageType"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop accountid : str`
- 
## Expand source code`@property def accountid(self) -> str: """The accountid of the ScheduledNotification event.""" return self["awsAccountId"]`The accountid of the ScheduledNotification event. 
- `prop message_type : str`
- 
## Expand source code`@property def message_type(self) -> str: """The message type of the ScheduledNotification event.""" return self["messageType"]`The message type of the ScheduledNotification event. 
- `prop notification_creation_time : str`
- 
## Expand source code`@property def notification_creation_time(self) -> str: """The notification creation time of the ScheduledNotification event.""" return self["notificationCreationTime"]`The notification creation time of the ScheduledNotification event. 
- `prop record_version : str`
- 
## Expand source code`@property def record_version(self) -> str: """The record version of the ScheduledNotification event.""" return self["recordVersion"]`The record version of the ScheduledNotification event. 
 ### Inherited members