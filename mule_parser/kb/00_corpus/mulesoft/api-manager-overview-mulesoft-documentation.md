# API Manager Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/latest-overview-concept](https://docs.mulesoft.com/api-manager/latest/latest-overview-concept)

---

![API Manager page navigation shown with callouts.](_images/api-manager-ui-overview.png) 

# API Manager Overview

Anypoint API Manager (API Manager) is a component of Anypoint Platform that enables you to manage, govern, and secure APIs and server instances. It provides an interface to configure the runtime capabilities of Omni Gateway, Anypoint Mule Gateway, and server instance types such as Agents, MCP servers, and LLM servers.

API Manager helps organizations implement API governance policies, monitor API performance, manage server connectivity, and ensure security compliance across their API ecosystem. The tool supports both cloud and on-premises deployments, making it suitable for various enterprise environments.

With API Manager you can:

- 
Enforce policies 
- 
Collect and track analytics data 
- 
Manage proxies, server instances, and client applications 
- 
Provide encryption and authentication 

API Manager is tightly integrated with the following tools:

- 
[Design Center](../../design-center/): To specify the structure of the API
- 
[Exchange](../../exchange/): To store and publish API and server assets
- 
[Studio](../../studio/): To implement the API
- 
[Runtime Manager](../../runtime-manager/): To deploy, manage, and monitor API instances
- 
[API Governance](../../api-governance/): To govern API instances

Before using API Manager, familiarize yourself with the user interface and the tasks you can perform therein.

The following video provides a quick overview of API Manager:

## What API Manager Looks Like

To access API Manager, log in to Anypoint Platform and select **API Manager**:

![API Manager page navigation shown with callouts.](_images/api-manager-ui-overview.png) 

| 1 | The environment selector. Anypoint Platform enables you to create and manage separate deployment environments for APIs and applications. API Manager displays all environments except design environments. For details, see [Switching Environments](switch-environment-task). | 
| 2 | Sidebar: 
 | 
| 3 | The Add APIbutton. Enables you to add a new API instance, to promote an API from any environment to the current environment, or to import a configuration ZIP file that was exported from API Manager. For details, see[Getting Started with Managing an Instance](getting-started-proxy). | 
| 4 | The Environment informationbutton, available only to administrator users. Enables administrators to display a dialog with information about the current environment, such as environment credentials. Use environment credentials to configure Studio to sync with your environment. | 
| 5 | Search. Enables you to search for managed APIs using the API search field. Searches are case-insensitive. Filter search results by selecting Active. | 
| 6 | The tracking registration status of each API: Active,Inactive, orUnregistered.A status of  | 
| 7 | The name of each API. Clicking the API name navigates you to the API Settingsview, where you manage the following:
 | 
| 8 | The percentage of API requests that resulted in errors (in the past 24 hours). If "No Data" is displayed, automatic monitoring has not been enabled for the API. For details, see  | 
| 9 | The total number of API requests (in the past 24 hours). If "No Data" is displayed, automatic monitoring has not been enabled for the API. For details, see  | 
| 10 | The number of contracted client applications for each API. For details,
see [Client Applications, Contracts, and Credentials](api-contracts-landing-page). | 

### Tracking Registration Status

API Manager shows a tracking registration status for each API instance:

- 
**Active**: API Manager is currently receiving activity signals (for example, recent traffic via a registered gateway).
- 
**Inactive**: The API was previously active, but no activity has been observed for a period of time. The last active timestamp is still retained.
- 
**Unregistered**: API Manager has no current tracking data for this API version. This can occur either because the endpoint has never communicated with the platform**or**because tracking data (for example,`lastActiveDate`) was purged after an extended period of inactivity (for example, ~30 days of no activity).

| Governance policies and SLA tiers require the endpoint to be in Activestatus to function. | 

## API Manager Components, Concepts, and Features

### API Instances

An API instance describes a configuration of an API that is deployed on one of the following runtimes: Omni Gateway or Mule Gateway.
API Manager manages API instances after they are created by using the **Add**, **Promote**, or **Import** options. API instances remain under management until they are deleted.

API Manager also manages **server instances** (Agent and Tool Instances) that extend Omni Gateway functionality through Agents, MCP servers, or LLM servers. These are managed separately from API instances.

For more detail, see [Managing Instances](api-instance-landing-page).

### API Summary

The API Summary shows key information about a deployed API instance:

![API Summary page](_images/api-instance-summary.png) 

### Key Metrics

The API Summary page includes a Key Metrics section.

The **Key Metrics** section of the API summary contains the following charts:

- Total Requests
- 
Sum of requests in the selected time period for the given API. Data is aggregated in one minute increments. 
- Total Policy Violations
- 
Sum of requests that return policy violations. Data is aggregated in one minute increments. 
- Total Errors
- 
Sum of HTTP response codes that occur in the selected time period. The response codes counted in this metric are 400, 401, 402, 403, 404, 405, 408, 409, 410, 411, 412, 413, 415, 416, 417, 420, 422, 429, 500, 502, 503, 504, 504, 510, and 511. Data is aggregated in one minute increments. In the chart, HTTP response codes are abbreviated as 4xx and 5xx. 
- Average Response Time
- 
Average response time of requests in the selected time period for the given API. Data is aggregated in one minute increments. 

## Setting the Time Period for Key Metrics

You can view the data points collected for the last given period of time (such as the last 5 or 30 minutes) or over a given date and time range. Use the drop-down in the calendar icon to select the time period to display.

### API Alerts

An *API alert* (different from a Runtime Manager alert) is an alarm that flags one of the following:

- 
The API request violates a policy. 
- 
Requests received by the API exceed a given number within a specified period of time. 
- 
The API returns a specified HTTP error code. 
- 
The API response time exceeds a specified timeout value. 

API Manager triggers alerts when states change from desirable to undesirable or vice versa. When an alert is triggered, API Manager sends an email notification to you and to anyone else you specify in the configuration.

For details, see [Reviewing Alerts Concepts](using-api-alerts).

### Contracts

Contracts define how client applications consume APIs. A client application requests access in Exchange. Either the owner of the API instance approves the request in API Manager or the approval is automatic, depending on configuration.

Contracts are enforced with either of the following:

- 
SLA enforcement policies 
- 
Client enforcement policies 

For details about enforcement policies, see [Client Applications, Contracts, and Credentials](api-contracts-landing-page).

### Policies

Policies enable you to enforce regulations to help manage security, control traffic, and improve adaptability of your APIs. For example, a policy can control authentication, access, allotted consumption, and service level access (SLA).

API Manager supports the following types of policies:

- 
Default policies 
- 
Custom policies 

For details, see [Securing Omni Gateway Instances with Policies](../../gateway/latest/flex-gateway-secure-apis).

### SLA Tiers

*Service Level Access (SLA) tiers* are categories of user access that you define for an API. The tier definition combined with an SLA-based policy determines whether access to the API at a certain level requires your approval. The tier definition also can limit the number of requests an application can make to the API. To enforce SLA tiers, you need to apply a rate-limiting or throttling policy that is SLA-based.

For details, see [Reviewing SLA Tiers Concepts](defining-sla-tiers).

### Settings

When adding an API instance, you configure the API instance settings to set parameters such as the runtime and upstream and downstream URIs.

To add an API instance, see [Add API Instances](add-api-instances).

After you create the API instance, you can edit the configuration settings from Settings.

To edit an API instance, see [Editing an API Instance](edit-api-endpoint-task).

### Governance Report

API Governance is integrated with API Manager to identify the conformance status of your API instances.

API Governance tests API instances against rulesets to determine conformance issues such as missing policies and missing TLS contexts.

You can view the governance validation report details to get the information you need to fix conformance issues. The validation report is available both in API Manager on the Governance Report page and in API Governance.

To learn more about governing your API instances, see [Governing API Instances](govern-api-instances).

### Client Providers (Identity Providers)

You use client providers to enforce security and regulations in your business organization. Client providers authorize client applications.

For details about using client providers, see [Configure Multiple Client Providers for Client Management](configure-multiple-credential-providers).

### API Assets

API assets, published by Exchange, are the components that comprise applications. Components include any of the following:

- 
APIs (OAS, RAML, RAML fragments, HTTP, WSDL, and custom) 
- 
API groups 
- 
Policies 
- 
Examples 
- 
Templates 
- 
Modules 
- 
Connectors 

For details about sharing assets via a private Exchange or an Exchange public portal, see [Publishing Assets](../../exchange/about-sharing-assets).

### API Console

When you create or edit APIs in API Manager, use [Building, Implementing, and Testing a REST API](../../apikit/latest/apikit-4-implement-rest-api) to expose and test your API specification. You can test RAML and OAS APIs when you manage the API as an endpoint with proxy. The console flow is already included and enabled (by default) in the API specification when you download an out-of-the-box proxy for your Mule application.

Starting with Mule 4, you can enable access to API Console and modify the API Console path from API Manager. API Console access from API Manager is disabled by default. For information about how to enable API Console access from API Manager, see [Adding a Mule Gateway API Instance](create-instance-task-mule).

### API Groups

An *API group* is a collection of API instances that act as a single unit, so that applications can access them using one client ID. API groups are created in API Manager and published to Exchange.

For details, see [API Groups](api-groups-landing-page).

### Autodiscovery Schemes

Through autodiscovery schemes, API Manager can track the API throughout the life cycle as you modify, version, deploy, govern, and publish it.

| Multiple `autodiscovery`elements referencing the same API instance are not supported. Each Mule application can be linked to only one API instance in API Manager. | 

### Business Groups

A system administrator groups individuals within an organization into business groups. Each group has its own Exchange API assets and its own environments.

For details, see [Anypoint Platform Business Groups](../../access-management/business-groups).

### Environments

Anypoint Platform enables you to create and manage separate deployment environments for APIs and applications. These environments are independent from each other and enable you to test your applications under the same conditions as in your production environment.

The support for environments in strategic components of Anypoint Platform eliminates the need to construct version names to reflect an environment. Restricting access to and managing environments is also simplified. Permissions to access APIs are environment-based.

For details, see [Anypoint Platform Environments](../../access-management/environments).