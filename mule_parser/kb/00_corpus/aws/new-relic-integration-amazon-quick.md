# New Relic integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/newrelic-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/newrelic-integration.html)

---

With the New Relic action connector, you can access the New Relic observability platform directly in Amazon Quick through natural language. You can investigate incidents, analyze application performance, query telemetry data, and generate reports without leaving Amazon Quick.

New Relic is available as a built-in connector in Amazon Quick. To set up this
        integration, complete the following two steps. First, prepare your New Relic account
        with the required access. Then, create the integration in Amazon Quick and authenticate
        with your New Relic credentials. This integration uses OAuth 2.0 user authentication.
        For information about the authentication methods that Amazon Quick supports, see
        [Authentication methods](./quick-action-auth.html).

## Prerequisites

        Before you set up the integration, make sure that you have the following resources and access.

- 
                An active New Relic account with the required permissions and access. For information about account requirements and access configuration, see [New Relic AI MCP](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/)in the New Relic documentation.
- 
                For information about subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## Verify your New Relic account

        Before you configure Amazon Quick, verify that your New Relic account meets the following requirements.

- 
                Your New Relic account is active and you can sign in to [login.newrelic.com](https://login.newrelic.com).
- 
                The entities and data that you want to query are accessible to your account. 

## Set up the integration in Amazon Quick

        After you verify your New Relic account access, create the integration in Amazon Quick.

- 
                In the Amazon Quick console, choose **Connectors**.
- 
                Choose the **Create for your team**tab.
- 
                Find and choose **New Relic**.
- 
                In the **Create integration**dialog, enter the following fields:- 
                        **Name**– A descriptive name for your New Relic integration.
- 
                        **Description**(Optional) – Notes about how you plan to use this connection.
- 
                        **Connection type**– Choose**Public network**.
 
- 
                        
- 
                Choose **Create and continue**.
- 
                On the integration detail page, choose **Sign in**and authenticate with your New Relic account credentials. This step authorizes Amazon Quick to access New Relic on behalf of the authenticated user.
- 
                (Optional) Choose the users to share the integration with. 
- 
                Choose **Done**.

The integration appears in the **Existing actions** panel with
            a status of **Available**.

## Available actions

        After you set up the integration, you can use the following actions.

| Category | Action | Description | 
|---|---|---|
| Incident analysis | Generate Alert Insights Report | Generates an alert intelligence analysis report for a specific issue. Provides insights into root cause, impact, and recommended actions. | 
| Incident analysis | Generate User Impact Report | Analyzes affected entities and their relationships to quantify end-user impact through metrics like affected user count, degraded services, and severity indicators. | 
| Incident analysis | Search Incident | Retrieves alert incident events with flexible filtering by issue ID, entity GUID, or policy and condition pair. | 
| Incident analysis | List Recent Issues | Lists all recent issues (last 24 hours) for a specified account. | 
| Performance analysis | Analyze Transactions | Identifies slow and error-prone transactions, their traces, common transaction paths, and error distributions. | 
| Performance analysis | Analyze Golden Metrics | Analyzes key health indicators (throughput, response time, error rate, and saturation) across application and infrastructure entities. | 
| Performance analysis | Analyze Deployment Impact | Compares metrics before and after a deployment to identify regressions or improvements. | 
| Performance analysis | Analyze Kafka Metrics | Analyzes Kafka metrics including consumer lag, producer throughput, message latency, partition balance, and resource utilization. | 
| Performance analysis | Analyze Threads | Analyzes thread metric data including thread state, CPU usage, and memory consumption. Provides language-specific insights for applications. | 
| Performance analysis | List Garbage Collection Metrics | Retrieves garbage collection and memory metrics for a given entity. Use this action to identify whether GC issues are affecting application performance. | 
| Log analysis | Analyze Entity Logs | Analyzes application logs to identify error patterns, anomalous behavior, and recurring issues within a specified time window. | 
| Log analysis | List Recent Logs | Retrieves recent logs for a specified account and entity GUID. | 
| Error analysis | List Entity Error Groups | Retrieves error groups from the Errors Inbox within a time window. Groups errors by message and prioritizes by user impact. | 
| Queries | Natural Language to NRQL Query | Converts a natural language request into a New Relic Query Language (NRQL) query, runs it against New Relic, and returns the results. | 
| Queries | Execute NRQL Query | Runs an NRQL query directly against New Relic telemetry data. | 
| Entities | Get Entity | Retrieves entities by GUID or searches by name pattern. | 
| Entities | List Related Entities | Retrieves entities that are related to a given entity GUID. | 
| Entities | Search Entity with Tag | Searches for entities by using tag key and value pairs. | 
| Entities | List Entity Types | Lists the complete catalog of New Relic entity types with their domain, type, and metric definitions. | 
| Alerts | List Alert Policies | Lists alert policies for a specified account, with optional filtering by policy name. | 
| Alerts | List Alert Conditions | Retrieves alert condition details for a specific alert policy. | 
| Dashboards | List Dashboards | Lists all dashboards for a New Relic account. | 
| Dashboards | Get Dashboard | Retrieves detailed information for a specific dashboard by entity GUID. | 
| Change tracking | List Change Events | Retrieves a history of change events such as deployments, configuration changes, and other tracked activities for an entity. | 
| Monitoring | List Synthetic Monitors | Lists synthetic monitors that check service availability and performance from multiple geographic locations. | 
| Account | List Available New Relic Accounts | Lists all New Relic account IDs that are accessible to the authenticated user. | 
| Utilities | Convert Time Period to Epoch Ms | Converts a natural language time period to epoch milliseconds for use with time-based queries. | 

###### Note

The actions that you can use depend on the permissions that are configured in your New Relic account and the entities that are accessible to the authenticated user.

## Manage and troubleshoot

        To edit, share, or delete your integration, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

### Authentication issues

- 
                    **Sign-in fails**– Verify that your New Relic account is active and that you can sign in to[login.newrelic.com](https://login.newrelic.com)directly. If your organization uses single sign-on (SSO), confirm that your identity provider is configured correctly.
- 
                    **MCP server access denied**– Verify that your user has the required permissions to access the New Relic MCP server. For information about access requirements, see[New Relic AI MCP](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/)in the New Relic documentation.