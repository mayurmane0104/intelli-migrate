# Anypoint Monitoring Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring](https://docs.mulesoft.com/monitoring)

---

# Anypoint Monitoring Overview

Understanding the state of your infrastructure and systems is important for ensuring the reliability and stability of your services. As part of Anypoint Platform, Anypoint Monitoring provides visibility into integrations across your app network. The monitoring tools provide feedback from Mule flows and components in your app network.

Operations and development teams use the monitoring tools to diagnose issues and prescribe solutions to behavior that negatively impacts digital performance. The monitoring tools are designed to reduce the time to identify and resolve these issues through aggregated metrics, data visualization tools, alerts for issues, and a log aggregation system. Specifically, Anypoint Monitoring provides ways to:

- 
Aggregate and map metrics across dependent systems in real-time. 
- 
Configure dashboards and alerts to reduce the mean time to identification of issues (MTTI). 
- 
Store and search log data at scale. 

## Monitoring Features by Control Plane

Anypoint Monitoring feature availability depends on the control plane for your Anypoint Platform instance and your [Anypoint Platform package or plan](#billing).
Data isn’t shared across the separate instances of Anypoint Platform.

| Anypoint Monitoring Feature | [US](https://anypoint.mulesoft.com/monitoring),[EU](https://eu1.anypoint.mulesoft.com/monitoring)Clouds | [Canada](https://ca1.platform.mulesoft.com/monitoring),[Japan](https://jp1.platform.mulesoft.com/monitoring)Clouds | [India](https://in1.platform.mulesoft.com/login/)Cloud | 
|---|---|---|---|
| Yes | Yes | Yes | |
| Yes | Yes | Yes | |
| Yes | No | No | |
| Yes | No | No | |
| Yes | No | No | |
| Yes | Yes | Yes | |
| Yes | Yes | Yes | |
| 
 | Yes | No | No | 
| Yes | Yes | Yes | |
| Yes | Yes | Yes | |
| Yes | No | No | 

For more information about MuleSoft Government Cloud and Anypoint Platform Private Cloud Edition (Anypoint Platform PCE), see [Control Plane Hosting Options](../hosting-home/#control-plane-hosting-options).

### Anypoint Insights

Monitor performance data and issues across your deployed Mule apps and APIs (*entities*), and get detailed insights on specific deployments.

### Log Management

Manage logs and log data for your deployments with these logging features:

Support for logging features can vary by Anypoint Platform cloud. For details, see [Monitoring Features by Control Plane](#features).

#### Log Searches

| 
 | 

Search for and review logs from across your deployed applications.

| Log search limited to individual apps is available to all subscription tiers in Runtime Manager for apps deployed to CloudHub and CloudHub 2.0. You can navigate to Runtime Manager, open the app, and then click  The log aggregator system holds raw operational data and records events that occur in the operating system or Mule app. Log aggregation compiles, organizes, and indexes log files to facilitate management, searching, and analysis. Aggregated logs complement the monitoring system by helping you identify causes of operational issues and investigate failures. For more logging options, see  | 

#### Log Points

| 
 | 

In the US and EU Clouds, generate logs for Mule apps and APIs in real-time and without writing code.

#### Raw Data Downloads

| 
 | 

Download warehoused (archived) log data for a Mule app, for example, to help investigate security, compliance, or other issues that logs can reveal.

### Tools for Monitoring Integrations

| 
 | 

Use connectors that help deliver Anypoint Monitoring notifications to external systems, including custom metrics connectors.

### API Functional Monitoring

Monitor APIs and endpoints at scheduled intervals. Receive reports about whether tests pass or fail, and view statistics about API and endpoint performance.

## Data Storage and Retention

Data storage and retention limits are determined by your pricing plan. If your organization has the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform, this feature provides a higher resource allocation.

- 
For the Anypoint Integration Starter package or the Gold and Platinum subscriptions: - 
Stores metric data in the same region as your control plane 
 
- 
- 
For the Anypoint Integration Advanced package or Titanium subscription: - 
Significantly increases the storage 
- 
Stores log and metric data in the same region as your control plane 
 
- 

See [Anypoint Platform Packages and Plans](#billing). For complete details about pricing, contact your customer support representative.

## Anypoint Platform Packages and Plans

Feature availability in Anypoint Monitoring depends on the tier of your Anypoint Platform pricing package or plan:

- 
[Anypoint Monitoring Features for Usage-Based Packages](#plans-usage-based)(Starter and Advanced tiers)
- 
[Anypoint Monitoring Features for Legacy Core-Based Plans](#plans-legacy)(Gold, Platinum, and Titanium tiers)

### Anypoint Monitoring Features for Usage-Based Packages

Anypoint Monitoring provides standard tooling for monitoring Mule app and API performance so that you can more quickly identify and resolve issues.

- 
**Anypoint Integration Starter**package is available to all Anypoint Platform regions.
- 
**Anypoint Integration Advanced**package is available in the[US](https://anypoint.mulesoft.com/monitoring)and[EU](https://eu1.anypoint.mulesoft.com/monitoring)regions only at this time.

All organizations receive fundamental monitoring regardless of pricing model. However, organizations that have the Anypoint Integration Advanced package receive greater storage, guaranteed resources, and advanced capabilities that allow for greater control and flexibility. For more information, see [Anypoint Platform pricing](https://www.mulesoft.com/anypoint-pricing).

If your organization changes its subscription model from the Anypoint Advanced Integration package to the Anypoint Integration Starter package, ensure you have preserved your logs outside of Anypoint Platform. Within an hour of changing pricing models, MuleSoft clears the storage that formerly kept log data.

These features are available for Anypoint Platform customers who have usage-based plans:

| Feature | Anypoint Integration Starter Package | Anypoint Integration Advanced Package | 
|---|---|---|
| Realtime  | No | Yes | 
| No | Yes | |
| No | Yes | |
| No | Yes | |
| Out-of-the-box charts with metrics on individual Mule apps: 
 | Yes | Yes | 
| Advanced metrics for  | No | Yes | 
| No | Yes | |
| No | Yes | |
| 
 | No | Yes | 
| 
 | No | Yes | 
| Out-of-the-box charts with metrics on individual APIs: 
 | Yes | Yes | 
| 
 | No | Yes | 
| 
 | ||
| Distributed log management | No | Yes | 
| Log search | Yes (cross-application) | |
| No | Yes | |
| No | Yes | |
| Log tailing | Yes | Yes | 
| 
 | ||
| No | Yes | |
| Yes | Yes | |
| No | Yes | |
| Enhanced Support | No | Yes | 

| Anypoint Visualizer app network integration refers to features in the Application Networktab within Anypoint Monitoring. Outside of Anypoint Monitoring, the product Anypoint Visualizer is available to organizations in all core-based subscription tiers (Gold, Platinum, Titanium). | 

### Anypoint Monitoring Features for Legacy Core-Based Plans

Core-based subscriptions are based on vCore allotments instead of usage. All organizations receive fundamental monitoring capabilities with their subscriptions. However, customers subscribing at the Titanium tier receive greater storage, guaranteed resources, and advanced capabilities that allow for greater control and flexibility.

If your organization changes its subscription model from a Titanium to a Gold or Platinum subscription, ensure you have preserved your logs outside of Anypoint Platform. Within an hour of changing subscription models, MuleSoft clears the storage that formerly kept log data.

| Feature | Gold and Platinum Subscription Features | Platinum Subscription for Mulesoft Government Cloud Features | Titanium Subscription Features | 
|---|---|---|---|
| Dedicated infrastructure for data processing and storage | No | No | Yes | 
| 
 | No | No | Yes | 
| No | No | Yes | |
| More than 80 out-of-the-box charts covering metrics in the following categories: Overview, Inbound, Outbound, Performance, Failures, JVM, and Infrastructure | Yes | Yes | Yes | 
| No | No | Yes | |
| No | No | Yes | |
| No | No | Yes | |
| 
 | No | No | Yes | 
| 
 | No | No | Yes | 
| 16 out-of-the-box charts covering metrics in the following categories: Overview, Requests, Failures, Performance, and Client Application | Yes | Yes | Yes | 
| 
 | No | No | Yes | 
| Basic mode settings for charts (graphs, singlestats, tables) | Yes | Yes | Yes | 
| Advanced mode settings for charts (graphs, singlestats, tables) | Yes, with limited functionality | Yes, with limited functionality | Yes | 
| Advanced mode with additional features | No | No | Yes | 
| 
 | |||
| 
 | Yes | Yes | Yes, with  | 
| No | No | Yes | |
| 
 | |||
| Log search | No | Yes (cross-application) | |
| No | No | Yes | |
| No | No | Yes | |
| Log Tailing | Yes | Yes | Yes | 
| 
 | |||
| No | No | Yes | |
| Yes | No | Yes | |
| No | No | Yes | |

NOTE:

API Visualizer (formerly Anypoint Visualizer) app network integration refers to features in the **Application Network** tab within Anypoint Monitoring. API Visualizer as a product outside of Anypoint Monitoring is available to organizations regardless of pricing plan.

## Use Cases

The following use cases provide examples of how you can use Anypoint Monitoring.

- 
Understand performance-related KPIs 
 DevOps engineer Gary maintains a series of APIs related to a transaction processing system. Because the TPS requires swift response, Gary uses API response-time dashboards and alerts to send an email when a bottleneck occurs. After gathering some data, Gary can then size his apps.
- 
Plan resource allocation across the app network IT specialist Peyton uses API Visualizer to view their app network. For CloudHub and Anypoint Runtime Fabric apps, Peyton sees CPU and memory utilization and idle capacity using integrated Anypoint Monitoring. 
- 
Pinpoint root causes of issues 
 Support team member Darius receives a call that the system is running slowly. He examines dashboards and checks response times, failed requests, and so on. He identifies that the backend is not scaling for the number of requests; he can add capacity for Mule apps, or he can throttle requests for other backend issues.
- 
Measure API trends 
 Architect Kara monitors several APIs using dashboards, and she reports API call trends to leadership. She creates a dashboard that shows her top 10 API’s trends per month so she can easily identify APIs that have high volumes of calls or issues.
- 
Assess the stability of APIs 
 Operations administrator Vic can periodically assess the error rate and success rate of key APIs using aggregated views and computations in Anypoint Monitoring. Based on their observations, Vic can stabilize or redesign apps that perform poorly.
- 
Analyze logs 
 Support engineer Carole searches through Anypoint Monitoring logs and notices some apps frequently have errors. She uses this data to create dashboards for areas that have frequent issues, and she creates a plan to improve end processes based on the types of errors identified in the logs.
- 
Visualize regional or project-based consumption 
 Business owner Devon has apps across different runtime planes. He has aggregated dashboards of the regional or project-specific apps, and he can easily determine what is consuming the most resources and evangelize accordingly.

## Classic and Enhanced Monitoring Features

On EU and US Clouds, classic and enhanced monitoring feature sets are currently available. Clicking **Insights** from the classic Anypoint Monitoring mode opens to Anypoint Insights, provides access to other enhanced monitoring features, and includes a link back to classic monitoring, **Open Classic Monitoring**.

| Classic Features (US and EU Clouds) | Enhanced Features (US and EU Clouds) | 
|---|---|
| 
 | 
 |