# Understand Mule Credits Usage and Rates | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/mule-credits-usage-and-rates](https://docs.mulesoft.com/general/mule-credits-usage-and-rates)

---

# Understand Mule Credits Usage and Rates

A Mule Credit is a fungible currency that allows you to draw down from a single capacity pool as you consume services across MuleSoft. Instead of managing different usage types for all products, you purchase a package of credits to use flexibly across the entire MuleSoft platform. As you use these capabilities, Anypoint Platform deducts the corresponding credit amounts from your available balance.

Mule Credits apply to your entire Anypoint Platform organization and you can’t manage them per business group. Use Mule Credits before the `Order End Date` set in the **Usage Details** table on your **Order Form** because rollovers are not permitted. To see which usage types your subscription includes, refer to your **Order Form**, **Subscription Plan**, or **Features and Entitlement Document**.

## Mule Credits by Subscription Plan

The usage types available to you depend on your subscription plan.

| Subscription Plan | Available Usage Types | 
|---|---|
| 
 | MuleSoft Flows, MuleSoft Messages, Private Spaces, Network Connections, Load Balancers | 
| 
 | IDP Pages, Flow Integration Tasks | 
| 
 | Managed Assets, Gateway Requests, Private Spaces, Network Connections | 
| 
 | MuleSoft Flows, MuleSoft Messages, Managed Assets, Gateway Requests, Private Spaces, Network Connections | 
| 
 | All usage types: MuleSoft Flows, MuleSoft Messages, Managed Assets, Gateway Requests, IDP Pages, Flow Integration Tasks, Private Spaces, Network Connections, Load Balancers | 
| 
 | All usage types: MuleSoft Flows, MuleSoft Messages, Managed Assets, Gateway Requests, IDP Pages, Flow Integration Tasks, Private Spaces, Network Connections, Load Balancers | 

| MuleSoft All-Access License supports pre-commit and unlimited usage models. | 

## Usage Types

Each usage type (also called a meter) tracks a specific dimension of platform consumption. Credit rates vary by monthly consumption volume and reset on the first day of each calendar month. You consume credits at the same rate across all environments, including production, pre-production, sandbox, and design. For the full tiered rate table, see [Rate Cards](#rate-cards).

| Usage Type | Description | 
|---|---|
| 
 | A flow is a sequence of logical operations configured within the XML  Mule apps in production environments typically use multiple flows and subflows to divide the app into functional modules or for error-handling purposes. For example, one flow can receive a record and transform data into a given format that another flow processes. To calculate usage, MuleSoft tracks the number of flows across all business groups, environments, and applications on an hourly basis. For every 24-hour period starting at 00:00 UTC, MuleSoft identifies the hour with the highest flow count as the daily max flow. Based on your contract term, MuleSoft then aggregates these daily maximums over the month or year to determine final usage. | 
| 
 | The total volume of data containers processed by the runtime. To track message usage, the runtime report counts the number of times a Mule event source triggers a message. To calculate usage, MuleSoft aggregates the number of messages daily (UTC time) and monthly. After a Mule event source triggers a message, the report doesn’t track changes to the message because the application’s flows process it internally. | 
| 
 | An asset (API, Agent, MCP Server, or LLM) counts as managed if it has at least one active instance in  Multiple instances within the same business group don’t incur extra charges. Anypoint Platform deducts credits as long as the asset status is Active in API Manager, even if there are no calls to the asset. | 
| 
 | Any request that  | 
| 
 | The number of individual document pages that Intelligent Document Processing (IDP) processes in  | 
| 
 | Individual units of work or actions (reading, creating, or updating a record) executed within  | 
| 
 | A  | 
| 
 | Network connections allow you to securely connect corporate data centers and on-premises applications to CloudHub 1.0 and  | 
| 
 | 
 | 

## Rate Cards

You consume Mule Credits at the applicable multiplier rate based on the usage type identified in the [Mule Credit Rate Card](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/mulesoft/Mule_Credit_Rate_Card.pdf).

If your usage exceeds your contracted amount, MuleSoft sends a monthly overage invoice to your primary billing contact at your standard contracted rate. Contact your account team with any questions about your contract or billing.

## Viewing Usage and Billing

Mule Credits usage, monthly statements, and overage billing are centralized in Salesforce Digital Wallet. If you have an Anypoint Platform organization, you can also view your usage and entitlement details in Anypoint Usage Reports for cross-platform transparency.

To view your Mule Credits consumption:

- 
From the **App Launcher**, click**Digital Wallet**.
- 
Locate the **Mule Credits**consumption card in the**Consumption Cards**tab.

Digital Wallet is available in Lightning Experience in Enterprise and Unlimited editions, and requires the View Consumption user permission.

### Digital Wallet Features at a Glance

| Feature | For More Information | 
|---|---|
| Monitor and analyze near-real-time usage for your consumption-based products. | 
 | 
| View the Consumption Analytics dashboard, which includes Tableau Next visualizations that leverage standard consumption tags. Visualizations are interactive, allowing you to instantly transform your view, drill down into details, and optimize business planning with consumption forecasting. | 
 | 
| Set customized threshold alerts to receive usage notifications when your org’s usage exceeds specified thresholds. Also includes automated Monthly Account Summary emails that summarize usage from the previous month. | 
 | 

For more information about Digital Wallet access, see [Access Digital Wallet](https://help.salesforce.com/s/articleView?id=xcloud.wallet_access.htm&type=5).

## See Also

- 
[Digital Wallet–Enabled Consumption-Based Products](https://help.salesforce.com/s/articleView?id=xcloud.wallet_enabled_products_rate_cards.htm&type=5)(Salesforce Help)
- 
[Mule Credit Rate Card](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/mulesoft/Mule_Credit_Rate_Card.pdf)
- 
[MuleSoft Rates Landing Page](https://www.salesforce.com/mulesoft/rates)