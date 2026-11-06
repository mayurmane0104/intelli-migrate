# Usage Reports | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/usage-reports](https://docs.mulesoft.com/general/usage-reports)

---

One of these versions or any later date-patch:

Mule 4 image versions:

- 
4.5.0 and later 
- 
4.4.0-20230111-1 
- 
4.3.0-20221212-2 
- 
4.2.2-20221027-7 
- 
4.2.1-20221027-7 
- 
4.2.0-20221027-6 

Usage reports provide comprehensive monthly and daily summaries that give you valuable insights into your resource use across Anypoint Platform products. By correlating your usage with billing cycles, you can gain insights into the factors influencing your costs. This enables you to proactively manage your budget and make informed decisions to optimize your resource allocation.

When you use an Anypoint Platform product that is metered, MuleSoft measures your usage and aggregates the records on a daily and monthly basis.

Usage report data is refreshed twice a day. The most recent three days of data is subject to change. For example, on January 10, data from January 7 to January 10 might still be updated. Data from January 6 and earlier is final and won’t change.

All reports are calculated using the UTC time standard. For example, a daily usage is aggregated from 00:00 to 00:00 UTC.

Daily usage retention is three months and monthly usage retention is up to five years.

Organizations that have a usage-based pricing model can compare actual usage from the report against the existing contract. However, usage reports are not for billing purposes. For more information about usage metrics and pricing, read [Anypoint Platform Pricing](pricing) and [Usage and Pricing Metrics Reference](usage-metrics)

Some usage data, such as monthly statements and vCore allocation, appears in different areas of Anypoint Platform or Salesforce products.

Monthly statements for Mule runtime, including Mule flows, Mule messages, and data throughput are sent to the primary billing contact.

[Automation credits](automation-credits-usage-and-rates) for RPA, Composer, Intelligent Document Processing (IDP), Salesforce Flow Orchestration, and MuleSoft for Flow are sent to the primary billing contact.

For more information, see [Monthly Account Summaries](https://help.salesforce.com/s/articleView?id=000390885&type=1) documentation in Salesforce.

Usage of certain Salesforce generative AI features (Agentforce and Einstein generative AI) or direct calls to the large language model (LLM) gateway consumes credits. All Salesforce AI usage from Anypoint Platform features is routed through your connected Salesforce org, which tracks consumption and handles billing.

Anypoint Platform features that use Einstein generative AI or Agentforce features include:

Anypoint Code Builder

Use MuleSoft Dev Agent to develop integrations and API specs.

For more information about this feature, see [Developing Integrations Using MuleSoft Vibes](../anypoint-code-builder/int-ai-developing-integrations) and [MuleSoft Vibes Overview](../anypoint-code-builder/mulesoft-vibes).

Intelligent Document Processing (IDP)

Use Einstein generative AI to read and interpret documents.

For more information about this feature, see [Enhancing Data Extraction with Einstein](../idp/enhancing-data-extraction-with-einstein)..

Anypoint Exchange

Use Einstein generative AI to generate API documentation for REST APIs.

For more information about this feature, see [Generating API Documentation with Generative AI](../exchange/generating-documentation-with-ai).

For more information about how the usage for these features is tracked and billed, see [Agentforce and Generative AI Usage and Billing](https://help.salesforce.com/s/articleView?id=ai.generative_ai_usage.htm&type=5).

Alerts for usage reaching 80% and 90% of the contractual entitlement are sent automatically to the primary billing contact email address. The primary billing contact gets alerts monthly once thresholds are reached.

For more information, see the [Salesforce Usage Alerts FAQ](https://help.salesforce.com/s/articleView?id=004811177&type=1) knowledge article.

Runtime Manager vCore allocation information and other metrics appear in Access Management.

For more information, see [Runtime Manager Metrics](usage-metrics#runtime-manager-metrics).

Government Cloud and Anypoint Private Cloud Edition usages aren’t available in usage reports.

The following products are available in usage reports:

Anypoint MQ

API Experience Hub

API Governance

API Manager

Omni Gateway

Omni Gateway LLM Proxy

Intelligent Document Processing (IDP)

Mule Runtime

Object Store v2

To view usage reports for Mule runtime, all applications (in production and sandbox) must use these Mule versions:

| Deployment Type | Version Requirements | 
|---|---|
| CloudHub 2.0 | The latest date-patch versions for 4.3.0 and later | 
| CloudHub | The latest date-patch versions for 3.9 and 4.2.0 and later | 
| Runtime Fabric | One of these versions or any later date-patch: Mule 4 image versions: 
 | 
| Hybrid Standalone | One of these versions or any later date-patch: 
 Runtime Manager Agent 2.7.0 and later | 

You must redeploy your apps with a supported version, either manually or during the monthly patching cycle. The monthly patching cycle is applicable only for CloudHub and CloudHub 2.0 applications.

You can [roll back](../cloudhub-2/ch2-update-apps#roll-back-to-a-previous-successful-configuration) to a previous successful application configuration. However, if an app is using a Mule version not supported by usage reports, you must choose a compliant Mule version before deploying changes. After deployment, a new configuration with the previously chosen settings and a supported runtime is created.

Usage reports are available only when you’re signed in to the root organization and don’t appear at the business group level.

To access usage reports, you need the [Usage Viewer permission](../access-management/permissions-by-product#usage). If you don’t have this permission, contact your organization administrator to request access. The Usage Viewer permission must be [applied at the root organization level](../access-management/managing-permissions) rather than the business group level.

Sign in to Anypoint Platform using an account that has the Usage Viewer permission for your root organization.

In the Anypoint Platform navigation bar, click the business group selector, and ensure you are at the root organization level.

In the Anypoint Platform navigation bar, click your username icon and select **Usage Reports**.

Select the product for which to view a usage report.

Click **Monthly Usage Report** or **Daily Usage Report**.

Select the month or day of the usage report to view. For the selected product, only dates that Anypoint Platform collected data for are available.

The usage report appears, displaying an assortment of usage metrics that are [dependent on the product you selected](usage-metrics).

You can export both daily and monthly usage reports to CSV files. These metrics match the data available in usage reports.

Navigate to the usage report to download.

Click **Export as CSV**.

Use the Anypoint Usage API to programmatically access usage data. The API provides both daily and monthly details. Usage metrics are organized by business group and application. This provides detailed insight into product consumption.

To use the API, see the API documentation for the [Anypoint Usage API](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a/usage-api/) for access and implementation details. Users must have Usage Viewer permission to access the Usage API.

All features of Usage Reports are supported on Japan and Canada control planes.