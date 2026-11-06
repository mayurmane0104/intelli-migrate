# Adding a Scanner for Databricks Agent Bricks | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/adding-databricks-agent-bricks-scanner](https://docs.mulesoft.com/exchange/adding-databricks-agent-bricks-scanner)

---

```
PATCH /api/2.0/permissions/serving-endpoints/{endpoint_id}
{
  "access_control_list": [
    {
      "service_principal_name": "<clientId>",
      "permission_level": "CAN_QUERY"
    }
  ]
}
```
json# Adding a Scanner for Databricks Agent Bricks

Add a scanner to discover, import, and sync agents from Databricks Agent Bricks into Exchange. Then you can govern the agents and consume them in other applications.

## Before You Begin

Before adding the scanner, verify that you have these:

- 
Exchange Administrator permission 
- 
Databricks Workspace access 
- 
Workspace URL 
- 
Databricks Client ID 
- 
Databricks Client secret 
- 
Service Principal requires CAN_QUERY permission on each serving endpoint to enable full discovery and invocation. Use the Databricks Permissions API: API Endpoint Required Permission GET /api/2.0/serving-endpoints CAN_VIEW or higher GET /api/2.0/serving-endpoints/{name} CAN_VIEW or higher GET /api/2.0/serving-endpoints/{name}/openapi CAN_VIEW or higher POST /serving-endpoints/{name}/invocations CAN_QUERY or higher 

## Add a Scanner for Databricks Agent Bricks

- 
Verify that you are in the business group where you want to add the scanner. 
- 
From the sidebar in Exchange, click **Scanners**.
- 
Enter a name for the scanner. 
- 
From **Scanner Run Configuration**, complete these fields or options:**Field/Option****Value****Run Schedule**Select a frequency and time. **Sync Review**Select an option: **Auto-resolve**or**Ask to review**.
- 
From **Connection Configuration**, complete these fields:**Field****Value****Provider**Select **Databricks**.**Platform**Select **Agent Bricks**.**Service Type**Select **Agents**selected by default.**Authentication Method****OAuth**selected by default.**Workspace URL**Enter the workspace URL. **Client ID**Enter the client ID. **Client Secret**Enter the client secret. 
- 
Click **Test Connection**.If the connection fails, review the **Connection Configuration**settings. Update the settings, and then test the connection again.
- 
To send email notifications: - 
Select **Advanced Settings**and turn on**Send Email Notifications**.
- 
Enter an email address. 
 
- 
- 
Click **Add Scanner**.