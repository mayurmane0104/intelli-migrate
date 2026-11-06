# Using Logs in Anypoint Monitoring (US and EU) | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/logs-us-eu](https://docs.mulesoft.com/monitoring/logs-us-eu)

---

![Logs in Anypoint Monitoring](_images/intro-logs.png) 

# Using Logs in Anypoint Monitoring (US and EU)

[Advanced and Titanium tiers](/monitoring/#billing)

On [US](https://anypoint.mulesoft.com/monitoring) and [EU](https://eu1.anypoint.mulesoft.com/monitoring) Clouds, Anypoint Monitoring aggregates log files so you can manage, search for, filter, and analyze your logs. You can use aggregated logs in conjunction with monitoring to help identify issues and investigate failures quickly. These features support:

- 
Comparative analysis and identification of event and information patterns based on searches across selected Mule apps and environments. 
- 
Searches within the logs of a specific worker (or set of workers) for a Mule app so that you can narrow scope of issues to check. 
- 
Sharing a snapshot of important logs with developers who can work on the source of the issue. 

You can also search for individual application logs in Runtime Manager, see [View Log Data](../cloudhub/viewing-log-data).

| 
 Logs produced by apps with customized logging (by changing the pattern layout in the  
 
 Do not override the default JVM timezone for applications deployed to CloudHub and Anypoint Runtime Fabric with customized time zones. The timezone must be UTC. Changing the timezone to a local timezone causes logs to be indexed in Anypoint Monitoring with incorrect timestamps. | 

## Search Logs

In the sidebar, click **Log Search** to search for text in logs from the search field, through a filter, or with a DSL query.

![Logs in Anypoint Monitoring](_images/intro-logs.png) 

When you search for logs for APIs deployed through Omni Gateway (formerly Flex Gateway), use the **Application** filter. Use the **App ID** field to identify the instance.

### Search from the Log Search Field

To search the logs, type your search query into the log search field and press **Enter**.

- 
Search for a term, such as `"Info Dynamic Logging"`.Without quotes, the query returns results for matches to each term. 
- 
Use a wildcard in your search, such as `appId=myap*`.
- 
Use logical operators, such as `appId=myap* AND "Info Dynamic Logging"`.

### Search with a Filter

You can create a filter to search logs using predefined fields, operators, and values.

- 
Click **+Add a filter**.
- 
Select the predefined field from the drop-down list. - 
`application`
- 
`class`
- 
`environment`
- 
`environment type`
- 
`log level`
- 
`logger`
- 
`message`
- 
`thread`
- 
`timestamp`
- 
`worker`
 
- 
- 
Select the operator from the drop-down list. Operators vary by the field you select. 
- 
If applicable, enter a value, for example: ![A form to add a filter for errors](_images/log-filter-example.png)  See [Search Filters](#filters_predefined)and[Operators](#operators).
- 
(Optional) Enter a value in **Label**.
- 
Click **Save**.- NOTE
- 
Results for the **Application**filter include APIs deployed through Omni Gateway (formerly Flex Gateway).
 

### Search with the Query DSL

To convert a search query into a Query DSL:

- 
Click **+Add a filter**.
- 
Click **Edit Query DSL**.
- 
Enter your query, and click **Save**.
 This example shows a query for log-level INFO:`{ "query": { "match": { "log-level": { "query": "INFO", "type": "phrase" } } } }`textThe search query UI provides a link to the query documentation so that you can perform more complex queries than otherwise available. This example shows a complex query. 

```
{
  "query": {
    "range": {
      "workerId": {
        "gte": 0,
        "lte": 20
      }
    }
  }
}
```
| Some complex search queries do not have an equivalent in the search filter values UI, so you can only create and view such queries in the query UI. | 

## View Log Data

By default, the log entries in your log search results are abbreviated. You can expand and view the log message and details as a table or in JSON format.

![A log file entry](_images/log-expanded.png) 

### Tabular Logs

This example shows an expanded log entry as a table. The table contains log filter fields that you see in the Quick Filter list.

`application abcd40x.us-a1.abc.cloudhub.io class qtp437897409-31 environment Sandbox environment type %{[fields][env_type]} log level ERROR logger DefaultMessagingExceptionStrategy message **************************************************** Message : No record could be found in payload or in flow variable BATCH_RECORD (java.lang.IllegalStateException). Element : null ---------------------------------------------------- Exception stack is: No record could be found in payload or in flow variable BATCH_RECORD (java.lang.IllegalStateException). (org.mule.api.transformer.... (72 more...) (set debug level logging or '-Dmule.verbose.exceptions=true' for everything) **************************************************** timestamp April 25th 2024, 17:09:53.517 worker 0`text

### JSON-Formatted Logs

This example shows an expanded log entry in JSON format.

```
{
  "_version": 1,
  "_source": {
    "class": "qtp437897409-31",
    "logger": "DefaultMessagingExceptionStrategy",
    "_ending": 0,
    "timestamp": "2024-11-26T00:09:53.517Z",
    "message": ".Example***
    .ExampleMessage: No record could be found in payload or in flow variable
    BATCH_RECORD (java.lang.IllegalStateException)..ExampleElement...",
    "log level": "ERROR",
    "worker": "0",
    "environment": "Sandbox",
    "environment type": "sandbox",
    "application": "test40x.us-e1.qax.cloudhub.io"
  },
  "fields": {
    "timestamp": [
      "2024-11-26T00:09:53.517Z"
    ]
  },
  "highlight": {
    "orgId": [
      "@abcde@6046b96d@/..."
    ]
  },
  "sort": [
    1524701393517
  ]
}
```
json## Get Logs for Agentic Assets

API Manager and Agent Visualizer provide links to logs for agentic assets (agent, broker, and MCP server instances):

- 
In Agent Visualizer, click a node in the visual graph, and navigate to logs. For guidance, see [Access Logs](../agent-visualizer/troubleshoot-agent-network#access-logs)in the Agent Visualizer documentation.For more information about Agent Visualizer, see [Agent Visualizer Overview](../agent-visualizer/).
- 
In API Manager, navigate to **Agent and Tool Instances**, and click an instance:- 
To find logs for policies applied to agents, brokers, and MCP servers, click **Message Log**, and then click**View logs in Anypoint Monitoring**.
- 
For a broker’s reasoning logs, click **Message Log**, and then click the button dedicated to the broker. These logs come from the broker application.By default, broker logs include the actions the broker takes (including agents called and MCP tools executed), but they don’t include reasoning data due to potential logging of personally identifiable information. If your organization opts to enable a broker’s reasoning logs, set the broker’s `category`field in Runtime Manager:`INSECURE-LOGGING`category to`DEBUG`
 
- 

### View Full Logs on a Dedicated Page

After finding a log on a particular issue, you can view the complete log on a dedicated page (without the quick filters, search field, and filter tags). You can view the log detail in tabular or JSON format.

- 
From the selected log, click **View This Log**.![View This Log feature](_images/logs-view-surrounding.png)  
- 
View the extended log in tabular or JSON format. ![Extended logs example](_images/logs-view-extended.png)  

## View Surrounding Logs

After finding a log for a particular issue, you might want to know what other log reports preceded or followed it.

- 
From the selected log, click **View Surrounding Logs**.![View Surrounding Logs tab](_images/logs-view-surrounding.png)  
- 
Load the number of logs that you want to see before and after the selected log, or use the default. ![Surrounding logs view example](_images/logs-set-surrounding.png)  

The default settings are:

- 
**Load 5 more**newer logs
- 
**Load 5 more**older logs

## Working with Predefined Filters

When the **Quick Filters** list is open, you can select and use predefined log filters.

| For every result group, the Quick Filterslist displays the first five results of the most recent 500 log entries. When there are more than 500 entries or the top five values do not represent 100% of total values, aSee Morelink for each result group appears. You can clickSee Moreto open theAdd a Filterbox and set parameters to further filter your results. | 

This example of a predefined filter selects the ERROR log level.

![Predefined log filter](_images/log-filter-select.png) 

After you select a predefined filter from the Quick Filter list, you see it
near the top of the page, next to **Add a Filter**.

![Predefined filter actions](_images/log-filter-actions.png) 

When you hover over a filter, you can select from the following actions:

- 
**Enable/Disable**- Enables or disables the filter. When the filter is disabled, it is grayed out.
- 
**Pin/Unpin**- Pin or unpin the filter.
- 
**Invert**- Change the operation of the search filter. For example, if the search is`log level IS ERROR`, the inversion is`log level IS NOT ERROR`.
- 
**Remove**- Delete the filter.
- 
**Edit**- Change the filter configuration.

### Adding Filter Columns to Logs

From the Quick Filters list, you can add and remove columns to or from log results. For example, you might add the Log Level, Timestamp, or Environment field.

Click the column icon for a filter field, for example:

![Log filter column example](_images/log-filter-add-field.png) 

The resulting `log-level` column looks like this in the logs:

![Filter column in the logs](_images/log-filter-column.png) 

To remove the filter column, click the column icon for the filter field, for example:

![Column icon for removing the column from the logs](_images/log-filter-remove-field.png) 

You can also remove it with the [X icon](#column_move) that appears when you scroll over the column.

## Moving Filter Columns

To move filter columns in your log results to the left or right, you simply scroll over the column heading and use the arrow icons.

![Arrow icons for moving a filter column to the left or right](_images/log-filter-column-move.png) 

### Search Filters

Use predefined filters or filters that you create.

| Filter | Description | Examples | 
|---|---|---|
| 
 | Full domain of the Mule app in CloudHub. | 
 | 
| 
 | Java class that generates the log. | 
 | 
| 
 | CloudHub environment name. | 
 | 
| 
 | CloudHub environment type | 
 | 
| 
 | ALL, DEBUG, ERROR, FATAL, INFO, OFF, TRACE, WARN | 
 | 
| 
 | Log4J Logger class | 
 | 
| 
 | Log4J message | 
 | 
| 
 | Timestamp on the log. Accepted formats:  | Supported time settings are  
 | 
| 
 | CloudHub worker ID. | 
 | 

### Operators

You can use these operators when creating a search filter. For example `log-level IS`

| 
 | Available to all filters. | 
| 
 | Available to all filters. | 
| 
 | Available to  | 
| 
 | Available to  | 
| 
 | Available to all filters. | 
| 
 | Available to all filters. | 

## Filtering Based on the Entire Log Field Value

You can use the funnel-shaped icons on any log in your results to create and remove a filter for the entire log field value.

![Funnel icon used to create a log message filter](_images/log-filter-create-funnel.png) 

The filter you create is visible as a filter tag in the Filters area at the top of the page, for example:

![Log message filter tag](_images/log-filter-tag.png) 

You can edit and use that filter like any other filter. See [Search Filters](#filters_predefined).

## Share Logs

You can share the URL to your logs.

- 
From Logs, click **Share**.
- 
Select **Share**to load the URL of your log page to a**Share Logs Search Link**field.
- 
Click **Copy**.

## Save and View Saved Log Searches

Save and view log searches.

- 
Click **Save Search**.
- 
Select **View saved searches**.
- 
Click **View Saved Searches**again to return to the main Logs page.

## Clear a Search

You can clear the current search from the same menu shown in [Save and View Saved Log Searches](#save_view_log_searches):

- 
Click **Save Search**.
- 
Select **Clear Current Search**.