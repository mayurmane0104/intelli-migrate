# Using Built-in API Dashboards | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/api-dashboard](https://docs.mulesoft.com/monitoring/api-dashboard)

---

- 
Request Volume 
- 
Failed Requests 
- 
Total 4xx Errors 
- 
Total 5xx Errors 
- 
Policy Violations 
- 
Average Response Time 

# Using Built-in API Dashboards

The API dashboards provide charts to monitor API usage, which gives you insight into how your APIs are used and how they are performing.

If you have [enabled API auto-discovery](../mule-gateway/mule-gateway-autodiscovery-overview), your API metrics are available in the API dashboards in Anypoint Monitoring.

The enhanced metrics view includes detailed information about your APIs, and charts are sorted into dashboards based on the type of data displayed.

Charts displaying the `Last 1 hour` label show data that was collected during the past 60 minutes, starting with the current time.

| For [Gold and Platinum subscriptions](./#plans-legacy), Anypoint Monitoring retains API metrics data for 30 days. API Manager retains API metrics data for 30 days. | 

## Supported Versions of Mule Runtime Engine

Run your Mule app on a supported Mule runtime version. For supported versions, see [Mule Runtime Release Notes](../release-notes/mule-runtime/mule-esb).

## View the API Dashboard

- 
Log in to Anypoint Platform with a user account that has [permission to access Anypoint Monitoring content](am-permissions).
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
In the sidebar, click **Built-in dashboards**.
- 
In **Built-in dashboards**, select the**Environment**,**Resource name**, and**Version/Instance**for the API to view.
- 
Click **View**.On the dashboard, you can view information about a running, managed API. 
- 
Select the date and time range to view the statistics for and click **Confirm**.

## Enhanced Metrics View for API Dashboards

API dashboards provide you with various pages from which you can view different types of charts.

The following charts are available in the enhanced metrics view for APIs:

| API Dashboards | Charts | 
|---|---|
| 
 | |
| 
 | |
| 
 | |
| 
 | 

### Overview Charts

The following charts appear on the **Overview** dashboard:

- Request Volume
- 
The sum of requests in the selected time period for the given API. Data is aggregated in one minute increments. 
- Failed Requests
- 
The sum of failed requests in the selected time period for the given API. Data is aggregated in one minute increments. 
- Total 4xx Errors
- 
The sum of 400 errors (such as 404, 408, and so on) in the selected time period for the given API. 
- Total 5xx Errors
- 
The sum of 500 errors (such as 500, 502, and so on) in the selected time period for the given API. 
- Policy Violations
- 
The sum of requests for policy violations in the selected time period, grouped by policy violation ID. Data is aggregated in one minute increments. 
- Average Response Time
- 
The average response time of requests in the selected time period for the given API. Data is aggregated in one minute increments. 

### Requests Charts

The following charts appear on the **Requests** dashboard:

- Requests
- 
The sum of requests in the selected time period, grouped by the top N paths. By default, N is 100. - 
If you select a time range within the last hour, data is aggregated in one minute increments. 
- 
If you select a time range within the last day, data is aggregated in ten minute increments. 
- 
If you select a time range that is larger than one day, data is aggregated in one hour increments. This metric isn’t supported for APIs deployed through Omni Gateway (formerly Flex Gateway). 
 
- 
- Requests by Method
- 
The sum of requests in the selected time period, grouped by method. Data is aggregated in one minute increments. 
- Requests by Response Code
- 
The sum of requests in the selected time period, grouped by response code. Data is aggregated in one minute increments. 
- Requests by Request Size
- 
The sum of requests in the selected time period, grouped by request size. Data is aggregated in one minute increments. 
- Requests by Response Size
- 
The sum of requests in the selected time period, grouped by response size. Data is aggregated in one minute increments. 

### Failures Charts

The following charts appear on the **Failures** dashboard:

- Failures
- 
The sum of failed requests in the selected time period, grouped by the top N paths. By default, N is 100. - 
If you select a time range within the last hour, data is aggregated in one minute increments. 
- 
If you select a time range within the last day, data is aggregated in ten minute increments. 
- 
If you select a time range that is larger than one day, data is aggregated in one hour increments. This metric isn’t supported for APIs deployed through Omni Gateway (formerly Flex Gateway). 
 
- 
- Failures by Method
- 
The sum of failed requests in the selected time period, grouped by method. Data is aggregated in one minute increments. 
- Requests by Response Code
- 
The sum of failed requests in the selected time period, grouped by response code. Data is aggregated in one minute increments. 
- Requests by Request Size
- 
The sum of failed requests in the selected time period, grouped by request size. Data is aggregated in one minute increments. 
- Requests by Response Size
- 
The sum of failed requests in the selected time period, grouped by response size. Data is aggregated in one minute increments. 

### Performance Charts

These charts appear on the **Performance** dashboard:

- Requests by Performance
- 
The average request response times, grouped by path. - 
If you select a time range within the last hour, data is aggregated in one minute increments. 
- 
If you select a time range within the last day, data is aggregated in ten minute increments. 
- 
If you select a time range that is larger than one day, data is aggregated in one hour increments. This metric isn’t supported for APIs deployed through Omni Gateway (formerly Flex Gateway). 
 
- 
- Slow Requests
- 
The average response times that are greater than one second, grouped by path. 
 This chart is available only if your organization has the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform.- 
If you select a time range within the last hour, data is aggregated in one minute increments. 
- 
If you select a time range within the last day, data is aggregated in ten minute increments. 
- 
If you select a time range that is larger than one day, data is aggregated in one hour increments. This metric isn’t supported for APIs deployed through Omni Gateway (formerly Flex Gateway). 
 
- 

### Client Applications Charts

The following charts appear on the **Client Applications** dashboards:

- Requests by Client ID
- 
The sum of requests in the period, grouped by client ID. Data is aggregated in one minute increments. 
- Requests by Client IP
- 
The sum of requests in the period, grouped by client IP address. - 
If you select a time range within the last hour, data is aggregated in one minute increments. 
- 
If you select a time range within the last day, data is aggregated in ten minute increments. 
- 
If you select a time range that is larger than one day, data is aggregated in one hour increments. This metric isn’t supported for APIs deployed through Omni Gateway (formerly Flex Gateway). 
 
- 
- Requests by Location
- 
The sum of requests during the time period specified, grouped by country. Data retention for the Requests by Location chart is one hour. This metric isn’t supported for APIs deployed through Omni Gateway (formerly Flex Gateway). 

For information about chart metric collection, including the chart group **Other**, see [How Endpoint and Operation Use Metrics Are Gathered](app-dashboards#endpoint-operation-metrics).

## Endpoint and Operation Metrics Collection (Other Group)

Anypoint Monitoring collects top occurring endpoints or operations for each data collection interval. Endpoints or operations that are not top occurring are sorted into a group called **Other**. This grouping applies to built-in and custom metrics.

In each data collection interval, top occurring endpoints or operations vary. An endpoint or operation that is top occurring in one interval might not be top occurring in the next.

In Anypoint Monitoring charts and tables, the data comes from multiple data collection intervals. As a result, aggregated data shown in the dashboard is an estimation since the intervals might not have the same top occurring endpoints or operations. The tables show approximate counts for the most commonly occurring endpoints or operations when the **Other** grouping appears.

For example, when an endpoint occurs more often than other endpoints in one interval but less often in another interval, Anypoint Monitoring sorts it into the Other group for the first interval. In this case, the resulting table displays lower than actual values for that endpoint, since the metrics that do not appear are grouped into the **Other** group.

## Anypoint Monitoring Archive API

| 
 | 

You can access API analytics metrics data directly via the Anypoint Monitoring Archive API. Using this API, you can navigate and discover your API metrics data using a directory hierarchy.

The Anypoint Monitoring Archive API enables you to download files that contain [JSON objects](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/anypoint-monitoring-archive-api/minor/1.0/pages/Metric%20Data/) that represent one or more metric events. You can write an application to navigate the data collected by the API and integrate it into your own system.

You can also enable non-aggregated API events by setting this property: `anypoint.platform.config.analytics.agent.api_raw_metrics.enabled=true`.
These events contain more detailed information about each API invocation and can be accessed using the Anypoint Monitoring Archive API under the `raw` file type.

For more information about this API, see [Anypoint Monitoring Archive API](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/anypoint-monitoring-archive-api/minor/1.0/pages/home/) in Anypoint Exchange.

## Charting Inactivity for Average Response Time

To ensure charts are plotted continuously without interruptions, all average response time charts use a straight line to connect the last available value that precedes a period of app or API inactivity with the next available value. To understand activity in average response time charts, consider behavior in related charts, such as request counts, to get a holistic idea of your API or app’s activity.

## API Chart Mapping (Built-in and Insights Dashboards)

Charts and visualizations in the built-in dashboards and Anypoint Insights share API metrics.

| Built-in Dashboard Tab for an API | Built-in Dashboard Chart | Anypoint Insights Tab for an API | Anypoint Insights Chart | 
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
 | 
 | |
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
 | 

## See Also

[Anypoint Monitoring Archive API](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/anypoint-monitoring-archive-api/minor/1.0/pages/home/)