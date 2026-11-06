# Salesforce integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/salesforce-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/salesforce-integration.html)

---

With Salesforce action connector in Amazon Quick, you can perform actions within Salesforce organizations, including managing records, querying data, and interacting with Salesforce APIs. For Amazon Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## What you can do

        
        With Salesforce integration, you can perform actions within your Salesforce organizations through the action connector.

- **Action connector**
- 
                    Create, update, and query Salesforce objects such as leads, accounts, contacts, and opportunities. 

###### Note

Salesforce integration doesn't support data access or knowledge base creation. It's designed specifically for task execution and API interactions with Salesforce objects.

## Before you begin

        
        Before you set up Salesforce integration, make sure you have the following:

- 
                Salesforce organization with appropriate permissions. 
- 
                Salesforce connected app or API access credentials. 
- 
                Amazon Quick Author or higher. 
- 
                Administrative access to configure OAuth applications (if using user authentication). 

## Step 1: Set up Salesforce connected app

        
        ###### Note

Create a connected app in Salesforce. Do not create an external client app. External client apps are not compatible with this integration.

Create a connected app in Salesforce to enable OAuth authentication with Amazon Quick.

- 
                Sign in to your Salesforce account and navigate to the Setup page using the Setup icon in the top right. 
- 
                In the Quick Find bar, enter `Apps`, then follow these steps:- Select - **External Client Apps**
- Select - **Settings**
- Under Settings, create a new connected app 
 
- 
                Choose **New Connected App**.
- 
                Choose **Create a connected app**.
- 
                In the Basic Information section, enter the following required information: - **Connected App Name**- A descriptive name for your connected app.
- **API Name**- A unique API name for your application.
- **Contact Email**- Your contact email address.
 
- 
                In the OAuth Settings section, select the following checkboxes: - **Enable OAuth Settings**
-  **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows***(recommended)*Enable this option to add an additional security layer to the Authorization Code flow. 
- **Require Secret for Web Server Flow**
- **Require Secret for Refresh Token Flow**
- **Enable Client Credentials Flow**
- **Enable Authorization Code and Credential Flow**
- **Enable Token Exchange Flow**
- **Require Secret for Token Exchange Flow**
 
- 
                Add the following required OAuth scopes: - `api`- Access Salesforce APIs
- `refresh_token`- Maintain access when user is offline
- `offline_access`- Perform requests at any time
- `full`- Full access to all data
- `web`- Web-based access
- `visualforce`- Access Visualforce pages
- `custom_permissions`- Access custom permissions
- `chatter_api`- Access Chatter API
- `wave_api`- Access Analytics API
- `eclair_api`- Access Einstein Analytics API
- `pardot_api`- Access Pardot API
- `id`- Access identity information
- `email`- Access email address
- `profile`- Access basic profile information
- `address`- Access address information
- `phone`- Access phone number
- `open_id`- Access OpenID Connect
 
- 
                Enter the callback URL in the format: `<quicksuite-url>/sn/oauthcallback`
- 
                Choose **Save**.

## Step 2: Configure consumer details and execution user

        
        Configure the consumer details and set up an execution user for the client credentials flow.

- 
                From the Manage Connected Apps page, choose **Manage Consumer Details**. You might need to verify your identity.
- 
                Copy the **Consumer Key (Client ID)**and**Consumer Secret (Client Secret)**.
- 
                Choose **Apply**.
- 
                Choose **Initial Access Token**, then choose**OK**.
- 
                Configure the execution user: - 
                        From the connected app detail page, choose **Edit**under the Action column.
- 
                        Under OAuth Policies > Refresh Token Policy, select **Immediately expire refresh token**.
- 
                        Under Client Credentials Flow, for Run As, choose the user to assign the client credentials flow. 
- 
                        Choose **Save**.
 
- 
                        

## Step 3: Set up Salesforce action connector

        
        After preparing your Salesforce connected app credentials, create the Salesforce action connector in Amazon Quick.

Salesforce integration supports action execution only - data access and knowledge base creation are not available for Salesforce systems.

- 
                In the Amazon Quick console, choose **Connectors**.
- 
                Choose the **Create for your team**tab.
- 
                Find and choose **Salesforce**.
- 
                Fill in the integration details: - 
                        **Name**- Descriptive name for your Salesforce action connector.
- 
                        **Description**(Optional) - Purpose of the action connector.
 
- 
                        
- 
                Choose your connection type: - 
                        **User authentication**- OAuth-based authentication for individual user access.
- 
                        **Service authentication**- Service-to-service authentication for application access.
 
- 
                        
- 
                Fill in the connection settings based on your selected authentication method (either user or service): - 
                        For **User authentication (OAuth)**, configure the following fields:- **Base URL**- Salesforce instance URL (for example, https://your-domain.salesforce.com).
- **Client ID**- Salesforce connected app consumer key.
- **Client Secret**- Salesforce connected app consumer secret.
- **Token URL**- Salesforce OAuth token endpoint.
- **Auth URL**- Salesforce OAuth authorization endpoint.
- **Redirect URL**- OAuth redirect URI configured in your connected app.
 
 
- 
                        
- 
                Select **Create and continue**.
- 
                Choose users to share the integration with. 
- 
                Click **Next**.

## Step 4: Associate action connector to automation groups

        
        To use Salesforce actions in automations, you must associate the action connector with your automation groups.

- 
                Navigate to your automation group settings. 
- 
                Associate the Salesforce action connector with the automation group that will use these actions. 
- 
                Create a new automation for the automation group to access Salesforce actions in your workflows. 

## Available task actions

        
        After you create your Salesforce integration, you can review the available actions for interacting with Salesforce objects. Common Salesforce actions include:

- Create, read, update, and delete (CRUD) operations on standard and custom objects. 
- Query Salesforce data using SOQL (Salesforce Object Query Language). 
- Manage leads, accounts, contacts, and opportunities. 
- Execute Apex methods and custom logic. 
- Manage cases, tasks, and activities. 
- Access reports and dashboards. 

## Share integrations

        
        You can share Salesforce action connectors with other users in your organization. Follow these steps:

- 
                After you create the integration, choose **Share integration**.
- 
                Select users or groups to share the integration with. 
- 
                Set appropriate permissions for shared access. 
- 
                Confirm sharing settings. 

Shared users can use the Salesforce integration to perform actions within the connected Salesforce organization, subject to the permissions configured in the original authentication setup.

## Manage Salesforce action connectors

        
        After you create your Salesforce action connector, you can manage it using these options:

- 
                **Edit action connector**- Update authentication settings or Salesforce instance configuration.
- 
                **Share action connector**- Make the action connector available to other users in your organization.
- 
                **Monitor usage**- View action connector activity and API usage metrics.
- 
                **Review actions**- See the complete list of available Salesforce actions.
- 
                **Delete action connector**- Remove the action connector and revoke associated authentication.