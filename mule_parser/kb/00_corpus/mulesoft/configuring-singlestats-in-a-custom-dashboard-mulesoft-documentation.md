# Configuring Singlestats in a Custom Dashboard | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/dashboard-custom-config-singlestat](https://docs.mulesoft.com/monitoring/dashboard-custom-config-singlestat)

---

![Singlestat chart and configuration view](_images/dashboard-custom-config-singlestat.png) 

# Configuring Singlestats in a Custom Dashboard

[Advanced and Titanium tiers](/monitoring/#billing)

Configure singlestat charts for Mule apps and APIs in an Anypoint Monitoring custom dashboard. A singlestat chart displays a single value, such as the value of an Inbound - Average Request Count by Endpoint metric.

![Singlestat chart and configuration view](_images/dashboard-custom-config-singlestat.png) 

| 1 | A singlestat chart example You can customize the look of singlestats. | 
| 2 | Singlestat configuration tabs: 
 | 
| 3 | Advanced Mode: Switch for enabling[advanced](#mode_advanced)configurations | 

## Create a Singlestat Chart

Create a singlestat chart in a custom dashboard by following the guidance in [Add Charts to a Custom Dashboard](dashboard-custom-config#charts_adding).

## Configure a Singlestat Chart

Configure a singlestat chart in a custom dashboard.

- 
From **Custom Dashboards**, open the custom dashboard that contains your singlestat chart.For guidance, see [View a Custom Dashboard](dashboard-custom-config#view).
- 
Click the singlestat’s ![](_images/more-menu-vert-ellipsis.png) ( (**More menu**), and select**Configure**.
- 
Click the singlestat’s **General**configuration tab.- 
Provide a title and description. 
- 
Select and configure a singlestat mode (basic or advanced). Both modes require environment, resource (app or API), and metric settings. For more information, see [General Settings for Basic and Advanced Queries](#general).
 
- 
- 
Optionally: - 
In the singlestat’s **Time range**
- 
In the **Options**
- 
In the **Value Mappings**
 
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

## Time Range (Overrides, Time Shifts, Info Display)

Time range configurations provide a way to override *relative* time ranges (such as the last 30 minutes) selected from the dashboard UI by end users.

| Time Range Settings | |
|---|---|
| 
 | The amount of time covered by the statistic, for example, the last hour ( | 
| 
 | How long ago the covered time range ended, for example,  | 
| 
 | Hides information about the override time range settings from the singlestat or table, such as  | 

## Options Tab

The **Options** tab includes settings for singlestat [values](#value_singlestat), fonts, [coloring](#color_singlestat), [spark lines](#spark_singlestat), and [gauge icon](#gauge_singlestat) settings.

### Value Settings for Singlestats

Configure values for your singlestat. Value settings include the type of value you want (such as an average), the unit of measure, and others.

![Singlestat options example](_images/singlestat-config-options.png) 

| Values | |
|---|---|
| 
 | The value displayed by the singlestat. Available Settings: 
 | 
| 
 | Prepends text to the singlestat value. | 
| 
 | Appends text to the singlestat value. | 
| 
 | Unit of measurement to display with the singlestat value (for example,  | 
| 
 | Overrides the automatic decimal precision for the legend and tooltips. | 
| 
 | Select the font size for the stat, prefix, and postfix. | 

### Coloring and Thresholds

Add color-coded thresholds to a singlestat so that you can see whether it exceeds or stays within expected limits.

| Coloring | |
|---|---|
| 
 | Adds a background color determined by the  | 
| Value | Applies a color for the current singlestat value that matches the color determined by the  | 
| 
 | Sets a threshold using a numeric range such as  | 
| 
 | Sets the colors for the values that are below, within, or above the  | 

### Spark Lines

Configure spark line settings to show a visual representation of the data.

| Spark Lines | |
|---|---|
| 
 | Checkbox to show or hide the spark line. | 
| 
 | For covering the full height of the singlestat. | 
| 
 | For selecting the color of the spark line. | 
| 
 | For selecting the color of the area below the spark line. | 

### Gauge

Display an arc-like gauge that represents the value of the singlestat.

| Gauge | |
|---|---|
| 
 | Checkbox for showing or hiding the gauge. | 
| 
 | Sets a minimum value (such as  | 
| 
 | Sets a maximum value (such as  | 
| 
 | Checkbox for showing or hiding your Threshold settings. | 

## Value Mappings

From the **Value Mappings** configuration tab, you can provide a human-readable label for a summary statistic.

![Value mapping example](_images/singlestat-config-value-mapping.png) 

| Range to Text Settings | |
|---|---|
| 
 | Maps a number to a textual description, for example:  | 
| 
 | Maps a numeric range to a textual description, for example: From  |