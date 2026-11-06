# MuleSoft MCP Servers Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/mulesoft-mcp-server/mulesoft-mcp-server-release-notes](https://docs.mulesoft.com/release-notes/mulesoft-mcp-server/mulesoft-mcp-server-release-notes)

---

# MuleSoft MCP Servers Release Notes

MuleSoft MCP Servers implement the Model Context Protocol (MCP) so AI assistants in your IDE can work with MuleSoft products and services. MuleSoft DX MCP Server supports API design, application deployment, and asset management. MuleSoft Platform MCP Server supports service discovery, policy enforcement, and traffic monitoring across your organization.

## June 2, 2026

### What’s New

- 
New tool: `uc_get_test_generation_info`. Get information about which connector modules (CCM, ACM, FCM) are available and whether tests already exist before generating tests.
- 
New tool: `uc_generate_tests`. Generate tests for connector modules using either mock or real connections.
- 
Tool rename: `uc_generate_api_spec`is renamed to`uc_manage_api_spec`. The renamed tool also supports research-only and validation modes.
- 
Tool rename: `uc_publish_connector`is renamed to`uc_connector_lifecycle`. The renamed tool supports both`build`and`publish`actions.
- 
Tool update: `uc_generate_connector`. The`phases`parameter now accepts`flow`to generate a Flow Connector module in addition to the existing`ccm`and`anypoint`phases.

For tool parameter details, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools).

## May 28, 2026

### What’s New

- 
Introducing MuleSoft Platform MCP Server Get governed access to your entire IT landscape, including APIs, agents, MCP servers, and LLMs, and accelerate production-ready AI at scale. With remote access, use MuleSoft Platform MCP Server to scan, discover, govern, and monitor services across the infrastructure you already run. Typical platform areas you can address include: - 
Service scanning across agentic platforms 
- 
Discovery of APIs, agents, MCP servers, and LLMs in one place 
- 
Policy enforcement for PII detection, semantic routing, and token controls 
- 
Monitoring of traffic, cost, and performance across services 
 
- 

For more information, see [Getting Started with MuleSoft Platform MCP Server](../../mulesoft-mcp-server/getting-started-platform)

- 
With the addition of MuleSoft Platform MCP Server, MuleSoft MCP Server is renamed to MuleSoft DX MCP Server. This is a non-breaking change and only cosmetically affects the UI and documentation. There are no changes to tool names. 

## March 16, 2026

### What’s New

- 
Tool update: `get_flex_gateway_policy_example`. You can now generate examples for these policy features.- 
`ip_filter`: Allow or block requests based on IP addresses and CIDR ranges
- 
`jwt_generate`: Generate JSON Web Tokens
- 
`oauth2_token_introspection`: Validate OAuth2 tokens
- 
`rate_limiting`: Allow or block requests based on rate limits
- 
`data_storage`: Store and retrieve data using the Data Storage Library
 
- 
- 
Installation namespace change: When installing MuleSoft MCP Server in your IDE, the installation command is now `npm install -g mulesoft-mcp-server`. Previously, it used`mulesoft/mcp-server`.

## March 6, 2026

### What’s New

- 
New tool: `uc_add_pagination`. Add pagination support to a specific operation.
- 
New tool: `uc_list_connection_profiles`. List all available connection profiles with their IDs, names, authentication types, and descriptions.
- 
New tool: `uc_manage_operations`. Manage connector operations.
- 
New tool: `uc_publish_connector`. Publish a connector to Anypoint Exchange.

For tool parameter details, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools).

## February 17, 2026

Tool update: `search_asset`. Use the new `exchangeScope` parameter to set the search scope for either private or public assets. Additionally, the `search_asset` tool responses now use standardized relevance scores.

## February 6, 2026

### What’s New

- 
Tool update: `implement_api_spec`. Use APIkit flows to implement an API specification in a new integration project. You can implement a specification from a local asset or an Anypoint Exchange asset.
- 
New tool: `generate_or_modify_munit_test`. Generate, modify, or fix MUnit tests for Mule flows. Provide the flow XML, test scenario description, and dependencies for accurate test generation. Previously generating and modifying MUnit tests were different tools.

For tool parameter details, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools).

## January 15, 2026

### What’s New

- 
New tool: `implement_api_spec`. Use APIkit flows to implement an API specification in a new integration project. You can implement a specification from an Anypoint Exchange asset.
- 
New tool: `generate_munit_test`. Generate MUnit test cases for Mule flows, one test scenario at a time, with support for mocks, assertions, and dependencies.
- 
New tool: `modify_munit_test`. Modify or fix an existing MUnit test case, including updating assertions, mocks, payloads, and test logic.

For tool parameter details, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools).

## November 20, 2025

### What’s New

You can now use the MuleSoft MCP Server to build connectors with Connector Builder. These new MCP tools are available for use in Connector Builder.

- 
`uc_create_connector_workflow`
- 
`uc_generate_api_spec`
- 
`uc_generate_connector`

For more information, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools) and [Generate Base Connectivity with MCP Tools](../../connector-builder/base-connectivity#generate-base-connectivity-with-mcp-tools).

## October 3, 2025

### What’s New

Build Agent Fabric agent networks, manage governance rulesets, and more with new tools. All tools are available in MuleSoft MCP Server in Anypoint Code Builder; they aren’t available for use in other IDEs.

- 
Tools to create, edit, publish, and deploy agent networks for Agent Fabric solutions. 
- 
Tools to list, add, and validate governance rulesets. 
- 
Tools to open, mock, and validate API specs. 
- 
Tool to get metadata and instructions for enabling topics and agent actions from an OpenAI spec. 

For more information, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools).

## August 11, 2025

### What’s New

- 
New tool: `create_and_manage_metadata`. Define metadata for a flow component, attach metadata to Mule flow components, and update existing metadata. To define metadata, provide the Mule configuration file URI and sample data or schema. To apply metadata, specify existing metadata types. To update metadata, provide new schema or sample data.
- 
New tool: `test_connection`. Test a connector configuration for a Mule project. For example, test connectivity for a HTTP listener connection.

For more information, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools).

## July 17, 2025

### What’s New

- 
App Development - 
New tool: `create_api_spec`. Use AI to create an API specification. You must enable Agentforce in[Access Management](../../access-management/).
- 
New tool: `create_api_spec_project`. Create and scaffold an API specification or fragment project. You can specify the project name, location, and language (RAML, OAS, and so on).
- 
New tool: `create_MCP_server`. Create a MuleSoft MCP server. This tool uses Anypoint Connector for MCP (MCP Connector) to handle requests for creating MCP servers.
- 
New tool: `create_mule_project`. Create an integration project.
- 
New tool: `generate_mule_flow`. Use AI to create a flow.
- 
New tool: `run_local_mule_application`. Deploy and run your app locally.
- 
New tool: `search_asset`. Search for an asset in an organization and Anypoint Exchange. Returns the first asset in your organization that matches input criteria. If the tool doesn’t find any assets in your organization, then the tool returns assets in Anypoint Exchange that exactly or partially match`searchQuery`.
 
- 
- 
App Management - 
New tool: `create_and_manage_api_instances`. Create and configure API instances in Anypoint API Manager.
- 
New tool: `list_api_instances`. Get information for instances in an environment. You can also filter by an instance ID or label and include applied or available policies. The tool paginates results using the page parameter. Prompt tip: To get information for all instances, revise the results by using the page parameter.
- 
New tool: `list_applications`. Get information about all apps in the environment that you specify. You can also specify an optional deployment name. Results are sorted by last update date and time, in descending order.
- 
New tool: `update_mule_application`. Update a Mule app deployed to CloudHub 2.0 or Anypoint Runtime Fabric. Update the runtime version, configuration, and other app settings.
 
- 
- 
Policy Management - 
New tool: `manage_api_instance_policy`. Apply a new policy to an API instance and update an existing policy configuration.
- 
New tool: `manage_flex_gateway_policy_project`. Provide instructions to the LLM on how to manage an Anypoint Flex Gateway custom policy project. Instructions include how to create the project, set up the configuration, and build the project. The instructions also include how to publish a development version of the project and publish a release version of the project. See[Prerequisites for Omni Gateway Policy Development Kit (PDK)](../../pdk/latest/policies-pdk-prerequisites).
- 
New tool: `get_flex_gateway_policy_example`. Get an Anypoint Flex Gateway policy example to help you configure your Rust source code. You can get example policies that manipulate a request’s header and body, make HTTP calls to external services, share data between requests and responses, reject requests, and perform sleep operations.
 
- 
- 
Usage and Insights - 
New tool: `get_platform_insights`. See how your organization uses Anypoint Platform through operational insights. Insights include:- 
Usage trends for apps, such as flow count, message counts, and data throughput by business group and environment. Usage trends are for the current month. If it’s early in the month, you get usage for the last full month. 
- 
API and app call volume across consumers for the last 7 days. 
- 
API and app performance metrics such as errors and latency for the last 7 days. 
 
- 
- 
New tool: `get_reuse_metrics`. Get visibility into how you reuse assets across your organization. Drive efficiency, consistency, and cost savings by reducing duplication. Includes sandbox and production environments. Metrics are a year-to-date snapshot.
 
- 

For more information, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools)

## June 3, 2025

### What’s New

- 
App Development - 
New tool: `create_mule_project`. Create an integration project.
- 
New tool: `generate_mule_flow`. Use AI to create a flow.
- 
New tool: `run_local_mule_application`. Deploy and run your app locally.
- 
New tool: `search_asset`. Find an Anypoint Exchange asset by name or other parameters that you specify. Returns the first asset that matches the input criteria.
- 
New tool: `create_and_manage_assets`. Create an asset in Anypoint Exchange, update some Anypoint Exchange asset properties without republishing the asset, and delete an asset in Anypoint Exchange. Asset properties are the asset name, description, icon, contact name, and contact email.
 
- 
- 
App Management - 
New tool: `deploy_mule_application`. Deploy your app to CloudHub 2.0 or Anypoint Runtime Fabric and run it. You can deploy from a local project or Anypoint Exchange asset. This tool supports security, high availability, and performance optimizations for deployments.
- 
New tool: `list_applications`. Get information about all apps in the environment that you specify. You can also specify an optional deployment name. Results are sorted by last update date and time, in descending order.
 
- 

For more information, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools)