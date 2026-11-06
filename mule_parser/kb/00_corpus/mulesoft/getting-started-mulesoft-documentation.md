# Getting Started | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/quick-start](https://docs.mulesoft.com/monitoring/quick-start)

---

# Getting Started

Anypoint Monitoring provides data on Mule apps, APIs, and instances of agents, brokers, and MCP servers.

| Functional Monitoring is covered in [API Functional Monitoring](../api-functional-monitoring/). | 

## Supported Versions of Mule Runtime Engine

Run your Mule app on a supported Mule runtime version. For supported versions, see [Mule Runtime Release Notes](../release-notes/mule-runtime/mule-esb).

## Use Anypoint Monitoring

- 
Log in to Anypoint Platform with a user account that has [permission to access Anypoint Monitoring content](am-permissions).
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.If you do not find **Monitoring**or are unable to use Anypoint Monitoring, check your permissions ([Required Permission](#required_permission)).
- 
From the sidebar, you can find [Anypoint Monitoring features](./#features).

## Configurations

Custom dashboards and alerts require configuration before you can use them. For guidance, see:

## Required Permission

[Monitoring permissions](../access-management/permissions-by-product#monitoring) lists user and administrator permissions.

Typically, administrators set permissions through Access Management. See [Granting Permissions and Roles to Users](../access-management/users#granting-permissions-and-roles-to-users).

## Enable Anypoint Monitoring on CloudHub

For Anypoint Monitoring to start monitoring your Mule apps, you must deploy them to the appropriate version of Mule runtime engine.  See [Configure Anypoint Monitoring for Mule Apps (CloudHub)](configure-monitoring-cloudhub).

## Enable Anypoint Monitoring On-Premises

You can [install Anypoint Monitoring](am-installing) on an on-premises server to monitor applications that are running on that server and managed via Runtime Manager (hybrid apps).

## Access Key Metrics through the Anypoint Monitoring Agent

Access to [Key Metrics in API Manager](../api-manager/latest/analytics-chart) relies on the Anypoint Monitoring agent. The agent is available by default for some Mule app deployment models. Other models require enablement of Anypoint Monitoring or installation of the agent.

| Mule App Deployment Model | Action | 
|---|---|
| CloudHub 1.0 | Enable Anypoint Monitoring for your Mule Apps. See  | 
| CloudHub 2.0 | No action is required. Key Metrics and Anypoint Monitoring are available by default. | 
| Runtime Fabric | No action is required. Key Metrics and Anypoint Monitoring are available by default. See also,  | 
| Hybrid Deployments | Install the Anypoint Monitoring agent. See  | 
| Standalone Deployments On-Prem | Key Metrics are not supported because standalone deployments are not managed in Anypoint Platform. If you require Key Metrics, convert your standalone deployment to a hybrid deployment (see  |