# Integration workflows - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/integration-workflows.html](https://docs.aws.amazon.com/quick/latest/userguide/integration-workflows.html)

---

The following procedures describe the general workflows for creating and managing different types of integrations in Amazon Quick.

## Creating a knowledge base

        
        Knowledge bases connect external data sources to Amazon Quick so you can ask questions about and get insights from your content.

- 
                In the Amazon Quick console, choose **Knowledge**.
- 
                Find the application you want to connect to (for example, **Google Drive**,**Microsoft OneDrive**, or**Amazon S3**) and choose the**Add**(+) icon.
- 
                Complete the authentication process for your chosen application. 
- 
                Enter a **Name**and optional description for your knowledge base.
- 
                Select the files and folders you want to include in your knowledge base using the file picker or sync options. 
- 
                Choose **Create**.

After you choose **Create**, the data sync starts
            automatically.

## Creating an action connector

        
        Action connectors enable you to perform actions in external applications directly from Amazon Quick.

- 
                In the Amazon Quick console, choose **Connectors**.
- 
                Choose the **Create for your team**tab.
- 
                Find and choose the application you want to connect to (for example, **Google Drive**,**Atlassian Confluence Cloud**, or**Slack**).
- 
                Enter a **Name**for your connector. Optionally, add a description.
- 
                Configure the connection type and authentication method. For more information about authentication options, see [Authentication methods](./quick-action-auth.html).
- 
                Review the available actions and choose **Publish**.

After successful creation, your action connector is available for use in Amazon Quick chat, workflows, and Amazon Q Apps.

## Managing existing integrations

        
        You can edit, delete, share, and manage existing integrations from the Amazon Quick console.

### To edit an integration

For knowledge bases:

- 
                    In the Amazon Quick console, choose **Knowledge**.
- 
                    Choose the knowledge base you want to edit. 
- 
                    Choose the menu icon (⋮) and select **Edit**.
- 
                    Modify the settings as needed and choose **Save changes**.

For action connectors:

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the connector you want to edit. 
- 
                    Choose the menu icon (⋮) and select **Edit**.
- 
                    Modify the connector settings as needed and choose **Save changes**.

### To delete an integration

For knowledge bases:

- 
                    In the Amazon Quick console, choose **Knowledge**.
- 
                    Choose the knowledge base you want to delete. 
- 
                    Choose the menu icon (⋮) and select **Delete**.
- 
                    In the confirmation dialog, choose **Delete**to confirm.

For action connectors:

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the connector you want to delete. 
- 
                    Choose the menu icon (⋮) and select **Delete**.
- 
                    In the confirmation dialog, choose **Delete**to confirm.

The integration is permanently removed from your account. Any dependent resources (such as knowledge bases) that rely on this integration will be impacted.

### To share an integration

From the connector or knowledge base details page, choose the menu
                icon (⋮) and select **Share**.

### Managing action connectors

Action connectors have additional management options available from the connector details page.

- **Sign in or re-connect**
- 
                        For connectors that use Default OAuth app or Custom OAuth app authentication, you must sign in to the service before you can use its actions. If you have not yet signed in, a **Sign in**button appears on the details page. After you sign in, you can use**Re-Connect**to re-authenticate if your session expires or the connection is interrupted.
- **Test action APIs**
- 
                        Choose **Test action APIs**in the Actions section of the details page to test individual actions provided by the connector. This lets you verify that the connection is working correctly and that the service responds as expected.

###### Note

The **Test action APIs** option is available for
                    action connectors only. Knowledge bases do not support action
                    testing.