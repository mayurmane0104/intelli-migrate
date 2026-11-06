# Network Flow Monitor examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_networkflowmonitor_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_networkflowmonitor_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Network Flow Monitor.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-monitor`.

- **AWS CLI**
- 
            
                    **To create a monitor**The following `create-monitor`example creates a monitor named`demo`in the specified account.`aws networkflowmonitor create-monitor \ --monitor-name``demo`\ --local-resources type="AWS::EC2::VPC",identifier="arn:aws:ec2:us-east-1:123456789012:vpc/vpc-03ea55eeda25adbb0" \ --scope-arn`arn:aws:networkflowmonitor:us-east-1:123456789012:scope/e21cda79-30a0-4c12-9299-d8629d76d8cf`Output: `{ "monitorArn": "arn:aws:networkflowmonitor:us-east-1:123456789012:monitor/demo", "monitorName": "demo", "monitorStatus": "ACTIVE", "tags": {} }`For more information, see [Create a monitor in Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-monitors-create.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [CreateMonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/create-monitor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-scope`.

- **AWS CLI**
- 
            
                    **To create a scope**The following `create-scope`example creates a scope that includes a set of resources for which Network Flow Monitor will generate network traffic metrics.`aws networkflowmonitor create-scope \ --targets '``[{"targetIdentifier":{"targetId":{"accountId":"123456789012"},"targetType":"ACCOUNT"},"region":"us-east-1"}]`'Output: `{ "scopeId": "97626f8d-8a21-4b5d-813a-1a0962dd4615", "status": "IN_PROGRESS", "tags": {} }`For more information, see [Components and features of Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-components.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [CreateScope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/create-scope.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-monitor`.

- **AWS CLI**
- 
            
                    **To delete a monitor**The following `delete-monitor`example deletes a monitor named`demo`in the specified account.`aws networkflowmonitor delete-monitor \ --monitor-name``demo`This command produces no output. For more information, see [Delete a monitor in Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-monitors-delete.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteMonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/delete-monitor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-scope`.

- **AWS CLI**
- 
            
                    **To delete a scope**The following `delete-scope`example deletes a specified scope.`aws networkflowmonitor delete-scope \ --scope-id``fdc20616-6bb4-4242-a24e-a748e65ca7ac`This command produces no output. For more information, see [Components and features of Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-components.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteScope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/delete-scope.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-monitor`.

- **AWS CLI**
- 
            
                    **To retrieve information about a monitor**The following `get-monitor`example displays information about the monitor named`demo`in the specified account.`aws networkflowmonitor get-monitor \ --monitor-name``Demo`Output: `{ "monitorArn": "arn:aws:networkflowmonitor:us-east-1:123456789012:monitor/Demo", "monitorName": "Demo", "monitorStatus": "ACTIVE", "localResources": [ { "type": "AWS::EC2::VPC", "identifier": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-03ea55eeda25adbb0" } ], "remoteResources": [], "createdAt": "2024-12-09T12:21:51.616000-06:00", "modifiedAt": "2024-12-09T12:21:55.412000-06:00", "tags": {} }`For more information, see [Components and features of Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-components.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetMonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-monitor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-query-results-workload-insights-top-contributors-data`.

- **AWS CLI**
- 
            
                    **To retrieve the top contributor data on workload insights**The following `get-query-results-workload-insights-top-contributors-data`example returns the data for the specified query.`aws networkflowmonitor get-query-results-workload-insights-top-contributors-data \ --scope-id``e21cda79-30a0-4c12-9299-d8629d76d8cf`\ --query-id`cc4f4ab3-3103-33b8-80ff-d6597a0c6cea`Output: `{ "datapoints": [ { "timestamps": [ "2024-12-09T19:00:00+00:00", "2024-12-09T19:05:00+00:00", "2024-12-09T19:10:00+00:00" ], "values": [ 259943.0, 194856.0, 216432.0 ], "label": "use1-az6" } ], "unit": "Bytes" }`For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetQueryResultsWorkloadInsightsTopContributorsData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-results-workload-insights-top-contributors-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-query-results-workload-insights-top-contributors`.

- **AWS CLI**
- 
            
                    **To retrieve the top contributors on workload insights**The following `get-query-results-workload-insights-top-contributors`example returns the data for the specified query.`aws networkflowmonitor get-query-results-workload-insights-top-contributors \ --scope-id``e21cda79-30a0-4c12-9299-d8629d76d8cf`\ --query-id`1fc423d3-b144-37a6-80e6-e2c7d26eea0c`Output: `{ "topContributors": [ { "accountId": "123456789012", "localSubnetId": "subnet-0a5b30fb95dca2c14", "localAz": "use1-az6", "localVpcId": "vpc-03ea55eeda25adbb0", "localRegion": "us-east-1", "remoteIdentifier": "", "value": 908443, "localSubnetArn": "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-0a5b30fb95dca2c14", "localVpcArn": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-03ea55eeda25adbb0" } ] }`For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetQueryResultsWorkloadInsightsTopContributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-results-workload-insights-top-contributors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-query-status-monitor-top-contributors`.

- **AWS CLI**
- 
            
                    **To retrieve the status of the query**The following `get-query-status-monitor-top-contributors`example displays the current status of the query in the specified account.`aws networkflowmonitor get-query-status-monitor-top-contributors \ --monitor-name``Demo`\ --query-id`5398eabd-bc40-3f5f-aba3-bcb639d3c7ca`Output: `{ "status": "SUCCEEDED" }`For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetQueryStatusMonitorTopContributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-status-monitor-top-contributors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-query-status-workload-insights-top-contributors-data`.

- **AWS CLI**
- 
            
                    **To retrieve the status of the query**The following `get-query-status-workload-insights-top-contributors-data`example displays the current status of the query in the specified account.`aws networkflowmonitor get-query-status-workload-insights-top-contributors-data \ --scope-id``e21cda79-30a0-4c12-9299-d8629d76d8cf`\ --query-id`4333754d-8ae1-3f29-b6b7-c36db2e7f8ac`Output: `{ "status": "SUCCEEDED" }`For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetQueryStatusWorkloadInsightsTopContributorsData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-status-workload-insights-top-contributors-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-query-status-workload-insights-top-contributors`.

- **AWS CLI**
- 
            
                    **To retrieve the status of the query**The following `get-query-status-workload-insights-top-contributors`example displays the current status of the query in the specified account.`aws networkflowmonitor get-query-status-workload-insights-top-contributors \ --scope-id``e21cda79-30a0-4c12-9299-d8629d76d8cf`\ --query-id`f2a87c70-3e5a-362e-8beb-4747d13d8419`Output: `{ "status": "SUCCEEDED" }`For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetQueryStatusWorkloadInsightsTopContributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-status-workload-insights-top-contributors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-scope`.

- **AWS CLI**
- 
            
                    **To retrieve information about a scope**The following `get-scope`example displays information about a scope, such as status, tags, name and target details.`aws networkflowmonitor get-scope \ --scope-id``e21cda79-30a0-4c12-9299-d8629d76d8cf`Output: `{ "scopeId": "e21cda79-30a0-4c12-9299-d8629d76d8cf", "status": "SUCCEEDED", "scopeArn": "arn:aws:networkflowmonitor:us-east-1:123456789012:scope/e21cda79-30a0-4c12-9299-d8629d76d8cf", "targets": [ { "targetIdentifier": { "targetId": { "accountId": "123456789012" }, "targetType": "ACCOUNT" }, "region": "us-east-1" } ], "tags": {} }`For more information, see [Components and features of Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-components.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetScope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-scope.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-monitors`.

- **AWS CLI**
- 
            
                    **To retrieve a list of monitors**The following `list-monitors`example returns returns all the monitors in the specified account.`aws networkflowmonitor list-monitors`Output: `{ "monitors": [ { "monitorArn": "arn:aws:networkflowmonitor:us-east-1:123456789012:monitor/Demo", "monitorName": "Demo", "monitorStatus": "ACTIVE" } ] }`For more information, see [Components and features of Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-components.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListMonitors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/list-monitors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-scopes`.

- **AWS CLI**
- 
            
                    **To retrieve a list of scopes**The following `list-scopes`example lists all scopes in the specified account.`aws networkflowmonitor list-scopes`Output: `{ "scopes": [ { "scopeId": "fdc20616-6bb4-4242-a24e-a748e65ca7ac", "status": "SUCCEEDED", "scopeArn": "arn:aws:networkflowmonitor:us-east-1:123456789012:scope/fdc20616-6bb4-4242-a24e-a748e65ca7ac" } ] }`For more information, see [Components and features of Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-components.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListScopes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/list-scopes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags**The following `list-tags-for-resource`example returns all the tags associated with the specified resource.`aws networkflowmonitor list-tags-for-resource \ --resource-arn``arn:aws:networkflowmonitor:us-east-1:123456789012:monitor/Demo`Output: `{ "tags": { "Value": "Production", "Key": "stack" } }`For more information, see [Tagging your Amazon CloudWatch resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-query-monitor-top-contributors`.

- **AWS CLI**
- 
            
                    **To start a query**The following `start-query-monitor-top-contributors`example starts the query which returns a query ID to retrieve the top contributors.`aws networkflowmonitor start-query-monitor-top-contributors \ --monitor-name``Demo`\ --start-time`2024-12-09T19:00:00Z`\ --end-time`2024-12-09T19:15:00Z`\ --metric-name`DATA_TRANSFERRED`\ --destination-category`UNCLASSIFIED`Output: `{ "queryId": "aecd3a88-0283-35b0-a17d-6e944dc8531d" }`For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StartQueryMonitorTopContributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/start-query-monitor-top-contributors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-query-workload-insights-top-contributors-data`.

- **AWS CLI**
- 
            
                    **To start a query**The following `start-query-workload-insights-top-contributors-data`example starts the query which returns a query ID to retrieve the top contributors.`aws networkflowmonitor start-query-workload-insights-top-contributors-data \ --scope-id``e21cda79-30a0-4c12-9299-d8629d76d8cf`\ --start-time`2024-12-09T19:00:00Z`\ --end-time`2024-12-09T19:15:00Z`\ --metric-name`DATA_TRANSFERRED`\ --destination-category`UNCLASSIFIED`Output: `{ "queryId": "cc4f4ab3-3103-33b8-80ff-d6597a0c6cea" }`For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StartQueryWorkloadInsightsTopContributorsData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/start-query-workload-insights-top-contributors-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-query-workload-insights-top-contributors`.

- **AWS CLI**
- 
            
                    **To start a query**The following `start-query-workload-insights-top-contributors`example starts the query which returns a query ID to retrieve the top contributors.`aws networkflowmonitor start-query-workload-insights-top-contributors \ --scope-id``e21cda79-30a0-4c12-9299-d8629d76d8cf`\ --start-time`2024-12-09T19:00:00Z`\ --end-time`2024-12-09T19:15:00Z`\ --metric-name`DATA_TRANSFERRED`\ --destination-category`UNCLASSIFIED`Output: `{ "queryId": "1fc423d3-b144-37a6-80e6-e2c7d26eea0c" }`For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StartQueryWorkloadInsightsTopContributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/start-query-workload-insights-top-contributors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-query-monitor-top-contributors`.

- **AWS CLI**
- 
            
                    **To stop a query**The following `stop-query-monitor-top-contributors`example stops the query in the specified account.`aws networkflowmonitor stop-query-monitor-top-contributors \ --monitor-name``Demo`\ --query-id`aecd3a88-0283-35b0-a17d-6e944dc8531d`This command produces no output. For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StopQueryMonitorTopContributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/stop-query-monitor-top-contributors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-query-workload-insights-top-contributors-data`.

- **AWS CLI**
- 
            
                    **To stop a query**The following `stop-query-workload-insights-top-contributors-data`example stops the query in the specified account.`aws networkflowmonitor stop-query-workload-insights-top-contributors-data \ --scope-id``e21cda79-30a0-4c12-9299-d8629d76d8cf`\ --query-id`cc4f4ab3-3103-33b8-80ff-d6597a0c6cea`This command produces no output. For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StopQueryWorkloadInsightsTopContributorsData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/stop-query-workload-insights-top-contributors-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-query-workload-insights-top-contributors`.

- **AWS CLI**
- 
            
                    **To stop a query**The following `stop-query-workload-insights-top-contributors`example stops the query in the specified account.`aws networkflowmonitor stop-query-workload-insights-top-contributors \ --scope-id``e21cda79-30a0-4c12-9299-d8629d76d8cf`\ --query-id`1fc423d3-b144-37a6-80e6-e2c7d26eea0c`This command produces no output. For more information, see [Evaluate network flows with workload insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-configure-evaluate-flows.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StopQueryWorkloadInsightsTopContributors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/stop-query-workload-insights-top-contributors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to the specified resource**The following `tag-resource`example adds a tag to the monitor in the specified account.`aws networkflowmonitor tag-resource \ --resource-arn``arn:aws:networkflowmonitor:us-east-1:123456789012:monitor/Demo`\ --tags`Key=stack,Value=Production`This command produces no output. For more information, see [Tagging your Amazon CloudWatch resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from the specified resource**The following `untag-resource`example removes a tag from the monitor in the specified account.`aws networkflowmonitor untag-resource \ --resource-arn``arn:aws:networkflowmonitor:us-east-1:123456789012:monitor/Demo`\ --tag-keys`stack`This command produces no output. For more information, see [Tagging your Amazon CloudWatch resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-monitor`.

- **AWS CLI**
- 
            
                    **To update an existing monitor**The following `update-monitor`example updates the monitor named`Demo`in the specified account.`aws networkflowmonitor update-monitor \ --monitor-name``Demo`\ --local-resources-to-add type="AWS::EC2::VPC",identifier="arn:aws:ec2:us-east-1:123456789012:vpc/vpc-048d08dfbec623f94"Output: `{ "monitorArn": "arn:aws:networkflowmonitor:us-east-1:123456789012:monitor/Demo", "monitorName": "Demo", "monitorStatus": "ACTIVE", "tags": { "Value": "Production", "Key": "stack" } }`For more information, see [Components and features of Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-components.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UpdateMonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/update-monitor.html)in*AWS CLI Command Reference*.
 
-