# QuickBooks integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quickbooks-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/quickbooks-integration.html)

---

With the QuickBooks action connector, you can access QuickBooks Online directly in Amazon Quick through natural language. You can manage invoices, customers, vendors, accounts, and generate financial reports without leaving Amazon Quick.

Amazon Quick supports multiple authentication methods for QuickBooks. Choose the method that best fits your organization's security requirements.

- 
            **Default OAuth app**– Uses an AWS-managed OAuth application. No additional credentials are needed. Users authenticate directly with their Intuit account.
- 
            **Custom OAuth app**– Uses a customer-managed application registered in the Intuit Developer portal. This option gives your organization full control over the OAuth configuration.

For more information about the authentication methods that Amazon Quick supports, see
        [Authentication methods](./quick-action-auth.html).

## Before you begin

        Make sure that you have the following before you set up the integration.

- 
                An active QuickBooks Online account with access to the company data that you want to use. 
- 
                For **Custom OAuth app**: Access to the[Intuit Developer portal](https://developer.intuit.com/)on the Intuit website to create an app.
- 
                For Amazon Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## Configuring QuickBooks

        If you are using **Default OAuth app**
            authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#quickbooks-quicksuite-setup).

For Custom OAuth app authentication, complete the following steps in the Intuit Developer portal before configuring Amazon Quick.

### Create an Intuit Developer app (Custom OAuth app)

Create an app in the Intuit Developer portal to obtain the client
                credentials that you need for Amazon Quick. For more information, see
                [OAuth 2.0](https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0)
                on the Intuit Developer website.

- 
                    Sign in to the [Intuit Developer portal](https://developer.intuit.com/)on the Intuit website.
- 
                    From your workspace, choose the plus (+) button to create a new app. 
- 
                    For **Type**, select the QuickBooks Online platform.
- 
                    Enter an **App name**for your application.
- 
                    For **Permissions**, under**QuickBooks Online and Payments**, select the authorization scopes that your integration requires. For the recommended scopes, see[Recommended scopes](#quickbooks-oauth-scopes).
- 
                    Complete the app creation. On the confirmation page, choose **Show credentials**to view your development credentials.
- 
                    Record the following values. You need them when you configure Amazon Quick. - 
                            **Client ID**
- 
                            **Client secret**
 
- 
                            
- 
                    In the app settings, choose the **Redirect URIs**tab. Add the Amazon Quick callback URL:`https://``{region}`.quicksight.aws.amazon.com/sn/oauthcallback
- 
                    Choose **Save**.

### Recommended scopes

When you create an Intuit Developer app, select the following authorization scopes based on the actions that you want to use.

| Scope | Description | 
|---|---|
| `com.intuit.quickbooks.accounting` | Accesses QuickBooks Online accounting data, including invoices, customers, vendors, accounts, and financial reports. | 
| `com.intuit.quickbooks.payment` | Accesses QuickBooks Online payment data, including purchases and payment transactions. | 
| `openid` | Authenticates the user's identity. | 
| `email` | Reads the user's email address. | 
| `profile` | Reads the user's profile information. | 
| `phone` | Reads the user's phone number. | 
| `address` | Reads the user's address. | 

###### Note

The `openid`, `email`,
                    `profile`, `phone`, and
                    `address` scopes are used for user authentication
                    with Custom OAuth app.

## Setting up the connector in Amazon Quick

         
            ### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
                directly from the **Available** tab without additional
                configuration.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    On the **Available**tab, find**QuickBooks**and choose**Connect**.
- 
                    Complete the QuickBooks sign-in flow and grant the requested permissions. 

To configure a connector with Custom OAuth app instead,
                use the **Create for your team** tab as described
                below.

### Create from the Create for your team tab

After you complete any required QuickBooks configuration, create the connector in Amazon Quick.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Find and choose **QuickBooks**.###### NoteIf a QuickBooks connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.
- 
                    Enter a **Name**for your connector. Optionally, choose**+ Add Description**to add a description.
- 
                    For **Connection type**, choose**Public network**.
- 
                    For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.- 
                            For **Default OAuth app**:No additional credentials are needed. Choose **Next**to continue.
- 
                            For **Custom OAuth app**, configure the following fields:- 
                                    **Base URL**(Optional) – The QuickBooks API base URL. Example:`https://quickbooks.api.intuit.com`
- 
                                    **Client ID**– The client ID from your Intuit Developer app.
- 
                                    **Client secret**– The client secret from your Intuit Developer app.
- 
                                    **Token URL**– The token endpoint. Example:`https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer`
- 
                                    **Authorization URL**– The authorization endpoint. Example:`https://appcenter.intuit.com/connect/oauth2`
- 
                                    **Redirect URL**– Pre-filled with the Amazon Quick callback URL.
 
- 
                                    
 
- 
                            
- 
                    Choose **Next**.
- 
                    If you chose **Default OAuth app**or**Custom OAuth app**, an Intuit authorization window opens. Review the requested permissions and choose**Connect**.
- 
                    On the **Review**page, review the available actions for the connector. Choose**Next**.
- 
                    On the **Publish**page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.
- 
                    Choose **Publish**.

## Available actions

        After you set up the connector, the following actions are available.

| Category | Action | Description | 
|---|---|---|
| Queries | Search Entities | Searches across QuickBooks entities using a query. | 
| Accounts | Get Account Details | Retrieves details for a specific account by query. | 
| Accounts | Get Account | Retrieves a specific account by ID. | 
| Accounts | Create Account | Creates a new account in the chart of accounts. | 
| Invoices | Get Invoice | Retrieves a specific invoice by ID. | 
| Invoices | List Invoices | Lists invoices with optional filtering. | 
| Invoices | Create Invoice | Creates a new invoice. | 
| Customers | Get Customer | Retrieves a specific customer by ID. | 
| Customers | Create Customer | Creates a new customer record. | 
| Vendors | Create Vendor | Creates a new vendor record. | 
| Purchases | Create Purchase | Creates a new purchase transaction. | 
| Purchases | Create Bill | Creates a new bill from a vendor. | 
| Journal entries | Create Journal Entry | Creates a new journal entry. | 
| Reports | Get Profit and Loss Report | Generates a profit and loss report. | 
| Reports | Get Customer Balance Report | Generates a customer balance summary report. | 
| Reports | Get Customer Balance Detail | Generates a detailed customer balance report. | 
| Reports | Get Vendor Balance Report | Generates a vendor balance summary report. | 
| Reports | Get Vendor Balance Detail | Generates a detailed vendor balance report. | 
| Reports | Get General Ledger Report | Generates a general ledger report. | 
| Batch operations | Batch Execute Operation | Runs multiple operations in a single batch request. | 
| Company | Get Company Info | Retrieves information about the connected company. | 

###### Note

The actions that you can use depend on the company data accessible to the authenticated user.

## Managing and troubleshooting

        To edit, share, or delete your connector, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

### Authentication issues

- 
                    **Sign-in fails (Default OAuth app or Custom OAuth app)**– Verify that your Intuit account is active and that you can sign in to[quickbooks.intuit.com](https://quickbooks.intuit.com)on the Intuit website directly. For Custom OAuth app, confirm that the redirect URI in your Intuit Developer app matches the Amazon Quick callback URL.
- 
                    **Invalid client credentials (Custom OAuth app)**– Verify that the Client ID and Client secret match the values in your Intuit Developer app. You can view your credentials from the app settings in the Intuit Developer portal.
- 
                    **Insufficient permissions**– Verify that the scopes configured for your Intuit Developer app include the permissions required for the actions that you want to use. See[Recommended scopes](#quickbooks-oauth-scopes).