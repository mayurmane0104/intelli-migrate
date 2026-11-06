# Cloud Control API examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudcontrol_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudcontrol_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Cloud Control API.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-resource`.

- **AWS CLI**
- 
            
                    **To create a resource**The following `create-resource`example creates an AWS::Kinesis::Stream resource, named ResourceExample, with a retention period of 168 hours and a shard count of three.`aws cloudcontrol create-resource \ --type-name``AWS::Kinesis::Stream`\ --desired-state "{\"Name\": \"ResourceExample\",\"RetentionPeriodHours\":168, \"ShardCount\":3}"Output: `{ "ProgressEvent": { "EventTime": 1632506656.706, "TypeName": "AWS::Kinesis::Stream", "OperationStatus": "IN_PROGRESS", "Operation": "CREATE", "Identifier": "ResourceExample", "RequestToken": "20999d87-e304-4725-ad84-832dcbfd7fc5" } }`For more information, see [Creating a resource](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-create.html)in the*Cloud Control API User Guide*.- 
                    For API details, see [CreateResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/create-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource`.

- **AWS CLI**
- 
            
                    **To delete a resource**The following `delete-resource`example deletes a AWS::Kinesis::Stream resource with the identifier ResourceExample from your AWS account.`aws cloudcontrol delete-resource \ --type-name``AWS::Kinesis::Stream`\ --identifier`ResourceExample`Output: `{ "ProgressEvent": { "TypeName": "AWS::Kinesis::Stream", "Identifier": "ResourceExample", "RequestToken": "e48f26ff-d0f9-4ab8-a878-120db1edf111", "Operation": "DELETE", "OperationStatus": "IN_PROGRESS", "EventTime": 1632950300.14 } }`For more information, see [Deleting a resource](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-delete.html)in the*Cloud Control API User Guide*.- 
                    For API details, see [DeleteResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/delete-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-request-status`.

- **AWS CLI**
- 
            
                    **To get the status information of a resource request**The following `get-resource-request-status`example returns status information about the specified resource request.`aws cloudcontrol get-resource-request-status \ --request-token``"e1a6b86e-46bd-41ac-bfba-001234567890"`Output: `{ "ProgressEvent": { "TypeName": "AWS::Kinesis::Stream", "Identifier": "Demo", "RequestToken": "e1a6b86e-46bd-41ac-bfba-001234567890", "Operation": "CREATE", "OperationStatus": "FAILED", "EventTime": 1632950268.481, "StatusMessage": "Resource of type 'AWS::Kinesis::Stream' with identifier 'Demo' already exists.", "ErrorCode": "AlreadyExists" } }`For more information, see [Managing resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html)in the*Cloud Control API User Guide*.- 
                    For API details, see [GetResourceRequestStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/get-resource-request-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource`.

- **AWS CLI**
- 
            
                    **To get the current state of a resource**The following `get-resource`example returns the current state of the AWS::Kinesis::Stream resource named ResourceExample.`aws cloudcontrol get-resource \ --type-name``AWS::Kinesis::Stream`\ --identifier`ResourceExample`Output: `{ "TypeName": "AWS::Kinesis::Stream", "ResourceDescription": { "Identifier": "ResourceExample", "Properties": "{\"Arn\":\"arn:aws:kinesis:us-west-2:099908667365:stream/ResourceExample\",\"RetentionPeriodHours\":168,\"Name\":\"ResourceExample\",\"ShardCount\":3}" } }`For more information, see [Reading a resource's current state](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-read.html)in the*Cloud Control API User Guide*.- 
                    For API details, see [GetResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/get-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-requests`.

- **AWS CLI**
- 
            
                    **To list the active resource operation requests**The following `list-resource-requests`example lists the resource requests for CREATE and UPDATE operations that have failed in your AWS account.`aws cloudcontrol list-resource-requests \ --resource-request-status-filter``Operations=CREATE,OperationStatuses=FAILED`Output: `{ "ResourceRequestStatusSummaries": [ { "TypeName": "AWS::Kinesis::Stream", "Identifier": "Demo", "RequestToken": "e1a6b86e-46bd-41ac-bfba-633abcdfdbd7", "Operation": "CREATE", "OperationStatus": "FAILED", "EventTime": 1632950268.481, "StatusMessage": "Resource of type 'AWS::Kinesis::Stream' with identifier 'Demo' already exists.", "ErrorCode": "AlreadyExists" } ] }`For more information, see [Managing resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html)in the*Cloud Control API User Guide*.- 
                    For API details, see [ListResourceRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/list-resource-requests.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resources`.

- **AWS CLI**
- 
            
                    **To list the resources of a given type**The following `list-resources`example lists the AWS::Kinesis::Stream resources provisioned in your AWS account.`aws cloudcontrol list-resources \ --type-name``AWS::Kinesis::Stream`Output: `{ "TypeName": "AWS::Kinesis::Stream", "ResourceDescriptions": [ { "Identifier": "MyKinesisStream", "Properties": "{\"Name\":\"MyKinesisStream\"}" }, { "Identifier": "AnotherStream", "Properties": "{\"Name\":\"AnotherStream\"}" } ] }`For more information, see [Discovering resources](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-list.html)in the*Cloud Control API User Guide*.- 
                    For API details, see [ListResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/list-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-resource`.

- **AWS CLI**
- 
            
                    **To update the properties of an existing resource**The following `update-resource`example updates the retention policy of an AWS::Logs::LogGroup resource named ExampleLogGroup to 90 days.`aws cloudcontrol update-resource \ --type-name``AWS::Logs::LogGroup`\ --identifier`ExampleLogGroup`\ --patch-document "[{\"op\":\"replace\",\"path\":\"/RetentionInDays\",\"value\":90}]"Output: `{ "ProgressEvent": { "EventTime": "2021-08-09T18:17:15.219Z", "TypeName": "AWS::Logs::LogGroup", "OperationStatus": "IN_PROGRESS", "Operation": "UPDATE", "Identifier": "ExampleLogGroup", "RequestToken": "5f40c577-3534-4b20-9599-0b0123456789" } }`For more information, see [Updating a resource](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-update.html)in the*Cloud Control API User Guide*.- 
                    For API details, see [UpdateResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/update-resource.html)in*AWS CLI Command Reference*.
 
-