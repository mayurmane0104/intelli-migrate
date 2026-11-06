# Meeting Prerequisites for OAuth 2.0 Policies in API Manager | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/about-configure-api-for-oauth](https://docs.mulesoft.com/api-manager/latest/about-configure-api-for-oauth)

---

Query parameter

# Meeting Prerequisites for OAuth 2.0 Policies in API Manager

OAuth 2.0 token enforcement in Anypoint API Manager depends on platform setup, runtime configuration, and API metadata before callers can access protected endpoints. You grant API permissions, attach the OAuth policy to the API instance, register a client application, and use an OAuth 2.0 provider that issues and validates tokens for that client. For RAML-based APIs, define a security scheme when you want API Console to support the OAuth flow; RAML or OAS declarations alone do not attach the policy to the instance.

## Platform and Runtime Prerequisites

- 
Permissions to create or manage APIs 
- 
The OAuth 2.0 policy applied to the API instance so the resource is protected 
- 
A client application created in API Platform and registered to the API instance 
- 
An OAuth 2.0 provider that issues a token from the client credentials and validates it - 
If you use the Mule OAuth 2.0 provider, configure the runtime with the organization credentials 
 
- 
- 
For RAML-based API instances, specify a security scheme in the RAML when you use API Console with OAuth dance capabilities 

## Send Access Tokens to Protected Resources

When a resource is protected by an OAuth token enforcement policy, every request must include an OAuth token as a query parameter or in an authorization header. Use either placement consistently; do not send the token in both places at once.

| Places to include Token | Example | Notes | 
|---|---|---|
| 
 | Included as part of the URI | |
| Authorization header | 
 | The header consists of a key:value pair, where Authorization is the key and the value is composed as follows:
  | 

## Declare OAuth Protection in RAML

For RAML-based API instances, mark resources and methods as secured by OAuth so API Console reflects the intended protection.

| Declaring OAuth Token Enforcement in your RAML or OAS definition does not apply the policy to the API instance. | 

In the `securitySchemes` definition, set URIs for authorization and the access token.
Add `securedBy` on each resource and method you want to secure.

```
#%RAML 1.0
title: Interop Testing
version: v1.0
baseUri: http://127.0.0.1:8081/api
...
securitySchemes:
  oauth_2_0:
        description: |
            Mule OAuth 2.0.
        type: OAuth 2.0
        describedBy:
            headers:
                Authorization:
                    description: |
                      Used to send a valid OAuth 2 access token. Do not use
                      with the "access_token" query string parameter.
                    type: string
            queryParameters:
                access_token:
                    description: |
                      Used to send a valid OAuth 2 access token. Do not use together with
                      the "Authorization" header
                    type: string
            responses:
                401:
                    description: |
                        Bad or expired token.
                403:
                    description: |
                        Bad OAuth request.
        settings:
          authorizationUri: http://0.0.0.0:8081/authorize
          accessTokenUri: http://0.0.0.0:8081/access-token
          authorizationGrants: [authorization_code, password, client_credentials, implicit]
...
/users:
  get:
    securedBy: [oauth_2_0]
```
yaml## See Also

- 
[RAML securitySchemes](https://github.com/raml-org/raml-spec/blob/master/versions/raml-10/raml-10.md#oauth-20)