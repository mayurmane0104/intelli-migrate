# Set up service credentials - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-admin-config.html](https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-admin-config.html)

---

Before you create the knowledge base in Amazon Quick, complete the following configuration steps in AWS and Microsoft Entra ID. You create a KMS signing key, generate a certificate, register an application in Entra, and grant Amazon Quick permission to use the key.

This setup involves multiple systems and might require coordination between different administrators in your organization. The following table summarizes each step and the role needed to complete it.

| Step | What you do | Role needed | 
|---|---|---|
| 1. KMS key | Create an asymmetric signing key in AWS KMS. | AWS administrator (KMS and IAM console access) | 
| 2. Certificate | Generate a self-signed certificate using the KMS public key. | Same as Step 1 (AWS CLI and OpenSSL required) | 
| 3. Entra app | Register an application in Microsoft Entra, assign API permissions, and upload the certificate. | Microsoft 365 Global Admin or Privileged Role Admin | 
| 3b. Sites.Selected (optional) | Create a temporary admin app and grant per-site permissions via the Microsoft Graph API. | Microsoft 365 Global Admin (same as Step 3) | 
| 4. KMS key access | Grant Amazon Quick permission to use the KMS key for signing. | Amazon Quick administrator (Admin Pro) | 
| 5. Create KB | Create the knowledge base in Amazon Quick using the credentials from the previous steps. | Any Amazon Quick user (Author Pro or Admin Pro) | 

###### Tip

In many organizations, a single person with both AWS and Microsoft 365 administrator access can complete all steps. If responsibilities are split across teams, share this table to coordinate the setup.

## Prerequisites

        Before you begin, make sure that you have the following:

- 
                An AWS account with an active Amazon Quick instance. 
- 
                Access to the AWS KMS console (for creating the signing key). 
- 
                Amazon Quick administrator access (Admin Pro role) for granting KMS key permissions. 
- 
                A Microsoft 365 tenant with SharePoint Online. 
- 
                Global Administrator or Privileged Role Administrator access in Microsoft Entra ID. 
- 
                OpenSSL 3.0 or later and AWS CLI installed locally. 
- 
                The AWS account and Amazon Quick instance must be in the same Region. 

## Permissions

        The permissions you assign depend on two choices:

- 
                Whether you plan to enable document-level access control (ACL crawling). 
- 
                Whether you want to grant access to all SharePoint sites or only specific sites. 

### Choose your permission scope

By default, the Entra app registration uses
                `Sites.Read.All` or `Sites.FullControl.All`, which
                grants access to all SharePoint sites in your tenant. If your organization
                requires least-privilege access, you can use
                `Sites.Selected` instead. With `Sites.Selected`,
                the app can only access sites that you explicitly grant permission
                to.

| Scope | Access | Additional steps | 
|---|---|---|
| All sites (default) | App can read all SharePoint sites in the tenant. | — | 
| `Sites.Selected` | App can only access sites you explicitly grant. | Requires a temporary admin app and a Microsoft
                                Graph API call for each site. See [Step 3b: Grant site-level permissions (Sites.Selected only)](#sharepoint-kb-admin-sites-selected). | 

###### Note

If you use `Sites.Selected`, you must grant access
                    for each site individually. Any new sites added to the knowledge
                    base in the future also require a separate permission grant.

**All sites – content only (no ACL)**

| API | Permission | Type | 
|---|---|---|
| Microsoft Graph | `Sites.Read.All` | Application | 
| SharePoint REST | `Sites.Read.All` | Application | 

**All sites – with ACL crawling**

| API | Permission | Type | 
|---|---|---|
| Microsoft Graph | `Sites.Read.All` | Application | 
| Microsoft Graph | `User.Read.All` | Application | 
| Microsoft Graph | `GroupMember.Read.All` | Application | 
| SharePoint REST | `Sites.FullControl.All` | Application | 

###### Important

Choose either the all-sites permissions in the preceding tables or the
                `Sites.Selected` permissions in the following tables. Do not combine
                both. If you are unsure, start with all-sites. You can create a
                new Entra app registration with `Sites.Selected`
                later if needed.

**Sites.Selected – content only (no
                ACL)**

| API | Permission | Type | 
|---|---|---|
| Microsoft Graph | `Sites.Selected` | Application | 
| SharePoint REST | `Sites.Selected` | Application | 

**Sites.Selected – with ACL
                crawling**

| API | Permission | Type | 
|---|---|---|
| Microsoft Graph | `Sites.Selected` | Application | 
| Microsoft Graph | `User.Read.All` | Application | 
| Microsoft Graph | `GroupMember.Read.All` | Application | 
| SharePoint REST | `Sites.Selected` | Application | 

###### Note

OneNote crawling (`Notes.Read.All`) is not supported in
                admin-managed setup. Microsoft retired app-only tokens for OneNote APIs on
                March 31, 2025. Use [User-managed setup](./sharepoint-kb-user-managed.html) for OneNote content.

## Values collected during setup

        The following table summarizes the values you create or collect during setup and where you use them.

| Value | Created in step | Used in step | 
|---|---|---|
| KMS Key ARN | 1 (KMS) | 2 (Certificate), 4 (IAM), Quick setup | 
| Certificate file ( `certificate.cer`) | 2 (Certificate) | 3 (Entra upload) | 
| Certificate thumbprint (base64url) | 2 (Certificate) | Quick setup | 
| Application (Client) ID | 3 (Entra) | Quick setup | 
| Directory (Tenant) ID | 3 (Entra) | Quick setup | 
| SharePoint domain URL | Your M365 tenant | Quick setup | 

## Step 1: Create an AWS KMS asymmetric signing key

        Amazon Quick uses an AWS KMS asymmetric key to sign OAuth assertions when authenticating with Microsoft Entra ID. The private key never leaves KMS. Only the public key is exported and embedded in a certificate that gets uploaded to your Entra app registration.

### Create the KMS key

- 
                    Open the [AWS KMS console](https://console.aws.amazon.com/kms).
- 
                    In the left navigation, choose **Customer managed keys**.
- 
                    Choose **Create key**.

### Configure the key

On the **Configure key** page, set the following
                values:

| Setting | Value | 
|---|---|
| Key type | Asymmetric | 
| Key usage | Sign and verify | 
| Key spec | RSA_2048 | 
| Key material origin | KMS (recommended) | 
| Regionality | Single-Region key (default). Multi-Region keys are not supported. | 

### Add labels

On the **Add labels** page, enter an alias for the key.
                For example: `quick-sharepoint-service-auth`.

###### Note

The key administrator and key usage permissions on the following pages are optional. The defaults are sufficient for this setup. You grant Amazon Quick access to the key separately in Step 4.

Choose **Skip to review**, then choose
                **Finish** to create the key.

### Record the Key ARN

After the key is created, open the key detail page and record the
                **Key ARN**. The ARN has the following
                format:

`arn:aws:kms:us-west-2:123456789012:key/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`You need this value in Steps 2, 4, and when you create the knowledge base in Quick.

## Step 2: Generate a self-signed certificate

        Microsoft Entra ID requires an X.509 certificate to validate signed
            assertions. Because the KMS private key never leaves AWS KMS, you cannot use
            it directly with OpenSSL. Instead, you generate a temporary local key pair
            and create a certificate signing request. Then, use the OpenSSL
            `-force_pubkey` option to inject the KMS public key into the final
            certificate. The result is a self-signed certificate whose public key matches
            the KMS key pair.

### Prerequisites

- 
                    AWS CLI installed and configured. 
- 
                    OpenSSL 3.0 or later. 
- 
                    The KMS Key ARN from Step 1. 

### Generate the certificate

Run the following commands in a terminal. Replace the
                `placeholder` values with your own.

**Verify OpenSSL version**

`openssl version`Confirm the output shows version 3.0 or later.

**Export the KMS public key**

`aws kms get-public-key \ --key-id``KMS_KEY_ARN`\ --region`REGION`\ --output text \ --query PublicKey | base64 --decode > public_key.der

###### Note

On macOS, use `base64 --decode` or ```
base64
                        -D
```
 depending on your shell environment.

**Convert the public key to PEM format**

`openssl rsa -pubin -inform DER -in public_key.der -outform PEM -out kms_public_key.pem`**Generate a temporary local key pair**

`openssl genrsa -out temp_private_key.pem 2048`**Create a certificate signing request**

`openssl req -new \ -key temp_private_key.pem \ -out cert.csr \ -subj "/CN=QuickSharePointServiceAuth/O=``YourOrganization`/C=`US`"

**Generate the certificate with the KMS public
                    key**

```
openssl x509 -req \
    -in cert.csr \
    -signkey temp_private_key.pem \
    -out certificate.pem \
    -days 730 \
    -force_pubkey kms_public_key.pem
```
###### Note

OpenSSL displays the warning ```
Signature key and public key
                        of cert do not match
```
. This is expected because the
                    certificate is signed with the temporary local key but contains the
                    KMS public key. The certificate is valid and works correctly with
                    Microsoft Entra.

**Convert to DER format for Entra
                    upload**

`openssl x509 -in certificate.pem -outform DER -out certificate.cer`**Clean up temporary files**

`rm -f temp_private_key.pem cert.csr public_key.der kms_public_key.pem certificate.pem`###### Important

Keep the `certificate.cer` file. You upload it to
                    Microsoft Entra ID in Step 3.

### Calculate the certificate thumbprint

Run the following command to calculate the base64url-encoded SHA-1 thumbprint of the certificate:

`openssl dgst -sha1 -binary certificate.cer | base64 | tr '+/' '-_' | tr -d '='`Record this value. You enter it when you create the knowledge base in Quick.

###### Note

The base64url-encoded thumbprint is different from the hexadecimal thumbprint shown in the Microsoft Entra portal. Quick requires the base64url format.

## Step 3: Register an application in Microsoft Entra ID

        This step is required regardless of whether you use all-sites permissions
            or `Sites.Selected`. The only difference is which API permissions
            you assign in the
            [Configure API permissions](#sharepoint-kb-admin-entra-permissions) section.

### Register the application

- 
                    Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
- 
                    In the left navigation, expand **Entra ID**and choose**App registrations**.
- 
                    Choose **New registration**.
- 
                    For **Name**, enter`QuickSharePointServiceAuth`.
- 
                    For **Supported account types**, select**Accounts in this organizational directory only (Single tenant)**.
- 
                    Leave **Redirect URI**blank. A redirect URI is not required because the application uses the client credentials flow, not an interactive sign-in flow.
- 
                    Choose **Register**.

### Record application details

On the application **Overview** page, record the
                following values:

| Value | Location | 
|---|---|
| Application (client) ID | Shown on the Overview page under Essentials. | 
| Directory (tenant) ID | Shown on the Overview page under Essentials. | 

### Configure API permissions

Add the permissions that match your use case. Choose the permissions
                from the tables in the
                [Permissions](#sharepoint-kb-admin-config-permissions) section. Base
                your selection on your permission scope (all sites or Sites.Selected)
                and whether you enable ACL crawling.

**Content only – Microsoft Graph**

- 
                    `Sites.Read.All`

**Content only – SharePoint**

- 
                    `Sites.Read.All`

**ACL crawling – Microsoft Graph
                    (additional)**

- 
                    `Sites.Read.All`
- 
                    `User.Read.All`
- 
                    `GroupMember.Read.All`

**ACL crawling – SharePoint**

- 
                    `Sites.FullControl.All`

###### Note

`Sites.FullControl.All` is required for ACL crawling
                    because the SharePoint REST API requires full control permissions to
                    read site-level and item-level permission assignments. If you are
                    using `Sites.Selected`, see
                    [Step 3b: Grant site-level permissions (Sites.Selected only)](#sharepoint-kb-admin-sites-selected) for the
                    alternative permission set.

- 
                    In the left navigation of your app registration, choose **API permissions**.
- 
                    Choose **Add a permission**.
- 
                    Choose **Microsoft Graph**.
- 
                    Choose **Application permissions**.
- 
                    Search for and select the required Microsoft Graph permissions for your use case, then choose **Add permissions**.
- 
                    Choose **Add a permission**again.
- 
                    Choose **SharePoint**(under Microsoft APIs).
- 
                    Choose **Application permissions**.
- 
                    Search for and select the required SharePoint permissions for your use case, then choose **Add permissions**.

###### Important

Select the **Application permissions** tab, not
                    **Delegated permissions**. Admin-managed setup uses
                    the client credentials flow, which requires application
                    permissions.

### Grant admin consent

- 
                    On the **API permissions**page, choose**Grant admin consent for [Your Organization]**.
- 
                    Confirm the consent when prompted. 

###### Important

Admin consent is required for application permissions. Without it, the application cannot access SharePoint data.

### Upload the certificate

- 
                    In the left navigation of your app registration, choose **Certificates & secrets**.
- 
                    Choose the **Certificates**tab.
- 
                    Choose **Upload certificate**.
- 
                    Select the `certificate.cer`file you generated in Step 2.
- 
                    Choose **Add**.

###### Note

The Entra portal displays the certificate thumbprint in hexadecimal format. This is different from the base64url-encoded thumbprint you calculated in Step 2. Use the base64url value when you configure the knowledge base in Quick.

## Step 3b: Grant site-level permissions (Sites.Selected only)

        If you chose `Sites.Selected` as your permission scope, you
            must explicitly grant your Amazon Quick Entra app access to each SharePoint
            site. This requires a temporary admin app with
            `Sites.FullControl.All` permission to call the Microsoft Graph
            API.

Skip this step if you are using the all-sites permission scope
            (`Sites.Read.All` or
            `Sites.FullControl.All`).

### Get the Site ID for each SharePoint site

You need the Site ID for each SharePoint site you want to grant access to. To get a Site ID:

- 
                    In your browser, navigate to the SharePoint site (for example, `https://`).`yourcompany`.sharepoint.com/sites/`SiteName`
- 
                    Append `/_api/site/id`to the URL and press Enter. For example:`https://``yourcompany`.sharepoint.com/sites/`SiteName`/_api/site/id
- 
                    The page displays an XML response containing the Site ID (a GUID). Record this value. 

Repeat for each site you want to include in the knowledge base.

### Create a temporary admin app

The admin app is used only to grant site-level permissions to your Amazon Quick app. You can delete it after completing this step.

- 
                    In the [Microsoft Entra admin center](https://entra.microsoft.com/), go to**App registrations**and choose**New registration**.
- 
                    For **Name**, enter a descriptive name such as`Quick-SharePoint-PermissionGranter`.
- 
                    For **Supported account types**, select**Accounts in this organizational directory only (Single tenant)**.
- 
                    Leave **Redirect URI**blank and choose**Register**.
- 
                    Record the **Application (client) ID**from the Overview page.
- 
                    Choose **API permissions**, then**Add a permission**.
- 
                    Choose **Microsoft Graph**, then**Application permissions**. Search for and select`Sites.FullControl.All`. Choose**Add permissions**.
- 
                    Choose **Grant admin consent for [Your Organization]**and confirm.
- 
                    Choose **Certificates & secrets**, then**New client secret**. Enter a description, choose an expiration period, and choose**Add**.
- 
                    Record the secret **Value**immediately. This value is only displayed once.

###### Important

Copy the secret **Value**, not
                    the Secret ID. The Value is the longer string used for
                    authentication.

### Get an access token

Use the admin app credentials to retrieve an OAuth token from
                Microsoft Entra. Replace the `placeholder`
                values with your admin app's client ID, secret value, and tenant
                ID.

**macOS and Linux (bash)**

`curl -s --location "https://login.microsoftonline.com/``TENANT_ID`/oauth2/v2.0/token" \ --header "Content-Type: application/x-www-form-urlencoded" \ --data-urlencode "grant_type=client_credentials" \ --data-urlencode "client_id=`ADMIN_APP_CLIENT_ID`" \ --data-urlencode "client_secret=`ADMIN_APP_SECRET_VALUE`" \ --data-urlencode "scope=https://graph.microsoft.com/.default"

**Windows (PowerShell)**

`$tokenResponse = Invoke-RestMethod ` -Uri "https://login.microsoftonline.com/``TENANT_ID`/oauth2/v2.0/token" ` -Method Post ` -ContentType "application/x-www-form-urlencoded" ` -Body @{ grant_type = "client_credentials" client_id = "`ADMIN_APP_CLIENT_ID`" client_secret = "`ADMIN_APP_SECRET_VALUE`" scope = "https://graph.microsoft.com/.default" } $adminToken = $tokenResponse.access_token

The response contains an `access_token` field. Record
                this value for the next step.

### Grant site-level permissions

Use the admin token to grant your Amazon Quick Entra app
                `fullcontrol` access to each SharePoint site. Replace the
                `placeholder` values with your Site ID, admin
                token, and the client app ID and display name from Step 3.

**macOS and Linux (bash)**

`curl -s --location "https://graph.microsoft.com/v1.0/sites/``SITE_ID`/permissions" \ --header "Content-Type: application/json" \ --header "Authorization: Bearer`ADMIN_TOKEN`" \ --data '{ "roles": ["fullcontrol"], "grantedToIdentities": [{ "application": { "id": "`CLIENT_APP_ID`", "displayName": "`CLIENT_APP_NAME`" } }] }'

**Windows (PowerShell)**

`$body = @{ roles = @("fullcontrol") grantedToIdentities = @( @{ application = @{ id = "``CLIENT_APP_ID`" displayName = "`CLIENT_APP_NAME`" } } ) } | ConvertTo-Json -Depth 10 Invoke-RestMethod ` -Uri "https://graph.microsoft.com/v1.0/sites/`SITE_ID`/permissions" ` -Method Post ` -Headers @{ "Content-Type" = "application/json" "Authorization" = "Bearer $adminToken" } ` -Body $body

A successful response includes ```
"roles":
                    ["fullcontrol"]
```
 and the client app ID in the
                `grantedToIdentities` field.

###### Important

Repeat this command for each SharePoint site you want to include in the knowledge base. Any new sites added in the future also require a separate permission grant.

### Clean up

After you have granted permissions to all required sites, you can delete the temporary admin app from the Microsoft Entra admin center. The site-level permissions you granted remain in effect independently of the admin app.

###### Note

The temporary admin app is used only in your local environment to call the Microsoft Graph API. Amazon Quick never sees or has access to the admin app or its credentials. Only the client app credentials are provided to Amazon Quick when you create the knowledge base.

## Step 4: Grant Amazon Quick permission to the KMS key

        Amazon Quick needs permission to use the KMS key for signing OAuth assertions. You grant this permission from the Amazon Quick admin console.

###### Note

This step requires Amazon Quick administrator access (Admin Pro role). If you are not an administrator, ask your Amazon Quick admin to complete this step using the KMS key ARN from Step 1.

###### Important

If your organization manages its own Amazon Quick IAM service role,
                the following console steps might not apply. Instead, ensure the role
                has `kms:Sign` permission on the KMS key ARN from
                Step 1.

- 
                In Amazon Quick, choose **Manage account**from the left navigation pane.
- 
                Under **Permissions**, choose**AWS resources**.
- 
                On the AWS resources page, scroll to **AWS Key Management Service**and select the checkbox.
- 
                Choose **Select keys**.
- 
                In the **Select KMS keys**dialog, enter the KMS key ARN you recorded in Step 1 and choose**Add**.
- 
                The key ARN appears in the list. Choose **Finish**.
- 
                Choose **Save**at the bottom of the AWS resources page.

## Next steps

        After you complete the setup, create the SharePoint Online knowledge base
            connection in Amazon Quick. For instructions, see
            [Create the knowledge base in Amazon Quick](./sharepoint-kb-admin-connection.html).