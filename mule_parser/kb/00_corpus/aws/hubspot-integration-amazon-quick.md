# HubSpot integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/hubspot-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/hubspot-integration.html)

---

Access your HubSpot CRM data directly from Amazon Quick using natural language. With the HubSpot action connector, you can retrieve and list contacts, companies, deals, and tickets without leaving Amazon Quick.

HubSpot is available as a built-in connector in Amazon Quick. To set up this integration, complete the following two steps. First, prepare your HubSpot account with the required access. Then, create the connector in Amazon Quick and authenticate with your HubSpot credentials.

This connector supports Custom OAuth app authentication. For information
        about the authentication methods that Amazon Quick supports, see
        [Authentication methods](./quick-action-auth.html).

## Prerequisites

        Before you set up the integration, verify that you have the following resources and access.

- 
                An active HubSpot account with an admin role. 
- 
                Permissions to access CRM data including contacts, companies, deals, and tickets in your HubSpot account. 
- 
                A subscription that meets the requirements described in [Set up integrations in the console](./integration-console-setup-process.html).

## Verifying your HubSpot account

        Before you configure Amazon Quick, verify that your HubSpot account meets the following requirements.

- 
                Your HubSpot account is active and you can sign in to the [HubSpot sign-in page](https://app.hubspot.com/login)on the HubSpot website.
- 
                The CRM data that you want to access, including contacts, companies, deals, and tickets, is accessible to your account. 

## Configuring your HubSpot account

        The Custom OAuth app authentication method in Amazon Quick requires a MCP Auth app configured in your HubSpot developer settings.

### To configure a MCP Auth App

- 
                    Sign in to your HubSpot account. 
- 
                    Navigate to **Development**, and then**MCP Auth Apps**.
- 
                    Choose **Create MCP auth app**.
- 
                    On the **Create MCP Auth App**window, complete the following fields:- 
                            **Name**– Enter a name for your app.
- 
                            **Description**– Enter a short description.
- 
                            **Redirect URL**– Enter`https://`. Replace`region`.quicksight.aws.amazon.com/sn/oauthcallback`region`with your AWS Region, for example,`us-east-1`.
 
- 
                            
- 
                    Choose **Create**. HubSpot creates the app and generates a client ID and client secret.###### ImportantRecord the client secret and client ID. 

The client ID and client secret serve as the Client ID and Client Secret when you configure the action connector in Amazon Quick with the Custom OAuth app authentication method.

For more information, see [HubSpot MCP server](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server) on the HubSpot website.

## Setting up the integration in Amazon Quick

        After you verify your HubSpot account access, create the connector in Amazon Quick.

- 
                In the Amazon Quick console, choose **Connectors**.
- 
                Choose the **Create for your team**tab.
- 
                Choose **HubSpot**from the options available.
- 
                In the **HubSpot**dialog, enter the following fields:- 
                        **Name**– A descriptive name for your HubSpot connector.
- 
                        **Description (Optional)**– Choose**+ Add Description**to add notes about how this connector will be used.
- 
                        **Connection type**– Choose**Public network**.
 
- 
                        
- 
                For the **Custom OAuth app**authentication method, enter the following fields:- 
                        **Base URL**– This field is auto-populated as`https://mcp.hubspot.com`.
- 
                        **Client ID**– Enter the client ID from your HubSpot MCP Auth app.
- 
                        **Client Secret**– Enter the client secret from your HubSpot MCP Auth app.
- 
                        **Token URL**– This field is auto-populated as`https://api.hubapi.com/oauth/v1/token`.
- 
                        **Authorization URL**– This field is auto-populated as`https://app.hubspot.com/oauth/authorize`.
- 
                        **Redirect URL**– This field is auto-populated as`https://us-east-1.quicksight.aws.amazon.com/sn/oauthcallback`.
 
- 
                        
- 
                Choose **Next**, review the actions for HubSpot, and then choose**Next**again.
- 
                Specify who can access the connector: - 
                        To share with a team, enter a team name or group email. 
- 
                        To keep it private, leave the field blank. 
- 
                        To share with all users, toggle **Everyone in your organization**.
 
- 
                        
- 
                Choose **Publish**.

The connector appears in the **Available** panel
            with a status of **Connected**.

## Using available actions

        After you set up the connector, you can use the following read-only actions to access your HubSpot CRM data.

| Action | Description | 
|---|---|
| Get CRM Objects | Fetches multiple CRM objects of the same object type in a single request. | 
| Get properties | Fetches properties for the CRM objects. | 
| Get user details | Fetches user details. | 
| Search CRM Objects | Searches across CRM objects. | 
| Search Owners | Searches across owners. | 
| Search properties | Searches across properties. | 

###### Note

This connector supports read-only actions. The actions that you can use depend on the scopes configured in your HubSpot app.

## Troubleshooting

        To edit, share, or delete your connector, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

### Resolving authentication issues

- 
                    **Sign-in fails**– Verify that your HubSpot account is active and that you can sign in to the[HubSpot sign-in page](https://app.hubspot.com/login)on the HubSpot website. If your organization uses single sign-on (SSO), confirm that your identity provider is configured correctly.
- 
                    **Access denied**– Confirm that your HubSpot user has an admin role with permissions to access CRM data. Verify that the client ID and client secret from your app are correct and that the required read scopes are configured.