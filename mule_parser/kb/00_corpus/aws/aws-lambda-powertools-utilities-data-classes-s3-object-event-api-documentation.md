# aws_lambda_powertools.utilities.data_classes.s3_object_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/s3_object_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/s3_object_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.s3_object_event`

## Classes

- `class S3ObjectConfiguration (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3ObjectConfiguration(DictWrapper): """Configuration information about the S3 Object Lambda access point.""" @property def access_point_arn(self) -> str: """The Amazon Resource Name (ARN) of the S3 Object Lambda access point that received this request.""" return self["accessPointArn"] @property def supporting_access_point_arn(self) -> str: """The ARN of the supporting access point that is specified in the S3 Object Lambda access point configuration.""" return self["supportingAccessPointArn"] @property def payload(self) -> str: """Custom data that is applied to the S3 Object Lambda access point configuration. S3 Object Lambda treats this as an opaque string, so it might need to be decoded before use.""" return self["payload"]`Configuration information about the S3 Object Lambda access point. ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop access_point_arn : str`
- 
## Expand source code`@property def access_point_arn(self) -> str: """The Amazon Resource Name (ARN) of the S3 Object Lambda access point that received this request.""" return self["accessPointArn"]`The Amazon Resource Name (ARN) of the S3 Object Lambda access point that received this request. 
- `prop payload : str`
- 
## Expand source code`@property def payload(self) -> str: """Custom data that is applied to the S3 Object Lambda access point configuration. S3 Object Lambda treats this as an opaque string, so it might need to be decoded before use.""" return self["payload"]`Custom data that is applied to the S3 Object Lambda access point configuration. S3 Object Lambda treats this as an opaque string, so it might need to be decoded before use. 
- `prop supporting_access_point_arn : str`
- 
## Expand source code`@property def supporting_access_point_arn(self) -> str: """The ARN of the supporting access point that is specified in the S3 Object Lambda access point configuration.""" return self["supportingAccessPointArn"]`The ARN of the supporting access point that is specified in the S3 Object Lambda access point configuration. 
 ### Inherited members
- `class S3ObjectContext (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3ObjectContext(DictWrapper): """The input and output details for connections to Amazon S3 and S3 Object Lambda.""" @property def input_s3_url(self) -> str: """A pre-signed URL that can be used to fetch the original object from Amazon S3. The URL is signed using the original caller’s identity, and their permissions will apply when the URL is used. If there are signed headers in the URL, the Lambda function must include these in the call to Amazon S3, except for the Host.""" return self["inputS3Url"] @property def output_route(self) -> str: """A routing token that is added to the S3 Object Lambda URL when the Lambda function calls `WriteGetObjectResponse`.""" return self["outputRoute"] @property def output_token(self) -> str: """An opaque token used by S3 Object Lambda to match the WriteGetObjectResponse call with the original caller.""" return self["outputToken"]`The input and output details for connections to Amazon S3 and S3 Object Lambda. ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop input_s3_url : str`
- 
## Expand source code`@property def input_s3_url(self) -> str: """A pre-signed URL that can be used to fetch the original object from Amazon S3. The URL is signed using the original caller’s identity, and their permissions will apply when the URL is used. If there are signed headers in the URL, the Lambda function must include these in the call to Amazon S3, except for the Host.""" return self["inputS3Url"]`A pre-signed URL that can be used to fetch the original object from Amazon S3. The URL is signed using the original caller’s identity, and their permissions will apply when the URL is used. If there are signed headers in the URL, the Lambda function must include these in the call to Amazon S3, except for the Host. 
- `prop output_route : str`
- 
## Expand source code`@property def output_route(self) -> str: """A routing token that is added to the S3 Object Lambda URL when the Lambda function calls `WriteGetObjectResponse`.""" return self["outputRoute"]`A routing token that is added to the S3 Object Lambda URL when the Lambda function calls `WriteGetObjectResponse`.
- `prop output_token : str`
- 
## Expand source code`@property def output_token(self) -> str: """An opaque token used by S3 Object Lambda to match the WriteGetObjectResponse call with the original caller.""" return self["outputToken"]`An opaque token used by S3 Object Lambda to match the WriteGetObjectResponse call with the original caller. 
 ### Inherited members
- `class S3ObjectLambdaEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3ObjectLambdaEvent(DictWrapper): """S3 object lambda event Documentation: ------------- - https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-writing-lambda.html Example ------- **Fetch and transform original object from Amazon S3** import boto3 import requests from aws_lambda_powertools.utilities.data_classes.s3_object_event import S3ObjectLambdaEvent session = boto3.session.Session() s3 = session.client("s3") def lambda_handler(event, context): event = S3ObjectLambdaEvent(event) # Get object from S3 response = requests.get(event.input_s3_url) original_object = response.content.decode("utf-8") # Make changes to the object about to be returned transformed_object = original_object.upper() # Write object back to S3 Object Lambda s3.write_get_object_response( Body=transformed_object, RequestRoute=event.request_route, RequestToken=event.request_token ) """ @property def request_id(self) -> str: """The Amazon S3 request ID for this request. We recommend that you log this value to help with debugging.""" return self["xAmzRequestId"] @property def object_context(self) -> S3ObjectContext: """The input and output details for connections to Amazon S3 and S3 Object Lambda.""" return S3ObjectContext(self["getObjectContext"]) @property def configuration(self) -> S3ObjectConfiguration: """Configuration information about the S3 Object Lambda access point.""" return S3ObjectConfiguration(self["configuration"]) @property def user_request(self) -> S3ObjectUserRequest: """Information about the original call to S3 Object Lambda.""" return S3ObjectUserRequest(self["userRequest"]) @property def user_identity(self) -> S3ObjectUserIdentity: """Details about the identity that made the call to S3 Object Lambda.""" return S3ObjectUserIdentity(self["userIdentity"]) @property def request_route(self) -> str: """A routing token that is added to the S3 Object Lambda URL when the Lambda function calls `WriteGetObjectResponse`.""" return self.object_context.output_route @property def request_token(self) -> str: """An opaque token used by S3 Object Lambda to match the WriteGetObjectResponse call with the original caller.""" return self.object_context.output_token @property def input_s3_url(self) -> str: """A pre-signed URL that can be used to fetch the original object from Amazon S3. The URL is signed using the original caller’s identity, and their permissions will apply when the URL is used. If there are signed headers in the URL, the Lambda function must include these in the call to Amazon S3, except for the Host. Example ------- **Fetch original object from Amazon S3** import requests from aws_lambda_powertools.utilities.data_classes.s3_object_event import S3ObjectLambdaEvent def lambda_handler(event, context): event = S3ObjectLambdaEvent(event) response = requests.get(event.input_s3_url) original_object = response.content.decode("utf-8") ... """ return self.object_context.input_s3_url @property def protocol_version(self) -> str: """The version ID of the context provided. The format of this field is `{Major Version}`.`{Minor Version}`. The minor version numbers are always two-digit numbers. Any removal or change to the semantics of a field will necessitate a major version bump and will require active opt-in. Amazon S3 can add new fields at any time, at which point you might experience a minor version bump. Due to the nature of software rollouts, it is possible that you might see multiple minor versions in use at once. """ return self["protocolVersion"]`S3 object lambda event ## Documentation:## Example**Fetch and transform original object from Amazon S3**`import boto3 import requests from aws_lambda_powertools.utilities.data_classes.s3_object_event import S3ObjectLambdaEvent session = boto3.session.Session() s3 = session.client("s3") def lambda_handler(event, context): event = S3ObjectLambdaEvent(event) # Get object from S3 response = requests.get(event.input_s3_url) original_object = response.content.decode("utf-8") # Make changes to the object about to be returned transformed_object = original_object.upper() # Write object back to S3 Object Lambda s3.write_get_object_response( Body=transformed_object, RequestRoute=event.request_route, RequestToken=event.request_token )`## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop configuration :`- [S3ObjectConfiguration](#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectConfiguration)
- 
## Expand source code`@property def configuration(self) -> S3ObjectConfiguration: """Configuration information about the S3 Object Lambda access point.""" return S3ObjectConfiguration(self["configuration"])`Configuration information about the S3 Object Lambda access point. 
- `prop input_s3_url : str`
- 
## Expand source code`@property def input_s3_url(self) -> str: """A pre-signed URL that can be used to fetch the original object from Amazon S3. The URL is signed using the original caller’s identity, and their permissions will apply when the URL is used. If there are signed headers in the URL, the Lambda function must include these in the call to Amazon S3, except for the Host. Example ------- **Fetch original object from Amazon S3** import requests from aws_lambda_powertools.utilities.data_classes.s3_object_event import S3ObjectLambdaEvent def lambda_handler(event, context): event = S3ObjectLambdaEvent(event) response = requests.get(event.input_s3_url) original_object = response.content.decode("utf-8") ... """ return self.object_context.input_s3_url`A pre-signed URL that can be used to fetch the original object from Amazon S3. The URL is signed using the original caller’s identity, and their permissions will apply when the URL is used. If there are signed headers in the URL, the Lambda function must include these in the call to Amazon S3, except for the Host. ## Example**Fetch original object from Amazon S3**`import requests from aws_lambda_powertools.utilities.data_classes.s3_object_event import S3ObjectLambdaEvent def lambda_handler(event, context): event = S3ObjectLambdaEvent(event) response = requests.get(event.input_s3_url) original_object = response.content.decode("utf-8") ...`
- `prop object_context :`- [S3ObjectContext](#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectContext)
- 
## Expand source code`@property def object_context(self) -> S3ObjectContext: """The input and output details for connections to Amazon S3 and S3 Object Lambda.""" return S3ObjectContext(self["getObjectContext"])`The input and output details for connections to Amazon S3 and S3 Object Lambda. 
- `prop protocol_version : str`
- 
## Expand source code`@property def protocol_version(self) -> str: """The version ID of the context provided. The format of this field is `{Major Version}`.`{Minor Version}`. The minor version numbers are always two-digit numbers. Any removal or change to the semantics of a field will necessitate a major version bump and will require active opt-in. Amazon S3 can add new fields at any time, at which point you might experience a minor version bump. Due to the nature of software rollouts, it is possible that you might see multiple minor versions in use at once. """ return self["protocolVersion"]`The version ID of the context provided. The format of this field is `{Major Version}`.`{Minor Version}`. The minor version numbers are always two-digit numbers. Any removal or change to the semantics of a field will necessitate a major version bump and will require active opt-in. Amazon S3 can add new fields at any time, at which point you might experience a minor version bump. Due to the nature of software rollouts, it is possible that you might see multiple minor versions in use at once.
- `prop request_id : str`
- 
## Expand source code`@property def request_id(self) -> str: """The Amazon S3 request ID for this request. We recommend that you log this value to help with debugging.""" return self["xAmzRequestId"]`The Amazon S3 request ID for this request. We recommend that you log this value to help with debugging. 
- `prop request_route : str`
- 
## Expand source code`@property def request_route(self) -> str: """A routing token that is added to the S3 Object Lambda URL when the Lambda function calls `WriteGetObjectResponse`.""" return self.object_context.output_route`A routing token that is added to the S3 Object Lambda URL when the Lambda function calls `WriteGetObjectResponse`.
- `prop request_token : str`
- 
## Expand source code`@property def request_token(self) -> str: """An opaque token used by S3 Object Lambda to match the WriteGetObjectResponse call with the original caller.""" return self.object_context.output_token`An opaque token used by S3 Object Lambda to match the WriteGetObjectResponse call with the original caller. 
- `prop user_identity :`- [S3ObjectUserIdentity](#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectUserIdentity)
- 
## Expand source code`@property def user_identity(self) -> S3ObjectUserIdentity: """Details about the identity that made the call to S3 Object Lambda.""" return S3ObjectUserIdentity(self["userIdentity"])`Details about the identity that made the call to S3 Object Lambda. 
- `prop user_request :`- [S3ObjectUserRequest](#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectUserRequest)
- 
## Expand source code`@property def user_request(self) -> S3ObjectUserRequest: """Information about the original call to S3 Object Lambda.""" return S3ObjectUserRequest(self["userRequest"])`Information about the original call to S3 Object Lambda. 
 ### Inherited members
- `class S3ObjectSessionAttributes (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3ObjectSessionAttributes(DictWrapper): @property def creation_date(self) -> str: """The date and time when the temporary security credentials were issued. Represented in ISO 8601 basic notation.""" return self["creationDate"] @property def mfa_authenticated(self) -> str: """The value is true if the root user or IAM user whose credentials were used for the request also was authenticated with an MFA device; otherwise, false.""" return self["mfaAuthenticated"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop creation_date : str`
- 
## Expand source code`@property def creation_date(self) -> str: """The date and time when the temporary security credentials were issued. Represented in ISO 8601 basic notation.""" return self["creationDate"]`The date and time when the temporary security credentials were issued. Represented in ISO 8601 basic notation. 
- `prop mfa_authenticated : str`
- 
## Expand source code`@property def mfa_authenticated(self) -> str: """The value is true if the root user or IAM user whose credentials were used for the request also was authenticated with an MFA device; otherwise, false.""" return self["mfaAuthenticated"]`The value is true if the root user or IAM user whose credentials were used for the request also was authenticated with an MFA device; otherwise, false. 
 ### Inherited members
- `class S3ObjectSessionContext (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3ObjectSessionContext(DictWrapper): @property def session_issuer(self) -> S3ObjectSessionIssuer: """If the request was made with temporary security credentials, an element that provides information about how the credentials were obtained.""" return S3ObjectSessionIssuer(self["sessionIssuer"]) @property def attributes(self) -> S3ObjectSessionAttributes: """Session attributes.""" return S3ObjectSessionAttributes(self["attributes"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop attributes :`- [S3ObjectSessionAttributes](#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectSessionAttributes)
- 
## Expand source code`@property def attributes(self) -> S3ObjectSessionAttributes: """Session attributes.""" return S3ObjectSessionAttributes(self["attributes"])`Session attributes. 
- `prop session_issuer :`- [S3ObjectSessionIssuer](#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectSessionIssuer)
- 
## Expand source code`@property def session_issuer(self) -> S3ObjectSessionIssuer: """If the request was made with temporary security credentials, an element that provides information about how the credentials were obtained.""" return S3ObjectSessionIssuer(self["sessionIssuer"])`If the request was made with temporary security credentials, an element that provides information about how the credentials were obtained. 
 ### Inherited members
- `class S3ObjectSessionIssuer (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3ObjectSessionIssuer(DictWrapper): @property def get_type(self) -> str: """The source of the temporary security credentials, such as Root, IAMUser, or Role.""" return self["type"] @property def user_name(self) -> str: """The friendly name of the user or role that issued the session.""" return self["userName"] @property def principal_id(self) -> str: """The internal ID of the entity that was used to get credentials.""" return self["principalId"] @property def arn(self) -> str: """The ARN of the source (account, IAM user, or role) that was used to get temporary security credentials.""" return self["arn"] @property def account_id(self) -> str: """The account that owns the entity that was used to get credentials.""" return self["accountId"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop account_id : str`
- 
## Expand source code`@property def account_id(self) -> str: """The account that owns the entity that was used to get credentials.""" return self["accountId"]`The account that owns the entity that was used to get credentials. 
- `prop arn : str`
- 
## Expand source code`@property def arn(self) -> str: """The ARN of the source (account, IAM user, or role) that was used to get temporary security credentials.""" return self["arn"]`The ARN of the source (account, IAM user, or role) that was used to get temporary security credentials. 
- `prop get_type : str`
- 
## Expand source code`@property def get_type(self) -> str: """The source of the temporary security credentials, such as Root, IAMUser, or Role.""" return self["type"]`The source of the temporary security credentials, such as Root, IAMUser, or Role. 
- `prop principal_id : str`
- 
## Expand source code`@property def principal_id(self) -> str: """The internal ID of the entity that was used to get credentials.""" return self["principalId"]`The internal ID of the entity that was used to get credentials. 
- `prop user_name : str`
- 
## Expand source code`@property def user_name(self) -> str: """The friendly name of the user or role that issued the session.""" return self["userName"]`The friendly name of the user or role that issued the session. 
 ### Inherited members
- `class S3ObjectUserIdentity (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3ObjectUserIdentity(DictWrapper): """Details about the identity that made the call to S3 Object Lambda. Documentation: ------------- - https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html """ @property def get_type(self) -> str: """The type of identity. The following values are possible: - Root – The request was made with your AWS account credentials. If the userIdentity type is Root and you set an alias for your account, the userName field contains your account alias. For more information, see Your AWS Account ID and Its Alias. - IAMUser – The request was made with the credentials of an IAM user. - AssumedRole – The request was made with temporary security credentials that were obtained with a role via a call to the AWS Security Token Service (AWS STS) AssumeRole API. This can include roles for Amazon EC2 and cross-account API access. - FederatedUser – The request was made with temporary security credentials that were obtained via a call to the AWS STS GetFederationToken API. The sessionIssuer element indicates if the API was called with root or IAM user credentials. - AWSAccount – The request was made by another AWS account. - AWSService – The request was made by an AWS account that belongs to an AWS service. For example, AWS Elastic Beanstalk assumes an IAM role in your account to call other AWS services on your behalf. """ return self["type"] @property def account_id(self) -> str: """The account that owns the entity that granted permissions for the request. If the request was made with temporary security credentials, this is the account that owns the IAM user or role that was used to obtain credentials.""" return self["accountId"] @property def access_key_id(self) -> str: """The access key ID that was used to sign the request. If the request was made with temporary security credentials, this is the access key ID of the temporary credentials. For security reasons, accessKeyId might not be present, or might be displayed as an empty string.""" return self["accessKeyId"] @property def user_name(self) -> str: """The friendly name of the identity that made the call.""" return self["userName"] @property def principal_id(self) -> str: """The unique identifier for the identity that made the call. For requests made with temporary security credentials, this value includes the session name that is passed to the AssumeRole, AssumeRoleWithWebIdentity, or GetFederationToken API call.""" return self["principalId"] @property def arn(self) -> str: """The ARN of the principal that made the call. The last section of the ARN contains the user or role that made the call.""" return self["arn"] @property def session_context(self) -> S3ObjectSessionContext | None: """If the request was made with temporary security credentials, this element provides information about the session that was created for those credentials.""" session_context = self.get("sessionContext") if session_context is None: return None return S3ObjectSessionContext(session_context)`Details about the identity that made the call to S3 Object Lambda. ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop access_key_id : str`
- 
## Expand source code`@property def access_key_id(self) -> str: """The access key ID that was used to sign the request. If the request was made with temporary security credentials, this is the access key ID of the temporary credentials. For security reasons, accessKeyId might not be present, or might be displayed as an empty string.""" return self["accessKeyId"]`The access key ID that was used to sign the request. If the request was made with temporary security credentials, this is the access key ID of the temporary credentials. For security reasons, accessKeyId might not be present, or might be displayed as an empty string. 
- `prop account_id : str`
- 
## Expand source code`@property def account_id(self) -> str: """The account that owns the entity that granted permissions for the request. If the request was made with temporary security credentials, this is the account that owns the IAM user or role that was used to obtain credentials.""" return self["accountId"]`The account that owns the entity that granted permissions for the request. If the request was made with temporary security credentials, this is the account that owns the IAM user or role that was used to obtain credentials. 
- `prop arn : str`
- 
## Expand source code`@property def arn(self) -> str: """The ARN of the principal that made the call. The last section of the ARN contains the user or role that made the call.""" return self["arn"]`The ARN of the principal that made the call. The last section of the ARN contains the user or role that made the call. 
- `prop get_type : str`
- 
## Expand source code`@property def get_type(self) -> str: """The type of identity. The following values are possible: - Root – The request was made with your AWS account credentials. If the userIdentity type is Root and you set an alias for your account, the userName field contains your account alias. For more information, see Your AWS Account ID and Its Alias. - IAMUser – The request was made with the credentials of an IAM user. - AssumedRole – The request was made with temporary security credentials that were obtained with a role via a call to the AWS Security Token Service (AWS STS) AssumeRole API. This can include roles for Amazon EC2 and cross-account API access. - FederatedUser – The request was made with temporary security credentials that were obtained via a call to the AWS STS GetFederationToken API. The sessionIssuer element indicates if the API was called with root or IAM user credentials. - AWSAccount – The request was made by another AWS account. - AWSService – The request was made by an AWS account that belongs to an AWS service. For example, AWS Elastic Beanstalk assumes an IAM role in your account to call other AWS services on your behalf. """ return self["type"]`The type of identity. The following values are possible: - Root – The request was made with your AWS account credentials. If the userIdentity type is Root and you set an alias for your account, the userName field contains your account alias. For more information, see Your AWS Account ID and Its Alias.
- IAMUser – The request was made with the credentials of an IAM user.
- AssumedRole – The request was made with temporary security credentials that were obtained with a role via a call to the AWS Security Token Service (AWS STS) AssumeRole API. This can include roles for Amazon EC2 and cross-account API access.
- FederatedUser – The request was made with temporary security credentials that were obtained via a call to the AWS STS GetFederationToken API. The sessionIssuer element indicates if the API was called with root or IAM user credentials.
- AWSAccount – The request was made by another AWS account.
- AWSService – The request was made by an AWS account that belongs to an AWS service. For example, AWS Elastic Beanstalk assumes an IAM role in your account to call other AWS services on your behalf.
 
- `prop principal_id : str`
- 
## Expand source code`@property def principal_id(self) -> str: """The unique identifier for the identity that made the call. For requests made with temporary security credentials, this value includes the session name that is passed to the AssumeRole, AssumeRoleWithWebIdentity, or GetFederationToken API call.""" return self["principalId"]`The unique identifier for the identity that made the call. For requests made with temporary security credentials, this value includes the session name that is passed to the AssumeRole, AssumeRoleWithWebIdentity, or GetFederationToken API call. 
- `prop session_context :`- [S3ObjectSessionContext](#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectSessionContext)| None
- 
## Expand source code`@property def session_context(self) -> S3ObjectSessionContext | None: """If the request was made with temporary security credentials, this element provides information about the session that was created for those credentials.""" session_context = self.get("sessionContext") if session_context is None: return None return S3ObjectSessionContext(session_context)`If the request was made with temporary security credentials, this element provides information about the session that was created for those credentials. 
- `prop user_name : str`
- 
## Expand source code`@property def user_name(self) -> str: """The friendly name of the identity that made the call.""" return self["userName"]`The friendly name of the identity that made the call. 
 ### Inherited members
- `class S3ObjectUserRequest (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3ObjectUserRequest(DictWrapper): """Information about the original call to S3 Object Lambda.""" @property def url(self) -> str: """The decoded URL of the request as received by S3 Object Lambda, excluding any authorization-related query parameters.""" return self["url"] @property def headers(self) -> dict[str, str]: """A map of string to strings containing the HTTP headers and their values from the original call, excluding any authorization-related headers. If the same header appears multiple times, their values are combined into a comma-delimited list. The case of the original headers is retained in this map.""" return CaseInsensitiveDict(self["headers"])`Information about the original call to S3 Object Lambda. ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop headers : dict[str, str]`
- 
## Expand source code`@property def headers(self) -> dict[str, str]: """A map of string to strings containing the HTTP headers and their values from the original call, excluding any authorization-related headers. If the same header appears multiple times, their values are combined into a comma-delimited list. The case of the original headers is retained in this map.""" return CaseInsensitiveDict(self["headers"])`A map of string to strings containing the HTTP headers and their values from the original call, excluding any authorization-related headers. If the same header appears multiple times, their values are combined into a comma-delimited list. The case of the original headers is retained in this map. 
- `prop url : str`
- 
## Expand source code`@property def url(self) -> str: """The decoded URL of the request as received by S3 Object Lambda, excluding any authorization-related query parameters.""" return self["url"]`The decoded URL of the request as received by S3 Object Lambda, excluding any authorization-related query parameters. 
 ### Inherited members