# Connector Builder Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/connector-builder/connector-builder-release-notes](https://docs.mulesoft.com/release-notes/connector-builder/connector-builder-release-notes)

---

Text in operation types no longer overflows and is readable for all transformed operations, including paginated CCM operations.

# Connector Builder Release Notes

Use Connector Builder to create your own connectors easily. Connector Builder is an extension that streamlines and accelerates connector development by creating connectors either from an API specification (OAS 3.0), AI assistance (available when using Cursor), or MCP tools (available when using Cursor). These connectors integrate with SaaS applications that use HTTP-based connectivity.

For more information, see [Connector Builder Overview](../../connector-builder/).

## 1.4.0

**June 2, 2026**

| Connector Builder 1.4 is a pre-release that supports creating Flow connectors only. To create Anypoint connectors, use any other version of Connector Builder. | 

### What’s New

- 
You can now use Connector Builder to create Flow connectors that run in Salesforce Flow. All Connector Builder features are available for both Anypoint and Flow connectors. 
- 
These new MCP tools are available for use in Connector Builder. See [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools).- 
`uc_get_test_generation_info`
- 
`uc_generate_tests`
 
- 
- 
These MCP tools are renamed in this version. - 
`uc_generate_api_spec`is renamed to`uc_manage_api_spec`. The renamed tool also supports research-only and validation modes. See[Generate Base Connectivity with MCP Tools](../../connector-builder/base-connectivity#generate-base-connectivity-with-mcp-tools).
- 
`uc_publish_connector`is renamed to`uc_connector_lifecycle`. The renamed tool supports both`build`and`publish`actions. See[Package Connectors with MCP Tools](../../connector-builder/packaging-connectors#package-connectors-with-mcp-tools)and[Release Connectors to Anypoint Platform with MCP Tools](../../connector-builder/releasing-connectors#release-connectors-to-anypoint-platform-with-mcp-tools).
 
- 
- 
You can now execute operations directly from the editor at design time using the Try It panel, without packaging or deploying the connector. The Try It panel is available for all operations, regardless of platform. See [Execute Operations Using the Try It Panel](../../connector-builder/operations#execute-operations-try-it).

### Compatibility

| Software | Version | 
|---|---|
| Mule runtime engine | 4.10 and later | 

## 1.3.0

**March 6, 2026**

### What’s New

- 
These new MCP tools are available for use in Connector Builder. See [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools).- 
`uc_add_pagination`
- 
`uc_list_connection_profiles`
- 
`uc_manage_operations`
- 
`uc_publish_connector`
 
- 
- 
You can now create connection profiles in Connector Builder. See [Use Connection Profiles](../../connector-builder/connections#use-connection-profiles).
- 
You can now generate tests for your Anypoint Connectors. See [Testing Connectors](../../connector-builder/testing-connectors).
- 
You can now specify your own base package and Maven group ID for connectors, rather than using the default values ( `com::mulesoft::connectivity`for the base package and`com.mulesoft.connectivity`for the Maven group ID).
- 
The UI for creating a new project is improved. See [Base Connectivity](../../connector-builder/base-connectivity).

### Compatibility

| Software | Version | 
|---|---|
| Mule runtime engine | 4.10 and later | 

## 1.2.0

**December 18, 2025**

### What’s New

- 
Connector Builder now automatically performs pre-publish validation tasks before publishing connectors to Anypoint Exchange. The improved publishing workflow checks and updates `pom.xml`files to validate group IDs and distribution management settings. It also checks`settings.xml`for Anypoint credentials configuration and provides code snippets to help you configure authentication. Any formatting errors in these files are now displayed directly in the UI for quick resolution.
- 
Version information is now retrieved from the Language Server instead of the CLI, improving accuracy and reliability of dependency version management in project metadata. 
- 
Connector name validation now enforces a 20-character limit to prevent malfunction during connector operations. 
- 
The default Maven repository ID in the Anypoint `pom.xml`file is now set to`Repository`.
- 
Maven profiles are added to configure private Exchange deployment and remove unnecessary artifacts during publishing. 

### Compatibility

| Software | Version | 
|---|---|
| Mule runtime engine | 4.10 and later | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| W-20295471 | |
| Version comparison logic during project regeneration now properly detects version mismatches and displays correct values in comparison pop-ups. | W-20406985 | 

## 1.1.1

**December 18, 2025**

The features and fixed issues for this version are in version 1.2.0.

## 1.1.0

**November 20, 2025**

### What’s New

- 
You can now use the MuleSoft MCP Server to build connectors with Connector Builder. For more information, see [MuleSoft DX MCP Server Tool Reference](../../mulesoft-mcp-server/reference-mcp-tools)and[Generate Base Connectivity with MCP Tools](../../connector-builder/base-connectivity#generate-base-connectivity-with-mcp-tools). These new MCP tools are available for use in Connector Builder.- 
`uc_create_connector_workflow`
- 
`uc_generate_api_spec`
- 
`uc_generate_connector`
 
- 
- 
You can now easily publish connectors to Anypoint Exchange with the improved UI, which clearly guides you through each step of the publishing process. For more information, see [Release Connectors to Anypoint Platform](../../connector-builder/releasing-connectors#release-connectors-to-anypoint-platform).

### Compatibility

| Software | Version | 
|---|---|
| Mule runtime engine | 4.10 and later | 

## 1.0.0

**October 22, 2025**

### What’s New

- 
Connector Builder is now generally available. 

### Compatibility

| Software | Version | 
|---|---|
| Mule runtime engine | 4.10 and later | 

## See Also

- 
[Salesforce Help](https://help.salesforce.com)
- 
[MuleSoft Services](https://www.mulesoft.com/support-and-services)
- 
[Known Issues](https://help.salesforce.com/s/issues)