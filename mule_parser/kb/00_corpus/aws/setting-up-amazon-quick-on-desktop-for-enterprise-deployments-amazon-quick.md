# Setting up Amazon Quick on desktop for enterprise deployments - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/desktop-enterprise-setup.html](https://docs.aws.amazon.com/quick/latest/userguide/desktop-enterprise-setup.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: System administrators | 

To use Amazon Quick on desktop for enterprise deployments, administrators must configure enterprise single sign-on (SSO) so that users in the organization can sign in with their corporate credentials. This setup connects your organization's OpenID Connect (OIDC) compatible identity provider (IdP) to Amazon Quick.

###### Note

If you are using a Free or Plus account, this section does not apply to you.
            Continue to [Getting started](./getting-started-desktop.html).

The setup involves the following steps, in order:

- 
            Create an OIDC application in your IdP. 
- 
            Configure the extension access in the Amazon Quick management console. 
- 
            Distribute the desktop application to your users. 

This guide provides IdP-specific instructions for Microsoft Entra ID, Okta, and Ping Identity (PingFederate and PingOne). See instructions for your specific identity provider below.

## How enterprise sign-in works

        The Amazon Quick desktop application uses the OIDC protocol to authenticate users.
            When a user chooses **Enterprise login**, the application
            opens a browser window and redirects to your IdP's authorization endpoint. The
            application then exchanges the resulting authorization code for tokens using Proof Key
            for Code Exchange (PKCE).

Amazon Quick validates the token and maps the user to an identity in your account. The email address in your IdP must exactly match the email address of the user in Amazon Quick.

## Prerequisites

        Before you begin, verify that you have the following:

- 
                An AWS account with an active Amazon Quick subscription. The Amazon Quick account's home region (identity region) must be US East (N. Virginia) (us-east-1). All identity types are supported, including IAM Identity Center, IAM federation, and native Amazon Quick (username/password) users. 
- 
                Administrator access to your Amazon Quick account. 
- 
                Access to your IdP with permissions to create OIDC application registrations. 

###### Important

The Amazon Quick account's home region (identity region) must be US East (N. Virginia) (us-east-1). All inference for the desktop application also uses this Region. While Amazon Quick on the web can be used in other Regions, the desktop application connects to us-east-1 for both authentication and inference.

## Step 1: Create an OIDC application in your identity provider

        Register a public OIDC client application in your IdP. The Amazon Quick desktop application uses this client to authenticate users through the authorization code flow with PKCE. No client secret is required.

The desktop application requires refresh tokens to maintain long-lived sessions. How refresh tokens are configured depends on your IdP:

- 
                **Microsoft Entra ID**– The`offline_access`scope must be granted. Without it, users must re-authenticate frequently.
- 
                **Okta**– The Refresh Token grant type must be enabled on the application, and the`offline_access`scope must be granted.
- 
                **Ping Identity**– The Refresh Token grant type must be enabled, and the`offline_access`scope must be granted. For PingFederate, the**Return ID Token On Refresh Grant**setting must also be enabled in the OIDC policy.

Choose the instructions for your identity provider.

### Microsoft Entra ID

For detailed instructions, see [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in the Microsoft Entra
                documentation.

###### To create the Entra ID app registration

- 
                    In the Azure portal, navigate to **Microsoft Entra ID → App registrations → New registration**.
- 
                    Configure the following settings: Setting Value Name `Amazon Quick Desktop`Supported account types Accounts in this organizational directory only (Single tenant) Redirect URI platform Public client/native (mobile & desktop) Redirect URI `http://localhost:18080`
- 
                    Choose **Register**.
- 
                    On the **Overview**page, note the**Application (client) ID**and**Directory (tenant) ID**. You need these values in later steps.

This is a public client registration. PKCE is enforced automatically by Entra ID for public clients.

###### To configure API permissions

- 
                    In the app registration, navigate to **API permissions → Add a permission → Microsoft Graph → Delegated permissions**.
- 
                    Add the following permissions: `openid`,`email`,`profile`,`offline_access`.
- 
                    Choose **Add permissions**.
- 
                    If your organization requires it, choose **Grant admin consent for [your organization]**.

###### To configure authentication settings

- 
                    In the app registration, navigate to **Authentication**.
- 
                    Under **Advanced settings**, set**Allow public client flows**to**Yes**.
- 
                    Verify that `http://localhost:18080`is listed under**Mobile and desktop applications**.
- 
                    Choose **Save**.

Your OIDC endpoints use the following format. Replace
                `<TENANT_ID>` with your Directory (tenant) ID.

| Field | Value | 
|---|---|
| Issuer URL | `https://login.microsoftonline.com/<TENANT_ID>/v2.0` | 
| Authorization endpoint | `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/authorize` | 
| Token endpoint | `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token` | 
| JWKS URI | `https://login.microsoftonline.com/<TENANT_ID>/discovery/v2.0/keys` | 

### Okta

For detailed instructions, see [Create OpenID Connect app integrations](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm) in the Okta
                documentation.

###### To create the Okta OIDC Native Application

- 
                    In the Okta Admin Console, navigate to **Applications → Applications → Create App Integration**.
- 
                    Select **OIDC - OpenID Connect**as the sign-in method.
- 
                    Select **Native Application**as the application type, then choose**Next**.
- 
                    Configure the following settings: Setting Value App integration name `Amazon Quick Desktop`Grant type Authorization Code and Refresh Token Sign-in redirect URIs `http://localhost:18080`Assignments Assign to the appropriate users or groups 
- 
                    Choose **Save**.
- 
                    On the **General**tab, note the**Client ID**.

PKCE (S256) is enforced automatically by Okta for native applications.

###### To configure scopes

- 
                    In the Okta Admin Console, navigate to **Security → API → Authorization Servers**and select your authorization server (for example,**default**).
- 
                    On the **Scopes**tab, verify that the following scopes are enabled:`openid`,`email`,`profile`,`offline_access`.
- 
                    On the **Access Policies**tab, verify that the policy assigned to this application allows the`Authorization Code`and`Refresh Token`grant types.

###### To verify authentication settings

- 
                    In the app integration, go to the **General**tab.
- 
                    Under **General Settings**, confirm that the application type is**Native**, client authentication is**None**(public client), and PKCE is**Required**.
- 
                    Under **LOGIN**, confirm that`http://localhost:18080`is listed as a redirect URI.
- 
                    Choose **Save**if you made any changes.

Your OIDC endpoints use the following format. Replace
                `<OKTA_DOMAIN>` with your Okta domain (for example,
                `your-org.okta.com`).

| Field | Value | 
|---|---|
| Issuer URL | `https://<OKTA_DOMAIN>/oauth2/default` | 
| Authorization endpoint | `https://<OKTA_DOMAIN>/oauth2/default/v1/authorize` | 
| Token endpoint | `https://<OKTA_DOMAIN>/oauth2/default/v1/token` | 
| JWKS URI | `https://<OKTA_DOMAIN>/oauth2/default/v1/keys` | 

### Ping Identity

Choose the instructions for your Ping Identity product.

#### PingFederate

For detailed instructions, see [Setting up an OIDC application in PingFederate](https://docs.pingidentity.com/solution-guides/customer_use_cases/htg_oidc_app_setup_pf.html) in the Ping
                    Identity documentation.

###### To create the PingFederate OIDC client

- 
                        In the PingFederate administrative console, go to **Applications → OAuth → Clients**, and choose**Add Client**.
- 
                        In the **Client ID**field, enter a unique identifier for this client.
- 
                        In the **Name**field, enter`Amazon Quick Desktop`.
- 
                        For **Client Authentication**, select**None**.
- 
                        In the **Redirection URI**section, enter`http://localhost:18080`and choose**Add**.
- 
                        In the **Allowed Grant Types**list, select**Authorization Code**and**Refresh Token**.
- 
                        Select the **Require Proof Key for Code Exchange (PKCE)**checkbox.
- 
                        Under **Common Scopes**, grant the following:`openid`,`email`,`profile`,`offline_access`.
- 
                        Choose **Save**.
- 
                        Note the **Client ID**. You need this value in later steps.

###### To configure the OIDC policy

- 
                        In the PingFederate administrative console, go to **Applications → OAuth → OpenID Connect Policy Management**.
- 
                        Select the OIDC policy associated with this client, or choose **Add Policy**to create one.
- 
                        Select the **Return ID Token On Refresh Grant**checkbox. This ensures that the desktop application receives a fresh ID token with current claims when refreshing the session.
- 
                        Under **Attribute Contract**, verify that the`email`claim is included and mapped to the corresponding user attribute in your authentication source. The`email`claim must be present in tokens issued during both initial authentication and refresh token grants.
- 
                        Choose **Save**.

Your OIDC endpoints use the following format. Replace
                    `<PINGFEDERATE_HOST>` with your PingFederate server
                    hostname.

| Field | Value | 
|---|---|
| Issuer URL | `https://<PINGFEDERATE_HOST>` | 
| Authorization endpoint | `https://<PINGFEDERATE_HOST>/as/authorization.oauth2` | 
| Token endpoint | `https://<PINGFEDERATE_HOST>/as/token.oauth2` | 
| JWKS URI | `https://<PINGFEDERATE_HOST>/pf/JWKS` | 

#### PingOne

For detailed instructions, see [Editing an application – Native](https://docs.pingidentity.com/pingone/applications/p1_edit_application_native.html) in the Ping Identity
                    documentation.

###### To create the PingOne OIDC native application

- 
                        In the PingOne admin console, go to **Applications → Applications**and choose the**+**icon.
- 
                        Enter `Amazon Quick Desktop`as the application name.
- 
                        In the **Application Type**section, select**Native**, then choose**Save**.
- 
                        On the **Configuration**tab, choose**Edit**and configure the following settings:Setting Value Response Type Code Grant Type Authorization Code and Refresh Token PKCE Enforcement S256 Redirect URIs `http://localhost:18080`Token Endpoint Authentication Method None 
- 
                        Choose **Save**.
- 
                        On the **Resources**tab, add the following scopes:`openid`,`email`,`profile`,`offline_access`.
- 
                        On the **Attribute Mappings**tab, verify that the`email`attribute is mapped to the user's email address.
- 
                        Toggle the application to **Enabled**.
- 
                        Note the **Client ID**and**Environment ID**from the**Configuration**tab.

###### Note

The PingOne domain varies by region. The examples below use
                        `.com`. Replace the domain with the one for your
                        environment (for example, `.ca`, `.eu`, or
                        `.asia`).

Your OIDC endpoints use the following format. Replace
                    `<ENV_ID>` with your PingOne environment ID.

| Field | Value | 
|---|---|
| Issuer URL | `https://auth.pingone.com/<ENV_ID>/as` | 
| Authorization endpoint | `https://auth.pingone.com/<ENV_ID>/as/authorize` | 
| Token endpoint | `https://auth.pingone.com/<ENV_ID>/as/token` | 
| JWKS URI | `https://auth.pingone.com/<ENV_ID>/as/jwks` | 

## Step 2: Configure the extension access in the Amazon Quick management console

        ###### To add the extension access

- 
                Sign in to the Amazon Quick management console. 
- 
                Under **Permissions**, choose**Extension access**.
- 
                Choose **Add extension access**.
- 
                Select the **Desktop application for Quick**extension and choose**Next**.
- 
                Enter the Amazon Quick extension details: Field Value Name A name for this extension access Description (Optional) A description Issuer URL The OIDC issuer URL from Step 1 Authorization Endpoint The OIDC authorization endpoint URL from Step 1 Token Endpoint The OIDC token endpoint URL from Step 1 JWKS URI The JSON Web Key Set URI from Step 1 Client ID The OIDC client identifier from Step 1 
- 
                Choose **Add**.###### ImportantVerify that all values are correct before choosing **Add**. The extension access configuration cannot be edited after creation. If any value is incorrect, you must delete the extension access and create a new one.

###### To create the extension

- 
                In the Amazon Quick console, in the left navigation under **Connect apps and data**, choose**Extensions**.
- 
                Choose **Add extension**.
- 
                Select the **Desktop application for Quick**extension access you previously created. Choose**Next**.
- 
                Choose **Create**.

## Step 3: Download and distribute the desktop application

        After you configure enterprise sign-in, verify the setup by downloading and
            installing the desktop application yourself. Choose **Enterprise
            login** on the sign-in screen and authenticate with your corporate
            credentials to confirm the configuration is working. For download and installation
            steps, see [Getting started](./getting-started-desktop.html).

If the sign-in fails, verify the values you entered in Step 2 against the OIDC
            endpoints from Step 1. If any value is incorrect, delete the extension access under
            **Permissions → Extension access**, and repeat
            Step 2 with the correct values.

After you verify the setup, direct your users to [Getting started](./getting-started-desktop.html) for
            download, installation, and sign-in instructions.

## Troubleshooting

        - `redirect_mismatch`error
- 
                    Verify that the redirect URI in your IdP is exactly `http://localhost:18080`and is configured as a public client or native platform.
- User not found after sign-in
- 
                    The email in the IdP token must exactly match the email of a user in Amazon Quick. Verify that the user is provisioned and that the email addresses are identical in both systems. 
- Token validation failure
- 
                    Verify that the issuer URL in the extension access configuration matches the issuer URL in your IdP's OIDC configuration exactly. 
- Consent or permission errors (Microsoft Entra ID)
- 
                    Grant admin consent for the required API permissions in the Azure portal. Navigate to the app registration's **API permissions**page and choose**Grant admin consent for [your organization]**.
- Session expires frequently
- 
                    Verify that your IdP is configured to issue refresh tokens. For Microsoft Entra ID, the `offline_access`scope is required. For Okta, the Refresh Token grant type must be enabled and the`offline_access`scope must be granted. For Ping Identity, the Refresh Token grant type must be enabled and the`offline_access`scope must be granted. For PingFederate, also verify that**Return ID Token On Refresh Grant**is selected in the OIDC policy.
- `invalid_scope`error (Okta)
- 
                    Verify that `offline_access`is enabled on your authorization server. Navigate to**Security → API → Authorization Servers → default → Scopes**and confirm the scope is present. Also verify that the access policy for the application allows the Refresh Token grant type.
- Application not enabled (PingOne)
- 
                    If authentication fails immediately without reaching the PingOne login page, verify that the application toggle is set to **Enabled**in the PingOne admin console.
- Missing email claim after refresh (PingFederate)
- 
                    Verify that the `email`claim is included in the OIDC policy**Attribute Contract**and mapped to the correct user attribute. The mapping must produce the`email`claim for both initial authentication and refresh token grants.