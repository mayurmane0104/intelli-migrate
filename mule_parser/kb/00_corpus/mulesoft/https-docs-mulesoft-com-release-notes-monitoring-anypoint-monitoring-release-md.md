# https://docs.mulesoft.com/release-notes/monitoring/anypoint-monitoring-release-notes.md

**Source:** [https://docs.mulesoft.com/release-notes/monitoring/anypoint-monitoring-release-notes.md](https://docs.mulesoft.com/release-notes/monitoring/anypoint-monitoring-release-notes.md)

---

```
# Anypoint Monitoring Release Notes
> For the full documentation index, see: https://docs.mulesoft.com/llms.txt
## June 15, 2026
Anypoint Monitoring is thrilled to introduce features on the new India Cloud instance of Anypoint
Platform and the addition of Integration Intelligence to more clouds.
### Whatâ€™s New
[India Cloud](https://in1.platform.mulesoft.com/login/) provides these Anypoint Monitoring features:
- [Anypoint Insights](../../monitoring/anypoint-insights) dashboards for monitoring performance data
  and issues across your deployed Mule apps and API implementations
- [Telemetry Exporter](../../monitoring/telemetry-exporter) for exporting telemetry data to
  third-party observability platforms like Azure Monitor, Splunk HEC, and OpenTelemetry-compliant
  tools
- [Alerts](../../monitoring/alerts-hf) for indicating whether your apps and APIs are behaving as
  expected or exceeding a defined threshold
- [Reports](../../monitoring/reports) on app requests, performance, failures, CPU usage, and memory
  use
- [Log Search](../../monitoring/logs-search-hf-india) across your deployed apps
[Integration Intelligence](../../monitoring/integration-intelligence) is now available on India,
Japan, and Canada clouds.
You can also navigate to [Functional Monitoring](../../api-functional-monitoring/) (API Functional
Monitoring) from Anypoint Monitoring on India cloud.
For more information, see [Anypoint Monitoring Overview](../../monitoring/).
## June 3, 2026
Anypoint Monitoring releases enhancements to features in US, EU, Canada, and Japan cloud instances
of Anypoint Platform.
### Whatâ€™s New
For Canada and Japan clouds, weâ€™re excited to introduce an advanced monitoring capability:
- [Reports](../../monitoring/reports): You can now review and export reports to track system metrics
  and performance over time.
For US and EU clouds, weâ€™ve updated features to optimize performance and align capabilities
globally:
- [Custom dashboard performance improvements](../../monitoring/dashboard-custom-config): Experience
  faster load times when configuring charts. To avoid lag time, a new **Refresh** feature loads long
  resource lists (such as application lists) on demand.
- [Reports](../../monitoring/reports): This update ensures complete feature and parity with Reports
  in the Canada and Japan clouds.
## May 22, 2026
From May through June 2026, Anypoint Monitoring is rolling out an enhanced Log Search experience in
US and EU instances of Anypoint Platform. This version replaces the traditional Log Search.
For more information, see
[Using Enhanced Log Search in Anypoint Monitoring (US and EU)](../../monitoring/logs-search-hf).
## March 31, 2026
### Whatâ€™s New
- Integration Intelligence now supports:
  - Logs on CloudHub deployments
  - Custom data spaces when setting up Integration Intelligence
  - Flex Gateway visualizations for dashboards
For more information, see [Integration Intelligence](../../monitoring/integration-intelligence).
## Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><p>Now, only Salesforce administrators can turn on telemetry data ingestion for Integration Intelligence.</p></td><td><p>W-21436342</p></td></tr></tbody></table>
## March 30, 2026
### Whatâ€™s New
Anypoint Insights dashboards introduce new charts and visualizations of metrics in EU, US, Japan
(JP), and Canada (CA) cloud instances of Anypoint Platform. These app and API metrics bring Anypoint
Insights dashboards into near parity with metrics displayed through the built-in dashboards in
Anypoint Monitoring.
- [New Application Metrics in Anypoint Insights](#app-visualizations)
- [New API Metrics in Anypoint Insights](#api-visualizations)
To compare built-in dashboard charts and visualizations with those now in Anypoint Insights, see
[API Chart Mapping](../../monitoring/api-dashboard#api-chart-parity) and
[App Chart Mapping](../../monitoring/app-dashboards#app-chart-parity).
For descriptions of Anypoint Insights charts and visualizations in app and API details pages, see:
- [**Application Details**](../../monitoring/anypoint-insights#entity-metrics-apps) in Anypoint
  Insights
- [**API Details**](../../monitoring/anypoint-insights#entity-metrics-apis) in Anypoint Insights
### New Application Metrics in Anypoint Insights
Anypoint Insights adds charts and visualizations of application metrics in **Application Details**
tabs:
- App **Overview** tab:
  - No new charts or visualizations in this release
- App **Request** tab:
  - **Inbound - Maximum Response Time by Endpoint**
  - **Request Volume by Protocol**
  - **Request Volume by HTTP Endpoint**
  - **Outbound Request Volume by Port**
  - **Outbound Request Volume by Remote Host**
  - **Outbound Request Latency**
  - **Outbound Request Volume by Operation**
    For more information, see
    [Request Metrics for a Mule Application](../../monitoring/anypoint-insights#entity-metrics-app-requests).
- App **Errors** tab:
  - **Inbound - Response Time by Endpoint**, **Outbound - Response Time by Endpoint**
  - **Inbound - Request Count by Endpoint**, **Outbound - Request Count by Endpoint**
  - **Failed Mule Messages**
    For more information, see
    [Error Metrics for a Mule Application](../../monitoring/anypoint-insights#entity-metrics-app-errors).
- App **Flows** tab (new in this release):
  - **Inbound - Response Time by Flow**, **Outbound - Response Time by Flow**
  - **Inbound - Requests by Flow**, **Outbound - Requests by Flow**
  - **Inbound - Response Time by Flow**, **Outbound - Response Time by Flow**
  - **Inbound - Requests by Flow**, **Outbound - Requests by Flow**
  - **Failures by Flow**
    For more information, see
    [Flow Metrics for a Mule Application](../../monitoring/anypoint-insights#entity-metrics-app-flows).
- App **Connectors** tab (new in this release):
  - **Connector Message Volume**
  - **Response Time by Connector**
  - **Salesforce Requests**, **Salesforce Response Time**, **Salesforce Failures**
  - **Database Requests**, **Database Response Time**, **Database Failures**
  - **HTTP Requests**, **HTTP Response Time**, **HTTP Failures**
  - **Web Service Requests**, **Web Service Response Time**, **Web Service Failures**
  - **FTP Requests**, **FTP Response Time**, **FTP Failures**
  - **SFTP Requests**, **SFTP Response Time**, **SFTP Failures**
  - **SMTP Requests**, **SMTP Response Time**, **SMTP Failures**
  - **Object Store Requests**, **Object Store Response Time**, **Object Store Failures**
  - **Anypoint MQ Operations - Inbound**, **Anypoint MQ Response Time - Inbound**, **Anypoint MQ
    Failures - Inbound**
  - **Anypoint MQ Operations - Outbound**, **Anypoint MQ Response Time - Outbound**, **Anypoint MQ
    Failures - Outbound**
  - **Other Connector Requests**, **Other Connector Response Time**, **Other Connector Failures**
    For more information, see
    [Connector Metrics for a Mule Application](../../monitoring/anypoint-insights#entity-metrics-app-connectors).
- App **JVM** tab:
  - **Classes Loaded**, **Classes Loaded Total**, **Classes Unloaded**
  - **JVM Uptime**
  - **Par Eden Space** , **G1 Eden Space**
  - **Par Survivor Space**, **G1 Survivor Space**
  - **Metaspace**
  - **Compressed Class Space**
  - **JVM Memory Code Cache**, **Code Cache**
  - **Tenured Gen**, **G1 Old Gen**
    For more information, see
    [JVM Metrics for a Mule Application](../../monitoring/anypoint-insights#entity-metrics-app-jvm).
- App **Custom Metrics** tab:
  Monitor apps that use your organizationâ€™s custom metrics for a Mule application. Adjust settings
  of the charts that use your custom metrics.
  The **Custom Metrics** tab for an application appears in Anypoint Insights only if your
  organization has the Anypoint Integration Advanced package or a Titanium subscription to Anypoint
  Platform and the application you selected from Anypoint Insights is running on a supported version
  of Mule.
  For more information, see
  [Custom Metrics for a Mule Application](../../monitoring/anypoint-insights#entity-metrics-app-custom-metrics).
### New API Metrics in Anypoint Insights
Anypoint Insights adds charts and visualizations of API metrics in **API Details** tabs:
- API **Overview** tab:
  - **Total 4xx Errors**
  - **Total 5xx Errors**
    For more information, see
    [Overview Metrics for an API](../../monitoring/anypoint-insights#entity-metrics-api-overview).
- API **Requests** tab:
  - No new charts or visualizations in this release
    For more information, see
    [Request Metrics for an API](../../monitoring/anypoint-insights#entity-metrics-api-requests).
- API **Errors** tab:
  - No new charts or visualizations in this release
    For more information, see
    [Error Metrics for an API](../../monitoring/anypoint-insights#entity-metrics-api-errors).
- API **Polices** tab (new in this release):
  - **Policy Violations by Path**
  - **Policy Violations by Outcome**
  - **Policy Violations by Policy**
    For more information, see
    [Policy Metrics for an API](../../monitoring/anypoint-insights#entity-metrics-api-policies).
- API **Performance** tab:
  - **Request Latency by Endpoint**
    For more information, see
    [Performance Metrics for an API](../../monitoring/anypoint-insights#entity-metrics-api-performance).
- API **Client Applications** tab:
  - **Request Volume by Location**
    For more information, see
    [Client Application Metrics for an API](../../monitoring/anypoint-insights#entity-metrics-api-client-apps).
## March 23, 2026
### Whatâ€™s New
Use Integration Intelligence to monitor, analyze, and troubleshoot your MuleSoft telemetry data
directly in the Salesforce ecosystem and unlock the analytics engine for modern integration.
Integration Intelligence, which is now generally available in the US and EU cloud regions only,
includes enhancements since the beta release in November 2025:
- Create custom dashboards in Integration Intelligence to monitor metrics for your Mule apps and
  APIs. Pinpoint inefficiencies, benchmark performance, and drive smarter optimization decisions.
- Create custom visualizations from metrics belonging to the MuleSoft semantic model.
- View app and API performance metrics in the built-in dashboards.
- Select a time range for data displayed in the built-in dashboards and logs.
- Get data from more deployment types (in addition to CloudHub 2.0 and Runtime Fabric):
  - CloudHub (dashboard metrics only)
- Set up Integration Intelligence in a _default_ data space (not a custom data space at this time).
Unsupported in this release:
- Canada and Japan cloud regions
- CloudHub deployments for logs
- Flex Gateway visualizations for dashboards
- Agentic assets (brokers, agents, and MCP servers)
- Custom data spaces when setting up Integration Intelligence
See [Integration Intelligence](../../monitoring/integration-intelligence).
## January 30, 2026
### Whatâ€™s New
In Canada Cloud and Japan Cloud instances of Anypoint Platform, Telemetry Exporter is now available
to organizations with the Advanced subscription tier. Centralize observability with Telemetry
Exporter by exporting audit log and trace data to your third-party monitoring ecosystem.
Telemetry Exporter:
[Exporting Telemetry Data to Third-Party Monitoring Systems](../../monitoring/telemetry-exporter).
For information about subscription tiers, see
[Anypoint Platform Packages and Plans](../../monitoring/#billing).
## November 24, 2025
### Whatâ€™s New
Use Integration Intelligence (Beta) to efficiently monitor, analyze, and troubleshoot your data by
bringing your MuleSoft telemetry data into the Salesforce ecosystem, unlocking the analytics engine
for modern integrations.
- Monitor metrics for your Mule apps and APIs in Integration Intelligence dashboards.
- Troubleshoot Mule apps and APIs with Integration Intelligence logs.
  This Beta release supports **WARN**, **ERROR**, and **FATAL** log levels.
- Get business insights into usage, flows, request volume, and policy violations in an Integration
  Intelligence dashboard.
This Beta release supports these deployment hosts:
- CloudHub 2.0
- Runtime Fabric
Unsupported in this release:
- CloudHub deployments
- Flex Gateway APIs
- Agentic assets (brokers, agents, and MCP servers)
See [Integration Intelligence](../../monitoring/integration-intelligence).
## October 3, 2025
### Whatâ€™s New
As part of the Agent Fabric initiative on US and EU Clouds, Anypoint Monitoring now supports data
from agentic assets (agent, broker, and MCP server instances) in these features:
- Log Search adds support for logs from agentic assets.
  For more information, see
  [Get Agent, Broker, and MCP Server Logs](../../monitoring/logs-us-eu#search-agentic).
- Traces (Beta) now includes traces with spans for agentic assets.
  For more information, see [Examining Traces](../../monitoring/traces).
- Metrics on agentic assets accessible from Agent Visualizer nodes are available in Anypoint
  Monitoring.
  For more information, see [Monitoring Agentic Assets](../../monitoring/anypoint-insights-agentic).
See [Agent Fabric](../../general/learning-map-agent-fabric).
## October 1, 2025
### Whatâ€™s New
In Canada Cloud and Japan Cloud instances of Anypoint Platform, Logs and Alerts are now available as
an open beta release in the Advanced subscription tier. Any use of Anypoint Monitoring features in
the beta state is subject to the applicable beta services terms and conditions.
- Logs: [Using Logs in Anypoint Monitoring (Canada and Japan)](../../monitoring/logs-jp-ca)
- Alerts: [Getting Alerts (Canada and Japan)](../../monitoring/alerts-jp-ca)
  Alerts configurations support Mule application and API metrics.
For information about subscription tiers, see
[Anypoint Platform Packages and Plans](../../monitoring/#billing).
## April 30, 2025
### Whatâ€™s New
Anypoint Insights is now generally available (GA) in the US Cloud and EU Cloud instances of Anypoint
Platform.
Support for Anypoint Insights is available at these subscription tiers:
- All subscription tiers in the US Cloud and EU Cloud instances of Anypoint Platform
- Starter tier in the Canada Cloud and Japan Cloud (Hyperforce) instances
For information about subscription tiers, see
[Anypoint Platform Packages and Plans](../../monitoring/#billing).
## March 18, 2025
### Whatâ€™s New
The Beta version of Anypoint Insights is now available to all subscription tiers in the US Cloud and
EU Cloud instances of Anypoint Platform. From the list of entities in Anypoint Insights, you can
open detailed metrics on specific deployments in Anypoint Insights dashboards instead of **Built-in
dashboards**.
Tiers that now include Anypoint Insights:
- Starter usage-based tier
- Gold and Platinum core-based tiers
Support for Anypoint Insights continues at these tiers:
- Advanced and Titanium tiers in the US Cloud and EU Cloud instances of Anypoint Platform
- Starter tier in the Canada Cloud and Japan Cloud (Hyperforce) instances
For information about subscription tiers, see
[Anypoint Platform Packages and Plans](../../monitoring/#billing).
## March 7, 2025
### Whatâ€™s New
The [Metrics API](../../monitoring/anypoint-insights#metrics-api) is available in this release. This
API supports access to metrics displayed in Anypoint Insights charts.
## December 9, 2024
### Whatâ€™s New
- This product is now available on Hyperforce.
  Anypoint Platform instances on the Hyperforce infrastructure are:
  - [Canada Cloud](https://ca1.platform.mulesoft.com)
  - [Japan Cloud](https://jp1.platform.mulesoft.com)
- [Anypoint Insights](../../monitoring/anypoint-insights) is available for monitoring high-level
  performance metrics across your deployed Mule app and API implementations (_entities_) and for
  getting detailed metrics on specific entities.
  This feature is available in the Starter package tier on Canada Cloud and Japan Cloud. For US and
  EU clouds, this feature remains a Beta release available in the Advanced and Titanium tiers at
  this time. See [Anypoint Monitoring Packages and Plans](../../monitoring/#billing).
- API Functional Monitoring is available from Anypoint Monitoring on Canada Cloud and Japan Cloud.
For more information, see [Monitoring Features by Control Plane](../../monitoring/#features).
## August 21, 2024
### Whatâ€™s New
- The basic view in the API analytics dashboard is deprecated. Use the default (enhanced) view to
  see detailed information about your APIs.
- The **Inbound - Total Slow Requests by Endpoint** chart in built-in dashboards is deprecated.
## May 30, 2024
## Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue Resolution</th><th>ID</th></tr></thead><tbody><tr><td><p>The data for the table that renders Average, Min, and Max Response Times by HTTP Endpoint (Inbound and Outbound) is now properly computed.</p></td><td><p>R-1160926</p></td></tr><tr><td><p>The data for Inbound and Outbound Average Response Time chart is now properly computed.</p></td><td><p>R-1160926</p></td></tr></tbody></table>
## May 22, 2024
### Whatâ€™s New
- The Telemetry Exporter feature now supports
  [exporting traces](../../monitoring/telemetry-exporter) from Runtime Fabric apps to third-party
  observability and analytics apps.
## March 6, 2024
### Whatâ€™s New
- The Telemetry Exporter feature now supports
  [exporting traces](../../monitoring/telemetry-exporter) from CloudHub 2.0 apps to third-party
  observability and analytics apps.
## February 29, 2024
### Whatâ€™s New
- The [Telemetry Exporter](../../monitoring/telemetry-exporter) for
  [audit logs](../../access-management/audit-logging) enables you to export audit log data to
  third-party analytics and observability apps, such as Splunk HEC or Azure Monitor.  
  The Telemetry Exporter is available only for organizations that have the Anypoint Integration
  Advanced package or a Titanium subscription to Anypoint Platform.
- To enable Telemetry Exporter, two new
  [permissions](../../access-management/permissions-by-product#monitoring) are available:
  - Telemetry Exporter Administrator
  - Telemetry Exporter Configurations Manager
## February 6, 2024
### Whatâ€™s New
- When you monitor a
  [connector that is compatible with Java 17](https://help.salesforce.com/s/articleView?language=en_US&id=000782248&type=1),
  you must specify the Java version.
- Mule runtime engine 4.6.0 is now available.
  For information about the release notes, see
  [Mule Runtime Engine 4.6.0 Release Notes](../mule-runtime/mule-4.6.0-release-notes). For
  information about the new release cadence, see
  [Edge and LTS Releases for Mule](../mule-runtime/lts-edge-release-cadence).
### Known Issues
- The following charts in **Built-in Dashboards** for apps are currently unavailable for apps using
  Java 17:
  - Garbage Collection Count (CloudHub deployments only)
  - Garbage Collection Time (CloudHub deployments only)
  - ParNew Collection Count
  - ParNew Collection Time
  - Par Eden Space (Used, Maxed, Init, Committed)
  - Par Survivor Space (Used, Maxed, Init, Committed)
  - Code Cache (Used, Maxed, Init, Committed)
## October 31, 2022
- The Log Points and Reports features in Anypoint Monitoring are now supported for CloudHub 2.0.
## July 28, 2022
### Whatâ€™s New
- Basic alerts for APIs are now available in MuleSoft Government Cloud.
## April 28, 2022
### Whatâ€™s New
- Anypoint Monitoring supports built-in dashboards and alerting for APIs deployed through Flex
  Gateway.
- Organizations with a Titanium subscription can use log management in Anypoint Monitoring for APIs
  deployed through Flex Gateway.
- You can create basic alerts for APIs. Organizations that have a Gold or Platinum subscription can
  have up to six active API alerts per API instance. Organizations with a Titanium subscription can
  have up to ten active API alerts per API instance.
## April 5, 2022
### Whatâ€™s New
- A Platinum subscription to Anypoint Monitoring is available in Mulesoft Government Cloud. For a
  complete list of supported Anypoint Monitoring features, see the **Platinum Subscription for
  Mulesoft Government Cloud Features** column in the
  [**Anypoint Monitoring Features** table](../../monitoring/#anypoint-monitoring-features).
## December 7, 2021
## Whatâ€™s New
- In **Custom Dashboards**, advanced mode has two new metrics:
  - `disk_stats`
  - `operatingsystem`
## November 9, 2021
## Whatâ€™s New
- The world map chart is now available for built-in dashboards with enhanced API metrics.  
  In the **Client Application** section, the **Requests by Location** chart displays a world map
  that shows the number of requests per geographic location.
## September 13, 2021
## Whatâ€™s New
- Anypoint Monitoring now has two product-specific permissions: Anypoint Monitoring Viewer and
  Anypoint Monitoring Administrator.
  - The Anypoint Monitoring Viewer permission enables a user only to view assets in Anypoint
    Monitoring.
  - The Anypoint Monitoring Administrator permission enables a user to view, create, modify, and
    delete assets in Anypoint Monitoring.
- The **Overview** section of built-in API dashboards for enhanced metrics has two new charts. The
  **Total 4xx Errors** and **Total 5xx Errors** charts show the sum of all 400- and 500-errors
  respectively.
## Fixed Issues
<table><colgroup><col> <col></colgroup><thead><tr><th>Issue</th><th>ID</th></tr></thead><tbody><tr><td><p>In built-in dashboards, URLs previously contained an extra <code>https</code>.</p></td><td><p>MONITORING-4881</p></td></tr><tr><td><p>When creating alerts, servers had metrics but deployed apps did not appear in the list of servers, so you could not create alerts on these servers.</p></td><td><p>MONITORING-4839</p></td></tr><tr><td><p>Sorting alerts using the <strong>Name</strong> column was not working properly.</p></td><td><p>MONITORING-4850</p></td></tr><tr><td><p>Users could previously intercept an alert, modify the alert ID, and send it to other users.</p></td><td><p>MONITORING-4756, INFOSEC-17438</p></td></tr><tr><td><p>When you used an email link from a basic alert to access a dashboard or alert from an organization that was different than the organization you were logged in to, you were redirected to your own organizationâ€™s alert page. You are now prompted to log in to an account that is associated with the organization that sent the alert.</p></td><td><p>MONITORING-4662</p></td></tr><tr><td><p>When creating alerts, you could circumvent validation in the <strong>Recipient</strong> field and paste invalid emails.</p></td><td><p>MONITORING-4614</p></td></tr><tr><td><p>When you configured a custom dashboard and tried to select an API instance, a 408 error occurred.</p></td><td><p>SE-21708</p></td></tr><tr><td><p>When you configured a custom dashboard while using an on-premises deployment, available servers and applications did not load.</p></td><td><p>SE-22074</p></td></tr></tbody></table>
## June 16, 2021
### Enhancements
- Reports have a new column that specifies the `target name`, or location where the target is
  deployed, of the resource for which you are viewing a report.
- The following charts were renamed:
  - **Inbound - Total Requests by Endpoint** is now **Inbound - Total Requests by HTTP Endpoint**.
  - **Outbound - Total Requests by Endpoint** is now **Outbound - Total Requests by HTTP Endpoint**.
- Previously, in the **Custom Dashboards** API panel, APIs that did not support enhanced metrics did
  not appear. For enhanced usability, these APIs now appear in the API panel but are disabled.
- The `${timestamp}` variable is now available in alert email templates.
### Fixed Issues
- If you had previously chosen an environment when you accessed the **Reports** page, an error
  occurred when you tried to click **View**.
- When you accessed the **Custom Dashboards** page and clicked **Configure**, the **Save** button
  appeared before you made any changes.
- In **Custom Dashboards**, when you selected everything for an API Panel and changed to API
  Analytics Panel (deprecated), an error occured and your selections remained in each field. Because
  the metrics between API panels are different, your selections are now reset when you switch
  between API panel types.
- Fixed an issue related to the `group by` for the **Inbound - HTTP Endpoints** chart.
- Fixed an issue in which the **Inbound - Total Requests by HTTP Endpoint** and **Outbound - Total
  Requests by HTTP Endpoint** charts had empty cells. (SE-20663)
- In the **Built-in Dashboards** page, when you viewed an API that supported both basic and enhanced
  metrics and then clicked the **Switch to basic metrics** link, the **Switch to basic metrics**
  link did not work. (SE-19796)
- When you created a server alert, servers did not load automatically.
- When you created an API panel in **Custom Dashboards**, if you selected everything, changed to
  advanced mode, and then switched back to simple mode, API selector tried to load indefinitely.
- In **Custom Dashboards**, if you had two Runtime Fabric apps available that had the same name,
  there was an issue selecting the second one. (SE-20637)
- When you used Safari to access built-in dashboards, the date picker did not work properly.
  (SE-20203)
- When you used a link to **Log Search** that was shared by another user in the same organization,
  an error occurred if the query parameter in the URL was encoded:
  `The sharer organization is not the same as the active one.` You can now access log search after
  encoding query parameters in URLs. (SE-20282)
- When you had multiple hybrid apps deployed to the same server, created a custom dashboard, and
  then selected the second app out of the hybrid apps deployed to that server as the **Resource**,
  your selection changed to the first app deployed to that server whenever you tried to reconfigure
  the panel. (SE-20453)
## March 16, 2021
### Enhancements
- Basic alerts now support email templates. You can populate the subject and message body of basic
  alert emails to include variables for the alert metric, condition, severity, and more. For a
  complete list of available variables, refer to the
  [basic alerts documentation](#monitoring::basic-alerts.adoc#alert-variables).
- The **Alerts** page now sorts alerts by the most recently updated.
- When you use the Log Search feature, the logs that appear alongside the target log entry now load
  more quickly. SE-17024
- The **Connector Message Volume** chart tooltip has been enhanced to read **Number of outbound
  requests, grouped by connector type**.
- The following charts have been renamed:
  - **Inbound - Response Time by Endpoint** is now **Inbound - Response Time by HTTP Endpoint**.
  - **Inbound - Endpoints** is now **Inbound - HTTP Endpoints**.
  - **Outbound - Ports** is now **Outbound - HTTP Ports**.
  - **Outbound - Protocols** is now **Outbound - HTTP Protocols**.  
    SE-18756, SE-18909
- The following charts include enhanced queries for more accurate metrics reporting:
  - Inbound - Response Time by HTTP Endpoint
  - Inbound - HTTP Endpoints
  - Outbound - HTTP Ports
  - Outbound - HTTP Protocols
  - Outbound - Operations  
    SE-18756, SE-18909
### Fixed Issues
- Fixed an issue related to timeouts while searching for surrounding logs. SE-17024
- Fixed an issue in which multiline logs in log searches resulted in multiple events. SE-18091
- In basic mode of custom dashboards for hybrid apps, you could not select applications other than
  the first application that appeared when you accessed the resource selector. SE-19604
- Fixed an issue related to ordering applications by name when you clicked the **Application Name**
  column in reports.
- Fixed an issue related to deleting alerts while filters were enabled.
## January 27, 2021
### Enhancements
- Basic and advanced alerts now include a selection for user-defined severity. Note that when you
  modify existing alerts, you must assign a severity to that alert before you can save changes.
- You can now sort and filter alerts by severity in the **Alerts** page.
- When you create an alert and begin entering a value in the **Recipients** field, user emails
  associated with your organization that match the value you entered appear.
### Fixed Issues
- When you had apps with the same name deployed to multiple Anypoint Runtime Fabric clusters:
  - Regardless of which instance of the app you selected, the same one always appeared.
  - The metrics associated with that app were combined.
  To accommodate this fix, built-in dashboard URLs have been enhanced to use the appâ€™s ID to
  differentiate between instances of deployed apps. If you reload the page using the previous URL,
  the page will not load. (SE-19017)
- The Inbound - Response Time by Flow chart erroneously displayed the same value for average,
  minimum, and maximum columns. (SE-19048)
- The **Raw Data** page did not load for some Runtime Fabric users. (SE-18626, SE-19093)
- The data for Inbound - Requests by Flow and Inbound - Response Time by Flow charts were swapped.
  (SE-18786, SE-19048)
- In built-in API analytics charts, the following charts erroneously showed sums, instead of
  averages:
  - Average Response Time
  - Requests by Performance
  - Slow Requests  
    (SE-17969)
- General bug fixes and security enhancements.
## December 14, 2020
### Fixed Issues
Your environment now loads correctly during custom dashboard creation.
## November 12, 2020
### Fixed Issues
- If you had the same API deployed in two or more environments, the corresponding API widget label
  continued to show the first environment the API instance was deployed to, even after saving and
  reconfiguring the graph.
- Infinite scrolling did not work in the list of alerts.
- When using Anypoint Monitoring, the **Sign Out** button did not log you out of Anypoint Platform.
- When you clicked a link in an alert email, some redirects did not work as expected. The link in
  the alert email now directs you to an error page if that link goes to:
  - A deleted dashboard
  - A dashboard that cannot be found
  - A dashboard that is in a different organization than the current active organization.
## October 26, 2020
### Enhancement
The resource and version selectors in the **Built-in Dashboards**, **Custom Dashboards**,
**Alerts**, and **Log Points** pages contain information about the target and deployment type, if
available.
### Fixed Issues
- If you had two APIs with the same name but different targets, you could not differentiate which
  API was related to which cluster. The API names appeared without additional information. SE-15782.
- When you searched for an API instance or version, the search feature did not suggest results based
  on the version.
- When selecting assets to view in built-in dashboards, the supported runtime versions tooltip
  erroneously stated `Version 3.8.7-AM is supported for log search only`. All -AM runtime versions
  are deprecated.
- In **Built-in Dashboards**, the **Inbound - Maximum Response Time** chart used the wrong query to
  populate the chart.
## September 17, 2020
### Fixed Issues
- Because of time zone conflicts, the selected date sometimes did not match the dates in the charts.
- When you reconfigured a graph in custom dashboards, some of the application panel metrics changed
  to the first metric in the **Metrics** list.
- You could not edit some basic alerts.
## September 3, 2020
### Enhancements
- You can now enable Anypoint Monitoring automatically for new applications that you deploy to
  CloudHub. This feature is enabled automatically for Titanium users.
## July 30, 2020
### Enhancements
- Anypoint Monitoring now supports Mule runtime versions 3.8.7 and newer. SE-16739
### Fixed Issues
- Searches for alerts by name were case-sensitive.
- In the Custom Dashboards page, the tooltips for histogram charts did not display totals. SE-15270
- Email addresses were formatted incorrectly for alerts that had multiple email recipients.
## July 7, 2020
### Fixed Issues
- In custom dashboards, metrics changed when you edited content in the **General** tab.
- In custom dashboards, adding widgets to a new chart cleared existing charts.
- In built-in dashboards, the **JVM - Memory Utilization** chart is now named **JVM - Heap Total
  Memory**.
- In built-in dashboards, the **Application Process CPU Load** chart is now named **System CPU %
  Utilization**.
- In built-in dashboards, the **Application Process CPU Minutes** chart is now named **JVM CPU
  Time**.
## June 29, 2020
### New Feature
> [!NOTE] This feature is currently available only for certain customers.
You can now quickly and seamlessly create basic alerts for app and server metrics.
Basic alerts are available for the following metrics for servers or Mule apps:
- For on-premises servers and CloudHub apps:
  - CPU utilization
  - Memory utilization
  - Thread count
- For on-premises, Runtime Fabric, and CloudHub apps:
  - Message count
  - Message error count
  - Message response time
## May 20, 2020
### New Feature
You can now access the Anypoint Visualizer Troubleshooting visualization for an app in the
**Application Network** section of the **Built-In Dashboards** page in Anypoint Monitoring. The
**Application Network** section enables you to view direct callers and callees for a single app for
the most recent seven days.
## May 4, 2020
### Enhancements
A new version of the Anypoint Monitoring Archive API is available. The Anypoint Monitoring Archive
API allows you to retrieve API metrics that Anypoint Monitoring stores. You can
[download this API](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/anypoint-monitoring-archive-api/)
using Anypoint Exchange. This API is available only for users who have a Titanium subscription.
## April 15, 2020
> [!NOTE] IE 11 is not supported in Anypoint Monitoring.
### Enhancements
- In the **Log Search** feature, you can now view how to correctly format a date with clickable
  examples.
- The **Information** section of the built-in dashboards pages has word wrapping and hover text.
- When you share a log by copying the URL, a message appears instead of a countdown.
- Improved performance when switching between built-in dashboards, applications, or APIs.
### Fixed Issues
- The **CPU Utilization** and **Memory Utilization** tabs of the Reports feature no longer include
  Cloudhub or hybrid deployments.
- You could not add pre-Crowd APIs to built-in dashboards.
- The **Requests by HTTP Policy Violation** chart did not display a name or ID.
## March 26, 2020
### Enhancements
- The **Log Search** page now has a refresh button.
- New API metrics are provided:
  The **Built-in dashboards** page for APIs now has multiple tabs to show more information and
  enhance the root cause analysis for APIs. The new tabs include: **Overview**, **Requests**,
  **Failures**, **Performance**, and **Clients**. The user can switch between enhanced and basic
  metrics.
### Fixed Issues
- A legend for built-in API dashboards was incorrect.
## February 18, 2020
### Enhancements
- For smoother navigation, the tabs on the **Built-in Dashboards** page appear in the same order
  whether the window is collapsed or expanded.
- The built-in dashboard chart called **Total Requests by Type** is now **Total Requests by Response
  Type**.
### Fixed Issues
- Using the Export CSV feature for a chart resulted in CSVs containing fractional values, which
  caused incorrect sums of metrics. SE-14652
- Using the `is between` and `is not between` operations with a timestamp filter did not work.
- In advanced mode for custom dashboards, the API ID and API version ID were repeated.
- If you clicked a URL in an email report from API Functional Monitoring to view the result of a
  test and you were not logged in to Anypoint Platform, the URL would open the login page. After you
  logged in, Anypoint Platform did not redirect you to the page you tried to access.
- The notification switcher broke full-page scrolling.
- The built-in dashboards refresh rate allowed you to refresh in increments smaller than one minute.
- There was an invalid API instance value in the log-points selector.
- The following API charts did not show correct data:
  - Requests (Avg)
  - Average Size of Requests
  - Average Size of Responses
- When a query had one tag, aliases did not work correctly.
## February 6, 2020
### New Features
The Log Points feature for apps, which requires a Titanium subscription, enables you to generate
logs for apps and connectors without having to write code or redeploy the app.
### Enhancements
To enhance readability, when you use the **View Surrounding Logs** feature in a log search, only
five logs appear before and after the log you selected.
### Fixed Issues
- When you used the same instance label on two or more APIs in different environments, the
  **api-version-id** list did not clarify which API resided in which environment. Now, the
  **api-version-id** list also shows the environment name. SE-14062
- The list of APIs in advanced mode on the **Custom Dashboards** page did not include all the
  available APIs. This issue has been resolved. SE-12532
## January 23, 2020
### Enhancements
- When you search for logs, the **Quick Filter** section has an option called **See More** that
  further filters your search results.
- If you are using an -AM runtime, the built-in dashboards page displays a deprecation notice.
### Fixed Issues
- You could not delete saved searches in Log search. SE-13734
- When a long API instance name appeared on built-in dashboards, it exceeded the length of the
  selector and prevented you from clicking the underlying **View** button.
- The organization name was missing in alert notification emails.
- In the **Custom Dashboards** page, it was not possible to move charts using the mouse.
- A typo was corrected on the **Log Points** page.
- In the **Custom Dashboards** page, deleting a chart left an empty state image.
- In the **Advanced Mode** section of the **Custom Dashboards** page, there is now a label
  indicating that it is not possible to add alerts in advanced mode charts.
- Although users who do not have a paid subscription cannot export charts as CSVs, an **Export CSV**
  button appeared in chart options.
- Nongraph charts in advanced mode showed a label stating that alerts were not supported.
## December 7, 2019
### Enhancements
To enhance usability, the following built-in dashboards have renamed charts:
- Overview
- Inbound
- Outbound
- Performance
- Failures
### Fixed Issues
- API built-in dashboards showed "No data points" despite API Manager showing incoming requests.
  SE-13181
- In the **Custom Dashboards** page, the **Advanced query options** menu did not populate with a
  complete list of APIs. SE-12532
- When you tried to view a log, an error would sometimes appear. SE-13931
- When you added a link with the `absolute` type to a custom dashboard, the link did not open.
- When you added a link in a new or existing custom dashboard, the link redirected back to the
  dashboard until you refreshed the page.
- When you tried to navigate from the **Reports** page to a hybrid app, the link for the hybrid app
  did not resolve.
- In the **Built-In Dashboards** page, links on some charts did not resolve.
## October 7, 2019
This release contains the following new features for users who have a Titanium subscription:
- The **Flows** built-in dashboard tab shows detailed information about each flow in a Mule
  application.
- The **Connectors** built-in dashboard tab shows summary usage and performance information across
  all connector types.
- The **Inbound** and **Outbound** built-in dashboard tabs contain new charts.
This release also contains the following enhancements:
- The Alert Email template includes additional contextual information.
- The `Share` command in log search has been enhanced. This feature requires a Titanium
  subscription.
- Log-point configuration feedback is improved.
## June 18, 2019
This release contains the following enhancement:
The retention period for Anypoint Monitoring API analytics increased to 90 days for Gold and
Platinum subscriptions.
## June 12, 2019
Anypoint Monitoring support for Mule 3.9.x-AM and Mule 4.x-AM is being deprecated.
Update your applications to run on Mule versions 3.9.x and 4.x for better functionality and improved
performance, and to receive the latest patch updates as soon as they are available.
If you currently have Anypoint Monitoring enabled for applications running Mule 3.9.x-AM or 4.x-AM,
monitoring continues to work, but you will not receive important patch updates.
For information about setting the runtime version for your Mule app and enabling monitoring, see
[Configure and Enable Anypoint Monitoring for Mule Apps](../../monitoring/configure-monitoring-cloudhub).
## May 4, 2019
This release contains the following new features and enhancements:
- Support for hybrid and CloudHub apps running on Mule 4.2.0
- A **Custom Metrics** page from which you can easily access the
  [custom metrics connectors](../../monitoring/anypoint-custom-metrics-connector) for Mule 3 and 4
- Support for these [connector metrics](../../monitoring/monitor-connectors):
  - FTP
  - SFTP
  - SMTP
  - Object Store
  - Anypoint MQ
- Metrics for inbound Mule messages on the **Overview** and **Performance** tabs
## April 30, 2019
Anypoint Monitoring for applications deployed to Runtime Fabric is now supported. Monitoring is
enabled by default, so you donâ€™t need to set anything up in Anypoint Monitoring. For more
information, see
[Monitoring Applications Deployed to Runtime Fabric](../../runtime-fabric/latest/manage-monitor-applications).
## April 6, 2019
An enhanced Monitoring agent is now included in CloudHub runtime versions 3.9.0, 3.9.1, and 3.9.2.
## March 27, 2019
The following features now support CloudHub apps running on Mule 4.1.x:
- Custom Metrics
- Connector monitoring
## March 23, 2019
### New Features
This release contains the following new features:
1.  You can save built-in dashboards as custom dashboards, which simplifies the process of building
    custom dashboards and allows you to leverage the features and flexibility available in custom
    dashboards. For more information, see
    [Save a Built-in Dashboard as a Custom Dashboard](../../monitoring/save-builtin-dashboard-as-custom).
2.  In built-in and custom dashboards, you can export data for an app into a CSV file. For more
    information, see [Export App Data to a CSV File](../../monitoring/export-app-data-to-csv).
### Enhancements
This release contains the following enhancements:
- In addition to enabling monitoring for apps deployed to CloudHub and running on Mule 3.9.2, you
  can enable monitoring for apps running on the following Mule versions:
  - 4.1.5
  - 4.1.4
  - 4.1.3
  - 4.1.2
  - 4.1.1
  - 3.9.1
  - 3.9.0  
    For more information, see
    [Enable Monitoring for Mule Apps Deployed to CloudHub](../../monitoring/configure-monitoring-cloudhub)
- The sidebar menu in Anypoint Monitoring is restyled to make navigation more intuitive.
### Fixed Issues
- General bug fixes.
## February 22, 2019
The following new charts are available in the built-in dashboards:
- Inbound
  - Maximum Response Time
- Infrastructure
  - System Memory
  - Application Process CPU Load
  - Application Process CPU Minutes
  - Operating System Swap Space
- JVM
  - Committed Virtual Memory
For more information about built-in dashboards, see
[Built-in Application Dashboards](../../monitoring/app-dashboards).
## February 16, 2019
- You can now monitor Web Services connectors in the **Connectors** tab. For more information about
  monitoring connectors, see [Monitor Connectors](../../monitoring/monitor-connectors).
- You can now visualize custom metrics in real time using the built-in **Custom metrics** dashboard.
  For more information, see
  [Anypoint Custom Metrics Connector](../../monitoring/anypoint-custom-metrics-connector).
## February 7, 2019
The Anypoint Monitoring log points feature now supports the following API types and versions:
- Basic endpoint APIs (CloudHub and hybrid)
  - CloudHub
  - Hybrid
- Endpoint with Proxy APIs
  - CloudHub proxy
  - Hybrid proxy
- Mule 3 versions 3.8.5 and later
- Mule 4 versions 4.1.1 and later
See [Log Points](../../monitoring/log-points)
## January 12, 2019
This release contains the following new features:
- **Custom Dashboard API Support**
  - When you configure a custom dashboard and then work in Basic Mode, you can choose between an
    Application Panel and an API Panel to create dashboards to visualize API metrics.
  - In Advanced Mode you can add queries based on API metrics.
## December 15, 2018
This release contains the following new features:
- **API Analytics** - API Analytics is now available in Anypoint Monitoring. See
  [Builtin API Analytics Dashboard](../../monitoring/api-dashboard).
- **Anypoint Custom Metrics Connector** - (Requires a Titanium subscription) The Anypoint Custom
  Metrics connector enables sending metric values with dimensions to Anypoint Monitoring, where they
  can be visualized in real time using Custom Dashboards. See
  [Custom Metrics Connector](../../custom-metrics-connector/latest/).
## December 8, 2018
This release contains the following new features:
- **Log Points** - (Requires Titanium subscription) You can generate logs for a running API without
  writing any code or redeploying your application. You can select specific parameters within the
  API for which to generate logs, for example, the request header `host` parameter. For more
  information about log points, see [Anypoint Monitoring Log Points](../../monitoring/log-points)
- **Connector-level Flow Analysis** - (Requires Titanium subscription) You can now monitor the
  performance for connectors. For more information about monitoring connectors, see
  [Monitor Connectors](../../monitoring/monitor-connectors)
### Known Issues
The Anypoint Monitoring log points feature is only supported on Mule runtime engine version 3.8.5-AM
or later. For APIs not running on Mule runtime engine 3.8.5-AM or later, the log points feature does
not appear for the API.
Because you canâ€™t select the runtime version when you deploy an API from API Manager, you must
navigate to Runtime Manager, select the runtime version (3.8.5-AM or later), then redeploy the API.
> [!NOTE] Mule runtime engine versions appended with `-AM` are listed in Runtime Manager, in the
> **Runtime Version** menu under **Show old patch releases**.
### Fixed Issues
- General bug fixes.
## Version 1.05
### New Features and Enhancements
- Environment-wide reporting on application performance, including requests, failures, CPU and
  memory utilization. (Requires a Titanium subscription)
- Performance Improvements
  - All static resources are stored on a content delivery network (CDN).
  - Resources are prefetched on page load.
  - Changes to built-in dashboards load more quickly.
  - Extended connection pools life before timeout.
- Improvements to Deployment and Management:
  - New capabilities to associate an Organization with an environment so that you can build proofs
    of concept (POCs) without relying on engineering work.
  - Provisioning Configuration Management: Allows for changes to the data sources without requiring
    a new deployment. Versioning to allow controlled roll out.
  - Log Orchestration Service updates periodically from the Provisioning System: allows the creation
    of an Organization log index without requiring a deployment.
  - Admin console now exposes data from Provisioning: it allows easier visualization and editing of
    the environment properties.
- Minor user experience (UX) improvements.
- Log search share URL.
### Fixed Issues
- General bug fixes.
```