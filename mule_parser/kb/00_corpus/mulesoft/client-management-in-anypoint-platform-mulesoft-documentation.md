# Client Management in Anypoint Platform | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/access-management/managing-api-clients](https://docs.mulesoft.com/access-management/managing-api-clients)

---

# Client Management in Anypoint Platform

Configure up to 25 external client providers in Anypoint Platform to authorize API client applications. Apply OAuth 2.0 policies to protect your APIs, using your chosen OAuth 2.0 provider. This enables you to centralize and scale client authorization across environments.

## Supported OAuth 2.0 Providers

To configure client management on Anypoint Platform for supported providers, you must have an identity provider (IdP) account with the provider to use.

You can configure these OAuth 2.0 providers:

- 
[Dynamic Client Registration-compliant client providers](configure-client-management-openid-task)- 
[Microsoft Entra ID Client Management](configure-client-management-entra-id)
 Dynamic Client Registration-compliant identity providers must conform to the[OpenID Connect Client Registration 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-registration-1_0.html).
 
- 

## Multiple Client Providers

You can configure more than one client provider and [associate the client providers with different environments](environments#add-an-idp-to-an-existing-environment).

If you configure multiple client providers after you create environments, you can associate the new client providers with the environment. Review the existing client configuration before reassigning client providers to avoid any downtime with existing assets or APIs.

## Delete a Client Provider

When you delete a client provider from your root organization, the client provider is no longer available in environments that used it. Also, assets or APIs that used the client provider can no longer authorize users who want to access them.

| Before you delete a client provider, make sure that you don’t have APIs, assets, or environments that depend on the client provider or you will lose functionality. For example, any APIs that depend on the client provider can no longer authenticate user access. | 

- 
Sign in to Anypoint Platform using an account that has the Organization Administrator permission. 
- 
Select **Access Management**from themenu. 
- 
In the **Business Groups**menu, select your root organization.
- 
In the Access Management navigation menu, click **Client Providers**.
- 
Click the name of the client provider you want to delete. 
- 
In the client provider’s page, click **Delete**.
- 
Enter the name of the client identity provider name. 
- 
Click **Delete**.

## See Also

- 
[OpenID Connect Client Registration 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-registration-1_0.html)
- 
[Configuring PingFederate Client Management in Anypoint Platform](conf-client-mgmt-pf-task)
- 
[Configuring OpenID Connect Client Management in Anypoint Platform](configure-client-management-openid-task)
- 
[Migrate Client Applications for APIs with External Client Providers in API Manager](../api-manager/latest/migrate-client-apps#migrate_with_external)