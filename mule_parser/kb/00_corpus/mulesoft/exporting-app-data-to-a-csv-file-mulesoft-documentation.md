# Exporting App Data to a CSV File | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/export-app-data-to-csv](https://docs.mulesoft.com/monitoring/export-app-data-to-csv)

---

# Exporting App Data to a CSV File

In built-in and custom dashboards, you can export chart data to a CSV file. If you apply a filter to a dashboard, the exported data includes only the data included in the filter you set, such as a time-range filter.

- 
Log in to Anypoint Platform with a user account that has [permission to access Anypoint Monitoring content](am-permissions).
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
In the sidebar, click **Built-in dashboards**or**Custom dashboards**.
- 
Select the application for which to download the data. 
- 
Specify the time range for the data to download. 
- 
In the chart that contains the data to download, click the ![](_images/more-menu-vert-ellipsis.png) ( (**More menu**), and select**Export CSV**.
- 
In the **Export CSV**dialog, specify the way to format the data.- 
In **Mode**, select the format for the data:- 
**Series as rows**formats the data in rows in the CSV file.
- 
**Series as columns**formats the data as columns in the CSV file.
 
- 
- 
In **Date Time Format**, enter the values to specify the date format, for example:`YYYY-MM-DDTHH:mm:ssZ`
- 
Determine whether to use **Excel CSV dialect**(enabled by default).
 
- 
- 
Click **Export**.