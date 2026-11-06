# Exporting Telemetry Data to Third-Party Monitoring Systems | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/telemetry-exporter](https://docs.mulesoft.com/monitoring/telemetry-exporter)

---

Error : validating connection request. Please check your request and try again

# Exporting Telemetry Data to Third-Party Monitoring Systems

[Advanced and Titanium tiers](/monitoring/#billing)

Export Mule app trace data and [audit logs](../access-management/audit-logging) to third-party observability platforms like Azure Monitor, Splunk HEC, and OpenTelemetry-compliant tools.

To use the Telemetry Exporter, you must:

- 
Create a connection by providing a third-party observability platform credential that authorizes Anypoint Platform to share data with the observability platform. See also, [Supported Third-Party Monitoring Products](#third-party-support).
- 
Create a configuration that specifies the type of data Anypoint Platform exports and which business group and environment allows content to be exported to the connections that you configure. 

You can also edit and delete connections and configurations. Telemetry Exporter checks for changes to connections and configurations on an hourly basis. When you create or modify a connection or configuration, there might be a delay in applying your new settings.

When exported, audit logs have a unique ID in the `mulesoft.audit.id` attribute. In usual operations, each log is delivered only once, but under certain circumstances, some logs are delivered more than once. Duplicate log entries always share the unique `mulesoft.audit.id` attribute, so this attribute can be used to safely block or remove duplicate logs from the target system.

## Supported Third-Party Monitoring Products

The Telemetry Exporter enables you to create connections to most third-party observability and analytics platforms that:

- 
Have OpenTelemetry-supported endpoints. For example, the endpoint URL for New Relic is [https://otlp.nr-data.net:4318](https://otlp.nr-data.net:4318)
- 
Allow you to create an instrumentation key or access token. 

Azure Monitor and Splunk HEC are also compatible.

## Before You Begin

Before you configure the Telemetry Exporter, ensure that you have:

- 
Permissions that you require for your uses of Telemetry Exporter (see [Managing Permissions for Anypoint Monitoring](am-permissions))- 
**Telemetry Exporter Administrator**permission for creating and modifying connections
- 
**Telemetry Exporter Configurations Manager**permission for creating and modifying configurations
 
- 
- 
Access information for your third-party observability platform 
- 
The ability to create an instrumentation key or access token for your third-party observability platform. 
- 
Enabled trace data collection for your Mule apps: - 
For CloudHub 2.0 deployments, see [shared](../cloudhub-2/ch2-deploy-shared-space#enable-trace-data-collection)and[private spaces](../cloudhub-2/ch2-deploy-private-space#enable-trace-data-collection).
- 
For Runtime Fabric deployments, see [Runtime Fabric](../runtime-fabric/latest/use-anypoint-monitoring#enable-trace-data).
 
- 
- 
An endpoint for telemetry data that is accessible from across the internet (CIDR `0.0.0.0/0`) if your observability provider or your organization’s endpoint requires an IP allowlist or firewall ruleConsult your organization’s security guidelines when configuring open access rules for this endpoint. Telemetry Exporter generates its Internet Protocol (IP) address dynamically, which prevents allowlisting specific IPs, URLs, domains. 

## Access Telemetry Exporter

- 
Log in to Anypoint Platform using an account that has the Telemetry Exporter Administrator or Telemetry Exporter Configurations Manager permission. 
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
Click **Telemetry Exporter**.

To use create, view, edit, and delete connections and configurations for telemetry data exports, see [Manage a Connection](#manage-connections) and [Manage Configurations](#manage-configurations).

## Manage a Connection

Anypoint Platform needs permission to send data to third-party observability platforms. Create a connection with a third-party platform, such as New Relic or Splunk, to authorize data transfers. You can configure up to 10 connections.

Telemetry Exporter checks for changes to connections and configurations on an hourly basis. When you create or modify a connection or configuration, there might be a delay in applying your new settings.

### Create a Connection

- 
Log in to Anypoint Platform using an account that has the Telemetry Exporter Administrator permission. 
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
Click **Telemetry Exporter**.
- 
Click the **Connections**tab.
- 
Click **New Connection**.
- 
On the **Connection Details**page, enter the following information:- 
**Connection Name**: Name for your connection, using only alphanumeric characters and hyphens.
- 
**Destination Type**: Third-party observability platform to which you want to transfer data.
- 
**Endpoint URL**: Endpoint that enables external connections to your third-party observability platform (see[Supported Third-Party Monitoring Products](#third-party-support)). Some platforms, such as DataDog, require an OpenTelemetry collector endpoint that is enabled to translate the OpenTelemetry standard to DataDog formats.
 
- 
- 
Click **Next**.
- 
On the **Authentication**page, enter the information needed to authenticate your connection to the observability platform. Some platforms require only access tokens, while others also require a header key.
- 
Click **Test Connection**to ensure that Anypoint Platform can connect to your third-party observability platform.
- 
Click **Save Connection**.The new connection appears in the **Connections**tab on the**Telemetry Exporter**page.

### Edit a Connection

- 
Log in to Anypoint Platform using an account that has the Telemetry Exporter Administrator permission. 
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
Click **Telemetry Exporter**.
- 
Click the **Connections**tab.
- 
Next to the connection you want to edit, click **…**and select**Edit Connection**.
- 
On the **Connection Details**page, edit each field you want to change and click**Next**.
- 
On the **Authentication**page, edit each field you want to change and click**Test Connection**.
- 
If the connection is successful, click **Save Connection**.

### Delete a Connection

- 
Log in to Anypoint Platform using an account that has the Telemetry Exporter Administrator permission. 
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
Click **Telemetry Exporter**.
- 
Next to the connection you want to delete, click **…**and select**Delete Connection**.
- 
A warning appears: - 
If the connection is not in use, the warning asks whether to delete the connection. Click **Delete Connection**.
- 
If the connection is in use, the warning states that you must delete or redirect connections for any configurations that use the connection. Click **Dismiss**, and then[edit your configurations](#edit-configuration)to use other existing connections before deleting the current connection.
 
- 

## Manage Configurations

After you create a connection to your third-party observability platform, you must create a configuration to specify the scope of the data to send to the platform. When you create a new configuration, specify a data type, business group, environment type (traces only), and destination. You can export traces and audit logs from all of your business groups or a specific business group.

Telemetry Exporter checks for changes to connections and configurations on an hourly basis. When you create or modify a connection or configuration, there might be a delay in applying your new settings.

### Create a Configuration

- 
Log in to Anypoint Platform using an account that has the Telemetry Exporter Configurations Manager permission. 
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
Click **Telemetry Exporter**.
- 
Click **New Configuration**.
- 
On the **General Information**page, enter the following information:- 
**Configuration Name**: Name for your configuration that uses only alphanumeric characters.
- 
**Connection**: Existing connection that you configured.
- 
**Data Type**: Audit logs or trace data
 
- 
- 
Click **Next**.
- 
In the **Select Business Group**section, select one of the following:- 
**All business groups**: Audit logs are sourced from all business groups in the organization.
- 
**Select a business group**: Data of the type you specified is sourced only from the selected business group.
 
- 
- 
Click **Next**.
- 
If you selected trace data as the data type, select the environment type: - 
Production 
- 
Sandbox 
- 
Design 
 
- 
- 
Click **Save Configuration**.

### Edit Configurations

When you edit configurations, you can change the configuration name and connection. If you want to modify the data type business group or environment type, you must create a new configuration.

- 
Log in to Anypoint Platform using an account that has the Telemetry Exporter Configurations Manager permission. 
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
Click **Telemetry Exporter**.
- 
Next to the configuration you want to edit, click **…**and select**Edit Configuration**.
- 
On the **General Information**page, edit each field you want to change and click**Next**.
- 
On the **Business Group & Environment Type**page,**Next**.
- 
Click **Save Configuration**.

### Delete Configurations

- 
Log in to Anypoint Platform using an account that has the Telemetry Exporter Configurations Manager permission. 
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
Click **Telemetry Exporter**.
- 
Next to the configuration you want to delete, click **…**and select**Delete Connection**.A warning appears that confirms whether you want to delete the configuration. 
- 
Click **Delete Configuration**.

## Errors

If you receive this error, ensure that your endpoint supports OpenTelemetry:

## Known Issues

Telemetry Exporter currently has the following data differences, limitations, and known issues:

- 
For failed requests, Telemetry Exporter retries are handled using the OpenTelemetry specifications for handling failures: - 
Permanent failures, such as bad requests, do not retry. 
- 
5xx errors that can retry wait for a specific interval. Retries continue for 300 seconds before timing out. 
 
- 
- 
When you create configurations for the same connection, you cannot create a configuration that uses all business groups if there are configurations that use individual business groups. Conversely, you cannot create configurations for that connection if there is a configuration that uses all business groups. 
 For example,`Connection A`to Splunk has`Configuration A`and`Configuration B`that map to`Business Group A`and`Business Group B`. In this scenario, you are unable to use`Connection A`to create a configuration that exports data from all business groups.
- 
Because Azure Monitor Exporter does not support sending persistent queues, connections that use it might experience data loss. Data might be deleted from the sending queue when the Telemetry Exporter restarts hourly to apply updates. 
- 
The audit logs that the Telemetry Exporter sends to third-party apps often have different field names from the audit logs that appear in Access Management or the Audit Query Log API. 
 For example, audit logs shown in the UI or retrieved by the Audit Log Query API describe a user action (such as`update`or`delete`) as`action`, whereas the OpenTelemetry attribute refers to it as`mulesoft.audit.action`.
- 
If the audit log entry metadata and payload field exceed 30KB when compressed, the payload is truncated before compression.