# Set up integrations in the console - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/integration-console-setup-process.html](https://docs.aws.amazon.com/quick/latest/userguide/integration-console-setup-process.html)

---

The  console organizes integrations into separate categories
        based on their purpose. Use **Knowledge** to connect data
        sources for Q&A and insights. Use **Connectors** to set
        up action connectors that perform operations in external applications. The
        setup process adapts based on the integration you select, your subscription,
        and existing integrations.

## Choose integration options

        
        When you set up an integration, the console guides you based on several factors:

- 
                **Integration capabilities**– Each application supports different combinations of actions and knowledge base creation. For example, Google Drive supports both actions and knowledge base creation. Web Crawler supports knowledge base creation only.
- 
                **Subscription**– Configuring integrations requires an Enterprise subscription. This includes creating action connectors, setting up knowledge bases, and managing integration settings. Users with a Professional subscription can use integrations that have been shared with them.
- 
                **Existing integrations**– When you choose a connector that already exists, the console shows your existing connectors before offering to create new ones.

## View setup process examples

        
        The following examples show how different integrations guide you through different console setup processes.

### Google Drive – Set up a knowledge base

Google Drive supports knowledge base creation through user-managed or admin-managed authentication.

- 
                    In the console, choose **Knowledge**.
- 
                    Find **Google Drive**and choose the**Add**(+) icon.
- 
                    Choose your authentication method and complete the sign-in flow. 
- 
                    Enter a name and description for your knowledge base. 
- 
                    Select the files and folders you want to index, then choose **Create**.

### Google Drive – Set up an action connector

Google Drive also supports action connectors for performing file operations directly from .

- 
                    In the console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Find and choose **Google Drive**.
- 
                    Enter a **Name**for your connector. Optionally, choose**+ Add Description**to add a description.
- 
                    Choose your **Connection type**and**OAuth Configuration**, then complete the authentication setup.
- 
                    Review the available actions and choose **Publish**.

### Available connectors tab

The **Available** tab on the Connectors page shows
                connectors that use managed OAuth and are ready to use without additional
                configuration. Users can connect directly by choosing
                **Connect** on the connector card.

- 
                    In the console, choose **Connectors**.
- 
                    On the **Available**tab, find the connector you want to use.
- 
                    Choose **Connect**.
- 
                    Complete the sign-in flow for the application. 

### Working with existing connectors

When you choose a connector on the **Create for your
                team** tab that already exists, the console displays your
                existing connectors before offering to create a new one.

- 
                    In the console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Choose a connector that you've configured before. 
- 
                    A dialog appears showing your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.

## Integration management options

        
        After creating integrations, you can manage them through several console options:

- 
                **Edit integration**– Modify integration settings, authentication details, and configuration options.
- 
                **Delete integration**– Remove integrations with confirmation dialogs to prevent accidental deletion.
- 
                **Knowledge base management**– Separate flows for creating, editing, and deleting knowledge bases associated with your integrations.