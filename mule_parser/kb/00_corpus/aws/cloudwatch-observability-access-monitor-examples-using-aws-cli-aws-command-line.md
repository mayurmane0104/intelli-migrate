# CloudWatch Observability Access Monitor examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_oam_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_oam_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CloudWatch Observability Access Monitor.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-link`.

- **AWS CLI**
- 
            
                    **To create a link**The following `create-link`example creates a link between a source account and a sink that you have created in a monitoring account.`aws oam create-link \ --label-template``sourceAccount`\ --resource-types`AWS::CloudWatch::Metric`\ --sink-identifier`arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`Output: `{ "Arn": "arn:aws:oam:us-east-2:123456789111:link/a1b2c3d4-5678-90ab-cdef-example11111", "Id": "a1b2c3d4-5678-90ab-cdef-example11111", "Label": "sourceAccount", "LabelTemplate": "sourceAccount", "ResourceTypes": [ "AWS::CloudWatch::Metric" ], "SinkArn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345", "Tags": {} }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [CreateLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/create-link.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-sink`.

- **AWS CLI**
- 
            
                    **To create a sink**The following `create-sink`example creates a sink in the current account, so that it can be used as a monitoring account in CloudWatch cross-account observability.`aws oam create-sink \ --name``DemoSink`Output: `{ "Arn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345", "Id": "a1b2c3d4-5678-90ab-cdef-example12345", "Name": "DemoSink", "Tags": {} }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [CreateSink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/create-sink.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-link`.

- **AWS CLI**
- 
            
                    **To delete a link**The following `delete-link`example deletes a link between a monitoring account sink and a source account.`aws oam delete-link \ --identifier``arn:aws:oam:us-east-2:123456789111:link/a1b2c3d4-5678-90ab-cdef-example11111`This command produces no output. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/delete-link.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-sink`.

- **AWS CLI**
- 
            
                    **To delete a sink**The following `delete-sink`example deletes a sink. You must delete all links to a sink before you can delete that sink.`aws oam delete-sink \ --identifier``arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`This command produces no output. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteSink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/delete-sink.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-link`.

- **AWS CLI**
- 
            
                    **To return complete information about one link**The following `get-link`example returns complete information about a link.`aws oam get-link \ --identifier``arn:aws:oam:us-east-2:123456789111:link/a1b2c3d4-5678-90ab-cdef-example11111`Output: `{ "Arn": "arn:aws:oam:us-east-2:123456789111:link/a1b2c3d4-5678-90ab-cdef-example11111", "Id": "a1b2c3d4-5678-90ab-cdef-example11111", "Label": "sourceAccount", "LabelTemplate": "sourceAccount", "ResourceTypes": [ "AWS::CloudWatch::Metric" ], "SinkArn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345", "Tags": {} }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/get-link.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sink-policy`.

- **AWS CLI**
- 
            
                    **To return the current sink policy attached to the sink**The following `get-sink-policy`example returns the current sink policy attached to the sink.`aws oam get-sink-policy \ --sink-identifier``arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`Output: `{ "SinkArn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345", "SinkId": "a1b2c3d4-5678-90ab-cdef-example12345", "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789111:root\"},\"Action\":[\"oam:CreateLink\",\"oam:UpdateLink\"],\"Resource\":\"*\",\"Condition\":{\"ForAllValues:StringEquals\":{\"oam:ResourceTypes\":[\"AWS::Logs::LogGroup\",\"AWS::CloudWatch::Metric\",\"AWS::XRay::Trace\",\"AWS::ApplicationInsights::Application\"]}}}]}" }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetSinkPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/get-sink-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sink`.

- **AWS CLI**
- 
            
                    **To return complete information about one monitoring account sink**The following `get-sink`example returns complete information about a monitoring account sink.`aws oam get-sink \ --identifier``arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`Output: `{ "Arn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345", "Id": "a1b2c3d4-5678-90ab-cdef-example12345", "Name": "DemoSink", "Tags": {} }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetSink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/get-sink.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-attached-links`.

- **AWS CLI**
- 
            
                    **To return a list of source account links that are linked to this monitoring account sink**The following `list-attached-links`example returns a list of source account links that are linked to this monitoring account sink.`aws oam list-attached-links \ --sink-identifier``arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`Output: `{ "Items": [{ "Label": "Monitoring account", "LinkArn": "arn:aws:oam:us-east-2:123456789111:link/a1b2c3d4-5678-90ab-cdef-example11111", "ResourceTypes": [ "AWS::ApplicationInsights::Application", "AWS::Logs::LogGroup", "AWS::CloudWatch::Metric", "AWS::XRay::Trace" ] }] }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListAttachedLinks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/list-attached-links.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-links`.

- **AWS CLI**
- 
            
                    **To return a list of links for one monitoring account sink**The following `list-links`example returns a list of links for one monitoring account sink. Run this operation in a source account to return a list of links to monitoring account sinks that this source account has.`aws oam list-links`Output: `{ "Items": [{ "Arn": "arn:aws:oam:us-east-2:123456789111:link/a1b2c3d4-5678-90ab-cdef-example11111", "Id": "a1b2c3d4-5678-90ab-cdef-example11111", "Label": "sourceAccount", "ResourceTypes": [ "AWS::CloudWatch::Metric" ], "SinkArn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345" }] }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListLinks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/list-links.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-sinks`.

- **AWS CLI**
- 
            
                    **To return the list of sinks created in the monitoring account**The following `list-sinks`example returns a list of sinks created in the monitoring account. Run this operation in a monitoring account.`aws oam list-sinks`Output: `{ "Items": [ { "Arn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345", "Id": "a1b2c3d4-5678-90ab-cdef-example12345", "Name": "DemoSink" } ] }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListSinks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/list-sinks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To display the tags associated with a resource**The following `list-tags-for-resource`example displays the tags associated with a sink.`aws oam list-tags-for-resource \ --resource-arn``arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`Output: `{ "Tags": { "Team": "Devops" } }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-sink-policy`.

- **AWS CLI**
- 
            
                    **To create or update the resource policy**The following `put-sink-policy`example creates the resource policy that grants permissions to source accounts to link to the monitoring account sink.`aws oam put-sink-policy \ --policy '``{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789111:root"},"Action":["oam:CreateLink","oam:UpdateLink"],"Resource":"*","Condition":{"ForAllValues:StringEquals":{"oam:ResourceTypes":["AWS::Logs::LogGroup","AWS::CloudWatch::Metric","AWS::XRay::Trace","AWS::ApplicationInsights::Application"]}}}]}`' \ --sink-identifier`arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`Output: `{ "SinkArn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345", "SinkId": "a1b2c3d4-5678-90ab-cdef-example12345", "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789111:root\"},\"Action\":[\"oam:CreateLink\",\"oam:UpdateLink\"],\"Resource\":\"*\",\"Condition\":{\"ForAllValues:StringEquals\":{\"oam:ResourceTypes\":[\"AWS::Logs::LogGroup\",\"AWS::CloudWatch::Metric\",\"AWS::XRay::Trace\",\"AWS::ApplicationInsights::Application\"]}}}]}" }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [PutSinkPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/put-sink-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To assign one or more tags to the specified resource**The following `tag-resource`example tags a sink`arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`.`aws oam tag-resource \ --resource-arn``arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`\ --tags`team=Devops`This command produces no output. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove one or more tags from the specified resource.**The following `untag-resource`example removes a tag with the key`team`from sink`arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345`.`aws oam untag-resource \ --resource-arn``arn:aws:oam:us-east-2:123456789012:sink/f3f42f60-f0f2-425c-1234-12347bdd821f`\ --tag-keys`team`This command produces no output. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-link`.

- **AWS CLI**
- 
            
                    **To change what types of data are shared from a source account to its linked monitoring account sink**The following `update-link`example updates the link`arn:aws:oam:us-east-2:123456789111:link/0123e691-e7ef-43fa-1234-c57c837fced0`with resource types`AWS::CloudWatch::Metric`and`AWS::Logs::LogGroup`.`aws oam update-link \ --identifier``arn:aws:oam:us-east-2:123456789111:link/a1b2c3d4-5678-90ab-cdef-example11111`\ --resource-types`"AWS::CloudWatch::Metric"``"AWS::Logs::LogGroup"`Output: `{ "Arn": "arn:aws:oam:us-east-2:123456789111:link/a1b2c3d4-5678-90ab-cdef-example11111", "Id": "a1b2c3d4-5678-90ab-cdef-example11111", "Label": "sourceAccount", "LabelTemplate": "sourceAccount", "ResourceTypes": [ "AWS::CloudWatch::Metric", "AWS::Logs::LogGroup" ], "SinkArn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345", "Tags": {} }`For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UpdateLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/update-link.html)in*AWS CLI Command Reference*.
 
-