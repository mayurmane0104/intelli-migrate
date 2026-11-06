# Anypoint API Experience Hub Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/api-experience-hub/api-experience-hub-release-notes](https://docs.mulesoft.com/release-notes/api-experience-hub/api-experience-hub-release-notes)

---

- 
EU: January 8, 2026 
- 
US: January 9, 2026 

# Anypoint API Experience Hub Release Notes

| Starting October 2024, API Experience Hub enables testing managed package upgrades in sandbox environments before production. | 

The following table lists the release schedule for the API and UI, and the managed package. The API and UI release contains service updates affecting Anypoint APIs or the UI. The managed package includes updates to the components and data objects that interact with your Anypoint Platform organization. The API and UI release for EU occurs a day before the US release. The managed package is pushed to sandbox instances for testing for at least eight days before it’s pushed to production environments. If a service release or upgrade fails, customers receive an alert and another release or upgrade is manually pushed the next day.

The latest version of the API Experience Hub managed package is used when API portals are created during the new connection process.

| Release | Version | Managed Package Sandbox Push-Upgrade | API/UI Production Services Release | Managed Package Production Push-Upgrade | 
|---|---|---|---|---|
| January 2026 | No new version of the managed package | No new version of the managed package | ||
| 2.40.0 | January 27, 2026 | No update | January 31, 2026 | |
| May 2026 | 2.46.0 | May 8, 2026 | No update | May 11, 2026 | 
| 2.48.0 | May 21, 2026 | 
 | May 26, 2026 | 

## May 2026

### What’s New

- 
Apollo support is now available for GraphQL services in the managed package. This enhancement improves GraphQL API integration and compatibility for portal users leveraging Apollo-based clients. 
- 
Portal administrators can now customize labels for newly introduced asset types, including agentic assets such as MCPs, agents, and LLMs, through the portal builder. 
- 
You can now publish agents, LLMs, MCP servers, GraphQL, and gRPC services to your portal alongside existing API types. The **Catalog management**page (formerly**API management**) and the**APIs**page surface all supported service types in a unified catalog.For more information, see: 
- 
All portals now scale to 7,000 assets by default. Opting in is no longer required. For more information, see [Limitations](../../api-experience-hub/limitations).
- 
For portals configured before LLM support was available, Administrators can now add a page variation to show the **API Console**on the**Service Details**page for LLM services.For more information, see [Add Page Variation to Show the API Console for LLMs](../../api-experience-hub/common-builder-customizations#add-page-variation-to-show-the-api-console-for-llms).

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| The request panel now works correctly when proxy mocking is enabled. | W-22282240 | 
| Consumer asset search requests now correctly route through ProjectView for organizations with ProjectView enabled. | W-22247758 | 
| The Summary page method badges now display at the correct size with proper styling. | W-22300166 | 
| Summary page links now function correctly when Lightning Web Security (LWS) is disabled. | W-22300570 | 
| The endpoint documentation page no longer shows bottom navigation links. | W-22300139 | 

## January 2026

### What’s New

- 
When configuring Single Sign-On (SSO) for your portal, you can now enable multi-valued SAML attributes to send multiple groups in the groups claim. Sending groups as a comma-separated list is no longer required. For more information, see [Create and Configure an Application for Okta SAML and Microsoft Entra ID SAML](../../api-experience-hub/configuring-sso#step-1-enable-sso-for-your-portal).
- 
The maximum limit of user groups is now increased from 20 to 100. For more information, see [Limitations](../../api-experience-hub/limitations).

## November 2025

### What’s New

- 
Administrators can now enable portal scalability to increase API capacity to 7,000. Portals previously opted in and all new portals scale to 7,000 APIs. For more information, see [Opt In to Increase the Number of APIs In the Portal](../../api-experience-hub/managing-apis#opt-in-to-increase-the-number-of-apis-in-the-portal).
- 
API management now optimizes scrolling to support 7,000 APIs. 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| In the API Console, Boolean query parameters set to  | W-19881903 | 

## June 2025

### What’s New

- 
Admins can now enable Salesforce users to access a portal. For more information, see: 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| In the API Console, the Python requests examples from RAML files now display correctly. | W-1853152 | 
| The create connections endpoint is upgraded to make the connection more secure. | W-18717718 | 

## May 2025

### What’s New

- 
This product is now available on Hyperforce. Anypoint Platform instances on the Hyperforce infrastructure are: - 
[Canada Cloud](https://ca1.platform.mulesoft.com)
- 
[Japan Cloud](https://jp1.platform.mulesoft.com)
 
- 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| In the API Console, specs with multipart requests now work as expected. | W-18328020 | 
| An issue with loading assets in the API carousel component is now resolved. | W-18380623 | 

## April 2025

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| In the API Console, the multipart payload components now work as expected. | W-17986234 and W-17936498 | 
| The search component is now updated to prevent search failures. | W-18015093 and W-18088742 | 
| The UI in Anypoint Platform is now updated to prevent potential disruptions. | W-18121291 | 
| The search results are now sorted by relevance to the search term. | W-17898526 | 
| Tool tips now show as expected when scrolling. | W-17898560 | 

## March 2025

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| In the API Console, the multipart form data is now working as expected when Lightning Web Security (LWS) is enabled in the Salesforce organization. | W-17349235 | 
| In the API Console, copying a response to the clipboard is now working as expected when LWS is enabled in the Salesforce organization. | W-17369541 | 
| In the API Console, the API specs for some endpoints now show as expected. | W-17351714 | 
| In the API Console, examples of  | W-17413312 | 
| In the API Console, API type documentation now shows inherited properties when LWS is enabled in the Salesforce organization. | W-17883236 | 

## February 2025

### What’s New

- 
Administrators can now enable portal scalability to increase the maximum number of APIs available in the portal to 1,000. For API portals created before this release, administrators must opt in. New portals automatically scale to 1,000 APIs. For more information, see [Opt In to Increase the Number of APIs In the Portal](../../api-experience-hub/managing-apis#opt-in-to-increase-the-number-of-apis-in-the-portal).
- 
You can now refine search results by filtering APIs by tags and categories. For more information, see: 

## January 2025

### What’s New

- 
The documentation now includes instructions for configuring Single Sign-On (SSO) using Microsoft Entra ID for Security Assertion Markup Language (SAML). For more information, see [Enable SSO for Your Portal](../../api-experience-hub/configuring-sso#step-1-enable-sso-for-your-portal.adoc).

## October 2024

### What’s New

- 
You can now create and manage groups of users who can see specific APIs in your portal. For more information, see [Manage User Groups](../../api-experience-hub/managing-users#manage-user-groups).
- 
A new rate-limiting service now protects against potential distributed denial-of-service (DDoS) attacks. 
- 
API Console is now updated to 0.3.2. 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| The Builder can now access the current asset library of uploaded images. | W-13514487 | 
| When Lightning Web Security (LWS) is disabled, the codemirror bundle now loads as expected. | W-16723030 | 
| In the API Console, code examples now update when navigating between endpoints. | W-16723085 | 

For additional known issue information about this product, see [Known Issues](https://help.salesforce.com/s/issues).

## August 2024

### What’s New

- 
You can now assign a user the API Experience Hub Users Approver granular permission to approve or reject pending registration requests and enable or disable member users only. For more information, see: 
- 
This release contains accessibility improvements, including alternative text for images, more contrast for components, images, and text, and visible and persistent labels. 
- 
API Console is now updated to 0.3.1. 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| The API Console no longer loops when the Lightning Web Security component is disabled. | W-16251757 | 

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder can’t access the current asset library of uploaded images. | See  | W-13514487 | 
| In the API Console, the following known issues occur using authentication credentials: 
 | W-15184114 | 

## July 2024

### What’s New

- 
You can now manage separate deployment environments for your API portal. You can connect to multiple Salesforce sandbox organizations and switch between them. Manage Salesforce organizations from the **Manage your API portal**page by selecting sandbox environments that are available in the current Salesforce connection.For more information, see [Working With Sandboxes](../../api-experience-hub/working-with-sandboxes)
- 
You can now view AsyncAPI 2.6 specifications to discover and reuse within your organization. To learn about the AsyncAPI journey, see [AsyncAPI Support to Implement Event-Driven Architecture](../platform/event-driven-api).
- 
This product has a refreshed UI. This new UI brings the product visually closer to the [new visual style of Salesforce](https://www.salesforce.com/blog/salesforce-cosmos-slds-2/)and enhances consistency, accessibility, and the user experience.Changes include a refreshed navigation, icons, and colors. 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| In the API Console, examples display correctly when expanded in the  | W-14559605 | 
| In the API Console, the  | W-14560535 | 
| The color of the API Catalog description now displays correctly. | W-13570863 | 

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder can’t access the current asset library of uploaded images. | See  | W-13514487 | 
| In the API Console, the following known issues occur using authentication credentials: 
 | W-15184114 | 

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder can’t access the current asset library of uploaded images. | See  | W-13514487 | 
| In the API Console, the following known issues occur using authentication credentials: 
 | W-15184114 | 

## June 2024

### What’s New

- 
You can now add Chatter Feed tracking to engage with your portal community. For more information, see: 
- 
You can now add Google Analytics to gain valuable insights into how consumers are using your APIs and portal. For more information, see [Configuring User Analytics](../../api-experience-hub/configuring-user-analytics)
- 
The API Console now has expand and collapse buttons on the **Try It**and navigation panel.
- 
The registration handler used in configuring single sign-on now includes default values for SAML attributes and OpenID Connect default claims for most common identity providers in `AttributeExtractor`for the following fields:- 
First Name 
- 
Last Name 
- 
Email 
- 
Username 
 
- 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| The search results no longer return duplicate APIs. | W-15665689 | 

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder can’t access the current asset library of uploaded images. | See  | W-13514487 | 
| In the API Console, the following known issues occur using authentication credentials: 
 | W-15184114 | 

## May 2024

### What’s New

- 
The maximum number of APIs in a portal is increased to 350. 

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 
| In the API Console, the following known issues occur using authentication credentials: 
 | W-15184114 | 

## April 2024

### What’s New

- 
You can now test APIs using authorization credentials in the API console. 

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 
| In the API Console, the following known issues occur using authentication credentials: 
 | W-15184114 | 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| The registration handler no longer causes errors for single sign-on. | W-15203518 | 
| An error no longer occurs when loading the asset documentation. | W-15007406 | 
| The process of removing an API from the portal when the API does not exist in Exchange no longer fails. | W-15108878 | 
| The redirection of the self-registration component is now working as expected. | W-15244602 | 

## March 2024

### What’s New

- 
A Salesforce user with the System Administrator profile can now create an AEH_Anypoint permission set to configure only the minimum required permissions for the user who connects to Salesforce to link the Salesforce organization and Anypoint Platform organization. For more information, see [Assigning Permissions](../../api-experience-hub/assigning-permissions)
- 
The Experience Builder now has customizable properties for the following API Experience Hub Lightning components: - 
Asset Detail Header You can select properties to show the **Request access**button and lifecycle state in the**API Detail**page.
- 
API Console You can now select the property to show the endpoints expanded. For more information, see [API Experience Hub Lightning Components](../../api-experience-hub/api-experience-hub-lightning-components).
 
- 

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| Request access now works as expected when the  | W-15007911 | 
| In the API Console, the filter text no longer overlaps in the  | W-13803914 | 
| When editing an SLA contract tier, the current SLA tier no longer displays as an option. | W-13803915 | 

## January 2024

### What’s New

- 
The Experience Builder now has customizable properties for the following API Experience Hub Lightning components: - 
API Carousel The title, subtitle, and the number of cards displayed in the API Carousel can now be changed. 
- 
Asset Detail Header You can select which properties to show in the API Details page. For more information, see [API Experience Hub Lightning Components](../../api-experience-hub/api-experience-hub-lightning-components).
 
- 
- 
The **Application details**page now shows the instance URL of an API. For more information, see[My Applications](../../api-experience-hub/my-applications).
- 
The **API details**page now shows the tags and categories of an API. For more information, see[Viewing Service Details](../../api-experience-hub/viewing-api-details).
- 
The API Console now enables you to test an API using an instance URL. For more information, see [Testing APIs Using an API Instance](../../api-experience-hub/testing-apis-using-an-api-instance).
- 
Guest users are now prompted to log in or register when they request access to an API. 

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| The  | W-14610136 | 
| The diagnostic tooling UI is now improved. | W-14610428 | 
| The revoked status is now showing for API instances in the  | W-14580099 | 
| The search component for the API Catalog, search box, and applications now shows a message when more than 100 characters are entered. | W-13803905 | 
| The API Console has updated UI styling. | W-14782945 | 
| The API Console now displays the same order of payload examples as other Anypoint Platform products. | W-14651333 | 
| In the API Console, aborting a request is now working properly. | W-1450620 | 

## December 2023

### What’s New

- 
Administrators and security teams can now implement an external identity provider (IdP) as a login option for an API Experience Hub portal. Single sign-on (SSO) authentication provides a seamless login experience for your customers with your organization’s unique branding. For more information, see [Managing Users](../../api-experience-hub/managing-users)and[Enabling Single Sign-On for Your Portal](../../api-experience-hub/enabling-sso-for-your-portal).
- 
The **Manage your API portal**page now displays a banner when any detected issues occur during a diagnostic check. These checks help administrators identify error states and troubleshoot issues. For more information, see[Managing Your Portal](../../api-experience-hub/managing-your-portal)

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| In the API Console, the asset version now has a scroll bar. | W-14486849 | 
| In the request panel, editing the request now functions properly. | W-14388490 | 
| The API Experience Hub UI no longer loops infinitely when a Salesforce token is invalid. | W-13601286 | 
| When an existing user tries to self-register, a message displays that the user already exists. | W-14320962 | 
| API instance URLs now display in the application details page. | W-14226773 | 
| In the API Console, the request tab now displays a message when an endpoint has no information defined in the request. | W-13813441 | 
| In the API Console, the response and request tab is now updated when navigating between endpoints. | W-13813442 | 
| In the API Console, the documentation and request panels now collapse when navigating between endpoints. | W-13813444 | 
| In the API Console, AsyncAPIs now display the security section as expected. | W-14147883 | 
| In the API Console, an error no longer occurs when accessing the API Console through the Builder. | W-14266801 | 
| In the API Console, the URI parameters now display as expected. | W-14391257 | 

## October 2023

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 

### Fixed Issues

| Fixed Issues | ID | 
|---|---|
| The Request Access modal is now working as expected. | W-14321558 | 
| In the API Console, the documentation is now showing. | W-14226433 | 
| In the API Console, the request for  | W-14040586 | 
| In the API Console, disabling a query parameter now removes the parameter from the URL. | W-13813435 | 
| In the API Console, filtering the resource by  | W-13719806 | 

## September 2023

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the API Console, errors occur when interacting with the Navigation page. | W-13661525 | |
| In the API Console, the endpoints are not sorting in the same order in the Navigation and Summary pages. | W-13661668 | |
| In the API Console, the Response details option is not functioning. | W-13674034 | |
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 
| The API Console is not rendering APIs properly. | W-13565177, W-13570941, W-13570959 and W-13570967 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| In Firefox and Safari, the asset cards no longer show NaN in the last updated field. | W-13803899 | 
| Validations are now triggered in the request access inputs. | W-13803904 | 
| In the API Console, an error was fixed that occurred in Salesforce 246. | W-14112563 | 
| An unexpected error no longer shows when interacting with the API Console. | W-13994257 | 
| In the API Console, you can now modify the  | W-13949057 | 
| In the API Console, the example for the  | W-13813445 | 
| In the API Console, the content type is no longer missing in the  | W-13994271 | 

## August 2023

### What’s New

- 
The API Details page now shows the count of instances and a link to the **Instances**screen where you can view the name and URL, and copy the URL if available.

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the API Console, errors occur when interacting with the  | W-13661525 | |
| In the API Console, the endpoints are not sorting in the same order in the  | W-13661668 | |
| In the API Console, the response details option is not functioning. | W-13674034 | |
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 
| The API Console is not rendering APIs properly. | W-13565177, W-13570941, W-13570959 and W-13570967 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The portal no longer returns search results when no assets are published. | W-13639213 | 
| The connection no longer fails with an unexpected error when there is no Salesforce session. | W-13676586 | 
| The installation package no longer fails with an unexpected error when the Salesforce organization does not support the second generation packages. | W-13791676 | 
| The contract list no longer fails when there is a contract for an unaccessible API. | W-13798361 | 
| The application list no longer shows an error when searching for a term with more than 300 characters. | W-13803906 | 
| A collapse and expand icon now displays for long API names on the API details page. The  | W-13803907 | 
| The API Catalog no longer reloads when entering text in the search box. | W-13803913 | 
| In the API Console, the contact information now displays in the  | W-13569134 | 
| In the API Console, the section headers now span the width of the endpoint Documentation panel. | W-13121768 | 
| In the API Console, tables and links now have the correct styles in the  | W-13525191 | 
| In the API Console, the  | W-13568832 | 
| In the API Console, the  | W-13611254 | 
| In the API Console, endpoints are no longer showing an empty response. | W-13661016 | 
| In the API Console, the response type now has the correct styles applied. | W-13674045 | 
| In the API Console, the  | W-13674015 | 
| In the API Console, headers no longer appear as required when they are not required. | W-13813437 | 
| In the API Console, the  | W-13813438 | 
| In the API Console, the  | W-13813446 | 
| In the API Console, several API components are updated to the latest version. | W-11470978 | 
| In the API Console, component documentation and migration guides are improved. | W-13661633 | 
| In the API Console, running the storybook no longer fails. | W-13739888 | 

## July 2023

**July 22, 2023**

### Known Issues

| Known Issue | Workaround | ID | 
| In the API Console, the documentation does not show the contact information in the Summary page. | W-13569134 | |
| In the API Console, errors occur when interacting with the Navigation page. | W-13661525 | |
| In the API Console, the endpoints are not sorting in the same order in the Navigation and Summary pages. | W-13661668 | |
| In the API Console, the Response details option is not functioning. | W-13674034 | |
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 
| The API Console is not rendering APIs properly. | W-13565177, W-13569134, W-13570941, W-13570959 and W-13570967 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Validating an application name is improved. | W-13209583 | 
| Links to other pages in the asset documentation are now working. | W-13471725 | 
| When requesting access to an API, an error message now displays if you try to create a new application with more than 150 characters. | W-13569048 | 
| Switching between versions no longer fails when the previous version does not have a documentation page. | W-13665874 | 
| In the API Console, the font of the Example label in the Payload section of the Documentation panel is the same size as the font of the request in the Try it panel. | W-13192142 | 
| The height of the API Console no longer resizes to accommodate the amount of content. | W-13119966 | 
| In the API Console, the documentation is no longer missing the Responses information. | W-13120027 | 
| In the API Console, the Documentation panel does not resize when interacting with it. | W-13120176 | 
| In the API Console, endpoints for API Specifications are now showing the same information as Exchange. | W-13122551 | 
| In the API Console, required fields cannot be deleted. | W-13503524 | 
| In the API Console, the Query parameters no longer lose focus when you try to add a value. | W-13513145 | 
| In the API Console, headers that are added no longer lose values. | W-13527312 | 
| In the API Console, endpoints now nest properly when sharing a prefix with methods defined. | W-13570851 | 
| In the API Console, long endpoint paths in the navigation panel now display with ellipses. Hover to show the full path. | W-13570887 | 
| In the API Console, the resource filter results no longer list values that are not resources. | W-13570903 | 
| In the API Console, the Query parameters field no longer overlaps the available space when values are long. | W-13570935 | 
| In the API Console, AsyncAPIs now shows the Channels section. | W-13570941 | 
| In the API Console, AsyncAPIs no longer show the Requests and Responses tabs in the Documentation panel. | W-13570959 | 
| In the API Console, AsyncAPIs no longer show the Headers and Payload sections in the Documentation panel. | W-13570967 | 

### Known Issues

| Known Issue | Workaround | ID | 
|---|---|---|
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 
| The API Console is not rendering APIs properly. | W-13565177, W-13569134, W-13570941, W-13570959 and W-13570967 | 

### Fixed Issues

| Issue Resolution | ID | 
| When a portal is disconnected and the MuleSoft organization is linked again to the same Salesforce organization, the styling changes are now saved during the guided styling set up. | W-13505196 | 
| The search process is now improved when entering an API name in the search box. | W-13570503 | 
| An error message now displays when you try to change the Salesforce domain for a linked organization. | W-13580841 | 
| A user session now validates whether it is using the same Salesforce Organization ID that was used when connecting the portal. | W-13602052 | 
| An External Identity license check is now validated before the connection process. | W-13643584 | 
| An asset with an enumeration custom field no longer causes deserialization errors. | W-13717720 | 

## June 2023

**June 13, 2023**

MuleSoft announces the release of Anypoint API Experience Hub.

API Experience Hub is an API management platform and digital experience that enables organizations to create vibrant API ecosystems within and outside the enterprise. API providers can share, promote, and engage with their developer community. Developers and partners can find, explore, and consume APIs designed anywhere from a single place.

### Known Issues

| Known Issue | Workaround | ID | 
| When a portal is disconnected and the MuleSoft organization is linked again to the same Salesforce organization, the styling changes are not saved during the guided styling set up. | W-13505196 | |
| In the Builder, an  | Log in to the Salesforce organization as a System Administrator and confirm you can access the  | W-13518741 | 
| The Builder cannot access the current asset library of uploaded images. | See  | W-13514487 | 
| The API Console is not rendering APIs properly. | W-13565177 W-13569134 W-13570941 W-13570959 W-13570967 |