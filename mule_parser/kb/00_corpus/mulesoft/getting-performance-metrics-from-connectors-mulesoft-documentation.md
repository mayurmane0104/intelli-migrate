# Getting Performance Metrics from Connectors | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/monitor-connectors](https://docs.mulesoft.com/monitoring/monitor-connectors)

---

- 
Requests: Average number of Anypoint MQ connector inbound requests, grouped by operation and automatic intervals 
- 
Response Time: Average response time of Anypoint MQ connector inbound requests, grouped by operation and automatic intervals 
- 
Failures: Average number of Anypoint MQ connector inbound request failures, grouped by operation and automatic intervals 

# Getting Performance Metrics from Connectors

[Advanced and Titanium tiers](/monitoring/#billing)

View performance metrics for supported connectors in your Mule apps in Anypoint Monitoring dashboards. Built-in dashboards and Anypoint Insights support these connector metrics.

## Supported Mule Versions

To monitor connectors, you must use a [supported Mule version](../release-notes/mule-runtime/mule-esb) for your apps:

- 
Hybrid deployments 
- 
CloudHub and CloudHub 2.0 deployments 

| If your app uses Java 17, you must specify the version during deployment. For a list of compatible connectors, see [Java 17 Compatible Anypoint Connectors](https://help.salesforce.com/s/articleView?language=en_US&id=000782248&type=1). | 

## Connector Metrics

The type of connector determines the charts that are displayed. Unless otherwise specified, the following metrics are for outbound requests only.

| Connector | Charts | 
|---|---|
| 
 | |
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | The connector type "Other" is any connector not specified in this table. 
 | 

## Access Connector Monitoring

- 
Log in to Anypoint Platform with a user account that has [permission to access Anypoint Monitoring content](am-permissions).
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
Open **Insights**or**Built-in dashboards**.
- 
Navigate to a Mule app that uses a supported connector. 
- 
In the detail page for the app, click **Connectors**to view connector metrics.If you don’t see the **Connectors**tab, verify that you have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform and that the app you selected is running on a supported version of Mule.