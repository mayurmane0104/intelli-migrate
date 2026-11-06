# Anypoint Exchange Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/exchange/anypoint-exchange-release-notes](https://docs.mulesoft.com/release-notes/exchange/anypoint-exchange-release-notes)

---

The scope URL validation for the Microsoft Copilot scanner is now updated and no longer fails to retrieve agents during a scan.

# Anypoint Exchange Release Notes

Anypoint Exchange is a curated catalog of reusable assets such as agents, APIs, API groups, API spec fragments, brokers, custom assets, examples, large language models (LLMs), Model Context Protocol (MCP) servers, policies, templates, integration assets such as connectors. You can catalog (publish), share, discover, learn about, and reuse assets within your organization to facilitate collaboration, boost productivity, and promote standards.

## June 2026

### What’s New

The required scope URL to retrieve agent metadata for the Microsoft Copilot scanner is updated to  [https://<orgId>.api.crm.dynamics.com](https://<orgId>.api.crm.dynamics.com)[Adding a Scanner for Microsoft Azure Copilot](../../exchange/adding-microsoft-copilot-scanner).

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| W-22550680 | |
| Agent cards for agents added in Exchange from Anthropic Claude, Databricks Agent Bricks, and Snowflake Cortex AI now display the protocol type as Other instead of A2A. | W-22493536, W-22493540, and W-22493542 | 

### What’s New

- 
Administrators can now add scanners to automatically discover and catalog services for these external providers: - 
Anthropic Claude (agents) 
- 
Databricks Agent Bricks (agents) 
- 
LangChain LangSmith (agents) 
- 
Snowflake Cortex AI (agents) 
- 
Snowflake MCP (MCP servers) For more information, see: 
 
- 

## May 2026

### What’s New

- 
Generative AI documentation now supports gRPC APIs, MCP servers, and agents, in addition to REST, SOAP, AsyncAPI, and GraphQL APIs. For more information, see [Generating API Documentation with Generative AI](../../exchange/generating-documentation-with-ai).
- 
You can now add a scanner to discover, import, and sync APIs from external providers into Exchange. Once imported, you can apply governance rulesets and publish these services to a developer portal. Supported gateways are Amazon API Gateway, Azure API Management, Kong API Gateway, and Google Apigee. For more information, see: 
- 
The Amazon AgentCore scanner has been enhanced to now support the automatic discovery and cataloging of MCP servers. After the MCP servers are registered, you can govern and consume them in other applications. For more information, see [Adding a Scanner for Amazon Bedrock AgentCore MCP](../../exchange/adding-agentcore-mcp-scanner).
- 
You can now review and approve scan results before they’re imported into Exchange, giving you control over which external services are added to your catalog. When you configure a scanner to **Ask to review**, its status changes to**Pending review**after the scan completes. Open the scan to choose which services to import. Services you don’t import remain pending and reappear in the next scan. To permanently exclude a service from future scans, use the action menu to add it to the**Skipped**list.To enable manual review, set the scheduled run configuration to **Ask to review**when you add or edit a scanner.For more information, see [Review Scan Results Manually](../../exchange/managing-scanners#review-scan-results-manually).
- 
The **Agent Scanners**page in the Exchange sidebar has been renamed to Scanners, where you can now access all scanners regardless of service type from a single page.For more information, see [Discovering and Cataloging External Services with Scanners](../../exchange/discovering-and-importing-external-agents).

## April 2026

### What’s New

- 
Exchange now supports SHA-256 checksums for all assets, providing higher security standards for verifying asset integrity during download and distribution. 
- 
In addition to REST APIs, generative AI now supports expanded API documentation generation for SOAP APIs, AsyncAPI, and GraphQL. You can now generate documentation for API assets published using either single-file or multi-file specifications. For more information, see [Generating API Documentation with Generative AI](../../exchange/generating-documentation-with-ai).
- 
Agents verified by GoDaddy agent network service (ANS) in API Management now display a verified badge in the Exchange catalog and on asset detail pages, helping you quickly identify trusted assets. Instances also show whether managed instances are verified. For more information, see: 
- 
You can now add a scanner to automatically discover and catalog Amazon Bedrock AgentCore and Microsoft Foundry agents. This lets you govern and consume the agents in other applications. For more information, see: 
- 
Permissions for configuring a Microsoft Copilot Studio scanner now include read-only access for scanning Microsoft Copilot Studio agent metadata. For more information, see [Adding a Scanner for Microsoft Azure Copilot](../../exchange/adding-microsoft-copilot-scanner).

## March 2026

### What’s New

- 
You can now use the Exchange MCP server endpoint to retrieve asset and instance metadata from Exchange for your AI agents, without requiring Flex Gateway. For more information, see [Retrieving Asset Metadata Using an MCP Server Endpoint](../../exchange/retrieve-asset-metadata-using-mcp).
- 
Informatica’s CDGC Metadata Search MCP server and Cloud Address Verification MCP server are now available in Exchange. These assets are published to Exchange under **Provided by MuleSoft**and are maintained by Informatica.For more information about publicly hosted MCP servers, see [MuleSoft Assets](../../exchange/#mulesoft-assets).
- 
Exchange now supports gRPC APIs. You can now publish and consume gRPC APIs in Exchange. A gRPC API is specified in a Protocol Buffers (.proto) file that declares services and message contracts. For more information, see: 

## February 2026

### What’s New

- 
You can now add a scanner to automatically discover and register GoDaddy ANS agents. GoDaddy ANS agents are verified by GoDaddy to be safe and secure. Govern and consume the agents in other applications. For more information, see: 

## January 2026

### What’s New

- 
You can now add agent scanners to automatically discover and register AI agents across agent ecosystems on external platforms, which include Amazon Bedrock, Google Vertex AI, and Microsoft Azure Copilot. After the agents are registered, govern and consume them in other applications. For more information, see [Discovering and Cataloging External Services with Scanners](../../exchange/discovering-and-importing-external-agents).
- 
You can now use an MCP server URL to add the server’s metadata when publishing it to the registry in Exchange. For more information, see [Create an MCP Server](../../exchange/to-create-an-asset#create-mcp).
- 
Exchange now syncs public MCP servers from the official MCP registry to **Provided by MuleSoft**.These public MCP servers are maintained by the original providers and not MuleSoft. 
- 
You can now create and manage instances for publicly available MCP servers in API Manager to govern and monitor public assets. These assets are published to Exchange under **Provided by MuleSoft**and are maintained by their original providers, not by MuleSoft. When you create an instance from a publicly available asset, the instance is created within your private organization in Exchange and managed like any other instance in API Manager.For more information see, [Adding an MCP Server from Public Exchange](../../api-manager/latest/create-instance-public-exchange).
- 
You can now request access to running instances from publicly available assets. Instances for MCP servers published in **Provided by MuleSoft**are created within your private organization.

## November 2025

### What’s New

- 
API Notebook reached End of Life on November 28, 2025. 

## October 2025

### What’s New

- 
API Notebook is scheduled for End of Life on November 28, 2025. 
- 
Exchange now supports agent, broker, large language model (LLM), and Model Context Protocol (MCP) server asset types and Agentforce agents for Agent Fabric. For more information, see: 

## July 2025

### What’s New

- 
Admins can choose how asset owners can dte asset versions in Exchange. They can enable or disable the ability to permanently delete an asset to reuse the GAV (group ID, asset ID, and version) for a new asset. It doesn’t matter when the asset version was created. When enabled, asset owners see an option to allow the GAV to be reused when deleting an asset version. When disabled, the GAV can’t be reused after deleting the asset version. For more information, see [Managing Asset Deletion](../../exchange/managing-asset-deletion).
- 
Admins can control whether or not to assign owner roles when creating assets using a connected app. When enabled, when creating new assets using a connected app, roles aren’t assigned to connected app owners. When disabled, roles are assigned by default. For more information, see [Managing Connected Apps](../../exchange/managing-connected-apps).

## June 2025

### What’s New

- 
Users can now generate comprehensive and standardized API documentation for REST APIs from Exchange. This feature uses Einstein generative AI to analyze and create documentation, saving time and effort and ensuring high quality API creation. Users can focus on developing APIs while Einstein handles the documentation. For more information, see [Generating API Documentation with Generative AI](../../exchange/generating-documentation-with-ai).
- 
Client application owners can now add multiple individual users or teams as additional owners, granting them management capabilities for the client application. For more information, see [Add Users as Client Application Owners](../../exchange/about-my-applications#add-users-as-client-application-owners).

## December 2024

### What’s New

- 
This product is now available on Hyperforce. Anypoint Platform instances on the Hyperforce infrastructure are: - 
[Canada Cloud](https://ca1.platform.mulesoft.com)
- 
[Japan Cloud](https://jp1.platform.mulesoft.com)For more information, see [Anypoint Exchange on Control Planes](../../exchange/#exchange-on-control-planes).
 
- 

## October 2024

### What’s New

- 
You can now publish AsyncAPI 2.6 specifications with Avro schemas to share, discover, and reuse within your organization. To learn about the AsyncAPI journey, see [AsyncAPI Support to Implement Event-Driven Architecture](../platform/event-driven-api).

## September 2024

### What’s New

- 
The Exchange Maven Facade API version 3 now supports dynamic parameters for `artifactId`and`version`fields.For more information, see [Publishing Assets Using Maven](../../exchange/to-publish-assets-maven).

## June 2024

### What’s New

- 
You can now publish AsyncAPI 2.6 specifications to share, discover, and reuse within your organization. To learn about the AsyncAPI journey, see [AsyncAPI Support to Implement Event-Driven Architecture](../platform/event-driven-api).

## April 2024

### What’s New

App developers can now view GraphQL schemas and write, run, and test GraphQL APIs using the GraphQL console from the asset details page.
For more information, see [Viewing GraphQL API Schemas and Run Queries](../../exchange/view-graphql-api-schemas-and-run-queries).

## February 2024

### What’s New

You can now see the compatible Java versions for a connector by clicking **View version** in the asset details page.

## October 2023

### What’s New

You can now find and discover assets using the **Custom field** filter in the enhanced search experience. For more information about the custom field filter, see [Filter By Custom Fields](../../exchange/to-find-info#filter-by-custom-fields).

## July 2023

### What’s New

Exchange now provides asset usage and engagement metrics for administrators and asset owners to gain insight into the consumption and user engagement of their API specification fragments and REST APIs. The usage metrics measure how many times those assets are downloaded from Exchange, imported from API Designer, imported from Anypoint Studio, and the number of dependents and contracts for the asset. The asset engagement score is a composite metric that administrators and asset owners can use to measure the usage of the assets in Exchange.

## May 2023

### What’s New

The assets details page lets you find specific information within the API specification and pages of an asset using the CTRL+F or the command+F keyboard shortcut. In Exchange, this enhanced shortcut overrides the native browser shortcut, which searches only for words and phrases on the current page.

## April 2023

### What’s New

Exchange now includes the following RPA template asset types:

- 
RPA Activity templates Activity templates are reusable code within RPA to standardize the most used activity steps and make them available to other developers in the organization. These templates are `.cawl`files that are imported in the RPA Activity library for developers to use as part of their RPA processes.
- 
RPA Process templates Templates for RPA processes are imported into RPA Builder as projects and are customizable before deploying to RPA bots. Process templates are built on common patterns for RPA to build automation faster. These templates are `.crpa`files that are exported from RPA Builder to share with other developers.

## February 2023

### What’s New

- 
The enhanced search is now the default search experience for users logging into Exchange. Using the enhanced experience, you can: - 
Filter assets by type, organization, category, tag, and lifecycle state 
- 
See which API Spec properties and page text matched the search term 
- 
Save shortcuts to filters you have applied 
- 
Sort search results by relevance, name, last modified date, or rating 
 For more details about the enhanced search, see[Search for Assets](../../exchange/to-find-info).The legacy search experience is still available by clicking **Back to legacy search**from the Exchange landing page.
 
- 
- 
Exchange now supports JSON Schema and OAS 3.0 components as sub-types for the API Fragments asset type. 

## January 2023

### What’s New

- 
The documentation now uses more inclusive language. 
- 
The product now uses more inclusive language. 
- 
Exchange now includes the GraphQL API asset type. A GraphQL API allows a client to fetch only the object types and fields needed instead of fetching a fixed response like in a REST API. 
- 
A new Creator permission gives users the Asset Administrator role for the assets they create but restricts modifying assets or asset versions created by other users in the business group. For details, see [Set User Access Permissions](../../exchange/to-set-permissions).

## August 2022

### What’s New

A new **Conformance Status** page enables API developers to see details about conformance of their validated API definitions to governance rulesets. For details, see [View Conformance Status](../../exchange/asset-details#view-conformance-status).

## July 2022

### What’s New

- 
The search functionality has the following enhancements: - 
Improved sorting and synchronization between filters and the sidebar 
- 
Results display in list view when a search query is executed 
- 
Advanced search experience is enabled when searching for assets within the **shared with me**tab
 
- 

## April 2022

### What’s New

Exchange now includes the following asset types:

- 
Policy definition - Policies enforce regulations to help manage security, control traffic, and improve API adoption. Create a policy definition based on your specific business requirements and apply them to APIs to extend existing functionality or define new ones. 
- 
Ruleset - Rulesets are a group of rules or guidelines that define an application, for example, best practices or industry-specific standards. Add a ZIP file with multiple YAML files that describe the new ruleset. 

## March 2022

### New Features

Exchange now supports asset lifecycle states of development, stable, and deprecated to track the progress of assets as they move through the software development lifecycle.

We intuitively redesigned the asset details page and added the following capabilities:

- 
Affinity grouping - Asset information is now intuitively organized. 
- 
Patch versions - New Manage versions table to quickly view version details, add and delete a version, and change the lifecycle state for a version. 
- 
Lifecycle states - View the lifecycle state of an asset. 
- 
Last modified date - See when an asset was changed. 
- 
Collapsible metadata - Hide and expand metadata such as version, last published, categories, and tags. 

## September 2021

### New Features

- 
The Exchange API enables you to update asset metadata, including categories, custom fields, tags, and documentation pages, without needing to create a new asset version. 

### Fixed in This Release

- 
The **API is behind firewall**setting persists across page refreshes and different browser sessions in the same browser.
- 
Search results display correct asset names. 

## August 2021

### New Features

- 
The Exchange GraphQL API version 2 exposes the `status`and`contractsCount`properties for the API instances related to an API asset.
- 
The Exchange GraphQL API version 2 exposes the `apiGroupInstances`property with information from the API group instances related to an API group asset.
- 
The Exchange API, Exchange GraphQL API version 2, and Exchange Maven Facade API support connected application authentication, which can execute Exchange requests without sending a token by using the client application credentials of the client ID and client secret. 
- 
The Exchange form to publish assets has an optimized user experience. 
- 
Exchange supports resizing the portal sidebar to improve the readability of long API console endpoint labels. 
- 
The Exchange API portal includes an example `curl`request to add resources.
- 
The API console supports options to sort endpoints alphabetically and to show full endpoint paths. 
- 
Exchange validates tag length. 

### Fixed in This Release

- 
The delete version button works correctly for policy assets. 
- 
Selecting a section in the portal sidebar does not close API console dropdown menus. 
- 
Canceling changes on the asset sharing page works correctly. 
- 
After deleting a category, search results display the correct assets. 

## July 2021

### New Features

- 
Each asset has the optional properties `contactName`and`contactEmail`to record the name and email address of a person to contact about the asset.
- 
Audit logs record creating a public portal and discarding a public portal draft. 
- 
Exchange API version 2, Exchange Maven Facade API, and Anypoint CLI enable you to use a single request to both create an asset and set mutable asset data including tags, categories, custom fields, and documentation pages. 

### Fixed in This Release

- 
For users who are not logged in, public portals display a disabled request access button with a tooltip explaining that the user must log in to make a request. 
- 
Exchange prevents creating a category with an invalid value for the field `assetTypeRestrictions`.

## June 2021

### New Features

- 
Exchange administrators and asset administrators can share an asset with a team in their organization. 
- 
The Exchange interface implements improved accessibility standards, including: - 
Colors with better contrast for button hover states, links to rate and review assets, and search fields 
- 
Typeahead styles 
- 
Focus states for certain menus and buttons 
- 
Dropdown menu styles 
- 
Page title field styles 
 
- 
- 
The Anypoint CLI `asset list`command accepts an optional`organization`argument.
- 
Exchange security sanitizes asset information to plain text for asset-sharing notification emails. 
- 
The Anypoint CLI supports managing asset portal resources such as images with the `exchange asset resource`commands.

### Fixed in This Release

- 
The **View Code**action correctly links to Anypoint Design Center for API assets.
- 
The **Open Flow**action correctly links to Anypoint Flow Designer for template assets.
- 
Audit logs record adding assets to and removing assets from a public portal. 
- 
Exchange prevents changing instance visibility while the instance is loading. 

## May 2021

### New Features

- 
Exchange relocated interface elements to prevent confusion, including the search bar and the button to publish assets. 
- 
On macOS, you can save the asset name with the Command+Return keyboard combination. 

### Fixed in This Release

- 
Exchange security prevents certain types of cross-site scripting attacks that exploit remote image headers. 
- 
Exchange security prevents certain types of path traversal attacks that attempt to expose authorization tokens. 
- 
Deleted minor versions of assets do not appear in menus or cause "Resource not found" errors. 
- 
You can assign new values to variables defined in previous executions of API notebooks. 
- 
Search results correctly display titles of terms and conditions pages. 
- 
The API instances list displays with correct alignment when showing errors. 
- 
Files upload correctly after a failed previous upload attempt. 

## April 2021

### New Features

- 
Exchange cookie consent management provides public portal website visitors with full documentation and control of all cookies, in compliance with marketing and privacy regulations. 

### Fixed in This Release

- 
The version menu is visible when a video is included in the asset description. 
- 
When you apply a change to a category, the Exchange interface shows an animation while the change is applied. 
- 
Exchange API requires authorization to rate or review assets. 
- 
When you add an asset type restriction to a managed category, the value for that category is removed from each asset whose type is not allowed by the restriction. 
- 
Portal editing works correctly with the Apple Safari browser. 
- 
Deleting a category removes it from all assets. 
- 
Exchange shows only relevant warning messages. 
- 
Exchange verifies that asset type restrictions for tags use valid asset types. 

## March 2021

### New Features

- 
Exchange API v2 offers several new features: - 
Share assets with users and organizations. 
- 
Edit the version-agnostic properties of an asset: name, description, and icon. 
- 
Request access to API Groups. 
- 
Add resources such as images to the asset documentation and the public portal. 
- 
Publish assets asynchronously. 
- 
Publish and consume any asset type supported by Exchange, including connectors, examples, templates, Mule applications, and policies. 
 
- 
- 
Exchange Maven Facade API v3 includes improved error messages, publication feedback, and the capability to publish custom assets. Using Maven Facade API v3 to publish assets to Exchange requires the Mule Maven plugin version 3.5.0 or later. For examples and details, see the [New Features](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/exchange-maven-facade-api-http/minor/3.0/pages/New%20Features/)section of the API documentation on Exchange.
- 
Exchange star ratings have enhanced design for improved accessibility. (EXC-7286) 
- 
When you share an asset and search for users, Exchange uses enhanced highlighting on the search results as you type. (EXC-5434) 
- 
Exchange does not require you to scroll to read long tag names. (EXC-4261) 

### Fixed in This Release

- 
To ensure that assets use semantic versioning, Exchange prevents you from creating an asset with a version that starts with `v`. (EXC-7210, EXC-7292)The Exchange user interface supports accessing and deleting existing assets with versions that start with `v`.
- 
When you change an API to private or public, Exchange immediately shows the update. (EXC-6871) 
- 
When you add a category value to an asset, Exchange shows newly created values. (EXC-6822) 
- 
Exchange supports listing and downloading asset portal pages using Anypoint CLI. (EXC-5362) 
- 
When you add or delete a review, Exchange immediately shows the update. (EXC-3022) 

## February 2021

### Fixed in This Release

- 
Exchange graph search returns results correctly and without errors. (EXC-3769) 
- 
The Markdown editor visual mode does not escape underscores when it is not necessary. (EXC-4564) 
- 
After you create a new application on the request access page, the application menu shows all available API instances. (EXC-6398) 

## January 2021

### Fixed in This Release

- 
Deleting a review of a previous patch version of an asset works correctly. (EXC-7020) 
- 
Minor version selection on the API instances page works correctly and does not leave the page. (EXC-7068) 
- 
The sidebar shows correct highlighting when an account has only one organization. (EXC-7037) 
- 
The `exchange asset copy`command of`anypoint-cli`correctly copies the specified asset. (EXC-7086)
- 
When you change the business group scope in the navigation bar, the business group section in the sidebar shows the correct business group. (EXC-7105) 

## December 2020

### New Features

- 
The request access panel correctly filters API instances and does not show deprecated instances. (EXC-3044) 
- 
Audit logs record changing an asset name, description, or icon. (EXC-6975) 
- 
The portal of an asset with an unsupported type displays correctly without a 500 error. (EXC-7007) 

### Fixed in This Release

- 
Exchange documentation pages support links to other documentation pages such as `[the home page](pages/Home)`. (EXC-6778)
- 
Public portals correctly show only public API instances. (EXC-6969) 
- 
Deleting a terms and conditions page works correctly. (EXC-6983) 
- 
In a client applications page, the button to download charts downloads the CSV file correctly. (EXC-7062) 

## November 2020

### New Features

- 
The new Exchange search experience shows more than 20 results. 
- 
The new Exchange search experience offers multiple [search result relevance](../../exchange/to-find-info)options.
- 
The Exchange API version 1 documentation on Exchange is edited and updated. 

### Fixed in This Release

- 
In asset portals, long category names display correctly and wrap correctly. (EXC-3023) 
- 
When searching all types in a public portal, the asset type filter correctly shows **All types**. (EXC-6370)
- 
Opening Exchange in Anypoint Studio does not display an incorrect message about temporarily disabled search features. (EXC-6723) 
- 
The API instances page for API groups shows the sidebar. (EXC-6868) 

## October 2020

### New Features

- 
Attempting to publish an asset with a changed API version but without an increased asset major version shows an improved error message. (EXC-4989) 
- 
The asset creation page shows information about the `groupId`field. (EXC-5326)
- 
The version field shows help text about Semantic Versioning and a link for more details. (EXC-5423) 
- 
The title of the page for adding a new version correctly reads **Add a new version**. (EXC-5424)

### Fixed in This Release

- 
Links to Exchange documentation page headers work correctly. (EXC-6413) 
- 
Public portals consistently show the API console. (EXC-6526) 
- 
Removing all asset type restrictions from a category’s configuration does not change the categories assigned to an asset. (EXC-6592) 
- 
When you log in to Anypoint, the sidebar correctly highlights the selected section. (EXC-6618) 
- 
After you create a new asset version, Exchange correctly renders the public portal. (EXC-6650) 
- 
Exchange prevents users from navigating from a portal draft to the group instances page. (EXC-6675) 
- 
When requesting access to an API group, the preview of the terms and conditions renders correctly. (EXC-6672) 
- 
The search field **Clear**button has accessibility text. (EXC-6776)
- 
Exchange correctly encodes login redirection URIs without 404 errors. (EXC-6840) 

## September 2020

### New Features

- 
Asset portals validate images and discard corrupted files. (EXC-6619, EXC-6643) 

### Fixed in This Release

- 
Asset creation works in all cases when publishing from Anypoint Studio. (EXC-6400) 
- 
The API console renders endpoints in the correct order. (EXC-6445) 
- 
A saved search without an organization filter returns results correctly. (EXC-6553) 
- 
Exchange has improved session cookie security. (EXC-6656) 

## August 2020

### Fixed in This Release

- 
Exchange prevents inconsistently sharing an asset with the same API version in a different asset major version. (EXC-6517) 
- 
Deleting an asset with a dependency loop works correctly. (EXC-6554) 
- 
Anypoint Studio correctly shows the public portal for a custom asset. (EXC-6599) 

## July 2020

### New Features

- 
An error in a field of the advanced section expands the section to make it visible. (EXC-4263, EXC-6056) 
- 
Exchange shows loading states when editing an asset name or asset description. (EXC-6091) 
- 
Changing or removing an icon from an Exchange asset also changes or removes the icon from automatically generated assets such as Mule connectors and plugins. (EXC-6356, EXC-4421) 

### Fixed in This Release

- 
Creating an asset with a connected application token works correctly and without authorization errors. (EXC-6198) 
- 
The request access page correctly shows API instance environment names. (EXC-6264) 
- 
An asset’s public portal prevents users from performing private portal actions such as share and edit. (EXC-6281) 
- 
On the asset creation page, if the `assetId`field shows an error message, modifying the field correctly updates the message. (EXC-6302)
- 
Public portals correctly render custom favicons. (EXC-6359) 

## June 2020

### New Features

- 
Exchange supports OpenAPI Specification (OAS) 3.0 APIs. 
- 
Exchange includes new API console version 6.2, including support for OAS 3 specifications. 
- 
Public portals prompt external users for read-only access to their basic profile information when they log in for the first time. (EXC-4846) This change applies to all Anypoint Platform instances hosted in the EU control plane, in the US control plane, or in MuleSoft Government Cloud. 
- 
Exchange shows a descriptive error message when an asset ID field is not unique. (EXC-5328) 

### Fixed in This Release

- 
Images render correctly when changing versions on an asset portal. (EXC-4677) 
- 
The Exchange public portal prompt ensures user approval for all user information access. (EXC-4846) 
- 
Exchange prevents errors by correctly distinguishing session management between private Exchange instances and public portals. (EXC-4891) 
- 
Public assets provided by the MuleSoft organization do not include the redundant `visibility`attribute. (EXC-4892)
- 
A proxy serves external images so that image servers cannot read user IP addresses. (EXC-5361) 
- 
Exchange GraphQL v2 API calls return only successfully generated connectors. (EXC-5413) 
- 
Intermittent issues preventing public Exchange from rendering correctly are fixed. (EXC-5419) 
- 
Mocking service instances in API portals display the correct public or private visibility status. (EXC-5939) 
- 
Exchange prevents users from navigating to an inconsistent editing state. (EXC-5943) 
- 
Exchange returns correct `customFields`objects and no empty objects for all API queries. (EXC-6016)
- 
The **API instances**section of an API specification asset portal renders correctly when the API version contains non-ASCII characters. (EXC-6057)
- 
The API console renders correctly after leaving edit mode in a portal. (EXC-6058) 
- 
The mocking service accepts calls with a `baseUriParameter`value. (EXC-6061)
- 
Asset type icons render correctly in the overview panel of asset detail pages. (EXC-6082) 
- 
Exchange security prevents users from including remote HTML files. (EXC-6101) 

## May 2020

### New Features

- 
Graph search provides enhanced search capability powered by the application network graph. 
- 
For Anypoint Platform instances hosted in the EU control plane, public portals prompt external users for read-only access to their basic profile information when they log in for the first time. This change is not yet released to the Anypoint Platform instances hosted in the US control plane or MuleSoft Government Cloud. 
- 
API Groups enable organizations to publish related APIs bundled into a single unit, and enable developers to learn about and request access to groups of related APIs as a single unit. 
- 
Exchange supports saving the asset description by using the Command+Return or Control+Enter keyboard combination. (EXC-3762) 
- 
Uploading an image with a file extension that does not match the file’s actual type shows a more descriptive error message. (EXC-5902) 

### Fixed in This Release

- 
Exchange prevents using invalid sessions in private portals. (EXC-4828) 
- 
The **External**indicator displays with improved visibility when a user shares assets with an external organization. (EXC-5250)
- 
Public portals correctly display asset icons to users who are not logged in. (EXC-5293) 
- 
Users see a warning if a public API’s instances are all private. (EXC-5367) 
- 
Saving a public portal customization draft works correctly in all cases. (EXC-5383) 
- 
Version groups with spaces or special characters work correctly in asset URLs. (EXC-5418) 
- 
In Anypoint Studio 6, Exchange correctly shows the status of installed connectors. (EXC-5445) 
- 
Exchange security prevents errors when using fetch manual redirection inside API notebooks. (EXC-5937) 
- 
The **Policies**asset type in the type filter no longer shows the label**New**. (EXC-6050)

## April 2020

### New Features

- 
Client credentials are segregated across multiple identity providers (IdPs). In the Request Access dialog in Exchange, users select an API instance and then select or create a client application for the identity provider to which the instance belongs. 
- 
Exchange asset portals support WebP images. (EXC-3337) 
- 
Anypoint API Designer correctly publishes an asset to Exchange when the asset’s version group contains an underscore. (EXC-5927) 

### Fixed in This Release

- 
Client management works correctly for organizations without a defined client management type. (EXC-3011) 
- 
In a public portal, changing the version group of an asset works correctly. (EXC-4009) 
- 
Publishing an asset version works correctly after a failed previous attempt. (EXC-5214) 
- 
The asset portal for an asset with the "SNAPSHOT" suffix on every version loads correctly. (EXC-5349) 
- 
Publishing a new asset using a token that belongs to a connected application works correctly. (EXC-5357) 

## March 2020

### New Features

- 
The Markdown editor toolbar’s header button supports multiple header sizes. (EXC-3033) 
- 
Users can perform a single step to create a new application, request access to an API instance for that application, and select a service level agreement (SLA) tier for that access. (EXC-5251) 
- 
All assets have consistent navigation by minor version, and asset properties such as tags, categories, custom fields, and Markdown content pages are consistent for each minor version. (EXC-5180) 

### Fixed in This Release

- 
The API console renders endpoints in the correct order. (EXC-5308) 
- 
When the public portal login page background color is white, the **Sign up**button displays correctly. (EXC-4864)

## February 2020

### New Features

- 
When users update the asset name, description, labels, or categories of a REST API, these properties are updated in the generated connectors. (EXC-4699) 

### Fixed in This Release

- 
Exchange security prevents specific types of cross-site scripting attacks in the API console for OAS specifications by correctly escaping malicious user input. (APIC-361) 
- 
The request access feature prevents errors by ensuring a user selects an API instance before creating a new application. (EXC-5181) 
- 
Users can always log out without errors from an Exchange portal with a vanity domain. (EXC-4693) 

## January 2020

### New Features

- 
Cross-organization sharing enables a user to share an asset with their organization or an external organization and make the asset’s details viewable by all users of that organization. 
- 
Improved accessibility including keyboard accessibility for menus, filters, and other UI controls, and improved usability of API instances, sharing, deleting assets, and other application controls on screens with small resolutions. 
- 
Improved interface to request API access by showing the API instance selection menu and then the application selection menu, and showing the link to create a new application on the application selection menu. (EXC-4856) 
- 
The interactive API console is updated to include: - 
Latest web standards 
- 
WCAG 2.1 AA accessibility 
- 
New console elements for examples and annotations in documentation 
- 
Endpoints ordered in the UI, even when they are not ordered in the spec 
- 
Reduced time to initialize application 
- 
Request editor panel that only renders headers that are defined in the spec 
- 
Optimized performance for complex APIs 
 
- 

### Fixed in This Release

- 
Multiple issues in the interactive API console were fixed in this release. 
- 
Markdown pages display correctly for all content. (EXC-4950) 
- 
Exchange shows a message about the current search results only when search terms have been entered. (EXC-4848) 
- 
Exchange security prevents specific types of cross-site scripting attacks in API notebooks by correctly escaping malicious user input. (EXC-4781) 

## November 2019

### New Features

- 
Exchange public portal login pages reflect the public portal custom colors and logo and offer both standard Anypoint Platform login and optional single sign-on using a third-party identity provider. (EXC-4176) 
- 
Exchange supports terms and conditions pages for HTTP and SOAP API asset types. (EXC-3967) 
- 
Exchange shows that the review field is actionable, so a user can start a new review. (EXC-3962) 

### Fixed in This Release

- 
Category values containing spaces work correctly in GraphQL queries. (EXC-4610) 
- 
Users can make requests to endpoints other than the mocking service in public portals that have custom non-MuleSoft domains, also known as vanity domains. (EXC-4617) 
- 
Public portals that use vanity domains correctly show customer favicons. (EXC-4577) 
- 
Exchange wraps long custom field values to display the complete value. (EXC-4573) 
- 
Requesting access to an API redirects the user to the correct login page, either the organization login or the Anypoint Platform login, as configured by the organization administrator. (EXC-4557) 
- 
Users can edit pages that were created before Exchange validated page names and that have page names containing restricted characters. (EXC-4259) 
- 
Categories with names containing `/`or`\`can be deleted. (EXC-3791)

## October 2019

### New Features

- 
Exchange enhanced layout and readability for long names, page titles, API versions, organization names, and usernames in the asset portal. (EXC-4067, EXC-4068, EXC-4070, EXC-4071, EXC-4072) 
- 
The left navigation bar refers to the home page of the asset portal as "Home" and not as the asset name. (EXC-4069) 
- 
Exchange orders the HTML headers of the asset portal into correct document hierarchy for better accessibility. (EXC-3961) 

### Fixed in This Release

- 
The request access modal displays the correct SLA tier for each API instance. (EXC-4389) 
- 
Exchange prevents UI crashes when customizing colors for public portals. (EXC-4386) 
- 
API access requests work correctly for all API version names. (EXC-4345) 

## September 2019

### New Features

- 
General accessibility is improved in several ways throughout the Exchange UI. (API Console is not changed, and will have accessibility improvements in a later release.) (EX-R-105) - 
Exchange provides enhanced site semantics and Accessible Rich Internet Applications (ARIA) attributes. 
- 
Exchange has skip links for users navigating the site with a screen reader and easier design for users navigating the site with a keyboard. 
- 
Exchange pages have better indicators of which page element has focus, and better keyboard controls for focus. 
- 
Exchange messages and dialogs about user errors are clearer and do not rely on color as the sole means of communicating information. 
 
- 
- 
Users can publish new versions of Mule 3 connectors as Mule 4 extensions. (EXC-4227) 
- 
Improved placement of the **Publish new asset**button helps users to avoid publishing a new asset when searching for an asset. (EXC-3965)
- 
The page editor expands to fit the browser window. (EXC-3964) 
- 
Exchange enforces consistency across all versions of the asset in the three version-agnostic properties of name, icon, and description. (EXC-3391) 

### Fixed in This Release

- 
When a user is not logged in and requests access to an API from a public portal that has a vanity domain, Exchange directs the user to log in and does not show an error message. (EXC-4197) 
- 
Users are limited to writing only one review for each asset version so that they cannot manipulate the average ratings of assets by writing multiple reviews. (EXC-4179) 
- 
When Exchange loads images from external sites, the referrer headers do not reveal authorization codes. (EXC-4133) 
- 
Users can access and delete APIs that have API versions containing non-ASCII characters. (EXC-4130) 
- 
Exchange security prevents specific types of cross-site scripting attacks in API notebooks by disabling certain JavaScript functionality as described in [Document an Asset Using API Notebook](../../exchange/to-use-api-notebook). (EXC-4056)
- 
Users can run the `exchange asset describe`command in the Anypoint CLI on all asset types. (EXC-4052)
- 
Exchange security prevents certain types of cross-site scripting attacks on the public Exchange portal. (EXC-3727) 

## August 2019

### New Features

- 
The maximum number of values for each category increased from 200 to 500. (EXC-4066) 
- 
Exchange supports custom policies and enables users to browse, search, and filter policies. (EXC-3163) 
- 
Exchange prevents resource exhaustion attacks by limiting the number of asset versions that can be published. (INFOSEC-9354) 

### Fixed in This Release

- 
Users can successfully import all API connectors to Anypoint Studio. (EXC-4075) 
- 
When a user deletes and re-uploads an API, the user sees the correct API console. (EXC-4073) 
- 
Anypoint Exchange prevents disclosure of an asset creator’s personal information. (EXC-4063) 
- 
Corrected permissions prevent Asset Contributors from deprecating an asset, which is allowed only for an Organization Administrator, Exchange Administrator, or Asset Administrator. (EXC-3980) 
- 
Logging in to a federated organization that uses an external client identity provider opens the organization’s private Exchange portal and not the public portal. (EXC-3959) 

## July 2019

### Fixed in This Release

- 
If your session expires, you can log back in with no authorization errors and no need to refresh the page. (EXC-3904) 
- 
You can delete assets that have many versions. (EXC-3850) 
- 
You can delete assets that have long API versions. (EXC-3849) 
- 
When you use Maven to request the latest version of an asset, Exchange returns the asset with correct metadata. (EXC-3580) 
- 
Exchange prevents you from uploading a file whose type is not allowed, even if its file extension is incorrect. (EXC-3399) 

## June 2019

### New Features

- 
Markdown editor supports toggling bold text. (EXC-3825) 
- 
Validation of user input in API Instances table improved. (EXC-3809) 
- 
Studio experience interface simplified to show only applicable links. (EXC-3759) 
- 
Both markdown editor and visual editor provide full control of heading levels. (EXC-3643) 
- 
Permissions errors prevented by making only viewable assets clickable in the asset dependencies table. (EXC-3607) 
- 
When you view assets by business group and select a different business group, you see the new group and not the root organization. (EXC-3430) 
- 
Validation of user tag entry improved. (EXC-3414) 
- 
When you click a category or tag, you see matching assets from all business groups and assets provided by MuleSoft. (EXC-3219) 
- 
If the server is at capacity and unavailable when you try to use an API, you see a descriptive error message. (EXC-2991) 

### Fixed in this Release

- 
Edit mode does not show incorrect "Loading API" message. (EXC-3810) 
- 
Images uploaded after May 31, 2019 render correctly on the MuleSoft public portal. (EXC-3793) 
- 
Short and wide icons representing assets are correctly rendered in the UI. (EXC-3792) 
- 
Sharing an asset with a user while related assets are being generated shares the related assets as well. (EXC-3719) 
- 
When you use the mocking service through Exchange, it correctly recognizes headers and security schemas. (EXC-3711) 
- 
All users can always view images on custom pages in a public portal. (EXC-3669) 
- 
When you are editing one page, you can discard those changes and create a second page. (EXC-3642) 
- 
You receive an improved error message when you attempt to use Maven to publish a new version of a REST API created in Exchange with a different asset type, which is forbidden. (EXC-3511) 
- 
Exchange automatically revalidates the file when you upload a file to create a new asset and change the asset type. (EXC-3503) 
- 
Publishing through Maven correctly validates `groupId`and`assetId`values. (EXC-3361)
- 
APIs published in the Public Exchange portal display the full RAML and OAS code. (EXC-3254) 
- 
Exchange preserves user input entered while the API Console is loading. (EXC-3024) 
- 
You can install the SSH connector when using Anypoint Studio 6. (EXC-3014) 

## May 2019

### New Features

- 
Improved readability of API instances when requesting API access, especially for long API instance names. (EXC-3636) 
- 
When using direct upload, provide relevant information about the files that should be uploaded for each asset type. (EXC-3427) 
- 
Users can now customize the order of the user-generated pages in the public portal. (EXC-3405) 
- 
Users can now add SVG images as resources for asset portals and public portal customization. (EXC-3350) 
- 
Exchange now [searches](../../exchange/to-find-info)properties defined in RAML and OAS API specifications and the full text of asset portal page content. Users no longer need to create complex tags and categories to enable finding assets, since they can now search the API docs and API specs in addition to name, categories, and tags. (EXC-2967)

### Fixed in this Release

- 
When creating a SOAP API, the "File URL" link is now validated. File URLs entered with no protocol before validation was enabled will be updated to default to `http`. (EXC-3641)
- 
Users can use the mocking service to try the APIs available in public portals with branded domain names. (EXC-3585) 
- 
Prevent Exchange contributors and Exchange admins from changing the API name in the public portal, which should be a read-only view of the asset. (EXC-3568) 
- 
When accessing MuleSoft public assets, provide correct error information (401 instead of 404) to the Maven CLI so that Maven can retry the request with proper credentials instead of failing. (EXC-3520) 
- 
When an API version is made public, the visibility indicator in the API version drop-down in the asset portal reflects the correct state. (EXC-3513) 
- 
Remove orphan connectors when an API asset version is deleted. (EXC-3510) 
- 
Improve readability of portal page tables with long words. (EXC-3495) 
- 
Generate the correct mocking service URL for OAS API specifications. (EXC-3478) 
- 
Custom icons for an asset’s portal are now used in the dependencies table. (EXC-3471) 
- 
Tags are no longer overwritten with the previous asset version’s tags when updating the asset name. (EXC-3442) 
- 
Users can now upload assets using relative file paths in an `anypoint-cli`interactive session. (EXC-3423)
- 
Unauthenticated access to portal images is disabled for images uploaded after this update. To disable unauthenticated access to an image uploaded before this update, download it, remove it, and [upload it again](../../exchange/to-describe-an-asset#add-an-image). (EXC-3394)
- 
Prevent inconsistent asset type across multiple versions of an asset. (EXC-3392) 
- 
Making a version of an API public now depends on validation of that version and not on validation of uncompleted versions. (EXC-3336) 
- 
The browser back button now displays the correct pages in all cases. (EXC-3334) 
- 
Improve validation of the request body when creating contracts using the Experience API. (A contract is the link between a client application and an API instance.) (EXC-3021) 

## April 2019

### New Features

- 
Adding multiple tags to an asset is now easier. After a user types the tag and presses enter, a new tag is automatically started. (EXC-3431) 
- 
Exchange events, such as the most recent asset details page visited in Exchange, are now shown in the Recent Items list in the common Anypoint Platform navigation bar. (EXC-3264) 
- 
Users can now delete a draft of portal documentation. Previously users could only delete by editing the draft, removing all new edits, and publishing. When there were multiple changes in the draft, it could be difficult to tell which edits belonged to the draft and which to the old version. With the new option to delete a draft, users can have confidence that the right changes will be discarded automatically, preserving the original documentation content. (EXC-3116) 
- 
Added information messages when trying to create a page with an invalid name in the Asset Detail Page to explain why the validation failed and how the user can make the page name valid. (EXC-3041) 
- 
All policy URLs now have MuleSoft domains, so allowlists for API policies now require only MuleSoft URLs. No need to also add Amazon S3 URLs. (EXC-2680) 
- 
Users can now automate the publishing process by using the Command Line Interface (CLI) to upload RAML and OAS specifications to Exchange. (EXC-2539) 

### Fixed in this Release

- 
Exchange now generates the correct representation of mocking service URLs for OAS specifications. (EXC-3478) 
- 
To prevent hackers from accessing the authorization token from the request header, the authorization token is no longer included in the request header in each request made with API Console. (EXC-3416) 
- 
Enabled filtering by asset type in the public portal. (EXC-3400, EXC-3390) 
- 
If the user creates a Terms and Conditions page to supplement their asset documentation page, the Terms and Conditions page is now visible at all times. (EXC-3383) 
- 
Added `jpeg`to the list of supported extensions for portal resources (`bmp`,`gif`,`ico`,`jpe`,`jpeg`,`jpg`,`png`,`svg`,`tif`,`tiff`,`webp`). (EXC-3351)
- 
If the user selects the **API is behind firewall**option, navigates away, and returns, the selection is now remembered. (EXC-3335)
- 
Provided guardrails to prevent users from creating more than 50 pages in the documentation of a single asset. This prevents wasting unnecessary resources to support an unlimited number of pages. (EXC-3157) 
- 
Prevented users from creating portal contents without an associated file when publishing API specifications. (EXC-2541) 

## March 2019

### New Features

- 
Enable customers to use the Try It panel for API instances that are behind their firewall. (EXC-3117) 

### Fixed in this Release

- 
Links to websites outside the MuleSoft Public Exchange no longer show a blank page. (EXC-3172) 
- 
Dependency snippet in Public Exchange now shows up in focus, so users don’t have to scroll down and don’t fail to see the snippet dialog at the bottom of the page. (EXC-3166) 
- 
Accurate warning and error displayed when the user has reached the Maximum Page limit of 10 pages per portal in Public Portal. (EXC-3054) 
- 
There is no limit on the number of client applications or contracts visible to the user when the user tries to request access for an API or browses the client applications in the "My Applications" page. Previous limit was 200. (EXC-3017) 
- 
Enable customers to add custom headers in the Try It panel in the Exchange Portal API Console. (EXC-3008) 
- 
Maven dependencies for the test scope are no longer visible in the dependencies section in Exchange. (EXC-2624) 
- 
Correct error message when trying to publish an OAS 3 specification, since OAS 3 is not supported. (EXC-2552) 
- 
New error message reflects the correct information when an attempt is made to create a new asset with the same GroupID-AssetID-Version (GAV) as an asset deleted within the past 7 days. Error message changed from "Asset already exists. Choose another asset name or version." to "There is a deleted asset with the same version number. Try creating your new asset with a higher version number." (EXC-2484) 
- 
Validate that a published WSDL has either a WSDL file or a URL for a WSDL file, and not both. (EXC-2354) 

## February 2019

### New Features

- 
Syntax highlighting in asset description markdown content. (EXC-3226) 
- 
Faster contextual navigation with clickable tags and categories in asset details page. By clicking on a tag or category, Exchange triggers a search of all of the assets that contain that tag or category. (EXC-3227) 
- 
Easy drag and drop image upload on Exchange’s markdown editor. (EXC-3228) 

### Fixed in this Release

- 
The organizationId field is mandatory when publishing assets through Exchange xAPIs. Previously not sending organizationId returned a misleading 404 (Not Found) error. Now not sending organizationId returns an accurate 400 (Bad Request) error. (EXC-3168) 
- 
Public portals that use vanity domains to promote their company domain name can now render the API Console. API Console enables users to explore the API spec and try it out. (EXC-3143) 
- 
When a user goes to edit mode from a page that does not exist in the draft, Exchange now opens the home page in edit mode without an error. (EXC-2992) 
- 
Maven Facade now returns user-friendly and relevant error message text and code when internal services fail to validate a Mule asset. (EXC-2911) 
- 
Previously exceeding the rate limit for the underlying authentication service returned a misleading 401 (Unauthorized) error. Now exceeding the rate limit for the underlying authentication service returns an accurate 429 (Too Many Requests) error. (EXC-2900) 
- 
Exchange now prevents users from uploading compressed (zip) files whose uncompressed contents will exceed the maximum allowed size limit. Users will receive a 413 (Payload Too Large) HTTP error. (EXC-2527) 
- 
Allow Cyrillic text in category names. (EXC-2461) 

## January 2019

### New Features

- 
Conversion from RAML to OAS 2.0 and from OAS 2.0 to RAML in the publication process. 
- 
Ability to download a REST API specification in either RAML or OAS 2.0 with identification of the "Generated" specification. 
- 
Direct upload of RAML and RAML fragments. 
- 
New API console experience. 
- 
Consistent API specification publication user interface between Exchange and API Manager. 
- 
Contextual view of RAML versions of API specifications and fragments in API designer from Exchange. 

### Version Note

The Exchange versions have changed from version numbers to date versioning by year and month.

## 2.7

**October 2018**

### New Features

- 
Exchange provides root organization scope search and browse for all assets in a root organization, irrespective of which business groups users belong to. Users are no longer limited to finding assets within their own business group. 
- 
Vanity domain for public portals - Customers can now set their own domain name for their developer portal. This enables a more personalized and consistent branding experience, where you can use your own domain names. This also improves your search engine optimization(SEO) when your customers and users are searching for APIs that are specific to your domain. See [Public Portal Vanity Domain](../../exchange/portal-vanity-domain).
- 
Limits on Custom asset files - Prevents users from uploading malicious file contents as Custom types. See [Create a Custom Asset](../../exchange/to-create-an-asset#create-a-custom-asset).

### Fixed in this Release

- 
(Asset Manager) When recalculating latest version, check if uncompleted versions are considered. (EXC-2749) 
- 
(Asset Reviews) Some ratings table columns have incorrect length. (EXC-2776) 
- 
(Exchange UI) Incorrect asset id placeholder in Exchange Manual Publication. (EXC-2731) 
- 
(Studio 6 and 7) Logout of Exchange shows "Session Expired". (EXC-2774) 
- 
Cannot customize Public portal with images that have names longer than 64 characters. (EXCP-753) 
- 
Customer bearer token is shared with Marketo API while navigating to Exchange. (EXCP-768) 
- 
Empty reply from server uploading large VDP file. (EXC-2748) 
- 
Enable Spec download in public portals for unauthorized users. (EXCP-745) 
- 
Exchange 1 vulnerability. (EXCP-758) 
- 
Exchange asset tile list not rendering well in IE. (EXCP-748) 
- 
Exchange repository is not referenced in API POM files. (EXC-2723) 
- 
Hide save search for public portals. (EXCP-744) 
- 
Mocking service URL is incorrect when baseUri in RAML points to a mocking service instance. (EXCP-774) 
- 
New REST API with invalid RAML shows `The uploaded file does not have a valid RAML format`. (EXC-2759)
- 
Resolution of SE-9079. (EXCP-757) 
- 
Unrestricted upload of dangerous file types in `Creating an asset`. (EXC-2729)

### Version Note

The Exchange versions have changed from the 2.2.x to 2.x versions.

## 2.2.2

**September 2018**

### New Features

- 
REST Connect combines Mule 3 and Mule 4 connectors into one Exchange asset. As a result, all previous Mule 3 and Mule 4 RAML REST API Exchange assets now appear in a single REST API Exchange asset for the RAML specification. For more information, see [Converting a RAML to a Connector Using REST Connect](../../exchange/to-deploy-using-rest-connect).
- 
Categories are available. Search lets you search for Categories. You can set Category values in the Settings menu in the left navigation area. See [To Manage Categories](../../exchange/to-manage-categories).
- 
The Markdown editor supports HTML 5 tags. See the [Markdown Notes](../../exchange/to-describe-an-asset#_markdown_notes).

## 2.2.1

**April 2018**

We are pleased to announce the general availability of the latest release of Anypoint Exchange. This release provides structured and flexible mechanisms to enable precise searching and categorization of assets, content in EU region, and many product improvements.

### New Features

- 
Managed categories to allow Exchange administrators and Organizations owners to create categories and group Exchange assets. 
- 
Exchange contributors can now organize assets into different groups to improve asset browsing and discovery. 
- 
Custom fields allow Exchange administrators and contributors to extend existing asset attributes through the API. 
- 
Ability to reorder pages on asset detail page. 
- 
Public content including Anypoint Connectors, Templates, and Examples is now available in Exchange EU. 

### Fixed in This Release

- 
Add not null constraint to tag_type in asset_manager.asset_tags. (EXCP-505) 
- 
API Console no longer throws XML parsing error while retrieving data. (EXCP-486) 
- 
API Console now handles special characters in resource names. (EXCP-474) 
- 
API Console now shows status code RAML example blocks. (EXCP-407) 
- 
APIs: Client ID no longer changes after updating an application. (EXCP-401) 
- 
APIs: Deleting the last version no longer causes errors in the API Summary page. (EXC-2339) 
- 
APIs: Download as RAML now downloads all versions of an API. (EXCP-453) 
- 
APIs: Exchange Experience API (xAPI) categories are now ordered by displayName. (EXCP-512) 
- 
APIs: Exchange Experience API (xAPI) no longer returns 404 when hard deleting a previously soft deleted asset. (EXC-2329) 
- 
APIs: Exchange now lists whether an API is public or private in the version drop-down menu. (EXCP-297) 
- 
APIs: GET now correctly retrieves configurations from the root organization using an OAuth token from a business group. This allows `GET /organizations/${notAMasterOrgId}/tags/categories/`configurations and returns the configurations from the corresponding root org. (EXCP-507)
- 
APIs: Mocked RAML published to Exchange no longer causes errors. (EXCP-397) 
- 
APIs: PATCH - If fields don’t change, don’t display an error that existing tags use this configuration. (EXCP-528) 
- 
APIs: POST managed tags configuration now returns 409 for a wrong constraint name in the configuration. (EXCP-468) 
- 
APIs: PUT request responses are no longer duplicated. (EXC-2368) 
- 
APIs: RAML v0.8 dependencies now work correctly. (EXC-2213) 
- 
APIs: Safari browser use of the API Console now works correctly. (EXCP-428) 
- 
APIs: SOAP WSDL files opened in Anypoint Studio 7 now work correctly. (EXCP-136) 
- 
APIs: Visibility label in the right side details menu shows whether an API is Private or Public. (EXCP-169) 
- 
Business Groups: Renaming or deleting business groups now works correctly with Exchange. (EXC-2292 and EXC-2325) 
- 
Categories now works correctly for All Types. (EXCP-521) 
- 
Categories UI improvements. (EXCP-532) 
- 
Create Client Application no longer fails when an organization has client management and the user is not an admin. (EXCP-460) 
- 
Creating an Asset - Information menu typos are fixed. (EXCP-143) 
- 
Date now updates after modifying the asset_mappings table in Asset Manager. (EXC-2206) 
- 
Delete: Exchange contributors can now delete draft pages they create. (EXCP-387) 
- 
Exchange logo: Clicking the Exchange logo in top navigation bar now redirects to the Exchange home page. (EXCP-133) 
- 
IE 11 no longer displays a big check mark over a drop-down menu such as in the Settings > Categories > Asset Types menu. (EXCP-523) 
- 
Managed tags by assets feature in the Exchange Experience API (xAPI). 
- 
Managed tags configuration UI service. (EXCP-508) 
- 
Managed tags now look up the tag configurations from the root organization. (EXCP-498) 
- 
Managed tags with list types that already exist had repeating elements. (EXCP-504) 
- 
Marketo secret key no longer displays. (EXCP-461) 
- 
OpenAM: Updating an application no longer creates new OpenAM OAuth client applications. (EXCP-402) 
- 
Pages: Page name input field position appears consistently. (EXCP-239) 
- 
Pages: Page order can now be changed. (EXC-2322) 
- 
PCE audit logs now handle HTTPS correctly. (EXC-2312) 
- 
Portals: Customization navbar now displays published pages only. (EXCP-138) 
- 
Portals: Editor buttons now work correctly in Markdown view. (EXCP-140) 
- 
Portals: Editor icons now display correctly in Firefox. (EXCP-145) 
- 
Portals: Empty display name in a tag configuration no longer throws an error. (EXCP-511) 
- 
Portals: Exchange Portals now correctly renders the HTML image tag in a table. (EXCP-436) 
- 
Portals: Login button now displays correctly in customized Public Portals. (EXCP-127) 
- 
Ratings: Exchange now shows the version of the asset you are reviewing. (EXC-812) 
- 
REST Connect now sends failure email messages to the correct region in which the error occurred. (EXC-2369) 
- 
Search by query now strips out the slash ('/') character in a text search, and indexes search terms for `or`,`and`, and`what`. (EXC-2233)
- 
Version: Add runtime version in asset details. (EXCP-390) 
- 
Version: Exchange now displays the Mule Runtime version so that Anypoint Studio 7 users can choose only Mule 4 assets. (EXCP-130) 

## 2.1.1

**January 2018**

This release introduces an easy way to share searches across Business Group users and personalized saved searches for each Exchange user. We have also made various UI improvements and several bug fixes.

### New Features

- 
Saved search for organizations provides consistent search navigation to all business group users. 
- 
Personalized saved searches enables users to save their own frequently used searches. 
- 
Ability to copy images into the Exchange visual editor eliminates the need to serve images from outside Exchange. 

### Compatibility

Exchange 2.1.1 is compatible with Anypoint Studio version 6.4 and later.

### Fixed in This Release

- 
Add terms and conditions link doesn’t look good on low resolutions. (EXC-1841) 
- 
API Console cannot read property endpointUri of undefined error. (EXC-2190) 
- 
API Notebook doesn’t run in sequence. (EXC-2185) 
- 
API Notebook creating clients when in Markdown doesn’t work. (EXCP-129) 
- 
API Settings is not displaying the instances URLs. (EXC-2127) 
- 
Asset Admin sees the make asset public option. (EXCP-141) 
- 
Asset Manager tsquery operator characters cause a 502 if used in text search. (EXC-1479) 
- 
Asset-Manager the SQL query for the GET by :groupId: and :assetId: endpoint is slow for assets with approximately 27 versions. (EXC-2067) 
- 
Asset-Manager when an asset publication fails, but dependencies were saved, it ends up in an inconsistent state. (EXC-1993) 
- 
Asset-Manager when deleting an asset version, all asset permissions are removed. (EXC-1572) 
- 
Can delete an asset with contracts and instances. (EXCP-308) 
- 
Can’t create a new version of a WSDL. (EXC-2019) 
- 
Can’t delete Asset Version when API version is changed. (EXCP-325) 
- 
Can’t upload WSDLs with other files in the zip. (EXC-1865) 
- 
Change rate to review. (EXC-1847) 
- 
Console behavior of default values for query parameters. (EXCP-139) 
- 
Console error when authorizing for client credentials grant type. (EXCP-231) 
- 
Customization is not sending audit logs. (EXC-2089) 
- 
Customize navigation bar toggle icon. (EXCP-124) 
- 
Delete dialog shouldn’t allow send two DELETE requests to Exchange API. (EXCP-336) 
- 
Delete message doesn’t show dependents. (EXC-2040) 
- 
Dependency Resolver is not properly returning the list of assets that failed to be resolved. (EXC-2248) 
- 
Documentation files are not displaying in the console. (EXCP-123) 
- 
EU - Cannot create asset with files. (EXC-2211) 
- 
Exchange editor generates garbage characters if the text is enclosed in angle brackets. (EXCP-125) 
- 
Fix multi-line logs seen in Sumologic. (EXC-2234) 
- 
Go to existing application is not working. (EXC-2016) 
- 
GraphAPI - Getting only the last public version retrieves several assets. (EXC-2117) 
- 
Handle deleted user scenario. (EXC-2048) 
- 
IE-11 - Add image or link popup shows "undefined". (EXCP-128) 
- 
Knex throws error obtaining connections from pool in Asset Reviews Service. (EXC-2147) 
- 
Maven Facade returns some 403 from Asset Manager as 502 errors. (EXC-1576) 
- 
Maven Facade - 403 errors are always turned into 404. (EXC-1598) 
- 
Mocking Service is not working if baseURI has the old mocking service. (EXCP-331) 
- 
Optimize RAML parsing for API console. (EXCP-134) 
- 
Portal trying to load deleted API version. (EXC-2201) 
- 
Private instance is displayed in API Summary on public portal. (EXCP-335) 
- 
Query parameter limit with value 250 is ignored when retrieving applications from APIM. (EXCP-132) 
- 
RAML is downloaded twice to render API Console. (EXCP-313) 
- 
RAML Parser Error: Unable to parse RAML data. (EXCP-309) 
- 
RAML request panel shows incorrect URI parameter field. (EXCP-323) 
- 
Rating score is not recalculated when older version’s rating changes. (EXCP-137) 
- 
Request API Access Modal window looks weird in IE11. (EXCP-142) 
- 
Studio 7 examples import not working. (EXC-2225) 
- 
Update Tooltip in manual publication typo and new asset type. (EXC-1206) 
- 
Users with permissions across organizations are failing to authorize. (EXC-1610) 
- 
View mode changes when you select a saved search. (EXCP-384) 
- 
Visibility status is not refreshed after making an API public. (EXCP-333) 
- 
When Publishing to Exchange via Maven, if publication fails with Forbidden, an incorrect entry is created in the database. (EXC-1935) 
- 
when token expires before smart connector generation finishes, then the error can’t be sent. (EXC-1528) 

## 2.1.0

**November 2017**

We are pleased to announce the general availability of the latest release of Anypoint Exchange. This release enables Anypoint Platform users to publish and share APIs with developers inside and outside of their organizations.

### New Features

- 
Unification of Anypoint Exchange and API portals. Now all assets can be managed and shared through a single location. 
- 
Ability to create public portals for any APIs in Anypoint Exchange. 
- 
Rich documentation automatically generated for RAML or OAS specifications. 
- 
Interactive API use case validation through API Notebook. 
- 
Mocking service, which can be used to test API calls without implementing the API. 
- 
Ability to register clients and request access for APIs managed by Anypoint Platform. 
- 
Automatic indexing of API instances and endpoints via Exchange. 
- 
Sharing of APIs externally using Exchange portal. 
- 
Customization and branding features of Exchange portal. 
- 
HTML support for content inserted to a Markdown editor (limitations apply). 

### Compatibility

Exchange 2.1.0 is compatible with Anypoint Studio version 6.4 and later.

### Known Issues

- 
EXC-2191: Unable to use API notebook button in the WYSIWYG mode. Click on the editor window first, and then press the Notebook button. 
- 
EXC-2188: API notebook creators are not able to specify the API endpoint when configuring a client. Update RAML base URI to update the endpoint used by API Notebook. 
- 
EXC-1510: My application page is not responsive. 

## 2.0.0

**July 29, 2017**

We are pleased to announce the general availability of the latest release of Anypoint Exchange. This product enables Anypoint Platform users to publish and access Mule-related content within their own organization increasing visibility and reuse.

### Compatibility

Exchange 2.0.0 is compatible with Anypoint Studio version 6.3 and later.

The new Anypoint Exchange 2 in Anypoint Platform offers a complete rework of Exchange with support for OAS and RAML 1.0 specifications, an improved user interface, a new editor supporting both Visual and Markdown text creation, and the ability to rate assets.

### New Features

Anypoint Exchange lets you:

- 
Store all integration assets in one place in Exchange, such as best practices, integration patterns, API fragments, API specifications, examples, templates, and connectors. 
- 
Enrich portal content using the Visual editor and Markdown editor. 
- 
Quickly upload Open API specifications (Swagger) in Exchange which automatically converts to RAML for use across the Anypoint toolset. 
- 
Quickly upload WSDLs (SOAP APIs) in Exchange. 
- 
Consume and reuse all existing MuleSoft public content in Anypoint Studio and Design Center. 
- 
Collaborate with API owners and designers including the ability to comment and write reviews, ask questions, and provide feedback on each asset. 
- 
Share an asset within a business group with users outside of the business group to drive cross business organization collaboration. 
- 
Auto-generate a Mule 4.0 Design Center connector (using REST Connect) for any valid API specification for use within Design Center. 
- 
View a list of dependencies (API Fragments) for any API specification. 
- 
Version any asset published to Exchange. 
- 
View Dependency Snippet for connectors for use in Maven, Gradle, SBT, and Ivy. 
- 
Publish examples and templates using Studio 6.3 and later. 

### Migration

Exchange 1.7 is still accessible and will remain available for 90 days (as of July 29). None of the content on this old version of Exchange has been deleted. The URL for old Exchange is now [https://anypoint.mulesoft.com/exchange1/](https://anypoint.mulesoft.com/exchange1/). Existing customers with content on Private Exchange can also access the old Exchange using a link available on the Exchange 2.0 site. You can migrate the content to Exchange 2.0 using [migration instructions](../../exchange/migrate).

### Known Issues and Limitations

- 
EXC-1140: Unable to type anything below an image in the Visual editor. Switch to Markdown editor to continue editing. 
- 
EXC-1253: Visual editor is not supported for use with Internet Explorer 11. Use the Markdown editor instead. 
- 
Searching by tag at the user interface only works for the latest asset version. 
- 
Admin user cannot delete reviews created by other users. 
- 
Rating is not refreshed when a version is deleted. 
- 
Unable to deprecate an asset. 
- 
EXC-1522: Incorrect error message when a user without Exchange Contributor permission within a Business Group tries to create an asset. 
- 
EXC-1269: In Firefox, when a token is expired and user tries to publish to exchange, it throws a 403 error page. Clear cookies for Anypoint Platform and try again. 

## 1.7.1 Private Cloud Edition

**October 2016**

This release provides new features and bug fixes for the Anypoint Exchange on-premises release.

### Features

These feature changes occurred between the previous Anypoint Exchange On-Premises version 1.4.1 (May 2015) and the current release:

- 
Content ratings 
- 
Objects can now have the author’s name and photo 
- 
SOAP API (WSDL) support 
- 
Item type colors 
- 
Auto populating URI for new items 
- 
Auto resizing description container for editing 
- 
Access Management Organization ID 
- 
Business groups 
- 
Artifact states 
- 
Transition flows 
- 
Exchange roles 
- 
Private Exchange connectors can be installed in Studio 
- 
Audit log of all actions in a private Exchange 
- 
The RAMLs label was changed to REST APIs 
- 
The WSDLs label was changed to SOAP APIs 
- 
Requires Studio 4.2.0 and newer 

### Changed Features

The following features changed between versions 1.4.1 and 1.7.1:

- 
Removed video caption field until a video URL is added. 
- 
Removed `/mulesoft`from a path.
- 
Removed object amount limitation for private Exchanges. 
- 
Removed editing types within an organization. 
- 
Editing terms are now only available to Admin roles. 

### Current Differences with the Cloud Version

At the time of this release, the Anypoint Exchange cloud version is at 1.7.0. The only changes in the on-premises beta are the new REST APIs and SOAP APIs labels.

### Known Issues

None.

## 1.7.1

**September 2016**

This version of Anypoint Exchange fixes internal issues and provides these two updates:

- 
The **RAMLs**label is changed to**REST APIs**
- 
The **WSDLs**label is changed to**SOAP APIs**

## 1.7.0

**July 2016**

This version of Anypoint Exchange provides new features and fixes.

### Features

- 
Connectors linked to from a private Exchange can now be installed in Anypoint Studio. 
- 
Audit Logs now provide Exchange Administrators with a log of all actions that occur in a private Exchange. 

### Fixed Issues

| Issue | Description | 
|---|---|
| EXCHANGE-1126 | Scope drop-down now shows the Business Group Hierarchy on search and in publish/republish drop-down. | 
| EXCHANGE-1125 | Fix a bug on missing buttons when editing versions. | 
| EXCHANGE-1115 | Improve error messages and avoid data lost during validations. | 
| EXCHANGE-1099 | Scope drop-down now shows the Business Group Hierarchy on search and in publish/republish drop-down. | 
| EXCHANGE-1073 | Fix a bug showing the version header without data and saving an empty version. | 
| EXCHANGE-1072 | Changes the place of back to the list button. | 
| EXCHANGE-1063 | Fix the item and name inputs on IE when Create/Clone Artifact. | 
| EXCHANGE-1006 | Improve error messages and avoid data lost during validations. | 
| EXCHANGE-872 | Fix a bug showing the version header without data and saving an empty version. | 
| EXCHANGE-809 | Disables the video caption field until you add a video URL. | 
| EXCHANGE-779 | Add a  | 
| EXCHANGE-778 | Ad a  | 

## 1.6.2

**June 2016**

This version of Anypoint Exchange provides bug fixes and improvements.

### Fixed Issues

| Issue | Description | 
|---|---|
| EXCHANGE-869 | Hide non-relevant calls to actions in Exchange UI when the user launches it from Studio | 
| EXCHANGE-1038 | Download and docs icons should match the 2.2.1 MuleSoft styles | 
| EXCHANGE-1096 | Fix issue with removing filter terms (tags) from search results when the tag filter is launched from the item detail page | 
| EXCHANGE-1106 | All link versions wrongly point to only to the first version of the artifact | 
| EXCHANGE-1112 | User needs to update page to see the download icon when adding versions on an artifact | 

### Improvements

| Issue | Description | 
|---|---|
| EXCHANGE-553 | Simplify the artifact’s share URL by removing "/mulesoft" from the path | 
| EXCHANGE-1086 | MuleSoft tag should not be displayed for anonymous users | 
| EXCHANGE-1087 | The focus should return to the beginning of the list when the user returns to search results from the detail page | 
| EXCHANGE-1088 | Remove Exchange settings from Anypoint Platform Access Management | 
| EXCHANGE-1094 | Instead of displaying the main organization name, display "Master Organization" in the Publish/Republish dropdown | 
| EXCHANGE-1104 | Refactor how pre-defined search terms are treated in the backend to improve performance | 

## May 2016

This new version of Anypoint Exchange includes new features & functionality for addressing the viewing and publishing of artifacts across a hierarchical organization structure. Also within this version of Exchange aligns with the Anypoint Platform Styles and use of the new Nav Bar.

### Features and Functionality

The following sections describe the new features in this release.

#### Visual Enhancements

Alignment with the Anypoint Platforms Styles and Integration with the latest Anypoint Platform Navigation Bar.

#### Roles for Exchange

Besides the existing Organization Owner, Contributor and Administrator Roles, a separate Viewer role was created.

#### New State and Flow Transition of an Artifact

To address the movement of an artifact across a hierarchical structure, Exchange now provides new states for an artifact and also specific actions to be performed on them.

#### Business Groups

Business Groups are being incorporated in Exchange . This feature across with the Exchange Roles and the new state transition flow of an artifact provides:

- 
Ability of Central IT (maybe the root organization) to create artifacts and make them available to all Lines of Businesses (business groups) 
- 
Ability of Central IT to locate artifacts published in a business group and make it available to the rest of the business 
- 
Ability of an LOB to publish artifacts for internal (to that business group) consumption 

#### UI and UX Improvements

New Filters and actions now support the new Business Groups, Artifacts States, and Transition Flows functionalities.

#### Edit Types Removal

Edit Terms only available on root Organization for Admin and Owner Organization

#### API Changes

Before this release, Exchange used an internal Organization ID in the API resource, but this organization ID is replaced with the Access Management Organization ID to allow Business Groups. New endpoints are being incorporated in Exchange to work with Business Groups. New permissions are applied using the Business Groups hierarchy.

#### Avoid Losing User Data

When a session expires, Exchange prompts for credentials and completes the action. Exchange now displays a warning when a user tries to leave the edit page if there are unsaved changes.

### Removed Features

- 
The object amount limitation for private tenants has been removed. The possibility to request to increase the object amount limit it’s already removed from the Exchange configuration in Anypoint Platform access management. 
- 
The possibility to edit types was removed, all organizations now share the same types. 
- 
The feature to edit terms can now only be enabled for users with Admin roles in root organizations. 

### Architecture Changes

- 
Split UI from backend in different servers and all the related changes to fulfill this Architecture change. 
- 
Update Node.js version to v4. 

## Dec 2015

### Features and Functionality

This Anypoint Exchange release includes the following new features and functionality:

- 
WSDL Support: At the moment WSDL type does not have a Studio integration, however WSDLs can be added and managed via web UI. 
- 
Visual enhancements such as new colors for item types and UX improvements. 
- 
Auto-populated URI when creating new items. 
- 
Automatically resizable description container when editing content. 
- 
Firefox and Internet Explore 11 bugs fixed. 

### Dec 2015 Known Limitations

The version of the exchange available with the on-premises installation of the Anypoint Platform comes with an empty library of content, you must populate it with your own content.

## May 2015

### Features and Functionality

This Anypoint Exchange release includes the following new features and functionality:

- 
Ratings: All content has a rating associated to it. Users can rate only from Exchange in Anypoint Studio (Connectors need to be installed in Studio in order to rate them). Objects have their rating displayed only when they have two ratings or more. 
- 
Author: Objects can have the author’s name and photo. This can be used for partners or community contributors. This section is hidden if not filled out. 
- 
UI Refresh: Object type indicators have been improved . Text areas and button sizes have changed to improve readability 

### Known Limitations

To access private content from Anypoint Studio, version 4.2.0 or newer must be used.

## May 2015 Private Cloud Edition

Version: 1.4.1

This Anypoint Exchange release includes these new features and functionality:

- 
Create and publish private content: Choose between a variety of content types (templates, examples, connectors, and more) to add, describe your asset, and publish it in your organization’s exchange. Only the people you choose may have access to create and publish new content. 
- 
Search for content: Users within your organization can find the internally published content (as well as MuleSoft’s public content), increasing reuse and avoiding redundant work. Exchange Admins can customize search filters to make internal content easier to find. 

### Known Issues

Accessing private content from Anypoint Studio requires version 4.2.0 or newer.

## February 2015

### Features and Functionality

This Anypoint Exchange release includes the following new features and functionality:

- 
Create and Publish private content: Choose between a variety of content types (templates, examples, connectors, etc) to add, describe your asset and publish it in your organization’s exchange. Only the people you choose may have access to create and publish new content. 
- 
Search for Content: Users within your organization can find the internally published content (as well as MuleSoft’s public content), increasing the chance of reuse and avoiding redundant work. Exchange Admins can customize search filters to make internal content easier to find. 
- 
Seamless Anypoint Studio Integration: Access your private content seamlessly from Anypoint Studio. You can open templates or install connectors by opening Anypoint Exchange from Studio and logging into your Anypoint Platform account. 

### Known Limitations

To access private content from Anypoint Studio, version 4.2.0 or newer must be used.

## Support

If you need help using the product, refer to the documentation for the [Anypoint Exchange](../../exchange/). If you have additional questions or want to report a problem, Contact MuleSoft.

## See Also

- 
[Anypoint Exchange](https://www.anypoint.mulesoft.com/exchange/)
- 
[MuleSoft Trailblazer Community](https://trailhead.salesforce.com/trailblazer-community/neighborhoods/mulesoft)
- 
[Salesforce Help](https://help.salesforce.com)