# Configuring Tables in a Custom Dashboard | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/dashboard-custom-config-table](https://docs.mulesoft.com/monitoring/dashboard-custom-config-table)

---

![Table chart and configuration view](_images/dashboard-custom-config-table.png) 

# Configuring Tables in a Custom Dashboard

[Advanced and Titanium tiers](/monitoring/#billing)

Configure tables with Mule app and API metrics in custom dashboards.

![Table chart and configuration view](_images/dashboard-custom-config-table.png) 

| 1 | A table configured with multiple queries in advanced mode | 
| 2 | Table configuration tabs: 
 | 
| 3 | Advanced Mode: Switch for enabling[advanced](#mode_advanced)configuration modeAdvanced mode support complex configurations with up to 25 queries. | 
| 4 | Icons for moving, duplicating, and deleting queries from an advanced mode configuration | 

## Create a Table

Create a table in a custom dashboard by following the guidance in [Add Charts to a Custom Dashboard](dashboard-custom-config#charts_adding).

## Configure a Table

Configure a table in a custom dashboard.

- 
From **Custom Dashboards**, open the custom dashboard that contains your table.For guidance, see [View a Custom Dashboard](dashboard-custom-config#view).
- 
Click the table’s ![](_images/more-menu-vert-ellipsis.png) ( (**More menu**), and select**Configure**.
- 
Click the table’s **General**configuration tab.- 
Provide a title and description. 
- 
Select and configure a table mode (basic or advanced). Both modes require environment, resource (app or API), and metric settings. For more information, see [General Settings for Basic and Advanced Queries](#general).
 
- 
- 
Optionally: - 
In the table’s **Time range**
- 
In the **Options**
- 
In the **Column Styles**
 
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

## Options (Data and Pagination Settings)

In the **Options** configuration tab, you can set layout, column, and pagination options for tables in a custom dashboard.

### Data Settings (Options tab)

Provide time series data transformation, column, and paging configurations.

| Value Settings | |
|---|---|
| 
 | Creates a table with values for a given metric at a given time period. Like Time Series to Columns, the first column, Time, is for timestamps (such as  | 
| Time Series to Columns | Creates a table that shows values for a given metric at a given time period. Like Time Series to Rows, the first column, Time, is for timestamps. However, there is a column for each metric, such as  | 
| Time Series to Aggregations | Transforms time series into a table that calculates totals, averages, and so on for a given metric. The first column, Metric, is for metrics such as  Note that this example uses color-coded  | 

If you select Time Series to Aggregations, you can add pre-defined columns to the table.

| Columns for Aggregations | |
|---|---|
| 
 | Columns and their order are determined by the data query. Only available setting when Time Series to Rows, Time Series to Columns, Annotations, or Table is selected. | 
| 
 | Averages the recorded data for a given metric. | 
| 
 | Provides the lowest recorded value for a given metric. | 
| 
 | Provides the highest recorded value for a given metric. | 
| 
 | Provides the sum of all values recorded in the table. | 
| 
 | Shows the current value for a given metric. | 
| 
 | Provides the total number of data points collected on the metric. | 

### Paging (Options tab)

In the **Options** configuration tab, you can set pagination properties for tables so they don’t become too long and are more manageable.

| Paging Properties | |
|---|---|
| 
 | Number of table rows allowed per page. | 
| 
 | Checkbox for making the table scrollable. | 
| 
 | Percentage of the default font size from 80% to 250%. | 

## Column Styles (Options, Data Types, Thresholds, Links)

In the **Column Styles** configuration tab, you can create (**+Add**) and apply rules available for table columns.

To remove a rule, you need to click it, then find and click the Remove Rule button near the bottom left of the screen.

### Options (Column Styles tab)

| Options | |
|---|---|
| 
 | Identifies the column or columns to which the rule applies. Provide the name or a regular expression (regex) that matches the name of one or more columns in the table. For a regex, use this syntax:  | 
| 
 | Provides a title for the column. For example, if you add the  | 
| 
 | Treats values in the column as a link that you can configure through the  | 

### Link (Column Styles tab)

In the Column Styles configuration tab, you can configure a link from a value to a specified web page.

Link settings are available only when *Render Value As Link* is checked.

| Link | |
|---|---|
| URL | Specifies a URL that you can open when you click a value in the column. | 
| 
 | For providing a description of the link. This text appears when the end user hovers over the cell with the link. Use the same variables as for URL. | 
| Open In New Tab | Displays the web content in a new browser tab when you click on the value. | 

| Type | |
|---|---|
| 
 | Data type for values in the column. Valid values are Number, String, Date, and Hidden. | 
| 
 | Label for the unit of measure to use for the value, such as  | 
| 
 | The level of precision allowed for a decimal value, for example,  | 

### Thresholds (Column Styles tab)

In the Column Styles configuration tab, you can set thresholds for your data if Type is set to Number.

| Thresholds | |
|---|---|
| 
 | Comma-separated values, for example,  | 
| 
 | Indicates whether to apply the color code to the Value in a cell, to the Cell, to the entire Row, or whether color coding is Disabled. | 
| 
 | Color used to code values below (left-most color box), between (middle color box), and above (right-most color box) the specified threshold settings. For example, green values might represent OK, yellow a warning, and red an error. You can also invert the color coding. |