# Promoting an API Instance to Another Environment | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/promote-api-task](https://docs.mulesoft.com/api-manager/latest/promote-api-task)

---

# Promoting an API Instance to Another Environment

Before promoting an API instance to another environment, ensure that you have the `Manage APIs Configuration` permission.

To promote an entity, you must have permissions to view and manage the entity. For example, you must have the `View Policies` and `Manage Policies` permissions to promote a policy.

## Promote an API Instance from Another Environment

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
In **API Administration**, click**Add API**and select**Promote API from environment**.
- 
Select the **Source Environment**.
- 
Select the **API**by entering the name of the API into the search field.
- 
Select the **API Version**.
- 
Select the **API instance label**.
- 
Optionally, uncheck any of the **Include in Promotion**options you want to exclude.
- 
Click **Promote**.
- 
Review and update the Runtime & Endpoint Configuration details as needed and click **Save**.

Promoting an API instance affects only the API definition, not the existing deployed applications subscribed to the instance. After promoting an API, the **API Label** remains the same, but the **API Instance ID** changes.

For existing applications that must subscribe to a promoted API instance:

- 
Update the **API Instance ID**within the application.
- 
Update the application’s client ID and secret (because each environment has a different client ID and secret).