# Client Applications, Contracts, and Credentials | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/api-contracts-landing-page](https://docs.mulesoft.com/api-manager/latest/api-contracts-landing-page)

---

# Client Applications, Contracts, and Credentials

Credentials consist of two keys: the client ID and the client secret. Anypoint API Manager (API Manager) uses the following types of credentials:

- 
Client application 
- 
Organization 
- 
Basic Authentication policy 
- 
SOAP proxy 

## Client Application Credentials

As the Organization Administrator, after you grant access to applications in Anypoint Exchange (Exchange), a contract is automatically created between the instance and the application. The contract gives access to the application based on SLA tiers that you might specify. Only one contract can exist per instance and application at any time.

As a user, when you request access to an asset from Exchange, your request is automatically approved if no SLA tiers are defined. If the asset includes an SLA tier, you can either configure your request so that it is automatically approved despite the SLA tier, or you can request approval manually.

Client application credentials are generated when you create a new application and request access to an instance. Requests must include these credentials if the instance is protected by a client ID enforcement policy. Organization Administrators can configure this enforcement policy to accept credentials either as headers or as query parameters, although using headers is more secure.

For additional information about client application credentials, see:

Default policies that internally enforce client application credentials include:

- 
[Mule OAuth 2.0 Access Token Enforcement](../../mule-gateway/policies-included-oauth-access-token-enforcement)(Mule v3.8.5 or later)
- 
[PingFederate OAuth 2.0 Token Enforcement](../../mule-gateway/policies-included-pingfederate-oauth-token-enforcement)(Mule v3.8.5 or later)
- 
[OpenID Connect OAuth 2.0 Token Enforcement](../../gateway/latest/policies-included-openid-token-enforcement)(Mule v3.8.5 or later)
- 
[JWT Validation](../../gateway/latest/policies-included-jwt-validation)(Mule v3.8.5 or later)

For information about how to configure and apply client ID enforcement policies, see [Client ID Enforcement Policy](../../gateway/latest/policies-included-client-id-enforcement).

## Organization Credentials

Organization credentials provide a method to uniquely identify a specific environment, an organization, or a business group when linking Mule runtime engine (Mule) to an organization using Anypoint Platform. Mule uses these credentials to connect to and access your organization.

For example, you use environment credentials to connect a local Anypoint Studio (Studio) Mule deployment to API Manager through Autodiscovery. This connection allows the Studio-deployed application to be managed by API Manager. See [Review Environment Concepts](environments-concept) and [Autodiscovery](../../mule-gateway/mule-gateway-autodiscovery-overview).

For additional information about configuring and obtaining organization credentials, see [Configuring Organization Credentials in Mule Runtime 4](../../mule-gateway/mule-gateway-org-credentials-mule4).

## Basic Authentication Policy Credentials

The Simple Authentication default policy protects an instance by forcing requests to provide credentials. These credentials populate a request’s `Authorization` header. For details on building requests using the Simple Authentication policy, see [Basic Authentication: Simple Policy](../../gateway/latest/policies-included-basic-auth-simple).

The Lightweight Directory Access Protocol (LDAP) Authentication default policy restricts access by using an LDAP authentication mechanism. LDAP authentication forces requests to provide credentials in an `Authorization` header and then requests the configured LDAP instance to determine if the credentials are correct in the provided LDAP context. For details on configuring the LDAP Authentication policy, see [Basic Authentication: LDAP Policy](../../gateway/latest/policies-included-basic-auth-ldap).

## SOAP Proxy Credentials

You can protect a WSDL that is hosted on a remote location by configuring basic authentication credentials. For details on building a SOAP proxy, see [Build SOAP Proxies](building-soap-proxy).