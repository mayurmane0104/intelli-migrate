# Usage Reports Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/usage-reports/usage-reports-release-notes](https://docs.mulesoft.com/release-notes/usage-reports/usage-reports-release-notes)

---

# Usage Reports Release Notes

These release notes reflect enhancements, changes, and bug fixes for Anypoint Platform usage reports.

## May 19, 2026

### What’s New

- 
Mule Credits is now available on Salesforce Digital Wallet. With Digital Wallet, you can track daily and monthly consumption against your remaining capacity, identify usage trends for better budgeting and buying decisions, and configure proactive custom notifications to reduce surprises. Mule Credits is available with MuleSoft Integration, MuleSoft Automation, MuleSoft AI & API Management, Agent Fabric, and MuleSoft All-Access License. The usage types available to you depend on your subscription plan. 

For more information, see:

- 
[Digital Wallet-Enabled Consumption-Based Products](https://help.salesforce.com/s/articleView?id=xcloud.wallet_enabled_products_rate_cards.htm&type=5)

## March 30, 2026

### What’s New

- 
Usage reports now include LLM Proxy usage reports to track the number of tokens your LLM Proxy consumes from an LLM Provider. 

## March 17, 2026

### What’s New

- 
MuleSoft Automation Credits 3.0 is now available in Salesforce Digital Wallet. With this launch, you can now track daily and monthly consumption against your remaining capacity, identify usage trends for better budgeting and buying decisions, and configure proactive custom notifications to reduce surprises. Automation Credits 3.0 includes MuleSoft for Flow: Integration, Anypoint IDP, and MuleSoft for Flow: IDP. Detailed breakdowns of your product consumption are also available in Digital Wallet. MuleSoft Composer and Robotic Process Automation (RPA) are not included in Automation Credits 3.0. As of February 18, 2026, Flow Orchestration is included and don’t consume Automation Credits in 3.0. 
- 
Documentation for [Automation Credits Usage and Rates](../../general/automation-credits-usage-and-rates), previously distributed across Composer, IDP, and RPA documentation, is now available in[Usage Reports](../../general/usage-reports). This consolidation provides a single location for all automation credits information.

For more information, see:

- 
[Digital Wallet-Enabled Consumption-Based Products](https://help.salesforce.com/s/articleView?id=xcloud.wallet_enabled_products_rate_cards.htm&type=5)

## October 13, 2025

### What’s New

- 
Starting in October, new billable usage types for Flex Credits are available in connected Salesforce orgs. If your Anypoint Platform organization has a tenant relationship established with a Salesforce org and Agentforce is enabled, calls to the large language model (LLM) gateway will now consume Flex Credits for applicable AI features. If the connected Salesforce org currently has one of the Salesforce Flex Foundation, Agentforce 1 Edition or Agentforce add-on licenses, calls to the large language model (LLM) gateway will now consume Flex Credits. If you’re using Conversations for the Agentforce services, you’ll continue to consume Einstein Requests. If your Anypoint Platform organization is connected to a Salesforce org that doesn’t have Flex Credits entitlement, Einstein Requests continue to be consumed for applicable AI features. Currently, Einstein Requests consumption is based on calls made to the LLM gateway. To support this change, new Flex Credits usage types are available for AI usage. - 
Starter Prompts 
- 
Standard Prompts 
- 
Basic Prompts 
- 
Advanced Prompts 
 
- 

### What’s Changing

- 
Einstein Requests (ERs) are being unmetered for Anypoint Code Builder, Exchange AI documentation generation, and IDP, effective October 2025. This means Einstein Requests are no longer needed to use AI functionality in these products. 
- 
For Intelligent Document Processing (IDP), effective October 2025: - 
The per page price for Automation Credits 2.0 is being raised from 25 Automation Credits per page to 30 Automation Credits per page. 
- 
The per page price for Automation Credits 1.0 is being raised from 1 MuleSoft Automation Credit = 6 IDP document pages to 1 MuleSoft Automation Credit = 5 IDP document pages. 
 
- 

For more information, see:

- 
[Flex Credits Billable Usage Types](https://help.salesforce.com/s/articleView?id=ai.usage_flex_credits.htm&type=5).
- 
[Einstein Requests Billable Usage Types](https://help.salesforce.com/s/articleView?id=ai.generative_ai_usage_einstein_requests.htm&type=5).
- 
[Large Language Model Support](https://help.salesforce.com/s/articleView?id=ai.generative_ai_large_language_model_support.htm&type=5).

## August 19, 2025

### What’s New

- 
The usage report data now refreshes twice a day. Daily and month-to-date usage reports show updated information multiple times throughout the day and are subject to change. This gives you more current insights into your consumption. For more information, see [Usage Reports](../../general/usage-reports).

## July 7, 2025

### What’s New

- 
Alerts for usage reaching 80% and 90% of the contractual entitlement are now sent automatically to the primary billing contact email address. The primary billing contact gets alerts monthly once thresholds are reached. For more information, see the [Salesforce Usage Alerts FAQ](https://help.salesforce.com/s/articleView?id=004811177&type=1)knowledge article.

## June 26, 2025

### What’s New

- 
Anypoint MQ and Object Store v2 metrics are now available in [Usage Reports](../../general/usage-reports)with historical data.- 
Anypoint MQ reports message units, message bytes, API requests, and messages received. 
- 
Object Store v2 reports effective API requests. For more information about MQ and OS metrics, see: 
 
- 

## June 17, 2025

### What’s New

- 
The Anypoint Usage API is now available on Anypoint Exchange to access monthly and daily usage metrics. For more information, see [Usage API](../../general/usage-reports#usage-api).

## June 3, 2025

### What’s New

- 
The user icon dropdown menu option for **Usage**is renamed to**Usage Reports**.For more information, see [Access Usage Reports](../../general/usage-reports#access-usage-reports).

## April 1, 2025

### What’s New

- 
Usage Reports are now available for hybrid standalone deployments. To view your hybrid standalone deployment flows and messages, see [Supported Mule Runtime Versions](../../general/usage-reports#supported-mule-runtime-versions)for information about upgrading your applications.In a hybrid standalone deployment, you host Mule runtime engine and its services in an environment that you manage. The Mule runtime server can run on a physical server, a virtual machine, or within a third-party cloud installation. 

## March 18, 2025

### What’s New

- 
The usage dashboard includes new metrics for Flex Gateway: - 
Gateway Type Gateway type of the Flex Gateway registered. 
- 
Data Egress (GB) Total amount of outbound data in gigabytes (GB) transmitted by the Flex Gateway egress to upstream services. For more information about Flex Gateway usage metrics, see [Flex Gateway Usage](../../general/usage-metrics#flex-gateway-usage).
 
- 

## December 9, 2024

### What’s New

- 
Usage Reports are now available on Hyperforce. For details, refer to [Hyperforce Release Notes](../hyperforce/hyperforce-release-notes).For more information, see: 

## November 15, 2024

### What’s New

- 
Daily usage reports are now available for API Manager for APIs in preproduction, production, and for unclassified (not associated with an environment) APIs. 
- 
Usage reports for all products are in the new usage reports interface and the legacy view is removed. Historical data for API Manager before September 2024 isn’t available. 

## November 6, 2024

### What’s New

- 
The usage dashboard includes new metrics that provide details to analyze Runtime Fabric instances and application deployments and let you track, monitor, and govern core usage in hybrid environments: - 
CPU Limit Tracks the maximum amount of CPU, allocated by the user, that the application can burst to within the shared cluster or Runtime Fabric instance. 
- 
Cluster Capacity Shows the capacity of a set of workers or nodes that act as a single deployment target for a Runtime Fabric instance. 
 
- 
- 
The exportable CSV file for Runtime Fabric includes a new column ( **RTF Worker Count**). The Runtime Fabric worker count comes from the Runtime Manager configuration defined by the user rather than from the runtime plane.

For more information, see [Runtime Fabric Usage Metrics](../../general/usage-metrics#rtf-usage-metrics).

## September 26, 2024

### What’s New

- 
Daily usage reports and CSV download capabilities are now available. 

## May 1, 2024

### What’s New

- 
Intelligent Document Processing (IDP) metrics are available in Usage Report 

## July 12, 2023

### What’s New

- 
You can now view Mule runtime (Flows, Messages, and Data Throughput) metrics with the application and environment names that were previously shown as IDs. 

## February 1, 2023

### What’s New

- 
Mule runtime (Flows, Messages, and Data Throughput) metrics are available usage reports are available for all customers. 
- 
The maximum number of replicas per application deployed to CloudHub 2.0 is now 16 for organizations that have the Anypoint Integration Advanced package or a Platinum or Titanium subscription to Anypoint Platform.