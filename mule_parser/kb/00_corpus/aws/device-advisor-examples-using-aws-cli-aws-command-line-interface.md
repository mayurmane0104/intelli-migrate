# Device Advisor examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_iotdeviceadvisor_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_iotdeviceadvisor_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Device Advisor.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-suite-definition`.

- **AWS CLI**
- 
            
                    **Example 1: To create an IoT Device Advisor test suite**The following `create-suite-definition`example creates a device advisor test suite in the AWS IoT with the specified suite definition configuration.`aws iotdeviceadvisor create-suite-definition \ --suite-definition-configuration '``{ \ "suiteDefinitionName": "TestSuiteName", \ "devices": [{"thingArn":"arn:aws:iot:us-east-1:123456789012:thing/MyIotThing"}], \ "intendedForQualification": false, \ "rootGroup": "{\"configuration\":{},\"tests\":[{\"name\":\"MQTT Connect\",\"configuration\":{\"EXECUTION_TIMEOUT\":120},\"tests\":[{\"name\":\"MQTT_Connect\",\"configuration\":{},\"test\":{\"id\":\"MQTT_Connect\",\"testCase\":null,\"version\":\"0.0.0\"}}]}]}", \ "devicePermissionRoleArn": "arn:aws:iam::123456789012:role/Myrole"}`'Output: `{ "suiteDefinitionId": "0jtsgio7yenu", "suiteDefinitionArn": "arn:aws:iotdeviceadvisor:us-east-1:123456789012:suitedefinition/0jtsgio7yenu", "suiteDefinitionName": "TestSuiteName", "createdAt": "2022-12-02T11:38:13.263000-05:00" }`For more information, see [Create a test suite definition](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-create-suite-definition)in the*AWS IoT Core Developer Guide*.**Example 2: To create an IoT Device Advisor Latest Qualification test suite**The following `create-suite-definition`example creates a device advisor qualification test suite with the latest version in the AWS IoT with the specified suite definition configuration.`aws iotdeviceadvisor create-suite-definition \ --suite-definition-configuration '``{ \ "suiteDefinitionName": "TestSuiteName", \ "devices": [{"thingArn":"arn:aws:iot:us-east-1:123456789012:thing/MyIotThing"}], \ "intendedForQualification": true, \ "rootGroup": "", \ "devicePermissionRoleArn": "arn:aws:iam::123456789012:role/Myrole"}`'Output: `{ "suiteDefinitionId": "txgsuolk2myj", "suiteDefinitionArn": "arn:aws:iotdeviceadvisor:us-east-1:123456789012:suitedefinition/txgsuolk2myj", "suiteDefinitionName": "TestSuiteName", "createdAt": "2022-12-02T11:38:13.263000-05:00" }`For more information, see [Create a test suite definition](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-create-suite-definition)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [CreateSuiteDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/create-suite-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-suite-definition`.

- **AWS CLI**
- 
            
                    **To delete the IoT Device Advisor test suite**The following `delete-suite-definition`example deletes the device advisor test suite with the specified suite definition ID.`aws iotdeviceadvisor delete-suite-definition \ --suite-definition-id``0jtsgio7yenu`This command produces no output. For more information, see [DeleteSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_DeleteSuiteDefinition.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DeleteSuiteDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/delete-suite-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-endpoint`.

- **AWS CLI**
- 
            
                    **Example 1: To get the information about an IoT Device Advisor Account-level endpoint**The following `get-endpoint`example gets the information about a device advisor Account-level test endpoint.`aws iotdeviceadvisor get-endpoint`Output: `{ "endpoint": "t6y4c143x9sfo.deviceadvisor.iot.us-east-1.amazonaws.com" }`**Example 2: To get the information about an IoT Device Advisor Device-level endpoint**The following `get-endpoint`example gets the information about a device advisor device-level test endpoint with the specified thing-arn or certificate-arn.`aws iotdeviceadvisor get-endpoint \ --thing-arn``arn:aws:iot:us-east-1:123456789012:thing/MyIotThing`Output: `{ "endpoint": "tdb7719be5t6y4c143x9sfo.deviceadvisor.iot.us-east-1.amazonaws.com" }`For more information, see [Get a test endpoint](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-get-test-endpoint)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [GetEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/get-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-suite-definition`.

- **AWS CLI**
- 
            
                    **To get the information about an IoT Device Advisor test suite**The following `get-suite-definition`example get the information about a aevice advisor test suite with the specified suite definition ID.`aws iotdeviceadvisor get-suite-definition \ --suite-definition-id``qqcsmtyyjabl`Output: `{ "suiteDefinitionId": "qqcsmtyyjabl", "suiteDefinitionArn": "arn:aws:iotdeviceadvisor:us-east-1:123456789012:suitedefinition/qqcsmtyyjabl", "suiteDefinitionVersion": "v1", "latestVersion": "v1", "suiteDefinitionConfiguration": { "suiteDefinitionName": "MQTT connection", "devices": [], "intendedForQualification": false, "isLongDurationTest": false, "rootGroup": "{\"configuration\":{},\"tests\":[{\"id\":\"uta5d9j1kvwc\",\"name\":\"Test group 1\",\"configuration\":{},\"tests\":[{\"id\":\"awr8pq5vc9yp\",\"name\":\"MQTT Connect\",\"configuration\":{},\"test\":{\"id\":\"MQTT_Connect\",\"testCase\":null,\"version\":\"0.0.0\"}}]}]}", "devicePermissionRoleArn": "arn:aws:iam::123456789012:role/Myrole", "protocol": "MqttV3_1_1" }, "createdAt": "2022-11-11T22:28:52.389000-05:00", "lastModifiedAt": "2022-11-11T22:28:52.389000-05:00", "tags": {} }`For more information, see [Get a test suite definition](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-create-suite-definition)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [GetSuiteDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/get-suite-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-suite-run-report`.

- **AWS CLI**
- 
            
                    **To get the information about an IoT Device Advisor qualifying test suite run report**The following `get-suite-run-report`example gets the report download link for a successful device advisor qualifying test suite run with the specified suite definition ID and suite run ID.`aws iotdeviceadvisor get-suite-run-report \ --suite-definition-id``ztvb5aek4w4x`\ --suite-run-id`p6awv83nre6v`Output: `{ "qualificationReportDownloadUrl": "https://senate-apn-reports-us-east-1-prod.s3.amazonaws.com/report.downloadlink" }`For more information, see [Get a qualification report for a successful qualification test suite run](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-qualification-report)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [GetSuiteRunReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/get-suite-run-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-suite-run`.

- **AWS CLI**
- 
            
                    **To get the information about an IoT Device Advisor test suite run status**The following `get-suite-run`example gets the information about a device advisor test suite run status with the specified suite definition ID and suite run ID.`aws iotdeviceadvisor get-suite-run \ --suite-definition-id``qqcsmtyyjabl`\ --suite-run-id`nzlfyhaa18oa`Output: `{ "suiteDefinitionId": "qqcsmtyyjabl", "suiteDefinitionVersion": "v1", "suiteRunId": "nzlfyhaa18oa", "suiteRunArn": "arn:aws:iotdeviceadvisor:us-east-1:123456789012:suiterun/qqcsmtyyjabl/nzlfyhaa18oa", "suiteRunConfiguration": { "primaryDevice": { "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/MyIotThing", "certificateArn": "arn:aws:iot:us-east-1:123456789012:cert/certFile" }, "parallelRun": false }, "testResult": { "groups": [ { "groupId": "uta5d9j1kvwc", "groupName": "Test group 1", "tests": [ { "testCaseRunId": "2ve2twrqyr0s", "testCaseDefinitionId": "awr8pq5vc9yp", "testCaseDefinitionName": "MQTT Connect", "status": "PASS", "startTime": "2022-11-12T00:01:53.693000-05:00", "endTime": "2022-11-12T00:02:15.443000-05:00", "logUrl": "https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logEventViewer:group=/aws/iot/deviceadvisor/qqcsmtyyjabl;stream=nzlfyhaa18oa_2ve2twrqyr0s", "warnings": "null", "failure": "null" } ] } ] }, "startTime": "2022-11-12T00:01:52.673000-05:00", "endTime": "2022-11-12T00:02:16.496000-05:00", "status": "PASS", "tags": {} }`For more information, see [Get a test suite run](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-describe-suite)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [GetSuiteRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/get-suite-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-suite-definitions`.

- **AWS CLI**
- 
            
                    **Example 1: To list the IoT Device Advisor test suites you created**The following `list-suite-definitions`example lists up to 25 device advisor test suites you created in AWS IoT. If you have more than 25 test suites, the "nextToken" will be shown in the output. You can use this "nextToken" to show the rest of the test suites you created.`aws iotdeviceadvisor list-suite-definitions`Output: `{ "suiteDefinitionInformationList": [ { "suiteDefinitionId": "3hsn88h4p2g5", "suiteDefinitionName": "TestSuite1", "defaultDevices": [ { "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/MyIotThing" } ], "intendedForQualification": false, "isLongDurationTest": false, "protocol": "MqttV3_1_1", "createdAt": "2022-11-17T14:15:56.830000-05:00" }, { ...... } ], "nextToken": "nextTokenValue" }`**Example 2: To list the IoT Device Advisor test suites you created with the specified settings**The following `list-suite-definitions`example lists device advisor test suites you created in AWS IoT with the specified max-result number. If you have more test suites than the max number, the "nextToken" will be shown in the output. If you have "nextToken", you can use "nextToken" to show the test suites you created that weren't shown before.`aws iotdeviceadvisor list-suite-definitions \ --max-result``1`\ --next-token`"nextTokenValue"`Output: `{ "suiteDefinitionInformationList": [ { "suiteDefinitionId": "ztvb5aew4w4x", "suiteDefinitionName": "TestSuite2", "defaultDevices": [], "intendedForQualification": true, "isLongDurationTest": false, "protocol": "MqttV3_1_1", "createdAt": "2022-11-17T14:15:56.830000-05:00" } ], "nextToken": "nextTokenValue" }`For more information, see [ListSuiteDefinitions](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListSuiteDefinitions.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListSuiteDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/list-suite-definitions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-suite-runs`.

- **AWS CLI**
- 
            
                    **Example 1: To list all information about the specified IoT Device Advisor test suite runs status**The following `list-suite-runs`example lists all information about a device advisor test suite runs status with the specified suite definition ID. If you have more than 25 test suite runs, the "nextToken" will be shown in the output. You can use this "nextToken" to show the rest of the test suite runs.`aws iotdeviceadvisor list-suite-runs \ --suite-definition-id``ztvb5aew4w4x`Output: `{ "suiteRunsList": [ { "suiteDefinitionId": "ztvb5aew4w4x", "suiteDefinitionVersion": "v1", "suiteDefinitionName": "TestSuite", "suiteRunId": "p6awv89nre6v", "createdAt": "2022-12-01T16:33:14.212000-05:00", "startedAt": "2022-12-01T16:33:15.710000-05:00", "endAt": "2022-12-01T16:42:03.323000-05:00", "status": "PASS", "passed": 6, "failed": 0 } ] }`**Example 2: To list information about the specified IoT Device Advisor test suite runs status with the specified settings**The following `list-suite-runs`example lists information about a device advisor test suite runs status with the specified suite definition ID and the specified max-result number. If you have more test suite runs than the max number, the "nextToken" will be shown in the output. If you have "nextToken", you can use "nextToken" to show the test suite runs that weren't shown before.`aws iotdeviceadvisor list-suite-runs \ --suite-definition-id``qqcsmtyyjaml`\ --max-result`1`\ --next-token`"nextTokenValue"`Output: `{ "suiteRunsList": [ { "suiteDefinitionId": "qqcsmtyyjaml", "suiteDefinitionVersion": "v1", "suiteDefinitionName": "MQTT connection", "suiteRunId": "gz9vm2s6d2jy", "createdAt": "2022-12-01T20:10:27.079000-05:00", "startedAt": "2022-12-01T20:10:28.003000-05:00", "endAt": "2022-12-01T20:10:45.084000-05:00", "status": "STOPPED", "passed": 0, "failed": 0 } ], "nextToken": "nextTokenValue" }`For more information, see [ListSuiteRuns](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListSuiteRuns.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListSuiteRuns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/list-suite-runs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags attached to an IoT Device Advisor resource**The following `list-tags-for-resource`example lists the tags attached to a device advisor resource. The device advisor resource can be a Suitedefinition-Arn or a Suiterun-Arn.`aws iotdeviceadvisor list-tags-for-resource \ --resource-arn``arn:aws:iotdeviceadvisor:us-east-1:123456789012:suitedefinition/ba0uyjpg38ny`Output: `{ "tags": { "TestTagKey": "TestTagValue" } }`For more information, see [ListTagsForResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListTagsForResource.html)in the*AWS IoT API Reference*and[Resource types defined by AWS IoT Core Device Advisor](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotcoredeviceadvisor.html#awsiotcoredeviceadvisor-resources-for-iam-policies)in the*Service Authorization Reference*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-suite-run`.

- **AWS CLI**
- 
            
                    **To start an IoT Device Advisor test suite run**The following `start-suite-run`example lists the available widgets in your AWS account.`aws iotdeviceadvisor start-suite-run \ --suite-definition-id``qqcsmtyyjabl`\ --suite-definition-version`v1`\ --suite-run-configuration '`{"primaryDevice":{"thingArn": "arn:aws:iot:us-east-1:123456789012:thing/MyIotThing","certificateArn":"arn:aws:iot:us-east-1:123456789012:cert/certFile"}}`'Output: `{ "suiteRunId": "pwmucgw7lt9s", "suiteRunArn": "arn:aws:iotdeviceadvisor:us-east-1:123456789012:suiterun/qqcsmtyyjabl/pwmucgw7lk9s", "createdAt": "2022-12-02T15:43:05.581000-05:00" }`For more information, see [Start a test suite run](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-start-suite-run)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [StartSuiteRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/start-suite-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-suite-run`.

- **AWS CLI**
- 
            
                    **To stop an IoT Device Advisor test suite that is currently running**The following `stop-suite-run`example stops a device advisor test suite that is currently running with the specified suite definition ID and suite run ID.`aws iotdeviceadvisor stop-suite-run \ --suite-definition-id``qqcsmtyyjabl`\ --suite-run-id`nzlfyhaa18oa`This command produces no output. For more information, see [Stop a test suite run](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-stop-suite-run)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [StopSuiteRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/stop-suite-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add to and modify the existing tags of an IoT Device Advisor resource**The following `tag-resource`example adds to and modifies the existing tags of a device advisor resource with the specified resource arn and tags. The device advisor resource can be a Suitedefinition-Arn or a Suiterun-Arn.`aws iotdeviceadvisor tag-resource \ --resource-arn``arn:aws:iotdeviceadvisor:us-east-1:123456789012:suitedefinition/ba0uyjpg38ny`\ --tags '`{"TagKey": "TagValue"}`'This command produces no output. For more information, see [TagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_TagResource.html)in the*AWS IoT API Reference*and[Resource types defined by AWS IoT Core Device Advisor](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotcoredeviceadvisor.html#awsiotcoredeviceadvisor-resources-for-iam-policies)in the*Service Authorization Reference*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove the existing tags from an IoT Device Advisor resource**The following `untag-resource`example removes the existing tags from a device advisor resource with the specified resource arn and tag key. The device advisor resource can be a Suitedefinition-Arn or a Suiterun-Arn.`aws iotdeviceadvisor untag-resource \ --resource-arn``arn:aws:iotdeviceadvisor:us-east-1:123456789012:suitedefinition/ba0uyjpg38ny`\ --tag-keys`"TagKey"`This command produces no output. For more information, see [UntagResource](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_UntagResource.html)in the*AWS IoT API Reference*and[Resource types defined by AWS IoT Core Device Advisor](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotcoredeviceadvisor.html#awsiotcoredeviceadvisor-resources-for-iam-policies)in the*Service Authorization Reference*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-suite-definition`.

- **AWS CLI**
- 
            
                    **Example 1: To update an IoT Device Advisor test suite**The following `update-suite-definition`example updates a device advisor test suite in the AWS IoT with the specified suite definition ID and suite definition configuration.`aws iotdeviceadvisor update-suite-definition \ --suite-definition-id``3hsn88h4p2g5`\ --suite-definition-configuration '`{ \ "suiteDefinitionName": "TestSuiteName", \ "devices": [{"thingArn":"arn:aws:iot:us-east-1:123456789012:thing/MyIotThing"}], \ "intendedForQualification": false, \ "rootGroup": "{\"configuration\":{},\"tests\":[{\"name\":\"MQTT Connect\",\"configuration\":{\"EXECUTION_TIMEOUT\":120},\"tests\":[{\"name\":\"MQTT_Connect\",\"configuration\":{},\"test\":{\"id\":\"MQTT_Connect\",\"testCase\":null,\"version\":\"0.0.0\"}}]}]}", \ "devicePermissionRoleArn": "arn:aws:iam::123456789012:role/Myrole"}`'Output: `{ "suiteDefinitionId": "3hsn88h4p2g5", "suiteDefinitionName": "TestSuiteName", "suiteDefinitionVersion": "v3", "createdAt": "2022-11-17T14:15:56.830000-05:00", "lastUpdatedAt": "2022-12-02T16:02:45.857000-05:00" }`**Example 2: To update an IoT Device Advisor Qualification test suite**The following `update-suite-definition`example updates a device advisor qualification test suite in the AWS IoT with the specified suite definition ID and suite definition configuration.`aws iotdeviceadvisor update-suite-definition \ --suite-definition-id``txgsuolk2myj`\ --suite-definition-configuration '`{ "suiteDefinitionName": "TestSuiteName", \ "devices": [{"thingArn":"arn:aws:iot:us-east-1:123456789012:thing/MyIotThing"}], \ "intendedForQualification": true, \ "rootGroup": "", \ "devicePermissionRoleArn": "arn:aws:iam::123456789012:role/Myrole"}`'Output: `{ "suiteDefinitionId": "txgsuolk2myj", "suiteDefinitionName": "TestSuiteName", "suiteDefinitionVersion": "v3", "createdAt": "2022-11-17T14:15:56.830000-05:00", "lastUpdatedAt": "2022-12-02T16:02:45.857000-05:00" }`For more information, see [UpdateSuiteDefinition](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_UpdateSuiteDefinition.html)in the*AWS IoT API Reference*.- 
                    For API details, see [UpdateSuiteDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/update-suite-definition.html)in*AWS CLI Command Reference*.
 
-