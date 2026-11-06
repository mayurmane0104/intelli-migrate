# Set up service credentials - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-admin-config.html](https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-admin-config.html)

---

Before you create the knowledge base in Amazon Quick, complete the following configuration steps in AWS and Microsoft Entra ID. You create a KMS signing key, generate a certificate, register an application in Entra, and grant Amazon Quick permission to use the key.

This setup involves multiple systems and might require coordination between different administrators in your organization. The following table summarizes each step and the role needed to complete it.

| Step | What you do | Role needed | 
|---|---|---|
| 1. KMS key | Create an asymmetric signing key in AWS KMS. | AWS administrator (KMS and IAM console access) | 
| 2. Certificate | Generate a self-signed certificate using the KMS public key. | Same as Step 1 (AWS CLI and OpenSSL required) | 
| 3. Entra app | Register an application in Microsoft Entra, assign API permissions, and upload the certificate. | Microsoft 365 Global Admin or Privileged Role Admin | 
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
                A Microsoft 365 tenant with OneDrive. 
- 
                Global Administrator or Privileged Role Administrator access in Microsoft Entra ID. 
- 
                OpenSSL 3.0 or later and AWS CLI installed locally. 
- 
                The AWS account and Amazon Quick instance must be in the same Region. 

## Permissions

        Admin-managed setup crawls the OneDrive content of every user in your organization and always enforces document-level access control. The Entra app registration requires the following Microsoft Graph application permissions.

| Permission | Type | Purpose | 
|---|---|---|
| `Files.Read.All` | Application | Read files in all users' OneDrive content. | 
| `Sites.Read.All` | Application | Enumerate and read the OneDrive drives across the tenant. OneDrive for Business is hosted on SharePoint, so this permission is required to access each user's drive. | 
| `User.Read.All` | Application | Read user profiles to resolve document-level access control. | 
| `Group.Read.All` | Application | Read group objects to resolve group-based access control. | 
| `GroupMember.Read.All` | Application | Read group memberships to resolve document-level access control. | 

###### Important

Select the **Application permissions** tab, not
                **Delegated permissions**, when you assign these
                permissions in Entra. Admin-managed setup uses the client credentials
                flow, which requires application permissions.

###### Note

OneNote crawling (`Notes.Read.All`) is not supported in
                admin-managed setup. Microsoft retired app-only tokens for OneNote APIs on
                March 31, 2025. Use [User-managed setup](./onedrive-kb-user-managed.html) for OneNote content.

## Values collected during setup

        The following table summarizes the values you create or collect during setup and where you use them.

| Value | Created in step | Used in step | 
|---|---|---|
| KMS Key ARN | 1 (KMS) | 2 (Certificate), 4 (IAM), Quick setup | 
| Certificate file ( `certificate.cer`) | 2 (Certificate) | 3 (Entra upload) | 
| Certificate thumbprint (base64url) | 2 (Certificate) | Quick setup | 
| Application (Client) ID | 3 (Entra) | Quick setup | 
| Directory (Tenant) ID | 3 (Entra) | Quick setup | 

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
                For example: `quick-onedrive-service-auth`.

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

`openssl req -new \ -key temp_private_key.pem \ -out cert.csr \ -subj "/CN=QuickOneDriveServiceAuth/O=``YourOrganization`/C=`US`"

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

         
            ### Register the application

- 
                    Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/)on the Microsoft website.
- 
                    In the left navigation, expand **Entra ID**and choose**App registrations**.
- 
                    Choose **New registration**.
- 
                    For **Name**, enter`QuickOneDriveServiceAuth`.
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

Add the Microsoft Graph application permissions listed in the
                [Permissions](#onedrive-kb-admin-config-permissions) section.

- 
                    In the left navigation of your app registration, choose **API permissions**.
- 
                    Choose **Add a permission**.
- 
                    Choose **Microsoft Graph**.
- 
                    Choose **Application permissions**.
- 
                    Search for and select `Files.Read.All`,`Sites.Read.All`,`User.Read.All`,`Group.Read.All`, and`GroupMember.Read.All`, then choose**Add permissions**.

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

Admin consent is required for application permissions. Without it, the application cannot access OneDrive data.

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

        After you complete the setup, create the OneDrive knowledge base
            connection in Amazon Quick. For instructions, see
            [Create the knowledge base in Amazon Quick](./onedrive-kb-admin-connection.html).