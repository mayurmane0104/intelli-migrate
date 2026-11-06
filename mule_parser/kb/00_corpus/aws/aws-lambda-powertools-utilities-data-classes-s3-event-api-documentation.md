# aws_lambda_powertools.utilities.data_classes.s3_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/s3_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/s3_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.s3_event`

## Classes

- `class S3Bucket (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3Bucket(DictWrapper): @property def name(self) -> str: return self["s3"]["bucket"]["name"] @property def owner_identity(self) -> S3Identity: return S3Identity(self["s3"]["bucket"]["ownerIdentity"]) @property def arn(self) -> str: return self["s3"]["bucket"]["arn"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop arn : str`
- 
## Expand source code`@property def arn(self) -> str: return self["s3"]["bucket"]["arn"]`
- `prop name : str`
- 
## Expand source code`@property def name(self) -> str: return self["s3"]["bucket"]["name"]`
- `prop owner_identity :`- [S3Identity](#aws_lambda_powertools.utilities.data_classes.s3_event.S3Identity)
- 
## Expand source code`@property def owner_identity(self) -> S3Identity: return S3Identity(self["s3"]["bucket"]["ownerIdentity"])`
 ### Inherited members
- `class S3Event (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3Event(DictWrapper): """S3 event notification Documentation: ------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html - https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html - https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html """ @property def records(self) -> Iterator[S3EventRecord]: for record in self["Records"]: yield S3EventRecord(record) @property def record(self) -> S3EventRecord: """Get the first s3 event record""" return next(self.records) @property def bucket_name(self) -> str: """Get the bucket name for the first s3 event record""" return self["Records"][0]["s3"]["bucket"]["name"] @property def object_key(self) -> str: """Get the object key for the first s3 event record and unquote plus""" return unquote_plus(self["Records"][0]["s3"]["object"]["key"])`S3 event notification ## Documentation:- [https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html)
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
 ### Instance variables- `prop bucket_name : str`
- 
## Expand source code`@property def bucket_name(self) -> str: """Get the bucket name for the first s3 event record""" return self["Records"][0]["s3"]["bucket"]["name"]`Get the bucket name for the first s3 event record 
- `prop object_key : str`
- 
## Expand source code`@property def object_key(self) -> str: """Get the object key for the first s3 event record and unquote plus""" return unquote_plus(self["Records"][0]["s3"]["object"]["key"])`Get the object key for the first s3 event record and unquote plus 
- `prop record :`- [S3EventRecord](#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventRecord)
- 
## Expand source code`@property def record(self) -> S3EventRecord: """Get the first s3 event record""" return next(self.records)`Get the first s3 event record 
- `prop records : Iterator[`- [S3EventRecord](#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventRecord)]
- 
## Expand source code`@property def records(self) -> Iterator[S3EventRecord]: for record in self["Records"]: yield S3EventRecord(record)`
 ### Inherited members
- `class S3EventBridgeNotificationDetail (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3EventBridgeNotificationDetail(DictWrapper): @property def version(self) -> str: """Get the detail version""" return self["version"] @property def bucket(self) -> S3EventNotificationEventBridgeBucket: """Get the bucket name for the S3 notification""" return S3EventNotificationEventBridgeBucket(self["bucket"]) @property def object(self) -> S3EventBridgeNotificationObject: # noqa: A003 # ignore shadowing built-in grammar """Get the request-id for the S3 notification""" return S3EventBridgeNotificationObject(self["object"]) @property def request_id(self) -> str: """Get the request-id for the S3 notification""" return self["request-id"] @property def requester(self) -> str: """Get the AWS account ID or AWS service principal of requester for the S3 notification""" return self["requester"] @property def source_ip_address(self) -> str | None: """Get the source IP address of S3 request. Only present for events triggered by an S3 request.""" return self.get("source-ip-address") @property def reason(self) -> str | None: """Get the reason for the S3 notification. For 'Object Created events', the S3 API used to create the object: `PutObject`, `POST Object`, `CopyObject`, or `CompleteMultipartUpload`. For 'Object Deleted' events, this is set to `DeleteObject` when an object is deleted by an S3 API call, or 'Lifecycle Expiration' when an object is deleted by an S3 Lifecycle expiration rule. """ return self.get("reason") @property def deletion_type(self) -> str | None: """Get the deletion type for the S3 object in this notification. For 'Object Deleted' events, when an unversioned object is deleted, or a versioned object is permanently deleted this is set to 'Permanently Deleted'. When a delete marker is created for a versioned object, this is set to 'Delete Marker Created'. """ return self.get("deletion-type") @property def restore_expiry_time(self) -> str | None: """Get the restore expiry time for the S3 object in this notification. For 'Object Restore Completed' events, the time when the temporary copy of the object will be deleted from S3. """ return self.get("restore-expiry-time") @property def source_storage_class(self) -> str | None: """Get the source storage class of the S3 object in this notification. For 'Object Restore Initiated' and 'Object Restore Completed' events, the storage class of the object being restored. """ return self.get("source-storage-class") @property def destination_storage_class(self) -> str | None: """Get the destination storage class of the S3 object in this notification. For 'Object Storage Class Changed' events, the new storage class of the object. """ return self.get("destination-storage-class") @property def destination_access_tier(self) -> str | None: """Get the destination access tier of the S3 object in this notification. For 'Object Access Tier Changed' events, the new access tier of the object. """ return self.get("destination-access-tier")`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop bucket :`- [S3EventNotificationEventBridgeBucket](#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventNotificationEventBridgeBucket)
- 
## Expand source code`@property def bucket(self) -> S3EventNotificationEventBridgeBucket: """Get the bucket name for the S3 notification""" return S3EventNotificationEventBridgeBucket(self["bucket"])`Get the bucket name for the S3 notification 
- `prop deletion_type : str | None`
- 
## Expand source code`@property def deletion_type(self) -> str | None: """Get the deletion type for the S3 object in this notification. For 'Object Deleted' events, when an unversioned object is deleted, or a versioned object is permanently deleted this is set to 'Permanently Deleted'. When a delete marker is created for a versioned object, this is set to 'Delete Marker Created'. """ return self.get("deletion-type")`Get the deletion type for the S3 object in this notification. For 'Object Deleted' events, when an unversioned object is deleted, or a versioned object is permanently deleted this is set to 'Permanently Deleted'. When a delete marker is created for a versioned object, this is set to 'Delete Marker Created'. 
- `prop destination_access_tier : str | None`
- 
## Expand source code`@property def destination_access_tier(self) -> str | None: """Get the destination access tier of the S3 object in this notification. For 'Object Access Tier Changed' events, the new access tier of the object. """ return self.get("destination-access-tier")`Get the destination access tier of the S3 object in this notification. For 'Object Access Tier Changed' events, the new access tier of the object. 
- `prop destination_storage_class : str | None`
- 
## Expand source code`@property def destination_storage_class(self) -> str | None: """Get the destination storage class of the S3 object in this notification. For 'Object Storage Class Changed' events, the new storage class of the object. """ return self.get("destination-storage-class")`Get the destination storage class of the S3 object in this notification. For 'Object Storage Class Changed' events, the new storage class of the object. 
- `prop object :`- [S3EventBridgeNotificationObject](#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventBridgeNotificationObject)
- 
## Expand source code`@property def object(self) -> S3EventBridgeNotificationObject: # noqa: A003 # ignore shadowing built-in grammar """Get the request-id for the S3 notification""" return S3EventBridgeNotificationObject(self["object"])`Get the request-id for the S3 notification 
- `prop reason : str | None`
- 
## Expand source code`@property def reason(self) -> str | None: """Get the reason for the S3 notification. For 'Object Created events', the S3 API used to create the object: `PutObject`, `POST Object`, `CopyObject`, or `CompleteMultipartUpload`. For 'Object Deleted' events, this is set to `DeleteObject` when an object is deleted by an S3 API call, or 'Lifecycle Expiration' when an object is deleted by an S3 Lifecycle expiration rule. """ return self.get("reason")`Get the reason for the S3 notification. For 'Object Created events', the S3 API used to create the object: `PutObject`,`POST Object`,`CopyObject`, or`CompleteMultipartUpload`. For 'Object Deleted' events, this is set to`DeleteObject`when an object is deleted by an S3 API call, or 'Lifecycle Expiration' when an object is deleted by an S3 Lifecycle expiration rule.
- `prop request_id : str`
- 
## Expand source code`@property def request_id(self) -> str: """Get the request-id for the S3 notification""" return self["request-id"]`Get the request-id for the S3 notification 
- `prop requester : str`
- 
## Expand source code`@property def requester(self) -> str: """Get the AWS account ID or AWS service principal of requester for the S3 notification""" return self["requester"]`Get the AWS account ID or AWS service principal of requester for the S3 notification 
- `prop restore_expiry_time : str | None`
- 
## Expand source code`@property def restore_expiry_time(self) -> str | None: """Get the restore expiry time for the S3 object in this notification. For 'Object Restore Completed' events, the time when the temporary copy of the object will be deleted from S3. """ return self.get("restore-expiry-time")`Get the restore expiry time for the S3 object in this notification. For 'Object Restore Completed' events, the time when the temporary copy of the object will be deleted from S3. 
- `prop source_ip_address : str | None`
- 
## Expand source code`@property def source_ip_address(self) -> str | None: """Get the source IP address of S3 request. Only present for events triggered by an S3 request.""" return self.get("source-ip-address")`Get the source IP address of S3 request. Only present for events triggered by an S3 request. 
- `prop source_storage_class : str | None`
- 
## Expand source code`@property def source_storage_class(self) -> str | None: """Get the source storage class of the S3 object in this notification. For 'Object Restore Initiated' and 'Object Restore Completed' events, the storage class of the object being restored. """ return self.get("source-storage-class")`Get the source storage class of the S3 object in this notification. For 'Object Restore Initiated' and 'Object Restore Completed' events, the storage class of the object being restored. 
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: """Get the detail version""" return self["version"]`Get the detail version 
 ### Inherited members
- `class S3EventBridgeNotificationEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3EventBridgeNotificationEvent(EventBridgeEvent): """Amazon S3EventBridge Event Documentation: -------------- - https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-events.html """ @property def detail(self) -> S3EventBridgeNotificationDetail: # type: ignore[override] """S3 notification details""" return S3EventBridgeNotificationDetail(self["detail"])`Amazon S3EventBridge Event ## Documentation:## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [EventBridgeEvent](event_bridge_event.html#aws_lambda_powertools.utilities.data_classes.event_bridge_event.EventBridgeEvent)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop detail :`- [S3EventBridgeNotificationDetail](#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventBridgeNotificationDetail)
- 
## Expand source code`@property def detail(self) -> S3EventBridgeNotificationDetail: # type: ignore[override] """S3 notification details""" return S3EventBridgeNotificationDetail(self["detail"])`S3 notification details 
 ### Inherited members
- `class S3EventBridgeNotificationObject (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3EventBridgeNotificationObject(DictWrapper): @property def key(self) -> str: """Object key""" return unquote_plus(self["key"]) @property def size(self) -> int | None: """Object size. Object deletion event doesn't contain size.""" return self.get("size") @property def etag(self) -> str: """Object etag. Object deletion event doesn't contain etag; we default to empty string""" return self.get("etag", "") # type: ignore[return-value] # false positive @property def version_id(self) -> str: """Object version ID""" return self["version-id"] @property def sequencer(self) -> str: """Object key""" return self["sequencer"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop etag : str`
- 
## Expand source code`@property def etag(self) -> str: """Object etag. Object deletion event doesn't contain etag; we default to empty string""" return self.get("etag", "") # type: ignore[return-value] # false positive`Object etag. Object deletion event doesn't contain etag; we default to empty string 
- `prop key : str`
- 
## Expand source code`@property def key(self) -> str: """Object key""" return unquote_plus(self["key"])`Object key 
- `prop sequencer : str`
- 
## Expand source code`@property def sequencer(self) -> str: """Object key""" return self["sequencer"]`Object key 
- `prop size : int | None`
- 
## Expand source code`@property def size(self) -> int | None: """Object size. Object deletion event doesn't contain size.""" return self.get("size")`Object size. Object deletion event doesn't contain size. 
- `prop version_id : str`
- 
## Expand source code`@property def version_id(self) -> str: """Object version ID""" return self["version-id"]`Object version ID 
 ### Inherited members
- `class S3EventNotificationEventBridgeBucket (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3EventNotificationEventBridgeBucket(DictWrapper): @property def name(self) -> str: return self["name"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop name : str`
- 
## Expand source code`@property def name(self) -> str: return self["name"]`
 ### Inherited members
- `class S3EventRecord (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3EventRecord(DictWrapper): @property def event_version(self) -> str: """The eventVersion key value contains a major and minor version in the form <major>.<minor>.""" return self["eventVersion"] @property def event_source(self) -> str: """The AWS service from which the S3 event originated. For S3, this is aws:s3""" return self["eventSource"] @property def aws_region(self) -> str: """aws region eg: us-east-1""" return self["awsRegion"] @property def event_time(self) -> str: """The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, when S3 finished processing the request""" return self["eventTime"] @property def event_name(self) -> str: """Event type""" return self["eventName"] @property def user_identity(self) -> S3Identity: return S3Identity(self["userIdentity"]) @property def request_parameters(self) -> S3RequestParameters: return S3RequestParameters(self._data) @property def response_elements(self) -> dict[str, str]: """The responseElements key value is useful if you want to trace a request by following up with AWS Support. Both x-amz-request-id and x-amz-id-2 help Amazon S3 trace an individual request. These values are the same as those that Amazon S3 returns in the response to the request that initiates the events, so they can be used to match the event to the request. """ return self["responseElements"] @property def s3(self) -> S3Message: return S3Message(self._data) @property def glacier_event_data(self) -> S3EventRecordGlacierEventData | None: """The glacierEventData key is only visible for s3:ObjectRestore:Completed events.""" item = self.get("glacierEventData") return None if item is None else S3EventRecordGlacierEventData(item)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop aws_region : str`
- 
## Expand source code`@property def aws_region(self) -> str: """aws region eg: us-east-1""" return self["awsRegion"]`aws region eg: us-east-1 
- `prop event_name : str`
- 
## Expand source code`@property def event_name(self) -> str: """Event type""" return self["eventName"]`Event type 
- `prop event_source : str`
- 
## Expand source code`@property def event_source(self) -> str: """The AWS service from which the S3 event originated. For S3, this is aws:s3""" return self["eventSource"]`The AWS service from which the S3 event originated. For S3, this is aws:s3 
- `prop event_time : str`
- 
## Expand source code`@property def event_time(self) -> str: """The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, when S3 finished processing the request""" return self["eventTime"]`The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, when S3 finished processing the request 
- `prop event_version : str`
- 
## Expand source code`@property def event_version(self) -> str: """The eventVersion key value contains a major and minor version in the form <major>.<minor>.""" return self["eventVersion"]`The eventVersion key value contains a major and minor version in the form . . 
- `prop glacier_event_data :`- [S3EventRecordGlacierEventData](#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventRecordGlacierEventData)| None
- 
## Expand source code`@property def glacier_event_data(self) -> S3EventRecordGlacierEventData | None: """The glacierEventData key is only visible for s3:ObjectRestore:Completed events.""" item = self.get("glacierEventData") return None if item is None else S3EventRecordGlacierEventData(item)`The glacierEventData key is only visible for s3:ObjectRestore:Completed events. 
- `prop request_parameters :`- [S3RequestParameters](#aws_lambda_powertools.utilities.data_classes.s3_event.S3RequestParameters)
- 
## Expand source code`@property def request_parameters(self) -> S3RequestParameters: return S3RequestParameters(self._data)`
- `prop response_elements : dict[str, str]`
- 
## Expand source code`@property def response_elements(self) -> dict[str, str]: """The responseElements key value is useful if you want to trace a request by following up with AWS Support. Both x-amz-request-id and x-amz-id-2 help Amazon S3 trace an individual request. These values are the same as those that Amazon S3 returns in the response to the request that initiates the events, so they can be used to match the event to the request. """ return self["responseElements"]`The responseElements key value is useful if you want to trace a request by following up with AWS Support. Both x-amz-request-id and x-amz-id-2 help Amazon S3 trace an individual request. These values are the same as those that Amazon S3 returns in the response to the request that initiates the events, so they can be used to match the event to the request. 
- `prop s3 :`- [S3Message](#aws_lambda_powertools.utilities.data_classes.s3_event.S3Message)
- 
## Expand source code`@property def s3(self) -> S3Message: return S3Message(self._data)`
- `prop user_identity :`- [S3Identity](#aws_lambda_powertools.utilities.data_classes.s3_event.S3Identity)
- 
## Expand source code`@property def user_identity(self) -> S3Identity: return S3Identity(self["userIdentity"])`
 ### Inherited members
- `class S3EventRecordGlacierEventData (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3EventRecordGlacierEventData(DictWrapper): @property def restore_event_data(self) -> S3EventRecordGlacierRestoreEventData: """The restoreEventData key contains attributes related to your restore request. The glacierEventData key is only visible for s3:ObjectRestore:Completed events """ return S3EventRecordGlacierRestoreEventData(self._data)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop restore_event_data :`- [S3EventRecordGlacierRestoreEventData](#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventRecordGlacierRestoreEventData)
- 
## Expand source code`@property def restore_event_data(self) -> S3EventRecordGlacierRestoreEventData: """The restoreEventData key contains attributes related to your restore request. The glacierEventData key is only visible for s3:ObjectRestore:Completed events """ return S3EventRecordGlacierRestoreEventData(self._data)`The restoreEventData key contains attributes related to your restore request. The glacierEventData key is only visible for s3:ObjectRestore:Completed events 
 ### Inherited members
- `class S3EventRecordGlacierRestoreEventData (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3EventRecordGlacierRestoreEventData(DictWrapper): @property def lifecycle_restoration_expiry_time(self) -> str: """Time when the object restoration will be expired.""" return self["restoreEventData"]["lifecycleRestorationExpiryTime"] @property def lifecycle_restore_storage_class(self) -> str: """Source storage class for restore""" return self["restoreEventData"]["lifecycleRestoreStorageClass"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop lifecycle_restoration_expiry_time : str`
- 
## Expand source code`@property def lifecycle_restoration_expiry_time(self) -> str: """Time when the object restoration will be expired.""" return self["restoreEventData"]["lifecycleRestorationExpiryTime"]`Time when the object restoration will be expired. 
- `prop lifecycle_restore_storage_class : str`
- 
## Expand source code`@property def lifecycle_restore_storage_class(self) -> str: """Source storage class for restore""" return self["restoreEventData"]["lifecycleRestoreStorageClass"]`Source storage class for restore 
 ### Inherited members
- `class S3Identity (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3Identity(DictWrapper): @property def principal_id(self) -> str: return self["principalId"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop principal_id : str`
- 
## Expand source code`@property def principal_id(self) -> str: return self["principalId"]`
 ### Inherited members
- `class S3Message (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3Message(DictWrapper): @property def s3_schema_version(self) -> str: return self["s3"]["s3SchemaVersion"] @property def configuration_id(self) -> str: """ID found in the bucket notification configuration""" return self["s3"]["configurationId"] @property def bucket(self) -> S3Bucket: return S3Bucket(self._data) @property def get_object(self) -> S3Object: """Get the `object` property as an S3Object""" # Note: this name conflicts with existing python builtins return S3Object(self._data)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop bucket :`- [S3Bucket](#aws_lambda_powertools.utilities.data_classes.s3_event.S3Bucket)
- 
## Expand source code`@property def bucket(self) -> S3Bucket: return S3Bucket(self._data)`
- `prop configuration_id : str`
- 
## Expand source code`@property def configuration_id(self) -> str: """ID found in the bucket notification configuration""" return self["s3"]["configurationId"]`ID found in the bucket notification configuration 
- `prop get_object :`- [S3Object](#aws_lambda_powertools.utilities.data_classes.s3_event.S3Object)
- 
## Expand source code`@property def get_object(self) -> S3Object: """Get the `object` property as an S3Object""" # Note: this name conflicts with existing python builtins return S3Object(self._data)`Get the `object`property as an S3Object
- `prop s3_schema_version : str`
- 
## Expand source code`@property def s3_schema_version(self) -> str: return self["s3"]["s3SchemaVersion"]`
 ### Inherited members
- `class S3Object (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3Object(DictWrapper): @property def key(self) -> str: """Object key""" return self["s3"]["object"]["key"] @property def size(self) -> int: """Object byte size""" return int(self["s3"]["object"]["size"]) @property def etag(self) -> str: """Object eTag. Object deletion event doesn't contain eTag; we default to empty string""" return self["s3"]["object"].get("eTag", "") @property def version_id(self) -> str | None: """Object version if bucket is versioning-enabled, otherwise null""" return self["s3"]["object"].get("versionId") @property def sequencer(self) -> str: """A string representation of a hexadecimal value used to determine event sequence, only used with PUTs and DELETEs """ return self["s3"]["object"]["sequencer"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop etag : str`
- 
## Expand source code`@property def etag(self) -> str: """Object eTag. Object deletion event doesn't contain eTag; we default to empty string""" return self["s3"]["object"].get("eTag", "")`Object eTag. Object deletion event doesn't contain eTag; we default to empty string 
- `prop key : str`
- 
## Expand source code`@property def key(self) -> str: """Object key""" return self["s3"]["object"]["key"]`Object key 
- `prop sequencer : str`
- 
## Expand source code`@property def sequencer(self) -> str: """A string representation of a hexadecimal value used to determine event sequence, only used with PUTs and DELETEs """ return self["s3"]["object"]["sequencer"]`A string representation of a hexadecimal value used to determine event sequence, only used with PUTs and DELETEs 
- `prop size : int`
- 
## Expand source code`@property def size(self) -> int: """Object byte size""" return int(self["s3"]["object"]["size"])`Object byte size 
- `prop version_id : str | None`
- 
## Expand source code`@property def version_id(self) -> str | None: """Object version if bucket is versioning-enabled, otherwise null""" return self["s3"]["object"].get("versionId")`Object version if bucket is versioning-enabled, otherwise null 
 ### Inherited members
- `class S3RequestParameters (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3RequestParameters(DictWrapper): @property def source_ip_address(self) -> str: return self["requestParameters"]["sourceIPAddress"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop source_ip_address : str`
- 
## Expand source code`@property def source_ip_address(self) -> str: return self["requestParameters"]["sourceIPAddress"]`
 ### Inherited members