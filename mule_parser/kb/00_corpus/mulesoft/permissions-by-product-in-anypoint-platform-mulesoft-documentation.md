# Permissions by Product in Anypoint Platform | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/access-management/permissions-by-product](https://docs.mulesoft.com/access-management/permissions-by-product)

---

Organization Administrator

# Permissions by Product in Anypoint Platform

Find and assign Anypoint Platform permissions by product for teams and users. Review cross‑product dependencies and where to grant each permission. Make sure users have the exact access required for their roles.

Some products require permissions from other products to use them properly. For example, Anypoint Monitoring requires users to have certain Runtime Manager permissions in addition to Anypoint Monitoring-related permissions. See each product’s documentation to determine which permissions your users need and how to set them.

Depending on your organization’s licensing and entitlements, not all of these permissions are available during configuration.

## Access Management

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| 
 | For security reasons, assign this permission to as few users as possible. | |
| Audit Log Config Manager | Configure the retention period for audit logs across the organization. | This permission can be added only by an organization administrator at the root organization level. This permission appears only if the organization has the modern UI enabled in access management. | 
| Audit Log Viewer | View audit logs in Access Management. | 

## Agent Visualizer

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Anypoint Monitoring: Monitoring Viewer | View monitoring data for agentic assets. | |
| Exchange: Exchange Viewer | View agentic assets. | |
| API Manager: View APIs Configuration | View API nodes and relationships. | |
| API Manager: View Policies | View policies for assets. | 

## Anypoint Code Builder

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Anypoint Code Builder Developer | Create and use cloud IDE instances of Anypoint Code Builder. | This permission does not apply to Anypoint Code Builder for Desktop. This permission can be added only by an organization administrator at the root organization level. | 
| Mule Developer Generative AI User | Use natural language prompts to develop and generate flows using Agentforce for Anypoint Code Builder Generative Flows. | This permission can be added only by an organization administrator at the root organization level. | 

## API Catalog

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| API Catalog Contributor | Catalog assets and other resources using API Catalog. | 

## API Experience Hub

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| API Experience Hub Admin | View, create, modify, and delete content in API Experience Hub. | |
| API Experience Hub Users Approver | Approve or reject new user access requests and manage existing members' access. | 

## API Governance

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Governance Administrator | Manage profiles and view reports. | |
| Governance Viewer | View reports. | 

## API Manager

Depending on your organization, you might see one of these sets of permissions available for API Manager.

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| API Manager Environment Administrator | View, create, modify, and delete APIs in the specified environment. | Users can also execute any actions related to API configurations, groups, proxies, alerts, contracts, tiers, policies, automated policies, and other settings in the specified API Manager environment. | 
| API Group Administrator | View, create, modify, deprecate, and delete API groups and API group instances in the specified environment. | |
| Deploy API Proxies | Deploy API proxies in the specified environment. | |
| Manage API Alerts | View, create, modify, and delete API alerts in the specified environment. | |
| Manage APIs Configuration | View and modify API configurations in the specified environment. | |
| Manage Client Applications | Create and manage client applications in the root organization. | Users with this permission can view and modify application credentials and can add and remove client owners. This permission can be added only by an organization administrator at the root organization level. | 
| Manage Contracts | View, accept, reject, and delete contracts and tiers in the specified environment. | |
| Manage Policies | View, create, modify, and delete API policies in the specified environment. | |
| View API Alerts | View the API alerts in the specified environment. | |
| View APIs Configuration | View API configurations in the specified environment. | |
| View Client Applications | View client applications in the root organization. | This permission can be added only by an organization administrator at the root organization level. Users with this credential can’t view application secrets and can’t modify applications. | 
| View Contracts | View contracts and tiers in the specified environment. | |
| View Policies | View API policies in the specified environment. | 

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| API Creator | Create an API in the specified environment. | |
| API Versions Owner | View, modify, delete, and deprecate all API versions in the specified business group. | |
| Portals Viewer | View all portals in the specified business group. | 

## API Visualizer

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Visualizer Editor | View, create, modify, and delete content in Anypoint Visualizer. | This permission can be added only by an organization administrator at the root organization level. | 

## Data Gateway

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Data Gateway Administrator | Full access to Data Gateway Designer. | |
| Data Gateway Viewer | Read-only access to Data Gateway Designer. | 

## DataGraph

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Contribute | 
 | |
| Consume | 
 | |
| Operate | 
 | |
| DataGraph Admin | 
 | |
| DataGraph Project - Contributor | 
 | |
| DataGraph Project - Operator | View customer-facing logs and set a dedicated load balancer URL for Anypoint Datagraph in a specific project. | |
| DataGraph Project - Admin | 
 | 

## Design Center

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Design Center Developer | View, create, and manage all projects within a business group. | Use this permission to set up administrators for all projects within a specific business group. | 
| Design Center Creator | Create projects in Design Center from the navigation panel and view all projects created or shared with the user. | Use this permission to invite users to create, edit, and maintain your projects. | 
| Design Center Viewer | View all Design Center projects within a business group and test projects with the Mocking Service. | Users with this permission can’t create new projects, edit or rename existing projects, or share projects with another user. Assign this permission to those who consume your project in a specific business group. | 

### Design Center Project-level Permissions

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Project Administrator | Manage and share a Design Center project within a business group. | Use this permission to set up administrators for all the projects within a specific business group. | 
| Project Editor | Edit a Design Center project within a business group. | Use this permission to invite users to create, edit, and maintain your projects. | 
| Project Viewer | View a Design Center project within a business group and test projects with the Mocking Service. | Users with this permission can’t create a new project, edit or rename the existing project, or share the project with another user. Assign this permission to those who consume your project in a specific business group. | 

## Enhanced MuleSoft Experience

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Any of these permissions: 
 | View services | View services in the portfolio and open the catalog overview in Anypoint Exchange. | 
| Any of these permissions: 
 | Create services | Register MCP servers, agents, LLMs, or APIs. | 
| API Manager: API Creator | Create instances | Create or add instances. | 
| API Manager: View APIs Configuration | View instances | View instances for services and open the  | 
| API Manager: Edit APIs Configuration | Edit instances | Edit instances for services. | 
| Any of these permissions: 
 | Create scanners | Create scanners from  To view the  | 
| Any of these permissions: 
 | View monitoring | Open the  | 
| API Manager: View Policies | View policies | View and apply policies on instances, and access policies from the  | 
| API Manager: Manage Policies | Apply policies | Edit policy configurations and add policies. | 
| These permissions: 
 | Use the  | Apply optimization strategies using policies, view policies, view Exchange assets, and query metrics. The Mule Developer Generative AI User permission is required to enable AI features. | 
| Anypoint Code Builder: Mule Developer Generative AI User | Send prompts to agent | Use the native agent. | 
| Any of these permissions: 
 | Create governance strategies | Create governance strategies. To view and create governance strategies, you need the Governance Administrator permission for  | 
| Any of these permissions: 
 | View governance reports | View governance reports at the service and governance strategy levels. To see the conformance badge and whether rulesets passed or failed, you need the Exchange Viewer permission. To view or export detailed governance reports, including violations, warnings, and rule breakdowns, you need the Governance Viewer permission. | 
| Any of these permissions: 
 | View alerts | View API alerts in API Manager and read alerts in Runtime Manager. | 
| Any of these permissions: 
 | Manage alerts | Manage API alerts in API Manager and alerts in Runtime Manager. | 

## Exchange

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Exchange Administrator | 
 | Users with this permission have the same access as users with the Exchange contributor and Exchange viewer permissions, and access to share an asset with another user, deprecate an asset, and delete an asset. Use this permission to set up Exchange administrators for all assets within a specific business group. | 
| Exchange Contributor | View, create, and download assets within a business group. Users with this permission can edit asset portal content in an existing asset version. | Use this permission to invite users to edit and maintain your asset portal descriptions. | 
| Exchange Viewer | View and download assets within a business group. | Users with this permission can’t add new assets, edit asset portal content, or share an asset with another user. Assign this permission to those who consume your assets in a specific business group. | 
| Exchange Creator | Create new assets within a business group’s catalog. | A user with this permission can’t modify assets or asset versions created by other users in the business group. Once the users with this permission create an asset, the Asset Administrator permission is automatically assigned for the assets they create. The Asset Administrator permission allows these users to modify only the assets that they create. Use this permission to restrict the modification of assets except for assets created by this user while allowing all developers across all teams in a business group to create new assets in Exchange. | 
| Asset Viewer | View and download an asset. | Users with this permission can’t edit asset portal content or share an asset with another user. Use this permission to invite a user outside your business group to view and download an asset. | 
| Asset Contributor | View, add a new version, and download an asset. | Use this permission to invite a user outside of your business group to view, download, and add edit portal content for an asset. | 
| Asset Administrator | View, create, download, deprecate, and delete an asset. | Users with this permission have the same access as users with the Exchange Administrator permission, but on only a single asset. This permission is assigned by default to an asset creator. Use this permission to extend administrator permissions for an asset to an additional user. | 
| Generate Asset Documentation with AI | Generates documentation for existing asset versions within a business group using generative AI features. | 

## IDP

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Manage Actions | Complete access to IDP and assigns reviewer permission by default for every document action. | |
| Build Actions | Create, edit, and publish document actions and assign reviewers to the actions. | |
| Execute Published Actions | Execute a published document action and retrieve the results of the execution. | |
| Configure Connected Apps | Configure a connected app to communicate with IDP. | 

## Monitoring

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Monitoring Administrator | View, create, modify, and delete content in Anypoint Monitoring. | 
 | 
| Monitoring Viewer | View but not modify content in Anypoint Monitoring. | 
 | 
| Telemetry Exporter Administrator | 
 | Assign this permission at the root organization level. Availability of this permission depends on your organization’s subscription tier. | 
| Telemetry Exporter Configurations Manager | 
 | Availability of this permission depends on your organization’s subscription tier. | 

## MQ

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| View clients | View all client apps, including client app IDs and client secrets for each client app. | |
| View destinations | 
 | |
| Clear destinations | 
 | |
| Manage clients | 
 | |
| Administer destinations | 
 | |
| Manage destinations (deprecated) | 
 | This permission is deprecated. Assign these permissions instead: 
 | 
| Destination subscriber for given environment | 
 | |
| Destination publisher for given environment | 
 | |
| Read MQ Stats | View organization and environment statistics. | 

## Object Store v2

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Manage stores | Create, read, update, and delete stores. | |
| Manage stores data | Perform all store operations including data, partition, and confirmation APIs. | |
| View stores | Read store details. | |
| Manage store clients | Manage all clients of a cloud store. | This permission doesn’t apply to Object Store v2. | 
| View store clients (object store only) | View all clients of a cloud store. | This permission doesn’t apply to Object Store v2. | 
| Store Metrics Viewer | Retrieve Object Store v2 metrics using the Object Store v2 Stats API. | 

## Partner Manager

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Partner Manager Administrator | Have complete access to the host, partner, message flow configurations, and transaction activity. | |
| View Host, Partners and Message Flows | Have view-only access to the host, partner, and message flow configurations. | This user can’t view transaction activity. | 
| Manage Partners and Message Flows | 
 | This user can’t view and manage transaction activity. | 
| Manage Activity | View and manage transaction activity. | This user can’t view or modify either partner or message flow configurations. | 
| Manage Host | Create, modify, and delete host configurations. | This user can’t view or modify partner configurations or transaction activity. This access applies even if the user has the Organization Administrator permission. | 
| View Activity | Have view-only access to transaction activity. | This user can’t view or modify either partner or message flow configurations. | 

## RPA

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| RPA Administrator | Perform all tasks, except those provided by the RPA Project Manager permission. | A user with this permission can only view or administer automation projects if the user is part of the process team. | 
| RPA Automations Designer | RPA developer, citizen technologist, or knowledge source (such as a business analyst or process owner): In RPA Manager: 
 | ## Replaces these permissions
 | 
| RPA Automations Contributor | RPA developer, citizen technologist, or knowledge source (such as a business analyst or process owner): 
 | ## Replaces these permissions
 | 
| RPA Automations Manager | RPA developer, citizen technologist, or knowledge source (such as a business analyst or process owner): 
 | ## Replaces these permissions
 | 
| RPA Bots Manager | In RPA Manager: 
 | ## Replaces these permissions
 | 
| RPA Evaluations Viewer | In RPA Manager: 
 | ## Replaces these permissions
 | 
| RPA Evaluations Contributor | In RPA Manager: 
 | ## Replaces these permissions
 | 
| RPA Evaluations Manager | In RPA Manager: 
 | ## Replaces these permissions
 | 
| RPA Operations Viewer | In RPA Manager: 
 | ## Replaces these permissions
 | 
| RPA Operations Manager | In RPA Manager: 
 | ## Replaces these permissions
 | 
| RPA Performance Analyzer | In RPA Manager: 
 | ## Replaces these permissions
 | 
| RPA Project Manager | Be assigned as a project manager of automation projects in RPA Manager. For a user to function as a project manager, the user must also have one of these permissions: 
 | Replaces the RPA Project Management permissions. | 

## Runtime Manager

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| CloudHub Network Administrator | Manage CloudHub and CloudHub 2.0 network resources. | |
| CloudHub Network Viewer | View CloudHub and CloudHub 2.0 network resources. | |
| Delete Applications | Delete applications in a specific environment. | |
| Download Applications | Download application files in a specific environment. | |
| Manage Alerts | Create, update, and delete application alerts in a specific environment. | |
| Manage Application Data | Create and delete application data in a specific environment. | |
| Manage Queues | Clear application queues in a specific environment. | |
| Read Runtime Fabric | Query Runtime Fabric instances in the organization. | |
| Manage Runtime Fabrics | read, create, update, and delete Runtime Fabric resources. | |
| Manage Runtime Fabric | Read, create, update, and delete Runtime Fabric resources. | |
| Manage Schedules | Run and update application schedules in a specific environment. | |
| Manage Settings | Update application settings in a specific environment. | |
| Manage Tenants | Create, update, and delete application tenants in a specific environment. | |
| Read Alerts | View alerts in a specific environment. | |
| Read Applications | View applications in a specific environment. | |
| Manage Servers | Create, update, and delete server and Omni Gateway resources. | |
| Read Servers | View server and Omni Gateway resources. | |
| Manage Application Flows | Update flows. | |
| Create Applications | Create applications in a specific environment. | |
| Restart Applications | Restart applications deployed to Runtime Fabric in a specific environment. | 

## Secrets Manager

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Grant access to secrets | Browse, read metadata and grant access to secrets in a specific environment. | |
| Manage secret groups | 
 | |
| Read secrets metadata | Browse and read metadata of secrets in a specific environment. | |
| Write secrets | Upload, create, modify secrets in a specific environment. | 

## Tokenization

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Manage Tokenization Services | View, create, edit, and delete tokenization resources. | |
| Manage Tokenization Formats | View, create, edit, and delete tokenization formats. | 

## Usage

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Usage Viewer | View usage reports. | This permission can be added only by an organization administrator at the root organization level. |