# Grant Permission to Access an Environment | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/environment-permission-task](https://docs.mulesoft.com/api-manager/latest/environment-permission-task)

---

![permission relationships](_images/apim-permissions-relationships.png) 

# Grant Permission to Access an Environment

To be able to fully access API Manager operations within an environment, users must have the API Manager Environment Administrator permission. An API Manager Environment Administrator role is associated with tasks performed only in API Manager. You can change permissions for API Manager-related operations from Anypoint Access Management.

Regarding roles, note that:

- 
Roles and permissions assigned to a user in one particular business group are independent of the roles and permissions assigned to that same user in other business groups. 
- 
Roles are business group-specific, so ensure that you are in the correct business group for which to manage roles by clicking the menu next to your user icon. 

The following diagram illustrates the tasks enabled by having each permission:

![permission relationships](_images/apim-permissions-relationships.png) 

In this diagram, note that an Environment Administrator has access to all the functionalities and permissions.
Outer permissions provide permission to the inner permissions. For example, `Manage Alerts` gives permission to View Alerts and to View API Configuration.

API Manager supports the following additional environment-level permissions:

| Permission | Description | Notes | ||
|---|---|---|---|---|
| Deploy API Proxies | Deploy or redeploy an API proxy | Requires Runtime Manager and Hybrid access. This role enables deployment access from API Manager, but cannot guarantee that deployment is successful due to its dependency on Runtime Manager or Hybrid. | ||
| Manage Alerts | Create, edit, and delete alerts. | |||
| Manage APIs Configuration | Import APIs from Exchange | This permission also enables a user to promote an API to another environment, edit the configuration of an API, and delete APIs. 
 | ||
| Manage Contracts | Deploy, reject, and revoke contracts | This permission also gives the user permission over tiers. | ||
| Manage Policies | Create, edit, delete, enable, disable, and reorder a policy | |||
| View Alerts | List alerts and view configuration summary of an alert | |||
| View APIs Configuration | List and view APIs | List APIs, view configuration summary of an API, and download proxies. 
 | ||
| View Contracts | List contracts and their configuration | Can also list SLA tiers and their configuration. | ||
| View Policies | View a listing of policies and view the configuration of a policy | 

## Grant Permissions

To grant environment permissions to roles from API Manager:

- 
**Click Access Management**>**Users**>*a user to give permissions***API Manager**> Permissions.
- 
Select the permissions for the user and click ![blue plus icon](_images/blue-plus.png) to save the permissions: to save the permissions:

![How to set permissions in Access Management](_images/apim-user-perms.png) 

| The following API Manager 1.x roles are incompatible with API Manager 2.x: 
 |