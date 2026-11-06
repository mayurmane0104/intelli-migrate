# X-Ray examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_xray_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_xray_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with X-Ray.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-traces-get`.

- **AWS CLI**
- 
            
                    **To get a list of traces**The following `batch-get-traces`example retrieves a list of traces specified by an ID. The full trace includes a document for each segment, compiled from all of the segment documents received with the same trace ID.`aws xray batch-get-traces \ --trace-ids``1-5d82881a-0a9126e92a73e971eed891b9`Output: `{ "Traces": [ { "Id": "1-5d82881a-0a9126e92a73e971eed891b9", "Duration": 0.232, "Segments": [ { "Id": "54aff5735b12dd28", "Document": "{\"id\":\"54aff5735b12dd28\",\"name\":\"Scorekeep\",\"start_time\":1.568835610432E9,\"end_time\":1.568835610664E9,\"http\":{\"request\":{\"url\":\"http://scorekeep-env-1.m4fg2pfzpv.us-east-2.elasticbeanstalk.com/api/user\",\"method\":\"POST\",\"user_agent\":\"curl/7.59.0\",\"client_ip\":\"52.95.4.28\",\"x_forwarded_for\":true},\"response\":{\"status\":200}},\"aws\":{\"elastic_beanstalk\":{\"version_label\":\"Sample Application-1\",\"deployment_id\":3,\"environment_name\":\"Scorekeep-env-1\"},\"ec2\":{\"availability_zone\":\"us-east-2b\",\"instance_id\":\"i-0e3cf4d2de0f3f37a\"},\"xray\":{\"sdk_version\":\"1.1.0\",\"sdk\":\"X-Ray for Java\"}},\"service\":{\"runtime\":\"OpenJDK 64-Bit Server VM\",\"runtime_version\":\"1.8.0_222\"},\"trace_id\":\"1-5d82881a-0a9126e92a73e971eed891b9\",\"origin\":\"AWS::ElasticBeanstalk::Environment\",\"subsegments\":[{\"id\":\"2d6900034ccfe558\",\"name\":\"DynamoDB\",\"start_time\":1.568835610658E9,\"end_time\":1.568835610664E9,\"http\":{\"response\":{\"status\":200,\"content_length\":61}},\"aws\":{\"table_name\":\"scorekeep-user\",\"operation\":\"UpdateItem\",\"request_id\":\"TPEIDNDUROMLPOV17U4A79555NVV4KQNSO5AEMVJF66Q9ASUAAJG\",\"resource_names\":[\"scorekeep-user\"]},\"namespace\":\"aws\"}]}" }, { "Id": "0f278b6334c34e6b", "Document": "{\"id\":\"0f278b6334c34e6b\",\"name\":\"DynamoDB\",\"start_time\":1.568835610658E9,\"end_time\":1.568835610664E9,\"parent_id\":\"2d6900034ccfe558\",\"inferred\":true,\"http\":{\"response\":{\"status\":200,\"content_length\":61}},\"aws\":{\"table_name\":\"scorekeep-user\",\"operation\":\"UpdateItem\",\"request_id\":\"TPEIDNDUROMLPOV17U4A79555NVV4KQNSO5AEMVJF66Q9ASUAAJG\",\"resource_names\":[\"scorekeep-user\"]},\"trace_id\":\"1-5d82881a-0a9126e92a73e971eed891b9\",\"origin\":\"AWS::DynamoDB::Table\"}" } ] } ], "UnprocessedTraceIds": [] }`For more information, see [Using the AWS X-Ray API with the AWS CLI](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-tutorial.html)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [BatchTracesGet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/batch-traces-get.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-group`.

- **AWS CLI**
- 
            
                    **To create a group**The following `create-group`example creates a group resource named`AdminGroup`. The group gets a filter expression that defines the criteria of the group as a segment related to a specific service causing a fault or an error.`aws xray create-group \ --group-name``"AdminGroup"`\ --filter-expression "service(\"mydomain.com\") {fault OR error}"Output: `{ "GroupName": "AdminGroup", "GroupARN": "arn:aws:xray:us-west-2:123456789012:group/AdminGroup/123456789", "FilterExpression": "service(\"mydomain.com\") {fault OR error}" }`For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/create-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-sampling-rule`.

- **AWS CLI**
- 
            
                    **To create a sampling rule**The following `create-sampling-rule`example creates a rule to control sampling behavior for instrumented applications. The rules are provided by a JSON file. The majority of the sampling rule fields are required to create the rule.`aws xray create-sampling-rule \ --cli-input-json``file://9000-base-scorekeep.json`Contents of `9000-base-scorekeep.json`:`{ "SamplingRule": { "RuleName": "base-scorekeep", "ResourceARN": "*", "Priority": 9000, "FixedRate": 0.1, "ReservoirSize": 5, "ServiceName": "Scorekeep", "ServiceType": "*", "Host": "*", "HTTPMethod": "*", "URLPath": "*", "Version": 1 } }`Output: `{ "SamplingRuleRecord": { "SamplingRule": { "RuleName": "base-scorekeep", "RuleARN": "arn:aws:xray:us-west-2:123456789012:sampling-rule/base-scorekeep", "ResourceARN": "*", "Priority": 9000, "FixedRate": 0.1, "ReservoirSize": 5, "ServiceName": "Scorekeep", "ServiceType": "*", "Host": "*", "HTTPMethod": "*", "URLPath": "*", "Version": 1, "Attributes": {} }, "CreatedAt": 1530574410.0, "ModifiedAt": 1530574410.0 } }`For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [CreateSamplingRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/create-sampling-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-group`.

- **AWS CLI**
- 
            
                    **To delete a group**The following `delete-group`example deletes the specified group resource.`aws xray delete-group \ --group-name``"AdminGroup"`\ --group-arn`"arn:aws:xray:us-east-2:123456789012:group/AdminGroup/123456789"`This command produces no output. For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/delete-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-sampling-rule`.

- **AWS CLI**
- 
            
                    **To delete a sampling rule**The following `delete-sampling-rule`example deletes the specified sampling rule. You can specify the group by using either the group name or group ARN.`aws xray delete-sampling-rule \ --rule-name``polling-scorekeep`Output: `{ "SamplingRuleRecord": { "SamplingRule": { "RuleName": "polling-scorekeep", "RuleARN": "arn:aws:xray:us-west-2:123456789012:sampling-rule/polling-scorekeep", "ResourceARN": "*", "Priority": 5000, "FixedRate": 0.003, "ReservoirSize": 0, "ServiceName": "Scorekeep", "ServiceType": "*", "Host": "*", "HTTPMethod": "GET", "URLPath": "/api/state/*", "Version": 1, "Attributes": {} }, "CreatedAt": 1530574399.0, "ModifiedAt": 1530574399.0 } }`For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [DeleteSamplingRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/delete-sampling-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-encryption-config`.

- **AWS CLI**
- 
            
                    **To retrieve the encryption configuration**The following `get-encryption-config`example retrieves the current encryption configuration for your AWS X-Ray data.`aws xray get-encryption-config`Output: `{ "EncryptionConfig": { "KeyId": "ae4aa6d49-a4d8-9df9-a475-4ff6d7898456", "Status": "ACTIVE", "Type": "NONE" } }`For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [GetEncryptionConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-encryption-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-group`.

- **AWS CLI**
- 
            
                    **To retrieve a group**The following `get-group`example displays details for the specified group resource. The details include the group name, the group ARN, and the filter expression that defines the criteria for that group. Groups can also be retrieved by ARN.`aws xray get-group \ --group-name``"AdminGroup"`Output: `{ "Group": [ { "GroupName": "AdminGroup", "GroupARN": "arn:aws:xray:us-west-2:123456789012:group/AdminGroup/123456789", "FilterExpression": "service(\"mydomain.com\") {fault OR error}" } ] }`For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [GetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-groups`.

- **AWS CLI**
- 
            
                    **To retrieve all groups**The following example displays details for all active group. `aws xray get-groups`Output: `{ "Groups": [ { "GroupName": "AdminGroup", "GroupARN": "arn:aws:xray:us-west-2:123456789012:group/AdminGroup/123456789", "FilterExpression": "service(\"example.com\") {fault OR error}" }, { "GroupName": "SDETGroup", "GroupARN": "arn:aws:xray:us-west-2:123456789012:group/SDETGroup/987654321", "FilterExpression": "responsetime > 2" } ] }`For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [GetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sampling-rules`.

- **AWS CLI**
- 
            
                    **To retrieve all sampling rules**The following `get-sampling-rules`example displays details for all available sampling rules.:`aws xray get-sampling-rules`Output: `{ "SamplingRuleRecords": [ { "SamplingRule": { "RuleName": "Default", "RuleARN": "arn:aws:xray:us-east-1::sampling-rule/Default", "ResourceARN": "*", "Priority": 10000, "FixedRate": 0.01, "ReservoirSize": 0, "ServiceName": "*", "ServiceType": "*", "Host": "*", "HTTPMethod": "*", "URLPath": "*", "Version": 1, "Attributes": {} }, "CreatedAt": 0.0, "ModifiedAt": 1530558121.0 }, { "SamplingRule": { "RuleName": "base-scorekeep", "RuleARN": "arn:aws:xray:us-east-1::sampling-rule/base-scorekeep", "ResourceARN": "*", "Priority": 9000, "FixedRate": 0.1, "ReservoirSize": 2, "ServiceName": "Scorekeep", "ServiceType": "*", "Host": "*", "HTTPMethod": "*", "URLPath": "*", "Version": 1, "Attributes": {} }, "CreatedAt": 1530573954.0, "ModifiedAt": 1530920505.0 }, { "SamplingRule": { "RuleName": "polling-scorekeep", "RuleARN": "arn:aws:xray:us-east-1::sampling-rule/polling-scorekeep", "ResourceARN": "*", "Priority": 5000, "FixedRate": 0.003, "ReservoirSize": 0, "ServiceName": "Scorekeep", "ServiceType": "*", "Host": "*", "HTTPMethod": "GET", "URLPath": "/api/state/*", "Version": 1, "Attributes": {} }, "CreatedAt": 1530918163.0, "ModifiedAt": 1530918163.0 } ] }`For more information, see [Using Sampling Rules with the X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-sampling.html)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [GetSamplingRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-sampling-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sampling-targets`.

- **AWS CLI**
- 
            
                    **To request a sampling quota**The following `get-sampling-targets`example requests a sampling quota for rules that the service is using to sample requests. The response from AWS X-Ray includes a quota that can be used instead of borrowing from the reservoir.`aws xray get-sampling-targets \ --sampling-statistics-documents '``[ { "RuleName": "base-scorekeep", "ClientID": "ABCDEF1234567890ABCDEF10", "Timestamp": "2018-07-07T00:20:06, "RequestCount": 110, "SampledCount": 20, "BorrowCount": 10 }, { "RuleName": "polling-scorekeep", 31, "BorrowCount": 0 } ]`'Output: `{ "SamplingTargetDocuments": [ { "RuleName": "base-scorekeep", "FixedRate": 0.1, "ReservoirQuota": 2, "ReservoirQuotaTTL": 1530923107.0, "Interval": 10 }, { "RuleName": "polling-scorekeep", "FixedRate": 0.003, "ReservoirQuota": 0, "ReservoirQuotaTTL": 1530923107.0, "Interval": 10 } ], "LastRuleModification": 1530920505.0, "UnprocessedStatistics": [] }`For more information, see [Using Sampling Rules with the X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-sampling.html)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [GetSamplingTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-sampling-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-graph`.

- **AWS CLI**
- 
            
                    **To get a service graph**The following example displays a document within a specified time period that describes services processing incoming requests, and the downstream services that they call as a result.: `aws xray get-service-graph \ --start-time``1568835392.0`--end-time`1568835446.0`Output: `{ "Services": [ { "ReferenceId": 0, "Name": "Scorekeep", "Names": [ "Scorekeep" ], "Root": true, "Type": "AWS::ElasticBeanstalk::Environment", "State": "active", "StartTime": 1568835392.0, "EndTime": 1568835446.0, "Edges": [ { "ReferenceId": 1, "StartTime": 1568835392.0, "EndTime": 1568835446.0, "SummaryStatistics": { "OkCount": 14, "ErrorStatistics": { "ThrottleCount": 0, "OtherCount": 0, "TotalCount": 0 }, "FaultStatistics": { "OtherCount": 0, "TotalCount": 0 }, "TotalCount": 14, "TotalResponseTime": 0.13 }, "ResponseTimeHistogram": [ { "Value": 0.008, "Count": 1 }, { "Value": 0.005, "Count": 7 }, { "Value": 0.009, "Count": 1 }, { "Value": 0.021, "Count": 1 }, { "Value": 0.038, "Count": 1 }, { "Value": 0.007, "Count": 1 }, { "Value": 0.006, "Count": 2 } ], "Aliases": [] }, ... TRUNCATED FOR BREVITY ... ] } ], "StartTime": 1568835392.0, "EndTime": 1568835446.0, "ContainsOldGroupVersions": false }`For more information, see [Using the AWS X-Ray API with the AWS CLI](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-tutorial.html)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [GetServiceGraph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-service-graph.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-trace-summaries`.

- **AWS CLI**
- 
            
                    **To get a trace summary**The following `get-trace-summaries`example retrieves IDs and metadata for traces available within a specified time frame.`aws xray get-trace-summaries \ --start-time``1568835392.0`\ --end-time`1568835446.0`Output: `[ "http://scorekeep-env-1.123456789.us-east-2.elasticbeanstalk.com/api/move/VSAE93HF/GSSD2NTB/DP0PCC09", "http://scorekeep-env-1.123456789.us-east-2.elasticbeanstalk.com/api/move/GCQ2B35P/FREELDFT/4LRE643M", "http://scorekeep-env-1.123456789.us-east-2.elasticbeanstalk.com/api/game/VSAE93HF/GSSD2NTB/starttime/1568835513", "http://scorekeep-env-1.123456789.us-east-2.elasticbeanstalk.com/api/move/4MQNA5NN/L99KK2RF/null" ]`For more information, see [Using the AWS X-Ray API with the AWS CLI](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-tutorial.html)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [GetTraceSummaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-trace-summaries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-encryption-config`.

- **AWS CLI**
- 
            
                    **To update the encryption configuration**The following `put-encryption-config``example updates the encryption configuration for AWS X-Ray data to use the default AWS managed KMS key ``aws/xray`.`aws xray put-encryption-config \ --type``KMS`\ --key-id`alias/aws/xray`Output: `{ "EncryptionConfig": { "KeyId": "arn:aws:kms:us-west-2:123456789012:key/c234g4e8-39e9-4gb0-84e2-b0ea215cbba5", "Status": "UPDATING", "Type": "KMS" } }`For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [PutEncryptionConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/put-encryption-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-trace-segments`.

- **AWS CLI**
- 
            
                    **To upload a segment**The following `put-trace-segments`example uploads segment documents to AWS X-Ray. The segment document is consumed as a list of JSON segment documents.`aws xray put-trace-segments \ --trace-segment-documents "{\"id\":\"20312a0e2b8809f4\",\"name\":\"DynamoDB\",\"trace_id\":\"1-5832862d-a43aafded3334a971fe312db\",\"start_time\":1.479706157195E9,\"end_time\":1.479706157202E9,\"parent_id\":\"79736b962fe3239e\",\"http\":{\"response\":{\"content_length\":60,\"status\":200}},\"inferred\":true,\"aws\":{\"consistent_read\":false,\"table_name\":\"scorekeep-session-xray\",\"operation\":\"GetItem\",\"request_id\":\"SCAU23OM6M8FO38UASGC7785ARVV4KQNSO5AEMVJF66Q9ASUAAJG\",\"resource_names\":[\"scorekeep-session-xray\"]},\"origin\":\"AWS::DynamoDB::Table\"}"`Output: `{ "UnprocessedTraceSegments": [] }`For more information, see [Sending Trace Data to AWS X-Ray](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-sendingdata.html#xray-api-segments)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [PutTraceSegments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/put-trace-segments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-group`.

- **AWS CLI**
- 
            
                    **To update a group**The following `update-group`example updates the criteria by which to accept traces into the group named`AdminGroup`. You can specify the desired group by using either the group name or group ARN.`aws xray update-group \ --group-name``"AdminGroup"`\ --group-arn`"arn:aws:xray:us-west-2:123456789012:group/AdminGroup/123456789"`\ --filter-expression "service(\"mydomain.com\") {fault}"Output: `{ "GroupName": "AdminGroup", "GroupARN": "arn:aws:xray:us-east-2:123456789012:group/AdminGroup/123456789", "FilterExpression": "service(\"mydomain.com\") {fault}" }`For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [UpdateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/update-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-sampling-rule`.

- **AWS CLI**
- 
            
                    **To update a sampling rule**The following `update-sampling-rule`example modifies a sampling rule's configuration. The rules are consumed from a JSON file. Only the fields being updated are required.`aws xray update-sampling-rule \ --cli-input-json``file://1000-default.json`Contents of `1000-default.json`:`{ "SamplingRuleUpdate": { "RuleName": "Default", "FixedRate": 0.01, "ReservoirSize": 0 } }`Output: `{ "SamplingRuleRecords": [ { "SamplingRule": { "RuleName": "Default", "RuleARN": "arn:aws:xray:us-west-2:123456789012:sampling-rule/Default", "ResourceARN": "*", "Priority": 10000, "FixedRate": 0.01, "ReservoirSize": 0, "ServiceName": "*", "ServiceType": "*", "Host": "*", "HTTPMethod": "*", "URLPath": "*", "Version": 1, "Attributes": {} }, "CreatedAt": 0.0, "ModifiedAt": 1529959993.0 } ] }`For more information, see [Configuring Sampling, Groups, and Encryption Settings with the AWS X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-configuration.html#xray-api-configuration-sampling)in the*AWS X-Ray Developer Guide*.- 
                    For API details, see [UpdateSamplingRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/update-sampling-rule.html)in*AWS CLI Command Reference*.
 
-