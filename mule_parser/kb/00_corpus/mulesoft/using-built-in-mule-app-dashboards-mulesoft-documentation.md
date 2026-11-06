# Using Built-in Mule App Dashboards | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/app-dashboards](https://docs.mulesoft.com/monitoring/app-dashboards)

---

![Built-in dashboard selector](_images/builtin-dashboard-selection-interaction.png) 

# Using Built-in Mule App Dashboards

Built-in dashboards display deployment information about your application at the top of the screen and provide access to a number of different graphs.

The graphs and tables in built-in dashboards support many metrics, including application metrics. The **Overview** tab provides overall measures. You can view more granular application metrics through [additional tabs](#chart-reference).

When converting quantities of memory, Anypoint Monitoring uses the power of 10 (*MB*) to reflect metrics values rather than the power of 2 (*MiB*).

## How Anypoint Monitoring Collects Metrics

The Anypoint Monitoring agent collects and aggregates metrics on a per-minute basis, so one minute is the shortest possible time increment you can examine in dashboards for your deployments. Metrics collection begins at a random second of that minute, and collection repeats at the same second in subsequent minutes. For example, if the agent collects metrics at 12:00:15, it collects them again at 12:01:15, 12:02:15, and so on.

Within a Mule app, metrics for calls made to and from a connector start on different seconds. For example, metrics for inbound calls to port 8080 might be collected at 12:00:45, 12:01:45, and 12:02:45, while metrics for outbound calls made to an endpoint might be collected at 12:00:23, 12:01:23, and 12:02:23. Because inbound call metrics collection occurs at different seconds during a minute than call metrics for outbound calls, the total number of inbound and outbound calls reported during any minute might vary. For example, if app A reports ten outbound calls made at 12:05, app B might report that the total number of corresponding inbound calls is split between 12:04 and 12:05, or 12:05 and 12:06 time windows (namely, 12:04 reports four calls and 12:05 reports six calls, totaling the ten calls).

## Supported Versions of Mule Runtime Engine

Run your Mule app on a supported Mule runtime version. For supported versions, see [Mule Runtime Release Notes](../release-notes/mule-runtime/mule-esb).

## Anypoint Monitoring Metrics and Cloudwatch

Anypoint Monitoring collects some metrics that are also collected using Cloudwatch in Anypoint Runtime Manager. Anypoint Monitoring shows data that is aggregated in one minute intervals, and it is possible that data shown in Cloudwatch does not match based on when the data is collected.

## View a Built-in Dashboard

Built-in and custom dashboards are available from Anypoint Monitoring. You can view application metrics for applications deployed to CloudHub and to hybrid targets in both built-in and custom dashboards.

- 
Log in to Anypoint Platform with a user account that has [permission to access Anypoint Monitoring content](am-permissions).
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
In the sidebar, click **Built-in dashboards**.
- 
Select the **Environment**and**Resource name**for the app or API to view the corresponding dashboard.
- 
Click **View**.
 The built-in dashboard for the application or API is displayed.
- 
To switch to a dashboard for a different resource, click the built-in dashboard selector at the top of the page. ![Built-in dashboard selector](_images/builtin-dashboard-selection-interaction.png)  

Your data is prepopulated and displayed in the built-in dashboards and logs; no configuration is needed.

## Chart Reference

Anypoint Monitoring provides charts in these built-in dashboards:

### Overview

The following charts appear on the **Overview** dashboard:

- Mule Messages
- 
The total number of Mule messages that are processed successfully. 
- Average Response Time
- 
The average time to process Mule messages in the Mule application. 
- Errors
- 
The number of errors from processing Mule messages in the Mule application. 
- Inbound - Total Requests by Response Type
- 
The sum of inbound requests, grouped by type of response. Responses are `OK`or`Failed`. If a Mule app has more than one connector type, all types are included in this metric.
- Inbound - Average Response Time
- 
The average response time of inbound requests. If a Mule app has more than one connector type, all types are included in this metric. 
- Outbound - Total Requests by Response Type
- 
The sum of outbound requests, grouped by type of response. Responses are `OK`or`Failed`. If a Mule app has more than one connector type, all types are included in this metric.
- Outbound - Average Response Time
- 
The average response time of outbound requests. If a Mule app has more than one connector type, all types are included in this metric. 
- JVM - CPU % Utilization
- 
The average percentage of CPU used by the JVM, grouped by worker. The JVM used in this chart is the Mule JVM process. The calculation for CPU utilization is relative to the physical server on which Mule is deployed. For example, in RTF, the resource usage indicates the JVM use with respect to the entire server, and not with respect to the pod maximum CPU allocation. 
- JVM - Heap Used
- 
The average amount of heap memory utilized by the JVM, grouped by worker. The JVM used in this chart is the Mule JVM process. 
- JVM - Thread Count
- 
The average number of threads of the JVM, grouped by worker. The JVM used in this chart is the Mule JVM process. 

### Inbound

Inbound metrics are retained for 24 hours.
The following charts appear on the **Inbound** dashboard:

- Inbound - Total Requests by Response Type
- 
The sum of inbound requests, grouped by type of response. Responses are `OK`or`Failed`. If a Mule app has more than one connector type, all types are included in this metric.
- Inbound - Average Response Time
- 
The average response time of inbound requests. If a Mule app has more than one connector type, all types are included in this metric. 
- Inbound - Response Time by HTTP Endpoint
- 
The average, maximum, minimum, and total response times, grouped by endpoint. Anypoint Monitoring uses the average of data collected over one minute to calculate minimum and maximum response times. For more information about which endpoints appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).- 
Average: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600ms; red if the response time is greater than or equal to 600 ms 
- 
Maximum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 500ms; red if the response time is greater than or equal to 500 ms 
- 
Minimum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
 
- 
- Inbound - Total Requests by Endpoint
- 
The sum of inbound requests in the selected time period, grouped by endpoint. For more information about which endpoints appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Inbound - Response Time graphs (99, 90, 75, and 50 percentiles)
- 
The average response time of the 99, 90, 75, and 50 percentiles of inbound requests. The unit for these metrics is milliseconds (ms). 
- Inbound - Total Failed Requests
- 
The sum of failed inbound requests, grouped by type of response. 
- Inbound - Total Slow Requests by Endpoint
- 
The sum of inbound requests whose response time is greater than 1 second, grouped by endpoint. The sum of total calls in which the response time is greater than 1000 ms. 
- Inbound - Maximum Response Time
- 
The maximum response time, grouped by endpoint. This metric is available only for organizations that have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform. 
- Inbound - Protocols
- 
The sum of inbound requests, grouped by protocol. This metric is available only for organizations that have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform. 
- Inbound - HTTP Endpoints
- 
The sum of inbound requests, grouped by remote hosts (endpoints). This metric is available only for organizations that have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform. 

### Outbound

The following charts appear on the **Outbound** dashboard:

- Outbound - Total Requests by Response Type
- 
The sum of outbound requests, grouped by type of response. Responses are `OK`or`Failed`. If a Mule app has more than one connector type, all types are included in this metric.
- Outbound - Average Response Time
- 
The average response time of outbound requests, grouped by application. If a Mule app has more than one connector type, all types are included in this metric. 
- Outbound - Response Time by HTTP Endpoint
- 
The average, maximum, minimum, and total response times, grouped by endpoint. Anypoint Monitoring uses the average of data collected over one minute to calculate minimum and maximum response times. For more information about which endpoints appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).- 
Average: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600ms; red if the response time is greater than or equal to 600 ms 
- 
Maximum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 500ms; red if the response time is greater than or equal to 500 ms 
- 
Minimum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600ms; red if the response time is greater than or equal to 600 ms 
 
- 
- Outbound - Total Requests by HTTP Endpoint
- 
The sum of outbound requests in the selected time period, grouped by endpoint. For more information about which endpoints appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Outbound - Response Time (99, 90, 75, and 50 percentiles)
- 
The average response time of the 99, 90, 75, and 50 percentiles of outbound requests, grouped by application. The unit for these metrics is milliseconds (ms). 
- Outbound - Total Failed Requests
- 
The sum of failed outbound requests, grouped by type of response. 
- Outbound - HTTP Ports
- 
The sum of outbound requests, grouped by remote port. 
- Outbound - Operations
- 
The estimated count of outbound requests, grouped by operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Outbound - HTTP Protocols
- 
The sum of outbound requests for the selected time period, grouped by protocol. 
- Outbound - Endpoints
- 
The sum of outbound requests for the selected time period, grouped by remote hosts (endpoints). For more information about which endpoints appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).

### Flows

| 
 | 

- Inbound - Response Time by Flow
- 
The average inbound response time, grouped by flow. 
- Outbound - Response Time by Flow
- 
The average outbound response time, grouped by flow. 
- Inbound - Requests by Flow
- 
The sum of inbound requests, grouped by flow. 
- Outbound - Requests by Flow
- 
The sum of outbound requests, grouped by flow. 
- Failures by Flow
- 
The sum of failed inbound requests, grouped by flow. 
- Inbound - Slow Requests by Flow
- 
The sum of inbound requests whose response time is greater than 1000 ms, grouped by flow. Cell color varies according to the following thresholds: - 
Green if the response time is less than 300 ms 
- 
Yellow if the response time is greater than 300 ms and less than 600 ms 
- 
Red if the response time is greater than or equal to 600 ms 
 
- 
- Outbound - Slow Requests by Flow
- 
The sum of outbound requests whose response time is greater than 1000 ms, grouped by flow. Cell color varies according to the following thresholds: - 
Green if the response time is less than 300 ms 
- 
Yellow if the response time is greater than 300 ms and less than 600 ms 
- 
Red if the response time is greater than or equal to 600 ms 
 
- 
- Inbound - Response Time by Flow
- 
The average, minimum, and maximum inbound response time, grouped by flow. Anypoint Monitoring uses the average of data collected over one minute to calculate minimum and maximum response times. - 
Average: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
- 
Maximum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 500 ms; red if the response time is greater than or equal to 500 ms 
- 
Minimum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
 
- 
- Outbound - Response Time by Flow
- 
The average, minimum, and maximum outbound response time, grouped by flow. Anypoint Monitoring uses the average of data collected over one minute to calculate minimum and maximum response times. - 
Average: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
- 
Maximum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 500 ms; red if the response time is greater than or equal to 500 ms 
- 
Minimum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
 
- 
- Inbound - Requests by Flow
- 
The sum of inbound requests, grouped by flow. 
- Outbound - Requests by Flow
- 
The sum of outbound requests, grouped by flow. 
- Failures by Flow
- 
The sum of inbound failed requests, grouped by flow. 
- Inbound - Slow Requests by Flow
- 
The sum of inbound requests whose response time is greater than 1000 ms, grouped by flow. 
- Outbound - Slow Requests by Flow
- 
The sum of outbound requests whose response time is greater than 1000 ms, grouped by flow. 

### Connectors

If you don’t see the **Connectors** tab, verify that:

- 
You have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform. 
- 
The app you selected is a hybrid app deployed to a server, server group, or cluster. 

For more information, see [Monitor Connectors](monitor-connectors).

The following charts appear on the **Connectors** dashboard:

- Connector Message Volume
- 
The number of outbound requests, grouped by connector type. 
- Response Time by Connector
- 
The average outbound response time grouped by connector type. 
- Salesforce Requests
- 
The average number of Anypoint Connector for Salesforce (Salesforce Connector) requests, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Salesforce Response Time
- 
The average response time of Anypoint Connector for Salesforce (Salesforce Connector) requests. 
- Salesforce Failures
- 
The average number of Anypoint Connector for Salesforce (Salesforce Connector) requests failures, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Database Requests
- 
The average number of Anypoint Connector for Database (Database Connector) requests, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Database Response Time
- 
The average response time of Anypoint Connector for Database (Database Connector) requests. 
- Database Failures
- 
The average number of Anypoint Connector for Database (Database Connector) requests failures, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- HTTP Requests
- 
The average number of Anypoint Connector for HTTP (HTTP Connector) requests, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- HTTP Response Time
- 
The average response time of Anypoint Connector for HTTP (HTTP Connector) requests. 
- HTTP Failures
- 
The average number of Anypoint Connector for HTTP (HTTP Connector) requests failures, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Web Services Requests
- 
The average number of Anypoint Connector for Web Service Consumer (Web Service Consumer Connector) requests, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Web Services Response Time
- 
The average number of Anypoint Connector for Web Service Consumer (Web Service Consumer Connector) request failures. 
- Web Services Failures
- 
The average response time of Anypoint Connector for Web Service Consumer (Web Service Consumer Connector) requests, grouped by connector type. 
- FTP Requests
- 
The average number of Anypoint Connector for FTP (FTP Connector) requests, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- FTP Response Time
- 
The average response time of Anypoint Connector for FTP (FTP Connector) requests. 
- FTP Failures
- 
The average number of Anypoint Connector for FTP (FTP Connector) request failures, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- SFTP Requests
- 
The average number of Anypoint Connector for SFTP (SFTP Connector) requests, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- SFTP Response Time
- 
The average response time of Anypoint Connector for SFTP (SFTP Connector) requests. 
- SFTP Failures
- 
The average number of Anypoint Connector for SFTP (SFTP Connector) request failures, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- SMTP Requests
- 
The average number of Anypoint Connector for Email (Email Connector) requests, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- SMTP Response Time
- 
The average response time of Anypoint Connector for Email (Email Connector) requests. 
- SMTP Failures
- 
The average number of Anypoint Connector for Email (Email Connector) request failures, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Object Store Requests
- 
The average number of Object Store Connector request failures, grouped by operation. 
- Object Store Response Time
- 
The average response time of Object Store Connector requests, grouped by operation. 
- Object Store Failures
- 
The average number of Object Store Connector request failures, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Anypoint MQ Operations - Inbound
- 
The average number of Anypoint MQ Connector inbound requests, grouped by operation. 
- Anypoint MQ Response Time - Inbound
- 
The average response time of Anypoint MQ Connector inbound requests, grouped by operation. 
- Anypoint MQ Failures - Inbound
- 
The average number of inbound requests of Connectors of type Anypoint MQ Connector, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Anypoint MQ Operations - Outbound
- 
The average number of Anypoint MQ Connector outbound requests, grouped by operation 
- Anypoint MQ Response Time - Outbound
- 
The average response time of Anypoint MQ Connector outbound request failures, grouped by operation. 
- Anypoint MQ Failures - Outbound
- 
The average number of outbound requests of Connectors of type Anypoint MQ Connector, grouped by top occurring operation. For more information about which operations appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics).
- Other Connector Requests
- 
The average number of requests of Connectors of type `other`.
- Other Connector Response Time
- 
The average response time of requests for connectors of type `other`.
- Other Connector Failures
- 
The average number of requests failures of connectors of type `other`.

### Performance

The following charts appear on the **Performance** dashboard:

- Mule Messages
- 
The number of Mule messages processed in the runtime, grouped in automatic intervals. 
- Average Response Time
- 
The average time to process Mule messages in the Mule application. 
- Inbound - Average Response Time
- 
The average response time of inbound requests. 
- Inbound - Response Time by Endpoint
- 
The average, maximum, and minimum response times, grouped by top occurring endpoint. Anypoint Monitoring uses the average of data collected over one minute to calculate minimum and maximum response times. For more information about which endpoints appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics). Cell color varies according to the following thresholds:- 
Average: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
- 
Maximum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 500 ms; red if the response time is greater than or equal to 500 ms 
- 
Minimum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
 
- 
- Inbound - Response Time graphs (99, 90, 75, and 50 percentiles)
- 
The response time of the 99th, 90th, 75th, and 50th percentile of inbound requests, grouped by application. 
- Outbound - Average Response Time
- 
The average response time of outbound requests. 
- Outbound - Response Time by Endpoint
- 
The average, maximum, and minimum response times, grouped by endpoint. Anypoint Monitoring uses the average of data collected over one minute to calculate minimum and maximum response times. For more information about which endpoints appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics). Cells color varies according to the following thresholds:- 
Average: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
- 
Maximum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 500 ms; red if the response time is greater than or equal to 500 ms 
- 
Minimum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
 
- 
- Outbound - Response Time graphs (99, 90, 75, and 50 percentiles)
- 
The response time of the 99th, 90th, 75th, and 50th percentile of outbound requests. 

### Failures

*Inbound failed requests* occur when there are exceptions in Mule flows.

*Outbound failed requests* occur when outbound connectors are invoked and exceptions occur. These exceptions prompt 400- and 500-status codes. Outbound failed requests may also appear for other types of exceptions.

The following charts appear on the **Failures** dashboard:

- Errors
- 
The number of errors from processing Mule messages in the Mule application. 
- Inbound - Total Failed Requests
- 
The sum of failed inbound requests in the period. 
- Outbound - Total Failed Requests
- 
The sum of failed outbound requests in the period. 
- Inbound - Total Requests by Response Type
- 
The sum of inbound requests, grouped by type of response and automatic interval. 
- Outbound - Total Requests by Response Type
- 
The sum of inbound requests, grouped by type of response and automatic interval. 
- Inbound - Failure Response Time by Endpoint
- 
The average, maximum, and minimum response times of failed inbound requests, grouped by endpoint. Anypoint Monitoring uses the average of data collected over one minute to calculate minimum and maximum response times. For more information about which endpoints appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics). Cell color varies according to the following thresholds:- 
Average: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
- 
Maximum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 500 ms; red if the response time is greater than or equal to 500 ms 
- 
Minimum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
 
- 
- Inbound - Total Failed Requests by Endpoint
- 
The sum of failed inbound requests, grouped by endpoint. 
- Outbound - Failure Response Time by HTTP endpoint
- 
The average, maximum, and minimum response times of failed outbound requests, grouped by endpoint. Anypoint Monitoring uses the average of data collected over one minute to calculate minimum and maximum response times. For more information about which endpoints appear, see the section about [endpoint and operation data collection](#endpoint-operation-metrics). Cell color varies according to the following thresholds:- 
Average: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
- 
Maximum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 500 ms; red if the response time is greater than or equal to 500 ms 
- 
Minimum: Green if the response time is less than 300 ms; yellow if the response time is greater than 300 ms and less than 600 ms; red if the response time is greater than or equal to 600 ms 
 
- 
- Outbound - Total Failed Requests by HTTP Endpoint
- 
The sum of failed outbound requests, grouped by endpoint. 

### JVM

Anypoint Monitoring collects JVM metrics based on the JVM CPU and not the system CPU. As such, CPU metrics found in Cloudwatch reports are higher than JVM metrics in Anypoint Monitoring.

The following charts appear on the **JVM** dashboard:

- Old Gen GC Count
- 
The total number of JVM Old Gen garbage collections (GC) that have occurred, grouped by worker. 
- Old Gen GC Time
- 
The approximate accumulated JVM Old Gen garbage collection (GC) time elapsed, grouped by worker. 
- Young Gen GC Count
- 
The total number of JVM Young Gen garbage collections (GC), grouped by worker. 
- Young Gen GC Time
- 
The approximate accumulated JVM Young Gen garbage collection (GC) time elapsed, grouped by worker. 
- Classes Loaded
- 
The total number of loaded classes, grouped by worker. 
- Classes Loaded Total
- 
The number of classes loaded since JVM start, grouped by worker. 
- Classes Unloaded
- 
The total number of classes unloaded since JVM start, grouped by worker. 
- Heap Committed
- 
The amount of heap memory committed by the JVM, grouped by worker. 
- Heap Used
- 
The amount of heap memory utilized by the JVM, grouped by worker. 
- Thread Count
- 
The total number of threads of the JVM, grouped by worker. 
- JVM Uptime
- 
The time elapsed since the JVM started, grouped by worker. 
- Eden Space graphs (Used, Max, Init, and Committed)
- 
The memory metrics for JVM Eden space, grouped by worker. 
- Survivor Space graphs (Used, Max, Init, and Committed)
- 
The memory metrics for JVM Survivor space, grouped by worker. 
- Metaspace graphs (Used, Max, Init, Committed)
- 
The memory metrics for JVM metaspace, grouped by worker. 
- Code Cache graphs (Used, Max, Init, Committed)
- 
The memory metrics for JVM code cache, grouped by worker. 
- Compressed Class Space graphs (Used, Max, Init, Committed)
- 
The memory metrics for JVM compressed class, grouped by worker. 
- Old Gen Mem graphs (Used, Max, Init, Committed)
- 
The memory metrics for JVM Old Gen space, grouped by worker. 
- Committed Virtual Memory
- 
The amount of virtual memory guaranteed to be available to the running process, grouped by worker. This metric is available only for organizations that have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform. 

### Infrastructure

The following charts appear on the **Infrastructure** dashboard:

- JVM - CPU % Utilization
- 
The average percentage of CPU utilized by the JVM, grouped by worker. The JVM used in this chart is the Mule JVM process. The calculation for CPU utilization is relative to the physical server on which the Mule runtime is deployed. For example, in RTF, the resource usage here indicates the JVM’s utilization with respect to the entire server and not with respect to the pod maximum CPU allocation. 
- JVM - Heap Used
- 
The average amount of heap memory utilized by the JVM, grouped by worker. The JVM used in this chart is the Mule runtime JVM process. 
- Total System Processors
- 
The number of CPU processors available to the Java virtual machine for each worker. 
- System Memory
- 
The amount of system memory available for workers over time. 
- JVM Thread Count
- 
The average number of threads of the JVM, grouped by worker. 
- System CPU % Utilization
- 
The percentage of CPU used by all processes. This metric often aligns with the Cloudwatch System CPU % metric, but there may be different values given the timing of data aggregation for Anypoint Monitoring metrics. This metric is available only for organizations that have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform. 
- JVM CPU Time
- 
The cumulative CPU time consumed by the JVM. This metric is available only for organizations that have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform. 
- Operating System Swap Space
- 
The amount of memory the system is swapping, grouped by worker in automatic intervals. This metric is available only for organizations that have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform. 

### Custom Metrics

The **Custom metrics** tab appears only if your organization has the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform and the app you selected is running on a supported version of Mule. See [Anypoint Custom Metrics Connector](anypoint-custom-metrics-connector).

## Application Network

The **Custom metrics** tab appears only if your organization has the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform and the app you selected is running on a supported version of Mule. See [Anypoint Custom Metrics Connector](anypoint-custom-metrics-connector).

Setup requirements change based on your app deployment. Some deployment types require you to enable header injection or modify how API Visualizer (formerly Anypoint Visualizer) collects data. For more information, see the documentation for each deployment type:

The chart on the **Application Network** tab shows the [Troubleshooting visualization](../visualizer/troubleshooting-visualization) for the selected app, which must be started. The chart shows only direct callers and callees for the selected app. The connections are based on the selected time range, with a max of the most recent seven days.

You can click **Metrics** to see statistics, such as average response time and failures, related to the app you selected. For more information about metrics in API Visualizer, see [Choosing Your Metric](../visualizer/troubleshooting-visualization#choosing-your-metric).

## Endpoint and Operation Metrics Collection (Other Group)

Anypoint Monitoring collects top occurring endpoints or operations for each data collection interval. Endpoints or operations that are not top occurring are sorted into a group called **Other**. This grouping applies to built-in and custom metrics.

In each data collection interval, top occurring endpoints or operations vary. An endpoint or operation that is top occurring in one interval might not be top occurring in the next.

In Anypoint Monitoring charts and tables, the data comes from multiple data collection intervals. As a result, aggregated data shown in the dashboard is an estimation since the intervals might not have the same top occurring endpoints or operations. The tables show approximate counts for the most commonly occurring endpoints or operations when the **Other** grouping appears.

For example, when an endpoint occurs more often than other endpoints in one interval but less often in another interval, Anypoint Monitoring sorts it into the Other group for the first interval. In this case, the resulting table displays lower than actual values for that endpoint, since the metrics that do not appear are grouped into the **Other** group.

## How Data is Aggregated in Intervals

Anypoint Monitoring aggregates data in charts based on the selected time interval. The number of data points shown in a chart varies based on your selected time interval.

## Charting Inactivity for Average Response Time

To ensure charts are plotted continuously without interruptions, all average response time charts use a straight line to connect the last available value that precedes a period of app or API inactivity with the next available value. To understand activity in average response time charts, consider behavior in related charts, such as request counts, to get a holistic idea of your API or app’s activity.

## App Chart Mapping (Built-in and Insights Dashboards)

Charts and visualizations in the built-in dashboards and Anypoint Insights share application metrics.

| Built-in Dashboard Tab for an App | Built-in Dashboard Chart | Anypoint Insights Tab for an App | Anypoint Insights Chart | 
|---|---|---|---|
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | 
 | ||
| 
 | Charts that use your organization’s custom metrics. |