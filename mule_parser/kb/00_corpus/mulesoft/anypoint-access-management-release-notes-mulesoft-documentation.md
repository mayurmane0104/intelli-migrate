# Anypoint Access Management Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/access-management/access-management-release-notes](https://docs.mulesoft.com/release-notes/access-management/access-management-release-notes)

---

# Anypoint Access Management Release Notes

## April 21, 2026

### What’s New

- 
Audit logs now include entries for heap dumps triggered by MuleSoft staff, providing full transparency for all administrative actions performed in your environment. This enhancement ensures that every internal diagnostic action is visible in your audit trail, meeting the compliance and security requirements of organizations managing sensitive data. This visibility is enabled by default, and no configuration is required. For more information, see [Runtime Manager Audit Logging](../../access-management/audit-logging#runtime-manager).

## November 24, 2025

### What’s New

- 
You can now enable Integration Intelligence (Beta) in Anypoint Platform. Use Integration Intelligence (Beta) to monitor, analyze, and troubleshoot your data by bringing your MuleSoft telemetry data into the Salesforce ecosystem, unlocking a new, unified observability experience. For more information, see [Integration Intelligence](../../monitoring/integration-intelligence).

## November 20, 2025

### What’s New

- 
You can now enforce IP restrictions for signin to your Anypoint Platform organization. This feature helps protect your organization by restricting access to trusted networks only. This feature is available only for US and EU commercial clouds. For more information, see [Managing IP Restrictions](../../access-management/managing-ip-allowlists).

## May 12, 2025

### What’s New

- 
In addition to Authorization Header, you can now use short-lived bearer access tokens when configuring an external OpenID Connect (OIDC) identity provider (IdP). This method enhances security by allowing you to control the token lifespan and restrict scopes to only those that are necessary. For more information, see [Configuring OpenID Connect Client Management in Anypoint Platform](../../access-management/configure-client-management-openid-task).

## April 15, 2025

### What’s New

- 
You can now choose the client secret expiration duration when you configure a Microsoft Entra ID client provider. For more information, see [Configuring Microsoft Entra ID Client Management in Anypoint Platform](../../access-management/configure-client-management-entra-id).

## November 4, 2024

### What’s New

The new **Salesforce** page in Access Management enables you to:

- 
Connect your Anypoint Platform organization with trusted Salesforce organizations. For more information, see [Connecting a Trusted Salesforce Organization to Anypoint Platform](../../access-management/connecting-salesforce-orgs)
- 
Enable, remove, and repair connections to Salesforce organizations. For more information, see [Managing Connected Salesforce Orgs](../../access-management/managing-connected-salesforce-orgs)
- 
Enable Einstein for Anypoint Code Builder through a free, shared trial Salesforce organization. For more information, see [Enable or Disable Capabilities for a Connected Salesforce Organization](../../access-management/manage-capabilities)
- 
View capabilities, such as invocable actions and Einstein that are enabled for your Anypoint Platform organization through a connected Salesforce organization. 

## August 14, 2024

### What’s New

- 
You can now access the Settings page tab for users in three different ways: - 
Click the user’s name in the **Name**column.
- 
Click the username of the user in the **Username**column.
- 
Click the More actions menu (…) in the user’s row, and select **Manage User**.For more information, see [Access the User’s Settings Page](../../access-management/users#access-user-settings).
 
- 

## July 24, 2024

### What’s New

- 
The ability to add new PingFederate client providers is deprecated. You can continue to use and manage existing PingFederate client providers. 

## May 30, 2024

### What’s New

- 
The Audit Log Query API now returns versioned object information, which is captured at the time of log generation. Previously, queries returned only the latest object information, and you had to opt in to receive versioned information. This enhancement is now standard for query results. However, the data model for query results remains unchanged. 

## May 13, 2024

### What’s New

- 
You can now update Azure AD Client secrets in Anypoint Platform access management. For more information, see [Client Secrets](../../access-management/configure-client-management-entra-id).

## April 26, 2024

### What’s New

- 
You can now manage connected apps at the business group level. Previously configured connected apps are automatically associated with your root organization. Note that users who have the Organization Administrator permission in a business group can manage only the connected apps that are configured within the respective business group. 

## April 15, 2024

### What’s New

- 
The Audit Log Query API now enables you to specify a query parameter when you call the API. This opt-in feature enables API responses to include versioned object information that was captured when the audit log was generated. For more information, see the [Audit Log Query API](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/audit-log-query-api)in Exchange.

## February 29, 2024

### What’s New

- 
The [Telemetry Exporter feature](../../monitoring/telemetry-exporter)in Anypoint Monitoring enables you to export[audit log](../../access-management/audit-logging)data to third-party analytics and observability apps.

## January 26, 2024

### What’s New

- 
The modern UI is now the only Access Management experience for all organizations. Organizations that had access to the legacy UI can no longer switch to this view. The modern UI includes the following enhancements: - 
The Teams feature for robust and scalable permissions management. Your root organization is automatically given an "Everyone at <root organization>" team that enables you to provide a basic set of permissions for all users in your organization. 
- 
A polished business group interface featuring more details, including a broader look at membership, permissions, environments, and limits. This interface enables you to view and manage access to all of your business groups at once instead of having to switch between each business group. 
- 
Visual representations of feature consumption for business groups, users, teams, roles, and SAML identity providers 
- 
Custom confidentiality notifications 
- 
Configurable audit log retention period 
- 
Improved audit log query performance 
- 
Ability to sync your organization with MuleSoft Composer 
 
- 
- 
As part of the modern UI adoption, the following features and functions have moved: - 
The list of environments is now accessible from the **Business Groups**section in Access Management.
- 
Roles are now accessible from the **Business Groups**section in Access Management.
 
- 
- 
As part of the modern UI adoption, the following features have been deprecated: - 
The business group picker in the Anypoint Platform navigation bar is no longer available. Select a business group from the **Business Groups**section in Access Management.
 
- 

## January 9, 2024

### What’s New

- 
The Anypoint Platform Sign Up page includes the following new fields: - 
Job Title 
- 
Country 
- 
State/Province 
- 
Number of Employees 
- 
Industry 
 Additionally, the **Full Name**field has been changed to**First Name**and**Last Name**fields.
- 

## November 14, 2023

### What’s New

- 
The connected app scope assignment, `Permission changes`, now logs audits together under a single entry with the corresponding sub-action (`Add assignments`,`Replace assignments`, and`Delete assignments`) instead of multiple entries for each assignment.

## September 26, 2023

### What’s New

- 
The modern UI is now the default Access Management experience for all organizations. The modern UI provides a more accessible and intuitive user experience while enabling you to use additional features, such as custom confidentiality notifications and limits pages across Access Management. Organizations that had access to the legacy UI can switch back to it using the **Hide New Features**button until January 26, 2024.

## August 28, 2023

### What’s New

- 
A new connected apps scope, `Create BGs under a given org`, enables you to use apps that have the`client_credentials`grant type to create business groups.

## July 11, 2023

### What’s New

- 
The interface that’s used to assign permissions to users, teams, and connected apps is enhanced for improved usability. 

## July 10, 2023

### What’s New

- 
For newly created organizations, audit logs now have a default retention period of one year. If your organization was created before July 10, 2023 and you did not manually change the retention period, the default retention period is still six years. 

## July 6, 2023

### What’s New

- 
When an organization administrator logs in to Anypoint Platform, they are prompted to verify that their organization is compliant with impending multi-factor authentication enforcement. 

## June 29, 2023

### What’s New

- 
The modern user interface is now enabled for new organizations by default. 

## June 6, 2023

### What’s New

- 
The usability of the Anypoint Platform **Sign in**screen is enhanced.

## May 19, 2023

### What’s New

- 
The profile linking capability is now available for all organizations globally. 

## May 2, 2023

### What’s New

- 
The `openid:google_wif`scope is now available for use with connected apps. This scope enables you to configure Anypoint as an IdP for Google Cloud by providing an`id_token`and an access token during the OAuth2 token flow for`client_credentials`connected apps.

## April 26, 2023

### What’s New

- 
The Audit Log Query endpoint now applies rate limits ( `requests per minute`) per IP address that vary depending on your control plane:- 
US: 700 
- 
EU: 40 
- 
Gov: 40 
 
- 

## April 21, 2023

### What’s New

- 
You can now link your SSO login to other Anypoint Platform profiles that share the same email address. An organization administrator must enable this feature. Only identity providers that use OpenID Connect are supported. This feature is available only for organizations located in the EU control plane. 

## March 6, 2023

### What’s New

- 
In the Connected Apps audit logs, the `Token Retrieval Success`and`Token Retrieval Failure`entries now have`clientIP`in their payloads.

## March 1, 2023

## What’s New

- 
Access Management’s modern UI is now enabled by default for new organizations. Organizations that still use the legacy UI can migrate to the modern UI using the **Try New Features**dialog

## February 21, 2023

### What’s New

- 
To enhance accessibility and usability, the Connected Apps feature’s scope workflow has been polished. 

## January 18, 2023

### What’s New

- 
The following pages now have sections showing limits imposed by Anypoint Platform: - 
Business groups (including the page for your root organization) 
- 
Users 
- 
Teams 
- 
Roles 
- 
SAML identity providers 
 Note that this feature is available only if you have enabled the **New Features**Access Management user interface.
- 

## December 15, 2022

### What’s New

- 
Organization administrators can now create a custom confidentiality notification that appears when users log in to their organization. 

## November 30, 2022

### What’s New

- 
The Audit Log Query API now supports more efficient querying. For more information, see [the tutorial in the Audit Logs documentation](../../access-management/audit-logging#paginated-logs).
- 
For improved loading times, the pagination on the Audit Logs page has changed to display `many`instead of listing the number of entries if that number exceeds 10,000.
- 
If your organization has not opted in to the new and improved features, Access Management now prompts you to try the new features and offers UI prompts to enable smooth adoption. 
- 
Business group overviews now have the **Access Overview**section that enables you to view a list of users who have a specified permission across business groups.
- 
When you select a business group in the **Business Groups**page, the**Settings**section for that business group opens by default.
- 
Sliders for vCore allocations have been readded to the **Settings**section of business groups.
- 
To enhance usability, the Teams feature and permissions workflows have been polished. 

## November 14, 2022

### What’s New

- 
Audit logs now collect and display data for the connected apps `login`action via`token retrieval success`and`token retrieval failure`.

## October 29, 2022

### What’s New

- 
Multi-factor authentication (MFA) is now required for all non-SSO user accounts unless they are on their organization’s exemption list. At login, Anypoint Platform now prompts users to configure a verification method if they have not already. 
- 
You no longer have the option to make MFA optional across your entire organization. 

## October 10, 2022

### What’s New

- 
For enhanced security, Anypoint Platform now prompts non-SSO user accounts to verify their email address. 

## September 6, 2022

### What’s New

- 
You can now change the retention period for your organization’s audit logs. To change audit log retention periods, you must have the Audit Log Config Manager permission over your root organization. 

## August 20, 2022

### What’s New

- 
The Connected Apps feature now includes generated documentation based on supported scopes and permissions. This documentation is accessible in **Access Management**>**Connected Apps**>**Scopes Documentation**tab.

## July 23, 2022

### What’s New

- 
For enhanced security, Access Management might ask users to re-authenticate before they can modify their email addresses. Similarly, Access Management might ask organization administrators to re-authenticate before they can modify their organization users’ email addresses. This change prevents bad actors from taking advantage of stale browser sessions. 
- 
User accounts that are added to an existing organization must configure multi-factor authentication (MFA). 

## April 29, 2022

### What’s New

- 
When you create a new organization, multi-factor authentication (MFA) is enabled by default. While it is best to use the Connected Apps feature instead of service accounts, an organization administrator can add service accounts or other user accounts without MFA to an exemption list. 
- 
You can now check the retention period for your organization’s audit logs using the [Audit Logging API](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/audit-log-query-api/minor/1.0/console/method/%23335/).

## February 21, 2022

### What’s New

- 
You can now configure Azure Active Directory (Azure AD) as a client provider. As your client provider, Azure AD provides a stateless microservice to convert OAuth 2.0 client application registration requests to requests supported by Azure AD. Additionally, configuring Azure AD as a client provider enables you to authenticate and authorize existing API consumers. 

## January 14, 2022

### What’s New

- 
When you configure the **Issuer**field while adding a client provider, such as Okta, that is compatible with[this spec](https://datatracker.ietf.org/doc/id/draft-ietf-oauth-discovery-08.html), metadata from`$ISSUER/.well-known/oauth-authorization-server`is discovered and validated prior to merging. Once the validation is complete, a complete list of available grant types appears. If you want to fetch metadata for validation for an existing client provider, save that client provider again, and the validation occurs automatically.
 This change makes the client provider registration process smoother for Okta users. Additionally, this change also enables the use of the Client Credentials grant type.
- 
When you use dynamic client registration to configure a client provider, you can now configure the length of time at which a client provider times out. The minimum timeout value is five seconds, and the maximum value is 20 seconds. 

## November 3, 2021

### What’s New

- 
Organization administrators can now configure up to 25 SAML 2.0 or OpenID Connect identity providers (IdPs) for single sign-on. 
- 
To support multiple external IdPs, there are new endpoints available for the Access Management API; existing identity provider configurations are unaffected. 

## September 8, 2021

### What’s New

- 
In Organization settings and Runtime Manager subscription information, the name of VPN counter is now **Network Connections**. The**Network Connections**setting enables you to allocate your VPN connections and AWS Transit Gateway attachments in your organization.

## August 5, 2021

### What’s New

- 
Users who have not enabled multi-factor authentication (MFA) will be prompted to enable MFA weekly until they enable it. While MuleSoft recommends enabling MFA on all user accounts (preferably by requiring it for the entire organization), using MFA is still optional. 

## June 10, 2021

The Teams feature provides improved user and permission management. Teams provides user grouping mechanisms in Anypoint Platform, which streamlines collaboration, reuse, and scalability. Use teams to:

- 
Manage users and permissions across multiple business groups 
- 
Define permissions and then assign them to multiple users in one click 
- 
Set global permissions (for example, give everyone in your organization the Exchange Viewer permission) 
- 
Share Exchange assets with a specific group of users 

Additionally, the Access Management navigation menu and user interface have been revamped to simplify navigation and permission management across business groups.

Enhancements and updates are available on an opt-in basis. You can continue using old views after the Teams feature and user interface enhancement release.

## January 20, 2021

When you change your password, you can no longer reuse your previous three passwords.

## December 15, 2020

If you are using an external identity provider, such as Okta or Salesforce, you can now map users in a federated organization’s OpenID Connect (OIDC) groups to roles in Anypoint Platform.

## October 29, 2020

- 
You can now enable multi-factor authentication (MFA) as a sign-in requirement across your entire organization. MFA makes logging in to Anypoint Platform more secure. 
- 
You can now easily rotate SAML 2.0 SSO keys. You can generate a key or upload an existing public/private key pair. 

## June 29, 2020

You can now import SAML 2.0 metadata to configure your identity provider with Anypoint Platform.

## June 13, 2020

You can now export service provider SAML 2.0 metadata to configure Anypoint Platform with your identity provider.

## May 30, 2020

These are the enhancements and new features for Access Management.

- 
Organization administrators can configure whether SAML SSO can be initiated by Anypoint Platform (service provider-initiated SSO), their external identity provider (identity provider-initiated SSO), or both. 
- 
You can now log in using SSO from the Anypoint Platform login page via your organization’s domain. This domain is available on your user profile page. 
- 
When the permission scopes change for an approved connected app, an organization administrator must approve the new set of scopes. 

## January 24, 2020

Anypoint Platform now includes an External Access feature that serves as the foundation for improved cross-organization collaboration such as the sharing of assets.

## October 18, 2019

This release of Access Management provides increased security and development capabilities via the Connected Apps feature.

The Connected Apps feature enables you to delegate access to apps without sharing sensitive credentials or giving third parties full control of their accounts. You can audit the app’s use of data, and you can revoke access anytime.

With this release, developers can create apps that use a **Sign in with Anypoint Platform** widget. When users interact with this widget, they can authorize apps to access their Anypoint Platform information.

Actions taken by apps are audited. Note that some products do not currently include client IDs in this release of the Connected Apps feature.

## April 20, 2019

These are the enhancements and new features for Access Management:

- 
A VPN counter is added under Business Group settings to allow a fine-grained allocation of purchased VPNs within your organizations. 
- 
Audit log dates now display a timestamp for a year. 
- 
When configuring an external identity provider, users can now disable server certificate validation. See [Configure OpenID Connect Client Management](../../access-management/configure-client-management-openid-task).
- 
Enablement of non-SSO users for your organization allows organization administrators to invite and authenticate users outside of the external SSO configured for your organization. 
- 
Organization administrators can enable and disable automapper capability for Flow Designer under the organization settings in Access Manager. See the Flow Designer documentation for more information. 
- 
You can enable client deletion in Anypoint Platform, which allows deletions of clients within Anypoint Platform. See [Configure OpenID Connect Client Management](../../access-management/configure-client-management-openid-task).
- 
You can enable client deletion and updates in IdP, which allows updates and deletions of external clients in the configured IdP through an outbound call made by Anypoint Platform. To use this feature, you should opt-in to client deletion within Anypoint Platform. 
- 
The Audit Log screen and a downloadable CSV file now include environment names for events from API Manager, Runtime Manager, CloudHub, Partner Manager, and MQ. 

## August 25, 2018

*Version 0.46.0*

MuleSoft supports using [Salesforce Identity](https://trailhead.salesforce.com/content/learn/modules/identity_basics) as a SSO (single sign-on) provider with the [OpenID Connect](https://openid.net/developers/how-connect-works/) protocol. Salesforce is a [certified OpenID Provider](https://openid.net/certification/).

### Deprecated Functionality

- 
Deleted federated users are no longer able to sign in from the SSO login page. Organization administrators must re-enable deleted users before they can continue operations on Anypoint Platform. 
- 
You can’t create a Business Group name using special characters. Only the following characters are valid: - 
Letter 
- 
Number 
- 
Apostrophe 
- 
Space 
- 
Comma 
- 
Period 
- 
Hyphen 
- 
Underscore 
 Existing Business Groups whose names contain special characters aren’t affected. 
- 

## November 18, 2017

*Version 0.29.0*

Access Management v0.29.0 enables external Anypoint users to create client applications on public API portals. These external users will be shown under a New tab for external users in the Users section of the Access Management UI. This release also includes infrastructure changes that improve platform performance.

### Hardware and Software Requirements

No change.

### Compatibility

NA

### Deprecated Features or Functionality

None.

### Resolved Issues

None.

### Migration Guidance

No migration required.

## October 7, 2017

*Version 0.27.0*

Access Management v0.27.0 supports identity providers, such as Okta, that are compliant with the OpenID Connect Dynamic Client Registration protocol for API Client Management. You can now use these providers to protect API Gateways through a generic access token enforcement policy. This release also includes infrastructure improvements to help with performance. For more information, see the [client management documentation](../../access-management/managing-api-clients).

## June 24, 2017

*Version 0.23.1*

Access Management v0.23.1 enhances the user experience for configuring external identity forms through tooltips and form validation mechanisms. It provides several infrastructure improvements. MuleSoft has also validated our OpenID Connect SSO solution with Okta, OpenAM, and Ping Federate.

### Hardware and Software Requirements

No change.

### Compatibility

NA

### Deprecated Features or Functionality

None.

### Resolved Issues

None.

### Migration Guidance

No migration required.

## May 6, 2017

*Version 0.22.0*

Access Management v0.22 supports OpenID Connect-compliant identity providers (IdPs) for Single Sign On to Anypoint Platform. Through a new UI for external identity configurations, this release also brings the client UI configuration forms for PingFederate and OpenAM into the platform.

### Hardware and Software Requirements

No change

### Compatibility

N/A

### Deprecated Features or Functionality

The process for OAuth client management configuration is now self-serve through forms made available in the External Identity section of Access Management. The google forms for OpenAM and PingFederate configuration are now deprecated.

### Resolved Issues

None

### Migration Guidance

No migration required

## January 14, 2017

*Version 0.18.0*

Access Management v0.18 adds a [no CAPTCHA reCAPTCHA](https://cloud.google.com/security/products/recaptcha) verification step in our [sign up process](../../access-management/managing-your-account#how-to-create-your-account).

### Hardware and Software Requirements

No change.

### Compatibility

NA

### Deprecated Features or Functionality

None.

### Resolved Issues

None.

### Migration Guidance

No migration required.

## November 19, 2016

*Version 0.17.0*

Access Management v0.17 is a minor release that addresses some marketing requirements in our platform.

### Hardware and Software Requirements

No change.

### Compatibility

NA

### Deprecated Features or Functionality

None.

### Resolved Issues

None.

### Migration Guidance

No migration required.

## October 22, 2016

*Version 0.16.0*

Access Management v0.16 allows **Organization administrators** and **Audit Log Viewers** to view entitlement changes to their organization from the [Audit Logs UI](../../access-management/audit-logging).

Additionally, Access Management now supports Ping Federate v8.2.1.1 for [External Identity](../../access-management/external-identity).

### Hardware and Software Requirements

No change.

### Compatibility

NA

### Deprecated Features or Functionality

None.

### Resolved Issues

None.

### Migration Guidance

No migration required.

## September 24, 2016

*Version 0.15.0*

Access Management v0.15 improves the user invitation experience and allows users to accept organization invitations with an existing Anypoint username.

If a user has different usernames associated with an email address and receives an invitation to a new organization, the user is now given the option to accept the invitation with any one of her existing accounts, thereby,  associating the selected username with this new organization.

If the selected username is already associated with another Anypoint organization, the user is then given the option to detach this username from the existing organization. If she is the only user in that org, she is also given the ability to delete that organization as usernames must remain unique across all Anypoint organizations. At any stage in the invite process, she can always chose to create a new username.

### Hardware and Software Requirements

No change.

### Compatibility

NA

### Deprecated Features or Functionality

None.

### Resolved Issues

None.

### Migration Guidance

No migration required.

## August 27, 2016

*Version 0.14.0*

The Access Management V0.14.0 release makes minor improvements to Anypoint Platform’s notifications about your Trial subscription period.

If you are in your 30 day trial period, you can see the expiration date under the **Subscription** section in the Access Management UI. After your trial period expires your account will be converted to a “Free” subscription tier where you will lose the ability to deploy apps and APIs along with other Enterprise functionality within Anypoint Platform.

You will still be able to login to your account.

### Hardware and Software Requirements

No change.

### Compatibility

NA

### Deprecated Features or Functionality

None.

### Resolved Issues

None.

### Migration Guidance

No migration required.

## June 25, 2016 Release

*Version 0.13.0*

The Access Management V0.13.0, is a minor release that fixes a few bugs improving the platform’s performance.

### Hardware and Software Requirements

No change.

### Compatibility

NA

### Deprecated Features or Functionality

None.

### Resolved Issues

None.

### Migration Guidance

No migration required.

## May 14, 2016 Release

*Version 0.12.0*

The Access Management V0.12.0, is a minor release that makes the Audit Logs UI a GA functionality. Using this UI users can query and filter Audit logs.

### Hardware and Software Requirements

No change.

### Compatibility

NA

### Features and Functionality

Audit Logs UI for Anypoint Platform: Changes made by users within an Anypoint Platform organization are logged through an audit logging service. You can now access the data logs through the Audit Logs UI under Access Management or by leveraging the Audit Logging Query API. See Audit Logs.

### Deprecated Features or Functionality

None.

### Resolved Issues

None.

### Migration Guidance

No migration required.