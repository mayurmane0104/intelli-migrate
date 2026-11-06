# CloudWatch examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudwatch_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudwatch_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CloudWatch.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-alarms`.

- **AWS CLI**
- 
            
                    **To delete an alarm**The following example uses the `delete-alarms`command to delete the Amazon CloudWatch alarm named "myalarm":`aws cloudwatch delete-alarms --alarm-names``myalarm`Output: `This command returns to the prompt if successful.`- 
                    For API details, see [DeleteAlarms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-alarms.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-anomaly-detector`.

- **AWS CLI**
- 
            
                    **To delete a specified anomaly detection model**The following `delete-anomaly-detector`example deletes an anomaly detector model in the specified account.`aws cloudwatch delete-anomaly-detector \ --namespace``AWS/Logs`\ --metric-name`IncomingBytes`\ --stat`SampleCount`This command produces no output. For more information, see [Deleting an anomaly detection model](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html#Delete_Anomaly_Detection_Model)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteAnomalyDetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-anomaly-detector.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-dashboards`.

- **AWS CLI**
- 
            
                    **To delete specified dashboards**The following `delete-dashboards`example deletes two dashboards named`Dashboard-A`and`Dashboard-B`in the specified account.`aws cloudwatch delete-dashboards \ --dashboard-names``Dashboard-A``Dashboard-B`This command produces no output. For more information, see [Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteDashboards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-dashboards.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-insight-rules`.

- **AWS CLI**
- 
            
                    **To delete specified contributor insights rules**The following `delete-insight-rules`example deletes two contributor insights rules named`Rule-A`and`Rule-B`in the specified account.`aws cloudwatch delete-insight-rules \ --rule-names``Rule-A``Rule-B`Output: `{ "Failures": [] }`For more information, see [Use Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteInsightRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-insight-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-metric-stream`.

- **AWS CLI**
- 
            
                    **To delete a specified metric stream**The following `delete-metric-stream`example deletes the metric stream named`QuickPartial-gSCKvO`in the specified account.`aws cloudwatch delete-metric-stream \ --name``QuickPartial-gSCKvO`This command produces no output. For more information, see [Use metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteMetricStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-metric-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-alarm-history`.

- **AWS CLI**
- 
            
                    **To retrieve history for an alarm**The following example uses the `describe-alarm-history`command to retrieve history for the Amazon CloudWatch alarm named "myalarm":`aws cloudwatch describe-alarm-history --alarm-name``"myalarm"`--history-item-type`StateUpdate`Output: `{ "AlarmHistoryItems": [ { "Timestamp": "2014-04-09T18:59:06.442Z", "HistoryItemType": "StateUpdate", "AlarmName": "myalarm", "HistoryData": "{\"version\":\"1.0\",\"oldState\":{\"stateValue\":\"ALARM\",\"stateReason\":\"testing purposes\"},\"newState\":{\"stateValue\":\"OK\",\"stateReason\":\"Threshold Crossed: 2 datapoints were not greater than the threshold (70.0). The most recent datapoints: [38.958, 40.292].\",\"stateReasonData\":{\"version\":\"1.0\",\"queryDate\":\"2014-04-09T18:59:06.419+0000\",\"startDate\":\"2014-04-09T18:44:00.000+0000\",\"statistic\":\"Average\",\"period\":300,\"recentDatapoints\":[38.958,40.292],\"threshold\":70.0}}}", "HistorySummary": "Alarm updated from ALARM to OK" }, { "Timestamp": "2014-04-09T18:59:05.805Z", "HistoryItemType": "StateUpdate", "AlarmName": "myalarm", "HistoryData": "{\"version\":\"1.0\",\"oldState\":{\"stateValue\":\"OK\",\"stateReason\":\"Threshold Crossed: 2 datapoints were not greater than the threshold (70.0). The most recent datapoints: [38.839999999999996, 39.714].\",\"stateReasonData\":{\"version\":\"1.0\",\"queryDate\":\"2014-03-11T22:45:41.569+0000\",\"startDate\":\"2014-03-11T22:30:00.000+0000\",\"statistic\":\"Average\",\"period\":300,\"recentDatapoints\":[38.839999999999996,39.714],\"threshold\":70.0}},\"newState\":{\"stateValue\":\"ALARM\",\"stateReason\":\"testing purposes\"}}", "HistorySummary": "Alarm updated from OK to ALARM" } ] }`- 
                    For API details, see [DescribeAlarmHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-alarm-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-alarms-for-metric`.

- **AWS CLI**
- 
            
                    **To display information about alarms associated with a metric**The following example uses the `describe-alarms-for-metric`command to display information about any alarms associated with the Amazon EC2 CPUUtilization metric and the instance with the ID i-0c986c72.:`aws cloudwatch describe-alarms-for-metric --metric-name``CPUUtilization`--namespace`AWS/EC2`--dimensions`Name=InstanceId,Value=i-0c986c72`Output: `{ "MetricAlarms": [ { "EvaluationPeriods": 10, "AlarmArn": "arn:aws:cloudwatch:us-east-1:111122223333:alarm:myHighCpuAlarm2", "StateUpdatedTimestamp": "2013-10-30T03:03:51.479Z", "AlarmConfigurationUpdatedTimestamp": "2013-10-30T03:03:50.865Z", "ComparisonOperator": "GreaterThanOrEqualToThreshold", "AlarmActions": [ "arn:aws:sns:us-east-1:111122223333:NotifyMe" ], "Namespace": "AWS/EC2", "AlarmDescription": "CPU usage exceeds 70 percent", "StateReasonData": "{\"version\":\"1.0\",\"queryDate\":\"2013-10-30T03:03:51.479+0000\",\"startDate\":\"2013-10-30T02:08:00.000+0000\",\"statistic\":\"Average\",\"period\":300,\"recentDatapoints\":[40.698,39.612,42.432,39.796,38.816,42.28,42.854,40.088,40.760000000000005,41.316],\"threshold\":70.0}", "Period": 300, "StateValue": "OK", "Threshold": 70.0, "AlarmName": "myHighCpuAlarm2", "Dimensions": [ { "Name": "InstanceId", "Value": "i-0c986c72" } ], "Statistic": "Average", "StateReason": "Threshold Crossed: 10 datapoints were not greater than or equal to the threshold (70.0). The most recent datapoints: [40.760000000000005, 41.316].", "InsufficientDataActions": [], "OKActions": [], "ActionsEnabled": true, "MetricName": "CPUUtilization" }, { "EvaluationPeriods": 2, "AlarmArn": "arn:aws:cloudwatch:us-east-1:111122223333:alarm:myHighCpuAlarm", "StateUpdatedTimestamp": "2014-04-09T18:59:06.442Z", "AlarmConfigurationUpdatedTimestamp": "2014-04-09T22:26:05.958Z", "ComparisonOperator": "GreaterThanThreshold", "AlarmActions": [ "arn:aws:sns:us-east-1:111122223333:HighCPUAlarm" ], "Namespace": "AWS/EC2", "AlarmDescription": "CPU usage exceeds 70 percent", "StateReasonData": "{\"version\":\"1.0\",\"queryDate\":\"2014-04-09T18:59:06.419+0000\",\"startDate\":\"2014-04-09T18:44:00.000+0000\",\"statistic\":\"Average\",\"period\":300,\"recentDatapoints\":[38.958,40.292],\"threshold\":70.0}", "Period": 300, "StateValue": "OK", "Threshold": 70.0, "AlarmName": "myHighCpuAlarm", "Dimensions": [ { "Name": "InstanceId", "Value": "i-0c986c72" } ], "Statistic": "Average", "StateReason": "Threshold Crossed: 2 datapoints were not greater than the threshold (70.0). The most recent datapoints: [38.958, 40.292].", "InsufficientDataActions": [], "OKActions": [], "ActionsEnabled": false, "MetricName": "CPUUtilization" } ] }`- 
                    For API details, see [DescribeAlarmsForMetric](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-alarms-for-metric.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-alarms`.

- **AWS CLI**
- 
            
                    **To list information about an alarm**The following example uses the `describe-alarms`command to provide information about the alarm named "myalarm":`aws cloudwatch describe-alarms --alarm-names``"myalarm"`Output: `{ "MetricAlarms": [ { "EvaluationPeriods": 2, "AlarmArn": "arn:aws:cloudwatch:us-east-1:123456789012:alarm:myalarm", "StateUpdatedTimestamp": "2014-04-09T18:59:06.442Z", "AlarmConfigurationUpdatedTimestamp": "2012-12-27T00:49:54.032Z", "ComparisonOperator": "GreaterThanThreshold", "AlarmActions": [ "arn:aws:sns:us-east-1:123456789012:myHighCpuAlarm" ], "Namespace": "AWS/EC2", "AlarmDescription": "CPU usage exceeds 70 percent", "StateReasonData": "{\"version\":\"1.0\",\"queryDate\":\"2014-04-09T18:59:06.419+0000\",\"startDate\":\"2014-04-09T18:44:00.000+0000\",\"statistic\":\"Average\",\"period\":300,\"recentDatapoints\":[38.958,40.292],\"threshold\":70.0}", "Period": 300, "StateValue": "OK", "Threshold": 70.0, "AlarmName": "myalarm", "Dimensions": [ { "Name": "InstanceId", "Value": "i-0c986c72" } ], "Statistic": "Average", "StateReason": "Threshold Crossed: 2 datapoints were not greater than the threshold (70.0). The most recent datapoints: [38.958, 40.292].", "InsufficientDataActions": [], "OKActions": [], "ActionsEnabled": true, "MetricName": "CPUUtilization" } ] }`- 
                    For API details, see [DescribeAlarms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-alarms.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-anomaly-detectors`.

- **AWS CLI**
- 
            
                    **To retrieve a list of anomaly detection models**The following `describe-anomaly-detectors`example displays information about anomaly detector models that are associated with the`AWS/Logs`namespace in the specified account.`aws cloudwatch describe-anomaly-detectors \ --namespace``AWS/Logs`Output: `{ "AnomalyDetectors": [ { "Namespace": "AWS/Logs", "MetricName": "IncomingBytes", "Dimensions": [], "Stat": "SampleCount", "Configuration": { "ExcludedTimeRanges": [] }, "StateValue": "TRAINED", "SingleMetricAnomalyDetector": { "AccountId": "123456789012", "Namespace": "AWS/Logs", "MetricName": "IncomingBytes", "Dimensions": [], "Stat": "SampleCount" } }, { "Namespace": "AWS/Logs", "MetricName": "IncomingBytes", "Dimensions": [ { "Name": "LogGroupName", "Value": "demo" } ], "Stat": "Average", "Configuration": { "ExcludedTimeRanges": [] }, "StateValue": "PENDING_TRAINING", "SingleMetricAnomalyDetector": { "AccountId": "123456789012", "Namespace": "AWS/Logs", "MetricName": "IncomingBytes", "Dimensions": [ { "Name": "LogGroupName", "Value": "demo" } ], "Stat": "Average" } } ] }`For more information, see [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DescribeAnomalyDetectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-anomaly-detectors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-insight-rules`.

- **AWS CLI**
- 
            
                    **To retrieve a list of Contributor Insights rules**The following `describe-insight-rules`example shows all the Contributor Insight rules in the specified account.`aws cloudwatch describe-insight-rules`Output: `{ "InsightRules": [ { "Name": "Rule-A", "State": "ENABLED", "Schema": "CloudWatchLogRule/1", "Definition": "{\n\t\"AggregateOn\": \"Count\",\n\t\"Contribution\": {\n\t\t\"Filters\": [],\n\t\t\"Keys\": [\n\t\t\t\"$.requestId\"\n\t\t]\n\t},\n\t\"LogFormat\": \"JSON\",\n\t\"Schema\": {\n\t\t\"Name\": \"CloudWatchLogRule\",\n\t\t\"Version\": 1\n\t},\n\t\"LogGroupARNs\": [\n\t\t\"arn:aws:logs:us-east-1:123456789012:log-group:demo\"\n\t]\n}", "ManagedRule": false }, { "Name": "Rule-B", "State": "ENABLED", "Schema": "CloudWatchLogRule/1", "Definition": "{\n\t\"AggregateOn\": \"Count\",\n\t\"Contribution\": {\n\t\t\"Filters\": [],\n\t\t\"Keys\": [\n\t\t\t\"$.requestId\"\n\t\t]\n\t},\n\t\"LogFormat\": \"JSON\",\n\t\"Schema\": {\n\t\t\"Name\": \"CloudWatchLogRule\",\n\t\t\"Version\": 1\n\t},\n\t\"LogGroupARNs\": [\n\t\t\"arn:aws:logs:us-east-1:123456789012:log-group:demo-1\"\n\t]\n}", "ManagedRule": false } ] }`For more information, see [Use Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DescribeInsightRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-insight-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-alarm-actions`.

- **AWS CLI**
- 
            
                    **To disable actions for an alarm**The following example uses the `disable-alarm-actions`command to disable all actions for the alarm named myalarm.:`aws cloudwatch disable-alarm-actions --alarm-names``myalarm`This command returns to the prompt if successful. - 
                    For API details, see [DisableAlarmActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/disable-alarm-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-insight-rules`.

- **AWS CLI**
- 
            
                    **To disable specified contributor insight rules**The following `disable-insight-rules`example disables two contributor insights rules named`Rule-A`and`Rule-B`in the specified account.`aws cloudwatch disable-insight-rules \ --rule-names``Rule-A``Rule-B`Output: `{ "Failures": [] }`For more information, see [Use Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DisableInsightRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/disable-insight-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-alarm-actions`.

- **AWS CLI**
- 
            
                    **To enable all actions for an alarm**The following example uses the `enable-alarm-actions`command to enable all actions for the alarm named myalarm.:`aws cloudwatch enable-alarm-actions --alarm-names``myalarm`This command returns to the prompt if successful. - 
                    For API details, see [EnableAlarmActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/enable-alarm-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-insight-rules`.

- **AWS CLI**
- 
            
                    **To enable specified contributor insight rules**The following `enable-insight-rules`example enables two contributor insights rules named`Rule-A`and`Rule-B`in the specified account.`aws cloudwatch enable-insight-rules \ --rule-names``Rule-A``Rule-B`Output: `{ "Failures": [] }`For more information, see [Use Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [EnableInsightRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/enable-insight-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-dashboard`.

- **AWS CLI**
- 
            
                    **To retrieve information about a Dashboard**The following `get-dashboard`example displays information about the dashboard named`Dashboard-A`in the specified account.`aws cloudwatch get-dashboard \ --dashboard-name``Dashboard-A`Output: `{ "DashboardArn": "arn:aws:cloudwatch::123456789012:dashboard/Dashboard-A", "DashboardBody": "{\"widgets\":[{\"type\":\"metric\",\"x\":0,\"y\":0,\"width\":6,\"height\":6,\"properties\":{\"view\":\"timeSeries\",\"stacked\":false,\"metrics\":[[\"AWS/EC2\",\"NetworkIn\",\"InstanceId\",\"i-0131f062232ade043\"],[\".\",\"NetworkOut\",\".\",\".\"]],\"region\":\"us-east-1\"}}]}", "DashboardName": "Dashboard-A" }`For more information, see [Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetDashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-dashboard.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-insight-rule-report`.

- **AWS CLI**
- 
            
                    **To retrieve the time series data collected by a Contributor Insights rule**The following `get-insight-rule-report`example returns the time series data collected by a Contributor Insights rule.`aws cloudwatch get-insight-rule-report \ --rule-name``Rule-A`\ --start-time`2024-10-13T20:15:00Z`\ --end-time`2024-10-13T20:30:00Z`\ --period`300`Output: `{ "KeyLabels": [ "PartitionKey" ], "AggregationStatistic": "Sum", "AggregateValue": 0.5, "ApproximateUniqueCount": 1, "Contributors": [ { "Keys": [ "RequestID" ], "ApproximateAggregateValue": 0.5, "Datapoints": [ { "Timestamp": "2024-10-13T21:00:00+00:00", "ApproximateValue": 0.5 } ] } ], "RuleAttributes": [] }`For more information, see [Use Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetInsightRuleReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-insight-rule-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-metric-data`.

- **AWS CLI**
- 
            
                    **Example 1: To get the Average Total IOPS for the specified EC2 using math expression**The following `get-metric-data`example retrieves CloudWatch metric values for the EC2 instance with InstanceID`i-abcdef`using metric math exprssion that combines`EBSReadOps`and`EBSWriteOps`metrics.`aws cloudwatch get-metric-data \ --metric-data-queries``file://file.json`\ --start-time`2024-09-29T22:10:00Z`\ --end-time`2024-09-29T22:15:00Z`Contents of `file.json`:`[ { "Id": "m3", "Expression": "(m1+m2)/300", "Label": "Avg Total IOPS" }, { "Id": "m1", "MetricStat": { "Metric": { "Namespace": "AWS/EC2", "MetricName": "EBSReadOps", "Dimensions": [ { "Name": "InstanceId", "Value": "i-abcdef" } ] }, "Period": 300, "Stat": "Sum", "Unit": "Count" }, "ReturnData": false }, { "Id": "m2", "MetricStat": { "Metric": { "Namespace": "AWS/EC2", "MetricName": "EBSWriteOps", "Dimensions": [ { "Name": "InstanceId", "Value": "i-abcdef" } ] }, "Period": 300, "Stat": "Sum", "Unit": "Count" }, "ReturnData": false } ]`Output: `{ "MetricDataResults": [ { "Id": "m3", "Label": "Avg Total IOPS", "Timestamps": [ "2024-09-29T22:10:00+00:00" ], "Values": [ 96.85 ], "StatusCode": "Complete" } ], "Messages": [] }`**Example 2: To monitor the estimated AWS charges using CloudWatch billing metrics**The following `get-metric-data`example retrieves`EstimatedCharges`CloudWatch metric from AWS/Billing namespace.`aws cloudwatch get-metric-data \ --metric-data-queries '``[{"Id":"m1","MetricStat":{"Metric":{"Namespace":"AWS/Billing","MetricName":"EstimatedCharges","Dimensions":[{"Name":"Currency","Value":"USD"}]},"Period":21600,"Stat":"Maximum"}}]`' \ --start-time`2024-09-26T12:00:00Z`\ --end-time`2024-09-26T18:00:00Z`\ --region`us-east-1`Output: `{ "MetricDataResults": [ { "Id": "m1", "Label": "EstimatedCharges", "Timestamps": [ "2024-09-26T12:00:00+00:00" ], "Values": [ 542.38 ], "StatusCode": "Complete" } ], "Messages": [] }`For more information, see [Using math expressions with CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetMetricData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-metric-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-metric-statistics`.

- **AWS CLI**
- 
            
                    **To get the CPU utilization per EC2 instance**The following example uses the `get-metric-statistics`command to get the CPU utilization for an EC2 instance with the ID i-abcdef.`aws cloudwatch get-metric-statistics --metric-name``CPUUtilization`--start-time`2014-04-08T23:18:00Z`--end-time`2014-04-09T23:18:00Z`--period`3600`--namespace`AWS/EC2`--statistics`Maximum`--dimensions`Name=InstanceId,Value=i-abcdef`Output: `{ "Datapoints": [ { "Timestamp": "2014-04-09T11:18:00Z", "Maximum": 44.79, "Unit": "Percent" }, { "Timestamp": "2014-04-09T20:18:00Z", "Maximum": 47.92, "Unit": "Percent" }, { "Timestamp": "2014-04-09T19:18:00Z", "Maximum": 50.85, "Unit": "Percent" }, { "Timestamp": "2014-04-09T09:18:00Z", "Maximum": 47.92, "Unit": "Percent" }, { "Timestamp": "2014-04-09T03:18:00Z", "Maximum": 76.84, "Unit": "Percent" }, { "Timestamp": "2014-04-09T21:18:00Z", "Maximum": 48.96, "Unit": "Percent" }, { "Timestamp": "2014-04-09T14:18:00Z", "Maximum": 47.92, "Unit": "Percent" }, { "Timestamp": "2014-04-09T08:18:00Z", "Maximum": 47.92, "Unit": "Percent" }, { "Timestamp": "2014-04-09T16:18:00Z", "Maximum": 45.55, "Unit": "Percent" }, { "Timestamp": "2014-04-09T06:18:00Z", "Maximum": 47.92, "Unit": "Percent" }, { "Timestamp": "2014-04-09T13:18:00Z", "Maximum": 45.08, "Unit": "Percent" }, { "Timestamp": "2014-04-09T05:18:00Z", "Maximum": 47.92, "Unit": "Percent" }, { "Timestamp": "2014-04-09T18:18:00Z", "Maximum": 46.88, "Unit": "Percent" }, { "Timestamp": "2014-04-09T17:18:00Z", "Maximum": 52.08, "Unit": "Percent" }, { "Timestamp": "2014-04-09T07:18:00Z", "Maximum": 47.92, "Unit": "Percent" }, { "Timestamp": "2014-04-09T02:18:00Z", "Maximum": 51.23, "Unit": "Percent" }, { "Timestamp": "2014-04-09T12:18:00Z", "Maximum": 47.67, "Unit": "Percent" }, { "Timestamp": "2014-04-08T23:18:00Z", "Maximum": 46.88, "Unit": "Percent" }, { "Timestamp": "2014-04-09T10:18:00Z", "Maximum": 51.91, "Unit": "Percent" }, { "Timestamp": "2014-04-09T04:18:00Z", "Maximum": 47.13, "Unit": "Percent" }, { "Timestamp": "2014-04-09T15:18:00Z", "Maximum": 48.96, "Unit": "Percent" }, { "Timestamp": "2014-04-09T00:18:00Z", "Maximum": 48.16, "Unit": "Percent" }, { "Timestamp": "2014-04-09T01:18:00Z", "Maximum": 49.18, "Unit": "Percent" } ], "Label": "CPUUtilization" }`**Specifying multiple dimensions**The following example illustrates how to specify multiple dimensions. Each dimension is specified as a Name/Value pair, with a comma between the name and the value. Multiple dimensions are separated by a space. If a single metric includes multiple dimensions, you must specify a value for every defined dimension. For more examples using the `get-metric-statistics`command, see Get Statistics for a Metric in the*Amazon CloudWatch Developer Guide*.`aws cloudwatch get-metric-statistics --metric-name``Buffers`--namespace`MyNameSpace`--dimensions`Name=InstanceID,Value=i-abcdef``Name=InstanceType,Value=m1.small`--start-time`2016-10-15T04:00:00Z`--end-time`2016-10-19T07:00:00Z`--statistics`Average`--period`60`- 
                    For API details, see [GetMetricStatistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-metric-statistics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-metric-stream`.

- **AWS CLI**
- 
            
                    **To retrieve information about a metric stream**The following `get-metric-stream`example displays information about the metric stream named`QuickFull-GuaFbs`in the specified account.`aws cloudwatch get-metric-stream \ --name``QuickFull-GuaFbs`Output: `{ "Arn": "arn:aws:cloudwatch:us-east-1:123456789012:metric-stream/QuickFull-GuaFbs", "Name": "QuickFull-GuaFbs", "FirehoseArn": "arn:aws:firehose:us-east-1:123456789012:deliverystream/MetricStreams-QuickFull-GuaFbs-WnySbECG", "RoleArn": "arn:aws:iam::123456789012:role/service-role/MetricStreams-FirehosePutRecords-JN10W9B3", "State": "running", "CreationDate": "2024-10-11T18:48:59.187000+00:00", "LastUpdateDate": "2024-10-11T18:48:59.187000+00:00", "OutputFormat": "json", "IncludeLinkedAccountsMetrics": false }`For more information, see [Use metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetMetricStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-metric-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-metric-widget-image`.

- **AWS CLI**
- 
            
                    **To retrieve a snapshot graph of CPUUtilization**The following `get-metric-widget-image`example retrieves snapshot graph for the metric`CPUUtilization`of the EC2 instance with the ID`i-abcde`and saves the retrieved image as a file named "image.png" on your local machine.`aws cloudwatch get-metric-widget-image \ --metric-widget '``{"metrics":[["AWS/EC2","CPUUtilization","InstanceId","i-abcde"]]}`' \ --output-format`png`\ --output`text``|``base64`--decode`>``image.png`This command produces no output. - 
                    For API details, see [GetMetricWidgetImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-metric-widget-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-dashboards`.

- **AWS CLI**
- 
            
                    **To retrieve a list of Dashboards**The following `list-dashboards`example lists all the Dashboards in the specified account.`aws cloudwatch list-dashboards`Output: `{ "DashboardEntries": [ { "DashboardName": "Dashboard-A", "DashboardArn": "arn:aws:cloudwatch::123456789012:dashboard/Dashboard-A", "LastModified": "2024-10-11T18:40:11+00:00", "Size": 271 }, { "DashboardName": "Dashboard-B", "DashboardArn": "arn:aws:cloudwatch::123456789012:dashboard/Dashboard-B", "LastModified": "2024-10-11T18:44:41+00:00", "Size": 522 } ] }`For more information, see [Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListDashboards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-dashboards.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-metric-streams`.

- **AWS CLI**
- 
            
                    **To retrieve a list of metric streams**The following `list-metric-streams`example lists all the metric streams in the specified account.`aws cloudwatch list-metric-streams`Output: `{ "Entries": [ { "Arn": "arn:aws:cloudwatch:us-east-1:123456789012:metric-stream/QuickFull-GuaFbs", "CreationDate": "2024-10-11T18:48:59.187000+00:00", "LastUpdateDate": "2024-10-11T18:48:59.187000+00:00", "Name": "QuickFull-GuaFbs", "FirehoseArn": "arn:aws:firehose:us-east-1:123456789012:deliverystream/MetricStreams-QuickFull-GuaFbs-WnySbECG", "State": "running", "OutputFormat": "json" } ] }`For more information, see [Use metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListMetricStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-metric-streams.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-metrics`.

- **AWS CLI**
- 
            
                    **To list the metrics for Amazon SNS**The following `list-metrics`example displays the metrics for Amazon SNS.`aws cloudwatch list-metrics \ --namespace``"AWS/SNS"`Output: `{ "Metrics": [ { "Namespace": "AWS/SNS", "Dimensions": [ { "Name": "TopicName", "Value": "NotifyMe" } ], "MetricName": "PublishSize" }, { "Namespace": "AWS/SNS", "Dimensions": [ { "Name": "TopicName", "Value": "CFO" } ], "MetricName": "PublishSize" }, { "Namespace": "AWS/SNS", "Dimensions": [ { "Name": "TopicName", "Value": "NotifyMe" } ], "MetricName": "NumberOfNotificationsFailed" }, { "Namespace": "AWS/SNS", "Dimensions": [ { "Name": "TopicName", "Value": "NotifyMe" } ], "MetricName": "NumberOfNotificationsDelivered" }, { "Namespace": "AWS/SNS", "Dimensions": [ { "Name": "TopicName", "Value": "NotifyMe" } ], "MetricName": "NumberOfMessagesPublished" }, { "Namespace": "AWS/SNS", "Dimensions": [ { "Name": "TopicName", "Value": "CFO" } ], "MetricName": "NumberOfMessagesPublished" }, { "Namespace": "AWS/SNS", "Dimensions": [ { "Name": "TopicName", "Value": "CFO" } ], "MetricName": "NumberOfNotificationsDelivered" }, { "Namespace": "AWS/SNS", "Dimensions": [ { "Name": "TopicName", "Value": "CFO" } ], "MetricName": "NumberOfNotificationsFailed" } ] }`- 
                    For API details, see [ListMetrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-metrics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags associated with an existing alarm***The following `list-tags-for-resource`example lists all the tags associated with an alarm named`demo`in the specified account.`aws cloudwatch list-tags-for-resource \ --resource-arn``arn:aws:cloudwatch:us-east-1:123456789012:alarm:demo`Output: `{ "Tags": [ { "Key": "stack", "Value": "Production" }, { "Key": "team", "Value": "Devops" } ] }`For more information, see [Alarms and tagging](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_alarms_and_tagging.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-anomaly-detector`.

- **AWS CLI**
- 
            
                    **To create an anomaly detection model**The following `put-anomaly-detector`example creates an anomaly detection model for a CloudWatch metric.`aws cloudwatch put-anomaly-detector \ --namespace``AWS/Logs`\ --metric-name`IncomingBytes`\ --stat`SampleCount`This command produces no output. For more information, see [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [PutAnomalyDetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-anomaly-detector.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-composite-alarm`.

- **AWS CLI**
- 
            
                    **To create a composite cloudwatch alarm**The following `put-composite-alarm`example creates a composite alarm named`ProdAlarm`in the specified account.`aws cloudwatch put-composite-alarm \ --alarm-name``ProdAlarm`\ --alarm-rule`"ALARM(CPUUtilizationTooHigh) AND ALARM(MemUsageTooHigh)"`\ --alarm-actions`arn:aws:sns:us-east-1:123456789012:demo`\ --actions-enabledThis command produces no output. For more information, see [Create a composite alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm_How_To.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [PutCompositeAlarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-dashboard`.

- **AWS CLI**
- 
            
                    **To create a dashboard**The following `put-dashboard`example creates a dashboard named`Dashboard-A`in the specified account.`aws cloudwatch put-dashboard \ --dashboard-name``Dashboard-A`\ --dashboard-body '`{"widgets":[{"height":6,"width":6,"y":0,"x":0,"type":"metric","properties":{"view":"timeSeries","stacked":false,"metrics":[["Namespace","CPUUtilization","Environment","Prod","Type","App"]],"region":"us-east-1"}}]}`'Output: `{ "DashboardValidationMessages": [] }`For more information, see [Creating a CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [PutDashboard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-dashboard.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-insight-rule`.

- **AWS CLI**
- 
            
                    **To create a contributor insights rule**The following `put-insight-rule`example creates a Contributor Insights rule named`VPCFlowLogsContributorInsights`in the specified account.`aws cloudwatch put-insight-rule \ --rule-name``VPCFlowLogsContributorInsights`\ --rule-definition`file://insight-rule.json`\ --rule-state`ENABLED`Contents of `insight-rule.json`:`{ "Schema": { "Name": "CloudWatchLogRule", "Version": 1 }, "AggregateOn": "Count", "Contribution": { "Filters": [], "Keys": [ "tcp-flag" ] }, "LogFormat": "CLF", "LogGroupNames": [ "/vpc/flowlogs/*" ], "Fields": { "23": "tcp-flag" } }`This command produces no output. For more information, see [Create a Contributor Insights rule in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-CreateRule.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [PutInsightRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-insight-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-metric-alarm`.

- **AWS CLI**
- 
            
                    **To send an Amazon Simple Notification Service email message when CPU utilization exceeds 70 percent**The following example uses the `put-metric-alarm`command to send an Amazon Simple Notification Service email message when CPU utilization exceeds 70 percent:`aws cloudwatch put-metric-alarm --alarm-name``cpu-mon`--alarm-description`"Alarm when CPU exceeds 70 percent"`--metric-name`CPUUtilization`--namespace`AWS/EC2`--statistic`Average`--period`300`--threshold`70`--comparison-operator`GreaterThanThreshold`--dimensions`"Name=InstanceId,Value=i-12345678"`--evaluation-periods`2`--alarm-actions`arn:aws:sns:us-east-1:111122223333:MyTopic`--unit`Percent`This command returns to the prompt if successful. If an alarm with the same name already exists, it will be overwritten by the new alarm. **To specify multiple dimensions**The following example illustrates how to specify multiple dimensions. Each dimension is specified as a Name/Value pair, with a comma between the name and the value. Multiple dimensions are separated by a space: `aws cloudwatch put-metric-alarm --alarm-name``"Default_Test_Alarm3"`--alarm-description`"The default example alarm"`--namespace`"CW EXAMPLE METRICS"`--metric-name`Default_Test`--statistic`Average`--period`60`--evaluation-periods`3`--threshold`50`--comparison-operator`GreaterThanOrEqualToThreshold`--dimensions`Name=key1,Value=value1``Name=key2,Value=value2`- 
                    For API details, see [PutMetricAlarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-alarm.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-metric-data`.

- **AWS CLI**
- 
            
                    **To publish a custom metric to Amazon CloudWatch**The following example uses the `put-metric-data`command to publish a custom metric to Amazon CloudWatch:`aws cloudwatch put-metric-data --namespace``"Usage Metrics"`--metric-data`file://metric.json`The values for the metric itself are stored in the JSON file, `metric.json`.Here are the contents of that file: `[ { "MetricName": "New Posts", "Timestamp": "Wednesday, June 12, 2013 8:28:20 PM", "Value": 0.50, "Unit": "Count" } ]`For more information, see Publishing Custom Metrics in the *Amazon CloudWatch Developer Guide*.**To specify multiple dimensions**The following example illustrates how to specify multiple dimensions. Each dimension is specified as a Name=Value pair. Multiple dimensions are separated by a comma.: `aws cloudwatch put-metric-data --metric-name``Buffers`--namespace`MyNameSpace`--unit`Bytes`--value`231434333`--dimensions`InstanceID=1-23456789,InstanceType=m1.small`- 
                    For API details, see [PutMetricData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-metric-stream`.

- **AWS CLI**
- 
            
                    **To create a metric stream**The following `put-metric-stream`example creates a metric stream named`QuickFull-GuaFb`in the specified account.`aws cloudwatch put-metric-stream \ --name``QuickFull-GuaFbs`\ --firehose-arn`arn:aws:firehose:us-east-1:123456789012:deliverystream/MetricStreams-QuickFull-GuaFbs-WnySbECG`\ --role-arn`arn:aws:iam::123456789012:role/service-role/MetricStreams-FirehosePutRecords-JN10W9B3`\ --output-format`json`\ --no-include-linked-accounts-metricsOutput: `{ "Arn": "arn:aws:cloudwatch:us-east-1:123456789012:metric-stream/QuickFull-GuaFbs" }`For more information, see [Set up a metric stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-setup.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [PutMetricStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-metric-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-alarm-state`.

- **AWS CLI**
- 
            
                    **To temporarily change the state of an alarm**The following example uses the `set-alarm-state`command to temporarily change the state of an Amazon CloudWatch alarm named "myalarm" and set it to the ALARM state for testing purposes:`aws cloudwatch set-alarm-state --alarm-name``"myalarm"`--state-value`ALARM`--state-reason`"testing purposes"`This command returns to the prompt if successful. - 
                    For API details, see [SetAlarmState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/set-alarm-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-metric-streams`.

- **AWS CLI**
- 
            
                    **To start a specified metric stream**The following `start-metric-streams`example starts the metric stream named`QuickFull-GuaFbs`in the specified account.`aws cloudwatch start-metric-streams \ --names``QuickFull-GuaFbs`This command produces no output. For more information, see [Use metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StartMetricStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/start-metric-streams.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-metric-streams`.

- **AWS CLI**
- 
            
                    **To stop a specified metric stream**The following `stop-metric-streams`example stops the metric stream named`QuickFull-GuaFbs`in the specified account.`aws cloudwatch stop-metric-streams \ --names``QuickFull-GuaFbs`This command produces no output. For more information, see [Use metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StopMetricStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/stop-metric-streams.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add one or more tags to the specified resource**The following `tag-resource`example adds 2 tags to the cloudwatch alarm named`demo`in the specified account.`aws cloudwatch tag-resource \ --resource-arn``arn:aws:cloudwatch:us-east-1:123456789012:alarm:demo`\ --tags`Key=stack,Value=Production``Key=team,Value=Devops`This command produces no output. For more information, see [Tagging your Amazon CloudWatch resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove one or more tags from the specified resource**The following `untag-resource`example removes 2 tags from the cloudwatch alarm named`demo`in the specified account.`aws cloudwatch untag-resource \ --resource-arn``arn:aws:cloudwatch:us-east-1:123456789012:alarm:demo`\ --tag-keys`stack``team`This command produces no output. For more information, see [Tagging your Amazon CloudWatch resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/untag-resource.html)in*AWS CLI Command Reference*.
 
-