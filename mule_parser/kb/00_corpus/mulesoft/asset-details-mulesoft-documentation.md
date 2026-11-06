# Asset Details | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/asset-details](https://docs.mulesoft.com/exchange/asset-details)

---

![The asset details of the Exchange XAPI](_images/exchange-asset-detail-view.png) 

# Asset Details

The asset details page provides comprehensive information about an asset. You can view version-agnostic information, share the asset with others, publish it on the public portal, and download a copy of the asset. You can also view code, manage versions and lifecycle states, add categories and tags, generate and edit asset documentation, and test API endpoints.

See [Workflow: Publish Assets](workflow-sharing-assets) for more information about performing these functions.

Select an asset in Exchange to view the asset details page:

![The asset details of the Exchange XAPI](_images/exchange-asset-detail-view.png) 

The navigation bar lists:

- 
Additional pages 
- 
Saved search terms 
- 
Application names 
- 
Instances 
- 
The HTTP functions in the REST specification (for a REST API) 
- 
Conformance Status 
- 
Agents show card details 
- 
Brokers show access list and card details 
- 
MCP servers show details and tools 
- 
Terms and conditions and APIs using this policy (for a policy) 
- 
Settings 

The asset detail page provides this information:

- 
Asset name 
- 
Description 
- 
Asset type 
- 
Broker show as asset subtype 
- 
Agents show protocol 
- 
Organization 
- 
Contact name 
- 
Contact email 
- 
Asset creation date 
- 
Last updated date 
- 
Version 
- 
Categories and tags of the asset 
- 
Lifecycle state 
- 
Managed and unmanaged instances and includes whether agent instances are verified via GoDaddy Agent Naming Service (ANS) 
- 
Share by inviting users to have access 
- 
Conformance state 
- 
APIs show download specifications and view code 
- 
Add a new version 

These actions trigger an update to the last updated date on the asset details page:

- 
Create a new asset 
- 
Create a new asset version 
- 
Update any version agnostic property: - 
Name 
- 
Description 
- 
Icon 
- 
Contact name 
- 
Contact email 
 
- 

For REST APIs, use the API console to create example calls and mock data to test the API. For more information, see [Simulating Data in REST APIs](ex2-to-simulate-api-data).

For GraphQL APIs, use the GraphQL console to view GraphQL schemas and write and run queries. For more information, see [Viewing GraphQL API Schemas and Run Queries](view-graphql-api-schemas-and-run-queries).

From the asset details page, you can collapse and expand metadata such as version, last published, and categories and tags. See version information by clicking **View versions**. Administrators can use **Manage versions** to add a new version of the asset, view version details, and delete a version. See [Manage Versions](manage-versions) for more information.

The documentation page displays the asset documentation. An administrator or asset owner can edit documentation by clicking **Edit documentation** from the asset details page. You can generate documentation for REST APIs without documentation by clicking **Generate documentation**. For more information, see [Generating API Documentation with Generative AI](generating-documentation-with-ai).

![Asset details page showing the Edit documentation and the Generate documentation buttons](_images/ex-generate-doc.png)


## View REST API Elements in an Asset

View RAML, OAS, or AsyncAPI API specification information, including resources and the methods in each resource, in the left navigation bar.

- 
Click a method button: ![An API spec showing method resources](_images/ex2-rest-ftns.png)  
- 
Experiment with the API in the right side of a method view. This is similar to using a program such as Postman to specify custom HTTP headers and test each API’s method using the API’s endpoint. 
- 
To connect the API to one of your applications and use the API to send and receive data, click **Request access**.

## Search API Specification and Pages

The assets details page enables you to find specific information within the pages and API specification of an asset using the CTRL+F or the command+F keyboard shortcut. In Exchange, this enhanced shortcut overrides the native browser shortcut, which only searches for words and phrases on the current page. To quickly find the information you need, use this enhanced shortcut to search the content of every page and the API specification of an asset.

To search pages and the API specification using the enhanced find shortcut:

- 
In the asset details page, press CTRL+F or Command+F. 
- 
In the **Search content**box, enter a search term or phrase.
- 
Click a search result from the list. 
- 
Use the arrows to move through all the occurrences of the search term within the search results. 
- 
Click the **X**to close the Search content box.

The enhanced keyboard shortcut looks for terms or phrases in:

- 
Pages - 
Home 
- 
Additional pages 
 
- 
- 
Specification - 
Summary 
- 
Endpoints 
- 
Documentation 
- 
Types 
- 
Security 
 
- 

When you enter a search term or phrase in the search box, the search results box displays the sections within Pages and Specification that contain the search terms entered. Click the search result to open the page with the search term or phrase highlighted. The search result shows the number of search-term matches in each page. Use the arrows to move up or down in the list of search results and to the next page.

For example, enter the term `ruleset` in the **Search content** box. From Pages, there are three search results for ruleset in the Home page. Click **Home** to open the page. Use the arrows to find all of the highlighted instances of ruleset in the Home page.

![Search results for the term ruleset highlighted in the documentation](_images/ex-search-spec-and-pages.png) 

## View Instances

View the instances of APIs and other assets in the **Instances** list on the asset details page. Instances are managed or unmanaged (non-managed). Managed instances are managed in API Manager. For example, when you register an API in API Manager, it creates a managed instance. This instance is linked to a specific runtime (like Mule Gateway or Omni Gateway). Its environments (sandbox and production) appear automatically in the **Instances** list. The list includes the instance name, version, environment, URL, visibility, and whether an agent instance is verified via GoDaddy Agent Naming Service (ANS).

Unmanaged (external) instances run outside Anypoint Platform. These instances are primarily for discovery—helping your team find all APIs in one catalog even if they aren’t governed in API Manager.

Instances for brokers are created in YAML in Anypoint Code Builder. After the agent network project is published to Exchange, the instances appear in the **Instances** list.

To view instances:

- 
Select an asset in Exchange. 
- 
In the navigation bar, select **Instances**.
- 
The **Instances**list displays the instances of the asset.

## View Conformance Status

You can view governance conformance status in Exchange for versions of API specifications. The status is one of the following:

- 
**Conformant**: The API specification is conformant to governance rulesets against which it has been validated.
- 
**Not Conformant**: The API specification is not conformant to governance rulesets against which it has been validated.
- 
**Not Validated**: The API specification is not validated against governance rulesets.

Conformance status can be viewed in Exchange as follows:

- 
A conformance badge is displayed for a selected version of an API. 
- 
In the **Manage Versions**page, a**Conformance**column shows conformance status for each version of the API.
- 
A **Conformance Status**page appears for all REST APIs and AsyncAPIs. If a selected version of an API has been validated against governance rulesets, the conformance status page gives conformance information and gives options to fix nonconformant versions. The Conformance Status page also shows the filter criteria that resulted in the API being validated against the listed rulesets.

To view conformance status:

- 
Select an API asset that is of a type supported by Anypoint API Governance. 
- 
Review the conformance badge. 
- 
To view conformance by version, click **Manage Versions**.Review the **Conformance**column, which shows the governance conformance status for each version.
- 
To view conformance details, select **Conformance Status**in the navigation bar. From the conformance status page, you can:- 
Select the version of the API that you want to view. 
- 
For validated APIs, view the lists of centralized governance rulesets and additional rulesets against which the APIs have been validated. - 
If there are more rulesets than are shown on the initial page, click the **Show All**link to show the full list.
- 
Click the external link icon for a ruleset to view that ruleset’s page in Exchange. 
 
- 
- 
For nonconformant APIs, click one of the following: - 
**Fix in Design Center**After your API specification opens in Design Center, add the listed rulesets as dependencies and view the conformance messages in the **Project Errors**section to fix and republish your API specification.
 If the asset is published directly on Exchange without an existing version in the Design Center, a read-only version of the project opens. To fix conformance issues,[download the asset from Exchange](to-download-an-asset), then[import it to Design Center](../design-center/design-create-publish-api-specs-from-file), and[publish it to Exchange](../design-center/design-publish)with the same ID and a new minor version.
- 
**See instructions for Anypoint CLI**Follow the instructions on the page to copy, update, and run the Anypoint CLI commands to add the listed rulesets as dependencies and fix and republish your API specification. 
 
- 
 
- 

## View Governed APIs for a Ruleset

In a ruleset’s **Governed APIs** page, you can view the list of centrally-governed APIs to which the ruleset applies.

Developers can use the **Governed APIs** list as follows to help improve the quality of the rulesets and APIs that they develop:

- 
When their APIs fail a ruleset, they can see which other APIs successfully conform to the ruleset so that they can fix their APIs. 
- 
When they search for available rulesets to use for their API, they can see which APIs are conformant to a specific ruleset to evaluate how helpful the ruleset is. 

API consumers can use the **Governed APIs** list when they need to create an API service or application that is conformant to a certain set of standards or rules. They can:

- 
Ensure there is a ruleset in Exchange that has the rules they need. 
- 
See which APIs pass the rules for a ruleset so that they can ensure their application is consuming only the conformant APIs. 

Depending on the access you have to the APIs in Exchange, you might see only the APIs that are conformant to the ruleset. This ensures that vulnerabilities are not exposed to consumers who do not have proper access to the APIs. Organization administrators and contributors can see the conformant and non-conformant APIs for their organization.

To view the governed API list for a ruleset:

- 
Select a ruleset asset that is used in an API Governance profile. 
- 
Select **Governed APIs**in the navigation bar to see whether each listed API version passes all the rules in the ruleset.
- 
Select from the filter menus to refine the list of APIs. Default settings are: - 
All APIs 
- 
Your root organization 
- 
Any Ruleset Status 
 
- 
- 
To view an API’s **Conformance Status**details, click the open external link icon (![open external link icon](_images/open-external-link-icon.png) ). ).