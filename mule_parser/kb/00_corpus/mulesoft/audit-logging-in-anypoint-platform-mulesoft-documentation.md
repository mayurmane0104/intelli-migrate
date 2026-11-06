# Audit Logging in Anypoint Platform | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/access-management/audit-logging](https://docs.mulesoft.com/access-management/audit-logging)

---

Set T&C

# Audit Logging in Anypoint Platform

The audit logging service provides a queryable history of actions performed within Anypoint Platform. It keeps track of all user interactions with objects in the system and timestamps those actions. Audit logging also provides mechanisms for querying the set of users who performed actions, the set of objects that had actions performed on them, and other endpoints that enable log entry querying.

Audit logs have a default retention period of one year. If your organization was created before July 10, 2023 and you didn’t manually change the retention period, the retention period is six years. Users who have the Organization Administrator and Audit Log Config Manager permissions can customize the retention period. For more information, see [Configure Audit Log Retention in Anypoint Platform](audit-log-retention). Download your logs periodically to retain your log files for longer than the current retention period.

You can access audit logs through the Audit Log Query API or through the audit logging UI.

## Access Audit Logging

Access audit logs in the UI and via the Audit Log Query API, scoped to your business group.

Users who have the Anypoint Platform **Organization Administrator** permission or the **Audit Log Viewer** permission have access to both the UI and the Audit Log Query API. The audit log service is business-group aware, which means you see only logs that are relevant to your own business group.

The audit log UI is embedded in Access Management.

- 
Sign in to Anypoint Platform. 
- 
Select **Access Management**from themenu. 
- 
In the Access Management navigation menu, click **Audit Logs**.

The **Audit Logs** page displays the logs. You can:

- 
Download audit logs. 
- 
Set a time period for showing audit logs. 
- 
Filter audit logs by product, type, and actions. 
- 
Search audit logs by environment, object, and user. 

## Export Audit Logs

Export audit logs to external observability tools using Telemetry Exporter.

If you have the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform, you can use the [Telemetry Exporter feature](../monitoring/telemetry-exporter) in Anypoint Monitoring to export audit logs to third-party analytics and observability apps.

When exported, audit logs have a unique ID in the `mulesoft.audit.id` attribute. In usual operations, each log is delivered only once, but under certain circumstances, some logs are delivered more than once. Duplicate log entries always share the unique `mulesoft.audit.id` attribute, so this attribute can be used to safely block or remove duplicate logs from the target system.

Telemetry Exporter for audit logs currently has these data differences, limitations, and known issues:

- 
The audit logs that the Telemetry Exporter sends to third-party apps often have different field names from the audit logs that appear in Access Management or the Audit Query Log API. 
 For example, audit logs shown in the UI or retrieved by the Audit Log Query API describe a user action (such as`update`or`delete`) as`action`, whereas the OpenTelemetry attribute refers to it as`mulesoft.audit.action`.
- 
If the audit log entry metadata and payload field exceed 30KB when compressed, the payload is truncated before compression. 

## Audit Log Contents

Activities in the audit log are actions that occur at a particular time, involve one or more objects, have an action type (such as `delete` or `approve`) associated with the objects, and optionally a payload that can store application-specific information such as changed fields and environment information.

Each log entry has a set of properties that provides information about the activity:

- 
**Time**: Timestamp when the activity occurred
- 
**Product**: Product where the object resides, for example,`Access Management`
- 
**Type**: Type of object the action is performed on, for example,`Organization`
- 
**Action**: Action associated with the object, for example,`Create`
- 
**Object**: Name of the object, for example,`foo`
- 
**User Name**: User who performed the action, for example,`johndoe`Occasionally, there are `Anypoint Staff`log entries. This log entry is made when the audit action was performed by a user who doesn’t belong to your organization.`Anypoint Staff`entries are created when these events occur:- 
An internal or system process that’s a routine part of Anypoint Platform operations is performed 
- 
The MuleSoft procurement staff changes entitlements for your organization as a result of license grants 
- 
An action is performed by a MuleSoft employee on your behalf for other purposes, such as troubleshooting 
 
- 
- 
**Connected App**: Name of the connected app that takes an action on behalf of itself or a user. If a connected app didn’t run the action, the payload is`N/A`.
- 
**Environment**: Environment names for events from API Manager, Runtime Manager, CloudHub, Partner Manager, and MQ.
- 
**Parent**: (Optional) Parent of the object (if any) the action is performed on. This mainly applies to APIs.
- 
**Payload**: (Optional) More information about the log properties. For example, if an organization is created, the payload contains information about the organization and the owner, such as IDs.

This is a list of actions per product and object type that Anypoint Platform audits:

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| T&C | T&C | N/A | Create | Subaction: None | |
| Modify T&C | T&C | T&C | N/A | Edit | Subaction: None | 
| Set org custom theme | Portal theme | Org name | N/A | Create | Subaction: None | 
| Edit org custom theme | Bus. Group | Org Name | N/A | Edit | Subaction: None | 
| Add custom policy | Policy | PolicyID | N/A | Create | Subaction: None | 
| Delete custom policy | Policy | PolicyID | N/A | Delete | Subaction: None | 

### APIs

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create API | API | API ID | N/A | Create | Subaction: None | 
| Delete API | API | API ID | N/A | Delete | Subaction: None | 
| Import API | API | API ID | N/A | Create | Subaction: None | 
| Update label of API | API | API ID | N/A | Edit | Subaction: None | 
| Update consumer endpoint of API | API | API ID | N/A | Edit - update endpoint | Subaction: None | 
| Update endpoint URI of API | API | API ID | N/A | Edit - edit endpoint URI | Subaction: None | 

### API Versions

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create API version | API version | Version ID | API ID | Create | Subaction: None | 
| Delete API version | API version | Version ID | API ID | Delete | Subaction: None | 
| Import API | API version | Version ID | API ID | Create | Subaction: Import API version | 
| Edit name of API version | API version | Version ID | API ID | Edit | Subaction: Edit name | 
| Edit description of API version | API version | Version ID | API ID | Edit | Subaction: Edit description | 
| Edit API URL of API version | API version | Version ID | API ID | Edit | Subaction: Edit API URL | 
| Add tag | API Version | Version ID | API ID | Edit | Subaction: Add tag | 
| Remove tag | API Version | Version ID | API ID | Edit | Subaction: Remove tag | 
| Deprecate API | API version | Version ID | API ID | Edit | Subaction: Deprecate API | 
| Set T&Cs | API Version | Version ID | API ID | Edit | Subaction: Set terms & conditions | 
| Create RAML | API Version | Version ID | API ID | Edit | Subaction: Create RAML | 
| Modify RAML | API Version | Version ID | API ID | Edit | Subaction: Edit RAML | 
| Create endpoint | API version | Version ID | API ID | Edit | Subaction: Create endpoint | 
| Update existing endpoint | API version | Version ID | API ID | Edit | Subaction: Update endpoint | 
| Deploy proxy | API Version | Version ID | API ID | Deploy | Subaction: None | 
| Update deployed proxy | API version | Version ID | API ID | Edit | Subaction: Configure endpoint | 
| Redeploy proxy | API Version | Version ID | API ID | Deploy | Subaction: None | 
| Create SLA tier | Tier | SLA ID | Version ID | Create | Subaction: None | 
| Modify SLA tier | Tier | SLA ID | Version ID | Edit | Subaction: None | 
| Deprecate SLA tier | Tier | SLA ID | Version ID | Edit | Subaction: Deprecate SLA tier | 
| Delete SLA tier | Tier | SLA ID | Version ID | Delete | Subaction: None | 
| Apply policy | API policy | Policy ID | Version ID | Create | Subaction: None | 
| Edit policy | API policy | Policy ID | Version ID | Edit | Subaction: None | 
| Remove policy | API policy | Policy ID | Version ID | Delete | Subaction: None | 

### Application

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create application | Application | App ID | N/A | Create | Subaction: None | 
| Delete application | Application | App ID | N/A | Delete | Subaction: None | 
| Reset client secret | Application | App ID | N/A | Edit - reset client secret | Subaction: Reset client secret | 
| Request access | Contract | Object 1: App ID | N/A | Create | Subaction: None | 
| Request tier change | Contract | Object 1: App ID | N/A | Edit - request tier change | Subaction: Request tier change | 
| Request tier change approval | Contract | Object 1: App ID | N/A | Edit - request tier change approval | Subaction: Request tier change approval | 
| Approve application | Contract | Object 1: App ID | N/A | Edit - contract approval | Subaction: Contract approval | 
| Revoke application | Contract | Object 1: App ID | N/A | Edit - contract revoke | Subaction: Contract revoked | 
| Restore application | Contract | Object 1: App ID | N/A | Edit - contract restore | Subaction: Contract restored | 

The `Create Application` and `Delete Application` actions are logged at the root organization level.

## Access Management

Audited actions for Access Management entities, including users, roles, permissions, identity providers, organizations, environments, and connected apps.

### Users

Audit logging for login activities follows these rules:

- 
Organization Scope Login and logout actions are logged only at the organization level. 
- 
Anypoint Platform Accounts Login failures are logged only for existing user accounts. 
- 
SSO via SAML Login failures are recorded in the audit log. 
- 
SSO via LDAP or OIDC Login failures are not recorded in the audit log. This applies to both Anypoint Platform and Anypoint Platform Private Cloud Edition (Anypoint Platform PCE). 

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Signup / Organization creation | User | UserID | N/A | Create | Subaction: None | 
| User creation (w/out creating an org) | User | UserID | N/A | Create | Subaction: None | 
| Password reset requested | User | UserID | N/A | Edit | Subaction: Password reset | 
| Password changed | User | UserID | N/A | Edit | Subaction: Password changed | 
| Delete user | User | UserID | N/A | Delete | Subaction: None | 
| Disable user | User | UserID | N/A | Edit | Subaction: Disable user | 
| Login success | User | UserID | N/A | Login | Subaction: None | 
| Login success reauthenticate | User | UserID | N/A | Login - Reauthenticate | Subaction: Reauthenticate | 
| Login failure | User | UserID | N/A | Login | Subaction: Failure | 
| Login failure reauthentication | User | UserID | N/A | Login - Reauthentication Failure | Subaction: Reauthentication Failure | 
| Logout | User | UserID | N/A | Logout | Subaction: None | 

### Roles

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create role | Role | Role | N/A | Create | Subaction: None | 
| Edit role - add user | Object 1: Role | Object 1: Role | N/A | Edit | Subaction: Add user | 
| Edit role - remove user | Object 1: Role | Object 1: Role | N/A | Edit | Subaction: Remove user | 
| Edit role - change external group mapping | Role | Role | N/A | Edit | Subaction: Edit role mapping | 
| Delete role | Role | Role | N/A | Delete | Subaction: None | 

### Permissions

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| User permission change | Permission | Object 1: User | Parent 1: N/A | Permissions change | Subaction: None | 
| Role permission change | Permission | Object 1: Role | Parent 1: N/A | Permissions change | Subaction: None | 
| Environment permissions change | Permission | EnvID | N/A | Permissions change | Subaction: None | 

### Identity Management

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create identity provider configuration | Identity management | Provider name | N/A | Create | Subaction: None | 
| Edit identity provider configuration | Identity management | Provider name | N/A | Edit | Subaction: None | 
| Delete identity provider configuration | Identity management | Provider name | N/A | Delete | Subaction: None | 
| Warning | Object 1: Identity management | Object 1: Provider name | N/A | None | Subaction: None | 
| Create identity management key | Identity management key | KeyID | N/A | Create | Subaction: None | 
| Set primary identity management key | Identity management key | KeyID | N/A | Edit | Subaction: Set primary key 
 | 
| Delete identity management key | Identity management key | KeyID | N/A | Delete | Subaction: None | 

### Organization and Business Groups

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Edit domain name | Organization | OrgID | N/A | Edit | Subaction: None | 
| Create business group | Organization | OrgID | Parent organization | Create | Subaction: None | 
| Edit business group name | Organization | OrgID | Parent organization | Edit | Subaction: Edit name | 
| Edit business group owner | Organization | OrgID | Parent organization | Edit | Subaction: Edit owner | 
| Edit business group entitlement | Entitlement | EnvID | N/A | Edit | Subaction: Edit entitlement | 
| Delete business group | Organization | OrgID | Parent organization | Delete | Subaction: None | 

### Environments

| User Action | Object Type | Object | Parent | Action | Payload | ||
|---|---|---|---|---|---|---|---|
| Create environment | Environment | EnvID | N/A | Create | Subaction: None | ||
| Delete environment | Environment | EnvID | N/A | Delete | Subaction: None | ||
| Rename environment | Environment | EnvID | N/A | Edit | Subaction: None 
 | 

### Connected Apps

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create Connected Application | Connected Application | clientID | N/A | Create | Subaction:
None 
 | 
| Edit Connected Application | Connected Application | clientID | N/A | Edit | Subaction:
None 
 | 
| Delete Connected Application | Connected Application | clientID | N/A | Delete | Subaction:
None 
 | 
| Update Scope Assignments | Connected Application | clientID | N/A | Permissions Change | Subaction: Add Assignments | 
| Application Authorization Approved | External Authorization | clientID | N/A | Approved | Subaction: None | 
| Application Authorization Denied | External Authorization | clientID | N/A | Denied | Subaction: None | 
| Token Retrieval Success | Connected Application | clientID | N/A | Login - Token | Subaction: Token 
 | 
| Token Retrieval Failed | Connected Application | clientID | N/A | Login - Token | Subaction: Token 
 | 
| Revoke Access/Refresh Tokens | Connected Application | clientID | N/A | Revoke Tokens | Subaction:
None 
 | 

### Teams

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create Team | Team | Team Name | N/A | Create | Subaction:
None 
 | 
| Update Team | Team | Team Name | N/A | Update | Subaction:
None 
 | 
| Move Team | Team | Team Name | N/A | Move | Subaction:
None 
 | 
| Add Members | Team | Team Name | N/A | Edit | Subaction:
Add Members 
 | 
| Remove Members | Team | Team Name | N/A | Edit | Subaction:
Remove Members 
 | 
| Add Permissions | Team | Team Name | N/A | Permissions change | Subaction:
Add permissions 
 | 
| Remove Permissions | Team | Team Name | N/A | Permissions change | Subaction:
Remove permissions 
 | 
| Edit External Group Mappings | Team | Team Name | N/A | Edit | Subaction:
Edit external group mapping 
 | 
| Delete Team | Team | Team Name | N/A | Delete | Subaction: None 
 | 

### User IdP Profiles

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create User IdP Profile | User IdP Profile | N/A | N/A | Create | Subaction:
None 
 | 

## Anypoint DataGraph

Audited actions related to DataGraph operations, such as adding, updating, and removing APIs from unified schemas.

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Add API | User | data-graph-{api-name}-{env-name} | N/A | Add API | N/A | 
| Update API | User | data-graph-{api-name}-{env-name} | N/A | Update API | N/A | 
| Remove API | User | data-graph-{api-name}-{env-name} | N/A | Remove API | N/A | 

## Anypoint MQ

Audited actions for messaging components, including queues, exchanges, bindings, and clients.

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create/modify/delete/purge queue | Queue | queueID | N/A | Create/modify/delete | Subaction: None | 
| Create/modify/delete exchange | Exchange | exchangeID | N/A | Create/modify/delete | Subaction: None | 
| Create/delete exchange binding | Binding | bindingID | N/A | Create/delete | Subaction: None | 
| Create/delete/regenerate client | Client | clientID | N/A | Create/delete/regenerate | Subaction: None | 

## API Designer APIs

Audited actions for Design Center projects and API design activities, including project lifecycle and asset publication.

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create project | Project | Project ID | N/A | Create project | Subaction:
None 
 | 
| Delete project | Project | Project ID | N/A | Delete project | Subaction:
None 
 | 
| Delete files | Files | Project ID | N/A | Delete files | Subaction:
None 
 | 
| Rename project | Project | Project ID | N/A | Rename project | Subaction:
None 
 | 
| Clean branch | Project | Project ID | N/A | Clean branch | Subaction:
None 
 | 
| Create branch | Project | Project ID | N/A | Create branch | Subaction:
None 
 | 
| Delete branch | Project | Project ID | N/A | Delete branch | Subaction:
None 
 | 
| Save branch | Project | Project ID | N/A | Save branch | Subaction:
None 
 | 
| Delete file | Project | Project ID | N/A | Delete file | Subaction:
None 
 | 
| Move file | Project | Project ID | N/A | Move file | Subaction:
None 
 | 
| Import project | Project | Project ID | N/A | Import project | Subaction:
None 
 | 
| Publish to Exchange | Project | Project ID | N/A | Publish to Exchange | Subaction:
None 
 | 
| Publish to API Platform | Project | Project ID | N/A | Publish to API Platform | Subaction:
None 
 | 
| Add dependencies | Project | Project ID | N/A | Add dependencies | Subaction:
None 
 | 
| Remove dependencies | Project | Project ID | N/A | Remove dependencies | Subaction:
None 
 | 
| Change dependencies | Project | Project ID | N/A | Change dependencies | Subaction:
None 
 | 
| Reload dependencies | Project | Project ID | N/A | Reload dependencies | Subaction:
None 
 | 
| Merge Branch | Project | Project ID | N/A | Merge Branch | Subaction:
None 
 | 
| Share project | Project | Project ID | N/A | Share project | Subaction:
None 
 | 
| Sync with Github | Project | Project ID | N/A | Sync with Github | Subaction:
None 
 | 
| Unsync with Github | Project | Project ID | N/A | Unsync with Github | Subaction:
None 
 | 
| Modify organization settings | Project | Organization ID | N/A | Modify organization settings | Subaction:
None 
 | 
| Rename branch | Project | Project ID | N/A | Rename branch | Subaction:
None 
 | 
| Modify project settings | Project | Project ID | N/A | Modify project settings | Subaction:
None 
 | 

### Mocking Service

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create link | Link | Link ID | N/A | Create | Subaction:
Create Link | 
| Delete link | Link | Link ID | N/A | Delete | Subaction:
Delete Link | 

### Portals

These actions apply to API Manager v1.x portals:

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create portal | Portal | Object 1: Portal ID | N/A | Create | Subaction: None | 
| Modify portal association | Portal | Object 1: Portal ID | N/A | Edit | Subaction: Change portal association | 
| Delete portal | Portal | Portal ID | N/A | Delete | Subaction: None | 
| Add portal page | Portal | Page ID | Portal ID | Edit | Subaction: Add portal page | 
| Make portal page visible | Portal | Page ID | Portal ID | Edit | Subaction: Make page visible | 
| Delete portal page | Portal | Page ID | Portal ID | Delete | Subaction: Delete portal page | 
| Edit portal page | Portal | Page ID | Portal ID | Edit | Subaction: Edit portal page | 
| Hide portal page | Portal | Page ID | Portal ID | Edit | Subaction: Hide portal page | 
| Set portal theme | Portal | Portal ID | N/A | Edit | Subaction: Set portal theme | 
| Modify portal theme | Portal | Portal ID | N/A | Edit | Subaction: Modify portal theme | 
| Modify portal security | Portal | Portal ID | N/A | Edit | Subaction: Set security | 

## API Governance

Audited actions for governance profiles and enforcement activities across your APIs.

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create profile | Profile | Profile name | N/A | Create | Subaction: None | 
| Update profile | Profile | Profile name | N/A | Update | Subaction: None | 
| Delete profile | Profile | Profile name | N/A | Delete | Subaction: None | 
| Activate profile | Profile | Profile name | N/A | Activate | Subaction: None | 

## Exchange

Audited actions for Exchange assets, portals, metadata, and sharing operations.

### Assets

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create an asset | Asset | Asset ID | N/A | Create | Subaction: None | 
| Update an asset | Asset | Asset ID | N/A | Update | Subaction: None | 
| Delete an asset | Asset | Asset ID | N/A | Delete | Subaction: None | 
| Share an asset | Asset | Asset ID | N/A | Granted or revoked permissions | Subaction: None 
 | 
| Publish an asset to public portal | Asset Version Group | Asset ID and version group | N/A | Publish to public portal | Subaction: None | 
| Remove an asset from public portal | Asset Version Group | Asset ID and version group | N/A | Remove from public portal | Subaction: None | 
| Update an asset icon | Asset icon | Asset ID | Asset | Update | Subaction: None | 
| Delete an asset icon | Asset icon | Asset ID | Asset | Delete | Subaction: None | 
| Create a managed tag (category) | Asset managed tag | Asset ID and tag ID | Asset | Create | Subaction: None | 
| Delete a managed tag (category) | Asset managed tag | Asset ID and tag ID | Asset | Delete | Subaction: None | 
| Delete an organization | Organization | Organization ID | N/A | Delete | Subaction: None | 
| Update tags | Asset tags | Asset ID | Asset | Update | Subaction: None | 
| Create a tag configuration | Tag configuration | Tag configuration ID | N/A | Create | Subaction: None | 
| Update a tag configuration | Tag configuration | Tag configuration ID | N/A | Update | Subaction: None | 
| Delete a tag configuration | Tag configuration | Tag configuration ID | N/A | Delete | Subaction: None | 

### Asset Portals

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create a page | Asset portal page | Page ID | Asset portal | Create | Subaction: None 
 | 
| Update a page | Asset portal page | Page ID | Asset portal | Update | Subaction: None 
 | 
| Delete a page | Asset portal page | Page ID | Asset portal | Delete | Subaction: None | 
| Create a portal | Asset portal | Portal ID | Asset | Create | Subaction: None | 
| Publish a portal | Asset portal | Portal ID | Asset | Publish | Subaction: None | 

### API Metadata

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create an API instance | API instance | API instance ID | N/A | Create | Subaction: None 
 | 
| Delete an API instance | API instance | API instance ID | N/A | Delete | Subaction: None 
 | 
| Update an API instance | API instance | API instance ID | N/A | Update | Subaction: None 
 | 

### File Upload

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Upload file | Exchange file | File ID | N/A | Create | Subaction: None | 
| Delete file | Exchange file | File ID | N/A | Delete | Subaction: None | 
| Update file | Exchange file | File ID | N/A | Update | Subaction: None | 

### Public Portals

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Update a domain | Public portal domain | Organization ID and domain | Public portal | Update | Subaction: None 
 | 
| Delete a domain | Public portal domain | Organization ID and domain | Public portal | Delete | Subaction: None 
 | 
| Create a page | Public portal page | Page path | Public portal | Create | Subaction: None 
 | 
| Delete a page | Public portal page | Page path | Public portal | Delete | Subaction: None 
 | 
| Update a page | Public portal page | Page path | Public portal | Update | Subaction: None 
 | 
| Create a portal | Public portal | Organization ID | N/A | Create | Subaction: None 
 | 
| Publish a portal | Public portal | Organization ID | N/A | Publish | Subaction: None 
 | 
| Delete a portal | Public portal | Organization ID | N/A | Delete | Subaction: None 
 | 
| Update a portal | Public portal | Organization ID | N/A | Update | Subaction: None Properties: 
 | 

### Asset Reviews

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create a Comment | Asset portal review comment | Comment ID | Asset portal review | Create | Subaction: None | 
| Delete a comment | Asset portal review comment | Comment ID | Asset portal review | Delete | Subaction: None | 
| Update a comment | Asset portal review comment | Comment ID | Asset portal review | Update | Subaction: None | 
| Create a review | Asset portal review | Review ID | Asset | Create | Subaction: None | 
| Delete a review | Asset portal review | Review ID | Asset | Delete | Subaction: None | 
| Update a review | Asset portal review | Review ID | Asset | Update | Subaction: None | 

## IDP

Audited actions for Intelligent Document Processing (IDP), including document actions, versions, executions, and reviewer updates.

| User action | Object type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create Document Action | Document Action | Document Action Id | Create | Subaction: none 
 | |
| Update Document Action | Document Action | Document Action Id | Update | Subaction: none 
 | |
| Add/Delete reviewers to/from a Document Action | Document Action | Document Action Id | Update | Subaction: none 
 | |
| Delete Document Action | Document Action | Document Action Id | Delete | Subaction: none 
 | |
| Document Action Version Created | Document Action Version | Document Action Version Id | Create | Subaction: none 
 | |
| Document instance is reviewed | Document Action Execution | Document Action Execution Id | Update | Subaction: none 
 | 

## Object Store v2

Audited actions for Object Store v2 resources, including stores and related operations.

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create/modify/delete store | Store | storeID | N/A | Create/modify/delete | Subaction: None | 

## RPA

Audited actions across MuleSoft RPA, including run configurations, processes, bots, credentials, and variables.

| The payload is split when it contains more than 32k (32768) characters. Split audit log entries have identical correlation IDs. | 

### Run Configurations

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create run configuration | Run configuration | Run configuration ID | N/A | Create | Subaction: None 
 | 
| Edit run configuration | Run configuration | Run configuration ID | N/A | Edit | Subaction: None 
 | 
| Delete run configuration | Run configuration | Run configuration ID | N/A | Delete | Subaction: None 
 | 
| Deploy run configuration | Run configuration | Run configuration ID | N/A | Deploy | Subaction: None 
 | 
| Publish run configuration | Run configuration | Run configuration ID | N/A | Publish | Subaction: None 
 | 
| Revoke run configuration | Run configuration | Run configuration ID | N/A | Revoke | Subaction: None 
 | 
| Pause run configuration | Run configuration | Run configuration ID | N/A | Pause | Subaction: None 
 | 
| Continue run configuration | Run configuration | Run configuration ID | N/A | Continue | Subaction: None 
 | 

### Processes

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create process | Process | Process ID | N/A | Create | Subaction: none Properties: 
 | 
| Edit process | Process | Process ID | N/A | Edit | Subaction: none Properties: 
 | 
| Delete process | Process | Process ID | N/A | Delete | Subaction: none Properties: 
 | 

### Bots

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Register bot | Bot | Bot ID | N/A | Register | Subaction: none Properties: 
 | 
| Register bot | Bot | Bot ID | N/A | Register | Subaction: none Properties: 
 | 
| Delete bot | Bot | Bot ID | N/A | Delete | Subaction: none Properties: 
 | 

### Credential Pool

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create credential | Credential | Credential ID | N/A | Create | Subaction: none Properties: 
 | 
| Edit credential | Credential | Credential ID | N/A | Edit | Subaction: none Properties: 
 | 
| Delete credential | Credential | Credential ID | N/A | Delete | Subaction: none Properties: 
 | 

### Global Variables

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create global variable | Global variable | Global variable ID | N/A | Create | Subaction: none Properties: 
 | 
| Edit global variable | Global variable | Global variable ID | N/A | Edit | Subaction: none Properties: 
 | 
| Delete global variable | Global variable | Global variable ID | N/A | Delete | Subaction: none Properties: 
 | 

### Applications

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create Application | Application | Application ID | N/A | Create | Subaction: none Properties: 
 | 
| Edit Application | Application | Application ID | N/A | Edit | Subaction: none Properties: 
 | 
| Delete Application | Application | Application ID | N/A | Delete | Subaction: none Properties: 
 | 

### Service Times

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create service time | Service time | Service time ID | N/A | Create | Subaction: none Properties: 
 | 
| Edit service time | Service time | Service time ID | N/A | Edit | Subaction: none Properties: 
 | 
| Delete service time | Service time | Service time ID | N/A | Delete | Subaction: none Properties: 
 | 

## Runtime Manager

Audited actions for applications, deployments, infrastructure resources, and runtime configuration changes.

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create application | Application | AppID | N/A | Create | Subaction: None | 
| Start application | Application | AppID | N/A | Start | Subaction: None | 
| Restart application | Application | AppID | N/A | Restart | Subaction: None | 
| Stop application | Application | AppID | N/A | Stop | Subaction: None | 
| Delete application | Application | AppID | N/A | Delete | Subaction: None | 
| Change application zip file | Application | AppID | N/A | Modify | Subaction: None | 
| Promote application from sandbox | Application | AppID | N/A | Modify | Subaction: None | 
| Change application runtime | Application | AppID | N/A | Modify | Subaction: None | 
| Change application worker size | Application | AppID | N/A | Modify | Subaction: None | 
| Change application worker number | Application | AppID | N/A | Modify | Subaction: None | 
| Enable/disable persistent queues | Application | AppID | N/A | Modify | Subaction: None | 
| Enable/disable persistent queue encryption | Application | AppID | N/A | Modify | Subaction: None | 
| Modify application properties | Application | AppID | N/A | Modify | Subaction: None | 
| Enable/disable insight | Application | AppID | N/A | Modify | Subaction: None | 
| Modify log levels | Application | AppID | N/A | Modify | Subaction: None | 
| Create/modify/delete alerts | Application | AppID | N/A | Modify | Subaction: None | 
| Enable/disable alerts | Application | AppID | N/A | Modify | Subaction: None | 
| Create/modify/delete application data | Application | AppID | N/A | Modify | Subaction: None | 
| Create/modify schedules | Application | AppID | N/A | Modify | Subaction: None | 
| Create/modify/delete tenants | Application | AppID | N/A | Subaction: None | |
| Enable/disable schedules | Application | AppID | N/A | Modify | Subaction: None | 
| Clear queues | Application | AppID | N/A | Clear | Subaction: None | 
| Enable/Disable static IP | Application | AppID | N/A | Modify | Subaction: None | 
| Allocate/release static IP | Application | AppID | N/A | Modify | Subaction: None | 
| Trigger heap dump | Application | AppID | N/A | Trigger Action | Subaction: MULE_DIAGNOSTICS_REPORT | 
| LoadBalancer Create/modify/delete | LoadBalancer | LoadBalancerID | N/A | Create/modify/delete | Subaction: None | 
| Create/modify/delete alerts V2 | Alert | AlertID | N/A | Create/modify/delete | Subaction: None | 
| Create/modify/delete VPC | VPC | vpcID | N/A | Create/modify/delete | Subaction: None | 
| Create/modify/delete VPN | VPN | vpnId | N/A | Create/modify/delete | Subaction: None | 

### Servers

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Add server | Server | ServerID | N/A | Create | Subaction: None | 
| Delete server | Server | ServerID | N/A | Delete | Subaction: None | 
| Rename server | Server | ServerID | N/A | Modify | Subaction: Rename | 
| Create server group | Server group | ServerGroupID | N/A | Create | Subaction: None | 
| Delete server group | Server group | ServerGroupID | N/A | Delete | Subaction: None | 
| Rename server group | Server group | ServerGroupID | N/A | Modify | Subaction: Rename | 
| Add server to server group | Server group | ServerGroupID | N/A | Modify | Subaction: Add server | 
| Remove server from server group | Server group | ServerGroupID | N/A | Modify | Subaction: Remove server | 
| Create cluster | Cluster | ClusterID | N/A | Create | Subaction: None | 
| Delete Cluster | Cluster | ClusterID | N/A | Delete | Subaction: None | 
| Rename cluster | Cluster | ClusterID | N/A | Modify | Subaction: Rename | 
| Add server to cluster | Cluster | ClusterID | N/A | Modify | Subaction: Add server | 
| Remove server from cluster | Cluster | ClusterID | N/A | Modify | Subaction: Remove server | 
| Deploy application | Application | ApplicationID | N/A | Deploy | Subaction: None | 
| Delete application | Application | ApplicationID | N/A | Delete | Subaction: None | 
| Start application | Application | ApplicationID | N/A | Start | Subaction: None | 
| Stop application | Application | ApplicationID | N/A | Stop | Subaction: None | 
| Redeploy application with existing file | Application | ApplicationID | N/A | Redeploy | Subaction: None | 
| Redeploy application with new file | Application | ApplicationID | N/A | Redeploy | Subaction: Update binary | 

### Private Spaces in CloudHub 2.0

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create/Modify/Delete private space | Private Space | PrivateSpaceID | N/A | Create/Modify/Delete | Subaction: None | 
| Create/Modify/Delete connection | Private Space | PrivateSpaceID | N/A | Create/Modify/Delete | Subaction: None | 
| Create/Modify/Delete VPN | Private Space | PrivateSpaceID | N/A | Create/Modify/Delete | Subaction: None | 
| Create/Modify/Delete transit gateway | Private Space | PrivateSpaceID | N/A | Create/Modify/Delete | Subaction: None | 
| Create/Modify/Delete TLSContext | Private Space | PrivateSpaceID | N/A | Create/Modify/Delete | Subaction: None | 
| Create/Modify/Delete routes | Private Space | PrivateSpaceID | N/A | Create/Modify/Delete | Subaction: None 
 | 

## Secrets Manager

Audited actions for secrets and secret groups, including creation, updates, and deletions.

| User Action | Object Type | Object | Parent | Action | Payload | 
|---|---|---|---|---|---|
| Create a secret group | secretGroup | secretGroup name | N/A | Create | Subaction:
None 
 | 
| Delete a secret group | secretGroup | secretGroup name | N/A | Delete | Subaction:
None 
 | 
| Create a secret | a secret type such as sharedSecret | secret name | N/A | Create | Subaction:
None 
 | 
| Update a secret | a secret type such as sharedSecret | secret name | N/A | Update | Subaction:
None 
 | 
| Patch a secret | a secret type such as sharedSecret | secret name | N/A | Update | Subaction:
None 
 | 

## Audit Log REST API Access

The Audit Log Query API includes pagination options and examples.

You can access the
[Audit Log REST API](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/audit-log-query-api/) from the Audit Logging Query API.

### Use a Query Loop to Make Requests in Audit Logs

The [https://exchange-files.anypoint.mulesoft.com/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/ed7300b664308faafbb61765b35004e3a0c6a08b713784704686cfa984aa7dc7.zip?response-content-disposition=attachment%3B%20filename%3Daudit-log-query-api-1.0.9-raml.zip&Expires=1771053160&Key-Pair-Id=APKAJ3T3QD2CMFEXRAJA&Signature=M5k9Sc42FNnEx3c3slWW-nDIWQPKrGdGTtMg3bL3fF6Cb4](https://exchange-files.anypoint.mulesoft.com/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/ed7300b664308faafbb61765b35004e3a0c6a08b713784704686cfa984aa7dc7.zip?response-content-disposition=attachment%3B%20filename%3Daudit-log-query-api-1.0.9-raml.zip&Expires=1771053160&Key-Pair-Id=APKAJ3T3QD2CMFEXRAJA&Signature=M5k9Sc42FNnEx3c3slWW-nDIWQPKrGdGTtMg3bL3fF6Cb4)0JqiXPJ1XeZrTjV7bGuEhMFzCeXwi7BNalYkZDmFRWPemnTdVCMa1UE2dS0rTcLIt051K1ZDhRjzPa2Unels1Ox2FQpGfGOK~z-04bTF0AZkGeNlEmrWGIPdSgq7hTA726oFYI6RnrY6Jv56EeEDOg6hcKccPt8vF1TQY6jDL4dQY3sh6prbtNOslthEZZ492k7jwe5ZKDGgUTxAVFcQrjX9n9rpdP2UQCVvzXYIlopQAgA1LgvxDW9XSIkDF8mum-6hUIJg5i1cnIRrJxgkhrscosGi4jyw__[latest version of the query API] uses cursor pagination for efficiency, but you can continue to use the [previous version of the query API](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/audit-log-query-api/minor/1.0/console/method/%23245/), which uses offset pagination and returns the total number of records.

The latest version of the API uses pagination with cursors, so you can initiate query loops using cursors. Setting the `cursorPagination` query parameter to `true` enables you to use cursor paging.

When you use cursor pagination, each response returns a cursor. The cursor corresponds to the last data entry in the response dataset. The subsequent request in the query loop uses the cursor value that was returned in the previous response.

When the dataset is empty in the response, you have reached the end of the query loop, and there is no more data to query for that time window. At that point, stop the query loop. When the dataset is empty in the response, no cursor is returned.

When you use cursor pagination, `total` isn’t returned by default, because the query loop isn’t dependent on the offset or the number of total rows.
To see the total when you use cursor paging, set the `doIncludeTotal` query parameter to true.

When the `cursorPagination` query parameter is true and you use `offset` and `cursor` in the query body, `cursor` is prioritized, and `offset` is ignored.

There is no mapping between `offset` and `cursor` values; so when you run a query loop over a time window, you can’t switch to the new parameter somewhere in the middle by using the `cursorPagination` and continue the loop. This is because when using `cursorPagination`, `offset` is ignored and the loop restarts from the beginning.

The cursor-based pagination API isn’t applicable to the CSV query. The query continues to use offset-based pagination.

This example shows a series of calls in a query loop for cursor based query:

- 
The first call doesn’t have a cursor in the body and doesn’t request the `total`. The response returns this data:`POST https://base/audit/v2/organizations/<orgId>/query?cursorPagination=true`Body: `{ "startDate":"2022-09-01T22:14:47.099Z", "endDate":"2022-11-30T23:14:47.099Z", }`Response: `{ "data": [log entries], "cursor": '123_abcd' }`You can use the cursor from the first call’s response in the next call to get the next set of rows. 
- 
The second call has a specific cursor in the request: `POST https://base/audit/v2/organizations/<orgId>/query?cursorPagination=true`Body: `{ "startDate":"2022-09-01T22:14:47.099Z", "endDate":"2022-11-30T23:14:47.099Z", "cursor": '123_abcd' }`Response: `{ "data": [logs], "cursor": '123_xyz' }`
- 
The third call is the final call in a loop. Because there are no more logs to return, the response doesn’t have a cursor and contains no data. `POST https://base/audit/v2/organizations/<orgId>/query?cursorPagination=true`Body: `{ "startDate":"2022-09-01T22:14:47.099Z", "endDate":"2022-11-30T23:14:47.099Z", "cursor": '123_xyz' }`Response: `{ "data": [] }`
- 
This example shows how to use a cursor and request the total: `POST https://base/audit/v2/organizations/<orgId>/query?cursorPagination=true&doIncludeTotal=true`Body: `{ "startDate":"2022-09-01T22:14:47.099Z", "endDate":"2022-11-30T23:14:47.099Z", "cursor": '123_abcds' }`Response: `{ "data": [logs], "cursor": '123_asdfg' "total": 50000 }`

### Access the API Using curl Commands

These are example `curl` commands for accessing the API (Windows users must download `curl` before using these commands).

Get authorization information:

`curl 'https://anypoint.mulesoft.com/audit/v2/organizations/<organization_id>/platforms?include_internal=false' -H 'Authorization: bearer <bearer_value>'`Get actions by date range:

`curl 'https://anypoint.mulesoft.com/audit/v2/organizations/<organization_id>/query?include_internal=false' -H 'Authorization: bearer <bearer_value>' -H 'Content-Type: application/json;charset=UTF-8' -H 'Accept: application/json, text/plain, */*' --data-binary '{"startDate":"2017-03-08T20:16:41.250Z","endDate":"2017-03-08T21:16:41.250Z","platforms":[],"objectTypes":[],"actions":[],"objectIds":[],"userIds":[],"ascending":false,"organizationId":"<organization_id>","offset":0,"limit":25}' --compressed ;`### Rate Limit Policy for Audit Log Query Endpoint

The Audit Log Query endpoint applies rate limits per IP in the three control planes: US, EU, and gov.

This table outlines the rate limits for each control plane:

| Control Plane | Allowed requests per minute per IP | 
|---|---|
| US | 700 | 
| EU | 40 | 
| Gov | 40 | 

If a client exceeds the rate limit for a given control plane, the Audit Log Query endpoint returns a `503 Service Unavailable` status code until the minute expires. During this time, the service is unavailable to the client.

It’s best for Audit Log Query Endpoint users to monitor their request rates and adjust their usage accordingly to avoid exceeding the rate limit. Exceeding the rate limit can make the endpoint temporarily unavailable.

## See Also

- 
[Audit Log Query API](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/audit-log-query-api)