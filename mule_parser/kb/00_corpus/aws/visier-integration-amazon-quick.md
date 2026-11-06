# Visier integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/visier-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/visier-integration.html)

---

###### Note

This guide covers an integration validated with a third-party MCP server. Visier manages the setup and availability of the MCP server.

With the Visier integration in Amazon Quick, you can access Visier's people analytics platform directly through Model Context Protocol (MCP) server connectivity. You can query live workforce data, analyze headcount trends, assess retention health, generate workforce briefings, and more without leaving Amazon Quick.

Visier is available as an MCP-based connector in Amazon Quick. To set up this integration, complete the following two steps. First, prepare your Visier account with the required API access and MCP server configuration. Then, create the integration in Amazon Quick and authenticate with your Visier credentials.

## Prerequisites

        Before you set up the integration, make sure that you have the following resources and access.

- 
                An active Visier account with API access and MCP server enabled. For information about enabling the MCP server and configuring authentication, see [Visier MCP Server documentation](https://docs.visier.com/developer/agents/mcp/mcp-server-set-up.htm).
- 
                Appropriate data access scopes configured in your Visier account for the workforce data you want to query. 
- 
                For information about subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## Verify your Visier account

        Before you configure Amazon Quick, verify that your Visier account meets the following requirements.

- 
                Your Visier account is active and you can sign in to your Visier environment. 
- 
                You enabled the MCP Server capability in your Visier admin console under **Settings**,**API & Integrations**.
- 
                The workforce data and analytics you want to query are accessible to your account. 

## Set up the integration in Amazon Quick

        After you verify your Visier account access, create the integration in Amazon Quick. The setup wizard has four steps: Connect, Authenticate, Review, and Share integration.

### Connect

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Find and choose **Model Context Protocol (MCP)**.
- 
                    On the **Create integration**page, enter the following fields:- 
                            **Name**– A descriptive name for your Visier integration.
- 
                            **Description**(Optional) – Notes about how you plan to use this connection.
- 
                            **MCP server endpoint**– The MCP server endpoint URL from your Visier admin console.
- 
                            **Connection type**– Choose**Public network**.
 
- 
                            
- 
                    Choose **Next**.

### Authenticate

- 
                    Under **Authentication settings**, enter the OAuth credentials from your Visier MCP server configuration:- 
                            **Client ID**– The OAuth client ID.
- 
                            **Client secret**– The OAuth client secret.
- 
                            **Token URL**– The OAuth token endpoint.
- 
                            **Authorization URL**– The OAuth authorization endpoint.
 Amazon Quick pre-fills the **Redirect URL**.
- 
                            
- 
                    Choose **Create and continue**.
- 
                    In the Visier sign-in popup that appears, enter your Visier credentials and choose **Sign in**to authorize Amazon Quick to access Visier on your behalf.

### Review

- 
                    On the **Review**page, Amazon Quick discovers the tools exposed by the Visier MCP server and displays them in a table. Review the list of available actions to confirm that the expected tools are present.
- 
                    Choose **Next**.

### Share integration

- 
                    (Optional) On the **Share integration**page, search for teams or groups to share the integration with.
- 
                    Choose **Done**.

The integration appears in the **Existing actions** panel with
            a status of **Available**.

## Available actions

        After you set up the integration, you can use the following actions. The Visier MCP server exposes its people analytics capabilities as callable tools.

| Action | Description | 
|---|---|
| `ask_vee_question` | Asks Visier's Vee AI a natural language workforce question, such as headcount, turnover, or requisitions. | 
| `aggregate_metric_values` | Computes aggregate values for a metric, optionally grouped by a dimension and filtered by specific members. | 
| `sample_vee_questions` | Returns a list of sample questions that you can ask Vee to get started. | 
| `search_analytic_objects` | Finds analytic objects (for example, Employee or Applicant) matching a search string. | 
| `search_analytic_object_properties` | Returns all available properties for a given analytic object. | 
| `list_analytic_object_property_values` | Lists property values for specific analytic object members, such as employee tenure or pay. | 
| `search_metrics` | Finds metrics matching a search string. | 
| `search_dimensions_for_metric` | Finds dimensions available for a given metric, usable for grouping or filtering. | 
| `search_dimensions_for_analytic_object` | Finds dimensions available for a given analytic object. | 
| `search_filter_dimension_members` | Returns filterable members for a given dimension. | 
| `get_object_reference_graph` | Returns the reference graph showing how a given analytic object connects to others. | 

## Manage and troubleshoot

        To edit, share, or delete your integration, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

### Authentication issues

- 
                    **MCP server connection fails**– Verify that you enabled the MCP Server capability in your Visier admin console under**Settings**,**API & Integrations**. Confirm that you entered the endpoint URL and credentials correctly in Amazon Quick.
- 
                    **Data access errors**– Verify that the data access scopes configured in your Visier account include the workforce data you are trying to query. Contact your Visier administrator to review your account permissions.
- 
                    **No tools discovered**– If Amazon Quick does not discover any tools after you enter the MCP server URL, confirm that the MCP server is active. Also verify that your authentication credentials have not expired.