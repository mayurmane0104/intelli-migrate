# Amazon Quick Slack extension - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/slack-extension.html](https://docs.aws.amazon.com/quick/latest/userguide/slack-extension.html)

---

The Quick extension for Slack integrates AI-powered assistance directly into your team communication workflows. Users can access Quick knowledge and capabilities within Slack channels and direct messages without switching between applications.

The Slack extension enables users to:

- 
                Add Amazon Quick as a collaborator using **@Amazon Quick**mentions.
- 
                Get conversation summaries and insights. 
- 
                Access organizational knowledge bases and documents directly from Slack channels. 
- 
                Generate notes and action items from discussions in Slack threads. 
- 
                Get help with data analysis and report generation using uploaded files. 

###### Important

- 
                    When Amazon Quick is used in public Slack channels, responses are based on the invoking user's permissions. This may include content that other channel members aren't authorized to access. Carefully evaluate using Amazon Quick in public channels to prevent unintended exposure of sensitive information. 
- 
                    Amazon Quick does not use your user data for service improvement or for training its underlying large language models (LLMs). 

## Prerequisites for Slack extension

            Before adding the Amazon Quick Slack Extension, administrators must complete the following requirements:

- 
                    Have a paid Slack workspace. 
- 
                    Have admin access to your Slack workspace. 
- 
                    Get started with Amazon Quick. 
- 
                    Your Slack workspace ID (must start with 'T' and be alphanumeric). One way to find your Slack workspace ID is by navigating to your Slack workspace and starting a chat with the Slack Developer Tools app running the `/sdt whoami`command. For more information, see[Locate your Slack URL or ID](https://slack.com/help/articles/221769328-Locate-your-Slack-URL-or-ID)in the Slack help center.

If you configured the authentication to connect to Amazon Quick with IAM Identity Center, complete the following additional steps:

- 
                Ensure you have an IAM Identity Center instance enabled on your AWS account. 
- 
                If you are connecting an external IAM provider to IAM Identity Center, ensure that every user under your IAM provider configuration has an email associated with them. 
- 
                If you are using Entra ID, set up SCIM identity propagation between the Microsoft Entra ID instance and IAM Identity Center. For detailed steps, see [Configure SAML and SCIM with Microsoft Entra ID and IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/azure-ad-idp.html).

## Configure Slack extension access

            As an administrator, you must allow your Amazon Quick Slack extension to connect to your Amazon Quick application environment. You can use the Amazon Quick console to manage extension access configurations.

### User attribute mapping

When you configure a Slack extension, user identity is mapped by default using the following attributes:

- 
                        **Amazon Quick user attribute**- Email address is used to map Amazon Quick users to their corresponding Slack accounts. The system uses the email address to establish the connection between user identities.
- 
                        **Slack user attribute**- User Profile Email is used to match against Slack user accounts. This maps to the email address associated with the user's Slack profile.

These default mappings ensure secure and accurate user identification across both platforms without requiring additional configuration.

###### Topics

### Add Slack extension access for accounts using IAM Identity Center

Configuring extension access with IAM Identity Center requires completing steps specific to your identity provider (Entra ID or Okta) followed by common setup steps in AWS.

#### Configure IAM Identity Center with Entra ID

Follow these steps only if you are using IAM Identity Center with Entra ID to set up and configure an Azure tenant on your Microsoft Azure portal:

###### To set up an Azure tenant

- 
				                In the Azure account, create a new app registration. - 
				                        Go to **App registrations**.
- 
				                        In the **App registrations**screen, choose**New registration**. Under the**Supported account types**option, choose**Accounts in this organizational directory only (Personal use only - Single tenant)**. Once finished, choose**Register**.
- 
				                        Note the client ID. You will need this later. 
- 
				                        Create a client secret for the app registration and keep note of it. You will need this later. 
 
- 
				                        
- 
				                Add callback URLs for each Region in which your Slack extension will be installed. - 
				                        Navigate to the app registration's **Authentication**tab.
- 
				                        Choose **Platform Configurations**,**Add a platform**.
- 
				                        Choose **Web**.
- 
				                        Compose a callback URL using the following format, replacing `your-region`with your Amazon Quick instance Region. The Slack extension supports the following Regions:`ap-southeast-2`,`eu-west-1`,`us-west-2`, and`us-east-1`.`qbs-cell001.dp.appintegrations.``your-region`.prod.plato.ai.aws.dev/auth/idc-tti/callback
- 
				                        Insert the callback URL as the redirect URI and choose **Configure**when done.
 
- 
				                        

Follow these steps to configure a Trusted Token Issuer on your IAM Identity Center instance in your AWS Console:

###### To configure a Trusted Token Issuer

- 
				                Go to your AWS account and navigate to your IAM Identity Center instance. 
- 
				                Navigate to **Settings**,**Authentication**.
- 
				                Choose **Create trusted token issuer**.
- 
				                Add the issuer URL, which should follow this template, where `Tenant ID`refers to your Entra tenant ID:`login.microsoftonline.com/``Tenant ID`/v2.0###### NoteThe issuer URL should be the OIDC discovery endpoint of your identity without the well-known document URI path. If you include the well-known document URI path, this will not work. See Trusted token issuer configuration settings. 
- 
				                Choose **Email**as the Identity Provider attribute and IAM Identity Center attribute.
- 
				                Note the trusted token issuer ARN. You will need this in a later step. 

After completing these Entra ID-specific steps, proceed to the [Complete AWS Configuration (all providers)](#complete-aws-config-slack) section below.

#### Configure IAM Identity Center with Okta

Follow these steps only if you are using IAM Identity Center with Okta to set up and configure your App Integration in the Okta Admin console:

###### To set up an Okta Application

- 
				                In your Okta account, create a new Okta App Integration. - 
				                        In your Okta Admin console, navigate to **Applications**>**Applications**.
- 
				                        Click on **Create App Integration**.
- 
				                        For the Sign-in method, select **OIDC - OpenID Connect**.
- 
				                        For the Application type, select **Web Application**.
- 
				                        Click on **Next**.
- 
				                        Provide an App integration name. 
- 
				                        Under **Grant type**>**Core grants**, ensure**Authorization Code**and**Refresh Token**are selected.
- 
				                        Under **Grant type**>**Advanced**>**Other grants**, ensure**Implicit (hybrid)**is selected.
 
- 
				                        
- 
				                Add callback URIs for each Region in which your Slack extension will be installed - 
				                        Compose a callback URI using the following format, replacing `your-region`with your Amazon Quick instance Region for each region where you wish to configure the extension. The Slack extension supports the following Regions:`ap-southeast-2`,`eu-west-1`,`us-west-2`, and`us-east-1`.`qbs-cell001.dp.appintegrations.``your-region`.prod.plato.ai.aws.dev/auth/idc-tti/callback
- 
				                        Under **Sign-in redirect URIs**, click on**Add URI**and paste each of the URIs you generated from the previous step.
 
- 
				                        
- 
				                Provide your organization access to the app: - 
				                        Under **Assignments**>**Controlled access**, select the groups in your organization that need to have access.
- 
				                        Under **Assignments**>**Enable immediate access**, select**Enable immediate access with Federation Broker Mode**.
- 
				                        Click on **Save**.
 
- 
				                        
- 
				                Note down the **Client ID**and**Client Secret**for the app integration you just created. You will need this in the next steps.

###### To configure a Trusted Token Issuer

- 
				                Go to your AWS account and navigate to your IAM Identity Center instance. 
- 
				                Navigate to **Settings**>**Authentication**.
- 
				                Choose **Create trusted token issuer**.
- 
				                Add the issuer URL, which should follow this template, where `yourOktaDomain`refers to the okta URL for your organization, which may look like`your-organization.okta.com`:`https://{``yourOktaDomain`}/oauth2/default###### NoteThe issuer URL should be the OIDC discovery endpoint of your identity without the well-known document URI path. If you include the well-known document URI path, this will not work. See Trusted token issuer configuration settings. 
- 
				                Choose **Email**as the Identity Provider attribute and IAM Identity Center attribute.
- 
				                Note the trusted token issuer ARN. You will need this in a later step. 

After completing these Okta-specific steps, proceed to the [Complete AWS Configuration (all providers)](#complete-aws-config-slack) section below.

#### Complete AWS Configuration (all providers)

Follow these steps to set up permissions on AWS Console:

###### To set up permissions

- 
				                Navigate to Secrets Manager on AWS console. 
- 
				                Choose **Store a new secret**.
- 
				                Choose **Other type of secret**and choose the**Plaintext**tab.
- 
				                Your secret should be in the following format and use the app registration client ID and app registration client secret that you saved from the earlier steps: `{ "client_id":"``Your app registration client ID`", "client_secret":"`Your app registration client secret`" }
- 
				                Navigate to the secret you just created and save the ARN for later. 
- 
				                Now navigate to IAM on AWS console. 
- 
				                Choose **Access Management**,**Roles**in the left navigation bar.
- 
				                Choose **Create role**.
- 
				                Choose **Custom trust policy**.
- 
				                Configure the role to trust our service principal for the relevant Region that you selected when configuring your identity provider app integration by adding the following statement replacing `your-region`with the Region you chose when creating your identity provider app integration:`{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "``your-region`.prod.appintegrations.plato.aws.internal" }, "Action": "sts:AssumeRole", "Condition": {} } ] }
- 
				                Choose **Next**.
- 
				                Provide a name and description and choose **Create role**.
- 
				                Navigate to the role you just created and choose it. 
- 
				                Choose **Add Permissions**,**Create inline policy**.
- 
				                Choose **JSON**.
- 
				                Configure the role with permissions to read secrets from Secrets Manager and permissions to invoke `sso:DescribeTrustedTokenIssuer`by adding the following statement:`{ "Version": "2012-10-17", "Statement": [ { "Sid": "BasePermissions", "Effect": "Allow", "Action": [ "secretsmanager:GetSecretValue", "sso:DescribeTrustedTokenIssuer" ], "Resource": "*" } ] }`
- 
				                Provide a policy name and choose **Create policy**.
- 
				                Copy and save the ARN of the IAM role you created for later. You will need it in the next steps. 

Now you can follow these steps to create a new extension access configuration that will allow Amazon Quick to integrate with your Slack environment:

###### To create an extension access configuration

- 
				                Sign in to the Amazon Quick console. 
- 
				                In the top right, choose the profile picture icon. 
- 
				                From the drop-down menu, choose **Manage account**.
- 
				                Under **Permissions**, choose**Extension access**.
- 
				                In the top right, choose **New extension access**.
- 
				                If this is your first time setting up extension access, you are prompted to complete the **Trusted Token Issuer Setup**. Configure the following fields and then choose**Next**:- 
				                        **Trusted Token Issuer ARN**– Enter the trusted token issuer ARN that you noted from the earlier steps.
- 
				                        **Aud claim**– Enter the client ID from your app registration (Entra ID) or app integration (Okta) that you saved from the earlier steps.
 ###### NoteThis is a one-time setup that establishes a trusted identity source for all extensions. Once completed, you won't need to do this again for other extension accesses. 
- 
				                        
- 
				                Select **Slack**. Then, choose**Next**.
- 
				                Configure the following fields: - 
				                        **Name**- A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Slack extension (maximum 512 alphanumeric characters, hyphens allowed but no spaces).
- 
				                        **Description (optional)**- A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration (maximum 1000 characters).
- 
				                        **Slack Workspace ID**- Enter your Slack workspace identifier. Workspace IDs must start with 'T' and be between 1 and 256 alphanumeric characters.
- 
				                        **Secrets Role ARN**- Paste the ARN of the IAM role you created from the previous steps.
- 
				                        **Secrets ARN**- Paste the ARN of the Secrets Manager secret you created from the previous steps.
 
- 
				                        
- 
				                Choose **Add**to save the new access configuration.A success message will open up on the top right of your screen. 
- 
				                From the success message, choose **View extensions**to finish installing your extension.###### NoteYou can also navigate to the installation screen from **Connections**>**Extensions**in the Amazon Quick menu.

Once created, this extension access configuration enables authors and other admin in your organization to create and deploy Amazon Quick extensions within your Slack environment.

###### Note

For your end users to begin using your Slack extension, an admin or author must finish deploying a extension after you configure extension access. Notify your authors that they can view, edit, and complete installation of this extension under **Extensions** in the left navigation once it has been shared. To learn how to do this see Installing your Slack extension in the Slack extension author guide.

### Add Slack extension access for accounts using other authentication methods

Follow these steps to create a new extension access configuration that will allow Amazon Quick to integrate with your Slack environment.

- 
                        Sign in to the Amazon Quick console. 
- 
                        In the top right, select the profile picture icon. 
- 
                        From the drop-down menu, select **Manage account**.
- 
                        Under **Permissions**, select**Extension access**.
- 
                        In the top right, select **New extension access**.
- 
                        Select Slack, then, **Next**.
- 
                        Configure the following fields: - 
                                **Name**- A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Slack extension (maximum 512 alphanumeric characters, hyphens allowed but no spaces).
- 
                                **Description**(optional) - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration (maximum 1000 characters).
- 
                                **Slack Workspace ID**- Enter your Slack workspace identifier. Workspace ID must start with T and be between 1 and 256 alphanumeric characters long.
 
- 
                                
- 
                        Select **Add**to save the new access configuration.A success message will open up on the top right of your screen. 
- 
                        From the success message, select **View extensions**to finish installing your extension.###### NoteYou can also navigate to the installation screen from **Connections**>**Extensions**in the Amazon Quick menu.

Once created, this extension access configuration enables authors and other admins in your organization to deploy Amazon Quick Slack extensions in their workspace.

###### Note

For your end users to begin using your Slack extension, an
                        admin or author must finish deploying a extension after you configure
                        extension access. Notify your authors that they can view, edit, and complete
                        installation of this extension under **Extensions** in the
                        left navigation once it has been shared. To learn how to do this see [Installing your Slack extension in
                            the Slack extension author guide](https://docs.aws.amazon.com/quicksuite/latest/userguide/slack-extension-author-guide.html#add-extensions-slack).

### Edit Slack extension access

Use these steps to modify the configuration settings of an existing Slack extension access.

- 
                        Sign in to the Amazon Quick console. 
- 
                        In the top right, select the profile picture icon. 
- 
                        From the drop-down menu, select **Manage account**.
- 
                        Under **Permissions**, select**Extension access**.
- 
                        Select the three dot menu icon for the Slack Extension you need to edit. 
- 
                        Select **Edit**.
- 
                        Edit the configuration as required and select **Save**to confirm the changes.

Your changes to the Slack extension access configuration are saved and will take effect immediately.

### Delete Slack extension access

Follow these steps to permanently remove a Slack extension access configuration. This action cannot be undone.

- 
                        Sign in to the Amazon Quick console. 
- 
                        In the top right, select the profile picture icon. 
- 
                        From the drop-down menu, select **Manage account**.
- 
                        Under **Permissions**, select**Extension access**.
- 
                        Select the three dot menu icon for the Slack Extension you need to delete. 
- 
                        Select **Delete**.
- 
                        Enter the word, "confirm", and select **DELETE**.

###### Note

Deleting a extension access removes access for all users in your Slack workspace and deletes all extensions created for Slack. If delete extension access fails, the admin must switch to the author view and delete the Slack extensions that are using the configured extension access before returning to delete the extension access.

With Slack extension access configured, your team can now use
                **@Amazon Quick** mentions in channels and direct messages to
            access AI assistance and organizational knowledge directly within their
                Slack workspace.