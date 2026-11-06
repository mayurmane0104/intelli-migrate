# Managing Permissions for Anypoint Monitoring | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/am-permissions](https://docs.mulesoft.com/monitoring/am-permissions)

---

Monitoring Administrator

# Managing Permissions for Anypoint Monitoring

Anypoint Monitoring has product-specific permissions that control access to its assets:

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| View, create, modify, and delete content in Anypoint Monitoring. | 
 | |
| Monitoring Viewer | View but not modify content in Anypoint Monitoring. | 
 | 
| Telemetry Exporter Administrator | 
 | Assign this permission at the root organization level. Availability of this permission depends on your organization’s subscription tier. | 
| Telemetry Exporter Configurations Manager | 
 | Availability of this permission depends on your organization’s subscription tier. | 

In addition to Monitoring Administrator and Anypoint Monitoring Viewer permissions, asset-specific permissions are required to view and read API and app data for some deployments. For example, if you have the Anypoint Monitoring Viewer permission and want to view Anypoint Monitoring data on a hybrid Mule app deployment, you must also have the Read Applications permission (from Runtime Manager) in the same environment that the app is deployed to.

| Deployment Type | Permission | Grants the Ability to | Permission Type | 
|---|---|---|---|
| Hybrid Deployment Data | Read Applications | View app data for hybrid deployments. See also,  | |
| Omni Gateway (formerly Flex Gateway) Deployment Data | View API Alerts | View the API alerts for Flex API data. | |
| Read Servers | View server and Omni Gateway (formerly Flex Gateway) resources. |