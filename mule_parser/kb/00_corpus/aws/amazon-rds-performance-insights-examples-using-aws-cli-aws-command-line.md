# Amazon RDS Performance Insights examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_pi_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_pi_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon RDS Performance Insights.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-performance-analysis-report`.

- **AWS CLI**
- 
            
                    **To create a performance analysis report**The following `create-performance-analysis-report`example creates a performance analysis report with the start time`1682969503`and end time`1682979503`for the database`db-abcdefg123456789`.`aws pi create-performance-analysis-report \ --service-type``RDS`\ --identifier`db-abcdefg123456789`\ --start-time`1682969503`\ --end-time`1682979503`Output: `{ "AnalysisReportId": "report-0234d3ed98e28fb17" }`For more information about creating performance analysis reports, see [Creating a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.CreatingPerfAnlysisReport.html)in the*Amazon RDS User Guide*and[Creating a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.CreatingPerfAnlysisReport.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreatePerformanceAnalysisReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/create-performance-analysis-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-performance-analysis-report`.

- **AWS CLI**
- 
            
                    **To delete a performance analysis report**The following `delete-performance-analysis-report`example deletes the performance analysis report with the report ID`report-0d99cc91c4422ee61`.`aws pi delete-performance-analysis-report \ --service-type``RDS`\ --identifier`db-abcdefg123456789`\ --analysis-report-id`report-0d99cc91c4422ee61`This command produces no output. For more information about deleting performance analysis reports, see [Deleting a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.DeletePerfAnalysisReport.html)in the*Amazon RDS User Guide*and[Deleting a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.DeletePerfAnalysisReport.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeletePerformanceAnalysisReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/delete-performance-analysis-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-dimension-keys`.

- **AWS CLI**
- 
            
                    **Example 1: To describe dimension keys**This example requests the names of all wait events. The data is summarized by event name, and the aggregate values of those events over the specified time period. Command: `aws pi describe-dimension-keys --service-type``RDS`--identifier`db-LKCGOBK26374TPTDFXOIWVCPPM`--start-time`1527026400`--end-time`1527080400`--metric`db.load.avg`--group-by '`{"Group":"db.wait_event"}`'Output: `{ "AlignedEndTime": 1.5270804E9, "AlignedStartTime": 1.5270264E9, "Keys": [ { "Dimensions": {"db.wait_event.name": "wait/synch/mutex/innodb/aurora_lock_thread_slot_futex"}, "Total": 0.05906906851195666 }, { "Dimensions": {"db.wait_event.name": "wait/io/aurora_redo_log_flush"}, "Total": 0.015824722186149193 }, { "Dimensions": {"db.wait_event.name": "CPU"}, "Total": 0.008014396230265477 }, { "Dimensions": {"db.wait_event.name": "wait/io/aurora_respond_to_client"}, "Total": 0.0036361612526204477 }, { "Dimensions": {"db.wait_event.name": "wait/io/table/sql/handler"}, "Total": 0.0019108398419382965 }, { "Dimensions": {"db.wait_event.name": "wait/synch/cond/mysys/my_thread_var::suspend"}, "Total": 8.533847837782684E-4 }, { "Dimensions": {"db.wait_event.name": "wait/io/file/csv/data"}, "Total": 6.864181956477376E-4 }, { "Dimensions": {"db.wait_event.name": "Unknown"}, "Total": 3.895887056379051E-4 }, { "Dimensions": {"db.wait_event.name": "wait/synch/mutex/sql/FILE_AS_TABLE::LOCK_shim_lists"}, "Total": 3.710368625122906E-5 }, { "Dimensions": {"db.wait_event.name": "wait/lock/table/sql/handler"}, "Total": 0 } ] }`**Example 2: To find the SQL ID for statements contributing the most to DB load**The following `describe-dimension-keys`requests the SQL statement and SQL ID for the 10 statements that contributed the most to DB load.`aws pi describe-dimension-keys \ --service-type``RDS`\ --identifier`db-abcdefg123456789`\ --start-time`2023-05-01T00:00:00Z`\ --end-time`2023-05-01T01:00:00Z`\ --metric`db.load.avg`\ --group-by '`{"Group": "db.sql", "Dimensions": ["db.sql.id", "db.sql.statement"],"Limit": 10}`'Output: `{ "AlignedEndTime": 1.5270804E9, "AlignedStartTime": 1.5270264E9, "Identifier": "db-abcdefg123456789", "MetricList": [ { "Keys": [ { "Dimensions": {"db.sql.id": "AKIAIOSFODNN7EXAMPLE", "db.sql.statement": "SELECT * FROM customers WHERE customer_id = 123"}, "Total": 25.5,"Partitions": [12.3, 13.2] } ] } ] }`For more information about dimensions in Performance Insights, see [Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html)in the*Amazon RDS User Guide*and[Database load](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.ActiveSessions.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDimensionKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/describe-dimension-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-dimension-key-details`.

- **AWS CLI**
- 
            
                    **To get details for a specified dimension group for a DB instance**The following `get-dimension-key-details`example retrieves the full text of a SQL statement for DB instance`db-10BCD2EFGHIJ3KL4M5NO6PQRS5`. The`--group`is`db.sql`, and the`--group-identifier`is`db.sql.id`. In this example,`example-sql-id`represents a SQL ID retrieved by using the`get-resource-metrics`or`describe-dimension-keys`operations. In this example, the dimensions details are available. Thus, Performance Insights retrieves the full text of the SQL statement, without truncating it.`aws pi get-dimension-key-details \ --service-type``RDS`\ --identifier`db-10BCD2EFGHIJ3KL4M5NO6PQRS5`\ --group`db.sql`\ --group-identifier`example-sql-id`\ --requested-dimensions`statement`Output: `{ "Dimensions":[ { "Value": "SELECT e.last_name, d.department_name FROM employees e, departments d WHERE e.department_id=d.department_id", "Dimension": "db.sql.statement", "Status": "AVAILABLE" }, ... ] }`For more information about dimensions in Performance Insights, see [Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html)in the*Amazon RDS User Guide*and[Database load](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.ActiveSessions.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [GetDimensionKeyDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-dimension-key-details.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-performance-analysis-report`.

- **AWS CLI**
- 
            
                    **To get a performance analysis report**The following `get-performance-analysis-report`example gets the performance analysis report for the database`db-abcdefg123456789`with the report ID`report-0d99cc91c4422ee61`. The response provides the report status, ID, time details, and insights.`aws pi get-performance-analysis-report \ --service-type``RDS`\ --identifier`db-abcdefg123456789`\ --analysis-report-id`report-0d99cc91c4422ee61`Output: `{ "AnalysisReport": { "Status": "Succeeded", "ServiceType": "RDS", "Identifier": "db-abcdefg123456789", "StartTime": 1680583486.584, "AnalysisReportId": "report-0d99cc91c4422ee61", "EndTime": 1680587086.584, "CreateTime": 1680587087.139, "Insights": [ ... (Condensed for space) ] } }`For more information about performance analysis reports, see [Analyzing database performance for a period of time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzePerformanceTimePeriod.html)in the*Amazon RDS User Guide*and[Analyzing database performance for a period of time](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.AnalyzePerformanceTimePeriod.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [GetPerformanceAnalysisReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-performance-analysis-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-metadata`.

- **AWS CLI**
- 
            
                    **To get resource metadata for a database**The following `get-resource-metadata`example gets the resource metadata for the database`db-abcdefg123456789`. The response shows that SQL digest statistics are enabled.`aws pi get-resource-metadata \ --service-type``RDS`\ --identifier`db-abcdefg123456789`Output: `{ "Identifier": "db-abcdefg123456789", "Features":{ "SQL_DIGEST_STATISTICS":{ "Status": "ENABLED" } } }`For more information about SQL statistics for Performance Insights, see [SQL statistics for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sql-statistics.html)in the*Amazon RDS User Guide*and[SQL statistics for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/sql-statistics.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [GetResourceMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-resource-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-metrics`.

- **AWS CLI**
- 
            
                    **To get resource metrics**This example requests data points for the *db.wait_event*dimension group, and for the*db.wait_event.name*dimension within that group. In the response, the relevant data points are grouped by the requested dimension (*db.wait_event.name*).Command: `aws pi get-resource-metrics --service-type``RDS`--identifier`db-LKCGOBK26374TPTDFXOIWVCPPM`--start-time`1527026400`--end-time`1527080400`--period-in-seconds`300`--metric`db.load.avg`--metric-queries`file://metric-queries.json`The arguments for `--metric-queries`are stored in a JSON file,`metric-queries.json`. Here are the contents of that file:`[ { "Metric": "db.load.avg", "GroupBy": { "Group":"db.wait_event" } } ]`Output: `{ "AlignedEndTime": 1.5270804E9, "AlignedStartTime": 1.5270264E9, "Identifier": "db-LKCGOBK26374TPTDFXOIWVCPPM", "MetricList": [ { "Key": { "Metric": "db.load.avg" }, "DataPoints": [ { "Timestamp": 1527026700.0, "Value": 1.3533333333333333 }, { "Timestamp": 1527027000.0, "Value": 0.88 }, <...remaining output omitted...> ] }, { "Key": { "Metric": "db.load.avg", "Dimensions": { "db.wait_event.name": "wait/synch/mutex/innodb/aurora_lock_thread_slot_futex" } }, "DataPoints": [ { "Timestamp": 1527026700.0, "Value": 0.8566666666666667 }, { "Timestamp": 1527027000.0, "Value": 0.8633333333333333 }, <...remaining output omitted...> ], }, <...remaining output omitted...> ] }`- 
                    For API details, see [GetResourceMetrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-resource-metrics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-available-resource-dimensions`.

- **AWS CLI**
- 
            
                    **To list the dimensions that can be queried for a metric type on a DB instance**The following `list-available-resource-dimensions`example lists the`db.load`metrics you can query for the database`db-abcdefg123456789`.`aws pi list-available-resource-dimensions \ --service-type``RDS`\ --identifier`db-abcdefg123456789`\ --metrics`db.load`Output: `{ "MetricDimensions": [ { "Metric": "db.load", "Groups": [ { "Group": "db.user", "Dimensions": [ { "Identifier": "db.user.id" }, { "Identifier": "db.user.name" } ] }, { "Group": "db.sql_tokenized", "Dimensions": [ { "Identifier": "db.sql_tokenized.id" }, { "Identifier": "db.sql_tokenized.db_id" }, { "Identifier": "db.sql_tokenized.statement" } ] }, ... ] } ] }`For more information about dimensions in Performance Insights, see [Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html)in the*Amazon RDS User Guide*and[Database load](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.ActiveSessions.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ListAvailableResourceDimensions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-available-resource-dimensions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-available-resource-metrics`.

- **AWS CLI**
- 
            
                    **To list the metrics that can be queried for a metric type on a DB instance**The following `list-available-resource-metrics`example lists the`db.load`metrics you can query for the database`db-abcdefg123456789`.`aws pi list-available-resource-metrics \ --service-type``RDS`\ --identifier`db-abcdefg123456789`\ --metric-types`"os"``"db"`Output: `{ "Metrics": [ { "Description": "The number of virtual CPUs for the DB instance", "Metric": "os.general.numVCPUs", "Unit": "vCPUs" }, ......, { "Description": "Time spent reading data file blocks by backends in this instance", "Metric": "db.IO.read_latency", "Unit": "Milliseconds per block" }, ...... ] }`For more information about metrics in Performance Insights, see [Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html)in the*Amazon RDS User Guide*and[Database load](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.ActiveSessions.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ListAvailableResourceMetrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-available-resource-metrics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-performance-analysis-reports`.

- **AWS CLI**
- 
            
                    **To list performance analysis reports for a database**The following `list-performance-analysis-reports`example lists performance analysis reports for the database`db-abcdefg123456789`. The response lists all the reports with the report ID, status, and time period details.`aws pi list-performance-analysis-reports \ --service-type``RDS`\ --identifier`db-abcdefg123456789`Output: `{ "AnalysisReports": [ { "Status": "Succeeded", "EndTime": 1680587086.584, "CreateTime": 1680587087.139, "StartTime": 1680583486.584, "AnalysisReportId": "report-0d99cc91c4422ee61" }, { "Status": "Succeeded", "EndTime": 1681491137.914, "CreateTime": 1681491145.973, "StartTime": 1681487537.914, "AnalysisReportId": "report-002633115cc002233" }, { "Status": "Succeeded", "EndTime": 1681493499.849, "CreateTime": 1681493507.762, "StartTime": 1681489899.849, "AnalysisReportId": "report-043b1e006b47246f9" }, { "Status": "InProgress", "EndTime": 1682979503.0, "CreateTime": 1682979618.994, "StartTime": 1682969503.0, "AnalysisReportId": "report-01ad15f9b88bcbd56" } ] }`For more information about performance analysis reports, see [Analyzing database performance for a period of time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzePerformanceTimePeriod.html)in the*Amazon RDS User Guide*and[Analyzing database performance for a period of time](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.AnalyzePerformanceTimePeriod.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ListPerformanceAnalysisReports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-performance-analysis-reports.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a performance analysis report**The following `list-tags-for-resource`example lists tags for a performance analysis report with the report ID`report-0d99cc91c4422ee61`.`aws pi list-tags-for-resource \ --service-type``RDS`\ --resource-arn`arn:aws:pi:us-west-2:123456789012:perf-reports/RDS/db-abcdefg123456789/report-0d99cc91c4422ee61`Output: `{ "Tags": [ { "Value": "test-tag", "Key": "name" } ] }`For more information about tagging performance analysis reports, see [Adding tags to a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.ManagePerfAnalysisReportTags.html)in the*Amazon RDS User Guide*and[Adding tags to a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.ManagePerfAnalysisReportTags.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to a performance analysis report**The following `tag-resource`example adds the tag key`name`with the tag value`test-tag`to a performance analysis report with the report ID`report-0d99cc91c4422ee61`.`aws pi tag-resource \ --service-type``RDS`\ --resource-arn`arn:aws:pi:us-west-2:123456789012:perf-reports/RDS/db-abcdefg123456789/report-0d99cc91c4422ee61`\ --tags`Key=name,Value=test-tag`This command produces no output. For more information about tagging performance analysis reports, see [Adding tags to a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.ManagePerfAnalysisReportTags.html)in the*Amazon RDS User Guide*and[Adding tags to a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.ManagePerfAnalysisReportTags.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To delete a tag for a performance analysis report**The following `untag-resource`example deletes the tag`name`for a performance analysis report with the report ID`report-0d99cc91c4422ee61`.`aws pi untag-resource \ --service-type``RDS`\ --resource-arn`arn:aws:pi:us-west-2:123456789012:perf-reports/RDS/db-abcdefg123456789/report-0d99cc91c4422ee61`\ --tag-keys`name`This command produces no output. For more information about tagging performance analysis reports, see [Adding tags to a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.ManagePerfAnalysisReportTags.html)in the*Amazon RDS User Guide*and[Adding tags to a performance analysis report in Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.ManagePerfAnalysisReportTags.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/untag-resource.html)in*AWS CLI Command Reference*.
 
-