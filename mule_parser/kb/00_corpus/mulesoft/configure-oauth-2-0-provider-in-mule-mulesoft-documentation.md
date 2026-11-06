# Configure OAuth 2.0 Provider in Mule | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/mule-oauth-provider-landing-page](https://docs.mulesoft.com/api-manager/latest/mule-oauth-provider-landing-page)

---

![mule oauth provider](_images/mule-oauth-provider.png) 

# Configure OAuth 2.0 Provider in Mule

Mule OAuth 2.0 Provider is an OAuth 2.0 provider alternative developed by MuleSoft that can be used in any MuleSoft API Platform organization, including federated ones. The provider enables secure authentication and authorization for APIs across different environments and organizational structures. Use this provider to implement OAuth 2.0 flows, manage access tokens, and control API access permissions. It supports both single-tenant and multi-tenant deployments, making it suitable for various enterprise scenarios.

You must deploy Mule OAuth 2.0 Provider to a runtime with API gateway capabilities, for example, Mule runtime engine (Mule) 3.x, 4.2.0, or later, with the corresponding organization credentials. The following third party OAuth 2.0 providers are supported:

- 
PingFederate 
- 
OpenAM 
- 
OAuth 2.0 providers supporting Open ID Connect 

The [Mule OAuth 2.0 Access Token Enforcement policy](../../mule-gateway/policies-included-oauth-access-token-enforcement) is designed to work with Mule OAuth 2.0 Provider.

## Downloading Mule OAuth 2.0 Provider

You can download Mule OAuth 2.0 Provider from Anypoint Exchange.
See [Mule OAuth 2.0 server for Anypoint Platform](https://anypoint.mulesoft.com/exchange/org.mule.templates/api-gateway-oauth2-provider/).

This feature is available in Mule 4.2.0 and later.

## OAuth 2.0 Dance

The authentication performed by the OAuth 2.0 provider, API, and client application conforms to RFC 6749. This authentication process is known as the [OAuth 2.0 dance](oauth-dance-about).

Mule OAuth 2.0 Provider supports all [grant types](oauth-grant-types-about). The entity that requests access to a resource protected by the Mule OAuth 2.0 Access Token Enforcement policy is a `Client`.

### Endpoints

You can call the following Mule OAuth 2.0 Provider endpoints in your API implementation:

![mule oauth provider](_images/mule-oauth-provider.png) 

| Purpose | Default Path | Description | 
|---|---|---|
| Token validation | /validate | Used to verify the validity of the token: whether the token is expired, revoked or fake. You can define more than one validation endpoint, each of them enforcing different scopes. For more information, see <Scopes>. | 
| Authorization | /authorize | Used to obtain a token when the client is running in a browser using a scripting language or when the client is a web server. | 
| Access | /access_token | Used when the client is owned by the same entity as Mule OAuth 2.0 Provider or when the client is the same entity as the protected resource owner. | 
| Token revocation | /revoke | [Optional] Used to revoke a valid token to render it invalid. | 

### Implementing Scopes

The OAuth 2.0 [scopes](https://datatracker.ietf.org/doc/html/rfc6749#page-23) enable you to further limit access to a resource protected by OAuth. You can define words, such as `READ` and `WRITE`, or others specific to your organization, such as `CONTRACTOR`, `PUBLIC`, `EMPLOYEES_ONLY`, and so on.

You can define scopes in three different places:

- 
In the universal set definition, `defaultScopes`, where you define all possible scopes:`<oauth2-provider:config scopes="CONTRACTOR, PUBLIC_READ, EMPLOYEES_ONLY, WRITE" > ... </oauth2-provider:config>`xml
- 
In the `/validate`validation endpoint, to enforce a particular subset of the previously defined scopes.
- 
In the Mule OAuth 2.0 Access Token Enforcement policy, where you can enforce scopes by specifying a space-separated list. Specifying more than one scope enforces the `AND`logic. If the token to be validated is associated with all of the requested scopes, the policy validates the token successfully.

Example of using scopes in Mule 4.2.x or later:

```
...
    <oauth2-provider:config name="external-oauth2-provider"
    							resourceOwnerSecurityProvider="resourceOwnerSecurityProvider"
    							clientSecurityProvider="clientSecurityProvider"
    							supportedGrantTypes="AUTHORIZATION_CODE,IMPLICIT,RESOURCE_OWNER_PASSWORD_CREDENTIALS,CLIENT_CREDENTIALS"
    							listenerConfig="https.listener"
    							scopes="CONTRACTOR, PUBLIC_READ, EMPLOYEES_ONLY, WRITE"
                                defaultScopes="CONTRACTOR, PUBLIC_READ, EMPLOYEES_ONLY, WRITE"
                                clientStore="clientObjectStore">
    		<oauth2-provider:token-config path="/access-token" tokenTtl="5" tokenTtlTimeUnit="SECONDS" tokenStore="tokenObjectStore">
                <oauth2-provider:refresh-token-strategy>
                    <oauth2-provider:single-refresh-token objectStore="refreshTokenObjectStore"/>
                </oauth2-provider:refresh-token-strategy>
            </oauth2-provider:token-config>
    		<oauth2-provider:authorization-config path="/authorize" authorizationCodeStore="authorizationCodeObjectStore"/>
    	</oauth2-provider:config>
        <flow name="validateToken">
            <http:listener path="/validate" config-ref="https.listener"/>
            <oauth2-provider:validate-token scopes="#[['PUBLIC_READ']]" config-ref="external-oauth2-provider" accessToken="#[attributes.queryParams.access_token]"/>
            <error-handler>
                <on-error-continue type="OAUTH2-PROVIDER:TOKEN_UNAUTHORIZED">
                    <set-payload value="UNAUTHORIZED_TOKEN"/>
                </on-error-continue>
            </error-handler>
        </flow>
...
```
xmlFor complete information, see [Mule OAuth 2.0 Server for Anypoint Platform](https://anypoint.mulesoft.com/exchange/org.mule.templates/api-gateway-oauth2-provider/).

## Client Application Cache

To prevent any possible downtime of Mule OAuth 2.0 Provider due to errors when connecting to Anypoint Platform, the Mule OAuth client store caches each valid client application for which a token is requested.

In the rare instance that the provider requests a new token when there is no connection available, the client store falls back to cache. The entries expire in 30 days, which is the default setting. To ensure service availability in case of a restart or lack of connection to Anypoint Platform, you can configure this range to persist the cache locally.

In case a client application for which a token already exists in the client store is removed from Anypoint Platform,
the client store removes the client from the cache on the next token request, mirroring the platform status. The mechanism that caches the result of a successful token validation is part of the [Mule OAuth 2.0 Access Token Enforcement policy](../../mule-gateway/policies-included-oauth-access-token-enforcement).

### Customizing the Client Application Cache Mechanism

You can customize the default values of the cache mechanism in Mule 4.2.0 and later. The object store has two configurable properties:

| Property Name | Definition | 
|---|---|
| 
 | Defines whether the caching mechanism must persist locally. The default value is  | 
| 
 | Represents how many days each client application must be cached by the OAuth Server.
You can specify any positive floating-point number for this value. The default value is  |