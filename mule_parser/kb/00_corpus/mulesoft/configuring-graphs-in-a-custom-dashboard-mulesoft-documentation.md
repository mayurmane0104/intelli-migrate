# Configuring Graphs in a Custom Dashboard | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/dashboard-custom-config-graph](https://docs.mulesoft.com/monitoring/dashboard-custom-config-graph)

---

![Graph configuration view](_images/dashboard-custom-config-graph.png) 

# Configuring Graphs in a Custom Dashboard

[Advanced and Titanium tiers](/monitoring/#billing)

Configure metrics data in a graph. A custom dashboard graph in Anypoint Monitoring displays metrics for a Mule app or API.

Advanced options support fine-tuned configurations and multiple metrics in a single graph. You can also customize axes, the look of the graph, legends, and behavior of the graph when you hover over a data point.

![Graph configuration view](_images/dashboard-custom-config-graph.png) 

| 1 | Graph example (basic mode) | 
| 2 | Graph configuration tabs: 
 | 
| 3 | Advanced Mode: Switch for enabling[advanced](#mode_advanced)configurationsAdvanced mode supports complex configurations with up to 25 queries. | 

## Create a Graph

Create a graph in a custom dashboard by following the guidance in [Add Charts to a Custom Dashboard](dashboard-custom-config#charts_adding).

## Configure a Graph

Configure a graph in a custom dashboard.

- 
From **Custom Dashboards**, open the custom dashboard that contains your graph.For guidance, see [View a Custom Dashboard](dashboard-custom-config#view).
- 
Click the graph’s ![](_images/more-menu-vert-ellipsis.png) ( (**More menu**), and select**Configure**.
- 
Click the graph’s **General**configuration tab.- 
Provide a title and description. 
- 
Select and configure a graph mode (basic or advanced). For more information, see [General Settings for Basic and Advanced Queries](#general).
 
- 
- 
In the graph’s **Axes**tab, set the graph’s axes or use the defaults.For more information, see [Axes (X-Axis and Y-Axis Settings)](#axes).
- 
In the graph’s **Visuals**tab, set[bars, lines, or points](#visuals)for the graph.
- 
Optionally: - 
In the **Alert**tab, configure an[alert and email notification](#alerts_config).Alerting isn’t available in advanced mode. 
- 
In the **Advanced**tab, provide[advanced configurations](#advanced).
 
- 
- 
Click **Apply Changes**.
- 
Exit the configuration view by clicking the **X**next to the configuration tabs.

## General Settings for Basic and Advanced Queries

**General** tab settings include [basic](#mode_basic) and [advanced](#mode_advanced) modes (or queries) for configuring time-series data. Both configurations share fields for the title and a short description.

| Basic and Advanced Mode Settings | |
|---|---|
| 
 | Title to display in the UI. Defaults to Panel Title. | 
| 
 | Short description to display in the UI when users hover over the information ( | 

Other settings are specific to the setting mode (basic or advanced).

### Basic Mode

In the **General** configuration tab, a basic query selects a single metric for a deployed Mule app or API in a given environment.

| Basic Mode Settings | |
|---|---|
| 
 | From the drop-down menu, select the type of panel to display for the resource ( | 
| 
 | The drop-down menu includes these types of metrics: 
 For a list of basic metrics, see  | 
| 
 | The environment where your application or API is deployed. | 
| 
 | A deployed application. This option is available if you select  | 
| 
 | A deployed API. This option is available if you select  | 
| 
 | The Mule version or instance on which your API is deployed. This option is available if you select  | 

| When you create an application panel using a JVM metric, the query that supports the panel uses only the worker-id for the app. When you modify the panel at a later time, the resource fields are populated with the query content. Because some apps share a worker-id, the resource that appears in the selector might appear to be a different resource from the resource you selected originally. However, all resources share the same worker, so the query has the correct information despite the selector displaying a different resource name. | 

### Advanced Mode

In the **General** configuration tab, advanced mode settings support fine-tuned queries for metrics.

| If you switch back to basic mode, some advanced configuration queries are removed. | 

![Advanced configuration mode is on.](_images/config-general-advanced.png) 

| Advanced Mode Settings for Applications | |
|---|---|
| 
 | Lists metrics, such as  This field provides matching suggestions when you type in a character. For example,  For a list of advanced metrics, see  | 
| 
 | Supports conditional logic for filtering the  
 Grouping  | 
| 
 | Add one or more metric  | 
| 
 | For grouping the data by a selected time interval (such as  Valid values and arguments: 
 | 
| 
 | You can create a label for your metric using a literal string (such as  | 

| Advanced Mode Settings for APIs | |
|---|---|
| 
 | Lists metrics, such as  For a list of advanced metrics, see  | 
| 
 | Provides conditional logic for filtering the metric selected from the  You can select one or more filter tags (such as  | 
| 
 | For creating a function that selects a metric field (such as  | 
| 
 | For grouping the data by a selected time interval (such as  
 | 
| 
 | You can create a label for your metric using a literal string (such as  To use your tag as an alias, the tag must be included in the  | 

## Axes (X-Axis and Y-Axis Settings)

Configure the x-axis and y-axis of your graph in the **Axes** tab.

### Y-Axis Settings

Set a vertical y-axis for the left (Left Y) or right (Right Y) side of your graph.

| Y-Axis Settings | |
|---|---|
| 
 | If unchecked, hides the y-axis from the graph. | 
| 
 | The unit of measurement to use for values on the y-axis.  Values include  | 
| 
 | Valid values for a linear or logarithmic (log) scale for coordinates on the y-axis: 
 | 
| 
 | The minimum value for a y-coordinate. Defaults to  | 
| 
 | The maximum value for a y-coordinate. Defaults to  | 
| 
 | Overrides the automatic decimal precision on y-coordinates, for example, where  | 
| 
 | A string used to label the Y axis. Defaults to  | 

### X-Axis Settings

| X-Axis Settings | |
|---|---|
| 
 | If unchecked, hides the x-axis from the graph. | 
| 
 | Valid values: 
 | 
| 
 | Visible only if  | 
| 
 | Visible only if  | 

After you complete your configuration, you can click Save Changes. To exit the configuration and return to the dashboard, simply click the `X`.

## Visuals (Bar, Line, Data Point Settings)

You can configure the style and look of graph to use. Bar, line, and point graphs are supported.

![Singlestat example](_images/graph-config-visuals.png) 

| Visual Configuration Options | |
|---|---|
| 
 | You can check one or more of these modes: 
 | 
| 
 | Only available when the selected  
 | 
| 
 | 
 | 

## Alerts (Configuration, Notifications, History)

| 
 | 

From a graph’s **Alerts** tab, you can:

#### Configure an Alert

- 
Navigate to the **Alert**configuration tab for a graph that is configured in basic mode.
- 
Click **Add Alert**.
- 
Use **Alert Config**to configure the alert.Settings for Alerts in Custom Dashboards **Name**A title for your alert **Severity level**The severity level of your alert. **Condition****WHEN**: For triggering an alert if the metric rises above a specified level
- 
Configure email notifications when an alert is triggered. Notification Settings for Alerts **Send To**Email address for each recipient of the alert notification. If you add or change the email address of an alert recipient, they don’t receive an email until the alert is triggered. **Message**Message to send to the recipient. 
- 
Click **Save Changes**.
- 
Click **X**to exit the configuration and return to the dashboard.

#### View Alert State History

Use **State history** to view the status of the last 50 alerts.

You can also clear the history.

#### Delete an Alert

Use **Delete** to remove the alert from the graph.

## Advanced (Legends, Thresholds, Stacking, Hovering, Time Shift Settings)

Add and configure legends, thresholds, and other features for your graph.

### Legends (Advanced Setting)

In the **Advanced configuration** tab, configure legends for your graphs.

![Advanced graph settings for a legend](_images/graph-advanced-legend.png) 

| Legend Options | |
|---|---|
| 
 | Unchecking hides the legend. Checked by default. | 
| 
 | Check to display the selected legend Values (such as  | 
| 
 | Check to display the legend on the right side. Unchecked by default. | 
| 
 | Available when  | 

You can also display the following values in a legend:

| Legend Values | |
|---|---|
| Min | Minimum of all values returned from the query | 
| Max | Maximum of all values returned from the query | 
| Avg | Average of all values returned from the query | 
| Current | Last value returned from the query | 
| Total | Sum of all values returned from metric query | 
| Decimals | Overrides automatic decimal precision used in legends and tooltips | 

After you complete your configuration, click **Save Changes**.

To exit the configuration and return to the dashboard, click the **X**.

### Stacking and Hover (Advanced Setting)

In the **Advanced configuration** tab, you can configure a hover tooltip to display information about a data point in a graph when you hover over the value.

![Advanced graph settings, Stack and Hover](_images/graph-advanced-stacking-hover.png) 

| Hover Tooltip Settings | |
|---|---|
| 
 | To display one or all series in the tooltip. | 
| 
 | Displays data in no order (None), Decreasing, or Increasing order. Defaults to None. | 
| 
 | Available when  Valid values are: 
 | 

Stacking and Null functionality displays multiple series as a group within a stack. You can also specify how to deal with null values.

| Stacking and Null Settings | |
|---|---|
| 
 | When checked, stacks each series, one on top of another, instead of overlaying them. | 
| 
 | Available when  | 
| 
 | Determines how to display null values: Connected, Null, Null As Zero. | 

### Threshold (Advanced Setting)

In the **Advanced** configuration tab, you can set one or more thresholds, such as a line or section to a graph, to indicate whether the data crosses a limit that you specify.

| Thresholds are not available when an alert is in place on the graph. To re-enable thresholds for a chart, you must delete the alert. | 

![Threshold settings for a graph](_images/graph-advanced-threshold.png) 

| Threshold Settings | |
|---|---|
| 
 | Indicates whether the limit applies to data that is greater than ( | 
| Threshold value | A numeric value for the threshold. | 
| Threshold type | Identifier for the threshold (Custom, Critical, Warning, or OK). | 
| 
 | Adds a filler color to the graph that corresponds to the specified threshold setting. | 
| 
 | Adds a line to the graph that corresponds to the specified threshold setting. | 
| Fill Color | Similar to  | 
| Line Color | Similar to  | 

### Time Range Shift (Advanced Setting)

In the **Advanced** configuration tab, you can override any time intervals or ranges that end users select for the custom dashboard. Such selections are global and apply to all charts in the dashboard. Overrides are useful when the selection does not make sense for a particular graph.

Time ranges are calculated backwards from the present time. For example, you might set the time range so you can view the last 2 hours of data in a graph. You can also shift the time range to calculate backwards from an earlier point in time, for example, from 1 hour ago instead of from the present time.

| Time Range Shift Settings | |
|---|---|
| 
 | The amount of time to show in the x-axis of the graph (for example,  | 
| 
 | Amount of time before now (the current time) to  | 
| 
 | Checkbox for hiding the description of any Override Relative Time and Time Shift settings from the graph. |