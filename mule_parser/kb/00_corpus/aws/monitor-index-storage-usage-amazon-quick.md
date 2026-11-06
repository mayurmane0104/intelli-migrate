# Monitor index storage usage - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/index-usage-monitoring.html](https://docs.aws.amazon.com/quick/latest/userguide/index-usage-monitoring.html)

---

Index usage logs provide visibility into how your Amazon Quick index storage is consumed across knowledge bases and Spaces, including file uploads. You can use these logs to track growth trends, identify the largest sources, detect unexpected spikes, and plan capacity.

Before you query index usage data, you must configure
        `INDEX_USAGE_LOGS` delivery. For instructions on setting up
        delivery, see
        [Monitoring Amazon Quick usage using CloudWatch Logs](./monitoring-quicksuite-chat-feedback-cloudwatch.html).

## Log schema

        Each index usage log event includes the common fields that are shared
            across all Amazon Quick log types, such as `resource_arn`,
            `event_timestamp`, `log_type`,
            `account_id`, and `user_arn`. The event also
            includes the following index-specific fields:

| Field | Type | Description | 
|---|---|---|
| `consumed_index_size` | Integer | Total size (in bytes) consumed by the entire index. This is the authoritative total. | 
| `source_type` | String | `SPACE`or`KB`. | 
| `source_name` | String | Display name of the Space or knowledge base. | 
| `source_arn` | String | Full ARN of the source. | 
| `consumed_source_size` | Integer | Size (in bytes) consumed by this individual source. | 
| `consumed_source_doc_count` | Integer | Number of documents in this source. | 

###### Note

Events are published per source on change. Not all sources emit
                events every day. To reconstruct the current state, use the most
                recent event per `source_arn`.

## CloudWatch Logs Insights queries

        The following CloudWatch Logs Insights queries help you analyze index usage
            data. All queries use the pattern
            `stats latest(field) by source_arn` to get the most recent
            state per source. The queries then aggregate as needed. Replace
            `YOUR_LOG_GROUP` with your log group name.

### Size by source type (knowledge bases compared to Spaces)

Shows the total size split between knowledge bases and Spaces.

```
fields @timestamp, source_type, source_arn, consumed_source_size
| stats latest(consumed_source_size) as latest_size, latest(source_type) as type by source_arn
| stats sum(latest_size) as total_size by type
```
### Total index size over time

Shows the index size trend by using the
                `consumed_index_size` field.

```
fields @timestamp, consumed_index_size
| stats latest(consumed_index_size) as total_index_size by bin(1d) as day
| sort day asc
```
### Top knowledge bases by size

Shows the top 20 knowledge bases ranked by size.

```
fields @timestamp, source_type, source_arn, source_name, consumed_source_size
| filter source_type = "KB"
| stats latest(consumed_source_size) as latest_size, latest(source_name) as name by source_arn
| sort latest_size desc
| limit 20
```
### Top Spaces by size

Shows the top 20 Spaces ranked by size.

```
fields @timestamp, source_type, source_arn, source_name, consumed_source_size
| filter source_type = "SPACE"
| stats latest(consumed_source_size) as latest_size, latest(source_name) as name by source_arn
| sort latest_size desc
| limit 20
```
### All sources detail

Shows the latest state of every source with size, type, name, document count, and last update time.

```
fields @timestamp, source_type, source_name, consumed_source_size, consumed_source_doc_count, source_arn
| stats latest(consumed_source_size) as latest_size, latest(source_type) as type, latest(source_name) as name, latest(consumed_source_doc_count) as doc_count, latest(@timestamp) as last_updated by source_arn
| sort latest_size desc
| limit 100
```
### Top users by total size

Shows the top 20 users ranked by total source size across all their sources.

```
fields @timestamp, user_arn, source_arn, consumed_source_size
| parse user_arn "*:user/*/*" as @prefix, @namespace, @username
| stats latest(consumed_source_size) as latest_size, latest(@username) as user by source_arn
| stats sum(latest_size) as total_size by user
| sort total_size desc
| limit 20
```
## Create a CloudWatch dashboard

        You can create a CloudWatch dashboard to visualize index usage metrics. Use the CloudWatch console to create a dashboard and add Logs Insights widgets by using the queries from the preceding section.

- 
                Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch).
- 
                In the navigation pane, choose **Dashboards**.
- 
                Choose **Create dashboard**and enter a name (for example,`IndexUsageMetrics`).
- 
                Add widgets by using the **Logs**widget type. Select your index usage log group and paste the queries from the preceding section.

###### Tip

Use the pie chart visualization for the source type breakdown. Use the line chart for size over time. Use the bar chart for top sources. The table visualization works well for the all-sources detail query.